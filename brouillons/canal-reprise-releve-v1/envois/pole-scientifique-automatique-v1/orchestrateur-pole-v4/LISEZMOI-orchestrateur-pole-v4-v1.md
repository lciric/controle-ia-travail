# Orchestrateur du pôle, version 0.4.0 — la mémoire dans le cycle, filles mieux éprouvées — LISEZMOI v1

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 12:48 UTC (heure lue sur `date -u`). Exploratoire
(R-522 ; préenregistrement levé pour l'exploratoire, R-546). Copie de `orchestrateur-pole-v3` (jamais écrasé, R12),
plus ce qui suit, sur les « go » de Lazar de 13:32 heure de Paris (plus de tirages et plus de traits pour les filles ;
la mémoire dans le cycle : empreinte de prédiction, héritage de la preuve, marchepieds).

## Verdict

- **Mémoire prédictive en sélection par pari** : identité d'une hypothèse = signature brute (loi engagée sur une sonde
  fixe de 256 instances, jamais montrée aux agents ; même classe si la divergence moyenne ≤ 0,30 nat, seuil de la piste
  1) ; **héritage de la preuve** (une redite d'une éliminée repart du log W cumulé de sa classe ; promue si cumul + log W
  ≥ log 1/α ; valide : produit d'e-valeurs) ; redite d'une survivante refusée ; une épreuve par classe et par
  génération ; politiques « refus » et « rien » gardées comme bras de contrôle.
- **Marchepieds** dans la recombinaison (`tirage_recombinaison="stratifie_marchepieds"`) : la moitié des paires bâtie sur
  les filles survivantes, de la plus forte preuve à la plus faible ; le reste par strates.
- **Filles éprouvées sur 300 tirages par défaut** (`taille_plan_filles`), 500 dans les démonstrations ; population de
  démonstration à 4 traits (`exemples/*-4traits-v1.json`, générée par `exemples/generer_demo_4traits_v1.py`).
- **127 essais passent** (120 de v3 et 7 nouveaux : `essais/test_memoire_v4.py`).

## Ce qui change par rapport à `orchestrateur-pole-v3`

| fichier | changement |
|---|---|
| `pole/memoire.py` | sonde, signature, `chercher_classe`, `heritage`, `_garde_signature`, `nouvelle_generation`, classes indexées, politiques de redite |
| `pole/cycle.py` | héritage appliqué à la promotion (`issue["pari"]["heritage"]`) ; `taille_plan_filles` (300) ; `politique_redite` (« heritage ») ; tirage « stratifie_marchepieds » permis |
| `pole/pole.py` | mémoire construite avec la graine du pôle et la politique ; `nouvelle_generation` ; une fiche réessayée repasse la garde prédictive |
| `pole/recombinaison.py` | `_paires_valides`, `tirage_marchepieds`, `tirage="stratifie_marchepieds"` (preuve tirée de la mémoire) |
| `pole/simulation.py` | énoncés de filles uniques (identifiants des parents) ; loi d'une fille à la dimension de ses parents ; monde à lignées fécondes (`fecondite_lignees`) |
| `pole/__init__.py` | version 0.4.0 |
| `essais/test_memoire_v4.py` (nouveau) | signature et classes ; héritage, une épreuve par génération, survivante refusée ; politiques ; témoins hors classes ; héritage dans le cycle ; marchepieds |
| `essais/test_cycle_v3.py` | taille des plans de filles fixée à 80 dans les essais copiés de v3 |
| `demonstrations/demo_cycle_v4.py` (nouveau) | A : puissance des filles (traits × tirages) ; B : marchepieds (monde fécond, monde plat) ; C : redites (héritage, refus, rien) |
| `exemples/` | population et témoins à 4 traits, et leur générateur |

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python      # numpy ≥ 1.25 visible, claude_agent_sdk invisible
sha256sum -c EMPREINTES-orchestrateur-pole-v4-v1.txt
$PY -I -B -m unittest                      # 127 essais, environ 2 minutes
$PY -I -B demonstrations/demo_cycle_v4.py DOSSIER_NEUF --experience A      # puis B, puis C --generations 6
```

## Limites connues

- Le seuil de la signature (0,30 nat) vient de lois à 2 traits ; à 4 traits, les lois au hasard sont plus éloignées :
  moins de fausses fusions, plus de redites légères manquées (non mesuré).
- Les marchepieds ne valent que si les lignées sont fécondes (piste 3) : c'est une hypothèse sur le monde, que la
  démonstration B pose par construction ; le monde réel reste à mesurer (rétrodiction arXiv).
- Les agents simulés ne lisent pas la mémoire : seul le mécanisme (garde, héritage, choix des paires) est éprouvé.
- Héritage : les épreuves d'une classe se multiplient ; une vraie hypothèse mal engagée au premier essai part de bas
  (piste 2, variante B : + 0,50 vraie par course sur le refus, mais − 0,165 contre « rien »).
