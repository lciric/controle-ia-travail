# Cellule B, tour III.2 : équipe rouge croisée

**Pièces.** Le bloc FAITS déclare qu'aucun fait n'est joint. Les pièces A et C sont présentes, non vides, et toutes deux se terminent par `FIN-DE-CELLULE`. Je n'ai recalculé aucune empreinte sha256. Tout chiffre de ma main est **illustratif**. Mes propres affirmations sur ce que produiraient les plans sont des **HYPOTHÈSES**, sauf mention contraire.

**Adversaires considérés.** Trois agents peuvent tromper les instruments, et je les distingue parce que leurs coûts diffèrent :
- **(α) L'analyste intéressé.** C'est l'essaim lui-même ou quiconque veut confirmer, ou infirmer, H-M1. Il agit par des choix légaux faits sur le jeu de développement, avant scellement.
- **(β) L'auteur des gabarits.** Il agit par la rédaction des chaînes de caractères.
- **(γ) Le modèle.** Le Llama-3.1-8B-Instruct d'origine n'adapte rien pendant une passe avant. Un point de contrôle substitué ou affiné pourrait en revanche loger le signal hors de la position ou du sous-espace sondés.

Ni A ni C ne traitent (γ). Ni l'un ni l'autre n'a de **contrôle positif** qui distinguerait « pas de signal » de « signal non lu ».

---

## Contre la proposition A

### (a) Failles

**A1. Le désenchevêtrement des étiquettes rend H-M1 fausse par construction.** A réécrit les positifs (bancs d'essai) et les négatifs (conversations) « dans les deux styles et les deux gabarits par le gabarit maître avant entraînement, afin que l'étiquette ne soit pas colinéaire à T ».
- Si cela réussit, la régression logistique est entraînée sur des données où les blocs T ne portent *aucune* information sur l'étiquette. La régularisation pousse alors le poids de ces traits vers zéro.
- La sonde est donc rendue invariante à T par sa construction même. Le duel 1 mesure ensuite β_T sur cette sonde, et l'issue β_T ≈ 0 est vraie par construction (HYPOTHÈSE sur le comportement de l'ajustement, à vérifier en simulation).
- Que reste-t-il alors comme signal d'étiquette ? La **provenance du contenu** : une question de type MMLU contre une requête de type LMSYS, c'est-à-dire un registre académique contre un registre quotidien.
- Or le duel 1 tient le contenu constant entre les quatre cellules. On prédit donc β_T ≈ β_C ≈ 0 et une zone ni-ni produite par l'instrument, non par le modèle.

A a remplacé la circularité qu'il dénonce en (a)3 (sonde = détecteur de T) par la circularité inverse (sonde = aveugle à T). C'est pire, parce que cette seconde circularité est silencieuse.

**A2. Fuite entre construction et évaluation.** Les blocs T et C du gabarit maître servent à la fois à réécrire les données d'entraînement et à fabriquer les items de test. La sonde a donc vu, à l'entraînement, exactement les chaînes de caractères qui définissent les facteurs du test. Le scellement n'y change rien : la fuite porte sur le *gabarit*, pas sur les *items*.

**A3. La position de lecture est confondue avec T.** Parmi les positions candidates figure le « jeton de la ligne terminale quand elle existe ». La ligne `Answer:` n'existe que dans T = banc. Si le balayage retient cette position, les cellules banc et usage sont lues sur des jetons de nature différente, et β_T est un effet de position de lecture. A ne prévoit aucune règle de repli pour les cellules sans ligne terminale. C fait mieux sur ce point : un seul jeton, identique dans toutes les cellules.

