# Expérience 1 du pôle — juge v1 : non adopté (socle : adopté ; critère des filles : non adopté)

Horodatage : 2026-10-27T11:04:31Z (argument --horodatage (date -u dans la commande de lancement)). Graine maîtresse 90342783766775327375142856453646672169 ; 1000 répétitions par ligne ; 200 tirages frais par répétition ; α = 0.05 (seuil de richesse 20) ; lecture continue (promotion dès que W_t ≥ 1/α, inégalité de Ville).
Simulation seulement : ces taux valent pour les mondes synthétiques décrits, rien au-delà.

- **Global** — non adopté. Contrôles fatals : 28, échecs : ['tricheur-parent_et_loi_aveugle', 'T1b-fille'], taux max 0.392 (tricheur-parent_et_loi_aveugle) ; artefacts requis : 8, non vus : aucun ; puissance décisive : {'puissance-fille-neuve': 0.997, 'T3-couvert-eps0.2-net-vrai': 0.958} (insuffisantes : aucune).
- **Socle (fiches sans parents)** — adopté. Contrôles fatals : 18, échecs : aucun, taux max 0.001 (T1a-nul-marginale) ; artefacts requis : 6, non vus : aucun ; puissance décisive : {'T3-couvert-eps0.2-net-vrai': 0.958} (insuffisantes : aucune).
- **Critère des filles** — non adopté. Contrôles fatals : 10, échecs : ['tricheur-parent_et_loi_aveugle', 'T1b-fille'], taux max 0.392 (tricheur-parent_et_loi_aveugle) ; artefacts requis : 2, non vus : aucun ; puissance décisive : {'puissance-fille-neuve': 0.997} (insuffisantes : aucune).
- Perte de puissance sur la fille neuve (v0 − v1) : -0.0030000000000000027 (prédite ≤ 0.05).
- Ce qui a cédé : ['tricheur-parent_et_loi_aveugle', 'T1b-fille'].
- Conformité du rapport (70 couples, 1000 répétitions chacun) : conforme.
- Appariement v0/v1 (répétitions différentes par ligne de puissance) : {'puissance-fille-neuve': 5, 'T3-couvert-eps0.05-net-vrai': 713, 'T3-couvert-eps0.2-net-vrai': 39, 'puissance-loi-de-domaine-vraie': 4, 'puissance-loi-vraie-plus-derive': 17}.
- Déclencheurs de l'audit de symétrie (R4) : aucun.

