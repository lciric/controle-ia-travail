# Note de revérification — ordre de l'étalonnage, brouillon 7 — cl1

Date : 2026-11-21. Même vérificateur (Claude Opus 5.5), même mandat. Pièce : `ordre-etalonnage-ii-b-v5-brouillon7.md` (`b61bc15f…`, compagnon vérifié).

**Verdict : conforme pour l'étalonnage, avec une correction de forme (F3).** S'y ajoute une réserve pour l'ordre de la course (C1).

- **Rejeu** : le programme du brouillon 7, joué sur une copie du brouillon 6 (`ordre-rejeu-b7/`), rend `b61bc15f…`, **identique à l'octet**. Les six blocs de différence sont exactement les six remplacements annoncés :
  - la table des pièces, avec `prefixe_graines` ;
  - deux phrases sur le commit de lancement ;
  - GO-2026-11-21-84 sur la ligne « Exécutante » ;
  - la première action, `gardee`, confirmée ;
  - la ligne du champ de la première action.
- **Empreintes des pièces** : toutes justes.
  - Sur `origin/claude/iib-reconception-oracle-v1`, fichier et compagnon : texte scellé, deux consignes du maître v3, consigne du flagrant v2, errata 1 et 2, devis et son erratum 1.
  - Dans `origin/prep/iib-code-v5`, fichier et compagnon : `taches-entrainement.json` (`8d20a698…`) et `taches-evaluation.json` (`76cdeace…`). Ce sont les pièces de la configuration de la première course, mêmes chemins et mêmes empreintes.
- **GO-2026-11-21-84** est sur `main` (`git fetch origin main`, puis `git show`). Elle porte « étalonnage accordé, première action dans la perte de distillation « gardée » ». La tête `bef65df0…` est un ancêtre de `origin/main`.
- **Chemins acceptés par le code** :
  - `configuration_v5` exige seulement chemin et empreinte, avec l'égalité au chemin scellé pour la conception ;
  - `MondeReel` vérifie chaque pièce sous la racine du dépôt au commit de lancement ;
  - `controles-explo` (`lancer_iib_v3.sh`) exige au commit de lancement `$S`, pour les sept pièces, le fichier, son compagnon et l'empreinte égale à celle de la configuration ; il lit aussi `registres/go.md` à ce commit et y exige la ligne `GO-2026-11-21-70`.
  
  Des pièces hors de l'arbre du code revu, présentes au commit de lancement, sont donc ce qu'il faut.
- **`prefixe_graines = ""` pour l'étalonnage : juste.** Le code attend une chaîne, que le gabarit laisse vide. La section 14 donne pour l'étalonnage les clés de la conception d'origine et les clés neuves, sans préfixe ; seule la course « dérive ses clés de la même entropie sous un préfixe propre ».
- **F3 (forme)** : la ligne du § 11 garde `<<MOT_LAZAR_PREMIERE_ACTION_DANS_LA_PERTE>>`, barré mais toujours entre chevrons. Or le § 11 (« tant qu'un seul reste dans le texte… ») et le § 6 (« un champ du § 11 encore entre chevrons ») font de tout chevron restant un arrêt, et une recherche par programme le trouverait. *Correction* : écrire le nom du champ sans chevrons.
- **C1 (pour l'ordre de la course, sans effet ici)** : `designation_v5.configuration_de_course` copie la configuration de l'étalonnage et n'y écrit que l'oracle de la règle. La course garderait donc `prefixe_graines = ""`, et la phrase « la course aura son préfixe propre, fixé par son ordre » n'est pas réalisable avec le code actuel. Les clés de la course ne heurtent pas celles de l'étalonnage : les phases et les noms diffèrent (`iib/maitre/…`, `iib/temoin/…`, `iib/evaluation/…`). Mais la section 14 demande un préfixe propre. Il faudra soit un code de course qui pose ce préfixe, soit un écart déclaré dans l'ordre de la course.
