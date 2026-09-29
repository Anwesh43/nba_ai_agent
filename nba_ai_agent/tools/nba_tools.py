from services.nba_service import NbaService

nbs = NbaService()

def getUpcomingGames():
    print(f"Calling getUpComningGames tool")
    return nbs.getUpComingGames()

def getTopNPlayersInASeason(seasonYear : int, n : int):
    print(f"Calling getTopNPlayersInASeason in {seasonYear} and top {n}")
    return nbs.getTopNPlayersInASeason(seasonYear=seasonYear, n = n)

def getPlayerAdvanceStats(playerId : int, seasonYear : int):
    print(f"Calling getPlayerAdvancedStats in {seasonYear} for player {playerId}")
    return nbs.getPlayerAdvanceStats(playerId=playerId, seasonYear=seasonYear)

def getPlayerShotStats(playerId : int, seasonYear : int):
    print(f"Calling getPlayerShotStats {playerId} in {seasonYear}")
    return nbs.getPlayerShotStats(playerId=playerId, seasonYear=seasonYear)



