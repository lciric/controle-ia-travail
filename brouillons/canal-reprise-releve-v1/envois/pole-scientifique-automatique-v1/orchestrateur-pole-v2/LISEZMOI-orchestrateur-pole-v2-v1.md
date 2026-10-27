# Orchestrateur du pôle, version 0.2.0 — juge v1 et expérience 1 — LISEZMOI v1

Lignée conv-audit (instance du 27 octobre 2026, autre compte). Écrit à partir de 07:40 UTC (heure lue sur `date -u`).
Régime exploratoire pour tout ce qui précède l'expérience (R-522) ; l'expérience 1 elle-même se préenregistre (R1).

## Verdict

- Le juge v1 de la note `experience-1-juge/conception-experience-1-juge-v1.md` (`560f4a4c…`) est codé : **ordre
  d'exécution secret** tiré par le noyau après le gel, membre **« urne »** dans 𝓛, loi **« sans remise »**, **garde du
  plan d'exécution** ; avec les contrôles de l'expérience 1 (batterie T1b à six structures, T1b-fille, artefacts,
  puissance). **105 essais passent** (83 de v0, inchangés, et 22 nouveaux).
- Essais de fumée et exploration (graine 777, déclarés, non opposables) : le **socle** tient (0 promotion sur les 18
  contrôles fatals hors filles, 20 répétitions) ; le **critère des filles a un trou antérieur à v1** : une fille « parent
  mélangé à une loi aveugle fixe » est promue contre le nul augmenté (58/200 sous v0, 63/200 sous v1, sans aucune dérive) ;
  T1b-fille cède par la même porte (29/200 sous v1, toutes quand la moyenne de la dérive est loin de l'uniforme).
- L'expérience 1 garde le juge de la note tel quel ; un huitième tricheur (« parent et loi aveugle ») est ajouté au
  critère des filles, et la lecture est faite en deux parties (socle, filles) plus l'issue globale de la note.

## Ce qui change par rapport à `orchestrateur-v0` (jamais écrasé, R12)

| fichier | changement |
|---|---|
| `pole/selection_pari.py` | `BIBLIOTHEQUE_STANDARD_V1` (v0 + urne) ; membre `urne` (Σ_k ln c_k(t)! − ln t!) ; lois `calendrier`, `deterministe`, `sans_remise` ; `construire_engagement(…, plan_execution=…)` (« ordre_naturel » par défaut, comme v0 ; sous « ordre_secret », une instance ne porte que « z » et « g ») ; `ordre_execution` ; `tirer_frais(…, graine_noyau=…)` ; `verifier_plan_execution` et `evaluer(…, graine_noyau=…)` ; exception `PlanExecutionNonConforme` (sous-classe de `TiragesNonLies`, rattrapée par le cycle) |
| `pole/controles_pari_v1.py` (nouveau) | les lignes de l'expérience 1, trois juges (v1, v0, v1 sans urne), lecture gelée `juger_v1` |
| `pole/experience_juge_v1.py` (nouveau) | écriture scellée du manifeste (avant tout calcul), du rapport JSON et du rapport Markdown |
| `pole/pole.py` | options `--experience-juge-v1`, `--graine-maitresse` (exigée), `--repetitions`, `--essai`, `--familles` |
| `pole/__init__.py` | version 0.2.0 |
| `essais/test_juge_v1.py` (nouveau) | urne contre énumération exhaustive (n ≤ 6) et contre des lois échangeables (indépendantes, Pólya, sans remise) ; placement des issues par indice du plan ; ce que voit le monde ; garde du plan (cas sain, six artefacts) ; lois nouvelles ; mondes de la batterie ; gardes de l'expérience ; lecture gelée ; ligne de commande ; essai de fumée de la batterie T1b |

Tout le reste (cycle, fiches, mémoire, recombinaison, adaptateurs, exemples) est identique à v0 : le cycle du pôle reste
en ordre naturel et sur la bibliothèque de v0 tant que le juge v1 n'est pas adopté.

## Lancer (depuis ce dossier)

Utiliser un Python où `claude_agent_sdk` est **invisible** (ici `/opt/venv-essaim-sim-v1/bin/python`, environnement
virtuel sans paquets du système) : aucun essai ne peut alors démarrer l'outil réel, même par erreur.

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
$PY -I -B -m unittest                                    # 105 essais, environ 100 secondes
$PY -I -B pole --experience-juge-v1 --graine-maitresse G --sortie DOSSIER_NEUF --horodatage "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
# essai non décisif : ajouter --essai --repetitions 20 (et au besoin --familles T1b,T9)
```

L'expérience décisive refuse : moins de 1 000 répétitions, une exécution partielle, les graines 20261026 (exploration de
v0) et 777 (essais de fumée), un dossier de sortie non vide. Durée mesurée : 18 secondes pour 20 répétitions de toutes
les lignes, soit environ 15 minutes pour 1 000 (processeur, un cœur, Python 3.13.17).

## Essais de fumée et exploration (déclarés ; graine 777 ; non opposables)

- Essai 1 (20 répétitions, toutes familles, avant l'ajout du huitième tricheur) : socle 0 promotion ; T1b-fille 3/20
  sous v1 ; artefacts tous vus.
- Exploration (200 répétitions) : T1b-fille sous v1, promotions selon la composante constante de la dérive (milieu de
  `a`) : 15/61 (0,1), 0/67 (0,3), 14/72 (0,6) ; « parent + loi aveugle fixe » (q permutation de (0,45 ; 0,1 ; 0,45)),
  sans dérive : 58/200 (v0), 63/200 (v1). Conclusion d'exploration : l'ordre secret retire l'avantage de l'heure ; ce
  qui reste est une loi aveugle moyenne que le nul augmenté ne contient pas (il ne mélange le parent qu'à l'uniforme et à
  la marginale d'entraînement).
- Essai 2 (20 répétitions, toutes familles, code final) : socle 0/20 sur ses 18 contrôles fatals ; filles : « parent et
  loi aveugle » 5/20 et T1b-fille 3/20 sous v1 ; artefacts tous vus ; pari couvert ε = 0,05 : 2/20 sous v1 contre 20/20
  sous v0 (coût de l'urne sur les petits effets).

## Limites connues

- Simulation seulement ; mondes synthétiques ; K = 3, dimension 2, 200 tirages.
- La garantie de l'urne vaut sous le nul « issues indépendantes des traits » ; si les traits se mesurent au moment de
  l'exécution, l'heure fuit dans les traits (limite (a) de la note). En exécution réelle, c'est le noyau qui impose
  l'ordre (appel instance par instance, ou vérification par horodatages) : non codé ici.
- Le critère des filles (nul augmenté de v0) ne couvre pas « parent + loi aveugle quelconque », ni sans doute « parent
  incliné par des biais aveugles » : à repenser (nul des filles v2) avant toute génération de filles.
- Coût de l'urne : environ 5,5 nats à 200 tirages (K = 3) ; les petits effets perdent presque toute leur puissance.
- Règle des graines : SHA-256 (bibliothèque standard), écart à R9 déjà écrit pour v0 ; la graine maîtresse de
  l'expérience est tirée au scellement par `numpy.random.SeedSequence().entropy`.
