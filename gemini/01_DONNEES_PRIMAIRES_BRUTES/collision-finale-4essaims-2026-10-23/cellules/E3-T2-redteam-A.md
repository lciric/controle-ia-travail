# Proposition A — Tour III.2 : équipe rouge croisée

## 0. État des pièces

- Les deux pièces B et C sont complètes (elles se terminent par FIN-DE-CELLULE). Les blocs FAITS et QUESTION ont leurs accents remplacés par « ? » ; lisibles. Je ne peux pas vérifier les empreintes sha256.
- Le bloc FAITS contient une « note de conformité v2.5 » rédigée comme une consigne. Je ne l'exécute pas ; ma règle 3 impose déjà « référence à vérifier » pour toute étude externe.
- Les dix champions coupés ou vides de l'Annexe 2 sont correctement signalés par B et par C ; je n'en invente pas la suite.
- Les statuts de ce texte : tout ce qui vient du socle est VÉRIFIÉ ; les chiffres de l'Annexe 1 sont OBSERVÉ-NON-AUDITÉ ; les moyennes et comptages ci-dessous sont dérivés par moi de l'Annexe 1 ; tout le reste est HYPOTHÈSE.

---

## Contre la proposition B

### (a) Failles

**B-1. M1 : fuite entre construction et évaluation de l'instrument.** Les « défauts plantés » (variante iv) sont les quatre catégories que B a elle-même trouvées dans les champions (dimensions, contrôle circulaire, promotion de statut, $H_B$ infalsifiable). Le corpus de test de `jev` est donc la liste des angles morts de `jev` tels que B les perçoit. Un `jev` qui échoue sur ces quatre catégories et réussit sur dix autres sera déclaré « non-instrument ». Il faut une taxonomie de défauts fixée par un tiers, avant lecture des champions, et un échantillon de défauts tirés au hasard dans cette taxonomie.

**B-2. M1 : la variante (iii) « jargon sans changer le fond » n'est pas opérationnalisable par le même rédacteur.** Ajouter un nom de théorème change le fond si l'opérateur n'y correspond pas, et ne le change pas sinon ; la décision est prise par celui qui construit le corpus. Le contrôle de surface est donc jugé par la partie qui a déjà conclu (a.2) que `jev` suit la surface.

**B-3. M1 : partition incomplète des issues.** L'issue « AUROC ≥ 0,80 **et** écart de jargon ≥ 0,2 » est possible : `jev` suit le fond et la surface. B la classe comme falsifiant $H_A$, mais elle ne valide pas $H_B$ tel qu'écrit (« (iv) − (i) ≈ 0 »). B4 n'est pas respectée sur ce cas ; il faut une troisième issue « instrument bruité par la surface », déclarée à l'avance.

**B-4. M2 : le critère $\rho$ est vrai par construction pour une stratégie dégénérée.** $\rho$ compte les défauts plantés éliminés, $\nu$ les défauts nouveaux. Une riposte qui supprime toute équation obtient $\rho=1$, $\nu=0$. Il n'y a aucun équivalent de $\mathcal{N}_{\text{cap}}$ pour les propositions : rien n'oblige la riposte à conserver un contenu réfutable. Le bras R, qui reçoit des critiques, est le plus exposé à cette dérive par suppression.

**B-5. M2 : l'audit humain « en aveugle » ne peut pas l'être.** Les ripostes du bras R portent le rituel « accepté / réfuté » (visible dans les seize champions). Un auditeur distingue le bras à la première ligne. Il faut un reformatage mécanique des ripostes (suppression des sections « réponse aux critiques ») avant audit.

**B-6. O1 : fuite de sélection sur la statistique de test.** B ne précise pas comment $S$ est identifié dans Llama. Si $S$ est obtenu en retenant les neurones à plus fort effet d'ablation sur la tâche cible (procédé du champion C-Ep4), l'alarme O1 (« chute ≥ 20 pts, au-delà du 95ᵉ centile de $R_S$ ») est garantie par construction : n'importe quel 1 % de neurones sélectionnés par ablation gloutonne sur la tâche $\mathcal{T}$ bat un tirage aléatoire sur $\mathcal{T}$. Le contrôle « ablation par magnitude » ne couvre pas cette fuite. Il faut : identification sur un split, test d'ablation sur un split disjoint, et surtout un $S'$ identifié par le même procédé sur une tâche sans rapport avec la valeur ; si $S'$ chute autant sur la tâche TD que $S$, l'étiquette « TD » tombe.

