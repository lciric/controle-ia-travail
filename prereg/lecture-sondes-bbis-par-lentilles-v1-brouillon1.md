# Préenregistrement descriptif — lecture, par nos lentilles, des directions des sondes apprises sur la tâche (étape B bis de T0.7) — v1 — brouillon 1

- **Auteur** : rédacteur neuf, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1` (modèle servi : Opus 5.5), sur le mandat
  `docs/notes/neuron-lens-v1/mandat-redacteur-texte-lecture-sondes-bbis-par-lentilles-v1.md`
  (`3010f726510856f202c62b5acd9c50166e1bd4860d88f45f1d50ca951cd732bb`, vérifié contre son compagnon). Il n'a écrit ni T0.6, ni T0.7,
  ni aucune pièce de l'apprentissage des sondes sur la tâche (texte, addenda, code), ni P3-bis, ni aucune pièce de la tranche de
  l'ajustement de nos lentilles (texte gelé, addendum, commande, devis, code) ; il ne sera ni développeur, ni opérateur, ni lecteur de
  ce texte, ni lecteur ou juge d'aucun verdict (apprentissage des sondes sur la tâche, étape B, table conjointe, P3-bis, tranche des
  lentilles).
- **Date (UTC, `date -u`)** : 2026-11-18 ; lecture des pièces à partir de 16:41 ; entropie des graines tirée à 16:49:33 ; brouillon
  écrit de 16:58:55 à 17:02:37 (`date -u` relevé juste avant les dernières vérifications et le scellement comme brouillon).
- **Commit du code d'analyse** : **aucun code n'existe**. Écart au gabarit demandé (nœud N3) : le code sera cité après le scellement,
  par la ligne `CODE-LENTILLES-BBIS` du registre propre, avant toute exécution. Commits lus : branche de travail de la mère
  `claude/affectionate-bardeen-j7kddp` à `08476acff2d6158f40d4cd318668bd18c5cbb391` ; branche des lentilles
  `claude/brave-galileo-jhp684` à `310ca57b2b1bc2586b35571d8f6e84d313ab36ec`.
- **Documents qui font foi (chemin + empreinte)** :
  - mandat (ci-dessus) ;
  - apprentissage des sondes sur la tâche, lus **pour la forme de leurs sorties seulement** : texte scellé
    `prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb` (« T ») ; premier addendum
    `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`, `f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7` (« A1 ») ;
    second, `…-addendum-ecart-2-v1.md`, `18baeac32d26ebf174c62d7a36caedeee1d5b80648c6743c21dc30d2747afd26` (« A2 ») ; troisième,
    `…-addendum-ecart-3-v1.md`, `e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872` (« A3 ») ;
  - tranche de l'ajustement de nos lentilles (branche `claude/brave-galileo-jhp684`, dossier `docs/notes/neuron-lens-v1/`) : texte
    gelé `texte-gele-tranche-b-beta-v1.md`, `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454` (« G ») ; addendum des
    empreintes, partie 1, v3, `addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md`,
    `bd8067dcd04ae32bb5960dc95bef89384b3b914a1a35e918107411f43d1c95f1` ; commande v6, `commande-b-beta-v6.md`,
    `23c431d3040696fde477b46d6f214741fbcbfc2887b3213c737fe9e2b7f988cd` (la plus récente du dossier ; un « code de course v3 »,
    commit `a5ae50a65`, titre seul vu, a pu la suivre) ; devis v12, `devis-b-beta/devis-tranche-b-beta-v12.md`,
    `41a4c1f6dc5c2fe59be06d49e76425d857f79338b6bd29aac95ecfa3533294f1` (lieux de rangement et § 4 seulement ; lecture hors de la
    liste du mandat, déclarée) ;
  - gabarit `prereg/gabarit-preregistrement-v1.md`, `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` ; validateur
    `src/controle_ia/prereg.py`, `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` ;
  - code lu pour définir la direction d'une sonde et sa couche (hors de la liste du mandat, déclaré) :
    `src/controle_ia/sondes/familles.py`, `6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e` (l'empreinte que cite T,
    l. 19) ; `src/controle_ia/harnais/activations.py`, `adeb5856d430f3a6163989c2a53c8ced459235c6dcdd03834b694404c57e0095` (l. 1-80).
- **Statut** : **brouillon 1**, scellé comme brouillon (compagnon `.sha256`) ; aucune machine, aucune dépense, aucun résultat lu. Il
  ne vaut préenregistrement qu'après contre-lecture par un agent neuf d'un autre modèle, traitement des remarques, nœuds tranchés,
  scellement d'une version et ligne `SCELLEMENT-LENTILLES-BBIS`, **strictement avant toute lecture humaine d'une sortie de
  l'apprentissage des sondes sur la tâche** (au plus tard avant que le lecteur de son verdict ouvre sa lecture ; contrôle : « Plan
  d'analyse », point 1).

## Ce que l'auteur savait avant le scellement

- **Lu** : le mandat (entier) ; T (entier, pour la forme des sorties : c'est un préenregistrement, il ne porte aucun résultat) ; A2
  (l. 1-48 et 216-353, et les lignes qui nomment branche, fichiers des sondes et des scores) ; A3 (l. 1-95, et les lignes qui nomment
  la branche de sortie) ; A1 (les seules lignes qui nomment branche, fichiers, couche ou direction, par recherche) ; G (l. 1-560 :
  en-tête, documents, « Hypothèse » à « Liste d'arrêt » ; non lues : l. 561-667) ; l'addendum des empreintes v3 (entier) ; la commande
  v6 (entière) ; le devis v12 (lignes qui nomment les lieux de rangement, par recherche ; § 4, l. 282-315) ; l'en-tête (3 000 premiers
  caractères) de `docs/notes/neuron-lens-v1/verification-courte-commande-v13-v14-mere-v1.md`, pour savoir si une commande plus récente
  de la tranche existait (elle porte sur la commande du volet A, non sur cette tranche) ; le gabarit, le validateur,
  `sondes/familles.py` (entier), `harnais/activations.py` (l. 1-80), quelques lignes de `scellement.py` ; les règles de `CLAUDE.md`.
- **Valeurs vues** (aucune n'est une aire, un score, une issue ou un verdict d'une chaîne interdite) : dans G, des valeurs de la tranche
  des lentilles publiques et de la référence publiée sur Qwen3-8B (prédictions et seuils de G) ; dans T, des valeurs de planification
  (puissance) reprises de T0.7 et du texte de validité ; dans les addenda, des valeurs techniques de contrôle (« écart « attention »
  2,131·10⁻² » de la course arrêtée le 16 novembre ; « écart 5,18 sur le jeu 2 » d'un diagnostic ; des comptes d'essais) ; les durées et
  prix du devis v12.
- **Vu sans ouvrir** : les noms des fichiers de `docs/notes/neuron-lens-v1/` (local et branche des lentilles) et de ses sous-dossiers
  `devis-b-beta/`, `outils-b-beta/`, `correctifs-b-beta/`, `passations/` ; les noms des textes `prereg/T0.7-etape-B-bis-v1*` ; les noms
  des modules de `src/controle_ia/harnais/` ; les titres des huit derniers commits de la branche des lentilles et des trois derniers de
  la branche de travail, dont « garde de priorité de l'étape B bis (crédit < 12 USD → destruction des lentilles) », « code de course v3
  (ligne de calcul GO-2026-11-18-35 exigée par le lanceur) », « GO-2026-11-18-35 à -37 : lentilles en parallèle », et deux titres qui
  nomment une « épreuve des témoins » (« épreuve des témoins échouée », R-3311 ; « reprises de l'épreuve des témoins tant que l'échec
  est technique », R-3320), dont l'auteur ignore l'objet.
- **Jamais vu** : aucun fichier sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucune branche `calcul/` ou `donnees/` ; aucun
  fichier de `registres/` ; aucune sortie de 7a, 7b, T0.6, T0.7 (étape A comprise), de la base « mots et coût », de l'étape B, de
  l'apprentissage des sondes sur la tâche, de P3-bis ; aucun résultat de la tranche de l'ajustement de nos lentilles (G dit qu'il n'en
  existait aucun). **Aucun choix de ce texte (directions, lentilles, k, nuls, familles de jetons, libellés) n'a pu être fait d'après
  une sortie de ces chaînes.**

## Vocabulaire (noms en clair ; les identifiants viennent en appui)

- **Apprentissage des sondes sur la tâche** : l'étape B bis de T0.7 (T, A1 à A3). Ses **cellules plafond** : l'organisme à consigne
  cachée (« instruit », cellule P-instruit) et l'adaptateur saboteur aux doses 0,25 à 1 (P-S25 à P-S100) ; deux **plis externes** par
  cellule. **Sonde apprise** : la sonde finale d'une cellule et d'un pli (T, plan, point 5). **Lecteur honnête à capacité égale** : la
  même recette, apprise sur les activations du modèle nu lisant les mêmes textes (ENC dans T).
- **Direction d'une sonde** : le vecteur `w` de l'interface du harnais, dans les coordonnées brutes du flux résiduel à la couche ℓ de la
  sonde (sortie du bloc ℓ, avant la normalisation finale : `harnais/activations.py`, l. 3-5), normalisation repliée
  (`sondes/familles.py`, l. 16-18 et 233-237) ; pour la famille « attention », aussi la **requête** `q`, dans les mêmes coordonnées.
  **Signe +** : vers la classe positive (saboteur pour une sonde apprise ; texte du saboteur relu par le modèle nu pour un lecteur
  honnête).
- **Nos lentilles** : celles de la tranche de l'ajustement de nos lentilles (G) : **lentille côté sortie** (R : lit ce qu'une direction
  écrite dans le flux pousse vers la sortie) et **lentille côté entrée** (S : lit quels jetons d'entrée une direction lue capte), à la
  cible « sortie du bloc » (`out`). **Références** : la **lentille des logits** ; la **lentille côté sortie publique** de Neuronpedia
  (`npR`).
- **Pôle** : un neurone à porte de la couche, pris à un signe (deux par neurone, 28 672 par couche ; G, M.2).
- **Nul isotrope**, **nul des signes**, **concentration**, **part au-dessus du nul**, **familles de jetons nommées d'avance**, **pôles
  alignés** : définis en « Métrique ».

## Hypothèse

- **Objet, descriptif** (mandat ; question de Lazar, « et si on fait un nouveau texte scellé ? », pour que la lecture par lentille
  neuronale entre dans le billet sur les sondes) : décrire quels jetons et quels pôles nos lentilles associent aux directions que
  l'apprentissage des sondes sur la tâche aura apprises, à la couche où chaque sonde lit, et si cette lecture se distingue de
  directions aléatoires de même norme. **Aucune revendication, aucune hypothèse soumise à un seuil de rejet.** Aucune hypothèse du
  programme (H1 à H8, HC) n'est testée, modifiée ni revendiquée ; rien n'entre dans G0 (critère 3 compris), G1, T0.7 ni T0.8 sans nœud
  de Lazar.
- **Questions** : par notre lentille côté sortie (et côté entrée, nœud N2), à la couche de la sonde : (i) quels sont les premiers jetons
  de chaque direction, et la lecture est-elle plus concentrée que celle de directions aléatoires ? (ii) les familles de jetons nommées
  d'avance (« nombres », « coût ») y sont-elles plus fréquentes que sous le nul ? (iii) quels pôles de la couche écrivent le plus près
  de la direction, et que lit la lentille de ces pôles ? (iv) en quoi la lecture d'une sonde apprise diffère-t-elle de celle du lecteur
  honnête de même cellule, de l'autre pli, des autres doses, de la lentille des logits et de la lentille publique ?
- **Hypothèses de travail** : modèle `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659` (celle de
  T et de G) ; la couche ℓ d'une sonde (7, 15 ou 23 ; T, « Hypothèse ») est la sortie du bloc ℓ, que lit la cible `out` de nos
  lentilles à la même couche (la cible `out` de la lentille côté sortie couvre les couches 0 à 30 ; G, M.1) ; une lecture par lentille
  dit ce qu'une direction **pousse en moyenne**, non ce qu'elle fait sur un épisode (G, « Critères ») ; **règle de lecture** reprise
  de G : une lecture par lentille peut ajouter un soupçon sur une sonde, jamais la blanchir.
- **Lectures rivales que la description éclaire, sans les départager** : la sonde lit le texte (comparaison au lecteur honnête) ; elle
  lit le nombre déclaré ou le champ du coût (familles « nombres » et « coût » ; c'est la lecture sans le champ du coût de T qui en
  traite) ;
  elle lit une structure de surface (nul des signes, témoin de couche).

## Prédiction chiffrée et signe attendu

R3 : aucune course ne vise un signe ; texte descriptif, **aucune prédiction n'est décisive**. Attentes de l'auteur, déclarées pour
mémoire, chacune avec ce qui la réfuterait ; une attente réfutée est rapportée et ne change rien.

| attente | réfutée si | confiance |
|---|---|---|
| A-1 : au moins une des dix sondes apprises est, par notre lentille côté sortie à sa couche, « concentrée au-delà des deux nuls » (« Critères de lecture gelés »), à un signe au moins | aucune ne l'est | 0,55 |
| A-2 : la famille « nombres » ou la famille « coût » est « sur-représentée » dans les vingt premiers jetons d'au moins une sonde apprise sur l'adaptateur saboteur (P-S25 à P-S100), par notre lentille côté sortie | aucune ne l'est | 0,35 |
| A-3 : parmi les directions lues aux couches 23 et 7, la part des lectures « concentrées » est plus haute à 23 | part plus haute ou égale à 7 ; sans objet si l'une des deux couches n'a aucune direction | 0,5 |
| A-4 : à même cellule, même pli et même couche, le cosinus entre la sonde apprise et le lecteur honnête est positif pour la plupart des paires | positif pour la moitié des paires ou moins ; sans objet sans paire de même couche | 0,6 |

## Entrées exactes, et ce qui n'est jamais ouvert

**De l'apprentissage des sondes sur la tâche** (course du second addendum, chaîne v6 du troisième ; branche de sortie
`donnees/t07-etape-b-bis-v2`, A2, SA-16 ; A3, TA-1 ; `<run-bbis>` = le dossier de course nommé par la ligne `SCORES-BBIS` de son
registre propre, `registres/t07-etape-b-bis-v1.md`) :
- **E-1** `donnees/<run-bbis>/sondes-bbis.npz` — « poids des sondes finales et d'ENC » (T, « Données gardées ») : pour chaque cellule
  plafond (cinq) et chaque pli externe (deux), la sonde apprise et le lecteur honnête, soit **vingt sondes** ; lus par programme : `w`,
  `b` (pour l'empreinte seulement), `q` s'il existe, et, s'ils y sont, la couche et la famille. Les noms exacts des clés sont pris dans
  le code qui écrit ce fichier, au commit cité par la dernière ligne `CODE-BBIS` (lecture de code, jamais des données).
- **E-2** `diag/<run-bbis>/sondes-bbis.json` — lu par programme, **liste blanche de champs** : pour chaque sonde, cellule, pli, rôle
  (sonde apprise ou lecteur honnête), famille, agrégation, couche, empreinte (noms exacts des champs pris dans le code qui écrit ce
  fichier, comme pour E-1). Aucun autre champ (régularisation, graines, contrôle
  carte-processeur, réglage et empreinte de la sonde de l'ordre 2, résumé de la mesure de dispersion, empreintes des directions du
  plancher ; A2, SA-18) n'est lu ni écrit dans un journal.
- **E-3** les compagnons `.sha256` de E-1 et E-2 ; la ligne `SCORES-BBIS` (chemin, empreinte) ; la présence de la clé `VERDICT-BBIS`
  dans le même registre (clé et heure seulement, jamais le fichier du verdict).

**Jamais ouverts**, par personne de cette chaîne ni par son code : `donnees/<run-bbis>/scores-bbis-NNN.npz` (scores de la sonde, des
800 directions du plancher, des 100 sondes du nul de réétiquetage, du lecteur honnête, de la lecture sans le champ du coût, scores
d'apprentissage, **et poids des sondes de l'ordre 2**, qui ne sont donc pas lues ; A2, SA-17) ; `donnees/<run-bbis>/planchers-bbis-NNN.npz`
(directions du plancher) ; `diag/<run-bbis>/relecture-bbis.json` ; `runs/<run-bbis>/manifeste.json` ; tout journal de la course ;
`lecture-bbis.json`, `conjointe-bbis.json`, tout fichier de verdict ; la branche `donnees/t07-etape-b-bis-v1` (course arrêtée le 16
novembre) ; `lecture-t07.json` ; toute sortie de 7a, 7b, T0.6, T0.7 (étape A comprise), de la base « mots et coût », de l'étape B, de
P3-bis ; toute pièce de l'étiqueteur, du bras d'attaque ou du mode tenu à l'écart.

**De la tranche de l'ajustement de nos lentilles : aucune sortie versée ne porte nos lentilles.** Lieu retenu par Lazar : L1, « aucun
rangement ; seules les empreintes et les mesures dérivées sont versées » (devis v12, décision 2) ; G, P.3, étape 8 : « lentilles non
rangées (lieu L1 : elles disparaissent avec la machine) » ; G, P.6 : « Rien d'autre ne survit à la machine » ; commande v6, étape 12 :
ajustements et exports « restent sur la machine et disparaissent avec elle ». **Et la course des lentilles ne peut pas lire nos
sondes** : G, « Hypothèse » (« aucune sonde du programme n'est employée ou lue ») et « Liste d'arrêt » (« toute lecture touchant […]
T0.7 […] : interdit ; arrêt »). D'où le nœud N1. Entrées venues de la tranche, quelle que soit la voie : sa **recette** (G, addendum v3,
commande v6 : révisions, corpus de 932 documents, arguments, versions, correctifs) ; **après le prononcé de son verdict par son propre
lecteur** (G, P.7), la ligne du verdict d'ensemble et les empreintes de ses fichiers d'ajustement et d'exports (G, P.6), rien d'autre ;
l'empreinte attendue de la liste des jetons gardés de Llama, `c37186add16770aa3c04bd0c16c417544b7e2a15b374ee85e47fbda7ec148d68`,
89 498 identifiants (addendum v3, § 3).

**Sources publiques** (sur la machine de la voie retenue) : poids de Llama à la révision ci-dessus (`lm_head`, `model.norm`,
`embed_tokens`, `mlp.down_proj` des blocs 7, 15 et 23 ; clé selon R-3151) ; tokeniseur (`79e3e522…`, G) ; lentille côté sortie publique
`npR` (`neuronpedia/jacobian-lens`, révision `d2527c3cdbaa60dd4b65cbca1604921f044e989a`, fichier `a63a1588…`, addendum v3, § 2) ; corpus
DCLM, code voisin au commit `849bfe1678e28becceb1e3864afe5fc8297d02e4`, Drowse 6.1.4 (`673ed2b4…`), comme G.

## Métrique

1. **Directions lues** : pour chacune des vingt sondes de E-1, `w` et, pour la famille « attention », `q` (au plus quarante vecteurs),
   chacun aux deux signes. Norme nulle ou valeur non finie : « non calculable » (motif écrit). Les cellules de transfert n'ont pas de
   direction propre (sondes des cellules plafond, sans réapprentissage ; T, plan, point 9) : rien de plus à lire.
2. **Lecture côté sortie** d'un vecteur v à la couche ℓ : la fonction de lecture de la comparaison des lentilles
   (`checks/lens_compare.py`, l. 72-78 du code voisin, corrigé par le correctif (4) de G ; demi-précision de `unembed`, l. 47, comme
   publié ; jetons gardés de Llama), appliquée à v au lieu d'une colonne de `W_down`, avec notre lentille côté sortie, cible `out`, couche ℓ (export `R:dclm-llama`) ;
   notre code rend le **score de chaque jeton gardé** (89 498), non les seuls dix premiers. Même lecture par la lentille des logits et
   par `npR`.
3. **Lecture côté entrée** (si le nœud N2 la retient) : convention de la lecture côté entrée de G (`checks/reads_at_firings.py`,
   l. 84-107 : covecteur normé, produit avec `e_t − ē`, plongements des jetons gardés, centrés), avec notre lentille côté entrée, cible
   `out`, couche ℓ, appliquée au covecteur v ; l'espace (brut ou normalisé) où la matrice de la cible `out` prend un covecteur est fixé
   par le développeur d'après le code voisin, écrit et contre-lu avant le scellement de la version.
4. **Deux nuls construits d'avance** (graines : « Plan d'analyse », point 3) :
   - **nul isotrope** : M = 2 000 directions u_j ~ N(0, I) dans ℝ⁴⁰⁹⁶, ramenées à la norme de v ; tirées une fois par couche,
     partagées par toutes les directions et toutes les lentilles de cette couche ;
   - **nul des signes** : M = 2 000 directions u_j = ε_j ⊙ v, ε_j de coordonnées ±1 indépendantes et équiprobables ; tirées par vecteur,
     partagées par ses deux signes et toutes les lentilles. Même norme et mêmes valeurs absolues par coordonnée que v (il garde la forme
     que le repliement de la normalisation donne à `w`) ; direction brouillée.
   - Chaque direction nulle est lue par le même code et dans la même précision que v.
5. **Par direction (vecteur et signe), lentille et nul** :
   - z_t = (a_t(v) − m_t) / s_t, où a_t est le score du jeton t, m_t et s_t la moyenne et l'écart type de a_t sur les M directions
     nulles (moyenne sur des directions, jamais sur les jetons d'une action : aucune action n'est notée ici) ;
   - **les vingt premiers jetons** par score (k = 20) : identifiant, chaîne décodée (tokeniseur de G, échappée), score, z sous chaque
     nul, rang empirique du score parmi les M scores nuls du même jeton ; et les vingt premiers par z (nul isotrope) ;
   - **concentration** C(v) = max_t z_t ; p = (1 + #{j : C(u_j) ≥ C(v)}) / (M + 1), C(u_j) calculé avec les mêmes m_t et s_t (u_j
     compris : écart déclaré, négligeable à M = 2 000) ;
   - **part au-dessus du nul** P(v) : part des vingt premiers jetons dont le score dépasse le quantile 0,99 des M scores nuls du même
     jeton ; p de même forme ;
   - **familles de jetons nommées d'avance** (règles fixées ici, sur la chaîne décodée passée par `strip()`) : « nombres » : la chaîne
     s'écrit `^[0-9]+$` ; « coût » : la chaîne, en minuscules, est l'une de cost, costs, costly, price, prices, pricing, budget,
     budgets, expense, expenses, expensive, fee, fees, usd, dollar, dollars, $, spend, spent, spending, cheap, cheaper ; compte de
     chaque famille dans les vingt premiers jetons, et p de même forme.
6. **Pôles alignés** (côté sortie seulement ; pour v au signe + : le signe − rend les mêmes pôles, de signe opposé) : cosinus de v
   avec les 28 672 directions d'écriture des pôles du bloc ℓ (± colonnes de `mlp.down_proj`, coordonnées brutes) ; les **dix pôles**
   de plus grand cosinus : neurone, signe, cosinus, rang parmi les maxima nuls ; pour chacun, sa lecture par notre lentille côté sortie
   à la couche ℓ (dix premiers jetons, même fonction, comme la mesure de stabilité de G, M.2) ; concentration des pôles = cosinus
   maximal, et son p sous chaque nul.
7. **Comparaisons appariées, descriptives** : cosinus et nombre de jetons communs aux vingt premiers, entre la sonde apprise et le
   lecteur honnête de même cellule et même pli, entre les deux plis d'une cellule, entre les doses d'un même pli (cosinus seulement à
   même couche ; sinon « couches différentes : sans objet ») ; accord de notre lentille avec la lentille des logits et avec `npR`
   (jetons communs aux vingt premiers) ; **témoin de couche** : jetons communs entre la lecture de v à sa couche et à chacune des deux
   autres couches de T (même lentille).

## Seuil

- **Aucun seuil de décision, aucun taux d'erreur visé, aucun critère de succès** : le texte est descriptif. Les seules valeurs fixées
  d'avance sont des **règles de libellé** (« Critères de lecture gelés »), des **déclencheurs d'audit** (R4) et des **gardes** (« Liste
  d'arrêt »).
- **Niveaux des libellés** : « concentrée au-delà des deux nuls » si p ≤ 0,001 sous le nul isotrope **et** p ≤ 0,01 sous le nul des
  signes ; « non distincte du nul » si p > 0,05 sous l'un des deux ; « intermédiaire » sinon. Même règle pour la part au-dessus du nul
  et pour la concentration des pôles ; une famille est « sur-représentée » si p ≤ 0,01 sous les deux nuls. À côté de chaque compte de
  libellés est écrit le nombre attendu par le seul hasard sous le nul isotrope (nombre de lectures × 0,001).

## Plan d'analyse

1. **Ordre et antériorités** (registre propre ; « Lignes de registre ») : (a) `SCELLEMENT-LENTILLES-BBIS`, après contre-lecture et
   nœuds tranchés ; à l'inscription, la mère relève, par les clés seulement, que `VERDICT-BBIS` est absente du registre propre de
   l'apprentissage des sondes sur la tâche (ligne `ABSENCE-VERDICT-LENTILLES-BBIS`) ; présente : texte exposé, nœud ; (b)
   `CODE-LENTILLES-BBIS` (commit, empreintes, essais R5), avant toute exécution (nœud N3) ; (c) voie (b) seulement : devis propre, ligne
   `GO-LENTILLES-BBIS` (extrait du GO de Lazar), mot de Lazar sur la clé au moment de la commande (R-3151) ; rien ne part avant le
   prononcé du verdict de la tranche des lentilles par son lecteur, ni s'il est « chaîne en défaut » (nœud N7) ; (d) **E-1 et E-2
   ouverts par programme seulement après `VERDICT-BBIS`** (nœud N4), **récupérés seuls, par leur chemin** (clone partiel sans
   contenus, `--filter=blob:none`, puis extraction de ces deux chemins seulement ; aucun autre contenu de la branche des données n'est
   téléchargé, ni sur la machine ni dans un conteneur) ; ligne `ENTREES-LENTILLES-BBIS` (chemins, empreintes de E-1 et
   E-2, empreinte de l'extrait des champs de la liste blanche) ; (e) calcul (point 6), tables fermées, poussées, scellées :
   `TABLES-LENTILLES-BBIS` ; (f) lecture humaine (point 8) : `OUVERTURE-LENTILLES-BBIS`, puis `LECTURE-LENTILLES-BBIS`.
2. **Taille** : fixée par T, non choisie ici : vingt sondes (dix sondes apprises, dix lecteurs honnêtes), au plus quarante vecteurs ;
   89 498 jetons gardés ; 28 672 pôles par couche ; M = 2 000 directions par nul (résolution des p : 1/2 001, sous le plus petit niveau
   de libellé, 0,001).
3. **Graines (R9)** : entropie E = `207246359357165180107189867815730235805` (128 bits, `secrets.randbits(128)`, tirée le 2026-11-18 à
   16:49:33 UTC, avant toute lecture) ; graine de la clé k : `numpy.random.SeedSequence(entropy=E,
   spawn_key=(int.from_bytes(hashlib.sha256(k.encode()).digest()[:8], "big"),))`, générateur
   `numpy.random.Generator(numpy.random.PCG64(·))`, tirages en double précision ; clés : `lentilles-bbis/nul-isotrope/<couche>`,
   `lentilles-bbis/nul-signes/<cellule>/<pli>/<rôle>/<vecteur>`, `lentilles-bbis/temoins-calibration/<couche>/<nul>/<vecteur>`,
   `lentilles-bbis/colonnes-garde/<couche>`, `lentilles-bbis/essai/<garde>` ; un manifeste par course (configuration et empreinte,
   versions, graines, commit).
4. **Voie (b), recommandée** (nœud N1), sur une machine louée, dans cet ordre : montage de G (étape B0 : environnement épinglé de
   l'addendum v3, § 5 ; poids et tokeniseur à la révision épinglée ; Drowse 6.1.4 ; correctifs employés de G : (2) lentilles
   publiques, (4) comparaison des lentilles, (6) provenance « chat » du corpus d'activations ; essais du dépôt et du Llama miniature) ; corpus d'ajustement et ses contrôles (932 documents, moitiés 466 et 466, `rows_sha256` `a6afd972…`) ;
   **ajustement de notre lentille côté sortie** par les mêmes arguments que G (`02_fit.py --lens R --model
   meta-llama/Llama-3.1-8B-Instruct --docs 1000 --seq-len 128 --full-length --save-minutes 60`), et de la lentille côté entrée si N2
   la retient ; export `04_export_rlens.py <fichier d'ajustement R> --name dclm-llama` ; gardes de G : (d), (e) pour sa partie « matrice égale à l'identité »,
   (f), (g), (h), (n), (o), (q) ; corpus d'activations et `03_token_counts.py` une seule fois, liste des jetons gardés d'empreinte égale
   à `c37186ad…` (garde (r)) ; `npR` ; puis le calcul de ce texte ; versement ; destruction par identifiant (R10). Aucune mesure de G
   n'est refaite.
