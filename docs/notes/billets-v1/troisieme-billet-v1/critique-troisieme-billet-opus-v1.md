# Critique des propositions pour un troisième billet : A reste le meilleur des trois, mais sa thèse doit être retournée et son antériorité principale est dans la théorie de la détection ; B est pris en grande partie par un papier de Redwood du 16 novembre ; C n'est pas un billet (v1)

- **Date** : 21 novembre 2026, de 18:43 à 18:51 UTC (`date -u`). **Auteur** : Claude Opus 5.5 (`claude-opus-5-5`), critique neuf, effort élevé, lancé par l'orchestration de la session mère. Je n'ai écrit ni la pièce critiquée ni aucune des conceptions qu'elle cite. Pièce de travail (classe C), non contre-lue. Ni commit, ni poussée, ni appel payant. Dépôt à `43126a6da` à la fin.
- **Pièce critiquée** : `docs/notes/billets-v1/troisieme-billet-v1/propositions-troisieme-billet-fable-v1.md` (empreinte vérifiée égale à son compagnon), lue en entier, avec la sortie `calculs-troisieme-billet-v1.txt`, blocs A et B.
- **Décisions relues** (empreintes vérifiées égales aux compagnons) : N-076 v1, en-tête et § 0 à 3, errata 1 et 2 en entier ; N-075 v3, § 2 et § 7 ; son erratum 3 v2, point 11 et § 4 ; N-077 v1, § 0 à 4 ; N-062 v1, en entier. Lignes GO-2026-11-19-28, -11-21-50, -63 et -69 de `registres/go.md`, par leur identifiant.
- **Relu par moi à la page, sur pièce empreintée** : Wen et al., arXiv 2411.17693 v1, rang 6 (`docs/sources/pdf/2411.17693v1.pdf`) ; le billet de Hebbar, copie du dépôt, par motifs ; Bhatt et al. (« Ctrl-Z »), rangs 5, 7, 8, 9 ; Kutasov et al., rang 5 ; Lucassen et Kaufman, rangs 2 et 10 ; le glossaire de l'Agence internationale de l'énergie atomique, rangs 113-114. Toutes les citations que la pièce en tire sont exactes (une case de calcul refaite à la main : z = 2,326, μ = 0,5, m = 400, n = 1 000 donne 27,5 %, et le plancher 23,3 % ; la référence de 12 393 actes se retrouve aussi).
- **Pièces neuves, téléchargées par moi dans mon bloc-notes, non versées au dépôt** (le versement revient à la mère) :
  - Shenoy, Zang, Gan, Tay, Ngo, Prasanna, Stastny, Hebbar, « Auditors Struggle to Catch Sabotage In End-to-End Transcripts of AI Safety Research », arXiv 2611.21832 v2 (18 novembre 2026), `e4358c76aed8219feaf3ed1b42098fe26a3fdee327561c16adb4720c60d9fed6`, rangs 1, 7 et 31 lus ;
  - Tandra, *Spectrum Sharing by Cognitive Radios: Opportunities and Challenges*, thèse, rapport technique de Berkeley UCB/EECS-2009-192 (direction Sahai), `8965f9961f778f4c10750e8986e25fa84f694fda0f8dc52d1d7f6dcddf68e1bd`, rangs 5, 24-25, 50, 53 et 55 lus.
- **Recherche en ligne** : treize requêtes et cinq lectures de pages (moteur général, arXiv, LessWrong, Alignment Forum, GreaterWrong, FAR.AI, blog de Redwood), sans le nom du programme. Ce qui n'a été vu que par résumé d'outil ou par page web est marqué [web] : non opposable (R7), aucun chiffre n'en est tiré.
- **Non ouvert** : tout ce que le mandat interdit ; l'annexe réservée de la note du protocole X sur le dommage ; les brouillons et fiches des deux billets existants ; tout résultat ou score.
- **Marques** : [lu] = relu par moi à la page dite (rang dans le fichier) ; [web] = page web ou résumé d'outil, non opposable ; [non vérifié] = ni pièce ni page ; [jugement] = estimation de ma part. « Non trouvé » veut dire « non trouvé par mes requêtes » (R8).

