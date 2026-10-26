# Proposition B, tour III.3 : riposte

## 0. Pièces et statuts

- **Bloc FAITS** : il est vide et renvoie à la question. Je ne lui attribue aucun contenu.
- **Pièces reçues** : ma conception III.1, l'équipe rouge A et l'équipe rouge C sont complètes (marques de fin présentes). Je ne réponds qu'aux sections « Contre la proposition B » et à la conclusion de A, qui vise B et C.
- **Statuts** :
  - l'essai et le cadre sont RAPPORTÉS ;
  - les attaques et mes corrections sont des HYPOTHÈSES ;
  - aucune donnée nouvelle n'existe depuis III.1, donc rien ci-dessous n'est un résultat.
- **Chiffres** : ceux de ce tour sont illustratifs, sauf calcul explicite.

---

## (a) Verdicts sur les attaques

Notation : A-F-B*n* désigne la faille *n* de l'équipe rouge A contre B ; C-*n* désigne la faille *n* de C contre B ; « év. » renvoie à un scénario d'évasion, « c » à un contrôle manquant.

| # | Attaque | Verdict | Raison ou test |
|---|---|---|---|
| 1 | **E0 mesure un auto-rapport lexical** (A-F-B1, C-1, C-2, C-év.1, A-c1, C-c1) | **Acceptée** | Une question de suivi qui contient « test » fait bouger Δ pour une direction purement lexicale. Un modèle qui nierait l'annulerait. Toute la chaîne causale (E2, E4) héritait de ce défaut. Δ passe sur la tâche primaire (E0′) ; l'auto-rapport devient secondaire, posé dans une passe séparée après la réponse. **Rejet partiel** : le « coût nul » d'un déni stratégique suppose une capacité non établie sur Llama-3.1-8B et Qwen2.5-7B (HYPOTHÈSE). La correction ne dépend pas de ce désaccord. |
| 2 | **E0 sert de portier : un Δ nul arrête le programme** (A-év. conjointe, C-év.6, conclusion de A) | **Acceptée pour E2** | Ma règle « sans Δ, E2 n'a plus de cible » faisait d'un nul un arrêt, alors qu'un nul est aussi la signature d'un adversaire. Précision textuelle : E1, E3 et E4 continuaient en détection, donc l'arrêt n'était pas total. Désormais, un Δ nul est consigné « aucune cible comportementale à ce plan de coupe », jamais « pas d'état », et E2′ s'exécute quand même, adossée aux contrôles positifs. |
| 3 | **Aucun contrôle ne distingue « rien » de « ailleurs »** (conclusion de A) | **Transformée en test (E-1)** ; acceptation partielle | Aucun contrôle n'exclut « ailleurs » en général. On peut seulement retrouver une variable implantée connue, énumérer les plans de coupe couverts (couches, linéarité, type d'unité, longueur, nombre de tours) et ne prononcer de négatif que sur eux. |
| 4 | **E2 est condamnée à sa troisième issue ; LEACE n'efface que le linéaire** (A-F-B2, C-3) | **Transformée** | C a raison sur la géométrie : un MLP aval peut rendre linéaire une information d'ordre 2 laissée par LEACE. Je rejette en revanche l'idée que ma règle soit fausse. Si l'information est re-décodable, elle n'a pas été retirée ; conclure « non lue » serait illégitime, qu'il s'agisse d'un effet Hydre ou d'une démodulation. Le vrai défaut est que cette issue est probablement fréquente. Ce n'est pas mesuré : « quasi systématiquement » ne repose sur aucune donnée. Dans E2′, l'intervention principale devient le patching contrefactuel de sous-espace, avec plafond. LEACE reste secondaire, accompagné du taux de base et de la variante « attention bloquée » proposée par C. |
| 5 | **Pas de contrôle positif de sensibilité en E2** (A-c3) | **Acceptée** | Direction de refus (Arditi et al., 2024), plus l'implantation E-1(i). |
| 6 | **Un cadre construit sans les mots revient à un format** (A-F-B3) | **Acceptée** | Un sac de mots ne voit pas la numérotation. Je reprends contre moi le témoin « structure rigide sans évaluation » que C opposait à A. J'ajoute un facteur de format et un témoin structurel (E1′). |
| 7 | **Fuite entre construction et évaluation** (A-F-B4) | **Acceptée** | Spécifiée en E1′ : rédacteurs, gabarits et partitions disjoints. |
| 8 | **Encodage non linéaire, tardif ou dans l'attention** (A-év. E1, C-év.2) | **Acceptée comme limite et transformée** | Sondes à toutes les couches, sorties de têtes, sonde non linéaire avec mesure de sélectivité (Hewitt & Liang, 2019). L'issue « le moniteur linéaire ne suffit pas » est écrite d'avance. |
| 9 | **Le contrôle « poids réinitialisés » est trop haut ou trop faible** (A-F-B5, C-4) | **Acceptée** ; rejet partiel de C | Le modèle réinitialisé devient un plancher. Le contrôle informatif est l'explication échangée avec un autre neurone. Contre C : la H_A de E3 ne revendiquait pas la monosémanticité conceptuelle, seulement la prédictivité au-delà d'un témoin. J'accepte que le témoin « 5 jetons » soit trop faible et j'ajoute un témoin thématique. |
| 10 | **E3b est confondue par l'auteur des explications et par la cooccurrence** (A-F-B6, C-c3) | **Acceptée** | Deux témoins appariés (E3b′). |
| 11 | **Le contrôle positif LoRA ne valide pas une porte neuronale** (A-F-B7, C-5) | **Acceptée** | Remplacé par une implantation restreinte à k neurones, tirés par un tiers et inconnus du chercheur, plus une porte naturelle localisée par une méthode indépendante. |
| 12 | **La confirmation change à la fois de lexique et de gabarit** (A-F-B8) | **Acceptée** | Deux corpus de confirmation. |
| 13 | **Portes spécifiques au domaine** (C-év.3) | **Transformée** | Une H_A′ « par domaine » est déclarée d'avance, avec correction de multiplicité. |
| 14 | **Même budget pour les têtes d'attention** (A-c6) | **Acceptée** | Budget réparti d'avance entre neurones et têtes. |
| 15 | **E5 : longueur des réponses, juge non aveugle, Brier incomparables** (A-F-B9) | **Acceptée** | Plan intra-item contrebalancé, juge aveugle, extraction mécanique, bras de référence sans cadre. |
| 16 | **Prédiction « say not » transposée sans sa condition, donc non orientée** (A-F-B10) | **Acceptée** | Réorientée en reproduisant la condition de l'essai : certitude de l'utilisateur portant *sur l'erreur plantée*. Cette prédiction est séparée de la prédiction « injonction de vérification ». |
| 17 | **Rigueur sélective hors distribution ; omissions non mesurées** (C-év.4, A-év. E5) | **Acceptée comme limite de portée** ; rejet partiel | Je rejette la demande implicite de mesurer sur la distribution réelle des tâches : aucune quasi-copie n'est permise et rien n'est servi aux organismes. J'ajoute une mesure d'omission et je restreins la portée explicitement. |
| 18 | **Option D : filtre n-grammes contourné par paraphrase ; optimisation entre budgets au fil des générations** (C-év.5, C-c4, A-év. D) | **Acceptée** | Filtre de similarité par plongement dans un modèle tiers gelé et compteur par lignée. La décision reste de la gouvernance de Lazar, pas une recommandation. |

