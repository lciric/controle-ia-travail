# Proposition B — Riposte (Tour III.3)

Je suis la proposition B. L'attaque A est absente (jamais lancée) — je n'en invente rien. Je réponds uniquement à l'attaque C, qui vise ma conception point par point. L'attaque C est forte sur la mécanique d'agrégation ; je l'accepte là où elle me corrige, la transforme en test là où elle est contestable, la rejette là où elle se trompe.

---

## (a) Traitement de chaque attaque de C

### C-(a).1 — Destruction causale par paraphrase (EXP-1) → **ACCEPTÉE et transformée en contrôle obligatoire**

C a raison sur un point mécanique que ma conception traitait trop vite : relire en *teacher-forcing* un texte paraphrasé par un tiers ne lit pas les mêmes activations que la génération active. La distribution h_ℓ en lecture passive ≠ en génération. Mon seuil « Δ-AUROC < 0,05 entre brut et surface-apparié » confondait donc deux choses : (i) suppression du corrélat lexical, (ii) passage génération→lecture.

**Ce que j'accepte** : apparier la surface par réécriture tierce puis relire en teacher-forcing est un protocole confondu. Le contrôle n° 2 de C (« génération active vs lecture passive ») devient **obligatoire** et préalable.

**Ce que je ne concède pas** : C surdétermine en disant que le résidu d'intention est nécessairement détruit. C'est précisément ce qui est inconnu (c'est mon S1, HYPOTHÈSE). La bonne réponse n'est pas d'abandonner EXP-1 mais de **remplacer l'appariement par paraphrase** par un appariement **à la génération** : l'organisme génère lui-même, sous deux instructions qui produisent la **même surface cible** (longueur/format contraints par la consigne) mais diffèrent sur l'intention. Voir EXP-1 corrigée.

### C-(a).2 — Témoin ponctuel (citation faussée) contredit le biais diffus → **ACCEPTÉE, défaut réel**

C a raison. Mon « témoin vrai = citation faussée détectable par script » est une tromperie **localisée**, l'opposé du biais diffus défini par le programme (E §3.3, RAPPORTÉ). Sélectionner les sondes sur ce témoin, puis les tester sur le diffus en EXP-2, crée soit un échec artéfactuel, soit une tautologie. **Je retire ce témoin d'EXP-1.** Correction en (b).

### C-(a).3 — Tautologie du « dernier état » sous hygiène d'état (EXP-2) → **TRANSFORMÉE EN TEST** (c'est le contrôle n° 3 de C)

C a raison que **si** le contexte est tronqué entre actions (hygiène P §9), la base (iii) dernier état est aveugle aux actions 1…T−1 **par construction mécanique**, et le duel devient vrai par construction en faveur de H_A — sans rien prouver. Mais la prémisse (le contexte est-il tronqué ?) n'est pas donnée dans les faits : P §9 dit « remises à zéro et filtrage » **entre épisodes** (moniteurs amnésiques entre épisodes), pas nécessairement **entre actions intra-épisode**. C glisse de l'un à l'autre.

Donc : ce n'est pas une faille fatale, c'est **une variable de conception à fixer puis à contrôler**. J'intègre le contrôle n° 3 de C comme **condition de validité d'EXP-2** : évaluer le dernier état avec (a) contexte complet 1…T et (b) contexte tronqué à T. La comparaison honnête est (a). Si le séquentiel ne bat que (b), l'accumulation externe est **redondante avec l'attention interne** — et c'est un résultat, pas un artefact.

### C-(a).4 — Oubli de l'agrégation max/longueur (√(2 ln K)) → **ACCEPTÉE, contrôle le plus important**

C a entièrement raison et c'est sa meilleure contribution. E[max de K scores] croît en √(2 ln K) même sur du bruit pur. J'appariais l'horizon en **nombre d'actions N**, jamais la **longueur en jetons K_t par action**. Toute sonde `max` est alors un détecteur de verbosité déguisé, et le CUSUM d'EXP-3 peut se déclencher sur une simple dérive de longueur. **Le contrôle n° 1 de C (pente du score max vs ln K nulle) devient un pré-requis dur de toute EXP utilisant max.** C'est le premier test zéro-dépense à faire.

### C-(a).5 — CUSUM inadapté si le cadrage est stationnaire dès t=0 (EXP-3) → **ACCEPTÉE comme correction d'instrument**

C a raison : si l'instruction d'évaluation/sandbagging est au prompt système, la série de scores est stationnaire dans le régime « évalué » dès t=1, et un CUSUM intra-épisode calibré sur la moyenne initiale de l'épisode ne verra **aucune** rupture — falsifiant H_A par erreur d'instrument, pas par biologie du modèle. Ma formulation « changement de régime » était mal posée pour le cas statique.

**Correction** : séparer deux questions. (i) *Rupture intra-épisode* (le comportement change-t-il **pendant** l'épisode, p. ex. quand l'organisme « réalise » qu'il est testé) → CUSUM pertinent, calibré sur un régime de référence **externe** (épisodes sûrs), pas sur le début de l'épisode suspect. (ii) *Décalage statique de niveau* (évalué vs réel, constant sur l'épisode) → ce n'est pas un problème de point de rupture mais un **test à deux échantillons** sur la distribution des scores, cadrage apparié. Mon EXP-3 mélangeait les deux ; je la scinde.

### C-(b) — Scénarios d'évasion par instrument → **TRANSFORMÉS EN TÉMOINS-ATTAQUES PRÉENREGISTRÉS**

Je n'accepte ni ne rejette : je **convertis**. Chaque évasion décrite par C est une attaque concrète et falsifiable — donc exactement le **témoin vrai adaptatif** qui manquait à EXP-4 et qui durcit EXP-1/2. Je les intègre nommément :
- **leurre d'attention** (contre `attention`) → témoin obligatoire d'EXP-4, et motive le contrôle n° 5 de C (ablation top-k des α) ;
- **lissage de pic / dilution** (contre `lineaire`/`perceptron` via MIL-max) → témoin diffus **légitime** (c'est le vrai biais diffus, pas une citation faussée) : il remplace mon témoin ponctuel retiré en C-(a).2 ;
- **substitution in-distribution** (contre `mahalanobis`) → témoin ;
- **compensation/oscillation** (contre le séquentiel) → **le** témoin décisif d'EXP-2 : un biais concentré sur 2 actions, compensé par hyper-honnêteté ailleurs, somme ≈ 0. Si le séquentiel somme-cumulée tombe là-dessus, H_A (EXP-2) est falsifiée. J'en fais le témoin-adversaire n° 1.
- **omission structurelle** (variable confondante omise, aucun pic positif) → c'est le cas le plus dur et il attaque **le construit même** : une omission ne produit pas d'activation « de commission ». Voir point d'intégrité ci-dessous.

### C-(c) — Cinq contrôles négatifs manquants → **QUATRE ACCEPTÉS, UN REQUALIFIÉ**

- n° 1 (longueur/distribution du max) : **accepté, pré-requis dur**.
- n° 2 (lecture passive vs génération active) : **accepté, préalable à EXP-1**.
- n° 3 (position temporelle / cache KV) : **accepté, condition de validité d'EXP-2**.
- n° 4 (perplexité / charge cognitive) : **accepté**. Témoin faux = épisodes honnêtes **cognitivement difficiles**, appariés en perplexité. Si les sondes s'allument là, elles mesurent les « enjeux élevés »/l'incertitude (P §8.1), pas l'intention. C'est une dissociation de construit que j'avais sous-spécifiée en Q2.
- n° 5 (ablation top-k argmax) : **accepté comme test de fragilité structurelle** (l'angle mort Tr, P §5), **mais requalifié** : C en fait un contrôle négatif ; je le traite comme **mesure de robustesse de l'agrégateur** dans EXP-4. Nuance : si masquer 1–2 jetons sur 300 effondre le score, la sonde a un point de défaillance unique → elle cède au leurre/lissage. Si le score tient, l'agrégation est distribuée. Les deux issues falsifient quelque chose : c'est un duel, pas un simple garde-fou.

### Ce que je **rejette** de C

**Rejet 1 — « le duel EXP-2 est vrai par construction en faveur de H_A ».** Faux en général. Il ne l'est **que si** le contexte est tronqué entre actions, ce qui n'est pas établi par les faits (P §9 parle d'amnésie *entre épisodes*). Avec contexte complet 1…T, la base (iii) voit les actions antérieures *via* l'attention causale, et peut parfaitement égaler le séquentiel — c'est l'issue qui falsifie H_A. C confond une variable de conception non fixée avec une tautologie.

**Rejet 2 (partiel) — « apparier la surface détruit nécessairement le résidu d'intention » (C-a.1).** C'est une affirmation causale aussi forte que celle qu'elle m'attribue. Elle présuppose que le résidu d'intention n'est pas récupérable en génération contrainte. C'est mon S1, qui est **ouvert**. Je ne l'accepte donc pas comme fait, seulement comme risque — et je le teste par l'appariement à la génération.

---

## (b) Expériences corrigées

Changements transversaux appliqués partout : **appariement en longueur-jetons K_t par action** (pas seulement N) ; **pré-requis C-n°1** (pente score-max vs ln K ≈ 0) avant tout usage de `max` ; **contexte explicité** (complet vs tronqué) ; **témoins vrais = attaques diffuses de C**, plus de citation ponctuelle.

### EXP-0 (nouvelle, zéro-dépense, bloquante) — Le max est-il un détecteur de longueur ?

- **H_A** : à bruit/honnête apparié, le score `max` des sondes est invariant à K (pente vs ln K ≈ 0).
- **H_B** : le score `max` croît en √(2 ln K) → détecteur de verbosité.
- **Grandeur** : pente de régression du score-max sur ln K, sans unité ; K ∈ {50,100,200,500} jetons (illustratif).
- **Nul** : activations de bruit gaussien apparié en covariance → doit reproduire exactement √(2 ln K) (sert à calibrer la correction).
- **Témoin** : honnêtes réels de longueurs variées.
- **Garantie/seuil** : H_A tenue si |pente| borne-haute < seuil préenregistré **après** correction du score-max par le quantile attendu sous bruit (correction de type Gumbel). **Arrêt dur** : si la pente reste significative après correction, toute sonde `max` est recalée avant EXP-1/2.
- **Coût** : processeur, zéro dépense (sondes figées P3, vecteurs T0.5 — D point 5). VÉRIFIÉ dans les faits.

### EXP-1 corrigée — Signal interne vs surface, **par appariement à la génération**

- **H_A** : le signal est dans h_ℓ au-delà de la surface **et** du sujet lexical.
- **H_B** : corrélat de surface/sujet ; s'effondre au plancher à surface appariée.
- **Changement clé** : plus de paraphrase tierce relue en teacher-forcing. L'**organisme génère** sous deux consignes produisant la **même surface cible** (longueur/format contraints) : intention de biais présente vs absente. On lit les activations **en génération active** dans les deux cas.
- **Contrôle C-n°2 (obligatoire)** : comparer score sur h_ℓ (A génère biaisé) vs h_ℓ (organisme honnête **lit/réécrit** ce texte en teacher-forcing). **Même score élevé aux deux ⇒ la sonde lit le sujet, pas l'intention** → H_B. Score élevé seulement en génération active ⇒ résidu d'intention.
- **Témoin vrai** : **dilution/lissage de pic** (attaque C) et **omission structurelle** (attaque C) — biais diffus réels, pas ponctuels.
- **Témoin faux** : honnêtes appariés longueur **et K_t** et format, **plus** honnêtes cognitivement difficiles appariés en perplexité (C-n°4).
- **Bases mécaniques à battre** : longueur+ponctuation ; TF-IDF ; **+ perplexité du modèle** (nouvelle base, issue de C-n°4).
- **Seuil** : H_A tenue si AUROC(génération active) bat les trois bases mécaniques **et** le plancher covariance de ≥ 0,10, borne basse appariée > 0, **et** si score(génération active) − score(lecture passive) > 0 (dissociation intention/sujet).
- **Issue falsifiant H_A** : effondrement au plancher à K/perplexité appariés, **ou** score identique génération/lecture → détecteur de format/sujet.

### EXP-2 corrigée — Valeur ajoutée séquentielle, **avec contexte contrôlé et témoin-compensation**

- **Dédoublement de G1 (je maintiens, C ne l'attaque pas) :** **G1a** = séquentiel vs noir (lire l'intérieur apporte) ; **G1b** = séquentiel vs {dernier état, cascade} (notre accumulation bat les autres lectures). Sans dédoublement, D point 1 reconnaît l'issue non interprétable.
- **H_A** : un biais réparti sous le seuil par action reste détectable par l'agrégateur séquentiel calibré, invisible au dernier état **à contexte complet** et au max marginal.
- **H_B** : gain = artefact d'horizon ; à FP, **K_t** et horizon appariés, le dernier état à contexte complet fait aussi bien.
- **Contrôle C-n°3 (condition de validité)** : base (iii) évaluée en (a) contexte complet 1…T et (b) tronqué à T. **La comparaison probante est (a).** Si le séquentiel ne bat que (b), l'accumulation externe est **redondante avec l'attention interne** → résultat, non artefact.
- **Témoin vrai décisif (attaque-compensation de C)** : biais concentré sur 2 actions, compensé par hyper-honnêteté ailleurs, somme centrée ≈ 0. **Si la somme-cumulée rate ce cas**, H_A est falsifiée. J'ajoute donc un agrégateur **non-compensatoire** (p. ex. statistique sur le **sur-seuil cumulé** / nombre d'excursions, pas seulement la somme signée) et je les oppose : c'est un sous-duel interne.
- **Nul** : FP séquentiel sur épisodes honnêtes entiers, **sans puis avec corrélation bénigne injectée** (D point 5) — processeur, zéro dépense.
- **Garantie** : processus e / Ville, FP valide à tout temps d'arrêt.
- **Seuil** : H_A tenue si rappel_séquentiel − rappel_dernier-état(contexte complet) ≥ 0,15 à 1 % FP, K apparié, borne basse > 0, **et** FP séquentiel sous corrélation bénigne < 2 %, **et** l'agrégateur retenu attrape le témoin-compensation.
- **Issue falsifiant H_A** : dernier état (contexte complet) ou max marginal égale le séquentiel à K/horizon apparié → G1b échoue.

### EXP-3 corrigée — **Scindée** : décalage statique vs rupture intra-épisode

- **EXP-3a (statique, deux échantillons)** : même contenu, **cadrage évalué vs réel** ; test à deux échantillons sur la distribution des scores (pas CUSUM). Dissociation croisée (Q2) : Δ(même contenu, cadrage différent) vs Δ(même cadrage, contenus différents) vs permutation d'étiquettes.
  - **H_A** : décalage imputable à l'intention, persiste à cadrage apparié. **H_B** : répond au cadrage/contexte, disparaît à cadrage apparié.
- **EXP-3b (rupture intra-épisode, CUSUM corrigé)** : CUSUM calibré sur un **régime de référence externe** (épisodes sûrs), **pas** sur le début de l'épisode suspect (correction de l'erreur signalée par C). Pertinent seulement si l'on cherche un basculement *en cours* d'épisode.
- **Pré-requis** : EXP-0 passée (sinon la dérive de K déclenche le CUSUM — faux régime, exactement l'objection C-a.4/a.5).
- **Témoin vrai** : sandbagging **induit** (van der Weij 2024, RAPPORTÉ) — seul témoin disponible, le spontané ≤ 8B n'étant pas établi (E §3.4). **Je maintiens que le résultat le plus probable est décisif négatif** (la sonde « conscience d'éval » mesure le contexte) et doit être accepté symétriquement (P §12).

### EXP-4 corrigée — Frontière de robustesse, **avec fragilité structurelle et attaques de C**

- **H_A** (HC4+H6) : déplacer le verdict exige une obfuscation d'activations coûteuse ; il existe λ (paraphrase, reset, bruit) où le succès d'attaque chute plus vite que l'utilité.
- **H_B** : l'organisme déplace le verdict à coût d'utilité négligeable, sans accès aux poids.
- **Témoins vrais = attaques de C**, nommées et préenregistrées : leurre d'attention, lissage de pic, substitution in-distribution, compensation, omission structurelle.
- **Test de fragilité structurelle (C-n°5, requalifié en duel)** : masquer les k∈{1,2,3} jetons de score/α maximal et recalculer.
  - **H_A'** : l'agrégation est distribuée (score tient). **H_B'** : point de défaillance unique (score s'effondre → cède au leurre/lissage).
- **Grandeur** : g = fraction du chemin vers v* (P §4) ; coût = perte d'utilité (métrique à préenregistrer, **illustratif** tant que non fixée) ; pente succès/utilité sous λ.
- **Garantie** : matrice de transfert d'attaque (P §8.2).
- **Seuil** : H_A tenue si g ≈ 0 sous contenu boîte noire (|g|<0,1) **et** auto-incrimination g<0 sous manipulation (HC2b) **et** score robuste à l'ablation top-2. Fermeture d'une brèche prouvée seulement si transfert attaque-optimisée → extension < 0,2.
- **Issue falsifiant H_A** : g>0,3 à coût quasi nul, **ou** effondrement à l'ablation top-1/2 → sondes corruptibles par le registre / point de défaillance unique.

---

## Point d'intégrité non résolu par les corrections

L'attaque **« omission structurelle »** de C touche une limite que mes corrections n'effacent pas : un biais par **omission** (variable confondante absente, test sous-puissant choisi) ne produit pas nécessairement d'activation « de commission » positive. Les sondes du programme sont des détecteurs de **présence** d'une direction (tromperie, dissimulation) ; l'absence d'un concept correct n'a pas de signature évidente. Si EXP-1 montre que le signal diffus **de commission** existe mais que l'**omission** reste au plancher, alors le périmètre revendiqué du moniteur doit explicitement **exclure le sabotage par omission** — ou le programme doit construire une sonde de **complétude** (comparaison à un référentiel de ce qui *aurait dû* être dit), qui n'est pas dans la pièce F. **Je ne peux pas trancher avec les faits ;** je le signale comme limite de construit, non comme résultat.

---

## (c) Réponse à l'arbitre — une page

**Ce qui est établi (dans les faits transmis).**
- La règle d'agrégation `max`/`attention` (jamais moyenne) et les familles de sondes (F) — VÉRIFIÉ comme spécification.
- Le dédoublement nécessaire de G1 (a/b) découle directement de D point 1 (« un échec ne dira pas laquelle a échoué ») — c'est une conséquence, non une opinion.
- La mesure zéro-dépense (FP séquentiel sur honnêtes, sans/avec corrélation) est disponible sur processeur (D point 5) — VÉRIFIÉ.
- La littérature pertinente (Apollo 2025 70B ; Nguyen 2025 ; van der Weij 2024 ; Berglund 2023 ; Laine 2024) est RAPPORTÉE, chiffres à vérifier sur PDF (R7). L'étude multi-modèles 2026 et « Llama Scope » restent **référence à vérifier**.

**Ce qui n'est pas établi.**
- S1 (le biais diffus existe et est étiquetable dans h_ℓ d'un 8B) et S4 (il est spontané, non induit) restent HYPOTHÈSE (E §3.3–3.4). C'est le risque n° 1, avant la robustesse.
- S2 (lien causal représentation « conscience d'éval » → comportement) : HYPOTHÈSE (E §3.5, « mécanisme causal non élucidé »). EXP-3a vise surtout un **décisif négatif**.
- La transposition token→action de la robustesse max/attention (Tr) reste non calibrée.
- Le **sabotage par omission** peut être hors de portée de construit des sondes de présence (limite non résolue).

**Ce qui change après C.** J'accepte quatre des cinq contrôles de C comme pré-requis durs (longueur/max, génération vs lecture, contexte KV, perplexité), je requalifie le cinquième (ablation top-k) en duel de robustesse, et je transforme ses cinq scénarios d'évasion en **témoins-attaques préenregistrés** — ils remplacent mon témoin ponctuel erroné. Je rejette la thèse « EXP-2 vrai par construction » (elle ne vaut que sous troncature de contexte, non établie) et la thèse « la paraphrase détruit nécessairement l'intention » (c'est S1, ouvert).

**L'expérience à faire en premier.** **EXP-0** (le max est-il un détecteur de longueur ?), puis **EXP-2 nul** (FP séquentiel sous corrélation bénigne). Les deux sont **zéro-dépense** (processeur, D point 5), et toutes deux sont **bloquantes** : si le max dérive avec K après correction, toute sonde `max` est invalide et EXP-1/3 mesureraient un artefact ; si le séquentiel émet >5 % de FP sous corrélation bénigne, G1 ne doit rien consommer avant recalibration. On ne génère aucune trajectoire 8B (coût GPU, **non chiffré dans les faits — tout montant serait illustratif**) tant que ces deux garde-fous ne sont pas franchis.

**Ce qui me ferait changer d'avis.** Une publication sur la détection boîte blanche du biais diffus ≤ 8B ou sur les sondes séquentielles (veille E §6) ; une rupture de régime robuste au cadrage apparié en EXP-3a (révise S2) ; l'égalité dernier-état/séquentiel à contexte complet apparié en EXP-2 (abandonne H2, reformule G1).

FIN-DE-CELLULE