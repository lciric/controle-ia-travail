# Organismes discrets, bras A (déplacement des contrôles appris sans consigne) — devis de la carte des deux moniteurs à modèle de langue — v1, sur le texte v2

> **Écart déclaré à la règle « Fable conçoit ».** C'est une pièce décisive (devis), que la règle « Économie de Fable » donne à Claude Fable 5.2 en effort maximal. Elle est rédigée par **Claude Opus 5.5, en effort maximal**, rédacteur des devis de carte v3 et v4, Fable étant épuisé jusqu'au 29 novembre 2026 (mot de la session mère : « Opus à la place de Fable, GO-2026-11-22-145 » ; ligne non lue au registre, cloisonnement).

## Suppositions du côté habilité, à confirmer ou corriger par le lecteur habilité, sans interne

Aucune donnée n'est prise dans une pièce du côté habilité. Ce qui n'existe que là est supposé, ici, en tête ; les réponses du lecteur habilité, transmises par la session mère le 2026-11-22 vers 22:33Z, sont citées pour ce qu'elles disent.

| | supposition | valeur retenue | fondement | réponse du lecteur habilité |
|---|---|---|---|---|
| S1 | temps d'une lecture du moniteur boîte noire par action, en lots de 8 sur une A100 80 Go, raisonnement de 400 jetons au plus | **4,02 à 4,28 s** ; borne haute écrite **8,56 s** (le double, règle du pire cas) | le temps d'une action de l'agent, 40,2 à 42,8 s par épisode de dix actions en lots de 8 (devis v2, lignes 42 et 43, autre chaîne) : même modèle, à la même révision, aux mêmes réglages de génération (6.10, lignes 922 et 925 ; configuration de référence, lignes 103 et 105) | (1) « aucun débit n'est mesuré » ; hypothèse centrale « acceptable », avec une borne haute écrite |
| S2 | temps d'une lecture du juge d'une autre lignée, ses 102 points de lecture compris | **4,58 à 4,85 s** ; borne haute écrite **9,70 s** | le temps de S1, plus une passe sur le contexte refaite une fois par action, comptée **0,45 s** (la passe unique mesurée sur une transcription entière, plus longue qu'un contexte d'action : devis v2, ligne 45, autre chaîne), plus onze passes courtes qui reprennent ce contexte, comptées au plus un pas chacune contre 400 pas de génération (+ 2,75 %) | (2) « une passe sur le contexte puis onze passes courtes qui le reprennent » ; la passe sur le contexte « est refaite une fois par action après la génération » ; « le facteur dix ne s'applique pas » |
| S3 | durée de la lecture commune des cinq moniteurs sur la machine louée | **0,1 à 1,0 h** ; borne 1,0 h | « quelques minutes à moins d'une heure » | (3) elle tourne sur la machine louée, dans la même exécution ; durée à la taille réelle non mesurée |
| S4 | score du moniteur boîte noire (cas A, chaque valeur de 0 à 100 en un jeton) | lu au fil de la génération, **sans passe de plus** | ma lecture de 6.10, lignes 927 et 928 | — (non posée ; à confirmer) |
| S5 | mise en route de l'instance, chargement des deux modèles et passage de l'un à l'autre compris | **1,0 h** | devis v2, ligne 56 (supposée elle aussi) | — (à confirmer) |
| S6 | poids des deux modèles en `bfloat16` | **≈ 16 et ≈ 15 Go** | leurs noms (8 et 7 milliards de paramètres) et leur précision (6.10, ligne 926) : sous les 40 Go de téléchargement prévus (configuration de référence, ligne 116) | (4) les deux modèles se suivent, « la carte libérée entre les deux » : ils ne cohabitent pas en mémoire |

**Établi par la réponse (4), non supposé** : une seule instance et une seule exécution ; les deux modèles se suivent ; « une relance après panne reprend sur la même instance sans refaire ce qui est scellé ».

