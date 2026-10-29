# Reproduction de la borne de boucle de 2609.17560 (proposition 13) : rapport v1

**EXPLORATOIRE, NON PRÉENREGISTRÉ, NON OPPOSABLE (R7).** 29 octobre 2026. Sous-agent de la lignée conv-audit. Processeur seul, aucune dépense, aucun réseau. Fait suite au « go » de Lazar (29 octobre, 02:29 heure de Paris). Seule source sur le papier : `../corpus-primaire-v2/extrait-2609.17560-v1.md` (pages du PDF notées p.N). Monde synthétique : chiffres opposables à personne.

Fichiers : `reproduction-v1.py`, `reproduction-v1-sortie.json`, `manifeste-v1.json`, ce rapport, compagnons `.sha256`. Relance : `python3 -I -B reproduction-v1.py` (5 minutes, deux cœurs) ; graine 20261029, une fille par cellule (`numpy.random.SeedSequence`).

## 1. Verdict

- **Reproduit** : proposition 13 sur trafic frais, deux calendriers (p.12) ; validité sous acheminement par un juge biaisé (théorèmes 4-5, p.10) ; coût en log(1/δ_k) (p.12) ; validité sur jeu partagé **tant que les candidats ne dépendent pas du jeu** (p.12).
- **Ne tient plus, non traité par l'extrait** [INFÉRÉ] : jeu fini réutilisé **et** candidats choisis sur ce jeu. Meilleur de m variantes : 0,023 → 0,07 (m = 5), 0,18 (m = 20), 0,34 (m = 100). Exploitation des points étiquetés : 1,00 dès le deuxième audit.
- **Juge qui rend le verdict** (notre situation) : la garantie porte sur le Δ jugé, pas le vrai. Biais +0,1 pour les « lissés » : 1,00. Juge **sans biais mais bruité** (10 %) : 0,31 à 3 000 points, 1,00 à 20 000 (atténuation de Δ contre une tolérance).

## 2. Monde et règle de décision

- **Ce qui est repris de l'extrait.** Perte 0/1, B = 1. D_t = perte(candidat) − perte(titulaire) ∈ {−1 ; 0 ; 1}, Δ = E[D_t], et Δ > 0 signale une régression (p.7). Le verdict Safe(ε) affirme Δ < ε (p.8). Une **fausse certification** est un Safe(ε) émis alors que Δ ≥ ε. Les étiquettes ne sont achetées que sur les désaccords (lemme 2, p.7 ; p.8-9). L'estimateur de Horvitz-Thompson sert quand l'acheminement est aléatoire (p.9).
- **Choix de monde** [INFÉRÉ]. Binaire (désaccord ⇔ D_t ≠ 0) ; titulaire juste à 70 %, ρ = 0,20, ε = 0,05 ; **nulle de bord** (Δ = ε, pire cas), **bon** (Δ = −0,03), **nulle inversée** (Δ = +0,15) ; basculements indépendants par point, selon la justesse du titulaire ; K = 20, δ = 0,05 ; trafic frais plafonné à 3 000 points par audit (sinon, pas de verdict).
- **E-processus.** C'est notre brique `pari_apparie.trajectoire_log_richesse`, un mélange sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9}. On l'applique à v_t = (ε − Z_t)/(c + ε) ∈ [−1 ; 1], où c borne |Z_t| (c = 1, ou 1/π_min quand l'acheminement est aléatoire). Sous Δ ≥ ε, la richesse est une surmartingale positive. On certifie au premier instant où elle atteint 1/δ_k (inégalité de Ville). La version vectorisée a été comparée à la brique : écart maximal 4,4·10⁻¹⁵, instants de franchissement identiques.
- **Écart à l'extrait** [INFÉRÉ]. Discern utilise une suite de confiance de Bernstein empirique bilatérale à deux verdicts (p.8 ; forme à l'annexe A, non extraite). Ici : test unilatéral du seul Safe(ε), qui reçoit tout δ_k ; niveau 0 (certificat sans étiquette, p.8) omis, car ρ = 0,20 ≫ ε/B l'empêche de se déclencher. La validité familiale par l'union ne dépend que de la validité de chaque audit, que les deux constructions tirent de Ville.

## 3. Tableau par cellule