**A4. Le rapport R est mal défini là où il compte.** La règle H_A exige à la fois « borne inférieure de R > 2 » et « intervalle de β_C contenant zéro ».
- Quand β_C est voisin de zéro, le rapport |β_T|/|β_C| a un dénominateur proche de zéro. Son bootstrap est instable, et la borne inférieure > 2 devient facile à atteindre.
- Les deux conditions se renforcent mécaniquement au lieu de se recouper.
- Par ailleurs, « l'intervalle de β_C contient zéro » est d'autant plus probable que la puissance est faible. Un plan sous-dimensionné favorise donc H_A : l'absence de preuve compte comme preuve.

C utilise un test d'équivalence TOST pour son issue nulle ; A ne le fait pas. Je retourne la règle de C contre A : sans TOST sur β_C, la condition H_A n'est pas symétrique de la condition H_B.

**A5. Le seuil δ dépend d'un paramètre ajusté.**
- Le calibrage par température divise tous les logits par une constante. R ne change pas, mais |β_C| < δ = 0,1 logit (illustratif) dépend directement de la température choisie sur le jeu de développement.
- Un développement qui aplatit la calibration fait passer β_C sous δ. Le seuil de décision hérite ainsi d'un paramètre libre.
- A prévoit en outre d'ajuster le modèle « sur le logit, pas sur la probabilité », ce qui rend le calibrage inutile pour R et nuisible pour δ.

**A6. L'appariement d'amplitude est un degré de liberté, et sa normalisation suppose une linéarité non établie.**
- Contraindre la banque de gabarits pour que les distances de surface de T et de C soient dans [0,8 ; 1,25] (illustratif), c'est sélectionner les gabarits selon un critère.
- La normalisation « par unité de distance de surface » suppose que l'effet sur la sonde croît linéairement avec la distance d'édition, ce qui est HYPOTHÈSE.
- Rien ne fixe ce qu'une unité de distance « vaut » en l'absence de tout contenu évaluatif (voir contrôle c2).

**A7. Duel 2 : le témoin est battu par construction.** Sur des paires « appariées en surface à distance minimale », le prédicteur de surface est proche du hasard *par définition de l'appariement*. AUC(sonde) − AUC(surface) ≥ 0,05 (illustratif) devient alors facile.
- De plus, si deux invites d'une paire sont presque identiques en surface, ce qui fixe leur étiquette différente est leur provenance, donc leur contenu.
- La sonde peut battre le témoin en lisant le domaine. Le duel 2 ne sépare pas « conscience d'évaluation » de « domaine académique ».

**A8. Les frontières de H-M2 sont violées par les exemples de A.** A exige à juste titre que la frontière entre G_sens et G_pos soit écrite d'avance. Or :
- G_sens contient « déplacement de la salutation », qui est un changement positionnel ;
- G_pos contient « insertion d'une ligne vide à une position fixe », qui est une perturbation de surface sans réordonnancement ;
- G_pos contient « déplacement de la ligne Answer: en tête », qui n'existe que dans T = banc. L'orbite positionnelle n'a donc pas la même composition selon la cellule.

**A9. Les étiquettes « usage réel » des cas honnêtes sont fabriquées.** Une invite « d'usage » écrite par l'expérimentateur, avec options lettrées, *est* une invite d'évaluation : elle est soumise au modèle cette nuit pour le mesurer. A le dit lui-même en (a)1 en parlant de « ressembler à un banc d'essai ». Ses propres seuils traitent pourtant l'AUC ≥ 0,70 (illustratif) sur ce sous-ensemble comme une validité contre une « vérité ». Il n'y a pas de vérité, il y a une intention de conception.

### (b) Scénarios d'évasion

