Project Title

AI YouTube Comment Auto-Reply Bot :“AI + GenAI + Lightweight Agentic AI system for YouTube comment automation using LLM-based response generation and API orchestration.”

Description

AI-based YouTube chatbot that automatically reads comments, classifies them, and generates context-aware devotional replies using LLM with memory and scheduling.

Tech Stack
Python
YouTube Data API v3
HuggingFace Inference API
Mistral-7B LLM
Flask (keep-alive server)
Schedule (automation)
JSON (memory storage)
Render (deployment)

Features
AI-powered smart replies
Context-based responses (Ram / Krishna / Sai / Shani)
Duplicate reply prevention
Scheduled execution (every 6 hours)
Cloud deployment (24/7 running)
Lightweight memory system (JSON-based)


Setup Commands 
cd youtube-ai-bot
pip install -r requirements.txt
python bot.py

🌐 Deployment
Deployed on Render Background Worker
Auto runs every 6 hours
No manual execution needed

🔐 Environment Variables
HF_API_KEY=your_key
CHANNEL_ID=your_channel
BOT_NAME=your_bot_name

📌 Architecture
Fetch YouTube comments
Classify comment type
Detect video context
Generate AI reply
Prevent duplicates
Post reply via API
