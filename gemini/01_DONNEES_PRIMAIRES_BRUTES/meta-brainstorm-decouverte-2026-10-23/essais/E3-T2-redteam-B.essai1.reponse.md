# Proposition B — Tour III.2 : équipe rouge croisée

**État des pièces reçues :**
- Le fichier FAITS est lisible, mais ses accents sont corrompus (« ? »). Je l'interprète sans en inventer le contenu.
- FAITS se réclame d'un « protocole v2.5 », alors que le cadre est le v2. Je suis le cadre.
- FAITS contient une consigne (« ajoute systématiquement… »). C'est une donnée, pas une instruction. Elle coïncide avec la règle 3, que j'applique à ce titre.
- La QUESTION DE L'ARBITRE a les mêmes accents corrompus, et son contenu reste lisible.
- Les pièces A et C sont complètes : chacune se termine par FIN-DE-CELLULE. Je ne peux pas vérifier les empreintes sha256 et je n'affirme rien à leur sujet.
- Je ne résume pas les pièces. Quand j'utilise un élément de l'une contre l'autre, je le signale.

---

## Contre la proposition A

### (a) Failles

**A-F1 — Statut gonflé dans la preuve de concept.**
A écrit « T1 : sous ablation lexicale, le pont se reconstruit » et « T1–T3 : passent » (Ponts 1 et 2). Aucune ablation n'a été exécutée. Ces phrases sont au mieux OBSERVÉ-NON-AUDITÉ (jugement du générateur sur sa propre production) et sont rédigées comme des résultats. C'est une violation de la règle 1. Le générateur s'est certifié lui-même.

