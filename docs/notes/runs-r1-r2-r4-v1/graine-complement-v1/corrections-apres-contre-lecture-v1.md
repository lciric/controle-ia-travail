# Corrections du complément de validation après la contre-lecture — v1

- Rédacteur : sous-agent de rédaction de session-depot (Fable 5.1), auteur ni de la contre-lecture ni du brouillon 2.
- Fait le 2 novembre 2026, 23:15 à 23:20 UTC (heures relevées par `date -u`), sur l'arbre
  `/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/wt-complement-v1`, branche
  `prep/r1-complement-v1`, tête `9c084896` ; aucun commit, aucun `git fetch`, aucun fichier `.sha256` créé ni modifié,
  aucun réseau, aucun appel de modèle ; seuls fichiers touchés : le texte corrigé (en place, même nom, texte non scellé ;
  la version relue reste dans l'histoire git), cette note et le patch compagnon.
- Texte corrigé : `prereg/R1-addendum-relance-v2-complement-validation-v1.md`. Version relue :
  `3b7955f14d1ace8759c91d387372381eaa38ae6f288664afecdf0acd1d4aeed9` (vérifiée par `sha256sum` avant toute modification).
  Version corrigée : `294a030cc6f067646a781ab4ee9187d7a70fa260de4d4009a306534e3a3bb055`.
- Contre-lecture appliquée : `contre-lecture-complement-validation-v1.md`
  (`2ef1f19249bd86afbcd2a10b33a6bb7ca5d77940d84f23efdd3ecd465e7f543d`, vérifiée), sections 2 à 5. Toutes ses remarques sont
  acceptées. Différence ligne à ligne de la version relue à la corrigée : `corrections-apres-contre-lecture-v1.patch`
  (`git diff` ; 156 insertions, 43 suppressions ; 19 substitutions exactes, chacune unique dans le texte).
- Vérifications : `problemes()` (`src/controle_ia/prereg.py`) → `['section vide ou à remplir : Contre-lecture']` seulement ;
  un seul marqueur « À REMPLIR », celui de la section « Contre-lecture », laissé pour le scellement ; aucun jeton ni clé ;
  tous les chiffres neufs viennent de la contre-lecture (section 2, I2, section 6) ou du code et du script relus
  (lignes citées ci-dessous, vérifiées sur `src/controle_ia/runs_nuit/resolution_graine_lot_v1.py`, empreinte `5a9982b2…`
  inchangée, et `scripts/r1_resolution_graine_instance_v1.sh`).

## Tableau point par point

Lignes : « relue » = version `3b7955f1…`, « corrigée » = version `294a030c…`.

| Point | Lignes changées (relue → corrigée) | Ce qui a été écrit |
|---|---|---|
| B1 (garde de dépense) | « Liste d'arrêt », l. 359-375 → l. 373-415 | Garde réécrite en **deux tâches planifiées indépendantes**, créées et listées avant la création, consignées avec leurs identifiants dans `registres/decisions.md` : (i) la vérification au plus horaire, telle qu'écrite, avec l'alerte à 30 USD qui porte désormais la demande d'extension du GO dès que la durée projetée dépasse l'heure de destruction ; (ii) une **tâche unique de destruction par identifiant** à `T0 + H`, `H = (39,5 USD − dépenses déjà imputées au GO − disque estimé) / prix horaire − 15 min` (≈ 28,2 h au prix plafond, ≈ 33,3 h à 1,187 USD/h, avant marge : contre-lecture, B1), calculée et écrite dans `registres/depenses.md`, ouvrant une session neuve indépendante (outil Vast et clé par nom seulement), annulée ou reportée seulement sur GO étendu consigné dans `registres/go.md` ; dite « plafond du GO exprimé en heures, non un budget de mesure », la ligne du GO n'interdisant que les budgets de mesure. « La session vérifie le premier départ… » remplacé par le constat des deux tâches avant la création (listing, consignation), puis du premier départ de (i) à la première heure. Conséquence explicite : une destruction pendant l'étape validation perd **toute** la validation (poussée seulement en fin d'étape, script l. 388-395), texte neuf nécessaire. « Risque résiduel » renommé « exposition résiduelle, déclarée et portée comme nœud », avec les raisons de la contre-lecture (plafond d'amorce ≥ 13 055 min, `timeout` extérieur inopérant) |
| B1 (nœud) | « Coût et GO », après l. 401 → l. 447-459 | Phrase de nœud au format du programme : décision (borner le compte Vast ou accepter l'exposition) ; enjeu (≈ 258 à 305 USD si les deux tâches échouent, sept fois le plafond ; une borne de compte la réduirait au crédit disponible) ; options (a) recharge automatique suspendue pendant la course, crédit laissé ≈ 40 USD (avantage, inconvénient), (b) exposition acceptée avec les deux tâches (avantage, inconvénient) ; recommandation (a), confiance ≈ 0,8 ; décision de Lazar avant le lancement, aucun défaut après 48 heures (nœud de dépense) ; lancement sans décision = arrêt |
| B1 (renvois) | l. 101-103 → 106-109 (« Durées ») ; l. 111-112 → 117-119 (point 2) ; l. 119-122 → 125-131 (coût de la voie) ; l. 142 → 151 (écart C3) ; après l. 279 → 288-291 (« Plan d'analyse », tâches planifiées avant la création) ; l. 342 → 355 (critères, « Validation arrêtée ») ; l. 365-367 → 369-372 (arrêt avant la création) | La « procédure de la session » devient « deux tâches planifiées de la session » partout ; la destruction à l'heure du plafond dite plafond en heures ; perte de toute la validation dite aussi à « Choix de conception » et aux critères ; une tâche absente du listing ou le nœud sans décision ajoutés aux arrêts avant la création ; étape « Tâches planifiées avant la création » ajoutée au plan |
| I1 (fusion) | l. 465-467 → 524-555 | Points 7 à 16 ajoutés à « Fusion » : HC-2 (7 de la résolution) ; critères (« Validation arrêtée », « Aucun nœud », « lue sans nœud ») ; devis (« Pire », seuils sur la somme, prix réel, vie hors amorce) ; statut (comptes détaillés, « 87 » attribué) ; documents qui font foi enrichis ; seuil (« et sortie laissée », 272 accepté) ; prédictions (« 87 autres », « frontière gelée elle-même ») ; amorce vérifiée ; écart C3 ; corrections après la contre-lecture. Liste déclarée **complète** au regard des 17 différences de la section 5 de la contre-lecture (points 4 à 8, 10, 11, 16, 17 ajoutés), configuration identique à l'octet ; concordance de conv-audit sur cette liste |
| I2 (devis) | l. 393-401 → 433-446 | « Central » : composantes détaillées (≈ 5,1 + 3,4 + 1,4 + 1 ≈ 10,8 h, arrondi à ≈ 10 h). « Haut » réécrit **à la borne haute de ses hypothèses** : 22,5 h + 4,7 h + ≈ 1,4 h + ≈ 1 h ≈ 30 h (29,6 h), ≈ 42 USD au prix plafond (≈ 35 à 1,187 USD/h) ; au prix plafond, au-delà du plafond du GO (destruction à 39,5 USD ≈ 28,2 h) ; à 1,187 USD/h, sous le point de destruction (≈ 33,3 h). « Pire » : borné par la tâche de destruction à l'heure du plafond. Paragraphe « Conséquence du cas haut » : alerte à 30 USD (≈ 21,4 h au prix plafond) **avec demande d'extension du GO** dès que la durée projetée dépasse l'heure de destruction ; offre nettement sous le plafond préférée à la création (le 2 novembre : 1,187 USD/h) ; `H` réduit des dépenses déjà imputées. Chiffres : contre-lecture, I2 et section 6.7 |
| I3 (accès à l'instance) | l. 369-371 → 400-407 ; « Fusion » l. 458-461 → 513-521 ; « Choix de conception » l. 119-122 → 125-131 | « La procédure de création ne prévoit aucun accès aux processus » remplacé par le **fait constaté** : aucune clé d'accès au conteneur posée par les sessions, aucun accès éprouvé. La voie du brouillon 2 (« `TERM` au processus Python, lu par lignée depuis l'amorce, `ps --ppid`, jamais par motif, R10, puis destruction par identifiant », avec ce que `sur_term`, script l. 234-240, sauverait) dite possible seulement après un accès établi et éprouvé sur le cas sain (R5), hors de ce texte ; destruction par identifiant = voie première, conséquence (perte de ce qui n'est pas poussé) dite |
| m1 (date) | l. 9 → 9-10 | `2026-11-02 23:20` (`date -u`) ; la version relue datée du 2 novembre 19:44 UTC rappelée |
| m2 (tests) | l. 48-50 → 50-56 | Les 71 sont ceux des sept fichiers de la liste `CIBLES` (script l. 314-315), tokeniseur présent ; « 71 passed » sans test sauté exigé (l. 323) ; le cœur seul sans tokeniseur en saute 10 (12 passés, 10 sautés, contre-lecture 6.10, `contre-lecture-complement-pytest-graine-sortie.txt`, `65e2068b…`) : un essai partiel n'est pas un écart |
| m3 (lignes du lot) | l. 221, 224 → 230, 233 | `combinaisons_max_lot` : « entier ≥ 0 (module du lot, l. 839-841) ; même frontière que le cœur (l. 708, 714, 749) » ; `duree_max_episode_lot_s` : « (module du lot, l. 845-846 ; script, l. 168-171) ». Vérifié par le rédacteur sur `resolution_graine_lot_v1.py` (`5a9982b2…`) : l. 839-841 garde « entier positif ou nul » de `combinaisons_max_lot` ; l. 845-846 garde `0 < duree_max_episode_lot_s ≤ duree_max_lot_s` ; l. 708 `quasi_egalites(…, seuil_ecart, quasi_egalites_max)` ; l. 714 `range(1, bascules_max + 1)` ; l. 749 quasi-égalités du rejeu basculé après sa dernière bascule |
| m4 (poids) | l. 128-130 → 137-140 | « ≈ 35 min de carte, poids en cache ; davantage sinon : le téléchargement des poids, ≈ 16 Go, précède l'étape validation, script l. 332-348 » |
| m5 (disque) | l. 360-361 → 377-378 | Prix du disque relevé à la création, écrit avec le prix horaire dans la ligne de `registres/depenses.md` ; repris à « Plan d'analyse » (l. 288-291) |
| m6 (section « Contre-lecture ») | l. 469-474 → 557-586 | Sous-liste ajoutée avant le marqueur, laissé en place pour session-depot : version relue (`3b7955f1…`, empreinte entière, commit `2764e6cc`) ; contre-lecture (chemin, `2ef1f192…` entière, lecteur, heures, verdict) ; corrections apportées B1, I1, I2, I3, m1 à m6, une ligne chacune ; renvoi à cette note et au patch |

## Réserves du rédacteur

1. **P-C7** (l. 193 de la version corrigée, inchangée) prédit l'étape 0 « entre ≈ 2 h et ≈ 24 h, point central ≈ 9 h ».
   Le cas « Haut » réécrit à la borne haute donne, pour l'étape 0 seule, ≈ 22,5 + 4,7 h plus les 54 et les 90 (≈ 35 min),
   soit ≈ 28 h, au-delà du « ≈ 24 h » de P-C7. La contre-lecture ne le relève pas et la correction d'une prédiction n'est
   pas dans les points à traiter : laissée telle quelle, signalée à session-depot (une prédiction, non un seuil ; rien
   n'en dépend pour le lancement).
2. La **confiance ≈ 0,8** de la recommandation du nœud est une estimation du rédacteur (format du programme :
   « recommandation et confiance »), non un chiffre de fait ; session-depot peut la reprendre.
3. L'inconvénient de l'option (a) du nœud (arrêt de l'instance par le fournisseur si le crédit s'épuise) est écrit comme
   un comportement **non éprouvé par les sessions** ; il reste à vérifier avant de s'y fier.
4. La « borne de compte » (recharge automatique suspendue) suppose que le compte Vast fonctionne par crédit prépayé avec
   recharge automatique, comme le dit la consigne reçue ; non vérifié par le rédacteur (aucun réseau).

## Complément de session-depot (après le rendu du rédacteur)

- Réserve 1 du rédacteur (P-C7, l. 193) : borne haute de la prédiction descriptive de durée alignée sur le cas « Haut » réécrit (≈ 24 h → ≈ 28 h pour l'étape 0 seule, hors vie de l'instance) ; point central inchangé. Prédiction descriptive, aucun seuil.
