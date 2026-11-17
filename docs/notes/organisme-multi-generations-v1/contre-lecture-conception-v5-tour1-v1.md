# Contre-lecture (R2) — conception v5 du monde riche (famille MR-2, règle de garde opératoire) — tour 1, v1

- **Lecteur** : modèle C, lecteur neuf, autre lignée que le rédacteur de la pièce (modèle A) et que le lecteur de la v4 (modèle B).
  Je n'ai écrit aucune des pièces. Lecture entière de la pièce (577 lignes).
- **Heures** (`date -u`) : début 2026-11-17 01:05:51 ; fin de rédaction 2026-11-17 01:10:23 (relevée par `date -u` juste avant le scellement).
- **Pièce lue** : `conception-monde-riche-doublons-v5.md`, `a12ab1e50190b8d27ce6daa0e5c44b81f04c674a916103f518d093400b7481d9`
  (égale au compagnon).

## Verdict (une ligne)

**Corrections** : la v5 applique bien les neuf corrections de la v4 et rend la règle opératoire, sans changer un chiffre de la v4 ;
une seule correction majeure (la lecture de « code v68 » est présentée comme conforme au GO alors qu'elle contredit le devis v3 du
banc), quatre mineures ; aucune lecture interdite ; aucun identifiant de modèle au sens strict, mais des noms de modèles restent.

## Ce que j'ai vérifié (et comment)

