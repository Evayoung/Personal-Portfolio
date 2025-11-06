from typing import List, Dict, Any

# Define the structure for a single skill entry
SkillEntry = Dict[str, Any]

# Skill data for the "My Journey / Skills" section
SKILLS_DATA: List[SkillEntry] = [
    {
        "name": "Python / Reflex / Flet",
        "proficiency": 85,
        "type": "Frontend (Web)",
        "color": "linear-gradient(90deg, hsl(190 80% 60%), hsl(190 80% 60%), hsl(220 30% 28%) 100%)",
    },
    {
        "name": "FastAPI / SQLAlchemy / Pydantic",
        "proficiency": 95,
        "type": "Backend",
        "color": "linear-gradient(90deg, hsl(190 80% 60%), hsl(190 80% 60%), hsl(220 30% 28%) 100%)",
    },
    {
        "name": "PyQt / PySide / Kivy",
        "proficiency": 90,
        "type": "Desktop",
        "color": "linear-gradient(90deg, hsl(190 80% 60%), hsl(190 80% 60%), hsl(220 30% 28%) 100%)",
    },
    {
        "name": "KivyMD / Flet / Buildozer",
        "proficiency": 90,
        "type": "Mobile",
        "color": "linear-gradient(90deg, hsl(190 80% 60%), hsl(190 80% 60%), hsl(220 30% 28%) 100%)",
    },
    {
        "name": "Python",
        "proficiency": 95,
        "type": "Language",
        "color": "linear-gradient(90deg, hsl(190 80% 60%), hsl(190 80% 60%), hsl(220 30% 28%) 100%)",
    },
    {
        "name": "Rust (Experimental)",
        "proficiency": 65,
        "type": "Language",
        "color": "linear-gradient(90deg, hsl(190 80% 60%), hsl(190 80% 60%), hsl(220 30% 28%) 100%)",
    },
    {
        "name": "LangChain / AI API Integration",
        "proficiency": 70,
        "type": "AI",
        "color": "linear-gradient(90deg, hsl(190 80% 60%), hsl(190 80% 60%), hsl(220 30% 28%) 100%)",
    },
    {
        "name": "TensorFlow / OpenCV / YOLO",
        "proficiency": 65,
        "type": "Machine Learning",
        "color": "linear-gradient(90deg, hsl(190 80% 60%), hsl(190 80% 60%), hsl(220 30% 28%) 100%)",
    },
    {
        "name": "AWS / GCP / Render / Docker",
        "proficiency": 70,
        "type": "DevOps",
        "color": "linear-gradient(90deg, hsl(190 80% 60%), hsl(190 80% 60%), hsl(220 30% 28%) 100%)",
    },
    {
        "name": "SQL / NoSQL / VectorDB",
        "proficiency": 75,
        "type": "Database",
        "color": "linear-gradient(90deg, hsl(190 80% 60%), hsl(190 80% 60%), hsl(220 30% 28%) 100%)",
    },
]


# Quick facts/stats for the 'My Journey' section
STATS_DATA: List[Dict[str, str]] = [
    {"label": "Projects Completed", "value": "20+", "icon": "package"},
    {"label": "Years Experience", "value": "5+", "icon": "clock"},
]
