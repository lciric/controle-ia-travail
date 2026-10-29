# Question de la course 2 — axe 6, texte II (« hypothèses fragiles des statistiques ») — v2 (brouillon, non contre-lu, non servi ; QUARANTAINE)

Lignée session-depot (instance 2), 29 octobre 2026. **v2 = v1 (`docs/notes/ideation-organisme-v1/course-2/axe-6-texte-II-v1.md`, `1d5612ab…`, sur `main`) plus une liste de pistes, au niveau des classes, reprise du résumé de la réponse BA-002 d'Opus 5.5 reçu par la session (R-790)**, sur mot direct de Lazar (29 octobre ≈ 22:35 UTC, verbatim : « l’axe 6, consacré aux lois de probabilité, en m’appuyant sur ma question BA-001 et sans reprendre le résumé reçu en R-790. : tu peux le reprendre »). Seuls des noms de classes et de sous-types, et des références publiées, sont repris ; **aucun paramètre, aucune valeur numérique, aucun code de mode**. Le fichier de réponse BA-002 n'a pas été ouvert.
**Cette version porte du contenu dérivé de BA-002 : elle vit sur la branche de quarantaine `donnees/course-2-axe-6-v1`, jamais sur `main`.** Service, sorties et interface : comme la v1 (sous-session séparée ; quarantaine ; lecteur tenu à l'écart ; comptes et classes vers la défense).
**À faire avant service** : contre-lecture R2 par un Opus neuf tenu à l'écart (R-785) ; mesure du texte servi ; devis et GO.

<!-- DEBUT-TEXTE-SERVI -->
# Course d'idéation — question « hypothèses fragiles » — génération g

**Garde.** Niveau des lois de probabilité. Aucune fiche ne décrit une conduite d'agent, une consigne, une séquence d'actions, ni un procédé concret pour produire un déplacement. Une telle fiche est écartée avant le juge et comptée. Les déplacements synthétiques sont des opérations sur des lois ou des échantillons (rééchantillonnage pondéré, couplage, perturbation d'une loi d'activations), jamais des comportements.

## Glossaire (vaut définition)
- **Suite d'actions** X = (a_1, …, a_T) : textes produits par un agent ; un modèle de langage ouvert M, fixé, lit X et produit des **activations** h_{t,ℓ,p} (action, couche, position), fonction déterministe de X.
- **Statistique de surveillance** S : boîte noire S(X), ou boîte blanche S(X, H_Π(X)) sur un ensemble fini de **positions lues** Π. L'agrégation se fait **par maximum ou par attention** (poids dépendant des activations, concentrés sur peu de positions), jamais par moyenne uniforme. La décision est un seuil, ou un **test séquentiel** à e-valeurs (martingale de test, rejet au-delà de 1/α).
- **Loi de référence** P_0 : loi des suites honnêtes, connue par n suites ; le seuil est étalonné au niveau α sur elles.
- **Déplacement diffus** {P_ε} : P_0 en ε = 0 ; effet par action d(P_ε(a_t | a_<t), P_0(a_t | a_<t)) ≤ ε ; effet cumulé d(P_ε^(T), P_0^(T)) non négligeable (d : variation totale, Hellinger ou Kullback-Leibler).
- **Invisible** : puissance P_ε(S > s_α) ≤ α + δ.
- **Hypothèse porteuse** : propriété de P_0, ou de la relation entre P_0 et S, dont dépend l'étalonnage ou la puissance de S. Exemples : stationnarité, indépendance conditionnelle entre actions, exhaustivité des positions lues, linéarité d'un trait, homogénéité des suites honnêtes, étalonnage sur n fini.
- **Statistique riposte** : statistique qui retrouve de la puissance contre une classe donnée, avec un prix nommé contre les autres classes.

## Règles
Les chiffres sont repris d'une source citée (titre, auteurs, année, page) ou marqués SUPPOSÉ. Aucune donnée n'est réclamée : ni familles d'épisodes, ni statistiques ou directions du programme, ni résultats. Les références seront vérifiées sur le document original ; une référence inexacte vaut moins qu'une absence. Un refus arrête votre tour.

## Axe 6 — Hypothèses fragiles des statistiques
Pour une **classe** de statistiques (accès, agrégateur, positions lues, étalonnage), jamais pour une sonde particulière, nommez l'hypothèse porteuse dont dépend sa puissance, et la classe de lois déplacées sous laquelle elle tombe.

Obligatoires :
- (a) la classe de statistiques visée, définie dans le cadre ci-dessus ;
- (b) l'hypothèse porteuse, énoncée formellement ;
- (c) la classe de déplacements diffus, définie formellement, et la **condition mesurable** sur P_0 et S qui la rend invisible ;
- (d) la borne ou l'impossibilité, avec son énoncé et sa preuve esquissée, ou un théorème cité avec ce qu'il laisse ouvert ;
- (e) la statistique riposte, avec un minorant de puissance en ε, T, n et d, et son prix contre les autres classes ;
- (f) un test préenregistrable, sur suites honnêtes et déplacements synthétiques au niveau des lois : protocole, graines, résultat attendu, résultat qui réfute la riposte. La première expérience tourne sur processeur seul ;
- (g) une **quantité mesurable sur P_0 seule**, sans aucune loi déplacée, qui dit si l'hypothèse tient, avec la valeur qui la confirme et celle qui l'infirme.

Facultatifs :
- les combinaisons de classes ;
- la dépendance en n de l'étalonnage ;
- l'ordre dans lequel les hypothèses cèdent quand ε croît.

Pistes, non limitatives, que les fiches doivent dépasser ou rendre précises (une fiche qui ne fait que reprendre une piste sans hypothèse porteuse nouvelle n'est pas notable) :
- déplacement de moyenne, y compris porté par une direction orthogonale à celle qu'une statistique linéaire lit ;
- déplacement de covariance à moyenne égale, invisible à toute statistique linéaire du premier ordre ;
- déplacements portés par les orbites d'un groupe sous lequel la statistique est invariante (théorie de Hunt et Stein) ;
- dépendance temporelle modifiée à marginales égales (copule entre actions, chaîne de Markov d'ordre supérieur) ;
- mélanges clairsemés ou denses, près de la frontière de détection (critique supérieure de Donoho et Jin) ;
- non-stationnarité : dérive lente, composante périodique, salve concentrée sur une fenêtre ;
- déplacement hors des positions lues ; déplacement dans le noyau de l'agrégateur (maximum, attention) ;
- déplacement de queue (queue lourde, asymétrie, troncature) à corps de loi inchangé ;
- **combinaisons** dont l'invisibilité est synergique : aucune des statistiques spécialisées ne détecte seule, la combinaison reste visible à une statistique jointe.
Matériau, non imposé : tests à deux échantillons en grande dimension (Bai et Saranadasa ; Chen et Qin), combinaison d'e-valeurs (Vovk et Wang ; Ramdas et coauteurs), valeurs propres extrêmes (Johnstone), copules (Sklar ; Genest et Rémillard), test de normalité multivariée (Anderson). Références à vérifier sur le document original.

Non noté : toute fiche dont (c) ou (f) exige de produire une loi déplacée par un agent plutôt que par une opération sur des lois.

**Fiche** (3 000 à 8 000 caractères ; « sans objet » avec sa raison si un champ est inapplicable) :
- titre ;
- classe de statistiques ;
- hypothèse porteuse ;
- classe de déplacements ;
- condition d'invisibilité ;
- borne ou impossibilité ;
- riposte et prix ;
- test (f) ;
- quantité (g) ;
- prédiction chiffrée et signée (borne, ou puissance prédite en simulation à ε, T et n donnés) ;
- coût (heures de processeur, dollars) ;
- antériorités (au plus cinq : titre, auteurs, année, ce qui y est démontré) ;
- critère de mort ;
- SUPPOSÉ.

**Juge** (binaire) :
- K1 : (a) à (g) présents.
- K2 : condition (c) mesurable, c'est-à-dire écrite comme une égalité ou une borne sur des lois images.
- K3 : prédiction chiffrée et signée.
- K4 : critère de mort à seuil numérique, et première expérience sur processeur.
- K5 : antériorités au format.

Notable : K1 à K5 vrais. Un **témoin planté**, notable par construction, est glissé anonyme ; s'il n'est pas classé notable, la notation est fautive.

**Déroulé** : au plus deux fiches par proposeur. En passe 2, sur les fiches anonymes de l'autre fournisseur : seulement marquer un champ faux (preuve jointe) ou ajouter une antériorité.

## Critère de mort de l'axe
L'axe n'a rien donné si l'une de ces conditions est remplie :
- aucune fiche notable ne porte une condition (c) et une quantité (g) vérifiables ;
- toutes les fiches notables reprennent des classes classiques (déplacement de moyenne, mélange) sans hypothèse porteuse nouvelle ;
- le témoin planté échoue.
<!-- FIN-TEXTE-SERVI -->

## Hors texte servi — interface et lecture
- Fiches scellées sur une branche `donnees/course-2-axe-6-*`, jamais sur `main`.
- Lecture par le lecteur tenu à l'écart (N-054).
- Vers la défense, après contrôle lexical, seulement :
  - le nombre de fiches notables par classe d'hypothèse porteuse et par classe de déplacement ;
  - le nombre de fiches écartées par la garde.
- Transmettre les quantités (g) à la défense serait plus que « comptes et classes » : c'est un nœud pour Lazar, non tranché ici.
- R-750 : en cas de refus, au plus trois questions de repli, chacune différente et plus étroite, scellée avant service.
