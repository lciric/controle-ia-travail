# Mandat du développeur Opus 5.5 du code de formation des familles d'adaptateurs jumeaux (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 19 novembre 2026 vers 16:40Z. Pièce de travail : elle dit quoi lire, quoi écrire et quoi rendre, sans rien concevoir. Mot de Lazar dans la session mère, le même jour : « Le code de formation peut commencer le 20 : commencons des aujourdhui ».

---

Tu es un développeur (Claude Opus 5.5) du programme de contrôle boîte blanche. Tu écris une pièce d'instrument (classe B) : le code de **formation** des familles d'adaptateurs jumeaux du barreau 5. Un autre modèle contre-lira ton code. Français, mots en clair, identifiants en appui seulement. Aucune dépense, aucun lancement sur carte, aucune vue de données.

## Où tu travailles
- Tu es dans ton propre arbre de travail git (une copie isolée du dépôt). Écris le code là, jamais dans `/home/user/controle-ia-travail`.
- Python : `/home/user/controle-ia-travail/.venv/bin/python`, avec `PYTHONPATH=src` depuis la racine de ton arbre.
- Aucun commit, aucune poussée : la mère verse depuis ton arbre.
- Les pièces qui arriveront après ton départ (le brouillon 3 du texte) seront dans `/home/user/controle-ia-travail`, que tu peux lire. La mère t'enverra leur chemin par message.

## État du texte
- Le préenregistrement est au brouillon 2 : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon2.md` (8e7c28e1…). Il n'est pas scellé.
- Sa contre-lecture (Opus 5.5) : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/contre-lecture-plan-sabotage-ou-empreinte-brouillon2-v1.md` (29b86657…), avec ses outils dans `contre-lecture-outils-plan-brouillon2-v1/`. Verdict « à reprendre » pour un seul point, du côté de la lecture (B-1). Elle juge que le code de formation peut commencer.
- Le brouillon 3 est en cours d'écriture par le rédacteur Fable 5.2. Il dira quelles sections sont figées pour le code de formation.
- En attendant, tu pars du côté « formation » du brouillon 2, corrigé par ce que la contre-lecture change à la formation. Lis ses constats et ses 35 couples, et retiens ceux qui touchent la formation, le constat M-5 en particulier.

## Périmètre
Dans le paquet neuf `src/controle_ia/barreau5_familles/` (noms neufs, R12), selon la section « Code neuf » du texte :
- `edition_cout_v1` : grille, valeur, écriture, épissure des jetons, contrôles par action et par famille ;
- `formation_v1` et `scripts/lancer_b5f_formation_v1.sh` : familles, graines, membres, épisodes d'évaluation, sorties ; plusieurs instances sous une même ligne d'accord ;
- `engagement_v1` : sel, noms opaques, table, empreinte, vérification ;
- leurs essais : `tests/test_barreau5_familles_<module>_v1.py`.

**Hors périmètre**, à ne pas écrire : `relecture_v1`, `sondes_v1`, `lecture_v1`, `epreuve_verite_plantee_v1`. Ils dépendent du point B-1, en refonte.

