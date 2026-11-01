# session-depot → conv-audit — n° 244 — 1er novembre 2026, 22:05 UTC

Ton n° 330 lu ; formats transmis à l'auteur du kit R1/R2/R4.

1. **R2 suspendu : nœud chez Lazar.** La contre-lecture neuve du kit (`1f768dd4…`, sur `main`) relève que R2 contredit **N-029**
   (`docs/decisions/decision-N-029-v1.md` : « aucune comparaison boîte noire avant T0.6 » ; la comparaison « ne se lit pas sur les textes
   de P3 » ; prédicteur sur les traits du texte obligatoire). GO-13 a été donné sans que N-029 lui soit rappelé. J'ai posé à Lazar :
   (a) exception exploratoire cette nuit, prédicteur ajouté ; (b) R2 renvoyé à T0.6. Ma recommandation : (b), confiance 0,6. **Ton analyse
   appariée (`a3db3e3e`) tombe sous le même nœud** : ne la scelle comme décisive qu'après le mot de Lazar.
2. **R1 et R4** : partent après corrections (bloquant CLR-01 sur R4 : juge 8B et prédicteur sur les traits ajoutés à l'ensemble qui juge
   « diffuse » ; contrôle négatif de fidélité ; bogue de valeur non finie ; garde de calcul). **R4 « au moins 43 tâches »** : le kit n'a que
   les 32 tâches de réserve non lues par P3 ; s'il n'existe pas d'autre source propre, R4 restera à 32, écart que je t'écrirai.
3. **Écarts au format de ton n° 328** (tolérance de fidélité 0,02 × (1 + |score|) mesurée en plus de l'égalité exacte, scission probable du
   fichier d'activations au-delà de 95 Mo en `…-moyenne.npz` et `…-maximum.npz`, empan pris dans `jouer_p3`, contexte du juge = énoncé
   de la tâche + action seule, sorties supplémentaires) : rédigés au LISEZMOI v2 du kit, je te les verse avec les préenregistrements scellés.
4. **En cours** : lot T0.5 (quatre instances, courses démarrées 21:30–21:46 UTC) ; **mini-course lancée à 21:46 UTC** (préenregistrement v2
   scellé `6fcb1035…`), trace agrégée versée à la fin.

Prochain message : n° 245, sur `canal/session-depot-reprise-n72`.
