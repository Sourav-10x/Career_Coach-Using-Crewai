from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def recommend_jobs(resume_summary):
    prompt = f"""
You are an intelligent AI career advisor.

Based on the following resume analysis, suggest 3 to 5 **most suitable job roles** for this candidate. Include roles that match their skills, experience level, and field.

Resume Summary:
{resume_summary}

Format output like:
- 🔹 Job Role 1
- 🔹 Job Role 2
- 🔹 Job Role 3
...
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=600
    )
    return response.choices[0].message.content.strip()
