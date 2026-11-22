# Vérification des corrections — verifier_citations_v6.py

- **Pièces vérifiées.** Au commit 3888355b : `docs/notes/memoire-conception-v1/epreuve-outils-v1/verifier_citations_v6.py` (926ec631…) et `test_outils_epreuve_v6.py` (f5e404b3…). Les deux empreintes sont conformes à leurs compagnons.
- **Outil de recherche.** `recherche_autorisee_v2.py` est inchangé (8144f9b2…).
- **Méthode.** Le même contre-lecteur, en lecture seule. J'ai lu en entier l'écart entre la v5 et la v6.
- **Cloisonnement.** Aucun fichier des dossiers « ne-pas-lire » n'a été ouvert.

## Verdict

**Conforme.** Les points 22 et 23 corrigent le défaut moyen et le défaut faible de la v5. Je ne trouve pas de régression.

## Vérifications

1. **Les 170 dossiers exclus de la v5 sont tous comptés comme manquement en v6 ; aucun n'est encore ignoré.**
   - Sur l'arbre entier du commit, 397 dossiers sont comptés comme manquement pour le bras « memo », 408 pour le bras « base ».
   - **Dossiers déclarés, un par un :**

     | Dossier déclaré | Résultat |
     |---|---|
     | banque | manquement |
     | essai 1 | manquement |
     | `diag/` | manquement |
     | `protocole-x-programmation-de-poids-v1` | manquement |
     | `lentilles-sondes-p3-v1` | manquement |
     | `reponse-33-argon` | manquement |
     | dossier du mémo, pour le bras « base » | manquement |
     | `docs/notes` | ignoré |
     | `docs/decisions` | ignoré |
     | dossier des demandes lui-même | ignoré |

2. **Aucun effet sur les fichiers.**
   - Les deux changements de `chemin_autorise` (le chemin d'un dossier comparé aux préfixes et aux motifs) ne changent le jugement d'aucun fichier de l'arbre, ni pour le bras « memo », ni pour le bras « base », entre la v5 et la v6.
   - L'outil v2, qui charge les règles de la v5, reste donc juste pour les fichiers.
3. **Journal altéré ou absent : un rapport est écrit**, avec la porte 1 tombée, le motif, et le code 4. C'est vrai pour une action forgée, un commit d'un autre essai, l'autre bras, et un journal absent.
4. **Mutations précédentes.**
   - Cas sain : accepté.
   - Chemin cité absent du journal : manquement.
   - Champ `agent` absent : manquement.
   - Les 20 essais du dépôt passent.

## Remarque, sans défaut

- Six dossiers « hors de la liste » ne sont exclus par aucune règle, mais tout leur contenu est exclu par une règle de nom. Exemple : `docs/anteriorite`, `rapports/fille-cles-1-v1`.
- Déclarés, ils sont ignorés. C'est conforme au point 22 : la porte 1 se juge sur le journal, et l'outil n'en montre aucun fichier.

## Fichiers

- Arbre du commit : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/arbre6.txt`
- Liste des dossiers : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/dossiers6.txt`
