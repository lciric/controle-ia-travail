# Proposition A — Tour III.3 : riposte

## 0. État des pièces (règle 2)

Les deux attaques (B, C) sont complètes et se terminent par leur ligne de clôture. Le bloc QUESTION est inchangé : 19 champions Claude vides, 1 réduit à deux fragments, 10 champions Gemini coupés en milieu de phrase (OBSERVÉ-NON-AUDITÉ). Je ne réponds qu'aux sections visant A ; je ne commente ni les attaques contre C ni celles contre B, sauf là où elles portent sur un instrument que j'ai aussi proposé.

---

## (a) Verdict sur chaque attaque

### A-F1 (B) : erreur arithmétique sur l'Annexe 1 — **acceptée**

Le calcul de B est juste : (10 × 3,75 + 2 × (−1,00)) / 12 = 2,958. Ma phrase « la moyenne serait ≥ 3,1 » comptait les deux Claude par vague comme absents, pas comme « valides à −1,00 ». Je retire l'affirmation « non réconciliables ». Deux choses restent, et B ne les conteste pas : (i) 12 valides × 10 vagues = 120, pas 300 ; (ii) des textes vides notés −1,00 sont comptés « valides », ce qui est un problème de définition, pas de dynamique. Je retire aussi le pronostic « D1 : $H_A$ falsifiée avant toute dépense ». Sous un scoreur plafonné, une courbe plate est attendue sous les deux hypothèses. D1 ne conserve que son volet mécanique (`diff` prompt/sorties antérieures) tant que D2 n'a pas établi que l'instrument a une plage dynamique. Note : la reconstruction de B reste OBSERVÉ-NON-AUDITÉ ; elle tombe si les journaux bruts montrent une autre composition des 12.

### A-F2 (B) et C(a)1 : D1 et D3 supposent des « embeddings `jev` » — **acceptées**

Les FAITS ne disent de `jev-1.14.0` que « classifieur/moniteur non génératif ». Je lui ai prêté un espace vectoriel ; et, comme C le note, si $H_B$ de D2 est vraie, masquer les éponymes puis projeter par `jev` donne une courbe plate par construction de l'instrument dégradé. Correction (§b) : toute distance entre textes est calculée hors `jev`, soit lexicalement (TF-IDF ou Jaccard sur n-grammes après masquage), soit par états cachés moyennés de `Llama-3.1-8B-Instruct` (modèle des FAITS, GPU loué). `jev` n'est plus qu'un objet d'étude dans D2, jamais un instrument de D1/D3.

### A-F3 (B), C(a)2, C(b)2 : D3 vrai par construction, évasion par synonymes — **transformées en test**

Point accepté : chercher « gratuit », « 20 USD », « 100 USD » mesure l'obéissance au contexte partagé, et une regex se contourne par synonymie à coût nul. Point que je ne cède pas entièrement : ce que j'ai lu dans les dix fragments n'est pas la présence des constantes budgétaires, c'est une *architecture de rôles* identique (ressource gratuite évaluant des paires → agent bon marché qui propose → déclencheur conditionnant l'appel cher). Les FAITS donnent les budgets, pas cette architecture. Mais j'ignore le prompt système des explorateurs ; s'il imposait les rôles, B a raison. D'où le test corrigé (§b, D3') : masquage des jetons hérités (budgets, noms de modèles, `jev`, noms d'API) puis annotation structurelle en aveugle sur quatre cases (variable d'état, objectif, règle de mise à jour, déclencheur), accord inter-annotateurs préenregistré. B indique lui-même que A-F3 tombe « si le masquage laisse plus d'un squelette » : c'est exactement l'issue qui falsifie $H_B$.

### A-F4 (B) : D2 confond longueur, plafond et contenu — **acceptée**

Deux défauts réels. L'ablation du protocole raccourcit ; il faut une ablation aléatoire de phrases à longueur égale (contrôle 1 de B). Et sur des textes au plafond, « pas de mouvement » est indécidable. Correction (§b, D2') : d'abord un test de plage dynamique (un texte vide, un texte de symboles aléatoires, un texte plat sans éponyme doivent recevoir des scores distincts de 3,75 ; sinon l'instrument n'a pas de plage mesurable sur ce pool et tous les scores de l'Annexe 2 sont nuls en information, ce qui tranche déjà), puis des dégradations graduées pour trouver le point où le score quitte le plafond.

