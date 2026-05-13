enterprise_incidents = [
    {
        "incident_id": "INC-8472",
        "service": "Authentication Service",
        "region": "ap-south-1",
        "severity": "Critical",
        "issue": "Login requests failing after deployment rollout",
        "status": "Open"
    },
    {
        "incident_id": "INC-8473",
        "service": "Payment Gateway",
        "region": "us-east-1",
        "severity": "High",
        "issue": "Spike in transaction timeout errors",
        "status": "Investigating"
    },
    {
        "incident_id": "INC-8474",
        "service": "Monitoring Engine",
        "region": "eu-west-1",
        "severity": "Medium",
        "issue": "Alert notifications delayed by 15 minutes",
        "status": "Monitoring"
    }
]

for incident in enterprise_incidents:
    print("=" * 60)
    print(f"Incident ID : {incident['incident_id']}")
    print(f"Service     : {incident['service']}")
    print(f"Region      : {incident['region']}")
    print(f"Severity    : {incident['severity']}")
    print(f"Issue       : {incident['issue']}")
    print(f"Status      : {incident['status']}")