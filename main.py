import handling_requests as hr
import transform as tr
import json


# Remember to create trial GitHub account and replace the token bellow
GITHUB_TOKEN = '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'
FRESHDESK_TOKEN = 'pzDmWxNKghLhpVJur6NG'


def main():
    # Ask for user GitHub input and FreshDesk domain
    username = input("Please enter your GitHub username: ")
    domain = input("Please enter your Freshdesk domain name: ")

    # Get GitHub user information based on the username
    info = hr.get_github_user(username, GITHUB_TOKEN).json()

    # Transfer GitHub user information to Freshdesk-friendly one
    info_json = tr.transform_to_freshdesk_data(info)

    # Send JSON to Freshdesk domain
    contact_req = hr.create_freshdesk_contact(domain, FRESHDESK_TOKEN, info_json)


if __name__ == '__main__':
    main()