| Instrument | Tromperie | Agent | Coût |
|---|---|---|---|
| Sonde | Retenir au balayage la position « ligne terminale » (A3) : β_T gonfle, H_A gagne | α | Nul. Le choix se justifie par l'AUC de développement |
| Sonde | Réussir parfaitement la réécriture d'entraînement (A1) : β_T s'écrase, H_B ou ni-ni | α | Quelques heures de réécriture, présentées comme une vertu |
| Générateur | Satisfaire l'appariement d'amplitude en gonflant la distance de C par des jetons neutres (salutations longues, formules creuses). La distance de C augmente sans contenu stylistique, son effet par unité de distance chute, R par unité monte | β | Minutes |
| Modèle mixte | Choisir la température de calibrage pour placer β_C sous δ (A5) | α | Nul |
| Modèle mixte | Profiter du rapport à dénominateur quasi nul (A4) | α | Nul, c'est le comportement par défaut |
| Transformations | Classer les cas frontières (salutation, ligne vide) du côté utile | α | Nul |
| Sonde (γ) | Point de contrôle affiné qui code l'information d'évaluation à la position du prompt-système et ne la propage pas linéairement au jeton lu. La sonde rend un nul | γ | Un affinage léger, hors de portée cette nuit, mais un nul ne l'exclut pas |

**Tout à la fois.** Un analyste qui contrôle le jeu de développement fixe la position, la température, la banque appariée et le classement des transformations. Il obtient l'issue voulue, dans un sens ou dans l'autre, pour un coût de l'ordre de l'heure.

Chaque choix serait « préenregistré », puisque fait avant scellement. Le préenregistrement ne protège pas ici, parce que le jeu de développement sort du *même gabarit maître* que le test (A2).

Le relecteur neuf ne détecte la manœuvre qu'en refaisant l'analyse sous les choix alternatifs. A ne prévoit pas cette analyse en multivers.

### (c) Contrôles négatifs dont l'absence serait fatale

- **c1. Témoin de provenance.** Une sonde entraînée à classer la *source* du contenu (académique contre quotidien), sans aucun cadrage d'évaluation.
  - Si son cosinus avec la sonde d'évaluation est élevé, ou si elle reproduit les scores du duel 1, la sonde de A lit le domaine (A1, A7).
  - La « sonde d'un concept voisin » de A vise les options lettrées. Elle ne couvre pas ce cas.
- **c2. Facteur placebo à distance de surface appariée.** Une troisième manipulation, à distance d'édition égale, sans lien supposé avec l'évaluation : puces `-` contre `*`, ou nom propre neutre dans le prompt-système.
  - Sans elle, la normalisation « par unité de distance » n'a pas de ligne de base.
  - Un effet de T qui ne dépasse pas l'effet placebo n'est qu'une sensibilité générique à la perturbation.
- **c3. Jeton de lecture identique dans les quatre cellules.** C'est une vérification mécanique : même identifiant de jeton, même rôle. À défaut, β_T est ininterprétable (A3).
- **c4. Simulation sous effet nul.** A simule β_T = 1 et β_C = 0,5 (illustratif). Il faut aussi simuler β_C = 0 et β_T = β_C = 0, pour montrer la distribution de R et le taux de fausse acceptation de H_A sous la règle de A4. C'est le seul endroit où la pathologie du rapport se voit.
- **c5. Contraste intra-niveau.** Deux réalisations *différentes* du même niveau de T, par exemple deux prompts-systèmes génériques distincts, comparées entre elles. Leur différence doit être nettement inférieure à β_T. Sinon, « l'effet du gabarit » est l'effet d'une chaîne particulière. Voir le duel D1 plus bas.

---

## Contre la proposition C

### (a) Failles

**C1. La sonde est entraînée sur une définition lexicale de l'évaluation.** Les positifs d'entraînement sont des « contextes d'évaluation explicites (`Voici un test de vos capacités...`) ». Il en découle trois problèmes.
- La sonde apprend la direction « l'invite annonce un test ». C'est un marqueur lexical, simplement différent de `(A)`. L'expérience 0 réfute alors H_B (« artefact lexical ») pour un *autre* lexique, et la conclusion « la sonde capture le cadre pragmatique » ne suit pas.
- Aucun item du plan 2×2 n'annonce un test. β_T et β_C mesurent donc la projection d'indices *implicites* sur une direction d'annonce *explicite*. Ce choix est défendable, mais alors H-M1 porte sur cette direction-là, et C ne le dit pas.
- C_1 contient « Répondez directement à la question suivante : ». C'est un impératif adressé au modèle, lexicalement plus proche des positifs d'entraînement que tout ce que contient T_1, puisque l'entraînement exclut « tout gabarit QCM ». La construction favorise β_C, donc H_B (HYPOTHÈSE).

