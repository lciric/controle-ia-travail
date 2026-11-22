Voici la contre-lecture critique de la synthèse, organisée selon vos cinq axes. Pour chaque défaut, le niveau de gravité, la phrase visée, le problème et une correction en une phrase sont indiqués.

---

### 1. Fidélité aux sources (F, A, C, N)

- **[Défaut fort]** *Faux accord sur la garantie disjonctive.*
  - **Phrase visée :** « Les quatre modèles s'accordent sur le cœur : [...] La seule garantie qui tient sans minorant est disjonctive : "trouvé, ou bien certifié que la fréquence est sous un seuil". » (section 1).
  - **Problème :** Fable ne formule jamais la garantie disjonctive (la section 3 ne l'attribue d'ailleurs qu'à C, N et A). De plus, les quatre réponses identifient une autre garantie sans minorant sur $p$ : l'énumération exhaustive lorsque le langage est fini et tient dans le budget.
  - **Correction :** Attribuer la garantie disjonctive aux seuls A, C et N, et préciser qu'elle est la seule garantie uniforme sans minorant à budget fixe hors énumération d'une tranche finie.

- **[Défaut fort]** *Faux accord sur le guidage par le juge.*
  - **Phrase visée :** « Neon et Argon proposent une phase pilote sur une part du budget, puis une allocation adaptative : cela revient au "permis sur tirages distincts" de Fable. Accord de fait, à écrire. » (section 5).
  - **Problème :** Ce n'est pas un accord : A, C (omis ici, alors qu'il propose aussi un pilote sur $B_{\text{pilote}}$) et N supposent un vérificateur déterministe exact $V$, non un juge statistique sur échantillon fixe dont l'adaptativité corrompt la validité (Dwork et al.). Argon recommande même un bandit guidé par $V$ *pendant la course* sur $B - B_0$ (section 5.4), ce qui contredit Fable.
  - **Correction :** Acter une différence de régime (juge statistique sur tirages partagés chez F contre vérificateur exact chez A, C, N) plutôt qu'un accord de fait.

- **[Défaut moyen]** *Attribution fausse de l'indécidabilité (Rice, 1953) à Carbon.*
  - **Phrase visée :** « Indécidabilité (A, C, N ; Rice, 1953). » (section 4).
  - **Problème :** Carbon ne cite ni Rice (1953) ni l'indécidabilité ; il invoque la NP-complétude sur mots de longueur bornée (Cook, 1971), apport omis des impossibilités.
  - **Correction :** Restreindre l'attribution de Rice (1953) à A et N, et ajouter la borne de NP-dureté (Cook, 1971) au crédit de C.

- **[Défaut moyen]** *Exagération de l'unicité de Fable sur la composante mécanique et attributions inexactes à C et N.*
  - **Phrase visée :** « Mélange défensif [...] | F seul » (section 3) ; « Carbon et Neon disent qu'on ne peut pas changer sa loi : la recherche locale, le recuit et l'apprentissage par renforcement seraient donc inapplicables. » (section 5).
  - **Problème :** Neon propose explicitement un portefeuille hybride allouant $\lambda$ du budget au générateur dédupliqué et $1-\lambda$ à l'énumération/tirage sur $\Gamma$ (section 2.2.3), qui réalise le même principe sur tranche finie ; C envisage aussi le contournement par énumération directe et ne parle pas d'apprentissage par renforcement (seul N en parle) ; enfin, A exclut également MCMC sur générateur passif.
  - **Correction :** Indiquer que seul F formalise le mélange défensif pondéré sur grammaire infinie, tout en créditant N du portefeuille hybride et en corrigeant les attributions à A et C.

- **[Défaut moyen]** *Prédiction conforme et contrôle du risque attribués à tort à Argon.*
  - **Phrase visée :** « Filtre bon marché calibré (prédiction conforme, contrôle du risque) | Rappel au moins $1-\alpha$ [...] sans hypothèse sur la loi, si les tirages sont échangeables [...] | C, N, A » (section 3).
  - **Problème :** Argon n'évoque ni prédiction conforme ni échangeabilité ; il propose un filtrage par classe de dimension VC finie sous i.i.d. (Vapnik-Chervonenkis, Cohn et al.) et un filtre syntaxique exact sans faux négatifs (Courcelle, Knuth).
  - **Correction :** Retirer A de la ligne sur le filtrage conforme et distinguer le filtrage PAC/VC et le filtrage syntaxique exact proposés par A.

