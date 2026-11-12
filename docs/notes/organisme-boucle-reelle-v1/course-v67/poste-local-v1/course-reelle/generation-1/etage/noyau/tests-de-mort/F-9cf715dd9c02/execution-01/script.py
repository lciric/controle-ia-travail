import json, runpy
LOI = '{"base":{"biais":[0.0,0.6,-0.35],"poids":[[0.0,0.0],[-0.835,1.1],[-0.242,-2.2]],"type":"softmax"},"melange_aveugle":{"lambda":0.03,"probas":[1.0,1.0,1.0]},"type":"transformee"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')