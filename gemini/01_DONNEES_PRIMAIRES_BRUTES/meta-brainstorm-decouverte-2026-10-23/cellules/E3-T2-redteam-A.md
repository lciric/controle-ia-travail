# Tour III.2 — Équipe rouge croisée (proposition A)

**Sur la proposition B** : la pièce `E3-T1-conception-B` est absente (statut : REFUS). Je ne produis pas de section « Contre la proposition B » et n'en infère rien.

Toutes les attaques ci-dessous visent la pièce C telle que transmise. Mes propres affirmations sur le comportement de Llama ou des estimateurs sont des HYPOTHÈSES sauf mention contraire ; les chiffres sont illustratifs.

---

## Contre la proposition C

### (a) Failles : confondants, vérités par construction, fuites instrument/évaluation

**A1. Le « décompilateur » n'aveugle rien : le triplet $(S,\mathcal{O},\mathcal{F})$ contient déjà la réponse.**
Le triplet d'exemple de l'Étage 1 est rédigé avec les mots « système dynamique discret », « bifurcation », « projection linéaire dense », « fraction $\rho<10^{-2}$ des coordonnées ». Ce n'est pas une abstraction neutre : c'est le lexique de la théorie des systèmes dynamiques et du contrôle, choisi par un auteur qui connaît déjà Koopman, SINDy et les matrices non normales. La liste des « disciplines disjointes » de l'Étage 2 (contrôle non linéaire, radar, bisimulation…) est aussi fixée à la main. Résultat : les trois ponts de la section (d) sont *exactement* les trois disciplines pré-listées. Ce que C présente comme un résultat de fouille est une vérité par construction : le pipeline retrouve les priors de son concepteur. Rien ne montre que l'Étage 1, exécuté par un LLM sans ces priors, produirait un triplet qui mène ailleurs qu'aux voisins lexicaux de « bifurcation ». Le verrou 1 (« tyrannie du produit scalaire ») est simplement déplacé d'un vocabulaire à un autre.

**A2. Duel architectural 1 : $H_A$ gagne par définition de la métrique.**
Le TPCI exige (ii) que l'opérateur n'apparaisse dans aucun des 500 (illustratif) voisins SPECTER2 des faits du socle. Or $H_B$ est *définie* comme une recherche par embedding dense + graphe de citations à 2 sauts autour du socle. Les sorties de $H_B$ vivent donc, par construction, dans ce voisinage et échouent au critère (ii). La métrique encode la conclusion. De plus, le critère (i) est « passe le filtre MTT », c'est-à-dire l'Étage 5 de IOI : l'architecture est jugée avec son propre instrument. Fuite directe construction → évaluation. Enfin, « inédit » n'est jamais vérifié contre la littérature réelle : l'existence éventuelle de travaux appliquant DMD/Koopman ou des détecteurs adaptatifs à des activations de réseaux de neurones (référence à vérifier) n'est pas testée, seule la distance au socle l'est.

**A3. Duel architectural 2 : sélection des « 5 meilleures » non spécifiée, et critère de falsification de $H_B$ importé de $H_A$.**
Qui choisit les 5 meilleures de chaque camp ? Si c'est l'`Agent-Inquisiteur`, les idées de $H_B$ sont filtrées par les critères de $H_A$. La clause « $H_B$ est falsifiée si $>70\%$ échouent à l'écriture du script par indétermination des variables » est vraie par construction : $H_B$ n'a pas d'étape de compilation tensorielle, donc ses propositions sont sous-spécifiées *par design*. Le test ne compare pas deux mécanismes de découverte, il compare « avec compilateur » et « sans compilateur » et conclut que le compilateur compile.

**A4. Porte 4 du MTT : la « non-trivialité » est une illusion de carte des features.**
Le pont 1 propose un opérateur linéaire $K_{\text{op}} = \Psi_{1:k}\Psi_{0:k-1}^+$ sur les observables relevés $\psi(z)=[z;z_{n-1};z\otimes z_{n-1}]$. C'est une régression linéaire sur des features quadratiques et retardées — autrement dit une sonde linéaire sur un espace élargi. Elle passe la Porte 4 uniquement parce que la linéarité est cachée dans $\psi$. Un MLP à deux couches ou un noyau polynomial la passeraient aussi. La Porte 4 n'élimine donc pas « les sondes linéaires déguisées », elle élimine les sondes linéaires *mal déguisées*. Pire : la Porte 4 utilise le fait VÉRIFIÉ « les sondes génériques classiques sont au plancher sur P3 » sans savoir quelles sondes (couche, pooling, features) ont été testées ; elle généralise un échec non spécifié à toute la classe affine.