- **[Défaut moyen]** *Diagnostics de Neon attribués collectivement aux trois modèles Google et contradiction interne.*
  - **Phrase visée :** « Argon, Carbon et Neon : des diagnostics bon marché sur le générateur réel, sans appel au vérificateur : taux de collisions, autocorrélation des tirages, audit du déterminisme et des erreurs du vérificateur, masse non vue. » (section 5).
  - **Problème :** Seul N propose l'audit du déterminisme et des erreurs $(\alpha,\beta)$ du vérificateur (qui nécessite des appels au vérificateur, contredisant « sans appel ») ainsi que la masse non vue (aussi citée par F via McAllester et Schapire) ; de plus, A et C proposent des preuves formelles préalables (décomposabilité, cardinal, NP-dureté) omises ici.
  - **Correction :** Attribuer collisions et autocorrélation/indépendance à A, C et N, réserver l'audit du vérificateur (coûtant des appels pilotes) et la masse non vue à N (et F pour cette dernière), et ajouter les preuves préalables de A et C.

- **[Défaut faible]** *Erreurs ponctuelles d'attribution et apports importants omis.*
  - **Phrase visée :** « Recuit, tempering parallèle [...] C et N le disent inapplicable à un générateur fermé » (section 3) ; « Aiguille (F, N ; Wolpert et Macready, 1997) » (section 4) ; « Les trois modèles de Google la citent, avec la constante $4(e-2)$ » (section 6).
  - **Problème :** A cite aussi Wolpert-Macready (section 2.A) et l'inapplicabilité de MCMC ; C critique le recuit par le caractère binaire de $V$ plutôt que la boîte noire ; F mentionne aussi le dédoublonnage ; N ne mentionne pas la constante $4(e-2)$ pour Dagum et al. ; l'accord sur « vote, réordonnancement... » (section 5) amalgame des heuristiques critiquées par des modèles différents. Enfin, le tableau de section 3 omet le SPRT (Wald, cité par A, C, N), Dagum et al. (A, C, N), le test groupé de Dorfman (C), l'impossibilité en apprentissage actif (Dasgupta, Hanneke chez N), les bornes *anytime-valid* (Ramdas et al. chez N) et la séparation des trois budgets de F.
  - **Correction :** Corriger les attributions ponctuelles (retirer N de $4(e-2)$, ajouter A à Wolpert-Macready et MCMC) et compléter la section 3 par les méthodes et bornes omises.

---

### 2. Mathématiques

