historical_incidents = [
    {
        "incident_id": "HIST-1001",
        "service": "Authentication Service",
        "issue_pattern": "Login requests failing after deployment",
        "resolution": "Rollback deployment and restart authentication pods."
    },
    {
        "incident_id": "HIST-1002",
        "service": "Payment Gateway",
        "issue_pattern": "Transaction timeout spikes during checkout",
        "resolution": "Scale payment processing instances and verify database latency."
    },
    {
        "incident_id": "HIST-1003",
        "service": "Monitoring Engine",
        "issue_pattern": "Delayed alert notifications",
        "resolution": "Reconfigure alert queue workers and restart notification service."
    }
]