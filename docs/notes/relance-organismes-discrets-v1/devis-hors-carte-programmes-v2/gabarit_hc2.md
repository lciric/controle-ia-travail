# Organismes discrets, bras A (déplacement des contrôles appris sans consigne) — devis des lectures hors carte de la course — v1, BROUILLON 2

- **Objet** : borner ce que coûtent les lectures par modèle de langue faites hors de la carte louée pendant la course du bras A. Le devis de course l'exige à part, écrit et borné avant la demande de sa ligne 2 (`docs/notes/relance-organismes-discrets-v1/devis-bras-a-v2.md`, `83240ca6…`, sections 1, 6 et 9). Ce devis en reprend la section 6.
- **État** : brouillon 2, non scellé (le rédacteur ne scelle rien), non accepté. Il reprend le brouillon 1 (`docs/notes/relance-organismes-discrets-v1/devis-lectures-hors-carte-bras-a-v1-brouillon1.md`, `70adb048…`, laissé inchangé) après sa vérification par un agent Claude Opus 5.5 (`docs/notes/relance-organismes-discrets-v1/verification-devis-lectures-hors-carte-brouillon1-v1.md`, `b0f04bd5…` : « engageable après corrections », sept corrections, huit mineurs). Il porte aussi l'avenant 2 au devis des essais d'admission (`docs/notes/relance-organismes-discrets-v1/avenant-2-devis-essais-admission-plafond-google-65536-v1.md`, `5f84642a…`, brouillon non contre-lu), absent de l'arbre au brouillon 1. Les corrections restent à vérifier par le même contre-lecteur. **Aucune dépense n'est ouverte ; aucune ligne de calcul n'est demandée ici.**
- **En tête, pour Lazar** : aucun plafond ne change — {{TOT_PL}} USD en huit lignes, {{TOT_PL_EPR}} au premier engagement — et l'attendu non plus (≈ {{ATT_AVEC}} USD). Ce qui change : **six décisions au lieu de cinq** ; la décision 5, la sortie maximale du juge, est refaite sur l'avenant 2 et n'a plus de défaut ; la décision 6 est neuve : le pire cas et le versement chez Google ; les maxima des lignes 4 et 7 ne valent que sous une sortie maximale de course d'au plus {{SMAX_L4}} et {{SMAX_L7}} jetons ; la marge des plafonds se lit par instrument ; huit textes de lignes de calcul sont récrits.
- **Auteur** : le rédacteur du brouillon 1 (Claude Fable 5.2), le {{DATE}} (`date -u`), sur le même mandat, `docs/notes/relance-organismes-discrets-v1/mandat-redacteur-fable-devis-lectures-hors-carte-v1.md` (`86c98be8…`), relu en entier. Il n'a lu aucune pièce du côté habilité ; il n'a écrit ni le texte du bras A, ni les devis et avenants cités, ni la vérification, ni un programme de la course.
- **Marques** : **M** = relevé sur une pièce citée ; **C** = calculé ici, par programme (section 13) ; **S** = supposé, sans mesure ni pièce ; **[case]** = valeur à remplir, par la session de relance ou par le côté habilité.
- **Mots** : un **appel** est une lecture demandée ; un **envoi** est une tentative d'un appel. Le texte en permet trois par appel : l'envoi, une reprise s'il est resté sans réponse, une redemande de forme. Un **envoi coupé** est un envoi dont le programme ne voit pas la fin : coupé par un délai, par sa borne en octets, ou par une connexion coupée en route. La **réserve** d'un envoi est ce que le compteur retient avant de le laisser partir. Au **régime prudent**, un envoi sans compteur lisible est compté à 200 jetons par seconde de sa durée, et au moins à sa réserve (devis des essais d'admission, section 6.4).

## Corrections depuis le brouillon 1 : remarque → correction

Les remarques sont celles de la vérification (`b0f04bd5…`), sous ses numéros. « Où » renvoie aux sections de ce brouillon. Tous les chiffres, anciens et neufs, sont refaits par programme (section 13).

| remarque de la vérification | correction dans ce brouillon | où |
|---|---|---|
| **C-1.** L'avenant 2 est entré dans l'arbre après le brouillon 1 ; la décision 5 est posée sans lui ; le pire cas accepté chez Google change. | Avenant 2 lu en entier ; ceux de ses chiffres que je reprends sont refaits sur ses entrées. **Décision 5 refaite** : la sortie maximale du juge à la course est la plus grande de la règle 7 du texte et de la borne de réflexion déclarée plus 16 000 jetons, sous `outputTokenLimit` ; elle n'a plus de défaut. La fin de 4.4 et la réserve 9 sont récrites. | 3.2, 4.4, 9, 11 |
| **C-2.** La marge de 1,5 ne peut pas valoir pour la couverture, mesurée sur 320 lectures seulement aux lots d'épreuve. | La marge se lit par instrument : aux lignes décisives, 1,5 pour l'appariement (2 176 lectures réelles), 2 pour la couverture (320). Exemple du recalcul : {{PL2R_DECISIF}} et {{PL2R_REVISION}} USD. Les maxima ne changent pas. **Sa lettre n'est pas reprise telle quelle** : « moins de 24 lectures de cet instrument » mettrait à 3 les deux instruments après un essai de 18 et 6 lectures, contre la marge de 2 que C-6 écrit aux lignes 1 et 4. Le seuil de 24 reste lu sur l'essai entier ; celui de 1 000 se lit par instrument. | 5.1, 5.2, lignes 2 et 5 |
| **C-3.** Les maxima des lignes 4 et 7 ne tiennent que sous une sortie maximale de course que la règle 7 du texte peut dépasser. | Écrit en 5.1 et aux deux lignes : {{SMAX_L4}} jetons au plus chez Mistral, {{SMAX_L7}} chez le juge ; au-delà, la ligne ne part pas : nœud de Lazar. La garde 3 le vérifie. Deux précisions de ma part : {{R7_MAX_M}} et {{R7_MAX_J}} ne bornent la règle 7 que si la sortie maximale de l'essai borne la sortie observée ; et le seuil de Mistral tient à la réserve par la borne en octets, celle du compteur des essais. | 3.2, 4.2, 4.4, 5.1, garde 3, lignes 4 et 7 |
| **C-4.** La ligne 7 ne dit ni la sortie maximale, ni le niveau de réflexion, ni la lecture sans flux. Sous un niveau, la règle des appels à Google se vérifie sur une borne de réflexion déclarée, que le devis ne nomme pas, pas plus que le contrôle de `outputTokenLimit`. | Ligne 7 récrite. Garde 7 complétée : borne de réflexion déclarée à la configuration, `outputTokenLimit` lu avant tout envoi, `CONTINUATION` parmi les fins en défaut. | 4.4, garde 7, ligne 7 |
| **C-5.** La règle des appels à Google est absente des lignes 9 et 10, celles des moniteurs. | Clause ajoutée aux deux lignes ; ce que la règle exige d'un moniteur servi par Google est écrit en 4.5. | 4.5, lignes 9 et 10 |
| **C-6.** Aux lignes 1, 4, 7 et 8, « ramené à 2 (ou 3) fois la projection » oublie la réserve d'un envoi et l'arrondi de la règle : un plafond ainsi ramené pourrait arrêter une ligne saine. | « Ramené par la règle 5.1 », réserve et arrondi compris, aux quatre lignes. Lignes 2 et 5 : marge par instrument ; ligne 2 : pire cas et prix en cases. **Le texte proposé pour la ligne 1 fait {{SIGNES_1_VERIF}} signes à mon compte, non 545 : je l'ai resserré.** Mes textes font {{SIGNES_1}}, {{SIGNES_2}}, {{SIGNES_4}}, {{SIGNES_5}}, {{SIGNES_7}} et {{SIGNES_8}} signes aux lignes 1, 2, 4, 5, 7 et 8, comptés par programme ; aucune des dix lignes ne passe 600. | 8 |
| **C-7.** Il manque une décision sur le pire cas sans borne dure et sur le versement chez Google pour les lignes du juge. | **Décision 6, neuve**, sans défaut : c'est un paiement. | 6, 9 |
| **m-1.** « Environ 14 900 » en 4.4 et 5.2, 14 994 en section 13. | {{J_TOL}} partout : la valeur du programme, au jeton inférieur, à la réserve exacte de 1,05504 USD. La vérification trouve 14 990 avec la réserve arrondie à 1,06 ; je n'écris pas « environ 15 000 », que le plafond ne tient pas. | 4.4, 5.2 |
| **m-2.** 6.11 écrit « 160 artefacts : 32 par lecteur et par épreuve » pour quatre épreuves, quand son tableau compte 128 appels par lecteur. | Porté en question à la mère, avec son enjeu : à 160 appels, les lignes 1 et 4 passeraient leur maximum. | 2, 10 |
| **m-3.** Le tableau d'exemples de 4.5 prend « 3 et 15 », le tarif de Neon : il peut se lire comme un indice. | Plus aucun prix d'exemple : le coût d'un moniteur est donné par USD de prix d'entrée et de prix de sortie. La vérification proposait des prix ronds ; un prix rond peut être le tarif du premier lecteur, que je ne connais pas. | 4.5 |
| **m-4.** « S'il lit lui aussi l'action dans son contexte » suppose l'entrée d'un moniteur. | L'entrée d'une lecture du juge d'une autre lignée devient une case du côté habilité. Je ne garde que la longueur que le devis de course lui comptait. | 4.5, ligne 10 |
| **m-5.** La limite de mots de la consigne du juge est l'affaire d'un lecteur habilité à lire les consignes, non du rédacteur du texte (avenant 2). | Corrigé. | 4.4 |
| **m-6.** `CONTINUATION` manque aux fins en défaut de la garde 7. | Ajouté, avec C-4. | garde 7 |
| **m-7.** Le « pire cas tenu par les gardes » compte l'envoi coupé entier ; l'avenant 2 n'en compte que l'excès sur la réserve. | Dit, non changé : {{PIREJ_EXCES}} USD à la manière de l'avenant 2, {{PIREJ_80}} ici, plus prudent. | 5.3 |
| **m-8.** Citer le brouillon 44 du texte, dont la section 6.11 est identique. | Cité sur la foi de la vérification : mon mandat nomme le brouillon 43, je n'ai pas ouvert le 44. | 2, 12 |
| **Point 4.** Le premier lecteur : ce qui manque, la pièce qui le porte, et qui le remplit. | Repris aux cases de la session : c'est la session de relance qui remplit ; rien n'y relève du côté habilité ; une page de prix d'Anthropic est à relever le jour. | 10 |
| **Point 5.** Mes deux questions. | Réponses de la session du bras A. Sur les 80 appels du juge, 72 servent l'appariement et 8 la couverture, par inférence de 6.11 : la marque « supposé » tombe. « 102 points de lecture par action » se tranche à la section 13.2 du texte, puis chez les agents habilités de la mère : la ligne 10 le garde en case conditionnelle. | 2, 4.4, 4.5, 10 |
| **Point 7.** Un défaut sous 48 heures aux décisions 2 et 3 est admissible. | Inchangé. | 9 |

**Ce que j'ajoute sans que la vérification le demande**, à vérifier comme le reste :
1. **Huit appels à la fois** (décision 3, option recommandée). La règle de 5.1 ne compte qu'une réserve ; le compteur en retient huit. La marge utile de la ligne 4 tombe alors de 3 à {{MULT8_32768}} fois l'attendu ; son pire cas tenu par les gardes passe de {{PIRE2_EPREUVE}} à {{PIRE2V_EPREUVE}} USD ; le crédit à avoir chez Mistral, de {{CREDIT_M_EPR}} à {{CREDIT_M8_EPREUVE}} USD (5.1, 5.3, 6, lignes 4 à 6, décision 3, réserve 15).
2. **Chez Google, le crédit à avoir suit la règle des avenants** : le solde seul de chaque projet, converti au taux diminué de 5 %. Le tableau du brouillon 1 lui appliquait la marge de 15 % du devis des essais (32,50 USD), que les avenants ont remplacée (section 6).
3. **La page de prix de Google** dit, de Neon : « long-decode generation up to 1M tokens ». Ce n'est pas `outputTokenLimit` ; c'est le seul indice que j'aie sur la sortie maximale du modèle (décision 5).
4. **Le débit qu'une sortie pleine demande** pour finir dans le délai de 45 minutes, à chaque sortie maximale du juge (4.4).

## 0. En une page

1. **Les lectures hors carte coûtent de l'ordre de dix fois la carte.** Du côté de la relance, attendu ≈ {{ATT_AVEC}} USD avec les lots de la révision, ≈ {{ATT_SANS_LO}} à {{ATT_SANS_HI}} sans eux : ≈ 146 pour le premier lecteur (projection du texte, transcrite, non refaite ici), ≈ {{L2_EK_AVEC_0}} pour Mistral Large 4 (sorties supposées), ≈ {{J_EK_152_0}} pour le juge des deux ancres. Les deux lignes de carte : ≈ 20 à 25 USD attendus (M : devis de course, section 5).
2. **Plafonds de ce brouillon : {{TOT_PL}} USD en huit lignes**, {{TOT_PL_SANS}} sans les trois lignes de la révision, qui ne jouent que si la révision est ouverte. Le premier engagement — lots d'épreuve des deux lecteurs, ancres du juge — fait {{TOT_PL_EPR}} USD de plafonds pour ≈ {{ATT_EPR_LO}} à {{ATT_EPR_HI}} attendus. Les lignes décisives ne partent qu'après, à un plafond recalculé par programme sur le coût compté aux lots d'épreuve, jamais au-dessus des maxima écrits ici (section 5). **Ces maxima supposent une sortie maximale de course d'au plus {{SMAX_L4}} jetons chez Mistral et {{SMAX_L7}} chez le juge** (5.1).
3. **Aucun plafond « au pire cas » n'est praticable.** Trois envois par appel à la sortie maximale pleine font {{L2_MAJ_8192}} à {{L2_MAJ_32768}} USD pour le seul second lecteur (C). Ce qui borne la dépense est le compteur du programme : au pire, le plafond d'une ligne et un envoi coupé ({{CM_2690}} USD chez Mistral, {{CN_2690}} chez Google), sous les suppositions du devis des essais d'admission, dont l'une n'est pas documentée : que la coupure d'un envoi arrête la génération et la facturation.
4. **Les volumes ont changé depuis le devis de course.** Le texte, brouillon 43, compte 25 920 lectures des deux lecteurs (30 272 avec la révision), 152 appels du juge au plus, et 6 400 lectures pour chacun des deux moniteurs à modèle de langue. En entrée, à un envoi par appel et sans les consignes des moniteurs : ≈ {{TOT_TOK_SANS}} à {{TOT_TOK_AVEC}} millions de jetons (C), contre « au moins 33 à 35 millions » au devis de course.
5. **Trois choses manquent, et sont dites.** (a) Le tarif et le réglage du premier lecteur ne sont dans aucune pièce qui m'est ouverte : ce sont des cases pour la session. (b) Mistral Large 4 et `gemini-4-neon` ne sont mesurés à leur réglage dans aucune de mes pièces : leur attendu repose sur les sorties supposées du devis des essais d'admission, et se refait par la formule dès que leurs compteurs existent. (c) Le modèle, la consigne et le tarif des moniteurs relèvent du côté habilité : je n'en donne que les volumes, une formule et un plafond conditionnel. Avec raisonnement, un moniteur peut coûter autant qu'un lecteur (4.5).
6. **Six décisions pour Lazar** (section 9) : le découpage et sa taille ; le régime du compteur ; la cadence ; les conditions d'envoi des textes réels ; la sortie maximale du juge ; le pire cas et le versement chez Google. Seules les décisions 2 et 3 ont un défaut sous 48 heures ; la décision 5 perd le sien.
7. **Chez Google, rien de dur ne borne la perte.** Les deux lignes du juge ajoutent {{EXPO_J}} USD, au régime prudent, au pire cas des essais, que l'avenant 2 porte à {{AV2_PIRE}} USD quand Lazar en a accepté {{ACCEPTE}} (4.4 ; décision 6).
8. **Questions** (section 10). La répartition des appels du juge a sa réponse. Le sens de « 102 points de lecture par action » reste une case conditionnelle, à trancher du côté habilité. Une question est neuve : « 160 artefacts », ou 128 appels.

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
- 6.11 écrit « quatre épreuves mécaniques de la couverture (160 artefacts : 32 par lecteur et par épreuve) » : je garde le compte de son tableau, 128 appels par lecteur, que son majorant des envois reprend. L'écart est porté en question (section 10).
- **Juge des deux ancres** (M) : « 48 + 24 + 8 appels du juge ; 72 de plus sous la révision », soit 80 appels, 152 au plus. Selon la session du bras A, par inférence de 6.11 : 72 servent l'appariement et 8 la couverture ; la révision n'ajoute que de l'appariement.
- **Majorant des envois** (M) : 3 × (25 920 + 4 352 + 152) = 91 272.
- **Moniteurs** (M) : moniteur boîte noire par action en contexte, 5 × 1 280 = 6 400 lectures avec raisonnement ; juge d'une autre lignée, 6 400, « et, au cas B, ses 102 points de lecture par action (13.2) ».
- **Brouillon 44 du texte** : la vérification constate que sa section 6.11 (`b30aa902…`) est identique, octet pour octet, à celle du brouillon 43. Je ne l'ai pas ouvert : mon mandat nomme le brouillon 43.

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
| second lecteur | `mistral-large-4-0`, par le point d'accès retenu à la vérification de clé : l'européen s'il sert le modèle, sinon le global, déclaré (M) | `reasoning_effort` à `high`, lu en flux (M) | règle 7 du texte ; {{SMAX_L4}} au plus pour que les maxima de ce devis tiennent [case, après l'essai d'admission] |
| juge des deux ancres | `gemini-4-neon`, offre payante, deux clés (avenant 1) | niveau de réflexion le plus haut, `xhigh`, lu sans flux, sous une borne de réflexion déclarée (M : devis des essais ; avenant 2) | la plus grande de la règle 7 du texte et de la borne de réflexion déclarée plus 16 000 jetons, sous `outputTokenLimit` ; {{SMAX_L7}} au plus pour que le maximum de la ligne 7 tienne (4.4 ; décision 5) [case] |

- **Règle 7 du texte**, telle que le devis des essais d'admission la recopie (sa section 7) : « la plus grande de 8 192 et de quatre fois le maximum observé de la sortie à son essai d'admission, arrondie aux 1 024 supérieurs ».
- **Ce qu'elle peut rendre** (C) : de {{R7_MIN}} à {{R7_MAX_M}} chez Mistral, dont l'essai se joue à 32 768 ; de {{R7_MIN}} à {{R7_MAX_J}} chez le juge, dont l'essai se joue à {{SMAX_ESSAI_J}} (avenant 2). Davantage si la sortie maximale de l'essai ne borne pas la sortie observée : c'est ce que dit, avant chaque file, la sonde de borne de la vérification de clé (devis des essais, 4.6).
- Faute du maximum observé, les calculs sont donnés pour 8 192, 16 384, 32 768, {{SMAX_L4}} et {{R7_MAX_M}} chez Mistral ; pour {{SMAX_ESSAI_J}}, {{SMAX_L7}} et {{R7_MAX_J}} chez Neon.
- Réglages et modes de lecture sont ceux des essais d'admission (devis des essais, sections 5.1 à 5.3 ; avenant 2 pour la sortie maximale de Google) ; je les suppose gardés à la course (S) : un modèle est admis à un réglage, et à un seul.

### 3.3 Tarifs comptés (USD par million de jetons ; réflexion comptée au prix de sortie)

| lecteur | entrée | sortie | relevé le | pièce, empreinte, ce qu'on y lit |
|---|---|---|---|---|
| premier lecteur | [case] | [case] | « relevés et datés au devis de l'essai » (M : 6.11) | `devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md`, `533ad5b1…` : nom et empreinte repris du devis des essais d'admission ; pièce hors de ma liste, non ouverte |
| Mistral Large 4, prix de la fiche | 0,70 | 2,10 | 2026-11-21T14:30:44Z | `pages-de-prix-essais-admission-v1/mistral-large-4-0-2026-11-21.html`, `951cc3ff…` : « $0.7 … Input », « $2.1 … Output », « $0.07 … Cached input », par million |
| **Mistral Large 4, point d'accès européen (compté)** | **0,77** | **2,31** | même heure | `…/mistral-regional-inference-2026-11-21.html`, `b501d686…` : « billed at 1.1× standard list pricing (a 10% upcharge) » |
| **`gemini-4-neon`, offre payante, service courant (compté)** | **3** | **15** | même heure | `…/google-gemini-pricing-2026-11-21.html`, `4da10618…` : « Input price … $3.00 », « Output price (including thinking tokens) … $15.00 » |

- **Qui a relevé** : la session de relance a téléchargé ces trois pages (index `…/index-pages-de-prix-v1.md`, `8aeb9f9d…`). J'ai vérifié de nouveau leurs empreintes contre leurs compagnons et contre l'index, puis relu les prix dans les fichiers, par programme. Ce sont des pages publiques, au contenu modifiable : l'empreinte fixe ce qui a été lu.
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
- **Réserve d'un envoi** : [case]. Le maximum de la ligne 1 tient tant qu'elle ne passe pas {{RES1_MAX}} USD (C).
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
{{T_L2_RES5}}

- **{{SMAX_L4}} est la sortie maximale la plus haute que le maximum de la ligne 4 tolère** (réserve de {{RES_M_SEUIL}} USD) ; {{R7_MAX_M}}, la plus haute que la règle 7 peut rendre si l'essai borne la sortie observée (5.1).

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
| jetons d'entrée | {{TOK_JUGE_80}} pour 80 appels, {{TOK_JUGE_152}} pour 152 : 72 appels d'appariement et 8 de couverture, puis 72 d'appariement sous la révision | C sur M : répartition donnée par la session du bras A, par inférence de 6.11 |
| jetons de sortie, réflexion comprise | supposés : 2 000 à l'appariement, 4 000 à la couverture ; aucune mesure au niveau `xhigh` | S |
| réflexion | niveau le plus haut, `xhigh`, explicite dans le corps, sous une borne de réflexion déclarée à la configuration ({{BORNE_DECL}} jetons à l'essai, supposée) ; facturée au prix de sortie | M : devis des essais ; avenant 2 |
| tarif | 3 et 15 USD par million (3.3) | M |
| attendu, avec redemandes | {{J_EK_80}} USD pour 80 appels ; {{J_EK_72}} pour les 72 de la révision ; {{J_EK_80C}} et {{J_EK_72C}} si tous les appels ont la longueur d'une lecture de couverture | C sur S |
| **plafond de ce brouillon** | **{{PLJ_80}} USD** pour les 80 appels ; **{{PLJ_72}} USD** au plus pour les 72 de la révision | C |
| pire cas tenu par les gardes | {{PIREJ_80}} USD par ligne : le plafond et un envoi coupé au délai de 2 690 secondes ; {{PIREJ890_80}} à 890 secondes | C |

- **Les plafonds ne dépendent pas de la répartition** : ils comptent chaque appel comme une lecture de couverture. Celui des 80 appels tient jusqu'à une sortie moyenne de {{J_TOL}} jetons par appel (C). Si 24 des 72 appels étaient de couverture, l'attendu serait de {{J_EK_80_ALT}} USD au lieu de {{J_EK_80}} (C).
- **Règle permanente des appels à Google** (mot de Lazar du 21 novembre, GO-2026-11-21-71), appliquée au juge. Avant tout envoi, une vérification par code refuse l'envoi si : le réglage de réflexion n'est pas explicite dans le corps (niveau le plus haut admis, ou budget prévu) ; le plafond de sortie n'atteint pas la réflexion plus 16 000 jetons de texte ; la limite de mots de l'invite ne tient pas dans le plafond de texte. Après la réponse : zéro jeton de pensée, fin en `MAX_TOKENS`, `SAFETY`, `RECITATION` ou texte vide = défaut journalisé, jamais une réponse. Une garde commune vit dans `src/controle_ia/` ; le programme de la course l'emploie ou la reproduit, essais et mutations à l'appui (garde 7).
- **Sous un niveau, la règle se vérifie sur une borne déclarée** (M : avenant 2, section 4). Un niveau de réflexion n'a pas de borne écrite : le programme exige une borne de réflexion déclarée à la configuration, et refuse l'envoi si le plafond de sortie n'atteint pas cette borne plus 16 000. À l'essai : plafond de {{SMAX_ESSAI_J}}, borne de {{BORNE_DECL}}, « supposée, non relevée ». La garde d'avant l'envoi vérifie alors une soustraction ; ce qui protège, ce sont les défauts d'après la réponse. `outputTokenLimit`, rendu par l'appel de liste, se lit avant tout envoi : s'il est sous le plafond, rien ne part.
- **Ce que cette règle fait au coût** (C) : la réserve d'un envoi vaut {{J_RES_ENTREE}} + 15 × S ÷ 1 000 000 USD pour une sortie maximale de S jetons. La limite de mots de la consigne du juge et le rapport de jetons par mot sont à inscrire à la configuration par un lecteur habilité à lire les consignes (avenant 2, sections 4 et 9) ; contrainte : limite × rapport ≤ plafond de texte.

| plafond de sortie envoyé, jetons | borne de réflexion déclarée, au plus | réserve d'un envoi, USD | débit qu'une sortie pleine demande pour finir en 2 690 secondes, jetons par seconde | majorant vrai, trois envois pleins, 80 appels, USD | 152 appels, USD |
|---|---|---|---|---|---|
{{T_J_RES}}

- {{SMAX_ESSAI_J}} est le plafond de l'essai ; {{SMAX_L7}}, le plus haut que le maximum de la ligne 7 tolère ; {{R7_MAX_J}}, le plus haut que la règle 7 peut rendre si l'essai borne la sortie observée. Aucun de ces débits n'est mesuré (S) ; l'avenant 2 écrit le premier.
- **Un défaut est payé et n'est pas une réponse** : il prend l'un des trois envois de l'appel. `CONTINUATION`, que le devis des essais range avec la sortie maximale atteinte (sa section 5.5), se compte de même. Ce que devient une ancre dont les envois sont des défauts n'est pas dans 6.11.
- **La règle 7 du texte peut rendre moins, ou plus, que ce que ces garde-fous admettent** : sous {{SMAX_ESSAI_J}}, la garde refuse tout envoi du juge tant que la borne déclarée reste {{BORNE_DECL}} ; au-dessus de {{SMAX_L7}}, le maximum de la ligne 7 ne tient plus. C'est la décision 5.
- **Deux clés** (avenant 1, version 3 ; GO-2026-11-21-68) : aux essais, la file du juge est partagée par le rang, impairs sous `GEMINI_API_KEY`, pairs sous `GEMINI_API_KEY_2`. L'avenant écrit qu'à la course « le juge devra être servi de la même façon, ou sur une clé que quatre lectures seulement auront éprouvée : à écrire au texte ». Je suppose la même façon, avec un seul compteur et un seul plafond par ligne (S).
- **Chez Google, rien de dur ne borne la perte** : recharge automatique activée, aucun plafond de dépense (GO-2026-11-21-68). Lazar a accepté {{ACCEPTE}} USD pour les essais ; l'avenant 2 les porte à {{AV2_PIRE}} sans borne dure, {{AV2_PRUDENT}} au régime prudent (M). Les deux lignes du juge à la course y ajoutent {{EXPO_J}} USD au régime prudent (C) : {{EXPO_PIRE}} et {{EXPO_PRUDENT}} avec les essais. C'est la décision 6.

### 4.5 Moniteurs à modèle de langue : volumes et formule seulement (le reste relève du côté habilité)

| moniteur | lectures (M) | jetons d'entrée, ordre de grandeur |
|---|---|---|
| moniteur boîte noire par action en contexte | 5 × 1 280 = **6 400**, « avec raisonnement » ; le devis de course en comptait 8 960 si les deux témoins sont lus | {{TOK_MON}} millions ({{TOK_MON_TEMOINS}} avec les témoins), consigne non comptée (C sur M) |
| juge d'une autre lignée | **6 400** ; « et, au cas B, ses 102 points de lecture par action (13.2) » | entrée d'une lecture : [case du côté habilité]. À la longueur que le devis de course lui comptait — « ≈ 7 millions » de jetons pour 2 560 lectures, soit celle du moniteur par action —, {{TOK_MON}} millions, consigne non comptée (C sur M) |

- **D'où vient l'ordre de grandeur** : une action lue dans son contexte vaut 2 643 + 223 = 2 866 jetons en moyenne (M : devis de course, section 2, qui le tient de `prereg/T0.6-organismes-v0-v1.md`, ligne 645, relevé d'une autre chaîne ; fichier cloisonné, non ouvert). 6 400 × 2 866 = {{TOK_MON_EXACT}} (C).
- **Formule, tarif en case** : `coût = k × N × [ (e + c) × pe + s × ps ] ÷ 1 000 000`, avec `N` = 6 400 ; `e`, entrée d'une lecture hors consigne : 2 866 pour le moniteur par action en contexte (M), case pour le juge d'une autre lignée ; `c`, longueur de la consigne ; `s`, sortie facturée d'une lecture, raisonnement compris ; `pe`, `ps`, prix par million ; `k`, envois par appel. **`c`, `s`, `pe`, `ps` et `k` sont des cases du côté habilité.**
- **La même, en clair** (C), pour `e` = 2 866 : par moniteur, l'entrée coûte {{MON_COEF_E}} × `pe` USD, plus {{MON_COEF_C}} × `c` × `pe` ; la sortie, {{MON_COEF_S}} × `ps` USD par millier de jetons de sortie d'une lecture.
- **Le devis de course ne comptait que l'entrée.** Avec raisonnement, la sortie pèse autant que l'entrée dès {{MON_SEUIL_S3}} jetons par lecture si le prix de sortie vaut trois fois le prix d'entrée, {{MON_SEUIL_S4}} s'il vaut quatre fois, {{MON_SEUIL_S5}} s'il vaut cinq fois (C).

| sortie d'une lecture, jetons | coût de sortie d'un moniteur, par USD de prix de sortie par million, un envoi par appel (C) |
|---|---|
{{T_MON_UNIT}}

- **Aucun prix n'est donné en exemple** : un prix rond pourrait passer pour un tarif. Par USD de prix d'entrée par million, l'entrée d'un moniteur coûte {{MON_COEF_E}} USD, consigne non comptée (C).
- **Plafond conditionnel** : celui de la règle de la section 5, appliquée à ce coût : trois fois le coût aux valeurs supposées, deux fois sur une mesure d'au moins 24 lectures au réglage retenu, plus la réserve d'un envoi, arrondi aux 5 USD supérieurs. **Il ne se calcule qu'une fois les cases remplies** ; 6.11 dit que le moniteur a un devis et une ligne de calcul propres, « absents jusqu'ici ».
- **« 102 points de lecture par action » : case conditionnelle.** Selon la session du bras A, cela se tranche à la section 13.2 du texte, puis chez les agents habilités de la mère. Enjeu (C) : 102 appels par action feraient {{MON_102}} lectures et, à 2 866 jetons par lecture, {{MON_102_TOK}} milliard de jetons d'entrée, cent deux fois le poste. La ligne 10 ne chiffre rien avant la réponse.
- **Si un moniteur est un modèle de Google**, la règle permanente de 4.4 s'y applique entière : réglage de réflexion explicite dans le corps ; sous un niveau, borne de réflexion déclarée à la configuration ; plafond de sortie au moins égal à cette borne plus 16 000 jetons de texte, et sous `outputTokenLimit` ; limite de mots de la consigne tenue dans le plafond de texte ; après la réponse, zéro jeton de pensée, `MAX_TOKENS`, `SAFETY`, `RECITATION` ou texte vide = défaut journalisé, `CONTINUATION` compté comme `MAX_TOKENS`. La réserve de sortie d'un envoi vaut alors au moins la borne plus 16 000 jetons au prix de sortie : à la borne de l'essai du juge, {{MON_RES_G}} × `ps` USD (C). Les lignes 9 et 10 le portent.
- **S'il tourne sur une carte**, c'est une ligne de carte, absente d'ici.

## 5. Plafonds

### 5.1 La règle, écrite d'avance

`plafond = arrondi aux 5 USD supérieurs de [ m_a × n_a × c_a + m_c × n_c × c_c + r ]`

- `c_a`, `c_c` : coût moyen compté d'un appel, par instrument, tous ses envois compris, à la meilleure mesure disponible pour ce lecteur à son réglage.
- `m_a`, `m_c`, la marge, **par instrument** :
  - **3** tant que le lecteur n'est mesuré, à son réglage, sur aucun essai d'au moins 24 lectures : coûts supposés, ou juge après son essai d'admission, qui en compte huit ;
  - **2** dès qu'il l'est sur 24 lectures au moins, les deux instruments ensemble, synthétiques ou réelles : essai de mesure et essai d'admission du second lecteur (18 lectures d'appariement et 6 de couverture), ancres de la ligne 7 (72 et 8) ;
  - **1,5** pour l'instrument mesuré sur 1 000 lectures réelles au moins **de cet instrument**, par le même lecteur, au même réglage. Les lots d'épreuve en comptent 2 176 d'appariement et 320 de couverture : aux lignes décisives et de révision, l'appariement passe à 1,5 et **la couverture reste à 2**.
- `r`, la réserve d'un envoi : {{RES_M}} USD chez Mistral pour une sortie maximale de 32 768, {{RES_N}} chez Neon à {{SMAX_ESSAI_J}}, 1,00 supposé pour le premier lecteur [case]. Elle croît avec la sortie maximale (4.2, 4.4).
- **Les plafonds de ce brouillon sont des maxima.** Un plafond recalculé le remplace s'il est plus bas ou égal ; s'il est plus haut, la ligne ne part pas : nœud de Lazar, devis repris.
- **Ces maxima supposent une sortie maximale de course d'au plus {{SMAX_L4}} jetons chez Mistral et {{SMAX_L7}} chez le juge** (C), soit un maximum observé à l'essai d'admission d'au plus {{OBS_M}} et {{OBS_J}} jetons. Au-delà, la réserve d'un envoi fait passer les maxima des lignes 4 et 7 : à la valeur la plus haute de la règle 7, {{R7_MAX_M}} et {{R7_MAX_J}}, la règle rendrait {{PL4_R7}} et {{PL7_R7}} USD. Si la règle 7 rend plus de {{SMAX_L4}} chez Mistral ou de {{SMAX_L7}} chez le juge, la ligne ne part pas : nœud de Lazar, devis repris. La garde 3 le vérifie. Le seuil de Mistral tient à la réserve par la borne en octets, celle du compteur des essais : si l'essai établit que la sortie maximale borne aussi la réflexion, et si le compteur de la course réserve alors par la sortie maximale seule (4.2), la ligne 4 tient à {{PL2_EPREUVE}} USD jusqu'à {{R7_MAX_M}} ; ce devis ne s'y appuie pas. Les maxima des lignes 5, 6 et 8 tiennent jusqu'à {{SMAX_L5}}, {{SMAX_L6}} et {{SMAX_L8}} jetons. Pour le premier lecteur, le maximum de la ligne 1 suppose une réserve d'un envoi d'au plus {{RES1_MAX}} USD [case].
- **Ce que la règle garantit** (C) : à un appel à la fois, une ligne va au bout tant que, pour chaque instrument, le coût moyen compté par appel reste sous sa marge fois la mesure de référence. Une garde refuse de commencer un lot dont la projection ne tient pas sous le plafond (garde 2) : une ligne s'arrête entre deux lots plutôt qu'au milieu d'un lot.
- **À huit appels à la fois** (décision 3), le compteur retient huit réserves, et la marge utile baisse (C). La ligne 4 va au bout tant que le cumul compté reste sous {{CUM8_32768}} USD, soit {{MULT8_32768}} fois l'attendu, pour une sortie maximale de 32 768 ; sous {{CUM8_SEUIL}} USD, soit {{MULT8_SEUIL}} fois, à {{SMAX_L4}}.

### 5.2 Les huit lignes du côté de la relance

| n° | ligne | appels | envois au plus | attendu, USD | plafond de ce brouillon, un maximum, USD | pire cas tenu par les gardes, USD |
|---|---|---|---|---|---|---|
{{T_RESUME}}

- **D'où viennent ces plafonds** (C) : premier lecteur, marge de 2 sur le haut de sa fourchette (projection sur textes synthétiques) ; second lecteur et juge, marge de 3 sur des suppositions, le juge étant compté comme s'il ne lisait que des entrées de couverture.
- **Ce qu'ils tolèrent** (C) : au second lecteur, des sorties moyennes jusqu'à {{L2_TOL}} fois la supposition à un appel à la fois, {{TOL8_32768}} fois à huit ; au juge, {{J_TOL}} jetons de sortie par appel.
- **Exemple du recalcul** (C) : si les compteurs d'admission de Mistral rendaient juste la supposition, ses trois plafonds seraient {{PL_L2_SUPP2}} USD à la marge de 2 ; puis, les lots d'épreuve rendant la même chose, {{PL2R_DECISIF}} et {{PL2R_REVISION}} USD pour les lots décisifs et la révision, à 1,5 pour l'appariement et 2 pour la couverture.
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

- **Pire cas tenu par les gardes : le plafond de la ligne et un envoi coupé**, au régime prudent (décision 2) ; un envoi coupé par appel en vol, si les lectures vont en parallèle (décision 3) : huit chez Mistral font {{PAR8_CM}} USD, soit {{PIRE2V_EPREUVE}}, {{PIRE2V_DECISIF}} et {{PIRE2V_REVISION}} USD aux lignes 4, 5 et 6. Il repose sur trois suppositions non mesurées, celles du devis des essais : le service ne rend pas plus de 200 jetons par seconde ; la coupure d'un envoi arrête la génération et la facturation, ce qui n'est écrit nulle part ; les compteurs d'un envoi fini disent ce qui est facturé. **Si la deuxième manque, aucun chiffre ne vaut** ; la seule parade est la lecture de la console par Lazar après tout envoi coupé (garde 15).
- **Ce pire cas est compté large.** L'avenant 2 ne compte, pour un envoi coupé, que son excès sur la réserve, que le compteur retient déjà : une ligne du juge ferait {{PIREJ_EXCES}} USD au lieu de {{PIREJ_80}} (C). Je garde le compte le plus prudent.
- **Majorant vrai sans les gardes** (C) : trois envois par appel, sortie maximale pleine, un jeton d'entrée par octet. Second lecteur : {{L2_MAJ_8192}} USD à 8 192 de sortie maximale, {{L2_MAJ_16384}} à 16 384, {{L2_MAJ_32768}} à 32 768. Juge, 152 appels : {{J_MAJ152_65536}} USD à {{SMAX_ESSAI_J}}, {{J_MAJ152_262144}} à {{R7_MAX_J}}. Ce ne sont pas des plafonds : ils disent pourquoi le compteur est la seule borne.
- **Ce qui vérifie ces chiffres du dehors : la facture du fournisseur.** Aucun compteur du programme ne la remplace, et la troisième supposition ne s'éprouve que là. D'où le rapprochement à la clôture de chaque ligne (garde 17) : il éprouve le compte sur environ 2 500 lectures réelles avant la ligne des lots décisifs, quatre fois plus grosse. C'est une lecture de console par Lazar entre deux lignes : mon ajout, que le contre-lecteur ou Lazar peut retirer.
- **Une ligne arrêtée à son plafond.** Ce devis suppose qu'elle reprend sous une ligne nouvelle, au premier appel non servi, sans rejouer un appel servi (S). Le texte le dit peut-être autrement, hors de 6.11 : à vérifier par la session.

## 6. Crédit utilisable à avoir chez chaque fournisseur

**Chez Mistral**, la règle du devis des essais (sa section 6.5) : avant chaque ligne, le crédit utilisable couvre son plafond et un envoi coupé ; marge de 15 % pour l'écart entre prix comptés et prix facturés, arrondi au demi-dollar supérieur ; 20 % de plus si une taxe s'ajoute (S).

| fournisseur | ligne | plafond | envois coupés | à couvrir | **crédit utilisable à avoir** | paiement si une taxe de 20 % s'ajoute (S) |
|---|---|---|---|---|---|---|
{{T_CREDIT}}

(C. Un appel à la fois. Montants en USD, aux plafonds de ce brouillon ; ils baissent avec les plafonds recalculés.)

| fournisseur | ligne | plafond | envois coupés | à couvrir | **crédit utilisable à avoir** | paiement si une taxe de 20 % s'ajoute (S) |
|---|---|---|---|---|---|---|
{{T_CREDIT8}}

(C. Huit appels à la fois, option recommandée de la décision 3 : huit envois coupés au plus.)

- **Mistral** : le mode de paiement du compte n'est pas relevé ; le crédit n'y borne la perte que si le compte est prépayé (M : devis des essais, 6.4). Charger ligne par ligne laisse moins d'argent exposé qu'en une fois : {{CREDIT_M_EPR}} USD avant les lots d'épreuve à un appel à la fois, {{CREDIT_M8_EPREUVE}} à huit, puis ce que demandent les plafonds recalculés. Charger est un geste de Lazar.

**Chez Google**, la règle des avenants (avenant 1, version 3, section 4.4 ; avenant 2, section 3.1) a remplacé la marge de 15 % : sur chacun des deux projets, `plancher au centime de [ solde vu en euros × t × 0,95 ]`, moins la dépense retirée, atteint le seuil de la ligne. La recharge automatique n'est pas comptée ; tant que la pièce de constat ne dit pas les deux clés sur deux projets différents, la dépense retirée est la somme des dépenses comptées sous les deux clés depuis cette pièce (M : avenant 2).

| ligne | plafond, USD | envois coupés, USD | seuil compté, par projet, USD | solde à voir, par projet, au taux relevé |
|---|---|---|---|---|
{{T_CREDIT_G}}

(C. Taux relevé par l'avenant 2 : 1,0990 USD pour 1 €, fixage du 2026-11-20, soit {{T95}} après la marge de 5 %. Le solde à voir se refait au taux de la pièce de constat : seuil ÷ (t × 0,95), au centime supérieur.)

- **Le seuil d'une ligne du juge est de {{SEUIL_J_80}} USD comptés, soit {{EUR_J}} € vus sur chaque projet** au taux relevé (C).
- **Aux soldes vus avant les essais**, 11,93 € et 15,59 € le 21 novembre à 16:24:17Z (M : avenant 1), il manquerait {{MANQUE_A}} € et {{MANQUE_B}} €, soit {{MANQUE_TOT}} € (C).
- **Si chaque projet est porté à {{EUR_AV2}} €**, comme l'avenant 2 le recommande pour que ses trois lignes passent même au pire, son crédit compté est de {{CC_AV2}} USD : la ligne 7 passe son seuil sans versement neuf tant que les essais n'ont pas compté plus de {{MARGE_ESSAIS}} USD chez Google ; leur attendu y est de {{ATT_ESSAIS_G}} USD (C sur M). Au pire des essais, tout est à verser de nouveau.
- **Ligne 8** : le même seuil, la dépense comptée à la ligne 7 retirée, ou une pièce de constat neuve.
- **La recharge automatique reste activée** (GO-2026-11-21-68) : chaque recharge est un paiement sans geste de Lazar, d'un montant qui n'est pas relevé, et qui ne compte pour aucun seuil (M : avenant 2, section 8). Un versement fait à la main demande une pièce de constat neuve.
- **Fournisseur du premier lecteur** : [case]. Même règle que chez Mistral : à couvrir, {{PL1_EPREUVE}}, {{PL1_DECISIF}} et {{PL1_REVISION}} USD, chacun plus un envoi coupé par appel en vol.

## 7. Gardes du programme à écrire

Chacune est éprouvée sur un cas sain et sur un artefact, contre un faux fournisseur local, sans appel payant (R5). Toute garde qui coupe écrit son motif et rend un code de sortie non nul : aucun repli silencieux. Les gardes 1, 6 et 8 à 15 reprennent, à l'échelle de la course, celles du devis des essais d'admission (sa section 10) ; les gardes 2 à 5, 7, 16 et 17 sont neuves ou refondues. Depuis le brouillon 1 : les gardes 3, 7 et 12 changent.

| n° | garde | ce qu'elle fait | cas sain | artefact |
|---|---|---|---|---|
| 1 | plafond avant l'envoi | par ligne : refuse l'envoi si le cumul compté, les réserves des envois en vol et la réserve de cet envoi passent le plafond ; un envoi fini est compté à son coût réel, sur la plus grande des deux lectures de ses compteurs ; un envoi sans compteur lisible, à 200 jetons par seconde de sa durée et au moins à sa réserve | cumul bas : l'envoi part | cumul à 0,01 USD du plafond : refus, rien ne part ; envoi coupé à son délai : compté au débit déclaré |
| 2 | arrêt sur projection | avant chaque lot : si le cumul, plus ce lot au coût moyen compté jusque-là par instrument (à la mesure de référence pour le premier lot), passe le plafond, le lot ne commence pas ; la ligne s'arrête entre deux lots, cause écrite | coût moyen sous la mesure de référence : le lot commence | coût moyen au triple : le lot suivant ne commence pas |
| 3 | plafond recalculé, et sortie maximale | une ligne décisive ou de révision exige le rapport scellé des lots d'épreuve du même lecteur, recalcule son plafond par la règle de 5.1, marge par instrument, et refuse de partir s'il passe le maximum de ce devis ou diffère de celui de sa configuration ; toute ligne du second lecteur ou du juge refuse de partir si la sortie maximale de sa configuration n'est pas celle que rend la règle en vigueur sur le rapport d'admission scellé (règle 7 du texte ; pour le juge, décision 5), ou si elle passe {{SMAX_L4}} chez Mistral, {{SMAX_L7}} chez le juge | plafond recalculé de {{PL2R_DECISIF}} pour un maximum de {{PL2_DECISIF}} ; sortie maximale de 16 384 chez Mistral | rapport absent ; plafond recalculé au-dessus du maximum ; plafond de la configuration différent du calcul ; couverture recalculée à 1,5 sur 320 lectures ; sortie maximale de {{R7_MAX_M}} chez Mistral ou de {{R7_MAX_J}} chez le juge : la ligne ne part pas |
| 4 | ordre des phases | aucune entrée d'un lot décisif ne part avant les épreuves passées selon le texte, verdict scellé à l'appui ; aucune entrée de la révision sans la révision ouverte | épreuves passées : le lot décisif part | entrée décisive présentée avant le verdict : refus |
| 5 | trois envois, et reprise sans rejeu | trois envois au plus par appel ; relais borné à trois fois les appels de la ligne ; après une interruption, un appel déjà servi n'est jamais renvoyé | réponse au premier envoi | quatrième envoi : impossible ; reprise après interruption : seuls les appels non servis partent |
| 6 | corps de l'appel | le corps porte la sortie maximale de sa ligne et les seuls champs fixés pour ce lecteur ; une fin par sortie maximale atteinte n'est jamais lue comme une réponse | corps conforme | champ de plus ; autre sortie maximale : refus avant l'envoi |
| 7 | règle des appels à Google, par code | avant l'envoi : réflexion explicite ; sous un niveau de réflexion, le plafond se contrôle sur la borne de réflexion déclarée à la configuration ; plafond de sortie au moins égal à cette borne plus 16 000 jetons de texte ; `outputTokenLimit` lu avant tout envoi, au moins égal au plafond ; limite de mots de l'invite tenue dans le plafond de texte. Après la réponse : zéro jeton de pensée, `MAX_TOKENS`, `CONTINUATION`, `SAFETY`, `RECITATION`, texte vide = défaut journalisé | corps au niveau `xhigh`, plafond de {{SMAX_ESSAI_J}}, borne déclarée de {{BORNE_DECL}}, réflexion constatée | corps sans réglage de réflexion ; plafond de 8 192 ; configuration sans borne déclarée ; `outputTokenLimit` sous le plafond : rien ne part ; réponse à zéro jeton de pensée ; chacune des cinq fins : défaut, jamais une réponse ; mutations de la garde elle-même |
| 8 | borne dure en octets, chez Mistral | coupe l'envoi quand les octets de contenu reçus passent huit fois la sortie maximale ; l'envoi coupé est compté à sa réserve | flux sous la borne : il va au bout | flux au-delà : coupé, compté, cause écrite |
| 9 | nom servi | chaque réponse porte le nom servi relevé à la vérification de clé ; sinon arrêt de la file ; pour le juge, aucune ancre jugée n'est lue et c'est un nœud de Lazar (son choix du 21 novembre) | nom égal | nom autre sur une seule réponse : arrêt |
| 10 | rôle pourvu, identifiant figé, hôte | la ligne exige le rôle pourvu selon les règles d'admission, relevé de vérification scellé à l'appui, l'identifiant à la lettre et l'hôte de sa ligne ; aucun repli sur un autre modèle | relevé sain, identifiant égal | rôle non pourvu ; `mistral-large-latest` ; autre hôte : rien ne part |
| 11 | ligne de calcul, devis, prix du jour | exige l'identifiant d'une ligne valide de `registres/go.md` qui la nomme, l'empreinte de ce devis accepté, et les pages de prix relues le jour | ligne valide, prix égaux | ligne absente, ou d'un autre lecteur ; prix lu au-dessus du prix compté : rien ne part |
| 12 | conditions d'envoi et crédit | selon la décision 4 : pièce de constat lue, valeurs admises ; crédit au moins égal au seuil de la ligne (section 6) ; chez Google, par projet, sur le solde seul converti au taux diminué de 5 %, dépense retirée | pièce conforme, crédit au seuil ; chez Google, {{EUR_J}} € vus sur chaque projet | pièce absente ; crédit sous le seuil ; chez Google, un projet à {{EUR_J_MOINS}} € vus, qui comptent pour {{CC_J_MOINS}} USD : la ligne du juge ne part pas |
| 13 | clés par leur nom, rien de personnel | clés lues par leur nom dans le seul relais ; corps et en-têtes comparés à une liste locale d'interdits ; journaux relus pour toute chaîne de la forme d'une clé | clé factice dans le seul relais | nom absent ; courriel glissé dans un corps : refus |
| 14 | délais et appels en vol | délai par envoi et délai de silence réglés sur les durées des essais d'admission ; jamais plus d'appels en vol que le nombre décidé (décision 3) ; code 429 : attente bornée, puis l'envoi suivant de l'appel | flux lent mais vivant : il va au bout | flux muet : coupé au délai de silence ; un appel de trop en vol : refusé |
| 15 | lecture de la console après un envoi coupé | après un envoi coupé, aucune autre ligne du même fournisseur ne part sans la pièce scellée de la lecture de la console par Lazar ; chez Google, des deux projets | aucun envoi coupé : la ligne suivante part | envoi coupé sans pièce : elle ne part pas |
| 16 | ce qui est gardé | chaque envoi écrit sa ligne au journal avant de partir ; chaque réponse est écrite avant d'être analysée ; le dossier de la ligne est scellé, versé et poussé avant toute suppression | dossier versé, puis nettoyage | suppression demandée avant le versement : refus |
| 17 | rapprochement à la clôture | à la clôture d'une ligne, la dépense comptée est rapprochée de la dépense vue à la console par Lazar, pièce scellée à l'appui ; la ligne suivante du même fournisseur ne part pas sans cette pièce, ni si la dépense vue passe 1,15 fois la dépense comptée | dépense vue sous la dépense comptée : la ligne suivante part | pièce absente ; dépense vue à 1,3 fois la dépense comptée : la ligne suivante ne part pas |

## 8. Lignes de calcul proposées

Dix lignes, à citer telles quelles ; ce qui est entre crochets se remplit d'abord. Aucune n'est demandée ici. Depuis le brouillon 1 : les lignes 1, 2, 4, 5, 7, 8, 9 et 10 sont récrites ; les lignes 3 et 6 ne changent pas.

{{LIGNES}}

**Chaque ligne ajoute** : la variable de sa clé, lue par son nom ; le compte qui paie ; le texte scellé en vigueur ; les empreintes de ce devis accepté, des pages de prix relues le jour, du rapport d'admission du lecteur et, si la décision 4 l'exige, de la pièce de constat ; pour les lignes du juge, celles de la pièce de constat des soldes et du relevé du taux ; et la phrase « après tout envoi coupé, Lazar lit la console avant toute autre ligne chez ce fournisseur ». Les lignes d'engagement et de clôture au registre des dépenses suivent la forme du devis des essais d'admission (sa section 6.6).

**Pas de ligne de vérification de clé à part.** Les formes d'appel sont établies avant la course : à l'essai de mesure pour le premier lecteur, aux essais d'admission pour les deux autres. Avant chaque ligne, l'appel de liste, gratuit ; puis le nom servi contrôlé à chaque réponse (gardes 9 et 10). Si la session veut un appel de vérification payant, il se compte sous le plafond de sa ligne.

**Ordre.**
1. Les essais d'admission sont joués ; leurs rapports rendent, par instrument, le coût moyen compté d'un appel, le maximum de sortie, le taux de non-conformité et les durées ; pour le juge, le plus grand compte de pensée.
2. La session remplit les cases (section 10) ; ce devis est repris avec elles, puis vérifié par le même contre-lecteur.
3. Le texte est scellé, les rôles pourvus ; le programme est contre-lu, ses gardes éprouvées.
4. Lignes 1, 4 et 7. Puis le rapprochement de la dépense, le recalcul des plafonds, et les lignes 2 et 5. Les lignes 3, 6 et 8 seulement si la révision est ouverte. Les lignes 9 et 10 sont l'affaire du côté habilité.

Le devis de course veut ce devis borné avant la demande de sa ligne 2 : il l'est par les maxima de la section 5, qu'aucun recalcul ne peut passer sans revenir à Lazar. Il écrit aussi que la dépense de carte est perdue si les lectures ne sont pas payées ensuite : en demandant la seconde ligne de carte, dire à Lazar ce que coûteront les lectures des lots décisifs, ≈ {{ATT_DEC}} USD attendus et {{PL_DEC}} USD de plafonds.

**Avec les lignes du registre que le mandat m'a fait lire.** GO-2026-11-21-63 : « toute ligne neuve sur devis porté à Lazar ». GO-2026-11-21-69 : dépenses sur devis accordées pendant douze heures d'autonomie de la mère, jusqu'au 2026-11-22T05:30Z, chaque devis consigné avant la course ; le paiement reste à Lazar. Les lignes ci-dessus sont neuves, demandent des gestes de paiement et dépendent de six décisions, dont quatre sans défaut : je recommande de les porter à Lazar, quelle que soit la fenêtre d'autonomie. La vérification juge cette recommandation juste.

## 9. Décisions pour Lazar

**Décision 1 — Le découpage, et sa taille.**
- **Décision** : demander les lectures hors carte par lecteur et par phase, à des plafonds recalculés sous les maxima de ce brouillon, ou autrement.
- **Enjeu** : ≈ {{ATT_AVEC}} USD attendus et {{TOT_PL}} USD de plafonds du côté de la relance, moniteurs en sus, quand la carte en attend 20 à 25. Aucun plafond « au pire cas » n'existe : le majorant vrai atteint {{L2_MAJ_32768}} USD pour un seul lecteur, à 32 768 jetons de sortie maximale.
- **Option (a)** : huit lignes, par lecteur et par phase ; les lignes décisives au plafond recalculé sur les lots d'épreuve. Avantage : rien de décisif n'est payé avant les épreuves, et sur un coût compté sur textes réels ; premier engagement de {{TOT_PL_EPR}} USD. Inconvénient : huit lignes, et un retour vers Lazar entre les phases, pour le plafond recalculé et la dépense vue à la console.
- **Option (b)** : une ligne par lecteur, à plafond fixe ({{TOT_PL1}}, {{TOT_PL2}} et {{TOT_PLJ}} USD). Avantage : trois lignes. Inconvénient : des plafonds assis sur des textes synthétiques ou des suppositions ; aucune porte de dépense avant le décisif.
- **Option (c)** : réduire le plan de lecture. Avantage : moins cher. Inconvénient : c'est changer le texte ; non chiffré ici.
- **Recommandation** : (a). Confiance : haute sur le découpage, moyenne sur les marges (3 ; 2 ; 1,5, par instrument), qui sont mon choix. Pas de défaut : c'est une dépense.

**Décision 2 — Le régime du compteur à la course.**
- **Décision** : compter tout envoi sans compteur lisible au régime prudent, sur toutes les lignes de la course, ou garder les deux régimes des essais.
- **Enjeu** : au régime courant des essais, un envoi coupé est compté à sa réserve. Si la borne de sortie ne se comportait pas à pleine sortie comme à la sonde de borne de la vérification de clé (devis des essais, section 4.6), chaque appel pourrait porter un excès non compté : pour les 80 appels du juge, jusqu'à 81 envois coupés, soit ≈ {{OUVERT_JUGE}} USD au débit déclaré (C) ; aux essais, neuf envois, et une borne de {{AV2_NEUF}} USD plafond compris (M : avenant 2). Et rien de dur ne borne plus chez Google.
- **Option (a)** : régime prudent partout : un envoi sans compteur lisible est compté à 200 jetons par seconde de sa durée, et au moins à sa réserve. Avantage : le plafond et un envoi coupé bornent chaque ligne, sous les suppositions dites. Inconvénient : chez Google, trois envois coupés à 45 minutes ({{CN_2690}} USD chacun) épuisent le plafond de {{PLJ_80}} USD du juge ; la ligne s'arrête et se reprend sous une ligne nouvelle.
- **Option (b)** : les deux régimes des essais. Avantage : une coupure reste comptée bas et garde sa reprise. Inconvénient : le cas ouvert croît avec le nombre d'appels.
- **Recommandation** : (a), et un délai par envoi de 900 secondes chez Google si les durées de l'essai d'admission le permettent : un envoi coupé vaut alors {{CN_890}} USD. Confiance : haute. Défaut sous 48 heures : la recommandation.

**Décision 3 — La cadence.**
- **Décision** : lire en parallèle, jusqu'à huit appels à la fois par lecteur, ou un appel à la fois comme aux essais.
- **Enjeu** : 15 136 appels par lecteur. La durée d'un appel n'est pas mesurée (S) :

| durée d'un appel (S) | un appel à la fois, dix secondes de pause | dont les lots d'épreuve | huit appels à la fois, sans pause | dont les lots d'épreuve |
|---|---|---|---|---|
{{T_DUREE}}

- **Option (a)** : un appel à la fois. Avantage : la cadence des essais ; aucune limite de débit à craindre ; la marge entière de la règle. Inconvénient : {{DUREE_J_LO}} à {{DUREE_J_HI}} jours par lecteur.
- **Option (b)** : huit appels à la fois. Avantage : {{DUREE_PAR_HI}} heures au plus par lecteur, à ces durées. Inconvénient : il faut des limites de débit relevées d'au moins {{REQ_MIN}} requêtes et environ {{TPM_C}} jetons par minute (C sur S), un compteur qui réserve les envois en vol (garde 1), et que le texte ne fixe pas l'ordre des lectures (non lu) ; le pire cas tenu par les gardes passe d'un envoi coupé à huit, soit {{PAR8_CM}} USD chez Mistral ; la marge utile de la ligne 4 tombe de 3 à {{MULT8_32768}} fois l'attendu (5.1).
- **Recommandation** : (b) pour les deux lecteurs ; le juge, 80 appels, reste lu un appel à la fois. Confiance : moyenne. Défaut sous 48 heures : la recommandation, si le texte ne s'y oppose pas.

**Décision 4 — Les conditions d'envoi des textes réels.**
- **Décision** : exiger, avant le premier envoi de la course, le constat des conditions d'envoi chez chaque fournisseur, ou les tenir pour levées comme aux essais.
- **Enjeu** : les essais n'envoient que des textes synthétiques. La course envoie les actions de l'agent et, aux lectures de couverture, la référence (6.11). Le constat ligne par ligne aux consoles est abandonné (GO-2026-11-21-68) ; ce mot répondait à l'avenant des essais d'admission, dont les textes sont synthétiques. Le partage et la durée des journaux ne sont constatés sur aucun des deux projets de Google (avenant 1, version 3, section 9). La page de prix de Google porte, pour l'offre payante de Neon : « Used to improve our products … No » (M).
- **Option (a)** : constat exigé avant le premier envoi de la course : chez Google, partage des journaux désactivé et journaux à 7 jours, sur les deux projets ; chez Mistral, offre payante, refus de l'entraînement, point d'accès déclaré ; chez le fournisseur du premier lecteur, ce que l'essai de mesure exigeait [case]. Avantage : la condition que Lazar avait choisie le 21 novembre (« b a b go », choix 3 (b)) tient pour les textes réels. Inconvénient : une visite des consoles par Lazar.
- **Option (b)** : levées comme aux essais. Avantage : aucun aller-retour. Inconvénient : des références de tâches peuvent être conservées ou partagées sans qu'on le sache.
- **Recommandation** : (a). Confiance : moyenne ; c'est le choix de Lazar. Pas de défaut.

**Décision 5 — La sortie maximale du juge des deux ancres à la course.**
- **Décision** : fixer la sortie maximale du juge à la plus grande de deux valeurs — celle de la règle 7 du texte, et la borne de réflexion déclarée plus 16 000 jetons de texte (règle permanente des appels à Google) —, sous `outputTokenLimit` relevé par l'appel de liste ; ou autrement.
- **Enjeu** : l'essai d'admission se joue à {{SMAX_ESSAI_J}}, au niveau de réflexion le plus haut, sous une borne déclarée de {{BORNE_DECL}} jetons, supposée (M : avenant 2, sections 1 et 4). La règle 7 peut rendre de {{R7_MIN}} à {{R7_MAX_J}}, tant que l'essai borne la sortie observée (C). Sous {{SMAX_ESSAI_J}}, la garde de la règle permanente refuse tout envoi du juge, tant que la borne déclarée reste {{BORNE_DECL}}. Au-dessus de {{SMAX_L7}}, le maximum de {{PLJ_80}} USD de la ligne 7 ne tient plus (C). Au-dessus de `outputTokenLimit`, rien ne part ; cette limite n'est pas relevée, et la page de prix de Google dit seulement, de Neon : « long-decode generation up to 1M tokens » (M). La réserve d'un envoi vaut {{J_RES_ENTREE}} + 15 × S ÷ 1 000 000 USD : {{J_RES3_65536}} à {{SMAX_ESSAI_J}}, {{J_RES3_81920}} à {{SMAX_L7}}, {{J_RES3_262144}} à {{R7_MAX_J}} (C). Ce choix pèse peu sur la dépense : au régime prudent, le pire cas tenu par les gardes ne dépend pas de la sortie maximale.
- **Option (a)** : la plus grande des deux, soit {{SMAX_ESSAI_J}} au moins ; la borne déclarée reste {{BORNE_DECL}}, portée au plus grand compte de pensée observé à l'essai s'il la passe — la règle 7 rend alors {{R7_SI_PENSEE}} au moins, et c'est déjà le nœud — ; règle écrite au texte avant son scellement ; au-dessus de {{SMAX_L7}} ou de `outputTokenLimit`, nœud de Lazar. Avantage : les deux règles et le maximum de ce devis tiennent ; le juge lit au réglage de son essai tant que la règle 7 ne demande pas plus. Inconvénient : un brouillon du texte de plus ; la borne déclarée reste une supposition.
- **Option (b)** : un budget de réflexion chiffré et plus bas, si le service en admet un à la place d'un niveau. Avantage : une sortie maximale plus basse, et une borne que la garde vérifie vraiment. Inconvénient : ce n'est plus le réglage admis à l'essai.
- **Recommandation** : (a). Confiance : haute. **Pas de défaut** : la sortie maximale envoyée à Google tenait à un mot de Lazar, que l'avenant 2 dit remplacé, pour l'essai, par une décision de la mère sur un point rangé parmi ses nœuds (sa section 10, point 3). Le texte est l'affaire de son rédacteur.

**Décision 6 — Le pire cas et le versement chez Google pour les lignes du juge.**
- **Décision** : accepter, pour les lignes 7 et 8, un pire cas de {{PIREJ_80}} USD chacune, sans borne dure, et verser sur chaque projet de quoi atteindre le seuil de la ligne ; ou autrement.
- **Enjeu** : chez Google, recharge automatique activée et aucun plafond de dépense (GO-2026-11-21-68). Lazar a accepté {{ACCEPTE}} USD pour les essais ; l'avenant 2 les porte à {{AV2_PIRE}} sans borne dure, {{AV2_PRUDENT}} au régime prudent (M). Les deux lignes du juge ajoutent {{EXPO_J}} USD au régime prudent : {{EXPO_PIRE}} avec le pire cas des essais, {{EXPO_PRUDENT}} si tout reste au régime prudent (C). Seuil d'une ligne du juge : {{SEUIL_J_80}} USD par projet, dépense retirée, soit {{EUR_J}} € vus au taux relevé de l'avenant 2 (1,0990 USD pour 1 €, moins 5 %) (C). Les deux soldes vus avant les essais, 11,93 € et 15,59 €, ne le couvrent pas. Si les deux projets sont portés à {{EUR_AV2}} € pour les essais, comme l'avenant 2 le recommande, et que les essais coûtent leur attendu, le seuil est couvert sans versement neuf (section 6).
- **Option (a)** : accepter, et verser avant la ligne 7 ce qui manque au solde vu après les essais, pièce de constat neuve. Avantage : la ligne ne s'arrête pas pour une raison de caisse. Inconvénient : un paiement, et un solde immobilisé sur deux projets.
- **Option (b)** : servir le juge de la course sur une seule clé. Avantage : un seul projet à garnir, si l'on sait lequel porte la clé. Inconvénient : une voie que quatre lectures seulement auront éprouvée (avenant 1, version 3) : à écrire au texte ; et le lien entre chaque clé et son projet n'est pas constaté.
- **Recommandation** : (a). Confiance : moyenne. **Pas de défaut** : c'est un paiement, et il reste à Lazar (GO-2026-11-21-69). Lazar a écarté un plafond de dépense à la console (GO-2026-11-21-68) : je ne le repropose pas.

## 10. Réponses reçues, question neuve, cases à remplir

**Réponses de la session du bras A à mes deux questions du brouillon 1** :
1. **Les 80 appels du juge, « 48 + 24 + 8 »** : 72 servent l'appariement et 8 la couverture, par inférence de 6.11 — la révision ne relit que les lots de l'appariement et ajoute 72 appels, soit 48 + 24. C'est la répartition que j'avais supposée. La lettre est à la section du texte qui définit les deux ancres, que mon mandat ne m'ouvre pas : à confirmer par la mère. Enjeu faible : {{J_EK_80_ALT}} USD attendus au lieu de {{J_EK_80}} si 24 des 72 étaient de couverture ; les plafonds n'en dépendent pas (C).
2. **« Au cas B, ses 102 points de lecture par action »** : cela se tranche à la section 13.2 du texte, puis chez les agents habilités de la mère. Je le laisse en case conditionnelle (4.5 ; ligne 10).

**Question neuve à la mère** (un volume de 6.11 se lit de deux façons) :
3. **« Quatre épreuves mécaniques de la couverture (160 artefacts : 32 par lecteur et par épreuve) » : est-ce 128 appels par lecteur, comme au tableau et au majorant de 6.11, ou 160 ?** À 160, soit {{EXTRA_160}} lectures de couverture de plus par lecteur, les lots d'épreuve attendraient {{L2_EPR_160}} USD au second lecteur et jusqu'à {{L1_EPR_160}} au premier ; la règle rendrait {{PL_160}} USD aux lignes 1 et 4, au-dessus de leur maximum de {{PL2_EPREUVE}} (C).

**Cases de la session de relance** — la mère, ou une fille qu'elle habilite à ces pièces ; rien ici ne relève du côté habilité (vérification, point 4) :
1. **Premier lecteur.**
   - Modèle et réglage (effort ou budget de réflexion, sortie maximale) : à la règle de choix que cite 6.11, et au mot de Lazar qui fixe « le modèle Claude et le budget des lecteurs ».
   - Tarif relevé et daté : au devis de l'essai de mesure, puis sur une page de prix d'Anthropic relevée le jour, versée et empreintée. Mon mandat ne me permettait que mistral.ai et ai.google.dev.
   - Compteurs de l'essai de mesure : coût moyen compté d'un appel par instrument, sorties réflexion comprise, taux de redemande, durées, d'où le délai, le débit et le coût d'un envoi coupé.
   - La projection de 146,4 USD refaite par phase, et la confirmation qu'elle porte sur 15 136 lectures, révision et redemandes comprises.
   - Variable de la clé, fournisseur et crédit ; réserve d'un envoi, à comparer à {{RES1_MAX}} USD.
2. **Second lecteur, après son essai d'admission** : point d'accès retenu ; issue de la sonde de borne ; maximum de sortie, d'où la sortie maximale de la course, à comparer à {{SMAX_L4}} ; coût moyen compté d'un appel par instrument ; taux de non-conformité ; durées, d'où les délais ; jetons d'entrée comptés par Mistral sur ces entrées.
3. **Juge, après son essai d'admission** : les mêmes ; la sortie maximale selon la décision 5, à comparer à {{SMAX_L7}} et à `outputTokenLimit` ; le plus grand compte de pensée, à comparer à la borne déclarée ; le service par une ou deux clés ; la limite de mots de sa consigne et le rapport de jetons par mot.
4. **Chez Google** : les soldes vus après les essais, sur les deux projets, et le taux du jour ; si les deux clés sont sur deux projets différents.
5. **Ce que le texte dit, hors de 6.11** : d'une ligne arrêtée à son plafond ; de l'ordre des lectures ; d'une réponse en défaut ; de la répartition des appels du juge, à la lettre.

**Cases du côté habilité** : pour chaque moniteur, le modèle, le tarif relevé et daté, la longueur de la consigne, la sortie d'une lecture raisonnement compris, les envois par appel ; pour le juge d'une autre lignée, l'entrée d'une lecture ; s'il tourne par appels ou sur une carte ; s'il est servi par Google, la borne de réflexion déclarée et la sortie maximale ; le sens des « 102 points ».

## 11. Réserves

1. **Premier lecteur** : rien n'est refait. 146,4 USD est une transcription de 6.11 ; sa répartition par phase est une fourchette sur une supposition ; son tarif et son réglage ne sont dans aucune de mes pièces. Le mandat ne permettait de relever une page de prix que chez Mistral ou chez Google, les consignes de lancement interdisaient tout réseau, et ce lecteur n'est servi par aucun des deux : je n'ai rien relevé.
2. **Second lecteur et juge** : aucune mesure à leur réglage. L'attendu repose sur 2 000 et 4 000 jetons de sortie, supposés. De la moitié au quadruple de cette supposition, le second lecteur coûte de {{SENS_LO}} à {{SENS_HI}} USD (4.2).
3. **Longueurs** : mesurées sur 24 entrées synthétiques, reprises d'un devis qui les reprend lui-même ; les textes réels peuvent différer ; le découpage de Mistral n'est pas mesuré.
4. **Instrument et phase de chaque lot** : ma lecture de 6.11, recoupée par un seul compte ; la vérification la trouve juste sur ce compte.
5. **Tarifs** : lus dans des pages publiques versées ; la facturation de la réflexion de Mistral n'y est pas écrite.
6. **Marges (3 ; 2 ; 1,5, par instrument), arrondi aux 5 USD, redemandes à 2 sur 24** : mes choix, que le contre-lecteur peut défaire. La lettre de la marge n'est pas celle que la vérification proposait (table des corrections, C-2).
7. **« Pire cas tenu par les gardes »** : sous trois suppositions non mesurées, dont une non documentée (5.3). Chez Google, rien de dur au-delà.
8. **Règles de la course hors de 6.11** : non lues. Ce devis suppose la reprise d'une ligne arrêtée, sans rejeu.
9. **Avenant 1, version 3** : brouillon dans sa lettre (« ni revérifiée ni acceptée »). **Avenant 2** (`5f84642a…`) : brouillon non contre-lu. La file du juge et les vérifications de ses clés y passent à {{SMAX_ESSAI_J}} jetons, au niveau de réflexion le plus haut, sous une borne de réflexion déclarée de {{BORNE_DECL}} jetons, supposée ; pire cas chez Google des essais : {{AV2_PIRE}} USD sans borne dure, {{AV2_PRUDENT}} au régime prudent. Ceux de ses chiffres que je reprends se refont sur ses entrées (section 13, partie 14). Si sa contre-lecture en change un, les sommes de la décision 6 et les euros de la section 6 se refont.
10. **Durées** : aucune n'est mesurée ; la décision 3 repose sur 30 et 60 secondes par appel, supposées.
11. **Moniteurs** : je ne sais que leurs volumes. Aucun prix n'est donné, même en exemple.
12. **La garde commune des appels à Google** (`src/controle_ia/`) n'est pas ouverte : hors de ma liste. Je cite la règle, non son code.
13. **Le devis des essais d'admission** se dit « brouillon 5 » dans sa lettre ; l'index des pages de prix et les avenants le disent accepté. Je le cite comme il se nomme.
14. **Devise des comptes** : tout est compté en USD. La fiche de Mistral porte un sélecteur entre USD et EUR ; la devise du compte de Mistral n'est pas relevée. Chez Google, les soldes sont vus en euros ; le taux de 1,0990 USD pour 1 € est celui que l'avenant 2 relève, et je n'ai pas ouvert son fichier.
15. **Huit appels à la fois** : la règle de 5.1 ne compte qu'une réserve, quand le compteur en retient huit. Je n'ai pas relevé les maxima pour autant : la vérification les a refaits tels quels. Si la règle comptait huit réserves, seul le maximum de la ligne 4 changerait chez Mistral, de {{PL2_EPREUVE}} à {{PL4_8RES}} USD, pour une sortie maximale de 32 768 (C) ; ceux du premier lecteur dépendent de sa réserve, qui est une case. Le contre-lecteur ou Lazar peut préférer cette règle.
16. **`outputTokenLimit` de `gemini-4-neon` n'est pas relevé.** « Up to 1M tokens » est une phrase de la page de prix, non la limite de l'appel.
17. **La vérification du brouillon 1** est d'un agent Claude Opus 5.5 ; ses chiffres neufs sont refaits ici et trouvés égaux (section 13, parties 13 à 15), à deux écarts près, dits en table des corrections : la tolérance du juge (m-1) et les longueurs des lignes (C-6).

## 12. Ce que j'ai ouvert

Arbre : copie de travail sur la branche `relance-bras-a/devis-hors-carte`, tête `ba3ab17f…`. Empreintes calculées par `sha256sum` ; pour le devis de course, le devis des essais, l'avenant 1, les pages de prix, leur index et les mots de Lazar, elles sont égales à celles de leurs compagnons, et à celles du brouillon 1.

| pièce | empreinte | ce que j'en ai lu pour ce brouillon |
|---|---|---|
| `…/mandat-redacteur-fable-devis-lectures-hors-carte-v1.md`, le mandat | `86c98be8112805ecd1643fe8212b7e39a5a880e3dd8d7a69d5a00f51654127c2` | en entier, empreinte vérifiée avant lecture |
| `…/devis-lectures-hors-carte-bras-a-v1-brouillon1.md`, le brouillon 1, et ses programmes, `…/devis-hors-carte-programmes-v1/` | `70adb0482f69179e5279452f4fef45ff1d00a885118e7038888f5cc50284ccb8` | en entier ; programmes rejoués : ils refont le brouillon 1 octet pour octet |
| `…/verification-devis-lectures-hors-carte-brouillon1-v1.md` | `b0f04bd512a4ae9df9f943af8e88aea851128a80a0f7f3491daf390e739dfb43` | en entier, annexes comprises ; lue par `git show` sur la référence locale de la branche de la session du bras A |
| `…/avenant-2-devis-essais-admission-plafond-google-65536-v1.md` | `5f84642a896da2440c76c2c51aecb027224b644dde98ee0bcd3c63e4fd53f497` | en entier ; lu par `git show` sur la référence locale de sa branche |
| `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v2.md` | `83240ca61d7c300fc9f4ca802560a6010a2a7c2eb48dd58fe2c214ee03524ecd` | en entier |
| `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md` | `4f91b535ad91581510615c97039a4cae0a96f4d788088b2aff666d4c3d3f97b3` | la seule section 6.11, par la commande du mandat ; aucune recherche dans le texte |
| `…/devis-essais-admission-mistral-neon-bras-a-v1.md` | `421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc` | en entier au brouillon 1 ; relu ici : en-tête, sections 0 et 1, 4 à 10, tableau de la section 11 |
| `…/avenant-1-devis-essais-admission-recharge-et-deux-cles-v3.md` | `5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac` | en entier au brouillon 1 ; relu ici : en-tête, sections 0, 4, 8 et 9 |
| `…/pages-de-prix-essais-admission-v1/index-pages-de-prix-v1.md` | `8aeb9f9d3ae33a81540324d863c65193b52d03f6e75a4366e27e838bbd15b790` | en entier |
| `…/pages-de-prix-essais-admission-v1/mistral-large-4-0-2026-11-21.html` | `951cc3ff5f3cdd9b83776bfc6d4b4ef6fbe7c48a59c106945539fee6be1b3d36` | par programme : les prix de la fiche |
| `…/pages-de-prix-essais-admission-v1/mistral-regional-inference-2026-11-21.html` | `b501d686c7cff43cf3b9b1c0bf5b4227ff945c6cdf22e808769639bd2c2d5b18` | par programme : la phrase du prix régional, et celle du service par lots |
| `…/pages-de-prix-essais-admission-v1/google-gemini-pricing-2026-11-21.html` | `4da106182cbbb57172ce41eabb09eb0af08798cb4d030dea0ee444870d4554a8` | par programme : la section de Gemini 4 Neon, en entier |
| `…/mots-de-lazar-cinq-choix-lecteur-bras-a-2026-11-20-v1.md` | `93cbc6f4c78d00c5b91ca29e5b300bef345cd7aa46c89db2be6bff95a46d5beb` | en entier |
| `…/mots-de-lazar-compte-google-prepaye-bras-a-2026-11-21-v1.md` | `487b5a725b619b290a82c619a507f23de8ce6f72a0a2ed3b101bdc3168ab9421` | en entier |
| `…/mots-de-lazar-devis-essais-admission-bras-a-2026-11-21-v1.md` | `9b9ee5ca4e89f3dcd8d4c5865f7badf613943f00800b9a80d011bd6f45b1c57b` | en entier |
| `…/mots-de-lazar-juge-des-ancres-neon-bras-a-2026-11-20-v1.md` | `6ebab24f009bbb7587eb14c22ae832f3d93ce5911e832cce087e4afa7c6f9cf2` | en entier |
| `…/mots-de-lazar-juge-et-envoi-des-textes-bras-a-2026-11-21-v1.md` | `00af2aa83604df20181e9ea0fdcf15fbd88601f98f96388ce32d23d7c0a98e5a` | en entier |
| `…/mots-de-lazar-juge-et-point-19-bras-a-2026-11-20-v1.md` | `2845ca37e79361aaff125fb2f01cbcb569257526bae0c8eeaeddef7f61dcf6df` | en entier ; je n'en reprends que le compte de 6 400, que 6.11 porte aussi |
| `…/mots-de-lazar-second-lecteur-et-juge-des-ancres-bras-a-2026-11-20-v1.md` | `8189dcec0f83a74fde8c8b1ac82a74142f946f77dfda41b88e95d547c4534d6a` | en entier |

`…` = `docs/notes/relance-organismes-discrets-v1`.

- **Aucun `git fetch`.** La consigne de reprise proposait d'aller chercher la branche de la session du bras A ; le mandat l'interdit. La référence locale portait déjà la vérification, à l'empreinte dite : je l'ai lue là. Les références locales ont bougé pendant mon travail, du fait d'une autre session ; les deux empreintes sont restées égales, vérifiées deux fois.
- **Registre** : `registres/go.md` sur la référence locale `origin/main`, par la seule commande du mandat, la recherche ancrée sur l'identifiant en début de ligne, pour GO-2026-11-21-63, -68, -69 et -71. Chacune porte aussi des décisions sur d'autres travaux, vues en passant : je n'en fais rien.
- **Consignes permanentes** : la section « Appels aux modèles de Google » de `CLAUDE.md` sur `origin/main`, par la commande du mandat ; et le `CLAUDE.md` du dépôt de travail, reçu au lancement.
- **Débords, déclarés.** Ma première commande a listé les cent premières entrées du dossier de la relance, noms et tailles, de `addendum-3-…` à `decision-bras-a-avant-scellement-…` : le mandat ne demandait pas cette liste. Aucun de ces noms n'est un chemin cloisonné ; je n'en ai ouvert aucun hors de ma liste. La même commande a montré les titres des cinq derniers commits de la branche ; une autre, celui du dernier commit de la branche de l'avenant 2. Dans l'arbre : `git status --short`, `git rev-parse` et `git cat-file -e` sur les trois références et les deux pièces. Listes ciblées, par leur nom : le brouillon 1, le dossier de ses programmes, `mots-de-lazar-*`, le dossier des pages de prix, et `avenant-2*`, absent de mon arbre. Hors du dépôt : le bloc-notes du brouillon 1, où sont mes programmes et leurs essais.
- **Chemins cloisonnés** : plusieurs pièces permises en citent (`prereg/T0.6-organismes-v0-v1.md`, des chemins sous `runs/`, `docs/notes/bras-a-sans-interne-v1/`). Je recopie ces citations là où elles servent ; **je n'en ai suivi, listé ni empreinté aucun.** Le brouillon 44 du texte, que la vérification a comparé, n'est pas ouvert ici. Le fichier du taux de change que cite l'avenant 2 non plus.
- **Extraits gardés au bloc-notes**, pour y confronter les chiffres : la section 6.11, la section de la règle, les quatre lignes du registre, l'avenant 2, la vérification. Ils ne sont pas versés au dépôt.
- **Le programme de la vérification** (son annexe A, `65648b3a…`), rejoué au bloc-notes : sa sortie est, à la lettre, celle de son annexe B (`e3c61bee…`). Mes chiffres lui sont égaux, à l'écart dit en table des corrections (m-1).
- **Rien d'autre.** Aucun appel réseau, aucune page de prix relevée par moi, aucune clé lue, aucun appel de modèle, aucun sous-agent, aucune dépense ; rien scellé, rien committé. Fichiers écrits : celui-ci, sans compagnon d'empreinte, et ses programmes ; le brouillon 1 et ses programmes sont intacts. Un fichier de cache de Python, né de ma relecture des pages de prix dans le dossier des programmes du brouillon 1, a été retiré : ce dossier est tel que je l'ai trouvé. Ce brouillon a été composé deux fois avant d'être rendu : la première composition (`17fbf6c4…`) ne disait pas ce fichier de cache et comptait mal les décisions sans défaut ; elle est gardée au bloc-notes, non livrée.
- **Programmes**, versés sous `docs/notes/relance-organismes-discrets-v1/devis-hors-carte-programmes-v2/` : `calc_hc2.py` (`{{SHA_CALC}}`), tous les chiffres marqués C, repris de `calc_hc1.py` par remplacements exacts ; `controle_hc2.py`, qui refait {{N_CONTROLE}} de ces chiffres par une autre écriture et les trouve égaux ; `gabarit_hc2.md` et `faire_hc2.py`, qui insèrent dans ce devis les valeurs rendues par `calc_hc2.py`, sans rien recopier à la main, comptent les signes des lignes de calcul et refusent une ligne de registre interdite ; `verif_hc2.py`, qui relit ce devis composé, cherche chacun de ses nombres dans la sortie du calcul ou dans les pièces lues, recompte les signes des dix lignes et recalcule les empreintes de ce tableau. `extrait_prix.py` est celui du brouillon 1, inchangé.

## 13. Calculs, par programme

Sortie de `calc_hc2.py`, en fractions exactes. Arrondis : au plus proche pour les coûts ; au supérieur pour les réserves et les plafonds. Les parties 1 à 12 sont celles du brouillon 1, aux changements dits en table des corrections ; les parties 13 à 15 sont neuves.

```
{{TRACE}}
```
