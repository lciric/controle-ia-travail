# Réponse brute — gemini-4-neon

- Modèle demandé : gemini-4-neon
- Heure (date -u) : Sat Nov 21 18:13:43 UTC 2026
- Réglages : plafond de sortie 65536, réflexion 32768
- Question : question-servie-v1.md, précédée de « Réponds en français. »
- Modèle servi : gemini-4-neon
- Clé (nom) : GEMINI_API_KEY
- Jetons facturés : entrée 1795, texte 17608, réflexion 34992, total déclaré 54395
- Coût estimé : 0.7944 dollars (tarif 3.0 / 15.0 dollars par million, relance comprise)
- Motif d'arrêt : STOP
- Journal :
  - envoi unique

---

Le problème posé n’est pas d’abord un problème de cryptographie ou de comparaison de textes : c’est un **problème de contrôle d’information dans une expérience adaptative portant sur un objet unique (ou très petit)**. Son nœud central est double : d’une part, le prédicat « recouvrir » porte sur deux idées en langage naturel et non sur des ensembles formels ; d’autre part, **toute décision visible prise à propos de la famille candidate F transmet un signal aux concepteurs de moniteurs qui connaissent déjà F**, même si le verdict lui-même reste secret.

Les sept premières sections répondent aux sept questions de méthode. Suivent trois protocoles complets et distincts, la recommandation argumentée, puis la liste de ce qui reste inconnu.

---

## 1. Ce que « recouvrir » doit vouloir dire

### Le critère fondamental : la validité causale de la généralisation

Le but du secret d’évaluation S n’est pas de préserver une formulation littéraire, mais de garantir que l’évaluation finale distingue les moniteurs qui **généralisent** de ceux qui ne détectent que ce pour quoi ils ont été conçus ou entraînés. La définition du recouvrement doit donc être subordonnée à ce but causal :

> **Critère directeur :** F recouvre S si le fait de verser F au travail courant (générateurs d’idées et bancs d’essai) augmente sensiblement la probabilité qu’un moniteur du programme détecte S **par spécialisation sur F ou par suggestion de S**, sans amélioration comparable sur des menaces réellement indépendantes.

À l’aune de ce critère, les cinq notions proposées se hiérarchisent clairement :

1. **Identité (S = F) :** beaucoup trop étroit. Deux textes écrits indépendamment en langage naturel ne sont jamais identiques ; ce critère laisserait passer presque toutes les contaminations réelles.
2. **Inclusion de S dans F ($S \subset F$) :** **critère indispensable et le plus critique**, d’autant que S est une manière précise de nuire et F une famille de menaces. Si S est une réalisation particulière de F, verser F aux générateurs d’idées et au banc d’essai revient à préparer directement les moniteurs à S.
3. **Inclusion de F dans S ($F \subset S$) :** **également dangereux**, quoique plus nuancé. Comme F doit alimenter des générateurs d’idées à base de modèles de langage, dont la fonction même est d’extrapoler à partir d’exemples, un cas particulier F peut aisément conduire ces générateurs à reconstruire la famille plus vaste S.
4. **Mécanisme commun :** très pertinent. Deux menaces formulées différemment mais reposant sur le même levier causal (même faille d’architecture, même stratégie de dissimulation, même point d’exploitation de la tâche) induiront des contre-mesures directement transférables de F vers S.
5. **Trace commune dans ce qu’un moniteur lit :** **pertinent, mais à manier avec une prudence extrême.** Il faut distinguer deux choses :
   - *Une trace générique de canal* (par exemple : S et F produisent toutes deux une incohérence dans un journal d’actions) ne doit **pas** compter comme un recouvrement ; sinon, presque toutes les menaces observables par le même canal se recouvriraient, et l’on empêcherait justement la généralisation légitime.
   - *Une signature spécifique (transfert étroit)* — le fait qu’une règle de détection étroite, sur-ajustée aux particularités de F, déclenche incidemment sur S — constitue en revanche un vrai recouvrement, car un moniteur non généraliste obtiendrait alors un bon score sur S par simple effet de bord.

### Grille opérationnelle retenue

On définit donc « F recouvre S » comme la disjonction de **trois sous-critères explicites** :
1. **Inclusion ou extrapolation proche :** S est un cas particulier de F, F est un cas particulier de S, ou un concepteur (humain ou modèle générateur d’idées) exposé à F produirait vraisemblablement S ou une variante très proche.
2. **Mécanisme partagé :** F et S reposent sur le même principe de nuisance ou le même procédé de dissimulation.
3. **Transfert de détecteur étroit :** un détecteur spécifique conçu uniquement pour capturer F (sans viser la généralité) détecterait probablement S en exploitant la même signature observable.

### Peut-on remplacer la lecture par une règle sans jugement libre ou une mesure automatique ?

Deux pistes existent, chacune avec un prix net :

- **Mesure géométrique ou lexicale automatique** (similarité entre vecteurs de plongement de textes, recouvrement de mots-clés) : **inadaptée comme critère principal**. Le prix en serait un taux inacceptable de faux négatifs (une famille F très abstraite et un secret S très concret peuvent être géométriquement éloignés tout en vérifiant $S \subset F$) et de faux positifs (deux textes du même domaine partagent le même vocabulaire technique sans aucun recouvrement de menace).
- **Test comportemental de transfert en chambre close** (semi-objectif) : on peut réduire la part de jugement libre en opérationnalisant le critère directeur. Une instance neuve de modèle de langage qui ne lit **que F** engendre un ensemble de variantes concrètes de F et propose plusieurs détecteurs étroits taillés pour F ; puis, en chambre close, un évaluateur (ou un banc d’exécution isolé si S est déjà implémenté) vérifie si l’une des variantes coïncide avec S ou si l’un des détecteurs étroits se déclenche sur S.
  - *Prix :* coût de mise en œuvre nettement plus élevé, nécessité de disposer déjà d’une implémentation exécutable de S pour la seconde partie, et persistance d’un jugement humain ou automatisé pour décider si une variante coïncide avec S.

En résumé, pour deux idées écrites en langage naturel, **on ne peut pas éliminer totalement le jugement interprétatif**, mais on peut le discipliner par une grille à trois sous-critères, complétée si possible par un test d’extrapolation en chambre close.

---

## 2. Qui peut juger

### Conditions exigées d’un juge lisant S et F

Quiconque lit simultanément S et F devient porteur de S et de sa relation à F. Il doit donc satisfaire quatre conditions :
1. **Indépendance préalable et absence d’incitation :** n’avoir participé ni à la conception des moniteurs ni aux travaux bloqués par la mise en réserve de F (sinon biais fort en faveur de la libération de F).
2. **Compétence technique suffisante :** comprendre la surface d’observation des moniteurs et les mécanismes de nuisance, sans quoi le jugement dégénère en comparaison littéraire superficielle.
3. **Cloisonnement ultérieur rigoureux :** si le juge est un humain, il doit être **écarté de tout rôle lié aux moniteurs** — conception, amélioration, sélection, critique, rédaction de consignes pour les générateurs d’idées, création de nouvelles familles candidates (car connaître S biaiserait involontairement ses propositions), et même discussions informelles de fond sur les angles morts des moniteurs (une simple hésitation ou un silence ciblé en réunion constitue une fuite).
4. **Durée de l’écartement :** jusqu’au **gel définitif et scellé cryptographiquement** de tous les moniteurs soumis à l’évaluation finale (ou jusqu’à la retraite officielle de S et son remplacement par un secret inconnu du juge).

### Comparaison des profils de juges

- **L’auteur initial de S :** il connaît déjà S et est déjà écarté de la conception des moniteurs ; il n’ajoute donc aucune contamination humaine. Toutefois, il présente un **biais d’attachement** (risque de sous-estimer ou surestimer la singularité de son propre secret), il ne permet aucune redondance s’il est seul, et il ne peut pas être convenablement mis en aveugle sur des leurres s’il a écrit S. Il est en revanche précieux pour **pré-fabriquer des témoins calibrés** (section 4).
- **Un tiers humain extérieur au programme :** très bon pour l’indépendance et l’absence de fuites informelles de couloir, mais coûteux, lent, et potentiellement mal informé de la surface exacte d’observation des moniteurs (ce qui exige de lui fournir un dossier technique neutre).
- **Une instance neuve de modèle de langage dont le contexte est détruit :** c’est un changement structurel majeur.
  - *Ce que cela change en bien :* la destruction du contexte réalise une **amnésie contrôlable**. L’instance ne participe à aucune réunion le lendemain, n’a pas besoin d’être mise en quarantaine, ne conserve aucun biais de session en session, et permet de multiplier les évaluations indépendantes (plusieurs familles de modèles distinctes, plusieurs permutations de l’ordre de présentation entre S et F) à très faible coût.
  - *Les nouveaux risques introduits :*
    1. **Fuites d’infrastructure :** historique des appels, journaux du serveur, conservation ou ré-entraînement par le fournisseur de modèle. Si un concepteur de moniteurs administre le compte ou consulte les journaux, le cloisonnement est nul. Il faut impérativement un environnement isolé contrôlé par un gardien de l’évaluation (modèle auto-hébergé hors réseau, ou contrat garanti sans conservation ni entraînement).
    2. **Injection de consignes :** F étant un texte en langage naturel venant de l’extérieur du coffre, il peut contenir — par malveillance ou par coïncidence — des formulations détournant le juge. L’instance doit donc recevoir F dans un cadre strictement délimité comme donnée non fiable et ne produire qu’une sortie rigoureusement contrainte (des codes fixes, jamais de texte libre transmis à l’équipe).
    3. **Erreurs corrélées :** plusieurs instances d’un même modèle commettent souvent les mêmes erreurs (sensibilité excessive au vocabulaire de surface, cécité sur certaines analogies structurelles).
