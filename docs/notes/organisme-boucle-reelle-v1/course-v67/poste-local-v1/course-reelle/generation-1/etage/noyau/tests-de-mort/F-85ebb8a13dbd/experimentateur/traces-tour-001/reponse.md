```json
{"experience":[{"executer":{"script":"import json, runpy\nLOI = '{\"biais\":[-0.2,1.0,0.1],\"poids\":[[0.2,0.1],[-1.5,2.2],[0.5,-2.8]],\"type\":\"softmax\"}'\nev = runpy.run_path('tranche/evaluateur_lois_v62.py')\nev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')\n"}}]}
```