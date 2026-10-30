# Contre-lecture 4 (R2) — préenregistrement de la recombinaison bisociative à deux espaces, v2, brouillon 4 — v1

- Contre-lecteur : sous-agent neuf, Sonnet 5.5 (`claude-sonnet-5-5`). **Non-auteur** du brouillon 4 (ni des brouillons 1 à 3, du script de puissance, des contre-lectures 1 à 3). **Réserve de forme** : c'est le même modèle que l'auteur du brouillon 4 ; le brouillon demandait « de préférence un autre modèle ». L'instance est neuve et n'a rien écrit de la pièce, donc R2 est tenue à la lettre, mais l'indépendance de modèle ne l'est pas ; à consigner.
- Date et heure UTC (`date -u`) : 2026-10-30T02:24:05Z.
- Fichiers lus en entier, empreintes recalculées et égales aux compagnons `.sha256` : brouillon 4 `7e4557b14c3a6e662c28c8a77e4582a752f17164361baa55a3f0632cb6522a61` ; script de puissance v2 `15cc3afaed3ff9099f12456be777376ad4c715a7d411d0deb1789eb7a586d778` (lu aux lignes 1 à 200 et par recherche ailleurs, non en entier) ; sa sortie `55f898f2d5e41b3df4f20d2681e142faba3bba1a04855e5fe83ed0bb9387f01b` (lue des paragraphes 6 à 24) ; contre-lecture 3 `4a15c3f95d0e05575e84c4083bc20bc11c936fdd74c5fa94655ed4e72298f82e`. Le brouillon 3 n'a pas été relu (contexte seul, non nécessaire).
- Non lus (interdits) : tout chemin contenant `donnees/`. Aucun réseau, aucune dépense, aucun fichier existant modifié, rien scellé.
- **Réexécution du script** : `python3 -I`, sans écriture de bytecode, sortie dans le dossier de travail temporaire de la session, **6,4 secondes** (exécution complète, pas de version réduite). Résultat : `cmp` sans écart avec `calcul-puissance-bisociation-v2-brouillon4-v2-sortie.txt` ; même empreinte `55f898f2…`. Aucun dossier `__pycache__` créé.

## (a) CB3-01 à CB3-09, point par point

| Point | État | Où dans le brouillon 4 |
|---|---|---|
| CB3-01 (adoption avec un terme de concept sous δ_non) | **traité** | S3 forme F-A (l. 207 à 213) : A7 ≡ D0, donc A7 vrai impose une estimation ≥ 2,5 > 1,5 et N0 faux. Ligne 9 de la Table 1 (l. 645) avec « ou N0 » ; note de lecture (l. 664). Forme F-B gardée comme option de Lazar, avec sa contradiction dite (l. 210). Script § 7 bis : exclusion vérifiée (A7 nouvelle = 0,00 là où N0 est possible). |
| CB3-02 (recalage sur une seule donnée) | **traité**, une réserve résiduelle (N1 ci-dessous) | Fourchettes −3 à +9 « moyen », +2 à +14 « bien », source dite (l. 124, 131). Confiances recalées sur les probabilités du script § 19 (l. 159 : arrondis au 0,05 inférieur, vérifiés : 0,87→0,85 ; 0,82→0,80 ; 0,58→0,55 ; 0,74→0,70). Réfutation de grandeur sans effet sur le verdict (l. 157). Verdict attendu si le transfert échoue (l. 168). « Presque acquise » dit (l. 167). Ce que l'adoption autorise (l. 106, 596, 647). Probabilités 0,78 / 0,75 et 0,63 / 0,60 (script § 16). |
| CB3-03 (b_eloigne hors des conditions) | **traité**, nœud laissé à Lazar | S17 (l. 310 à 318), clause de A2 (l. 606), ligne 9 bis (l. 646), contraste 20 décisif (l. 577), C12 (l. 582), essais de garde (l. 714), coût calculé au script § 22 (adoption inchangée au centième). |
| CB3-04 (S16c non simulé) | **traité** | S16c gardé avec son sens dit (l. 296, 459) ; condition M_fonds_1ou2, code 16 (l. 556, 572), 600 mondes (S15), contraste 39 (l. 577), garde de loi (l. 687, 714), puissance du contraste au script § 24. |
| CB3-05 (φ = 4) | **traité** | Asymétrie selon L_r dite (l. 308). |
| CB3-06 (J) | **traité** | (i) prédiction PJ +9,2 / +6,1 au centre, bas de fourchette +5 / +3 dans le script (l. 155, 276 ; script § 11) ; (ii) portée dite (l. 115, 276) ; (iii) essai R5 sur 300 miroirs de `M_inertes`, V9 (l. 567, 712 ; script § 21, chiffres recalculés à la main : 0,925 à un effet parasite de +3). |
| CB3-07 (S9, préfixe des indices) | **traité** | Seuil 15,3 (l. 243 à 247) ; manifeste scellé avant le premier monde, une seule invocation, ordre vérifié par le lecteur de la porte (l. 246, 591, 683) ; formule n' = ⌈n (σ̂ / 15,3)²⌉ vérifiée (2 625 ; 4 101). |
| CB3-08 (A3 dans la ligne 5) | **traité** | A3 absent de la ligne 5 (l. 641), déclencheur d'audit seulement (l. 610, 625, 689), coût 0,030 (script § 23). |
| CB3-09 (mécanique) | **traité** | Contraste 10 : code 1, rangé en descriptif (l. 575, 577) ; P15 déclencheur d'audit (l. 627, 689) ; libellés « Table 1 ligne 10 », « Table 2 ligne 7 » et facteur 0,995² partout dans le script (l. 15 à 18, 173, 276, 363, 514) ; ligne de gel : loi de q et mots de surface ajoutés (l. 792). |

