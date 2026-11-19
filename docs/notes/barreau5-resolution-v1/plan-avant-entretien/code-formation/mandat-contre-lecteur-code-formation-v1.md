# Mandat du contre-lecteur Fable 5.2 du code de formation des familles d'adaptateurs (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 19 novembre 2026 vers 17:00Z. Pièce de travail : elle dit quoi lire, quoi juger et quoi rendre.

---

Tu es un contre-lecteur neuf (Claude Fable 5.2) du programme de contrôle boîte blanche, dépôt `/home/user/controle-ia-travail`. Tu contre-lis une pièce d'instrument (classe B) écrite par un développeur Claude Opus 5.5 : le code qui formera, sur des cartes louées, les familles d'adaptateurs jumeaux du barreau 5. Tu es d'un autre modèle que l'auteur, comme le veut la règle des pièces d'instrument. Tu vérifieras ensuite toi-même ses corrections. Français, mots en clair. Aucune dépense, aucun lancement réel, aucun commit.

## Pièces (vérifie chaque empreinte : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement verifier <fichier>` pour les fichiers scellés ; pour le code, compare au § 5 du rapport v2)
- **Rapports du développeur** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/rapport-developpeur-code-formation-v1.md` (85004d61…) et `rapport-developpeur-code-formation-v2.md` (d24a76d1…). Le v2 donne au § 5 les empreintes complètes de tous les fichiers de code.
- **Code** :
  - `src/controle_ia/barreau5_familles/` : `edition_cout_v1.py`, `engagement_v1.py`, `formation_v1.py`, `__init__.py` ;
  - `scripts/lancer_b5f_formation_v1.sh` et `scripts/amorce_b5f_formation_v1.sh`.
- **Essais** : `tests/test_barreau5_familles_edition_cout_v1.py`, `tests/test_barreau5_familles_engagement_v1.py`, `tests/test_barreau5_familles_formation_v1.py`, `tests/test_lancer_b5f_formation_v1.py`, `tests/test_amorce_b5f_formation_v1.py` (161 essais).
- **Le texte qui fait foi pour ce code** : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` (525f338e…). Ce n'est pas encore la version scellée ; son contre-lecteur le vérifie. Il liste les sections figées pour le code de formation : lis-les en entier.
- **Autour** :
  - la contre-lecture du brouillon 2 (`docs/notes/barreau5-resolution-v1/plan-avant-entretien/contre-lecture-plan-sabotage-ou-empreinte-brouillon2-v1.md`), son constat M-5 en particulier ;
  - la table des corrections du brouillon 3 (`table-corrections-plan-brouillon3-v1.md`) ;
  - le devis du brouillon 3 (`devis-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md`) ;
  - le mandat du développeur (`mandat-developpeur-code-formation-v1.md`).
- **Modules réemployés**, à lire pour juger leur emploi : `src/controle_ia/organismes/lora.py`, `organismes/distillation.py`, `t06/distillation_transcription.py`, `t06/identite.py`, `t06/cout.py`, `t06/lanceur.py`, `harnais/`.
- **Outils du dépôt** : `.claude/hooks/garde_calcul.py`, `src/controle_ia/manifeste.py`, `src/controle_ia/scellement.py`.

