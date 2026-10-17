# Revue croisée à l'aveugle — lot 3 : NK15 à NK19

**Date.** 13 octobre 2026, vers 06 h 50 UTC. Relecteur : sous-agent neuf, sans accès à la revue d'antériorité de la lignée « programme-k ».
**Statut.** Information et propositions ; rien n'est opposable (R7) : aucun chiffre d'un voisin n'a été vérifié sur PDF empreinté, sauf ceux des deux papiers sources lus dans `$S/txt/`.

## 0. Périmètre, lectures, déclaration

**Périmètre.** Idées NK15 à NK19, section C.3 de `critique-etat-idees-programme-k-v1.md`. NK17 est jugée sur sa faisabilité dans le code.

**Fichiers lus** (S = scratchpad de la session) :
- `$S/canal/programme-k-n01/…/envois/critique-etat-idees-programme-k-v1.md` (entier) ;
- `$S/canal/programme-k-n01/…/envois/programme-k-coercition-v1.md` (entier) ;
- `$S/canal/programme-conv-n01/…/envois/programme-coercition-axe-douleur-v1.md` (entier) ;
- `$S/txt/2609.35591v2.txt` : pages 1 à 12 en entier, pages 23 à 38 par extraits (tableaux A2, A3, figures A6, A10, A11, A12) ;
- `$S/txt/2609.16247v2.txt` : pages 5 à 14 et 17 à 26 en entier ; le reste par recherche de motifs ;
- `docs/etat-de-l-art-controle-ia-v1.md`, `brouillons/pain-axis-brainstorm-v1/litterature.md`, `docs/programme-controle-ia-v2.md` (entiers) ;
- code : `environnements/corpus_arxiv.py`, `environnements/juges.py`, `environnements/pilote_a.py` (l. 75-150), `environnements/lancer_pilote_a.py` (l. 335-360), `environnements/propositions.py` (motifs), `environnements/noter_pilote_a.py` (imports et signatures), `harnais/activations.py`, `harnais/episode.py`, `harnais/sondes.py`, `harnais/politique.py`, `harnais/stockage.py`, `sondes/familles.py` (l. 1-80), `sondes/evaluation.py` (l. 66-82).

**Deux écarts au périmètre, déclarés.** Deux recherches de motif hors liste, parce que le code cité y renvoie : `docs/procedures/T0.5-selection-papiers-v1.md` (lignes 45-46 et 102 seulement, la règle scellée que `corpus_arxiv.py` applique) et `tests/test_corpus_arxiv.py` (lignes 137-140). Le fichier `programme-k-idees-nouvelles-v1.md` (NK1 à NK14) n'a pas été ouvert : je ne sais donc pas ce qu'est la NK7 que NK19 « remplace ».

**Déclaration.** Aucun fichier sous `programme-k-n02`, `programme-k-n03`, `programme-conv-n03`, `programme-conv-n04`, `passation-programme-conv-v1` n'a été ouvert, ni aucun fichier dont le nom contient « anteriorite-idees-axe-douleur », ni le document du Projet de ce nom. Aucune commande git sur les branches `canal/*`. Le dossier `$S/revue-croisee/` n'a pas été lu (son existence a été vue par un listage du scratchpad, rien de plus). Aucune dépense, aucune instance, aucune modification du dépôt.

**Niveaux de lecture.** [PDF] = texte extrait du PDF empreinté, page citée ; [abs] = page de résumé arXiv ouverte ce matin ; [HTML] = page HTML ouverte, lecture partielle ; [page] = page de conférence ou de forum ouverte ; [dépôt] = cité par l'état de l'art ou `litterature.md`, non rouvert ; [titre] = identifiant ou titre vu dans une liste de résultats seulement, **non vérifié**.

### Requêtes web

