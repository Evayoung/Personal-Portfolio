import reflex as rx
from ..styles.data import SKILLS_DATA, STATS_DATA
from ..styles import animation

# --- Component: Stat Card ---

def experience_card(year: str, title: str, role: str, description: str,) -> rx.Component:
    """Renders a single experience card with subtle styling."""
    return rx.vstack(
        
        rx.badge(f"{year}"),
        rx.heading(role, size="4", color="var(--fg)", margin_y="0.5rem"),
        rx.text(title, font_size="14px", color="var(--primary)", opacity="0.6", font_weight="bold"),
        rx.text(description, font_size="12px", color="var(--fg)", opacity="0.6"),
        justify="start",
        padding="1rem",
        background="vard(--card)",
        border_left="2px solid",
        border_color="var(--primary)",
        min_width="100%",
        spacing='1',
        
        # style=animation.HOVER_EFFECTS["hover_card_soft"],
    )

# --- Custom Component: Glowing Skill Bar ---

def skill_bar(name: str, proficiency: int, type_name: str, color: str) -> rx.Component:
    """
    Renders a skill bar with a custom glowing progress effect based on the CSS keyframes.

    Args:
        name: The skill name (e.g., "Python").
        proficiency: The proficiency percentage (e.g., 95).
        icon_name: The name of the icon to display.
        color: The specific HSL color for the progress bar fill.
    """
    # Define the width and custom style for the animated fill component
    fill_style = {
        "width": f"{proficiency}%",
        "height": "100%",
        "background": color,
        "border_radius": "0.5rem",
        "position": "absolute",
        "top": 0,
        "left": 0,
        "z_index": 1,
        "box_shadow": f"0 0 10px {color}", # Add a subtle glow
        # Apply the custom CSS animation 'skill-fill'
        "animation": "skill-fill 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards",
        "transform": "translateX(-100%)", # Initial state for animation
    }

    return rx.vstack(
        # Top row: Name, Icon, and Percentage
        rx.hstack(
            # rx.icon(tag=icon_name, color=color, size=24),
            rx.text(name, font_size="14px", font_weight="200", color="var(--fg)"),
            rx.spacer(),
            rx.text(f"{type_name}", font_weight="400", color="var(--fg)", font_size="12px",),
            width="100%",
            align="center",
            margin_bottom="0.5rem",
            style=animation.PAGE_ANIMATIONS["page_fade_in_fast"],
        ),

        # Progress Bar Container (Muted background, holds the animated fill)
        rx.box(
            rx.box(**fill_style), # The animated progress fill
            width="100%",
            height="8px",
            background="var(--muted)",
            border_radius="0.5rem",
            overflow="hidden",
            position="relative",
            margin_bottom="1.5rem",
        ),
        
        width="100%",
        align_items="start",
        spacing="1",
    )


# --- Component: Stat Card ---

def stat_card(label: str, value: str) -> rx.Component:
    """Renders a single stat/fact card with subtle styling."""
    return rx.vstack(
        rx.heading(value, size="7", color="var(--primary)", margin_y="0.4rem"),
        rx.text(label, font_size="12px", color="var(--fg)", opacity="0.6", font_weight="400"),
        align="center",
        justify="center",
        padding="1rem",
        border_radius="var(--radius)",
        background="var(--card)",
        border="1px solid",
        border_color="var(--primary)",
        min_width="140px",
        width="45%",
        spacing="1",
        style=animation.HOVER_EFFECTS["hover_card_soft"],
    )

# --- Main Section Component ---

