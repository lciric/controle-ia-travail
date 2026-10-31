# LISEZMOI — arène « mélange d'équilibre » — v3 (Q1 à nombre de paramètres égal, Q2 à classe de fonctions égale)

Sous-agent neuf Opus 5.5 (lignée conv-audit), 31 octobre 2026, branche `canal/conv-audit-n04`. Auteur du brouillon 3 et du code v3 ; n'a écrit ni les brouillons 1 et 2, ni les codes v1 et v2, ni les contre-lectures. Réponse aux constats CM2-01 à CM2-16 de `contre-lecture-arene-melange-v2-brouillon2.md` (`c6751de3…`).

**Statut : brouillon 3, non gelé ; contre-lecture 3 par un modèle autre qu'Opus ; seuils (S1 à S18) à Lazar.**

Ce que je n'ai **pas** fait : rien scellé, rien committé, aucun `.sha256` écrit dans le dépôt, aucun fichier existant modifié (compagnons v1 et v2 revérifiés : intacts), rien lu sous `donnees/`, aucun réseau, **aucune graine tirée de RACINE = 20261201 ni de RACINE_TENUE = 20261202**, ni des racines d'essai déjà employées (20261291 à 20261298, 20269501, 20269502 : refusées par garde en v3).

## Ce qui change par rapport à la v2

