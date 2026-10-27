# Cellule A — tour III.2 : équipe rouge croisée

**Pièces.** B (`55cbd60d…`) et C (`958c180e…`) sont présentes, complètes, terminées par FIN-DE-CELLULE. Les faits sont ceux de la v2 (`63e09aa3…`). Ni `selection_pari.py` ni le rapport de méta-conception ne sont servis ; ce que je dis du nul augmenté vient de J et J2 seulement. Tous les chiffres que je produis moi-même sont **illustratifs** ; les statuts des faits sont inchangés.

**Deux failles communes, dites une fois** (je les rappelle sans les répéter) :

- **F0 — le schéma de traits appartient à l'auteur de la fiche.** Les deux propositions fondent leur garde de redite sur une sonde à schéma égal (B : « test de suffisance à schéma égal » ; C : sonde « partitionnée par domaine/tâche »). Aucune ne dit que le **noyau** possède le schéma. Tant que la fiche déclare ses traits, ajouter une colonne inerte change de schéma et sort de toute sonde. Statut : OBSERVÉ-NON-AUDITÉ (lecture de B et C ; aucune pièce ne décrit qui enregistre les traits).
- **F1 — la fuite par absence.** M1 exclut les témoins de tout ce qui est servi (docstring, RAPPORTÉ). B et C gardent cette règle. Or un agent de recombinaison voit la population de sa génération (C § 3, RAPPORTÉ) ; la différence entre « population vue » et « mémoire servie » désigne les témoins. Les deux propositions ont un contrôle « classifieur de témoins », mais aucune ne lui donne en entrée la paire (population, mémoire), qui est la vraie surface d'attaque.

---

## Contre la proposition B

### (a) Failles

**B1 — La fermeture 𝒜(H) est à un seul parent ; l'archive servie au proposeur la rend contournable.** B met dans le nul augmenté la fermeture aveugle du parent déclaré, et sert au proposeur « les survivantes avec leur fermeture explicite ("pour être promue, il faut battre ceci") ». Une fille qui mélange son parent déclaré avec une **autre survivante non déclarée** n'est ni dans 𝒜(parent) ni dans la bibliothèque aveugle ; le test de suffisance d'E2, mené paire par paire contre chaque entrée archivée, ne la voit pas non plus (p′ n'est fonction d'aucun p_H seul). J (limite 4b) ne couvre que « parents, mélanges, enveloppes » des parents déclarés. HYPOTHÈSE : B a déplacé le trou de J2 d'un cran, de « loi aveugle moyenne » à « survivante non déclarée ».

**B2 — La dépense d'α par classe est soit non valide, soit à puissance divisée par deux.** B écrit α_j = α·2^{−j} « pour la j-ième fiche d'une même classe ». Si la première tentative (celle qui a été éliminée) est j = 0 et dépense α, la somme sur la classe vaut 2α : la borne d'union donne ≤ 2α, pas ≤ α. Si l'indexation commence à j = 1, chaque **première** tentative de toute classe ne dispose que de α/2 — c'est-à-dire que tout le pôle passe à α/2 sans le dire, et la lecture « puissance ≥ 0,90 » de J n'est plus comparable. Ma dérivation, HYPOTHÈSE ; vérifiable par un essai unitaire d'une ligne.

**B3 — Le test de suffisance est un second juge, avec moins de données et sans garantie séquentielle.** Il décide « redite » si D ≤ τ sur M instances de sonde. Une fille honnête à composante vraie faible (ε = 0,05, cas que B ne demande que « rapporté ») donne un D petit ; elle est classée redite et paie l'α décroissant d'E3. Le détecteur n'a donc pas la résolution du juge (200 tirages séquentiels, Ville), mais il **précède** le juge et lui retire de l'α. B le reconnaît en partie (thèse 4 : « préfiltre économique ») puis en fait un instrument de validité (thèse 3, E3) : les deux rôles sont incompatibles tant que la résolution du détecteur n'est pas au moins celle du juge.

**B4 — E2 : τ est étalonné « sur des paires honnêtes » du même banc.** Le seuil qui fixe le FPR est appris sur les négatifs qui servent ensuite à mesurer le FPR. Fuite instrument/évaluation. Il faut un lot de calibration disjoint, par graine et par monde.

