import os
import re
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from src.utils import clean_text, chunk_text

load_dotenv()
llm = ChatGoogleGenerativeAI(
    model=os.getenv("GOOGLE_GENAI_MODEL", "gemini-2.0-flash"),
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert user‑researcher."),
    ("human",
     "Here is all content from Reddit user {username}, including quotes with permalinks:\n\n"
     "{content_chunk}\n\n"
     "Generate **one clean user-persona** in markdown, using this exact structure:\n"
     "Name: <username>\n"
     "Age: <estimated or N/A>\n"
     "Occupation: <estimated or N/A>\n"
     "Status: <estimated or N/A>\n"
     "Location: <estimated or N/A>\n"
     "Tier: <estimated or N/A>\n"
     "Archetype: <estimated or N/A>\n\n"
     "### Interests\n- **Label**: \"Exact quote\" ([permalink])\n\n"
     "### Personality Traits\n- **Trait**: Explanation if needed.\n\n"
     "### Values & Motivations\n- **Value**: Explanation.\n\n"
     "### Goals / Pain Points\n- **Goal or Pain Point**: explanation.\n\n"
     "### Communication Style\n- **Style**: explanation.\n\n"
     "DO NOT include any other sections, duplicates, or drafts—just this final version.")
])

def build_persona(posts, comments, username: str) -> str:
    entries = posts + comments
    formatted = "\n\n".join(
        f"> \"{clean_text(e['text'])}\" ([{e['permalink']}]({e['permalink']}))"
        for e in entries if e.get("text") and e.get("permalink")
    )

    chunks = chunk_text(formatted, max_chars=15000)
    full_content = "\n\n".join(chunks)

    response = (prompt | llm).invoke({
        "username": username,
        "content_chunk": full_content
    })

    return response.content.strip()
