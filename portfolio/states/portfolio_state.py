# ============================================
# FILE: states/portfolio_state.py (FIXED)
# ============================================
import reflex as rx
from typing import List, Dict, Any

# --- MOCK DATA ---
PROJECTS_DATA: List[Dict[str, Any]] = [
    {
        "id": "qrive_platform",
        "title": "QRive, Verified Business Identity Platform",
        "category": "Full-Stack / SaaS",
        "description": (
            "A professional SaaS platform enabling businesses to create verified digital hubs accessible via QR codes. "
            "Each hub showcases trusted details like verified bank accounts, social links, and business profiles to build customer trust "
            "and prevent fraud. Built with Reflex for the frontend and FastAPI for the backend."
        ),
        "tech_stack": ["Reflex", "FastAPI", "PostgreSQL", "Render", "Python"],
        "image_url": "/image1.jpg",
        "live_demo_url": "#",
        "code_url": "#",
        "project": "featured",
    },
    {
        "id": "church_population_server",
        "title": "Church Population Analytics Server",
        "category": "Backend / Data",
        "description": (
            "A FastAPI-powered data server for recording and analyzing demographic data from church programs. "
            "It tracks population estimates, gender, and age groups across multiple program types with secure query endpoints and role-based access control."
        ),
        "tech_stack": ["FastAPI", "PostgreSQL", "SQLAlchemy", "Python", "Pydantic"],
        "image_url": "/image2.jpg",
        "live_demo_url": "#",
        "code_url": "#",
        "project": "",
    },
    {
        "id": "voice_assistant_learning_app",
        "title": "Bi-Directional Voice Assistance Learning App",
        "category": "AI/Accessibility",
        "description": (
            "An intelligent bi-directional voice learning system designed for the visually impaired. "
            "The app enables seamless two-way interaction using natural speech recognition and speech synthesis, "
            "allowing users to learn, respond, and navigate without visual aid. Built with real-time audio streaming "
            "and local/offline inference capabilities."
        ),
        "tech_stack": [
            "FastAPI",
            "SpeechRecognition",
            "TTS (gTTS/Pyttsx3)",
            "KivyMD",
            "SQLite"
        ],
        "image_url": "/hero-bg.jpg",
        "live_demo_url": "#",
        "code_url": "#",
        "project": "featured",
    },
    {
        "id": "steganography_tool",
        "title": "Image Steganography Desktop Tool",
        "category": "Desktop / Security",
        "description": (
            "A Python desktop application for securely embedding and extracting hidden messages within images. "
            "Built with PyQt for a sleek UI and includes file encryption features for enhanced data security."
        ),
        "tech_stack": ["PyQt", "Pillow", "Python", "Cryptography"],
        "image_url": "/steg.png",
        "live_demo_url": "#",
        "code_url": "#",
        "project": "",
    },
    {
        "id": "backendforge_builder",
        "title": "BackendForge, FastAPI Builder System",
        "category": "Backend/Automation",
        "description": (
            "A code automation tool that scaffolds production-ready FastAPI backends instantly. "
            "BackendForge generates database models, CRUD routes, and authentication logic automatically "
            "from schema definitions, improving development speed and enforcing best practices."
        ),
        "tech_stack": [
            "FastAPI",
            "SQLAlchemy",
            "Pydantic",
            "Reflex",
            "PostgreSQL"
        ],
        "image_url": "/backendforge.png",
        "live_demo_url": "#",
        "code_url": "#",
        "project": "featured",
    }
]

class UIState(rx.State):
    """Global UI state for handling responsive menus and modals."""
    menu_open: bool = False

    def toggle_menu(self):
        self.menu_open = not self.menu_open


# --- STATE MANAGEMENT (FIXED) ---
class ProjectState(rx.State):
    """Manages the portfolio data and the hover state for all project cards."""
    
    # Store the currently hovered project ID (simpler approach)
    hovered_project_id: str = ""

    def set_hover(self, project_id: str, is_hovered: bool):
        """
        Sets the hover status for a specific project card.
        
        Args:
            project_id: The ID of the project being hovered
            is_hovered: True when mouse enters, False when it leaves
        """
        if is_hovered:
            self.hovered_project_id = project_id
        else:
            # Only clear if this was the hovered project
            if self.hovered_project_id == project_id:
                self.hovered_project_id = ""
    
    def is_project_hovered(self, project_id: str) -> bool:
        """
        Check if a specific project is currently hovered.
        
        Args:
            project_id: The ID of the project to check
            
        Returns:
            True if this project is hovered, False otherwise
        """
        return self.hovered_project_id == project_id

