# Contre-lecture (R2) — conception du monde riche, famille MR-2, fichier `conception-monde-riche-doublons-v7.md` — tour 3, v1

- **Lecteur** : modèle C, lecteur neuf ; je n'ai écrit aucune des pièces. Lecture du différentiel v6 → v7 en entier, des passages touchés et des endroits que les corrections ont pu déranger (§2.4, §3.2, §7, sections « Contre-lecture »).
- **Heures** (`date -u`) : début 2026-11-17 01:17:57 ; fin de rédaction 2026-11-17 01:18:55 (relevée juste avant le scellement).
- **Pièce lue** : `conception-monde-riche-doublons-v7.md`, `1f1b64df885a5215eb481692671e73167a16e7cfc3d5558610f3d45811d1137a` (égale au compagnon).
  Version précédente : `conception-monde-riche-doublons-v6.md`, `59bdeff4…` (égale à celle citée par la pièce). Le brief appelle « conception v5 » la pièce v7 du fichier.

## Verdict (une ligne)

**Scellable** : les trois corrections du tour 2 (C-1 à C-3, cinq couples) sont appliquées fidèlement, le différentiel ne contient rien d'autre, aucun chiffre ne change ; aucune correction exigée, deux remarques facultatives.

## Ce que j'ai vérifié

| contrôle | résultat |
|---|---|
| empreintes v7, différentiel v6→v7, rapport du tour 2, `outils-v7/appliquer_corrections_v7_v1.py` | égales à leurs compagnons ; rapport du tour 2 = `3ea95e1c…` |
| `diff -u` v6 → v7 refait | **identique** (hors les deux lignes d'en-tête) au `differentiel-conception-v6-v7.diff` (110 lignes) |
| rien d'autre dans le différentiel | 6 zones : titre et « Statut » (version v7), « Rédacteur de la v6 » (C-1), nouvelle ligne « Rédacteur de la v7 », « Heures » (ajout v7), §2.4 (C-3), §3.2 audit (C-2), section « Contre-lecture (v6 …) » (deux couples de C-1), section « Contre-lecture (v7 …) » ajoutée. Aucun chiffre, aucune règle, aucune table changée |
| chaque « ancien » du rapport tour 2 | figure **une seule fois** dans la v6 (compté : 1, 1, 1, 1, 1) |
| chaque « nouveau » | recopié caractère pour caractère dans la v7 : C-1 (3 couples), C-2, C-3 (le reste de la ligne « Un échec de R5-7… » suit sans coupure) |
| faits cités par la section v7 | `monde_riche_v4.py` (`4b165847…`, égal) : la graine du flux de proposition (ligne 212), du juge (231) et du test de mort (237) portent le drapeau `masquage` ; exact |
| §3.2 et §3.4 relus | dénominateur « tous les mondes tirés » intact (N = 24, G sur les 24 tirés, `2·G ≥ 24`, un monde sans tirage conforme en 8 ne garde rien) ; P_CACHÉE = 0 décide ; passes rapportées sans décider ; ordre D-2 intact |
| accord des trois retouches entre elles | §3.2 « Passes rapportées » (« à coder et à essayer (R5) ») ↔ R5-8 (§2.4) ↔ audit de symétrie (exception de la passe 0,25) : cohérents ; la liste R5-1 à R5-7 de la table n'est pas touchée, R5-8 vit dans la phrase qui suit, comme le rapport le demandait ; aucun « sept essais » ailleurs à corriger |
| lectures interdites, identifiants | aucune lecture interdite dans la pièce ; aucune valeur de clé ; pas d'identifiant de modèle nouveau dans les retouches (les noms cités du verdict, déjà signalés, restent à la mère) |

## (1) Les corrections du tour 2, une à une

| # | verdict |
|---|---|
| C-1 (trois couples) | **appliquée fidèlement**. Le rédacteur de la v7 note lui-même que la lettre A est « probable, non établie par une pièce » : la réserve est dite, la mère confirme |
| C-2 | **appliquée fidèlement** ; l'audit et « Passes rapportées » s'accordent |
| C-3 | **appliquée fidèlement** : essai R5-8 avec cas sain et artefact |

## (2) à (4)

- (2) Règle opératoire, dénominateur « tous les mondes tirés » : inchangés et conformes à GO-2026-11-17-05 (relus au §3.2 et au §3.4).
- (3) Rien d'autre ne change : confirmé par le différentiel refait.
- (4) Aucune lecture interdite constatée ; aucun identifiant de modèle ajouté.

## Remarques facultatives (aucune n'est exigée)

- R5-8 ne couvre que le flux de **proposition**. Dans le code v4 la graine du juge (ligne 231) et du test de mort (ligne 237) portent aussi le drapeau : si le module neuf ne sépare que la proposition, le juge et le test de mort de la passe 0,25 « sans masquage » restent sur d'autres flux, et « même flux de génération 1 » (§3.2) ne serait vrai que pour la proposition. Sans effet sur la décision (cette passe est rapportée, ne décide pas) ; à préciser dans le code ou la pièce des règles du banc.
- La ligne « Rédacteur de la v7 » raconte une lecture de consigne (« la consigne me nomme modèle C ») qui a plus sa place dans un registre que dans l'en-tête ; sans effet.

## Points pour la mère

1. **Lettre du rédacteur de la v6 et de la v7** : A est posée par déduction (le brief dit « corrections par le modèle A », le brief des rédacteurs dit « tu es du modèle C »). À confirmer par une pièce. Si c'était C, les trois couples de C-1 se défont. Moi, lecteur C, je suis d'une autre lignée que A ; je suis une autre instance que le lecteur du tour 2 (mêmes lettres) : la condition « ni le rédacteur ni celui du rapport » est remplie par instance, non par lettre.
2. **M-1 toujours ouverte** : le devis du banc v3 importe `monde_riche_v4.py` sans le changer ; la pièce exige un module à noms neufs égal à la v4 sur 12 graines (R5-7). À accorder dans la pièce des règles du banc avant le banc.
3. **Noms de modèles avec version** cités du verdict v2 et des lignes de GO : à trancher (garder comme citations ou remplacer par des lettres).
4. Rappel des risques dits par la pièce : la règle tient presque par construction à P_CACHÉE = 0 (probabilité au-dessus de 0,9999) ; à la borne haute 0,043 elle ne tiendrait qu'avec une probabilité de 0,09 à 0,17 ; le banc ne garde pas contre des proposeurs qui ne masquent pas. Lazar devrait le lire en clair avant le banc.
5. La pièce peut être scellée telle quelle ; le code du banc et la pièce des règles restent à contre-lire (ordre D-2, la règle en dernier).

## Incidents de ma main

- Un fichier de travail `d67.diff` dans le bloc-notes (diff v6 → v7), hors dépôt.
- Aucune machine, aucun appel de modèle ou de loueur, aucune dépense ; aucune branche `calcul/pilote-mr2-v74-entree-*` ouverte ; aucun secret ; aucune pièce modifiée ; rien committé.
