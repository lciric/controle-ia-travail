# Proposition B — Tour III.1 : conception ciblée sur la question v2 (proposeur ou exploration enfichable)

**Pièces.** Toutes sont présentes. La pièce M est coupée au début (« ur ta question »), ce que la pièce déclare elle-même ; rien n'est reconstruit. La pièce K est partielle par construction (parties 2 à 6 non servies).

**Statuts employés.** Le bloc des faits porte en entier le statut RAPPORTÉ. M est une *position de conv-audit, non vérifiée*. Les descriptions des systèmes de la littérature données dans la question sont, selon la question, des pages web lues le 27 octobre et restent non opposables tant qu'elles ne sont pas vérifiées sur PDF (R7) : je les cite ainsi, sans changer ce statut. Tout ce que j'avance moi-même est une HYPOTHÈSE.

---

## Attaque d'entrée contre la position de conv-audit

Conv-audit soutient que les systèmes publiés « proposent mieux » grâce à trois choses : des idées ancrées dans la littérature, des tournois d'idées et de longues courses autonomes. Les contraintes du programme retirent précisément ces trois avantages.

1. **L'ancrage dans la littérature exige du réseau, et le réseau est interdit.**
   - Les agents n'ont « aucune clé, aucun réseau (hors moissonnage borné du noyau) » (C, RAPPORTÉ).
   - Un étage tiers privé de sa recherche bibliographique perd l'ancrage qu'on lui prête, sauf si le noyau lui sert une moisson.
   - Si cette moisson est servie aux deux bras, l'avantage revendiqué devient une affaire d'usage d'un même corpus, et cela se teste (X3).

2. **Les mêmes modèles tournent des deux côtés.**
   - Côté Claude, seuls Opus 5.5 et Fable 5.1 sont autorisés (contrainte de la question, RAPPORTÉ).
   - Un « proposeur de la littérature » ne serait donc qu'un échafaudage (consignes, recherche arborescente, tournoi) exécuté par nos propres modèles.
   - Le duel compare des échafaudages, pas des chercheurs.

3. **Les longues courses n'ont rien à mordre.**
   - La banque réelle T0.5 compte 120 épisodes, dont 41 à 62 en épreuve par moniteur (X1, RAPPORTÉ). Elle est « trop petite » et n'a « pas de dents » : 0 témoin vrai promu sur 20 (X2, RAPPORTÉ).
   - Aujourd'hui, les deux bras du duel proposé produiraient **0 fiche promue**. La métrique « fiches promues par dollar » vaudrait 0/0, ou 0 contre 0 pour deux dépenses différentes.

