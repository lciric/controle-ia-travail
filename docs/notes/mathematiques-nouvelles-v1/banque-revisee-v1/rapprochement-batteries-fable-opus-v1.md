# Rapprochement des deux batteries de fuite (juge Fable, juge Opus) — proposition d'une batterie unique — v1

- Nature : note de travail (classe C), écrite par la session des mathématiques nouvelles le 2026-11-22, pour la mère, avant tout gel. Elle ne gèle rien : la batterie gelée sera écrite par le concepteur (Fable) et contre-lue par Opus, selon la règle « qui conçoit ».
- Décision appliquée : GO-2026-11-22-115 (« l'option Fable … go, ajoute deux sondes (style, nombres), avec un rappel au plus de 10 % à fausses alarmes fixées »).
- Sources, empreintes vérifiées : jugement Fable `juge-fable-max-v1.md` (b1380fe3…), son erratum 1 (81073193…), jugement Opus `juge-opus-max-v1.md` (f82e0c8f…), copiés dans `juges-recus/` depuis la branche claude/avis-carbon-astra-v1.

## Verdict

1. Les deux formulations se recoupent presque entièrement : les « deux sondes (style, nombres) » du juge Opus sont déjà deux des trois sondes de la condition 3 du juge Fable, au même point de fonctionnement (fausses alarmes ≤ 0,10) et au même seuil (rappel ≤ 0,20, soit un excès ≤ 0,10 au-dessus du hasard), jugé de la même façon (borne haute d'un intervalle à 90 % par rééchantillonnage des racines).
2. **Une contradiction de lettre, à trancher par Lazar avant le gel** : « un rappel au plus de 10 % à fausses alarmes fixées ». Pris à la lettre avec des fausses alarmes fixées à 10 %, ce critère demande un excès nul au-dessus du hasard en borne haute : une sonde sans information a un rappel attendu d'environ 0,10, et la borne haute de son intervalle est au-dessus ; une banque parfaitement saine échouerait donc le plus souvent (à confirmer par l'épreuve sur un cas sain, règle R5).
3. Quatre écarts secondaires (statut de la règle aveugle, branche si la version 7 tient à moitié, relecture de la banque réelle, épreuve du critère) se règlent par une seule batterie, proposée au § 3.

## 1. Ce qui se recoupe

| point | juge Fable (§ 3.3) | juge Opus (§ 2.3) | rapprochement |
|---|---|---|---|
| sonde de style | classifieur actuel, inchangé | même | identique |
| sonde des nombres | « voit les nombres (nombre et taille des littéraux, proximité de 0 et de 1) » | lit seulement les littéraux ; ordre de grandeur, fraction, 0/1/2, nombre, position par rapport aux constantes du monde | même objet ; la spécification d'Opus est plus complète, à prendre |
| point de fonctionnement | fausses alarmes ≤ 0,10, seuil réglé sur les mondes d'apprentissage | fausses alarmes ≤ 0,10 sur les vrais non vus, ex æquo jamais franchis par tirage | identique ; garder la règle des ex æquo |
| seuil | rappel ≤ 0,20 | excès (rappel − 0,10) ≤ 0,10 | identique |
| ensembles | chaque strate de faux (faux tôt, pièges) | faux tôt, pièges, tous les faux | prendre les trois |
| jugement | borne haute à 90 %, rééchantillonnage des racines | même, 2 000 tirages, borne non calculable = « non tenu » | identique ; garder la règle « non calculable = non tenu » |
| racines | au moins 40 neuves, tirées après le gel | même ; `secrets.randbits(128)`, empreintes commises avant mesure ; une version 8 sur un autre lot | identique ; prendre le protocole d'Opus |
| aire de 0,75 | condition nécessaire, même calcul | rapportée sans effet | **Lazar a tranché pour Fable** : condition nécessaire |
| invariant de construction | condition 1, contrôlée à la plantation | paires minimales, grandeurs de même loi, paire unité de tirage | même intention ; l'invariant d'Opus est plus fort, à prendre comme forme de la condition 1 |
| deux fuites | forme et instance | forme et instance | identique |
| deux cycles au plus | oui | (date butoir) | les deux : deux cycles, et pas au-delà du 4 décembre 23:59Z |

## 2. Ce qui diverge

1. **La lettre « rappel ≤ 10 % »** (verdict, point 2). Trois lectures possibles :
   - (i) excès ≤ 0,10, soit rappel ≤ 0,20 à fausses alarmes ≤ 0,10 — c'est la lettre du juge Opus que Lazar dit ajouter, et la condition 3 du juge Fable ; les deux sondes ne changent alors que la spécification de la sonde des nombres et les ensembles ;
   - (ii) rappel ≤ 0,10 à fausses alarmes fixées plus bas, à 0,05 (excès ≤ 0,05) — plus strict, tenable en principe, mais la largeur d'intervalle sur 40 racines peut le rendre intenable même sain (à vérifier à l'épreuve R5) ;
   - (iii) rappel ≤ 0,10 à fausses alarmes ≤ 0,10, en borne haute — intenable en pratique (échoue le plus souvent sur le cas sain).
   - Recommandation : (i), confiance 0,8. C'est ce que disent les deux juges et ce que la mère a inscrit comme « complété des deux sondes du juge Opus ». Défaut proposé sous 48 heures : (i).