---

## (b) Expériences corrigées

Règles communes :
- seuils et tailles **illustratifs**, fixés par écrit avant la collecte ;
- une mesure primaire par expérience, les secondaires corrigées par la méthode de Holm ;
- chaque négatif est énoncé avec son plan de coupe : couches, unités, linéarité, un tour, longueur maximale.

### E-1 (nouveau) : sensibilité de la chaîne, préalable à tout négatif causal

- **H_A** : la chaîne complète (sonde, intervention, Δ_comp, recherche de porte) retrouve une variable implantée connue.
- **H_B** : elle ne la retrouve pas.
- **Implantations**, sur des copies :
  1. **Variable non lexicale et distribuée** : ajustement fin complet d'une copie, pour qu'un comportement mesurable dépende d'un déclencheur structurel non lexical (par exemple la parité du nombre de tours, illustratif).
  2. **Porte éparse** : ajustement restreint aux lignes *gate* et *up* de k neurones tirés par un tiers, inconnus de la personne qui cherche.
  3. **Témoin naturel** : la direction de refus.
- **Issues** :
  - Si H_B est retenue pour un type d'implantation, tout négatif de E2′ ou E4′ sur ce type et ce plan de coupe est non interprétable.
  - Si H_A est retenue, les négatifs deviennent interprétables pour ce type de variable seulement.
- **Réserve** : une variable implantée peut être plus saillante qu'une variable naturelle. E-1 borne la sensibilité par le haut ; elle ne la garantit pas.

