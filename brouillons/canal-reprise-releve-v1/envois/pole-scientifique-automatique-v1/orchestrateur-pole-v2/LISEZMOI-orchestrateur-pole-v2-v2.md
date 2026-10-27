# Orchestrateur du pôle, version 0.2.0 — juge v1 et expérience 1 — LISEZMOI v2

Lignée conv-audit (instance nouvelle), écrit le 27 octobre 2026 à partir de 10:52 UTC (heure lue sur `date -u`).
**Remplace la v1** (`LISEZMOI-orchestrateur-pole-v2-v1.md`, `dbd2811b…`, gardée sans modification) : même contenu, plus
la section « Corrections après la contre-lecture cl1 », la section « Comment lire le rapport » et le compte d'essais (111).
Exploratoire (R-522). **Mot de Lazar du 27 octobre, 12:02 heure de Paris** : « pas besoin de faire de préenregistrement
je lève cette règle pour toute la partie exploratoire jusqu'à avoir obtenu un système qui marche ». L'expérience 1 se
lance donc sans texte scellé (le brouillon `experience-1-juge/preenregistrement-experience-1-juge-v1.md`, `1af7df8c…`,
reste tel quel, sans suite) ; sa lecture est celle que le code fige (`juger_v1`), poussée avant l'exécution.

## Verdict

- Le juge v1 de la note `experience-1-juge/conception-experience-1-juge-v1.md` (`560f4a4c…`) est codé : ordre
  d'exécution secret tiré par le noyau après le gel, membre « urne » dans 𝓛, loi « sans remise », garde du plan
  d'exécution ; avec les contrôles de l'expérience 1. **111 essais passent** (83 de v0, inchangés, et 28 nouveaux).
