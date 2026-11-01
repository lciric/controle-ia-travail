# LISEZMOI — arène « mélange d'équilibre » — v5 (jeu réécrit pour poser la question « à classe égale » ; CM4-01 à CM4-09)

Rédacteur neuf Opus 5.5 (lignée conv-audit), 1er novembre 2026, branche `canal/conv-audit-n04`. N'a écrit aucun des brouillons 1 à 4, aucun code v1 à v4, aucune contre-lecture ni vérification de ce pilote.

**Statut : brouillon 5, non gelé ; décisions D-Q2 (nœud de Lazar) et D-T attendues ; vérification courte par un modèle autre qu'Opus ; puis gel des seuils ; puis scellement ; puis calcul décisif.**

Ce que je n'ai **pas** fait : rien scellé, rien committé, aucun `.sha256` écrit, aucun fichier existant modifié, rien lu sous `donnees/`, rien lu ni écrit dans `arene-extension-familles-v1/`, aucun `git fetch`, aucun réseau, aucun modèle ; **aucune graine tirée de RACINE = 20261201 ni de RACINE_TENUE = 20261202**, ni d'une racine des v1 à v4, ni de la plage 20265001–20265999.

## En bref

- **Diagnostic** : la pureté de B′ vient de la **couverture** — dès qu'un moniteur de la classe (u ≥ K = 3 unités) couvre les trois directions auxquelles la contrainte attache l'attaquant, le jeu restreint devient plat et le tirage n'y gagne plus rien (gain du mélange 0,049–0,074 à u = 1, 0,031–0,042 à u = 2, 0,005 à u = 3, ≈ 0,001 à u ≥ 5). Ni le solveur ni la projection sur le simplexe.
- **Condition testable et garde** : jeux témoins à équilibre connu (sain : intérieur retrouvé ; artefact : point-selle reconnu), avant tout lancement ; critère « jeu dégénéré = gain du mélange ≤ 0,01 » (additif b, après que le témoin artefact a montré que la pureté forcée ne voyait pas un point-selle).
- **Règle gelée → u\* = 1** (u = 2 échoue à δ 1,4 : 5 jeux dégénérés sur 16 pour 4 permis) : Q2 se confond avec la Table 1 ; **retrait proposé** (D-Q2, recommandation (a), confiance 0,7). Descriptif : le tirage aide à u < 3 (B_u − M_u +0,04 à +0,06 à u = 2), plus au-delà.
- **Pilote v5** (6 bras) : Q1 réfutée (C3, D) pour la troisième fois ; B − A +0,11 / +0,12 ; A cycle.
- **Temps** : 39,2 s par tâche ; N = 100 à 9 000 s tient jusqu'à e = 0,44 (mesurée : 0,51 à 0,98) ; recommandation 12 600 s pour la marge (D-T).

## Fichiers neufs