5. **Garde de la fonction de lecture** (R5) : à chaque couche lue, 64 colonnes de `W_down` tirées par graine ; les dix premiers jetons
   rendus par notre code égalent ceux de la fonction de lecture du voisin (cas sain) ; sur une lentille dont la matrice de la couche est
   perturbée (artefact), ils diffèrent pour au moins une colonne.
6. **Calcul** : lectures, nuls, statistiques, pôles, comparaisons (« Métrique ») ; **calibration** : 200 directions témoins tirées de
   chaque nul (graines propres) passent par le chemin des directions réelles, et leurs p de concentration sont calculés contre les M
   directions nulles ; **déclencheurs d'audit évalués et audits joués sur la machine**, avant la destruction (la lentille ne lui survit
   pas) ; tout est écrit dans des fichiers fermés.
7. **Comparaisons multiples** : aucune correction (descriptif) ; chaque compte de libellés porte son attendu par hasard ; nombre total
   de lectures écrit.
8. **Lecture** : par le lecteur neuf, sur processeur, après `VERDICT-BBIS` scellée et après le prononcé du verdict de la tranche des
   lentilles ; il applique les « Critères de lecture gelés » aux tables, écrit la description, la scelle (`LECTURE-LENTILLES-BBIS`) ;
   un désaccord entre ses phrases et celles que le code rend mécaniquement est tranché par un second lecteur neuf, sans nouveau calcul.
