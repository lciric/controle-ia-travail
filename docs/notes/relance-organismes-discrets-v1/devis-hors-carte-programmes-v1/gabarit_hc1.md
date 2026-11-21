# Organismes discrets, bras A (déplacement des contrôles appris sans consigne) — devis des lectures hors carte de la course — v1, BROUILLON 1

- **Objet** : borner ce que coûtent les lectures par modèle de langue faites hors de la carte louée pendant la course du bras A. Le devis de course l'exige à part, écrit et borné avant la demande de sa ligne 2 (`docs/notes/relance-organismes-discrets-v1/devis-bras-a-v2.md`, `83240ca6…`, sections 1, 6 et 9). Ce devis en reprend la section 6.
- **État** : brouillon 1, non contre-lu, non scellé (le rédacteur ne scelle rien), non accepté. **Aucune dépense n'est ouverte ; aucune ligne de calcul n'est demandée ici.**
- **Auteur** : agent neuf (Claude Fable 5.2), le {{DATE}} (`date -u`), sur le mandat `docs/notes/relance-organismes-discrets-v1/mandat-redacteur-fable-devis-lectures-hors-carte-v1.md` (`86c98be8…`). Il n'a lu aucune pièce du côté habilité ; il n'a écrit ni le texte du bras A, ni les devis cités, ni un programme de la course.
- **Marques** : **M** = relevé sur une pièce citée ; **C** = calculé ici, par programme (section 13) ; **S** = supposé, sans mesure ni pièce ; **[case]** = valeur à remplir, par la session de relance ou par le côté habilité.
- **Mots** : un **appel** est une lecture demandée ; un **envoi** est une tentative d'un appel. Le texte en permet trois par appel : l'envoi, une reprise s'il est resté sans réponse, une redemande de forme. Un **envoi coupé** est un envoi dont le programme ne voit pas la fin : coupé par un délai, par sa borne en octets, ou par une connexion coupée en route. La **réserve** d'un envoi est ce que le compteur retient avant de le laisser partir. Au **régime prudent**, un envoi sans compteur lisible est compté à 200 jetons par seconde de sa durée, et au moins à sa réserve (devis des essais d'admission, section 6.4).

## 0. En une page

1. **Les lectures hors carte coûtent de l'ordre de dix fois la carte.** Du côté de la relance, attendu ≈ {{ATT_AVEC}} USD avec les lots de la révision, ≈ {{ATT_SANS_LO}} à {{ATT_SANS_HI}} sans eux : ≈ 146 pour le premier lecteur (projection du texte, transcrite, non refaite ici), ≈ {{L2_EK_AVEC_0}} pour Mistral Large 4 (sorties supposées), ≈ {{J_EK_152_0}} pour le juge des deux ancres. Les deux lignes de carte : ≈ 20 à 25 USD attendus (M : devis de course, section 5).
2. **Plafonds de ce brouillon : {{TOT_PL}} USD en huit lignes**, {{TOT_PL_SANS}} sans les trois lignes de la révision, qui ne jouent que si la révision est ouverte. Le premier engagement — lots d'épreuve des deux lecteurs, ancres du juge — fait {{TOT_PL_EPR}} USD de plafonds pour ≈ {{ATT_EPR_LO}} à {{ATT_EPR_HI}} attendus. Les lignes décisives ne partent qu'après, à un plafond recalculé par programme sur le coût compté aux lots d'épreuve, jamais au-dessus des maxima écrits ici (section 5).
3. **Aucun plafond « au pire cas » n'est praticable.** Trois envois par appel à la sortie maximale pleine font {{L2_MAJ_8192}} à {{L2_MAJ_32768}} USD pour le seul second lecteur (C). Ce qui borne la dépense est le compteur du programme : au pire, le plafond d'une ligne et un envoi coupé ({{CM_2690}} USD chez Mistral, {{CN_2690}} chez Google), sous les suppositions du devis des essais d'admission, dont l'une n'est pas documentée : que la coupure d'un envoi arrête la génération et la facturation.
4. **Les volumes ont changé depuis le devis de course.** Le texte, brouillon 43, compte 25 920 lectures des deux lecteurs (30 272 avec la révision), 152 appels du juge au plus, et 6 400 lectures pour chacun des deux moniteurs à modèle de langue. En entrée, à un envoi par appel et sans les consignes des moniteurs : ≈ {{TOT_TOK_SANS}} à {{TOT_TOK_AVEC}} millions de jetons (C), contre « au moins 33 à 35 millions » au devis de course.
5. **Trois choses manquent, et sont dites.** (a) Le tarif et le réglage du premier lecteur ne sont dans aucune pièce qui m'est ouverte : ce sont des cases pour la session. (b) Mistral Large 4 et `gemini-4-neon` ne sont mesurés à leur réglage dans aucune de mes pièces : leur attendu repose sur les sorties supposées du devis des essais d'admission, et se refait par la formule dès que leurs compteurs existent. (c) Le modèle, la consigne et le tarif des moniteurs relèvent du côté habilité : je n'en donne que les volumes, une formule et un plafond conditionnel. Avec raisonnement, un moniteur peut coûter autant qu'un lecteur (4.5).
6. **Cinq décisions pour Lazar** (section 9) : le découpage et sa taille ; le régime du compteur ; la cadence ; les conditions d'envoi des textes réels ; la sortie maximale du juge. **Deux questions à la mère** (section 10) : la répartition des appels du juge par instrument ; le sens de « 102 points de lecture par action ».

## 1. Ce que ce devis couvre

- **Couvert, du côté de la relance** : les deux lecteurs de l'oracle, hors des familles des moniteurs — le premier, un modèle Claude ; le second, le candidat `mistral-large-4-0`, sous réserve de son essai d'admission — ; leurs lots d'épreuve ; le juge des deux ancres, `gemini-4-neon`, sous réserve de son essai d'admission. Selon la section 6.11 du texte, le juge lit dans la course : ses 152 appels au plus sont comptés dans le majorant des envois.
- **Couvert pour les seuls volumes** : le moniteur boîte noire par action en contexte et le juge d'une autre lignée (4.5). Leur modèle et leurs consignes relèvent du côté habilité ; je ne les ai pas cherchés.
- **Hors de ce devis** : l'essai de mesure et les deux essais d'admission (« hors de la course », 6.11 ; ils ont leurs devis) ; les lignes de carte, pour lesquelles 6.11 dit un devis neuf dû ; ce qui tourne sur processeur (base « mots et coût », classifieurs) ; un moniteur qui tournerait sur une carte, qui serait une ligne de carte.

**Ce qui a changé depuis la section 6 du devis de course**, qui chiffrait le texte scellé précédent :

| poste | devis de course, section 6 (M) | texte, brouillon 43, section 6.11 (M) |
|---|---|---|
| lectures des deux lecteurs | 1 792, un plan entier par lecture, et ≈ 272 aux épreuves | **25 920**, et 4 352 sous la révision : l'appariement se lit action par action |
| ancres | « ancre humaine », 8 jugements écrits d'avance, 0 USD | jugées par `gemini-4-neon` : 80 appels, 152 au plus |
| moniteur boîte noire par action en contexte | 6 400 ; 8 960 si les deux témoins sont lus | 6 400, « avec raisonnement » |
| juge d'une autre lignée | 2 560 | 6 400 |
| jetons d'entrée, tous postes | au moins 33 à 35 millions ; ≈ 42 avec les témoins | ≈ {{TOT_TOK_SANS}} à {{TOT_TOK_AVEC}} millions (C) ; ≈ {{TOT_TOK_TEMOINS}} si le moniteur lisait les témoins |

## 2. Volumes (M : texte, brouillon 43, section 6.11, seule section lue)

| lot, au nom du texte | instrument | phase | appels par lecteur, au plus | lectures des deux lecteurs |
|---|---|---|---|---|
{{T_VOL}}

| phase | appels d'appariement | appels de couverture | appels par lecteur | envois au plus, par lecteur | lectures des deux lecteurs |
|---|---|---|---|---|---|
{{T_PHASE}}

- **Les colonnes « instrument » et « phase » sont de mon fait.** L'instrument recoupe le compte que le devis des essais d'admission donne par lecteur (sa section 7) : 13 888 lectures d'appariement et 1 248 de couverture (C : les sommes tombent juste). La phase se lit sur le nom des lots. La liste des cinq épreuves de l'oracle, au sens du texte, n'est pas dans 6.11 : je range sous « lots d'épreuve » les cinq lots nommés avant les lots décisifs.
- 6.11 écrit « quatre épreuves mécaniques de la couverture (160 artefacts : 32 par lecteur et par épreuve) » : je garde le compte de son tableau, 128 appels par lecteur.
- **Juge des deux ancres** (M) : « 48 + 24 + 8 appels du juge ; 72 de plus sous la révision », soit 80 appels, 152 au plus.
- **Majorant des envois** (M) : 3 × (25 920 + 4 352 + 152) = 91 272.
- **Moniteurs** (M) : moniteur boîte noire par action en contexte, 5 × 1 280 = 6 400 lectures avec raisonnement ; juge d'une autre lignée, 6 400, « et, au cas B, ses 102 points de lecture par action (13.2) ».

## 3. Longueurs, réglages, tarifs, formule

### 3.1 Longueurs mesurées (M : devis des essais d'admission, section 6.2, sur les 24 entrées synthétiques de l'essai de mesure)

| instrument | octets de la consigne remplie | jetons d'entrée, compte de Claude | jetons d'entrée, compte de Google |
|---|---|---|---|
| appariement, 18 entrées | 3 092 à 4 468 | 1 092 à 1 565 ; moyenne {{EA}} (23 625 sur 18) | 720 à 1 038 ; moyenne 864 ; {{GA}} sur les six entrées de l'ancienne file du juge |
| couverture, 6 entrées | 8 831 à 21 503 | 3 277 à 7 597 ; moyenne {{EC}} (31 591 sur 6) | 2 125 à 4 834 ; moyenne 3 369 ; {{GC}} sur les deux entrées de l'ancienne file du juge |

- 6.11 : l'entrée d'une lecture d'appariement vaut à peu près sa consigne et trois champs d'une action ; celle d'une lecture de couverture, sa consigne, dix actions et la référence. **Ces longueurs viennent de textes synthétiques** ; celles des textes réels de la course ne sont pas mesurées (S).
- Le découpage de Mistral n'est pas mesuré : l'attendu prend le compte de Claude, le plus haut, comme au devis des essais. Le pire cas prend un jeton par octet du corps, borné ici à 5 000 et 24 000 octets (S ; le programme calcule sur le corps réel).
- Sorties mesurées sur ces entrées, réflexion comprise, à des efforts plus bas : de 49 à 403 jetons pour Carbon et GPT ; jusqu'à 660 et 1 239 pour Claude Haiku 5.5. **Aucune à l'effort le plus haut** (M) : rien n'est donc mesuré au réglage de Mistral Large 4 ni de Neon.

### 3.2 Réglages et sortie maximale

| lecteur | modèle et voie d'accès | réglage, un seul | sortie maximale envoyée à la course |
|---|---|---|---|
| premier lecteur | un modèle Claude [case : identifiant] | « le modèle Claude et le budget des lecteurs », fixés par Lazar sur l'essai de mesure (M : 6.11) [case] | [case] |
| second lecteur | `mistral-large-4-0`, par le point d'accès retenu à la vérification de clé : l'européen s'il sert le modèle, sinon le global, déclaré (M) | `reasoning_effort` à `high`, lu en flux (M) | règle 7 du texte [case, après l'essai d'admission] |
| juge des deux ancres | `gemini-4-neon`, offre payante, deux clés (avenant 1) | niveau de réflexion le plus haut, `xhigh`, lu sans flux (M) | règle 7 du texte et règle permanente des appels à Google (4.4 ; décision 5) [case] |

- **Règle 7 du texte**, telle que le devis des essais d'admission la recopie (sa section 7) : « la plus grande de 8 192 et de quatre fois le maximum observé de la sortie à son essai d'admission, arrondie aux 1 024 supérieurs ».
- Faute de ce maximum, les calculs sont donnés pour 8 192, 16 384 et 32 768 chez Mistral, pour 32 768 et 65 536 chez Neon.
- Réglages et modes de lecture sont ceux des essais d'admission (devis des essais, sections 5.1 à 5.3) ; je les suppose gardés à la course (S) : un modèle est admis à un réglage, et à un seul.

### 3.3 Tarifs comptés (USD par million de jetons ; réflexion comptée au prix de sortie)

| lecteur | entrée | sortie | relevé le | pièce, empreinte, ce qu'on y lit |
|---|---|---|---|---|
| premier lecteur | [case] | [case] | « relevés et datés au devis de l'essai » (M : 6.11) | `devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md`, `533ad5b1…` : nom et empreinte repris du devis des essais d'admission ; pièce hors de ma liste, non ouverte |
| Mistral Large 4, prix de la fiche | 0,70 | 2,10 | 2026-11-21T14:30:44Z | `pages-de-prix-essais-admission-v1/mistral-large-4-0-2026-11-21.html`, `951cc3ff…` : « $0.7 … Input », « $2.1 … Output », « $0.07 … Cached input », par million |
| **Mistral Large 4, point d'accès européen (compté)** | **0,77** | **2,31** | même heure | `…/mistral-regional-inference-2026-11-21.html`, `b501d686…` : « billed at 1.1× standard list pricing (a 10% upcharge) » |
| **`gemini-4-neon`, offre payante, service courant (compté)** | **3** | **15** | même heure | `…/google-gemini-pricing-2026-11-21.html`, `4da10618…` : « Input price … $3.00 », « Output price (including thinking tokens) … $15.00 » |

- **Qui a relevé** : la session de relance a téléchargé ces trois pages (index `…/index-pages-de-prix-v1.md`, `8aeb9f9d…`). J'ai vérifié leurs empreintes contre leurs compagnons et contre l'index, puis lu les prix dans les fichiers, par un programme d'extraction de texte. Ce sont des pages publiques, au contenu modifiable : l'empreinte fixe ce qui a été lu.
- **Réflexion** : facturée en sortie chez Google, c'est écrit sur la page (M). Chez Mistral, non trouvé : supposé au prix de sortie (S), comme au devis des essais.
- **Repli de Mistral sur le point d'accès global** : compté au prix européen, borne haute, comme au devis des essais.
- **Aucune remise n'est comptée** : ni l'entrée en cache (0,07 chez Mistral ; « Context caching price … $0.15 », implicite, chez Google), ni les services à moitié prix de Google (« Batch » et « Flex », 1,50 et 7,50) ; le service prioritaire de Google (5,40 et 27,00) n'est pas employé. Les appels restent synchrones, comme aux essais ; le service par lots de Mistral n'existe pas sur ses points d'accès régionaux (M : page de l'inférence régionale).
- **Dû avant chaque ligne** : les pages relues le jour de l'engagement. Un prix lu au-dessus du prix compté : ce devis est repris.