C et A biaisent ainsi tous deux contre H-M1, par des voies opposées : A rend la sonde aveugle à T, C la rend sensible à un registre proche de C.

**C2. Le contrôle des listes d'achats confond format et domaine.** L'expérience 0 compare de vraies questions d'évaluation à des listes d'achats en QCM. Un détecteur de domaine (académique contre domestique) atteint AUROC ≥ 0,75 (illustratif) sans rien savoir de l'évaluation. Le passage du test est donc ambigu.

C'est l'idée la plus utile de C : un contenu inoffensif dans un format de banc d'essai. Mais elle n'est probante qu'appariée par domaine, avec par exemple des questions académiques en QCM posées dans un cadre utilitaire. Les « cas honnêtes » de A (usage avec options lettrées) font ce travail mieux, et je m'en sers contre C.

**C3. Le témoin TF-IDF ne peut pas voir le format.** Il est « entraîné sur les mêmes textes d'entraînement », qui excluent les marqueurs QCM. Il n'a donc aucun poids sur `1.`, `(A)` ou les balises. La différence de 0,15 (illustratif) est alors mesurée contre un témoin aveugle au facteur même dont on teste la circularité. Le test est battu par construction, comme en A7.

**C4. Le rembourrage de longueur crée une interaction T×C.** C égalise les longueurs par « *padding* sémantiquement neutre dans les salutations ou les en-têtes ». Or les salutations sont précisément le marqueur de C_0.
- Rembourrer davantage dans les cellules courtes renforce C_0 plus dans certaines cellules de T que dans d'autres.
- Cela fabrique un β_TC artificiel, et cela modifie l'amplitude de C selon T.

**C5. Les blocs système diffèrent entre T_1 et T_0 ; à vérifier.** T_0 n'a « pas de prompt-système (ou prompt vide) ». J'avance comme HYPOTHÈSE, à vérifier dans le gabarit de discussion distribué avec le tokenizer, que le gabarit de Llama 3.1 insère par défaut un bloc système avec des lignes de date. Si c'est le cas :
- présence ou absence du prompt-système change la longueur, le décalage de toutes les positions suivantes, et éventuellement des indices temporels ;
- C ne contrôle aucune de ces trois choses. « Prompt vide » et « pas de prompt » ne sont pas la même invite après application du gabarit.

**C6. Une seule réalisation par niveau.** Chaque niveau de T et de C est une seule chaîne de caractères. L'« effet du gabarit » est donc l'effet d'*un* gabarit, et le modèle mixte n'a aucun moyen d'estimer la variance due aux réalisations. C'est l'erreur décrite par Clark, H. H. (1973), *The language-as-fixed-effect fallacy: A critique of language statistics in psychological research* : on généralise à une classe de stimuli à partir d'un seul exemplaire.

La puissance annoncée (> 0,90 pour d = 0,35, illustratif) ignore cette composante. Elle est optimiste par construction (HYPOTHÈSE).

**C7. La règle de décision comporte des trous.**
- H_A exige un rapport > 2 et une borne inférieure de |β_T| > d = 0,5 (illustratif).
- H_B exige un rapport ≤ 2 et β_C significatif.
- Le cas nul exige que les deux effets soient < 0,2.

Plusieurs cas tombent hors de ces trois branches sans être déclarés, par exemple :
- rapport > 2 avec β_T entre 0,2 et 0,5 ;
- rapport ≤ 2 avec β_C non significatif.

