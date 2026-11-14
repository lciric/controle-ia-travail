# Consigne — vérification courte du brouillon 6 « validité de l'adaptateur » (commit C7 rempli) — v1

Écrite le 2026-11-14T06:38:35Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A), auteur des brouillons 4 à 6. Lot « compte 4 », tâche 1. **Aucune dépense, aucune instance, aucune clé.**

## 0. Interdits permanents (recopiés du brief du compte 4, section 6, sans changement)

- Aucune dépense ni machine louée sans ligne de GO inscrite **et** mot de Lazar.
- Aucune valeur de clé : jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
- Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`, `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a ou 7b, l'étiqueteur, `scripts/extraire_mesures_epreuve_t06_v1.py`, la branche `calcul/p3bis-reel-v2`.
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- Aucune recherche récursive qui traverse ces chemins : pas de `ls registres`, pas de `find` ni de `grep -r` larges ; fichiers nommés seulement.
- Jamais d'heure écrite à la main (`date -u` dans la même commande). Jamais de `git fetch` sans refspec.
- Garde des secrets à 0 avant chaque commit (sans objet ici : tu ne commites rien).
- Jamais toucher les instances Vast 58936096, 58936099, 58936100, 60480302, 60541314 ni les serveurs Hetzner `poste-temoin-bailey-*` ; aucun appel au loueur.
- Ne jamais contourner, reformuler ni confier à une autre session un refus de permission, du crochet ou d'un classifieur : arrêt, rapport à la mère.
- Rien de publié, aucun contact extérieur (tu rédiges, Lazar envoie).

**Ajoutés pour cette vérification.**
- Lecture seule, sauf les fichiers du § 5 (et des fichiers temporaires dans le bloc-notes `/tmp/claude-0/-home-user-controle-ia-travail/0bb788a7-74e8-52db-b35a-9747a8f95b86/scratchpad/verif-va-b6/`, non versés). Aucune écriture git (ni `add`, ni `commit`, ni `push`, ni `checkout`, ni `fetch`, ni `worktree`) ; aucun appel réseau, aucune recherche sur la toile, aucun sous-agent.
- **Aucun fichier de `registres/`** ; **aucun fichier de P3-bis** (procédure du rendez-vous, consigne du lecteur, verdict, tout `docs/verdicts/verdict-P3-bis*`) ; **rien de `donnees/`, `diag/`, `runs/`**.
- **T0.7** : tu **n'ouvres** ni `prereg/T0.7-*`, ni le contenu d'un fichier de `src/controle_ia/t07/` (tu resterais ainsi éligible aux rôles de P3-bis). Permis seulement, sans rien afficher du contenu : `git diff --stat` et `git ls-tree` sur les commits `b4cd9953` et `c2fab6cc7267b76228a75dc3e2e08bc7aa038961` pour `src/controle_ia/t07/`, et `git show <commit>:<chemin> | sha256sum` (empreinte seule). Ce que la pièce de confirmation dit du contenu (lignes, fonction changée) est « non vérifié, hors périmètre ».
- **Jamais** `brouillons/ii-b-saboteur-budget-v1/consigne-privee-maitre-ii-b-*` ni aucune pièce de (ii-b).
- Pas de `verifier-arbre` ; `PYTHONPATH=src python3 -m controle_ia.scellement verifier <fichier>` sur fichiers nommés seulement.
- Dans un fichier nommé, `grep -n`, `sed -n` ou l'outil de lecture sur ce seul fichier ; jamais `grep -r`, `find`, `ls -R`, `git grep`.
- Aucune lecture de sonde, de score ni de résultat d'aucune course.
- **Modèles** : dans tout fichier que tu écris, ton modèle est « modèle B » et celui de l'auteur « modèle A » (R-2598), sans identifiant.

## 1. Qui tu es

Vérificateur **neuf**, sous-agent de la session du compte 4 ; tu n'as écrit ni ce texte, ni ses brouillons, ni ses couples, ni leurs relectures, ni T0.7, ni son module ; tu n'es lecteur ni de P3-bis ni de T0.7 scellé. Ton modèle doit être **différent** du modèle A (N-052) ; ton identifiant ne figure que dans ton dernier message. Français ; aucun sigle non développé.

## 2. Objet

Le brouillon 6 du texte « validité de l'adaptateur » est écrit par programme sur le brouillon 5 : 14 couples de l'auteur (A6-01 à A6-14), produits par `faire-couples-brouillon6-v1.py` à l'annonce de la mère (journal du compte 4, version 18, C4-0056 : ligne `CODE-T07` remplacée une seule fois, nouveau commit C7 `c2fab6cc7267b76228a75dc3e2e08bc7aa038961`). Ils remplissent le marqueur `COMMIT_C7_T07`, citent la pièce de confirmation au commit de fusion, remplacent les identifiants de modèles par « modèle A » et « modèle B » (R-2605), et mettent à jour l'en-tête, la table du traitement et « Avant le scellement ». Tu dis si le différentiel ne fait que cela, si le commit est celui de l'annonce, et si chaque fait cité est juste.

## 3. Fichiers à lire (vérifie chaque empreinte)

