"""
Authentication module
"""

import base64

def TokenAuth(token):
    """Do basic authentication by encoding the token in base 64 and adding :X at the end since that is the format of the Freshdesk API Authentication"""

    auth = base64.b64encode(token.encode('utf-8')).decode()

    return auth