# Vérification des corrections du code de l'instrument et de l'analyse du bras A, version 9 — v1

**Verdict : engageable.** Ni défaut bloquant ni défaut à corriger. Restent des mineurs et des précisions de texte.

- **C-1 de la version 8 tenu.** Le constat de lancement reconnaît maintenant une révocation par son sens. Elle est vue qu'elle soit mal orthographiée, écrite comme une décision, en minuscules, ou hors de la table. Un identifiant voisin, lui, n'est pas pris.
- **M-1, M-2 et M-4 tenus.** M-3 et M-5 sont des écarts motivés et acceptables.
- **Les cinq écarts du complément 1 sont tenus.**
- **Les trois points neufs du brouillon 31 sont portés.** Ce sont le mode de contrôle, la ligne qui cause l'arrêt et un seul nombre par dose pour l'agrégateur.
- **Garde statique.** Sur un faux dépôt, sous un crochet d'audit, elle n'ouvre ni ne liste rien de cloisonné, et un lien physique n'est plus ouvert.
- **Ce qui reste.** Deux limites, toutes deux sans passage à tort du code lui-même :
  - le mode de contrôle protège le rejeu par la procédure seulement : l'analyse ne sait pas qu'un contrôle a eu lieu (M-1 ci-dessous) ;
  - une ligne qui retire la configuration en n'en citant que l'empreinte abrégée n'est pas vue (M-2).
- **Les trois défauts de la partie A du relevé** sont des précisions de texte, non des questions pour Lazar.
- **Essais : 314 passés.**

## Pièces lues et conditions

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), même contre-lecteur que pour les versions 5 à 8.
- **Code** : commit `389879c8`. Les neuf modules `*_bras_a_v9.py`, les sept fichiers d'essais `tests/*_bras_a_v9.py` et `scripts/constat_de_lancement_discretion_bras_a_v2.py` répondent tous à leurs compagnons. Leurs empreintes sont celles de la note, par exemple :
  - `analyse_bras_a_v9.py` : `41824766…` ;
  - `graines_bras_a_v9.py` : `33e4e733…` ;
  - programme du constat v2 : `e7e20b2a…`.
- **Textes** :
  - brouillon 31 (`6fd71ee2…`), empreinte seulement ;
  - notes des brouillons 30 (`9730ffe9…`), partie 1 et 2, et 31 (`fea0c882…`), parties 1 et 2 ;
  - note du code v9 (`7ee7bb7c…`) et relevé v9 (`5de28a7f…`), en entier.
- **Essais** : la commande de la note donne **314 passés** (70 s) :

  ```
  PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v9.py tests/test_verdicts_bras_a_v9.py tests/test_graines_bras_a_v9.py tests/test_cloisonnement_bras_a_v9.py tests/test_permutation_etiquettes_bras_a_v9.py tests/test_mesures_bras_a_v9.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py
  ```

  L'essai du rédacteur qui passe la garde sur le vrai dépôt tourne sous un crochet qui refuse toute ouverture cloisonnée avant qu'elle ait lieu. Mes propres essais de la garde n'ont tourné que sur un faux dépôt.
- **Essais d'attaque** : données synthétiques, registres fabriqués, dans le bloc-notes sous `/tmp/claude-0/-home-user-controle-ia-travail/b7727ccc-db8b-5b89-bce1-17602831b69d/scratchpad/contre-lecture-code-v9/`. Chacun a sa sortie `….sortie.txt` :
  - `attaques_v9.py` : lignes neuves, rejeu sous le mode de contrôle, ligne de commande, constat, écarts du complément 1, agrégateur, M-1 ;
  - `audit_cloisonnement_v9.py` : faux dépôt et crochet d'audit, garde et `listages_a_relire`, lien physique ;
  - `attaques_cloisonnement_v9.py` : 24 modules plantés ;
  - `fuzz_livraison_v9.py` : 400 livraisons altérées au hasard ;
  - `essais.sortie.txt` : la commande de la note.
- **Heure** : 2026-11-19T19:44Z.

---

## 1. Défauts bloquants, défauts à corriger

Aucun.

## 2. Défauts mineurs

