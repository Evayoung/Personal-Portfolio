import reflex as rx
from ..styles import animation

def service_card(icon: str, title: str, description: str,) -> rx.Component:
    """Renders a single experience card with subtle styling."""
    return rx.vstack(
        rx.badge(rx.icon(f"{icon}", size=24), padding="0.5rem"),
        rx.heading(
            title, 
            size="4", 
            color="var(--fg)", 
            margin_y="0.5rem",
            _hover={
                "transform": "scale(1.03)",
                "color": "var(--primary)",
            }
        ),
        rx.text(description, font_size="12px", color="var(--fg)", opacity="0.6"),
        justify="start",
        padding="1rem",
        border_radius="var(--radius)",
        background="var(--card)",
        border="2px solid",
        border_color="var(--primary)",
        min_width="35%",
        spacing='1',
        style=animation.HOVER_EFFECTS["hover_card_soft"],
    )


# --- Main Section Component ---

def services_section() -> rx.Component:
    """
    Renders the 'My Journey' and 'My Skills' section.
    Uses the glass-morphism style for the main container.
    """
    return rx.section(
        rx.vstack(
            rx.heading(
                "My Services", 
                size=rx.breakpoints(initial="8", sm="9", md="9"),
                margin_bottom="1.5rem", 
                color="var(--fg)", 
                width="100%", 
                text_align="center"
                ),
            
            rx.hstack(
                rx.text(
                    "Comprehensive development solutions tailored to your technical needs, from backend infrastructure to AI integration.",
                    text_align="center",
                    width=rx.breakpoints(initial="100%", sm="70%", md="70%"),
                    font_size=rx.breakpoints(initial="15px", sm="16px", md="18px"),
                    color="var(--alt-fg)",
                    opacity="0.8",
                    margin_top="1rem",
                ),
                width="100%",
                justify="center",
            ),
            
            # --- Service Flex ---
            rx.grid(
                service_card(
                    "code",
                    "Backend Architecture & API Development",
                    "Designing and developing robust, scalable backend systems with FastAPI, Flask, and modern database solutions (SQL/NoSQL). Specialized in RESTful APIs, GraphQL, and microservices architecture.",
                ),
                service_card(
                    "brain",
                    "AI Agent & Automation System",
                    "Developing intelligent automation systems and AI-powered agents. Skilled in AI model integration, natural language processing, and workflow automation using modern LLM frameworks.",
                ),
                service_card(
                    "monitor",
                    "Web Systems Development",
                    "Building fast, interactive, and visually engaging web applications using Reflex, Flet, and FastHTML. Focused on crafting seamless user experiences with optimized performance and strong backend integration.",
                ),
                service_card(
                    "smartphone",
                    "Cross-Platform App Development",
                    "Creating responsive, cross-platform applications using Kivy/KivyMD, PyQt/PySide, Flet, and modern Python web frameworks like Reflex — with a strong focus on performance and user experience.",
                ),
                service_card(
                    "message_square",
                    "System Research & Technical Consulting",
                    "Providing in-depth technical analysis, system design consulting, and research-backed engineering solutions for complex software and AI projects.",
                ),
                service_card(
                    "database",
                    "Data Engineering & Analytics",
                    "Building data processing pipelines and analytics tools using Python, SQL, and modern data frameworks. Experienced in transforming raw data into actionable insights for decision-making.",
                ),
                service_card(
                    "cloud",
                    "DevOps & Cloud Deployment",
                    "Deploying and maintaining applications on AWS, GCP, and Render with Docker-based workflows. Focused on reliability, automation, and CI/CD integration.",
                ),
                width="100%",
                columns=rx.breakpoints(initial="1", sm="2"),
                gap="2rem",
                margin_top="2rem",
            ),
            
            width="100%",
            max_width="1200px",
            padding="2rem",
            
            
        ),
        width="100%",
        display="flex",
        align_items="center",
        justify_content="center",
        bg="var(--bg)",
        id="services",
    )