#### Vérification des calculs revendiqués par la synthèse (section 6)
1. **Rentabilité d'un filtre** : Sous tirages i.i.d., $p>0$, $r_{\text{rec}}>0$, vérificateur exact, absence de dédoublonnage et **coûts de filtrage et de calibration nuls**, l'identité de Wald donne un coût espéré par succès de $C_{\text{direct}}=(c_g+c_v)/p$ sans filtre et $C_{\text{filtre}}=(c_g+q c_v)/(p r_{\text{rec}})$ avec filtre. Ainsi $C_{\text{filtre}}<C_{\text{direct}} \iff r_{\text{rec}}>(1+qr)/(1+r)$. **Calcul exact.**
2. **Plafond du gain** : Tout filtre satisfait $q=\mathbb{P}(X\in F)\ge \mathbb{P}(X\in F\cap S)=p r_{\text{rec}}$ et $r_{\text{rec}}\le 1$, donc $C_{\text{filtre}} \ge c_g/(p r_{\text{rec}})+c_v \ge c_g/p+c_v$, atteint par un filtre parfait ($q=p, r_{\text{rec}}=1$). Le gain maximal vaut $C_{\text{direct}}/(c_g/p+c_v)=(1+r)/(1+pr)\le 1+r$. **Calcul exact** sous les mêmes hypothèses (et hors dédoublonnage).
3. **Borne de couverture de Fable** : Pour des classes disjointes ($\sum_c q(c)\le 1$), il existe au plus $\lfloor 1/\tau\rfloor \le 1/\tau$ classes de masse $\ge \tau$. Sous $N$ tirages i.i.d. (ou négativement associés), par borne d'union, $\mathbb{P}(\exists c : q(c)\ge \tau \text{ non vue}) \le \frac{1}{\tau}(1-\tau)^N \le \frac{1}{\tau}e^{-\tau N} \le \delta$ dès que $N \ge \frac{1}{\tau}\ln\!\left(\frac{1}{\tau\delta}\right)$. **Calcul exact** (avec $N$ entier, $\tau,\delta\in(0,1)$).
4. **Borne disjonctive** : Pour $n\ge 1$ tirages i.i.d. (fixé d'avance) et $V$ exact, si $p < 1-\delta^{1/n}$ la disjonction vaut $1$ ; si $p \ge 1-\delta^{1/n}$, $\mathbb{P}(\text{succès})=1-(1-p)^n \ge 1-\delta$ (y compris au bord $p=1-\delta^{1/n}$). **Calcul exact.**

- **[Défaut faible]** *Hypothèses omises sur la rentabilité du filtre.*
  - **Phrase visée :** « Le filtre abaisse le coût par succès si et seulement si $r_{\text{rec}} > (1 + q\cdot r)/(1 + r)$. » (section 3).
  - **Problème :** La formule ne vaut qu'en coût *espéré*, sous tirages i.i.d., sans dédoublonnage, avec vérificateur exact et à coûts de filtrage et de calibration négligeables (sinon le numérateur ajoute $c_f/c_g$ et le budget pilote réduit le gain).
  - **Correction :** Préciser qu'il s'agit du coût espéré i.i.d. hors dédoublonnage, à coûts de filtrage et de calibration nuls.

- **[Défaut fort]** *Seuil $n\cdot r\cdot\Delta \ge L\cdot\ln 2 + \ln(1/\alpha)$ non défini, non vérifié et présenté comme critère suffisant.*
  - **Phrase visée :** « On ne force la reconnaissance que si l'évidence paie la longueur de description : $n\cdot r\cdot\Delta \ge L\cdot\ln 2 + \ln(1/\alpha)$. » (section 7 ; aussi section 3).
  - **Problème :** (1) $n$, $r$ et $\Delta$ ne sont définis ni dans la synthèse ni dans F (qui renvoie à une « réponse 28 » absente), et $r$ entre en collision avec $r=c_v/c_g$ ; (2) le calcul n'a pas été vérifié ; (3) pour les valeurs $e$ pondérées ($w(c)=2^{-L(c)}$, retenue si $E_c \ge 2^{L(c)}/\alpha$), le contrôle FWER $\le \alpha$ par Markov et borne d'union exige un **code préfixe** ($\sum_c 2^{-L(c)}\le 1$), la validité $\mathbb{E}_{H_0}[E_c]\le 1$ sous le nul composite et l'absence d'adaptativité ; (4) côté détection, même si $\mathbb{E}_{H_1}[\ln E_c]=n r \Delta$ (tirages frais i.i.d. et alternative connue), l'inégalité n'assure qu'un dépassement *en espérance* (puissance voisine de $1/2$, sans terme de variance/marge) ; enfin le contrôle en ligne exige un budget $\alpha_t$ décroissant, pas un $\alpha$ constant.
  - **Correction :** Définir $n$, $r$ (sous un autre symbole) et $\Delta$, qualifier la formule d'ordre de grandeur en espérance sous code préfixe et tirages frais i.i.d., et rappeler que sa validité sous le nul composite reste non prouvée.

- **[Défaut moyen]** *Hypothèses incomplètes sur la garantie $q(c) \ge \varepsilon\cdot u(c)$.*
  - **Phrase visée :** « Probabilité minimale $\varepsilon\cdot u(c)$ pour toute classe $c$, quel que soit le modèle ; perte d'au plus $\varepsilon$ du budget » (section 3).
  - **Problème :** Si $q=(1-\varepsilon)p+\varepsilon u$, $q(c)\ge \varepsilon u(c)$ est une identité élémentaire, mais elle suppose $u(c)>0$ et la capacité de tirer effectivement selon $u$ dans l'espace des classes canoniques ; la perte bornée à $\varepsilon$ du *budget* exige en outre que le coût tirage+vérification soit identique sous $u$ et $p$ (et néglige le durcissement du seuil du juge relevé par F). Enfin, pour la *découverte* (contrairement à l'importance sampling d'Hesterberg), l'énumération sans remise sur la part $\varepsilon$ domine le tirage aléatoire $u$.
  - **Correction :** Préciser l'hypothèse d'égalité des coûts unitaires (hors coût statistique sur le juge) et signaler qu'une énumération sans remise sur la part $\varepsilon$ domine le tirage aléatoire avec remise.

- **[Remarque]** *Erreurs mathématiques dans la source Neon (jugée sans indulgence).* En section 2.2.1 de N, la borne de Chernoff $\mathbb{P}(E_k^c)\le \exp(-(np-k)^2/(2np))$ et le coût Las Vegas exact $\frac{k}{p}(c_g+c_v)$ sont **faux pour $k\ge 2$** au regard de sa propre définition de $E_k$ (« au moins $k$ objets valides *distincts* »), car la loi binomiale compte les répétitions (si $|S|=1$, $\mathbb{P}(E_2)=0$). Par ailleurs, sa formule de Chung-Erdős (section 3.3) est algébriquement exacte (vérifiée via $(\mathbb{E}[S])^2/\mathbb{E}[S^2]$), mais son augmentation pour $\rho_{ij}<0$ ne suffit pas à prouver la dominance stricte sur l'i.i.d. (il faut l'association négative citée par C).

