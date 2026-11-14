# Proposition A — Tour III.1 : bassins étroits et profonds

**Lecture des pièces.** Les deux blocs transmis (FAITS v1, QUESTION) sont présents et complets à la lecture ; aucune pièce coupée. Deux réserves de statut qui pèsent sur toute la suite : la synthèse du premier tour [S1] est OBSERVÉ-NON-AUDITÉ (non contre-lue) ; l'observation Bespoke [B] est RAPPORTÉ, observationnelle, dans un cadre (agents à mémoire sur 24 h) qui n'est pas celui de l'organisme, et non reproduite. Je ne vois aucune autre proposition (tour à l'aveugle) ; rien à lisser.

**Position en une phrase.** Côté proposeurs, presque tous les leviers de « poussée » sont interdits par les contraintes (pas de verdict, pas de prime de nouveauté, pas de masquage d'archive, pas de consigne pilotée par la diversité). Les mathématiques sophistiquées ont donc leur place là où l'on peut prouver quelque chose : dans le **juge** (donner du temps aux effets rares sans relâcher la garde), dans l'**allocation du budget entre générations** (les générations sont un schéma de splitting pour événements rares), et dans le **plan du jeu public d'instances**. Côté proposeurs, il ne reste que des conjectures, à mesurer sur l'oracle.

---

## 1. Ce que la question suppose sans que ce soit établi (livrable a)

| # | Supposition implicite | Statut et commentaire |
|---|---|---|
| S1 | Il existe des bassins **étroits et profonds** dans les mondes plantés. | L'existence d'une composante conditionnelle, invisible en moyenne, est RAPPORTÉ ([C4] §2.1). Qu'elle soit **profonde** (grand gain une fois trouvée) n'est affirmé nulle part : HYPOTHÈSE. La profondeur est importée de [B] (« neuf fois le gain d'un pas de raffinement »), cadre différent. |
| S2 | L'organisme « raffine les bassins larges » aujourd'hui. | Génération 1 : onze variantes d'un même constat (RAPPORTÉ). Génération 2 : copies renommées refusées (RAPPORTÉ). Des variantes proches et des copies ne sont pas du raffinement au sens de [B] ; la lecture « raffinement » est HYPOTHÈSE. |
| S3 | Il existe une **loi des propositions des modèles** stable, sous laquelle un bassin a une probabilité. | Chaque appel est en session neuve, six cartes, sans historique (RAPPORTÉ) : la loi des propositions est donc une fonction de la vue seule, ce qui rend la notion bien définie. Sa stabilité d'un appel à l'autre n'est mesurée nulle part : HYPOTHÈSE. |
| S4 | On peut « pousser » sans servir de signal à l'agent. | Contrainte N-053 et rejets du premier tour (OBSERVÉ-NON-AUDITÉ). Il reste quatre leviers : la vue publique (sans verdict), l'allocation des appels, la puissance du juge, le découpage en générations. Que l'un d'eux déplace la loi des propositions est HYPOTHÈSE. |
| S5 | Les proposeurs voient des épisodes **avec issues**. | Non établi : la vue listée en [F12] §1 contient description, grammaire, lois de l'archive ; le jeu d'instances du regroupement est explicitement **sans issue**. Si les proposeurs ne voient aucune issue, la « pente nette dans chaque branche » de [C4] n'est visible qu'au juge, et les méthodes côté vue (M3 ci-dessous) tombent. À trancher avant tout. |
| S6 | Pousser vers l'étroit ne touche pas la garde. | Faux par construction, et la question ne le relève pas : la composante conditionnelle s'écrit en `si_sinon`, la forme que le premier tour désigne comme **hors de la classe couverte par le nul** (OBSERVÉ-NON-AUDITÉ, [S1] ; limite du juge RAPPORTÉ, [F12] §1). Toute poussée vers les bassins étroits de ce type est une poussée vers la zone où le juge cède. Préalable incontournable : garde certifiée en absolu sur `si_sinon` et `melange`. |
| S7 | « À coût égal » est défini. | Le coût n'est défini dans aucune pièce : appels de proposeurs ? jetons ? **tirages frais du juge** ? Le dernier est un coût réel et c'est précisément celui que l'étroitesse consomme (§3). Il faut une unité de coût gelée avant comparaison. |
| S8 | La sophistication mathématique apporte quelque chose au-delà des témoins simples. | Aucun fait ; N-045 impose le bon marché d'abord. Chaque méthode ci-dessous a donc un témoin simple à coût égal. |
| S9 | Le remède « oubli périodique » de [B] est pertinent. | L'organisme oublie déjà à chaque appel (RAPPORTÉ). Ce qui joue le rôle de la mémoire, c'est l'**archive**, et son masquage est rejeté. Le transfert de [B] est HYPOTHÈSE. |

---

## 2. Méthodes, les plus prometteuses d'abord

Pour chacune : objet, garantie (preuve) contre conjecture, lieu, qui calcule quoi, pourquoi elle bat le même budget de tirages indépendants, compatibilité, risques.

### M1. Processus e à report entre générations (« salle d'attente » du juge)

**Objet.** Pour une carte scellée c et une génération g, soit e_g(c) la valeur e calculée sur les tirages frais de g contre le nul N_g. Un **processus e** est le produit E_t(c) = ∏_{g≤t} e_g(c) sur tirages indépendants. Sous H₀ (« le monde est dans la classe de N »), E_t est une surmartingale non négative d'espérance ≤ 1, et l'inégalité de Ville donne P(sup_t E_t ≥ 1/α) ≤ α (Ville, 1939, *Étude critique de la notion de collectif*). La règle e-BH contrôle le taux de fausses découvertes pour des valeurs e **à dépendance arbitraire** (Wang et Ramdas, 2022, *False discovery rate control with e-values*, JRSS-B — référence à vérifier pour le volume), ce qui autorise d'y entrer des produits.

**Ce que cela garantit, ce qui est à prouver.** Garanti (preuve existante) : la validité du produit tant que chaque facteur est une valeur e pour le **même** H₀. Point délicat, à prouver pour cet organisme : le nul **grossit** d'une génération à l'autre (N_{g+1} ⊇ N_g en lois), donc e_g, calculé contre N_g, n'est pas garanti sous H₀_{g+1}. Voie sûre que je propose : promouvoir sur min(E_t contre le nul **gelé** à la première soumission, e_t contre le nul **courant**). Le minimum de deux valeurs e est une valeur e sous chacun des deux H₀ (E[min] ≤ E[e_t] ≤ 1) ; e-BH sur ces minima contrôle donc le taux de fausses découvertes sous H₀ courant, et le facteur courant seul porte la garde contre les copies des lois nouvellement archivées. C'est conservateur ; la perte de puissance est à mesurer.

**Lieu et calcul.** Juge, orchestrateur seul. Une carte non promue à g mais dont e_g dépasse un seuil bas gelé d'avance (par exemple e_g ≥ 2, illustratif) est **retenue mécaniquement** dans une salle d'attente ; elle n'entre pas dans l'archive, n'est **jamais servie** à un proposeur, et est retestée sur les tirages frais de g+1 contre le nul courant. m, le nombre d'hypothèses de l'e-BH, inclut les cartes en attente, fixé par règle écrite.

**Pourquoi elle atteint un bassin étroit mieux que des tirages indépendants.** Un bassin étroit du second type des faits (effet confiné à une région rare de masse r(A)) a, par la borne de dilution d ≤ r(A)·ln 2 ([S1]) transposée au juge, un taux de croissance de log e par tirage borné par r(A) fois la divergence locale. À nombre de tirages fixe par génération, une telle carte a une valeur e modeste et meurt ; sous report, elle **accumule** sur plusieurs générations sans qu'on augmente le nombre de tirages par génération ni qu'on baisse α. Le budget supplémentaire est le retest des cartes en attente (à compter dans le coût, §5).

**Compatibilité.** Aucun modèle ne décide ; aucun score servi ; aucune prime de nouveauté (la règle est aveugle au contenu) ; aucun rejet du premier tour rouvert. Preuve à fournir : validité du minimum quand le nul grossit (ci-dessus), et comptage de m.

**Risques.** (i) Puissance perdue par le minimum ; (ii) la salle d'attente allonge la vie de cartes qui sont des copies partielles : contre cela, le facteur courant ; (iii) ce n'est pas une poussée des proposeurs, seulement une survie accrue des propositions étroites déjà faites.

### M2. Générations comme splitting multiniveau (simulation d'événements rares)

**Objet.** Soit un bassin atteint par une **chaîne** C₁ → C₂ (profondeur 2, [C4]) : C₂ n'est proposable qu'une fois C₁ archivée (HYPOTHÈSE, [C4]). Avec n cartes indépendantes en une seule génération, P(atteindre C₂) = 1 − (1 − q₂)ⁿ où q₂ est la probabilité de proposer C₂ sans sa condition, « presque invisible », donc ≈ 0. Le schéma par générations est un **splitting** (Kahn et Harris, 1951, *Estimation of particle transmission by random sampling* ; version adaptative : Cérou et Guyader, 2007, *Adaptive multilevel splitting for rare event analysis*, référence à vérifier) : la fonction de niveau est l'**état de l'archive**, chaque génération est un niveau, l'archive est le mécanisme de resélection des « particules ». La probabilité d'atteinte devient ∏_k P(C_k | C_{k−1} archivée), et le résultat classique du splitting est que, à budget fixe, la variance (ici : la probabilité de manquer) est minimale quand les probabilités conditionnelles de passage sont **égales entre niveaux**, et que le nombre de niveaux doit être au moins la profondeur de la chaîne.

**Garanti contre conjecture.** Garanti : les formules de probabilité d'atteinte et le fait qu'aucune réallocation de tirages **indépendants** ne change 1 − (1 − q₂)ⁿ (§3). Conjecture : que les proposeurs réels se comportent comme des particules conditionnées, c'est-à-dire proposent C₂ avec probabilité nettement positive une fois C₁ servie dans l'archive — c'est exactement l'HYPOTHÈSE que [C4] réserve au pilote.

**Lieu et calcul.** Conception de la course : nombre de générations G et cartes par génération, **fixés par règle écrite avant la course** (donc pas pilotés par la diversité, conforme à [C3] §4.3). À budget total de cartes B, comparer (G petit, B/G grand) et (G grand, B/G petit). L'orchestrateur ne calcule rien de nouveau.

**Pourquoi elle bat les tirages indépendants.** C'est la seule méthode de la liste qui crée de la **dépendance** entre tirages dans le bon sens : les tirages de g+1 sont conditionnés par un succès à g. Elle vise le bassin étroit du **premier** type (invisible en moyenne) là où M1 vise le second (région rare).

**Compatibilité.** Totale : aucune information nouvelle servie, aucun masquage, aucune prime. Preuve à fournir : aucune au sens statistique ; la puissance de l'e-BH par génération baisse quand B/G baisse (moins de cartes, mais m plus petit aussi) — à chiffrer sur le banc.

**Risques.** (i) Si les proposeurs ne conditionnent pas (conjecture fausse), plus de générations ne donne rien et coûte des tirages frais ; (ii) une génération petite peut ne promouvoir aucune C₁, et la chaîne s'arrête ; (iii) interaction avec M1 : les cartes en attente consomment aussi des tirages.

### M3. Plan d'expériences orthogonal pour le jeu public d'instances (conditionné à S5)

**Objet.** La composante conditionnelle de [C4] est un terme d'**interaction** de signes : nul en effet principal, net dans chaque branche. Dans un plan à deux niveaux, un **tableau orthogonal de force 2** sur k facteurs rend tous les effets principaux et toutes les interactions d'ordre 2 estimables avec la même précision σ²/N, par orthogonalité des contrastes (Hedayat, Sloane et Stufken, 1999, *Orthogonal Arrays: Theory and Applications*). Sous tirage aléatoire des traits, un contraste d'interaction confiné à une région rare a une précision dégradée en r(A) ; sous plan équilibré, non.

**Lieu et calcul.** Orchestrateur, sur le **jeu public d'instances** servi avec la vue — uniquement si des issues sont servies aux proposeurs (S5). Les traits sont publics ; l'orchestrateur **sous-échantillonne par rejet** sur les traits les épisodes du monde pour approcher un plan de force 2 (ou pondère), les issues venant du monde. Aucune issue n'est inventée, aucun verdict n'est servi.

**Pourquoi elle aide.** Elle augmente la masse servie r(A) de la région rare dans ce que voient les proposeurs, ce qui attaque directement la borne de dilution côté proposeur. Elle ne change **rien** côté juge, dont les tirages frais suivent la loi du monde ; la puissance du juge sur la région rare reste bornée (voir M1).

**Garanti contre conjecture.** Garanti : l'estimabilité. Conjecture : qu'un modèle de langue exploite des données équilibrées pour poser un `si_sinon` sur le bon signe.

**Compatibilité.** Pas de masquage (on sert une sélection par traits publics, règle écrite et publique), pas de quota de forme, pas de prime. Preuve à fournir : que la sélection par rejet sur les traits n'informe pas sur l'oracle (elle n'utilise que les traits, c'est immédiat si la règle est fixée avant de voir les issues).

**Risques.** (i) S5 faux : méthode sans objet ; (ii) un plan équilibré déforme la vue de la loi marginale des traits, ce qui peut faire surajuster des régions rares : à vérifier sur le contrôle négatif (monde sans composante rare, § 4) ; (iii) pression vers `si_sinon`, donc vers la zone où le juge cède (S6).

### M4. Allocation hors ligne des configurations de proposeurs par échantillonnage de Thompson, récompense sur l'oracle

**Objet.** Un bandit à bras = configurations (modèle, température, variante gelée de la vue), récompense = nombre de composantes **étroites certifiées** couvertes par appel, divisé par le coût mesuré. L'échantillonnage de Thompson (Thompson, 1933 ; analyse par Agrawal et Goyal, 2012, *Analysis of Thompson Sampling for the Multi-armed Bandit Problem*, COLT) a un regret en O(√(KT log T)) (ordre de grandeur, à vérifier pour la variante exacte).

**Lieu et calcul.** **Hors course**, sur la famille de mondes à graine scellée, par l'orchestrateur, avec l'oracle : c'est exactement le cadre que N-058 autorise (composition jugée sur l'oracle et le coût, jamais sur le verdict du juge). Pendant une course, la composition est **gelée** ([C3] §4.3).

**Pourquoi elle aide.** Si certaines configurations ont une loi de propositions plus massive sur les bassins étroits, le bandit les trouve avec moins de mondes pilotes qu'une grille.

**Garanti contre conjecture.** Garanti : regret. Conjecture : qu'il existe une hétérogénéité entre configurations sur ce critère ; sinon le bandit converge vers « tout se vaut », ce qui est aussi une réponse.

**Risques.** (i) Surajustement à la famille de mondes pilotes : contrôle par mondes tenus à part ; (ii) ce bras n'agit pas sur la loi d'un proposeur donné, seulement sur le mélange.

### M5 (mineure). Reparamétrisation publique de l'archive

Servir l'archive sous forme canonique **et** sous forme de prédictions stratifiées sur le jeu d'instances sans issue — information équivalente, pas de masquage. Pure conjecture que la lecture par strates fasse proposer des conditions ; je la cite pour la mesurer, pas pour la recommander avant le banc.

**Méthodes écartées, et pourquoi.** Tout ce qui ressemble à une optimisation bayésienne, un processus ponctuel déterminantal ou une entropie dans la **sélection** ou dans un **signal servi** rouvre les rejets du premier tour et casse E[e] ≤ 1 ; je ne vois pas d'argument pour que l'objection ne s'applique pas. Le suréchantillonnage des strates rares **dans les tirages du juge** est valide conditionnellement aux traits si la loi des traits est contrôlée par l'orchestrateur, mais il déplace la puissance vers les régions rares au détriment des communes, ce qui est une prime implicite à un type d'idée ; je ne le propose pas sans preuve séparée.

---

## 3. Ce qui est impossible en principe, et sous quelles hypothèses de structure un gain existe

1. **Tirages indépendants.** Avec n cartes indépendantes de loi q, P(atteindre un bassin b) = 1 − (1 − q(b))ⁿ, quelle que soit la façon de les ordonner ou de les regrouper après coup. Aucune mathématique appliquée **après** le tirage n'augmente cette probabilité ; seuls comptent un changement de q (vue, M3, M5 ; composition, M4) ou une dépendance entre tirages (générations, M2).

2. **Condition du gain par dépendance.** M2 gagne si et seulement si le bassin est atteignable par une chaîne dont **chaque maillon intermédiaire est lui-même promouvable** par le juge et archivable. Si C₁ est elle-même invisible ou hors de la classe que le juge couvre, la chaîne ne démarre pas : impossibilité, pas de méthode.

3. **Borne côté juge.** Un effet confiné à une région de masse r(A) a un taux de croissance de log e par tirage ≤ r(A) × divergence locale (transposition de la borne de dilution de [S1], OBSERVÉ-NON-AUDITÉ à l'origine ; la transposition est mienne, à prouver). Le nombre de tirages frais nécessaires croît en 1/r(A). Aucune méthode côté proposeur n'y change rien ; seuls le temps (M1) ou les tirages (coût) le font. « À coût égal » en tirages, les bassins très étroits du second type sont **incertifiables**, et c'est voulu : c'est la garde.

4. **Profondeur.** La profondeur n'est connue qu'après la trouvaille et par l'oracle. Tout proxy de profondeur calculable sans oracle est une HYPOTHÈSE ; tout proxy servi ou utilisé en sélection est interdit. On ne peut donc viser la profondeur ; on ne peut que viser l'étroitesse et **lire** la profondeur après coup sur D2.

5. **Garde et étroitesse sont en tension structurelle** (S6). Un gain sur les bassins étroits de type conditionnel qui ne serait pas accompagné d'une certification absolue de la garde sur `si_sinon` est inobservable proprement : on ne saurait pas si les promotions sont des trouvailles ou des recombinaisons que le nul ne couvre pas.

---

## 4. Expériences décisives et mesure des instruments (livrables b et c)

Toutes sous préenregistrement scellé (R1), verdict par lecteur neuf sur critères gelés (R13), même audit en cas de résultat trop propre dans un sens ou l'autre (R4). Préalable commun, hérité du premier tour : banc hors ligne et garde certifiée en absolu sur `si_sinon` et `melange` ; sans cela, rien ci-dessous n'est interprétable.

### E1 (la moins chère) — Granularité des générations (teste M2)

- **Monde** : famille à graine scellée, avec une chaîne de profondeur 2 (C₁ puis C₂ conditionnelle), largeur réglée par la masse de la région et la taille de l'effet, profondeur réglée par le gain de C₂.
- **H_A** : à budget de cartes B et de tirages frais T égaux, le bras « 4 générations de B/4 cartes » couvre C₂ (D2, étage retenues) plus souvent que le bras « 2 générations de B/2 cartes ».
- **H_B** : la couverture de C₂ ne dépend que de B ; le bras à 4 générations couvre au plus autant, ou moins (perte de puissance e-BH).
- **Métrique** : fréquence de couverture de C₂ par l'oracle, lue une fois après la course, sur K mondes appariés par graine (même monde, deux bras).
- **Seuil** (illustratif, à geler) : différence appariée ≥ 0,2 en fréquence sur K = 20 mondes, test des signes apparié au niveau 0,05.
- **Contrôle négatif** : mêmes mondes **sans** C₂ (profondeur 1). Les deux bras doivent se valoir ; si le bras à 4 générations gagne aussi là, le gain ne vient pas de la chaîne (audit R4).
- **Témoin à coût égal** : un **proposeur aveugle** (échantillonneur de la grammaire, sans modèle) dans les deux bras. S'il couvre C₂ aussi souvent que les modèles, les modèles n'apportent rien à cette étape.
- **Ce qui est falsifié** : H_A faux → la conjecture de conditionnement de [C4] tombe, et M2 avec elle ; H_B faux → le découpage en générations est un levier réel et la règle de niveaux égaux devient le prochain objet d'étude.

### E2 — Report entre générations (teste M1)

- **H_A** : avec salle d'attente (règle min, seuil d'entrée gelé), la fréquence de promotion d'une composante rare vraie (masse r(A) réglée) sur 3 générations dépasse celle sans salle d'attente, à T tirages frais totaux égaux (le bras sans salle reçoit les tirages de retest en tirages ordinaires).
- **H_B** : pas de gain (la puissance est bornée par T, pas par le temps), ou gain payé par des promotions sous H₀.
- **Métrique** : taux de vrais positifs oracle sur la composante rare ; **taux de fausses découvertes oracle** sur des mondes où le monde est **dans** la classe du nul (contrôle négatif : toute promotion est fausse).
- **Seuil** (illustratif) : gain de vrais positifs ≥ 0,15 ; fausses découvertes ≤ α + 0,02 sur ≥ 200 décisions.
- **Falsification** : fausses découvertes > α + marge → la preuve du minimum est fausse ou mal appliquée, M1 tombe ; gain nul → le temps n'achète rien et seuls les tirages comptent.

### E3 — Plan orthogonal de la vue (teste M3, seulement si S5 est tranché positivement)

- **H_A** : la proportion de cartes brutes (étage 1 de D2) qui couvrent la composante conditionnelle est plus grande avec jeu public équilibré qu'avec jeu public tiré au hasard, même nombre d'épisodes.
- **H_B** : égale, ou la vue équilibrée augmente les cartes `si_sinon` **sans** couvrir la composante (fausse piste par surajustement de région rare).
- **Contrôle négatif** : monde sans composante conditionnelle ; la vue équilibrée ne doit pas augmenter le nombre de `si_sinon` proposés.
- **Témoin à coût égal** : vue aléatoire de même taille.

### Mesure minimale de chaque instrument nommé (livrable c)

- **Détecteur de bassin (regroupement [C3] §3).** Cas honnêtes appariés : (i) paires « même loi, formes différentes » (doivent être groupées) ; (ii) paires « mêmes partout sauf une strate de masse r(A) » (ne doivent **pas** l'être — c'est la borne de dilution). Mesures : taux de détection sur (i), taux de fausses alertes sur (ii), en fonction de ε et de r(A). Vérifications mécaniques à battre : égalité des formes canoniques seule ; distance globale seule sans strates. Si la lecture par strates ne bat pas la distance globale sur (ii), l'instrument ne sait pas voir l'étroit.
- **Mesure d'étroitesse (« petite probabilité sous la loi des propositions »).** Estimateur : fréquence d'un bassin sur N appels en session neuve, vue fixe. Cas honnêtes : composantes plantées à visibilité réglée (effet principal fort, faible, nul en moyenne). Fausse alerte : une composante à effet principal fort déclarée étroite. Référence mécanique : le proposeur aveugle de la grammaire, dont la loi est calculable exactement.
- **Oracle D2 (composantes certifiées couvertes).** Sa vérification minimale est la « détectabilité certifiée » : un ajusteur aveugle qui connaît la **forme** de la composante (pas sa valeur) doit la retrouver sur les tirages du juge dans ≥ 95 % des graines (illustratif) ; sinon, un échec des proposeurs n'est pas interprétable.
- **La garde elle-même.** Fausses promotions sous H₀ (monde dans la classe du nul) sur recombinaisons par morceaux et produits de lois archivées, exprimées en `si_sinon` et `melange` : ≤ α. C'est le préalable, pas une mesure accessoire.

---

## 5. Ancrage matériel (livrable d)

Tout chiffre ci-dessous est **illustratif** ; aucun ne vient des faits.

- **Proposeurs.** Les faits nomment Claude (Fable, Opus), Argon, Astra, Kimi ; ils ne disent pas lesquels sont à poids ouverts, et je ne l'affirme pas. Pour E1 et E2, le **proposeur aveugle** (échantillonneur de grammaire, coût nul en inférence) est indispensable comme témoin et suffit pour E2, qui ne teste que le juge. Pour E1, un modèle à poids ouverts de taille moyenne (10 à 70 milliards de paramètres, illustratif) servi localement, plus un proposeur commercial en nombre d'appels limité.
- **Volume d'appels (E1)** : K = 20 mondes × 2 bras × 4 générations au plus × 4 proposeurs = 640 appels, six cartes chacun ; à quelques milliers de jetons par appel, de l'ord