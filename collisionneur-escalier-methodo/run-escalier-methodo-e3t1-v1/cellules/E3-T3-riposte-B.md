# Proposition B — Tour III.3 : riposte

**Pièces.**
- Le bloc FAITS est vide par décision de l'arbitre. Il n'est pas coupé et je n'en invente aucun contenu.
- Les pièces E3-T1-conception-B, E3-T2-redteam-A et E3-T2-redteam-C sont complètes : chacune se termine par sa ligne de fin.
- Je ne réponds qu'aux sections « Contre la proposition B ».

**Statuts.** Ils sont inchangés par rapport au tour III.1 :
- les calculs sont des raisonnements que chacun peut refaire, pas des faits ;
- tout paramètre qui ne vient pas de l'énoncé est « illustratif » ;
- mes suppositions portent le statut HYPOTHÈSE.

---

## (a) Verdict attaque par attaque

### Équipe rouge A — failles

**A-1 (le « cas le plus favorable » du régime P) — acceptée.**
- Dans mon propre modèle, le terme items vaut $\sigma_I^2/n$, qui est nul pour un effet diffus.
- La borne $\Delta(1-\Delta)$ n'est le minimum de $\pi_d-\Delta^2$ que pour des items déterministes, avec $d_i\in\{-1,0,1\}$ et $\pi_d\ge\Delta$.
- Correction : la phrase « la famille 2 seule ne détecte aucun δ ≤ 0,15 à 80 %, quel que soit $r$ » devient **conditionnelle à l'issue H_A d'E2** ($\hat q$ faible).
- Si $\hat q$ est élevé, les graines aident aussi en régime P, et la puissance dépend de la forme de l'effet, qui est inconnue.

**A-2 (triple usage des deux répliques gratuites) — acceptée, transformée.**
- Les répliques gratuites gardent deux rôles :
  1. l'estimation ;
  2. le bras de base. Estimer une variance sur les données mêmes qu'on teste est l'usage ordinaire d'un test apparié.
- Elles perdent le rôle de cas A/A d'évaluation.
- Les paramètres des instruments sont scellés sur une moitié tirée au sort des répliques d'E1′. Le banc A/A est évalué sur l'autre moitié.
- Les cas A/B « diffus » sont désormais construits à partir des répliques du **cran cher** (E1-bis), et non de la base. Le banc cesse ainsi de rendre a5 vraie par construction.

**A-3 (puissance de 0,5 à Δ = δ) — acceptée. La faute est dans la règle, pas dans les tableaux.**
- Les tableaux du §1 ont été calculés pour $\mathrm{SE}\le\delta/2{,}487$. Cela correspond au test « borne basse unilatérale à 95 % > 0 » avec une puissance de 0,80 à Δ = δ.
- La condition supplémentaire $\widehat\Delta\ge\delta$ ramenait cette puissance à environ 0,5. C'est exactement ce que je reprochais à « l'autre analyse » du programme.
- Je la retire (règle corrigée en (b)).
- Le seuil implicite devient $\widehat\Delta\ge1{,}645\cdot\mathrm{SE}\approx0{,}66\,\delta$ quand la SE est à sa valeur cible.

**A-4 (variance de la base transférée aux crans chers) — acceptée, transformée en test E1-bis.**

**A-5 (dérive et graine confondues) — acceptée.** Trois mesures :
- les répliques d'E1′ sont entrelacées dans une même fenêtre de temps, dans un ordre tiré au sort ;
- dans l'escalier, chaque paire de bras s'exécute dans le même bloc temporel ;
- le contrôle de dérive rejoue **les mêmes graines** à deux dates, plus un rejeu à la même date qui donne le plancher de non-déterminisme.

