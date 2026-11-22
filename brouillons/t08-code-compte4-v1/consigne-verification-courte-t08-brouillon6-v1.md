# Consigne — vérification courte du différentiel de T0.8, du brouillon 5 au brouillon 6 (candidat) — v1

Écrite le 2026-11-14T03:58:09Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A), auteur des brouillons 5 et 6. Lot « compte 4 », tâche 3. **Aucune dépense, aucune instance, aucune clé.**

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
- Lecture seule, sauf les fichiers du § 5 (et des fichiers temporaires dans le bloc-notes `/tmp/claude-0/-home-user-controle-ia-travail/0bb788a7-74e8-52db-b35a-9747a8f95b86/scratchpad/verif-t08-b6/`, non versés). Aucune écriture git (ni `add`, ni `commit`, ni `push`, ni `checkout`, ni `fetch`, ni `worktree`) ; lecture git permise dans l'arbre `/home/user/t08-code-compte4-v1` seulement (`git -C /home/user/t08-code-compte4-v1 log|show|diff|ls-tree` sur les commits nommés ici et les chemins `src/controle_ia/t08/`, `tests/test_t08_*`, `docs/notes/t08-code-compte4-v1/`, `essai/t08-jouet-compte4-v1/`). Aucun appel réseau, aucune recherche sur la toile, aucun sous-agent.
- **Aucun fichier de `registres/`** ; **aucun fichier de P3-bis** (procédure du rendez-vous, consigne du lecteur, verdict, tout `docs/verdicts/verdict-P3-bis*`) ; **aucun fichier de T0.7** (ni `prereg/T0.7-*`, ni `src/controle_ia/t07/`) : tu n'en as pas besoin, et sa lecture t'exclurait du verdict de P3-bis ; si un passage du code t'y renvoie, écris-le en « non vérifiable » sans l'ouvrir.
- **Rien de `donnees/`, `diag/`, `runs/` à la racine d'un dépôt** (ni dans `/home/user/controle-ia-travail`, ni à la racine de `/home/user/t08-code-compte4-v1`) ; en particulier, **jamais** `donnees/20261007-082440-t05-extraction/taches-evaluation.json` (il porte les cibles réelles). **Permis** : les sorties **factices** de l'essai du développeur sous `/home/user/t08-code-compte4-v1/essai/t08-jouet-compte4-v1/a/` et `…/b/` (leurs sous-dossiers `diag/`, `runs/`, `donnees/`, `registres-factices/`, `prereg/`, `docs/` y sont des copies ou des fabrications de l'essai, sans donnée réelle ; les noms « t06-7b-jouet » y désignent un 7b **factice**).
- Pas de `verifier-arbre` ; `PYTHONPATH=src python3 -m controle_ia.scellement verifier <fichier>` sur fichiers nommés seulement.
- Dans un fichier nommé, `grep -n`, `sed -n` ou l'outil de lecture sur ce seul fichier ; `grep -n` permis aussi sur le seul dossier `src/controle_ia/t08/` et sur les fichiers `tests/test_t08_*_v1.py` de l'arbre ; jamais `grep -r` ailleurs, `find`, `ls -R`, `git grep`.
- Aucune lecture de sonde, de score ni de résultat d'aucune course réelle (tu lis des textes, du code et les sorties factices de l'essai jouet, rien d'autre).
- **Interdit du programme** : jamais de moyenne ni de médiane sur les jetons dans un score de sonde ; si tu en vois une dans le code, c'est un constat bloquant.
- **Modèles** : dans tout fichier que tu écris, ton modèle est « modèle B » et celui du développeur « modèle A » (R-2598), sans identifiant.


## 1. Qui tu es

Vérificateur **neuf**, sous-agent de la session du compte 4 ; tu n'as écrit ni T0.8 (brouillons 1 à 6), ni la base (A), ni le code de T0.8, ni aucune de leurs relectures, ni T0.6, T0.7 ou P3-bis. Ton modèle doit être **différent** du modèle A (N-052) ; ton identifiant ne figure que dans ton dernier message. Tu n'as vu aucun résultat de 7b, de la pièce HD ni de sonde. Exclu ensuite du verdict de T0.8. Français ; aucun sigle non développé.

## 2. Objet

Le brouillon 6 est écrit par programme sur le brouillon 5 : 14 couples, dont les quatre couples VT5C-01 à VT5C-04 de la vérification courte du brouillon 5 (rapport, version 3, qui fait foi) tels qu'écrits, et dix couples de l'auteur (T6-01 à T6-10) : statut de la phrase T5-19 (« nœud de Lazar, non scellable avant son mot », VT5-03), déclaration de vue de l'auteur (VT5-04), entrée « Contre-lecture 4 », relecture suivante, en-tête. Tu dis si le différentiel ne fait que cela, s'il applique fidèlement le rapport, et si chaque fait cité est juste.

## 3. Fichiers à lire (vérifie chaque empreinte)

| rôle | chemin | sha256 |
|---|---|---|
| **brouillon 6** | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon6.md` | `ff7b0ddda5294aaba7b51276f6dfb5c857a9df4c6c0c444d723cf28fd68c92c6` (compagnon) |
| brouillon 5 (base du différentiel) | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon5.md` | `0c0e43270a819974168646406e349f48b6441d9afbdfaeb9d78b976228aba22b` (compagnon) |
| brouillon 4 gelé (sections gelées) | `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md` | `7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5` (compagnon) |
| rapport de la vérification du brouillon 5, **version 3** (et, pour la seule entrée « Contre-lecture 4 », les versions 1 et 2 : empreintes) | `/home/user/controle-ia-travail/prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon5-verification-courte-v3.md` (`-v1.md`, `-v2.md`) | `f788bb73baa0d71f826d4778c2b2e2c55baa20383f2f49e777d670d849df6d7e` (compagnons) |
| script, couples, sortie de l'application ; appliquer | `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/faire-couples-t08-brouillon6-v1.py`, `couples-t08-brouillon6-v1.json`, `sortie-application-t08-brouillon6-v1.json` ; `appliquer-couples-t08-v1.py` | compagnons |
| validateur | `/home/user/controle-ia-travail/src/controle_ia/prereg.py` | — |

## 4. Ce que tu vérifies

1. **Différentiel** : rejeu des 14 couples sur le brouillon 5 dans le bloc-notes : sortie égale au brouillon 6 à l'octet ; aucun autre changement.
2. **Fidélité** : VT5C-01 à VT5C-04 égaux à ceux de la section « 3. Couples » du rapport v3 ; chaque constat VT5-01 à VT5-09 traité comme le dit l'entrée « Contre-lecture 4 » (appliqué, porté, ou statut écrit).
3. **Sections gelées** : « Hypothèse », « Prédiction », « Métrique », « Seuil », « Critères de lecture gelés », « Liste d'arrêt » égales à l'octet au brouillon 4 ; « Plan d'analyse » égal au brouillon 4 hors la seule ligne de T5-19 (dont le texte change par VT5C-04 et T6-04 seulement).
4. **Statut de T5-19** : la mention écrite (en-tête et point 1) suffit-elle à ce qu'aucun scellement ne se fasse sans le mot de Lazar ? Est-elle juste au regard de la règle « Gel vérifiable » ?
5. **Déclaration de vue** : est-elle une « déclaration de vue » au sens de la règle du gel (ce qui a été vu, sans changer ni seuil ni règle) ?
6. **Faits cités** : empreintes et verdicts de l'entrée « Contre-lecture 4 » et de l'en-tête conformes aux fichiers.
7. **Forme** : `problemes` ne relève que les six marqueurs ; aucun identifiant de modèle.

**Gravité** : comme au rapport du brouillon 5.

## 5. Ce que tu rends

`/home/user/controle-ia-travail/prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon6-verification-courte-v1.md`, scellé puis vérifié ; script éventuel à côté (`…-v1-calcul.py`), scellé, sortie recopiée à l'octet ; **aucun extrait portant un identifiant de modèle** dans le rapport ni dans la sortie du script. Si tu dois refaire ton rapport, version neuve sous nom neuf (R12), et dis-le. Sections : **0. Identité** (« modèle B ») ; **1. Verdict** (« candidat conforme », « conforme après les corrections listées » ou « non conforme » ; nombres de constats par gravité) ; **2. Constats** (`VT6-01`…, couple exact quand la correction est mécanique) ; **3. Couples** (bloc JSON) ; **4. Sections gelées** ; **5. Limites**. Dernier message : verdict en trois lignes, nombres, chemin et empreinte **de la version qui fait foi** (et du script), identifiant de modèle. Si ton temps s'épuise : rapport partiel scellé.
