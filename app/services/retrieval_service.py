from app.datasets.historical_incidents import historical_incidents


def retrieve_similar_incidents(service_name):

    matching_incidents = []

    for incident in historical_incidents:

        if incident["service"].lower() == service_name.lower():

            matching_incidents.append(incident)

    return matching_incidents