## (b) Ajouts du brouillon 4

**Ce qui tient.**
- *Règle A7 (forme F-A).* Pas de circularité nouvelle : A7 ≡ P4 ≡ D0, dit à l'avance. La coexistence de la ligne 10 de la Table 1 et de la ligne 5 de la Table 2 est logiquement exclue ; la ligne 6 de la Table 2 peut coexister, et c'est dit (l. 664).
- *Adoption par puissance.* Les probabilités sont des calculs sur des effets supposés, sans lecture d'aucun résultat de la version 2 : aucun monde n'a été simulé. Aucun seuil n'a été choisi après un résultat de la version 2. Les valeurs de v1 viennent d'un jeu de résultats déjà produit et antérieur ; S9 passe de 18 à 15,3 sur la recommandation de la contre-lecture 3, et S3 sur celle du même rapport.
- *Choix ouverts S3 et S17.* Chacun a deux options avec avantage et inconvénient, une recommandation et un niveau de confiance ; chaque option est complète (lignes de table, essais de garde). Rien ne dépend d'un défaut de 48 heures (l. 192).
- *Ligne de gel.* Le texte contient 28 marqueurs « À REMPLIR » (comptés) : S1 à S12 (12), V1 à V6 (6), S14, S15 (2), S16a à S16f (6), S17 (1), Contre-lecture 4 (1). La ligne de gel (l. 792) les couvre tous, valeur par valeur, et recopie les recommandations du texte (contrôlé sur S1 à S17). Elle déclare que le scellement attend ce rapport.
- *Aucune lecture avant scellement.* Exigé à l'en-tête (l. 16, 21), à la fin des critères (l. 668), dans la liste d'arrêt (l. 692) ; le code s'écrit après scellement (l. 21) ; l'ordre est « gel, scellement, code, gardes, validation, une invocation » (l. 591) ; le fichier de validation reste fermé jusqu'au verdict. Le brouillon ne lit aucune donnée de la version 2 (aucune n'existe) et rien sous `donnees/`.
- *Prédictions avec signe et chiffre.* P1 à P6, P9 à P11, P14 à P16 et PJ ont un signe, une fourchette et une réfutation. Listes d'arrêt : complète pour les ajouts (ordre du manifeste, loi de M_fonds_1ou2, J sur miroirs, clause de b_eloigne).

**Remarques (aucune ne bloque le gel ; N1 à N4 sont à corriger avant scellement, N5 à N7 sont facultatives).**

