import json, runpy
LOI = '{"biais":[0.0,0.5,-0.6],"poids":[[0.0,0.0],[-0.835,1.3],[-0.242,-2.5]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')