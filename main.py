import requests

INVESTWELL_API_URL = "https://demo.investwell.app/api/aggregator"
INVESTWELL_AUTH_NAME = "demoapi"
INVESTWELL_AUTH_PASSWORD = "API@1001"


def get_authorization_token():
    endpoint = f"{INVESTWELL_API_URL}/auth/getAuthorizationToken"
    payload = {"authName": INVESTWELL_AUTH_NAME, "password": INVESTWELL_AUTH_PASSWORD}
    response = requests.post(endpoint, json=payload)
    if response.status_code == 200:
        return response.json().get("token")
    return None


def get_portfolio_returns(token, filters):
    endpoint = f"{INVESTWELL_API_URL}/reports/getPortfolioReturns"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"filters": filters}
    response = requests.get(endpoint, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    return None
