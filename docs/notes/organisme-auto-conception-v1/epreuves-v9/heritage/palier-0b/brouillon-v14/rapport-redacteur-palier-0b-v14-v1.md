# Rapport du rédacteur — préenregistrement du palier 0b, version 14 (erratum après le code v6) — v1

**BROUILLON, EN ATTENTE DU MOT DE LAZAR.** Rien n'est scellé ; la version 13 scellée reste le texte en vigueur ; le palier ne part pas avant un GO de Lazar qui nomme la version 14. Pièce de travail (classe C). Rédacteur neuf, modèle F. 2026-11-20 (`date -u` : 17:46Z en cours de travail ; journal de l'outil : 17:54:49Z).

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v14/`. Abréviation : P = `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

## 1. Verdict

La version 14 est produite par **33 remplacements exacts** sur la version 13, tous appliqués ensemble par `scripts/remplacer_texte_exact_v1.py` (`391db990…`), sans avertissement. **Une seule ligne commence par « - Commit du code d'analyse : »** (compte : 1) ; elle porte le blanc `COMMIT_V6` (une seule fois dans le texte) et aucun groupe de quarante chiffres hexadécimaux entre accents graves (compte : 0). Le bloc qui la suit porte les 64 lignes de la table du code v6, dans son ordre, et rien d'autre. Aucun critère, aucun seuil, aucune valeur gelée, aucune prédiction, aucune issue n'est touché. Neuf points sont laissés en remarque, aucun tranché (§ 5). Aucun refus de permission, de classifieur ni de garde.

