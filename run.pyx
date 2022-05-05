from playerManager import PlayerManager
from battleManager import BattleManager

pm = PlayerManager()
bm = BattleManager(pm)
results = bm.runAllBattles()
results.writeResults("results")