- **Plusieurs juges indépendants (architecture recommandée lorsqu’on vérifie) :** un **panel hétérogène d’instances neuves** issues d’au moins trois familles de modèles différentes, chacune exécutée en double avec permutation d’ordre (S puis F, puis F puis S), sous contrôle de témoins plantés, avec **recours optionnel à un tiers humain extérieur** uniquement sur les cas d’audit ou de désaccord (tout en préservant un délai fixe de réponse).

---

## 3. Ce que le verdict laisse fuir, et comment le compter

### L’asymétrie fondamentale de la fuite

Supposons que, du point de vue des concepteurs de moniteurs qui connaissent F, la probabilité a priori que F recouvre S vaille $p$ (par exemple $p = 0{,}05$). Il faut distinguer deux mesures de fuite (calculs élémentaires de théorie de l’information) :

1. **La fuite moyenne** (information mutuelle de Shannon entre S et un verdict binaire exact) vaut l’entropie binaire :
   $$I(S ; V) = -p \log_2 p - (1-p)\log_2(1-p)$$
   Pour $p = 0{,}05$, cela ne fait qu’environ $0{,}29$ bit en moyenne.
2. **La fuite dans le pire cas (gain d’information ponctuel)** est **beaucoup plus dangereuse**, car l’asymétrie est brutale :
   - Sur un verdict « ne recouvre pas » ($V = 0$), les concepteurs excluent une région de probabilité $p$ : la fuite vaut $-\log_2(1-p)$ bits (pour $p = 0{,}05$, seulement $0{,}074$ bit).
   - Sur un verdict « recouvre » ($V = 1$), les concepteurs localisent S dans le voisinage de F : la fuite vaut $-\log_2 p$ bits (pour $p = 0{,}05$, **$4{,}32$ bits d’un seul coup** ; pour $p = 0{,}01$, **$6{,}64$ bits**). Si F est étroite, S est pratiquement dévoilé.

Sur une suite de $K$ demandes adaptatives, même un jeu de devinettes involontaire érode S : dans le pire cas, $K$ réponses binaires exactes bien choisies (chacune couvrant la moitié de l’espace restant) révèlent $K$ bits et divisent l’espace des hypothèses par $2^K$.

### Moyens de borner la fuite et comptage de la fuite restante

1. **Forme du verdict :** supprimer toute justification textuelle, tout score continu, toute indication du sous-critère déclencheur et, s’il existe plusieurs secrets $\{S_1, \dots, S_m\}$, ne jamais dire lequel est touché.
   - *Fuite restante :* si le verdict agrège $m$ secrets indépendants (« recouvre au moins un secret »), la probabilité de positif passe de $p$ à $p_m = 1 - (1-p)^m \approx m p$, ce qui réduit la fuite de localisation sur un secret particulier d’environ $\log_2 m$ bits, sans éliminer la fuite si $m$ est petit.
2. **Destinataires (et le piège de l’action visible) :** cacher le mot « recouvre » aux concepteurs ne sert à rien si **le sort visible de F dépend du verdict**. Tant que des personnes liées aux moniteurs connaissent F et constatent si F entre ou non dans le banc d’essai, elles reçoivent le verdict de fait. Les destinataires ne bornent la fuite que si l’action observable est découplée du verdict.
3. **Délai :** reporter l’annonce jusqu’au gel final réduit la fuite exploitable à **0 bit**, mais bloque F jusque-là. Un délai fixe court (par exemple une publication de statut toutes les deux semaines) ne réduit pas l’information par requête, mais empêche les boucles adaptatives rapides et **supprime le canal auxiliaire temporel** (qui trahirait un recours à un juge humain en cas de doute).
4. **Budget maximal de demandes ($K_{\max}$) :** borner strictement le nombre de tests permis avant le gel final.
   - *Fuite restante :* au plus $K_{\max}$ bits dans le pire cas adaptatif (en moyenne au plus $\sum_{i=1}^{K_{\max}} H_2(p_i)$), **mais ne protège absolument pas contre le choc d’un seul verdict positif ($-\log_2 p$ bits)**.
5. **Réponse commune à un lot de $B$ familles :** si au moins une famille du lot recouvre S, tout le lot est mis en réserve.
   - *Fuite restante :* si le lot est libéré, fuite d’exclusion égale à $-B \log_2(1-p)$ bits (identique à $B$ réponses négatives séparées). Si le lot est mis en réserve, la probabilité de blocage vaut $1-(1-p)^B \approx B p$ ; la localisation est diluée parmi $B$ familles, ce qui économise environ $\log_2 B$ bits en cas de blocage.
   - *Prix :* bloquer $B-1$ familles innocentes dès qu’une seule touche S.
6. **Bruit unilatéral (mise en réserve aléatoire de probabilité $q$, ou quota fixe de réserve) :** c’est l’outil décisif pour casser la fuite d’un verdict positif. Toute famille recouvrante (ou douteuse) est mise en réserve avec probabilité $1$ ; toute famille non recouvrante est néanmoins mise en réserve au hasard avec probabilité $q \in (0, 1)$, sous un statut strictement identique.
   - *Comptage exact de la fuite restante :*
     - En cas de **libération** : les concepteurs apprennent que F ne recouvre pas S (hors faux négatif du juge) ; fuite d’exclusion $= -\log_2(1-p)$ bits (ex. $0{,}074$ bit pour $p=0{,}05$).
     - En cas de **mise en réserve** : le rapport de vraisemblance (facteur de Bayes en faveur du recouvrement) est borné par $1/q$. La probabilité a posteriori que F recouvre S vaut $\frac{p}{p + (1-p)q}$, et le gain d’information ponctuel sur le recouvrement vaut $\log_2\left(\frac{1}{p+(1-p)q}\right) \le \log_2(1/q)$ bits.
     - *Exemple chiffré :* avec $p = 0{,}05$ et $q = 0{,}5$, observer une mise en réserve ne fait monter la probabilité de recouvrement que de $5\%$ à $9{,}5\%$ (gain de $0{,}93$ bit au lieu de $4{,}32$ bits !). L’information mutuelle moyenne tombe à $H_2(p+(1-p)q) - (1-p)H_2(q) \approx 0{,}048$ bit (divisée par 6).
     - *Variante par quota fixe :* sur chaque lot de $B$ familles, mettre toujours en réserve $\max(r, X)$ familles (où $X$ est le nombre de familles recouvrantes). Tant que $X \le r$, même le **nombre** de mises en réserve ne fuit rien.
   - *Point de vigilance :* cette protection échoue si l’on autorise la soumission répétée de variantes d’une famille déjà mise en réserve (la probabilité que $k$ copies non recouvrantes soient toutes bloquées par hasard chute à $q^k$). Il faut donc interdire la re-soumission de variantes proches.
7. **Découplage total par banque de secrets pré-engagés et retrait silencieux :** si toute famille F est **toujours libérée** et que les secrets recouverts sont simplement retirés d’une banque pré-engagée de $M$ secrets (ou triés après le gel final), alors :
   - *Fuite directe par le verdict :* **strictement 0 bit**.
   - *Fuite résiduelle indirecte (conditionnement de survie) :* les concepteurs savent que le secret évalué à la fin n’aura été recouvert par aucune des familles $F_1, \dots, F_k$ libérées, ce qui correspond uniquement à la fuite d’exclusion $-\sum_{i=1}^k \log_2(1-p_i)$ bits — **jamais** à la fuite catastrophique d’un positif.

---

## 4. Aveuglement et témoins plantés

### Comment savoir que le juge juge bien