**A-6 (le contrôle négatif d'E2 teste un autre objet) — acceptée.**
- Le modèle local ne sert plus qu'à vérifier la chaîne de calcul.
- Sur le système réel, deux contrôles le remplacent :
  - un contrôle négatif : rejeu identique (même graine, même entrée) ;
  - un contrôle positif : température augmentée, et $\hat q$ doit monter.

**A-7 (E6 est circulaire) — acceptée.**
- E6 ne réfute que la cohérence du simulateur. Ce n'est pas une expérience au sens de B4.
- Elle est retirée des duels et devient un calcul de dimensionnement.
- « L'escalier est compétitif » reste une HYPOTHÈSE non testée.

**A-8 ($2^{4-1}$ sans repli) — rejetée sur le point technique, acceptée sur la conséquence.**
- *Rejet.* Avec le générateur D = ABC (I = ABCD), en résolution IV :
  - les effets principaux sont aliasés avec des interactions d'ordre 3, pas d'ordre 2 ;
  - l'interaction sous-modèles × longueur est aliasée avec l'interaction d'ordre 2 complémentaire, et non avec l'effet « itérations ».
- *Acceptation.* Les interactions d'ordre 2 ne sont pas séparables.
- *Remède.* Le seul repli utile est la demi-fraction complémentaire I = −ABCD, soit 8 exécutions qui complètent un $2^4$.
  - Un repli par inversion de tous les signes régénère la même fraction : le mot ABCD est de longueur paire.

### Équipe rouge A — scénarios d'évasion

| Manœuvre | Verdict | Parade ou limite |
|---|---|---|
| Mémorisation des 60 items | Acceptée | Aucun instrument statistique sur ces 60 items ne la voit. Seules parades : E5 (items neufs) et des canaris, à condition que le canal de fuite soit sous contrôle (HYPOTHÈSE). **Menace non neutralisée, consignée.** |
| Une régression volontaire (7 contre 1, $P(X\ge7\mid8)=9/256\approx0{,}035$, calcul refait) | Acceptée | L'audit « trop propre » détecte des anomalies naïves, pas un adversaire qui connaît la règle. Il est maintenu, mais ne vaut pas garantie. |
| Cache pendant les répliques gratuites | Acceptée | $r\ge2$ par bras à chaque cran, quelle que soit la valeur de $\hat q$. $\hat q$ est mesuré par bras. Les jetons facturés par réplique sont relevés par un compteur indépendant. |
| Remplissage $s(b)\approx b$ | Transformée | L'analyse en intention de traiter sur $b$ n'est pas trompée : un dollar vide donne Δ ≈ 0, donc un plateau ou une zone grise, donc on reste. Ce qui est trompé : la variable instrumentale et E3. E3 est remplacée par un placebo de budget (E3′). |
| Variance gonflée pour bloquer le plateau | Rejetée | Avec ma règle, zone grise = rester, et la séquence fixe s'arrête au premier non-rejet. L'escalier **ne continue pas**. Une asymétrie de $\hat q$ entre bras déclenche l'audit. |
| Invalider 2 ou 3 sorties du bras cher | Acceptée | Le taux de validité par bras et par cran est publié avant la BA. Un McNemar sur la validité, avec seuil scellé, détecte l'asymétrie. La BA restreinte aux items valides dans les deux bras n'est qu'un diagnostic : le biais de collision que C reproche à A s'applique aussi à ma voie V2. |
| Sous-déclaration de $s$ | Acceptée | Compteur de coût indépendant (facturation, jetons comptés côté client). Un écart au-delà d'un seuil scellé déclenche l'audit. |
| Combinaison des manœuvres | Acceptée | Le régime C est retiré comme voie de décision (voir C-6). La contamination reste le résidu non couvert. |

Contrôles négatifs proposés par A :
- n° 2, 3, 4, 5 et 7 : acceptés ;
- n° 6 : accepté, sous la forme corrigée (demi-fraction complémentaire) ;
- n° 1 (canaris) : accepté sous condition, faisable seulement si l'on contrôle les documents par lesquels la fuite passerait.

### Équipe rouge C — failles

**C-1 (E1 ne peut pas réfuter H_B ; E4 trop peu puissante) — acceptée sur le fond, chiffres corrigés.**
- *E1.* Sous H_A, $\hat R\sim\chi^2_5/5$ si le dénominateur est connu. Réfuter H_B exige $\hat R<2\cdot\chi^2_{5;0,05}/5=0{,}458$, soit $P(\chi^2_5<2{,}29)$.
  - Cette probabilité se situe entre les quantiles 0,10 (1,610) et 0,25 (2,675) de $\chi^2_5$ : elle est de l'ordre de 0,2, et non « inférieure à 15 % ».
  - La conclusion de C tient malgré cet écart : E1 ne peut pas réfuter H_B.
- *E4.* Si les deux versions sont exécutées indépendamment, $\mathrm{SE}_{\text{int}}=\sqrt2\,\mathrm{SE}_\Delta$, et non $2\,\mathrm{SE}$.
  - Avec $\mathrm{SE}_\Delta\approx0{,}06$ (illustratif), on obtient $\mathrm{SE}_{\text{int}}\approx0{,}085$.
  - Réfuter H_B à δ = 0,10 reste donc presque impossible. Les deux points sont corrigés en E1′ et E4′.

**C-2 (E3 conditionne sur une variable post-traitement) — acceptée.** C'est une contradiction : je déclarais l'estimateur biaisé, puis j'en faisais une issue réfutante. E3 est remplacée par E3′, une comparaison randomisée.

**C-3 ($\hat q/2$ absorbe $\sigma_\gamma^2$) — acceptée sur le principe, transformée.**
- Dans le modèle linéaire, $\mathbb E[(Y_{ik}-Y_{ik'})^2]=2\bar v+2\sigma_\gamma^2$, donc $\hat q/2$ estime $\bar v+\sigma_\gamma^2$.
- Le biais relatif vaut $\sigma_\gamma^2/\bar v$, soit 0,8 % avec les valeurs illustratives 0,02 et 0,05.
- « Biaisé vers 1 par construction » surestime donc l'effet pour un petit $\sigma_\gamma$. Dans l'exemple de C (« positif partout »), le modèle linéaire est faux, mais le décalage moyen se voit.
- Correction : une analyse de variance à deux facteurs, items × répliques.
  - $\mathbb E[\mathrm{MS}_{\text{rép}}]=\bar v+n\sigma_\gamma^2$ et $\mathbb E[\mathrm{MS}_{\text{rés}}]=\bar v$ : la contamination disparaît.
  - Diagnostic préalable : un McNemar entre répliques A/A (contrôle n° 2 de C, emprunté).

**C-4 (OFAT contre factoriel) — acceptée, deux corrections.**
1. L'allocation optimale de l'OFAT est $n_0=6$, $n_1=3$, soit 18 exécutions pour $\sigma^2(1/6+1/3)=\sigma^2/2$. Le rapport avec le factoriel est 18/8 = 2,25, et non 2,5.
2. Le gain ne porte que sur le bruit d'exécution. Le terme items $\mathrm{Var}_i(d_i)/n$ est identique dans les deux plans.
   - En régime P avec des items quasi déterministes, le factoriel ne gagne donc rien sur le terme dominant, et il paie les coins chers.
   - Cela fait pencher vers l'escalier dans ce cas.

**C-5 (E4 contamine l'ordre de la séquence fixe) — acceptée.**
- E4′ s'exécute après le scellement des décisions de l'escalier.
- Son résultat ne modifie pas l'ordre en cours. Il n'informe que le plan de la version suivante, avec un α propre.

**C-6 (le régime C est une tautologie) — acceptée. La voie 2 est retirée comme voie de décision.**
- Argument supplémentaire, contre moi-même : avec la règle corrigée (A-3), $\hat q=0$ et $\sigma_\gamma=0$, un seul item basculé deviendrait « significatif ».
- Le hasard que C invoque est celui de l'échantillonnage des items, c'est-à-dire le terme du régime P.
- Le régime C ne sert plus qu'à décomposer le bruit des graines pour choisir $r$.

### Équipe rouge C — scénarios d'évasion

| Manœuvre | Verdict | Parade |
|---|---|---|
| Saboter la base pour franchir le premier cran | Acceptée | La configuration de base est hachée et scellée avant tout essai. Elle doit être celle des répliques gratuites. HYPOTHÈSE : l'énoncé ne dit pas quelle configuration elles répliquent, l'arbitre doit le préciser. La BA de la base dans l'escalier doit tomber dans la bande A/A d'E1′, sinon audit. |
| Hachage du numéro de cran sur un système déterministe | Neutralisée en partie | Elle visait le régime C, qui est retiré. En régime P, sans connaissance des étiquettes, le décalage a une moyenne proche de 0 : $\sigma_I^2$ gonfle, on tombe en zone grise et on reste. J'emprunte le contrôle n° 3 de C : un **pseudo-cran** (changement cosmétique, sans capacité ajoutée) mesure le plancher de sensibilité à l'invite. Un vrai cran doit le dépasser. |
| Diluer l'audit (9 contre 2 ; $P(X\ge9\mid11)=67/2048\approx0{,}033$) | Acceptée | Même limite que chez A. L'audit n'est pas une défense contre un adversaire informé. |
| Évasion totale | Rejetée en l'état | Elle repose sur le régime C (retiré) et sur E3 (remplacée). Le résidu est la contamination, déjà consignée. |

Contrôles négatifs proposés par C : les trois sont acceptés.
- n° 1 : caractéristiques opératoires d'E1′, calculées ci-dessous ;
- n° 2 : McNemar A/A ;
- n° 3 : pseudo-cran.

---

## (b) Expériences corrigées

### P0 — Instrumentation préalable (pas un duel)
- Compteur de coût indépendant du système.
- Configuration de base hachée.
- Taux de validité par bras.
- Exécutions entrelacées par blocs temporels.
- Plafond de dépense réglable indépendamment du budget affiché (HYPOTHÈSE, nécessaire pour E3′).

### E1′ — Décomposition de la variance
- **H_A** : $\sigma_\gamma\le0{,}01$.
- **H_B** : $\sigma_\gamma\ge0{,}04$.
- Les deux seuils sont illustratifs et à sceller.

**Protocole.**
- 12 répliques de la base : les 2 gratuites et 10 payées, entrelacées et tirées au sort.
- Analyse de variance items (60) × répliques. Statistique : $F=\mathrm{MS}_{\text{rép}}/\mathrm{MS}_{\text{rés}}$, avec 11 et 649 ddl.

**Paramètre de non-centralité**, avec $\bar v=0{,}05$ (illustratif), $n=60$ et $\varphi=1+n\sigma_\gamma^2/\bar v$ :
- sous H_A, $\varphi\le1{,}12$ ;
- sous H_B, $\varphi\ge2{,}92$.

**Caractéristiques opératoires.** J'approxime le dénominateur comme connu, puisqu'il a 649 ddl. Je prends $\chi^2_{11}$ : 0,05 → 4,575 ; 0,25 → 7,584 ; 0,75 → 13,70 ; 0,95 → 19,68.
- *Réfuter H_A* : on rejette si $F>1{,}12\times19{,}68/11=2{,}00$. Sous H_B, $P(\chi^2_{11}>2{,}00\times11/2{,}92=7{,}54)\approx0{,}75$.
- *Réfuter H_B* : la borne haute unilatérale à 95 % de φ doit être inférieure à 2,92, ce qui revient à $F<2{,}92\times4{,}575/11=1{,}21$.
  - Sous $\varphi=1{,}12$, la probabilité vaut environ 0,6.
  - Sous $\varphi=1$, elle vaut environ 0,73.
- Entre les deux, la zone grise est déclarée. Ces valeurs sont illustratives et reposent sur le modèle linéaire.

**Contrôles.**
- Négatif : rejeu à même graine et même entrée, le même jour. On attend $\hat q_{\text{rejeu}}=0$ ; sinon a4 est réfutée.
- McNemar entre répliques A/A.
- Les paramètres des instruments sont scellés sur 6 répliques tirées au sort. Le banc A/A utilise les 6 autres.

**Falsification.**
- $F>2{,}00$ réfute H_A.
- $F<1{,}21$ réfute H_B.

### E1-bis — La variance dépend-elle de la configuration (a5) ?
- **Protocole.** 6 répliques du cran le plus cher, dans la même fenêtre que E1′.
- **H_A** : $\bar v_{\text{cher}}/\bar v_{\text{base}}\in[0{,}67 ;1{,}5]$.
- **H_B** : ce rapport est en dehors de cet intervalle.
- Les bornes sont illustratives.
- **Puissance.** $\mathrm{MS}_{\text{rés}}$ a 5 × 59 = 295 ddl par configuration : ce rapport est bien estimé.
- **Limite dite.** $\sigma_\gamma$ par configuration n'est **pas** testable avec 6 répliques.
- **Usage.** Ces répliques fournissent aussi les cas A/B diffus du banc.

### E2′ — Déterminisme, mesuré par bras
- **Protocole.** $\hat q$ est calculé par bras sur les répliques d'E1′ et d'E1-bis.
- **H_A** : $\hat q\le0{,}05$.
- **H_B** : $\hat q\ge0{,}15$.
- Les deux seuils sont illustratifs.
- **Contrôles sur le système réel.**
  - Négatif : le rejeu identique.
  - Positif : température augmentée. Si $\hat q$ ne monte pas, l'instrument est aveugle.
- **Falsification.** Inchangée par rapport au tour III.1.

### E3′ — Placebo de budget (emprunté à l'attaque de A contre C)
- **Protocole.** Deux bras avec le même plafond réel $c$ et des budgets affichés différents, $b_{\text{bas}}$ et $b_{\text{haut}}$.
- **H_A** : $b$ n'agit que par la capacité de dépense, donc ΔBA = 0.
- **H_B** : $b$ change la stratégie, $|\Delta\mathrm{BA}|\ge\delta$.
- **Falsification.**
  - Un IC à 90 % bilatéral inclus dans $]-\delta ;\delta[$ réfute H_B.
  - Une borne basse supérieure à 0, ou une borne haute inférieure à 0, réfute H_A.
- **Puissance.** C'est une comparaison appariée ordinaire. D'après le §1, elle n'est réaliste que pour δ ≥ 0,15 sur l'indice poolé.
- **Contrôle négatif.** Le même $b$ affiché deux fois.
- **Si le plafond n'est pas réglable.** E3′ est infaisable et la variable instrumentale est abandonnée par défaut, au profit de l'analyse en intention de traiter seule. C'est consigné, et ce n'est pas une réfutation.

### E4′ — Transposabilité d'une version à la suivante
- **Calendrier.** E4′ s'exécute après le scellement de l'escalier.
- **Protocole.** Mêmes graines rejouées. Contrôle de dérive : même version, mêmes graines, deux dates.
- **H_A** : les signes des effets par axe sont conservés et l'interaction est inférieure à 0,20 en valeur absolue.
- **H_B** : l'interaction est supérieure ou égale à 0,20 en valeur absolue (illustratif).
- **Justification du seuil.** $\mathrm{SE}_{\text{int}}\approx0{,}085$ (illustratif). Une interaction de 0,10 est indétectable, et je le dis.
- **Falsification.** Une borne haute inférieure à 0,20 réfute H_B. Une borne basse supérieure à la dérive mesurée réfute H_A.

### E5 — Malédiction du gagnant
- Inchangée : elle reste la **seule** parade statistique contre la contamination.
- Elle exige un jeu d'items neufs, qui n'est pas dans les faits.
- On y ajoute des canaris, sous la condition dite plus haut.

### E6 — Retirée
Elle devient un calcul de dimensionnement, sans valeur réfutante.

### Règle gelée corrigée (une voie parmi d'autres)

**Conditions préalables.**
- P0 est en place.
- $r\ge2$ par bras, et $r$ est fixé à partir d'E1′.
- Le critère porte sur l'indice poolé, en régime P.
- Le test est un rééchantillonnage stratifié par classe ou un test de signe pondéré.

**Monter.** Trois conditions à la fois :
- la borne basse unilatérale à 95 % est supérieure à 0 ;
- la borne basse en famille 2 est supérieure à −δ (garde-fou, illustratif) ;
- le coût par point est inférieur ou égal à $V$, valeur fixée par l'arbitre (a12).

**Plateau.** La borne haute de l'IC à 90 % est inférieure à δ.

**Zone grise.** On reste, puisque la moins chère l'emporte.
- Un seul lot supplémentaire est permis, seulement si E1′ conclut H_B, c'est-à-dire si le bruit des graines domine.
- Ce lot est compté comme une analyse intermédiaire dans la fonction de dépense d'erreur.

**Multiplicité.** L'ordre est scellé et l'on s'arrête au premier non-rejet. Le pseudo-cran sert de plancher.

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi
Tout ce qui suit est établi **par calcul, sous des hypothèses dites**, et non observé.

- **Granularité.** Un item pèse 1/24 en famille 2, et 1/36 en famille 1 sous a2 (HYPOTHÈSE 18/18).
- **Famille 2 seule.** Si les items sont quasi déterministes, elle ne détecte aucun δ ≤ 0,15 avec une puissance de 80 %. McNemar exact exige au moins 5 basculements nets, soit Δ ≥ 0,21.
- **Indice poolé, cas favorable** (items déterministes, aucune dégradation) :
  - δ = 0,15 : puissance d'environ 0,94 ;
  - δ = 0,10 : puissance d'environ 0,80, limite et optimiste ;
  - δ = 0,05 : puissance d'environ 0,54.
- **δ = 0,05 n'est pas un objectif atteignable sur 60 items.**
- **Les deux répliques gratuites** estiment le bruit item × graine. Elles ne bornent pas l'effet d'exécution partagé : un seul degré de liberté.
- **Seuil sur l'estimation ponctuelle.** Une règle « $\widehat\Delta\ge\delta$ » a une puissance de 0,5 à Δ = δ. C'est vrai de ma règle du tour III.1, maintenant corrigée, et de l'exigence Δ ≥ +0,10 de l'autre analyse, si elle porte sur l'estimation ponctuelle.
- **Plateau.** L'absence de différence n'en est pas un ; il faut un test d'équivalence.
- **Séquence fixe.** Elle contrôle le taux d'erreur familial seulement si l'ordre est scellé et si chaque lot de zone grise est compté.
- **Dépense et causalité.** Conditionner sur $s$ ou sur la validité est un biais de collision. Seules les comparaisons randomisées sur $b$ sont causales.
- **Usage des 60 items.** Ils peuvent servir à **sélectionner**, pas à **confirmer**.
- **Factoriel ou escalier.** Le $2^{4-1}$ n'a d'avantage, d'environ 2,25 fois, que sur le bruit d'exécution, pas sur le terme items.

### Ce qui n'est pas établi
- **Les paramètres de variance** : $\sigma_\gamma$, $\bar v$ par configuration (a5), le déterminisme à graine fixée (a4), la stabilité du fournisseur (a10).
- **L'équilibre de la famille 1** (a2).
- **L'absence de fuite des 60 items** (a8, non audité). Aucun instrument statistique sur ces items ne peut l'établir.
- **L'unité de coût** (a6) et **la valeur d'un point de BA** (a12).
- **La restriction d'exclusion** ($b$ n'agit que par $s$).
- **La transposabilité d'une version à la suivante.**
- **La compétitivité de l'escalier** face aux méthodes multi-fidélité (HYPOTHÈSE).
- **La cible de l'inférence.** C'est la population d'items selon ma lecture (a3). Le régime C est retiré comme voie de décision.

### Les voies qui restent et ce qui les départage
1. **δ = 0,15 sur l'indice poolé**, avec garde-fou en famille 2. Robuste, mais aveugle aux gains de 0,05 à 0,10.
2. **δ = 0,10 sur l'indice poolé**, si E1′ et E2′ montrent un bruit dominé par les items et si l'arbitre accepte une puissance limite.
3. **Ajouter des items avant toute décision fine.** C'est aussi la seule voie qui permet E5.

Ce qui les départage : E1′ et E2′, puis les décisions de l'arbitre sur a3 et a12.

### L'expérience à faire en premier : P0 suivi d'E1′, avec E1-bis et E2′ dans la même fenêtre

**Coût, à 20 USD par exécution de base et 22 USD par exécution chère** (illustratif, unité a6 non établie) :
- 10 répliques de la base : 200 USD ;
- 6 répliques du cran cher : 132 USD ;
- 2 rejeux : 40 USD ;
- total : environ 370 USD.

**Pourquoi elle d'abord :**
- elle fixe $r$ et dit si le goulot est les graines ou les items ;
- elle teste a4, a5 et, en partie, a10 ;
- elle réutilise les répliques gratuites ;
- elle **ne compare aucune configuration** : elle ne dépense ni α ni crédit de réutilisation des 60 items.

**Ses deux issues réfutent chacune quelque chose :**
- $F>2{,}00$ réfute « le bruit des graines est négligeable » ;
- $F<1{,}21$ réfute « un effet d'exécution partagé domine ».

Ces seuils sont illustratifs et à sceller avant lecture.

FIN-DE-CELLULE