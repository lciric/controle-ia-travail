# Contre-lecture (R2) du préenregistrement de l'épreuve de la garantie de seuil du théorème de mise en œuvre aléatoire des audits (papier D, chantier 3) — v1

- Contre-lecteur : sous-agent neuf, Opus 5.5, qui n'a écrit ni le préenregistrement ni le script. Date : 2026-11-24.
- Pièce relue : `prereg-seuil-chantier3-v1.md` (bloc-notes de session). Aucun fichier modifié, rien de lancé, aucun tirage sur la grille, aucun commit, pas de réseau.
- Empreintes des documents qui font foi recalculées : les quatre empreintes citées (théorème, `check_audit_v1.py`, note, audit et son script) se vérifient.

## Verdict

**Conforme avec corrections.** La structure exigée par R1 est complète. Le validateur, lancé sur une copie, ne relève qu'un défaut : la section « Contre-lecture » attendue, sans ses deux empreintes. Tous les chiffres de conception déterministes se recalculent à l'identique. Aucun défaut n'est bloquant. Six défauts majeurs laissent cependant une latitude après lecture, ou feraient prononcer un verdict faux. Ils sont à corriger avant le scellement.

## Défauts

**1. Majeur. L'objet éprouvé est une étape de la preuve, pas l'énoncé du théorème** (section Hypothèse, garantie (G) ; table de lecture, ligne « garantie réfutée »).
L'énoncé de la partie (c) (lignes 364 à 393 du `.tex`) porte sur le processus **plafonné**, au niveau **δ**. La borne δ/2 sur le processus **non plafonné** n'apparaît que dans la preuve : c'est la version unilatérale de (a), avec Λ = ln(2K/δ). Elle ne découle pas non plus de l'énoncé de (a), qui est bilatéral au niveau δ. La métrique mesure donc bien l'étape de preuve : processus non plafonné, événement strict, séparé du dépassement de budget. En revanche, si l'on observe δ/2 < V ≤ δ, la conclusion écrite, « la partie (c) […] est fausse », va trop loin.
Corrections :
- renommer (G) en « étape unilatérale de la preuve de (c) » ;
- ajouter une métrique du processus plafonné, à lire contre δ : arrêt des audits dès que N atteint B_rand ; l'événement plafonné est inclus dans « violation non plafonnée ou dépassement » ;
- graduer le verdict en trois issues : « étape de preuve réfutée » si δ/2 < V ≤ δ ; « énoncé (c) réfuté » si la violation plafonnée dépasse δ ; « (a) réfutée » seulement par l'événement bilatéral au niveau δ.

**2. Majeur. Le contrôle (4) de l'audit de symétrie est faux dès que la marge est non nulle** (Critères, audit de symétrie, point 4).
P(Bin(n,ρ_κ) < nρ_κ) n'est la probabilité de violation au premier tour audité qu'à m = 0. Pour une marge m, il faut P(Bin(n,ρ_κ) < n(ρ_κ − m/(γW))), où ρ_κ est le taux du plan de marge m. Or l'audit est déclenché par toute réfutation à λ = 1, donc à m = ε : la fréquence observée, presque nulle, serait comparée à environ 0,5. On déclarerait un « défaut » à tort, et une réfutation réelle serait invalidée. C'est une asymétrie contraire à R4.
Correction : écrire la formule générale en m.

**3. Majeur. L'audit de symétrie n'a pas de tolérances chiffrées** (points 2 à 4).
Les tolérances manquent pour l'écart entre les deux chemins de comptage, pour la moyenne et la variance de x̂_K, et pour la fréquence au premier tour. Or « sans défaut » conditionne les verdicts de réfutation : la décision est laissée à l'auditeur après lecture.
Correction : fixer d'avance les tolérances, par exemple identité répétition par répétition à 10⁻⁹ près, puis 5 erreurs types, comme sur le banc témoin. Fixer aussi la racine de graines de la relance : par exemple entropie + 1, et aucune troisième course sans décision de Lazar.

