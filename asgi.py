# asgi.py
import reflex as rx

# Import the app instance from your main app file
# (This assumes your main file is portfolio/portfolio.py)
from portfolio.portfolio import app

# Call app.get_asgi_app() to get the REAL, compiled
# ASGI 3.0 application that Granian can run.
asgi_app = app.get_asgi_app()