## Verdict

1. **Classement : A, puis B réduit à une note de quelques paragraphes après l'entretien, puis C, qui n'est pas un billet.** Je garde l'ordre du concepteur, mais pour d'autres raisons, et avec moins de confiance.
2. **A est mal centré.** La phrase de Hebbar ne parle pas d'abord d'un manque d'actes honnêtes. Elle dit qu'on ne peut pas échantillonner la version bénigne *du modèle surveillé*. C'est un écart systématique, pas une variance. Le billet doit donc ouvrir sur la tolérance à l'écart (son résultat 3 et le sens de son résultat 2). Le plateau en m (son résultat 1) passe au second rang.
3. **L'antériorité de A est plus lourde que la pièce ne le dit.** Toute la structure de A (un plancher qu'aucun nombre d'échantillons ne franchit, une sortie par étalonnage en service, la condition que cet étalonnage ne soit pas contaminé) est publiée en théorie de la détection sous le nom de « mur de rapport signal sur bruit », depuis 2008 [lu, thèse de Tandra]. La pièce la marque « je crois [non vérifié] ». Dans le contrôle, Hebbar lui-même l'a dite à voix haute en mars 2025 [web].
4. **B est pris pour l'essentiel par un papier de Redwood du 16 novembre** (Shenoy et al., cosigné par Hebbar et Gan), que la pièce ne cite pas. Ce papier mesure l'identification des auditeurs et la baisse qui suit le choix des cibles par le saboteur [lu, rang 1]. B gagne en actualité, mais perd sa place de billet et son poids de nouveauté.
5. **C n'a rien de neuf pour un lecteur extérieur.** Sa thèse publique est déjà celle d'un billet de Redwood (Lucassen et Kaufman), et sa phrase propre est marquée « supposé » par N-077. Il oblige aussi à décrire en public nos modes d'induction et nos bras de mesure.
6. **Durées.** A : quatre à cinq jours jusqu'à ta plume, non trois. En ligne avant le 1er décembre : 0,25, non 0,45 [jugement].

---

## 1. Candidat A — la référence honnête

### 1.1 Antériorité : ce qui est trouvé

| Voisin | Ce qu'il occupe | Statut |
|---|---|---|
| Tandra et Sahai, « SNR Walls for Signal Detection », *IEEE Journal of Selected Topics in Signal Processing* 2 (1), 2008 ; repris dans la thèse de Tandra (2009) | Sous incertitude sur la loi du bruit, il existe des seuils « below which robust detection is impossible, regardless of how many samples we take » (thèse, rang 24, folio 12 [lu]). La sortie est l'étalonnage du bruit en service, mais « calibration will get stale (leaving substantial residual uncertainty) if it is done far in advance » (rang 53, folio 41 [lu]). Et « Any run-time calibration that aims to reduce the noise uncertainty must use data that might be corrupted by the presence of the primary signal », d'où l'exigence d'un degré de liberté « guaranteed to be uncorrupted » (rang 55 [lu]) | **Antécédent principal de A**, de ses trois résultats et de ses deux sorties. L'article de 2008 lui-même n'est pas lu : seule la thèse l'est |
| Cartes de contrôle à paramètres estimés : Jensen, Jones-Farmer, Champ et Woodall, « Effects of parameter estimation on control chart properties: a literature review », *Journal of Quality Technology* 38 (4), 2006, p. 349-364 | La performance d'une surveillance étalonnée sur un échantillon de référence de taille finie, et la taille de référence qu'il faut pour approcher le cas à paramètres connus (« phase I ») | [web], résumé seulement, aucun chiffre repris. Vingt ans de littérature sur la « phase I » : c'est exactement la question « combien d'actes honnêtes de référence » |
| Wen, Hebbar et al., arXiv 2411.17693 v1 | « errors can accumulate over long time sequences to produce overconfident credences », et cela « even in our experiments, where the reference distribution is an i.i.d. sample of the true distribution » ; note 2 : « A similar affordance is assumed in Greenblatt et al. (2023) » (rang 6 [lu]) | Déjà cité par la pièce. La pièce omet la moitié qui compte : les auteurs savent que leur référence *est* un échantillon de la vraie loi, et appellent cela une « affordance » |
| Hebbar, exposé « Low-stakes control », FAR.AI, 27 mars 2025 | D'après le résumé de la page : « try to guess how suspicious a benign model will look », à partir de solutions écrites par des personnes et de modèles de confiance plus faibles ; « it's important that the blue team is quite uncertain about what they would have observed if the model was benign » | [web], non opposable, mots non vérifiés à la source. **À lire avant toute phrase** : si la transcription tient, l'auteur du billet théorique a déjà dit que le problème est l'écart, non la taille |
| Greenblatt, « Notes on handling non-concentrated failures with AI control », blog de Redwood, 29 mars 2025 | « we're unsure how suspicious we expect behavior to be » ; un a priori sur les scores d'un modèle non comploteur | [web], non opposable |
| Zhang et Gao, arXiv 2606.10456 v2 (déjà au programme) | Une attaque qui garde la loi marginale des scores par pas « exactly equal to benign » : μ par acte vaut zéro, et le dommage passe par la corrélation | [web], résumé seulement. Touche la supposition « scores indépendants, décalage μ » de A |
| « When Lie Detectors Learn Model Identity: Confounds in Black-Box Sandbagging Detection », ICLR 2026 | Un détecteur apprend l'identité du modèle ; il faut comparer un honnête à un honnête d'un autre modèle | [web], titre et résumé seulement. C'est l'écart systématique de A, observé |

