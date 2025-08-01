# career_coach_crew.py

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from utils.pdf_parser import extract_text_from_pdf
from langchain.chat_models import ChatOpenAI

# Load environment
load_dotenv()

# Shared OpenAI LLM instance
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# Load resume text
resume_path = "SOURAV_MAHANTY_Resume.pdf"
resume_text = extract_text_from_pdf(resume_path)

# ------------------------ AGENTS ------------------------
resume_agent = Agent(
    role="Resume Analyzer",
    goal="Analyze resume and extract domain, key skills, and experience level",
    backstory="You are an expert in career coaching, helping candidates evaluate their own resumes.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

skill_agent = Agent(
    role="Skill Matcher",
    goal="Identify skill gaps for a Data Analyst role compared to the resume",
    backstory="You help students identify what's missing from their profile to target specific job roles.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

job_agent = Agent(
    role="Job Recommender",
    goal="Recommend job roles based on the resume content",
    backstory="You know the current market and suggest job roles that best suit a candidate's profile.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

course_agent = Agent(
    role="Course Recommender",
    goal="Suggest online courses to close the candidate's skill gaps",
    backstory="You are well-versed with courses from Coursera, Udemy, and edX.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# ------------------------ TASKS ------------------------
task1 = Task(
    description="Analyze the candidate's resume text and extract their domain, technical and soft skills, and experience level.",
    agent=resume_agent,
    expected_output="Structured summary including domain, skills, and experience"
)

task2 = Task(
    description="Compare the candidate's skills with those required for a 'Data Analyst' role. Return matched and missing skills, and improvement suggestions.",
    agent=skill_agent,
    expected_output="Matched Skills, Missing Skills, Suggestions"
)

task3 = Task(
    description="Suggest 3-5 job roles that fit the candidate's skills and experience.",
    agent=job_agent,
    expected_output="Recommended job titles"
)

task4 = Task(
    description="Recommend 1-2 online courses per missing skill from Coursera, Udemy, or edX.",
    agent=course_agent,
    expected_output="Courses listed under each missing skill"
)

# ------------------------ CREW ------------------------
crew = Crew(
    agents=[resume_agent, skill_agent, job_agent, course_agent],
    tasks=[task1, task2, task3, task4],
    verbose=True
)

# ------------------------ RUN ------------------------
print("\n🚀 Starting CrewAI career coaching session...")
result = crew.kickoff()
print("\n Final Output:\n")
print(result)