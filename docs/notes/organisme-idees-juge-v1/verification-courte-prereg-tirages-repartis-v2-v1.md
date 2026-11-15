# Vérification courte — différentiel v1 → v2 du préenregistrement « tirages répartis par blocs avec arrêt anticipé » (idée 1.2) — v1

- Lecteur : sous-agent neuf ; je n'ai écrit ni la v1, ni la v2, ni leurs contre-lectures, ni le banc, ni la preuve, ni le juge.
- Date (UTC) : 2026-11-15, 09:20 à 09:35 (`date -u`). Dépôt lu sur `main` ; aucun commit, aucune poussée, aucun appel payant ;
  rien écrit sous `diag/`, `donnees/`, `docs/verdicts/` ; aucun code des dossiers de copie exécuté (deux fichiers de la copie
  `94bfd92` lus, non joués). **Aucun résultat du banc n'existe et je n'en ai produit aucun** (R1).
- Pièces, toutes égales à leur compagnon : v1 `prereg-tirages-repartis-arret-anticipe-v1.md`
  (`2a500156d1b36855330e02c1a261cb40c882032ebf0090760e87b7695b876a65`) ; v2 `prereg-tirages-repartis-arret-anticipe-v2.md`
  (`c7f80e8c9fff5128ca60a1071b70519844a2f9ccdd9344f0ece0aab0e3e13c2b`) ; contre-lecture [CL]
  `contre-lecture-prereg-tirages-repartis-v1.md` (`5ae17f81cbeb83161e49d7d3ce5c8fa4ff38c4db9d38afd7cfc5b8ae676df109`) ;
  contre-lecture du 1.1 [CL-1.1] `contre-lecture-prereg-nul-limite-et-preuve-v1.md`
  (`763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e`) ; banc B v1 `prereg-nul-par-morceaux-limite-v1.md`
  (`46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089`) ; registre R-2875, R-2878, R-2881 lus.
- Programme de recalcul à moi et sa sortie (bloc-notes de la session, non durable, **recopiés en entier en annexe**) :
  `recalcul_verification_v1.py` (`d1066eaa4aa48badf2fd2f2cda93e37ef5379fcbcb3e689dec7ae60e3f7769ba`), `sortie-recalcul-verification-v1.txt` (`48371611b7ffeeceb0790568c4cf4276b63295e3cca2cac2120a4f71e3944347`).
- Les numéros de ligne renvoient à la v2, sauf mention.

## Verdict

**Scellable après corrections.** Les dix-sept remarques de [CL] sont portées, la ligne V5 et les deux mineurs repris du 1.1
aussi ; tous les chiffres neufs se recalculent à l'identique ; l'oracle ne dépend d'aucun résultat du banc ; aucune
revendication, aucune adoption. Restent **quatre corrections qui touchent les critères gelés ou le plan** (C1 à C4), **une
de déclaration** (C5), deux de forme (C6, C7) et une précision hors du différentiel (C8). Aucune ne demande de calcul neuf ni
ne change un seuil ; elles tiennent en une dizaine de lignes, sous un nom neuf (v3, R12 : la v2 est scellée par empreinte).
Une relecture du seul différentiel v2 → v3 suffit ensuite.

## Corrections demandées

**C1 — Les qualifications d'un gain ne sont pas exclusives (l. 267-268, étage 4 l. 400).** « d'effectif seulement » et
« sans effet de ciblage » peuvent être vraies ensemble (bornes hautes de C_A − C_F125 et de C_A − C_P toutes deux sous 0) ; la
table n'en dit rien. Défaut présent en v1, non relevé par [CL], mais le point (5) de la commande exige l'exclusivité.
- ancien (l. 267-268) : « "d'effectif seulement" si la borne haute de C_A − C_F125 < 0 ; "sans effet de ciblage" si la borne
  haute de C_A − C_P ≤ 0 ; "de structure" si aucune des deux. »
- nouveau : « … ; "de structure" si aucune des deux ; **si les deux sont vraies, les deux qualifications sont prononcées
  ensemble ("d'effectif seulement et sans effet de ciblage")**. » ; étage 4 : quatre issues au lieu de trois.

