### Note d'intégrité (Règle 2)
Dans les pièces transmises : la pièce **M** a son tout premier caractère coupé (« ur ta question » pour « Sur ta question ») ; la pièce **K** est servie dans sa partie 1 seulement (les parties 2 à 6 sont explicitement omises).

---

## (a) Ce que la question et la position de conv-audit supposent sans que ce soit établi

J'attaque de front la recommandation de conv-audit (pièces M et Question). Elle repose sur six postulats non prouvés ou directement contredits par l'état du code rapporté dans la pièce K :

1. **Supposition 1 : « Une fiche promue par notre juge actuel sur un domaine réel est une découverte utile. »**
   - Statut : **HYPOTHÈSE** (contredite par construction dans la pièce K).
   - *Attaque :* Le rapport K (§ 2.1, **RAPPORTÉ**) établit que la bibliothèque de nuls actuelle ($\mathcal{L}$ : marginale, uniforme, moyennes glissantes, urne) est **aveugle aux traits** $z$. Dans un domaine réel (par exemple le programme de contrôle ou la rétrodiction arXiv), l'issue dépend trivialement des traits (ex. : un épisode long déclenche plus souvent une alerte). Par conséquent, *toute* hypothèse qui encode une corrélation basique déjà connue du programme bat $\mathcal{L}$ et obtient $W_t \ge 1/\alpha$. Sans un « nul informé » (incluant la prédiction calibrée du moniteur de référence), maximiser les « fiches promues par dollar » (métrique de conv-audit) ne sélectionne pas le meilleur chercheur : cela sélectionne le proposeur qui génère le plus vite des banalités vraies à bas coût.

2. **Supposition 2 : « Les systèmes de la littérature proposent mieux que nous grâce à leur architecture (tournois, etc.) indépendamment de leur accès direct au réseau et aux clés. »**
   - Statut : **HYPOTHÈSE**.
   - *Attaque :* Les chercheurs automatiques publiés tirent leur ancrage d'appels dynamiques à Semantic Scholar, arXiv ou Google Search pendant l'idéation. Si on les enferme dans notre bac à sable sans réseau ni clés (exigence du noyau, pièce C et S, **RAPPORTÉ**), leur étage de proposition se réduit à une chaîne de consignes (prompts) interrogeant un modèle sur une banque statique servie par le noyau. Il n'est aucunement établi que le gabarit de texte de Sakana ou d'Agent Laboratory surpasse une consigne directe donnée à Opus 5.5 sur le même dossier de documents.

3. **Supposition 3 : « Une idée scientifique en texte libre produite par un système externe peut être traduite sans perte fatale dans l'algèbre fermée des 12 lois de `selection_pari.py`. »**
   - Statut : **HYPOTHÈSE**.
   - *Attaque :* Le rapport K (§ 2.0 et § 2.1, **RAPPORTÉ**) montre que le juge ne sait évaluer qu'une loi prédictive catégorielle $p(\text{issue} \mid z, g, \text{passé})$ choisie parmi 12 types précodés (`TYPES_LOI`), sur des vecteurs gaussiens $z$ où les conditions `si_sinon` seuillent $z$ à 0. Il ne sait juger ni une aire sous la courbe (AUC), ni un rappel à 1 % de faux positifs, ni un énoncé mécaniste (« la sonde lit la consigne »). Forcer un proposeur externe à passer par ce goulot d'étranglement détruit toute idée portant sur une métrique fonctionnelle ou un mécanisme causal.

4. **Supposition 4 : « L'organisme actuel possède un gradient de sélection darwinienne pour guider le proposeur. »**
   - Statut : **HYPOTHÈSE** (réfutée dans le code, pièce K).
   - *Attaque :* Le rapport K (§ 2.1, **RAPPORTÉ**) révèle que `_controler_pari` impose `severite_attendue == alpha`, ce qui fige `Fiche.aptitude()` à $-\ln \alpha$ pour *toutes* les survivantes. Le « darwinisme » vanté en pièce C est en réalité un filtre binaire plat à $\alpha$ sans gradient d'aptitude. De plus, `MondeNoyau` en v6 n'est qu'une enveloppe tautologique de `MondeSimule` (si la fiche est marquée vraie, le monde *est* la loi de la fiche, K § 2.1 **RAPPORTÉ**).

5. **Supposition 5 : « L'ordre secret et l'urne (juge v1) sont nécessaires et sans coût rédhibitoire pour évaluer un proposeur sur une banque de données réelles. »**
   - Statut : **HYPOTHÈSE** (contredite par E1 et K).
   - *Attaque :* L'expérience 1 (E1, **RAPPORTÉ**) montre que l'urne fait chuter la puissance de détection d'un petit effet net ($\varepsilon = 0,05$) de $0,909$ (v0) à $0,196$ (v1) à 200 tirages. Or, comme le note K (§ 2.1, **RAPPORTÉ**), sur une banque de données figée (rétrodiction arXiv ou épisodes en cache), il n'y a pas de dérive temporelle du monde pendant l'exécution : l'urne fait perdre 80 % de puissance sur les effets fins pour parer une menace inexistante sur banque statique, tandis que le vrai risque (l'analyse adaptative par réutilisation de la même banque de génération en génération, K § 2.1) n'est pas couvert par la garantie de Ville par fiche.

6. **Supposition 6 : « Le canal entre générations est étanche au pilotage. »**
   - Statut : **HYPOTHÈSE** (contredite par K).
   - *Attaque :* La pièce K (§ 2.1, **RAPPORTÉ**) documente que l'agent de synthèse écrit des « leçons » en texte libre (jusqu'à 1 500 caractères) injectées dans la consigne de tous les agents de la génération suivante (`memoire.ajouter_lecon`, `texte_consigne`), et que l'expérimentateur peut laisser des fichiers texte lus par le vérificateur (`_copier_pour_rejeu`). Un proposeur externe ou interne branché sur ces leçons peut être pollué ou piloté par dérive textuelle.

