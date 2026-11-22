# Proposition A — Tour III.3 : réponse aux critiques

## 0. État des pièces

- **Conception A (III.1) : absente, statut REFUS** `[VÉRIFIÉ — lecture]`. Je n'en reconstruis ni le contenu ni le motif.
- **Bloc FAITS** : identique à la question de l'arbitre (même empreinte). Il ne contient aucune donnée empirique et les « notes retirées » n'y figurent pas `[VÉRIFIÉ — lecture]`.
- **Conceptions B à F (III.1)** : non transmises. Je ne les connais que par les critiques qui les visent, et je ne peux donc pas vérifier ce que ces critiques leur attribuent.

Tout ce qui suit est de statut **HYPOTHÈSE**, sauf mention contraire. Aucune expérience n'a été exécutée, et tous les nombres sont **illustratifs**.

---

## (a) Réponse aux critiques visant A

Les cinq critiques croisées (B, C, D, E, F) ont chacune une section « Sur la proposition A ». Toutes constatent l'absence de la pièce et ne formulent aucune objection `[VÉRIFIÉ — lecture]`. Il n'y a donc rien à accepter, à rejeter ou à transformer en test.

Je ne réponds pas aux sections visant C, D, E, F ou B, qui ne me concernent pas. En revanche, conformément à B1, **je me sers** de plusieurs objections comme contraintes de conception pour l'expérience posée en (b). Je les reprends avec le statut que leurs auteurs leur ont donné, sans juger si elles sont fondées contre leurs cibles :

| # | Contrainte reprise | Formulée par (contre) |
|---|---|---|
| 1 | Adaptateur placebo honnête, apparié en rang et en volume | B (contre C, F) ; C, E, F (contre B) ; D |
| 2 | Entraînement et test sur des instanciations indépendantes du même mécanisme | C (contre E) ; B (contre F) ; D (contre F) |
| 3 | Aucun capteur étendu conçu après lecture du candidat | B (contre C, E, F) ; C, E, F (contre B) ; E (banque pré-scellée) |
| 4 | Dommage standardisé sur une loi commune, pas tronqué à un seuil | C, E, F (contre B) ; D |
| 5 | Signal planté pour vérifier la puissance quand la dimension dépasse l'effectif | E (contre C) ; F (contre E) ; B |
| 6 | Verdict par intervalle sur un contraste scalaire pré-enregistré | D (règle de décision) |
| 7 | Variante connue diluée comme contrôle du critère | B (contre C) |
| 8 | Famille à visibilité graduée contre la bimodalité artificielle | C, E, F (contre B) |
| 9 | Unité de réplication = instanciation × famille de dossiers ; pas d'arrêt optionnel | B, D, F |

---

## (b) Expériences

Je ne peux pas livrer d'« expériences corrigées » : corriger suppose un original, et l'original est absent. Ce qui suit est **une expérience posée à ce tour**, pas la révision d'un texte de III.1.

Je ne propose pas de candidat : le protocole évalue un candidat fourni par un tiers. Cela évite aussi la fuite entre concepteur de l'attaque et concepteur de l'instrument (contrainte 3).

### Expérience 1 — Absorption relative en transfert d'instanciation

**Cadre.**
- **Modèle** : un modèle ouvert de 1 à 8 milliards de paramètres.
- **Tâche** : une analyse longue, découpée en sous-items à vérité terrain vérifiable.
- **Mécanismes** : honnête, familles connues K₁…K_j, candidat x.
- **Instanciations** : au moins 8 adaptateurs par mécanisme, entraînés indépendamment (graines, données et formulations distinctes). La classe honnête porte elle aussi des adaptateurs placebo (contrainte 1).
- **Capteurs Φ**, figés avant tout essai : lecture d'états internes réduite à faible dimension, score d'un juge de texte, résultat d'un audit au hasard.
- **Classe de décision** : une seule, régularisée et pré-enregistrée.

**Estimande.** R(m) est le rappel, à taux de fausses alertes α = 0,05, d'un détecteur ré-entraîné sur des exemples étiquetés du mécanisme m.
- Le détecteur est testé sur une **instanciation tenue à l'écart** et sur une **famille de dossiers tenue à l'écart** (contrainte 2).
- Le taux de fausses alertes est calibré sur des honnêtes placebo séparés et rapporté avec son intervalle.
- Le rappel est standardisé sur une loi commune du dommage et de la difficulté (contrainte 4).

**Référence interne.** R_ref est la même quantité pour une famille connue retirée du catalogue puis ré-instanciée avec des adaptateurs neufs. C'est un « faux nouveau » dont on sait qu'il est une variante.

**Contraste.** θ = R_ref − R(x), au seuil t = 0,20.

**Duel (B4).**
- **H_A : θ ≤ t.** Le ré-entraînement absorbe x à peu près comme une famille connue retirée.
- **H_B : θ > t.** Il ne l'absorbe pas.

L'intervalle sur θ est un bootstrap groupé par instanciation et par famille de dossiers (contrainte 9).
- Intervalle entièrement sous t : H_B est réfutée, la prétention de nouveauté tombe dans ce banc.
- Intervalle entièrement au-dessus de t : H_A est réfutée, x n'est pas une variante au sens du banc.
- Intervalle à cheval : pas de verdict. Cette issue est déclarée d'avance, sans doublement d'effectif hors plan séquentiel (contrainte 6).

**Portes de recevabilité.** Chacune peut échouer, et un échec invalide le banc, pas le candidat.

