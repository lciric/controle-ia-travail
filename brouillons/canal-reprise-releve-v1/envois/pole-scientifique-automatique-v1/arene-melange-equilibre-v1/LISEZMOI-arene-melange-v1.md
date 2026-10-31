# LISEZMOI — arène « mélange d'équilibre » contre « unique réentraîné » — v1

Sous-agent neuf Opus 5.5 (lignée conv-audit), 31 octobre 2026, branche `canal/conv-audit-n04`. Décision de Lazar R-695 (« gooo »), piste 3 du brainstorm P-041, test (b), sur processeur. Rien n'est scellé ni committé par moi ; aucun `.sha256` écrit ; aucune lecture sous `donnees/` ; aucun réseau ; **aucune exécution sur la racine de décision**.

## Ce que fait le code

`arene_melange_v1.py` (numpy, scipy) : arène coévolutive synthétique. Monde : loi propre N(0, I₆) ; loi cible = mélange de 3 gaussiennes à distance 4 de l'origine ; l'attaquant choisit les moyennes et écarts-types diagonaux d'un mélange de 3 gaussiennes dans une boîte, sous la **contrainte de comportement** « distance (Wasserstein d'ordre 2 entre composantes appariées, en moyenne quadratique) ≤ δ » à la cible (piste 2). Le défenseur est un moniteur linéaire ou maxout sur échantillons, seuillé à α = 1 % de fausses alertes sur des échantillons propres. L'attaquant joue en dernier à chaque tour : meilleure réponse par SLSQP sur un objectif lissé à échantillons de Monte-Carlo fixés, plusieurs départs tirés, projection déclarée et comptée.

Quatre bras, chacun avec sa propre trajectoire de T = 8 tours, à partir d'un moniteur commun au tour 0 :
- **A** unique réentraîné sur toutes les attaques passées (protocole de Bailey et collègues) ;
- **B** mélange d'équilibre, par double oracle : matrice de gains moniteur × attaque, programme linéaire (HiGHS) pour les deux stratégies d'équilibre, nouveau moniteur entraîné contre la stratégie d'équilibre de l'attaquant ;
- **C** mélange uniforme de moniteurs entraînés comme ceux de A ;
- **D** unique « maxout » à capacité égale (T + 1 unités, autant de paramètres que le mélange final de B), réentraîné sur toutes les attaques passées.