---

## (b) Réponses aux points 1 à 3 de l'arbitre : candidats, traduction et proposeur propre

### 1. Les candidats de la littérature (étage de proposition séparable sans clés ni réseau)

Conformément à la règle 3, toute référence dont le titre exact ou l'année ne peut être garanti sans accès externe est marquée « référence à vérifier », sans identifiant arXiv de mémoire. Les coûts par idée en dollars sont **illustratifs** (calculés au tarif standard d'environ 3 à 15 USD par million de jetons sur Opus 5.5 / Fable 5.1).

| Système | Licence et code | Séparabilité sans clés ni réseau | Entrée → Sortie de l'étage de proposition | Coût estimé par idée | Valeur publiée et statut |
|---|---|---|---|---|---|
| **The AI Scientist v1** (Lu et al., 2024, *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*, Sakana AI) | Code ouvert (Apache 2.0, **RAPPORTÉ** dans la littérature, à vérifier sur dépôt) | **Oui, avec chirurgie.** L'étage `generate_ideas` est un module Python distinct. Il appelle normalement l'API Semantic Scholar (réseau + clé) : il faut remplacer cet appel par une recherche locale sur un fichier JSON de résumés servi par le noyau, et rediriger le client LLM vers le `Relais` local (127.0.0.1). | **Entrée :** code de base (`seed_code.py`), description du domaine, archive des idées précédentes.<br>**Sortie :** JSON (`Name`, `Title`, `Experiment`, `Interestingness`, `Feasibility`, `Novelty`). | ~0,05 à 0,15 USD (**illustratif**, ~3 à 5 appels de génération + réflexion + filtre de nouveauté). | Les auteurs rapportent un coût complet d'environ 15 USD par article généré et évaluent les idées via un relecteur LLM automatisé corrélé aux scores ICLR (**RAPPORTÉ**, à vérifier sur PDF). **Attaque :** leur métrique de valeur repose sur un relecteur LLM dont le biais d'inflation est documenté ; aucune garantie statistique de type Ville. |
| **The AI Scientist v2** (Sakana AI, 2025, référence à vérifier) | Code ouvert (à vérifier) | **Partielle.** Remplace le gabarit fixe de v1 par une recherche arborescente (MCTS / arbre d'exploration agentique) couplant hypothèse et débogage d'expérience. Isoler le seul proposeur sans la boucle d'exécution lui retire son mécanisme principal (le retour d'exécution dans l'arbre). | **Entrée :** objectif de recherche, contexte documentaire.<br>**Sortie :** nœuds d'hypothèses et plans d'ablation. | ~0,30 à 1,00 USD par nœud racine (**illustratif**, dû au facteur de branchement de l'arbre). | Revendique l'acceptation d'un article à un atelier ICLR (**RAPPORTÉ**, référence à vérifier). **Attaque :** si on coupe l'arbre de son exécuteur libre (interdit par notre noyau C-17), il ne reste qu'un générateur par arbre standard. |
| **AI Co-Scientist** (Google, 2025, référence à vérifier) | **Fermé / Propriétaire** (pas de code ouvert officiel) | **Non séparable directement** (code absent). On ne peut qu'en réimplémenter l'algorithme publié : génération d'hypothèses + débat contradictoire + tournoi Elo interne entre agents. | **Entrée :** question de recherche et corpus local.<br>**Sortie :** hypothèses classées par score Elo après débats simulés. | ~0,50 à 2,00 USD par hypothèse survivante du tournoi (**illustratif**, nécessite $O(N \log N)$ appels de débat). | Validation expérimentale rapportée en biomédecine / repositionnement de médicaments (**RAPPORTÉ**, référence à vérifier). **Attaque :** le tournoi Elo interne optimise la plausibilité rhétorique aux yeux du modèle juge du tournoi (exactement l'enfermement que notre noyau cherche à éviter). |
| **Agent Laboratory** (Schmidgall et al., 2025, *Agent Laboratory: Using LLM Agents as Research Assistants*, référence à vérifier) | Code ouvert (MIT, à vérifier) | **Oui.** L'étape de revue de littérature et de formulation de plan (dialogue entre rôles « Postdoc » et « PhD ») est séparable du codeur (`mle-solver`), à condition de lui fournir une moisson documentaire pré-calculée par le noyau. | **Entrée :** sujet de recherche, résumés d'articles locaux.<br>**Sortie :** plan expérimental en texte libre. | ~0,10 à 0,25 USD (**illustratif**, 3 à 6 tours de dialogue multi-agent). | Évalue le taux de réussite d'exécution et la qualité perçue par humains/LLM (**RAPPORTÉ**, à vérifier sur PDF). **Attaque :** produit de la prose non structurée, très éloignée d'une loi prédictive $p(y \mid z)$. |
| **Robin / Kosmos / PaperQA2** (FutureHouse / Edison, 2024–2025, ex. Skarlinski et al., 2024, référence à vérifier) | PaperQA2 est ouvert (Apache 2.0) ; Kosmos/Robin partiellement fermés (à vérifier) | **Non sans dénaturation.** Leur valeur ajoutée réside dans le moissonnage itératif profond (RAG agentique multi-sauts sur des milliers de PDF en ligne). Sans réseau dans le bac à sable, cet étage est aveugle, sauf si le noyau exécute lui-même PaperQA2 *avant* la génération pour produire un dossier de synthèse. | **Entrée :** corpus massif de PDF + question.<br>**Sortie :** synthèse citée avec contradictions identifiées et hypothèses. | ~0,50 à 3,00 USD par synthèse (**illustratif**, forte consommation de jetons de lecture). | PaperQA2 rapporte battre les humains sur des bancs de questions-réponses scientifiques ( LitQA2, **RAPPORTÉ**, à vérifier sur PDF). **Attaque :** c'est un **lecteur/moissonneur**, pas un formulateur de lois probabilistes. Sa place est *dans le service de moisson du noyau*, pas comme proposeur de fiches. |
| **CodeScientist / AI-Researcher / Zochi** (2025–2026, références à vérifier) | Code ouvert pour AI-Researcher / CodeScientist (à vérifier) | **Faible intérêt en tant que proposeur isolé.** Ces systèmes (comme ShinkaEvolve et OpenEvolve cités en pièce C, **RAPPORTÉ**) excellent dans la boucle *mutation de code → exécution → sélection*. | **Entrée :** dépôt de code + banc d'essai.<br>**Sortie :** patch de code + hypothèse implicite. | ~0,20 à 0,80 USD (**illustratif**). | Résultats rapportés sur bancs d'apprentissage automatique (MLE-bench, etc., **RAPPORTÉ**, à vérifier). **Attaque :** coupés de leur boucle d'exécution libre en Docker (écartée pour sûreté en S et C, **RAPPORTÉ**), leur étage de proposition initial est minimaliste. |