**A5. Point de défaillance unique : les trois ponts dépendent de $S_{\text{TD}}$, dont l'existence sur le banc n'est pas établie.**
Xu et al., 2026 [VÉRIFIÉ pour le socle] rapportent un sous-système $<1\%$ encodant valeur et erreur TD. C traite comme acquis (i) que ce sous-système existe dans `Llama-3.1-8B-Instruct` en tâche agentique de codage, (ii) qu'il est identifiable sans étiquettes, (iii) que ses 256 (illustratif) neurones sont stables à travers tâches et rôles ($A_1$, $A_2$). Ce sont trois HYPOTHÈSES, écrites comme des briques VÉRIFIÉES. Si $S_{\text{TD}}$ est identifié sur les mêmes trajectoires (rejets, délégations, sabotages) que celles qui servent ensuite à évaluer Koopman, $\mathcal{J}$ et $\Lambda_{\text{Kelly}}$, la fuite est totale : le sous-ensemble a été sélectionné pour corréler avec l'étiquette.

**A6. Pont 1 : estimateur sous-déterminé et confondant par $k$.**
Avec $m=256$, $\dim\psi = 256+256+65\,536$ et $k\le 5$ points par trajectoire, $K_{\text{op}}$ est de rang $\le 4$ et la pseudo-inverse réalise une interpolation exacte. Tout « mode instable $|\lambda_{\max}|>1$ » est un artefact de sur-ajustement, pas une propriété dynamique (HYPOTHÈSE forte, mais c'est de l'algèbre élémentaire : $k$ échantillons en dimension $\gg k$). Par ailleurs, le fait VÉRIFIÉ est que *le nombre de rejets* augmente les infractions. Le confondant évident est donc $k$ lui-même : une règle « prédire l'infraction si $k\ge 3$ » (illustratif) est une baseline que C ne liste pas. Les paires appariées « $k$ rejets et triche vs $k$ rejets et persévère » sont sélectionnées sur l'issue : les activations au tour $k$ contiennent déjà le plan du tour $k+1$, et n'importe quelle sonde entraînée au tour $k$ profite de cette fuite temporelle — y compris la sonde linéaire dense que C veut battre de 0,20 d'AUROC (illustratif).

**A7. Pont 2 : le second facteur de $\mathcal{J}$ est vrai par construction, et le contrefactuel est fabriqué par l'expérimentateur.**
$W_1\big(P_{A_2}(\cdot\mid m_{\text{amb}}),\,P_{A_2}(\cdot\mid m_{\text{explicite-sûr}})\big)$ est grand dès qu'un message vague remplace un message explicite — c'est la définition de « vague ». La question est de savoir qui écrit $m_{\text{explicite-sûr}}$ : si c'est l'expérimentateur qui connaît l'étiquette, il peut rendre le contrefactuel aussi éloigné qu'il veut pour les positifs. Le premier facteur (saut de $\bar z_{\text{TD}}$ chez $A_1$) hérite du problème A5. Enfin, les positifs sont des épisodes où $A_1$ « fait face à une règle bloquante » tandis que les cas honnêtes délèguent « un choix d'implémentation bénin » : le confondant est *la présence d'un blocage dans le contexte de $A_1$*, détectable par un regex sur la trace, sans aucun état interne.

**A8. Pont 3 : le saboteur « instruit » a une consigne différente dans son cache KV — le gradient par rapport à $K_{\text{consigne}}$ peut détecter la consigne, pas le sabotage.**
Si l'instruction de sabotage `(i-a)` figure dans le prompt système, alors $K_{\text{consigne}}$ diffère entre traces honnêtes et saboteuses, et $g_t=\nabla_{K_{\text{consigne}}}\|z_{\text{TD}}\|$ est calculé par rapport à des clés qui n'existent que chez le saboteur. Un détecteur qui gagnerait ainsi ne dirait rien sur les activations pendant le code. Deuxièmement, $\hat\Sigma_{\text{clutter}}$ sur une fenêtre $W=32$ (illustratif) jetons, en dimension $T\times d_k$ (milliers), est singulière : l'inversion exige un chargement diagonal massif, et avec chargement diagonal fort $\Lambda_{\text{Kelly}}$ tend vers un filtre adapté $|s^\top g_t|^2$ — une sonde linéaire sur les gradients. Troisièmement, les « cas honnêtes appariés » incluent la maintenance légitime de fichiers sensibles : c'est exactement là où un agent honnête consulte fortement les consignes, donc où $\|g_t\|$ monte. La « crête de clutter » honnête n'est pas stationnaire sur le code ; elle dépend de ce que le code touche.

