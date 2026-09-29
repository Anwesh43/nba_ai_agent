from services.nba_service import NbaService
from services.image_service import ImageService 

nbs = NbaService()
imageService = ImageService()

def getUpcomingGames():
    print(f"Calling getUpComningGames tool")
    return nbs.getUpComingGames()

def getTopNPlayersInASeason(seasonYear : int, n : int):
    print(f"Calling getTopNPlayersInASeason in {seasonYear} and top {n}")
    return nbs.getTopNPlayersInASeason(seasonYear=seasonYear, n = n)

def getPlayerAdvanceStats(playerId : str, seasonYear : int):
    print(f"Calling getPlayerAdvancedStats in {seasonYear} for player {playerId}")
    return nbs.getPlayerAdvanceStats(playerId=playerId, seasonYear=seasonYear)

def getPlayerShotStats(playerId : str, seasonYear : int):
    print(f"Calling getPlayerShotStats {playerId} in {seasonYear}")
    return nbs.getPlayerShotStats(playerId=playerId, seasonYear=seasonYear)

def getPlayerImages(playerName : str):
    print(f"Calling getPlayerImages tool {playerName}")
    return imageService.getImages(query=playerName)

def writeHTML(htmlStr : str, fileName : str):
    print(f"Calling writeHTML tool for {fileName}")
    with open(fileName, "w") as f:
        f.write(htmlStr)
    return {
        "status": "Success",
        "message": f"Written html to {fileName}, please don't display html to end user"
    }