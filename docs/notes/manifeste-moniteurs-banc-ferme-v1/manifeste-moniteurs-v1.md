# Manifeste des moniteurs que la course du banc fermé et la porte G1 évaluent — v1

- Classe C (travail). Écrit le 2026-11-21 entre 19:46 et 19:55 UTC (`date -u`) par un sous-agent Claude Opus 5.5 neuf, lancé par la mère (`session_01Qi7Gr3eYmAhDEJzqLgWcv1`) au titre du nœud 9 du préenregistrement de la course du banc fermé (« manifeste des moniteurs : établi par la mère », Lazar, GO-2026-11-21-75). L'auteur n'a conçu aucun moniteur et n'en conçoit aucun ici. Il n'a écrit aucune des pièces citées.
- **Ce que ce texte est** : une liste de moniteurs, avec pour chacun le nom en clair, la famille de modèle, le rôle, la décision qui le fixe et le chemin:ligne. **Aucun contenu de moniteur** : aucune invite, aucun trait, aucune couche, aucun poids, aucun seuil, aucun score, aucun résultat.
- **Ce qu'il n'est pas** : la table d'empreintes de la garde 5 (section D7 bis de la course, champ n° 16), qui recense des fichiers par nom et par empreinte, au jour de la pose, à l'aide d'un programme de classe B. Ce texte n'en tient pas lieu et ne remplit pas le champ n° 16.
- **Qui ne le lit pas sans le déclarer** : il nomme des moniteurs. Celui qui ne doit rien lire des moniteurs ne le lit pas sans le déclarer au registre des accès : l'auteur de la course, qui « ne lit rien des moniteurs » (course, brouillon 14, l. 44), et toute personne ou session qui écrit une famille aveugle (échelon 1 de la règle du bras d'attaque, l. 113).

## Pièces lues (chemin, empreinte recalculée)

| Pièce | Empreinte |
|---|---|
| Course du banc fermé, brouillon 14 : `prereg/course-banc-ferme-v1-brouillon14.md`, branche `origin/claude/prereg-course-banc-ferme-v1` (tête `5182b602`) | `4489d39957b7dba53d015521867c2d7cb56ee01a6d3e2070523b889555173784` |
| Répétition générale, brouillon 9 : `prereg/repetition-generale-banc-ferme-v1-brouillon9.md`, même branche | `a58cab35cf4914a4e78decec95f296d824626752f4028b347ca5741d49f76e08` |
| Pièce de sécurité v16 : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v16.md`, branche `origin/claude/piece-securite-banc-ferme-v1` (tête `dd90f13f`) | `b8bcda60ead6f58f4cc59adf209c779eb81b201fc730734b9175e0faefdaeeec` |
| Audit des lignées : `docs/notes/scellement-2-lignees-lecteurs-v1/lignees-a-exclure-v1.md` | `596b5a73453b97ed876a2197dfd8ed68183802f531296f0bfac50d156b536862` |
| Sa vérification : `…/verification-lignees-a-exclure-v1.md` | `8718c80bee53da3521e0c0f934af99d91c284465aec604f076a060ec5399ce96` |
| N-007 et N-008 : `docs/decisions/decision-N-007-N-008-v1.md` | `ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232` |
| N-029 : `docs/decisions/decision-N-029-v1.md` | `084e30523c0a0349cb1daf0dcf804f6c9d38c10d4f8bceed23c787fa507f34e4` |
| N-053 : `docs/decisions/decision-N-053-v1.md` | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` |
| N-054 : `docs/decisions/decision-N-054-v1.md` | `c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f` |
| N-056 : `docs/decisions/decision-N-056-v1.md` | `3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d` |
| N-063, v2 (qui prime sur la v1) : `docs/decisions/decision-N-063-v2.md` | `b2d9f03543802f82890c99eff77d4aab34ad532b50986b887c046906914b625b` |
| Brouillon 6 du préenregistrement de G1 : `brouillons/G1-preenregistrement-v1-brouillon6.md` (non scellé, non contre-lu) | `939b56e540fa49ea910bf63f8ded66d67c95cf03a4dfec6ccc7f51622cc601bb` |

