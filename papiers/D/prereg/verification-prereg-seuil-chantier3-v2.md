# Vérification des corrections (contre-lecture 2, R2) du préenregistrement de l'épreuve de la garantie de seuil — v2

- Contre-lecteur : le même qu'à la contre-lecture 1, sous-agent Opus 5.5, qui n'a écrit ni le texte ni le script. Date : 2026-11-24.
- Pièce relue : `prereg-seuil-chantier3-v2.md`, empreinte `bd58748a8ac83f2757e551e344d0c3f3474c4626d712267af2eea2050aaa4085`, vérifiée sur disque. Premier rapport : `contre-lecture-prereg-seuil-v1.md`, `841171cc…`.
- Garanties : aucun fichier modifié, rien de lancé, aucun tirage. Seuls des calculs exacts ont été faits, sur une copie.

## Verdict

**Non scellable en l'état : une seule correction suffit.**
Les treize défauts de la v1 sont corrigés, douze entièrement et le défaut 12 en partie. Les ajouts se vérifient, et tous les chiffres des bancs témoins se recalculent à l'identique.

Un nouveau défaut reste. Sur le banc témoin, la garde du compteur de l'écart bilatéral ne peut pas détecter son propre artefact, « écart compté d'un seul côté ». Tel qu'il est écrit, le texte ferait donc s'arrêter la course par sa propre règle d'arrêt n° 2, avant tout tirage de la grille. On y échapperait seulement par un écart à un texte scellé.

Une fois ce point corrigé (défaut R1 ci-dessous), le texte est **scellable**. Il ne garde alors que des réserves mineures, R2 à R4.

## Sort des défauts de la v1

| N° | Défaut | Sort |
|---|---|---|
| 1 | Objet éprouvé : l'étape de preuve et non l'énoncé | **Corrigé.** Les trois énoncés (E), (C) et (A) sont justes. L'étape unilatérale est bien aux lignes 411 à 414. Le processus plafonné est conforme à l'arrêt des audits à B_rand. Le verdict est gradué. L'invariant entre violations est juste : à mêmes tirages, x̂' ≥ x̂, et le plafond P = ⌊B_rand⌋ ne mord que si N > B_rand. |
| 2 | Contrôle (4) faux pour m > 0 | **Corrigé.** p₁(m) = P(A < nρ_κ − n(m+τ)/(γW)) est exacte, puisque x̂_{κ+1} − c = γW(ρ_κ − A_κ/n) − m. |
| 3 | Audit sans tolérances ; racine de relance non fixée | **Corrigé.** Les tolérances sont chiffrées et raisonnables : 5 erreurs types ; variance à 3 %, soit environ 6,7 erreurs types à R = 10⁵. L'entropie de relance est fixée ; pas de troisième course sans Lazar. |
| 4 | Audit à sens unique ; témoin aveugle à la mémoire | **Corrigé.** Contrôles systématiques en tout point ; ε recalculée par la forme fermée ; deux témoins à mémoire ajoutés. |
| 5 | Prolongation contradictoire | **Corrigé.** La règle est unique et exhaustive. |
| 6 | Lecture ambiguë à λ = 0 | **Corrigé.** Trois cases disjointes et exhaustives sur la classe finale ; l'ordre de priorité est écrit. |
| 7 | Risque d'ensemble | **Corrigé.** Recalcul : 138 × 10⁻⁴ = 1,38 % ; 2 × 138 × 10⁻⁴ = 2,76 % ; 276 × 10⁻⁴ = 2,76 % ; 690 × 10⁻⁵ = 0,69 %. Une fausse réfutation exige une prolongation classée à tort, d'où au plus 10⁻⁴ par point. |
| 8 | Égalité à η = ∞ | **Corrigé.** κ est défini avec τ : le minimum de K − 1 − κ(0) vaut bien 24. Entre le plan clos et le plan glouton, l'écart est d'au plus 2 × 10⁻¹⁵, sous 10⁻⁹. |
| 9 | Latitude de la bissection | **Corrigé.** Estimateur et non décision ; deux conditions de validité ; ensemble de lecture d'au moins 125 points. |
| 10 | Prédictions non réfutables | **Corrigé.** |
| 11 | Graines | **Corrigé.** Voir la réserve R3. |
| 12 | Gardes des arrêts 4 et 5 | **Corrigé en partie.** Les gardes sont ajoutées. Celle de la sensibilité à τ se vérifie : l'artefact déplace le compte d'environ 1 388 répétitions, pour un seuil de 10. En revanche, une garde nouvelle, celle de l'écart bilatéral, n'est pas éprouvable (R1). |
| 13 | Références | **Corrigé.** Lignes 364 à 393, et preuve aux lignes 395 à 423, exactes. Le commit `67f0b2df` existe et est la tête de branche. |

## Recalculs des ajouts (arithmétique exacte, sans tirage)

**Témoin à mémoire entière** (a = 1, K = 12, n = 100, c = 1,2).
- ε = 0,58553.
- Plans : κ = 6, 4, 3 aux trois marges.
- Par programmation dynamique sur le compte cumulé : P*_V = 0,751, puis 3,242 × 10⁻³, puis 1,22 × 10⁻⁷ ; P*_O = 6,26 × 10⁻⁴, puis 8,68 × 10⁻⁴, puis 7,29 × 10⁻⁴. Au plafond du théorème, V' est égale à V aux arrondis près.
- La contrainte finale exige N ≥ 120. Avec un plafond d'épreuve de 118, on a donc toujours x̂'_K ≥ 1,22 > c, et V' = 1 exactement aux trois marges.
- L'artefact « plafond par tour » (118 > n) et l'artefact « plafond ignoré » sont détectés.