**Conclusion sur le point 1 :** Une fois privés de réseau et de clés (exigence non négociable du noyau, S **RAPPORTÉ**), les proposeurs de la littérature se réduisent à **deux mécanismes réels** : (1) un pipeline de lecture structurée de corpus (type PaperQA2, qui relève du moissonnage du noyau) et (2) un graphe d'appels LLM (génération + filtre d'auto-critique type AI Scientist v1, ou tournoi Elo type Co-Scientist). Importer une dépendance tierce lourde pour obtenir trois appels de prompt est une erreur d'architecture ; il suffit d'implémenter le graphe d'appels en 100 lignes dans notre orchestrateur (sous Opus 5.5 / Fable 5.1) pour le tester comme bras.

---

### 2. Le format de la fiche et le problème de la traduction

Le juge actuel exige un objet `loi_predictive` choisi parmi les 12 types de `selection_pari.TYPES_LOI` sur l'espace $(z, g)$ (pièce K § 2.0, **RAPPORTÉ**). Or, un proposeur de la littérature produit du texte libre.

**Trois options d'architecture pour la traduction :**
1. *Traduction par l'étage externe sous consigne :* impossible sans réécrire les prompts internes du système tiers, ce qui invalide l'idée même de « tester le système de la littérature tel quel ».
2. *Gabarit mécanique (expressions régulières / analyseur syntaxique) :* impossible à partir de texte libre non contraint.
3. *Agent traducteur dédié (Opus 5.5) suivi d'un compilateur mécanique strict (`fiche.py`) :* c'est la seule voie viable si l'on garde un proposeur en texte libre.

**Ce que l'on perd à la traduction (et pourquoi c'est le point aveugle de conv-audit) :**
- **Biais de substitution du traducteur :** Si le proposeur externe soumet une idée vague ou inexprimable dans les 12 lois (ex. : « la sonde d'intention échoue quand l'agent délègue le sabotage à un sous-agent », faille C1 de K § 1, **RAPPORTÉ**), l'agent traducteur Opus 5.5, forcé de produire une loi valide sur les traits existants $z$, va *inventer* une corrélation de substitution sur les traits disponibles. Si la fiche est promue, on crédite à tort le proposeur externe d'une idée qui vient en réalité du traducteur.
- **Perte d'expressivité (les 3 verrous de K § 2.1) :** On perd (i) les hypothèses qui requièrent la création d'un *nouveau trait* mesurable $z_{d+1}$ non présent dans `espace_instances`, (ii) les comparaisons fonctionnelles (AUC, rappel à 1 % de faux positifs), et (iii) les tests d'intervention causale.

**Comment mesurer qu'une idée « traduite » est encore l'idée proposée (Protocole d'Aller-Retour Aveugle) :**
Soit $I_0$ l'idée en texte libre, et $F = \text{Traducteur}(I_0)$ la fiche JSON contenant uniquement `loi_predictive` et `espace_instances` (**en masquant le champ texte `enonce`** pour éviter toute fuite textuelle, conformément à l'esprit de N-053 point 1, **RAPPORTÉ**).
- Un agent **Rétro-traducteur** d'une autre famille (Fable 5.1), qui ne voit que l'objet mathématique `loi_predictive` de $F$ et le dictionnaire des noms de traits $z$, génère en langage naturel l'affirmation scientifique $I_1 = \text{Retro}(F)$ que teste exactement cette équation.
- Un juge de fidélité vérifie sur un lot contenant $I_0$ et 4 idées leurres du même domaine si $I_1$ s'apparie uniquement à $I_0$ et si le signe, les variables conditionnelles et le sous-domaine coïncident. Toute fiche qui échoue à cet aller-retour est rejetée *avant* le gel comme « infidèle / intraduisible ».

---