- **Demande** : message de la session du bras A (`session_013QMayn5HfnqnuvfPbwUUQf`), 2026-11-22 vers 22:24Z ; confirmée par la session mère (`session_013QMayjbmQUdDuDs2S3i3XD`), 2026-11-22 vers 22:28Z : « Le devis de la carte des deux moniteurs, depuis le texte et les prix déjà cités. Toute donnée du côté habilité y est marquée « supposée », et la liste exacte de ces suppositions va en tête ». Même cloisonnement que le mandat du devis de carte (`97165ddf…`). Aucune dépense.
- **Date (UTC)** : écrit le 2026-11-22T22:40:07Z (`date -u`).
- **Commit du dépôt lu** : `643d4817` (branche `relance-bras-a/devis-carte-v3`).
- **Objet** : chiffrer la carte louée sur laquelle les deux moniteurs à modèle de langue lisent les actions à l'étape de discrétion (6.3 (m)) : le moniteur boîte noire par action et le juge d'une autre lignée, au plus 6 400 lectures avec raisonnement chacun. Le devis de carte v3, puis v4, en donnait un ordre de grandeur (décision 3) ; ce devis le remplace.
- **Texte chiffré** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon55.md`, `cc55502ad4ef0fa1de5f8f4444975fec2eb7f3f77db8913c96f1bdf9225facb1` ; numéros de ligne du brouillon 55.
- **Statut** : version 1, non contre-lue. Elle propose deux lignes de GO (décision 1) et laisse à Lazar le moment de les accorder (décision 2). Aucune ne peut servir avant la garde de production : ligne de la table B et issue de la base inscrites (8.4, ligne 1155 ; 13.2, ligne 1499).
- **Marques** : **M**, mesuré ou relevé, ou nombre lu tel quel dans la pièce citée ; **C**, calculé ici (programme en section 9) ; **S**, supposé (S1 à S6 ci-dessus).
- **Sceau** : empreinte compagnon `devis-carte-moniteurs-bras-a-v1.md.sha256`, écrite par `controle_ia.scellement sceller`.

## 0. En une page

1. **Ce qui tourne.** À l'étape de discrétion, sur une carte louée, dans une seule exécution : le moniteur boîte noire par action (`meta-llama/Llama-3.1-8B-Instruct`, le modèle de l'agent à sa révision), puis le juge d'une autre lignée (`Qwen/Qwen2.5-7B-Instruct`), chacun au plus 6 400 lectures avec raisonnement (400 jetons générés au plus, lots de 8 : 6.10, lignes 918 à 926) ; puis les ouvertures et la lecture commune des cinq moniteurs, sur la même machine.
2. **≈ 16,4 à 18,2 h de carte, ≈ 20,4 à 25,7 USD attendus** (C), lecture commune comprise.
3. **Deux lignes de GO proposées, une par lecture de moniteur** (13.2, ligne 1493), sur une seule instance : le moniteur boîte noire, plafond de repli **55 USD** ; le juge, avec les ouvertures et la lecture commune, **60 USD** ; ensemble **115 USD** (C).
4. **Plafonds recalculés à l'étape (m)** : ≈ 28 + 31 = **59 USD** si le débit des deux moniteurs est mesuré d'ici là et égal aux hypothèses hautes ; sinon, sur le seul débit de l'agent, doublé, ≈ 47 à 51 + 52 à 57 USD, **99 à 108 USD** : 6 à 14 % sous le repli (C).
5. **Les 102 points du juge** ne multiplient pas son temps par dix (réponse 2) : une passe de contexte de plus par action, ≈ 13 % (C). **Le point fragile est ailleurs** : aucun débit des moniteurs n'est mesuré (réponse 1), si bien que les plafonds restent près du repli tant qu'aucune mesure n'existe.
6. **Effet sur la décision 3 du devis de carte v4** : une fois contre-lu, ce devis remplit la part « moniteurs » de la case « devis » de 13.2 ; sous la lettre de 13.2, le départ de la ligne 1 ne l'attend plus que jusqu'à sa contre-lecture.
7. **Deux décisions pour Lazar** (section 7) : la structure des lignes de GO (dépense, sans défaut) ; le moment de les accorder.

## 1. Pièces lues, avec empreintes

| pièce | empreinte | ce qui en est lu |
|---|---|---|
| texte v2, brouillon 55 | `cc55502ad4ef0fa1de5f8f4444975fec2eb7f3f77db8913c96f1bdf9225facb1` | 6.2, ligne 735 (clés des deux moniteurs) ; 6.3 (m), ligne 766 ; 6.10, lignes 918 à 930 ; 6.11, lignes 959 et 960 ; 8.2, ligne 1091 ; 8.4, lignes 1154, 1155, 1164, 1196, 1198, 1199 ; 13.2, lignes 1489 à 1500 |
| devis de carte v2 | `83240ca61d7c300fc9f4ca802560a6010a2a7c2eb48dd58fe2c214ee03524ecd` | lignes 42, 43, 45, 51, 56, 69, 80 à 82, 96 à 101 |
| devis de carte v4 (même rédacteur) | `f82514e9326df61f2fbd73f3eab644107f910aae620afe70b3d6ef9fcde7e0f3` | sections 3.3 et 5.2 (règles de calcul) ; décision 3 |
| configuration de référence, `prereg/T0.6-organismes-config-7b-v1.json` | `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` | lignes 41, 103, 105, 115 à 117 |
| `registres/depenses.md` (registre vivant) | — | ligne 515 (dernier relevé de prix cité par le devis v2) |
| messages de la session mère, 2026-11-22 vers 22:28Z et 22:33Z | — | entiers (confirmation ; réponses du lecteur habilité) |

Aucune pièce du côté habilité n'est ouverte.

## 2. Ce que le texte fait lire aux deux moniteurs, et où

| | moniteur boîte noire par action | juge d'une autre lignée |
|---|---|---|
| modèle (6.10, ligne 922) | `meta-llama/Llama-3.1-8B-Instruct`, à la révision de l'agent | `Qwen/Qwen2.5-7B-Instruct`, révision figée |
| lectures (M) | cinq conditions × 1 280 = 6 400 au plus (6.11, ligne 960) | toutes les actions des cinq conditions, 6 400 au plus (6.10, ligne 918) |
| mode et réglages (lignes 924 et 925) | avec raisonnement ; 400 jetons générés au plus ; température 1,0 ; balise absente imposée ; lots de 8 | les mêmes |
| chargement (ligne 926) | `bfloat16`, noyau `sdpa` | les mêmes |
| lecture du score (lignes 927 et 928) | cas A : chaque valeur de 0 à 100 en un jeton | cas B : chiffre par chiffre, fin « non-chiffre » ; « 102 points de lecture par action » (13.2, ligne 1490 ; 6.11, ligne 960) |
| graine (6.2, ligne 735) | une par lecture, la même à la même position dans les cinq conditions | la même règle |

- **Actions non appliquées** (illisibles, ou révision d'une proposition absente) : non lues (ligne 930) ; 6 400 est un majorant.
- **Quand** : à l'étape (m) (6.3, ligne 766), après la lecture décisive et l'analyse ; la base « mots et coût » d'abord ; la production des scores n'est demandée qu'après la ligne de la table B et l'issue de la base (8.4, ligne 1155 ; garde de production du lanceur, 13.2, ligne 1499). L'instance de la seconde ligne de carte est détruite bien avant (8.5) : l'étape a sa propre instance.
- **Comment** : trois sous-commandes, « l'extraction pour la base, la base, l'étape de discrétion ; la session principale verse entre elles » ; l'étape de discrétion se joue en une seule exécution, « production, ouvertures et lecture commune, sans rendre la main entre les trois » (13.2, ligne 1499). La carte ne sert qu'à l'étape de discrétion ; une seule instance, les deux modèles l'un après l'autre, la lecture commune sur la même machine (réponses 3 et 4).
- **Hors de ce devis** : la base « mots et coût », le classifieur lexical, le classifieur de surface et l'agrégateur séquentiel tournent sur processeur (6.11, ligne 960), sauf la part de la lecture commune qui tourne sur la machine louée (S3).

## 3. Débits, durées et prix

- **Débits et durées** : S1 à S6, en tête.
- **Prix** (M) : 1,1833 USD par heure relevé (registre des dépenses, ligne 515) ; borne 1,30 USD par heure, stockage ≤ 0,08 en plus, soit 1,38 au plus ; téléchargement ≤ 0,05 USD par Go, 40 Go prévus (configuration de référence, lignes 41, 115 à 117 ; règle du devis v2, ligne 69). Tarif à relever le jour de la création, pilote de l'hôte compris ; démarrer au-dessus du prix du devis est interdit (8.4, ligne 1164).
- **Carte** : la même que pour la course, A100 SXM4 80 Go ; une autre carte serait un relevé neuf et un nœud (devis v2, ligne 51).
- **Règles de calcul** : celles du devis de carte (v4, 3.3) — attendu (bas de fourchette à 1,1833, haut à 1,30, plus 1 à 2 USD de téléchargement par mise en route) ; pire cas (heures au haut × 4 × 1,38, plus 4 USD) ; plafond de repli arrondi aux 5 USD supérieurs ; plafond recalculé arrondi à l'unité (v4, 5.2).

## 4. Les deux lignes, en projection

**Ligne A — lecture du moniteur boîte noire par action** (l'instance est créée sous elle).

| poste | compte et formule | durée |
|---|---|---|
| mise en route (S5) | une fois | 1,0 h (S) |
| lectures | 6 400 au plus (M) × 4,02 à 4,28 s (S1) | 7,15 à 7,61 h (C) |
| **total** | | **8,15 à 8,61 h (C)** |

- **Attendu** : 8,15 h × 1,1833 + 1 = 10,6 USD à 8,61 h × 1,30 + 2 = 13,2 USD (C).
- **Pire cas** : 8,61 h × 4 × 1,38 + 4 = 51,52 USD ; **plafond de repli : 55 USD** (C).

**Ligne B — lecture du juge d'une autre lignée**, puis ouvertures et lecture commune (même instance, même exécution).

| poste | compte et formule | durée |
|---|---|---|
| lectures, 102 points compris | 6 400 au plus (M) × 4,58 à 4,85 s (S2) | 8,14 à 8,62 h (C) |
| ouvertures (cinq lignes au journal) | — | négligeable (S) |
| lecture commune des cinq moniteurs (S3) | une fois | 0,1 à 1,0 h (S) |
| **total** | | **8,24 à 9,62 h (C)** |

- **Attendu** : 8,24 h × 1,1833 = 9,8 USD à 9,62 h × 1,30 = 12,5 USD (C) ; pas de téléchargement de plus (compté à la ligne A).
- **Pire cas** : 9,62 h × 4 × 1,38 + 4 = 57,09 USD ; **plafond de repli : 60 USD** (C).

**Ensemble** : **≈ 16,4 à 18,2 h ; ≈ 20,4 à 25,7 USD attendus ; plafonds de repli 55 + 60 = 115 USD** (C). Le devis de carte v3 donnait ≈ 15 à 16 h et ≈ 19 à 23 USD : l'écart vient de la passe de contexte du juge et de la lecture commune.

**Plafonds recalculés à l'étape (m)** (règle du devis de carte, 5.2) :
- `PA = 2 × 1,38 × (max(1,0 ; m) + 6 400 × tA / 3 600) + 4` ; `PB = 2 × 1,38 × (6 400 × tB / 3 600 + L) + 4` ; arrondis à l'unité supérieure.
- `tA`, `tB` : secondes par lecture **mesurées**, prises telles quelles ; à défaut de mesure, `tA = 2 × d / 10` et `tB = 2 × (1,0275 × d / 10 + 0,45)`, où `d` est le temps par épisode de l'agent mesuré aux lignes 1 et 2 (S1 et S2 doublés) ; `m` : la mise en route mesurée aux lignes 1 et 2 ; `L` : la durée de la lecture commune, 1,0 h à défaut de mesure (S3).
- Exemples (C) : débits mesurés égaux aux hypothèses hautes, `L` = 1 h : 28 + 31 = **59 USD**. Sans mesure des moniteurs, `L` = 1 h : `d` = 40 s, 47 + 52 = 99 USD ; `d` = 42,8 s, 49 + 55 = **104 USD** ; `d` = 45 s, 51 + 57 = 108 USD.

**Arrêts** : plafond atteint, arrêt de la ligne, versement scellé, reprise par nœud (8.2, ligne 1091) ; scores scellés dès leur production (8.4, ligne 1155) ; une relance après panne reprend sur la même instance sans refaire ce qui est scellé (réponse 4) : la relance complète que garde la règle du pire cas est un majorant.

## 5. Ce que les réponses du lecteur habilité ont changé

| réponse (session mère, 22:33Z) | avant | après |
|---|---|---|
| (1) aucun débit mesuré | hypothèse 4,02 à 4,28 s, sans borne écrite | même hypothèse, borne haute écrite (S1, S2) ; les plafonds recalculés sans mesure restent à 6 à 14 % du repli |
| (2) une passe de contexte de plus par action, puis onze passes courtes | facteur 1,0 à 1,255 sur le juge, et un risque de facteur dix | + 0,45 s et + 2,75 % par lecture (S2) ; le risque de facteur dix est levé |
| (3) lecture commune sur la machine louée, de quelques minutes à moins d'une heure | durée inconnue, borne de 4 h choisie sans donnée | 0,1 à 1,0 h (S3) ; plafond du juge 60 USD au lieu de 80 |
| (4) une seule instance, une seule exécution, la carte libérée entre les deux | ma lecture | établi ; décision 1, option (a) |

## 6. Conditions à tenir avant chaque ligne — listées, non remplies

| condition | source | ligne A | ligne B |
|---|---|---|---|
| garde de production : ligne de la table B et issue de la base inscrites au registre | 8.4, ligne 1155 ; 13.2, ligne 1499 | oui | oui |
| ligne de GO de la lecture, plafond couvrant la ligne ; rien ne part avant la sienne | 13.2, ligne 1493 | la sienne | la sienne |
| tarif du jour de la carte, au plus le prix du devis, pilote de l'hôte relevé | 13.2, ligne 1489 ; 8.4, ligne 1164 | oui | — (même instance) |
| lanceur de l'étape de discrétion : la version que la contre-lecture habilitée rend conforme, chemin et empreinte à sa configuration scellée ; restes (b) et (c) de la case du module | 13.2, lignes 1499 et 1500 | oui | oui |
| table des identifiants opaques tirée de sa propre entropie, scellée à part, engagée ; écart à R9 accordé (GO-2026-11-19-97, cité par le texte) | 8.4, ligne 1154 ; 6.2 ; 13.2, ligne 1499 | oui | oui |
| consigne des deux moniteurs chargée par son empreinte ; message à marqueur exact | 8.4, lignes 1198 et 1199 | oui | oui |
| jetons de fin du moniteur boîte noire relevés au chargement et écrits à la configuration scellée | 6.10, ligne 926 | oui | — |
| configuration de l'analyse de la discrétion scellée avant la réception de la sortie de la lecture commune | 13.2, ligne 1491 | — | oui |
| journal des ouvertures : une ligne par moniteur avant sa lecture | 8.4, ligne 1196 | — | oui |
| ce devis contre-lu ; les suppositions S1 à S6 confirmées ou corrigées par le lecteur habilité | 13.2, ligne 1490 ; demande de la session mère | oui | oui |

## 7. Décisions pour Lazar

**Décision 1 — structure des lignes de GO de la carte des moniteurs.**
- **Décision** : deux lignes de GO, une par lecture de moniteur à modèle de langue, sur une seule instance : la ligne A (moniteur boîte noire, mise en route comprise ; l'instance est créée sous elle) et la ligne B (juge, ouvertures, lecture commune), que le lanceur exige avant la production des scores du juge.
- **Enjeu** : 13.2 veut une ligne de GO « par lecture de moniteur à modèle de langue » (ligne 1493) ; l'étape de discrétion est une seule exécution sur une seule instance (13.2, ligne 1499 ; réponse 4) ; la garde de calcul du dépôt lie une création d'instance à une ligne de GO.
- **Options** : (a) deux lignes, une instance — avantage : la lettre de 13.2 et l'exécution unique sont tenues ; inconvénient : la ligne B se vérifie dans le lanceur, en cours d'exécution, non à la création de l'instance. (b) une seule ligne pour toute l'étape (115 USD de repli) — avantage : la plus simple ; inconvénient : contraire à la lettre de 13.2 : écart, donc nœud. (c) deux instances en parallèle, une par moniteur — avantage : ≈ 9 à 11 h de mur au lieu de 16 à 18 (C : la ligne B, sur sa propre instance, prend une mise en route de plus) ; inconvénient : contraire à l'exécution unique (écart, nœud), et une mise en route de plus.
- **Recommandation** : (a), confiance moyenne à haute (la vérification de la ligne B par le lanceur est du côté habilité).
- **Défaut** : aucun (dépense).

**Décision 2 — moment où les deux lignes s'accordent.**
- **Décision** : accorder les deux lignes dès la contre-lecture de ce devis, aux plafonds de repli (55 et 60 USD), utilisables seulement après la garde de production ; un complément à l'étape (m) pourra les abaisser, jamais les relever, si un débit des moniteurs est mesuré d'ici là.
- **Enjeu** : aucun débit des moniteurs n'est mesuré (réponse 1) ; sans cette mesure, le complément de l'étape (m), sur le seul débit de l'agent doublé, ne gagnerait que 6 à 14 % sur le repli (99 à 108 USD contre 115, section 4), au prix d'un tour de GO au bout de la course.
- **Options** : (a) les deux lignes demandées à l'étape (m), par un complément d'une page écrit par la session principale — avantage : plafonds recalculés sur ce qui sera mesuré ; inconvénients : un tour de GO au bout de la course ; pièce décisive que la règle « Économie de Fable » donne à Fable : écart à déclarer, sauf si Fable est disponible (quota rétabli le 29 novembre 2026). (b) les deux lignes accordées dès la contre-lecture, aux plafonds de repli, abaissables à l'étape (m) — avantage : aucun tour de GO à la fin, pour un plafond à peine plus haut ; inconvénient : 115 USD de plafonds pour ≈ 20 à 26 attendus, accordés longtemps avant leur emploi.
- **Recommandation** : (b), confiance moyenne.
- **Défaut sous 48 heures** : (a) : l'option (b) accorde une dépense, qui n'a jamais de défaut.

## 8. Réserves

1. **Débits des moniteurs supposés** (S1, S2) : aucun n'est mesuré (réponse 1) ; l'hypothèse vient de l'agent, sur une autre chaîne.
2. **Passe de contexte du juge** (S2) : comptée au temps d'une passe sur une transcription entière, plus longue qu'un contexte d'action ; c'est un majorant probable, non une mesure.
3. **Lecture commune** (S3) : « quelques minutes à moins d'une heure », à la taille réelle non mesurée.
4. **Score du moniteur boîte noire** (S4) et **mise en route** (S5) : supposés, non posés au lecteur habilité.
5. **Poids des modèles** (S6) : d'après leurs noms et leur précision.
6. **Prix** : dernier relevé de mes pièces le 18 novembre (registre des dépenses, ligne 515) ; le tarif du jour se relève à la création.
7. **Rédacteur et contre-lecteur** : même modèle si le contre-lecteur est Opus 5.5 (écart déclaré en tête).
8. **Lignes de GO citées sans lecture du registre des GO** (cloisonnement) : GO-2026-11-22-145 (d'après la session mère) ; GO-2026-11-19-97 (d'après le texte, 6.2).

## 9. Calculs, par programme

Programme (Python 3, bibliothèque standard), joué tel quel le 2026-11-22 vers 22:40Z :

```python
# Calculs du devis de la carte des deux moniteurs à modèle de langue du bras A.
# Entrées : texte v2 brouillon 55 (6.10, 6.11, 13.2) ; devis v2 (débits de l'agent, prix) ; configuration de référence ;
# réponses du lecteur habilité transmises par la session mère (2026-11-22, 22:33Z), sans interne.
import math
h = lambda s: s / 3600
n = 6400                                # lectures par moniteur, au plus (texte, lignes 918 et 960)
t_b, t_h = 40.2 / 10, 42.8 / 10         # S1 : s par lecture du moniteur boîte noire = une action de l'agent en lots de 8 (devis v2, lignes 42-43)
passe = 0.45                            # S2 : passe de contexte refaite une fois par action (devis v2, ligne 45 : une passe sur texte imposé)
courtes = 11 / 400                      # S2 : onze passes courtes, chacune au plus un pas contre 400 pas de génération
tJ = lambda t: t * (1 + courtes) + passe   # s par lecture du juge
L_b, L_h = 0.1, 1.0                     # S3 : lecture commune sur la carte, « quelques minutes à moins d'une heure »
mer = 1.0                               # S5 : mise en route, les deux modèles (devis v2, ligne 56)
relu, borne, stock = 1.1833, 1.30, 0.08
pire = borne + stock
tel_b, tel_h = 1.0, 2.0
c5 = lambda x: 5 * math.ceil(x / 5)

