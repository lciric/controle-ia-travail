# Contre-lecture de fidélité des deux portées v3 des dix corrections de l'audit sur l'évasion sous filtrage pendant l'entraînement après pré-entraînement (billet de Yair Halberstadt) — v1

- **Contre-lecteur** : sous-agent neuf (Opus 5.5). Je n'ai écrit ni l'audit, ni la v2, ni aucune des deux v3. Aucun fichier du dépôt n'a été modifié ; aucun commit, aucun accès réseau, aucune dépense.
- **Branche** : `papier-d/evasion-post-entrainement-v1`, tête `93ad7db9`. Audit lu sur `origin/audit/evasion-post-entrainement-v1` (`d6c13162`, empreinte du rapport `5e70f802…`).
- **Cloisonnement, à savoir** : la variante B a été écrite par la session `session_01Qi7Gr5…`, qui est aussi la session qui m'a confié cette contre-lecture. Je l'ai jugée avec la même exigence que l'autre portée (règle de symétrie R4).
- **Abréviations du rapport** : « portée de référence » = v3 du commit `b1006d58` à la racine du paquet ; « variante B » = dossier `variante-b-v3-session-fille-2/`. P = `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1`.

---

## 0. Verdict

- **Portée de référence (`b1006d58`) : fidèle avec réserves.** Les dix corrections sont portées sur le fond dans les quatre pièces publiques. Il reste deux défauts majeurs :
  - le billet garde l'affirmation de nécessité « requires (H1)…(H2)…(H3) », que contredit la phrase suivante ;
  - `test_mort_halberstadt_v2.py` réécrit son JSON scellé quand on le lance depuis son dossier, ce qui est le défaut que la correction 10 visait.

  S'y ajoutent sept défauts mineurs.
- **Variante B : fidèle avec réserves.** La portée est plus complète et plus exacte, et la table de correspondance dit vrai sur les vingt cases sondées. Il reste un défaut majeur : en voulant retirer la nécessité, la variante a transformé H1 à H3 en condition **suffisante** (« arises in particular when »). Cette affirmation est fausse sous l'opérateur de pénalité, et je donne un contre-exemple au § 3. S'y ajoutent quatre défauts mineurs, dont deux petites erreurs de chiffres ou de bord introduites par la correction.
- **Recommandation** : partir de la **variante B** et y reporter cinq passages de la portée de référence (§ 4).

Les tables numériques n'ont pas changé entre la v2 et l'une ou l'autre v3, ni dans les manuscrits ni dans les billets. Je l'ai vérifié par programme : 112 valeurs dans les tables du manuscrit, mêmes empreintes, et sorties JSON `verified_examples` identiques à la v2. Les deux scripts v3 reproduisent leur JSON scellé octet pour octet. Tous les nombres nouveaux recalculés à la main concordent, à une exception près, dans la variante B (défaut B-3).

---

## 1. Tableau des dix corrections par portée

Légende : **F** = portée fidèlement ; **P** = portée partiellement ; **N** = non portée ; **D** = portée mais déformée. Les numéros de ligne renvoient aux fichiers v3 de chaque portée.

