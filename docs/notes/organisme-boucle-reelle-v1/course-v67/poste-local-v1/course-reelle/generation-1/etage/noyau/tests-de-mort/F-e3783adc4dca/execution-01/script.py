import json, runpy
LOI = '{"biais":[0.0,0.85,0.35],"poids":[[0.0,0.0],[-0.9,1.2],[0.1,-1.4]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
