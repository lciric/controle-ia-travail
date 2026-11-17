# Règles du banc de calibration complet de la famille MR-2 (mondes riches à doublons) — v1

- **Statut** : pièce des règles du banc complet (GO-2026-11-17-05, Q-B2 (b)), **v1, à contre-lire (R2)**. Elle ne lance rien,
  ne dépense rien, ne tire aucun secret. Une fois contre-lue, corrigée, ses points ouverts tranchés (section 12) et sa version
  finale scellée, elle **fait foi pour l'application** des règles du banc (brouillon 6 du préenregistrement de la course,
  section « Seuil ») ; chaque écart entre elle et le brouillon 6 ou la conception v7 est listé (section 12) et se règle comme le
  brouillon 6 le dit : le texte candidat de la course est corrigé pour l'égaler, ou la pièce est refaite.
- **Rédacteur** : modèle A, sous-agent neuf d'un script d'orchestration de la session mère. Je n'ai écrit ni la conception (v1 à
  v7), ni le préenregistrement de la course (brouillons 1 à 6), ni le code du pilote (v68 à v71), ni le pilote, ni son verdict,
  ni le devis v3 du banc, ni aucune de leurs contre-lectures. **Réserve de lignée** : même modèle que les rédacteurs de la
  conception, du préenregistrement et du code du pilote ; la contre-lecture doit venir d'un lecteur neuf d'une autre lignée
  (modèle C), qui n'ait écrit ni cette pièce, ni le code de la course, ni la conception.
- **Heures** (`date -u`) : début 2026-11-17 02:34:42 ; mesure des durées (pièce d'appui du devis v4) 02:51:19 à la fin de son
  passage ; fin de la rédaction : dernière ligne.
- **Décisions qui la commandent** (registres vivants `registres/go.md`, `registres/decisions.md`) : R-2492 (lignes
  GO-2026-11-13-01, 365 USD sur crédits, et GO-2026-11-13-02, 57 USD hors crédits, « sous conditions toutes exigées », dont
  « banc de calibration fait (n et seuils fixés par leurs règles) ») ; R-2501 (Q-15 (b) : 24 mondes de calibration) ;
  GO-2026-11-16-08 (issue P-2 du pilote acceptée ; le banc n'est pas lancé par ce mot) ; **GO-2026-11-17-05** (Q-B1 (a) : machine
  jetable louée, secret et mondes seulement sur elle ; Q-B2 (b) : **un seul banc complet, après la pièce des règles du banc et
  le code v68 de la course contre-lus, la règle en dernier (ordre D-2)** ; Q-B3 (a) : **dénominateur = tous les mondes tirés**).
- **Langue** : sans sigle ; les termes « loi », « promue », « retenue », « nat », « gain », « au-delà de l'archive », « au-delà de
  l'enveloppe », « composante », « conditionnelle », « condition », « couvre », « captée » ont le sens du brouillon 6 (en-tête,
  « Langue »).

## Pièces lues (chemin, empreinte ; recalculées, égales à leur compagnon)

Chemins relatifs à `docs/notes/organisme-multi-generations-v1/` sauf mention.

| pièce | empreinte sha256 | lu |
|---|---|---|
| `conception-monde-riche-doublons-v7.md` (fait foi pour la famille et la règle de garde) | `1f1b64df885a5215eb481692671e73167a16e7cfc3d5558610f3d45811d1137a` | entière |
| `contre-lecture-conception-v5-tour3-v1.md` (« scellable » ; remarque sur les graines du juge et du test de mort) | `d94f75c1dcf7e2624ca5d052bcccc088cf7104bdf4255b208e962ceddbb8bec1` | entière |
| `preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon6.md` | `4deec5252a35362f5ef050834a9b56836e76385bcc1f28d860368b37ac251a82` | entier |
| `contre-lecture-preenregistrement-course-tour3-v1.md` (m-18, m-19 : sans effet sur les règles du banc) | `aa9c6c19643c89e46d87b0fb609fa2cec4e0d6286f493caf9de6bb3e8f9d5da8` | entière |
| `preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon3.md` (§3.6, §6, §16) | `2dda3b74ff5e13d56a8f0818623b0b64730a3b3da5f86a136df321343f653a39` | en partie |
| `conception-monde-riche-doublons-v3.md` (§1.6, §1.8, §3.3, §3.4) | `386d48bacd6c487d88846d0991d83bd4ad95122f70500d6fbeb7859cde56659c` | en partie |
| `verification-conception-v3-fable-v2.md` (F-2 : mesure de surdité, règle de n) | `8646ed4fb542b86b99db0a6126152541c54c3292d1f6a719f8ad9f66e2c95ed2` | F-2 |
| `banc-calibration-mr2-v1/devis-banc-calibration-mr2-v3.md` et ses contre-lectures (tours 1, 2, 3, fin du tour 1) | `ec5a6e99…` ; `7fd26c76…` ; `ec7c4e9d…` ; `281bb6ee…` ; `af8862a6…` | entiers |
| verdict v2 du pilote MR-2 v14 (seule pièce de la sortie du pilote lue), branche `verdict/pilote-mr2-v74-v14-v1` (commit `61230010`), `pilote-v1/lecture-issue-pilote-v14-mere/verdict-issue-v2/verdict-issue-pilote-mr2-v14-v2.md`, par `git show` | `e64458e82bae1d03e40656ad3b65456769eefd2603a7306e9a7d401eba8e1a3d` | entier |
| rapport du développeur du code v68 du pilote, branche `prep/pilote-mr2-v1` (tête `a5fdfcdf`), `pilote-v1/code-v68/rapport-developpeur-code-pilote-v68-v1.md`, par `git show` | `6635e43a11956eb28d7eb8ee4e0975405bbceea32572609e13b0fa8812d82a51` | entier |
| programme de la mesure du pilote, même branche, `pilote-v1/outils/mesure_pilote_v4.py` (fonction `graine_monde_pilote`, lignes 250 à 270, et en-tête seulement) | `676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365` | extrait |
| `outils-v4/monde_riche_v4.py` (famille, `course`, `resume`) | `4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8` | entier |
| `outils-v1/monde_riche_outils_v1.py` (oracle, juge simplifié, e-BH, test de mort) ; `outils-v1/puissance_monde_riche_v1.py` (`cle`, `rng_de`, `_bruiter`, attribution par monde) | `1825b956…` ; `7344b107…` | extraits |
| `outils-v2/verifier_monde_v2.py` (C7, C8, ordre des contrôles) ; `outils-v2/monde_riche_outils_v2.py` (`grouper_v2`, `representant_v2`) ; `outils-v2/attribution_v2b.py` ; `outils-v2/puissance_monde_riche_v2.py` (paires de doublons) ; `outils-v3/puissance_monde_riche_v3.py` (`representant_v3`) | `d8f2f634…` ; `3fab97a1…` ; `dee69027…` ; `12458ee3…` ; `60aee2a3…` | extraits |
| lignes GO-2026-11-13-01, -13-02, -16-08, -17-05 | registre vivant `registres/go.md` | lignes |

Rien d'autre de la sortie du pilote n'a été ouvert ; aucune branche `calcul/pilote-mr2-v74-entree-*` ; aucun secret, aucun monde de
calibration ni de course.

## 0. En dix lignes

1. Le banc complet joue, sur **24 mondes de calibration** tirés d'un secret neuf, sur une machine jetable louée, **sans aucun appel
   de modèle**, les six étapes de l'ordre D-2 : **f, fusion, n, forme de la valeur e de groupe, τ, puis la règle de garde en
   dernier** ; ensuite seulement, des mesures qui ne décident rien.
2. Code : celui de la course, gelé et contre-lu, dont le **module MR-2 à noms neufs, égal à `monde_riche_v4.py`** (lecture de
   « code v68 gelé » tranchée ici sous réserve de la mère, section 2) ; `monde_riche_v4.py` n'est que la référence de l'essai R5-7.
3. Juge : **le juge de la course** (celui qui jugera les cartes réelles) ; la certification C8 garde le juge interne du
   vérificateur de la famille (section 3) ; écart de lettre avec « juge simplifié » (conception v7 §3.2), section 12.
4. Proposeurs : modèle synthétique gelé de la v3b ; **P_CACHÉE = 0** (p_c ponctuel du pilote) décide ; P_VUE = 0,25 supposée ;
   test de mort simulé par la statistique gelée, sans expérimentateur ni bac.
5. Chaque règle a son objet, sa simulation, sa mesure, sa décision et son repli écrits d'avance (section 7). Trous du brouillon 6
   fermés ici : l'archive de 8 lois de la règle de n et la simulation qui la fait ; la loi « à moins de 0,01 nat » de la même
   règle ; la définition de la troisième forme ; la fusion contre l'effet de K1 ; ce qu'est une composante fusionnée « captée ».
6. Règle de garde : G sur les **24 mondes tirés**, tenue si **2·G ≥ 24** ; elle tient **presque par construction** à P_CACHÉE = 0
   (au-dessus de 0,9999 sous le modèle réduit) ; passes rapportées sans décider à la borne haute du pilote (tenue avec la
   probabilité 0,09 à 0,17), à 0,01 à 0,05 et sans masquage.
