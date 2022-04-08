"""
THe module, which is used for transforming the chosen GitHub data to a format, suitable for Freshdesk
"""

import json

def transform_to_freshdesk_data(GitHub_json):
    """
    Choose fields from GitHub response and make it into a "Freshdesk-friendly" Python Object

    :param GitHub_json: JSON response from GitHub
    """
    contact = {
        "name": GitHub_json['name'],
        "email": GitHub_json['email'],
        "address": GitHub_json['location'],
        "description": GitHub_json['bio']
    }

    # Turn Python object into JSON object
    contact_json = json.dumps(contact)

    return contact_json