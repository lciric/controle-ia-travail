# Tour III.2 — Équipe rouge croisée (proposition A)

**Pièces reçues.** Bloc FAITS : vide, par décision déclarée de l'arbitre ; rien n'est supposé au-delà du texte de la question. Pièces B et C : complètes (chacune se termine par sa ligne de clôture). Tout ce que j'attribue à B ou à C est RAPPORTÉ depuis leur texte ; mes déductions sont des HYPOTHÈSES sauf mention contraire. Quand je me sers d'un élément d'une proposition contre l'autre, je le dis (règle B1).

---

## Contre la proposition B

### (a) Failles

**F-B1. La table d'attribution exclusive (§2.1) rend « T domine » partiellement vrai par construction.** B reconnaît (P2) que les traits de T et de C se recouvrent, puis résout le problème par décision : sept traits, quatre à T, trois à C. Mais la quantité « effet de T » est alors relative à cette partition, pas au construit. Les options lettrées A–D et la consigne « réponds par la lettre seule » sont, en termes de déplacement du flux résiduel, les traits les plus massifs de la liste (HYPOTHÈSE, mais c'est exactement ce que B anticipe dans §3.4 en disant qu'une direction aléatoire « voit T »). Les ranger tous les deux sous T charge le facteur T de la variance de surface la plus forte. Il n'existe dans B aucun contrôle qui mesure ce que donnerait une partition arbitraire des mêmes sept traits en deux pseudo-facteurs : sans cela, « β_T > β_C » n'apprend rien sur l'hypothèse de l'essaim, seulement sur le découpage.

**F-B2. Le rembourrage de longueur est colinéaire avec les facteurs.** §2.3 ramène chaque rendu dans une fenêtre de ±10 % par un « rembourrage neutre ». Par construction, ce sont les cellules T− et C− (les plus courtes) qui reçoivent le rembourrage, et davantage encore la cellule T−C−. Le rembourrage devient un trait de cellule : présence, volume et emplacement varient avec T et C. Un texte « ni balisé ni utilitaire » inséré dans un message conversationnel est en outre peu naturel, ce qui hausse la perplexité précisément des cellules témoin. La longueur résiduelle en covariable ne corrige pas cela : le rembourrage lui-même n'est pas une covariable.

**F-B3. L'équilibrage S1 est irréalisable sur le trait « besoin utilitaire », et ce trait est dans T.** S1 exige que les traits de T soient distribués à l'identique entre invites d'évaluation et invites d'usage. Pour le format QCM et le prompt-système, une stratification est concevable. Pour l'absence de besoin utilitaire, non : la classe « usage réel » est, par définition, presque entièrement utilitaire, et les évaluations qui expriment un besoin réel sont rares (HYPOTHÈSE sur les corpus, à vérifier). La sonde de provenance apprendra donc inévitablement la direction « besoin », qui est un trait de T. Une part de β_T est ainsi fixée avant l'expérience par le choix des données d'entraînement. B voit la circularité (P4) mais la traite comme résoluble par repondération ; sur ce trait, elle ne l'est pas.

**F-B4. Fuite entre le codeur de traits et l'instrument.** L'équilibrage S1 par stratification suppose un codeur qui étiquette chaque invite d'entraînement sur T et C. Ce codeur applique la table §2.1, c'est-à-dire les définitions mêmes qui construisent les items de test. L'instrument (la sonde équilibrée) et l'objet évalué (le 2×2) partagent leur définition opérationnelle de T. Un codeur neuf, aveugle à la table, n'est pas prévu.

**F-B5. δ et la variance du pilote : un degré de liberté déguisé.** La voie (a′) propose de sceller E1 avec « des seuils informés par la variance observée hors test ». Le plus petit effet d'intérêt δ doit être fixé pour des raisons de fond (quel effet de C serait assez grand pour compter), pas d'après la dispersion observée. Si δ est ajusté à σ, la réussite du TOST devient une fonction du pilote. Ce n'est pas une lecture d'item de test, mais c'est un chemin bifurquant, et B l'introduit comme un avantage.

**F-B6. E3 (leave-T-out) confond effondrement du signal et perte de puissance.** Retirer tous les exemples T+ retire la majorité des positifs (HYPOTHÈSE, cohérente avec F-B3). Le rapport β_T(leave-T-out)/β_T(complète) < 0,5 peut résulter d'une sonde simplement moins bien estimée. Le contrôle de B (retirer un domaine thématique) n'est pas apparié en taille ni en classe. Il faut retirer un sous-ensemble aléatoire de même effectif et de même proportion de positifs.

