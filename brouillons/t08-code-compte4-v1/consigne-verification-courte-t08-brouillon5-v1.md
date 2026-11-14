# Consigne — vérification courte du différentiel de T0.8, du brouillon 4 gelé au brouillon 5 (candidat) — v1

Écrite le 2026-11-14T03:48:14Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A), auteur du brouillon 5. Lot « compte 4 », tâche 3. **Aucune dépense, aucune instance, aucune clé.**

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
- Lecture seule, sauf les fichiers du § 5 (et des fichiers temporaires dans le bloc-notes `/tmp/claude-0/-home-user-controle-ia-travail/0bb788a7-74e8-52db-b35a-9747a8f95b86/scratchpad/verif-t08-b5/`, non versés). Aucune écriture git (ni `add`, ni `commit`, ni `push`, ni `checkout`, ni `fetch`, ni `worktree`) ; lecture git permise dans l'arbre `/home/user/t08-code-compte4-v1` seulement (`git -C /home/user/t08-code-compte4-v1 log|show|diff|ls-tree` sur les commits nommés ici et les chemins `src/controle_ia/t08/`, `tests/test_t08_*`, `docs/notes/t08-code-compte4-v1/`, `essai/t08-jouet-compte4-v1/`). Aucun appel réseau, aucune recherche sur la toile, aucun sous-agent.
- **Aucun fichier de `registres/`** ; **aucun fichier de P3-bis** (procédure du rendez-vous, consigne du lecteur, verdict, tout `docs/verdicts/verdict-P3-bis*`) ; **aucun fichier de T0.7** (ni `prereg/T0.7-*`, ni `src/controle_ia/t07/`) : tu n'en as pas besoin, et sa lecture t'exclurait du verdict de P3-bis ; si un passage du code t'y renvoie, écris-le en « non vérifiable » sans l'ouvrir.
- **Rien de `donnees/`, `diag/`, `runs/` à la racine d'un dépôt** (ni dans `/home/user/controle-ia-travail`, ni à la racine de `/home/user/t08-code-compte4-v1`) ; en particulier, **jamais** `donnees/20261007-082440-t05-extraction/taches-evaluation.json` (il porte les cibles réelles). **Permis** : les sorties **factices** de l'essai du développeur sous `/home/user/t08-code-compte4-v1/essai/t08-jouet-compte4-v1/a/` et `…/b/` (leurs sous-dossiers `diag/`, `runs/`, `donnees/`, `registres-factices/`, `prereg/`, `docs/` y sont des copies ou des fabrications de l'essai, sans donnée réelle ; les noms « t06-7b-jouet » y désignent un 7b **factice**).
- Pas de `verifier-arbre` ; `PYTHONPATH=src python3 -m controle_ia.scellement verifier <fichier>` sur fichiers nommés seulement.
- Dans un fichier nommé, `grep -n`, `sed -n` ou l'outil de lecture sur ce seul fichier ; `grep -n` permis aussi sur le seul dossier `src/controle_ia/t08/` et sur les fichiers `tests/test_t08_*_v1.py` de l'arbre ; jamais `grep -r` ailleurs, `find`, `ls -R`, `git grep`.
- Aucune lecture de sonde, de score ni de résultat d'aucune course réelle (tu lis des textes, du code et les sorties factices de l'essai jouet, rien d'autre).
- **Interdit du programme** : jamais de moyenne ni de médiane sur les jetons dans un score de sonde ; si tu en vois une dans le code, c'est un constat bloquant.
- **Modèles** : dans tout fichier que tu écris, ton modèle est « modèle B » et celui du développeur « modèle A » (R-2598), sans identifiant.


## 1. Qui tu es

Vérificateur **neuf**, sous-agent de la session du compte 4 ; tu n'as écrit ni T0.8 (brouillons 1 à 5), ni la base (A), ni le code de T0.8, ni aucune de leurs relectures, ni T0.6, T0.7 ou P3-bis. Ton modèle doit être **différent** du modèle A, auteur du brouillon 5 (N-052) ; ton identifiant de modèle ne figure que dans ton dernier message. Tu n'as vu aucun résultat de 7b, de la pièce HD ni de sonde. Exclu ensuite du verdict de T0.8 ; déclaré à la mère pour « qui a lu quoi ». Français ; aucun sigle non développé.

## 2. Objet

Le brouillon 5 de T0.8 est écrit par programme sur le brouillon 4 **gelé** (R-2251) : 19 couples (T5-01 à T5-19), appliqués une fois chacun. Il remplit le seul marqueur `COMMIT_CODE_T08` au commit `453a71e1c6729d7ec5d43e3a4a0e3522dfd38579` du code (branche `prep/t08-code-compte4-v1`), après contre-lecture du code, deux passes de corrections et deux vérifications. Il note les modèles « modèle A » et « modèle B » sans identifiant (R-2598, R-2605) et ajoute les entrées de relecture. Il ajoute **une phrase au point 1 du plan** (T5-19 : sorties et manifeste de la course de T0.8 elle-même, VCT8B-01), soumise à la mère. Tu dis si le différentiel ne fait que cela, sans signe, seuil, règle ni critère de lecture neufs, et si chaque fait cité est juste.

## 3. Fichiers à lire (vérifie chaque empreinte)

| rôle | chemin | sha256 |
|---|---|---|
| **brouillon 5** (vérifié) | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon5.md` | `0c0e43270a819974168646406e349f48b6441d9afbdfaeb9d78b976228aba22b` (compagnon) |
| brouillon 4 gelé (base du différentiel) | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md` | `7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5` (compagnon) |
| script des couples, paramètres, couples, sortie de l'application | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/faire-couples-t08-brouillon5-v3.py`, `parametres-t08-brouillon5-v1.json`, `couples-t08-brouillon5-v1.json`, `sortie-application-t08-brouillon5-v1.json` | compagnons |
| appliquer (motif du validateur) | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/appliquer-couples-t08-v1.py` | compagnon |
| pièce des empreintes du code | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/empreintes-code-t08-453a71e1-v1.md` | `797ac9672963a118d246d8161c4fe6da19cbdcdf8a24c30be175c6bac85af204` (compagnon) |
| relectures citées par les entrées neuves (en-têtes et verdicts seulement) | contre-lecture 1 du code `…/contre-lecture-1-code-t08-v1.md` ; vérifications `…/verification-courte-corrections-t08-v1.md`, `…/verification-corrections-2-t08-v1.md` (dossier `brouillons/t08-code-compte4-v1/`) ; vérification courte du brouillon 3 `/home/user/controle-ia-travail/prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon3-verification-courte-v1.md` ; rapports des corrections dans la branche (`/home/user/t08-code-compte4-v1/docs/notes/t08-code-compte4-v1/`) ; journaux `registres-provisoires/compte-4-2026-11-14-v3.md` (C4-0030) et `-v6.md` (C4-0037) | empreintes citées par le brouillon 5 |
| validateur et gabarit | `/home/user/controle-ia-travail/src/controle_ia/prereg.py` ; `prereg/gabarit-preregistrement-v1.md` | — |

Lecture git permise, sans écriture, dans `/home/user/t08-code-compte4-v1` : `git -C … show 453a71e1:<chemin>` et `ls-tree` pour recalculer les empreintes de la pièce.

## 4. Ce que tu vérifies

1. **Différentiel** (`diff` des deux brouillons, et rejeu des couples sur le brouillon 4 dans le bloc-notes : la sortie doit être égale au brouillon 5 à l'octet) : chaque changement vient d'un couple T5-01 à T5-19 ; aucun autre.
2. **Sections gelées** : seuls l'en-tête, le point 1 du plan (T5-19), le tableau du calendrier (identifiants de modèles), la section « Contre-lecture » et « Marqueurs à remplir » changent ; « Hypothèse », « Prédiction », « Métrique », « Seuil », « Critères de lecture gelés », « Liste d'arrêt », le reste du « Plan d'analyse » sont égaux à l'octet au brouillon 4 (vérifie par programme, section par section).
3. **T5-19** : la phrase ajoutée ouvre-t-elle une lecture de données de 7b, de sonde ou de résultat ? Contredit-elle « Ordre des lectures et embargo » ou la « Liste d'arrêt » ? Est-elle utile (le code la lit, VCT8B-01) et suffisante ? Gravité si elle reste soumise à la mère et qu'elle est refusée.
4. **Faits cités** : commit et empreintes de la pièce (recalcule-les toutes au commit `453a71e1`), empreintes et verdicts des relectures citées, entrée « Contre-lecture 3 » (brouillon relu, rapport, verdict, onze couples, R-2250, R-2251) conformes aux fichiers.
5. **Identifiants de modèles** : il n'en reste aucun ; la notation « modèle A » / « modèle B » ne change le sens d'aucune phrase (en particulier l'écart déclaré à N-052 de la contre-lecture 1).
6. **Forme** : `PYTHONPATH=src python3 -c "from controle_ia.prereg import problemes; print(problemes('brouillons/T0.8-bases-boite-noire-v0-v1-brouillon5.md'))"` : seuls les six marqueurs restants doivent être relevés.

**Gravité** : *bloquant* : un changement hors des couples, une section gelée touchée sans couple déclaré, un fait faux ; *majeur* : à corriger avant le scellement ; *mineur* : le reste.

## 5. Ce que tu rends

`/home/user/controle-ia-travail/prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon5-verification-courte-v1.md`, scellé puis vérifié ; script éventuel à côté (`…-calcul.py`), scellé, sortie recopiée à l'octet. Sections : **0. Identité** (« modèle B », heures `date -u`, fichiers lus et empreintes) ; **1. Verdict** (« candidat conforme », « conforme après les corrections listées » ou « non conforme ») ; nombres de constats par gravité ; **2. Constats** (`VT5-01`…, gravité, endroit, preuve, correction ; couple exact « ancien » → « nouveau » quand elle est mécanique, « ancien » présent une seule fois dans le brouillon 5) ; **3. Couples** (bloc JSON) ; **4. Sections gelées** ; **5. T5-19** ; **6. Limites**. Dernier message : verdict en trois lignes, nombres, chemin et empreinte du rapport (et du script), identifiant de modèle. Si ton temps s'épuise : rapport partiel scellé.
