# Rapport de la contre-lecture 1 du lecteur du texte et de l'amorce v3 (classe B)

Pièce versée à l'identique du rapport rendu par le contre-lecteur (sous-agent neuf, Sonnet 5.5, effort élevé), sur le commit adb6c6b2.

---

## Contre-lecture (classe B, code) : lecteur du texte de la dose-réponse et amorce v3

**Verdict : prêt sous corrections listées.**
- Lecteur du texte (pièce 1) : deux défauts majeurs, CL-01 et CL-02, à corriger avant d'inscrire `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE`. Le reste est mineur.
- Amorce v3 (pièce 2) : prête, aucun défaut.

Le calcul de T0.6 est repris sans changement. Le texte de désignation (empreinte 19dbc99e, lu en entier) est suivi, avec l'option A.

### Ce que j'ai rejoué
- Les deux fichiers d'essais : 88 passés en 168 s (75 pour le lecteur, 13 pour l'amorce). L'arbre du dépôt est resté propre.
- Comparaison syntaxique (AST) de `lecteur_texte_dose_reponse_v1.py` avec `mots_et_cout_t06_v3.py`, docstrings retirées :
  - Identiques : `ajuster`, `noter`, `matrice_b`, `mots_de`, `vocabulaire`, `cout_present`, `traits_base_a`, `centres_de_tache`, `etat_dose`, `former_pp`, `lire_scores`, `lire_jeu`, `apprendre_modele`, `noter_indices`, `taux_un_pourcent`, `exiger_colonnes_entree`, `exiger_traits`.
  - Différents, chacun vérifié ligne à ligne :
    - `Contexte` et `comptes_rapportes` ne changent que le nom de la liste de conditions.
    - `exiger_arbre` ne change que ses messages.
    - `controler_code` et `lire_fichier_code` sont paramétrés.
    - `audit_r4`, `calculer`, `valider_issue`, `cles_graines` et `executer` sont réécrits pour la course, comme le texte l'exige.
  - Constantes de calcul (traits, réglages, seuils, solveur, modules gelés) : égales à celles de T0.6.
  - Seule constante de T0.6 non reprise : `PART_SANS_CENTRE_MAX` (réserve R-BA5, propre à T0.8), ce qui concorde avec les écarts déclarés.
- Phrases gelées comparées par programme au texte scellé (copie de `origin/main`, empreinte vérifiée) : les phrases de K0, K1, KA-2, KA-3 et KA-4, les suites, les réserves R-K2 à R-K6 et la lecture prudente y figurent toutes à la lettre. Les seules citations de la section absentes du code sont celles de l'option B.
- Format des mesures : concordance exacte, par code, avec `course_v2.ligne_de_mesure` (21 clés), `ecrire_bloc`, `lecture_v2` (lignes C, DR-6, DR-7, DR-8) et le manifeste de `creer_manifeste` (`config.mode`, `config.prereg.sha256`, `config.designation_critere_3`, `preenregistrement.sha256`).
- Amorce v3 : `diff` avec la v2 (amorce et lanceur) ne montre que les changements annoncés ; liste d'essais (58) ; empreintes `.sha256` des dix fichiers examinés conformes.
- Mes expériences (bloc-notes, données factices) :
  - Un coût `Infinity` dans les mesures : refusé (CL-01).
  - Un lancement de forme réelle joué en mode jouet : accepté (CL-02).
  - Garde des plis, plis mêlés, `valider_doses` : voir CL-04 et CL-05.
  - Les six déclencheurs de l'audit de symétrie, sur des entrées fabriquées : logique correcte, avec les bornes du texte.
- Mutations sur une copie du dépôt, avec les 75 essais du lecteur : tous passent encore quand j'applique ensemble ces quatre mutants :
  - audit neutralisé (déclencheurs 1 et 2 forcés à faux, seuils 4 à 6 inatteignables) ;
  - suppression de la branche « fichier réel existant » de la seconde exécution ;
  - `valider_doses` rendu vide ;
  - garde des plis désactivée.

### Constats

