# portfolio/asgi.py
import reflex as rx
from portfolio import portfolio  # your rx.App instance

# Export the *real* ASGI callable that Granian expects
app: rx.App = portfolio.app  # type: ignore
asgi_app = app.asgi_app   # <-- this is the 3-arg callable