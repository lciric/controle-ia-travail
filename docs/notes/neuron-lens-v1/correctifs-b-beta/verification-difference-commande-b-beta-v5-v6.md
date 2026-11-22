# Vérification de la différence entre la commande v5 et la commande v6 (lancement de la tranche de l'ajustement de nos lentilles)

**Verdict : employable.** La v6 lève l'unique défaut de la vérification v4 → v5 et ne change rien d'autre que ce qui est permis.

Vérificateur neuf (R2) : modèle Sonnet 5.5 (`claude-sonnet-5-5`). Fichiers lus : `commande-b-beta-v5.md` (empreinte `b1fc8694…`, confirmée), `commande-b-beta-v6.md`, `correctifs-b-beta/verification-difference-commande-b-beta-v4-v5.md`, `devis-b-beta/releve_prix_h100_v3.py`.

## Constats
- `diff v5 v6` : quatre endroits exactement — titre (v5 → v6), en-tête (trois lignes de filiation ajoutées), étape 8 (une phrase), ligne N-1 du tableau des défauts levés. Aucun autre écart.
- Étape 8 v6 : « `dph_total` à 5 % près du prix avec 200 Go de l'offre retenue au relevé (colonne `prix_avec_200_go`) » ; le `dph_total` de l'instance (stockage compris) est donc comparé à la bonne colonne. Les bornes [1,85 ; 2,62], `gpu_name`, la destruction en cas d'échec et la définition de <PRIX> sont inchangées.
- La colonne `prix_avec_200_go` existe dans `COLONNES` du script `releve_prix_h100_v3.py` (ligne 53) ; elle contient `prix_avec_stockage(o)` = `dph_total` + `storage_cost` × 200 / 720 (lignes 62-63 et 91), ce que l'en-tête du relevé dit aussi. La colonne `dph_total` du relevé reste hors stockage supplémentaire (5 Gio comptés seulement) : la correction est la bonne.
- Aucune étape sur 7a, 7b, étape B, étape B bis, P3 ni T0.6 touchée par la différence.

## Réserve mineure
La phrase de l'étape 8 compte deux parenthèses consécutives ; lisible, sans effet.
