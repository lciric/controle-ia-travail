# Cellule B, tour III.1 : une mémoire qui alimente le juge avant de conseiller le proposeur

**Pièces.** Toutes sont présentes. M2 et J2 sont des extraits déclarés comme tels, sans coupure visible. Deux pièces sont seulement citées, jamais servies : `selection_pari.py` et le rapport de méta-conception v6.3. Ce que je dis du nul augmenté vient donc uniquement de J et J2. Le tour est à l'aveugle : je ne vois ni A ni C, et je n'attaque que la question et les pièces.

## Thèse en cinq points réfutables

1. **La garde actuelle ne garde presque rien** [RAPPORTÉ, lecture du code M1, non exécuté].
   - `chercher_redites` compare le seul `enonce` aux seules éliminées, par Jaccard des 3-grammes de caractères au seuil 0,5.
   - La prédiction n'est examinée qu'ensuite, et par égalité exacte de `signature_prediction` : signe, valeur, métrique, seuil et empreinte de la loi.
   - Une copie renommée sous 0,5 n'atteint donc jamais la comparaison des prédictions. Une copie au-dessus de 0,5 la franchit en remplissant `ce_qui_change` et en déplaçant le seuil d'un millième.
   - Les voisines des survivantes ne sont pas examinées du tout.
2. **La redite doit se définir par le contenu, pas par la forme** [HYPOTHÈSE].
   - Notons 𝒜(H) la fermeture aveugle d'une entrée archivée H : l'ensemble des lois g∘p_H, où g est un post-traitement qui ne dépend pas des traits (mélange avec une loi aveugle, inclinaison par issue, changement de température).
   - H′ est une redite de H si, sous la loi vraie, H′ n'apporte rien au-delà de 𝒜(H).
   - Cette définition n'est observable que dans des mondes à loi plantée. Ailleurs, on l'approche par un test de suffisance sur des instances de sonde tenues par le noyau.
3. **Le traitement doit être asymétrique** [HYPOTHÈSE].
   - **Survivantes.** Leur fermeture 𝒜 entre dans le nul augmenté. Une redite « positive » ne peut alors pas être promue comme neuve : elle compte comme réplication.
   - **Éliminées.** On ne bloque pas, on **dépense α par classe d'équivalence**.
   - Le danger d'une redite d'éliminée n'est pas d'abord le gaspillage. C'est la multiplicité : m retentatives indépendantes d'une loi fausse, chacune au niveau α = 0,05, mènent jusqu'à 1 − 0,95^m de promotions de classe, soit environ 0,40 pour m = 10 (calcul à partir du α des faits).
4. **Pour la redite, la garde de mémoire est un préfiltre économique ; la validité reste au juge** [HYPOTHÈSE]. Si la fermeture aveugle entre dans le juge (E1), la mémoire n'a plus à trancher qu'une seule question : est-ce que cela vaut le coût d'une expérience ?
5. **Les témoins ne peuvent pas prouver que la mémoire aide le proposeur** [HYPOTHÈSE, tirée de la conception C].
   - Les témoins sont plantés, pas proposés. Ils mesurent le juge, pas les découvertes.
   - Le point 4 de la question (« découvertes vraies sur les témoins par dollar ») mesure donc la mauvaise chose. Il faut des mondes plantés, où le noyau calcule le gain oracle de chaque fiche proposée.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Ce qui manque |
