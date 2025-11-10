import reflex as rx
import os

# Simple production detection
is_production = os.getenv("REFLEX_ENV") == "prod"

# Your Render URL
RENDER_URL = "https://personal-portfolio-su62.onrender.com"

# Port from environment
PORT = int(os.getenv("PORT", 8000))

config = rx.Config(
    app_name="portfolio",
    
    # Remove badge
    show_built_with_reflex=False,
    
    # URLs - HTTPS not WSS
    api_url=RENDER_URL if is_production else "http://localhost:8000",
    deploy_url=RENDER_URL if is_production else "http://localhost:3000",
    
    # Port configuration
    backend_port=PORT,
    frontend_port=PORT if is_production else 3000,
    backend_host="0.0.0.0" if is_production else "localhost",
    
    # Environment
    env=rx.Env.PROD if is_production else rx.Env.DEV,
    
    # CORS
    cors_allowed_origins=[RENDER_URL] if is_production else [
        "http://localhost:3000",
        "http://localhost:8000"
    ],
    
    # Timeout
    timeout=120,
    
    # Database
    db_url=os.getenv("DATABASE_URL", "sqlite:///reflex.db"),
    
    # Plugins
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(), 
    ]
)