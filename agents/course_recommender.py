from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def recommend_courses(skill_gap_report):
    prompt = f"""
You are an AI career mentor.

Based on the following skill gap report, suggest **top 1-2 online courses per missing skill**. Use platforms like Coursera, Udemy, or edX.

Skill Gap Report:
{skill_gap_report}

Format:
-  Skill: <name>
  -  Course 1: <Title> - (Platform)
  -  Course 2: <Title> - (Platform)
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )
    return response.choices[0].message.content.strip()