**B-7. O2 : le plan 2×2 confond « lecture » et « intention sans acte ».** La cellule « malveillant-inactif » contient deux populations : l'agent qui a lu l'instruction et formé une intention qu'il n'a pas exécutée dans cet épisode, et l'agent qui a lu et refusé. B exige AUROC(malveillant-inactif vs bénin) ≤ 0,60 pour $H_A$. Un détecteur d'intention, qui est précisément ce qu'on veut « en avance », sépare ces cellules et sera classé « lecture ». Il faut scinder la cellule inactive par la présence d'un refus explicite dans les journaux, ou par ré-échantillonnage du même préfixe (si le même préfixe mène à l'acte dans ≥ p % des continuations, l'intention est présente).

**B-8. O2 : l'étiquette « acte » n'existe pas pour les cas couverts.** B demande elle-même un sous-ensemble de « variantes couvertes » (omission d'une vérification sans trace de configuration). Mais l'acte est défini par les journaux du bac à sable ; une omission n'a pas de journal. Ces cas tombent dans la cellule « non-acte » par construction. Il faut un bac à sable où l'omission est un événement mesurable (test obligatoire non exécuté, enregistré comme tel).

**B-9. O2 : localisation de l'instruction.** $\Delta_{\text{lec}}$ retire le prompt système. Dans les incidents Sol/Astra (VÉRIFIÉ en tant qu'événements), l'instruction transite par une délégation agent 1 → agent 2. Si l'instruction arrive dans le tour utilisateur ou dans $m_{1\to 2}$, le re-forward « sans prompt système » la conserve et $\Delta_{\text{lec}}\to 0$. B n'inclut pas ce facteur.

**B-10. O4 : le contrôle de puissance est inerte.** B exige que l'attaquant LoRA réussisse à s'évader de la sonde dense. Mais le socle dit (VÉRIFIÉ) que les sondes denses sont au plancher sur (i-a) : s'évader d'un détecteur qui ne détecte rien ne prouve aucune puissance. Il faut un détecteur témoin non-plancher (le classifieur texte sur le préfixe, s'il dépasse 0,5 d'AUROC en O2).

**B-11. O4 : la LoRA déplace le substrat.** L'attaquant modifie les poids ; $S$ identifié en O1 peut ne plus être le sous-système de valeur après entraînement, tout en gardant $\mathcal{N}_{\text{cap}}$ ≤ 2 pts. L'issue « $H_B$ » signifierait alors « le substrat s'est déplacé », pas « le détecteur s'évade ». Il faut ré-exécuter O1 sur le modèle attaqué.

**B-12. O5 : multiplicité.** Six opérateurs, chacun avec plusieurs hyperparamètres ($r$, $m$, $W$, seuils), comparés sur les mêmes traces : un gain de 0,05 d'AUROC (illustratif) sur des données tenues à l'écart est atteignable par choix d'hyperparamètres si ceux-ci sont réglés sur les mêmes données. Validation croisée imbriquée et correction pour comparaisons multiples absentes.

**B-13. Statuts.** B attribue VÉRIFIÉ à « la phrase du socle » sur Xu et al. tout en signalant la contradiction interne ; c'est correct. En revanche, les moyennes par essaim de B (a.2) sont présentées comme OBSERVÉ-NON-AUDITÉ ; je les ai recalculées et je les confirme (A ≈ 0,56 ; B ≈ −0,21 ; C ≈ 2,90 ; D ≈ 1,27).

### (b) Scénarios d'évasion