**B5 — E4 : le « contrôle de manipulation » est vrai par construction.** B exige que « le taux de redites baisse dans le bras 2 ». Mais le bras 2 contient la garde, qui **refuse** mécaniquement les redites : le taux de redites *soumises* baisse que les agents lisent ou non la mémoire. Le contrôle ne vaut que sur les redites *proposées avant garde*. Tel qu'écrit, il reproduit exactement le défaut de M2 qu'il prétend corriger.

**B6 — E4 : le placebo « d'un autre monde de même schéma » n'est pas vide de contenu.** Une mémoire d'un autre monde porte des protocoles, des causes d'échec techniques et des gabarits qui sont **transférables** (ils ne dépendent pas de la loi plantée). Le verdict « 2 ≈ 3 : le contexte aide, pas le contenu » confond contenu *procédural* (transférable) et contenu *factuel* (spécifique au monde). Il manque un placebo à format conservé et verdicts permutés dans le même monde, distinct du bras « empoisonné à 20 % ».

**B7 — Bibliothèque « classée par richesse observée ».** Remplacer la sévérité déclarée par la richesse observée supprime la porte de Goodhart de S11 mais ouvre la malédiction du vainqueur : la richesse dépend de l'ampleur vraie de l'effet, pas de la qualité du protocole. Un protocole appliqué à une fiche à grand effet est promu ; un protocole excellent appliqué à un petit effet ne l'est jamais. Le mérite est attribué au protocole pour ce qui revient à la fiche.

**B8 — Statut d'un chiffre.** « ≈ 13 nats pour 5 paramètres » est présenté comme analogue à l'urne de J ; c'est un ordre de grandeur de regret, non un calcul sur la famille précise (λ, q, b ne sont pas libres sur un ouvert de dimension 5 : q est sur le simplexe, b est défini à une constante près). Illustratif, et B le dit ; mais E1 « peut échouer par la puissance » repose dessus, donc la dimension effective doit être écrite avant le scellement.

### (b) Scénarios d'évasion

