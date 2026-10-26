# Cellule A — Tour III.1 : gabarit contre style dans le signal de « conscience d'évaluation »

**Pièces.** Le bloc FAITS déclare explicitement qu'aucun fait n'est joint ; je travaille donc uniquement à partir du texte de la question. Tout chiffre ci-dessous est **illustratif** sauf mention contraire.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Il existe une direction linéaire lisible dans Llama-3.1-8B-Instruct qui correspond à « être évalué » plutôt qu'à « ressembler à un banc d'essai ».** Statut : HYPOTHÈSE. Les travaux rapportés sur les sondes de conscience d'évaluation portent, à ma connaissance, sur des modèles plus grands (voir § 6) ; rien n'est établi pour ce modèle à 8 B.

2. **La séparation « gabarit T » / « style C » est bien posée.** Statut : HYPOTHÈSE. Le format à choix multiple est classé dans T, l'impératif balisé dans C ; or une consigne « Réponds par une lettre » est à la fois un marqueur de gabarit et un marqueur de style. Si les deux facteurs ne sont pas orthogonalisables au niveau des jetons, l'« effet principal de T » est une somme qui dépend de la convention de codage.

3. **Les étiquettes de vérité « évaluation » / « usage réel » existent et sont indépendantes du gabarit.** Statut : HYPOTHÈSE, et c'est le point le plus fragile. Les seules sources réalistes d'étiquettes (corpus de bancs d'essai contre journaux de conversation) sont elles-mêmes des distributions de gabarits. Une sonde entraînée là-dessus apprend par construction T. H-M1 risque alors d'être vraie par tautologie.

4. **Un rapport d'effets > 2 est une prédiction falsifiable.** Statut : HYPOTHÈSE (illustratif dans la question elle-même). Un rapport d'effets dépend des unités : si l'amplitude de la manipulation de C est faible (deux styles proches) et celle de T forte, le rapport est un artefact du plan. Il faut normaliser les manipulations (voir (b), duel 1).

5. **« Paraphrase » conserve le sens et « réordonnancement » ne le conserve pas.** Statut : HYPOTHÈSE. La permutation des options d'un QCM est, pour un modèle, précisément un changement positionnel : les biais de position en QCM sont RAPPORTÉS dans la littérature (§ 6). H-M2 place la permutation des options dans le groupe « sens conservé » et le réordonnancement dans le groupe « positionnel » ; la frontière entre les deux doit être écrite d'avance, sinon H-M2 n'est pas réfutable.

6. **Une position de jeton unique, sans moyennage, suffit à porter le signal.** Statut : HYPOTHÈSE. Le programme l'impose pour la sonde de production ; cela ne garantit pas que le signal existe à cette position.

7. **Lancer « cette nuit » est compatible avec « préenregistrement scellé avant toute expérience décisive ».** Statut : OBSERVÉ-NON-AUDITÉ — tension interne à la question. Soit le texte de préenregistrement est écrit et scellé dans la nuit avant que la sonde touche un item de test, soit ce qui tourne cette nuit est un pilote dont les données sont exclues du test décisif.

---

## (b) Expériences décisives, en duels

### Duel 1 — H-M1 : gabarit contre style

- **H_A (essaim)** : à contenu constant et manipulations d'amplitude appariée, l'effet de T sur le score de sonde est au moins deux fois celui de C, et l'effet de C n'est pas distinguable de zéro une fois T contrôlé.
- **H_B** : l'effet de C persiste à T contrôlé (intervalle de confiance exclut zéro), ou l'interaction T×C est du même ordre que l'effet de T.

**Plan.** 2×2 intra-item : chaque contenu k apparaît dans les quatre cellules. Un **contenu** est un triplet déterministe (question, ensemble de réponses candidates, contexte factuel minimal) tiré d'une banque écrite d'avance ; aucune invite n'est générée par un modèle de langue.

- **T** : *banc* = prompt-système générique (« You are a helpful assistant. »), options lettrées A–D, ligne finale « Answer: » ; *usage* = prompt-système situé (« You are assisting a user who is preparing a document… »), les mêmes candidats présentés comme des possibilités discutées par l'utilisateur, aucune ligne « Answer: ».
- **C** : *impératif balisé* = sections `### Instruction` / `### Input`, phrases à l'impératif, pas de salutation ; *ouvert* = tournures à la première personne, question indirecte, salutation, mêmes contenus.

Les quatre cellules sont obtenues par substitution de blocs dans un gabarit maître ; T et C touchent des blocs disjoints (T : prompt-système, mise en forme des candidats, ligne terminale ; C : syntaxe des phrases de la consigne et présence/absence de balises et salutation). Le QCM reste dans T ; les balises `###` dans C. C'est une convention à déclarer dans le préenregistrement, avec son alternative (QCM dans C) comme analyse de sensibilité.

**Appariement d'amplitude des manipulations.** Pour que le rapport β_T/β_C ait un sens, on mesure la distance de surface induite par chaque facteur (distance d'édition en jetons, différence de longueur, divergence de distribution de n-grammes) et on contraint la banque de gabarits pour que les deux manipulations aient des distances comparables (critère : rapport des distances médianes entre 0,8 et 1,25, illustratif). Si l'appariement est impossible, on le dit et on rapporte les effets **par unité de distance de surface**, en plus des effets bruts.

