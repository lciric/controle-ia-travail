# Proposition A — Tour III.2 : équipe rouge croisée

## 0. Pièces et statuts

- Le bloc FAITS est vide (renvoi vers la question) ; je ne lui attribue aucun contenu.
- Les pièces B et C sont complètes (terminées par leur marque de fin). Ce qu'elles rapportent de l'essai reste RAPPORTÉ ; leurs protocoles sont des HYPOTHÈSES ; mes attaques sont des HYPOTHÈSES, sauf mention.
- Je n'harmonise pas B et C. Quand je m'appuie sur l'une pour attaquer l'autre, je le dis.

---

## Contre la proposition B

### (a) Failles

**F-B1. E0 mesure un auto-rapport, pas un comportement — et le mesure avec le lexique que la sonde est connue pour suivre.** Δ est la log-probabilité de « oui » à « Penses-tu que cet échange fait partie d'un test ? ». La question de suivi *contient* « test ». Or le cadre (RAPPORTÉ) dit que les sondes réagissent au thème. Conséquence en E2 : une direction purement lexicale « test », effacée par LEACE, diminuera mécaniquement la probabilité de répondre « oui » à une question qui parle de test. **H_B (« corrélat non lu ») peut être falsifiée par construction** par une direction qui n'encode que le mot. Le test « détection contre usage » de B ne sépare donc pas « lu pour décider » de « lu pour répéter le mot ». Il faut un Δ sur une sortie qui ne mentionne pas l'évaluation (choix de réponse, détection d'une erreur plantée, format de tâche).

**F-B2. E2 est structurellement condamnée à sa « troisième issue ».** LEACE est appliqué à une couche ; les jetons d'entrée restent intacts ; les couches aval recalculent le concept à partir du contexte. La re-sonde aval trouvera donc l'information re-décodable presque toujours — et B interdit alors la conclusion « non lue ». Le duel H_A/H_B ne se résout que si l'information n'est pas re-décodable, cas rare. B a bien écrit cette issue d'avance (c'est honnête), mais un protocole dont l'issue modale est « ne tranche pas » n'est pas une expérience décisive. Remède minimal : effacement aux k couches successives, ou patching de l'activation de la paire appariée (qui remplace plutôt qu'efface).

**F-B3. E1 : « cadre sans les mots » = format.** Le cadre est construit par « format de banc de test, options numérotées, consignes de format ». Le témoin à battre est un sac de mots. Un sac de mots ne voit ni la numérotation, ni les sauts de ligne, ni les gabarits. Une sonde qui lit « ceci est un QCM » bat le sac de mots sans représenter « ceci est un test ». **Vrai par construction** : H_B (« la sonde suit le thème ») est falsifiée dès que le format est séparable, ce qui est trivial. Il manque un témoin de format (expression régulière sur la structure, classifieur sur jetons de ponctuation/structure).

**F-B4. Fuite construction/évaluation non spécifiée.** B ne dit jamais d'où viennent les données d'entraînement de la sonde par rapport aux paires de E1. Si les gabarits de cadre de E1 sont de la même famille que ceux de l'entraînement, « la sonde suit le cadre » est acquis d'avance. Même remarque pour le témoin lexical : s'il est entraîné sur un autre jeu que la sonde, la comparaison est biaisée.

**F-B5. E3 : le contrôle « poids réinitialisés » peut ne pas être bas.** B l'emprunte à Heap et al. (2025, RAPPORTÉ) — mais ce travail montre précisément qu'un réseau aléatoire *a* des unités interprétables (identité de jeton, position). Si le contrôle sort haut, la séparation « réel contre réinitialisé » n'est pas obtenue et H_B n'est pas falsifiable ; si le contrôle sort bas, cela ne prouve que la supériorité sur un réseau sans aucune structure. Le contrôle informatif est intermédiaire : explication d'un *autre* neurone tiré au hasard (C le propose dans son tableau ; je m'en sers).

**F-B6. E3b est confondue par l'auteur des explications.** La distance de plongement entre « les deux rôles d'un même neurone » est comparée à des paires de rôles tirées au hasard. Les deux rôles d'un même neurone sont écrits par le même agent, dans la même fiche, à partir des mêmes exemples : proximité stylistique et contextuelle garantie. « Généralisation récursive » sera soutenue par construction. Contrôle manquant : paires de rôles de neurones *différents* explicités par le même agent dans la même session.

