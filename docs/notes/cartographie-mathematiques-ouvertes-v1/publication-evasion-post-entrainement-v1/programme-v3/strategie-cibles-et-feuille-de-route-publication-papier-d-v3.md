# Programme et feuille de route de publication du papier D — v3

**Objet du papier D.** La conjecture d'évasion sous filtrage pendant l'entraînement après pré-entraînement (billet de Yair Halberstadt) : un détecteur imparfait de désalignement est placé dans la boucle d'entraînement, et l'on étudie les équilibres de Gibbs du rejet pur et de la pénalité.

- **Date** : 24 novembre 2026, vers 14 h (temps universel).
- **Auteur** : Claude Fable 5.2, effort élevé, sous-agent de rédaction, sur mandat de la session mère. Demande d'origine de Lazar : « mets à jour avec Fable le programme pour le papier D à partir de la note de sortie du collisionneur ».
- **Statut** : pièce de travail, non contre-lue, non scellée. Elle remplace la v2 sans l'écraser. Elle ne décide rien : deux points sont soumis à Lazar (section 5), et toute diffusion, toute soumission et toute dépense restent ses décisions.
- **Version remplacée, gardée intacte** : `P/strategie-cibles-et-feuille-de-route-publication-papier-d-v2.md` (empreinte `752868bfc48b21af…`) ; v1 : même dossier (`12ac2a2946431233…`).
- **Abréviations de chemins** : `P/` = `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/` ; `D/` = `papiers/D/`. Branche : `papier-d/evasion-post-entrainement-v1`.

**Limites de cette pièce.**
- Rien n'a été vérifié en ligne. Aucune échéance, aucune règle de conférence ou de revue, aucun chiffre de l'état de l'art n'est opposable ici : tout est marqué « à vérifier sur pièce ».
- Les scripts du dépôt n'ont pas été relancés. Quatre calculs cités ont été refaits à part (section 1.3).
- La note de sortie du collisionneur a été lue en entier, avec son erratum. Les neuf cellules du collisionneur n'ont pas été relues, sauf une recherche ciblée sur la normalisation par groupe. La spécification des instruments de l'expérience sur modèle ouvert et le verdict de l'expérience de seuil n'ont été lus qu'en partie.
- L'auteur est un modèle de la même maison que la lettre A du collisionneur (Claude Opus 5.5), dont le lecteur de la note était déjà. Un biais en faveur de ses propositions est possible.

---

## 1. En bref

