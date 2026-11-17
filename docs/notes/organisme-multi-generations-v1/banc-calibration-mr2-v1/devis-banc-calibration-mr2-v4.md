# Devis du banc de calibration complet MR-2 (24 mondes, ordre D-2, la règle en dernier) — v4

- **Statut** : devis, **sans lancement**. Il est **refait pour le banc complet** (GO-2026-11-17-05 : Q-B1 (a) machine jetable louée,
  secret et mondes seulement sur elle ; Q-B2 (b) un seul banc complet ; Q-B3 (a) dénominateur = tous les mondes tirés), sur les
  règles de la pièce `regles-banc-calibration-mr2-v1.md` (même dossier, `87d7536ee10a4f240aec7fe1ee4200e1a5d7d168daab816a4e8ca7e6139d87f7`,
  v1 à contre-lire). Aucune dépense, aucune machine louée, aucun appel au loueur ni à un fournisseur de modèles, aucun commit. Il
  **propose** une ligne « calcul » (section 9), que la mère inscrit si son pire tient sous 3 USD et que le devis est contre-lu
  (GO-2026-11-17-05).
- **Version v4** : texte neuf (le périmètre change : banc complet au lieu du « banc de la règle seul » de la v3). La v3
  (`devis-banc-calibration-mr2-v3.md`, `ec5a6e99313dd1a48f4105e756813b3500a1181cc66babbb0af4bfb7c5a62eb2`) reste intacte (R12). Les
  deux mineures du tour 3 de sa contre-lecture (m8, m9) et la mineure neuve de la fin du tour 1 (m10) sont reprises (section 12).
- **Rédacteur** : modèle A, rédacteur neuf, sous-agent d'un script d'orchestration de la session mère ; je n'ai écrit ni les
  versions v1 à v3 de ce devis, ni leurs contre-lectures, ni la conception, ni le préenregistrement, ni le code du pilote, ni son
  verdict. J'ai écrit la pièce des règles v1, la mesure des durées et le calcul de ce devis (section 1). **Réserve de lignée** :
  même lignée que le rédacteur de la v1 ; la contre-lecture doit venir d'un lecteur neuf d'une autre lignée (modèle C).
- **Heures** (`date -u`) : début de la tâche 2026-11-17 02:34:42 ; mesure des durées 02:51:19 à 02:59:56 ; calcul 03:05:41 ;
  rédaction du devis à partir de 03:10:34 ; fin : dernière ligne.

## 0. Verdict en trois lignes

1. **Le banc complet n'appelle aucun modèle** : part sur crédits de Claude **0 USD** attendu et au pire ; seule dépense : la machine
   jetable louée, **hors crédits**.
2. **Attendu ≈ 0,31 USD** (≈ 6,0 h à 0,052222 USD/h, prix de la machine du pilote, sur 8 processeurs et 4 processus ; de 0,17 à
   0,89 USD selon la machine et son prix) ; **pire ≤ 2,99 USD : le pire tient sous 3 USD**, par construction (minuterie × prix relu
   maximal ≤ 3 USD), la minuterie et la borne de prix suivant le nombre de processus choisi à la location : **18 h et 0,166 USD/h à 8
   processus ; 23 h et 0,13 à 6 ; 33 h et 0,09 à 4**. Aucun nœud de dépense : la mère peut inscrire la ligne une fois ce devis
   contre-lu.
3. Le banc complet demande ≈ **17 h de calcul d'un processus attendues et 85 h au pire**, contre ≈ 5 h pour le banc de la règle seul
   (v3) : les règles de n et de forme et les mesures dominent. Avant toute location, l'**essai à blanc du lanceur** sur 2 mondes de
   développement relit ces durées (garde de durée, section 6) ; le **code de la course et du banc reste à écrire**, pas seulement à
   contre-lire.

## 1. Pièces lues et écrites (chemin, empreinte ; recalculées, égales à leur compagnon)

Chemins relatifs à `docs/notes/organisme-multi-generations-v1/` sauf mention.