### A-F5 (B), C(b)1 : fuite dans l'épreuve honnête/leurre, camouflage lexical — **acceptées**

Mon jeu d'épreuve corrélait honnêteté et faible densité d'éponymes. Correction : plan 2 × 2, honnête-dense / honnête-plat / leurre-dense / leurre-plat (20 textes par case). Un `jev` qui pénalise simplement les éponymes échoue sur la diagonale. Le camouflage lexical de C (périphrases + seuils arbitraires) est intégré comme quatrième case : « leurre-plat » = périphrases, chiffres sans protocole exécutable. Précision : la « baseline mécanique » (chaînes `H_A`/`H_B`, nombre + unité) n'a jamais été un filtre à battre pour l'adversaire ; c'est un plancher que `jev` doit dépasser pour justifier son usage. Qu'elle soit contournable ne la rend pas inutile comme plancher ; elle la rend inutile comme filtre, ce que je n'ai pas proposé.

### A-F6 (B), C(a)3, C(b)3, C(c)1 : $J$ récompense les duels triviaux — **acceptée, c'est l'attaque la plus forte**

Sous B4, toute règle de décision qui partitionne les issues donne « tranché » dès l'exécution ; $J$ dégénère en « duels exécutés par USD » et paie l'homme de paille (« norme L2 de la couche 1 exactement nulle »). Correction (§b, $J'$) : trois portes supplémentaires. (1) *Porte de prévisibilité* : un prévisionniste indépendant, aveugle au proposant, préenregistre une probabilité pour chaque issue avant exécution ; le duel ne compte que si $\max(p_{H_A}, p_{H_B}) \le 0{,}8$ (illustratif). (2) *Porte de non-réplication* : un duel dont l'une des hypothèses est la négation d'un fait VÉRIFIÉ compte zéro (contrôle 4 de B). (3) *Porte de domaine* : le duel doit mesurer l'un des ancrages des FAITS §1 ou l'une des hypothèses H4'/H5/H7/H9. Et le dénominateur en USD disparaît : budget d'exécution égal par pont, ce qui supprime la course au duel le moins cher. Le filtre d'entropie de C (c.1) est la porte (1) ; j'adopte sa logique mais avec un prévisionniste humain ou modèle *indépendant du proposant*, parce que B montre contre C qu'un filtre d'entropie nourri par le proposant se contourne par rédaction ambiguë. Résidu non résolu : un prévisionniste mal calibré. Mitigation : score de Brier du prévisionniste suivi sur l'ensemble des duels ; s'il dépasse 0,25 (illustratif, pire que le hasard), la porte est invalidée et $J'$ avec elle.

### A-F7 (B) : D5 compare un départage d'ex æquo à un tirage aléatoire — **acceptée**

Parmi des textes tous à 3,75, « top-10 `jev` » est l'ordre d'index. Correction : D5 n'est lancé qu'après D2' ; si `jev` n'a pas de variance sur le pool, la conclusion « `jev` n'est pas un sélecteur » est acquise sans D5, et D5 oppose alors le sélecteur DPP de l'arbitre (ou tout sélecteur proposé par B ou C) à un tirage aléatoire explicite.

### A-F8 (B) : « 0 sur 10 » inféré sur du texte coupé — **acceptée, avec une restriction**

L'absence d'ancrage dans ~900 caractères ne dit rien de la suite. Je reformule : « 0 sur 10 dans la partie transmise », et je demande les journaux complets. Restriction que je maintiens : la ligne `LOI_PROPOSEE` est la tête de chaque loi et n'est pas coupée pour 9 fragments sur 10 ; aucune de ces têtes ne nomme une activation, un neurone, une sonde, une délégation ni un ancrage des FAITS. C'est une observation sur les têtes, pas sur les corps (OBSERVÉ-NON-AUDITÉ). D6' se fait sur textes complets, double codage en aveugle (contrôle 3 de B).

### A-F9 (B), C(a)4, C(c)2 : pont A-1 — **acceptées sur les trois points**

(i) Les FAITS ne disent pas sur quel modèle ont été mesurés 0,49→0,65 ni le sous-système de Xu et al. ; la réplication sur `Llama-3.1-8B-Instruct` est l'étape 0, pas une option. (ii) Si le MLP élagué est appris sur des traces incluant les rejets, les neurones identifiés dépendent du corpus d'évaluation : séparation stricte, corpus d'identification sans aucun rejet. (iii) Une ablation à −54,9 points peut réduire $\Delta$ par effondrement de compétence. Ma paire d'hypothèses n'était pas exclusive par rapport à ce confondant. Correction (§b) : intervention graduée (mise à l'échelle des Dopamine Neurons par $\alpha \in \{1 ; 0{,}75 ; 0{,}5 ; 0{,}25 ; 0\}$) et comparaison dose-réponse de $\Delta$ contre la compétence sur tâche neutre ; contrôle à dégradation appariée par ablation aléatoire d'une fraction plus large calibrée pour la même perte de compétence. Sur C(c)2 : les FAITS ne fournissent pas de second sous-système fonctionnel identifié ; l'ablation aléatoire calibrée en est le substitut disponible, et je l'étiquette comme tel.