On compte la fréquence des suites qui contiennent au moins une fausse certification, avec un intervalle de Wilson à 95 %. Une suite compte 20 audits nuls. Sauf mention contraire : 2 000 suites, répartition égale (δ_k = 0,0025). « Puissance » : part des bons candidats certifiés, mesurée dans une suite de 20 bons. « Étiquettes » : désaccords lus jusqu'au verdict, en moyenne parmi les certifiés.

| Cellule | Fausses (suites) | Wilson 95 % | Puissance | Étiquettes |
|---|---|---|---|---|
| **A** frais, égal | 0,034 | 0,027–0,043 | 1,00 | 90 |
| **A** frais, k⁻² | 0,0315 | 0,025–0,040 | 1,00 | 115 (56 à k = 1 ; 139 à k = 20) |
| **B** partagé, n = 500 | 0,0195 | 0,014–0,027 | 0,60 | 60 |
| **B** partagé, n = 2 000 | 0,023 | 0,017–0,031 | 1,00 | 90 |
| **B** partagé, n = 2 000, k⁻² | 0,0275 | 0,021–0,036 | 1,00 | 114 |
| **C** sélection m = 5, n = 500 / 2 000 | 0,0695 / 0,070 | 0,059–0,081 / 0,060–0,082 | — | — |
| **C** sélection m = 20, n = 500 / 2 000 | 0,1585 / 0,176 | 0,143–0,175 / 0,160–0,193 | 1,00 (n = 2 000) | 61 |
| **C** sélection m = 100, n = 500 / 2 000 | 0,346 / 0,3365 | 0,325–0,367 / 0,316–0,358 | — | — |
| **C** exploitation, n = 500 / 2 000 | 1,00 / 1,00 | 0,998–1 | 1,00 (n = 2 000) | 20 |
| **D-i** trafic neuf (sélection / exploitation) | 0,031 / 0,025 | 0,024–0,040 / 0,019–0,033 | 1,00 / 1,00 | 90 ; 9 041 points neufs par suite |
| **D-ii-a** nulles **passées par la boucle**, sélection m = 20 | réels 0,155 ; alarme 0,089 | alarme 0,077–0,102 | — | — |
| **D-ii-a** nulles **figées hors boucle**, sélection m = 20 | réels 0,169 ; alarme 0,017 | alarme 0,012–0,024 | — | — |
| **D-ii-a** nulles passées / figées, exploitation | réels 1,00 ; alarme 1,00 / 0,020 | — | — | — |
| **D-ii-a** témoin : jeu partagé non adaptatif | réels 0,031 ; alarme 0,012 | alarme 0,008–0,018 | — | — |
| **D-ii-b** recalibrage par 380 nulles, sélection (400 suites) | 0,040 | 0,025–0,064 | 1,00 | lecture complète, 21 audits par audit réel |
| **D-ii-b** recalibrage, exploitation (400 suites) | 0,000 (R4) | 0–0,0095 | 0,00 | idem |
| **D-iii-a** seuil × m (m = 20), sélection | 0,0125 | 0,008–0,018 | 1,00 | 91 |
| **D-iii-a** seuil × 20, exploitation | 1,00 | 0,998–1 | 1,00 | 28 |
| **D-iii-b** e-BH pondéré, sélection / exploitation | 0,1705 / 1,00 | 0,155–0,188 / 0,998–1 | 1,00 / 1,00 | 62 / 20 |
| **D-iv** parts jamais réutilisées (100 points), sélection / exploitation | 0,009 / 0,008 | 0,006–0,014 / 0,005–0,013 | 0,04 / 0,04 | 15 |
| **E1** juge qui rend le verdict, biais +0,1 (candidats lissés) | 1,00 | 0,998–1 | 1,00 | 0 étiquette humaine ; 1 700 points jugés |
| **E2** même juge, qui n'oriente que l'acheminement (π_min = 0,5) | 0,0245 | 0,019–0,032 | 1,00 | 118 (731 points) |
| **E3** juge bruité symétrique (10 %), verdict (500 suites) | 0,31 à 3 000 points ; 1,00 à 20 000 | 0,27–0,35 ; 0,99–1 | — | — |

