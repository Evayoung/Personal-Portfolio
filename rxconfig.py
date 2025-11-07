import reflex as rx
import os

# CRITICAL: Render provides PORT environment variable
PORT = int(os.getenv("PORT", 8000))

# Detect environment
is_production = os.getenv("ENV") == "production"

# Your actual Render URL
RENDER_URL = "https://personal-portfolio-su62.onrender.com"

config = rx.Config(
    app_name="portfolio",
    
    # Remove the badge
    show_built_with_reflex=False,
    
    # URLs - Critical for WebSocket
    api_url=RENDER_URL if is_production else "http://localhost:8000",
    deploy_url=RENDER_URL if is_production else "http://localhost:3000",
    
    # CRITICAL: Use Render's PORT and bind to 0.0.0.0
    backend_port=PORT,
    frontend_port=PORT,  # Same port for both in production
    backend_host="0.0.0.0",  # Must be 0.0.0.0, not localhost
    
    # Environment
    env=rx.Env.PROD if is_production else rx.Env.DEV,
    
    # CORS - Required for WebSocket connections
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