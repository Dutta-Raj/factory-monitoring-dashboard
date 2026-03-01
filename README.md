🏭 AI-Powered Worker Productivity Dashboard

A full-stack factory monitoring dashboard that ingests AI-generated events from CCTV computer vision systems and visualizes worker and workstation productivity metrics.

The system simulates a manufacturing factory with 6 workers and 6 workstations, processes AI activity events, and computes productivity metrics displayed in a dashboard.

📊 Dashboard Preview

Factory productivity metrics including:

Worker utilization

Workstation production

Factory-level performance

Production rate monitoring

✨ Features
📡 AI Event Ingestion

Accepts AI-generated CCTV events

JSON-based event ingestion API

Supports activity types:

working

idle

absent

product_count

Example event:

{
 "timestamp": "2026-01-15T10:15:00Z",
 "worker_id": "W1",
 "workstation_id": "S3",
 "event_type": "working",
 "confidence": 0.93,
 "count": 1
}
👷 Worker Productivity Metrics

The system calculates:

Total active time

Total idle time

Utilization percentage

Total units produced

Units produced per hour

🏭 Workstation Metrics

Each workstation shows:

Occupancy time

Utilization percentage

Total production count

Throughput rate

🏢 Factory-Level Analytics

Factory dashboard displays:

Total productive time

Total production count

Average worker utilization

Overall production rate

🔄 Auto Data Refresh

The dashboard automatically refreshes metrics periodically to simulate real-time factory monitoring systems.

🛠 Tech Stack
Backend

Python

FastAPI

REST APIs

Frontend

React

Recharts (charts)

Axios

Database

SQLite

Containerization

Docker

📁 Project Structure
factory-monitoring-dashboard

backend
│
├── main.py
├── database.py
├── models.py
├── seed.py
└── requirements.txt

frontend
│
├── src
├── public
└── package.json

Dockerfile
docker-compose.yml
README.md
🚀 Local Setup Instructions
Prerequisites

Python 3.9+

Node.js

npm

Git

1️⃣ Clone Repository
git clone https://github.com/Dutta-Raj/factory-monitoring-dashboard.git
cd factory-monitoring-dashboard
2️⃣ Run Backend
cd backend

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs
3️⃣ Run Frontend
cd frontend

npm install
npm start

Frontend runs at:

http://localhost:3000
🐳 Docker Setup

Run the full application using Docker.

docker-compose up --build

This will start:

Backend API

Frontend dashboard

Database

⚙️ System Architecture
AI CCTV Cameras
        ↓
Computer Vision Model
        ↓
Structured Event JSON
        ↓
FastAPI Backend
        ↓
SQLite Database
        ↓
Metrics Engine
        ↓
React Dashboard
📡 Handling Intermittent Connectivity

Edge devices may temporarily lose connectivity.
To address this:

events are buffered locally

data is sent when connection is restored

timestamps ensure correct ordering

🔁 Handling Duplicate Events

Duplicate events may occur due to network retries.

The system handles this by:

validating event timestamps

filtering duplicate event IDs

idempotent API ingestion

⏱ Handling Out-of-Order Timestamps

Edge devices may send delayed events.

The backend:

sorts events by timestamp

recalculates metrics if needed

maintains accurate productivity calculations

🤖 Model Drift Detection

Computer vision models may degrade over time.

Drift can be detected using:

abnormal confidence scores

sudden productivity pattern changes

anomaly detection pipelines

Retraining can be triggered using updated factory datasets.

📈 Scaling to 100+ Cameras

To support large factories:

Horizontal Backend Scaling

Multiple API servers behind a load balancer.

Message Queues

Use systems like:

Kafka

RabbitMQ

for large event pipelines.

Distributed Databases

Use scalable databases such as:

PostgreSQL

TimescaleDB

Cassandra

Stream Processing

Use:

Apache Spark

Apache Flink

for real-time analytics.

📌 Future Improvements

Real camera integration

Worker safety alerts

AI anomaly detection

Predictive maintenance analytics

Multi-factory monitoring
