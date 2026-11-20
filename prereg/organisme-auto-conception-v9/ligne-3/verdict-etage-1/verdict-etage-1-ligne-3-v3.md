# Verdict de l'étage 1 de la ligne 3 (votes effectifs des juges) — v3

Pièce de classe A, à contre-lire par un autre modèle qui rejouera les critères, puis à sceller par la mère sur main et à soumettre à Lazar. Écrite le 2026-11-20 par l'agent du verdict, modèle O, agent neuf qui n'a écrit ni le préenregistrement, ni les additifs, ni le code, ni l'aide, ni le relevé.

**Version 2.** Elle remplace la version 1 (`verdict-etage-1-ligne-3-v1.md`, `7da76ed456d1563cd3ac10dfc4f58da1dfae331d1701f4ff863b5051bac18574`), gardée sans modification. Elle porte à la lettre les corrections 1 à 5 du § 5 de la contre-lecture `contre-lecture-verdict-etage-1-ligne-3-v1.md` (`a5e2b23bfbf0bda7a24783181f8ce2a623ac11618f892b87db41a2ed807f3c03`, vérifiée contre son compagnon ; verdict « À corriger », mot, taille, table et puissance rejoués égaux sur 83 champs). Pour la correction 4, l'agent du verdict lit lui-même les prédictions par un programme neuf (`lire_predictions_etage_1_v1.py`, sortie `lecture-predictions-etage-1-v1.json`), au lieu de la dernière phrase proposée, comme la correction le permet. Elle rappelle aussi le nœud 2 de l'additif 1 (§ 7, point 5). Aucun mot, aucune taille, aucune table, aucune puissance ne change. Différentiel : `differentiel-verdict-v1-v2.diff`.

**Version 3.** Elle remplace la version 2 (`verdict-etage-1-ligne-3-v2.md`, `f9835cbc2d5b088e011049a2138a9b6d2d4f78d46fd90c757faf415237bb5745`), gardée sans modification. Elle porte à la lettre la correction 1 du § 5 du contrôle `controle-verdict-etage-1-ligne-3-v1-v2-v1.md` (`090d8dd50c295129c78beb669bb66fee2a018f49f40aa8c13fe553c1698542df`, vérifié contre son compagnon ; verdict « À corriger » sur la seule prédiction P3) : P3 est lue sous ses quatre lectures et ses deux sens. Les chiffres viennent de mon programme neuf `lire_p3_etage_1_v1.py` (sortie `lecture-p3-etage-1-v1.json`), comparés par `comparer_p3_contre_lecteur_v1.py` (sortie `comparaison-p3-contre-lecteur-v1.json`) au rejeu du contre-lecteur : 41 champs, aucun écart. Le § 8, point 7 (c), est ajusté. Aucun mot de l'étage 1, aucune taille, aucune table, aucune puissance ne change. Différentiel : `differentiel-verdict-v2-v3.diff`.

## Verdict

**« non, pas à cette taille »** (table gelée, PR l. 314) : la tolérance de l'estimateur ne tient pas aux treize cellules de la règle à n = 100 ; elle y tient à n = 200 et à n = 400. **Pas de dépense** ; la table et un devis à la taille voulue (200 témoins) retournent à Lazar ; la ligne à 25 USD ne part pas (PR l. 233, 241, 378 ; DV l. 9, 172).

## Pièces lues et empreintes

