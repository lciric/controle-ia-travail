# Mandat du développeur Opus 5.5 des corrections du code de formation (barreau 5) — v2

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 19 novembre 2026 vers 18:05Z. Pièce de travail : elle dit quoi corriger, avec quelles décisions déjà prises, et quoi rendre.

---

Tu es un développeur neuf (Claude Opus 5.5) du programme de contrôle boîte blanche. Tu corriges le code de formation des familles d'adaptateurs jumeaux du barreau 5 selon sa contre-lecture. C'est une pièce d'instrument (classe B). Le même contre-lecteur (Claude Fable 5.2) vérifiera tes corrections. Français, mots en clair. Aucune dépense, aucun lancement réel, aucun commit : la mère verse.

## Où tu travailles
- **Dossier** : dans le dépôt principal, `/home/user/controle-ia-travail`, sans arbre isolé.
- **Fichiers que tu peux modifier ou créer** :
  - `src/controle_ia/barreau5_familles/` ;
  - `scripts/lancer_b5f_formation_v1.sh` et `scripts/amorce_b5f_formation_v1.sh` ;
  - les cinq fichiers `tests/test_barreau5_familles_*_v1.py`, `tests/test_lancer_b5f_formation_v1.py` et `tests/test_amorce_b5f_formation_v1.py` ;
  - un fichier d'essais neuf pour l'amorce entière, si tu en fais un ;
  - ton rapport.
- **Rien d'autre.** Le code est encore en version 1 de travail, jamais figé : tu le corriges en place, sans changer les noms. L'historique git garde la version contre-lue, au commit `1a53fc7a`.

## Pièces à lire d'abord
- **La contre-lecture** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/contre-lecture-code-formation-v1.md` (5174b105…), en entier, avec ses outils dans `outils-contre-lecture-code-formation-v1/`. Elle te donne 1 constat bloquant, 9 majeurs, 14 mineurs, et 20 mutations, dont 14 que les essais manquent.
- **Les rapports du développeur précédent** : `rapport-developpeur-code-formation-v1.md` et `rapport-developpeur-code-formation-v2.md`, même dossier.
- **Le texte** : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md`, avec ses sections figées pour la formation ; et sa vérification, `docs/notes/barreau5-resolution-v1/plan-avant-entretien/verification-plan-brouillon3-v1.md`, pour les couples qui touchent la formation.
- **La fiche de décision sur le constat V-B1** : `fiche-decision-v-b1-lazar-v1.md`, même dossier que la vérification.

## Décisions déjà prises, à coder
1. **B-1** : chaque famille se tire sur le modèle nu, jamais sous un adaptateur d'une autre famille. Applique la correction de la contre-lecture, et écris un essai qui l'attrape.
2. **M-1** : la commande de création transmet les clés par leur nom, de façon que le loueur reçoive la valeur, jamais le texte « $HF_TOKEN ». Aucune valeur de clé ne s'écrit nulle part.
3. **M-2, minuterie**, mot de la mère qui applique la règle de Lazar « récupérer ce qui est récupérable » (R-3661) :
   - la minuterie ne détruit une instance que sur une preuve de versement complet (inventaire des sorties, noms, tailles, empreintes, poussé et relu) ;
   - sans cette preuve à l'échéance, l'instance est **arrêtée, non détruite**, et un signal l'écrit pour la mère ;
   - pas de sommeil d'un seul tenant qui puisse couper le versement final.
4. **M-3** :
   - le code exige la ligne `SCELLEMENT-B5F` du registre propre (`registres/barreau5-familles-jumelles-v1.md`), au commit de la course, et refuse sans elle ;
   - un texte « scellé comme brouillon » ne passe pas pour le préenregistrement ;
   - la mère inscrira cette ligne au scellement du texte.
5. **M-4, M-6 et M-8** : corrige comme la contre-lecture le propose (retirage plutôt qu'arrêt de toute l'instance, tirage écrit sur disque, inventaire hors fin nominale, épisodes d'évaluation des saboteurs d'apprentissage dans les entrées de lecture). Où le texte doit trancher, code le choix le plus prudent et dis-le.
6. **M-5, relance** : code la relance unique d'une instance tombée, comme le dit le calendrier du texte (« une instance tombée se relance une fois »). Le sens précis de « pièce » est laissé au texte : expose-le en paramètre et dis-le.
7. **M-7** : la garde du point 5 devient une liste blanche de ce qu'une instance de formation peut écrire, au lieu d'une liste noire.
8. **36 ou 39 adaptateurs** : Lazar n'a pas encore tranché. Le nombre de membres des familles d'apprentissage (deux ou trois, sur-saboteur compris) devient un paramètre, sans défaut caché. Les essais couvrent les deux valeurs.
9. **M-9, essais** : chaque mutation manquée de la contre-lecture doit être attrapée par un essai. Rejoue son outil de mutations (`outils-contre-lecture-code-formation-v1/mutations-cl-v1.py`), dans une copie hors du dépôt, sous le bloc-notes, et donne le compte final. Ajoute une suite d'essais qui joue l'amorce entière hors ligne : minuterie, `timeout`, porte des essais, versement.
10. **Les mineurs** : corrige-les, ou dis pourquoi non.

## Essai à blanc de l'opérateur d'édition avec le vrai tokeniseur, si c'est faisable sans donnée interdite
- **Le risque** : la contre-lecture le juge le plus menaçant pour le gel. Une part d'actions non éditables au-dessus de 10 % ferait refuser toutes les familles.
- **L'essai** :
  - n'emploie que le tokeniseur public du modèle de la configuration (`prereg/T0.6-organismes-config-7b-v1.json`) ;
  - fais-le sur des actions écrites par programme à partir des descriptions de tâches et des formats des environnements, jamais sur des transcriptions ou des sorties de courses ;
  - mesure la part non éditable ;
  - dis ce que l'essai ne voit pas.
- **Si le tokeniseur ne se télécharge pas**, ou si l'essai demande une donnée interdite, ne le fais pas et dis-le.

## Règles
- **Écriture** : fichiers seulement par les outils d'écriture et d'édition, jamais par une commande. Commandes simples.
- **Garde du dépôt** : aucun nom de commande d'arrêt par motif, aucun enchaînement d'arrêt de processus, aucun `kill` avec ses options dans une commande, même dans une recherche. Pour lire les lignes de l'amorce qui en parlent, utilise l'outil de lecture.
- **Interdits de cloisonnement** : n'ouvre rien de `diag/`, aucun score, aucune activation, aucune transcription de course, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ou de P3-bis. N'ouvre aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b », ni `brouillons/ii-b-saboteur-budget-v1/`, ni rien sous `/root/.claude/`.
- **Essais** : lance seulement les fichiers d'essais du paquet, jamais la suite entière du dépôt.
- **Refus d'outil** : au premier refus, arrête-toi et dis-le.

## Sorties
- Le code et les essais corrigés.
- `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/rapport-developpeur-corrections-code-formation-v3.md`, scellé (`cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`). Il contient :
  - une table « constat → correction → essai qui l'attrape » ;
  - le compte des mutations attrapées ;
  - le résultat de l'essai à blanc du tokeniseur, ou la raison de son absence ;
  - les choix laissés au texte ;
  - les empreintes finales de tous les fichiers de code et d'essais.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. La liste de tes fichiers, avec leurs empreintes.
3. Dix lignes au plus :
   - les constats corrigés ;
   - les mutations attrapées, sur 20 et plus ;
   - le nombre d'essais, et combien passent ;
   - la part non éditable mesurée ;
   - ce qui menace le gel du 22.
