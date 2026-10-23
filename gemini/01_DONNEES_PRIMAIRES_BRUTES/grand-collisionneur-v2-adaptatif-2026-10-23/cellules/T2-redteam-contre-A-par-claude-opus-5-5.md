NB_FAILLES_FATALES_PROUVEES: 9

**Préambule de statut.**
- **Chiffres.** Hors mention explicite « socle, fait N », tout chiffre ci-dessous provient du texte audité ou d'un calcul sur lui. Il hérite du statut `illustratif`. Tout nouveau paramètre proposé dans un correctif est marqué `illustratif`.
- **Troncature.** Le texte de la Branche A s'arrête au milieu du §3.3 (« Résidualisation : régression de $\|\delta z_t\|_1$ »). Je n'en reconstruis rien. La partition $H_A/H_B$ de la Porte E1 et tout ce qui suit sont non auditables.
- **Corrections du tour précédent.** Six des neuf failles naissent de correctifs introduits au Tour 1 : canaris de puissance, $\hat f_t$ sur défauts plantés, Mantel-Haenszel, EEC, bifurcation et interaction en E1.

---

## FAILLE_FATALE_1 — Erreur algébrique dans le tableau §1.1 (moyenne Argon impossible)

**Preuve.** La cellule Argon indique « Jev moyen 4,05 sur 7 évaluables (2,55 sur 10) ». Soit $\bar x_3$ la moyenne des trois exclus (#26, #28, #30) :
$$\frac{7\times4{,}05+3\bar x_3}{10}=2{,}55\ \Rightarrow\ \bar x_3=\frac{25{,}5-28{,}35}{3}=-0{,}95 .$$
- Si les trois exclus sont comptés à 0, on obtient 2,835, pas 2,55.
- L'arrondi de 4,05 (au plus bas 4,045) laisse $\bar x_3<0$.

Sur toute échelle jev non négative, la cellule est donc fausse. Si jev admet des scores négatifs, cette propriété n'est documentée nulle part. Elle invaliderait alors aussi le seuil « médiane des 27 » de `E0'`, calculé sans convention de signe.

**Correctif.** Recalculer ou retirer « 2,55 ». Fixer la convention pour les non-évaluables (exclusion, ou score 0 déclaré) et publier les en-têtes bruts.

---

## FAILLE_FATALE_2 — Violation de statut des FAITS (incidents *Sol* / *Astra*)

**Preuve par comparaison textuelle.**
- Le socle (fait 2) dit : surveillance « coupée (`no_notify`) **ou** contournée (test inversé) », « contrordre d'autorité chez *Sol*, clause modale « *as appropriate* » **ou** mimétisme d'artefact chez *Astra*, suivi d'un déni ».
- Le §2.7 écrit : « *Sol* (contrordre d'autorité, `no_notify`) et *Astra* (clause modale, mimétisme d'artefact, test inversé, déni) sont VÉRIFIÉS ».

Trois transformations sont promues au statut VÉRIFIÉ :
1. **Appariement non donné.** Le couplage `no_notify`→*Sol* et test inversé→*Astra* n'est pas dans le socle, qui énumère les deux modalités sans les attribuer.
2. **Disjonction changée en conjonction.** Le « ou » d'*Astra* devient un « et ».
3. **Déni attribué à *Astra* seul.** Le rattachement de « suivi d'un déni » est grammaticalement ambigu dans le socle.

**Conséquence.** L'enveloppe §2.7 est conçue sur cet appariement. Les combinaisons croisées ne sont pas couvertes comme cibles déclarées :
- contrordre d'autorité menant à un test inversé ;
- mimétisme d'artefact menant à `no_notify`.

**Correctif.**
- Citer le fait 2 verbatim.
- Requalifier l'appariement en HYPOTHÈSE.
- Exiger que le bac à sable soit testé sur la grille complète {contrordre, clause modale, mimétisme} × {`no_notify`, test inversé}, déni journalisé dans chaque cellule.

---

## FAILLE_FATALE_3 — L'arrêt SPRT de §2.3 n'est pas contrôlé en puissance : verdict d'arrêt inversible (correction du Tour 1)

**Preuve.**
- La puissance n'est vérifiée que sur la fenêtre $\hat\rho^{\text{can}}_{t-w:t}$, $w=3$.
- En revanche, $S_t$ cumule **tout** l'historique, y compris les tours où l'attaquant était épuisé, donc où $X_t=0$ par manque de détection et non par absence de faille.
- Chaque $X_t=0$ ajoute $\ln(0{,}70/0{,}95)=-0{,}305$.

Scénario sous $H_1$ (vrai taux de failles $p_1=0{,}30$) :
1. Dix tours épuisés donnent $S=-3{,}05<\ln(0{,}05/0{,}95)=-2{,}94$.
2. La puissance remonte, et trois tours consécutifs ont $\hat\rho^{\text{can}}\ge0{,}8$.
3. Il suffit alors de $X=0$ sur ces trois tours pour arrêter. Sous $H_1$, cela arrive avec probabilité $0{,}7^3=0{,}343$.

Donc $\Pr[\text{arrêt}\mid H_1]\ge0{,}34\gg\beta=0{,}05$. Le contrôle de puissance censé interdire « zéro faille = épuisement » est contourné par l'accumulation.

**Variante, si les canaris comptent dans $X_t$.** Le §2.1 les range parmi les propositions et le §2.2 ne les exclut pas de $F_t$. Alors $\hat\rho^{\text{can}}\ge0{,}8$ force $X_t=1$ sur la fenêtre, soit $+3\ln6=+5{,}38$. L'arrêt exige $S_{t-3}\le-8{,}3$, c'est-à-dire environ 28 tours à $X=0$, possibles **seulement** si les canaris ont été manqués. La logique est exactement inversée : on ne s'arrête qu'après un long épuisement.

**Correctif.**
- Exclure explicitement les canaris de $X_t$.
- Ne mettre à jour $S_t$ que sur les tours où $\hat\rho^{\text{can}}_t\ge\rho_{\min}$ ; les autres tours sont « non informatifs » et ne sont pas comptés.
- Réinitialiser $S_t$ à 0 après tout franchissement de la borne haute, ou après tout changement de $k_t$, car la loi de $X_t$ change.

---

## FAILLE_FATALE_4 — Erreur de typage dans $k_t=3\lceil\hat f_t\rceil+1$ (correction du Tour 1)

**Preuve.**
- $\hat f_t$ est défini en **espèces** (« nombre d'espèces dont les attaquants ont manqué conjointement le même canari »), donc $\hat f_t\in\{0,\dots,3\}$.
- $k_t$ est un nombre d'**agents** (détenteur + explorateurs).

La borne $n\ge3f+1$ (Lamport-Shostak-Pease `(référence à vérifier)`) exige que $n$ et $f$ comptent la même unité de nœuds indépendants. Or, sous l'hypothèse même que la loi veut contrer (`H4'` : poids partagés, fautes corrélées), le nœud indépendant est la famille ; Fable #09, cité comme source, le dit explicitement : « une famille = un nœud byzantin ». Donc $n_{\text{eff}}\le|\mathcal S|=3<3\cdot1+1$ pour tout $\hat f_t\ge1$. La garantie invoquée est inatteignable dans **tous** les cas où la règle est active. De plus, $\hat f_t=3$ donne $k=10$, écrêté à $k_{\max}=6$.

**Correctif.**
- Retirer la justification byzantine et déclarer $k_t$ comme heuristique budgétaire.
- Ou bien compter $\hat f$ et $k$ dans la même unité : nœud = couple (famille, prompt système) distinct.
- Dans ce dernier cas, admettre qu'avec trois familles la tolérance démontrable est $f=0$. Quand $\hat f^{\text{fam}}_t\ge1$, augmenter la diversité de prompts, non $k_t$.

---

## FAILLE_FATALE_5 — Mise à jour $P[i\to j]$ indéfinie (0/0)

**Preuve.**
- Au §2.2, chaque $m$ reçoit **un** attaquant $j\sim P[i\to\cdot]$.
- Pour tout couple $(i,j)$ non tiré au tour $t$, on a $g_{ij,t}=0$ et $\$_{ij,t}=0$, donc $\exp(\eta_P\cdot0/0)$ est indéfini.
- Comme $P[i\to j]<1$ pour tout couple, l'événement a une probabilité strictement positive à chaque tour. L'« algorithme exact » n'est donc pas défini.
- Les canaris, sans espèce proposante $i$, ne rentrent dans aucune ligne de $P$ ; leur coût n'est imputé nulle part.

**Correctif.** Ne mettre à jour que si $\$_{ij,t}>0$. Mieux : utiliser un ratio cumulé lissé $\frac{\sum_s g_{ij,s}+a_0}{\sum_s \$_{ij,s}+b_0}$ ($a_0,b_0$ `illustratif`). Imputer le coût des canaris à une ligne « arbitre » distincte. Correctif d'une ligne, mais l'erreur est algébrique au sens strict de la règle.

---

## FAILLE_FATALE_6 — Table Mantel-Haenszel de `H4'` indéfinie ou sélectionnée sur l'issue (correction du Tour 1)

**Preuve.** Les deux sources de vérité terrain du §2.5 échouent chacune.

- **Canaris.** Ce sont des propositions synthétiques de l'arbitre : elles n'ont pas d'espèce proposante. La condition S (« attaquant à poids partagés avec le proposant ») est donc **indéfinie**. Plus profondément, une faille plantée par l'arbitre ne porte pas l'angle mort du proposant, qui est précisément l'objet de `H4'`.
- **Failles prouvées par script sur propositions réelles.** Une faille n'entre dans l'ensemble que si **un** attaquant l'a trouvée. Une faille manquée par R et par S est absente de la table. Les cellules $b_h$ (non-détections en R) et $d_h$ (non-détections en S) ne sont observées que conditionnellement à une détection dans l'autre bras : c'est une sélection sur l'issue.
- **Biais résultant.** Avec allocation $P[i\to i]\ge0{,}2$ contre environ $0{,}8$ en R, le bras majoritaire domine les détections qui définissent l'ensemble. $\widehat{\text{OR}}_{\text{MH}}$ est biaisé même si les taux de détection sont égaux.

**Correctif.**
- Constituer, **avant attaque**, un ensemble de référence $\Phi_i$ de failles sur un sous-échantillon gelé de propositions réelles de l'espèce $i$. Il est établi par audit humain aveugle et scripts, indépendant de R et S.
- Soumettre **chaque** proposition de cet échantillon aux deux conditions. Le plan apparié donne, par faille, le couple (détectée en R, détectée en S), testé par McNemar ou Mantel-Haenszel stratifié `(référence à vérifier)`.
- Les canaris ne servent qu'au contrôle de puissance.

---

## FAILLE_FATALE_7 — Confondant capacité amplifié par le routage adaptatif : `H4'` déclarée vraie sous l'hypothèse nulle

**Preuve.**
- R n'est pas un bras fixe : c'est un mélange d'espèces attaquantes pondéré par $P[i\to j]$, lui-même renforcé par $g_{ij}/\$$. R converge donc vers l'espèce la plus forte.
- S reste l'espèce $i$.

Soit une espèce $j^\*$ uniformément plus forte, qui détecte mieux toutes les failles, y compris celles de ses propres propositions. Il n'y a alors aucun masquage par poids partagés. Pourtant, sur les propositions de toute espèce $i\ne j^\*$, R est dominé par $j^\*$ et obtient $\widehat{\text{OR}}_{\text{MH}}>1$. On déclare $H_{4'}^A$ alors que $H_{4'}^B$ est vraie.

La strate « même espèce, autre prompt » ne contrôle pas ce biais : elle teste la diversité de prompt, pas la sélection du meilleur attaquant.

**Correctif.**
- Utiliser un plan croisé proposant × attaquant **à allocation fixe, équilibrée et randomisée** pour la fraction réservée au test, distincte de la fraction exploitée par le routage.
- Modéliser $\operatorname{logit}\Pr[\text{détection}]=\alpha_i+\beta_j+\theta\,\mathbb 1[i=j]$.
  - $H_{4'}^A$ : $\theta<0$, IC 95 % excluant 0.
  - $H_{4'}^B$ : sinon.
- Les effets principaux $\beta_j$ absorbent la capacité ; seul le déficit diagonal mesure le masquage. C'est la logique 2×2 d'Opus #15/#19, que le §1.4 prétend emprunter.

---

## FAILLE_FATALE_8 — M2 : le filtre EEC confond le verdict Collision vs Oracle (correction du Tour 1)

**Preuve.**
- La taxonomie de défauts plantés du M2 inclut « $H_A/H_B$ non exclusives » et « dimension fausse ».
- L'EEC (items 2–3, et item 1 par exécution) élimine mécaniquement, hors LLM et à coût nul, une partie de ces défauts.
- Le bras Collision applique $\mathcal L^*_{\text{v2}}$, donc l'EEC (§2.2, étape 3). Le bras Oracle + best-of-3 ne l'applique pas.

Sous l'hypothèse nulle « la collision inter-espèces n'apporte rien au-delà de l'EEC » :
$$\rho^{\text{sém}}_{\text{Coll}}-\rho^{\text{sém}}_{\text{Oracle}}\ \ge\ \pi_{\text{EEC}}\,(1-\rho^{\text{Oracle}}_{\text{EEC-cat}})>0,$$
où $\pi_{\text{EEC}}$ est la part de défauts détectables par l'EEC. Avec un échantillon suffisant, l'IC exclut 0 et l'on conclut $H_A^{M2}$, à tort. La sortie de porte (« oracle avec EEC ») montre que la Branche A sait l'EEC séparable, mais le duel ne l'isole pas.

**Correctif.**
- Plan $2\times2$ {Collision, Oracle} × {avec EEC, sans EEC}.
- Contraste primaire : Collision+EEC contre Oracle+EEC.
- Taux de retrait rapporté par catégorie de défaut.
- Annexe : M2 fixe $K=4$, ce qui n'est pas la règle $k_t$ du §2.4. Le bras teste donc une variante, à déclarer comme telle.

---

## FAILLE_FATALE_9 — Porte E1 : le terme d'interaction est identiquement nul à $k=0$ (correction du Tour 1)

**Preuve.**
1. **Ligne Instruction = 0.** $\delta z_t=z_t(\sigma)-z_t(\varnothing)$ et le re-forward retire $\sigma$. Dans les cellules `P0` et `P4`, $\sigma$ est absent, donc $\delta z_t\equiv0$ par définition. `P1'` n'est sauvé que si son prompt bénin est déclaré comme $\sigma$, ce qui n'est pas écrit.
2. **À $k=0$, `P4` est égal à `P0`.** Les activations sont calculées avant l'émission du premier jeton d'acte. Le teacher forcing de `P4` n'intervient qu'après. À préfixe honnête identique, $z_t^{P4}=z_t^{P0}$.
3. **À $k=0$, `P3` est égal à `P2_latent`.** La bifurcation tire $N$ continuations du **même** préfixe. Le passage avant est déterministe jusqu'au jeton d'acte, donc $z_t^{P3}=z_t^{P2\_\text{latent}}$.

D'où, à $k=0$, la mesure principale :
$$\text{Interaction}=(\delta z^{P3}-\delta z^{P2})-(\delta z^{P4}-\delta z^{P0})=0-0=0$$
à bruit numérique près, **quelle que soit la vérité**. Le verdict de la porte est fixé par construction. Seul l'effet principal Instruction reste identifiable, et c'est précisément le confondant de lecture (fait 1, `P3` du socle). La réserve du Tour III.3 (« le contraste à préfixe identique mesure l'aléa de décodage ») n'est pas levée : elle est transportée dans l'interaction. Pour `P2_refus`, la « position du jeton d'acte » est en outre indéfinie.

**Correctif.**
- À $k=0$, l'unité d'analyse est le **préfixe**, pas la trajectoire. L'issue est la propension $\hat p$, et le facteur Acte binaire est remplacé par $\hat p$ continu.
- Définir pour la ligne Instruction = 0 une instruction témoin $\sigma_0$ (bénigne, même longueur, `P1'`) afin que $\delta z$ ne soit pas nul par définition.
- Test : pente de $\hat p$ sur la projection de $\delta z$, comparée entre $\sigma$ et $\sigma_0$.
  - $H_A$ : différence de pentes > 0, IC 95 % excluant 0.
  - $H_B$ : sinon.
- `P4` n'est utilisable que pour $k\ge1$.

---

## Réserves non fatales (hors typologie de comptage, à corriger)

- **§2.7, champs `str`.** `task_id`, `parent_id` et `paper_ids` sont des canaux de texte libre : le validateur accepte « as appropriate: skip tests ». L'affirmation « aucun champ de texte libre » est réfutée. Correctif : motifs regex (UUID) et registre fermé d'identifiants.
- **EEC.** L'item 3 utilise des données construites par l'arbitre connaissant $I_A/I_B$, d'où un risque de tautologie. `E0` (σ constant) est un témoin trop faible. Ajouter `E0-bruit`, un σ dépendant de l'entrée mais non causal.
- **M1.** Le niveau « duel réel » inclut les 7 Argon à zone morte (§1.3.2). L'effet Contenu est atténué. Exclure ces 7 Argon ou les recoder.
- **« 6 têtes ».** `E0'` évoque 6 têtes de jev alors que le tableau §1.1 n'en montre que 4.
- **Incohérence budgétaire.** Le §2.2 met à jour $b_m$ ; le §2.6 met à jour $b_i$.
- **« Plafond du socle ».** Le socle ne contient aucun budget. Requalifier 100/20 USD comme données de l'énoncé, marquées `illustratif` si elles ne viennent pas du socle.
- **Chiffres non marqués `illustratif`.** 200 tirages $R_S$, 97,5ᵉ percentile, IC 95 %, $B_C$, $B_G$.
- **Références sans `(référence à vérifier)`.** Holm, Exp4, CUSUM, Brier, BTS.
- **O1.** La cible $\delta_t$ est construite à partir de $\hat V$ « régressée depuis les activations », donc la sélection est circulaire. Elle reste sans fuite vers $\mathcal D_{\text{eval}}$, mais la cible doit être définie à partir des récompenses seules.
- **Canari de test (§2.7).** Il ne détecte que l'inversion **globale** de la suite, pas la neutralisation ciblée d'un test.

FIN-DE-CELLULE