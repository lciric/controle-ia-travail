# Contre-lecture (R2) — conception du monde riche, famille MR-2, fichier `conception-monde-riche-doublons-v6.md` — tour 2, v1

- **Lecteur** : modèle C, lecteur neuf ; je n'ai écrit aucune des pièces. Lecture entière de la v6 (618 lignes) et de ses deux différentiels.
- **Heures** (`date -u`) : début 2026-11-17 01:13:34 ; fin de rédaction 2026-11-17 01:15:17 (relevée juste avant le scellement).
- **Pièce lue** : `conception-monde-riche-doublons-v6.md`, `59bdeff4ad5914ebeed8751ae645134f04ed57a15e9ff2178c9f13d183d8cdde` (égale au compagnon).
  Version précédente : `conception-monde-riche-doublons-v5.md`, `a12ab1e5…` (égale au compagnon). Le brief appelle « conception v5 » la pièce v6 du fichier.

## Verdict (une ligne)

**Corrections** (aucune majeure, trois mineures) : les six couples du tour 1 sont appliqués fidèlement et le différentiel ne contient rien d'autre ;
trois défauts restent, dont deux créés par la v6 elle-même (étiquette de lignée du rédacteur, audit de flux, essai manquant).

## Ce que j'ai vérifié

| contrôle | résultat |
|---|---|
| empreintes v5, v6, différentiel v5→v6, `appliquer_corrections_v6_v1.py` | égales à leurs compagnons |
| `diff -u` v5 → v6 refait | **identique** (hors deux lignes d'en-tête) au `differentiel-conception-v5-v6.diff` (118 lignes) |
| rien d'autre dans le différentiel | 8 zones touchées, toutes comptées : titre et « Statut » (m-2), « Rédacteur » (m-3), « Rédacteur de la v6 » et « Heures » (en-tête), §3.2 (m-1), §4.1 (m-4), §7 (m-3), §8 première ligne (M-1) et ligne « Taux d'erreur » (m-5), section « Contre-lecture » ajoutée. Aucun chiffre ne change |
| chaque couple du rapport tour 1 | recopié exactement ; chaque « ancien » figurait une fois dans la v5 (le programme le vérifie) ; les « nouveaux » du différentiel sont les textes du rapport, caractère pour caractère, pour M-1, m-1, m-2, m-4, m-5, et les trois couples de m-3 |
| faits cités par M-1 | devis du banc v3 (`ec5a6e99…`) lignes 34, 68, 150, 188 : importe `monde_riche_v4.py` sans le modifier, « code v68 gelé » = arbre v68 à v74 ; exact |
| faits cités par m-1 | `monde_riche_v4.py` (`4b165847…`) : graine du flux de génération (`rng_de("v4-gen", w, masquage)`), du juge et du test de mort portent `masquage` ; exact (le complément « test de mort, ligne 237 » est juste aussi) |
| §3.2, §3.4, §4.1, §8 relus après retouche | chiffres intacts ; dénominateur « tous les mondes tirés » intact (g_r = 0 sans tirage conforme en 8, G sur 24, `2·G ≥ N`) ; P_CACHÉE = 0 décide |
| lectures interdites | aucune dans la pièce (pas de 7a, 7b, T0.6, T0.7, B bis, P3-bis, bras d'attaque, mode tenu à l'écart ; rien sous `diag/`, `runs/`, `donnees/`) ; aucune valeur de clé |

## (1) Les corrections du tour 1, une à une

| # | verdict |
|---|---|
| M-1 | **appliquée fidèlement** ; la tension reste ouverte, dite telle (« lecture à confirmer par la mère ») ; voir points pour la mère |
| m-1 | **appliquée fidèlement**, mais le texte voisin n'est pas mis en accord : voir C-2 |
| m-2 | appliquée ; le texte inséré est exact (trois retouches seulement) |
| m-3 | appliquée pour les trois couples ; noms cités du verdict laissés à la mère, comme le rapport le demandait |
| m-4, m-5 | appliquées fidèlement |

## Corrections exigées (toutes mineures)

**C-1 — L'étiquette « modèle C » donnée au rédacteur de la v6 est fausse ou, au mieux, brouille la condition de lignée.** Le brief dit que les
corrections sont écrites par le modèle A, et que le lecteur du tour 1 comme celui du tour 2 est le modèle C. La v6 se déclare rédigée par « modèle C »
(deux endroits), alors que le même modèle C est le lecteur du rapport (ligne 588) ; la phrase finale demande un tour 2 par un lecteur « ni le rédacteur de la v6
ni celui du rapport », qui ne peut être ni le modèle C ni, si le rédacteur est A, ... mais A est la lignée du rédacteur de la v5 : l'exigence « autre lignée »
du §7 doit alors se lire pour la v6 aussi. La mère confirme qui a écrit la v6 ; si c'est A, les trois couples suivent.
- ancien : `- **Rédacteur de la v6** : modèle C, sous-agent neuf d'un script d'orchestration ; je n'ai écrit ni la v4, ni la v5, ni`
- nouveau : `- **Rédacteur de la v6** : modèle A (même lignée que le rédacteur de la v5), sous-agent neuf d'un script d'orchestration ; je n'ai écrit ni la v4, ni la v5, ni`
- ancien : `Rédacteur de la v6 : modèle C, neuf, qui n'a écrit ni la v5 ni son rapport.`
- nouveau : `Rédacteur de la v6 : modèle A (même lignée que le rédacteur de la v5), neuf, qui n'a écrit ni la v5 ni son rapport.`
- ancien : `la condition de lignée posée au §7 (réserve « Lignée ») est remplie pour la v5.`
- nouveau : `la condition de lignée posée au §7 (réserve « Lignée ») est remplie pour la v5 ; pour la v6, elle exige un lecteur d'une autre lignée que le modèle A du rédacteur de la v6.`

**C-2 — La phrase de l'audit de symétrie contredit la correction m-1.** Le §3.2 dit désormais que la passe 0,25 « sans masquage » n'a pas le même flux (code v4),
mais l'audit « relit … l'égalité des flux entre passes » sans réserve : dans la v4 il échouerait par construction sur cette passe et déclencherait un audit sans cause
(la v6 le sait et a décidé de ne pas le réécrire faute de couple ; le défaut subsiste). Il faut que les deux phrases s'accordent.
- ancien : `et l'égalité des flux entre passes.`
- nouveau : `et l'égalité des flux entre passes (la passe 0,25 « sans masquage » exceptée tant que le module neuf n'a pas séparé la graine du drapeau de masquage, voir « Passes rapportées » ; un écart de flux sur une autre passe est une anomalie).`

**C-3 — La séparation de la graine du drapeau est « à essayer (R5) » mais aucun essai ne la porte.** La liste R5-1 à R5-7 (§2.4) est la liste des essais exigés avant le gel ; m-1 y ajoute
une exigence de code sans ligne. Sans essai, rien n'établit que la séparation laisse les passes à masquage vrai égales à la v4 (R5-7) tout en donnant un flux commun à la passe 0,25.
- ancien : `Ces essais sont du **code**, non de la conception : ils ne sont pas faits ici.`
- nouveau : `Ces essais sont du **code**, non de la conception : ils ne sont pas faits ici. S'y ajoute, exigé par la correction m-1 de la contre-lecture v5, un essai R5-8 : cas sain, le flux de proposition de la passe 0,25 « sans masquage » est égal à celui des autres passes sur les 12 graines de développement et les passes à masquage vrai restent égales à la v4 (R5-7) ; artefact, la graine rendue dépendante du drapeau : écart de flux détecté.`

## Remarques facultatives (aucune n'est exigée)

- Lignes 565-566 (§7) : « cette v5 » désigne la pièce précédente ; sans effet, la section « Contre-lecture » dit l'état.
- Les remarques facultatives du tour 1 (audit de symétrie presque certain à P_CACHÉE = 0 ; type de E1 pour C0 ; hypothèses de la table du §3.4) restent non appliquées ; c'est permis.
- La ligne « Rédacteur » dit encore « Je n'ai écrit ni la v4… » au sein d'une rédaction par A : lecture « instance neuve », sans objet.

## Points pour la mère

1. **Qui a écrit la v6** : la pièce dit « modèle C » ; le brief dit A. À confirmer (C-1). Si c'était bien un modèle C, la contre-lecture du tour 2 que je fais n'est pas d'une autre lignée, et il faut un lecteur A ou B.
2. **M-1 reste ouverte** (écart au devis v3 : importer `monde_riche_v4.py` sans le changer, ou module neuf à noms neufs égal à la v4 sur 12 graines). C'est la mère qui tranche, avant la pièce des règles du banc.
3. **Noms de modèles avec version** dans la pièce (proposeurs et relais cités du verdict v2 et des lignes de GO ; budget « Claude » ; `verifier_monde_kimi_v1.py` est un chemin) : la v6 les garde et dit pourquoi ; le brief veut « aucun identifiant de modèle ». À trancher : conserver comme citations de pièces qui font foi, ou remplacer par des lettres (ce qui coûte la fidélité aux citations du verdict).
4. Rappel des risques déjà dits par la pièce : la règle tient presque par construction à P_CACHÉE = 0 ; à la borne haute 0,043 elle ne tiendrait qu'avec une probabilité de 0,08 à 0,17 ; le banc ne garde pas contre des proposeurs qui ne masquent pas.

## Incidents de ma main

- Un fichier de travail `d56.diff` dans le bloc-notes (diff v5 → v6 pour comparaison), hors dépôt.
- Une première commande avec une redirection vers une variable vide (`$TMPDIR_X`) a échoué sans rien écrire.
- Aucune machine, aucun appel de modèle ou de loueur, aucune dépense ; aucune branche `calcul/pilote-mr2-v74-entree-*` ouverte ; aucun secret ; aucune pièce modifiée ; rien committé.
