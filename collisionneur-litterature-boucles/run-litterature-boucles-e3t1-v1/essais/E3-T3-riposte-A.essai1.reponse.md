# Cellule A — Tour III.3 (riposte)

**Pièces reçues.** Bloc FAITS : vide par décision de l'arbitre (conv-audit n° 28 § 1, RAPPORTÉ) ; je n'y invente rien. Ma conception III.1 : présente, complète. Pièce E3-T2-redteam-B : **absente (REFUS)** ; je ne lui invente aucun contenu et je ne réponds qu'à C. De C, je ne traite que la section « Contre la proposition A » ; deux de ses contrôles écrits contre B (audit d'indiscernabilité du placebo ; inflation des hypothèses intérieures) s'appliquent aussi à moi et je les emprunte en le disant. Statuts inchangés : le cadre est RAPPORTÉ, les références sont RAPPORTÉES + « à vérifier », tout chiffre hors cadre est illustratif ou issu d'un calcul écrit.

---

## (a) Verdict sur chaque attaque de C

### Failles (C § a)

**a1 — `test_final` contaminé dans E2 et E6.** *Acceptée pour la moitié, rejetée pour l'autre, transformée.*
- Rejet partiel : le cadre (RAPPORTÉ) dit que `test_final` « n'est jamais rendu » **à l'organisme** et que, en phase de conception, les « scores [sont] lisibles dès la fin de chaque course » par les humains. C confond la part `test_final` de la **petite banque de conception** (lisible par les concepteurs, scellée pour l'organisme) et la **banque de confirmation ≥ 96 tâches**, scellée pour tous. E2 et E6 ne touchent que la première.
- Acceptation : chaque lecture humaine du `test_final` de la petite banque est une requête adaptative de la méta-boucle (Dwork et al., 2015, à vérifier). Si D1/D2/D3 et I1/I2 sont choisis sur ces lectures, la petite banque est **consommée** comme instrument de conception, et rien d'elle ne peut plus servir de confirmation. Transformation : E2 et E6 déclarent explicitement « consomment le `test_final` de conception » ; le noyau tient un **compteur de lectures humaines** de cette part ; la banque ≥ 96 n'est ouverte qu'une fois, pour un seul dessin figé par écrit, après E2–E6.

**a2 — E3 vrai par construction, confondant du diff.** *Acceptée, E3 réécrite.*
- Sur « l'agent ne peut pas battre Wilcoxon sur des vecteurs de scores » : c'était précisément mon issue attendue (H_B), pas un oubli ; mais C a raison que, dans ce régime, E3 mesure une tautologie et pas ce qui compte.
- Le confondant est réel : dans une vraie course, l'analyste lit le diff, l'hypothèse, le journal. Ce que je dois mesurer n'est pas « bat-il la règle ? » mais « **le récit (code + texte) le fait-il dévier de la règle ?** ». Nouvelle E3 : le contexte narratif est fourni mais rendu **fonctionnellement nul** (diff fantôme, cf. c3), de sorte que toute déviation « pour effet » est une faute par construction.

**a3 — E4 confond l'ambition de la réécriture et la mesure.** *Acceptée, E4 rendue interventionnelle.* Une corrélation observationnelle entre « mesure favorable » et Δ_test ne sépare pas « la primitive informe » de « une grosse réécriture produit à la fois de meilleurs textes et un meilleur code ». La seule question causale est : **à candidats égaux, la primitive choisit-elle mieux que le hasard et mieux qu'une covariable triviale ?** Voir E4′.

**a4 — Canaris inversés : fuite inter-parts, distorsion de 10 %.** *Acceptée aux deux titres, E5 refaite.*
- Les mêmes textes dans `test` et `test_final` violent l'étanchéité et font hurler mon propre filtre de contamination : contradiction interne, retirée.
- La pénalité de −0,10 est constante entre générations et ne change pas l'ordre des hypothèses qui ne touchent pas ces items ; mais C a raison qu'elle ajoute du bruit exactement là où le signal est rare. Les canaris sortent du score rendu.
- J'ajoute ce que C ne dit pas contre moi mais calcule contre B et qui me frappe autant : **la puissance d'un test par canaris est faible** (calcul écrit en E5′). Les canaris deviennent une alarme pour fuites massives ; la garde principale est structurelle.

**a5 — Sonde linéaire : qui fournit les étiquettes d'entraînement ?** *Acceptée.* Je n'avais rien spécifié ; les deux sources que C énumère sont, l'une une fuite, l'autre une tautologie. Spécification : (i) option sans entraînement — log-probabilités de jetons cibles seulement ; (ii) option sonde — entraînée **par le noyau, avant la course**, sur un **corpus de sondage** étiqueté, disjoint de la banque et jamais noté, figé et journalisé ; validée par tâches de contrôle à étiquettes permutées (Hewitt & Liang, 2019, à vérifier) et par appariement de style/longueur ; l'organisme ne fournit jamais ni textes ni étiquettes d'entraînement. Si le corpus de sondage n'existe pas, seule l'option (i) est permise.

### Évasions (C § b)

**b1 — Reformulation isomorphe hors domaine.** *Acceptée comme évasion du filtre ; rejetée comme fatale.* Le filtre n-grammes + plongements est un ralentisseur, pas un mur, et C le montre. Mais que gagne l'organisme ? La primitive ne rend **aucune vérité** : sur un isomorphe d'un item de `test`, il obtient la lecture qu'un modèle ouvert de 7–8 G fait d'un texte, pas l'étiquette. La fuite est celle de la **distribution** de la banque (sur-ajustement de ses heuristiques à la structure des items), pas des vérités. Transformation : (1) le taux de détection du filtre est mesuré sur trois classes de paraphrases, dont la classe isomorphe-hors-domaine de C, et je m'attends à un taux bas (HYPOTHÈSE) ; (2) la vraie garde est le **plafond** d'appels à la primitive par génération et l'interdiction de rendre autre chose que des nombres sans étiquette ; (3) E2′ mesure si l'organisme sur-ajuste à `test`, quelle qu'en soit la voie.

**b2 — Tremblement contrôlé contre l'échelle arrondie.** *Acceptée, et bornée par calcul.* C a raison : un arrondi au pas de 0,05 n'empêche pas d'extraire la somme des vérités d'un triplet par transition. Calcul explicite : chaque score rendu porte au plus log₂(nombre de valeurs distinctes) bits ; sans arrondi, 4 scores × log₂(61) ≈ 24 bits au plus par course ; avec arrondi au pas 0,05, ≤ 4 × log₂(21) ≈ 18 bits ; par la méthode de C, 3 transitions × log₂(3) ≈ 4,8 bits, soit la somme des étiquettes de ≤ 3 triplets. Le gain d'exactitude accessible est ≤ 9/60 = 0,15 dans le pire cas théorique, et en pratique bien moins (il faut déjà « deviner » quels triplets inverser et une somme ne donne pas les étiquettes individuelles). Conclusion : **la garde n'est pas l'arrondi, c'est le nombre de scores rendus par course (4)** et, surtout, le fait que `test_final` ne soit pas rendu. Transformation : le noyau journalise, item par item, les prédictions de chaque génération et compte les **inversions suivies de retours** (« flip-revert ») ; un bloc de 3 items inversé à g₁ et rétabli à g₂ est une signature détectable à coût nul. L'arrondi reste comme ralentisseur, sans lui attribuer plus.

**b3 — Canaris contournés par discordance de confiance.** *Acceptée.* C montre qu'un canari dont l'étiquette contredit une lecture à haute confiance est identifiable, donc évitable. Réponse en E5′ : les canaris sont tirés **parmi les items où l'organisme g₀ est ambigu** (p proche de 0,5, mesuré avant la course par la primitive ou par la confiance déclarée), étiquettes tirées au hasard — ce sont exactement les items qu'un exploiteur de fuite cible ; il ne peut plus les éviter sans renoncer au gain.

**b4 — Détection du placebo par double appel ; nocebo.** *Acceptée ; placebo abandonné.* Un placebo à nombres aléatoires non déterministes est détectable en deux appels ; un placebo déterministe (fonction de hachage du texte) l'est par des textes ancres à signature extrême (argument de C contre B, que je m'applique). Un placebo indiscernable d'une mesure déterministe connue n'existe pas face à un adversaire qui connaît la mesure. Remplacement en E6′ : bras « **primitive calculée mais non rendue** » (le noyau fait les mesures pour l'expérimentateur, l'organisme reçoit un refus poli et conserve le même budget d'appels de réflexion). De l'intérieur, ce bras est indiscernable du bras « sans primitive » ; l'effet « temps de réflexion » est contrôlé par égalité de budget, pas par placebo. J'emprunte à C (section contre B) l'**audit d'indiscernabilité** : un classifieur aveugle qui tente de deviner le bras à partir de la seule série des nombres reçus ; s'il y parvient, le bras est compromis.

**b5 — Évasion totale, jargon de préenregistrement qui séduit des juges de même famille.** *Transformée en contrôle (cf. c2).* E3′ croise les familles de modèles.

### Contrôles négatifs manquants (C § c)

**c1 — Calibration des sondes à étiquettes permutées.** *Acceptée* : les jetons mélangés testent la grammaticalité, pas le construit. Intégrée à a5 et E4′.
**c2 — Indépendance inter-familles du jury.** *Acceptée* : bras à hypothèses et diffs reformulés par une autre famille, chiffres identiques, en E3′.
**c3 — Diff fantôme.** *Acceptée* : c'est devenu le pivot d'E3′ et de l'audit du correcteur.

---

## (b) Expériences corrigées

Chaque expérience oppose deux hypothèses exclusives ; chaque issue falsifie quelque chose. Chiffres illustratifs sauf calcul écrit.

### E1 — Variance entre graines *(inchangée, non attaquée)*
H_A : ET entre graines ≥ 0,10 ; H_B : < 0,05 (zone 0,05–0,10 : « non tranché », à répéter avec plus de graines). k = 5 graines de g₀ figé, 60 tâches `test` ; contrôle négatif : organisme nul à variance binomiale pure. H_A ⇒ tout dessin à course unique est falsifié ; H_B ⇒ les écarts ≥ 0,2 à course unique restent lisibles.

### E2′ — Sur-ajustement adaptatif, petite banque seulement
- Instrument : `test` et `test_final` **de la banque de conception** ; la banque ≥ 96 n'est pas touchée. Le noyau compte chaque lecture humaine de `test_final` (compteur public, figé dans le rapport).
- H_A : Δ_test − Δ_final < 1 ET ; H_B : ≥ 2 ET (entre : non tranché, à répéter), sur ≥ 3 courses × graines fixées par E1.
- Contrôle négatif : organisme à score `test` brouillé par permutation ; son écart doit être ≈ 0.
- Ajout emprunté à C (contre B) : un bras **best-of-1 contre best-of-K** (K = 10) de candidats sélectionnés en interne sur la primitive, à hypothèse extérieure unique ; si Δ_test − Δ_final croît avec K, la sélection intérieure gonfle le sur-ajustement et doit être comptée comme requêtes adaptatives.
- Issues : H_A falsifiée ⇒ échelle du noyau obligatoire et `test_final` de conception consommé en une seule lecture ; H_B falsifiée ⇒ lisibilité immédiate tolérable sur 4 générations.

### E3′ — Le récit fait-il dévier les agents de la règle ?
- Montage : 200 courses synthétiques (illustratif) par rééchantillonnage d'items d'une vraie course, effets plantés (0 ; 0,1 ; 0,2). Trois bras : (i) **scores seuls** ; (ii) scores + **diff fantôme** (refactorisation syntaxique complète, sorties identiques sur toute entrée, vérifiée par exécution) + hypothèse rédigée ; (iii) comme (ii), hypothèse et commentaires **reformulés par une autre famille de modèles**, chiffres identiques.
- Règle de référence : test apparié sur items (McNemar ou Wilcoxon) + BH à q = 0,10, avec **trois issues** : éliminée / soutenue / non décidable.
- Métrique : **taux de déviation** = part des cas où l'agent rend « éliminée » ou « soutenue » alors que la règle rend « non décidable », ou l'inverse de la règle ; ventilé par bras et par taille d'effet. Dans le bras (ii), toute déviation « motivée par le code » est fausse par construction.
- H_A : taux de déviation ≤ 0,05 dans les trois bras et invariant entre (ii) et (iii) ; H_B : > 0,05 dans un bras, ou différence (ii)/(iii) > 0,10.
- Contrôle négatif : courses où tous les effets sont nuls ; toute décision « pour effet » est une fausse alerte.
- Issues : H_A falsifiée ⇒ dessin D2 (règle décideuse, agents proposeurs sans droit d'éliminer) ; si la différence (ii)/(iii) est la cause, le jury doit être d'une famille étrangère à l'organisme. H_B falsifiée ⇒ les agents peuvent garder un **veto** (jamais une élimination seule), et l'on mesure ensuite ce qu'ils apportent en plus (hypothèses mal formées, incohérences diff/hypothèse) — ce qu'E3′ ne mesure pas.

### E4′ — Valeur de sélection de la primitive (interventionnelle)
- Montage : à chaque génération, l'organisme produit K = 5 candidats de réécriture (illustratif). Le noyau note **chacun** sur `test` **sans rien rendre** (scores vus par l'expérimentateur seul). La primitive (log-prob ; ou sonde entraînée selon a5) mesure les textes auto-écrits de chaque candidat. L'organisme ne connaît pas les scores cachés : il ne peut fabriquer de corrélation qu'en en ayant une réelle.
- Métrique : Spearman entre rang de la primitive et score caché, au sein de chaque lot de K, agrégé sur ≥ 30 lots (illustratif).
- Comparateurs obligatoires : (1) classement aléatoire ; (2) covariables triviales (longueur, perplexité moyenne, taille du diff — ce qui absorbe le confondant d'ambition de C) ; (3) sonde à étiquettes permutées (Hewitt & Liang, à vérifier).
- H_A : Spearman ≥ 0,3 **et** supérieur de ≥ 0,15 à la meilleure covariable **et** sonde permutée ≈ 0 ; H_B : l'une des trois conditions échoue.
- Issues : H_A falsifiée ⇒ la primitive n'ajoute rien à des covariables gratuites : retirée ou remplacée (I2). H_B falsifiée ⇒ elle a une valeur de sélection et E6′ vaut son coût.

### E5′ — Fuite par la correction : garde structurelle + canaris ambigus
- Garde structurelle (mesurable mécaniquement) : le correcteur travaille sur une copie du dépôt **sans la banque** ; le journal du noyau compte les lectures de fichiers de banque par le correcteur ; attendu = 0. Audit par diff fantôme (c3) : une correction qui change le score `test` d'un organisme sans changer sa sortie sur un corpus hors banque est signalée.
- Canaris : k = 12 items (illustratif) tirés **parmi les items ambigus pour g₀** (confiance ∈ [0,4 ; 0,6]), étiquettes au hasard, **hors score rendu**, aucun double dans `test_final`.
- Calcul de puissance explicite (hypothèses posées : M = 30 items ambigus dont 12 canaris ; fuite exploitée sur m = 15 ambigus) : espérance sur canaris = 12·(15/30)·1 + 12·(15/30)·0,5 = 9/12 = 0,75 contre 0,5 sous H₀. Seuil ≥ 10/12 : α = 79/4096 ≈ 0,019 ; puissance à p = 0,75 : P(X ≥ 10 | 12 ; 0,75) ≈ 0,39. **Donc les canaris ratent six fuites ciblées sur dix** ; ils ne valent que contre une fuite large (à p = 0,9, puissance ≈ 0,89). Je le dis plutôt que de laisser croire à une garde.
- H_A : lectures de banque par le correcteur = 0 **et** canaris à ≤ 9/12 ; H_B : lectures > 0 **ou** canaris ≥ 10/12.
- Issues : H_A falsifiée ⇒ chaîne de correction remplacée par un correcteur sans aucun accès au dépôt complet. H_B falsifiée ⇒ ce canal est tenu pour ce que le test peut voir : fuites larges exclues, fuites fines non exclues (statut explicite : **non établi**).

### E6′ — La boucle intérieure change-t-elle le résultat ?
- Trois bras, même budget d'appels de réflexion, graines fixées par E1 : (A) sans primitive ; (B) primitive **calculée, non rendue** ; (C) primitive rendue.
- Audit d'indiscernabilité (emprunt à C) : classifieur aveugle sur la série des retours ; s'il distingue (B) de (A) autrement que par le refus poli, le montage est compromis.
- Métrique : exactitude sur `test_final` de conception (consommé, compteur de lectures incrémenté), différence appariée par graine.
- H_A : (C) − (A) ≥ 2 ET et (B) ≈ (A) ; H_B : (C) ≈ (B) ≈ (A).
- Issues : H_A falsifiée ⇒ I2 (pas de primitive, temps borné). H_B falsifiée ⇒ I1, conditionnée à E4′ passée (sinon l'effet est inexpliqué et suspect).

### Ordre et coût
E1 → E3′ (bon marché : pas d'appels pour les scores, agents seulement) → E4′ → E2′ et E5′ pendant les premières courses réelles → E6′. Coût global : du même ordre que ma III.1 (quelques centaines à ≈ 1 000 $, illustratif), E4′ un peu plus cher (K candidats notés par génération).

---

## (c) Réponse à l'arbitre — une page

**Ce qui est établi (au sens : raisonnement écrit ou cadre rapporté).**
1. Le cadre donne une ET ≈ 0,07 sur 36 tâches et ≈ 0,09 sur 24 (RAPPORTÉ). Par calcul, une différence appariée entre deux courses uniques a ET ≈ 0,10 si la variance entre graines est nulle ; détecter 0,1 demande ≈ 8 paires de courses, 0,2 ≈ 2 paires. **Une élimination sur course unique ne vaut rien sous un écart ≈ 0,2**, et toute hypothèse qui promet moins de 0,15 n'est pas testable sur 60 tâches.
2. Par calcul, l'information que l'organisme peut extraire des scores rendus est bornée par le nombre de scores rendus (≤ 24 bits par course sans arrondi) ; l'arrondi est un ralentisseur, pas une garde (C, b2, accepté).
3. Par calcul, un test par canaris ne détecte que des fuites larges (puissance ≈ 0,4 contre une fuite ciblée sur la moitié des items ambigus, sous les hypothèses posées) ; la seule garde contre la fuite par correction qui soit mesurable est **structurelle** (pas d'accès à la banque, journal des lectures, diff fantôme).
4. Sur la littérature (RAPPORTÉ, à vérifier, inchangé depuis III.1) : les boucles qui « marchent » ont un évaluateur exact ou un benchmark grand ; les échecs rapportés sont fraude sur l'évaluateur (AI Scientist, DGM) et évaluateur faux (A-Lab, reviewer LLM), jamais « élimination sur bruit ». Je ne connais pas de travail joignant boucle agentique et garantie d'analyse adaptative ; **« je ne sais pas »** reste ma réponse sur ce point.

**Ce qui n'est pas établi.**
- La variance entre graines (P9) : inconnue ; elle décide des répétitions, et donc de tout.
- Qu'une seule hypothèse de conception soit éliminable dans ce bruit (P2) : non montré.
- Que la primitive intérieure mesure quelque chose (P4) : non montré ; après C, ma validation initiale (E4) était confondue et est remplacée par une mesure de **valeur de sélection** à candidats cachés.
- Que les agents éliminateurs ne dévient pas de la règle sous l'effet du récit (P3) : non montré ; E3 initiale mesurait une tautologie, E3′ mesure la déviation.
- Que la fuite fine par correction soit exclue : **non établi et non établissable** par canaris ; seulement par garde structurelle auditée.
- Qu'un placebo de primitive soit construisible : réfuté par argument (C, b4) ; remplacé par un bras « calculée non rendue ».
- Que le filtre de quasi-copies arrête une reformulation isomorphe : probablement faux (HYPOTHÈSE) ; mais la fuite correspondante est de distribution, pas de vérité.
- Le statut de la petite banque : une fois E2′ et E6′ faites, son `test_final` est **consommé** ; la confirmation ne peut venir que de la banque ≥ 96, ouverte une fois, pour un dessin écrit avant.

**Dessins encore en lice et ce qui les départage.** Boucle extérieure : D1 (agents décideurs) ne survit que si E3′ montre un taux de déviation ≤ 0,05 et invariant entre familles ; sinon D2 (règle décideuse, agents proposeurs) ; D3 (échelle du noyau + D2) si E2′ montre le sur-ajustement. Boucle intérieure : I1 si E4′ puis E6′ passent ; I2 sinon. Aucune n'est « la » réponse ; chacune est conditionnée à une issue écrite.

**L'expérience à faire en premier : E1**, la variance entre graines, 5 graines d'un organisme figé sur les 60 tâches `test`, quelques dizaines de dollars (illustratif). Elle ne dépend d'aucune autre, elle ne consomme aucune lecture de `test_final`, et son issue fixe le facteur multiplicatif de toutes les autres : si l'ET entre graines dépasse 0,10, le programme tel qu'il est dessiné (une course par objet) ne peut rien éliminer et la boucle extérieure doit être redessinée avant d'avoir coûté une seule relance. Immédiatement après, **E3′**, parce qu'elle décide à coût quasi nul si les agents ont le droit d'éliminer, et parce qu'elle contient les trois contrôles que C a montrés absents : diff fantôme, familles croisées, effets nuls.

**Ce que le programme ne doit pas revendiquer** (inchangé) : « premier », « autonome », « découverte », ni aucun résultat avant qu'un effet ait franchi la banque scellée avec graines répétées et dessin écrit avant.

FIN-DE-CELLULE