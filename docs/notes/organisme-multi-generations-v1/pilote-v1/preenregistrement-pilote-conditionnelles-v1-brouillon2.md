# Préenregistrement — pilote d'une génération : les vrais proposeurs trouvent-ils une composante conditionnelle avant sa condition ? — v1, brouillon 2

**Statut : brouillon 2 (R1), candidat au scellement après la vérification courte du différentiel et les préalables de la
section « Préalables ».** Il applique à la lettre les corrections E-1 à E-11 de la contre-lecture
`contre-lecture-pilote-v2.md` (Claude Fable 5.2, « scellable après corrections »,
`823b6e9e8624efe77685300a7303d6fdece8bbdfad4ec10765706e2f8f49c0fc`, vérifiée contre son compagnon), et les mots de Lazar
**R-2504** et **R-2506**. Le brouillon 1 (`ef90476f32c8e16b950f725ebcfcc2c3a8aefd7b30c392bd574993b42b75af0e`) reste versé,
inchangé (R12). Ses titres de niveau 2 sont ceux du gabarit (`prereg/gabarit-preregistrement-v1.md`) : le scellement décisif
passe par `controle_ia.prereg.sceller_prereg` (E-11 (iv)). **Aucune course, aucun appel, aucune dépense** avant le texte scellé,
les lignes de GO inscrites par Lazar et les préalables.

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent de la session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`.
  **Conflit dit** : je suis aussi l'auteur de la conception v4, de sa famille MR-2 et de la valeur 0,02 que ce pilote éprouve.
- **Heures** (`date -u`) : début du brouillon 2 2026-11-13 09:48:26 ; programme v2 scellé puis sorties du 09:53:29 au 09:54:36 ; fin : dernière ligne.
- **Calculs** : légers, un processus à la fois, `ulimit -v 6000000`, `OMP_NUM_THREADS=2` ; Python 3.13.18, numpy 2.5.3.

## Changements depuis le brouillon 1

| # | correction ou mot | ce que fait le brouillon 2 | où |
|---|---|---|---|
| R-2506 (1) | 4 mondes MR-2, bras A seul, 16 appels ; P_VUE supposée 0,25, à dire | dessin à 4 mondes et un bras ; bras B retiré ; P_VUE = 0,25 **supposée, non mesurée**, écrit à la règle et au banc ; **Q-P1 retirée** (tranchée) | Dessin ; Critères ; Décisions |
| R-2506 (2) | décision sur la valeur ponctuelle portée au banc, sauf P-1, avec ses taux d'erreur écrits d'avance, refaits sur 16 appels et scellés | règle P-0 / P-1 / P-2 au ponctuel ; **taux d'erreur** par programme (`taux-pilote-v2.json`) | Prédiction ; Critères |
| R-2504 | rien servi sur les conditions ; profondeur ouverte à 3 conditions | gabarit et gardien : « au plus 3 conditions emboîtées », sans dire à quoi elles servent ; la ligne « §3.6 (grammaire servie) » de la section 6 de la conception v4 est **retirée** | Dessin ; Code (C-5, C-6) |
| E-1 | écrire la règle qui décide vraiment | la décision passe par le ponctuel au banc ; table par compte x et table par p vrai refaites par le programme ; **le pilote ne peut jamais établir H-P** (0 sur 16 laisse une borne haute de 0,038, sous p_max cette fois, mais le banc ne mesure rien sur les proposeurs) ; la phrase du brouillon 1 « ne réfute qu'une hypothèse franchement fausse » est remplacée | Prédiction ; Critères |
| E-2 | « répondu », minimum, borne de jetons, appels manquants | répondu = réponse complète **et** une carte admise évaluable ; tronqué, échec, sans carte hors du dénominateur ; **minimum 12 sur 16 et 3 par monde**, sinon P-0 ; bornes de sortie par proposeur écrites ; les 16 appels attendus vérifiés par le programme | Métrique ; Dessin |
| E-3 | une unité par appel | **première conditionnelle** de chaque monde seule ; n = 16 connu d'avance ; seconde de chaîne à part ; appels d'un même modèle non indépendants : puissance optimiste, dit | Métrique |
| E-4 | proposeurs inégaux | survie par **produit des q̂ par proposeur** (p_prod) rapportée ; classe de décision différente → réserve et nœud de Lazar avant le banc ; le banc tourne aussi à p_prod | Métrique ; Critères |
| E-5 | R-2504 au texte ; profondeur | voir R-2504 ; essai R5 du gardien (3 conditions admise, 4 refusée) ; empreinte du gabarit au bloc gelé ; « p_c ne vaut que pour ce gabarit, le même au banc et dans la course » | Dessin ; Code |
| E-6 | gardien et évaluation | **C-16** (lois de référence passées au gardien avant tout appel) et **C-17** (égalité évaluateur de la chaîne / `M.probas`) ; carte admise non évaluable = réserve listée par le programme | Code ; Métrique |
| E-7 | essais, imports, septième carte, nom neuf | programme **`mesure_pilote_v2.py`** : essais P-0 (deux formes), P-1, P-2, minimum tenu, neuf artefacts, septième carte refusée comptée, imports gelés (chaque module égal à son compagnon, deux empreintes écrites) ; π1 cite `2230dd70…` | Métrique ; Lignes de GO |
| E-8 | sensibilité contre principale | compte différent entre τ et τ', ou classe différente entre unité appel et unité carte → réserve et nœud avant le banc ; le banc tourne aux deux valeurs | Critères |
| E-9 | devis, défauts | total au pire **39 USD** (20 + 19) dit en tête ; aucune dépense avec défaut ; π1 cite le programme v2 | Devis ; Décisions |
| E-10 | graine, isolement | fonction exacte, codée et essayée sur un secret public (`graine-pilote-v2.json`) ; les 8 tirages sont ceux de `generer_v4` ; le témoin atteste aussi l'absence d'outil, de fichier, de dépôt et de texte hors des pièces gelées | Dessin |
| E-11 | prédiction, audit, lecteur, titres | prédiction d'auteur écrite ; déclencheurs d'audit chiffrés (x = 0 ; x ≥ 3) ; audit et lecture de l'issue par des sous-agents neufs ; titres du gabarit | Prédiction ; Audit ; Critères |
| S-1 à S-10 | suggestions | S-1 adoptée par R-2506 ; S-2 sans objet (bras B retiré) ; S-3 bascule à 0,5 = **0,034** ; S-4 comparaison avant arrondi ; S-5 sans objet ; S-6 refus propre et conduite sur erreur ; S-7 heures hors du corps empreinté ; S-8 `p_min_vue` sans rôle, dit ; S-9 probabilités par classe **retirées** de la sortie ; S-10 défauts écrits | partout |

## Documents qui font foi (chemin, empreinte sha256)

Chemins relatifs à `docs/notes/organisme-multi-generations-v1/`.

| pièce | chemin | empreinte |
|---|---|---|
| contre-lecture du brouillon 1 (fait foi) | `pilote-v1/contre-lecture-pilote-v2.md` | `823b6e9e8624efe77685300a7303d6fdece8bbdfad4ec10765706e2f8f49c0fc` |
| brouillon 1 (gardé) | `pilote-v1/preenregistrement-pilote-conditionnelles-v1-brouillon1.md` | `ef90476f32c8e16b950f725ebcfcc2c3a8aefd7b30c392bd574993b42b75af0e` |
| mots de Lazar R-2504, R-2506 | `registres/decisions.md` (registre vivant) | — |
| conception v4 (famille MR-2) | `conception-monde-riche-doublons-v4.md` | `47e38ec0663320e8c68011130c3f1b8e1017969cbb740d30c83a78eb5db0a6dc` |
| générateur et vérificateur MR-2 | `outils-v4/monde_riche_v4.py` | `4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8` |
| seuils (script ; sortie) | `pilote-v1/outils/seuil_pilote_v1.py` ; `pilote-v1/sorties/seuil-pilote-v1.json` | `14eecfccdd83274d32388fcf2771bc608f0ad83bd8a3e5ac1161322d775e46ab` ; `16cd10047d2b353e05e02c711dbaa8943e5845ad6e60732dfad7dbb6a03590c5` |
| **programme de la mesure, de la règle, des taux et de la graine (v2)** | `pilote-v1/outils/mesure_pilote_v2.py` | `2230dd70bec2f3e9971dda3f5b7b76cc066493c97a3280fb077b12172e837b3d` |
| taux d'erreur (sortie scellée) | `pilote-v1/sorties/taux-pilote-v2.json` | `a1240a57f474f3bac369e2a65a3155a9924769c549000e729a8bac029eea3a36` |
| essais R5 du programme | `pilote-v1/sorties/essai-mesure-pilote-v2.json` | `77fdd8d36c60c0e7a76b4a1689936d147e4876018f97382be426bbc8f350933b` |
| essai de la fonction de graine | `pilote-v1/sorties/graine-pilote-v2.json` | `e9706452e27ef2decf5de6d85c92856932ae5f93de525287111be61dccb1955d` |
| devis (script ; sortie) | `pilote-v1/outils/devis_pilote_v2.py` ; `pilote-v1/sorties/devis-pilote-v2.json` | `fa475e7a93e8bc4aa80c70a18d0e02ef1feae7d3a7751ff5bc29ad82c4ef5290` ; `dba76367488ca0b7c66fbf66f03e44357cf5ad02d99b267d522ab2489542c350` |
| programme v1 et ses sorties (gardés, remplacés) | `pilote-v1/outils/mesure_pilote_v1.py` ; `devis_pilote_v1.py` (importé par le v2) | `0d806aca…` ; `99d5d677…` |
| code v67 (différentiel lu) | `docs/notes/organisme-boucle-reelle-v1/ecart-1-sortie-proposeur-v1/code-v67/organisme-v67-contre-7e415cb.patch` | compagnon |

Modules importés par le programme v2, chacun vérifié contre son compagnon à chaque lancement (liste au champ `hors_corps` de
chaque sortie) : `monde_riche_v4.py` et `seuil_pilote_v1.py` (empreintes écrites dans le programme), et les outils v1 à v3
(`monde_riche_outils_v1`, `puissance_monde_riche_v1`, `generateur_mondes_v1`, `complements_synthese_v1`,
`verifier_monde_kimi_v1`, `monde_riche_outils_v2`, `generateur_mondes_v2`, `verifier_monde_v2`, `puissance_monde_riche_v2`,
`puissance_monde_riche_v3`).

## En dix lignes

1. **Question** : sans sa condition dans l'archive, un vrai proposeur propose-t-il une composante conditionnelle MR-2 ? La
   conception v4 a supposé 0,02 par carte, sans pièce ; la course n'a de sens que si c'est vrai.
2. **Dessin** (R-2506) : **4 mondes MR-2**, **bras A seul** (archive {K1}), 4 vrais proposeurs, un appel chacun par monde :
   **16 appels**, au plus 6 cartes chacun ; mondes d'un secret propre, jamais publiés, jamais réutilisés.
3. **Rien servi** sur les conditions ni sur les sortes d'effets ; profondeur permise : **au plus 3 conditions emboîtées** (R-2504).
4. **Mesure** (programme `mesure_pilote_v2.py`) : x = appels répondus dont une carte porte la première conditionnelle du monde ;
   **p_c = 1 − (1 − x/n)^(1/6)** ; Clopper-Pearson 95 %.
5. **Règle** : P-0 si moins de 12 appels répondus ou moins de 3 dans un monde ; **P-1** (nœud) si la borne basse de p_c >
   0,051 (x ≥ 9 sur 16) ; sinon **P-2** : le banc de 24 mondes reçoit **p_c ponctuel** et P_VUE = 0,25 supposée.
6. **Ce qui décide en pratique** : au banc, la règle de garde tient si x ≤ 2 sur 16 (p_c ≤ 0,022), presque jamais si x ≥ 4.
7. **Taux d'erreur écrits d'avance** (modèle approché) : si p vrai = 0,02, la course est refusée **une fois sur cinq** (0,20) ;
   si p vrai = 0,051, elle est permise **une fois sur quatre** (0,26) ; 0,075 → 0,075 ; 0,10 → 0,017.
8. **Prédiction de l'auteur** : 1 à 3 appels sur 16 (p_c entre 0,01 et 0,035), confiance faible ; aucun signe visé (R3).
9. **Devis** : **39 USD au pire** (crédits de Claude 20 ; hors crédits 19 : Argon 8, Astra 8, machine 3) ; ≈ 14,90 attendus.
10. **Code** : C-1 à C-17 manquent dans la chaîne v67 (monde privé à 8 traits, Claude et Astra, une génération sans étage,
    gardien à 3 conditions, égalités d'évaluation) ; dits, non écrits.

## Question et ce qui existe

La conception v4 (`47e38ec0…`) a rendu la question du progrès répondable **sous une hypothèse** de masquage : 0,02 par carte
tant que la condition n'est pas connue, 0,25 ensuite, sans pièce. Sous cette hypothèse, la règle de garde tient (8 mondes sur
12) ; sans elle, non (0 sur 12). La part marginale (2 % en médiane) dit la structure, pas le comportement des proposeurs, qui
reçoivent 400 épisodes et peuvent essayer des conditions. Lazar a retenu le pilote (R-2501, Q-14 (b)), puis ce dessin
(R-2506). Ce qui existe : la course réelle v67 (issue C1, Kimi et Argon, monde jouet à 2 traits) ; aucune mesure du
comportement de proposeurs sur des composantes conditionnelles.

## Hypothèse

H-P : la probabilité par carte qu'un vrai proposeur, sans la condition dans l'archive, propose la première conditionnelle d'un
monde MR-2 est assez basse pour que la règle de garde d'un banc de 24 mondes tienne (p_c ≤ 0,034, point de bascule à 0,5 du
modèle approché ; p_max = 0,051 est le point où elle ne tient plus qu'avec probabilité 0,05). Le pilote donne au banc la valeur
de ce paramètre ; il ne peut **jamais établir** H-P (le banc ne mesure rien sur les proposeurs, et 16 appels laissent une
borne haute d'au moins 0,038) ; il peut la réfuter (P-1) ou conduire le banc à la refuser (P-2 défavorable).

## Prédiction chiffrée et signe attendu

**Prédiction de l'auteur** (E-11 (i)) : **x entre 1 et 3 sur 16** (p_c entre 0,011 et 0,034) ; confiance faible (aucune pièce sur
ces proposeurs devant ces mondes). **Aucun signe visé** (R3) : l'issue favorable n'est pas recherchée ; chaque issue a sa suite
écrite. Réfutation : P-1 (x ≥ 9), ou P-2 défavorable au banc (x ≥ 3 le plus souvent, voir ci-dessous).

**Lecture par compte** (n = 16 ; `taux-pilote-v2.json`, `a1240a57…`, champ `taux.n=16.par_x` ; « règle tenue au banc » sous le
modèle approché de `seuil_pilote_v1.py`, le banc lui-même décide) :

| x sur 16 | p_c | intervalle 95 % | issue | règle de garde tenue au banc (modèle) | classe |
|---|---|---|---|---|---|
| 0 | 0 | [0 ; 0,0377] | P-2 | 1,00 | favorable |
| 1 | 0,0107 | [0,0003 ; 0,0582] | P-2 | 1,00 | favorable |
| 2 | 0,0220 | [0,0026 ; 0,0774] | P-2 | 0,93 | favorable |
| 3 | 0,0340 | [0,0069 ; 0,0966] | P-2 | 0,49 | défavorable (à la bascule) |
| 4 | 0,0468 | [0,0125 ; 0,1163] | P-2 | 0,10 | défavorable |
| 5 à 8 | 0,061 à 0,109 | bornes basses 0,019 à 0,046 | P-2 | ≤ 0,008 | défavorable |
| 9 et plus | ≥ 0,129 | borne basse ≥ 0,057 | **P-1** | — | — |

**Taux d'erreur de la décision, écrits d'avance** (R-2506 (2) ; même sortie, champ `taux.n=16.par_p_vrai` ; appels supposés
indépendants, ce qui rend ces taux **optimistes** : deux appels d'un même modèle ne sont pas deux tirages indépendants, E-3) :

| p vrai par carte | 0 | 0,005 | 0,01 | 0,02 | 0,03 | 0,034 | 0,04 | 0,051 | 0,075 | 0,10 | 0,15 | 0,25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P-1 | 0 | 0 | 0 | 0 | 0,0004 | 0,0009 | 0,0027 | 0,0126 | 0,0979 | 0,307 | 0,778 | 0,997 |
| classe favorable (x ≤ 2) | 1 | 0,989 | 0,937 | 0,727 | 0,485 | 0,400 | 0,292 | 0,153 | 0,030 | 0,004 | 0,0001 | 0 |
| **course permise** (P-2 puis règle tenue au banc) | 1 | 0,989 | 0,951 | **0,799** | 0,602 | 0,525 | 0,418 | **0,259** | 0,075 | 0,017 | 0,0006 | 0 |
| **course refusée** | 0 | 0,011 | 0,050 | **0,201** | 0,398 | 0,475 | 0,582 | **0,741** | 0,925 | 0,983 | 0,999 | 1 |

- **Erreur de refus** (l'hypothèse de la v4 est vraie, p = 0,02, et la course est refusée) : **0,20**.
- **Erreur d'acceptation** (p vrai = p_max = 0,051, et la course est permise) : **0,26** ; à 0,075 : 0,075 ; à 0,10 : 0,017.
- À 12 ou 14 appels répondus (minimum tenu) : refus à 0,02 de 0,22 et 0,21 ; acceptation à 0,051 de 0,29 et 0,27 ; à 0,075 de
  0,10 et 0,09 (même sortie, `n=12`, `n=14`).
- Entre 0,03 et 0,05, le pilote ne décide rien de fiable (permise de 0,60 à 0,26) : dit d'avance.

## Dessin

### Mondes et secret

- **Famille MR-2** (conception v4 §2 ; `monde_riche_v4.py`, `4b165847…`, porté dans l'arbre de l'organisme sous un nom neuf, C-4,
  C-15) ; vérification C0 à C8 v4 (toute conditionnelle certifiée, C8 à m = 48), refus rapportés.
- **Quatre mondes du pilote**, d'un **secret du pilote** distinct des secrets de calibration et de test (forme Q-3 (c)) : ce
  texte scellé, sans secret ; pièces servies gelées et scellées ; secret machine de 32 octets (`secrets.token_bytes`) tiré sur la
  machine privée, **empreinte inscrite et poussée** ; puis la phrase de Lazar, empreinte inscrite.
- **Graine du monde r ∈ {1, 2, 3, 4}** (E-10 (i), fonction `graine_monde_pilote` du programme v2) : **2⁶⁴ + entier des 8 premiers
  octets (gros-boutiste) de sha256(« pilote-conditionnelles-v1 » ∥ 0x00 ∥ secret (32 octets) ∥ 0x00 ∥ phrase en UTF-8, non vide,
  sans octet nul ∥ 0x00 ∥ empreinte sha256 du texte scellé (32 octets) ∥ 0x00 ∥ r (un octet))**. Les **8 tirages** d'un monde
  sont ceux de `generer_v4` (sous-graines `SeedSequence(graine, spawn_key=(k,))`, k = 0 à 7, code scellé) : **aucun autre
  compteur**. Essai sur un secret public de développement (32 octets nuls ; `graine-pilote-v2.json`, `e9706452…`) : rejeu égal,
  quatre graines distinctes ≥ 2⁶⁴, un secret différent change la graine, cinq entrées malformées refusées, huit sous-graines
  distinctes.
- Génération et vérification dans un processus qui n'imprime que des empreintes et des contrôles ; mondes écrits par
  `ecrire_prive` dans un dossier de la liste blanche, **hors de tout dépôt** ; seules leurs empreintes vont au registre.
- **Jamais publiés** (ni secret, ni phrase, ni devis), **jamais réutilisés** (ni au banc de 24 mondes, ni en test). La sortie de
  la mesure ne contient que des empreintes de mondes et des comptes d'appels ; elle ne dit plus la composition des mondes par
  classe (S-9).

### Archive servie

**K1** de chaque monde (`k1_du_monde`), arrondie à six décimales, servie comme héritage de génération 0. **Bras A seul**
(R-2506) : archive {K1}. La condition de la première conditionnelle est une moyenne, jamais l'effet de K1 (le programme refuse le
monde sinon). La probabilité d'une conditionnelle **une fois sa condition connue** n'est **pas mesurée** : le banc garde
**0,25, supposée** (conception v4), et le rapport du pilote le dira.

### Proposeurs, gabarit, gardien

| proposeur | modèle | crédits | plafond de session | borne de sortie (E-2 (iii), estimé) |
|---|---|---|---|---|
| Fable 5.2 | `claude-fable-5-2` | Claude | 3 USD | 70 000 jetons |
| Opus 5.5 | `claude-opus-5-5` | Claude | 2 USD | 95 000 jetons |
| Argon | `gemini-4-argon` | hors crédits | 2 USD | 36 000 jetons |
| Astra | `gpt-6-astra` (« rapporté, à confirmer » ; prix supposé 10 / 50 USD par million de jetons) | hors crédits | 2 USD | 36 000 jetons |

- **Bornes de sortie** : (plafond de session − coût d'environ 15 000 jetons d'entrée) / prix de sortie, arrondi au-dessous
  (**estimé**). Six arbres pleins de 48 feuilles demandent environ 30 000 jetons (estimé : ≈ 5 000 par carte) ; **la réflexion
  compte dans la sortie** : chez Argon et Astra la marge est mince ; une réponse coupée est « tronquée », hors du dénominateur,
  comptée (le minimum de 12 sur 16 l'encadre). Les bornes sont écrites dans la configuration et lues par le code (C-7).
- **Un appel** par proposeur et par monde ; au plus 6 cartes ; la septième et les suivantes sont refusées au gardien et
  comptées ; **aucune reprise** d'un appel en échec ou tronqué.
- **Gabarit servi** (R-2504) : celui de la course : dimension 8, 3 sous-populations, grammaire servie (`par_sous_population`,
  `si_sinon` sur un trait ou une sous-population), **« au plus 3 conditions emboîtées »** ; **rien** sur l'existence possible de
  conditions dans le monde, ni sur les sortes d'effets, ni sur la famille ; aucune consigne diversifiante ; la tranche de 400
  épisodes de développement. La ligne « §3.6 (grammaire servie) » de la section 6 de la conception v4 (« le gabarit servi aux
  proposeurs dit l'existence possible d'une condition ») est **retirée** par R-2504. **Empreinte du gabarit servi** au bloc gelé
  de ce texte (marqueur [GABARIT-SHA256]) ; **p_c ne vaut que pour ce gabarit, le même au banc et dans la course.**
- **Gardien** mécanique : grammaire, bornes ±4, **au plus 3 conditions emboîtées**, évaluation sur un jeu factice à la dimension
  du monde ; essai R5 : une carte à 3 conditions admise, une à 4 refusée (C-5).
- **Isolement** : relais par fournisseur ; une session neuve sans historique par appel ; **réponse brute** (corps entier, raison
  d'arrêt, en-tête du modèle servi, usage) écrite et scellée **avant** l'extraction des cartes ; **témoin d'isolement** de chaque
  session : identité du relais, absence d'historique, empreinte du texte servi égale à celle reçue, **aucun outil, aucun accès à
  un fichier ou à un dépôt, aucun texte servi hors des pièces gelées** (E-10 (ii) : la conception de la famille est dans le
  dépôt, et deux proposeurs sont de la lignée qui l'a écrite) ; absence = arrêt.
- **Aucun juge, aucun test de mort, aucun expérimentateur, aucun vérificateur** (Q-P2 (a), section « Décisions »).

### Ordre

Texte scellé → lignes de GO inscrites → secret engagé et poussé → phrase de Lazar → 4 mondes générés et vérifiés, empreintes au
registre → C-16 et C-17 joués (arrêt sinon) → essai à blanc (proposeurs factices des quatre relais, vraies pièces servies) →
16 appels réels, monde 1 à 4 → réponses brutes et témoins scellés → extraction → gardien → `CARTES.json` scellé →
**`mesure_pilote_v2.py mesurer`, une seule fois** → rapatriement (réponses brutes, témoins, cartes, sortie de la mesure ;
jamais les mondes) → destruction de la machine (R10).

## Métrique

Programme `mesure_pilote_v2.py` (`2230dd70…`), commande `mesurer MONDES.json CARTES.json SORTIE.json` :

- **Appel** : état exporté `complet` (raison d'arrêt normale), `tronque` (raison d'arrêt = borne) ou `echec`. **Répondu** =
  `complet` et au moins une carte admise et évaluable ; un appel complet sans telle carte est « sans carte ». Tronqué, échec et
  sans carte : **hors du dénominateur**, comptés à part (E-2 (i)). Les **16 couples** (monde, proposeur) doivent tous figurer,
  une fois chacun ; sinon refus (E-2 (iv)).
- **Unité** (E-3) : la **première conditionnelle** de chaque monde, une par appel ; n = nombre d'appels répondus (16 au plus,
  connu d'avance) ; la seconde d'une chaîne rapportée à part (`secondes_de_chaine`).
- **Porte** : attribution Δ_i = gain(carte | W) − gain(carte | W₋ᵢ) ≥ τ_i = max(0,005 ; 0,75 · I_i), oracle de 12 000 instances.
  Carte refusée, au-delà de la sixième, ou admise mais non évaluable : ne porte pas ; les non évaluables sont **listées comme
  réserve** (E-6) et relues à l'audit. La porte est la règle de capture de la conception, la même qu'au banc ; sa dépendance au
  reste de la carte (contre-lecture, E-8) est une réserve dite, pas un réglage.
- **Principale** : x = appels répondus dont une carte admise porte la première conditionnelle ; **p_c = 1 − (1 − x/n)^(1/6)** ;
  intervalle : Clopper-Pearson 95 % bilatéral sur x/n, transformé ; borne basse comparée à p_max **avant arrondi** (S-4).
- **Par proposeur** (E-4) : x_j sur n_j ; survie d'une génération = Π_j (1 − x_j/n_j) (ramenée à quatre proposeurs si l'un n'a
  aucun appel répondu) ; **p_prod** = 1 − survie^(1/24) ; jamais un classement (N-058).
- **Sensibilités** (E-8) : τ'_i = max(0,005 ; 0,25 · I_i) ; unité carte (cartes qui portent / emplacements, Clopper-Pearson).
- **Chaîne réelle** (secondaires, aucune issue) : coût par fournisseur et par appel (relevés des relais rapprochés des réponses
  brutes), jetons d'entrée et de sortie, troncatures, sessions en échec, cartes rendues, refusées, au-delà de six, non
  évaluables, durées.
- Retiré du brouillon 1 : les probabilités par classe (forte, moyenne, faible, latente) ; elles disaient la composition des
  mondes jamais publiés (S-9) et le banc ne les reprend pas (R-2506 ne parle que de p_c) ; Q-P3 retirée avec elles.

## Seuil

- **p_max = 0,051** (`seuil-pilote-v1.json`, `16cd1004…`), recalculé par le programme à chaque lancement (refus s'il diffère) :
  plus petit p où la règle de garde d'un banc de 24 mondes tient avec probabilité ≤ 0,05 sous le modèle approché (survie
  (1 − p)²⁴, toute carte qui porte est captante, 2 mondes sur 12 à chaîne). **Bascule à 0,5 : 0,034** (`taux-pilote-v2.json`,
  S-3) ; p_max cumule deux prudences (règle tenue ≤ 0,05 et borne basse à 97,5 %).
- **Classe de décision** : « favorable » si P(règle tenue au banc | p_c) ≥ 0,5 sous ce modèle (x ≤ 2 sur 16) ; sert aux réserves
  E-4 et E-8, jamais à décider à la place du banc.
- **Minimum** : 12 appels répondus sur 16 et au moins 3 par monde.
- Niveau des intervalles : 95 %. `p_min_vue` de `seuil_pilote_v1.py` n'a aucun rôle (S-8).

## Plan d'analyse

1. Vérifier les empreintes : texte scellé, mondes (registre), réponses brutes, témoins, `CARTES.json`, programme et modules
   importés (le programme les vérifie lui-même).
2. Lancer **une seule fois** `python3 -I -B mesure_pilote_v2.py mesurer MONDES.json CARTES.json SORTIE.json` sur la machine privée ;
   sortie scellée ; heures et chemin hors du corps empreinté (S-7).
3. Issue lue au champ `regle` de la sortie, **par un sous-agent neuf** qui n'a écrit ni ce texte, ni le code, ni la conception
   v4 (E-11 (iii) : elle commande une course de 422 USD de plafonds) ; il applique la section suivante et rien d'autre.
4. Rapprochement des coûts par fournisseur ; écarts rapportés.
5. Aucune autre exclusion que celles de la section « Métrique » ; aucune analyse en sous-groupe ne décide.
6. Le rapport dit : « P_VUE = 0,25 supposée, non mesurée » ; « p_c ne vaut que pour ce gabarit » ; les taux d'erreur ci-dessus.

## Critères de lecture gelés

La première ligne qui s'applique donne l'issue (calculée par le programme, champ `regle`) :

| issue | condition | ce qui suit |
|---|---|---|
| **P-0** non concluant | moins de 12 appels répondus sur 16, ou moins de 3 dans un monde | nœud de Lazar ; aucun banc sur cette mesure ; causes rapportées (échecs, troncatures, sans carte) |
| **P-1** « MR-2 ne sert pas telle quelle » | borne basse de p_c > 0,051 (x ≥ 9 sur 16 ; ≥ 8 sur 14 ; ≥ 7 sur 12) | nœud de Lazar : aucun banc MR-2 avec masquage ; options écrites alors (MR-1 et la réponse « garde et boucle », Q-13 (a) ; famille neuve sur texte neuf) |
| **P-2 avec réserve** | sinon, et l'une de : classe(p_c) ≠ classe(p_prod) (E-4) ; x à τ ≠ x à τ' (E-8) ; classe(p_c) ≠ classe(unité carte) (E-8) | **nœud de Lazar avant le banc** ; le banc tourne aux valeurs en désaccord (p_c, p_prod, p à τ', p unité carte), toutes rapportées ; Lazar dit laquelle décide |
| **P-2** banc | sinon | banc de 24 mondes de calibration (code v68 gelé) : **P_CACHÉE := p_c ponctuel**, **P_VUE := 0,25 supposée** ; la règle de garde de la conception v4 y décide de la course ; le banc rapporte aussi la règle aux deux bornes de l'intervalle (mesure, ne décide pas) |

Une issue P-2 favorable **ne dit pas** que les proposeurs « ne voient pas » les conditionnelles : elle dit que le pilote ne l'a pas
réfuté, avec les taux d'erreur ci-dessus.

## Audit de symétrie (R4), écrit d'avance

Déclencheurs chiffrés (E-11 (ii) ; champ `audit_R4` de la sortie) :

- **x = 0** (trop propre pour l'hypothèse) : relire **toutes** les cartes refusées au gardien, au-delà de six ou non évaluables,
  et 3 cartes par appel tirées au hasard (graine dérivée de l'empreinte de `CARTES.json`) ; vérifier que les épisodes servis
  contiennent les traits ; vérifier que les témoins disent le gabarit servi ; rapporter.
- **x ≥ 3** (défavorable ou à la bascule, contre l'hypothèse) : relire les cartes qui portent ; vérifier qu'aucune pièce servie ne
  décrit la famille ou une condition (fuite, gabarit, témoins) ; vérifier l'isolement ; relire aussi les cartes refusées et non
  évaluables ; rapporter.
- L'audit est fait par un **sous-agent neuf** qui n'a écrit ni ce texte, ni le code, ni la conception v4 ; il ne change pas
  l'issue, il la commente (réserve écrite).

## Liste d'arrêt

- Empreinte d'un monde, du texte, d'une pièce servie, du gabarit, du programme ou d'un module importé différente → arrêt avant tout
  appel (le programme refuse de lui-même pour ses modules).
- C-16 ou C-17 en défaut (une loi de référence refusée au gardien ; écart d'évaluation > 10⁻⁹) → arrêt avant tout appel.
- Réponse brute ou témoin d'isolement absent pour un appel → arrêt (code 3), pièces versées.
- Panne d'un relais → l'appel est « échec », aucune reprise, aucune bascule ; deux échecs du même fournisseur → arrêt du pilote,
  issue lue sur ce qui est répondu (P-0 si le minimum manque).
- Dépense d'un fournisseur atteignant sa part → arrêt ; aucune ligne d'extension.
- Un monde sans tirage conforme en 8 → arrêt avant tout appel, cause écrite ; nouvelle graine seulement sur texte neuf et mot de
  Lazar.
- **Erreur du programme de la mesure** (exception, pas un refus nommé ; S-6) : la mesure n'a rien rendu, rien n'est lu ; cause
  écrite ; correction seulement par un programme sous un nom neuf, contre-lu, scellé, avant tout nouveau lancement ; les entrées
  ne changent pas. Un **refus nommé** sur les entrées (appel manquant, empreinte) : l'export est corrigé sans regarder aucune
  attribution, l'écart est rapporté.
- Essais R5 du programme faits (`essai-mesure-pilote-v2.json`, `77fdd8d3…`, `tout_conforme` vrai) : P-2 (2 sur 16), P-1 (16 sur
  16), P-0 à 11 répondus, P-0 par un monde à 2, minimum tenu à 12 (P-2), neuf entrées malformées refusées (appel manquant, en
  double, proposeur inconnu, emplacement non entier, en double, septième admise, carte d'un appel en échec, empreinte fausse,
  trois mondes), septième refusée comptée, carte à mémoire listée non évaluable, un proposeur qui trouve partout (survie par
  produit 0), un module importé à empreinte fausse refusé.

## Code : ce qui manque pour faire tourner un monde MR-2 dans la chaîne réelle (dit, non écrit)

Lu dans le différentiel du code v67 et la configuration v8 ; l'arbre de l'organisme (`lciric/ideation-organism`, `ab53b7f4`)
n'est pas dans cette session : noms à vérifier sur l'arbre. Noms neufs (R12).

| # | où (v67) | ce qui manque |
|---|---|---|
| C-1 | `A.charger_monde(RACINE)`, `L64.verifier_monde(monde, MONDE_SHA256)` | monde lu hors de l'arbre, chemin au lancement, empreinte comparée au registre |
| C-2 | manifeste `monde={source, sha256, loi_vraie}` | n'écrire que l'empreinte du monde |
| C-3 | `B65.DIM`, `episodes_de_developpement` | dimension 8, 3 sous-populations lues dans le monde ; tranche de 400 épisodes du monde MR-2 |
| C-4 | compilation du monde | `compiler_v4` et `verifier_v4` dans l'arbre ; loi compilée validée par `selection_pari.valider_loi` |
| C-5 | gardien (jeu factice D = 2) | jeu factice à la dimension du monde ; **au plus 3 conditions emboîtées** (R-2504) ; septième carte refusée et comptée ; **essai R5 : 3 conditions admise, 4 refusée** |
| C-6 | gabarit (D = 2) | D = 8, 3 sous-populations, `si_sinon`, `par_sous_population`, **« au plus 3 conditions emboîtées »** ; rien sur les conditions du monde ni les sortes d'effets ; empreinte du gabarit écrite au manifeste |
| C-7 | proposeurs Kimi et Argon seuls ; plafond de session unique | commandes et relais pour **Claude (Fable 5.2, Opus 5.5)** et **Astra** ; plafond de session et **borne de sortie par modèle** (section « Dessin ») ; délais par fournisseur ; configuration v9 ; voie d'accès aux crédits de Claude à confirmer |
| C-8 | jetons (Kimi, Argon) | champs de Claude et d'Astra ([CHAMPS-ASTRA]) ; **raison d'arrêt** lue (complet / tronqué) |
| C-9 | parts `kimi`, `argon` ; lecteur du GO | parts `claude`, `argon`, `astra`, machine ; lecteur de deux lignes (π1, π2) |
| C-10 | réponses (réserve R-2 de la v67) | réponse brute et témoin d'isolement (contenu de la section « Dessin ») par appel, scellés avant l'extraction ; absence = arrêt |
| C-11 | `B.GENERATIONS` = 2 ; `jouer_boucle` avec juge et étage | lanceur du pilote : une génération, proposeurs puis gardien, sans juge ni étage ; 4 mondes, sessions séparées ; aucun bac exigé |
| C-12 | héritage de départ | {K1} par monde, écrit par programme depuis le monde privé ; empreinte au registre |
| C-13 | — | export `CARTES.json` = `{"cartes": [...], "appels": [...]}` au format du programme v2 (appel : monde, proposeur, état complet / tronque / echec ; carte : monde, proposeur, emplacement ≥ 1, état admise / refusee, loi) et `MONDES.json` privé |
| C-14 | lecture gelée v66 | lecture du pilote = champ `regle` de la sortie du programme v2 et rapprochement des coûts |
| C-15 | — | générateur MR-2 dans l'arbre avec `graine_monde_pilote` (fonction du programme v2) ; `ecrire_prive` |
| **C-16** | — | avant tout appel, pour chaque monde : les lois de référence (« K1 + première conditionnelle » calibrée, monde entier, K1) **passent le gardien du pilote**, sinon arrêt (E-6) |
| **C-17** | — | égalité des probabilités entre l'évaluateur de la chaîne (`selection_pari.proba`) et `M.probas` sur un jeu fixe de cartes de la grammaire servie, à 3 conditions comprises (écart ≤ 10⁻⁹), sinon arrêt (E-6) |
| C-18 | — | outils de l'audit et du rapport : rapprochement des coûts ; tirage des cartes relues (graine) ; proposeurs factices des quatre relais pour l'essai à blanc ; rapatriement qui prouve qu'aucun monde ne sort (liste des fichiers copiés et leurs empreintes) |

Chaque garde neuve essayée sur un cas sain et un artefact (R5) ; contre-lecture du code par un autre modèle que son développeur
(N-052). C-1 à C-10, C-15 à C-17 servent aussi la course.

## Préalables

**Avant le scellement** : vérification courte du différentiel brouillon 1 → brouillon 2 ; décisions Q-P2 et Q-P4 ; code C-1 à
C-18 écrit, essayé, contre-lu, gelé, empreintes en bloc gelé (dont celle du gabarit) ; identifiant et prix d'Astra confirmés ;
marqueurs levés. **Avant le premier appel** : lignes de GO inscrites ; secret engagé et poussé, puis phrase de Lazar ; mondes
vérifiés, empreintes au registre ; C-16 et C-17 joués ; essai à blanc réussi ; relais lancés avec leur part comme plafond ;
rapatriement essayé sur l'essai à blanc.

## Devis

`devis_pilote_v2.py` (`fa475e7a…`), sortie `devis-pilote-v2.json` (`dba76367…`) ; tout **estimé** sauf les plafonds. **Total au
pire : 39 USD** (E-9 (i) : le « ≈ 20 USD » d'un pilote se lit par ligne, crédits de Claude seuls ; R-2506 dit « même pire 20 + 19
USD »).

| poste (USD), 4 mondes, bras A, 16 appels | attendu | pire |
|---|---|---|
| **crédits de Claude** : Fable 5.2 (4 appels × 3) et Opus 5.5 (4 × 2) | 9,60 | **20,00** |
| Argon (4 appels × 2) | 1,00 | 8,00 |
| Astra (4 appels × 2) | 4,00 | 8,00 |
| machine (plafond) | 0,30 | 3,00 |
| **hors crédits** | 5,30 | **19,00** |
| **total** | 14,90 | **39,00** |

Le pire n'est une borne que si chaque relais coupe à sa part (C-7, C-9, essayés à l'essai à blanc). Aucun expérimentateur, aucun
vérificateur, aucun test de mort.

## Lignes de GO proposées, mot pour mot, non inscrites

```
| GO-AAAA-MM-JJ-NN (π1) | AAAA-MM-JJ | calcul | **Pilote d'une génération de l'organisme sur la famille MR-2, part sur crédits de Claude** : proposeurs Fable 5.2 (plafond de session 3 USD) et Opus 5.5 (2 USD), un appel par proposeur et par monde, au plus 6 cartes, aucune reprise ; 4 mondes du secret du pilote (engagé et poussé avant la phrase de Lazar), jamais publiés ni réutilisés ; bras A seul (archive {K1}) ; rien servi sur les conditions, au plus 3 conditions emboîtées (R-2504) ; gardien mécanique seul, aucun juge, aucun test de mort ; conditions toutes exigées : préenregistrement du pilote contre-lu, vérifié et scellé ; code du pilote (C-1 à C-18) contre-lu et gelé ; C-16 et C-17 joués ; essai à blanc réussi avec les vraies pièces servies ; mondes vérifiés et leurs empreintes inscrites ; réponses brutes et témoins d'isolement versés pour chaque appel ; mesure par `mesure_pilote_v2.py` (`2230dd70…`) une seule fois, issue lue par un sous-agent neuf ; jamais de ligne d'extension ; arrêt par identifiant (R10), dépenses et arrêts consignés | 20 USD (sur crédits) | 2026-11-30 | Lazar | R-2501, R-2504, R-2506 ; mot de Lazar à recopier |
| GO-AAAA-MM-JJ-NN (π2) | AAAA-MM-JJ | calcul | **Même pilote, part hors crédits** : Argon proposeur (2 USD par session) 8 USD, Astra proposeur (2 USD par session) 8 USD (identifiant et prix confirmés avant l'appel), machine 3 USD ; plafond de chaque relais égal à sa part ; mêmes conditions que la ligne π1 ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 19 USD | 2026-11-30 | Lazar | R-2501, R-2504, R-2506 ; mot de Lazar à recopier |
```

## Décisions de Lazar à trancher avant le scellement

Q-P1 (bras B) **retirée** : tranchée par R-2506 (bras A seul). Q-P3 (reprise des probabilités par classe) **retirée** : le banc ne
reprend que p_c (R-2506), les probabilités par classe ne sont plus calculées (S-9).

**Q-P2 — Périmètre de la chaîne réelle.** (a) **Proposeurs et gardien seuls** : la mesure n'a besoin que des cartes ; code plus
court ; l'étage reste éprouvé par l'essai à blanc de la course. (b) Plus le juge mécanique (processeur seul) : promotions
rapportées, aucune revendication ; demande le juge v68 avant le pilote. (c) Plus les tests de mort des cartes promues : chaîne
entière ; jusqu'à 1,60 USD par test (dépense : nœud, sans défaut). Recommandation : **(a)**, confiance 0,6. Défaut sous 48 heures :
(a) (aucune dépense de plus).

**Q-P4 — Où tourne le pilote.** (a) **La machine jetable de la course** (3 USD au plus, prix horaire consigné, détruite après) : le
pilote y éprouve la chaîne de la course. (b) Le poste local de Lazar (comme la v67) : pas de machine à payer ; mondes privés sur
son poste. Recommandation : **(a)**, confiance 0,5. **Sans défaut** (dépense, E-9 (ii)).

**Échéance.** Code C-1 à C-18, vérification, pilote, banc de 24 mondes, puis course avant le 30 novembre : serré.

## Portée

Une génération, quatre mondes, quatre proposeurs, un appel chacun : une **mesure** de ces proposeurs, devant ce gabarit, sur cette
famille. Rien sur le progrès, rien sur la probabilité une fois la condition connue (supposée), rien sur la qualité des idées ;
aucune décision de composition (N-058).

## Contre-lecture

- **Contre-lecture 1** : Claude Fable 5.2 (`claude-fable-5-2`), lecteur neuf, autre modèle que l'auteur ; brouillon relu
  `ef90476f32c8e16b950f725ebcfcc2c3a8aefd7b30c392bd574993b42b75af0e` ; rapport `pilote-v1/contre-lecture-pilote-v2.md`
  `823b6e9e8624efe77685300a7303d6fdece8bbdfad4ec10765706e2f8f49c0fc` (v1 `6d86bf11ce61c167bd6878f3f79cb12a9345ff9c7b4bab61036102d1ed20cd96`,
  gardée) ; verdict « scellable après corrections » (11 exigées) ; toutes portées (table « Changements depuis le brouillon 1 »).
- **À faire** : vérification courte du différentiel brouillon 1 → brouillon 2 par un sous-agent neuf (de préférence le même lecteur
  ou un autre Fable), sur ce texte, `mesure_pilote_v2.py` et ses quatre sorties, `devis_pilote_v2.py` ; points : E-1 (tables
  refaites par le programme), E-2 (minimum), E-4 et E-8 (nœuds), E-10 (graine).

## Marqueurs restants (aucun ne doit rester au scellement)

[GABARIT-SHA256] (empreinte du gabarit servi) ; [CHAMPS-ASTRA] (C-8) ; identifiant et prix d'Astra ; voie d'accès aux crédits de
Claude (C-7) ; bloc gelé des empreintes du code du pilote ; décisions Q-P2 et Q-P4.

Fin de la rédaction : 2026-11-13 09:58:16 UTC (`date -u`).