7. Mesures hors D-2 (surdité, tranche de choix de 2 000 épisodes contre 400, C7 sur les pièces gelées, doublons sur paires
   difficiles, fréquences des sortes, coût de d_nul à 48 feuilles, valeurs [BANC] des prédictions) : définies ici, rapportées, sans
   effet sur aucune valeur.
8. Ordre des engagements : cette pièce finale, le code du banc, le modèle de proposeurs et la règle **poussés avant le secret** ;
   le secret poussé **avant la phrase de Lazar** ; les empreintes des mondes au registre avant tout calcul ; **un seul banc**.
9. Avant le banc, sans défaut : sous-choix de τ (Lazar) ; confirmation de Q-4 et Q-6 (Lazar ou la mère, brouillon 6, point
   ouvert 11) ; tout second cycle est un nœud ; la dépense suit le devis v4.
10. Ce texte ne décide pas de la course : la lecture du banc par un lecteur neuf (R13) et le GO de Lazar le font.

## 1. Ce que le banc fait, et ce qu'il ne fait pas

- **Il fait** : sur chaque monde de calibration conforme, il simule des générations de l'organisme avec des **cartes
  synthétiques** (modèle de proposeurs gelé, section 5) passées par la **chaîne de la course** (gardien, regroupement, juge, e-BH sur
  les groupes, représentant, test de mort simulé) ; il en tire, par des règles écrites d'avance et dans l'ordre D-2, les valeurs
  de f, de la fusion, de n, de la forme de la valeur e de groupe et de τ ; il mesure la règle de garde **en dernier** ; il
  rapporte des mesures qui ne décident rien.
- **Il ne fait pas** : aucun appel de modèle (la machine ne porte aucune clé de fournisseur de modèles) ; aucun test de mort par
  l'expérimentateur, aucun bac `bwrap` ; **il ne mesure rien sur les vrais proposeurs** (conception v7 §3.3 : la garde contre des
  proposeurs qui ne masquent pas est le pilote, non le banc) ; il ne règle aucun seuil hors de ses règles ; il ne lit aucune
  issue de la course ; il ne réutilise ni les mondes du pilote, ni les mondes de développement, ni le secret de test.
- **« Banc complet »** : les six étapes de D-2 jouées sans arrêt et leurs sorties rapatriées. Les mesures hors D-2 sont dues ;
  leur échec s'écrit et n'annule pas les étapes (section 11, garde B-6).

## 2. Lecture de « code v68 gelé » (point M-1 de la conception, point ouvert 2 du brouillon 6) : tranchée ici, sous réserve de la mère

Deux lectures restaient ouvertes : (a) l'arbre v68 à v74 du pilote, qui importe `monde_riche_v4.py` sans le changer (devis v3,
écrit pour le « banc de la règle seul ») ; (b) un **module neuf à noms neufs, égal à la v4** (E-5 et R5-7 de la conception v7).
**Cette pièce retient (b)**, pour quatre raisons : (i) le mot de Lazar qui commande ce banc dit « le code v68 **de la course**
contre-lu » (GO-2026-11-17-05) ; (ii) la conception v7, qui fait foi, exige pour le code qui décide des noms neufs sans
remplacement à l'exécution (E-5) ; (iii) le brouillon 6 suit la conception (V-1) ; (iv) la lecture (a) servait l'option
Q-B2 (a), que Lazar n'a pas retenue. Conséquences :

- le banc tourne sur le **code de la course gelé** (points V-1 à V-36 du brouillon 6, contre-lus nommément, bloc gelé des
  empreintes) ; `monde_riche_v4.py` (`4b165847…`) n'y est pas importé : il est la **référence** de l'essai R5-7 (égalité, sur les
  12 graines de développement `cle("monde-mr1-v4-calibration-developpement", r)`, des devis à l'octet, de la suite des refus, des
  étiquettes C8 et du champ `resultat` d'une génération simulée par le port de `course`) ;
- un échec de R5-7 est un **nœud** (p_c ne se transporte que sur la même famille) ;
- les lignes du devis v3 qui disent l'import (lignes 34, 68, 150 et 188) sont remplacées par le devis v4 du banc.

## 3. Le code qui joue au banc, rôle par rôle

| rôle | code (course gelée ; points du brouillon 6) | précision |
|---|---|---|
| tirage et vérification des mondes | générateur et vérificateur MR-2 à noms neufs (V-1 à V-5, V-7, V-9) | égaux à `generer_v4` et `verifier_v4` (R5-7) ; contrôles C0 à C8 v4, toute conditionnelle certifiée, borne de 10 composantes contrôlée ; **C8 garde le juge interne du vérificateur** (200 graines, 400 tirages, m = 48) : il définit « certifiée », il n'est pas le juge du banc ; C7 joué avec les pièces servies gelées (mesure M3) |
| oracle | V-27 | 12 000 instances par monde ; information I_i, attribution Δ_i, gains au sens v60 et de l'enveloppe, sentinelles, ajustement « tempéré et incliné » au maximum de vraisemblance attendue |
| jeu planté | V-24 | V-monde, V-K1+i, V-diluée-0,03 et -0,05, F1 à F5, copies, H1, T-ELIM, T-MAL ; jamais regroupé, retenu ni servi |
| gardien | V-13 | appliqué aussi aux cartes synthétiques ; une carte refusée n'est pas jugée et est comptée |
| regroupement | V-21 (`grouper`) | jeu public de **2 000** instances par génération, 192 strates, ε = 0,01, ε_strat = 0,04, liaison complète (la simulation de la conception v4 regroupait sur 1 500 instances : la course et le banc suivent le texte, 2 000) |
| juge | V-23 (`juger_carte`) | **juge de la course** : nul v8 de l'archive, pari apparié, n tirages frais par la valeur de l'étape, huit instants de lecture réguliers, valeur e arrêtée au premier instant de lecture où la richesse atteint le seuil de la forme (hypothèse (b) de la preuve, annexe A) |
| valeur e de groupe, e-BH | V-23 | trois formes (section 7.4) ; e-BH sur les groupes à **m = 48** |
| représentant | V-22 | couverture dirigée minimale ; à couverture mutuelle (écart ≤ 10⁻³), tranche de choix de **2 000** épisodes, une par groupe, la même pour tous les candidats ; puis l'empreinte canonique ; formes canoniques égales : le premier par rang de carte |
| test de mort | **simulé** | statistique gelée du tour fermé (gain moyen de log-score sur la marginale empirique, comptes + 0,5) calculée **par le lanceur** sur une tranche de 400 épisodes, seuil 0,02 nat (T-ELIM : 2,0) ; aucun expérimentateur, aucun bac, aucun vérificateur |
| lanceur du banc | V-12 (nom neuf) | ordre D-2, passes, mesures, manifeste par run (R9), sorties sans monde |

**Pourquoi le juge de la course, et non le « juge simplifié »** : le brouillon 6 écrit que « tout chiffre de puissance du juge réel
vient du juge simplifié de la conception […] : il indique, il ne gèle rien. Les chiffres qui gèlent viennent du banc complet avec
le code de la course gelé ». n, la forme et τ gelés par le banc doivent valoir pour le juge qui jugera les cartes de la course.
La conception v7 §3.2 et le brouillon 6 (« Seuil », règle 6) écrivent « juge simplifié contre le nul v8 » pour la génération 1
simulée de la règle de garde : écart de lettre, nœud au sens du brouillon 6, section 12 (à P_CACHÉE = 0, la règle n'en dépend
presque pas).

## 4. Mondes, secret, graines, ordre des engagements

### 4.1 Mondes de calibration

- **N = 24**, rangs r = 0 à 23, **fixé** (Q-15 (b), R-2501) ; secret de calibration **neuf**, distinct du secret du pilote (ses
  quatre mondes ne sont jamais réutilisés) et du secret de test de la course.
- **Graine du monde r** (forme de `graine_monde_pilote`, `mesure_pilote_v4.py`, `676d5f37…`, lignes 253 à 269, **étiquette
  neuve**) : G_r = 2⁶⁴ + entier des 8 premiers octets (gros-boutiste) de sha256(`b"banc-calibration-mr2-v1"` ∥ 0x00 ∥ secret
  (32 octets) ∥ 0x00 ∥ phrase de Lazar en UTF-8 (non vide, sans octet nul) ∥ 0x00 ∥ empreinte de la **version finale scellée de
  cette pièce** (32 octets) ∥ 0x00 ∥ r (1 octet)).
- **Tirages** : au plus **8**, sous-graines `SeedSequence(G_r, spawn_key=(k,))`, k = 0 à 7 (forme de `generer_v4`) ; chaque tirage
  vérifié C0 à C8 v4 ; le premier tirage conforme est le monde r. **Aucun tirage conforme en 8** : le monde est tiré, compté au
  dénominateur, **g_r = 0** (Q-B3 (a)), refus rapportés avec leurs motifs, **sans arrêt**.
- Le secret de calibration et les mondes **ne vivent que sur la machine** et meurent avec elle (Q-B1 (a)) ; seules leurs
  empreintes vont au registre ; aucun monde n'est poussé, publié ni réutilisé. **Conséquence dite** : les mondes de calibration
  ne sont pas regénérables après le banc ; la vérification ultérieure repose sur les empreintes et les sorties rapatriées.

### 4.2 Flux aléatoires du banc (R9)

- **Racine publique des flux du monde r** : F_r = 2⁶⁴ + entier des 8 premiers octets (gros-boutiste) de
  sha256(`b"banc-calibration-mr2-v1|flux"` ∥ 0x00 ∥ empreinte de la version finale scellée de cette pièce ∥ 0x00 ∥ r (1 octet)).
  Elle est fixée avant le secret ; elle ne dépend d'aucun monde (même structure que la course, dont les flux viennent du texte
  scellé et les mondes du secret).