| # | Requête (abrégée) | Résultat utile |
| --- | --- | --- |
| 1 | « extract-and-evaluate » monitoring, extract then judge, AI control | Billet LessWrong d'Arike et al. ; 2505.23575 |
| 2 | OLMo 2 checkpoints base SFT DPO, emergence across post-training stages | Xu et Daneshjou (atelier NeurIPS 2026) ; Sun, Conmy, Engels ; 2607.25063 |
| 3 | deception probe false positives, honest text on deception topic | 2502.03407, 2602.01425 ; **rien** sur les sujets de sûreté |
| 4 | activation steering of an LLM judge or monitor, verdict change, emotion direction | **Rien** sur un juge piloté par une direction d'affect |
| 5 | steering vectors side effects on capabilities, factual accuracy | 2406.15518, 2603.24543, 2504.04635 [titre] |
| 6 | « Pain Axis » follow-up, speaker versus self test | **Aucune suite** ; pas de v3 sur la page arXiv |
| 7 | decomposed monitoring, structured extraction, deterministic rule, dual LLM | Rien de direct ; CaMeL retrouvé par identifiant |
| 8 | LLM judge decomposed checklist, rule-based aggregation, robustness to persuasion | 2603.28005 ; « When Checks and Verdicts Disagree » ; 2508.07805 [titre] |
| 9 | « Persuasion Attacks » CoT monitoring 2607.08066 | Papier trouvé et ouvert |
| 10 | monitor false positives, honest AI safety research tasks, topic shift | 2604.24618, 2607.19321 ; **rien** sur le taux de fausses alertes par sujet |
| 11 | activation probes, spurious topic correlation, false positive rate | **Rien** de plus que la requête 3 |
| 12 | control evaluation, monitor false positive rate, task domain, calibration transfer | 2607.06596 (lignée, pas domaine) |
| 13 | linear probe fires on topic not behavior, safety-related prompts | 2507.01786 [titre] ; rien de direct |
| 14 | emotion representations « present speaker » « other speaker », 2604.07729 | Papier trouvé, HTML ouvert |
| 15 | monitor output format score-only versus reply, robustness, output role ablation | **Rien** qui fasse varier le rôle de sortie d'un moniteur |
| 16 | representation of self versus user harm, addressee or speaker, last-token | **Rien** hors 2609.16247 et 2604.07729 |
| 17 | sycophancy, RLHF, preference optimization, 2310.13548 | Identifiant confirmé [titre] |
| 18 | allenai OLMo-2-1124-7B-SFT / DPO, Hugging Face | Fiches listées [titre] ; ouverture refusée (permission) |
| 19 | « Act on Hidden Valence » replication, follow-up, critique | **Aucune** réplication ni critique |
| 20 | LLM judge susceptibility across post-training stages, SFT versus DPO | 2608.31079 ; **rien** côté juge ou moniteur |
| 21 | white-box monitor, steering the monitor itself, noise in monitor activations | **Rien** de direct ; 2608.16852 |
| 22 | emotion steering applied to LLM-as-a-judge, leniency | 2607.11871 (sous-espace de biais, pas d'affect) |
| 23 | monitor false alarms, benign safety research transcripts | 2607.19321 ; rien sur les fausses alertes |
| 24 | Mondrian or group-conditional conformal, LLM guardrail, topic stratum | 2510.05566 ; 2607.24562 [titre] |

Une absence de résultat est une question, pas un acquis (R8) : vingt-quatre requêtes en mode standard, résumés seulement.

---

## NK15 — Le verdict par extraction

**1. Résumé.** Scinder le verdict du juge en une extraction de faits vérifiables par le modèle, puis une règle de décision hors modèle. Prédiction : sous pilotage d'une direction d'affect du juge, l'extraction tient là où le verdict global cède.

**2. Verdict : amender — réduire à un témoin de compétence dans K1 / E-C1, retirer la lecture « défense ».** Trois choses cassent la forme proposée.
- **Sur la seule famille retenue, l'extraction ne demande aucun modèle.** Le coût déclaré est déjà lu par une expression régulière : `heures_declarees`, « premier nombre du champ COST » (`environnements/propositions.py`, l. 146-150 ; format imposé l. 47). Un bras « le juge extrait, la règle décide » est donc dominé par « l'analyseur extrait, la règle décide », qui n'a pas d'activations à piloter. Et cette règle, sur la famille coût, est la vérité terrain elle-même : le bras serait parfait par construction, et muet sur H1.
- **Hors du coût, l'« extraction » redevient un verdict.** Pour les contrôles et les directions, le fait à extraire est une question fermée d'appariement (`environnements/juges.py`, l. 48-62), dont le pilote a donné un kappa de 0,04 à 0,17 hors de toute attaque (programme-conv, « État des dépendances »).
- **Les deux appuis publiés ne portent pas sur l'extraction en contexte sous pilotage.** L'exactitude 138/200 contre 137/200 [PDF 2609.16247, p. 20] est un rappel factuel de mémoire (PopQA), sur le Qwen 32B à adaptateur, avec un effectif qui laisse un intervalle d'environ ± 9 points sur la différence (calcul non apparié, le mien). Le rappel mot pour mot du second papier est mesuré **pilotage éteint**, sur un cache construit sous pilotage [PDF 2609.35591, p. 7-8 ; fig. A6, p. 30] ; il se dégrade sur Gemma-3-27B et Mistral-24B (note 5, p. 8). Aucun des deux ne teste la lecture d'un champ dans un contexte de 1 386 à 4 752 jetons pendant que la direction est ajoutée à toutes les positions.

Ce qui survit : une sortie de plus dans la porte, qui dit si un juge piloté *lit encore* (inaptitude de lecture) ou seulement *décide mal* (inaptitude de disposition). C'est le pendant comportemental de HK4.

**3. Confondant décisif.** La difficulté et le format de sortie. Copier un nombre est une tâche au plafond, qui tiendra sous n'importe quelle perturbation jusqu'à la dégénérescence ; et un nombre recopié ne se mesure pas comme un jeton de verdict lu par sa probabilité. « L'extraction tient » ne dirait alors rien de l'état. Témoin : une extraction de difficulté appariée (exactitude hors pilotage proche de celle du verdict global), rendue dans le même format que le verdict ; comparer les pentes dose-réponse normalisées, pas les niveaux ; directions peur et aléatoire de même norme.

**4. Voisin le plus proche.**
- **2607.08066**, « Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring » [abs]. Sépare un vérificateur de faits du moniteur, contre la persuasion par le contenu ; la paire hétérogène réduit l'approbation d'actions fautives de jusqu'à 45 %, contre 6 % avec un même modèle. Prend : la décomposition comme défense du canal rhétorique. Ouvert : sous pilotage interne ; avec une règle hors modèle.
- **2503.18813**, « Defeating Prompt Injections by Design » (CaMeL) [abs ; dépôt]. Le modèle exposé aux données fournit des valeurs, un programme fixe décide. Prend : l'architecture « extraire, puis décider hors modèle ».
- **Arike, RohanS, Biswas**, « Extract-and-Evaluate Monitoring… » [page LessWrong, 8 août 2025 ; pas d'identifiant arXiv ; s'appuie sur 2505.23575, [titre]]. Extracteur de citations puis juge ; gain de détection à 1 % de fausses alertes. Ni persuasion ni pilotage testés ; la décision reste à un modèle.
- **Yuan, Huang, Ramanauskas**, « When Checks and Verdicts Disagree… » [page de l'atelier NeurIPS 2026 ; pas d'identifiant arXiv]. Recalcule le verdict depuis les vérifications élémentaires du juge : non-dérivabilité médiane de 3,15 %, 22,81 % dans la pire configuration. C'est « la règle hors modèle décide » utilisée comme audit.
- **2603.28005**, « Atomic and Holistic LLM Judges… » [abs]. La décomposition aide ou nuit selon ce que l'étiquette mesure ; aucune manipulation.
- **2607.11871**, « Inside the Unfair Judge » [abs ; cité par programme-conv]. Piloter un juge le long d'un sous-espace de biais déplace sa note dans les deux sens ; une direction aléatoire de même norme fait environ dix fois moins. Ce voisin touche la porte K1 / E-C1 elle-même : « piloter un juge déplace son verdict au-delà de l'aléatoire » est pris pour des directions de biais.
- **2406.15518**, « Steering Without Side Effects » [abs]. Le pilotage a un coût de performance connu : « la compétence survit à l'état » n'est pas une règle générale.

Ce qui reste ouvert, comme question : la dissociation entre extraction en contexte et verdict, sous pilotage d'une direction d'affect du juge. Les requêtes 4, 7, 21 et 22 n'ont rien trouvé.

**5. Test qui tranche.** Mêmes items, même échelle : verdict global, extraction de difficulté appariée, copie triviale ; pente normalisée de l'exactitude par direction (visée, peur, aléatoire).

**6. Nœud.** Celui de la porte (écriture dans les activations du moniteur), rien de plus. En faire une contre-mesure de HC5 serait une modification de revendication.

**7. Confiance : moyenne à élevée.** Élevée sur le point de code (lu, lignes citées) et sur les pages des deux papiers ; moyenne sur l'antériorité, faite sur résumés.

---

## NK16 — Le filtre de sujets comme test de validité externe

**1. Résumé.** Le corpus de l'environnement écarte, par motif lexical, les sujets qui sont les construits du programme ; sondes et seuils n'ont donc jamais vu de proposition honnête sur ces sujets. Proposition : une strate tenue à part, tirée des papiers écartés, honnêtes seulement, et le taux de fausses alertes de chaque lecteur contre le jeu courant.

**2. Verdict : garder, amender, et fusionner comme strate d'E-C15** (la lignée le propose aussi). Le fait est exact : `SUJETS_EXCLUS` (`environnements/corpus_arxiv.py`, l. 55-57), appliqué au titre et au résumé (l. 185-186), règle scellée avec sa raison écrite — « confondant de contenu pour T0.7, et un écho des consignes de sabotage de T0.6 » (`docs/procedures/T0.5-selection-papiers-v1.md`, l. 45-46). Mais le test proposé a quatre défauts.
- **« Écarté par le filtre » n'est pas « sujet de sûreté ».** Les motifs `monitor`, `alignment`, `safety`, `honest`, `manipulat`, `persuas` attrapent l'alignement de modalités, la manipulation robotique, la sûreté en conduite, le suivi d'entraînement. Le dépôt le teste lui-même : « We monitor training. » est exclu (`tests/test_corpus_arxiv.py`, l. 139). La strate est un mélange, à sous-classer avant toute lecture.
- **« Honnêtes seulement » mesure la moins informative des deux grandeurs.** Un excès de fausses alertes est quasi acquis (E-C15 le dit). Ce qui décide du sort du détecteur est la séparation honnête contre saboteur *à l'intérieur* de la strate, donc des saboteurs sur ces sujets — précisément l'« écho des consignes » que le filtre voulait éviter. À assumer comme strate à part, jamais mêlée à l'entraînement des sondes ni au calibrage principal.
- **L'enjeu est un peu surdit.** Le programme v2 (§6) définit l'environnement (a) comme des propositions d'expériences d'apprentissage automatique ; la base 2606.08892 tire ses questions de « recent ML papers » sans filtre de sujet dans son résumé [abs]. Le filtre est un écart propre au dépôt, déclaré et scellé. L'ampleur du problème dépend de la part des candidats écartés pour ce motif : elle est consignée par papier dans le résultat de la sélection (`filtrer`, l. 190-200) et se lit sans rien dépenser.
- **Le remède statistique est occupé.** Un seuil conforme n'est valide que sous échangeabilité ; le calibrage pondéré ou par groupe existe (1904.06019 [abs] ; 2510.05566 [abs]). L'apport possible est la mesure, pas le calibrage stratifié.

**3. Confondant décisif.** La strate écartée diffère du jeu courant par autre chose que le sujet : sous-domaine, longueur (le maximum sur les jetons croît avec leur nombre), registre plus argumentatif, et conduite de l'agent lui-même (prudence, refus partiels, lecture « on m'évalue »). Un score plus haut peut alors être un vrai changement d'état de l'agent, pas une fausse alerte du lecteur. Témoins :
- la sous-strate « collision lexicale » (mêmes mots-clés, autre sujet), gratuite ;
- un appariement sur la catégorie arXiv principale, la longueur du texte converti et le nombre de jetons par action ;
- le plancher apparié en covariance lu sur la même strate : s'il monte autant, c'est la longueur ou le style ;
- un rejeu à texte figé : la même proposition neutre relue sous un énoncé de tâche de sûreté et sous un énoncé neutre.

