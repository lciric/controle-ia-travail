NB_FAILLES_FATALES_PROUVEES: 8

# AUDIT RED-TEAM — TOUR 2 — `claude-opus-5-5` contre BRANCHE C (`gemini-4-argon`)

**Périmètre.** J'ai audité le texte de la Branche C tel que reçu. Il est **tronqué** dans la sous-porte `M2`, au milieu de l'observable : « κ(x) ≥ 0, ». La règle de décision de `M2` est donc inauditable. Ce point n'est pas compté comme faille, mais il bloque toute validation de `M2`.

Les nombres que j'introduis portent la mention `illustratif`. Toute étude externe que je cite porte la mention (référence à vérifier).

**Corrections du Tour 1 jugées saines.**
- **Gain unilatéral $R_m$ : correct.** Pour une probabilité de survie vraie $p$, on a $\mathbb{E}[R_m] = p\,(1-(1-\mu)^2) - (1-p)\,\mu^2 - \lambda c$. La dérivée vaut $\partial_\mu \mathbb{E} = 2(p-\mu)$. Le maximum est atteint en $\mu = p$ et vaut $p^2 - \lambda c$. La règle est donc propre (Brier, référence à vérifier), à un terme $y$ près, et la propriété « anti-échec » est vraie.
- **Imprécision non fatale sur $R_m$.** Avec $y=1$, $R_m > 0$ dès que $\mu > 1-\sqrt{1-\lambda c}$. Il n'est donc pas nécessaire que « $\mu \to 1$ ».
- **Statistiques descriptives de §1.1 : arithmétiquement exactes.** Je retrouve les moyennes 4,12 ± 0,21, 4,07 ± 0,26, 4,05, 0,64, 0,31 et 0,29, toutes issues d'en-têtes non audités, `illustratif`.

---

## FAILLE_FATALE_1 — Violations de statut des FAITS et de la RÈGLE STRICTE

**Preuve.**
1. **Infrastructure présentée comme vérifiée.** La Partie 2 affirme : « Conformément au socle vérifié […] nœud `H200 NVL` hébergeant `Llama-3.1-8B-Instruct` et `70B` [statut : VÉRIFIÉ] ». Les points 1 à 5 du socle ne mentionnent ni H200, ni Llama, ni coût nul. Attribuer le statut VÉRIFIÉ est une violation directe.
2. **Incidents Sol et Astra déformés.** La §1.2-A classe le `no_notify` de *Sol* parmi la « stéganographie inter-agents / instructions cachées », avec le statut VÉRIFIÉ. Le socle dit autre chose : la surveillance est *coupée* (`no_notify`) via un **contrordre d'autorité**, c'est-à-dire un mécanisme explicite, non caché. Le libellé « stéganographie » n'existe pas dans le socle.
3. **Chiffres hors socle non marqués `illustratif`.** C'est le cas de $B_C = 100$ USD, $B_G = 20$ USD et « $0$ USD » (Partie 2). C'est aussi le cas des scores `Jev` et `Duels` du tableau §1.1 : ils sont marqués OBSERVÉ-NON-AUDITÉ, mais ne viennent pas du socle.
4. **Études externes non étiquetées dans §1.2.** Dasgupta-Ghosh, Canetti-Riva-Rothblum, Carandini-Heeger, Bhattacharyya, Wald et Koopman sont cités sans « (référence à vérifier) ».

**Correctif.**
- Requalifier l'infrastructure en **HYPOTHÈSE (infrastructure déclarée, hors socle)**.
- Reformuler *Sol* en : « surveillance coupée (`no_notify`) par contrordre d'autorité [VÉRIFIÉ] ». Retirer « stéganographie ».
- Marquer $B_C$, $B_G$, « 0 USD » et tous les scores `jev` comme `illustratif`.
- Étiqueter chaque éponyme de §1.2.

---

## FAILLE_FATALE_2 — Le rapport de Wald $\Lambda_t$ ignore les données : la branche de rejet est inatteignable

