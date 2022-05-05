from playerManager import PlayerManager
from battleManager import BattleManager

if __name__ == "__main__":
    print("Starting...")
    pm = PlayerManager()
    bm = BattleManager(pm)
    results = bm.runAllBattles()
    results.writeResults("results")
