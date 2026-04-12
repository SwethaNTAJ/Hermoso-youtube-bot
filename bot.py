# Some how this code strict way to replay like Hare Krishna means danyavadalu type 


# import json, os
# import requests
# import time
# import random
# import schedule
# from googleapiclient.discovery import build
# from google.oauth2.credentials import Credentials
# from dotenv import load_dotenv

# # ---------------- 🌐 FIX: WEB SERVER (REMOVE RENDER WARNING) ----------------
# from flask import Flask
# import threading

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Bot is running!"

# def run_server():
#     app.run(host="0.0.0.0", port=10000)

# threading.Thread(target=run_server).start()

# # ---------------- 🔐 ENV ----------------
# load_dotenv()

# HF_API_KEY = os.getenv("HF_API_KEY")
# CHANNEL_ID = os.getenv("CHANNEL_ID")
# BOT_NAME = os.getenv("BOT_NAME")

# SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
# HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

# # ---------------- 🔐 AUTH ----------------
# credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
# youtube = build("youtube", "v3", credentials=credentials)

# # ---------------- 🧠 FUNCTIONS ----------------
# def classify_comment(comment):
#     c = comment.lower()

#     if "upload" in c or "episode" in c or "pettandi" in c:
#         return "request"
#     elif "?" in c:
#         return "question"
#     elif any(word in c for word in ["waste", "bad", "darunam", "fake", "worst"]):
#         return "negative"
#     else:
#         return "general"

# def detect_video_god(title):
#     t = title.lower()

#     if "ram" in t:
#         return "ram"
#     elif "shani" in t:
#         return "shani"
#     elif "sai" in t:
#         return "sai"
#     elif "krishna" in t:
#         return "krishna"
#     else:
#         return "general"

# def fallback_reply(comment, ctype, video_god):
#     c = comment.lower()

#     if "all episodes" in c:
#         return "👍 Tappakunda anni episodes upload cheyadaniki try chestam!"

#     if video_god == "ram":
#         return random.choice(["🙏 Jai Shri Ram!", "🙏 Jai Sita Ram!"])
#     elif video_god == "shani":
#         return "🙏 Jai Shani Dev!"
#     elif video_god == "sai":
#         return "🙏 Om Sai Ram!"
#     elif video_god == "krishna":
#         return "🙏 Hare Krishna!"

#     if ctype == "request":
#         return "👍 Tappakunda upload chestam soon!"
#     elif ctype == "negative":
#         return "🙏 Mee opinion ki dhanyavadalu."
#     elif ctype == "question":
#         return "😊 Soon explain chestam!"
#     else:
#         return "🙏 Dhanyavadalu!"

# def generate_reply(comment, ctype, video_god):
#     try:
#         API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
#         headers = {"Authorization": f"Bearer {HF_API_KEY}"}

#         prompt = f"""
# Short Telugu devotional reply (1 line).

# Video God: {video_god}
# Comment type: {ctype}

# Comment: {comment}
# Reply:
# """

#         payload = {
#             "inputs": prompt,
#             "parameters": {"max_new_tokens": 40, "temperature": 0.9}
#         }

#         response = requests.post(API_URL, headers=headers, json=payload)
#         result = response.json()

#         reply = result[0]["generated_text"].replace(prompt, "").strip()
#         reply = reply.split("\n")[0]

#         if not reply or len(reply) < 3:
#             return fallback_reply(comment, ctype, video_god)

#         return reply

#     except:
#         return fallback_reply(comment, ctype, video_god)

# # ---------------- 🔁 MAIN BOT ----------------
# def run_bot():

#     print("\n🔁 Running bot...\n")

#     try:
#         with open("replied_comments.json", "r") as f:
#             replied_comments = json.load(f)
#     except:
#         replied_comments = []

#     next_page_token = None

#     while True:

#         request = youtube.commentThreads().list(
#             part="snippet,replies",
#             allThreadsRelatedToChannelId=CHANNEL_ID,
#             maxResults=100,
#             order="time",
#             pageToken=next_page_token
#         )

#         response = request.execute()

#         for item in response.get("items", []):

#             comment_id = item["snippet"]["topLevelComment"]["id"]
#             comment_text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
#             video_id = item["snippet"]["topLevelComment"]["snippet"]["videoId"]

#             if comment_id in replied_comments:
#                 continue

#             already_replied = False
#             if "replies" in item:
#                 for reply in item["replies"]["comments"]:
#                     if BOT_NAME.lower() in reply["snippet"]["authorDisplayName"].lower():
#                         already_replied = True
#                         break

