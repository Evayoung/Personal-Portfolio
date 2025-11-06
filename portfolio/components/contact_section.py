import reflex as rx
from ..styles.data import SKILLS_DATA, STATS_DATA
from ..styles import animation

# Helper to define the custom button style based on the primary color
PRIMARY_BUTTON_STYLE = {
    "bg": "var(--primary)",
    "color": "var(--bg)",
    "border_radius": "0.6rem",
    "font_weight": "500",
    # "box_shadow": "0 0 10px 1px hsl(190, 80%, 45%)", # Soft glow for buttons
    "transition": "all 0.3s ease",
    "_hover": {
        
        "transform": "translateY(-2px)",
        # "box_shadow": "0 6px 12px rgba(0,0,0,0.3), 0 0 20px 2px hsl(190, 80%, 65%)", # Enhanced glow
    },
}


def contact_card(icon: str, title: str, content: str) -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.badge(
                rx.icon(icon, size=20),
                padding="1rem",
                border_radius="50%",
            ),
            rx.vstack(
                rx.heading(title, font_weight="500", font_size="16px", color="var(--fg)"),
                rx.text(content, font_weight="normal", font_size="12px", color="var(--alt-fg)"),
                spacing="1"
            ),
            spacing="4",
            align="center",
        ),

        rx.cond(
            title != "My Location",
            rx.icon_button(
                rx.icon("copy", size=16),
                variant="soft",
                color_scheme="blue",
                aria_label=f"Copy {title}",
                border_radius="50%",
                size="2",
                cursor="pointer",
                style={
                    "color": "var(--primary)",
                    "transition": "all 0.3s ease",
                },
                on_click=[
                    rx.call_script(f"navigator.clipboard.writeText('{content}')"),
                    rx.toast.success(f"{title} copied to clipboard!", position="bottom-right"),
                ]
            )
        ),
        width="100%",
        bg="var(--card)",
        padding="1rem",
        border_radius="15px",
        justify="between",
        align="center",
        _hover={"bg": "var(--border)"},
    )


# --- Main Section Component ---

