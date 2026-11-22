# Vérification de collisionneur_v9_v8g.py (93f96e95…) — rendu v1

Verdict : **à corriger**. Le différentiel est conforme à l'annoncé, mais l'acceptation laisse partir un chemin réel du dépôt. Je l'ai démontré de bout en bout : `scripts/depot_expurge.py.` se trouve dans l'invite III.2 envoyée, et le code de sortie est FINI.

Le point (1) tient : le différentiel v8d→v8g contient l'en-tête, VERSION, le bloc neuf, `garder_motifs`, la ligne d'`etat.md`, `verifier`, le devis, l'option et `principal`. Rien d'autre. Les sceaux tiennent, et 359 essais passent.

## Bloquants
1. **Lignes 622-625 (`formes_acceptables`)** : le contrôle `exists()` porte sur le jeton brut. Les jetons suivants sont donc acceptés :
   - un chemin réel suivi d'un point final, d'un tiret ou d'une suite (`scripts/depot_expurge.py.`, `…py-`, `…py/x`) ;
   - une remontée (`docs/x/../../registres.`, `scripts/../tests/test_depot_expurge_v8.py.`) ;
   - une forme absolue déguisée que le motif de base ne voit pas, parce que `/home/` est précédé d'un point (`docs/../../../home/user/secret`, `runs/../../../../etc/passwd.`) ;
   - un dossier réel en préfixe (`docs/sources/inexistant.pdf`) ;
   - une variante de casse (`scripts/DEPOT_EXPURGE.PY`).

   Correction : refuser tout composant `..`, `.` ou vide. Retirer la ponctuation finale (`.` et `-`) de chaque composant. Refuser si un préfixe au-delà de la racine (`docs/`, `runs/` ou `scripts/`), dont le jeton entier, existe dans le dépôt, en comparant sans tenir compte de la casse (lister le dossier). Convertir `OSError` en refus : un nom trop long lève aujourd'hui une `OSError` hors `Arret`, après les écritures.
2. **Ligne 2912, à comparer aux lignes 2903-2911** : le contrôle du contenu s'exécute après `sceller_composition`, `declarer_script`, l'ouverture des lignes, les rejugements et `consigner_absences`. Un refus laisse donc des écritures : démontré, un `absence_acceptee` neuf au journal avec un refus au code 7. Correction : séparer `controler_acceptations(dossier, specs)`, qui lit seulement et renvoie les acceptations neuves, l'appeler avant `sceller_composition` (les cellules se lisent déjà), puis journaliser à la place actuelle.
3. **Essais** : les mutants M2 (contrôle `exists` retiré) et M4 (retrait du bloc sans vérifier l'empreinte) survivent. Le cas `docs/programme-controle-ia-v2.md` n'exerce pas le contrôle d'existence : il est refusé par le motif `controle-ia`. Il faut ajouter :
   - un chemin réel sans autre motif, avec et sans point final ;
   - une remontée ;
   - un préfixe réel ;
   - une cellule réécrite et rescellée sur le disque après l'acceptation, dont la garde doit refuser le bloc (mon essai `test_att_cellule_reecrite_scellee` tue M4) ;
   - un refus de contenu qui ne laisse aucun octet neuf au journal (essai entier, et pas seulement le décompte de `motif_accepte`).

## Non-bloquants
- **Ligne 672** : `replace(bloc, "")` recolle les voisins. `"x" + bloc + "docs/notes/x"` masque le motif (démontré). Peu probable (bloc recopié et collé à une lettre), mais remplacer par `"\n"` ne coûte rien. Retirer toutes les copies est sans danger : chacune a le texte contrôlé.
- **`RACINE_DEPOT = parents[3]`** : si le script est lancé depuis une copie placée ailleurs, `exists()` interroge un mauvais arbre et tout passe. Garde proposée : refuser l'acceptation si `RACINE_DEPOT/"CLAUDE.md"` est absent.
- **`verifier`** ne revalide pas les acceptations journalisées et ne signale pas une acceptation devenue caduque (empreinte changée). Proposé : rejouer `formes_acceptables` sur la cellule et comparer les empreintes.
- **Rapport du développeur** : `docs/programme-controle-ia-v2.md` y est cité comme refusé au titre de « chemin réel », alors qu'il l'est par le motif `controle-ia`. Une phrase à corriger.
- Points (3) et (4), le reste : sur un refus, l'acceptation n'est pas journalisée ; `etat.md` et le devis suivent la règle de la garde. L'essai à blanc en lecture seule sur le dossier du tirage au hasard redonne le seul `scripts/pipelines` (conception F), conforme au rapport.

## Mutations (essais v8g, copies dans `mut/`, racine fixée au dépôt)
| Mutant | Résultat |
|---|---|
| M1 contrôle des formes retiré | tué |
| M2 contrôle `exists` retiré | **survit** |
| M3 catégorie libre | tué |
| M4 empreinte non vérifiée au retrait du bloc | **survit** (tué par mon essai) |
| M5 journalisation avant contrôle | tué |
| M6 catégorie ignorée au retrait | tué |
| M7 contrôle du contenu absent | tué |
