# Chemin critique du second cycle de la lecture « accumuler les scores de sondes sur l'épisode » — v1

- **Pour** : Lazar et la session mère. **De** : planificateur neuf (Claude Opus 5.5), sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1` ; aucun rôle de rédaction, de lecture ni de jugement dans ce cycle. **Date (UTC)** : 2026-11-18, vers 21:30.
- **Objet** : dire si un résultat, au moins intermédiaire, du second cycle peut exister avant l'entretien du 27 novembre, et comment. **Planification seulement** : aucun seuil, aucun critère d'analyse, aucune donnée d'expérience ; rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`.
- **Textes servis** (empreinte vérifiée contre son compagnon) : `points-a-trancher-cycle-2-v1-brouillon3.md` (`1999a6ded7bfdcdc0f29bc1c940873903dc2a15c5c5a8b9f7ca795f0a15890ac`), `ordre-exploratoire-temps-1-v1-brouillon3.md` (`af4cb7fb2e206c9f40137614f485acc5ec67e51c510f476a6a86b2ef2ee5ac60`), `devis-cycle-2-v1-brouillon2.md` (`065057f04fa67a55a5f370d782baf8ed738e2b4849bd69427805548608913088`), tous trois dans ce dossier ; `registres/go.md` lignes GO-2026-11-18-49 à -57 (fichier lu à `01f676f2…`, commit `036308b39`).
- **Calcul** : `pieces-chemin-critique-v1/chemin_critique_cycle_2_v1.py` et sa sortie `pieces-chemin-critique-v1/sortie-chemin-critique-cycle-2-v1.txt` (empreintes dans leurs compagnons) : passe avant et arrière sur le graphe, puis 20 000 tirages triangulaires par scénario (graine `SeedSequence(20261118)`, numpy 2.4.6).

---

## 1. Verdict

