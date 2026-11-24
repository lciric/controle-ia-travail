# Contre-lecture de conformité — passe de recalcul v6 et programme de comparaison v2 (barreau 8, additif 2) — Sonnet 5.5

- **Modèle** : Claude Sonnet 5.5 (sous-agent neuf ; n'a écrit ni les codes, ni le texte scellé, ni les additifs).
- **Heure** : début 2026-11-24T11:05:15Z ; rapport écrit vers 11:30Z (`date -u`).
- **Branche** : `barreau8/code-passe-additif-2-v1`, commit `3405f7afe9`.

## Ce que j'ai lu (pour le registre « qui a lu quoi »)

`CLAUDE.md` ; `prereg/lecture-sondes-barreau8-v1.md` (table I partielle, conditions D-1 à D-13, gardes P0 à P10, section « Code, registre… », par extraits) ; additif 1 (sections « Conditions de départ », « Note d'interface version 7… » en entier, « Codes, registre… », « Liste d'arrêt ») ; additif 2 en entier ; notes v6 (par différence seulement) et v7 (par différence mot à mot v6/v7, plus les blocs « Effectifs ») ; fiche `-v7-champs.json` ; `comparaison-interface-v6-v7-v1.json` et `constantes-reportees-additif-1-v1.json` (avec contrôle des compagnons) ; `comparer_interface_v6_v7_v2.py` et son essai ; `passe_recalcul_v6.py` (différence avec la v5 en entier, plus lectures ciblées) et son essai (extraits P0, P1, P3, P8, M-4, M-5) ; notice v7 ; `registres/sondes-iib-v1.md`. Existence par `ls` seulement : `diag/20261122-202132-iib-reel` (absent de cette branche), `donnees/…taches-evaluation.json`, `donnees/20261019-230011-p3-reel/…` (présents).
Lu en plus (hors liste, sans contenu privé) : noms et empreintes des rapports de conformité antérieurs de `docs/notes/barreau8-cote-moniteurs-sorties-v1/` (par `sha256sum`) ; `requirements-cpu.txt` ; liste des fichiers de `docs/notes/rejeu-activations-saboteur-voie-a-v1/prealables-cote-expose-v7-brouillon/` (noms) et empreinte de l'extrait (`sha256sum`, **contenu non ouvert**).
**Non lu** : `diag/`, `donnees/` (contenu), `runs/`, `traces/`, `docs/verdicts/`, `registres/iib-*`, `src/controle_ia/iib/`, branches `claude/iib-executante-*` et `essai/iib-explo-*`, `registres/decisions.md`, `registres/etat.md`, le code de la lecture (`lecture_sondes_v5.py`, hors périmètre), le contenu de l'extrait du côté exposé (la phrase de la notice « versions présentes et égales à 5.18.0 et 0.23.2 » n'est donc **pas vérifiée par moi**).
Écritures : ce rapport ; copie de travail dans mon bloc-notes (mutations) ; rien dans le dépôt hors ce fichier.

## Rejeux