| N° | Correction (§ 6 de l'audit) | Portée de référence (`b1006d58`) | Variante B |
|---|---|---|---|
| 1 | Découplage : sous A, variation égale à la covariance divisée par la moyenne, non-hausse si et seulement si la covariance est négative ou nulle, le placement hors boucle ne suffit pas ; sous B, covariance négative ou nulle nécessaire mais non suffisante, indépendance ou association négative suffisante | **F**. Billet l. 19, 96-98 et 110 ; commentaire l. 15 ; manuscrit, résumé l. 39, contribution 3 l. 52, énoncé R2 l. 212-217, remarque l. 248 (i)-(iii) ; README l. 19. Réserve : contribution 1 du manuscrit (l. 50) garde « an off-loop deployment monitor » (mineur R-6). | **F**. Billet l. 20, 98-100 et 114 ; commentaire l. 15 ; manuscrit, résumé, contribution 3, R2 l. 232-237, remarque « Placement is not covariance » l. 264 ; README l. 17. Les trois contre-exemples sont chiffrés dans le billet. |
| 2 | Le « dilemme » : dans la niche, B dépasse A en furtif exactement quand B dépasse A en honnêteté ; il faut dire les deux moitiés | **F dans les énoncés, P dans les légendes.** Billet l. 18, 60, 80 et 84 ; commentaire l. 11 ; manuscrit, théorème 1, point 4(c), l. 140 ; README l. 15. Mais le texte et la légende de la table 3 (l. 301 et 305) ne disent que la moitié « B amplifie plus le furtif », et « Rejection–Penalty Dilemma » reste en titre (billet l. 46 ; manuscrit l. 51, 96 et 125) (mineur R-4). | **F**. Billet l. 19, 62, 82 et 86 ; commentaire l. 11 ; manuscrit, point 4(c) l. 148, preuve l. 186, remarque l. 189-190, texte et légende de la table 3 l. 326 et 330 ; README l. 13. « Dilemma » est remplacé par « contrast ». Petite erreur de chiffre (défaut B-3). |
| 3 | « Collapses to stealth » remplacé : l'honnêteté s'effondre, la masse va aux tricheurs, et la part furtive tend vers $\beta_f p_f/(\beta_v p_v+\beta_f p_f)$ | **F**. Billet l. 17 ; commentaire l. 10 ; manuscrit, résumé, point 4(a) l. 133 (exact, « for every η », « can be small »), remarque (iv) avec 3/128 ; README l. 14. | **F avec une erreur de bord.** Billet l. 17 et 58 (3/128) ; commentaire l. 10 ; manuscrit l. 137 et 200 ; README l. 11. Mais le manuscrit écrit « $< 1$ » (l. 137) et « strictly below one » (l. 200), ce qui est faux quand $\beta_v = 0$, cas admis par le domaine (défaut B-2). |
| 4 | Opérateur A déclaré comme choix de modèle, équivalent à une prime de $\eta^{-1}\log\beta$, et rejet répété dont la barrière ne s'efface pas | **F**. Billet l. 17 et 42 ; commentaire l. 5 et 18 ; manuscrit, résumé, l. 89 ; README l. 9. Ajout exact : A coïncide avec un entraînement sans moniteur suivi d'un rejet unique à l'inférence (correct, car $\pi_A \propto \beta\,\pi_{no}$). | **F**. Billet l. 18, 43 (+195,3 et −92,1) et 112 ; commentaire l. 5 et 10 ; manuscrit, remarque `rem:modelA` l. 96-97, remarque sur $\eta=0$ l. 87, titre du point 4 l. 129, limitations l. 349 ; README l. 12. |
| 5 | Retirer « every theorem … verified in exact rational arithmetic » et ne plus faire de « 0 contre-exemple sur 14 000 » un argument | **F dans le billet, le commentaire et le README ; P dans le manuscrit.** Billet l. 21 ; README l. 30 ; manuscrit l. 53 et 253. Mais le manuscrit garde, l. 257, « Tables … confirm these thresholds to full precision » (mineur R-5). Le JSON garde `total_instances: 14000, total_violations: 0`, avec une note de réserve (acceptable). | **F**. Billet l. 22 et 119 ; commentaire l. 18 ; manuscrit, résumé, contribution 4, section « What the Companion Script Checks » l. 271-278, « illustrate » l. 282 ; README l. 29-32. Les familles du JSON sont décrites avec leurs limites (« SPECIAL CASE ONLY », « TAUTOLOGICAL »). |
| 6 | Retirer la nécessité et l'exhaustivité du théorème 2 pris dans son ensemble (« requires breaking one of two… », « les trois seuls régimes », « exhaustive », « necessary and sufficient ») | **P**. Manuscrit F : le paragraphe H1 à H3 est retiré et l'ouverture de la section 3 (l. 197) dit « we do not prove that avoiding deployment-effective evasion requires any one of them ». Commentaire et README F. **Mais le billet (l. 90) garde « producing a deployed policy that … requires: (H1) … (H2) … (H3) »** avant de dire qu'il ne revendique pas cette nécessité (défaut R-1, majeur). | **D**. La nécessité est bien retirée partout (« We do not claim… nor that breaking one of the inequalities is necessary », manuscrit l. 217). Mais elle est remplacée par une suffisance non démontrée et fausse sous B : « arises in particular when the following three conditions hold » (manuscrit l. 211-216 ; billet l. 92) (défaut B-1, majeur). |
| 7 | « Universal » restreint à A ; enrichissement sous B seulement à récompense égale ; corriger la ligne 9 du commentaire v2 | **F**. Billet l. 50-52 ; commentaire l. 9 (corrigé) ; manuscrit, titre du point 1 l. 101, remarque (v) ; README l. 13. « Universal » ne figure plus nulle part. | **F**. Billet l. 51-53 (0,8810 → 0,8748) ; commentaire l. 9 ; manuscrit l. 105 et 110, remarque l. 193-194 ; README l. 10. |
| 8 | Citer Price, Robertson et Fisher pour les identités, Korbak et al. 2022 pour la forme de Gibbs (après vérification sur PDF), et présenter « sondes hors boucle » comme déjà publiée | **F**. Billet l. 52 et 115 ; commentaire l. 9 et 20 ; manuscrit l. 44, 48 et 51, bibliographie ; README l. 40. Les quatre sont cités dans chaque pièce publique. | **F, avec un manque.** Billet l. 17, 35, 53 et 117 ; manuscrit l. 48, 51, 94 et 264, plus Bailey et al. 2024 ; README l. 42. **Le commentaire ne cite pas Korbak et al. 2022** (mineur B-4). |
| 9 | Petits bords : $p_f = 0$ hors du domaine ; rapport des seuils non défini si $p_h\beta_h = p_f\beta_f$ ; $\pi_0(\mathcal S) > 0$ requis ; lien pièges–ratio critique seulement pour $\beta_h = 1$ | **P**. Billet l. 90, 96 et 113 ; manuscrit l. 186, 197 et 212. Mais l'énoncé de R1 dans le manuscrit (l. 210) garde « if $\Pi_f$ is unreachable ($p_f = 0 \iff \Delta D_{KL} = +\infty$) … then … » comme un cas du théorème, en contradiction avec la l. 197 (mineur R-3). | **F**. Billet l. 96, 98 et 104 ; manuscrit l. 200 (avec le cas négatif, que j'ai vérifié : 0 désaccord sur 100 000 tirages), l. 230, 232 et 268. |
| 10 | Hygiène : le script ne doit plus écrire à côté de son JSON scellé ; corriger `c_seuil` ; nettoyer le compagnon `.sha256` de Carbon ; retirer « closed-form » pour le seuil sous B | **P**. Le script de vérification refuse son propre dossier mais **réécrit en silence** un JSON déjà présent dans le dossier de sortie (mineur R-7). `c_seuil` est corrigé. **`test_mort_halberstadt_v2.py` écrit par défaut dans le dossier courant, donc à côté de lui-même s'il est lancé en place, et y réécrirait `resultats-test-mort-halberstadt-v2.json` scellé.** Je l'ai constaté sur une copie (défaut R-2, majeur). Compagnon de Carbon : nouveau `…md.v2.sha256` propre (F). « Closed-form » retiré (billet l. 15 ; manuscrit l. 119). | **F, sauf Carbon.** Le script n'écrit rien sans `--out` et refuse d'écraser ; `test_mort_halberstadt_v2.py` exige un chemin et refuse d'écraser (constaté sur des copies) ; `c_seuil` est corrigé. « Closed-form » retiré (billet l. 56 ; manuscrit l. 123). **Le compagnon de Carbon n'est pas traité**, réserve déclarée (mineur B-5). |

