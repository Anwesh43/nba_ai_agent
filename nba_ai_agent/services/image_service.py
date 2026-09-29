from services.base_http_client import BaseHTTPClient 
import os 
from dotenv import load_dotenv 

load_dotenv()

class ImageService:
    def __init__(self):
        self.client = BaseHTTPClient(baseURL = os.environ["SERP_BASE_URL"])
        self.apiKey = os.environ["SERP_API_KEY"]
        
    def getImages(self, query : str):
        try:
            qpParams = {
                "engine": "google_images", 
                "api_key": self.apiKey,
                "q": query, 
                "domain": "google.com",
                "hl": "en",
                "gl": "us",
                "location": "Austin, Texas, United States"
            }
            response = self.client.getCall("search", qpParams=qpParams)
            return response["image_results"]
        except Exception as e:
            print("Error", e)
            return {
                "status": "Error",
                "message": str(e)
            }