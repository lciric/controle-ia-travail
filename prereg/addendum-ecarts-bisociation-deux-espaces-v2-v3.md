# Addendum d'écarts déclarés — préenregistrement de bisociation à deux espaces v2 — v3 (BROUILLON, NON SCELLÉ ; remplace le brouillon v2 `73e36970…`, gardé, lui-même remplaçant v1)

Rédigé par conv-audit (Opus 5.5), 30 octobre 2026 ; v2 à 15:59 UTC ; **v3 par conv-audit (Fable 5.1) à 23:35 UTC**, qui ajoute la section « Points déclarés par le code corrigé » (R-606) sans toucher aux décisions de Lazar ; v2 écrite après la contre-lecture du code (Opus 5.5 neuf, `experience-v2/contre-lecture-code/contre-lecture-code-experience-v2-v1.md`) et la révision de Lazar (R-600). Se rattache à `prereg/preenregistrement-bisociation-deux-espaces-v2.md` (empreinte `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea`, scellé le 30 octobre, R-581), qui reste inchangé (R12). Cet addendum ne s'applique qu'une fois scellé à son tour.

## Pourquoi un addendum

Pendant l'écriture du code, avant toute validation du générateur et toute invocation des mondes de décision, le code a relevé quatre points où le préenregistrement ne permet pas de lancer tel quel, et huit lectures à confirmer (`experience-v2/ecarts-et-questions-v1.md`, `ecarts-et-questions-v1.md.sha256`). Un écart à un préenregistrement scellé est un nœud de décision de Lazar.

**Ce qui a été lu avant ces décisions, et seulement cela** (règle R1) : des taux de plomberie (régénération, exclusion) sur des mondes d'essai aux indices 920000 à 920299 et 930000 et plus, hors de toute plage du § 7 ; et la reproduction des témoins de v1 (b, a, c, d1) sur les mondes de non-régression, exigée par la liste d'arrêt. **Aucun contraste de décision, aucune moyenne de Δ(N, ·), aucun résultat de V1 à V9 n'a été calculé ni lu.**

## Décisions de Lazar

Mots directs de Lazar, 30 octobre 2026, heure de Paris : 12:19 (R-585) « Ma recommandation : (a), confiance 0,7. ; go recos » ; puis, après la contre-lecture du code et **avant toute lecture**, 16:58 (R-600) « Je recommande « copie », confiance 0,8. : go ; Je recommande (b), confiance 0,7 : c'est l'écart le plus petit. : go ».

| Point | Écart au texte scellé | Décision |
|---|---|---|
| **Q-01** taux de régénération | **(b) Replanter sur le même monde de base** : en cas d'échec de plantation, seul le placement des ponts est retenté ; champs, articles, opérateurs et palettes du monde sont inchangés (écart à G11). Le seuil S11 reste à **2 %** pour tous les taux (exclusion, régénération complète, bras vides) ; aucun seuil ne change. Les taux de replantation et de régénération complète sont rapportés par condition et par nombre de champs. (La décision (a) de 12:19 — seuil 10 % et régénération au même nombre de champs — est remplacée.) |
| **Q-03** graine de la non-régression | § 7 : « C11, sans code de contraste » ; la clé de rééchantillonnage n'a pas de deuxième élément pour NR_bien (10) et NR_moyen (11). | **Code de contraste 16** pour la non-régression (libre dans la liste du § 7) : clé `(10, 16, 99)` et `(11, 16, 99)`. |
| **Q-04** jumelle de V4 | **Copie** : pour chaque pont planté, l'un des deux articles (règle déterministe écrite dans le code) prend les mots propres du domaine de l'autre ; mêmes latents et même flux de graines pour les rôles 1 à 3. (La lecture « échange » de 12:19 est remplacée : elle laissait le cosinus de chaque paire plantée inchangé et faisait échouer V4 par construction, contre-lecture du code.) |
| **Q-02** grille | § 5 et § 9 : grille sur 200 mondes de validation ; § 8 : N_grille parmi les descriptifs ; § 7 : aucun code de contraste. | **N_grille tourne seulement à l'étape (1) du § 9** (validation) ; ses résultats sont écrits dans le fichier de validation scellé, rapportés comme diagnostic. |
| **Q-05 à Q-12** | Lectures retenues par le code (conditions de V1 à V6, définitions complétées de V2, V3, V5, V7, tolérance bit à bit de G8 sous fuite, portée de S11, résultats par nombre de champs sans intervalle, couverture des concepts par émission, σ̂ à ddof 1, plage NR de la reproduction). | **Validées telles qu'écrites** dans `ecarts-et-questions-v1.md`. |

## Effet attendu des écarts sur le verdict