1. **Avec ce qui est déjà décidé** (validité de l'adaptateur levée par GO-2026-11-18-58, deux machines permises par le plafond de 275 USD de GO-2026-11-18-56), le verdict de la confirmation tombe, au milieu des tirages, vers le **28 novembre** ; il tient avant le 25 à 18:00 dans environ **2 %** des tirages, avant le 27 à 00:00 dans environ **19 %**. La phrase « peu probable » est juste.
2. **Ce qui peut exister avant le 25** : le texte de la confirmation scellé avec la sonde gelée, et leurs empreintes déposées chez un tiers. C'est un **résultat intermédiaire vérifiable du dehors**, sans aucun chiffre de l'hypothèse. Il arrive avant le 25 à 18:00 dans environ **69 %** des tirages, et presque toujours si le temps 1 est borné à 48 heures.
3. **Trois levées** de dépendances de prudence, chacune un nœud qui te revient, portent la chance d'un verdict avant le 27 à environ **83 %**, et avant le 25 à 18:00 à environ **39 %**. La plus forte est de générer la famille pendant le temps 1, sorties scellées fermées. La moins chère est de borner le temps 1. **Le geste du jour, quel que soit ton choix** : lancer tout de suite la piste des tâches fraîches. Les compteurs du premier tirage, que le devis disait illisibles, sont écrits dans des messages de commit (section 3.4).

---

## 2. Ce qui a changé depuis les points à trancher (brouillon 3)

- **Tes décisions** (GO-2026-11-18-56, mot « go autres recos ») : nœuds 1 (b), 2 (a) mode « coût » rejoué, 4 (oui, 75 USD, disque de 250 Go si une offre tient le prix, sinon couche par couche), 5 (a) 275 USD, 6 (b), 7 (empreintes seules, bras d'attaque oui, second modèle reporté), 8 (a) extraction à devis. Propositions 9 à 14 telles qu'écrites. Le nœud 3 reste ouvert, mais il porte sur la porte de fin de phase 1 et ne touche pas ce chemin.
- **Lecture de l'apprentissage des sondes sur la tâche (étape B bis)** : elle repart par un quatrième addendum d'écart (égalité à la seconde des lignes `GO-BBIS` et `CODE-BBIS`), puis par un module de lecture sous un nom neuf. Aucune lecture avant le scellement de l'addendum et sa contre-lecture (GO-2026-11-18-56, point 1).
- **Hors du mandat, déclaré** : GO-2026-11-18-58 (21:16Z) **lève déjà** la condition « verdict de la validité de l'adaptateur » à l'ouverture du temps 1. La table conjointe reste exigée.
- **État des registres** (clés et heures seulement) :
  - registre propre de l'étape B bis : `SCELLEMENT-BBIS` et `ABSENCE-B-BBIS` le 2026-11-14 à 12:30:30Z ; `CODE-BBIS` le 2026-11-16 à 12:57:27Z, puis le 2026-11-17 à 11:05:29Z ; `GO-BBIS` le 2026-11-17 à 11:05:29Z ; `SCORES-BBIS` le 2026-11-18 à 19:43:48Z. **Manquent** `LECTURE-BBIS`, `VERDICT-BBIS` et `CONJOINTE-BBIS`, dans cet ordre (texte scellé de l'étape B bis, l. 99).
  - registre propre de la validité de l'adaptateur : `SCELLEMENT-VADAPT` le 2026-11-14 à 09:45:18Z, **seule ligne** ; ni code, ni ligne de GO, ni course.
  - registre des scellements (hors mandat, déclaré) : `VERDICT-T07-ETAPE-B` le 2026-11-17 à 11:20:08Z. Le verdict de la lecture des sondes (étape B) est donc scellé.
- **Date utile** : GO-2026-11-18-30 écrit « résultats prêts le 24 ou le 25 novembre pour l'entretien du 27 » (hors mandat, déclaré). Les calculs gardent deux échéances : **le 25 à 18:00Z** et **le 27 à 00:00Z**.

---

## 3. Données brutes : durées mesurées et leurs sources

Ce sont des horodatages de registre et de commit sur la branche principale distante (`origin/main`). Ce sont des durées écoulées, nuits et attentes comprises. Aucune n'est une durée de travail pur.

### 3.1 Textes du premier cycle (rédaction, contre-lecture, code, scellement)

| segment | début → fin | durée | source |
|---|---|---|---|
| brouillon 1 → contre-lecture 1 | 2026-11-10 16:10:44 → 16:28:25 | 0,3 h | commits `8e907c89`, `a223075a` |
| brouillon 1 → brouillon 2 | 16:10:44 → 17:07:25 | 0,9 h | `101b458e` |
| brouillon 2 → code v1 rendu | 17:07:25 → 18:54:08 | 1,8 h | `2d5d60c8` |
| brouillon 2 → ligne `CODE-ACCB6` | 17:07:25 → 2026-11-11 12:51:23 | **19,7 h** | registre propre du premier cycle |
| arrêt de nuit dans ce segment | 2026-11-10 22:05:52 → 2026-11-11 07:44:56 | 9,7 h | `005dca55`, `4f6e5cf3` |
| brouillon 1 → `SCELLEMENT-ACCB6` | 2026-11-10 16:10:44 → 2026-11-11 13:10:34 | **21,0 h** (11,3 h hors nuit) | registre propre |
| mandat de l'opérateur → `LECTURE-ACCB6` | 2026-11-18 16:15:17 → 17:12:58 | 1,0 h | `77d55971` ; registre propre |
| `LECTURE-ACCB6` → verdict versé | 17:12:58 → 17:32:31 | 0,3 h | `9a5e50c8` (noms de fichiers seulement) |

### 3.2 Textes du second cycle

Du brouillon 1 (2026-11-18 18:35:44) aux brouillons 3 (19:41:48), deux contre-lectures et une vérification comprises : **1,1 h**. Source : commits du dossier, de 18:35:44 à 19:41:48.

### 3.3 Apprentissage des sondes sur la tâche (étape B bis) et lecture des sondes (étape B)

| segment | début → fin | durée | source |
|---|---|---|---|
| troisième addendum : brouillon 1 → scellé | 2026-11-18 04:02:38 → 05:46:36 | **1,7 h** | `081f8d99`, `438a9c52` |
| second addendum, son code et sa contre-lecture | 2026-11-17 02:39:51 → 04:43:13 (essais 05:46:08) | 2,1 à 3,1 h | `6467b922`, `30151693`, `5378c2de` |
| `SCELLEMENT-BBIS` → `SCORES-BBIS` | 2026-11-14 12:30:30 → 2026-11-18 19:43:48 | **103,2 h** | registre propre |
| première répétition sur carte → `SCORES-BBIS` | 2026-11-14 23:46:47 → 2026-11-18 19:43:48 | 92,0 h | registre des dépenses, l. 460 à 523 |
| échecs de lancement | clonage refusé (23:48:43Z) ; « torch ne voit pas la carte » (2026-11-15 07:29:55Z) ; contrôle carte-processeur, code 9 (08:34:03Z) ; ligne de création refusée par le classifieur (23:53Z) | — | dépenses, l. 461, 464, 468, 471 |
| course arrêtée du 16 novembre | 17:25:30 → 21:39:14 | 4,23 h | dépenses, l. 482 |
| `GO-BBIS` → départ de la course | 2026-11-17 11:05:29 → 2026-11-18 15:44:24 | **28,6 h** | registre propre ; dépenses, l. 523 |
| marche de la course | 15:44:24 → 19:42:12 | **3,96 h**, 4,69 USD | dépenses, l. 523 |
| étape B : `SCORES-T07` → `VERDICT-T07-ETAPE-B` | 2026-11-14 01:55:05 → 2026-11-17 11:20:08 | **81,4 h** (lecture, audit des fuites et verdict) | registre des scellements (clés et heures) |

### 3.4 Tâches fraîches : le premier tirage, octobre

Ces compteurs sont écrits dans les messages de commit. Le devis les disait illisibles.

| grandeur ou segment | valeur | source |
|---|---|---|
| règle de sélection scellée → run de sélection versé | 2026-10-06 13:42:24 → 14:07:13 : **0,4 h** | `ea08b9c0`, `d90445c6` |
| compteurs de la sélection | **3 405 entrées, 1 836 candidats (53,9 %), 125 papiers examinés, 96 gardés (76,8 % des examinés), 29 exclus par la chaîne (28 échecs de conversion, 1 délai)** | `d90445c6` |
| procédure d'extraction : brouillon 2 → scellée | 2026-10-06 19:23:42 → 2026-10-07 07:17:57 : **11,9 h** (trois contre-lectures et une vérification) | `812212dc`, `971725e8` |
| première vague, bloquée | 14 papiers sur 96, puis arrêt : 4 lancements de sous-agents sur 7 refusés par le classifieur | `3e845c5b` (16:14:06) |
| reprise après réglage des permissions par Lazar → tentative finie | 22:17:30 → 23:13:42 : **82 papiers en 0,94 h, soit environ 88 papiers par heure** | `535d54db`, `e4bb4e95` |
| papiers invalides à la première tentative | **0 sur 96** (le devis supposait 10 à 30 %) | `e4bb4e95` |
| contre-vérification | arrêtée par la **limite d'usage hebdomadaire du compte** à 11 avis sur 16 (2026-10-08 03:10:53) ; reprise le 10 octobre vers 15:10, lue à 15:18:32 ; 0 échec sur 16 | `e15de30a`, `d0125248` |
| procédure scellée → environnement assemblé | 2026-10-07 07:17:57 → 2026-10-10 15:19:42 : **80,0 h** pour 96 papiers, dominées par les deux blocages | `b12a94a2` |

**Faisabilité, à recompter par la session mère** (arithmétique sur ces compteurs) : si la requête rend le même ensemble, il reste 1 836 − 125 = **1 711 candidats**. Au rendement observé, ils donnent environ 1 314 papiers gardés, soit 1,7 fois les 760 visés. Il faut en examiner environ 990. **Réserve** : la requête d'aujourd'hui peut rendre un autre ensemble, et le taux d'échec de conversion (22 % des examinés) commande le nombre de papiers examinés.

### 3.5 Créations d'organismes et autres courses (durées de location)

| course | durée | source |
|---|---|---|
| course exploratoire de dose-réponse des organismes, seconde tentative | 2026-11-09 06:25:36 → 20:06:53 : **13,69 h** ; première tentative le 2026-11-08 vers 17:05, d'où environ 13 h entre deux tentatives | dépenses, l. 408 et 413 (heures seulement) |
| course de confirmation des organismes | 2026-11-11 14:19:58 → 2026-11-12 05:18:03 : **14,97 h** | dépenses, l. 421 (heures seulement) |
| course d'auto-conception de l'organisme d'idéation | accord vers 10:20Z ; départ vers 17:19 (nom du dossier `20261118-171908-…`) ; close à 19:30:13 : **2,2 h de marche, environ 7 h d'attente** (épreuve des témoins échouée, reprise) | dépenses, l. 519 et 522 ; GO-2026-11-18-20, -36, -39 |

**Recoupement du devis** (calcul de ce texte, qui n'est pas une mesure) : pour 64 tâches, le modèle du devis donne une pièce de génération d'environ 12,5 à 13,6 h. Les deux courses réelles comparables ont loué la carte 13,69 et 14,97 h, relectures et poussées comprises, soit 1,0 à 1,2 fois ce modèle. **Le devis paraît juste à 10 à 20 % près sur la marche.** Le risque est ailleurs : dans le lancement. Il a fallu 13 h, puis 28,6 h, puis 92 h de répétitions selon la course.

---

## 4. Tableau des étapes

Les durées sont écoulées, en heures (basse / probable / haute). La colonne « dépend de » distingue :

- **réelle** : la logique l'impose ;
- **règle** : un texte ou une décision l'impose ;
- **prudence** : levable par un nœud, avec ce que la levée coûte en garde (section 7).

| étape (repère) | dépend de | durées | source des durées | avant l'ouverture ? |
|---|---|---|---|---|
| quatrième addendum de l'étape B bis : rédaction, contre-lecture, scellement (E1) | — | 1,5 / 3 / 10 | 3.3 (1,7 h ; 2,1 à 3,1 h) ; haut = une nuit (3.1, 9,7 h) | oui (autre session) |
| module de lecture neuf de l'étape B bis : code, essais, contre-lecture (E2) | — (en parallèle de E1) | 2 / 6 / 18 | 3.1 (code : 1,8 h pour v1, 19,7 h jusqu'à la ligne de code) | oui |
| lecture de l'étape B bis par un lecteur neuf, sur processeur (E3) | E1, E2 — **règle** (GO-2026-11-18-56) | 0,5 / 2 / 12 | 3.1 (1,0 h) | oui |
| verdict de l'étape B bis par un agent neuf (E4) | E3 — **règle** (R13) | 0,3 / 3 / 69 | 3.1 (0,3 h) ; haut : E3 et E4 ensemble = 81,4 h, durée mesurée de l'étape B (3.3) | oui |
| table conjointe (E5) | E4 — **règle** (texte scellé de l'étape B bis, l. 99) ; exigée à l'ouverture : **prudence** (GO-2026-11-18-58) | 0,5 / 2 / 8 | non mesurée ; code `conjointe_v2.py` déjà versé (`a95537f9`) | oui |
| ordre exploratoire : marqueurs remplis par la mère, contre-lu, scellé (P1) | — | 1 / 3 / 8 | 3.2 (1,1 h) | **oui, aujourd'hui** |
| recette de la famille, par une instance aveugle, mode « coût » rejoué, scellée fermée (P2) | décision 2 (a) — faite | 2 / 5 / 12 | 3.1 et 3.2 (supposé court, mode connu) | **oui, aujourd'hui** |
| code de la relecture complémentaire, repris de la chaîne de l'étape B bis (P3) | — | 2 / 5 / 12 | 3.3 (second addendum et son code, 2 à 3 h) | **oui, aujourd'hui** |
| **ouverture du temps 1** (OUV) | E5, P1, P2 — **règle** (ordre, conditions 1 à 3) ; la validité de l'adaptateur est levée (GO-2026-11-18-58) | 0,1 / 0,25 / 1 | — | — |
| textes du tirage complémentaire et de l'extraction à l'échelle, contre-lus, scellés (F1) | proposition 13 — faite | 3 / 8 / 16 | 3.4 (11,9 h) | **oui, aujourd'hui** |
| devis de l'extraction et ligne de GO (F2) | F1 — **règle** (décision 8 (a)) | 1 / 4 / 24 | haut : ton délai de réponse après la fin de l'autonomie (2026-11-19 à 09:06:42Z) | devis oui ; ligne sur ton mot |
| run de sélection complémentaire (F3) | F2, P2 (la recette porte la règle du tirage et l'entropie) — **réelle** | 0,3 / 1 / 3 | 3.4 (0,4 h) | oui |
| extraction d'environ 760 papiers (F4) | F3 — **réelle** | 8 / 14 / 80 | 3.4 : 88 papiers par heure, donc 8,7 h ; haut = 80,0 h mesurées en octobre (classifieur, limite hebdomadaire) | oui |
| contre-vérification, assemblage, liste scellée fermée `TACHES-ACC2` (F5) | F4 — **réelle** | 1 / 3 / 12 | 3.4 (minutes une fois débloquée) | oui |
| relecture complémentaire sur carte : lancement, marche, poussée, destruction (T1) | OUV — **prudence** (ligne de GO proposée, devis § 10) ; P3 — réelle | 4 / 8 / 30 | devis § 6 (3,6 à 9,3 h de marche) ; 3.3 (3,96 h ; `GO-BBIS` → départ, 28,6 h) | non (levée E) |
| conception et gel de la sonde, épreuve plantée du développement, simulation de puissance (T2) | T1 — réelle | 24 / 48 / 168 | ordre § 8 (sept jours au plus) ; points à trancher, C (un jour au moins) ; **non mesurée** | non |
| clôture `SONDES-ACC2` (SONDES) | T2 ; F5 strictement avant — **règle** (ordre, condition 2) | 0,1 / 0,25 / 1 | — | — |
| code de la chaîne de confirmation : génération à lots poussés et garde de débit, relecture à texte égal, notation, lecture, épreuve plantée, simulation ; essais sur jouets ; contre-lecture (C1) | — | 16 / 36 / 72 | 3.1 (19,7 h pour un code plus petit) ; points à trancher, C (deux jours) | **oui, aujourd'hui** |
| bras d'attaque, agent neuf qui lit la recette (AB) | P2 — réelle ; avant la création — **règle** (décision 7 (ii)) | 4 / 12 / 48 | **non mesurée** | oui, après P2 (petite dépense) |
| le code rejoue l'épreuve sur la sonde gelée ; dernière contre-lecture ; `SCELLEMENT-ACC2` (S1) | SONDES, C1, AB — **règle** (proposition 9) | 2 / 6 / 24 | 3.1 (de `CODE-ACCB6` au scellement, 0,3 h) ; points à trancher, C | non |
| gestes avant création : ligne d'engagement, dépôt daté des empreintes chez un tiers (G1) | S1 — **règle** (ligne proposée « seulement après `SCELLEMENT-ACC2` ») | 0,5 / 4 / 24 | non mesurée ; ton geste | non |
| création de la famille (FAM) : une machine à 400 tâches / **deux machines à 400** / deux machines à 600 | G1 — réelle (proposition 9) | 53/60/120 ; **30/40/80** ; 45/54/108 | devis §§ 4, 5 et 9 ; 3.5 (recoupement à 10 à 20 % près) ; haut = hôte deux fois plus lent | non |
| validité de la famille, épreuve plantée sur ses données honnêtes, lecture, sur processeur (L1) | FAM — réelle | 4 / 12 / 24 | points à trancher, C ; 3.1 (lecture en 1 h) | non |
| verdict par un agent neuf (V1) | L1 — règle (R13) | 0,3 / 8 / 24 | 3.1 (0,3 h) ; points à trancher, C | non |

---

## 5. Chemin critique et marges

**Scénario de référence** : ce qui est décidé, avec deux machines. Le chemin critique, dans 82 % des tirages :

> module de lecture neuf de l'étape B bis → lecture → verdict → table conjointe → ouverture → relecture complémentaire → conception et gel → `SONDES-ACC2` → scellement → gestes → création de la famille → lecture → verdict.

Dans 16 % des tirages, c'est le quatrième addendum qui précède la lecture, plutôt que le module. **Les tâches fraîches ne commandent le délai que dans environ 1 % des tirages, si elles partent aujourd'hui.**

**Marges au rythme probable**, comptées pour un verdict le 25 à 18:00 :

- **25 h** sur tout le chemin critique ;
- 35 h pour l'ordre exploratoire ;
- 33 h pour la recette et pour le code de la relecture ;
- 64 h pour les tâches fraîches ;
- 58 h pour le code de la chaîne ;
- 78 h pour le bras d'attaque.

**Pourquoi le « probable » ment.** La somme des durées probables donne un verdict le 24 à 17:00. La médiane des tirages, elle, le place le 28 à 08:45. La différence ne vient pas d'une erreur : les étapes non mesurées ont une queue longue. La conception de la sonde va de 24 à 168 h ; le verdict de l'étape B bis peut monter à 69 h. Les dates de bascule (section 9) sont donc calculées sur le rythme probable, puis sur le rythme bas : ce sont les **dernières** dates permises, pas des prévisions.

---

## 6. Scénarios

Les dates sont en UTC ; P10 / P50 / P90 sont les quantiles des tirages. « Scellé » signifie texte de la confirmation scellé avec la sonde gelée (`SCELLEMENT-ACC2`).

| scénario | ouverture, P50 | scellé, P50 | verdict, P10 / P50 / P90 | verdict avant le 25 à 18:00 | verdict avant le 27 à 00:00 | scellé avant le 25 à 18:00 |
|---|---|---|---|---|---|---|
| **sans levée** (validité de l'adaptateur exigée) | **non datable** : son registre ne porte que `SCELLEMENT-VADAPT` ; ni code, ni GO, ni course | — | — | ≈ 0 | ≈ 0 | ≈ 0 |
| **A** — avec la levée (GO-2026-11-18-58), une machine, 400 tâches | 20 nov. 12:55 | 24 nov. 20:53 | 27 nov. 13:45 / 29 nov. 13:16 / 1er déc. 22:43 | 0,001 | 0,039 | 0,69 |
| **B** — A + deux machines, 400 tâches (permis par le plafond de 275 USD) | 20 nov. 12:47 | 24 nov. 21:07 | 26 nov. 12:21 / 28 nov. 08:45 / 30 nov. 17:59 | 0,024 | 0,186 | 0,69 |
| **B6** — B à 600 tâches | 20 nov. 12:55 | 24 nov. 21:08 | 27 nov. 05:45 / 29 nov. 04:21 / 1er déc. 12:57 | 0,003 | 0,070 | 0,69 |
| **E** — B + relecture complémentaire jouée avant l'ouverture, scellée fermée (nœud) | 20 nov. 12:50 | 24 nov. 06:59 | 26 nov. 00:36 / 27 nov. 19:17 / 30 nov. 02:27 | 0,061 | 0,298 | 0,80 |
| **D** — B + génération de la famille pendant le temps 1, scellée fermée, 600 tâches (nœud) | 20 nov. 12:55 | 24 nov. 20:23 | 25 nov. 16:29 / 27 nov. 02:49 / 29 nov. 02:54 | 0,111 | 0,463 | 0,70 |
| **BT** — B + temps 1 borné à 48 heures (nœud) | 20 nov. 12:33 | 23 nov. 03:45 | 25 nov. 12:31 / 26 nov. 15:44 / 27 nov. 23:10 | 0,160 | 0,631 | ≥ 0,99 |
| **BDE** — B + D + E | 20 nov. 12:52 | 24 nov. 07:46 | 25 nov. 10:53 / 26 nov. 19:04 / 28 nov. 13:19 | 0,167 | 0,567 | 0,80 |
| **BDET** — tous les leviers (B + D + E + T) | 20 nov. 12:54 | 22 nov. 16:31 | 24 nov. 22:05 / 26 nov. 00:16 / 27 nov. 08:00 | **0,389** | **0,834** | ≥ 0,99 |

**Lecture intermédiaire.** Rien de ce qui sort du temps 1 n'est un résultat rapportable (ordre exploratoire, « Nature »). Ce qui peut se montrer avant le 25, sans aucun chiffre de l'hypothèse :

1. le texte de la confirmation scellé, la sonde gelée et la recette scellée fermée, avec leurs empreintes déposées chez un tiers (69 % des tirages en B, 80 % en E, presque toujours en T) ;
2. si la famille existe, le compte rendu de **l'épreuve plantée sur ses données honnêtes**. C'est une mesure de l'instrument, pas de l'hypothèse ; la montrer avant le verdict est ton choix.

**Ce qui n'est pas calculé ici.** Une lecture partielle de la famille, sur une première tranche de tâches, demanderait un plan séquentiel écrit avant le scellement, avec sa règle de dépense de l'erreur. C'est un choix d'analyse : il n'appartient pas à ce texte. Il resterait un nœud à part. Des noms de fichiers d'essais `tests/test_sequentiel_cycle2_*` sont présents dans l'arbre de travail ; je ne les ai pas ouverts. La session mère peut les rapprocher.

---

## 7. Leviers

1. **Parallélisme.**
   - Écrire le module de lecture de l'étape B bis en même temps que le quatrième addendum, pas après.
   - Deux machines de génération : environ 3 à 4 USD attendus de plus, 7 USD au pire (devis § 5). Gain d'environ 20 h à 400 tâches. Seul, il fait passer le verdict avant le 27 de 4 % à 19 %.
   - L'extraction par vagues ; le code de la chaîne pendant le temps 1 ; le bras d'attaque dès la recette scellée.
2. **Préparation avant l'ouverture** : tout ce que liste la section 10. Ces étapes sortent du chemin critique si elles partent **aujourd'hui** ; leurs marges vont de 33 à 78 h.
3. **Levée E — relecture complémentaire jouée avant l'ouverture, sorties scellées fermées.**
   - Gain : 8 h au rythme probable. Surtout, le risque de lancement, qui a pesé jusqu'à 92 h pour l'étape B bis, passe hors du chemin.
   - Coût en garde : les activations existent avant le verdict de l'étape B bis. Il faut un opérateur qui ne soit ni l'analyste, ni le lecteur ou le juge de l'étape B bis, et une ouverture écrite au registre au seul moment de l'ouverture.
   - C'est un écart à la condition de la ligne de GO proposée (« seulement après `OUVERTURE-TEMPS1-ACC2` », devis § 10) : **nœud**.
4. **Levée D — générer la famille pendant le temps 1.** Seule la pièce de génération est concernée : distillation, adaptateurs, épisodes. Ses sorties sont scellées fermées. La relecture et la notation par la sonde gelée, de 9 à 30 h, viennent après le scellement.
   - Gain : la plus grosse part de la marche de carte quitte le chemin critique.
   - Coût en garde : la phrase « la famille n'existait pas quand la sonde a été gelée » devient « la sonde a été gelée sans accès à la famille ». La garde passe du temps au cloisonnement : condition d'arrêt « exposition » de l'ordre § 8, point 4, et dépôt daté des empreintes de génération.
   - Il faut générer au plafond d'effectif, 600 tâches, avant la simulation : 90 à 124 USD attendus au lieu de 62 à 84, pire cas 268 USD sous 275 (devis § 5).
   - Le bras d'attaque et la liste des tâches doivent précéder la génération. **Les tâches fraîches deviennent alors le chemin critique** (85 % des tirages avec tous les leviers).
   - C'est un écart à la proposition 9 adoptée : **nœud**, à faire contre-lire, car le contre-lecteur avait déjà trouvé un ordre inexécutable.
5. **Levée T — temps 1 borné à 48 heures.** L'ordre exploratoire est encore un brouillon : on peut l'écrire avant son scellement.
   - Gain : c'est le levier le plus fort à lui seul (scénario BT : verdict avant le 27 dans 63 % des tirages au lieu de 19 %).
   - Coût en garde : plus de chances d'un temps 1 sans sonde défendable, donc du repli que tu as choisi au point 6 (b), qui donne un cycle rapporté sans famille. La sonde gelée est aussi moins mûrie.
   - Ce n'est pas un critère d'analyse, mais cela change la limite écrite de l'ordre : **nœud**.
6. **Levée de la table conjointe à l'ouverture** : gain de 2 h au rythme probable, au prix de la garde que GO-2026-11-18-58 a gardée. **Non recommandée.**

---

## 8. Avant-mortem : le 27 est arrivé sans résultat ; pourquoi

1. **Le verdict de l'étape B bis a traîné.** Même mesure de référence : l'étape B a mis 81,4 h entre ses scores et son verdict.
   - Parade : module et addendum en parallèle ; mandats du lecteur et du juge écrits dès maintenant ; code de la table conjointe vérifié avant le verdict.
2. **Le lancement sur carte a échoué plusieurs fois.** L'étape B bis a connu quatre échecs en 2,5 jours : authentification du clonage, carte invisible, écart carte-processeur, refus du classifieur.
   - Parade : reprendre à l'identique l'image, la commande et le filtre d'offres de la course réussie du 18 novembre (pilote 595.91.07) ; levée E ; chercher dès aujourd'hui une offre à 250 Go dont le stockage reste sous 0,08 USD de l'heure (recherche gratuite).
3. **L'extraction des tâches fraîches s'est arrêtée.** En octobre, deux causes l'ont bloquée : le classifieur (4 lancements sur 7 refusés) et la limite d'usage hebdomadaire du compte. Elles ont fait 80 h pour 96 papiers ; il en faut ici huit fois plus.
   - Parade : régler les permissions de la session **avant** la première vague, comme le 7 octobre ; relever l'usage restant du compte avant de lancer ; pousser vague par vague ; écrire le devis du point 8 (a) dès aujourd'hui avec les compteurs de la section 3.4.
4. **La conception de la sonde a pris la semaine entière** que l'ordre lui permet.
   - Parade : simulation de puissance et épreuve plantée codées et éprouvées sur jouets avant l'ouverture, pour que l'analyste n'écrive que la sonde ; levée T.
5. **Tes gestes sont arrivés après leur fenêtre** : dépôt daté, lignes de GO de dépense après la fin de l'autonomie (2026-11-19 à 09:06:42Z), levées D, E et T.
   - Parade : un seul message demain matin, avec les trois levées au format de décision, les deux lignes de GO tirées d'un devis final scellé, et le fichier d'empreintes prêt à déposer.

---

## 9. Dates de bascule (UTC)

**La règle** : si une étape n'est pas faite à la date de la première colonne, on montre le plan le 27, pas un résultat du cycle. La seconde colonne est la dernière chance : elle suppose que tout le reste aille au rythme bas.

Les dates sont calculées pour le scénario B (ce qui est décidé), avec un verdict visé le 25 à 18:00. Pour viser le 27 à 00:00, ajouter 30 h.

| étape | bascule (reste au rythme probable) | dernière chance (reste au rythme bas) |
|---|---|---|
| verdict de l'étape B bis | **20 nov. 09:30** | 23 nov. 00:30 |
| ouverture du temps 1 | **20 nov. 11:45** | 23 nov. 01:06 |
| relecture complémentaire poussée | **20 nov. 19:45** | 23 nov. 05:06 |
| liste des tâches scellée fermée | **22 nov. 19:45** | 24 nov. 05:06 |
| sonde gelée (`SONDES-ACC2`) ; code de la chaîne contre-lu | **22 nov. 20:00** | 24 nov. 05:12 |
| texte scellé (`SCELLEMENT-ACC2`) | **23 nov. 02:00** | 24 nov. 07:12 |
| départ de la création (gestes faits) | **23 nov. 06:00** | 24 nov. 07:42 |
| scores de la famille poussés | **24 nov. 22:00** | 25 nov. 13:42 |
| lecture faite | **25 nov. 10:00** | 25 nov. 17:42 |

Avec la levée D, la liste des tâches devient la première bascule : **22 nov. 06:00** (dernière chance 23 nov. 14:12).

**Hors du calcul, mais certaine** : l'autonomie de dépense par anticipation finit le **19 nov. à 09:06:42** (GO-2026-11-18-53). Après, toute ligne de dépense de ce cycle attend ton mot.

---

## 10. Ce qui peut commencer AUJOURD'HUI, sans aucun verdict et sans dépense

1. **Le quatrième addendum de l'étape B bis et son module de lecture neuf, en parallèle** (autre session ; processeur seulement).
2. **L'ordre exploratoire** : marqueurs de la section 2 recopiés par la mère depuis les lignes de registre et les compagnons, sans ouvrir les fichiers ; réserve de GO-2026-11-18-58 écrite ; contre-lecture ; scellement (`ORDRE-TEMPS1-ACC2`). Si tu le décides, la borne de 48 heures y entre avant le scellement.
3. **La recette de la famille** par une instance aveugle aux sondes : mode « coût » rejoué, règle du tirage, entropie ; contre-lue ; scellée fermée (`RECETTE-FAMILLE-ACC2`).
4. **Les deux textes du tirage** : règle du tirage complémentaire, avec les identifiants déjà employés exclus ; procédure d'extraction à l'échelle, avec la taille de l'échantillon de contre-vérification récrite. Contre-lus, scellés.
5. **Le devis de l'extraction** (point 8 (a)), avec les compteurs de la section 3.4 cités par commit. Le prix des appels reste à relever : c'est l'écrire, pas le dépenser.
6. **Le code de la relecture complémentaire**, repris de la chaîne de l'étape B bis (relecture à état imposé, apprentissage sur carte), avec ses essais et sa contre-lecture.
7. **Le code de la chaîne de confirmation**, écrit sans rien voir de la famille : génération à lots poussés et garde de débit, cellules à texte égal, second témoin, 800 directions par couche, notation, lecture, épreuve plantée, simulation de puissance. Essais sur données jouets ; contre-lecture.
8. **Le devis final**, scellé hors brouillon, avec tes décisions : 275 USD, 75 USD, disque. Puis le texte des deux lignes de GO, prêt à inscrire.
9. **Une recherche d'offres de carte** à disque d'au moins 250 Go, stockage sous 0,08 USD de l'heure. Lecture seule : aucune instance créée.
10. **Les mandats** : analyste du temps 1, neuf et non exposé ; opérateur de la relecture ; lecteur et juge de la confirmation ; agent du bras d'attaque (lecteur seul de la recette). **Le fichier d'empreintes** à déposer chez un tiers.
11. **Les trois décisions de levée** (E, D, T), au format de décision, pour ton message de demain matin.

## 11. Ce qui demande une dépense

| poste | renvoi | attendu ; plafond |
|---|---|---|
| relecture complémentaire du temps 1 (une carte A100) | devis § 6 et § 10 ; décision 4 | 5 à 15 USD hors garde ; plafond 75 USD (β) ; disque de 250 Go ou couche par couche |
| extraction des tâches fraîches (appels de modèle) | devis § 7 ; décision 8 (a) | **non chiffré** : devis à écrire (section 10, point 5) |
| bras d'attaque | devis § 8 ; décision 7 (ii) | « petite dépense » ; devis à écrire |
| création de la famille (une à trois cartes A100) | devis §§ 4, 5, 9 et 10 ; décision 5 (a) | 62 à 84 USD à 400 tâches ; 90 à 124 à 600 ; seconde machine +3 à 4 ; plafond 275 USD |
| levée D | devis § 5 | génération au plafond d'effectif, 600 tâches : 90 à 124 USD, pire cas 268 |
| levée E | devis § 6 | aucun surcoût ; seule change la condition de départ de la ligne |
| répétition sur carte avant l'ouverture (facultative, contre le risque n° 2) | ligne de la relecture complémentaire | moins de 1 USD par essai (3.3 : 0,06 à 0,25 USD) |
| hors de ce chemin | devis § 8 | seconde famille de réplication (après une issue positive seulement) ; second modèle de base (reporté) |

---

## 12. Ce qui, hors de nous, permet de vérifier

- **Le dépôt daté des empreintes chez un tiers**, avant la création de la famille : il prouve à quiconque ce qui était fixé, et quand (recette, liste, texte scellé, sonde gelée).
- **Les horodatages du dépôt distant et des registres** : toute date de ce texte se recompte par `git log origin/main --format='%H %cI'` sur les chemins cités.
- **Le calcul** : script et sortie scellés ; une graine fixe ; une autre personne obtient les mêmes nombres.
- **Après coup** : comparer, étape par étape, les dates réelles à celles de la section 9. Cette comparaison étalonne les durées non mesurées (conception de la sonde, code, bras d'attaque) pour le cycle suivant.
- **Une contre-lecture** de ce texte par un agent neuf est conseillée avant que la mère s'en serve pour te demander les levées. La règle ne l'exige pas pour un texte de planification.

## 13. Réserves

- Les tirages sont **indépendants par étape**. Les retards réels sont corrélés : ta disponibilité, les limites du compte, les pannes du loueur. Les queues sont donc plus lourdes que ce que montre le calcul.
- Quatre durées **ne sont pas mesurées** : conception de la sonde, code de la chaîne de confirmation, bras d'attaque, table conjointe. Les nombres de la section 6 en dépendent fortement.
- Le recoupement du devis par les deux courses d'organismes suppose qu'elles ont fait la même suite de pièces. Je ne l'ai pas relu.
- La faisabilité du tirage (section 3.4) suppose que la requête rende le même ensemble qu'en octobre.

## 14. Lectures

- **Dans le mandat** :
  - les trois textes servis : points à trancher sections A à D, ordre exploratoire en-tête, section 2 et conditions d'ouverture, devis entier ;
  - `registres/go.md`, lignes GO-2026-11-18-49 à -57 ;
  - registres propres de l'étape B bis et de la validité de l'adaptateur (clés et heures) ;
  - `registres/depenses.md` : lignes de l'étape B bis et de l'auto-conception, durées de location des courses d'organismes, dont j'ai extrait les seules heures et sommes ;
  - `git log` de la branche principale distante.
- **Hors mandat, déclaré** :
  - points à trancher sections E à G (affichées avec le reste du fichier) ;
  - ordre exploratoire sections 4 et 8 ;
  - GO-2026-11-18-58, -10-09, -18-26, -18-30, -18-31, -18-33, -18-45, -18-20, -18-36, -18-39 ;
  - clés et heures de `registres/scellements-v1.md` (lignes de l'étape A et de l'étape B) et du registre propre du premier cycle ;
  - messages de commit du premier tirage des tâches fraîches (octobre) ;
  - titres de sections et quelques lignes de la table de contre-lecture de `prereg/validite-adaptateur-v1.md` ; lignes 99 et 222 de `prereg/T0.7-etape-B-bis-v1.md` ;
  - en contexte, des lignes de dépenses d'autres études (organisme d'idéation, lentille neuronale, « raisons ou regard »), qui portaient des issues de ces études-là, hors de la liste cloisonnée ;
  - noms de fichiers non suivis de l'arbre de travail.
- **Non ouvert** : rien sous `diag/`, `runs/`, `donnees/` ni `docs/verdicts/`. Aucun résultat, score, aire ni issue des études cloisonnées. Des lignes de dépenses des courses d'organismes, je n'ai tiré que les heures.
