# Mandat du contre-lecteur neuf du lanceur de la première passe, version 7 — v1

Rédigé le 2026-11-21 par la session des lentilles. Classe B (instrument).
- **Toi** : agent neuf sur Opus 5.5.
- **Le développeur** : sur Fable 5.2, il a écrit les versions 4 à 7 du lanceur.
- **Le contre-lecteur précédent** : lui aussi sur Opus 5.5, il a contre-lu les versions 4 à 6. Il s'est arrêté avant de commencer la version 7, faute de mémoire de travail. Tu le remplaces.

## Les mots qui fondent le travail

Ces deux lignes sont relues par leur identifiant dans `registres/go.md` de la branche principale. Leurs textes sont cités ici ; tu n'ouvres pas les registres.
- **GO-2026-11-20-56** : le message entier d'un arrêt d'égalité ou des directions nulles va dans le seul fichier d'arrêt. La ligne de commande n'affiche que le nom de l'arrêt. Il faut un lanceur neuf et une liste de fichiers neuve dans la fiche du code.
- **GO-2026-11-21-06**, pour les lentilles :
  - les mots fixes de la ligne affichée sont gardés : « ARRÊT : », « fichier d'arrêt : <chemin> », « fichier d'arrêt non écrit », « versement à l'arrêt en échec : rien n'est supprimé » ;
  - une garde neuve est ajoutée : le lanceur refuse de partir si un `arret.json` existe déjà.

## Ce qu'on te demande

Dis si `lanceur_v7` (commit `cc7f4576`, branche `claude/brave-galileo-jhp684`) fait exactement ce qui suit, ni plus ni moins :
- `lanceur_v6`, déjà jugé conforme ;
- plus la garde de GO-2026-11-21-06.

Dis aussi si chaque garde est éprouvée sur un cas sain et sur un artefact (règle R5).

Ton verdict est l'un des trois suivants : **conforme**, **conforme sous corrections** (corrections numérotées) ou **non conforme**. Sépare les écarts bloquants des non bloquants.

## Pièces

Toutes sont sur la branche `claude/brave-galileo-jhp684`, commit `cc7f4576`. Fais `git pull origin claude/brave-galileo-jhp684` en nommant la branche.

**Code** (`src/controle_ia/lentilles_sondes_bbis/`)
- `lanceur_v7.py` (`a5d6fc7b…`), à lire contre `lanceur_v6.py` (`e0517259…`).
- `statistiques_v3.py`, où sont levés les deux arrêts cloisonnés. Il est inchangé.

**Essais** (`tests/`)
- `test_lentilles_sondes_bbis_lanceur_v7_garde_arret_present_v1.py` (`bc35c890…`).
- `test_lentilles_sondes_bbis_lanceur_v7_v1.py` (`c88cab55…`), à lire contre `…_lanceur_v6_v1.py`.
- `test_lentilles_sondes_bbis_lanceur_v7_interruptions_v1.py` (`9ed9e7ca…`), à lire contre `…_lanceur_v6_interruptions_v1.py`.
- `lentilles_sondes_bbis_jouets_v7.py`.
- Les six autres copies, toutes préfixées `test_lentilles_sondes_bbis_` : `addendum_concentration_v5`, `corrections_contre_lecture_v6`, `garde_egalite_v4`, `gardes_non_vues_v6`, `montage_v7`, `procedure_v7`.

**Notes** (`docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/`)
- `notes-lanceur-v7-v1.md`. Son § 2 porte cinq nœuds sur des chemins voisins.
- `empreintes-code-v7.txt` (`a2b5c098…`).
- `sortie-essais-v7.txt`.
- `outils/fabrique-lanceur-v7-v1.py`, `outils/essai-des-essais-v6.py` et `outils/sortie-essai-des-essais-v6.txt`.
- Pour le contexte : `notes-lanceur-v6-v1.md`, `notes-lanceur-v5-v1.md`.

**Contre-lectures précédentes**, pour le contexte (`docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/`)
- `contre-lecture-lanceur-v5-messages-arret-v1.md` (`d821cf66…`).
- `verification-correction-lanceur-v6-v1.md` (`23f466a8…`).

**Pour mémoire**, sur la branche principale, par `git show origin/main:<chemin>` :
- l'addendum `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md` (`7c738708…`), section EC-6 ;
- la section « Qui, quelle machine, quel coût » de `prereg/lecture-sondes-bbis-par-lentilles-v1.md` (`ca5066d7…`).

## À vérifier

1. **Empreintes** : vérifie celles des pièces, puis `empreintes-code-v7.txt` contre le disque, avec `grep -v '^#' … | sha256sum -c`.
2. **Fabrique**
   - Rejouée sur une copie de `lanceur_v6`, elle doit rendre `lanceur_v7` à l'octet près, ainsi que les copies d'essais.
   - Aucune ligne de calcul ne change, et rien ne change d'autre que la garde.
   - Le cloisonnement des messages et les fermetures de la version 6 restent intacts.
