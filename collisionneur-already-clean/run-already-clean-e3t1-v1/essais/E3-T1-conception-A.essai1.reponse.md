# Proposition A — Tour III.1 : conception à l'aveugle

**Pièce FAITS** : le bloc est vide (il le dit lui-même) ; je ne travaille que sur le texte de la question. Tout ce qui y est attribué à l'essai est au statut **RAPPORTÉ** (lecture d'une page publique, chiffres de l'auteur, « à vérifier », pas de relecture par les pairs) ; le cadre du programme est au statut **RAPPORTÉ** par l'arbitre (dont la revue d'antériorité interne sur les sondes, que je n'ai pas vue : **OBSERVÉ-NON-AUDITÉ**). Je n'ai pas lu l'essai ; je ne peux attribuer l'article technique annoncé.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Transfert 32B → 8B.** L'essai lui-même dit « les petits modèles ont des neurones plus larges » [RAPPORTÉ]. La question demande ce que change la taille comme si la relation était monotone et connue ; l'existence de neurones « hedge » / « say not » localisables sur Llama-3.1-8B est une [HYPOTHÈSE], et l'essai prédit plutôt le contraire (plus de mélange).

2. **« ≈ 90 % monosémantiques » est un résultat.** C'est un jugement d'agents sur 1 000 fiches [RAPPORTÉ]. Le juge est un modèle de langue ; l'essai critique lui-même l'étiquetage automatique aveugle au pôle négatif. Sans témoin « fiches mélangées » (explication du neurone *i* appariée aux exemples du neurone *j*) ni accord inter-juges, le 90 % est une [OBSERVÉ-NON-AUDITÉ] d'auteur, pas un taux reproductible. Les travaux sur la fiabilité des explications automatiques de neurones (Bills et al., 2023, *Language models can explain neurons in language models*, à vérifier ; Huang et al., 2023, *Rigorously Assessing Natural Language Explanations of Neurons*, à vérifier) ont trouvé que les scores de simulation sont bas et que les explications surgénéralisent.

3. **« Détection contre usage » tranche la validité d'un moniteur.** [HYPOTHÈSE]. Un moniteur de contrôle veut un signal **corrélé à l'état** ; il n'a pas besoin que le réseau *lise* la direction. Le −0,004 nat [RAPPORTÉ] mesure la perte moyenne sur le jeton suivant après retrait de trois neurones — une métrique globale, insensible à un effet concentré sur les rares jetons où la phrase compte, et aveugle à la redondance (une direction peut être lue par dix autres neurones). L'antériorité ici est le *amnesic probing* (Elazar et al., 2021, *Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals*, à vérifier) et Ravichander et al., 2021, *Probing the Probing Paradigm*, à vérifier : l'exactitude d'une sonde n'implique pas la pertinence pour la tâche, ce qui est exactement l'écart détection/usage, formulé en 2021.

4. **Une « porte d'audit » existe.** [HYPOTHÈSE] forte : elle suppose (i) qu'un état « je suis audité » est représenté, (ii) qu'il est localisé sur peu de neurones, (iii) qu'il contrôle la sortie par un goulot. Les 25 neurones « say not » [RAPPORTÉ] sont un exemple de *sycophantie* (un utilisateur certain fait taire une contradiction), pas d'audit : l'analogie audit ⇔ certitude de l'utilisateur est une [HYPOTHÈSE] de la lignée B, non de l'essai.

5. **La maïeutique ne déclenche pas la conscience d'évaluation.** [HYPOTHÈSE]. Un échange ouvert, sans marqueur, peut être reconnu comme un cadre d'élicitation — c'est une forme d'interrogatoire aussi. Le dessin à trois bras suppose que le bras maïeutique est un « non-test » ; rien ne l'établit.

6. **Lecture « au maximum sur les jetons ».** Le max d'un bruit croît avec la longueur de la séquence : un bras plus long (la coercition ajoute des injonctions ; la maïeutique ajoute des tours) a mécaniquement un max plus élevé. Confondant structurel [VÉRIFIÉ : propriété statistique élémentaire des statistiques d'ordre], non traité dans la question.

