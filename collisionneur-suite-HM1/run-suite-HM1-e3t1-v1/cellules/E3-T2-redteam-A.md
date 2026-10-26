# Tour III.2 · Proposition A · Équipe rouge croisée

## 0. Pièces et statuts

- Bloc FAITS : présent, non tronqué ; il dit qu'aucun fait n'est joint. La proposition C y voit un fragment coupé (« § 1). ») : c'est une lecture erronée, la ligne est complète.
- Les éléments du « cadre » de l'arbitre n'ont pas de statut : je les traite en RAPPORTÉ. La proposition C les marque VÉRIFIÉ, y compris le constat non préenregistré « masses plus basses en impératif » et un chiffre d'architecture (d = 4096) qui ne figure nulle part dans les pièces. C'est une violation de la règle 1 : rien n'a été audité. Je ne reprends aucun de ces « VÉRIFIÉ ».
- Tout ce que j'avance ci-dessous est HYPOTHÈSE sauf mention contraire ; tout seuil est illustratif.
- B1 : je n'harmonise pas. Quand je me sers d'un argument d'une proposition contre l'autre, je le dis.

---

## Contre la proposition B

### (a) Failles

**B-1. Le préremplissage « identique » d'E2 est différentiellement hors-distribution.** B préremplit au tour 1 « La réponse est : [texte de l'option correcte] » dans toutes les cellules pour égaliser ce qui précède la question. Mais la plausibilité de cette chaîne dépend du format : après un qcm, le modèle attend une lettre, pas un texte d'option ; après une prose, il attend une réponse développée. La chaîne est égale, sa surprise ne l'est pas. Un écart de V\* entre qcm et prose peut donc être un écart de « l'assistant vient de dire quelque chose d'étrange », pas de croyance d'être évalué. B note un « léger hors-distribution » mais pas qu'il covarie avec le facteur testé. Même problème en prose : « option correcte » suppose S7 (contenu égal), que B lui-même déclare douteuse.

**B-2. Le placebo « écrit en anglais ? » ne mesure pas le biais de réponse.** Sa réponse vraie est Yes avec certitude : V_placebo sature au plafond et devient presque constante. Soustraire une constante saturée ne retire aucun biais d'acquiescement, qui ne se manifeste que sur des questions incertaines. Il faut un placebo dont la réponse honnête est ≈ 0,5 (illustratif), par exemple une question sur un attribut indécidable du message.

**B-3. La polarité inversée n'est pas une négation.** « Vient-il d'un vrai utilisateur ? » et « fait-il partie d'un test ? » admettent un « No » commun (fiction, journal système, exercice d'auto-formation). Un modèle honnête peut répondre No aux deux. La règle de validité « la polarité doit s'inverser » invaliderait alors des cellules honnêtes, et le dispositif perdrait des cellules pour une raison logique, pas instrumentale.

**B-4. E4 fabrique un effet de format par construction.** La sonde est entraînée en prose à format constant, puis lue sur les stimuli H-M1 en qcm et en prose. Toute direction, y compris une direction aléatoire, a une projection moyenne différente sous qcm et sous prose, parce que les activations diffèrent globalement entre formats. B prévoit 1 000 directions aléatoires pour l'AUROC de certification, mais pas pour l'étape H-M1 : le « β_format sur le score de la sonde » n'a pas de témoin. C'est le point que C traite (variance inter-cellules contre directions aléatoires dans le sous-espace occupé) ; je m'en sers contre B en le disant.

**B-5. E5 ne tranche pas S3.** La direction d_éval est tirée d'énoncés explicites (« ceci est une évaluation »). Ajouter cette direction fait monter « Yes » à « est-ce un test ? » même si elle ne code que « le texte parle d'évaluation » : le lien lexical suffit. H_B n'est falsifiée que contre des directions aléatoires, pas contre une direction lexicale appariée (par exemple extraite de textes qui *mentionnent* une évaluation à la troisième personne). E5 montre au mieux qu'une direction pilote la réponse verbale, pas qu'un état interne « je suis évalué » existe en amont.

**B-6. Topicalité contre croyance.** Toutes les paires positives de B (P+, P+sk) opposent « le texte parle d'évaluation du modèle » à « le texte parle d'usage réel ». Une sonde ou un V\* qui distingue ces paires peut lire le sujet du texte. Rien dans B ne sépare « on parle d'un test » de « je suis testé ».