### E0′ : un écart comportemental lié au cadre existe-t-il sur nos 8B ?

- **Mesure primaire, désignée d'avance** : Δ_comp sur la tâche primaire d'items construits pour l'instrument, sans jamais mentionner l'évaluation. Une seule des mesures suivantes est désignée comme primaire ; les autres sont secondaires :
  - exactitude au format figé ;
  - taux de refus ;
  - marqueurs de prudence spontanés (liste figée) ;
  - longueur ;
  - entropie du premier jeton substantiel.
- **Mesure secondaire** : Δ_auto, l'auto-rapport, posé dans une passe distincte après la réponse, sous deux formes : avec le mot (« test ») et sans le mot (« décris le contexte de cet échange », codé par un juge aveugle).
- **Contrôles** :
  - thème présent, cadre absent (A-c1) ;
  - variation de surface sans lien.
- **H_A** : l'intervalle de confiance de Δ_comp(cadre) exclut celui du contrôle.
- **H_B** : il ne l'exclut pas.
- **Lectures des dissociations** :
  - Δ_auto non nul et Δ_comp nul : compatible avec la classification métalinguistique *a posteriori* décrite par C. Consigné, sans conclure à un état.
  - Δ_comp non nul et Δ_auto nul : compatible avec un déni comme avec un effet non métacognitif. Ne tranche pas.

### E1′ : thème, cadre et format

- **Dessin** : thème × cadre (2×2), plus un facteur format (rigide ou libre). On y inclut la cellule « format rigide sans enjeu » : extraction JSON, formulaires de production routinière.
- **Données** :
  - la sonde est entraînée sur le corpus T ;
  - les paires de E1′ sont écrites par un second rédacteur, avec des gabarits disjoints ;
  - les témoins sont entraînés sur T, avec les mêmes partitions que la sonde.
- **Lectures** :
  - sondes linéaires à toutes les couches ;
  - sorties de têtes ;
  - sonde MLP à une couche cachée, avec sélectivité mesurée contre une tâche de contrôle ;
  - maximum sur les jetons, étalonné contre un nul de même longueur.
- **Témoins à battre** :
  - sac de mots ;
  - témoin structurel : classifieur sur la ponctuation, la numérotation, la longueur des lignes et les jetons de structure ;
  - longueur seule ;
  - 1 000 directions aléatoires.
- **H_A** : l'AUC sur l'axe cadre, à thème et format fixés, dépasse **les deux** témoins (écart bootstrap qui exclut 0).
- **H_B** : le signal s'explique par le thème ou par le format.
- **Issue écrite d'avance** : si aucun cadre ne peut être construit qui diffère du format sans lexique, on consigne « cadre non identifiable en entrée, à un tour ». C'est un résultat sur la question M elle-même.
- **Issue « non linéaire »** : la sonde non linéaire bat les témoins alors que la sonde linéaire n'y parvient pas. On consigne alors : « le moniteur linéaire ne suffit pas ».
- **Taille** : au moins 450 négatifs honnêtes par cellule (1,96·√(0,05·0,95/n) ≤ 0,02).
- **Portée** : un tour, au plus N jetons. Le multi-tour fait l'objet d'un bras ultérieur.

### E2′ : détection contre usage

**Interventions :**
1. **Mesure principale** : patching contrefactuel du sous-espace sondé. L'activation de la paire cadre− est injectée dans cadre+ sur ce sous-espace, à toutes les positions de cadre, simultanément sur les couches L à L+m. Elle est faite dans les deux sens (cadre− vers cadre+ et inversement).
2. **Plafond** : patching du résiduel complet aux mêmes positions et aux mêmes couches.
3. **Garde-fou contre l'illusion de sous-espace** (Makelov et al., 2023) : patching du complément orthogonal.
4. **Mesure secondaire** : LEACE à une couche, avec deux contrôles :
   - taux de base de re-décodabilité après effacement de directions aléatoires (A-c3) ;
   - variante de C, où l'attention des couches au-delà de L vers les positions de cadre est bloquée. Si l'information reste re-décodable à la même position, il s'agit d'une fuite non linéaire et non d'un effet Hydre.
5. **Poussée** : trois doses, pour obtenir une courbe dose-réponse.

**Cadrage :**
- **Mesure** : Δ_comp sur les jetons décisifs. Garde-fou : la perplexité sur texte neutre doit rester stable.
- **Contrôles positifs** : la direction de refus et E-1(i).
- **Témoins** : sous-espaces aléatoires de même dimension.