## Ce que tu juges, au moins
1. **La conformité aux sections figées du brouillon 3** : familles, membres, graines, épisodes d'évaluation, sorties, engagement, liste d'arrêt, données gardées, calendrier des instances.
2. **L'opérateur d'édition du coût**, la pièce la plus délicate. Grille, valeur, écriture du nombre, épissure des jetons. Vérifie que les transcriptions des membres d'une famille ne diffèrent que par les jetons du nombre, et juge les choix que le texte ne fixe pas (rapport v1, § 4).
3. **Les invariants** :
   - aucun score de sonde, aucune activation lue ni écrite sur une instance de formation (liste d'arrêt, point 5, forme M-5a) ;
   - aucun score de sonde dans l'entraînement, le choix, l'arrêt ou l'exclusion d'un adaptateur (N-053) ;
   - graines par `numpy.random.SeedSequence` dérivées par tâche (R9) ;
   - arrêt et destruction par identifiant seulement (R10) ;
   - aucune sortie supprimée avant son versement (règle « récupérer ce qui est récupérable ») ;
   - aucune valeur de clé lue, écrite ou affichée.
4. **Les gardes** : chacune a-t-elle un cas sain qui passe et un artefact qui est refusé (R5) ? Un essai peut-il passer à vide, sans éprouver ce qu'il annonce ?
5. **Contrôle par mutation**, à la manière de R4. Réintroduis un à un, dans une copie hors du dépôt, une dizaine de défauts plausibles dans le code (par exemple : une activation écrite, une graine fixe, une sortie effacée avant versement, une épissure décalée d'un jeton, un engagement accepté après la création de l'instance de lecture). Dis lesquels les essais attrapent.
6. **Le lanceur et l'amorce** :
   - refus sans identifiant d'accord valide (garde de calcul) ;
   - lecture du registre propre au commit de la course ;
   - code identique à celui de la ligne `CODE-FORMATION-B5F` ;
   - coupures ;
   - minuterie de destruction par identifiant ;
   - branches de sortie par instance ;
   - essais d'une amorce sur l'instance.
7. **Les deux écarts déclarés au brouillon 3** (rapport v1, § 3) et les choix que le texte ne fixe pas (rapports v1 et v2) : qui doit les trancher (le texte, Lazar, la mère), et ta recommandation.

## Forme
- Verdict en tête, l'un des trois : « conforme », « conforme après ces corrections », « à reprendre ».
- Chaque constat est classé bloquant, majeur ou mineur. Chaque correction est donnée au plus près du code : fichier, lignes, avant, après.
- Tes outils et leur sortie, sous des noms neufs.

## Sorties (scellées par la commande ci-dessus, non commises)
1. `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/contre-lecture-code-formation-v1.md`
2. tes outils dans `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/outils-contre-lecture-code-formation-v1/`.

## Règles
- **Essais** : lance les 161 essais une fois, en commande simple depuis `/home/user/controle-ia-travail` : `PYTHONPATH=src .venv/bin/python -B -m pytest -q -p no:cacheprovider <les cinq fichiers>`. Ne lance jamais la suite entière du dépôt.
- **Mutations** : dans une copie hors du dépôt, sous le bloc-notes. Ne modifie jamais le code du dépôt.
- **Rien de réel** : ni réseau vers un loueur de cartes, ni création d'instance, ni lancement du lanceur ou de l'amorce hors de leurs essais.
- **Écriture** : écris tes fichiers seulement avec les outils d'écriture et d'édition de fichiers, jamais par une commande.
- **Garde du dépôt** : n'écris dans aucune commande le nom d'une commande d'arrêt par motif, ni un enchaînement d'arrêt de processus, ni `kill` avec ses options, même dans une recherche ; elle refuse ces commandes. Pour lire les lignes de l'amorce qui en parlent, utilise l'outil de lecture de fichiers.
- **Interdits de cloisonnement** : n'ouvre jamais un fichier dont le nom contient « consigne-privee » ou « conception-ii-b », ni `brouillons/ii-b-saboteur-budget-v1/`, la branche `lot/compte-4-v1`, la ligne R-2059, les notes « pour Lazar seul », le fichier des scores par unité du bras A, ni rien sous `/root/.claude/`.
- **Aucune donnée ni résultat** : n'ouvre aucun fichier de `diag/` ni aucun score, et aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ou de P3-bis.
- **Refus d'outil** : au premier refus, arrête-toi et dis-le, sans le contourner.
- **Rendu à la mère** : n'y recopie aucun nombre de résultat d'expérience close.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Les chemins et les empreintes de tes sorties.
3. Dix lignes au plus : le verdict ; le nombre de constats par classe ; les trois plus graves ; les mutations attrapées et manquées ; ce qui menace le gel du code le 22 novembre.
4. La liste des fichiers que tu as ouverts.