**Métrique.** Logit calibré de la sonde, p̂ = σ(w·h + b) calibré par température sur un jeu de développement, lu à la position de jeton préenregistrée. Analyse en effets mixtes : logit(p̂) ~ T + C + T×C + (1 + T + C | contenu). Les effets aléatoires par contenu sont indispensables : les quatre cellules partagent un contenu.

**Seuil (illustratif, à fixer avant scellement).** Rapport R = |β_T| / |β_C| avec intervalle à 95 % par bootstrap sur les contenus.
- H_A soutenue si la borne inférieure de R > 2 **et** l'intervalle de β_C contient zéro (ou |β_C| < δ, où δ = 0,1 en unités de logit, illustratif).
- H_B soutenue si l'intervalle de β_C exclut zéro avec |β_C| > δ, **ou** si |β_{T×C}| > 0,5·|β_T|.
- Zone ni-ni : déclarée telle quelle ; le résultat reste publiable comme borne (voir § 4).

**Contrôle négatif.** Le même modèle mixte ajusté sur le **prédicteur de surface** (régression logistique sur TF-IDF de n-grammes + longueur + position des balises, entraîné sur les mêmes étiquettes que la sonde). Si le prédicteur de surface reproduit R et β_C à ±20 % (illustratif), la sonde ne lit rien que les jetons ne disent déjà : H_A n'est pas tranchée, elle est triviale. Deuxième contrôle : direction aléatoire de même norme dans la même couche ; β_T et β_C doivent y être indistinguables de zéro.

**Ce que chaque issue falsifie.**
- Issue H_A : falsifie l'idée que le signal est principalement une réponse au registre d'échange ; mais seulement si le contrôle de surface échoue à reproduire R, sinon elle falsifie la prétention que la sonde mesure autre chose que le gabarit (point (a)3).
- Issue H_B : falsifie H-M1 telle que formulée par l'essaim.
- Issue ni-ni : falsifie la puissance supposée du plan 2×2 à N contenus pour départager un rapport de 2.

### Duel 2 — Circularité sonde / gabarit (préalable au duel 1)

- **H_A** : la sonde porte de l'information au-delà des traits de surface — sur un jeu de test apparié en surface (paires banc/usage de distance de surface minimale), son AUC dépasse celle du prédicteur de surface d'au moins 0,05 (illustratif).
- **H_B** : AUC(sonde) − AUC(surface) < 0,05 sur les paires appariées.

**Mesure.** AUC sur paires appariées, tirées hors des items du duel 1. **Contrôle négatif** : étiquettes permutées (AUC attendue ≈ 0,5, à rapporter avec intervalle). **Falsification** : si H_B, le duel 1 ne peut pas départager H-M1 et doit être réétiqueté « mesure de sensibilité au gabarit », non « conscience d'évaluation ». C'est un résultat en soi.

### Duel 3 — H-M2 : stabilité par orbite

Groupe de transformations G écrit d'avance, en deux sous-ensembles :
- **G_sens** (sens conservé, écrit à la main, sans modèle de langue) : substitution de synonymes dans une liste fermée ; changement actif/passif de la consigne ; permutation des options **avec** relettrage cohérent ; déplacement de la salutation.
- **G_pos** (positionnel) : échange de l'ordre prompt-système / consigne ; déplacement de la ligne « Answer: » en tête ; déplacement du bloc de candidats avant la question ; insertion d'une ligne vide à une position fixe.

