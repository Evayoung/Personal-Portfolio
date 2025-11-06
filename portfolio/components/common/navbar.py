# FILE: portfolio/components/common/navbar.py
import reflex as rx
from ...states.portfolio_state import UIState
from .menu import menu  # import the slide-in menu component

PRIMARY_BUTTON_STYLE = {
    "bg": "primary.500",
    "color": "primary.contrast",
    "border_radius": "0.6rem",
    "font_weight": "300",
    "transition": "all 0.3s ease",
    "_hover": {"bg": "primary.600", "transform": "translateY(-2px)"},
}

def nav_link(label: str, href: str) -> rx.Component:
    return rx.link(
        label,
        href=href,
        font_size="12px",
        font_weight="300",
        color="var(--fg)",
        text_decoration="none",
        _hover={"color": "var(--primary)", "transform": "translateY(-2px)"},
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # --- Logo ---
            rx.text(
                "MO",
                font_weight="700",
                font_size="1.5rem",
                color="var(--fg)",
                text_shadow="0 0 8px hsl(190, 80%, 50%)",
            ),

            # --- Desktop Links ---
            rx.hstack(
                nav_link("Home", "#home"),
                nav_link("About", "#about"),
                nav_link("Services", "#services"),
                nav_link("Portfolio", "#portfolio"),
                nav_link("Contact", "#contact"),
                spacing="5",
                align="center",
                display=rx.breakpoints(initial="none", md="flex"),
            ),

            # --- Desktop CTA ---
            rx.button(
                "Let's Talk",
                **PRIMARY_BUTTON_STYLE,
                padding="0.7rem 1.25rem",
                display=rx.breakpoints(initial="none", md="flex"), #
                on_click=rx.redirect("#contact")
            ),

            # --- Mobile Menu Icon ---
            rx.icon(
                "menu",
                size=28,
                color="var(--fg)",
                display=rx.breakpoints(initial="block", md="none"),
                cursor="pointer",
                on_click=UIState.toggle_menu,
            ),

            justify="between",
            align="center",
            width="100%",
            padding_x=rx.breakpoints(initial="1rem", md="2rem"),
            padding_y="0.8rem",
        ),
        rx.script("""
            // Add/remove menu-open class based on menu state
            const observer = new MutationObserver(() => {
                // This will run when state changes
                const menuOpen = document.querySelector('[data-menu-state]');
                if (menuOpen) {
                    document.body.classList.toggle('menu-open', menuOpen.dataset.menuState === 'true');
                }
            });
            observer.observe(document.body, { childList: true, subtree: true });
        """),
        menu(),
        position="sticky",
        top="0",
        z_index="1000",
        class_name="glass",
        width="100%",
    )
# 