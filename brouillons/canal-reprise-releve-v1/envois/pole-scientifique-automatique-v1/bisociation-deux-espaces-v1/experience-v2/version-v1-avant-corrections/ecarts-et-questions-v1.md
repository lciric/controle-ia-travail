# Écarts et questions — expérience v2 (bisociation à deux espaces) — v1

Rédigé par Sonnet (seconde session), le 30 octobre 2026. Préenregistrement de référence : `prereg/preenregistrement-bisociation-deux-espaces-v2.md`, empreinte `e821e875…`. Je n'ai tranché aucun point ci-dessous. Les points marqués BLOQUANT empêchent l'exécution qui en dépend (indiquée).

## Questions bloquantes

**Q-01 — BLOQUANT pour l'invocation unique : le taux de régénération après échec de plantation dépasse S11 (2 %).**
- Mesure (essai de plomberie, RACINE_VALIDATION, indices 920000 à 920299, 300 mondes par condition, hors de toute plage du § 7 ; seuls les taux de régénération et d'exclusion ont été lus) : M_bien 5,0 % ; M_moyen 5,7 % ; M_mal 5,7 % ; M_inertes 5,0 % ; M_couplage_faible 4,7 % ; M_palettes_communes 5,3 % ; M_palettes_disjointes 5,7 % ; M_fonds_1ou2 4,3 % ; V_fuite 4,3 % ; V_concepts_absents 4,0 % ; INV 2,7 % ; V_moyeu_conceptuel 2,7 % ; SP 0 ; V_surface 0. Exclusion : 0 sauf M_mal (0,7 %).
- Cause (diagnostic sur 600 mondes M_bien, indices 930000+) : 36 articles sur 40 sont réservés aux ponts (G6 : 15 paires entre champs différents, 3 paires dans un même champ) ; l'échec porte presque toujours sur le dernier pont tiré, surtout dans les mondes à 2 champs (39 échecs « surface » contre 2 à 3 champs ; mondes acceptés par nombre de champs : 2 → 183, 3 → 204, 4 → 213, donc la loi du nombre de champs est déformée par la régénération). L'ordre de plantation (a, b, c, d, e) est un choix d'implémentation du premier sous-agent, non écrit au § 1.
- Variantes essayées dans un fichier de travail, NON adoptées : (e) avant (b), (c), (d) : 22,7 % de régénération en M_bien ; (d) avant (b), (c), (e) : 8,7 %. Aucun ordre simple ne passe sous 2 %.
- Conséquence : la liste d'arrêt (« taux de mondes régénérés > S11 → arrêt ») s'appliquerait presque sûrement à M_bien et M_moyen. Décision de Lazar : relever S11 pour ce taux, ou un algorithme de plantation qui garde la loi des champs, ou moins d'articles de ponts (S16e). C'est une modification de seuil ou de paramètre : nœud de décision.

**Q-02 — N_grille : bras des mondes de décision, ou de la seule validation ?** § 5 et § 9 : grille sur 200 mondes de validation « moyen » ; § 7 : aucun code de contraste pour N_grille ; § 8 : « N_grille » figure parmi les descriptifs à 95 %. Implémenté : N_grille tourne seulement à l'étape (1) du § 9 ; il est exclu des mondes de décision (`travail_v2.BRAS_DECISION`). À confirmer.

**Q-03 — BLOQUANT pour l'invocation (étape 3, mondes NR) : graine du rééchantillonnage de la non-régression (C11, A5).** § 7 : « C11, sans code de contraste ». La clé `(code de condition, code de contraste, 99)` n'a donc pas de deuxième élément pour NR_bien (10) et NR_moyen (11). `analyse_v2.CODE_CONTRASTE_NR = None` : l'invocation refuse de partir (vérifié avant le premier monde) tant qu'il n'est pas fixé. Lecture naturelle possible (non retenue) : le code 1 de Δ(N, b).

**Q-04 — BLOQUANT pour la validation V4 : définition de la jumelle.** § 6 V4 : « échangeant les mots propres de deux domaines pour les articles de ponts ». Quels deux domaines, quels mots. Code écrit pour la lecture « pour chaque pont planté, ses deux articles échangent les mots propres de leurs domaines » (`monde_v2.generer(..., surcharge={"jumelle": True})`, `validation_v2.v4_jumelles`), refusé tant que `lecture="echange_ponts"` n'est pas passée explicitement. Latents égaux et étiquettes identiques vérifiés sur 3 mondes d'essai (plomberie).

## Lectures retenues, non bloquantes (à confirmer ou corriger)

- **Q-05** — V1 : le texte ne dit pas dans quelle condition. V1 est évaluée sur M_bien et M_moyen (les deux doivent passer) ; V2, V3, V5 sur M_bien ; V6 (≥ 6) sur M_moyen ; le plafond de l'oracle (S8) en M_bien et M_moyen est rangé avec V6.
- **Q-06** — Définitions complétées pour V2 (κ latent : fonds, moyeu H et rares latents ; poids log(40/fréquence latente)), V3 (10 % = ⌈0,1 × paires valides⌉, égalités par indice), V5 (cinq statuts : conceptuel, greffe+jumeau, faux, proche, surface ; moyenne sur les paires plantées valides, tous mondes), V7 (classes de paires, priorité dans l'ordre de la liste du § 6). Aucun seuil n'en dépend sauf V2, V3, V5.
- **Q-07** — G8 « bit à bit » : avec la fuite de domaine ρ, une émission rare couverte est remplacée par le fond dominant du domaine ; dans M_inertes les émissions rares changent d'articles, donc quelques articles diffèrent aussi par leurs étiquettes de fond (l'essai en tolère ≤ 10 articles par monde). Opérateurs, moyeu, contraintes, domaines et latents sont bit à bit égaux (vérifié).
- **Q-08** — Portée de S11 : exclusion contrôlée dans les conditions de décision seulement (M_bien, M_moyen, SP, INV, V_fuite, M_inertes, NR_bien, NR_moyen), rapportée ailleurs ; régénération et sortie vide contrôlées dans toutes les conditions.
- **Q-09** — « Résultats par nombre de champs (2, 3, 4) » : estimation de Δ(N, b) et nombre de mondes seulement, sans intervalle (aucun code de graine au § 7).
- **Q-10** — Couverture des concepts (G9 i) : tirée par émission (article, concept), non par mot de lexique (contrairement aux opérateurs de v1).
- **Q-11** — σ̂ de S9 : écart-type avec ddof = 1 sur les mondes non exclus. M_mal : « abandonnée si plafond < S8 » est consigné comme drapeau, sans arrêt. Contraste 10 : mondes non exclus des deux côtés. L'horodatage du manifeste est à la seconde et `verifier_ordre` exige un résultat strictement postérieur (toujours vrai en pratique : une condition dure plus d'une seconde).
- **Q-12** — Reproduction des témoins : mondes NR_bien et NR_moyen, RACINE_VALIDATION, indices 0 à 1199 (aucune autre plage de validation n'emploie les codes 10 et 11).

## Ce qui n'a pas été exécuté (consigne R1)

- Validation du générateur V1 à V9 : code écrit (`validation_v2.py`), non lancé. Donc non faits : l'essai R5 de J sur les 300 miroirs de M_inertes (V9 ; seule la plomberie est éprouvée sur 30 mondes d'essai, sans lire le booléen), V4, et les seuils S13.
- Invocation unique (étapes 1 à 3), les contrastes de décision, la grille, S9 : non lancés ; aucune moyenne de Δ(N, ·) calculée sur un monde.

## Écarts du code du premier sous-agent corrigés

Voir `LISEZMOI-experience-v2-v1.md`, section « Qui a écrit quoi ». L'original est conservé dans `brouillon-opus-origine/`.