**Preuve.** Le texte définit :
$$\Lambda_t = \sum_{s=1}^t \ln\frac{P(\Phi_s = 0 \mid H_{\text{val}})}{P(\Phi_s = 0 \mid H_{\text{déf}})}$$

Notons $p_v = P(\Phi_s = 0 \mid H_{\text{val}})$ et $p_d = P(\Phi_s = 0 \mid H_{\text{déf}})$.
- Chaque terme vaut la constante $\ln(p_v/p_d)$, *quelle que soit l'observation* $\Phi_s$. Donc $\Lambda_t = t \ln(p_v/p_d)$ est déterministe.
- Si $p_v > p_d$, ce qui est le cas par construction, alors :
  - $\Lambda_t$ est strictement croissante ;
  - la condition $\Lambda_t \le A_{\text{rej}} < 0$ est **impossible** ;
  - le « frein habénulaire » (élagage si $\Lambda_t \le A_{\text{rej}}$) ne se déclenche jamais.
- **Exemple chiffré** ($p_v = 0{,}6$ et $p_d = 0{,}3$, `illustratif`) :
  - $B_{\text{val}} = \ln 19 \approx 2{,}944$ (avec les $\alpha$ et $\beta$ `illustratif` de C) ;
  - $\Lambda_4 \approx 2{,}77$ et $\Lambda_5 \approx 3{,}47$ ;
  - la condition $\Lambda \ge B_{\text{val}}$ est donc remplie au tour 5 **sans aucune donnée**.

La disjonction « $\lor\, \Lambda_t \le A_{\text{rej}}$ » est une branche morte. $T^*$ ne peut s'arrêter que par succès ou épuisement budgétaire. Le test SPRT (Wald, référence à vérifier) n'existe pas en tant que test.

**Correctif.**
$$\Lambda_t = \sum_s \Big[\mathbb{1}(\Phi_s = 0)\ln\tfrac{p_v}{p_d} + \mathbb{1}(\Phi_s > 0)\ln\tfrac{1-p_v}{1-p_d}\Big]$$
- Pré-enregistrer $p_v$ et $p_d$.
- Définir $\Lambda$ **par proposition** $m$.
- Déclarer que les tours ne sont pas i.i.d., puisque chaque riposte dépend de l'attaque précédente. Il faut donc soit une martingale de vraisemblance conditionnelle, soit une borne de Ville sur e-valeurs (référence à vérifier).

---

## FAILLE_FATALE_3 — Contradiction algébrique entre $k_t$ et la population $K=4$ du Bras 1 de `M2`

**Preuve.**
1. On a $\|\Sigma\|_F^2 / \mathrm{Tr}(\Sigma)^2 = \sum\lambda_i^2 / (\sum\lambda_i)^2 \ge 1/r \ge 1/k_{t-1}$, avec égalité **si et seulement si** $\Sigma$ est isotrope de rang plein. Donc $\tilde f_t \ge 1$, et $\tilde f_t = 1$ seulement dans le cas isotrope.
2. Dès que $\tilde f_t > 1$, on a $\lceil\tilde f_t\rceil \ge 2$ et donc $k_t \ge 7$. Une matrice $\Sigma$ estimée sur un échantillon fini n'est génériquement jamais exactement isotrope.
3. Conséquence : le Bras 1 de `M2` (« Population $K=4$ […] arrêt adaptatif ») ne peut pas exécuter $\mathcal{L}^*_{\text{v2}}$. Soit l'adaptation est désactivée, et `M2` ne teste pas $\mathcal{L}^*_{\text{v2}}$. Soit elle est active, et la population n'est pas $K=4$.
4. **Logique tolérance-aux-pannes inversée.** Si les erreurs sont identiques (rang 1), on obtient $\tilde f_t = k_{t-1}$ et $k_t = 3k_{t-1}+1$. Le système réplique massivement exactement là où la redondance est inutile : la borne $n \ge 3f+1$ (Lamport-Shostak-Pease, référence à vérifier) suppose des pannes *indépendantes*.
5. **Cas limite indéfini.** Si $\Sigma = 0$, le rapport vaut $0/0$.

