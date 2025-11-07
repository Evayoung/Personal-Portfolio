import reflex as rx
import os

# Render provides PORT environment variable
PORT = int(os.getenv("PORT", 10000))

# Detect environment
is_production = os.getenv("ENV") == "production"

# Your actual Render URL
RENDER_URL = "https://personal-portfolio-su62.onrender.com"

config = rx.Config(
    app_name="portfolio",
    
    # Remove the badge - FREE FEATURE, no payment needed
    show_built_with_reflex=False,
    
    # URLs for WebSocket
    api_url=RENDER_URL if is_production else "http://localhost:8000",
    deploy_url=RENDER_URL if is_production else "http://localhost:3000",
    
    # Port configuration for Render
    backend_port=PORT,
    frontend_port=PORT,
    backend_host="0.0.0.0",
    
    # Environment
    env=rx.Env.PROD if is_production else rx.Env.DEV,
    
    # CORS for WebSocket
    cors_allowed_origins=[RENDER_URL] if is_production else [
        "http://localhost:3000",
        "http://localhost:8000"
    ],
    
    # WebSocket timeout
    timeout=120,
    
    # Database
    db_url=os.getenv("DATABASE_URL", "sqlite:///reflex.db"),
    
    # Your plugins
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(), 
    ]
)