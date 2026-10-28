# Démonstration de bout en bout du pari apparié borné — sorties de la première course (code v7, version 27)

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), après le relevé `date -u` de 00:30:30 UTC le
28 octobre. Commande (depuis `../../orchestrateur-pole-v7/`) :
`python -I -B demonstrations/demo_pari_apparie_v7.py DOSSIER --nul 200` (graine 20261028, 4 générations × 40 unités,
α = 0,05, τ = 0,05, 6 contrastes au hasard par génération). Exploratoire (R-546) ; banque synthétique ; zéro dépense.

- `lecture-pari-apparie.json` : L1 / L2 / L3, artefacts R5, nul × 200, réglages, description publique de la banque.
- `course.json` : journal par génération (tranche, nouvelles fiches, α_g, m_c, parties, « sans partie », abandons, promues),
  état final (log e, seuils, gelées, abandons, journal des parties, α engagé).
- `banque.json` : non versée (1,6 Mo, reproductible par la graine) ; son empreinte : `banque.json.sha256-seule.txt`.

Ce que ça dit : voir `../../orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v27.md` (verdict : L1 tenue, dents jusqu'à
l'écart 0,5 en deux générations, G1 promue en génération 3 par e-BH pondéré, aucune promotion sur 200 banques nulles).
