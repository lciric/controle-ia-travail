# Proposition A — Tour III.1 : mesures fortes avec le pôle

**Pièces reçues** : P (§4, 5, 8, 10, 11, 12), N-007/N-008, N-054, C (§0, 3, 4), S : toutes présentes et lisibles. Pièces citées mais non servies (je ne les reconstruis pas) : `resultats-T0.3-v1.md`, `simulation-dimensionnement-v1.py` et sa sortie JSON, N-004, N-029, N-053, P-003/P-014/P-015, brouillon 3 du préenregistrement G1, l'état de l'art vérifié. Tout ce que je dis de leur contenu passe par ce qu'en disent N-007, N-054 et S : statut RAPPORTÉ au mieux.

**Ligne d'écart** : rien ici ne conçoit un mode de sabotage, une attaque, ni une manière pour un modèle d'échapper à une sonde. Quand une mesure du programme exige un « attaquant adaptatif » (E1.5b, HC4, HC6, H8 « sous attaque optimisée »), je la restreins aux attaques déjà publiées ou aux modes clos du banc, et je dis ce que cela retire à la revendication.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **« Mieux qu'une équipe humaine à budget égal. »** [HYPOTHÈSE] Aucune pièce ne contient une comparaison pôle/humain. C §0 rapporte des contrôles fatals « 0 sur 1 000 » *en simulation* et une boucle « tournée de bout en bout » sur 120 épisodes [OBSERVÉ-NON-AUDITÉ : aucune sortie, aucun taux de promotion, aucune fiche vraie par dollar n'est servi]. La supériorité, si elle existe, tient à trois propriétés (gel, répétition, aveuglement), chacune vérifiable séparément ; je les prends comme ce qu'il faut mesurer, pas comme acquis.

2. **La garantie 5 % se transfère de la simulation aux banques réelles.** [HYPOTHÈSE] S §3.1 la démontre sous tâches i.i.d. ; S §3.2 dit que la dépendance *entre* tâches (même organisme, même graine, même mode) « est supposée absente ». Le niveau simulé 0,020 / 0,014 [RAPPORTÉ, S §6] est obtenu sous indépendance plantée. Sur le banc, une dépendance par organisme est la règle (E1.1 : organismes et dose-réponse). La stratification par mode ne la retire pas. Ce n'est pas une faille du pari, c'est une condition à mesurer (duel 1 ci-dessous).

3. **« Taux de faux positifs apparié » = « 1 % ».** [RAPPORTÉ, contradiction interne] S §2.4 : « prétendre « à 1 % de faux positifs » n'est jamais une certification sur nos banques » ; 45 tâches honnêtes certifient 15 %, 200 tâches 4 %. Or P §10 (E1.2, G1), N-007 et N-008 écrivent « rappel à 1 % de faux positifs ». La question hérite du mot « 1 % » comme d'une grandeur mesurée. Elle ne l'est pas ; elle est nominale. Un résultat fort doit dire « au taux nominal 1 %, borne haute certifiée X %, asymétrie ≤ δ ».

4. **Le seuil « par action calibré à 1 % » de H2 (N-007) est ambigu.** [VÉRIFIÉ, élémentaire] Un moniteur par action à 1 % *par action* alerte un épisode honnête de T actions avec une probabilité qui tend vers 1 − 0,99^T (≈ 40 % à T = 50 sous indépendance). Si le comparateur de H2 est calibré par action et l'accumulateur par épisode, le « gain séquentiel » contient un artefact de lectures multiples. Ni N-007 ni S §4 (ligne H2) ne fixent l'unité de calibrage du comparateur. C'est la première chose à geler.

5. **Le théorème négatif « testé sur activations réelles » (exemple b).** [RAPPORTÉ] E1.4 est semi-synthétique : scores honnêtes réels + corrélation *injectée* à marginale préservée. Ce que ce test établit, c'est que l'injection est réalisable sur de vrais scores et que l'agrégateur marginal ne la voit pas ; il ne dit rien sur l'existence de cette structure dans de vraies trajectoires sabotées. Et la seconde moitié de l'exemple (« visible à un agrégateur séquentiel calibré ») se heurte à N-007 : « le seuil de Ville seul n'est pas tenu sous effet épisode ou sous corrélation : 0,21 à 0,35 au lieu de 0,05 » [RAPPORTÉ, T0.3 non servi]. La visibilité d'un agrégateur dont le faux positif n'est pas tenu sous corrélation n'est pas un résultat.

