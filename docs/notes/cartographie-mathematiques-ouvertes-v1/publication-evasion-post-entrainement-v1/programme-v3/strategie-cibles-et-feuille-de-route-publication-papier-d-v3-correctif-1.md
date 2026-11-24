# Programme et feuille de route de publication du papier D — v3, correctif 1

**Objet du papier D.** La conjecture d'évasion sous filtrage pendant l'entraînement après pré-entraînement (billet de Yair Halberstadt) : un détecteur imparfait de désalignement est placé dans la boucle d'entraînement, et l'on étudie les équilibres de Gibbs du rejet pur et de la pénalité.

- **Date** : 24 novembre 2026 ; v3 vers 14 h, correctif 1 vers 14 h 25 (temps universel).
- **Auteur** : Claude Fable 5.2, effort élevé, sous-agent de rédaction, sur mandat de la session mère. Demande d'origine de Lazar : « mets à jour avec Fable le programme pour le papier D à partir de la note de sortie du collisionneur ».
- **Statut** : pièce de travail, non scellée. Elle remplace la v2 sans l'écraser. Elle ne décide rien : trois points sont soumis à Lazar (section 5), une restriction de son mot sur la marge d'audit lui est proposée (section 6), et toute diffusion, toute soumission et toute dépense restent ses décisions.
- **Correctif 1** : la v3 (empreinte `b4ee88e2869e88e1…`, gardée intacte à côté) a été contre-lue par Claude Opus 5.5, neuf, effort élevé : « accepté avec corrections », six défauts à corriger, sept mineurs, aucun bloquant (`contre-lecture-opus-programme-v3-v1.md`, `76b3cee7e39cb87e…`). Les treize sont traités ici ; correspondance dans `table-corrections-contre-lecture-programme-v3-v1.md`. La vérification des corrections par le même contre-lecteur reste à faire.
- **Version remplacée, gardée intacte** : `P/strategie-cibles-et-feuille-de-route-publication-papier-d-v2.md` (empreinte `752868bfc48b21af…`) ; v1 : même dossier (`12ac2a2946431233…`).
- **Abréviations de chemins** : `P/` = `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/` ; `D/` = `papiers/D/`. Branche : `papier-d/evasion-post-entrainement-v1`.

**Limites de cette pièce.**
- Rien n'a été vérifié en ligne. Aucune échéance, aucune règle de conférence ou de revue, aucun chiffre de l'état de l'art n'est opposable ici : tout est marqué « à vérifier sur pièce ».
- Les scripts du dépôt n'ont pas été relancés. Six calculs cités ont été refaits à part (section 1.3).
- La note de sortie du collisionneur a été lue en entier, avec son erratum. Les neuf cellules du collisionneur n'ont pas été relues, sauf une recherche ciblée sur la normalisation par groupe. La spécification des instruments de l'expérience sur modèle ouvert et le verdict de l'expérience de seuil n'ont été lus qu'en partie.
- L'auteur est un modèle de la même maison que la lettre A du collisionneur (Claude Opus 5.5). Le lecteur de la note était déjà un Opus 5.5, et le contre-lecteur de la v3 aussi. Un biais en faveur des propositions de la lettre A est possible.

---

## 1. En bref

