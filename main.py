#!/usr/bin/env python3
import argparse
from pathlib import Path
from src.reddit_scraper import fetch_user_content
from src.persona_builder import build_persona

def parse_cli():
    parser = argparse.ArgumentParser(description="Generate a Reddit user persona")
    parser.add_argument("profile_url", help="Full Reddit profile URL")
    parser.add_argument("--output", "-o", help="Output path for persona `.txt`")
    return parser.parse_args()

def main():
    args = parse_cli()
    posts, comments, username = fetch_user_content(args.profile_url)
    persona_markdown = build_persona(posts, comments, username)

    out_path = Path(args.output or f"data/{username}_persona.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(persona_markdown, encoding="utf-8")

    print(f"✅ Persona written to {out_path.resolve()}")

if __name__ == "__main__":
    main()