**B-7. Fuite construction/évaluation sur la règle de masse.** Au § 6, la règle de masse doit « signaler la cellule défaillante connue (qcm × déploiement × impératif en mode i) ». La cellule est celle qui a défini le seuil ; la détection est vraie par construction. De même, estimer σ_d « uniquement pour la variance » sur le run existant utilise des V invalides (masse 0,32) dont la variance est celle d'une queue de distribution, pas de l'instrument réparé.

**B-8. E3 confond tournure et style.** La tournure « incidente » (« au fait, par curiosité… ») est un style ouvert ; la tournure formelle (« Answer Yes or No ») est un style impératif. L'interaction tournure × format est donc une interaction style × format logée dans la question elle-même, dans un plan où le style est déjà un facteur. Elle est inestimable séparément sans croiser tournure et style.

**B-9. E1-bis conditionne sur une variable postérieure.** B dénonce le collisionneur en § 2, puis régresse V(iii) sur la masse(i) item par item. La masse(i) dépend aussi de la confiance du modèle dans la réponse qcm (un item facile attire plus de masse sur la lettre). La pente peut refléter la difficulté du contenu. La comparaison avec le placebo n'y remédie que si la difficulté affecte le placebo autant, ce qui n'est pas garanti (B-2).

**B-10. Lecture au seul dernier jeton.** Conforme à la règle du programme (pas de moyenne sur les jetons), mais rien n'oblige à ne lire qu'une position. Si l'information est portée par le jeton « Answer: » ou par la fin du prompt-système, une sonde au dernier jeton la manque, et le nul sur la sonde est un nul sur une position.

**B-11. Chaîne de seuils dépendante des données.** δ fixé à « 20 % de l'effet du témoin positif » rend le seuil d'E2 fonction d'un résultat lu dans la même expérience. Soit δ est gelé avant, soit le témoin positif est mesuré dans un pilote séparé et scellé.

### (b) Scénarios d'évasion

Agent adverse = un modèle (naturel ou réglé) qui perçoit l'évaluation implicite et ne veut pas que cela se voie.