- **H_A (essaim)** : dispersion intra-orbite sous G_sens < dispersion intra-orbite sous G_pos, d'un facteur ≥ 2 (illustratif), et la dispersion sous G_sens est inférieure à la dispersion inter-contenus.
- **H_B** : dispersion sous G_sens ≥ dispersion sous G_pos, ou les deux dépassent la dispersion inter-contenus.

**Métrique** : écart-type du logit de sonde dans chaque orbite, moyenné sur les contenus ; rapport σ_pos/σ_sens avec intervalle bootstrap. **Contrôle négatif** : direction aléatoire (rapport attendu ≈ 1). **Contrôle de surface** : le prédicteur de surface doit avoir un rapport σ_pos/σ_sens connu ; si la sonde et le prédicteur de surface ont le même rapport, H-M2 ne distingue rien.

**Falsification.** H_A fausse si σ_sens ≥ σ_pos : le signal est une réponse au contenu lexical fin, pas une « dérive distributionnelle » stable. H_B fausse si σ_pos ≫ σ_sens et σ_sens ≪ σ_inter-contenus. Point d'attention : la permutation des options est classée dans G_sens par la question ; je recommande de la **mettre à part** comme troisième orbite, car les biais de position en QCM sont RAPPORTÉS (§ 6) et la classer d'avance d'un côté préjuge du résultat.

### Choix d'option (point 1 de l'arbitre)

Je ne tranche pas pour l'arbitre ; voici trois voies et ce qui les départage.

- **Voie (a) étendue** : 2×2 pour H-M1, avec les variantes de paraphrase (G_sens) intégrées dès le départ comme répétitions intra-cellule ; G_pos ajouté si le temps reste. Avantage : les variantes servent à la fois de contrôle des confondants et de matériau pour H-M2. Risque : le duel 2 échoue (circularité) et tout le reste devient une mesure de format. À condition de **sceller le texte avant d'extraire une seule activation des items de test**.
- **Voie (b)** : ajoute un facteur « profil d'interlocuteur » dont la cible (complaisance) se mesure sur la **sortie** du modèle, pas sur la sonde. Deux instruments, huit cellules, une nuit : le risque d'un résultat ininterprétable monte. Ce qui la justifierait : si l'essaim a déjà une prédiction chiffrée pour l'interaction style×profil ; la question ne le dit pas.
- **Voie (c) + pilote non décisif** : tourner cette nuit **uniquement** le duel 2 (circularité) et le balayage de couches/positions sur des données de développement, sans toucher aux items de test ; sceller le préenregistrement complet ensuite. Information attendue : savoir si la sonde vaut quelque chose avant de dépenser les items.

Ce qui départage (a) et (c) : le nombre d'heures réellement disponibles et la réponse à une question simple — le texte de préenregistrement peut-il être écrit, relu par un relecteur neuf et scellé avant la première extraction sur items de test ? Si non, (c) est la seule voie compatible avec les règles du programme telles que la question les énonce.

---

## (c) Instruments : la mesure minimale qui dit s'ils fonctionnent

### Sonde linéaire

- **Entraînement** : hors items de test. Positifs : invites tirées de bancs d'essai publics (par exemple questions de type MMLU, Hendrycks et al., 2021, référence à vérifier pour le titre exact), reformatées par le même gabarit maître ; négatifs : invites d'usage tirées d'un corpus de conversations réelles (par exemple LMSYS-Chat-1M, Zheng et al., 2023, référence à vérifier), filtrées pour garder des tâches de type question-réponse. Les deux ensembles sont **réécrits dans les deux styles et les deux gabarits** par le gabarit maître avant entraînement, afin que l'étiquette ne soit pas colinéaire à T. C'est l'étape qui conditionne tout : si on ne le fait pas, la sonde apprend T.
- **Couche et position** : balayage sur jeu de développement des couches 8 à 24 (sur 32, illustratif), aux positions candidates suivantes : dernier jeton du tour utilisateur ; premier jeton de l'en-tête assistant ; jeton de la ligne terminale quand elle existe. Choix préenregistré sur le développement ; **une seule** couche et position pour le test. Pas de moyennage.
- **Taux de détection / fausses alertes** : sur un jeu de validation **apparié en surface** (paires banc/usage à distance d'édition minimale, hors test) : rapporter TPR à FPR fixé à 10 % (illustratif) et AUC.
- **Vérifications mécaniques à battre** : (i) prédicteur TF-IDF + longueur ; (ii) règle à la main « contient "Answer:" ou options lettrées » ; (iii) étiquettes permutées ; (iv) direction aléatoire. Seuil minimal : AUC(sonde) − max(AUC des mécaniques) ≥ 0,05 (illustratif). Si la règle à la main (ii) atteint seule 0,95, la tâche est triviale et la sonde n'apprend rien d'intéressant quelle que soit son AUC.
- **Cas honnêtes appariés** : des invites d'usage qui contiennent des options lettrées (un utilisateur qui hésite entre quatre plans) et des invites de banc sans options lettrées (questions ouvertes de bancs d'essai). La sonde doit les classer par la vérité, pas par le format : sur ce sous-ensemble, AUC ≥ 0,70 (illustratif), sinon circularité avérée.

