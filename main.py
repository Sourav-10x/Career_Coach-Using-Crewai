from utils.pdf_parser import extract_text_from_pdf
from agents.resume_analyzer import analyze_resume
from agents.skill_matcher import match_skills
from agents.job_recommender import recommend_jobs
from agents.course_recommender import recommend_courses



# Step 1: Extract resume text
resume_path = "SOURAV_MAHANTY_Resume.pdf"
resume_text = extract_text_from_pdf(resume_path)

# Step 2: Analyze resume
analysis = analyze_resume(resume_text)
print("\n Resume Analysis:\n", analysis)

# Step 3: Match skills for a target job
target_job = "Data Analyst"
skill_gap_report = match_skills(analysis, target_job)
print(f"\n Skill Gap Report for '{target_job}':\n", skill_gap_report)

# Step 4: Recommend best-fit job roles
print("\n Recommending best-fit job roles...")
job_suggestions = recommend_jobs(analysis)

print("\n Recommended Roles:\n")
print(job_suggestions)

# Step 5: Recommend courses for missing skills
print("\n Recommending courses to close skill gaps...")
course_recos = recommend_courses(skill_gap_report)

print("\n Course Recommendations:\n")
print(course_recos)