| partie | rôle | contrôle | juge | promotions | taux | borne haute 95 % | log W max observé |
|---|---|---|---|---|---|---|---|
| filles | fatal | T1b-fille | v1 | 150/1000 | 0.1500 | 0.1695 | 20.300 |
| filles | fatal | T9-disjonction-partitionnee | v1 | 0/1000 | 0.0000 | 0.0027 | 0.000 |
| filles | fatal | tricheur-adimensionnement | v1 | 0/1000 | 0.0000 | 0.0027 | 0.000 |
| filles | fatal | tricheur-copie_renommee | v1 | 0/1000 | 0.0000 | 0.0027 | 0.000 |
| filles | fatal | tricheur-enveloppe_aveugle | v1 | 0/1000 | 0.0000 | 0.0027 | 0.087 |
| filles | fatal | tricheur-fille_constante | v1 | 0/1000 | 0.0000 | 0.0027 | -0.534 |
| filles | fatal | tricheur-forme | v1 | 0/1000 | 0.0000 | 0.0027 | 0.000 |
| filles | fatal | tricheur-jargon_rare | v1 | 0/1000 | 0.0000 | 0.0027 | 0.000 |
| filles | fatal | tricheur-parent_et_loi_aveugle | v1 | 392/1000 | 0.3920 | 0.4177 | 26.235 |
| filles | fatal | tricheur-pari_couvert | v1 | 0/1000 | 0.0000 | 0.0027 | -0.478 |
| filles | puissance_decisive | puissance-fille-neuve | v1 | 997/1000 | 0.9970 | 0.9988 | 123.414 |
| filles | artefact_requis | artefact-fille-sans-parents-dans-le-nul-enveloppe_aveugle | v1 | 640/1000 | 0.6400 | 0.6646 | 102.045 |
| filles | artefact_requis | artefact-fille-sans-parents-dans-le-nul-forme | v1 | 402/1000 | 0.4020 | 0.4277 | 151.748 |
| filles | descriptif | T1b-fille | v0 | 326/1000 | 0.3260 | 0.3508 | 16.745 |
| filles | descriptif | puissance-fille-neuve | v0 | 994/1000 | 0.9940 | 0.9969 | 124.887 |
| filles | descriptif | tricheur-parent_et_loi_aveugle | v0 | 416/1000 | 0.4160 | 0.4418 | 26.391 |
| socle | fatal | T1a-nul-marginale | v1 | 1/1000 | 0.0010 | 0.0045 | 3.861 |
| socle | fatal | T1a-nul-moyenne_glissante | v1 | 1/1000 | 0.0010 | 0.0045 | 3.049 |
| socle | fatal | T1a-nul-uniforme | v1 | 0/1000 | 0.0000 | 0.0027 | 1.898 |
| socle | fatal | T1b-auto_excite-loi-calendrier | v1 | 0/1000 | 0.0000 | 0.0027 | 0.522 |
| socle | fatal | T1b-auto_excite-loi-composition | v1 | 0/1000 | 0.0000 | 0.0027 | -0.000 |
| socle | fatal | T1b-calendrier_deterministe-loi-calendrier | v1 | 0/1000 | 0.0000 | 0.0027 | -0.000 |
| socle | fatal | T1b-calendrier_deterministe-loi-composition | v1 | 0/1000 | 0.0000 | 0.0027 | -0.000 |
| socle | fatal | T1b-derive_lineaire-loi-calendrier | v1 | 0/1000 | 0.0000 | 0.0027 | -0.511 |
| socle | fatal | T1b-derive_lineaire-loi-composition | v1 | 0/1000 | 0.0000 | 0.0027 | -0.000 |
| socle | fatal | T1b-marche_aleatoire-loi-calendrier | v1 | 0/1000 | 0.0000 | 0.0027 | 1.080 |
| socle | fatal | T1b-marche_aleatoire-loi-composition | v1 | 0/1000 | 0.0000 | 0.0027 | -0.000 |
| socle | fatal | T1b-rupture-loi-calendrier | v1 | 0/1000 | 0.0000 | 0.0027 | 0.299 |
| socle | fatal | T1b-rupture-loi-composition | v1 | 0/1000 | 0.0000 | 0.0027 | -0.000 |
| socle | fatal | T1b-sinusoide-loi-calendrier | v1 | 0/1000 | 0.0000 | 0.0027 | 0.218 |
| socle | fatal | T1b-sinusoide-loi-composition | v1 | 0/1000 | 0.0000 | 0.0027 | -0.000 |
| socle | fatal | T3-couvert-eps0.05-net-faux | v1 | 0/1000 | 0.0000 | 0.0027 | -0.523 |
| socle | fatal | T3-couvert-eps0.2-net-faux | v1 | 0/1000 | 0.0000 | 0.0027 | -0.484 |
| socle | fatal | T6-parasite-de-Kelly | v1 | 0/1000 | 0.0000 | 0.0027 | -0.106 |
| socle | puissance_decisive | T3-couvert-eps0.2-net-vrai | v1 | 958/1000 | 0.9580 | 0.9673 | 43.973 |
| socle | artefact_requis | T1b-calendrier_deterministe-loi-composition | v1_sans_urne | 1000/1000 | 1.0000 | 1.0000 | 5.477 |
| socle | artefact_requis | T1b-derive_lineaire-loi-calendrier | v0 | 670/1000 | 0.6700 | 0.6940 | 11.845 |
| socle | artefact_requis | artefact-T1a-bibliotheque-uniforme-seule | v1 | 969/1000 | 0.9690 | 0.9768 | 205.050 |
| socle | artefact_requis | artefact-T6-denominateur-en-ligne | v1 | 881/1000 | 0.8810 | 0.8968 | 5.305 |
| socle | artefact_requis | artefact-T6-denominateur-part-separee | v1 | 425/1000 | 0.4250 | 0.4509 | 9.722 |
| socle | artefact_requis | artefact-permutation-de-l-ordre-d-evaluation | v1_permutation_evaluation | 1000/1000 | 1.0000 | 1.0000 | 212.303 |
| socle | descriptif | T1b-auto_excite-loi-calendrier | v0 | 652/1000 | 0.6520 | 0.6763 | 12.301 |
| socle | descriptif | T1b-auto_excite-loi-calendrier | v1_sans_urne | 1/1000 | 0.0010 | 0.0045 | 3.123 |
| socle | descriptif | T1b-auto_excite-loi-composition | v0 | 76/1000 | 0.0760 | 0.0910 | 4.425 |
| socle | descriptif | T1b-auto_excite-loi-composition | v1_sans_urne | 665/1000 | 0.6650 | 0.6891 | 5.479 |
| socle | descriptif | T1b-calendrier_deterministe-loi-calendrier | v0 | 1000/1000 | 1.0000 | 1.0000 | 81.218 |
| socle | descriptif | T1b-calendrier_deterministe-loi-calendrier | v1_sans_urne | 0/1000 | 0.0000 | 0.0027 | -0.000 |
| socle | descriptif | T1b-calendrier_deterministe-loi-composition | v0 | 0/1000 | 0.0000 | 0.0027 | -0.916 |
| socle | descriptif | T1b-derive_lineaire-loi-calendrier | v1_sans_urne | 8/1000 | 0.0080 | 0.0141 | 4.004 |
| socle | descriptif | T1b-derive_lineaire-loi-composition | v0 | 786/1000 | 0.7860 | 0.8065 | 5.491 |
| socle | descriptif | T1b-derive_lineaire-loi-composition | v1_sans_urne | 1000/1000 | 1.0000 | 1.0000 | 5.491 |
| socle | descriptif | T1b-marche_aleatoire-loi-calendrier | v0 | 992/1000 | 0.9920 | 0.9955 | 28.939 |
| socle | descriptif | T1b-marche_aleatoire-loi-calendrier | v1_sans_urne | 4/1000 | 0.0040 | 0.0089 | 5.928 |
| socle | descriptif | T1b-marche_aleatoire-loi-composition | v0 | 280/1000 | 0.2800 | 0.3039 | 5.485 |
| socle | descriptif | T1b-marche_aleatoire-loi-composition | v1_sans_urne | 1000/1000 | 1.0000 | 1.0000 | 5.491 |
| socle | descriptif | T1b-rupture-loi-calendrier | v0 | 966/1000 | 0.9660 | 0.9742 | 25.153 |
| socle | descriptif | T1b-rupture-loi-calendrier | v1_sans_urne | 1/1000 | 0.0010 | 0.0045 | 3.789 |
| socle | descriptif | T1b-rupture-loi-composition | v0 | 479/1000 | 0.4790 | 0.5050 | 5.371 |
| socle | descriptif | T1b-rupture-loi-composition | v1_sans_urne | 1000/1000 | 1.0000 | 1.0000 | 5.492 |
| socle | descriptif | T1b-sinusoide-loi-calendrier | v0 | 1000/1000 | 1.0000 | 1.0000 | 39.297 |
| socle | descriptif | T1b-sinusoide-loi-calendrier | v1_sans_urne | 1/1000 | 0.0010 | 0.0045 | 4.986 |
| socle | descriptif | T1b-sinusoide-loi-composition | v0 | 0/1000 | 0.0000 | 0.0027 | 0.089 |
| socle | descriptif | T1b-sinusoide-loi-composition | v1_sans_urne | 1000/1000 | 1.0000 | 1.0000 | 5.492 |
| socle | descriptif | T3-couvert-eps0.05-net-vrai | v0 | 909/1000 | 0.9090 | 0.9229 | 13.075 |
| socle | descriptif | T3-couvert-eps0.05-net-vrai | v1 | 196/1000 | 0.1960 | 0.2175 | 7.540 |
| socle | descriptif | T3-couvert-eps0.2-net-vrai | v0 | 997/1000 | 0.9970 | 0.9988 | 48.173 |
| socle | descriptif | puissance-loi-de-domaine-vraie | v0 | 999/1000 | 0.9990 | 0.9998 | 161.713 |
| socle | descriptif | puissance-loi-de-domaine-vraie | v1 | 995/1000 | 0.9950 | 0.9976 | 153.369 |
| socle | descriptif | puissance-loi-vraie-plus-derive | v0 | 997/1000 | 0.9970 | 0.9988 | 82.773 |
| socle | descriptif | puissance-loi-vraie-plus-derive | v1 | 980/1000 | 0.9800 | 0.9861 | 72.978 |
