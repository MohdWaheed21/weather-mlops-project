# 🌦️ Weather Prediction MLOps Project

An end-to-end production-ready Machine Learning project that predicts whether it will rain tomorrow using historical weather data.

This project is built with a complete MLOps pipeline including:

* Machine Learning Model Training
* FastAPI Backend API
* React Frontend Dashboard
* SQLite Database for Prediction History
* Docker Containerization
* MLflow Experiment Tracking
* GitHub Actions CI/CD Pipeline
* Cloud Deployment using Render
* Frontend Deployment using Vercel

This is not just a notebook project — it is a real-world deployable ML product.

---

# 🚀 Live Demo

## Backend API (Live)

## API Documentation

## Frontend Dashboard

(Deploy on Vercel and add your frontend live link here)

Example:

```text id="readme01"
https://weather-dashboard.vercel.app
```

---

# 📌 Features

## Machine Learning

* Rain prediction using Random Forest Classifier
* Real-world weather dataset
* Data preprocessing pipeline
* Feature engineering
* Model persistence using Joblib

## Backend

* FastAPI REST API
* Input validation using Pydantic
* Prediction API endpoint
* History API endpoint
* Automatic SQLite table creation

## Frontend

* Beautiful React Dashboard
* Smart dropdown-based UI
* Rain prediction interface
* Prediction history display
* Real-time backend integration

## MLOps

* Dockerized backend deployment
* MLflow experiment tracking
* GitHub Actions CI/CD automation
* Cloud deployment pipeline
* Production-ready architecture

---

# 🛠️ Tech Stack

## Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

## Backend

* FastAPI
* Pydantic
* SQLite
* Uvicorn

## Frontend

* React
* Axios
* CSS

## MLOps & Deployment

* Docker
* MLflow
* GitHub Actions
* Render
* Vercel

---

# 📂 Project Structure

```text id="readme02"
weather-mlops-project/
│
├── backend/
│   ├── app.py
│   ├── schema.py
│   └── database.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── App.js
│
├── model/
│   └── rain_prediction.pkl
│
├── src/
│   └── train.py
│
├── data/
│   └── raw/
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── Dockerfile
├── requirements.txt
├── render.yaml
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash id="readme03"
git clone https://github.com/yourusername/weather-mlops-project.git
cd weather-mlops-project
```

---

# Backend Setup

## Create Virtual Environment

```bash id="readme04"
python -m venv venv
```

## Activate Environment

### Windows

```bash id="readme05"
venv\Scripts\activate
```

### Linux / Mac

```bash id="readme06"
source venv/bin/activate
```

## Install Dependencies

```bash id="readme07"
pip install -r requirements.txt
```

---

# Run Backend

```bash id="readme08"
uvicorn backend.app:app --reload
```

Backend runs at:

```text id="readme09"
http://127.0.0.1:8000
```

Swagger Docs:

```text id="readme10"
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

```bash id="readme11"
cd frontend
npm install
npm start
```

Frontend runs at:

```text id="readme12"
http://localhost:3000
```

---

# Docker Setup

## Build Docker Image

```bash id="readme13"
docker build -t weather-mlops-app .
```

## Run Docker Container

```bash id="readme14"
docker run -p 8000:8000 weather-mlops-app
```

---

# MLflow Setup

## Run Training

```bash id="readme15"
python src/train.py
```

## Start MLflow UI

```bash id="readme16"
mlflow ui
```

MLflow Dashboard:

```text id="readme17"
http://127.0.0.1:5000
```

---

# API Endpoints

## GET /

Health check endpoint

## POST /predict

Predict whether it will rain tomorrow

### Example Input

```json id="readme18"
{
  "Location": 10,
  "Temp9am": 18,
  "Humidity9am": 92,
  "Pressure9am": 1002,
  "RainToday": 1
}
```

### Example Output

```json id="readme19"
{
  "prediction": "Rain Tomorrow ☔"
}
```

## GET /history

Returns recent prediction history

---

# CI/CD Pipeline

Using GitHub Actions:

* Automatic dependency installation
* Backend testing
* Model verification
* Docker image build
* Deployment readiness check

Every push triggers the production pipeline automatically.

---

# Deployment

## Backend Deployment

Deployed using Render

## Frontend Deployment

Deployed using Vercel

---

# Resume Highlight

Built an end-to-end production-grade Weather Prediction MLOps System using FastAPI, React, Docker, MLflow, SQLite, GitHub Actions CI/CD, and cloud deployment with Render and Vercel.

---

# Future Improvements

* PostgreSQL integration
* AWS EC2 deployment
* Kubernetes orchestration
* Prometheus + Grafana monitoring
* Model drift detection
* Automated retraining pipeline
* Authentication system
* User accounts
* Admin analytics dashboard

---

# 👨‍💻 Author

## MD Waheed Pasha

B.Tech Student | Machine Learning Engineer | AI Enthusiast

GitHub: Add your GitHub profile here
LinkedIn: Add your LinkedIn profile here

---

# ⭐ If you like this project, give it a star on GitHub!

This project reflects real ML Engineering + MLOps practices used in industry.
