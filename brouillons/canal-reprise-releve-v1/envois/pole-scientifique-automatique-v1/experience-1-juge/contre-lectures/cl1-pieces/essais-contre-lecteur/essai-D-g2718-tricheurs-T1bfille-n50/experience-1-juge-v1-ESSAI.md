# Expérience 1 du pôle — juge v1 : ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée (socle : ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée ; critère des filles : ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée)

**ESSAI — non décisif** (moins de répétitions ou familles partielles ; graine d'essai).

Horodatage : 2026-10-27T09:08:39Z (argument --horodatage (date -u dans la commande de lancement)). Graine maîtresse 2718 ; 50 répétitions par ligne ; 200 tirages frais par répétition ; α = 0.05 (seuil de richesse 20) ; lecture continue (promotion dès que W_t ≥ 1/α, inégalité de Ville).
Simulation seulement : ces taux valent pour les mondes synthétiques décrits, rien au-delà.

- **Global** — ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée. Contrôles fatals : 9, échecs : ['tricheur-parent_et_loi_aveugle', 'T1b-fille'], taux max 0.36 (tricheur-parent_et_loi_aveugle) ; artefacts requis : 2, non vus : aucun ; puissance décisive : {'puissance-fille-neuve': 0.98} (insuffisantes : aucune).
- **Socle (fiches sans parents)** — ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée. Contrôles fatals : 0, échecs : aucun, taux max None (None) ; artefacts requis : 0, non vus : aucun ; puissance décisive : {} (insuffisantes : aucune).
- **Critère des filles** — ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée. Contrôles fatals : 9, échecs : ['tricheur-parent_et_loi_aveugle', 'T1b-fille'], taux max 0.36 (tricheur-parent_et_loi_aveugle) ; artefacts requis : 2, non vus : aucun ; puissance décisive : {'puissance-fille-neuve': 0.98} (insuffisantes : aucune).
- Perte de puissance sur la fille neuve (v0 − v1) : 0.020000000000000018 (prédite ≤ 0.05).
- Ce qui a cédé : ['tricheur-parent_et_loi_aveugle', 'T1b-fille'].

| partie | rôle | contrôle | juge | promotions | taux | borne haute 95 % | log W max observé |
|---|---|---|---|---|---|---|---|
| filles | fatal | T1b-fille | v1 | 5/50 | 0.1000 | 0.1915 | 8.256 |
| filles | fatal | tricheur-adimensionnement | v1 | 0/50 | 0.0000 | 0.0513 | 0.000 |
| filles | fatal | tricheur-copie_renommee | v1 | 0/50 | 0.0000 | 0.0513 | 0.000 |
| filles | fatal | tricheur-enveloppe_aveugle | v1 | 0/50 | 0.0000 | 0.0513 | 0.102 |
| filles | fatal | tricheur-fille_constante | v1 | 0/50 | 0.0000 | 0.0513 | -0.622 |
| filles | fatal | tricheur-forme | v1 | 0/50 | 0.0000 | 0.0513 | 0.000 |
| filles | fatal | tricheur-jargon_rare | v1 | 0/50 | 0.0000 | 0.0513 | 0.000 |
| filles | fatal | tricheur-parent_et_loi_aveugle | v1 | 18/50 | 0.3600 | 0.4762 | 22.798 |
| filles | fatal | tricheur-pari_couvert | v1 | 0/50 | 0.0000 | 0.0513 | -0.582 |
| filles | puissance_decisive | puissance-fille-neuve | v1 | 49/50 | 0.9800 | 0.9955 | 125.932 |
| filles | artefact_requis | artefact-fille-sans-parents-dans-le-nul-enveloppe_aveugle | v1 | 30/50 | 0.6000 | 0.7060 | 114.650 |
| filles | artefact_requis | artefact-fille-sans-parents-dans-le-nul-forme | v1 | 15/50 | 0.3000 | 0.4146 | 111.087 |
| filles | descriptif | T1b-fille | v0 | 22/50 | 0.4400 | 0.5556 | 11.770 |
| filles | descriptif | puissance-fille-neuve | v0 | 50/50 | 1.0000 | 1.0000 | 107.520 |
| filles | descriptif | tricheur-parent_et_loi_aveugle | v0 | 23/50 | 0.4600 | 0.5750 | 20.920 |
