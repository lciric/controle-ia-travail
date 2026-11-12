import json, runpy
LOI = r'{"lois":{"0":{"biais":[0.0,1.0,0.3],"poids":[[0.0,0.0],[-1.2,1.7],[0.3,-2.1]],"type":"softmax"},"1":{"biais":[0.0,0.8,0.2],"poids":[[0.0,0.0],[-1.1,1.9],[0.2,-2.2]],"type":"softmax"}},"type":"par_sous_population"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
import csv
with open('gains.csv', encoding='utf-8', newline='') as f:
    valeurs = [float(ligne['gain']) for ligne in csv.DictReader(f)]
print('RESULTAT: ' + repr(sum(valeurs) / len(valeurs)))