---

### 3. Le verdict

- **[Défaut fort]** *Verdict essentiellement porté par Fable et exagéré quant à la portée pratique.*
  - **Phrase visée :** « Oui, on peut forcer, mais au sens d'un théorème seulement, et à un prix qu'une borne inférieure fixe. [...] Fable ajoute le point qui répond à la question du directeur : le minorant, on peut le fabriquer soi-même. » (section 1).
  - **Problème :** Cette thèse reprend presque mot pour mot la « Réponse courte » de F et n'est pas le verdict partagé des quatre modèles : A, C et N traitent le générateur comme boîte noire stricte et mettent en avant le certificat disjonctif, la déduplication, l'élagage et le filtrage calibré (seul N propose un portefeuille hybride voisin sur tranche finie). Surtout, le verdict est exagéré face aux « puits profonds étroits » : fabriquer un minorant mécanique $\varepsilon\cdot 2^{-L}$ est formellement exact mais pratiquement vide dès que $L$ croît, car le coût explose exponentiellement — cela ne « force » que la tranche courte accessible en force brute.
  - **Correction :** Présenter le verdict comme une impossibilité de forçage en boîte noire pure (hors certificat disjonctif), complétée par la proposition de F (et le portefeuille de N) qui n'assure une garantie effective que sur la tranche courte énumérable.

---

### 4. Les décisions D1 à D5

