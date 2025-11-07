import reflex as rx
import os

# --- Configuration Constants ---
# Use a more explicit variable check that you control in Render's settings
IS_PROD = os.getenv("ENV") == "PROD" 

# Render will provide the external URL in the service environment variables
# Fallback to the one you provided if the automatic one isn't available
RENDER_URL_BASE = os.getenv("RENDER_EXTERNAL_HOSTNAME", "personal-portfolio-su62.onrender.com")

# Ensure URL is complete with scheme (https)
RENDER_URL_HTTPS = f"https://{RENDER_URL_BASE}"
RENDER_URL_HTTP = f"http://{RENDER_URL_BASE}" # For safety

# Render assigns port dynamically via the PORT env var
BACKEND_PORT = int(os.getenv("PORT", 8000))


config = rx.Config(
    app_name="portfolio",
    
    # --- Badge Removal (Since 0.7.x) ---
    show_built_with_reflex=False,
    
    # --- Networking and Deployment ---
    # api_url should point to the backend's public endpoint.
    # Using the full HTTPS URL is the safest, most explicit approach for external access.
    api_url=RENDER_URL_HTTPS if IS_PROD else "http://localhost:8000",
    deploy_url=RENDER_URL_HTTPS,
    
    # Backend server settings
    backend_port=BACKEND_PORT,
    backend_host="0.0.0.0" if IS_PROD else "localhost",
    
    # Frontend port is usually 3000 locally, but must match the backend port in a 
    # unified production deployment like Render/Gunicorn to be served correctly.
    frontend_port=BACKEND_PORT if IS_PROD else 3000,
    
    # --- Environment and Database ---
    env=rx.Env.PROD if IS_PROD else rx.Env.DEV,

    # Critical for WebSockets and API calls. Must allow your public URL.
    cors_allowed_origins=[RENDER_URL_HTTPS, RENDER_URL_HTTP] if IS_PROD else [
        "http://localhost:3000",
        "http://localhost:8000",
    ],
    
    # WARNING: Switch to PostgreSQL for production to avoid data loss on restarts!
    db_url=os.getenv("DATABASE_URL", "sqlite:///reflex.db"), 
    
    # --- Other Settings ---
    timeout=120,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)