- **Coût contre log(1/δ_k)** (A, k⁻²). Ajustement linéaire : 14,1 étiquettes par unité de log(1/δ_k), R² = 0,998, sur des log(1/δ_k) allant de 3,5 à 9,5.
- **Gonflement par audit sous sélection**, comparé au taux nominal mesuré en B (0,0012 par audit) : environ × 3,3 pour m = 5, × 9,6 pour m = 20 et × 26 pour m = 100. Chaque fois, c'est sous la borne d'union sur les variantes, m·δ_k, soit 0,0125, 0,05 et 0,25 par audit. **La taille du jeu ne change presque rien** (n = 500 ou 2 000). Le biais de sélection et le pouvoir de détection de l'e-processus évoluent tous deux à l'échelle 1/√n [INFÉRÉ].
- **Sous exploitation, un jeu plus grand aggrave les choses.** Au deuxième audit, le taux de fausse certification vaut 0,49 pour n = 500 et 0,998 pour n = 2 000 : chaque audit sans verdict lit tout le jeu et y achète plus d'étiquettes, qui fuient vers la boucle. Le premier audit reste nominal (0,0015 et 0,002).

## 4. Ce qui est reproduit, ce qui est inféré

**Reproduit, page de l'extrait citée :**
1. Validité familiale sur trafic frais, avec répartition égale (horizon connu) et avec δ_k ∝ k⁻² (suite non bornée) : proposition 13, p.12. Cellules A.
2. « Each successive audit is more expensive by only a log(1/δ(k)) factor » (p.12, renvoi au théorème 7) : la croissance est linéaire en log(1/δ_k). Cellule A, k⁻².
3. Sur trafic partagé, la validité familiale tient par l'union, « needs no independence between audits » (p.12) : vérifié **pour des candidats choisis sans regarder le jeu**. Cellules B. Sur jeu fini, on observe une baisse de puissance : 0,60 à n = 500, faute de points. Ce n'est pas exactement la dégradation « des audits concurrents » dont parle l'extrait.
4. Un juge biaisé ou adversarial « can waste budget but cannot break coverage » (p.9 ; théorème 5, p.10 ; zéro violation, p.21) : 0,0245 de fausses certifications, mais 31 % d'étiquettes en plus que sous un acheminement constant (118 contre 90). Cellule E2.
5. Les chiffres du papier (p.1) ne sont ni visés ni reproduits.

