# LISEZMOI — arène « mélange d'équilibre » contre ses témoins à capacité égale — v2

Sous-agent neuf Opus 5.5 (lignée conv-audit), 31 octobre 2026, branche `canal/conv-audit-n04` ; auteur du brouillon 2 et du code v2, qui n'a écrit ni le brouillon 1 ni le code v1. Réponse aux constats CM-01 à CM-17 de `contre-lecture-arene-melange-v1-brouillon1.md` (`37218654…`).

Ce que je n'ai **pas** fait : rien scellé, rien committé, aucun `.sha256` écrit dans le dépôt (les essais du scellement en écrivent dans le dossier temporaire de pytest, hors dépôt), aucun fichier existant modifié (v1 et compagnons vérifiés par `sha256sum -c` : intacts), aucune lecture sous `donnees/`, aucun réseau, aucune clé, **aucune graine tirée de RACINE = 20261201 ni de RACINE_TENUE = 20261202**. Un cache `__pycache__` que j'avais créé dans ce dossier, par un import de vérification sans `PYTHONDONTWRITEBYTECODE`, a été supprimé (il est ignoré par git).

## Ce qui change par rapport à la v1

- **Hypothèse principale** : « B bat les témoins à capacité égale ». Témoins « finale seulement » sur les 9 moniteurs mêmes de B : C1 poids uniformes, C2 poids de Dirichlet (graine dérivée), C3 « ou » déterministe (scores standardisés, λ = 8) ; plus D (paramètres égaux). B > A devient un contrôle de plomberie. L'ancien bras C est retiré, remplacé par C1.
- **A** est nommé « défense unique réentraînée, même oracle ». Ce n'est pas le protocole de Bailey.
- **δ = (1,4 ; 1,8)**, choisis par une règle écrite avant son exécution (`choisir_deltas`, critère sur A seul) sur une racine de calibrage distincte.
- **Lecture** :
  - marges relatives pour la Table 3 (ρ × effet de plomberie du pilote) ;
  - correction de Bonferroni sur 2 δ (Tables 1 et 2) et sur 8 tests (Table 3) ;
  - tables réécrites, complètes, avec un essai d'exhaustivité ;
  - lecture mécanique `lire_tables` comme aide au lecteur R13.