9. **Contrôles appariés** : mêmes directions nulles pour toutes les lentilles d'une couche ; même nul des signes pour v et −v ; sonde
   apprise et lecteur honnête comparés à même cellule, même pli, même couche.

## Critères de lecture gelés

**Phrase de tête, toujours écrite** : « Lecture descriptive, par nos lentilles, des directions des sondes apprises sur la tâche et des
lecteurs honnêtes de même recette, à la couche où chaque sonde lit. Elle dit quels jetons et quels pôles la lentille associe à chaque
direction ; elle ne dit rien de la détection du sabotage, qui appartient au verdict de l'apprentissage des sondes sur la tâche, ni de
ce qu'une sonde fait sur un épisode. » Suivie de : « Lentille : [verdict d'ensemble de la tranche des lentilles] ; lentille ré-ajustée
par la même recette, empreinte [égale / différente] de celle de la tranche. »

| ce qui est observé (par direction, signe et lentille) | phrase gelée |
|---|---|
| concentrée au-delà des deux nuls | « Par [lentille], la direction de [sonde, en clair] (couche [ℓ], signe [±]) se distingue des deux nuls (concentration [C] ; p [p_iso] et [p_signes]) ; ses premiers jetons : [vingt jetons]. » |
| intermédiaire | « Par [lentille], la direction de [sonde] (couche [ℓ], signe [±]) ne se distingue des nuls qu'en partie (p [p_iso] et [p_signes]) : ses premiers jetons sont rapportés, sans être nommés comme ce qu'elle capte. » |
| non distincte du nul | « Par [lentille], la direction de [sonde] (couche [ℓ], signe [±]) ne se distingue pas du nul (p [p_iso] et [p_signes]) : ses jetons sont en table, et aucune phrase ne les nomme comme ce qu'elle capte. » |
| famille sur-représentée | « La famille [nombres / coût] paraît [n] fois dans ses vingt premiers jetons (attendu sous le nul [e] ; p [..] et [..]) : la lecture ajoute un soupçon que la sonde lise [des nombres / le coût] ; elle ne le prouve pas. » |
| famille non sur-représentée | « La famille [..] n'y est pas sur-représentée ([n] ; p [..] et [..]) : cela ne blanchit pas la sonde. » |
| pôles alignés concentrés | « Les pôles qui écrivent le plus près de la direction ([dix pôles], cosinus [..]) se distinguent des nuls (p [..] et [..]) ; notre lentille les lit : [jetons par pôle]. » |
| pôles non distincts | « Aucun pôle de la couche n'écrit plus près de la direction que sous le nul (p [..] et [..]). » |
| comparaison appariée | « Cosinus [c] entre [sonde] et [autre] (même couche) ; [j] jetons communs sur vingt. » ; ou « couches différentes : sans objet ». |
| non calculable ou non lue | « Non lue : [motif]. » |

