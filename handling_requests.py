"""
The module, which is used for handling requests
"""

import requests
import json
import TokenAuth as ta


def get_github_user(username, token):
    """
    Get chosen GitHub data by username using given an authentication token by using the requsts library

    :param username: GitHub username
    :param token: GitHub authentication token
    """
    git_header = {'Authorization': "Token " + token}
    url = f'https://api.github.com/users/{username}'
    res = requests.get(url, git_header)

    # If the request is successful, print out a confirmation message
    if res.status_code == 200:
        print("GitHub user information fetched successfully, turning it into a Freshdesk contact... \n")

    # Otherwise, print out the response code
    else:
        print(f'Failed to fetch the user information, the response code is {res.status_code}')

    return res


def create_freshdesk_contact(domain, token, contact_info):
    """
    Create a freshdesk contact in a given domain using given an authentication token

    :param domain: Freshdesk domain
    :param token: Freshdesk authentication API token
    :param contact_info: Contact Information in JSON
    """
    headers = {'Content-Type': 'application/json'}
    url = f'https://{domain}.freshdesk.com/api/v2/contacts'
    req = requests.post(url, auth=ta(domain, token), data=contact_info, headers=headers)

    # If the request is successful (HTTP_STATUS_CODE_201), notify with an appropriate message
    if req.status_code == 201:
        print("Contact created successfully, the response is given below \n" + str(req.content) + "\n")
        print("Location Header : " + req.headers['Location'])

    # If the contact already exists, try to update it (HTTP_STATUS_CODE_409)
    elif req.status_code == 409:
        print("Contact already exists, updating the existing contact \n")
        response = json.loads(req.content)
        contact_id = response['errors'][0]['additional_info']['user_id']
        update_existing_contact(domain, token, contact_id, contact_info)

    # Otherwise, print out an error message
    else:
        print("Failed to create contact, response code and errors are displayed below: ")
        response = json.loads(req.content)
        print(f'Response code: {req.status_code} \n')
        print(response["errors"])
    return req


def update_existing_contact(domain, token, contact_id, contact_info):
    """
    Update existing Freshdesk contact, identified by domain and id using given authentication API token

    :param domain: Freshdesk domain
    :param token: Freshdesk API Token
    :param contact_id: Freshdesk Contact ID
    :param contact_info: Contact Information in JSON

    """
    headers = {'Content-Type': 'application/json'}
    url = f'https://{domain}.freshdesk.com/api/v2/contacts/{contact_id}'
    req = requests.put(url, auth=ta(domain, token), data=contact_info, headers=headers)
    if req.status_code == 200:
        print("Contact updated successfully")
    else:
        print("Failed to update contact, errors are displayed below:\n")
        response = json.loads(req.content)
        print(response["errors"])

    return req