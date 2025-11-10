import reflex as rx
import os

# Detect production
is_production = os.getenv("PORT") is not None

# Your Render URL
RENDER_URL = "https://personal-portfolio-su62.onrender.com"

# Render's dynamic port
PORT = int(os.getenv("PORT", 10000))

config = rx.Config(
    app_name="portfolio",
    
    # Remove badge
    show_built_with_reflex=False,
    
    # CRITICAL FIX: api_url must be https://, NOT wss://
    # Reflex automatically converts this to wss:// for WebSocket
    api_url=RENDER_URL if is_production else "http://localhost:8000",
    deploy_url=RENDER_URL if is_production else "http://localhost:3000",
    
    # Port configuration
    backend_port=PORT if is_production else 8000,
    frontend_port=PORT if is_production else 3000,
    backend_host="0.0.0.0" if is_production else "localhost",
    
    # Environment
    env=rx.Env.PROD if is_production else rx.Env.DEV,
    
    # CORS
    cors_allowed_origins=[RENDER_URL] if is_production else [
        "http://localhost:3000",
        "http://localhost:8000"
    ],
    
    # WebSocket timeout
    timeout=120,
    
    # Database
    db_url=os.getenv("DATABASE_URL", "sqlite:///reflex.db"),
    
    # Plugins
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(), 
    ]
)