- Chaque tâche tire de `SeedSequence(F_r, spawn_key=(clé du flux, indices…))`, la clé du flux étant l'entier des 4 premiers
  octets de sha256 de son nom ; noms et indices :

| flux | indices | usage |
|---|---|---|
| `oracle` | — | 12 000 instances de l'oracle du monde |
| `reference-regroupement` | génération g | jeu public de 2 000 instances du regroupement |
| `proposition` | g | cartes synthétiques de la génération (une uniforme par composante et par carte, tirée quelle que soit sa probabilité) |
| `juge` | g, rang de carte | tirages frais du juge |
| `mort` | g, rang de carte | tranche de 400 épisodes du test de mort simulé |
| `choix` | g, empreintes canoniques triées des membres | tranche de choix de 2 000 épisodes du groupe |
| `f` | — | lois synthétiques de la règle de f |
| `n` | δ (0 ou 1), n, graine 0 à 199 | jugements de la règle de n |
| `forme` | taille, copie, graine | jugements de la règle de forme |
| `mesures` | nom de la mesure, indices | mesures hors D-2 |

- **Les flux ne dépendent ni de la passe (P_CACHÉE, drapeau de masquage), ni de n, ni de la forme** (R5-8, étendu aux graines du
  juge et du test de mort comme le demande la remarque du tour 3 de la contre-lecture de la conception) : deux simulations aux
  mêmes valeurs rendent les mêmes cartes et les mêmes jugements (égalités de contrôle, sections 7.5 et 7.6) ; deux passes ne
  diffèrent que par le seuil appliqué à la même uniforme et par ce qui en découle.
- Forme exacte des clés et des concaténations : écrite par le code et recopiée au manifeste (marqueur [GRAINES-BANC], levé par le
  code) ; essai R5 T-3.

### 4.3 Ordre des engagements (chaque pas inscrit au registre avec son heure `date -u`)

1. Cette pièce, contre-lue, corrigée, points ouverts tranchés, **version finale scellée** ; code de la course et du banc écrit,
   essayé, contre-lu (les quatre points [GO] nommés), **gelé** ; bloc gelé des empreintes ; le bloc du banc porte l'empreinte de
   cette pièce finale, le modèle de proposeurs (P_CACHÉE = 0, P_VUE = 0,25, liste des passes), les grilles, δ et δ_bas.
