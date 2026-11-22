# Consigne — vérification courte du différentiel de T0.8, du brouillon 6 au brouillon 8 (candidat) — v1

Écrite le 2026-11-14T06:29:26Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A), auteur des brouillons 5 à 8. Lot « compte 4 », tâche 3. **Aucune dépense, aucune instance, aucune clé.**

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
- Lecture seule, sauf les fichiers du § 5 (et des fichiers temporaires dans le bloc-notes `/tmp/claude-0/-home-user-controle-ia-travail/0bb788a7-74e8-52db-b35a-9747a8f95b86/scratchpad/verif-t08-b8/`, non versés). Aucune écriture git (ni `add`, ni `commit`, ni `push`, ni `checkout`, ni `fetch`, ni `worktree`) ; lecture git permise dans l'arbre `/home/user/t08-code-compte4-v1` seulement (`git -C /home/user/t08-code-compte4-v1 log|show|diff|ls-tree` sur les commits nommés ici et les chemins `src/controle_ia/t08/`, `tests/test_t08_*`, `docs/notes/t08-code-compte4-v1/`, `essai/t08-jouet-compte4-v1/`). Aucun appel réseau, aucune recherche sur la toile, aucun sous-agent.
- **Aucun fichier de `registres/`** ; **aucun fichier de P3-bis** (procédure du rendez-vous, consigne du lecteur, verdict, tout `docs/verdicts/verdict-P3-bis*`) ; **aucun fichier de T0.7** (ni `prereg/T0.7-*`, ni `src/controle_ia/t07/`) : tu n'en as pas besoin, et sa lecture t'exclurait du verdict de P3-bis ; si un passage du code t'y renvoie, écris-le en « non vérifiable » sans l'ouvrir.
- **Rien de `donnees/`, `diag/`, `runs/` à la racine d'un dépôt** (ni dans `/home/user/controle-ia-travail`, ni à la racine de `/home/user/t08-code-compte4-v1`) ; en particulier, **jamais** `donnees/20261007-082440-t05-extraction/taches-evaluation.json` (il porte les cibles réelles). **Permis** : les sorties **factices** de l'essai du développeur sous `/home/user/t08-code-compte4-v1/essai/t08-jouet-compte4-v1/a/` et `…/b/` (leurs sous-dossiers `diag/`, `runs/`, `donnees/`, `registres-factices/`, `prereg/`, `docs/` y sont des copies ou des fabrications de l'essai, sans donnée réelle ; les noms « t06-7b-jouet » y désignent un 7b **factice**).
- **Jamais** `brouillons/ii-b-saboteur-budget-v1/consigne-privee-maitre-ii-b-*` (consigne privée du maître de (ii-b)) ni aucun fichier de `brouillons/iib-code-compte4-v1/` ou de l'arbre `/home/user/iib-code-compte4-v1` : tu n'en as pas besoin.
- Pas de `verifier-arbre` ; `PYTHONPATH=src python3 -m controle_ia.scellement verifier <fichier>` sur fichiers nommés seulement.
- Dans un fichier nommé, `grep -n`, `sed -n` ou l'outil de lecture sur ce seul fichier ; `grep -n` permis aussi sur le seul dossier `src/controle_ia/t08/` et sur les fichiers `tests/test_t08_*_v1.py` de l'arbre ; jamais `grep -r` ailleurs, `find`, `ls -R`, `git grep`.
- Aucune lecture de sonde, de score ni de résultat d'aucune course réelle (tu lis des textes, du code et les sorties factices de l'essai jouet, rien d'autre).
- **Interdit du programme** : jamais de moyenne ni de médiane sur les jetons dans un score de sonde ; si tu en vois une dans le code, c'est un constat bloquant.
- **Modèles** : dans tout fichier que tu écris, ton modèle est « modèle B » et celui du développeur « modèle A » (R-2598), sans identifiant.


## 1. Qui tu es

Vérificateur **neuf**, sous-agent de la session du compte 4 ; tu n'as écrit ni T0.8 (brouillons 1 à 8), ni la base (A), ni le code de T0.8, ni aucune de leurs relectures, ni T0.6, T0.7 ou P3-bis. Ton modèle doit être **différent** du modèle A (N-052) ; ton identifiant ne figure que dans ton dernier message. Tu n'as vu aucun résultat de 7b, de la pièce HD ni de sonde. Exclu ensuite du verdict de T0.8. Français ; aucun sigle non développé.

## 2. Objet

Le brouillon 7 est écrit par programme sur le brouillon 6 (19 couples : VT6C-01 et VT6C-02 de la vérification courte du brouillon 6, tels qu'écrits, et T7-01 à T7-17 de l'auteur) ; le brouillon 8 est écrit par programme sur le brouillon 7 (12 couples de l'auteur, T8-01 à T8-12) après le mot de Lazar sur la phrase T5-19 du point 1 du plan : « go a pour T5-19 » (option (a) : phrase gardée, code inchangé), recopié tel quel au journal du compte 4 (C4-0054). Le brouillon 8 remplit le marqueur `MOT_LAZAR_T5_19` par ce mot et le remplace, pour l'inscription du mot au registre par la session mère et sa confirmation des trois points gardés, par `LIGNE_MOT_LAZAR_T5_19`. Tu vérifies le **différentiel du brouillon 6 au brouillon 8**, qui couvre les deux : il ne fait que cela, il applique fidèlement le rapport du brouillon 6 et le mot de Lazar, et chaque fait cité est juste.

## 3. Fichiers à lire (vérifie chaque empreinte)

| rôle | chemin | sha256 |
|---|---|---|
| **brouillon 8** | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon8.md` | `129b1db245e186040256c8630dfb585bcd2a1e1ab4ea7b8ff817696fbd3220a7` (compagnon) |
| brouillon 7 (étape) | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon7.md` | `1877e384cc639cd627b92af87f8c72775db160034d85ebf701dcc3256da4c017` (compagnon) |
| brouillon 6 (base du différentiel) | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon6.md` | `ff7b0ddda5294aaba7b51276f6dfb5c857a9df4c6c0c444d723cf28fd68c92c6` (compagnon) |
| brouillon 4 gelé (sections gelées) | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md` | `7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5` (compagnon) |
| rapport de la vérification courte du brouillon 6 (sections « 2. Constats » et « 3. Couples ») | `/home/user/controle-ia-travail/prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon6-verification-courte-v1.md` | `8794f9d7f772d85b76b2d2364f5e23dc8f2843f192e8b89b90c0c0246c287322` (compagnon) |
| brouillon 7 : script, couples, sortie de l'application | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/faire-couples-t08-brouillon7-v1.py`, `couples-t08-brouillon7-v1.json`, `sortie-application-t08-brouillon7-v1.json` | `3756a1bc40424ffae979607c721cfbb0e1c741f74166f3a10c982420862d51a3`, `ee0eec6ce32d31938ba6942fa74db51dfa41ffd4066da10d2174dd298c8fee93`, `9564d885e24ff82a65904b91466dcd3963b2bb471ae371cafc1819133d2aa709` (compagnons) |
| brouillon 8 : script, couples, sortie de l'application | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/faire-couples-t08-brouillon8-v1.py`, `couples-t08-brouillon8-v1.json`, `sortie-application-t08-brouillon8-v1.json` | `f0ab03563a68b3b4789ca4c672b3fcc7e3ac5306871a8e31ca629fa090361883`, `8451cb7e7ecbad8e8c643c8787327712b36705d7552e456338a9ca3475e466b4`, `cbff15303c05f85778141e21489daf638273f7292284b5dc3aedeb0c7082b869` (compagnons) |
| appliquer les couples | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/appliquer-couples-t08-v1.py` | `87e8464236a57ecbade88c90df0d98c50d0f3a502afc3ce81be913cb6f845c31` (compagnon) |
| journaux du compte 4 : mot de Lazar (v16, C4-0054) ; entrées C4-0047 et C4-0048 (v11) | `/home/user/controle-ia-travail/registres-provisoires/compte-4-2026-11-14-v16.md` ; `…-v11.md` | `190fb7ed632c52c36f3ece7d837b84d9f9529f830553bf46c1ae10021cec9288` ; `d1784495329b1aafb08e7c6193aa4835b1d8d6137a4055e40bc9d38b0905c74e` (compagnons) |
| validateur | `/home/user/controle-ia-travail/src/controle_ia/prereg.py` | — |

## 4. Ce que tu vérifies

1. **Différentiel** : dans le bloc-notes, rejeu des 19 couples du brouillon 7 sur le brouillon 6 (sortie égale au brouillon 7 à l'octet), puis des 12 couples du brouillon 8 sur le brouillon 7 (sortie égale au brouillon 8 à l'octet) ; rejeu des deux scripts `faire-couples-…` aux dates et heures écrites dans les en-têtes « Date » (couples égaux à l'octet aux fichiers versés) ; aucun autre changement.
2. **Fidélité au rapport du brouillon 6** : VT6C-01 et VT6C-02 égaux à ceux de sa section « 3. Couples » ; chaque constat VT6-01 à VT6-07 traité comme le dit l'entrée « Contre-lecture 5 » du brouillon 8.
3. **Fidélité au mot de Lazar** : le mot est recopié à l'identique (journal v16) ; le brouillon 8 le lit comme l'option (a), phrase gardée, code inchangé, et rien d'autre ; la phrase T5-19 du point 1 est **inchangée** hors du renvoi entre parenthèses ; aucun effet donné au mot avant son inscription par la session mère (marqueur `LIGNE_MOT_LAZAR_T5_19`, que le validateur refuse tant qu'il n'est pas rempli).
4. **Sections gelées** : « Hypothèse », « Prédiction », « Métrique », « Seuil », « Critères de lecture gelés », « Liste d'arrêt » égales à l'octet au brouillon 4 ; « Plan d'analyse » égal au brouillon 4 hors la seule ligne de T5-19.
5. **Marqueurs** : `problemes` ne relève que les sept marqueurs `CODE_MOTS_ET_COUT_T06`, `RUN_7B`, `EMPREINTES_ENTREES_7B`, `ENTROPIE_T08`, `GO_T08`, `LIGNE_DEPENSE_T08`, `LIGNE_MOT_LAZAR_T5_19`, une occurrence chacun ; la table des marqueurs et l'en-tête les nomment tous, avec qui les remplit.
6. **Déclaration de vue** (bornée au brouillon 8) : reste-t-elle une « déclaration de vue » au sens de la règle du gel (ce qui a été vu, sans changer ni seuil ni règle) ; ses ajouts sur (ii-b) touchent-ils 7a, 7b, la pièce HD ou une sonde ?
7. **Faits cités** : empreintes, verdicts et renvois de l'en-tête, de l'entrée « Contre-lecture 5 » et de la table des marqueurs conformes aux fichiers ; aucun identifiant de modèle.

**Gravité** : *bloquant* : le différentiel fait autre chose que ce qui est décrit, une section gelée change, le mot de Lazar est lu au-delà de ce qu'il dit ou prend effet avant son inscription ; *majeur* : à corriger avant le scellement ; *mineur* : le reste.

## 5. Ce que tu rends

`/home/user/controle-ia-travail/prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon8-verification-courte-v1.md`, scellé puis vérifié ; script éventuel à côté (`…-v1-calcul.py`), scellé, sortie recopiée à l'octet ; **aucun extrait portant un identifiant de modèle** dans le rapport ni dans la sortie du script. Si tu dois refaire ton rapport, version neuve sous nom neuf (R12), et dis-le. Sections : **0. Identité** (« modèle B ») ; **1. Verdict** (« candidat conforme », « conforme après les corrections listées » ou « non conforme » ; nombres de constats par gravité) ; **2. Constats** (`VT8-01`…, couple exact quand la correction est mécanique) ; **3. Couples** (bloc JSON) ; **4. Sections gelées** ; **5. Limites**. Dernier message : verdict en trois lignes, nombres, chemin et empreinte **de la version qui fait foi** (et du script), identifiant de modèle. Si ton temps s'épuise : rapport partiel scellé.
