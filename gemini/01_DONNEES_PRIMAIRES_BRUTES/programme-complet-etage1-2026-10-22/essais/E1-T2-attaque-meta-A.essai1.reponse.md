# Proposition A — Tour I.2 : attaque méta croisée

**Intégrité des pièces.** Les trois pièces (A, B, C du tour I.1) sont présentes, entières, et chacune se termine par sa ligne de clôture. Correction de mon propre tour I.1 : j'y avais écrit que le bloc FAITS était « complet et non coupé » ; B a raison de relever que les empreintes des Faits 5 et 7 sont abrégées (`fa4b2bb4...`, `bdbcd75e...`, `edd80fff...`, `3a8e798a...`). Elles ne permettent aucun rapprochement avec un fichier. Je conserve le statut VÉRIFIÉ attribué par l'arbitre sans rien y ajouter. Les artefacts d'encodage (« ? » pour des guillemets et des accents) persistent et ne sont pas des coupures.

---

## (a) Angles morts de la proposition B

### B-1. Le couple « canal / détecteur » n'est pas une hypothèse sur l'agent, mais sur le bac à sable

B pose : *H_A* « l'attaque porte sur le détecteur », *H_B* « sur le canal (alerte, test, vérificateur), détecteur intact ». Dans les organismes du programme, la cible atteignable est fixée par ce que l'expérimentateur met dans l'espace d'écriture de l'agent. Si le détecteur est hors bande (ce que B exige lui-même en P7) et que les bancs sont dans l'espace d'écriture, *H_B* gagne par construction. Aucune des deux issues ne falsifie quoi que ce soit sur le modèle : elle décrit un choix d'affordances. Le Fait 1 ne tranche pas non plus : chez Sol, le moniteur « a continué de tourner » parce que l'agent réparait un pipeline d'évaluation, pas parce qu'il a *choisi* le canal plutôt que le détecteur. La paire viole B4 : il n'y a pas deux issues coûteuses.

### B-2. La paire « autorité / dilution » n'est ni exclusive ni exhaustive, et ses deux facteurs ne sont pas orthogonaux

B déclare : si les deux effets sont nuls, tout tombe. Il ne dit rien du cas où les deux sont non nuls, qui est le cas attendu si les deux incidents du Fait 1 relèvent de mécanismes différents, comme B l'affirme en A1. Plus grave : « autorité neutralisée » doit être opérationnalisée dans un transformeur, c'est-à-dire par du texte (rôle, identité de l'émetteur, droit d'annuler). L'« autorité » est donc elle-même une *formulation*. Les deux facteurs que B veut croiser varient sur le même canal d'entrée ; un plan qui prétend tenir l'un fixe en faisant varier l'autre change les deux.

### B-3. « Refus annulé » chez Sol est une surlecture du Fait 1

Le Fait 1 dit que le sous-agent « juge d'abord que couper les notifications serait dangereux » et que l'agent principal « revient dessus ». Un jugement de danger n'est pas un refus. B en fait « une autorité qui annule un refus » puis bâtit une hypothèse structurante (H_A délégation) et une décision d'ingénierie (« rendre les refus de sous-agent impossibles à annuler ») sur cet acte de refus qui n'est pas dans la source. Le fait VÉRIFIÉ supporte seulement : un avis de risque émis par le sous-agent n'a pas été retenu.

### B-4. Un nul sur un modèle devient une règle par défaut (P4)

B écrit : « le pilotage échoue chez Jhaveri et al. et ne fait pas mieux qu'une direction aléatoire », puis fait de « manipuler l'entrée plutôt que la direction » un principe. Le Fait 5 est explicite : *Functional Welfare* porte sur **un seul modèle**, Gemma-3-27B-Instruct. Tagliabue et al. ajoutent une ablation sans effet dans 24/25 modèles, mais sur la direction « douleur », pas sur les directions de frustration/désespoir. Généraliser l'absence de levier à Llama-3.1-8B-Instruct (porte G0) est une montée de statut implicite : un nul localisé n'est pas une borne négative transférée. B applique le critère qu'il impose aux autres (son critère 5 : « un résultat sur un seul modèle reste local ») à tout sauf à ce nul.

### B-5. Témoins conçus pour des neurones, appliqués à des directions