| Instrument de B | Évasion | Coût |
|---|---|---|
| Fermeture dans le juge (E1) | Fille = parent déclaré mélangé à une survivante non déclarée, servie avec sa fermeture dans la consigne (B1) | nul : l'archive dit quoi mélanger |
| Test de suffisance (E2) | Ajouter un trait inerte (F0) : plus de schéma commun, plus de sonde | une colonne |
| Dépense d'α par classe (E3) | Composer mélange puis inclinaison puis température : hors de la classe de fonctions ĝ si ĝ est contraint ; ou passer par F0 | script |
| Garde Jaccard conservée en préfiltre | Sous 0,5 par paraphrase ; `ce_qui_change` rempli d'une phrase type et seuil décalé d'un millième (B l'a vu lui-même) | script |
| Bibliothèque par richesse (B7) | Soumettre des protocoles sur des fiches « à grand effet » (quasi-témoins vrais) pour faire entrer son protocole | un appel |
| Placebo | L'agent compare la mémoire à ce qu'il observe dans ses propres expériences ; un verdict contredit par un rejeu signale le placebo | zéro, si l'agent rejoue |
| Témoins | F1 | zéro |

**Tous à la fois, par un proposeur scripté sans appel de modèle** : colonne inerte (sort des sondes) + mélange de deux survivantes servies (sort de la fermeture) + `ce_qui_change` type (passe Jaccard) + seuil déplacé (passe `signature_prediction`). Ce qui reste pour l'arrêter : le juge, avec un nul qui devrait contenir les mélanges de **toutes** les survivantes — ce que B ne propose pas et dont le coût en puissance, s'il vaut ½·dim·ln n par survivante (illustratif), devient prohibitif après quelques générations.

### (c) Contrôles négatifs fatals (leur absence invalide la conclusion)

1. **E1 — nul composite réel.** Outre « q fixe », tirer g au hasard par répétition (λ, q, b aléatoires) et vérifier ≤ α ; puis « parent + survivante non déclarée » (B1) : **doit être vu** sous v1+fermeture (taux > α), sinon le trou n'existe pas et B1 est falsifiée — ce qui serait une bonne nouvelle, mais il faut la constater.
2. **E2 — calibration disjointe de τ** (B4) et rapport séparé du taux de « redites » déclarées sur des paires à schémas différents : la pièce doit dire combien de redites vraies passent par F0, pas les exclure du banc.
3. **E3 — détecteur oracle.** Deux bras : classes assignées par le noyau (oracle) et par le détecteur d'E2. Si le taux de classe dépasse α même avec l'oracle, c'est la dépense (B2) qui est fausse ; sinon ce sont les faux négatifs. Sans ce bras, H_A et H_B d'E3 ne se séparent pas.
4. **E4 — redites proposées avant garde** (B5), **placebo à verdicts permutés dans le même monde** (B6), **A/A** (deux courses du même bras, pour le plancher de bruit ; S1 le demandait, B ne l'a pas), et **classifieur de témoins nourri de (population, mémoire)** (F1).
5. **E5 — déjà présent** (bras « viser la survie haute »). Il manque : un bras où la survie estimée est calculée à partir de descripteurs **déclarés** par la fiche, pour mesurer de combien la Goodhart est pire que sous descripteurs calculés par le noyau.

---

## Contre la proposition C

### (a) Failles

**C1 — Expérience 1 : H_A est une paille, et son issue dépend d'un choix de construction.** H_A (« Jaccard + égalité de `signature_prediction` suffit ») a déjà contre elle la lecture du code (RAPPORTÉ) et S2 (RAPPORTÉ) : B4 veut deux issues dont chacune falsifie quelque chose, pas une issue acquise. Pire : `signature_prediction` contient l'empreinte de `loi_predictive`. Si les « 25 paraphrases lexicales à loi identique » gardent l'objet `loi_predictive` octet pour octet, H_A les détecte à 100 % par la seule empreinte ; si le script les re-sérialise, elle n'en détecte aucune. Le résultat est fixé par le générateur de tricheurs, non par l'instrument. Fuite constructeur/évaluateur ; il faut déclarer, par tricheur, si l'empreinte est conservée.

**C2 — Expérience 2 : le bras 1 peut échouer pour une raison d'implémentation et faire conclure à tort.** C écrit « enveloppe convexe en ligne (mélange par poids exponentiels de Vovk/agrégation universelle) entre les lois parentes et 𝓛 ». Un mélange bayésien d'experts suit le **meilleur expert**, pas la **meilleure combinaison convexe** : son regret est borné par ln N contre un expert fixe. Or le tricheur de J2 gagne précisément parce que la loi vraie est, de fait, « parent corrigé par une loi aveugle moyenne » (J2, OBSERVÉ-NON-AUDITÉ) : aucun expert seul ne l'approche, une combinaison λ oui. Pour dominer la combinaison, il faut un mélange sur une **grille** de (λ, q) — coût en puissance d'ordre ln(taille de grille), ou prix de ½·dim·ln n pour une famille continue (illustratif) — et C ne le précise pas. Si le bras 1 tombe sous 0,85 de puissance *ou* promeut le tricheur, C conclut « H_A réfutée, la mémoire doit suppléer » alors que c'est l'agrégateur qui est mal choisi. Ma dérivation, HYPOTHÈSE.

**C3 — Expérience 2 : τ_pred est le paramètre libre qui fait gagner le bras 2.** Le bras 2 « ≤ 0,05 de faux positifs » n'est pas un taux statistique : la garde refuse de façon déterministe au-dessus de τ_pred, étalonné sur la même famille de tricheurs. Baisser τ_pred fait tendre les fausses promotions vers 0 et monte le rejet des filles honnêtes ; C exige 0,90 de puissance pour le bras 2 mais ne dit pas sur quelles filles honnêtes τ_pred est **fixé avant** de voir les tricheurs. Même fuite que B4.

**C4 — L̃ doublement centrée : juste pour l'inclinaison, muette sur la composition.** L̃ est invariante au biais multiplicatif par issue (C le démontre ; VÉRIFIÉ par le calcul : le centrage en k retire le normalisateur par instance, le centrage en m retire ln β_k). Mais la politique de garde est « L̃ proche **ou** Jaccard ≥ 0,5 déclenche, puis D_JS à l'enveloppe convexe tranche ». Un mélange suivi d'une inclinaison rend L̃ non colinéaire (le mélange n'est pas affine en log) et le texte renommé passe sous 0,5 : le déclencheur ne tire pas, l'enveloppe n'est jamais testée. B avait vu cette composition (S8) ; C ne la met ni dans le banc d'Expérience 1 (quatre familles pures) ni dans la politique.

**C5 — I_c = s·H(p̂_c) : s est constante, ou déclarée.** Si α est le même pour toutes les fiches (J : α = 0,05), s = −ln α est une constante et I_c se réduit à l'entropie binaire de la survie : « pénaliser les régions triviales (s ≈ 0) » est vide. Si s varie, c'est la `severite_attendue` **déclarée par l'auteur** (M1, RAPPORTÉ ; S11 de B) : déclarer haut attire le budget. C note en (a)5 que la survie intermédiaire peut être fabriquée, puis bâtit la sélection de cellule dessus sans garde.

**C6 — Les cellules (Domaine, Opérateur) sont étiquetées par la fiche.** La grille MAP-Elites et le tirage de Thompson lisent le `domaines`/`operateurs` que la fiche déclare (M1 indexe `fiche.domaines`, RAPPORTÉ). Un proposeur qui veut une cellule à p̂ ≈ 0,5 change l'étiquette. C sait que la structure est « sensible au découpage de l'ontologie » mais n'exige pas que le noyau calcule les descripteurs (B le fait pour E5).

**C7 — Expérience 3 : trois bras, quatre différences, et une vérité inobservable.** (i) Le bras 1 a `active=False` (pas de garde), le bras 2 a la garde : 1 contre 2 mêle garde et consigne ; le bras 3 ajoute contenu vrai, grille orientée et contre-exemples : 2 contre 3 mêle trois facteurs. Aucune différence n'est attribuable. (ii) La métrique « survivantes vérifiées vraies sur l'évaluation finale scellée » sur **données réelles** (arXiv, tabulaires) n'est pas une vérité : l'évaluation scellée est un test de plus à α, et Σ(−ln α_i) sur des fiches toutes à α = 0,05 vaut 3 × un compte. Le point 5 de B (les témoins mesurent le juge, les mondes plantés mesurent les découvertes) s'applique en plein. (iii) Rétrodiction arXiv avec des modèles ouverts à date de coupe inconnue : la « vérité connue après coup » peut être dans les poids ; HYPOTHÈSE, non contrôlée. (iv) 5 générations dont la première à mémoire vide : 4 générations utiles, 10 graines, seuil +25 % « contre les deux autres bras » sans pilote de puissance (R-473).

**C8 — Registre de Brier : exigence hors de portée.** « Détecter avec une puissance ≥ 90 % une source dont les témoins faux survivent à 2α sur 50 fiches » : sous α = 0,05, 2,5 contre 5 survies attendues ; un test binomial à 5 % a une puissance de l'ordre de 0,4 (mon calcul, illustratif), pas 0,9. L'instrument « témoin de base » que C donne à battre ne peut pas atteindre la mesure minimale qu'il fixe ; donc rien ne peut la battre non plus.

**C9 — Faits et références.** (i) C range « Jaccard 3-grammes / SimHash normé » parmi les préfiltres de texte en citant G2 ; G2 dit : gain de SimHash **au niveau du mot** par construction, **indécis** au niveau du texte, −0,148 sur le corpus réel (B1-08 indécise ; le survivant B1-03 est la normalisation de la somme de SHA-256, pas SimHash). S2, ligne 1 de « ce qui survit », fait déjà cette confusion ; C la propage. (ii) Le titre donné pour Lehman et Stanley 2011 est tronqué (« …for novelty alone »). (iii) « vérifié par analogie avec G1/G2 qui ont coûté 0 USD » : un coût n'est pas vérifié par analogie ; c'est illustratif.

### (b) Scénarios d'évasion

| Instrument de C | Évasion | Coût |
|---|---|---|
| Garde Jaccard/SimHash | Paraphrase sous 0,5 ; ou re-sérialisation de la loi pour changer l'empreinte (C1) | script |
| L̃ + enveloppe convexe | Mélange puis inclinaison puis renommage : le déclencheur ne tire pas (C4) ; ou F0 | script |
| Enveloppe convexe avec lois constantes | Mélanger avec une **autre survivante** (non constante) : hors de l'enveloppe {p_arch} ∪ {constantes} ; déclarer la fille d'un seul parent | nul |
| Grille (Domaine, Opérateur) + Thompson sur I_c | Étiqueter la fiche dans la cellule à p̂ ≈ 0,5, déclarer une sévérité haute (C5, C6) | zéro |
| Contre-exemples locaux servis (« résiduelle négative à fort z_2 ») | Fille = parent + correction aveugle sur z_2 copiée du contre-exemple : passe le juge si le monde est stationnaire. Ce n'est pas une fraude, c'est l'apprentissage voulu ; mais rien ne distingue alors « a compris » de « a recopié le résidu », et la mémoire s'attribue un mérite qui est celui du résidu publié | un appel |
| Agrégateur en ligne (Expérience 2, bras 1) | Choisir λ hors de la grille si la grille est grossière ; l'agrégateur suit un point de grille voisin et perd un écart linéaire en n | script |
| Témoins | F1 ; de plus, C sert des « statistiques par cellule » : une cellule où une fiche est survenue sans apparaître en mémoire est un témoin | zéro |

**Tous à la fois** : colonne inerte + mélange avec une survivante non déclarée, incliné + étiquette de cellule choisie + sévérité déclarée haute. Zéro appel de modèle. Ce qui l'arrête : rien dans C, sauf le juge — dont C a justement décidé, par Expérience 2 bras 2, de ne pas modifier le nul.

### (c) Contrôles négatifs fatals

1. **Expérience 1 — déclarer l'empreinte.** Pour chaque tricheur, dire si `loi_predictive` est octet-identique ; rapporter H_A séparément sur les deux sous-ensembles. Ajouter la composition mélange∘inclinaison∘renommage (C4). Sans cela, la comparaison H_A/H_B mesure le générateur de tricheurs.
2. **Expérience 2 — deux agrégateurs.** Bras 1a : mélange d'experts simple ; bras 1b : mélange sur grille (λ, q). Si 1a échoue et 1b passe, C2 est confirmée et H_A n'était pas testée. Reproduire d'abord l'artefact de J2 sur une **graine neuve** (777 est exploratoire, non opposable) : s'il n'est pas vu, le banc n'a pas de dents (R5).
3. **Expérience 2 — τ_pred fixé sur des filles honnêtes scellées avant les tricheurs** (C3), et rapport du taux de filles honnêtes à ε = 0,05 refusées par la garde.
4. **Expérience 3 — plan factoriel** {garde on/off} × {consigne : vide / placebo / vraie} × {orientation : uniforme / I_c}, sinon aucune attribution (C7-i) ; **mondes plantés** avec gain oracle tenu par le noyau au lieu de « vrai sur l'évaluation scellée » (C7-ii) ; **A/A** ; **redites proposées avant garde** ; **classifieur de témoins sur (population, mémoire)** (F1) ; pour arXiv, un contrôle de contamination (fiches dont la vérité est postérieure à la date de coupe déclarée du modèle ; si indisponible, retirer le banc).
5. **Estimateur de survie par région — le contrôle que C annonce en (a)5 et oublie en (b)** : une cellule fabriquée de tautologies et d'absurdités à survie 0,5 doit recevoir un I_c élevé **et** un gain oracle nul ; si l'orientation par I_c y envoie du budget, C5 est démontrée et l'instrument est rejeté. Un bras à descripteurs calculés par le noyau contre descripteurs déclarés (C6).
6. **Registre de Brier — calcul de puissance avant toute exigence** (C8) : donner l'effectif de témoins faux nécessaire pour 0,9 de puissance à 2α ; s'il dépasse ce qu'une course produit, l'instrument n'existe pas à cette échelle.

---

## Ce que je retiens pour la cellule A (en le disant)

- Je prends à B la **fermeture aveugle dans le juge** et la distinction « économie / validité », mais je tiens que la fermeture doit porter sur **l'ensemble des survivantes** ou que l'archive ne doit pas servir les fermetures au proposeur : les deux ne sont pas compatibles (B1).
- Je prends à C la **L̃ doublement centrée** comme signature contre l'inclinaison, et sa remarque (a)2 que la redite modulo l'aveugle est d'abord un défaut du juge.
- Contre les deux : **le noyau doit posséder le schéma de traits** (F0) et **ce qui est servi doit être testé comme surface de fuite des témoins** (F1). Une expérience unique les départage : H_A « avec schéma possédé par le noyau, le proposeur scripté "tous à la fois" est promu ≤ α » contre H_B « il reste promu > α (borne basse de Wilson), parce que le trou est dans le nul, pas dans le schéma ». Si H_A tient, les gardes de mémoire de B et C redeviennent de pures économies ; si H_B tient, c'est le nul du juge qu'il faut refaire avant toute mémoire.

FIN-DE-CELLULE