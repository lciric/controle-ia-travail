import json, runpy
LOI = '{"biais":[0.0,0.9,0.2],"poids":[[0.0,0.0],[-1.1,1.6],[0.2,-2.0]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')