#             if already_replied:
#                 replied_comments.append(comment_id)
#                 continue

#             video_details = youtube.videos().list(
#                 part="snippet",
#                 id=video_id
#             ).execute()

#             video_title = video_details["items"][0]["snippet"]["title"]
#             video_god = detect_video_god(video_title)

#             ctype = classify_comment(comment_text)
#             reply_text = generate_reply(comment_text, ctype, video_god)

#             print("💬", comment_text)
#             print("🤖", reply_text)

#             youtube.comments().insert(
#                 part="snippet",
#                 body={
#                     "snippet": {
#                         "parentId": comment_id,
#                         "textOriginal": reply_text
#                     }
#                 }
#             ).execute()

#             replied_comments.append(comment_id)
#             time.sleep(2)

#         next_page_token = response.get("nextPageToken")

#         if not next_page_token:
#             break

#     with open("replied_comments.json", "w") as f:
#         json.dump(replied_comments, f)

#     print("✅ Cycle Done")

# # ---------------- ⏰ SCHEDULER ----------------
# run_bot()  # run immediately

# schedule.every(6).hours.do(run_bot)

# print("🚀 Bot started (runs every 6 hours)...")

# while True:
#     schedule.run_pending()
#     time.sleep(1)




#  this code bit cool way to replay like Hare Krishna means Hare krishna  type 

import json, os
import requests
import time
import random
import schedule
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from dotenv import load_dotenv

# ---------------- 🌐 FIX: WEB SERVER ----------------
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_server():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_server).start()

# ---------------- 🔐 ENV ----------------
load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
CHANNEL_ID = os.getenv("CHANNEL_ID")
BOT_NAME = os.getenv("BOT_NAME")

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

# ---------------- 🔐 AUTH ----------------
credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
youtube = build("youtube", "v3", credentials=credentials)

# ---------------- 🧠 CLASSIFICATION ----------------
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

# ---------------- 🛕 GOD DETECTION (LIGHTWEIGHT) ----------------
def detect_video_god(comment):
    c = comment.lower()

    if "ram" in c:
        return "ram"
    elif "shani" in c:
        return "shani"
    elif "sai" in c:
        return "sai"
    elif "krishna" in c:
        return "krishna"
    else:
        return "general"

# ---------------- 🔁 SMART FALLBACK ----------------
def fallback_reply(comment, ctype, video_god):
    c = comment.lower()

    if "all episodes" in c:
        return random.choice([
            "👍 Tappakunda anni episodes upload chestam!",
            "🙏 Mee request consider chestam!",
            "📺 Soon full series upload chestam!"
        ])

    if video_god == "ram":
        return random.choice([
            "🙏 Jai Shri Ram!",
            "🙏 Jai Sita Ram!",
            "🙏 Sri Ram blessings meeku undali!"
        ])

    elif video_god == "shani":
        return random.choice([
            "🙏 Jai Shani Dev!",
            "🙏 Shani Bhagavan krupa undali!"
        ])

    elif video_god == "sai":
        return random.choice([
            "🙏 Om Sai Ram!",
            "🙏 Sai Baba blessings!"
        ])

    elif video_god == "krishna":
        return random.choice([
            "🙏 Hare Krishna!",
            "🙏 Radhe Krishna!"
        ])

    if ctype == "request":
        return random.choice([
            "👍 Tappakunda upload chestam!",
            "🙏 Mee request consider chestam!",
            "📌 Soon try chestam!"
        ])

    elif ctype == "negative":
        return random.choice([
            "🙏 Mee opinion ki dhanyavadalu.",
            "🙏 Mee feedback valuable.",
            "🙏 Improve avadaniki try chestam."
        ])

    elif ctype == "question":
        return random.choice([
            "😊 Soon explain chestam!",
            "🙏 Next videos lo clarify chestam!",
            "👍 Answer try chestam!"
        ])

    else:
        return random.choice([
            "🙏 Dhanyavadalu!",
            "❤️ Mee support chala mukhyam!",
            "🙏 Thanks for your support!"
        ])

