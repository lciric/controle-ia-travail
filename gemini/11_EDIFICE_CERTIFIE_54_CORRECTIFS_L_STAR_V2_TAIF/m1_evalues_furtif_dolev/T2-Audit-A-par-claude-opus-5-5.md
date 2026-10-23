FAILLES_PROUVEES_PAR_AUDITEUR: 16

Le décompte ci-dessus est établi par l'auditeur, indépendamment de tout chiffre de l'auteur. Le texte est tronqué au niveau de `MonotoneCapToken.__init__`, et rien n'est imputé à la partie manquante.

---

## Volet I : Jumeau Nié, $S_{\text{TD}}$, $d_z$

**F1. Le centrage dans `fit_S_TD` détruit le signal recherché.**
`D = D - D.mean(0)` retire précisément le contraste moyen P4−P2. La SVD de la matrice centrée renvoie la direction de **variance** maximale des différences, pas celle du décalage moyen.
- Contre-exemple : soit $\delta_i = \mu + \varepsilon_i$ avec $\varepsilon_i$ isotrope. Alors $D_c = \varepsilon$ et $u_1$ est aléatoire, avec $|\langle u_1, \mu/\|\mu\|\rangle| \sim d^{-1/2}$. La direction est donc quasi orthogonale à l'effet.
- Correctif : SVD non centrée ($D^\top D$), ou $\hat\mu/\|\hat\mu\|$.

**F2. Double usage des données (circularité) : le « nul exact » n'est plus exact.**
$u_1$ est estimé sur les mêmes $\delta_i$ que ceux qui sont ensuite testés par retournement de signe. Avec centrage, $u_1$ dépend de la configuration de signes : l'échangeabilité conditionnelle est rompue et le niveau n'est plus garanti.
- Correctif : ajustement sur un pli A et test sur un pli B.
- Alternative : SVD **non centrée**. $D^\top D$ est alors invariant aux retournements de lignes, ce qui restaure l'exactitude du test.

**F3. Incohérence du plan contrôlé.**
Le texte place la négation « en amont, hors fenêtre lexicale visible à $k=0$ ». Dans un décodeur causal, tout ce qui est en amont dans le contexte est visible à $k=0$. Il y a donc deux cas :
- soit la négation est dans le prompt, et B-I.3 doit la détecter : la « surface lexicale identique » est fausse ;
- soit elle n'y est pas, et le bras n'est pas défini.

Par ailleurs, la statistique n'utilise que P4−P2. Le bras $\sigma_r^0$ n'intervient dans aucun test.

**F4. Le détecteur de canal subliminal $\max_k \Psi(k)/\text{median}_j\Psi(j)$ est mal défini et non calibré.**
- $\Psi$ est défini plus loin comme dictionnaire Koopman vectoriel : le ratio scalaire n'a pas de sens.
- Un maximum sur $K$ positions croît mécaniquement (≈ $\sqrt{2\ln K}$ sous un nul gaussien). Aucune distribution nulle ni aucun niveau ne sont fournis.
- Masquer en `<PAD>` *les seules* clauses modales laisse passer les autres porteurs lexicaux. Les PAD insérés introduisent en outre une perturbation positionnelle hors distribution, ce qui est confondant.
- Correctif : nul par permutation de la statistique max, et contrôle lexical complet.

**Vérifié sain, non signalé :**
- $J(\nu)=1-3/(4\nu-1)$ avec $\nu=n-1$ ;
- énumération $2^B$ et estimateur MC $(hits+1)/(total+1)$ ;
- Ledoit-Wolf en float64 hors BOS ;
- score de Brier (règle strictement propre, perte nulle en $y=\mu=0$ correcte) ;
- $r\le\lfloor 40{,}96\rfloor = 40$.

---

## Volet II : Do-Clamp, Koopman, rétraction

**F5. La preuve de stabilité ignore la dynamique du modèle entre les tours.**
La suite $\rho_n=r(\rho_{n-1})$ suppose que $\mathcal C$ est itéré sur lui-même. En réalité, l'état suit $z_{t+1}=F(\mathcal C(z_t))$, où $F$ est la dynamique du LLM et des rejets.
- La seule borne démontrée est $\|\mathcal C(z)-c\|<R$ juste après l'intervention, ce qui est trivial par tanh.
- « Converge vers $a$ » et « pas d'accumulation sous $n$ rejets » ne sont pas prouvés sans hypothèse sur $F$ (contraction, ou dérive bornée).

**F6. La projection dans l'espace lifté n'est pas réalisable dans le flux résiduel et perd l'idempotence.**
$U\in\mathbb R^{m\times q}$ agit sur $[x;\phi(x)]$. Le résultat n'a en général aucune préimage par $\Psi$, puisque la partie $\phi$ projetée n'est plus égale à $\phi$(partie $x$).
- L'opérateur effectivement injectable est $x\mapsto c_x + v_x - U_x(U_x^\top v_x + U_\phi^\top(\phi(x)-\phi(c)))$.
- Cet opérateur est non linéaire en $x$ et n'est pas idempotent, car $U_x$ n'est pas orthonormée.
- De plus, les vecteurs propres de $K^\top$ sont complexes et non orthogonaux. L'orthonormalisation réelle n'est pas spécifiée.

