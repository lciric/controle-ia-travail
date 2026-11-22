# Vérification des corrections : collisionneur_v9_v8h.py (d9b41b11…) — rendu v1

Verdict : **à corriger**, un seul point, minime. Les corrections B2, la séparation des voisins et la revalidation par `verifier` tiennent, et B1 tient sur les douze formes que j'avais données. Mais `chemin_hors_depot` laisse encore passer un nom réel quand la ponctuation est interne au deuxième composant, ou quand MOTIF_JETON_CHEMIN coupe le jeton.

Les sceaux tiennent, 376 essais passent, et l'essai à blanc en lecture seule sur la conception F redonne `['scripts/pipelines']`.

## Bloquant
1. **Lignes 649-663, `chemin_hors_depot`** : les cas suivants sont acceptés, alors que le texte envoyé contient un nom réel.
   - Ponctuation interne au deuxième composant, ou extension altérée : `scripts/depot_expurge.py./x`, `docs/sources./x`, `docs/sources-/x`, `scripts/depot_expurge..py`. La ponctuation finale n'est retirée que du jeton entier, et `Path("x.py.").stem` vaut `"x.py."`.
   - Jeton coupé par MOTIF_JETON_CHEMIN : `scripts/depot​_expurge.py`, `scripts/depot­_expurge.py`, `scripts/depot+expurge.py`, `scripts/depot%5Fexpurge.py`. Le jeton contrôlé est alors `scripts/depot`, mais le texte envoyé reconstruit visiblement le nom réel.

   Corrections proposées :
   - (a) comparer le nom et chaque entrée du dossier après casefold et retrait de tout caractère non alphanumérique, sur le nom comme sur sa racine sans extension ;
   - (b) exiger que le caractère qui suit le jeton soit la fin du texte, un blanc ou l'un de `, ; : ! ? ) ] } » " ' ’` ; sinon refus.

   Ajouter ces huit cas aux essais.

## Non-bloquants
- Un préfixe d'une entrée réelle passe (`runs/collisionneur-protocole`, préfixe d'un dossier de course). Option : refuser si le nom normalisé est un préfixe d'une entrée normalisée, à partir de 8 caractères.
- Le mutant où l'erreur du système de fichiers est acceptée (`except OSError: return True`) survit : aucun essai ne la provoque. Ajouter un `iterdir` doublé qui lève `OSError`.
- Le mutant où le contrôle des formes est retiré survit, mais il est équivalent : la liste blanche refuse déjà toute forme autre que `docs/`, `runs/` ou `scripts/`. On peut le garder comme défense en profondeur.

## Mutations (essais v8g et v8h, copies dans `h/`)
- Tués :
  - liste blanche retirée ;
  - catégorie libre ;
  - empreinte non vérifiée au retrait ;
  - contrôle avancé (B2) retiré ;
  - recollement ;
  - revalidation de `verifier` retirée ;
  - comparaison sans casse retirée ;
  - ponctuation finale gardée ;
  - composants « . » et « .. » admis ;
  - garde de la racine retirée ;
  - comparaison sans extension retirée.
- Survivent : contrôle des formes retiré (équivalent) ; erreur du système de fichiers acceptée.
- Témoin sans mutation : passe.
