# Vérification de collisionneur_v9_v8i.py (7c7aa713…) — rendu v1

Verdict : **à corriger**, sur deux points à une ligne chacun. Les huit contournements de la v8h et les préfixes sont tous refusés. Les sceaux tiennent, 388 essais passent, et l'essai à blanc en lecture seule sur la conception F redonne `['scripts/pipelines']`.

## Bloquants
1. **Chemin réel imbriqué** (`chemin_hors_depot`, seul le deuxième composant est comparé). Ces trois jetons sont acceptés :
   - `scripts/pipelines/docs/sources/y` ;
   - `scripts/x/docs/brief-claude-code-programme-complet-v2.md` ;
   - `docs/zz/runs/collisionneur-protocole-x-tirage-au-hasard-v1-20261122-080414`.

   Le motif de base ne voit pas l'occurrence intérieure, parce que son garde arrière exclut « / ». Correction : refuser tout composant au-delà du premier dont la forme normalisée est `docs`, `runs` ou `scripts` ; ou appliquer la comparaison à chaque suffixe qui commence par l'un d'eux.
2. **Homoglyphes et pleine chasse** (`COMPOSANT_ADMIS`). Ces deux jetons sont acceptés alors qu'ils affichent le nom réel :
   - `scripts/dеpot_expurge.py`, avec un е cyrillique ;
   - `scripts/ｄｅｐｏｔ_expurge.py`, en pleine chasse.

   Correction : restreindre les composants à l'ASCII, `[A-Za-z0-9]+(?:[-_.][A-Za-z0-9]+)*`.

Ajouter ces cinq cas aux essais.

## Mutations
- Tués (13) :
  - liste blanche retirée ;
  - catégorie libre ;
  - empreinte non vérifiée au retrait du bloc ;
  - contrôle avancé (B2) retiré ;
  - recollement des voisins ;
  - revalidation de `verifier` retirée ;
  - ponctuation finale gardée ;
  - garde de la racine retirée ;
  - contrôle du caractère suivant retiré ;
  - forme des composants libre ;
  - préfixes retirés ;
  - normalisation retirée ;
  - erreur du système de fichiers acceptée.
- Survivent, tous équivalents :
  - contrôle des formes retiré : la liste blanche le couvre ;
  - « . » et « .. » admis : la forme des composants les exclut déjà ;
  - comparaison sans extension retirée : la règle des préfixes la couvre.