| pièce | empreinte | contrôle |
|---|---|---|
| conception v5 | `a12ab1e5…` | égale au compagnon |
| différentiel v4→v5 | `127e615a…` | égale au compagnon ; **identique octet pour octet** au `diff -u` que j'ai refait de v4 et v5 (hors deux lignes d'en-tête) |
| conception v4, contre-lecture v4 v2 | `47e38ec0…`, `16da94d4…` | égales ; lues en entier (la seconde) |
| `outils-v5/*.py`, `sorties-v5/*` (9 fichiers) | compagnons | tous égaux à leur compagnon |
| `monde_riche_v4.py` | `4b165847…` | égale ; lu : `course`, `EXIGENCES_V4`, `tirer_gabarit_v4`, `verifier_v4` |
| verdict v2 du pilote (par `git show` d'une référence distante déjà présente, sans rien écrire dans le dépôt) | `e64458e8…` | égal ; chiffres du §8 recontrôlés (voir plus bas) |
| lignes `GO-2026-11-13-01`, `-02`, `GO-2026-11-16-08`, `GO-2026-11-17-05`, décisions R-2500 à R-2510 | registres vivants | lues |

**Rejeu** : `calcul_regle_v5.py` rejoué dans le bloc-notes (sortie hors dépôt, `ulimit -v 6000000`, `OMP_NUM_THREADS=2`,
numpy 2.5.3) : sortie standard **identique** à `calcul-regle-v5.stdout`. La table du §3.4 se relit exactement dans le champ `table`
(toutes les fourchettes recomptées : q, règle tenue sur 24 et sur 12, bascules 0,0283 / 0,0318 / 0,0300 / 0,0336 / 0,0463 / 0,0507,
0,91 et 0,67 pour « aucun monde sans tirage conforme », baisse de moins de 0,03 à ρ = 0,6 : 0,025 au plus). P(G = 24) à ρ = 0,5 :
0,9961²⁴ = 0,910 (la v5 dit 0,91). Borne haute 1 − 0,025^(1/84) = 0,042965 (égale au verdict : 0,2316 sur 14 appels ramené à six cartes).
Les motifs et sortes du §4.1 sont recomptés dans les sorties : C6 8 tirages, 10 vraies en écart (4 interactions de sous-population
fortes, 4 décalages moyens, 2 faibles), 11 composantes en trop (10 faibles, 1 moyenne), **6 sur 10 sur la même sous-population**,
aucune conditionnelle en écart ; C0 aux mondes 1, 4, 7 ; C3 au monde 11 ; `tous_egaux` vrai ; 1 − (10/12)² = 0,306.
Chiffres du §8 contre le verdict : 0 sur 14 (4, 4, 3, 3), [0 ; 0,043], 14 sur 14, c = 6, 73 cartes, 42 tirées, `si_sinon` 3,
Fable tronqué 2 sur 4, durées, taux 0,21 / 0,27 / 0,09 à 14 appels : tous justes ; 1 − 0,75⁶ = 0,822.

## (1) Les neuf corrections, une à une

| # | verdict | observation |
|---|---|---|
| E-1 | **appliquée** | bascule écrite (§3.3 point 1, §3.4), « le banc ne mesure que les mondes » (point 2), 0,25 estimé (point 3) ; table exacte rejouée ; §0 et §4.2 mis en accord |
| E-2 | **appliquée** | §2.1 « Ce que MR-2 ne fait pas », §2.3 « Non examiné », §6 ligne §1-§2 |
| E-3 | **appliquée** | phrase du §6 retirée (R-2504, texte du registre vérifié) ; plus aucune occurrence de « existence possible » hors de la table qui la cite comme ancien |
| E-4 | **appliquée** | Q-14 reclassée nœud, option (c) dite factice, tranchée (b) (R-2501, GO-2026-11-16-08) |
| E-5 | **appliquée** pour ce qu'elle demande (essais listés, noms neufs) ; **voir M-1** pour la tension avec « code v68 » et le devis v3. Je confirme par lecture du code le constat sur la borne de 10 composantes (`monde_riche_v4.py`, ligne 97 : tenue par le gabarit seul ; `EXIGENCES_V4` ne la porte pas). La borne des leurres, elle, est bien contrôlée par le vérificateur (`distracteurs_min`) : R5-5 est juste |
| E-6 | **appliquée** | motifs rejoués à l'identique, sortes comptées, sélection déclarée ; réserve de portée en m-4 |
| E-7 | **appliquée** | essai à blanc dit non consigné ; antériorité dite telle qu'elle est ; ordre « versés et poussés avant l'engagement » écrit au §3.2 |
| E-8 | **appliquée** | N = 24 fixé ; dénominateur = tous les mondes tirés ; G_cond ; passes rapportées ; table refaite |
| E-9 | **appliquée** | (i), (ii), (iii) écrits au §6 et au §4.4 ; 0,31 juste |

## (2) Règle opératoire, dénominateur

Opératoire : N = 24 fixé, g_r défini pour les trois cas (aucun tirage conforme en 8 → 0 ; certifiée non captée non vide → 1 ;
sinon 0), G = somme sur les 24 mondes tirés, règle `2·G ≥ N` en entiers (essais 12/11 sur 24 et 6/5 sur 12 dans le programme),
ordre D-2 (sixième étape, brouillon 3 ligne D-2 : « f, fusion, n, forme, τ, mesure de la règle » : concorde), P_CACHÉE = 0 décide,
passes rapportées avec l'ordre « la passe qui décide se joue la première », antériorité (versement avant engagement). Dénominateur
conforme à GO-2026-11-17-05 (Q-B3 (a)) et au mot de Lazar. La règle tient « presque par construction » à P_CACHÉE = 0 : la pièce le
dit elle-même (§3.3, §3.4, réserves) et ne cache pas que la garde contre les proposeurs vient du pilote. Je confirme que c'est
exact : tout monde conforme porte une conditionnelle certifiée que, à P_CACHÉE = 0, aucune carte de la génération 1 ne porte.
Défauts d'opérativité : M-1 (code) et m-1 (flux), plus les remarques facultatives.

## (3) Rien d'autre ne change

Le différentiel est complet et fidèle. Aucun chiffre de la v4 n'est modifié (comparaison des lignes retirées : seulement texte,
en-tête, §3.2, §3.3, §4.1 motifs, §6 lignes citées, §7, §8 neuf). **Mais** la phrase « **et rien d'autre** » est trop forte : trois
retouches de cohérence ne sont dans aucune ligne de la table des changements (m-2).

## (4) Lectures interdites, identifiants