| Fichier | Rôle | Empreinte |
|---|---|---|
| `gel-conception-arene-melange-v5.md` | gel v5, écrit avant toute ligne de code v5 et tout calcul (09:14 UTC) | `b55689cbddb1699ac288deb1b8b808e4d9e5d9fe2f827e2b9e827bc56017d2a0` |
| `gel-conception-arene-melange-v5b.md` | additif b (critère de dégénérescence), après les seuls jeux témoins (09:24 UTC) | `a91d29fd748f29d14f3c839594d434569d3a3f6284dac39e856711045601e391` |
| `arene_melange_v5.py` | code v5 (bloc d'identité du brouillon 5) | `71df9a49ba2594837cb38485a50de5b0f25fd210c9f56838f35fdf634c78d575` |
| `essais/test_arene_melange_v5.py` | 115 essais (90 gardes, chacune un essai nommé) | `e29e5221304d0431ee0557e212b96725a31d96eb2fa6ad2033d3fac8dba58801` |
| `diagnostic-purete-arene-melange-v5.json` | diagnostic de la pureté (16 × 2 tâches, échelle u ∈ 1, 2, 3, 5, 9) | `19d9acfb01c324ff34777d7dfa3b50052ec6a27ef271a8fad351cf1bf209d367` |
| `diagnostic-purete-arene-melange-v5-pids.txt` | PID du diagnostic | `6998d3f460047c8c8a6df5fc05c191edcb92eac7624e2233d07977164f7471d3` |
| `essai-pilote-arene-melange-v5-detection.json` | pilote v5 (24 × 2 tâches, 6 bras) | `116084f83fc95d2c9de08a3af97f89667474ff3138d000cd93384fa648fbfab6` |
| `essai-pilote-arene-melange-v5-pids.txt` | PID du pilote | `2ad2727c6386737b5df2dbdcc906287dc2f83011627a113882c8f5e53b376f32` |
| `audit-essai-arene-melange-v5.json` | audit d'essai (instances 0 à 4, deux δ) | `2f1c3931c4d7c394632af871e95096021581b8e59e6a742c5d92d861fe78fa33` |
| `audit-essai-arene-melange-v5-pids.txt` | PID de l'audit | `28d551c040f8c7e9780195690a6d26fdcf155de445d859c3f3c6afd138eb3be3` |
| `calcul-puissance-arene-melange-v5.py` | calcul de puissance v5 (table de temps CM4-01 comprise) | `cb846327082b241c75296af26a58ae5515a517850a4eaf4513a72da7481ecdc1` |
| `calcul-puissance-arene-melange-v5-sortie.txt` | sa sortie, désignée (M5) | `78ff081970a139b814e9a1c57e5d723a88d3d90cb9519c41a7b683c730f9b423` |
| `preenregistrement-arene-melange-equilibre-v1-brouillon5.md` | brouillon 5 (validateur : « Seuil », « Contre-lecture » à remplir ; 19 marqueurs) | `70655e34391c1c8478f2cf80c8cd59a883ae964272960b7da74c3ce058ad7620` |
| `journal-pilotes-arene-melange-v5.txt` | journal horodaté | `50e66a6c61bc7e026507dfd1384f6617a20b20ecba9dd745ef6c8339a87e9835` |
| `LISEZMOI-arene-melange-v5.md` | ce fichier | — |

**Compagnons `.sha256` à créer par conv-audit** (ce rédacteur n'en écrit aucun) : tous les fichiers ci-dessus, et celui du brouillon 4 (`305911b7…`, CM4-07).

## Commandes (depuis un dossier temporaire vide, chemins absolus ; `python3 -I` ignore `PYTHONPATH` : le code ajoute `src/` lui-même)

```
R=/home/claude/controle-ia-travail ; D=$R/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1
python3 -I -B -m pytest -q -p no:cacheprovider $D/essais/test_arene_melange_v5.py          # ≈ 3 min, 115 essais
python3 -I $D/arene_melange_v5.py temoins                                                  # jeux témoins (≈ 2 s)
python3 -I $D/arene_melange_v5.py identite
python3 -I -B $D/calcul-puissance-arene-melange-v5.py $D/essai-pilote-arene-melange-v5-detection.json \
    --audit $D/audit-essai-arene-melange-v5.json --diagnostic $D/diagnostic-purete-arene-melange-v5.json
# décision (après D-Q2, D-T, vérification courte, gel des seuils, préenregistrement copié sous prereg/ et scellé, GO,
# arbre git propre), charge < 0,5 au lancement :
timeout <S8> python3 $D/arene_melange_v5.py decision --prereg $R/prereg/<nom>.md --instances 0:100 --run-id <AAAAMMJJ-HHMMSS>-arene-melange-v5 --processus 2
python3 $D/arene_melange_v5.py orphelins --pids $R/runs/<run-id>/pids-travail.txt [--arreter]      # avant toute reprise
timeout 5400 python3 $D/arene_melange_v5.py audit --prereg $R/prereg/<nom>.md --source-run <run-id> --instances 0:10 \
    --run-id <run-id>-audit --S1 … --S6 … --S15 …
```

## Racines

| Racine | Usage |
|---|---|
| 20264601 / 20264602 | diagnostic de la pureté |
| 20264611 | jeux témoins (chaque lancement) |
| 20264621 / 20264622 | pilote v5 et audit d'essai v5 |
| 20264631 / 20264632 | réservées (reprise, ou pilote à u = 2 si Lazar retient l'option (b)) ; **non employées** |
| 20264641 / 20264642 / 20264643 | essais du code v5 |
| 20264651 | simulations du calcul de puissance v5 |
| v1 à v3 (25 valeurs), toutes celles de la v4, 20264555, 20264777, 20264001, 20264999 ; plage 20265001–20265999 | refusées par garde |
| 20261201 / 20261202 | **jamais employées** (décision) |

## Essais

- `essais/test_arene_melange_v5.py` : **115 réussis** (179,8 s), dont `test_temoins_sain_et_artefacts`, `test_diagnostic_sain_et_choix_de_u`, `test_branche_u1_sans_q2`, `test_bras_v4_inchanges` (le code v4 n'accepte pas les racines v5 : l'essai lui permet la racine des essais v5 dans son seul processus), `test_chaque_garde_a_son_essai` (90 gardes).
- v1 : 25 réussis ; v3 : 57 ; v4 : 97 ; **v2 : 44 réussis, 1 échec connu** (`test_decision_refusee_brouillon2_pour_la_bonne_raison`, CM2-01 : attend que le brouillon 2 n'ait pas de compagnon ; il a été scellé depuis).

## Réserves

1. **Additif b écrit après un calcul** (les seuls jeux témoins, aucune tâche de l'arène) : il durcit la règle (g_u ≥ f_u) ; déclaré au gel et au brouillon ; à juger par la vérification.
2. **Branche « u\* = 1 » ajoutée au code après le diagnostic** (bras de décision et d'audit selon la classe, Table 7 « Q2 retirée ») : écrite au gel v5 § 2 et § 6 comme conséquence de u\* = 1, sans changer le calcul d'aucun bras (recalcul au bit d'une tâche du diagnostic ; continuité v4) ; le diagnostic a tourné sur `1cdf4a58…`, le pilote sur `71df9a49…`.
3. **u = 2 manqué de peu** (5 jeux dégénérés sur 16 au lieu de 4 à δ 1,4) : poser Q2 à u = 2 (option (b)) serait un choix après lecture ; déclaré dans D-Q2.
4. Le diagnostic est en mode léger (sans familles tenues, coût ni courbe) et sur 16 instances : non opposable.
5. **Temps de l'option (b)** estimé (65 à 75 s par tâche), non mesuré.
6. Questions v1 et v2 au collisionneur : elles décrivent A comme réentraîné « contre la dernière attaque » ; dans le code (v1 à v5), A est réentraîné contre le mélange uniforme de **toutes** les attaques passées (meilleure réponse à l'historique, au sens du jeu fictif côté défenseur, déployée en dernier itéré). À corriger dans les pièces servies à Argon et au collisionneur.
7. Aucun commit : l'ordre gel → code → calcul repose sur le journal v5, les empreintes épinglées et les manifestes ; à committer par conv-audit (CM4-05).
8. `resource_tracker` non consigné ; antériorités toutes SUPPOSÉ.
