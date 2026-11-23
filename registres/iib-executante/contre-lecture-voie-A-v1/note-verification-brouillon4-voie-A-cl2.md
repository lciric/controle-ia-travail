# Vérification du brouillon 4 de l'additif et du devis de la voie (A) — cl2

Date : 2026-11-22. Classe A. Contre-lecteur : Claude Opus 5.5, le même rôle que pour le brouillon 3. Je n'ai écrit aucune pièce. Rien dépensé. Aucun loueur, aucun modèle externe. Rien poussé. Aucune pièce interdite ouverte. Aucune variable d'environnement affichée.

## Verdict

**Scellable après corrections.**

Le brouillon 4 porte exactement les quatre majeurs et les trois mineurs de cl2, et les errata 1 et 2 du mandat. Les deux rejeux sont identiques à l'octet. Aucune régression. Les trois champs restants sont bien les seuls attendus.

Mais le deuxième rempart, neuf, a deux défauts :
- son seuil (échéance plus 10 minutes) tombe dans la fenêtre normale de la minuterie (M1) ;
- son code 6 détruit sans rapatriement vérifié, contre la règle de Lazar sur ce qui est récupérable (M2).

Aucun des deux ne fait passer le plafond. Après ces deux corrections et un mineur, puis le remplissage des trois champs, l'additif est scellable.

## Pièces

Branche `origin/claude/iib-executante-v5-fable-additif-c`, commit `6d88fbf50ca305a0e8ad93b59171fd5e10da0de5`. Toutes les empreintes sont conformes à leurs compagnons.

| pièce | empreinte |
|---|---|
| additif, brouillon 4 | `12196e82731d8f60…` |
| devis, brouillon 4 | `02730ddd46c95366…` |
| différences entre les brouillons 3 et 4 | `32ec2aef660e8a94…` |
| programme de calcul v4 | `053d793b…` |
| sortie du calcul v4 | `df2a357d…` |
| vérification des gardes v4 | `7e0d1a5e…` |
| sortie de la vérification v4 | `de0426fb…` |

Les pièces citées en tête sont toutes vérifiées par empreinte : mandat `c5c2d5de…`, errata 1 `4642543b…` et 2 `a2593319…`, note cl2 `b96d839e…`, correctifs 0023 à 0025, contre-lectures et vérifications des correctifs 0022 et 0023, configuration sans entropie `4a7c6118…`, programme qui l'écrit `9d085bbe…`, épreuve de l'entropie `2e450a6a…`.

Au code final `f7a5123e…` (arbre `717f0b20…`), les empreintes des amorces et des listes sont exactes : `4140d3b3…`, `03962c29…`, `81e2f75a…` (26 lignes) et `035c9427…`.

## A. Points de cl2 et des errata : portés

| point | où le brouillon 4 le porte | état |
|---|---|---|
| M1, correctif 0024 | § 2, ligne 0024 (commit `9780b7e3…`, arbre `475631a8…`) ; exigence 1 et ligne du code : « 0021 à 0025 » ; devis, § 7, point 7 ; vérification v4 citée en tête, en A1, en A3 et au devis, § 4 | porté. Par l'erratum 2, la vérification est rejouée à `f7a5123e` et non à `9780b7e3` |
| M2, exécutante | § 4.2 : `session_013QMaym1QE4UyYr1H8KU8Rf`, `GO-2026-11-22-94`. Échéance de la ligne de session : § 7, point 10, et A3 | porté. Branche écrite `claude/iib-executante-v6` (cl2 disait v5) : c'est la branche réelle des registres de l'exécutante, et c'est juste |
| M3, `GO-2026-11-22-93` | en tête de l'additif, en A1 et dans « Accord cité » du devis : la phrase de cl2, mot pour mot | porté |
| M4, second rempart | la phrase « tient le total sous 60 USD » est retirée de A3 et du devis, § 4. À sa place : trois remparts chiffrés par [M29], la surveillance non comptée comme rempart, et une réserve au § 7, point 8, de l'additif comme du devis | porté, sous la forme de l'erratum 1 (voir M1 et M2 ci-dessous) |
| m1, crédit | devis, § 0 : 12,995 USD comme valeur d'origine ; 39,81 USD relus ; [M31] couvre 21,32 USD | porté |
| m2, écriture du compte | A3, § 4.3, point 3, et § 4.4, point 2 ; le programme v4 imprime le compte à trois décimales ([M24] : « 5.52 (compte 5.515, arrondi au centime supérieur) ») | porté |
| m3, en-tête | « et la différence du correctif 0024 » ; ce qui est lu à l'arbre de la voie est nommé | porté |
| erratum 1, point 1 | deuxième rempart écrit et éprouvé par programme (`second-rempart`, sept cas [M30]) ; l'écart au mot de la mère est déclaré | porté (voir C) |
| erratum 1, point 2 | pire si la minuterie joue seule : 56,61 USD [M29](a), calculé par programme, sous 60 | porté |
| erratum 1, point 3 | troisième rempart, la mère, écrit et non compté | porté |
| erratum 2, points 1 à 4 | code `f7a5123e`, arbre `717f0b20` ; vitesse du premier lot : diagnostic, `null`, « non_mesuree » (A4) ; empreintes ; 311 et 313 | porté. Les champs du commit et de l'arbre sont remplis, car la vérification du 0025 est rendue : `note-verification-0022-cl1.md`, `5c0ec3c3…`, « Verdict : autorisable », au commit `f7a5123e` |

