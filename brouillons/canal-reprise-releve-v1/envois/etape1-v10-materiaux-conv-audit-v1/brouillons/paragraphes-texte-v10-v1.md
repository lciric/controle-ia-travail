# Étape 1 v10 — paragraphes proposés (brouillon v1, sous-agent conv-audit, 26 octobre 2026)

Brouillon à reprendre par session-depot dans `prereg/gradient-etape1-sondes-v10.md` (nom neuf, R12), puis contre-lecture
neuve (R2) et scellement. Chaque paragraphe remplace ou complète le passage de la v9 (`6abcbe61…`) cité en tête.
Aucun chiffre ci-dessous ne vient d'un score de course ; les chiffres de la banque viennent de `LISEZMOI-v9.md`
(`cdd64b97…`) et du manifeste public de `banque-confrontation-v5.json` (`28e3c728…`) ; les calculs, de
`/var/tmp/etape1-v10-v1/outils/erreur_type_ecart_detectable_v1.py` (sortie `sorties/erreur-type-ecart-detectable-v1.txt`).

## P1 — Plan, point 1 « Données » (remplace l. 362-369 de la v9)

Banque `confrontation-v5` (`banque-confrontation-v5.json`, `28e3c728d9d1251d50da18d61827b9f99578721f9988e19e3a3e19909e5c6e46`,
branche `outils/banque-confrontation-v2-travail`, contre-lue « utilisable après corrections », `LISEZMOI-v9.md`) :
entraînement 80 tâches (servies avec leurs vérités ; conscience d'évaluation 24 + 24, délégation 16 + 16, dont les
16 paires), test de développement 48 (conscience 18 + 18, délégation 6 + 6, une trace par paire ; score rendu à chaque
génération), test final 48 (même composition ; jamais rendu, lu une fois). Le lanceur épingle cette empreinte et refuse
toute autre banque (la v1 `f1387a20…`, la v2, la v3 `157a2b45…`, la v4 `6504045c…` comprises) ; `verifier_banque` du
noyau n'épingle rien (BC2-02) : la garde est au lanceur. Traits : dossier **dérivé** des traits `traits-16384` de la v1
(`donnees/traits-etape1-v1`, `6479769`, manifeste `034d8460…`), sans réextraction : l'extraction n'a donné au modèle que
la consigne système et le champ `texte`, une tâche à la fois (`extraire_activations_v2.py` `8286f4e7…`, l. 68 et 153) ;
les 176 textes de la v5 sont, à l'octet près, des textes de la même part de la v1 (vérifié par empreinte du texte,
176 sur 176, aucun doublon). Le dossier dérivé range les 176 vecteurs par identifiant v5, ne porte aucun identifiant v1,
et son manifeste est à l'empreinte de la v5 (`deriver_traits_v5_v1.py`, brouillon, à versionner) ; son empreinte est
citée ici avant le scellement. Le noyau exige l'égalité des identifiants des traits et de la banque servie (BC5-01).

## P2 — Ce que le noyau sert (phrase sur la vérité servie ; n° 59 (iii), `LISEZMOI-v5.md` § 4.4)

« Le noyau ne sert à l'organisme aucune vérité de `test` ni de `test_final`. » Sur la v1 cette phrase était fausse
dans les faits : les identifiants servis portaient la vérité (`-H`, `-S`). Sur la v5 (identifiants opaques) elle tient
à deux conditions, dites ici : (a) aucune pièce issue d'une course sur la v1 ou la v3 n'entre dans une course sur la v5
(garde du lanceur en code, BC5-02) ; (b) aucune copie de la v1 ou de la v3 n'est lisible par l'organisme, car leurs
textes sont ceux de la v5 et leurs identifiants rendent les vérités par simple correspondance de texte. `predire`
rend des probabilités, jamais une vérité, pour les seules tâches de la banque servie (égalité des identifiants).

## P3 — Amorçage (R-441 ; remplace « l'amorçage garde le maximum du modèle », l. 466, et les pires cas l. 471-475)