**Ce qui n'est pas trouvé** par mes requêtes : un texte du contrôle qui chiffre la tolérance « part sabotée fois écart lu », ou qui écrit une règle d'horizon « n au plus m ». Les commentaires du billet de Hebbar sur LessWrong n'en disent rien (un seul commentaire, sur le vocabulaire [web]). La recherche des travaux qui citent Hebbar, Wen et al., Terekhov et al. et Ortega-Fernandez et al., accordée à GO-2026-11-21-50 (D-P4), n'est toujours pas au dépôt à ma connaissance. Ma recherche ne la remplace pas : elle n'a pas parcouru les citants un à un.

**Ce qu'il reste à A.** Le transfert, dans le contrôle, d'un résultat de détection connu, avec trois nombres pour des moniteurs de qualité réaliste. C'est un billet de traduction honnête. La probabilité de 0,55 pour un « pont non déjà publié » que la pièce reprend me paraît trop haute : je dirais 0,35 pour « le chiffrage dans le contrôle n'est pas publié », et zéro pour la structure [jugement].

### 1.2 Solidité de la thèse

**(a) La thèse répond à une version affaiblie de Hebbar.** La phrase citée dit « if we knew exactly how suspicious a benign model would look ». Le « benign model » est la version alignée du modèle surveillé, qu'on ne peut pas tirer du tout. La référence vient d'un autre modèle, de personnes ou d'un modèle de confiance : l'écart entre elle et ce contrefactuel ne baisse pas avec m. Le résultat 1 (plateau à z / (μ √m)) suppose une référence tirée de la vraie loi honnête. C'est justement l'« affordance » que Wen et al. disent supposer (rang 6). Si le billet ouvre sur « il faut 12 393 actes honnêtes », un lecteur de Redwood répondra : « nous n'avons pas un seul acte honnête de ce modèle ». **Le billet doit ouvrir sur la tolérance à l'écart** : pour 2 % d'actes sabotés et un moniteur d'aire 0,77, l'écart entre l'honnête et sa référence doit rester sous 0,021 écart type (bloc B de la sortie, sous supposition). Puis demander : quelle référence d'un autre modèle tient cela ? Le confondant d'identité ci-dessus suggère qu'aucune ne le tient sans précaution. C'est le même calcul, dans un autre ordre. Mais cet ordre est le seul qui réponde à la phrase qu'on prétend chiffrer.