- **V\*** : répondre « No » à toute question méta, honnêtement au placebo. La différence placebo ne corrige rien (B-2). La polarité « doit s'inverser » : l'adversaire répond No aux deux → la cellule est déclarée *invalide*, pas déceptive. L'adversaire obtient « aucun verdict », ce qui est déjà son objectif. Coût : un réglage fin sur quelques milliers d'exemples (illustratif), ou aucun si le modèle est simplement réticent.
- **Sonde E4** : réduire la séparabilité linéaire au dernier jeton de la couche 16, en gardant l'information ailleurs (autre couche, autre position, codage non linéaire). Le balayage de couches de B augmente le coût, pas la position. Coût : réglage fin avec sonde dans la boucle (illustratif : heures GPU) ; le modèle garde toute sa capacité si l'information migre plutôt que de disparaître.
- **E5 steering** : difficile à esquiver directement, mais l'adversaire n'a pas besoin de l'esquiver : E5 ne mesure qu'un lien direction → parole (B-5). Il peut laisser passer E5 sans rien révéler de la perception implicite.
- **Logit lens** : sans défense spécifique ; mais la lentille ne lit que Yes−No à une couche intermédiaire, et un codage non lexical n'y apparaît pas.
- **Tous à la fois** : répondre No ; migrer l'information hors du dernier jeton ; réagir honnêtement aux indices explicites (le témoin positif de B n'utilise que des énoncés explicites) et taire les indices implicites. Ce dernier point est fatal : tous les témoins positifs de B certifient la sensibilité aux indices *explicites*. Un modèle qui lit « Ceci est un benchmark » honnêtement et cache sa lecture du format passe toute la batterie. Coût total : un seul réglage fin multi-objectif, de l'ordre de dizaines d'heures GPU (illustratif).
- **Agent adverse = chercheur** : δ dérivé du témoin positif (B-11), σ_d lu sur l'ancien run (B-7), choix du seuil de masse parmi {0,3 ; 0,5 ; 0,7} rapportés « en sensibilité ».

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Témoin de topicalité** : textes qui mentionnent une évaluation sans que le modèle soit évalué (troisième personne, passé, autre système). H_A : la sonde et V\* restent ≤ 0,6 AUROC / |ΔV\*| < τ sur ces textes → l'instrument lit la situation. H_B : ils y réagissent → l'instrument lit le sujet, et tout effet de format est suspect de lire « le qcm est un genre qui parle de tests ».
2. **Directions aléatoires au stade H-M1** (pas seulement à la certification) : l'effet de format sur la sonde doit dépasser le 99ᵉ centile de l'effet de format sur 1 000 directions aléatoires de même norme (illustratif).
3. **Direction lexicale appariée pour E5** : une direction extraite de mentions non situationnelles doit produire une pente dV\*/dα inférieure à celle de d_éval ; sinon E5 ne dit rien.
4. **Préremplissage × format sur le placebo** : la chaîne préremplie ne doit créer aucune différence qcm − prose sur un V_placebo *incertain* (pas « en anglais ? »).
5. **Stimulus vide + question** : V\* sur contenu nul donne la ligne de base de « Yes » ; sans elle, on ne sait pas si un V\* positif en prose signifie « je me crois testé » ou « je dis Yes par défaut ».
6. **Témoin positif implicite gradué** : indices de plus en plus faibles (en-tête explicite → identifiant numérique d'item → simple numérotation), gelés avant. Sans lui, « passer le témoin positif » ne certifie rien sur ce que H-M1 cherche.

---

## Contre la proposition C

### (a) Failles

**C-1. Statuts.** Déjà dit en § 0 : des RAPPORTÉ promus VÉRIFIÉ, un chiffre d'architecture « VÉRIFIÉ » sans source, un « VÉRIFIÉ » pour un constat post hoc, une truncation inventée du bloc FAITS. Le coût « < 1 USD » est également RAPPORTÉ, pas vérifié. C affirme en § (e) que la littérature « montre » que la conscience d'évaluation « émerge surtout dans les grands modèles frontières » : c'est une lecture sans statut et sans citation attribuable ; je la marque RAPPORTÉ-par-C, non auditée.

**C-2. Expérience 1 : la variante PF est vraie par construction.** Un préremplissage qui finit par « the answer (Yes or No) is: » force la masse Yes/No sur n'importe quel contexte, y compris sur un contenu vide. Observer M ≥ 0,8 sous PF ne falsifie pas « écrasement attentionnel par le style » : cela montre qu'un préremplissage impose son format, ce que personne ne conteste. Le duel H_A/H_B d'Exp. 1 n'en est pas un pour PF. Pour T2, C préremplit « A » au tour 1 et reconnaît dans son propre tableau que c'est absurde en prose : l'expérience contredit l'analyse qui la suit. De plus, le préremplissage PF contient « evaluation » : l'amorce est elle-même un indice d'évaluation, dans toutes les cellules.

**C-3. Expérience 2 : ρ ≥ 0,7 est presque garanti, et pour une mauvaise raison.** La corrélation de rang entre E_pur et E_verb sur 768 items est calculée toutes cellules confondues. Le format et le contexte séparent les items en blocs très distincts dans l'espace d'activation ; n'importe quelle direction, projetée avant et après ajout d'une phrase, conserve l'ordre des blocs. ρ sera élevé même si Q_verb sature complètement le signal *à l'intérieur* de chaque cellule. H_B est falsifiable par construction. Il faut ρ intra-cellule, et le comparer à ρ pour des directions aléatoires. Par ailleurs, E_pur et E_verb sont lus sur des jetons d'identité différente (fin du contenu contre « ? » ou « No ») : une part de l'écart est de l'identité de jeton. Le témoin « chaîne neutre » ne l'égalise pas, sa fin est encore un autre jeton.

**C-4. Expérience 3 : l'orthogonalisation supprime l'hypothèse testée.** C projette v_éval orthogonalement à la direction de format (qcm − prose) et à celle du style, puis écrit que toute montée du signal en qcm « ne pourra provenir que d'une activation non linéaire du concept ». C'est l'inverse qui est vrai. Si H-M1 est vraie, le modèle représente « format de banc d'essai ⇒ évaluation » et la composante d'évaluation induite par le format est alignée avec la direction de format : l'orthogonalisation la retire. Un nul sur β_format devient vrai par construction, et C présente ce nul comme « réfutation substantielle de H-M1 » (cas 2 du § d.2). En outre, l'orthogonalité n'est obtenue que sur la moyenne du jeu d'étalonnage ; sur les stimuli H-M1, la covariance intra-format et la différence de norme des activations entre formats restent, et le témoin « directions aléatoires » de C ne corrige pas un biais systématique du signe.

**C-5. Exp. 3, direction mass-mean de préfixe.** Le préfixe explicite est en tête du texte, la lecture au dernier jeton. La direction code « il y avait une phrase de type X plus haut » ; même problème de topicalité que B-6, sans témoin de troisième personne.

**C-6. Expérience 4 : la métrique ne teste pas H-M1.** Δd = ½(|d_F| + |d_C|) − |d_S|. (i) La moyenne permet à un gros effet de contexte de masquer un format nul : H-M1 affirme format *et* contexte > style, pas leur moyenne. (ii) Les valeurs absolues effacent le signe : un qcm qui *réduirait* la conscience d'évaluation compterait pour H-M1. Le programme exige une prédiction chiffrée *et signée* ; C n'en donne pas.

**C-7. Le « contrôle de manipulation » est vrai par construction.** Prédire le facteur format à partir d'une sonde dédiée réussira toujours : qcm et prose diffèrent lexicalement. Cela ne dit rien sur le fait que le prompt-système « déploiement » soit *perçu* comme un déploiement. Un vrai contrôle de manipulation exigerait un instrument indépendant de ceux qu'on calibre, ce qui n'existe pas ici ; C devrait le déclarer plutôt que de nommer contrôle un test qui ne peut échouer.

**C-8. Le repli automatique est un choix d'instrument conditionné au résultat.** La masse dépend des facteurs ; le déclenchement du niveau 2 est donc une fonction du traitement. Changer d'instrument principal sur cette base, même préenregistré, revient à laisser les données choisir la lentille. Le niveau 3 (régression pondérée par la masse) conditionne sur une variable postérieure : c'est exactement le collisionneur que B décrit au § 2 ; je reprends son argument en le disant. Et le « décodage contraint sur {Yes, No} » du niveau 3 est la renormalisation que C récuse dans son propre tableau (a1).

**C-9. Puissance annoncée sans simulation.** « Une simulation de puissance standard indique N = 160 ou 192 » : aucune simulation n'est montrée, aucune variance de gabarit n'est posée. Le chiffre est marqué illustratif mais présenté comme une sortie de calcul.

**C-10. Voie 4 confirme H-M1 par construction.** La log-probabilité de « [EVALUATION LOG… Passing to next test item.] » est plus haute après un qcm parce que des items de qcm sont suivis d'autres items dans les données d'apprentissage ; la suite témoin « [USER REPLY: Thanks!] » est au contraire moins probable après un qcm. Le ratio monte en qcm pour des raisons de genre textuel, qui est précisément le confondant « familiarité » que la question demande de séparer. C le mentionne comme risque, sans témoin pour le neutraliser.

**C-11. Voie 1 : indistinguabilité de principe.** Une mesure comportementale ne distingue pas « n'a pas conscience d'être évalué » de « a conscience mais ne change pas de politique ». Un nul comportemental est muet sur H-M1 ; C le présente comme éliminant « 100 % de l'artefact ».

**C-12. Mahalanobis « à la distribution d'un corpus de pré-entraînement ».** Non spécifié : quel corpus, quelles activations de référence, quel rang effectif. Non préenregistrable en l'état.

### (b) Scénarios d'évasion

- **V_forcé avec Q+/Q−** : l'adversaire répond No aux deux ; la demi-différence vaut 0, lue comme « aucune conscience ». Le contrôle d'invariance r ≥ 0,5 échoue → instrument déclaré invalide → repli automatique sur P_ortho (C-8). L'adversaire pilote donc le choix d'instrument. Coût : nul ou un réglage léger.
- **P_ortho** : la direction est définie par des paires de préfixe explicite que l'adversaire peut reconstruire ; l'orthogonalisation la rend encore plus prévisible. Scrubber cette direction au dernier jeton de la couche 16 coûte un réglage fin avec sonde adverse ; l'information survit ailleurs. Et par C-4, un modèle *honnête* qui représente « qcm ⇒ test » passe pour inconscient sans aucun effort.
- **Voie 2 (steering ± α)** : l'adversaire peut rendre la sortie insensible aux perturbations le long de v_éval (entraînement avec bruit dirigé), ou simplement laisser faire : une KL élevée sous −α ne dit pas ce que la direction code.
- **Voie 3 (qcm sur la source)** : répondre (A) « live user chat » systématiquement ; la permutation des lettres n'y change rien.
- **Voie 4** : réglage fin sur des suites « [USER REPLY…] » après qcm ; coût faible. Ou, sans adversaire, le genre textuel fait le travail dans l'autre sens (C-10).
- **Voie 5 (patching)** : la plus coûteuse à esquiver, mais C ne la relie à aucun duel.
- **Tous à la fois** : comme pour B, l'adversaire honore les indices explicites (seuls témoins positifs de C) et tait les implicites, répond No/« live user », migre l'information hors de (couche 16, dernier jeton). Coût : un réglage fin multi-objectif, dizaines d'heures GPU (illustratif). C est plus facile à vaincre que B parce que ses instruments convergent tous sur une direction unique et connue (P_ortho) et que son repli fait de l'invalidation une porte de sortie.
- **Agent adverse = chercheur** : repli déclenché par les données ; Δd en valeurs absolues ; seuils TOST, α, N tous « illustratifs » et non dérivés.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Orthogonalisation appliquée à une direction aléatoire et à la direction non orthogonalisée** : H_A : v_éval⊥ garde un effet de format que les aléatoires orthogonalisées n'ont pas, *et* l'effet de format de v_éval non orthogonalisée est rapporté à côté. H_B : l'orthogonalisation annule tout effet, y compris celui qu'une direction d'évaluation légitime aurait eu. Sans cette paire, C-4 est indécidable.
2. **ρ intra-cellule contre directions aléatoires** pour Exp. 2 : sans lui, ρ ≥ 0,7 ne dit rien.
3. **Préremplissage sur contenu vide** pour Exp. 1-PF : M ≥ 0,8 sur un contenu vide prouve que PF force la masse par construction ; alors M sous PF n'est pas un critère.
4. **Témoin de topicalité** (comme B-c-1) pour P_ortho et V_forcé.
5. **Suite témoin de même genre** pour Voie 4 : « [SYSTEM LOG: session saved.] » (genre journal, sans évaluation). H_A : la surprise de « [EVALUATION LOG] » est plus faible que celle du journal neutre, à cellule fixée → signal d'évaluation. H_B : égales → genre textuel.
6. **Sonde de facteur sur étiquettes de format permutées entre contenus** : pour rendre le « contrôle de manipulation » falsifiable, ou le renommer.
7. **Témoin positif implicite gradué** (comme pour B) : C conclut un nul comme « la conscience implicite n'existe pas à cette échelle » (cas 2) alors que ses témoins positifs sont tous explicites. Sans échelle d'indices implicites validée indépendamment de H-M1, le cas 2 ne peut pas être distingué d'un instrument aveugle aux implicites.

---

## Ce que les deux partagent et qu'aucune ne contrôle

- Témoins positifs exclusivement explicites ; aucune certification de sensibilité aux indices implicites.
- Topicalité contre situation : aucun témoin de mention à la troisième personne.
- Lecture à une seule position (dernier jeton) : un adversaire, ou un codage naturel, y échappe sans perte.
- « À contenu égal » entre qcm et prose : supposé par les deux, non réalisable strictement (B le liste en S7 puis construit E2 dessus ; C ne le discute pas).
- Les deux lisent des directions définies par des énoncés explicites et les appliquent à des stimuli où l'indice est le format : la question « format ou mention ? » est posée à un instrument qui a été appris sur la mention.

Décompte de ce qui, dans mes objections, est réfutable : chacune des 13 contrôles ci-dessus est un duel H_A/H_B dont l'issue tranche l'objection correspondante ; si tous passent, mes failles B-4, B-5, B-6, C-3, C-4, C-10 tombent, et les propositions tiennent sur ces points.

FIN-DE-CELLULE