print(f"s par lecture : boîte noire {t_b:.4f} à {t_h:.4f} (borne haute {2*t_h:.4f}) ; juge {tJ(t_b):.4f} à {tJ(t_h):.4f} (borne haute {2*tJ(t_h):.4f})")
# Ligne A : moniteur boîte noire, mise en route comprise
A_b, A_h = mer + h(n * t_b), mer + h(n * t_h)
EA_b, EA_h = A_b * relu + tel_b, A_h * borne + tel_h
PA = A_h * 4 * pire + 4
print(f"A : {A_b:.4f} à {A_h:.4f} h ; attendu {EA_b:.4f} à {EA_h:.4f} ; pire {PA:.4f} -> {c5(PA)}")
# Ligne B : juge (102 points), ouvertures, lecture commune
Bl_b, Bl_h = h(n * tJ(t_b)), h(n * tJ(t_h))
B_b, B_h = Bl_b + L_b, Bl_h + L_h
EB_b, EB_h = B_b * relu, B_h * borne
PB = B_h * 4 * pire + 4
print(f"B : lectures {Bl_b:.4f} à {Bl_h:.4f} h ; avec la lecture commune {B_b:.4f} à {B_h:.4f} h ; attendu {EB_b:.4f} à {EB_h:.4f} ; pire {PB:.4f} -> {c5(PB)}")
print(f"Ensemble : {A_b+B_b:.4f} à {A_h+B_h:.4f} h ; attendu {EA_b+EB_b:.4f} à {EA_h+EB_h:.4f} ; plafonds de repli {c5(PA)} + {c5(PB)} = {c5(PA)+c5(PB)}")
# Plafonds recalculés à l'étape (m) : débits mesurés pris tels quels ; à défaut, d de l'agent, doublé
PA_m = lambda tA, m=1.0: 2 * pire * (max(1.0, m) + h(n * tA)) + 4
PB_m = lambda tB, L: 2 * pire * (h(n * tB) + L) + 4
print(f"  débits mesurés égaux aux hypothèses hautes, L = {L_h} : A {PA_m(t_h):.4f} -> {math.ceil(PA_m(t_h))} ; B {PB_m(tJ(t_h), L_h):.4f} -> {math.ceil(PB_m(tJ(t_h), L_h))}")
for d in (40.0, 42.8, 45.0):
    print(f"  d = {d} s, doublé, L = {L_h} : A {PA_m(2*d/10):.4f} -> {math.ceil(PA_m(2*d/10))} ; B {PB_m(2*tJ(d/10), L_h):.4f} -> {math.ceil(PB_m(2*tJ(d/10), L_h))}")