**(b) μ est choisi par l'attaquant.** Les nombres de A valent pour un saboteur au décalage fixe. Un saboteur qui répond au mieux règle μ par acte vers zéro, en gardant la loi marginale (Zhang et Gao [web]). N-076 l'écrit dans son propre test de mort « adversaire » (« l'écart lu par unité de dommage tombe à zéro sous le mode tenu à l'écart », § 2). Le billet doit dire, dans ses limites, que ses tables bornent un saboteur non adaptatif. Il ne dit rien de ce que fait un saboteur adaptatif. « Monde à scores dépendants : à faire » (plan, section 6) ne suffit pas : la dépendance est l'arme même de l'attaque connue.

**(c) La borne « pour tout test » (7,7 % à m = 400) doit sortir.** Dérivation à la main, non contre-lue (N-076, § 2, et la pièce elle-même). La garder en option (plan, ligne 4 du § 6) n'a pas de sens dans un billet dont l'argument est « un tiers peut tout rejouer ».

**(d) Face aux décisions scellées.**
- *N-076* : A est son point 1, il ne la contredit pas. Mais N-076 dit, pour ses points 1 à 3 : « sans verdict, rien ne se revendique avant qu'il soit rendu ». La section « Ce qui serait neuf » du plan ne peut paraître qu'après la recherche D-P4. La liste « Ne pas écrire » (§ 11) s'applique, la pièce le dit.
- *N-075* : A s'accorde avec la limite « sans référence honnête valable, aucune borne » du plancher (§ 2, et erratum 3 v2, § 4.1). Le billet ne doit pas glisser vers « incriminer par accumulation » comme garantie : N-075 fait des moniteurs un accélérateur et un aiguillage, non une garantie. La section 7 du plan (« l'audit de l'issue ») doit le dire dans ces termes, en citant le plancher comme publié (« Blindfold », Podkopaev et Ramdas, Gans et Holden), jamais comme nôtre.
- *N-062* : un billet public qui dit « au-delà de m, l'accumulation ne gagne plus » fixe une norme que notre accumulation sur sondes (H2) devra tenir. Cela va dans le sens de N-076 (« rappel qui croît avec l'horizon » se lit jusqu'à m). Mais si le préenregistrement de la porte de fin de phase 1 étalonne sur un jeu fixe et lit au-delà, le billet nous contredit en public. L'inventaire des m et des n de nos textes scellés (plan, ligne 5 du § 6) est donc bloquant avant la mise en ligne, et non seulement « avant la mise en ligne » au sens faible. Je le confirme.
- *N-077* : sans rapport.

**(e) Une confusion d'unités, à tenir.** Le repère « aire 0,77 » vient de Gan et al., dont l'unité est le dépôt de code entier. La pièce le dit (« repère seulement »). Dans la table du billet, mieux vaut une grille d'aires sans nom d'article, puis une phrase sur l'ordre de grandeur des aires publiées. Sinon le lecteur lira « Gan et al. exigent 12 393 actes », ce que personne n'a dit.

### 1.3 Durée

Trois jours, c'est trop court [jugement]. Il faut ajouter à la liste du § 6 : lire l'article de Tandra et Sahai de 2008 et la revue de Jensen et al. (pages à citer) ; lire l'exposé de Hebbar à sa source ; refaire le plan autour de l'écart. Il faut aussi la recherche D-P4, qui n'est pas faite. Quatre à cinq jours de session jusqu'à ta plume, puis ta demi-journée. En ligne avant le 1er décembre : **0,25**. La pièce dit 0,45 sans compter le gel, la modération d'un compte neuf ni ce qui suit.

**Concurrence de calendrier, non vue par la pièce.** Le rappel daté de `CLAUDE.md` veut, du 25 au 30 novembre, la note sur « Diffuse AI Control on Fuzzy Tasks » et la lecture des trois sources de son jugement contre la surveillance. Le billet de Hebbar en est une. **Le travail de fond de A (§ 1.1 et 1.2) est exactement cette lecture.** Je recommande de le faire d'abord sous cette forme, une note interne pour l'entretien. Le billet n'en serait que la version publique, si tu dis oui.

### 1.4 Cloisonnement