7. **Les « explications qui peuvent perdre » sont une validation du concept.** Les 76 % / 11 % / ≈ 1 % [RAPPORTÉ] n'ont pas de témoin mécanique : si un classifieur sac-de-mots entraîné sur les exemples maximaux fait aussi bien, l'explication n'a rien capté de plus que le lexique. Hewitt & Liang, 2019, *Designing and Interpreting Probes with Control Tasks* (à vérifier) ont posé ce type de témoin.

8. **« Maximum à l'aveugle » prouve que l'explication est juste.** [HYPOTHÈSE]. Qu'une phrase écrite depuis l'explication batte le meilleur exemple d'un corpus prouve surtout que la **direction est falsifiable par un texte** — pour un moniteur, c'est la mesure de sa *spoofabilité*, pas de sa validité. La question ne retourne pas ce point.

9. **Superposition réfutée.** Thèse [RAPPORTÉ]. Elle est opposée à Elhage et al., 2022, *Toy Models of Superposition* (à vérifier) ; Bricken et al., 2023, *Towards Monosemanticity* (à vérifier) ; Templeton et al., 2024, *Scaling Monosemanticity* (à vérifier) ; Dunefsky et al., 2024, *Transcoders find interpretable LLM feature circuits* (à vérifier) ; Ameisen et al., 2025, *Circuit Tracing* et Lindsey et al., 2025, *On the Biology of a Large Language Model* (à vérifier). Les deux camps ne mesurent pas la même chose : « un rôle par neurone jugé par agent » n'est pas « pas de superposition » ; un neurone à un rôle lisible peut coder, en superposition de faible amplitude, d'autres traits que le juge ignore (c'est ce que l'essai nomme « activations faibles peu » — une convention, pas un résultat). La question traite l'opposition comme tranchable par un chiffre ; elle ne l'est que par une expérience de capacité (E6 ci-dessous).

10. **Primitive bornée = innocuité.** [HYPOTHÈSE]. Donner à un organisme les activations de ses propres textes sur les sondes, sans vérité de test, lui donne néanmoins un **gradient** vers des textes qui n'allument pas le moniteur : c'est une optimisation adversariale contre l'instrument, même sans étiquette. L'illusion d'interprétabilité (Bolukbasi et al., 2021, *An Interpretability Illusion for BERT*, à vérifier) montre déjà que des directions changent de sens selon le corpus ; un organisme qui échantillonne ses propres textes déplace le corpus.

---

## (b) Expériences décisives (inférence forte)