- **M-1. Le mode de contrôle ne protège le rejeu que par la procédure.**
  - Essai : constat sain, lecture interrompue après l'acte de reprise, puis une révocation entrée, mal orthographiée. Le contrôle la voit et le programme sort en code 1, sans écrire de fichier, le constat d'origine intact.
  - Mais un rejeu lancé sans tenir compte du contrôle est lu par l'analyse (« ne repère pas »), sur l'ancien constat sain.
  - Le rédacteur l'écrit comme une limite, et le brouillon 31 veut ce contrôle sans fichier. C'est donc conforme au texte, mais la seule barrière est l'enchaînement du rejeu.
  - Correction proposée au texte : faire sceller au contrôle sain un fichier versionné, par exemple `controle-de-lancement-bras-a-<date>.json`, distinct du constat d'origine, que l'analyse exigerait pour un rejeu après un acte de reprise. Le constat d'origine resterait intact, comme le texte le veut.
  - À défaut, le contre-lecteur de l'enchaînement devra vérifier ce point.
- **M-2. Un retrait de la configuration qui n'en cite que l'empreinte abrégée n'est pas vu.** `cite_l_empreinte` cherche l'empreinte entière. Une ligne du registre qui retire la configuration avec ses seize premiers signes, l'usage courant des registres, laisse le constat sain (essai). Un identifiant de GO écrit « GO 2099-01-01-01 », sans tiret, n'est pas vu non plus. Correction : regarder aussi un préfixe de seize signes au moins de l'empreinte de la configuration, ou écrire au texte, comme consigne de tenue, que toute ligne qui touche une configuration en cite l'empreinte entière.
- **M-3. Un constat écrit à la main passe** (date « x », commit « y »). C'est la limite écrite et voulue par le brouillon 29 : une garde de procédure. Rien à changer au code.

## 3. Correction de la version 8 et du complément 1 → tenue ou non

| point | jugement | preuve (rejouée contre v9) |
|---|---|---|
| C-1 révocation par le sens | **tenu** | « révocation », « revocation », décision « est révoqué », identifiant en minuscules, ligne hors de la table : malsain, avec l'identifiant de la ligne. `GO-…-011` : sain (juste) |
| M-1 valeur ajustée | **tenu** | dans le cas de ma vérification v8, `valeur_p_haut_holm = 100000000000000000029/2000000000000000000000` (> 0,05), état « indécis » ; `valeur_p_haut_holm_arrondie = 0.05` |
| M-2 retrait de la configuration | **tenu** (empreinte entière) | une ligne qui retire la configuration en citant son empreinte entière la fait dire non inscrite et rend le constat malsain. Reste M-2 ci-dessus (empreinte abrégée) |
| M-3 constat malsain non gardé | **écart motivé, acceptable** | le brouillon 31 veut le constat malsain sur la sortie standard, en une ligne JSON, versée au manifeste scellé ; aucun fichier. La trace existe |
| M-4 constat et moment de la lecture | **tenu** | l'acte (six champs) et les constats de l'étape (m) (onze champs) portent l'empreinte du constat ; une analyse sous une autre ligne que celle du constat est refusée ; mode de contrôle pour le rejeu (M-1 ci-dessus) |
| M-5 garde statique | **tenu** pour le lien physique (non ouvert, violation) ; **écart motivé** pour T0.8 reconnu au nom (limite écrite) | faux dépôt |
| écart 1, acte à cinq champs | **tenu** (six champs) | champs relus sur l'acte écrit |
| écart 2, fichier des grandeurs de l'étape (n) | **tenu** | `grandeurs-de-l-etape-n-bras-a.json`, cinq champs ; refus de rejeu de l'étape (n) après lui (code ; essais de panne du rédacteur, non rejoués par moi) |
| écart 3, constat à sept puis huit champs | **tenu** | `ligne_de_go` et `sha256_du_programme_du_constat` ; l'analyse confronte les deux |
| écart 4, `piece_source` | **tenu** | garde ordinaire « provenance non établie », **avant l'acte de reprise** : après ce refus, aucun acte, aucun fichier d'arrêt neuf. Une pièce dont `piece_source` n'est pas un objet : même garde |
| écart 5, lignes de révocation et valeurs fictives | **tenu** | une révocation d'identifiant `GO-0000-00-00-00` qui nomme la ligne employée : refusée. Une ligne fictive étrangère : rien |

Fouille de 400 livraisons altérées : 290 arrêts, tous l'événement nommé.

## 4. Les points neufs du brouillon 31 (question 2)

