# Critères gelés appliqués par l'agent du verdict — étage 1 de la ligne 3 — v1

Pièce de l'agent du verdict, modèle O. Écrite le 2026-11-20 après lecture des quatre textes et avant toute ouverture des mesures (`resultat-etage-1-ligne-3-v3.json` non ouvert à l'heure d'écriture).

Textes (tirés de origin/main par `git show`, empreintes recalculées égales au mandat) :
- PR `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` — `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0`
- A1 `prereg/organisme-auto-conception-v9/additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md` — `e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0`
- A2 `prereg/organisme-auto-conception-v9/additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v3.md` — `f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a`
- DV `prereg/organisme-auto-conception-v9/devis-ligne-3-etage-payant-v7.md` — `382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270`

Les numéros de ligne sont ceux de ces copies.

## 0. Contrôles avant lecture (ordre du mandat, geste 2)

**C0-a. Mélange planté de l'alarme** — A2 l. 104 : « *Valeurs attendues à la taille décisive*, par la règle D de l'additif 1 (2 000 suites) : 1 000, 500, 500 et 1 000. Une autre valeur serait une faute du banc, à rendre à la mère avant toute lecture. » Appliqué à chaque cellule d'alarme (m = 10, 20, 40), clé `comptes_du_melange_plante` (A2 l. 101) : suites qui changent = 1 000 ; « à effet » = 500 ; « sans effet » = 500 ; sans changement = 1 000.

**C0-b. P2** — PR l. 134 : « P2 (théorie, deux juges égaux et symétriques). Les quatre règles (juge 1 seul, juge 2 seul, unanimité, « au moins un ») ont la même erreur équilibrée : écarts entre règles, en moyenne sur les 2 000 répliques, dans ± 0,01 (prédit ; signe : nul). *Réfutation* : un écart hors de ± 0,02, qui dirait une faute du banc. » Et table PR l. 316 : « P2 manquée (écart entre règles hors de ± 0,02 chez deux juges égaux et symétriques) | **invalide** : faute du banc, à corriger avant toute lecture ». Appliqué : à J = 2, dans chaque cellule où les deux juges ont le même taux dans les deux classes (profils de taux 0,05 ; 0,10 ; 0,20 ; 0,30, toutes lois à deux juges, tous ρ, tous n), écart moyen d'erreur équilibrée entre toute paire des quatre règles S1, S2, U, F ; P2 manquée si l'un d'eux est hors de ± 0,02. Le seuil « ± 0,01 » est la prédiction, rapportée ; « ± 0,02 » décide.

Si C0-a ou C0-b tombe : « faute du banc » ou « invalide », rien d'autre n'est lu.

## 1. Tolérance de l'estimateur — PR l. 177

« **Tolérance de l'estimateur** (une cellule « tient ») : |biais| ≤ 0,05 ; erreur quadratique moyenne ≤ 0,10 ; couverture entre 0,90 et 0,98 ; part « indéfini » ≤ 0,02. Les quatre ensemble. »