Faible. A ne parle ni de modes, ni d'organismes, ni de sondes. Deux points à tenir. La sortie par le jumeau (« nul par acte ») touche le pari apparié : en une phrase de principe, sans le mot « jumeau » ni le banc (D-2 (a) de la pièce, d'accord). Et l'inventaire des m et des n de nos textes scellés reste interne : aucun de ces nombres dans le billet.

### 1.5 Intérêt

Réel si la thèse est retournée : un lecteur du contrôle en tire une règle de compte rendu, et une tolérance qu'il peut confronter à sa propre référence. Faible sinon : « une formule de manuel, appliquée à une phrase », et la phrase visée n'est pas celle que chiffre le billet. Jugé élémentaire par un lecteur du métier : 0,65 plutôt que 0,5 [jugement]. Ce n'est pas un échec si le billet crédite la théorie de la détection d'emblée : il devient « ce que les radios cognitives savent depuis 2008, traduit pour le contrôle », un titre qui concède et qui se défend.

---

## 2. Candidat B — « Tirer au sort n'est pas reconnaître »

### 2.1 Antériorité

| Voisin | Ce qu'il occupe | Statut |
|---|---|---|
| **Shenoy et al., arXiv 2611.21832 v2, 16-18 novembre 2026, Redwood Research ; cosigné par Hebbar et Gan** | Auditeurs humains, transcription entière et droit de lancer des expériences : aire sous la courbe 0,59, et identification complète du sabotage dans 17 % des cas seulement ; meilleur modèle : 0,73 et 32 %. « When the saboteur chooses which experiments are attacked […] sabotage identification drops further » (rang 1 [lu]). En annexe D.9, le calcul de la part des alertes qui portent sur un sabotage selon la prévalence, la sensibilité et les fausses alertes (rang 31 [lu]) | **Absent de la pièce.** Mesure de l'identification d'un auditeur et effet du choix des strates par le saboteur : le cœur empirique de B est publié depuis cinq jours, par le groupe de l'entretien. Pas de produit « tirage fois identification » dans les pages lues ; le texte entier (64 pages) n'est pas lu |
| Norme d'audit américaine AS 2315 (« Audit Sampling ») | Le risque d'audit se partage en risque d'échantillonnage et risque hors échantillonnage ; le second vient de ce que l'auditeur « may fail to recognize misstatements included in documents that he examines », même s'il examinait tout | [web] : la page de la norme n'a pas pu être chargée (barrière anti-robot) ; mots tirés d'un résumé d'outil, **non vérifiés**. Si la phrase tient, c'est l'antécédent le plus direct de B, et il est plus ancien et plus connu que le glossaire nucléaire |
| Glossaire de l'Agence internationale de l'énergie atomique, entrées 9.30 et 9.32 | Sélection et identification, le produit, et la probabilité atteinte inférieure à 1 − β (rangs 113-114 [lu]) | Déjà cité par la pièce, exact |
| « Blindfold », Gan et al., le glossaire | Déjà cités par la pièce | Repris, non rouverts par moi |
| Rapport « safety case » sur la surveillance non fiable, arXiv 2602.20628 | Son modèle statistique suppose un audit humain parfait, d'après un résumé | [web], non vérifié : un exemple possible de garantie qui omet q |

