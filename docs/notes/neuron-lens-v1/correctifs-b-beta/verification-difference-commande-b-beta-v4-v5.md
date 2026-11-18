# Vérification de la différence entre la commande v4 et la commande v5 (lentilles, tranche d'ajustement)

**Verdict : à corriger (légèrement).** Un défaut, une ligne : l'étape 8 compare le prix de l'instance (stockage compris) à la colonne `dph_total` du relevé, qui est hors stockage. Le reste de la différence est juste.

Vérificateur neuf (R2) : Claude Sonnet 5.5 (`claude-sonnet-5-5`). Lecture seule, rien exécuté chez le loueur.

## Différence (`diff` v4 / v5)
Quatre endroits seulement : titre (v4 → v5), en-tête (trois lignes ajoutées pour la filiation), étape 8 (une phrase), tableau des défauts levés (une ligne N-1). Rien d'autre n'a changé (étapes 7, 9 et suivantes, prix, plafonds, minuterie identiques).

## Points jugés
1. **Champs demandés par l'étape 8** : `dph_total` et `gpu_name` sont tous deux dans `CHAMPS` de `suivi_vast_v6.py` (ligne 44) ; le filtre ne garde que ces clés. Juste.
2. **Exécutabilité de « `dph_total` à 5 % près de celui de l'offre au relevé »** : le relevé `releve_prix_h100_v3.py` écrit bien une colonne `dph_total` par offre (`COLONNES`, fonction `ligne`). **Mais** cette colonne est le prix de l'offre **hors stockage** : le script calcule à part `prix_avec_200_go = dph_total + storage_cost × 200 / 720`, et c'est cette dernière colonne que l'étape 4 utilise pour choisir l'offre (≤ 2,62 et ≥ 1,85). L'étape 8 lit au contraire le `dph_total` de l'instance « (stockage compris) ». Comparer l'un à l'autre est donc inexact : l'écart est le coût du stockage de 200 Go (quelques pour cent du prix horaire selon le tarif de stockage de l'hôte), qui peut dépasser les 5 % et faire détruire à tort une instance saine, ou masquer un vrai écart. **Correction proposée** : « à 5 % près du `prix_avec_200_go` de l'offre retenue au relevé » (même phrase de l'étape 8, et même mot dans la ligne N-1 du tableau).
3. **« Créée depuis cette offre, par son identifiant : même machine par construction »** : juste au vu de l'étape 7 (la commande de création prend `<OFFRE>`, l'identifiant d'offre de la colonne `id` du relevé) ; une offre disparue ou déjà louée fait échouer la création (branche d'échec de l'étape 7), elle n'aboutit pas sur une autre machine. Réserve mineure : la garantie tient à l'identifiant d'offre, pas à un identifiant de machine relu ; la phrase le dit assez (N-1 déclaré).
4. **Autre changement** : aucun hors du tableau de levée.

## Conclusion
Employable après la correction d'une expression (colonne comparée : `prix_avec_200_go`). Sans elle, l'étape 8 contient un contrôle numériquement faux, ce que la v5 voulait précisément éviter.
