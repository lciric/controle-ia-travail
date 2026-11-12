import json, runpy
LOI = '{"lois":{"0":{"biais":[0.0,0.6,-0.35],"poids":[[0.0,0.0],[-0.835,1.1],[-0.242,-2.2]],"type":"softmax"},"1":{"biais":[0.0,0.58,-0.38],"poids":[[0.0,0.0],[-0.95,1.15],[-0.25,-2.15]],"type":"softmax"}},"type":"par_sous_population"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')