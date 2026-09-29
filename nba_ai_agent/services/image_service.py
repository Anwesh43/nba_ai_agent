from services.base_http_client import BaseHTTPClient 
import os 
from dotenv import load_dotenv 

load_dotenv()

class ImageService:
    def __init__(self):
        self.client = BaseHTTPClient(baseURL = os.environ["SERP_BASE_URL"])
        self.apiKey = os.environ["SERP_API_KEY"]
        self.limit = 3

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
            imageResults =  response["images_results"]
            results = []
            
            for imageResult in imageResults:
                obj = {}
                obj["thumbnail"] = imageResult["thumbnail"]
                obj["original"] = imageResult["original"]
                obj["imageWidth"] = imageResult["original_width"]
                obj["imageHeight"] = imageResult["original_height"]
                results.append(obj)
                if len(obj) == self.limit:
                    break
            return results 
        except Exception as e:
            print("Error", e)
            return {
                "status": "Error",
                "message": str(e)
            }