**Règles** : aucune phrase ne nomme les jetons d'une lecture « non distincte du nul » ou « intermédiaire » comme ce que la direction
capte ; aucune phrase ne dit qu'une sonde détecte ou ne détecte pas le sabotage, lit ou ne lit pas « l'état saboteur », ni ne rapproche
la lecture d'une aire ; le mot « soupçon » ne s'emploie que pour une famille sur-représentée ; toute description au-delà des phrases
gelées est marquée « description libre, après lecture, non préenregistrée ».

**Audit de symétrie (R4)**, déclencheurs gelés, évalués et joués sur la machine : (i) **trop beau** : les dix sondes apprises et les dix
lecteurs honnêtes « concentrés » par notre lentille côté sortie ; ou, pour une direction des couches 7 ou 15, les mêmes vingt premiers
jetons par notre lentille et par la lentille des logits ; ou deux directions distinctes (deux plis, deux doses) de cosinus > 0,999 ; ou
une sonde apprise et son lecteur honnête de cosinus > 0,99 ; (ii) **tout négatif** : aucune lecture d'aucune direction « concentrée »
ni « intermédiaire », par notre lentille **et** par la lentille des logits. Contenu de l'audit : empreintes des tableaux lus contre E-2 ;
couche de la sonde, de la lentille et du harnais ; conventions de signe ; décodage ; deux directions relues par un chemin indépendant
(produits en double précision, sans la fonction du voisin). Issue écrite en réserve ; aucune table ne change.

