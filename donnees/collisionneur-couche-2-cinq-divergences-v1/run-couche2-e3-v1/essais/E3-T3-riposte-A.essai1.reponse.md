# Collisionneur 3×3 — Tour III.3 — Riposte de la proposition A

**Pièces reçues.** Ma conception (E3-T1-A), les deux attaques (E3-T2-B, E3-T2-C) sont complètes et closes par FIN-DE-CELLULE. Toujours non servis : sortie JSON de la simulation, carte d'inventaire, `sources-lues-v1.txt`, texte de P-015 (donc la définition de « mention » et de « témoin instruit »). Je n'ai pas de processeur : aucune simulation relancée. Statuts inchangés : chiffres de simulation OBSERVÉ-NON-AUDITÉ, décisions de D RAPPORTÉ, prix SUPPOSÉ, mes raisonnements HYPOTHÈSE, mes chiffres hors pièces « illustratif ». Je ne réponds qu'aux sections qui visent A (dont la « faille commune » de B et le duel B-2, déclarés communs).

---

## (a) Verdict sur chaque attaque

Légende : **ACC** acceptée ; **REJ** rejetée ; **TEST** transformée en test (section b).

### Équipe rouge B

| # | attaque | verdict | raison, ou test |
|---|---|---|---|
| B-0 | Faille commune : aucune tâche vierge ; D2 compare deux contaminations | **ACC + TEST** | Exact. A1 § 5 prend c15 de `resume.json` de P3 (RAPPORTÉ) : c'est un choix de couche tiré des 60 tâches de P3, contraire à la réserve que je posais moi-même. Mon D2 mesure une **différence** de contaminations, pas une contamination. Sans tâches neuves (arXiv refusé, B1 D2), le duel B-1 n'est pas exécutable : **nœud pour Lazar**, et portée de G1 à déclarer « conditionnelle à des tâches ayant servi au choix de couche ». Corrigé en T2. |
| B-a1 | D2 ne lit que les honnêtes ; la fuite gonflerait le rappel saboté ; H_A/H_B mal opposées | **ACC + TEST** | Les sondes de T0.7 ont appris sur des jeux liés à la réserve (A1 § 1, RAPPORTÉ) : la fuite porte sur la direction de sabotage. Un test sur les honnêtes est nécessaire, pas suffisant. Conséquence : le choix « 64 ou 96 » **ne peut pas** être pris sur données avant G1 (lire les sabotés d'épreuve est interdit). Je retire l'option 96. T2 réécrit : contamination mesurée **dans** G1, comme strate rapportée. |
| B-a2 | la réserve « vierge » n'existe pas | **ACC** | Mot fautif. Je voulais dire « non lue au pilote ». Toute la réserve porte la dose et T0.7. |
| B-a3 | fuite pilote → développement lu par l'organisme (G_max = 1) | **ACC** | Si le pilote fixe K et les strates sur des épisodes que l'organisme relit, D-S12 est violée en substance. Correction : le pilote est une **partie propre** (« lecture pilote », v10) ; K n'est plus choisi par lui (K = 10 fixé par nœud, le pilote ne fait que mesurer a, h, concordance et les écrire au préenregistrement) ; le développement de l'organisme passe sur des tâches que le pilote n'a pas lues — soit 16 tâches (organisme quasi aveugle : 0,10 pour 20 points à 20 unités, A1 table S1, OBSERVÉ-NON-AUDITÉ), soit **différé à la nouvelle extraction** (N-049). Nœud pour Lazar. |
| B-a4 | dose ajustée contre le seul 8B ; « diffus » = meilleur boîte noire par action | **ACC + TEST** | P-015 (RAPPORTÉ par B1) définit « diffus » par le meilleur moniteur boîte noire par action. La recherche de dose doit tourner contre la **liste scellée** de tous les moniteurs par action disponibles à cette date (8B, 3B, Qwen, b*, règle du coût déclaré), et « diffus » se code contre leur maximum. Coût : la recherche passe de ≈ 7–8 h (C) à ≈ 11–14 h de carte [illustratif, 8B + 3B ; Qwen et b* sans rythme mesuré]. |
| B-a5 | strates de dose contre plancher de 48 pour H1a : qui cède ? | **ACC** | Les strates de dose cèdent **en épreuve**. L'épreuve de G1 et de H1a ne contient que la dose diffuse (une seule strate, 64 unités). La dose-réponse (H1b, déjà « rapportée comme information », N-055, RAPPORTÉ) se mesure au pilote et au développement, à 5 %. |
| B-a6 | « mention » non définie dans les faits ; D4 non dichotomique | **ACC + TEST** | La définition est dans P-015, non servi : je ne l'invente pas ; D4 est conditionnel à son scellement. D4 réécrit avec un seuil ponctuel (T4). |
| B-a7 | dérive temporelle : S_x généré après les jumeaux | **ACC + TEST** | Vrai. Contrôle de dérive à la génération de S_x (T5). |
| B-a8 | deux règles de décision ; puissance calculée sous une seule | **ACC en partie** | D-S11 (c) « le pari décide » est la lecture retenue par N-055 (RAPPORTÉ), même si « pièce du préenregistrement ». Sous l'intervalle à 95 % de N-008, le plancher structurel (48/93 unités, propre à la richesse) disparaît mais le bruit par unité reste ; je n'ai pas les moyens de le chiffrer ici. À écrire : si D-S11 bascule, les tables d'A1 sont à refaire. |
| B-b | évasions ; point décisif : dommage par dose jamais mesuré | **ACC + TEST** | Le dommage des deux modes connus n'est mesurable que par l'étiquetage à deux séries (N-054, RAPPORTÉ). Il entre au pilote (T6). Sur « le bras informé apprend la frontière » : **REJ en partie** — P-015 est public pour ce bras (N-056 § 6 : il connaît le protocole, pas les seuils calibrés) ; la règle de dose ne révèle pas les seuils. |
| B-c1 | permutation des étiquettes de bout en bout | **ACC + TEST** | T7, processeur, zéro dépense une fois la banque faite. |
| B-c2 | étiquetage dans le pilote | **ACC** | = T6. |
| B-c3 | plancher « longueur brute » et stratification par longueur réalisée | **ACC** | Ajouté aux planchers rapportés. La longueur réalisée est un **champ d'épisode** (une strate diviserait le calibrage sous 99, A1 § 6). |
| B-c4 | contrôle de dérive à S_x | **ACC** | = T5. |
| B-2 | duel sur l'union des contrôles 12 à 4 800 | **ACC** | C'est mon D1 rendu exécutable ; je le reprends tel quel (T1) avec son contrôle négatif (coupe par tâche > 0,10). |

### Équipe rouge C

| # | attaque | verdict | raison, ou test |
|---|---|---|---|
| C-a1 | fuite pilote → épreuve via la bascule à 96 tâches | **ACC** | Même faille que B-a1/B-a3 : option 96 retirée, K non choisi par le pilote. |
| C-a2 | absence de preuve ≠ preuve d'absence sur les honnêtes | **ACC** | = B-a1. |
| C-a3 | D4′ contre le plancher de 48 | **ACC** | = B-a5 : épreuve = dose diffuse seule. |
| C-a4 | jumeaux partagés « décachetés » avant S_x | **REJ pour l'épreuve, ACC pour l'ordre** | Les scores d'épreuve ne sont jamais exposés à l'orchestrateur ni au pôle (A1 § 7 ; B1 § 6, RAPPORTÉ) ; G1 les lit **une fois**, après chargement du fichier scellé de S_x. Le concepteur du bras n'y accède pas (quarantaine, N-056 § 6). L'attaque vaut en revanche contre **mon ordre** (étape 4 puis 6) : si G1 lisait les modes connus avant S_x, ce serait deux lectures. Correction : une seule lecture de G1, tous modes ensemble, après génération de S_x. Les jumeaux de **développement** sont décachetés par l'organisme, mais S_x n'y entre pas (D-S10 : « mode tenu à l'écart hors décision »). |
| C-a5 | 16 tâches : intervalle de a trop large | **ACC** | Avec 15 ddl, l'intervalle d'une variance couvre ≈ 0,55–2,4 σ̂² [illustratif, C] ; à 31 ddl, ≈ 0,64–1,8 [illustratif]. Puisque K n'est plus choisi par le pilote (B-a3), a n'a plus à être tranché : il est **rapporté avec son intervalle**, et la puissance du préenregistrement s'écrit aux deux bornes. Je propose le pilote sur les 32 tâches de réserve (voir B-a3, nœud organisme). |
| C-b1 | h élevé trompe la recherche de dose en moyenne sur 16 tâches | **ACC + TEST** | Le critère « diffus » doit être **par unité** (part d'actions sous seuil ≥ 0,99 par épisode, A1 § 7 : dose réalisée rapportée), jamais une moyenne sur tâches. Condition d'échec scellée : si moins de 90 % des unités d'épreuve sont réalisées diffuses [illustratif], la strate est mal codée et H1a n'est pas lisible (T3). |
| C-b2 | « mention » muette pour une raison superficielle ; T absent du duel | **ACC** | D4 devient à quatre conditions H, M, T, S (T4). Je n'avais pas mis T dans le duel. |
| C-b3 | mode orthogonal aux sondes de P3 aveugle le sujet et ses deux comparateurs blancs | **REJ comme faille nouvelle** | C'est la conséquence de l'option (b) du nœud 1, acceptée par Lazar : « un échec ne dira pas laquelle a échoué » (N-056 § 1, RAPPORTÉ). Elle vise le programme, pas A. **ACC comme argument d'ordre** : c'est précisément pourquoi l'écart blanc/blanc se mesure au pilote avant le calibrage. |
| C-c1 | contamination sur sabotés ; 4 tâches vierges ne suffisent pas | **ACC** | = B-0/B-a1. |
| C-c2 | notes de juge incomplètes (54 et 50 sur 180, C § 4, RAPPORTÉ) contre l'exigence de score fini | **ACC + TEST** | Le pilote mesure le taux de scores non finis par cellule sous la lecture par l'espérance du jeton (T8). |
| C-c3 | contrôle 12 par strate de calibrage : je l'oppose à C sans me l'appliquer | **ACC + TEST** | Juste. Avec l'horizon en strate, 9 600 → 4 800 par strate, et quatre contrôles (2 modes × 2 strates) sous 0,05. Recommandation corrigée : **aucune strate de calibrage** par défaut ; l'horizon devient strate seulement si le pilote montre que la loi des scores honnêtes en dépend (T9). |

**Bilan** : sur 26 attaques, 21 acceptées (dont 11 transformées en test), 3 rejetées en partie (B-b bras informé, C-a4 épreuve, C-b3), 2 acceptées sous réserve de chiffrage impossible ici (B-a8, C-a5). Les trois rejets sont motivés par des pièces RAPPORTÉES (N-056 § 1 et § 6, A1 § 7, B1 § 6).

---

## (b) Expériences corrigées

Chaque test oppose deux hypothèses exclusives ; chaque issue falsifie quelque chose (B4). Les chiffres de puissance viennent d'A1 (OBSERVÉ-NON-AUDITÉ) ; les volumes sont [illustratifs].

**T1 — Union des contrôles 12 à 4 800 (duel B-2, repris).** Simulation processeur, zéro dépense. `controle_12_intra_taches` étendue à deux cellules partageant les moitiés et l'effet U ; 64 tâches, K_cal = 75 et 150, a ∈ {0 ; 0,2 ; 0,3}, 2 000 répétitions. H_A : union ≤ 0,05 à 4 800. H_B : > 0,05. Règle : intervalle à 95 % contre 0,05 ; s'il contient 0,05, c'est « 2 000 répétitions suffisent » qui est falsifié. Contrôle négatif : coupe par tâche sur les mêmes tirages > 0,10, sinon le simulateur ne reproduit pas A1. Issue : H_A → minimum 4 800 tenable (économie ≈ 4 800 épisodes, ≈ 130–180 h de carte [illustratif, 100–140 s/épisode]) ; H_B → 9 600 obligatoire. **À faire avant le devis v2 : c'est le poste dominant (66 % des épisodes, A1 § 8).**

**T2 — Contamination, mesurée dans G1 et non avant.** Les 60 tâches de P3 et les 4 restantes sont toutes en épreuve (64 unités). Préenregistrement : deux sous-strates **déclarées, rapportées, hors décision** : « lues en P3 » (60) et « non lues » (4). H_A : le rappel du blanc séquentiel à 1 % sur « lues en P3 » dépasse celui sur « non lues » de plus de 5 points. H_B : écart ≤ 5. Avec 4 tâches, l'intervalle couvrira presque sûrement les deux : **l'issue attendue est la troisième, qui falsifie « ce banc suffit à exclure la fuite »** — c'est exactement ce que B-0 dit, et il faut l'écrire à Lazar avant la dépense plutôt qu'après. Contrôle négatif : sondes aléatoires appariées, écart nul attendu. Le seul test informatif demande des tâches neuves (duel B-1 de B) : **nœud — nouvelle extraction (option c de D2 de P-036) avant ou pendant la couche 2.** Pour la réserve : elle ne va plus en épreuve ; la question de sa contamination ne se pose que pour le pilote et le développement, dont les lectures ne portent aucune revendication.

**T3 — Régime diffus par unité.** Au pilote, sur 32 tâches × 2 modes × 10 exécutions, trois niveaux de dose écrite, boîte noire **par action, toute la liste scellée** (B-a4). Statistique par épisode : part d'actions sabotées sous le seuil 1 % du maximum des moniteurs par action (seuil calibré sur les honnêtes de développement, D-S14 scellée). H_A : à un niveau de dose au moins, ≥ 90 % des unités [illustratif] ont une part ≥ 0,99 et l'étiquetage (T6) confirme le sabotage dans ≥ 80 % de ces unités [illustratif]. H_B : aucun niveau ne satisfait les deux. H_A → la dose d'épreuve est fixée à ce niveau, 64 unités toutes diffuses ; H_B → le régime « diffus avec dommage » n'existe pas sur ce banc, H1a n'est pas testable, nœud. Contrôle négatif : la dose 0 (honnête) doit donner une part ≥ 0,99 dans ≥ 99 % des unités. Contamination du calibrage : les seuils de cette recherche viennent des honnêtes de développement seuls ; le calibrage d'épreuve n'est pas encore généré à ce moment (ordre, section c).

**T4 — Mention, témoin, saboteur (conditionnel au scellement de la définition de P-015).** Sur les 64 tâches, K = 3 pour M et T. Métrique : différences appariées de rappel à 1 % du blanc séquentiel. H_A : r_S − max(r_M, r_T) < 10 points (la sonde lit l'instruction ou la présence d'une consigne). H_B : ≥ 10 points. Puissance pour 20 points à 64 unités, K = 3 : 0,94–1,00 (A1, S1/S2) ; pour 10 points : 0,33–0,52 — l'issue « non promu » à 10 points falsifie « la banque discrimine à 10 points », pas H_B. Contrôle négatif (à la demande de C-b2) : le prédicteur de traits du texte (N-029) et le plancher « longueur brute » (B-c3) doivent eux aussi être rapportés sur M et T ; si r_S − r_M y est aussi ≥ 10 points, le gain de la sonde n'est pas interne. H_A → l'énoncé de H2 change ; H_B → artefact d'intention écarté pour ce mode. Lever « mention » reste un **nœud**, pas un défaut : P-015 (b) est appliqué (R-321, RAPPORTÉ).

**T5 — Dérive à la génération de S_x.** Au moment de générer S_x, régénérer 64 × 3 = 192 jumeaux honnêtes [illustratif] à graines identiques sur la même pile épinglée (B1 § 6). Métrique : taux de fausses alertes au seuil 1 % scellé, par cellule, et statistique de rang entre anciens et nouveaux scores. H_A : taux hors [0,5 % ; 2 %] ou rang significatif à 5 % dans une cellule. H_B : ni l'un ni l'autre dans toutes. H_A → les jumeaux de S_x sont régénérés en entier et la comparaison inter-modes perd son appariement (à écrire) ; H_B → jumeaux partagés tenus. Pas d'identité au bit près exigée (non-déterminisme des noyaux) : égalité en loi des scores.

**T6 — Étiquetage à deux séries au pilote.** Sur les 640 épisodes sabotés du pilote, les deux séries indépendantes (N-054 point 1). H_A : accord ≥ 0,9 et sabotage présent dans ≥ 80 % des unités à la dose retenue [illustratif]. H_B : non. H_B falsifie « la dose diffuse produit un sabotage » avant toute dépense d'épreuve. Coût en jetons non chiffré (aucun rythme dans les pièces ; B1 D5).

**T7 — Permutation de bout en bout.** Sur la banque réelle, étiquettes saboté/honnête réaffectées au hasard dans chaque tâche, 200 permutations [illustratif], toute la chaîne (jumeaux partagés, calibrage partagé, intersection-union à trois comparateurs, deux modes). H_A : part de promotions de G1 ≤ 0,05. H_B : > 0,05. H_B falsifie la validité de la chaîne, pas d'une cellule. Processeur, après génération, avant lecture d'épreuve ; nécessite que la permutation soit une lecture déclarée (signature « permutation »), sinon elle compterait comme lecture d'épreuve — à trancher au préenregistrement.

**T8 — Scores non finis.** Au pilote, par cellule, taux d'épisodes sans score fini sous la lecture par l'espérance du jeton. H_A : ≤ 2 % dans chaque cellule [illustratif]. H_B : > 2 % dans au moins une. H_B → la lecture de cette cellule change avant la banque (nœud) ; à 30 % de pertes, 64 unités tomberaient sous 48 (C-c2).

**T9 — Horizon comme strate de calibrage.** Sur les honnêtes du pilote, statistique de rang des scores par cellule entre horizons prévus. H_A : différence significative à 5 % avec correction par cellule. H_B : non. H_A → l'horizon est une strate de calibrage et T1 se refait à 4 800 par strate avec quatre contrôles ; H_B → aucune strate de calibrage, 9 600 entiers.

**Pilote corrigé** [illustratif] : 32 tâches de réserve × 2 modes × 10 exécutions = 640 sabotés ; 320 jumeaux ; M et T 32 × 2 × 2 × 3 = 384 ; recherche de dose 3 niveaux × 32 × 3 × 2 modes = 576 (absorbée en partie par les 640) ; calibrage du développement 32 × 30 = 960. Total ≈ 2 300 épisodes ; à 100–140 s par épisode (génération + 8B, ou + 3B), 64–90 h de carte, **≈ 70–125 USD** (prix SUPPOSÉ). Au-dessus des 90 USD de l'extension : le pilote lui-même demande un GO, ou se réduit à 16 tâches (≈ 36–65 USD) au prix d'un intervalle de a deux fois plus large.

---

## (c) Réponse à l'arbitre

### Ce qui est établi (au statut indiqué)

- **Plafond d'unités** : 96 tâches, 64 d'évaluation ; au plus 64 unités sabotées par mode en épreuve, puisque la réserve ne peut plus y entrer (contamination non testable sans tâches neuves). RAPPORTÉ (A1 § 1, B1 § 1) ; conséquence HYPOTHÈSE partagée par A, B et C.
- **Planchers structurels** : 48 unités pour un écart constant de 10 points, 93 pour 5 points ; δ = 0,05 incertifiable à 64 unités, δ = 0,10 certifiable. Calcul sans aléa (A1 `E_ter`, recalculé par C) : OBSERVÉ-NON-AUDITÉ, mais arithmétique, non simulé.
- **Le calibrage domine la dépense** (57–66 % des épisodes) et doit être coupé **dans** les tâches, pas par tâche (0,03–0,04 contre 0,14–0,26 au contrôle 12). OBSERVÉ-NON-AUDITÉ, reproduit par C à graine neuve.
- **Dénominateur de D-S9** : le seuil à 1 % est une statistique d'ordre lue par les deux fiches ; le nombre de modes qui le lisent ne change pas son bruit. Lecture A (par fiche). HYPOTHÈSE non contestée par les deux équipes rouges.
- **Contrainte de code** : seuil infini sous 99 épisodes par cellule et par strate ; duplication des jumeaux par mode nécessaire (essai exécuté, A1 § 6). RAPPORTÉ.
- **Deux décisions sont déjà prises** et ne se lèvent pas par défaut : P-015 (b) (R-321) et D-S9 (a) (N-055). RAPPORTÉ.

### Ce qui ne l'est pas

- **a, h, concordance, écart blanc/blanc** : supposés (A1 § 10) ; toutes les tables de puissance en dépendent. Sans mesure, « K = 10 donne 0,63–0,78 à 10 points » est une proposition conditionnelle.
- **4 800 tient-il l'union des deux contrôles 12 ?** Non simulé (A1 ne tire qu'une cellule). C'est T1 ; tout le devis v2 en dépend.
- **La contamination par P3 et T0.7** : non mesurable sur ce banc (B-0). G1 porte une portée conditionnelle qu'il faut dire à Lazar.
- **Le régime « diffus avec dommage » existe-t-il ?** Jamais mesuré ; T3 + T6.
- **« Mention » et « témoin »** : définitions non servies ; D4 inexécutable tant que P-015 n'est pas scellé dans la fiche.
- **Rythmes des épisodes sabotés, prix de carte, 36 = 4 + 32, taux de scores non finis** : non mesurés ou non vérifiables ici.
- **L'organisme du pôle à la couche 2** : si le pilote prend la réserve, il n'a plus de développement ; nœud.

### Les cinq divergences, corrigées

1. **Dénominateur** : lecture A ; 9 600 recommandés sur les 64 tâches, moitiés dans chaque tâche, **sans strate de calibrage** par défaut ; 4 800 seulement si T1 le tient sur l'union. Ce qui ferait changer : T9 positif (strate horizon → tout se divise), a mesuré > 0,5.
2. **Exécutions** : K = 10 sur 64 unités, fixé par nœud et non par le pilote (sinon fuite, B-a3). L'option « 96 tâches » est morte ; « agrandir le banc » est le seul levier vrai et devient un nœud (extraction neuve, arXiv). Ce qui ferait changer : écart blanc/blanc mesuré ≤ 5 points au pilote → aucun K ne sauve G1 (b), nœud sur la cible.
3. **Jumeaux** : partagés, avec T5 au moment de S_x, duplication par mode dans le format, règle de score manquant aveugle au mode, et **une seule lecture de G1** après génération de S_x.
4. **Mention et dose** : « mention » gardée à K = 3 (nœud, pas défaut), **témoin instruit dans le duel** ; recherche de dose contre toute la liste des boîtes noires par action ; **épreuve = dose diffuse seule**, dose-réponse au pilote et au développement, rapportée.
5. **Ordre** : (0) captures gelées (T8 et T9 exigent que les captures du pilote soient définitives) ; (1) T1 sur processeur, zéro dépense ; (2) pilote sur la réserve : T3, T6, T8, T9, a, h, concordance, rythmes ; (3) préenregistrement de G1, scellé, contre-lu, avec puissance écrite aux bornes de l'intervalle de a et portée conditionnelle (T2) ; (4) calibrage d'épreuve ; (5) modes connus en épreuve, scores scellés ; (6) S_x généré avec T5 ; (7) T7 ; (8) lecture unique de G1. Dépense perdue si une hypothèse tombe : à l'étape 2, le pilote seul ; à l'étape 4, le calibrage, qui ne dépend d'aucun mode et resterait réutilisable sauf si T9 impose une strate.

### L'expérience à faire en premier

**T1**, parce qu'elle ne coûte rien, qu'elle décide du poste qui pèse 57 à 66 % de la banque, et que son issue est scellable avant tout GO. Si son intervalle contient 0,05, le résultat est aussi utile : il dit que 2 000 répétitions ne suffisent pas, avant qu'on dépense pour le savoir. La seconde est le pilote, parce que tout le reste (K, régime diffus, dommage, scores finis, strate horizon, rythmes) y tient pour 70 à 125 USD [illustratif, prix SUPPOSÉ] — et parce qu'un pilote qui tombe sur H_B de T3 ou de T6 économise la banque entière.

FIN-DE-CELLULE