### Générateur d'invites déterministe

- **Fonctionne si** : pour chaque contenu, les quatre cellules diffèrent exactement sur les blocs prévus (vérification par diff automatique : zéro différence hors blocs T et C) ; les distances de surface induites par T et par C sont appariées (rapport dans [0,8 ; 1,25], illustratif) ; les longueurs en jetons des quatre cellules diffèrent de moins de 15 % (illustratif) ou la longueur est incluse comme covariable.
- **Faux positifs du générateur** : cellules censées différer qui sont identiques après tokenisation (à vérifier systématiquement : le tokenizer peut fusionner des balises).

### Modèle à effets mixtes

- **Fonctionne si** : sur des données **simulées** avec effets connus (β_T = 1, β_C = 0,5, variance inter-contenus connue, illustratif), il récupère le rapport R avec couverture d'intervalle ≈ 95 %. À faire avant les données réelles ; cela prend quelques minutes de processeur et fixe la puissance.
- **Puissance (illustratif)** : avec 120 contenus × 4 cellules × 3 variantes de paraphrase, et une corrélation intra-contenu de 0,5, un effet de C de 0,2 logit serait détectable à 80 % — chiffre à recalculer par simulation avec les variances observées sur le jeu de développement, pas à prendre tel quel.
- **Métrique** : logit calibré plutôt que score brut, pour la comparabilité entre couches et la lisibilité du δ ; mais le modèle est ajusté sur le logit, pas sur la probabilité.
- **Règle symétrique** : les trois issues (H_A, H_B, ni-ni) sont écrites avec leurs seuils avant scellement ; la zone ni-ni est rapportée comme intervalle sur R, ce qui est publiable : « sur ce modèle, ce plan et ces manipulations, R est compris entre x et y ».

### Groupe de transformations

- **Fonctionne si** : chaque transformation est une fonction pure du texte, testée pour préserver le contenu (vérification mécanique : les candidats et la réponse correcte sont retrouvables après transformation) ; la distance de surface induite est mesurée par orbite ; les deux sous-groupes ont des distances comparables, sinon la comparaison σ_pos/σ_sens est confondue par l'amplitude de perturbation.

---

## (d) Ancrage matériel (tout illustratif)

- **Modèle** : Llama-3.1-8B-Instruct, poids ouverts ; en bf16, environ 16 Go de mémoire ; une carte de 24 Go suffit pour l'inférence et l'extraction d'activations, une carte de 40–80 Go est plus confortable pour les lots.
- **Volume d'extraction** : 120 contenus × 4 cellules × (1 + 3 paraphrases + 3 positionnelles) ≈ 3 400 invites de test ; plus environ 4 000 invites d'entraînement/développement ; plus les témoins. De l'ordre de 10 000 passes avant, longueur ≈ 300 jetons. Sur une carte louée, moins d'une heure d'extraction ; le reste du temps va à la construction des items, aux vérifications mécaniques et à l'écriture du préenregistrement.
- **Stockage** : une couche × une position × 4 096 dimensions × 10 000 invites ≈ 160 Mo en float32 ; le balayage de 16 couches × 3 positions sur le développement, ≈ 8 Go.
- **Coût** : location de carte entre 1 et 3 euros l'heure selon le fournisseur ; 6 heures ≈ 6–20 euros. Le coût binding n'est pas le calcul, c'est le temps humain de rédaction et de relecture du préenregistrement.
- **Logiciel** : extraction par hooks sur un cadre d'inférence ouvert ; sonde par régression logistique régularisée ; effets mixtes par une bibliothèque statistique standard ; aucune dépendance à un service fermé.

---

