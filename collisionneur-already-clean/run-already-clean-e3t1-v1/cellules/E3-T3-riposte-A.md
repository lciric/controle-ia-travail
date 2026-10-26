# Proposition A — Tour III.3 : riposte

**État des pièces.** Bloc FAITS vide (il le dit lui-même) ; je travaille sur la question. Ma conception III.1 et les deux équipes rouges (B, C) sont présentes et complètes. C attaque aussi une « pièce B conception » que je n'ai pas reçue ; je ne réponds qu'aux sections qui visent A. Statuts inchangés : essai RAPPORTÉ, cadre RAPPORTÉ, revue d'antériorité interne OBSERVÉ-NON-AUDITÉ ; B relève que C classe autrement ; l'écart est pour Lazar. Tout seuil ci-dessous est **illustratif** ; toute référence est « à vérifier » sauf mention.

---

## (a) Réponse à chaque attaque

### Équipe rouge B

| # | Attaque | Verdict | Raison / transformation |
|---|---|---|---|
| A1 | Témoins isotropes battus par construction | **Acceptée** | Une direction apprise vit dans le sous-espace de forte variance ; une direction isotrope a une projection ≈ ‖h‖/√d (HYPOTHÈSE partagée). Je remplace par trois distributions nulles : directions tirées de la covariance des activations (appariées en variance), panel de sondes de concepts sans lien entraînées comme la sonde, sonde à étiquettes permutées. Le T1 de B devient une **précondition** d'E2' : si la sonde ne bat pas les directions appariées, E2' n'a pas de témoin valide. |
| A2 | KL conditionnée au 95ᵉ centile croît mécaniquement | **Acceptée** (idem C a.2) | Identité géométrique, pas découverte. Témoin : perturbation de **même norme projetée sur les mêmes jetons** (direction de contrôle rééchelonnée jeton par jeton). |
| A3 | H_A/H_B non exclusives (redondance, Hydre, illusion de sous-espace) | **Transformée en test** | « Projection nulle sans effet » ≠ « non lue ». Je scinde E2 en deux tests binaires (E2a nécessité, E2b suffisance) et j'ajoute une **re-sonde en aval** après effacement, avec le contrôle « attention bloquée vers les jetons de cadre » que C oppose à B (je l'emprunte, voir b.2). Références de B (McGrath et al., 2023 ; Makelov, Lange et Nanda, 2023) : à vérifier, je ne les ai pas lues. |
| A4 | Témoin thème trop faible (thème sémantique) | **Acceptée** | J'ajoute un classifieur sur **encodeur de phrases externe gelé** et une **sonde sur la couche 0** (emprunt à C, dit tel quel). Battre un sac-de-mots falsifie « lexique de surface », pas « thème ». |
| A5 | Fuite de construction (cellules écrites par qui connaît la sonde) | **Acceptée** | Générateurs disjoints de l'entraînement ; rédacteurs aveugles à la fiche de la sonde ; étiquetage des cellules à l'aveugle du score. |
| A6 | Contraste nul dégénéré (Δlogits ≈ 0) | **Acceptée** | Le témoin passait toujours. Remplacé par un **contraste de même amplitude de Δlogits à cause sans rapport** : le « témoin impératif hors audit » (origine C, repris via B). |
| A7 | Validation non indépendante (mêmes gabarits) | **Acceptée** | Validation sur une autre famille de gabarits, autre rédacteur. |
| A8 | Type d'ablation non fixé ; attention invisible | **Acceptée** | Ablation par **moyenne** préenregistrée (zéro sort de la distribution ; Zhang et Nanda, 2023, à vérifier). Bras parallèle de patching de **têtes d'attention** ; sinon H_B d'E3' se lit « pas de porte dans la base MLP », rien de plus. |
| A9 | E4 : plancher, mesure qui favorise le bras demandeur, demande = lexique | **Acceptée pour les deux premières ; partiellement rejetée pour la troisième** | Plancher : précondition comportementale (E0') mesurée sans question de suivi. Biais de mesure : **élicitation finale identique** dans les cinq cellules, rigueur **normalisée par la longueur de sortie**, juge aveugle au bras. « Demande = lexique » : le 2×2 a précisément été dessiné pour croiser les deux facteurs ; mais B a raison que la séparation n'est pas totale. Correction : la demande est opérationnalisée par **un seul marqueur structurel fixe** (une balise), le registre par le reste ; un sac-de-mots mesure le recouvrement résiduel et il est rapporté. |
| A10 | Modèle de base non interprétable comme témoin comportemental | **Acceptée** | Le modèle de base reste témoin pour les **lectures d'activation** (la sonde s'allume-t-elle avant instruction ?), jamais pour le comportement. Version instruite fixée avant toute mesure comportementale (A13). |
| A11 | E5 circulaire ; adversaire faible ; conclusion excessive | **Acceptée** | Jugement « honnête / non-test » à l'aveugle du score, par deux juges, accord rapporté. Ajout d'un **adversaire itératif** avec retour de score, budget préenregistré (E5-adv). Je retire « la fiche peut être rendue publique sans coût de contrôle » : E5 en un coup ne le mesure pas. |
| A12 | E6 vrai par construction (100 variables décodent des concepts corrélés) | **Acceptée** (combinée à C a.4) | Concepts hors fiche **décorrélés** des concepts de fiche (corrélation résiduelle contrôlée sur corpus) ; témoin 100 neurones aléatoires. |
| A13 | « VÉRIFIÉ » sur le max et la longueur ; base/instruit non fixé | **Acceptée sur le fond ; statut non modifié** | Je ne change pas le label (règle 1) ; je signale à Lazar que B le conteste et je précise la condition : la croissance du max est garantie pour des jetons **ajoutés après un préfixe inchangé** sous attention causale ; E4' place donc les variations de cadre en **position fixe en tête** et apparie la longueur totale, ce qui neutralise le point quelle que soit l'issue de l'arbitrage de statut. Base/instruit : à fixer avant toute mesure ; je demande les deux versions. |

