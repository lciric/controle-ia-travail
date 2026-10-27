# Expérience 1 du pôle — juge v1 : ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée (socle : ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée ; critère des filles : ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée)

**ESSAI — non décisif** (moins de répétitions ou familles partielles ; graine d'essai).

Horodatage : 2026-10-27T08:16:15Z (argument --horodatage (date -u dans la commande de lancement)). Graine maîtresse 4242 ; 20 répétitions par ligne ; 200 tirages frais par répétition ; α = 0.05 (seuil de richesse 20) ; lecture continue (promotion dès que W_t ≥ 1/α, inégalité de Ville).
Simulation seulement : ces taux valent pour les mondes synthétiques décrits, rien au-delà.

- **Global** — ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée. Contrôles fatals : 28, échecs : ['tricheur-parent_et_loi_aveugle'], taux max 0.45 (tricheur-parent_et_loi_aveugle) ; artefacts requis : 8, non vus : aucun ; puissance décisive : {'puissance-fille-neuve': 1.0, 'T3-couvert-eps0.2-net-vrai': 0.95} (insuffisantes : aucune).
- **Socle (fiches sans parents)** — ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée. Contrôles fatals : 18, échecs : aucun, taux max 0.0 (T1a-nul-marginale) ; artefacts requis : 6, non vus : aucun ; puissance décisive : {'T3-couvert-eps0.2-net-vrai': 0.95} (insuffisantes : aucune).
- **Critère des filles** — ESSAI OU EXÉCUTION PARTIELLE — aucune issue n'est prononcée. Contrôles fatals : 10, échecs : ['tricheur-parent_et_loi_aveugle'], taux max 0.45 (tricheur-parent_et_loi_aveugle) ; artefacts requis : 2, non vus : aucun ; puissance décisive : {'puissance-fille-neuve': 1.0} (insuffisantes : aucune).
- Perte de puissance sur la fille neuve (v0 − v1) : 0.0 (prédite ≤ 0.05).
- Ce qui a cédé : ['tricheur-parent_et_loi_aveugle'].

| partie | rôle | contrôle | juge | promotions | taux | borne haute 95 % | log W max observé |
|---|---|---|---|---|---|---|---|
| filles | fatal | T1b-fille | v1 | 0/20 | 0.0000 | 0.1192 | 4.976 |
| filles | fatal | T9-disjonction-partitionnee | v1 | 0/20 | 0.0000 | 0.1192 | 0.000 |
| filles | fatal | tricheur-adimensionnement | v1 | 0/20 | 0.0000 | 0.1192 | 0.000 |
| filles | fatal | tricheur-copie_renommee | v1 | 0/20 | 0.0000 | 0.1192 | 0.000 |
| filles | fatal | tricheur-enveloppe_aveugle | v1 | 0/20 | 0.0000 | 0.1192 | 0.000 |
| filles | fatal | tricheur-fille_constante | v1 | 0/20 | 0.0000 | 0.1192 | -0.622 |
| filles | fatal | tricheur-forme | v1 | 0/20 | 0.0000 | 0.1192 | 0.000 |
| filles | fatal | tricheur-jargon_rare | v1 | 0/20 | 0.0000 | 0.1192 | 0.000 |
| filles | fatal | tricheur-parent_et_loi_aveugle | v1 | 9/20 | 0.4500 | 0.6278 | 14.573 |
| filles | fatal | tricheur-pari_couvert | v1 | 0/20 | 0.0000 | 0.1192 | -0.648 |
| filles | puissance_decisive | puissance-fille-neuve | v1 | 20/20 | 1.0000 | 1.0000 | 90.577 |
| filles | artefact_requis | artefact-fille-sans-parents-dans-le-nul-enveloppe_aveugle | v1 | 12/20 | 0.6000 | 0.7576 | 88.001 |
| filles | artefact_requis | artefact-fille-sans-parents-dans-le-nul-forme | v1 | 10/20 | 0.5000 | 0.6726 | 121.081 |
| filles | descriptif | T1b-fille | v0 | 3/20 | 0.1500 | 0.3218 | 10.985 |
| filles | descriptif | puissance-fille-neuve | v0 | 20/20 | 1.0000 | 1.0000 | 98.650 |
| filles | descriptif | tricheur-parent_et_loi_aveugle | v0 | 7/20 | 0.3500 | 0.5335 | 14.879 |
| socle | fatal | T1a-nul-marginale | v1 | 0/20 | 0.0000 | 0.1192 | 1.161 |
| socle | fatal | T1a-nul-moyenne_glissante | v1 | 0/20 | 0.0000 | 0.1192 | 0.645 |
| socle | fatal | T1a-nul-uniforme | v1 | 0/20 | 0.0000 | 0.1192 | 0.248 |
| socle | fatal | T1b-auto_excite-loi-calendrier | v1 | 0/20 | 0.0000 | 0.1192 | -1.099 |
| socle | fatal | T1b-auto_excite-loi-composition | v1 | 0/20 | 0.0000 | 0.1192 | -0.000 |
| socle | fatal | T1b-calendrier_deterministe-loi-calendrier | v1 | 0/20 | 0.0000 | 0.1192 | -0.000 |
| socle | fatal | T1b-calendrier_deterministe-loi-composition | v1 | 0/20 | 0.0000 | 0.1192 | -0.000 |
| socle | fatal | T1b-derive_lineaire-loi-calendrier | v1 | 0/20 | 0.0000 | 0.1192 | -0.511 |
| socle | fatal | T1b-derive_lineaire-loi-composition | v1 | 0/20 | 0.0000 | 0.1192 | -0.000 |
| socle | fatal | T1b-marche_aleatoire-loi-calendrier | v1 | 0/20 | 0.0000 | 0.1192 | -1.099 |
| socle | fatal | T1b-marche_aleatoire-loi-composition | v1 | 0/20 | 0.0000 | 0.1192 | -0.000 |
| socle | fatal | T1b-rupture-loi-calendrier | v1 | 0/20 | 0.0000 | 0.1192 | -0.511 |
| socle | fatal | T1b-rupture-loi-composition | v1 | 0/20 | 0.0000 | 0.1192 | -0.000 |
| socle | fatal | T1b-sinusoide-loi-calendrier | v1 | 0/20 | 0.0000 | 0.1192 | -0.191 |
| socle | fatal | T1b-sinusoide-loi-composition | v1 | 0/20 | 0.0000 | 0.1192 | -0.000 |
| socle | fatal | T3-couvert-eps0.05-net-faux | v1 | 0/20 | 0.0000 | 0.1192 | -0.684 |
| socle | fatal | T3-couvert-eps0.2-net-faux | v1 | 0/20 | 0.0000 | 0.1192 | -0.559 |
| socle | fatal | T6-parasite-de-Kelly | v1 | 0/20 | 0.0000 | 0.1192 | -0.269 |
| socle | puissance_decisive | T3-couvert-eps0.2-net-vrai | v1 | 19/20 | 0.9500 | 0.9888 | 38.922 |
| socle | artefact_requis | T1b-calendrier_deterministe-loi-composition | v1_sans_urne | 20/20 | 1.0000 | 1.0000 | 5.477 |
| socle | artefact_requis | T1b-derive_lineaire-loi-calendrier | v0 | 13/20 | 0.6500 | 0.7977 | 9.229 |
| socle | artefact_requis | artefact-T1a-bibliotheque-uniforme-seule | v1 | 19/20 | 0.9500 | 0.9888 | 125.534 |
| socle | artefact_requis | artefact-T6-denominateur-en-ligne | v1 | 18/20 | 0.9000 | 0.9663 | 5.261 |
| socle | artefact_requis | artefact-T6-denominateur-part-separee | v1 | 9/20 | 0.4500 | 0.6278 | 8.127 |
| socle | artefact_requis | artefact-permutation-de-l-ordre-d-evaluation | v1_permutation_evaluation | 20/20 | 1.0000 | 1.0000 | 212.303 |
| socle | descriptif | T1b-auto_excite-loi-calendrier | v0 | 14/20 | 0.7000 | 0.8361 | 8.908 |
| socle | descriptif | T1b-auto_excite-loi-calendrier | v1_sans_urne | 0/20 | 0.0000 | 0.1192 | -1.099 |
| socle | descriptif | T1b-auto_excite-loi-composition | v0 | 1/20 | 0.0500 | 0.1960 | 3.302 |
| socle | descriptif | T1b-auto_excite-loi-composition | v1_sans_urne | 15/20 | 0.7500 | 0.8726 | 5.044 |
| socle | descriptif | T1b-calendrier_deterministe-loi-calendrier | v0 | 20/20 | 1.0000 | 1.0000 | 81.218 |
| socle | descriptif | T1b-calendrier_deterministe-loi-calendrier | v1_sans_urne | 0/20 | 0.0000 | 0.1192 | -0.000 |
| socle | descriptif | T1b-calendrier_deterministe-loi-composition | v0 | 0/20 | 0.0000 | 0.1192 | -0.916 |
| socle | descriptif | T1b-derive_lineaire-loi-calendrier | v1_sans_urne | 1/20 | 0.0500 | 0.1960 | 3.665 |
| socle | descriptif | T1b-derive_lineaire-loi-composition | v0 | 16/20 | 0.8000 | 0.9069 | 5.491 |
| socle | descriptif | T1b-derive_lineaire-loi-composition | v1_sans_urne | 20/20 | 1.0000 | 1.0000 | 5.491 |
| socle | descriptif | T1b-marche_aleatoire-loi-calendrier | v0 | 20/20 | 1.0000 | 1.0000 | 21.038 |
| socle | descriptif | T1b-marche_aleatoire-loi-calendrier | v1_sans_urne | 0/20 | 0.0000 | 0.1192 | 0.514 |
| socle | descriptif | T1b-marche_aleatoire-loi-composition | v0 | 4/20 | 0.2000 | 0.3784 | 5.416 |
| socle | descriptif | T1b-marche_aleatoire-loi-composition | v1_sans_urne | 20/20 | 1.0000 | 1.0000 | 5.483 |
| socle | descriptif | T1b-rupture-loi-calendrier | v0 | 19/20 | 0.9500 | 0.9888 | 18.608 |
| socle | descriptif | T1b-rupture-loi-calendrier | v1_sans_urne | 0/20 | 0.0000 | 0.1192 | 0.000 |
| socle | descriptif | T1b-rupture-loi-composition | v0 | 8/20 | 0.4000 | 0.5814 | 5.228 |
| socle | descriptif | T1b-rupture-loi-composition | v1_sans_urne | 20/20 | 1.0000 | 1.0000 | 5.491 |
| socle | descriptif | T1b-sinusoide-loi-calendrier | v0 | 20/20 | 1.0000 | 1.0000 | 31.395 |
| socle | descriptif | T1b-sinusoide-loi-calendrier | v1_sans_urne | 0/20 | 0.0000 | 0.1192 | 0.237 |
| socle | descriptif | T1b-sinusoide-loi-composition | v0 | 0/20 | 0.0000 | 0.1192 | 0.013 |
| socle | descriptif | T1b-sinusoide-loi-composition | v1_sans_urne | 20/20 | 1.0000 | 1.0000 | 5.492 |
| socle | descriptif | T3-couvert-eps0.05-net-vrai | v0 | 16/20 | 0.8000 | 0.9069 | 10.073 |
| socle | descriptif | T3-couvert-eps0.05-net-vrai | v1 | 4/20 | 0.2000 | 0.3784 | 4.258 |
| socle | descriptif | T3-couvert-eps0.2-net-vrai | v0 | 19/20 | 0.9500 | 0.9888 | 44.232 |
| socle | descriptif | puissance-loi-de-domaine-vraie | v0 | 20/20 | 1.0000 | 1.0000 | 136.945 |
| socle | descriptif | puissance-loi-de-domaine-vraie | v1 | 20/20 | 1.0000 | 1.0000 | 137.212 |
| socle | descriptif | puissance-loi-vraie-plus-derive | v0 | 20/20 | 1.0000 | 1.0000 | 71.799 |
| socle | descriptif | puissance-loi-vraie-plus-derive | v1 | 20/20 | 1.0000 | 1.0000 | 68.057 |