**Verdict.** La note de sortie du collisionneur ne renverse pas le programme : elle le resserre. Sa « trouvaille principale » (une condition manquante à l'inversion entre rejet pur et pénalité) ne touche pas le manuscrit, qui portait déjà la condition ; le défaut réel qu'elle a fait trouver est ailleurs, dans la normalisation de la récompense sous pénalité, et il est corrigé. Le manuscrit théorique est prêt pour une cible modeste une fois remplis les préalables sans dépense de la section 7.1 ; la conférence principale reste conditionnée à une expérience payante, non décidée, dont le résultat peut être contraire.

1. **Ce qui était déjà au manuscrit.** La condition de l'inversion (théorème 1, point 4(c)). Les modèles du collisionneur n'ont vu qu'un résumé des faits, pas le manuscrit.
2. **Ce que la note a fait corriger.** La normalisation : sous pénalité, c'est l'écart « récompense honnête plus pénalité » qui compte, et non la pénalité seule (correctifs 2 et 3). Et la remarque qui dit quelle procédure d'entraînement réalise chaque opérateur.
3. **Ce qui n'existe pas.** Aucun code d'entraînement d'un modèle de langue avec bras de rejet pur, de masquage et de pénalité, donc aucune qualification d'un tel code sur un cas exact. Aucune expérience sur réseau réel. Aucune lecture d'antériorité du manuscrit sur les articles voisins.
4. **Trois points soumis à Lazar**, sans défaut : viser d'abord un atelier non archivistique ; ouvrir, sur devis, le banc de code à niches de triche construites ; dire si son accord antérieur sur un petit dépôt public compagnon tient tel quel (section 5).
5. **Rien de payant, rien de diffusé, pas de formalisation en Lean, pas d'arbre exact à quatre bras avant le 1er décembre 2026.** La borne plus fine de la marge du plancher d'audit est inscrite selon le mot de Lazar ; une restriction venue du mandat de la mère lui est proposée, sans lui être prêtée (section 6).
6. **La v2 contenait des affirmations fausses ou fragiles**, corrigées en section 8 : probabilités d'acceptation chiffrées, « zéro erreur mathématique », « élimination définitive » de Lean, formule de point fixe attribuée à tort à toute optimisation en ligne, affirmation ambiguë sur la pénalité et le furtif sous normalisation par groupe (vraie dans une géométrie, fausse dans une autre), dates.

### 1.1 Base retenue et pièces qui font foi

| Pièce | Chemin | Empreinte (début) | État |
|---|---|---|---|
| Manuscrit, base retenue | `P/manuscrit-arxiv/main-v4-correctif-3-erratum-1.tex` (et `.pdf`) | `25d094dd9a2b0e2e…` | contre-lu (correctif 2), corrections vérifiées (correctif 3), une réserve mineure levée par l'erratum 1 ; non diffusé |
| Script de vérification des correctifs 2 et 3, et sa sortie | `P/verifier_correctif_3_v1.py` ; `P/exemples-verifies-correctif-3-v1.json` | `76c381ca1171f515…` ; `e5111e54b6ca5297…` | aucun défaut ; relancé par le vérificateur sur une copie |
| Note du correctif 2 | `P/note-correctif-2-manuscrit-v4-v1.md` | `5a241d8e12053d35…` | pièce de travail |
| Contre-lecture du correctif 2 ; vérification du correctif 3 | `D/audits/contre-lecture-sonnet-correctif-2-manuscrit-v4-v1.md` ; `D/audits/verification-sonnet-corrections-correctif-3-manuscrit-v4-v1.md` | `86fc0787bec9bf8f…` ; `b92c6785b53ac222…` | « accepté avec corrections », puis « corrections acceptées » |
| Billet et page de dépôt portés au correctif 3 | `P/billet-lesswrong-evasion-post-entrainement-en-v4-correctif-3.md` ; `P/github-page/README-v4-correctif-3.md` | `79179bb4f674aa92…` ; `ca195464f3870b8c…` | portés ; vérification par le contre-lecteur non trouvée |
| Note de sortie du collisionneur et son erratum 1 | branche `runs/collisionneurs-reprise-2026-11-24-v1`, `docs/notes/collisionneur-v9/notes-de-sortie-v1/note-sortie-cible-publication-papier-d-v1.md` et `…-v1-erratum-1.md` | `d26699ccf9eb0711…` (version PDF : `62f261135aff3c00…`) ; erratum : `d82ebef9a0b3af5b…` | pièce de travail ; lecteur du même modèle que la lettre A |
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

Refaits à part, sur processeur, hors du dépôt (scripts `calc/controle_v3.py` et `calc/controle_v3_correctif_1.py` à côté de cette pièce, graines consignées). Le contre-lecteur a relancé le premier et refait les points 1 à 6 par ses propres scripts ; ses comptes concordent avec ceux-ci.

1. la condition de l'inversion avec récompense honnête non nulle : 100 000 tirages, aucun désaccord avec le calcul direct ;
2. le freinage du furtif par la pénalité **sous gradient euclidien sur les logits** d'un softmax à trois classes : la formule de la note tient, et le signe est négatif dans les 17 750 tirages où la part honnête dépasse $1/\sqrt 3$. Ce freinage ne vaut pas sous gradient naturel (point 5) ;
3. les pièges par mélange : si une fraction $q$ des pièges est marquée et le reste indiscernable, le rapport de densité des épisodes ordinaires aux pièges est borné par $1/(1-q)$ ;
4. le point fixe sous division par l'écart-type du groupe, avec ancre, en champ moyen : $\pi\propto p\,e^{\eta\bar r/\sigma(\pi)}$, c'est-à-dire la pénalité à une pression effective qui dépend de la politique. C'est une dérivation d'une ligne, contrôlée sur un exemple (écart de $3\cdot10^{-15}$) ;
5. l'effet instantané d'une hausse de la pénalité sur le furtif, géométrie par géométrie, sur 100 000 tirages en niche parfaite et 100 000 en détection partielle (section 8.1) ;
6. le point fixe du lot rempli de survivants avec leur moyenne pour ligne de base : c'est la pénalité où l'épisode intercepté est noté comme la moyenne des acceptés, à la pression $\eta/\bar Z(\pi)$ ; trois exemples, écart d'au plus $7\cdot10^{-15}$, contre 0,016 à 0,47 pour la pénalité de score brut nul à la même pression.

Les points 3 à 6 sont des contrôles de cette pièce et de sa contre-lecture. Ils ne sont pas écrits dans un texte du dépôt.

---

## 2. Intégration de la note de sortie, proposition par proposition

Lettres de la note : Opus = Claude Opus 5.5 (lettre A) ; Carbon = `gemini-4-carbon` (lettre B) ; Neon = `gemini-4-neon` (lettre C). Tours : III.1 conception, III.2 critique croisée, III.3 réponse. Selon l'erratum 1 de la note, Opus a réfléchi lui aussi, à l'effort « high » ; les niveaux ne se comparent pas d'un fournisseur à l'autre, et aucun écart de traitement entre modèles n'est à en tirer. Statuts : **retenue**, **rejetée**, **reportée**, **déjà faite**, **soumise à Lazar**.

| N° | Proposition | Source | Statut | Raison, en une ligne |
|---|---|---|---|---|
| 1 | Écrire la condition de l'inversion entre rejet pur et pénalité en niche parfaitement furtive | Neon III.1 ; refaite par Opus III.2 et III.3 ; acceptée par Carbon III.3 | **déjà faite** | Elle figurait au théorème 1, point 4(c), avant le collisionneur ; les modèles n'ont vu qu'un résumé. Forme générale ajoutée aux correctifs 2 et 3. |
| 2 | Dire que le plancher sous pénalité dépend de la récompense honnête plus la pénalité, et non de la pénalité seule | Neon III.1 ; précisé par Opus III.2 ; accepté par Neon III.3 | **déjà faite** | Section « Task Reward and In-Loop Monitor » de la base : le score brut d'interception et l'écart $R_0 + C$ sont distingués ; vérifié par le script. |
| 3 | Dire quelle procédure réalise le rejet pur ; distinguer rejet pur, masquage et filtrage itéré | Carbon III.1 (masquage) ; Neon III.1 (rejet en un pas) ; trois réalisations au III.3 (Opus, Carbon, Neon) | **déjà faite** pour l'énoncé ; la réalisation de référence d'une expérience est **reportée** : proposée par la conception de Fable, arrêtée avec la décision sur le banc de code | Remarque « Which training procedures realize each operator » : trois réalisations exactes du rejet pur, masquage rangé sous la pénalité, filtrage itéré rangé sous le rejet répété. |
| 4 | Qualifier le code d'entraînement sur un cas calculable exactement (arbre de séquences court, bandit à trois bras) avant tout modèle réel | Carbon, puis Opus III.2 ; adoptée par les trois III.3 | non faite pour l'objet visé : **reportée** ; principe déjà appliqué à deux autres codes | Aucun code d'entraînement n'existe. Le principe est appliqué au simulateur du calendrier d'audit (trois bancs témoins de l'expérience de seuil) et au calcul de points fixes tabulaires (script du correctif 3), qui n'entraînent rien. L'arbre exact à quatre bras : « pas maintenant ». |
| 5 | Ajouter un bras de masquage, distinct du rejet pur et de la pénalité | Opus, Carbon, Neon III.3 | **retenue** pour toute expérience ; ouverture **soumise à Lazar** (banc de code à niches construites) | Au manuscrit, le masquage est déjà identifié à la pénalité de score brut nul. Le préenregistrement sur modèle ouvert n'a pas ce bras : à transmettre à sa session. |
| 6 | Fixer les classes avant l'entraînement par un critère aveugle au détecteur (arbre syntaxique, oracle caché) | Opus III.2 contre Carbon et Neon ; Carbon III.2 contre Neon ; adoptée III.3 | **retenue** | Sinon l'enrichissement est vrai par construction. Le préenregistrement sur modèle ouvert établit déjà la triche par programme ; sa variable principale combine cette vérité et le verdict du moniteur : à confronter par son contre-lecteur. |
| 7 | Tenir disjoints les jeux de tests de la récompense, des pièges et de l'oracle | Opus III.2 ; adoptée par les trois | **retenue** pour le banc ; **soumise à Lazar** (banc de code à niches construites) | Sans cela l'oracle entre dans la récompense. Sans objet pour le manuscrit théorique. |
| 8 | Repasser les mêmes trajectoires dans les poids gelés, pour séparer sélection des séquences et dérive des représentations | Opus, Carbon, Neon III.2 ; adoptée III.3 | **retenue** | Une forme voisine est déjà au préenregistrement sur modèle ouvert (textes du premier tour réencodés par le modèle final ; sonde figée contre sonde réapprise). |
| 9 | Mesurer le taux de faux négatifs à taux de fausses alertes fixé | Carbon, Neon III.2 ; adoptée par les trois | **retenue** | Une dérive uniforme des scores ferait passer un instrument cassé pour stable. Le préenregistrement sur modèle ouvert lit une aire sous la courbe : à transmettre. |
| 10 | Construire des pièges par mélange, de distance connue exactement | Opus III.2 ; adoptée par Carbon et Neon | **reportée** | Aucun bras de pièges n'est ouvert. Côté théorie, le mélange borne aussi le rapport de densité (section 1.3, point 3) : à écrire seulement si la cible le demande. |
| 11 | Porter le nombre de graines à dix ou douze, après calibrage du bruit entre graines | Opus (dix), Carbon et Neon (douze) III.3 | **retenue** en principe | Avec cinq graines appariées le plus petit niveau atteignable est 1/16. Le préenregistrement sur modèle ouvert prévoit huit à douze paires, par calcul de puissance : compatible, plancher à discuter. |
| 12 | En Lean, donner des témoins de cohérence des hypothèses plutôt qu'un énoncé faux qui ne compile pas | Carbon, Neon III.2 ; adoptée par Opus III.3 | **reportée** après le 1er décembre | La formalisation existe ; son script de rejeu emploie précisément l'énoncé faux refusé. Carbon et Neon jugent le gain nul en conférence ; Opus la garde pour une revue. |
| 13 | Ajouter une dynamique : réplicateur sur la partition finie ; descente miroir dont l'équilibre de Gibbs est le point fixe ; transitoire sous gradient contre équilibre | Opus III.1 ; Neon III.1 ; Neon III.2 et Carbon III.3 | **déjà faite** en partie (brouillon hors manuscrit) ; le reste **reporté** | Le brouillon de dynamique traite déjà le réplicateur sous le nom de gradient naturel (sans ancre, le flot de gradient naturel tabulaire est la dynamique du réplicateur sur la partition ; identité classique, à citer sur une référence vérifiée), et donne la forme miroir et l'identité exacte en temps fini. Reste à écrire : l'effet instantané de la pénalité, géométrie par géométrie (section 8.1). |
| 14 | Comparer rejet pur et pénalité à divergence appariée | Neon III.1 ; critique d'Opus III.2 ; calcul de Carbon III.2 ; ramenée à un second test par Neon III.3 | **rejetée** comme test principal ; **reportée** comme second test | L'estimande change, et le calcul de Carbon (une forte pénalité y inverse le signe) n'a été refait ni par le lecteur ni ici. |
| 15 | Abandonner la normalisation des récompenses par groupe ; ajouter un test de translation de la récompense | Opus III.2 ; adoptée par les trois III.3 | **retenue** pour toute expérience | La division par l'écart-type du groupe laisse invariant le rapport $(R_0+C)/\Delta R$ ; elle rend non réglable la pression effective $\eta/\sigma(\pi)$, donc les produits qui entrent dans les seuils. Le brouillon en champ moyen dit « seule l'horloge change », mais sans ancre ; avec ancre, l'équilibre se déplace (section 8.1). |
| 16a | Cible : un atelier non archivistique, maintenant, avec le manuscrit théorique | Opus, Carbon, Neon III.1 ; confirmée III.3 | **soumise à Lazar** (première cible) | Accord indépendant des trois, sur un résumé du manuscrit ; règles citées de mémoire. |
| 16b | Cible : la revue à évaluation continue (Transactions on Machine Learning Research), en l'état | Carbon III.1 et III.3 pour ; Neon III.1 et III.3 contre ; Opus III.3 sous condition | **soumise à Lazar** (première cible), comme option 2 | Désaccord non résolu ; chacun s'appuie sur des critères de la revue cités de mémoire. |
| 16c | Cible : la conférence sur l'apprentissage automatique sûr et digne de confiance | Carbon III.1 (préférée) ; Neon III.1 (alternative) ; Opus III.1 (piste courte, pour le manuscrit actuel) | **soumise à Lazar** (première cible), comme option 3a | Opus la place pour le manuscrit actuel ; existence d'une piste courte et échéance à vérifier dans l'appel de l'année. |
| 16d | Cible : la piste principale d'une grande conférence, seulement si une expérience montre la prédiction sur un vrai modèle | Opus, Carbon, Neon III.1 ; Opus III.3 (bascule de signe au seuil prédit) | **reportée**, conditionnée à la décision sur le banc de code | Aucune expérience n'existe ; la prédiction est bilatérale et peut être réfutée. |
| 16e | Écarter comme première cible les conférences de théorie de l'apprentissage, les conférences de sécurité des systèmes et la revue longue | Opus, Carbon, Neon III.1 | **retenue** (elles restent écartées) | Pas de borne d'apprentissage ; pas d'attaque de bout en bout ; revue trop lente pour une première diffusion. |
| 17 | Diffusion : prépublication sobre, aucune promotion pendant l'évaluation, code anonymisé, billet après la décision | Opus, Carbon, Neon III.1 ; voie séparée de Carbon III.1 et III.3 | **retenue** comme règle de prudence ; tout geste reste à Lazar | Règles à lire dans l'appel de l'année. Aucune diffusion avant le geste de Lazar. |
| 18 | Trois tâches pour le banc de code : test visible corrompu ; fonctions sur entiers bornés générées, avec solveur exhaustif ; optimisation sous budget de temps avec deux failles | Opus ; Carbon ; Neon — toutes au III.3 | **soumise à Lazar** (banc de code à niches construites) ; aucune choisie | Aucune n'a été critiquée, puisqu'elles datent du dernier tour. La tâche d'Opus est proche de celle du préenregistrement existant. |
| 19 | Mesurer les critères des instruments avant l'entraînement seulement | Opus III.2 contre Neon ; adoptée par Neon III.3 | **retenue** | Un critère qui contient l'hypothèse testée écarte comme défectueux l'instrument qui la contredit. |
| 20 | Faire battre à chaque instrument des vérifications mécaniques sur des cas honnêtes appariés (longueur, mots-clés, arbre syntaxique, perplexité) | Opus, Carbon, Neon III.1 | **retenue** | Conforme à la règle du programme sur les bases de comparaison ; à transmettre à la session du préenregistrement. |
| 21 | Chercher l'antériorité du manuscrit lui-même, en commençant par deux articles | note, « À reprendre ensuite » | **retenue**, avant toute diffusion | Les notices sont vérifiées, le contenu n'est pas lu pour l'antériorité. Une zone occupée serait un nœud de décision. |
| 22 | Définir le coût de maintien et le taux de triche sur épisodes ordinaires | Opus III.1 et III.3 | **déjà faite** | Les deux sont définis dans la base (section sur la récompense ; théorème 2, régime des pièges). Le résumé transmis aux modèles ne les portait pas. |
| 23 | Tester la dépendance de chemin à loi initiale unique, par une pénalité nulle puis pleine | Carbon III.2 ; reprise par Neon III.3 | **reportée** | Voisine de la bistabilité du brouillon de dynamique et du contraste par dose d'amorçage du préenregistrement existant. |
| 24 | Retourner la difficulté de la stéganographie spontanée en prédiction de la barrière d'accessibilité, par dosage de la masse furtive initiale | Opus III.1 ; critiquée par Carbon et Neon III.2 | **reportée** | Le dosage par affinage change aussi la compétence et la survie au détecteur ; l'amorçage par doses existe déjà dans le préenregistrement. |
| 25 | Ajouter une quatrième classe explicite, l'échec, dans toutes les prédictions | Neon III.3 ; calcul d'Opus III.3 | **retenue** pour toute expérience | Le rapport du furtif à l'honnête ne dépend pas des autres classes ; les probabilités absolues, si. |
| 26 | Écarter les bornes séquentielles ou computationnelles lourdes | Opus, Carbon, Neon III.1 | **retenue** (elles restent écartées) | Risque d'impasse, gain douteux. La section sur le budget d'audit, qui existe, n'est pas de ce type. |
| 27 | Réécrire le manuscrit en article de position | Carbon, Neon III.1 | **reportée**, non recommandée à ce stade | Demande une réécriture ; existence et règles de la piste à vérifier dans l'appel de l'année. |
| 28 | Propositions retirées ou corrigées par leurs auteurs : accélération du furtif par des représentations orthogonales ; bonus de triche défini par l'échec aux tests cachés ; validation des pièges par un classifieur faible ; contrôle négatif qui prédit le même signe que l'hypothèse rivale ; ajustement à 0,90 sur quatre points ; conditionnement sur un taux de triche mesuré après traitement ; rééchantillonnage sur trois graines ; trois à cinq graines ; deux initialisations pour la dépendance de chemin | Carbon III.1 ; Opus III.1 ; Carbon III.1 ; Carbon III.1 ; Carbon III.1 ; Neon III.1 ; Opus III.1 ; les trois ; Neon III.1 | **rejetées** | Réfutées, biaisées ou non jugeables au tour III.2 ; retirées ou corrigées au tour III.3. |
| 29 | Tenir une sonde interne hors de la boucle et la comparer au juge sur le texte, pour voir si l'audit hors boucle garde son taux de faux négatifs | Opus III.1 (duel sur l'audit hors boucle) ; Neon III.1 (sonde interne contre juge sur le texte) ; critique de Carbon III.2 (covariance imposée par construction) ; Opus III.3 (sonde entraînée sans exemples furtifs) ; Neon III.3 (juge en mesure secondaire) | **reportée**, conditionnée à la décision sur le banc de code | C'est le bras qui éprouverait le mécanisme d'audit du théorème 2 ; la repasse dans les poids gelés ne le couvre pas. À transmettre à la session du préenregistrement, qui a une sonde figée et une sonde réapprise. |
| 30 | Croiser affinage complet et affinage de faible rang | Carbon III.3 ; critique de Neon III.2 | **reportée** ; à transmettre | L'affinage de faible rang pourrait induire lui-même le couplage testé. Le préenregistrement existant n'emploie que des adaptateurs de rang faible. Le croisement double des bras : sur devis. |
| 31 | Porte « égalité des bras sans détecteur », à côté de la convergence sur bandit exact et de l'invariance par translation | Carbon III.3 | **retenue** pour toute expérience | Porte sans coût, à passer avant tout modèle réel. Non faite : aucun code d'entraînement n'existe. |
| 32 | Loi jointe continue de l'avantage de triche et de la survie, avec contexte | Carbon III.1 | **reportée** | Option de la version longue, voisine de la transition continue par la méthode de Laplace de la v2 ; ni dérivée ni contre-lue. |
| 33 | Dire que le rejet pur est linéaire en la survie, ce qui rend exacte l'agrégation par classe, alors que la pénalité est convexe | Opus III.3 ; Carbon III.3 | **retenue** : une phrase proposée au manuscrit | Sous rejet pur, le poids d'une classe à récompense constante ne dépend que de sa survie moyenne ; sous pénalité, la survie moyenne ne donne qu'une borne. Le préenregistrement existant encadre déjà cet effet par deux bornes. |
| 34 | Éteindre une niche rare par l'estimation de la divergence en politique, comparée à une relecture pondérée de la loi initiale | Carbon III.3 | **reportée** | Dernier tour : ni critiquée ni recalculée. |
| 35 | Borne exacte pour la classe composée de la politique et du banc de test | Neon III.3 | **reportée** | Rejet partiel de Neon à la critique de circularité ; non refaite. |
| 36 | Dire que le régime des pièges est vide quand leur support est disjoint de celui des épisodes ordinaires | Neon III.1 | **retenue** : une phrase proposée au manuscrit | La distance en variation totale vaut alors 1 et la borne ne dit rien. La base suppose une distance strictement inférieure à 1, sans dire ce que cela exclut. |

