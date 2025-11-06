# 🌐 Personal Portfolio (2025)

A modern, interactive personal portfolio built with **[Reflex](https://reflex.dev)** — showcasing my professional work, projects, and research as a **Full-Stack Software Engineer & AI Systems Architect**.
Designed for performance, simplicity, and elegance, this portfolio highlights a seamless blend of **Python + Reflex (Pure Python UI)** with responsive design and smooth animations.

---

## 🚀 Live Demo

👉 **[View Online (Hosted on Render)](https://your-render-link-here)**
*(You can also deploy this project on Netlify, Vercel, or Reflex Cloud — see below for setup.)*

---

## 📸 Preview

| Section           | Screenshot                                                    |
| ----------------- | ------------------------------------------------------------- |
| Hero Section      | ![Hero Section](assets/screenshot/hero_section.jpg)           |
| About Section     | ![About Section](assets/screenshot/abou_section.jpg)          |
| Services Section  | ![Services Section](assets/screenshot/service_section.jpg)    |
| Portfolio Section | ![Portfolio Section](assets/screenshot/portfolio_section.jpg) |
| Contact Section   | ![Contact Section](assets/screenshot/contact_section.jpg)     |

---

## ✨ Features

* 🎨 **Responsive Design** — optimized across devices using Reflex breakpoints and CSS.
* ⚙️ **Modular Architecture** — all sections built as reusable Reflex components.
* 🧠 **Animation System** — powered by `animations.py` for hover effects and smooth UI transitions.
* 📄 **CV Download Button** — instantly downloads your CV from `assets/cv/My_CV.pdf`.
* 📧 **Contact via Gmail** — one-click mail badge opens Gmail with recipient pre-filled:
  `mailto:meshelleva@gmail.com`
* 🔗 **Social Links Integration** — direct links to social media (GitHub, LinkedIn, etc.) included in footer.
* 🧱 **Extensible Design** — supports new sections (blog, testimonials, projects) and backend integrations.

---

## 🧩 Project Structure

```
Portfolio/
├── .statics/
├── .web/
├── assets/
│   ├── cv/
│   │   └── My_CV.pdf
│   ├── screenshot/
│   │   ├── hero_section.jpg
│   │   ├── abou_section.jpg
│   │   ├── service_section.jpg
│   │   ├── portfolio_section.jpg
│   │   ├── contact_section.jpg
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
│   ├── styles/
│   │   ├── animations.py
│   │   ├── data.py
│   ├── states/
│   │   └── portfolio_section.py
│   ├── pages/
│   │   └── index.py
│   ├── services/
│   │   └── db.py
│   ├── components/
│   │   ├── common/
│   │   │   ├── footer.py
│   │   │   ├── nav_bar.py
│   │   │   ├── menu.py
│   │   ├── hero_secion.py
│   │   ├── about_secion.py
│   │   ├── services_secion.py
│   │   ├── portfolio_secion.py
│   │   ├── contact_secion.py
│   └── utils/
│
├── rxconfig.py
└── requirements.txt
```

---

## 🛠️ Tech Stack

| Layer              | Technology                                          |
| ------------------ | --------------------------------------------------- |
| Frontend & Backend | **Reflex (Python)**                                 |
| Styling            | **CSS**, Reflex theme tokens, and custom animations |
| Deployment         | Render / Reflex Cloud / Netlify / Vercel            |
| Assets             | Static images, icons, and downloadable PDF          |
| Future Extensions  | Database (via `services/db.py`), Blog, Project CMS  |

---

## ⚡ Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/Personal_Portfolio.git
cd Personal_Portfolio
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run locally

```bash
reflex run
```

This will start the local Reflex development server and open your portfolio at **[http://localhost:3000](http://localhost:3000)**

---

## 🌍 Deployment

You can deploy this project easily to any of the following:

* **Render:** Continuous deployment from GitHub
* **Reflex Cloud:** One-click deploy via Reflex dashboard
* **Netlify or Vercel:** Using static export (`reflex export`)

Example (for static export):

```bash
reflex export
```

Then upload the `/web` folder to your preferred static hosting provider.

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository, open issues, or submit pull requests for:

* New section ideas (blog, resume timeline, testimonials, etc.)
* UI/UX improvements
* Integration of external APIs (GitHub projects, Medium feed, etc.)

---

## 📜 License

This project is licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for details.

---

## 👤 Author

**Meshell Eva**
Full-Stack Software Engineer | AI Systems Architect | Data Researcher
📧 [meshelleva@gmail.com](mailto:meshelleva@gmail.com)
🌐 [LinkedIn](https://linkedin.com/in/meshelleva) | [GitHub](https://github.com/yourusername)

---

## 💬 Acknowledgements

* Built with ❤️ using [Reflex](https://reflex.dev)
* Animated transitions inspired by modern Python UI practices
* Open-source community support and inspiration
