import json, runpy
LOI = '{"biais":[-0.2,1.0,0.1],"poids":[[0.2,0.1],[-1.5,2.2],[0.5,-2.8]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