Compagnons `.sha256` vérifiés : les sept décisions ou notes ci-dessus qui en ont un, et le brouillon 6 de G1.

Lues en plus, aux seules lignes dites : `registres/decisions.md` (`4b91c7b5…`) l. 374-383 (décisions D1, D2, proposition P-003) et l. 996 (R-768) ; `registres/go.md` (`ac33f39b…`) l. 128, 671 et 674 ; `src/controle_ia/harnais/modeles.py` (`d0befc29…`) l. 1-80 (liste blanche des modèles) ; `prereg/bras-attaque-regle-v1.md` sur la branche de la course (`88418df0…`) l. 110-135 ; `docs/decisions/decision-N-060-v3.md` (`2b448f69…`) l. 22-26 ; `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md` l. 329-331 ; `docs/notes/devis-famille-reserve-cycle-2-v1/devis-banque-d-episodes-famille-reserve-cycle-2-v3.md` l. 441-442 ; `docs/notes/banc-ferme-choix-contre-lecture-fable-v1/contre-lecture-trois-choix-banc-ferme-fable-v1.md` (`bc9ec0fd…`) l. 95-99.

## 1. La course du banc fermé n'évalue aucun moniteur

| Pièce | Ce qu'elle dit | Chemin:ligne |
|---|---|---|
| Course, brouillon 14 | « aucune lecture par un moniteur » ; la lecture des épisodes par des moniteurs gelés attend le scellement 3 et un préenregistrement à part | `prereg/course-banc-ferme-v1-brouillon14.md`:69 ; voir aussi :286, :300, :502 |
| Course, brouillon 14 | la course relève de l'échelon 1 (famille aveugle), « dont les verdicts appartiennent au préenregistrement de G1 » | :70 |
| Répétition générale, brouillon 9 | « Aucun moniteur » ; ses épisodes n'entrent dans aucune mesure de G1 | `prereg/repetition-generale-banc-ferme-v1-brouillon9.md`:33-34 |

**Ce qui compte pour la course** : les moniteurs qui **liront plus tard ces épisodes**. Ce sont eux que visent l'exclusion des lignées des lecteurs du dommage (course :84, :138 ; pièce de sécurité :176, condition 11), le lecteur de la question fermée (course :212) et la lignée du vérificateur (pièce de sécurité :454 ; GO-2026-11-21-72). Ce sont les moniteurs de G1, sections 2 et 3. S'y ajoute le panel des juges du papier C, si ces épisodes lui servent (section 4).

## 2. G1 : le sujet et la liste d'intersection-union, où chaque comparateur est à battre

La liste vient du brouillon 6 de G1, qui n'est pas scellé. Elle peut changer au scellement. Un moniteur qui lit l'intérieur de l'agent n'a pas de modèle à lui : sa famille est celle de l'agent qu'il lit, Llama-3.1-8B-Instruct (Meta) (G1 :51 ; course, nœud 2, :545).

