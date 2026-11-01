# LISEZMOI — arène « mélange d'équilibre » — v4 (Q1 à nombre de paramètres égal ; Q2 à classe égale contre D, à moniteurs égaux contre C3′)

Rédacteur de reprise Opus (lignée conv-audit), 1er novembre 2026, branche `canal/conv-audit-n04`. Le code v4, le gel v4, le calibrage, le pilote v4 et le premier journal v4 sont d'un rédacteur Opus coupé par la limite d'usage le 31 octobre (≈ 13:45 UTC) ; ils ont été **vérifiés et réutilisés tels quels**. Aucun des deux n'a écrit les brouillons 1 à 3, les codes v1 à v3 ni une contre-lecture de ce pilote.

**Statut : brouillon 4, non gelé ; vérification courte par un modèle autre qu'Opus ; puis gel des seuils par Lazar ; puis scellement ; puis calcul décisif.**

Ce que je n'ai **pas** fait : rien scellé, rien committé, aucun `.sha256` écrit, aucun fichier existant modifié, rien lu sous `donnees/`, rien lu ni écrit dans `arene-extension-familles-v1/`, aucun `git fetch`, aucun réseau, aucun modèle ; **aucune graine tirée de RACINE = 20261201 ni de RACINE_TENUE = 20261202**, ni d'une racine déjà employée, ni de la plage 20265001–20265999.

## Pièces trouvées à la reprise et ce que j'en ai fait

