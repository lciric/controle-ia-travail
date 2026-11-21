# Comparaison des phrases du lecteur neuf et des phrases rendues par le code — lecture des sondes de l'étape B bis par la lentille publique — v1

Lecteur : `lecture/lecteur_independant_lentilles_bbis_v1.py` (n'importe aucun module du code de la lecture ; recalcule les libellés par le « Seuil » gelé, les jetons communs par les identifiants). Code : `phrases-code-lentilles-bbis-v1.json` (`0c706569…`). Égalité : mêmes phrases par ligne, comme ensemble ; « même ordre » rapporte l'ordre des phrases de famille (non fixé par le texte). Les phrases elles-mêmes sont dans `description-v1.md` (celles du lecteur) et `phrases-code-lentilles-bbis-v1.json` (celles du code) ; sortie complète : `comparaison-phrases-lecteur-code-v1.json`.

**Bilan** : 174 lignes, 174 égales, **0 désaccord** ; 0 libellé différent ; 0 jeton commun différent ; 0 clé présente d'un seul côté ; ordre différent sur 100 lignes (ordre des deux phrases de famille seulement).

| direction (ou paire) | libellé du lecteur | phrases du lecteur | phrases du code | égales | même ordre |
|---|---|---|---|---|---|
| `P-instruit/e1/enc/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e1/enc/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e1/enc/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e1/enc/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e1/enc/w/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-S25/e0/enc/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e0/enc/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e0/enc/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e0/enc/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e0/enc/w/poles` | intermédiaire | 0 | 0 | oui | oui |
| `P-S25/e0/enc/q/logits/+` | intermédiaire | 3 | 3 | oui | non |
| `P-S25/e0/enc/q/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e0/enc/q/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e0/enc/q/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e0/enc/q/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-S50/e0/enc/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e0/enc/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e0/enc/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e0/enc/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e0/enc/w/poles` | non distincte du nul | 1 | 1 | oui | oui |
| `P-S75/e0/enc/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e0/enc/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e0/enc/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e0/enc/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e0/enc/w/poles` | non distincte du nul | 1 | 1 | oui | oui |
| `P-S75/e1/sonde/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e1/sonde/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e1/sonde/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e1/sonde/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e1/sonde/w/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-S75/e1/enc/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e1/enc/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e1/enc/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e1/enc/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e1/enc/w/poles` | non distincte du nul | 1 | 1 | oui | oui |
| `P-S100/e0/enc/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e0/enc/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e0/enc/w/publique/+` | intermédiaire | 3 | 3 | oui | non |
| `P-S100/e0/enc/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e0/enc/w/poles` | intermédiaire | 0 | 0 | oui | oui |
| `P-S100/e1/enc/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e1/enc/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e1/enc/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e1/enc/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e1/enc/w/poles` | intermédiaire | 0 | 0 | oui | oui |
| `P-instruit/e0/sonde/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e0/sonde/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e0/sonde/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e0/sonde/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e0/sonde/w/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-instruit/e0/enc/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e0/enc/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e0/enc/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e0/enc/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e0/enc/w/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-instruit/e1/sonde/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e1/sonde/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e1/sonde/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-instruit/e1/sonde/w/publique/-` | concentrée au-delà des deux nuls | 3 | 3 | oui | non |
| `P-instruit/e1/sonde/w/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-S50/e1/enc/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e1/enc/w/logits/-` | intermédiaire | 3 | 3 | oui | non |
| `P-S50/e1/enc/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e1/enc/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e1/enc/w/poles` | non distincte du nul | 1 | 1 | oui | oui |
| `P-S75/e0/sonde/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e0/sonde/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e0/sonde/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e0/sonde/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S75/e0/sonde/w/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-S100/e0/sonde/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e0/sonde/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e0/sonde/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e0/sonde/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e0/sonde/w/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-S100/e1/sonde/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e1/sonde/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e1/sonde/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e1/sonde/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S100/e1/sonde/w/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-S25/e0/sonde/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e0/sonde/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e0/sonde/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e0/sonde/w/publique/-` | intermédiaire | 3 | 3 | oui | non |
| `P-S25/e0/sonde/w/poles` | intermédiaire | 0 | 0 | oui | oui |
| `P-S25/e0/sonde/q/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e0/sonde/q/logits/-` | intermédiaire | 3 | 3 | oui | non |
| `P-S25/e0/sonde/q/publique/+` | intermédiaire | 3 | 3 | oui | non |
| `P-S25/e0/sonde/q/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e0/sonde/q/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-S25/e1/sonde/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e1/sonde/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e1/sonde/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e1/sonde/w/publique/-` | intermédiaire | 3 | 3 | oui | non |
| `P-S25/e1/sonde/w/poles` | intermédiaire | 0 | 0 | oui | oui |
| `P-S25/e1/sonde/q/logits/+` | concentrée au-delà des deux nuls | 3 | 3 | oui | non |
| `P-S25/e1/sonde/q/logits/-` | concentrée au-delà des deux nuls | 3 | 3 | oui | non |
| `P-S25/e1/sonde/q/publique/+` | concentrée au-delà des deux nuls | 3 | 3 | oui | non |
| `P-S25/e1/sonde/q/publique/-` | concentrée au-delà des deux nuls | 3 | 3 | oui | non |
| `P-S25/e1/sonde/q/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-S25/e1/enc/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e1/enc/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e1/enc/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e1/enc/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e1/enc/w/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-S25/e1/enc/q/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e1/enc/q/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e1/enc/q/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e1/enc/q/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S25/e1/enc/q/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-S50/e0/sonde/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e0/sonde/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e0/sonde/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e0/sonde/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e0/sonde/w/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-S50/e0/sonde/q/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e0/sonde/q/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e0/sonde/q/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e0/sonde/q/publique/-` | intermédiaire | 3 | 3 | oui | non |
| `P-S50/e0/sonde/q/poles` | concentrée au-delà des deux nuls | 1 | 1 | oui | oui |
| `P-S50/e1/sonde/w/logits/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e1/sonde/w/logits/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e1/sonde/w/publique/+` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e1/sonde/w/publique/-` | non distincte du nul | 3 | 3 | oui | non |
| `P-S50/e1/sonde/w/poles` | intermédiaire | 0 | 0 | oui | oui |
| `sonde-lecteur:P-instruit/e0/sonde/w~P-instruit/e0/enc/w` | comparaison | 1 | 1 | oui | oui |
| `sonde-lecteur:P-instruit/e1/sonde/w~P-instruit/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `plis:P-instruit/e0/sonde/w~P-instruit/e1/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `plis:P-instruit/e0/enc/w~P-instruit/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `sonde-lecteur:P-S25/e0/sonde/w~P-S25/e0/enc/w` | comparaison | 1 | 1 | oui | oui |
| `sonde-lecteur:P-S25/e0/sonde/q~P-S25/e0/enc/q` | comparaison | 1 | 1 | oui | oui |
| `sonde-lecteur:P-S25/e1/sonde/w~P-S25/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `sonde-lecteur:P-S25/e1/sonde/q~P-S25/e1/enc/q` | comparaison | 1 | 1 | oui | oui |
| `plis:P-S25/e0/sonde/w~P-S25/e1/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `plis:P-S25/e0/sonde/q~P-S25/e1/sonde/q` | comparaison | 1 | 1 | oui | oui |
| `plis:P-S25/e0/enc/w~P-S25/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `plis:P-S25/e0/enc/q~P-S25/e1/enc/q` | comparaison | 1 | 1 | oui | oui |
| `sonde-lecteur:P-S50/e0/sonde/w~P-S50/e0/enc/w` | comparaison | 1 | 1 | oui | oui |
| `sonde-lecteur:P-S50/e1/sonde/w~P-S50/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `plis:P-S50/e0/sonde/w~P-S50/e1/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `plis:P-S50/e0/enc/w~P-S50/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `sonde-lecteur:P-S75/e0/sonde/w~P-S75/e0/enc/w` | comparaison | 1 | 1 | oui | oui |
| `sonde-lecteur:P-S75/e1/sonde/w~P-S75/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `plis:P-S75/e0/sonde/w~P-S75/e1/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `plis:P-S75/e0/enc/w~P-S75/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `sonde-lecteur:P-S100/e0/sonde/w~P-S100/e0/enc/w` | comparaison | 1 | 1 | oui | oui |
| `sonde-lecteur:P-S100/e1/sonde/w~P-S100/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `plis:P-S100/e0/sonde/w~P-S100/e1/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `plis:P-S100/e0/enc/w~P-S100/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S25/e0/sonde/w~P-S50/e0/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S25/e0/sonde/w~P-S75/e0/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S25/e0/sonde/w~P-S100/e0/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S50/e0/sonde/w~P-S75/e0/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S50/e0/sonde/w~P-S100/e0/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S75/e0/sonde/w~P-S100/e0/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S25/e0/sonde/q~P-S50/e0/sonde/q` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S25/e0/enc/w~P-S50/e0/enc/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S25/e0/enc/w~P-S75/e0/enc/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S25/e0/enc/w~P-S100/e0/enc/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S50/e0/enc/w~P-S75/e0/enc/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S50/e0/enc/w~P-S100/e0/enc/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S75/e0/enc/w~P-S100/e0/enc/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S25/e1/sonde/w~P-S50/e1/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S25/e1/sonde/w~P-S75/e1/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S25/e1/sonde/w~P-S100/e1/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S50/e1/sonde/w~P-S75/e1/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S50/e1/sonde/w~P-S100/e1/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S75/e1/sonde/w~P-S100/e1/sonde/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S25/e1/enc/w~P-S50/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S25/e1/enc/w~P-S75/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S25/e1/enc/w~P-S100/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S50/e1/enc/w~P-S75/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S50/e1/enc/w~P-S100/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
| `doses:P-S75/e1/enc/w~P-S100/e1/enc/w` | comparaison | 1 | 1 | oui | oui |