2. **Statut de la règle aveugle.** Fable : condition 4 (règle A du brouillon 4 ≤ la moitié des faux) ; non tenue, la lecture en preuve reste calculée mais « gain ≥ 0,20 hors de portée » est écrit d'avance. Opus : non bloquante ; cible de dessin plus forte (instances saillantes, médiane ≤ 0,50). Rapprochement : condition 4 telle que Fable (Lazar l'a choisie), jugée en borne haute ; la règle des instances saillantes rapportée en description, sans effet.
3. **Branche si la version 7 tient à moitié.** Fable : famille qui résiste → banque restreinte aux gabarits appariés des familles qui tiennent ; batterie non tenue après deux cycles → lecture en preuve seule. Opus : branche b (version 7 certifiée, forme non tenue, instance tenue) → H3 sur la version 7, preuve seule ; branche c (sinon, ou date dépassée) → version 6. Lazar : les bras partent sur la version 6 après le 4 décembre. Proposition au § 3, branches.
4. **Relecture sur la banque réelle.** Fable : une valeur hors de la plage vue sur les racines neuves ferme la lecture en verdict et est un fait d'instrument à expliquer. Opus : au-delà du 95e centile. Proposition : la règle de Fable (plus prudente, plus simple), pour chaque condition 2 à 4.
5. **Épreuve du critère (R5)** : seul Opus la pose. La règle gelée R5 l'impose de toute façon. Proposition : la prendre.
6. **Troisième sonde, tenue à l'écart du concepteur** (Fable seul). Écrite par le vérificateur du code après le gel de la banque. Lazar n'en parle pas ; sa décision prend « les quatre conditions » du juge Fable, donc elle est incluse. Le juge Fable l'autorise à être retirée en premier, avec une ligne d'écart, si la capacité manque.

## 3. Batterie unique proposée (à geler par le concepteur)

Calculée sans appel de modèle. Jugée sur le générateur (au moins 40 racines neuves), puis relue sur la banque réelle au rejeu, avant tout appel.

- **C1 — invariant de construction** (contrôlé par le code à la plantation) : paires (ou triplets) minimales ; chaque gabarit apparié donne vérité, faux tôt et piège dans les mêmes proportions, dans chaque monde, même squelette de jetons à part les nombres, littéraux tirés de la même loi ; la paire est l'unité de tirage de la sous-banque ; gabarits non appariables dits et comptés, jamais retirés en silence.
- **C2 — aire du classifieur de style ≤ 0,75**, même calcul qu'aujourd'hui (plus grande des deux strates), borne haute ; les aires par strate, sur tous les faux, contre les vrais du même gabarit, et leurs intervalles, rapportés.
- **C3 — rappel à fausses alarmes ≤ 0,10 : au plus 0,20** (excès ≤ 0,10) pour chacune de trois sondes — style (inchangée), nombres (spécification du juge Opus, gelée avec la batterie), tenue à l'écart (écrite par le vérificateur après le gel) — et chacun de trois ensembles (faux tôt, pièges, tous les faux) ; borne haute à 90 % par 2 000 rééchantillonnages des racines ; ex æquo jamais franchis par tirage ; non calculable = non tenu.
- **C4 — règle aveugle A du brouillon 4, sans retouche** : contre-exemple vérifié sur au plus la moitié des faux, borne haute. La règle des instances saillantes est rapportée en description.
- **Épreuve R5 de la batterie, avant emploi** : tenue sur une banque construite saine ; tombe sur un artefact « vérité par la grandeur du littéral » et sur un artefact « vérité par le gabarit » ; tombe (C4) sur un artefact « contre-exemple au plafond ».
- **Lecture** : C1 à C3 tenues → lecture en verdict ouverte ; sinon en description. C4 non tenue → lecture en preuve calculée, « gain ≥ 0,20 hors de portée » écrit d'avance. Intervalle à cheval : branche prudente.
- **Branches de la course** (à confirmer par Lazar, car il a écrit « ensuite, ils partent sur la version 6 » sans dire le cas d'une version 7 prête mais partielle) :
  - version 7 figée, certifiée et mesurée au plus tard le 2026-12-04T23:59Z, C1 et C4 tenues → bras sur la version 7 ; lecture en verdict si C2 et C3 tiennent aussi, sinon preuve seule ;
  - sinon (C4 non tenue, version 7 non prête, ou date dépassée) → bras sur la version 6, lecture en preuve seule, verdicts en description ; la version 7 passe au pilote 2.
  - recommandation : celle-ci, confiance 0,65 (la fuite d'instance est celle que la lecture en preuve emploie ; une version 7 qui ne la ferme pas n'achète rien de plus que la version 6).
- **Relecture de la banque réelle** : une valeur hors de la plage vue sur les racines neuves ferme la lecture en verdict, et c'est dit en tête du rapport.
- **Ajustement** : le concepteur peut ajuster les nombres par écrit, avant la première mesure de la version 7 ; tout ajustement est un écart nommé, porté à la mère.

## 4. Ce que la mère doit trancher (ou porter à Lazar)

1. Lecture de « rappel au plus de 10 % » : (i), (ii) ou (iii). Recommandation (i).
2. Branche « version 7 prête mais partielle » : recommandation au § 3.
3. Garder la troisième sonde (tenue à l'écart) : recommandation oui, retirable en premier avec ligne d'écart.