3. **La garde `exiger_aucun_fichier_d_arret`**
   - Elle passe avant la fiche du code, tout registre, toute requête, tout chargement et `etat["parti"]`.
   - Le chemin gardé est celui où l'enveloppe écrit l'arrêt.
   - Elle n'écrit ni ne supprime rien.
   - Elle traite un fichier vide et un lien cassé.
   - Une relance après un premier arrêt cloisonné est refusée, sans qu'aucun mot du premier message ne sorte.
4. **Les deux copies d'essais dont le contenu change**
   - Les changements sont-ils légitimes, et aucune épreuve n'est-elle perdue ?
   - La défense du versement, quand un fichier apparaît après la garde, est-elle toujours éprouvée ?
   - La constante `OUTIL` de la copie des interruptions est morte : est-ce sans effet ?
5. **Les cinq nœuds du § 2**
   - Pour chacun, dis si la garde accordée l'exige, le permet, ou s'il est hors de son champ.
   - Le développeur recommande de ne rien garder de plus pour les points 1 à 4, et d'écrire une consigne dans le mandat de l'opérateur pour le point 5.
6. **Essais**
   - Joue le paquet entier une fois : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_lentilles_sondes_bbis_*.py`. Il dure environ 15 à 25 minutes ; le développeur rapporte 2 052 réussis.
   - Joue tes propres altérations de la garde, chacune dans une copie jetable du paquet. Le contre-lecteur précédent aurait joué celles-ci :
     - la garde appelée après la fiche du code ;
     - la garde visant un autre chemin ;
     - la garde aveugle à un fichier vide ;
     - la garde aveugle à un lien cassé (`exists()` au lieu de `lexists`) ;
     - la garde qui affiche le premier message ;
     - la défense du versement retirée.

## Outils jetables que tu peux reprendre

Ils se trouvent dans le bloc-notes, sous `/tmp/claude-0/-home-user-controle-ia-travail/4c8fa2bf-6366-5665-a27b-6d403d9264f6/scratchpad/contre-lecteur-code-v1/`. Le contre-lecteur précédent les a écrits.
- `venv/` : torch 2.14.1 en version processeur et `requirements-cpu.txt`, déjà installés.
- `v5/scenario2.py` et `v5/jouer2.sh` : ils jouent chaque chemin d'arrêt avec des valeurs témoins et injectent les interruptions de la version 6. Pour viser `lanceur_v7`, ajoute ce nom dans la boucle. La variante `deja_la` pose un `arret.json` avant le calcul.
- `mutations-v6/` : la manière de poser des copies jetables du paquet.

Lis ces outils avant de t'en servir. Tes propres fichiers jetables vont sous `/tmp/claude-0/-home-user-controle-ia-travail/4c8fa2bf-6366-5665-a27b-6d403d9264f6/scratchpad/contre-lecteur-lanceur-v7/`.

## Ce que tu n'ouvres jamais

- La liste « Jamais ouverts » du texte de lecture v1 ou v2, et tout ce qu'elle nomme.
- Toute sortie, tout score, toute table, toute lecture ou tout verdict de l'apprentissage des sondes sur la tâche (étape B bis), y compris la clé `VERDICT-BBIS` et la note de lecture réservée à Lazar.
- Toute table ou sortie de la lecture par la lentille publique.
- `diag/`, `runs/`, `donnees/`, `docs/verdicts/`.
- Les branches `donnees/*`, `calcul/*` et `verdict/*` : ni extraites ni lues. Fais tes `fetch` et tes `pull` en nommant la branche, et déclare tout nom affiché.
- Tout fichier dont le nom contient « consigne-privee » ou « conception-ii-b », et `brouillons/ii-b-saboteur-budget-v1/`.
- P3, P3-bis, T0.6, T0.7 hors des textes cités, l'étape B, le bras d'attaque, le saboteur à budget.
- Tout registre de la branche principale.
- Aucune clé, aucun secret.

## Règles de travail

- Tu n'écris rien dans le dépôt : aucun commit, aucun push. Ton rendu est ton message final, que la session des lentilles versera scellé.
- Rien ne se télécharge en dehors de l'environnement existant, rien ne se loue, rien ne se dépense.
- Un refus d'outil n'est jamais rejoué, reformulé ni contourné ; il est déclaré.
- Aucune règle neuve. Là où le texte est muet, rapporte un nœud pour Lazar.
- Langue : français, en nommant les choses en clair.

## Forme du rendu

1. Verdict.
2. Empreintes.
3. Décompte des essais.
4. Points 1 à 6.
5. Corrections, d'abord les bloquantes, puis les non bloquantes.
6. Nœuds pour Lazar.
7. Expositions et refus d'outil.
