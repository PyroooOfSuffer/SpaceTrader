import requests

class SpaceTraderAPI:
    BASE_URL = "https://api.spacetrader.io/v2"
# region Internal

    def __init__(self, agent_token: str):
        self.limit: int = 1
        self.page: int = 10
        self.headers: dict = {
            "Authorization" : f"Bearer {agent_token}",
            "Accept": "application/json"
        }

    def _request(self, method: str, endpoint: str, params: dict = None, data: dict = None, auth: bool = True):
        url = f"{self.BASE_URL}{endpoint}"
        if auth:
            headers = self.headers
        else:
            headers = {"Accept": "application/json"}
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data
        )
        response.raise_for_status()
        return response.json()

    def _params(self, limit: int = None, page: int = None):
        if not limit:
            limit = self.limit
        if not page:
            page = self.page
        params = {
            "limit": limit,
            "page": page
        }
        return params

# endregion
# region Change self.var

    def set_params(self, limit: int = 10, page: int = 1):
        self.limit = limit
        self.page = page

    def set_new_token(self, agent_token):
        self.headers: dict = {
            "Authorization": f"Bearer {agent_token}",
            "Accept": "application/json"
            }


# endregion
# region Status

    def get_status(self):
        return self._request("GET", "", auth = False)

# endregion
# region Agents

    def register(self, symbol: str, faction: str = "COSMIC", email: str = None):
        if email:
            data = {
                "symbol": symbol,
                "faction" : faction,
                "email" : email
            }
        else:
            data = {
                "symbol" : symbol,
                "faction" : faction
            }
        return self._request("POST", "/register", data = data, auth = False)

    def get_my_agent(self):
        return self._request("GET","/my/agent")

    def list_agent(self, limit: int = None, page: int = None):
        params = self._params(limit, page)
        return self._request("GET", "/agents", params = params, auth = False)

    def get_public_agent(self, symbol: str):
        return self._request("GET", f"/agent/{symbol}", auth = False)

#endregion
# region Contracts

    def list_contract(self, limit: int = None, page: int = None):
        params = self._params(limit, page)
        return self._request("GET","/my/contracts", params = params)

    def get_contract(self, contract: str):
        return self._request("GET", f"/my/contracts/{contract}")

    def accept_contract(self, contract: str):
        return self._request("POST", f"/my/contracts/{contract}/accept")

    def deliver_cargo_to_contract(self, contract: str, ship: str, cargo: str, units: int):
        data = {
            "shipSymbol" : ship,
            "tradeSymbol" : cargo,
            "units" : units
        }
        return self._request("POST", f"/my/contracts/{contract}/deliver", data = data)

    def fulfill_contract(self, contract: str):
        return self._request("POST", f"/contracts/{contract}/fulfill")

#endregion
# region Factions

    def list_faction(self, limit: int = None, page: int = None):
        params = self._params(limit, page)
        return self._request("GET", "/factions", params = params, auth = False)

    def get_faction(self, faction: str):
        return self._request("GET", f"/factions/{faction}")

#endregion
# region Fleet

    def fleet(self): #TODO all fleet requests
        pass

#endregion
# region System

    def system(self): #TODO all system requests
        pass

#endregion