|---|---|---|---|
| S1 | Une mémoire peut améliorer les propositions. | HYPOTHÈSE | Aucune ablation probante. M2 dit « aucune conclusion » (agents simulés qui ne lisent pas la mémoire). S1 liste l'apport de la mémoire parmi « ce qu'aucun modèle n'a pu établir ». |
| S2 | Le proposeur reçoit la mémoire. | RAPPORTÉ (M1) : faux aujourd'hui en partie | `texte_consigne` ne sert que deux rôles. L'expérimentateur reçoit les gabarits et la dernière leçon. La recombinaison reçoit la dernière leçon. Aucun rôle ne reçoit les éliminées avec leur cause. |
| S3 | Les redites sont assez fréquentes pour peser. | HYPOTHÈSE | Seul chiffre : une redite sur 26 fiches, avec des agents simulés qui ne lisent rien (M2, sans conclusion). Le taux de base avec de vrais agents est inconnu. |
| S4 | « Toute garde fondée sur le texte » est franchie par les tricheurs. | Deux statuts | Vrai par construction pour Jaccard sur `enonce` (RAPPORTÉ, code). HYPOTHÈSE pour les plongements sémantiques : non mesuré. Les tricheurs de S2 viennent d'équipes rouges ; leur passage n'est pas établi par une course décrite dans les pièces. |
| S5 | Chaque fiche engage une loi évaluable sur des instances quelconques. | HYPOTHÈSE | En mode seuil (`demonstration-v1`), la loi est absente : `signature_prediction` ne l'inclut qu'« en sélection par pari ». La signature prédictive impose donc le mode pari partout. |
| S6 | Un « jeu fixe d'instances de sonde » existe entre fiches. | HYPOTHÈSE, douteuse | Des fiches de domaines éloignés n'ont pas le même schéma de traits. Une sonde n'a de sens qu'à schéma égal, et les filles recombinées changent de schéma. |
| S7 | Le juge produit des verdicts sûrs sur lesquels bâtir la mémoire. | RAPPORTÉ, exploratoire, non opposable | J2 : l'expérience 1 n'a pas tourné. Le critère des filles promeut « parent + loi aveugle fixe » 58/200 (v0) et 63/200 (v1), et encore 5/20 après l'ajout du huitième tricheur (graine 777). Une mémoire construite sur ces verdicts hérite de leurs erreurs. |
| S8 | Les « transformations aveugles » forment une équivalence bien définie. | HYPOTHÈSE (dérivation ci-dessous, à vérifier par essai unitaire) | Le mélange n'est pas inversible. Les deux signatures proposées ne couvrent pas les mêmes transformations. |
| S9 | Viser une survie intermédiaire maximise l'apprentissage. | HYPOTHÈSE | La survie mêle vérité et facilité du test. On peut fabriquer une survie de 0,5 en choisissant un seuil, sans rien apprendre de vrai. |
| S10 | Le registre de Brier mesure la calibration. | RAPPORTÉ (M1, champ `lecture`) : seulement sous nul connu | Hors témoins faux, l'écart mêle calibration et proportion de vraies. Le registre n'est d'ailleurs servi à aucun agent. |
| S11 | Les gabarits « sévères » sont sévères. | RAPPORTÉ (M1) : tri sur `severite_attendue` déclarée | La sévérité est annoncée par l'auteur, pas mesurée. Déclarer une sévérité basse fait entrer son protocole dans la bibliothèque : c'est une porte de Goodhart (HYPOTHÈSE). |

**Dérivation pour S8** [HYPOTHÈSE, à confirmer par un essai unitaire, K = 3] :

- **Mélange.** Avec p′(k|x) = (1−λ)p(k|x) + λq_k et λ < 1, p′ est croissante en p(k|x).
  - Les **rangs par issue** sont invariants.
  - Les log-cotes ne le sont pas.
- **Inclinaison.** Avec p′(k|x) ∝ p(k|x)·e^{b_k}, les log-cotes ln p′(k|x)/p′(j|x) sont décalées d'une constante.
  - Les **log-cotes centrées sur la sonde** sont invariantes.
  - Les rangs par issue ne le sont pas en général pour K ≥ 3, à cause de la normalisation qui dépend de x.
- **Mélange suivi d'inclinaison.** Aucune des deux signatures n'est invariante.
- **Changement de température (β → kβ).** Les rangs restent invariants, mais la calibration change. L'équivalence par rangs **tue donc une recalibration**, qui peut être une vraie amélioration si l'éliminée était morte de surconfiance.
- **Changement d'échelle des traits sans changement de fonction.** Les prédictions sur sonde brute sont identiques : n'importe quelle signature le voit.

**Proposition.** Remplacer les deux signatures par un **test de suffisance** : peut-on ajuster une fonction ĝ, en validation croisée sur la sonde, telle que p′ ≈ ĝ(p_H) ?

- On mesure D = KL moyenne entre p′ et ĝ(p_H) sur des instances de sonde tenues hors ajustement.
- La redite est déclarée si D ≤ τ, où τ est étalonné sur des paires honnêtes.
- Ce test couvre toute la fermeture, compositions comprises.
- Il manque :
  - les lois qui coïncident sur la sonde et divergent ailleurs ;
  - la même loi éprouvée sur une population nouvelle, qui est une généralisation et non une redite ;
  - la redite par protocole, c'est-à-dire la même loi testée par une autre expérience, qui est une réplication légitime ;
  - tout ce qui traverse deux schémas de traits.

