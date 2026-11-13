# Vérification courte de la conception « monde riche et doublons » v2 — v1

- **Objet** : `conception-monde-riche-doublons-v2.md` (`af0d0e72927db409edf8a5ee0d348a93d5d7404409d61dde45a110d670524a5f`,
  vérifiée, égale à son compagnon), ses pièces `outils-v2/` et `sorties-v2/` (compagnons revérifiés : 10 outils et 35 sorties,
  tous justes), contre la contre-lecture v1 (`contre-lecture-conception-monde-riche-v1.md`, `e7d5cda0…`).
- **Demande** : message de la mère (session `session_01XJ6Mgn4MZR4nxqK44C8Ea3`), vérification courte. Mêmes interdits que la
  consigne `e77ccad0…` ; aucune écriture git ; aucun appel externe ; aucune dépense ; deux rejeux légers, un à la fois, sous
  `ulimit -v 6000000` et `OMP_NUM_THREADS=2`.
- **Réserve de lignée, à trancher par la mère** : après le redémarrage du conteneur, cette session tourne sur **Claude Opus 5.5**,
  le **même modèle que le concepteur**. La contre-lecture v1 était faite par Fable 5.2. N-052 demande un autre modèle ; cette
  vérification ne le tient pas. Je n'ai écrit ni la conception ni ses outils. Je recommande qu'un lecteur Fable relise au moins
  les points V-1 et V-5 avant le préenregistrement.
- **Heures** (`date -u`) : début 2026-11-13 00:25:38 ; rejeux 00:28:13 → 00:36:45 ; fin de rédaction 00:38:08.
- Écrits : ce rapport et son compagnon ; le reste dans
  `/tmp/claude-0/-home-user/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/cl-monde-riche-v2/`. Aucun refus de
  permissions ni de classifieur.

## Verdict

**Utilisable pour le préenregistrement après corrections** : les sept corrections exigées ci-dessous (V-1 à V-7).

Les douze corrections de la v1 sont appliquées sur le fond. Restent :
- un écart entre le texte et le code de la nouvelle règle du représentant (V-1) ;
- une affirmation fausse sur la graine de hachage (V-2), sans effet sur les chiffres ;
- deux renvois faux (V-3) et un décompte faux de m (V-4) ;
- une lecture trop forte du test « taille de l'archive » (V-5) ;
- deux points du devis et de Q-12 (V-6) ;
- un enjeu incomplet dans Q-11 (V-7).

## Corrections exigées

**V-1 — La « tranche de choix » n'est pas appariée dans le code.** Le §3.4 et la docstring de `monde_riche_outils_v2.py` décrivent
**une** tranche de 400 épisodes frais. Les trois appels de `representant_v2` (`puissance_monde_riche_v2.py`, l. 77, 165 et 262) tirent
au contraire une tranche **différente pour chaque candidat** (`rng_de(…, i)`). Deux lois sont donc comparées sur des épisodes
différents : la comparaison est bruitée sans nécessité.

Ce défaut explique sans doute les pertes restantes. Les 6 groupes à perte > 0,01 sont 3 situations, chacune comptée deux fois (six
variantes et paire), dans les mondes 6, 10 et 11 ; le cas le plus grave est une tempérée à 2,0 choisie contre la loi, perte
0,167 nat.

À faire :
1. Une seule tranche par groupe, la même pour tous les candidats ; le préenregistrement la fixe par la graine de la tâche du groupe.
2. Refaire `representant` avec cette règle.
3. Écrire dans la garde 25 que la tranche est recalculée à l'identique.
4. La proposition « 2 000 épisodes » ne vient qu'après l'appariement.

**V-2 — `PYTHONHASHSEED` n'est jamais fixé : `python3 -I` l'ignore.** Vérifié ici : avec `-I`, `PYTHONHASHSEED=0` et `=1` laissent
le hachage aléatoire. Le lanceur v2 lance tout par `python3 -I -B`. Sont donc fausses :
- « `PYTHONHASHSEED=0` fixé » (changements, ligne E-2 ; §1.6 ; journal) ;
- « rejouée sous la graine de hachage 1 » (§1.6) ;
- le champ `pythonhashseed` des JSON, qui recopie la variable d'environnement, pas la graine en vigueur.