**4. Majeur. L'audit n'est pas déclenché dans les deux sens, et le banc témoin est aveugle à la mémoire** (R4 ; gardes).
L'audit est déclenché par « trop propre » à λ = 0 et par une réfutation, mais jamais par « la garantie tient ». C'est pourtant l'issue que P1 annonce : « zéro violation dans la plupart des points ». Le banc témoin a a = 0 et Γ_K = 1. Il ne voit donc aucune erreur sur a, sur la récurrence à mémoire ni sur Γ_K, qui figure dans ε (par exemple Σaⁱ au lieu de Σa²ⁱ). Une telle erreur peut gonfler ε, laisser des violations à λ = 0 et produire « tient » sans aucun audit.
Corrections :
- lancer les contrôles (1) à (4) en tout point à λ = 1, quelle que soit l'issue : leur coût est faible ;
- ajouter un second banc témoin avec a > 0, par exemple η = ∞ et a = 1, avec une probabilité exacte calculée par programmation dynamique sur les comptes d'audits cumulés (petit K, n = 100) ;
- recalculer ε en chaque point par un second chemin, la forme fermée Γ_K = (1 − a^{2K})/(1 − a²).

**5. Majeur. Le texte se contredit sur la prolongation** (section Seuil contre la table de lecture).
La section Seuil ne prolonge que les points indéterminés. La ligne de réfutation exige au contraire « au-dessus, confirmé par la prolongation ». Plusieurs questions restent ouvertes :
- un point « au-dessus » est-il prolongé ?
- que conclure si la prolongation le classe « indéterminé » ou « sous » ?
- un point d'abord indéterminé, puis classé « au-dessus » après prolongation, vaut-il réfutation ?
Correction : une règle unique, écrite d'avance pour chaque combinaison.

**6. Majeur. La lecture n'est pas univoque à λ = 0** (lignes « trop propre », « marge non nécessaire », réfutation de P2).
Si la borne haute est sous 0,5 mais la fréquence au-dessus de δ/2, le point est à la fois « trop propre » et une réfutation de P2. Le verdict après un audit sans défaut n'est pas écrit : est-ce « tient » en ce point avec P2 réfutée ? Si la fréquence est sous δ/2, le point relève à la fois de « trop propre » et de « marge non nécessaire ».
Corrections : réserver « trop propre » à V̂ = 0 ou à « sous δ/2 » ; écrire le verdict de chaque case après audit ; donner un ordre de priorité explicite.

**7. Mineur. Le risque d'ensemble est mal annoncé** (Seuil).
Le chiffre de 1,4 % ne vaut que pour le premier tirage. Avec une prolongation lue seule, il n'y a pas de biais d'arrêt optionnel, mais le risque par point double : environ 2 × 10⁻⁴, soit au plus 2,8 % sur 138 points. Les autres familles de tests ne sont pas chiffrées : 138 tests à λ = 0, 276 classements de P3, 690 tests de Fisher (environ 6,9 % au total).
Correction : annoncer le risque par famille.

Puissance : elle suffit largement.
- À 1,15 δ/2, la probabilité de classer « au-dessus » vaut 0,9998.
- À δ/20, la borne haute vaut 0,0031 (δ = 0,05) ou 0,0059 (δ = 0,1), loin de δ/2.
- La zone indéterminée couvre ±7,3 % à δ = 0,05 et ±5,1 % à δ = 0,1 : « au plus environ ±7 % » est légèrement sous-estimé.

**8. Mineur. Un cas d'égalité, propre à η = ∞, peut arrêter la course à tort** (règle d'arrêt 3).
Avec c = ½γK et K pair, la trajectoire sans audit atteint c exactement au tour K/2. Le calcul en flottants du plan laisse alors des taux de 4 × 10⁻¹⁶ à 2 × 10⁻¹⁵ en 32 points. Un κ calculé par « premier taux > 0 » donne 25 tours tenus au lieu de 24, et la règle d'arrêt 3 se déclencherait. Avec la formule exacte, le minimum est bien 24.
Correction : définir κ par la formule exacte, ou par un seuil sur ρ, et signaler l'égalité déterministe x̂_{K/2} = c à λ = 0 (couverte par τ).

**9. Mineur. La bissection laisse de la latitude** (Métrique).
Elle décide sur l'estimation ponctuelle. L'unité de « 2 % » n'est pas dite (fréquence ou marge ?). Le tirage de confirmation n'a pas de conséquence écrite s'il classe ε_emp « au-dessus ». L'« encadrement par la grille » et l'ensemble des points où P4 est lue (« en tout point ») ne sont pas définis.