**CL-01 (majeur) : le lecteur refuse un coût non fini que la course peut légitimement écrire.**
- Fichier : `scripts/lecteur_texte_dose_reponse_v1.py`, l. 939 (`lire_mesures`).
- Texte violé : Liste d'arrêt, « non-convergence d'une base : "non calculable", écrit tel quel, jamais "échoue" ». Plus largement, la pièce reprend celle de T0.6, qui traite un coût illisible comme tel.
- Scénario : `t06/cout.lire_cout` lit le premier nombre du champ COST par `float(...)`. Un champ de plus de 308 chiffres donne `inf`, que `json.dumps` écrit `Infinity` dans `mesures.jsonl`. `lecture_v2` traite ce cas (`cout_lisible` renvoie faux), mais `lire_mesures` lève `ArretPiece` sur la valeur et refuse tout le lancement avant le manifeste. Le coût est rare, mais il suffit d'une action sur 19 200 pour bloquer la pièce. Un correctif de code après l'inscription de la ligne `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE` est lui-même bloqué par la garde de date du registre.
- Correction : accepter un `cout` flottant non fini (`inf`, `nan`) et le stocker comme `nan` (illisible, comme `None`). Garder le refus pour tout autre type. Ajouter un essai (cas sain avec `Infinity`, artefact avec une chaîne).

**CL-02 (majeur) : le mode jouet lit un lancement réel sans registre ni garde.**
- Fichier : `scripts/lecteur_texte_dose_reponse_v1.py`, l. 783-795 (`lire_lancement`) et l. 1788.
- Texte violé : R1 (« aucune lecture de résultat avant scellement ») ; Liste d'arrêt, « un score ... ouvert avant la ligne `DOSES-JUGEES-CRITERE-3` ».
- Scénario : mes essais ont joué `--mode jouet` sur un lancement dont le manifeste est décisif et en mode réel. La pièce l'accepte et écrit issue, audit et doses jugées, sans registre ni contrôle du code. Son effet de bord sur la seconde exécution la rend ensuite refusable si le dépôt est le même, mais un clone jetable ne garde aucune trace. La pièce de T0.6 a le même trou.
- Correction : en mode jouet, refuser un manifeste du lancement avec `decisif` vrai ou `config.mode == "reel"`. Ajouter un essai avec cas sain et artefact.

