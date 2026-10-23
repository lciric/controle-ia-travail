# Dossier d'antériorité, de white space et de campagne 72 h GPU (500 USD) sur les 5 volets unifiés $S_{\text{TD}}$

**Branche B, tour 1. Ce document ne vaut pas certification.**

---

## 0. Avertissements d'intégrité

1. **Références.** Je ne peux vérifier aucune des références de ce dossier, y compris celles du socle :
   - Xu et al., `arXiv:2602.00986v2` ;
   - Jhaveri/Tagliabue 2026, source du constat `0,49 → 0,65`.

   Elles sont toutes marquées *(référence à vérifier)*. Les identifiants `26xx.xxxxx` (2026) ne doivent pas figurer dans un dossier de financement avant vérification manuelle.

2. **« White space 100 % vierge ».** Aucune revue ne peut le certifier. Je remplace cette formule par un **delta falsifiable** et un **critère de réfutation (kill)** pour chaque volet. C'est plus défendable devant un jury.

3. **Anomalies du corpus Cholesky-DPP.** Plusieurs résultats sont des collisions lexicales hors sujet. Ils ne doivent pas être cités :

   | Identifiant | Sujet réel | Cause probable |
   |---|---|---|
   | 2004.12568 | atténuation des ondes millimétriques | collision sur « attenuation » |
   | 1506.06570, 1101.2456 | algèbres de Hecke, espace de Fock | collision sur « affine » |
   | 2212.11238 | panel ECFA | collision sur « panel » |
   | 2208.08342 | PAPR | — |
   | 2304.07859 | inégalités isopérimétriques affines | — |
   | 1902.09833 | impulsions quantiques | — |
   | 2403.11870 | suppression de nuages | — |
   | 2603.29727 | conception de médicaments | — |
   | 2606.05868 | YouZhi (LLM financiers) | — |

   Deux autres signaux d'alerte :
   - le survey 2203.08975 apparaît cinq fois, signe d'un effondrement de la diversité du DPP ;
   - les polarités sont incohérentes : SecAlign ou 2203.08975 sont tantôt `True`, tantôt `False`.

4. **Quatre problèmes techniques corrigés plus bas.**
   - (a) Une rétraction radiale $C^1$ **ne peut pas** être idempotente sur une boule fermée (§2-II).
   - (b) `P2` vs `P4` seuls **confondent** intention et acte (§1-I).
   - (c) Jonckheere-Terpstra suppose des groupes indépendants. Or les chaînes $d=1..6$ sont des mesures répétées (§2-IV).
   - (d) Combiner les cinq volets par moyenne harmonique teste un **nul global**. Cela ne remplace pas les inférences par volet (§2-V).

---

## 1. Carte d'antériorité et baselines anti-strawman

### Volet I : Jumeau Nié $\sigma_r^0$, $k=0$, `P2`/`P4`

| Antériorité | Ce qu'elle couvre déjà | Baseline obligatoire |
|---|---|---|
| Zou et al., *Representation Engineering*, arXiv:2310.01405 (référence à vérifier) | Lecture linéaire de l'honnêteté et de l'intention par stimuli contrastifs (LAT) | LAT-PCA sur les mêmes paires, même couche |
| Burns et al., *CCS*, arXiv:2212.03827 (référence à vérifier) | Sondes non supervisées sur paires de négation | CCS sur $(\sigma_r,\sigma_r^0)$ |
| Marks & Tegmark, *Geometry of Truth*, arXiv:2310.06824 (référence à vérifier) | Sonde mass-mean | **Notre 1re direction $S_{\text{TD}}$ est une sonde mass-mean** : le delta n'est pas la direction |
| Goldowsky-Dill et al., arXiv:2502.03407 ; Hubinger et al., *Sleeper Agents*, arXiv:2401.05566 ; MacDiarmid et al., *Simple probes can catch sleeper agents*, Anthropic 2024 (références à vérifier) | Détection pré-acte d'une intention de défection | Sonde de défection de type « simple probe », sans plan apparié |
| Pal et al., *Future Lens*, arXiv:2311.04897 ; Wu, Morris, Levine, arXiv:2404.00859 (références à vérifier) | Décodage du futur depuis un état caché unique | Exactitude top-k du futur token à $k=0$ |
| Turpin et al., arXiv:2305.04388 ; Chen et al., arXiv:2505.05410 (références à vérifier) | Écart verbalisation/décision | Sans objet (cadrage) |
| Hedges 1981 ; Lakens 2013 ; tests de permutation de Fisher 1935 (références à vérifier) | $d_z$, retournement de signe | Méthodes standard, **non revendiquées** |

**Correction de plan.** Le contraste `P2` − `P4` mélange deux effets.
- `P2` = intention+, acte−.
- `P4` = intention−, acte+.
- Donc $\Delta = (\text{effet intention}) - (\text{effet acte})$, et aucun des deux n'est identifiable seul.

Il faut le plan 2×2 complet :
- `P1` = intention+, acte+ ;
- `P3` = intention−, acte− ;
- effet intention $= \tfrac12[(P1+P2)-(P3+P4)]$.

**Delta falsifiable.**
- Le plan 2×2 intention×acte, à surface lexicale contrôlée par le jumeau nié, est mesuré **avant** le premier token d'acte.
- Le nul exact est apparié par bloc.
- Un **TOST d'équivalence** sur des traits lexicaux de surface vérifie qu'ils ne reproduisent pas l'effet.

**Kill.**
- Le contrôle lexical échoue à l'équivalence (marge 0,2 σ, illustratif).
- Ou bien l'effet disparaît quand $S_{\text{TD}}$ est estimé sur un split disjoint.