| Pièce (non scellée à l'arrivée) | Vérification | Sort |
|---|---|---|
| `gel-conception-arene-melange-v4.md` | écrit avant tout calcul : présent au commit `f65feb1a` (12:51 UTC) avant le code du calibrage (`c34a06d7`, 12:57 UTC) et le calibrage (13:05 UTC) ; empreinte épinglée dans le code | réutilisé |
| `arene_melange_v4.py` | diff contre le code du calibrage (`git show c34a06d7`) : seule la ligne `DELTAS_V4` diffère ; 78 gardes, chacune avec un essai | réutilisé |
| `calibrage-deltas-arene-melange-v4.json` | 48 instances × 9 δ, A seul, racine gelée, gel au manifeste ; moyennes et erreurs-types recalculées : identiques ; règle réappliquée : (1,4 ; 1,6) | réutilisé |
| pilote v4 en deux parties (`…-instances-00-05.json`, `…-05-24.json`) et leurs PID | même code, même configuration, même racine, instances disjointes, 48 tâches ; commande `orphelins` saine | réutilisé |
| `essais/test_arene_melange_v4.py` | présent (la consigne de reprise le disait absent) ; 3 essais attendaient le brouillon 4 | réutilisé ; passe en entier une fois le brouillon 4 écrit |
| `calcul-puissance-arene-melange-v4.py` | lit les deux parties et l'audit ; gardes de racine et d'empreinte | réutilisé ; sortie produite |
| `journal-pilotes-arene-melange-v4.txt` | s'arrête au lancement du pilote (étape 5) | laissé intact ; **suite** dans `journal-pilotes-arene-melange-v4b.txt` |
| brouillon 4, sortie de puissance, LISEZMOI v4, JSON du pilote complet, audit d'essai v4 | absents | **écrits** (noms ci-dessous ; aucun `*brouillon4*` n'existait à l'arrivée) |

## Fichiers neufs de cette reprise

| Fichier | Rôle | Empreinte |
|---|---|---|
| `preenregistrement-arene-melange-equilibre-v1-brouillon4.md` | brouillon 4 (non scellé : 15 seuils, commit et contre-lecture 4 à remplir ; validateur : « Seuil », « Contre-lecture ») | `305911b7ab1945d7607377ede9c8cbfcf2257834bca6d6aadcf7c19be41f8160` |
| `essai-pilote-arene-melange-v4-detection.json` | pilote v4 complet (union des deux parties, 48 tâches, analyse recalculée par `analyser`) | `4d1fb23f0c72de79270609fa6516020f71611e54210dc1a02059c3c67db36b8e` |
| `assembler-pilote-arene-melange-v4.py` | script d'assemblage (gardes de `charger_tous` ; 24 × 2 tâches exigées ; sortie neuve) | `406db1c3de37f4d76df809ffdf26231b7fcfaf0659e9296563cbd720fbfb0832` |
| `audit-essai-arene-melange-v4.json` | audit d'essai v4 : attaquant indépendant, instances 0 à 4, deux δ, 6 bras ; 2 375 s de mur | `528b5cd4f68b48812895a39ecd7b249cd3e9dffdb888f14e6244486dc3102ead` |
| `calcul-puissance-arene-melange-v4-sortie.txt` | sortie du calcul de puissance v4, désignée (M4) | `45a7fe3b56d80f571ffbaf02203fe1c9993d7aa162a1e0161aeed289decb8428` |
| `journal-pilotes-arene-melange-v4b.txt` | journal, suite (reprise du 1er novembre) | `e92f06900e6397f2c603addabe9b3b380bb31d4f0a2cc8921ce2bd16df19f8bb` |
| `LISEZMOI-arene-melange-v4.md` | ce fichier | — |

## Commandes (depuis un dossier temporaire vide, chemins absolus)

```
R=/home/claude/controle-ia-travail ; D=$R/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1
export PYTHONPATH=$R/src
python3 -I -B -m pytest -q -p no:cacheprovider $D/essais/test_arene_melange_v4.py          # ≈ 6 min
python3 -I $D/arene_melange_v4.py identite
python3 -I $D/arene_melange_v4.py audit-essai --pilote $D/essai-pilote-arene-melange-v4-detection-instances-00-05.json \
    --instances 0:5 --sortie <NOUVEAU>.json --processus 2
python3 -I -B $D/assembler-pilote-arene-melange-v4.py <NOUVEAU>.json $D/essai-pilote-arene-melange-v4-detection-instances-00-05.json \
    $D/essai-pilote-arene-melange-v4-detection-instances-05-24.json
python3 -I -B $D/calcul-puissance-arene-melange-v4.py $D/essai-pilote-arene-melange-v4-detection-instances-00-05.json \
    $D/essai-pilote-arene-melange-v4-detection-instances-05-24.json --audit $D/audit-essai-arene-melange-v4.json
# décision (après vérification courte, gel des seuils, préenregistrement copié sous prereg/ et scellé, GO), machine sans autre calcul lourd :
timeout 9000 python3 $D/arene_melange_v4.py decision --prereg $R/prereg/<nom>.md --instances 0:100 --run-id <AAAAMMJJ-HHMMSS>-arene-melange-v4 --processus 2
python3 $D/arene_melange_v4.py orphelins --pids $R/runs/<run-id>/pids-travail.txt [--arreter]      # avant toute reprise
timeout <S8 audit> python3 $D/arene_melange_v4.py audit --prereg $R/prereg/<nom>.md --source-run <run-id> --instances 0:10 \
    --run-id <run-id>-audit --S1 … --S6 … --S15 …
```

Note (CM3-13) : les compagnons `essais/*.sha256` sont en chemin relatif ; les vérifier depuis `essais/`.

## Racines

| Racine | Usage |
|---|---|
| 20264101 / 20264102 | recalibrage des δ (A seul, 48 instances × 9 δ) |
| 20264201 / 20264202 | pilote v4 (48 tâches) et audit d'essai v4 (10 tâches) |
| 20264211 / 20264212 | réservées (reprise du pilote) ; **non employées** |
| 20264301 / 20264302 / 20264303 | essais du code v4 |
| 20264401 | simulations du calcul de puissance v4 |
| déjà employées (20261101, 20261291–98, 20261301, 20261311–16, 20262291/97, 20262313, 20269501/02, 20269731/32, 20269741/42) ; plage 20265001–20265999 | refusées par garde |
| 20261201 / 20261202 | **jamais employées** (décision) |

## Résultats (non opposables ; détail dans (M4))

- **Calibrage (A seul, 48 instances × 9 δ, racine 20264101)** : V(A) moyen (erreur-type) 0,6 : 0,372 (0,018) ; 0,8 : 0,312 (0,018) ; 1,0 : 0,233 (0,019) ; 1,2 : 0,161 (0,016) ; **1,4 : 0,102 (0,013)** ; **1,6 : 0,056 (0,011)** ; 1,8 : 0,026 (0,006) ; 2,0 : 0,007 (0,002) ; 2,4 : 0,001 (0,0004) → **δ = (1,4 ; 1,6)** ; couple instable sous rééchantillonnage ((1,2 ; 1,6) 43 %, (1,4 ; 1,6) 33 %, (1,4 ; 1,8) 23 %).
- **Q1** (réplique v2 et v3) : B − A +0,128 / +0,139 ; B − C1 +0,020 / +0,021 ; B − C2 +0,040 / +0,036 ; B − C3 −0,194 / −0,144 ; B − D −0,234 / −0,180 → Q1 réfutée (C3, D).
- **Q2** : B′ − D +0,002 / +0,004 ; B′ − C3′ +0,007 / +0,011 ; poids de B′ purs 71 % / 58 %, **pureté forcée par le jeu sur toutes les tâches pures** ; moniteur dominant surtout celui du tour 2, 3 ou 4 (le dernier : 2 et 1 tâches pures) → « Q2 non exercée » (plafond de la classe), 1,000 conditionnel au pilote, 0,990 avec son incertitude.
- **Condition d'application** : A ne progresse pas (I1 +0,002 / −0,001) ; I3 0,90 / 0,94 contre la valeur nulle 0,7345 (simulée 0,7329) : I3 − nul +0,17 [B2 +0,10 ; +0,23] / +0,21 [+0,16 ; +0,25] → « cycle » ; B ≈ nul ; D, B′ sous le nul.
- **Audit d'essai v4** : aucun drapeau ; |écart moyen| ≤ 0,0011 ; fausse alerte simulée du critère 0,002 (0,011 à bruit doublé) ; puissance 0,76 à un écart de 0,010, 1,00 à 0,015.
- **S10** : fausse alerte simulée v3 0,323 ; k = 3 0,095 ; **k = 4 (repli écrit d'avance) 0,025**.
- **Gel v4 § 4** : 31 branches, 29 tenues, 2 réfutées (V(A) ≥ 10α au δ bas : 0,082 ; S10 à k = 3).
- **Temps** : 60,7 s de processeur par tâche (max 87,3) ; décision N = 100 : 101 min de mur à efficacité 1 (67 % du délai) ; efficacités mesurées 0,52 (pilote) et 0,51 (audit) sur machine partagée → dépassement ; condition de lancement écrite (machine sans autre calcul lourd). Audit de la décision : 40 min à efficacité 1.
- **Plomberie** : 3 non-convergences sur 1 632 (2 dans une tâche : S18 = 0,05 aurait arrêté le pilote) ; 0 départ non fini sur 69 918 ; fausses alertes à 0,0002 de α au plus.

## Essais

- `essais/test_arene_melange_v4.py` : **97 réussis** (348,9 s ; `python3 -I -B -m pytest -q -p no:cacheprovider`, depuis un dossier temporaire vide), dont les 3 qui lisent le brouillon 4 (refus de décision sur copie, validateur et identité), `test_chaque_garde_a_son_essai` (78 gardes), `test_bras_v3_inchanges`, `test_bras_v2_inchanges`.
- v1 : 25 réussis ; v3 : 57 réussis ; **v2 : 44 réussis, 1 échec connu** (`test_decision_refusee_brouillon2_pour_la_bonne_raison` attend que le brouillon 2 n'ait pas de compagnon `.sha256` ; il a été scellé depuis — CM2-01, corrigé à partir de la v3 par l'essai sur copie temporaire ; fichier scellé, non modifiable ici).

## Réserves et points ouverts

1. **Temps (divergence non résolue avec R-739)** : 9 000 s exigent une efficacité ≥ 0,67 ; mesurée 0,51–0,52 sur la machine partagée de cette session. Condition de lancement écrite (charge < 0,5 avant le lancement) ; options pour Lazar : N = 80 ou `timeout 12600`.
2. **Repli S10 déclenché** (k = 4) : prédiction du gel réfutée, règle appliquée telle qu'écrite.
3. **δ instables** : le couple (1,4 ; 1,6) ne sort que 33 % des rééchantillonnages ; V(A) au pilote 0,082 au δ bas (sous 10α) et 0,036 au δ haut (3,6 α).
4. **Audit** : bruit apparié estimé sur 5 tâches par δ ; I3 jamais changé par l'audit des tours de A (contrôle faible de la forme du cycle).
5. **Table 2** : la ligne « imprécis » recouvre aussi une régression démontrée d'ampleur non tranchée (cas du pilote à 24 instances) ; non corrigé (règle de lecture), option pour Lazar.
6. **Q2 « non exercée »** prévue à 0,99 : la décision répliquera un plafond ; elle ne dira pas si le tirage aide sous ce plafond. Options non implantées : témoin « mode », « ou » sur le support de B′, maxout de 73 unités, conception à moins d'unités.
7. Le pilote v4 a tourné en deux lancements simultanés (4 processus sur 2 cœurs, machine chargée) : sans effet sur les résultats (tâches déterministes), mais l'efficacité mesurée n'est pas celle d'une décision seule.
8. CM3-08 : consigner dans `registres/decisions.md` l'empreinte et l'heure du gel v4 — à faire par conv-audit.
9. Antériorités toutes SUPPOSÉ ; `resource_tracker` non consigné.