**Le fond tient** : le déterminisme vient des parcours triés. Les deux lancements avaient des graines aléatoires différentes et rendent
des courses égales. Mon rejeu, avec une graine **réellement** fixée à 2 (sans `-I`), est égal champ pour champ aux quatre courses
scellées des mondes 0 et 1 (voir Rejeux). Correction de texte seulement : « déterminisme par parcours triés, établi sous trois
graines de hachage ». Le champ doit dire la graine en vigueur, ou être retiré.

**V-3 — Deux renvois faux.**
- §2.4 cite `sorties-v2/banc-generateur-w12-v2.json`. Ce fichier n'existe pas (vérifié sur disque) : la course a été coupée, seule
  la sortie vide `.stdout` existe. À retirer.
- §4.1 cite `sorties-v2/attribution-w12-v2.json` avec l'empreinte `3c4d00c8…`. Cette empreinte est celle de
  `sorties-v2/attribution-w12-v2b.json`, et le fichier sans « b » n'existe pas. À corriger.

Le reste tient : les 93 pièces du tableau sont justes, et les empreintes abrégées des §1.6, §2.3, §3.4, §3.6 et §6 aussi.

**V-4 — m = 44 ne correspond à aucun décompte écrit.**
- Le décompte donné (« 24 cartes, 13 vraies plantées au plus, 4 fausses, 4 copies, T-ELIM ») fait 45 ou 46 selon que T-ELIM est
  compté dans les 13 ou non (le §1.5 et le devis l'y comptent).
- Il oublie F5 et H1 (générations 2 et suivantes) ainsi que T-MAL.
- La règle de la v67 (m = cartes + plantées + instruments = 12 + 8 + 2 = 22) donne ici **48** : 24 cartes, 12 vraies, 4 fausses,
  4 copies, F5, H1, T-ELIM, T-MAL. Avec Kimi, **54**.

La validité d'e-BH n'est pas touchée : m reste au-dessus du nombre de cartes de la famille. Les seuils, eux, bougent un peu (+0,087 nat
au seuil hors famille à m = 48). À faire : écrire la règle de m et son décompte, avec et sans Kimi. Inutile de refaire les simulations,
le banc refait tout avec le code v68.

**V-5 — Le test « taille de l'archive » ne dit pas que le juge ne devient pas sourd.**
- Dans `_archive_monde`, l'archive contient **toujours W₋ᵢ** (le monde moins la composante i), plus k lois partielles bruitées que
  W₋ᵢ domine déjà.
- Ce test mesure donc seulement le coût d'ajuster le mélange sur plus de membres. C'est utile, et c'était une part de E-3.
- Il ne mesure pas la puissance contre une archive réaliste de génération 3, faite de lois partielles **sans** W₋ᵢ.

À restreindre : la phrase du §0, point 4 (« stable à 0,54 ») et la lecture du §1.6 (« pas de surdité dans le juge simplifié »). Le
§1.8 doit demander au banc des archives sans W₋ᵢ, faites des retenues simulées d'une génération 2.

**V-6 — Devis et Q-12 : deux points.**
1. « + 8 si les fausses et copies promues sont testées » oublie F5 : 9 lois, et 10 si H1 promue est testée (13 promotions sur 480 à
   n = 400). Le texte doit dire si H1 promue est testée. Par la même formule, Q-12 (b) passe de 435 à **445** sur crédits
   (T_pire = 46 : 6 × (5 + 46 × 1,50) = 444) ; le total au pire passe de 486 à environ 496.
2. Q-12 recommande (a) en invoquant « pas de non concluant par défaut de plafond » (devis v66 §5, citation vérifiée). Or la borne de
   1,50 USD par test d'Opus est elle-même un plafond, qui produit des « non concluants », et Opus n'a jamais été éprouvé dans ce rôle.
   Le dire dans Q-2 et Q-12 ; sinon la justification présentée à Lazar est inexacte.

**V-7 — Q-11 : l'enjeu oublie ce que la conception établit sur le latent.** Q-11 recommande (c), un trait latent obligatoire.
- Le §4.1 établit qu'une loi prédictive ne « capte » presque jamais une composante latente (4 sur 23), et que D2 l'exclut.
- Un latent obligatoire ajoute donc à chaque monde une composante qu'aucun proposeur ne peut trouver et qu'aucune mesure principale
  ne compte ; il abaisse aussi le gain du monde.

L'enjeu et les inconvénients de (b) et (c) doivent le dire, puisque c'est Lazar qui tranche.

## Corrections suggérées

- **T-1** Écrire que les « 6 groupes » de pertes du §3.4 sont 3 situations comptées deux fois.
- **T-2** Le cas central suppose 6 représentants testés par génération, contre 9,2 promus en génération 1 dans la simulation v2. Le
  central attendu est un peu bas (environ +4 USD à 2 × 3).
- **T-3** Pire cas : écrire la règle des reprises d'un appel de proposeur (aucune reprise, ou reprise comptée). Le pire cas suppose
  un seul appel par proposeur et par génération.
- **T-4** C8 v2 : dire que « moyenne de puissance ≥ 0,5 » **remplace** la règle « indétectable : refus » de la v1.
- **T-5** `mesurer_fuite` laisse un fichier ouvert (avertissement aux essais) : sans effet, à nettoyer dans le code v68.

## E-1 à E-12 et S-1 à S-9

| | appliquée à la lettre ? | remarque |
|---|---|---|
| E-1 | oui sur la règle (couverture dirigée, phrase fausse retirée, sort du groupe, simulations refaites) | code non apparié : V-1 |
| E-2 | oui sur le fond (parcours triés, rejoués égaux) | graine de hachage jamais fixée : V-2 |
| E-3 | oui (règle de n écrite, intervalles avec le nombre de lois distinctes, banc avec code v68) | m : V-4 ; archive : V-5 |
| E-4 | oui (toutes les simulations v2 tirent du générateur v2 ; seuils déclarés réglés en v1) | — |
| E-5 | oui (latent à part, taille et poids tirés, règles de C8 codées, fréquences rapportées) | T-4 |
| E-6 | oui (dix régularités classées ; code conforme à la table) | — |
| E-7 | oui (C7 en mesure ; refus seulement à six décimales ; essai sur 14 nombres ordinaires sans refus) | — |
| E-8 | oui (trois hypothèses écrites ; α non repris ; Q-9) | — |
| E-9 | oui (pire cas par formule, replantation, tests de Kimi, borne par expérimentateur, Q-12) | V-6 |
| E-10 | oui (Q-8 sur le mot R-2443) | — |
| E-11 | oui (200 graines, borne basse de Wilson ≥ 0,8, libellé) | — |
| E-12 | oui (garantie de procédure, engagement poussé avant la phrase, hors dépôt, empreinte corrigée) | — |

S-1 à S-9 : reprises sans risque.
- Les choix ouverts par S-1 et S-8 sont tranchés au banc de calibration, sous la règle de changement du §1.8 (nouveau secret).
- La liste blanche de S-7 compare des chemins réels.

## Devis et questions

- **Pire cas 409 USD** à 2 × 3 : juste par la formule et sous ses hypothèses (vérifié : 6 × (9 + 37 × 1,60) = 409,2 ; crédits
  363 ; hors crédits 34,2 + 12 + 10 = 56,2, arrondi à 57). Les variantes Kimi (417 et 475,8), 1 × 3 et 3 × 3 sont justes aussi.
  Il est complet à V-6 et T-3 près.
- **Q-1 à Q-12** : formes justes. Corriger Q-12 et Q-2 (V-6) et Q-11 (V-7).
- **Aucune question ne manque** pour Lazar, à une exception près : la réserve de lignée de cette vérification, qui relève de la mère.

## Rejeux (interpréteur système, Python 3.13.18, numpy 2.5.3 ; un processus ; sorties dans `rejeux/` de mon bac)

| sortie scellée | rejeu | résultat |
|---|---|---|
| `generations-w12-g3-n400-v2.json` | mondes 0 et 1, deux conditions, graine de hachage **effective** 2 (sans `-I`) ; `803d7a00…` | les 4 courses égales champ pour champ |
| `representant-w12-v2.json` | complet, 12 mondes, graine de hachage effective 3 ; `0308ffaf…` | champ `resultat` égal |

Les chiffres des §1.6, §2.4, §3.4, §3.6, §4.1 et §6 recopient fidèlement leurs sorties : représentant, doublons, archive, détection,
générations, attribution v2b, banc, fréquences et devis, contrôlés champ par champ.