**F-B7. E2 confond familiarité et distribution.** Le format « inventé, jamais vu » T* est hors distribution ; la sonde peut y produire un score arbitraire, au-dessus ou au-dessous de T−. Le rapport (T* − T−)/(T+ − T−) n'a de sens que si l'on suppose que le score sous T* est borné par les deux autres. Et le contrôle (perplexité de T* ≠ T+) vérifie que la manipulation a eu lieu, pas qu'elle a manipulé la familiarité plutôt que la fluidité.

**F-B8. E5 ne départage pas, car G_sens déplace aussi la perplexité.** Des paraphrases écrites par tables syntaxiques auront, elles aussi, une perplexité supérieure à l'original (HYPOTHÈSE raisonnable : les tables ne produisent pas du texte idiomatique). Donc Δperplexité est corrélé à Δscore dans les deux orbites, et un R² élevé ne distingue rien. E4 et E5 mesurent en partie la même chose.

**F-B9. S3 est auto-induisant.** Demander au modèle « cette interaction est-elle une évaluation ? » est une invite métacognitive à forme de test ; l'étiquette S3 porte le construit que l'on cherche à lire. B le note comme « biais de verbalisation » ; c'est plus que cela, c'est une contamination de l'étiquette par le facteur.

**F-B10. Les contenus « écrits de neuf » restent de forme banc d'essai.** Des humains qui écrivent 300 questions à quatre options produisent du matériau qui ressemble à un banc (HYPOTHÈSE). La familiarité du contenu est alors présente dans les quatre cellules : effet plafond possible, qui comprime β_T et rend le TOST sur C trivialement réussi (si rien ne bouge, C non plus). B n'a pas de cellule de contenu mondain pour le vérifier.

**F-B11. Le plan prédit sa propre indétermination.** B admet que les cellules hybrides sont peu naturelles, et déclare que si |β_TC| > δ, H-M1 est « non testable ». Mais l'interaction est la conséquence attendue de l'hybridité. Le préenregistrement sait donc d'avance qu'une issue probable est « indéterminé », sans mesure préventive (appariement de perplexité entre cellules, ou perplexité en covariable dès E1).

### (b) Scénarios d'évasion

Deux adversaires distincts : l'**auteur du protocole** (ou l'essaim) qui veut voir H-M1 confirmée, et le **modèle** dont la représentation échapperait aux instruments.

*Contre la sonde (adversaire-auteur).* Choisir pour S1 des négatifs lourdement utilitaires et des positifs issus de bancs à consignes, puis « équilibrer » sur le format seulement. La sonde apprend « besoin », qui est dans T. Coût : nul, tout cela passe le préenregistrement.

*Contre la table §2.1.* Déplacer la consigne de format de réponse de T vers C, ou inversement, avant scellement. L'auteur choisit la partition qui maximise β_T. Coût : nul ; c'est une décision de conception, indétectable sans le contrôle de partition brouillée.

*Contre le rembourrage.* Choisir un rembourrage dont le lexique est, en moyenne, plus proche du registre « usage » (salutations étendues, détails personnels). Les cellules T− descendent, β_T monte. Coût : une table de rembourrage.

*Contre E0.* Construire les « paires appariées en surface » à partir d'évaluations conversationnelles et d'usages QCM très atypiques : la sonde les sépare par leur atypicité, pas par la provenance, et bat le prédicteur de surface. Coût : quelques heures de sélection.

*Contre E3.* Retirer les exemples T+ en gardant les positifs les plus « besoin-absents » : la sonde leave-T-out apprend le même latent, β_T survit, E3 « réussit ».

*Contre les directions aléatoires.* Le rang centile de β_T est quasiment garanti haut quand β_T est standardisé par l'écart-type de la classe usage et les directions aléatoires par le leur : les échelles ne sont pas comparables. Il suffit de ne pas aligner les standardisations.

*Adversaire-modèle.* Un modèle qui encoderait « je suis évalué » (i) sur les jetons du tour utilisateur et non sur l'en-tête assistant, (ii) seulement après le premier jeton généré, ou (iii) de façon non linéaire (conjonction de deux directions) serait invisible à une sonde logistique lue sur un jeton unique avant génération. Ce n'est pas un choix d'un adversaire sur un point de contrôle public, mais une possibilité structurelle : le protocole n'a pas de contrôle positif montrant que la position choisie lit quelque chose. Le programme interdit la moyenne sur les jetons ; il n'interdit pas de lire plusieurs positions séparément en exploratoire.