## 2. Fichiers et empreintes

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v14.md` (1 098 lignes) | `840400f3968095934c93b91fb6e3f8c8001953541b4df4f5546da4953af9ae4a` |
| `differentiel-palier-0b-v13-v14-v1.diff` (`diff -u`, 274 lignes) | `aa37724f16b828bdc32cccbeb379fb52776712be977d6ebd2ca55ab7e5599cc4` |
| `remplacements-palier-0b-v13-v14-v1.json` | `7d9c127602d4f69fc130ea4d5e7f7acec2708cda1c1dd84445c6c5596751328e` |
| `preenregistrement-heritage-palier-0b-etage-processeur-v14.md.journal-remplacements-v1.json` | `706b5869ce3bf44f821a6489086d709da25e4926e22dc5b869011c73d190bbaf` |

Chacun a son compagnon `.sha256` ; ce rapport reçoit le sien. Cible : la version 13, `d9591d5bb53ba6688fdfe004ac5fee96ad8e1ea6093ab86850e4eecab177f959` (égale au journal de l'outil).

Pièces vérifiées avant tout geste, chacune recalculée et égale à son compagnon : mandat (`2a44da18…`), version 13 (`d9591d5b…`), audit des trous (`8e965f80…`), rapport du code v6 (`0f408c6f…`), table extraite (`639335b9…`), vérification du code v6 (`a7d0b1bc…`), outil (`391db990…`). Sur `origin/main`, après un `git fetch`, au commit `84171548a934b7855efad1f187f1c17ea57c165b` : `registres/decisions.md` (`099edc1f…`) et `registres/go.md` (`61d52dc1…`), par `git show` redirigé. Les décisions de 17:41Z y sont inscrites : **R-4332** (17:41:48Z). Lues aussi : R-4285, R-4292, R-4295, R-4296, R-4304 ; GO-2026-11-20-25 et GO-2026-11-20-66.

## 3. Les 33 remplacements

Chaque ancre comptée par `grep -c -F -e` sur la version 13 avant l'appel : 33 fois « 1 ».

| n° | lieu de la version 13 | ce que fait le remplacement |
|---|---|---|
| 1 | titre | « v13 » devient « v14 » |
| 2 | statut (l. 3) | statut « BROUILLON, non scellé, en attente du mot de Lazar » et ligne de version, placés devant le statut de la version 13, repris tel quel |
| 3 | ligne de date (l. 6) | heures des versions 13 et 14 |
| 4 | ligne du commit (l. 7) | le commit du code v5 remplacé par le blanc `COMMIT_V6` ; « Version 14 » |
| 5 | ligne du commit | le contrôle « ancêtre de `main` » dit de la version 12 ; reste à faire pour le code v6 |
| 6 | ligne du commit | phrase de la table : 64 fichiers du code v6, table extraite `639335b9…` |
| 7 à 9 | table | lignes ajoutées : `lancer_etapes_8_et_9_v1.py` ; trois sorties du banc v5 ; `mutations_v5.py` |
| 10 à 13 | table | empreintes changées : `etalonnage.py`, `etapes.py`, `graines.py`, `tirages.py` |
| 14 | table | ligne ajoutée : essais `lancement` |
| 15, 16 | table | empreintes changées : essais `statistique`, `verrou` |
| 17 | mandats | mandat de la version 14 ; R-4304, R-4332, R-4295, R-4296 et GO-66 cités à la lettre, noms de modèle et identifiants de session omis |
| 18 | documents qui font foi | pièces de la version 14 |
| 19 | B7 bis | source étrangère au mode « sources » (silence n° 3) |
| 20 | B8, « Graines » (l. 332) | phrase « aucun programme de lancement … n'existant encore », corrigée (premier lieu) |
| 21 | B8, fin de « Graines » | alinéa « Version 14 » : modes, champ `mode`, lots, sorties scellées, nom des dossiers, `lancer_famille`, manifestes, empreinte du programme de lancement |
| 22 | M7 | dénominateur de R pris à la famille B (silence n° 16) |
| 23 | ordre des opérations, point 2 | ce qui est fait, ce qui reste, dans l'ordre |
| 24 | ordre des opérations, point 9 | `etape_8`, `etape_9`, case retirée |
| 25 | « Ce qui est rapporté » | reliquat : ventilation par génération perdue |
| 26 | « Ce qui est rapporté », fin | où se lisent l'enrichissement et les écarts du mode « sources » |
| 27 | section « Contre-lecture » | alinéa « Version 14 » |
| 28 | section « Contre-lecture » | fichiers à donner et points à vérifier en premier |
| 29 | annexe C | « Version 14 — le code v6 » : 117 essais, banc de 147 défauts, silences n° 14, 17, 18, 19 |
| 30 | réserve 24 | ce que le rédacteur de la version 14 a fait et n'a pas fait |
| 31 | annexe H, « Erratum du commit » | inscription refaite, commit en blanc |
| 32 | annexe H, « Version 12 », § 2, silence n° 14 (l. 991) | phrase corrigée (second lieu) |
| 33 | fin du texte | section neuve « Version 14 » de l'annexe H : onze points, dix-neuf silences, programme de lancement, comptes, « Ce qui demande un code v6 », trois remarques du § 8, huit remarques à la mère, nœud du GO, tenue |

Contrôles après l'appel : lignes « - Commit du code d'analyse : » : **1** ; lignes de la version 14 qui portent une ligne de la table extraite (`grep -c -F -f`) : 64 ; lignes en forme de table (deux espaces, 64 chiffres hexadécimaux, deux espaces) : 64 ; bloc relu à l'œil, dans l'ordre de la table extraite ; table extraite rejouée sur `P/code-v6/` du disque (`sha256sum -c` : 64 justes).

## 4. Ce que je n'ai pas fait

- Je n'ai lancé aucun code du palier, ni l'outil de lecture d'en-tête du verrou : que le verrou refuse un commit en blanc est ma lecture du motif de `graines.py` (code v6, l. 111 et 157), non un essai.
- Je n'ai pas lu la version 13 en entier (347 Ko) : l'en-tête, « Métrique », « Les six critères », B7 bis, B8, les huit points, l'ordre des opérations, « Ce qui est rapporté », la liste d'arrêt, « Contre-lecture », l'annexe C, les réserves 23 à 25, et, de l'annexe H, « Erratum du commit », la fin de « Version 9 » et « Version 12 ». Une phrase d'une section non relue que l'erratum rendrait fausse m'aurait échappé (dit à la réserve 24).
- Je n'ai lu ni le § 12 du rapport du code v6 (j'ai pris la table extraite), ni ses différentiels au-delà du début, ni la lecture pour le lancement, ni la vérification de la version 13.
- Le code v6 n'est pas sur `origin/main` au commit relu (constat par `git cat-file -e`) : le commit reste en blanc.

## 5. Points où la lettre ne suffit pas — en remarque, aucun tranché

Les huit premiers sont écrits au texte (annexe H, « Version 14 », § 7) ; le neuvième n'est qu'ici.

1. **Le blanc du commit.** Le remplir change l'empreinte du texte : la contre-lecture porte-t-elle sur le texte au blanc ou rempli, et le remplissage demande-t-il un contrôle de différentiel ? « Le mot de Lazar » et « le GO qui nomme la v14 » : un mot ou deux ? Pour remplir, la mère devra remplacer aussi les mots qui suivent le blanc (« — BLANC, À REMPLIR PAR LA MÈRE : … ne le porte pas. » et la phrase « Tant que ce blanc n'est pas rempli … et refuse. »), qui deviendraient faux.
2. **La mesure du temps et de la mémoire de l'étape 8**, que R-4332 dit « permise » : le mandat ne la porte pas ; l'annexe C borne l'essai de forme à 200 tirages et deux nombres de sources, et il n'est pas étendu au mode « sources ». Non inscrite.
3. **L'agrégation sur les sources** de la part des entrées gardées et des facteurs d'enrichissement (silence n° 5) : le rapport propose deux voies, la décision n'en choisit aucune. Non fixée.
4. **L'inventaire du § 6 du rapport du code v6** (« s'il est retenu ») : non repris, renvoi seulement.
5. **La lecture de la case retirée** (silence n° 10) : écrite à l'ordre des opérations et à l'annexe H, non dans la table des six critères, pour ne toucher aucun mot d'un critère.
6. **NE-2 et NE-3 de la vérification de la version 13**, « gardés pour une version suivante » (R-4295) : le mandat ne les nomme pas ; non portés.
7. **La pièce de contrôle de la mère** : à quelle ligne s'écrit l'empreinte du programme de lancement, et avec quel chemin.
8. **Les étapes 3 à 7** restent à jouer avant l'étape 8, et l'audit des trous dit qu'aucun programme ne les enchaîne : hors du mandat, signalé.
9. **La troisième remarque du § 8 du rapport** (le point 6 et le généraliste) : le mandat en nomme deux, le point 11 de la liste en nomme trois ; je l'ai portée, en remarque, avec les deux autres. Et une tenue : dans la ligne du commit, la phrase « **Version 14** : ce contrôle reste à faire … » précède la description du contrôle qu'elle nomme (celui d'ancêtre de `main`) ; le sens tient, la tournure est à reprendre si le contre-lecteur le veut.

## 6. Gestes et écarts

- Une commande simple par appel ; aucun heredoc, aucun code en ligne passé à un interpréteur ; le JSON est écrit par l'outil d'écriture ; aucune commande de liste ; `python3 --version` : 3.13.18.
- **Écarts déclarés** : un `git fetch origin main`, que l'en-tête du mandat ne nomme pas, pour lire `origin/main` à jour (comme les rédacteurs des versions 9 à 13) ; un `git rev-parse origin/main` et un `git cat-file -e` (code 128 attendu : le rapport du code v6 n'est pas sur `main`) ; un `grep` où des accents graves non protégés ont fait tenter au shell une commande « [0-9a-f]{40} » inexistante (« command not found », rien n'a tourné), refait correctement ; des `sha256sum`, `wc`, `cat` de compagnons, tous sur des chemins complets.
- Aucun lancement du code, aucun tirage, aucune pièce d'autorisation, aucun appel à un fournisseur, aucune dépense, aucune écriture dans le dépôt, aucun commit, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`, aucune publication.
- **À ne pas verser** : `decisions-origin-main.md` et `go-origin-main.md`, copies de lecture des registres laissées dans mon dossier ; elles portent des noms de modèle et des identifiants de session. Les pièces rendues n'en portent aucun.

Signé : rédacteur neuf, modèle F.