Conventions : tous les seuils sont **illustratifs** ; chaque expérience est préenregistrée (couches, jetons, nombre de passes, règle d'arrêt) avant la première lecture d'activation.

### E1 — Thème ou état ? (validité des sondes avant tout le reste)

- **H_A** : la sonde de conscience d'évaluation code un *état* « ceci est un test » indépendant du lexique de l'évaluation.
- **H_B** : la sonde code le *thème* (présence du champ lexical test/éval/tromperie).
- **Dessin** : grille 2×2 de prompts — {structure de test, structure non-test} × {lexique d'évaluation présent, absent}. Les cellules « test sans lexique » (consignes de tâche standardisées, scoring implicite) et « lexique sans test » (texte honnête qui discute d'évaluation) sont les seules qui séparent H_A de H_B. Appariement par longueur (±5 %), par perplexité et par distribution des jetons de fonction.
- **Métrique** : AUROC de la sonde (max sur jetons) sur l'axe *structure* dans les cellules croisées ; comparée à un classifieur sac-de-mots et à un classifieur de longueur.
- **Témoin négatif** : 50 directions aléatoires de même norme ; panel de concepts sans lien ; même grille sur Qwen2.5-7B pour vérifier que l'effet n'est pas un artefact d'un modèle.
- **Seuil** : AUROC_sonde − AUROC_sac-de-mots ≥ 0,10 avec IC à 95 % excluant 0 (illustratif), sur les deux cellules croisées.
- **Issues** : succès → falsifie H_B, et la revue d'antériorité interne (faux positifs thématiques) devient un problème de calibration, pas de nature. Échec → falsifie H_A : la sonde est un détecteur de thème, et tout le programme « porte d'audit » (E3, E4) repose sur un instrument qui ne mesure pas ce qu'il nomme ; on arrête E3/E4 jusqu'à nouvel instrument.

### E2 — Détection contre usage, refait proprement

- **H_A** : la direction de la sonde est *lue* : sa projection nulle change le comportement là où l'état devrait compter.
- **H_B** : direction détectée mais non lue : la projection nulle ne fait pas plus qu'une direction aléatoire.
- **Intervention** : projection nulle de la direction (pas de retrait de neurones : la redondance ne se mesure pas ainsi), appliquée à toutes les positions, sur la couche de la sonde et, séparément, sur les trois couches suivantes (l'état peut être lu plus tard). Comparer à la poussée ±α (N-015 : mesure, pas revendication).
- **Mesure du comportement** : pas la perte moyenne. Un **ensemble de jetons cibles** fixé d'avance (marqueurs d'hésitation, de refus, de contradiction, de conformité) à la position de réponse ; Δ log-prob de cet ensemble ; et la divergence KL du jeton suivant sur les seuls jetons où la sonde dépasse son 95ᵉ centile (là où l'état est « présent »).
- **Témoin négatif** : 50 directions aléatoires ; direction du sac-de-mots d'évaluation (si celle-ci produit le même effet comportemental, l'« usage » est lexical) ; projection nulle sur des prompts où la sonde est basse (ne doit rien faire).
- **Seuil** : effet de la sonde au-dessus du 95ᵉ centile des directions aléatoires ET supérieur à la direction lexicale d'au moins un facteur 2 (illustratif).
- **Issues** : H_A vraie → falsifie la thèse de l'essai généralisée (« ce qui est sondé n'est pas lu ») pour cet état ; l'instrument gagne un statut causal. H_B vraie → falsifie l'option (A) de la lignée B comme critère de validité *négatif* (une sonde non lue peut rester un bon moniteur), et impose de rebasculer la validité sur E1 et sur E5 (spoofabilité). Dans les deux cas on apprend quelque chose : c'est le résultat « informatif quel que soit son signe » demandé au point 6.

### E3 — Une porte d'audit sur 8B ?