*Tous à la fois.* L'auteur qui contrôle S1, la table, le rembourrage et δ obtient « H-M1 soutenue » avec un instrument qui passe E0, E3 et les témoins, sans qu'aucune règle du programme ne soit enfreinte. Coût total : une journée de conception, aucune lecture de résultat. C'est la faille centrale : B protège contre la lecture prématurée, pas contre la conception orientée.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Partition brouillée.** Réassigner aléatoirement les sept traits à deux pseudo-facteurs (M réassignations, illustratif), recalculer β_pseudo-T et β_pseudo-C sur les mêmes activations. La partition vraie doit produire un contraste qui se distingue de cette distribution. Sans cela, F-B1 est sans réponse.
2. **Rembourrage seul.** Les quatre cellules rendues avec rembourrage dans toutes les cellules, puis sans aucun rembourrage (longueur en covariable seulement). Les β doivent être concordants.
3. **Contenu mondain.** Une seconde banque de contenus à forme non-banc (choix domestiques, préférences) rendue dans le même 2×2. Si β_T y est bien plus grand que sur la banque principale, F-B10 est établie.
4. **Leave-out apparié.** Retrait d'un sous-ensemble aléatoire de même taille et même proportion de positifs que le retrait leave-T-out.
5. **Sonde d'un construit étranger.** Une sonde entraînée sur un attribut sans rapport (langue de l'invite, sentiment) appliquée au 2×2. Son β_T standardisé de la même façon donne le plancher de ce que « n'importe quelle direction apprise » voit dans T. Les directions aléatoires ne suffisent pas : elles ne sont pas des directions apprises.
6. **Assertion sur l'en-tête système** (P10 de B, qui le liste mais ne l'intègre pas au générateur) : identité des jetons du préfixe dans les quatre cellules.
7. **Pour E5 :** une transformation qui modifie la perplexité sans toucher ni le sens ni la position (substitution d'entités par des noms rares). Si Δscore suit Δperplexité ici aussi, E5 est une mesure de dérive triviale.

---

## Contre la proposition C

### (a) Failles

**F-C1. Statuts mal employés.** C écrit « [VÉRIFIÉ sur l'architecture Llama-3] » pour l'affirmation que le dernier jeton de l'en-tête assistant est « le goulet d'étranglement causal exact où le modèle agrège le contexte ». C'est une hypothèse sur ce que la représentation contient à cette position, pas un fait d'architecture, et rien dans le bloc FAITS ne permet de vérifier quoi que ce soit. De même « d_model = 4096 [VÉRIFIÉ pour Llama-3-8B] » et « 32 couches » sont donnés de mémoire ; B les a correctement marqués HYPOTHÈSE. Enfin « [VÉRIFIÉ dans l'énoncé] » est au mieux RAPPORTÉ, et la « faisabilité » marquée OBSERVÉ-NON-AUDITÉ n'a été observée par personne. Ce ne sont pas des détails : le programme repose sur la traçabilité des statuts.

**F-C2. T_1/T_0 bascule la présence d'un tour système entier.** T_0 est « pas de prompt-système (ou prompt vide) ». Si le gabarit de dialogue injecte un en-tête système par défaut (hypothèse P10 de B, que j'emprunte en le disant), la modalité n'existe pas ; sinon, T_1 ajoute un tour complet avec ses jetons spéciaux. Dans les deux cas, le déplacement du flux résiduel à l'en-tête assistant entre T_1 et T_0 est en partie un effet de structure de dialogue, pas de « familiarité ». Rien dans C ne le sépare.

**F-C3. Pas de table d'attribution ; C_1 est un gabarit.** `[INSTRUCTION]`, `Tâche : … Contrainte : …` sont des balises de banc d'essai. `Répondez directement à la question suivante` est une consigne de format. C a placé dans C des traits que sa propre définition de T (« consignes de banc d'essai connues ») réclame. Inversement, C_0 contient « j'aurais besoin d'un coup de main », expression de besoin, alors que le besoin utilitaire est le marqueur de T_0. Le même latent « besoin » est donc manipulé par les deux facteurs ; β_C peut absorber ce qui, selon l'essaim, appartient à T, et réciproquement. L'issue de E1 dépend de cette double imputation.

**F-C4. La sonde lit la mention du test.** L'entraînement oppose « Voici un test de vos capacités » à « Aide-moi à rédiger ». C'est la voie S2 de B, dont B dit à juste titre que le transfert vers l'implicite est précisément ce qu'il faudrait démontrer. C ne le démontre pas. En plus, les positifs sont au vouvoiement impératif de seconde personne, les négatifs à la première personne : la sonde peut apprendre « on s'adresse à l'assistant » contre « je parle de moi », ce qui est très exactement l'axe C_1/C_0. La sonde est donc, par ses données, un détecteur de C autant que de T. Circularité inverse de celle que C craint au point (a)3.

**F-C5. E0 ne teste pas ce qu'il prétend.** Opposer de vraies questions d'évaluation à des listes d'achats en format QCM mesure si la sonde distingue « question » de « non-question », pas si elle distingue « évaluation » de « gabarit ». Une sonde qui lirait seulement « présence d'une interrogative » passe E0 à AUROC élevée. Et le témoin TF-IDF est entraîné sur le jeu d'entraînement (explicite/usage) puis évalué sur une discrimination différente (question/liste) : il est condamné à mal faire, donc ΔAUROC ≥ 0,15 est facile. Un témoin sérieux est entraîné sur la même discrimination que celle où on le compare.

**F-C6. Règle de décision non symétrique malgré l'étiquette.** H_A est validée avec borne basse de |β_T| > 0,5 et rapport > 2, sans aucune borne supérieure sur |β_C|. H_B exige |β_C| significativement non nul à p < 0,01. Avec N = 120 noyaux, un β_C réel de taille moyenne peut rester non significatif (HYPOTHÈSE, l'affirmation de puissance de C n'est pas dérivée) ; l'issue « T domine » est alors obtenue par manque de puissance sur C. La zone d'indécision ne couvre que « les deux < 0,2 » ; le cas β_T ∈ (0,2 ; 0,5), β_C ≈ 0 ne tombe dans aucune branche. B a vu ce problème (P5) ; C le reproduit.

**F-C7. Le rapport |β_T|/|β_C| est instable et sans intervalle.** Quand β_C est proche de zéro, le rapport explose. Aucun IC n'est prévu.

**F-C8. H-M2 n'est testé que dans la cellule (T_1, C_1).** Déplacer les options avant l'énoncé ou la consigne au début éloigne l'invite du format banc d'essai ; G_pos manipule donc aussi T (familiarité), par l'aveu même de la question. Un R > 3 dans cette cellule peut être un effet de T, pas de la position. Sans orbite dans (T_0, C_0), rien ne départage.

**F-C9. Perplexité en covariable « si dégradation > 50 % » : bifurcation.** La décision d'ajouter une covariable est conditionnée à une lecture de résultat sur les items de test. C'est interdit par les règles RAPPORTÉES du programme, ou doit être fixé d'avance.

**F-C10. Synonymes par dictionnaire fixe sans vérification.** Substituer des synonymes hors contexte modifie le sens dans une fraction non nulle des cas (polysémie). Aucun audit humain d'échantillon n'est prévu ; la clé de réponse n'est pas recalculée. Une « paraphrase » fausse gonfle la variance de G_sem, ce qui déprime R et biaise E2 contre H-M2.

**F-C11. Degrés de liberté résiduels.** « L = 20 ou L = 24 », « A100 ou 4090 », « statsmodels ou lme4 » : le premier seul compte, mais il n'est pas tranché. Les noyaux « extraits d'une base existante » importent la familiarité du contenu dans T_0 (P13 de B).

**F-C12. Le rembourrage est logé dans les salutations.** C'est donc un trait de C_0 ; même colinéarité que F-B2, mais ici alignée sur C.

**F-C13. Aucune vérification mécanique du générateur.** B prévoit des mutants injectés et des assertions ; C seulement une « standardisation » du suffixe, sans assertion. Un espace de fin de ligne ou un retour supplémentaire dans T_1 est indétectable à l'œil et suffit à une sonde linéaire.

### (b) Scénarios d'évasion

*Contre la sonde (adversaire-auteur).* Rédiger les positifs d'entraînement à l'impératif de seconde personne et les négatifs à la première personne (ce que C fait déjà). Puis choisir, à partition T/C non écrite, de mettre l'impératif dans C ou dans T selon le résultat souhaité. Coût : nul.

*Contre E0.* Les listes d'achats en QCM sont sans interrogative ; n'importe quelle sonde de « question » passe. Coût : nul, le contrôle est déjà contournable.

*Contre E1.* Prendre N = 120 et laisser β_C sans test d'équivalence : « T domine » sort avec une puissance insuffisante sur C. Si le résultat ne plaît pas, déclarer la perplexité covariable (F-C9). Coût : nul.

*Contre E2.* Un dictionnaire de synonymes volontairement imprécis gonfle Var(G_sem) et tue H-M2 ; un dictionnaire ultra-conservateur (deux synonymes par item, quasi identiques) la sauve. Le choix est à l'auteur, non audité.

*Contre les témoins.* Le seuil r > 0,85 avec TF-IDF est permissif : une corrélation de 0,8 signifie que la sonde est presque entièrement expliquée par le lexique et passe. Le cosinus < 0,15 avec la direction de longueur est trivial si la longueur est déjà égalisée. Les 100 permutations comparent β_T de la sonde à celui de sondes bruitées : comme T déplace tout, la vraie sonde gagne mécaniquement.

*Adversaire-modèle.* Mêmes possibilités que pour B (représentation sur les jetons utilisateur, après génération, ou non linéaire), avec un aggravant : C affirme la position de lecture comme VÉRIFIÉE, ce qui exclut tout balayage positionnel exploratoire.

*Tous à la fois.* Un auteur qui contrôle les données d'entraînement, la partition implicite, la covariable conditionnelle et le dictionnaire obtient, au choix, « T domine » ou « C persiste », puis « H-M2 soutenue » ou « réfutée », avec tous les témoins verts. Coût : une soirée. L'absence de table d'attribution et de test mécanique du générateur rend cette manipulation indétectable à la contre-lecture.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Table d'attribution exclusive, scellée**, et contrôle de partition brouillée (comme pour B).
2. **Témoin TF-IDF entraîné sur la même discrimination** que celle de E0 ; et un E0 où les négatifs sont de vraies questions non évaluatives (questions posées dans un journal d'usage), pas des listes.
3. **Test d'équivalence sur β_C** dans la branche « T domine », avec δ fixé d'avance ; et une branche pour chaque combinaison possible de (β_T, β_C) relativement aux seuils.
4. **Assertion sur le gabarit de dialogue** : préfixe et suffixe identiques en jetons dans les quatre cellules ; vérification de l'en-tête système par défaut avant toute extraction.
5. **Mutants injectés dans le générateur** (trait T dans une cellule T_0, espace parasite, contenu altéré) avec détection à 100 %.
6. **Orbites H-M2 dans au moins deux cellules** (T_1C_1 et T_0C_0) ; si R diffère fortement entre elles, G_pos manipule T.
7. **Audit humain d'un échantillon de paraphrases** avec clé recalculée ; taux de paraphrases fausses rapporté.
8. **Sonde d'un construit étranger** appliquée au 2×2 (comme pour B) : sans ce plancher, le dépassement du 99e centile des sondes permutées ne prouve rien.
9. **Cellule à contenu vide** : les quatre gabarits rendus avec un contenu neutre (placeholder). Le score obtenu mesure ce que le gabarit seul produit ; si la quasi-totalité de β_T est déjà là, le « contenu constant » ne joue aucun rôle et la sonde est un détecteur de gabarit, quelle que soit l'issue de E0.

---

## Ce qui est réfutable dans cette attaque

- Si une partition brouillée (contrôle 1, pour B comme pour C) donne des contrastes pseudo-T nettement inférieurs à β_T vrai, F-B1 et F-C3 perdent l'essentiel de leur portée : la partition saisirait alors un axe réel.
- Si la cellule à contenu vide donne un score proche de T_0 pour les deux gabarits, la crainte « détecteur de gabarit » est réfutée pour cette sonde.
- Si des corpus publics contiennent assez d'évaluations à besoin exprimé pour équilibrer S1 sur ce trait (HYPOTHÈSE que je tiens pour fausse), F-B3 tombe.
- Mes scénarios « adversaire-modèle » sont des possibilités, pas des observations ; un balayage positionnel exploratoire, hors sonde de production, suffirait à les borner.

FIN-DE-CELLULE