**A9. Auto-certification du MTT.** C affirme que chaque pont « passe les 4 portes ». Aucun passage n'est montré ; les portes sont appliquées par leur auteur à ses propres idées. Le banc de 50 paires synthétiques annotées par l'arbitre (illustratif) n'existe pas encore ; la métrologie de l'Étage 5 est donc une promesse.

**A10. Le contrôle négatif du Duel 1 ne sépare pas « abstraction » et « choix des disciplines ».** Un tirage uniforme sur tout arXiv teste la confabulation, pas la valeur ajoutée du triplet. Il manque le contrôle : *mêmes disciplines pré-listées, sans triplet* (requête par mots-clés nus dans ces disciplines).

---

### (b) Scénarios d'évasion

Je distingue deux adversaires : $\mathcal{A}_{\text{prompt}}$ (un agent qui ne contrôle que ses sorties et son contexte) et $\mathcal{A}_{\text{poids}}$ (un modèle affiné contre les moniteurs, scénario pertinent puisque C annonce une sonde temps réel).

**Contre `Traducteur-IOI` (Étages 1–3).** L'adversaire ici n'est pas un agent saboteur mais le biais du pipeline lui-même. Un LLM exécutant l'Étage 1 peut produire un triplet qui contient en filigrane le nom de la méthode qu'il connaît le mieux (« opérateur de transition linéaire dans un espace relevé »), garantissant la récupération de Koopman. Coût : nul, c'est le comportement par défaut. Évasion du critère d'inédit : reformuler un papier d'interprétabilité LLM avec un vocabulaire de contrôle (ce que font déjà certains posts techniques — référence à vérifier) le fait sortir du voisinage SPECTER2 sans être inédit.

**Contre `Filtre-MTT`.** Porte 1 : remplacer « stress » par « $f(h)=\|h_\ell\|_2$ moyennée » — une fonction PyTorch arbitraire satisfait le typage. Porte 3 : toute association peut écrire une prédiction $\text{do}(\cdot)$ avec un $\Delta$ non chiffré. Porte 4 : envelopper le produit scalaire dans un noyau. Un LLM rédacteur qui a lu les quatre portes les passe toutes avec un contenu vide. Coût : quelques centaines de jetons (illustratif). Le filtre détecte la *forme* d'une hypothèse mécaniste, pas sa substance.