**C2 — Lectures de validité « par monde » sans critère (l. 247-248, 258-262, étages 1 et 1 bis l. 396-397).** Le texte dit
que les quatre lectures sont « lues sur les 500 générations ensemble, et pour chacun des deux mondes séparément », mais les
seuils de la lecture (1) n'existent que pour 500 (≤ 13, ≥ 39), et rien ne dit si une borne basse de moyenne > 1 **dans un
seul monde** (lecture (3)) déclenche « garantie mise en défaut ». Deux lecteurs pourraient prononcer deux verdicts.
- ancien (l. 247-248) : « Lues sur les 500 générations ensemble, et pour chacun des deux mondes (M₀, M₀′) séparément. »
- nouveau : « **Jugées** sur les 500 générations ensemble (seuils de la section "Seuil") ; **rapportées sans critère** pour
  chacun des deux mondes (250 générations ; pour mémoire, au niveau 0,05/7 : tenue ≤ 4, non tenue ≥ 23 sur 250). La lecture
  (2) vaut à chaque instant de chaque carte, donc dans chaque monde. » — ou, au choix de l'auteur, des seuils par monde
  écrits, avec la famille de comparaisons portée à quatorze (≤ 3, ≥ 24 sur 250 ; recalcul en annexe).

**C3 — Répartition des deux mondes de la famille N non écrite (l. 327).** « 250 à monde M₀ ; 250 à monde M₀′ » ne dit pas
lesquelles. La cellule est g mod 10 (l. 311, 331) : une répartition par parité confondrait monde et cellule (M₀ ne verrait
que les cellules paires ; recalcul en annexe).
- ancien : « **Famille N** (500 générations) : **250 à monde M₀** … ; **250 à monde M₀′** … »
- nouveau : ajouter « M₀ pour g de 0 à 249, M₀′ pour g de 250 à 499 (25 générations par cellule et par monde) ».

**C4 — Voisines du monde de la famille N : loi de base non désignée (l. 329-330).** La v1 (l. 188) disait « M₀ où S1 est
remplacée par softmax(W1 + 0,05·Δ, b1), Δ centrée » ; la v2 écrit « le monde dont la loi de base S_k est remplacée par
softmax(W_k + 0,05·Δ, b_k) » sans dire quel k pour M₀ (mélange de cinq lois), ni pour M₀′ quand la loi tirée est S3 ou S4
(lois `si_sinon`, sans W_k unique), ni que Δ est centrée. Changement non déclaré au tableau.
- nouveau : « pour M₀ : S1 (comme en v1) ; pour M₀′ : la loi d'archive tirée, **tirée parmi S1 et S2** (ou, si S3 et S4
  restent permises, la branche softmax U qui est déplacée est dite) ; Δ ~ N(0, 1) centrée par colonne, une par carte ».

**C5 — Tableau du différentiel incomplet (l. 62-88).** Aucun changement non déclaré ne modifie un seuil ou un critère **à
l'insu du lecteur**, mais plusieurs ne se rattachent à aucune ligne du tableau :
1. énoncés de la garantie resserrés (l. 127-131, 133-136, 138-151) : C1 « plans, instants, bibliothèque, m et α », C3 « ni les
   autres cartes », preuve du lemme « sachant G_k, de loi P*(· | x) », théorème (a) « règle adverse G », (c) réécrit, preuve
   (a) « exactement les issues révélées » — tous conformes à [CL] § 1.1 et § 1.2, que le tableau ne cite pas ;
2. paragraphe neuf « Confirmation par la contre-lecture » (l. 153-158) ; ses chiffres sont ceux de [CL] § 1.3 (0,0044 ±
   0,0009 ; 0,433 ± 0,038 ; 1,267 ; 2,618 ; 3,4 pour 3,377) — vérifiés ;
3. prédiction neuve **Q9**, avec un chiffre neuf « moyennes ponctuelles ≤ 0,8 » (l. 212) ; la ligne M3 du tableau ne cite ni
   « Prédiction » ni « Seuil » ;
4. phrases retirées : « Elle tranche la tension que le relevé signale (§ 1.2) en faveur de la règle [de la fiche] » (v1
   l. 98-99) ; « dérive à peine négative, le cas le plus dur pour la continuation » (v1 l. 189) ; « l'intérêt réel est pour
   les domaines où un tirage est cher » (v1 l. 270) ; renvoi inversé entre les deux préenregistrements (v1 l. 12 ; v2
   l. 21-22, décision de la mère R-2881) ;
5. clés de graines à quatre éléments par carte (construction, plan, issues fraîches) et clé de l'oracle (l. 361-364) ;
   lignes neuves de la liste d'arrêt (gel, domination, oracle après le rejeu, l. 416, 419, 422) ; mutations neuves (l. 372-374) ;
   « aucune moyenne ni médiane sur des jetons » (l. 251) ; H-1.2 « au plus égal » (l. 100) ;
6. le banc B est recopié (l. 275-306) avec des abréviations : « j uniforme » omis en Q5 et V2, loi de Δ omise en V1, loi de
   u omise en V2 ; C_decl, l'archive A0, la colonne « classes qui contiennent M » et les bras du 1.1 ne sont pas repris.