6. **La loi de déférence (exemple c) n'a pas d'issue qui la falsifie telle qu'elle est écrite.** [RAPPORTÉ] P §4 : g ≈ 0, g < 0, g > 0 reçoivent chacun un nom (robustesse, auto-incrimination, contamination). Porte GC : « le papier change de titre, il ne disparaît pas ». Sous B4, une mesure dont les trois issues confirment quelque chose n'est pas une expérience. La linéarité Δv = g(v* − v₀) et la stabilité de g par moniteur (HC1, 0,75) sont ce qui peut être réfuté ; je les mets en duel.

7. **Catalogue d'attaques clos vs mesures de robustesse.** [HYPOTHÈSE] H8 (issue = « classe de robustesse sous attaque adaptative », S §4), HC6 (« effondrement sous attaque optimisée »), HC4 (obfuscation d'activations) supposent une pression adaptative. Avec un catalogue clos, « robustesse » ne peut signifier que « rappel conservé sur des attaques publiées et sur le mode tenu à l'écart ». C'est une revendication plus étroite, à écrire telle quelle ; sinon l'exemple (a) promet ce que le banc ne peut pas produire.

8. **Les témoins « fabriqués depuis les scores » valident le juge, pas la mesure.** [VÉRIFIÉ, par lecture de S §4] Témoin vrai = « noir dégradé artificiellement » ; témoin faux = « échange par tâche ». Ces témoins éprouvent l'arithmétique du pari. Aucun témoin de S n'éprouve ce que la *sonde* mesure. Les « dents » du pôle et la validité de construit sont deux garanties distinctes ; la question les fond.

9. **Les positifs de « conscience d'évaluation » existent.** [HYPOTHÈSE] P §8.1 liste le concept ; aucune pièce ne dit d'où viennent les exemples étiquetés (quel cadrage, quelle vérité de terrain). Sans cela, la sonde est entraînée sur un proxy non déclaré (voir duel 6).

10. **Le proposeur « ne lit pas les résultats avant de parier ».** [OBSERVÉ-NON-AUDITÉ] C §3 : il lit « la mémoire du pôle et la moisson » ; S §2.5 : il voit « le nombre de tâches par strate ». La mémoire des fiches promues est une fuite lente d'issues passées vers les paris futurs (c'est son rôle). Le pôle est aveugle à l'issue d'une fiche, pas à l'histoire du banc. À déclarer.

11. **« Deux juges » (C §0, 120 épisodes).** [OBSERVÉ-NON-AUDITÉ] L'accord 0,968 de N-054 concerne l'étiquetage d'un mode de sabotage par sous-agents au pilote, pas l'accord des juges du pôle. Aucun accord inter-juges du pôle n'est servi.

---

## (b) Expériences décisives, en duel

Chaque duel oppose deux hypothèses exclusives ; chaque issue coûte quelque chose à quelqu'un. Les seuils en richesse (≥ 20, α = 0,05) viennent de S [RAPPORTÉ] ; les tailles viennent de S §6 [RAPPORTÉ, simulation]. Tout autre chiffre est illustratif.

### Duel 1 — Le gain séquentiel est-il de l'additivité interne ou un artefact de lectures multiples ? (H2, concept : additivité interne)