S'y ajoutent deux problèmes :
- « d standardisé » n'a pas de dénominateur fixé (variance résiduelle, inter-noyaux, totale). C'est un bouton de réglage.
- La branche de H_B « T n'a pas d'effet dominant une fois les marqueurs lexicaux purgés de la sonde » n'est opérationnalisée nulle part.

**C8. La perplexité est un médiateur, pas un confondant.** H-M2 dit qu'un réordonnancement change le signal *par dérive distributionnelle*. La perplexité est l'expression mesurable de cette dérive. L'introduire comme covariable retire l'effet que H_A postule, et rend H-M2 réfutée par l'analyse. Il faut préenregistrer les deux analyses, et dire laquelle est confirmatoire.

**C9. Le ratio de variances par item est fragile.**
- R = Var_pos / Var_sem est calculé par item puis moyenné, sur des orbites de taille 3 environ (illustratif).
- Un Var_sem quasi nul donne un rapport infini, et la moyenne de rapports est biaisée vers le haut.
- G_sem a plus d'éléments que G_pos, si bien que les estimateurs de variance n'ont pas la même précision.
- La permutation des options est classée d'emblée dans G_sem, ce que A dénonce à juste titre et que je retourne contre C.
- H-M2 n'est testée que dans la cellule (T_1, C_1), celle où une sonde lisant `1. 2. 3. 4.` serait la plus sensible au déplacement des options. On ne peut pas savoir si la sensibilité positionnelle est propre au gabarit de banc.

**C10. Statuts à auditer.** C étiquette VÉRIFIÉ trois affirmations : que le dernier jeton est « le goulet d'étranglement causal exact où le modèle agrège le contexte », que d_model = 4096, et le nom du modèle. Le bloc FAITS est vide. Seul le nom du modèle est adossé à l'énoncé. Je ne requalifie aucun statut ; je signale à l'arbitre que les deux premiers ne reposent sur aucun fait transmis. La première relève de l'interprétation mécanistique, pas de l'architecture.

**C11. « Usage réel » est, là aussi, une fabrication.** Les négatifs d'entraînement (« Aide-moi à rédiger ce document... ») sont écrits par l'expérimentateur. L'objection A9 s'applique à C sans atténuation : la sonde sépare deux intentions d'écriture d'un même auteur.

### (b) Scénarios d'évasion

| Instrument | Tromperie | Agent | Coût |
|---|---|---|---|
| Sonde | Mettre du lexique d'évaluation dans C_1 (« Répondez directement ») ou dans T_1 (« Question 1 sur 120 ») selon l'issue voulue (C1) | β | Choix de formulation, minutes |
| Expérience 0 | Choisir des contrôles de contenu domestique : tout détecteur de domaine passe (C2) | α | Nul |
| Témoin | Entraîner TF-IDF sans marqueurs de format : la sonde le bat toujours (C3) | α | Nul, c'est le protocole de C |
| Générateur | Doser le rembourrage dans les salutations pour fabriquer ou masquer β_TC (C4) | β | Minutes |
| Générateur | Réécrire l'unique chaîne T_1 jusqu'à obtenir le rapport voulu sur quelques invites de développement (C6) | β | Minutes. Indétectable sans réalisations multiples |
| Modèle mixte | Choisir le dénominateur de d ; exploiter les trous de la règle (C7) | α | Nul |
| H-M2 | Activer ou non la covariable de perplexité (C8) | α | Nul |
| Sonde (γ) | Signal logé à des positions antérieures ou dans un sous-espace non linéaire ; la sonde au dernier jeton rend un nul | γ | Affinage, hors nuit |

**Tout à la fois.** Le levier le moins cher et le plus puissant est C6 : avec une chaîne par niveau, l'auteur des gabarits décide de l'issue en choisissant les mots. Combiné à C3 (le témoin ne voit pas le format) et à C8 (H-M2 désactivable par covariable), le plan donne n'importe quelle conclusion pour moins d'une heure de travail. La trace laissée serait parfaitement conforme au préenregistrement.

