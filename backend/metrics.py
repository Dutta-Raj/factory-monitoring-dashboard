from sqlalchemy.orm import Session
import models
from collections import defaultdict

def compute_metrics(db: Session):

    events = db.query(models.Event).all()

    worker_stats = defaultdict(lambda: {
        "active": 0,
        "idle": 0,
        "units": 0
    })

    station_stats = defaultdict(lambda: {
        "occupied": 0,
        "units": 0
    })

    total_units = 0

    for e in events:

        if e.event_type == "working":
            worker_stats[e.worker_id]["active"] += 1
            station_stats[e.workstation_id]["occupied"] += 1

        if e.event_type == "idle":
            worker_stats[e.worker_id]["idle"] += 1

        if e.event_type == "product_count":
            worker_stats[e.worker_id]["units"] += e.count
            station_stats[e.workstation_id]["units"] += e.count
            total_units += e.count

    worker_metrics = []

    for w, data in worker_stats.items():

        total = data["active"] + data["idle"]

        utilization = (data["active"] / total * 100) if total > 0 else 0

        worker_metrics.append({
            "worker_id": w,
            "active_time": data["active"],
            "idle_time": data["idle"],
            "utilization": round(utilization,2),
            "units_produced": data["units"]
        })

    station_metrics = []

    for s, data in station_stats.items():

        station_metrics.append({
            "station_id": s,
            "occupancy": data["occupied"],
            "units_produced": data["units"]
        })

    factory_metrics = {
        "total_units": total_units,
        "total_workers": len(worker_metrics)
    }

    return {
        "workers": worker_metrics,
        "stations": station_metrics,
        "factory": factory_metrics
    }