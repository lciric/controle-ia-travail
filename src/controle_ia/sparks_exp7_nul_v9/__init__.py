"""SPARKS-EXP7-NUL v9 : la v8, avec le protocole du tir réel complété (contre-lecture du delta v5 → v8, points 5, 10 à 19
et 31) et la détection d'une boucle de redémarrage par l'amorce elle-même. Neufs :
- `vast_lecture` : offres filtrées (« gpu », une carte) et prix tirés de l'offre retenue par une règle écrite ; inventaire
  par `show instances --raw` lu en JSON strict et filtré par identifiant ; verdict de boucle sur trois lectures ; lignes de
  l'amorce dans le journal de Vast ; sorties brutes effacées après lecture ;
- `tir` : ligne de GO dont le périmètre nomme « SPARKS » et « tir » ;
- `garde_code` (liste fermée v9) ; l'amorce v9 (au redémarrage, sans ordre neuf : boucle présumée, destruction immédiate
  par la minuterie ; chaque redémarrage consigné au registre des démarrages ; ordre « fin » avant la borne ; message de la
  phase causale exact) ; le script d'instance v9 ; le lanceur v9 ; l'essai v9 ; le banc v9.
"""