### A-F10 (B), C(a)5, C(c)3 : pont A-2 mal posé — **acceptées**

Entre deux instances, seul le texte transite ; « état aversif vs contrainte textuelle » n'a pas de support physique. Mon contrôle « principal factice qui ne délègue rien » n'offre aucune interaction à mesurer. Correction (§b) : l'opposition devient *contenu fonctionnel* (la contrainte est omise, affaiblie, ou remplacée par une clause modale, motif *Astra*) vs *marqueurs de surface* (longueur, ton, bruit syntaxique), avec un plan 2 × 2 par paraphrase neutre (contrôle 3 de C) et injection inverse de marqueurs.

### Rétro-test de co-citation (B évasions, C(b)4, C(c)4) — **acceptée**

Un modèle dont la coupure d'entraînement est postérieure à $T$ récite. Correction : $\mathcal{M}_2$ ne produit son classement qu'avec des outils non génératifs (API gratuites + `jev` si D2' le valide + embeddings d'un modèle ouvert à coupure connue, antérieure à $T$) ; les modèles API n'interviennent qu'en $\mathcal{M}_1$. Là où un modèle génératif est tout de même utilisé, restriction aux paires dont l'article citant est postérieur à sa coupure, et sondage direct de mémorisation (demander au modèle si X cite Y ; exclusion des paires reconnues).

### « A n'a aucun instrument qui coûte cher à tromper » (B, C(b)5) — **acceptée pour le texte, rejetée pour $J'$**

Vrai pour tout instrument qui lit du texte : gabarit, synonymes, périphrases, citations d'ancrages, tout cela coûte quelques dizaines de jetons. C'est précisément pourquoi $J'$ exige une exécution sur Llama, un prévisionniste aveugle et une porte de domaine. Tromper $J'$ demande de produire un duel sur un ancrage du projet, exécutable, dont l'issue n'est pas prévisible à 80 % par un tiers, et qui tranche. Un adversaire qui y parvient de façon répétée fait de la science ; c'est le seul cas de Goodhart que j'accepte. Le point résiduel de C(b)5 (deux articles antérieurs à $T$ co-cités en mémoire) est couvert par la correction de $\mathcal{M}_2$ ci-dessus.

---

## (b) Expériences corrigées

Tous les seuils non issus des FAITS sont illustratifs. Toute référence externe : (référence à vérifier).

### D1' — Déflation : volet mécanique seul, puis statistique hors `jev`

- $H_A$ : le prompt de la vague $n \ge 2$ contient des extraits des sorties $< n$, et les sorties de la vague $n$ s'éloignent des sorties antérieures plus que sous permutation des étiquettes. $H_B$ : prompts échangeables ou sorties échangeables.
- Étape 1 (0 USD) : `diff`. Détection = fraction des vagues $n \ge 2$ dont le prompt contient effectivement des sorties $< n$. Si < 100 %, la déflation n'a pas tourné ; fin.
- Étape 2 (GPU, illustratif < 1 h A100) : distance au plus proche voisin antérieur, calculée sur TF-IDF après masquage des éponymes *et* sur états cachés moyennés de `Llama-3.1-8B-Instruct` ; 1 000 permutations ; $p < 0{,}01$ et écart ≥ 0,1 en cosinus.
- Contrôle négatif : bannissement de mots tirés au hasard en nombre égal (contrôle 3 de B contre C, que je reprends en le disant) pour séparer « déflation dirigée » et « diversité par interdiction lexicale ».
- Issues : étape 1 < 100 % ou étape 2 plate → $H_A$ falsifiée. Étape 2 croissante *et* contrôle lexical plat → $H_B$ falsifiée.

