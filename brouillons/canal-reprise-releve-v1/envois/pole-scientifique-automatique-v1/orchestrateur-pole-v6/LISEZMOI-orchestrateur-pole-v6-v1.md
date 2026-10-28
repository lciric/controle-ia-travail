# Orchestrateur du pôle, version 0.6.0 — premier lancement réel préparé sans dépense — LISEZMOI v1

Lignée conv-audit (instance du 27 octobre 2026, servie par Fable 5.1 pour cette version ; v3 à v5 écrites sous Opus 5.5),
écrit à partir de 13:37 UTC (heure lue sur `date -u` : 13:36:57). Exploratoire (R-522, R-546). Copie de
`orchestrateur-pole-v5` (jamais écrasé, R12), plus les trois pièces annoncées par le devis du premier lancement réel
(`../premier-lancement-reel/devis-premier-lancement-reel-v1.md`, `aabfc2e6…`), une correction tirée de la contre-lecture
d'aptitude (`../premier-lancement-reel/contre-lecture-aptitude-v1/`, `d4c6ef64…`, faille C4) et deux contraintes de Lazar
du 27 octobre (14:17, heure de Paris). **Rien n'est dépensé** : aucune vraie clé, aucun réseau, aucun appel de modèle.

## Verdict

- **Monde tenu par le noyau** (`pole/monde_noyau.py`, `--monde-noyau`) : après le gel, le noyau tire les issues du monde
  caché aux instances du plan, dans l'ordre imposé, et les dépose dans `mesures.json` ; l'agent les range par un code
  rejouable ; le noyau compare les issues déclarées aux issues déposées **avant** d'appeler le vérificateur (toute
  différence : « rejetee (test change) »). Le monde (vérités, lois) n'est jamais écrit dans un dossier d'agent. Monde
  tautologique par construction (une fiche vraie a pour monde sa propre loi) : il éprouve la plomberie, pas le domaine.
- **Dépôt unique par engagement** : une fiche rejouée (indécise, hors budget) reçoit le même ordre secret et les mêmes
  issues qu'à son premier gel, pour toute la course ; sans cela, un agent qui voit des issues défavorables pourrait planter
  pour obtenir un tirage neuf (censure stratégique, faille C4 de la contre-lecture).
- **Relais de clé réel** (`pole/relais_reel.py`) : serveur local (boucle locale seulement), autre processus, qui lit la clé
  dans **son seul** environnement et l'en efface, n'accepte que le jeton factice du pôle, le remplace par la clé, relaie
  vers l'amont (réponses en flux morceau par morceau), lit l'usage et tient un **plafond de dépense indépendant** de
  l'orchestrateur, avec **réservation par appel** (des appels simultanés ne franchissent pas le plafond ensemble : défaut
  vu par la répétition générale, corrigé). Journal sans clé ni corps. Barème officiel lu le 27 octobre 2026 ; un modèle
  inconnu est compté au tarif le plus haut.
- **Répétition générale** (`demonstrations/repetition_generale_v6.py`) : une course entière par l'adaptateur réel, le
  relais réel, un amont factice et un faux moteur (`essais/faux_sdk/`) qui imite le kit d'agents sans appel de modèle :
  sept vérifications (course au bout, témoins, mesures déposées et conformes, un appel servi par agent avec la clé
  ajoutée, garde des outils exercée, clé absente partout, contre-essai « clé dans l'environnement de l'orchestrateur »
  refusé). Sur une génération : **tout tenu** en 1,3 s.
- **Seulement Opus 5.5 et Fable 5.1** pour un lancement réel (`adaptateurs.MODELES_REELS_PERMIS`, décision de Lazar) :
  tout autre nom de modèle est refusé avant tout import du kit.
- **Ligne de commande complète** : `--juge`, `--nul-filles`, `--taille-plan`, `--taille-plan-filles`,
  `--tirage-recombinaison`, `--politique-redite`, `--noyau-secret`, `--monde-noyau [FICHIER]`, `--p-vraie-noyau` ; le moteur
  réel en sélection par pari **exige** `--monde-noyau`.
- **154 essais passent** (130 de v5 et 24 nouveaux : `essais/test_v6_monde_noyau.py`,
  `essais/test_v6_relais_reel.py`, `essais/test_v6_repetition.py`), cas sains et artefacts (R5).

## Ce qui change par rapport à `orchestrateur-pole-v5`