**Aucune régression.** Les phrases retirées du brouillon 3 sont toutes nommées par la note des différences. La configuration sans entropie, comparée clé par clé à la configuration scellée de l'étalonnage (`08e22099…`, lue à `f7a5123e`), diffère en six valeurs dans cinq clés, et en aucune autre : `code.branche`, `code.commit`, `entropie` (nulle), `go_id`, `instances_intouchables`, `offre.etiquette`.

## B. À corriger

### Bloquants

Aucun.

### Majeurs

**M1 — Le seuil du deuxième rempart tombe dans la fenêtre normale de la minuterie.**

Code lu à `f7a5123e`, dans les deux amorces. À l'échéance, la minuterie :
1. consigne, sous `timeout -k 10 2400`, soit 40 minutes au plus ;
2. puis tente la destruction pendant une marge de 1 800 secondes.

Dans son fonctionnement normal, une machine peut donc encore tourner jusqu'à l'échéance plus 70 minutes. [M29](a) le compte d'ailleurs ainsi (2 400 + 1 800 secondes).

Or la règle `second-rempart` rend le code 4 dès l'échéance plus 600 secondes pour toute machine qui tourne. Rejoué : à l'échéance plus 2 400 secondes, état « tourne », code 4. Le texte en tire « la minuterie a fait défaut » (A3, et [M30], cas 2). C'est faux à cet instant.

Effets :
- l'arrêt coupe la consignation en cours ;
- il tue la minuterie, qui ne détruira plus ;
- une machine qui allait se détruire seule dépend alors de la session, pendant deux heures puis jusqu'au geste de destruction.

Cela affaiblit le premier rempart au lieu de le doubler. La dépense reste tenue : 55,62 USD.

Correction, au choix de la mère, puisque son mot dit « plus 10 minutes » :
- **(i), recommandée** : seuil à l'échéance plus 2 400 + 1 800 + 600 = 4 800 secondes (80 minutes). Pire du cas (b) : 55 + (4 800 + 600) s × 1,38 / 3 600 + 2 h × 0,08 = **57,23 USD**, sous 59,76. [M32] change alors : 30 h + 4 800 + 600 + 7 200 s = 33,50 h, donc création de la course au plus tard le **2026-11-24 à 14:30Z**, au lieu de 15:40Z. Le chiffre 8 400 du § 5 et de A3 devient 12 600.
- **(ii)** : garder « plus 10 minutes », mais écrire honnêtement que le code 4 peut couper une minuterie qui consigne encore, et que le disque est alors rapatrié par la session. Le rendre à la mère au § 7, point 9.

Dans les deux cas, retirer « la minuterie a fait défaut » du libellé du code 4 et du cas 2 de [M30], ou le réserver au seuil de (i).

**M2 — Le code 6 détruit « rapatriement vérifié ou non ».**

CLAUDE.md, mot de Lazar (R-3661) : « aucun orchestrateur ni programme ne supprime une sortie de course avant ce versement ; le versement, lui, ne se discute pas ».

Le code 6 détruit au bout de deux heures, avec `RAPATRIEMENT_VERIFIE=oui` posé au titre du « mot de la mère donné d'avance ». Le lanceur l'accepte : son message dit « rapatriement vérifié, ou mot de la mère sur les écarts ». Mais un mot de la mère ne lève pas une règle de Lazar.

Le plafond n'en a pas besoin. Si la machine reste à l'arrêt au lieu d'être détruite sans versement, la même hypothèse de 48 heures donne 55 + 0,46 + 3,84 = **59,30 USD**, sous 59,76.

Correction : au code 6, « rapatriement non vérifié à deux heures : machine gardée à l'arrêt, nœud ; destruction après rapatriement vérifié ou sur mot de Lazar ». Ajouter 59,30 à [M29](b) comme borne de ce chemin. Sinon, porter ce point à Lazar, et non à la seule mère : § 7, point 9, et devis, § 8.

### Mineurs

- **m1 — Instant incohérent non refusé.** `second-rempart E M arret A` avec A > M (arrêt dans le futur) rend le code 5 au lieu du code 2. Rejoué : `E, E+800, arret, E+900` donne le code 5. Ajouter `arret_s > maintenant_s` à la condition du code 2, et un huitième cas à [M30]. Le chemin « instant non entier » rend bien le code 2 (rejoué), mais aucun cas de [M30] ne le montre ; on peut l'y ajouter.
- **m2 — Suites de M1.** Si (i) est retenu, il faut changer dans un même geste : [M29](b), [M30] (seuil), [M32], A3 (« 2 heures 20 », « 8 400 secondes »), § 5, devis § 4 (tableau), § 6 et § 7, point 11, ainsi que la note des différences.