| pièce | empreinte sha256 | usage |
|---|---|---|
| verdict v2 du pilote MR-2 v14 (seule pièce de la sortie du pilote lue ; branche `verdict/pilote-mr2-v74-v14-v1`, commit `61230010`, par `git show`) | `e64458e82bae1d03e40656ad3b65456769eefd2603a7306e9a7d401eba8e1a3d` | prix et heures de la machine, dépense, durées par appel |
| rapport du développeur du code v68 du pilote (branche `prep/pilote-mr2-v1`, tête `a5fdfcdf`, par `git show`) | `6635e43a11956eb28d7eb8ee4e0975405bbceea32572609e13b0fa8812d82a51` | §6 : 4 mondes de développement vérifiés en 882 s ; §9 |
| pièce des règles du banc v1 (écrite dans cette tâche) | `87d7536ee10a4f240aec7fe1ee4200e1a5d7d168daab816a4e8ca7e6139d87f7` | comptes par étape, ordre, gardes |
| `banc-calibration-mr2-v1/mesure-durees-banc-mr2-v1.py` (écrit et scellé avant son passage) ; sortie `.json` ; `.stdout` | `7fe05002ef12b917b1604d9024a4430d641f45511b8aa7eaee38dd364ff6e126` ; `d0c3e21af65b2facaa66e801ceec0015c2acc530728261e7f48a9a47a44a760a` ; `1863044f1fc55301a1dca460b5948fbf30798bbf511581d0b48e8c7158df409c` | durées unitaires (section 4.1) |
| `banc-calibration-mr2-v1/calcul-devis-banc-mr2-v4.py` (écrit et scellé avant son passage officiel) ; sortie `.json` ; `.stdout` | `1cccc7d4c02f905abcc1e0fce5ea6142b3d109ee0330363c1e4ab212d69061be` ; `892fe8d4f4e4cd7c7e083d98adf669ddd38c9a1a850f979a2f7b7b5a15808be2` ; `e2dc58e88393cefa9822951771e4d91dfa181dee22f4f454206bed6884654d51` | toutes les durées et tous les montants des sections 4 et 5 |
| `devis-banc-calibration-mr2-v3.md` et ses contre-lectures : tour 1, tour 2, tour 3, fin du tour 1 | `ec5a6e99…` ; `7fd26c76…` ; `ec7c4e9d…` ; `281bb6ee…` ; `af8862a6…` | reprise des mineures, bornes de la machine du pilote recopiées par la v3 |
| `sorties-v4/journal-sorties-v4.txt` ; `sorties-v4/partie-v4-monde-0.json` (heures) | `8d284f0b6dbcfcbbb00385ab6d8ecfec08e5f14bceb001b8a99fc9175381498b` ; compagnon | recoupement des durées (section 4.2) |
| conception v7 ; brouillon 6 du préenregistrement de la course | `1f1b64df…` ; `4deec525…` | périmètre, ordre D-2, mesures citées |
| lignes GO-2026-11-13-01, -13-02, -16-08, -17-05 | registre vivant `registres/go.md` | conditions, plafond de 3 USD |

Rien d'autre de la sortie du pilote n'a été ouvert ; aucune branche `calcul/pilote-mr2-v74-entree-*` ; aucun secret, aucun monde de
calibration ni de course. La mesure des durées tourne sur la **graine publique de développement** r = 0
(`cle("monde-mr1-v4-calibration-developpement", 0)`), avec le code scellé de la conception v4.

## 2. Ce que le banc complet joue (pièce des règles v1, sections 4 à 8)

Par monde conforme (24 mondes tirés), dans l'ordre :

| poste | contenu (unités par monde) | durée attendue (s) | au pire (s) |
|---|---|---|---|
| S0, tirage et vérification | 1 tirage conforme (C0 à C8 : 200 graines par composante à n = 400) et ≈ 1 tirage refusé (ρ = 0,5) | 281,3 | 674,6 |
| S1, règle de f | 12 lois synthétiques, attribution à 4 valeurs de f | 1,9 | 2,4 |
| S2, fusion | au plus 9 lois V-K1+i, attribution | 10,0 | 35,0 |
| S3, règle de n | 2 générations simulées (n = 400) ; archive A₈ ; 2 lois × 5 valeurs de n × 200 graines = **2 000 jugements** contre 8 lois | 883,0 | 2 130,8 |
| S4, règle de forme | 6 copies × 200 graines = **1 200 jugements** contre 8 lois, à n retenu | 428,4 | 1 797,0 |
| S5, règle de τ | 3 générations simulées à n retenu | 134,0 | 201,6 |
| S6, règle de garde | 8 générations 1 simulées (passe qui décide et 7 passes rapportées) | 280,9 | 422,6 |
| M1, surdité | composantes certifiées non couvertes par A₃ (1 attendue, 3 au pire) × 200 graines, et leur référence {W₋ᵢ} | 123,2 | 1 345,5 |
| M7, valeurs [BANC] | jeu planté de 3 générations (15, 21, 21 lois ; 19, 25, 25 au pire) × 20 répétitions | 422,5 | 1 846,6 |
| M2, M4, M5, M6 | tranche de choix, paires de doublons, fréquences, chronométrage | 15,0 | 18,8 |
| **total par monde** | | **2 580,2 (43 min)** | **8 474,9 (2 h 21 min)** |