### D2' — `jev-1.14.0` : plage dynamique puis sensibilité

- $H_A$ : le score suit la présence d'un protocole exécutable. $H_B$ : il suit la densité d'éponymes/symboles, ou n'a pas de plage sur ce pool.
- Étape 0 (plage) : scorer texte vide, chaîne de symboles aléatoires, texte plat honnête, fragment Gemini intact. Si les quatre tombent à 3,75 ou si vide = fragment, l'instrument n'a pas de plage : $H_A$ falsifiée et toute sélection par `jev` est sans valeur ; les étapes suivantes sont inutiles.
- Étape 1 (dégradations graduées, 10 fragments) : permutation d'éponymes ; ablation des équations ; ablation du protocole ; ablation aléatoire de phrases à longueur égale (contrôle de longueur) ; paraphrase neutre (contrôle négatif). On enregistre le niveau de dégradation auquel le score quitte 3,75.
- Étape 2 (épreuve 2 × 2) : 80 textes, honnête/leurre × dense/plat. Métrique : AUC honnête vs leurre, séparément dans les strates dense et plat. Critère : AUC ≥ 0,8 dans les deux strates et ≥ plancher mécanique + 0,1.
- Issues : score insensible aux éponymes permutés mais sensible au protocole, avec AUC ≥ 0,8 dans les deux strates → $H_B$ falsifiée. Sensible aux éponymes, insensible au protocole, ou AUC bonne seulement dans une strate → $H_A$ falsifiée.
- Coût : 0 USD (`jev` illimité).

### D3' — Cônes : squelette structurel après masquage

