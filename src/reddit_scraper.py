import os
import praw
from urllib.parse import urlparse
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(
    dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"),
    override=True
)

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")

print("⚙ CLIENT_ID loaded:", CLIENT_ID is not None)
print("⚙ CLIENT_SECRET loaded:", CLIENT_SECRET is not None)
print("⚙ USER_AGENT raw:", repr(USER_AGENT))

def fetch_user_content(profile_url):
    if not CLIENT_ID or not CLIENT_SECRET or not USER_AGENT:
        raise RuntimeError("Missing Reddit credentials in `.env`.")
    username = Path(urlparse(profile_url).path.rstrip("/")).name
    reddit = praw.Reddit(
        client_id=CLIENT_ID.strip(),
        client_secret=CLIENT_SECRET.strip(),
        user_agent=USER_AGENT.strip()
    )
    redditor = reddit.redditor(username)

    posts = [
        {
            "text": submission.title + "\n\n" + submission.selftext,
            "permalink": f"https://www.reddit.com{submission.permalink}"
        }
        for submission in redditor.submissions.new(limit=50)
    ]
    comments = [
        {
            "text": comment.body,
            "permalink": f"https://www.reddit.com{comment.permalink}"
        }
        for comment in redditor.comments.new(limit=100)
    ]

    return posts, comments, username
