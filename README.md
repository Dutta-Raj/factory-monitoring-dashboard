# 🏭 AI-Powered Worker Productivity Dashboard

A full-stack factory monitoring dashboard that ingests AI-generated events from CCTV computer vision systems and visualizes worker and workstation productivity metrics.

## 📋 **Live Demo**
- **Frontend Dashboard**: [https://frontend-gold-nine-13.vercel.app/](https://frontend-gold-nine-13.vercel.app/)
- **Backend API**: [https://factory-monitoring-dashboard.onrender.com](https://factory-monitoring-dashboard.onrender.com)
- **API Documentation**: [https://factory-monitoring-dashboard.onrender.com/docs](https://factory-monitoring-dashboard.onrender.com/docs)
- **GitHub Repository**: [https://github.com/Dutta-Raj/factory-monitoring-dashboard](https://github.com/Dutta-Raj/factory-monitoring-dashboard)

---

## ✨ **Features**
- 📡 **AI Event Ingestion** - REST API that accepts JSON events from CCTV systems
- 👷 **Worker Metrics** - Active time, idle time, utilization %, units produced, units/hour
- 🏭 **Workstation Metrics** - Occupancy time, utilization %, production count, throughput rate
- 📊 **Factory Analytics** - Total productive time, production count, average utilization, production rate
- 🔄 **Auto Data Refresh** - Dashboard updates automatically to simulate real-time monitoring

---

## 🛠 **Tech Stack**
| Layer | Technology |
|-------|------------|
| **Backend** | FastAPI (Python) |
| **Frontend** | React with Recharts |
| **Database** | SQLite |
| **Deployment** | Render (backend) + Vercel (frontend) |
| **Containerization** | Docker & Docker Compose |

---

## 📁 **Project Structure**
factory-monitoring-dashboard/
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── seed.py
│ └── requirements.txt
├── frontend/
│ ├── src/
│ │ ├── App.js
│ │ ├── config.js
│ │ └── ...
│ ├── public/
│ └── package.json
├── docker-compose.yml
├── Dockerfile
├── README.md
└── render.yaml

text

---

## 🚀 **Local Setup Instructions**

### Prerequisites
- Python 3.9+
- Node.js 16+
- npm
- Git

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Dutta-Raj/factory-monitoring-dashboard.git
cd factory-monitoring-dashboard
2️⃣ Run Backend
bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
uvicorn main:app --reload
Backend runs at: http://127.0.0.1:8000

3️⃣ Run Frontend
bash
cd frontend
npm install
npm start
Frontend runs at: http://localhost:3000

4️⃣ Initialize Database
bash
curl -X POST http://127.0.0.1:8000/api/refresh
🐳 Docker Setup
bash
docker-compose up --build
This starts both backend and frontend containers.

⚙️ System Architecture
text
AI CCTV Cameras
        ↓
Computer Vision Model
        ↓
Structured Event JSON
        ↓
FastAPI Backend (Render)
        ↓
SQLite Database
        ↓
Metrics Engine
        ↓
React Dashboard (Vercel)
📡 API Endpoints
Method	Endpoint	Description
POST	/api/events	Ingest AI events
GET	/api/metrics	Fetch all metrics
POST	/api/refresh	Reset with sample data
GET	/api/health	System health check
Sample Event
json
{
  "timestamp": "2026-03-02T10:15:00Z",
  "worker_id": "W1",
  "workstation_id": "S3",
  "event_type": "working",
  "confidence": 0.93,
  "count": 1
}
📊 Metrics Calculated
Worker Level
Total Active Time: Time spent in "working" state

Total Idle Time: Time spent in "idle" state

Utilization %: (Active Time / Total Time) × 100

Units Produced: Sum of product_count events

Units Per Hour: Units / Active Time (hours)

Workstation Level
Occupancy Time: Total time worker present

Utilization %: (Occupied Time / Total Time) × 100

Units Produced: Sum of product_count at station

Throughput Rate: Units / Occupied Time (hours)

Factory Level
Total Productive Time: Sum of all workers' active time

Total Production: Sum of all units produced

Average Production Rate: Total Units / Total Productive Time

Average Utilization: Mean of workers' utilization

🔧 Handling Edge Cases
Intermittent Connectivity
Edge devices buffer events locally when offline and send batched events when connection is restored. The backend accepts batches with timestamps and validates event order.

Duplicate Events
Each event is checked against a cache of recent event signatures (timestamp + worker + workstation + type). Duplicates within 5 minutes are rejected.

Out-of-Order Timestamps
A buffer holds events for 30 seconds, sorts them by timestamp, then processes in correct order. Events older than 24 hours are rejected.

🤖 Model Management
Versioning
Events include a model_version field. A model registry table tracks all deployed models with their metadata and performance metrics.

Drift Detection
Data Drift: Compare confidence score distributions using Jensen-Shannon divergence

Concept Drift: Monitor correlation between working events and actual production

Performance Drift: Compare against human-labeled ground truth (1% sample)

Retraining Triggers
Drift score > 0.15 for 3 consecutive days

Production correlation < 0.7 for 24 hours

Weekly scheduled retraining

Manual trigger via admin UI

📈 Scaling Strategy
5 → 100+ Cameras
Scale	Architecture
5-10 cameras	Single FastAPI + SQLite
10-50 cameras	Load balancer + multiple API servers + PostgreSQL
50-500 cameras	Kafka event streaming + TimescaleDB + Spark streaming
Multi-Site
Each factory runs its own local cluster (Kafka + TimescaleDB). Daily snapshots sync to a central data lake for global analytics. The HQ dashboard shows aggregated metrics across all sites.

🚀 Deployment
Backend (Render)
Connected to GitHub for auto-deploys

Environment variables set in dashboard

Root directory: /backend

Build command: pip install -r requirements.txt

Start command: uvicorn main:app --host 0.0.0.0 --port $PORT

Frontend (Vercel)
Connected to GitHub

Root directory: /frontend

Environment variable: REACT_APP_API_URL=https://factory-monitoring-dashboard.onrender.com

📌 Future Improvements
Real camera integration

Worker safety alerts

Predictive maintenance

Mobile app for supervisors

Custom report builder

Email/SMS alerts

📬 Contact
Rajdeep Dutta
Email: rajdeepdutta104@gmail.com
GitHub: github.com/Dutta-Raj