- **Mode de contrôle** (`--controle`) :
  - aucun fichier écrit, le constat d'origine intact (empreinte inchangée) ;
  - la même ligne JSON à huit champs sur la sortie standard, code 0 si sain, 1 si malsain ;
  - le contrôle prend la configuration, l'état figé et la ligne de GO d'origine, avec le registre courant, le commit et la date du moment (relevé B.5 : juste) ;
  - limite : M-1.
- **Ligne qui cause l'arrêt** : nommée sur la sortie d'erreur par son identifiant, jamais par son texte. Le mot « retiré » de la ligne fautive ne paraît ni sur la sortie standard ni sur la sortie d'erreur (essai en ligne de commande). Une ligne hors de la table est dite « ligne hors de la table ».
- **Agrégateur, un seul nombre par dose** :
  - une table de trois nombres, ou une liste, à la place du nombre d'une dose donne « non rapportée » à chaque dose, et **aucun** des nombres du contenu ne paraît dans le résultat (essai) ;
  - une table à trois doses seulement donne « non rapporté » en entier.

## 5. Les trois défauts de la partie A du relevé (question 3)

| point | nature | avis |
|---|---|---|
| A.1 pièce illisible quand la clé de provenance est inscrite | **précision** | Aujourd'hui, la même pièce corrompue donne une garde ordinaire si la configuration inscrit la clé, et un refus de la livraison (issue du point 21) si elle ne l'inscrit pas. Une configuration ne devrait pas changer l'issue d'une même pièce. Je recommande d'écrire qu'**une pièce dont `piece_source` ne se lit pas, ou qui n'est pas un objet JSON, est toujours « provenance non établie »**, que la clé soit inscrite ou non : on ne peut pas établir qu'elle est une livraison du module. C'est une classification, non une règle de jugement |
| A.2 provenance avant l'acte de reprise | **précision** | l'ordre du code est le bon : une pièce qui n'est pas la bonne ne dépense pas la ligne de GO. À écrire |
| A.3 résultat non recomposable après le fichier (n) | **précision** | recomposer le résultat de la règle sur les pièces scellées, sans relire le fichier des scores, est une fonction pure, et non une relecture. Je recommande d'écrire que ce n'est pas un rejeu, et de le permettre pour le rapport. À défaut, écrire que le rapport de la ligne C4 se compose avant la fin de l'étape (n), comme le code l'impose |

Aucun n'appelle le mot de Lazar.

## 6. La garde statique (question 4)

Faux dépôt, valeurs par défaut, crochet d'audit écrit à part :
- ni `violations_de_la_garde_statique` ni `listages_a_relire` n'ouvre ni ne liste un chemin cloisonné ;
- quinze chemins élagués, chacun par son nom, y compris sous une autre casse ;
- un départ cloisonné, ou par `..`, est refusé ;
- liens symboliques : non suivis ; lien physique : **non ouvert** (violation) ;
- des 24 modules plantés, 19 sont refusés, un est signalé (`glob` de `.jsonl`), et trois restes déclarés passent (`iterdir` sans extension, nom lu dans la pièce, programme rangé sous un chemin cloisonné), plus le témoin sain.

## 7. Ce que je n'ai pas regardé
- Les essais de panne du fichier des grandeurs de l'étape (n) et des dossiers (point 12 de la note du brouillon 30) : passés dans la commande, non rejoués par moi.
- Le texte des brouillons 30 et 31 hors des notes ; le reste des modules v9 hors des parties citées.

## 8. Fichiers ouverts
- `CLAUDE.md`.
- `docs/notes/relance-organismes-discrets-v1/code-v9-bras-a-note-v1.md` et `defauts-du-texte-trouves-en-codant-v9.md`, en entier ; `preenregistrement-v2-brouillon30-note-v1.md` (lignes 29 à 63) ; `preenregistrement-v2-brouillon31-note-v1.md` (lignes 30 à 55).
- Code : `scripts/constat_de_lancement_discretion_bras_a_v2.py`, en entier ; `graines_bras_a_v9.py` (lignes 181 à 290) ; `cloisonnement_bras_a_v9.py` (le lien physique) ; `analyse_bras_a_v9.py` (le fichier des grandeurs, par recherche).
- `tests/aide_bras_a_v9.py`, par différence avec la v8.
- **Non ouverts** :
  - aucun interne de moniteur, aucun module habilité, rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8 ;
  - aucune fiche de l'organisme d'idéation, aucune réponse de lecteur, aucune clé ;
  - ni le vrai registre ;
  - aucun appel réseau ni de modèle, aucun sous-agent, rien d'installé, rien committé.
