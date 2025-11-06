import reflex as rx
from ..styles import animation
# Reusing the primary button style from navbar for consistency
PRIMARY_BUTTON_STYLE = {
    "bg": "var(--primary)",
    "color": "var(--bg)",
    "border_radius": "0.6rem",
    "font_weight": "400",
    "font_size": "14px",
    "pading": "1rem",
    "transition": "all 0.3s ease",
    "_hover": {
        "bg": "primary.600",
        "transform": "translateY(-2px)",
        "box_shadow": "0 6px 12px rgba(0,0,0,0.3), 0 0 20px 2px hsl(190, 80%, 65%)",
    },
}

# Style for the secondary/outline button, using the accent color
SECONDARY_BUTTON_STYLE = {
    "bg": "var(--card)",
    "color": "var(--fg)", # Use accent amber color
    # "border": "2px solid",
    "border_color": "accent.500",
    "border_radius": "0.6rem",
    "font_weight": "400",
    "font_size": "14px",
    "pading": "1rem",
    "transition": "all 0.3s ease",
    "_hover": {
        "bg": "var(--border)", # Darker amber on hover
        "transform": "translateY(-2px)",
        "box_shadow": "0 6px 12px rgba(0,0,0,0.3), 0 0 20px 2px hsl(45, 90%, 65%)",
    },
}

# The box style for the glowing profile picture
PROFILE_RING_STYLE = {
    "width": rx.breakpoints(initial="140px", sm="160px", md="200px"),
    "height": rx.breakpoints(initial="140px", sm="160px", md="200px"),
    "border_radius": "50%",
    "overflow": "hidden",
    "justify": "center",
    "align": "center",
    "class_name": "border-gradient-ring", # Custom class for glowing border effect
    "padding": "0.3rem",
    "box_shadow": "0 0 30px rgba(0,0,0,0.6)", # Base shadow
    "transition": "all 0.5s ease",
    "_hover": {
        "transform": "scale(1.03)",
        "box_shadow": "0 0 40px rgba(0,0,0,0.8)",
    }
}


def hero_section() -> rx.Component:
    """
    Hero section component with Cyber-Organic styling and animations.
    """
    return rx.box(
        
        # Overlay container (centered content)
        rx.vstack(
            # Profile Picture with Glowing Ring
            rx.box(
                rx.image(
                    src="/me-photo.jpg", # Assuming you meant profile-photo.jpg as per project structure
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    border_radius="50%",
                    loading="lazy",
                ),
                **PROFILE_RING_STYLE
            ),
            
            # Name
            rx.heading(
                "Olorundare Micheal",
                weight="bold",
                size=rx.breakpoints(initial="8", sm="9", md="9"),
                text_align="center",
                width="100%",
                color="var(--fg)", 
                class_name="glow-text", 
            ),

            # Role/Title
            rx.heading(
                "Full-Stack Developer & AI Engineer",
                weight="bold",
                size=rx.breakpoints(initial="7", sm="8", md="8"),
                color="var(--primary)", # Use primary cyan for the role
                text_align="center",
                width="100%",
                margin_top="-0.5rem", # Tighten spacing
            ),

            # Description Text
            rx.hstack(
                rx.text(
                    "Crafting digital experiences with cutting-edge technology and creative innovation. " \
                    "Specializing in full-stack development, AI integration, and cloud architecture.",
                    text_align="center",
                    width=rx.breakpoints(initial="90%", sm="75%", md="60%"),
                    font_size=rx.breakpoints(initial="16px", sm="18px", md="20px"),
                    color="var(--fg)",
                    opacity="0.8",
                    margin_top="1rem",
                ),
                width="100%",
                justify="center",
            ),

            # CTA Buttons
            rx.hstack(
                rx.button(
                    "View My Work",
                    rx.icon("arrow_down", size=18),
                    **PRIMARY_BUTTON_STYLE, # Apply primary button style
                    padding=rx.breakpoints(initial="0.8rem 1.5rem", sm="1rem 1.75rem"),
                    on_click=rx.redirect("#portfolio")
                ),

                rx.button(
                    "Download CV",
                    **SECONDARY_BUTTON_STYLE,
                    padding=rx.breakpoints(initial="0.8rem 1.5rem", sm="1rem 1.75rem"),
                    on_click=rx.redirect("/cv/My_CV.pdf", is_external=True),
                ),

                width="100%",
                padding_top="2rem",
                spacing="6",
                align="center",
                justify="center",
            ),

            # Social Media Badges (Apply the hover/glow effects)
            rx.hstack(
                rx.badge(
                    rx.icon("github", size=24), 
                    padding="0.75rem", 
                    border_radius="50%", 
                    bg="var(--border)", 
                    color="var(--fg)",
                    cursor="pointer",
                    style=animation.HOVER_EFFECTS["hover_card_soft"], 
                    on_click=rx.redirect("https://github.com/Evayoung", is_external=True),
                ),
                rx.badge(
                    rx.icon("linkedin", size=24), 
                    padding="0.75rem", 
                    border_radius="50%", 
                    bg="var(--border)", 
                    color="var(--fg)", 
                    cursor="pointer",
                    style=animation.HOVER_EFFECTS["hover_card_soft"],
                    on_click=rx.redirect("https://linkedin.com/in/micheal-olorundare", is_external=True),
                ),
                rx.badge(
                    rx.icon("mail", size=24), 
                    padding="0.75rem", 
                    border_radius="50%", 
                    bg="var(--border)", 
                    color="var(--fg)",
                    cursor="pointer",
                    style=animation.HOVER_EFFECTS["hover_card_soft"],
                    on_click=rx.redirect("https://mail.google.com/mail/?view=cm&fs=1&to=meshelleva@gmail.com", is_external=True),
                ),
                width="100%",
                justify="center",
                margin_top="2rem",
                align="center",
                spacing="6",
            ),

            width="100%",
            max_width="1000px",
            height="100%",
            padding="2rem",
            spacing="5", # Increased spacing slightly for better vertical rhythm
            justify="center",
            align="center",
            # padding_top="80px", # Account for navbar height
            position="relative",
            z_index="1",
            margin_x="auto", # Center the vstack content
            
        ),

        # Container-level props (background + overlay)
        id="home",
        width="100%",
        min_height="100vh",
        display="flex",
        flex_direction="column",
        align_items="center",
        justify_content="center", 
        position="relative",
        background_image="url('/hero-bg.jpg')", 
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        _before={
            "content": "''",
            "position": "absolute",
            "top": "0",
            "left": "0",
            "width": "100%",
            "height": "100%",
            "bg": "rgba(0,0,0,0.75)", # Reduced opacity slightly for background visibility
            "z_index": "0",
        },
    )
