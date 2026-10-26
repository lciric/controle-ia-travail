# Cellule A — Tour III.3 : riposte

**Pièces** : C4 (mondes à ponts plantés) toujours absente ; le fichier d'essai de la brique 1 (`5b7011b1…`) absent, comme C l'a relevé. Rien ci-dessous n'en suppose le contenu.
**Statuts** : chiffres de C1, C2, C3a, C3b, R-525 : RAPPORTÉ. Les attaques de B et C sont des HYPOTHÈSES sur ma conception ; mes réponses aussi. Tout chiffre hors des faits est illustratif. Je ne réponds qu'aux sections visant A ; les sections contre B et contre C ne sont pas commentées.

---

## (a) Réponse à chaque attaque

### Équipe rouge B

**A1 — confondant d'information (le bras stratifié voit les opérateurs, le noyau ne voit que S).** *Acceptée.* Dans C3b, c5 ne voit l'opérateur qu'après tirage ; mon bras (2) le voyait avant. Correctif : trois bras à information strictement égale (voir E1'). La stratification se décline en « domaine seul + paire forcée » (même information que c5) et « domaine × opérateur » (information supplémentaire déclarée comme telle, bras séparé).

**A2 — étiquettes vraies contre d_i bruités.** *Acceptée, et je m'en sers* : j'adopte le test final de B (étiquettes estimées par le même extracteur et le même regroupement pour tous les bras) comme forme de E1'. Je le dis : E1' est le test de B, pas le mien. Ma v0 (Q5, point 2) reposait sur un instrument absent de mon tableau ; il y entre (ligne « regroupement de domaine », E1').

**A3 — le contrôle négatif de E1 teste la métrique.** *Acceptée.* Nouveau contrôle : permutation des **vecteurs d_i entre articles** (la représentation est découplée de la vérité plantée, pas l'étiquette de mesure). Tous les bras, qui ne voient que d_i, doivent tomber au niveau uniforme sur le « bisoc vrai » mesuré contre la vérité plantée inchangée. Un bras qui reste haut lit autre chose que d_i.

**A4 — E1 n'est pas une inférence forte.** *Acceptée.* H_B devient « le noyau ne fait pas mieux que la stratification de plus que le plancher A/A ». Les deux issues sont alors exclusives et exhaustives.

**A5 — grille de E2 sans résolution ; homonymes connus du filtre.** *Acceptée.* Pas de ε 0,05 sur [0 ; 0,5] ; la « falaise » est définie comme une variation de bisoc vrai > 0,15 sur un pas de 0,05 (illustratif). Homonymes plantés par un agent autre que l'auteur du filtre, moitié hors de son lexique.

**A6 — la ligne de base de E3 vaut zéro par construction ; prédiction au taux de base.** *Acceptée ; c'est la faille la plus grave avec la C-1 ci-dessous.* Le gabarit de juxtaposition n'est plus la ligne de base. Trois filles nulles mécaniques la remplacent (taux de base, combinaison aveugle, mélange perturbé) ; le score est corrigé du hasard et le nombre de prédictions par fille est **budgété** (E3').

**A7 — champ (iv) déclaratif.** *Acceptée partiellement.* Le champ (iv) est retiré de tout rôle d'évaluation ; il reste une pièce de lisibilité. Sur mondes plantés, l'unification juge ; sur du réel, voir C-1 : le critère ne s'applique qu'aux objets qui portent des instances.

**A8 — E4 : piscine absente, contrôle t₀ − 10 impropre, sonde de fuite verbale, étiquettes OpenAlex rétroactives, coupe du fuseur.**
- Piscine : *acceptée* ; fixée et publiée avant le run (E4').
- t₀ − 10 ans : *acceptée* ; ce n'est pas un contrôle négatif propre (un bon prédicteur peut anticiper). Retiré ; remplacé par jumelles appariées en topologie (voir C-3) et par permutation des partenaires.
- Sonde verbale : *acceptée* ; voir C-3, et surtout : E4' ne fait plus intervenir le fuseur. L'appariement (tirage + filtre) est mécanique ; la rétrodiction teste l'appariement seul. La fusion sur du réel est un test séparé, plus faible (E4'-bis), sous anonymisation.
- Étiquetage OpenAlex rétroactif : HYPOTHÈSE de B, *acceptée comme risque* ; je n'ai pas de fait. Mitigation : étiquettes de domaine construites par partition du graphe de citations **avant t₀** (processeur), les concepts OpenAlex ne servant qu'à nommer les partitions a posteriori. Donnée nécessaire à déclarer.
- Coupe du fuseur < t₀ : *acceptée* ; coût en qualité non chiffré, et c'est précisément pourquoi E4' sort le fuseur de la boucle.

**A9 — E5 truqué pour l'appariement par opérateur.** *Acceptée.* Le générateur plante, à nombre égal, des ponts par opérateur partagé et des ponts A–B–C par terme intermédiaire sans opérateur commun ; il est écrit par un agent autre que celui de l'appariement.

**A10 — 12 points importés sans A/A.** *Acceptée.* Tout seuil est fixé après l'étalonnage A/A (E0'), comme R-525 le place en tête.

**Évasions (jargon rare, cellule peu peuplée, paraphrase, multiplicité, silence à froid).** *Acceptées comme menaces.* Deux réponses mécaniques : (i) budget fixe de prédictions par fille et de filles par paire, avec score corrigé du hasard — sans quoi B a raison : « aucun instrument ne fait payer la multiplicité » ; (ii) un **bras adverse** dans chaque expérience : un script sans compréhension qui applique les évasions décrites par B et C ; son taux de survie est une métrique de fausse alerte de l'instrument, reportée telle quelle. Le jargon rare (« cohomologie » vide) : *transformée en test* — l'extracteur est mesuré sur l'usage, non la présence, avec des résumés à mention incidente (déjà dans mes « cas honnêtes appariés ») ; s'il ne sépare pas usage et mention de ≥ 20 points de F1 (illustratif), la grille d'opérateurs n'a pas d'entrée fiable et la v0 abandonne la case « opérateur » au profit du domaine seul.

**Contrôles 1–5 de B.** Tous adoptés : fille au taux de base (E3'), A/A (E0'), étiquettes estimées (E1'), ponts non-opérateurs (E5'), piscine fixée (E4').

### Équipe rouge C

**C-1 — le critère « prédit plus » n'est exécutable que sur jouet.** *Acceptée, avec une conséquence de conception.* Sur résumés bruts, aucun `set.difference()` n'existe ; le traduire par un modèle de langue réintroduit ce que je voulais éliminer. Conséquence : **la v0 ne recombine pas des articles, elle recombine des hypothèses du pôle**, c'est-à-dire des objets qui, par l'étage amont (R-525 : test et nul figés par le noyau, tirages frais après engagement), portent déjà une observable, une prédiction et un générateur de données. Sur ces objets, les instances existent. Sur la littérature réelle, la recombinaison ne produit qu'un **candidat** qu'il faut d'abord convertir au format du pôle — et c'est l'étage amont, non la recombinaison, qui juge le contenu. Je retire donc la prétention que le critère mécanique s'applique au texte.

**C-2 — fuite circulaire extracteur / grille.** *Acceptée partiellement.* Fuite réelle si le même jeu de 100 résumés calibre l'extracteur et définit les strates. Correctif : jeu d'annotation (extracteur) ≠ jeu d'évaluation (E1'), taxonomie des cellules fixée avant l'annotation. *Rejetée* sur la conclusion « la stratification gagne par construction » : avec étiquettes estimées dans tous les bras (A2 de B), le noyau et la stratification subissent la même discrétisation, et c'est exactement ce que E1' mesure.

**C-3 — rétrodiction : confondant topologique à 2 sauts ; fuite implicite du fuseur.** *Acceptées toutes les deux.* Jumelles appariées sur nombre de voisins communs et attachement préférentiel avant t₀ (contrôle 2 de C, adopté). Fuseur hors de E4' ; en E4'-bis, anonymisation des entités (contrôle 3 de C, adopté) : si le score s'effondre après anonymisation, la fuite était là.

**C-4 — E2 confond géométrie de S et forçage glouton.** *Acceptée.* Plan factoriel : {c1 sans forçage, c5 avec forçage, stratification sans forçage, stratification avec forçage} × grille de bruit (E2').

**Évasion 1 — raccord par morceaux (fille = f(X) + g(W) sur instances mixtes).** *Acceptée ; trou réel.* « Défini sur une instance où aucun parent ne prédit » est satisfait par un produit cartésien trivial. Le critère devient : la fille doit battre, sur tirages frais, **la combinaison mécanique aveugle** des parents (somme, produit, enveloppe harmonique) sur les instances nouvelles, de plus que le plancher A/A (contrôle 1 de C, adopté). Une fille qui ne dépasse pas la combinaison aveugle n'a pas d'interaction, donc pas de contenu propre.

**Évasion 2 — camouflage taxonomique.** *Acceptée* ; même réponse que pour B (bras adverse ; extracteur mesuré sur l'usage ; repli sur le domaine seul si l'extracteur échoue).

**Évasion 3 — clause ± qui neutralise le filtre.** *Acceptée.* Correctif : un texte portant les deux marqueurs sur un axe n'est plus « non compté » ; il est **ambigu**, et toute paire contenant un texte ambigu sur un axe est soit renvoyée à un second étage (plages de paramètres déclarées, à l'arbre borné C-17), soit rejetée. Le taux de textes ambigus est lui-même surveillé : s'il dépasse son niveau de fond d'un corpus honnête (mesuré en E0'), c'est un signal d'attaque. *Transformée en test* : clauses ± plantées par le bras adverse ; le rappel du filtre ne doit pas descendre sous sa valeur sans attaque.

**Évasion 4 — tout à la fois.** *Acceptée.* Le bras adverse de chaque expérience combine les trois ; son taux de survie mécanique est reporté. Si ce taux dépasse celui des filles honnêtes moins le plancher A/A, l'instrument correspondant est déclaré vide et retiré de la v0.

---

## (b) Expériences corrigées

Toutes sur processeur, Python, mondes plantés écrits par un agent autre que l'auteur de l'extracteur, du filtre et du canoniseur ; graines publiées ; bras adverse (script d'évasion) dans chaque expérience ; seuils fixés après E0'.

### E0' — Étalonnage A/A (préalable à tout seuil)
Deux courses identiques, graines différentes, de chaque bras de E1' à E5'. Le plancher de bruit δ₀ par métrique est l'écart-type des différences A/A ; tout seuil ci-dessous est exprimé en multiples de δ₀. Mesure aussi le taux de fond de textes ambigus (±) et le taux de base de chaque classe d'instance.

### E1' — Le noyau sert-il à quelque chose, à information égale ? (test de B, adopté)
- Entrées : d_i bruités (norme de bruit ≈ 0,6 comme C3b, RAPPORTÉ) ; **étiquettes estimées** de domaine (regroupement sur d_i) et d'opérateur (extracteur) identiques pour tous les bras.
- Bras : (1) c5 ; (2) stratification sur domaine estimé + paire forcée après tirage (même information que c5) ; (3) stratification domaine × opérateur estimés (information en plus, bras séparé) ; (4) uniforme + paire forcée (témoin faible) ; (5) adverse.
- Grille : n ∈ {12 ; 30 ; 50} ; ε ∈ {0 ; 0,1 ; 0,2 ; 0,3} ; opérateurs ∈ {8 ; 40} (illustratif, reprise de B).
- H_A : c5 dépasse (2) en bisoc vrai de plus de 2 δ₀ (la répulsion continue absorbe les erreurs de frontière). H_B : c5 ne dépasse pas (2) de plus de 2 δ₀.
- Contrôles : d_i permutés entre articles → tous au niveau uniforme ; mondes sans pont → tous à ≤ α.
- Issues : H_A falsifie ma v0 « stratification seule » (réintroduire le noyau sur S seul, γ fixé, pas de Sinkhorn sur L — A7 RAPPORTÉ). H_B falsifie le maintien du noyau et de sa machinerie spectrale.

### E2' — Où la forme cède (plan factoriel)
- Facteurs : forçage de paire {sans, avec} × tirage {noyau, stratification} × ε ∈ {0, 0,05, …, 0,5} × séparation s ∈ {0,2 ; 0,6 ; 1,0} × hubs h ∈ {0 ; 0,3} × n ∈ {12 ; 20 ; 50} ; homonymes plantés par un autre agent, moitié hors lexique du filtre.
- H_A : la perte de bisoc vrai est continue (aucune variation > 0,15 pour un pas de ε de 0,05, illustratif) et attribuable à un facteur identifiable. H_B : une falaise existe ou la perte est inséparable du forçage.
- Contrôle : ε = 1 → niveau du hasard.
- Issues : H_B falsifie l'usage de l'appariement par opérateur sur étiquettes bruitées sans extracteur mesuré ; H_A borne ε tolérable et falsifie la crainte d'instabilité (castes 2/4/5, RAPPORTÉ).

### E3' — La fille prédit-elle plus, corrigé du hasard et des combinaisons aveugles
- Objets : hypothèses au format du pôle (observable, prédiction, générateur), pas des résumés (C-1).
- Consigne de fusion : champs (i) opérateur partagé et préconditions ; (ii) observable et valeur ; (iii) réfutateur. Le champ (iv) est hors évaluation. **Budget** : k prédictions par fille (k fixé, illustratif 5), m filles par paire (illustratif 3) ; au-delà, rejet mécanique.
- Bras : (1) fuseur (modèle ouvert 7–8 milliards de paramètres, version à vérifier au run, ou API) ; (2) fille au taux de base ; (3) combinaison aveugle des parents (somme / produit cartésien / enveloppe harmonique, sans lecture des textes) ; (4) mélange perturbé 0,51/0,49 + ε ; (5) adverse (raccord par morceaux + clause ± + jargon rare).
- Métrique : exactitude sur tirages **frais** des instances nouvelles, moins le taux de base ; gain sur (3) ; taux de chimères (nouvelles et fausses) ; survie des bras (2)–(5).
- H_A : le fuseur dépasse la combinaison aveugle de plus de 2 δ₀ en exactitude corrigée, et les bras (2)–(5) sont rejetés à ≥ 1 − α. H_B : le fuseur ne dépasse pas (3) de plus de 2 δ₀, ou un bras nul survit au-delà de α.
- Contrôles : parents du même domaine sans isomorphisme → détection ≤ α ; parents permutés → idem.
- Issues : H_B falsifie le modèle de langue comme opérateur de fusion de la v0 (reste la combinaison mécanique, qui est alors déclarée pour ce qu'elle est : une régularisation, pas un pont). H_A falsifie « la fusion est décorative » (C2, RAPPORTÉ) **au niveau des hypothèses du pôle seulement**.

### E4' — Rétrodiction, appariement seul, sans fuseur
- Données : OpenAlex ; domaines = partitions du graphe de citations avant t₀ (étiquettes OpenAlex non utilisées dans le tirage) ; 50 paires positives (disjointes avant t₀, ≥ 20 articles joints en 3 ans, illustratif) ; 50 jumelles appariées en taille, croissance, **voisins communs et attachement préférentiel** avant t₀ ; piscine de partenaires fixée et publiée (illustratif : 200 partitions).
- Bras : (1) appariement mécanique (tirage + filtre), sans modèle ; (2) nul stratifié même filtre ; (3) prédicteur topologique pur (voisins communs) — il doit être battu, sinon on ne mesure que de la prédiction de liens.
- Métrique : Hit@10 positives ; AUC positives contre jumelles ; écart au bras (3).
- H_A : (1) dépasse (2) et (3) de plus de 2 δ₀. H_B : non.
- Contrôle : partenaires permutés → niveau du nul ; jumelles → ≤ nul.
- Issues : H_B falsifie la valeur de l'appariement par opérateur sur du réel au-delà de la topologie ; H_A la soutient — pour l'appariement, pas pour la fille.
- **E4'-bis** (fusion sur paires réelles, facultatif) : entités anonymisées ; sonde de fuite = chute du score après anonymisation (contrôle 3 de C). Faible par nature ; ne tranche rien seul.

### E5' — Duel de mécanismes, loyal
- Générateur (autre agent) : ponts par opérateur partagé et ponts A–B–C par terme intermédiaire sans opérateur commun, à nombre égal ; homonymes des deux types.
- Bras : appariement par opérateur ; A–B–C de Swanson ; stratification domaine seule ; adverse.
- H_A : l'appariement par opérateur a un rappel total (les deux types de ponts) supérieur à Swanson de plus de 2 δ₀, à faux ponts égaux. H_B : non.
- Contrôle : mondes sans pont → ≤ α.
- Issues : H_B retire l'appariement par opérateur de la v0 au profit d'un A–B–C avec filtre d'homonymie ; H_A retire Swanson.

### Instruments révisés (ajouts au tableau du tour III.1)
- **Regroupement de domaine** (nouveau) : pureté contre vérité plantée, à n ∈ {12 ; 30 ; 50} ; fausse alerte = frontières coupant un domaine ; à battre : partition aléatoire.
- **Extracteur d'opérateurs** : jeu d'annotation ≠ jeu d'évaluation ; mesure sur l'usage (résumés à mention incidente) ; fausse alerte = jargon rare planté.
- **Filtre** : textes ± comptés ambigus ; taux de fond des ± mesuré en E0'.
- **Critère « prédit plus »** : applicable aux seules hypothèses du pôle ; ligne de base = combinaison aveugle ; budget de prédictions.

Coût : E0', E1', E2', E5' et les bras nuls de E3' sur processeur, 0 USD (C3a rapporte 0 USD pour la génération 0, RAPPORTÉ) ; fuseur de E3' : 5–15 USD par API ou un GPU grand public (illustratif) ; E4' : API OpenAlex gratuite, processeur. Total < 20 USD, 2–3 jours (illustratif).

---

## (c) Réponse à l'arbitre

**Ce qui est établi (RAPPORTÉ, C3b, non audité par une autre famille).** Le noyau du rapport C1 n'est pas semi-défini positif (1 000/1 000) ; la forme trace récompense la similarité de domaine ; Sinkhorn sur L entier efface la qualité ; le correctif « domaine dans S, qualité à part, paire par opérateur après tirage » atteint 0,89–0,95 de diversité de domaine et 0,995–1,000 de « bisoc » — **mais contre un tirage uniforme et avec étiquettes plantées**. Le filtre de compatibilité est un réducteur (57 % → 34 % en régime réaliste), pas une garantie. L'interface non vide n'est pas un pont (65–67 % sans pont planté). Le tri `_score_pertinence_texte` et le Cholesky de la v6.2.1 n'existent pas.

**Ce qui n'est pas établi (HYPOTHÈSE).** Tout ce qui compte pour la question : (1) que la répulsion déterminantale apporte quoi que ce soit au-delà d'une stratification, à information égale et sur étiquettes **estimées** — personne ne l'a couru ; (2) que les étiquettes de domaine et d'opérateur soient extractibles de résumés courts à un bruit tolérable ; (3) que « pont = domaine éloigné + opérateur partagé » soit la bonne définition, contre A–B–C ou l'isomorphisme relationnel ; (4) qu'une fille « prédise plus que ses parents » : B (A6) et C (raccord par morceaux) ont montré que mon critère du tour III.1 était **vide** — satisfait par une prédiction au taux de base et par une somme additive triviale ; je l'ai reconstruit (E3') mais il n'est pas couru ; (5) que la rétrodiction mesure autre chose que la prédiction de liens topologique à 2 sauts ; (6) que l'étage amont (sélection) ne promeuve pas du faux — R-525 en fait la première expérience, non réalisée.

**Ce que les attaques changent dans ma recommandation.** Deux corrections de fond, pas de détail. Premièrement, la v0 recombine des **hypothèses du pôle** (observable, prédiction, générateur figés par le noyau), pas des articles : c'est la seule situation où un critère de contenu mécanique existe (C-1). La littérature réelle sert à la rétrodiction de l'**appariement**, mécanique et sans modèle (E4'), et ne fournit que des candidats à convertir au format du pôle. Deuxièmement, chaque instrument porte un **bras adverse** et un **budget** (prédictions par fille, filles par paire) : sans cela, B a raison, rien ne fait payer la multiplicité, et C a raison, un script sans compréhension survit à 100 %.

**Forme à retenir pour la v0, sous réserve de E1' et E3'** : tirage stratifié sur domaine estimé, paire par opérateur forcée après tirage (le noyau n'y entre que si E1' donne H_A) ; filtre de compatibilité avec textes ambigus comptés, déclaré réducteur ; fusion sous consigne à trois champs, budgétée, jugée contre la combinaison aveugle sur tirages frais ; rétrodiction de l'appariement seul, jumelles appariées en topologie. Rien ici ne touche aux gardes de sûreté du noyau (C2, RAPPORTÉ).

**L'expérience à faire en premier : E3' sur mondes plantés, processeur seul, 0 USD, avant tout choix de mécanisme de tirage.** Raison : les cinq autres expériences classent des mécanismes par la qualité des filles qu'ils produisent ; si le critère de « contenu accru » est vide — et B et C l'ont montré vide dans sa forme du tour III.1 — tout classement en aval est un artefact. E3' se court sans fuseur dans sa partie décisive : les bras nuls (taux de base, combinaison aveugle, mélange perturbé, adverse) doivent être rejetés à ≥ 1 − α par le critère corrigé ; s'ils ne le sont pas, le critère est encore vide et l'étage de recombinaison n'a pas de juge. E1' (le test de B) se court en parallèle, même coût, et tranche le noyau contre la stratification. Si C4 est rendue, ses mondes plantés sont audités par mon tableau (un vérificateur mécanique retrouve 100 % des isomorphismes ; un classifieur lexical ne dépasse pas α + 10 points, illustratif) avant d'être réutilisés, et mes seuils sont réalignés sur les siens.

**Ce qui me ferait changer d'avis** : E1' à H_A → noyau sur S seul réintroduit ; E3' à H_B → pas de modèle de langue dans la fusion de la v0 ; E5' à H_B → A–B–C de Swanson avec filtre d'homonymie à la place de l'opérateur partagé ; E4' où le prédicteur topologique égale l'appariement → la « bisociation sur littérature » est renommée prédiction de liens, et suspendue.

FIN-DE-CELLULE