### 3. Le proposeur propre (Opus 5.5 + Fable 5.1) et les failles résiduelles du juge

#### Où un proposeur peut-il encore tricher face au juge v1 + nul v2 + mémoire v5 ?
Le juge étant figé et le nul composite, l'optimisation de Goodhart va se déplacer exactement dans les angles morts mécaniques identifiés en E1, E2, D4 et K (**RAPPORTÉ**) :

1. **Exploitation du nul aveugle aux traits (la triche majeure sur données réelles) :** Tant que $\mathcal{L}$ ne contient que des lois aveugles aux traits $z$ (K § 2.1), le proposeur n'a pas besoin de faire de la science : il lui suffit de proposer une loi qui prédit l'issue à partir du trait le plus corrélé marginalement (ex. la longueur de l'épisode). Il battra l'urne et la marginale à coup sûr ($W_t \gg 1/\alpha$).
2. **Le clonage hors-sonde (contournement de la mémoire v5) :** La mémoire v5 détecte les redites en comparant la divergence KL sur une sonde fixe `_sonde` de **256 instances gaussiennes** avec un seuil d'ordre $0,05/m$ (D4b et K § 2.1, **RAPPORTÉ**). Un proposeur qui veut faire passer $k$ fois la même idée (pour multiplier ses chances de franchir $1/\alpha$ sur le bruit ou gonfler son score de « fiches promues par dollar ») peut utiliser une loi `si_sinon` qui ajoute une branche absurde sur une région de l'espace $z$ où la loi de sélection du plan (`selection_divergence`) ne tire jamais d'instances, mais où les 256 points de `_sonde` tombent (ou inversement : deux lois identiques sur les 120 points d'extrême divergence choisis par `selection_divergence`, mais divergentes de plus de $0,30\text{ nat}$ sur le cœur de la gaussienne sondé par `_sonde`).
3. **La triche du « Ou Exclusif » (XOR) sur les filles (contournement du nul v2) :** L'expérience 2 (E2, **RAPPORTÉ**) prouve que le nul des filles v2 bloque les combinaisons linéaires, logarithmiques et le produit des parents (0 sur 1 000), mais laisse passer à **963 sur 1 000** une fille construite par « ou exclusif » des parents ($A$ si $z_1 z_2 > 0$, $B$ sinon). Un agent de recombinaison paresseux peut systématiquement soumettre un découpage arbitraire de l'espace des traits attribuant une moitié au parent $A$ et l'autre au parent $B$ sans aucune synthèse conceptuelle, et être promu à 96,3 %.
4. **La concentration sur un sous-domaine trivial (biais de `selection_divergence`) :** Le plan d'exécution de 120 instances est choisi par `selection_divergence` là où la loi de la fiche s'écarte le plus de l'uniforme (K § 2.0, **RAPPORTÉ**). Un proposeur peut soumettre une loi plate partout ($p \approx \text{uniforme}$ ou égale au nul) sauf sur une micro-niche triviale et bien connue (ex. $z_1 > 2,5$) où il parie fort. Toute la sélection des 120 instances se concentrera sur cette niche : la fiche aura une couverture réelle du domaine quasi nulle, mais un taux de promotion maximal.
5. **Le pilotage inter-générationnel par les « leçons » :** En lisant `texte_consigne` (produit par la synthèse en texte libre, K § 2.1 **RAPPORTÉ**), le proposeur apprend quelles formes syntaxiques de `TYPES_LOI` passent le mieux le filtre et s'enferme dans un sous-espace étroit (effondrement de mode).

#### Conception du proposeur propre (« Proposeur-C ») et des gardes du noyau
Avec uniquement Opus 5.5 et Fable 5.1, un proposeur propre robuste repose sur **trois corrections du noyau** et **une architecture d'agents contradictoire** :

- **Corrections obligatoires du noyau (avant de brancher quelque proposeur que ce soit) :**
  1. *Nul informé obligatoire ($\mathcal{L}_{\text{domaine}}$) :* ajouter dans $\mathcal{L}$ le prédicteur de référence du domaine (ex. régression logistique sur les traits de base ou score calibré du moniteur existant, K § 2.1). Une fiche n'est promue que si elle apporte du **contenu empirique net au-delà du connu**.
  2. *Sonde de mémoire alignée sur le plan :* calculer la signature de la mémoire non seulement sur les 256 points fixes de `_sonde`, mais aussi sur l'union des plans d'exécution `selection_divergence` des deux fiches comparées (bloque le clonage hors-sonde).
  3. *Contenu empirique minimal (anti-niche) et garde anti-partition (anti-XOR) :* exiger que l'entropie de la sélection des instances couvre au moins $M$ sous-populations distinctes (ou que la divergence moyenne sur l'ensemble du réservoir de 600 instances dépasse un seuil $\delta_0$, conformément au critère « risque $\times$ couverture » de S, **RAPPORTÉ**) ; pour les filles, ajouter dans `nul_filles_v2` les partitions élémentaires à 1 seuil par trait ($A$ si $z_j > 0$ sinon $B$).
  4. *Coupure du canal de pilotage (`texte_consigne`) :* supprimer les leçons en texte libre de l'agent de synthèse. Le proposeur ne reçoit de la mémoire qu'un tableau structuré purement numérique/symbolique : liste des couples `(domaines, operateurs, traits_actifs, statut: survivante | eliminee | redite_refusee, log_W_max)`.