- Q-01 : la replantation est décidée avant les bras, sur les seuls latents ; les graines des bras ne dépendent pas de la tentative ; tous les bras sont notés sur les mêmes mondes (contre-lecture du code) : **aucun biais entre bras**. La population des mondes reste repondérée par la réussite de la plantation (non mesurée), ce qui peut changer la grandeur estimée et les écarts entre conditions (contrastes 14, 15, 39), non le signe d'un écart apparié. **Aucun seuil ne change.**
- Lectures signalées par la contre-lecture : Q-05 est **plus strict** que le texte (V1 exigée dans M_bien et M_moyen) ; Q-07 : la phrase de G8 sur l'égalité bit à bit des concepts de fond est fausse dès qu'il y a fuite de domaine (défaut du texte scellé, non du code ; la comparaison bit à bit porte sur les latents) ; Q-12 : la reproduction emploie RACINE_VALIDATION hors des plages du § 7 (déclaré).
- Q-02, Q-03, Q-04 : mécaniques ; aucun seuil de décision touché.

## Points déclarés par le code corrigé (v3 ; `experience-v2/LISEZMOI-experience-v2-v2.md`, R-606 ; aucun seuil touché)

Ces points sont des choix de code ou des lectures du texte scellé, relevés par le sous-agent qui a corrigé le code (Opus 5.5 neuf) ; ils sont déclarés ici pour qu'aucun ne soit découvert après lecture des résultats. Aucun n'est une décision de Lazar ; aucun ne change un seuil de décision.

| N° | Point | Déclaration |
|---|---|---|
| (v) | Plafond de replantations (Q-01 (b)) | **`MAX_REPLANTATIONS = 50`** : après 50 échecs de placement des ponts sur le même monde de base, régénération entière (tentative suivante, règle inchangée, comptée dans le taux soumis à S11 = 2 %). Graines de replantation r ≥ 1 : clé `(code, m, 0, t, r)` à cinq éléments, sans collision avec les clés du § 7. Mesure sur 33 600 mondes d'essai (indices 970000 à 972399, hors plages du § 7, seuls des comptes lus) : **0 régénération entière** ; mondes replantés de 0 % (SP) à 5,8 % par condition ; rapportés par condition et par nombre de champs, sans seuil. M_inertes replante sous le code 1 et garde donc les latents de M_bien. |
| (vi-a) | Concordance avec la vérité (déclencheur d'audit) | Grandeur définie : **part des couples (article, étiquette de concept observée) dont le concept est latent chez l'article** (F_f avec f parmi ses fonds, R_r avec r parmi ses rares, H si l'article porte le moyeu), agrégée par condition sur les mondes non exclus (`mesures_v2.concordance_verite`), écrite dans les données d'audit. Elle sert le déclencheur « concordance avec la vérité » du texte scellé, qui n'en donnait pas la formule. |
| (vi-b) | Identités déclarées d'avance | Ne déclenchent l'audit que les identités de **N** avec **N_global, N_β0 ou un témoin (b, a, d1, d1c, b_eloigne, référence c)**, comme le texte ; exceptions prévues par construction : N ≡ N_β0 dans V_concepts_absents et d1c ≡ d1 dans NR ; les autres identités sont rapportées sans déclencher. **Choix à valider par la contre-lecture R2** : si elle juge la liste trop étroite, l'élargissement se fait avant scellement. |
| (i) | Ordre d'écriture | Le fichier scellé des moyennes de validation et de la grille (étape (1) du § 9) est écrit **après** le manifeste de run ; le § 9 le place à l'étape (1) sans dire l'ordre. |
| (ii) | N_rare | Prend l'étiquette partagée **la plus rare de l'étage commun**, opérateur ou concept. |
| (iii) | Taux de bras vides | Dénominateur : **tous les mondes, exclus compris**. |
| (iv) | Lectures déjà notées | Q-05 plus strict que le texte (V1 exigée dans M_bien et M_moyen) ; Q-07 : la phrase de G8 sur l'égalité bit à bit des concepts de fond est fausse sous fuite de domaine (défaut du texte scellé, non du code ; la comparaison bit à bit porte sur les latents) ; Q-12 : la reproduction emploie RACINE_VALIDATION hors des plages du § 7. |
| (vii) | Garde d'exigence | `validation_v2` et `invocation_unique_v2` refusent de partir tant que cet addendum n'est pas scellé (`invocation_unique_v2.ADDENDUM`, à mettre au nom de la version scellée : `addendum-ecarts-bisociation-deux-espaces-v2-v3.md` si cette v3 est celle scellée) ; refus éprouvé. |

## Contre-lecture et scellement

- Contre-lecture du code par un Opus neuf : faite (`contre-lecture-code-experience-v2-v1.md`) ; ses deux désaccords (Q-01, Q-04) sont retournés à Lazar et tranchés (R-600) ; corrections de code en cours.
- Contre-lecture R2 de cet addendum (v3) par un sous-agent neuf d'un modèle différent de ses auteurs (Opus 5.5 pour v1 et v2, Fable 5.1 pour v3) : **à faire par Sonnet 5.5** ; à défaut (limite d'usage), Opus 5.5 neuf, en déclarant que v1 et v2 ont été écrites par Opus.
- Contre-lecture des corrections du code (R-606) par un sous-agent neuf : à faire ; peut être jointe à la précédente si le même agent lit le code.
- Scellement par `controle_ia.scellement sceller` (empreinte reportée dans `invocation_unique_v2.ADDENDUM`), puis validation V1 à V9, puis invocation unique ; aucune lecture de résultat avant (R1).
