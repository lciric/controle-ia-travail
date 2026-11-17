# Rapport du développeur — code de lancement du crible (v), v1

- **Auteur** : développeur neuf (modèle A) ; n'a écrit ni le texte du crible, ni ses brouillons, ni aucune contre-lecture, ni le
  pilote, ni son code, ni sa procédure ; aucun identifiant de modèle dans les fichiers.
- **Date** : 2026-11-16T23:35Z à 2026-11-17T01:37Z (`date -u`).
- **Texte suivi** : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-v-version-foi-v2.md`
  (`2b99627dd378564dba816bc10593cdb0d06d77a3fdd4eb9e3cca022c76838715`, lu entier), **jugé scellable** au tour différentiel 2
  (`contre-lecture-crible-v-foi-tour2-v1.md`, aucune correction exigée ; deux remarques facultatives F-3 et F-1, rien de bloquant) ;
  prédictions V1 à V7 **non changées** (R-2993) ; aucune valeur refaite par ce code (devis, durées, III-7 : sans objet ici).
- **Lus, non modifiés** : lanceur v74 du pilote (`demonstrations/pilote_mr2_v74.py`) et ses modules (`pole/pilote_mr2_v70.py`,
  `proposeurs_pilote_v70.py`, `proposeurs_pilote_v72.py`, `sonde_pilote_v74.py`, `audit_pilote_v70.py`), configuration v12
  (`f69503dd…`), commande et relais v70 (arbre de l'organisme, paquet `e3d83e47…`, tête 605e0f6, branche `lot/compte-organisme-v1`) ;
  mesure du pilote `mesure_pilote_v4.py` (`676d5f37…`) et outils MR-2 (`monde_riche_v4.py` `4b165847…`, `complements_synthese_v1.py`
  `89eb7ba8…`, `monde_riche_outils_v1.py` `1825b956…`) ; procédure v14 du pilote (`20355627…`) et son programme machine sans ssh
  (v2) ; procédure v6 de la machine du jeu de l'idée 1.1 (lanceur v2, amorce v2, garde v1). **Non ouverts** : l'issue du pilote
  MR-2 v14 (seule la section « Pour les cribles » transmise par la consigne a été lue), toute branche `calcul/pilote-mr2-v74-entree-*`,
  la branche de sortie du pilote, la pièce de dépense du pilote, le relevé de v67 ; rien sous `diag/`, `runs/`, `donnees/` ; rien de
  7a, 7b, T0.6, T0.7, P3-bis, du bras d'attaque.
- **Aucune machine, aucun appel au loueur ni à aucun fournisseur, aucune clé employée, aucune dépense** ; tous les appels des essais
  passent par les relais **factices** de la configuration v12 (amont en mémoire) ; aucun fichier existant modifié ; aucun commit.

## 0. Verdict (trois lignes)

1. Le code neuf du crible (v) est écrit, joué hors ligne et scellé : lanceur à **files parallèles** (M = 1 ou 2, 4 M relais),
   **borne B_a = 900 s par appel** (coupure comptée « échec », journalisée, jamais reprise), **garde de départ**, mesure, lecture
   gelée, partie A, procédure de la machine (amorce, programme machine, outil de la session), essai à blanc complet, banc de mutations,
   répétition locale de la machine : **40 essais unitaires, 9 essais à blanc et de scénarios, 5 essais de la mesure, 52 mutations tuées sur 52 (3 témoins conformes), 37 cas de répétition de la machine : **aucun échec, aucun écart****.
2. Le crible **peut partir avant le 21 novembre** : rien dans le code n'attend cette date ; ce qui reste avant le feu est au § 5
   (contre-lecture du code par un autre modèle, D relevée, fiche, lignes κv1 et κv2, mots de Lazar).
3. Aucun résultat n'est lu ni prédit ici ; rien n'est adopté.

## 1. Pièces (dossier `docs/procedures/crible-v-v1/`, chacune scellée avec son compagnon `.sha256`)

| pièce | rôle | empreinte |
|---|---|---|
| `crible_v_commun_v1.py` | nombres gelés du texte (N, B_a, ε, ε_strat, 0,8, seuils, W_min, règle de M, garde de départ, lignes κ), graine des mondes, écriture scellée | `785b2091be687cb3d1af8ffc8ea7d91f865ec8a9a34f4b8d5b40dfecf6fe8980` |
| `lanceur_crible_v_v1.py` | lanceur : secret, generer, preparer, sonde, jouer (files, B_a, abandon, garde de départ), mesurer, lire, rapatrier | `2636bcb1deefc0a7dc1427bb476b7c0e2efdc1b5ae6d9e76c3a7c2ac592d7725` |
| `mesure_crible_v_v1.py` | mesure (nom réservé), une seule fois ; principale puis rejeu sous archive fictive ; chrono du placebo | `470e1279122f91ca6bd7ecf783472ad31248bb3a92af8d903a7631de5a9ab012` |
| `lire_crible_v_v1.py` | lecture gelée (nom réservé) : étages 0 à 6, H-v, V1 à V7, marques de l'audit R4 | `4380be0e7e02e6bf893e5699333db90c932cc4786861f10ee82ccd4a6b328dd0` |
| `partie_a_crible_v_v1.py` | partie A (traces de v67), chargeur gardé | `e62f2ba373617b33970900d0ed910a184a71e44d81c5ce8c4421017d0d1c62c0` |
| `amorce_crible_v_v1.sh` | amorce de la machine (minuterie, clone partiel, programme machine à son empreinte) | `61abbccfcf2be6641408c073701a58b59d2121ca0060e58393df1746edea50d2` |
| `machine_crible_v_v1.py` | programme machine (états, barrières, balayage, poussées, essai à blanc, sonde, crible, mesure, rapatriement) | `a48da4b91fa0a42436348cf472f70834a7ab4dfe03bac051f7d30091c91e34b4` |
| `session_crible_v_v1.py` | outil de la session (offre, création, commande, ligne, prix, dépense, destruction, absence, feux) | `196ee5c060a8ee039e891d5f990fd16a558bba1f2a6b29333f2d0cc9c9f73366` |
| `essais_crible_v_v1.py` | essais R5 (paliers unitaire, jouer, mesure) | `2ef389f88c1cc88932c66635d273e12ff36d5ad620f4a5d08148896331a702d2` |
| `banc_mutations_crible_v_v1.py` | banc de mutations (52 mutations, 3 témoins) | `32e07f880cc7b471db85dabeb32f8fa7cb503544d326bd8c87e13528a3c0fd4f` |
| `repetition_crible_v_v1.py` | répétition locale de la machine (dépôt jouet, loueur simulé) | `6a765f88f7e58d96dae4d2aaf372227006731efd4c5971f7252122fa6e7262f8` |
| `procedure-machine-crible-v-v1.md` | procédure de la machine (gestes, feux, destruction, preuve d'absence) | `03da4c3ac52183ca899d202724c83e4db610aa17b38a763ffdd7baa41ceedccf` |
| `devis-machine-crible-v-v1.md` | devis de la machine | `b542dd18ff7d4afccfa638580e621f3f4dfc66dd8de91297ea6931f28fee7632` |
| `gabarits-crible-v-v1.md` | gabarits : addendum, fiche de lancement, inscriptions, ligne de feu | `efd4574ae4cb60d8ba3e4dcbe2c1488836ec31da6e1bdaa365c6d23409d760df` |
| `sortie-essais-unitaires-crible-v-v1.json` | sortie gardée : 40 essais unitaires, 0 échec | `a88107c259615dda3abe0f5d10945612f163268a076610171d01ea6bd35586c4` |
| `sortie-essais-jouer-crible-v-v1.json` | sortie gardée : essai à blanc complet et scénarios, 9 essais, 0 échec | `1a8e2f52579f7b0ccfb8430f42213e20e2a4fac7f019543eb7f7cb5f805806cf` |
| `sortie-essais-mesure-crible-v-v1.json` | sortie gardée : mesure une fois, seconde mesure, recalcul, exception, 5 essais, 0 échec | `3130b9f00963edc7010d5a7b9d38cc56d762a0c15dc7a8fe390f6d47eb768820` |
| `sortie-banc-mutations-crible-v-v1.json` | sortie gardée : 52 mutations tuées sur 52, 3 témoins conformes | `d936cd0ddadaa5cf7b30da513b80dd9de46266973a8876c4efa367bea8eb881e` |
| `sortie-repetition-crible-v-v1.json` | sortie gardée : répétition de la machine, 37 cas, 0 écart | `c565edb12b5e09339ebd813bc472ae9fa7a901f83dd3c1ba6f8dd8a61b40acfa` |
| `sortie-chrono-placebo-crible-v-v1.json` | sortie gardée : énumération exacte du placebo, pire cas, 0,364 s | `72e70d3f9980d43557d087eec962e20d9bfda8989ed754c2d8b3ac704363c9c7` |
| `essai-a-blanc-m1-v1/CARTES.json` | essai à blanc complet M = 1 (mondes d'essai), pièce gardée | `5dbe2f6dc013390e509c24dce914e9f33c4ad990f856719d7213841874f8a58a` |
| `essai-a-blanc-m1-v1/DOLLARS.json` | essai à blanc complet M = 1 (mondes d'essai), pièce gardée | `5bf1a69e5a45a74995f978a254f53c88fefbc5bfc804d437f0d59095c5e70bae` |
| `essai-a-blanc-m1-v1/coupures-crible-v-v1.jsonl` | essai à blanc complet M = 1 (mondes d'essai), pièce gardée | `a83f0e65fbb48af8e276b3e256edf0d6e0a158bd86ff9dec6fa61111583d9ef4` |
| `essai-a-blanc-m1-v1/lecture-crible-v-v1.json` | essai à blanc complet M = 1 (mondes d'essai), pièce gardée | `a330ce72f456a6632734cd0271b543b3a01f0dc47ddd8f251d9da55bcf53a8ee` |
| `essai-a-blanc-m1-v1/mesure-crible-v-v1.json` | essai à blanc complet M = 1 (mondes d'essai), pièce gardée | `5b24ad2c33c59bb7649484970b0fc9607115f51a25d62edfe12298ba16209179` |
| `essai-a-blanc-m1-v1/sortie-fictive-crible-v-v1.json` | essai à blanc complet M = 1 (mondes d'essai), pièce gardée | `ccad939d1c40aa4111f5fafe4dd090009a9e44234fc3d894e749b09a745344f3` |
| `essai-a-blanc-m1-v1/sortie-mesure-crible-v-v1.json` | essai à blanc complet M = 1 (mondes d'essai), pièce gardée | `3237892a0719570dcd0f94d24f279013391ef1c573632f847e67ecc5c9ed08ee` |

Le manifeste et le relevé de l'essai à blanc ne sont pas gardés ici : ils portent, par construction des relais du pilote (état du relais, modèle servi), des identifiants de modèle ; ils restent dans le dossier de travail de la session. L'amorce porte l'empreinte du programme machine (`SHA_MACHINE`) ; la répétition l'a éprouvée.

## 2. Ce que fait le code (au regard du texte)

- **Mondes** (`lanceur generer`) : 20 mondes MR-2 du secret du crible, graine `graine_monde_crible` (fonction du pilote, étiquette
  « crible-v-v1 », r de 1 à 20, sur un octet), 8 tirages de `generer_v4` au plus ; **étiquettes C8 « certifiée » rendues par
  `verifier_v4` à la génération** gardées dans `CERTIFIEES.json` (privé, latente exclue), liées au fichier des mondes par un
  engagement ; un monde sans tirage conforme : refus, arrêt avant tout appel.
- **Préparation** (`preparer`) : oracle de 12 000 instances à `cle("oracle-crible-v", empreinte du devis)`, K1 du monde, C-16 et
  C-17 du pilote, épisodes de développement (règle du bloc gelé, étiquette « crible-v-v1|episodes-developpement »), textes servis
  ≤ 52 000 octets (≈ 48 600 aux mondes d'essai), **gabarit servi du pilote à `e77d3041…`** (refus sinon).
- **Appels** (`jouer`) : M files (mondes k + 1, k + 1 + M, …) ; dans une file, les mondes l'un après l'autre ; **les quatre appels
  d'un monde partent ensemble** ; corps servi relu et **égal pour les quatre** (arrêt avant les appels du monde sinon), texte reçu
  égal au corps préparé (arrêt sinon) ; commande gelée de la v12 sur les relais de la file (ports + 10 k, plafond = mondes de la file
  × plafond de session, appels = mondes de la file) ; réponse brute et témoin d'isolement scellés avant l'extraction ; **coupure à
  B_a** : commande tuée, « échec », cause `au_dela_de_B_a`, ligne relue dans `coupures-crible-v-v1.jsonl`, plafond de session dans
  les dollars si le journal du relais n'a pas de ligne ; **panne de relais** : la voie à clé commune (claude : Pr-2 et Pr-4 ; gemini :
  Pr-1 ; astra : Pr-3) abandonnée, ses appels restants « échec » sans être lancés ; **arrêt du crible** si elle n'a encore aucun
  appel répondu ou si le minimum de 16 mondes complets n'est plus possible ; coût au-dessus du pire cas, part d'un fournisseur
  atteinte, pièces absentes : arrêt (code 3) ; garde de la réflexion absente du lanceur v74 reprise telle quelle.
- **Mode réel** : configuration à `f69503dd…`, numpy 2.5.3, texte à son empreinte, **addendum d'empreintes** portant le code présent,
  M de la règle pour D, **garde de départ** (6 000 + 3 D + ⌈20/M⌉ × 900 s avant l'échéance), **relevé de la sonde neuve** (module de
  la sonde v74, sous le code du crible et le chemin de ses relais), κv1 et κv2 au montant exact, engagements, registre des lancements
  (un seul lancement par texte) ; options de l'essai à blanc et crochets refusés.
- **Mesure** (`mesure_crible_v_v1.py`, une seule fois) : dans l'ordre du texte, (1) copies et a_w par `decider`, qui ne reçoit que
  les lois des cartes valides de la moitié bon marché (objets `LoiBonMarche`), K1 servie (softmax) et le jeu public
  (`JeuPublic` : traits et sous-populations de `SeedSequence(entropy=racine, spawn_key=(r, 30))`, immuable, sans issue) — copie :
  forme canonique de K1, ou d_nul < 0,01 et d_strat < 0,04 au **sens dirigé** (carte → K1), q > 0,8 strictement ; (2) couvertures
  des composantes certifiées hors effet de K1 et hors ce que K1 servie porte, τ = max(0,005 ; 0,75·I) ; (3) dollars des quatre
  appels de chaque monde (journaux des relais), aux prix publics (Pr-1 au cinquième du prix de la configuration) et au compte de la
  configuration ; (4) bras T, R, B, E, Clopper-Pearson, rééchantillonnage `(99, b)` (10 000), **placebo par énumération exacte**
  (compte égal à C(n_c, k_R), refus sinon), sensibilités de la « Métrique » ; sortie principale écrite et scellée ; (5) **rejeu
  sous archive fictive** par sa fonction distincte (refus si la sortie principale n'est pas scellée ; ne rend que k_R et S_R), second
  fichier scellé.
- **Lecture gelée** (`lire_crible_v_v1.py`) : étages 0 à 6 dans l'ordre, table W_min recalculée et égale à la table gelée, lecture
  de H-v (« non éprouvée au crible » si k_R < 4 ou > n_c − 4), états de V1 à V7 (V4 sans verdict), marques de l'audit R4 ; rien
  n'est adopté.
- **Partie A** (`partie_a_crible_v_v1.py`) : chargeur gardé (tout champ du juge lu : refus nommé), archive de la génération 2 = {K1}
  et toutes les cartes de la génération 1, dimensions de S-V1 **lues** dans le texte de la boucle réelle (3 issues, 2 traits,
  2 sous-populations), graine `(67, g, 30)`.
- **Machine** : `amorce_crible_v_v1.sh` (arguments, minuterie de destruction armée avant toute passe, clone partiel limité au code du
  crible et à `prereg/`, programme machine à son empreinte) ; `machine_crible_v_v1.py` (états horodatés, barrières 1 à 3, balayage,
  poussée vérifiée et reprise, essai à blanc à M, sonde neuve, crible réel, feu d'arrêt par PID, mesure une fois, lecture remise non
  ouverte, rapatriement sans monde) ; `session_crible_v_v1.py` (offre, création, commande, contrôle de la ligne, inventaire, prix
  relu, dépense, destruction par l'identifiant lu, preuve d'absence, feux). Procédure : `procedure-machine-crible-v-v1.md` ; devis :
  `devis-machine-crible-v-v1.md` ; gabarits de l'addendum, de la fiche et des inscriptions : `gabarits-crible-v-v1.md`.

## 3. Essais joués (sorties gardées dans ce dossier)

Tous joués contre le code scellé ci-dessus, le 2026-11-17 entre 01:26 et 01:36 UTC, sur les **mondes d'essai** (20 mondes MR-2
tirés par `lanceur generer` d'un secret d'essai et d'une phrase d'essai publics, jamais ceux du crible), relais **factices** de la
configuration v12 (aucun appel réel), ports décalés (aucune collision avec d'autres sessions du poste).

| palier | essais | échecs | ce qui est montré |
|---|---|---|---|
| unitaire (`sortie-essais-unitaires-…`) | 40 | 0 | chaque ligne de la liste d'arrêt sur cas sain et artefact : empreintes (addendum, module MR-2 au compagnon refait, gabarit à un octet près), configuration v12 (plafond de Pr-1 changé : refus), relevé de sonde absent ou d'un autre code, corps servis égaux (un épisode retiré : arrêt), coupure sans trace (arrêt), témoin supprimé (arrêt), part atteinte (arrêt), abandon (sain ; premier appel sans répondu ; minimum impossible au monde 3), fonction de décision (oracle, issue, carte chère, archive, loi plantée, autre objet : refus nommés), seuil strict et sens dirigé, jeu public (graine, champ d'issue), cartes valides, rejeu fictif (avant l'écriture, rendant W), placebo (taille k_R + 1, énumération tronquée), rééchantillonnage, graines, règle de M, garde de départ, W_min, partie A (champs du juge), rapatriement (marque de monde), lecture gelée à toutes ses bornes, V1 à V7 |
| jouer (`sortie-essais-jouer-…`) | 9 | 0 | **essai à blanc complet M = 1** (80 appels, une coupure à B_a simulée à 20 s : « échec », journalisée, plafond de session aux dollars, aucune reprise, corps servis égaux et égaux aux pièces préparées, témoins conformes) ; **M = 2** (deux files de dix mondes, 8 relais au plafond de 10 sessions, deux coupures) ; panne de relais d'un fournisseur ayant répondu (le crible continue, appels restants « échec » non lancés) ; panne au premier appel (arrêt) ; panne rendant le minimum impossible (arrêt, « non concluant ») ; coût au-dessus du pire cas (arrêt, dépense comptée) ; corps altéré (arrêt avant les appels du monde) ; témoin supprimé (arrêt) ; garde de départ (refus avant tout dossier) ; mode réel sans ses pièces (refus avant tout dossier) |
| mesure (`sortie-essais-mesure-…`) | 5 | 0 | mesure une seule fois par le lanceur, sorties principale puis fictive scellées, lecture écrite ; seconde mesure refusée ; programme joué sur un jeu de cartes de référence (k_R = 5, S_R = 0,6449, W_R = 15, W_B = 20, p_choix = 0,0036) **égal au recalcul indépendant** (cartes valides, q_w, couvertures hors K1, dollars publics, placebo exact, rééchantillonnage, jeux publics) ; division par zéro forcée : code 1, aucune sortie |
| banc de mutations (`sortie-banc-mutations-…`) | 52 mutations + 3 témoins | 0 survivante | toutes les mutations exigées par l'étape 0 du texte (règle qui lit l'oracle, une issue, les cartes chères ; « ≥ » pour « > » ; minimum des deux sens ; jeu public tiré du secret ou porteur d'issues ; carte refusée, tronquée, au-delà de six comptée ; effet de K1 compté ; placebo k_R + 1 et énumération tronquée ; dollars de la configuration ; rééchantillonnage tiré des données ; carte chère servie à une session bon marché ; production appelée avec l'archive fictive ou une loi plantée ; monde complet à quatre appels ; dollars des appels coupés ou en échec omis ; appel plus long que B_a repris ou non compté en échec ; rejeu fictif avant la sortie principale) et une mutation par garde de la liste d'arrêt et par borne de la lecture : **52 tuées pour la raison attendue** (l'essai nommé échoue) ; témoins sans mutation conformes aux trois paliers |
| répétition de la machine (`sortie-repetition-…`) | 37 cas | 0 écart | outil de la session (14 cas : offre par la garde, création, ligne sans GO-2026-11-15-06 refusée, feu d'un autre GO, commande à deux lignes, clés par leur nom, ligne altérée refusée, échéance, prix relu, dépense, destruction par l'identifiant lu, identifiant tapé ou intouchable refusé, preuve d'absence, cause bornée) ; branche de sortie déjà présente (rien n'est poussé) ; minuterie (DELETE au loueur simulé par l'identifiant, clé masquée) ; phrase absente (arrêt (A)) ; **nominal** (mise en place → fini : barrières 1 à 3 jouées par l'outil, phrase chiffrée RSA-OAEP et effacée, inscriptions sur `main`, essai à blanc à M, crible à blanc, mesure une fois, lecture remise non ouverte, rapatriement sans monde, aucune clé factice ni jeton poussé, états horodatés dans l'ordre) ; feu d'arrêt pendant `jouer` (lanceur et relais arrêtés par leurs PID, arrêt (A)) |
| énumération du placebo (`sortie-chrono-placebo-…`) | 2 lancements | — | 0,364 s au pire cas (n_c = 20, k_R = 10), par le programme de mesure lui-même ; charge du poste ≈ 11 |

Durées relevées et conditions : `devis-machine-crible-v-v1.md`, § 4. **Incidents** : (i) deux essais d'abord mal écrits (partie A :
une loi constante est dans le nul de K1 par construction ; module MR-2 : le compagnon non refait masquait l'empreinte écrite ;
borne V1 à 7) et deux mutations d'abord survivantes (G10, R07) : essais renforcés, banc rejoué entier ; (ii) une première répétition
nominale arrêtée en « arret (A) : un port des relais est occupé (8811) » par une autre session du poste qui jouait ces ports : la garde a
tenu ; ports décalés en répétition (variable de répétition seulement) et contrôle des ports aligné sur le serveur des relais
(`SO_REUSEADDR`) ; (iii) le disque du poste s'est rempli pendant un essai (d'autres sessions) : dossiers de travail périmés effacés,
essais rejoués ; aucune sortie gardée n'en vient ; (iv) une commande de contrôle a été bloquée par le crochet de calcul parce qu'elle
contenait le nom de l'outil du loueur suivi d'un verbe de création dans un motif de recherche : rien n'a été lancé.

## 4. Réserves et choix à contre-lire (aucun ne change une prédiction, un seuil ou un étage)

1. **Étiquette des épisodes** : « crible-v-v1|episodes-developpement » (lecture de « règle des graines du bloc gelé, étiquette neuve
   crible-v-v1 », « Partie B ») ; l'identifiant opaque de l'archive {K1} garde l'étiquette du pilote (il ne dit rien du monde).
2. **« Répondu » vu du lanceur** : complet avec au moins une carte admise d'emplacement ≤ 6 ; l'évaluabilité (oracle) n'est jugée que
   par la mesure. La règle d'abandon (« perdu en entier », « minimum encore possible ») peut donc compter répondu un appel dont toutes
   les cartes admises sont non évaluables (cas rare ; la mesure, elle, suit la définition du texte).
3. **Coupure à B_a** : la commande est tuée ; le relais peut poursuivre la requête à l'amont jusqu'à son propre délai (3 540 s pour
   Pr-2 et Pr-4, 1 740 s pour Pr-1 et Pr-3) pendant que la file passe au monde suivant ; sa ligne de journal peut ne jamais venir
   (relais arrêtés à la fin) : l'appel est alors compté au **plafond de session** (borne haute ; source `plafond_coupure`) ; la
   console de Lazar fait foi pour la facture (R-2803).
4. **Sonde neuve** : elle passe par les quatre relais du crible aux ports de la file 0 ; à M = 2, les relais de la file 1 (ports 8821 à
   8824) ne sont éprouvés que par l'essai à blanc sur la machine.
5. **Archive fictive** (sensibilité sans verdict) : K1 ; K1 et chaque composante forte ou moyenne (monde réduit) ; K1 et toutes ensemble.
   Choix de l'écriture du code, à contre-lire (le texte dit « K1 et les composantes fortes et moyennes du monde »).
6. **Essai à blanc sur la machine** : la coupure y est simulée à une borne d'essai de 60 s (non 900 s : quinze minutes de machine
   épargnées), par le même chemin de code ; dans les essais de ce dossier, à 20 s.
7. **Feu d'arrêt pendant `jouer`** : le lanceur reçoit TERM par son PID et meurt sans relevé partiel (comme le pilote) ; ses relais
   sont arrêtés par leurs PID (`pids-relais.json`) ; les commandes en vol, orphelines, échouent quand leur relais meurt.
8. **Clés passées à la création** (comme GO-2026-11-15-04 pour le pilote) : configuration de l'instance chez le loueur et
   environnement de la minuterie (sous-processus de l'amorce) jusqu'à la destruction ; le programme machine les retire de son
   environnement et ne les donne qu'à `sonde` et `jouer` réels ; balayage avant chaque poussée.
9. **Garde de départ** lue à la lettre (6 000 + 3 D + ⌈20/M⌉ × 900 s restant au départ des appels, barrières déjà passées comprises) :
   prudente ; avec D ≈ 5 000 s, elle demande 39 000 s au départ des appels, soit au plus ≈ 6 h 10 de mise en place, barrières,
   génération, préparation et essai à blanc depuis l'impression.
10. **Port occupé** : un relais d'une autre tâche sur 8811 à 8824 arrête la machine (arrêt (A), constaté en répétition quand une
    autre session jouait sur ce poste les mêmes ports ; les répétitions et essais de ce dossier emploient des ports décalés).
11. **Partie A** écrite et essayée sur un relevé synthétique seulement : la forme du relevé de v67 attendue par l'adaptateur
    (en tête de `partie_a_crible_v_v1.py`) n'a pas été vérifiée (relevé non ouvert, branche de données) ; à relire par son premier
    lecteur avant l'essai sain ; la partie A n'est pas jouée.
12. **Banc de mutations** : les mutations de la mesure sont tuées sur un **jeu de cartes de référence écrit par les essais** (lois des
    mondes d'essai réduites à K1, à une moyenne, à toutes les certifiées, et cartes pièges), parce que les relais factices ne rendent
    aucune carte portant une composante certifiée au-delà de K1 (essai à blanc : « hors de la zone utile ») ; les cartes de vrais
    proposeurs ne sont éprouvées qu'au feu.
13. **Durées relevées sur ce poste** (information, § 3) : poste à 4 processeurs partagé avec d'autres sessions (charge 9 à 13) ;
    bornes hautes, jamais D.
14. **Le relevé de la sonde neuve** n'a pas de cas sain hors d'un appel réel (ses conclusions demandent des usages de fournisseur) :
    absent, d'un autre code, d'un autre chemin de relais : refusés (artefacts) ; la sonde à blanc écrit un relevé de forme complète.
15. **Rapatriement de la sonde** non répété (la répétition saute la sonde réelle) ; mêmes règles que le rapatriement du crible.

## 5. Ce qui reste avant le feu

1. **Texte qui fera foi** : la v2 est jugée scellable (tour différentiel 2) ; **à sceller par `sceller_prereg` et copier sous
   `prereg/`** (mère) ; son empreinte devient la racine des graines.
2. **Contre-lecture du code** (étape 0 du texte : sous-agent neuf **d'un autre modèle**, R2) : lanceur, mesure, lecture, partie A,
   amorce, programme machine, outil de la session, essais, banc, répétition, procédure, devis ; rendue `scellable`.
3. **Addendum d'empreintes** scellé sous `prereg/` (gabarit au § 1 de `gabarits-crible-v-v1.md`) : empreintes du code de ce rapport
   (§ 1), sorties gardées des essais, du banc et de la répétition ; il ne change rien d'autre.
4. **D, M et la date** : les quatre durées (mise en place, génération, mesure, rapatriement) **ne sont pas dans la section lue du
   verdict du pilote** : par la règle écrite, le budget reste **« non lançable », mot de la mère**, tant qu'elles ne sont pas relevées
   sur les états nommés du journal de la machine du pilote (lecture que ce développeur n'a pas faite : elle passe par la branche de
   sortie du pilote) ; puis M par la règle ; **fiche de lancement** commitée (D, M, texte, addendum).
5. **Lignes « calcul » κv1 (104,39 USD) et κv2 (100,28 USD)** inscrites par la mère, citant GO-2026-11-15-06 (l'outil refuse
   sinon) ; avant κv2, lire sur la pièce de dépense du pilote les coûts par appel de Pr-1 (F-1 du tour différentiel 2) ; enveloppe :
   ce crible seul 204,67, avec (iii) 474,67 (sous 1 275) ; les cinq ensemble non (nœud de Lazar au dernier crible).
6. **Mots de Lazar** : passage des trois clés et du jeton des machines à la machine du crible (GO-2026-11-15-04 ne portait que sur le
   pilote) ; présence de Lazar pour la demi-heure qui suit l'impression (mot daté de moins de dix minutes) ; **sa phrase**, tapée par
   lui dans la session qui lance, après l'inscription de l'empreinte du secret.
7. **Engagement du secret** : la machine tire le secret et pousse son empreinte ; la mère l'inscrit sur `main` avant la phrase
   (barrière 1). **Mondes vérifiés et empreintes** : la machine génère et vérifie les 20 mondes (C0 à C8 v4, C-16, C-17) et pousse H,
   HC et S1 à S20 ; la mère les inscrit avant le feu 2 ; D et M inscrits avant le feu 3.
8. **Ligne de feu** au registre des décisions (forme du § 4 des gabarits), crédit du loueur, préavis à Lazar, rappel à l'échéance
   plus cinq minutes.
9. **Calendrier** : rien dans ce code n'attend le 21 novembre ; dès les points 1 à 8 levés, le crible part ; durée attendue sur la
   machine ≈ 2 h 40 d'appels à M = 1, plus les barrières (1 h 40 au plus), la génération et la mesure ; l'accord échoit le 30 novembre.

## 6. Déclaration

Je déclare avoir écrit seul ces pièces, en fichiers neufs, sans modifier aucun fichier existant, sans commit ni poussée ; n'avoir
créé aucune machine, n'avoir appelé ni le loueur ni aucun fournisseur de modèles, n'avoir employé ni lu aucune clé, n'avoir rien
dépensé ; n'avoir ouvert ni l'issue du pilote MR-2 v14 (seule la section « Pour les cribles » de la consigne), ni aucune branche
`calcul/pilote-mr2-v74-entree-*`, ni rien sous `diag/`, `runs/`, `donnees/` ; n'avoir changé aucune prédiction gelée (R-2993) ;
aucun identifiant de modèle n'est écrit dans ces pièces (clés de configuration seulement). Les mondes des essais sont tirés d'un
secret d'essai public et d'une phrase d'essai, jamais ceux du crible.
