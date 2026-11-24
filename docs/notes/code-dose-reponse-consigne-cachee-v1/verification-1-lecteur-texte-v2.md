# Rapport de la vérification 1 des corrections du lecteur du texte (v2)

Pièce versée à l'identique du rapport rendu par le même contre-lecteur (Sonnet 5.5), sur le commit 6b2b821a.

---

## Vérification des corrections du lecteur du texte (commit 6b2b821a, v2)

**Verdict : prêt.** CL-01 à CL-07 sont traités. Je n'ai trouvé aucun défaut bloquant ni majeur dans la v2. Deux remarques mineures, sans correction exigée, sont plus bas (VN-01 et VN-02).

### 1. État de chaque constat

| Constat | État | Preuve |
|---|---|---|
| CL-01 | **corrigé** | `_flottant_non_fini` (l. ~784) et `lire_mesures` (l. 967-974). Un `cout` flottant non fini (`Infinity`, `-Infinity`, `NaN`) est stocké `nan`, donc illisible pour `cout_lisible`. Chaîne, booléen, liste ou objet restent refusés. Essais `test_cl01_*` : le brut contient bien `Infinity`, `-Infinity` et `NaN`, et le cas sain comme les quatre artefacts passent. |
| CL-02 | **corrigé** | `lire_lancement` (l. 819) : l'`elif man.get("decisif") or cfg.get("mode") == "reel"` ne s'applique qu'au mode jouet. `test_cl02_*` éprouve les deux signes séparément et par `executer_jouet`. Rien n'est écrit. |
| CL-03 | **corrigé** | `executer` (l. 1856) refuse, en mode réel, un `--registre` différent de `registres/scellements-v1.md` (comparaison après résolution des chemins). Cas sain : le registre par défaut passe cette garde. |
| CL-04 | **corrigé** | Essais ajoutés pour les déclencheurs de l'audit 1, 2, 4, 5 et 6, avec les bornes, l'échantillon par graine, la garde des plis, les plis mêlés, les centres, la branche « fichier réel » et les tirages dégénérés. Voir §3 pour mes mutants. |
| CL-05 | **corrigé** | `attendu_doses` reconstruit le document ; `valider_doses` le compare champ à champ, plus les prédictions K-P1, K-P2 et K-P4. Falsifications refusées une à une par les essais (phrase, suite, état du témoin positif, qualificatifs, réserves, doses jugées, option, motif, etc.). Deux clés de plus au fichier (d) (`etats_temoins`, `audit_motifs`) : changement de format déclaré, avec `CLES_DOSES` mise à jour. |
| CL-06 | **sans objet côté code** | Aucun changement de code. L'ordre v5 doit nommer les quatre lignes dans `lignes_registre`. |
| CL-07 | **corrigé** | `controler_code` (l. 603-605) ajoute « clone superficiel : `git fetch --unshallow` » quand le dépôt est superficiel. Essai présent. |

Autres vérifications :
- Aucun écart hors des constats : le diff v1 → v2 ne contient que ces corrections et les renommages. Le lanceur v2 ne diffère du v1 que par le module joué.
- Le calcul de T0.6, la garde d'identité et le fabricant factice v1 restent inchangés.
- `FICHIERS_PIECE` pointe sur la v2.
- Les `.sha256` des trois fichiers neufs sont conformes. La v1 est intacte (`git diff` vide sur ses fichiers).

### 2. Constats neufs introduits par la v2
Aucun bloquant ni majeur. Deux remarques mineures :
- **VN-01 (mineur)** : `scripts/lecteur_texte_dose_reponse_v2.py`, l. ~1943, appel de `valider_doses(d, sources)` dans `executer`. Les sources viennent des mêmes objets en mémoire que ceux qui ont servi à construire `d` (états, établies, qualificatifs, motifs), et non des fichiers (b) et (c) relus après leur écriture. Cette vérification protège donc contre une erreur de câblage, pas contre un fichier (b) écrit différemment. `valider_doses(d)` seul (sans sources) reconstruit à partir du document lui-même : il ne détecte pas une falsification cohérente de `etats_lecteur`. Aucune correction exigée : le vérificateur neuf (R13) doit comparer le fichier (d) aux fichiers (b) et (c) écrits.
- **VN-02 (mineur)** : la clé `predictions` n'est contrôlée que sur K-P1, K-P2 et K-P4 (K-P3, les aires, ne l'est pas). Les prédictions sont descriptives et aucune dose jugée n'en dépend.

### 3. Mes quatre mutants appliqués à la v2
Avec les quatre mutants ensemble (audit neutralisé, branche « fichier réel » de la seconde exécution supprimée, `valider_doses` rendu vide, garde des plis désactivée), 35 essais échouent : 35 échecs, 93 passés. La suite saine passe : 128 passés en 306 s.

Chaque mutant seul fait échouer au moins un essai (`-k cl0`, hors e2e) :

| Mutant | Résultat |
|---|---|
| audit, seuils des déclencheurs 4, 5 et 6 | 5 échecs |
| audit, déclencheurs 1 et 2 | 3 échecs |
| branche « fichier réel » de la seconde exécution | 1 échec |
| `valider_doses` rendu vide | 25 échecs |
| garde des plis désactivée | 1 échec |

J'ai ajouté trois mutants de retour en arrière sur CL-01, CL-02 et CL-03 : chacun fait aussi échouer 1 essai.

### 4. Verdict
**Prêt.**

### 5. Cloisonnement
- Je n'ai ouvert aucune donnée d'organisme : rien sous `diag/`, `runs/` ni `donnees/` du dépôt, aucun score, verdict ni sortie de course.
- Je n'ai pas ouvert les consignes privées ni `prereg/P3-consignes-v1.md`, ni `registres/etat.md`, ni les passations.
- J'ai extrait les fichiers v2 du commit par `git show`, vers mon bloc-notes (`.../scratchpad/v2`, `r_*`). Toutes mes exécutions ont utilisé des données factices, sur des copies hors du dépôt.
- Je n'ai modifié, committé ni poussé aucun fichier du dépôt (état propre vérifié), créé aucune instance ni lancé aucune génération de modèle.