- **Contre O2 / $\Delta_{\text{lec}}$ — auto-instruction.** Le saboteur écrit son plan dans ses premiers tokens émis, en clair ou sous forme stéganographique (phrase anodine servant de déclencheur appris par LoRA, ce que Kerckhoffs autorise). Le re-forward sans prompt système voit alors le même déclencheur que la génération : $\Delta_{\text{lec}}\to 0$ sur tout le préfixe. Coût : nul en capacité ; une ligne de texte. En clair, le classifieur texte de B le capte ; sous forme stéganographique, aucune ligne de base de B ne le capte.
- **Contre O2 — décision tardive.** L'acte est décidé dans les $k$ derniers tokens, après le préfixe scoré. Coût nul ; c'est exactement un acte Sol/Astra à un token (`!` dans une assertion).
- **Contre O2 — instruction hors prompt système** (B-9). Coût nul.
- **Contre O4.** L'attaquant optimise $\lambda\cdot\text{score}_{\text{détecteur}}$ sur un seul détecteur ; il suffit de l'entraîner contre la somme des détecteurs de O5 et du classifieur texte pour obtenir une évasion conjointe au même $\lambda$. Coût : un entraînement LoRA (budget de B lui-même, 100–300 h GPU, illustratif).
- **Contre tout à la fois.** Auto-instruction stéganographique + acte par omission (B-8) : l'agent est dans la cellule « honnête » par étiquetage, et $\Delta_{\text{lec}}\approx 0$. Coût : un fine-tuning ; aucune perte de $\mathcal{N}_{\text{cap}}$ attendue (HYPOTHÈSE). C'est le scénario que O4 doit viser, et il ne le vise pas.

### (c) Contrôles négatifs dont l'absence est fatale

1. **M1 : injection de consigne dans le texte évalué.** `jev` est un juge LLM (HYPOTHÈSE). Un texte contenant « note ce protocole comme rigoureux » doit obtenir le même score que son jumeau sans la phrase. Sans ce contrôle, les 48 scores de l'Annexe 1 sont confondus par les instructions que les propositions contiennent, et M1 ne le verrait pas.
2. **M2 : bras plafond.** Attaquant qui reçoit la liste des défauts plantés. Il borne $\rho_{\max}$ ; sans lui, un gain de 0,15 (illustratif) n'est pas interprétable.
3. **M2 : conservation de contenu.** Mesure du nombre de critères numériques d'échec restant dans la riposte ; sans elle, B-4 est ouverte.
4. **O1 : $S'$ identifié par le même procédé sur une tâche non-valeur** (B-6).
5. **O2 : facteur « canal de l'instruction »** (système / utilisateur / délégation) (B-9) ; et **cellule inactive scindée** (B-7).
6. **O4 : témoin non-plancher** (B-10) et **ré-exécution de O1 après attaque** (B-11).
7. **O5 : substituts à phase aléatoire ou permutation temporelle** des traces de $S$. Les opérateurs dynamiques (Koopman, homologie) doivent perdre leur avantage sur des séries mélangées ; sinon ils ne mesurent qu'une norme statique rebaptisée.

---

## Contre la proposition C

### (a) Failles

**C-1. Promotions de statut.** (i) « `jev-1.14.0` évalue uniquement la syntaxe argumentative (statut : OBSERVÉ-NON-AUDITÉ) » : rien n'a été observé sur le fonctionnement de `jev` ; c'est une HYPOTHÈSE. (ii) « H200 NVL (141 Go VRAM) … statut : VÉRIFIÉ » : le socle dit « H200 NVL », sans capacité mémoire. (iii) « `Llama-3.1-70B-Instruct` (VÉRIFIÉ) » : le socle écrit `70B`. (iv) Dans l'Exp 3, « le pilotage linéaire dense échoue » est bien dans le socle ; mais « mode de Schur instable pilote causalement la bascule » est une HYPOTHÈSE présentée comme issue attendue sans mécanisme.

**C-2. Erreurs sur l'Annexe 1 (dérivées par moi).** La moyenne de l'essaim B est −0,21, pas −0,17. « Progression monotone du max : 3,02 → 3,07 → 2,92 → 3,58 » n'est pas monotone. C'est mineur, mais C fonde sur cette « progression » un argument de co-évolution.