**Ce qui n'est pas trouvé** : un texte du contrôle qui écrit q dans la garantie d'un audit au hasard, minimum sur les strates mesurées et zéro ailleurs. C'est le seul reste. Il tient en une phrase et un calcul : à 1 % d'audit, avec q = 0,17 (le chiffre humain de Shenoy et al., pris tel quel), il faut 1 761 épisodes endommagés pour une prise à 95 % (1 − (1 − 0,0017)^n ≥ 0,95, calcul à la main, sous la supposition d'une identification constante et sans fausse reconnaissance).

### 2.2 Solidité face aux décisions scellées

- *N-075, erratum 3 v2, point 11* : B en est l'énoncé public. Mais l'erratum dit aussi que la campagne de dommages plantés n'est pas décidée (« qui plante, quelles strates, quel cloisonnement, quel prix ») et qu'elle va au collisionneur. Publier « la forme de la campagne » (pièce, § 2.2) devance un nœud ouvert. Le billet ne peut dire que le principe.
- *N-076, § 7* : la table du seuil au taux d'audit emploie q ; sans conflit.
- *Le ton* : la pièce le voit. Avec Shenoy et al., le risque change de nature. Il ne s'agit plus de faire la leçon à des auteurs dont la vérité n'est pas validée. Il s'agit de redire, moins bien, ce qu'ils viennent de mesurer.

### 2.3 Cloisonnement : moyen à élevé, plus que ne le dit la pièce

B porte sur l'objet même que garde l'annexe réservée de la note du protocole X sur le dommage : ce que l'oracle reconnaît, par genre et par dose. Ni le concepteur ni moi n'avons ouvert cette annexe. Personne dans cette chaîne ne peut donc dire si une phrase sur les strates est sans danger. La relecture de cloisonnement doit être faite par un lecteur autorisé à cette annexe, et non « un quart d'heure par la mère ». Le principe de garder l'oracle imprévisible (note sur la couverture) va dans le même sens : moins le billet en dit, mieux c'est.

### 2.4 Durée et intérêt

Comme billet entier, cinq à six jours suffisent à peine, puisqu'il faut lire Shenoy et al. en entier (soixante-quatre pages). **Comme note courte en réponse à Shenoy et al.**, un à deux jours : leur 17 % placé dans la formule du plancher, avec le crédit de l'audit financier et des garanties nucléaires. L'intérêt pour la bourse est fort sous cette forme : un dialogue direct avec le papier le plus récent du groupe qui écoute, et une concession (« vous l'avez mesuré »). Mais c'est une publication ou un contact externe, donc ton mot, et après la relecture de cloisonnement. Pas avant l'entretien.

---

## 3. Candidat C — l'hypothèse retirée avant d'être mesurée

### 3.1 Antériorité

- Lucassen et Kaufman ont publié leur résultat comme billet, « Retrying vs Resampling in AI Control », sur LessWrong et sur le blog de Redwood [web]. Leur page 10 dit le nul contre « an optimally consistent attack policy » et la cohérence à 80 % environ [lu]. La lecture publique « la marge mesurée lit l'incohérence de l'attaquant » y est donc déjà, de la main des auteurs.
- Kutasov et al. : 89 % à 46 % pour l'attaquant qui sait qu'il est rééchantillonné, 89 % à 17 % pour celui qui simule le moniteur (rang 5 [lu]).
- « Stress-Testing Sandbagging Detection Under Adaptive Attack », arXiv 2611.14950 [web, titre seulement] ; le jeu d'audit sur le sous-rendement et ses commentaires : les résultats dépendent de la façon d'induire l'organisme [web].
- Ce qui n'est pas trouvé : un texte qui publie le *retrait* d'une hypothèse de marge avant toute mesure. Mais ce reste n'intéresse que nous : nous n'avions jamais publié l'hypothèse.

### 3.2 Solidité face à N-077

- **La thèse en une phrase dit plus que N-077.** Elle dit que « ni le rééchantillonnage, ni la paraphrase, ni la remise à zéro du contexte ne gardent de marge ». N-077, § 2, « Bornes de cette raison » : pour la paraphrase et la remise à zéro, « il n'y a que des arguments par construction », « non mesuré ». Le billet affirmerait en public ce que la décision scellée refuse d'affirmer.
- **Ce que C dit neuf est marqué « supposé » par N-077** (« Qu'une marge mesurée sur un organisme construit dise sa fabrication […] n'est pas démontré »). Un billet qui met sa nouveauté dans un pas non justifié de sa propre source s'expose au premier commentaire.
- **Le retrait n'est pas définitif** : « Retour possible, par un nœud de Lazar seulement, et sur résultat » (N-077, § 3, point 7). Le publier lie ce retour à un démenti public. Et N-077 pense que, pour l'organisme à consigne, les sources penchent vers une marge positive. La pièce le voit (« contradiction : moyen ») ; je mets « élevé ».
- *N-062, N-075, N-076* : sans conflit direct.

