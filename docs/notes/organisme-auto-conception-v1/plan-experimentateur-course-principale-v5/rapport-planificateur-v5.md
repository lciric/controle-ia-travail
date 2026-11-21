# Rapport du planificateur — v5 du plan de la course principale

- Auteur : planificateur du plan v4, qui écrit aussi la v5, modèle F.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 08:30:37Z, avant l'écriture.
- Commande : le message de la mère qui rend la vérification de la v4 « Conforme, sous deux retouches de lettre » (`804a6675ea350fbe30835e40f7d538be1f731240c159f01c887da33567f57dbb`), donne ses deux relevés et demande la v5, sous les règles du mandat de la v4.
- Processeur seul : aucun appel, aucune clé lue ni nommée, aucune dépense, aucune machine louée, aucun code de l'organisme lancé, aucune écriture dans un dépôt, aucun commit. Rien ouvert sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Seul programme joué : mon programme de calcul, sans entrée.
- **Aucun refus de permission, de classifieur ni de garde n'a été rencontré.**
- La v4 et ses pièces n'ont pas été touchées.

## 1. Pièces rendues

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/planificateur-plan-v5-course-principale/`. Chaque pièce a son compagnon `.sha256`.

| pièce | objet |
|---|---|
| `plan-experimentateur-tests-de-mort-course-principale-v5.md` | la v5 |
| `differentiel-plan-v4-v5.md` | ce qui change |
| `rapport-planificateur-v5.md` | ce rapport |
| `table-empreintes-planificateur-v5.md` | empreintes |
| `calculs_plan_v5.py`, `calculs-plan-v5-sortie.txt`, `calculs-plan-v5-passe-2.txt` | calculs ; joué deux fois, `cmp` muet |

## 2. Les deux retouches, et leur lieu

| n° | retouche demandée | lieu dans la v5 | portée |
|---|---|---|---|
| 1 | D8 (a) : les dix noms avec leur source ; le point (1) tombe ; deux branches (a1) et (a2), (a2) dite lire une valeur | § 7.3, option (a) ; § 9, réserve 8 ; § 1, une ligne | oui |
| 2 | table du § 4.2 : E1-AC à 5,75–6,75 heures ; E1-v69 au devis d'heures du palier 1 ; chemin critique retrouvable depuis la table | § 4.2 : colonne « heures » sur les quatorze lots, alinéa « Les heures de la table », additions du chemin critique | oui |

**L'écart 1 du rapport de la v4, mis à jour.** Il disait : « champs fermés de D8 (a) non nommés ». Il est levé par le relevé de la mère. Les dix champs sont `titre`, `axe`, `module_change`, `mecanisme`, `plus_proche_voisin`, `ce_qui_distingue`, `epreuve_monde_plante`, `cout`, `ce_qui_la_refuterait`, `limites` (configuration `3f662ee8…`, clé `champs_fiche`). Aucun n'a de liste de valeurs : le point « valeurs par identifiant » tombe, comme la v4 l'annonçait sous condition. Ce qui reste de l'écart : **je n'ai pas ouvert la configuration moi-même** ; je tiens les noms du relevé de la mère, vérifié par le contre-lecteur.

**L'écart 2 du rapport de la v4** (« GO-15 et GO-28 ») est clos : la mère et le contre-lecteur confirment GO-2026-11-20-15 et GO-2026-11-20-28.

## 3. Calculs

Aucun chiffre ne change. Le programme reçoit un bloc de plus, qui somme la colonne d'heures : 46 à 56 heures pour les lots de code ; 37,5 à 47,5 sans E5 ni E6 ; 18,25 à 20,25 pour E0, E1-AC, C3, E8 et E9 ; 20,25 à 23,25 avec C2. Les 55 premières lignes de sa sortie sont celles de la sortie de la v4, à l'octet (comparaison faite).

## 4. Écarts

1. **Une colonne « heures » sur toute la table**, et non sur les deux seules lignes E1 : sans elle, le chemin critique ne se retrouvait pas depuis la table. Les heures de E0, E2, E4 à E9 et de l'ancien E1 sont lues au plan v1 (`0bb27bc0…`, l. 162 à 171), que je n'avais pas ouvert à la v4 ; lecture par recherche de lignes, dans ce seul fichier.
2. **La recommandation de D8 précisée d'un membre de phrase** : « (a), dans sa branche (a2) si Lazar accorde la lecture d'une valeur par programme ». Sans lui, « puis (a) » ne disait plus quelle branche. L'ordre (d), (a), (b), la confiance 0,6 et l'absence de défaut sont inchangés.
3. **Une phrase de D5 retouchée** pour rester vraie dans un texte nommé v5 : le défaut reste compté à partir du texte de la v4. Rien d'autre de D5 n'est touché.
4. **Un alinéa de tête, deux lignes au § 1 et la signature** ajoutés ou retouchés, pour dire ce qu'est la v5.
5. **Configuration de la course non ouverte par moi** (voir § 2).
6. Le programme et le plan de la v5 partent de copies de ceux de la v4, faites par une commande de copie simple.

## 5. Pour la mère

- D8 (a) ne garde de substance que par (a2), qui lit la valeur d'un champ libre et n'est pas « sans aucune valeur » ; (a1) rend à peu près ce que GO-2026-11-20-28 a déjà rendu. C'est écrit tel quel au § 7.3.
- Le défaut de D5 court sur le texte de la v4 ; la v5 ne le déplace pas.
- L'écart 3 du rapport de la v4 (une recherche à joker, déclarée, sans effet) reste à consigner.

— planificateur du plan v4, auteur de la v5, modèle F
