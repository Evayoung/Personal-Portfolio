
import reflex as rx

config = rx.Config(
    app_name="portfolio",
    show_built_with_reflex = False,
    api_url="http://0.0.0.0:1000",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(), 
    ]
)