**Verdict.** La note de sortie du collisionneur ne renverse pas le programme : elle le resserre. Sa « trouvaille principale » (une condition manquante à l'inversion entre rejet pur et pénalité) ne touche pas le manuscrit, qui portait déjà la condition ; le défaut réel qu'elle a fait trouver est ailleurs, dans la normalisation de la récompense sous pénalité, et il est corrigé. Le manuscrit théorique est prêt pour une cible modeste après trois gestes sans dépense ; la conférence principale reste conditionnée à une expérience payante, non décidée, dont le résultat peut être contraire.

1. **Ce qui était déjà au manuscrit.** La condition de l'inversion (théorème 1, point 4(c)). Les modèles du collisionneur n'ont vu qu'un résumé des faits, pas le manuscrit.
2. **Ce que la note a fait corriger.** La normalisation : sous pénalité, c'est l'écart « récompense honnête plus pénalité » qui compte, et non la pénalité seule (correctifs 2 et 3). Et la remarque qui dit quelle procédure d'entraînement réalise chaque opérateur.
3. **Ce qui n'existe pas.** Aucun code d'entraînement d'un modèle de langue avec bras de rejet pur, de masquage et de pénalité. Aucune expérience sur réseau réel. Aucune lecture d'antériorité du manuscrit sur les articles voisins.
4. **Deux décisions soumises à Lazar**, sans défaut : viser d'abord un atelier non archivistique ; ouvrir, sur devis, le banc de code à niches de triche construites (section 5).
5. **Rien de payant, rien de diffusé, pas de formalisation en Lean, pas d'arbre exact à quatre bras avant le 1er décembre 2026.** La borne plus fine de la marge du plancher d'audit est inscrite, sous condition (section 6).
6. **La v2 contenait des affirmations fausses ou fragiles**, corrigées en section 8 : probabilités d'acceptation chiffrées, « zéro erreur mathématique », « élimination définitive » de Lean, formule de point fixe attribuée à tort à toute optimisation en ligne, accélération du furtif par la pénalité sous normalisation par groupe, dates.

### 1.1 Base retenue et pièces qui font foi

| Pièce | Chemin | Empreinte (début) | État |
|---|---|---|---|
| Manuscrit, base retenue | `P/manuscrit-arxiv/main-v4-correctif-3-erratum-1.tex` (et `.pdf`) | `25d094dd9a2b0e2e…` | contre-lu (correctif 2), corrections vérifiées (correctif 3), une réserve mineure levée par l'erratum 1 ; non diffusé |
| Script de vérification des correctifs 2 et 3, et sa sortie | `P/verifier_correctif_3_v1.py` ; `P/exemples-verifies-correctif-3-v1.json` | `76c381ca1171f515…` ; `e5111e54b6ca5297…` | aucun défaut ; relancé par le vérificateur sur une copie |
| Note du correctif 2 | `P/note-correctif-2-manuscrit-v4-v1.md` | `5a241d8e12053d35…` | pièce de travail |
| Contre-lecture du correctif 2 ; vérification du correctif 3 | `D/audits/contre-lecture-sonnet-correctif-2-manuscrit-v4-v1.md` ; `D/audits/verification-sonnet-corrections-correctif-3-manuscrit-v4-v1.md` | `86fc0787bec9bf8f…` ; `b92c6785b53ac222…` | « accepté avec corrections », puis « corrections acceptées » |
| Billet et page de dépôt portés au correctif 3 | `P/billet-lesswrong-evasion-post-entrainement-en-v4-correctif-3.md` ; `P/github-page/README-v4-correctif-3.md` | `79179bb4f674aa92…` | portés ; vérification par le contre-lecteur non trouvée |
| Note de sortie du collisionneur et son erratum 1 | branche `runs/collisionneurs-reprise-2026-11-24-v1`, `docs/notes/collisionneur-v9/notes-de-sortie-v1/note-sortie-cible-publication-papier-d-v1.md` | `d26699ccf9eb0711…` (version PDF : `62f261135aff3c00…`) | pièce de travail ; lecteur du même modèle que la lettre A |
| Préenregistrement de l'expérience de seuil, son erratum 1 | `D/prereg/prereg-seuil-chantier3-v3.md` ; `…-erratum-1.md` | `4f3ee5c3a10b55d3…` ; `411aba8156f16600…` | scellés |
| Témoin des trois bancs exacts | `D/resultats/seuil-v1/essai-gardes-bancs-temoins-v3.txt` | `5e02409fbcc27d72…` | sept gardes sur sept, aucun défaut |
| Verdict de l'expérience de seuil | branche `lecture/seuil-papier-d-v1`, `D/resultats/seuil-v1/verdict-lecture-seuil-chantier3-2026-11-24-v1.md` | `6967654e12881835…` | lu en tête seulement |
| Remarque sur la simulation de la marge | `D/theorie/brouillon-fable-budget-audit-v1/audit-budget-section-v1-correctif-4.tex`, remarque « A preregistered simulation of the margin » | `f546547e940ea115…` | ajoutée au brouillon de section, qui n'est pas dans le manuscrit de base |

### 1.2 État des autres travaux, pour les dépendances

| Travail | Pièce | État constaté dans le dépôt |
|---|---|---|
| Section de dynamique en temps fini (trois règles d'apprentissage sur le modèle tabulaire, modèle à deux canaux) | `D/theorie/brouillon-fable-dynamique-v1/dynamics-section-v1-correctif-3.tex` (`d0dbb9e4e556345c…`) ; code `D/code/dynamique_gradient_evasion_v1.py` | brouillon de Fable, contre-lu, puis relu par Fable (neuf retouches) ; correctif 3 ; vérification du correctif 3 non trouvée ; hors manuscrit |
| Proposition sur les avantages normalisés par groupe, en champ moyen | `D/theorie/grpo-champ-moyen-v1.tex` (`c69aa7879749c398…`) | brouillon v1 ; aucune contre-lecture trouvée |
| Section de géométrie du découplage de l'audit (sondes) | `D/theorie/decouplage-geometrique-v3-correctif-2.tex` (`78efcfc48d81dbdd…`) | jugée « fidèle » à la relecture ; hors manuscrit |
| Section sur le budget d'audit dans le jeu séquentiel | `D/theorie/brouillon-fable-budget-audit-v1/audit-budget-section-v1-correctif-4.tex` | correctifs 3 et 4 ; vérification des derniers correctifs non trouvée ; hors manuscrit |
| Formalisation en Lean | `D/lean/` ; table `D/lean/LISEZMOI-lean-v4.md` (`1c2fc92f7356a837…`) | trente théorèmes, cinq fichiers, sans admission (`sorry`), alignés sur le correctif 1 de la v4 ; non citée au manuscrit ; tenue par une autre session |
| Vérification des références | `D/verification-references-v1/registre-references-v2.md` (`31b4492e6b15ecb1…`) | quatre-vingts références : 76 concordantes, 1 corrigée, 1 année à trancher, 2 non confirmées ; huit corrections à porter ; tenue par la même autre session |
| Expérience sur modèle ouvert (triche non interceptée sous filtre de la chaîne de pensée : rejet répété, pénalité, sans filtre) | `D/preenregistrement-modele-ouvert-v1/brouillons-fable-v2/` : préenregistrement (`865e2a37e28c047b…`), devis (`7c5cb16e0f4d8a0f…`) | v2 après contre-lecture ; vérification des corrections interrompue ; six décisions ouvertes ; **rien n'est scellé, rien n'est lancé** ; tenue par la même autre session |

Règle de partage en vigueur : aucune session n'écrit dans le périmètre de l'autre ; un besoin croisé passe par les mères (`D/passations/2026-11-24-1045-partage-branche-papier-d-v1.md`).

### 1.3 Calculs refaits pour cette pièce

Refaits à part, sur processeur, hors du dépôt (script `calc/controle_v3.py` à côté de cette pièce, graine consignée) :

1. la condition de l'inversion avec récompense honnête non nulle : 100 000 tirages, aucun désaccord avec le calcul direct ;
2. le freinage transitoire du furtif par la pénalité sous gradient ordinaire sur un softmax à trois classes : la formule de la note tient, et le signe est négatif dans les 17 750 tirages où la part honnête dépasse $1/\sqrt 3$ ;
3. les pièges par mélange : si une fraction $q$ des pièges est marquée et le reste indiscernable, le rapport de densité des épisodes ordinaires aux pièges est borné par $1/(1-q)$ ;
4. un exemple, un seul, du point fixe sous division par l'écart-type du groupe avec ancre : la loi atteinte est la pénalité à une pression effective qui dépend de la politique.

Les points 3 et 4 sont des observations de cette pièce. Elles ne sont ni écrites dans un texte du dépôt ni contre-lues.

---

## 2. Intégration de la note de sortie, proposition par proposition

Lettres de la note : Opus = Claude Opus 5.5 (lettre A) ; Carbon = `gemini-4-carbon` (lettre B) ; Neon = `gemini-4-neon` (lettre C). Tours : III.1 conception, III.2 critique croisée, III.3 réponse. Selon l'erratum 1 de la note, Opus a réfléchi lui aussi, à l'effort « high » ; les niveaux ne se comparent pas d'un fournisseur à l'autre, et aucun écart de traitement entre modèles n'est à en tirer. Statuts : **retenue**, **rejetée**, **reportée**, **déjà faite**, **soumise à Lazar**.

| N° | Proposition | Source | Statut | Raison, en une ligne |
|---|---|---|---|---|
| 1 | Écrire la condition de l'inversion entre rejet pur et pénalité en niche parfaitement furtive | Neon III.1 ; refaite par Opus III.2 et III.3 ; acceptée par Carbon III.3 | **déjà faite** | Elle figurait au théorème 1, point 4(c), avant le collisionneur ; les modèles n'ont vu qu'un résumé. Forme générale ajoutée aux correctifs 2 et 3. |
| 2 | Dire que le plancher sous pénalité dépend de la récompense honnête plus la pénalité, et non de la pénalité seule | Neon III.1 ; précisé par Opus III.2 ; accepté par Neon III.3 | **déjà faite** | Section « Task Reward and In-Loop Monitor » de la base : le score brut d'interception et l'écart $R_0 + C$ sont distingués ; vérifié par le script. |
| 3 | Dire quelle procédure réalise le rejet pur ; distinguer rejet pur, masquage et filtrage itéré | Carbon III.1 (masquage) ; Neon III.1 (rejet en un pas) ; trois réalisations au III.3 (Opus, Carbon, Neon) | **déjà faite** pour l'énoncé ; choix de la réalisation de référence **soumis à Lazar** avec le point (b) | Remarque « Which training procedures realize each operator » : trois réalisations exactes du rejet pur, masquage rangé sous la pénalité, filtrage itéré rangé sous le rejet répété. |
| 4 | Qualifier le code d'entraînement sur un cas calculable exactement (arbre de séquences court, bandit à trois bras) avant tout modèle réel | Carbon, puis Opus III.2 ; adoptée par les trois III.3 | **déjà faite** en partie ; le reste **reporté** | Faite pour l'expérience de seuil (trois bancs témoins) et sur le modèle tabulaire (script du correctif 3). L'arbre exact à quatre bras : « pas maintenant ». Aucun code d'entraînement de réseau n'existe. |
| 5 | Ajouter un bras de masquage, distinct du rejet pur et de la pénalité | Opus, Carbon, Neon III.3 | **retenue** pour toute expérience ; ouverture **soumise à Lazar** (b) | Au manuscrit, le masquage est déjà identifié à la pénalité de score brut nul. Le préenregistrement sur modèle ouvert n'a pas ce bras : à transmettre à sa session. |
| 6 | Fixer les classes avant l'entraînement par un critère aveugle au détecteur (arbre syntaxique, oracle caché) | Opus III.2 contre Carbon et Neon ; Carbon III.2 contre Neon ; adoptée III.3 | **retenue** | Sinon l'enrichissement est vrai par construction. Le préenregistrement sur modèle ouvert établit déjà la triche par programme ; sa variable principale combine cette vérité et le verdict du moniteur : à confronter par son contre-lecteur. |
| 7 | Tenir disjoints les jeux de tests de la récompense, des pièges et de l'oracle | Opus III.2 ; adoptée par les trois | **retenue** pour le banc ; **soumise à Lazar** (b) | Sans cela l'oracle entre dans la récompense. Sans objet pour le manuscrit théorique. |
| 8 | Repasser les mêmes trajectoires dans les poids gelés, pour séparer sélection des séquences et dérive des représentations | Opus, Carbon, Neon III.2 ; adoptée III.3 | **retenue** | Une forme voisine est déjà au préenregistrement sur modèle ouvert (textes du premier tour réencodés par le modèle final ; sonde figée contre sonde réapprise). |
| 9 | Mesurer le taux de faux négatifs à taux de fausses alertes fixé | Carbon, Neon III.2 ; adoptée par les trois | **retenue** | Une dérive uniforme des scores ferait passer un instrument cassé pour stable. Le préenregistrement sur modèle ouvert lit une aire sous la courbe : à transmettre. |
| 10 | Construire des pièges par mélange, de distance connue exactement | Opus III.2 ; adoptée par Carbon et Neon | **reportée** | Aucun bras de pièges n'est ouvert. Côté théorie, le mélange borne aussi le rapport de densité (section 1.3, point 3) : à écrire seulement si la cible le demande. |
| 11 | Porter le nombre de graines à dix ou douze, après calibrage du bruit entre graines | Opus (dix), Carbon et Neon (douze) III.3 | **retenue** en principe | Avec cinq graines appariées le plus petit niveau atteignable est 1/16. Le préenregistrement sur modèle ouvert prévoit huit à douze paires, par calcul de puissance : compatible, plancher à discuter. |
| 12 | En Lean, donner des témoins de cohérence des hypothèses plutôt qu'un énoncé faux qui ne compile pas | Carbon, Neon III.2 ; adoptée par Opus III.3 | **reportée** après le 1er décembre | La formalisation existe ; son script de rejeu emploie précisément l'énoncé faux refusé. Carbon et Neon jugent le gain nul en conférence ; Opus la garde pour une revue. |
| 13 | Ajouter une dynamique : réplicateur sur la partition finie ; descente miroir dont l'équilibre de Gibbs est le point fixe ; transitoire sous gradient contre équilibre | Opus III.1 ; Neon III.1 ; Neon III.2 et Carbon III.3 | **déjà faite** en partie (brouillon hors manuscrit) ; le reste **reporté** | Le brouillon de dynamique donne déjà la forme miroir et l'identité exacte en temps fini ; le mot « réplicateur » n'y figure pas. Le freinage transitoire sous gradient ordinaire n'y est pas : proposition courte à ajouter. |
| 14 | Comparer rejet pur et pénalité à divergence appariée | Neon III.1 ; critique d'Opus III.2 ; calcul de Carbon III.2 ; ramenée à un second test par Neon III.3 | **rejetée** comme test principal ; **reportée** comme second test | L'estimande change, et le calcul de Carbon (une forte pénalité y inverse le signe) n'a été refait ni par le lecteur ni ici. |
| 15 | Abandonner la normalisation des récompenses par groupe ; ajouter un test de translation de la récompense | Opus III.2 ; adoptée par les trois III.3 | **retenue** pour toute expérience | La division par l'écart-type du groupe rend l'intensité et la pénalité effectives non réglables. Le brouillon en champ moyen dit « seule l'horloge change », mais sans ancre : à réconcilier (section 8, ligne 7). |
| 16a | Cible : un atelier non archivistique, maintenant, avec le manuscrit théorique | Opus, Carbon, Neon III.1 ; confirmée III.3 | **soumise à Lazar** (a) | Accord indépendant des trois, sur un résumé du manuscrit ; règles citées de mémoire. |
| 16b | Cible : la revue à évaluation continue (Transactions on Machine Learning Research), en l'état | Carbon III.1 et III.3 pour ; Neon III.1 et III.3 contre ; Opus III.3 sous condition | **soumise à Lazar** (a), comme option 2 | Désaccord non résolu ; chacun s'appuie sur des critères de la revue cités de mémoire. |
| 16c | Cible : la conférence sur l'apprentissage automatique sûr et digne de confiance | Carbon III.1 (préférée) ; Neon III.1 (alternative) ; Opus III.1 (piste courte, pour le manuscrit actuel) | **reportée** | Existence d'une piste courte et échéance à vérifier dans l'appel de l'année ; option 3 du point (a). |
| 16d | Cible : la piste principale d'une grande conférence, seulement si une expérience montre la prédiction sur un vrai modèle | Opus, Carbon, Neon III.1 ; Opus III.3 (bascule de signe au seuil prédit) | **reportée**, conditionnée au point (b) | Aucune expérience n'existe ; la prédiction est bilatérale et peut être réfutée. |
| 16e | Écarter comme première cible les conférences de théorie de l'apprentissage, les conférences de sécurité des systèmes et la revue longue | Opus, Carbon, Neon III.1 | **retenue** (elles restent écartées) | Pas de borne d'apprentissage ; pas d'attaque de bout en bout ; revue trop lente pour une première diffusion. |
| 17 | Diffusion : prépublication sobre, aucune promotion pendant l'évaluation, code anonymisé, billet après la décision | Opus, Carbon, Neon III.1 ; voie séparée de Carbon III.1 et III.3 | **retenue** comme règle de prudence ; tout geste reste à Lazar | Règles à lire dans l'appel de l'année. Aucune diffusion avant le geste de Lazar. |
| 18 | Trois tâches pour le banc de code : test visible corrompu ; fonctions sur entiers bornés générées, avec solveur exhaustif ; optimisation sous budget de temps avec deux failles | Opus ; Carbon ; Neon — toutes au III.3 | **soumise à Lazar** (b) ; aucune choisie | Aucune n'a été critiquée, puisqu'elles datent du dernier tour. La tâche d'Opus est proche de celle du préenregistrement existant. |
| 19 | Mesurer les critères des instruments avant l'entraînement seulement | Opus III.2 contre Neon ; adoptée par Neon III.3 | **retenue** | Un critère qui contient l'hypothèse testée écarte comme défectueux l'instrument qui la contredit. |
| 20 | Faire battre à chaque instrument des vérifications mécaniques sur des cas honnêtes appariés (longueur, mots-clés, arbre syntaxique, perplexité) | Opus, Carbon, Neon III.1 | **retenue** | Conforme à la règle du programme sur les bases de comparaison ; à transmettre à la session du préenregistrement. |
| 21 | Chercher l'antériorité du manuscrit lui-même, en commençant par deux articles | note, « À reprendre ensuite » | **retenue**, avant toute diffusion | Les notices sont vérifiées, le contenu n'est pas lu pour l'antériorité. Une zone occupée serait un nœud de décision. |
| 22 | Définir le coût de maintien et le taux de triche sur épisodes ordinaires | Opus III.1 et III.3 | **déjà faite** | Les deux sont définis dans la base (section sur la récompense ; théorème 2, régime des pièges). Le résumé transmis aux modèles ne les portait pas. |
| 23 | Tester la dépendance de chemin à loi initiale unique, par une pénalité nulle puis pleine | Carbon III.2 ; reprise par Neon III.3 | **reportée** | Voisine de la bistabilité du brouillon de dynamique et du contraste par dose d'amorçage du préenregistrement existant. |
| 24 | Retourner la difficulté de la stéganographie spontanée en prédiction de la barrière d'accessibilité, par dosage de la masse furtive initiale | Opus III.1 ; critiquée par Carbon et Neon III.2 | **reportée** | Le dosage par affinage change aussi la compétence et la survie au détecteur ; l'amorçage par doses existe déjà dans le préenregistrement. |
| 25 | Ajouter une quatrième classe explicite, l'échec, dans toutes les prédictions | Neon III.3 ; calcul d'Opus III.3 | **retenue** pour toute expérience | Le rapport du furtif à l'honnête ne dépend pas des autres classes ; les probabilités absolues, si. |
| 26 | Écarter les bornes séquentielles ou computationnelles lourdes | Opus, Carbon, Neon III.1 | **retenue** (elles restent écartées) | Risque d'impasse, gain douteux. La section sur le budget d'audit, qui existe, n'est pas de ce type. |
| 27 | Réécrire le manuscrit en article de position | Carbon, Neon III.1 | **reportée**, non recommandée à ce stade | Demande une réécriture ; existence et règles de la piste à vérifier dans l'appel de l'année. |
| 28 | Propositions retirées par leurs auteurs : accélération du furtif par des représentations orthogonales ; bonus de triche défini par l'échec aux tests cachés ; validation des pièges par un classifieur faible ; trois à cinq graines ; deux initialisations pour la dépendance de chemin | Carbon III.1 ; Opus III.1 ; Carbon III.1 ; les trois ; Neon III.1 | **rejetées** | Réfutées ou biaisées au tour III.2, retirées au tour III.3. |

**Désaccords que cette pièce ne tranche pas.** La revue à évaluation continue en l'état (Carbon pour, Neon contre, Opus sous condition). Les pièges tirés parmi des épisodes réels : fonctionnement voulu pour Opus, tautologie pour Carbon et Neon. La formalisation en Lean : utile pour Opus, sans gain pour Carbon et Neon.

**Ce que la note ignorait.** Le résumé des faits transmis aux modèles disait qu'il n'y avait « ni expérience sur réseaux ni preuve mécanisée ». Au moment des dernières cellules, la formalisation en Lean existait, ainsi que quatre brouillons de sections (dynamique, normalisation par groupe, géométrie du découplage, budget d'audit). Les jugements des modèles sur la profondeur du manuscrit portent donc sur un état antérieur et résumé ; ils restent valables pour le manuscrit de base, qui ne contient aucune de ces pièces.

---

## 3. Ce qui est déjà fait, avec le chemin de la pièce

1. **Condition de l'inversion.** `P/manuscrit-arxiv/main-v4-correctif-3-erratum-1.tex`, théorème 1, point 4(c) : en niche parfaitement furtive, la pénalité donne strictement plus de furtif absolu que le rejet pur si et seulement si $\eta(\Delta R + C) > \log(1/\beta_{\mathrm v})/(1-\beta_{\mathrm v})$. Le résumé et la liste des contributions disent « past an explicit threshold ». La remarque qui suit ajoute que, sous la même condition, la pénalité donne aussi plus d'honnêteté et moins de triche totale. Cette condition était déjà dans la v4 et son correctif 1.
2. **Forme générale avec récompense honnête non nulle.** Même fichier, section « Task Reward and In-Loop Monitor » : la condition devient $\eta(1-\beta_{\mathrm v})(R_0 + \Delta R + C) > \log(1/\beta_{\mathrm v})$. Ajoutée au correctif 2, précisée au correctif 3 (deux conventions pour la pénalité démêlées ; domaine des énoncés qui supposent une pénalité positive).
3. **Procédures qui réalisent chaque opérateur.** Même fichier, remarque « Which training procedures realize each operator » :
   - pénalité : apprentissage par renforcement régularisé par la divergence de Kullback-Leibler à la loi initiale, l'épisode intercepté recevant le score de pénalité ; le masquage de la récompense et le lot écarté sans rééchantillonnage en sont le cas de score brut nul ; une ligne de base constante déplace la pénalité d'autant ;
   - rejet pur, trois réalisations exactes de même loi : entraînement sans moniteur puis rejet à l'inférence ; filtrage de la référence puis entraînement sans moniteur (exact à la limite idéale seulement) ; récompense corrigée par $\eta^{-1}\log\beta$ dans la boucle, qui exige une probabilité de survie par épisode ;
   - filtrage itéré : il réalise la loi du rejet répété, non le rejet pur ; l'affinage supervisé sur les seuls survivants donne $\beta^T\pi_0$.
4. **Vérification sur le modèle tabulaire.** `P/verifier_correctif_3_v1.py`, sortie `P/exemples-verifies-correctif-3-v1.json`, aucun défaut : translation sur neuf cas (écart d'au plus $2\cdot10^{-16}$ ; la translation naïve s'écarte de 0,015 à 0,35) ; récompense corrigée sur trois jeux (écart d'au plus $10^{-14}$ à la loi du rejet pur) ; trois variantes du lot écarté, le gradient étant obtenu par énumération des issues ; filtrage itéré ; inversion sur une grille de 384 cas, 20 000 tirages et 64 points à $10^{-6}$ du seuil en arithmétique à cinquante chiffres, sans désaccord.
5. **Qualification sur cas exact pour l'expérience de seuil du théorème de l'audit tiré au hasard.** `D/resultats/seuil-v1/essai-gardes-bancs-temoins-v3.txt` : trois bancs témoins à vérité exacte (sans mémoire, par forme close ; mémoire entière, par programmation dynamique ; mémoire partielle, par énumération), sept gardes passées sur cas sain et sur artefact. Code : `D/code/experience_seuil_chantier3_v3.py`.
6. **Remarque sur la marge du plancher d'audit.** Voir section 6.
7. **Billet et page de dépôt portés à la normalisation.** `P/billet-…-en-v4-correctif-3.md`, `P/github-page/README-v4-correctif-3.md`.

**Limites de ce qui est fait.**
- Le script du correctif 3 vérifie des points fixes par gradients en espérance exacte. Il ne tire aucun lot et n'entraîne aucun réseau. La variante « lot rempli de survivants » n'est établie que sur trois jeux de paramètres, à la limite d'un grand lot ; le manuscrit le dit (« not claimed in general »). Aucun jeu ne teste le cas où le visible est toujours intercepté.
- **Rien n'est fait pour un code d'entraînement de réseau** avec bras de rejet pur, de masquage et de pénalité. Il existe deux codes jouets d'une autre nature : la dynamique tabulaire et à deux canaux (`D/code/dynamique_gradient_evasion_v1.py`) et un réseau à une couche cachée pour le découplage d'une sonde (`D/code/experience_jouet_decouplage_sonde_v1.py`).
- Le manuscrit dit lui-même que l'opérateur de rejet pur coïncide avec un entraînement sans moniteur suivi d'un seul rejet à l'inférence. La note de sortie en tire une remarque juste : c'est moins un filtre « dans la boucle » qu'un filtre de sortie. Le résumé le laisse entendre ; l'introduction ne le dit pas en clair. Retouche proposée, non faite.

---

## 4. Contenu visé, selon la cible

**Version courte (atelier, prépublication).** Le manuscrit de base suffit : deux théorèmes, leurs remarques, la remarque sur les procédures. Aucun théorème nouveau n'est requis. Trois gestes sans dépense restent à faire avant toute diffusion : porter les corrections de références, lire l'antériorité sur PDF, retirer les traces internes (section 7.1).

**Version longue (revue, conférence principale).** S'y ajoutent, selon la cible et après contre-lecture finale de chaque brouillon :
- la dynamique en temps fini, complétée d'une proposition sur le freinage transitoire sous gradient ordinaire, qui donne une prédiction à deux horizons ;
- la normalisation par groupe, une fois le cas avec ancre établi ;
- la géométrie du découplage de l'audit ;
- le budget d'audit, avec la marge resserrée seulement si la cible l'exige (section 6) ;
- une expérience sur modèle réel, si Lazar l'ouvre (point (b)).

**Extensions proposées par la v2 et non faites.** La transition continue par la méthode de Laplace et les pièges à rapport de densité borné n'ont été ni dérivés ni contre-lus dans le dépôt. Les deux formules de la v2 passent un contrôle d'une ligne ; ce n'est pas une preuve. Elles restent des options de la version longue.

---

## 5. Deux points soumis à Lazar

Ce sont des nœuds de décision : aucun défaut ne s'applique après 48 heures. Rien n'est engagé d'ici le mot de Lazar.

### (a) Viser d'abord un atelier non archivistique — SOUMIS À LAZAR

**Décision demandée.** La première cible du manuscrit théorique est-elle un atelier non archivistique d'une des trois grandes conférences d'apprentissage automatique (Conference on Neural Information Processing Systems, International Conference on Machine Learning, International Conference on Learning Representations) ?

**Enjeu.** Le choix fixe le calendrier, les règles d'anonymat à respecter, le sort du billet, et dit si une expérience payante est nécessaire avant une première soumission. Il commande aussi trois dépendances : la borne resserrée de la marge d'audit, la citation de Lean, l'entrée des sections longues.

| Option | Avantage | Inconvénient |
|---|---|---|
| 1. Atelier non archivistique d'abord, avec le manuscrit de base ; conférence principale ensuite, seulement si une expérience montre la bascule de signe au seuil prédit | Les trois modèles y placent le manuscrit, indépendamment, dès le premier tour. Coût nul. Retours de relecteurs du domaine. Laisse ouvertes les soumissions ultérieures, si la règle de l'appel le confirme. | Prestige faible. Calendrier subordonné à l'existence d'un atelier adapté, inconnue aujourd'hui. Les trois modèles n'ont vu qu'un résumé. Règles citées de mémoire. |
| 2. Revue à évaluation continue d'abord (Transactions on Machine Learning Research), avec le manuscrit de base | Pas de calendrier. Publication archivée. Permettrait le billet, selon la voie séparée de Carbon. | Les modèles divergent : Neon juge l'algèbre trop élémentaire pour cette revue. Une théorie déjà archivée oblige ensuite à un article expérimental autonome. Durée d'évaluation non vérifiée. |
| 3. Attendre une expérience et viser directement une conférence principale, ou la conférence de l'Institute of Electrical and Electronics Engineers sur l'apprentissage automatique sûr et digne de confiance (Secure and Trustworthy Machine Learning) | Un seul article, le plus fort possible. Pas de morcellement. | Dépend d'une expérience ni scellée ni financée, dont la prédiction est bilatérale. Retarde toute prise de date. Les trois modèles jugent la conférence principale hors d'atteinte sans cette expérience, et incertaine avec. |

**Recommandation.** Option 1, la revue à évaluation continue restant le repli si aucune expérience n'est ouverte. **Confiance : moyenne, environ 0,65.** Elle repose sur un accord de trois modèles qui n'ont pas lu le manuscrit, et sur des règles non vérifiées. Aucune probabilité d'acceptation n'est avancée : il n'en existe aucune qui soit fondée.

**Préalable, quelle que soit l'option.** Lire l'appel de l'année de chaque cible : existence, date, statut archivistique, anonymat, règle sur les prépublications et les billets, double soumission, limite de pages. Consigner la page lue, sa date et son empreinte.

### (b) Le banc de code à niches de triche construites, sur devis — SOUMIS À LAZAR

**Décision demandée.** Ouvre-t-on, sur devis, une expérience sur modèle réel dont les niches de triche sont construites et dosées, avec un oracle caché, pour éprouver la bascule de signe entre rejet pur et pénalité au seuil prédit ?

**Enjeu.** Sans expérience sur modèle réel, les trois modèles jugent la conférence principale hors d'atteinte. Avec, rien n'est acquis : la prédiction peut être réfutée. Les coûts avancés par les modèles varient d'un facteur dix pour des plans voisins (de 40 à 450 heures de carte graphique pour la seule première expérience), et leurs auteurs les disent illustratifs. Un préenregistrement d'expérience sur modèle ouvert existe déjà, tenu par une autre session, avec un autre plan : rejet répété et non rejet pur, moniteur de la chaîne de pensée à soupçon gradué, banque de tâches publique à assertion visible mutée. Son devis, non scellé, plafonne un premier étage d'étalonnage à 86 heures de carte et chiffre le second entre 66 et 601 heures selon les tranches, sans avancer de prix. Deux plans payants en parallèle seraient un doublon.

| Option | Avantage | Inconvénient |
|---|---|---|
| 1. Fondre les corrections du collisionneur dans le préenregistrement existant (bras de masquage, bras de rejet pur par récompense corrigée, test de translation, classes aveugles au détecteur, taux de fausses alertes fixé), par une version nouvelle écrite par sa session | Une seule expérience, déjà contre-lue une fois, à étages plafonnés. Son moniteur fournit une probabilité de survie par épisode, ce que la récompense corrigée exige. | Son contraste principal n'est pas la bascule de signe. La niche parfaite n'y est pas garantie mécaniquement. Chaque bras ajouté renchérit : complément de devis. Faisabilité à juger par ses concepteurs, non par cette pièce. |
| 2. Construire un banc neuf : détecteur à règle qui n'inspecte jamais le corps de la solution, classes par arbre syntaxique et oracle caché, trois jeux de tests disjoints, après qualification du code sur un arbre exact | Teste directement la prédiction bilatérale, l'élément le plus difficile à dire évident. Paramètres de la niche fixés par construction. | Conception à faire de zéro : trois tâches et trois réalisations du rejet pur jamais critiquées. Code d'entraînement inexistant. Coût inconnu à un facteur dix près. S'ajoute aux chantiers actifs. |
| 3. Ne rien ouvrir maintenant ; s'en tenir aux pas sans dépense ; décider après le 1er décembre, une fois le point (a) tranché | Aucune dépense ni dispersion avant l'entretien. Un atelier ou une revue ne demandent pas ce banc. | La conférence principale reste hors d'atteinte. Le calendrier glisse. |

**Recommandation.** Option 3 jusqu'au 1er décembre ; ensuite option 1 plutôt que 2, si Lazar vise la conférence principale. **Confiance : modérée, environ 0,55.** Ce qui la ferait changer : si le plan existant ne peut pas porter une niche parfaite, l'option 2 devient la seule qui éprouve la bascule ; si Lazar s'en tient à l'atelier ou à la revue, aucun banc n'est nécessaire.

**Dans tous les cas.** Aucune heure de carte sans devis vérifié et accord. La conception d'un plan neuf ou d'une version nouvelle du préenregistrement revient à Fable, sa contre-lecture à Opus. Le choix de la tâche et de la réalisation du rejet pur fait partie de cette conception, pas de la présente pièce.

---

## 6. La borne plus fine de la marge du plancher d'audit

**Ce qui est acquis.** L'expérience de seuil du théorème de l'audit tiré au hasard a été préenregistrée, courue sur processeur et lue par un lecteur neuf. Aucune réfutation. La garantie tient en 137 points sur 138 ; le dernier est non concluant, non contredit. La marge est nécessaire : sans elle, le seuil est franchi avec une fréquence d'au moins 0,86. Elle est conservatrice d'un facteur 1,75 à 3,56 sur le seuil (médiane 2,49). En audits réservés, cela représente 2 à 57 % de trop, 10,5 % en médiane. Un audit exact par programmation dynamique a porté sur 32 points à mémoire entière. La marge n'est pas le budget : « deux fois moins d'audits » serait faux.

**Décision de Lazar** (mot du 24 novembre, R-5284).
- Une remarque au manuscrit, maintenant : **faite**. Elle est dans le brouillon de la section sur le budget d'audit (`D/theorie/brouillon-fable-budget-audit-v1/audit-budget-section-v1-correctif-4.tex`, remarque « A preregistered simulation of the margin »). Cette section n'est pas dans le manuscrit de base.
- Un théorème resserré : **après le 1er décembre seulement, sur préenregistrement neuf, et seulement si la cible visée l'exige. Rien n'est commencé d'ici là.**

**Inscription au programme.**
- *Objet* : une borne plus fine de la marge, par l'une des deux voies nommées dans la remarque : une inégalité maximale de martingale à la place de la borne d'union sur les tours ; des queues binomiales exactes à la place de l'inégalité de Bernstein.
- *Condition d'ouverture* : la décision (a) est prise, et la cible retenue fait entrer la section sur le budget d'audit dans la version soumise, à un niveau d'exigence où un facteur 2,5 sur la marge serait une faiblesse. Un atelier ne l'exige pas.
- *Procédure* : préenregistrement neuf, écrit par Fable, contre-lu par Opus, scellé avant tout tirage ; sur processeur.
- *Priorité* : basse. Le gain médian en audits est d'un dixième.

---

## 7. Dépendances, ordre et dates

### 7.1 Dépendances

| Pour faire | Il faut d'abord |
|---|---|
| Toute diffusion (prépublication, commentaire, billet, dépôt public) | lecture d'antériorité sur PDF ; corrections de références portées ; manuscrit débarrassé des traces internes ; billet et page de dépôt vérifiés ; règles de l'appel lues ; **geste de Lazar** |
| Décision (a) | appels de l'année lus et consignés |
| Décision (b) | décision (a) ; devis vérifié |
| Banc ou expérience sur modèle réel | décision (b) ; conception par Fable (tâche, réalisation du rejet pur) ; qualification du code sur un cas exact ; préenregistrement scellé ; accord de dépense |
| Scellement du préenregistrement existant sur modèle ouvert | vérification de ses corrections ; instruments écrits, contre-lus et empreintés ; ses six décisions ouvertes ; empreintes finales des brouillons de dynamique et de découplage ; accord de dépense sur le premier étage |
| Théorème resserré de la marge d'audit | 1er décembre passé ; décision (a) ; cible qui l'exige ; préenregistrement neuf |
| Citation de Lean dans une pièce publique | alignement sur la base retenue ; témoins de cohérence des hypothèses ; accord de la mère, puis de Lazar |
| Soumission en conférence principale | résultat d'expérience conforme à la prédiction — il peut ne pas l'être |

**Traces internes à retirer du manuscrit avant diffusion.** La note d'auteur qui cite les versions et les relectures internes ; les noms de scripts en français ; le nom d'auteur et le lien laissés en attente. La page de dépôt cite aussi des noms de fichiers internes. Aucun identifiant d'accord ou de registre n'a été trouvé dans le manuscrit lui-même.

### 7.2 Avant le 1er décembre 2026

Tout est sans dépense, sur processeur, sans diffusion. Les dates sont proposées, non engagées ; les chantiers de l'entretien du 1er décembre passent avant.

| Ordre | Tâche | Qui | Date proposée |
|---|---|---|---|
| 1 | Verser cette v3 ; présenter à Lazar les décisions (a) et (b) | session mère | 25 novembre |
| 2 | Lire les appels de l'année des cibles de la section 5(a) et les consigner | une session ayant accès au réseau, ou Lazar | 25 au 27 novembre |
| 3 | Lecture d'antériorité sur PDF, page citée : le travail sur la surveillance des modèles de raisonnement et l'obscurcissement (Baker et al.) ; la lecture bayésienne de l'apprentissage par renforcement régularisé (Korbak, Perez, Buckley) ; puis l'obscurcissement appris sous pénalité de la chaîne de pensée (Skaf et al.) et l'évasion de moniteurs de l'espace latent par renforcement (Gupta, Jenner) | Opus, effort élevé | 26 au 28 novembre |
| 4 | Correctif du manuscrit, en fichier neuf : référence de Bartók et al. corrigée ; une phrase d'introduction sur le rejet pur comme filtre de sortie ; copie de diffusion sans trace interne. Contre-lecture, puis vérification par le même contre-lecteur | session qui tient le manuscrit ; contre-lecteur d'un autre modèle | 27 au 30 novembre |
| 5 | Vérification du billet et de la page de dépôt portés au correctif 3 | même contre-lecteur | avec la tâche 4 |
| 6 | Transmettre, par les mères, à la session du préenregistrement sur modèle ouvert les lignes 5 à 11, 15, 19, 20 et 25 de la table de la section 2 | session mère | 25 novembre |

**Ne sont pas ouverts avant le 1er décembre** : la formalisation en Lean ; l'arbre exact à quatre bras (« pas maintenant », selon la mère) ; le théorème resserré de la marge ; tout calcul payant ; toute diffusion ou soumission ; toute conception de banc.

### 7.3 Après le 1er décembre 2026

L'ordre suit les dépendances. Aucune date n'est donnée pour ce qui dépend d'un appel ou d'une décision.

| Ordre | Tâche | Condition | Qui |
|---|---|---|---|
| 1 | Décision (a), puis décision (b) | appels lus | Lazar |
| 2 | Geste de diffusion : prépublication, puis commentaire et billet dans l'ordre que les règles lues permettent | tâches 3 à 5 de la section 7.2 closes | Lazar |
| 3 | Soumission à la première cible | décision (a) ; **échéance à vérifier dans l'appel de l'année** | Lazar |
| 4 | Pas sans dépense de la théorie : inversion à divergence appariée recalculée sur le modèle tabulaire ; point fixe sous normalisation par groupe avec ancre ; proposition sur le freinage transitoire | utiles à la version longue ou au banc | Opus pour les calculs ; Fable pour un énoncé nouveau |
| 5 | Formalisation en Lean : alignement sur la base retenue, forme avec récompense honnête, témoins de cohérence des hypothèses, contre-exemple certifié de l'inversion privée de sa condition | sa session ; citation publique sur accord | session qui tient Lean |
| 6 | Expérience sur modèle réel : version nouvelle du préenregistrement ou banc neuf ; qualification du code sur un cas exact, tabulaire puis petit réseau ; devis ; accord | décision (b) favorable | Fable pour la conception ; Opus pour la contre-lecture et le code |
| 7 | Théorème resserré de la marge du plancher d'audit | section 6 | Fable, puis Opus |
| 8 | Sections longues au manuscrit : dynamique, normalisation par groupe, découplage, budget d'audit | cible qui les demande ; contre-lecture finale de chacune | session qui tient le manuscrit |
| 9 | Conférence principale | résultat de l'expérience ; **échéance à vérifier dans l'appel de l'année** | Lazar |

### 7.4 Cibles : ce qui reste à vérifier sur pièce

| Cible | Avis des modèles | À vérifier dans l'appel de l'année |
|---|---|---|
| Atelier non archivistique d'une des trois grandes conférences | compétitif pour les trois | existence d'un atelier adapté ; échéance ; statut non archivistique ; anonymat ; limite de pages |
| Revue à évaluation continue (Transactions on Machine Learning Research) | Carbon : oui ; Neon : non ; Opus : après une expérience exacte | critères d'acceptation ; durée d'évaluation ; règle sur les prépublications et les billets |
| Conférence sur l'apprentissage automatique sûr et digne de confiance | Carbon la préfère ; Neon en alternative ; Opus pour le manuscrit actuel, en piste courte | existence d'une piste courte ; échéance ; anonymat |
| Piste principale d'une des trois grandes conférences | hors d'atteinte sans expérience, pour les trois | échéance ; prépublication ; non-promotion ; double soumission avec un atelier |
| Piste des articles de position | Carbon, Neon : au prix d'une réécriture | existence ; critères |
| Conférences de théorie de l'apprentissage (Conference on Learning Theory, Algorithmic Learning Theory), conférences de sécurité des systèmes, Journal of Machine Learning Research en première cible | écartées par les trois | sans objet |

---

## 8. Affirmations de la v2 corrigées

| N° | Affirmation de la v2 | Ce que les pièces nouvelles montrent | Ce que dit la v3 |
|---|---|---|---|
| 1 | « Zéro erreur mathématique » du manuscrit | L'audit indépendant a ensuite imposé dix corrections ; la vérification de fidélité a relevé un défaut majeur (la suffisance de trois hypothèses, fausse sous pénalité) ; le correctif 2 a trouvé que la normalisation n'est pas libre sous pénalité. | Aucune erreur connue non corrigée dans la base. Les preuves sont contre-lues par des modèles, non par un mathématicien extérieur. |
| 2 | Acceptation « très probable (80–90 %, potentiel Spotlight) » en atelier ; « > 80 % » à la revue à évaluation continue | Aucune source. Avis d'un seul modèle. Le collisionneur à trois modèles diverge sur la revue. | Aucune probabilité chiffrée. |
| 3 | « Rejet certain » en piste principale ; bassin de relecteurs « 2 à 3 fois plus dense » | Opinions sans source. | Les trois modèles jugent le manuscrit non compétitif en l'état en piste principale ; rien de plus. |
| 4 | « Élimination définitive de Lean 4 » | Faux en fait : trente théorèmes existent, sur un mot direct de Lazar. Sa valeur en conférence reste disputée. | Elle existe, n'est pas revendiquée au manuscrit, et sa suite est reportée après le 1er décembre. |
| 5 | Sous optimisation en ligne ancrée sur la loi initiale, « l'optimum obéit » à une équation auto-cohérente à survie normalisée et récompense centrée sur les survivants | La formule est l'équation des équilibres d'une règle précise : gradient sur les seuls épisodes acceptés, normalisé par leur nombre, avec leur moyenne pour ligne de base (brouillon de dynamique, proposition « Regularised discard policy gradient »). Plusieurs équilibres peuvent coexister ; celui qui est atteint dépend du départ. | Trois cas distincts, selon la base : lot normalisé par sa taille totale, sans ligne de base : pénalité de score brut nul, exactement ; ligne de base constante : pénalité déplacée d'autant ; lot rempli de survivants : pénalité de score brut nul à pression auto-cohérente, sur exemples seulement et à grand lot. |
| 6 | Le rejet pur « correspond uniquement » à un affinage par rejet suivi d'un renforcement ancré sur la loi filtrée | Trois réalisations exactes existent ; l'ajustement sur échantillons acceptés n'est exact qu'à la limite idéale. | Voir section 3, point 3. |
| 7 | Sous avantages normalisés par groupe, la pénalité « accélère directement le gradient relatif de la triche furtive » | Contredit trois fois : le brouillon en champ moyen borne les taux uniformément en la pénalité et trouve le furtif ralenti face à l'honnête ; sous gradient ordinaire, la pénalité freine d'abord le furtif dès que la part honnête dépasse $1/\sqrt 3$ ; Carbon a retiré l'affirmation voisine. | Prédiction à deux horizons, à établir : freinage transitoire, puis amplification à l'équilibre au-delà du seuil. Avec ancre, la division par l'écart-type déplace l'équilibre et pas seulement l'horloge (un exemple, section 1.3). |
| 8 | Théorème de transition continue par la méthode de Laplace ; théorème des pièges à rapport de densité borné, qui « élimine totalement » le plancher d'attaques rares | Ni dérivés ni contre-lus dans le dépôt. La borne de rapport de densité est infinie pour des pièges synthétiques de support disjoint. | Options de la version longue. Pour des pièges par mélange, la borne vaut $1/(1-q)$ : observation à vérifier. |
| 9 | Théorème du découplage « sous covariance bornée » | La base établit que, sous pénalité, une covariance nulle ne suffit pas et qu'une covariance positive ne fait pas forcément monter la survie à l'audit à forte pression. | Une borne en covariance ne vaut telle quelle que pour le rejet pur. Le brouillon de géométrie du découplage traite la question autrement. |
| 10 | Calendrier daté (atelier « février », conférence « mai », piste de position « fin janvier ») ; durée d'évaluation de la revue ; label de passage en conférence | Cités de mémoire par un modèle. | Aucune date. Tout est « à vérifier dans l'appel de l'année ». |
| 11 | « Protocole de prise de date aujourd'hui » : poster d'abord le commentaire | La diffusion est le geste de Lazar ; les préalables de la section 7.1 ne sont pas remplis. Un accord antérieur de Lazar existe pour un petit dépôt public compagnon (GO-2026-11-24-05) ; les passations lues disent que rien n'a été diffusé. | Aucune diffusion avant le geste de Lazar. Exécution de l'accord antérieur à confirmer par la mère. |
| 12 | Coût d'expérience de « 30 à 80 dollars » (v1) ; écart attendu « supérieur à 15 points » ; banc et modèles nommés de mémoire | Le devis existant chiffre en heures, sans prix : 16 à 86 heures pour l'étalonnage seul. Le contenu d'un des bancs nommés n'est pas vérifié ; la licence du plus petit modèle nommé n'est pas libre d'office. | Aucun coût ni taille d'effet avancé hors devis. |
| 13 | Toilettage : retirer les « 14 000 tirages » du résumé, renommer les scripts, remplacer les tables par des diagrammes de phase | Fait pour le résumé. Les scripts portent encore des noms en français. Les tables restent ; des figures de phase existent pour le seul modèle à deux canaux. | Renommage à la copie de diffusion. Diagrammes : version longue. |

**Non opposable, à vérifier sur pièce avant tout usage.** Toutes les règles et échéances de conférences et de revue. Les références citées de mémoire par les modèles et absentes du registre : le travail de Roger et Greenblatt sur le raisonnement caché ; l'article de l'optimisation proximale de politique ; la sonde non supervisée de Burns et al. ; l'article de Goodhart. Les heures de carte et les coûts avancés par les modèles. Les six références dont seule la notice est vérifiée et dont le PDF doit être fourni par Lazar (Price, Robertson, Fisher, Lancaster, Stein, et l'ouvrage de Boucheron et al. pour un théorème précis).

---

## 9. Ce qui change par rapport à la v2

1. **Source.** La v2 intégrait deux avis d'un seul modèle. La v3 intègre un collisionneur à trois modèles, ligne par ligne, avec un statut par proposition.
2. **Base.** La v2 portait sur la v2 du manuscrit. La v3 porte sur la v4 avec son correctif 3 et son erratum 1, et dit ce qui est déjà fait, avec les chemins.
3. **Cible.** Plus de « trajectoire reine » retenue ni de dates. L'atelier d'abord est soumis à Lazar, avec deux autres options.
4. **Expérience.** Plus de campagne annoncée ni de coût. Le banc à niches construites est soumis à Lazar, sur devis, en regard du préenregistrement qui existe déjà.
5. **Théorie.** Plus de « quatre théorèmes » à produire. Deux versions de contenu, selon la cible ; quatre brouillons existants replacés ; deux extensions de la v2 ramenées au rang d'options.
6. **Marge du plancher d'audit.** Inscrite : théorème resserré, sous trois conditions, après le 1er décembre.
7. **Lean.** D'« éliminé » à « existant, non revendiqué, suite reportée ».
8. **Corrections.** Treize lignes d'affirmations de la v2 retirées ou resserrées, dont toutes les probabilités d'acceptation.
9. **Calendrier.** Deux blocs, avant et après le 1er décembre 2026 ; rien de payant, rien de diffusé, ni Lean ni arbre exact à quatre bras avant.
10. **Prudence.** Tout ce qui vient de mémoire de modèle est marqué non opposable.