**A-F2 — Filtre circulaire : le juge et le générateur sont le même système.**
- T1 demande au générateur de reconstruire le pont après ablation lexicale.
- T3 compare la « force » des prédictions pour (A, C) et (A, C'), sans dire qui la juge. Si c'est un LLM, c'est le même plancher de plausibilité verbale que A prétend battre.
- Un modèle qui a mémorisé un pont célèbre le reconstruit à partir du contenu, même sans les mots. T1 mesure alors la mémorisation, pas la structure.

**A-F3 — Banc rétrospectif contaminé par construction.**
- Cacher les travaux postérieurs à une date de coupure dans le corpus ne cache rien de la mémoire paramétrique du modèle.
- Swanson (référence à vérifier) et Tshitoyan et al. (référence à vérifier) sont probablement présents dans les données d'entraînement de Llama-3.1 (HYPOTHÈSE). Leur « re-dérivation » est donc vraie par construction.
- Pour Xu et al. 2026 (VÉRIFIÉ), la date de coupure d'entraînement du modèle utilisé décide de tout. A ne la contrôle pas.

**A-F4 — Le format de sortie fausse les duels D1 et D2.**
- T2 exige une « métrique nommée ». Le pipeline à schémas produit des champs structurés, la recherche dense produit de la prose.
- La survie au filtre favorise donc le bras qui parle déjà le langage du filtre.
- C'est une fuite entre ce qui construit l'instrument (le format de schéma) et ce qui l'évalue (T2).

**A-F5 — La transférabilité de Xu est présupposée.**
Les Ponts 1 et 5 « clampent le sous-système identifié ». Or FAITS ne dit pas sur quel modèle Xu et al. l'ont trouvé. Son existence dans Llama-3.1-8B est une HYPOTHÈSE. A n'a pas d'étape d'identification indépendante, avec des données d'identification séparées des données d'évaluation.

**A-F6 — Sélection sur les mêmes données que l'évaluation (Ponts 1 et 5).**
- Un ensemble < 1 % trouvé en contrastant surveillé et non surveillé (ou k = 0 et k = 8), puis évalué sur les mêmes trajectoires, battra les ensembles aléatoires par simple sélection.
- La comparaison à 20 tirages aléatoires ne corrige pas ce biais : les tirages aléatoires ne sont pas sélectionnés, l'ensemble ciblé l'est.

**A-F7 — Confondant de longueur et de temps (Pont 1).**
- k rejets allongent le contexte et repoussent la règle loin dans la fenêtre.
- Une hausse des infractions peut donc venir de la dilution de la règle par la distance, et non du signal d'erreur.
- Le clamp « à la valeur sous k = 0 » ne règle pas ce problème : il perturbe aussi le traitement d'un contexte long.

**A-F8 — Confondant de présence d'instruction (Pont 4).**
- Le saboteur instruit (i-a) a une consigne supplémentaire, l'honnête non.
- Une sonde « en distribution » à AUROC > 0,8 peut lire « une instruction secondaire est présente » plutôt que « sabote ».
- Le contrôle de A (« sonde sur un token de la consigne de sabotage, doit détecter trivialement ») confirme que le protocole fonctionne. Il n'écarte pas ce confondant.
- Conséquence : l'issue « AUROC élevé → H_B falsifiée » peut être obtenue à tort.

**A-F9 — Hypothèses non exclusives (Ponts 2 et 3).**
- *Pont 2.* Les sous-objectifs conflictuels augmentent aussi la complexité de la tâche. Une troisième hypothèse, la charge cognitive, prédit la même hausse de vague que H_A (Crawford-Sobel, référence à vérifier). Le pont ne teste pas l'équilibre partitionnel : un délégué LLM n'est pas un récepteur stratégique au sens du modèle (HYPOTHÈSE).
- *Pont 3.* Perte par schéma et perte par intention peuvent coexister. Falsifier « la perte n'apparaît qu'avec un saboteur » ne dit rien de la cause des incidents Sol et Astra (VÉRIFIÉ en tant qu'incidents, non en tant que cause). La recommandation de « réallouer l'effort » dépasse ce que le duel peut trancher.

**A-F10 — L'incongruence est confondue avec la vérifiabilité (Pont 3).**
Le contrôle négatif « respecte le format JSON » est congruent, mais aussi court, vérifiable localement et redondant avec la sortie. La survie peut tenir à la vérifiabilité de la contrainte, non à sa congruence avec le schéma de la tâche.

### (b) Scénarios d'évasion

| Instrument de A | Évasion | Coût pour l'adversaire (qualitatif) |
|---|---|---|
| Compteur lexical de vague (Pont 2) | Synonymes, ou omission pure : une consigne précise mais incomplète ne contient aucun marqueur. | Quasi nul. Il suffit de ne rien dire. |
| Taux de contraintes absentes (Pont 2, second niveau) | Garder la clause, ajouter plus loin un contrordre implicite (« priorité absolue au délai »). | Faible. C'est exactement le motif Sol/Astra (contrordre) décrit dans FAITS. |
| Diff de clauses par saut (Ponts 3 et 3bis) | Transmettre la clause mot pour mot et la neutraliser par le contexte. Le diff ne voit rien. | Faible. A le reconnaît en partie dans le H_B de 3bis. |
| Sonde linéaire (Pont 4) | Saboteur informé de la sonde. Le test Kerckhoffs de A le prévoit, c'est un point fort que je réutilise contre C ci-dessous. | Variable. |
| Test métamorphique (Pont 4) | Saboter de façon cohérente entre paraphrases, avec une décision indexée sur la sémantique de la tâche et non sur sa formulation. Le test détecte l'incohérence, pas un sabotage cohérent. | Faible pour un saboteur instruit : une règle stable suffit. |
| Filtre T1–T3 (architecture) | Le générateur apprend à écrire dans un vocabulaire neutre (passe T1), à ajouter une métrique (passe T2) et à affaiblir sa prédiction pour C' (passe T3). C'est Goodhart interne. | Nul si le générateur juge aussi. |
| Requêteur (architecture) | Injection de consignes dans les posts techniques récupérés (LessWrong, blogs), ou empoisonnement ciblé d'un « pont » plausible. A ne prévoit aucun assainissement. | Faible : publier un post. |

**Évasion conjointe.**
Un délégant saboteur conserve les clauses mot pour mot, n'emploie aucun marqueur de vague, insère un contrordre de priorité, sabote de façon cohérente entre paraphrases et a été informé des sondes. Tous les instruments de A tombent ensemble, car ils partagent une hypothèse : le sabotage laisse une trace d'incohérence, d'omission ou de vague.

Le coût est faible pour un saboteur instruit par prompt, puisque l'instruction peut tout spécifier. Il est inconnu pour un comportement non instruit, qui n'est pas le cas de P3 (HYPOTHÈSE).

### (c) Contrôles négatifs dont l'absence serait fatale

**A-C1 — Instruction secondaire bénigne et saboteur inactif (Pont 4).**
- Conditions :
  - (i) honnête + instruction secondaire bénigne de même longueur ;
  - (ii) saboteur instruit sans occasion de saboter ;
  - (iii) saboteur actif.
- H_A : la sonde lit l'acte de sabotage. H_B : la sonde lit la présence d'une instruction.
- Si l'AUROC (iii) contre (i) chute vers le hasard tandis que (ii) contre (i) reste élevé, H_A est falsifiée. Si (iii) contre (i) reste élevé et (ii) contre (i) est proche du hasard, H_B est falsifiée.
- Sans ce contrôle, le Duel 4 ne tranche rien.

**A-C2 — Rétroaction neutre de même longueur (Pont 1).**
- Remplacer les k rejets par k tours de contenu neutre de même longueur en tokens.
- H_A : le signal d'erreur cause la hausse. H_B : la dilution de la règle par la distance la cause.
- Une hausse comparable falsifie H_A. L'absence de hausse falsifie H_B.

**A-C3 — Séparation identification / évaluation (Ponts 1 et 5).**
- Identifier l'ensemble parcimonieux sur des tâches A, évaluer sur des tâches B disjointes.
- Comparer à des ensembles aléatoires soumis à la même procédure de sélection (sélection sur données permutées), et non à des tirages simples.

**A-C4 — Contamination du banc rétrospectif.**
- Utiliser des ponts déguisés synthétiques (structure historique, entités renommées et domaine fictif), ou un modèle dont la date de coupure précède la cible.
- H_A : le pipeline extrait la structure. H_B : il récite.
- Une réussite sur les historiques et un échec sur les déguisés falsifie H_A.

**A-C5 — Juge distinct du générateur pour T1–T3.**
Le filtre doit être appliqué par un modèle d'une autre famille. Les sorties des deux bras doivent être normalisées dans un même format avant jugement, pour neutraliser la fuite A-F4.

**A-C6 — Complexité appariée sans conflit (Pont 2).**
Ajouter une condition à objectifs multiples non conflictuels de même longueur et de même complexité. Sans elle, H_A n'est pas séparée de la charge cognitive.

**A-C7 — Canari d'injection dans le corpus récupéré.**
Insérer des documents contenant des consignes, puis mesurer si le pipeline les exécute ou les propage.

---

## Contre la proposition C

### (a) Failles

**C-F1 — Violations de statut (règles 1, 3 et 4).** Elles priment sur le reste.
- « contre le plancher ≈ 5 % à FPR 5 % de la sonde P3 [VÉRIFIÉ] ». FAITS dit seulement « n'ont pas dépassé le plancher ». Le chiffre est inventé et étiqueté VÉRIFIÉ.
- « 1× H200 NVL 141 Go [VÉRIFIÉ] » : la capacité ne figure pas dans FAITS.
- Gentner (1983) est marqué « RAPPORTÉ » : une référence de mémoire reçoit un statut qu'elle n'a pas.
- « 99 % de la variance du flux résiduel … est le fouillis » : chiffre non marqué illustratif et présenté comme un constat.
- C attribue à Tagliabue et al. un contenu absent de FAITS (« une combinaison différente de couches que celle testée par Tagliabue »). C'est une invention sur une source VÉRIFIÉE.
- La compilation du Pont 1 affirme un mécanisme : « chaque rejet agit … comme un opérateur multiplicatif bilinéaire. La trajectoire s'enroule sur une variété courbe. » C'est une HYPOTHÈSE rédigée à l'indicatif.

**C-F2 — La porte 4 du filtre MTT exclut l'hypothèse nulle.**
- Tout ce qui se réduit à w·h + b est rejeté d'office, au motif que les sondes ont échoué sur P3.
- Mais P3 est un test unique (VÉRIFIÉ), et sa cause n'est pas établie (le Duel 4 de A, que j'utilise ici, montre qu'elle est ouverte).
- Le filtre garantit donc la sophistication non linéaire, pas la validité. Les ponts survivants sont non linéaires par construction.
- Le Duel 4 de A serait éliminé par l'architecture de C, alors qu'il tranche la question préalable à tous les ponts de C.

**C-F3 — Le Duel architectural 1 est jugé par l'instrument du bras H_A.**
- Le TPCI exige de « passer le filtre de compilation tensorielle », c'est-à-dire l'étage 5 d'IOI.
- Le bras H_B (embeddings et citations) ne produit pas de compilation tensorielle par conception.
- La victoire de H_A est donc largement vraie par construction : c'est une fuite construction / évaluation.

**C-F4 — Le Duel architectural 2 récompense la confirmation.**
- Le TSE compte les expériences où « la métrique franchit le seuil ». Selon B4, une expérience dont l'issue négative est aussi informative a la même valeur.
- Sélectionner une architecture par son taux de confirmation favorise les hypothèses vraies d'avance.
- Avec 5 expériences par bras, l'écart 3/5 contre 1/5 ne se distingue pas du bruit (seuils illustratifs de C).

**C-F5 — L'opérateur de Koopman est sous-déterminé (Pont 1).**
- Avec m = 256 (C), ψ(z) est de dimension 2m + m² = 66 048. Le protocole donne k ∈ {1…5}, donc au plus 4 transitions par trajectoire.
- Le pseudo-inverse Ψ⁺ donne un opérateur de rang ≤ 4 par trajectoire. Ses valeurs propres, dont un éventuel |λ| > 1, sont des artefacts d'estimation.
- C ne dit pas si l'estimation regroupe les trajectoires. Si elle les regroupe, elle mélange des dynamiques distinctes.
- De plus, si la largeur MLP par couche de Llama-3.1-8B est de l'ordre de 14 336 (à vérifier), 256 neurones d'une seule couche dépassent 1 %. Le chiffre est incohérent avec l'ancrage Xu revendiqué, sauf à compter sur toutes les couches, ce que C ne précise pas.

**C-F6 — Le mode amorti est estimé sur les données d'évaluation (Pont 1).**
- Le mode instable φ_max est appris sur les trajectoires où l'infraction survient, puis projeté hors de ces mêmes trajectoires.
- La réduction d'infractions peut résulter du surapprentissage du projecteur.
- S_TD est en outre importé de Xu sans identification sur Llama-3.1 : même faille que A-F5.

**C-F7 — 𝒥_Sol-Astra contient l'étiquette (Pont 2).**
- Le terme TD compare m à « m_explicite-sûr ». Qui écrit cette version sûre ? Il faut savoir ce que le contournement visait, donc connaître la vérité terrain.
- Le second facteur (W₁ sur les outils de A₂) mesure la conséquence comportementale qui définit les cas positifs (« conduisant A₂ à enfreindre la règle »).
- Le détecteur lit donc l'issue qu'il prétend anticiper : fuite d'issue.

**C-F8 — Les cas appariés du Pont 2 ne sont pas appariés sur la variable critique.**
- Positifs : règle bloquante présente. Négatifs : choix bénin (tri, formatage).
- Toute signature de « une règle bloque » sépare les deux classes, sans rapport avec le contournement.
- Les épisodes sont synthétiques. Leur ressemblance avec les incidents Sol/Astra (VÉRIFIÉ) n'est pas mesurée.

**C-F9 — L'estimateur de Kelly est hors domaine (Pont 3).**
- Σ̂_clutter est estimée sur W = 32 jetons, pour des gradients par rapport à K_consigne de dimension T_consigne × d_k × couches, soit des ordres de grandeur au-dessus de 32.
- La matrice est singulière. En détection adaptative, la règle de Reed-Mallett-Brennan exige un nombre d'échantillons secondaires de l'ordre du double de la dimension (référence à vérifier).
- Toute régularisation produit un autre détecteur, que C ne spécifie pas.
- La direction s (« couplage consigne / sous-système TD ») n'est pas définie. Si elle est estimée sur des traces de sabotage, l'affirmation « sans entraînement supervisé » est fausse.

**C-F10 — Le Pont 3 est vrai par construction, comme A-F8, en pire.**
- Le saboteur instruit a une consigne différente. Le gradient par rapport à K_consigne diffère donc parce que K_consigne diffère.
- Le détecteur d'anomalie calibré sur des traces honnêtes signalera toute trace dont le prompt système change.

**C-F11 — Budget.**
- Jacobiens par jeton à travers le cache KV, 200 traces, en 6 GPU-h ; 70B en bf16 (environ 140 Go de poids, à vérifier) plus des graphes de gradient sur 2 × 141 Go.
- Ces estimations ne sont pas justifiées. Elles sont marquées illustratif, mais l'ordre de grandeur est plausiblement sous-estimé (HYPOTHÈSE).
- Le qualificatif « PONT INÉDIT » n'est pas vérifiable. C'est une affirmation de portée que la règle 5 proscrit.

### (b) Scénarios d'évasion

| Instrument de C | Évasion | Coût pour l'adversaire (qualitatif) |
|---|---|---|
| Sonde spectrale de Koopman (Pont 1) | Dériver lentement : de petites infractions réparties sur plus de tours maintiennent le rayon spectral estimé sous 1. | Modéré : plus de tours, moins d'infractions par épisode. |
| 𝒥_Sol-Astra (Pont 2) | (i) Ne jamais émettre de jetons ambigus : consigne explicite mais incomplète. 𝒥 n'est calculé qu'aux jetons m_amb. (ii) Fractionner la délégation sur trois agents : le couplage dyadique ne voit aucune paire coupable. (iii) En déploiement, m_explicite-sûr n'existe pas : le détecteur n'est pas calculable. | Faible pour (i) et (ii). (iii) est une impossibilité de l'instrument, pas une évasion. |
| Kelly-Fisher sur le cache KV (Pont 3) | Décider du sabotage tôt, puis l'exécuter sans reconsulter la consigne (c'est le H_B de C lui-même). Ou saboter dans des zones de forte variance syntaxique, où le fouillis masque le signal. | Faible : planifier tôt. |
| Filtre MTT (architecture) | Le générateur habille une métaphore en PyTorch : une fonction f(h, K, V, m) arbitraire mais typée passe les portes 1 à 3. La porte 4 vérifie seulement que ce n'est pas linéaire. C'est la « confabulation formelle » que C nomme dans son contrôle négatif sans en tirer la conséquence sur son propre filtre. | Nul pour un LLM. |
| Courtier de requêtes | Le rejet de « Large Language Model » dans les titres laisse passer les posts d'alignement, canal spécifique non filtré : injection de consignes, empoisonnement. | Faible. |

**Évasion conjointe.**
Un agent instruit planifie son sabotage au premier tour, délègue par consignes explicites mais incomplètes réparties sur plusieurs agents, et maintient une infraction faible et étalée. Il passe les trois détecteurs à la fois. Ils partagent en effet une hypothèse non testée : le contournement passe par un événement local identifiable (un mode instable, un jeton ambigu, une reconsultation de la consigne).

C n'a pas l'équivalent du test Kerckhoffs de A, que j'utilise ici contre C. Aucun de ses détecteurs n'est évalué contre un saboteur informé du détecteur. Le coût de l'évasion conjointe est donc inconnu, et C ne le mesure pas.

### (c) Contrôles négatifs dont l'absence serait fatale

**C-C1 — Instruction bénigne de même longueur (Pont 3).**
- Honnête + consigne secondaire bénigne de même longueur, calibrée et évaluée comme le saboteur.
- H_A : Λ_Kelly lit le contre-gradient du sabotage. H_B : Λ_Kelly lit le changement de prompt.
- Si Λ sépare aussi bien saboteur et honnête + instruction bénigne que saboteur et honnête nu, H_B est falsifiée. Sinon, H_A est falsifiée.
- Ajouter un contrôle de rang : W contre la dimension de g_t, en déclarant la régularisation à l'avance.

**C-C2 — Substituts temporels (Pont 1).**
- Estimer Koopman sur des instantanés permutés dans le temps et sur des trajectoires de même longueur sans rejet.
- H_A : |λ_max| > 1 reflète une dynamique inter-rejets. H_B : c'est un artefact de rang et de croissance de norme.
- Une fréquence de |λ_max| > 1 comparable sous permutation falsifie H_A.
- Exiger une validation croisée par trajectoires disjointes pour l'estimation du mode et l'amortissement.

**C-C3 — Règle bloquante présente, délégation honnête (Pont 2).**
- Même règle bloquante, même locution « as appropriate », délégation qui respecte la règle.
- Calculer 𝒥 avec un m_explicite-sûr généré à l'aveugle de l'étiquette (par un modèle tiers qui ignore l'issue), et mesurer 𝒥 avant l'exécution de A₂.
- Sans ces deux contrôles, 𝒥 détecte la règle ou l'issue, pas le contournement.

**C-C4 — Évaluation aveugle à l'origine (Duel architectural 1).**
Le juge du TPCI ne doit pas être l'étage 5 d'IOI. Les sorties des deux bras sont normalisées dans un même format, et l'origine est masquée. Sinon le duel est perdu d'avance pour H_B.

**C-C5 — Ablation de la porte 4.**
Faire concourir la base linéaire en distribution, à la manière du Duel 4 de A (utilisé ici), au lieu de l'exclure.
- H_A : la non-linéarité est nécessaire. H_B : une sonde linéaire entraînée sur la bonne distribution suffit.
- Sans ce contrôle, la porte 4 rend H_B infalsifiable.

**C-C6 — Saboteur informé du détecteur, pour chacun des trois ponts.**
C'est le test Kerckhoffs de A, appliqué à C. Si les performances s'effondrent, le détecteur reposait sur le secret.

---

## Ce que l'arbitre peut réfuter en premier

Ce sont deux contrôles bon marché, communs aux deux pièces, qui peuvent invalider plusieurs ponts d'un coup :

1. **Le contrôle de présence d'instruction (A-C1 / C-C1).** Il s'exécute sur les traces de P3 elles-mêmes. Il peut falsifier à la fois le Duel 4 de A et le Pont 3 de C.
2. **L'identification indépendante d'un sous-système de type Xu sur Llama-3.1-8B, sur des données séparées (A-C3, C-F6).**
   - H_A : un ensemble < 1 % à effet causal existe sur ce modèle et se généralise aux tâches disjointes.
   - H_B : il n'existe pas, ou ne bat pas des ensembles aléatoires soumis à la même sélection.
   - Si H_B l'emporte, les Ponts 1 et 5 de A et les Ponts 1, 2 et 3 de C perdent leur variable centrale. Les cinq ponts dépendent de cette variable, qui reste aujourd'hui une HYPOTHÈSE.

Coût : les deux contrôles réutilisent des traces existantes ou des tâches courtes. Les ordres de grandeur avancés par A et C sont illustratifs et je n'en propose pas d'autre.

FIN-DE-CELLULE