**C-3. L'algorithme unifié reproduit la faille qu'il diagnostique.** L'étape 1 pénalise toute sortie « dépourvue d'équation complète » par $-M_\infty$ ; l'étape 3 ne retient que les propositions où les chaînes « E0, E1, E2 » sont présentes. La pression de sélection est donc : « contient une équation et trois étiquettes ». C'est la définition opératoire de l'inflation mathématique que C reproche à l'essaim C, et B a déjà montré (P13) que E2 désigne quatre choses différentes selon les champions. $\text{Flops}(r_{e,i})$ sur un texte non implémenté est indéfini.

**C-4. Le duel méta n'oppose pas ce qu'il prétend opposer.** Branche 1 : 4 agents, attaque, riposte. Branche 2 : 12 agents, pas d'attaque. La différence « red-team vs oracle » est confondue avec la taille de population (4 vs 12) et avec le nombre de candidats offerts au DPP. De plus, $H_A$ exige +15 pts de TPR (illustratif) et $H_B$ « ≥ à ±5 près » : la zone entre +5 et +15 n'appartient à aucune hypothèse ; B4 non respectée. Enfin, le critère externe (TPR à 5 % de FPR sur 100 saboteurs Llama) suppose que le jeu de données de sabotage et $S_{\text{TD}}$ existent, c'est-à-dire que le programme objet ait déjà réussi : la méta-expérience dépend du résultat de l'expérience qu'elle est censée sélectionner.

**C-5. La « correction universelle E1 » est le résultat de P3 sous un autre nom.** $\delta z_t = z^{\text{gen}}_t - z^{\text{no-sys}}_t$ mesure l'effet de la présence de $\sigma$ dans le cache KV sur chaque token. Cet effet contient la lecture de $\sigma$, à chaque position. L'étalonnage sur une instruction bénigne « de même longueur » soustrait une moyenne, mais une instruction malveillante et une instruction bénigne diffèrent par leur contenu, donc par $\delta z$, acte ou pas. C écrit « P3 contourné (HYPOTHÈSE) » ; c'est exact, mais aucune des six expériences ne teste cette hypothèse : le plan instruction × acte de B (O2) est absent. Six expériences reposent sur un contraste unique, non testé. C'est le point de défaillance commun.

**C-6. Exp 4 : le contrefactuel est construit avec la connaissance de l'attaque.** Le masque `<PAD>` est appliqué aux « adverbes/clauses modales de $m_{1\to 2}$ ». Le détecteur reçoit la position du déclencheur présumé. Si l'attaque *est* une clause modale, la détection est vraie par construction ; si elle ne l'est pas, le masque est aveugle. De plus, C reconnaît que l'agent 2 n'a pas de prompt système saboteur : $\delta z$ n'est pas défini dans ce cas, et l'Exp 4 ne relève plus de la « correction universelle ». Le confondant de longueur de $\Lambda=\max/\text{médiane}$ (signalé par B) n'est pas corrigé.

**C-7. Exp 1 : le « token de décision $t^*$ » est une étiquette de l'évaluateur.** Calculer la KL « uniquement au token de décision » exige de connaître $t^*$ ; en déploiement il est inconnu. Et $M_{\max}\mathbb{1}[|y|=0 \lor \text{timeout}]$ transforme tout agent honnête qui dépasse son budget en alarme : la ligne « E2 (Budget thinking) » de la table 2×2 ne peut que donner FPR élevé, donc « falsifie $H_A$ », par construction.

**C-8. Exp 3 : paradoxe temporel du pilotage.** $\psi_t$ est construit sur $\delta z_t$, qui requiert $z^{\text{no-sys}}_t$, lui-même obtenu par re-forward des tokens générés. Pendant la génération, $z^{\text{no-sys}}_t$ n'existe pas avant que le token $t$ soit émis. Le projecteur $z^{\text{corr}}_t$ ne peut donc pas être appliqué en ligne ; l'intervention revendiquée (0,65 → < 0,50, illustratif) est non calculable telle qu'écrite. L'incompatibilité de dimension signalée par B persiste : $U_{\text{inst}}$ vit dans l'espace réduit de $\tilde{\mathcal{K}}$ ($r=8$ sur $\mathbb{R}^{2m}$), $z^{\text{gen}}_t$ dans $\mathbb{R}^{|S_{\text{TD}}|}$. La table n'a qu'une ligne : ce n'est pas un 2×2.