- nouveau : une ligne « [CL] § 1.1 et § 1.2 — énoncés du lemme et du théorème 2 alignés sur les six hypothèses exactes ;
  paragraphe de confirmation ; Q9 » et une ligne « autres retouches » qui liste 4 à 6 ; l. 21 : « le banc B v2 est défini
  ici **pour ce qui sert à l'idée 1.2** ; ce que le texte ne répète pas (lois de j, de Δ, de u ; C_decl ; archive A0) reste
  celui de [BANC-v1] ».

**C6 — m14 : « à confirmer » est périmé (l. 59-60, 84, 462).** R-2881, décision (2), a confirmé la recopie sous `prereg/`.
- ancien : « (décision de la mère, à confirmer) » ; nouveau : « (décision de la mère, R-2881) » ; ajouter R-2881 à la l. 47.

**C7 — Section « Contre-lecture » (l. 471-472).** La version qui fera foi cite cette vérification (chemin et empreinte) et le
traitement de C1 à C8, à la place de « À venir ».

**C8 — Hors du différentiel, mais à écrire avant le code (l. 320-323 ; v1 l. 184-185).** « M à composante de signe opposé
(deux) » : (a) pour **V4**, la composante est un mélange de poids λ avec une loi neuve ; son opposé (poids négatif) n'est
pas une loi de la grammaire du juge — objet non défini pour une cellule sur cinq ; (b) pour V1, V2, V3, V5, l'opposé est une
loi unique : « deux » cartes seraient identiques, ce que le texte ne dit pas vouloir. L'addendum ne pouvant rien changer
d'autre que des empreintes (l. 8-9), le codeur devrait inventer.
- nouveau (proposition, au choix de l'auteur) : « M à composante de signe opposé, à force × 1 et × 0,5 (deux) ; pour V4, où
  l'opposé n'est pas une loi, ces deux cartes sont deux fausses construites de plus (cosinus ≤ 0) ».
De même, sans que ce soit exigé : le nombre de cartes de chaque sorte parmi les 8 « membres exacts » et les 8 « autres
sortes » de la famille N (l. 330-332) n'est pas écrit (déjà vrai en v1).

## Constats par point de la commande

### (1) Différentiel exact

`diff` v1 → v2 : 38 blocs, 192 lignes retirées, 464 ajoutées (286 → 558 lignes). Je l'ai lu en entier. Chaque changement
de seuil, de critère, de bras, de famille, de métrique ou de liste d'arrêt se rattache à une ligne du tableau de tête ; les
changements sans ligne sont listés en C4 et C5. Parties **inchangées au mot près** (vérifié) : contexte et renvois de
l'hypothèse ; arrêts bas et haut, plafond, blocs ; bras F, F-arrêt ; Q2 (au mot « copies » près), Q4, Q7, Q8 ; zone utile ;
étages 2, 4, 5 ; garde N-058 ; nœud de Lazar (complété).

### (2) Les 3 majeurs et les 14 mineurs de [CL]

| remarque | état | où (v2) | note |
|---|---|---|---|
| M1 oracle | **fermée** | l. 230-236, 240-243, 320-325, 380, 422 | va au-delà du « nouveau » de [CL] : porteuse sans gain exclue de la couverture, déclaré « ajout de ma part » (l. 68) |
| M2 exclusivité, « non jugeable », Q1 | **fermée pour la principale** | l. 263-266, 397, 204 | reste C1 (étage 4) et C2 (lectures par monde) |
| M3 lectures de validité | **fermée** | l. 244-248, 261-262, 327-329, 353-354, 372-373, 396, 419 | réserve R-a ci-dessous |
| m1 placebo, P′ | fermée | l. 347-350, 268 | |
| m2 « au plus B » | fermée | l. 224-226, 100 | |
| m3 positions, clés | fermée | l. 344, 361-363, 311 | « g mod 10 » au lieu du « g mod 8 » de [CL] : suite de V5, cohérent |
| m4 doses haute et basse | fermée | l. 199-200, 206 | cinq cellules au lieu de quatre : suite de V5 |
| m5 hypothèse (ii) | fermée | l. 105-109 | fait vérifié sur `faits-v1.md`, l. 34 : « onze cartes promues et retenues » |
| m6 témoin à 1,25 | fermée | l. 351-352 | |
| m7 différences de montage | fermée | l. 435-440, 373-374 | « et plantées » ajouté à « cartes jugées » : non vérifié par moi au-delà de `cycle.py`, l. 625 |
| m8 essai E1 | fermée | l. 377-379, 415 | |
| m9 portée | fermée | l. 178-182, 143-144 | |
| m10 « Ce que cela règle » | fermée | l. 160-169, 443-445 | signalement à Lazar écrit deux fois |
| m11 issues contraires, « tout négatif » | fermée | l. 214-220, 403-408 | |
| m12 empreintes entières | fermée | l. 10-52, 551-557 | 32 empreintes entières recalculées sur disque, toutes égales ; exception déclarée (pièce d'une autre branche) |
| m13 titre de la règle e-BH | fermée | l. 185-186 | |
| m14 lieu, zone utile | **acceptée en partie, justifiée** | l. 57-60, 269-271 | la version qui fait foi ira sous `prereg/` (ce que [CL] demandait) ; « en partie » ne tient qu'à la copie de travail gardée sous `docs/notes/` ; confirmé par R-2881 (C6) |

### (3) Ligne V5 et mineurs repris du 1.1

- **V5** (l. 303, 305-306, 310-313, annexe A) : conforme au « nouveau » de [CL-1.1] M1 et à R-2875 (trois doses au banc ;
  les deux plus basses pour l'idée 1.2, comme les autres types ; dix cellules, 750 générations). La « lecture par strate » de
  R-2875 concerne la métrique du 1.1, pas ce texte.
- **m1** (gel avant les issues fraîches) : l. 278, 361-363, 372, 416 — porté, avec garde, mutation et ligne d'arrêt.
- **m2** (|s| ≥ 0,3) : l. 285 — porté ; Q5 et V3 restent tirables (signe opposé à la coupure).

### (4) Chiffres neufs, recalculés

| chiffre de la v2 | recalcul | accord |
|---|---|---|
| tenue ≤ 13 sur 500 au niveau 0,05/7 (l. 204, 259) | P(X ≤ 13) = 0,00551 ≤ 0,00714 < P(X ≤ 14) = 0,01081 | oui |
| non tenue ≥ 39 sur 500 (l. 260) | P(X ≥ 39) = 0,00461 ≤ 0,00714 < P(X ≥ 38) = 0,00766 | oui |
| à 5 bras : ≤ 13, ≥ 38, non jugeable 14 à 37 (annexe B ; [CL] M2) | identique | oui |
| doses de V5 : 2,2 ; 9,3 ; 20,0 nats sur 200 (l. 305) | rejeu à l'octet du script de l'annexe A : sortie égale ; programme à moi, autre graine, coupure tirée à la lettre du banc : 2,3 ; 9,1 ; 20,2 | oui (écart d'échantillon) |
| V2 : 2,1 ; 8,8 ; 20,2 (l. 305-306) | lu dans [BANC-v1], annexe A ; à moi : 2,3 ; 9,1 ; 19,9 | oui |
| 10 cellules ; 750 + 500 = 1 250 générations (l. 311, 313, 381) | 5 × 2 ; 75 × 10 + 500 | oui |
| 30 000 évaluations ; 1,0 à 1,7 heure (l. 427-428) | 1 250 × 24 ; 1,00 et 1,67 h à 0,12 et 0,20 s | oui |
| B = 4 800 ; F125 6 000 ; 32 instants ; log 480 ≈ 6,17 ; log(22/0,05) ≈ 6,087 | 4 800 (192 blocs, 8 tours complets) ; 6 000 ; 32 ; 6,1738 ; 6,0868 | oui |
| annexes A et B : empreintes des scripts et des sorties | recalculées sur les blocs recopiés dans le texte : égales aux quatre empreintes citées ; fichiers du bloc-notes égaux aussi | oui |
| oracle « une demi-heure au plus » (l. 429-430) | **non recalculable** sans jouer le code de la copie ; ordre de grandeur plausible | réserve R-c |
| clés de graines (l. 360-364) | 666 clés essayées, 666 états distincts : aucune collision entre clés à trois et à quatre éléments | oui |

Pour mémoire (non exigé) : si la vraie part valait 0,02 dans un bras, il serait « tenu » avec probabilité 0,87 ; à 0,01,
0,9994. La confiance 0,85 de Q1 suppose donc des parts nettement sous 0,02, ce que l'essai jouet de [CL] appuie (≤ 0,0044).

### (5) Exclusivité et couverture des critères gelés

- Ordre des étages : 1 arrête tout ; 1 bis pose une réserve et laisse lire ; 2 remplace la principale ; 3 ; 4 ; 5. Un bras
  « non tenu » et un autre « non jugeable » : l'étage 1 l'emporte. Aucun bras « non jugeable » ni « non tenu » : validité
  tenue (implicite, suffisant).
- Lecture (1) : trois issues par bras, exhaustives (0 à 13 ; 14 à 38 ; 39 à 500). **« non jugeable » → « validité non
  établie », écrit**, avec « aucune adoption ne peut s'en réclamer ».
- Principale : quatre issues lues dans l'ordre, « sinon » final : **exclusives et exhaustives**. Cas limites passés à la
  main : intervalle de C_A − C_F tout entier dans ]0 ; 0,02[ → « pas de gain » ; gain net de couverture avec borne haute de
  FP_A − FP_F > 0,05 et borne basse ≤ 0,02 → « non tranché » ; A égal à F → « pas de gain » et audit « tout négatif ».
- **Défauts** : C1 (étage 4), C2 (lectures par monde).
- Lectures (2) et (3) sans correction de multiplicité (l. 389) : déclaré ; le risque est une fausse alerte, du côté prudent.

### (6) Oracle des fausses promotions

Défini sans dépendre des résultats du banc : 20 000 instances et issues d'une graine propre `(famille, g, 2000)`, distincte
des flux jugés ; loi du monde connue ; calculé et scellé **avant** le rejeu (étape 3, l. 380) ; « oracle calculé après le
rejeu » invalide le run (l. 422) ; mutation « oracle calculé sur les issues jugées » (l. 374). Le retirage des fausses par
le cosinus n'emploie que les **instances** de l'oracle, aucune issue. Deux remarques sans effet sur le verdict : le gain est
une estimation sur échantillon (ajustement du nul et score sur les mêmes 20 000 issues, marge de certificat comprise : biais
de l'ordre de 10⁻⁴ nat, du côté « fausse ») ; le seuil est exactement 0 — les cartes à gain presque nul changent de classe
sur du bruit, elles sont comptées et rapportées à part.

### (7) Revendication et adoption

Aucune revendication (l. 114-115, 558). **Adoption = nœud de Lazar, écrit** (l. 441-445), avec le signalement de la
condition « dénominateur fixe » levée par preuve contre-lue (R-2878) ; « validité non établie » interdit de s'en réclamer
(l. 397). Processeur seul, toute dépense interdite (l. 423). Garde N-058 gardée (l. 446-448).

### Validateur

`controle_ia.prereg.problemes` sur la v2 (`PYTHONPATH=src`) rend **`[]`** (aucun défaut). Sections vues : Différentiel ;
Hypothèse ; Garantie ; Prédiction chiffrée et signe attendu ; Métrique ; Seuil ; Plan d'analyse ; Critères de lecture gelés ;
Liste d'arrêt ; Coût ; Écarts ; Contre-lecture ; Annexes A et B ; Citations obligatoires.

## Réserves (non bloquantes)

- **R-a — Ce que les quatre lectures voient vraiment.** La mutation « valeur e au maximum » doit être tuée par la lecture (3)
  (l. 372-373). Dans l'essai jouet de [CL], cette moyenne vaut 2,618 ± 0,225 sur 20 000 générations ; ramené à 500
  générations, l'intervalle s'élargit d'un facteur √40 ≈ 6,3, soit ± 1,4 : la borne basse (≈ 1,2) passe 1 de peu, et la loi est
  à queue lourde. La mutation peut donc **survivre** sur 500 générations ; la liste d'arrêt répond alors « pas de jeu »
  (l. 414) : échec du côté sûr, mais prévisible. À écrire : sur quel jeu d'essai la mise à mort est établie (par exemple
  20 000 générations d'un monde d'essai). Quant à la **fuite d'instants non révélés**, aucune des quatre lectures ne la voit
  sur W (dans [CL], 1,267 est lu sur le rapport exact, non sur W) : seule la garde d'accès du code et sa mutation en
  protègent — ce que [CL] disait déjà ; le titre de la ligne M3 du tableau ne doit pas laisser croire davantage.
- **R-b — Zone utile.** La couverture compte « au moins une porteuse », dont M à force × 1,5 : à la dose haute, 1,2 pour V2,
  V3, V5, soit environ 20 nats sur 200 tirages. C_F peut approcher 0,95 dans ces cellules ; le critère porte sur la couverture
  réunie. Risque déclaré et accepté (l. 269-271) ; rien à changer.
- **R-c — Oracle à 20 000 issues.** Que les routines d'ajustement du juge acceptent un instant de 20 000, et en combien de
  temps, n'est pas vérifié (je n'ai rien joué de la copie). L'essai du code le dira avant le jeu ; la borne de 24 heures couvre.
- **R-d — P « consomme au moins autant que A »** (l. 349) : vrai sauf le cas où toutes les cartes de P finissent arrêtées
  haut ou au plafond avant l'épuisement du budget ; la consommation réelle est rapportée, cela suffit.

## Ce que je n'ai pas fait

Je n'ai pas relu la preuve ([PREUVE]) ni refait la démonstration du théorème 2 ([CL] l'a fait) ; je n'ai pas rejoué l'essai à
20 000 générations de [CL] ; je n'ai exécuté aucun code du juge ; les citations des PDF voisins n'ont pas été relues (faites
par [CL], m13). Les fréquences de R-a sont un calcul d'échelle sur les chiffres de [CL], non une mesure.

## Annexe — programme de recalcul et sortie, recopiés en entier

Lancé par `.venv/bin/python -I recalcul_verification_v1.py docs/notes/organisme-idees-juge-v1/prereg-tirages-repartis-arret-anticipe-v2.md`
(numpy 2.4.6 ; la section 4 du programme exécute les deux scripts **recopiés dans le texte de la v2**, qui emploient scipy 1.17.1).

```python
"""Vérification courte du préenregistrement 1.2 v2 : recalcul indépendant des chiffres neufs (processeur seul ; aucun juge,
aucun nul, aucune issue jugée, aucun code des dossiers de copie). Usage : python recalcul_verification_v1.py CHEMIN_V2"""
import hashlib, io, contextlib, math, re, sys
from fractions import Fraction
import numpy as np

# --- 1. Seuils de validité : binomiale exacte en fractions (sans scipy) -------------------------------------------------
def loi_binomiale(n, p):
    p = Fraction(p)
    return [Fraction(math.comb(n, k)) * p**k * (1 - p)**(n - k) for k in range(n + 1)]

def seuils(n, bras, taux=Fraction(1, 20), alpha=Fraction(1, 20)):
    pmf = loi_binomiale(n, taux)
    cdf = [sum(pmf[:k + 1]) for k in range(n + 1)]          # P(X <= k)
    sf = [1 - (cdf[k - 1] if k else 0) for k in range(n + 1)]  # P(X >= k)
    niveau = alpha / bras
    kt = max(k for k in range(n + 1) if cdf[k] <= niveau)
    knt = min(k for k in range(n + 1) if sf[k] <= niveau)
    return niveau, kt, knt, cdf, sf

print("== 1. seuils de la validité, lecture (1) ==")
for n, bras in ((500, 5), (500, 7), (250, 7), (250, 14)):
    niveau, kt, knt, cdf, sf = seuils(n, bras)
    print(f"n={n} bras={bras} niveau={float(niveau):.5f} : tenue si <= {kt} (P(X<={kt})={float(cdf[kt]):.5f} ; P(X<={kt+1})={float(cdf[kt+1]):.5f}) ; "
          f"non tenue si >= {knt} (P(X>={knt})={float(sf[knt]):.5f} ; P(X>={knt-1})={float(sf[knt-1]):.5f}) ; non jugeable {kt+1} à {knt-1}")
print("parts : 13/500 =", 13 / 500, "; 14/500 =", 14 / 500, "; 38/500 =", 38 / 500, "; 39/500 =", 39 / 500, "; Q1 v1 : 0,02 x 500 =", 0.02 * 500)
for p in ("0.005", "0.01", "0.02", "0.03"):
    c = float(sum(loi_binomiale(500, Fraction(p))[:14]))
    print(f"si la vraie part vaut {p} : P(un bras « tenu ») = {c:.4f} ; sept bras indépendants tous tenus = {c**7:.4f}")

# --- 2. Comptes simples ------------------------------------------------------------------------------------------------
print("== 2. comptes ==")
cellules = 5 * 2
gT, gN = 75 * cellules, 500
print("cellules", cellules, "; générations T", gT, "; N", gN, "(2 x 250) ; total", gT + gN, "; v1 :", 75 * 8, "+ 500 =", 75 * 8 + 500)
ev = (gT + gN) * 24
print("évaluations", ev, "; heures d'un cœur à 0,12 s et 0,20 s :", round(ev * 0.12 / 3600, 2), round(ev * 0.20 / 3600, 2))
print("budget B", 24 * 200, "; blocs", 24 * 200 // 25, "= tours complets", 24 * 200 // 25 // 24, "; F125", 24 * 250, "; rapport", 250 / 200,
      "; 240 multiple de 25 ?", 240 % 25 == 0, "; instants à 800 :", 800 // 25, "; à 200 :", 200 // 25)
print("log(m/alpha)=log 480 =", round(math.log(480), 4), "; log(22/0,05) =", round(math.log(22 / 0.05), 4), "; log(1/20) =", round(math.log(1 / 20), 4))
print("bras G : 2 blocs x 24 =", 48, "blocs, restent", 192 - 48, "; une carte seule peut monter à", min(800, 50 + (192 - 48) * 25), "tirages (plafond 800)")
print("générations de la famille N par cellule et par monde si M0 = g < 250 :", sorted({(g % 10, g < 250) for g in range(500)}).__len__(), "couples, effectif",
      {sum(1 for g in range(500) if g % 10 == c and g < 250) for c in range(10)})
print("si M0 = g pair : cellules vues par M0 :", sorted({g % 10 for g in range(500) if g % 2 == 0}), "(monde et cellule confondus)")

# --- 3. Doses de V5 : programme à moi, banc B v2 à la lettre (s_A ~ U[-1 ; 1] au centième, retiré tant que |s| < 0,3) ---
print("== 3. doses de V5 (et V2 pour comparaison), 600 mondes, 6 000 instances, autre graine ==")
K, D = 3, 2
def softmax_alea(rng):
    return np.round(rng.normal(0, 1.5, (K, D)), 6), np.round(rng.normal(0, 0.3, K), 6)
def proba(W, b, z):
    s = z @ W.T + b
    s = s - s.max(axis=1, keepdims=True)
    e = np.exp(s)
    return e / e.sum(axis=1, keepdims=True)
def information(ligne, dose, graine, mondes=600, n=6000):
    v = []
    for ss in np.random.SeedSequence(graine).spawn(mondes):
        rng = np.random.default_rng(ss)
        W1, b1 = softmax_alea(rng)
        z = np.round(rng.normal(size=(n, D)), 6)
        if ligne == "V5":
            j = int(rng.integers(0, 2))
            while True:
                seuil = round(float(rng.uniform(-1, 1)), 2)
                if abs(seuil) >= 0.3:
                    break
        else:
            j, seuil = int(rng.integers(0, 2)), 0.0
        u = rng.normal(size=K); u -= u.mean(); u /= np.linalg.norm(u)
        E = np.zeros((K, D)); E[:, 1 - j] = u
        haut = (z[:, j] > seuil)[:, None]
        pm = np.where(haut, proba(W1 + dose * E, b1, z), proba(W1 - dose * E, b1, z))
        p1 = proba(W1, b1, z)
        v.append(float(np.mean(np.sum(pm * (np.log(pm) - np.log(p1)), axis=1))))
    return np.median(v), np.quantile(v, 0.25), np.quantile(v, 0.75)
for ligne in ("V5", "V2"):
    for dose in (0.4, 0.8, 1.2):
        m, q1, q3 = information(ligne, dose, 715517)
        print(f"{ligne} dose {dose:.2f} : médiane {m:.4f} nat/épisode [{q1:.4f} ; {q3:.4f}] ; sur 200 épisodes {200 * m:.1f} nat ; épisodes pour log 480 : {math.log(480) / m:.0f}")

# --- 4. Rejeu à l'octet des deux scripts recopiés dans le texte (annexes A et B) ---------------------------------------
print("== 4. rejeu des annexes du texte ==")
texte = open(sys.argv[1], encoding="utf-8").read()
print("empreinte du texte lu :", hashlib.sha256(texte.encode("utf-8")).hexdigest())
for nom in ("Annexe A", "Annexe B"):
    corps = texte.split("## " + nom, 1)[1].split("\n## ", 1)[0]
    blocs = re.findall(r"```(python)?\n(.*?)```", corps, flags=re.S)
    sortie_ecrite = next(b for lang, b in blocs if not lang)
    code = next(b for lang, b in blocs if lang)
    cites = re.findall(r"`([0-9a-f]{64})`", corps)
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        exec(compile(code, nom, "exec"), {"__name__": "rejeu"})
    print(nom, ": empreinte du code recopié", hashlib.sha256(code.encode()).hexdigest() == cites[0], "; de la sortie recopiée",
          hashlib.sha256(sortie_ecrite.encode()).hexdigest() == cites[1], "; sortie rejouée égale à la sortie écrite :", tampon.getvalue() == sortie_ecrite)

# --- 5. Clés de graines : aucune collision entre les flux nommés au texte ------------------------------------------------
print("== 5. clés de graines ==")
racine = int(hashlib.sha256(texte.encode("utf-8")).hexdigest(), 16)
cles = []
for fam in (0, 1):
    for g in (0, 1, 24, 25):
        cles += [(fam, g, 24), (fam, g, 25), (fam, g, 1000), (fam, g, 1001), (fam, g, 2000)]
        for i in range(24):
            cles += [(fam, g, i, 0), (fam, g, i, 1), (fam, g, i, 2)]
cles += [(99, b) for b in range(50)]
etats = {c: tuple(np.random.SeedSequence(entropy=racine, spawn_key=c).generate_state(4)) for c in cles}
print(len(cles), "clés,", len(set(cles)), "distinctes,", len(set(etats.values())), "états distincts")
```

```
== 1. seuils de la validité, lecture (1) ==
n=500 bras=5 niveau=0.01000 : tenue si <= 13 (P(X<=13)=0.00551 ; P(X<=14)=0.01081) ; non tenue si >= 38 (P(X>=38)=0.00766 ; P(X>=37)=0.01242) ; non jugeable 14 à 37
n=500 bras=7 niveau=0.00714 : tenue si <= 13 (P(X<=13)=0.00551 ; P(X<=14)=0.01081) ; non tenue si >= 39 (P(X>=39)=0.00461 ; P(X>=38)=0.00766) ; non jugeable 14 à 38
n=250 bras=7 niveau=0.00714 : tenue si <= 4 (P(X<=4)=0.00457 ; P(X<=5)=0.01309) ; non tenue si >= 23 (P(X>=23)=0.00389 ; P(X>=22)=0.00777) ; non jugeable 5 à 22
n=250 bras=14 niveau=0.00357 : tenue si <= 3 (P(X<=3)=0.00128 ; P(X<=4)=0.00457) ; non tenue si >= 24 (P(X>=24)=0.00187 ; P(X>=23)=0.00389) ; non jugeable 4 à 23
parts : 13/500 = 0.026 ; 14/500 = 0.028 ; 38/500 = 0.076 ; 39/500 = 0.078 ; Q1 v1 : 0,02 x 500 = 10.0
si la vraie part vaut 0.005 : P(un bras « tenu ») = 1.0000 ; sept bras indépendants tous tenus = 1.0000
si la vraie part vaut 0.01 : P(un bras « tenu ») = 0.9994 ; sept bras indépendants tous tenus = 0.9955
si la vraie part vaut 0.02 : P(un bras « tenu ») = 0.8667 ; sept bras indépendants tous tenus = 0.3673
si la vraie part vaut 0.03 : P(un bras « tenu ») = 0.3603 ; sept bras indépendants tous tenus = 0.0008
== 2. comptes ==
cellules 10 ; générations T 750 ; N 500 (2 x 250) ; total 1250 ; v1 : 600 + 500 = 1100
évaluations 30000 ; heures d'un cœur à 0,12 s et 0,20 s : 1.0 1.67
budget B 4800 ; blocs 192 = tours complets 8 ; F125 6000 ; rapport 1.25 ; 240 multiple de 25 ? False ; instants à 800 : 32 ; à 200 : 8
log(m/alpha)=log 480 = 6.1738 ; log(22/0,05) = 6.0868 ; log(1/20) = -2.9957
bras G : 2 blocs x 24 = 48 blocs, restent 144 ; une carte seule peut monter à 800 tirages (plafond 800)
générations de la famille N par cellule et par monde si M0 = g < 250 : 20 couples, effectif {25}
si M0 = g pair : cellules vues par M0 : [0, 2, 4, 6, 8] (monde et cellule confondus)
== 3. doses de V5 (et V2 pour comparaison), 600 mondes, 6 000 instances, autre graine ==
V5 dose 0.40 : médiane 0.0116 nat/épisode [0.0084 ; 0.0151] ; sur 200 épisodes 2.3 nat ; épisodes pour log 480 : 533
V5 dose 0.80 : médiane 0.0453 nat/épisode [0.0337 ; 0.0585] ; sur 200 épisodes 9.1 nat ; épisodes pour log 480 : 136
V5 dose 1.20 : médiane 0.1009 nat/épisode [0.0732 ; 0.1287] ; sur 200 épisodes 20.2 nat ; épisodes pour log 480 : 61
V2 dose 0.40 : médiane 0.0114 nat/épisode [0.0078 ; 0.0150] ; sur 200 épisodes 2.3 nat ; épisodes pour log 480 : 539
V2 dose 0.80 : médiane 0.0456 nat/épisode [0.0309 ; 0.0587] ; sur 200 épisodes 9.1 nat ; épisodes pour log 480 : 135
V2 dose 1.20 : médiane 0.0997 nat/épisode [0.0705 ; 0.1301] ; sur 200 épisodes 19.9 nat ; épisodes pour log 480 : 62
== 4. rejeu des annexes du texte ==
empreinte du texte lu : c7f80e8c9fff5128ca60a1071b70519844a2f9ccdd9344f0ece0aab0e3e13c2b
Annexe A : empreinte du code recopié True ; de la sortie recopiée True ; sortie rejouée égale à la sortie écrite : True
Annexe B : empreinte du code recopié True ; de la sortie recopiée True ; sortie rejouée égale à la sortie écrite : True
== 5. clés de graines ==
666 clés, 666 distinctes, 666 états distincts
```