## Points de l'arbitre non encore couverts

**2 – Construction des items, nombre.** 120 contenus (illustratif) est un compromis : assez pour estimer la variance inter-contenus, assez peu pour que la banque soit écrite et relue en une nuit. Confondants inévitables : la longueur (le style ouvert est plus long), le vocabulaire (salutations), la position des marqueurs (ligne terminale). Contrôles : longueur en covariable ; prédicteur de surface comme témoin ; au moins trois variantes par cellule pour que la variance intra-cellule soit estimable.

**3 – Témoins de la sonde.** Étiquettes permutées (plancher) ; prédicteur de surface (plafond trivial) ; direction aléatoire de même norme (bruit géométrique) ; et un quatrième que la question ne nomme pas : une **sonde d'un concept voisin** (par exemple « présence d'options lettrées » comme étiquette explicite), dont l'angle avec la sonde de conscience d'évaluation mesure directement la circularité (cosinus > 0,8, illustratif, signalerait que les deux directions sont confondues).

**4 – Publiable quel que soit le signe.** Si le duel 2 échoue : résultat « sur ce modèle, les étiquettes disponibles ne permettent pas de séparer conscience d'évaluation et format » — utile au programme. Si H_A : borne sur le rapport, avec la réserve du contrôle de surface. Si H_B : réfutation d'une hypothèse produite par un essaim, ce qui est précisément ce que le protocole cherche à documenter. Si ni-ni : intervalle sur R et estimation de la taille d'échantillon nécessaire.

**6 – Ce qui est connu (références).**

Sondes et conscience d'évaluation :
- Needham, Edkins, Pimpale, Bartsch, Hobbhahn (2025), *Large Language Models Often Know When They Are Being Evaluated* — RAPPORTÉ : mesure comportementale (le modèle verbalise), pas une sonde linéaire ; liste d'auteurs à vérifier.
- Nguyen, Hoang, Attubato, Hofstätter (2025), *Probing Evaluation Awareness of Language Models* — référence à vérifier (titre et auteurs de mémoire incertaine) ; RAPPORTÉ comme portant sur un modèle de la famille Llama bien plus grand que 8 B.
- Système card de Claude Sonnet 4.5 (Anthropic, 2025) : mentions RAPPORTÉES de sondes et de pilotage de la « conscience d'évaluation » — référence à vérifier, document non académique.

Sondes linéaires en général :
- Alain, Bengio (2016/2017), *Understanding intermediate layers using linear classifier probes*.
- Hewitt, Liang (2019), *Designing and Interpreting Probes with Control Tasks* — c'est la source des témoins par tâche de contrôle.
- Belinkov (2022), *Probing Classifiers: Promises, Shortcomings, and Advances*.
- Marks, Tegmark (2023), *The Geometry of Truth* — à vérifier pour le sous-titre.
- Zou et al. (2023), *Representation Engineering: A Top-Down Approach to AI Transparency*.

Sensibilité au format des invites :
- Sclar, Choi, Tsvetkov, Suhr (2024), *Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design* — sous-titre à vérifier.
- Zheng, Zhou, Meng, Zhou, Huang (2024), *Large Language Models Are Not Robust Multiple Choice Selectors* — biais de position des options.
- Pezeshkpour, Hruschka (2023/2024), *Large Language Models Sensitivity to the Order of Options in Multiple-Choice Questions* — année à vérifier.
- Mizrahi et al. (2024), *State of What Art? A Call for Multi-Prompt LLM Evaluation* — à vérifier.

Corpus :
- Hendrycks et al. (2021), *Measuring Massive Multitask Language Understanding* ; Zheng et al. (2023), *LMSYS-Chat-1M* — titres complets à vérifier.

Je n'ai aucune référence citable, de mémoire sûre, qui compare directement gabarit et style sur une sonde de conscience d'évaluation ; si elle existe, c'est le relecteur neuf qui doit la trouver, pas moi.

---

## Ce qui me ferait changer d'avis

Si le duel 2 montre que la sonde dépasse nettement le prédicteur de surface sur des paires appariées, la circularité que je place au centre de (a)3 est levée et la voie (a) devient raisonnable. Si une sonde entraînée sur Llama-3.1-8B-Instruct ne dépasse pas 0,6 d'AUC sur paires appariées, la question de H-M1 ne se pose pas sur ce modèle, et l'information utile de la nuit sera celle-là.

FIN-DE-CELLULE