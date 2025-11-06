import reflex as rx

config = rx.Config(
    app_name="portfolio",
    show_built_with_reflex = False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(), # <--- Note: We didn't use this plugin
    ]
)