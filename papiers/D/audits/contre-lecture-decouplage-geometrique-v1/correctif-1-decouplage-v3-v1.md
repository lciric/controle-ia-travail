# Correctif 1 de la v3 de la section sur le découplage géométrique (boucle unique)

- **Source** : `verification-decouplage-v3-v1.md` (dans ce dossier), même contre-lecteur Opus que pour la v2. Verdict : la v3 corrige fidèlement, avec réserves. Il relève deux défauts majeurs nouveaux et dix mineurs.
- **Pièce corrigée** : `papiers/D/theorie/decouplage-geometrique-v3-correctif-1.tex`. La v3 reste telle quelle. Marque : **À REVOIR PAR FABLE**. Non diffusé.
- **Rejeu** : `verif/v2_jouet.py` a été rejoué par la fille 2 sur une copie. Il redonne 0,359 → 0,415 (sonde disjointe, ReLU), 2,96e-6 (Adam sur le réseau linéaire), 7,1e-7 (moment initial non nul), et ‖W_{:,S}‖ = 3,0557. La phrase du LISEZMOI « `v2_jouet.py` n'a pas été rejoué » est donc dépassée.

| Défaut | Correction |
|---|---|
| 1 (majeur) : les « 48 tirages » attribués au réseau du papier | Décrits tels qu'ils sont : 12 graines, la tâche du papier et une variante à deux directions, réseaux linéaire et ReLU, 600 pas, baisse jamais supérieure à 10⁻³ |
| 2 (majeur) : « coïncident seulement si Σ ∝ I » | Les deux orthogonalités coïncident pour tout w quand l'espace des lignes de W est invariant par Σ (par exemple Σ ∝ I, ou Σ = diag(1, 2, 3) avec W = e₁) ; elles diffèrent en général |
| 3 : attributions | (a) partie 2 et cas gaussien de la partie 1 ; (b) « masking of gradients as in gradient routing » ; (c) « related phenomena (evasion of latent-space monitors under optimization) » |
| 4 : aire réajustée en ReLU | 0,832 → 0,833–0,835, sous la valeur de Bayes ; « generically injective » en linéaire |
| 5 : fichier bibliographique absent | Non corrigé dans le texte ; à faire avec la vérification sur PDF (R7) |
| 6 : 3e-6 | Conditions précisées : 200 pas d'Adam, taux 1e-3, réseau linéaire, sonde orthogonale partagée ; contre 2e-17 en descente de gradient |
| 7 : optimiseurs | Premier moment initial d'Adam (7e-7) ; décroissance découplée pure « sans ancrage d'activation et avec 1 − γλ > 0 » |
| 8 : sonde orthogonale à W_{:,S} | Existence si \|S\| > rang ; orthogonalité à l'instant t ; sonde choisie après coup, ce qui est légitime |
| 9 : paragraphe numérique | ‖W_{:,S}‖ de 0 à 3,06 ajouté à côté de ‖Ww‖ ; la figure est à refaire |
| 10 : borne « attained » | Seule la première inégalité est atteinte |
| 11 : remarque nouvelle | « Under Operator A » ; « mostly » ; seuil au 95e centile des scores honnêtes ; renvoi au script |
| 12 : en-tête et LISEZMOI | En-tête aligné ; le rejeu de `v2_jouet.py` est fait (voir ci-dessus) |