Lu avec PR l. 169 (« erreur quadratique moyenne » = sa racine, dans l'unité de ρ ; biais et erreur contre la valeur plantée de la cellule) et PR l. 161 (valeur plantée poolée). Bornes inclusives telles qu'écrites (≤, « entre » lu inclusif 0,90 ≤ c ≤ 0,98).

## 2. Cellules de la règle et règle gelée de taille — PR l. 233 ; A1 l. 81

PR l. 233 : « **Règle gelée du nombre de témoins de l'étage 2.** N = 100 si la tolérance tient à n = 100 pour un taux d'erreur de 0,20, aux sept valeurs de ρ sous la loi 1 et aux six valeurs jouées (ρ ≤ 0,75) sous la loi 3. Sinon, **aucune dépense** : la table et un devis à la taille voulue retournent à Lazar (le devis donne le coût par dizaine de témoins). »

A1 l. 81 : « les cellules à deux juges, taux d'erreur 0,20 égal dans les deux classes, aux sept valeurs de ρ sous la loi 1 et aux six sous la loi 3 ; la loi 3 n'est jouée qu'à deux juges. « Tient à n » veut dire : les treize cellules tiennent à ce n. »

## 3. Table gelée de l'estimateur — PR l. 309 à 316

PR l. 309 : « (lois 1 et 3 décident ; la loi 2 est rapportée) ».

| issue observée (PR l. 313 à 316) | verdict |
|---|---|
| la tolérance tient à n = 100 pour un taux d'erreur de 0,20, aux sept valeurs de ρ sous la loi 1 et aux six valeurs jouées (ρ ≤ 0,75) sous la loi 3 | « oui » de l'étage 1 : l'étage 2 se joue à 100 témoins |
| elle tient pour un n de la grille plus grand, pas à 100 | « non, pas à cette taille » : pas de dépense ; table et devis à la taille voulue rendus à Lazar |
| elle ne tient à aucun n ≤ 400 pour un taux de 0,20 | « non » : l'estimateur est trop bruité ou faux ; résultat porté tel quel, étage 2 non joué |
| P2 manquée (écart entre règles hors de ± 0,02 chez deux juges égaux et symétriques) | invalide : faute du banc, à corriger avant toute lecture |

## 4. Règle E — A1 l. 80 à 85

A1 l. 80 : « Je n'ajoute aucune ligne à la table gelée ». l. 82 : si la tolérance tient à n = 50 et à aucun de 100, 200, 400 : « cas non prévu par la table gelée : la tolérance tient à n = 50 et à aucun n plus grand », avec la table par n et les tolérances manquantes. l. 83 : pas d'étage 2, aucune dépense, table à Lazar. l. 84 : « Cet audit part **pour toute issue non monotone** (la tolérance tient à un n et manque à un n plus grand de la grille), que la table ait une ligne ou non : il dit, par cellule, quelle tolérance manque, de combien, et si l'écart tient dans le bruit de 2 000 répliques. Quand une ligne de la table s'applique à la lettre […], le mot reste celui de la table, et l'audit est joint. » l. 85 : aucune relance.

Monotonie lue sur « tient aux treize cellules à n » (la règle) et, à titre d'audit, cellule par cellule.

## 5. Table « plus petit n qui tient la tolérance » — PR l. 232 ; A1 l. 131 (choix 4)

PR l. 232 : « Pour J = 2 et pour J = 5, la table « plus petit n qui tient la tolérance », par taux d'erreur et par loi ». A1 l. 131 : « « plus petit n qui tient » = le plus petit n où la cellule tient ». Rendue par cellule (loi, profil, ρ, J).

## 6. Règle gelée de portée — PR l. 234 à 240 ; A1 règle B (l. 39 à 42)

PR l. 240 : « *La puissance qui décide* est la plus basse, sur les quatre comparaisons et sur leurs cellules faisables des lois 1 et 3, pour l'écart de 0,10. Si elle est sous 0,5, ou si une comparaison n'a aucune cellule faisable, les comparaisons d'agrégations sont déclarées **descriptives avant la dépense**, par un additif scellé : elles ne peuvent plus porter un « oui ». » PR l. 194 : « puissance exigée 0,5 ». PR l. 238 : cellules infaisables nommées. A1 l. 40 : bras R à ρ′ = 0 hors du monde planté pour le bras R. « Sous 0,5 » lu strict : 0,5 tient.

## 7. Ce que l'étage 1 rend — PR l. 241

« le verdict de l'étage 1, la table « plus petit n qui tient la tolérance », la taille que la règle du nombre de témoins retient, et la puissance qui décide. Si la taille voulue est 200 témoins, un devis neuf, au-dessus du plafond de GO-2026-11-19-66 (cas haut 44,78 USD au devis, § 6), retourne à Lazar ; la ligne à 25 USD ne part pas. » Avec PR l. 378 (« étage 1 non « oui » — pas d'étage 2 ») et DV l. 172.

## 8. Autres critères gelés de lecture de l'étage 1 nommés par le texte (descriptifs, sans « oui »)

- PR l. 318 : « lecture descriptive par cellule, contre les prédictions P3 à P6 et contre le critère de réfutation de chaque carte ; aucun de ces bras ne porte le « oui » de la ligne ».
- PR l. 320 (`fa38f9faa24e0`), l. 321 (branche (2) de `fefca0bd94064`), l. 322 (branche (3)), l. 323 (branche (1), non jouée), l. 324 à 328 (`fcfa3d98b90f8`, clauses (i), (ii), (iii), mot par cellule, sens (a) décide).
- PR l. 326 : clause (ii) — part d'abstentions par vote à δ = 0 à plus de 0,02 de 0,1275 « dit une faute du banc ». Contrôle de banc, lu à côté de C0.
- A1 l. 105 à 112 (silence 2) : l'alarme `fcbf4a2dd1a57` ne reçoit aucun mot ; P6 lue sur ses deux clauses (fausse alarme du bras B > 80 sur 1 000 à chaque m ; détection « à effet » du bras B ≤ bras D à m = 20 et 40).
- A1 règle A (l. 23 à 28) : puissance de « positif » de ρ′ − ρ, information, hors règle gelée.
- PR l. 348 (audit de symétrie, « trop propre » à l'étage 1) : « une cellule sans aucune réplique hors intervalle ».

Ces lectures sont des mesures décrites ; elles ne changent pas le verdict de l'étage 1 (PR l. 318). Elles sont appliquées dans la mesure où les champs du résultat les portent ; ce qui n'est pas appliqué est dit.

Agent du verdict, modèle O.
