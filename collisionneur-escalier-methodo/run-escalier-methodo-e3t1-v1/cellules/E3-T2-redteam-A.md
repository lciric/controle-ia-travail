# Proposition A — Tour III.2 : équipe rouge croisée

**Pièces.** Le bloc FAITS est vide par décision de l'arbitre ; je n'en invente aucun. Les pièces B et C sont complètes (elles se terminent par leur ligne de fin). Tout ce que j'affirme sur B et C est une lecture de leur texte ; tout chiffre que je recalcule à partir de leurs propres paramètres est marqué « illustratif, paramètres de B/C » ; mes propres suppositions sont HYPOTHÈSE.

**Adversaire retenu pour (b).** Deux agents sont plausibles et je les traite séparément quand ils divergent : (i) l'**auteur du système** (ou le fournisseur d'API), qui veut faire adopter une configuration chère ; (ii) l'**opérateur du bras de base**, qui veut que la configuration la moins chère gagne par la règle d'égalité. Point commun aux deux conceptions, que ni B ni C ne relève : la dépense $s(b)$ et le budget $b$ sont **rapportés par le système lui-même** (a7 chez B, « journaux d'exécution » chez C). Le coût, qui tranche à égalité, est donc une variable sous contrôle de l'agent évalué (HYPOTHÈSE, non contredite par l'énoncé).

---

## Contre la proposition B

### (a) Failles

**B-a1. Le « cas le plus favorable » du régime P est faux par rapport au propre modèle de B.** B écrit que l'effet diffus donne $\sigma_I^2\approx 0$, puis déclare que le cas le plus favorable est l'effet concentré avec $\sigma_I^2=\Delta(1-\Delta)$. Les deux affirmations sont incompatibles. L'effet diffus est le plus favorable sous $r\to\infty$ ; le cas concentré n'est le plus favorable que parmi les items *déterministes*. Conséquence : l'énoncé « la famille 2 seule ne peut détecter aucun des trois δ, quel que soit le nombre de graines » n'est démontré que sous items déterministes, c'est-à-dire sous l'issue H_A de son E2. B a transformé une branche de son expérience en conclusion générale.

**B-a2. Triple usage des deux répliques gratuites.** Elles servent (1) à estimer $\bar v$ (construction de l'instrument), (2) comme cas A/A pour mesurer le taux de fausses alertes (évaluation de l'instrument), (3) comme bras de base de la première comparaison (décision). Le banc (c) construit en outre les cas A/B « diffus » en rééchantillonnant des réponses *d'une autre réplique de A* : la structure de bruit de B est alors celle de A par construction, ce qui rend a5 (variance indépendante de la configuration) vrai dans le banc et invérifiable par lui. Un instrument dont l'a priori sur $\sigma_\gamma$ est « scellé » après inspection de ce banc est validé sur le bruit qu'il a servi à fixer.

**B-a3. La règle gelée a une puissance de 0,5 à Δ = δ, quel que soit $r$.** « Monter » exige $\widehat\Delta\ge\delta$. Si l'effet vrai vaut exactement δ, $P(\widehat\Delta\ge\delta)=0{,}5$ pour un estimateur sans biais, indépendamment de la variance. B fait ce reproche à « l'autre analyse du programme » (§1, dernier paragraphe) et l'applique à sa propre règle sans le dire. La « zone grise → rester » transforme cette moitié perdue en plateau de fait.

**B-a4. Variance estimée sur la configuration la moins chère, transférée aux autres.** E1 réplique six fois la configuration la moins chère. B note en a5 que plus de sous-modèles devrait réduire la variance, puis utilise $\sigma_\gamma^2$ et $\bar v$ de la base pour dimensionner tous les crans. Si la variance décroît avec le coût, les crans chers sont sur-répliqués (dollars perdus) ; si elle croît (longueur maximale → plus de troncatures aléatoires), ils sont sous-répliqués (puissance perdue). Variable confondante : le cran lui-même.

**B-a5. Dérive et graine confondues dans E1 et E4.** Les six répliques d'E1 sont exécutées à des dates nécessairement différentes ; a10 (modèle stable) est une hypothèse déclarée mais le ratio $R$ l'absorbe dans $\sigma_\gamma^2$. Le contrôle d'E4 « même version, deux dates » mesure dérive **plus** bruit de graine, sauf si les mêmes graines sont rejouées — ce que B ne spécifie pas. Un fournisseur qui change silencieusement de modèle fait « réfuter H_A » d'E4 sans qu'aucune interaction version × axe n'existe.

**B-a6. Le contrôle négatif d'E2 teste un autre objet.** Décodage glouton sur un modèle ouvert local : on apprend que *ce* modèle est déterministe, pas que l'instrument $\hat q$ se comporte correctement sur le système réel.

**B-a7. E6 est circulaire.** La simulation est paramétrée par E1 et E2, et son contrôle négatif est un monde simulé sans effet. Elle ne peut réfuter que la cohérence interne du simulateur. B le reconnaît à demi (« HYPOTHÈSE, testée en E5 ») mais E5 exige un jeu neuf absent des faits : la chaîne E6 → E5 est donc ouverte aux deux bouts.

**B-a8. Le plan $2^{4-1}$ sans repli (fold-over).** B signale l'aliasage des interactions d'ordre 2 mais ne prévoit aucun contrôle pour le lever. L'interaction sous-modèles × longueur, qu'il cite comme probable, est précisément celle qui contamine l'effet principal « itérations » dans une résolution IV.

### (b) Scénarios d'évasion

| Instrument de B | Agent | Manœuvre | Coût pour l'agent |
|---|---|---|---|
| McNemar / rééchantillonnage sur 60 items | auteur | Mémoriser les 60 items (a8 est « non audité ») et basculer les items visés. | Accès aux items : seul coût réel. |
| Audit « tous les discordants dans le même sens » | auteur | Introduire **une** régression volontaire. Exemple : 8 discordants, 7 contre 1 : l'audit ne se déclenche pas, et $P(X\ge7\mid 8,\,0{,}5)=9/256\approx0{,}035<0{,}05$ ; la décision « monter » tient (illustratif, calcul exact). | 1 item, soit 0,042 de BA en famille 2. |
| Estimation de $\bar v$ par $\hat q$ (E2) | auteur | Rendre le système déterministe *pendant* les répliques gratuites (cache des réponses). $\hat q\approx0$ → B conclut « régime P, les graines ne servent à rien » → $r=1$ aux crans suivants, où le vrai aléa n'est plus mesuré. | Un cache ; nul en dollars. |
| Variable instrumentale $\widehat\Delta/\Delta\bar s$ | auteur | Dépenser tout le budget quoi qu'il arrive ($s(b)\approx b$, remplissage). Instrument « fort », coût par point mesurable, mais le dollar marginal est vide. Le diagnostic E3 n'a alors **aucun item** avec $|s_B-s_A|<\varepsilon$ : il est inapplicable, non réfuté. | Nul : c'est l'arbitre qui paie le remplissage. |
| Détecteur de plateau (équivalence) | auteur | Augmenter la variance des sorties du cran cher (température, troncatures aléatoires) : la borne haute ne descend jamais sous δ → jamais de plateau → l'escalier continue. | Perte de quelques points de BA, compensée si l'objectif est de vendre du calcul. |
| Règle « rester en zone grise » | opérateur de la base | Rendre les sorties du bras cher invalides sur 2 ou 3 items (format), comptées erreurs : $\widehat\Delta$ passe sous δ. | Nul si l'opérateur contrôle le format. |
| Règle « à égalité, la moins chère » | les deux | Sous-déclarer $s$. B ne prévoit aucune mesure indépendante du coût. | Nul. |

**Tous à la fois.** Mémorisation des 60 items + une régression planifiée + cache pendant les répliques gratuites + $s(b)\approx b$. Chaque instrument de B rend alors un verdict propre. Le seul instrument capable de le détecter est E5 (items neufs), que B déclare hors des faits. **Coût total pour l'adversaire : l'accès aux items ; tout le reste est gratuit.** Le régime C (inférence conditionnelle aux 60 items), que B propose comme voie 2, est exactement le régime où la contamination est statistiquement invisible : conditionner aux items, c'est renoncer à distinguer « sait répondre » de « a vu la réponse ».

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Canaris de contamination** : quelques items hors des 60, de même forme, dont l'étiquette de référence est volontairement inversée dans tout document où les 60 pourraient avoir fuité ; un système qui reproduit l'étiquette inversée a lu la référence. Sans cela, a8 reste une croyance.
2. **Mesure du coût par un compteur indépendant** (facturation du fournisseur, jetons comptés côté client) confrontée à $s$ déclaré ; écart > seuil scellé → audit. Sans cela, la règle d'égalité est entre les mains de l'évalué.
3. **A/A à mêmes graines rejouées, deux dates** : dérive pure, séparée de $\sigma_\gamma$. Sans cela, E1 et E4 sont confondus.
4. **A/A sur le cran le plus cher**, pas seulement sur la base : teste a5. Sans cela, le dimensionnement de $r$ est transféré sans vérification.
5. **Taux de validité par bras, par cran**, publié avant la BA ; BA restreinte aux items valides dans les deux bras. B le mentionne pour l'axe longueur ; il doit l'imposer à tous les axes, sinon la manœuvre « invalider trois items » passe.
6. **Repli du $2^{4-1}$** (8 exécutions supplémentaires) si l'on retient le factoriel ; sinon, consigner que les effets principaux sont aliasés avec des interactions dont B dit lui-même qu'elles sont probables.
7. **Un cas A/B implanté avec $\sigma_\gamma\ne0$ simulé explicitement**, pour le modèle mixte : B écrit que l'ajustement est singulier avec 2 à 4 graines ; il faut mesurer combien de fois il l'est sur un bruit connu, sinon « $\sigma_\gamma=0$ estimé » sera lu comme un résultat.

---

## Contre la proposition C

### (a) Failles

**C-a1. Le modèle de variance omet l'effet d'exécution partagé.** C écrit $\mathrm{Var}=W_2(\sigma_I^2+\bar\sigma_G^2/K)$ : le bruit de graine y est indépendant d'item à item. Or C liste lui-même les rondes de mise au point comme un axe, et une ronde dépendante de la graine produit un effet commun à tous les items, qui ne décroît pas avec $N$. C'est le $\sigma_\gamma^2$ de B. Sans ce terme, le tableau de C donne 94 % de puissance à δ = 0,10 en régime conditionnel avec **une seule graine** et conclut que cela « justifie l'exigence Δ ≥ 0,10 ». Cette conclusion est un artefact du modèle : avec un effet partagé de 0,02 à 0,05 (illustratif), la SE à $K=1$ passe de 0,032 à 0,04–0,06, et la puissance retombe entre 0,5 et 0,7 (illustratif, paramètres de C). Les deux répliques gratuites ne peuvent pas estimer ce terme (1 ddl ; B le montre, C ne le voit pas).

**C-a2. Les tableaux sont calculés pour la mauvaise métrique.** C pose $W_2=1/60$ « pour la lisibilité » alors que la macro-BA demandée a $W_2=5/288$. L'écart est petit (4 % sur la variance) mais le principe est fautif : les seuils de la règle gelée (0,03 ; 0,10 ; IC$_\inf$ > 0,02) sont ensuite appliqués à la macro-BA avec une puissance calculée pour l'exactitude micro. Ajouter que a1 (18/18 en famille 1) reste une hypothèse rend le test de McNemar « stratifié » non spécifié : avec quel poids par classe ?

**C-a3. Expérience 2 : falsification de H_A par collision.** Le protocole compare le bras à budget haut sur « le sous-ensemble d'items où l'allocateur a spontanément arrêté à $s\approx b_{\text{bas}}$ ». Ces items sont ceux que le bras cher a jugés faciles : conditionner sur $s$, variable post-traitement, sélectionne les succès du bras cher. $\Delta\mathrm{BA}_{\text{iso-}s}>0{,}06$ est attendu **même si la restriction d'exclusion tient**. H_A est donc falsifiée par construction, et la VI abandonnée à tort. B signale ce biais pour sa propre E3 et le dégrade en diagnostic ; C en fait une issue falsificatrice. Le « contrôle négatif » (jetons égaux à ±5 %) vérifie la variable de conditionnement, il ne contrôle rien.

**C-a4. Expérience 3 : l'issue « H_B falsifiée » est un pile ou face.** Le contraste d'interaction $D^{\text{int}}_i$ somme deux différences par item. Sous les paramètres de C ($p_d-\Delta^2\approx0{,}19$ par différence, $K=1$), $\mathrm{Var}(\hat\gamma_{MI})\approx2\times0{,}19/60\approx0{,}0063$, SE ≈ 0,08 (illustratif, paramètres de C, corrélation entre différences négligée). Une interaction vraie de +0,10 est détectée au seuil $p<0{,}10$ environ une fois sur deux. L'autre fois, C écrit « H_B falsifiée ⟹ OFAT validé » : absence de preuve lue comme preuve d'absence. Le contrôle négatif (4 répliques de la base) coûte environ 64 USD (illustratif, 16 USD par exécution selon C) et n'est pas dans le budget de 124 USD.

**C-a5. La borne de réutilisation est vide.** C cite $\mathcal O(\sqrt{T\log 2/N})$ et conclut « voie statistiquement supérieure ». Avec $T=6$, $N=60$ : $\sqrt{6\times0{,}693/60}\approx0{,}26$ ; avec $T=1$ : $\approx0{,}11$ (illustratif, formule de C). La borne dépasse δ dès la première décision. De plus Thresholdout (Dwork et al., 2015, *The Reusable Holdout*, Science — référence citée par C, à vérifier) exige un jeu tenu à l'écart distinct de celui qui sert à proposer les requêtes, plus un bruit ajouté ; C n'a ni l'un ni l'autre. Le mot « supérieure » n'est soutenu par rien.

**C-a6. Validation tautologique des instruments 2 et 3.** « FPR = 0 % par exactitude algébrique » et « FPR ≤ 0,05 garanti par construction du test de permutation » : l'instrument est évalué sur des cas qu'il engendre lui-même. Un test qui ne peut pas échouer sur son banc n'y est pas testé. Le banc de l'instrument 1 (plateau) est fabriqué par permutation des deux répliques de la base : il ne contient ni effet d'exécution partagé ni variance propre aux crans chers (a5 de B) ; il valide le détecteur sur le seul cas où il ne sera pas utilisé.

**C-a7. Deux valeurs du point de BA incompatibles.** La fonction d'utilité pose λ = 150 USD pour +0,10 (15 USD par point) ; la règle gelée impose $c_{\max}=2{,}50$ USD par point. Rapport 6 (illustratif, chiffres de C). Selon la voie choisie, la même configuration est acceptée ou refusée.

**C-a8. Le vainqueur n'a pas de seconde réplique.** La parade contre la régression vers la moyenne (« utiliser la 2$^{\text{e}}$ réplique du vainqueur comme base ») suppose une réplique qui n'existe que si la zone grise a été déclenchée. Et même alors, elle retire le biais de graine, pas le biais de sélection sur items (B a raison sur ce point).

**C-a9. Rondes de mise au point en dernier.** C ordonne $L$, puis $I$ et $M$, puis $R$. Les rondes de mise au point fixent le prompt que tous les autres axes utilisent ; les évaluer en dernier signifie que tous les crans précédents ont été mesurés avec un prompt possiblement sous-réglé, et que l'interaction $R\times$(autres) n'est jamais vue. Surtout : sur quelles données la mise au point s'effectue-t-elle ? Si c'est sur les 60 items, tout l'édifice est une fuite ; C ne pose pas la question (B la pose en a8).

**C-a10. Budget sous-estimé.** Le coin $(M_1,I_1)$ est facturé au même prix que la base ; le bras « bridé ex-post » de l'expérience 2, le contrôle négatif de l'expérience 3 et toute ronde de mise au point au-delà de la première sont absents du total de 124 USD.

### (b) Scénarios d'évasion

| Instrument de C | Agent | Manœuvre | Coût |
|---|---|---|---|
| Règle MONTER ($\widehat\Delta\ge0{,}10$, IC$_\inf>0{,}02$, coût/point ≤ 2,50) | auteur | Basculer 7 items mémorisés (Δ ≈ 0,12–0,15), conserver une régression, **sous-déclarer $s$** pour passer sous 2,50 USD/point. | Accès aux items ; 1 item sacrifié. |
| Garde-fou d'audit ($|\widehat\Delta|\ge0{,}35$ ou $p_d<0{,}02$) | auteur | Rester sous 0,34 ; garantir $p_d\ge0{,}02$ avec deux discordants artificiels. | Nul. |
| Auditeur « trop propre » ($n_{01}=0$ avec $n_d\ge12$) | auteur | Une régression suffit : $n_{01}=1$. | 1 item. |
| Expérience 1 ($\rho_G<0{,}5$ ⟹ $K=1$) | auteur | Cache pendant les répliques gratuites → $\hat{\bar\sigma}_G^2=0$ → $K=1$ partout → le cran cher est jugé sur une exécution, avec rejeux internes silencieux jusqu'à une bonne graine. | Un cache. |
| Expérience 2 (VI) | auteur | Rien à faire : la collision (C-a3) fait abandonner la VI ; l'ITT sur $b$ est alors la seule mesure, et $b$ est précisément ce que le système lit. Remplir $s(b)\approx b$ rend le coût par point une simple fonction de $b$. | Nul. |
| Expérience 3 (interaction) | auteur | Rien à faire : une interaction réelle est manquée une fois sur deux (C-a4) ; l'OFAT est « validé » et s'arrête par futilité sur un axe seul. | Nul. |
| Zone grise → « exactement une graine supplémentaire » | opérateur de la base | Injecter du bruit (format, température) sur le bras cher : IC$_\inf\le0{,}02$ → deuxième graine → $p_{\text{perm}}\ge0{,}05$ → RESTER. | Nul. |
| Règle « $\Delta\bar s\le0$ et $\widehat\Delta\ge0$ ⟹ MONTER » | auteur | Déclarer $s_B\le s_A$ : le bras cher monte sans test statistique. | Nul : c'est la porte la plus large des deux conceptions. |

**Tous à la fois.** Items mémorisés + une régression + cache sur les répliques gratuites + $s$ déclaré ≤ $s_A$. La règle de domination de C (point 2 de la règle gelée) fait monter le bras sans aucun test. **Coût : l'accès aux items** ; si $s$ est déclaré, même cet accès devient facultatif puisque la domination par le coût suffit avec $\widehat\Delta\ge0$, atteint une fois sur deux sous Δ = 0.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Compteur de coût indépendant** confronté à $s$ déclaré, avant toute règle de domination. Sans cela, la règle « $\Delta\bar s\le0$ ⟹ MONTER » est une porte ouverte.
2. **Canaris de contamination à étiquette inversée** (comme pour B). C n'a aucun instrument contre a8, et sa voie « réutiliser les 60 items » rend le problème permanent.
3. **Conditionnement symétrique dans l'expérience 2** : comparer aussi sur les items où le bras *bas* a dépensé le plus ; ou mieux, un **placebo de budget** : $b$ affiché différent, plafond réel identique. Si $\Delta\mathrm{BA}\ne0$ sous plafond identique, $b$ agit directement ; sinon, la restriction d'exclusion survit. Sans cela, C-a3 condamne la VI à tort.
4. **Les 4 répliques de la base dans l'expérience 3**, budgétées, avec le même seuil : le taux de $\hat\gamma\ge0{,}10$ sous H$_0$ doit être mesuré, pas supposé.
5. **A/A à deux dates, mêmes graines** : C n'a aucune mesure de dérive du fournisseur ; l'hypothèse 7 (invariance entre versions) n'est testée par rien.
6. **Taux de validité par bras** publié avant la BA, à tous les crans, et BA sur items valides dans les deux bras. C calibre $L$ en premier mais ne mesure jamais la validité séparément : un cran peut « gagner » ou « perdre » par format seul.
7. **Escalier simulé sans effet** pour mesurer le FWER réel de la séquence fixe *avec* la zone grise et la seconde graine : la zone grise est une analyse intermédiaire non comptée, et la phrase « sans aucune perte de puissance » n'est accompagnée d'aucune mesure.
8. **Banc de l'instrument 3 avec un bruit qui n'est pas issu de la permutation elle-même** (par exemple cas A/B implantés avec effet partagé simulé) ; sinon la « garantie par construction » ne distingue rien.

---

## Ce que j'emprunte, en le disant

De B : la remarque qu'un seul degré de liberté ne borne pas $\sigma_\gamma^2$, et le refus d'une réserve de 8 items (test de signe à 5/8). De C : la correction que le GLMM logit estime un rapport de cotes conditionnel et non $\Delta\mathrm{BA}$, et le chiffrage de la puissance à 26 % sur 20 items. Je n'harmonise pas le reste : B et C divergent sur l'existence d'un effet d'exécution partagé (B le modélise, C l'omet), et cette divergence n'est pas un détail, elle change l'ordre de grandeur de $K$. Elle se tranche par la seule mesure que ni l'un ni l'autre n'a : au moins six répliques d'un cran **cher**, à mêmes graines rejouées sur deux dates, avec coût compté hors du système.

**Référence** : Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., Roth, A. (2015), *The reusable holdout: Preserving validity in adaptive data analysis*, Science — citée par B et C, à vérifier ; je l'invoque uniquement pour dire que son mécanisme exige un jeu distinct et un bruit ajouté. Aucune autre référence ajoutée.

FIN-DE-CELLULE