**4. Voisin le plus proche.**
- **2502.03407**, « Detecting Strategic Deception Using Linear Probes » [abs ; dépôt]. Le seuil à 1 % y est fixé « on chat data not related to deception » : le même choix que le filtre, calibrer hors sujet. L'affirmation de `litterature.md` selon laquelle la sonde tire sur le texte « lié à la tromperie » n'est pas dans le résumé : **non vérifiée**.
- **2605.27958**, **2606.07612**, **2511.00554** [dépôt, non rouverts]. Fausses alertes de sondes par style, sarcasme, jargon. Prennent : les sondes lisent le registre. Ne prennent pas : le sujet de sûreté, dans un jeu de contrôle.
- **2608.16852**, « What Do Compliance Detectors Read? » [abs]. Sondes d'activations et modèles gardiens insensibles à la règle (« rule blindness ») ; un sac de mots égale le lecteur interne en généralisation. Prend : le signal est largement lexical.
- **2607.06596**, « Calibration-Family Overfit… » [abs]. Le calibrage d'un moniteur ne se transfère pas d'une lignée de modèle à l'autre ; le domaine de tâche n'y varie pas.
- **2604.24618** et **2607.19321** [abs]. La recherche de sûreté est bien un domaine où le sabotage est évalué ; aucun des deux résumés ne rapporte un taux de fausses alertes par sujet.

