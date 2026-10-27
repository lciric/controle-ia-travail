# Orchestrateur du pôle, version 0.3.0 — le cycle juge avec le juge v1 et le nul des filles v2 — LISEZMOI v1

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 12:22 UTC (heure lue sur `date -u`). Exploratoire
(R-522) ; préenregistrement levé pour la partie exploratoire (mot de Lazar du 27 octobre, 12:02 heure de Paris).
Copie de `orchestrateur-pole-v2` (jamais écrasé, R12), plus ce qui suit.

## Verdict

- En sélection par pari, le cycle du pôle juge désormais par défaut avec **le juge v1** (ordre d'exécution secret tiré
  par le noyau après le gel, urne dans 𝓛 ; expérience 1 : socle adopté) et **le nul des filles v2** (membres ajustés,
  lecture aux instants fixés ; expérience 2 : adopté). L'ordre est **imposé à l'expérimentateur** : le noyau l'écrit dans
  `ordre-execution.json` après le gel et le recalcule à l'évaluation ; une déclaration d'ordre naturel ou une empreinte
  d'ordre fausse est rejetée (« rejetee (test change) »).
- La recombinaison tire par défaut **par strates de domaines** (décision R-527), avec abstention ; le noyau corrigé de
  v0 reste disponible (`tirage_recombinaison="noyau_corrige"`).
- **120 essais passent** (les 111 de v2, inchangés, qui tournent maintenant sous les nouveaux défauts, et 9 nouveaux).
- La génération 1 (recombinaison) peut tourner en simulation ; démonstration de bout en bout : `demonstrations/`.

## Ce qui change par rapport à `orchestrateur-pole-v2`

| fichier | changement |
|---|---|
| `pole/nul_filles_v2.py` (nouveau) | le module validé par l'expérience 2 (`../nul-des-filles-v2/nul_filles_v2.py`, `10909b3f…`), imports relatifs seulement ; numpy, importé seulement pour les filles |
| `pole/cycle.py` | `ConfigGeneration` : `juge` (« v1 » par défaut, « v0 »), `nul_filles` (« v2 » par défaut, « v2_souple », « v0 »), `instants_filles` (8) ; `preparer_engagement` selon le juge et le nul ; graine du noyau par génération (jamais écrite dans un dossier d'agent) ; `ordre-execution.json` ; évaluation par `evaluer` (sans parents) ou `evaluer_v2` (filles), avec la graine du noyau ; `instants_reguliers` |
| `pole/selection_pari.py` | `tirer_frais_selon_ordre` : ce que fait un expérimentateur qui suit l'ordre imposé |
| `pole/recombinaison.py` | `tirage_stratifie` (R-527) et `_fusionner` (étage commun aux deux tirages) ; `recombiner(…, tirage=…)` |
| `pole/simulation.py` | l'expérimentateur simulé suit `ordre-execution.json` et recopie plan et empreinte d'ordre ; l'agent de recombinaison simulé peut proposer des filles « triviales » (`p_fille_triviale`) que le monde suit exactement (pire cas), notées hors de la vue de l'orchestrateur |
| `pole/__init__.py` | version 0.3.0 |
| `essais/test_cycle_v3.py` (nouveau) | 9 essais : ordre imposé puis recalculé (cas sain) ; ordre ignoré et empreinte fausse rejetés (artefacts) ; juge v0 en ordre naturel ; engagement d'une fille sous v2, v0, souple ; configurations refusées ; « parent + loi aveugle » éliminée sous v2 ; tirage stratifié (tour des strates, abstention, paires déjà fusionnées) |
| `demonstrations/demo_cycle_v3.py` (nouveau) | le pôle complet en simulation : v3, v3 avec le nul de v0, v0 ; filles triviales |
| `pole/cycle.py` (suite) | `tirage_recombinaison` (« stratifie » par défaut) |

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python      # numpy ≥ 1.25 visible, claude_agent_sdk invisible
sha256sum -c EMPREINTES-orchestrateur-pole-v3-v1.txt
$PY -I -B -m unittest                      # 120 essais, environ 2 minutes
$PY -I -B demonstrations/demo_cycle_v3.py DOSSIER_NEUF --courses 20 --generations 4 --p-triviale 0.4
```

## Limites connues

- La graine du noyau dérive de la graine du pôle : en simulation seulement. En exécution réelle, le noyau doit la tenir
  hors de toute vue d'agent (non codé).
- Un expérimentateur qui exécute dans un autre ordre mais **déclare** l'ordre imposé et recopie son empreinte n'est pas
  détecté par le noyau (limite CJ1-05) : c'est le vérificateur, qui rejoue le code, et l'imposition réelle de l'ordre par
  le noyau qui doivent le prendre.
- Tirage stratifié : la strate est le premier domaine déclaré de chaque fiche (« domaine estimé ») ; la marche « à la
  Swanson » par étiquette rare (meilleure mesurée aux ponts plantés, non retenue par la règle) n'est pas portée.
- La mémoire du cycle est encore celle de v0 (redite par le texte, leçons écrites) ; la signature brute, l'héritage de
  la preuve et les marchepieds (essais de la mémoire, pistes 1 à 3) n'y sont pas encore portés.
- Option stricte du nul des filles (produit des parents au nul, décision n° 1 de Lazar, défaut au 29 octobre) : dans un
  monde à deux traits, elle coûte environ 10 points de puissance sur une fille « loi entièrement neuve » (0,88 à 0,91
  contre 0,92 à 0,98 en souple et 1,0 sous l'ancien nul, 100 répétitions, essai déclaré dans le n° 105) ; rien dès 4 traits.