### 3.4 Formule

`coût = k × [ n_a × (e_a × pe + s_a × ps) + n_c × (e_c × pe + s_c × ps) ] ÷ 1 000 000`

C'est la formule du devis des essais d'admission (sa section 6.3), qui la tient du devis de l'essai de mesure. `n_a`, `n_c` : appels d'appariement et de couverture ; `e` : jetons d'entrée d'un appel ; `s` : jetons de sortie facturés d'un appel, réflexion comprise ; `pe`, `ps` : prix par million ; `k` : envois par appel, en moyenne.

- **Attendu** : entrées mesurées (3.1) ; sorties supposées, 2 000 jetons à l'appariement et 4 000 à la couverture (S : les suppositions du devis des essais, « sans mesure à cet effort ») ; `k` = 1, puis `k` = 1 + 2/24 = {{K_RED}}, « avec redemandes » : c'est le taux de non-conformité le plus haut que l'admission du second lecteur permet, 22 réponses de forme conforme sur 24 (S pour la course).
- **Recoupe** (C) : cette formule rend les attendus du devis des essais d'admission, 0,18 USD pour ses 24 appels à Mistral et 0,34 USD pour ses 8 appels à Neon.

## 4. Un tableau par lecteur

### 4.1 Premier lecteur de l'oracle (un modèle Claude)

