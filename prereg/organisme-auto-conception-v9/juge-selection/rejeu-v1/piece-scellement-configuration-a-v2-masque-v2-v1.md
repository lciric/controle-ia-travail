# Pièce de scellement — configuration A v2 et masque v2 du rejeu du juge de sélection (organisme v9) — v1

Écrite par la mère (`session_01QPDgKgejkqwnuaJHJ31Ydo`) le 20 novembre 2026, sur GO-2026-11-20-36 (1), selon la contre-lecture de la configuration A v2 (§ 3.1), qui fixe mot pour mot les textes T1 à T9. La pièce v1 (`piece-scellement-manifeste-rejeu-v1.md`, `9e46ac3be599992678670e6728a057c1670bdd23de628ba94d286dbacaa6e2ad`), la configuration A v1 (`configuration-a-masque-v1.json`, `8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4`) et le masque v1 restent scellés et inchangés (R12).

## Pièces scellées

Dossier de la chaîne, recopié à l'octet de `lot/compte-organisme-v1` (commit `f6c05537`) : `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/rejeu-masque-lecteur-v1/configuration-a-v2/`.

| pièce | chemin | sha256 |
|---|---|---|
| configuration A v2 | `prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/configuration-a-masque-v2.json` (copie du dossier de la chaîne) | `a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54` |
| masque v2 | `…/configuration-a-v2/masque-v2/masque_style_cartes_v2.py` | `769aace5b64c697799b76a0120a5c2926c75798a388c93fa00ddc93224401c01` |
| essais du masque v2 | `…/configuration-a-v2/masque-v2/essais_masque_style_cartes_v2.py` | `7c84260f3fabe5ebcf7a9ea8447cf94dd462710755055026a44194282be14b71` |
| proposition de la configuration A v2 | `…/configuration-a-v2/proposition-configuration-a-v2-v1.md` | `2f6ef529445bae369fa17312ab16285ac0e9df5bcf12b27a9f57c6a24333fa36` |
| contre-lecture du masque v2 (Sonnet), « Conforme » | `…/configuration-a-v2/masque-v2/contre-lecture-masque-v2-v1.md` | voir son compagnon |
| contre-lecture de la configuration A v2 (Opus neuf), « Conforme », 32 contrôles sur 32 | `…/configuration-a-v2/contre-lecture-v1/contre-lecture-configuration-a-v2-v1.md` | `29be16ad65f36c2194dc028378b8f88b5450d7f57d8f0a9bfd2763c1ca1166a5` |

## Textes exacts (contre-lecture, § 3.1)

**T1.** « Écarts aux critères v7 accordés par Lazar. GO-2026-11-20-36 (1) tranche le nœud de la proposition de la configuration A v2 (`2f6ef529…`) par l'option (a) : la réserve « sous réserve du nœud » est levée. Il en résulte trois écarts aux critères v7 scellés, accordés : (i) le masque joué est `masque_style_cartes_v2.py` (`769aace5…`), non `masque_style_cartes_v1.py` (en-tête, l. 3 et l. 11) ; (ii) la liste des clés retirées de la configuration A v2 est tirée, sous GO-2026-11-20-28, d'un programme qui a lu les seuls noms de clés de `contenu`, et non de la seule consigne (§ 1, l. 41) ; l'ordre et la liste des dix champs restent ceux de la consigne ; (iii) la troisième ligne de l'en-tête des cartes masquées nomme les trois clés retirées et leurs nombres. Le masque v1 a été joué une fois sous GO-2026-11-20-24 et a refusé sans rien écrire (compte rendu `e13da23c…`) ; le jeu suivant est le second sous GO-2026-11-20-24, relancé par GO-2026-11-20-36 (1). »

**T2.** « La configuration A v2 est la v1 plus la seule clé `cles_hors_champs_retirees` = `{"_": 2, "cout_note": 1, "epreuve_hors_ligne": 1}`, égale au résultat des noms de clés (`86aecdee…`) ; les sept autres clés sont égales à la v1, vérifié par programme. `hors_choix` est vide : les nombres attendus portent sur les 94 cartes. La configuration B (`b44371d2…`) et le manifeste (`a81d30d3…`) ne changent pas : les trois champs de B sont parmi les dix ; le manifeste ne cite ni la configuration A ni le masque. »

**T3.** « « Masquée » se lit ici, comme dans GO-2026-11-20-36 (1) : retirée de la forme masquée seule, que lisent les deux lecteurs et le lecteur par programme en forme « masque ». La carte non masquée, que lit le lecteur par programme en forme « fiches », reste telle qu'elle est (critères v7, § 1, l. 46). »

**T4.** « Le lecteur par programme, en forme « fiches », lit encore les trois clés quand leur valeur est un texte (`de99117b…`, l. 168 et 175). Sur les cartes qui les portent, et sur elles seules, le « oui » du critère D peut donc tenir à une clé que la forme masquée n'a plus, et une baisse de D sous le masque peut venir de ce retrait plutôt que de la coupe. Le « non », la voie et le compte « devenu indécidable » n'en dépendent pas. »

**T5.** « De deux à quatre cartes perdent, sous le masque, une clé hors des dix champs, qu'aucun des deux lecteurs ne lira et dont personne ne connaît le contenu. Retirer une clé peut desservir la carte qui la porte ; la montrer aurait pu la servir ou la signaler (règle R4). »

**T6.** « Le masque v2 peut encore refuser sur les cartes : si l'un des dix champs manque à une carte ou n'est pas un texte (l. 131-134), ou si une autre clé hors des champs s'y trouve. Le résultat des noms de clés ne dit rien des deux premiers cas. Un refus arrête le jeu : rien n'est relancé, la mère décide. »

**T7.** « Sans la clé neuve, le masque v2 rend la sortie du v1, aux deux seules valeurs près qui diffèrent par nature : le nom de la pièce et l'empreinte du programme. C'est la lecture de « à l'octet » que vérifient les essais (55 réussis, rejoués par la contre-lecture du masque v2). »

**T8.** « La troisième ligne de `en_tete` nomme les trois clés, leurs nombres et l'empreinte de la configuration. Elle ne désigne aucune carte. Les deux lecteurs la liront avec les deux premières : c'est ce que l'option (a) prévoit, et ce que les critères demandent de dire d'avance (§ 1, l. 42). Le lecteur par programme ne lit pas `en_tete`. »

**T9.** « Un refus de compte n'écrit à l'écran que le nom d'une clé, le nombre trouvé et le nombre attendu, sans identifiant ni valeur. C'est la sorte d'information que rend GO-2026-11-20-28 : il se recopie au compte rendu. »

## Suite
Les textes P1 à P3 (contre-lecture, § 3.2) seront portés à la proposition du rejeu ; le mandat neuf de l'exécutant du second jeu sous GO-2026-11-20-24 suit les douze changements du § 4 de la contre-lecture et passe par la mère avant tout lancement.
