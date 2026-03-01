AI-Powered Worker Productivity Dashboard
Overview

This project implements a full-stack web application that ingests AI-generated events from factory CCTV computer vision systems and visualizes worker and workstation productivity metrics.

The system simulates a manufacturing environment with 6 workers and 6 workstations.
AI events such as working, idle, absent, and product_count are processed to compute productivity metrics and displayed in a dashboard.

Technologies used:

Backend: FastAPI

Database: SQLite

Frontend: React

Charts: Recharts

Containerization: Docker

Architecture
Edge → Backend → Dashboard Flow
AI CCTV Cameras
       ↓
Computer Vision Model
       ↓
Structured Event JSON
       ↓
FastAPI Backend API
       ↓
SQLite Database
       ↓
Metrics Computation Engine
       ↓
React Dashboard
Edge Layer

AI CCTV cameras detect worker activity using computer vision and send structured events.

Example event:

{
  "timestamp": "2026-01-15T10:15:00Z",
  "worker_id": "W1",
  "workstation_id": "S3",
  "event_type": "working",
  "confidence": 0.93,
  "count": 1
}
Backend Layer

The backend:

receives events via API

stores events in the database

computes productivity metrics

exposes APIs to the dashboard

Dashboard Layer

The frontend dashboard visualizes:

factory productivity metrics

worker utilization

workstation production rates