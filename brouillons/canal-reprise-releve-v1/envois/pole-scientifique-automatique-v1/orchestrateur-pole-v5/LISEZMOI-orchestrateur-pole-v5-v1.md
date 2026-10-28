# Orchestrateur du pôle, version 0.5.0 — seuil de signature par fiche, graine du noyau secrète, vivier de 60 fiches — LISEZMOI v1

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 13:05 UTC (heure lue sur `date -u`). Exploratoire
(R-522, R-546). Copie de `orchestrateur-pole-v4` (jamais écrasé, R12), plus ce qui suit, sur les « go » de Lazar de
13:52 heure de Paris.

## Verdict

- **Seuil de la signature à 5 % de fausses fusions par fiche** : une nouvelle fiche est comparée aux m signatures de
  l'archive ; le seuil est le quantile d'ordre 0,05 / m de la divergence entre deux lois tirées au hasard (référence :
  softmax de force 1,5, 2 000 paires sur la sonde du pôle), plafonné à 0,30 nat. Une copie exacte reste reconnue.
- **Graine du noyau secrète pour une exécution réelle** (`noyau_secret=True`) : tirée par `secrets` à chaque génération,
  tenue en mémoire, jamais écrite dans un dossier d'agent, écrite après toutes les évaluations sous `noyau/`. En simulation,
  le défaut reste la graine dérivée de celle du pôle (reproductible).
- **Vivier de démonstration de 60 fiches** à 4 traits (`exemples/population-pari-vivier60-4traits-v1.json`, vérités
  `exemples/monde-pari-vivier60-v1.json`, générés par `exemples/generer_vivier_v1.py`).
- **130 essais passent** (127 de v4 et 3 nouveaux : `essais/test_v5.py`).

## Ce qui change par rapport à `orchestrateur-pole-v4`

| fichier | changement |
|---|---|
| `pole/memoire.py` | `_reference`, `seuil_effectif` ; `chercher_classe` compare au seuil effectif |
| `pole/cycle.py` | `noyau_secret` (faux par défaut) ; graine par `secrets` ; `noyau/graine-noyau-generation-XX.json` écrit après les évaluations |
| `pole/__init__.py` | version 0.5.0 |
| `essais/test_v5.py` (nouveau) | le seuil se resserre quand l'archive grandit ; fausses fusions par fiche tenues sur lois neuves ; graine secrète (absente des dossiers d'agent, écrite après, neuve à chaque génération) |
| `demonstrations/demo_cycle_v5.py` (nouveau, remplace les démonstrations copiées de v3 et v4) | A, B sur le vivier (six paires par génération, cinq générations), C avec un bras « sans mémoire » ; option `--bras` |
| `exemples/` | vivier de 60 fiches et son générateur |

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python      # numpy ≥ 1.25 visible, claude_agent_sdk invisible
sha256sum -c EMPREINTES-orchestrateur-pole-v5-v1.txt
$PY -I -B -m unittest                      # 130 essais, environ 2 minutes 30
$PY -I -B demonstrations/demo_cycle_v5.py DOSSIER_NEUF --experience A     # B (environ 30 min), C --generations 6
```

## Limites connues

- La loi de référence du seuil (softmax de force 1,5) est celle du monde simulé ; pour de vrais agents, il faudra la
  remplacer par la distribution des divergences entre fiches réellement distinctes de l'archive.
- La graine secrète protège l'ordre d'exécution si et seulement si les agents n'ont accès ni au processus de
  l'orchestrateur ni à la racine du pôle (bac à sable du moteur réel : à vérifier au premier lancement réel).
- Le reste : voir les LISEZMOI de v3 et v4.
