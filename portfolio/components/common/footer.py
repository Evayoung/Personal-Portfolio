# Application footer

import reflex as rx


def footer() -> rx.Component:
    """Modern centered footer — clean, symmetric, responsive."""
    return rx.box(
        
        rx.text(
            "© 2024 - 2025 Olorundare Micheal. Crafted with passion and cutting-edge technology.",
            font_weight="500",
            text_align="center",
            font_size="12px",
            color="var(--alt-fg)",
            letter_spacing="0.04em",
            margin_bottom="0.5rem",
        ),
        
        padding="2rem",
        bg="var(--bg)",
        width="100%",
        box_shadow="0 -2px 6px rgba(0,0,0,0.04)",
        border_top="1px solid var(--border)",
        align="center",
    )