## Liste d'arrêt

| condition | action |
|---|---|
| texte non scellé, `SCELLEMENT-LENTILLES-BBIS` absente, ou `VERDICT-BBIS` déjà présente à son inscription | rien ne part ; texte exposé : nœud (version neuve qui déclare l'exposition, ou abandon) |
| code non cité par `CODE-LENTILLES-BBIS`, un essai (R5) manquant ou en échec | rien ne part |
| voie (b) : pas de GO de Lazar sur devis, pas de feu écrit de la mère, clé passée sans le mot de Lazar (R-3151), verdict de la tranche des lentilles non prononcé ou « chaîne en défaut » | rien ne part |
| dépense : cumul relevé plus un quart d'heure de carte au plafond du GO ; durée au-delà du pire cas du devis ; processus mort sans résumé | arrêt, versement de ce qui existe, destruction par identifiant (R10) ; une relance au plus sous le même GO |
| `SCORES-BBIS` absente, ou en plusieurs lignes | rien ne part ; plusieurs lignes : nœud (la mère désigne la course, par les noms seulement) |
| E-1 ouvert avant `VERDICT-BBIS` (sauf nœud N4 tranché autrement) ; un fichier de la liste « jamais ouverts » ouvert, ou un contenu de la branche des données autre que E-1 et E-2 téléchargé ; un champ de E-2 hors de la liste blanche lu ou écrit | lecture invalide ; nœud |
| empreinte de E-1 ou de E-2 différente de son compagnon ou de la ligne de registre | arrêt (R11) |
| empreinte d'une sonde recalculée (convention du code qui écrit E-1) différente de celle de E-2 ; couche hors de {7, 15, 23} ; famille hors de {linéaire, attention} ; cellule ou pli manquant | arrêt : forme mal comprise ; nœud |
| sonde en échec à l'apprentissage (paramètres non finis, T) | cette sonde « non lue », sans arrêt |
| une garde de G sur la lentille ré-ajustée ((d), (e), (f), (g), (h), (n), (o), (q), (r)) ; liste des jetons gardés d'une autre empreinte que `c37186ad…` | arrêt avant tout calcul ; versement ; destruction ; nœud |
| garde de la fonction de lecture (plan, point 5) : écart sur le cas sain, ou égalité sur l'artefact | arrêt avant tout calcul |
| calibration (plan, point 6) : moins d'une ou plus de 24 directions témoins sur 200 à p ≤ 0,05, pour une couche, une lentille et un nul | tables de cette couche, de cette lentille et de ce nul « non calculables », motif écrit, sans arrêt du reste |
| valeur non finie dans une lecture ou un nul | arrêt |
| tables ouvertes par une personne avant `VERDICT-BBIS` scellée et le prononcé du verdict de la tranche des lentilles ; une table ou une phrase de ce texte transmise au lecteur du verdict de l'apprentissage des sondes sur la tâche, de l'étape B, de la table conjointe ou de P3-bis avant leurs verdicts scellés | lecture invalide ; nœud |
| clé de ce texte écrite dans `registres/scellements-v1.md` (la garde de T0.7 y refuse toute clé inconnue ; T, « Liste d'arrêt ») | arrêt de l'écriture ; ligne retirée par la mère, déclaré |
| lentille absente ou détruite avant le calcul | « non lue : lentille absente » ; **jamais** remplacée par la lentille publique sous le nom « nos lentilles » (aucun repli silencieux, R5) |
| toute envie d'écart à ce texte | écrite, datée, version neuve (R12), contre-lue, avant d'être faite |
| tout refus d'une permission, du crochet ou du classifieur | ni rejoué, ni reformulé, ni contourné ; arrêt ; nœud |

**R5** : chaque garde codée est essayée avant la course sur un cas sain et sur un artefact (« Code neuf ») ; résultats consignés.

## Qui, quelle machine, quel coût

- **Développeur neuf** : écrit le code (« Code neuf ») sans aucune vue des données (jouets et Llama miniature seulement) ; ni auteur
  de ce texte, ni opérateur, ni lecteur.
- **Opérateur neuf** : n'a lu aucune sortie ni aucun score de l'apprentissage des sondes sur la tâche, ni des autres chaînes
  interdites ; ni auteur, ni développeur, ni lecteur de ce texte, ni lecteur ou juge d'aucun verdict nommé ici ; lance la course, ne lit
  que les codes d'arrêt, les existences et les empreintes, n'ouvre aucune table.
- **Lecteur neuf** : n'a lu aucun résultat de l'apprentissage des sondes sur la tâche (score, aire, issue, verdict), ni des autres
  chaînes interdites ; ni auteur, développeur ou opérateur, ni lecteur d'aucun verdict nommé ici ; lit ce texte, les tables fermées et
  la ligne du verdict de la tranche des lentilles ; décrit selon les « Critères de lecture gelés ».
- **Machine** (nœud N1) : **le processeur seul ne peut pas lire nos lentilles** : elles n'existent que sur une machine qui les ajuste
  (lieu L1). Voie (b), recommandée : une H100 SXM 80 Go, filtre d'offre de la commande v6 (prix stockage de 200 Go compris au plus
  2,62 USD/h, trafic au plus 0,04 USD/Go, débit montant d'au moins 200 Mbit/s, machine vérifiée), image `python:3.12.16-bookworm`, disque
  de 200 Go, mémoire d'au moins 64 Go. La lecture humaine se fait sur processeur.
- **Coût** (estimation de l'auteur, tirée des durées du devis v12, § 4 : banc de 11,2 à 11,8 s par document, × 0,9 à 1,2 pour Llama,
  pire cas 23,6 s ; 932 documents ; montage de 0,5 à 1 h, pire 3 h ; à refaire par un devis propre avant tout GO) : voie (b), lentille
  côté sortie seule : ≈ 3,6 à 5,8 h, **≈ 10 à 16 USD** trafic compris ; pire cas ≈ 11,3 h, **≈ 31 USD** ; avec la lentille côté entrée
  en plus : ≈ 6,3 à 9,6 h, ≈ 17 à 26 USD ; pire cas ≈ 17,6 h, ≈ 47 USD. Le calcul propre à ce texte : moins d'une demi-heure de carte.
  Lecture : 0 USD.

## Frontière : ce que ce texte ne dit pas

1. Rien sur la détection du sabotage : aucune phrase ; elle reste au verdict de l'apprentissage des sondes sur la tâche (T).
2. Rien sur les sondes génériques, le critère 3 de G0, G1, ni aucune hypothèse du programme ; aucun résultat n'entre dans un
   préenregistrement du programme sans nœud de Lazar.
3. Une liste de jetons dit ce que la lentille associe à une direction (ce qu'elle « pousse en moyenne »), non ce que la sonde emploie
   sur un épisode, ni un rôle causal ; aux couches 7 et 15, sous les deux tiers de la profondeur, G attend lui-même que la lecture
   prédise mal ce qu'une activation fait en contexte (lecture contre ablation couche par couche, B-7).
4. Une lecture peut ajouter un soupçon sur une sonde, jamais la blanchir (règle de G).
5. Voie (b) : la lentille lue est ré-ajustée par la même recette ; elle n'est pas, au bit près, celle que juge le verdict de la
   tranche ; l'écart n'est pas mesuré.
6. La comparaison au lecteur honnête décrit un recouvrement avec un lecteur du texte de même recette ; elle ne dit pas « au-delà du
   texte » (seules les épreuves de T en jugent).
7. Les réglages retenus (famille, couche) lus ici ne sont pas des scores ; ils montrent ce que la validation interne a choisi ; c'est,
   avec les directions, la seule information de l'apprentissage des sondes sur la tâche qui passe dans cette lecture.
8. Rien sur les sondes de l'ordre 2, les sondes du nul de réétiquetage, les directions du plancher : non lues.
9. Rien d'un autre modèle, d'un autre mode de sabotage, ni d'une autre couche que 7, 15 et 23.

## Données gardées et plan de stockage

- Course (voie (b)), branche `calcul/lentilles-sondes-bbis-v1`, morceaux de moins de 95 Mo, compagnons `.sha256` :
  `diag/<run-lentilles>/tables-lentilles-bbis.json` (toutes les tables, déclencheurs et audits ; **fermé**) ;
  `donnees/<run-lentilles>/lectures-lentilles-bbis-NNN.npz` (scores de tous les jetons gardés par vecteur et lentille ; résumés des nuls
  par jeton : moyenne, écart type, quantile 0,99 ; statistiques des directions nulles et des directions témoins ; **fermés**) ;
  `diag/<run-lentilles>/montage-lentilles-bbis.json` (gardes de l'ajustement, empreintes des fichiers d'ajustement et d'export, liste
  des jetons gardés : nombre et empreinte, versions ; aucune lecture de sonde) ; `runs/<run-lentilles>/manifeste.json` (R9).
- Non gardées : la lentille ré-ajustée et les activations (lieu L1 par défaut ; tout rangement est un nœud de Lazar).
- Lecture : `diag/<run-lecture>/lecture-lentilles-bbis.json` (phrases rendues par le code) et la description du lecteur,
  `docs/notes/lecture-sondes-bbis-par-lentilles-v1/description-v1.md`, chacune scellée avec son compagnon.

## Lignes de registre

Registre **propre** : `registres/lecture-sondes-bbis-par-lentilles-v1.md`, format `| clé | AAAA-MM-JJTHH:MM:SSZ | chemin | sha256 |`,
lignes ajoutées, jamais réécrites. Clés : `SCELLEMENT-LENTILLES-BBIS` (version scellée de ce texte), `ABSENCE-VERDICT-LENTILLES-BBIS`,
`CODE-LENTILLES-BBIS`, `GO-LENTILLES-BBIS` (voie (b)), `ENTREES-LENTILLES-BBIS`, `TABLES-LENTILLES-BBIS`, `OUVERTURE-LENTILLES-BBIS`,
`LECTURE-LENTILLES-BBIS`. Lues, jamais écrites : `SCORES-BBIS` et `VERDICT-BBIS` (registre propre de l'apprentissage des sondes sur
la tâche ; clés, heures et chemins seulement). **Jamais** `registres/scellements-v1.md` (nœud N6).

## Code neuf (à écrire sans aucune vue des données, contre-lire, éprouver ; R5)

- `src/controle_ia/lentilles_sondes_bbis/` (noms neufs, R12) : `entrees_v1` (E-1, E-2, liste blanche, empreintes, refus de tout autre
  chemin, refus avant `VERDICT-BBIS`) ; `lecture_v1` (lectures côté sortie et côté entrée, références, scores complets, garde de la
  fonction de lecture) ; `nuls_v1` (deux nuls, directions témoins, graines) ; `statistiques_v1` (z, concentration, part, familles,
  pôles, comparaisons) ; `audits_v1` (déclencheurs R4, calibration) ; `phrases_v1` (phrases gelées) ; lanceur et amorce repris de la
  tranche des lentilles sous des noms neufs, avec les seules étapes du plan, point 4.
- **Essais** (cas sain et artefact pour chaque garde) : liste blanche (ouvrir un fichier de scores : refus) ; ouverture avant
  `VERDICT-BBIS` (refus) ; empreinte d'une sonde (un poids altéré : arrêt) ; couche ou famille hors de l'ensemble ; fonction de lecture
  (colonnes de `W_down` ; lentille perturbée) ; nuls (graines reproductibles ; même norme ; nul des signes de mêmes valeurs absolues) ;
  calibration (nul sain : dans les bornes ; chemin des directions réelles faussé, par exemple autre précision : hors des bornes) ;
  familles (vocabulaire jouet) ; symétrie des pôles (v et −v) ; valeurs non finies ; clé dans `registres/scellements-v1.md` (refus) ;
  une phrase par libellé ; bout en bout sur un Llama miniature.

## Nœuds ouverts (à trancher avant le scellement de la version)

- **N1 — où nos lentilles rencontrent les directions.** Enjeu : sous L1, nos lentilles ne survivent pas à la course des lentilles, et
  cette course n'a pas le droit de lire nos sondes. (a) **étape ajoutée à la course des lentilles** : exclue en l'état (G l'interdit ;
  il faudrait une version neuve de G, contre-lue, et retenir la course avant son départ) ; (b) **machine courte neuve** qui ré-ajuste
  notre lentille par la même recette, lit les directions, verse les tables fermées et se détruit : indépendante de la course des
  lentilles, ≈ 10 à 16 USD (pire ≈ 31) ; lentille non identique au bit ; (c) **rangement restreint** des matrices de nos lentilles
  aux couches 7, 15 et 23 par la course des lentilles (≈ 6 × 67 Mo), lecture plus tard ailleurs : ≈ 1 à 3 USD, mais version neuve de
  G, mot de Lazar sur le lieu L1, course retenue avant son départ, et une machine portant les poids de Llama pour la lecture ; (d)
  **processeur seul, lentille publique** (`npR` et lentille des logits) : aucune location, mais ce ne sont pas nos lentilles (titre à
  changer) ; il faut ≈ 15 à 20 Go de disque (fichiers entiers des poids qui portent la sortie et les couches lues, `npR`, corpus des
  jetons gardés) et la clé dans le conteneur. **Recommandation : (b)**, confiance 0,6 ; (c) seulement si
  la course des lentilles n'est pas partie et que Lazar veut le coût le plus bas.
- **N2 — lentilles à ré-ajuster (voie (b))** : côté sortie seule (recommandé, confiance 0,55 : G attend une lecture côté entrée peu
  lisible au milieu du réseau, B-5 ; moitié du coût) ou les deux.
- **N3 — code cité après le scellement** : écart au gabarit, à accorder par Lazar (ou par la mère, si son autonomie GO-2026-11-18-26 le
  couvre) ; recommandé (confiance 0,7) : le texte doit être scellé avant toute lecture humaine d'une sortie de l'apprentissage des
  sondes sur la tâche, et le code ne peut rien choisir d'après elles.
- **N4 — moment d'ouverture des poids par programme** : après `VERDICT-BBIS` (recommandé, confiance 0,6 : aucun fichier fermé de cette
  étape n'est ouvert avant son verdict) ou dès `SCORES-BBIS` (plus de marge pour le billet ; tables fermées jusqu'au verdict).
- **N5 — passerelle avec une tranche hors programme** : G se dit hors programme (« aucun résultat n'entre […] dans un préenregistrement
  du programme sans nœud de Lazar », GO-2026-11-17-03) ; ce texte emploie sa recette sur des sondes du programme ; la question de
  Lazar le couvre peut-être ; recommandé : une ligne à Lazar (confiance 0,6).
- **N6 — registre** : registre propre (recommandé, confiance 0,8), plutôt que `registres/scellements-v1.md`, que le mandat semble
  nommer (« registre des scellements ») et où la garde de T0.7 refuse les clés inconnues (T, « Liste d'arrêt »).
- **N7 — dépense et préalables de la voie (b)** : devis propre, GO de Lazar, mot sur la clé (R-3151) ; attendre le prononcé du verdict
  de la tranche des lentilles avant de louer (recommandé : une recette en « chaîne en défaut » ne se rejoue pas).

## Contre-lecture

- **Contre-lecture 1, à faire** : un sous-agent neuf d'un **autre modèle** que l'auteur (mandat), qui n'a écrit ni ce texte, ni aucune
  pièce de l'apprentissage des sondes sur la tâche ou de la tranche des lentilles, et ne sera ni développeur, ni opérateur, ni lecteur
  de ce texte, ni lecteur d'aucun verdict nommé ici. Brouillon relu : ce brouillon 1 (empreinte dans son compagnon `.sha256`) ;
  rapport : à venir, versé avec son empreinte.
- **Fichiers à lui donner** (lecture seule) : ce brouillon ; le mandat ; T (« Hypothèse », « Métrique », « Plan d'analyse » points 1,
  5, 9, 12, « Liste d'arrêt », « Données gardées », « Lignes de registre », « Code neuf ») ; A2 (§ 0, SA-10, SA-16 à SA-18) ; A3
  (en-tête, § 0, TA-1) ; sur la branche `claude/brave-galileo-jhp684`, par `git show` : G (en-tête, « Hypothèse », « Métrique », P.3,
  P.6, P.7, « Critères de lecture gelés », « Liste d'arrêt »), l'addendum v3 (§ 2, § 3, § 5), la commande v6 (« Demande de feu »,
  étape 12), le devis v12 (§ 2, point 6 ; § 4) ; `src/controle_ia/sondes/familles.py` ; `src/controle_ia/harnais/activations.py`
  (l. 1-80) ; `src/controle_ia/prereg.py` ; le gabarit ; `CLAUDE.md`.
- **Interdits du contre-lecteur** : ceux de l'auteur (rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucune branche
  `calcul/` ou `donnees/` ; aucune sortie ni aucun résultat des chaînes nommées ; aucune recherche récursive large).
- **État au validateur** (`prereg.problemes`) : un seul manque attendu pour un brouillon non contre-lu, la section « Contre-lecture »
  sans ses deux empreintes (brouillon relu et rapport).