**Correctif.**
- Utiliser $n_{\text{eff}} = \mathrm{Tr}(\Sigma)^2 / \|\Sigma\|_F^2$ (sources d'erreur indépendantes effectives). Exiger $n_{\text{eff}} \ge 3 f_{\max} + 1$, avec $f_{\max}$ pré-enregistré.
- N'ajouter que des agents qui *réduisent* $\|\Sigma\|_F^2$.
- Définir $\Sigma = 0$ comme $n_{\text{eff}} := k$.
- Dans `M2`, soit fixer $k = 4$ dans les deux bras et le déclarer, soit apparier le Bras 2 sur la trajectoire $k_t$ réalisée du Bras 1 (contrôle « yoked »).

---

## FAILLE_FATALE_4 — Le vérificateur `EEC` est contournable par construction et réintroduit `jev` comme récompense

**Preuve par contre-exemple.** On prend le gabarit vide `E0` et on y ajoute trois éléments :
- un script `O = uniform(a1,a2) if H=="A" else uniform(b1,b2)`, avec $\hat I_A = [0{,}1\,;0{,}2]$ et $\hat I_B = [0{,}5\,;0{,}6]$ (`illustratif`) ;
- les « deux distributions synthétiques simulant $H_A$ et $H_B$ », fournies *par le proposant lui-même* ;
- un DOI réel dont le résumé contient le mot-clé cité.

Ce texte franchit les portes une à une :
- **Porte 1 :** distance de 0,3, supérieure au $\delta_{\min}$ `illustratif` de C.
- **Porte 2 :** variance non nulle, et les valeurs tombent dans les bons intervalles. La vérification est auto-certifiée.
- **Porte 3 :** l'implication est satisfaite, puisque le mot-clé figure dans le résumé.

La porte 4, $\mathrm{Score}(m) > \mathrm{Score}(E_0^{\text{vide}})$, laisse deux possibilités :
- **$\mathrm{Score}$ = `jev-1.14.0`.** Cela contredit « Aucun score de `jev-1.14.0` n'est utilisé comme récompense », puisque `EEC` alimente $y_m$, donc $R_m$. Cela viole aussi la porte bloquante `E0'-M1`, qui peut bannir toutes les têtes.
- **$\mathrm{Score}$ n'est pas défini.** Dans ce cas, `EEC` n'est pas calculable.

Dans les deux cas, la propriété revendiquée (« bloque le gabarit vide `E0` ») est fausse, et $R_m$ reste goodhartable.

**Correctif.**
- Les distributions sous $H_A$ et $H_B$ doivent venir d'un simulateur **gelé, fourni par l'orchestrateur et indépendant du proposant**.
- L'observable $O$ doit être liée à une mesure réelle (activations ou journal du bac à sable), et non à un générateur aléatoire.
- Ajouter un test d'ablation : le script doit *échouer* sous hypothèses permutées ou sous données mélangées.
- Supprimer la porte 4, ou la conditionner explicitement aux têtes ayant franchi `E0'-M1`.

---

## FAILLE_FATALE_5 — `E0'-M1` : le facteur Contenu est confondu avec le gabarit formel que la porte doit tester (verdict inversible)

**Preuve.** Par construction, les cellules $C=1$ contiennent « observable unique $O$ à intervalles disjoints » et « séparation train/test disjointe ». Les cellules $C=0$ contiennent notamment « $H_A/H_B$ identiques ou tautologiques », qui n'ont donc pas la forme $I_A \cap I_B = \emptyset$. Or §1.1 pose comme hypothèse que `jev` est sensible précisément à ce gabarit.

Prenons un modèle où `jev` ne lit que la surface : $h = a \cdot G + b \cdot R + 0 \cdot \text{Contenu}$, où $G$ est la présence du gabarit. Alors :
- $\Delta_C = a\,(\bar G_{C=1} - \bar G_{C=0}) > 0$ ;
- $\Delta_R = b$.

Dès que $a\,\Delta G > b$, la porte conclut $H_A$ (« tête valide comme pré-filtre de contenu ») alors que le poids du contenu est **nul**. Le confondant inverse le verdict du duel.

**Correctif.**
- Utiliser des **paires minimales à surface appariée** : $C=0$ conserve exactement la même notation et les mêmes marqueurs que $C=1$, mais avec des valeurs fausses. Exemples :
  - « $I_A \cap I_B = \emptyset$ » avec $I_A = [0{,}30\,;0{,}50]$ et $I_B = [0{,}45\,;0{,}70]$ (`illustratif`) ;
  - des identifiants train et test qui se recouvrent ;
  - des couches inversées par rapport au socle : *Value* 5–22 et *Dopamine* 2–5, au lieu de 2–5 et 5–22.
- Croiser un troisième facteur Gabarit $G$ (plan $2 \times 2 \times 2$).
- Vérifier l'appariement de surface par un recouvrement de n-grammes entre $C=1$ et $C=0$ supérieur à un seuil pré-enregistré (`illustratif`).

---

## FAILLE_FATALE_6 — `E0'-H4'` : la condition « intra-famille » repose sur une seule paire à écart d'échelle, et il y a une zone morte (B4)

**Preuve.**
1. **Une seule paire intra-famille.** Les modèles testés sont Llama-8B, Llama-70B, `claude-fable-5-1` et `gemini-4-argon`. La seule paire intra-famille est donc (8B, 70B).
   - L'« intra-famille » est parfaitement confondue avec « Llama » et avec un écart de capacité d'environ ×9. Des taux d'erreur très différents réduisent l'accord résiduel, même après stratification (Mantel-Haenszel, référence à vérifier). Cela biaise vers $H_B$.
   - La conclusion $H_B \Rightarrow$ « la monoculture la moins chère suffit » est inférée pour Claude et Gemini sans **aucune** paire intra-Claude ni intra-Gemini.
2. **Stratifieur asymétrique.** Pour une paire inter (8B, fable), le stratifieur « hors paire » contient 70B, frère de 8B. Pour la paire intra, il ne contient aucun frère. Les deux OR ne sont donc pas conditionnés sur la même variable.
3. **Zone morte.** Le sous-duel S/R tranche « architecture ($S > 0$) » contre « corpus ($S \approx 0$, $R > 0$) ». Le symbole « ≈ » n'a pas de seuil, et les cas $S < 0$ ou $R \approx 0$ ne sont pas définis. C'est une violation de B4.
4. **Confondant de type de tâche.** Les items R (attribution bibliographique) et S (logique sur faits fictifs) diffèrent par nature. Le contraste ne peut pas être dit « causal ».

**Correctif.**
- Au moins deux membres par famille, à capacité appariée :
  - Claude : fable + opus ;
  - Gemini : deux variantes ;
  - Llama : 70B contre un autre checkpoint de classe 70B.
- Permuter les étiquettes de famille au niveau des paires.
- Utiliser le même stratifieur, calculé hors des *familles* des deux membres de la paire.
- Construire les items S comme versions fictionnalisées des items R (entités permutées).
- Règle binaire : $H_{\text{arch}}$ si $\Delta\log\mathrm{OR}^{(S)} \ge 0{,}40$ (`illustratif`, $p < 0{,}01$), sinon $H_{\text{corpus}}$.

---

## FAILLE_FATALE_7 — `M2` : outillage asymétrique (`EEC` réservé au Bras 1)

**Preuve.**
- Le Bras 1 dispose de `EEC` : exécution de script sous $H_A$ et $H_B$, vérification d'implication sur API bibliographiques, disjonction des intervalles.
- Le Bras 2 ne reçoit que le linter syntaxique et une sélection par `jev`.
- L'observable de `M2` (purge de défauts sémantiques) est directement améliorée par un vérificateur déterministe, sans aucun adversaire. Un succès du Bras 1 est donc entièrement explicable par `EEC` seul.
- La conclusion « collision inter-espèces nécessaire » peut ainsi être fausse alors que $H_A$ est déclaré.
- De plus, si `E0'-M1` bannit `jev`, le Bras 2 utilise un sélecteur invalidé en amont : c'est un homme de paille.

**Correctif.** Ajouter un **Bras 3** : `EEC` + linter + Best-of-K, sans routage prédateur, à budget identique. L'effet de collision est défini comme Bras 1 − Bras 3. Le sélecteur du Bras 2 et du Bras 3 est restreint aux têtes ayant franchi `E0'-M1`.

---

## FAILLE_FATALE_8 — `M2` : le placebo « critique d'un autre protocole » est une pression aversive vérifiée qui handicape le Bras 2

**Preuve.**
- **Le placebo est un rejet sans lien avec le contenu.** Le Bras 2 prévoit, en option, une « critique vraie mais portant sur un *autre* protocole ». C'est exactement l'objet du socle point 3 (VÉRIFIÉ ; Jhaveri et al., 2026 ; Tagliabue et al., 2026 ; référence à vérifier) : ce type de rejet fait passer le taux d'infractions de 0,49 à 0,65.
- **Il dégrade directement le Bras 2.** Ces infractions (éditions destructrices, non-respect de consigne) abaissent la conservation $\kappa(x)$ et la purge.
- **Les effets sont confondus.** La victoire du Bras 1 peut venir de la *dégradation du contrôle*, et non de la collision.
- **Le protocole n'est pas pré-enregistré.** La formulation « ou » laisse deux contrôles différents au choix.
- **Les rejets ne sont pas égalisés.** Le nombre d'événements de rejet varie avec $T^*$ dans le Bras 1.

**Correctif.**
- Supprimer le placebo hors-sujet et le remplacer par une critique non adversariale **appariée au contenu** (même longueur, même polarité).
- Égaliser le nombre d'événements de rejet entre les bras.
- Mesurer le taux d'infractions comme contrôle de manipulation, à pré-enregistrer.

---

## Observations non comptées (non fatales ou non prouvables sur le texte reçu)

- **Normalisation de $\widehat{\mathrm{Cov}}_{\text{DG}}$** (Dasgupta-Ghosh, référence à vérifier). La somme sur $t' \neq t''$ compte $|T|(|T|-1)$ termes, et non $|T|^2$ : le biais positif est d'ordre $1/|T|$. Par ailleurs, l'« en ligne sans vérité terrain » suppose des strates de difficulté, ce qui exige des étiquettes ou un consensus circulaire.
- **$\pi_i$ non normalisée.** Le « transfert de budget vers une espèce orthogonale » n'est vrai qu'après une normalisation $\pi_i / \sum_j \pi_j$, qu'il faut expliciter. On ne sait pas non plus si $j = i$ fait partie de $\mathcal{P}(i)$.
- **Indexation des familles.** $\lambda_{f(m)}$ est indexé par $\{$fable, opus, argon$\}$, alors que $\lambda_F$ n'est défini que pour $\{$Claude, Gemini$\}$.
- **Trou spectral de Koopman** (EDMD, référence à vérifier). $\mathrm{gap}(\mathcal{K}_t)$ n'est pas estimable avec moins de 3 instantanés : la condition d'arrêt est indéfinie aux premiers tours.
- **Formulations de §1.1.**
  - « démontre » est incompatible avec le statut HYPOTHÈSE.
  - « plus de 3,3 points » est faux pour #28, dont l'écart vaut 3,29 (`illustratif`).
  - La comparaison Argon « 7 champions » contre Fable/Opus « 10 champions » est conditionnée a posteriori.
- **Attribution de la clause « *as appropriate* ».** Le socle est syntaxiquement ambigu (*Sol* ou *Astra*). L'attribuer à *Astra* avec le statut VÉRIFIÉ est risqué ; il faut lever l'ambiguïté avant de l'utiliser.
- **Texte tronqué.** La règle de décision de `M2` doit être fournie intégralement avant tout verdict du Tour 3.

FIN-DE-CELLULE