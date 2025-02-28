import requests

class SpaceTraderAPI:
    BASE_URL = "https://api.spacetrader.io/v2"

    def __init__(self, agent_token: str):
        self.limit: int = 1
        self.page: int = 10
        self.headers: dict = {
            "Authorization" : f"Bearer {agent_token}",
            "Content-Type": "application/json"
        }

    def set_params(self, limit: int = 10, page: int = 1):
        self.limit = limit
        self.page = page

    def _request(self, method: str, endpoint: str, params: dict = None, data: dict = None, auth: bool = True):
        url = f"{self.BASE_URL}{endpoint}"
        if auth:
            headers = self.headers
        else:
            headers = {"Content-Type" : "application/json"}
        response = requests.request(
            method = method,
            url = url,
            headers = headers,
            params = params,
            json = data
        )
        response.raise_for_status()
        return response.json()

    def get_status(self):
        return self._request("GET", "", auth=False)