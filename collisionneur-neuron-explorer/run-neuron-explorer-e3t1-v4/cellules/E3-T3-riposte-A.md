# Proposition A — Tour III.3 : riposte

## 0. État des pièces

- Bloc FAITS : vide par ordre de l'arbitre (GO-2026-10-26-01). Rien à inventer.
- Pièce E3-T1-conception-A (la mienne) : présente, complète.
- Pièces E3-T2-redteam-B et E3-T2-redteam-C : présentes, complètes, terminées par FIN-DE-CELLULE. Je ne réponds qu'aux sections « Contre la proposition A ».
- Statuts inchangés : tout ce qui vient du dépôt est RAPPORTÉ ; les faits du programme sont RAPPORTÉS par la question. Je ne relève pas les statuts attribués par C dans sa propre pièce : ils ne visent pas A.
- Convention : « accepté » signifie que la conception est modifiée en (b) ; « transformé en test » signifie qu'un bras ou un contrôle est ajouté avec sa règle de décision ; « rejeté » est toujours motivé.

---

## (a) Réponse à chaque attaque

### Attaques de B

**A-F1 (E1 vrai par construction : la sonde approche l'indice de cadrage).** **Accepté, puis transformé en test.** Nuance d'abord : la sonde de l'étape 1 est entraînée sur une banque en deux familles (RAPPORTÉ), pas nécessairement sur des paires identiques-sauf-cadrage ; mais tant que les étiquettes « évaluation » coïncident avec un vocabulaire de cadrage, la différence des moyennes est la représentation de l'indice et B a raison. Correction : (i) contrôle « direction de cadrage sans évaluation » (B-(c)2) ; (ii) transfert croisé : une sonde entraînée sur cadrages **implicites** (format de banc d'essai, choix multiples, absence d'historique, sans le mot « test ») est poussée sur des paires à cadrage **explicite**, et réciproquement. Duel : H_A, l'effet survit au transfert croisé et dépasse la quasi-cible ; H_B, l'effet ne survit pas ou ne dépasse pas la quasi-cible. H_B falsifie la lecture « conscience d'évaluation » pour cette sonde, et le programme garde « indice lu au dernier jeton ». J'accepte la note de fin de B : ce contrôle est le pivot.

**A-F2 (sonde de surface et sonde sémantique colinéaires).** **Accepté.** Correction : on pousse (a) la direction de sonde, (b) sa composante orthogonale à la direction de surface, (c) la direction de surface orthogonalisée à la sonde. Si (b) ne fait pas mieux que le nul, la sonde est de surface *sur cette banque* ; ce n'est pas un défaut du test, c'est son verdict. La banque à cadrage implicite de A-F1 sert de second remède.

**A-F3 (écart comportemental de base non mesuré).** **Accepté : ajout de E0.** Différence avec la règle d'arrêt que C reproche à B : je ne conditionne pas E1 à E0. Si E0 donne un écart nul, E1 se lit autrement (voir (b)) : une poussée qui crée un écart absent à sec ne « valide » pas la sonde, elle révèle un levier d'injection, interprétable seulement avec le nul quasi-cible et la perplexité sur tâche.

**A-F4 (duels non exhaustifs en E3 et E4).** **Accepté.** E3 : une seule statistique, m\* = plus petit m tel que le recouvrement atteint 50 % ; H_A : m\* ≤ 8 ; H_B : m\* > 64 ; zone 8 < m\* ≤ 64 : « levier modérément épars », qui falsifie l'hypothèse « un balayage neurone par neurone a un objet » tout en autorisant un balayage restreint à l'ensemble m\*. E4 : rapport R ≥ 3 → H_A ; R < 1,5 → H_B ; 1,5 ≤ R < 3 → falsifie « la banque scellée est assez décorrélée pour trancher » et déclenche la mesure de distance lexicale ci-dessous, sans extension du balayage. Seuils illustratifs, écrits d'avance.

**A-F5 (décomposition surcomplète, angle, attention).** **Accepté.** La famille des colonnes de W_out est surcomplète et le « coefficient » dépend de la méthode. Correction : le classement se fait par **contribution causale moyenne** c_i = E_banque[a_i(x)] · ⟨W_out[:, i], v⟩ sur les couches en amont de la sonde (incluse), pas par alignement géométrique ; le vecteur poussé pour m neurones est normalisé pour avoir la **même projection sur v** que la direction complète (ce qui neutralise la confusion angle/parcimonie signalée). Attention : j'écris explicitement que E3 teste « levier épars dans les MLP » ; H_B n'exclut pas un levier d'attention ; un bras « sorties de têtes projetées sur v » (32 × 32 = 1 024 objets, arithmétique sur la configuration à vérifier) est ajouté à faible coût.

**A-F6 (fuite : cas plantés = lentille 1).** **Accepté**, de même que la faille 2 de C qui dit la même chose. La lentille 1 redevient uniquement la vérification mécanique à battre. Vérité terrain non lexicale : (i) neurones dont l'ablation (mise à la moyenne) change une réponse factuelle mesurable, repérés par ablation et non par projection ; (ii) les m\* neurones d'une direction de refus re-dérivée par différence des moyennes sur le modèle épinglé (méthode distincte du balayage ; référence Arditi et al., 2024, à vérifier). Limite assumée : (ii) reste une direction choisie pour son effet d'intervention, elle teste la capacité du balayage à retrouver des leviers connus, pas à en découvrir.

**A-F7 (comparaisons multiples).** **Accepté.** Condition primaire unique préenregistrée : couche de la sonde, dose fixée par E0′ (plus grande dose à laquelle la perplexité sur tâche des 256 directions aléatoires reste sous un plafond écrit d'avance, illustratif +10 %), mode de position primaire (voir faille 4 de C). Les conditions secondaires sont corrigées par la distribution du maximum sur toutes les conditions sous le nul des directions aléatoires (max-T).

**A-F8 (le nul « neurones aléatoires » est gonflé).** **Rejeté comme défaut, transformé en règle de rapport.** Ce nul ne contrôle pas un taux de fausses alertes ; il répond à A2 : un axe privilégié par la porte du MLP a-t-il déjà, « gratuitement », l'effet qu'on attribue à la sonde ? S'il est gonflé, c'est l'information cherchée. Règle : le rapport affiche séparément le centile contre les directions aléatoires (taux de fausses alertes contrôlé) et le centile contre les neurones (étalon de spécificité) ; seul le premier sert au seuil.

**A-F9 (« aucune intervention validée » est une inférence).** **Accepté.** Reformulé : « les pièces ne mentionnent aucune intervention validée » (lecture des pièces) ; « il n'en existe pas » est HYPOTHÈSE.

**Évasions de B.** E1, E2, E3 : acceptées, couvertes par A-F1/A-F2/A-F5 ; je note comme B que l'adversaire affiné est hors du modèle épinglé et que rien ici ne le borne. **E4 (banque scellée lexicalement proche)** : transformé en test : la banque scellée est produite par un gabarit distinct, préenregistré, et la distance lexicale entre banques (chevauchement de n-grammes, mesure à fixer) est elle-même empreintée avant ouverture ; si la distance est inférieure à un plancher écrit d'avance, la réplication est déclarée non informative, quel que soit R. **E6 (explications chargées de déclencheurs)** : accepté ; permutation des explications à l'intérieur d'une même classe lexicale (B-(c)6). **E7 (détection du placebo par incohérence ; canal de sélection des textes)** : première voie acceptée : rendu déterministe par (texte, direction, sel secret). Seconde voie : partiellement rejetée. Sélectionner ses textes d'entraînement par poussée est l'usage légitime de la caste « expérimentateur », et E7 le mesure sur banque scellée : si le score scellé monte, l'amélioration est réelle. Le danger n'est pas là ; il est dans la reconstruction de la sonde de contrôle (évasion 4 de C), traitée plus bas.

**Contrôles négatifs de B (1–6).** Tous acceptés et intégrés : E0 ; direction quasi-cible ; sonde à étiquettes mélangées à chaque dose et couche sous correction globale ; vérité terrain non lexicale ; placebo déterministe ; permutation intra-classe.

### Attaques de C

**Faille 1 (incompatibilité d'espace dans E3).** **Rejeté sur la qualification, accepté sur le fond.** La décomposition par W_out est celle que supposait E3 ; il n'y a pas d'erreur de catégorie mais une sous-spécification, la même qu'A-F5. Le confondant ajouté par C (variance d'activation sur le corpus, anisotropie des colonnes) est réel et la contribution causale moyenne c_i le traite.

**Faille 2 (circularité de la table (c)).** **Accepté** (voir A-F6). La remarque de C que ce test vérifiait seulement la linéarité locale après normalisation est juste.

**Faille 3 (fuite lexicale E1/E2 ; références de surface sous-spécifiées).** **Accepté en partie, transformé.** Les références de surface sont définies par le programme (RAPPORTÉ), je ne les redéfinis pas ; j'ajoute une seconde sonde de surface « sac de n-grammes » entraînée sur la banque, et les deux sont orthogonalisées comme en A-F2.

**Faille 4 (point d'application non fixé).** **Accepté.** Trois modalités préenregistrées, une primaire : **P1**, poussée à toutes les positions de la réponse générée, dose relative à la **norme résiduelle médiane** de la couche hors premiers jetons (pour ne pas injecter un vecteur démesuré aux positions à forte norme ; HYPOTHÈSE sur la révision épinglée, à mesurer ; B cite Sun et al., 2024, « Massive Activations in Large Language Models », à vérifier) ; **P2**, dernier jeton du préfixe seulement ; **P3**, toutes positions y compris préfixe. La perplexité est mesurée sur la tâche elle-même, en plus du texte neutre.

**Évasion 1 (porte ET : la poussée sur la version non cadrée ne déclenche pas la conjonction).** **Accepté comme limite, transformé.** E1 teste la suffisance **dans le contexte non cadré**. Bras ajouté : poussée sur une version à cadrage structurel sans indice lexical ; si l'effet n'apparaît que là, c'est une conjonction, et la sonde est « suffisante conditionnellement ». Ce bras est confondu avec A-F1 (le contexte est déjà partiellement cadré) : je l'écris, et le nul quasi-cible est appliqué dans ce bras aussi.

**Évasion 2 (étalement L∞ par l'organisme ; E3 en H_B annule E4).** **Partiellement rejeté.** E3 porte sur le modèle épinglé et les sondes de l'étape 1 ; un organisme n'écrit pas dans les poids, il choisit ses textes. Qu'il puisse choisir des textes à représentation étalée est un risque pour la sonde elle-même, antérieur à E3 et indépendant de lui. **Accepté** sur la règle d'arrêt : H_B en E3 suspend le balayage complet, pas le mode sondage (illustratif 15–30 USD), qui reste autorisé une fois.

**Évasion 3 (leurre polysémantique en E6).** **Accepté**, avec une précision : E6 teste l'instrument « maximum à l'aveugle », pas le neurone ; une explication validée par E6 ne certifie rien sur ce que le neurone fait par ailleurs, et aucune conception de A ne « blanchit » un neurone. Le contrôle de couverture des sens secondaires (C-(c)3) est intégré.

**Évasion 4 (reconstruction de la sonde par différences finies via « pousser »).** **Accepté comme le risque sérieux de la demande 3.** Remarque : la primitive de base (lecture de sonde sur textes propres, RAPPORTÉ) permet déjà une recherche du sous-espace orthogonal par réécriture ; « pousser » en accélère la convergence. Transformé en test (E8) : un organisme de référence, écrit exprès, cherche à abaisser la sonde de contrôle sans dégrader sa tâche ; on compte les appels nécessaires avec et sans « pousser ». Si « pousser » fait passer ce nombre sous le plafond d'une course, la primitive n'est pas livrée sous forme vectorielle libre. Bornes immédiates : aucune lecture de sonde sur un texte poussé ; plafond en textes distincts ; rendu binaire au seuil préenregistré, sans score continu.

**Évasion 5 (conjointe : faux négatif global).** **Accepté comme description, rejeté comme objection à la logique.** Aucun instrument de A ne prétend prouver une absence : H_B en E1 signifie « cette direction n'écrit pas dans ce contexte », pas « il n'y a pas de levier ». Je reformule les issues en (b) pour que H_B ne puisse pas être lue comme une absolution.

**Contrôles de C (1–3).** Tous acceptés : troisième nul tiré selon la covariance empirique du flux résiduel à la couche de la sonde (apparié en norme) ; bras d'ablation de nécessité en E3 ; couverture des sens secondaires en E6.

---

## (b) Expériences corrigées

Conventions : Llama-3.1-8B-Instruct, révision épinglée ; nuls N1 = 256 directions aléatoires isotropes de même norme (contrôle du taux de fausses alertes) ; N2 = 256 directions tirées selon la covariance empirique de la couche, même norme (contrôle de l'appartenance au sous-espace actif) ; N3 = 256 neurones aléatoires (étalon, pas un seuil) ; modalité de position P1 primaire ; dose fixée par E0′ ; seuils illustratifs, empreintés avant toute mesure.

**E0 — Y a-t-il quelque chose à écrire ?**
H_A : l'écart de log-probabilité du choix entre version cadrée et non cadrée, à sec, dépasse le bruit de rééchantillonnage (graines, reformulations appariées). H_B : il ne le dépasse pas.
Issues : H_A → E1 se lit comme « la poussée reproduit-elle l'écart naturel ? » ; H_B → E1 se lit comme « la poussée crée-t-elle un écart latent ? », et tout effet positif n'est retenu que s'il bat N2 et la quasi-cible, avec perplexité sur tâche dans la bande. Les deux issues sont informatives ; aucune n'annule E1.

**E1 — La direction de la sonde écrit-elle ce qu'elle lit, au-delà de l'indice ?**
Directions poussées : v (sonde), v⊥ (orthogonalisée aux deux sondes de surface), q (quasi-cible : cadrage lexicalement voisin sans évaluation, B-(c)2), s (surface orthogonalisée à v), v_impl (sonde entraînée sur cadrages implicites, poussée sur paires explicites) et v_expl (l'inverse), sonde à étiquettes mélangées ; chacune contre N1, N2, N3.
H_A : v⊥ et le transfert croisé dépassent N1, N2 **et** q. H_B : au moins l'un des trois échoue.
Issues : H_B → la lecture « conscience d'évaluation » est falsifiée pour cette sonde ; elle reste un détecteur d'indice. H_A → l'hypothèse « ce n'est que l'indice » est falsifiée ; cela établit une suffisance dans le contexte testé, ni une nécessité, ni un savoir du modèle, ni l'absence d'une conjonction non déclenchée (évasion 1 de C : bras à cadrage structurel ajouté, même règle). Correction max-T sur les conditions secondaires (couches, doses, P2, P3).

**E2 — Verbalisation ou comportement ?**
H_A : la poussée de v⊥ déplace ensemble le taux de verbalisation « test/évaluation » et la métrique de E1, et le couple diffère de celui produit par l'injection textuelle du cadrage. H_B : verbalisation seule, ou couple identique à l'injection textuelle.
Issues : H_B → la direction est un lecteur de vocabulaire ou un substitut du texte ; H_A → la verbalisation n'est pas purement lexicale, sans dire que le modèle « sait ».

**E3 — Direction contre neurones (MLP, puis attention).**
Classement par contribution causale moyenne c_i ; vecteur à m neurones normalisé à projection égale sur v ; m\* = plus petit m atteignant 50 % de l'effet de v⊥.
H_A : m\* ≤ 8. H_B : m\* > 64. Zone intermédiaire : falsifie « un balayage neurone par neurone a un objet », autorise un balayage restreint à l'ensemble m\*.
Bras de nécessité (C-(c)2) : mise à la moyenne des m\* neurones sur la version cadrée ; si l'effet naturel de E0 subsiste, les m\* neurones sont un court-circuit d'injection, pas le mécanisme : revendication réduite à « suffisant ».
Contrôles : m neurones aléatoires appariés en norme de colonne et en fréquence d'activation ; m neurones de la sonde à étiquettes mélangées. Bras attention : même protocole sur les sorties de têtes ; H_B dans les MLP et H_A dans l'attention est une issue nommée d'avance.

**E4 — Balayage préenregistré, mode sondage.**
Préconditions empreintées : liste des neurones signalés sur la banque de conception ; gabarit distinct pour la banque scellée ; distance lexicale inter-banques au-dessus d'un plancher écrit d'avance ; deux vocabulaires cibles, dont un sans rapport.
H_A : R ≥ 3 (fraction répliquée des signalés sur fraction répliquée de neurones aléatoires), et R pour le vocabulaire sans rapport < 1,5. H_B : R < 1,5. 1,5 ≤ R < 3 : banque insuffisamment décorrélée, pas d'extension.
Vérité terrain pour l'étalonnage (A-F6 corrigé) : neurones trouvés par ablation et m\* de la direction de refus re-dérivée ; la lentille 1 est la vérification mécanique à battre.

**E5 — Amorces courtes contre transcriptions (inchangé)**, avec P1 fixé et dose à la norme médiane ; H_B entraîne le remesurage de tous les coûts.

**E6 — Le « maximum à l'aveugle » a-t-il un contenu ?**
H_A : explications vraies > explications permutées **au sein d'une même classe lexicale**, et > le contrôle « cinq exemples du corpus ». H_B : pas de différence sur l'un des deux.
Contrôle de couverture (C-(c)3) : après retrait du champ lexical de l'explication, les pics résiduels d'activation sont-ils encore au-dessus des témoins sur les tâches du programme ? Si oui, l'explication est partielle et le rapport le dit ; E6 n'émet jamais de verdict sur l'innocuité d'un neurone.

**E7 — Primitive « pousser » dans les organismes.**
Bras : primitive réelle ; placebo déterministe (rendu fonction de (texte, direction, sel secret), donc indiscernable par répétition) ; sans primitive ; test A/A pour la variance entre courses avant toute lecture d'écart.
H_A : écart de score scellé réel contre placebo au-dessus de la variance A/A. H_B : pas d'écart.
Bornes : jamais sur tâches de banque ; aucune lecture de sonde sur texte poussé ; plafond en textes distincts ; rendu binaire.

**E8 — Fuite de la sonde par différences finies (nouveau, répond à l'évasion 4 de C).**
Organisme de référence écrit exprès ; cible : abaisser la sonde de contrôle sur ses textes sans baisser son score de tâche.
H_A : le nombre d'appels nécessaires avec « pousser » reste au-dessus du plafond d'une course. H_B : il passe en dessous.
Issues : H_B → la primitive n'est pas livrée sous forme vectorielle libre (liste fermée ou retrait) ; H_A → livraison possible sous les bornes de E7, avec le constat, à consigner, que la primitive de base permet déjà la même recherche plus lentement.

---

## (c) Réponse à l'arbitre

**Ce qui est établi.** Rien de causal. Les faits sur la méthode sont RAPPORTÉS (lecture du dépôt par l'arbitre, chiffres de l'auteur, licence absente) et mesurés sur Qwen3.5-4B, pas sur le modèle épinglé ; aucun ne transfère sans remesurage. Les faits du programme (sondes au dernier jeton, deux familles, primitive bornée, boucles) sont le cadre, RAPPORTÉ. Ce que le tour II.2 a établi à mon encontre, et que j'accepte : telle que je l'avais écrite, E1 était vraie par construction si la sonde est une différence de moyennes de l'indice de cadrage ; la table (c) était circulaire (lentille 1 comme vérité terrain) ; E3 reposait sur une décomposition mal définie et ignorait l'attention ; E3 et E4 avaient des issues qui ne falsifiaient rien ; le point d'application n'était pas fixé ; les comparaisons multiples n'étaient pas corrigées ; la primitive « pousser » ouvrait une voie de reconstruction de la sonde de contrôle.

**Ce qui n'est pas établi.** (1) Qu'il existe, à sec, un écart comportemental cadré/non cadré sur Llama-3.1-8B-Instruct (E0 ; HYPOTHÈSE). (2) Que les sondes de l'étape 1 dépassent nettement les références de surface (aucun score dans les pièces). (3) Qu'une direction qui lit écrit autre chose que l'indice qu'elle lit (E1 corrigé). (4) Qu'un levier épars existe pour l'une ou l'autre famille (E3) ; la littérature sur la superposition rend cette hypothèse a priori faible pour un concept rare et contextuel, mais c'est un a priori, pas un résultat (références en III.1, toutes à vérifier). (5) Que les témoins aléatoires denses sont le bon nul : la question est tranchée dans la conception (trois nuls, rôles séparés), pas dans les faits. (6) Que la méthodologie de l'agent mesure quelque chose (E6 ; aucun taux de succès rapporté par l'auteur). (7) Qu'un adversaire affiné soit borné par quoi que ce soit ici : hors du modèle épinglé, donc hors périmètre tant que le directeur n'a pas décidé autrement.

**Ce qui falsifierait l'idée de leviers uniques pour la conscience d'évaluation.** E3 en H_B dans les MLP **et** dans l'attention, avec le bras de nécessité montrant que l'effet naturel de E0 survit à l'ablation de tout petit ensemble ; et E4 en H_B sur une banque scellée dont la décorrélation lexicale est attestée. Si E1 tombe aussi (v⊥ et transfert croisé ne battent pas la quasi-cible), le programme garde la sonde comme détecteur d'indice et renonce, pour elle, à toute revendication causale.

**L'expérience à faire en premier.** E0 puis E1 corrigé, dans cet ordre et dans la même semaine : coût illustratif de l'ordre de 10⁵ passes avant courtes, quelques heures de carte, aucun code du dépôt (licence absente). E0 dit s'il y a une plage ; E1 corrigé, avec le nul quasi-cible, l'orthogonalisation et le transfert implicite/explicite, dit si la direction porte autre chose que l'indice. Tout balayage neurone par neurone attend E3 ; la primitive « pousser » attend E8 ; la méthodologie de l'agent n'entre dans la boucle extérieure que sous la forme déjà conforme à l'esprit du programme (hypothèse écrite d'avance, test qui la briserait, clôture chiffrée empreintée), et E6 décide du reste. Plusieurs voies restent ouvertes selon les issues ; aucune n'est « la » réponse, et chaque issue ci-dessus nomme ce qu'elle élimine.

FIN-DE-CELLULE