---

## 2. Défauts

### Portée de référence

1. **R-1 (majeur) — nécessité résiduelle dans le billet.**
   - *Où* : `P/billet-lesswrong-evasion-post-entrainement-en-v3.md`, l. 90 : « producing a deployed policy that both favors stealth … and evades deployment monitoring $M_{audit}$ requires: (H1)…; (H2) survival against $M_{loop}$ correlates positively with survival against $M_{audit}$; (H3)… ».
   - *Problème* : c'est l'affirmation de nécessité que la correction 6 retire. Elle est de plus fausse sous B pour H2, puisque le contre-exemple à covariance nulle, cité par le même billet l. 98, fait monter la survie à l'audit sans corrélation positive. La phrase suivante, qui se défend de revendiquer cette nécessité, contredit la première sans l'effacer.
   - *Correction proposée* : supprimer « requires: (H1)…(H3) » comme l'a fait le manuscrit de référence. Sinon, écrire « Three quantities matter: (H1)…, (H2)…, (H3)… ; we prove neither that they are necessary nor that they are sufficient. »
2. **R-2 (majeur) — `test_mort_halberstadt_v2.py` peut réécrire son JSON scellé.**
   - *Où* : `docs/notes/cartographie-mathematiques-ouvertes-v1/test_mort_halberstadt_v2.py`, l. 400 : `sortie = … else (pathlib.Path.cwd() / "resultats-test-mort-halberstadt-v2.json")`.
   - *Constat* : la docstring (l. 12) dit « jamais à côté du script », ce qui est faux quand le dossier courant est celui du script. Lancé sur une copie dans son propre dossier, le script y a bien écrit `resultats-test-mort-halberstadt-v2.json`. Dans le dépôt, ce fichier existe et il est scellé. C'est le défaut que la correction 10 visait (règle des versions, R12).
   - *Correction proposée* : reprendre la garde de la variante B (chemin exigé, refus d'écraser), dans une version neuve v3 du script.
3. **R-3 (mineur) — $p_f = 0$ encore traité comme un cas de R1.**
   - *Où* : `P/manuscrit-arxiv/main-v3.tex`, l. 210 : « if $\Pi_f$ is unreachable ($p_f = 0 \iff \Delta D_{KL}=+\infty$) or non-maintainable … then $\lim \pi_B(\Pi_f) = 0$ ».
   - *Problème* : la l. 197 dit pourtant que ce cas est hors du domaine.
   - *Correction proposée* : reprendre la variante B, l. 230 (« lies outside the domain … only an informal limit »).
4. **R-4 (mineur) — la niche décrite d'un seul côté dans la table 3, et le mot « Dilemma » gardé.**
   - *Où* : `main-v3.tex` l. 301 (« Operator B drives absolute stealth strictly above Operator A ») et légende l. 305 (« negative penalty amplifies absolute stealth strictly more »). Le titre « Rejection–Penalty Dilemma » reste dans le billet (l. 46) et le manuscrit (l. 51, 96 et 125).
   - *Problème* : la table montre pourtant $\pi_B(h)$ qui dépasse $\pi_A(h)$.
   - *Correction proposée* : reprendre le texte et la légende de la variante B (l. 326 et 330) et le titre « Rejection–Penalty Contrast ».
5. **R-5 (mineur) — « confirm these thresholds to full precision ».**
   - *Où* : `main-v3.tex`, l. 257.
   - *Problème* : les lignes de croisement sont évaluées aux seuils arrondis à quatre décimales, ce que la légende elle-même reconnaît.
   - *Correction proposée* : « illustrate these thresholds (values rounded to six decimals) ». Le titre du billet « Verified Numerical Phase-Transition Table » (l. 62) peut devenir « Numerical Table ».
6. **R-6 (mineur) — restes de vocabulaire et de notation.**
   - *Où* : manuscrit, contribution 1 (l. 50), « evasion against an off-loop deployment monitor » ; billet, l. 97, identité de R2 écrite avec $\operatorname{Cov}_{\pi_0}$ et $\mathbb{E}_{\pi_0}$ non conditionnés, alors que le membre de gauche conditionne sur $\mathcal S$.
   - *Correction proposée* : « a separate audit monitor » ; $\operatorname{Cov}_{\pi_0(\cdot\mid\mathcal S)}$, comme la variante B l. 99. La conclusion « what protects an audit is weak dependence on what the loop selects » (l. 98) est vague : « non-positive covariance (under A) or independence/negative association (under B) ».
7. **R-7 (mineur) — `verifier_exemples_papier_v3.py` réécrit en silence une sortie existante.**
   - *Où* : l. 466-470.
   - *Constat* : une seconde exécution vers le même `--out` a rendu le code 0 et réécrit le fichier. Il écrit aussi par défaut un dossier `sortie-verification-v3/` dans le dossier courant.
   - *Correction proposée* : refuser d'écraser, comme la variante B.

### Variante B

1. **B-1 (majeur) — suffisance non démontrée, et fausse sous B, introduite par la correction 6.**
   - *Où* : `P/variante-b-v3-session-fille-2/manuscrit-arxiv/main-v3.tex`, l. 211-216, et `…/billet-…-v3.md`, l. 92 : « a deployed policy that both favors stealth over honesty and evades deployment monitoring arises in particular when (H1), (H2), (H3) hold ».
   - *Problème* : H2 (covariance positive) ne suffit pas à faire monter la survie à l'audit sous B quand la pression est forte. Contre-exemple que j'ai calculé : $\beta_{loop} \in \{0{,}1 ; 0{,}5 ; 0{,}9\}$ et $\beta_{audit} \in \{0{,}1 ; 0{,}95 ; 0{,}45\}$, sur trois atomes équiprobables. La covariance vaut $+0{,}0467$ et la survie à l'audit est de $0{,}5$ sous la loi de base. Sous B, avec $k = \eta(\Delta R+C)$, elle vaut $0{,}543$ à $k=2$, puis $0{,}459$ à $k=10$, puis tend vers $0{,}45$ : elle **baisse**. De plus, H1 telle qu'elle est écrite (« overcomes the prior rarity $\log(p_h/p_f)$ ») omet le terme $\log(\beta_h/\beta_f)$, qui est nécessaire sous A.
   - *Correction proposée* : retirer le paragraphe H1 à H3, comme le manuscrit de référence. Sinon, le restreindre à A (« under Operator A, positive covariance raises audit survival for every η ») et dire qu'on ne revendique ni nécessité ni suffisance.
2. **B-2 (mineur) — « $< 1$ » faux quand $\beta_v = 0$.**
   - *Où* : manuscrit, l. 137 (« tends to $\beta_f p_f/(\beta_v p_v+\beta_f p_f) < 1$ ») et l. 200 (« under Operator A the stealthy mass has a limit strictly below one »).
   - *Problème* : le domaine admet $\beta_v = 0$, et la part vaut alors 1, ce que dit d'ailleurs le point 2 de la même proposition. La l. 200 confond aussi « stealthy mass » et part furtive *parmi les tricheurs*. Sous A, la masse furtive absolue tend vers $\beta_f p_f/(\beta_v p_v+\beta_f p_f)$, qui ne vaut 1 que si $\beta_v = 0$ ; la phrase est donc juste seulement pour $\beta_v > 0$.
   - *Correction proposée* : « $\le 1$, and $< 1$ whenever $\beta_v > 0$ », ou « which can be small » comme la référence.
3. **B-3 (mineur) — chiffre faux à la sixième décimale.**
   - *Où* : manuscrit, l. 326 et légende l. 330 : « $\pi_A(\Pi_h) = 0.827379$ ».
   - *Problème* : la valeur exacte est $0{,}827382$ (recalculée : $0{,}85/(0{,}85 + 0{,}024\,e^{2})$). $0{,}827379$ est $\pi_B(\Pi_h)$ au seuil arrondi $C = 0{,}2792$, la ligne en gras de la table.
   - *Correction proposée* : écrire $0.827382$, ou $0.827$ comme le billet et la remarque l. 190.
4. **B-4 (mineur) — Korbak, Perez et Buckley 2022 absent du commentaire.**
   - *Où* : `…/commentaire-…-v3.md`.
   - *Correction proposée* : reprendre la dernière phrase du commentaire de référence (l. 20).
5. **B-5 (mineur) — compagnon `.sha256` de la contre-lecture de Carbon non traité.**
   - *Constat* : c'est déclaré en réserve 2 de la table. La portée de référence a déjà versé `contre-lecture-carbon-high-publication-v1.md.v2.sha256`, propre et concordant (`ae7ab7d1…`, vérifié).
   - *Correction proposée* : adopter ce fichier.

### Communs aux deux portées (signalés pour symétrie, hors liste fermée)

- **C-1 (réserve R7).** Les références bibliographiques ajoutées (Price, Nature 227:520-521 ; Robertson, Animal Production 8:95-108 ; Fisher 1930 ; Korbak et al. 2022 ; et pour la variante B, Bailey et al. 2024) ne sont pas vérifiées sur PDF. Aucun chiffre n'en est tiré, mais pages et volumes sont à vérifier avant diffusion. Les deux portées le déclarent : erratum de référence, point 8 ; table B, réserve 1.
- **C-2 (mineur).** Le titre du théorème 1, « Exact Characterization of Stealth Selection under an Imperfect Filter », est gardé de la v2 dans les deux manuscrits. « Exact Thresholds for Stealth Selection » serait plus juste.
- **C-3.** L'avis d'opportunité et la feuille de route v2 gardent « classification exhaustive en 3 régimes ». Ils sont hors du paquet et hors de la liste fermée, mais à corriger avant de s'en servir. La variante B le dit en réserve 3 ; la portée de référence n'en dit rien.

### Vérifications sans défaut

Les trois contrôles suivants n'ont relevé aucun défaut.

- **Absence de survente résiduelle**, dans les deux portées et dans les quatre pièces publiques plus le script. Je n'ai trouvé :
  - ni « universal » ;
  - ni « collapses to stealth » ;
  - ni « backfire », sinon en négation dans la variante B (« A penalty is not a backfire ») ;
  - ni « 14,000 » comme argument ;
  - ni « exhaustive » affirmé ;
  - ni « necessary and sufficient » appliqué au théorème 2 entier : il ne reste que pour le critère R1, ce qui est correct ;
  - ni « off-loop » présenté comme suffisant ;
  - ni « mathematically right » ;
  - ni « resolves the question exactly ».
- **Nombres nouveaux recalculés indépendamment** (script `recalcul_independant.py` du bloc-notes, arithmétique rationnelle exacte quand c'est possible). Tous concordent avec les deux portées, sauf B-3 :
  - le placement hors boucle : $1/2 \to 37/50$, soit $+6/25$ ;
  - l'audit dans la boucle : $3/4 \to 7/12$ ;
  - la covariance nulle exacte : $19/30 \to 0{,}77002$ à $k = 4$ ; dérivée en 0 nulle, valeur jamais inférieure à $19/30$ sur $k \in [0, 50]$ ;
  - la part furtive limite : $3/128$, et $125/128$ de triche visible ;
  - le logarithme de la cote : $+195{,}27$ et $-92{,}12$, seuil $1{,}438$ ;
  - les récompenses hétérogènes : $0{,}8810 \to 0{,}8748$ ;
  - la niche : $\pi_B(h)$ vaut $0{,}776 \to 0{,}827382 \to 0{,}918$, la triche totale $0{,}1726$ sous A contre $0{,}0819$ sous B à $C = 2{,}5$ ;
  - $\Delta R = 3$ : $\pi_B(h) = 0{,}3935$ contre $\pi_A(h) = 0{,}0072$ ;
  - $C^*_{R3} = 5{,}462585$.
- **Opérateur de rejet pur présenté comme un choix de modèle** : c'est fait dans les quatre pièces publiques des deux portées.

---

## 3. Sondage de la table de correspondance de la variante B

J'ai sondé vingt cases, au-delà des dix demandées : ligne 1 en entier (billet, commentaire, manuscrit, README, script) ; ligne 2 (billet, manuscrit, script) ; ligne 3 (billet, manuscrit, script) ; ligne 4 (billet avec $+195{,}3$ et $-92{,}1$, commentaire, manuscrit, README) ; ligne 5 (billet, manuscrit, script) ; ligne 7 (billet, manuscrit) ; ligne 8 (manuscrit et bibliographie) ; ligne 9 (billet et manuscrit) ; ligne 10 (billet, script, test, réserve sur Carbon). **Les vingt sont exactes** : l'endroit cité existe et contient bien la correction annoncée.

Les « vérifications faites » de la table sont reproduites :

- deux sorties identiques avec et sans `--out` ;
- refus d'écraser ;
- tables et exemple rationnel identiques à la v2 ;
- `test_mort_halberstadt_v2.py` sans échec : sa sortie est d'ailleurs identique octet pour octet au JSON scellé de la référence `resultats-test-mort-halberstadt-v2.json` ;
- PDF de 11 pages, cohérent avec le `.tex` (sondé par `pdftotext`).

La seule réserve sur la table est de fond, pas d'exactitude. Elle range « arises in particular when » (ligne 6) comme correction de la nécessité, alors que c'est le défaut B-1.

---

## 4. Recommandation

**Retenir la variante B comme base.** Ses avantages :

- toutes les corrections sont portées, et chaque contre-exemple est chiffré dans le billet ;
- la remarque « Placement is not covariance » et la remarque sur les deux côtés de la niche sont propres ;
- le script, son docstring et son JSON décrivent honnêtement les familles d'essais (cas particulier, tautologie), avec des contrôles exacts pour toutes les affirmations nouvelles ;
- aucune écriture par défaut, aucun écrasement, y compris pour le test interne ;
- le cas négatif du rapport des seuils est traité, et la phrase sur Lean est ramenée à « no formal proof is claimed » ;
- une table de correspondance vérifiable, et qui dit vrai.

**Passages à reporter de la portée de référence ou à corriger dans la variante B :**

1. **Retrait du paragraphe H1 à H3** : manuscrit l. 211-216 et billet l. 92. Le remplacer par l'ouverture de la section 3 du manuscrit de référence (l. 197) : « three levers… not claimed to be an exhaustive classification: we do not prove that avoiding deployment-effective evasion requires any one of them… ». Cela corrige B-1.
2. **Compagnon de Carbon** : adopter `contre-lecture-carbon-high-publication-v1.md.v2.sha256` de la référence (B-5).
3. **Commentaire** : ajouter la phrase d'antériorité de la référence (l. 20), qui cite Korbak, Perez et Buckley 2022 (B-4).
4. **Point 4(a) du manuscrit** : reprendre la formulation exacte de la référence (l. 133), « with equal rewards, $\pi_A(\Pi_f\mid\Pi_{tr}) = \beta_f p_f/(\beta_v p_v+\beta_f p_f)$ for every η, which can be small ». Corriger aussi la l. 200 (B-2) et remplacer $0.827379$ par $0.827382$ (B-3).
5. **Facultatif, mais juste et utile** : la phrase de la référence (billet l. 42 ; manuscrit l. 89) selon laquelle l'opérateur A coïncide avec un entraînement sans moniteur suivi d'un rejet unique à l'inférence.

Si l'on gardait au contraire la portée de référence comme base, il faudrait y corriger R-1 et R-2 (majeurs), puis reporter de la variante B :

- la remarque « Placement is not covariance » ;
- le texte et la légende de la table 3 ;
- « illustrate » ;
- la phrase sur $p_f = 0$ dans R1 ;
- le script et le test à refus d'écraser.

C'est plus de travail pour un résultat équivalent.

Dans les deux cas, la diffusion reste suspendue :

- aux vérifications sur PDF exigées par R7 (C-1) ;
- à la vérification par ce même contre-lecteur des corrections ci-dessus (pièce de classe B) ;
- au geste de Lazar.

---

## 5. Commandes lancées

Toutes en lecture locale ou sur des copies dans le bloc-notes ; aucun fichier du dépôt n'a été modifié (`git status --short` vide à la fin).

```
git status ; git log --oneline -5
git show origin/audit/evasion-post-entrainement-v1:docs/notes/audit-evasion-post-entrainement-v1/rapport-audit-evasion-post-entrainement-v1.md > <bloc-notes>/audit.md
git show origin/audit/...:rapport-audit-....md | sha256sum ; git log --oneline -3 origin/audit/evasion-post-entrainement-v1
cat -n <toutes les pièces v2, v3 de référence, variante B, errata, LISEZMOI, table>
git diff --no-index (v2 ↔ v3 de référence ; v2 ↔ variante B) pour le manuscrit et le script ; diff test_mort v1 ↔ v2 (les deux)
grep -n -i -E "universal|exhaustive|collaps|backfire|closed.form|14,000|necessary.and.sufficient|dilemma|off-loop|full precision|requires|rational arithmetic|resolves|mathematically right|characteriz" <les huit pièces publiques v3>
awk/grep : extraction des 112 valeurs des tables (v2, v3 de référence, variante B) puis md5sum ; même chose pour les tables des billets
cp verifier_exemples_papier_v3.py (les deux) → <bloc-notes>/runA, runB
python3 -I verifier_exemples_papier_v3.py --out <bloc-notes>/runA/out   (référence ; cmp avec le JSON scellé : identique ; seconde exécution : réécrit sans refus ; --out = dossier du script : refusé)
python3 -I verifier_exemples_papier_v3.py > stdout.json ; --out o.json ; --out o.json de nouveau   (variante B ; identique au JSON scellé ; refus d'écraser)
cp test_mort_halberstadt_v2.py (les deux) → <bloc-notes>/tmA, tmB
python3 -I test_mort_halberstadt_v2.py   (référence, dossier courant = dossier du script : écrit à côté du script ; identique au JSON scellé)
python3 -I test_mort_halberstadt_v2.py ; ... r.json ; ... r.json de nouveau   (variante B : usage exigé, écrit, refus d'écraser ; cmp avec le JSON scellé de la référence : identique)
python3 -I <bloc-notes>/recalcul_independant.py   (recalcul indépendant de tous les chiffres nouveaux)
python3 -I -c "... comparaison des JSON v2 / v3 / variante B ..." ; python3 - (contre-exemple à covariance positive sous B)
sha256sum -c <compagnons .sha256 des pièces v3, des deux portées>   (toutes OK)
cat contre-lecture-carbon-high-publication-v1.md.sha256 et .v2.sha256 ; sha256sum du fichier (concorde)
pdftotext main-v3.pdf (les deux) ; grep de phrases témoins ; pdfinfo (10 et 11 pages)
git show --stat b1006d58 ; git status --short
```
