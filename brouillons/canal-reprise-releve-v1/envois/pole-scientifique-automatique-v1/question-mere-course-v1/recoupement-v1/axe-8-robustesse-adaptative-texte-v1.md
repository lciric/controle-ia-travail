# Course 2 — texte I (question « défense ») — axe 8 « robustesse adaptative », texte à insérer — v1

**Statut : brouillon, non servi, non scellé.** Non contre-lu (contre-lecture R2 par un modèle d'un autre fournisseur avant toute insertion).
Rédacteur : lignée conv-audit, rédacteur neuf, modèle Claude Opus 5.5. Date relevée avant l'écriture (`date -u`) : **2026-11-01 16:04 UTC**.
Mandat : R-1037 (Lazar, 09:22 UTC : chapitre 8 « on le prend » pour la course 2 ; conv-audit le rédige « au format des sept autres ») ; R-743 (côté défenseur, niveau méthode, aucune recette ; un troisième arrêt clôt le sujet) ; R-744 (option (b) : texte tiré de la synthèse du collisionneur sur N10) ; R-1056 (lancement de cette rédaction).

**Fichiers lus (empreintes `sha256sum` relevées à 16:04 UTC) :**
- `question-course-2-defense-fusion-v5.md` — `a750144963913ba1c3dcf3eed5d4f8322d7d0246135e17c95ac8e7253c2dd680` (concorde avec son `.sha256`)
- `analyse-approfondie-axe-8-robustesse-v2.md` — `87e373095e1a15fd41839a63d4f3271acf06683c42bf5b6cae13e05c53b56d51` (concorde avec son `.sha256`)
- Synthèse du collisionneur, tour 1, section N10 (lignes 274 à 300), copie hors dépôt `scratchpad/main-lecture/synthese-noeuds-v12-tour1-v1.md` — `e4d5a5c94c37534a7481772af2f1150f325be38c46c356353520c44cf2f85aa5`
- Synthèse du collisionneur, tour 2, section « # N10 » (lignes 236 à 247, et lignes 117, 286, 330), copie hors dépôt `scratchpad/sd-syntheses/synthese-noeuds-v12-tour2-v1.md` — `da839da51678bc1e1eefd53e075b4b3f181e8d54ae9570e8f3e50eb714769e6a`
  (ces deux empreintes figurent dans des fichiers du dépôt, notamment `collisionneur-noeuds-31-octobre-v1/relecture-opus-synthese-noeuds-v12-tour1-v1.md` et `…-tour2-v1.md`)
- `registres/decisions.md` (lignes R-339, R-486, R-742, R-743, R-744, R-1037, R-1047, R-1056 seulement) — `a409330aa8eda94c0ab996d9131c771b91e6fb1e4b1da39a24c98765a772cf73`
- `corpus-primaire-v5-integral/LISEZMOI-v2.md` (liste des 23 papiers, pour savoir si Bailey et collègues sont déjà une pièce) — `179f719aa3febae83503f644fee27cc62f14750a9eb986f4aebcbee8b8f2c3ea`

Non ouverts : textes II et III, `bras-attaque-v1/`, `donnees/`. Aucun appel réseau ni de modèle.

---

## 1. Texte à insérer

### 1.1 Bloc d'axe (après « Axe 7 », avant « Boucle entre générations »)

```
## Axe 8 — Robustesse adaptative : le prix imposé à un surveillé qui s'adapte
Livrable : une **fiche de mesure à préenregistrer**, pas un résultat ; adversaire synthétique, hors de la course (texte II) ; rien sur carte pendant la course. Quelle défense (statistique des axes 1, 4 ou 5, seule ou composée) rend l'évasion chère à un surveillé qui s'adapte, et comment un tiers le vérifie-t-il ?
Obligatoires : (a) **classe d'attaquants** nommée par son accès (boîte noire ; boîte blanche, nombre de couches lues) et ses budgets (référence, maximum, unité de coût), gelés dans la fiche, jamais par une technique ; l'attaquant vise la défense composite entière ; (b) le **levier** du défenseur (couches lues, couplage à la qualité de la tâche hors de l'espace interne, capacité de la classe de moniteurs, archive de réentraînement, sous-espaces nécessaires à la tâche) et la barrière visée : informationnelle (signal présent) ou computationnelle (déplacement coûteux) ; (c) **mesure** : front performance de la tâche × taux d'évasion par budget, aucun ratio ; fonction de décision et seuil gelés avant toute lecture ; constantes d'échelle (plancher d'utilité) calibrées sur les seuls honnêtes du pilote, puis gelées avant tout comparatif ; estimand stratifié par difficulté, honnêtes appariés exactement, toutes les tâches évaluées, dégénérescence rapportée et non filtrante ; fausses alertes comme pour G1 ; (d) trois **témoins** : sans défense, moniteur aux étiquettes permutées, filtre de difficulté seule (base à battre) ; prédiction signée sur la pente du front selon les couches lues ou la longueur de trajectoire ; (e) **portée et vérification** : un optimiseur local donne une borne haute de la valeur du jeu, jamais une borne basse du coût d'attaque ni une robustesse universelle ; résultat conditionnel à la classe ; un tiers sans accès à la conception rejoue sur poids figés et code empreintés, sans degré de liberté après scellement.
Facultatifs : rayon certifié du moniteur dans l'espace des activations, restreint aux déplacements qui conservent la tâche, vérifié par programme ; prix cumulé sur une menace diffuse ; dilemme entre lecture des activations et lecture de la sortie.
Matériau, non imposé : prix de l'évasion sur un modèle et une tâche (Bailey et collègues, p. 3, 23, 26 ; modèle entraîné à être surveillable : évasion renchérie, non fermée, p. 25-26) ; robustesse certifiée (CROWN) ; double oracle ; regret en ligne. Pilote « mélange d'équilibre » : [verdict à insérer avant service, ou ligne retirée] ; la pureté des poids est un plafond de la classe de moniteurs, non une preuve d'inutilité du tirage.
Une fiche qui décrit un contournement ou exige une entrée adverse est écartée avant la notation et comptée (règle « niveau méthode »).
```

Mesure du bloc (programme, entre les clôtures, clôtures exclues) : **2 761 caractères (2 883 octets), 6 lignes** ; phrase de boucle : 159 caractères. Voir § 4, réserve 1.

### 1.2 Phrase à ajouter à « Boucle entre générations » (après la phrase sur l'axe 7)

```
Une fiche de l'axe 8 nomme la statistique (axe 1, 4 ou 5) dont elle mesure la tenue et la faille de l'axe 3 que le prix mesuré fermerait ou laisserait ouverte.
```

Et, dans la première phrase de la boucle, la liste « (axes 1, 2, 4, 5, 7) » reste telle quelle : l'axe 8 a sa phrase propre parce que son vis-à-vis porte deux noms (statistique et faille), non un seul.

### 1.3 Entrée pour « Pièces (liste fermée) »

**Une pièce nouvelle, conditionnelle** : « verdict du pilote “mélange d'équilibre” (verdict seulement) », à ajouter seulement si le verdict est scellé et prononcé (R13) avant le service ; sinon **aucune**, et la ligne « Pilote “mélange d'équilibre” » du matériau est retirée. Bailey et collègues (arXiv 2412.09565v2) sont **déjà une pièce** : ils figurent parmi les 23 papiers (`corpus-primaire-v5-integral/LISEZMOI-v2.md`, ligne 27). CROWN n'est **pas** une pièce : il est nommé dans le matériau comme méthode, au même titre que « Mahalanobis » à l'axe 1 ; une fiche qui le cite en antériorité le marque « à vérifier » (K5).

### 1.4 Entrée pour l'annexe 2 (provenance)

Phrase à ajouter sous « Décisions du 30 octobre » :
« Décision du 1er novembre : axe 8 retenu pour la course 2 (R-1037, 09:22 UTC), rédigé du côté du défenseur, au niveau méthode (R-339, R-743), à partir de N10 (collisionneur, tour 1 et tour 2) et de l'analyse approfondie v2 de conv-audit (`87e37309…`). »

Lignes de tableau (au format « Bloc du texte servi | Provenance | Statut ») :

| Bloc du texte servi | Provenance | Statut (recoupement v2) |
|---|---|---|
| Axe 8 : existence, livrable « fiche de mesure à préenregistrer », adversaire hors course (texte II) | L (R-1037 ; R-743) ; CO N10 tour 1 et tour 2 (« pilote non lu », « préenregistrement ») | décidé par L (R-1037), contre la recommandation (b) du collisionneur (tour 1 : quatre espèces ; tour 2 : 0,55) |
| Axe 8 (a) classe par accès et budgets, cible composite | CO N10 tour 1 (D : sept grandeurs ; C : défense composite entière) ; tour 2 (C, D) | commun à trois au tour 2 (B, C, D, sous condition ; A de même nature) ; gel des budgets dans la fiche : choix de CA (voir écart) |
| Axe 8 (b) leviers, barrière informationnelle ou computationnelle | CO N10 tour 1, critère 18, leviers « contrôlés par le défenseur » (A, B, C, D ; sous-espaces : C seul) ; CA, analyse v2, § 1 (b), (f) | commun ; levier « modèle surveillable » laissé au matériau (classé « incertain », B requalifié par A) |
| Axe 8 (c) front sans ratio, gel de la fonction de décision, constantes d'échelle après le pilote, stratification, toutes les tâches | CO N10 tour 1, convergences (i), (ii), (iv) ; tour 2, D en T3 | commun ; divergence 11 du tour 1 **résolue au tour 2** (tour 2, ligne 286) |
| Axe 8 (d) trois témoins ; prédiction de pente | CO N10 tour 1, convergence (v) (D, repris par A, C) ; tour 2 (grille de budgets pour la pente : A sur D, repris par D) ; CA, analyse v2, § 1 (d) | commun |
| Axe 8 (e) borne haute seulement ; vérificateur hors programme | CO N10 tour 1, convergence (iii) et critère 18 (vérificateur) ; tour 2, conditions de D | commun sur le principe ; granularité du vérificateur divergente (A, B, C, D), non tranchée |
| Axe 8 facultatifs (rayon certifié, menace diffuse, dilemme) | CA, analyse v2, § 1 (c), (d), § 3 (c), § 4 (d) | proposé par CA ; non passé au collisionneur comme texte |
| Axe 8 matériau (Bailey p. 3, 23, 25-26, 26 ; CROWN ; double oracle ; regret ; lecture du pilote) | CA, analyse v2, § 0, § 3 ; CO N10 tour 1 (« non contrôlé par l'attaquant à bas coût », pièce 24 p. 23, 26) ; tour 2, condition « recopie de la lecture déléguée » (A, B, C) | pages de Bailey vérifiées sur PDF empreinté par CA (R-744) ; CROWN : page de titre vérifiée (R-744) ; lecture du pilote : condition commune du tour 2 |
| Axe 8, dernière ligne (fiche de contournement écartée) | L (R-339, R-743) ; règle « niveau méthode » du préambule | imposé |
| Boucle : vis-à-vis de l'axe 8 | CA | proposé |

---

## 2. Choix et écarts

- **Accord à quatre sur la mesure, suivi entier** : front performance × évasion par budget sans ratio (convergence (i)), stratification et appariement par difficulté et attaque de la défense composite entière (ii), aucune borne basse (iii), toutes les tâches évaluées (iv), trois témoins (v), vérificateur à poids et code empreintés sans degré de liberté après scellement (critère 18) ; les leviers retenus en (b) sont les seuls classés « contrôlés par le défenseur » ; le tirage au hasard et le modèle surveillable, classés « incertains », restent au matériau.
- **Divergence « sept grandeurs à geler »** (D contre A, B, C au tour 1 ; résolue au tour 2 par D en T3) : les sept grandeurs sont toutes couvertes, mais réparties selon la règle du tour 2 — classe, budgets de référence et maximal, unité de coût **gelés dans la fiche par le proposeur** (a) ; fonction de décision, seuil et taux d'évasion comme métrique **gelés avant toute lecture** (c) ; plancher d'utilité, **constante d'échelle calibrée sur les honnêtes du pilote** puis gelée (c) ; fausse alerte comme pour G1. **Écart déclaré** : D en T3 range les budgets parmi les constantes d'échelle ; ce chapitre les fait geler par le proposeur (sur consigne de l'orchestrateur), parce qu'une fiche sans budget ne nomme pas sa classe ; la grille de budgets reste ouverte à la pente (A sur D, tour 2).
- **Recommandation (b) du collisionneur contre décision (a) de Lazar** : les quatre espèces recommandaient la génération suivante (tour 1 : 0,65 à 0,90 ; tour 2 : 0,55), pour le plafond de taille, le pilote non lu et le devis. Lazar a tranché pour la course 2 (R-1037). Le chapitre limite le coût ainsi : le livrable est une fiche de préenregistrement, pas un résultat ; rien ne s'exécute sur carte pendant la course ; K4 s'applique tel quel (première expérience sur processeur ou données déjà payées, étage sur carte : devis et GO par fiche) ; la condition « recopie de la lecture déléguée du pilote » (A, B, C, tour 2) est reprise au matériau.
- **Ce qui n'est pas repris de l'analyse v2** : l'information mutuelle par estimateurs variationnels, les bornes d'impossibilité en dimension et le cadre de regret marqués SUPPOSÉ (non versés) ne sont pas cités comme pièces ; « regret en ligne » reste un mot de matériau, sans référence.

## 3. Laissé vide pour raison de sécurité

Aucune technique d'évasion, aucun algorithme ni objectif d'attaquant, aucun paramètre opérationnel (ni l'ampleur du déplacement des activations ni les réglages de Bailey et collègues, seulement leurs pages et le sens du prix), aucun exemple d'entrée adverse : les classes sont nommées par leur accès et leur budget seulement (R-339, R-743).
Les attaques vivent dans le texte II, nommé et non décrit ; les deux passages de classe 1 du tour 1 (C, N10) ne sont ni repris ni résumés.

## 4. Réserves

1. **Plafond de taille** : le texte I v5 sert 11 699 caractères pour un plafond de 12 000 ; le bloc d'axe 8 (2 761) et la phrase de boucle (159) le portent à **environ 14 620 caractères**, soit environ 2 620 au-dessus du plafond ; c'est le bloc le plus long du texte (l'axe 4, titre compris, en fait 1 377, mesuré par programme) : le resserrer d'abord coûterait un témoin ou un levier, ce que l'accord du collisionneur ne permet pas sans perte. L'insertion exige soit le relèvement du plafond par Lazar, soit des retraits ailleurs, soit une sous-session à part comme l'axe 7 ; la version nouvelle et la remesure sont chez session-depot (R-1037 : « devis à refaire »). Non tranché ici.
2. **Pilote non lu** : le verdict du pilote « mélange d'équilibre » n'est pas prononcé (brouillon 5, R-1047) ; tant qu'il ne l'est pas, la ligne du matériau est retirée et la pièce conditionnelle n'entre pas ; les constantes d'échelle de (c) ne peuvent pas être calibrées, la fiche les laisse nommées et non chiffrées.
3. **Un levier peut être une porte d'attaque** : un proposeur qui décrit pourquoi un levier tient peut glisser vers ce qui le ferait céder ; la dernière ligne du bloc et la règle « niveau méthode » l'écartent, mais la garde de forme de la course n'a pas été étalonnée sur des fiches d'axe 8 (R5 : cas sain et artefact à ajouter aux témoins plantés).
4. **Granularité du vérificateur** : divergente entre les quatre espèces (modèle ouvert de l'extrait ; groupe extérieur doté de calcul ; équipe d'évaluation de sécurité ; optimiseur et tâches tenus par une équipe indépendante) ; le bloc ne retient que le principe commun.
5. **Copies des synthèses hors dépôt** : lues sur leurs copies du dossier temporaire ; leurs empreintes figurent dans des fichiers du dépôt, mais les originaux n'ont pas été rouverts ici.
6. **Contre-lecture** : non faite (R2) ; la phrase de boucle et l'entrée de pièce conditionnelle sont des propositions de conv-audit, non passées au collisionneur.
