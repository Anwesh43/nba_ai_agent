from services.base_http_client import BaseHTTPClient 
import os 
from dotenv import load_dotenv 

load_dotenv()

class NbaService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["NBA_BASE_URL"])

    def _handleError(self, e):
        print("Error", e)
        return {
            "status": "error",
            "message": str(e)
        }
    
    def getUpComingGames(self):
        try:
            response = self.client.getCall("api/games", qpParams={"page": 1, "pageSize": 20, "sortBy": "date"})
            return response 
        except Exception as e:
            return self._handleError(e)

    def getTopNPlayersInASeason(self, seasonYear : int = 2026, n : int = 5):
        try:
            qpParams = {
                "season": seasonYear,
                "page": 1,
                "pageSize": n
            }
            response = self.client.getCall("api/playertotals", qpParams=qpParams)
            return response 
        except Exception as e:
            return self._handleError(e)

    def getPlayerAdvanceStats(self, playerId : str, seasonYear : int = 2026):
        try:
            qpParams = {
                "playerId": playerId,
                "page": 1,
                "pageSize": 10,
                "season": seasonYear
            }
            response = self.client.getCall("api/playeradvancestats", qpParams=qpParams)
            return response
        except Exception as e:
            return self._handleError(e)

    def getPlayerShotStats(self, playerId : str, seasonYear : int = 2026):
        try:
            qpParams = {
                "playerId": playerId, 
                "page": 1,
                "pageSize": 10, 
                "season": seasonYear
            }
            response = self.client.getCall("api/playershotchart", qpParams=qpParams)
            return response
        except Exception as e:
            return self._handleError(e)
        