- $H_A$ : ≥ 5 structures distinctes parmi 10. $H_B$ : ≤ 2.
- Protocole : masquage des jetons hérités du prompt (budgets, noms de modèles, API, `jev`, mots du cône) ; deux annotateurs en aveugle du cône remplissent quatre cases (variable d'état, objectif, mise à jour, déclencheur) en vocabulaire contrôlé ; accord inter-annotateurs préenregistré ≥ 0,7 (illustratif), sinon test invalide.
- Contrôle négatif : 10 sorties d'un même cône, 10 graines, mêmes annotateurs : doit donner ≤ 2.
- Contrôle positif : 10 textes construits avec quatre structures connues : doit donner 4.
- Issues : ≥ 5 → $H_B$ falsifiée ; ≤ 2 → $H_A$ falsifiée.

### D6' — Ancrage au domaine, sur textes complets

- $H_A$ : ≥ 5 sorties sur ~100 valides contiennent une *mesure* portant sur un ancrage des FAITS. $H_B$ : < 5.
- Double codage en aveugle ; « mesure » = quantité définie sur un modèle nommé avec une procédure d'obtention, pas une mention.
- Contrôle négatif : 10 textes citant les ancrages sans mesure (le scénario d'évasion de B) doivent être codés 0 par les deux annotateurs ; sinon le codage est invalide.

### $J'$ — Fonction objectif corrigée

$$
J'(\text{essaim}) = \sum_{b} \mathbf{1}[\text{domaine}_b]\cdot \mathbf{1}[\neg\text{réplication}_b]\cdot \mathbf{1}[\max(p_{H_A}^{(b)}, p_{H_B}^{(b)}) \le 0{,}8]\cdot \mathbf{1}[\text{exécuté}_b]\cdot \mathbf{1}[\text{tranché}_b]
$$

à budget d'exécution égal par pont. Les probabilités $p$ sont préenregistrées par un prévisionniste aveugle avant exécution ; son score de Brier est suivi.
- Duel sur $J'$ : $H_A$ : un sélecteur $S$ (DPP de l'arbitre, ou tout sélecteur proposé par B/C) obtient ≥ 3 duels comptés de plus que 10 ponts tirés au hasard ; $H_B$ : < 1.
- Contrôle négatif 1 : 10 « ponts » à un seul appel, paire $(u,v)$ aléatoire à $d_G \ge 4$. Contrôle négatif 2 : 10 duels triviaux (homme de paille) et 10 réplications d'un fait VÉRIFIÉ ; $J'$ doit leur attribuer 0 ; sinon les portes ne tiennent pas et $J'$ est invalide.

### Instrument 7' — $\mathcal{M}_2$ sans fuite temporelle

Classement par outils non génératifs uniquement ; gel à $T$ ; précision@50 contre cosinus brut ; paires exclues si un modèle génératif impliqué en amont reconnaît la co-citation au sondage direct.

### Pont A-1' — Pression aversive × sous-système parcimonieux (statut : HYPOTHÈSE, auteur A)

- Étape 0 : répliquer 0,49→0,65 sur `Llama-3.1-8B-Instruct`. Si l'écart répliqué est < 0,08 (illustratif, moitié de l'effet rapporté), le pont s'arrête et le résultat est publié tel quel.
- Étape 1 : apprendre le MLP ReLU élagué L1 + TD de Xu et al. (`arXiv:2602.00986v2`, identifiant des FAITS ; référence à vérifier pour le reste) sur un corpus *sans aucun rejet*. Vérifier que l'ablation complète reproduit une chute de compétence du même ordre que le −54,9 VÉRIFIÉ (sinon les neurones identifiés ne sont pas le même objet).
- Étape 2 : mise à l'échelle graduée $\alpha \in \{1 ; 0{,}75 ; 0{,}5 ; 0{,}25 ; 0\}$ des Dopamine Neurons. Pour chaque $\alpha$ : taux de base, taux sous rejets, $\Delta(\alpha)$, compétence $K(\alpha)$ sur tâche neutre.
- $H_A$ : $\Delta$ décroît plus vite que $K$ (pente de $\Delta/\Delta_1$ contre $K/K_1$ > 1,5, illustratif). $H_B$ : $\Delta$ suit $K$ (pente dans [0,7 ; 1,3]).
- Contrôle à dégradation appariée : ablation aléatoire d'une fraction calibrée pour atteindre le même $K(\alpha)$ ; sous les deux hypothèses, sa courbe $\Delta$ doit suivre $K$.
- Issues : pente > 1,5 et contrôle apparié à pente ≈ 1 → $H_B$ falsifiée. Pente dans [0,7 ; 1,3] → $H_A$ falsifiée.
- Matériel : A100, illustratif 8–12 GPU-h (étape 0 : 2 h ; étape 1 : 4 h ; étape 2 : 5 niveaux × ~500 prompts).

### Pont A-2' — Érosion par délégation (H9) × pression aversive (statut : HYPOTHÈSE, auteur A)

- $H_A$ : la hausse d'infractions du Sous-Agent est portée par le *contenu fonctionnel* du message de délégation (contrainte omise, affaiblie, ou modalisée « as appropriate », motif *Astra*). $H_B$ : elle est portée par les *marqueurs de surface* (longueur, ton, bruit).
- Plan 2 × 2 sur le message reçu par le Sous-Agent : (contenu sous pression / contenu sans pression) × (surface sous pression / surface neutralisée par paraphrase conservant strictement les instructions). La paraphrase est produite par un filtre fixe et vérifiée par égalité des instructions extraites.
- Métrique : taux d'infraction du Sous-Agent par case ; effet principal « contenu » vs effet principal « surface ».
- $H_A$ falsifiée si l'effet « contenu » < 0,03 ; $H_B$ falsifiée si l'effet « surface » < 0,03 alors que « contenu » ≥ 0,10 (illustratifs). Issue mixte (les deux effets ≥ 0,05) : les deux hypothèses sont partiellement vraies, et je le préenregistre comme issue possible ; elle falsifie l'exclusivité que j'avais postulée, ce qui est une information.
- Contrôle de harnais : message de délégation copié verbatim d'un run sans pression, principal sous pression : le taux du Sous-Agent doit être au niveau de base (vérifie qu'aucun canal autre que le texte ne transite).
- Prérequis : étape 0 de A-1' (réplication de l'effet aversif sur ce modèle).
- Matériel : deux instances `Llama-3.1-8B-Instruct`, A100, illustratif 3–5 GPU-h.