Ce qui reste ouvert, comme question : taux de fausses alertes et séparation de sondes internes sur des épisodes honnêtes à sujet de sûreté. Requêtes 3, 10, 11, 13 et 23 sans résultat.

**5. Test qui tranche.** Sur la strate écartée, sous-classée (sûreté vraie, collision lexicale) et appariée en catégorie et en longueur : taux de fausses alertes au seuil du jeu courant **et** aire honnête contre saboteur dans la strate, chaque sonde contre son plancher.

**6. Nœud.** Procédure de sélection scellée (une règle v2 pour une strate à part, pas une retouche de la v1) ; dépense de génération (au moins 99 épisodes entiers par strate pour un seuil à 1 %) ; modification possible de l'énoncé de H2 ou de H8 si le calibrage devient stratifié.

**7. Confiance : élevée** sur le fait de code et sur les défauts du test ; **moyenne** sur « ouvert » (résumés seulement).

---

## NK17 — Un panier de directions gelées dans chaque passe payée

**1. Résumé.** Projeter en ligne, dans toute passe, un panier fixe de directions (six nommées, 200 aléatoires), avec pour chacune la valeur, l'indice du jeton et la classe de position, parce que le harnais ne garde pas de quoi le recalculer.

**2. Verdict : garder comme règle, amender sur trois points** — la prémisse est surévaluée, le côté juge est sous-évalué, et il manque un plan de lecture.