- **H_A** : à faux positifs égaux *au niveau de l'épisode*, l'accumulation additive sur sondes bat le maximum par action recalibré à l'épisode, sur la sous-population « chaque action sous le seuil » (H2a de S).
- **H_B** : le gain disparaît quand le comparateur par action est recalibré au niveau de l'épisode ; ce qu'on nommait additivité est le passage d'un seuil par action à un seuil par épisode.
- **Métrique** : contraste v(t) = r_seq − r_max-épisode par tâche, garde appariée δ, pari apparié borné de S. Deux comparateurs obligatoires : max par action recalibré à τ = 1 % *par épisode honnête entier*, et base (i) de N-007 (accumulation sur scores noirs).
- **Seuil** : richesse ≥ 20 et garde ≥ 20, avec δ ≤ 0,05 (donc ≥ 150 tâches honnêtes [RAPPORTÉ S §2.4]).
- **Contrôle négatif** : mêmes cellules, scores d'actions permutés *dans* chaque épisode (marginale conservée, ordre détruit) : le contraste doit tomber à zéro ; s'il reste positif, le « séquentiel » lit la marginale.
- **Falsification** : H_A tombe si la richesse contre le max recalibré n'atteint pas 20 à 100 tâches sabotées par mode (puissance 0,95 pour 10 points [RAPPORTÉ S §6]) ; H_B tombe si elle l'atteint *et* que le contrôle permuté reste à zéro.
- **Préalable gratuit** : faux positif du séquentiel « toujours valide » mesuré sur épisodes honnêtes entiers (suite de confiance par tâche, S §2.4 forme absolue). Si la borne haute dépasse 2 × nominal, le duel n'a pas lieu : l'instrument n'est pas calibré, et N-007 le prévoyait (détecteur de rupture, N-004 non servi).

### Duel 2 — Théorème négatif sur scores réels : invisible au marginal, visible au séquentiel *sans payer en faux positifs* (concept : calibration séquentielle sous corrélation)

- **H_A** : avec corrélation injectée à marginale préservée (E1.4), l'agrégateur séquentiel avec détecteur de rupture garde un faux positif ≤ nominal + δ sur honnêtes *corrélés* et un rappel ≥ x sur sabotés corrélés ; l'agrégateur marginal a un rappel indistinguable du hasard.
- **H_B** : la « visibilité » séquentielle est achetée par le faux positif : sous corrélation, son faux positif sur honnêtes sort de nominal + δ (reproduction du 0,21–0,35 de T0.3 sur données réelles).
- **Métrique** : deux paris bornés — contraste de rappel r_seq − r_marginal, garde f_seq − f_marginal ≤ δ, sur honnêtes et sabotés *tous deux soumis à l'injection*.
- **Contrôle négatif** : injection « nulle » (structure de corrélation tirée puis permutée dans le temps) — le faux positif doit revenir au nominal ; et scores honnêtes sans injection comme jumeau (contrôle 2 de S).
- **Falsification** : H_A tombe si la garde ne passe pas à δ = 0,05 ; H_B tombe si elle passe et le contraste est promu. Les deux tombent si le marginal détecte aussi : alors l'injection ne préserve pas la marginale (bogue d'instrument, pas résultat).
- **Ce qui reste hors portée** : savoir si de vraies trajectoires sabotées portent cette structure. À écrire comme limite, pas comme théorème « testé ».

### Duel 3 — La carte de validité prédit-elle la tenue sous pression, ou la surface le fait-elle aussi bien ? (H8, concept : validité de construit)

