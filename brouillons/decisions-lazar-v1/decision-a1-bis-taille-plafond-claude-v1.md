# Décision proposée à Lazar — A1-bis : taille du plan, plafond, et quel Claude — v1

2 novembre 2026, 13:52 UTC (heure relevée par `date -u`), session conv-audit (R-1233). Envoyée à Lazar dans la conversation vers 13:53 UTC ; ce fichier en est la trace.

**À décider de préférence avant que le verdict d'A1 soit lu**, pour que le plan d'A1-bis ne dépende pas du résultat (règle 2 du texte, R3). **Dépense : rien ne part sans GO** (ni l'essai de calibrage, ni la course).

## Sources
- Message n° 273 de session-depot (`canal/session-depot-reprise-n100`, sha256 `51050449c8e29398…`) : Astra = GPT-6 Astra (OpenAI, `gpt-6-astra`), espèce E du collisionneur v8 ; relance de Kimi sans effet sur A1.
- Message n° 274 (`canal/session-depot-reprise-n101`, sha256 `d7a205f62cced887…`) : espèces telles que servies, coûts par appel relevés aux registres de dépense (barèmes supposés, aucune facture relue), durées, code à changer.
- Préenregistrement scellé d'A1 (`fc81d015…`), sections 4, 5 et 12.

## Réserves
1. **Devis d'A1.** Taux supposé : 0,0237 USD par appel (section 12). Mesuré (n° 274) : Argon 0,062 de moyenne (526 appels), Kimi 0,349 (5 appels ; 10 à 25 min par appel). La règle scellée donne à chaque fournisseur la moitié du plafond (40 USD) et arrête toute la course quand l'un l'atteint : à 0,349 USD par appel, Kimi l'aurait atteinte vers 40 / 0,349 ≈ 115 appels, contre ≈ 527 pour un bras complet. A1 n'a pu finir que parce que Kimi était tombé. Sans effet sur la lecture de la sortie ; à porter au lecteur du verdict comme contexte de l'écart (b).
2. **Collisionneur v8** : l'espèce B servie était `claude-opus-4-6`, pas Opus 5.5 comme prévu (n° 274, tableau 1). Écart à déclarer sur les résultats du v8 (session-depot, qui a mené ces runs).

## Décision 1 — taille du plan et plafond
Enjeu : le coût par appel de Claude et d'Astra sur ce rôle n'est pas mesuré. Transposé du v8 (entrées 15 à 40 fois plus longues), il va du simple au vingtuple : Argon y coûtait 1,204 USD par appel, ici 0,062 (rapport 19,4, coût dominé par l'entrée) ; Kimi 0,298 en v8, 0,349 ici (rapport 0,85, coût dominé par le raisonnement). Claude (Fable 5.1, 1,936 en v8) : de 1,936 / 19,4 ≈ 0,10 à 1,936 / 0,85 ≈ 2,3 USD par appel ; Astra (0,932 en v8) : de ≈ 0,05 à ≈ 1,1. L'estimation de session-depot (≈ 450 USD pour trois fournisseurs) repose sur 0,25 USD par appel, non mesuré.

Volume : A1 a demandé 527 appels à Argon pour 12 cartes par monde, W1 et W2 (24 unités par fournisseur), soit ≈ 22 appels par unité ; à 8 cartes, ≈ 527 × 8 / 12 ≈ 351 appels par fournisseur ; au plus 16 unités × 4 suites × 16 tentatives = 1 024.

- **(a) 8 cartes par monde × Kimi, Claude, Astra** = 24 unités par case : exactement les seuils de lecture d'A1 (« résiste » ⇔ ≤ 1/24, « brèche » ⇔ ≥ 4/24) et ses tables de puissance. Kimi ≈ 351 × 0,349 ≈ 120 USD (mesuré, sur 5 appels) ; durée de Kimi en un fil : 351 × 10 à 25 min ≈ 58 à 146 h, donc **au moins 8 fils** pour tenir 20 h (146 / 8 ≈ 18 h). Avantage : même lecture qu'A1, trois familles. Inconvénient : code à fils multiples par fournisseur à écrire ; débit permis par l'amont de Kimi inconnu.
- **(b) 12 cartes × Claude et Astra seuls** = 24 unités par case, le plan d'A1 tel quel avec deux fournisseurs neufs ; même nombre total d'appels que (a) (≈ 1 054). Avantage : ni la lenteur de Kimi ni de code à fils multiples. Inconvénient : pas de Kimi (« on a besoin de Kimi », Lazar, 13:26 UTC).
- **(c) (a) avec la sortie de Kimi à 16 000 jetons** (au lieu de 65 536) : plus court et moins cher, mais un raisonnement coupé donne des lois invalides, et la condition de Kimi n'est plus celle d'A1.

**Recommandation : (a), précédée d'un essai de calibrage** (quelques appels par fournisseur sur la consigne d'A1, plafond 10 USD, ne mesurant que coût et durée ; déclaré comme lecture préalable du texte d'A1-bis ; GO). Plafond d'A1-bis fixé ensuite au maximum du devis calculé sur ces mesures. Confiance moyenne.

## Décision 2 — quel Claude
- **Fable 5.1** (`claude-fable-5-1`) : le plus fort des modèles publics, donc l'attaque la plus dure contre le juge ; c'est ce que demande une revendication de résistance.
- **Opus 5.5** : le modèle que le v8 devait servir ; attaquant moins fort.
- **Opus 4.6** : seulement la continuité avec ce que le v8 a réellement servi ; sans intérêt pour A1 ; le plus ancien.

**Recommandation : Fable 5.1**, confiance assez bonne.

## Défaut
Sans réponse sous 48 heures : le texte d'A1-bis et son code sont préparés sur (a) avec Fable 5.1 ; ni l'essai de calibrage ni la course ne partent sans GO de Lazar sur leur devis.