Source : `calcul-devis-banc-mr2-v4.json` (`892fe8d4…`), champ `par_monde_s` ; la colonne « pire » porte déjà les facteurs de la
section 4.3 sauf celui de la machine. Aucun appel de modèle, aucun jeton, aucun gabarit servi.

## 3. Ce que le pilote a mesuré, et ce que le devis en prend (verdict v2 seul)

| mesure du pilote (verdict v2) | valeur | usage au devis |
|---|---|---|
| machine | 0,082018 USD pour 1,5706 h à **0,052222 USD/h** ; création 11:26:57Z, destruction 13:01:11Z | **prix attendu** de la machine |
| passe du pilote | manifeste `debut_utc` 12:14:34Z, `fin_utc` 12:59:07Z | **surcharge attendue** : (création → début : 47 min 37 s) − génération des 4 mondes (882 s au conteneur, rapport v68 §6) + (fin → destruction : 2 min 4 s) = **0,583 h** |
| tentative antérieure | « machine d'une tentative antérieure » : 0,074757 USD | risque d'une tentative perdue avant le tirage (section 8, point 7) |
| dépense totale | 15,378197 USD, aucune part atteinte ; « la console fait foi » (R-2803) | — |
| durées et coûts par appel (proposeur C1 de 389 à 553 s, les trois autres de 34 à 109 s ; deux appels tronqués de C1) | — | **n'entrent pas** dans ce devis (aucun appel au banc) ; ils servent au devis de la course |
| p_c = 0 sur 14 appels, intervalle [0 ; 0,043] | — | règles du banc (P_CACHÉE = 0 décide ; borne haute rapportée), non le coût |

Bornes de l'offre de la procédure du pilote, recopiées par le devis v3 (§4) : au moins 4 processeurs, 8 Go, 20 Go de disque, au plus
0,15 USD/h, relu au plus 0,17, avec ou sans carte graphique (inutilisée) ; aucune offre à processeurs seuls au 16 novembre (R-2947,
cité par la v3). Ce devis les **resserre** selon le nombre de processus (section 6).

## 4. Durées

### 4.1 Durées unitaires mesurées (`mesure-durees-banc-mr2-v1.json`, `d0c3e21a…`)

Un processus, `OMP_NUM_THREADS=2`, Python 3.13.18, numpy 2.5.3, juge **simplifié** de la conception (le juge de la course n'est pas
écrit) ; conteneur partagé, charge moyenne 7,08 au début et 9,61 à la fin, pour 4 processeurs visibles.

| opération | durée (s) |
|---|---|
| jugement d'une carte, n = 200 / 400 / 800, archive de 1 loi | 0,074 / 0,100 / 0,182 |
| idem, archive de 8 lois | 0,250 / 0,357 / 0,599 |
| idem, archive de 17 lois | 0,326 / 0,506 / 0,710 |
| tirage conforme (génération 11,58 + vérification C0 à C8 207,97) | 219,6 |
| tirage refusé en C6 (génération 5,40 + vérification 56,84) | 62,2 |
| génération 1 simulée complète, n = 400 / 800 (course v4, plus 5,0 s pour regrouper sur 2 000 instances au lieu de 1 500) | 35,1 / 38,4 |
| génération 2 ou 3 simulée, n = 400 (même correction) ; n = 800 | 41,9 ; 47,7 et 46,7 |
| regroupement de 24 cartes, 1 500 / 2 000 instances | 22,5 / 27,5 |
| attribution d'une loi ; enveloppe d'une archive de 8 / 17 lois | 0,11 ; 3,1 / 5,1 |

Médianes de 3 essais pour les jugements ; une mesure pour le reste. Le regroupement domine une génération simulée ; le jugement
domine les règles de n et de forme et les mesures M1 et M7.

### 4.2 Recoupement avec le journal de la conception v4

Le monde 0 de la v4 (même graine publique, même code, même interpréteur) a pris **424 s** (08:02:20 → 08:09:24, journal
`8d284f0b…`) pour les mêmes opérations que celles mesurées ici : 5,4 + 56,8 + 11,6 + 208,0 (deux tirages, un refus C6 comme en v4)
+ 30,1 (une génération) + 103,9 (trois générations) = **415,8 s** : écart de 2 %. La charge du conteneur n'a donc pas faussé la
mesure de façon visible ; elle reste dite.