Sorties par tâche (δ, instance) : (iii) détection contre la meilleure réponse finale (la plus forte de deux attaques, standard et renforcée) ; (ii) détection sur 50 lois tenues à l'écart tirées d'une racine à part, et sa courbe par tour ; (i) détection sur les attaques vues ; coût par contournement (bissection sur δ', piste 5) ; nouveauté résiduelle par tour (piste 4) ; (iii) par tour ; poids de B ; contrôles (fausses alertes, valeur du jeu restreint, projections, non-convergences, temps processeur par tour). `analyser` calcule les écarts appariés par instance et leurs intervalles par rééchantillonnage (IC95, IC90).

Gardes (R5), toutes avec essai sain et essai artefact dans `essais/test_arene_melange_v1.py` : refus de partir en décision sans préenregistrement scellé, conforme et **identifié** (identifiant, RACINE, RACINE_TENUE, empreinte de la configuration, empreinte du fichier de code exécuté) ; refus des racines de décision en essai ; refus d'écraser ; programme linéaire (statut, égalité primale-duale) ; matrice de gains ; poids ; admissibilité des lois ; échantillonnage stratifié ; moniteurs non finis ou non calibrés ; fausses alertes hors α ± 0,005 ; non-convergence > 5 % (déclenchée pour de vrai en essai avec 60 itérations) ; tour 0 reproductible ; plafond de 600 s de processeur par tâche ; reproductibilité bit à bit.

## Fichiers (empreintes au moment de la remise)

| Fichier | Empreinte |
|---|---|
| `arene_melange_v1.py` | `6402dc6b2998d2f48262ddfe1d4d0d13b6a6115fcc8d01852c3b7c8182fd0d3b` |
| `essais/test_arene_melange_v1.py` | `52168b51dd2eff313af8dfcf4b7fbcd9c410f9111553240ba0687f0fa9a8d085` |
| `calcul-puissance-arene-melange-v1.py` | `65df7c5228b31ffb23a320009af278909e012973b1e76d42a05c7e1b215c1f5b` |
| `calcul-puissance-arene-melange-v1-sortie.txt` (sortie sur le pilote v2) | `17863f83097d8380fae23dfbfdf00fc5e2ce3d7349ade194c2be020dbca63fda` |
| `essai-pilote-racine-essai-v2.json` (pilote retenu ; code `9ed8c8b5…`) | `f094b495381db7e342e73432ccb16abfe1bdc06498c4f77928cd7e2d7aff78c5` |
| `essai-pilote-racine-essai-v2-journal.txt` | `f32ed14bab0267820cd1371a2da125d05767cc72a139216c209d482ed6cdad76` |
| `essai-pilote-racine-essai-v1.json` (pilote dépassé, sans attaquant renforcé ; code `ce10256f…`) | `f34e33d7026aef042cd68adcb793cf72ce0b4d52dc78eeead29a1f591df26c2d` |
| `essai-pilote-racine-essai-v1-journal.txt` | `e97c54b320d2d60ca3e33465742cb5e2fdccb751e84a0cd3a08c48a9129bac0c` |
| `preenregistrement-arene-melange-equilibre-v1-brouillon1.md` | non scellé (brouillon) |

Configuration `CONFIG_V1` : `6685585fcfc028e0617d6786eb78bdb4fc159930af8fdf0444be1085f960d2ca` (identique dans les pilotes v2 et dans le code remis). Entre le pilote v2 et la remise, le code n'a changé que par l'ajout de la vérification de l'empreinte du code dans `exiger_identite_prereg` (aucun changement de calcul).

Note : le commit `5919719a` (posé par l'agent parent pendant le pilote v2) contient un état intermédiaire de ce dossier, dont un journal v2 vide ; les fichiers ci-dessus sont la version de remise.

## Commandes

```
cd /home/claude/controle-ia-travail
D=brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1
# essais (≈ 6 s)
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m pytest -q -p no:cacheprovider $D/essais
# pilote sur racine d'essai (refuse RACINE et RACINE_TENUE ; refuse d'écraser)
PYTHONPATH=src python3 $D/arene_melange_v1.py essai --instances 0:24 --sortie $D/<nouveau-nom>.json --processus 2
# puissance (refuse tout fichier tiré d'une racine de décision ou d'une autre configuration)
PYTHONPATH=src python3 $D/calcul-puissance-arene-melange-v1.py $D/essai-pilote-racine-essai-v2.json
# décision : après contre-lecture, gel des seuils par Lazar, préenregistrement copié sous prereg/ et scellé, GO
PYTHONPATH=src timeout 7200 python3 $D/arene_melange_v1.py decision --prereg prereg/<nom>.md \
    --instances 0:<N> --run-id <AAAAMMJJ-HHMMSS>-arene-melange-v1 --processus 2
```

Le mode décision appelle `exiger_prereg_arene` **avant** toute graine de décision, puis `creer_manifeste(decisif=True, prereg=…)` (arbre propre exigé), puis écrit `diag/<run-id>/resultats-arene.json` et `analyse-arene.json` par `ecrire_resultat` (scellés). Il n'a jamais été lancé, sauf dans l'essai qui vérifie qu'il refuse de partir.

## Ce qui a été lu (racine d'essai seulement)

| Exécution | Racines | Tâches | Code |
|---|---|---|---|
| plomberie interactive, instance 0, δ = 1,6 (oracle logistique, puis oracle « détection » et variante logistique) | RACINE_ESSAI = 20261291, RACINE_ESSAI_TENUE = 20261292 | 3 tâches | versions intermédiaires |
| pilote v1 | idem | 48 (24 instances × 2 δ) | `ce10256f…` |
| pilote v2 (retenu) | idem | 48 (24 instances × 2 δ) | `9ed8c8b5…` |
| essais du code | RACINE_ESSAI, RACINE_ESSAI + 1000 (= 20262291, pour vérifier qu'une autre racine change le résultat), RACINE_ESSAI_TENUE ; petite configuration (d = 3, K = 2, T = 2) et instances 0 et 1 de la configuration complète | quelques tâches par passage | courant |

**RACINE = 20261201 et RACINE_TENUE = 20261202 n'ont jamais servi à tirer une graine.**

Résultats du pilote v2 (non opposables, détail dans la sortie de puissance § 1-2, § 6) : B − A sur (iii) = +0,125 (δ = 1,6) et +0,037 (δ = 2,4) ; D − B = +0,186 (δ = 1,6) et −0,005 (δ = 2,4) ; B − C ≈ 0 ; B − A sur (ii) ≈ −0,06 ; attaquant renforcé : aucun changement notable (au plus 0,0005 en moyenne).

## Temps processeur mesuré

Mesure : `time.process_time()` du processus (un fil par processus, `OMP_NUM_THREADS=1`) pour chaque tâche, chaque tour et la phase finale ; temps de mur par `time.perf_counter()` et par le `time` de bash.

- Pilote v2 : 48 tâches sur 2 processus ; mur 590,4 s (bash : réel 9 min 50,8 s, utilisateur 19 min 5,4 s) ; somme des temps processeur des tâches 1 145,0 s ; efficacité 0,97.
- Par tâche (4 bras) : moyenne 23,85 s, médiane 24,20 s, maximum 32,01 s.
- Par tour, moyenne sur les tâches (tours 1 → 8) : A 0,10 → 0,09 s ; B 0,09 → 0,19 s ; C 0,08 → 0,20 s ; D 0,35 → 0,71 s. Phase finale (deux meilleures réponses finales, familles tenues, coût par bissection) : A 1,46 s ; B 3,07 s ; C 5,77 s ; D 5,50 s. L'essentiel du temps est dans la phase finale et la préparation (échantillons tenus, calibration), non dans les tours.
- Projection pour la décision : N = 100 instances par δ → 79,5 min de processeur, 41,0 min de mur sur 2 cœurs ; N = 150 → 119,3 min, 61,5 min ; N maximal sous 2 h de mur au temps maximal par tâche : 218.
- Pilote v1 : mur 369,5 s (réel 6 min 10 s, utilisateur 11 min 59 s). Essais : ≈ 6 s. Script de puissance : 8,3 s.
- Total consommé par moi : environ 35 minutes de processeur.

## Réserves

1. **Oracle du défenseur changé après une observation d'essai** (logistique → « détection », pour les quatre bras) : justifié par le principe du double oracle, mais décidé après avoir vu B = A sur une instance d'essai. La contre-lecture doit le juger (R3, R4) ; S13 laisse le choix à Lazar.
2. **D est-il la bonne « capacité égale » ?** Même nombre de paramètres que le mélange final de B, mais une autre famille de fonctions (maxout déterministe) ; un témoin quadratique, ou un « OU » déterministe des moniteurs mêmes de B, serait une autre lecture de la consigne. Non fait.
3. (iii) est une borne haute de la valeur du jeu (attaquant local). Le contrôle par l'attaquant renforcé ne montre pas d'insuffisance au pilote, mais ne la prouve pas absente.
4. Le coût par contournement est censuré à 1 pour environ la moitié des tâches de B, C, D : l'écart B − A en fraction de δ est une borne basse.
5. À δ = 2,4, le bras A est presque entièrement contourné (0,0008) : régime proche de la dégénérescence (S11).
6. Le calcul de puissance emploie la borne de Student, la décision le percentile du rééchantillonnage.
7. La garde « aucun départ fini » de l'attaquant et le plafond de mur total (externe) ne sont pas provoqués par un essai.