def contact_section() -> rx.Component:
    """
    Renders the 'My Journey' and 'My Skills' section.
    Uses the glass-morphism style for the main container.
    """
    desc="Leading development of AI-powered web applications with React, Node.js, and machine learning integration."
    return rx.section(
        rx.vstack(
            rx.heading(
                "Let's Talk", 
                size=rx.breakpoints(initial="8", sm="9", md="9"),
                margin_bottom="1.5rem", 
                color="var(--fg)", 
                width="100%", 
                text_align="center"
                ),
            
            rx.hstack(
                rx.text(
                    "Ready to bring your ideas to life? Let's discuss your project and create something amazing together.",
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
            
            # --- Contact Form ---
            rx.flex(
                # rx.box(
                #     rx.vstack(
                #         rx.heading("Send Me a Message", size="6", margin_bottom="1rem", font_weight="500", color="var(--primary)"),
                #         rx.flex(
                #             rx.vstack(
                #                 rx.text("Full Name", size="2", font_weight="400", align="left", width="100%", color="var(--fg)"),
                #                 rx.input(
                #                     placeholder="Micheal James",
                #                     type="text",
                #                     width="100%",
                #                     size=rx.breakpoints(initial="3", md="3"),
                #                     color_scheme="blue",
                #                     font_size="14px",
                #                     variant="soft",
                #                     color="var(--primary)",
                #                     style={
                #                         "color": "var(--primary)",
                #                         "background_color": "var(--bg)",
                #                     },
                #                 ),
                #                 width="100%",
                #                 spacing="2",
                #                 # margin_top="1rem"
                #             ),

                #             rx.vstack(
                #                 rx.text("Email Address", size="2", font_weight="400", align="left", width="100%", color="var(--fg)"),
                #                 rx.input(
                #                     placeholder="micheal@example.com",
                #                     type="email",
                #                     width="100%",
                #                     size=rx.breakpoints(initial="3", md="3"),
                #                     color_scheme="blue",
                #                     font_size="14px",
                #                     variant="soft",
                #                     color="var(--primary)",
                #                     style={
                #                         "color": "var(--primary)",
                #                         "background_color": "var(--bg)",
                #                     },
                #                 ),
                #                 width="100%",
                #                 spacing="2",
                #                 # margin_top="1rem"
                #             ),
                #             width="100%",
                #             gap="1rem",
                #             direction=rx.breakpoints(initial="column", md="row")
                #         ),

                #         rx.vstack(
                #             rx.text("Suject", size="2", font_weight="400", align="left", width="100%", color="var(--fg)"),
                #             rx.input(
                #                 placeholder="Project Discussion",
                #                 type="text",
                #                 width="100%",
                #                 size=rx.breakpoints(initial="3", md="3"),
                #                 color_scheme="blue",
                #                 font_size="14px",
                #                 variant="soft",
                #                 color="var(--primary)",
                #                 style={
                #                     "color": "var(--primary)",
                #                     "background_color": "var(--bg)",
                #                 },
                #             ),
                #             width="100%",
                #             spacing="2",
                #             # margin_top="2rem"
                #         ),

                #         rx.vstack(
                #             rx.text("Message", size="2", font_weight="400", align="left", width="100%", color="var(--fg)"),
                #             rx.text_area(
                #                 placeholder="Tell me about your Project...",
                #                 type="text",
                #                 width="100%",
                #                 height="150px",
                #                 color_scheme="blue",
                #                 font_size="14px",
                #                 variant="soft",
                #                 color="var(--primary)",
                #                 style={
                #                     "color": "var(--primary)",
                #                     "background_color": "var(--bg)",
                #                 },
                #             ),
                #             width="100%",
                #             spacing="2",
                #             # margin_top="2rem"
                #         ),

                #         rx.button(
                #             rx.icon("send", size=14),
                #             "Send Message",
                #             **PRIMARY_BUTTON_STYLE, 
                #             padding="0.7rem 1.25rem",
                #             width="100%",
                #             margin_top="1rem"
                #             # display=rx.breakpoints(initial="none", md="flex"),
                #         ),
                #         width="100%",
                #         spacing="4",
                #     ),

                    
                #     spacing="4",
                #     padding="1.5rem",
                #     background="var(--card)",
                #     border_radius="var(--radius)",
                #     border="2px solid",
                #     border_color="var(--primary)",
                #     # max_height="530px",
                #     width=rx.breakpoints(initial="100%", sm="48%"),
                # ),
                rx.box(
                    rx.vstack(
                        contact_card("mail", "Email Address", "Meshelleva@gmail.com"),
                        contact_card("phone", "Phone Number", "+2348064676590"),
                        # contact_card("message_circle", "Chat", "+2349029952120"),
                        contact_card("map_pin", "My Location", "Ilorin Kwara State, Nigeria"),
                        width="100%",
                        spacing="3"
                    ),
                    
                    width=rx.breakpoints(initial="100%", sm="48%"),
                ),
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.vstack(
                                        height="15px",
                                        width="15px",
                                        background_color="var(--primary)",
                                        border_radius="50%",
                                    ),
                                    rx.heading("Available For Projects", font_weight="500", font_size="14px", color="var(--primary)"),
                                    width="100%",
                                    spacing="4",
                                    align="center",
                                    justify="start"
                                ),

                                rx.text(
                                    "Currently accepting new projects and collaborations. Average response time: within 24 hours.", 
                                    font_weight="normal", 
                                    font_size="12px", 
                                    color="var(--alt-fg)"
                                    ),
                                rx.hstack(
                                    rx.vstack(
                                        rx.text("Timezone", font_weight="normal", font_size="12px", color="var(--fg)"),
                                        rx.heading("WAT (UTC+1)", font_weight="500", font_size="14px", color="var(--primary)"),
                                        width="48%",
                                        spacing="1"
                                    ),
                                    rx.vstack(
                                        rx.text("Best Time", font_weight="normal", font_size="12px", color="var(--fg)"),
                                        rx.heading("7 AM - 6 PM", font_weight="500", font_size="14px", color="var(--primary)"),
                                        width="48%",
                                        spacing="1"
                                    ),
                                    width="100%",
                                    justify="between",
                                    # padding="1rem",
                                ),
                                width="100%",
                                spacing="2",
                            ),
                            width="100%",
                            bg="var(--card)",
                            padding="1rem",
                            border_radius="15px",
                            border="2px solid var(--primary)",
                            margin_top="0.5rem",
                        ),

                        rx.hstack(
                            rx.badge(
                                rx.icon("facebook", size=20),
                                padding="1rem",
                                border_radius="50%",
                                cursor="pointer",
                                # bg="blue",
                                color="var(--fg)",
                                style=animation.HOVER_EFFECTS["hover_card_soft"], 
                                on_click=rx.redirect("https://www.facebook.com/micheal.evayoung", is_external=True),
                            ),

                            rx.badge(
                                rx.icon("instagram", size=20),
                                padding="1rem",
                                border_radius="50%",
                                cursor="pointer",
                                # bg="pink",
                                color="var(--fg)",
                                style=animation.HOVER_EFFECTS["hover_card_soft"], 
                                on_click=rx.redirect("https://www.instagram.com/meshelleva", is_external=True),
                            ),

                            rx.badge(
                                rx.icon("send", size=20),
                                padding="1rem",
                                border_radius="50%",
                                cursor="pointer",
                                # bg="blue",
                                color="var(--fg)",
                                style=animation.HOVER_EFFECTS["hover_card_soft"], 
                                on_click=rx.redirect("http://t.me/Meshelleva", is_external=True),
                            ),

                            rx.badge(
                                rx.icon("message_circle", size=20),
                                padding="1rem",
                                border_radius="50%",
                                cursor="pointer",
                                # bg="green",
                                color="var(--fg)",
                                style=animation.HOVER_EFFECTS["hover_card_soft"], 
                                on_click=rx.redirect("https://wa.me/qr/M7BFASLBRJY7F1", is_external=True),
                            ),
                            
                            aligh="center",
                            justify="center",
                            width="100%",
                            spacing="6",
                            margin_top="2rem",
                        ),

                        width="100%",
                        # padding="2rem",
                        spacing="3"
                    ),
                    
                    # padding=rx.breakpoints(initial="0.5rem", sm="4rem"),
                    width=rx.breakpoints(initial="100%", sm="48%"),
                ),
                
                width="100%",
                direction=rx.breakpoints(initial="column", sm="row"), # Two columns on desktop
                gap="4rem",
                margin_top="2rem",
            ),
            
            width="100%",
            max_width="1200px",
            padding=rx.breakpoints(initial="2rem", md="2rem"),
            
            
        ),
        width="100%",
        display="flex",
        align_items="center",
        justify_content="center",
        bg="var(--bg)",
        id="contact",
    )