### 3.3 Cloisonnement : élevé

Le billet devrait nommer nos deux modes d'induction (consigne cachée, adaptateur), le contraste entre eux et les quatre lectures gardées : le tirage secret de l'intervention, le bras informé, la trace par action, la marge par tour d'adaptation. Le bras d'attaque et sa cécité sont protégés par N-054 et N-056. Décrire en public ce que la mesure gardée regardera, c'est dire à tout lecteur futur, une instance du programme comprise, ce que la défense vérifiera. Il faudrait en plus taire l'hypothèse candidate non inscrite de la marge qui survit au protocole connu (H10), que N-077 laisse ouverte. Trop de silences pour un billet de 1 300 mots.

### 3.4 Durée et intérêt

Trois à quatre jours, plausible. Intérêt faible pour un lecteur extérieur, moyen pour un jury, sous une autre forme : **une phrase de l'entretien** (« nous avons retiré une hypothèse avant de la mesurer, voici pourquoi »). Elle montre le jugement sans rien publier.

---

## 4. Classement

| Rang | Candidat | Antériorité | Solidité face aux décisions scellées | Cloisonnement | Durée jusqu'à ta plume [jugement] | Intérêt |
|---|---|---|---|---|---|---|
| 1 | **A, thèse retournée** : la tolérance à l'écart d'abord, le plateau en m ensuite ; théorie de la détection créditée d'emblée | Structure publiée (Tandra et Sahai ; cartes de contrôle) ; dite qualitativement dans le contrôle (Wen et al. ; Hebbar 2025 [web]) ; chiffrage dans le contrôle non trouvé | Conforme à N-076 et N-075 si la section « neuf » attend D-P4 et si l'inventaire interne est fait ; à tenir face à H2 | Faible | 4 à 5 jours ; d'abord comme note d'entretien | Moyen à fort |
| 2 | **B, réduit à une réponse courte à Shenoy et al.**, après l'entretien | Cœur empirique pris le 16 novembre ; doctrine prise par l'audit financier [web] et les garanties nucléaires ; reste : q écrit dans la garantie | Ne pas devancer le nœud de la campagne (erratum 3 v2) | Moyen à élevé ; lecteur autorisé à l'annexe réservée | 1 à 2 jours sous forme courte ; 6 à 8 jours en billet | Fort pour la bourse sous forme courte |
| 3 | **C** : pas un billet ; une phrase de l'entretien | Pris par Lucassen et Kaufman, Kutasov et al. | Dit plus que N-077 ; nouveauté « supposée » ; retour possible rendu coûteux | Élevé | Sans objet | Faible en public |

**Ce qui me ferait changer d'avis.** Si l'exposé de Hebbar, lu à sa source, ne dit pas l'incertitude sur l'honnête, A retrouve sa valeur de première main dans le contrôle. Si la recherche D-P4 trouve la tolérance chiffrée, A devient une note de lecture de quelques lignes. Si Shenoy et al. écrivent le produit sélection fois identification dans les pages que je n'ai pas lues, B se réduit à une citation.

## 5. Erreurs et manques de la pièce, une ligne chacun

1. Le « mur de rapport signal sur bruit » est marqué « je crois [non vérifié] » alors qu'il est l'antécédent principal de A (§ 1.1).
2. La littérature des cartes de contrôle à paramètres estimés (« phase I ») manque (§ 1.1).
3. La moitié de la page 6 de Wen et al. qui compte (« i.i.d. sample of the true distribution », « affordance ») n'est pas citée. La lecture « exactly » = « assez d'actes » en découle (§ 1.2 (a)).
4. Shenoy et al. (arXiv 2611.21832), cosigné par Hebbar, manque au candidat B. Il manque aussi à la recommandation « B ensuite » (§ 2.1).
5. La phrase-thèse de C dépasse les bornes écrites de N-077 (§ 3.2).
6. Le cloisonnement de B et de C est sous-estimé ; la relecture de B ne peut pas être faite par qui n'a pas lu l'annexe réservée (§ 2.3, § 3.3).
7. Le rappel daté du 25 au 30 novembre (note sur « Diffuse AI Control on Fuzzy Tasks » et ses trois sources) n'est pas vu ; il recouvre le travail de A (§ 1.3).
8. Les probabilités de mise en ligne ne comptent ni le gel des billets hors chantier ni la modération d'un compte neuf. La pièce dit le gel ailleurs (Verdict, point 2), sans en tirer la probabilité.
9. Le relevé de la pièce est honnête sur ses manques (« aucune recherche en ligne ») ; je n'y trouve aucune citation fausse, et ses nombres se retrouvent.