| pièce | sha256 |
|---|---|
| PR, v7 (origin/main, `git show`) | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` |
| A1, v2 | `e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0` |
| A2, v3 | `f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a` |
| DV, v7 | `382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270` |
| `E/etage-1/resultat-etage-1-ligne-3-v3.json` | `eb7a673bc9612458f4c86cf817ef60e58c8118772934c52fbdba18cc4f3c60ce` |
| `E/etage-1/manifeste-etage-1-ligne-3-v3.json` | `6c64c32c1d0bf7257e5b00277051de26dcedffec6fb0193066164cda9053eb92` |
| `E/chronometrage/manifeste-chronometrage-ligne-3-v3.json` | `fe3069ec637f69ff5ae09cb236d13aad644ac01323b91f9e988bef99a53f9db0` |
| mandat de l'agent du verdict | `cd3706925ee07f06fbe17449d08cba9d3f9c9cde91e2a87df8d2c9af36ca1be7` |

Tous les compagnons vérifiés par `env -C DOSSIER sha256sum -c` : OK (y compris le compte rendu d'exécution et le relevé). E = `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/execution-etage-1-v1/`. Les manifestes n'ont pas été relus au fond : leur contrôle (`programme_sha256`, `autorisation`, `dossier_du_code_propre`) est le geste de la mère (A2 l. 91, 137, 138) ; le compte rendu d'exécution le dit fait, égal.

Critères appliqués, écrits avant toute mesure : `criteres-appliques-v1.md` (même dossier).

## 1. Contrôles avant lecture

- **Mélange planté** (A2 l. 104) : aux trois cellules d'alarme (m = 10, 20, 40), 1 000 suites qui changent, 500 « à effet », 500 « sans effet », 1 000 sans changement, 2 000 suites : **conforme**.
- **P2** (PR l. 134, 316) : 248 cellules à deux juges égaux et symétriques (profils 0,05 ; 0,10 ; 0,20 ; 0,30 ; lois 1, 2, 3 ; tous ρ et n). Écart maximal d'erreur équilibrée entre deux des quatre règles (juge 1, juge 2, unanimité, « au moins un ») : **0,0054** (loi 1, taux 0,30, ρ = 0,3, n = 50) ; aucune cellule hors de ± 0,02, aucune hors de ± 0,01 (prédiction). **P2 tenue** : le banc n'est pas invalide.
- Clause (ii) du double rendu (PR l. 326, contrôle de banc) : part d'abstentions par vote à δ = 0 à moins de 0,02 de 0,1275 dans toutes les cellules et pour les trois lois du lecteur.

## 2. Estimateur : la règle de taille

Tolérance (PR l. 177) : |biais| ≤ 0,05 ; erreur quadratique moyenne ≤ 0,10 ; couverture dans [0,90 ; 0,98] ; part « indéfini » ≤ 0,02. Cellules de la règle (PR l. 233 ; A1 l. 81) : deux juges, taux 0,20, sept ρ sous la loi 1, six sous la loi 3.

| n | 50 | 100 | 200 | 400 |
|---|---|---|---|---|
| les treize cellules tiennent | non | **non** | **oui** | oui |

À n = 100, huit cellules sur treize manquent, toutes par la seule erreur quadratique moyenne (biais, couverture et part « indéfini » tiennent partout) :

| loi | ρ | erreur quadratique moyenne à n = 100 | dépassement |
|---|---|---|---|
| 1 | 0,15 | 0,1128 | 0,0128 |
| 1 | 0,30 | 0,1164 | 0,0164 |
| 1 | 0,45 | 0,1104 | 0,0104 |
| 1 | 0,60 | 0,1021 | 0,0021 |
| 3 | 0,15 | 0,1114 | 0,0114 |
| 3 | 0,30 | 0,1167 | 0,0167 |
| 3 | 0,45 | 0,1126 | 0,0126 |
| 3 | 0,60 | 0,1018 | 0,0018 |

Tiennent à n = 100 : loi 1 à ρ = 0 (0,0985), 0,75, 0,9 ; loi 3 à ρ = 0 (0,09999728, sous la borne de 0,10 ; 0,1000 à l'arrondi), 0,75. À n = 200, les treize tiennent (erreur quadratique moyenne de 0,040 à 0,081, couverture de 0,93 à 0,96, aucun « indéfini »). Le détail par cellule et par n est dans `resume-application-etage-1-v1.txt`.

**Taille voulue : 200 témoins** (le plus petit n de la grille où la tolérance tient aux treize cellules ; elle tient aussi à 400). La règle gelée ne retient pas N = 100 : aucune dépense sous ce texte (PR l. 233).

**Monotonie (A1 l. 84)** : l'issue est monotone au niveau de la règle (non, non, oui, oui), et aucune des 195 cellules de la grille n'est non monotone (aucune ne tient à un n pour manquer à un n plus grand). L'audit de symétrie de la règle E n'a donc pas lieu de partir. Audit « trop propre » de l'étage 1 (PR l. 348) : aucune cellule à couverture 1 (aucune « sans réplique hors intervalle »).

## 3. Table « plus petit n qui tient la tolérance » (PR l. 232, 241 ; A1 l. 131)

Valeurs par cellule ; « — » : ne tient à aucun n ≤ 400. Lois 1 et 3 décident ; loi 2 rapportée (PR l. 309).

**Deux juges**

| loi | profil | ρ = 0 | 0,15 | 0,3 | 0,45 | 0,6 | 0,75 | 0,9 |
|---|---|---|---|---|---|---|---|---|
| 1 | taux 0,05 | — | 400 | — | — | 400 | 400 | 400 |
| 1 | taux 0,10 | 400 | 200 | 400 | 400 | 200 | 200 | 200 |
| 1 | taux 0,20 | 100 | 200 | 200 | 200 | 200 | 100 | 100 |
| 1 | taux 0,30 | 200 | 200 | 200 | 100 | 100 | 100 | 100 |
| 1 | sévère | 200 | 200 | 200 | 200 | 200 | 100 | 100 |
| 1 | indulgent | 200 | 200 | 200 | 200 | 200 | 100 | 100 |
| 1 | inégal | 200 | 200 | 200 | 200 | 200 | 200 | 100 |
| 3 | taux 0,20 | 100 | 200 | 200 | 200 | 200 | 100 | (non jouée) |
| 2 | taux 0,05 | — | — | 400 | 400 | 400 | — | 400 |
| 2 | taux 0,10 | 400 | 200 | 200 | 400 | 400 | 400 | 200 |
| 2 | taux 0,20 | 200 | 200 | 200 | 200 | 200 | 200 | 100 |
| 2 | taux 0,30 | 200 | 200 | 200 | 200 | 200 | 100 | 100 |
| 2 | sévère | 200 | 200 | 200 | 200 | 200 | 200 | 100 |
| 2 | indulgent | 200 | 200 | 200 | 200 | 200 | 200 | 100 |
| 2 | inégal | 200 | 100 | 200 | 200 | 200 | 200 | 200 |

**Cinq juges**

| loi | profil | ρ = 0 | 0,15 | 0,3 | 0,45 | 0,6 | 0,75 | 0,9 |
|---|---|---|---|---|---|---|---|---|
| 1 | taux 0,05 | 200 | 400 | 400 | 400 | 400 | 400 | 200 |
| 1 | taux 0,10 | 100 | 200 | 200 | 200 | 200 | 100 | 100 |
| 1 | taux 0,20 | 50 | 100 | 100 | 100 | 100 | 50 | 50 |
| 1 | taux 0,30 | 50 | 50 | 50 | 50 | 50 | 50 | 50 |
| 1 | sévère | 50 | 100 | 100 | 100 | 100 | 50 | 100 |
| 1 | indulgent | 50 | 100 | 100 | 100 | 100 | 50 | 50 |
| 1 | inégal | 50 | 200 | 100 | 100 | 100 | 50 | 50 |
| 4 | taux 0,05 | 200 | — | — | 400 | 400 | 400 | 400 |
| 4 | taux 0,10 | 100 | — | 400 | 200 | 200 | 200 | 200 |
| 4 | taux 0,20 | 50 | 200 | 100 | 100 | 100 | 100 | 100 |
| 4 | taux 0,30 | 50 | 50 | 50 | 50 | 50 | 50 | 50 |
| 4 | sévère | 50 | 100 | 100 | 100 | 100 | 100 | 100 |
| 4 | indulgent | 50 | 100 | 100 | 100 | 100 | 100 | 100 |

## 4. Puissance qui décide et règle de portée (PR l. 234 à 240 ; A1 règle B)

Monde de puissance (deux juges sévères de même profil, taux moyen 0,20, n = 100), écart vrai de 0,10, lois 1 et 3, cellules faisables. Comptes de cellules faisables égaux à ceux du texte (PR l. 238) : unanimité 4 et 2 ; juge seul 2 et 1 ; bras R 2 et 2. Hors du bras R, ρ′ = 0 partout (A1 l. 40). Écart vrai par formule égal à 0,10 dans chaque cellule faisable.

| comparaison | cellules faisables (loi ; ρ ; ρ′) et puissance | plus basse |
|---|---|---|
| contre l'unanimité | loi 1 : 0,1650 ; 0,1705 ; 0,2250 ; 0,3270 (ρ = 0 à 0,45) ; loi 3 : 0,1600 ; 0,1845 (ρ = 0 ; 0,15) | **0,160** |
| contre le juge 1 seul | loi 1 : 0,4685 ; 0,6625 (ρ = 0 ; 0,15) ; loi 3 : 0,4715 (ρ = 0) | 0,4685 |
| contre le juge 2 seul | loi 1 : 0,4450 ; 0,6540 ; loi 3 : 0,4495 | 0,445 |
| contre le juge répété, trois votes | loi 1 : 0,5145 (ρ′ = 0,5) ; 0,4760 (ρ′ = 0,9) ; loi 3 : 0,5040 ; 0,4820 (ρ = 0) | 0,476 |

**Puissance qui décide : 0,160** (contre l'unanimité, loi 3, ρ = 0), sous 0,5. Aucune comparaison sans cellule faisable à l'écart 0,10.

**La règle de portée s'applique** (PR l. 240), et pour **les quatre comparaisons** : chacune a au moins une cellule faisable sous 0,5 (unanimité 0,160 ; juge 1 seul 0,4685 ; juge 2 seul 0,445 ; juge répété 0,476). Les comparaisons d'agrégations sont à déclarer **descriptives avant la dépense, par un additif scellé**, à la lettre, pour l'étage 2 à 100 témoins que ce texte prévoit, et qui ne part pas ; elles ne peuvent plus porter un « oui » (PR l. 343). La mesure des votes effectifs et l'écart ρ′ − ρ restent lus selon leur table.

Rapporté (PR l. 240) : à l'écart 0,05, plus basse 0,043 ; à l'écart 0,15, plus basse 0,4385 (unanimité), et aucune cellule faisable contre le juge seul ni contre le juge répété, comme le texte l'écrit (PR l. 238).

**Limite de lecture, dite** : cette puissance est celle du monde à n = 100 que le texte fixe (PR l. 232, 236). La taille voulue est 200 ; le texte ne dit pas si la règle de portée se relit à 200 témoins, et l'étage 1 n'a pas mesuré cette puissance à 200. Je ne tranche pas : c'est un cas que le texte ne prévoit pas, il revient à Lazar avec le devis (§ 7).

## 5. Autres lectures gelées de l'étage 1, descriptives (PR l. 318 ; aucune ne porte le « oui »)

- **Puissance de la lecture « positif » de ρ′ − ρ** (A1 règle A, information hors règle gelée), part « positif » pour les deux juges, sur les cellules faisables : écart 0,2 (6 cellules) de 0,130 à 0,656 ; écart 0,3 (5) de 0,329 à 0,824 ; écart 0,5 (4) de 0,807 à 0,996. 15 cellules faisables sur 21, comme A1 l. 25.
- **`fefca0bd94064`, branche (2)** (cinq juges, lois 1 et 4) : « réfuté sur le banc » dans 115 cellules sur 364 (60 sur 91 à 25 témoins d'étalonnage, 41 à 50, 11 à 100, 3 à 200 — loi 1, taux 0,30, ρ = 0,3 ; 0,45 ; 0,6) ; « tient sur le banc » dans les 249 autres. Plus petite taille d'étalonnage à partir de laquelle la branche tient dans toutes les cellules : **aucune**. À deux juges : « sans prise ».
- **`fefca0bd94064`, branche (3)** (garde de cadrage, sens (a)) : t = 20 — c = 0,10 et 0,15 « réfuté sur le banc », c = 0,20 et 0,25 « tient sur le banc », c = 0,30 « sans prise » ; t = 40 — c = 0,10 et 0,15 « réfuté », c = 0,20, 0,25 et 0,30 « tient ».
- **`fefca0bd94064`, branche (1)** : non jouée (GO-2026-11-19-73).
- **`fcfa3d98b90f8`** (double rendu, sens (a)), à chaque n : s = 0 « sans prise » ; à s = 0,5 et s = 1, « réfuté sur le banc » à δ = 0 et δ = 0,2, « tient sur le banc » à δ = 0,5. Clause (iii) à s = 0,5 : « sans prise » à δ = 0, « tient » à δ = 0,2 et 0,5. À δ = 0, le « réfuté » dit le coût du mécanisme quand aucun juge ne lit la surface (PR l. 328) ; le « tient » se lit avec la réserve 11.
- **`fa38f9faa24e0`** (bras P, par cellule et par ρ′) : deux juges, 997 « réfuté sur le banc » et 251 « sans prise » ; cinq juges, 654 « réfuté », 432 « sans prise », 6 « tient ». Au profil inégal, le bras R est le meilleur juge répété (A1 l. 55).
- **Alarme `fcbf4a2dd1a57`** : « mesurée, sans mot : aucune règle de mot gelée » (A1 l. 105). **P6 réfutée** (A1 l. 110) par la seule clause « fausse alarme » à m = 40 : 112 suites sans changement en alarme sur 1 000 chez la sentinelle (seuil : plus de 80) ; 34 à m = 10, 53 à m = 20. Clause « détection » non atteinte : sentinelle contre bras apparié, 348 contre 17 à m = 20, 448 contre 21 à m = 40 (215 contre 15 à m = 10, hors clause). Ce mot porte sur une prédiction du rédacteur, non sur la carte.
- **Prédictions** (PR l. 318), lues par l'agent du verdict avec `lire_predictions_etage_1_v1.py` (sortie `lecture-predictions-etage-1-v1.json`). Convention, déclarée : valeurs observées (moyennes sur les 2 000 répliques), sans intervalle sauf où la clause en nomme un, cellule par cellule ; « réfutée » si une clause est atteinte dans une cellule où elle se lit (comme A1 l. 110 pour P6).
  - **P1** : aucune de ses deux clauses de réfutation n'est atteinte (à n = 50 et taux 0,10, deux juges, lois 1 et 3 : 0 cellule sur 7 tient ; à n = 400 et taux 0,20 : 0 cellule sur 13 manque) : non réfutée. Sa prédiction « à la limite à n = 100 pour un taux de 0,20 » n'est pas tenue aux treize cellules (5 sur 13 tiennent).
  - **P2** : tenue (§ 1).
  - **P4** : non réfutée (plus grand gain du bras N sur la majorité stricte fixe, cinq juges, ρ ≥ 0,6, 156 cellules : 0,0103, loi 4, profil indulgent, ρ = 0,6, n = 400 ; seuil 0,02).
  - **P5** (lue sur le suiveur séduisant, PR l. 137) : non réfutée ; à δ = 0,5 et s = 1, les faux acceptés à trait du bras 1 sont sous ceux du bras 2 à chaque n (écart de −0,049 à −0,064, intervalle tout entier sous 0). Les parties de P5 sans clause (rien de mieux à δ = 0 ; part d'abstentions égale à l'instabilité plantée ; baisse « croissant avec δ ») ne sont pas lues contre une clause ; la part d'abstentions est le contrôle de la clause (ii), § 1.
  - **P5 bis** : non réfutée (rondes saines déclenchées au seuil 0,10 : 0,574 à t = 20 et 0,700 à t = 40, au-dessus de 10 % ; au seuil 0,30 à t = 40 : 0,000, sous 10 %).
  - **P5 ter** (suiveur repoussant, sans mot de carte) : non réfutée (à δ = 0,5 et s = 1, bras 1 au-dessus du bras 2 à chaque n, écart de +0,049 à +0,052 ; à δ = 0,5 et s = 0,5, intervalle de l'écart de surface du bras 1 entre −0,348 et −0,285, hors de ± 0,05).
  - **P5 quater** (suiveur séduisant, s = 1) : non réfutée (bras 1 sous le bras 2 à δ = 0,5, de −0,049 à −0,064 ; au-dessus à δ = 0,2, de +0,035 à +0,038, à chaque n).
  - **P6** : réfutée (puce précédente).
  - **P10** : sa clause de réfutation (puissance qui décide de 0,5 ou plus) n'est pas atteinte (0,160).
  - **P3 : lue sur ses quatre lectures possibles** (bras C ou bras P ; contre la majorité stricte ou contre les poids égaux), cinq juges, parce que sa clause ne nomme ni le bras ni la référence ; aucune lecture n'est choisie. Clause « gain de 0,02 ou plus avec des juges échangeables » (loi 1, taux égaux entre juges, 168 cellules) : atteinte dans aucune cellule, sous aucune lecture (plus grand gain : 0,0153). Clause « aucun gain en blocs à 200 témoins d'étalonnage » (loi 4, n = 400, ρ ≥ 0,6, 18 cellules) : sous chacune des quatre lectures, 12 ou 13 cellules sont sans gain et 5 ou 6 ont un gain, de 0,0150 au plus ; aucune n'atteint le gain prédit de 0,02 à 0,06. Sous la convention déclarée plus haut, **P3 est réfutée**, sous les quatre lectures : le mot ne dépend ni du bras ni de la référence. Il dépend de la convention : lue « aucun gain dans aucune cellule de blocs », la clause ne serait atteinte sous aucune lecture. Les deux sens sont rapportés. Ce mot porte sur une prédiction du rédacteur, non sur une carte.

Ces mots décrivent un banc de juges scriptés ; ils ne valident, n'écartent ni ne classent aucune carte (PR l. 329).

## 6. Comparaison avec l'aide (`criteres_mecaniques`, marquée aide, ouverte après mes calculs)

**Aucun désaccord.** Égaux, champ par champ (`comparaison-a-l-aide-v1.json`) : tenue par n aux cellules de la règle ; taille voulue (200 ; clé de l'aide `taille_retenue_par_la_regle`) ; mot de l'estimateur ; P2 « valide » ; plus petit n par cellule (195 sur 195) et par groupe ; puissance qui décide (0,16) et minima par comparaison ; aucune comparaison sans cellule faisable ; portée ; branche (2), les 115 cellules réfutées et « aucune » taille ; branche (3), sens (a), les dix mots ; P6 et ses clauses par m ; mot de la carte de l'alarme. Hors de l'aide, les drapeaux et mots que le code écrit dans les blocs de mesures sont aussi égaux aux miens : drapeau « tient » de l'estimateur (780 sur 780), mots de `fa38f9faa24e0` (2 340 sur 2 340), mots de `fcfa3d98b90f8` (36 sur 36).

Une nuance, non un désaccord : l'aide écrit « descriptives avant la dépense (puissance sous 0,5) » sans dire que cette puissance est celle du monde à n = 100 alors que la taille voulue est 200 (§ 4, limite).

L'aide n'est jamais le verdict : le verdict ci-dessus vient de l'application propre des critères.

## 7. Ce qui revient à Lazar, selon les textes

1. **Taille au-dessus de 100** (PR l. 233, 241, 314 ; DV l. 9, 172) : la taille voulue est 200 témoins. Aucune dépense ; la table ci-dessus et un devis neuf à 200 témoins, au-dessus du plafond de 25 USD de GO-2026-11-19-66 (le DV en donne l'ordre de grandeur : cas haut 44,78 USD, pire 88,36 USD, § 6), retournent à Lazar ; la ligne à 25 USD ne part pas.
2. **Cas non prévu** : la règle de portée est mesurée à n = 100 (PR l. 232, 236), et la taille voulue est 200. Le texte ne dit pas si la portée se relit à 200 témoins, ni si l'additif de portée se scelle sur la puissance à 100 ; aucune puissance n'est mesurée à 200, et l'étage 1 ne se rejoue pas (A1 l. 85). Plus largement, le texte ne prévoit d'étage 2 que sur un « oui » (PR l. 331, 378) : un étage 2 à 200 témoins — banque, plan d'appels, seuil de 40 témoins complets, cellule de stabilité, portée — n'est pas écrit par ce préenregistrement. À trancher par Lazar avec le devis.
3. **n = 50 seul** : sans objet (la tolérance ne tient pas à 50, et tient à 200 et 400).
4. **Banc fautif** : sans objet (mélange planté conforme, P2 tenue, clause (ii) dans sa bande).
5. **Nœud 2 de l'additif 1** (A1 l. 105), rappelé : aucune règle de mot n'est gelée pour la carte de l'alarme `fcbf4a2dd1a57` ; elle reste « mesurée, sans mot ». En écrire une serait un critère gelé neuf, qui revient à Lazar. Ce n'est pas une suite de l'étage 1, mais le nœud reste ouvert. Le nœud 1 (ligne de la table pour « n = 50 seul ») est sans objet ici (point 3).

Aucune revendication ; aucune carte n'est tranchée par un juge (PR l. 47, 345).

## 8. Écarts et réserves de l'agent du verdict

1. **Première commande contre l'en-tête du mandat** : avant d'avoir lu le mandat, ma première commande a listé le dossier E (`ls -la`) et enchaîné deux commandes (`;`) pour vérifier l'empreinte du mandat. Le mandat demandait de respecter son en-tête dès la première commande. Rien sous `archives-reponses-modeles/` n'a été touché ; la liste n'a montré que des noms de fichiers de E. Toutes les commandes suivantes sont simples, sans liste ni joker.
2. **Mesures vues avant les contrôles du geste 2** : pour connaître la structure du résultat, un programme a affiché le premier élément de chaque bloc de mesures (valeurs d'une cellule de chaque bloc, dont des drapeaux et mots calculés par le code hors de `criteres_mecaniques`), avant que les contrôles du mélange planté et de P2 soient faits. Le bloc `criteres_mecaniques` n'a pas été ouvert avant mes calculs. Les deux contrôles ont ensuite passé ; aucune règle n'a été choisie après lecture.
3. **Les blocs de mesures portent eux-mêmes des mots et des drapeaux calculés par le code** (`tient`, `mot_de_la_carte`, `clause_*`, `mot_fa38f9faa24e0_par_rho_prime`, `theorie_p2.garde`) : je ne les ai pas utilisés pour décider ; mon programme recalcule chaque mot des mesures brutes, puis les compare.
4. Bornes de la tolérance lues inclusives, comme écrites ; la cellule loi 3, ρ = 0, n = 100 est à 0,09999728, sous la borne : elle tient sans que l'inclusion joue ; aucune valeur de la grille n'est exactement à une borne. (Vérifié par `lire_predictions_etage_1_v1.py` : valeur `0.09999728055099333` ; plus petite distance à une borne sur les 780 cellules-tailles, 2,7 × 10⁻⁶, celle de cette cellule.)
5. Les bruits de 2 000 répliques (écarts types approchés) sont rapportés dans `application-criteres-etage-1-v1.json` ; ils ne servent à aucun critère, l'issue étant monotone.
6. Je n'ai pas relancé le banc ni le chronométrage ; aucun appel de modèle ; aucune écriture dans le dépôt.
7. **Version 2, écarts à la lettre des corrections, déclarés** : (a) à la correction 2, une parenthèse de vérification est ajoutée après le texte donné ; (b) par cohérence avec la correction 3, « taille retenue (200) » du § 6 devient « taille voulue (200 ; clé de l'aide `taille_retenue_par_la_regle`) » ; (c) à la correction 4, la dernière phrase proposée (« P3, P5, P5 ter et P5 quater : non lues ») est remplacée par ma lecture de P5, P5 ter et P5 quater, que la correction permet ; les chiffres de P1 et P4 sont recalculés par mon programme, égaux à ceux de la contre-lecture. En version 2, P3 restait non lue, pour une raison (le mot dépendrait du bras et de la référence) que les mesures démentent ; en version 3, elle est lue sous ses quatre lectures et ses deux sens (correction 1 du contrôle), par `lire_p3_etage_1_v1.py`. Ma raison de la version 2 s'appuyait sur une phrase de la contre-lecture que le contrôle retire ; je ne l'avais pas recalculée moi-même : c'est un manquement de ma part, à garder déclaré. Rien d'autre ne change que l'en-tête de version, le rappel du nœud 2 (§ 7, point 5, demandé par la session) et la liste des pièces.

## 9. Pièces rendues (même dossier, chacune avec compagnon `.sha256`)

`criteres-appliques-v1.md` ; `controles_avant_lecture_v1.py` et `controles-avant-lecture-v1.json` ; `structure_resultat_v1.py` et `structure-resultat-v1.txt` ; `explorer_resultat_v1.py` et `inventaire-resultat-v1.txt` ; `appliquer_criteres_etage_1_v1.py` et `application-criteres-etage-1-v1.json` ; `resumer_application_v1.py` et `resume-application-etage-1-v1.txt` ; `extraire_aide_v1.py`, `aide-criteres-mecaniques-v1.json` (aide, marquée telle), `resumer_aide_v1.py`, `resume-aide-v1.json` ; `comparer_a_l_aide_v1.py` et `comparaison-a-l-aide-v1.json` ; pour la version 2, `lire_predictions_etage_1_v1.py` et `lecture-predictions-etage-1-v1.json`, et `differentiel-verdict-v1-v2.diff` ; pour la version 3, `lire_p3_etage_1_v1.py` et `lecture-p3-etage-1-v1.json`, `comparer_p3_contre_lecteur_v1.py` et `comparaison-p3-contre-lecteur-v1.json`, et `differentiel-verdict-v2-v3.diff` ; les versions 1 et 2 du verdict, gardées sans modification ; ce verdict. Programmes joués par `python3 -I -B`, bibliothèque standard seule, aucun tirage.

Agent du verdict, modèle O.