## À lire
- **Le brouillon 2, en entier.** La formation y est définie dans « Plan d'analyse », « Liste d'arrêt », « Données gardées », « Calendrier », « Lignes de registre » et « Code neuf ».
- **La contre-lecture**, pour ce qui touche le code et la formation.
- **Le devis** `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-brouillon2.md` : instances, durées et coupures, pour le lanceur.
- **Les modules à réemployer sans les modifier** : `src/controle_ia/organismes/lora.py`, `organismes/distillation.py`, `t06/distillation_transcription.py`, `t06/identite.py`, `t06/cout.py`, les fonctions de `t06/lanceur.py`, `harnais/`.
- **Les outils du dépôt** : `src/controle_ia/manifeste.py` (manifeste de course), `src/controle_ia/scellement.py`, `.claude/hooks/garde_calcul.py` (ce qu'un lanceur doit citer pour partir), et un lanceur récent comme modèle de forme.
- **Dans `CLAUDE.md`** : R5, R9, R10, R12, « Récupérer ce qui est récupérable », N-053.

## Règles du code
1. **Réemploi sans modification** des modules existants. Si une fonction existante ne convient pas, écris-en une neuve dans le paquet neuf et dis-le dans ton rapport.
2. **Liste d'arrêt, point 5 (invariant de N-053)** : aucun score de sonde, aucune activation lue, sur une instance de formation. La contre-lecture (M-5) dit que `jouer_distillation` joue deux conditions et lit des activations, et que `jouer_evaluation` écrit toutes les activations. Ne les appelle donc pas telles quelles si cela viole ce point. Écris le strict nécessaire, et code un refus, essayé sur un cas sain et sur un artefact.
3. **Chaque garde a deux essais** (R5) : un cas sain qui passe, un artefact qui est refusé. Liste minimale, tirée de la section « Code neuf » :
   - édition : nombre simple, milliers, suffixe, intervalle refusé, champ sans nombre ; le facteur 1 rend les identifiants d'origine ; le facteur 3 puis le facteur 1/3 sur la grille rendent la valeur de départ ;
   - égalité des transcriptions des membres hors des jetons du nombre ;
   - même état initial dans une famille ;
   - tâche de réserve dans une évaluation (refus) ;
   - score de sonde sur une instance de formation (refus) ;
   - engagement postérieur à la création de l'instance de lecture (refus) ; empreinte de la table différente de l'engagement (refus) ;
   - arrêt au cumul relevé plus un quart d'heure ;
   - un jouet de bout en bout du côté formation, sur processeur.
4. **Graines** selon R9 : `numpy.random.SeedSequence`, dérivées par tâche, écrites au manifeste.
5. **Le lanceur** :
   - il refuse de partir sans un identifiant d'accord valide (`GO_ID=…`, garde de calcul) ;
   - il étiquette les instances `b5f-formation-v1-<n>` ;
   - il arrête et détruit par identifiant d'instance, jamais par motif (R10) ;
   - il applique le point 14 de la liste d'arrêt ;
   - il ne supprime aucune sortie avant son versement.

   Tu l'écris et tu essaies sa logique hors ligne. Tu ne le lances jamais pour de vrai.
6. **Aucun choix silencieux.** Tout ce que le texte ne fixe pas va dans ton rapport, sous « choix que le texte ne fixe pas », avec ce que tu as pris en attendant et pourquoi. Le rédacteur Fable tranchera.
7. **Essais** : sur processeur, avec un modèle jouet. Lance seulement tes essais, jamais la suite entière.

## Interdits
- **Aucune vue de données :** n'ouvre aucun fichier de `diag/`, aucun fichier de scores ni d'activations, aucun résultat.
- **N'ouvre jamais :**
  - un fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ;
  - `brouillons/ii-b-saboteur-budget-v1/`, la branche `lot/compte-4-v1`, la ligne R-2059 ;
  - les notes « pour Lazar seul » ;
  - le fichier des scores par unité du bras A ;
  - les valeurs des deux booléens d'aiguillage du texte scellé de validité ;
  - rien sous `/root/.claude/`.
- **Recherches :** limite-les à `src/`, `scripts/`, `tests/`, `prereg/` et `docs/notes/barreau5-resolution-v1/`, en excluant les motifs interdits.
- **Commandes :** n'écris aucune commande dont le texte contient le nom d'une commande d'arrêt par motif, même dans une recherche : la garde du dépôt la refuse. Aucune commande `rm` sur un chemin construit par variable.
- **Refus d'outil :** au premier refus, arrête-toi et dis-le, sans le contourner.
- **Écriture :** écris sur disque tôt et souvent.

## Sorties
- Le code et ses essais, dans ton arbre.
- `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/rapport-developpeur-code-formation-v1.md`, scellé (`PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B -m controle_ia.scellement sceller <fichier>`), avec :
  - les modules et leurs fonctions publiques ;
  - la table « garde → essai sain → essai artefact » ;
  - les réemplois, et les fonctions neuves écrites à la place d'une fonction existante ;
  - les choix que le texte ne fixe pas ;
  - ce qui reste à faire, et la commande qui lance tes essais ;
  - les empreintes des fichiers de code, calculées à la fin.

## Rends
1. La phrase exacte de ton invite système qui nomme le modèle qui te sert.
2. Le chemin de ton arbre de travail, et la liste de tes fichiers.
3. Dix lignes au plus :
   - ce qui est écrit et essayé (nombre d'essais, passés ou non) ;
   - ce qui reste ;
   - les choix que le texte ne fixe pas ;
   - ce qui menace la date du 22 novembre.
4. La liste des fichiers et des dossiers que tu as ouverts, une ligne chacun.