| fichier | changement |
|---|---|
| `pole/monde_noyau.py` (nouveau) | `MondeNoyau` (vérités déclarées + tirage par graine, loi de la fiche si vraie, marginale aveugle sinon ; graine des tirages liée à la graine du noyau), `charger_monde_noyau`, `issues_conformes` |
| `pole/cycle.py` | `Generation(…, monde_noyau=, depots=)` ; dépôt de `mesures.json` au gel ; comparaison des issues déclarées avant le vérificateur ; dépôt unique par engagement (ordre et mesures) ; consigne « monde tenu par le noyau » |
| `pole/simulation.py` | l'expérimentateur simulé range les mesures déposées quand `mesures.json` existe (sinon, il mesure comme avant) |
| `pole/pole.py` | `executer_pole(…, monde_noyau=)`, dépôts partagés entre générations ; nouvelles options de ligne de commande ; moteur réel en pari sans `--monde-noyau` refusé ; modèles réels vérifiés |
| `pole/adaptateurs.py` | `MODELES_REELS_PERMIS`, `ModeleNonPermis`, `verifier_modele_reel` (avant l'import du kit) |
| `pole/relais_reel.py` (nouveau) | le relais réel : `Compteur` (plafond, réserve par appel), `LecteurUsageFlux`, `cout_usd`, barème, `servir`, ligne de commande ; lançable par `python -I pole/relais_reel.py …` |
| `essais/faux_sdk/` (nouveau) | `claude_agent_sdk.py` (faux moteur : contrôle des options, rôle joué par le simulateur, crochets exercés sur cinq appels dont trois interdits, appel réel au relais), `amont_factice.py` |
| `demonstrations/repetition_generale_v6.py` (nouveau) | la répétition générale et son rapport scellé |
| `essais/test_v6_*.py` (nouveaux) | cas sains et artefacts des trois pièces, du dépôt unique et des modèles permis |
| `pole/__init__.py` | version 0.6.0 |

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python      # numpy ≥ 1.25 visible, claude_agent_sdk invisible
sha256sum -c EMPREINTES-orchestrateur-pole-v6-v1.txt
$PY -I -B -m unittest                      # 154 essais, environ 3 minutes
$PY -I -B demonstrations/repetition_generale_v6.py DOSSIER_NEUF --generations 2 --horodatage "$(date -u +%H:%M) UTC"
# simulation avec le monde du noyau (processeur, sans dépense) :
$PY -I -B pole --selection pari --monde-noyau exemples/monde-pari-demo-v1.json --noyau-secret \
    --population exemples/population-pari-demo-4traits-v1.json --temoins exemples/temoins-pari-demo-4traits-v1.json \
    --generations 2 --budget-usd 20 --sortie DOSSIER_NEUF --horodatage "$(date -u +%H:%M) UTC"
```

## Premier lancement réel (option a) : ce que fait session-depot, sur le mot de Lazar

1. Un Python avec `claude_agent_sdk` et numpy ≥ 1.25 ; ce dossier vérifié par ses empreintes.
2. Le relais, dans un terminal à part, avec la clé dans **son seul** environnement :
   `ANTHROPIC_API_KEY=… python -I pole/relais_reel.py --port 8787 --plafond-usd 20 --journal RELAIS.jsonl`
   (la variable est effacée de l'environnement du relais après lecture ; rien d'autre ne la porte).
3. L'orchestrateur, dans un environnement **sans aucun nom de variable de clé** (il refuse de partir sinon) :
   `python -I pole --moteur claude-sdk --confirmer-moteur-reel --url-relais http://127.0.0.1:8787 --selection pari
   --monde-noyau exemples/monde-pari-demo-v1.json --noyau-secret --population … --temoins … --generations 2
   --budget-usd 20 --modele-experimentateur claude-opus-5-5 --modele-verificateur claude-fable-5-1
   --modele-recombinaison claude-opus-5-5 --modele-synthese claude-opus-5-5 --sortie … --horodatage "$(date -u +%H:%M) UTC"`
4. Lecture : `bilan.json`, `journal/`, `noyau/` (graines écrites après coup), `RELAIS.jsonl` (coût réel par appel).

## Limites connues (contre-lecture d'aptitude, 27 octobre)

- Le monde du noyau est tautologique ; le domaine du programme demande un `MondeProgramme` (banque d'épisodes en cache,
  puis moniteurs), un nul **informé** (prédiction calibrée du moniteur courant), une configuration sans urne pour une
  banque figée, un rôle **proposeur**, et la réécriture des hypothèses du programme en lois par instance : v7.
- Deux canaux de texte entre agents restent ouverts (dossier copié au vérificateur ; leçons en prose servies à la
  génération suivante) ; la lignée du vérificateur n'est garantie que par deux noms de modèles différents (avec la
  contrainte Opus 5.5 / Fable 5.1, c'est bien deux modèles) ; l'aptitude est constante en mode pari : v7.
- Le relais ne garantit pas qu'un agent ne puisse pas lui parler depuis son bac à sable avec le jeton factice (rôle du
  bac à sable réseau du kit et de la garde des outils) : il borne alors la dépense, pas l'usage.
- Le faux moteur imite l'interface du kit telle que l'adaptateur l'utilise ; une différence d'interface avec le vrai kit
  n'apparaîtra qu'au premier lancement réel (c'est son objet).
- Sous `noyau_secret`, la graine de la génération d'un premier gel est réutilisée pour le rejeu d'une fiche aux
  générations suivantes ; elle est déjà écrite sous `noyau/` à ce moment-là (hors des dossiers d'agents).
