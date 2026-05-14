from fastapi import FastAPI
from app.datasets.sample_incidents import enterprise_incidents
from app.services.incident_service import analyze_incidents
from app.services.ai_engine import generate_incident_analysis
from app.models.incident_models import IncidentRequest


app = FastAPI(
    title="Incident Intelligence Platform",
    description="""
AI-powered operational incident intelligence platform designed for enterprise support environments.

Core capabilities include:
- Incident retrieval
- Operational severity analysis
- AI-assisted resolution workflows
- Incident intelligence enrichment
""",
    version="1.0.0",
    contact={
        "name": "Engineering Team"
    }
)


@app.get(
    "/",
    tags=["System"]
)
def home():

    return {
        "message": "Incident Intelligence Platform API is running"
    }


@app.get(
    "/incidents",
    tags=["Incidents"],
    summary="Retrieve enterprise incidents",
    description="Fetches all currently available enterprise operational incidents."
)
def get_incidents():

    return {
        "total_incidents": len(enterprise_incidents),
        "incidents": enterprise_incidents
    }


@app.get(
    "/incidents/summary",
    tags=["Incident Intelligence"],
    summary="Generate operational incident summary",
    description="Provides operational insights and severity analysis for enterprise incidents."
)
def incident_summary():

    summary = analyze_incidents(enterprise_incidents)

    return summary


@app.get(
    "/incidents/ai-analysis",
    tags=["AI Intelligence"],
    summary="Generate AI-powered incident analysis",
    description="Uses an LLM to generate operational incident assessment and recommendations."
)
def ai_incident_analysis():

    incident = enterprise_incidents[0]

    analysis = generate_incident_analysis(incident)

    return {
        "incident_id": incident["incident_id"],
        "operational_analysis": analysis
    }


@app.post(
    "/incidents/analyze",
    tags=["AI Intelligence"],
    summary="Analyze a submitted enterprise incident",
    description="Accepts incident payloads and generates operational intelligence analysis."
)
def analyze_dynamic_incident(incident: IncidentRequest):

    incident_payload = incident.dict()

    analysis = generate_incident_analysis(incident_payload)

    return {
        "submitted_incident": incident_payload,
        "operational_analysis": analysis
    }