## C. L'écart déclaré au mot de la mère

Écrit dans le brouillon : à l'échéance plus 10 minutes, arrêt ; rapatriement de deux heures au plus ; puis destruction. L'écart est rendu au § 7, point 9, et au devis, § 8.

**Cohérent avec le code, oui :**
- la sous-commande `destruction` de `scripts/lancer_iib_v3.sh` à `f7a5123e` refuse tout état hors de `ETATS_ARRET="exited stopped"`, une liste fermée ;
- elle exige `RAPATRIEMENT_VERIFIE=oui`, la ligne `instance` de `lancement.txt` égale à l'identifiant, une liste des intouchables non vide, l'étiquette exacte, le module de lecture vérifié et un inventaire lisible ;
- l'arrêt d'abord est donc obligatoire ;
- les codes de sortie de la destruction (4, 6, 7) mènent au nœud prévu par le texte.

**Pas sans trou :** les deux défauts M1 et M2 ci-dessus. Les autres chemins sont fermés :
- état illisible : code 2 ;
- machine relancée après l'arrêt : code 4, puis nœud ;
- machine déjà à l'arrêt : chemin normal, et nœud à 24 heures ;
- machine absente : rien à faire, et un inventaire illisible n'est pas une absence.

## D. La réserve pour Lazar : 64,76 USD

Elle est exacte et bien placée.

Sous le correctif 0023, la surveillance arrête la machine au total compté T = min(60, 55 + compte), sans la détruire. T vaut 60 dès un compte de 5. On ajoute 0,92 de consignation et 3,84 de stockage (48 heures) : 64,76 USD. Pour un compte de 0, comme sur la machine de l'étalonnage : 59,76.

Le compte de 0,92 est prudent : un arrêt par la surveillance ne consigne pas.

Le texte dit aussi, à juste titre, deux choses :
- la surveillance et le deuxième rempart vivent dans la même session : si elle meurt, rien dans l'ordre ne borne la dépense ;
- les 48 heures ne sont tenues par aucun code (additif, § 7, point 8 ; devis, § 7, points 8 et 9, et § 8).

Rien à corriger ici. Si M1 (i) est retenu, la réserve ne change pas.

## E. Champs restants

Il n'en reste que trois dans l'additif, et aucun dans le devis :
- `<<ENTROPIE_VOIE_A>>` (deux occurrences) ;
- `<<EMPREINTE_CONFIG_VOIE_A>>` (deux occurrences) ;
- `<<COMMIT_LANCEMENT_ETALONNAGE_VOIE_A>>` (deux occurrences).

C'est conforme : seulement l'entropie, l'empreinte de la configuration et le commit de lancement. La mention « À REVOIR PAR FABLE » est absente. Il reste à relever l'empreinte du devis dans son compagnon au scellement (§ 6).

## F. Rejeux

| rejeu | résultat |
|---|---|
| `python3 -I calcul-devis-voie-A-v4.py`, avec le Python du système et avec celui de l'environnement virtuel | code 0 ; **identique à l'octet** (`df2a357d…`) |
| différence entre les sorties v3 et v4 | seules [M05], [M24] et [M25] changent d'écriture, et [M29] à [M32] s'ajoutent, comme annoncé |
| [M29] à la main | (a) 55 + 4 200 s × 1,38 / 3 600 = **56,61** ; (b) 55 + 1 200 s × 1,38 / 3 600 + 2 × 0,08 = 55,62 ; (c) 55 + 3,84 = 58,84 ; (d) 60 + 0,92 + 3,84 = **64,76**. Tout est exact |
| [M30] | les sept cas rejoués un par un par la sous-commande : codes 0, 4, 0, 0, 5, 6, 2, conformes à la sortie. Hors liste : « x » donne 2 ; arrêt dans le futur donne 5 (m1) ; tourne à E + 2 400 donne 4 (M1) |
| [M32] | 30 h + 600 + 600 + 7 200 s = 32,33 h ; 1795651200 − 116400 = 1795534800 = **2026-11-24T15:40:00Z** (`date -u`). La fin de session 1795651200 = 2026-11-26T00:00:00Z. Exact |
| `verifier-gardes-du-lanceur-v4.sh` à `f7a5123e`, sur `registres/go.md` de `main` à la tête `4e47b5d6…` (registre `7776d200…`), configuration de l'étalonnage `08e22099…` et configuration de la voie `4a7c6118…`, avec chacun des deux Python | code 0 ; **identique à l'octet** (`de0426fb…`) |
| différence entre les vérifications v3 et v4 | en-tête ; « 60.0 » devient « 60 » aux lignes 48, 50, 53, 55 et 78 ; § 2 ter (58.123456, exact) et § 6 ajoutés. Mêmes décisions |
| minuterie des deux amorces à `f7a5123e` | `timeout -k 10 2400` et `MINUTERIE_MARGE_S:-1800`, comme [S9] |

Les dossiers temporaires de cette vérification sont supprimés de mon bloc-notes. Il ne reste que cette note.