**Désaccords que cette pièce ne tranche pas.** La revue à évaluation continue en l'état (Carbon pour, Neon contre, Opus sous condition). Les pièges tirés parmi des épisodes réels : fonctionnement voulu pour Opus, tautologie pour Carbon et Neon. La formalisation en Lean : utile pour Opus, sans gain pour Carbon et Neon.

**Ce que les modèles n'avaient pas sous les yeux.** La note écrit : « Le manuscrit ne contient ni expérience sur réseaux ni preuve mécanisée. » C'est toujours vrai du manuscrit. Hors du manuscrit, existaient déjà au moment des dernières cellules la formalisation en Lean et quatre brouillons de sections (dynamique, normalisation par groupe, géométrie du découplage, budget d'audit). Les jugements des modèles sur la profondeur du manuscrit portent donc sur un état antérieur et résumé ; ils restent valables pour le manuscrit de base, qui ne contient aucune de ces pièces.

---

## 3. Ce qui est déjà fait, avec le chemin de la pièce

1. **Condition de l'inversion.** `P/manuscrit-arxiv/main-v4-correctif-3-erratum-1.tex`, théorème 1, point 4(c) : en niche parfaitement furtive, la pénalité donne strictement plus de furtif absolu que le rejet pur si et seulement si $\eta(\Delta R + C) > \log(1/\beta_{\mathrm v})/(1-\beta_{\mathrm v})$. Le résumé et la liste des contributions disent « past an explicit threshold ». La remarque qui suit ajoute que, sous la même condition, la pénalité donne aussi plus d'honnêteté et moins de triche totale. Cette condition était déjà dans la v4 et son correctif 1.
2. **Forme générale avec récompense honnête non nulle.** Même fichier, section « Task Reward and In-Loop Monitor » : la condition devient $\eta(1-\beta_{\mathrm v})(R_0 + \Delta R + C) > \log(1/\beta_{\mathrm v})$. Ajoutée au correctif 2, précisée au correctif 3 (deux conventions pour la pénalité démêlées ; domaine des énoncés qui supposent une pénalité positive).
3. **Procédures qui réalisent chaque opérateur.** Même fichier, remarque « Which training procedures realize each operator » :
   - pénalité : apprentissage par renforcement régularisé par la divergence de Kullback-Leibler à la loi initiale, l'épisode intercepté recevant le score de pénalité ; le masquage de la récompense et le lot écarté sans rééchantillonnage en sont le cas de score brut nul ; une ligne de base constante déplace la pénalité d'autant ;
   - rejet pur, trois réalisations exactes de même loi : entraînement sans moniteur puis rejet à l'inférence ; filtrage de la référence puis entraînement sans moniteur (exact à la limite idéale seulement) ; récompense corrigée par $\eta^{-1}\log\beta$ dans la boucle, qui exige une probabilité de survie par épisode ;
   - filtrage itéré : il réalise la loi du rejet répété, non le rejet pur ; l'affinage supervisé sur les seuls survivants donne $\beta^T\pi_0$.
4. **Vérification sur le modèle tabulaire.** `P/verifier_correctif_3_v1.py`, sortie `P/exemples-verifies-correctif-3-v1.json`, aucun défaut : translation sur neuf cas (écart d'au plus $2\cdot10^{-16}$ ; la translation naïve s'écarte de 0,015 à 0,35) ; récompense corrigée sur trois jeux (écart d'au plus $10^{-14}$ à la loi du rejet pur) ; trois variantes du lot écarté, le gradient étant obtenu par énumération des issues ; filtrage itéré ; inversion sur une grille de 384 cas, 20 000 tirages et 64 points à $10^{-6}$ du seuil en arithmétique à cinquante chiffres, sans désaccord.
5. **Qualification sur cas exact du simulateur de l'expérience de seuil du théorème de l'audit tiré au hasard** (un simulateur du calendrier d'audit, non un code d'entraînement). `D/resultats/seuil-v1/essai-gardes-bancs-temoins-v3.txt` : trois bancs témoins à vérité exacte (sans mémoire, par forme close ; mémoire entière, par programmation dynamique ; mémoire partielle, par énumération), sept gardes passées sur cas sain et sur artefact. Code : `D/code/experience_seuil_chantier3_v3.py`.
6. **Remarque sur la marge du plancher d'audit**, dans le brouillon de section, hors du manuscrit de base. Voir section 6.
7. **Billet et page de dépôt portés à la normalisation.** `P/billet-…-en-v4-correctif-3.md`, `P/github-page/README-v4-correctif-3.md`.

**Limites de ce qui est fait.**
- Le script du correctif 3 vérifie des points fixes par gradients en espérance exacte. Il ne tire aucun lot et n'entraîne aucun réseau. La variante « lot rempli de survivants » n'est établie que sur trois jeux de paramètres, à la limite d'un grand lot ; le manuscrit le dit (« not claimed in general »). Aucun jeu ne teste le cas où le visible est toujours intercepté.
- **Rien n'est fait pour un code d'entraînement de réseau** avec bras de rejet pur, de masquage et de pénalité. Il existe deux codes jouets d'une autre nature : la dynamique tabulaire et à deux canaux (`D/code/dynamique_gradient_evasion_v1.py`) et un réseau à une couche cachée pour le découplage d'une sonde (`D/code/experience_jouet_decouplage_sonde_v1.py`).
- Le manuscrit dit lui-même que l'opérateur de rejet pur coïncide avec un entraînement sans moniteur suivi d'un seul rejet à l'inférence. La note de sortie en tire une remarque juste : c'est moins un filtre « dans la boucle » qu'un filtre de sortie. Le résumé le laisse entendre ; l'introduction ne le dit pas en clair. Retouche proposée, non faite.

---

## 4. Contenu visé, selon la cible

**Version courte (atelier, piste courte, prépublication).** Le manuscrit de base suffit : deux théorèmes, leurs remarques, la remarque sur les procédures. Aucun théorème nouveau n'est requis. Restent, sans dépense, les préalables de diffusion de la section 7.1 : corrections de références portées ; antériorité lue sur PDF ; affirmations attribuées à Price, Robertson et Fisher lues sur PDF ; traces internes retirées ; billet et page de dépôt vérifiés ; règles des appels lues. Trois phrases sont proposées au correctif du manuscrit : le rejet pur comme filtre de sortie ; l'agrégation par classe, exacte sous rejet pur et simple borne sous pénalité ; le régime des pièges, vide quand leur support est disjoint de celui des épisodes ordinaires.

**Version longue (revue, conférence principale).** S'y ajoutent, selon la cible et après contre-lecture finale de chaque brouillon :
- la dynamique en temps fini, complétée d'une proposition sur l'effet instantané de la pénalité, géométrie par géométrie (gradient euclidien, gradient naturel). Ce n'est pas une prédiction unique du modèle : le signe dépend de la géométrie (section 8.1) ;
- la normalisation par groupe, une fois le cas avec ancre écrit et contre-lu ;
- la géométrie du découplage de l'audit ;
- le budget d'audit, avec sa remarque sur la marge ; la marge resserrée selon la section 6 ;
- une expérience sur modèle réel, si Lazar l'ouvre.

**Extensions proposées par la v2 et non faites.** La transition continue par la méthode de Laplace et les pièges à rapport de densité borné n'ont été ni dérivés ni contre-lus dans le dépôt. Les deux formules de la v2 passent un contrôle d'une ligne, refait par le contre-lecteur ; ce n'est pas une preuve. Elles restent des options de la version longue.

---

## 5. Trois points soumis à Lazar

Ce sont des nœuds de décision : aucun défaut ne s'applique après 48 heures. Rien n'est engagé d'ici le mot de Lazar.

### (a) Viser d'abord un atelier non archivistique — SOUMIS À LAZAR

**Décision demandée.** La première cible du manuscrit théorique est-elle un atelier non archivistique d'une des trois grandes conférences d'apprentissage automatique (Conference on Neural Information Processing Systems, International Conference on Machine Learning, International Conference on Learning Representations) ?

**Enjeu.** Le choix fixe le calendrier, les règles d'anonymat à respecter, le sort du billet, et dit si une expérience payante est nécessaire avant une première soumission. Il commande aussi trois dépendances : la borne resserrée de la marge d'audit, la citation de Lean, l'entrée des sections longues.

| Option | Avantage | Inconvénient |
|---|---|---|
| 1. Atelier non archivistique d'abord, avec le manuscrit de base ; conférence principale ensuite, seulement si une expérience montre la bascule de signe au seuil prédit | Les trois modèles y placent le manuscrit, indépendamment, dès le premier tour. Coût nul. Retours de relecteurs du domaine. Laisse ouvertes les soumissions ultérieures, si la règle de l'appel le confirme. | Prestige faible. Calendrier subordonné à l'existence d'un atelier adapté, inconnue aujourd'hui. Les trois modèles n'ont vu qu'un résumé. Règles citées de mémoire. |
| 2. Revue à évaluation continue d'abord (Transactions on Machine Learning Research), avec le manuscrit de base | Pas de calendrier. Publication archivée. Permettrait le billet, selon la voie séparée de Carbon. | Les modèles divergent : Neon juge l'algèbre trop élémentaire pour cette revue. Une théorie déjà archivée pourrait obliger ensuite à un article expérimental autonome : cela dépend des règles de double soumission, à vérifier. Durée d'évaluation non vérifiée. |
| 3a. Conférence de l'Institute of Electrical and Electronics Engineers sur l'apprentissage automatique sûr et digne de confiance (Secure and Trustworthy Machine Learning), en piste courte, avec le manuscrit de base, si cette piste existe | Public naturel du modèle de menace. Aucune expérience requise selon Opus, qui y place le manuscrit actuel ; Carbon préfère cette conférence, Neon la donne en alternative. Publication en conférence. | L'existence de la piste courte n'est pas vérifiée, ni son échéance. Si elle est archivistique, elle pèse sur une soumission ultérieure du même fond en conférence principale : à vérifier. Un seul modèle la place pour le manuscrit en l'état. |
| 3b. Attendre une expérience et viser directement la piste principale d'une grande conférence, ou de la conférence de l'option 3a | Un seul article, le plus fort possible. Pas de morcellement. | Dépend d'une expérience ni scellée ni financée, dont la prédiction est bilatérale. Retarde toute prise de date. Les trois modèles jugent la conférence principale hors d'atteinte sans cette expérience, et incertaine avec. |

**Recommandation.** Option 1, la revue à évaluation continue restant le repli si aucune expérience n'est ouverte. L'option 3a est sa rivale directe : elle ne peut être classée face à l'option 1 qu'une fois son appel lu. **Confiance : moyenne, environ 0,6**, abaissée depuis la v3 parce que l'option 3a, omise alors, n'est pas départagée. Elle repose sur un accord de trois modèles qui n'ont pas lu le manuscrit, et sur des règles non vérifiées. Aucune probabilité d'acceptation n'est avancée : il n'en existe aucune qui soit fondée.

**Préalable, quelle que soit l'option.** Lire l'appel de l'année de chaque cible : existence, date, statut archivistique, anonymat, règle sur les prépublications et les billets, double soumission, limite de pages. Consigner la page lue, sa date et son empreinte. Si un appel de l'année n'est pas encore paru, consigner celui de l'année précédente, marqué « indicatif », non opposable ; la décision peut alors être prise sous réserve.

### (b) Le banc de code à niches de triche construites, sur devis — SOUMIS À LAZAR

**Décision demandée.** Ouvre-t-on, sur devis, une expérience sur modèle réel dont les niches de triche sont construites et dosées, avec un oracle caché, pour éprouver la bascule de signe entre rejet pur et pénalité au seuil prédit ?

**Enjeu.** Sans expérience sur modèle réel, les trois modèles jugent la conférence principale hors d'atteinte. Avec, rien n'est acquis : la prédiction peut être réfutée. Les coûts avancés par les modèles varient d'un facteur dix pour des plans voisins (de 40 à 450 heures de carte graphique pour la seule première expérience), et leurs auteurs les disent illustratifs. Un préenregistrement d'expérience sur modèle ouvert existe déjà, tenu par une autre session, avec un autre plan : rejet répété et non rejet pur, moniteur de la chaîne de pensée à soupçon gradué, banque de tâches publique à assertion visible mutée. Son devis, non scellé, plafonne un premier étage d'étalonnage à 86 heures de carte et chiffre le second entre 66 et 601 heures selon les tranches, sans avancer de prix. Deux plans payants en parallèle seraient un doublon.

| Option | Avantage | Inconvénient |
|---|---|---|
| 1. Fondre les corrections du collisionneur dans le préenregistrement existant (bras de masquage, bras de rejet pur par récompense corrigée, test de translation, classes aveugles au détecteur, taux de fausses alertes fixé), par une version nouvelle écrite par sa session | Une seule expérience, déjà contre-lue une fois, à étages plafonnés. Son moniteur fournit une probabilité de survie par épisode, ce que la récompense corrigée exige. | Son contraste principal n'est pas la bascule de signe. La niche parfaite n'y est pas garantie mécaniquement. Chaque bras ajouté renchérit : complément de devis. Faisabilité à juger par ses concepteurs, non par cette pièce. |
| 2. Construire un banc neuf : détecteur à règle qui n'inspecte jamais le corps de la solution, classes par arbre syntaxique et oracle caché, trois jeux de tests disjoints, après qualification du code sur un arbre exact | Teste directement la prédiction bilatérale, l'élément le plus difficile à dire évident. Paramètres de la niche fixés par construction. | Conception à faire de zéro : trois tâches et trois réalisations du rejet pur jamais critiquées. Code d'entraînement inexistant. Coût inconnu à un facteur dix près. S'ajoute aux chantiers actifs. |
| 3. Ne rien ouvrir maintenant ; s'en tenir aux pas sans dépense ; décider après le 1er décembre, une fois la première cible choisie | Aucune dépense ni dispersion avant l'entretien. Un atelier, une piste courte ou une revue ne demandent pas ce banc. | La conférence principale reste hors d'atteinte. Le calendrier glisse. |

**Recommandation.** Option 3 jusqu'au 1er décembre ; ensuite option 1 plutôt que 2, si Lazar vise la conférence principale. **Confiance : modérée, environ 0,55.** Ce qui la ferait changer : si le plan existant ne peut pas porter une niche parfaite, l'option 2 devient la seule qui éprouve la bascule ; si Lazar s'en tient à l'atelier, à la piste courte ou à la revue, aucun banc n'est nécessaire.

**Dans tous les cas.** Aucune heure de carte sans devis vérifié et accord. La conception d'un plan neuf ou d'une version nouvelle du préenregistrement revient à Fable, sa contre-lecture à Opus. La tâche et la réalisation de référence du rejet pur sont proposées par cette conception et arrêtées avec la décision de Lazar sur le banc ; la présente pièce n'en choisit aucune.

### (c) L'accord antérieur sur un petit dépôt public compagnon — QUESTION POSÉE À LAZAR

**Question.** L'accord donné le 24 novembre vers 6 h 30, temps universel, pour ouvrir un petit dépôt public compagnon (GO-2026-11-24-05) tient-il tel quel, ou attend-il les préalables de diffusion de la section 7.1 ?

**Les faits.**
- L'accord porte sur un dépôt public de trois fichiers propres : la page de présentation, le manuscrit compilé au nom de Lazar, le script de vérification, après revue par Neon.
- Il a été donné quand le manuscrit en était à sa v2. Depuis : dix corrections de l'audit indépendant, un défaut majeur relevé à la vérification de fidélité, la correction de la normalisation sous pénalité. La base est aujourd'hui la v4 avec son correctif 3 et son erratum 1.
- Selon les passations lues, rien n'a été diffusé. Cette pièce n'a pas pu le vérifier hors du dépôt.
- Les préalables de la section 7.1 sont une proposition de cette pièce. Ils ne figurent pas dans l'accord de Lazar. Ni cette pièce ni la session mère ne peuvent suspendre ou conditionner cet accord.

| Réponse possible | Avantage | Inconvénient |
|---|---|---|
| 1. L'accord tient tel quel, appliqué à la base actuelle | Prise de date immédiate. Geste déjà accordé. | L'antériorité n'est pas lue. Une référence est encore fausse dans la base. Un dépôt public au nom de l'auteur pèse sur l'anonymat d'une soumission ultérieure, selon des règles non lues. |
| 2. L'accord tient, après les seuls préalables courts : référence corrigée, traces internes retirées, page de dépôt vérifiée | Quelques jours de délai seulement. Évite de publier une erreur connue. | Antériorité et règles d'anonymat toujours non lues au moment du geste. |
| 3. L'accord attend tous les préalables de la section 7.1 | Aucun geste public avant que la zone revendiquée et les règles soient vérifiées. | Retarde la prise de date ; restreint un accord déjà donné. |

**Avis de la pièce, qui ne vaut pas décision.** Attendre, par la réponse 3, ou à défaut la réponse 2. Raison : l'accord visait une version que l'audit a corrigée dix fois depuis, et un dépôt public ne se reprend pas. **Confiance : modérée, environ 0,6.** Le risque propre de l'attente, qu'un autre publie d'abord, n'est pas chiffrable ici.

---

## 6. La borne plus fine de la marge du plancher d'audit

**Ce qui est acquis.** L'expérience de seuil du théorème de l'audit tiré au hasard a été préenregistrée, courue sur processeur et lue par un lecteur neuf. Aucune réfutation. La garantie tient en 137 points sur 138 ; le dernier est non concluant, non contredit. La marge est nécessaire : sans elle, le seuil est franchi avec une fréquence d'au moins 0,86. Elle est conservatrice d'un facteur 1,75 à 3,56 sur le seuil (médiane 2,49). En audits réservés, employer la marge la plus petite épargnerait de 2 à 57 % du budget de référence de la remarque (le budget uniforme de référence), 10,5 % en médiane. Un audit exact par programmation dynamique a porté sur 32 points à mémoire entière. La marge n'est pas le budget : « deux fois moins d'audits » serait faux.

**Ce que Lazar a dit** (mot du 24 novembre, vers 13 h 10, temps universel ; tel que le registre le consigne, R-5284) : « (b) remarque au manuscrit maintenant — garantie tenue en 137/138, marge nécessaire, conservatrice d'un facteur 2,49 en médiane sur le seuil, soit 10,5 % d'audits réservés en médiane (2 à 57 %) ; (a) théorème resserré après le 1er décembre, sur préenregistrement neuf ». Son mot ne contient aucune autre condition.

**Ce qui est fait.** La remarque est écrite dans le brouillon de la section sur le budget d'audit (`D/theorie/brouillon-fable-budget-audit-v1/audit-budget-section-v1-correctif-4.tex`, remarque « A preregistered simulation of the margin »), **hors du manuscrit de base**. Elle commente le théorème de l'audit tiré au hasard, que le manuscrit de base ne contient pas. Tant que cette section n'entre pas au manuscrit, le mot de Lazar n'a pas d'effet visible dans la pièce qui serait diffusée. Son report est mis au calendrier (section 7.2, tâches 7 et 8). Rien n'est commencé pour le théorème resserré.

**Ce qui vient du mandat de la session mère, et non du mot de Lazar.** La restriction « seulement si la cible visée l'exige ».

**Ce qui est proposé à Lazar.** Ces trois points restreignent ou précisent un accord donné. Ils ne s'appliquent que s'il les accepte ; d'ici là, son mot vaut tel quel.
1. *Restriction.* N'ouvrir le théorème resserré que si la cible retenue l'exige : c'est-à-dire si elle fait entrer la section sur le budget d'audit dans la version soumise, à un niveau d'exigence où un facteur 2,5 sur la marge serait une faiblesse. Un atelier ne l'exige pas.
2. *Priorité basse.* Le gain médian est d'un dixième du budget de référence.
3. *Précision demandée.* « Remarque au manuscrit » vise-t-il le manuscrit de base ? Si oui, la section sur le budget d'audit, ou au moins son théorème de l'audit tiré au hasard, doit y entrer avec la remarque. Si non, le mot est rempli par le brouillon de section.

Recommandation : accepter la restriction et la priorité basse. Confiance : assez bonne, environ 0,7, parce que le gain mesuré est modeste et qu'aucune cible courte ne demande ce théorème.

**Quelle que soit la réponse.** Rien n'est ouvert avant le 1er décembre. Le théorème resserré se fait sur préenregistrement neuf, écrit par Fable, contre-lu par Opus, scellé avant tout tirage, sur processeur. Deux voies sont nommées dans la remarque : une inégalité maximale de martingale à la place de la borne d'union sur les tours ; des queues binomiales exactes à la place de l'inégalité de Bernstein.

---

## 7. Dépendances, ordre et dates

### 7.1 Dépendances

| Pour faire | Il faut d'abord |
|---|---|
| Tout geste de diffusion nouveau (prépublication, commentaire, billet) | lecture d'antériorité sur PDF ; corrections de références portées ; affirmations attribuées à Price, Robertson et Fisher lues sur PDF ; manuscrit débarrassé des traces internes ; billet et page de dépôt vérifiés ; règles de l'appel lues ; **geste de Lazar** |
| Dépôt public compagnon | la réponse de Lazar à la question (c) de la section 5 : son accord antérieur tient-il tel quel ? |
| Décision sur la première cible | appels de l'année lus et consignés ; à défaut, appels de l'année précédente, marqués « indicatifs » |
| Décision sur le banc de code | décision sur la première cible ; devis vérifié |
| Banc ou expérience sur modèle réel | décision sur le banc ; conception par Fable (tâche, réalisation du rejet pur) ; qualification du code sur un cas exact ; préenregistrement scellé ; accord de dépense |
| Scellement du préenregistrement existant sur modèle ouvert | vérification de ses corrections ; instruments écrits, contre-lus et empreintés ; ses six décisions ouvertes ; empreintes finales des brouillons de dynamique et de découplage ; accord de dépense sur le premier étage |
| Report de la remarque sur la marge dans le manuscrit | vérification des correctifs 3 et 4 de la section sur le budget d'audit ; entrée de cette section, ou de son théorème de l'audit tiré au hasard, dans un fichier neuf du manuscrit ; précision de Lazar (section 6, point 3) |
| Théorème resserré de la marge d'audit | 1er décembre passé ; préenregistrement neuf ; et, si Lazar accepte la restriction proposée, une cible qui l'exige |
| Citation de Lean dans une pièce publique | alignement sur la base retenue ; témoins de cohérence des hypothèses ; accord de la mère, puis de Lazar |
| Soumission en conférence principale | résultat d'expérience conforme à la prédiction — il peut ne pas l'être |

**Traces internes à retirer avant diffusion.** Dans le manuscrit : la note d'auteur qui cite les versions et les relectures internes ; les noms de scripts en français ; le nom d'auteur laissé en attente. Dans la page de dépôt : le lien vers le PDF laissé en attente et les noms de fichiers internes. Aucun identifiant d'accord ou de registre n'a été trouvé dans le manuscrit.

### 7.2 Avant le 1er décembre 2026

Tout est sans dépense, sur processeur, sans diffusion. Les dates sont proposées, non engagées ; les chantiers de l'entretien du 1er décembre passent avant.

| Ordre | Tâche | Qui | Date proposée |
|---|---|---|---|
| 1 | Verser cette pièce ; présenter à Lazar les trois points de la section 5 et la proposition de la section 6 | session mère | 25 novembre |
| 2 | Lire les appels de l'année des cibles de la section 7.4 et les consigner ; pour un appel non encore paru, consigner celui de l'année précédente, marqué « indicatif » | une session ayant accès au réseau, ou Lazar | 25 au 27 novembre |
| 3 | Demander à Lazar les PDF sous droits de Price, Robertson et Fisher, cités dans le manuscrit de base ; y lire, page citée, les affirmations qui leur sont attribuées | session mère pour la demande ; Opus pour la lecture | demande le 25 novembre ; lecture à réception |
| 4 | Lecture d'antériorité sur PDF, page citée : le travail sur la surveillance des modèles de raisonnement et l'obscurcissement (Baker et al.) ; la lecture bayésienne de l'apprentissage par renforcement régularisé (Korbak, Perez, Buckley) ; puis l'obscurcissement appris sous pénalité de la chaîne de pensée (Skaf et al.) et l'évasion de moniteurs de l'espace latent par renforcement (Gupta, Jenner) | Opus, effort élevé | 26 au 28 novembre |
| 5 | Correctif du manuscrit, en fichier neuf : référence de Bartók et al. corrigée ; trois phrases proposées (rejet pur comme filtre de sortie ; agrégation par classe exacte sous rejet pur, simple borne sous pénalité ; régime des pièges vide à supports disjoints) ; copie de diffusion sans trace interne. Contre-lecture, puis vérification par le même contre-lecteur | session qui tient le manuscrit ; contre-lecteur d'un autre modèle | 27 au 30 novembre |
| 6 | Vérification du billet et de la page de dépôt portés au correctif 3 | même contre-lecteur | avec la tâche 5 |
| 7 | Vérification des correctifs 3 et 4 de la section sur le budget d'audit, préalable au report de la remarque sur la marge | contre-lecteur d'un autre modèle | 27 au 30 novembre |
| 8 | Report de la remarque sur la marge dans le manuscrit : fichier neuf portant la section sur le budget d'audit, ou son théorème de l'audit tiré au hasard, avec la remarque | session qui tient le manuscrit | après la tâche 7 : avant le 1er décembre si Lazar dit que son mot vise le manuscrit de base ; sinon avec la version longue |
| 9 | Transmettre, par les mères, à la session du préenregistrement sur modèle ouvert les propositions du collisionneur qui touchent son plan : bras de masquage ; classes aveugles au détecteur ; jeux de tests disjoints ; repasse dans les poids gelés ; taux de faux négatifs à taux de fausses alertes fixé ; pièges par mélange ; nombre de graines ; abandon de la normalisation par groupe et test de translation ; critères des instruments mesurés avant l'entraînement ; vérifications mécaniques ; classe « échec » ; sonde interne tenue hors de la boucle ; croisement de l'affinage complet et de l'affinage de faible rang ; porte « égalité des bras sans détecteur » (lignes 5 à 11, 15, 19, 20, 25 et 29 à 31 de la table de la section 2) | session mère | 25 novembre |

**Ne sont pas ouverts avant le 1er décembre** : la formalisation en Lean ; l'arbre exact à quatre bras (« pas maintenant », selon la mère) ; le théorème resserré de la marge ; tout calcul payant ; tout geste de diffusion nouveau et toute soumission ; toute conception de banc.

### 7.3 Après le 1er décembre 2026

L'ordre suit les dépendances. Aucune date n'est donnée pour ce qui dépend d'un appel ou d'une décision.

| Ordre | Tâche | Condition | Qui |
|---|---|---|---|
| 1 | Décision sur la première cible, puis décision sur le banc de code | appels lus, ou consignés comme indicatifs | Lazar |
| 2 | Geste de diffusion : prépublication, puis commentaire et billet dans l'ordre que les règles lues permettent | tâches 3 à 6 de la section 7.2 closes | Lazar |
| 3 | Soumission à la première cible | décision sur la première cible ; **échéance à vérifier dans l'appel de l'année** | Lazar |
| 4 | Pas sans dépense de la théorie : inversion à divergence appariée recalculée sur le modèle tabulaire ; point fixe sous normalisation par groupe avec ancre, écrit et contre-lu ; proposition sur l'effet instantané de la pénalité, par géométrie (euclidienne et naturelle) | utiles à la version longue ou au banc | Opus pour les calculs ; Fable pour un énoncé nouveau |
| 5 | Formalisation en Lean : alignement sur la base retenue, forme avec récompense honnête, témoins de cohérence des hypothèses, contre-exemple certifié de l'inversion privée de sa condition | sa session ; citation publique sur accord | session qui tient Lean |
| 6 | Expérience sur modèle réel : version nouvelle du préenregistrement ou banc neuf ; qualification du code sur un cas exact, tabulaire puis petit réseau, avec la porte « égalité des bras sans détecteur » ; devis ; accord | décision favorable sur le banc | Fable pour la conception ; Opus pour la contre-lecture et le code |
| 7 | Théorème resserré de la marge du plancher d'audit | section 6 | Fable, puis Opus |
| 8 | Sections longues au manuscrit : dynamique, normalisation par groupe, découplage, budget d'audit s'il n'y est pas déjà entré | cible qui les demande ; contre-lecture finale de chacune | session qui tient le manuscrit |
| 9 | Conférence principale | résultat de l'expérience ; **échéance à vérifier dans l'appel de l'année** | Lazar |

### 7.4 Cibles : ce qui reste à vérifier sur pièce

| Cible | Avis des modèles | À vérifier dans l'appel de l'année |
|---|---|---|
| Atelier non archivistique d'une des trois grandes conférences | compétitif pour les trois | existence d'un atelier adapté ; échéance ; statut non archivistique ; anonymat ; limite de pages |
| Revue à évaluation continue (Transactions on Machine Learning Research) | Carbon : oui ; Neon : non ; Opus : après une expérience exacte | critères d'acceptation ; durée d'évaluation ; règle sur les prépublications et les billets |
| Conférence sur l'apprentissage automatique sûr et digne de confiance | Carbon la préfère ; Neon en alternative ; Opus pour le manuscrit actuel, en piste courte | existence d'une piste courte ; statut archivistique ; échéance ; anonymat |
| Piste principale d'une des trois grandes conférences | hors d'atteinte sans expérience, pour les trois | échéance ; prépublication ; non-promotion ; double soumission avec un atelier |
| Piste des articles de position | Carbon, Neon : au prix d'une réécriture | existence ; critères |
| Conférences de théorie de l'apprentissage (Conference on Learning Theory, Algorithmic Learning Theory), conférences de sécurité des systèmes, Journal of Machine Learning Research en première cible | écartées par les trois | sans objet |

---

## 8. Affirmations de la v2 corrigées

| N° | Affirmation de la v2 | Ce que les pièces nouvelles montrent | Ce que dit la v3 |
|---|---|---|---|
| 1 | « Zéro erreur mathématique » du manuscrit | L'audit indépendant a ensuite imposé dix corrections ; la vérification de fidélité a relevé un défaut majeur (la suffisance de trois hypothèses, fausse sous pénalité) ; le correctif 2 a trouvé que la normalisation n'est pas libre sous pénalité. | Aucune erreur connue non corrigée dans la base. Les preuves sont contre-lues par des modèles, non par un mathématicien extérieur. |
| 2 | Acceptation « très probable (80–90 %, potentiel Spotlight) » en atelier ; « > 80 % » à la revue à évaluation continue « avec expériences contrôlées » | Aucune source. Avis d'un seul modèle. Le collisionneur à trois modèles diverge sur la revue. | Aucune probabilité chiffrée, avec ou sans expérience. |
| 3 | « Rejet certain » en piste principale ; bassin de relecteurs « 2 à 3 fois plus dense » | Opinions sans source. | Les trois modèles jugent le manuscrit non compétitif en l'état en piste principale ; rien de plus. |
| 4 | « Élimination définitive de Lean 4 » | Faux en fait : trente théorèmes existent, sur un mot direct de Lazar. Sa valeur en conférence reste disputée. | Elle existe, n'est pas revendiquée au manuscrit, et sa suite est reportée après le 1er décembre. |
| 5 | Sous optimisation en ligne ancrée sur la loi initiale, « l'optimum obéit » à une équation auto-cohérente à survie normalisée et récompense centrée sur les survivants | La formule est l'équation des équilibres d'une règle précise : gradient sur les seuls épisodes acceptés, normalisé par leur nombre, avec leur moyenne pour ligne de base (brouillon de dynamique, proposition « Regularised discard policy gradient »). Plusieurs équilibres peuvent coexister ; celui qui est atteint dépend du départ. | Quatre cas distincts, selon la normalisation du lot et la ligne de base. (1) Lot normalisé par sa taille totale, sans ligne de base : pénalité de score brut nul, exactement. (2) Même lot, ligne de base constante : pénalité déplacée d'autant. (3) Lot rempli de survivants, sans ligne de base : pénalité de score brut nul à la pression auto-cohérente $\eta/\mathbb E_\pi[\beta]$, sur exemples seulement et à grand lot. (4) Lot rempli de survivants, avec leur moyenne pour ligne de base — c'est la formule de la v2 : pénalité où l'épisode intercepté est noté comme la moyenne des acceptés ($C=-b(\pi)$), à la pression $\eta/\bar Z(\pi)$ ; rétroaction positive, absente de la pénalité à score fixe, d'où plusieurs équilibres possibles. Le cas 4 ne se ramène pas au cas 3. |
| 6 | Le rejet pur « correspond uniquement » à un affinage par rejet suivi d'un renforcement ancré sur la loi filtrée | Trois réalisations exactes existent ; l'ajustement sur échantillons acceptés n'est exact qu'à la limite idéale. | Voir section 3, point 3. |
| 7 | Sous avantages centrés sur la moyenne du groupe, avec ou sans division par l'écart-type, pénaliser le visible « abaisse la moyenne du groupe et accélère directement le gradient relatif de la triche furtive » | L'affirmation est ambiguë : son signe dépend de la quantité regardée, de la division par l'écart-type et de la géométrie du gradient. Elle est vraie dans un cas, fausse dans d'autres (section 8.1). Le retrait de Carbon porte sur une affirmation voisine, non sur celle-ci. | Ni « accélère directement », ni « contredite ». Une proposition à écrire sur l'effet instantané de la pénalité, géométrie par géométrie ; elle n'est pas une prédiction unique du modèle. Avec ancre, la division par l'écart-type déplace l'équilibre, et pas seulement l'horloge. |
| 8 | Théorème de transition continue par la méthode de Laplace ; théorème des pièges à rapport de densité borné, qui « élimine totalement » le plancher d'attaques rares | Ni dérivés ni contre-lus dans le dépôt. La borne de rapport de densité est infinie pour des pièges synthétiques de support disjoint. | Options de la version longue. Pour des pièges par mélange, la borne vaut $1/(1-q)$ : observation à vérifier. |
| 9 | Théorème du découplage « sous covariance bornée » | La base établit que, sous pénalité, une covariance nulle ne suffit pas et qu'une covariance positive ne fait pas forcément monter la survie à l'audit à forte pression. | Une borne en covariance ne vaut telle quelle que pour le rejet pur. Le brouillon de géométrie du découplage traite la question autrement. |
| 10 | Calendrier daté (atelier « février », conférence « mai », piste de position « fin janvier ») ; durée d'évaluation de la revue ; label de passage en conférence | Cités de mémoire par un modèle. | Aucune date. Tout est « à vérifier dans l'appel de l'année ». |
| 11 | « Protocole de prise de date aujourd'hui » : poster d'abord le commentaire | Les préalables de la section 7.1 ne sont pas remplis. Un accord de Lazar existe déjà pour un petit dépôt public compagnon (GO-2026-11-24-05), donné sur une version du manuscrit corrigée depuis ; les passations lues disent que rien n'a été diffusé. | Aucun geste de diffusion nouveau avant le mot de Lazar. Le sort de l'accord antérieur lui est demandé (section 5, point (c)) ; cette pièce ne le suspend pas. |
| 12 | Coût d'expérience de « 30 à 80 dollars » (v1) ; écart attendu « supérieur à 15 points » ; banc et modèles nommés de mémoire | Le devis existant chiffre en heures, sans prix : 16 à 86 heures pour l'étalonnage seul. Le contenu d'un des bancs nommés n'est pas vérifié ; la licence du plus petit modèle nommé n'est pas libre d'office. | Aucun coût ni taille d'effet avancé hors devis. |
| 13 | Toilettage : retirer les « 14 000 tirages » du résumé, renommer les scripts, remplacer les tables par des diagrammes de phase | Fait pour le résumé. Les scripts portent encore des noms en français. Les tables restent ; des figures de phase existent pour le seul modèle à deux canaux. | Renommage à la copie de diffusion. Diagrammes : version longue. |

### 8.1 La pénalité et le furtif sous avantages centrés : ce qui tient, géométrie par géométrie

Cadre des contrôles : champ moyen, modèle tabulaire à trois strates, 100 000 tirages par cas (`calc/controle_v3_correctif_1.py` ; le contre-lecteur trouve les mêmes signes par ses propres tirages). La question est l'effet instantané d'une hausse de la pénalité. Sauf mention, la niche est parfaite : le furtif n'est jamais intercepté.

| Règle | Grandeur | Effet d'une hausse de la pénalité |
|---|---|---|
| Ligne de base par la moyenne seule, gradient naturel | taux de croissance du logarithme de la part furtive | **croît** dans les 100 000 tirages : sa dérivée vaut $(1-\beta_{\mathrm v})\pi_{\mathrm v}>0$. La v2 est ici juste à la lettre. |
| même règle | taux du furtif contre l'honnête | inchangé : il vaut $\Delta R$ |
| même règle | taux du furtif contre le visible | croît dans les 100 000 tirages |
| Division par l'écart-type, gradient naturel, sans ancre | avantage normalisé du furtif | **décroît** dans les 100 000 tirages. La v2 est ici contredite. |
| même règle | taux du furtif contre l'honnête | décroît dans les 100 000 tirages |
| même règle | taux du furtif contre le visible | croît dans 75 552 tirages sur 100 000 (75 289 chez le contre-lecteur). Le brouillon en champ moyen dit seulement que ce taux reste borné. |
| Ligne de base par la moyenne seule, gradient euclidien sur les logits | taux de croissance du logarithme de la part furtive | **décroît** dans les 17 672 tirages où la part honnête dépasse $1/\sqrt 3$ : c'est le freinage relevé par Neon. Il croît dans 80 424 tirages sur 100 000 au total. |

Trois précisions.
- **Hors de la niche parfaite**, quand le furtif est intercepté une partie du temps, la première ligne ne tient plus : sous gradient naturel avec la moyenne seule, le taux de croissance de la part furtive ne croît avec la pénalité que dans 49 720 tirages sur 100 000, et le taux du furtif contre l'honnête baisse toujours.
- **Avec ancre**, la division par l'écart-type ne change pas seulement l'horloge : le point fixe est la pénalité à la pression $\eta/\sigma(\pi)$, qui dépend de la politique (section 1.3, point 4).
- Le brouillon de dynamique le dit lui-même : l'effet du moniteur se lit dans une géométrie donnée.

**Conséquence.** Il n'y a pas de « prédiction à deux horizons » qui vaudrait pour le modèle. Il y a, à l'équilibre, la condition de l'inversion ; et, à l'instant initial, un signe qui dépend de la règle d'apprentissage. Une expérience devra donc fixer et consigner sa règle avant de prédire un transitoire.

**Non opposable, à vérifier sur pièce avant tout usage.** Toutes les règles et échéances de conférences et de revue. Les références citées de mémoire par les modèles et absentes du registre : le travail de Roger et Greenblatt sur le raisonnement caché ; l'article de l'optimisation proximale de politique ; la sonde non supervisée de Burns et al. ; l'article de Goodhart. Les heures de carte et les coûts avancés par les modèles. Les six références dont seule la notice est vérifiée et dont le PDF doit être fourni par Lazar (Price, Robertson, Fisher, Lancaster, Stein, et l'ouvrage de Boucheron et al. pour un théorème précis).

---

## 9. Ce qui change par rapport à la v2

1. **Source.** La v2 intégrait deux avis d'un seul modèle. La v3 intègre un collisionneur à trois modèles, ligne par ligne, avec un statut par proposition.
2. **Base.** La v2 portait sur la v2 du manuscrit. La v3 porte sur la v4 avec son correctif 3 et son erratum 1, et dit ce qui est déjà fait, avec les chemins.
3. **Cible.** Plus de « trajectoire reine » retenue ni de dates. L'atelier d'abord est soumis à Lazar, avec trois autres options.
4. **Expérience.** Plus de campagne annoncée ni de coût. Le banc à niches construites est soumis à Lazar, sur devis, en regard du préenregistrement qui existe déjà.
5. **Théorie.** Plus de « quatre théorèmes » à produire. Deux versions de contenu, selon la cible ; quatre brouillons existants replacés ; deux extensions de la v2 ramenées au rang d'options.
6. **Marge du plancher d'audit.** Inscrite : théorème resserré après le 1er décembre, sur préenregistrement neuf (mot de Lazar) ; restriction « si la cible l'exige » proposée à Lazar ; report de la remarque au manuscrit mis au calendrier.
7. **Lean.** D'« éliminé » à « existant, non revendiqué, suite reportée ».
8. **Corrections.** Treize lignes d'affirmations de la v2 retirées, resserrées ou précisées, dont toutes les probabilités d'acceptation.
9. **Dépôt public compagnon.** L'accord antérieur de Lazar n'est ni exécuté ni suspendu par cette pièce : son sort lui est demandé.
10. **Calendrier.** Deux blocs, avant et après le 1er décembre 2026 ; rien de payant, rien de diffusé, ni Lean ni arbre exact à quatre bras avant.
11. **Prudence.** Tout ce qui vient de mémoire de modèle est marqué non opposable.

---

## 10. Ce que le correctif 1 change par rapport à la v3

Détail, défaut par défaut : `table-corrections-contre-lecture-programme-v3-v1.md`.

1. **Normalisation par groupe.** « Contredite trois fois » est retiré. La section 8.1 dit ce qui tient, géométrie par géométrie. La « prédiction à deux horizons » devient une proposition sur l'effet instantané de la pénalité, par géométrie.
2. **Point fixe sous lot rempli de survivants.** Un quatrième cas est ajouté, celui de la formule de la v2 ; il ne se ramène pas au troisième.
3. **Marge du plancher d'audit.** Le mot de Lazar est cité tel que le registre le consigne. La restriction « si la cible l'exige » est rendue au mandat de la mère et proposée à Lazar. La remarque est dite faite dans le brouillon de section seulement ; son report au manuscrit est au calendrier.
4. **Première cible.** L'option 3 est scindée : la piste courte de la conférence sur l'apprentissage automatique sûr et digne de confiance, avec le manuscrit de base, devient une option à part.
5. **Table d'intégration.** Huit lignes ajoutées (29 à 36) et la ligne 28 complétée.
6. **Dépôt public compagnon.** Le sort de l'accord antérieur est une question posée à Lazar ; la pièce ne tranche pas.
7. **Mineurs.** Statut de la qualification du code d'entraînement abaissé à « non faite » ; une seule formulation pour le choix de la réalisation du rejet pur ; citation exacte de la note ; trace interne replacée dans la page de dépôt ; propositions nommées en clair ; préalables de diffusion alignés, PDF de Price, Robertson et Fisher demandés, repli sur les appels de l'année précédente ; empreintes et chiffres précisés.
8. **Contraintes inchangées.** Aucune dépense ; Lean et l'arbre exact à quatre bras après le 1er décembre ; aucune diffusion ; aucune date présentée comme vérifiée.
