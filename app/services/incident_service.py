from collections import Counter
from app.core.constants import ACTIVE_INCIDENT_STATUSES


def analyze_incidents(incidents):

    severity_counter = Counter()
    open_incidents = []

    for incident in incidents:

        severity_counter[incident["severity"]] += 1

        if incident["status"] in ACTIVE_INCIDENT_STATUSES:
            open_incidents.append(incident)

    operational_summary = {
        "total_incidents": len(incidents),
        "open_incidents": len(open_incidents),
        "severity_breakdown": dict(severity_counter),
        "operational_risk": calculate_operational_risk(severity_counter)
    }

    return operational_summary


def calculate_operational_risk(severity_counter):

    if severity_counter.get("Critical", 0) >= 1:
        return "High"

    elif severity_counter.get("High", 0) >= 2:
        return "Elevated"

    return "Normal"