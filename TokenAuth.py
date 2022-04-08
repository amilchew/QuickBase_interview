"""
Authentication module
"""

import base64

def TokenAuth(domain, token):
    """Do basic authentication by encoding the token in base 64 and adding :X at the end since that is the format of the Freshdesk API Authentication"""
    domain.header['Authorization'] = 'Basic {}'.format(
        base64.b64encode('token:X'.encode('utf-8')).decode())
    return domain.header