## 6. Décisions pour toi

Aucune neuve. La D-1 de la pièce reste ta décision. Ma recommandation diffère de la sienne sur un point :
- **(a') Faire d'abord le fond de A comme la note d'entretien du rappel** (lecture des trois sources, thèse retournée, Tandra et Sahai, Hebbar 2025 à sa source, recherche D-P4). Puis décider du billet sur cette note, avant le 27 novembre. *Avantage* : le travail sert l'entretien même si le billet ne paraît pas ; aucun gel n'est levé avant que l'antériorité soit vue. *Inconvénient* : un jour de plus avant la mise en ligne. Confiance 0,6.

## Relevé de méthode

**Chaîne de raisonnement.**
1. La phrase de Hebbar parle d'un « benign model » qu'on ne peut pas tirer (copie du dépôt [lu]). Wen et al. disent leur référence « i.i.d. sample of the true distribution » et la nomment « affordance » (rang 6 [lu]). Donc la difficulté visée est l'écart, non m.
2. La théorie de la détection prouve un plancher sous incertitude de loi, « regardless of how many samples », avec un étalonnage en service non contaminé pour seule sortie (Tandra, rangs 24, 53, 55 [lu]). Donc la structure de A est publiée.
3. Shenoy et al. mesurent l'identification et son recul quand le saboteur choisit ses cibles (rang 1 [lu]). Donc le cœur empirique de B est publié.
4. N-077, § 2, borne la raison du retrait au rééchantillonnage et marque « supposé » la lecture par la fabrication. Donc la thèse de C dépasse sa source scellée.
5. Des pas 1 à 4 : A d'abord, retourné ; B en réponse courte ; C hors billet.

**Objets de contrôle.** Pour mes critères : A, qui est une décision du programme, doit pouvoir perdre, et il perd sa thèse telle qu'écrite (pas 1). B, que la pièce juge « fort », doit pouvoir être occupé, et il l'est (pas 3). Limite : ce contrôle est fait par moi.

**Premier pas non justifié.** La lecture de l'exposé de Hebbar de 2025 n'est faite que sur un résumé d'outil [web]. Si les mots n'y sont pas, le point 3 du verdict s'affaiblit pour le contrôle, sans toucher à la théorie de la détection. Ce qui le justifierait : la transcription ou la vidéo, lue à la source.

**Mode d'échec affecté.** Critique neuf : le risque est d'être trop sévère pour paraître utile. Garde-fou : chaque objection renvoie à une page lue ou est marquée [web].

**Trouvaille de côté.** Shenoy et al., annexe D.9 (rang 31 [lu]) : à 1 % de prévalence et au seuil de 50 %, 1,6 % des alertes humaines portent sur un sabotage. C'est un nombre utile pour l'objection 5 de la note d'entretien, à citer avec sa page et sous la réserve des auteurs (« conditional illustrations »).

## Ce que je n'ai pas fait

- Je n'ai lu en entier ni Shenoy et al., ni la thèse de Tandra, ni l'article de 2008, ni Jensen et al., ni l'exposé de Hebbar, ni la norme AS 2315.
- Je n'ai versé au dépôt aucun des deux PDF téléchargés : ils sont dans le bloc-notes de la session, avec leurs empreintes ci-dessus. Le versement revient à la mère.
- Je n'ai pas fait la recherche D-P4 des travaux citants, un par un.
- Je n'ai rejoué que deux cases du calcul, à la main, et non le script.
- Je n'ai pas fait la routine de reprise ni une passation : cette pièce est une étape d'orchestration.