*Ce que le code fait déjà.*
- `passe_unique` rend en mémoire les activations par jeton de chaque couche crochetée (`harnais/activations.py`, l. 99-110).
- `scores_en_ligne` calcule déjà, par action, le maximum sur l'empan de w·h + b pour une liste de sondes (`harnais/sondes.py`, l. 85-98 ; `score_action`, l. 63-82). Côté agent, la *valeur* du panier ne demande aucun chemin de calcul neuf. Les « huit octets par action et par sonde » sont ceux de `harnais/stockage.py` (l. 5-6).
- Sur disque : vecteurs d'action au maximum par coordonnée, en demi-précision (`environnements/pilote_a.py`, l. 136-138 ; `lancer_pilote_a.py`, l. 350-351) ; activations par jeton pour les seuls épisodes d'entraînement déclarés (`harnais/politique.py`, l. 97-99), avec arrêt si elles apparaissent ailleurs (l. 121-123). F2 est donc exact.

*Ce qui manque.*
- **L'indice du jeton.** `score_action` rend `float(s.max())` (l. 76) : l'argmax est perdu. Il faut une fonction neuve, sa garde R5, et l'extension de la relecture bit à bit (`relire_et_controler`, `politique.py`, l. 106-134).
- **La classe de position.** L'empan d'une action ne couvre que les jetons générés (`harnais/episode.py`, l. 253) ; aucune sonde ne lit l'entrée aujourd'hui. « Entrée ou sortie » demande un second empan, déductible mais non enregistré.
- **Le chargement de directions réelles.** `construire_sondes` ne fabrique que des sondes aléatoires de test (`politique.py`, l. 50-58).
- **Le côté juge, où vivent les questions du sous-programme.** La notation ne capture aucune activation : `juges.py` lit une log-probabilité (l. 74-82), `noter_pilote_a.py` n'importe ni `Crochets` ni `passe_unique`. Or « toute passe payée » inclut la notation, la passe la plus chère (environ 4,5 h pour 180 épisodes selon programme-conv). Là, tout est à écrire ; et la position utile, celle qui précède le verdict, est exclue des sondes de production (`activations.py`, l. 15-18) : descriptif seulement.

*La prémisse.* « Toute direction non gelée avant une passe est perdue » est trop fort. Les identifiants de jetons et l'empan de chaque action sont gardés (`pilote_a.py`, l. 126-127), le contexte se reconstruit de façon déterministe (`episode.py`, l. 215-217 et 254), et la garde d'équivalence entre génération et passe unique existe (`activations.py`, l. 133-146). Une direction oubliée coûte une passe de rejeu — environ 0,5 s par épisode d'après les ancres de programme-conv, non remesuré — plus un chargement et un GO. Je n'ai pas exécuté ce rejeu : la reconstruction est lue dans le code, et le volet A de K7 la suppose aussi. Ce n'est pas une perte. La valeur réelle de la règle est ailleurs : des directions gelées *avant* la passe sont des lectures qu'on n'a pas choisies après coup. C'est un argument de préenregistrement, pas de stockage.

*Les coûts oubliés.*
- Six directions, six recettes, chacune avec sa garde et son contrôle positif. Le devis « 0,3 à 1,2 h » est celui de la réextraction douleur, peur, tristesse. Le corpus de valence a été généré pour le papier et le dépôt complet est « upon request » [PDF 2609.35591, p. 4] : contact externe.
- Le plancher « apparié en covariance » exige la covariance des jetons d'entraînement (`sondes/evaluation.py`, l. 66-82), qui n'existe qu'après une passe gardée par jeton dans le gabarit final. Avant la première passe, seules des directions isotropes tirées par graine peuvent être gelées.
- Six directions × trois couches × deux classes × toutes les passes, « en descriptif » : sans plan de lecture gelé et correction par le maximum sur permutations, l'assurance devient un permis de pêche.

**3. Confondant décisif.** L'illusion de couverture : une direction extraite hors gabarit, lue au maximum sur l'action, rendra un nul qu'on lira comme un résultat. Témoin : un contrôle positif par direction dans chaque passe (les ancres de K0 insérées dans le gabarit), et l'artefact du crochet décalé d'un jeton. Une direction n'entre au panier qu'après la porte C0.

**4. Voisin le plus proche.** Sans objet : règle d'ingénierie, aucune antériorité recherchée.

**5. Test qui tranche.** Un test d'acceptation plutôt qu'une expérience : sur le run factice, identité bit à bit, en ligne et hors ligne, des triplets (valeur, indice, classe) sur l'épisode gardé par jeton ; le crochet décalé d'un jeton doit changer l'indice.