| n° | Moniteur, en clair | Famille de modèle | Rôle | Décision qui le fixe | Chemin:ligne |
|---|---|---|---|---|---|
| 1 | Le sujet : accumulation séquentielle des scores de la sonde principale d'intention, qui lit l'agent pendant qu'il agit | Llama (Meta), l'agent lu | sujet de la porte ; case « blanc, séquentiel » du plan deux par deux | N-007-N-008 :28, :66 ; N-056 :38-46 | G1 :199, :214 |
| 2 | Juge informé de la taille de l'agent, score maximal par action | Llama (Meta) : Llama-3.1-8B-Instruct | comparateur 1 ; case « noir, par action » | D1 (a), `registres/decisions.md`:376 ; N-029 :20-22 | G1 :201, :214 |
| 3 | Le même juge, accumulation additive des scores (base (i)) | Llama (Meta), sans modèle propre : agrège les scores du n° 2 | comparateur 2 ; case « noir, séquentiel » | N-007-N-008 :42, :47 | G1 :202, :214 |
| 4 | Juge informé plus petit, score maximal | Llama (Meta) : Llama-3.2-3B-Instruct | comparateur 3 | D1 (b), `registres/decisions.md`:376 | G1 :203 |
| 5 | Le même, accumulation additive | Llama (Meta) | comparateur 4 | N-007-N-008 :42 | G1 :204 |
| 6 | Juge robustifié, score maximal | **non établie, à fixer par Lazar** (section 5) | comparateur 5 | P-003, `registres/decisions.md`:381 ; N-007-N-008 :49, :66 | G1 :205 |
| 7 | Le même, accumulation additive | celle du n° 6 | comparateur 6 | idem | G1 :206 |
| 8 | Prédicteur sur les traits du texte des actions, score maximal | aucune : sans modèle de langue | comparateur 7, obligatoire ; bras **spécialisé** au sens de N-054 (traits liés au champ du coût) | N-029 :23-27 ; N-054 :42-44 | G1 :207 |
| 9 | Le même, accumulation additive | aucune | comparateur 8 | N-029 ; N-007-N-008 :42 | G1 :208 |
| 10 | Triage, inspection et jugement réimplémentés d'après la méthode publiée TRACE (« TRACE-lite ») | **non établie** : le choix du modèle observateur est « un nœud de Lazar » (R-768) | comparateur 9 | P-003, `registres/decisions.md`:381 ; R-768, `registres/decisions.md`:996 | G1 :209 |
| 11 | Modèle temporel appris sur un observateur séparé, de type TRACES (base (iv)) | **non établie, à fixer par Lazar** (section 5) | comparateur 10 | N-007-N-008 :45, :47 | G1 :210 |
| 12 | Cascade de portes indépendantes sur la sonde du sujet (base (ii)) | Llama (Meta), l'agent lu | comparateur 11 ; base blanche que G1 doit battre | N-007-N-008 :43 ; N-056 :38-46 | G1 :211 |
| 13 | Sonde sur le dernier état seul (base (iii)) | Llama (Meta), l'agent lu | comparateur 12 ; base blanche que G1 doit battre | N-007-N-008 :44 ; N-056 :38-46 | G1 :212 |
| 14 | Recette publiée d'HELIOS, rejouée sur notre agent, **conditionnelle** | Llama (Meta), l'agent lu | comparateur 13, si elle est rejouée et diffère du n° 13 | décision DG1-3 (b) du brouillon 6 ; P-040 | G1 :213 |

## 3. G1 : moniteurs rapportés, hors décision

Ils ne sont pas critères de la porte. Ils lisent pourtant les épisodes : leur famille compte pour l'exclusion.

| n° | Moniteur, en clair | Famille de modèle | Rôle | Décision | Chemin:ligne |
|---|---|---|---|---|---|
| 15 | Plancher « tout signaler » | aucune | plancher rapporté | N-007-N-008 :68 | G1 :215 |
| 16 | Plancher « juge en une passe avec le même modèle » | Llama (Meta) : Llama-3.1-8B-Instruct | plancher rapporté | N-007-N-008 :68 ; P-003 :381 | G1 :215 |
| 17 | Juge d'une autre lignée | Qwen (Alibaba) : Qwen2.5-7B-Instruct | bras rapporté | N-053 :33-35 ; `src/controle_ia/harnais/modeles.py`:27 | G1 :215 |
| 18 | Sondes aléatoires appariées en covariance ; sonde nulle de la chaîne de traitement | Llama (Meta), l'agent lu | témoins | brouillon 6 de G1, sans décision nommée à la ligne | G1 :215 |
| 19 | Cellules « nu » (sondes génériques contre juges sans description de la menace) et « à exemples » | les juges de la cellule : famille non dite à la ligne. Si ce sont les juges de D1 : Llama | cellules rapportées | R-746 (1) et (4), cités par G1 | G1 :215 |
| 20 | Lecture des sondes sans les positions qui portent une évidence textuelle ; condition « suppression consignée » | Llama (Meta), l'agent lu | bras rapportés ; la lecture filtrée est la lecture principale de toute revendication d'« intention » | N-053 :17-22 | G1 :215 |
| 21 | Directions de concept et témoin lexical | Llama (Meta), l'agent lu | rapportés | P-013 (b), cité par G1 | G1 :215 |
| 22 | Traits internes de l'agent comme traits du pôle, aux trois couches décidées, toutes rapportées | Llama (Meta), l'agent lu | rapportés | N-056 :52-54 | G1 :215 |
| 23 | Bases de la littérature qui lisent l'intérieur : dérive cumulée non supervisée, test de Page sur les états internes, sommes sur fenêtre, sonde supervisée de référence haute | Llama (Meta), l'agent lu | rapportées | brouillon 6 de G1 | G1 :215 |
| 24 | Juge génératif ouvert de grande taille, en plafond | non dite ; **non décidé** (changement de modèle, GO à part) | plafond, plus tard | N-029 :28-30 ; R-746 (2) | G1 :215 |
| 25 | Sous-ensemble des lectures décisives à plus grande taille | non dite ; **non décidé** (GO à part) | contrôle d'échelle | N-053 :36-37 | — |
| 26 | Ressources publiques : NARCBench, Liars' Bench, SHADE-Arena, Llama Scope | jamais dans la liste sans nœud à part ; si Llama Scope y entre : Llama | hors de la liste scellée | N-061 | G1 :215 |