- `comparer … calculer` : mot « report », 8 identiques / 14 changés / 0 ajouté / 0 absent, aucun écart aux valeurs attendues. `controler` : « absente » pour les deux pièces, seul écart, attendu.
- Recalcul indépendant (programme à moi, formules de l'additif 1 appliquées à la fiche) : T=64, E=1, A=10, J=400, L=8, K=4, m=2, N=2 560, N_c=640, k=1, pas 16 et 128, n15=161, n7=21, taille 1 502 781 440, place libre 3 100 000 000, budget 12 h, 13 états : **tous égaux à M-4 et à la table que construit le programme**. Les deux chaînes de la liste fermée sont égales caractère pour caractère à celles de l'additif 2 et de la fiche (vérifié par extraction du texte de l'additif).
- Intégration : la table construite sur les vraies pièces, passée à `specification_depuis_table(SPECIFICATION_TEXTE, …)` de la passe : acceptée, spécification inchangée ; `place_libre` ou `n15` modifiés : refus « ligne 24 ».
- Essais : `189 passed` en 1 min 52 (145 pour la passe, comme dit la notice).
- Mutations (copie de travail, sous-ensemble P0/P1/P3/M-4/M-5) : 12 sur 14 tuées (booléen accepté, versions non comparées, décodages non comparés, champs couverts non contrôlés, empreinte de l'extrait, borne V, tri des clés, rapport v5, empreinte de `config.json`, comptage des lignes de code, additif 2 non contrôlé, chemin des tâches). **Deux survivent** : constats 5 et 6.
- Recherche par programme (AST) des littéraux de la v6 (64, 400, 640, 2 560, 161, 21, 256, 128, 16, 10, 8, 4096, 1,1e9, 3,1e9) : seuls restent ceux de `SPECIFICATION_TEXTE` (lignes 228 à 269), tous soumis à l'égalité avec la table (`CHAMPS_DE_FORME`) ; aucun en dur ailleurs. Noms de fichiers `.npz`/`.jsonl` de la course : plus aucun (seuls les noms de la livraison, inchangés).

## Constats

1. **Moyen** — `comparer_interface_v6_v7_v2.py`, l. 675-683 (`ecrire`) contre l. 661-674 (`controler`). M-4 exige que la pièce réécrite rende les mêmes états de blocs et champs changés que la v1, « sinon : nœud ». `ecrire` écrit et scelle les deux pièces sans rejouer ce contrôle, qui n'existe que dans `controler`, après coup ; or R12 interdit de réécrire (`ecrire_json_et_compagnon` refuse l'existant). Une pièce divergente serait donc déjà scellée sur disque. De plus, si la table existe déjà et la pièce non, la pièce est écrite puis l'écriture de la table échoue (état partiel). *Correction* : dans `ecrire`, appeler `controler_contre_la_version_1` sur les objets en mémoire et refuser en cas d'écart ; vérifier l'absence des deux cibles et de leurs compagnons avant d'écrire la première.
2. **Mineur** — essais du comparateur : aucun artefact pour `controler_contre_la_version_1` (états de blocs différents, table de l'additif 1 d'une autre empreinte ou aux champs « nœud » autres que les quatre, statuts des autres champs), ni pour `ecarts_aux_valeurs_attendues` avec une table qui rend une autre valeur (« n'est pas scellée »), ni pour le refus de `ecrire` (code 2). Seul le cas sain est joué (l. 300-306). R5 demande un artefact par garde. *Correction* : trois essais (v1 truquée par `tmp_path` ; fiche à T=32 → écarts non vides ; `principal(["ecrire", …])` sur racine factice → code 2, rien d'écrit).
3. **Mineur** — l. 558 et 568 : `note_v7.chemin` est recopié de la fiche sans être comparé à `CHEMIN_NOTE_V7` (seule l'empreinte l'est). *Correction* : refuser si `valeurs["note.chemin"] != CHEMIN_NOTE_V7`.
4. **Remarque** — M-4 dit que le programme « ne lit que » les notes, la fiche et leurs compagnons ; `controler` lit aussi la pièce v1 et la table de l'additif 1. C'est requis par la comparaison que M-4 impose et déclaré en tête du module ; à garder tel quel, à citer au rapport scellé.
5. **Moyen** — `passe_recalcul_v6.py` l. 780-782 (`_posterieure`) : « strictement postérieure par le rang **et** par l'heure ». Mutation `>=` : tous les essais passent. Le cas « ligne de code à la même seconde que la ligne de l'additif 2, rang supérieur » (et le cas symétrique additif 2 / additif 1) n'est pas éprouvé ; l'essai « heure antérieure » ne l'attrape pas. *Correction* : un essai de plus dans `test_p0_artefacts_du_registre…` avec heure égale (motif « 0 ligne(s) CODE-PASSE-IIB strictement postérieure » et « n'est pas strictement postérieure »).
6. **Mineur** — l. 1171 : `trace.controle("P3", e == 1, …)` survit à la mutation « toujours vrai » ; le cas E ≠ 1 est déjà arrêté par `exiger_table_neuve` (essai « table-deux-episodes »). Garde redondante, non éprouvée seule. *Correction* : un essai direct de `garde_p3_structure` avec `episodes_par_tache=2`, ou retrait assumé de la redondance.
7. **Mineur** — D-16, « rapports de conformité antérieurs non cités » : le code ne refuse que l'empreinte `fa9158fb…` (l. 104, 926). Les autres rapports antérieurs du dossier (ex. `rapport-conformite-codes-passe-v5-lecture-v5-brouillon1.md`, `44aaa3da…`, et les `contre-lecture-*`) seraient acceptés ; la notice le dit pour le seul rapport v5. La garantie réelle repose sur la session mère, qui choisit la ligne de code. *Correction* : soit étendre la liste aux empreintes des rapports antérieurs présents, soit déclarer au rapport de conformité que le code n'en tient qu'un.
8. **Mineur** — `exiger_table_neuve` / P0 : l'empreinte et le contenu de la table sont contrôlés, mais ni son chemin (`constantes-reportees-additif-2-v1.json`), ni sa citation de la table de l'additif 1 et des pièces `note_v7`/`fiche_v7`. Une table bien formée d'un autre chemin passerait si le bordereau la cite. M-5 n'exige que « présente à son empreinte, disant report » : conforme à la lettre ; durcissement facultatif (comparer le chemin à une constante).
9. **Mineur** — essais M-5 incomplets sur les variantes symétriques : aucun essai « additif 2 altéré après la ligne » (le texte et l'additif 1 le sont ; la mutation qui saute l'additif 2 est pourtant tuée, par un autre essai) ; « clé `transformers` seule absente de l'extrait » ; adaptateur (et non seulement fichier des identifiants) d'une autre empreinte ou sans compagnon. Le code traite les rôles uniformément ; risque faible. *Correction* : ajouter ces trois cas aux listes paramétrées.
10. **Remarque** — la vérification que l'extrait réel (`1ff87c08…`, empreinte confirmée par `sha256sum`) contient `transformers`=5.18.0 et `tokenizers`=0.23.2, égales à `requirements-cpu.txt` et à l'environnement local (`5.18.0`, `0.23.2`, confirmé), repose sur la notice ; je n'ai pas ouvert l'extrait.

Aucun constat bloquant. Aucun écart de lettre trouvé sur : fiche et valeurs de référence v6 (tableau de l'additif 1 reporté clé par clé), sorts des champs, structure des rôles (s1) à (s8), RP-7 (formules, plancher 81/11, place libre), budget, paires, liste des constantes RP-1 à RP-14, liste fermée et conditions jointes de M-4, trois différences de la table, mot d'ensemble, réécriture sous `comparaison-interface-v6-v7-v2.json`, mêmes états et champs que la v1 ; M-1 (JSON strict, deux clés, clauses (a) à (d), ordre, versions avant tout, égalité des deux décodages, texte du journal, V lu dans `config.json` à son empreinte, tout avant `chargeur.poids()`) ; M-2 (trois fichiers, extrait épinglé, quatrième clé et `donnees/<run_id>/` refusés, tâches au chemin de la table) ; M-4 côté passe (nœud, champs couverts autres que les quatre, constante différente refusée) ; M-5 (huit clés, une ligne de code exactement et strictement postérieure, antérieures comptées à part, bordereau à dix clés, trois textes intacts) ; D-16 ; livraison, P2, P4 à P10 inchangés (différence avec la v5 limitée à l'aiguillage des chemins, au contrôle n15/n7, à la trace et au manifeste).

## Notice

La ligne de commande de la section « Module » correspond à l'analyseur du module (actions, options, obligatoires : vérifié par `--help` et lecture de `principal`) ; `145 essais` exact. Chemins existants sur `origin/main` : additifs, registre, notes v6/v7, fiche, pièces v1, devis, `go.md`, invites, extrait. Absents à ce jour, normalement : `constantes-reportees-additif-2-v1.json`, `registres/bordereau-code-passe-barreau8-v6.json`, rapport de conformité. `diag/20261122-202132-iib-reel/` absent de cette branche (côté exposé) ; `donnees/20261114-001352-t07-lecture-reel/` sur la branche `origin/donnees/t07-etape-a-v1` (D-8, comme la notice v6). Aucune erreur trouvée.

## Table des quatorze blocs changés (note v7 contre note v6)

Vérification champ par champ de la fiche contre la note v7 : tous égaux (fichier, tableaux, forme de clé, étendue, types, plafond, textes vides, préfixe, épisode = tâche, conditions et doses, adaptateurs, rang, alpha, projections, noms de fichiers, texte privé « non », recette égale, invite, pas 10, lot 8, effectifs, `B100`, `etats-lectures-iib-v1.json`, oracle `evaluation-iib-v5.json` et « non », tâches (chemin, empreinte, réserve « non »), commit, run). Pas de désaccord, donc pas de ligne 20 de l'additif 1.

| # | bloc | verdict |
|---|---|---|
| 1 | en-tête | sans effet sur le texte scellé |
| 2 | « Livraison au côté moniteurs » | couvert par l'additif 2 (M-5, trois lignes pour le programme de l'extrait ; RP-10) |
| 3 | (3) fichier des identifiants | couvert par l'additif 2 (M-1, M-4 ; comptes : déclarés) |
| 4 | (4) fichier des textes | couvert par l'additif 2 (M-1, clause (b) : appel par défaut) |
| 5 | (5) conditions, adaptateurs | couvert par l'additif 2 (M-2) et expliqué par la fiche (RP-11) |
| 6 | (6) contexte | couvert par l'additif 2 (M-1, clause (d)) ; recette égale : attestée par la fiche |
| 7 | (9) lectures du dommage et de la diffusion | couvert par l'additif 2 (M-5 pour l'extrait) ; le reste sans effet sur le texte scellé |
| 8 | (11) fichier de l'oracle | sans effet sur le texte scellé |
| 9 | (12) commit et run | couvert par l'additif 2 (M-2, D-13) |
| 10 | (b) fichiers versés | couvert par l'additif 2 (M-2) |
| 11 | (c) distinguer les actions | couvert par l'additif 2 (M-1, clause (a)) |
| 12 | (d) tailles | sans effet sur le texte scellé (RP-7 inchangé ; comptes déclarés) |
| 13 | (e) ce que la passe ne relit jamais | couvert par l'additif 2 (M-2 ; P8 inchangée, liste fermée) |
| 14 | question des tâches de réserve | expliqué par la fiche (`taches.reserve_jouee_par_l_evaluation` « non ») |

Aucun « nœud ». Réserve de lecture : le bloc (e) v7 dit l'extrait des états « livré au seul lecteur des sondes » (la v6 : « côté moniteurs ») ; resserrement sans conséquence sur une règle, signalé pour mémoire.

## Conclusion

**À corriger** (corrections légères, aucune bloquante) : constats 1 (moyen), 5 (moyen), puis 2, 3, 6, 7, 9 (mineurs) ; 4, 8, 10 sont des remarques. Si la session mère accepte les constats 2, 3, 6, 7 et 9 comme réserves déclarées au rapport scellé, seuls 1 et 5 conditionnent un « conforme ».