Un juge (modèle ou humain) ne doit jamais être cru sur parole. On l’étalonne **en continu et à son insu** en mêlant la vraie comparaison à des objets témoins dont la réponse attendue est connue d’avance :
- des **leurres positifs** (recouvrant S selon au moins un des trois sous-critères : inclusion directe, mécanisme commun, signature étroite) ;
- des **proches négatifs** (ne recouvrant pas S, mais situés dans le même domaine technique, de même longueur et de même style, pour éviter des négatifs triviaux qui gonfleraient artificiellement la note du juge) ;
- et, idéalement, des **paires étalons hors-S**, c’est-à-dire des paires $(S_{\text{test}}, F_{\text{test}})$ construites sur des secrets factices sans lien avec le vrai S, afin que le juge ignore même quelle paire contient le véritable secret du programme.

### Qui peut fabriquer un leurre qui recouvre S sans fuite ?

Il est **impossible** de fabriquer de manière fiable un leurre qui recouvre S sans connaître S. La fabrication doit donc être strictement confinée aux acteurs qui connaissent déjà S, ou confiée à une instance éphémère en chambre close :

1. **Pré-fabrication scellée par l’auteur de S dès la création de S (méthode la plus propre) :** au moment où l’auteur rédige S, il rédige aussi un jeu de leurres positifs (une généralisation englobant S, une spécialisation, une variante à même mécanisme) et de proches négatifs. Le tout est scellé dans le coffre du gardien. **Aucun nouvel humain ne lit S.**
2. **Fabrication en chambre close par une instance neuve détruite aussitôt :** si S existe déjà sans leurres pré-fabriqués, le gardien lance une instance neuve isolée (modèle différent de ceux du panel juge, pour limiter les biais stylistiques partagés), lui confie S et des consignes de génération de leurres positifs et proches négatifs, stocke les résultats dans le coffre chiffré, puis détruit le contexte de l’instance.
3. **Complément par paires étalons hors-S :** n’importe quel collaborateur externe (qui ne connaît pas S) peut fabriquer des paires factices $(S_{\text{test}}, F_{\text{test}})$ étiquetées, pour masquer le vrai S au milieu d’un lot.

**Condition impérative de sécurité :** les leurres positifs fabriqués à partir de S contiennent de l’information sur S ; ils ont donc **exactement le même niveau de classification que S** (jamais visibles hors du coffre, détruits ou déclassifiés seulement après le gel final).

### Protocole d’aveuglement anti-reconnaissance stylistique

Un risque subtil est que le juge reconnaisse la « patte » stylistique de l’auteur de S (ou d’un modèle générateur) sur les leurres, et repère par contraste la vraie famille F. Pour contrer cela :
1. **Normalisation stylistique isolée :** avant tout jugement, chaque texte (F et chaque leurre, un par un) est réécrit dans un gabarit canonique de longueur fixe (par exemple : objectif de la nuisance, mécanisme de dissimulation, traces observables plausibles) par une **instance neuve dédiée qui ne voit que ce texte seul**, puis est détruite.
2. **Suppression de toute métadonnée** (dates, noms d’auteurs, noms de fichiers), affectation d’identifiants opaques et permutation aléatoire.
3. **Isolement par paire pour les modèles-juges :** chaque paire $(S, X)$ est soumise à une **instance neuve séparée**, afin que le juge ne puisse pas comparer F aux leurres dans un même contexte et calibrer ses réponses par effet de contraste. (Pour un juge humain voyant un lot, l’ordre est aléatoire et la proportion de positifs varie d’un lot à l’autre.)
4. **Règle d’invalidation pré-enregistrée :** le gardien vérifie d’abord les scores du juge sur les témoins. Si le juge échoue sous le seuil fixé, son verdict sur F est automatiquement invalidé et reclassé en « non tranché ».

### Taux d’erreur tolérables dans chaque sens

Les deux erreurs ont des coûts profondément asymétriques :

- **Faux négatif (dire « ne recouvre pas » alors que F recouvre S) :** coût **catastrophique et irréversible** (contamination de l’évaluation finale). Le taux tolérable doit être **très bas** : idéalement inférieur à $5\%$ sur l’ensemble des leurres positifs, et quasi nul ($0\%$ sur les témoins d’inclusion franche). On y parvient par une **règle de vote prudente** dans le panel (par exemple, un seul juge sur trois votant « recouvre » ou « doute » suffit à empêcher le classement « ne recouvre pas »).
- **Faux positif (dire « recouvre » alors que F ne recouvre pas S) :** coût **modéré et réversible** (blocage d’une famille innocente ou consommation d’un secret de réserve). Un taux de $10\%$ à $25\%$ sur des proches négatifs difficiles reste généralement tolérable.
  - *Mise en garde subtile :* il ne faut pas compter sur les faux positifs du juge pour remplacer le bruit aléatoire $q$ ! Les faux positifs du juge surviennent préférentiellement quand F est thématiquement *proche* de S ; ils fuient donc encore une information directionnelle, contrairement à un tirage aléatoire pur indépendant de S.

---

## 5. Que faire de la famille ensuite

### Examen des cinq options envisagées

1. **Garder F scellée jusqu’à l’évaluation finale :** protège S contre l’injection de F dans les générateurs d’idées et le banc d’essai (sans pouvoir effacer F de la mémoire de ceux qui l’ont déjà lue). Ne protège contre la fuite du verdict **que** si des familles non recouvrantes sont également gardées scellées de manière indiscernable (bruit $q$ ou quota fixe), ou en cas de moratoire général.
2. **Verser F au travail courant :** acceptable dans le cas « ne recouvre pas » (hors réserve aléatoire) ; **destructeur** dans les cas « recouvre » et « non tranché » si S reste le secret actif ; en revanche, **valide** si S est retiré silencieusement d’une banque de secrets pré-engagés.
3. **Verser F en partie (version expurgée) :** **à proscrire formellement.** Comme des personnes liées à la conception des moniteurs connaissent déjà le texte intégral de F, leur rendre une version amputée crée un **effet de pochoir** : le passage retiré désigne S avec une précision chirurgicale, bien pire que le mot « recouvre ». De plus, les générateurs d’idées risquent de ré-engendrer la partie retirée à partir du reste.
4. **Substituer F à S ou la joindre à S comme second secret :**
   - *Substituer F à S :* **mauvaise option**, car F est déjà connue de personnes qui participent de près ou de loin à la conception des moniteurs ; elle ne satisfait plus l’exigence d’aveuglement strict de S.
   - *Joindre F à S comme second secret :* inutile et trompeur si F recouvre S (double comptage d’une même menace). Si F ne recouvre *pas* S et tombe dans la réserve aléatoire, elle peut être conservée comme **évaluation secondaire distincte** (mesurant la généralisation hors banc d’essai et hors générateurs, mais non strictement aveugle aux humains qui la connaissaient) — jamais mélangée dans le même indicateur que S.
5. **Remplacer S par un secret neuf et libérer l’ancien :**
   - *Libérer l’ancien S en cours de projet :* **déconseillé**, car cela annonce le recouvrement, introduit un secret tardif sans horodatage antérieur à la conception des moniteurs (risque de biais rétrospectif), et perturbe le travail en cours.
   - *Activer silencieusement un autre secret issu d’une banque pré-engagée (sans libérer l’ancien avant le gel final) :* **excellente option**, analysée en détail dans le Protocole 2.

### Suite à donner à F dans chacun des trois cas

La décision dépend du régime choisi par le programme :

| Verdict interne du juge | Régime A : S unique protégé par réserve aléatoire (Protocole 1) | Régime B : Banque de $M$ secrets pré-engagés avec rotation silencieuse (variante en ligne du Protocole 2) |
| :--- | :--- | :--- |
| **F recouvre S** | **Garder F scellée** jusqu’au gel des moniteurs. Ne pas la verser en partie. Ne pas la substituer à S. | **Verser F normalement** au travail courant. Retirer silencieusement le secret $S_j$ touché du groupe « strictement intact » dans le journal scellé du coffre (ne pas le libérer avant le gel final). |
| **F ne recouvre pas S** | Tirage aléatoire indépendant de probabilité $q$ : avec probabilité $1-q$, **verser F** ; avec probabilité $q$, **garder F scellée** jusqu’au gel final (où elle servira d’évaluation secondaire hors banc d’essai). | **Verser F normalement** au travail courant. Aucun secret retiré. |
| **Le juge ne tranche pas** (désaccord, cas limite ou échec sur témoins) | **Traiter exactement comme un recouvrement : garder F scellée** jusqu’au gel final (l’asymétrie des coûts interdit de libérer dans le doute). | **Traiter avec prudence : verser F**, et marquer silencieusement le secret $S_j$ concerné comme « douteux / exclu de l’ensemble principal intact » dans le journal scellé. |