**10. Mineur. Plusieurs prédictions ne sont pas réfutables telles qu'écrites.**
Dans P1, « V ≤ δ/20 partout » et « la plupart » n'ont pas de règle de réfutation : à classer comme descriptif, ou à doter d'un critère. Dans P3, le sort d'un point indéterminé à λ = 0,1 ou λ = 0,75, qui ne reçoit pas de prolongation, n'est pas dit.

**11. Mineur. Les graines sont incomplètement spécifiées (R9).**
La composante `i_rang` n'est définie ni pour les blocs 0 à 5 (lots de 10⁴ ?), ni pour le bloc 7 (λ = 0 et λ = 1 au même point partagent la même clé), ni pour les blocs 8 et 9. Les lots à l'intérieur d'une itération de bissection ne sont pas couverts non plus. La règle d'arrêt 4 rattraperait un doublon, mais il faut l'écrire d'avance.

**12. Mineur. Les règles d'arrêt 4 et 5 ne sont pas éprouvées (R5).**
Les gardes des règles 4 (valeur non finie, clé en double, fichier déjà présent) et 5 (sensibilité à τ) ne sont pas testées sur un cas sain et sur un artefact. L'action à prendre quand la garde « tirages » se déclenche en un point de la grille n'est pas dite. Le critère « 5 % en relatif » est mal posé quand les comptes sont petits.
Correction : un écart absolu en comptes.

**13. Mineur. Plusieurs références sont à reprendre.**
- B_rand n'est pas précisé pour λ < 1 (B_{λε} ou B_ε ?).
- Le théorème occupe les lignes 364 à 393, et non 364 à 390.
- Le commit de départ est à mettre à jour au scellement : HEAD est `3cb84756`.

## Les deux écarts à la note : justifiés, sans renvoi à décision

**Premier écart, c = ½ΔR·G_K.** La note ne donnait cette valeur qu'en exemple. L'écart ne touche ni une hypothèse ni une revendication.
Recalculs : 138 points admissibles sur 144. Les 6 points inadmissibles sont bien ceux où n = 100, γ = 0,2, η = 1 et C = 19 (ε de 0,74 à 0,93, pour c = 0,5). La règle de la note donnerait 8 points sans audit et 30 points inadmissibles, deux ensembles disjoints. Les autres chiffres se confirment :
- au moins 24 tours tenus ;
- au moins 2,5 audits attendus par tour tenu ;
- √(2Λ) ≥ 3,717 ;
- ε/c ≤ 0,795 ;
- environ 6 × 10¹⁰ tirages.

Seul effet de bord : l'égalité du défaut 8.

**Second écart, le banc témoin.** Il renforce R5. Le banc est vérifié : ε = 0,0562, nρ₀ = 100, et P*(0) ≈ 1 − 2 × 10⁻⁶, P*(ε/2) ≈ 0,052, P*(ε) ≈ 1,8 × 10⁻⁶. Chacun des trois artefacts du compteur est détecté à au moins une marge :
- lecture au seul dernier tour : détectée à m = 0 et à m = ε/2 ;
- fusion avec le dépassement : détectée à m = ε (141 comptes contre une tolérance de 5) ;
- seuil comparé à c − m : détecté à m = ε/2 et à m = ε.

Sa limite (a = 0) est traitée au défaut 4.

Le plan est monotone en la marge : 0 violation sur 138 points × 41 valeurs de λ. Avec le couplage des tirages, la décroissance de V en m est donc démontrable, et le test de Fisher de P3 n'est qu'une garde.

## Commandes lancées

- `sha256sum` sur les documents qui font foi ; `git rev-parse HEAD` ; `git log --oneline -3`.
- Validateur sur une copie : `PYTHONPATH=src python -c "from controle_ia.prereg import problemes; print(problemes('copie-prereg-v1.md'))"`. Sortie : une seule ligne, « section Contre-lecture sans les deux empreintes exigées ».
- `python -I cl/calc.py`, `cl/held.py`, `cl/mono.py` (bloc-notes). Calculs déterministes seulement, aucun tirage aléatoire : admissibilité, κ et tours tenus, règle de la note, banc témoin exact et artefacts, largeurs et puissance de Clopper-Pearson, monotonie du plan.
