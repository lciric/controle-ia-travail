# Vérification des corrections — outils de l'épreuve v5

- **Commit** : 8f850c4d, dossier `docs/notes/memoire-conception-v1/epreuve-outils-v1/`.
- **Pièces vérifiées**, toutes trois conformes à leurs compagnons :
  - `recherche_autorisee_v2.py` (8144f9b2…) ;
  - `verifier_citations_v5.py` (d66dfe53…) ;
  - `test_outils_epreuve_v5.py` (850bd60f…).
- **Contexte relu** : `liste-autorisation-bibliothecaire-v3.md` (6a9a41e3…), par son écart avec la v2.
- **Méthode** : écarts avec la v1 de l'outil et la v4 du vérificateur lus en entier. Aucun fichier des dossiers « ne-pas-lire » n'a été ouvert.

## Verdicts

- **recherche_autorisee_v2.py : conforme.**
- **verifier_citations_v5.py : non conforme.** Une correction de quelques lignes : la règle du point 19 laisse ignorer, une fois déclarés, 170 dossiers exclus.

## Points de la v4, un par un

1. **Segment « ne-pas-lire » — corrigé.** L'outil liste 0 chemin des deux dossiers, pour le bras « memo » comme pour le bras « base ». `lire` d'un chemin de l'essai 1 rend « REFUS ». La liste v3 écrit la même règle.
2. **Dossier exclu déclaré — corrigé en partie.**
   - Désormais un manquement : la banque, le dossier de l'essai 1, `diag/`.
   - Toujours ignorés : `docs/notes/protocole-x-programmation-de-poids-v1`, `docs/notes/lentilles-sondes-p3-v1`, `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-33-argon`. La porte 1 tient (mutations).
   - **Cause** (lignes 252 à 257) : un dossier n'est compté que si son nom contient l'un des neuf mots d'une liste écrite à la main. Les exclusions par motif (résultats, programmation de poids, demande 24, sous-dossiers hors de la sous-liste des demandes) n'y sont pas.
   - **Mesure sur l'arbre** : 170 dossiers sont exclus par une règle, autre que « hors de la liste », et seraient pourtant ignorés une fois déclarés. Exemples : `P3-mesures-*`, `audit-symetrie-*`, `barreau5-*`.
   - **Correction** : ignorer un dossier seulement si `chemin_autorise_bras` le refuse pour le seul motif « hors de la liste d'autorisation ». Ce sont les dossiers parents, comme `docs/notes`. Tout autre motif de refus est un manquement.
3. **Journal contrôlé — corrigé.** Une ligne dont l'action est `empreinte`, dont le commit est celui d'un autre essai, ou dont le bras est l'autre bras, fait tomber la porte 1 (code 4). Une ligne bien formée mais écrite à la main reste acceptée : c'est la limite déclarée, acceptable si la procédure interdit au répondant tout accès en écriture.
4. **Champ `agent` — corrigé.** Absent ou vide, c'est un manquement.
5. **Outil.** Chaque ligne du journal porte `commit` et `bras`. Les 18 essais du dépôt passent.

## Absence de régression

- Les règles de la v3 sont rejouées sur l'arbre du commit :
  - aucun fichier hors de la sous-liste des demandes n'est accepté ;
  - aucun fichier autorisé n'est refusé par un nom de dossier ;
  - les accents sont gérés ;
  - la banque est refusée, même par `../`.
- Le bras « base » n'accède toujours à rien du mémo.
- Une citation absente du journal reste un manquement.

## Faible

- Lignes 217 à 222 : quand le journal est altéré ou absent, le vérificateur rend le code 4 sans écrire de rapport. L'examinateur n'a alors que le message d'erreur. Correction : écrire tout de même le rapport, avec `porte_1_fichiers_ouverts: false` et le motif.

## Fichiers

- Arbre du commit : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/arbre5.txt`
- Script de rejeu des règles : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/citations_regles_v5.py`
- Journal de l'outil : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/j5.jsonl`