- **[Défaut moyen]** *D1, D2 et D4 suivent uniquement Fable, avec une contradiction interne en D2 et une prémisse inexacte en D4.*
  - **Phrase visée :** « D1. Fixer le sens contractuel de "forcer" : garantie de pire cas dans la grammaire publique [...] D2. Mettre un bras sans modèle de langue (énumérateur ordonné par longueur, valeurs e pondérées par la longueur) [...] c'est la seule garantie complète. [...] D4. Interdire en course que la recherche soit guidée par le juge statistique » (section 8).
  - **Problème :** D1, D2 et D4 reprennent D1–D3 de Fable (jusqu'aux scores de confiance 0,8, 0,85, 0,7) sans fondement dans A, C et N (qui ne réduisent pas « garantir » au pire cas sur la grammaire et ne proposent pas de valeurs $e$ pondérées). Qualifier D2 de « seule garantie complète » contredit la reconnaissance en section 3 et 7 que la validité sous le nul composite reste à prouver. D4 ne peut s'appuyer sur un prétendu accord avec A et N.
  - **Correction :** Indiquer que D1, D2 et D4 relèvent du seul cadre de F, retirer « seule garantie complète » de D2 tant que le nul composite n'est pas démontré, et ne fonder D4 que sur l'adaptativité du juge statistique.

- **[Défaut faible]** *D3 mélange les apports et omet l'analyse formelle préalable.*
  - **Phrase visée :** « D3. Ajouter au premier étage du plan les diagnostics bon marché proposés par Argon, Carbon et Neon [...] ne coûtent presque aucun appel au juge. » (section 8).
  - **Problème :** L'audit du juge et la masse non vue proviennent de N seul ; auditer le juge ou certifier une masse non vue sur $S$ consomme des appels au vérificateur ; enfin D3 omet l'audit formel de la grammaire (sous-grammaire nécessaire, décidabilité/NP-dureté) proposé par A et C.
  - **Correction :** Attribuer chaque diagnostic à son auteur, séparer tests gratuits et budget pilote, et inclure l'audit formel de la grammaire (A, C) dans l'étape 0.

- **[Défaut moyen]** *D5 omet une référence décisive fondant D4.*
  - **Phrase visée :** « D5. Vérifier sur PDF les citations 1 à 4 de la section 6 [...] Ce sont les quatre appuis de la réponse » (section 8).
  - **Problème :** Les citations 1 à 4 viennent toutes de F, alors que D4 repose explicitement sur Dwork et al. (2015), absente même de la liste 1–13 de la section 6.
  - **Correction :** Inclure Dwork et al. (2015) parmi les références prioritaires à vérifier sur PDF avant d'acter D4.

---

### 5. Faits non vérifiés et audit des références

- **[Défaut moyen]** *Affirmations issues de sources non vérifiées ou externes présentées sans marque.*
  - **Phrase visée :** « C'est la limite de la queue déjà nommée par cinq modèles sur six dans le tour précédent du collisionneur. » (section 4) ; « le tempering échoue exactement sur un mode étroit voisin d'un mode large » (section 7) ; « validité perdue (Dwork et collaborateurs, 2015) » (section 8).
  - **Problème :** Le premier fait renvoie sans pièce justificative à un tour antérieur absent du dossier ; le deuxième efface la certitude seulement « moyenne pour la portée » donnée par F à Woodard et al. (2009) ; le troisième cite Dwork et al. sans marque de non-vérification (R7).
  - **Correction :** Sourcer ou retirer la mention du tour précédent, rétablir la nuance de portée sur Woodard et al., et marquer Dwork et al. comme non vérifié sur PDF.

- **[Remarque]** Les niveaux de confiance en section 8 (0,8 à 0,65) sont des appréciations subjectives non justifiées, et les coûts/scores de devinette des sections 0 et 2 ne sont pas vérifiables dans les pièces jointes (seul le coût de F y figure).

#### Audit des références (ce que je sais vs ce que je suppose)

- **[Défaut moyen]** *Deux attributions impropres reprises sans filtre : Bahadur-Savage (1956) et Blumer et al. (1987).*
  - **Phrase visée :** « Carbon cite Bahadur et Savage (1956) pour la forme non paramétrique. » (section 4) ; « Blumer, Ehrenfeucht, Haussler et Warmuth, 1987, *Occam's Razor* ; Wang et Ramdas, 2022 [...] : seuil pondéré par la longueur. » (section 6).
  - **Problème :** *Ce que je sais :* Bahadur et Savage (1956) existe bien, mais porte sur l'inexistence de procédures non paramétriques pour la moyenne de lois **non bornées**, et ne s'applique pas aux variables de Bernoulli bornées dans $\{0,1\}$ ; Blumer et al. (1987) existe bien, mais prouve des bornes PAC d'apprentissage supervisé, non un seuil par valeurs $e$ pondérées (et Wang & Ramdas 2022 porte sur le contrôle FDR par e-BH, non sur $n r \Delta \ge L \ln 2 + \ln(1/\alpha)$).
  - **Correction :** Déplacer Bahadur-Savage (1956) et Blumer et al. (1987) dans les attributions impropres en section 6 et ne plus les présenter comme fondements des énoncés visés.

- **[Défaut faible]** *Traitement inexact de Dorfman (1943) et imprécisions de la section 6 sur les références douteuses.*
  - **Phrase visée :** « Carbon, coût de vérification groupée de Dorfman (1943) "en $O(\sqrt{p})$". L'ordre de grandeur est plausible, à vérifier. » et « Carbon, "Daniel Gillman (1998)". Argon écrit David Gillman ; le prénom est à vérifier. » (section 6).
  - **Problème :** *Ce que je sais :* (1) Dorfman (1943) existe et le calcul élémentaire $\min_k (\frac{1}{k}+1-(1-p)^k) \approx 2\sqrt{p}$ confirme exactement le coût $O(\sqrt{p} c_{\text{ver}})$ *par candidat testé* écrit par C ; (2) l'auteur de 1998 est bien **David Gillman** (erreur de prénom chez C) ; (3) Halmos (1946) existe (estimation sans biais à taille fixe) et Nisan-Szegedy (1994) porte sur le degré polynomial des fonctions booléennes : la méfiance de la synthèse sur ces deux attributions (A et C) est fondée ; (4) Hesterberg (1995) existe mais porte sur la variance de l'importance sampling, non sur la recherche sur grammaire ; (5) C cite **Wald et Wolfowitz (1940)** (test à deux échantillons) au lieu du test d'aléa d'une suite (Wald et Wolfowitz, 1943). *Ce que je suppose (faute de PDF) :* pour Dagum et al. (2000), je sais que la constante $4(e-2)$ est authentique dans leur règle d'arrêt, mais je suppose seulement sans vérification sur PDF l'exactitude des coefficients $+1$ et $(1+\varepsilon)$ repris par C (qu'il attribue en outre à $\mathcal{AA}$ complet plutôt qu'à la règle d'arrêt de base).
  - **Correction :** Retirer Dorfman (1943) des attributions douteuses, corriger « Daniel » en « David Gillman », confirmer les réserves sur Halmos (1946) et Nisan-Szegedy (1994), et ajouter les réserves sur Wald-Wolfowitz (1940) et la portée d'Hesterberg (1995).

FIN DE LA RÉPONSE