| rôle | chemin (dépôt `/home/user/controle-ia-travail`) | sha256 |
|---|---|---|
| **brouillon 6** | `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon6.md` | `7f0a29d1e8a656b01e763b43a2948d90eb7cf8df0ea444f068d975716098a0f5` (compagnon) |
| brouillon 5 (base du différentiel) | `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon5.md` | `56fb63e9b2f4ae8cb8361e94568a99c4ddbdb219220670a7e05f004afdaead26` (compagnon) |
| générateur des couples | `brouillons/validite-adaptateur-v1/candidat1-pieces/faire-couples-brouillon6-v1.py` | `f92c31c31eb1a7b6727d58a6d863884a4939f450c821ee90aef20600336915c2` (compagnon) |
| couples appliqués | `brouillons/validite-adaptateur-v1/candidat1-pieces/couples-brouillon6-v1.json` | `540487c02f788ad0c796ac69c37863d619d71939cc733b0a011ee2f690f84a08` (compagnon) |
| script d'application | `brouillons/validite-adaptateur-v1/candidat1-pieces/appliquer-couples-vadapt-v2.py` | `933f0ebe4b97aa9aa5987a30e3f1898487c9dd6a241db71b2df2c2b67c978b71` (compagnon) |
| sortie de l'application | `brouillons/validite-adaptateur-v1/candidat1-pieces/sortie-application-couples-brouillon6-v1.json` | `bc9453722eeb99a634fbfc192a1547591b1b3631c9b95bc4ed4bdad21d70eb22` (compagnon) |
| pièce de confirmation au commit de fusion, v2 (la v1, fautive, n'est pas à lire) | `brouillons/validite-adaptateur-v1/candidat1-pieces/confirmation-champs-t07-fusion-c2fab6cc-v2.md` | `321b169aef79a0ef3291a88f08d60f83ceaacef400615a3d8c14f97de88a440f` (compagnon) |
| annonce de la mère, recopiée | `registres-provisoires/compte-4-2026-11-14-v18.md` (C4-0056) | `dc6fbfae2eb115731df920ef677870f3b03516f2a9877414fe14e205b4de8830` (compagnon) |
| validateur | `src/controle_ia/prereg.py` | — |

## 4. Ce que tu vérifies

1. **Rejeu** : dans le bloc-notes, `python3 -I brouillons/validite-adaptateur-v1/candidat1-pieces/faire-couples-brouillon6-v1.py 2026-11-14 06:37 c2fab6cc7267b76228a75dc3e2e08bc7aa038961 "message de la mère du 2026-11-14, R-2617 et R-2642, journal du compte 4, C4-0056 ; ligne `CODE-T07` remplacée une seule fois, S7 `bd4b7cd9`" /tmp/claude-0/-home-user-controle-ia-travail/0bb788a7-74e8-52db-b35a-9747a8f95b86/scratchpad/verif-va-b6/couples.json` : couples égaux à l'octet au fichier versé ; puis `appliquer-couples-vadapt-v2.py` (usage dans son en-tête) sur le brouillon 5 : sortie égale au brouillon 6 à l'octet ; aucun autre changement que les 14 couples.
2. **Commit** : le commit écrit dans le brouillon 6 est, à chaque occurrence, celui de l'annonce de la mère (C4-0056) ; le renvoi à l'annonce est juste ; aucune occurrence du marqueur ne reste.
3. **Couples, un par un** : chacun fait-il ce que dit l'en-tête du générateur ; introduit-il une erreur, une contradiction avec une autre section, une phrase historique réécrite à tort ?
4. **Pièce de confirmation** : dans les limites du § 0 (noms, statistiques, empreintes ; aucun contenu affiché), ses affirmations sur les fichiers changés entre `b4cd9953` et `c2fab6cc` et sur les empreintes sont-elles exactes ? Ce qu'elle dit du contenu : « non vérifié, hors périmètre ».
5. **Forme** : `PYTHONPATH=src python3 -c "from controle_ia.prereg import problemes; print(problemes('brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon6.md'))"` rend-il `[]` ; aucun identifiant de modèle dans le brouillon 6.
6. **Faits cités** : empreintes, numéros de décision et renvois de l'en-tête, de la table du traitement et de « Avant le scellement » conformes aux fichiers que tu peux lire ; le reste en « non vérifiable ».

**Gravité** : *bloquant* : le différentiel fait autre chose que ce qui est décrit, ou le commit n'est pas celui de l'annonce ; *majeur* : à corriger avant le scellement ; *mineur* : le reste.

## 5. Ce que tu rends

`/home/user/controle-ia-travail/prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon6-verification-courte-v1.md`, scellé puis vérifié ; script éventuel à côté (`…-v1-calcul.py`), scellé, sortie recopiée à l'octet ; aucun identifiant de modèle dans ces fichiers. Si tu dois refaire ton rapport, version neuve sous nom neuf (R12), et dis-le. Sections : **0. Identité** (« modèle B » ; heures `date -u` ; fichiers lus et empreintes) ; **1. Verdict** (« candidat conforme », « conforme après les corrections listées » ou « non conforme » ; nombres par gravité) ; **2. Constats** (`VB6-01`… ; couple exact « ancien » → « nouveau » sur le brouillon 6 quand la correction est mécanique, « ancien » présent une seule fois) ; **3. Couples** (bloc JSON) ; **4. Limites**. Dernier message : verdict en trois lignes, nombres, chemin et empreinte de la version qui fait foi (et du script), identifiant de modèle. Si ton temps s'épuise : rapport partiel scellé.
