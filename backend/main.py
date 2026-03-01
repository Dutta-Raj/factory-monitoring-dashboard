from fastapi.middleware.cors import CORSMiddleware
from metrics import compute_metrics
from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Factory Dashboard API running"}


@app.post("/seed")
def seed_data():

    db: Session = SessionLocal()

    workers = [
        models.Worker(worker_id="W1", name="Alice"),
        models.Worker(worker_id="W2", name="Bob"),
        models.Worker(worker_id="W3", name="Charlie"),
        models.Worker(worker_id="W4", name="David"),
        models.Worker(worker_id="W5", name="Eva"),
        models.Worker(worker_id="W6", name="Frank"),
    ]

    stations = [
        models.Workstation(station_id="S1", name="Assembly"),
        models.Workstation(station_id="S2", name="Packaging"),
        models.Workstation(station_id="S3", name="Inspection"),
        models.Workstation(station_id="S4", name="Welding"),
        models.Workstation(station_id="S5", name="Painting"),
        models.Workstation(station_id="S6", name="Sorting"),
    ]

    db.add_all(workers)
    db.add_all(stations)
    db.commit()

    return {"message": "Sample data inserted"}


@app.post("/events")
def add_event(event: dict):

    db: Session = SessionLocal()

    new_event = models.Event(**event)

    db.add(new_event)
    db.commit()

    return {"message": "event stored"}
@app.get("/metrics")
def get_metrics():

    db: Session = SessionLocal()

    return compute_metrics(db)