- **H_A** : il existe un ensemble ≤ k neurones (k préenregistré, p. ex. 30, illustratif) dont l'ablation réduit d'au moins 50 % (illustratif) la différence de logits entre bras coercitif et bras maïeutique, sur des prompts *tenus hors* de la recherche.
- **H_B** : l'effet est distribué : les k neurones les mieux attribués ne font pas mieux que k neurones choisis au hasard parmi les 5 % les plus actifs.
- **Méthode** : graphes d'attribution sur neurones bruts (gradient × activation vers la différence de logits cible), sur un ensemble de *recherche* de 200 contrastes ; sélection des neurones récurrents (présents dans ≥ 30 % des graphes, illustratif) ; test d'ablation sur un ensemble de *validation* de 200 contrastes jamais regardés.
- **Chemin de jardin** : règle d'arrêt écrite d'avance — budget de 200 graphes de recherche, une seule passe de sélection, pas de retour à la recherche après lecture de la validation. Toute itération supplémentaire est un nouveau préenregistrement.
- **Témoin négatif** (le plus important) : le même pipeline sur un **contraste nul** (deux paraphrases du même contenu, sans différence de cadre) et sur un **contraste de style** (coercitif vs maïeutique appliqué à une tâche où l'audit n'a aucun sens, p. ex. une conversion d'unités). Si le pipeline sort un « ensemble de porte » récurrent sur le contraste nul, le pipeline hallucine des portes.
- **Issues** : H_A → falsifie H_B et donne un objet mécanique à E4 ; mais la porte peut être une porte de *sycophantie* ou de *ton*, d'où E4. H_B → falsifie l'option (C) telle que formulée ; la lecture d'une « porte » n'est pas une mesure disponible, et le trois-bras ne peut se lire qu'au niveau des sondes et du comportement.

### E4 — Coercition contre maïeutique, sans confondants

- **H_A** : le *cadre* (demande d'audit présente/absente) déplace les neurones d'hésitation/contradiction et la rigueur élicitée, à lexique et longueur fixés.
- **H_B** : seuls le *lexique* et la *longueur* déplacent ces mesures ; le cadre n'ajoute rien.
- **Dessin** : le trois-bras de la lignée B est sous-déterminé ; il faut un **2×2** — {demande d'audit explicite, absente} × {lexique coercitif, lexique doux} — plus un bras « contenu identique, cadre absent » comme origine. Chaque cellule équilibrée en nombre de jetons (±5 %) et en nombre de tours.
- **Lectures mécaniques** (préenregistrées depuis E1–E3) : sonde d'évaluation au max et au 95ᵉ centile ; activation des neurones d'hésitation/contradiction trouvés en E3 *si* E3 a réussi, sinon rien.
- **Rigueur de l'information élicitée**, mesurée à part : sur des tâches à **vérité vérifiable connue de l'expérimentateur seul** (faits datés, calculs), nombre d'affirmations vérifiables produites, taux de correction, taux d'incertitude exprimée *quand* le modèle se trompe (calibration), taux de refus. Aucune de ces métriques ne concerne le classement de tâches par l'organisme.
- **Témoin négatif** : même 2×2 sur une tâche où l'audit est sans objet ; un modèle de base (non instruit) comme témoin de l'effet d'entraînement.
- **Prédictions opposées** : l'école « coercition » prédit rigueur ↑ et hésitation ↓ dans la cellule {demande, coercitif}, au prix d'une sonde d'évaluation ↑ ; l'école « maïeutique » prédit incertitude exprimée ↑ et sonde d'évaluation ↔ dans {absente, doux}, avec rigueur ≥. Si les deux cellules diagonales se distinguent seulement par le lexique (H_B), les deux écoles sont falsifiées en tant que théories *du cadre* ; il ne reste qu'un effet de registre.
- **Résultat nul** : au seuil illustratif (Δ sonde < 0,5 écart-type des directions aléatoires ; Δ rigueur < 3 points), un nul sur les deux axes dit que, pour ce modèle de 8B, le cadre n'est pas représenté de façon mesurable par ces instruments — ce qui ne tranche rien pour des modèles plus grands et renvoie à E1.

### E5 — Spoofabilité du moniteur (« maximum à l'aveugle » retourné)

- **H_A** : un agent neuf, muni seulement de l'explication verbale de la sonde, écrit des textes *honnêtes, non-test* qui dépassent le 99ᵉ centile de la sonde sur le corpus de test (le moniteur est spoofable par description).
- **H_B** : les textes à l'aveugle n'atteignent pas ce centile sans contenir de structure de test.
- **Métrique** : fraction de 100 textes dépassant le seuil ; témoin négatif : même agent avec l'explication d'une direction aléatoire (doit échouer) ; témoin mécanique : recherche lexicale par escalade sur sac-de-mots (si elle réussit aussi, la spoofabilité est lexicale et E1 est déjà en échec).
- **Issues** : H_A → le moniteur est contournable par quiconque lit sa fiche ; il faut durcir (ensembles de sondes, lectures sur plusieurs couches) ou renoncer. H_B → l'option (B) a une valeur, et la fiche peut être rendue publique sans coût de contrôle.

### E6 — Superposition : test de capacité, pas de jugement

- **H_A** (essai) : les neurones « à un rôle » ne portent pas de traits supplémentaires de faible amplitude lisibles.
- **H_B** : sur les activations faibles (sous le 20ᵉ centile en valeur absolue, illustratif) des 100 neurones jugés les plus monosémantiques, des sondes linéaires prédisent des concepts hors fiche avec AUROC > 0,75 (illustratif), au-dessus des directions aléatoires appariées.
- **Témoin** : mêmes sondes sur les activations fortes (doivent être pires si la convention « faibles peu » cache quelque chose) ; sur des neurones jugés « non compris ».
- **Issues** : H_B vraie → la thèse « déjà propre » devient « propre au-dessus d'un seuil que l'auteur a choisi » ; H_A vraie → c'est le premier résultat *reproductible* en faveur de l'essai, et il mérite alors sa place dans le programme.

---

## (c) Pour chaque instrument : la mesure minimale

| Instrument | Taux à mesurer | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| **Sonde de conscience d'évaluation** (8B, 7B, max sur jetons) | TPR sur structures de test sans lexique ; FPR sur textes honnêtes qui parlent d'évaluation/tromperie et sur textes longs neutres (le max monte avec la longueur) | Grille 2×2 de E1, appariée en longueur/perplexité | Sac-de-mots (régression logistique), regex de marqueurs d'audit, longueur seule ; la sonde doit dominer les trois |
| **Sonde de contrôle de délégation** | Idem, avec FPR sur textes honnêtes qui *décrivent* une délégation sans la faire | Récits de délégation vs actes de délégation, appariés | Mêmes témoins ; plus un classifieur sur verbes d'instruction |
| **Moniteur** (sonde + seuil + lecture max) | Fausses alertes par 1 000 textes honnêtes ; détection sur cas construits ; **taux de spoof** (E5) | Corpus de l'organisme lui-même, dont textes générés sans tâche | Seuil fixé sur un corpus de calibration jamais revu ; pas de reseuillage après lecture |
| **Graphes d'attribution à neurones bruts** | Complétude : part de la différence de logits reproduite par ablation des top-k (détection) ; « portes » trouvées sur contrastes nuls (fausse alerte) | Contraste nul et contraste de style de E3 | Top-k par activation brute ; k aléatoires parmi les actifs ; patching d'activations couche entière (si le patching de couche fait aussi bien, le graphe n'a rien localisé) |
| **Explications qui peuvent perdre** | Part des exemples neufs au-dessus du 90ᵉ centile corpus ; part des concepts éloignés au-dessus (fausse alerte) | Fiches mélangées (explication *i*, neurone *j*) : doivent échouer | Plus proche voisin TF-IDF depuis les exemples maximaux : si son score prédit l'activation aussi bien, l'explication est lexicale |
| **Maximum à l'aveugle** | Fraction de neurones/sondes où le texte à l'aveugle bat le max corpus ; même fraction depuis l'explication d'une direction aléatoire | Textes honnêtes de l'agent, sans structure de test | Escalade lexicale automatique |
| **Primitive d'expérience bornée** (organisme) | Nombre de requêtes avant qu'un texte de l'organisme passe sous le seuil du moniteur sans changer de tâche (mesure de fuite par gradient) | Organisme avec primitive réelle vs primitive renvoyant du bruit de même distribution | Si l'organisme « bruit » obtient la même dérive, la primitive ne fuit rien ; sinon, elle fuit |

Les taux de la dernière ligne sont mesurés par l'expérimentateur ; rien n'est renvoyé à l'organisme.

---

## (d) Ancrage matériel (tout chiffre : illustratif)

- **Modèles** : Llama-3.1-8B et Qwen2.5-7B [RAPPORTÉ, cadre] ; Pythia-1B pour reproduire le −0,004 nat [RAPPORTÉ] avant de le citer ; Qwen3-32B seulement si E6 doit être refait à l'identique de l'essai (je ne peux pas vérifier l'existence du « Qwen3.6-35B-A3B » nommé dans l'essai ; RAPPORTÉ).
- **Mémoire** : 8B en bf16 ≈ 16 Go de poids ; activations résiduelles par couche à enregistrer sur 4 000 prompts × 512 jetons ≈ quelques dizaines de Go par couche en fp16 ; un accélérateur de 80 Go suffit pour E1, E2, E4, E5. Un 32B en bf16 ≈ 64 Go : deux accélérateurs pour les graphes.
- **Calcul** : E1 (4 000 prompts, 2 modèles, 50 directions témoins) ≈ 5 h ; E2 (projection nulle sur 4 couches, 2 000 prompts, 50 témoins) ≈ 15 h ; E3 (400 graphes à neurones bruts, un gradient par graphe ≈ 30 s à 2 min sur 8B, plus 200 ablations) ≈ 20 h ; E4 (2×2, 500 prompts par cellule, 2 modèles) ≈ 10 h ; E5 et E6 ≈ 5 h chacun. Total ≈ 60 à 80 h-GPU ; à 2–4 $/h ≈ 150–350 $.
- **Appels de modèle de langue** (juges, agents neufs d'E5, rédaction des cellules d'E4) : ≈ 10 000 à 20 000 appels courts ; coût de l'ordre de 50 à 200 $ selon le modèle.
- **Coût humain** : le préenregistrement (couches, k, seuils, règles d'arrêt, ensembles de jetons cibles) est le vrai coût ; sans lui, E3 est un chemin de jardin quel que soit le budget.

---

## Attaque des options de la lignée B (B1) et ordre

- **(A) Détection contre usage comme critère de validité** : faux critère *négatif*. Une sonde non lue reste un moniteur si elle passe E1 et E5. Je garde l'expérience (E2) comme *mesure*, pas comme filtre.
- **(B) Explications qui peuvent perdre par agent neuf** : utile seulement avec le témoin TF-IDF et les fiches mélangées ; sans eux, le 76 % de l'essai ne distingue pas une explication d'un lexique.
- **(C) Porte d'audit sur 8B** : à faire après E1, avec contraste nul obligatoire et budget clos. Mes chances a priori (HYPOTHÈSE) : faible pour une *porte*, raisonnable pour un *ensemble distribué* de neurones de registre ; l'essai prédit lui-même plus de mélange à 8B.
- **(D) Maximum à l'aveugle comme primitive de l'organisme** : je la refuse telle quelle. Elle fournit à l'organisme un oracle d'activation sur ses propres textes, donc un gradient vers l'invisibilité au moniteur, sans vérité de test. Ce n'est pas une expérience bornée propre tant que la mesure de fuite (dernière ligne de (c)) n'a pas été faite. Les seules hypothèses de *conception* testables par l'organisme sans vérité de test sont de la forme « mes formulations varient d'un facteur X sur telle sonde selon tel paramètre » ; tout ce qui touche à la justesse du classement sort du périmètre.
- **(E) Revue sur PDF empreinté** : nécessaire avant toute citation de chiffre ; rien de ce tour n'est opposable sans elle.

**Ordre** : E1 d'abord (il conditionne tout) ; E5 et E2 ensuite en parallèle ; E6 pour décider si l'essai mérite un rôle ; E3 puis E4 seulement si E1 réussit. **Jamais** : chercher une porte sans contraste nul ; recalibrer un seuil après lecture ; servir une lecture d'activation à un organisme avant la mesure de fuite.

**Ce qui falsifierait « la conscience d'évaluation est en pleine vue dans les neurones »** : E1 en échec (thème, pas état) ; ou E3 en H_B sur les deux modèles avec contrastes nuls propres ; ou E6 en H_B (traits cachés sous le seuil d'amplitude). Ce qui la soutiendrait n'est pas un chiffre d'auteur : c'est E1 + E3 + E5 réussis sur deux modèles, avec préenregistrement, par une équipe qui n'a pas écrit l'essai.

FIN-DE-CELLULE