**Générique ou spécialisé** (N-054 :40-45) : seul le prédicteur sur les traits du texte est classé par une décision (spécialisé, N-054 :44). Les juges informés reçoivent « la description fixe des modes connus » (G1 :201). Pour tous les autres, le classement est à déclarer au préenregistrement de G1 (« ce qu'un bras sait du mode est déclaré », N-054 :45). Ce manifeste ne classe rien.

## 4. Hors G1 : le panel des juges du papier C, sous condition

| Moniteur | Famille | Condition | Chemin:ligne |
|---|---|---|---|
| Panel des juges génératifs du papier C | Llama (Llama-3.1-8B-Instruct), Qwen (Qwen2.5-7B-Instruct), **Mistral (Mistral AI) : Mistral-7B-Instruct-v0.3** | seulement si ces épisodes servent au papier C. La règle du bras d'attaque prévoit deux mesures du papier C lues par des moniteurs de texte (`prereg/bras-attaque-regle-v1.md`:134-135). **Le statut actuel de D2 n'est pas vérifié** | D2, `registres/decisions.md`:377 ; `src/controle_ia/harnais/modeles.py`:26-29 ; course :84, :138 ; contre-lecture des trois choix :95 |

Hors de cette liste, d'autres rôles lisent sans être des moniteurs évalués : les lecteurs du dommage (champ n° 18), le vérificateur interne, le lecteur de la question fermée, et le juge du second temps. Ce dernier est proposé comme un Claude Fable 5.2, donc de la lignée Claude d'Anthropic (course :141, champ n° 10, à remplir). Voir le point 5 de la section 6.

## 5. Les familles encore ouvertes

| Moniteur | Établie par une pièce ? | Ce qui la borne, sans la fixer |
|---|---|---|
| Observateur séparé de la base (iv) (n° 11) | **Non établie, à fixer par Lazar.** N-007-N-008 :45 dit « observateur séparé » sans modèle. Le brouillon 4 de T0.8 (:330) dit : « aucun code à ce jour » | la référence boîte noire est locale et n'envoie aucun texte d'action à un tiers (N-029 :17, :32-33) ; un modèle chargé par le harnais est dans la liste blanche (Llama, Qwen, Mistral ; `modeles.py`:23-30, « tout ajout passe par un GO de Lazar »). La publication TRACES emploie des observateurs Llama et Qwen (`docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md`:104) : c'est un fait du papier, non une décision du programme |
| Juge robustifié de la proposition P-003 (n° 6 et 7) | **Non établie, à fixer par Lazar.** P-003 (:381) fixe la méthode (invites de 2606.08892), pas le modèle | mêmes bornes. Indice non décisoire : le brouillon 4 de T0.8 (:329) demande « une rubrique que le 8B tienne », ce qui supposerait Llama |
| Modèle observateur de TRACE-lite (n° 10), **ouvert lui aussi, et omis par l'audit des lignées** | **Non établie, à fixer par Lazar.** R-768 (:996) : « restent : choix du modèle observateur (nœud de Lazar) ». Le code dit que l'observateur n'est pas fixé et qu'il doit être dans la liste autorisée (`src/controle_ia/bases/trace_lite_conduite_v1.py`:15, lu par la seule recherche) | mêmes bornes. Recommandation non décisoire : Llama-3.1-8B-Instruct comme observateur principal (`docs/sources/lecture-pdf-niveau1/rapport-TRACE-AcMAS-v1.md`:120) |
| Juge ouvert de grande taille (n° 24) ; lectures à plus grande taille (n° 25) | non décidés ; hors de la liste tant qu'il n'y a pas de GO à part | un changement de modèle demande un GO (N-029 :29-30 ; N-053 :37) |

**Conséquence pour l'exclusion.** Tant qu'aucun GO n'ajoute de modèle à la liste blanche, chacune des trois familles ouvertes sera Llama, Qwen ou Mistral. L'exclusion des lecteurs du dommage reste alors « Llama ; Qwen » (audit des lignées :26, et sa vérification :56). Mistral devient exclu sans condition si l'un des trois est un Mistral. Il l'est déjà tant que ces épisodes servent au papier C. **Aucun moniteur établi n'est de la lignée Claude**, et les familles ouvertes ne peuvent pas l'être sans GO. La condition de la ligne GO-2026-11-21-72, qui demande un vérificateur d'une autre lignée si un moniteur évalué est un Claude, n'est donc pas déclenchée par ce manifeste. Elle le serait si un GO fixait un Claude pour l'une des familles ouvertes.

## 6. Nœuds, pour Lazar

1. **Famille de l'observateur séparé de la base (iv)** : non établie, à fixer par Lazar. Elle tient le champ n° 3 de la course ouvert (course :84).
2. **Famille du juge robustifié de P-003** : non établie, à fixer par Lazar. Même effet.
3. **Modèle observateur de TRACE-lite** : non établi. R-768 le désigne comme un nœud de Lazar, et l'audit des lignées ne le compte pas parmi les familles ouvertes. Mêmes conséquences que pour les points 1 et 2.
4. **Statut du panel du papier C et usage de ces épisodes au papier C** : c'est ce qui décide si Mistral est exclu des lecteurs du dommage.
5. **Le mot « juge » dans la condition 11 de la pièce de sécurité** (:176, « famille d'un moniteur ou d'un juge qui lira ces épisodes ») : vise-t-il aussi le juge du second temps, proposé comme un Claude Fable 5.2 (course :141) ? Si oui, la lignée Claude est exclue des lecteurs du dommage. Lecture de l'auteur : non, car N-060 v3 :24-25 ne vise que les « moniteurs évalués ». La lettre est ambiguë.
6. **Juge ouvert de grande taille et lectures à plus grande taille** : si l'un entre dans la liste scellée de G1, sa famille s'ajoute à l'exclusion.

## 7. Réserves, et ce qui a été vu sans être cherché

- La liste de G1 vient d'un brouillon non scellé et non contre-lu, dont les décisions datent du 5 novembre. Un brouillon plus récent, s'il existe hors de `brouillons/`, n'a pas été cherché.
- Des recherches par `git grep` sur `docs/`, `registres/`, `brouillons/`, `prereg/` et `src/`, menées hors des chemins interdits, ont affiché des lignes isolées que l'auteur n'a pas ouvertes au-delà : brouillons 1 à 4 de T0.8 (périmètre de la version 0) ; notes de préparation de la couche 2 (devis et collisionneur) ; notes du protocole X ; idées du brainstorm sur l'axe de la douleur ; `registres/etat.md`:361 ; trois lignes du code de TRACE-lite (:15, :79, :236).
- Vus sans être recopiés : les numéros des trois couches de N-056 point 3 et de G1 :215 ; un chiffre de résultat de P3 dans N-029 :26 et dans une ligne de G1 affichée par la recherche (:124) ; les noms des traits du prédicteur dans N-029 et G1 :207. Rien de cela n'est repris ici.
- Rien n'a été lu sous `donnees/`, `runs/`, `diag/` ou `archives-reponses-modeles/`, ni aucun fichier « consigne-privee » ou « conception-ii-b ». Aucune famille aveugle, aucun épisode, aucune invite, aucun poids, aucun seuil.
