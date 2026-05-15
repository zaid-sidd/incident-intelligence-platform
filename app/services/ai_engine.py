import os

from openai import OpenAI
from dotenv import load_dotenv

from app.services.retrieval_service import retrieve_similar_incidents

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_incident_analysis(incident):

    similar_incidents = retrieve_similar_incidents(
        incident["service"]
    )

    historical_context = ""

    for similar in similar_incidents:

        historical_context += f"""
Historical Incident:
Service: {similar['service']}
Pattern: {similar['issue_pattern']}
Resolution: {similar['resolution']}
"""

    try:

        prompt = f"""
You are an enterprise incident management assistant.

Analyze the following production incident and provide:

1. Business impact
2. Probable root cause
3. Recommended immediate action

Incident Details:
Service: {incident['service']}
Severity: {incident['severity']}
Issue: {incident['issue']}
Status: {incident['status']}

Relevant Historical Context:
{historical_context}

Provide a concise operational response.
"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You assist enterprise operations teams with incident analysis."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return {
            "business_impact": response.choices[0].message.content,
            "analysis_source": "openai",
            "historical_matches_found": len(similar_incidents)
        }

    except Exception:

        return {
            "business_impact": "Authentication failures may impact active user sessions and service accessibility.",
            "probable_root_cause": "Recent deployment rollout may have introduced authentication instability or configuration mismatch.",
            "recommended_action": "Rollback recent deployment changes, verify authentication service logs, and monitor error rates closely.",
            "analysis_source": "fallback-engine",
            "historical_matches_found": len(similar_incidents)
        }