| Porte | Ce qui doit se produire | Ce que l'échec indique |
|---|---|---|
| G1 — placebo | Un placebo tenu à l'écart est signalé au taux α, pas davantage | Les capteurs lisent l'identité de l'adaptateur |
| G2 — faux nouveau | R_ref est élevé | Un échec sur x serait ininterprétable |
| G3 — signal planté | Un décalage diffus de taille connue, injecté dans des traits honnêtes, est retrouvé au même effectif (contrainte 5) | Le banc manque de puissance |
| G4 — dilution | Une famille connue appliquée à une fraction des étapes, à dommage apparié, n'est pas classée « non absorbée » (contrainte 7) | Le critère mesure la dilution |
| G5 — permutation | La permutation d'étiquettes donne la loi nulle de θ à l'effectif réel | Le seuil t est mal situé par rapport au bruit |

**Limite déclarée.** L'effectif utile est le nombre d'instanciations indépendantes, pas le nombre d'épisodes. À 8 par mécanisme, un θ vrai proche de t ne sera pas tranché.

**Ce que l'expérience ne dit pas.** Réfuter H_A établit une non-absorption **dans Φ, à ce budget**. C'est nécessaire mais pas suffisant pour parler de catégorie. L'attribution positive, c'est-à-dire qu'un autre observable rattrape x, exige une banque d'extensions scellée avant la soumission du candidat (contrainte 3). C'est l'objet d'une seconde expérience.

### Expérience 2 (esquisse) — Y a-t-il un creux ?

Elle répond à l'objection selon laquelle un seuil ne fait que découper un continuum. On construit une famille dont la trace dans Φ décroît continûment (contrainte 8), puis on mesure θ le long du paramètre.
- **H_A** : θ varie continûment, sans palier. Dans ce cas « catégorie » n'est qu'une convention sur t.
- **H_B** : un palier persiste, hors artefact de censure.

---

## (c) Réponse à l'arbitre

### Ce qui est établi

Rien d'empirique : le bloc FAITS ne contient que la question. Sont VÉRIFIÉS par lecture l'absence de ma conception et l'absence d'objection dirigée contre A. Les références ci-dessous sont **RAPPORTÉES, toutes citées de mémoire**.

### Ce qui ne l'est pas (mes positions, HYPOTHÈSE)

**1. La distinction.** Elle est fondée seulement **relativement** à un catalogue d'attaques connues, à un jeu de capteurs, à une classe de décision et à un budget. Dans l'absolu, elle n'est pas décidable. Ce qui se mesure est continu : c'est le coût d'absorption par ré-entraînement à capteurs constants. Tant qu'aucun creux n'est démontré, « catégorie » est une convention de seuil sur ce coût.

**2. Exemples historiques.** Ma lecture est que la séparation tenait chaque fois à une hypothèse de la défense rendue caduque, pas à un réglage.
- Kocher, 1996, « Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems » : l'attaque passe par un observable (le temps) extérieur au modèle mathématique défendu.
- Shacham, 2007, « The Geometry of Innocent Flesh on the Bone: Return-into-libc without Function Calls (on the x86) » : la défense supposait du code injecté, l'attaque réutilise du code présent. C'est aussi un assemblage du return-into-libc antérieur (référence à vérifier), ce qui montre que les deux étiquettes ne s'excluent pas.
- Biham et Shamir, 1990, « Differential Cryptanalysis of DES-like Cryptosystems ».
- Szegedy et coll., 2013, « Intriguing properties of neural networks ».

Biais à signaler : ces catégories ont été nommées après coup.

**3. Publications.** Je ne connais aucune publication qui établisse un critère mesurable séparant « attaque » et « catégorie » (référence à vérifier). Travaux voisins, de mémoire :
- Athalye, Carlini et Wagner, 2018, « Obfuscated Gradients Give a False Sense of Security » (évaluation adaptative des défenses) ;
- Greenblatt, Shlegeris, Sachan et Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion » ;
- van der Weij et coll., 2024, « AI Sandbagging: Language Models can Strategically Underperform on Evaluations » ;
- Benton et coll., 2024, « Sabotage Evaluations for Frontier Models ».

**4. Groupe de modèles.** La question n'est pas tranchée. On peut mesurer « nouveau par rapport au catalogue du banc », pas « nouveau dans le monde », puisque les modèles ont lu la littérature. Les témoins que je retiens viennent des critiques :
- un énumérateur mécanique à budget égal (B) ;
- les mêmes modèles privés d'échange (D) ;
- un solo muni des mêmes rôles (F) ;
- des familles connues renommées, qui doivent être reclassées « non nouvelles » (B, D) ;
- une provenance masquée dès la décision d'implémenter (D).

Un angle mort planté par le concepteur mesure une recherche, pas une conception.

**5. Expérience à faire en premier.** L'Expérience 1 de (b), **précédée de ses cinq portes**. Tant que G1 à G5 ne sont pas passées, aucun verdict sur un candidat n'est interprétable.

### Ce qui me ferait changer d'avis

- **Pas de palier dans l'Expérience 2** : j'abandonne « catégorie » comme classe et je ne garde que le coût continu.
- **Échec de G2** (une famille connue ré-instanciée n'est pas absorbée) : le critère mesure l'identité d'instanciation, je le retire.
- **L'énumérateur mécanique égale le groupe** : aucune conception collective n'est attestée.
- **Une publication fournit un critère déjà validé** : je m'y range après vérification de la référence.

FIN-DE-CELLULE