2. Ces pièces **versées, committées et poussées sur le dépôt de travail privé** (jamais sur le dépôt public de l'organisme, V-36) ;
   heure du dépôt distant.
3. Machine jetable louée (devis v4) ; sur elle, **secret de calibration** de 32 octets tiré (`secrets.token_bytes`), écrit en mode
   0600, jamais écrasé (un second tirage sur la machine est refusé) ; **empreinte** du secret (jamais sa valeur) inscrite au
   registre, committée et poussée.
4. **Seulement ensuite**, la **phrase de Lazar**, tapée par lui dans la session qui lance ; son empreinte inscrite, committée,
   poussée.
5. **Contrôle des commits par le lanceur, hors de la machine** (la machine ne porte aucun jeton du dépôt) : empreintes de la pièce,
   du code et du modèle dans un commit poussé **antérieur** à celui du secret, empreinte du secret dans un commit **antérieur** à
   celui de la phrase (garde 35 du brouillon 6, forme du banc). Sinon : refus de tirer les mondes.
6. Tirage et vérification des 24 mondes ; **empreintes des mondes inscrites au registre** (barrière) avant toute étape.
7. Étapes 1 à 6 de D-2, dans l'ordre (section 7) ; chaque valeur retenue écrite et scellée avant l'étape suivante ; la passe
   P_CACHÉE = 0 de l'étape 6 écrite et scellée avant les passes rapportées.
8. Mesures hors D-2 (section 8).
9. Rapatriement (pièces permises seulement, aucun fichier qui porte un monde), empreintes relues sur la copie ; destruction de la
   machine par son identifiant (R10) ; absence prouvée.

## 5. Modèle de proposeurs synthétiques (gelé) et génération simulée

### 5.1 Modèle (celui de la v3b, porté par `course` de `monde_riche_v4.py`, lignes 214 à 230)

- 4 proposeurs × 6 cartes par génération, dans l'ordre proposeur puis carte (rang de carte 0 à 23).
- Pour chaque carte : S = chaque composante **connue** gardée avec la probabilité **0,9** ; chaque composante inconnue ajoutée
  avec la probabilité de sa classe : **forte 0,5, moyenne 0,25, latente 0,25, faible 0,1** ; une **conditionnelle** inconnue est
  ajoutée avec **P_VUE = 0,25** (supposée, non mesurée) si sa composante de condition est connue, avec **P_CACHÉE** sinon ; S vide :
  S = {effet de K1}. La carte est le monde réduit à S, coefficients multipliés par exp(N(0 ; 0,15)) et biais bruités (σ = 0,15,
  `_bruiter`).
- **Connues** : l'effet de K1 au départ, puis la réunion des ensembles S des cartes **retenues** des générations antérieures (les
  ensembles de construction, non l'attribution, comme en v4). En génération 1, aucune conditionnelle n'a sa condition connue
  (K1 est une forte ; la seconde conditionnelle d'une chaîne a pour condition la première).
- **Valeur qui décide** : **P_CACHÉE = 0** (p_c ponctuel du pilote, x = 0 sur 14 appels ; champ `regle` du verdict v2 :
  `P_CACHEE_banc = 0,0`). Les passes rapportées changent la seule P_CACHÉE (section 7.6). Ce modèle est **arbitraire** pour ses
  probabilités par classe et pour P_VUE (conception v7 §7, réserves).

### 5.2 Une génération simulée g (ordre des pas)

Archive de départ A₁ = {K1} (K1 : la meilleure loi softmax du seul trait de l'effet principal le plus fort, ajustée par
l'oracle). Pour g = 1, 2, … :
(1) 24 cartes du modèle ; (2) gardien ; (3) regroupement des cartes admises ; (4) chaque carte admise jugée contre le nul v8 de
A_g, à la valeur de n de l'étape ; (5) valeur e de chaque groupe à la forme de l'étape ; (6) e-BH sur les groupes, m = 48 ;
(7) représentant de chaque groupe promu ; (8) test de mort simulé de chaque représentant ; (9) **retenues** = représentants
survivants, dans l'ordre croissant du rang de carte ; (10) A_{g+1} = A_g ∪ retenues ; connues ∪= ensembles S des retenues ;
**captées** ∪= composantes que couvre une retenue (attribution à f, section 6). Les captées de départ sont celles que couvre K1.
Les lois plantées ne sont jugées que là où une mesure le demande (M7) ; elles n'entrent jamais dans un groupe ni dans une archive.

## 6. Définitions communes

- **Composante** : un effet du monde ; après l'étape 2, une **composante fusionnée** est une classe de la fusion (section 7.2) ;
  la latente n'est jamais fusionnée et reste à part.
- **Ordre des classes** (fixé ici, proposition B4-14 du brouillon 6 retenue) : **faible < conditionnelle < moyenne < forte** ; la
  conditionnelle, de la taille d'une moyenne, est rangée sous elle parce qu'elle est invisible dans la marginale de son trait.
- **Étiquette C8** d'une composante : celle du vérificateur (« certifiée détectable quand le reste du monde est connu » si la borne
  basse de Wilson à 95 % de la puissance est ≥ 0,8 ; « indétectable » si la borne haute est < 0,1 ; « proche du seuil » sinon) ;
  d'une fusionnée : la **moins favorable** de ses membres (indétectable, puis proche du seuil, puis certifiée) ; d'où : une
  fusionnée est certifiée si et seulement si tous ses membres le sont.
- **Couvre** : une loi couvre l'effet i si Δ_i ≥ max(0,005 ; f·I_i) (oracle, f de l'étape 1 ; avant l'étape 1, f n'est pas
  utilisé). Une loi couvre une fusionnée si elle couvre **l'un au moins** de ses membres ; une archive A couvre ce que couvre
  l'une au moins de ses lois. **Captée** : couverte par K1 ou par une retenue.
- **Promotion d'une loi seule** (sentinelles, copies de la règle de forme, lois plantées) : valeur e arrêtée au seuil m/α,
  promue si son logarithme est ≥ log(m/α) = log 960 ≈ 6,867 (m = 48, α = 0,05) ; c'est le seuil de rang 1 d'e-BH, celui
  qu'affronte un groupe porteur seul.
- **Sentinelle** (brouillon 6, « Seuil ») : S_i(A) = le monde réduit aux effets que A couvre (effets bruts) et aux membres de la
  composante i, tempéré et incliné au maximum de vraisemblance attendue ; **S_i diluée à δ** = λ·S_i(A) + (1 − λ)·A*, A* la
  meilleure loi seule de A (gain de l'oracle), λ ∈ [0 ; 1] trouvé par bissection (40 pas) pour un gain au-delà de l'enveloppe de
  A égal à δ ; défini seulement si S_i(A) non diluée gagne au moins δ au-delà de l'enveloppe de A.
- **Médiane** : au sens usuel (moyenne des deux valeurs centrales si le nombre de mondes est pair). **Wilson** : à 95 %,
  z = 1,959964. **Part** : nombre de promotions sur 200 graines, sauf mention.
- **Monde exclu** : un monde sans tirage conforme n'entre dans **aucune** médiane ni dans τ ; il n'entre que dans le dénominateur
  de la règle de garde (g_r = 0) ; il est compté à part pour chaque étape.
- **Sorties** : comptes, classes et sortes, étiquettes et puissances C8, parts, valeurs retenues, empreintes ; **jamais** un
  coefficient, un indice de trait, un seuil, une pente, un biais, un lien de condition ni une loi (règle C-2 du pilote).

## 7. Ordre D-2 : les six règles (chaque règle se sert des valeurs fixées avant elle ; aucune n'est rejouée après une suivante)

### 7.1 Étape 1 — f (attribution)

- **Objet** : le facteur f du critère d'attribution Δ_i ≥ max(0,005 ; f·I_i).
- **Lois** : par monde conforme, **12 lois synthétiques** au dessin de `attribution_v2b.py` (`dee69027…`, par
  `_attribution_monde`) : S = sous-ensemble tiré des effets du monde (taille 1 à 5, sans remise), loi = `_bruiter(spec, S, 0,15)`.
- **Mesure** : pour f ∈ {0,5 ; 0,6 ; 0,75 ; 0,9}, une loi est **exacte** si l'ensemble des effets qu'elle couvre, latente exclue,
  égale S, latente exclue ; part des lois exactes **sur toutes les lois des mondes conformes** (au plus 288).
- **Décision** : f = l'élément de plus grande part ; si la part à 0,75 est à 0,01 près de la plus grande : **0,75** ; égalité
  exacte entre deux autres valeurs : la plus proche de 0,75, puis la plus petite. Valeur retenue : [BANC-f].
- **Rapporté** : part et Wilson par f ; vrais positifs, faux négatifs, faux positifs par classe.

### 7.2 Étape 2 — fusion des composantes non séparables

- **Règle** (à f retenu) : pour deux effets i ≠ j, **tous deux autres que l'effet de K1 et que la latente**, i et j sont
  fusionnés si l'attribution de V-K1+i couvre j, ou celle de V-K1+j couvre i ; **fermeture par transitivité**. (Sans l'exclusion de
  l'effet de K1, toute composante fusionnerait avec lui, V-K1+i le contenant : trou du brouillon 6, fermé ici.)
- **Fusionnée** : étiquette C8 la moins favorable ; **classe la plus faible** dans l'ordre faible < conditionnelle < moyenne <
  forte ; pour G_cond, elle compte comme conditionnelle si l'un de ses membres en est une ; identifiant : le plus petit identifiant
  de ses membres (ordre numérique : E2 avant E10).
- Calculée par le vérificateur sur chaque monde conforme, écrite à son rapport privé, appliquée à l'identique par l'oracle (et, dans
  la course, aux mondes de test).
- **Rapporté** : nombre de mondes à fusion, tailles et classes des fusionnées, étiquettes ; aucun lien de condition.

### 7.3 Étape 3 — n, tirages frais par carte (règle de Q-5 (c))

1. **Simulation de l'archive** (trou du brouillon 6 fermé ici) : par monde conforme, générations 1 et 2 simulées à **n = 400 et
   forme « moyenne »** (valeurs de la conception, **provisoires**, fixées ici avant le banc), P_CACHÉE = 0, P_VUE = 0,25, f et
   fusion retenus ; mêmes flux que toute simulation à P_CACHÉE = 0.
2. **Archive de 8 lois A₈** = {K1} ∪ les **7 premières** lois de la liste « retenues de la génération 2 dans l'ordre croissant du
   rang de carte, puis retenues de la génération 1 dans le même ordre » ; **sans W₋ᵢ** (aucune loi de l'oracle n'y est ajoutée).
   Moins de 7 retenues sur les deux générations : **monde exclu de la médiane**, compté (motif « archive incomplète »).
3. **Composante i** : la première composante (fusionnée) **de classe faible**, dans l'ordre numérique des identifiants, **non
   couverte par A₈**, dont la sentinelle non diluée gagne au moins δ = 0,0275 nat au-delà de l'enveloppe de A₈. Aucune : monde
   exclu, compté (motif « aucune faible éligible »). La certification n'est pas exigée (une faible est le plus souvent « proche du
   seuil »).
4. **Lois jugées** : S_i diluée à **δ = 0,0275 nat** (milieu de 0,025-0,03) ; et, pour le point (ii) de la règle, S_i diluée à
   **δ_bas = 0,005 nat** (trou du brouillon 6 fermé ici : « lois à moins de 0,01 nat au-delà de l'enveloppe » devient la même
   sentinelle diluée au milieu de [0 ; 0,01[ ; choix du rédacteur de la pièce, à contre-lire).
5. **Mesure** : pour chaque n de la grille {200, 300, 400, 600, 800} et chaque monde éligible, 200 graines ; à chaque graine,
   S_i^δ jugée contre A₈ à n tirages (part p_r(n)) et S_i^δ_bas jugée de même (part q_r(n)) ; promotion d'une loi seule.
6. **Décision** : M(n) = médiane des p_r(n) ; Q(n) = médiane des q_r(n), sur les mondes éligibles ; **n = le plus petit n de la
   grille tel que M(n) ≥ 0,5 et Q(n) ≤ 0,25** ; si aucun n ne tient les deux : **n = 400**, rapporté ; **moins de 8 mondes
   éligibles** (8 : sans pièce, dit) : **n = 400 par repli**, rapporté. Valeur retenue : [BANC-n].
7. **Rapporté** : M(n), Q(n), parts mises en commun avec Wilson, mondes exclus par motif, nombre de retenues des générations 1
   et 2.

### 7.4 Étape 4 — forme de la valeur e de groupe (à n retenu)

1. **Objet** : sur les mondes éligibles de l'étape 3, même A₈, même i, même S_i^δ, un **groupe de 3 copies exactes** de S_i^δ
   (doublons au sens de la forme canonique ; k = 3), **seul groupe porteur** de la génération simulée (il affronte le seuil de
   rang 1, m/α = 960) ; chaque copie jugée sur ses **propres** tirages, 200 graines.
2. **Trois formes**, calculées à chaque graine sur les mêmes trajectoires :
   - **F1, moyenne** : moyenne des valeurs e des 3 copies, chacune arrêtée au seuil m/α ;
   - **F2, représentant seul** : valeur e du représentant (formes canoniques égales : la première copie par rang), arrêtée au
     seuil m/α ;
   - **F3, arrêt ajusté à la taille du groupe** (définition fixée ici) : moyenne des valeurs e des k copies, **chacune arrêtée au
     premier instant de lecture où sa richesse atteint k·m/α** (k = 3 : 2 880), sinon au dernier instant ; k est connu avant les
     tirages.
   Le groupe est promu si sa valeur e est ≥ m/α.
3. **Éligibilité** (D-3) : seules les formes dont la preuve de validité (annexe A) est jugée valide par la contre-lecture de cette
   pièce, et dont l'hypothèse (b) est vérifiée sur le code par sa contre-lecture, sont éligibles.
4. **Décision** : est gelée la forme éligible de **plus grande part médiane** sur les mondes éligibles ; si F1 est éligible et que
   sa part médiane est à **moins de 0,02** de la meilleure : **F1** ; égalité exacte entre F2 et F3 : **F2**. Moins de 8 mondes
   éligibles : **F1 par repli** (forme par défaut du brouillon 3, §3.6 point 3), rapporté. Valeur retenue : [BANC-FORME].
5. **Rapporté** : parts médianes et mises en commun des trois formes ; groupes de **2** et de **6** copies (copies 1 et 2, 1 à 6 ;
   mêmes tirages pour les copies communes ; k = 2 ou 6 dans F3), sans effet sur le choix.

### 7.5 Étape 5 — tolérance τ des fausses découvertes (Q-9 (a), refaite sur MR-2, E-9 (iii))

1. **Simulation** : par monde conforme, **trois générations** simulées à n, forme, f et fusion retenus, **P_CACHÉE = 0, P_VUE =
   0,25** (passe qui décide ; la conception ne fixe pas la passe de τ : choix du brouillon 6, repris).
2. **Fausse découverte** : retenue de la génération g qui n'est pas une **vraie découverte** ; vraie découverte : gain au-delà de A_g
   au sens v60 (moins le gain de la meilleure loi seule de A_g) **et** gain au-delà de l'enveloppe de A_g, tous deux **≥ g₀ =
   0,02 nat** (même définition que la ligne FD de la course).
3. **Décision** : τ = Σ fausses découvertes / Σ retenues, sur les trois générations des mondes conformes (**part d'ensemble**) ;
   **aucune marge** (la ligne FD se lit sur la borne basse de Wilson du monde). **Sous-choix « part d'ensemble » contre « sa borne
   haute de Wilson » : nœud de Lazar, à trancher avant le banc** (section 12) ; la borne haute est calculée et rapportée sous
   toute décision. Aucune retenue sur tous les mondes : τ « non mesurable », écrit ; la ligne FD de la course n'a alors pas de τ
   (nœud). Valeur retenue : [BANC-τ].
4. **Rapporté** : τ et sa borne de Wilson ; fausses découvertes et retenues par génération et par monde ; découvertes réelles sous
   le seuil (gain au-delà de l'enveloppe > 0) ; recombinaisons ; **minimums** de fausses découvertes qui déclenchent la ligne FD
   (borne basse de Wilson > τ) pour 3, 5, 8, 10, 15, 20 et 30 retenues, à τ retenu.
5. **Égalité de contrôle** : si n retenu = 400 et forme retenue = F1, les générations 1 et 2 de cette étape égalent, carte pour
   carte et jugement pour jugement, celles de l'étape 3 (mêmes flux, mêmes valeurs) ; un écart arrête le banc (garde B-13).

### 7.6 Étape 6 — règle de garde, en dernier (conception v7 §3.2 ; brouillon 6, « Seuil », règle 6 ; GO-2026-11-17-05)

- **Texte de Lazar** (R-2492, recopié) : « Pas de course si moins de la moitié des mondes de calibration gardent une composante
  certifiée encore trouvable après une génération 1 simulée. »
- **Génération 1 simulée** (section 5.2, g = 1) : archive {K1}, à **n, forme, f et fusion retenus** ; chaîne de la course ; modèle
  gelé.
- **Indicatrice** g_r : **0** si aucun tirage conforme en 8 ; sinon **1** si et seulement si l'ensemble E_r des composantes
  (fusionnées) **certifiées**, latente exclue, **non captées** au sortir de la génération 1 est non vide.
- **Compte** : **G = Σ_r g_r sur les 24 mondes tirés** ; **G_cond** : même compte, restreint aux mondes où E_r contient une
  composante qui compte comme conditionnelle.
- **Règle** : **tenue si et seulement si 2·G ≥ 24**, soit G ≥ 12 ; comparaison d'entiers. Seuil « au moins la moitié » : **de
  Lazar, sans pièce**.
- **Passe qui décide, jouée la première** : P_CACHÉE = **0** ; G, G_cond et « tenue » ou « non tenue » écrits et scellés **avant
  toute autre passe**. **Égalité de contrôle** : sa génération 1 égale celle de l'étape 5 (mêmes flux, mêmes valeurs) ; un écart
  arrête le banc (B-13).
- **Passes rapportées, qui ne décident pas** (mêmes 24 mondes, mêmes flux, dans cet ordre) : **borne haute de l'intervalle du
  pilote**, puis **0,01 ; 0,02 ; 0,03 ; 0,04 ; 0,05 ; 0,25 (sans masquage)** ; la borne basse égale le ponctuel (0) : pas de passe
  de plus. La borne haute **se lit au champ de la sortie de mesure scellée du pilote** (`sortie-mesure-pilote-v70.json`,
  `b206639e77c78b095c6999c89eebaa3e26726b474b81ef4021007bd6e0a36bb9`, empreinte relevée par le verdict v2), par le lanceur, qui
  contrôle l'empreinte ; nom du champ : marqueur [CHAMP-BORNE-HAUTE], levé par qui a le droit de lire cette sortie (recalcul
  pour mémoire : 1 − 0,025^(1/84) = 0,042965 ; jamais cet arrondi à la place du champ). Champ absent ou empreinte autre : passe
  « non jouée », écrite en tête, **sans arrêt** (elle ne décide pas).
- **Pour chaque passe** : G, G_cond, borne de Wilson de G/24, « tenue » ou « non tenue » **à titre d'information** ; nombre de
  cartes de la génération 1 qui portent une conditionnelle ; classes des composantes restantes ; mondes sans tirage conforme ;
  refus par contrôle et motifs.
- **Ce qui suit un échec** : **pas de course** ; aucune nouvelle famille, aucun nouveau tirage de mondes de calibration, aucun
  réglage du modèle de proposeurs sur ces mêmes mondes ; une famille revue passe par un texte neuf et le mot de Lazar. **Un succès ne
  prouve rien sur le progrès** : il dit que la course **peut** y répondre, sous le modèle.

### 7.7 Règle de changement (brouillon 3 §16.1 point 5, incorporé par renvoi au brouillon 6)

Toute valeur autre que celles que rendent les règles 1 à 6, et tout changement d'un seuil fixé hors du banc (ε, ε_strat,
192 strates, 2 000 instances, plancher 0,005, bornes C8 0,8 et 0,1, g₀, α, m, δ, δ_bas, grilles), **est un changement** : il est
écrit, et un **nouveau secret de calibration** tire de nouveaux mondes pour le confirmer ; chaque cycle est rapporté ; au-delà de 3
cycles, arrêt et proposition à Lazar. **Sous GO-2026-11-17-05 (« un seul banc complet »), un second cycle est une dépense et un banc
de plus : nœud, mot de Lazar exigé avant lui.** Une mesure hors D-2 ne commande aucun changement : elle s'écrit.

## 8. Mesures hors D-2 et valeurs [BANC] (jouées après l'étape 6 ; rapportées ; ne décident rien)

Elles se jouent **après** la règle (dont la passe qui décide est déjà scellée) : ainsi la règle reste la dernière étape de D-2 et
aucune mesure ne peut retarder ni empêcher son calcul ; le lecteur lit la règle en dernier (section 10). Chacune a sa loi, son
archive, ses graines et sa lecture ; celles que la pièce ne définit pas sont retirées du texte de la course (brouillon 6,
« Préalables », point 8).

| # | mesure | loi(s) et archive(s) | graines, n | lecture (sans décision) |
|---|---|---|---|---|
| **M1** | **surdité** (D.1 « Portée de C8 » ; L.2 PL-sourd ; A6) | pour chaque archive A ∈ {**A₃** : archive au début de la génération 3 de l'étape 5 ; **A₈** de l'étape 3} et chaque composante (fusionnée) **certifiée**, latente exclue, **non couverte par A** : S_i(A) non diluée jugée contre A (p_i(A)) ; **référence** : la même construction avec l'archive {W₋ᵢ} (W₋ᵢ : le monde sans les membres de i), S_i({W₋ᵢ}) jugée contre {W₋ᵢ} (p_i(W)) ; et la puissance C8 de i | 200 graines ; n retenu | p_i(A), p_i(W), écart ; couple (i, A) « **sourd** » si p_i(A) < 0,5 ≤ p_i(W) ; comptes par classe et par archive ; c'est la mesure à laquelle la course compare PL-sourd |
| **M2** | **tranche de choix de 2 000 épisodes contre 400** (D.8 point 7) | groupes des trois générations de l'étape 5 dont le représentant s'est départagé par la tranche ; représentant recalculé sur les **400 premiers** épisodes de la même tranche | — | perte = gain de l'oracle du meilleur membre moins celui du choisi, pour 2 000 et 400 ; groupes à perte > 0,01 nat ; choisis sous g₀ alors que le meilleur est au-dessus |
| **M3** | **C7 sur les pièces gelées** | au tirage (C0 à C8), le vérificateur reçoit les **pièces servies gelées** de la course (gabarit `e77d3041…`, consignes de l'expérimentateur et du vérificateur, grammaire ; empreintes au bloc gelé) | — | touches à deux décimales par monde ; une égalité à six décimales est un **refus du tirage** (règle du vérificateur v2, inchangée), compté parmi les refus avec son motif ; pièces non gelées avant le secret : C7 joué sur les seules pièces gelées, la liste des autres écrite |
| **M4** | **doublons sur paires difficiles** (brouillon 3 §16.1 point 5) | par monde conforme, paires construites sur le monde (donc disjointes des 12 mondes de développement), aux dix catégories de `doublons-w12-v2` (base = fortes et première moyenne ; variantes σ = 0,05, 0,1, 0,2, 0,3 ; reformulation ; tempérée 1,2 ; mêlée 0,8 à l'uniforme : à regrouper ; distincte-moyenne, ajout-faible, ajout-moyenne : à ne pas regrouper) et une catégorie neuve **ajout-conditionnelle** (base et première conditionnelle : à ne pas regrouper) ; `grouper` de la course | 2 000 instances | part juste par catégorie (Wilson sur les mondes) ; catégorie sans objet si le monde n'a pas les composantes voulues ; une part juste < 0,8 s'écrit en tête ; ε et ε_strat inchangés (règle de changement) |
| **M5** | **fréquences des sortes déformées par les rejets** (D.1 « Régularités ») | (a) classe × sorte des 24 mondes conformes, et de tous les tirages, refusés compris ; (b) 10 000 gabarits tirés par la fonction gelée sans les contraintes v4 et avec elles, sur une graine publique (`cle("frequences-sortes-banc-mr2-v1")`), sans aucun coefficient | — | tables (a) et (b) ; déclarées avec le générateur (Q-10 (a)) |
| **M6** | **coût de d_nul à 48 feuilles** (D.8 point 4, V-21) | durée murale de chaque regroupement des générations simulées (étapes 3, 5, 6) et nombre de feuilles des cartes | — | médiane et maximum ; coût projeté pour la course |
| **M7** | **valeurs [BANC] des prédictions** (brouillon 6, P1 à P5, P8, P9) | (P1 à P5) pour chaque génération g de l'étape 5, le jeu planté de g (V-24 : V-monde, V-K1+i, V-diluées, F1 à F4, et pour g ≥ 2 F5 et les copies des quatre premières retenues de g − 1, H1, T-ELIM ; T-MAL au gardien) jugé **40 fois** contre A_g (40 répétitions du jeu entier, flux par (g, répétition)) ; vraies promues testées (test simulé ; T-ELIM au seuil 2,0) ; « vraie du critère » : gain au-delà de A_g (v60 et enveloppe) ≥ g₀ ; (P8) perte au regroupement dans l'étape 5 : composantes certifiées couvertes par au moins une carte et par aucun représentant, par génération ; (P9) τ de l'étape 5 | 40 répétitions ; n retenu | parts par type et par classe (forte, moyenne, **conditionnelle**, faible) avec Wilson ; fausses couvertes promues ; part des répétitions où une vraie du critère est promue puis survit en génération 1 ; recopiées aux marqueurs [BANC] du texte candidat de la course |

Mesures du brouillon 3 et de la conception v3 que le brouillon 6 ne cite pas (étalonnage du juge simplifié, mondes témoins) : **non
reprises** ; M7 tient lieu de détection par classe avec le juge de la course.

## 9. Prédictions chiffrées, écrites d'avance (R1 ; aucun signe n'est visé, R3)

La prédiction qui décide d'une dépense est **P0** ; les autres étapes fixent des seuils par règle : leurs valeurs indicatives ne sont
pas des hypothèses éprouvées, et une valeur loin de l'indication déclenche l'audit (section 10), non un changement.

| étape | prédiction | pièce |
|---|---|---|
| **P0, règle (passe qui décide)** | part attendue des mondes gardants 0,996 ; **règle tenue avec la probabilité au-dessus de 0,9999** ; **G = 24 le plus probable** (0,91 à ρ = 0,5) ; au moins un monde sans tirage conforme : 0,09 (ρ = 0,5) à 0,33 (ρ = 0,6) | conception v7 §3.4 ; `sorties-v5/calcul-regle-v5.json` (`10ff446d…`) ; recalcul : 1 − (1 − 0,5⁸)²⁴ = 0,0897 et 1 − (1 − 0,6⁸)²⁴ = 0,3340 |
| passes rapportées | 0,01 : tenue 0,9995 à 0,9999 ; 0,02 : 0,91 à 0,96 ; 0,03 : 0,50 à 0,66 ; 0,04 : 0,14 à 0,25 ; **borne haute 0,042965 : 0,09 à 0,17** (G ≈ 8 à 9) ; 0,05 : 0,02 à 0,06 ; sans masquage : 0,0000 (G ≈ 0) | même pièce (modèle réduit ; le banc refait la table avec le code gelé) |
| f | 0,75 le plus probable (règle d'égalité ; 0,74 d'ensembles exacts à 0,75 sur MR-1, `attribution-w12-v2b.json`, `3c4d00c8…`) ; aucune mesure sur MR-2 | conception v3 §5 (brouillon 3) |
| fusion | non chiffrée par les pièces (les refus C6 de la v4 viennent d'effets de sous-population non séparables ; la fusion ne s'applique qu'aux mondes conformes) | conception v7 §4.1 |
| n | 400 le plus probable, 300 ou 600 possibles : sur MR-1, 0,72 de promotions à n = 400 pour un gain de 0,02 à 0,03 contre {K1} (`detection-w12-r40-v2.json`, `6a3d1444…`) ; 0,54 sur les faibles contre {W₋ᵢ} et 7 ou 15 lois partielles (`archive-w8-r30-v2.json`, `a631ad47…`) ; sous 0,01 nat : 0,08 à n = 400, 0,21 à n = 800 (sous-famille v1) : le point (ii) devrait tenir sur toute la grille | conception v3 §1.6 |
| forme | pour des copies de puissance p chacune : F1 ≈ p³, F2 ≈ p, F3 entre les deux selon la part qui atteint 3·m/α ; F2 ou F3 le plus probable ; F1 seulement si p ≥ 0,99 environ | calcul de la forme (annexe A, remarque) |
| τ | 0,15 à 0,20 (v4 : 36 sur 204 = 0,176 ; v3b : 28 sur 181 = 0,155) | conception v7 §4.4 |

Le modèle réduit ignore les cartes porteuses non retenues et les autres certifiées manquées (qui font garder plus) et les captures
par une carte qui ne porte pas la composante (qui font garder moins).

## 10. Lecture du banc : critères écrits d'avance, audit de symétrie, ce qui suit

- **Lecteur** : un sous-agent neuf (R13) qui n'a écrit ni cette pièce, ni le code de la course ou du banc, ni la conception, ni le
  préenregistrement ; il lit les sorties rapatriées dans cet ordre : (1) complétude et gardes (section 11) ; (2) valeurs des
  étapes 1 à 5 et leurs drapeaux de repli ; (3) mesures M1 à M7 ; (4) **la règle en dernier**. Son verdict est scellé, puis
  soumis à Lazar pour GO.
- **Table de lecture** (passe P_CACHÉE = 0, code gelé, 24 mondes tirés ; la première ligne qui s'applique donne l'issue) :

| condition observée | issue | suite |
|---|---|---|
| banc incomplet : nombre de mondes tirés ≠ 24 ; exception ou arrêt dans une étape de D-2 ; empreinte d'un module, du bloc ou de cette pièce ≠ bloc gelé ; étape de D-2 sautée, rejouée ou hors d'ordre ; ordre des engagements en défaut ; égalité de contrôle en défaut | **« banc non jugeable »** | pas de course sous ce banc ; cause écrite ; un banc de plus est un nœud (un seul banc) |
| **2·G < 24** | **« règle non tenue : pas de course »** | aucun appel payant de la course ; audit A0 ; ni nouvelle famille, ni nouveaux mondes de calibration, ni réglage sur ces mondes sans texte neuf et mot de Lazar |
| **2·G ≥ 24** | **« règle tenue : la course peut répondre (sous le modèle) »** | valeurs [BANC-f], [BANC-n], [BANC-FORME], [BANC-τ] et [BANC] recopiées au texte candidat avec chemins et empreintes ; la course reste soumise à toutes les autres conditions de GO-2026-11-13-01 et -02 ; audit A0 **si G = 24** |

- **Écrit en tête, sous toute issue** : G_cond ; nombre de mondes sans tirage conforme ; refus par contrôle et motifs ; classes des
  composantes restantes ; G et règle « à titre d'information » de chaque passe rapportée, **la borne haute du pilote en premier** ;
  les drapeaux de repli des étapes 1 à 5 ; les mesures en échec ; la phrase : « la règle tient presque par construction à
  P_CACHÉE = 0 ; elle ne garde pas contre des proposeurs qui ne masquent pas ; à la borne haute du pilote, elle tient avec la
  probabilité 0,09 à 0,17 sous le modèle réduit ». Une passe rapportée « non tenue » ne change pas l'issue : elle s'écrit et se
  soumet à Lazar avec la demande de GO (information ; Lazar peut révoquer d'un mot, R-2492).
- **Audit de symétrie (R4), écrit d'avance** ; ses constats s'écrivent avant toute phrase de résultat ; il ne change aucune valeur,
  sauf s'il trouve un défaut du code (alors « banc non jugeable ») :
  - **A0, règle** : déclenché à **G = 24** (« trop propre », attendu par construction) **comme** à **G < 12** : relire les refus
    et leurs motifs, les mondes sans tirage conforme, toute composante certifiée captée en génération 1 sans carte qui la porte,
    toute conditionnelle dont la condition serait l'effet de K1 (V-9), l'égalité des flux entre passes (aucune exception : les flux
    sont indépendants de la passe, section 4.2) et les égalités de contrôle.
  - **A-f** : f rendu par la règle d'égalité, ou f ∈ {0,5 ; 0,9} (bord de grille) : relire les parts et dix lois synthétiques au
    hasard.
  - **A-n** : n par repli (moins de 8 mondes éligibles, ou aucun n ne tient), ou n au bord de la grille (200 ou 800) : relire les
    exclusions, M(n) et Q(n).
  - **A-forme** : F1 retenue par la marge de 0,02, ou repli : relire les parts des trois formes.
  - **A-τ** : τ = 0, τ > 0,4, ou τ non mesurable : relire les retenues et la définition appliquée.

## 11. Liste d'arrêt du banc (chaque garde essayée sur un cas sain et un artefact, R5)

| # | garde | cas sain | artefact → action |
|---|---|---|---|
| B-1 | nombre de mondes | 24 mondes tirés, rangs 0 à 23 | 23 ou 25, rang manquant ou doublé → refus de lancer (code 2), ou arrêt, « banc non jugeable » |
| B-2 | empreintes | modules, bloc gelé et cette pièce finale égaux au bloc ; numpy 2.5.3 | une empreinte ou une version autre → refus de lancer (code 2) |
| B-3 | ordre des engagements | pièce, code et modèle poussés avant le secret ; secret avant la phrase ; commits relus hors de la machine | ordre inverse, empreinte absente ou non poussée → refus de tirer les mondes (code 2) |
| B-4 | unicité | un seul lancement, un seul secret sur la machine | second lancement, second secret, secret de calibration réutilisé pour la course → refus |
| B-5 | ordre D-2 | étapes 1 à 6 dans l'ordre, chaque valeur scellée avant la suivante | étape sautée, rejouée, hors d'ordre, valeur retenue réécrite → arrêt, « banc non jugeable » |
| B-6 | exceptions | aucune | exception dans une étape de D-2 → arrêt, « banc non jugeable » ; dans une mesure hors D-2 → mesure « en échec », cause écrite, audit A0 étendu au chemin de code commun ; le banc reste jugeable |
| B-7 | clés | aucune variable de clé de fournisseur de modèles dans l'environnement du lanceur | une variable présente → refus de démarrer (code 2) |
| B-8 | confidentialité des mondes | sorties sans coefficient ni loi (règle C-2) ; rapatriement des seules pièces permises | un fichier qui porte un monde → refus de le copier, rien copié, arrêt du rapatriement, cause écrite |
| B-9 | passe qui décide | P_CACHÉE = 0 jouée et scellée la première | autre passe d'abord → arrêt, « banc non jugeable » |
| B-10 | minuterie | minuterie de destruction armée avant toute passe (devis v4) | minuterie atteinte avant la fin de D-2 → destruction, « banc non jugeable » ; pendant les mesures → mesures restantes « non faites », écrites |
| B-11 | mondes sans tirage conforme | comptés, g_r = 0, sans arrêt | arrêt sur un tel monde → défaut du lanceur (essai T-6) |
| B-12 | borne haute du pilote | champ lu, empreinte contrôlée | champ absent ou empreinte autre → passe « non jouée », écrite, sans arrêt |
| B-13 | égalités de contrôle | générations simulées aux mêmes valeurs égales entre étapes | écart → arrêt, « banc non jugeable » (signe d'un défaut de déterminisme) |
| B-14 | échéance et ligne | ligne « calcul » du banc lue par son identifiant, non échue, avant la location | ligne absente ou échue → refus de louer |

Arrêt = sorties partielles scellées et rapatriées, cause écrite, aucune issue autre que « banc non jugeable ». **Aucun repli
silencieux** (R5).

## 12. Écarts au brouillon 6 et à la conception v7, et points ouverts

**Écarts et choix de la pièce** (nœuds au sens du brouillon 6, « Seuil » : le texte candidat est corrigé pour égaler la pièce, ou
la pièce est refaite ; la conception v7 n'est pas modifiée, elle reste versée) :

| # | point | brouillon 6 ou conception v7 | cette pièce | qui tranche |
|---|---|---|---|---|
| E-1 | lecture de « code v68 gelé » | ouverte (M-1) | module neuf égal à la v4 (section 2) | la mère confirme |
| E-2 | juge du banc | « juge simplifié » pour la génération 1 de la règle (conception v7 §3.2 ; brouillon 6, règle 6) ; « code gelé » pour n et la forme | juge de la course partout ; C8 garde le juge du vérificateur (section 3) | la mère ; option : juge simplifié porté pour la seule règle (sans effet attendu à P_CACHÉE = 0), n, forme et τ restant au juge de la course |
| E-3 | simulation qui forme l'archive de la règle de n | non dite (n et forme pas encore fixés) | générations 1 et 2 à n = 400, forme moyenne, P_CACHÉE = 0 (7.3, point 1) | contre-lecture |
| E-4 | formation des 8 lois | « la pièce écrit comment » | {K1} et 7 retenues (génération 2 puis 1) ; monde exclu sous 7 (7.3, point 2) | contre-lecture |
| E-5 | « lois à moins de 0,01 nat » (point (ii) de n) | non définies | S_i diluée à δ_bas = 0,005 nat, médiane ≤ 0,25 (7.3, point 4) | contre-lecture |
| E-6 | doublons de la règle de forme | « 3 doublons de S_i diluée » | 3 copies exactes, chacune sur ses tirages (7.4) | contre-lecture |
| E-7 | troisième forme | « arrêt ajusté à la taille du groupe » sans définition | chaque membre arrêté à k·m/α, moyenne (7.4) ; preuve en annexe A | contre-lecture (D-3) |
| E-8 | fusion contre l'effet de K1 | non dite | effet de K1 et latente exclus de la fusion (7.2) | contre-lecture |
| E-9 | « captée » d'une fusionnée | non dite | captée si l'un de ses membres l'est (section 6) | contre-lecture |
| E-10 | place des mesures hors D-2 | « règle de garde lue en dernier » | mesures jouées après la règle, lues avant elle (section 8, section 10) | la mère |
| E-11 | exception dans une mesure | « exception » rend le banc non jugeable (L.0) | une exception dans une mesure hors D-2 ne l'annule pas (B-6) | la mère |
| E-12 | flux | « indexés par le rang r » ; graines du juge et du test de mort liées au drapeau dans la v4 | racine publique tirée de l'empreinte de la pièce ; flux indépendants de la passe, de n et de la forme (4.2) | contre-lecture |
| E-13 | gardien sur les cartes synthétiques | absent de la simulation v4 | appliqué, refus comptés (section 3) | contre-lecture |
| E-14 | jeu public du regroupement | 1 500 instances dans la simulation v4 | 2 000, valeur du texte (section 3) | — (le texte prime) |

**Nœuds de Lazar, à trancher avant le banc (aucun défaut sous 48 heures)** :

1. **Sous-choix de τ** : part d'ensemble (brouillon 6, recommandation du brouillon 3, confiance 0,55) ou sa borne haute de
   Wilson ; non nommé par R-2492. Sans son mot, la pièce ne se scelle pas comme finale et le banc ne se lance pas ; s'il retient la
   borne haute, la règle 5 change de mot et la pièce est refaite (v2).
2. **Q-4 (nul v8) et Q-6 (retirage automatique)** : le banc en dépend (juge, tirage des mondes) ; non confirmés par les conditions
   des lignes de GO (brouillon 6, point ouvert 11) ; mot de Lazar ou, à défaut, décision de la mère consignée au registre,
   **avant le banc**.
3. **Second cycle du banc** (règle de changement) : nœud.
4. **Dépense** : la ligne « calcul » suit le devis v4 (`devis-banc-calibration-mr2-v4.md`) ; au-delà de 3 USD au pire, nouveau mot
   de Lazar (GO-2026-11-17-05).

**Points de la mère** : E-1, E-2, E-10, E-11 ci-dessus ; la lettre du rédacteur (A) ; à dire à Lazar en clair avant le banc (point
ouvert 9 du brouillon 6) : la règle tient presque par construction à P_CACHÉE = 0, ne garde pas contre des proposeurs qui ne
masquent pas, tient avec la probabilité 0,09 à 0,17 à la borne haute du pilote, et MR-2 ne satisfait pas la lettre de Q-13 (c)
(E-2 de la contre-lecture v4 : composante invisible dans la marginale, non introuvable).

## 13. Essais exigés du code du banc par cette pièce (R5 : cas sain et artefact ; banc de mutations ; contre-lecture)

| # | essai | cas sain | artefact |
|---|---|---|---|
| T-1 | graine des mondes | 24 graines distinctes, rejouables, égales à la formule (étiquette neuve) sur un secret public | étiquette du pilote, ou empreinte d'une autre pièce → graines différentes détectées |
| T-2 | ordre D-2 et scellement des valeurs | valeurs écrites et scellées dans l'ordre 1 à 6 | étape rejouée ou valeur réécrite → arrêt (B-5) |
| T-3 | flux indépendants de la passe, de n et de la forme | sur les 12 graines de développement, cartes égales entre passes là où les uniformes le permettent ; jugements égaux aux mêmes valeurs | graine rendue dépendante de la passe → écart détecté (R5-8 étendu) |
| T-4 | règle 2·G ≥ N sur les 24 tirés | 12 gardants et 12 non conformes → tenue ; 11 et 13 → non tenue | compte sur les seuls conformes → détecté |
| T-5 | archive A₈ | 7 retenues ou plus → {K1} et 7, ordre écrit | 6 retenues → monde exclu, compté |
| T-6 | monde sans tirage conforme | g_r = 0, sans arrêt, exclu des médianes et de τ | arrêt, ou monde compté dans une médiane → détecté |
| T-7 | composante i de la règle de n | première faible éligible dans l'ordre numérique (E2 avant E10) | ordre alphabétique (E10 avant E2) → détecté |
| T-8 | repli de n et de la forme | moins de 8 mondes éligibles → n = 400, F1, drapeaux écrits | repli silencieux → détecté |
| T-9 | trois formes | sur trajectoires écrites à la main : F1, F2, F3 calculées comme la section 7.4 (seuils 960 et k·960) | F3 arrêtée à m/α → détecté |
| T-10 | fusion | effet de K1 et latente exclus ; transitivité ; étiquette et classe de la fusionnée | fusion avec l'effet de K1 → détectée |
| T-11 | passe qui décide d'abord, borne haute au champ | P_CACHÉE = 0 scellée la première ; champ lu, empreinte contrôlée | autre ordre → arrêt ; champ absent → « non jouée », sans arrêt |
| T-12 | égalités de contrôle | générations égales aux mêmes valeurs | une carte changée → arrêt (B-13) |
| T-13 | confidentialité | sorties sans coefficient, sans lien de condition | clé interdite dans une sortie → refus (règle C-2) |
| T-14 | mesures après la règle | une exception simulée dans M1 → M1 « en échec », règle intacte | exception dans l'étape 3 → « banc non jugeable » |

Plus l'**essai à blanc de bout en bout** du lanceur sur 2 mondes de développement, hors ligne, qui **mesure les durées par monde
et par étape** et la mémoire de pointe ; le devis v4 se relit sur cette mesure avant toute location (garde de durée du devis v4).

## Annexe A — Preuves de validité des trois formes de la valeur e de groupe (D-3 ; à contre-lire avec cette pièce)

**Cadre.** Génération g, archive A_g. Hypothèse nulle commune H₀ : « le monde est dans la classe du nul v8 de A_g ». Chaque carte i
est jugée sur ses propres tirages frais (flux `juge`, indexé par g et le rang de carte) ; sa richesse W_i(t), lue aux huit
instants réguliers t₁ < … < t₈ = n, est le rapport de la vraisemblance de la carte à la plus grande vraisemblance du nul.
**Hypothèses** (brouillon 3 §3.6 point 4, recopiées) : **(a)** sous H₀, W_i est majorée par une martingale positive M_i
d'espérance 1 pour la filtration des tirages de i (la vraisemblance de la carte rapportée à celle du membre du nul qui égale le
monde) — établi pour la classe linéaire du nul v8 seulement ; pour le membre tempéré et incliné, « au second ordre près de
l'optimum, sans preuve » ; **(b)** le code arrête la valeur e au premier instant de lecture où W_i atteint le seuil de la forme,
sinon au dernier instant (à vérifier sur le code, V-23) ; **(c)** H₀ est fausse par construction dans un monde riche : les preuves
bornent le taux de fausses découvertes **au sens de H₀**, non la part des fausses découvertes au sens de l'oracle.

**Lemme 1 (arrêt).** Pour tout seuil c > 0 fixé avant les tirages, soit τ_i(c) le premier instant de lecture où W_i ≥ c (t₈ sinon) :
temps d'arrêt borné. Sous (a), E[W_i(τ_i(c))] ≤ E[M_i(τ_i(c))] = 1 (arrêt optionnel d'une martingale à un temps borné). Donc
E_i(c) = W_i(τ_i(c)) est une valeur e.

**Lemme 2 (groupes indépendants des tirages).** Les groupes sont une fonction des lois des cartes et d'un jeu public d'instances
**sans issue** (flux `reference-regroupement`), fixée avant tout tirage du juge ; la taille k de chaque groupe est donc connue
avant les tirages et indépendante d'eux.

**F1 (moyenne).** Ē_g = (1/k) Σ_{i∈g} E_i(m/α). Par les lemmes 1 et 2, conditionnellement aux groupes, E[Ē_g] ≤ 1 : valeur e.

**F2 (représentant seul).** Le représentant ρ(g) est choisi par la couverture dirigée (lois et instances publiques sans issue),
puis par la tranche de choix (flux `choix`, épisodes distincts des tirages du juge et de la tranche du test de mort), puis par
l'empreinte canonique et le rang : ρ(g) est **indépendant des tirages du juge**. Alors E[E_{ρ(g)}(m/α)] = Σ_r P(ρ(g) = r)·E[E_r(m/α) |
ρ(g) = r] = Σ_r P(ρ(g) = r)·E[E_r(m/α)] ≤ 1 : valeur e. (Condition : l'indépendance des flux `choix` et `juge`, garde 25 et V-22.)

**F3 (arrêt ajusté à la taille).** Ẽ_g = (1/k) Σ_{i∈g} E_i(k·m/α), le seuil k·m/α étant fixé avant les tirages (lemme 2). Par le
lemme 1 à c = k·m/α, chaque terme est d'espérance ≤ 1 ; donc E[Ẽ_g] ≤ 1 : valeur e. Un seul membre qui atteint k·m/α porte à lui
seul le groupe à m/α : c'est ce que la forme vise (coût de la moyenne au bord du seuil, brouillon 6, D.8 point 5).

**e-BH.** Les valeurs e des groupes, sous dépendance quelconque, avec m = 48 fixé avant les tirages et au moins égal au nombre
d'hypothèses jugées par e-BH (au plus 24 groupes ; les plantées sont jugées hors famille à log(m/α)), donnent un taux de fausses
découvertes ≤ α au sens de H₀ (règle e-BH sur des e-valeurs, citée d'après la conception v3 §3.3, non relue ici ; aucun chiffre
n'en est tiré).

**Remarque (prédiction de la section 9, non une preuve).** Pour k copies indépendantes d'une même loi de puissance p (P(E_i(m/α) ≥
m/α) = p) : F2 est promue avec la probabilité p ; F1 seulement si la moyenne atteint m/α, soit, sans dépassement du seuil entre deux
lectures, si toutes les copies l'atteignent (≈ p^k) ; F3 si la somme des valeurs arrêtées à k·m/α atteint k·m/α, au moins dès
qu'une copie atteint k·m/α.

## Déclaration

- **Rôle** : rédacteur neuf de la pièce des règles du banc complet ; sous-agent d'un script d'orchestration de la session mère ;
  aucune autorité de décision. Lettre : **modèle A** (même lignée que les rédacteurs de la conception, du préenregistrement et
  du code du pilote).
- **Pièces écrites par moi dans cette tâche** (scellées, compagnon `.sha256`) : cette pièce ;
  `banc-calibration-mr2-v1/mesure-durees-banc-mr2-v1.py` (scellé avant son passage) et sa sortie ; le programme du calcul du devis
  v4 et sa sortie ; `banc-calibration-mr2-v1/devis-banc-calibration-mr2-v4.md`.
- **Pièces lues** : section « Pièces lues » ci-dessus (empreintes recalculées, égales à leur compagnon) ; branches du pilote
  (`verdict/pilote-mr2-v74-v14-v1`, `prep/pilote-mr2-v1`) récupérées dans un dossier neuf du bloc-notes, à profondeur 1 et sans
  contenus de fichiers (filtre `blob:none`, options du serveur local configurées dans ce seul dossier), fichiers tirés un à un par
  `git show` (≈ 1,2 Mo en tout).
- **Interdits tenus** : aucune machine, aucun appel au loueur ni à un fournisseur de modèles, aucune dépense ; aucune branche
  `calcul/pilote-mr2-v74-entree-*` ; aucun secret, aucun monde de calibration ni de course ; du pilote, seuls le verdict v2 et du
  code (programme de la mesure, rapport du développeur) lus ; rien sous `diag/`, `runs/`, `donnees/` ; rien de 7a, 7b, T0.6, T0.7,
  B bis, P3-bis, du bras d'attaque ni du mode tenu à l'écart ; aucune valeur de clé, ni `env` ni `printenv` ; aucun git avec
  `GIT_DIR`, `GIT_WORK_TREE` ou `GIT_INDEX_FILE` ; aucun fichier existant modifié ; rien committé ; aucun identifiant de modèle
  écrit.
- **Incidents** : la mesure des durées a tourné sur le conteneur partagé, chargé par d'autres processus (charge moyenne relevée
  dans sa sortie) : ses durées sont des majorants probables (devis v4) ; scellements sous l'interpréteur du venv avec
  `PYTHONPATH=src` : des `__pycache__` ignorés par git peuvent en naître.

Fin de la rédaction : [HEURE-FIN]