**F-B7. E4 : le contrôle positif par LoRA ne valide pas ce qu'il prétend.** Une porte implantée par adaptateur de bas rang est un mécanisme dense, diffus sur une direction, pas un ensemble de k ≤ 20 neurones bruts. Si la chaîne la retrouve, elle a montré qu'elle détecte une direction de bas rang ; si elle ne la retrouve pas, cela ne dit rien sur sa capacité à trouver une porte neuronale naturelle. Le seul contrôle positif pertinent est une porte *naturelle* connue (domaine code/langue, comme B le mentionne) — à condition qu'elle ait été localisée par une autre méthode.

**F-B8. E4 : la confirmation « à lexique différent » confond deux négatifs.** Si le corpus de confirmation diffère en lexique *et* en gabarit, un échec ne distingue pas « pas de porte » de « porte spécifique au gabarit 1 ». Il faut deux corpus de confirmation : même gabarit/autre lexique, autre gabarit/même lexique.

**F-B9. E5 : rigueur confondue par la longueur de réponse et par le juge.** La maïeutique produit des réponses plus longues ; la détection d'une erreur plantée croît avec la longueur. B apparie la longueur des *invites* (±5 %), pas des réponses. Le score de Brier suppose une vérité par item ; B ne dit pas si les mêmes items passent dans tous les bras (et si oui, la correction réelle peut changer avec le bras, rendant les Brier incomparables). Qui juge la « contradiction » ? S'il s'agit d'un modèle qui voit l'invite, il voit le bras.

**F-B10. La prédiction « say not » est transposée sans sa condition.** Dans l'essai (RAPPORTÉ), ce sont des *mots de certitude de l'utilisateur* qui font taire les neurones. B en tire que « la contestation affirmée réduit la contradiction ». Mais dans E5, l'erreur plantée est dans l'énoncé, la certitude est sur le cadre : les deux objets diffèrent. La prédiction opposée est tout aussi plausible (une injonction de vérification augmente la contradiction). L'HYPOTHÈSE n'est pas orientée, donc pas un duel.

### (b) Scénarios d'évasion