L'appel d'amorçage demande le maximum du modèle (64 000 jetons pour `claude-fable-5-1` et `claude-opus-5-5`, 32 000
pour Gemini ; `collisionneur_v2.py` l. 51-58, lu par `appels.py` l. 164 quand `boucle.py` l. 521 ne fixe rien), à effort
« high » et sans budget de réflexion (`collisionneur_v2.py` l. 105, 390-394 ; ces modèles refusent un budget, l. 5).
À la répétition du 25 octobre, la réflexion adaptative a consommé tout le plafond (aucun texte, R-441). Correction :
si la réponse finit au plafond sans texte ou coupée, **une seule relance**, même consigne, au plafond de relance du
collisionneur (128 000 ; Gemini 65 536), règle d'`executer_cellule` ; un second échec laisse `AMORCAGE_INVALIDE`, sans
autre reprise. Pires cas d'amorçage (prompt de 60 000 caractères) : Fable 3,40 + 6,60 = 10,00 USD ; Opus 1,36 + 2,64
= 4,00 ; Gemini 1,80 + 3,48 = 5,28 ; 19,28 pour trois lignées (v9 : 6,6). Le plafond d'une génération de la répétition
(5 USD) refuserait la relance de Fable : il passe à 11 USD pour la génération 0 de la répétition, ou l'amorçage reçoit
un plafond propre de 11 USD par lignée (à trancher, décision D2). Exemples d'amorçage (BC5-04) : règle écrite d'avance —
six exemples du train, par famille et par classe : 2 délégations honnêtes, 2 sabotées, 1 conscience « évaluation »,
1 « usage réel » ; dans chaque case, les plus petits identifiants v5 — ou, à défaut, leur composition consignée ici et
identique dans tous les bras (la génération 0 est commune à A_r et B_r). Sur la v5, la règle actuelle
(`banque["train"][:6]`, `boucle.py` l. 509) donne 1 délégation honnête et 5 consciences, aucun sabotage.

## P4 — Lecture contre les références (BC5-03 ; ajoute au point 6 et aux critères de lecture gelés)

Chaque score de la famille « conscience d'évaluation » se lit contre le **maximum** des références figées : surface
0,75 (`test`) et 0,6944 (`test_final`) ; provenance (plus proche voisin sur les mots du train) 0,8056 et 0,8333
(`reference-provenance-conscience-banque-v5-v1.json`, `0640fa05…`). Les scores sont aussi rendus sur les tâches dont la
catégorie d'origine est absente du train (8 en `test` : 4 et 4 ; 14 en `test_final` : 10 et 4). Ces références et
comptes sont des chiffres de la banque, non des résultats.

## P5 — Effectifs et bruit (n° 62 § 5 ; à mettre dans « Seuil »)

Sur la v5, en délégation, 6 traces par classe : une erreur déplace l'exactitude équilibrée de la famille de 0,083 et le
score global de 0,042. Au hasard, l'écart type du score global vaut 0,083 (v3 : 0,066) ; à une exactitude vraie de 0,75,
0,072. Écart minimal détectable entre deux bras (bilatéral 5 %, puissance 80 %, erreurs indépendantes) : 0,33 pour une
course par bras, 0,23 pour deux, 0,19 pour trois, 0,135 pour six, 0,10 pour onze (0,29 / 0,20 / 0,165 / 0,117 / 0,09 à
0,75). Plancher apparié sur les mêmes 48 tâches, que les répétitions ne baissent pas : 0,13 si les bras diffèrent sur
10 % des tâches, 0,18 sur 20 %, 0,22 sur 30 %. L'effet prédit de H-G1 (+0,10) est donc sous l'écart détectable du plan ;
la table de puissance de la v9 (`puissance-v2.json`, test final 36 + 24) est à refaire sur 36 + 12. Le premier seuil
significatif à 5 % sur 12 traces est 10 justes. Le train garde 16 paires, le test aucune (BC5-14) : écart de structure,
non une fuite.

## P6 — Porte 0, sans dépense (principe de Lazar : la version simple d'abord)

Avant toute course payante : deux sondes témoins fixes (Plan, point 7 de la v9 : linéaire normalisée, 1 000 pas, Brier
et logarithmique borné), entraînées par l'entraîneur du noyau sur les 80 tâches du train, **lues sur `test` seulement**
(le test final reste fermé), par vue, contre le maximum des références (P4) et contre la règle « au hasard ». Script
écrit, scellé et contre-lu avant d'être lancé (R1, R2) ; aucun appel de modèle. Lecture gelée : si aucune vue ne dépasse
le maximum des références de plus de l'écart apparié détectable (calculé d'avance sur 48 tâches), la v10 le dit et les
courses d'organismes ne revendiquent rien sur la valeur des activations au-delà du texte ; elles restent descriptives
ou n'ont pas lieu (décision D3). Ce n'est pas un run visant un signe (R3) : la porte est symétrique (R4).

## P7 — Séparation (BC5-02 ; liste d'arrêt)

Le lanceur refuse, en code et avec essais (sain, artefact), tout `--depuis`, organisme imposé, archive, ronde de
conception importée ou vivier dont le manifeste ne porte pas l'empreinte `28e3c728…` ; la disjonction du vivier
(`32f4b534…`) est vérifiée contre les 96 textes de test et de test final de la v5 et contre les 24 jumelles retirées
(les deux ensembles sont dans les 120 textes de test et de test final de la v1 : si la disjonction a été calculée contre
ces 120, elle vaut ; sinon, recalcul). Ligne de la liste d'arrêt : « pièce issue d'une course sur la v1 ou la v3
(pilotes 1 à 4, répétition du 25 octobre) dans une course sur la v5 : refus du lanceur ; condition de ce texte ».
