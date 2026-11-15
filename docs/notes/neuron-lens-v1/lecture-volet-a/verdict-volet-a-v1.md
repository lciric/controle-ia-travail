# Verdict du volet A de « Neuron Lens » (Qwen3-8B) — lecture par un lecteur neuf — v1

Écrit le 2026-11-15, entre 03:24 et 03:40 UTC. Lecteur neuf (sous-agent) : je n'ai écrit ni le texte gelé, ni le code, ni la course.
Critères appliqués mécaniquement : texte gelé `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` (`34b88243`), selon mon plan
scellé avant toute lecture de résultat, `plan-de-lecture-v1.md` (`9413e09b`). Seul le volet A est jugé ; la tranche B-α n'a pas été courue.
Verdict à soumettre à Lazar (R13) ; il ne franchit aucune porte du programme (expérience hors programme).

## Verdict

**Chaîne : saine** (les trois cas sains passent ; aucune empreinte fausse).

**Mesure A-i (lire la direction d'une sonde) : « n'apporte rien »**, par deux lignes du critère gelé, chacune suffisante :
A1 « non retrouvée » ; A3 « dépendance non lue » sur C1 et sur C2.

| | C1 (nuisible / bénin) | C2 (fuite plantée) | C3 (vrai / faux) |
|---|---|---|---|
| A1 | — | **non retrouvée** (4 couches négatives sur 4 ; 0 case sur 20 où S place un jeton planté dans ses 10 premiers) | — |
| A2 (rapporté) | pas sans objet (sac de jetons 0,7843) ; « nomme » : oui (4 couches positives) | — | — |
| A3 | **dépendance non lue** (couches 20 et 26 ; 8 et 14 sans objet) | **dépendance non lue** (4 couches) | — |
| S fait mieux que sans lentille | sur A2 : **oui** (4 couches positives, toutes positives de A2) | sur A1 : **non** (couches 8 et 20 positives pour la comparaison, mais aucune couche positive de A1) | — |
| « sans lentille ≥ S » à chaque couche | sur A2 : non (aucune couche) | sur A1 : non (couches 14 et 26 seulement) | — |
| A-ii (neurones comme traits) | **indéterminé**, qualificatif « au-delà du texte » (voir ambiguïté 1) | **sans objet** (plafond : une seule couche jugeable), qualificatif sans objet | **apporte**, qualificatif « au-delà du texte » |

Déclencheurs de l'audit symétrique du texte gelé : **aucun** (ni « trop beau », ni « tout négatif »). Mes verdicts, recalculés par mon
programme sans importer le code de la course, sont **identiques** à ceux que la course a écrits dans `volet-a-brut.json` (`8bb9f31a`).

**Réserves de symétrie, à lire avec le verdict** (détail plus bas) : (a) A3 est dégénérée — la chute est exactement nulle dans 39 cases sur
40 parce que les 20 jetons nommés par la lecture S sont presque tous absents des textes ; ce n'est pas une seconde preuve indépendante de
A1 ; (b) « apporte » sur C3 ne repose que sur l'en-distribution, et 64 neurones tirés au hasard ou 64 composantes principales font presque
aussi bien aux couches profondes ; (c) « nomme » (A2) tient à des corrélations faibles (0,06 à 0,20), qu'un témoin à étiquettes permutées
atteint dans une découpe.

Règle de lecture du texte gelé, rappelée : une lecture par lentille peut ajouter un soupçon sur une sonde, jamais la blanchir ; « fuite non
retrouvée » se lit « l'instrument ne voit pas une fuite plantée à cette profondeur ».

## Sources et empreintes

| pièce | chemin | empreinte |
|---|---|---|
| texte gelé | `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` | `34b88243` (compagnon : conforme) |
| plan de lecture, scellé avant lecture | `docs/notes/neuron-lens-v1/lecture-volet-a/plan-de-lecture-v1.md` | `9413e09b` |
| cas sains | `diag/20261114-165239-neuron-lens-volet-a/brut-cas-sains.json` | `2294511e` (conforme) |
| mesures C1 | `…/brut-mesures-C1.json` | `26b8d7e6` (conforme) |
| mesures C2 | `…/brut-mesures-C2.json` | `5197b450` (conforme) |
| mesures C3 | `…/brut-mesures-C3.json` | `a196420b` (conforme) |
| relevé des fichiers | `…/releve-fichiers.json` | `2b26efa8` (conforme) |
| sortie complète | `…/volet-a-brut.json` | `8bb9f31a` (conforme) |
| manifeste | `runs/20261114-165239-neuron-lens-volet-a/manifeste.json` | `59da2609` (conforme) |
| mon calcul | `docs/notes/neuron-lens-v1/lecture-volet-a/calcul_verdicts_volet_a_v1.py` | `4f1d4c71` |
| sa sortie | `…/lecture-volet-a/calcul-verdicts-volet-a-v1.json` | `4b4b07a0` |
| compléments descriptifs | `…/lecture-volet-a/complements_volet_a_v1.py` ; sortie `complements-volet-a-v1.json` | `a4aea5c1` ; `590a9430` |

Sauf mention, **tout chiffre ci-dessous vient de `calcul-verdicts-volet-a-v1.json` (`4b4b07a0`)**, calculé sur les trois fichiers de mesures
(`26b8d7e6`, `5197b450`, `a196420b`) ; les chiffres marqués « (compl.) » viennent de `complements-volet-a-v1.json` (`590a9430`).

Manifeste (`59da2609`) : run décisif, dépôt propre, préenregistrement cité `34b88243`, entropie 20261114, couches 8, 14, 20, 26, 200
tirages de A3, 20 tirages de neurones au hasard, 2 000 rééchantillonnages, `GO-2026-11-14-05`. Les six fichiers de résultats portent
l'empreinte du manifeste (`59da2609`) et le même identifiant de run. Empreintes des lentilles R, S (`out`), S (`mid`) et du tokeniseur
au relevé (`2b26efa8`) : égales à celles du texte gelé. Empreintes des modules de la course citées au manifeste : égales aux fichiers de
la branche (contrôlées pour huit modules). `volet-a-brut.json` : `fumee` faux, mesures identiques octet de données pour octet aux trois
fichiers bruts, 0 avertissement de convergence, 103 830 jetons gardés, 2 448 textes rendus vérifiés.

## 1. Cas sains (lus en premier) — `brut-cas-sains.json` (`2294511e`)

| cas | règle gelée | observé | passe |
|---|---|---|---|
| (i) lecture R brute du pôle `L8 n344 +` | un des 10 premiers commence par « owl » ou « noct », ou vaut « night » | owl, noct, cosy, bedtime, autumn, owl, night, pupils, 夜间, ow | oui (règle rejouée sur la liste) |
| (ii) lecture S brute (`mid`, couche 1) du pôle `L1 n11672 −` | un des 10 premiers contient « german » ou « 德 » | german, german, german, germany, germans, 德国, germ, germany, deutsche, deutsch | oui (rejouée) |
| (iii) cas synthétique, « Ġworld » au rang 1, lecture S `_z` et lecture sans lentille `_z` | aux 4 couches | 8 booléens vrais sur 8 | oui (booléens lus ; non rejouable sans les matrices) |

Les listes sur le vocabulaire entier sont les mêmes à un jeton près ((ii) : « ドイツ » à la place de « deutsch »). Les trois cas passent
largement (7 formes sur 10 pour (ii)) : c'est attendu pour des pôles choisis dans le README voisin, je le note sans en faire une réserve.

## 2. A1 (C2) — meilleur rang d'un jeton planté dans la lecture S `_z`, deux signes

Rangs parmi 103 830 jetons gardés ; 5 découpes ; « témoin » = l'un des 102 témoins place un jeton planté dans ses 10 premiers.

| couche | rang de S par découpe | médiane | rang sans lentille par découpe | médiane | (i) S place P (≤ 10) | (ii) un témoin place P | condition tenue | couche | S strictement meilleur que sans lentille |
|---|---|---|---|---|---|---|---|---|---|
| 8 | 564, 921, 1442, 1422, 825 | 921 | 22841, 23760, 23243, 19295, 19966 | 22841 | 0 / 5 | 0 / 5 | 0 / 5 | négative | 5 / 5 (positive) |
| 14 | 7696, 7458, 6661, 7372, 5378 | 7372 | 2874, 3638, 3086, 2842, 2401 | 2874 | 0 / 5 | 1 / 5 (découpe 4ᵉ) | 0 / 5 | négative | 0 / 5 (négative) |
| 20 | 463, 918, 1029, 683, 811 | 811 | 1917, 1141, 1393, 1442, 1087 | 1393 | 0 / 5 | 1 / 5 (découpe 4ᵉ) | 0 / 5 | négative | 5 / 5 (positive) |
| 26 | 5427, 5109, 3741, 2975, 5812 | 5109 | 2924, 2832, 3353, 2844, 10550 | 2924 | 0 / 5 | 1 / 5 (découpe 5ᵉ) | 0 / 5 | négative | 1 / 5 (négative) |

- **A1 : « non retrouvée »** (4 couches négatives). Meilleur rang de S sur les 20 cases : 463 (0,45 % du vocabulaire gardé) (compl.).
- Composantes à part : (i) S ne place jamais un jeton planté dans ses 10 premiers (0 / 20) ; (ii) un témoin le fait dans 3 cases sur 20
  (attendu au hasard pour 102 directions, deux signes, 4 jetons : environ 0,076 par case, soit 1,5 case sur 20) (compl.).
- La lecture sans lentille ne place pas non plus un jeton planté (meilleur rang 1 087) (compl.).
- Ma condition recalculée (`rang ≤ 10 et aucun témoin`) est égale au booléen de la course dans les 20 cases.
- Sonde de C2 : AUROC de test 1,0000 aux couches 14, 20, 26 et 0,99997 à la couche 8 (minimum sur les découpes 0,99987) : **la sonde a bien
  appris la fuite** ; ce n'est pas la sonde qui manque, c'est la lecture. Description jointe : aucun jeton planté non plus parmi les 20
  premiers de la lecture R (différence des moyennes et poids de la sonde), à aucune couche ni découpe (compl.).

## 3. A2 (C1) — corrélation de rangs entre la lecture S `_z` et les poids du sac de jetons (rapporté)

Sac de jetons sur C1, AUROC en distribution par découpe : 0,7300, 0,7567, 0,8056, 0,8056, 0,8239 ; moyenne **0,7843** ≥ 0,60 → A2 **n'est
pas sans objet** (valeur identique aux quatre couches, comme attendu).

| couche | ρ de S par découpe | ρ sans lentille par découpe | condition (ρ de S > 99ᵉ centile des 100 directions) | couche | ρ de S > ρ sans lentille |
|---|---|---|---|---|---|
| 8 | 0,122, 0,131, 0,146, 0,140, 0,201 | −0,091, −0,118, −0,011, −0,112, −0,043 | 4 / 5 | positive | 5 / 5 (positive) |
| 14 | 0,120, 0,131, 0,128, 0,100, 0,093 | −0,048, −0,029, −0,008, 0,015, −0,019 | 4 / 5 | positive | 5 / 5 (positive) |
| 20 | 0,106, 0,138, 0,113, 0,136, 0,063 | −0,107, −0,066, −0,108, −0,114, −0,178 | 3 / 5 | positive | 5 / 5 (positive) |
| 26 | 0,124, 0,158, 0,150, 0,162, 0,119 | −0,010, 0,021, −0,020, −0,025, 0,025 | 4 / 5 | positive | 5 / 5 (positive) |

- **« Nomme » : oui** (4 couches positives) — rapporté ; n'entre dans le verdict que par la comparaison.
- **S fait mieux que sans lentille sur A2 : oui** (4 couches positives pour la comparaison, toutes positives de A2).
- Témoins rapportés hors condition : la sonde à étiquettes permutées atteint ρ = 0,1377 à la couche 20, quatrième découpe, contre 0,1364
  pour S dans la même case ; 0,117 à la couche 26 et 0,075 à la couche 14, même découpe ; direction de C3 : au plus 0,102 (compl.).
- Limite : les 100 ρ aléatoires ne sont pas versés ; la condition est lue sur le booléen de la course, non rejouée.

## 4. A3 — chute d'AUROC de la sonde après retrait des 20 jetons de la lecture S

Chutes par découpe ; « 95ᵉ » = 95ᵉ centile des 200 tirages appariés ; « sac » = chute avec les 20 premiers jetons du sac de jetons.

**C1**

| couche | chute S | 95ᵉ centile | chute du sac (moyenne) | sans objet (< 0,02) | condition | « chute < moitié du sac » | jetons S présents dans le test (sur 20) |
|---|---|---|---|---|---|---|---|
| 8 | 0, 0, 0,0022, 0, 0 | 0, 0,0045, 0,0012, 0,0022, 0,0001 | 0,0322, −0,0211, 0,0056, 0,0056, 0,0333 (0,0111) | **oui** | 0 / 5 | 4 / 5 | 0, 1, 1, 0, 0 |
| 14 | 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0 | 0,0356, −0,0133, 0,0033, 0,0289, 0,0389 (0,0187) | **oui** | 0 / 5 | 4 / 5 | 0 partout |
| 20 | 0, 0, 0, 0, 0 | 0,0012, 0,0022, 0, 0,0033, 0,0022 | 0,0411, 0,0367, 0,0411, 0,0011, 0,0300 (0,0300) | non | 0 / 5 (négative) | 5 / 5 (positive) | 0 partout |
| 26 | 0, 0, 0, 0, 0 | 0,0067, 0,0056, 0,0044, 0,0044, 0,0011 | 0,0256, 0,0400, 0,0400, 0,0256, 0,0456 (0,0353) | non | 0 / 5 (négative) | 5 / 5 (positive) | 0 partout |

Deux couches non sans objet (20, 26) → C1 n'est pas sans objet ; aucune couche positive ; toutes positives pour la condition contraire →
**« dépendance non lue »**.

**C2**

| couche | chute S | 95ᵉ centile | chute du sac | sans objet | condition | « chute < moitié du sac » | jetons S présents dans le test |
|---|---|---|---|---|---|---|---|
| 8 | 0 partout | 0 partout | 0,5000, 0,5000, 0,5000, 0,4999, 0,5000 | non | 0 / 5 (négative) | 5 / 5 (positive) | 0 partout |
| 14 | 0 partout | 0 partout | 0,5000 partout | non | 0 / 5 (négative) | 5 / 5 (positive) | 0 partout |
| 20 | 0 partout | 0 partout | 0,5000 partout | non | 0 / 5 (négative) | 5 / 5 (positive) | 0, 1, 1, 0, 1 |
| 26 | 0 partout | 0 partout | 0,5000 partout | non | 0 / 5 (négative) | 5 / 5 (positive) | 0 partout |

→ **« dépendance non lue »**. Aucun exemple écarté pour texte vide (0 partout) ; 20 jetons du sac retirés dans chaque case.

Comparaison exacte et comparaison après arrondi à 6 décimales (ce que fait le code de la course ; le texte gelé ne prévoit pas d'arrondi) :
**aucune différence**, sur aucun seuil du volet A.

## 5. Verdict de A-i, ligne par ligne

| ligne du critère gelé | tenue |
|---|---|
| cas sain manqué | non |
| A1 non retrouvée | **oui** |
| « sans lentille ≥ S » à chaque couche sur A1 et sur A2 | non (A1 : couches 14 et 26 seulement ; A2 : aucune) |
| A3 « dépendance non lue » dans chaque contraste non sans objet, au moins un | **oui** (C1 et C2) |

→ **« n'apporte rien »** (priorité sur « apporte quelque chose » ; la question « A1 retrouvée et S fait mieux » ne se pose pas). Issue
modale prédite par le texte gelé : « n'apporte rien » ou « indéterminé » (confiance 0,7) — conforme à la prédiction.

## 6. A-ii — neurones comme traits, par contraste

AUROC moyennes sur 5 découpes. « IC » = intervalle à 95 % de l'écart (neurones − sonde) par rééchantillonnage apparié, 2 000 tirages,
graines du texte gelé pour le hors distribution. Les jeux de test des 5 découpes se recouvrent : ce n'est pas l'intervalle d'exemples
indépendants (dit par le texte gelé).

### C1 (60 exemples de test par découpe ; hors distribution : 463 d'AdvBench contre 30 bénins de test) — **indéterminé**

| couche | sonde, en distribution | k=1 | k=8 | k=64 | k=512 | sonde, hors distribution | k=1 | k=8 | k=64 | k=512 | IC hors distribution à k=64 | à k=512 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | 0,7931 | 0,5494 | 0,6500 | 0,6684 | 0,7491 | 0,8732 | 0,5764 | 0,6841 | 0,7426 | 0,8206 | −0,1306 [−0,1681 ; −0,0939] | −0,0526 [−0,0828 ; −0,0230] |
| 14 | 0,8660 | 0,5677 | 0,7076 | 0,8031 | 0,8582 | 0,9308 | 0,6442 | 0,7109 | 0,8521 | 0,9085 | −0,0787 [−0,1064 ; −0,0543] | −0,0223 [−0,0402 ; −0,0055] |
| 20 | 0,9364 | 0,7382 | 0,7853 | 0,8738 | 0,9136 | 0,9808 | 0,8172 | 0,8522 | 0,9472 | 0,9718 | −0,0337 [−0,0494 ; −0,0209] | −0,0090 [−0,0158 ; −0,0032] |
| 26 | 0,8851 | 0,6478 | 0,7549 | 0,8264 | 0,8464 | 0,9660 | 0,6713 | 0,8099 | 0,9076 | 0,9312 | −0,0584 [−0,0768 ; −0,0416] | −0,0348 [−0,0503 ; −0,0208] |

- Plafond : aucune couche (sonde < 0,99 partout) ; 4 couches jugeables.
- « N'apporte rien » : **non** — à k = 512 la sonde ne gagne de plus de 0,05 sur les deux parties à aucune couche (et à k = 64, couche 20,
  l'écart hors distribution est de 0,034).
- « Apporte » : **non** — à aucun k ≤ 64 la condition en distribution (neurones ≥ sonde − 0,02) ne tient à une seule couche (écarts à
  k = 64 : −0,125, −0,063, −0,063, −0,059) ; la borne basse hors distribution ≥ −0,05 ne tient qu'à la couche 20, k = 64 (−0,0494).
- → **« indéterminé »**. Prédiction du texte gelé « écart en distribution < 0,02 dès k = 64 » : **non tenue** sur C1 ; issue prédite
  (« indéterminé » ou « sans objet ») : tenue.
- Qualificatif : meilleur détecteur à k ≤ 64 hors distribution 0,9472 (couche 20) contre sac de jetons 0,8195 → **« au-delà du texte »**
  dans la lecture « toutes couches » ; couche par couche : oui aux couches 14 (0,852), 20, 26 (0,908), non à la couche 8 (0,743) — ambiguïté 1.
- Rapportés : détecteur dense 0,771 / 0,862 / 0,935 / 0,875 en distribution (couches 8 à 26) ; 64 neurones au hasard 0,571 / 0,628 / 0,680 /
  0,635 ; 64 composantes principales 0,713 / 0,810 / 0,900 / 0,861 ; à k = 512 la sonde sur composantes n'a que 139 composantes (rang de
  l'apprentissage, déclaré par le code) ; base « longueur seule » 0,608 (texte gelé : 0,61).

### C2 (178 exemples de test par découpe ; hors distribution : consignes paraphrasées) — **sans objet** (plafond)

| couche | sonde, en distribution | sonde, hors distribution | plafond | k=64 en distribution | k=64 hors distribution | IC hors distribution à k=64 |
|---|---|---|---|---|---|---|
| 8 | 1,0000 | 0,8866 | en distribution seulement → jugeable hors distribution | 0,9992 | 0,9850 | +0,0984 [+0,0794 ; +0,1191] |
| 14 | 1,0000 | 0,9998 | les deux → sans objet | 1,0000 | 0,9997 | −0,0002 [−0,0006 ; +0,0002] |
| 20 | 1,0000 | 0,9998 | les deux → sans objet | 1,0000 | 0,9993 | −0,0005 [−0,0011 ; 0,0000] |
| 26 | 1,0000 | 0,9972 | les deux → sans objet | 0,9974 | 0,9667 | −0,0306 [−0,0419 ; −0,0211] |

Une seule couche non sans objet (8) → contraste **sans objet** ; qualificatif sans objet (sac de jetons hors distribution : 0,5000, par
construction). Issue prédite : tenue. Rapporté sans verdict : à la couche 8, les détecteurs sur neurones font **mieux** que la sonde
résiduelle hors distribution dès k = 8 (+0,035 [+0,012 ; +0,058]) ; sac de jetons en distribution 1,0000 ; base « longueur seule » 0,638.

### C3 (179 exemples de test par découpe ; pas de hors distribution) — **apporte**, « au-delà du texte »

| couche | sonde | k=1 | k=8 | k=64 | k=512 | écart à k=64 | IC en distribution à k=64 (graine du lecteur, description) | 64 neurones au hasard | 64 composantes | dense |
|---|---|---|---|---|---|---|---|---|---|---|
| 8 | 0,7918 | 0,6308 | 0,7257 | 0,7931 | 0,7853 | +0,0013 | [−0,0146 ; +0,0177] | 0,7160 | 0,7843 | 0,7839 |
| 14 | 0,9400 | 0,8697 | 0,9139 | 0,9349 | 0,9471 | −0,0051 | [−0,0139 ; +0,0030] | 0,8671 | 0,9305 | 0,9402 |
| 20 | 0,9882 | 0,9498 | 0,9780 | 0,9835 | 0,9862 | −0,0047 | [−0,0086 ; −0,0012] | 0,9683 | 0,9872 | 0,9878 |
| 26 | 0,9838 | 0,9148 | 0,9653 | 0,9744 | 0,9825 | −0,0094 | [−0,0165 ; −0,0036] | 0,9426 | 0,9841 | 0,9792 |

- Plafond : aucune couche (maximum 0,9882 à la couche 20, à 0,0018 du plafond de 0,99) ; 4 couches jugeables.
- « N'apporte rien » : non. « Apporte » : **oui** — à k = 64, neurones ≥ sonde − 0,02 aux 4 couches ; à k = 8, aux couches 20 et 26.
  Si la couche 20 passait le plafond, il resterait 3 couches jugeables et la condition tiendrait encore.
- Qualificatif : 0,9835 contre sac de jetons 0,5480 → **« au-delà du texte »** (les deux lectures de l'ambiguïté 1 s'accordent).
- Prédiction « écart < 0,02 dès k = 64 » : tenue sur C3. Base « longueur seule » 0,568 (texte gelé : 0,57).

### Intervalles : sensibilité

Bornes basses hors distribution recalculées avec les graines du texte gelé : égales à celles de la course à 2 × 10⁻¹⁶ près. Avec une graine
à moi, et avec un tirage non stratifié par classe (le texte gelé dit « stratifiés par découpe » sans parler des classes ; le code de la
course tire par classe, lecture qu'il déclare) : **mêmes verdicts** sur C1 et C2 ; la case la plus proche d'un seuil (C1, couche 20, k = 64,
borne −0,0494 pour un seuil de −0,05) donne −0,0502 et −0,0503 dans ces deux variantes, sans effet sur le verdict (la condition en
distribution y manque de toute façon).

## 7. Audit symétrique (R4)

Déclencheurs du texte gelé :
- « trop beau » : A1 au rang 1 à toutes les couches — non (rangs médians 921, 7 372, 811, 5 109) ; « neurones égaux à la sonde partout » — le
  texte n'en donne pas de définition ; avec celle que le code de la course déclare (écart ≤ 0,005 en distribution pour le meilleur k ≤ 64, à
  chaque contraste et couche) : non (C1 : 0,059 à 0,125 ; C3 : 0,0013, 0,0051, 0,0047, 0,0094 ; C2 : ≤ 0,0026). **Non déclenché** ; la course
  n'a donc pas joué l'audit (pas de sixième découpe dans la sortie), ce qui est conforme.
- « tout négatif » (A1 non retrouvée **et** A-ii « n'apporte rien » sur C1 et C3) : **non déclenché** (C1 indéterminé, C3 apporte). L'AUROC
  de la sonde de C2 est rapportée quand même (§ 2) : ≥ 0,9999 partout, donc A1 ne se relit pas comme « la sonde n'a pas appris ».

Réserves de symétrie que je signale, sans changer le verdict mécanique :

1. **A3 trop propre, côté négatif.** La chute de S est exactement 0 dans 19 cases sur 20 sur C1 et 20 sur 20 sur C2 ; le 95ᵉ centile des
   tirages est exactement 0 dans 7 et 20 cases ; 89 % et 99 % des tirages sont exactement nuls (compl.). Cause visible dans le brut : sur
   les 20 jetons nommés par la lecture S, **au plus un** est présent dans les textes de test (2 présences au total sur 20 cases pour C1, 3 pour
   C2), et aucun n'est un jeton planté (compl.) ; le retrait ne modifie presque aucune invite, et le code garde alors le score d'origine.
   « Dépendance non lue » est donc la conséquence mécanique du même fait que A1 (la lecture S nomme des jetons qui ne sont pas dans les
   textes), pas une seconde mesure indépendante. La règle s'applique telle quelle ; je ne l'arbitre pas.
2. **A3 sur C1 tient à un fil.** Le sac de jetons ne fait chuter la sonde que de 0,011 à 0,035 (une chute négative dans une découpe) ;
   C1 a exactement 2 couches non sans objet, la couche 14 manque le plancher à 0,0187. Avec une couche de moins, C1 serait « sans objet » ;
   le verdict de A-i ne changerait pas (C2 suffit, et A1 seul suffit).
3. **A1 très net, côté négatif** (0 case sur 20, meilleur rang 463). Les garde-fous prévus pour un négatif sont tenus : cas sains passés,
   sonde de C2 à 1,000, chute de 0,5000 quand on retire les jetons du sac (la sonde dépend bien de jetons du texte). Limite : la liste des
   20 jetons du sac n'est pas versée, je ne peux pas vérifier qu'elle contient les jetons plantés ; les rangs des 102 témoins non plus.
4. **C2 à 1,0000 partout** (sonde, sac de jetons, détecteur dense) : attendu d'une fuite plantée, prévu par le texte gelé (plafond) ;
   pénalité choisie = la plus petite de la grille (10⁻⁴) dans presque toutes les cases, par la règle d'égalité.
5. **« Apporte » sur C3, côté positif.** Le critère ne compare les neurones choisis qu'à la sonde. Or, aux mêmes couches, 64 composantes
   principales font aussi bien (écart −0,010 à +0,000) et **64 neurones tirés au hasard** sont à −0,0198 de la sonde à la couche 20 (dans la
   marge de 0,02 à eux seuls), −0,041 à la couche 26, −0,073 et −0,076 aux couches 14 et 8 (compl.). L'apport propre au choix des neurones
   est donc net aux couches 8 et 14, mince aux couches 20 et 26. C3 n'a pas de jeu hors distribution : « apporte » y repose sur
   l'en-distribution seule, sur des découpes qui se recouvrent.
6. **« Nomme » (A2), côté positif** : corrélations de 0,06 à 0,20 ; le témoin à étiquettes permutées, rapporté hors condition, égale S dans
   une case (§ 3). La condition gelée ne regarde que les 100 directions aléatoires.
7. **Accord parfait entre mes verdicts et ceux de la course** : attendu, les deux partent du même brut ; mon programme réécrit les règles
   mais j'ai lu le code de la course pour connaître les champs et reproduire ses graines. Ce n'est pas une réplication de la course.

## 8. Écarts et ambiguïtés rencontrés (non arbitrés)

1. **Qualificatif de A-ii** : le texte dit « le meilleur détecteur à k ≤ 64 » sans dire si le meilleur se prend sur toutes les couches
   (lecture du code de la course) ou couche par couche. C1 : « au-delà du texte » dans la première lecture ; dans la seconde, oui aux couches
   14, 20, 26, non à la couche 8. C3 : les deux s'accordent.
2. **« S fait mieux que sans lentille »** n'a pas une réponse unique : non sur A1, oui sur A2. Sans effet ici (« n'apporte rien » prime).
3. **Arrondi à 6 décimales** avant comparaison aux seuils : ajouté par le code, absent du texte gelé. Aucun cas où il change une comparaison.
4. **Stratification du rééchantillonnage par classe** : lecture du code, non écrite au texte gelé. Sans effet sur les verdicts (§ 6).
5. **Témoins non rejouables** : les rangs des 102 témoins de A1, les 100 ρ aléatoires de A2 et les 20 jetons du sac de A3 ne sont pas dans
   le brut ; seuls leurs effets (booléens, chutes) y sont. Conditions de A1 et A2 lues, non recalculées.
6. **Manifeste** : `versions` ne consigne pas `scikit-learn`, alors que le texte gelé dit « version consignée » et que l'addendum la liste
   (le fichier d'exigences du dépôt réduit épingle 1.6.1) ; le champ `graines` est vide (l'entropie et l'arbre sont dans `config`) ; le
   commit `799a8a32` est celui du dépôt réduit envoyé à la machine (`docs/notes/neuron-lens-v1/depot-reduit-volet-a-v10-3a470fa4/rapport.json`),
   pas un objet de la branche ; le manifeste ne liste pas les empreintes des résultats, ce sont les résultats qui portent la sienne.
7. **Description jointe A.5** (étiquettes et lectures du catalogue des 8 premiers neurones, accord avec la liste de mots) : le brut ne
   contient que les indices des neurones ; cette description, sans critère, n'est pas dans les pièces que j'ai lues. Lecture R : identifiants
   des 20 premiers jetons versés, non décodés ici.
8. **Écarts à mon plan** : (a) j'ai ajouté après lecture un second programme, descriptif, sans critère (`complements_volet_a_v1.py`) et un
   intervalle en distribution à ma graine ; (b) pour identifier le commit du manifeste, j'ai cherché la chaîne `799a8a32` dans
   `docs/notes/neuron-lens-v1/` et lu deux lignes du journal de course v2 et un champ du rapport du dépôt réduit, après mes verdicts.
   Aucun autre `diag/`, `runs/`, branche ou `donnees/` n'a été ouvert ; aucun modèle chargé, aucun appel payant.

## 9. Ce que le verdict dit et ne dit pas

- Il dit : sur Qwen3-8B, aux couches 8, 14, 20, 26, à la dernière position du tour d'utilisateur, la lentille S appliquée au poids d'une
  sonde qui sépare parfaitement deux consignes **ne nomme pas** les jetons plantés (ni dans ses 10 premiers, ni dans ses 400 premiers), et les
  jetons qu'elle nomme ne sont pas ceux dont la sonde dépend.
- Il ne dit pas que la sonde est propre (règle de lecture gelée), ni que la lentille ne lit rien : sur C1 sa lecture est corrélée, faiblement
  mais au-dessus des directions aléatoires et de la lecture sans lentille, aux poids du sac de jetons.
- A-ii : rien de tranché sur C1, rien de jugeable sur C2, un « apporte » sur C3 à lire avec la réserve 5.
