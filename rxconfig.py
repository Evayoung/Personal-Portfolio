import reflex as rx
import os

# --- Environment and URL Setup ---
# 1. Detect production: More robustly check for Render's PORT variable.
is_production = os.getenv("PORT") is not None 

# 2. Base URL: The Render app URL must use HTTPS.
RENDER_HOST = "personal-portfolio-su62.onrender.com"
RENDER_URL = f"https://{RENDER_HOST}"
RENDER_WS_URL = f"wss://{RENDER_HOST}" # Use WSS for production WebSocket

# 3. Dynamic Port: Render sets the port for the backend process.
BACKEND_PORT = int(os.getenv("PORT", 10000))

# --- Reflex Configuration ---
config = rx.Config(
    app_name="portfolio",
    
    # Badge removal
    show_built_with_reflex=False,
    
    # 2. URLs for WebSocket (CORRECTED)
    # The API URL *must* use WSS:// for Render's SSL/WebSocket proxying
    api_url=RENDER_WS_URL if is_production else "http://localhost:8000", 
    deploy_url=RENDER_URL if is_production else "http://localhost:3000",
    
    # 3. Port configuration
    # This ensures Reflex *knows* what port is being used,
    # even though the start command is what forces it.
    backend_port=BACKEND_PORT,
    frontend_port=3000, # Only relevant for local 'reflex run'
    backend_host="0.0.0.0",
    
    # 4. Environment
    env=rx.Env.PROD if is_production else rx.Env.DEV,
    
    # 5. CORS - This is correct, but let's base it on our robust var
    cors_allowed_origins=[RENDER_URL] if is_production else [
        "http://localhost:3000",
        "http://localhost:8000"
    ],
    
    # 6. WebSocket timeout
    timeout=120,
    
    # 7. Database
    db_url=os.getenv("DATABASE_URL", "sqlite:///reflex.db"),
    
    # 8. Your plugins
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(), 
    ]
)