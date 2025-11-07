import os
import reflex as rx

config = rx.Config(
    app_name="portfolio",
    show_built_with_reflex = False,
    frontend_port=int(os.getenv("PORT", 3000)),  
    # backend_port=8000  # Optional: if you're exposing backend separately
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(), 
    ]
)
