# FILE: portfolio/components/common/menu.py
import reflex as rx
from ...states.portfolio_state import UIState

PRIMARY_BUTTON_STYLE = {
    "bg": "primary.500",
    "color": "primary.contrast",
    "border_radius": "0.6rem",
    "font_weight": "300",
    "transition": "all 0.3s ease",
    "_hover": {"bg": "primary.600", "transform": "translateY(-2px)"},
}

def nav_link(label: str, href: str) -> rx.Component:
    """Reusable mobile nav link with subtle hover animation."""
    return rx.link(
        label,
        href=href,
        font_size="14px",
        font_weight="400",
        color="var(--fg)",
        text_decoration="none",
        _hover={"color": "var(--primary)", "transform": "translateX(4px)"},  # Changed to translateX for better mobile UX
        transition="color 0.2s ease, transform 0.2s ease",
        on_click=UIState.toggle_menu,  # Close menu when link is clicked
    )

def menu() -> rx.Component:
    """Slide-in mobile navigation menu with overlay and close icon."""
    return rx.fragment(
        # --- Overlay (dim background) ---
        rx.box(
            on_click=UIState.toggle_menu,
            position="fixed",
            top="0",
            left="0",
            width="100vw",
            height="100vh",
            background_color="rgba(0,0,0,0.5)",
            z_index="998",
            opacity=rx.cond(UIState.menu_open, "1", "0"),
            pointer_events=rx.cond(UIState.menu_open, "auto", "none"),
            transition="opacity 0.3s ease-in-out",
        ),

        # --- Menu Drawer ---
        rx.box(
            rx.vstack(
                # --- Close Button (Top-right) ---
                rx.icon_button(
                    rx.icon("x", size=24),
                    on_click=UIState.toggle_menu,
                    align_self="flex-end",
                    color="var(--fg)",
                    bg="transparent",
                    _hover={"color": "var(--primary)", "transform": "rotate(90deg)"},
                    transition="all 0.2s ease",
                    aria_label="Close menu",
                    mb="1rem",
                    size="3",
                ),

                # --- Navigation Links ---
                nav_link("Home", "#home"),
                nav_link("About", "#about"),
                nav_link("Services", "#services"),
                nav_link("Portfolio", "#portfolio"),
                nav_link("Contact", "#contact"),

                # --- CTA Button ---
                rx.button(
                    "Let's Talk",
                    on_click=rx.redirect("#contact"),
                    **PRIMARY_BUTTON_STYLE,
                    width="100%",
                    mt="2rem",
                ),

                spacing="5",
                align="start",  # Changed from center to start for better mobile UX
                padding="2rem 1.5rem",
                width="100%",
            ),

            position="fixed",
            top="0",
            right=rx.cond(UIState.menu_open, "0", "-320px"),  # KEY FIX: Move off-screen instead of translate
            width="70vw",
            max_width="320px",
            height="100vh",
            background_color="rgba(18,18,20,0.95)",  # Slightly more opaque
            backdrop_filter="blur(10px)",
            box_shadow="-5px 0 20px rgba(0,0,0,0.4)",
            transition="right 0.4s cubic-bezier(0.4, 0, 0.2, 1)",  # Smooth easing
            z_index="999",
            border_left="1px solid rgba(255,255,255,0.1)",
            class_name="glass-menu",
            overflow_y="auto",
            overflow_x="hidden",  # Prevent horizontal scroll within menu
        ),
    )