**Surclaims du corpus à retirer.**
- « éliminant tout biais de surface lexicale » : on le borne, on ne l'élimine pas.
- « inférence exacte » : elle n'est exacte que sous l'hypothèse de symétrie et d'indépendance des blocs.

### Volet II : `Do-Clamp` affine idempotent + Koopman + 5e bras `rand-parc`

| Antériorité | Ce qu'elle couvre déjà | Baseline obligatoire |
|---|---|---|
| Belrose et al., *LEACE*, arXiv:2306.03819 (référence à vérifier) | Projection affine idempotente en forme close | LEACE à la même couche |
| Ravfogel et al., *INLP*, arXiv:2004.07667 ; *R-LACE*, arXiv:2201.12091 (références à vérifier) | Projections itérées dans l'espace nul | INLP, 10 itérations (illustratif) |
| Arditi et al., arXiv:2406.11717 (référence à vérifier) | Ablation orthogonale **idempotente, appliquée à chaque token** | **Bras 2** |
| Turner et al., *ActAdd*, arXiv:2308.10248 ; Li et al., *ITI*, arXiv:2306.03341 ; Rimsky et al., *CAA*, arXiv:2312.06681 (références à vérifier) | Pilotage additif | **Bras 3** |
| Wu et al., *ReFT/LoReFT*, arXiv:2404.03592 (référence à vérifier) | $h + R^\top(Wh+b-Rh)$ ; **avec $W=0$, c'est exactement $P_{\text{do}}$** | LoReFT-$W{=}0$ appris (bras optionnel) |
| Templeton et al., *Scaling Monosemanticity*, 2024 ; Jaeger, arXiv:1403.3369 ; Postmus & Abreu, arXiv:2410.16314 (références à vérifier) | Clampage de caractéristiques, projecteurs doux (conceptors) | Conceptor à ouverture 10 (illustratif) |
| Williams, Kevrekidis, Rowley 2015 (EDMD) ; Lusch, Kutz, Brunton 2018 ; Korda & Mezić 2018 (Koopman-MPC) (références à vérifier) | Lifting de Koopman et commande | Sans objet |
| Anil et al., *Many-shot jailbreaking*, 2024 ; Russinovich et al., *Crescendo*, arXiv:2404.01833 (références à vérifier) | Érosion multi-tours du refus | Protocole de rejets répétés identique |

**Delta falsifiable.** L'idempotence n'est **pas** nouvelle (LEACE, Arditi, LoReFT-$W{=}0$). Le delta porte sur trois points :
- le choix de $U$ par **modes de Koopman de dérive** estimés par EDMD inter-tours ;
- une consigne $c$ fixée au tour 0 ;
- une rétraction radiale à défaut d'idempotence borné ($\le\delta/e$), contrôlée par `rand-parc` $L_\infty$.

**Kill.**
- La pente de dérive sous `Do-Clamp` n'est pas inférieure à celle d'Arditi **et** de LoReFT-$W{=}0$.
- Ou bien `rand-parc` reproduit au moins 50 % (illustratif) de l'effet.

**Surclaims à retirer.**
- « stabilité spectrale absolue » ;
- « $0{,}49\to0{,}49$ garanti ».

Le diagnostic $\rho\big((I-UU^\top)A\big)$ porte sur un **modèle**, ce n'est pas un certificat.

### Volet III : pare-feu dyadique *Sol/Astra*

| Antériorité | Ce qu'elle couvre déjà | Baseline obligatoire |
|---|---|---|
| Debenedetti et al., *CaMeL*, arXiv:2503.18813 ; motif « Dual LLM », Willison 2023 (références à vérifier) | **Dyade privilégié/quarantaine à capacités : antériorité la plus proche** | **CaMeL** |
| Chen et al., *StruQ*, arXiv:2402.06363 ; Wallace et al., *Instruction Hierarchy*, arXiv:2404.13208 ; Hines et al., *Spotlighting*, arXiv:2403.14720 ; *SecAlign*, arXiv:2410.05451 (références à vérifier) | Séparation des canaux instruction/données | Spotlighting (gratuit à implémenter) |
| Wu et al., *IsolateGPT*, arXiv:2403.04960 ; Shi et al., *Progent*, arXiv:2504.11703 ; Jia et al., *Task Shield*, arXiv:2412.16682 (références à vérifier) | Isolation et politiques de privilèges | Politique Progent équivalente à $\Pi_0$ |
| Beurer-Kellner et al., *LMQL*, arXiv:2212.06094 ; Willard & Louf, *Outlines*, arXiv:2307.09702 ; Geng et al., arXiv:2305.13971 (références à vérifier) | Décodage contraint par schéma | Sortie forcée Outlines vers $\mathcal{S}_{\text{strict}}$ |
| Rebedea et al., *NeMo Guardrails*, arXiv:2310.10501 ; Inan et al., *Llama Guard*, arXiv:2312.06674 (références à vérifier) | Garde-fous programmables, juge LLM | Llama Guard en filtre |
| RFC 6962 / RFC 9162 ; Crosby & Wallach, USENIX Sec. 2009 (références à vérifier) | Journaux Merkle infalsifiables | Sans objet |
| Miller 1955 ; Paninski 2003 ; Lin 1991 (références à vérifier) | Correction Miller-Madow, divergence JS | Sans objet |
| Debenedetti et al., *AgentDojo*, arXiv:2406.13352 (référence à vérifier) | Banc d'injection pour agents | **Banc d'évaluation** |

