# Addendum d'écarts déclarés — préenregistrement de bisociation à deux espaces v2 — v1 (BROUILLON, NON SCELLÉ)

Rédigé par conv-audit (Opus 5.5), 30 octobre 2026. Se rattache à `prereg/preenregistrement-bisociation-deux-espaces-v2.md` (empreinte `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea`, scellé le 30 octobre, R-581), qui reste inchangé (R12). Cet addendum ne s'applique qu'une fois scellé à son tour.

## Pourquoi un addendum

Pendant l'écriture du code, avant toute validation du générateur et toute invocation des mondes de décision, le code a relevé quatre points où le préenregistrement ne permet pas de lancer tel quel, et huit lectures à confirmer (`experience-v2/ecarts-et-questions-v1.md`, `ecarts-et-questions-v1.md.sha256`). Un écart à un préenregistrement scellé est un nœud de décision de Lazar.

**Ce qui a été lu avant ces décisions, et seulement cela** (règle R1) : des taux de plomberie (régénération, exclusion) sur des mondes d'essai aux indices 920000 à 920299 et 930000 et plus, hors de toute plage du § 7 ; et la reproduction des témoins de v1 (b, a, c, d1) sur les mondes de non-régression, exigée par la liste d'arrêt. **Aucun contraste de décision, aucune moyenne de Δ(N, ·), aucun résultat de V1 à V9 n'a été calculé ni lu.**

## Décisions de Lazar

Mot direct de Lazar, 30 octobre 2026, 12:19 heure de Paris (R-585) : « Ma recommandation : (a), confiance 0,7. ; go recos ».

| Point | Écart au texte scellé | Décision |
|---|---|---|
| **Q-01** taux de régénération | Liste d'arrêt : « taux de mondes régénérés après échec de plantation > S11 (2 %) → arrêt ». Mesuré sur mondes d'essai : 4 à 5,7 % dans les conditions principales (36 articles sur 40 réservés aux ponts ; le dernier pont échoue surtout dans les mondes à 2 champs), ce qui déforme la loi du nombre de champs (G). | (a) **Seuil d'arrêt du seul taux de régénération porté à 10 %** (les taux d'exclusion et de bras vides restent à 2 %). **Régénération au même nombre de champs que le monde raté** : la nouvelle tentative tire un monde avec le nombre de champs déjà tiré, de sorte que la loi du nombre de champs reste celle de G. Le taux de régénération est rapporté par condition et par nombre de champs. |
| **Q-03** graine de la non-régression | § 7 : « C11, sans code de contraste » ; la clé de rééchantillonnage n'a pas de deuxième élément pour NR_bien (10) et NR_moyen (11). | **Code de contraste 16** pour la non-régression (libre dans la liste du § 7) : clé `(10, 16, 99)` et `(11, 16, 99)`. |
| **Q-04** jumelle de V4 | § 6 V4 : « échangeant les mots propres de deux domaines pour les articles de ponts » ne dit pas quels domaines ni quels mots. | Lecture retenue : **pour chaque pont planté, ses deux articles échangent les mots propres de leurs domaines** ; mêmes latents et même flux de graines pour les rôles 1 à 3. |
| **Q-02** grille | § 5 et § 9 : grille sur 200 mondes de validation ; § 8 : N_grille parmi les descriptifs ; § 7 : aucun code de contraste. | **N_grille tourne seulement à l'étape (1) du § 9** (validation) ; ses résultats sont écrits dans le fichier de validation scellé, rapportés comme diagnostic. |
| **Q-05 à Q-12** | Lectures retenues par le code (conditions de V1 à V6, définitions complétées de V2, V3, V5, V7, tolérance bit à bit de G8 sous fuite, portée de S11, résultats par nombre de champs sans intervalle, couverture des concepts par émission, σ̂ à ddof 1, plage NR de la reproduction). | **Validées telles qu'écrites** dans `ecarts-et-questions-v1.md`. |

## Effet attendu des écarts sur le verdict

- Q-01 : les bras sont comparés sur les mêmes mondes (écarts appariés) ; la régénération ne choisit pas les mondes sur une quantité mesurée par un bras. Elle peut changer la population des mondes, pas favoriser un bras. La régénération au même nombre de champs supprime la déformation de G. **Aucun seuil de décision (S1 à S10, S12 à S17) n'est touché.**
- Q-02, Q-03, Q-04 : mécaniques ; aucun seuil de décision touché.

## Contre-lecture et scellement

- Contre-lecture du code par un Opus neuf : en cours (arrêtée sur limite d'usage, reprise à 16:00 heure de Paris) ; son avis sur Q-01 à Q-12 est intégré avant scellement ; tout désaccord qui touche une décision ci-dessus retourne à Lazar.
- Contre-lecture R2 de cet addendum par un modèle différent de son auteur : À FAIRE.
- Scellement par `controle_ia.scellement sceller`, puis application au code, avant la validation du générateur.