*(En régime de moratoire sans vérification — Protocole 3 — il n’y a pas de verdict : F est gardée scellée jusqu’à la fin de la vague de S, puis versée à l’ouverture de la vague suivante.)*

### Que dire, et à qui, pour ne pas dévoiler le verdict ?

- **Règle absolue :** personne participant à la conception des moniteurs (y compris l’auteur de F) ne reçoit jamais les mots « recouvre », « ne recouvre pas », « doute », ni aucun score, ni aucun délai variable.
- **Qui sait le vrai verdict ?** Uniquement le **gardien de l’évaluation** (cloisonné jusqu’au gel final) et le **journal chiffré du coffre** (dont seule l’empreinte cryptographique est versée au registre public pour audit ultérieur).
- **Message canonique transmis à l’équipe (à une date fixe du calendrier) :**
  - Dans le Régime A, uniquement l’une des deux phrases normalisées :
    - *« Famille [identifiant] : autorisée pour versement au travail courant. »*
    - *« Famille [identifiant] : placée en réserve protocolaire jusqu’au gel des moniteurs. »* (Formule strictement identique pour un recouvrement, un doute du juge ou un tirage au sort de réserve.)
  - Dans le Régime B, une seule phrase, toujours identique : *« Famille [identifiant] : autorisée pour versement au travail courant. »*

### Que écrire dans les résultats d’un banc d’essai auquel il manque un monde pour cette raison ?

Il faut concilier **honnêteté scientifique** (ne pas cacher une lacune) et **étanchéité de l’aveugle** (ne pas désigner S) par une règle en deux temps :

- **Avant le gel définitif des moniteurs (rapports intermédiaires et internes) :**
  - Ne jamais mentionner de résultat de vérification ni décrire le contenu technique du monde manquant comme « trop proche du secret ».
  - Inscrire une mention standardisée et vérifiable par empreinte :
    > *« Avertissement de couverture : conformément au protocole de réserve aveugle du programme, $r$ familles candidates sur $B$ proposées à la date du [date] (empreintes enregistrées au registre sous les numéros [liste]) sont maintenues hors du banc d’essai jusqu’au gel définitif des moniteurs. La mise en réserve peut résulter d’un tirage aléatoire de réserve, d’une incertitude méthodologique ou d’une règle de non-recouvrement, sans distinction communiquée avant le gel. Les résultats présentés portent exclusivement sur les $B-r$ mondes autorisés et ne couvrent pas les familles réservées. »*
- **Après le gel définitif des moniteurs (rapport final public) :**
  - Lever l’aveugle intégralement en ouvrant le journal scellé : lister toutes les familles mises en réserve avec leur **motif réel enregistré à l’époque** (preuve qu’il n’y a pas eu de suppression opportuniste de mauvais résultats), puis présenter **séparément** les performances des moniteurs sur : (1) le banc d’essai de travail, (2) les familles réservées aléatoirement (hors banc, mais non strictement aveugles), (3) les secrets strictement aveugles et intacts, et (4) le cas échéant, les secrets retirés pour recouvrement.

---

## 6. Faut-il seulement vérifier ?

Comparer la vérification en cours de route aux règles qui s’en passent fait apparaître que **la vérification en ligne n’est pas toujours la meilleure option**.

### Comparaison des quatre stratégies

1. **Vérification en cours de route (avec bruit $q$ pour protéger un S unique) :**
   - *Protection de S :* bonne mais imparfaite (risque résiduel de faux négatif du juge + fuite bornée par $\log_2(1/q)$ bits en cas de réserve + fuite d’exclusion).
   - *Coût :* élevé en ingénierie (coffre, témoins, panel isolé, gardien) et perte opérationnelle d’une fraction $q$ de familles innocentes.
2. **Mettre en réserve toute famille nouvelle sans rien regarder (moratoire total) :**
   - *Protection de S :* **maximale** (0 bit de fuite, 0 risque de faux négatif).
   - *Coût :* très faible en infrastructure, mais **très lourd scientifiquement et opérationnellement** si l’évaluation est lointaine (le banc d’essai reste incomplet, les pistes nouvelles sont figées, les chercheurs sont découragés de proposer des familles).