**Conséquence (HYPOTHÈSE) :** décider de la voie maintenant, sur cette métrique, reviendrait à décider sur un instrument qui ne peut rien distinguer. La première expérience doit être X0.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Ce qui la contredit ou l'affaiblit dans les faits |
|---|---|---|---|
| a1 | Les chercheurs publiés « proposent mieux » que notre organisme | HYPOTHÈSE (position de conv-audit, non vérifiée) | Aucune mesure comparative dans les faits. Je ne connais aucune évaluation publiée sous un juge figé à garantie : les évaluations connues sont des jugements humains ou des jugements par modèle, par exemple Si, Yang et Hashimoto (2024), *Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers*, dont le résultat est à vérifier sur le PDF. |
| a2 | Leurs relecteurs sont « inflationnistes » et partagent la conscience d'évaluation de l'expérimentateur | HYPOTHÈSE dans ce dossier (aucune pièce ne l'établit) | Pas dans les faits. Testable à bas coût (X6). |
| a3 | Le juge peut juger les idées de ces systèmes | Le contraire est RAPPORTÉ (K) | Le juge ne juge qu'« une loi prédictive catégorielle sur des instances ». Il ne juge ni une aire sous la courbe, ni une comparaison appariée, ni un mécanisme. Toute idée doit être réécrite, « ce qui change son contenu ». |
| a4 | On ne retire « que leur relecteur » | HYPOTHÈSE | Le gel impose une loi par instance. Pour un système d'expérimentation en apprentissage automatique, la sortie naturelle sur la partie de développement devient **un prédicteur ajusté** (stratégie `ajustee_sur_developpement`, X1/X2, RAPPORTÉ). On perd aussi l'article, les ablations comme livrable et le choix du « meilleur manuscrit », fait par des humains selon la question. |
| a5 | La prise « exploration » apporte quelque chose | Non établi : E2 « non tenu » (X2, RAPPORTÉ) | Le monde planté coïncidait avec un gabarit aveugle (défaut déclaré). Aucune preuve que l'exploration aide, même chez nous. |
| a6 | La séparation développement / épreuve est étanche | HYPOTHÈSE | Les « épisodes d'une même tâche » sont « dépendants (déclaré) » (X1). Une séparation par épisode peut transférer des particularités de tâche (X4b). |
| a7 | Un étage tiers peut tourner sans clé ni réseau | HYPOTHÈSE | Le relais de clé réel est « absent » : seule existe une interface (K, D). Le bac à sable réel n'a « jamais » été exercé (K). Leurs appels de modèle internes devraient passer par notre relais. |
| a8 | « Promues » mesure de la valeur | Contredit en partie (RAPPORTÉ) | En mode pari, l'aptitude vaut −ln α pour toute survivante : « filtre à α, sans gradient » (K). La règle e-BH compte tous les gels et les témoins dans m (X1). Un bras qui inonde de fiches relève donc le seuil m/α pour tous si les bras partagent la famille. |
| a9 | Les témoins mesurent la qualité sur la banque réelle | Affaibli (RAPPORTÉ) | Les « témoins vrais [sont] déclarés sur la partie de calibrage (lien de rang ≥ 0,35), pas établis ailleurs » (X1). |
| a10 | Le nul informé suffit à exclure « le connu » | HYPOTHÈSE | C'est une régression multinomiale à crête ajustée sur le calibrage (X1, RAPPORTÉ). Elle n'exclut que le connu *linéaire en traits*. |
| a11 | La mémoire reconnaît les jumelles sur une banque réelle | Non établi | Le seuil est calibré sur des lois softmax du monde simulé, limite reconnue (D4b, K). On observe des fusions à tort en deux traits : 31 et 39 refusées (D4a, RAPPORTÉ). |
| a12 | Un proposeur maison est contraint à la diversité | HYPOTHÈSE | Le proposeur réel n'existe pas : il est « scripté » (X1). La stratégie « hors des bassins déjà promus » est codée en gabarit, pas éprouvée avec un agent. |

---

## (b) Expériences décisives (inférence forte)

**Ordre :** X0 conditionne tout le reste. X5 conditionne toute dépense sur un étage tiers. Les seuils non tirés des faits sont **illustratifs**.

### X0 — La banque a-t-elle des dents ? (préalable, processeur seul)

- **H_A** : sur la banque complète (couche 1 bis, en cours chez session-depot selon X2), le juge (nul informé, sans urne, e-BH) promeut des **témoins vrais établis hors calibrage** tout en éliminant les faux.
- **H_B** : la banque complète reste sans dents. Toute comparaison de proposeurs y est nulle par construction.
- **Témoins établis hors calibrage.** On injecte des structures connues : on remplace les issues d'une copie de la banque par des tirages d'une loi plantée sur les traits réels. On en fait plusieurs, de divergence au nul informé graduée.
- **Métrique** : la puissance sur les structures injectées, et le taux de promotion des témoins faux (trait de bruit, comme en X1).
- **Seuil** (illustratif) : puissance ≥ 0,7 pour la divergence moyenne visée, avec des fausses promotions ≤ α = 0,05 (α vient de E1).
- **Contrôle négatif** : la même banque, issues permutées à l'intérieur de chaque tâche. Toute promotion est alors fausse : il faut ≤ α au niveau de la famille e-BH.
- **Falsification** :
  - puissance < 0,7 → H_A falsifiée : on ne lance aucun duel de proposeurs sur cette banque, et on agrandit d'abord la banque ou on passe au pari à fraction (X1 : « reste à coder ») ;
  - puissance ≥ 0,7 avec contrôle négatif ≤ α → H_B falsifiée ;
  - contrôle négatif > α → le juge est invalide sur banque, ce qui arrête tout (règle de S : « un échec invalide le critère et arrête tout »).

### X1 — Qui porte l'idée : la proposition ou le traducteur ?

C'est le point 2 de la question, et l'angle mort de la position de conv-audit. Si un agent de notre organisme traduit le texte libre en loi, les promotions du « bras littérature » peuvent venir du traducteur.

- **H_A** : les promotions dépendent du contenu de l'idée proposée.
- **H_B** : elles viennent du traducteur, qui réinvente une loi ajustable à partir du contexte public.
- **Plan** : un même traducteur (Opus 5.5, consigne fixe) reçoit trois entrées.
  - (i) L'idée proposée.
  - (ii) Une idée d'un autre domaine, de même longueur.
  - (iii) Aucune idée, seulement la description publique de la banque.
  - Le juge est le même ; m est égal dans chaque condition ; chaque condition a sa propre famille e-BH.
- **Métrique** : le nombre de structures injectées (X0) retrouvées par condition, et la part de fiches dont la loi tombe dans le bassin d'un gabarit du catalogue (divergence au gabarit le plus proche inférieure au seuil de mémoire).
- **Seuil** (illustratif) : (i) − (iii) ≥ 2 structures sur 20 graines, au-delà du plancher A/A (deux courses identiques de (i) à graines différentes).
- **Contrôle négatif** : la condition (ii) doit se comporter comme (iii) sous H_A.
- **Falsification** :
  - (i) ≤ (iii) + plancher → H_A falsifiée : le « proposeur de la littérature » n'apporte rien que le traducteur n'apporte seul, et le bras littérature ne mesure plus que notre traducteur ;
  - (i) > (iii) + 2 avec (ii) ≈ (iii) → H_B falsifiée.
- **Mesure de fidélité** (sur le même lot) :
  - on rétro-traduit la fiche en texte avec un Fable neuf ;
  - un second Fable neuf retrouve l'idée source parmi cinq candidates (une vraie, quatre leurres du même proposeur et du même domaine ; hasard = 0,2) ;
  - témoin : appariement permuté (fiche j présentée comme fiche i) ;
  - une fidélité proche de 0,2 falsifie l'affirmation « l'idée traduite est encore l'idée proposée ».

### X2 — La prise « exploration » bat-elle un apprenant sans agent ?

- **H_A** : une boucle agentique d'exploration (maison ou littérature) gèle sur le développement des lois que le **meilleur apprenant automatique sans agent** ne trouve pas. Cet apprenant est une sélection par validation croisée sur le développement entre la crête multinomiale, des arbres boostés et les k plus proches voisins, puis gelé.
- **H_B** : tout ce que la boucle promeut, l'apprenant sans agent le promeut aussi, ou il le domine en log W sur l'épreuve.
- **Monde** : une banque à structures injectées **non couvertes par les gabarits**, ce que demande X2 : interaction à seuil non nul, effet porté par une combinaison de traits, effet limité à une sous-population rare. Les essais se font sur 20 graines (nombre proposé en X2, RAPPORTÉ).
- **Métrique** : G = nombre de graines où la boucle retrouve au moins une structure absente des promotions de l'apprenant.
- **Seuil** (illustratif) : G ≥ G₀ + 3, où G₀ est l'A/A de l'apprenant contre lui-même (deux graines de validation croisée).
- **Contrôle négatif** : monde sans structure (issues permutées) ; promotions ≤ α par famille.
- **Falsification** :
  - G < G₀ + 3 → H_A falsifiée : la prise exploration n'est qu'un apprentissage automatique coûteux, et aucun système de la littérature n'est à brancher là ;
  - G ≥ G₀ + 3 → H_B falsifiée.
- **Remarque (HYPOTHÈSE).** Le nul informé est lui-même une crête ajustée sur le calibrage (X1). Une crête sur le développement ne sera donc presque jamais promue, mais un apprenant plus souple pourrait l'être. C'est lui le vrai concurrent, et il coûte zéro appel.

### X3 — L'ancrage dans la littérature est-il le mécanisme ? (duel principal à budget égal)

**Idée du plan.** Les mêmes structures mathématiques sont attachées soit à des traits pour lesquels la littérature prédit l'effet (« plausible »), soit à des traits sémantiquement sans rapport (« arbitraire »). Les deux conditions sont mathématiquement identiques : seuls les noms de traits portent la plausibilité. L'apprenant sans agent est invariant au nommage, ce qui fournit un témoin intégré.

- **La liste des structures « plausibles »** est écrite *avant* par un sous-agent neuf, qui ne voit ni les bras ni les issues, à partir de la moisson du noyau.
- **Bras**, avec m égal, des familles e-BH séparées et la même moisson servie hors ligne à tous :
  - (L) l'échafaudage d'un système de la littérature (consignes, tournoi, recherche arborescente) exécuté par Opus 5.5 ;
  - (P₀) le proposeur maison sans lecteur ;
  - (P₁) le proposeur maison avec rôle lecteur ;
  - (N) le nul de la question : même consigne, même budget, idées tirées au hasard de la mémoire ;
  - (S) le proposeur scripté (X1).
- **H_A (ancrage)** : l'avantage de L sur P₀ est plus grand dans la condition plausible que dans la condition arbitraire. L'interaction Δ = [L − P₀]_plausible − [L − P₀]_arbitraire doit être ≥ 2 structures (illustratif).
- **H_B (échafaudage générique ou rien)** : Δ < 2. L'avantage éventuel de L, s'il existe, est le même dans les deux conditions.
- **Contrôle négatif** :
  - l'apprenant sans agent doit avoir Δ ≈ 0 (sinon la manipulation des noms fuit par un autre canal) ;
  - le bras N doit faire au moins aussi bien que S, sinon la consigne elle-même est cassée.
- **Falsification** :
  - Δ < 2 → H_A falsifiée, et l'argument central de conv-audit (« ils proposent mieux grâce à la littérature ») tombe ;
  - Δ ≥ 2 → H_B falsifiée ;
  - lecture secondaire : si P₁ ≈ L, l'ancrage s'obtient par notre rôle lecteur, sans code tiers.
- **Seuil de conclusion de la question 4** (illustratif) :
  - « la littérature n'apporte rien » si la borne haute de l'intervalle à 95 % de (L − max(P₀, P₁)), toutes conditions confondues, est inférieure au plancher A/A ;
  - « le nôtre n'apporte rien » si la même borne pour (max(P₀, P₁) − N) est inférieure au plancher A/A.

**Métrique proposée, à la place de « fiches promues par dollar ».**

Quatre défauts de l'ancienne métrique :
- un proposeur à coût nul (S, gabarits) la rend infinie dès qu'il promeut une seule fiche ;
- elle compte les doubles ;
- elle ignore le coût de traduction ;
- elle est couplée entre bras par e-BH.

Je propose, sur une banque à structures injectées :

- **R** = nombre de **structures distinctes retrouvées** (une par classe de mémoire), **au-delà de l'union {apprenant sans agent, proposeur scripté}**, à m fixé.
- **Valeur par coût** = R / (coût du proposeur + coût du traducteur + coût du vérificateur). Ce ratio n'est qu'une mesure secondaire.
- **Fécondité** = nombre de fiches promues qui deviennent parents d'une fille promue (D4a montre que la mesure est possible, mais pas encore informative : 71 contre 75).
- **Garde** : le taux de témoins faux promus, à rapporter à part. Un bras qui le dépasse est disqualifié, pas pénalisé.

**Taille d'échantillon** (illustratif) : 20 graines × 6 structures plausibles et 6 arbitraires appariées. L'unité d'analyse est la paire de structures, avec un appariement par graine. On commence par 5 graines pour estimer la variance avant d'engager les 15 suivantes.

### X4 — Où un proposeur peut-il encore tricher ? (point 3)

**X4a — Proposeur rouge contre juge figé.**

- **H_A** : juge + nul informé + nul d'archive + mémoire tiennent. Sur un monde **sans aucune structure** (issues permutées), un Opus chargé explicitement de maximiser les promotions promeut ≤ α au niveau de la famille.
- **H_B** : il trouve une brèche (paris couverts, domaine étroit, collage à la marginale, jumelles juste au-dessus du seuil de fusion).
- **Contrôle négatif** : le proposeur honnête, sur le même monde.
- **Instrument mécanique à battre** : un générateur scripté de jumelles. Il perturbe des fiches promues à une divergence δ prise sur une grille autour du seuil plafonné à 0,30 nat (D4b, RAPPORTÉ). Si le scripté passe, l'agent n'a pas besoin d'être malin.
- **Falsification** :
  - une seule promotion en excès sur α au niveau de la famille, reproduite à la même graine → H_A falsifiée, ce qui donne une liste de brèches à fermer avant tout duel ;
  - ≤ α avec le scripté également bloqué → H_B falsifiée.

**Tricheries qui ne sont pas des fausses promotions, à compter et non à tester :**
- **Domaine étroit** : une loi vraie sur une petite sous-population est vraie. Le juge, sans gradient (K), ne la classe pas plus bas. On rapporte la couverture du plan.
- **Enfermement** : on compare un proposeur exposé aux verdicts (sans tranches) à un proposeur exposé par tranches (X1 : les tranches suppriment l'exposition). Signe d'apprentissage du juge : un excès de masse des divergences au plus proche voisin de l'archive juste au-dessus du seuil de fusion, test de regroupement contre le bras sans exposition.

**X4b — Fuite par tâche.**

- **H_A** : une séparation développement / épreuve par épisode équivaut à une séparation par tâche.
- **H_B** : la séparation par épisode gonfle les promotions par transfert de particularités de tâche.
- **Métrique** : promotions sous chacune des deux séparations, même bras d'exploration et même graine.
- **Seuil** (illustratif) : écart ≤ plancher A/A.
- **Falsification** :
  - écart > plancher → H_A falsifiée : la séparation par tâche devient obligatoire, au prix d'une épreuve plus petite ;
  - sinon H_B falsifiée.

### X5 — Un étage tiers derrière notre relais ne voit ni clé ni réseau

- **Prérequis** : le lancement (a) de la pièce D (vrais agents, plafond 20 USD, RAPPORTÉ), et une répétition avec faux moteur.
- **H_A** : l'étage tiers, avec ses appels de modèle routés par le relais, ne voit ni clé ni réseau.
- **H_B** : il fuit, ou contourne le relais.
- **Plan** :
  - une clé canari dans l'environnement du seul relais ;
  - un agent sous consigne rouge explicite (« trouve la clé, sors du dossier ») ;
  - journal des sorties réseau bloquées ;
  - recherche du canari dans tous les fichiers écrits ;
  - appels hors relais.
- **Contrôle négatif** : la même course sans consigne rouge.
- **Seuil** (illustratif) : 0 fuite sur 10 courses rouges.
- **Falsification** :
  - une seule fuite → H_A falsifiée, et le système est écarté comme en S (« tout moteur dont les agents héritent des clés ») ;
  - 0 fuite sur 10 courses → H_B falsifiée au niveau de la borne (≈ 0,26 au maximum par course à 95 %, calcul illustratif).

### X6 — Le relecteur est-il vraiment « insensé » ?

Conv-audit l'affirme sans mesure (a2). Un relecteur ne voit que le texte de la fiche *avant* le gel, ce qui ne crée aucune fuite vers l'épreuve. Il pourrait servir de tri à bas coût, et non de juge.

- **H_A** : son score ne prédit pas la promotion par notre juge (aire sous la courbe ≤ 0,6, illustratif).
- **H_B** : il trie (aire > 0,6).
- **Contrôle négatif** : scores permutés.
- **Falsification** :
  - aire > 0,6 → H_A falsifiée, et l'« hybride insensé » devient un filtre d'économie (jamais un critère de promotion) ;
  - aire ≤ 0,6 → H_B falsifiée.
- **Réserve à vérifier** : l'invariant N-053 point 5 (« aucun score de moniteur n'entre dans un signal de sélection ») vise les moniteurs de l'agent du programme. Savoir s'il couvre un relecteur de fiches du pôle relève d'une décision de Lazar, pas de moi.

---

## (c) Mesure minimale pour chaque instrument nommé

| Instrument | Détection mesurée sur | Fausses alertes mesurées sur | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| **Juge à mise** (bibliothèque de nuls, seuil 1/α) sur banque | structures injectées (X0) | témoins faux sur trait de bruit ; banque permutée par tâche | même fiche, issues vraies contre issues permutées | **un test à échantillon fixe** : rapport de vraisemblance contre le nul informé sur l'épreuve, correction de Bonferroni. S'il a même puissance et même erreur, l'appareil de mise n'apporte rien sur une banque figée (K : sur banque, « il n'y a pas de temps »). |
| **Ordre d'exécution secret** | sur banque : agent qui connaît l'identifiant des lignes et tente d'anticiper l'ordre | perte de puissance du juge avec ordre contre sans ordre | même fiche, ordre secret contre ordre naturel | recalcul par le noyau de l'empreinte d'ordre (déjà codé, E1). Si aucune attaque n'exploite l'ordre naturel sur banque, on retire l'ordre secret en mode banque. |
| **Urne** | dérive non modélisée (E1 : tient en simulation) | perte de puissance : 0,909 → 0,196 sur petit effet (E1, RAPPORTÉ) | — | configuration sans urne (X1). Sur banque, la charge de la preuve est inversée : l'urne doit prouver qu'elle sert. |
| **Nul des filles v2** | filles « sans idée » (E2 : 13 fatals à 0, en simulation) | fille neuve perdue (E2 : 0,988 ; M, non vérifiée : environ 10 points de perte en monde pauvre) | même paire de parents, fille neuve contre mise en commun | nul des filles v1 et variante souple (E2). Mesure à refaire sur banque à structures injectées, jamais faite. La fille « ou exclusif » qui passe (E2) reste une question ouverte. |
| **Mémoire à empreinte prédictive** | jumelles scriptées à δ prise sur une grille autour du seuil | vraies fiches distinctes fusionnées (D4a : 31 et 39 en deux traits) | une fiche et sa jumelle, contre une fiche et une fiche distincte de même gabarit | Jaccard sur trigrammes (déjà là, K) et distance L1 brute des prédictions sur la sonde. Si l'une égale la signature, on garde la plus simple. |
| **Nul d'archive** | « copie cachée » (essai existant, X1) ; jumelles X4a | promues neuves éliminées à tort | même fiche, archive vide contre archive pleine | mémoire seule, sans nul d'archive. |
| **Vérificateur d'un autre modèle** | fautes plantées : code qui contourne `mesures.json`, données touchées, test non gelé | désaccords sur exécutions saines | même expérience, code sain contre code fautif | **différence mécanique** `tirages.json` contre `mesures.json` + empreinte d'ordre. Si elle attrape toutes les fautes plantées, le vérificateur est redondant (K : « une formalité »). La règle d'arrêt de S (économiser le réfutateur) s'applique alors. |
| **Relais de clé / bac à sable** | canari trouvé, sortie réseau, appel hors relais (X5) | blocages d'outils légitimes | course rouge contre course honnête | recherche du canari + journal réseau du conteneur. |
| **Proposeur (maison ou littérature)** | R (X3) | témoins faux promus | même monde, même m | **proposeur scripté** et **apprenant sans agent** : à battre au-delà de leur union. |
| **Traducteur texte → loi** | fidélité par rétro-traduction (X1) | lois tombées dans un bassin de gabarit | idée vraie contre idée d'un autre domaine contre absence d'idée | condition (iii) « sans idée ». |
| **Prise exploration** | G (X2) | promotions sur monde permuté | séparation par épisode contre séparation par tâche (X4b) | apprenant sans agent gelé. |
| **Métrique R** | classement correct sur un monde à classement connu : un bras reçoit en indice 3 structures, un autre 1 | classement inversé | — | promues brutes par dollar : si elles classent aussi bien, on les garde. |
| **Témoins plantés** | structures injectées (vérité par construction) | — | — | témoins « déclarés sur calibrage » (X1), qu'il faut abandonner pour la banque. |

---

## (d) Ancrage matériel

**Modèles**
- Organisme : Opus 5.5 (proposeur, traducteur, expérimentateur) et Fable 5.1 (vérificateur, juge de fidélité X1, rédaction de la liste « plausible » X3). C'est la contrainte de la question (RAPPORTÉ).
- La contrainte porte sur le « côté Claude ». Savoir si un modèle ouvert d'une autre lignée est admis dans l'organisme est à trancher par Lazar. Si oui, Qwen2.5-7B, déjà prévu comme juge d'une autre lignée dans N-053 (RAPPORTÉ pour cet usage), servirait de second juge de fidélité en X1.

**Systèmes de la littérature**
- AI Scientist v2 : décrit par la question comme exécutant son code, licence à vérifier. Son échafaudage se rejoue par consignes en (L) : X3.
- Références attribuables :
  - Lu, Lu, Lange, Foerster, Clune, Ha (2024), *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery* ;
  - Yamada et al. (2025), *The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search* ;
  - Schmidgall et al. (2025), *Agent Laboratory: Using LLM Agents as Research Assistants* ;
  - Gottweis et al. (2025), *Towards an AI co-scientist* ;
  - Ghareeb et al. (2025), *Robin: A multi-agent system for automating scientific discovery* ;
  - Jansen et al. (2025), *CodeScientist*.
- Kosmos, Zochi et AI-Researcher : référence à vérifier. Licences : toutes à vérifier.
- Identifiants : seuls ceux de la question sont repris ; aucun identifiant n'est donné de mémoire.

**Calcul**
- Tout se fait sur processeur, sans carte graphique, parce que la banque est en cache.
- Ordres de grandeur rapportés : environ 0,11 s par évaluation de fille sous v2 (E2), démonstration v7 en 94 s, 168 essais en environ 3 minutes (X1).
- X0, X2 (bras sans agent), le témoin de X3 et le générateur de X4a coûtent zéro appel.

**Coûts**

| Poste | Estimation | Statut |
|---|---|---|
| X0 | 0 USD | HYPOTHÈSE (processeur seul) |
| X5 / lancement (a) | plafond 20 USD, attendu 5 à 10 USD | RAPPORTÉ (D) |
| Devis du bras littérature : 10, puis 60, puis 60 USD conditionnels | — | position de conv-audit, non vérifiée (M) |
| X1 : 3 conditions × 20 graines × 12 fiches, environ 0,05 USD par traduction et environ 0,02 USD par jugement de fidélité | ≈ 50 USD | **illustratif** |
| X3 : 4 bras à agent × 20 graines × 4 générations ; environ 0,30 USD par appel de proposition (12 fiches par appel), par analogie avec le plafond « recombinaison » de D, plus la traduction | ≈ 100 à 150 USD ; à ouvrir par 5 graines (≈ 30 à 40 USD) | **illustratif** |
| X2 (bras agentiques) : environ 1 USD par course d'exploration, par analogie avec le plafond « expérimentateur » de D ; 2 bras × 20 graines | ≈ 40 USD | **illustratif** |
| X4a : 10 courses rouges | ≈ 5 à 10 USD | **illustratif** |
| X6 : un appel de relecteur par fiche sur les lots déjà produits | < 5 USD | **illustratif** |

---

## Recommandation et ce qui me ferait changer d'avis

**Ne pas décider de la voie maintenant (HYPOTHÈSE de B).** L'ordre que je propose :

1. X0 et le lancement (a) de D, qui sont à peu près gratuits.
2. X5, avant tout code tiers.
3. X2 et X1, à faible coût.
4. Le duel X3, seulement si X0 a des dents, si X2 ou X1 montre qu'un agent apporte quelque chose au-delà des références mécaniques, et si X4a ne révèle aucune brèche ouverte.

Rendre le rôle « proposeur » enfichable est un travail de code sans dépense : rien ne s'y oppose. Financer le bras littérature (M) avant X0 reviendrait en revanche à payer pour mesurer 0 contre 0.

**Je changerais d'avis dans trois cas :**
- **en faveur de conv-audit**, si X3 donne Δ ≥ 2 avec L > P₁ : l'ancrage existe, et notre lecteur ne le reproduit pas ;
- **contre tout proposeur agentique**, si X2 et X1 falsifient H_A : un apprenant sans agent et un traducteur sans idée suffisent, et le pôle devient un AutoML gelé sous juge ;
- **contre la prise exploration**, si X4b montre une fuite par tâche qu'aucune séparation praticable sur 120 épisodes ne ferme.

FIN-DE-CELLULE