- **Bifurcation de conception postérieure au pilote v2 (déclarée, décision de routine de conv-audit)** : Q2, à classe de fonctions égale. **B′** = double oracle dont l'oracle rend des maxouts à 9 unités (classe du moniteur final de D) ; **C3′** = « ou » déterministe des moniteurs de B′. Prédiction Q2 écrite dans `gel-conception-arene-melange-v3.md` **avant** toute exécution de B′ (journal, étapes 1 à 3).
- Q1 renommée « à nombre de paramètres égal » (B déploie 7 paramètres par requête, C3 et D 63).
- **Condition d'application** mesurée : matrice H (moniteur du tour s × attaque du tour t), I1 (progrès), I2 (oubli), I3 (retours) ; Table 5.
- Rubrique « Portée d'une réfutation et d'une confirmation ».
- **Marges par principe** : m = S1 = 0,02 pour tous les témoins (plus de ρ, plus d'ancrage sur B − A).
- **Déclencheur 9** (« conforme et trop propre ») et **attaquant indépendant** (SLSQP lourd à départs structurés + stratégie d'évolution sans gradient), modes `audit` (tâches de la décision) et `audit-essai`.
- S10 par erreur-type ; tailles mesurées avec le rééchantillonnage réel ; effet bloquant de chaque déclencheur écrit ; déclencheur 3 sorti de la Table 1.
- **Arrêt par PID** (R10) : PID et instants de départ consignés, TERM converti en arrêt du pool, survivants arrêtés par PID, garde « aucun orphelin », commande `orphelins`.
- Essai de refus sur **copie temporaire** du brouillon (CM2-01).
- Bras A, B, C1, C2, C3, D **inchangés** : essai `test_bras_v2_inchanges` (sorties identiques champ à champ au code v2 sur une même racine).

## Fichiers (tous nouveaux)

| Fichier | Rôle | Empreinte |
|---|---|---|
| `preenregistrement-arene-melange-equilibre-v1-brouillon3.md` | brouillon 3 (non scellé : 18 seuils, commit et contre-lecture 3 à remplir) | `3ac8fe1fd1ee4cdb6ebc904a739f8098226703b02b6c0be428e2a572449dced0` |
| `arene_melange_v3.py` | code (δ = (1,4 ; 1,8) inchangés) ; configuration `02db9c9183f4f601d9a77fd956f61f92de3bbafe31d78b809096743c6b15ac44` | `88c8781815007d92d5b0af17a7dc1995c00eae0773085c5a0ca35a1aafee4f0d` |
| `essais/test_arene_melange_v3.py` | 57 essais (62 gardes, chacune avec son essai) | `3fa646dbf132c813d924511c1e8fd7f190a2924049949d93c3b8003b17bc0051` |
| `gel-conception-arene-melange-v3.md` | conception v3 et prédictions, écrits **avant** toute exécution de B′ | `25035088a36742db86c3b6be818e5c97fabd8dd48c1f9e56934fce15e9f09506` |
| `essai-pilote-arene-melange-v3-detection.json` | pilote v3 (racine 20261311, 24 instances × 2 δ, 8 bras) | `e171e303330e47195757a9855a55181aea1bf1f75078fa9c6c7891033221427d` |
| `essai-pilote-arene-melange-v3-pids.txt` | PID des processus de travail du pilote | `4a767a82d99dda69d350f172f858430c1ddc70a5c1832a6497de4e5a91c94736` |
| `audit-essai-arene-melange-v3.json` | attaquant indépendant sur 2 tâches du pilote | `681efec1e67fb18effb687dee6dd9873f5339a87c2c321fe5698876569ee2172` |
| `calcul-puissance-arene-melange-v3.py` | puissance et tailles avec la règle réelle, lecture simulée, temps | `1d92d6a18c2d79c1f56630ac7e0ec9bf8610648d5331c194cb5a36546dd48c20` |
| `calcul-puissance-arene-melange-v3-sortie.txt` | sa sortie, désignée (M3) | `00a2234972c7bc0f0138a5c3e2c6b9fc1c6810b7c888b1b91342aecd10e434e5` |
| `journal-pilotes-arene-melange-v3.txt` | commandes, horodatages, empreintes, ordre des étapes | `90def1506e5a528c322046d270d54f5ea3cd71b1e7d0b4eed0a1bb583669a312` |
| `LISEZMOI-arene-melange-v3.md` | ce fichier | — |

## Ordre des étapes (journal)

1. 10:23 UTC : code v3 écrit, jamais exécuté (`04df57d2…`).
2. 10:25 UTC : gel v3 et prédictions Q2.
3. 10:29 UTC : premiers essais (premières exécutions de B′) ; deux corrections de plomberie, puis une accélération de C3′ sans changement de fonction ; code final `88c87818…` à 10:38 UTC.
4. 10:39–11:08 UTC : pilote v3 ; 11:08–11:19 : audit d'essai ; 11:19–11:24 : puissance ; 11:30 : brouillon 3, 57 essais réussis.

## Commandes

```
cd /home/claude/controle-ia-travail
D=brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m pytest -q -p no:cacheprovider $D/essais/test_arene_melange_v3.py   # ≈ 1 min
PYTHONPATH=src python3 $D/arene_melange_v3.py identite
PYTHONPATH=src python3 $D/calcul-puissance-arene-melange-v3.py $D/essai-pilote-arene-melange-v3-detection.json $D/audit-essai-arene-melange-v3.json   # ≈ 5 min
# décision (après contre-lecture 3, gel des seuils, préenregistrement copié sous prereg/ et scellé, GO) :
PYTHONPATH=src timeout 9000 python3 $D/arene_melange_v3.py decision --prereg prereg/<nom>.md --instances 0:100 \
    --run-id <AAAAMMJJ-HHMMSS>-arene-melange-v3 --processus 2
# si un arrêt externe survient, avant toute reprise :
PYTHONPATH=src python3 $D/arene_melange_v3.py orphelins --pids runs/<run-id>/pids-travail.txt [--arreter]
# audit d'attaquant indépendant (déclencheur 9), après scellement de l'analyse :
PYTHONPATH=src timeout 5400 python3 $D/arene_melange_v3.py audit --prereg prereg/<nom>.md --source-run <run-id> \
    --instances 0:5 --run-id <AAAAMMJJ-HHMMSS>-arene-melange-v3-audit
```

## Racines lues

| Racine | Usage |
|---|---|
| 20261311 / 20261312 | pilote v3 (48 tâches) et audit d'essai (2 tâches) |
| 20261313 / 20261314 | essais du code v3 ; 3 mesures de temps d'une tâche (temps et compteurs seulement) |
| 20261315 / 20261316 | réservées à l'option de recalibrage des δ ; **non employées** |
| 20261291 à 20261298, 20269501 / 20269502 | déjà employées ; refusées par garde en v3 |
| 20261201 / 20261202 | **jamais employées** (décision) |

## Résultats du pilote v3 (non opposables ; détail dans (M3))

- **Q1** (réplique la v2) : B − A +0,104 / +0,118 ; B − C1 +0,021 / +0,017 ; B − C2 +0,030 / +0,035 ; B − C3 −0,174 / −0,078 ; B − D −0,223 / −0,104. Q1 réfutée (C3, D).
- **Q2** : B′ − D +0,001 / +0,009 ; B′ − C3′ +0,008 / +0,029 ; B′ − B +0,224 / +0,113. Poids de B′ purs dans 62 % et 54 % des tâches (support 1,4 et 1,8). **Prédiction Q2 réfutée** (j'attendais D ≥ B′ et C3′ ≥ B′) ; sous la règle gelée, la décision lirait « Q2 non exercée » (probabilité simulée 0,998).
- **Condition d'application** : A ne progresse pas (I1 −0,001) et oublie (I2 +0,07 / +0,11) ; retours 88 % / 93 %. Prédite et tenue.
- **Audit d'essai** : changements de 0,000 à 0,005 ; aucun artefact.
- **Plomberie** : 2 non-convergences sur 1 632 ; 0 départ non fini sur 69 750 ; 2 départs au statut 9 ; fausses alertes à 0,0006 de α au plus.

## Temps

- Par tâche (8 bras) : moyenne 57,0 s, maximum 79,8 s ; pilote : 28 min 42 s de mur pour 48 tâches, efficacité 0,80 (machine partagée).
- Décision projetée : N = 100 → 190 min de processeur, **120 min de mur** sur 2 cœurs ; N = 60 → 72 min. N maximal sous 1 h 15 : 62.
- Audit de 10 tâches : 19 min de processeur sur 2 cœurs ; 51 min au rythme de mur mesuré sur la machine chargée.
- Consommé dans cette session : ≈ 60 min de processeur.

## Réserves et points ouverts

1. **Q2 sera vraisemblablement « non exercée »** : à classe égale, l'équilibre du jeu restreint est presque pur ; la règle n'a pas été changée après le pilote. Si Lazar veut une question Q2 exercée, il faut une nouvelle conception (par exemple moins d'unités par moniteur de B′), donc un nouveau gel.
2. **Lacune** : pas de maxout unique de 73 unités (même total que B′).
3. **S18** : à la valeur de configuration actuelle (0,05), probabilité ≈ 0,16 que la décision s'arrête par la garde de convergence ; recommandation 0,10 (changement d'un champ, identité à régénérer).
4. **Tailles réelles** au-dessus du nominal dans quelques cellules (jusqu'à 0,017 contre 0,006 en Q1, 0,026 contre 0,013 en Q2) ; déclaré au S2.
5. **A près du plancher à δ 1,8** (1,5 α et 2,7 α aux pilotes) ; option de recalibrage à décider par Lazar.
6. **Temps** : N = 100 dépasse 1 h 15 ; recommandation `timeout 9000`, option N = 60.
7. Le processus `resource_tracker` de multiprocessing n'est pas consigné parmi les PID (il se termine avec le processus principal).
8. Le pilote logistique n'a pas été rejoué en v3 (celui de la v2 tient pour S13 ; il ne touche pas aux bras nouveaux).
9. Antériorités toutes SUPPOSÉ.
10. Contre-lecture 3 (modèle autre qu'Opus) et gel des seuils par Lazar à faire ; à tout changement de valeur de configuration, régénérer le bloc d'identité.
