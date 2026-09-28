import requests 
from typing import Dict 
from urllib.parse import urlencode 

class BaseHTTPClient:
    def __init__(self, baseURL : str):
        self.baseURL = baseURL 

    def getCall(self, endpoint, qpParams : Dict = {}):
        response = requests.get(f"{self.baseURL}/{endpoint}?{urlencode(qpParams)}")
        response.raise_for_status()
        return response.json()

