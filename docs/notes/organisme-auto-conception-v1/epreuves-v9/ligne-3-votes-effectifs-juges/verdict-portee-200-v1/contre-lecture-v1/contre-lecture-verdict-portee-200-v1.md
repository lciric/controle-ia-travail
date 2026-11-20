# Contre-lecture du verdict de la mesure « portée à 200 » de la ligne 3 (votes effectifs des juges) — v1

Écrite le 2026-11-20 par le contre-lecteur neuf, d'un autre modèle que l'agent qui prononce : je n'ai écrit ni le texte de la ligne 3, ni un additif, ni le code, ni le verdict de l'étage 1 ou sa contre-lecture, ni le verdict que je lis. Mandat : `mandat-contre-lecteur-verdict-portee-200-v1.md` (`9eb4489f7ec7f9ac4dad426a159c5e7f66542380c0304bb249e59da1379bedda`), lu en entier. Pièce lue : `verdict-portee-200-ligne-3-v1.md` (`d27305c859d6c4ddcf6c2bd6a669a64f66c9cc69cb1d8b3f7e2f2a0fc39e0147`, égale à son compagnon).

## Verdict de la contre-lecture

**À corriger : une phrase de l'audit de symétrie (correction 1), qui ne touche ni un compte qui décide ni l'issue.** Tout le reste est conforme : mon recalcul indépendant rend la même faute du banc (aucune), la même puissance qui décide (0,3505, soit 701 répliques gagnées sur 2 000, contre l'unanimité, loi 1, ρ = 0), les mêmes minima par comparaison et la même **issue B**. Une fois la phrase remplacée : conforme, à sceller.

## 1. Empreintes vérifiées

Toutes recalculées par `sha256sum` et trouvées égales à celles que le verdict cite : additif 3 v3 scellé (`71b7a876…`), additif 5 v2 scellé (`581e97e5…`), texte v7 (`4e3680d9…`), verdict scellé de l'étage 1 (`1628b4d7…`), résultat de la mesure (`afcb453a…`), manifeste de la mesure (`da6a9300…`), manifeste du chronométrage (`9819b671…`), compte rendu de l'exécutant (`c0fd3ddc…`), contrôle du manifeste par la mère (`0dcd2dc7…`), banc v4 (`79865552…`, cité trois fois dans l'additif 5), mandat de l'agent qui prononce (`7a1d61fc…`, égal à son compagnon), et les huit pièces de la section 7 du verdict.

Le résultat et le manifeste de l'étage 1 sont absents du disque. Je les ai tirés de `origin/lot/compte-organisme-v1`, au chemin `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/execution-etage-1-v1/etage-1/`, par `git cat-file blob` redirigé vers mon bloc-notes. Empreintes : `eb7a673bc9612458f4c86cf817ef60e58c8118772934c52fbdba18cc4f3c60ce` et `6c64c32c1d0bf7257e5b00277051de26dcedffec6fb0193066164cda9053eb92`, égales à celles du verdict scellé de l'étage 1 (l. 21 et 22).

## 2. Rejeu des programmes du verdict

Les quatre programmes rejoués par `python3 -B`, par leur chemin, vers mon bloc-notes (Python 3.13.18). Les quatre sorties sont égales à l'octet à celles du verdict :

| sortie | sha256 du rejeu | égale |
|---|---|---|
| `sortie-faute-du-banc-portee-200-v1.json` | `29f6d93c96f5bebd7b19ee5a029809593245cd72d751f633acf8d9bea4db65d4` | oui |
| `sortie-comptes-portee-200-v1.json` | `31e0847cf52d9030a06e0c0eef4fb9007d37e4d58e8d1a00ced5a268cfc1370a` | oui |
| `sortie-audit-symetrie-portee-200-v1.json` | `c4f3d3db79026c655ca618139dca406c76513a03a8933e0c5303f08a94c265f5` | oui |
| `sortie-comparaison-aide-portee-200-v1.json` | `9eddc658830b4a1798f82696864606376984ab75d637cbc9adeebc7fc449c771` | oui |

## 3. Recalcul indépendant

Programme `recalcul_contre_lecture_verdict_portee_200_v1.py`, sortie `sortie-recalcul-contre-lecture-verdict-portee-200-v1.json`. Il ne reprend ni le code du banc ni celui de l'agent qui prononce. Formules écrites par moi d'après le texte v7 (l. 101 à 104, l. 205, l. 236 à 238) ; racine cherchée par balayage puis dichotomie ; pour l'unanimité et le juge seul, une forme fermée en plus (écart vrai = 1,2 d (1 − ρ) et 0,6 d (1 − ρ)). Les comptes sont lus dans le champ entier `repliques_gagnees_par_comparaison` du résultat, recoupés avec les puissances.

**Faute du banc, jouée d'abord, sur les seuls champs de structure (§ 6, cinq contrôles) :**

| contrôle | constaté par moi |
|---|---|
| 210 cellules | 210, dans l'ordre de l'énumération gelée, à 200 comme à l'étage 1 |
| 2 000 répliques dans chaque cellule faisable | oui, dans les 49 cellules faisables (31 à l'écart de 0,05 ; 13 à 0,10 ; 5 à 0,15) |
| à 0,10, les treize mondes du § 1, point 5, et eux seuls | oui : aucun absent, aucun en trop ; ma faisabilité recalculée ne diffère sur aucune des 210 cellules |
| écart vrai égal à l'écart visé à 1e-9 près | plus grand écart 4,2e-17 (champ) ; 8,3e-17 (mon recalcul) ; mon `d` à 1,9e-16 au plus du résultat (1,4e-16 par la forme fermée) |
| `d`, a, b égaux à l'étage 1, cellule par cellule | 372 valeurs comparées, toutes égales ; a = 0,20 + d et b = 0,20 − d exacts |

Aucun manque : pas d'issue C. Le manifeste porte n = 200.

**Comptes qui décident (§ 3) :**

| comparaison | plus bas compte sur 2 000 | cellule | verdict lu |
|---|---|---|---|
| contre l'unanimité | 701 (0,3505) | loi 1, ρ = 0, rang 14 | égal |
| contre le premier juge seul | 1 634 (0,8170) | loi 3, ρ = 0, rang 63 | égal |
| contre le second juge seul | 1 626 (0,8130) | loi 1, ρ = 0, rang 56 | égal |
| contre le bras R (un juge, trois votes, majorité) | 1 689 (0,8445) | loi 3, ρ = 0, ρ′ = 0,5, rang 148 | égal |

Cellules lues : 6, 3, 3 et 4 ; aucune comparaison sans cellule faisable. **Puissance qui décide : 701 sur 2 000.** 701 est sous 1 000 : « sous 0,5 » strict tenu, **issue B** par la lettre du § 3. 701 est hors de 956 à 1 044 : pas « près du seuil ». Les seize comptes des treize mondes à l'écart de 0,10, à 100 et à 200, sont ceux que le verdict écrit, un par un.

**Déclencheurs de l'audit (§ 6) :** puissance à l'étage 1 : 320 sur 2 000 (0,160 ; unanimité, loi 3, ρ = 0), donc 200 n'est pas sous 100 ; pas au-dessus de 0,90 ; dans l'intervalle prédit ; trois comptes nuls exactement (bras R, rangs 0, 2 et 4, écart de 0,05, monde de l'unanimité), aucun sur une comparaison plantée. 58 lignes comparées à 100 : aucune ne baisse. Écart vrai du bras R à ρ′ = 0 contre « au moins un » dans ces trois cellules : −0,068 ; −0,065 ; −0,051 ; écarts observés moyens : −0,084 ; −0,079 ; −0,067. Replis du bras C : 0 dans les 49 cellules. À 0,10, « au moins un » est la règle la plus choisie dans chacune des treize cellules (de 1 228 à 1 959).

**Aide du code, lue en dernier :** issue B, 0,3505, 701, minima 701 ; 1 634 ; 1 626 ; 1 689 : égale à mon recalcul.

## 4. L'ordre des gestes

- **Faute du banc avant toute puissance : tenu.** Le programme de la faute du banc ne garde que douze champs de structure ; il ne lit ni puissance ni compte gagné (lu dans son code).
- **Audit de symétrie écrit avant le prononcé : tenu.** Il est à la section 2, avant les sections 3 et 5. Il part par la lecture à la lettre du déclencheur « 0 ou 1 exactement » (toute comparaison d'une cellule faisable), déclarée à l'écart 5 du verdict : c'est la lecture la plus stricte, et elle est la même dans les deux sens. Les cinq relectures du § 6 y sont. J'ai relu les deux qui tiennent au code du banc v4 : n = 200 donne 100 par classe, puis 50 bons et 50 mauvais en lecture (`cellule_puissance`, `indices_moities`) ; Holm sur quatre au niveau 0,05 et écart observé de 0,05 au moins (`holm`, `NIVEAU_HOLM`, `MARGE_COMPARAISON`).
- **Aide du code comparée après : tenu.** Le programme des comptes ne lit pas `criteres_mecaniques` ; seul le quatrième programme le lit.
- Remarque, sans correction : le programme des comptes rend l'issue en même temps que les déclencheurs de l'audit. Trois déclencheurs sur quatre demandent la puissance qui décide ; l'agent ne pouvait pas les lire sans elle. L'ordre des fichiers sur disque ne se vérifie pas (même minute) ; je m'en tiens à la construction des programmes et à l'ordre des sections.

## 5. La prédiction et l'étage 2

- **Prédiction du § 1** (« sous 0,5 : entre 0,30 et 0,50 » ; réfutation à 0,5 ou plus) : 0,3505. **Tenue**, à la lettre. Le verdict le dit, avec la réserve juste (prédiction calée sur le 0,160 connu).
- **Ce que l'issue B fait de l'étage 2 à 200** : le verdict reprend la colonne 3 du § 3 mot pour mot (clause de l. 343 ; rangs 2 et 4 hors d'atteinte ; aucun « oui » possible ; rang 3 garde son « non » ; ρ′ − ρ « positif » rapporté comme une mesure ; le reste non concluant), ajoute que la taille reste 200 dans les deux issues, et ne décide rien de la dépense. Conforme.

## 6. Correction demandée

**Correction 1 — section 2, relecture 3.** La phrase donne pour le monde de l'unanimité à l'écart de 0,05 une plage de d et une fréquence qui ne s'accordent pas avec la sortie de l'audit. Ce monde a neuf cellules faisables, de d = 0,042 à d = 0,167. « Au moins un » y est choisi de 650 à 768 fois sur 2 000 aux sept cellules où d vaut 0,076 au plus, mais 939 fois à d = 0,104 (rang 4) et 1 313 fois à d = 0,167 (rang 5). Aucun compte qui décide n'est touché.

Ancre (comptée une fois par `grep -c -F -e` dans le verdict) :

Ancien :

> (d de 0,042 à 0,104), « au moins un » n'est choisi qu'environ une fois sur trois et, aux rangs 0 et 7, un juge seul l'est un peu plus souvent (670 et 686 contre 650 et 660)

Neuf :

> (neuf cellules faisables, d de 0,042 à 0,167), « au moins un » n'est choisi qu'environ une fois sur trois aux sept cellules où d vaut 0,076 au plus (de 650 à 768 sur 2 000), puis 939 fois à d = 0,104 (rang 4) et 1 313 fois à d = 0,167 (rang 5) ; aux rangs 0 et 7, un juge seul l'est un peu plus souvent (670 et 686 contre 650 et 660)

## 7. Remarques, sans correction

1. Le § 3 dit « lue sur les comptes entiers ». Le verdict tire ses comptes des puissances (k = puissance × 2 000, contrôle exact), non du champ entier `repliques_gagnees_par_comparaison` que le résultat porte. Les deux lectures sont égales dans les 49 cellules faisables (mon programme lit le champ entier et le recoupe).
2. Écart 8 du verdict : le commit `f1b1f95c` existe (« Travaux en cours versés pour ne rien perdre ») ; je n'ai pas relu ce qu'il verse. Les octets des huit pièces sur disque sont ceux de la section 7.
3. L'arbre de travail est sur la branche `claude/sharp-ramanujan-eks887`, dont la tête (`68c9fb2b`) est celle de `origin/main`.

## 8. Mes écarts

1. **Premier appel avant la lecture du mandat.** Pour vérifier l'empreinte du mandat, j'ai lancé une commande chaînée (`&&`) qui contenait `ls -la` sur les dossiers `additif-3-portee-200-v1/` et `verdict-portee-200-v1/`, `git status --short` et `git branch --show-current`. Le mandat interdit la liste et le chaînage ; je ne l'avais pas encore lu. Sortie : noms et tailles des fichiers de ces deux dossiers, nom de la branche ; aucune mesure. Ensuite : une commande simple par appel, aucun joker, aucune liste.
2. J'ai lu des parties du banc v4 (`classes`, `indices_moities`, `holm`, `p_valeur_unilaterale`, début de `cellule_puissance`) et trois passages du texte v7 hors des lignes nommées (l. 96 à 105, l. 205), pour écrire mes formules et relire l'audit.
3. Un petit programme de plus dans mon bloc-notes (`structure_v1.py`) a lu les seuls noms des clés des deux résultats, sans valeur ; il n'est pas versé.
4. Mes programmes ont été écrits et lancés dans mon bloc-notes, puis le programme de recalcul et sa sortie copiés à l'identique ici.

Aucune relance de la mesure, aucune graine, aucun changement de règle ; aucun commit, aucun réseau, aucune dépense ; rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`.

## 9. Mes pièces

Dossier `verdict-portee-200-v1/contre-lecture-v1/`, chacune avec son compagnon `.sha256`.

| fichier | sha256 |
|---|---|
| `recalcul_contre_lecture_verdict_portee_200_v1.py` | `727091615e293ba8368557e05292bf3d24b1c6daa780e36ccc946bc1e8dd4014` |
| `sortie-recalcul-contre-lecture-verdict-portee-200-v1.json` | `48b5006fb218b9e38d821387928bf02b7ea226830a44450c49b3563f10b1b7f1` |

Lancement : `python3 -B recalcul_contre_lecture_verdict_portee_200_v1.py RESULTAT_200 RESULTAT_ETAGE_1 MANIFESTE_200 SORTIE_JSON` (le résultat de l'étage 1 est la copie de mon bloc-notes, section 1).

Contre-lecteur neuf, modèle F.
