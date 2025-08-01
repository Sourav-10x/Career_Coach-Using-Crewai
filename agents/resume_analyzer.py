from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(text):
    prompt = f"""
You are a career coach. Analyze the following resume text and return:

1. Candidate's field or domain
2. Key technical and soft skills
3. Years of experience or level (e.g., entry-level, mid-level, senior)

Resume Text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=800
    )
    return response.choices[0].message.content.strip()