```

Sortie :

```
s par lecture : boîte noire 4.0200 à 4.2800 (borne haute 8.5600) ; juge 4.5806 à 4.8477 (borne haute 9.6954)
A : 8.1467 à 8.6089 h ; attendu 10.6400 à 13.1916 ; pire 51.5211 -> 55
B : lectures 8.1432 à 8.6181 h ; avec la lecture commune 8.2432 à 9.6181 h ; attendu 9.7542 à 12.5036 ; pire 57.0921 -> 60
Ensemble : 16.3899 à 18.2270 h ; attendu 20.3941 à 25.6951 ; plafonds de repli 55 + 60 = 115
  débits mesurés égaux aux hypothèses hautes, L = 1.0 : A 27.7605 -> 28 ; B 30.5460 -> 31
  d = 40.0 s, doublé, L = 1.0 : A 46.0133 -> 47 ; B 51.5088 -> 52
  d = 42.8 s, doublé, L = 1.0 : A 48.7611 -> 49 ; B 54.3321 -> 55
  d = 45.0 s, doublé, L = 1.0 : A 50.9200 -> 51 ; B 56.5504 -> 57
```

Contrôles faits à la main dans le texte, recoupés par le programme : surcoût du juge, (4,85 − 4,28) ÷ 4,28 = 0,133 ; écart des plafonds recalculés au repli, 1 − 99 ÷ 115 = 0,139 et 1 − 108 ÷ 115 = 0,061.

## 10. Déclaration

- **Rédacteur** : agent neuf pour ce devis (Claude Opus 5.5, à la place de Claude Fable 5.2 : écart déclaré en tête) ; rédacteur des devis de carte v3 et v4 ; auteur ni du texte, ni d'aucune pièce du côté habilité, ni du lanceur de l'étape de discrétion.
- **Ouvert** : les pièces de la section 1, aux lignes dites ; les deux messages de la session mère. **Ni ouvert, ni listé, ni cherché, ni empreinté** : aucun chemin cloisonné du mandat du devis de carte ; aucune pièce du côté habilité ; les chemins que cite le texte n'ont pas été suivis.
- **Aucune machine lancée, aucune clé, aucune dépense, aucun modèle extérieur consulté.** Les données du côté habilité ont été demandées à la session mère, par message, sans interne ; ses réponses sont citées en tête et en section 5.
