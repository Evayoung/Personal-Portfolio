
# ============================================
# FILE: components/portfolio_section.py (FIXED)
# ============================================
import reflex as rx
from typing import Dict, Any
from ..states.portfolio_state import ProjectState, PROJECTS_DATA

# --- HELPER COMPONENTS ---

def sort_button(label: str) -> rx.Component:
    """The custom button to filter projects."""
    return rx.box(
        rx.text(label, size="2"),
        padding_y="0.5rem",
        padding_x="0.75rem",
        bg="var(--border)",
        color="var(--fg)",
        border_radius="8px",
        cursor="pointer",
        transition="opacity 0.4s ease-in-out",
        _hover={
            "background_color": "var(--hover-button)",
        },
    )


def project_links_overlay(project: Dict[str, Any]) -> rx.Component:
    """Smooth overlay animation on hover."""
    return rx.center(
        rx.hstack(
            rx.hstack(
                rx.icon(tag="external_link", size=15),
                rx.text("Live Demo", font_size="12px"),
                padding_y="0.5rem",
                padding_x="0.75rem",
                bg="var(--border)",
                color="var(--fg)",
                border_radius="10px",
                cursor="pointer",
                on_click=rx.toast.info(f"{project['title']} demo link not available", position="bottom-right"),
                _hover={
                    "transition": "opacity 0.4s ease-in-out",
                    "background_color": "var(--hover-button)",
                },
            ),
            rx.hstack(
                rx.icon(tag="github", size=15),
                rx.text("Code", font_size="12px"),
                padding_y="0.5rem",
                padding_x="0.75rem",
                bg="black",
                color="var(--fg)",
                border_radius="10px",
                cursor="pointer",
                on_click=rx.toast.info(f"{project['title']} repo not updated!", position="bottom-right"),
                _hover={
                    "transition": "opacity 0.4s ease-in-out",
                    "background_color": "#fbf706",
                    "color": "#000000",
                },
            ),

            spacing="4",
        ),
        width="100%",
        height="100%",
        position="absolute",
        top="0",
        left="0",
        z_index="10",
        background_color="rgba(0, 0, 0, 0.85)",
        opacity=rx.cond(ProjectState.hovered_project_id == project["id"], "1", "0"),
        transition="opacity 0.4s ease-in-out", 
    )


def project_card(project: Dict[str, Any]) -> rx.Component:
    image_url = project["image_url"]
    return rx.box(
        rx.flex(
            # --- Image/Overlay Area (Layered) ---
            rx.box(
                project_links_overlay(project),

                width="100%",
                height="200px",
                position="relative",
                overflow="hidden",
                
            ),

            # --- Info Area ---
            rx.vstack(
                rx.flex(
                    rx.badge(project["category"], color_scheme="sky", size="1"),
                    rx.cond(
                        project["project"] != "",
                        rx.box(
                            rx.text(project["project"], font_size="10px", font_weight="500"),
                            padding_y="0.2rem",
                            padding_x="0.5rem",
                            bg="#DEDB03",
                            color="black",
                            border_radius="12px",
                            cursor="pointer",
                            transition="opacity 0.4s ease-in-out",
                            _hover={
                                "background_color": "var(--hover-button)",
                            },
                        )
                        
                    ),
                    width="100%",
                    justify="between",
                    align="center",
                ),
                
                rx.heading(
                    project["title"], 
                    size="4", 
                    margin_top="0.5rem",
                    transition="opacity 0.4s ease-in-out",
                    color=rx.cond(
                        ProjectState.hovered_project_id == project["id"], 
                        "var(--primary)",
                        "var(--fg)"
                        )
                    ),
                
                rx.text(
                    project["description"],
                    size="2",
                    color="gray",
                    opacity="0.9",
                    margin_bottom="1rem"
                ),

                # Tech Stack Tags
                rx.hstack(
                    rx.foreach(
                        project["tech_stack"],
                        lambda tag: rx.badge(
                            tag, 
                            color="var(--alt-fg)", 
                            bg="var(--border)",
                            font_size="10px", 
                            padding_y="0.25rem",
                            padding_x="0.5rem",
                            border_radius="10px",
                            border="1px solid var(--harsh)",
                        ),
                    ),
                    wrap="wrap",
                    spacing="2",
                ),

                align_items="start",
                spacing="3",
                width="100%",
                padding="1rem",
                background_color="var(--muted)",
                flex="1",  
                justify="between",  
            ),

            spacing="0",
            direction="column",
            width="100%",
            height="100%",  
        ),

        width=rx.breakpoints(
            initial="100%",
            sm="48%",
            md=rx.cond(project["project"] == "featured", "60%", "35%")
        ),
        border="1px solid var(--primary)",
        border_radius="12px",
        overflow="hidden",
        padding="0",
        background_image = f"url('{image_url}')",
        # background_image=f"url('{project["image_url"]}')", 
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        transition="all 0.3s ease",
        min_height="400px",
        on_mouse_enter=ProjectState.set_hover(project["id"], True),
        on_mouse_leave=ProjectState.set_hover(project["id"], False),
    )


# --- MAIN SECTION COMPONENT ---

def portfolio_section() -> rx.Component:
    """Renders the 'My Portfolio' section."""
    return rx.section(
        rx.vstack(
            rx.heading(
                "My Portfolio",
                size=rx.breakpoints(initial="8", sm="9", md="9"),
                margin_bottom="1.5rem",
                width="100%",
                text_align="center",
                color="var(--fg)"
            ),

            rx.hstack(
                rx.text(
                    "Showcase of innovative projects that demonstrate technical excellence and creative problem-solving.",
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
            
            # --- Sort Buttons ---
            rx.hstack(
                sort_button("All"),
                sort_button("Full-Stack"),
                sort_button("Frontend"),
                sort_button("AI/ML"),
                sort_button("DevOps"),
                sort_button("Mobile"),
                sort_button("Desktop"),
                sort_button("Blockchain"),
                width="100%",
                align="center",
                justify="center",
                wrap="wrap",
                spacing="3",
                padding="2rem 0",
            ),

            # --- Project Grid ---
            rx.flex(
                rx.foreach(PROJECTS_DATA, project_card),
                width="100%",
                wrap="wrap",
                gap="2rem",
                margin_top="1rem",
                justify=rx.breakpoints(initial="center", md="start"),
            ),

            width="100%",
            max_width="1200px",
            padding="2rem",
            
        ),
        width="100%",
        display="flex",
        align_items="center",
        justify_content="center",
        bg="var(--card)",
        id="portfolio"
    )