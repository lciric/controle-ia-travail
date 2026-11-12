import csv
import json
import runpy

LOI = '{"biais":[0.0,0.6,-0.35],"poids":[[0.0,0.0],[-0.835,1.1],[-0.242,-2.2]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')

with open('gains.csv', encoding='utf-8', newline='') as fichier:
    gains = [float(ligne['gain']) for ligne in csv.DictReader(fichier) if ligne['gain'] != '']
print('RESULTAT: ' + repr(sum(gains) / len(gains)))