**CL-03 (mineur) : `--registre` est accepté en mode réel.**
- Fichier : `scripts/lecteur_texte_dose_reponse_v1.py`, l. 1788 (la liste des options d'essai refusées en mode réel) et `main`.
- Texte violé : R5, aucun repli silencieux.
- Scénario : un registre commité à un autre chemin remplace `registres/scellements-v1.md`. La garde de date et des empreintes porte alors sur un registre choisi par l'opérateur.
- Correction : refuser `registre` en mode réel, ou l'imposer égal à `REGISTRE_DEFAUT`.

**CL-04 (mineur) : gardes sans cas sain et artefact (R5).** Les mutations ci-dessus n'en font échouer aucun essai.
- Les déclencheurs (1), (2), (4), (5) et (6) de l'audit (seul le (3) est éprouvé).
- La garde des plis : `plis_imposes` n'est jamais utilisé par les essais.
- `noter_indices` (plis mêlés) et `exiger_centres`.
- `valider_doses`.
- La branche « tout fichier réel » de `exiger_premiere_execution`.
- La branche « tirages dégénérés » de `rappel_episode`.
- Correction : ajouter un essai par garde, cas sain et artefact. Mes scripts de bloc-notes (`exp2.py` et `exp3.py`) donnent des cas utilisables.

**CL-05 (mineur) : `valider_doses` (l. 1693) est trop lâche.**
- Il accepte une `phrase`, une `suite`, un `temoin_positif`, des `qualificatifs` ou une réserve R-K2 falsifiés (essayés un par un).
- Correction : reconstruire le document attendu depuis `ligne_k`, les phrases et les états, et comparer champ à champ.

**CL-06 (mineur) : référence temporelle et contenu de `lignes_registre`.**
- Fichier : `controler_registre_reel`, l. ~640.
- Texte : Plan, point 1, « trois lignes au registre, sinon aucune création ».
- La pièce borne les lignes à la création du manifeste du lancement, qui suit la création de l'instance (installation, essais, descente du modèle). Une ligne inscrite dans cet intervalle passerait la garde de la pièce mais violerait le texte.
- Correction, côté ordre de lancement : `designation_critere_3.lignes_registre` doit nommer les quatre lignes (`DESIGNATION-CRITERE-3`, `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE`, `SONDES-LUES-CRITERE-3`, `CODE-MOTS-ET-COUT-T06`). Seule la garde de `controles_v2` au moment de la création de l'instance fait respecter le texte. Pas de changement de code demandé.

**CL-07 (mineur) : clone superficiel, message de refus.**
- Le refus du clone superficiel est juste. Mais le message « commit cité absent du dépôt » ne distingue pas ce cas d'une falsification.
- Correction : ajouter « clone superficiel : `git fetch --unshallow` » quand `rev-parse --is-shallow-repository` vaut `true`.

**Remarques sans correction demandée**
- La pièce lit le résultat de la lecture du coût sans vérifier qu'il est décisif. Son manifeste n'est pas dans la liste blanche du texte. La garde reste le lien `entrees_sha256` et l'étape R13.
- `scripts/lecteur_texte_dose_reponse_v1.py` écrit le fichier des détails avant le fichier d'issue (b). C'est inoffensif.
- Amorce v3 : `extraction_v1` s'exécute avant la garde `git diff` du code. Cet ordre était déjà celui de la v2 (python en ligne).

### Avis sur les trois nœuds de l'auteur
1. **Lecture de K0 : acceptée.**
   - Le résultat absent donne un refus (code 2, rien d'écrit). C'est cohérent avec « attente » : le texte ne demande pas de fichier K0 dans ce cas.
   - C1 et C2 : aucun fichier de mesures ni de textes n'est ouvert. Seuls les `bloc.json` sont lus, pour lier la lecture du coût aux blocs ; c'est nécessaire et acceptable.
   - Sous K1, les étapes (b) et (c) tournent en descriptif. Le texte ne dit pas « rien n'est lu » pour K1, seulement « aucun score de sonde ouvert ». Choix défendable ; je ne demande pas de changement.
2. **Clone superficiel : accepté.** Ne pas affaiblir la garde. L'ordre doit exiger `git fetch --unshallow` avant `verifier-code` et avant l'exécution (voir CL-07).
3. **Format des mesures : accepté.** L'égalité stricte des 21 clés est conforme à R11, et l'essai de concordance l'établit contre le code. Une réserve : CL-01.

### Amorce v3 (pièce 2)
- `extraction_v1` ajoute `designation_critere_3.chemin` quand la clé n'est pas `null`. La clé absente, un chemin absolu, un `..`, un motif ou un saut de ligne sont refusés. Le cas sain et sept artefacts sont éprouvés. La v2 laisse bien le texte hors de l'arbre, ce qu'un essai montre.
- Je n'ai trouvé aucun autre changement, ni dans l'amorce ni dans le lanceur.
- Liste d'essais : empreinte, 58 collectés (45 + 13) et expression `ATTENDUS="58"` cohérentes.
- Les modes git du lanceur sont corrects.

### Déclaration de cloisonnement
- Je n'ai ouvert aucune donnée d'organisme : rien sous `diag/`, `runs/` ni `donnees/` du dépôt, aucun score, verdict ni sortie de course, aucun coffre.
- Je n'ai pas ouvert `brouillons/g0-criteres-2-3-v1/consignes-privees-dose-reponse-consigne-cachee-v4.json` ni `prereg/P3-consignes-v1.md`.
- Je n'ai pas ouvert `registres/etat.md` ni aucune passation. Une liste de noms de fichiers d'un `git grep` en a mentionné une, sans ouverture.
- J'ai lu `registres/scellements-v1.md` (lignes de clés) et `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`.
- Toutes mes exécutions ont utilisé des données factices, dans mon bloc-notes sous `/tmp/claude-0/-home-user-controle-ia-travail/284bccf9-0383-5ff3-a54b-5c2ab1c46a42/scratchpad/` (`exp1.py` à `exp4.py`, copie `mut/`).
- Je n'ai modifié, committé ni poussé aucun fichier du dépôt. Je n'ai créé aucune instance ni lancé aucune génération de modèle.