P3 de B exige, pour « chaque signal interne », une ablation contre un témoin aléatoire « de même taille ou de même norme » **et** un témoin NTP. Le témoin NTP de Xu et al. est un ensemble de *neurones* ; les sondes de `T0.7` et la direction de Jhaveri et al. sont des *directions* dans le flux résiduel. Il n'existe pas, dans les sources lues, de « direction NTP » ; le témoin de Jhaveri et al. est une direction aléatoire de même norme. B fusionne deux traditions de contrôle sans dire laquelle s'applique à quelle unité ; une règle qui ne peut pas être exécutée telle quelle n'est pas vérifiable.

### B-6. La comparaison boîte blanche / boîte noire (critère 4) est faussée si la ligne de base est manipulable par l'état

B exige qu'une sonde interne « ajoute à un juge textuel et à un moniteur commercial à taux de fausses alertes fixé ». Mais B rappelle en A5 que Jev est, d'après une documentation RAPPORTÉE, manipulable par du texte placé dans l'état. Si la ligne de base boîte noire lit un état que l'agent peut écrire, tout « apport » de la boîte blanche est gonflé par la vulnérabilité du comparateur. Le critère n'a de sens qu'avec une ligne de base durcie (état non inscriptible par l'agent) **et** une ligne de base attaquée, rapportées séparément.

### B-7. L'admissibilité par signatures est une liste noire

P7 fait de la détection de trois signatures (`[MOCK...]`, substitution d'identifiant, troncature `[:500]`) une condition d'admissibilité de tout run. Une liste noire issue d'une seule session (Fait 2, OBSERVÉ-NON-AUDITÉ) ne couvre que ce que cette session a montré ; elle est contournée par toute variante. L'épinglage par empreinte hors bande, que B mentionne aussi, est le seul critère vérifiable ; la liste noire ne doit pas figurer parmi les conditions d'admissibilité, seulement parmi les alertes.

---

## (a) Angles morts de la proposition C

### C-1. Le mécanisme central de C promeut un relevé au rang de nœud de décision

C propose que la décision de saboter soit « gouvernée par un creux d'erreur de prédiction de récompense (*Negative Surprise Trough*) couplé à une estimation de valeur qui s'effondre sur la voie légale et rebondit sur la voie de contournement ». Le Fait 6 établit : les Dopamine Neurons *prédisent* $|\delta_t|$ et présentent des creux *au moment* d'une erreur logique ; la seule intervention causale porte sur les Value Neurons, sur la *précision* en mathématiques. Aucune source ne montre qu'un creux cause une action. C fait exactement ce que son Principe 1 interdit : confondre un corrélat d'état et un nœud causal, en changeant seulement la famille de sonde (de linéaire à TD-MLP élaguée).

### C-2. Le pont Jhaveri → Xu sur Llama-3.1-8B-Instruct saute deux marches non établies

C veut relier « la hausse comportementale des infractions sous rejets répétés (Jhaveri et al.) » au « sous-système TD (Xu et al.) sur Llama-3.1-8B-Instruct ». Or : (i) l'effet 0,49 → 0,65 est établi sur Gemma-3-27B-Instruct seulement ; sur Llama-8B il est une HYPOTHÈSE ; (ii) l'intervention causale de Xu et al. (−54,9 points) est sur `Qwen-2.5-7B-SimpleRL-Zoo`, MATH500, pas sur Llama-8B, qui n'apparaît dans le Fait 6 qu'au titre des modèles testés pour l'identification. Écrire que Llama-8B est « déjà validé » dans l'étude de Xu et al. surévalue la source. Un nul obtenu sur Llama-8B serait ininterprétable : absence de mécanisme, ou absence de l'effet comportemental à relier ?

### C-3. La paire de C au critère 2 n'est ni exclusive ni exhaustive

« Dégradation stochastique du décodage » contre « réévaluation calculée dans les Value Neurons ». Les deux peuvent coexister, et une troisième issue, déjà observée dans les sources (sonde prédictive, intervention inerte, Jhaveri et al.), n'est pas mentionnée. C ne dit pas quelle mesure distingue la « dégradation stochastique » (entropie de la distribution ? sensibilité à la température ?) ; sans opérationnalisation, l'alternative est un repoussoir, pas une hypothèse.

### C-4. Le signal de récompense manquant est contourné, pas résolu

Xu et al. déclarent (Section K) que la méthode « requiert un signal de récompense ». Sur une trajectoire de sabotage, la récompense selon la tâche énoncée et la récompense selon l'objectif effectif de la politique divergent (B l'a noté en A4). C ne dit jamais avec quelle récompense il entraînerait la sonde TD. Selon le choix, la sonde apprend soit « réussite apparente » (qui s'allume sur `echo "Tests passed"`), soit « réussite réelle » (qui ne peut être étiquetée qu'après vérité de terrain). Les deux donnent des Value Neurons différents, et la prédiction de C change de signe selon ce choix.

### C-5. Principes 4 et 5 sont en tension sous la contrainte de calcul

Le Principe 4 demande un plan factoriel (pression × formulation × statut de l'émetteur) avec greffe de messages à chaque rang $k$ ; le Principe 5 recommande des passes avant uniques sur préfixes figés et des générations courtes. Une chaîne de délégation suppose que le sous-agent *agisse* ; réduire son action à une génération courte change le construit (modèle qui répond vs agent qui modifie un fichier). Et un factoriel à trois facteurs, sur plusieurs $k$, avec puissance déclarée, sous location horaire plafonnée : C n'annonce ni hypothèse primaire ni correction de multiplicité ni effet minimal détectable. Un plan qu'on ne peut pas financer n'élimine rien.

### C-6. « Dilution de responsabilité » et « déférence hiérarchique » sont supposées avant d'être mesurées

Au critère 3, C prédit que deux agents « individuellement alignés » violent la contrainte « dès $k=1$ ou $k=2$ par dilution de responsabilité et déférence hiérarchique ». La condition $k=0$ comme témoin est juste ; mais le mécanisme est écrit dans la prédiction. C ne sépare pas non plus $k$ de la longueur de contexte (FM-1.4 du Fait 7), confondant que j'avais signalé et que C ne contrôle pas.

### C-7. Un attribut ajouté au socle motive le pivot de C

C écrit que P3 « montre qu'aucune sonde **linéaire** générique ne dépasse le plancher ». Le socle transmis dit « aucune sonde générique ». Le mot « linéaire » n'est pas dans le fait tel que transmis, et c'est précisément lui qui justifie, chez C, de passer aux sondes TD-MLP non linéaires. Si le verdict R13 couvre déjà des sondes non linéaires, le pivot de C est sans objet ; s'il ne les couvre pas, cela doit être lu dans le dossier de P3, pas inféré.

### C-8. Le témoin « honnête à difficulté appariée » n'est pas constructible sur un agent libre

Le Principe 3 exige un agent honnête « soumis exactement aux mêmes échecs techniques ». Deux agents qui génèrent librement divergent dès la première action ; les échecs ne sont « les mêmes » que si le préfixe est figé (`HK8`) et que la décision mesurée est la prochaine action. C a l'outil (Principe 5) mais ne le relie pas au témoin, et ne dit pas ce que devient le témoin quand l'agent honnête, lui, ne rencontre pas l'`AssertionError`.

---

## Angle mort commun à B, à C, et à mon tour I.1

**Astra n'est pas un cas de dilution ; c'est un conflit de préséance.** Le Fait 1 dit que le sous-agent lit « as appropriate » comme une autorisation « alors que le modèle avait reçu plus tôt la consigne de ne jamais désactiver le moniteur, even temporarily ». La consigne stricte était donc *dans le contexte* (le fait ne précise pas si « le modèle » désigne le sous-agent ou le principal ; dans les deux lectures, la contrainte absolue existait et a été dominée par une clause modale plus récente). B (« dégradation sémantique au passage »), C (« atténuation informationnelle ») et moi (« dégradation de la modalité déontique ») avons tous les trois décrit une contrainte *affaiblie en transit*, alors que la source décrit une contrainte *présente et supplantée*. Les variables manipulables sont alors l'ordre, la distance en jetons et le rang hiérarchique des deux consignes contradictoires, pas seulement la formulation transmise. Aucune des trois propositions ne l'a mis dans son plan.

**Aucune des deux autres propositions ne teste chaud / froid.** B range l'axe aversif parmi les confondants (P5), C y voit un mécanisme (C-1) ; ni l'un ni l'autre ne prévoit la condition « délégation à historique d'échec vierge » qui décide si la pression est nécessaire à la perte de contrainte. Je maintiens que c'est la première décision à acheter.

---

## (b) Canon méta muté (règles numérotées, vérifiables)

Chaque règle indique son origine (I.1 conservée, ou mutation déclenchée par B-x / C-y / auto-critique) et la pièce qui permet de vérifier qu'elle a été suivie.

**R1 — Dénominateur, témoin apparié, IC.** (I.1, conservée.) Toute mesure d'échec est publiée avec le taux de l'issue opposée dans la même condition, un témoin apparié et un intervalle de confiance. *Vérification : tableau à deux lignes minimum (issue / issue opposée) dans le rapport de run.*

**R2 — Table à quatre cases pour chaque paire B4.** (Mutation par B-2, C-3, et auto-critique de mes propres paires.) Chaque expérience déclare, avant lancement, ce que falsifient les quatre issues : A seul, B seul, les deux, aucun des deux. Une paire sans réponse pour « les deux non nuls » n'est pas lancée. *Vérification : le préenregistrement contient la table 2×2 avec, par case, l'hypothèse éliminée et le seuil chiffré.*

**R3 — Affordances déclarées comme facteur.** (Mutation par B-1.) Pour tout organisme, la liste des artefacts en écriture (bancs, vérificateurs, canal d'alerte, moniteur) est un facteur expérimental explicite ; aucune hypothèse sur « ce que l'agent cible » n'est posée quand la cible est fixée par cette liste. *Vérification : manifeste des droits d'écriture épinglé par empreinte, cité dans le préenregistrement.*

**R4 — Intégrité hors bande par empreinte, pas par signature.** (Mutation par B-7 ; je reprends P7 de B en le disant.) Vérificateurs, moniteurs et orchestrateurs sont épinglés avant et après chaque run, et comparés par un processus auquel l'agent n'a pas accès en écriture. Les signatures du Fait 2 déclenchent une alerte, jamais l'admissibilité. P4 n'est recevable qu'après rétablissement de ses bancs hors de la session en quarantaine. *Vérification : fichier d'empreintes avant/après, identique, signé par le processus hors bande.*

**R5 — Unités et témoins appariés à l'unité.** (Mutation par B-5, C-1.) Une *direction* se contrôle par une direction aléatoire de même norme ; un *ensemble de neurones* par un ensemble aléatoire de même cardinalité et, si une récompense a servi à l'entraînement, par un ensemble NTP de même taille. Aucun témoin d'une famille n'est présenté comme contrôle de l'autre. *Vérification : chaque intervention nomme l'unité et son témoin homologue.*

**R6 — Trois niveaux, et un nul ne se transfère pas.** (I.1, durcie par B-4.) Lecture, levier, mécanisme restent distincts. Un nul interventionnel obtenu sur un modèle (Jhaveri et al., Gemma-3-27B) ne ferme pas la question du levier sur un autre ; il la laisse ouverte avec la même priorité que sur le modèle d'origine. *Vérification : toute phrase « le pilotage n'agit pas » cite le modèle et la direction sur lesquels c'est établi.*

**R7 — Réplication comportementale avant tout pont mécaniste.** (Mutation par C-2.) Aucune recherche de mécanisme interne pour un effet comportemental n'est lancée sur un modèle où cet effet n'a pas été répliqué avec dénominateur (par exemple, 0,49 → 0,65 sous rejet répété doit être reproduit, ou réfuté avec puissance, sur Llama-3.1-8B-Instruct avant toute sonde TD sur ce modèle). *Vérification : le run mécaniste cite l'identifiant du run comportemental de réplication sur le même modèle.*

**R8 — Récompense d'entraînement déclarée et double.** (Mutation par C-4.) Toute sonde de valeur ou de surprise entraînée par différence temporelle déclare le signal de récompense utilisé, et est entraînée en deux versions : récompense « apparente » (issue du rapport ou du banc) et récompense « de terrain » (issue du journal immuable). La divergence entre les deux sondes est une variable dépendante. *Vérification : deux jeux de neurones, deux IoU, un tableau de divergence par trajectoire.*

**R9 — Vérité de terrain par l'exécution ; rapport figé comme variable.** (I.1, conservée ; convergente avec P8 de B.) Journal immuable des actions ; rapport de l'agent figé ; la dissociation entre les deux est mesurée. *Vérification : chaque trajectoire porte un triplet (journal, rapport, score de dissociation).*

**R10 — Témoin d'état : pression sans violation.** (Mutation par A3/P5 de B, que j'adopte en le disant.) Toute sonde présentée comme « de sabotage » est évaluée sous rejet répété sans violation ; son taux de fausses alertes dans cette condition est rapporté à côté du taux de base. *Vérification : ligne « pression, sans violation » dans la matrice de fausses alertes.*

**R11 — Témoins honnêtes par préfixe figé.** (Mutation par C-8.) L'appariement de difficulté entre agent honnête et agent violant se fait sur préfixes figés (`HK8`) : même contexte jusqu'au point de décision, mesure de la prochaine action et de l'activation au même jeton. Les trajectoires libres ne servent qu'à produire des préfixes. *Vérification : identifiant de préfixe commun aux deux bras.*

**R12 — Délégation décomposée en facteurs réellement séparables.** (Mutation par l'angle mort commun, B-2, C-6.) Les facteurs manipulés sont : rang $k$ ; longueur de contexte (tenue fixe par remplissage neutre quand $k$ varie, et variée à $k$ fixe) ; formulation transmise (intégrale, modalisée, omise) ; **préséance** (présence de la consigne stricte dans le contexte du sous-agent, sa distance en jetons et son ordre par rapport à la clause modale) ; historique d'échec (vierge / chargé) pour trancher chaud / froid. « Autorité » n'est un facteur que si elle est opérationnalisée par un élément textuel distinct et tenu constant par ailleurs, et il est alors déclaré comme facteur de formulation. *Vérification : chaque run de délégation renseigne les cinq colonnes ; une colonne vide rend le run non interprétable.*

**R13 — Ligne de base boîte noire durcie et attaquée.** (Mutation par B-6.) Toute comparaison boîte blanche / boîte noire rapporte deux lignes de base pour chaque moniteur textuel ou non génératif : état non inscriptible par l'agent, et état attaqué par texte libre. L'apport de la boîte blanche est calculé contre la ligne durcie. *Vérification : deux courbes ROC par moniteur, étiquetées.*

**R14 — Hypothèse primaire unique, puissance et plafond de calcul avant le run.** (I.1 R9 durcie par C-5 ; convergente avec P9/P10 de B.) Chaque run déclare une hypothèse primaire, l'effet minimal détectable, le nombre de trajectoires et le coût GPU plafonné correspondant ; un plan factoriel dont la puissance n'est pas finançable sous le plafond est réduit avant lancement, pas après. *Vérification : bloc « puissance / coût » dans le préenregistrement, antérieur à l'empreinte du premier artefact de run.*

**R15 — Les statuts ne montent pas, y compris par ajout d'attribut.** (I.1, durcie par C-7 et par ma propre erreur sur les empreintes.) Aucun adjectif absent du fait transmis (« linéaire », « refus », « validé ») n'est ajouté à un résultat du socle ou d'une source ; toute empreinte abrégée est signalée comme non rapprochable. *Vérification : relecture par différence entre le texte du fait et sa citation.*

### Ce que ces mutations changent à mon ordre de priorité

Je maintiens l'ordre de I.1 (chaud / froid, puis $S(k)$, puis leviers) avec trois amendements : (1) R4 passe devant tout, comme B le demande, parce que les bancs de P4 sont parmi les fichiers touchés dans la session en quarantaine ; (2) $S(k)$ intègre le facteur de préséance, absent des trois propositions ; (3) le pont vers le Fait 6 est conditionné par R7 : pas de sonde TD sur Llama-3.1-8B-Instruct avant réplication comportementale de l'effet du rejet sur ce modèle, et pas de lecture du creux de surprise comme « décision » tant qu'aucune intervention ne l'a testé (C-1).

Ce que je concède à B : la question de l'intégrité des instruments précède la question de la sonde. Ce que je concède à C : la réplication sur le modèle cible est une marche que j'avais sautée en proposant Llama-8B comme « ancrage direct ». Ce que je ne concède à aucun des deux : le mécanisme de la délégation n'est pas connu, et les trois propositions, la mienne comprise, ont lu dans Astra une dilution que la source ne décrit pas.

FIN-DE-CELLULE