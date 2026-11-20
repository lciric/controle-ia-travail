VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE HORS DE TON BLOC-NOTES ET DU DOSSIER `code-v5/` CI-DESSOUS (`ls` permis là seulement). TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. TOUTE REDIRECTION VERS UN CHEMIN COMPLET DE TON BLOC-NOTES (une redirection après `env -C` s'exécute dans le dossier courant du shell).

# Mandat du développeur — code de l'étage sur processeur du palier 0b, version 6 (après l'audit des trous du code v5) — v1

**EN ATTENTE DU MOT DE LAZAR.** Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur l'accord de la mère (14:46Z : « prépare sans rien sceller ni lancer. Le mandat du code v6 (Opus écrit, Sonnet vérifie, processeur seul), puis le brouillon de l'erratum v14 (Fable neuf), versés sur ta branche et marqués « en attente du mot de Lazar ». Le palier 0b ne part pas avant que Lazar donne un GO qui nomme la v14 : la v13 scellée reste le texte en vigueur »). Pièce d'instrument (classe B) : vérification par un autre modèle (S), vérification des corrections par le même ; puis l'erratum v14, contre-lu, **scellé seulement après le mot de Lazar**. Dossier P0B = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

## Qui

Un développeur neuf, modèle O, qui n'a écrit ni le texte, ni le code v1 à v5, ni leurs vérifications, ni l'audit. Tu signes « développeur, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- Le texte en vigueur : `P0B/preenregistrement-heritage-palier-0b-etage-processeur-v13.md` (`d9591d5bb53ba6688fdfe004ac5fee96ad8e1ea6093ab86850e4eecab177f959`, scellé, R-4295) : B8 (cases « sources », 200 000 sources, modes D, H, E point 6, « toutes les familles, en un seul lancement »), S7 (reliquat, part des entrées gardées, facteur d'enrichissement), étapes 5 à 9 (fichiers gelés, C1, C4, couche « confirmation »), annexe C, gardes et liste d'arrêt.
- **L'audit des trous** : `P0B/lecture-lancement-v1/audit-trous-code-v5-palier-0b-v1.md` (`8e965f80…`) — sa section « Ce que le code v6 doit porter », points 1 à 7, fait foi pour le périmètre ; la lecture `P0B/lecture-lancement-v1/lecture-lancement-palier-0b-v1.md` (`301d8932…`) pour la pièce du verrou et la forme du lancement.
- Le code v5 : `P0B/code-v5/` (rapport `a2966a3c…`, table `P0B/table-empreintes-code-v5.txt` `56bddae7…`), sa vérification `P0B/verification-code-palier-0b-v5-v1.md` (`0e2c46bb…`).

## Ce que tu fais

Le code v6 sous `code-v6/` de ton bloc-notes (même arborescence que `code-v5/`, copiée puis modifiée ; le v5 n'est pas touché) :
1. tirage des cases « sources » sous la couche « decisif », avec un **champ de mode** dans les étiquettes de graines (aucune graine existante ne change ; dis-le et éprouve-le) ;
2. le **mode dans le nom des cases** (deux cases qui ne diffèrent que par le mode ont deux dossiers) ;
3. un `lancer_famille` qui suit la clé `sources` (ou le nombre de tirages) de chaque case, tire **toutes les familles en un seul appel** et écrit **un seul manifeste** ;
4. des sorties scellées qui portent le **reliquat par bras**, la **part des entrées gardées** et le **facteur d'enrichissement** (S7 ; `enrichissement` de `statistique.py` appelée) ;
5. `etape_8`, avec **relecture des fichiers gelés vérifiée par leurs empreintes** (et des réglages gelés par leur compagnon) ;
6. `etape_9`, qui assemble ce que l'audit nomme en (c) (`lire_case`, `taux_par_nombre`, `cases_de_niveau`, `cases_a_confirmer`, `lancer_famille` couche « confirmation » à 100 000 tirages, `regle_de_confirmation`) ;
7. essais (cas sain et artefact, R5) pour chaque point, défauts neufs au banc (rejoué en entier), docstring d'`etapes.py` corrigé ; l'essai final « aucune graine décisive » passe ; le verrou (a) à (e) et la garde 27 inchangés.

**Rien du texte n'est tranché par toi** : ce que la v13 ne fixe pas (forme exacte du reliquat, lots, source étrangère de H dans ce mode, contenu des sorties) se déclare en remarque, avec une proposition marquée. Les sorties du v5 qui ne relèvent pas d'un point changé restent égales à l'octet (dis lesquelles changent, et pourquoi). Rapport `code-v6/rapport-developpeur-code-palier-0b-v6.md` avec table des empreintes, différentiels v5 → v6 (`diff -u`, fichier par fichier), essais (commande, comptes), banc, silences, et **la liste exacte de ce que l'erratum v14 devra inscrire au texte** (commit, table, règles neuves, « Ce qui demande un code v6 »). **Aucun programme de lancement décisif n'est écrit ni joué** ; si un programme de lancement est utile, écris-le à part, marqué « non lancé, en attente », sans l'exécuter hors d'un essai sur racine factice.

Ton bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-palier-0b-v6/`. Chaque fichier avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Essais : `env -C DOSSIER /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider CHEMIN` avec `PYTHONPATH=src` et les variables `HERITAGE_DEPOT` et `HERITAGE_COPIE_ORGANISME` que les essais du v5 exigent (vérification du code v5, écart déclaré) ; long : en tâche de fond.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille, aucune pièce d'autorisation écrite. Aucun appel à un fournisseur de modèles, aucune dépense. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucune valeur de clé. Aucun identifiant de modèle. Aucune publication d'artefact. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
