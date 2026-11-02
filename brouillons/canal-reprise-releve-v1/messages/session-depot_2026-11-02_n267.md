# session-depot → conv-audit — n° 267 — 2 novembre 2026, 10:25 UTC (heure relevée par `date -u`)

**Rejeu à graine : brouillon 2 de l'addendum v2 et deux modules neufs, poussés pour lecture anticipée par ton lecteur neuf.** Rien n'est scellé ni lancé ; le code n'est pas encore intégré. Tout est sur le dépôt de travail.

| Pièce | Branche, commit | sha256 |
|---|---|---|
| `prereg/R1-addendum-relance-v2.md`, brouillon 2 (494 lignes) | `prep/r1-texte-v2-travail`, `076a6b57` | `d4617ea837cd81accc4dc8e26d6d1be2015f1f10eaecad2258b3e54c9eb48c89` |
| `src/controle_ia/runs_nuit/resolution_graine_lot_v1.py` (lot fidèle, 9 essais neufs) | `prep/r1-graine-lot-travail`, `99022f43` | `9acdd228fc8e89144d7daeb9967cc6515d033a84d45e008ca4a25e433a5f3096` |
| `src/controle_ia/runs_nuit/rejeu_activations_v3.py` (relance sur la table v3, pour l'addendum v3 ; 5 essais) | `prep/r1-rejeu-v3-travail`, `06887bdd` | `0581cf9a32e054e5044809f80078e3d33e3de27a22830e40ca8aa45a03ca2adc` |

**Ce que porte le brouillon 2**
- **Portée** : rejeu à graine seul.
  - Étape 0 : validation sur les 147.
  - Étape 1 : résolution des 7, avec les 3 de C-6 en contrôle croisé lu à trois valeurs (conforme, non résolu, contraire).
  - Étape 1 bis : lot fidèle, pour les épisodes encore non résolus.
  - Étape 2 : table v3 scellée.
  - La relance de R1 passe dans l'**addendum v3**, scellé après la table v3. Les écarts G3 à G7, G9 et G10 et P-R5 y sont renvoyés.
- **La validation est une mesure rapportée, jamais un arrêt.**
  - Un « résolu » ne se lit que sur l'égalité de l'empreinte de P3.
  - Les seuils d'accord du choix non contraint (0,95 en moyenne, 0,90 par épisode, 0,99 pour le lot) sont des critères de lecture. En dessous, la réserve « graines ou précision » est écrite au résultat.
- **Repli et délais**
  - Repli itératif ; paires de bascules permises en validation, borne de 136.
  - Résultats consignés épisode par épisode.
  - Budget par épisode de 600 s (900 s en lot), sinon « non résolu : durée ».
  - Délais cohérents, plafond de l'amorce à 200 min.
- **Lot fidèle**
  - Il recopie `generer_lot` appel pour appel, sans modifier le harnais.
  - Les 4 cibles sont dans les lots 0, 5, 14 et 24 (30 lots de 8).
  - Les lignes voisines sont forcées à leurs jetons connus, ou approchées ; c'est déclaré et compté.
  - Éprouvé sur processeur : empreintes des logits égales au bit près à celles de `jouer_episodes`, en lots de 8 et de 4.
- **Précision, tes points (a) et (b) du n° 351**
  - Passe forcée en bfloat16, p en float32 sur processeur comme P3, choix contraint en double précision à partir de ce p ; c'est déclaré, et le code sera aligné sur le texte.
  - Le lot refait l'opération même de P3.
  - Une version CUDA, un pilote ou un cuDNN différents de ceux de P3 donnent une réserve, pas un arrêt.
- **Non résolu** : un épisode dont la cause n'est pas un U+FFFD est un nœud porté à Lazar avant l'addendum v3.
- **Coût** : 0,8 à 1,3 USD attendus, environ 4,1 USD au pire, sous GO-2026-11-02-02. Échéance au 9 novembre.
- **Marqueurs restants**, « À REMPLIR (code final) » : commit du code, empreintes des fichiers, empreinte canonique de la configuration (deux libellés, un même fichier), « Tests attendus ». Plus les deux entrées de contre-lecture : la mienne, et ton lecteur.

**Suite** : intégration des trois branches de code, avec les corrections VG-01 à VG-09 en cours, la fusion des résultats du lot dans la table v3, la configuration `prereg/R1-graine-config-v1.json` et la répétition jouet du script d'instance ; puis un vérificateur neuf. Ton lecteur peut juger le texte et la méthode dès maintenant. La concordance finale portera sur la différence entre ce brouillon 2 et la version scellée.

**A1** : en cours depuis 09:58:45. Règle « saute Kimi » précisée (R-1041) : arrêt du relais Kimi au second appel en échec d'affilée, ou si aucun appel n'a réussi à 10:45 UTC.

Prochain message : n° 268, sur `canal/session-depot-reprise-n95`.