| | lots d'épreuve | lots décisifs | lots de la révision | total |
|---|---|---|---|---|
{{T_L1}}

- **Modèle, réglage, sortie maximale, tarif** : [cases]. 6.11 dit seulement que Lazar fixe « le modèle Claude et le budget des lecteurs » sur l'essai de mesure, et que les réglages retenus sont ceux de la règle `runs/essai-mesure-lecteurs-bras-a-v1/regle-de-choix-claude-carbon-v1.json` (`b14b7084…`) : chemin cité par 6.11, cloisonné pour moi, non ouvert.
- **Sorties, réflexion comprise** : « mesurées par l'essai de mesure » (M : 6.11) ; [case]. Le seul chiffre de mes pièces est le maximum cité en 3.1 pour Claude Haiku 5.5 ; rien n'y dit que ce soit le modèle ni le réglage retenus.
- **Attendu** : 6.11 donne « lectures du lecteur 1, ≈ 146,4 USD », projection sur textes synthétiques, « non des dépenses accordées ni des résultats », « à reprendre au devis de la course ». **Je la transcris ; je ne peux pas la refaire** : ses compteurs sont dans des pièces qui me sont fermées. Je lis qu'elle porte sur les 15 136 lectures d'un lecteur, révision et redemandes comprises (grandeur du devis de l'essai de mesure, citée par le devis des essais d'admission, section 7) : à confirmer par la session. Elle fait {{C1_MOYEN}} millièmes de USD par appel (C).
- **Répartition par phase** (C sur S) : elle dépend du rapport entre le coût d'une lecture de couverture et celui d'une lecture d'appariement, que je n'ai pas. Je le borne entre 1 et 4 : le rapport des entrées est de {{RATIO_E}}, celui des sorties est supposé entre 1 et 4. La session la refait au juste avec les deux coûts moyens par instrument.
- **Pire cas tenu par les gardes** : le plafond de la ligne et un envoi coupé, soit {{COEF_COUPE}} × `ps` USD au délai de 2 690 secondes [case]. **Majorant vrai sans les gardes** : {{ENVOIS_LECTEUR}} envois à la sortie maximale pleine [case].

### 4.2 Second lecteur de l'oracle : Mistral Large 4, sous réserve de son essai d'admission

| | lots d'épreuve | lots décisifs | lots de la révision | total |
|---|---|---|---|---|
{{T_L2}}

- **Réflexion** : `reasoning_effort` à `high`, le niveau le plus haut que le modèle accepte et son défaut (M : devis des essais, 5.2). Le compte de la réflexion n'est pas rendu à part chez Mistral ; la sortie facturée la comprend, par supposition (S).
- **Un appel coûte, à ces suppositions** : {{CA_M}} millièmes de USD à l'appariement, {{CC_M}} à la couverture (C). La sortie fait {{PART_SORTIE}} % du coût : **c'est elle qui décide, et elle n'est pas mesurée.**

| sorties moyennes, appariement et couverture | lots d'épreuve | lots décisifs | lots de la révision | total, avec redemandes (C) |
|---|---|---|---|---|
{{T_L2_SENS}}