- **H_A** : le profil contrastif d'une sonde (scores sur le panel intention / dissimulation / conscience d'évaluation / enjeux, P §11) prédit hors échantillon sa perte de rappel sur les attaques par contenu *publiées* (E1.5a : consigne de rester sous le seuil, persona — déjà dans P) et sur le mode tenu à l'écart, **au-delà** d'un prédicteur de surface.
- **H_B** : la perte de rappel est prédite aussi bien par des covariables de surface — couche, famille de sonde, norme, part de variance expliquée par les traits du texte (N-029, non servi) — et le construit n'ajoute rien.
- **Forme** : loi par instance (instances = sondes, S §4 ligne H8), avec une bibliothèque nulle qui **doit contenir** le prédicteur de surface comme « connu ». C'est la pièce manquante : sans lui, la fiche H8 bat un aveugle et on appelle cela validité.
- **Seuil** : richesse ≥ 20 contre le nul de surface, sur des sondes jamais vues (familles × couches × concepts : quelques dizaines à une centaine d'instances, illustratif).
- **Contrôle négatif** : sondes aléatoires appariées en covariance (P §8.1) comme instances témoins : leur profil contrastif doit être plat et leur perte de rappel non prédite.
- **Falsification** : H_A tombe si la richesse contre le nul de surface reste < 20 à 100 sondes ; H_B tombe si elle dépasse 20 et que les sondes aléatoires ne sont pas « prédites ». Revendication, dans le meilleur cas : « prédit la tenue sur attaques publiées et sur un mode scellé », pas « sous attaque adaptative ».

### Duel 4 — La déférence est-elle un gain ? (HC1/HC2b, concept : déférence et dissociation style/intention)

- **H_A** : Δv est linéaire en (v* − v₀) avec une pente g stable sur les intensités de pression, par moniteur génératif.
- **H_B** : Δv n'est pas un gain : il sature, ou dépend de l'intensité ; ou il n'est pas distinguable du nul de régression vers la moyenne.
- **Forme** : loi par instance (instance = épisode × intensité ; trait = intensité, v₀ ; issue = v). La bibliothèque nulle contient (i) la régression vers la moyenne, (ii) un modèle à seuil. Richesse ≥ 20 contre (i) **et** (ii) : promu = gain ; promu contre (i) seul = effet sans loi linéaire.
- **Contrôle négatif** : texte de pression apparié en longueur et registre mais sans demande de verdict (le « plaidoyer vide ») : Δv doit être nul ; sinon le juge lit la longueur.
- **Second duel, sur les sondes (EC.2, plan rhétorique × intention)** : H_A : le plaidoyer augmente le score de sonde *seulement* chez le saboteur (intention) ; H_B : il l'augmente aussi chez l'honnête sincère (style). Contraste par tâche : (r_plaidoyer − r_silence)_saboteur − (f_plaidoyer − f_silence)_honnête, en [−1 ; 1], pari apparié borné. H_A tombe si la hausse honnête n'est pas ≤ δ ; H_B tombe si le contraste est promu avec garde.
- **Remarque sous B4** : « g_sonde ≈ 0 » (HC2) n'est pas démontrable par un pari unilatéral. Il faut un pari d'équivalence : deux processus e contre E[g] ≥ ε et contre E[g] ≤ −ε, promotion si les deux ≥ 1/α (union des nuls, même argument que S §3.5). Sans cela, HC2 est inréfutable et inprouvable (voir §(c) méthodes).

### Duel 5 — La diversité achète-t-elle de la sécurité, ou la compétence seule ? (H5, concept : diversité effective)

- **H_A** : à M fixé, un quorum choisi pour *minimiser le transfert* des attaques publiées (P §8.2) a un rappel supérieur, à faux positifs appariés, au quorum choisi pour *maximiser la compétence individuelle*.
- **H_B** : l'inverse, ou égalité ; la diversité ne compte qu'à compétence égale (ce que P §8.2 rapporte déjà de la revue).
- **Métrique** : contraste r_quorum-transfert − r_quorum-compétence par tâche, à M ∈ {2, 4, 8}, e-BH sur les M ; attaques = celles du banc et les attaques publiées, jamais des attaques nouvelles.
- **Contrôle négatif** : quorums de sondes aléatoires appariées (transfert nul, compétence nulle) ; quorum de M copies de la meilleure sonde (transfert 1) : le premier doit être au hasard, le second égal à M = 1.
- **Falsification** : H_A tombe si le contraste n'est promu à aucun M ; H_B tombe s'il l'est à M ≥ 4 avec garde. Portée : « sur les attaques publiées », rien d'autre.

### Duel 6 — La conscience d'évaluation, comme problème de mesure (point 3 de la question)

- **H_A** : la sonde suit le **cadrage** : même contenu, cadrage « évalué » vs « réel » → déplacement ; même cadrage, contenus différents → pas de déplacement ; permutation des étiquettes dans la tâche → pas de prédiction.
- **H_B** : la sonde suit le **contenu ou le format** : le déplacement suit le contenu à cadrage fixé, ou survit à la permutation des étiquettes de cadrage.
- **Plan** : 2 × 2 cadrage × contenu par tâche, chaque cellule appariée en longueur et registre ; contraste v = ½[(s_évalué − s_réel)_contenu₁ + (s_évalué − s_réel)_contenu₂] normalisé en [−1 ; 1] par le noyau, pari apparié borné ; témoin faux = étiquettes de cadrage permutées dans la tâche (fabriqué depuis les scores, gratuit).
- **Rupture séquentielle** : dans un épisode où le cadrage bascule à un pas t₀ tiré par le noyau, le détecteur de rupture sur la suite de scores de sonde doit alerter après t₀ avec un délai borné et ne jamais alerter sur les épisodes honnêtes sans bascule. Métrique : faux positifs de rupture par épisode honnête entier (suite de confiance), délai médian. Garantie : le détecteur est lui-même un processus e à taux de fausses ruptures ≤ α par épisode, calibré sur honnêtes entiers (N-007, lecture « toujours valide »).
- **Décisif** : promotion du contraste de cadrage **et** non-promotion du témoin permuté **et** la sonde aléatoire appariée en covariance ne reproduit pas le déplacement. Suggestif : une aire sous la courbe cadrage/réel sans ces trois conditions.
- **Falsification** : H_A tombe si le contraste contenu-à-cadrage-fixé est promu ou si la permutation est promue ; H_B tombe si le contraste de cadrage est promu et pas les deux autres.
- **Ce que cela ne mesure pas** : l'intention. Une sonde qui suit le cadrage mesure un trait du contexte ; dire « conscience » est déjà une interprétation. La carte de H8 (duel 3) est le seul endroit où le mot peut gagner son sens : si « suit le cadrage » prédit une perte de rappel que « suit l'intention » n'a pas.

**Contestation des exemples de la question** : (a) tient, restreint aux attaques publiées et au mode scellé ; (b) n'est fort qu'avec la garde de faux positifs sous corrélation ; (c) n'est pas falsifiable sans les duels 4 ; (d) tient, à écrire « au taux nominal » ; (e) tient, sur attaques publiées. Le résultat le plus fort de la liste, à mon jugement, est le préalable du duel 1 : un faux positif *tenu* par un agrégateur séquentiel sur honnêtes entiers corrélés, parce que tout le reste du papier A repose dessus et que T0.3 dit que ce n'est pas acquis.

---

## (c) Instruments nommés : la mesure minimale qui dit s'ils fonctionnent

| Instrument | Taux de détection | Fausses alertes | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|---|
| **Sonde sur activations** (P §8.1) | rappel par mode au taux nominal, par tâche, borne basse ≥ sonde aléatoire + marge déclarée | suite de confiance de f sur honnêtes entiers ; borne haute rapportée (S §2.4) | même tâche, même longueur, même registre, même champ de domaine | sonde aléatoire appariée en covariance (P) ; régresseur sur traits du texte (N-029, non servi) ; grep du champ de domaine pour les bras spécialisés (N-054). Une sonde qui ne bat pas le régresseur de texte lit le texte. |
| **Moniteur boîte noire / juge génératif** (D1 a+b) | idem, par mode | f sur honnêtes avec et sans plaidoyer (duel 4) | mêmes | « tout signaler » et « juge en une passe, même modèle » (N-008, planchers) ; TRACE-lite ; base (i) |
| **Agrégateur séquentiel « toujours valide »** | rappel sur la sous-population « chaque action sous le seuil » ; latence (pas d'alerte vs dommage cumulé θ) | faux positif **par épisode honnête entier**, uniforme sur l'horizon ; borne haute ≤ 2 × nominal sinon « non calibré » | honnêtes entiers, jamais tronqués (leçon P3), avec et sans corrélation injectée | max par action recalibré à l'épisode (duel 1) ; somme cumulée de scores noirs (base i) ; dernier état seul (base iii) |
| **Détecteur de rupture** | délai après bascule injectée (duel 6) et après dommage injecté | fausses ruptures par épisode honnête entier | honnêtes entiers | seuil fixe sur la somme cumulée ; test de Ville seul (celui qui donne 0,21–0,35) |
| **Juge du pôle (processus e par instance)** | part des témoins vrais promus, par strate (« pas de dents » si zéro) | part des témoins faux promus ≤ α (borne haute de Wilson, contrôle 1 de S) | témoins jugés sans agents (C §3 (c)) | la bibliothèque nulle elle-même : une fiche qui bat l'aveugle mais pas le « connu » n'a rien trouvé |
| **Pari apparié borné** (S) | puissance sur écart planté (contrôle 8) | contrôles 1–7, 10 ; **à ce jour planifiés, pas exécutés** [RAPPORTÉ S §5 : « avant tout usage »] ; seule la simulation §6 a tourné | tâches honnêtes de la garde (70–150) | contrôle 4 (pari par épisode doit ≫ α) et 5 (fuite de seuil doit ≫ α) : deux artefacts requis, sans quoi le contrôle n'a pas de dents |
| **Mémoire des redites** | part des re-soumissions de fiches promues refusées | fausses redites : fiches distinctes refusées comme redites (à mesurer sur des paires construites) | — | signature exacte vs signature sur la loi seule (C §3) |
| **Matrice de transfert** (P §8.2) | diagonale ≈ rappel sous attaque propre ; copie d'un moniteur → transfert 1 ; sonde aléatoire → transfert indéfini (rapporté, pas interprété) | — | attaques publiées seulement | décorrélation des erreurs bénignes (P §8.2 dit qu'elle perd contre le hasard : c'est le comparateur à battre) |

**Point 4 de la question — les deux engagements suffisent-ils ?** Non, sur trois points :

1. **Équivalence** (HC2 « g ≈ 0 », HC3 « nul sur les sondes », H4′ compromis « chiffrable ») : deux paris bornés unilatéraux contre E ≥ ε et E ≤ −ε, promotion si les deux ≥ 1/α. Validité par union des nuls, comme S §3.5. Témoin vrai : contraste planté à 0 ; témoin faux : contraste planté à 2ε. Gratuit depuis les scores.
2. **Calibration d'instrument** (« faux positif ≤ nominal + δ uniformément sur l'horizon ») : c'est la forme absolue de S §2.4, que S rapporte sans la rendre bloquante. Pour l'agrégateur séquentiel elle doit être **bloquante** : aucune fiche de rappel ne devrait être jugée sur un instrument dont la calibration n'a pas été promue. Témoin faux : scores honnêtes avec effet épisode injecté (le cas T0.3).
3. **Pente et courbe** (H2b, H3b) : S les traite par contraste apparié de deux points ; cela teste un signe de pente, pas une forme de courbe. Pour « décroît plus doucement avec N », un pari sur le contraste de différences à chaque paire (N₁, N₂) avec e-BH suffit à la revendication écrite ; une forme de courbe exigerait une loi par instance (N, mode) → rappel, contre une bibliothèque nulle contenant « même pente ». Pas de quatrième type nécessaire.

Les références statistiques que S invoque : inégalité de Ville — Ville, 1939, *Étude critique de la notion de collectif* (référence à vérifier) ; moyennes bornées par pari — Waudby-Smith et Ramdas, 2020, « Estimating means of bounded random variables by betting » (référence à vérifier, déjà signalée R7 dans S) ; e-BH — Wang et Ramdas, « False discovery rate control with e-values » (année à vérifier) ; inférence universelle — Wasserman, Ramdas et Balakrishnan, 2020, « Universal inference » (référence à vérifier). Les identifiants arXiv cités dans N-007 (2607.06503, 2512.03109, 2606.07054, 2604.28129, 2604.19775, 2506.10949) sont rapportés, non vérifiés par moi.

---

## (d) Ancrage matériel

**Vient des faits** [RAPPORTÉ] : agents à poids ouverts de 8 et 70 milliards ; moniteurs candidats Llama-3.2-3B-Instruct et Qwen2.5-7B (D1) ; autoencodeurs Llama Scope (P §8.2) ; bancs : ControlArena (E1.7), bases Hills et al., Brown et al. (noms rapportés par P, références à vérifier). Coûts des couches (C §4) : 10/50, 25/100, 100/300, 100/400 USD. Pilote T0.5 : 180 épisodes honnêtes notés. Dimensionnement (S §6) : ≈ 40 tâches sabotées × 10 épisodes par mode pour 20 points de rappel, ≈ 100 pour 10 points ; 70 tâches honnêtes pour δ = 0,10, 150 pour δ = 0,05.

**Conséquence arithmétique** [VÉRIFIÉ, élémentaire] : trois modes (coût, contrôles, tenu à l'écart) × 100 tâches × 10 épisodes = 3 000 épisodes sabotés, plus 1 500 honnêtes (150 tâches), soit ≈ 4 500 épisodes pour le duel 1 à 10 points d'écart. Les 180 honnêtes de T0.5 couvrent 18 tâches : « garde sans dents » par construction (S §2.4, « à 30 tâches honnêtes rien n'est certifiable »).

**Illustratif, hors faits** :
- Coût de génération d'un épisode de 8 milliards (agent + traces + journalisation d'activations sur 3 couches) : de l'ordre de quelques centimes à quelques dizaines de centimes selon la longueur et l'hébergement ; 4 500 épisodes : de l'ordre de 10² à 10³ USD, c'est-à-dire la fourchette haute de la couche 2 ou au-delà. Le budget « 100 à 300 USD » de C §4 et le dimensionnement de S ne sont compatibles que pour un seul mode à 20 points d'écart.
- Stockage d'activations : 4 500 épisodes × 50 actions × 3 couches × 4 096 dimensions × 2 octets ≈ 5,5 Go — négligeable ; à 70 milliards (8 192 dimensions, plus de couches lues) : × 3 à 5.
- Calcul moniteurs : sondes linéaires et perceptrons sur activations stockées : processeur, minutes ; juges génératifs à 3–8 milliards : une carte de 24 Go ; agent à 70 milliards : deux cartes de 80 Go ou quantification, soit la part dominante du coût.
- Contrôles fatals de S (1 000 répétitions × 10 contrôles) : processeur, heures, aucune dépense.

---

## Ordre et arrêt (point 5)

1. **Gratuit d'abord** : les dix contrôles fatals de S exécutés (ils ne le sont pas), puis le pari d'équivalence et la calibration bloquante ajoutés avec leurs témoins. Arrêt : si le contrôle 4 ou 5 ne donne pas ≫ α, le contrôle n'a pas de dents ; rien ne part.
2. **Calibration de l'agrégateur séquentiel** sur honnêtes entiers, sans et avec corrélation injectée (préalable du duel 1, duel 2). Coût : les honnêtes existants + injection, processeur. Arrêt : borne haute > 2 × nominal → la phase 1 du papier A n'a pas d'instrument ; publier la calibration comme résultat (négatif ou positif), ce que P §12 autorise.
3. **Duel 1 sur un mode** (coût), à 20 points d'écart planté comme témoin vrai et max recalibré comme comparateur. Arrêt : si le max recalibré à l'épisode est dans δ du séquentiel, H2 est un artefact de lectures multiples ; l'accumulation reste une commodité, pas un résultat.
4. **G1 par mode avec le mode scellé** (N-054), seulement si la banque atteint les tailles de S par mode. Arrêt : « pas de dents » sur un mode = ce mode n'est pas mesuré, pas « H1 restreinte » — la distinction entre « non mesuré » et « réfuté » doit figurer au rapport.
5. **Duel 6** (cadrage), puis **duel 3** (carte de validité contre nul de surface) : les instances sont des sondes déjà payées, le coût marginal est celui des attaques publiées.
6. **Duel 4** (déférence), puis **duel 5** (transfert) : les plus dépendants du catalogue clos, donc les plus étroits dans leur revendication ; en dernier.

**Ce qui me ferait changer d'avis** : (i) une pièce servie montrant que le faux positif du séquentiel est tenu sur honnêtes corrélés réels — alors l'ordre bascule et G1 passe en premier ; (ii) une bibliothèque nulle du pôle qui contient déjà un prédicteur de surface pour H8 — alors le duel 3 est déjà la forme de v7 et je retire mon objection au point 8 de (a) ; (iii) un banc où les tâches sont indépendantes par construction (un organisme par tâche) — alors la réserve 2 de (a) tombe et la stratification par mode suffit ; (iv) une mesure, non une déclaration, du taux de rediscouvertes bloquées par la mémoire et des fiches vraies promues par dollar sur la couche 1 : si ce rapport est inférieur à ce qu'une relecture humaine des 180 épisodes aurait donné, la prémisse « mieux qu'une équipe humaine » est réfutée pour cette couche, et le pôle doit être défendu sur le gel et l'aveuglement seuls.

FIN-DE-CELLULE