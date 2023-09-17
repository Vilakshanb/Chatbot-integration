import requests
from config import INVESTWELL_API_URL, INVESTWELL_AUTH_NAME, INVESTWELL_AUTH_PASSWORD


def get_investwell_token():
    endpoint = f"{INVESTWELL_API_URL}/auth/getAuthorizationToken"
    headers = {"Content-Type": "application/json"}
    payload = {"authName": INVESTWELL_AUTH_NAME, "password": INVESTWELL_AUTH_PASSWORD}

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json().get("token")
    else:
        # Handle error scenarios
        return None


def get_portfolio_returns(token, filters, group, pan=None):
    endpoint = f"{INVESTWELL_API_URL}/reports/getPortfolioReturns"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    params = {"group": group, "filters": filters}
    if pan:
        params["pan"] = pan

    response = requests.get(endpoint, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        # Handle error scenarios
        return None