- **À reprendre sur les compteurs de l'essai d'admission** (M : 6.11, « par la même formule, aux tarifs de `mistral-large-4-0` par la voie d'accès retenue ») : le rapport de cet essai rend le coût projeté des 13 888 et 1 248 lectures, redemandes au taux mesuré (devis des essais, section 7). La session le répartit par phase et recalcule les plafonds par la règle de la section 5.
- **Réserve d'un envoi** (C), en USD. La borne en octets est celle du devis des essais (sa section 6.4) : huit octets par jeton de sortie maximale. La réserve « par la sortie maximale seule » ne vaut que si l'essai d'admission a établi que la sortie maximale borne aussi la réflexion.

| sortie maximale envoyée | borne dure en octets de l'envoi | réserve, par la borne en octets | réserve, par la sortie maximale seule |
|---|---|---|---|
{{T_L2_RES}}

### 4.3 Les lots d'épreuve, lus par les deux lecteurs

| lot, au nom du texte | instrument | appels par lecteur | lectures des deux lecteurs | jetons d'entrée par lecteur, en millions (C) | second lecteur, attendu avec redemandes (C sur S) |
|---|---|---|---|---|---|
{{T_EPR}}

- **Premier lecteur, mêmes lots** : {{L1_LO_EPREUVE}} à {{L1_HI_EPREUVE}} USD (4.1). **Les deux lecteurs ensemble** : 4 992 lectures, {{ENVOIS_EPR_2L}} envois au plus.
- **Ancres** : jugées par `gemini-4-neon` (4.4), 80 appels.
- **En tout, pour les épreuves** : 4 992 lectures des deux lecteurs et 80 appels du juge ; attendu ≈ {{ATT_EPR_LO}} à {{ATT_EPR_HI}} USD ; plafonds {{PL1_EPREUVE}} + {{PL2_EPREUVE}} + {{PLJ_80}} = {{TOT_PL_EPR}} USD ; sorties, réflexion, tarifs et pire cas : ceux de chaque lecteur (4.1, 4.2, 4.4).
- **Ces lots se lisent d'abord** ; les lots décisifs ne se lisent qu'après les épreuves passées selon le texte (consignes permanentes du dépôt : « épreuves avant toute lecture d'un épisode saboté »). Ce sont donc les lignes 1, 4 et 7 de la section 8.

### 4.4 Juge des deux ancres : `gemini-4-neon`, sous réserve de son essai d'admission

| grandeur | valeur | marque |
|---|---|---|
| appels | 80 (« 48 + 24 + 8 ») ; 72 de plus sous la révision ; 152 au plus | M |
| envois au plus | 240 ; 216 de plus sous la révision ; 456 au plus | M |
| jetons d'entrée | {{TOK_JUGE_80}} pour 80 appels, {{TOK_JUGE_152}} pour 152, si 72 appels sont d'appariement et 8 de couverture, puis 72 d'appariement sous la révision | C sur S : répartition inférée, question à la mère |
| jetons de sortie, réflexion comprise | supposés : 2 000 à l'appariement, 4 000 à la couverture ; aucune mesure au niveau `xhigh` | S |
| réflexion | niveau le plus haut, `xhigh`, explicite dans le corps ; facturée au prix de sortie | M |
| tarif | 3 et 15 USD par million (3.3) | M |
| attendu, avec redemandes | {{J_EK_80}} USD pour 80 appels ; {{J_EK_72}} pour les 72 de la révision ; {{J_EK_80C}} et {{J_EK_72C}} si tous les appels ont la longueur d'une lecture de couverture | C sur S |
| **plafond de ce brouillon** | **{{PLJ_80}} USD** pour les 80 appels ; **{{PLJ_72}} USD** au plus pour les 72 de la révision | C |
| pire cas tenu par les gardes | {{PIREJ_80}} USD par ligne : le plafond et un envoi coupé au délai de 2 690 secondes ; {{PIREJ890_80}} à 890 secondes | C |

- **Les plafonds ne dépendent pas de la répartition inférée** : ils comptent chaque appel comme une lecture de couverture. Celui des 80 appels tient jusqu'à une sortie moyenne d'environ {{J_TOL}} jetons par appel (C).
- **Règle permanente des appels à Google** (mot de Lazar du 21 novembre, GO-2026-11-21-71), appliquée au juge. Avant tout envoi, une vérification par code refuse l'envoi si : le réglage de réflexion n'est pas explicite dans le corps (niveau le plus haut admis, ou budget prévu) ; le plafond de sortie n'atteint pas la réflexion plus 16 000 jetons de texte ; la limite de mots de l'invite ne tient pas dans le plafond de texte. Après la réponse : zéro jeton de pensée, fin en `MAX_TOKENS`, `SAFETY`, `RECITATION` ou texte vide = défaut journalisé, jamais une réponse. Une garde commune vit dans `src/controle_ia/` ; le programme de la course l'emploie ou la reproduit, essais et mutations à l'appui (garde 7).
- **Ce que cette règle fait au coût** (C) : la réflexion se règle ici par un niveau, non par un budget chiffré ; sa provision est donc le plafond de sortie moins 16 000 jetons de texte. La consigne du juge doit porter une limite de mots qui tienne dans ces 16 000 jetons : c'est l'affaire du rédacteur du texte.

| plafond de sortie envoyé | provision de réflexion | réserve d'un envoi | majorant vrai, trois envois pleins, 80 appels | 152 appels |
|---|---|---|---|---|
{{T_J_RES}}

- **Un défaut est payé et n'est pas une réponse** : il prend l'un des trois envois de l'appel. Ce que devient une ancre dont les envois sont des défauts n'est pas dans 6.11.
- **La règle 7 du texte peut donner moins que cette règle n'exige** : à 8 192, tout envoi du juge serait refusé par la garde. C'est la décision 5.
- **Deux clés** (avenant 1, version 3 ; GO-2026-11-21-68) : aux essais, la file du juge est partagée par le rang, impairs sous `GEMINI_API_KEY`, pairs sous `GEMINI_API_KEY_2`. L'avenant écrit qu'à la course « le juge devra être servi de la même façon, ou sur une clé que quatre lectures seulement auront éprouvée : à écrire au texte ». Je suppose la même façon, avec un seul compteur et un seul plafond par ligne (S).
- **Chez Google, rien de dur ne borne la perte** : recharge automatique activée, aucun plafond de dépense (GO-2026-11-21-68). Le pire cas accepté, 84,06 USD, vaut pour les lignes des essais. Les deux lignes du juge à la course y ajoutent {{EXPO_J}} USD au régime prudent (C), à accepter à part.

### 4.5 Moniteurs à modèle de langue : volumes et formule seulement (le reste relève du côté habilité)

| moniteur | lectures (M) | jetons d'entrée, ordre de grandeur (C) |
|---|---|---|
| moniteur boîte noire par action en contexte | 5 × 1 280 = **6 400**, « avec raisonnement » ; le devis de course en comptait 8 960 si les deux témoins sont lus | {{TOK_MON}} millions ({{TOK_MON_TEMOINS}} avec les témoins), consigne non comptée |
| juge d'une autre lignée | **6 400** ; « et, au cas B, ses 102 points de lecture par action (13.2) » | {{TOK_MON}} millions, consigne non comptée, s'il lit lui aussi l'action dans son contexte (S) |

- **D'où vient l'ordre de grandeur** : une action lue dans son contexte vaut 2 643 + 223 = 2 866 jetons en moyenne (M : devis de course, section 2, qui le tient de `prereg/T0.6-organismes-v0-v1.md`, ligne 645, relevé d'une autre chaîne ; fichier cloisonné, non ouvert). 6 400 × 2 866 = {{TOK_MON_EXACT}} (C).
- **Formule, tarif en case** : `coût = k × N × [ (2 866 + c) × pe + s × ps ] ÷ 1 000 000`, avec `N` = 6 400 ; `c`, longueur de la consigne ; `s`, sortie facturée d'une lecture, raisonnement compris ; `pe`, `ps`, prix par million ; `k`, envois par appel. **`c`, `s`, `pe`, `ps` et `k` sont des cases du côté habilité.**
- **La même, en clair** (C) : par moniteur, l'entrée coûte {{MON_COEF_E}} × `pe` USD, plus {{MON_COEF_C}} × `c` × `pe` ; la sortie, {{MON_COEF_S}} × `ps` USD par millier de jetons de sortie d'une lecture.
- **Le devis de course ne comptait que l'entrée.** Avec raisonnement, la sortie pèse autant que l'entrée dès {{MON_SEUIL_S}} jetons par lecture, si le prix de sortie vaut cinq fois le prix d'entrée (C).

| prix d'entrée et de sortie, **exemples et non tarifs** | sortie par lecture | entrée, USD | sortie, USD | un moniteur, un envoi par appel (C) |
|---|---|---|---|---|
{{T_MON_EX}}

- **Plafond conditionnel** : celui de la règle de la section 5, appliquée à ce coût : trois fois le coût aux valeurs supposées, deux fois sur une mesure d'au moins 24 lectures au réglage retenu, plus la réserve d'un envoi, arrondi aux 5 USD supérieurs. **Il ne se calcule qu'une fois les cases remplies** ; 6.11 dit que le moniteur a un devis et une ligne de calcul propres, « absents jusqu'ici ».
- **Si un moniteur est un modèle de Google**, la règle permanente de 4.4 s'y applique : la réserve d'un envoi vaut alors au moins la réflexion plus 16 000 jetons au prix de sortie.
- **S'il tourne sur une carte**, c'est une ligne de carte, absente d'ici.

## 5. Plafonds

### 5.1 La règle, écrite d'avance

`plafond = arrondi aux 5 USD supérieurs de [ m × ( n_a × c_a + n_c × c_c ) + r ]`

- `c_a`, `c_c` : coût moyen compté d'un appel, par instrument, tous ses envois compris, à la meilleure mesure disponible pour ce lecteur à son réglage.
- `m`, la marge : **3** si ces coûts sont des suppositions, ou mesurés sur moins de 24 lectures (c'est le cas du juge après son essai d'admission, qui en compte huit) ; **2** s'ils sont mesurés sur 24 lectures au moins, synthétiques ou réelles (essai de mesure ; essai d'admission du second lecteur ; ancres de la ligne 7) ; **1,5** s'ils sont mesurés sur 1 000 lectures réelles au moins du même lecteur (ses lots d'épreuve en comptent 2 496).
- `r`, la réserve d'un envoi : {{RES_M}} USD au plus chez Mistral, {{RES_N}} chez Neon à 65 536, 1,00 supposé pour le premier lecteur [case].
- **Les plafonds de ce brouillon sont des maxima.** Un plafond recalculé le remplace s'il est plus bas ou égal ; s'il est plus haut, la ligne ne part pas : nœud de Lazar, devis repris.
- **Ce que la règle garantit** (C) : une ligne va au bout tant que le coût moyen compté par appel reste sous `m` fois la mesure de référence. Une garde refuse de commencer un lot dont la projection ne tient pas sous le plafond (garde 2) : une ligne s'arrête entre deux lots plutôt qu'au milieu d'un lot.

### 5.2 Les huit lignes du côté de la relance

| n° | ligne | appels | envois au plus | attendu, USD | plafond de ce brouillon, un maximum, USD | pire cas tenu par les gardes, USD |
|---|---|---|---|---|---|---|
{{T_RESUME}}

- **D'où viennent ces plafonds** (C) : premier lecteur, marge de 2 sur le haut de sa fourchette (projection sur textes synthétiques) ; second lecteur et juge, marge de 3 sur des suppositions, le juge étant compté comme s'il ne lisait que des entrées de couverture.
- **Ce qu'ils tolèrent** (C) : au second lecteur, des sorties moyennes jusqu'à {{L2_TOL}} fois la supposition ; au juge, {{J_TOL}} jetons de sortie par appel.
- **Exemple du recalcul** (C) : si les compteurs d'admission de Mistral rendaient juste la supposition, ses trois plafonds seraient {{PL_L2_SUPP2}} USD à la marge de 2 ; puis, les lots d'épreuve rendant la même chose, {{PL2R_DECISIF}} et {{PL2R_REVISION}} USD pour les lots décisifs et la révision, à la marge de 1,5.
- **Sommes** (C) : premier lecteur {{TOT_PL1}} USD ({{TOT_PL1_SANS}} sans la révision) ; second lecteur {{TOT_PL2}} ({{TOT_PL2_SANS}}) ; juge {{TOT_PLJ}} ({{PLJ_80}}) ; ensemble **{{TOT_PL}}**, **{{TOT_PL_SANS}}** sans les trois lignes de la révision ({{TOT_PL_REV}} USD), **{{TOT_PL_EPR}}** pour les lignes 1, 4 et 7.

Les mêmes chiffres, rangés par objet du mandat (C) :

| objet | lectures des deux lecteurs, et appels du juge | attendu, USD | plafonds de ce brouillon, USD | lignes |
|---|---|---|---|---|
{{T_OBJET}}

### 5.3 Ce que ces plafonds bornent

- **Entre les envois, le compteur** (garde 1) : aucun envoi ne part si le cumul compté et sa réserve passent le plafond.
- **Pendant un envoi.** Chez Mistral, lu en flux : la borne dure en octets (garde 8), sous les trois suppositions du devis des essais (sa section 6.4). Chez Google, lu sans flux : rien que le délai.

| délai du relais, secondes | jetons rendus à 200 par seconde (S) | un envoi coupé chez Mistral, USD | chez Google, USD |
|---|---|---|---|
{{T_COUPE}}

- **Pire cas tenu par les gardes : le plafond de la ligne et un envoi coupé**, au régime prudent (décision 2) ; un envoi coupé par appel en vol, si les lectures vont en parallèle (décision 3) : huit chez Mistral font {{PAR8_CM}} USD. Il repose sur trois suppositions non mesurées, celles du devis des essais : le service ne rend pas plus de 200 jetons par seconde ; la coupure d'un envoi arrête la génération et la facturation, ce qui n'est écrit nulle part ; les compteurs d'un envoi fini disent ce qui est facturé. **Si la deuxième manque, aucun chiffre ne vaut** ; la seule parade est la lecture de la console par Lazar après tout envoi coupé (garde 15).
- **Majorant vrai sans les gardes** (C) : trois envois par appel, sortie maximale pleine, un jeton d'entrée par octet. Second lecteur : {{L2_MAJ_8192}} USD à 8 192 de sortie maximale, {{L2_MAJ_16384}} à 16 384, {{L2_MAJ_32768}} à 32 768. Juge, 152 appels : {{J_MAJ152_32768}} USD à 32 768, {{J_MAJ152_65536}} à 65 536. Ce ne sont pas des plafonds : ils disent pourquoi le compteur est la seule borne.
- **Ce qui vérifie ces chiffres du dehors : la facture du fournisseur.** Aucun compteur du programme ne la remplace, et la troisième supposition ne s'éprouve que là. D'où le rapprochement à la clôture de chaque ligne (garde 17) : il éprouve le compte sur environ 2 500 lectures réelles avant la ligne des lots décisifs, quatre fois plus grosse. C'est une lecture de console par Lazar entre deux lignes : mon ajout, que le contre-lecteur ou Lazar peut retirer.
- **Une ligne arrêtée à son plafond.** Ce devis suppose qu'elle reprend sous une ligne nouvelle, au premier appel non servi, sans rejouer un appel servi (S). Le texte le dit peut-être autrement, hors de 6.11 : à vérifier par la session.

## 6. Crédit utilisable à avoir chez chaque fournisseur

Règle du devis des essais (sa section 6.5) : avant chaque ligne, le crédit utilisable couvre son plafond et un envoi coupé ; marge de 15 % pour l'écart entre prix comptés et prix facturés, arrondi au demi-dollar supérieur ; 20 % de plus si une taxe s'ajoute (S).

| fournisseur | ligne | plafond | un envoi coupé | à couvrir | **crédit utilisable à avoir** | paiement si une taxe de 20 % s'ajoute (S) |
|---|---|---|---|---|---|---|
{{T_CREDIT}}

(C. Montants en USD, aux plafonds de ce brouillon ; ils baissent avec les plafonds recalculés.)

- **Mistral** : le mode de paiement du compte n'est pas relevé ; le crédit n'y borne la perte que si le compte est prépayé (M : devis des essais, 6.4). Charger ligne par ligne laisse moins d'argent exposé qu'en une fois : {{CREDIT_M_EPR}} USD avant les lots d'épreuve, puis ce que demandent les plafonds recalculés. Charger est un geste de Lazar.
- **Google** : la règle des seuils de l'avenant 1, version 3 (sa section 4.4) : sur chaque projet, le solde vu en euros, converti au taux diminué de 5 %, plus une recharge automatique, moins la dépense retirée, atteint le seuil de la ligne. **Seuil d'une ligne du juge : {{SEUIL_J_80}} USD.** En euros vus, par exemple : {{SEUIL_J_EUR}} (C). La valeur d'une recharge automatique n'est pas relevée (point ouvert de l'avenant) : sans elle, le solde seul compte. Soldes vus le 21 novembre à 16:24:17Z, avant les essais : 11,93 € et 15,59 € (M : avenant 1).
- **Fournisseur du premier lecteur** : [case]. Même règle : à couvrir, {{PL1_EPREUVE}}, {{PL1_DECISIF}} et {{PL1_REVISION}} USD, chacun plus un envoi coupé.

## 7. Gardes du programme à écrire

Chacune est éprouvée sur un cas sain et sur un artefact, contre un faux fournisseur local, sans appel payant (R5). Toute garde qui coupe écrit son motif et rend un code de sortie non nul : aucun repli silencieux. Les gardes 1, 6 et 8 à 15 reprennent, à l'échelle de la course, celles du devis des essais d'admission (sa section 10) ; les gardes 2 à 5, 7, 16 et 17 sont neuves ou refondues.

| n° | garde | ce qu'elle fait | cas sain | artefact |
|---|---|---|---|---|
| 1 | plafond avant l'envoi | par ligne : refuse l'envoi si le cumul compté, les réserves des envois en vol et la réserve de cet envoi passent le plafond ; un envoi fini est compté à son coût réel, sur la plus grande des deux lectures de ses compteurs ; un envoi sans compteur lisible, à 200 jetons par seconde de sa durée et au moins à sa réserve | cumul bas : l'envoi part | cumul à 0,01 USD du plafond : refus, rien ne part ; envoi coupé à son délai : compté au débit déclaré |
| 2 | arrêt sur projection | avant chaque lot : si le cumul, plus ce lot au coût moyen compté jusque-là par instrument (à la mesure de référence pour le premier lot), passe le plafond, le lot ne commence pas ; la ligne s'arrête entre deux lots, cause écrite | coût moyen sous la mesure de référence : le lot commence | coût moyen au triple : le lot suivant ne commence pas |
| 3 | plafond recalculé | une ligne décisive ou de révision exige le rapport scellé des lots d'épreuve du même lecteur, recalcule son plafond par la règle de 5.1, et refuse de partir s'il passe le maximum de ce devis ou diffère de celui de sa configuration | plafond recalculé de {{PL2R_DECISIF}} pour un maximum de {{PL2_DECISIF}} | rapport absent ; plafond recalculé au-dessus du maximum ; plafond de la configuration différent du calcul |
| 4 | ordre des phases | aucune entrée d'un lot décisif ne part avant les épreuves passées selon le texte, verdict scellé à l'appui ; aucune entrée de la révision sans la révision ouverte | épreuves passées : le lot décisif part | entrée décisive présentée avant le verdict : refus |
| 5 | trois envois, et reprise sans rejeu | trois envois au plus par appel ; relais borné à trois fois les appels de la ligne ; après une interruption, un appel déjà servi n'est jamais renvoyé | réponse au premier envoi | quatrième envoi : impossible ; reprise après interruption : seuls les appels non servis partent |
| 6 | corps de l'appel | le corps porte la sortie maximale de sa ligne et les seuls champs fixés pour ce lecteur ; une fin par sortie maximale atteinte n'est jamais lue comme une réponse | corps conforme | champ de plus ; autre sortie maximale : refus avant l'envoi |
| 7 | règle des appels à Google, par code | avant l'envoi : réflexion explicite ; plafond de sortie au moins égal à la réflexion plus 16 000 jetons de texte ; limite de mots de l'invite tenue dans le plafond de texte. Après la réponse : zéro jeton de pensée, `MAX_TOKENS`, `SAFETY`, `RECITATION`, texte vide = défaut journalisé | corps au niveau `xhigh`, plafond de 65 536, réflexion constatée | corps sans réglage de réflexion ; plafond de 8 192 ; réponse à zéro jeton de pensée ; chacune des quatre fins : défaut, jamais une réponse ; mutations de la garde elle-même |
| 8 | borne dure en octets, chez Mistral | coupe l'envoi quand les octets de contenu reçus passent huit fois la sortie maximale ; l'envoi coupé est compté à sa réserve | flux sous la borne : il va au bout | flux au-delà : coupé, compté, cause écrite |
| 9 | nom servi | chaque réponse porte le nom servi relevé à la vérification de clé ; sinon arrêt de la file ; pour le juge, aucune ancre jugée n'est lue et c'est un nœud de Lazar (son choix du 21 novembre) | nom égal | nom autre sur une seule réponse : arrêt |
| 10 | rôle pourvu, identifiant figé, hôte | la ligne exige le rôle pourvu selon les règles d'admission, relevé de vérification scellé à l'appui, l'identifiant à la lettre et l'hôte de sa ligne ; aucun repli sur un autre modèle | relevé sain, identifiant égal | rôle non pourvu ; `mistral-large-latest` ; autre hôte : rien ne part |
| 11 | ligne de calcul, devis, prix du jour | exige l'identifiant d'une ligne valide de `registres/go.md` qui la nomme, l'empreinte de ce devis accepté, et les pages de prix relues le jour | ligne valide, prix égaux | ligne absente, ou d'un autre lecteur ; prix lu au-dessus du prix compté : rien ne part |
| 12 | conditions d'envoi et crédit | selon la décision 4 : pièce de constat lue, valeurs admises ; crédit au moins égal au seuil de la ligne (section 6) ; chez Google, par projet | pièce conforme, crédit au seuil | pièce absente ; crédit sous le seuil |
| 13 | clés par leur nom, rien de personnel | clés lues par leur nom dans le seul relais ; corps et en-têtes comparés à une liste locale d'interdits ; journaux relus pour toute chaîne de la forme d'une clé | clé factice dans le seul relais | nom absent ; courriel glissé dans un corps : refus |
| 14 | délais et appels en vol | délai par envoi et délai de silence réglés sur les durées des essais d'admission ; jamais plus d'appels en vol que le nombre décidé (décision 3) ; code 429 : attente bornée, puis l'envoi suivant de l'appel | flux lent mais vivant : il va au bout | flux muet : coupé au délai de silence ; un appel de trop en vol : refusé |
| 15 | lecture de la console après un envoi coupé | après un envoi coupé, aucune autre ligne du même fournisseur ne part sans la pièce scellée de la lecture de la console par Lazar ; chez Google, des deux projets | aucun envoi coupé : la ligne suivante part | envoi coupé sans pièce : elle ne part pas |
| 16 | ce qui est gardé | chaque envoi écrit sa ligne au journal avant de partir ; chaque réponse est écrite avant d'être analysée ; le dossier de la ligne est scellé, versé et poussé avant toute suppression | dossier versé, puis nettoyage | suppression demandée avant le versement : refus |
| 17 | rapprochement à la clôture | à la clôture d'une ligne, la dépense comptée est rapprochée de la dépense vue à la console par Lazar, pièce scellée à l'appui ; la ligne suivante du même fournisseur ne part pas sans cette pièce, ni si la dépense vue passe 1,15 fois la dépense comptée | dépense vue sous la dépense comptée : la ligne suivante part | pièce absente ; dépense vue à 1,3 fois la dépense comptée : la ligne suivante ne part pas |

## 8. Lignes de calcul proposées

Dix lignes, à citer telles quelles ; ce qui est entre crochets se remplit d'abord. Aucune n'est demandée ici.

{{LIGNES}}

**Chaque ligne ajoute** : la variable de sa clé, lue par son nom ; le compte qui paie ; le texte scellé en vigueur ; les empreintes de ce devis accepté, des pages de prix relues le jour, du rapport d'admission du lecteur et, si la décision 4 l'exige, de la pièce de constat ; et la phrase « après tout envoi coupé, Lazar lit la console avant toute autre ligne chez ce fournisseur ». Les lignes d'engagement et de clôture au registre des dépenses suivent la forme du devis des essais d'admission (sa section 6.6).

**Pas de ligne de vérification de clé à part.** Les formes d'appel sont établies avant la course : à l'essai de mesure pour le premier lecteur, aux essais d'admission pour les deux autres. Avant chaque ligne, l'appel de liste, gratuit ; puis le nom servi contrôlé à chaque réponse (gardes 9 et 10). Si la session veut un appel de vérification payant, il se compte sous le plafond de sa ligne.

**Ordre.**
1. Les essais d'admission sont joués ; leurs rapports rendent, par instrument, le coût moyen compté d'un appel, le maximum de sortie, le taux de non-conformité et les durées.
2. La session remplit les cases (section 10) ; ce devis est repris en brouillon 2, contre-lu par un autre modèle, ses corrections vérifiées.
3. Le texte est scellé, les rôles pourvus ; le programme est contre-lu, ses gardes éprouvées.
4. Lignes 1, 4 et 7. Puis le rapprochement de la dépense, le recalcul des plafonds, et les lignes 2 et 5. Les lignes 3, 6 et 8 seulement si la révision est ouverte. Les lignes 9 et 10 sont l'affaire du côté habilité.

Le devis de course veut ce devis borné avant la demande de sa ligne 2 : il l'est par les maxima de la section 5, qu'aucun recalcul ne peut passer sans revenir à Lazar. Il écrit aussi que la dépense de carte est perdue si les lectures ne sont pas payées ensuite : en demandant la seconde ligne de carte, dire à Lazar ce que coûteront les lectures des lots décisifs, ≈ {{ATT_DEC}} USD attendus et {{PL_DEC}} USD de plafonds.

**Avec les lignes du registre que le mandat m'a fait lire.** GO-2026-11-21-63 : « toute ligne neuve sur devis porté à Lazar ». GO-2026-11-21-69 : dépenses sur devis accordées pendant douze heures d'autonomie de la mère, jusqu'au 2026-11-22T05:30Z, chaque devis consigné avant la course ; le paiement reste à Lazar. Les lignes ci-dessus sont neuves, demandent des gestes de paiement et dépendent de cinq décisions : je recommande de les porter à Lazar, quelle que soit la fenêtre d'autonomie.

## 9. Décisions pour Lazar

**Décision 1 — Le découpage, et sa taille.**
- **Décision** : demander les lectures hors carte par lecteur et par phase, à des plafonds recalculés sous les maxima de ce brouillon, ou autrement.
- **Enjeu** : ≈ {{ATT_AVEC}} USD attendus et {{TOT_PL}} USD de plafonds du côté de la relance, moniteurs en sus, quand la carte en attend 20 à 25. Aucun plafond « au pire cas » n'existe : le majorant vrai atteint {{L2_MAJ_32768}} USD pour un seul lecteur, à 32 768 jetons de sortie maximale.
- **Option (a)** : huit lignes, par lecteur et par phase ; les lignes décisives au plafond recalculé sur les lots d'épreuve. Avantage : rien de décisif n'est payé avant les épreuves, et sur un coût compté sur textes réels ; premier engagement de {{TOT_PL_EPR}} USD. Inconvénient : huit lignes, et un retour vers Lazar entre les phases, pour le plafond recalculé et la dépense vue à la console.
- **Option (b)** : une ligne par lecteur, à plafond fixe ({{TOT_PL1}}, {{TOT_PL2}} et {{TOT_PLJ}} USD). Avantage : trois lignes. Inconvénient : des plafonds assis sur des textes synthétiques ou des suppositions ; aucune porte de dépense avant le décisif.
- **Option (c)** : réduire le plan de lecture. Avantage : moins cher. Inconvénient : c'est changer le texte ; non chiffré ici.
- **Recommandation** : (a). Confiance : haute sur le découpage, moyenne sur les trois marges (3 ; 2 ; 1,5), qui sont mon choix. Pas de défaut : c'est une dépense.

**Décision 2 — Le régime du compteur à la course.**
- **Décision** : compter tout envoi sans compteur lisible au régime prudent, sur toutes les lignes de la course, ou garder les deux régimes des essais.
- **Enjeu** : au régime courant des essais, un envoi coupé est compté à sa réserve. Si la borne de sortie ne se comportait pas à pleine sortie comme à la sonde de borne de la vérification de clé (devis des essais, section 4.6), chaque appel pourrait porter un excès non compté : pour les 80 appels du juge, jusqu'à 81 envois coupés, soit ≈ {{OUVERT_JUGE}} USD au débit déclaré (C), contre neuf et 76,70 USD aux essais. Et rien de dur ne borne plus chez Google.
- **Option (a)** : régime prudent partout : un envoi sans compteur lisible est compté à 200 jetons par seconde de sa durée, et au moins à sa réserve. Avantage : le plafond et un envoi coupé bornent chaque ligne, sous les suppositions dites. Inconvénient : chez Google, trois envois coupés à 45 minutes ({{CN_2690}} USD chacun) épuisent le plafond de {{PLJ_80}} USD du juge ; la ligne s'arrête et se reprend sous une ligne nouvelle.
- **Option (b)** : les deux régimes des essais. Avantage : une coupure reste comptée bas et garde sa reprise. Inconvénient : le cas ouvert croît avec le nombre d'appels.
- **Recommandation** : (a), et un délai par envoi de 900 secondes chez Google si les durées de l'essai d'admission le permettent : un envoi coupé vaut alors {{CN_890}} USD. Confiance : haute. Défaut sous 48 heures : la recommandation.

**Décision 3 — La cadence.**
- **Décision** : lire en parallèle, jusqu'à huit appels à la fois par lecteur, ou un appel à la fois comme aux essais.
- **Enjeu** : 15 136 appels par lecteur. La durée d'un appel n'est pas mesurée (S) :

| durée d'un appel (S) | un appel à la fois, dix secondes de pause | dont les lots d'épreuve | huit appels à la fois, sans pause | dont les lots d'épreuve |
|---|---|---|---|---|
{{T_DUREE}}

- **Option (a)** : un appel à la fois. Avantage : la cadence des essais ; aucune limite de débit à craindre. Inconvénient : {{DUREE_J_LO}} à {{DUREE_J_HI}} jours par lecteur.
- **Option (b)** : huit appels à la fois. Avantage : {{DUREE_PAR_HI}} heures au plus par lecteur, à ces durées. Inconvénient : il faut des limites de débit relevées d'au moins {{REQ_MIN}} requêtes et environ {{TPM_C}} jetons par minute (C sur S), un compteur qui réserve les envois en vol (garde 1), et que le texte ne fixe pas l'ordre des lectures (non lu) ; le pire cas tenu par les gardes passe d'un envoi coupé à huit, soit {{PAR8_CM}} USD chez Mistral.
- **Recommandation** : (b) pour les deux lecteurs ; le juge, 80 appels, reste lu un appel à la fois. Confiance : moyenne. Défaut sous 48 heures : la recommandation, si le texte ne s'y oppose pas.

**Décision 4 — Les conditions d'envoi des textes réels.**
- **Décision** : exiger, avant le premier envoi de la course, le constat des conditions d'envoi chez chaque fournisseur, ou les tenir pour levées comme aux essais.
- **Enjeu** : les essais n'envoient que des textes synthétiques. La course envoie les actions de l'agent et, aux lectures de couverture, la référence (6.11). Le constat ligne par ligne aux consoles est abandonné (GO-2026-11-21-68) ; ce mot répondait à l'avenant des essais d'admission, dont les textes sont synthétiques. Le partage et la durée des journaux ne sont constatés sur aucun des deux projets de Google (avenant 1, version 3, section 9). La page de prix de Google porte, pour l'offre payante de Neon : « Used to improve our products … No » (M).
- **Option (a)** : constat exigé avant le premier envoi de la course : chez Google, partage des journaux désactivé et journaux à 7 jours, sur les deux projets ; chez Mistral, offre payante, refus de l'entraînement, point d'accès déclaré ; chez le fournisseur du premier lecteur, ce que l'essai de mesure exigeait [case]. Avantage : la condition que Lazar avait choisie le 21 novembre (« b a b go », choix 3 (b)) tient pour les textes réels. Inconvénient : une visite des consoles par Lazar.
- **Option (b)** : levées comme aux essais. Avantage : aucun aller-retour. Inconvénient : des références de tâches peuvent être conservées ou partagées sans qu'on le sache.
- **Recommandation** : (a). Confiance : moyenne ; c'est le choix de Lazar. Pas de défaut.

**Décision 5 — La sortie maximale du juge des deux ancres.**
- **Décision** : fixer la sortie maximale du juge à la plus grande de deux valeurs — celle de la règle 7 du texte, et la réflexion plus 16 000 jetons de texte de la règle permanente des appels à Google — ou autrement.
- **Enjeu** : la règle 7 peut rendre 8 192 ; la garde de la règle permanente refuserait alors tout envoi du juge. La réserve d'un envoi passe de {{J_RES_32768}} à {{J_RES_65536}} USD entre 32 768 et 65 536 (C).
- **Option (a)** : la plus grande des deux, écrite au texte avant son scellement. Avantage : les deux règles tiennent. Inconvénient : un brouillon du texte de plus.
- **Option (b)** : un budget de réflexion chiffré et plus bas, si le service en admet un à la place d'un niveau. Avantage : une sortie maximale plus basse. Inconvénient : ce n'est plus le réglage de l'essai d'admission.
- **Recommandation** : (a). Confiance : haute. Défaut sous 48 heures : la recommandation. Le texte est l'affaire de son rédacteur ; l'avenant 2 au devis des essais, absent de l'arbre, traite peut-être déjà ce point pour l'essai.

## 10. Cases à remplir, et questions

**Questions à la mère** (un volume manque à 6.11) :
1. **Les 80 appels du juge, « 48 + 24 + 8 » : lesquels sont d'appariement, lesquels de couverture ?** J'ai supposé 72 et 8, puis 72 d'appariement sous la révision. Les plafonds n'en dépendent pas ; l'attendu, si.
2. **« Au cas B, ses 102 points de lecture par action » : est-ce 102 appels par action, soit 6 400 × 102 = {{MON_102}} lectures, ou 102 points lus dans un seul appel ?** Je n'ai pas cherché ; la formule de 4.5 prend 6 400.

**Cases de la session de relance** :
1. Premier lecteur : identifiant, réglage, sortie maximale, variable de la clé, fournisseur et crédit ; tarif relevé et daté ; coût moyen compté d'un appel par instrument et taux de redemande au réglage retenu ; la projection de 146,4 USD refaite par phase.
2. Second lecteur, après son essai d'admission : point d'accès retenu ; issue de la sonde de borne ; maximum de sortie, d'où la sortie maximale de la course ; coût moyen compté d'un appel par instrument ; taux de non-conformité ; durées, d'où les délais ; jetons d'entrée comptés par Mistral sur ces entrées.
3. Juge, après son essai d'admission : les mêmes ; la sortie maximale selon la décision 5 ; le service par une ou deux clés ; la limite de mots de sa consigne.
4. Chez Google : la valeur d'une recharge automatique par projet.
5. Ce que le texte dit, hors de 6.11 : d'une ligne arrêtée à son plafond ; de l'ordre des lectures ; d'une réponse en défaut.

**Cases du côté habilité** : pour chaque moniteur, le modèle, le tarif relevé et daté, la longueur de la consigne, la sortie d'une lecture raisonnement compris, les envois par appel ; s'il tourne par appels ou sur une carte ; le sens des « 102 points ».

## 11. Réserves

1. **Premier lecteur** : rien n'est refait. 146,4 USD est une transcription de 6.11 ; sa répartition par phase est une fourchette sur une supposition ; son tarif et son réglage ne sont dans aucune de mes pièces. Le mandat ne permettait de relever une page de prix que chez Mistral ou chez Google, la consigne de lancement interdisait tout réseau, et ce lecteur n'est servi par aucun des deux : je n'ai rien relevé.
2. **Second lecteur et juge** : aucune mesure à leur réglage. L'attendu repose sur 2 000 et 4 000 jetons de sortie, supposés. De la moitié au quadruple de cette supposition, le second lecteur coûte de {{SENS_LO}} à {{SENS_HI}} USD (4.2).
3. **Longueurs** : mesurées sur 24 entrées synthétiques, reprises d'un devis qui les reprend lui-même ; les textes réels peuvent différer ; le découpage de Mistral n'est pas mesuré.
4. **Instrument et phase de chaque lot** : ma lecture de 6.11, recoupée par un seul compte.
5. **Tarifs** : lus dans des pages publiques versées ; la facturation de la réflexion de Mistral n'y est pas écrite.
6. **Marges (3 ; 2 ; 1,5), arrondi aux 5 USD, redemandes à 2 sur 24** : mes choix, que le contre-lecteur peut défaire.
7. **« Pire cas tenu par les gardes »** : sous trois suppositions non mesurées, dont une non documentée (5.3). Chez Google, rien de dur au-delà.
8. **Règles de la course hors de 6.11** : non lues. Ce devis suppose la reprise d'une ligne arrêtée, sans rejeu.
9. **Avenant 1, version 3** : brouillon dans sa lettre (« ni revérifiée ni acceptée ») ; une pièce de vérification existe au dossier, vue par son nom, non ouverte. **Avenant 2 : absent de l'arbre** ; seul existe le mandat de son rédacteur, vu par son nom, non ouvert ; ce nom annonce un plafond de 65 536, d'où les deux valeurs de 4.4.
10. **Durées** : aucune n'est mesurée ; la décision 3 repose sur 30 et 60 secondes par appel, supposées.
11. **Moniteurs** : je ne sais que leurs volumes. Les exemples de 4.5 ne sont pas des tarifs.
12. **La garde commune des appels à Google** (`src/controle_ia/`) n'est pas ouverte : hors de ma liste. Je cite la règle, non son code.
13. **Le devis des essais d'admission** se dit « brouillon 5 » dans sa lettre ; l'index des pages de prix et l'avenant 1 le disent accepté. Je le cite comme il se nomme.
14. **Devise des comptes** : tout est compté en USD. La fiche de Mistral porte un sélecteur entre USD et EUR ; la devise du compte de Mistral n'est pas relevée. Chez Google, les soldes sont vus en euros (avenant 1).

## 12. Ce que j'ai ouvert

Arbre : copie de la branche de la session du bras A, tête `45b8ebcf…`. Empreintes calculées par `sha256sum` ; pour le devis de course, le devis des essais, l'avenant, les pages de prix, leur index et les mots de Lazar, elles sont égales à celles de leurs compagnons.

| pièce | empreinte | ce que j'en ai lu |
|---|---|---|
| le mandat (chemin en tête) | `86c98be8112805ecd1643fe8212b7e39a5a880e3dd8d7a69d5a00f51654127c2` | en entier, empreinte vérifiée avant lecture |
| `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v2.md` | `83240ca61d7c300fc9f4ca802560a6010a2a7c2eb48dd58fe2c214ee03524ecd` | en entier |
| `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md` | `4f91b535ad91581510615c97039a4cae0a96f4d788088b2aff666d4c3d3f97b3` | la seule section 6.11, par la commande du mandat ; aucune recherche dans le texte |
| `…/devis-essais-admission-mistral-neon-bras-a-v1.md` | `421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc` | en entier |
| `…/avenant-1-devis-essais-admission-recharge-et-deux-cles-v3.md` | `5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac` | en entier |
| `…/pages-de-prix-essais-admission-v1/index-pages-de-prix-v1.md` | `8aeb9f9d3ae33a81540324d863c65193b52d03f6e75a4366e27e838bbd15b790` | en entier |
| `…/pages-de-prix-essais-admission-v1/mistral-large-4-0-2026-11-21.html` | `951cc3ff5f3cdd9b83776bfc6d4b4ef6fbe7c48a59c106945539fee6be1b3d36` | par programme : le texte visible de la fiche, ses prix, et quelques chaînes de son code (raisonnement, sortie maximale) |
| `…/pages-de-prix-essais-admission-v1/mistral-regional-inference-2026-11-21.html` | `b501d686c7cff43cf3b9b1c0bf5b4227ff945c6cdf22e808769639bd2c2d5b18` | par programme : le texte de la page |
| `…/pages-de-prix-essais-admission-v1/google-gemini-pricing-2026-11-21.html` | `4da106182cbbb57172ce41eabb09eb0af08798cb4d030dea0ee444870d4554a8` | par programme : la section de Gemini 4 Neon, les lignes qui la précèdent, et des comptes de mots sur la page |
| `…/mots-de-lazar-cinq-choix-lecteur-bras-a-2026-11-20-v1.md` | `93cbc6f4c78d00c5b91ca29e5b300bef345cd7aa46c89db2be6bff95a46d5beb` | en entier |
| `…/mots-de-lazar-compte-google-prepaye-bras-a-2026-11-21-v1.md` | `487b5a725b619b290a82c619a507f23de8ce6f72a0a2ed3b101bdc3168ab9421` | en entier |
| `…/mots-de-lazar-devis-essais-admission-bras-a-2026-11-21-v1.md` | `9b9ee5ca4e89f3dcd8d4c5865f7badf613943f00800b9a80d011bd6f45b1c57b` | en entier |
| `…/mots-de-lazar-juge-des-ancres-neon-bras-a-2026-11-20-v1.md` | `6ebab24f009bbb7587eb14c22ae832f3d93ce5911e832cce087e4afa7c6f9cf2` | en entier |
| `…/mots-de-lazar-juge-et-envoi-des-textes-bras-a-2026-11-21-v1.md` | `00af2aa83604df20181e9ea0fdcf15fbd88601f98f96388ce32d23d7c0a98e5a` | en entier |
| `…/mots-de-lazar-juge-et-point-19-bras-a-2026-11-20-v1.md` | `2845ca37e79361aaff125fb2f01cbcb569257526bae0c8eeaeddef7f61dcf6df` | en entier ; je n'en reprends que le compte de 6 400, que 6.11 porte aussi |
| `…/mots-de-lazar-second-lecteur-et-juge-des-ancres-bras-a-2026-11-20-v1.md` | `8189dcec0f83a74fde8c8b1ac82a74142f946f77dfda41b88e95d547c4534d6a` | en entier |

`…` = `docs/notes/relance-organismes-discrets-v1`.

- **Registre** : `registres/go.md` sur la référence locale `origin/main` (`bf63c169…`), par la seule commande du mandat, pour GO-2026-11-21-63, -68, -69 et -71. La recherche de -69 a rendu aussi les lignes -70 et -73, qui la citent ; celle de -71, la ligne -72 : vues en passant, je n'en fais rien.
- **Consignes permanentes** : la section « Appels aux modèles de Google » de `CLAUDE.md` sur `origin/main`, par la commande du mandat ; et le `CLAUDE.md` du dépôt de travail, reçu au lancement.
- **Listes de noms**, par motifs ciblés dans le dossier de la relance : `mots-de-lazar-*`, `*avenant*`, le devis de course, le devis des essais, son dossier de pages de prix, et le nom de ce devis, pour vérifier qu'il n'existait pas. Le motif `*avenant*` a montré, sans que je les ouvre : les versions 1 et 2 de l'avenant 1, ses deux contre-lectures, la vérification de sa version 3, et le mandat du rédacteur de l'avenant 2.
- **Chemins cloisonnés** : plusieurs pièces permises en citent (`prereg/T0.6-organismes-v0-v1.md`, des chemins sous `runs/`, `docs/notes/bras-a-sans-interne-v1/`). Je recopie ces citations là où elles servent ; **je n'en ai suivi, listé ni empreinté aucun.**
- **Rien d'autre.** Aucun appel réseau, aucune page de prix relevée par moi, aucune clé lue, aucun appel de modèle, aucun sous-agent, aucune dépense ; aucun `git fetch` ; rien scellé, rien committé. Fichier écrit : celui-ci, sans compagnon d'empreinte.
- **Programmes**, dans le bloc-notes de la session, hors du dépôt (`{{BLOC}}`) : `calc_hc1.py` (`{{SHA_CALC}}`), tous les chiffres marqués C ; `extrait_prix.py`, lecture des pages de prix ; `controle_hc1.py`, qui refait 35 de ces chiffres par une autre écriture et les trouve égaux ; `gabarit_hc1.md` et `faire_hc1.py`, qui insèrent dans ce devis les valeurs rendues par `calc_hc1.py`, sans rien recopier à la main.

## 13. Calculs, par programme

Sortie de `calc_hc1.py`, en fractions exactes. Arrondis : au plus proche pour les coûts ; au supérieur pour les réserves et les plafonds.

```
{{TRACE}}
```