# ---------------- 🤖 AI REPLY ----------------
def generate_reply(comment, ctype, video_god):
    try:
        API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
        headers = {"Authorization": f"Bearer {HF_API_KEY}"}

        prompt = f"""
You are a Telugu devotional YouTube admin.

Rules:
- Reply must be SHORT (1 line)
- Use Telugu + simple English
- Be natural, not repetitive
- Understand comment meaning
- Match VIDEO GOD: {video_god}
- request → say upload soon
- negative → calm reply
- devotional → blessings
- question → simple answer

Comment: {comment}

Reply:
"""

        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 40,
                "temperature": 1.1
            }
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()

        print("HF RAW:", result)  # debug

        reply = result[0]["generated_text"].replace(prompt, "").strip()
        reply = reply.split("\n")[0]

        if not reply or len(reply) < 3:
            return fallback_reply(comment, ctype, video_god)

        return reply

    except Exception as e:
        print("AI ERROR:", e)
        return fallback_reply(comment, ctype, video_god)

# ---------------- 🔁 MAIN BOT ----------------
def run_bot():

    print("\n🔁 Running bot...\n")

    try:
        with open("replied_comments.json", "r") as f:
            replied_comments = json.load(f)
    except:
        replied_comments = []

    next_page_token = None
    MAX_PAGES = 2
    page_count = 0

    while True:

        request = youtube.commentThreads().list(
            part="snippet,replies",
            allThreadsRelatedToChannelId=CHANNEL_ID,
            maxResults=20,
            order="time",
            pageToken=next_page_token
        )

        response = request.execute()

        new_count = 0

        for item in response.get("items", []):

            comment_id = item["snippet"]["topLevelComment"]["id"]
            comment_text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

            if comment_id in replied_comments:
                continue

            already_replied = False
            if "replies" in item:
                for reply in item["replies"]["comments"]:
                    if BOT_NAME.lower() in reply["snippet"]["authorDisplayName"].lower():
                        already_replied = True
                        break

            if already_replied:
                replied_comments.append(comment_id)
                continue

            video_god = detect_video_god(comment_text)
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
            new_count += 1

            time.sleep(2)

        if new_count == 0:
            print("😴 No new comments, stopping early")
            break

        next_page_token = response.get("nextPageToken")

        page_count += 1
        if page_count >= MAX_PAGES or not next_page_token:
            break

    with open("replied_comments.json", "w") as f:
        json.dump(replied_comments, f)

    print("✅ Cycle Done")

# ---------------- ⏰ SCHEDULER ----------------
run_bot()

schedule.every(6).hours.do(run_bot)

print("🚀 Bot started (runs every 6 hours)...")

while True:
    schedule.run_pending()
    time.sleep(1)
 










 

# this code bit funny,naughty typeRadhakrishnaaa....❤🤖  Krishna meeda nammakam undali 😉
# import json, os
# import requests
# import time
# import random
# import schedule
# from googleapiclient.discovery import build
# from google.oauth2.credentials import Credentials
# from dotenv import load_dotenv

# # ---------------- 🌐 FIX: WEB SERVER ----------------
# from flask import Flask
# import threading

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Bot is running!"

# def run_server():
#     app.run(host="0.0.0.0", port=10000)

# threading.Thread(target=run_server).start()

# # ---------------- 🔐 ENV ----------------
# load_dotenv()

# HF_API_KEY = os.getenv("HF_API_KEY")
# CHANNEL_ID = os.getenv("CHANNEL_ID")
# BOT_NAME = os.getenv("BOT_NAME")

# SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
# HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

# # ---------------- 🔐 AUTH ----------------
# credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
# youtube = build("youtube", "v3", credentials=credentials)

# # ---------------- 🧠 CLASSIFICATION ----------------
# def classify_comment(comment):
#     c = comment.lower()

#     if "upload" in c or "episode" in c or "pettandi" in c:
#         return "request"
#     elif "?" in c:
#         return "question"
#     elif any(word in c for word in ["waste", "bad", "darunam", "fake", "worst"]):
#         return "negative"
#     else:
#         return "general"

# # ---------------- 🛕 GOD DETECTION ----------------
# def detect_video_god(comment):
#     c = comment.lower()

#     if "ram" in c:
#         return "ram"
#     elif "shani" in c:
#         return "shani"
#     elif "sai" in c:
#         return "sai"
#     elif "krishna" in c:
#         return "krishna"
#     else:
#         return "krishna"   # 🔥 default Krishna style

# # ---------------- ❤️ AUTO LIKE ----------------
# def like_comment(comment_id):
#     try:
#         youtube.comments().setModerationStatus(
#             id=comment_id,
#             moderationStatus="published"
#         ).execute()

#         youtube.comments().markAsSpam(id=comment_id)  # ❌ remove this if not needed

#     except Exception as e:
#         print("Like Error:", e)

# # ---------------- 🔁 FALLBACK ----------------
# def fallback_reply(comment, ctype, video_god):

