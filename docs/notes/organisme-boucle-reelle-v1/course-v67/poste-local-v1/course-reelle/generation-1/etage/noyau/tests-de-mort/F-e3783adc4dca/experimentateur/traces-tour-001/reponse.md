```json
{"experience":[{"executer":{"script":"import json, runpy\nLOI = '{\"biais\":[0.0,0.85,0.35],\"poids\":[[0.0,0.0],[-0.9,1.2],[0.1,-1.4]],\"type\":\"softmax\"}'\nev = runpy.run_path('tranche/evaluateur_lois_v62.py')\nev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')\n"}}]}
```