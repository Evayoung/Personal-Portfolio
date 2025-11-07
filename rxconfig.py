import reflex as rx
import os

# --- Environment and URL Setup ---
# 1. Detect production: Use the PORT env var, which Render always sets.
is_production = os.getenv("PORT") is not None 

# 2. Base URL: The Render app URL must use HTTPS.
RENDER_HOST = "personal-portfolio-su62.onrender.com"
RENDER_URL = f"https://{RENDER_HOST}"
# Use WSS (Secure WebSocket) for production API
RENDER_WS_URL = f"wss://{RENDER_HOST}" 

# 3. Dynamic Port: This is the single port Render uses
PRODUCTION_PORT = int(os.getenv("PORT", 10000))

# --- Reflex Configuration ---
config = rx.Config(
    app_name="portfolio",
    
    # Badge removal
    show_built_with_reflex=False,
    
    # 2. URLs (CRITICAL)
    api_url=RENDER_WS_URL if is_production else "http://localhost:8000", 
    deploy_url=RENDER_URL if is_production else "http://localhost:3000",
    
    # 3. --- THE CRITICAL FIX ---
    # In production, the backend and frontend MUST be the same port.
    # In dev, they are separate.
    backend_port = PRODUCTION_PORT if is_production else 8000,
    frontend_port = PRODUCTION_PORT if is_production else 3000,
    # ---
    
    backend_host="0.0.0.0",
    
    # 4. Environment
    env=rx.Env.PROD if is_production else rx.Env.DEV,
    
    # 5. CORS
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