**Inféré, au-delà de l'extrait :**
- Cellules C, D, E1 et E3, ainsi que tous les choix de monde de la section 2.
- **Lecture du commentaire de la proposition 13.** La phrase sur le partage du trafic (p.12) suit immédiatement celle qui permet un choix « fully adaptively » de l'audit k. Lue sans réserve, elle couvrirait le cas C, et C la contredit. L'extrait justifie la validité conditionnelle de chaque audit par la fraîcheur du trafic (« which is what lets audit k's increments be conditionally valid given H_k »). La lecture la plus probable est donc que la phrase vise des audits concurrents non adaptatifs. La preuve (annexe B) n'est pas extraite : **on ne conclut pas que le papier se trompe** (R8). On conclut que la réserve « candidats indépendants du trafic partagé » est nécessaire et qu'elle n'est pas écrite dans l'extrait.
- **Remède iii-a** : il est valide sous sélection parce qu'une certification de la variante choisie implique celle d'au moins une des m variantes (union sur les variantes). Cela suppose que les m variantes soient tirées sans le jeu et que m soit compté en entier.
- **Remède ii-b** : borne conformale par échangeabilité. Si les nulles de bibliothèque sont échangeables avec les réels nuls, la probabilité qu'un des K réels dépasse le maximum des L nulles vaut au plus K/(K + L) = 0,05 pour L = 380.

## 5. Ce qui est à nous, ce qui est à eux (pour Q2)

**À eux, à ne pas revendiquer :**
- La borne de boucle par union sur une suite adaptative d'audits, sur trafic frais, à budget unique.
- Le calendrier en k⁻² et le coût en log(1/δ_k).
- La validité sous trafic partagé quand les candidats ne sont pas adaptatifs.
- La validité sous acheminement adversarial.
- Notre famille à m déclaré d'avance, lue par e-BH, équivaut à leur répartition égale (déjà noté : `anteriorite-Q2-v2.md`, section 5).

**À nous : des questions, pas des trous (R8)**, chacune mesurée ici sur un jouet :
1. **Jeu figé réutilisé avec boucle adaptative.** La borne d'union ne protège plus. Le gonflement est borné par m·δ_k sous sélection parmi m variantes, et non borné sous exploitation des points vus. Quantifier ce régime et lui associer des remèdes, voilà ce qui n'est pas dans l'extrait.
2. **Nulles de bibliothèque.** Elles ne servent que si elles **passent par la boucle**, à l'aveugle. Figées hors boucle, elles restent nominales (alarme 0,017) alors que les réels sont gonflés (0,169) : elles ne voient rien. Passées par la boucle, elles détectent l'exploitation à coup sûr (alarme 1,00) et la sélection partiellement (0,089). Pour **recalibrer** au niveau familial, il faut de l'ordre de K/δ nulles, soit 380 pour 20 audits et 21 fois le coût des audits. Ça marche sous sélection (0,040 ; puissance 1,00), mais c'est dégénéré sous exploitation (puissance 0).
3. **Juge qui rend le verdict.** C'est la différence de fond avec leur section 6.6 : chez eux, le juge n'oriente que l'acheminement et la vérité reste achetée. Ici, la garantie vaut « sur le jeu du juge ». Un biais dépendant du candidat la renverse (E1). Un bruit symétrique suffit aussi, parce qu'il atténue Δ en (1 − 2e)Δ et que Safe(ε) avec ε > 0 est une affirmation de tolérance (E3). L'atténuation par l'erreur de mesure est un fait statistique connu ; son effet sur un certificat de tolérance lu par un juge reste une question.

**Conséquence pratique pour le pôle** [INFÉRÉ] :
- Contre la sélection, le remède le moins cher est le seuil multiplié par le nombre de variantes essayées contre le jeu : 0,0125 de fausses certifications, puissance 1,00, 91 étiquettes. Il exige de **compter honnêtement toutes les variantes** que la boucle a confrontées au jeu, y compris en interne. C'est difficile avec une boucle de modèles de langage.
- Contre l'exploitation, seules les données jamais vues protègent. Le trafic neuf coûte environ 9 000 points par suite contre 2 000 réutilisés. Le découpage en parts protège mais tue la puissance : 0,04 avec 100 points par part.
- La lecture e-BH ne corrige rien (0,17) : elle suppose des e-valeurs valides une à une.

## 6. Garde R4

- **D-ii-b sous exploitation : 0 fausse certification sur 400 suites, signalé TROP PROPRE.** La cause est identifiée : après une vingtaine d'audits, tous les points où le titulaire se trompe sont connus. Tous les candidats, nuls ou bons, ont alors la même trajectoire, donc le même pic, et un réel doit dépasser **strictement** le maximum des nulles. Les ex æquo empêchent toute certification. La borne tient, mais la procédure ne certifie plus rien (puissance 0). Ce 0 n'est pas une preuve de qualité.
- **C sous exploitation (1,00) et E1 (1,00) : propres dans l'autre sens.** L'attaque est maximale par construction : mémorisation parfaite des points étiquetés, que l'ordre de lecture fixe place en tête. Une attaque plus faible donnerait une valeur intermédiaire. C'est une borne haute, pas une estimation.
- **D-iv (0,009 ; 0,008)** : bas par impuissance (100 points), non par une garde.
- A, B (0,0195 à 0,034) et E2 (0,0245) ne sont pas suspectes : le mélange sur Λ et le plafond rendent Ville prudente (0,0017 par audit pour 0,0025 en A).

## 7. Limites

- **Monde de Bernoulli** binaire, basculements indépendants, un seul jeu de valeurs (ε, ρ, exactitude) ; ni monde gaussien ni dérive (p.13).
- **Aucun juge-modèle réel** : bruit simulé ; titulaire jugé sans erreur dans E1.
- **Règle d'arrêt** : test unilatéral par pari au lieu de la suite de confiance de Bernstein empirique bilatérale de l'extrait ; niveau 0 omis.
- **Adaptation** : sélection sur la moyenne du jeu entier, la boucle voyant tout le jeu, et exploitation par mémorisation parfaite. La fuite plus faible, une adaptation par les seuls verdicts, n'est pas simulée.
- **Taille** : 2 000 suites (400 au recalibrage, 500 en E3), K = 20, plafond de 3 000 points (20 000 en E3).
- **Briques modifiées en cours de session** : `pari_apparie.py` et `porte_pace.py` ont été modifiés par une autre session (version 40 : refus des valeurs non finies) entre deux exécutions. La sortie JSON est identique, à l'empreinte près, avant et après. Le manifeste prend désormais les empreintes au lancement et signale toute modification survenue pendant l'exécution.
- Non opposable (R7) ; emprunter la proposition 13 dans Q2, avec la réserve « candidats non adaptatifs », demande un préenregistrement scellé (R1).