- Contre-lecture cl1 (sous-agent neuf, Fable 5.1) : « scellable après corrections », aucun bloquant ; ses quatre
  majeurs et treize mineurs sont traités (section dédiée) ; **aucune ligne calculée ne change** (essai de fumée 3, même
  graine que l'essai 2 : promotions et log W max identiques sur les 70 lignes).
- Essais de fumée et exploration (déclarés, non opposables) : le socle tient ; le critère des filles a un trou antérieur
  à v1 (« parent + loi aveugle »), d'où un huitième tricheur et la lecture en deux parties (socle, filles).

## Ce qui change par rapport à `orchestrateur-v0` (jamais écrasé, R12)

| fichier | changement |
|---|---|
| `pole/selection_pari.py` | `BIBLIOTHEQUE_STANDARD_V1` (v0 + urne) ; membre `urne` ; lois `calendrier`, `deterministe`, `sans_remise` ; `construire_engagement(…, plan_execution=…)` ; `ordre_execution` ; `tirer_frais(…, graine_noyau=…)` ; `verifier_plan_execution` et `evaluer(…, graine_noyau=…)` ; exception `PlanExecutionNonConforme` |
| `pole/controles_pari_v1.py` (nouveau) | les 70 lignes de l'expérience 1 (`ROSTER_V1`), trois juges, suivi par répétition, lecture gelée `juger_v1` avec conformité et déclencheurs de l'audit de symétrie |
| `pole/experience_juge_v1.py` (nouveau) | écriture scellée du manifeste (avant tout calcul), du rapport JSON et du rapport Markdown |
| `pole/pole.py` | options `--experience-juge-v1`, `--graine-maitresse` (exigée), `--repetitions`, `--essai`, `--familles` |
| `pole/outils.py` | une phrase du manifeste corrigée (CJ1-13) |
| `pole/__init__.py` | version 0.2.0 |
| `essais/test_juge_v1.py` (nouveau) | 28 essais (voir la v1, plus ceux des corrections cl1) |

Le cycle du pôle reste en ordre naturel et sur la bibliothèque de v0 tant que le juge v1 n'est pas adopté.

## Lancer (depuis ce dossier)

Utiliser un Python où `claude_agent_sdk` est **invisible** (ici `/opt/venv-essaim-sim-v1/bin/python`).

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v2-v1.txt     # d'abord : les essais créent essais/_tmp/ (hors empreintes)
$PY -I -B -m unittest                                    # 111 essais, environ 105 secondes
$PY -I -B pole --experience-juge-v1 --graine-maitresse G --sortie DOSSIER_NEUF --horodatage "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
```

L'expérience décisive refuse : un nombre de répétitions autre que 1 000, une exécution partielle, les graines déjà
utilisées (20261026, 777, 4242, 31337, 2718, la graine de 128 bits du contre-lecteur, 20261027, 20261028), un dossier de
sortie non vide ; elle s'arrête si une évaluation n'a pas tourné sous le plan du juge de sa ligne. Durée : environ 15
minutes sur un cœur.

## Corrections après la contre-lecture cl1

Rapport : `experience-1-juge/contre-lectures/rapport-contre-lecture-experience-1-juge-v1-cl1.md` (`25a9b63c…`).

- **CJ1-02** : `ROSTER_V1`, les 70 couples (contrôle, juge), identiques à l'annexe A du rapport ; `juger_v1`, en
  exécution décisive, ne prononce aucune issue (« EXÉCUTION INCOMPLÈTE OU NON CONFORME ») si un couple manque, est en
  trop ou en double, ou si une ligne n'a pas 1 000 répétitions ; essayé sur un cas sain et quatre artefacts.
- **CJ1-03** : chaque ligne consigne le plan **observé** dans les évaluations (`plan_execution_observe`) et le nombre
  d'empreintes d'ordre distinctes ; une évaluation sous un autre plan que celui du juge arrête le contrôle
  (`PlanObserveNonConforme`) ; essayé sur un cas sain et un artefact.
- **CJ1-04** : chaque ligne consigne ses promotions répétition par répétition (`promotions_par_repetition`) ; la lecture
  compte, par ligne de puissance appariée, les répétitions où v0 et v1 diffèrent.
- **Déclencheurs de l'audit de symétrie** évalués mécaniquement et écrits au rapport (CJ1-03, CJ1-04, CJ1-07, CJ1-09).
- **CJ1-05** : la limite de la garde du plan (une empreinte d'ordre recopiée est acceptée) est écrite et essayée comme
  limite documentée, pas comme refus.
- **CJ1-11, CJ1-13, CJ1-16** : chaîne du critère T9 (10⁻⁹) ; exactement 1 000 répétitions hors essai ; graines refusées
  étendues ; phrase du manifeste corrigée.
- Les autres constats portaient sur le texte du préenregistrement, devenu sans objet (mot de Lazar) ; ceux qui gardent
  un sens pour lire le rapport sont repris ci-dessous.

## Comment lire le rapport

- **Issue** : `juger_v1` applique la règle de la note (adopté si tous les contrôles fatals ≤ α, tous les artefacts requis
  > α, chaque puissance décisive ≥ 0,90 ; non adopté si un fatal cède ou une puissance manque ; non concluant sinon),
  sur le socle, sur le critère des filles, et globalement (adopté si et seulement si les deux parties le sont). Un
  rapport qui n'a pas exactement les 70 couples de `ROSTER_V1` à 1 000 répétitions chacun ne reçoit aucune issue.
- **Socle** (fiches sans parents) : 12 des 18 contrôles fatals sont à 0, ou presque, par construction (les six lois
  « composition », dominées par l'urne ; les six « calendrier » sous v1, que l'ordre secret réduit à une loi aveugle au
  hasard) ; les dents statistiques du socle sont T1a (trois lignes), T6 et T3 net faux. « Toutes les fatales du socle à
  0 » est probable (le contre-lecteur l'estime entre un tiers et la moitié) : déclencheur d'un audit léger (répétitions et
  log W max finis), pas une réserve. Un « socle adopté » ne licencie que la génération 0, sans recombinaison.
- **Filles** : attendu « non adopté » (trou « parent + loi aveugle », T1b-fille), à refaire avec le nul des filles v2.
- **Appariement v0/v1** : par scénario (loi, instances) ; les tirages du monde diffèrent entre juges (ils dérivent de
  l'empreinte de l'engagement) : appariement partiel ; le rapport compte les répétitions où v0 et v1 diffèrent.
- **T9** garde la règle de v0 : W seule sur 200 instances, sans part de calibrage ni marge 2δ₀, et log W max ≤ 10⁻⁹.
- **Ce que l'expérience valide** : le juge, pas le dispositif réel qui impose l'ordre ; la garde du plan ne protège que
  contre un étiquetage non conforme (CJ1-05).
- **Constantes** (dans `parametres` du rapport) : λ = 0,5 (T1b-fille, « parent et loi aveugle ») ; λ = 0,3 (puissance avec
  dérive) ; amplitude 1,5 des logits de la sinusoïde ; q de « parent et loi aveugle » tirée de Dirichlet(1, 1, 1) (q fixée
  à l'exploration de conception) ; marginale d'entraînement des filles sur 100 instances (T1b-fille : instants tirés sur
  l'horizon).

## Essais de fumée et exploration (déclarés ; non opposables)

- Essais 1 et 2 (graine 777, 20 répétitions, toutes familles) et exploration (200 répétitions) : voir la v1.
- Essai 3 (graine 777, 20 répétitions, code corrigé) : lignes identiques à l'essai 2 ; déclencheur R4 « toutes les
  fatales du socle à 0 » levé (attendu probable, CJ1-07).
- Essais du contre-lecteur cl1 (déclarés par lui, CJ1-16) : graines 4242 (deux fois, rapports identiques), 31337, 2718
  et une graine de 128 bits ; entre autres, « parent et loi aveugle » 9/20 et 18/50 sous v1, T1b-fille 0/20 et 5/50 sous
  v1, fille neuve 49/50 sous v1.

## Limites connues

- Simulation seulement ; mondes synthétiques ; K = 3, dimension 2, 200 tirages ; le monde auto-excité est presque
  absorbant (CJ1-15).
- La garantie de l'urne vaut sous le nul « issues indépendantes des traits » ; si les traits se mesurent au moment de
  l'exécution, l'heure fuit dans les traits ; en exécution réelle, c'est le noyau qui impose l'ordre : non codé ici.
- Le critère des filles (nul augmenté de v0) ne couvre pas « parent + loi aveugle » : nul des filles v2 en conception
  (`nul-des-filles-v2/conception-nul-des-filles-v2-v1.md`).
- Coût de l'urne : environ 5,5 nats à 200 tirages ; les petits effets perdent presque toute leur puissance.
- Reproductibilité bit à bit promise sur l'environnement nommé (Python 3.13.17, Linux, `/opt/venv-essaim-sim-v1`) ;
  ailleurs, seules les statistiques sont attendues égales (CJ1-12).