---

## (b) Expériences décisives

L'ordre est imposé. E1 à E3 tournent sur processeur et conditionnent la suite. E4 et E5 ne se lancent que si E1 et E2 passent : sinon, la brique « équivalence » sur laquelle repose la mémoire est invalide.

### E1 : la fermeture aveugle dans le juge

- **H_A.** On ajoute au nul augmenté un membre « fermeture aveugle » : le maximum, sur λ, q et b, de la vraisemblance de g∘p_parent, ajusté sur les tirages frais. J construit déjà ainsi la « marginale ajustée ».
  - Effet attendu : « parent + loi aveugle fixe » promu ≤ α.
  - Coût attendu : perte de puissance ≤ 0,05 sur les filles réellement neuves.
- **H_B.** La fermeture échoue, de l'une de deux façons :
  - le tricheur reste promu au-delà de α (borne basse de Wilson > α) ;
  - ou la puissance sur la fille neuve tombe sous 0,90, seuil de lecture de J.
- **Pourquoi H_A peut tenir** [HYPOTHÈSE].
  - Sous le nul « H′ = g∘p_parent », la loi vraie appartient à la famille. Le dénominateur la domine donc, et l'argument de Ville de J s'applique.
  - Sous dérive, ce n'est plus qu'une approximation, comme J le dit des filles (limite 4b).
  - Le coût attendu est de l'ordre de ½·dim(θ)·ln n nats sur les petits effets. Avec 5 paramètres et n = 200, cela fait environ 13 nats (illustratif, analogue au calcul de l'urne dans J), contre un seuil ln 20 ≈ 3,0. **E1 peut donc échouer par la puissance.**
- **Métrique.** Taux de promotion, avec les réglages de J : 1 000 répétitions, 200 tirages frais, K = 3, α = 0,05, graine maîtresse neuve.
- **Cas.**
  - Tricheurs : mélange fixe (q permutation de (0,45 ; 0,1 ; 0,45), comme J2), inclinaison, mélange suivi d'inclinaison, température.
  - Cas honnêtes appariés : fille = parent + composante vraie sur un trait (ε = 0,2 et ε = 0,05), plus la batterie T1b-fille.
- **Contrôle d'artefact** (il doit être vu, sinon le contrôle n'a pas de dents) : le juge v1 sans fermeture, sur graine neuve, doit montrer le trou avec un taux > α.
- **Issue qui falsifie.**
  - Tricheurs ≤ α et puissance ≥ 0,90 : H_B est falsifiée, et les redites positives sont traitées par le juge.
  - Sinon, H_A est falsifiée, et l'on dit quelle porte a cédé (tricheur ou puissance). Une garde de mémoire séparée devient alors nécessaire, et E2 décide de sa forme.

### E2 : quel encodage détecte l'équivalence ?

