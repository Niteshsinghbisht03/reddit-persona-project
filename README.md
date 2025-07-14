# 🧠 Reddit Persona Generator

Generate structured user personas from any public Reddit profile using LLMs like **Gemini (via LangChain)**.

This tool scrapes a Reddit user's posts and comments, summarizes their behavior and interests using an LLM, and outputs a clean, markdown-formatted persona file.

---

## ✨ Features

- 🔍 Scrapes up to 50 posts and 100 comments from a given Reddit user
- 🧠 Uses Google Gemini (`gemini-2.0-flash`) via LangChain for persona generation
- 📄 Outputs a **clean, single** markdown-formatted `.txt` file
- ✅ Automatically includes quotes and source links (permalinks)
- 🔒 Environment variables managed with `.env` (no hardcoded secrets)

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/reddit-persona-project.git
cd reddit-persona-project
```

### 2. Set Up Virtual Environment
```
python -m venv .venv
source .venv/bin/activate  
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Add Your API Keys to .env

Create a .env file in the project root:
```
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=script:reddit-persona:1.0 (by u/yourusername)

GOOGLE_API_KEY=your_google_api_key
GOOGLE_GENAI_MODEL=gemini-2.0-flash
```

### 5. Run
```
python main.py https://www.reddit.com/user/kojied/ -o data/kojied_persona.txt
```

