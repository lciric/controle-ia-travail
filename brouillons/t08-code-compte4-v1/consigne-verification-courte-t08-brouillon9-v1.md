# Consigne — vérification courte du différentiel de T0.8, du brouillon 8 au brouillon 9 (candidat) — v1

Écrite le 2026-11-14T06:45:46Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A), auteur des brouillons 5 à 9. Lot « compte 4 », tâche 3. **Aucune dépense, aucune instance, aucune clé.**

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
- Lecture seule, sauf les fichiers du § 5 (et des fichiers temporaires dans le bloc-notes `/tmp/claude-0/-home-user-controle-ia-travail/0bb788a7-74e8-52db-b35a-9747a8f95b86/scratchpad/verif-t08-b9/`, non versés). Aucune écriture git (ni `add`, ni `commit`, ni `push`, ni `checkout`, ni `fetch`, ni `worktree`) ; lecture git permise dans l'arbre `/home/user/t08-code-compte4-v1` seulement (`git -C /home/user/t08-code-compte4-v1 log|show|diff|ls-tree` sur les commits nommés ici et les chemins `src/controle_ia/t08/`, `tests/test_t08_*`, `docs/notes/t08-code-compte4-v1/`, `essai/t08-jouet-compte4-v1/`). Aucun appel réseau, aucune recherche sur la toile, aucun sous-agent.
- **Aucun fichier de `registres/`** ; **aucun fichier de P3-bis** (procédure du rendez-vous, consigne du lecteur, verdict, tout `docs/verdicts/verdict-P3-bis*`) ; **aucun fichier de T0.7** (ni `prereg/T0.7-*`, ni `src/controle_ia/t07/`) : tu n'en as pas besoin, et sa lecture t'exclurait du verdict de P3-bis ; si un passage du code t'y renvoie, écris-le en « non vérifiable » sans l'ouvrir.
- **Rien de `donnees/`, `diag/`, `runs/` à la racine d'un dépôt** (ni dans `/home/user/controle-ia-travail`, ni à la racine de `/home/user/t08-code-compte4-v1`) ; en particulier, **jamais** `donnees/20261007-082440-t05-extraction/taches-evaluation.json` (il porte les cibles réelles). **Permis** : les sorties **factices** de l'essai du développeur sous `/home/user/t08-code-compte4-v1/essai/t08-jouet-compte4-v1/a/` et `…/b/` (leurs sous-dossiers `diag/`, `runs/`, `donnees/`, `registres-factices/`, `prereg/`, `docs/` y sont des copies ou des fabrications de l'essai, sans donnée réelle ; les noms « t06-7b-jouet » y désignent un 7b **factice**).
- **Jamais** `brouillons/ii-b-saboteur-budget-v1/consigne-privee-maitre-ii-b-*` (consigne privée du maître de (ii-b)) ni aucun fichier de `brouillons/iib-code-compte4-v1/` ou de l'arbre `/home/user/iib-code-compte4-v1` : tu n'en as pas besoin.
- Pas de `verifier-arbre` ; `PYTHONPATH=src python3 -m controle_ia.scellement verifier <fichier>` sur fichiers nommés seulement.
- Dans un fichier nommé, `grep -n`, `sed -n` ou l'outil de lecture sur ce seul fichier ; `grep -n` permis aussi sur le seul dossier `src/controle_ia/t08/` et sur les fichiers `tests/test_t08_*_v1.py` de l'arbre ; jamais `grep -r` ailleurs, `find`, `ls -R`, `git grep`.
- Aucune lecture de sonde, de score ni de résultat d'aucune course réelle (tu lis des textes, du code et les sorties factices de l'essai jouet, rien d'autre).
- **Interdit du programme** : jamais de moyenne ni de médiane sur les jetons dans un score de sonde ; si tu en vois une dans le code, c'est un constat bloquant.
- **Modèles** : dans tout fichier que tu écris, ton modèle est « modèle B » et celui du développeur « modèle A » (R-2598), sans identifiant.


## 1. Qui tu es

Vérificateur **neuf**, sous-agent de la session du compte 4 ; tu n'as écrit ni T0.8 (brouillons 1 à 9), ni la base (A), ni le code de T0.8, ni aucune de leurs relectures, ni T0.6, T0.7 ou P3-bis. Ton modèle doit être **différent** du modèle A (N-052) ; ton identifiant ne figure que dans ton dernier message. Tu n'as vu aucun résultat de 7b, de la pièce HD ni de sonde. Exclu ensuite du verdict de T0.8. Français ; aucun sigle non développé.

## 2. Objet

Le brouillon 9 est écrit par programme sur le brouillon 8 : 14 couples, dont les trois couples VT8C-01 à VT8C-03 de la vérification courte du différentiel du brouillon 6 au brouillon 8 tels qu'écrits, et onze couples de l'auteur (T9-01 à T9-11) : déclaration de vue complétée (VT8-04), sort de VT5-07 porté au marqueur `LIGNE_MOT_LAZAR_T5_19` (VT8-05), « (ii-b) » défini (VT8-06), renvoi dans « Ce que les auteurs savaient avant le scellement », entrée « Contre-lecture 6 », relecture suivante, en-tête. Tu dis si le différentiel ne fait que cela, s'il applique fidèlement le rapport du brouillon 8, et si chaque fait cité est juste.

## 3. Fichiers à lire (vérifie chaque empreinte)

| rôle | chemin | sha256 |
|---|---|---|
| **brouillon 9** | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon9.md` | `dae4cc12a2e9de07d97fc8e5739c5cf5db79b98f234be30d94c52dbf72fb64ef` (compagnon) |
| brouillon 8 (base du différentiel) | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon8.md` | `129b1db245e186040256c8630dfb585bcd2a1e1ab4ea7b8ff817696fbd3220a7` (compagnon) |
| brouillon 4 gelé (sections gelées) | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md` | `7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5` (compagnon) |
| rapport de la vérification courte du brouillon 8 et son script | `/home/user/controle-ia-travail/prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon8-verification-courte-v1.md` ; `…-v1-calcul.py` | `220fe2fd8fedef8a06626e22f630fdd916f58675d5c441473be9c62dcca7b6fc` ; `c738299edb8c720ad78f3dc626ab986b7adf6f5fcfab2d6ef160ab1b7f6ca266` (compagnons) |
| brouillon 9 : script, couples, sortie de l'application | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/faire-couples-t08-brouillon9-v1.py`, `couples-t08-brouillon9-v1.json`, `sortie-application-t08-brouillon9-v1.json` | `b015b54f8c5a11308c8fec547dbc35f87d0aaa64c2fcc61039e84d9d526af1aa`, `f10703563b80399bd1b7db1e40259501bfce4d1a1c9859d3fcb60b44431c6095`, `290477e7af98dbb16bd927f75f63adf0222e2261cf1e87f666ebbb6b1340ee77` (compagnons) |
| appliquer les couples | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/appliquer-couples-t08-v1.py` | `87e8464236a57ecbade88c90df0d98c50d0f3a502afc3ce81be913cb6f845c31` (compagnon) |
| journal du compte 4 (pour les faits cités par la déclaration de vue : C4-0045 à C4-0057) | `/home/user/controle-ia-travail/registres-provisoires/compte-4-2026-11-14-v10.md`, `…-v11-sans-identifiants.md`, `…-v16.md`, `…-v17.md`, `…-v19.md` | compagnons |
| validateur | `/home/user/controle-ia-travail/src/controle_ia/prereg.py` | — |

## 4. Ce que tu vérifies

1. **Différentiel** : dans le bloc-notes, rejeu du script `faire-couples-t08-brouillon9-v1.py` à la date et à l'heure de la ligne « Date » du brouillon 9 (couples égaux à l'octet au fichier versé), puis des 14 couples sur le brouillon 8 (sortie égale au brouillon 9 à l'octet) ; aucun autre changement.
2. **Fidélité** : VT8C-01 à VT8C-03 égaux à ceux de la section « 3. Couples » du rapport du brouillon 8 ; chaque constat VT8-01 à VT8-06 traité comme le dit l'entrée « Contre-lecture 6 ».
3. **Sections gelées** : « Hypothèse », « Prédiction », « Métrique », « Seuil », « Critères de lecture gelés », « Liste d'arrêt » égales à l'octet au brouillon 4 ; « Plan d'analyse » égal au brouillon 4 hors la seule ligne de T5-19, elle-même égale au brouillon 8.
4. **Déclaration de vue** (VT8-04, VT8-06) : reste-t-elle une déclaration de vue (ce qui a été vu, sans changer ni seuil ni règle) ; ce qu'elle dit lu est-il appuyé par les journaux nommés ; ce qu'elle dit de (ii-b) et de la section « Devis de la confirmation 7b » est-il juste dans ce que tu peux vérifier (le reste en « non vérifiable ») ; le renvoi ajouté dans « Ce que les auteurs savaient avant le scellement » est-il hors des sections gelées et sans effet sur une règle ?
5. **VT5-07** (VT8-05) : la ligne de la table des marqueurs dit-elle sans ambiguïté que la mère écrit le sort de VT5-07, et que le mot de Lazar ne porte que sur T5-19 ?
6. **Marqueurs et forme** : `problemes` ne relève que les sept marqueurs, une occurrence chacun ; aucun identifiant de modèle ; faits cités (empreintes, verdicts, renvois) de l'en-tête et de l'entrée « Contre-lecture 6 » conformes aux fichiers.

**Gravité** : *bloquant* : le différentiel fait autre chose que ce qui est décrit, ou une section gelée change ; *majeur* : à corriger avant le scellement ; *mineur* : le reste.

## 5. Ce que tu rends

`/home/user/controle-ia-travail/prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon9-verification-courte-v1.md`, scellé puis vérifié ; script éventuel à côté (`…-v1-calcul.py`), scellé, sortie recopiée à l'octet ; **aucun extrait portant un identifiant de modèle** dans le rapport ni dans la sortie du script. Si tu dois refaire ton rapport, version neuve sous nom neuf (R12), et dis-le. Sections : **0. Identité** (« modèle B ») ; **1. Verdict** (« candidat conforme », « conforme après les corrections listées » ou « non conforme » ; nombres de constats par gravité) ; **2. Constats** (`VT9-01`…, couple exact quand la correction est mécanique) ; **3. Couples** (bloc JSON) ; **4. Sections gelées** ; **5. Limites**. Dernier message : verdict en trois lignes, nombres, chemin et empreinte **de la version qui fait foi** (et du script), identifiant de modèle. Si ton temps s'épuise : rapport partiel scellé.
