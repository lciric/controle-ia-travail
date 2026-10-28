# Expérience 1 du pôle — juge v1 : ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée (socle : ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée ; critère des filles : ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée)

**ESSAI — non décisif** (moins de répétitions ou familles partielles ; graine d'essai).

Horodatage : 2026-10-27T08:48:59Z (argument --horodatage (date -u dans la commande de lancement)). Graine maîtresse 31337 ; 50 répétitions par ligne ; 200 tirages frais par répétition ; α = 0.05 (seuil de richesse 20) ; lecture continue (promotion dès que W_t ≥ 1/α, inégalité de Ville).
Simulation seulement : ces taux valent pour les mondes synthétiques décrits, rien au-delà.

- **Global** — ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée. Contrôles fatals : 5, échecs : aucun, taux max 0.0 (T1a-nul-marginale) ; artefacts requis : 1, non vus : aucun ; puissance décisive : {'T3-couvert-eps0.2-net-vrai': 0.96} (insuffisantes : aucune).
- **Socle (fiches sans parents)** — ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée. Contrôles fatals : 5, échecs : aucun, taux max 0.0 (T1a-nul-marginale) ; artefacts requis : 1, non vus : aucun ; puissance décisive : {'T3-couvert-eps0.2-net-vrai': 0.96} (insuffisantes : aucune).
- **Critère des filles** — ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée. Contrôles fatals : 0, échecs : aucun, taux max None (None) ; artefacts requis : 0, non vus : aucun ; puissance décisive : {} (insuffisantes : aucune).
- Perte de puissance sur la fille neuve (v0 − v1) : None (prédite ≤ 0.05).
- Ce qui a cédé : rien.

| partie | rôle | contrôle | juge | promotions | taux | borne haute 95 % | log W max observé |
|---|---|---|---|---|---|---|---|
| socle | fatal | T1a-nul-marginale | v1 | 0/50 | 0.0000 | 0.0513 | 1.783 |
| socle | fatal | T1a-nul-moyenne_glissante | v1 | 0/50 | 0.0000 | 0.0513 | 0.342 |
| socle | fatal | T1a-nul-uniforme | v1 | 0/50 | 0.0000 | 0.0513 | 0.646 |
| socle | fatal | T3-couvert-eps0.05-net-faux | v1 | 0/50 | 0.0000 | 0.0513 | -0.707 |
| socle | fatal | T3-couvert-eps0.2-net-faux | v1 | 0/50 | 0.0000 | 0.0513 | -0.506 |
| socle | puissance_decisive | T3-couvert-eps0.2-net-vrai | v1 | 48/50 | 0.9600 | 0.9867 | 37.027 |
| socle | artefact_requis | artefact-T1a-bibliotheque-uniforme-seule | v1 | 47/50 | 0.9400 | 0.9758 | 198.592 |
| socle | descriptif | T3-couvert-eps0.05-net-vrai | v0 | 46/50 | 0.9200 | 0.9636 | 12.354 |
| socle | descriptif | T3-couvert-eps0.05-net-vrai | v1 | 10/50 | 0.2000 | 0.3073 | 6.944 |
| socle | descriptif | T3-couvert-eps0.2-net-vrai | v0 | 49/50 | 0.9800 | 0.9955 | 43.912 |
