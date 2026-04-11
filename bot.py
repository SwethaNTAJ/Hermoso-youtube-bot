import json,os
import requests
import time
import random
import schedule
# from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build 
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

HF_API_KEY = os.getenv("HF_API_KEY")
CHANNEL_ID = os.getenv("CHANNEL_ID")
BOT_NAME = os.getenv("BOT_NAME")

# ---------------- 🔧 CONFIG ----------------
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"] 
  
MAX_COMMENTS = 100

HF_API_KEY = "HF_API_KEY"
HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

BOT_NAME = "BOT_NAME"

# ---------------- 🔐 AUTH (RUN ONCE) ----------------
# flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
# credentials = flow.run_local_server(port=8080)
# youtube = build("youtube", "v3", credentials=credentials)

from google.oauth2.credentials import Credentials

credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
youtube = build("youtube", "v3", credentials=credentials)

# ---------------- 🧠 FUNCTIONS ----------------
def classify_comment(comment):
    c = comment.lower()

    if "upload" in c or "episode" in c or "pettandi" in c:
        return "request"
    elif "?" in c:
        return "question"
    elif any(word in c for word in ["waste", "bad", "darunam", "fake", "worst"]):
        return "negative"
    else:
        return "general"

def detect_video_god(title):
    t = title.lower()

    if "ram" in t:
        return "ram"
    elif "shani" in t:
        return "shani"
    elif "sai" in t:
        return "sai"
    elif "krishna" in t:
        return "krishna"
    else:
        return "general"

def fallback_reply(comment, ctype, video_god):
    c = comment.lower()

    if "all episodes" in c:
        return "👍 Tappakunda anni episodes upload cheyadaniki try chestam!"

    if video_god == "ram":
        return random.choice(["🙏 Jai Shri Ram!", "🙏 Jai Sita Ram!"])
    elif video_god == "shani":
        return random.choice(["🙏 Jai Shani Dev!"])
    elif video_god == "sai":
        return random.choice(["🙏 Om Sai Ram!"])
    elif video_god == "krishna":
        return random.choice(["🙏 Hare Krishna!"])

    if ctype == "request":
        return "👍 Tappakunda upload chestam soon!"
    elif ctype == "negative":
        return "🙏 Mee opinion ki dhanyavadalu."
    elif ctype == "question":
        return "😊 Soon explain chestam!"
    else:
        return "🙏 Dhanyavadalu!"

def generate_reply(comment, ctype, video_god):
    try:
        API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
        headers = {"Authorization": f"Bearer {HF_API_KEY}"}

        prompt = f"""
Short Telugu devotional reply (1 line).

Video God: {video_god}
Comment type: {ctype}

Comment: {comment}
Reply:
"""

        payload = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": 40, "temperature": 0.9}
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()

        reply = result[0]["generated_text"].replace(prompt, "").strip()
        reply = reply.split("\n")[0]

        if not reply or len(reply) < 3:
            return fallback_reply(comment, ctype, video_god)

        return reply

    except:
        return fallback_reply(comment, ctype, video_god)

# ---------------- 🔁 MAIN BOT FUNCTION ----------------
def run_bot():

    print("\n🔁 Running bot...\n")

    # Load JSON
    try:
        with open("replied_comments.json", "r") as f:
            replied_comments = json.load(f)
    except:
        replied_comments = []

    # 🔥 PAGINATION LOOP
    next_page_token = None

    while True:

        request = youtube.commentThreads().list(
            part="snippet,replies",
            allThreadsRelatedToChannelId=CHANNEL_ID,
            maxResults=100,
            order="time",
            pageToken=next_page_token
        )

        response = request.execute()

        for item in response.get("items", []):

            comment_id = item["snippet"]["topLevelComment"]["id"]
            comment_text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            video_id = item["snippet"]["topLevelComment"]["snippet"]["videoId"]

            if comment_id in replied_comments:
                continue

            # Check already replied
            already_replied = False
            if "replies" in item:
                for reply in item["replies"]["comments"]:
                    if BOT_NAME.lower() in reply["snippet"]["authorDisplayName"].lower():
                        already_replied = True
                        break

            if already_replied:
                replied_comments.append(comment_id)
                continue

            # Get video title
            video_details = youtube.videos().list(
                part="snippet",
                id=video_id
            ).execute()

            video_title = video_details["items"][0]["snippet"]["title"]
            video_god = detect_video_god(video_title)

            ctype = classify_comment(comment_text)
            reply_text = generate_reply(comment_text, ctype, video_god)

            print("💬", comment_text)
            print("🤖", reply_text)

            youtube.comments().insert(
                part="snippet",
                body={
                    "snippet": {
                        "parentId": comment_id,
                        "textOriginal": reply_text
                    }
                }
            ).execute()

            replied_comments.append(comment_id)
            time.sleep(2)

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    # Save JSON
    with open("replied_comments.json", "w") as f:
        json.dump(replied_comments, f)

    print("✅ Cycle Done")

# ---------------- ⏰ SCHEDULER ----------------
schedule.every(1).minutes.do(run_bot)

print("🚀 Bot started (runs every 1 mins)...")

while True:
    schedule.run_pending()
    time.sleep(1) 