3. **Ne rien réserver et concevoir un secret neuf $S'$ juste avant l’évaluation (secret tardif) :**
   - *Protection contre la fuite pendant le développement :* **totale** (0 bit, S’ n’existe pas encore).
   - *Coût opérationnel :* **minimal** (aucun blocage, aucune infrastructure de vérification).
   - *Failles graves :* perte de la preuve cryptographique d’antériorité ; risque de **biais rétrospectif** (si l’auteur de $S'$ connaît, même vaguement, l’architecture des moniteurs construits, il peut inventer un secret trop facile ou artificiellement adversarial) ; et **biais de sélection** vers des menaces de plus en plus exotiques à mesure que les familles courantes couvrent l’espace naturel.
4. **Tirer au sort ce qui est réservé sans rien vérifier (face à un S déjà fixé) :**
   - *Fuite sur S :* 0 bit.
   - *Protection contre la contamination :* **insuffisante !** Avec probabilité $p(1-q)$ par famille, une famille recouvrante passe librement et contamine S sans qu’on le sache. Par exemple, avec $k = 10$ familles, $p = 0{,}05$ chacune et $q = 0{,}5$, la probabilité qu’au moins une famille contamine silencieusement S est de $1 - (1 - 0{,}025)^{10} \approx 22\%$. Pour rendre ce risque négligeable, il faudrait pousser $q$ si près de $1$ qu’on retomberait dans le coût du moratoire total sans même avoir sa garantie.
5. **Cinquième voie (issue de la comparaison) — Banque de $M$ secrets pré-engagés + libération inconditionnelle + vérification différée après le gel final :**
   - Ne rien vérifier en cours de route (tout libérer), puis vérifier le recouvrement entre les $M$ secrets et l’ensemble des familles travaillées **après le gel des moniteurs** (en aveugle des résultats des moniteurs).
   - *Protection :* 0 bit de fuite en cours de route, pré-engagement préservé, pas de quarantaine longue des juges. Si $p = 0{,}05$ et $k = 10$ familles indépendantes, un secret donné survit avec probabilité $(0{,}95)^{10} \approx 60\%$ ; avec $M = 8$ secrets indépendants, on espère environ $4{,}8$ secrets intacts et la probabilité d’épuisement total tombe sous $0{,}1\%$.
   - *Coût :* concevoir $M$ secrets indépendants en amont, plus le **biais de sélection** (les menaces sur lesquelles deux humains convergent spontanément sont classées à part ; d’où l’obligation de publier aussi le taux de redécouverte).

### Quelle règle coûte le moins pour une même protection, et sous quelles hypothèses ?

- **Si le secret S est unique, l’échéance proche et le nombre de familles nouvelles faible (1 à 3) :** le **moratoire total** coûte le moins pour une protection supérieure ; vérifier en ligne n’est pas rentable.
- **Si le programme est récurrent, que l’on peut pré-créer $M$ secrets indépendants ($M \ge 6$) et que la probabilité de recouvrement $p$ est modérée ($p \lesssim 0{,}1$) :** la **banque pré-engagée avec tri post-gel** domine toutes les autres options (zéro blocage, zéro fuite de verdict, puissance statistique supérieure).
- **Si le secret S est unique et irremplaçable, l’échéance lointaine, et le coût du blocage élevé :** la **vérification en ligne avec réserve aléatoire** est la seule option permettant de libérer une fraction du travail sans exposer S.
- **Si l’espace des menaces est très vaste et qu’un tiers externe rigoureusement coupé de l’architecture des moniteurs peut produire un secret en fin de projet :** le **secret tardif** coûte le moins en travail quotidien, au prix d’une perte de crédibilité externe liée à l’absence d’horodatage initial.

---

## 7. Ce que la littérature apporte, et où elle s’arrête

*(Conformément aux consignes, toutes les références bibliographiques, années et ordres de grandeur ci-dessous sont cités de mémoire ; les détails bibliographiques et résultats quantitatifs sont donc marqués « non vérifié ».)*

1. **Engagements cryptographiques**
   - *Sources :* Manuel Blum, *Coin Flipping by Telephone* (1981/1983, non vérifié) ; Moni Naor, *Bit Commitment Using Pseudorandomness* (*Journal of Cryptology*, 1991, non vérifié).
   - *Ce qui s’applique :* **pleinement**, pour prouver l’antériorité et l’intégrité du texte de S, des leurres pré-fabriqués, du journal chiffré des verdicts et du gel final des moniteurs (en utilisant une fonction de hachage cryptographique accompagnée d’un sel aléatoire à haute entropie, afin d’écarter toute attaque par dictionnaire sur des textes courts ou structurés).
   - *Où cela s’arrête :* l’engagement scelle des octets, non leur sens ; il n’empêche pas les fuites humaines et ne permet pas de comparer deux textes sans les ouvrir.

2. **Preuves à divulgation nulle de connaissance**
   - *Source :* Shafi Goldwasser, Silvio Micali et Charles Rackoff, *The Knowledge Complexity of Interactive Proof Systems* (symposium sur la théorie du calcul, 1985, puis revue en 1989, non vérifié).
   - *Ce qui s’applique :* **quasiment rien au problème central.**
   - *Où cela s’arrête :* pour deux raisons indépendantes. D’abord, « F recouvre S » pour deux idées en langage naturel n’est pas une relation mathématique formelle traduisible en circuit public (même si l’on prouvait cryptographiquement l’exécution d’un modèle de langage — travaux récents sur les preuves d’inférence vérifiable, référence à chercher — cela prouverait seulement la loyauté d’exécution d’un modèle, non la justesse sémantique du jugement). Ensuite et surtout, **une preuve à divulgation nulle de connaissance révèle la valeur de vérité du prédicat** ; or ici, c’est précisément le bit « F recouvre S » lui-même qui constitue la fuite majeure.

3. **Intersection privée d’ensembles et calcul sécurisé à plusieurs parties**
   - *Sources :* Andrew Chi-Chih Yao, *Protocols for Secure Computations* (1982) et *How to Generate and Exchange Secrets* (1986) ; Oded Goldreich, Silvio Micali et Avi Wigderson (1987) pour le calcul sécurisé à plusieurs parties ; Michael Freedman, Kobbi Nissim et Benny Pinkas (2004) pour l’intersection privée d’ensembles (détails bibliographiques non vérifié).
   - *Ce qui s’applique :* **non applicable à deux idées en langage naturel** (sauf si l’on réduisait artificiellement S et F à des ensembles finis de mots-clés ou d’identifiants discrets, ce qui viderait le critère de recouvrement de sa pertinence).
   - *Où cela s’arrête :* ces protocoles suppriment le besoin d’un tiers de confiance *pendant le calcul*, mais **ne protègent jamais contre l’inférence tirée du résultat du calcul**. Même un calcul sécurisé parfait de la fonction « recouvre » fuiterait exactement les mêmes $-\log_2 p$ bits en cas de réponse positive.

4. **Tiers de confiance et séquestre**
   - *Source :* pratique établie en gouvernance de la sécurité et droit des contrats (séquestre de code source ; synthèse spécifique aux évaluations d’intelligence artificielle : référence à chercher).
   - *Ce qui s’applique :* **directement**, sous la forme du rôle de gardien de l’évaluation (ou d’organisme tiers), qui conserve S sous séquestre, administre le coffre, exécute les protocoles en chambre close et publie les journaux après le gel.
   - *Où cela s’arrête :* la sécurité repose sur l’intégrité, la disponibilité et la compétence d’une personne ou d’une organisation, et le tiers de confiance ne résout pas à lui seul la fuite causée par la décision visible sur F.

5. **Salles blanches et cloisonnements des secrets d’affaires**
   - *Source :* méthodologie de conception en salle blanche (*clean-room design*) issue du droit d’auteur logiciel et des cloisonnements d’information en droit et finance (références juridiques précises à chercher).
   - *Ce qui s’applique :* **très directement**, pour structurer la frontière étanche entre la zone contaminée (auteur de S, gardien, éventuel juge humain) et la zone propre (concepteurs de moniteurs et générateurs d’idées), avec interface écrite minimale et journalisée.
   - *Où cela s’arrête :* dans une petite équipe de recherche (« quelques personnes »), les cloisons humaines s’érodent vite par les échanges informels. L’usage d’instances éphémères de modèles permet justement de maintenir la zone contaminée à un effectif humain minimal.

6. **Mise en aveugle et comités indépendants des essais cliniques**
   - *Source :* Susan S. Ellenberg, Thomas R. Fleming et David L. DeMets, *Data Monitoring Committees in Clinical Trials: A Practical Perspective* (Wiley, 2002, non vérifié).
   - *Ce qui s’applique :* **l’une des analogies méthodologiques les plus directement transposables.** On en reprend la charte pré-enregistrée du comité indépendant, la stricte limitation des communications à des messages canoniques (afin que ni le ton ni le calendrier ne trahissent la tendance), et les comités indépendants d’adjudication travaillant sur des dossiers anonymisés et standardisés.
   - *Où cela s’arrête :* un essai clinique statue rarement et globalement (continuer ou arrêter l’essai) sur des critères cliniques très codifiés, alors qu’ici l’on statue de façon répétée sur des objets conceptuels singuliers en langage naturel.

7. **Jeux de test tenus à l’écart et analyse adaptative des données**
   - *Sources :* Cynthia Dwork, Vitaly Feldman, Moritz Hardt, Toniann Pitassi, Omer Reingold et Aaron Roth, *Preserving Statistical Validity in Adaptive Data Analysis* (symposium sur la théorie du calcul, 2015, non vérifié) et *The Reusable Holdout: Preserving Validity in Adaptive Data Analysis* (*Science*, 2015, non vérifié). Ces travaux établissent (ordres de grandeur cités de mémoire, non vérifié) qu’un jeu de test de taille $n$ interrogé de manière adaptative naïve peut perdre sa validité après un nombre de requêtes linéaire en $n$, alors qu’un mécanisme bruité à seuil permet d’atteindre un nombre de requêtes de l’ordre de $n^2$ sous hypothèses appropriées.
   - *Ce qui s’applique :* **le diagnostic qualitatif fondamental** — interroger de manière adaptative un objet d’évaluation, même par des réponses très pauvres, crée une dépendance statistique qui ruine la mesure de généralisation — et le principe consistant à limiter et bruiter les retours.
   - *Où cela s’arrête :* **les garanties mathématiques ne s’appliquent pas ici**, car elles reposent sur un jeu de test composé de $n$ observations indépendantes et identiquement distribuées avec $n$ grand. Ici, $n = 1$ (un seul secret S, ou quelques secrets) : la loi des grands nombres ne joue pas, et le mécanisme de jeu de test réutilisable à seuil ne fonctionne pas tel quel.

8. **Confidentialité différentielle des réponses et réponse aléatoire**
   - *Sources :* Stanley L. Warner, *Randomized Response: A Survey Technique for Eliminating Evasive Answer Bias* (*Journal of the American Statistical Association*, 1965, non vérifié) ; Cynthia Dwork, Frank McSherry, Kobbi Nissim et Adam Smith, *Calibrating Noise to Sensitivity in Private Data Analysis* (conférence sur la théorie de la cryptographie, 2006, non vérifié) ; théorèmes de composition de Cynthia Dwork, Guy N. Rothblum et Salil Vadhan (2010, non vérifié).
   - *Ce qui s’applique :* **le cadre mathématique du rapport de vraisemblance borné et de la composition des fuites**, qui fonde directement le bruit unilatéral (mise en réserve aléatoire $q$) et le comptage rigoureux de la fuite cumulée.
   - *Où cela s’arrête :* la confidentialité différentielle bilatérale stricte exigerait de libérer avec probabilité strictement positive une famille recouvrant S, ce qui détruirait S. On ne peut donc appliquer qu’une **protection asymétrique** (bruit uniquement vers la mise en réserve), et le compromis bruit/utilité ressemble à celui de la confidentialité différentielle locale (coût élevé en familles innocentement bloquées dès que l’on veut une fuite inférieure au bit).

---

## Trois protocoles complets et distincts

---

### Protocole 1 : Filtre en ligne par panel d’instances éphémères étalonné et réserve aléatoire unilatérale

*Conçu pour le cas où S est unique et irremplaçable, l’évaluation finale lointaine, et où l’on souhaite débloquer une fraction significative des familles non recouvrantes tout en bornant la fuite.*

#### Déroulement pas à pas

1. **Étape 0 — Scellement initial et constitution du coffre (avant toute requête)**
   - **Acteurs :** auteur de S, gardien de l’évaluation (personne strictement exclue de la conception des moniteurs jusqu’au gel final).
   - **Qui lit quoi :** le gardien reçoit S (en clair), ainsi que des leurres positifs et proches négatifs pré-fabriqués par l’auteur de S (ou, à défaut, générés en chambre close par une instance neuve d’un modèle distinct des futurs juges, puis détruite). Un collaborateur externe (ne connaissant pas S) fournit en outre un jeu de paires étalons factices $(S_{\text{test}}, F_{\text{test}})$.
   - **Ce qui est scellé :** la charte du protocole (grille des trois sous-critères, seuils d’acceptation sur témoins, probabilité de réserve aléatoire $q$ — par exemple $q = 0{,}5$ —, budget maximal $K_{\max}$ — par exemple $K_{\max} = 5$ —, calendrier fixe de réponse tous les quatorze jours), ainsi que les empreintes cryptographiques salées de S et des témoins, inscrits au registre public.

2. **Étape 1 — Dépôt de F**
   - **Qui lit quoi :** l’auteur de F dépose le texte de F dans une boîte de dépôt dont seul le gardien a l’accès en lecture. L’empreinte salée de F et son horodatage sont inscrits au registre public.
   - **Contrôle anti-répétition :** le gardien (ou une instance neuve isolée comparant F aux seules familles précédemment mises en réserve, sans S) vérifie que F n’est pas une reformulation d’une famille déjà mise en réserve. Si c’est un doublon manifeste, la requête n’est pas rejouée : elle reçoit automatiquement le statut de mise en réserve à la date prévue (évitant l’attaque par essais répétés contre $q$).

3. **Étape 2 — Préparation en aveugle dans le coffre**
   - **Qui lit quoi :** uniquement le gardien et des scripts isolés exécutés sur une machine ou un compte inaccessible aux concepteurs de moniteurs (modèles locaux hors réseau ou contrats garantissant zéro conservation ni entraînement).
   - **Normalisation stylistique :** pour chaque texte candidat (F, $L_+$ leurres positifs de S, $L_-$ proches négatifs de S, et les textes des paires étalons hors-S), le script lance une **instance neuve séparée** qui ne voit que ce seul texte, le réécrit dans le gabarit canonique de longueur fixe, écrit le texte normalisé dans le coffre chiffré, puis **détruit immédiatement son contexte**.
   - **Mélange :** le script attribue des identifiants opaques et permute aléatoirement les paires (graine enregistrée dans le journal chiffré du coffre).

4. **Étape 3 — Jugement en aveugle par panel hétérogène**
   - **Qui lit quoi :** pour chaque paire normalisée du lot et pour chaque modèle du panel (au moins trois modèles de familles distinctes, chacun testé dans les deux ordres de présentation : premier puis second texte, et réciproquement -> six évaluations par paire), le script lance une **instance neuve dédiée**. Chaque instance lit uniquement : la grille de recouvrement, les consignes de traitement des textes comme données non fiables, et les deux textes normalisés.
   - **Ce qui est écrit :** chaque instance renvoie strictement trois codes fermés parmi `{RECOUVRE, DOUTE, NON}` (un par sous-critère), sans texte libre, enregistrés dans le journal chiffré du coffre.
   - **Ce qui est détruit :** le contexte de chaque instance immédiatement après écriture du code, ainsi que tout fichier tampon hors du coffre chiffré.

5. **Étape 4 — Contrôle sur témoins, agrégation prudente et tirage aléatoire**
   - **Qui lit quoi :** un script déterministe audité dans le coffre (vérifié par le gardien).
   - **Contrôle qualité :** le script vérifie d’abord le score du panel sur les témoins plantés (par exemple : exigence de zéro faux négatif sur les leurres positifs francs, au plus un sur les limites, et taux de faux positifs sous $25\%$ sur les proches négatifs). Si un modèle échoue, il est exclu ; si le panel entier échoue, le verdict interne sur F devient automatiquement `NON_TRANCHE`.
   - **Agrégation asymétrique sur F :** F est classée `NON_RECOUVRE` uniquement si au moins cinq évaluations sur six renvoient `NON` sur les trois sous-critères. Elle est classée `RECOUVRE` si une majorité renvoie `RECOUVRE`, et `NON_TRANCHE` sinon. *(Option : dans le cas `NON_TRANCHE`, recours possible à un tiers humain extérieur lié par cloisonnement jusqu’au gel final, qui reçoit le lot entier anonymisé ; mais uniquement si sa réponse tient dans le calendrier fixe des quatorze jours.)*
   - **Tirage aléatoire :** si et seulement si le verdict interne est `NON_RECOUVRE`, le script tire une pièce cryptographique (probabilité $q$ de réserve, $1-q$ de libération). Dans les deux autres cas (`RECOUVRE` ou `NON_TRANCHE`), la décision est la réserve.

6. **Étape 5 — Archivage scellé et communication canonique**
   - **Ce qui est écrit :** le journal chiffré du coffre consigne toutes les sorties brutes, les scores sur témoins, le verdict interne, le tirage aléatoire et le motif réel ; l’empreinte cryptographique de cette nouvelle entrée de journal est publiée au registre public.
   - **Qui reçoit quel mot :** à la date fixe prévue, le gardien envoie à l’équipe exactement l’une des deux phrases canoniques : *« Famille [identifiant] : autorisée pour versement au travail courant »* ou *« Famille [identifiant] : placée en réserve protocolaire jusqu’au gel des moniteurs »*. Aucun autre mot.

7. **Étape 6 — Gel final et audit**
   - Après scellement cryptographique de tous les moniteurs, ouverture de S, des leurres et du journal du coffre ; publication intégrale des motifs et des performances séparées (banc d’essai, familles en réserve aléatoire, et secret S).

#### Analyse du Protocole 1

- **Hypothèses :** disponibilité d’un gardien fiable hors conception des moniteurs ; infrastructure d’exécution des modèles rigoureusement isolée et sans journalisation accessible ; capacité des modèles-juges (vérifiée sur témoins) à maintenir un taux de faux négatifs très faible ; tolérance du programme à la mise en réserve d’une fraction $q$ des familles innocentes.
- **Ce qu’il laisse fuir et vers qui :** vers les concepteurs de moniteurs qui connaissent F :
  - si F est autorisée : $-\log_2(1-p)$ bits d’exclusion (faible si $p$ est petit) ;
  - si F est placée en réserve : au plus $\log_2(1/q)$ bits de rapprochement vers S (ex. $\le 1$ bit pour $q = 0{,}5$).
  - Sur $K_{\max}$ requêtes, la fuite cumulée reste bornée par la somme des contributions individuelles.
- **Failles :** exposition au faux négatif (même faible) du panel de modèles ; biais résiduel si les auteurs de F utilisent malgré tout leur connaissance préalable de F ; coût élevé en familles innocentes bloquées si l’on veut une fuite très faible ($q$ proche de $1$) ; sensibilité à l’erreur humaine du gardien.
- **Manière la plus simple de le faire échouer :**
  - *Par erreur :* lancer le panel de modèles sur un compte partagé ou une interface qui conserve l’historique des requêtes lisible par l’équipe — ou laisser le gardien répondre plus vite dans les cas simples que dans les cas douteux (canal auxiliaire temporel).
  - *Par malveillance :* glisser dans F une injection de consignes incitant les modèles-juges à répondre `NON` pour faire libérer une famille qui recouvre S ; ou soumettre plusieurs variantes reformulées d’une même idée afin de contourner le bruit $q$ (par essais répétés).
- **Coût :** moyen à élevé en mise en place (coffre isolé, normalisation, témoins, gardien dédié), plus perte de travail courant sur une fraction $q$ des familles innocentes (partiellement compensée par leur réutilisation comme évaluation secondaire).

---

### Protocole 2 : Banque de secrets pré-engagés, libération inconditionnelle et tri post-gel

*Conçu pour un programme récurrent où l’on refuse tout blocage du travail courant et toute fuite de verdict en cours de route.*

#### Déroulement pas à pas

1. **Étape 0 — Constitution et scellement d’une banque de $M$ secrets (avant le cycle de conception des moniteurs)**
   - **Acteurs :** $M$ concepteurs de secrets indépendants les uns des autres (par exemple $M = 6$ à $10$, aucun ne participant à la conception des moniteurs, et ne communiquant pas entre eux sur leurs secrets) et le gardien de l’évaluation.
   - **Qui lit quoi :** chaque concepteur $j$ rédige un secret $S_j$ (accompagné idéalement de deux leurres positifs et deux proches négatifs), sans lire les autres secrets. Seul le coffre du gardien rassemble les $M$ dossiers.
   - **Ce qui est scellé :** les $M$ empreintes salées des secrets et la charte d’évaluation post-gel (grille de recouvrement, règle d’adjudication en aveugle des scores, règle de publication séparée des secrets intacts et des secrets recouverts) sont publiées au registre public avant le début du travail sur les moniteurs.

2. **Étape 1 — Soumission et versement inconditionnel de chaque famille F**
   - **Qui lit quoi :** personne ne lit S ni aucun $S_j$ !
   - **Ce qui est écrit et scellé :** dès qu’une famille candidate F (ou toute idée structurée versée aux générateurs et bancs d’essai) entre dans le travail courant, son texte daté et son empreinte salée sont archivés dans le registre des travaux du programme.
   - **Qui reçoit quel mot :** à chaque soumission, la règle publique s’applique automatiquement sans jugement : *« Famille [identifiant] : archivée et versée immédiatement au travail courant. »*
   - *(Variante 2bis — Sentinelle de réserve minimale : si le programme craint d’épuiser tous ses secrets avant la fin, le gardien peut exécuter périodiquement en silence le contrôle de recouvrement sur la banque à l’aide d’instances détruites, sans rien dire tant qu’il reste au moins $M_{\min}$ secrets intacts — par exemple $M_{\min} = 2$ — et ne déclencher une procédure d’exception qu’en cas d’atteinte du seuil critique.)*

3. **Étape 2 — Gel définitif des moniteurs**
   - **Ce qui est scellé :** au terme du cycle de développement, tous les moniteurs candidats (code, paramètres, consignes, poids) sont scellés par empreinte cryptographique au registre public. Aucune modification n’est plus permise.

4. **Étape 3 — Adjudication du recouvrement post-gel, en aveugle complet des résultats des moniteurs**
   - **Ordre impératif :** cette étape a lieu **avant** que quiconque impliqué dans le jugement de recouvrement n’ait connaissance des performances des moniteurs sur les $S_j$ (idéalement avant même d’exécuter les moniteurs sur les $S_j$, afin d’éliminer tout biais de confirmation !).
   - **Qui lit quoi :** un comité d’adjudication indépendant (combinant panel d’instances neuves de modèles et juges humains extérieurs, étalonnés par les témoins plantés) lit chaque secret $S_j$ face au dossier complet des familles versées $\{F_1, \dots, F_k\}$ et des grandes pistes explorées par le programme.
   - **Ce qui est écrit et scellé :** le comité classe chaque $S_j$ en trois catégories pré-enregistrées : `INTACT` (aucun recouvrement avec les travaux du programme), `AMBIGU` (doute ou recouvrement partiel), `RECOUVERT` (recouvert par au moins une famille travaillée). Ce classement est scellé au registre public **avant** l’exécution ou la divulgation des scores des moniteurs.
   - **Ce qui est détruit :** les contextes des instances de modèles utilisées ; les juges humains n’ont plus besoin d’être cloisonnés puisque les moniteurs sont déjà gelés.

5. **Étape 4 — Évaluation finale et publication intégrale**
   - Les moniteurs gelés sont évalués sur l’ensemble des $M$ secrets.
   - **Ce qui est écrit dans le rapport final :** (1) le résultat principal de généralisation, calculé sur les secrets classés `INTACT` ; (2) le taux de redécouverte spontanée (fraction de secrets classés `RECOUVERT` ou `AMBIGU`) ; et (3) séparément, les scores obtenus sur les secrets `AMBIGU` et `RECOUVERT` (à titre diagnostique et de transparence).

#### Analyse du Protocole 2

- **Hypothèses :** capacité budgétaire et humaine à concevoir $M$ secrets véritablement indépendants et de haute qualité avant le cycle de développement ; probabilité de recouvrement $p$ suffisamment modérée par rapport à $k$ pour que plusieurs secrets survivent ; discipline rigoureuse d’archivage de tout ce qui entre dans le travail courant ; séparation stricte entre adjudication de recouvrement et lecture des scores des moniteurs.
- **Ce qu’il laisse fuir et vers qui :**
  - *Fuite directe par verdict pendant le développement :* **strictement 0 bit** vers les concepteurs de moniteurs.
  - *Fuite indirecte (conditionnement de survie) :* les concepteurs savent que les secrets `INTACT` à la fin ne recouvriront aucune famille travaillée ; cela équivaut à la seule fuite d’exclusion $-\sum_{i=1}^k \log_2(1-p_i)$ bits, jamais à une fuite de localisation.
- **Failles :** **biais de sélection** vers des menaces rares ou atypiques (les menaces intuitives, sur lesquelles deux concepteurs convergent spontanément, sortent de l’ensemble `INTACT`) ; risque théorique d’épuisement de la banque si $M$ est trop faible ou si les secrets initiaux sont corrélés entre eux ; inutilisable rétroactivement pour sauver un cycle déjà très avancé où un seul S existe.
- **Manière la plus simple de le faire échouer :**
  - *Par erreur :* faire tourner les moniteurs sur les $S_j$ avant de classer les $S_j$ en `INTACT`/`RECOUVERT`, et laisser les auditeurs connaître les résultats — le biais de confirmation ruine immédiatement l’objectivité du classement ; ou faire écrire les $M$ secrets par la même personne (corrélation cachée vidant la banque d’un coup).
  - *Par malveillance :* un concepteur de moniteurs soumet délibérément des familles « parapluie » volontairement très vagues et générales pour couvrir tout l’espace des menaces, afin soit de légitimer l’entraînement sur tout, soit de provoquer l’invalidation des secrets difficiles (parade : règles strictes de spécificité des familles et publication du taux de couverture).
- **Coût :** **nul en blocage opérationnel** pendant tout le développement, faible en infrastructure temps réel, mais **élevé en coût fixe initial** pour la conception indépendante des $M$ secrets.

---

### Protocole 3 : Séparation temporelle en vagues sans vérification en cours de route (moratoire court puis renouvellement)

*Conçu pour le cas où l’on refuse toute vérification en ligne (jugée trop risquée ou trop coûteuse), où S est déjà unique et scellé, et où l’on peut découper le programme en deux jalons.*

#### Déroulement pas à pas

1. **Étape 0 — Déclaration de moratoire sur la vague en cours (vague 1)**
   - **Acteurs :** direction du programme, gardien de l’évaluation.
   - **Règle publique :** aucune vérification de recouvrement n’est effectuée contre S. Toute famille candidate apparue après le scellement de S (y compris F et les suivantes) est placée en **moratoire strict** jusqu’au gel de la vague 1.
   - **Ce qui est scellé :** l’empreinte salée de F (et de chaque nouvelle famille) est enregistrée dans un registre « file d’attente vague 2 », ainsi que la date cible du gel de la vague 1 (raccourcie si nécessaire pour ne pas bloquer durablement le programme).
   - **Qui lit quoi :** **personne ne lit jamais S et F ensemble pendant la vague 1.** S reste scellé et non ouvert.
   - **Qui reçoit quel mot :** à chaque dépôt, message automatique unique : *« Famille [identifiant] : enregistrée en file d’attente pour la vague suivante, sans examen par rapport au secret en cours. »*

2. **Étape 1 — Achèvement et gel des moniteurs de la vague 1**
   - Les concepteurs terminent une première version complète des moniteurs sur le banc d’essai antérieur (avec mention de couverture neutre signalant les familles en file d’attente pour la vague 2).
   - **Ce qui est scellé :** empreintes cryptographiques de tous les moniteurs de la vague 1.

3. **Étape 2 — Ouverture de S, évaluation de la vague 1 et audit rétrospectif**
   - S est ouvert et les moniteurs gelés de la vague 1 sont évalués sur S.
   - **Contrôle honnête d’exposition cognitive :** après le gel, on vérifie (en transparence) si l’une des familles de la file d’attente (dont F, qui était déjà connue de certains participants) recouvrait S ; si oui, on le documente explicitement dans le rapport comme limite possible d’amorçage cognitif, sans invalider le protocole de séparation du banc d’essai.

4. **Étape 3 — Ouverture de la vague 2 et pré-engagement d’un secret neuf (ou d’une banque)**
   - **Libération :** toutes les familles de la file d’attente (dont F) — ainsi que l’ancien secret S désormais public — sont **versées librement** au banc d’essai et aux générateurs d’idées pour la vague 2.
   - **Création du nouveau secret :** avant le début des travaux de conception de la vague 2, un concepteur indépendant (ou $M$ concepteurs pour basculer vers le Protocole 2) qui **ne connaît pas les détails internes des moniteurs en cours de développement**, mais reçoit la liste des familles publiques de la vague 2 (y compris F et l’ancien S) pour éviter une répétition triviale, rédige et scelle un secret neuf $S^{(2)}$ (ou une banque $\{S^{(2)}_1, \dots, S^{(2)}_M\}$).
   - **Ce qui est détruit :** rien de particulier en cours de vague 1 (aucune instance juge n’ayant été lancée).

#### Analyse du Protocole 3

- **Hypothèses :** le programme peut être découpé en jalons relativement rapprochés ; la lacune temporaire du banc d’essai pendant la fin de la vague 1 est supportable ; les personnes connaissant déjà F restent capables de ne pas sur-orienter informellement la vague 1 vers F ; un concepteur véritablement indépendant des choix d’architecture des moniteurs est disponible pour créer $S^{(2)}$ avant la vague 2.
- **Ce qu’il laisse fuir et vers qui :** **strictement 0 bit** sur S pendant toute la vague 1 (puisque rien n’est testé). Lors du passage à la vague 2, les concepteurs savent seulement que $S^{(2)}$ a été conçu en évitant les familles déjà publiques de la vague 2 (conditionnement normal de généralisation hors-distribution).
- **Failles :** n’empêche pas la contamination cognitive informelle par les personnes qui connaissent déjà F pendant la vague 1 ; risque de glissement du calendrier si la vague 1 traîne (tentation de « tricher » informellement avec F) ; coût de l’arrêt temporaire du travail lié à F ; difficulté de garantir que le concepteur de $S^{(2)}$ ignore totalement l’architecture des moniteurs de la vague 1 (dont héritera probablement la vague 2 !).
- **Manière la plus simple de le faire échouer :**
  - *Par erreur :* laisser la vague 1 s’allonger pendant des mois, si bien que des chercheurs frustrés s’inspirent officieusement de F dans les réglages des moniteurs sans l’inscrire au banc d’essai ; ou laisser le concepteur de $S^{(2)}$ lire le rapport technique détaillé des moniteurs de la vague 1 avant d’écrire $S^{(2)}$.
  - *Par malveillance :* un participant qui connaît F et soupçonne sa proximité avec les angles morts de ses moniteurs incorpore discrètement une contre-mesure spécifique à F dans son moniteur de la vague 1 (détectable seulement par un audit approfondi du code et des consignes, difficile à prouver).
- **Coût :** **le plus faible de tous en infrastructure et en complexité** (aucun coffre de jugement en ligne, aucun panel de modèles à étalonner), mais un coût en **délai opérationnel** (gel temporaire de F jusqu’à la fin de la vague 1) et le coût de conception d’un nouveau secret pour la vague 2.

---

## Recommandation

### Architecture recommandée : transition en deux temps

Il convient de dissocier le **cas immédiat** (un secret S déjà scellé, une famille F déjà bloquée) du **régime récurrent** du programme :

1. **Pour le régime récurrent (dès la prochaine phase du programme) : adopter le Protocole 2 (banque de $M$ secrets pré-engagés, avec $M$ entre 6 et 10, libération inconditionnelle des familles candidates et adjudication de recouvrement post-gel en aveugle des résultats).**
   - *Pourquoi :* évaluer la généralisation sur un unique secret S souffre de toute façon d’une variance statistique énorme (un seul point d’évaluation) et rend chaque nouvelle famille candidate criseogène. Le Protocole 2 résout les deux problèmes ensemble : zéro fuite de verdict en cours de route, zéro blocage du travail, pré-engagement intact, et puissance statistique multipliée.
2. **Pour la crise immédiate (F face au S actuel) :**
   - **Si le gel d’un premier jalon de moniteurs peut avoir lieu rapidement (dans un horizon de quelques semaines à deux mois) :** appliquer le **Protocole 3** (garder F en moratoire sans la vérifier, évaluer proprement la vague 1 sur S, puis libérer F dans la vague 2 en basculant vers le Protocole 2).
   - **Si le gel final est lointain (plusieurs mois ou davantage) et que le blocage de F paralyse réellement un travail critique :** appliquer le **Protocole 1** (panel d’instances neuves hétérogènes étalonné sur témoins + mise en réserve aléatoire de probabilité $q = 0{,}5$ et budget strict $K_{\max} \le 5$), tout en préparant en parallèle la banque de secrets du Protocole 2 pour éliminer le besoin de vérification en ligne à l’avenir.

### Degré de confiance : **0,78 / 1**

- La confiance est **très élevée** (proche de $0{,}9$) sur les principes structurels : définition causale à trois sous-critères, rejet du versement partiel et de la substitution de F à S, nécessité impérative du bruit unilatéral dès que l’on vérifie en ligne, supériorité à moyen terme de la banque pré-engagée avec tri post-gel, et règles de communication neutre.
- Elle est ramenée à **$0{,}78$** sur le choix opérationnel exact entre Protocole 1 et Protocole 3 pour le cas immédiat, car cet arbitrage dépend de paramètres factuels du programme qui ne sont pas précisés dans l’énoncé.

### Ce qui me ferait changer d’avis

1. **Une probabilité de recouvrement spontané $p$ élevée (par exemple $p > 0{,}25$) :** si l’espace des menaces plausibles est étroit, le Protocole 2 risquerait d’épuiser trop vite une banque de taille réaliste et souffrirait d’un biais de sélection trop prononcé. Je recommanderais alors le **Protocole 3** (vagues courtes en moratoire strict) ou un Protocole 1 à quota élevé.
2. **Un coût prohibitif de conception des secrets :** si concevoir un seul secret de qualité mobilise des ressources si rares qu’il est impossible de constituer une banque de $M \ge 5$ secrets indépendants, le Protocole 2 devient impraticable ; le choix se resserre entre le Protocole 3 et le Protocole 1.
3. **Une implication centrale des détenteurs actuels de F dans les moniteurs :** si les personnes qui connaissent déjà F sont les principaux concepteurs des moniteurs (et non des contributeurs périphériques), la mise en réserve de F ne suffit plus à protéger parfaitement S ; cela pousserait à raccourcir drastiquement la vague 1 (Protocole 3) et à cloisonner plus strictement les auteurs futurs.
4. **Un échec empirique des modèles-juges lors d’un essai à blanc :** si, testé sur des paires factices $(S_{\text{test}}, F_{\text{test}})$, le panel de modèles dépassait $5\%$ de faux négatifs sur des inclusions abstrait/concret, il faudrait renoncer au jugement automatisé du Protocole 1 au profit d’un tiers humain extérieur ou du Protocole 3.
5. **Une contrainte contractuelle externe imposant le secret S actuel comme juge unique jusqu’à la fin :** cela exclurait toute rotation ou vague courte et imposerait l’arbitrage strict entre moratoire total et Protocole 1.

---

## Ce que je ne sais pas, et ce qu’il faudrait savoir du programme

En excluant tout renseignement sur le contenu de S et de F, voici ce que j’ignore et ce qui permettrait d’affiner concrètement le protocole et ses paramètres ($q$, $M$, $K_{\max}$, calendrier) :

1. **Calendrier et découpage :** combien de temps reste-t-il avant l’évaluation finale ? Le programme autorise-t-il un gel intermédiaire (vague 1 / vague 2) ?
2. **Capacité à produire des secrets :** combien de secrets du type de S existent déjà aujourd’hui ? Combien coûte la conception d’un secret indépendant supplémentaire, et combien de concepteurs indépendants (hors conception des moniteurs) sont disponibles ?
3. **Rythme et densité des familles candidates :** combien de familles du type de F sont attendues d’ici l’évaluation finale ? À quel point des concepteurs indépendants convergent-ils habituellement vers des idées proches dans ce domaine (ordre de grandeur de $p$ : plutôt $1\%$, $10\%$ ou $30\%$) ?
4. **Périmètre exact des personnes connaissant F :** quel rôle précis jouent les personnes qui ont déjà lu F dans la conception des moniteurs ? Sont-elles remplaçables ou centrales ? Peut-on instaurer pour les futures soumissions un dépôt direct au gardien avant toute diffusion interne ?
5. **Coût réel de la lacune du banc d’essai :** la mise de côté de F bloque-t-elle un axe essentiel de recherche ou seulement un scénario parmi une vingtaine ? Quelle proportion $q$ de familles innocentes le programme accepte-t-il de placer en réserve aléatoire ?
6. **Infrastructure technique et gouvernance :** le programme dispose-t-il déjà d’une personne entièrement cloisonnée (ou d’un organisme tiers) pouvant tenir le rôle de gardien ? Peut-il faire tourner des modèles de langage de familles diverses sur une infrastructure isolée, sans conservation des journaux et inaccessible aux concepteurs de moniteurs ?
7. **Nature des moniteurs évalués :** les moniteurs sont-ils des détecteurs spécialisés par menace, des modèles généralistes lisant des traces d’exécution, ou des dispositifs hybrides ? Cela conditionne fortement le poids à donner au sous-critère « transfert de détecteur étroit ».
8. **Modèle de menace interne :** le protocole doit-il seulement protéger une petite équipe coopérative contre les fuites involontaires et le sur-ajustement inconscient, ou doit-il aussi résister à un participant incité à tricher activement (par exemple dans une compétition entre équipes) ?
9. **Performance réelle des modèles sur la tâche de jugement :** j’ignore quel sera le taux effectif de faux positifs et de faux négatifs des modèles de langage actuels sur le niveau d’abstraction propre à ce programme ; seul un essai à blanc préalable sur paires factices étiquetées peut le mesurer avant toute utilisation sur le vrai S.
