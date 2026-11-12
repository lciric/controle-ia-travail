import json, runpy
LOI = '{"condition":{"indice":1,"seuil":0.0},"si":{"biais":[0.0,0.8,-0.8],"poids":[[0.5,-0.5],[-1.0,1.5],[0.8,-2.0]],"type":"softmax"},"sinon":{"biais":[0.0,0.7,0.4],"poids":[[0.2,0.5],[-1.2,1.2],[0.3,-2.0]],"type":"softmax"},"type":"si_sinon"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')