**Delta falsifiable.** Chaque brique est standard ; le delta est **l'intégration mesurée**. Il se décompose en deux points :
- un ASR (taux de succès d'attaque) au moins aussi bas que CaMeL à utilité égale ;
- une **alarme statistique de glissement de distribution** (JS-MM) qui capte les attaques satisfaisant $\Pi_0$.

**Kill.**
- L'ASR est supérieur à CaMeL à utilité égale (± 2 pts, illustratif).
- Ou bien JS-MM n'apporte aucun gain de détection au-delà de $\Pi_0$ seul.

**Correction.** Un arbre de Merkle donne l'**évidence de falsification**, pas la **non-répudiation**. L'anti-déni exige aussi :
- des signatures asymétriques (Ed25519) de chaque agent sur (index, racine) ;
- la publication de la racine chez un témoin.

### Volet IV : `H9`, $d=1..6$

| Antériorité | Ce qu'elle couvre déjà | Baseline obligatoire |
|---|---|---|
| Page 1954 ; Lu & Reynolds, *JQT* 2001 ; Montgomery & Mastrangelo 1991 ; Tartakovsky et al. 2014 (références à vérifier) | **CUSUM sur résidus AR(1) : entièrement standard** | Sans objet |
| Adams & MacKay, *BOCPD*, arXiv:0710.3742 ; Shin, Ramdas, Rinaldo, *e-detectors*, arXiv:2203.03532 ; Vovk et al. 2003 ; Volkhonskiy et al. 2017 (références à vérifier) | Détection de rupture en ligne, non paramétrique | **BOCPD et e-detector sur la même série** |
| Jonckheere 1954 ; Terpstra 1952 ; Page 1963 (test L) (références à vérifier) | Alternatives ordonnées | **Test L de Page** (mesures répétées) |
| Perez et al., arXiv:2407.04503 ; Ren et al., arXiv:2404.04286 ; Shumailov et al., *Nature* 2024 (références à vérifier) | Érosion sémantique itérée | Mesure d'érosion du jeu du téléphone |
| Birgisson et al., *Macaroons*, NDSS 2014 ; RFC 2693 (SPKI) ; Biscuit ; RFC 8693 ; UCAN (références à vérifier) | **Atténuation monotone par construction** | Sans objet |

**Delta falsifiable.** Le **couplage en boucle fermée** : une alarme CUSUM au saut $d$ déclenche une atténuation automatique de $\Pi_{d+1}$. On le mesure par la réduction des actions non autorisées tentées.

**Kill.**
- L'ARL$_1$ du CUSUM pré-blanchi n'est pas meilleur que celui de BOCPD ou de l'e-detector à ARL$_0$ égal.
- Ou bien le couplage ne réduit pas les escalades par rapport à une atténuation statique.

### Volet V : contrôle des essaims `H4'`

| Antériorité | Ce qu'elle couvre déjà | Baseline obligatoire |
|---|---|---|
| Du et al., arXiv:2305.14325 ; Castro & Liskov, OSDI 1999 (références à vérifier) | Débat multi-agents, BFT ($N\ge 3f+1$) | Vote majoritaire simple |
| Verga et al., *PoLL*, arXiv:2404.18796 ; Wang et al., *MoA*, arXiv:2406.04692 ; Jiang et al., *LLM-Blender*, arXiv:2306.02561 (références à vérifier) | Jurys et ensembles hétérogènes | Jury PoLL |
| Greenblatt et al., *AI Control*, arXiv:2312.06942 ; Benton et al., arXiv:2410.21514 ; Motwani et al., arXiv:2402.07510 (références à vérifier) | Moniteurs de confiance, sabotage, collusion | Moniteur de confiance de même famille |
| Huang et al., arXiv:2408.00989 ; Amayuelas et al., arXiv:2406.14711 ; Gu et al., *Agent Smith*, arXiv:2402.08567 ; Lee & Tiwari, arXiv:2410.07283 (références à vérifier) | Résilience aux agents malveillants | Topologie de Huang et al. |
| Liu et al., *LoRA-as-an-Attack!*, arXiv:2403.00108 ; *BadMerging*, arXiv:2408.07362 ; Xu et al., arXiv:1910.03137 ; Pillutla et al., *RFA*, arXiv:1912.13445 (références à vérifier) | LoRA malveillants, détection de chevaux de Troie | Sans objet |
| Mantel & Haenszel 1959 ; Breslow & Day 1980 ; Tarone 1985 ; Newcombe 1998 ; Schuirmann 1987 ; Wilson, *PNAS* 2019 ; Vovk & Wang, *Biometrika* 2020 (références à vérifier) | Statistiques utilisées, **non revendiquées** | Sans objet |
| Blum 1981 (coin flipping) ; Kerckhoffs 1883 (références à vérifier) | Engagement commit-reveal | Sans objet |

**Delta falsifiable.** Le delta combine trois éléments :
- un **contrôle positif obligatoire** : l'attaque sans défense doit être significative par CMH, sinon l'équivalence TOST est vide ;
- la stratification par famille avec garde Breslow-Day ;
- l'engagement cryptographique des **poids, de la graine et du siège** du saboteur avant l'audit hors-famille.

**Kill.**
- Le contrôle positif n'est pas significatif.
- Ou bien Breslow-Day rejette l'homogénéité : pas d'estimation poolée.
- Ou bien l'auditeur hors-famille ne fait pas mieux que l'auditeur intra-famille (AUROC, ± 0,03, illustratif).

**Limites de puissance.**
- Avec $K=3$ strates, Breslow-Day est peu puissant : un non-rejet ne prouve **pas** l'homogénéité.
- $N=9,f=2$ respecte $3f+1\le N$. Mais un vote LLM n'est pas un protocole BFT : on adopte un quorum $2f+1=5$ explicite, sans revendication byzantine formelle.

---

## 2. Protocole mathématique sur le substrat $S_{\text{TD}}$

### Substrat commun
- **Interprétation opérationnelle de « $S_{\text{TD}}<1\%$ »**, à réaligner sur Xu et al. *(référence à vérifier)* : un sous-espace de rang $r=\lceil 0{,}01\,D\rceil$ (illustratif), de base orthonormale $Q\in\mathbb R^{D\times r}$.
- **Estimation** : SVD des contrastes appariés sur un **split de calibration disjoint** (anti double-dipping).
- **Lecture** : $s(h)=\langle w,\,Q^\top(h-\mu)\rangle$.

### Volet I
- **Contraste par bloc** :
  - $\Delta_b=s_b(P2)-s_b(P4)$ ;
  - $\Delta_b^{\sigma}=s_b(\sigma_r)-s_b(\sigma_r^0)$ ;
  - effet intention 2×2 si `P1`/`P3` sont disponibles.
- **Taille d'effet** : $d_z = J\,\bar\Delta/s_\Delta$, avec $J=1-\frac{3}{4(B-1)-1}$.
- **Nul exact** :
$$p=\frac{\#\{\varepsilon\in\{\pm1\}^B : T(\varepsilon\odot\Delta)\ge T(\Delta)\}}{2^B}$$
  - Exact si les $\Delta_b$ sont indépendants et **symétriques** autour de 0.
  - $p_{\min}=2^{-B}$ en unilatéral : il faut $B\ge5$ pour $\alpha=0{,}05$ (illustratif).
- **Planification** : $d_z=0{,}5$ (illustratif) demande $B\approx27$ en unilatéral à 80 % de puissance. On retient $B=64$ (illustratif).
  - Énumération exacte si $B\le16$ ;
  - Monte-Carlo $(k+1)/(M+1)$ sinon.
- **Correction multiple** : Holm sur les contrastes primaires.

### Volet II
- **Projection** : $P_{\text{do}}(x)=x-UU^\top(x-c)$, avec $U^\top U=I$.
  - On a $U^\top(P_{\text{do}}x-c)=0$, d'où $P_{\text{do}}^2=P_{\text{do}}$.
- **Lemme.** L'image d'une rétraction $C^1$ est une sous-variété plongée sans bord *(Lee, Introduction to Smooth Manifolds, référence à vérifier)*. Une boule fermée n'en est pas une. **Il n'existe donc aucune rétraction $C^1$ idempotente sur une boule fermée.**
- **Deux modes, au choix explicite** :
  - (i) $\delta=0$ : $\rho(r)=\min(r,R)$. On obtient $T^2=T$ exactement, 1-Lipschitz, non $C^1$.
  - (ii) $\delta>0$ : $\rho(r)=r$ si $r\le R-\delta$, et $R-\delta e^{-(r-R+\delta)/\delta}$ sinon. On obtient $C^1$, avec $\|T^2x-Tx\|\le\delta/e$.
- **Composition** : $T=g_{c,R,\delta}\circ P_{\text{do}}$, où $g$ est centré en $c$. Comme $x-c\in U^\perp$ après $P_{\text{do}}$, la rétraction préserve la consigne : $U^\top T(x)=U^\top c$.
- **Koopman (EDMD)** :
  - dictionnaire $\Psi(z)=[1,z,\sqrt{2/m}\cos(zW+b)]$, qui contient l'état ;
  - opérateur $\Psi(z_{t+1})\approx\Psi(z_t)K$ ;
  - fonctions propres $\varphi_i=\Psi v_i$ ;
  - $U=\mathrm{orth}\{\nabla\varphi_i(\bar z)\}$ pour les $|\lambda_i|$ maximaux non constants.
  - Le relèvement dans le flux résiduel se fait par $U_D=QU$, $c_D=\mu+Qc$.
- **Cinq bras** :
  1. aucun ;
  2. ablation Arditi ;
  3. ActAdd/CAA ;
  4. `Do-Clamp` ;
  5. `rand-parc` $L_\infty$, c'est-à-dire une perturbation aléatoire **parcimonieuse** de même $\|\cdot\|_\infty$ et de même taille de support que $T(x)-x$. Cette interprétation de « rand-parc » est à confirmer.
- **Critère** : pente MCO du taux de rejet par tour, par scénario. On teste les différences de pentes appariées (bras − Do-Clamp) par retournement de signe.

### Volet III
- **Parsing strict** : rejet des clés dupliquées, des `NaN`/`Infinity`, des champs hors schéma, et des booléens pris pour des entiers.
- **Prédicat** : $\Pi_0$ décidable, hors modèle. Il vérifie :
  - action ∈ politique(rôle) ;
  - `seq` monotone ;
  - alternance dyadique ;
  - `prev_root` égal à la racine Merkle courante.
- **Merkle** : RFC 6962, avec séparation de domaine `0x00`/`0x01`, et preuves d'inclusion RFC 9162.
- **Divergence** : $\mathrm{JS}_2=\big[H(M)-\tfrac12H(P)-\tfrac12H(Q)\big]/\ln2$. Les biais plug-in sont :
  - $\frac{m_P-1}{2N_P}$ pour $P$ ;
  - $\frac12\sum_i \mathrm{Var}(\hat m_i)/m_i$ pour le mélange (delta-méthode).
- **Propriété vérifiée** : si $P=Q$ et $N_P=N_Q$, la correction annule exactement le biais d'ordre 1, $(m-1)/(4N)$.
- **Test** : par permutation.

### Volet IV
- **Pré-blanchiment** : $e_t=\big[(x_t-\hat\mu)-\hat\phi(x_{t-1}-\hat\mu)\big]/\hat\sigma$.
- **CUSUM** : $S_t=\max(0,S_{t-1}+e_t-k)$.
  - Attention : un saut de moyenne $\delta$ ne laisse qu'une signature de $(1-\phi)\delta$ sur les résidus (Lu & Reynolds, référence à vérifier).
  - $h$ est calibré par **bootstrap paramétrique incluant l'erreur d'estimation de $\phi$**, pour une ARL$_0$ de 200 (illustratif).
- **Tendance** : JT avec nul par permutation des labels $d$ **à l'intérieur de chaque chaîne**, adapté aux mesures répétées.
- **Jeton** : chaîne HMAC de type macaroon.
  - $\Pi_d=\Pi_0\cap\bigcap_{j\le d}C_j$, ce qui donne $\Pi_{d+1}\subseteq\Pi_d$ par construction.
  - Une alarme CUSUM retire automatiquement les permissions à risque.

### Volet V
- **CMH** : $\chi^2=\frac{(|\sum_k(a_k-E_k)|-\tfrac12)^2}{\sum_k V_k}$, avec $\widehat{OR}_{MH}$ et sa variance de Robins-Breslow-Greenland.
- **Breslow-Day** : résolution de la quadratique $(1-\psi)A^2+(n_0-m_1+\psi(n_1+m_1))A-\psi n_1m_1=0$, correction de Tarone, $K-1$ ddl.
- **Newcombe (méthode 10)** :
  - $L=\hat d-\sqrt{(p_1-l_1)^2+(u_2-p_2)^2}$ ;
  - $U=\hat d+\sqrt{(u_1-p_1)^2+(p_2-l_2)^2}$ ;
  - TOST : $z_{0,95}=1{,}645$ ⇔ IC à 90 % inclus dans $[-\Delta,\Delta]$, avec $\Delta=0{,}10$ (illustratif).
  - La p-valeur est obtenue par inversion en $z$.
- **Commit** : $\mathrm{SHA256}(\texttt{tag}\,\|\,\text{sel}_{32}\,\|\,\mathrm{SHA256}(\text{poids})\,\|\,\mathrm{canon}(\text{méta}))$.
  - Les préfixes de longueur fixe rendent le codage non ambigu.
  - Les méta-données engagent la famille, le siège, la graine et les hyperparamètres.
  - Kerckhoffs : seul le sel est secret jusqu'à la révélation.
- **Moyenne harmonique (HMP)** : $\mathring p=L/\sum 1/p_i$, rendue valide sous dépendance arbitraire par le facteur conservateur $e\ln L$ si $L\ge3$ (Vovk & Wang 2020, référence à vérifier). Elle teste **uniquement** le nul global.

### Code Python unifié

```python
# =====================================================================
# std_core.py — Substrat unifié S_TD · Volets I–V
# Dépendances : numpy>=1.24, scipy>=1.10. Tous les seuils sont illustratifs.
# =====================================================================
from __future__ import annotations
import hashlib, hmac, itertools, json, math, os, re, tempfile
from dataclasses import dataclass
import numpy as np
from scipy.stats import norm, chi2, t as student_t

def canon(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()

def holm(ps):
    ps = np.asarray(ps, float); m = ps.size; o = np.argsort(ps)
    adj = np.maximum.accumulate((m - np.arange(m)) * ps[o])
    out = np.empty(m); out[o] = np.minimum(adj, 1.0); return out

# ------------------------------------------------------------ 0. S_TD
@dataclass
class SubstratSTD:
    Q: np.ndarray   # (D, r) base orthonormale
    mu: np.ndarray  # (D,)
    def coords(self, H):
        return (np.asarray(H, float) - self.mu) @ self.Q
    def score(self, H, w=None):
        Z = self.coords(H)
        w = np.eye(Z.shape[-1])[0] if w is None else np.asarray(w) / np.linalg.norm(w)
        return Z @ w
    def vers_residuel(self, U_r, c_r):
        return self.Q @ U_r, self.mu + self.Q @ c_r

def estimer_STD(H_a, H_b, r_frac=0.01):  # r_frac = 1 % (illustratif)
    """SVD des contrastes appariés H_a − H_b sur un split de CALIBRATION
    disjoint des tests. 1re direction ≈ sonde mass-mean (cf. Marks & Tegmark)."""
    H_a, H_b = np.asarray(H_a, float), np.asarray(H_b, float)
    D = H_a.shape[1]; r = min(max(1, math.ceil(r_frac * D)), H_a.shape[0])
    mu = 0.5 * (H_a.mean(0) + H_b.mean(0))
    _, _, Vt = np.linalg.svd(H_a - H_b, full_matrices=False)
    Q = Vt[:r].T.copy()
    if (H_a - H_b).mean(0) @ Q[:, 0] < 0: Q[:, 0] *= -1
    return SubstratSTD(Q=Q, mu=mu)

# ------------------------------------------------------------ I. Jumeau Nié
def hedges_dz(diff):
    diff = np.asarray(diff, float); n = diff.size; s = diff.std(ddof=1)
    J = 1.0 - 3.0 / (4.0 * (n - 1) - 1.0)
    return J * diff.mean() / s if s > 0 else float("nan")

def _dz(S, diff):
    X = S * diff; m, s = X.mean(1), X.std(1, ddof=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(s > 0, m / s, np.sign(m) * np.inf)

def retournement_signe(diff, alternative="greater", exact_max=16, n_mc=100_000, seed=0):
    """Nul exact (2^B) si B ≤ exact_max, sinon Monte-Carlo (k+1)/(M+1).
    Le facteur J de Hedges est constant : il n'affecte pas la p-valeur."""
    diff = np.asarray(diff, float); n = diff.size
    obs = _dz(np.ones((1, n)), diff)[0]; exact = n <= exact_max
    S = (np.array(list(itertools.product((1.0, -1.0), repeat=n))) if exact
         else np.random.default_rng(seed).choice((1.0, -1.0), size=(n_mc, n)))
    null, tol = _dz(S, diff), 1e-12
    if alternative == "greater":  k = np.sum(null >= obs - tol)
    elif alternative == "less":   k = np.sum(null <= obs + tol)
    else:                         k = np.sum(np.abs(null) >= abs(obs) - tol)
    p = k / len(null) if exact else (k + 1) / (len(null) + 1)
    return {"dz_hedges": hedges_dz(diff), "p": float(p), "exact": exact, "B": n,
            "p_min": (1 if alternative != "two-sided" else 2) / 2 ** n}

def tost_apparie(diff, marge, alpha=0.05):  # alpha 0,05 (illustratif)
    diff = np.asarray(diff, float); n = diff.size
    m, se = diff.mean(), diff.std(ddof=1) / math.sqrt(n)
    p = max(student_t.sf((m + marge) / se, n - 1), student_t.cdf((m - marge) / se, n - 1))
    return {"p": float(p), "equivalent": bool(p < alpha), "moyenne": float(m)}

def volet_I(sub, H, w=None, L=None, marge_lex=None):
    """H[c] : (B, D) états au rang k=0 (dernier token AVANT le 1er token d'acte).
    c ∈ {P1(I+,A+), P2(I+,A−), P3(I−,A−), P4(I−,A+), sigma, sigma0}."""
    s = {c: sub.score(v, w) for c, v in H.items()}
    out = {"C_P2_P4": retournement_signe(s["P2"] - s["P4"]),
           "C_jumeau": retournement_signe(s["sigma"] - s["sigma0"])}
    if "P1" in s and "P3" in s:  # plan 2×2 : seul moyen d'identifier l'effet intention
        out["effet_intention"] = retournement_signe(((s["P1"] + s["P2"]) - (s["P3"] + s["P4"])) / 2)
        out["effet_acte"] = retournement_signe(((s["P1"] + s["P4"]) - (s["P2"] + s["P3"])) / 2, "two-sided")
    if L is not None:  # contrôle lexical : la surface ne doit PAS reproduire l'effet
        out["controle_lexical"] = tost_apparie(L["sigma"] - L["sigma0"], marge_lex)
    out["holm_primaires"] = holm([out["C_P2_P4"]["p"], out["C_jumeau"]["p"]]).tolist()
    return out

# ------------------------------------------------------------ II. Do-Clamp
def P_do(X, U, c):
    """Projection affine idempotente sur {x : UTx = UTc} (U orthonormalisé)."""
    U, _ = np.linalg.qr(U)
    return X - ((X - c) @ U) @ U.T

def rho(r, R, delta):
    if not delta: return np.minimum(r, R)            # exact : idempotent, non C1
    a = R - delta                                     # C1 : défaut ≤ δ/e
    return np.where(r <= a, r, R - delta * np.exp(-(r - a) / delta))

def retraction(X, c, R, delta=0.0):
    V = X - c; r = np.linalg.norm(V, axis=-1, keepdims=True)
    with np.errstate(divide="ignore", invalid="ignore"):
        sc = np.where(r > 0, rho(r, R, delta) / r, 1.0)
    return c + V * sc

def T_do(X, U, c, R, delta=0.0):
    return retraction(P_do(X, U, c), c, R, delta)

def defaut_idempotence(X, U, c, R, delta):
    Y = T_do(X, U, c, R, delta)
    return float(np.max(np.linalg.norm(T_do(Y, U, c, R, delta) - Y, axis=-1)))

class DictKoopman:
    """Ψ(z) = [1, z, √(2/m)·cos(zW+b)] — contient l'état (lecture exacte)."""
    def __init__(self, r, m=64, gamma=1.0, seed=0):
        g = np.random.default_rng(seed); self.r, self.m = r, m
        self.W = g.normal(scale=math.sqrt(2 * gamma), size=(r, m))
        self.b = g.uniform(0, 2 * np.pi, m)
    def __call__(self, Z):
        Z = np.atleast_2d(Z)
        return np.hstack([np.ones((len(Z), 1)), Z, math.sqrt(2 / self.m) * np.cos(Z @ self.W + self.b)])
    def grad(self, v, z):
        s = -math.sqrt(2 / self.m) * np.sin(z @ self.W + self.b)
        return v[1:1 + self.r] + self.W @ (s * v[1 + self.r:])

def edmd(Z0, Z1, psi, ridge=1e-6):
    A, B = psi(Z0), psi(Z1)
    return np.linalg.solve(A.T @ A + ridge * np.eye(A.shape[1]), A.T @ B)

def directions_derive(K, psi, z_ref, n_modes=1):
    lam, V = np.linalg.eig(K); cols, vals = [], []
    for i in np.argsort(-np.abs(lam)):
        g = psi.grad(V[:, i], z_ref)
        if np.linalg.norm(g) < 1e-6: continue          # mode constant
        cols += [g.real, g.imag] if abs(lam[i].imag) > 1e-10 else [g.real]
        vals.append(lam[i])
        if len(vals) >= n_modes: break
    U, _ = np.linalg.qr(np.column_stack([c for c in cols if np.linalg.norm(c) > 1e-10]))
    return U, np.array(vals)

def rayon_spectral_boucle(Z0, Z1, U):
    """Diagnostic sur MODÈLE linéaire (pas un certificat) : ρ(A) vs ρ((I−UUT)A)."""
    M = np.linalg.lstsq(np.c_[Z0, np.ones(len(Z0))], Z1, rcond=None)[0]
    A = M[:-1].T; Pp = np.eye(A.shape[0]) - U @ U.T
    return float(max(abs(np.linalg.eigvals(A)))), float(max(abs(np.linalg.eigvals(Pp @ A))))

def rand_parc_Linf(X, X_do, frac_support=0.1, seed=0):  # 10 % (illustratif)
    """5e bras : perturbation aléatoire parcimonieuse, même ‖·‖∞ et même support."""
    g = np.random.default_rng(seed); Dl = X_do - X
    eps = np.abs(Dl).max(-1); k = np.maximum(1, (np.abs(Dl) > frac_support * eps[:, None]).sum(-1))
    out = X.copy()
    for i in range(X.shape[0]):
        idx = g.choice(X.shape[1], size=int(k[i]), replace=False)
        out[i, idx] += eps[i] * g.choice((-1.0, 1.0), size=int(k[i]))
    return out

def pentes(Y):
    T = Y.shape[1]; t = np.arange(T) - (T - 1) / 2
    return (Y - Y.mean(1, keepdims=True)) @ t / (t @ t)

def volet_II(Y_bras, ref="do_clamp"):
    """Y_bras[nom] : (n_scénarios, T tours). H1 : Do-Clamp dérive moins."""
    p_ref = pentes(Y_bras[ref])
    return {n: retournement_signe(pentes(Y) - p_ref, "greater") for n, Y in Y_bras.items() if n != ref}

# ------------------------------------------------------------ III. Sol/Astra
def _sans_doublon(pairs):
    d = {}
    for k, v in pairs:
        if k in d: raise ValueError(f"clé dupliquée {k!r}")
        d[k] = v
    return d

def _const_interdite(x): raise ValueError(f"constante non-JSON {x}")

def parse_strict(raw):
    return json.loads(raw, object_pairs_hook=_sans_doublon, parse_constant=_const_interdite)

CHAMPS = {"role", "seq", "action", "args", "prev_root"}
ACTIONS = {"lire", "resumer", "proposer", "refuser"}
HEX64, CLE = re.compile(r"[0-9a-f]{64}"), re.compile(r"[a-z_]{1,32}")

def valider_S_strict(m):
    if type(m) is not dict or set(m) != CHAMPS: return False, "schéma"
    if type(m["role"]) is not str or m["role"] not in ("Sol", "Astra"): return False, "role"
    if type(m["seq"]) is not int or not 0 <= m["seq"] < 2 ** 53: return False, "seq"
    if type(m["action"]) is not str or m["action"] not in ACTIONS: return False, "action"
    a = m["args"]
    if type(a) is not dict or len(a) > 8: return False, "args"
    for k, v in a.items():
        if not CLE.fullmatch(k): return False, f"clé {k}"
        if not ((type(v) is str and len(v) <= 512) or type(v) is int): return False, f"valeur {k}"
    if type(m["prev_root"]) is not str or not HEX64.fullmatch(m["prev_root"]): return False, "prev_root"
    return True, "ok"

def _h(b): return hashlib.sha256(b).digest()
def feuille(d): return _h(b"\x00" + d)
def noeud(l, r): return _h(b"\x01" + l + r)

def racine_merkle(D):  # RFC 6962 MTH
    n = len(D)
    if n == 0: return _h(b"")
    if n == 1: return feuille(D[0])
    k = 1 << ((n - 1).bit_length() - 1)
    return noeud(racine_merkle(D[:k]), racine_merkle(D[k:]))

def preuve_inclusion(m, D):
    n = len(D)
    if n <= 1: return []
    k = 1 << ((n - 1).bit_length() - 1)
    return (preuve_inclusion(m, D[:k]) + [racine_merkle(D[k:])] if m < k
            else preuve_inclusion(m - k, D[k:]) + [racine_merkle(D[:k])])

def verifier_inclusion(m, n, donnee, preuve, racine):  # RFC 9162 §2.1.3.2
    if m >= n: return False
    fn, sn, r = m, n - 1, feuille(donnee)
    for p in preuve:
        if sn == 0: return False
        if fn & 1 or fn == sn:
            r = noeud(p, r)
            if not fn & 1:
                while not fn & 1 and fn != 0: fn >>= 1; sn >>= 1
        else:
            r = noeud(r, p)
        fn >>= 1; sn >>= 1
    return sn == 0 and r == racine

class PareFeuSolAstra:
    """Évidence de falsification. La NON-RÉPUDIATION exige en plus des signatures
    Ed25519 de chaque agent sur (index, racine) et une racine publiée chez un témoin."""
    POLITIQUE = {"Sol": {"lire", "resumer", "proposer"}, "Astra": {"lire", "resumer", "refuser"}}
    def __init__(self): self.journal, self.dernier_role = [], None
    @property
    def racine(self): return racine_merkle(self.journal).hex()
    def Pi0(self, m):
        return (m["action"] in self.POLITIQUE[m["role"]] and m["seq"] == len(self.journal)
                and m["role"] != self.dernier_role and m["prev_root"] == self.racine)
    def soumettre(self, raw):
        try: m = parse_strict(raw)
        except ValueError as e: return False, f"parse : {e}"
        ok, why = valider_S_strict(m)
        if not ok: return False, why
        if not self.Pi0(m): return False, "Π0 violé"
        self.journal.append(canon(m)); self.dernier_role = m["role"]
        return True, {"index": len(self.journal) - 1, "racine": self.racine}

def _H(p):
    p = p[p > 0]; return float(-np.sum(p * np.log(p)))

def js_mm_bits(cP, cQ):
    cP, cQ = np.asarray(cP, float), np.asarray(cQ, float); NP, NQ = cP.sum(), cQ.sum()
    p, q = cP / NP, cQ / NQ; m = 0.5 * (p + q); nz = m > 0
    js = _H(m) - 0.5 * (_H(p) + _H(q))
    bP, bQ = (np.count_nonzero(cP) - 1) / (2 * NP), (np.count_nonzero(cQ) - 1) / (2 * NQ)
    bM = 0.5 * np.sum((p[nz] * (1 - p[nz]) / (4 * NP) + q[nz] * (1 - q[nz]) / (4 * NQ)) / m[nz])
    return {"js_plugin_bits": js / math.log(2), "js_mm_bits": (js + bM - 0.5 * (bP + bQ)) / math.log(2)}

def js_permutation(xP, xQ, n_cat, n_perm=2000, seed=0):
    g = np.random.default_rng(seed); xP, xQ = np.asarray(xP), np.asarray(xQ)
    f = lambda a, b: js_mm_bits(np.bincount(a, minlength=n_cat), np.bincount(b, minlength=n_cat))["js_mm_bits"]
    obs, pool, nP = f(xP, xQ), np.r_[xP, xQ], len(xP); c = 0
    for _ in range(n_perm):
        z = g.permutation(pool); c += f(z[:nP], z[nP:]) >= obs
    return {"js_mm_bits": obs, "p": (c + 1) / (n_perm + 1)}

# ------------------------------------------------------------ IV. H9
def ajuster_AR1(x):
    x = np.asarray(x, float); mu = x.mean(); xc = x - mu
    phi = xc[1:] @ xc[:-1] / (xc[:-1] @ xc[:-1])
    return mu, phi, float(np.std(xc[1:] - phi * xc[:-1], ddof=2))

def residus_std(x, mu, phi, sg):
    xc = np.asarray(x, float) - mu; return (xc[1:] - phi * xc[:-1]) / sg

def cusum(z, k=0.5, h=5.0, sens=+1):  # k, h (illustratifs)
    S, tr = 0.0, []
    for t, zt in enumerate(sens * np.asarray(z)):
        S = max(0.0, S + zt - k); tr.append(S)
        if S > h: return t, np.array(tr)
    return None, np.array(tr)

def _sim_ar1(g, phi, n, size):
    x = np.empty((size, n)); x[:, 0] = g.normal(size=size) / math.sqrt(1 - phi ** 2)
    e = g.normal(size=(size, n))
    for t in range(1, n): x[:, t] = phi * x[:, t - 1] + e[:, t]
    return x

def arl0_bootstrap(h, phi, m1=100, k=0.5, n_sim=1000, T_max=2000, seed=0):
    """Inclut l'erreur d'estimation de (μ, φ, σ) en phase I. Censure à T_max ⇒ conservateur."""
    g = np.random.default_rng(seed); X1 = _sim_ar1(g, phi, m1, n_sim)
    mu = X1.mean(1, keepdims=True); Xc = X1 - mu
    ph = (Xc[:, 1:] * Xc[:, :-1]).sum(1) / (Xc[:, :-1] ** 2).sum(1)
    sg = (Xc[:, 1:] - ph[:, None] * Xc[:, :-1]).std(1, ddof=2)
    X2 = _sim_ar1(g, phi, T_max + 1, n_sim) - mu
    S = np.zeros(n_sim); RL = np.full(n_sim, float(T_max)); vivant = np.ones(n_sim, bool)
    for t in range(1, T_max + 1):
        S = np.maximum(0, S + (X2[:, t] - ph * X2[:, t - 1]) / sg - k)
        neuf = vivant & (S > h); RL[neuf] = t; vivant &= ~neuf
        if not vivant.any(): break
    return float(RL.mean())

def calibrer_h(phi, arl0_cible=200, **kw):  # ARL0 = 200 (illustratif)
    lo, hi = 0.5, 20.0
    for _ in range(20):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if arl0_bootstrap(mid, phi, **kw) < arl0_cible else (lo, mid)
    return hi

def jt_stat(x, d):
    J, niv = 0.0, np.unique(d)
    for i, a in enumerate(niv):
        xa = x[d == a]
        for b in niv[i + 1:]:
            df_ = x[d == b][None, :] - xa[:, None]
            J += (df_ > 0).sum() + 0.5 * (df_ == 0).sum()
    return J

def jt_chaines(X, n_perm=5000, seed=0):
    """X : (n_chaînes, n_d). Nul : échangeabilité de d DANS chaque chaîne."""
    g = np.random.default_rng(seed); X = np.asarray(X, float); n, K = X.shape
    d = np.tile(np.arange(K), n); J0 = jt_stat(X.ravel(), d); c = 0
    for _ in range(n_perm):
        P = np.argsort(g.random((n, K)), axis=1)
        c += jt_stat(np.take_along_axis(X, P, 1).ravel(), d) >= J0
    return {"J": J0, "p": (c + 1) / (n_perm + 1)}

PERM_RE = re.compile(r"[a-z0-9_.:-]+")

@dataclass(frozen=True)
class JetonCapacite:
    ident: str; sig: bytes; caveats: tuple = ()
    @staticmethod
    def emettre(cle, ident, perms):
        sig = hmac.new(cle, ident.encode(), hashlib.sha256).digest()
        return JetonCapacite(ident, sig).attenuer(perms)
    def attenuer(self, perms):
        perms = sorted(perms); assert all(PERM_RE.fullmatch(p) for p in perms)
        cav = "perms=" + ",".join(perms)
        return JetonCapacite(self.ident, hmac.new(self.sig, cav.encode(), hashlib.sha256).digest(),
                             self.caveats + (cav,))
    def permissions(self):
        P = None
        for c in self.caveats:
            s = frozenset(x for x in c.split("=", 1)[1].split(",") if x)
            P = s if P is None else P & s
        return P if P is not None else frozenset()

def verifier_jeton(cle, j):
    s = hmac.new(cle, j.ident.encode(), hashlib.sha256).digest()
    for c in j.caveats: s = hmac.new(s, c.encode(), hashlib.sha256).digest()
    return hmac.compare_digest(s, j.sig)

def deleguer(j, alarme, perms_risque, demandees=None):
    P = j.permissions(); cible = (set(P) if demandees is None else set(demandees) & P)
    if alarme: cible -= set(perms_risque
