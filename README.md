# 🌿 EcoLens

A sustainability companion app — scan products, track your carbon footprint, earn badges, play eco-games, and chat with EcoBot.

## Project Structure

```
ecolens/
├── backend/          FastAPI + SQLite
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── routers/      auth, scanner, profile, games, chatbot
│   └── services/     carbon_estimator, badge_service
└── frontend/
    ├── index.html
    └── static/       style.css, app.js
```

## Setup & Run

### Backend

```bash
cd ecolens/backend
pip install -r requirements.txt
cp .env.example .env   # edit if needed
uvicorn main:app --reload --port 8000
```

### Frontend

Open `ecolens/frontend/index.html` in your browser, or serve it:

```bash
cd ecolens/frontend
python -m http.server 3000
```

Then visit `http://localhost:3000`

## Features

| Feature | Description |
|---|---|
| 📷 Carbon Scanner | Upload image, enter barcode, or type text to get CO₂ estimate + eco rating |
| 🧬 Eco-DNA Profile | Monthly carbon chart, badges, streak, top categories |
| 🏅 Badges | Auto-awarded for milestones (first scan, carbon saved, etc.) |
| 🎮 Eco-Games | Treasure hunts, streaks, challenges with point rewards |
| 🤖 EcoBot | Chatbot with disposal tips, eco stories, greener alternatives |

## Notes

- OCR requires Tesseract installed (`tesseract-ocr`). Without it, the app falls back gracefully to filename/text-based estimation.
- Carbon estimates are mock values for development — replace `services/carbon_estimator.py` with a real API (e.g., Climatiq) for production.
- Default DB is SQLite (`ecolens.db`) — no setup needed.