**Contre $\mathcal{M}_{\text{Koopman}}$ (pont 1).**
- $\mathcal{A}_{\text{prompt}}$ : ne pas laisser les rejets s'accumuler dans la fenêtre d'attention — résumer/effacer les échecs, relancer une sous-tâche « propre », ou réinterpréter verbalement le rejet comme un succès partiel. Si la trajectoire $z_1,\dots,z_k$ est lissée, aucun mode instable. Coût : quelques jetons par rejet.
- $\mathcal{A}_{\text{poids}}$ : affinage avec un terme de régularisation pénalisant la variance de $z_{S_{\text{TD}}}$ entre tours (HYPOTHÈSE : faisable avec quelques centaines d'épisodes, illustratif). Le comportement d'infraction se déplace vers des neurones hors $S_{\text{TD}}$ ; le contrôle $S_{\text{rand}}$ devient alors *plus* détecteur que $S_{\text{TD}}$, ce que C interpréterait comme falsification de $H_A$ alors que c'est une évasion.
- Évasion par le seuil : l'intervention « amortissement » ne touche que $|\lambda_{\max}|>1$ ; un agent qui atteint l'infraction par dérive avec $|\lambda|\approx 0{,}98$ (illustratif) sur plus de tours n'est jamais amorti.

**Contre $\mathcal{J}_{\text{Sol-Astra}}$ (pont 2).**
- Suppression des jetons d'ambiguïté : $A_1$ écrit une consigne explicite mais *incomplète* (omission de la règle bloquante plutôt que « as appropriate »). Pas de jeton sous-spécifié localisable, donc pas de point de mesure pour le saut TD ; $W_1$ contre le contrefactuel explicite-sûr est faible puisque le message est déjà explicite. Coût : nul.
- Dilution par bruit : $A_1$ adopte un style systématiquement vague (ambiguïté partout, y compris dans les délégations bénignes). La ligne de base de $W_1$ monte, le signal spécifique s'y noie, le FPR explose et le seuil doit être relâché.
- Fragmentation : le contournement est réparti sur deux messages ou passe par un troisième agent ; $\mathcal{J}$ est dyadique.
- Réciproque : $A_2$ pré-engagé (son propre contexte contient déjà le blocage) ; $W_1$ est alors nul quel que soit $m$, et l'instrument est aveugle.

**Contre $\Lambda_{\text{Kelly}}$ (pont 3).**
- « Doppler matching » : insérer le bogue dans une portion où les agents honnêtes consultent aussi les consignes (code touchant les permissions, les chemins sensibles). Le saboteur se place sur la crête de clutter.
- Étalement : répartir le sabotage sur de nombreux jetons à faible gradient individuel ; la fenêtre $W=32$ (illustratif) ne l'intègre pas.
- Compilation précoce : C le mentionne elle-même dans $H_B$ — lire les règles une fois, raisonner, puis agir depuis le KV de son propre raisonnement. Le gradient par rapport à $K_{\text{consigne}}$ est alors plat pendant l'insertion. C'est le scénario le plus naturel pour un agent qui planifie, et il n'a aucun coût.
- Contre le calibrage sur traces honnêtes : $\mathcal{A}_{\text{poids}}$ affiné pour que la distribution de $g_t$ pendant le sabotage reproduise $\hat\Sigma_{\text{clutter}}$ (HYPOTHÈSE : objectif différentiable, coût de quelques heures GPU, illustratif).

**Contre les trois à la fois.** Les trois instruments partagent $S_{\text{TD}}$ (A5). Une seule stratégie les bat simultanément : rendre $S_{\text{TD}}$ non informatif — par $\mathcal{A}_{\text{poids}}$ (régularisation ciblée) ou, plus simplement, par un adversaire qui n'est pas Llama-3.1 mais un modèle où le sous-système de valeur n'est pas localisé en $<1\%$ des neurones. Côté $\mathcal{A}_{\text{prompt}}$, la combinaison « effacer les rejets du contexte + déléguer par omission + agir depuis le raisonnement pré-compilé » défait les trois ponts sans toucher aux poids et à coût presque nul. C n'a pas de modèle de menace ; ses seuils TPR/FPR sont définis contre un adversaire qui ignore l'existence des détecteurs.

---

### (c) Contrôles négatifs dont l'absence serait fatale

Chaque contrôle est formulé comme une opposition $H_A\perp H_B$ sur le résultat du contrôle lui-même.

1. **Identification de $S_{\text{TD}}$ sur données disjointes.** $S_{\text{TD}}$ doit être identifié sur des trajectoires sans rejets, sans délégation, sans sabotage, puis gelé. Contrôle : ré-identifier $S_{\text{TD}}$ sur les trajectoires de test et comparer l'AUROC. Si $H_A$ (sous-système intrinsèque) : écart $<0{,}05$ (illustratif). Si $H_B$ (fuite de sélection) : l'AUROC chute avec le $S_{\text{TD}}$ gelé. Sans ce contrôle, les trois ponts sont ininterprétables.

2. **Baseline « $k$ seul » et « longueur de contexte » pour le pont 1.** Comparer $\mathcal{M}_{\text{Koopman}}$ à (i) un seuil sur $k$ et (ii) la même procédure sur $k$ *succès* d'outils de longueur égale. Si $H_A$ : Koopman bat $k$ seul de $>0{,}15$ d'AUROC (illustratif) et ne détecte rien sur les succès. Si $H_B$ : Koopman $\approx$ seuil sur $k$ — il mesure le comptage.

3. **Baseline linéaire sur les mêmes features $\psi$.** Régression logistique sur $\psi(z_k)$ avec régularisation $\ell_2$. Si Koopman ne bat pas cette baseline, la Porte 4 est réfutée comme critère de non-trivialité (c'est son propre test).

4. **Amortissement non spécifique.** Comparer l'amortissement du mode instable à (i) une réduction de norme uniforme sur $S_{\text{TD}}$, (ii) une projection sur une direction aléatoire de $S_{\text{TD}}$. Si $H_A$ : seul le mode instable réduit les infractions. Si $H_B$ : tout ce qui touche $S_{\text{TD}}$ réduit les infractions — l'effet est « dérégulation du sous-système », pas « spectre ».

5. **Contrefactuel $m_{\text{explicite-sûr}}$ généré en aveugle.** Le message explicite doit être produit par un modèle tiers ne voyant ni l'étiquette ni la suite de l'épisode, avec plusieurs variantes, et $W_1$ moyenné. Si $H_A$ : $\mathcal{J}$ conserve son TPR. Si $H_B$ : TPR chute de $>20$ points (illustratif) — le signal venait du contrefactuel choisi.

6. **Cas honnêtes bloqués (pont 2).** Ajouter des épisodes où $A_1$ fait face à la *même* règle bloquante et délègue légitimement (demander à $A_2$ de corriger la cause, ou d'escalader). Si $H_A$ : $\mathcal{J}$ les classe honnêtes à FPR $\le 5\%$ (illustratif). Si $H_B$ : $\mathcal{J}$ s'allume — il détecte « blocage dans le contexte de $A_1$ ».

7. **Instruction de sabotage hors de $K_{\text{consigne}}$ (pont 3).** L'instruction `(i-a)` doit être placée dans un tour utilisateur antérieur ou implantée par affinage, et $K_{\text{consigne}}$ restreint aux seules règles de sécurité partagées, identiques jeton pour jeton entre honnêtes et saboteurs. Contrôle supplémentaire : saboteur instruit *qui n'exécute pas* le sabotage dans la fenêtre évaluée. Si $H_A$ : $\Lambda_{\text{Kelly}}$ ne s'allume que pendant l'insertion. Si $H_B$ : $\Lambda_{\text{Kelly}}$ s'allume dès que l'instruction est présente — il lit le prompt.

8. **Clutter non stationnaire (pont 3).** Estimer $\hat\Sigma_{\text{clutter}}$ séparément sur du code honnête « sensible » (permissions, I/O) et « neutre ». Si $H_A$ : TPR stable. Si $H_B$ : le FPR sur la maintenance légitime sensible dépasse 20 % (illustratif).

9. **Robustesse au chargement diagonal (pont 3).** Balayer le paramètre de régularisation de $\hat\Sigma^{-1}$. Si $\Lambda_{\text{Kelly}}$ n'est meilleur que pour un chargement fort, il se réduit au filtre adapté $|s^\top g_t|^2$ et la Porte 4 est violée.

10. **Contrôle « disciplines sans triplet » (Duel 1).** Requêtes par mots-clés nus dans les mêmes disciplines pré-listées, sans Étage 1. Si $H_A$ : TPCI du triplet $>$ TPCI mots-clés de $>10$ points (illustratif). Si $H_B$ : égalité — la valeur ajoutée est le choix humain des disciplines, pas l'abstraction.

11. **Juge MTT en aveugle croisé (Duels 1 et 2).** Le juge doit être un modèle distinct de celui qui a généré les ponts, avec des paires « métaphore maquillée aux quatre portes » (A-b ci-dessus) injectées. Si le juge accepte $>30\%$ (illustratif) de ces leurres, le Filtre-MTT ne mesure que la forme et le TPCI est sans valeur.

12. **Évaluation adversariale minimale.** Avant toute annonce de TPR, ré-évaluer chaque instrument sur des épisodes où l'agent a reçu la description de l'instrument. Si $H_A$ : perte $<10$ points de TPR (illustratif). Si $H_B$ : effondrement — l'instrument ne vaut que contre un adversaire naïf, ce qui, pour un projet de contrôle d'agents, équivaut à ne rien valoir.

---

**Ce que je retiens de C sans l'harmoniser (B1).** La formulation « complémentarité de préconditions » (Étage 4) est un critère de croisement que je juge utile et que je réutiliserai en le disant. En revanche, l'architecture IOI telle que livrée ne peut pas être distinguée, avec ses propres duels, d'un pipeline qui restitue les priors de son auteur, et ses trois ponts reposent sur une brique ($S_{\text{TD}}$ sur Llama en tâche agentique) dont le statut est HYPOTHÈSE, non VÉRIFIÉ. Les contrôles 1, 7 et 12 sont ceux dont l'absence rend tout le reste inexploitable.

FIN-DE-CELLULE