- **Coût par contournement** : seuil relatif (κ = 0,5 de la détection de la cible non modifiée) avec garde de ligne de base, courbe V(δ') et bissection dans l'encadrement.
- **Gardes** :
  - 52 sites `raise GardeArret`, chacun avec un motif unique et un essai qui le provoque ; un essai vérifie cette couverture par l'arbre syntaxique du code ;
  - garde de la racine de décision placée dans `gen` et re-vérifiée dans chaque processus de travail ;
  - identité du préenregistrement vérifiée champ à champ : configuration canonique, empreintes du code et de quatre fichiers de `controle_ia`, versions de numpy et scipy, N ;
  - statuts et itérations de SLSQP consignés, départs non finis comptés.
- **Observation du brouillon 1** (oracle et seuil) : archivée par reproduction avec le code v1 inchangé.

## Fichiers (tous nouveaux)

| Fichier | Rôle | Empreinte |
|---|---|---|
| `preenregistrement-arene-melange-equilibre-v1-brouillon2.md` | brouillon 2 (non scellé : 14 seuils et la contre-lecture 2 à remplir) | `622e50d2ad961654b6daaa96d76a94f6dfd2d67188d9f7af199979359c0a1891` |
| `arene_melange_v2.py` | code gelé (`DELTAS_V2 = (1.4, 1.8)`) ; configuration `1d7544e652ee6ab782577c5731127c7338844ef3d39844d86842688ddb2031a3` | `8e1e651b4be3e6fea6bf6bdf0fc00a19d479aa818323461fbf550582dfdb46bb` |
| `essais/test_arene_melange_v2.py` | 45 essais | `074aa9ff53f7d8d55b3cc922bf511a0b23af8dbf04ddd1d246df1a18e7b2f44d` |
| `calcul-puissance-arene-melange-v2.py` | puissance, tailles par δ, lecture simulée, temps | `0991184bd899c82a192c052b44944e84eeee1858dd8526b0381d038ca0843efc` |
| `calcul-puissance-arene-melange-v2-sortie.txt` | sa sortie sur les deux pilotes, désignée (M) dans le brouillon | `9cf0eaeb764524ad1b337009f4de551a7339fe05fb80405d3e006f6855a72c38` |
| `gel-conception-arene-melange-v2.md` | conception, principe de l'oracle, prédictions signées, écrits **avant** les pilotes | `1628515a8cf2955f328e5785e5de3ec4279211bec73bea47e870413781292b83` |
| `calibrage-deltas-arene-melange-v2.json` | calibrage des δ (racine 20261295, bras A seul) | `f887e9c1051f40490e7c72c24fa74680f6b4e7818c0c9343d6e63a58c8ba933e` |
| `essai-pilote-arene-melange-v2-detection.json` | pilote, oracle détection (racine 20261293) | `121580c88d580fdd88460eb2352455121ce1c9680ba7e0e30a5f7e23ae4d166d` |
| `essai-pilote-arene-melange-v2-logistique.json` | pilote, oracle logistique, descriptif (même racine) | `a948c85a0dc074559133bc29067f6ed4975a1c0818426773822e8b6b5ac70d01` |
| `archive-observation-oracle-v1.py` | reproduction de l'observation du brouillon 1 (code v1, racine 20261291, instance 0, δ = 1,6) | `4338d3558d25a1ae188c9067ba7281a403a17b1db22c6c8691cff5068a988def` |
| `archive-observation-oracle-v1.json` | sa sortie | `0b52cac34b83aa04bca918cf0384d3bd5f3dd0a2154fd39957e17a95d4a65bc4` |
| `journal-pilotes-arene-melange-v2.txt` | commandes, horodatages et empreintes, dans l'ordre des étapes | `fcaa40f8e9099915e6d56eccc0de42deec2ce432a87ef4ad87862e361c1a2391` |
| `LISEZMOI-arene-melange-v2.md` | ce fichier | — |

## Ordre des étapes (prouvé par le journal)

1. Code, puis essais. Les mesures de temps et de plomberie ont été faites sur la seule racine des essais du code, 20261297.
2. Empreinte du code avant calibrage : `ab064418…`.
3. Calibrage (09:15 UTC), puis la seule ligne écrite après lui, `DELTAS_V2` (différentiel d'une ligne).
4. Fichier de gel, avec ses prédictions ; son empreinte est consignée.
5. Pilote « détection » (09:16–09:29 UTC), pilote logistique (09:29–09:42 UTC), archive, puis sortie de puissance.

Le script de puissance, avec sa grille ρ, est daté de 09:18:31 UTC, avant la fin du premier pilote. Aucun changement de conception n'a eu lieu après les pilotes.

## Commandes

```
cd /home/claude/controle-ia-travail
D=brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m pytest -q -p no:cacheprovider $D/essais/test_arene_melange_v2.py   # ≈ 22 s
PYTHONPATH=src python3 $D/arene_melange_v2.py identite        # bloc d'identité à recopier dans le préenregistrement
PYTHONPATH=src python3 $D/calcul-puissance-arene-melange-v2.py $D/essai-pilote-arene-melange-v2-detection.json $D/essai-pilote-arene-melange-v2-logistique.json
# décision : après contre-lecture 2, gel des seuils par Lazar, préenregistrement copié sous prereg/ et scellé, GO
PYTHONPATH=src timeout 4500 python3 $D/arene_melange_v2.py decision --prereg prereg/<nom>.md \
    --instances 0:100 --run-id <AAAAMMJJ-HHMMSS>-arene-melange-v2 --processus 2
```

## Racines lues

| Racine | Usage |
|---|---|
| 20261293 / 20261294 | pilotes v2 (détection, logistique), 48 tâches chacun |
| 20261295 / 20261296 | calibrage des δ, bras A seul, 108 tâches |
| 20261297 / 20261298 | essais du code ; 4 tâches de mesure de temps et de plomberie (seuls les temps et les compteurs ont été lus) |
| 20261291 / 20261292 | (brouillon 1) archive seulement, code v1 ; refusées par garde en v2 |
| 20261201 / 20261202 | **jamais employées** (décision) |

## Résultats des pilotes

Valeurs non opposables ; détail dans (M).

- **Détection** :
  - (iii), moyennes A / B / C1 / C2 / C3 / D : 0,076 / 0,211 / 0,186 / 0,175 / 0,404 / 0,446 à δ 1,4 ; 0,015 / 0,143 / 0,125 / 0,106 / 0,224 / 0,255 à δ 1,8 ;
  - contrastes : B − A +0,135 / +0,128 ; B − C1 +0,025 / +0,018 ; B − C2 +0,036 / +0,037 ; B − C3 −0,193 / −0,081 ; B − D −0,235 / −0,112 ; (ii) B − A −0,061 / −0,069.
- **Logistique** : B ≈ A (+0,003 / +0,0015), poids purs sur 0,29 et 0,12 des tâches.
- **Prédictions du gel** : 12 branches tenues sur 16. Sont réfutées « B ≈ C1 à 0,01 près » (aux deux δ) et « poids purs sur plus de la moitié des tâches sous l'oracle logistique » (aux deux δ).
- **Plomberie** : 0 non-convergence sur 1 248 entraînements ; 0 départ non fini sur 52 218 ; tous les statuts SLSQP à 0 ; au plus 83 itérations ; fausses alertes moyennes à 0,0003 de α au plus.

## Temps mesuré

- Mesure : `time.process_time` par tâche, `time.perf_counter` pour le mur, plus le `time` de bash.
- **Pilote « détection »**, seul processus sur la machine : 12 min 31 s de mur pour 48 tâches. Somme des temps processeur 1 440 s, efficacité 0,96.
- **Par tâche** (6 bras) : moyenne 30,0 s, médiane 29,6 s, maximum 35,7 s.
- **Décision projetée** : N = 100 par δ donne 100 min de processeur, soit **52 min de mur sur 2 cœurs**. La cible de 1 h 15 est tenue ; le N maximal sous 1 h 15 est de 143 au temps moyen et de 121 au temps maximal.
- **Autres exécutions** : calibrage 1 min 14 s ; pilote logistique 12 min 12 s ; archive 36 s ; puissance 23 s ; essais 22 s.
- **Total consommé** : environ 55 min de processeur.

## Réserves et points ouverts

1. **S6 (ρ) décide la classe de C1 et C2.** ρ = 0,10 donne « B > C1 », ρ = 0,25 donne « ≈ » (ce qui déclenche la règle de Lazar), ρ = 0,50 donne « ≈ » pour les deux. La recommandation 0,25 a été écrite après la lecture du pilote ; la grille, elle, a été écrite avant. Le verdict HP (« réfutée ») n'en dépend pas. La lecture sans seuil est toujours recopiée.
2. **Taille de l'équivalence** mesurée jusqu'à 0,013, contre 0,006 nominal, pour B − C1 à δ 1,4. C'est l'effet de l'approximation de Student sur 24 instances (déclaré au S2).
3. **Puissance de la non-régression** sous un écart nul : seulement 0,49 à S5 = 0,02. C'est sans enjeu au vu du pilote (« régression avérée » 1,00), mais c'est une limite.
4. **Tâches longues.** `pool.map` ne garde aucun point de reprise ; la règle de reprise est écrite (§ Plan 5).
5. **Le champ « graines » du manifeste**, ajouté par `creer_manifeste`, n'est pas employé ; c'est déclaré, et la bibliothèque n'est pas modifiée.
6. **Garde de convergence** à 5 % par tâche, soit 26 entraînements : 2 non-convergences dans une tâche arrêteraient la décision. Il y en a eu 0 sur 1 248 aux deux pilotes ; c'est un risque faible, déclaré.
7. **Antériorités** toutes SUPPOSÉ, y compris la convention de non-infériorité citée en S6.
8. **Contre-lecture 2** (R2, un autre modèle) et gel des seuils par Lazar restent à faire. Si une valeur de configuration change, il faut régénérer le bloc d'identité (`identite`) et recalculer les empreintes.