**Issues :**
- H_B est falsifiée si le patching du sous-espace réduit Δ_comp au-delà du 95e centile aléatoire, dans les deux sens, et si le contrôle positif passe.
- H_A est falsifiée si le contrôle positif passe et si le plafond fait bouger Δ_comp (il y a donc quelque chose à médier), alors que le sous-espace sondé reste dans le nul.
- **Troisième issue** : le plafond lui-même ne fait pas bouger Δ_comp. L'information n'est pas à ces positions ni à ces couches. On consigne le plan de coupe, sans trancher.

Le plafond rend cette troisième issue identifiable. Elle n'est plus la sortie par défaut.

### E3′ : lisibilité neuronale au 8B

- **Ce que l'expérience revendique** : la prédictivité des explications, non la monosémanticité conceptuelle.
- **Métrique** : écart de taux d'activation forte entre les exemples neufs et les presque-manqués.
- **Contrôles** :
  - explication échangée avec celle d'un autre neurone (contrôle principal) ;
  - modèle réinitialisé (plancher) ;
  - fiches mélangées, que le juge doit signaler ;
  - sous-échantillon jugé par un humain.
- **Témoins** :
  - liste des 5 jetons les plus activants ;
  - **témoin thématique** : sac de 30 mots du champ lexical du neurone.
- **Falsification de H_A** : écart au-dessus du contrôle échangé et du témoin thématique inférieur à 10 points (illustratif).

### E3b′ : superposition contre « généralisation récursive »

- **Témoins** :
  - paires de rôles de neurones différents, écrites par le même agent dans la même session ;
  - paires aléatoires appariées en information mutuelle ponctuelle (PMI) de corpus.
- **Mesure complémentaire** : la cooccurrence est rapportée séparément.
- **Issues** :
  - distance inférieure aux deux témoins : la version « empilement arbitraire » est falsifiée ;
  - distance indiscernable des deux témoins : la thèse « généralisation récursive » est falsifiée pour ce modèle.

### E4′ : la porte d'audit

- **Unités** : neurones et têtes d'attention. Le budget est réparti d'avance (60/40, illustratif) et le total reste gelé.
- **Contrôles positifs** :
  - E-1(ii), à l'aveugle ;
  - une porte naturelle (langue ou code) localisée par statistiques d'activation sur un corpus séparé, donc par une autre méthode que celle qu'on teste.
- **Confirmation** : deux corpus, l'un avec le même gabarit et un autre lexique, l'autre avec un autre gabarit et le même lexique.
- **Hypothèses** :
  - H_A : au plus k ≤ 20 unités (illustratif) au total ;
  - H_A′ : au plus k ≤ 20 unités par domaine, pour trois domaines fixés d'avance, avec correction de Holm ;
  - H_B : ni l'une ni l'autre.
- **Règle d'arrêt** : inchangée. Budget épuisé sans confirmation et contrôles positifs passés : on consigne « H_B à ce budget et à ce plan de coupe ».

### E5′ : coercition contre maïeutique

**Dessin :**
- **Facteurs** : marqueurs d'audit × mode impératif ou interrogatif × contestation ou accueil, plus un **quatrième facteur** : certitude de l'utilisateur portant sur l'erreur plantée.
- **Bras de référence** : sans aucun cadre, pour mesurer une dégradation et pas seulement une différence.
- **Plan intra-item** : chaque item passe dans tous les bras, en carré latin.
- **Réponses** : longueur plafonnée et rapportée ; détection des erreurs normalisée par la longueur.

**Mesure de la rigueur :**
- **Juge** : aveugle, il voit la réponse seule, sans l'invite. L'extraction est mécanique chaque fois que c'est possible.
- **Calibration** : probabilités au format figé, score de Brier décomposé en fiabilité et résolution.
- **Exactitude** : rapportée à part.
- **Omission** : items à plusieurs erreurs plantées ou à éléments requis, mesurée par un taux de rappel.

