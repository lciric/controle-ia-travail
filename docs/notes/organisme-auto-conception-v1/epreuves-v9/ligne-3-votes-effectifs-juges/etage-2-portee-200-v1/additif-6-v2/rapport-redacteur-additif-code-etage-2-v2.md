# Rapport du rédacteur — additif 6, version 2 (code de l'étage 2 à 200, ligne 3, organisme v9) — v2

Pièce de travail (classe C), écrite le 2026-11-20, même rédacteur (modèle F), même mandat (`a9663af401d1fcebfcaf626f2de104847ad44492760b98054cb1ae8478220695`, en-tête compris). Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-additif-code-etage-2/v2/`. La version 1 (`19016dcf3d0c735c7ff0ac30bf05c36a613eace4877bd463f8ffca63a0caa8a3`) et son rapport sont gardés sans modification.

## 1. Pièces reçues, empreintes recalculées

| pièce | sha256 |
|---|---|
| contre-lecture `E/additif-6-v1/contre-lecture-v1/contre-lecture-additif-6-v1.md`, « À corriger », lue en entier | `86bf181f1e4ddec7df3594e5cd028b4607976976d04884bcfd2e353c670e7cc9` |
| son jeu `jeu-corrections-additif-6-v1.json`, 32 remplacements | `11d3dedc91042080f24deee343ada64e0d3afb0fa93997810f9c6365894ed6f4` |
| outil `scripts/remplacer_texte_exact_v1.py`, lu en entier | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |
| relevé des essais sous l'interpréteur retenu | `6210dd81771ac1a3410d39aab9e31755e05b9da9a1dd850252e7030137a69619` |

## 2. Les deux passes

1. **Première passe : le jeu du contre-lecteur, tel quel.** `/usr/local/bin/python3 -I -B scripts/remplacer_texte_exact_v1.py --cible <v1> --remplacements <jeu> --sortie v2/passe-1-jeu-du-contre-lecteur-additif-6.md` : « FAIT : 32 remplacement(s) », sortie **`9751d78aa6f6993029d79627463727667690a2614af8982aa0ec87b40eee15a0`**, égale à l'essai du contre-lecteur. Heure du journal : 2026-11-20T16:46:30Z.
2. **Seconde passe : la tenue, de ma main**, par le même outil, sur la sortie de la première : jeu `jeu-tenue-redacteur-additif-6-v2.json`, « FAIT : 31 remplacement(s) ». Elle porte : la date (16:46Z, heure du journal) ; la phrase de version ; deux lignes de table (contre-lecture, jeu) ; les renvois aux lignes R-4324 à R-4327 là où l'additif disait « sans ligne au registre », « à inscrire », « rapportée » ou « à confirmer par la mère » ; la réserve 9 du § 14 ; trois lignes des pièces lues. Le titre et le statut viennent du jeu du contre-lecteur (C1, C2).

**Version 2 : `additif-6-code-etage-2-preenregistrement-ligne-3-v2.md`, `014b8e790dc4538edabf83e1e66c2294393bbbd1ab1e8de1ddcc3e2b2f38bc54`.**

Différentiels (`diff -u`) : `differentiel-additif-6-v1-v2.diff` (v1 → v2) ; `differentiel-additif-6-passe-1-v2.diff` (première passe → v2 : ma main seule).

## 3. Contestation écrite : aucune

Je n'ai refusé aucun des 32 textes du jeu. Ce que j'en ai relu contre les fichiers : les neuf empreintes qu'il ajoute, égales ; le contrat du lanceur de relais ; et que `reponse_sha256` du journal du compteur est l'empreinte des octets du fichier de réponse brute (code d'appel v4, l. 1031 à 1036), ce qui fonde la comparaison par empreinte du geste 11. **Non relu par moi** : les programmes des deux relais, la porte de plafond, les contrôles du lanceur de la course v9 cités au § 9. Ce texte des relais est celui du contre-lecteur ; rien n'en a été lancé.

## 4. Les lignes du registre, relues à la lettre

`git fetch origin main` fait ; tête `bed0187f320bf14fc0cb3bdc988549830ba0db23` ; `registres/decisions.md` `da56d7637bd849c5b06d50eb9cc30e206ba2b478b77dce7c55abf566e7ca307c` ; `registres/go.md` inchangé (`61d52dc1…`). R-4324, R-4325, R-4326 et R-4327 y sont.

**Ce que ces lignes ne nomment pas**, et que l'additif garde comme connu par la seule coordination (§ 14, réserve 6) :

- le partage « écrit tel quel » (n° 48) et l'échéance confirmée (n° 50), que le jeu dit « décidé » et « confirmé par la mère (16:27Z) » : R-4326 ne les porte pas ;
- le renvoi `MODELES_CLAUDE` à la déclaration du précédent : R-4327 ne le porte pas ;
- des cinq décisions de 15:20Z, R-4325 nomme le refus par l'historique et la portée par pièce, non la forme réelle seule, le journal existant sans manifeste, la lecture unique de la pièce du (4) ;
- les restes de procédure (n° 34) n'ont pas de ligne.

**Une nuance de lettre** : R-4326 écrit, pour la racine 2026111935, « écart déclaré, racine neuve et question à Lazar si l'aveugle est touché » ; c'est R-4327 qui dit « sans effet sur l'aveugle, déclaration seule ». L'additif cite les deux lignes ensemble.

## 5. Un point que je signale sans le contester

N° 49 (texte du jeu, C28) : le pire du juge Argon, 30,44 USD, « passe sur la carte Google sous GO-2026-11-20-64, au-delà des 15,41 USD que cette ligne nomme : déclaré ». Le texte n'est pas faux : GO-2026-11-20-68, de Lazar et postérieure, met le juge Argon sur la clé Google sous 88,36 USD, et R-4326 l'inscrit. Mais c'est une dépense possible au-delà d'un chiffre que nomme une ligne de Lazar : à lui dire au compte rendu.

## 6. Écarts

1. `git fetch origin main`, demandé par la coordination ; deux `git show origin/main:…` redirigés vers mon dossier (`main-decisions-v2.md`, `main-go-v2.md`).
2. La seconde passe est faite par l'outil du dépôt et non par l'outil d'édition : un journal en garde chaque zone.
3. La coordination m'a écrit deux fois (demande de la version 2 ; décisions inscrites et recommandations acceptées).
4. Aucun programme de l'étage 2 lancé ; aucune commande sur un chemin sous `archives-reponses-modeles/` ; aucun appel, aucune clé lue, aucune dépense ; aucune écriture dans le dépôt ni dans le clone ; aucune publication. **Aucun refus de permission, de classifieur ni de garde.**

Rédacteur neuf, modèle F.
