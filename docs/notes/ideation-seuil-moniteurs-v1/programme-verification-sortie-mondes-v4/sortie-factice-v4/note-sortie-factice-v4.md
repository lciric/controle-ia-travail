# Note — sortie factice v4 (décalage de F cohérent), programme de vérification v4 inchangé

- Auteur : développeur du programme de vérification de la sortie des mondes, modèle O. 2026-11-21. Pièce de travail (classe C).
- Cause : constat du développeur du programme de vérité v2. Le compte rendu de correspondance tiré de la sortie factice v3 (`c35c4bc3…`) donne « dérive incohérente : F écartée » au contrôle de la dérive : le décalage de 0.5 ne triple pas le taux sous la loi transmise.
- **Aucun programme v5.** Le programme de vérification v4 (`7b4e04a1cbd68c4a1b4f2abd2d21535a889f7407108003f8b9d136f67c259f9f`) est joué tel quel, depuis son dossier. Seules la fabrique et la sortie factice passent en v4.

## Ce qui change

- `fabriquer_sorties_factices_v4.py`. Dans T09, `decalage_en_ecarts_types` est **calculé par programme**, avec `statistics.NormalDist`, pour la loi factice de la tranche de F à n = 299, normale(0.25, 1.0). La formule est δ = (q₀,₉₉ − q₀,₉₇) / σ, soit 0,4455542659, écrit « 0.4456 ». La valeur 0,446 de la note de conception n'est pas reprise : elle est retrouvée. Rien d'autre ne change (différentiels joints : la fabrique, et la sortie factice, une seule valeur).
- `verifier_decalage_factice_v4.py` relit le fichier produit et recalcule les taux au seuil à 99 % : il rend le verdict à la tolérance absolue de 0,001 sur 0,03.
- `test_verifier_sortie_auteur_mondes_v4_sur_factice_v4.py` est une copie des essais v4. Il n'en change que la fabrique, la sortie factice, le chemin du programme v4 et la valeur attendue (« 0.4456 »).

## Contrôles

**Contrôle a posteriori** (`controle-decalage-factice-v4.txt`) :

```
loi de la tranche a 299 : normale(mu=0.25, sigma=1.0)
decalage transmis (ecarts types) : 0.4456
decalage exact qui triple (ecarts types) : 0.4455542659
taux avant derive au seuil : 0.0100000000
taux apres derive au seuil : 0.0300031120
ecart absolu a 0.03 : 3.112e-06 ; tolerance absolue 0.001
verdict : coherente
```

**Programme de vérification v4 sur la sortie factice v4** :
- vérification : code 0, lisible, aucun écart ;
- correspondance : 37 témoins convertis et 2 non convertis (LM1 et LM2, monde M, D3) ;
- `derive_de_F` : valeur « 0.4456 », clé de rang 2, tranche de rang 2.

**Essais.** Les 316 essais v4, rejoués sur la sortie factice v4, passent tous.

**Programme de vérité v2** (`…/dev-verite-temoins-mondes-v2/calculer_verite_temoins_imposes_v2.py`, `bcd7fbacc38da278adb99be6417237fb66c00bfbebafcdca8afa20b261cbe9a3`), non contre-lu de mon côté. Lancé par `python3 -I -B … --recalculer ENTREE SORTIE --correspondance CORRESPONDANCE`, il sort en code 0 : 37 témoins calculés, 0 refusé. Son bloc `derive_de_F`, recopié tel quel :

```
"accord_avec_la_lecture_de_T09": true,
"decalage_qui_triple_sous_cette_loi_en_ecarts_types": 0.44555426589,
"decalage_transmis_en_ecarts_types": 0.4456,
"loi_de_la_tranche": {"parametres": {"mu": 0.25, "sigma": 1.0}, "type": "normale"},
"rang_de_la_cle": 2,
"statut": "calcule",
"taux_apres_derive": {"borne_erreur": 1.0000316547076338e-12, "mode": "flottant_borne", "valeur": 0.030003111972, "valeur_exacte": null},
"taux_vise": "3/100",
"tolerance_absolue": "1/1000",
"tranche_associee_a_T09": {"n_calibration_contient_299": true, "rang": 2, "rangs_des_tranches_a_299": [2], "regle": "…"},
"verdict": "dérive cohérente"
```

## Ce que je n'ai pas lu, et ce que j'ai effacé

- Je n'ai lu ni la table de vérité, ni le reste de la sortie du programme de vérité. Je n'ai cherché dans cette sortie que le bloc `derive_de_F` et les comptes. La recherche a laissé paraître les premières lignes du témoin libre LA1, qui portent des valeurs factices.
- Cette sortie est effacée : elle portait des valeurs calculées sous des lois factices.

développeur du programme de vérification de la sortie des mondes, modèle O