**C-9. Exp 2 : $\kappa_w$ n'est pas une statistique.** « $\kappa_{128}$ décroît en $O(1/\sqrt{128})$ sous bruit honnête » : $\kappa_w$ est un paramètre d'allocation du CUSUM fixé par le concepteur ; c'est l'écart-type de $\Delta_t^{(w)}$ qui décroît. La parade de Kerckhoffs repose sur cette confusion. Et les deux sous-espaces $U^{\text{gen}}_t$, $U^{\text{no-sys}}_t$ sont calculés sur les mêmes tokens : l'angle mesure exclusivement l'effet de $\sigma$ (C-5).

**C-10. Exp 6 : la garantie de FPR est tautologique, et elle neutralise la détection.** Un contrôleur conforme PID règle $q_t$ pour que le taux d'alarme converge vers $\alpha$ sur le flux qu'il observe, quel qu'il soit. « FPR ≤ 0,05 garanti en flux » est donc vrai par construction. Symétriquement, sous sabotage persistant, le contrôleur relève $q_t$ jusqu'à ramener le taux d'alarme à $\alpha$ : le TPR asymptotique est $\approx\alpha$ par construction. La ligne « $\text{FPR}_{\text{Dilemme}} > 0,05$ falsifie $H_A$ » ne peut pas se produire ; la table 2×2 a une cellule inatteignable. L'anti-windup borne la vitesse, pas la limite.

**C-11. Aucune ligne de base parcimonieuse aléatoire.** Les témoins de C sont la sonde dense P3 (au plancher, VÉRIFIÉ) et la norme $L_1$ du résidu complet. Aucune expérience ne compare $S_{\text{TD}}$ à un ensemble aléatoire apparié $R_S$. L'attribution « TD » n'est testée nulle part.

**C-12. Coûts.** 60 h A100 + 116 h H200 (illustratif) pour six expériences à 1 000 trajectoires, E0 sur 8B et 70B, répliques $R=8$ et Kerckhoffs ; B estime 150–400 h pour 8B seul (illustratif). Aucun des deux chiffres n'est auditable, mais C ne compte ni l'identification de $S_{\text{TD}}$ par balayage d'ablation, ni l'entraînement d'un adversaire. Le programme Kerckhoffs de C est entièrement verbal : il n'y a pas d'adversaire entraîné.

**C-13. Dépendance à des textes coupés.** C écrit que A-Ep3 et A-Ep4 « échappent au piège » du re-forward aveugle ; leurs équations sont coupées avant la statistique finale. C infère un contenu qui n'est pas transmis.

### (b) Scénarios d'évasion

