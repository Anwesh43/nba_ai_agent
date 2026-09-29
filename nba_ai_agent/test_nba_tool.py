from tools.nba_tools import getPlayerShotStats, getTopNPlayersInASeason, getUpcomingGames, getPlayerAdvanceStats
from typing import Dict 
import json 

def writeFile(data : Dict, fileName : str):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"Writing data in {fileName}")

if __name__ == "__main__":
    writeFile(getUpcomingGames(), "test_upcoming_game.json")
    writeFile(getTopNPlayersInASeason(seasonYear=2023, n = 5), "test_topn_players.json")
    writeFile(getPlayerShotStats(playerId="hardeja01", seasonYear=2017), "test_player_shots.json")
    writeFile(getPlayerAdvanceStats(playerId="hardeja01", seasonYear=2017), "test_player_advance_stats.json")
        
    