### 4.3 Facteurs du pire, écrits d'avance (`calcul-devis-banc-mr2-v4.py`)

| facteur | valeur | raison |
|---|---|---|
| juge de la course contre juge simplifié | **× 2** sur les jugements | non mesuré (le juge de la course n'est pas écrit) ; garde de durée à l'essai à blanc (section 6) |
| générations simulées | × 1,1 | le jugement n'y pèse qu'une petite part |
| monde le plus lourd | × 1,25 | 10 composantes au plus, 8 au monde mesuré |
| n retenu | **800** (bord de la grille) | règles de forme, de τ, de la garde, mesures |
| refus du générateur | ρ = 0,6 par tirage, chaque refus au coût d'un tirage complet | v4 : 0,5, refus presque tous avant C8 |
| mesures | M1 : 3 composantes ; M7 : 19, 25 et 25 lois | contre 1 et 15, 21, 21 attendus |
| machine louée plus lente que ce conteneur | **× 1,5** (au pire seulement) | comme la v3 (m10 : le facteur ne vaut qu'au pire) |
| efficacité du parallélisme | 0,8 | barrières entre les étapes (chaque valeur retenue attend tous les mondes), mondes inégaux |

### 4.4 Durée totale selon le nombre de processus

Calcul : 24 mondes × durée par monde (× 1,5 au pire) ÷ (P × 0,8) + surcharge (0,583 h attendue ; au pire 0,5 h de mise en place,
1 h de barrière de la phrase de Lazar, 0,5 h de rapatriement et de destruction : 2,0 h). Calcul d'un processus : **17,20 h
attendues, 84,75 h au pire**.

| processus P (processeurs) | durée attendue | durée au pire | minuterie (pire × 1,15, arrondi au-dessus) | prix relu maximal (3 USD ÷ minuterie, au plus 0,17) |
|---|---|---|---|---|
| **8** (au moins 16) | **3,27 h** | **15,24 h** | **18 h** | **0,166 USD/h** |
| 6 (au moins 12) | 4,17 h | 19,66 h | 23 h | 0,13 USD/h |
| 4 (au moins 8) | 5,96 h | 28,48 h | 33 h | 0,09 USD/h |

## 5. Devis : attendu et pire, crédits et hors crédits séparés

Tout est **estimé** sauf les plafonds. Consigne permanente de Lazar : crédits de Claude au maximum. **Rien ne peut aller sur
crédits** : le banc n'appelle aucun modèle, et la machine se paie chez le loueur.

| poste (USD) | sur crédits : attendu | sur crédits : pire | hors crédits : attendu | hors crédits : pire |
|---|---|---|---|---|
| proposeurs (rôles C1, C2, X1, X2) | 0 | 0 (aucune clé sur la machine) | 0 | 0 |
| expérimentateur, vérificateur, juge à modèle | 0 | 0 | 0 | 0 |
| machine, 4 processus | — | — | **0,31** (5,96 h × 0,052222) ; 0,89 à 0,15 USD/h | **2,97** (33 h × 0,09) |
| machine, 6 processus | — | — | 0,22 ; 0,63 à 0,15 USD/h | 2,99 (23 h × 0,13) |
| machine, 8 processus | — | — | 0,17 ; 0,49 à 0,15 USD/h | 2,99 (18 h × 0,166 = 2,988) |
| réseau du loueur (prix consignés par l'outil) | — | — | quelques millièmes | compris dans la part |
| **total** | **0** | **0** | **≈ 0,31** (0,17 à 0,89) | **≤ 2,99 : sous 3 USD** |

**Le pire tient sous 3 USD** : la dépense d'une machine est bornée par sa minuterie × le prix relu à la création, et la borne de prix
de chaque configuration est fixée pour que ce produit tienne sous 3 USD. Aucun nœud de dépense ; au-delà de ces bornes, pas de
location (section 6).

## 6. Machine, minuterie, coupures

- **Choix de la machine, par règle écrite** (à la location, jamais au jugé) : la plus grande valeur de P ∈ {8, 6, 4} pour laquelle une
  offre a **au moins 2·P processeurs, au moins 4 Go + 1,5 Go par processus, au moins 30 Go de disque**, et un prix au plus égal au
  **prix relu maximal** de P (0,166 ; 0,13 ; 0,09 USD/h) ; carte graphique permise, inutilisée. Aucune offre : pas de location,
  la mère le dit à Lazar (blocage, non une dépense).
- **Coupures** : (i) **minuterie de destruction armée par l'amorce avant toute passe** : 18 h (P = 8), 23 h (P = 6) ou 33 h
  (P = 4), lancée hors de la machine, arrêt par identifiant (R10) ; (ii) prix relu à la création au-dessus de la borne de P :
  destruction aussitôt ; (iii) phrase de Lazar absente dans l'heure : arrêt de la machine ; (iv) **une seule machine** sous la
  ligne ; une seconde n'est créée, après l'absence prouvée de la première et avant tout tirage de mondes, que si la dépense
  consignée plus sa minuterie × son prix relu tient sous 3 USD, sinon nouveau mot de Lazar ; (v) aucune ligne d'extension ;
  (vi) **aucune clé de fournisseur de modèles** sur la machine, le lanceur refuse de démarrer sinon (garde B-7) ; (vii) échéance de
  la ligne : 2026-11-30 (garde B-14).
- **Garde de durée** (neuve, avant toute location) : l'essai à blanc du lanceur du banc sur **2 mondes de développement**, au
  conteneur, un processus, mesure la durée de chaque étape par monde et la mémoire de pointe ; durée projetée au pire = (moyenne
  mesurée par monde × 24 × 1,25 × 1,5) ÷ (0,8·P) + 2 h. Si elle dépasse **minuterie ÷ 1,15** pour le P visé, ou si la mémoire de
  pointe dépasse 1,5 Go par processus : **pas de location** ; devis refait et nouveau mot de Lazar si le pire ne tient plus sous
  3 USD. Le facteur « juge × 2 » de la section 4.3 est alors remplacé par la mesure.
- **Ordre sur la machine** : celui de la pièce des règles (section 4.3) : amorce, minuterie, interpréteur (numpy 2.5.3), arbre et
  empreintes, secret, phrase, tirage et barrière des mondes, étapes 1 à 6, mesures, rapatriement, destruction, absence prouvée ;
  sorties poussées sur une branche neuve `calcul/…`, feux de la mère sur une branche d'entrée (procédure du pilote).

## 7. Ce qu'il faut avant tout lancement

1. **Pièce des règles** contre-lue (R2, lecteur d'une autre lignée), corrigée, **points ouverts tranchés** (sous-choix de τ, nœud de
   Lazar ; Q-4 et Q-6 ; E-1, E-2, E-10, E-11 à la mère), version finale scellée.
2. **Code de la course et du banc** écrit (points V-1 à V-36 du brouillon 6 : générateur et vérificateur à noms neufs, juge,
   regroupement, représentant, oracle, jeu planté, lanceur du banc), essayé (R5, dont les essais T-1 à T-14 de la pièce des règles),
   muté, joué à blanc, **contre-lu par un autre modèle que le développeur**, les quatre points [GO] nommés (regroupement,
   représentant à tranche de choix appariée, réponses brutes, témoins par test), gelé.
3. **Essai à blanc du lanceur et garde de durée** (section 6).
4. **Procédure machine du banc v1**, dérivée de la v14 du pilote (amorce, minuterie, programme machine, outil de session, essais à
   blanc sur dossier jetable), sans clé de fournisseur, vérifiée « jouable » par un lecteur neuf ; crochet `garde_calcul.py` éprouvé
   (cas sain et artefact) ; `GO_ID=` de la ligne du banc en tête de la commande de création.
5. **Ligne « calcul »** inscrite par la mère sur ce devis contre-lu (GO-2026-11-17-05 : pire sous 3 USD).
6. **Engagements** dans l'ordre de la pièce des règles (section 4.3) ; le mot « présent pour la demi-heure » de Lazar, condition de la
   v14, est à garder (la barrière de la phrase a déjà fait perdre une tentative du pilote).
7. **Lecture** du banc par un sous-agent neuf (R13 : elle commande une course de 422 USD de plafonds), puis GO de Lazar.

Rappel des autres conditions de GO-2026-11-13-01 et -02 qui touchent le banc : conception v4 revue et contre-lue (faite : v7,
« scellable ») ; préenregistrement de la course contre-lu et scellé (brouillon 6, non scellable avant le banc) ; code v68 de la
course contre-lu (point 2 ci-dessus) ; **banc de calibration fait (n et seuils fixés par leurs règles)** : c'est ce banc.

## 8. Risques

1. **Le code n'existe pas** : le juge, le regroupement, le représentant, l'oracle, le jeu planté et le lanceur du banc sont à
   écrire, essayer et contre-lire avant le banc ; c'est le plus long des préalables, au regard de l'échéance du **30 novembre** des
   lignes de la course et de la ligne du banc.
2. **Durées** : le juge de la course n'est pas mesuré (× 2 supposé au pire) ; la garde de durée le mesure avant la location. Un banc
   qui dépasserait sa minuterie serait « non jugeable » (au plus 3 USD perdus) et un second banc serait un nœud.
3. **Plafonds de session et autonomie** : la session qui lance peut s'arrêter pendant 3 à 33 h ; les sorties étant poussées par la
   machine et la minuterie la détruisant d'elle-même, une session neuve reprend par la branche de sortie ; destruction et preuve
   d'absence restent dues par identifiant (R10).
4. **Résultat trop propre (R4)** : à P_CACHÉE = 0, G = 24 est le plus probable (0,91) et la règle tient avec une probabilité
   au-dessus de 0,9999 sous le modèle réduit ; l'audit A0 est écrit d'avance ; la passe à la borne haute du pilote tiendrait avec la
   probabilité 0,09 à 0,17 seulement.
5. **Refus du générateur** : probabilité qu'au moins un des 24 mondes n'ait aucun tirage conforme ≈ 9 % au taux de refus de la v4
   (0,5 par tirage) et ≈ 33 % à 0,6 (recalcul : 1 − (1 − 0,5⁸)²⁴ = 0,0897 ; 1 − (1 − 0,6⁸)²⁴ = 0,3340) ; compté au dénominateur,
   sans arrêt.
6. **Offres** : P = 8 demande au moins 16 processeurs ; P = 4 demande une offre à 0,09 USD/h au plus (celle du pilote était à
   0,052222) ; aucune offre à processeurs seuls au 16 novembre.
7. **Tentative perdue** : une tentative antérieure du pilote a coûté 0,074757 USD (verdict v2) ; la règle de la seconde machine
   (section 6, coupure (iv)) garde le cumul sous 3 USD.
8. **Mémoire** : non mesurée ici ; mesurée à l'essai à blanc (garde de durée) ; `ulimit -v` par processus, comme la v4.

## 9. Ligne de GO proposée (non inscrite ; la mère l'inscrit sur ce devis contre-lu, GO-2026-11-17-05)

```
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | **Banc de calibration complet MR-2, part hors crédits** (GO-2026-11-17-05 : Q-B1 (a), Q-B2 (b), Q-B3 (a)) : simulation sur processeur seulement, aucun appel de modèle, aucune clé de fournisseur de modèles sur la machine ; règles de la pièce des règles du banc, version finale scellée (empreinte à recopier) : f, fusion, n, forme, τ, puis la règle de garde en dernier (au moins 12 mondes sur les 24 tirés ; P_CACHÉE = 0 décide), passes et mesures rapportées ; code de la course et du banc gelé et contre-lu ; secret de calibration neuf engagé et poussé avant la phrase de Lazar ; mondes jamais poussés ni réutilisés ; une machine jetable, P ∈ {8, 6, 4} processus choisi à la location, prix relu au plus 0,166 / 0,13 / 0,09 USD/h, minuterie 18 / 23 / 33 h (minuterie × prix ≤ 3 USD) ; garde de durée sur l'essai à blanc avant la location ; seconde machine seulement si dépense consignée + minuterie × prix ≤ 3 USD ; conditions toutes exigées : pièce des règles contre-lue et scellée, points ouverts tranchés, procédure machine du banc vérifiée « jouable », lecture par un sous-agent neuf ; jamais de ligne d'extension ; arrêt par identifiant (R10), dépenses et arrêts consignés | 3 USD (hors crédits) | 2026-11-30 | Lazar (GO-2026-11-17-05) | R-3050 ; devis `devis-banc-calibration-mr2-v4.md` (empreinte à recopier) |
```

Aucune ligne sur crédits de Claude : rien ne s'y paie.

## 10. Décisions

- **Aucun nœud de dépense** : le pire tient sous 3 USD (section 5).
- **À la mère** : inscrire la ligne sur ce devis contre-lu ; les points de la pièce des règles qui lui reviennent (E-1, E-2, E-10,
  E-11, lettre du rédacteur).
- **À Lazar, sans défaut** (pièce des règles, section 12) : sous-choix de τ ; Q-4 et Q-6 s'il ne laisse pas la mère les confirmer ;
  tout second cycle du banc. À lui dire en clair avec la demande de GO : la règle tient presque par construction à P_CACHÉE = 0 et
  ne garde pas contre des proposeurs qui ne masquent pas ; MR-2 ne satisfait pas la lettre de Q-13 (c).

## 11. Déclaration

- **Rôle** : rédacteur neuf du devis v4 ; sous-agent d'un script d'orchestration ; aucune autorité de décision ; lettre : modèle A.
- **Pièces lues** : section 1 ; branches du pilote récupérées dans un dossier neuf du bloc-notes, à profondeur 1 et sans contenus de
  fichiers (filtre `blob:none`), fichiers tirés un à un par `git show`.
- **Calculs** : la mesure des durées (un processus, graine publique de développement, code scellé de la conception v4) et le calcul
  du devis (arithmétique seule) ont été scellés avant leur passage officiel ; le calcul a eu un essai à blanc, sortie au bloc-notes
  hors dépôt, au résultat égal.
- **Interdits tenus** : aucune machine, aucun appel au loueur ni à un fournisseur de modèles, aucune dépense, aucun lancement ;
  aucune branche `calcul/pilote-mr2-v74-entree-*` ; aucun secret, aucun monde de calibration ni de course ; rien sous `diag/`,
  `runs/`, `donnees/` ; aucune valeur de clé, ni `env` ni `printenv` ; aucun fichier existant modifié ; aucun commit ; aucun
  identifiant de modèle écrit (les proposeurs sont nommés par leurs rôles du brouillon 6).
- Les durées et l'attendu de la machine sont **estimés** (mesure unitaire, prix du pilote) ; seules la minuterie et la borne de prix
  sont des bornes.


## 12. Contre-lecture des versions précédentes (v1 à v3), reprise, et ce que la v4 en fait

L'historique de la section 11 de la v3 est repris ici, **avec les deux mineures du tour 3 appliquées à son texte** (m8, m9) ; les
étiquettes de proposeurs du pilote y sont remplacées par leurs rôles du brouillon 6 (aucun identifiant de modèle dans ce fichier).

### Tour 1 (v1 → v2)

- **Rapport** : `contre-lecture-devis-banc-calibration-mr2-tour1-v1.md` (même dossier), empreinte
  `7fd26c76bfcb6c16c722dc4a9a18f91da193b2271c76ec98f8f009598be3e191` ; lecteur : modèle C, contre-lecteur neuf (R2) ; verdict :
  **corrections (2 majeures, 5 mineures)**. Pièce lue : la v1, `6172ae590c29901a040bd39804177a844e74b9f9f7589acf22b7b5e22ca942db`.
- **Rédacteur des corrections** : déclaré par la v2 « un rédacteur neuf (modèle C) » ; le rapport du tour 2 relève que la consigne
  donnait les corrections au modèle A, rédacteur de la v1 ; provenance non établie (tour 2, m6) ; le rapport du tour 1 est du
  modèle C.

| point du rapport | suite (v2) |
|---|---|
| **M1** — liste d'arrêt contre dénominateur | appliquée : « monde sans tirage conforme » retiré de la liste d'arrêt, compté selon Q-B3 et rapporté ; probabilité d'au moins un monde sans tirage conforme chiffrée (≈ 9 % à 0,5 refus par tirage, ≈ 33 % à 0,6 ; recalculées : 1 − (1 − 0,5^8)^24 = 0,0897 ; 1 − (1 − 0,6^8)^24 = 0,3340) |
| **M2** — condition de la course non remplie sous Q-B2 (a) | appliquée (Lazar averti) |
| **m1** à **m5** | appliquées (13 lignes du bloc gelé ; arrondi de l'attendu ; coûts « chacun » du proposeur C1 ; prédiction chiffrée à la borne haute ; couplage des deux passes) |
| remarques facultatives 1 à 4 ; points pour la mère 1 à 5 | non portées, ou portées par M1, M2, m2, m4 |

### Tour 2 (v2 → v3)

- **Rapport** : `contre-lecture-devis-banc-calibration-mr2-tour2-v1.md`, `ec7c4e9de51f73c37424e111b889aab41695ac80b9e508cb59fdcb67e4b597e8` ;
  lecteur : modèle C, neuf ; verdict : **corrections (0 majeure, 2 mineures)**. Pièce lue : la v2,
  `4103d02ce509a8b3d280299aeaa0e82d62d7a796f8a5f8fc6a0f72ed018b47f3`.
- **Rédacteur des corrections** : un rédacteur neuf que sa consigne déclare du modèle C (la même consigne porte aussi « corrections
  par le modèle A ») ; le rapport du tour 2 est lui aussi du modèle C : à ce tour, le même modèle a peut-être lu et corrigé (provenance non établie, comme au tour 1).

| point du rapport | suite (v3) |
|---|---|
| **m6** — rédacteur des corrections du tour 1 | appliquée en substance, « nouveau » du rapport refusé dans sa lettre (attribution non vérifiable remplacée par l'aveu d'incertitude) |
| **m7** — « deux décisions » contre trois | appliquée |
| points pour la session mère 1 à 4 | le point 2 est traité par m6 (peut-être le même modèle au rapport et aux corrections à ce tour, et peut-être au tour 1 si la déclaration de la v2 est exacte : un tour 3 serait à confier à un lecteur d'un autre modèle) |

### Tour 3 (sur la v3) et fin du tour 1 (lecteur neuf, sur la v3)

- **Rapport du tour 3** : `contre-lecture-devis-banc-calibration-mr2-tour3-v1.md` (même dossier), empreinte à lire sur son compagnon :
  `281bb6ee08626b789f40eff3ae1b84df86aa6b364c45d7a2e0800cca749eeffe` ; lecteur : modèle C ; pièce lue : la v3, `ec5a6e99…` ; verdict :
  **corrections (0 majeure, 2 mineures)**.
- **Rapport de la fin du tour 1** : `contre-lecture-devis-banc-calibration-mr2-fin-tour1-v1.md`, `af8862a6fcd2c8ad3ec63931774c870f1ce6162adc83119b464ea4249e4cc10f` ;
  lecteur : modèle C, neuf ; pièce lue : la v3 ; verdict : **corrections (0 majeure, 3 mineures)** : m8 et m9 confirmées, m10 neuve.

| point | où dans la v3 | suite (v4) |
|---|---|---|
| **m8** — recalcul mal arrondi (0,089 et 0,335 au lieu de 0,0897 et 0,3340) | §11, tour 1, ligne M1 | **appliquée à la lettre** dans le tableau du tour 1 ci-dessus (« nouveau » du rapport recopié) ; les mêmes valeurs servent aux sections 8 (point 5) et à la pièce des règles (section 9) ; recalcul refait : 0,08966 et 0,33404 |
| **m9** — provenance non établie affirmée deux fois | §11, tour 2 (phrase du rédacteur ; tableau, points pour la mère) | **appliquée à la lettre** : les deux « nouveau » du rapport sont recopiés ci-dessus (« a peut-être lu et corrigé (provenance non établie, comme au tour 1) » ; « peut-être le même modèle au rapport et aux corrections à ce tour ») |
| **m10** — base de la durée au pire non dite ; facteur de la machine ambigu | §4 | **appliquée en substance** : la section des durées est réécrite ; la base de chaque chiffre est dite (section 4.1 : médianes de 3 essais ; 4.2 : recoupement avec la v4 ; 4.3 : facteurs nommés), et le facteur de la machine (× 1,5) ne vaut qu'au pire, écrit tel |
| remarque 1 (fin du tour 1) : état du code v68 | §7 point 7 ; Q-B2 | **prise** : la v4 dit que le code de la course n'existe pas et reste à écrire (section 0, point 3 ; section 8, point 1) ; la lecture de « code v68 gelé » est fixée par la pièce des règles (section 2 : module neuf égal à la v4) |
| remarque 2 : autres conditions de -01 et -02 qui touchent le banc | — | **prise** (section 7, rappel) |
| remarque 3 et conséquence de m9 : sous-section « Tour 3 » | §11 | **prise** (cette sous-section) |
| remarque 1 du tour 3 et points pour la mère 1 et 4 (indépendance des lecteurs) | — | **à la mère** : les tours 1 à 3 et la fin du tour 1 ont été lus par des lecteurs du modèle C ; ce devis v4 est du modèle A et doit être lu par un lecteur neuf d'une autre lignée (modèle C) ; si la mère veut un lecteur d'un troisième modèle, elle le dit |
| point pour la mère 3 (fin du tour 1) : étiquettes de proposeurs | — | **pris** : ce fichier ne porte que les rôles C1, C2, X1, X2 |

Le fond de la v3 que la v4 garde : lieu (machine jetable louée, Q-B1 (a)), séparation crédits et hors crédits, plafond de 3 USD,
minuterie armée avant toute passe, une seule machine, destruction par identifiant. Ce qu'elle remplace : le périmètre (banc complet),
toutes les durées et tous les montants, la lecture de « code v68 gelé », la ligne de GO proposée.

Fin de la rédaction : 2026-11-17T03:13:58Z (`date -u`, relevée juste avant le scellement).