**Témoin à mémoire partielle** (a = 0,5, K = 3, n = 1000, c = 0,175).
- Γ_K = 1,3125 et ε = 0,053326 ; avec Σaⁱ à la place de Σa²ⁱ, on obtiendrait 0,061082.
- Par énumération : P*_V = 0,7993, puis 0,01622, puis 4,69 × 10⁻⁶.
- Les artefacts « a mis à 0 » sont détectés sur les deux témoins. Sans mémoire, V tombe à 0 pour a = 1 et à environ 0,47 pour a = 0,5.

**Règle de prolongation, cases à λ = 0, priorités, risques** : justes, et sans contradiction entre elles.

## Défauts restants

**R1. Majeur. La garde du compteur de l'écart bilatéral ne peut pas réussir son épreuve** (section Gardes, ligne « Compteurs de la violation plafonnée et de l'écart bilatéral »).
- Sur le témoin sans mémoire, à m = ε, la vérité vaut D* = 2,67 × 10⁻⁵, soit 2,7 comptes attendus sur 10⁵. La tolérance est de 11,2 comptes.
- L'artefact « un seul côté » donne 0,18 compte pour le côté haut et 2,49 comptes pour le côté bas. Il passe donc la garde, qui ne se déclenche pas sur son artefact : la règle d'arrêt n° 2 arrête la course.

Correction proposée : éprouver le compteur, sur ce témoin, avec un seuil d'épreuve ε/2 au lieu de ε, soit |A − nρ_ε| > nε/(2γW), la vérité exacte restant calculée par la même formule.
- Vérité : 0,2552, soit 25 517 comptes.
- Côté haut seul : 0,1292 ; côté bas seul : 0,1437. L'écart vaut 11 000 à 12 600 comptes, pour une tolérance de 692.

La garde au seuil nominal ε reste comme cas sain.

**R2. Mineur. Le rôle de l'écart bilatéral dans le verdict « tient » n'est pas univoque** (table à λ = 1 et verdict d'ensemble).
Le verdict d'ensemble « tient » n'exige que V et V'. Mais la ligne « une classe non concluant sans réfutation », jointe à l'ordre de priorité, rend « non concluant » un point où seul l'écart bilatéral est indéterminé après prolongation.
Correction : écrire si la classe de l'écart bilatéral entre ou non dans le verdict sur (E) et (C). Recommandation : non. Elle est alors rapportée à part, comme son verdict.

**R3. Mineur. Deux précisions manquent sur l'audit renforcé et le bloc 8.**
- Le contrôle 2 renforcé, déclenché par une réfutation, compare à « la fréquence de la course » sans dire laquelle : premier tirage ou prolongation. Recommandation : la prolongation, puisque c'est elle qui porte la réfutation.
- Le bloc 8 tire épisode par épisode, alors qu'« un lot est un seul appel binomial ». Il faut préciser qu'au bloc 8, un lot est un tableau de Bernoulli de taille (répétitions, K, n).

**R4. Mineur. Le scellement doit être vérifié.**
Entre la v2 relue et le texte scellé, seule la section « Contre-lecture » doit changer. Si R1 est corrigé, la version scellée diffère de `bd58748a…`. La contre-lecture 2 doit alors citer l'empreinte de la version relue, et la mère vérifie, par une comparaison des deux textes, que seuls le point R1 et la section « Contre-lecture » ont changé.

Plus aucune latitude après lecture des résultats, hors R2. Aucune issue n'est laissée sans verdict écrit.

## Validateur

Sur la copie `copie-prereg-v2.md`, `controle_ia.prereg.problemes` ne renvoie qu'une ligne : « contre-lecture 2 sans ses deux empreintes (brouillon relu et rapport) ». C'est attendu.

Empreintes à porter dans l'entrée « Contre-lecture 2 » :
- brouillon relu : `bd58748a8ac83f2757e551e344d0c3f3474c4626d712267af2eea2050aaa4085` (v2) ;
- rapport : l'empreinte SHA-256 du présent fichier, `verification-prereg-seuil-v2.md`, calculée après son écriture et transmise à la mère.

Si une v3 corrige R1, son empreinte est à ajouter, avec la mention « correction R1 vérifiée par comparaison des deux textes ».

## Commandes lancées

- `sha256sum` sur la v1, la v2 et le premier rapport ; `git rev-parse HEAD` ; `git cat-file -t 67f0b2df` ; `sed` sur les lignes 395 à 424 du `.tex`.
- `python -I cl/v2.py` : programmation dynamique du témoin à mémoire entière, énumération du témoin à mémoire partielle, D* du témoin sans mémoire.
- `python -I cl/dside.py` et `cl/dfix.py` : les deux côtés de l'écart bilatéral, et un seuil d'épreuve de remplacement.
- `python -I cl/tau.py` : effet de l'artefact de tolérance.
- Validateur sur la copie : `problemes('copie-prereg-v2.md')`.