- **Banc.** Des paires (entrée archivée, fiche nouvelle) dans des mondes plantés à schéma de traits fixe.
  - **Positifs** : tricheurs scriptés (renommage, jargon rare, paraphrase, changement d'échelle des traits, mélange, inclinaison, compositions).
  - **Négatifs appariés** : des fiches honnêtes au texte quasi identique (Jaccard ≥ 0,5 sur l'énoncé, même domaine, même opérateur) mais dont la loi ajoute une composante vraie.
  - **Vérité** : l'oracle, c'est-à-dire le gain sous la loi vraie au-delà de 𝒜(H) comparé à δ.
- **H_A.** Le test de suffisance sur sonde cachée atteint un TPR ≥ 0,90 à FPR ≤ 0,05. Il bat d'au moins 0,10 en TPR à FPR égal, avec un intervalle apparié dont la borne basse est > 0, la meilleure des vérifications mécaniques :
  - Jaccard de M1 ;
  - égalité de `signature_prediction` ;
  - rangs par issue seuls ;
  - log-cotes centrées seules.
- **H_B.** Une de ces vérifications, ou un plongement sémantique, fait aussi bien ou mieux.
- **Prédictions signées** [HYPOTHÈSE] :
  - les rangs ratent l'inclinaison ;
  - les log-cotes ratent le mélange ;
  - Jaccard rate le renommage et rejette des honnêtes.
- **Ce qui réfute ma dérivation de (a).** Si les rangs ou les log-cotes attrapent tous les positifs composés.
- **Contrôles.**
  - Négatif : un encodage aléatoire, une direction par fiche comme le « nul » de G2, doit donner une aire sous la courbe d'environ 0,5.
  - Sain : la copie exacte doit être détectée à 100 %.
  - Si le contrôle négatif dépasse 0,6, le banc fuit et E2 est nulle.
- **Coût mesuré.** Nombre d'instances de sonde nécessaires pour atteindre le TPR visé (balayage de 50 à 2 000, illustratif).

### E3 : dépense d'α par classe face à des retentatives adverses

- **H_A.** Avec α_j = α·2^{−j} pour la j-ième fiche d'une même classe détectée, la probabilité qu'au moins un membre d'une classe fausse soit promu reste ≤ α. Cela tient face à un proposeur scripté qui retente m = 10 transformations aveugles d'une loi éliminée.
- **H_B.** Les faux négatifs du détecteur d'E2 font fuir la classe : taux de promotion de classe > α.
- **Contrôle d'artefact.** Sans dépense, le taux de classe doit dépasser α nettement.
  - S'il ne le fait pas, Ville étant conservatrice, la multiplicité n'est pas une menace réelle ici.
  - La prémisse « validité » de ma thèse 3 est alors falsifiée, et la garde redevient purement économique.
- **Cas honnêtes appariés.** Une loi vraie éliminée une première fois par un test faible (n petit), puis reproposée avec n plus grand. On rapporte sa puissance sous α_j.
- **Issue qui falsifie.**
  - Taux de classe > α : H_A est falsifiée.
  - Taux ≤ α avec une puissance de reproposition ≥ 0,80 (illustratif) : H_B est falsifiée.

### E4 : l'ablation avec de vrais agents, dans des mondes plantés

- **Bras**, à budget égal en dollars et en jetons de consigne (rembourrage neutre si nécessaire) :
  1. sans mémoire ;
  2. mémoire B : fermeture dans le juge, dépense d'α, consigne décrite plus bas ;
  3. **placebo** : mémoire d'une course dans un autre monde planté de **même schéma**, au format identique et au contenu faux pour ce monde ;
  4. **mémoire empoisonnée** : 20 % des verdicts inversés (illustratif) ;
  5. facultatif : mémoire M1 telle quelle.
- **Métrique principale.** Gain oracle net cumulé des survivantes nouvelles, par dollar, à la génération G. Le gain oracle se mesure en nats sous la loi vraie, au-delà de la fermeture de l'archive.
- **Métriques secondaires.**
  - Taux de redites oracle par génération.
  - Nombre de structures plantées distinctes retrouvées (diversité).
  - Garde-fou : taux de témoins faux gardés et de témoins vrais éliminés, inchangé entre les bras.
- **H_A.** Le bras 2 moins le bras 3 donne un gain > 0, avec une borne basse d'intervalle > 0 et un effet ≥ un minimum fixé au scellement.
- **H_B.** Le bras 2 moins le bras 3 donne ≤ 0, ou un intervalle qui contient 0 avec un point sous le minimum.
- **Lectures.**
  - 2 ≈ 3 > 1 : « le contexte aide, pas le contenu ».
  - 4 < 1 : « une mémoire non vérifiée nuit ».
  - 2 ≤ 3 + minimum : **« la mémoire n'aide pas », sur ce banc.**
- **Contrôle de manipulation, sans lequel aucune conclusion n'est permise.** Le taux de redites doit baisser dans le bras 2 par rapport au bras 1. S'il ne baisse pas, les agents ne lisent pas la mémoire, et l'issue est « non concluant », pas « n'aide pas ». C'est exactement le défaut de M2.
- **Plan.** Au moins 4 générations après la première génération non vide, parce que la mémoire est vide en génération 0. Appariement par monde. Test de permutation sur les différences par monde. Par exemple 6 mondes × 2 graines × 6 générations (illustratif ; puissance à calculer sur un pilote déclaré, R-473).

### E5 : viser une survie intermédiaire

On peut l'ajouter comme bras d'E4 pour économiser.

- **H_A.** Orienter les propositions vers des régions à survie estimée entre 0,3 et 0,7 augmente le gain oracle par dollar, par rapport à une exploration uniforme. Les régions sont définies par des descripteurs **calculés par le noyau à partir de la loi** (traits dont dépend la loi, divergence au nul), pas par le texte.
- **H_B.** Cette orientation augmente la survie sans gain oracle, voire en le baissant : le pôle apprend le facile.
- **Métriques.**
  - Gain oracle par dollar.
  - Fraction des survivantes dont le gain oracle est ≤ δ (survivantes vides).
- **Contrôle d'artefact.** Un bras « viser une survie haute » doit montrer une survie en hausse sans gain oracle. Si ce n'est pas le cas, la métrique n'a pas de dents.
- **Issue qui falsifie.**
  - Gain oracle du bras intermédiaire ≤ gain du bras uniforme : H_A est falsifiée.
  - Gain supérieur, avec une fraction de survivantes vides non accrue : H_B est falsifiée.

---

## Réponses courtes aux points 1 à 3 de la question

Ce sont des HYPOTHÈSES, à départager par E1 à E5.

### Encodage par usage

| Usage | Encodage proposé | Coût | Mode d'échec |
|---|---|---|---|
| Détecter une redite | Test de suffisance sur sonde cachée, à schéma égal. Le texte ne sert que de préfiltre de coût. La structure canonisée (opérateur, variables, signe) sert entre schémas. | Faible : n_sonde × K évaluations par paire. | Lois égales sur la sonde mais différentes hors sonde. Généralisation à une population nouvelle prise pour une redite. |
| Retrouver ce qui sert au proposeur | Structure, verdict avec sa cause et protocole. Le rappel par plongement est acceptable ici, car un faux positif coûte peu. | Faible. | Effondrement de la diversité (on copie ce qui a marché). Héritage des verdicts faux. |
| Attribuer le mérite | Log-richesse de la fille contre le nul augmenté par la fermeture de ses parents : sa contribution nette, pas sa survie. | Déjà calculée par le juge. | Approximation seulement sous dérive (J, limite 4b). |

### Consigne du proposeur

Elle contient :

- les classes éliminées, avec leur cause et le **budget α restant** de chaque classe ;
- les survivantes, comme marchepieds, avec leur fermeture explicite (« pour être promue, il faut battre ceci ») ;
- les protocoles classés par **richesse observée**, pas par sévérité déclarée ;
- un budget d'exploration fixe, uniforme sur les descripteurs (par exemple 20 %, illustratif).

Elle ne contient jamais :

- les témoins ;
- les instances de sonde ;
- un verdict non vérifié par l'autre famille.

### Contre l'empoisonnement

- Tout verdict entre en mémoire avec son statut : vérifié ou non, scellé ou non.
- Un échantillon tiré au hasard des survivantes est rejoué sur l'évaluation scellée.
- La fermeture d'une **éliminée** n'entre pas dans le nul, puisque son verdict peut être faux. Seule la dépense d'α s'applique, ce qui évite de bloquer définitivement une vérité éliminée à tort.

---

## (c) Instruments nommés : mesure minimale de fonctionnement

| Instrument | Il doit détecter | Cas honnêtes appariés | Vérification mécanique à battre | Mesure minimale |
|---|---|---|---|---|
| Garde Jaccard des 3-grammes (M1) | Redites d'éliminées | Fiches au texte proche et à la loi neuve | Aucune : c'est le témoin faible. | TPR et FPR sur le banc d'E2. Prédiction signée (HYPOTHÈSE) : TPR faible sur renommage et jargon rare, FPR élevé sur les honnêtes proches. |
| Plongements sémantiques | Paraphrases | Idem, plus des homonymes | Jaccard ; égalité de `signature_prediction` | Gain de TPR à FPR ≤ 0,05 sur le banc d'E2. Le jargon rare est rapporté à part. |
| Encodage structurel | Variables renommées, même opérateur | Même opérateur avec un signe ou une condition différente | Empreinte de la structure canonisée (tri des variables, alpha-renommage) | TPR et FPR sur le banc d'E2, entre schémas uniquement. |
| Signatures invariantes (rangs, log-cotes centrées, suffisance) | Redites modulo transformation aveugle | Recalibrations vraies (température), composantes vraies faibles | Rangs seuls ; log-cotes seules (E2) | TPR ≥ 0,90 à FPR ≤ 0,05 ; aire sous la courbe du contrôle aléatoire ≈ 0,5 ; nombre minimal d'instances de sonde. |
| Juge à nul augmenté par la fermeture | Fille sans apport sur les traits | Fille avec une composante vraie (ε = 0,2 ; 0,05) | Juge v1 sans fermeture (le trou doit être vu) | Promotion des tricheurs ≤ α ; puissance ≥ 0,90 (E1). |
| Registre de calibration (Brier) | Source qui surestime la sévérité de ses tests | Source calibrée de même effectif | Test binomial « survie observée contre sévérité annoncée » sur les témoins faux | Détection d'une surestimation injectée (par exemple un facteur 3, illustratif) et taux de fausses alertes sur la source calibrée, à effectif de témoins égal. Si Brier ne bat pas le test binomial, le registre est superflu. |
| Bibliothèque de protocoles | Protocoles qui donnent des tests puissants | Protocole tiré au hasard parmi les survivantes | Tri par sévérité déclarée (actuel) contre tri par richesse observée | Puissance des expériences qui reçoivent un gabarit, contre un gabarit au hasard. On rapporte aussi le taux de gabarits venus d'une survivante fausse (mondes plantés). |
| Leçons en texte | Causes d'échec réutilisables | Le même résumé servi en JSON brut (`resume_pour_synthese`) | Résumé mécanique sans agent de synthèse | Sous-bras d'E4 : la leçon doit battre le JSON brut en gain oracle par dollar. Test d'empoisonnement : taux de propagation d'une leçon qui contient un verdict faux. |
| Archive qualité-diversité par descripteurs | Effondrement de la diversité | Archive à îlots sans descripteurs | Tirage stratifié par domaine estimé (S2) | Nombre de structures plantées retrouvées à budget égal. |
| Témoins | Qualité du juge | Fiches proposées de même forme | Classifieur, ou agent, chargé de repérer les témoins | Taux de repérage ≤ hasard + ε. Au-delà, les témoins cessent de mesurer (docstring de M1). |
| Mémoire placebo | Effet du seul contexte | Mémoire vraie de même format | Agent chargé de dire laquelle est la vraie | Le placebo doit être indiscernable par sa forme. Seul son contenu est faux pour le monde courant. |

---

## (d) Ancrage matériel

Tout ce qui suit est **illustratif** sauf mention contraire.

- **E1 à E3 : processeur seul, bibliothèque standard, comme le juge v1.**
  - Ordre de grandeur : quelques heures de processeur pour 1 000 répétitions par contrôle.
  - Coût monétaire proche de 0.
  - Les 105 essais du juge v1 existent (RAPPORTÉ, J2) et servent de socle. On ajoute des essais unitaires : invariances de (a) sur des lois connues, ajustement de la fermeture, dépense d'α.
- **E4 et E5 : vrais agents.**
  - **Modèles ouverts, deux familles distinctes**, puisque C exige un vérificateur d'une autre famille : par exemple Qwen2.5-32B-Instruct comme proposeur et expérimentateur, Llama-3.1-70B-Instruct ou Mistral-Small comme vérificateur.
  - **Plongements** pour le bras sémantique : par exemple bge-m3.
  - **Volume** : 6 mondes × 2 graines × 4 bras × 6 générations × 6 fiches, soit environ 1 700 fiches.
  - **Jetons** : environ 60 000 par fiche (proposition, expérience, vérification), soit environ 100 millions au total.
  - **Coût de location** : sur un ou deux GPU de classe H100 avec un serveur d'inférence par lots, environ 2 à 4 jours, pour 150 à 500 USD.
  - **Point de comparaison non transposable** : les 152,7 contre 150,8 « dollars simulés » de M2 (RAPPORTÉ) viennent d'agents simulés.
- **Mondes plantés.** Simulateurs sur processeur. Le noyau tient la loi vraie, la graine des instances de sonde et le calcul oracle ; aucun agent ne voit ces éléments.

---

## Ce qui réfuterait la proposition B elle-même

- **E1 réussit et E3 montre que la multiplicité ne menace pas.** La mémoire n'a alors aucun rôle de validité. Ma thèse 4 se réduit à « préfiltre de coût », et la garde peut rester rudimentaire.
- **E2 : les rangs ou les log-cotes seuls suffisent.** Ma dérivation de (a) est fausse, ou sans portée pratique.
- **E4 : 2 ≈ 3, avec un contrôle de manipulation réussi.** C'est le contenu de la mémoire qui est inutile, y compris dans ma version.
- **E5 : le bras intermédiaire bat l'uniforme sans hausse des survivantes vides.** Mon scepticisme sur S9 est réfuté.

FIN-DE-CELLULE