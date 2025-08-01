from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def match_skills(candidate_skills, target_job_role):
    prompt = f"""
You are a career advisor AI.

Compare the candidate's skills with the required skills for the job role: {target_job_role}

Candidate's Skills:
{candidate_skills}

Return:
1.  Matched Skills
2.  Missing Skills (Skill Gaps)
3.  Suggest how to bridge the skill gaps (e.g., technologies, tools, techniques)

Format output in clean bullet points.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=1000
    )

    return response.choices[0].message.content.strip()