#     if "all episodes" in comment.lower():
#         return "😈 Krishna cheptunnadu... tondaralo anni episodes vastayi, wait cheyandi 😉"

#     if ctype == "negative":
#         return "😈 Krodham vaddu... Krishna ni gurthu chesukondi, anni baaguntayi 🙏"

#     if ctype == "request":
#         return "😈 Mee korika vinipinchindi... tondaralo upload chestam 😉"

#     if ctype == "question":
#         return "😈 Adbhutamaina prashna... next video lo cheptam 😎"

#     return random.choice([
#         "😈 Krishna meeda nammakam undali 😉",
#         "🙏 Hare Krishna! Mee support chala mukhyam",
#         "😈 Smile 😊 Krishna meeku blessings istunnadu"
#     ])

# # ---------------- 🤖 AI REPLY ----------------
# def generate_reply(comment, ctype, video_god):
#     try:
#         API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
#         headers = {"Authorization": f"Bearer {HF_API_KEY}"}

#         prompt = f"""
# You are Lord Krishna replying to YouTube comments 😈

# Rules:
# - 1 line only
# - Telugu + simple English
# - Slight attitude + wisdom
# - Friendly, calm, divine tone
# - No repetition

# Comment type: {ctype}
# Comment: {comment}

# Reply:
# """

#         payload = {
#             "inputs": prompt,
#             "parameters": {
#                 "max_new_tokens": 40,
#                 "temperature": 1.2
#             }
#         }

#         response = requests.post(API_URL, headers=headers, json=payload)
#         result = response.json()

#         reply = result[0]["generated_text"].replace(prompt, "").strip()
#         reply = reply.split("\n")[0]

#         if not reply or len(reply) < 3:
#             return fallback_reply(comment, ctype, video_god)

#         return reply

#     except Exception as e:
#         print("AI ERROR:", e)
#         return fallback_reply(comment, ctype, video_god)

# # ---------------- 🔁 MAIN BOT ----------------
# def run_bot():

#     print("\n🔁 Running bot...\n")

#     try:
#         with open("replied_comments.json", "r") as f:
#             replied_comments = json.load(f)
#     except:
#         replied_comments = []

#     next_page_token = None
#     MAX_PAGES = 2
#     page_count = 0

#     while True:

#         request = youtube.commentThreads().list(
#             part="snippet,replies",
#             allThreadsRelatedToChannelId=CHANNEL_ID,
#             maxResults=20,
#             order="time",
#             pageToken=next_page_token
#         )

#         response = request.execute()

#         new_count = 0

#         for item in response.get("items", []):

#             comment_id = item["snippet"]["topLevelComment"]["id"]
#             comment_text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

#             if comment_id in replied_comments:
#                 continue

#             already_replied = False
#             if "replies" in item:
#                 for reply in item["replies"]["comments"]:
#                     if BOT_NAME.lower() in reply["snippet"]["authorDisplayName"].lower():
#                         already_replied = True
#                         break

#             if already_replied:
#                 replied_comments.append(comment_id)
#                 continue

#             video_god = detect_video_god(comment_text)
#             ctype = classify_comment(comment_text)

#             reply_text = generate_reply(comment_text, ctype, video_god)

#             print("💬", comment_text)
#             print("🤖", reply_text)

#             # ✅ POST REPLY
#             youtube.comments().insert(
#                 part="snippet",
#                 body={
#                     "snippet": {
#                         "parentId": comment_id,
#                         "textOriginal": reply_text
#                     }
#                 }
#             ).execute()

#             # ❤️ AUTO LIKE
#             try:
#                 youtube.comments().setModerationStatus(
#                     id=comment_id,
#                     moderationStatus="published"
#                 ).execute()
#             except Exception as e:
#                 print("Like Error:", e)

#             replied_comments.append(comment_id)
#             new_count += 1

#             time.sleep(2)

#         if new_count == 0:
#             print("😴 No new comments, stopping early")
#             break

#         next_page_token = response.get("nextPageToken")

#         page_count += 1
#         if page_count >= MAX_PAGES or not next_page_token:
#             break

#     with open("replied_comments.json", "w") as f:
#         json.dump(replied_comments, f)

#     print("✅ Cycle Done")

# # ---------------- ⏰ SCHEDULER ----------------
# run_bot()

# schedule.every(6).hours.do(run_bot)

# print("🚀 Bot started (runs every 6 hours)...")

# while True:
#     schedule.run_pending()
#     time.sleep(1)

 