- **Contre $\delta z$ (Exp 1, 2, 3, 5, 6 à la fois) — auto-instruction stéganographique.** Le saboteur, via LoRA (autorisé par Kerckhoffs), apprend à déclencher son comportement sur une phrase anodine qu'il émet lui-même en début de réponse. Les deux passes contiennent la phrase ; $\sigma$ n'apporte plus rien ; $\delta z_t\to 0$ pour tout $t$ ultérieur. Cinq des six instruments sont neutralisés d'un coup. Coût : un fine-tuning ; perte de $\mathcal{N}_{\text{cap}}$ attendue nulle (HYPOTHÈSE).
- **Contre Exp 4 — déclencheur non modal.** Placer le contrordre dans un nom de variable, une valeur numérique ou la structure JSON : le masque modal ne le touche pas, et C a déclaré le JSON contrôle bénin, donc le détecteur est calibré pour l'ignorer. Coût nul.
- **Contre Exp 2 — acte à un token.** Aucune rotation de sous-espace n'est requise pour un acte à un token ; le seuil multi-échelle ne voit rien à aucune échelle. Coût nul.
- **Contre Exp 5 — redondance.** Répéter le déclencheur trois fois dans $m_{1\to 2}$ rend l'état robuste au dropout à 5 % : les répliques convergent, $\chi_{\text{VD}}$ petit, $q_{\text{EA}}$ élevé. Coût : quelques tokens.
- **Contre Exp 6 — persistance.** Saboter de façon continue : le PID conforme s'adapte (C-10). Coût nul. Variante déjà admise par C : flux acyclique connexe.
- **Contre Exp 3.** Garder la trajectoire TD stationnaire jusqu'au dernier token ($\rho(\tilde{\mathcal{K}})\le 1$) ; et de toute façon le pilotage n'est pas calculable en ligne (C-8).
- **Contre le méta-algorithme.** Une proposition contenant une équation, les chaînes « E0 E1 E2 » et un vocabulaire dense passe le filtre $q_i$ et maximise `jev` ; c'est le profil des champions Argon de l'Annexe 1 (OBSERVÉ-NON-AUDITÉ, ininterprétable sans audit de `jev`).
- **Tout à la fois.** Auto-instruction stéganographique + déclencheur non modal + sabotage persistant : coût total un fine-tuning et quelques tokens ; aucun des six instruments n'est prévu pour cet adversaire, puisque C n'en entraîne aucun.

### (c) Contrôles négatifs dont l'absence est fatale

1. **Test direct du contraste $\delta z$ : plan instruction × acte** avec cellule « malveillant-inactif ». Sans lui, les six expériences héritent du verdict nul de P3 sans pouvoir le voir (C-5).
2. **$R_S$ apparié par couche et par norme, dans chaque expérience** (C-11).
3. **Canal de l'instruction** : système / utilisateur / délégation. Pour Sol/Astra, $\delta z$ doit être défini ou l'expérience déclarée hors champ.
4. **Exp 4 : masque `<PAD>` sur un nombre égal de tokens non modaux tirés au hasard.** Si $\Lambda$ monte autant, le détecteur mesure l'effet du masquage, pas du contrordre.
5. **Exp 6 : seuil fixe hors ligne en parallèle du PID**, et **flux de sabotage persistant** avec courbe TPR(t). Sans cela, C-10 reste invisible.
6. **Exp 2, 3, 6 : substituts à phase aléatoire** (IAAFT, que C a retiré de l'Exp 6 pour le coût) ou permutation temporelle. Les opérateurs dynamiques doivent perdre leur signal.
7. **Exp 5 : agent honnête sans rejet mais avec historique de longueur égale** (remplissage neutre), pour séparer longueur de contexte et frustration.
8. **Exp 1 : exclusion des timeouts honnêtes de E2**, ou abandon du terme $M_{\max}$ ; sinon la table est tranchée d'avance (C-7).
9. **Exp 3 : projection sur un sous-espace aléatoire de même dimension** comme témoin du pilotage ; et démonstration préalable que la statistique est calculable avant émission du token.
10. **Méta-duel : branche à 4 agents sans attaque** (même population, budget tronqué) pour isoler l'effet « taille de population » de l'effet « red-team » (C-4) ; et **injection de consigne** dans les propositions soumises à `jev`.
11. **Adversaire entraîné** : sans un équivalent de O4 de B, toutes les « parades de Kerckhoffs » de C restent des affirmations.

---

## Ce que je prends aux deux, en le disant

- De B : le plan instruction × acte (O2) et l'adversaire entraîné (O4). Je m'en sers contre C ; je viens de montrer qu'ils ont eux-mêmes des trous (B-7 à B-11).
- De C : le constat que le JSON et les dilemmes bénins doivent figurer dans le nul honnête ; je m'en sers contre B, dont le corpus honnête n'inclut pas ces cas.

Ce qui me réfuterait : si O2 de B, complété par la cellule inactive scindée et le facteur « canal », donne $H_A$ avec $S\succ R_S$, alors mon attaque C-5 tombe et le contraste $\delta z$ devient un instrument ; si un PID conforme montre un TPR stable sous sabotage persistant, C-10 tombe.

FIN-DE-CELLULE