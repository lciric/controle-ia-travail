import json, runpy
LOI = '{"biais":[0.0,0.75,0.05],"poids":[[0.0,0.0],[-0.8,1.0],[-0.25,-1.7]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')