**N1 — Incertitude de P4 laissée hors de la « fourchette honnête » (moyenne).**
- Lieu : résumé points 4 et 5 ; nœud ouvert 5 (l. 83) ; l. 139 à 142 et 159.
- Défaut : l'ancrage sur une seule donnée de v1 ne couvre que l'avance de N_β0 sur b. La fourchette de P4 (+3 à +8, centre +5,5) n'a **aucune donnée** (v1 n'avait pas de canal de concepts) ; c'est une opinion de l'auteur. Or, sous F-A, l'adoption s'effondre juste sous le bas de cette fourchette : 0,88 / 0,82 à P4 = 3 ; 0,23 à 2,5 ; 0,00 à 1,5 (script § 17). Trois formulations deviennent donc trop fortes :
  - « fourchette honnête » (point 4 du résumé) : elle ne l'est que conditionnellement à P4 ≥ 3 ;
  - « la probabilité d'adoption dépend presque uniquement de l'avance de l'éloignement seul » (l. 83) : c'est faux sous F-A, la sensibilité à P4 est du même ordre (script § 17) ;
  - la confiance 0,90 sur P4 (l. 142), « plafonnée faute d'une deuxième donnée » : il n'y en a pas même une première.
- Correction : une phrase dans le résumé et dans la réserve 5, disant que 0,78 / 0,75 suppose P4 entre 3 et 8 sans source et que l'adoption est quasi nulle sous 2,5 ; abaisser la confiance de P4 ou la marquer « sans donnée ». Ni chiffre ni seuil à changer.

