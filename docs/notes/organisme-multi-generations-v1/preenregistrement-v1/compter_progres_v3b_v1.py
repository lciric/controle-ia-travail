# Compte, sur les 12 parties scellées v3b (condition regroupement), les composantes captées
# neuves après la génération 1 (champ `captes`). Lecture seule.
import json, sys
dossier = sys.argv[1]
n = 0
for w in range(12):
    d = json.load(open('%s/generations-a2-v3b-monde-%d.json' % (dossier, w)))['resultat']
    c = [set(x['captes']) for x in d['generations']]
    neuves2, neuves3 = len(c[1] - c[0]), len(c[2] - c[1])
    n += (neuves2 + neuves3) > 0
    print(w, d['composantes'], len(c[0]), neuves2, neuves3)
print('mondes avec composante neuve apres la generation 1 :', n, 'sur 12')