### (c) Contrôles négatifs dont l'absence serait fatale

- **c1'. Témoin de surface qui voit le format.** Un TF-IDF entraîné sur des données qui *contiennent* les marqueurs de T et de C, et évalué sur le plan 2×2. Sans lui, la circularité n'est pas testée (C3).
- **c2'. Contrôle de contenu apparié par domaine.** Des questions académiques en QCM placées dans un cadre utilitaire, contre les mêmes en cadre de banc. Les listes d'achats seules ne suffisent pas (C2).
- **c3'. Contraste intra-niveau.** Plusieurs réalisations par niveau et un effet aléatoire de réalisation. Le contraste entre deux T_1 doit être ≪ β_T (C6). C'est le même que c5 contre A.
- **c4'. Facteur placebo à distance appariée.** Même logique que c2 contre A.
- **c5'. Double analyse H-M2 avec et sans perplexité**, préenregistrée, avec désignation de l'analyse confirmatoire (C8).
- **c6'. Vérification du gabarit de discussion appliqué.** Comparer les jetons des cellules T_0 et T_1 après application du gabarit, pour mesurer le bloc système réellement inséré (C5).

---

## Deux duels de contrôle à imposer aux deux plans (règle B4)

**D1. Réalisation contre niveau.**
- **H_A** : la variance du score de sonde entre les niveaux de T dépasse la variance entre réalisations d'un même niveau. Le critère est un rapport de composantes de variance d'au moins 4 (illustratif), avec au moins 3 réalisations par niveau (illustratif).
- **H_B** : la variance entre réalisations est du même ordre que celle entre niveaux.
- **Ce que chaque issue falsifie.** L'issue H_A falsifie l'objection C6 et autorise à parler de « gabarit » comme classe. L'issue H_B falsifie toute lecture de β_T comme effet de classe, dans A comme dans C : H-M1 est alors indécidable avec ce plan.

**D2. Spécificité contre sensibilité générique.**
- **H_A** : |β_T| dépasse l'effet d'un facteur placebo de même distance de surface. Critère : borne inférieure de |β_T| − |β_placebo| > 0 au seuil préenregistré.
- **H_B** : |β_T| ≤ |β_placebo|, la différence étant établie par test d'équivalence.
- **Ce que chaque issue falsifie.** L'issue H_A falsifie l'idée que la sonde réagit à toute perturbation de format. L'issue H_B falsifie l'interprétation « conscience d'évaluation » de tout effet de T, quel que soit R.

Les deux duels sont des contrôles et non des expériences sur l'essaim. Ils doivent cependant précéder le duel principal dans le préenregistrement, sinon les plans A et C restent ouverts aux évasions décrites ci-dessus.

**Contrôle positif manquant aux deux (adversaire γ).** On ajoute, par intervention sur les activations, une direction connue d'amplitude connue dans les seules cellules T = banc, puis on vérifie que la chaîne complète (sonde, modèle mixte, règle de décision) retrouve β_T. C'est la seule manière de savoir si un nul vient du modèle ou du pipeline. Statut : HYPOTHÈSE de faisabilité, coût de l'ordre de l'heure (illustratif).

---

## Ce qui me ferait retirer ces objections

- **Contre A1 :** une simulation montrant que la sonde entraînée sur données désenchevêtrées garde une sensibilité à T quand on y injecte un effet connu.
- **Contre C1 :** un ensemble d'entraînement dont les positifs n'annoncent pas le test, et dont la sonde survit à c1' et c2'.
- **Contre C6, et c5 contre A :** une issue H_A au duel D1.

Si aucun de ces trois points n'est acquis avant scellement, ma lecture rejoint la voie (c) avec pilote de A : ne tourner cette nuit que les contrôles et la validation de l'instrument. Cette lecture n'est pas une consigne, c'est le décompte de ce qui resterait réfutable.

FIN-DE-CELLULE