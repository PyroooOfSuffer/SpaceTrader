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

# region Status

    def get_status(self):
        return self._request("GET", "", auth = False)

# endregion
# region Agents

    def register(self, agent_symbol: str, faction_symbol: str = "COSMIC", email: str = None):
        if email:
            data = {
                "symbol": agent_symbol,
                "faction" : faction_symbol,
                "email" : email
            }
        else:
            data = {
                "symbol" : agent_symbol,
                "faction" : faction_symbol
            }
        return self._request("POST", "/register", data = data, auth = False)

    def get_my_agent(self):
        return self._request("GET","/my/agent")

    def list_agent(self, limit: int = None, page: int = None):
        params = self._params(limit, page)
        return self._request("GET", "/agents", params = params, auth = False)

    def get_public_agent(self, agent_symbol: str):
        return self._request("GET", f"/agent/{agent_symbol}", auth = False)

#endregion
# region Contracts

    def list_contract(self, limit: int = None, page: int = None):
        params = self._params(limit, page)
        return self._request("GET","/my/contracts", params = params)

    def get_contract(self, contract_id: str):
        return self._request("GET", f"/my/contracts/{contract_id}")

    def accept_contract(self, contract_id: str):
        return self._request("POST", f"/my/contracts/{contract_id}/accept")

    def deliver_cargo_to_contract(self, contract_id: str, ship_symbol: str, trade_symbol: str, units: int):
        data = {
            "shipSymbol" : ship_symbol,
            "tradeSymbol" : trade_symbol,
            "units" : units
        }
        return self._request("POST", f"/my/contracts/{contract_id}/deliver", data = data)

    def fulfill_contract(self, contract_id: str):
        return self._request("POST", f"/contracts/{contract_id}/fulfill")

#endregion
# region Factions

    def list_faction(self, limit: int = None, page: int = None):
        params = self._params(limit, page)
        return self._request("GET", "/factions", params = params, auth = False)

    def get_faction(self, faction_symbol: str):
        return self._request("GET", f"/factions/{faction_symbol}")

#endregion
# region Fleet

    def list_ship(self, limit: int = None, page: int = None):
        params = self._params(limit, page)
        return self._request("GET","/my/ships", params=params)

    def purchase_ship(self, ship_type: str, waypoint_symbol: str):
        data = {
            "shipType" : ship_type,
            "waypointSymbol" : waypoint_symbol
        }
        return self._request("POST", "/my/ships", data=data)

    def get_ship(self, ship_symbol: str):
        return self._request("GET", f"/my/ships/{ship_symbol}")

    def get_ship_cargo(self, ship_symbol: str):
        return self._request("GET", f"/my/ships/{ship_symbol}/cargo")

    def orbit_ship(self, ship_symbol: str):
        return self._request("POST", f"/my/ships/{ship_symbol}/orbit")

    def refine_ship(self, ship_symbol: str, trade_symbol: str):
        data = {
            "produce" : trade_symbol
        }
        return self._request("POST", f"/my/ships/{ship_symbol}/refine", data=data)

    def create_chart(self, ship_symbol: str):
        return self._request("GET", f"/my/ships/{ship_symbol}/chart")

    def get_ship_cooldown(self, ship_symbol: str):
        return self._request("GET", f"/my/ships/{ship_symbol}/cooldown")

    def dock_ship(self, ship_symbol: str):
        return self._request("POST", f"/my/ships/{ship_symbol}/dock")

    def create_survey(self, ship_symbol: str):
        return self._request("POST", f"/my/ships/{ship_symbol}/survey")

    def extract_resource(self, ship_symbol: str):
        return self._request("POST", f"/my/ships/{ship_symbol}/extract")


    def siphon_resources(self, ship_symbol: str):
        return self._request("POST", f"/my/ships/{ship_symbol}/siphon")

    def extract_resource_survey(self, ship_symbol: str, survey: dict):
        data = survey
        return self._request("POST", f"/my/ships/{ship_symbol}/extract/survey", data=data)

    def jettison_cargo(self, ship_symbol: str, trade_symbol: str, units: int):
        data = {
            "symbol" : trade_symbol,
            "units" : units
        }
        return self._request("POST", f"/my/ships/{ship_symbol}/jettison", data=data)

    def jump_ship(self, ship_symbol: str, waypoint_symbol: str):
        data = {
            "waypointSymbol" : waypoint_symbol
        }
        return self._request("POST", f"/my/ships/{ship_symbol}/jump", data=data)

    def navigate_ship(self, ship_symbol: str, waypoint_symbol: str):
        data = {
            "waypointSymbol" : waypoint_symbol
        }
        return self._request("POST", f"/my/ships/{ship_symbol}/navigate", data=data)

    def patch_ship_nav(self, ship_symbol: str, flight_mode: str):
        data = {
            "flightMode" : flight_mode
        }
        return self._request("PATCH", f"/my/ships/{ship_symbol}/nav", data=data)

    def get_ship_nav(self, ship_symbol: str):
        return self._request("GET", f"/my/ships/{ship_symbol}/nav")

    def warp_ship(self, ship_symbol: str, waypoint_symbol: str):
        data ={
            "waypointSymbol" : waypoint_symbol
        }
        return self._request("POST", f"/my/ships/{ship_symbol}/warp", data=data)

    def sell_cargo(self, ship_symbol: str, trade_symbol: str, units: int):
        data ={
            "symbol" : trade_symbol,
            "units" : units
        }
        return self._request("POST", f"/my/ships/{ship_symbol}/sell", data=data)

    def scan_system(self, ship_symbol: str):
        return self._request("POST", f"/my/ships/{ship_symbol}/scan/system")

    def scan_waypoints(self, ship_symbol: str):
        return self._request("POST", f"/my/ships/{ship_symbol}/scan/waypoints")

    def scan_ships(self, ship_symbol: str):
        return self._request("POST", f"/my/ships/{ship_symbol}/scan/ships")

    def refuel_ship(self, ship_symbol: str, units: int, from_cargo: bool = False):
        data ={
            "units" : units,
            "fromCargo" : from_cargo
        }
        return self._request("POST", f"/my/ships/{ship_symbol}/refuel", data=data)

    def purchase_cargo(self, ship_symbol: str, trade_symbol: str, units: int):
        data ={
            "symbol" : trade_symbol,
            "units" : units
        }
        return self._request("POST", f"/my/ships/{ship_symbol}/purchase", data=data)

    def transfer_cargo(self, ship_symbol: str, trade_symbol: str, units: int, target_ship_symbol: str):
        data ={
            "tradeSymbol" : trade_symbol,
            "units" : units,
            "shipSymbol" : target_ship_symbol
        }
        return self._request("POST", f"/my/ships/{ship_symbol}/transfer", data=data)

    # TODO negotiate contract and onwards

#endregion
# region System

    def system(self): #TODO all system requests
        pass

#endregion
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