**N2 — Racines de graines non fixées (faible à moyenne).**
- Lieu : § 7 (l. 571) et audit (l. 630).
- Défaut : `RACINE` et `RACINE_VALIDATION` ne reçoivent aucune valeur ni règle de choix. Si la racine de décision est choisie après la validation (ou après un premier coup d'œil), elle ouvre un degré de liberté dans un préenregistrement qui interdit tout réglage (R1, R9).
- Correction : fixer les deux valeurs au scellement, ou écrire la règle de dérivation et exiger qu'elles figurent au manifeste scellé avant la validation du générateur.

**N3 — Deux critères de lecture qui exigent une interprétation (faible).**
- Lieu : l. 630 (« artefact trouvé » / « aucun artefact »), l. 565 (V7 : « monde mal réglé »).
- Défaut : l'issue de l'audit décide de lignes entières des deux tables (lignes 1 et 2), mais aucun critère opérationnel ne dit ce qu'est un artefact trouvé ; V7 « sans seuil » peut tout de même déclencher une version nouvelle sur un jugement. Le lecteur de la porte (R13) devrait interpréter.
- Correction : une phrase par audit (« artefact trouvé » = lecture d'un champ latent constatée par balayage ou permutation donnant un gain ≥ …), ou déclarer ces deux jugements comme confiés au sous-agent d'audit avec rapport scellé. Même défaut qu'aux brouillons précédents, mais l'audit de J sur miroirs et celui de P15 sont des ajouts du brouillon 4 qui y renvoient.

**N4 — Libellé « avant toute méthode » contredit par V9 (faible).**
- Lieu : l. 558, 567, 674, 712.
- Défaut : V9 calcule d1c et c (des témoins) pendant la validation du générateur, que la liste d'arrêt place « avant toute méthode ». Et le texte ne dit pas si un audit déclenché par V9 (probabilité 0,02) doit être rendu **avant** l'invocation unique des mondes de décision ou seulement avant le verdict (la ligne 1 de la table renvoie au verdict).
- Correction : écrire « avant les bras candidats et leurs ablations » et « audit de V9 rendu avant l'invocation ».

**N5 — P7 (première partie) et P12 sans grandeur (faible, facultative).**
- Lieu : l. 145, 150.
- Défaut : « > 0 » pour N − N_PCg et « pente > 0 » n'ont pas de chiffre. P12 est descriptive ; P7 est une condition de la ligne gain_contrôle, donc lue.
- Correction : une fourchette pour P7, ou « sans grandeur prédite, signe seul ».

**N6 — Seuils qui épousent les centres de l'auteur (note, non bloquante).**
- Lieu : S3 raison, S5 raison, l. 226.
- Constat : δ = 2,5 et la forme F-A sont justifiés par leur puissance aux centres P4 = 5,5 et P5 = 3, qui sont des opinions de l'auteur. Ce n'est pas un réglage après résultat (aucun résultat de la version 2 n'existe), et le brouillon le dit (« presque acquise », l. 167). Pour R3 (aucun run visant un signe positif), le garde-fou est ce que l'adoption autorise (descriptif seulement) et la lecture « sous W1 à W4 ». Suffisant.

**N7 — Mécanique du contre-lecteur 4 (note).**
- Au scellement, l'entrée « Contre-lecture 4 » du brouillon (l. 786) doit recevoir l'empreinte du brouillon relu (`7e4557b1…`, ci-dessus) et celle de ce rapport, plus le traitement de chaque remarque ; le validateur du dépôt n'exige que les deux empreintes de 64 caractères. Les réserves propres au brouillon 4 (l. 784) sont à reporter dans le traitement de chaque remarque.

## (c) Calcul de puissance

- **Reproductibilité.** Sortie identique au bit près (compare `cmp`, empreinte `55f898f2…`). Exécution complète en 6,4 secondes ; aucune version réduite nécessaire.
- **Graines.** Le script n'emploie **aucun** générateur aléatoire (recherche de « random » et de « SeedSequence » : zéro occurrence). Les « intégrales sur fourchette » sont des sommes sur une grille de milieux. R9 ne s'applique donc pas au script ; il s'applique au code d'expérience, décrit au § 7 du brouillon (voir N2 pour les racines). Le brouillon le dit exactement (l. 16, 324).
- **Cohérence des chiffres annoncés avec la sortie réexécutée.**
  - Adoption **0,94 / 0,92** au centre de v1 : § 13, ligne 6,6 (forme b4) ; § 16, dernière ligne. ✓
  - Adoption **0,78 / 0,75** sur −3 à +9 : § 16 (trois décimales 0,783 / 0,747) ; identique « bien » fixé, comonotone ou indépendant. ✓
  - Adoption **0,63 / 0,60** sur −6 à +9 : § 16 (0,627 / 0,598). ✓
  - Variante P4 uniforme 3 à 8 : 0,78 / 0,74 (§ 16, § 19). ✓
  - Forme du brouillon 3 reproduite : 0,760 / 0,725 et 0,61 / 0,58 (contre-lecture 3 : 0,76 / 0,73 et 0,61 / 0,58). ✓
  - Ligne 4 de la Table 1 sur la fourchette : 0,13 (§ 18) = 1,5 / 12. ✓ « Autres dont indécis » : 0,09 / 0,13. ✓
  - Confiance « N adoptée 0,70 » : 0,78 / 0,74 arrondi au 0,05 inférieur. ✓
  - Totaux de mondes : 11 400 + 4 800 = 16 200 ; 23 400 avec extension (§ 15). ✓ S9 : 2 625 ; 3 322 ; 4 101 ; plafond à 21,64 (§ 14). ✓
- **Logique.** Je n'ai pas trouvé d'erreur de logique qui change un chiffre annoncé. Points vérifiés : A2 contre a (`nb + 4,8`), contre d1c (`nb − 4`), A7 b4 et b3, retrait de A3 (le gain de 0,02 à 0,03 est exactement 1 / 0,97), facteur 0,995², seuil de J à 5 / 3. Quatre réserves de méthode, toutes déjà déclarées par le brouillon (l. 326, 784 réserve 7) : indépendance des facteurs d'une conjonction ; écart-type de Δ(N, N_β0) inconnu ; comonotonie entre « bien » et « moyen » ; les valeurs fixées de A4, A5, A6 (−12 ; 0 ; −3,5) ne sont pas intégrées sur leur fourchette. La seule faiblesse de lecture est celle de N1 (P4 non intégré dans le chiffre de tête).

## Verdict

**Soumettable avec corrections mineures** (aucune simulation nouvelle, aucun seuil à changer) : N1 (porter l'incertitude de P4 et corriger « presque uniquement » dans la réserve 5), N2 (fixer les racines de graines), N3 (critère opérationnel de l'audit et de V7), N4 (ordre de V9) ; N5 à N7 facultatives ou mécaniques. Les neuf points de la contre-lecture 3 sont traités, la sortie du script est reproduite au bit près, et la ligne de gel couvre les 28 marqueurs ; Lazar peut geler après les corrections N1 à N4 sans nouvelle contre-lecture complète.
