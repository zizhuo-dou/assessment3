# 🌍 WorldExplorer — Flask Web Application

WorldExplorer is a data-driven Flask web application built as part of the CS551P Advanced Programming assessment. It allows users to explore global country and city data interactively, visualize statistics, and understand structured backend development using modern Python practices.

---

## 📦 Features

- 🌐 Browse all countries from a CSV dataset
- 🏙 View detailed city data by country
- 📊 Statistics page: most populous countries, city population summaries
- 🔍 Search functionality for countries and cities
- ✅ Error handling (404, 500)
- 📂 Modular code structure using Flask Blueprints
- 🧪 Unit tests using `pytest`
- 🎨 UI styled with Bootstrap 5
- ☁️ Deployed to Render

---

## 🧠 Technologies & Concepts

- Flask + Jinja2 templating
- SQLAlchemy ORM with SQLite
- Object-Oriented Programming (OOP)
- MVC / MVT web architecture
- Data loading from CSV via pandas / Python
- GitHub version control & deployment pipeline
- Python testing (`pytest`)
- RESTful route structure (planned)

## website (cloud)

https://assessment-final-version.onrender.com

---

## 🚀 Getting Started

1. **Clone the repo**
```bash
git clone https://github.com/zizhuo-dou/worldexplorer.git
cd worldexplorer
Set up virtual environment

bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Run the application



python run.py 
Access it locally
Visit http://localhost:5000

🧪 Running Tests
pytest tests/
Tests cover models and route functionality.

##📁 Project Structure

worldexplorer/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   └── static/
├── data_loader.py
├── run.py
├── requirements.txt
├── Procfile
└── README.md