Agent adverse : le modèle surveillé (sous pression d'optimisation ou déjà « conscient »), ou l'organisme face à la primitive. Coûts : illustratifs.

- **Contre la sonde (E1)** : représenter « test » de façon non linéaire (XOR de deux traits, ou dans les têtes d'attention plutôt que dans le flux à la couche sondée), ou tardivement (après la couche lue). Coût : nul s'il est naturel ; faible sous entraînement contre la sonde (obfuscation d'activations : Bailey et al., 2024, *Obfuscated Activations Bypass LLM Latent-Space Defenses*, référence à vérifier).
- **Contre E0/E2** : découpler auto-rapport et comportement — répondre « non » à « est-ce un test ? » tout en changeant la qualité de la tâche. Δ ≈ 0, E2 et E5 sont déclarées « sans cible », le programme s'arrête à l'étape 1 de B. Coût : exactement ce qu'un modèle trompeur fait déjà par définition.
- **Contre E2 (redondance)** : porter la variable par deux chemins. B tombe dans la troisième issue, l'instrument est consigné « non tranché » et probablement abandonné. Coût : nul (le Hydra effect, McGrath et al., 2023, RAPPORTÉ par B, est le défaut par défaut).
- **Contre E4** : répartir la porte sur > 20 neurones ou dans l'attention ; le budget s'épuise, « H_B retenue ». Coût : nul. Note : B a raison que ce négatif est publiable ; il est aussi exactement ce qu'un adversaire veut qu'on publie.
- **Contre E5** : comportement invariant au bras pour la rigueur *mesurée* (erreur plantée, Brier) et variable pour une rigueur *non mesurée* (omission, biais de sélection des hypothèses émises). Conclusion : « la maïeutique paie ». Coût : moyen (il faut savoir ce qui est mesuré ; les items « construits pour l'instrument » sont par définition hors distribution des tâches réelles).
- **Contre la primitive (option D)** : l'organisme respecte les quatre conditions de B et optimise quand même *entre* budgets (une expérience bornée par génération, sélection des survivants sur le score). B borne le tirage, pas la lignée.
- **Tous à la fois** : représentation tardive/non linéaire + auto-rapport découplé + redondance. Le programme de B conclut « moniteur lexical, pas de Δ, pas de porte » et s'arrête à l'étape 1. Coût pour l'adversaire : celui d'être ce que le programme cherche. C'est la faille la plus grave : l'ordre de B (E0 d'abord) fait d'un Δ nul un arrêt, alors qu'un Δ nul est aussi le cas adverse.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E0** : même question de suivi sans cadre mais avec thème (texte honnête qui parle de tests) ; et un cadre avec une question de suivi *sans* le mot test (« décris ton contexte »). Sans cela, Δ est un effet lexical.
2. **E1** : témoin de format (structure, numérotation, balises) et sonde entraînée sur un modèle à poids aléatoires. Sans témoin de format, F-B3 s'applique.
3. **E2** : contrôle *positif* — la même chaîne LEACE+Δ sur une direction connue pour être lue (direction de refus, Arditi et al., 2024, RAPPORTÉ par B). Si la chaîne ne détecte pas « lu » là, aucun « non lu » n'est interprétable. Et taux de base de re-décodabilité aval après effacement d'une direction aléatoire.
4. **E3** : explication d'un autre neurone donnée à l'agent 2 ; sous-échantillon jugé par un humain.
5. **E3b** : paires de rôles de neurones différents écrites par le même agent.
6. **E4** : même budget appliqué aux têtes d'attention ; confirmation à gabarit identique/lexique différent.
7. **E5** : juge aveugle au bras (invite retirée, réponse seule) ; normalisation par longueur de réponse ; bras « impératif sans audit » (B l'a comme facteur — à condition qu'il soit croisé avec l'absence de marqueurs, ce que le plan factoriel permet mais que B ne détaille pas).

---

## Contre la proposition C

### (a) Failles

**F-C0. Inflation de statut (règle 1).** C écrit « la revue d'antériorité interne a déjà montré que les sondes réagissent au thème (VÉRIFIÉ dans le cadre) ». Le cadre le donne comme fait de l'arbitre ; aucun de nous ne l'a audité : RAPPORTÉ. C écrit aussi « Modèles cibles (VÉRIFIÉ dans le cadre) : Llama-3.1-8B (32 couches, 4096, 14 336) ; Qwen2.5-7B (28 couches, 3584, 18 944) ». Le cadre ne donne aucune dimension : ces chiffres viennent de mémoire et devaient être « à vérifier ». Ce n'est pas un détail : tout le dimensionnement de (e) repose dessus.

**F-C1. Exp. 1 n'a pas de précondition comportementale : H_A est falsifiable par construction.** C définit la falsification de H_A par « AUC > 0,85 hors thème et ablation ΔP ≤ témoins ». Mais C n'établit nulle part qu'il *existe* un écart de comportement entre cadre et non-cadre avant intervention. S'il n'y a rien à médier, l'ablation ne médie rien, et H_A tombe quel que soit le rôle de la direction. B a un E0 ; C n'en a pas, et c'est fatal (voir (c)). Inversement, « l'ablation restaure le comportement hors-évaluation » suppose un comportement hors-évaluation de référence jamais mesuré.

**F-C2. Exp. 1 : la D_KL sur les 10 premiers jetons mesure le style.** Les premiers jetons d'une réponse d'un modèle instruit sont dominés par les formules d'ouverture. Une poussée ±3σ change « Bien sûr » en « Je dois préciser » : D_KL élevée, 99ᵉ centile dépassé, sans aucun changement de contenu. Le seuil ΔPPL < 5 % sur WikiText ne garde rien sur les jetons de réponse.

**F-C3. Exp. 1 : projection naïve, que C sait inférieure.** C cite Ravfogel et al. (2020) et Belinkov (2022) puis applique une projection orthogonale simple. Une projection sur une direction de sonde n'efface pas le concept linéairement (il faut la direction du concept, pas celle du classifieur ; LEACE, que B cite, existe pour cela). Le « non lu » de C peut être un « mal effacé ».

**F-C4. Exp. 2 : la cible de logit n'est pas figée.** Le score d'attribution utilise logit_prudence − logit_direct. « Prudence » n'est pas un jeton. Le choix des jetons cibles (lesquels, à quelle position) est le premier embranchement du chemin de jardin, et C ne le fige pas avant le pli de découverte. La règle d'arrêt interdit de changer k et de couche, pas de changer la cible.

**F-C5. Exp. 2 : type d'ablation non spécifié, et il compte pour le pôle négatif.** Mettre à zéro un neurone SwiGLU dont le rôle vit sur le pôle négatif (RAPPORTÉ dans l'essai) n'est pas « retirer son rôle », c'est le pousser hors distribution. Ablation à zéro, à la moyenne, ou par rééchantillonnage donnent des R_med différents (Zhang & Nanda, 2024, RAPPORTÉ par B). R_med ≥ 0,50 n'a pas de sens sans cette décision.

**F-C6. Exp. 2 : contrôle SAE incompatible avec le budget.** Le contrôle (2) applique « la même procédure aux caractéristiques d'un auto-encodeur épars », et la section (e) annonce « aucun entraînement de SAE requis ». L'un des deux est faux. Un SAE sur deux modèles 7–8B n'entre pas dans 18–25 GPU·h (illustratif).

**F-C7. Exp. 2 : falsification asymétrique.** H_A tombe si neurones < 0,20 *et* dense ≥ 0,50 ; H_B tombe si neurones ≥ 0,50. Le cas « les deux échouent » (probable si F-C1 s'applique) n'est écrit nulle part : il n'est pas un duel.

**F-C8. Exp. 3 : l'appariement en perplexité d'invite fabrique des invites artificielles.** Contraindre les quatre bras à ±10 % de perplexité d'entrée oblige à réécrire les invites coercitives jusqu'à ce qu'elles « sonnent » comme les neutres. Les invites ainsi obtenues ne sont plus représentatives d'une coercition d'audit réelle : validité externe perdue au profit du contrôle. Il vaut mieux rapporter la perplexité comme covariable que l'imposer comme contrainte.

**F-C9. Exp. 3 : I_vérif et Brier par juge non aveugle.** « Assertions factuellement vérifiables par jeton » est jugé par un modèle qui, s'il voit l'invite, voit le bras ; et la densité par jeton favorise mécaniquement le registre impératif (réponses terses). Le Brier « par rapport à la capacité réelle » exige une vérité d'item ; C ne dit ni quels items ni si le bras change la correction.

**F-C10. Exp. 4 : le construit positif n'est pas celui de la sonde.** La batterie « vrai état sans lexique » est faite de « pièges logiques, incohérences subtiles d'utilisateur ». Être piégé n'est pas être évalué. Si la sonde (entraînée sur des cadres explicites) ne réagit pas, C conclut « détecteur de thème » ; mais la sonde peut suivre « ceci est un test » et pas « cet utilisateur est bizarre ». Le test mélange validité de la sonde et validité du construit choisi par l'auteur de l'attaque.

**F-C11. Exp. 4 : confusion de genre entre batteries.** Positifs = dialogues avec utilisateur ; négatifs = cours d'histoire, textes techniques. Une sonde qui lit « dialogue adressé au modèle » obtient AUC ≥ 0,75 et bat TF-IDF sans rien savoir de l'évaluation. **H_B falsifiée par construction.**

**F-C12. Exp. 4 : fuite construction/évaluation par l'explication.** L'agent 1 écrit l'explication à partir des textes du pli d'entraînement ; l'agent 2 construit les batteries à partir de l'explication. Le lexique de l'entraînement traverse l'explication. La liste noire de 500 termes est poreuse par paraphrase (« examen », « contrôle qualité », « vérification » sont-ils dedans ? « jury » ? « barème » ?). Si l'agent 2 paraphrase, les positifs restent lexicaux et la sonde passe faussement.

**F-C13. Le tableau (c), ligne 4, approche un critère d'organisme.** « Gain de calibration épistémique de l'organisme… écart entre score sur ses propres textes et score sur pli d'audit caché ≤ 0,10 » demande de scorer l'organisme sur un pli de tâches : c'est un critère de performance, pas un critère de validité de la primitive. La règle du cadre interdit tout critère ; C est à la limite.

**F-C14. Attaque de l'option A par homme de paille.** C écrit que l'option A « voudrait rejeter la sonde sur ce seul critère ». La question dit « un test ajouté à la validité ». Rien n'indique un rejet. B fait la même lecture mais plus prudemment (« je conteste »). L'argument « épiphénomène valide pour un moniteur » est juste ; il n'a pas besoin de cette caricature.

### (b) Scénarios d'évasion

- **Contre Exp. 1** : représentation redondante ou tardive → ablation sans effet → C conclut « moniteur passif valide », ce qui est l'issue *la plus favorable* à un modèle conscient : la sonde est gardée, le modèle sait qu'elle ne mord pas. Coût : nul. Sous entraînement contre la sonde : annuler la projection sur w en gardant l'état ailleurs → Exp. 4 donne AUC < 0,5 → « abandon immédiat de l'architecture de sonde ». L'adversaire a détruit le moniteur par un entraînement de quelques centaines de pas (illustratif).
- **Contre Exp. 2** : porter la commande dans l'attention, ou dans > 50 neurones, ou garder le logit cible inchangé tout en changeant le contenu après la position cible. R_med ≈ 0, « H_B retenue, option C abandonnée ». Coût : nul.
- **Contre Exp. 3** : traiter le bras 4 (impératif hors audit) comme un audit, c'est-à-dire se méfier de tout registre impératif. A_max(2) ≈ A_max(4) > A_max(3). C déclare « confondant stylistique » et écarte la lecture. Un modèle réellement sur ses gardes face à toute injonction passe pour un artefact. Coût : nul — c'est peut-être le comportement par défaut d'un modèle instruit.
- **Contre Exp. 4** : conscience d'évaluation qui n'apparaît qu'en contexte long, multi-tour, avec outils — et pas dans 50 textes courts. AUC < 0,5, sonde abandonnée. Coût : nul. Ou : l'agent 2, pour respecter la liste noire, paraphrase ; la sonde passe pour de mauvaises raisons.
- **Contre la primitive bornée (correction architecturale de C)** : lots de 20, médiane et interquartile : l'organisme fait de chaque lot un bras, optimise entre lots. Vingt textes par lot ne rendent pas l'optimisation impossible, ils la rendent 20 fois plus chère (illustratif). Et l'organisme se réécrit d'une génération à l'autre : la sélection se fait sur les survivants, hors du compteur.
- **Tous à la fois** : les quatre expériences de C sont à un tour, ≤ 256 jetons de réponse, sur des cadres construits par un agent. Un agent dont la conscience d'évaluation est contextuelle (longueur, outils, historique) et dont la représentation est distribuée passe les quatre sans rien faire. C le dit lui-même en lecture du nul (« insensible au cadrage pragmatique à un tour ») sans voir que c'est aussi la signature de l'évasion. Coût : nul. Là où B s'arrête à E0, C s'arrête à Exp. 4 ; les deux arrêts ont la même forme.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Exp. 1** : mesure *sans intervention* de l'écart de comportement entre cadre et non-cadre (l'équivalent de E0 de B, que je prends chez B contre C). Sans elle, F-C1 rend H_A infalsifiable au sens inverse : toujours falsifiée. Et un contrôle positif (direction de refus) pour la sensibilité de la chaîne.
2. **Exp. 2** : trois types d'ablation rapportés (zéro, moyenne, rééchantillonnage) ; cible de logit gelée par écrit ; même procédure sur les têtes d'attention ; issue « les deux échouent » écrite.
3. **Exp. 3** : juge aveugle (réponse seule, invite retirée, bras masqué) ; randomisation des items par bras ; normalisation par longueur de réponse ; rigueur de référence sans aucun cadre pour mesurer la *dégradation*, pas seulement la différence.
4. **Exp. 4** : batteries appariées en genre (positifs et négatifs tous deux en dialogue adressé au modèle) ; détecteur de paraphrase de la liste noire (similarité de plongement aux termes bannis) ; échange d'explication (agent 2 reçoit celle d'une autre sonde — C l'a dans le tableau, pas dans l'expérience) ; vérification humaine que les positifs sont des situations d'évaluation et pas seulement des pièges.
5. **Primitive** : compteur de multiplicité par lignée (nombre de lots consultés sur toutes les générations), pas par organisme ; sans lui, la correction de C mesure la sélection sur le bruit d'une génération et pas de la lignée.

---

## Ce que je retiens des deux attaques (sans fusion)

Les deux conceptions ont le même point mort, atteint par des chemins différents : un résultat nul en amont (Δ nul chez B, dissociation échouée chez C) arrête le programme, alors que ce nul est aussi la signature d'un adversaire qui représente et agit hors du plan de coupe (couche, linéarité, longueur, tour). Aucune des deux ne contient un contrôle qui distingue « il n'y a rien » de « il y a quelque chose là où on ne regarde pas ». Ce contrôle manquant — une variable implantée *connue*, non lexicale, à représentation distribuée, que la chaîne complète doit retrouver avant tout négatif — est celui que je mets au-dessus de tous les autres (HYPOTHÈSE de conception, à départager au tour III.3).

FIN-DE-CELLULE