**F7. Le 5e bras `rand-parc` n'est pas apparié en magnitude.**
$\delta=-UU^\top(z-c)$ est génériquement **dense** (support $=d$). Apparier support et $L_\infty$ donne alors $\|\varepsilon\|_2=\|\delta\|_\infty\sqrt d \ge \|\delta\|_2$.
- Pour des composantes quasi gaussiennes, le ratio vaut ≈ $\sqrt{2\ln d}\approx 4{,}1$ en norme, soit environ 17× en énergie, pour $d=4096$.
- Le contrôle « magnitude vs direction » est donc biaisé.
- Correctif : apparier la norme $L_2$, via une direction aléatoire de même rang $q$.

**F8. Le critère « IC contenant 0 » relève du sophisme de l'absence de preuve.**
Un IC qui contient 0 ne démontre pas l'absence de dérive : il suffit d'un $n$ faible pour l'obtenir.
- Correctif : test d'équivalence TOST avec une marge pré-enregistrée.

**Vérifié sain, non signalé :**
- $Q^2=Q$ et l'idempotence de $P_{\text{do}}$ ;
- le caractère $C^1$ de $r$ en $a$ ;
- la non-idempotence globale admise ;
- le quantile conforme $\lceil (n+1)(1-\alpha)\rceil/n$ gelé hors ligne ;
- le bootstrap apparié par session.

---

## Volet III : Sol/Astra

**F9. La JSD a des poids incohérents.**
$M$ est pondéré par $N_P/(N_P+N_Q)$ (via `cP+cQ`), mais on soustrait $\tfrac12(H(P)+H(Q))$. La JSD généralisée exige $H(M_\pi)-\pi_P H(P)-\pi_Q H(Q)$.
- Contre-exemple : $P=(1,0)$ avec $N_P=1000$, $Q=(\tfrac12,\tfrac12)$ avec $N_Q=10$.
- On obtient $H(M)\approx 0{,}044$ bit et un résultat ≈ $-0{,}46$, tronqué à 0, alors que $P\ne Q$.
- Le cas `cRef` (grand) contre fenêtre (petite) est exactement celui de `jsd_threshold_null`. Le moniteur devient aveugle.

**F10. Merkle : duplication de la dernière feuille sans domain separation (CVE-2012-2459).**
- Les journaux $[a,b,c]$ et $[a,b,c,c]$ ont la même racine. Une mutation du log est donc indétectable et la non-répudiation est rompue.
- La taille de l'arbre n'est pas engagée, et aucun préfixe ne distingue feuilles et nœuds.
- Le RFC 6962 cité en antériorité (préfixes 0x00/0x01, pas de duplication) n'est pas suivi.

**F11. La rétraction « identité exacte dans le cône sûr » est contradictoire.**
- $T$ est défini sur une **boule** $B(c,a)$. Une rétraction radiale préserve la direction et n'a aucune notion de cône.
- Un cône est radialement non borné, alors que $T$ est bornée par $R$ : elle ne peut pas être l'identité sur un cône.

**Vérifié sain, non signalé :** la formule Miller-Madow $(m-1)/(2N)$ et la conversion en bits.

---

## Volet IV : H9

**F12. Le pré-blanchiment est estimé in-sample sur la série surveillée.**
$\hat\phi$, la moyenne et l'écart-type sont estimés sur la série même, y compris après une rupture éventuelle.
- Un saut de moyenne pousse $\hat\phi\to 1$. Les innovations deviennent quasi différenciées, et le saut persistant se réduit à un pic unique : le CUSUM perd sa puissance.
- La calibration de $h$ sous un N(0,1) i.i.d. ignore l'erreur d'estimation, ce qui gonfle les fausses alarmes.
- Correctif : séparer phase I et phase II, et calibrer par bootstrap.

**F13. La variance de Jonckheere-Terpstra avec ex æquo est incomplète.**
Le code ne garde que le premier terme. Il manque les deux termes positifs :
$$+\frac{[\sum n(n-1)(n-2)][\sum t(t-1)(t-2)]}{36N(N-1)(N-2)}+\frac{[\sum n(n-1)][\sum t(t-1)]}{8N(N-1)}.$$
La variance est donc sous-estimée et le test anti-conservateur, alors qu'une « correction d'ex æquo » est revendiquée.

**F14. JT est appliqué à des mesures répétées dépendantes.**
Une même chaîne fournit des observations aux profondeurs $d=1..6$, qui sont autocorrélées. JT suppose des échantillons indépendants.
- L'antériorité directe ici est le test de Page (alternative ordonnée en blocs), ou une permutation par chaîne entière.

**F15. Le seuil mis à jour par PID sur un flux non étiqueté s'auto-aveugle.**
Avec $e_t=\mathbb 1[s_t>q_t]-\alpha$, le régulateur force la fréquence d'alarme à long terme vers $\alpha$ **quelle que soit la distribution**. Sous une attaque persistante, $q_t$ monte et les alarmes retombent à $\alpha$.
- Les garanties ACI et conformal-PID (Gibbs & Candès ; Angelopoulos et al.) exigent le score de la vraie étiquette. Ce n'est pas une alarme brute.
- Ce mécanisme contredit aussi la calibration ARL$_0$ et le gel hors ligne du §2.2.

---

## Volet V : H4'

**F16. Le leave-one-pair-out inclut les paires sœurs de la même famille.**
Il y a une fuite intra-famille : les erreurs sont corrélées au sein d'une famille, ce qui biaise l'estimation de façon optimiste et fausse les poids Mantel-Haenszel.
- Correctif : leave-one-**family**-out, c'est-à-dire un cross-fitting par cluster.

**Vérifié sain, non signalé :**
- le stratifieur calculé sur un panel externe gelé, exclu des familles évaluées (pas de circularité) ;
- l'antériorité PBFT $N\ge 3f+1$ ;
- l'antériorité HMP.