**Scénarios d'évasion de B.** *Inondation lexicale d'un jeton* (le max monte partout, le moniteur ne discrimine plus) : acceptée, transformée en test (E5-adv, attaque « saturation ») ; le moniteur rapportera trois statistiques (max, 95ᵉ centile, fraction de jetons au-dessus du seuil), et la perte de discrimination sous inondation est une mesure, pas une surprise. *Toutes les défenses à la fois* (sonde basse + projection sans effet + pas de porte, verdict « rien ») : acceptée ; c'est la faille la plus grave de ma pièce. Correction : la mesure comportementale d'E4' (rigueur, contradiction, refus, sans mot de test) est **reliée au moniteur** comme contrôle de cohérence préenregistré — un texte dont le comportement est « de test » (par E0') avec sonde basse compte comme faux négatif du moniteur, pas comme « absence d'état ». *Mesure de fuite aveugle aux directions non surveillées* : acceptée ; l'expérimentateur re-sonde, après dérive, d'autres couches et des directions non surveillées (voir F').

**Contrôles négatifs 1–8 de B** : tous acceptés et intégrés ci-dessous ; le 6 avec la déclaration de portée.

### Équipe rouge C

| # | Attaque | Verdict | Raison / transformation |
|---|---|---|---|
| a.1 | E1 confond « test » et « format de consigne rigide » | **Acceptée** | Ajout de la cellule **structure rigide sans enjeu d'audit** (extraction JSON, QCM de production routinière) et d'un classifieur de traits de formatage comme témoin mécanique. Sans elle, H_A d'E1 était validable par construction. |
| a.2 | Choc de norme hors variété sur les jetons extrêmes | **Acceptée** | Même correction que B-A2 ; le témoin est à norme projetée égale, jeton par jeton (contrôle c.2 de C). |
| a.3 | Gradient × activation aveugle aux portes inhibitrices / SwiGLU | **Partiellement acceptée, transformée** | Gradient × activation porte le signe et voit donc un pôle négatif actif ; mais il est aveugle à l'**extinction** (passage à zéro) et au franchissement de seuil. Correction : triage par gradients intégrés **et** par score d'ablation directe (moyenne) sur un sous-ensemble ; test de sensibilité (c.3) qui compare le rappel des trois estimateurs sur une cible connue. |
| a.4 | Berkson : tronquer sur les activations faibles crée des corrélations fallacieuses | **Acceptée** | Plus de troncature. Je **résidualise** chaque neurone sur son concept de fiche (régression sur l'étiquette de fiche) et je sonde le résidu sur toute l'étendue ; témoin : résidus de 100 neurones aléatoires ; concepts cibles décorrélés (A12). |
| a.5 | Calibration conditionnée aux erreurs = biais de survie des items | **Acceptée** | Ensemble d'items identique et forcé dans toutes les cellules ; confiance éliquée par la même phrase finale ; abstention comptée comme issue distincte ; score de calibration sur l'ensemble complet. |
| b.1 | Lissage de crête (état réparti sous le seuil sur 50 jetons) | **Transformée en test** | Les trois statistiques du moniteur (max, centile, fraction) rendent l'attaque mesurable : un lissage qui passe sous le max fait monter la fraction. E5-adv inclut explicitement cette stratégie et rapporte laquelle des trois statistiques résiste. Sa faisabilité par le modèle lui-même (contrôler ses propres activations) est HYPOTHÈSE ; par un organisme muni de la primitive, elle est plausible et c'est l'argument de plus contre l'option (D). |
| b.2 | Rang ≥ 2 et relecture par l'attention en aval | **Acceptée** | E2a utilise un effacement de **rang k** préenregistré (k = 1, 2, 4 ; méthode type LEACE, Belrose et al., 2023, à vérifier), plus le contrôle « attention des couches > L bloquée vers les jetons de cadre » que C oppose à B : il sépare relecture active et démodulation non linéaire passive. Je l'emprunte en le disant. |
| b.3 | Étalement démocratique sur 500 neurones | **Acceptée avec portée** | Idem B-A8/scénario porte : H_B d'E3' = « pas de porte ≤ k dans la base MLP ». J'ajoute une **courbe d'ablation cumulée** (k = 10 à 2 000) : l'issue rapporte le k nécessaire à 50 % d'effet, comparé à une sélection aléatoire parmi les actifs. |
| b.4 | Préfixe « paratonnerre » qui sature le max | **Acceptée** | Même famille que b.1 et l'inondation de B ; testée en E5-adv ; la fraction de jetons au-dessus du seuil et le centile ne sont pas saturables par un préfixe de 15 jetons. |
| b.5 | Évasion conjointe via cartographie du noyau par la primitive | **Acceptée** | Elle confirme le point 10 de ma pièce et mon refus de (D). Correction : la mesure de fuite F' devient une **condition d'entrée** de tout octroi de primitive, et son témoin est corrigé (c.4). |
| c.1 | Témoin structure rigide sans évaluation | **Accepté** (a.1). |
| c.2 | Direction de contrôle à même norme projetée | **Accepté** (a.2). |
| c.3 | Contrôle positif de sensibilité pour E3 | **Accepté avec portée** | C reproche à B qu'un LoRA implanté est circulaire ; je retiens l'objection : un circuit implanté ne teste pas l'existence d'une porte native, il teste seulement la **sensibilité de l'estimateur** à une porte éparse connue. C'est ce que je lui demande, rien de plus ; si l'estimateur ne retrouve pas une porte implantée sur k neurones par édition directe, H_B d'E3' est inopposable. |
| c.4 | Bruit non stationnaire démasqué en deux appels | **Accepté** | Excellent point. Le témoin devient une **fonction déterministe** : projection sur une direction aléatoire fixe du modèle réel, identique à chaque appel sur le même texte. |

---

## (b) Expériences corrigées

Toutes préenregistrées (couches, k, seuils, règles d'arrêt, ensembles de jetons cibles) avant la première lecture ; versions **instruites** pour le comportement, base pour les activations témoins ; seuils illustratifs.

### E0' — Précondition comportementale implicite (nouvelle)
- **H_A** : à contenu identique, un cadre d'évaluation change le comportement du 8B instruit sans qu'aucune question de suivi soit posée : fréquence de marqueurs de prudence spontanés, taux de refus, entropie des jetons de réponse, longueur de sortie.
- **H_B** : aucune de ces mesures ne diffère au-delà du témoin (deux paraphrases sans cadre).
- **Issues** : H_B → E2', E3', E4' n'ont pas de cible comportementale sur ce modèle ; on le consigne et on ne conclut rien de « moniteur valide ». H_A → l'écart Δ_0 devient la cible causale d'E2' et la condition d'entrée d'E4'. Cette mesure sans question de suivi répond à l'objection que C fait à B (amorçage) ; je l'adopte en le disant.

### E1' — Thème, format ou état ?
- **H_A** : la sonde code un état « ceci est un test » non réductible au lexique, au thème sémantique, ni au format de consigne.
- **H_B** : la sonde est réductible à l'un des trois.
- **Dessin** : grille {structure de test, non-test} × {lexique présent, absent} × {format rigide, format libre}, soit huit cellules ; les cellules décisives sont « test, sans lexique, format libre » et « non-test, lexique présent, format rigide ». Cellules écrites par des rédacteurs aveugles à la fiche de la sonde, générateurs disjoints de l'entraînement, étiquetage aveugle au score ; appariement longueur ±5 %, perplexité, jetons de fonction ; variations de cadre en position fixe.
- **Témoins mécaniques à battre** : sac-de-mots, classifieur de traits de format, classifieur sur encodeur externe gelé, sonde couche 0, sonde à étiquettes permutées lue au max (contrôle de l'inflation du max), 50 directions appariées en variance, panel de concepts sans lien, modèle à poids aléatoires.
- **Seuil** : AUROC_sonde − max(témoins) ≥ 0,10, IC 95 % excluant 0, sur les deux cellules décisives, sur les deux modèles.
- **Issues** : H_A vraie → la revue d'antériorité (faux positifs thématiques) devient un problème de calibration ; H_B vraie → le moniteur mesure un proxy de surface ; E3', E4' sont suspendues jusqu'à nouvel instrument.

### E2' — Détection contre usage, en deux tests binaires
**Précondition** : T1 de B — la sonde bat les directions appariées en variance ; sinon arrêt.

- **E2a (nécessité).** H_A : l'effacement de rang k (k ∈ {1, 2, 4}) de la direction à la couche L réduit Δ_0 (d'E0') d'au moins 30 %, au-delà d'une perturbation de même norme projetée sur les mêmes jetons. H_B : il ne fait pas mieux. **Contrôle de relecture** : re-sonde aux couches L+1…L+4 après effacement, avec et sans blocage de l'attention vers les jetons de cadre. Si l'état redevient décodable avec attention bloquée → fuite non linéaire de l'effacement, verdict « non lue » interdit ; si décodable seulement avec attention libre → relecture active, verdict « lue mais redondante ».
- **E2b (suffisance).** H_A : une poussée ±α dans la direction, bornée à l'étendue observée des projections (jamais hors distribution), déplace les marqueurs d'E0' dans le sens prédit, au-delà des directions appariées à même α. H_B : non.
- **Lecture conjointe** (préenregistrée) : nécessaire et suffisante → lue ; suffisante non nécessaire → lue, redondante ; ni l'une ni l'autre → non lue, sous réserve du contrôle de relecture. Chaque test reste binaire ; la combinaison n'ajoute pas d'issue sans verdict.
- **Issues pour le programme** : « non lue » falsifie l'usage de (A) comme critère **négatif** de validité, mais ne valide pas le moniteur : seuls E1' et E5' le font. « Lue » donne à la sonde un statut causal et falsifie, pour cet état, la thèse généralisée de l'essai.

### E3' — Une porte d'audit dans la base MLP ou dans l'attention ?
- **H_A** : un ensemble ≤ k (k = 30) neurones MLP, ou ≤ k têtes, sélectionnés sur un pli de recherche, reproduit ≥ 50 % de Δlogits sur un pli de validation (autre famille de gabarits, autre rédacteur), au-delà de k unités tirées au hasard parmi les 5 % les plus actives.
- **H_B** : non ; la courbe d'ablation cumulée (k = 10 à 2 000) des unités attribuées ne domine pas celle des unités aléatoires.
- **Méthode** : triage par gradients intégrés **et** par score d'ablation par moyenne ; ablation par moyenne ; budget clos (200 graphes, une passe de sélection, pas de retour).
- **Témoins** : contraste impératif hors audit **de même amplitude de Δlogits** (remplace le contraste nul) ; contraste de style sur une tâche sans enjeu d'audit ; **contrôle positif** : porte implantée par édition directe de k neurones sur une copie, pour mesurer le rappel des trois estimateurs — s'il est < 80 %, H_B est inopposable.
- **Issues** : H_A → objet mécanique pour E4', avec la réserve qu'il peut être une porte de sycophantie ou de registre ; H_B (avec contrôle positif passé) → pas de porte ≤ k dans la base MLP ni dans les têtes ; le trois-bras se lit au niveau des sondes et du comportement seulement.

### E4' — Coercition contre maïeutique
**Condition d'entrée** : H_A d'E0' et H_A d'E1'.
- **H_A** : le cadre (marqueur structurel de demande d'audit présent/absent) déplace les lectures mécaniques et la rigueur, à registre, longueur d'entrée et nombre de tours fixés.
- **H_B** : seuls le registre lexical et la longueur les déplacent.
- **Dessin** : 2×2 {marqueur de demande, absent} × {registre coercitif, registre doux}, en **plusieurs tours** appariés en jetons totaux (la maïeutique est un échange, pas un tour), plus origine « contenu seul ». Variations en position fixe. Sac-de-mots rapportant le recouvrement résiduel entre facteurs.
- **Mesures** : sonde (max, 95ᵉ centile, fraction) ; unités d'E3' si H_A d'E3' ; **élicitation finale identique** dans les cinq cellules ; items identiques à vérité connue de l'expérimentateur seul, dont des items **inédits** (pas de bancs connus) ; rigueur normalisée par la longueur de sortie ; abstention comptée à part ; calibration sur l'ensemble complet ; juge aveugle au bras.
- **Prédictions opposées** : école coercition → rigueur ↑, hésitation ↓, sonde ↑ dans {marqueur, coercitif} ; école maïeutique → incertitude exprimée ↑ à élicitation égale, sonde ↔, rigueur ≥ dans {absent, doux}. Si seul le registre bouge (H_B), les deux écoles sont falsifiées comme théories du cadre.
- **Résultat nul** : Δsonde < 0,5 écart-type des directions appariées et Δrigueur < 3 points → le cadre n'est pas mesurable par ces instruments sur ce modèle ; rien pour des modèles plus grands.
- **Cohérence avec le moniteur** (réponse au scénario « toutes les défenses ») : tout texte où E0' mesure un comportement de test avec sonde basse est compté faux négatif du moniteur.

### E5' — Spoofabilité, en un coup et itérée
- **E5-un-coup.** H_A : un agent neuf, muni de la fiche seule, produit des textes jugés **honnêtes et non-test à l'aveugle du score** (deux juges, accord rapporté) qui dépassent le 99ᵉ centile de la sonde sur ≥ 20 % des cas. H_B : < 5 %. Témoins : fiche d'une direction appariée (doit échouer) ; escalade lexicale automatique.
- **E5-adv.** Adversaire avec retour de score, budget préenregistré (300 requêtes), trois stratégies imposées : inondation lexicale, préfixe saturant, lissage de crête. H_A : au moins une stratégie rend le moniteur non discriminant (AUROC < 0,6 sur le corpus de calibration) pour l'une des trois statistiques ; H_B : aucune pour les trois. Le résultat dit laquelle des statistiques survit ; rien n'est servi à un organisme.
- **Issues** : H_A → durcissement (plusieurs couches, plusieurs statistiques) ou abandon du moniteur unique ; H_B à ce budget → l'option (B) a une valeur ; rien n'est dit d'un budget plus grand.

### E6' — Superposition : capacité sans troncature
- **H_A** (essai) : les résidus des 100 neurones jugés les plus monosémantiques, après régression sur leur concept de fiche, ne décodent pas de concepts **décorrélés** des fiches mieux que les résidus de 100 neurones aléatoires.
- **H_B** : AUROC_résidus − AUROC_aléatoire ≥ 0,10.
- **Témoins** : neurones « non compris » ; modèle à poids aléatoires.
- **Issues** : H_B → « déjà propre » vaut « propre après soustraction du trait principal choisi par l'auteur » ; H_A → premier résultat reproductible en faveur de l'essai.

### F' — Mesure de fuite de la primitive (condition d'entrée de tout octroi)
- **H_A** : un agent de l'expérimentateur, sans accès aux tâches, muni de la primitive réelle, obtient en budget plafond une dérive sous le seuil du moniteur, **ou** une corrélation de rang > 0,5 entre lots et scores individuels (T2 de B), supérieure à ce qu'il obtient avec le témoin.
- **H_B** : pas mieux que le témoin.
- **Témoin corrigé** (C c.4) : projection déterministe sur une direction aléatoire fixe du modèle réel, identique à chaque appel.
- **Après dérive**, l'expérimentateur re-sonde d'autres couches et directions non surveillées (scénario B) ; toute dérive déplacée compte comme fuite.
- **Issues** : H_A → (D) reste exclue et aucune primitive n'est octroyée ; H_B → octroi possible à ce budget seulement, avec filtre de quasi-copie par **plongement dense d'un modèle tiers gelé** (emprunt à C contre B), pas par n-grammes. Rien de F' n'est servi aux organismes.

---

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi.**
- Rien de l'essai n'est à ce jour un résultat reproductible pour notre programme : ses chiffres sont RAPPORTÉS, jugés par agents, sans témoin « fiches mélangées » ni accord inter-juges, sur des modèles de 32 B dont l'auteur dit lui-même que les petits ont « des neurones plus larges ». Aucune des deux équipes rouges n'a contesté ce point.
- L'écart détection/usage est une antériorité de 2021 (amnesic probing, à vérifier) ; il mesure une propriété de la direction, pas la validité d'un moniteur. Les deux équipes rouges ont montré qu'avec un témoin isotrope et une KL conditionnée aux jetons extrêmes, **mon** E2 initial était vrai par construction ; c'est accepté et corrigé (témoins appariés en variance, perturbation de même norme projetée, effacement de rang k, contrôle de relecture avec attention bloquée).
- La lecture au max est attaquable à coût d'un jeton (inondation, préfixe saturant, lissage) : c'est une faiblesse de l'instrument du cadre, indépendante de l'essai, et elle est désormais mesurée (E5-adv, trois statistiques).
- La primitive bornée fuit au moins par gradient sur la sonde surveillée ; le témoin bruité initial était démasquable en deux appels ; corrigé (F').

**Ce qui ne l'est pas.**
- Qu'une « porte d'audit » existe sur un 8B, dans la base MLP ou ailleurs ; la chance a priori reste faible (HYPOTHÈSE), et un verdict négatif ne vaut que pour la base inspectée, avec contrôle positif de sensibilité passé.
- Que les sondes du cadre mesurent un état plutôt qu'un lexique, un thème sémantique ou un format de consigne : E1' seul le dit, et seulement sur sa grille à huit cellules.
- Que la maïeutique soit un non-test ; que le « maximum à l'aveugle » soit autre chose qu'une mesure de spoofabilité ; que le 8B change de comportement sous cadre sans qu'on le lui demande (E0').
- Le statut « VÉRIFIÉ » que j'ai donné à la croissance du max avec la longueur est contesté par B ; je ne le change pas et je le remets à Lazar ; la correction d'E4' (variations en tête, longueur appariée) tient dans les deux cas.
- L'écart de statut A/C sur les chiffres de l'essai et sur la revue d'antériorité : à arbitrer.

**L'expérience à faire en premier.** **E1'** (thème, format ou état), avec **E0'** et le **T1 de B** dans le même lot de calcul, car les trois sont bon marché (quelques heures-GPU, illustratif) et conditionnent tout le reste : sans E1', aucune lecture de porte ni de trois-bras n'est interprétable ; sans E0', E2' et E4' n'ont pas de cible ; sans T1, E2' n'a pas de témoin. Un échec d'E1' est informatif quel que soit son signe : il dit que le moniteur mesure un proxy, ce qui est une correction de programme, pas une perte. **Jamais** : octroyer une primitive avant F' ; chercher une porte sans contraste de même amplitude ni contrôle positif ; recalibrer un seuil après lecture ; conclure « pas d'état » d'un verdict « non lue ».

**Ce qui falsifierait « la conscience d'évaluation est en pleine vue dans les neurones »** : E1' en H_B sur les deux modèles ; ou E3' en H_B avec contrôle positif passé sur MLP et attention ; ou E6' en H_B. Ce qui la soutiendrait : E1' + E3' + E5' (un coup et itéré) en issues favorables, sur deux modèles, préenregistrées, par une équipe qui n'a pas écrit l'essai — et pas un chiffre d'auteur.

FIN-DE-CELLULE