- **Architecture du Proposeur-C (Opus 5.5 + Fable 5.1) :**
  - **Entrées servies par le noyau :** (1) fiches de lecture structurées extraites des PDF du dépôt par un rôle lecteur amont (sans réseau), (2) le tableau structuré de l'archive (survivantes et éliminées, sans prose), (3) le schéma exact de `espace_instances` et `TYPES_LOI`.
  - **Étage 1 — Génération diversifiée par quotas (Opus 5.5) :** Au lieu d'un tournoi Elo (qui homogénéise vers le consensus moyen du modèle), imposer un échantillonnage stratifié forcé sur une grille `(sous-ensemble de traits × famille d'opérateur)` non encore saturée dans l'archive, avec deux modes : *exploitation/falsification* des survivantes et *exploration orthogonale* loin des signatures existantes (répulsion par la sonde de mémoire). Opus 5.5 produit directement le couple `(énoncé, loi_predictive)` pour éviter toute perte de traduction.
  - **Étage 2 — Crible pré-gel d'espèce croisée (Fable 5.1) :** Avant le gel, Fable 5.1 ne note **jamais** la « plausibilité » ni l'« intérêt » de l'idée (ce qui recréerait le filtre conservateur de la littérature). Il exécute uniquement trois vérifications formelles : (a) l'aller-retour aveugle (`Retro(loi_predictive)` correspond-il à `enonce` ?), (b) la loi dégénère-t-elle vers un membre de $\mathcal{L}_{\text{domaine}}$ sur 90 % de l'espace ?, (c) pour une fille, est-ce une simple partition géographique des parents ?

---

## (c) Réponse au point 4 de l'arbitre : critique de la métrique et expériences décisives (Inférence forte B4)

### Pourquoi « Fiches promues par dollar » est une mauvaise métrique
La métrique proposée par conv-audit (« fiches promues par dollar ») viole la loi de Goodhart pour quatre raisons :
1. **Elle récompense les vérités triviales à bas coût :** Tant que le nul ne contient pas toute la connaissance triviale du domaine, le proposeur le moins cher qui émet des évidences connues maximise le ratio.
2. **Elle ignore le contenu d'information et l'ampleur :** Comme toute fiche promue a la même valeur binaire ($1$ si $\sup_t W_t \ge 1/\alpha$, $0$ sinon, K § 2.1), promouvoir trois micro-effets redondants à 0,10 USD bat la découverte d'une faille majeure à 0,50 USD.
3. **Elle masque le coût et le déchet de traduction :** Un proposeur externe en texte libre qui produit 10 idées à 0,05 USD dont 8 sont intraduisibles dans `TYPES_LOI` (et qui consomment 0,10 USD d'agent traducteur chacune) a un coût réel par fiche *évaluable* bien supérieur à son coût facial.
4. **Elle ignore la fécondité de lignée (marchepieds) :** Une fiche de génération 0 dont les filles en génération 1 et 2 battent le nul strict v2 vaut plus qu'une impasse isolée.

### La bonne métrique : Gain d'Information Cumulé et Fécond par Dollar ($\text{GIF}/\$ $)
Sur une course de $G=2$ générations à budget total **tout compris** $B_{\text{total}}$ (incluant appels du proposeur, appels du traducteur éventuel, et coût d'exécution/vérification des fiches soumises), pour l'ensemble $S$ des fiches promues contre le **nul informé** $\mathcal{L}_{\text{domaine}}$ et non fusionnées par la mémoire :
$$\text{GIF}/\$ = \frac{1}{B_{\text{total}}} \sum_{f \in S} \underbrace{\max\left(0, \log W_{\max}(f \mid \mathcal{L}_{\text{domaine}}) - \ln(1/\alpha)\right)}_{\text{gain d'évidence net au-delà du seuil}} \times \underbrace{C_{\text{couv}}(f)}_{\text{couverture } \in [0,1]} \times \underbrace{(1 - \max_{a \in \text{Archive} < f} \text{Sim}(f, a))}_{\text{nouveauté prédictive}}$$
complété par le **Taux de Rappel des Vérités Cachées ($\text{TRVC}/\$ $)** lorsque l'on opère sur un monde ou une banque où $M$ structures vraies non triviales (ou failles S/D/E de l'audit, K § 2.2) sont connues du seul noyau.

---

### Les 3 expériences décisives (Format B4 : duel $H_A$ contre $H_B$)

#### Expérience 1 — Le goulot de traduction : Génération native contrainte vs Texte libre traduit
- **Question tranchée :** L'étage de traduction (texte libre $\to$ `TYPES_LOI`) détruit-il ou fabrique-t-il artificiellement la valeur des proposeurs de la littérature ?
- **$H_A$ (Hypothèse de l'ancrage direct) :** Un proposeur qui génère directement dans la grammaire formelle de la fiche (`loi_predictive` + `enonce`) préserve mieux l'alignement sémantique-mathématique et obtient un taux de survie fidèle supérieur à coût égal.
- **$H_B$ (Hypothèse du découplage créatif, implicite chez conv-audit) :** Laisser le proposeur penser en texte libre (style littérature) puis traduire par un agent dédié produit des fiches aussi fidèles et plus riches, sans biais de substitution du traducteur.
- **Protocole :** Sur un banc de 60 problèmes à vérité connue (vivier v5 étendu avec un nul informé $\mathcal{L}_{\text{domaine}}$), on compare à budget égal :
  - *Bras 1 (Natif) :* Opus 5.5 génère directement la fiche complète.
  - *Bras 2 (Traduit) :* Opus 5.5 génère l'idée en texte libre (format JSON de *AI Scientist v1*), puis un second appel Opus 5.5 traduit en `loi_predictive`.
  - *Contrôle négatif (Biais du traducteur) :* On passe au traducteur du Bras 2 vingt idées en texte libre **vides de sens ou portant sur des traits absents** (fausses pistes).
- **Métrique et Seuils :**
  1. Taux de succès à l'Aller-Retour Aveugle (fidélité $\tau_{\text{fid}}$ via Fable 5.1) ;
  2. Taux de promotion sur le contrôle négatif ($\tau_{\text{sub}}$, qui mesure les découvertes usurpées par le traducteur) ;
  3. $\text{GIF}/\$ $ net (calculé uniquement sur les fiches passant le filtre de fidélité).
- **Issues falsificatrices :**
  - Si $\tau_{\text{fid}}(\text{Bras 2}) < 0,70$ (**illustratif**) **ou** si $\tau_{\text{sub}} > \alpha = 0,05$ (le traducteur invente des lois vraies à partir de texte vide) **ou** si $\text{GIF}/\$(\text{Bras 1}) \ge \text{GIF}/\$(\text{Bras 2})$, alors **$H_B$ est réfutée** : on abandonne définitivement tout proposeur en texte libre non contraint.
  - Si $\tau_{\text{fid}}(\text{Bras 2}) \ge 0,85$, $\tau_{\text{sub}} \le 0,05$ et $\text{GIF}/\$(\text{Bras 2}) > 1,25 \times \text{GIF}/\$(\text{Bras 1})$ (**illustratif**), alors **$H_A$ est réfutée** : le découplage texte libre + traducteur est adopté.

#### Expérience 2 — Duel à budget égal : Proposeur de la littérature (sans clés/réseau) vs Proposeur propre vs Nul aléatoire
- **Question tranchée :** Une fois isolé dans notre bac à sable sans réseau et placé devant notre juge (v1 + nul v2 + mémoire v5 + nul informé), le mécanisme d'idéation de la littérature (*AI Scientist v1* / tournoi *Co-Scientist*) apporte-t-il quelque chose par rapport à notre proposeur propre ?
- **$H_A$ (Position de conv-audit) :** Le proposeur de la littérature (chaîne génération + réflexion + tournoi/filtre de nouveauté) obtient un $\text{GIF}/\$ $ et un taux de découverte de lignées fécondes (génération 1) significativement supérieurs au proposeur maison.
- **$H_B$ (Hypothèse de réduction au noyau) :** Sans accès réseau dynamique et sous le même modèle de base (Opus 5.5 / Fable 5.1) et la même moisson locale, l'architecture de la littérature ne fait que dépenser des jetons supplémentaires en débats internes qui filtrent les idées audacieuses ; le proposeur propre stratifié (Proposeur-C) fait au moins aussi bien par dollar.
- **Protocole (Duel à budget total fixe de 15 USD par bras, illustratif, sur la banque de rétrodiction arXiv 2003–2016 ou banque d'épisodes en cache, $N=10$ courses indépendantes de 2 générations par bras, soit 60 fiches en Gen 0 et 30 filles en Gen 1 au total par bras) :**
  - *Bras L (Littérature) :* Pipeline *AI Scientist v1* (ou tournoi Elo à 4 tours) alimenté par les résumés locaux, suivi du traducteur validé en Exp. 1.
  - *Bras P (Proposeur-C maison) :* Tirage stratifié par quotas d'opérateurs/traits sur Opus 5.5 + crible formel Fable 5.1 (sans filtre de plausibilité subjective).
  - *Contrôle négatif / Le Nul du duel ($\text{Bras } 0$) :* Même budget, même schéma JSON, mais le proposeur tire au hasard des couples de traits et d'opérateurs de `TYPES_LOI` dans la mémoire (générateur aléatoire syntaxiquement valide + prompt minimaliste sans stratégie ni littérature).
- **Taille d'échantillon et Seuils :** 10 courses appariées (mêmes graines de monde/banque) par bras. Test de permutation apparié unilatéral à $\alpha = 0,05$.
  - Seuil d'inutilité du proposeur de la littérature : $\text{GIF}/\$(\text{Bras L}) \le 1,20 \times \text{GIF}/\$(\text{Bras P})$ (**illustratif**, marge de 20 % requise pour justifier la dette technique d'un code tiers et d'un traducteur).
  - Seuil d'inutilité globale des proposeurs LLM : le bras ne bat pas le générateur aléatoire $\text{Bras } 0$ d'au moins $+50\,\%$ en $\text{GIF}/\$ $ (**illustratif**).
- **Issues falsificatrices :**
  - Si $\text{GIF}/\$(\text{Bras L}) \le 1,20 \times \text{GIF}/\$(\text{Bras P})$, **$H_A$ (position de conv-audit) est réfutée** : on n'importe aucun proposeur de la littérature.
  - Si $\text{GIF}/\$(\text{Bras L}) > 1,20 \times \text{GIF}/\$(\text{Bras P})$ avec au moins 2 lignées fécondes de plus en génération 1, **$H_B$ est réfutée** : l'étage externe est adopté.
  - *Contrôle fatal :* Si ni Bras L ni Bras P ne battent significativement $\text{Bras } 0$ (aléatoire), **les deux sont réfutés** : cela prouve que l'espace des 12 lois de `TYPES_LOI` est si restreint qu'une recherche exhaustive/aléatoire sur processeur suffit, rendant tout appel LLM de proposition inutile.

#### Expérience 3 — Fermeture des triches résiduelles du juge (Nul aveugle aux traits et Filles XOR)
- **Question tranchée :** Un proposeur qui optimise son taux de promotion peut-il battre le juge v1 + nul v2 sans découvrir la vraie loi causale du monde ?
- **$H_A$ (Suffisance du juge actuel v5) :** Le juge v1 + nul des filles v2 strict + mémoire v5 suffit à bloquer à $\le \alpha$ tout proposeur opportuniste qui exploite les corrélations marginales des traits ou des partitions arbitraires de parents.
- **$H_B$ (Vulnérabilité aux triches structurelles) :** Sans un membre « référence dépendante des traits » dans $\mathcal{L}$ et sans un membre « partition simple (XOR) » dans `nul_filles_v2`, un proposeur opportuniste atteint un taux de fausse promotion $> 50\,\%$.
- **Protocole (sur processeur seul, 1 000 répétitions, 0 USD, calqué sur E1/E2) :**
  - On injecte deux agents tricheurs : (1) `Tricheur_Bruit_Trait` en Gen 0 qui prédit uniquement l'effet marginal d'un trait confondant $z_1$ déjà connu de la base de référence ; (2) `Tricheur_Partition_XOR` en Gen 1 qui combine deux parents survivants par $A \cdot \mathbb{I}(z_1 z_2 > 0) + B \cdot \mathbb{I}(z_1 z_2 \le 0)$ dans un monde où la vraie loi n'a aucune interaction d'ordre 2.
  - On les évalue sous le Juge v5 actuel contre le Juge v5+ (enrichi de $\mathcal{L}_{\text{domaine}}$ et du nul de partition).
- **Issues falsificatrices :**
  - Si sous le Juge v5 actuel, le taux de promotion de l'un de ces deux tricheurs dépasse $\alpha = 0,05$ (attendu : $> 0,80$ d'après E2 où XOR passe à $0,963$, **RAPPORTÉ**), **$H_A$ est réfutée** : il est interdit de lancer la moindre compétition de proposeurs avant d'avoir fusionné le Juge v5+.
  - Si le Juge v5+ ramène ces deux tricheurs à $\le 0,01$ tout en gardant une puissance $\ge 0,90$ sur une vraie fille à interaction synergique à 500 tirages, **$H_B$ est corroborée et son remède validé**.

---

## (d) Validation des instruments nommés (Point c du livrable)

Pour chaque instrument mobilisé dans la question et dans cette conception, voici la mesure minimale de fonctionnement avant emploi :

| Instrument | Taux de détection exigé (Vrais Positifs) | Taux de fausses alertes maximal (Faux Positifs) | Cas honnêtes appariés (pour mesurer les faux positifs) | Vérification mécanique simple à battre (Témoin) |
|---|---|---|---|---|
| **1. Filtre de fidélité de traduction (Aller-Retour Aveugle Fable 5.1)** | $\ge 90\,\%$ de rejet sur des paires `(énoncé, loi)` où l'on a permuté un signe, un trait $z_j$ ou une condition `si_sinon` (**illustratif**). | $\le 5\,\%$ de rejet sur des fiches de référence écrites à la main où `loi_predictive` traduit exactement `enonce` (**illustratif**). | Les 60 fiches saines du vivier v5 (`population-pari-vivier60-4traits-v1.json`, D4b **RAPPORTÉ**) dotées de leur énoncé exact. | Correspondance lexicale mécanique : vérifier par script Python que tous les indices de traits $z_j$ et seuils numériques cités dans `loi_predictive` apparaissent littéralement dans `enonce`. |
| **2. Garde de mémoire prédictive anti-clonage (Sonde v5+ sur plan)** | $\ge 95\,\%$ de détection des « clones hors-sonde » (lois identiques sur les 120 points de `selection_divergence` mais modifiées ailleurs, **illustratif**). | $\le 5\,\%$ de fausses fusions **par fiche** (taux garanti par le quantile $0,05/m$ de D4b, **RAPPORTÉ**) sur des lois réellement distinctes. | Paires de fiches testant le même sous-ensemble de traits avec deux formes fonctionnelles distinctes (ex. linéaire vs non-monotone) sur les mêmes instances. | Égalité exacte de l'arbre syntaxique canonisé de `loi_predictive` (arrondi à $10^{-2}$) ou Jaccard des 3-grammes de l'énoncé $> 0,5$ (K § 2.1, **RAPPORTÉ**). |
| **3. Nul informé du domaine ($\mathcal{L}_{\text{domaine}}$)** | $\ge 99\,\%$ d'élimination (promotion $\le 0,01$) des fiches qui ne font que répéter la prédiction du moniteur de base ou la corrélation marginale d'un trait connu. | Perte de puissance $\le 5$ points (puissance $\ge 0,90$ à 500 tirages, **illustratif**) sur une hypothèse apportant un gain net de divergence KL $\ge 0,10\text{ nat}$ au-delà de la base. | Fiches vraies qui corrigent une erreur systématique du moniteur de base sur une sous-population $g$ spécifique. | Le juge v1 actuel avec bibliothèque aveugle aux traits (`BIBLIOTHEQUE_STANDARD_V1`, K § 2.1 **RAPPORTÉ**). |
| **4. Crible anti-niche (Couverture minimale du domaine)** | $100\,\%$ de rejet des paris ultra-couverts (lois égales à l'uniforme sur $> 90\,\%$ du réservoir de 600 instances et concentrant `selection_divergence` sur $< 10\,\%$ de l'espace). | $0\,\%$ de rejet sur des hypothèses de sous-population légitimes déclarées explicitement dans le champ `contraintes` / `sous_populations` ($g$). | Fiches portant sur un mode de sabotage rare mais déclaré comme domaine cible $g$, où la loi diverge sur tout $g$. | Seuil mécanique sur l'entropie des poids de sélection ou sur la variance des traits $z$ dans l'échantillon de 120 instances choisi par `selection_divergence`. |

---

## (e) Ancrage matériel et Recommandation (Point 5 de l'arbitre)

### Ancrage matériel (Modèles, Calcul, Coûts)
- **Modèles autorisés (contrainte de Lazar, Question, RAPPORTÉ) :** Claude Opus 5.5 (proposeur, traducteur éventuel, expérimentateur, recombinaison) et Claude Fable 5.1 (vérificateur d'autre modèle, rétro-traducteur aveugle, crible formel). Pour le domaine du contrôle (N-053 point 4, **RAPPORTÉ**), les épisodes en banque utilisent les modèles ouverts déjà prévus au programme (ex. Qwen2.5-7B en juge rapporté et modèle à 8 milliards de paramètres).
- **Calcul et Coûts :**
  - *Expérience 3 (fermeture des triches XOR et nul informé en simulation) :* 1 cœur CPU (Python 3.13 / numpy), ~15 minutes de calcul, **0 USD** (comme E1 et E2, **RAPPORTÉ**).
  - *Premier lancement réel de plomberie (Devis D, option a) :* CPU + appels API via le `Relais` local, **5 à 10 USD attendus (plafond 17,80 / 20 USD, RAPPORTÉ en pièce D)**.
  - *Expérience 1 (Goulot de traduction, 60 idées × 2 bras) :* CPU + API, environ **4 à 6 USD** (**illustratif**).
  - *Expérience 2 (Duel Proposeur-C vs Littérature vs Aléatoire sur banque réelle arXiv ou cache d'épisodes) :* CPU + API, **15 USD par bras**, soit **45 USD au total** (**illustratif**, inférieur aux 10 + 60 + 60 USD du devis mentionné en pièce M, **RAPPORTÉ**).

### 5. Recommandation : quand décider, et qu'est-ce qui ferait changer d'avis ?

**Verdict : Il ne faut surtout pas décider d'intégrer un proposeur de la littérature maintenant, ni dépenser 1 dollar de duel de proposeurs avant d'avoir franchi deux portes bloquantes.**

1. **Pourquoi attendre après le premier lancement réel (Pièce D, option a) ET après le passage à une banque réelle (option b) :**
   - Aujourd'hui, l'organisme n'a jamais fait tourner un seul vrai agent via `AdaptateurClaudeSDK` ni le `Relais` de clé (pièce D et K § 2.1, **RAPPORTÉ**). Brancher un système tiers avant d'avoir validé le bac à sable réel (option a de D, 5 à 10 USD) mélange les pannes de plomberie et l'évaluation scientifique.
   - Surtout, en option (a), le monde est `MondeNoyau` (tautologique : si la fiche est marquée vraie, le monde *est* la loi de la fiche, K § 2.1 **RAPPORTÉ**) et les fiches sont pré-écrites. Un proposeur ne peut être testé qu'en option (b) (banque arXiv 2003–2016) ou sur une banque cachée d'épisodes du programme (recommandation n° 1 de K § 2.1), une fois le **nul informé ($\mathcal{L}_{\text{domaine}}$)** codé sur processeur (0 USD).
2. **Ce qu'il faut faire tout de suite (sans dépense supplémentaire) :**
   - Rendre l'interface du rôle `proposeur` modulaire dans le code (une simple fonction qui prend le dossier de lecture et le tableau d'archive et rend une liste de JSON `Fiche`), ce qui coûte 0 USD et quelques heures de code ;
   - Corriger les 4 failles identifiées par K et E2 (nul informé $\mathcal{L}_{\text{domaine}}$, sonde de mémoire sur plan, blocage du XOR dans `nul_filles_v2`, suppression du texte libre dans `texte_consigne`) et valider cela en simulation (Expérience 3, 0 USD) ;
   - Exécuter le devis D (option a, 5–10 USD) pour valider la sûreté du relais et du bac à sable réel.
3. **Ce qui me ferait changer d'avis :**
   - *Pour adopter immédiatement un proposeur de la littérature :* qu'on me montre à l'Expérience 1 que la traduction texte libre $\to$ `TYPES_LOI` a une fidélité $\ge 85\,\%$ en aller-retour aveugle sans substitution ($\tau_{\text{sub}} \le 0,05$), **et** qu'à l'Expérience 2 (en bac à sable sans réseau, devant notre juge muni d'un nul informé), le pipeline *AI Scientist v1* bat notre Proposeur-C d'au moins 20 % en $\text{GIF}/\$ $.
   - *Pour abandonner l'algèbre fermée des 12 lois (`TYPES_LOI`) au profit de scripts Python d'évaluation :* si lors de l'Expérience 1 sur la banque du programme de contrôle, plus de 50 % (**illustratif**) des hypothèses connues du programme (H1–H9 ou les failles S/D/E de l'audit) échouent au test d'aller-retour aveugle parce qu'elles sont mathématiquement inexprimables comme lois catégorielles par instance. Dans ce cas, c'est le format de la fiche du juge qu'il faudra élargir aux statistiques fonctionnelles (AUC, rappel à 1 % de faux positifs par ré-échantillonnage dans le noyau) avant de juger quelque proposeur que ce soit.

FIN-DE-CELLULE