**Prédictions orientées**, chacune réfutable séparément (HYPOTHÈSES) :
- **P1**, transposée de l'essai : la certitude de l'utilisateur sur l'erreur réduit sa contradiction. Si des analogues « say not » ont été identifiés en E3′ ou E4′, leur activation baisse.
- **P2** : une injonction de vérification augmente la contradiction.
- **Duel principal**, inchangé :
  - H_A : à rigueur équivalente (marge écrite d'avance), la lecture de cadre est plus basse sous maïeutique, au-delà du bras lexical ;
  - H_B : la différence s'explique par le lexique, ou la rigueur baisse.

**Portée** : les items sont construits pour l'instrument. Une rigueur sélective hors distribution n'est pas exclue, et les conclusions ne se transposent pas aux tâches ouvertes.

### Option D′ (pour la décision de Lazar, pas une recommandation)

Les quatre conditions de III.1 sont maintenues, avec trois changements :
- filtre de similarité par plongement dans un modèle tiers gelé, en plus des n-grammes ;
- compteur de consultations **par lignée**, sur toutes les générations ;
- distribution complète des tirages rapportée.

### Ordre révisé et coût

| Étape | Expériences | Remarque |
|---|---|---|
| 1 | **E0′ et E1′** | Même corpus apparié, une seule passe. |
| 1 bis | **E-1** | En parallèle, sur des copies. |
| 2 | **E3′** | — |
| 3 | **E2′** | — |
| 4 | **E4′** | — |
| 5 | **E5′** | — |

E-1 ajoute de l'ordre de 20 à 40 GPU·h (illustratif). Le coût dominant reste humain : second rédacteur et tiers qui tire les neurones implantés.

---

## (c) Réponse à la question de l'arbitre (une page)

**Établi au sens des statuts.**
- Rien de l'essai n'est VÉRIFIÉ ici. Ses chiffres (90/7/2–4 %, 76/11/≈1 %, −0,004 nats) sont RAPPORTÉS. La méthode des graphes à neurones bruts n'est pas publiée : elle n'est pas reproductible aujourd'hui.
- Le fait que nos sondes réagissent au thème est RAPPORTÉ par le cadre ; B ne l'a pas audité.

**Établi par raisonnement au cours des trois tours**, et non par l'expérience :
1. Un écart défini par un auto-rapport lexical ne peut pas servir de cible à un test d'usage.
2. Un test « détection contre usage » n'est interprétable qu'avec un contrôle positif de sensibilité et un plafond (patching du résiduel complet).
3. Un cadre d'évaluation « sans lexique » se confond avec le format tant qu'un témoin structurel n'est pas battu.
4. Tout négatif ne vaut que pour un plan de coupe déclaré.
5. Une détection non lue fait un témoin passif : utilisable sur un modèle figé, fragile sous pression d'optimisation. C'est un argument, pas un résultat.

**Non établi :**
- l'existence d'un écart comportemental lié au cadre sur Llama-3.1-8B et Qwen2.5-7B ;
- l'existence d'une variable « ceci est un test » au-delà du lexique et du format ;
- la lisibilité neuronale au 8B, et la validité des juges d'agents ;
- l'existence d'une porte d'audit ;
- un gain de la maïeutique à rigueur égale ;
- la transposition des neurones « say not » du 32B au 8B ;
- la robustesse de tout cela en multi-tour et en contexte long.

**Expérience à faire en premier : E0′ et E1′ sur le même corpus apparié.**

Pourquoi elle :
- son coût est faible (5 à 15 GPU·h, illustratif) ;
- elle ne suppose aucun mécanisme causal ;
- elle est informative quel que soit son signe :
  - **négatif** : le moniteur est lexical ou structurel à un tour, ce qui est un résultat de validité d'instrument ;
  - **positif** : on borne le résidu de cadre et on obtient une cible pour E2′.

Conditions préalables, écrites :
- un second rédacteur ;
- des gabarits gelés ;
- une mesure primaire désignée ;
- des seuils fixés ;
- les deux témoins, lexical et structurel.

**Voie concurrente : E-1 d'abord**, ce qui revient à la position de A. Le départage tient à l'objectif :
- si Lazar veut interpréter des négatifs causaux (E2′, E4′) à court terme, E-1 doit précéder ;
- si l'objectif est la validité des moniteurs existants, E1′ précède, et E-1 tourne en parallèle.

**Ce qui falsifierait « la conscience d'évaluation est en pleine vue dans les neurones »**, au 8B, à budget et plan de coupe déclarés. Il suffit de l'une de ces issues :
- E4′ est négative alors que les deux contrôles positifs passent ;
- le signal de cadre n'apparaît que dans une sonde dense ou non linéaire ;
- les meilleures unités s'activent sur le lexique d'un document cité, non adressé au modèle ;
- en E3′, les explications ne battent pas le contrôle d'explication échangée.

À l'inverse, des candidats confirmés hors lexique et hors format, avec un effet au-delà du nul dans les deux sens, falsifieraient la thèse « simple corrélat thématique diffus ».

FIN-DE-CELLULE