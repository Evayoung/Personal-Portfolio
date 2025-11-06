# import reflex as rx

# # --- Cyber-Organic Theme Definition ---
# # These HSL values are pulled directly from your assets/style.css and converted
# # into a format suitable for Reflex/Chakra-UI theme customization.
# CYBER_ORGANIC_COLORS = {
#     # Core Colors (Base on --bg, --fg)
#     "bg": "hsl(220, 20%, 8%)",
#     "fg": "hsl(210, 20%, 95%)",
#     "muted": "hsl(220, 25%, 15%)",
#     "card": "hsl(220, 30%, 12%)",
#     "border": "hsl(220, 30%, 18%)",
    
#     # Primary (Cyan)
#     "primary": {
#         "500": "hsl(190, 80%, 60%)", # --primary
#         "600": "hsl(190, 60%, 45%)", # --cyber-cyan-dim (for darker hover)
#         "contrast": "hsl(220, 20%, 8%)", # --primary-contrast
#     },
#     # Accent (Amber/Organic)
#     "accent": {
#         "500": "hsl(45, 90%, 60%)", # --accent
#         "600": "hsl(45, 70%, 45%)", # --organic-amber-dim
#     },
# }

# # --- FIX: Define the Radius Constant Separately ---
# RADIUS_CONSTANT = "0.75rem"


# # Typography Definition
# CUSTOM_FONTS = {
#     # Space Grotesk for headings and technical text
#     "heading": "Space Grotesk, sans-serif",
#     # Crimson Pro for body text
#     "body": "Crimson Pro, serif",
# }

# # Default global style settings
# GLOBAL_STYLE = {
#     "body": {
#         "font_family": CUSTOM_FONTS["body"],
#         "background_color": CYBER_ORGANIC_COLORS["bg"],
#         "color": CYBER_ORGANIC_COLORS["fg"],
#         "min_height": "100vh",
#     },
#     # Apply heading font to all Reflex/Chakra Heading components
#     rx.heading: {
#         "font_family": CUSTOM_FONTS["heading"],
#     },
#     # Ensure all links/buttons have smooth transitions
#     rx.link: {
#         "transition": "all 0.35s cubic-bezier(0.4, 0, 0.2, 1)",
#     },
# }

# # The custom theme object that will be passed to rx.App
# CUSTOM_THEME = rx.theme(
#     name="cyber_organic_theme",
#     # Override the default color palette with our custom HSL tokens
#     colors={
#         "gray": {
#             "50": CYBER_ORGANIC_COLORS["fg"],
#             "900": CYBER_ORGANIC_COLORS["bg"],
#         },
#         **CYBER_ORGANIC_COLORS # Spread our custom colors directly
#     },
#     # Set custom fonts
#     fonts=CUSTOM_FONTS,
#     # Set custom global styles
#     styles=GLOBAL_STYLE,
#     # Set default radius for components (like buttons, cards)
#     radii={
#         # FIX: Now referencing the new RADIUS_CONSTANT
#         "default": RADIUS_CONSTANT, 
#     },
#     # Make sure we use the color mode (Dark by default)
#     appearance="dark",
#     has_background=True,
#     # The following two props are removed to avoid conflict with Radix predefined color names
#     # accent_color="primary", 
#     # gray_color="muted",
# )

# class PortfolioConfig(rx.Config):
#     # Pass the custom theme to the config
#     theme = CUSTOM_THEME
#     pass

# config = rx.config(
#     app_name="portfolio",
#     plugins=[
#         rx.plugins.SitemapPlugin(),
#         rx.plugins.TailwindV4Plugin(),
#     ]
# )

import reflex as rx

config = rx.Config(
    app_name="portfolio",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(), # <--- Note: We didn't use this plugin
    ]
)