Aucune lecture interdite : du pilote, seul le verdict v2 est cité ; le rapport du développeur de la branche `prep/pilote-mr2-v1`
est cité par empreinte, §0 à §2, ce que les interdits permettent ; ni 7a, 7b, T0.6, T0.7, B bis, P3-bis, bras d'attaque, mode tenu à
l'écart, ni `diag/`, `runs/`, `donnees/` dans la pièce (recherche par motifs : aucune occurrence). Aucune valeur de clé.
**Identifiant de modèle** : l'identifiant entre accents graves de la v4 est bien retiré (aucune chaîne de la forme `claude-…`), **mais**
des noms de modèles avec leur version subsistent aux lignes 24, 558, 559, 569, 575 et 576, et des noms de relais aux lignes 483, 486
et 569 (les couples ci-dessous doivent citer ces textes pour être exacts ; c'est la seule raison pour laquelle ils paraissent ici). Si la consigne « aucun identifiant de modèle » vise aussi ces noms, c'est la correction m-3 ; si elle ne vise
que les identifiants de l'interface, c'est sans objet pour les lignes 483 à 576 (reprises du verdict et du GO). À trancher par la mère.

## Corrections exigées

**M-1 (majeure) — La lecture de « code v68 gelé » est donnée pour conforme au GO alors qu'elle contredit le devis v3 du banc, sans le
dire.** Le GO-2026-11-17-05 (Q-B2 (b)) dit « après la pièce des règles du banc et le code v68 de la course contre-lus » ; le verdict
du pilote dit « code v68 gelé ». Le devis v3 du banc (`banc-calibration-mr2-v1/devis-banc-calibration-mr2-v3.md`, `ec5a6e99…`, lignes
34, 68, 150, 188) fait **importer `monde_riche_v4.py` sans le modifier** et lit « code v68 gelé » comme l'arbre v68 à v74 du pilote.
La v5 (§2.4, E-5, essai R5-7) exige au contraire un **module neuf à noms neufs**, égal à la v4 sur 12 graines, et écrit (§8, première
ligne) que c'est « conformément à GO-2026-11-17-05 ». C'est une lecture, pas une conformité : elle change ce que le GO appelle « le
code contre-lu » (un module que ni le développeur du code v68 ni un lecteur n'ont encore vu). Les deux pièces sont à mettre
d'accord avant la pièce des règles du banc ; la v5 doit le dire à l'endroit où elle invoque le GO.
- ancien : `conformément à GO-2026-11-17-05 (banc complet) |`
- nouveau : `au titre de GO-2026-11-17-05 (banc complet), **lecture à confirmer par la mère** : le devis du banc v3 (`ec5a6e99…`, lignes 34, 68, 150 et 188) importe `monde_riche_v4.py` sans le modifier et lit « code v68 gelé » comme l'arbre v68 à v74 du pilote, alors que E-5 exige un module à noms neufs égal à la v4 (R5-7) ; la pièce des règles du banc et le devis du banc complet fixent laquelle des deux lectures vaut, avant tout engagement de secret |`

**m-1 — « Même flux » : faux pour la passe « sans masquage » dans le code v4.** Le §3.2 dit que les passes « ne diffèrent que par le
seuil appliqué à la même uniforme », y compris la passe 0,25 « sans masquage », et l'audit de symétrie lit « l'égalité des flux entre
passes ». Dans `course` (v4, lignes 212 et 231), la graine du flux de proposition et celles du juge portent le **drapeau de
masquage** : la passe « sans masquage » n'a donc pas le même flux que les autres, et l'audit y échouerait par construction.
- ancien : `(indice de flux = rang r ; `course` tire une`
- nouveau : `(indice de flux = rang r ; dans la v4 la graine du flux porte le drapeau de masquage : la passe 0,25 « sans masquage » n'a donc pas le même flux que les autres, sauf si le module neuf sépare la graine du drapeau, à coder et à essayer (R5) ; `course` tire une`

**m-2 — « Et rien d'autre » dépasse la table des changements.** Trois retouches ne figurent dans aucune ligne : le dernier point du §5
(« v5 : ce point est dépassé par GO-2026-11-17-05… »), la cellule « §17 (devis) » du §6 (« à revoir dans la pièce du devis avec les
coûts par appel du pilote »), les réserves du §7 (modèle de proposeurs, « règle presque par construction », ordre v5, ordre des classes
pour la fusion, lignée). Elles sont toutes des mises en cohérence, aucune ne change un chiffre ; le texte doit le dire.
- ancien : `**et rien d'autre**`
- nouveau : `**et rien d'autre que des mises en cohérence sans effet sur un chiffre, ajoutées sans ligne propre dans la table : dernier point du §5, cellule « §17 (devis) » du §6, réserves du §7**`

**m-3 — Noms de modèles encore dans la pièce** (si la consigne les vise ; voir §4 plus haut). Lignes 24 et 558-559 :
- ancien : `Claude Opus 5.5, sous-agent neuf` — nouveau : `modèle A, sous-agent neuf`
- ancien : `(Claude Opus 5.5) ; la contre-lecture de la v4 venait` — nouveau : `(modèle A) ; la contre-lecture de la v4 venait`
- ancien : `d'une autre lignée de la même maison (Fable) ; celle de la v5` — nouveau : `d'une autre lignée (modèle B) ; celle de la v5`

Pour les noms de relais et de modèles cités du verdict aux lignes 483, 486, 569, 575, 576 : décision de la mère (je ne donne pas de
couple, car chacune de ces occurrences est un nom cité du verdict et des lignes de GO, où il fait foi).

**m-4 — Sélection de C6 : portée dite trop large.** Le §4.1 constate sur 8 tirages refusés que C6 ne touche pas aux conditionnelles,
puis écrit sans réserve que C6 « ne sélectionne pas » sur elles.
- ancien : `il **ne sélectionne pas** sur les conditionnelles`
- nouveau : `il **n'a pas sélectionné** sur les conditionnelles dans ces 12 graines (8 tirages refusés, aucune « K1 + conditionnelle » en écart) ; rien ne le garantit pour les 24 mondes du banc, où les refus se rapportent par motif (§3.2)`

**m-5 — Réserve du verdict v2 omise au §8.** Le verdict (ligne 75) écrit que x = 0 sur 14 est « trop propre pour l'hypothèse » ; le §8
relaie la phrase « ne l'a pas réfuté » mais pas cette réserve, qui commande la lecture de l'audit R4 (symétrie) de la course.
- ancien : `il ne l'a pas réfuté. « Une issue`
- nouveau : `il ne l'a pas réfuté ; le verdict écrit aussi que x = 0 sur 14 est « trop propre pour l'hypothèse » (réserve d'audit, qui ne change pas l'issue). « Une issue`

## Remarques facultatives (aucune n'est exigée)

- Le déclencheur d'audit « G = 24 à P_CACHÉE = 0 » se produira dans le cas le plus probable (0,91 à ρ = 0,5, 0,67 à ρ = 0,6) : l'audit
  est donc presque certain ; ce n'est pas faux, mais autant le dire comme une étape ordinaire.
- C0 (§4.1) : « pente de E1, une principale » aux mondes 4 et 7 : les sorties de la v5 ne portent pas le type de E1 pour C0 ; le fait
  se lit dans les parties v4, que je n'ai pas rouvertes pour ce détail.
- La table du §3.4 suppose six cartes par appel et indépendance (le pilote en a admis moins de six par appel en moyenne) : dit pour
  la borne haute, pas pour la table ; une ligne suffirait.
- Le nom de fichier `verifier_monde_kimi_v1.py` (ligne 41) est un chemin, non un identifiant ; sans objet.

## Réponse aux questions de la mère (courte)

1. Neuf corrections : toutes appliquées ; E-5 appliquée mais à mettre en accord avec le devis v3 (M-1).
2. Règle opératoire : oui ; dénominateur tous les mondes tirés : oui ; réserve m-1 (flux) à fermer avant le code.
3. Rien d'autre ne change : vrai pour les chiffres, trop fort dans la phrase (m-2).
4. Lectures interdites : aucune ; identifiants : voir m-3.

## Incidents de ma main

- Un fichier de travail `/tmp/claude-0/d.diff` écrit hors du bloc-notes (le `diff -u` v4/v5 pour comparer au différentiel) ; en dehors du dépôt, sans effet.
- `calcul_regle_v5.py` rejoué avec sa sortie dans le bloc-notes (jamais dans `sorties-v5/`) ; le verdict v2 extrait par `git show` d'une référence distante déjà présente (aucun `fetch`, aucun clone, aucun git d'écriture).
- Aucune machine, aucun appel de modèle ou de loueur, aucune dépense ; aucune branche `calcul/pilote-mr2-v74-entree-*` ouverte ; aucun secret ; aucune pièce modifiée ; rien committé.
