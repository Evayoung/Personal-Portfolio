# FILE: Portfolio/portfolio.py
# ============================================
import reflex as rx
from .pages import index

app = rx.App(stylesheets=["style.css"])

# Public pages
app.add_page(index.index_page, route="/")

"""
Portfolio/
├── .statics/
├── .web/              
├── assets/   
│   ├── cv/
│   │   ├── My_CV.pdf
│   │  
│   ├── screenshot/ 
│   │   ├── hero_section.jpg 
│   │   ├── abou_section.jpg
│   │   ├── service_section.jpg
│   │   ├── portfolio_section.jpg   
│   │   ├── contact_section.jpg    
│   │  
│   ├── style.css
│   ├── hero_bg.jpg
│   ├── image1.jpg
│   ├── image2.jpg
│   ├── favicon.ico
│   └── profile-photo.jpg
│               
├── portfolio/              
│   ├── __init__.py
│   ├── portfolio.py
│   │
│   ├── styles/
│   │   ├── animations.py
│   │   ├── data.py
│   │  
│   ├── states/
│   │   ├── portfolio_section.py
│   │   
│   ├── pages/
│   │   ├── index.py
│   │   ├── # future expantion
│   │   
│   ├── services/
│   │   ├── db.py # for future expantion
│   │
│   ├── components/
│   │   ├── common/
│   │   │   ├── footer.py
│   │   │   ├── nav_bar.py
│   │   │   ├── menu.py
│   │   │ 
│   │   ├── hero_secion.py
│   │   ├── about_secion.py
│   │   ├── services_secion.py
│   │   ├── portfolio_secion.py
│   │   ├── contact_secion.py
│   │   
│   └── utils/
├── rxconfig.py
└── requirements.txt
"""