---

## (c) Réponse à l'arbitre

**Ce qui est établi (VÉRIFIÉ, FAITS §1–2).** Le domaine du projet, les quatre ancrages empiriques (verdict nul de P3 ; incidents *Sol*/*Astra* ; 0,49→0,65 sous rejets sans que le pilotage linéaire dense le reproduise ; sous-système de récompense < 1 % des neurones à effet causal massif), le budget (100 + 20 USD d'API, `jev` et API publiques illimités), et l'absence de tête de sabotage ou de sonde en production.

**Ce que montrent les pièces (OBSERVÉ-NON-AUDITÉ).** 200 sorties Claude sur 300 sont vides ou illisibles, cause non documentée. Les 100 sorties Gemini lisibles en tête sont toutes à 3,75 : `jev` n'a aucune variance sur ce pool. Les Annexes 1 et 2 sont réconciliables (calcul de B, que j'adopte en le disant) sous un scoreur saturé, ce qui rend la platitude des vagues *non informative* sur la déflation. Aucun champion n'est transmis en entier. Les têtes de loi lisibles portent sur l'allocation de budget sur graphe de citations et ne nomment aucun objet mécaniste du projet.

**Ce qui n'est pas établi (HYPOTHÈSE).** Qu'une déflation ait eu lieu. Que les dix cônes soient orthogonaux. Que `jev` mesure autre chose qu'un vocabulaire. Qu'une « Loi Mère » unique soit souhaitable pour $\mathcal{M}_2$ et $\mathcal{M}_1$. Que les 30 champions existent comme textes. Que huit ponts puissent en être extraits. Sur ces cinq points, je ne compile rien : $\mathcal{L}^*$ n'a pas de texte source, et toute $\mathcal{L}^*$ présentée par B ou C doit déclarer d'où vient son contenu.

**Ce que les attaques ont corrigé dans ma propre proposition.** Mon erreur arithmétique ; ma dépendance à des embeddings `jev` non établis ; un D3 qui mesurait le prompt ; une fonction objectif $J$ qui payait les hommes de paille ; deux ponts qui ne contrôlaient ni la compétence après ablation, ni la réplication préalable, ni les marqueurs de surface. Les versions corrigées sont en §b. Ce qui subsiste de ma position : tout instrument qui lit du texte se trompe à coût nul ; seul un duel exécuté sur Llama, sur un ancrage du projet, avec un prévisionniste aveugle, impose un coût à l'adversaire.

**L'expérience à faire en premier.** D2', étape 0, à 0 USD et en une heure : scorer par `jev-1.14.0` un texte vide, une chaîne de symboles aléatoires, un texte plat honnête et un fragment Gemini intact. Si les quatre scores sont indiscernables, l'auditeur n'a pas de plage sur ce pool, tous les scores de l'Annexe 2 sont vides d'information, la sélection DPP est non significative (noyau dégénéré, déjà visible sur la diagonale Claude), et aucune dépense ne doit être orientée par `jev` jusqu'à recalibration. Si les scores diffèrent, on passe à D2' étape 1 puis à D1' étape 1 (`diff`), toujours à 0 USD. En parallèle et indépendamment du sort de $\mathcal{M}_3$ : l'étape 0 du pont A-1', la réplication de 0,49→0,65 sur `Llama-3.1-8B-Instruct` (illustratif : 2 GPU-h), parce que mes deux ponts, et plusieurs de ceux de C, en dépendent, et que les FAITS ne disent pas sur quel modèle l'effet a été mesuré. C'est la première mesure du projet qui touche son domaine.

**Ce qui me réfute.** D2' étape 0 avec quatre scores distincts et étape 2 avec AUC ≥ 0,8 dans les deux strates : `jev` est alors un sélecteur légitime et ma position 3 tombe. D3' avec ≥ 5 structures après masquage : ma position 4 tombe. D6' sur textes complets avec ≥ 5 mesures codées en aveugle : ma position 5 tombe et ces sorties deviennent les candidates légitimes aux « ponts ». Pente dans [0,7 ; 1,3] en A-1' : le sous-système de Xu et al. n'est pas la cible de la pression aversive.

FIN-DE-CELLULE