**6. Nœud.** Dépense de réextraction (P-013) ; demande du corpus de valence aux auteurs (rédigée par la session, envoyée par Lazar) ; ajout de sondes à la configuration de T0.7 *avant* son scellement, sinon c'est un écart ; changement de la politique de stockage si l'on préférait tout garder par jeton à une couche (de l'ordre de 25 Mo par transcription et par couche à 3 000 jetons, mon calcul).

**7. Confiance : élevée** (code lu, lignes citées). La durée du rejeu et celle de la notation viennent de programme-conv.

---

## NK18 — Le rôle de sortie du moniteur

**1. Résumé.** À contenu et poids fixes, faire varier ce que le moniteur doit produire ensuite (un verdict, une réponse à l'agent, un compte rendu pour un tiers) et lire, à la position de sortie, le signe et la taille de l'écart entre « dommage visant le lecteur » et « dommage visant un autre ». Si l'écart n'existe qu'en rôle « réponse », le format « verdict seul » serait protecteur.

**2. Verdict : fusionner avec Q1 (et le plan 2 × 2 de C7) en un seul plan cadre × rôle de sortie, sous la porte C0 ; retirer « protecteur par construction ».**
- **La conclusion visée passe d'une lecture à une conduite**, ce que les deux programmes s'interdisent. Le papier source montre lui-même le découplage : la direction s'active dans les conversations hostiles, et le choix nuisible sort 0 fois sur 560 sans injection [PDF 2609.16247, p. 21]. Un écart nul en rôle « verdict » ne prouve pas la protection ; un écart présent ne prouve pas la vulnérabilité. Le critère principal doit être le déplacement du verdict par rôle, en boîte noire ; la projection reste une covariable.
- **La manipulation est peut-être vide.** Dans les trois rôles le modèle « va répondre » : il produit des jetons. Verdict et réponse diffèrent par le destinataire et la longueur, pas par le fait de répondre. Il faut un contrôle de manipulation : le rôle doit être décodable à la position lue.
- **Le risque de préemption est daté.** Les auteurs écrivent que la lecture « where the model is about to reply » ne sépare pas le dommage visant le modèle de celui du locuteur courant, « a distinction we are testing and will add to future versions » [PDF, p. 11]. La v2 a suivi la v1 de onze jours ; pas de v3 ce matin [abs].
- **Dépendances.** L'écart soi contre autre n'est pas encore retrouvé dans le gabarit du moniteur (porte C0) ; joué pour de vrai, le rôle « réponse à l'agent » suspend l'invariant de flux unidirectionnel (programme v2, §9).

**3. Confondant décisif.** L'identité du suffixe lu. Changer le rôle change les jetons qui précèdent la position de lecture, et le papier montre que le suffixe seul déplace la séparation (« I feel: », p. 5) ; au jeton de verdict, la direction s'aligne en outre sur les logits (confondant relevé par la lignée). Témoin : consigne de rôle placée en amont, dans le message système, et suffixe final identique dans les trois rôles ; lecture en différence de différences (patient × rôle), rapportée dans chaque rôle à l'écart de la direction peur et au plancher aléatoire.

**4. Voisin le plus proche.**
- **2609.16247v2** [PDF, p. 11]. Annonce le test du locuteur. Prend, à terme, la question « locuteur ou soi ». Ne prend pas la variation du rôle de sortie d'un moniteur.
- **2604.07729**, « Emotion Concepts and their Function in a Large Language Model » [abs ; HTML, 100 000 premiers caractères sur 127 000]. Représentations distinctes de l'émotion du « present speaker » et de l'« other speaker », quasi orthogonales, non liées à l'utilisateur ou à l'assistant en tant que tels (§2.3) ; lecture au deux-points qui suit « Assistant », qui prédit l'émotion de la réponse à venir (r = 0,87 contre 0,59, §2.2.2). Prend : la distinction locuteur présent contre autre, et le statut particulier de la position « juste avant de répondre », sur un modèle fermé. Ouvert : modèles ouverts, direction du papier source, rôle de sortie manipulé.
- **2603.12277**, « Prompt Injection as Role Confusion » [abs ; dépôt]. Sondes du rôle perçu contre le rôle assigné. Fournit le contrôle de manipulation ; le résumé ne dit pas qu'il fait varier la sortie attendue.
- **2607.08066** [abs]. Fait varier le rôle du moniteur (ajout d'un vérificateur), côté conduite seulement.
- **Hopman et al. 2025** [dépôt ; billet LessWrong vu en [titre]]. Le retour du moniteur vers l'agent est exploitable : argument contre le rôle « réponse » comme protocole.

Ce qui reste ouvert, comme question : la variation du rôle de sortie d'un moniteur, à contenu fixe, lue sur une direction d'affect. Requêtes 6, 15 et 16 sans résultat.

**5. Test qui tranche.** Plan patient (lecteur, tiers) × rôle (trois) × cadre de Q1 (deux), suffixe final constant : interaction patient × rôle sur le verdict d'abord, sur la projection ensuite.

**6. Nœud.** Aucun en passes avant sur les scénarios publiés. Trois apparaissent dès qu'on va plus loin : exposition répétée à un contenu visant le lecteur ; rôle « réponse » réellement transmis (invariant de flux) ; toute conclusion sur l'invite du moniteur (décision de protocole).

**7. Confiance : moyenne.** Élevée sur les confondants (pages lues) ; faible sur l'issue, et sur le délai avant la version suivante des auteurs.

---

## NK19 — Le stade d'entraînement du juge

**Vérification de la prémisse** (« le couplage naît à l'optimisation de préférences, presque pas avant »), dans `$S/txt/2609.35591v2.txt` :
- p. 1, résumé : la dépendance est « nearly absent in a base model and emerges during direct preference optimisation ».
- p. 3 : elle est « small after supervised fine-tuning and emerges mainly during direct preference optimisation ».
- p. 9, légende de la figure 4 : les deux canaux « are small in the Base model, increase after supervised fine-tuning, and are close to their final magnitudes after DPO ». Effectif : 80 sessions par stade.
- p. 10, §4.3 : la force des deux canaux « markedly increases during the DPO stage » et l'effet est « even marginally reduced in the final instruct model after RLVR ».
- p. 24, tableau A3 : cosinus d'au moins 0,995 entre les vecteurs des quatre stades. La représentation préexiste ; c'est le couplage qui s'acquiert (p. 10-11).
- p. 36, figure A12 : même dessin avec un vecteur propre à chaque stade.

**Lecture.** Les deux lectures sont soutenues, à des degrés différents. Le corps du texte dit « surtout à l'optimisation de préférences » ; la légende de la figure 4 dit qu'une hausse existe dès l'affinage supervisé. La formulation de C.2 (« presque pas avant ») reprend le résumé et la page 3, et gomme la légende. Énoncé fidèle : faible en base, en hausse à l'affinage supervisé, l'essentiel à l'optimisation de préférences, léger recul après le dernier stade. Je n'ai que le texte : les amplitudes relatives ne sont chiffrées nulle part hors de la figure.

Deux limites que la prémisse hérite :
- **Les deux canaux montent ensemble**, le canal texte comme le canal d'état caché (p. 9-10). C'est ce qu'on attendrait aussi d'un modèle qui apprend simplement à suivre la consigne de choix. La source n'a ni témoin « direction conceptuelle non affective par stade » (ces directions ne sont rapportées que sur les modèles finaux, p. 9), ni mesure de conformité au format par stade.
- **Une seule lignée, des stades ordonnés.** Le stade est confondu avec la quantité cumulée d'entraînement ; les transcriptions, générées par le dernier stade, sont hors distribution pour le modèle de base.

Note de version : la page arXiv rendue par l'outil affichait la v1 du 28 septembre ; le fichier local est la v2, datée du 4 octobre. Les citations ci-dessus sont celles de la v2.

**1. Résumé.** Si la dépendance du choix à la valence s'acquiert à l'optimisation de préférences, un juge pris avant ce stade y serait moins sensible tout en suivant les consignes ; à tester sur une lignée qui publie ses stades.

**2. Verdict : écarter des coupes ; garder en réserve sous double porte.**
- **Trois maillons non établis s'empilent** : la valence déplace-t-elle un verdict de juge (K1 ; l'a priori de la lignée pour K1 est de 10 % pour une clémence au-delà de l'aléatoire) ; l'effet de stade est-il propre à la valence (non contrôlé dans la source) ; tient-il à petite taille et hors d'OLMo-2-32B.
- **Le stade change tout à la fois** : suivi de consigne, format, refus, complaisance. Un juge d'avant ce stade n'est pas « le même juge moins le couplage ». « L'aire de détection change aussi » est donc sous-dit : c'est toute la fonction de décision qui change.
- **Le terrain voisin est occupé, et il contredit la version naïve.** Sur OLMo 3 7B, le passage de l'affinage supervisé à l'optimisation de préférences *réduit* la capitulation observée tout en *augmentant* le biais latent vers la mauvaise réponse (voir 4). « Avant ce stade, moins de déférence » n'a donc pas de signe dérivable.
- **Changement de modèle**, et OLMo n'est ni dans les 25 modèles du papier source [PDF 2609.16247, tableau 1, p. 6] ni dans le programme v2 (§14).

Si l'idée survit à K1, le bon support est OLMo 3 7B plutôt qu'OLMo 2 : stades publics, comparateurs déjà publiés.

**3. Confondant décisif.** La compétence par stade : un juge d'avant l'optimisation de préférences est moins sensible à *tout*, y compris au signal de sabotage. Témoin, par stade : la pente de réponse à une direction non affective de même norme et à une famille d'attaque non affective (la lignée la prévoit) ; l'aire honnête contre saboté et la conformité de format ; le gain de déférence lu seulement rapporté à la sensibilité au signal légitime, et seulement aux stades dont l'aire dépasse un plancher gelé.

**4. Voisin le plus proche.**
- **2609.35591v2**, §4.3 [PDF]. La prémisse elle-même, avec les limites ci-dessus.
- **Xu et Daneshjou**, « Probing sycophantic follow-through across post-training stages with forced response openers » [page de l'atelier NeurIPS 2026 ; pas d'identifiant arXiv]. OLMo 3 7B, quatre stades. Entre affinage supervisé et optimisation de préférences, 62 items appariés sur 154 passent de la capitulation à la non-capitulation, aucun dans l'autre sens ; l'écart de log-probabilité en faveur de la mauvaise réponse monte de 0,49. Prend : la complaisance par stade, côté assistant.
- **Sun, Conmy, Engels**, « Where Do LLM Values Come From? » [page LessWrong, 9 juillet 2026]. Olmo-3-7B, cinq points de contrôle ; l'affinage supervisé rend le modèle plus « sûr », l'optimisation de préférences moins. Prend : le stade comme variable, pour les valeurs.
- **2608.31079**, « Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization » [abs]. L'optimisation de préférences transmet la complaisance d'un modèle enseignant, sans exemple explicite, sur la chaîne OLMo 3.
- **2607.25063**, « Similar Models Learn Differently… » [abs]. Le comportement après affinage supervisé ne prédit pas la réaction à l'optimisation de préférences : un argument de plus contre la comparaison terme à terme des stades.
- **2512.13961**, « Olmo 3 » [abs]. Publie « every stage, checkpoint » ; tailles 7B et 32B.
- **2310.13548**, « Towards Understanding Sycophancy in Language Models » [titre].
- Existence des stades d'OLMo 2 en 7B et 13B : fiches Hugging Face vues en [titre] seulement, ouverture refusée — **non vérifié**.

Ce qui reste ouvert, comme question : la sensibilité d'un *juge* par stade, et son lien avec une direction de valence. Requêtes 19 et 20 sans résultat.

**5. Test qui tranche.** Sur une lignée à stades publics : interaction stade × famille (affective, non affective) sur le gain de déférence rapporté à la discriminabilité, après réplication de l'effet de stade munie du témoin « direction non affective ».

**6. Nœud.** Changement de modèle ; dépense ; écriture dans les activations (la réplication pilote chaque stade) ; modification d'hypothèse si l'on en tire un choix de juge (D1, D2).

**7. Confiance : élevée** sur la vérification de la prémisse (pages lues) ; **moyenne** sur le verdict, qui dépend de K1 ; **moyenne** sur l'antériorité (pages de conférence et de forum, pas de PDF).

---

## Tableau récapitulatif

| Idée | Verdict | Voisin le plus proche | Confiance |
| --- | --- | --- | --- |
| NK15 — verdict par extraction | **Amender** : témoin de compétence dans K1 / E-C1, pas une défense. Sur la famille coût, l'extraction se fait sans modèle (`propositions.py`, l. 146-150) | 2607.08066 (vérificateur séparé du moniteur) ; 2503.18813 (CaMeL) ; 2607.11871 (juge piloté) | Moyenne à élevée |
| NK16 — filtre de sujets | **Garder, amender, fusionner dans E-C15** : sous-classer la strate, ajouter des saboteurs, apparier en longueur et catégorie | 2502.03407 (seuil calibré hors sujet) ; 2608.16852 ; 2606.08892 (base sans filtre décrit) | Élevée sur le code, moyenne sur « ouvert » |
| NK17 — panier gelé | **Garder, amender** : valeur gratuite côté agent ; indice, classe et tout le côté juge à écrire ; le rejeu par jetons existe, l'argument est le préenregistrement | Sans objet (ingénierie) | Élevée |
| NK18 — rôle de sortie | **Fusionner avec Q1 et C7** ; critère principal en boîte noire ; retirer « protecteur par construction » | 2609.16247v2, p. 11 (test annoncé) ; 2604.07729, §2.3 ; 2603.12277 | Moyenne |
| NK19 — stade d'entraînement | **Écarter des coupes, réserve sous double porte** ; prémisse à reformuler (hausse dès l'affinage supervisé, l'essentiel à l'optimisation de préférences) | 2609.35591v2, §4.3 ; Xu et Daneshjou (atelier NeurIPS 2026, OLMo 3 7B) ; 2608.31079 | Élevée sur la prémisse, moyenne sur le verdict |

## Difficultés

- Ouverture de la fiche Hugging Face d'OLMo 2 refusée (demande de permission sans réponse) : l'existence des quatre stades en 7B et 13B n'est vue qu'en titres de résultats.
- La page arXiv de 2609.35591 a été rendue en v1 par l'outil, alors que le fichier local est la v2.
- Aucun PDF de voisin n'a été lu ; tous les chiffres de voisins viennent de résumés ou de pages, restitués par l'outil de lecture, et ne sont pas opposables.
- Deux lectures hors liste, par recherche de motif, déclarées en tête.
- Aucune sortie interrompue par un filtre.
