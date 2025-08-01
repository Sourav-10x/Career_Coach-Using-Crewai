**💼 Career Coach CrewAI – Your AI-Powered Career Advisor**

Career Coach CrewAI is a multi-agent AI application that helps students and professionals make informed career decisions. By uploading a resume and entering a target job role, the system intelligently analyzes your experience, evaluates your fit, highlights missing skills, and suggests personalized career and learning paths. It's your AI mentor — focused on your growth.

**🤖 What Makes It Smart?**

This project uses CrewAI to orchestrate four specialized LLM-powered agents that work in sequence:

📄 Resume Analyzer: Extracts your domain, skills, and experience from a PDF

🎯 Skill Matcher: Compares your current skills with a target job role

🧠 Job Recommender: Suggests job roles that match your background

📚 Course Finder: Recommends online courses to fill identified skill gaps

Each agent is powered by OpenAI (GPT-3.5/4o mini), enabling deep understanding, reasoning, and communication — just like a human career counselor, but faster and more scalable.

🧩 Modular Yet Simple
The entire logic is executed through a single file (crew.py) that initializes agents, assigns tasks, and generates a structured PDF report using reportlab. Resume parsing is handled using PyMuPDF in a helper file (pdf_parser.py). You can interact with it through the terminal or easily integrate it into a web interface using Flask or Gradio for a live demo experience.

**⚙️ Tech Stack at a Glance**

Component	Tool/Library
🤖 Agent System :	CrewAI

🔍 LLM Backend:	OpenAI GPT-3.5/4 (langchain_openai)

📄 PDF Parsing:	PyMuPDF (fitz)

📝 Report Output:	reportlab (PDF generation)

💻 Frontend (opt):	Flask / Gradio(If you want you can integrate)


**🚀 Why It Stands Out**

✅ Real-world use case: helps tailor resumes to job roles

🔁 Fully extensible: add more agents (e.g., LinkedIn scraping, cover letter writer)

🧠 Multi-agent collaboration shows true potential of agentic AI

📝 Generates clean, personalized, downloadable career reports

🌐 Can be deployed or integrated into student portals, LMS, or career dashboards

Whether you're a student trying to align your profile with industry demands or a professional seeking a promotion roadmap — Career Coach CrewAI delivers clear, actionable insights using the power of language models and agent architecture.