def about_section() -> rx.Component:
    """
    Renders the 'My Journey' and 'My Skills' section.
    Uses the glass-morphism style for the main container.
    """
    desc="Leading development of AI-powered web applications with React, Node.js, and machine learning integration."
    return rx.section(
        rx.vstack(
            rx.heading(
                "About Me", 
                size=rx.breakpoints(initial="8", sm="9", md="9"),
                margin_bottom="1.5rem", 
                color="var(--fg)", 
                width="100%", 
                text_align="center"
                ),
            
            rx.hstack(
                rx.text(
                    "Passionate developer with 5+ years of experience crafting innovative digital solutions."
                    "I blend technical expertise with creative problem-solving to build exceptional user experiences.",
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
            
            # --- Skills Grid ---
            rx.flex(
                rx.box(
                    rx.box(
                        rx.heading("My Journey", size="6", margin_bottom="1rem", color="var(--primary)"),
                        rx.text(
                            """Started as a curious developer who fell in love with the intersection of technology and creativity.
                            Over the years, i've evolved from building simple websites to architecting complex, AI-poered
                            applicaions that solve real-world problems.\n

                            When i'm not coding, you'll find me exploring the latest in AI research, contributing to
                            open-source projects, or mentoring upcoming developers. I belive in building not just softwares,
                            but experiences that truly matter.""",
                            color="var(--fg)",
                            font_size="14px",
                            opacity="0.8",
                            # margin_bottom="2rem",
                        ),
                        width="100%",
                        padding="1.5rem",
                        background="var(--card)",
                        border_radius="var(--radius)",
                        border="2px solid",
                        border_color="var(--primary)",
                        # border_color="",
                    ),
                    rx.heading("Experience", size="6", margin_top="2rem", color="var(--primary)"),
                    rx.vstack(
                        experience_card(
                            "2025", 
                            "Bi-Directional Voice Learning Assistant (R&D Project)", 
                            "Machine Learning Engineer", 
                            "Prototyped an AI-driven voice interface for visually impaired learners using Python speech recognition, text-to-speech, and adaptive feedback systems for inclusive learning experiences."
                        ),

                        experience_card(
                            "2024", 
                            "Fingerprint Authentication & Verification System", 
                            "Software Engineer (R&D Project)", 
                            "Developed a biometric authentication and identity verification platform integrating fingerprint recognition with secure database matching with 3 user types: Student, Admin & Supa-Admin."
                        ),

                        experience_card(
                            "2023", 
                            "Academic Plagiarism Detection System", 
                            "Research Developer", 
                            "Built a plagiarism detection engine using Bayesian probability models to analyze student project data and compute similarity scores. Extended with grammar and punctuation correction capabilities using NLP-based statistical inference."
                        ),

                        experience_card(
                            "2022", 
                            "Facial Recognition Student Attendance System", 
                            "Computer Vision Engineer", 
                            "Implemented an AI-powered attendance system using facial recognition. The system registers student facial data and automates attendance tracking within predefined lecture windows, isolating unrecognized faces."
                        ),
                        width="100%",
                        spacing="6",
                        margin_top="1.5rem",
                    ),
                    
                    spacing="4",
                ),

                rx.box(
                    rx.box(
                        rx.heading("Technical Skills", size="5", margin_bottom="1rem", color="var(--primary)"),
                        rx.vstack(
                            *[skill_bar(s["name"], s["proficiency"], s["type"], s["color"]) for s in SKILLS_DATA],
                            width="100%",
                            spacing="0",
                        ),
                        width="100%",
                        padding="2rem",
                        background="var(--card)",
                        border_radius="var(--radius)",
                        border="2px solid",
                        border_color="var(--primary)",
                        # border_color="",
                    ),

                    # --- Quick Stats / Facts ---
                    rx.hstack(
                        *[stat_card(stat["label"], stat["value"]) for stat in STATS_DATA],
                        width="100%",
                        justify="center",
                        spacing="6",
                        # wrap="wrap", # Allow wrapping on small screens
                        margin_bottom="3rem",
                        margin_top="3rem",
                    ),
                    padding_top=rx.breakpoints(initial="0.5rem", sm="4rem"),
                    min_width="45%",
                ),
                
                width="100%",
                direction=rx.breakpoints(initial="column", md="row"), # Two columns on desktop
                gap="4rem",
                margin_top="2rem",
            ),
            
            width="100%",
            max_width="1200px",
            padding=rx.breakpoints(initial="2rem", md="2rem"),
            
            
        ),
        width="100%",
        min_height="100vh",
        display="flex",
        align_items="center",
        justify_content="center",
        bg="var(--bg)",
        id="about",
    )
