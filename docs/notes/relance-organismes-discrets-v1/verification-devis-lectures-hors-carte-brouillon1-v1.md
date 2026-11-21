# Vérification du devis des lectures hors carte du bras A, brouillon 1 — v1

**Verdict : engageable après corrections.** Les volumes sont fidèles à la section 6.11 du texte (identique au brouillon 44) ; l'attendu (≈ 254,79 USD) et les plafonds (670 USD en huit lignes, 130 au premier engagement, 560 sans la révision) sont justes au centime, refaits par un programme écrit sans lire celui du rédacteur. La frontière du mandat est tenue. Sept corrections, dont trois de fond : l'avenant 2 est désormais dans l'arbre et change la décision 5 et le pire cas accepté chez Google ; la marge de 1,5 ne peut pas valoir pour la couverture, mesurée sur 320 lectures seulement ; les maxima des lignes 4 et 7 ne tiennent que sous une sortie maximale de course que la règle 7 du texte peut dépasser.

- **Vérificateur** : agent neuf (Claude Opus 5.5), le 2026-11-21 vers 19:12Z (`date -u`). Il n'a écrit ni le devis, ni ses programmes, ni le texte, ni les devis et avenants cités. **Rien n'est scellé ni committé.**
- **Objet** : `docs/notes/relance-organismes-discrets-v1/devis-lectures-hors-carte-bras-a-v1-brouillon1.md`, sha256 `70adb0482f69179e5279452f4fef45ff1d00a885118e7038888f5cc50284ccb8`, et `docs/notes/relance-organismes-discrets-v1/devis-hors-carte-programmes-v1/` (cinq fichiers, empreintes égales à leurs compagnons ; `calc_hc1.py` = `388ec1d9…`, celle que cite le devis).
- **Interdits appliqués** : ceux du mandat du rédacteur (`mandat-redacteur-fable-devis-lectures-hors-carte-v1.md`, `86c98be8…`, empreinte vérifiée). Aucun réseau, aucun `git fetch`, aucune clé, aucun chemin cloisonné ouvert, listé ni empreinté.

## 1. Point 1 — volumes, attendu et plafonds, recalculés

Programme indépendant : `verif_hc.py` (annexe A, sha256 `65648b3ad9b35e3007ce4f0112b156384afe4bb0610b997a0c6fdf65cce0584f`, fractions exactes), écrit avant toute lecture de `calc_hc1.py`, sur les seules entrées des pièces : tableau de 6.11 ; longueurs du devis des essais, 6.2 (23 625 sur 18, 31 591 sur 6 ; 5 159 sur 6, 7 933 sur 2) ; prix lus dans les pages versées (0,7 et 2,1 ; « 1.1× standard list pricing » ; 3,00 et 15,00, « including thinking tokens »).

| grandeur | devis | recalcul | |
|---|---|---|---|
| appels par lecteur, épreuve / décisif / révision | 2 496 / 10 464 / 2 176 | 2 176 + 320 ; 9 536 + 928 ; 2 176 + 0 | égal |
| appariement / couverture, par lecteur | 13 888 / 1 248 | 13 888 / 1 248 (égal au compte de la grandeur `C`, devis des essais, section 7) | égal |
| lectures des deux lecteurs | 25 920 ; 30 272 | 25 920 ; 30 272 | égal |
| juge ; majorant des envois | 80, 152 ; 91 272 | 80, 152 ; 91 272 (égal à 6.11) | égal |
| entrée par lecteur, avec révision | 24,8 millions | 24 798 928 | égal |
| entrée, tous postes | 80,7 ; 86,4 ; 93,8 millions | 80,66 ; 86,44 ; 93,78 | égal |
| Mistral, par phase, avec redemandes | 17,88 ; 71,53 ; 13,27 ; total 102,69 | 17,8819 ; 71,5332 ; 13,2733 ; 102,6884 | égal |
| recoupe des essais (Mistral, Neon) | 0,18 ; 0,34 | 0,1811 ; 0,3393 | égal |
| juge, 80 et 72 appels, avec redemandes | 3,16 ; 2,54 | 3,1643 ; 2,5412 | égal |
| premier lecteur réparti (rapport 1 à 4) | 24,14–26,80 ; 101,21–102,73 ; 16,87–21,05 | mêmes valeurs | égal |
| réserves Mistral à 8 192 / 16 384 / 32 768 ; Google à 32 768 / 65 536 | 0,171 / 0,322 / 0,625 ; 0,564 / 1,056 | 0,1700 / 0,3214 / 0,6242 ; 0,5635 / 1,0550 (le devis arrondit au millième supérieur) | égal |
| plafonds 1 à 8 | 55, 210, 45, 55, 220, 45, 20, 20 | mêmes | égal |
| somme ; sans révision ; lignes 1, 4, 7 | 670 ; 560 ; 130 | 670 ; 560 ; 130 | égal |
| attendu ; sans révision ; premières lignes | 254,79 ; 217,93–222,11 ; 45,19–47,84 | 254,7939 ; 217,9325–222,1062 ; 45,1883–47,8449 | égal |
| envoi coupé à 2 690 s, Mistral / Google | 1,24 / 8,07 | 1,2428 / 8,0700 | égal |
| crédits Mistral ; Google | 65,00 ; 254,50 ; 53,50 ; 372,50 ; 32,50 | mêmes | égal |
| majorants vrais | 1 089 / 1 948 / 3 667 ; 135, 257 / 253, 481 | 1 088,87 / 1 948,15 / 3 666,71 ; 135,24, 256,97 / 253,21, 481,10 | égal |
| tolérance de sortie du juge | « environ 14 900 » (4.4 et 5.2) ; 14 994 (section 13) | 14 990 | **mineur m-1** |

**Fidélité à 6.11 et au devis de course.** Les neuf lots, leurs comptes et le majorant sont recopiés à la lettre ; l'attribution d'instrument et de phase, que 6.11 ne dit pas, tombe juste sur le seul recoupement disponible (13 888 et 1 248). La section 6.11 du brouillon 44 (`b30aa902…`) est identique octet pour octet à celle du brouillon 43 (`diff` des deux extraits par la commande du mandat) : rien n'est à refaire pour le texte vérifié depuis. Le tableau « ce qui a changé » reprend fidèlement la section 6 du devis de course (1 792 et ≈ 272 ; ancre humaine à 0 USD ; 6 400 et 8 960 ; 2 560 ; 33 à 35, ≈ 42 millions). Un seul point de 6.11 reste ambigu et n'est pas porté en question : « 160 artefacts : 32 par lecteur et par épreuve » pour quatre épreuves, quand le tableau compte 128 appels par lecteur. Le devis garde 128, comme le majorant de 6.11 ; si c'était 160, la ligne 4 attendrait 18,34 USD et son plafond recalculé passerait 55 (mineur m-2).

## 2. Point 2 — frontière du mandat : tenue

- Les deux moniteurs à modèle de langue n'apparaissent qu'en volumes (6 400 lectures chacun, 18,3 millions de jetons d'entrée en ordre de grandeur, tiré du devis de course), avec une formule dont `c`, `s`, `pe`, `ps` et `k` sont des cases du côté habilité, et un plafond conditionnel non chiffré. **Aucun nom de modèle, aucune consigne.**
- Aucune ligne de GO du 19 novembre n'est nommée ; rien de ce que les mots de Lazar décident pour les deux points réservés n'est recopié (contrôlé aussi par `faire_hc1.py`). Les chemins cloisonnés cités par les pièces permises sont recopiés, non suivis.
- Deux réserves, sans correction obligatoire : le tableau d'exemples de 4.5 prend « 3 et 15 », le tarif de Neon, ce qui peut se lire comme un indice (m-3) ; « s'il lit lui aussi l'action dans son contexte (S) » est une supposition sur l'entrée d'un moniteur, qui devrait être une case (m-4). Les lignes 9 et 10 sont des gabarits pour le côté habilité ; elles disent qu'elles ne se demandent pas avant son devis propre : c'est conforme à 6.11 (« devis et ligne de GO propres »).

## 3. Point 3 — règle permanente des appels à Google

| exigence de la règle | où le devis l'applique | état |
|---|---|---|
| réflexion explicite au plus haut | 3.2, 4.4, garde 7 (`xhigh` dans le corps) | appliquée |
| plafond ≥ réflexion + 16 000 | 4.4 (provision = plafond − 16 000), garde 7, décision 5 | appliquée, **incomplète** : sous un niveau, la règle se vérifie sur une borne de réflexion *déclarée* (avenant 2, section 4 : 49 536, supposée) ; le devis ne la nomme pas, ni le contrôle de `outputTokenLimit` (C-1, C-4) |
| limite de mots tenue dans le plafond de texte | 4.4, garde 7 | appliquée ; l'avenant 2 (sections 4 et 9) en fait l'affaire d'un lecteur habilité (`limite_de_mots`, `jetons_par_mot`), non du rédacteur du texte (m-5) |
| défauts après la réponse | 4.4, garde 7 | appliquée ; ajouter `CONTINUATION`, rangé avec la sortie maximale atteinte au devis des essais (5.5) (m-6) |
| toute lecture par un modèle de Google | juge : oui ; moniteurs : conditionnel en 4.5 | **absent des lignes 9 et 10** (C-5) |

Le premier lecteur (Claude) et le second (Mistral) ne sont pas servis par Google : la règle ne les vise pas.

## 4. Point 4 — le premier lecteur : ce qu'il faut, et qui le remplit

Ce qui manque, et la pièce qui le porte :
1. **Le modèle et le réglage** (effort ou budget de réflexion, sortie maximale) : la règle de choix citée par 6.11, `runs/essai-mesure-lecteurs-bras-a-v1/regle-de-choix-claude-carbon-v1.json` (`b14b7084…`), et le mot de Lazar qui fixe, sur l'essai de mesure, « le modèle Claude et le budget des lecteurs » (6.11).
2. **Le tarif relevé et daté** : « relevés et datés au devis de l'essai, puis au devis de la course » (6.11) — devis de l'essai de mesure `devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md` (`533ad5b1…`, empreinte reprise du devis des essais), puis **une page de prix d'Anthropic relevée le jour**, versée et empreintée. Le mandat du rédacteur ne lui permettait que mistral.ai et ai.google.dev : il ne pouvait pas la relever.
3. **Les compteurs** : coût moyen compté d'un appel par instrument, sorties réflexion comprise, taux de redemande, durées (d'où délai, débit et coût d'un envoi coupé), au rapport de l'essai de mesure (sous des chemins cloisonnés pour le rédacteur).
4. **La projection de 146,4 USD refaite par phase**, et la confirmation qu'elle porte sur 15 136 lectures, révision et redemandes comprises.

**Qui** : la session de relance (la mère, ou une fille qu'elle habilite à ces pièces). Le premier lecteur est un lecteur de l'oracle, du côté de la relance : **rien ne relève du côté habilité**. Aucune de ces pièces n'est ouverte ici.

## 5. Point 5 — les deux questions du rédacteur

**Question 1 — répartition des 80 appels du juge.** 6.11 la tranche par inférence, non par la lettre. La révision ne relit que « les lots de l'appariement » (même tableau) et ajoute exactement 72 appels du juge, soit 48 + 24 : les 72 premiers appels sont donc ceux de l'ancre d'appariement, et les 8 restants ceux de la couverture. C'est la répartition supposée par le rédacteur. **Pièce qui le confirme à la lettre** : la section du texte qui définit les deux ancres, du côté de la relance, lisible par la mère (non lue ici : le mandat borne la lecture à 6.11). Enjeu faible : l'attendu passe de 3,16 à 4,19 USD au plus si 24 des 72 étaient de couverture, et les plafonds n'en dépendent pas.

**Question 2 — « au cas B, ses 102 points de lecture par action ».** 6.11 ne le tranche pas : la phrase renvoie à 13.2. **Pièce qui tranche** : la section 13.2 du texte (case « devis »), lisible par la mère ; et, derrière elle, le chiffrage du juge d'une autre lignée par le côté habilité (`docs/notes/bras-a-sans-interne-v1/reponses-sans-interne-demandes-v8-v3.md`, `6c0f71f6…`, citée par les mots de Lazar, cloisonnée, non ouverte). Le juge d'une autre lignée est un moniteur : **la réponse est du côté habilité**, la mère n'en relaie que le volume. Enjeu : 102 appels par action feraient 652 800 lectures et ≈ 1,87 milliard de jetons d'entrée (C), cent deux fois le poste ; la ligne 10 ne doit rien chiffrer avant la réponse, ce qu'elle dit déjà.

## 6. Point 6 — les lignes de calcul sont-elles citables telles quelles ?

Non, pas toutes. Toutes tiennent sous 600 signes, n'emploient que des noms en clair et ne nomment que les lignes de GO permises. Mais :
- lignes 1, 4, 7 et 8 : « ramené à 2 [ou 3] fois la projection » oublie la réserve d'un envoi et l'arrondi de la règle 5.1 : un plafond ainsi « ramené » serait plus bas que la règle et pourrait arrêter une ligne saine (C-6) ;
- lignes 2 et 5 : la marge de 1,5 sur la couverture contredit la règle 5.1 elle-même (C-2) ;
- ligne 4 : ni la sortie maximale ni sa borne en octets, dont dépend le maximum de 55 USD (C-3) ;
- ligne 7 : ni la sortie maximale, ni le niveau de réflexion, ni le mode sans flux (C-4) ;
- lignes 9 et 10 : la règle de Google conditionnelle manque (C-5) ;
- lignes 1 à 3 : des crochets restent ouverts ; c'est dit, et ils se remplissent par la session (point 4).

## 7. Point 7 — les décisions pour Lazar

Bien posées dans leur forme (décision, enjeu, options avec avantage et inconvénient, recommandation et confiance, défaut ou son absence). Trois défauts :
1. **Décision 5** est posée sans l'avenant 2, qui joue l'essai du juge à 65 536 sous une borne de réflexion déclarée et dit lui-même que la règle 7 lira un essai joué à 65 536 (sa section 10, point 11). Elle ne doit pas prendre de défaut : la sortie maximale de Google tenait à un mot de Lazar (« goreco »), et l'avenant 2 range ce point parmi ses nœuds (section 10, point 3). Texte de remplacement en C-1.
2. **Il manque une décision** sur le pire cas sans borne dure et le versement chez Google pour les lignes du juge : le devis écrit « à accepter à part » sans la poser, et un versement est un paiement, qui reste à Lazar (GO-2026-11-21-69). Texte en C-7.
3. Décisions 2 et 3 : un défaut sous 48 heures sur des règles qui bornent une dépense est admissible, puisque chaque ligne attend de toute façon son GO ; je n'en fais pas une correction.

La recommandation de section 8 — porter les lignes à Lazar malgré la fenêtre d'autonomie — est juste : GO-2026-11-21-63 écrit « toute ligne neuve sur devis porté à Lazar ».

## 8. Corrections (texte de remplacement exact)

**C-1. Avenant 2 présent ; décision 5.** L'avenant 2 au devis des essais (`avenant-2-devis-essais-admission-plafond-google-65536-v1.md`, sha256 `5f84642a896da2440c76c2c51aecb027224b644dde98ee0bcd3c63e4fd53f497`) est entré dans l'arbre au commit `30a956fb9`, après la rédaction du brouillon.
- Réserve 9, remplacer « **Avenant 2 : absent de l'arbre** ; seul existe le mandat de son rédacteur, vu par son nom, non ouvert ; ce nom annonce un plafond de 65 536, d'où les deux valeurs de 4.4. » par : « **Avenant 2** (`5f84642a…`, brouillon non contre-lu) : la file du juge et les vérifications de ses clés passent à 65 536 jetons, au niveau de réflexion le plus haut, sous une borne de réflexion déclarée de 49 536 jetons, supposée ; pire cas chez Google des essais : 89,67 USD sans borne dure, 32,97 au régime prudent. »
- Décision 5, remplacer le bloc entier par :
  > **Décision 5 — La sortie maximale du juge des deux ancres à la course.**
  > - **Décision** : fixer la sortie maximale du juge à la plus grande de deux valeurs — celle de la règle 7 du texte, et la borne de réflexion déclarée plus 16 000 jetons de texte (règle permanente des appels à Google) —, sous `outputTokenLimit` relevé par l'appel de liste ; ou autrement.
  > - **Enjeu** : l'essai d'admission se joue à 65 536, sous une borne déclarée de 49 536, supposée (avenant 2, sections 1 et 4). La règle 7 peut rendre de 8 192 à 262 144 : à 8 192, la garde refuse tout envoi ; au-dessus de 81 920, le maximum de 20 USD de la ligne 7 ne tient plus (C) ; au-dessus de `outputTokenLimit`, rien ne part. La réserve d'un envoi vaut 0,072 + 15 × S ÷ 1 000 000 USD : 1,056 à 65 536, 4,005 à 262 144.
  > - **Option (a)** : la plus grande des deux, la borne déclarée portée au plus grand `thoughtsTokenCount` observé à l'essai s'il passe 49 536, écrite au texte avant son scellement ; au-dessus de 81 920 ou de `outputTokenLimit`, nœud de Lazar. Avantage : les deux règles et le maximum de ce devis tiennent. Inconvénient : un brouillon du texte de plus.
  > - **Option (b)** : un budget de réflexion chiffré et plus bas, si le service en admet un. Avantage : une sortie maximale plus basse et une borne vérifiable. Inconvénient : ce n'est plus le réglage admis à l'essai.
  > - **Recommandation** : (a). Confiance : haute. **Pas de défaut** : la sortie maximale de Google tenait à un mot de Lazar, que l'avenant 2 dit remplacé par une décision de la mère sur un point rangé parmi ses nœuds (sa section 10, point 3).
- 4.4, dernier point, remplacer « Le pire cas accepté, 84,06 USD, vaut pour les lignes des essais. Les deux lignes du juge à la course y ajoutent 56,14 USD au régime prudent (C), à accepter à part. » par : « Lazar a accepté 84,06 USD pour les essais (GO-2026-11-21-68) ; l'avenant 2 les porte à 89,67 sans borne dure, 32,97 au régime prudent. Les deux lignes du juge à la course y ajoutent 56,14 USD au régime prudent (C) : 145,81 et 89,11 avec les essais. C'est la décision 6. »

**C-2. Marge de 1,5 par instrument.** 5.1, remplacer la formule et le point `m` par :
> `plafond = arrondi aux 5 USD supérieurs de [ m_a × n_a × c_a + m_c × n_c × c_c + r ]`
> - `m_a`, `m_c`, la marge, **par instrument** : **3** si le coût de cet instrument est supposé, ou mesuré sur moins de 24 lectures de cet instrument ; **2** s'il est mesuré sur 24 lectures au moins ; **1,5** s'il est mesuré sur 1 000 lectures réelles au moins de cet instrument, du même lecteur. Les lots d'épreuve en comptent 2 176 d'appariement et 320 de couverture : la couverture des lots décisifs reste à 2.

Et 5.2, « Exemple du recalcul », remplacer « 110 et 25 USD pour les lots décisifs et la révision, à la marge de 1,5 » par « 115 et 25 USD pour les lots décisifs et la révision, à 1,5 pour l'appariement et 2 pour la couverture » (C : 114,61 → 115 ; la révision n'a que de l'appariement). Les maxima de 210 et 220 USD ne changent pas.

**C-3. Sortie maximale de la course et maxima.** Ajouter à 5.1, après « Les plafonds de ce brouillon sont des maxima. » : « **Ils supposent une sortie maximale de course d'au plus 71 680 jetons chez Mistral et 81 920 chez le juge** (C : au-delà, la réserve d'un envoi fait passer les maxima des lignes 4 et 7). La règle 7 du texte peut rendre jusqu'à 131 072 chez Mistral, dont l'essai se joue à 32 768, et 262 144 chez le juge, joué à 65 536 ; au-delà de ces deux valeurs, la ligne ne part pas : nœud de Lazar, devis repris. La garde 3 le vérifie. »

**C-4. Ligne 7.** Remplacer son texte par (548 signes) :
> bras A, lectures hors carte, juge des deux ancres (`gemini-4-neon`), seulement s'il est admis : 80 appels, 240 envois au plus, sans flux ; niveau de réflexion le plus haut, explicite ; sortie maximale par la décision 5, sous `outputTokenLimit` et 81 920 au plus ; plafond 20 USD au plus, ramené par la règle 5.1 (marge 3) ; régime prudent ; pire cas tenu par les gardes 28,07 USD si la coupure arrête la facturation, non documenté ; aucune borne dure ; compté à 3 et 15 USD par million ; règle des appels à Google tenue par code (GO-2026-11-21-71).

Et à la garde 7, ajouter dans « ce qu'elle fait » : « sous un niveau de réflexion, le plafond se contrôle sur la borne de réflexion déclarée à la configuration ; `outputTokenLimit` lu avant tout envoi, au moins égal au plafond » ; et dans « artefact » : « `CONTINUATION` : défaut ; `outputTokenLimit` sous le plafond : rien ne part ».

**C-5. Lignes 9 et 10.** Ajouter à la fin de la ligne 9, avant le point final : « ; si le modèle est de Google, règle des appels à Google tenue par code (GO-2026-11-21-71) ». La ligne 10 dit « même formule, mêmes cases et même plafond conditionnel que la ligne 9 » : ajouter « et la même clause de Google ».

**C-6. Lignes 1, 4 et 8 : le recalcul suit la règle.**
- Ligne 1, remplacer « ramené à 2 fois la projection refaite sur les compteurs de l'essai de mesure si elle est plus basse » par « ramené par la règle 5.1 de ce devis (marge 2 sur la projection refaite aux compteurs de l'essai de mesure, plus la réserve d'un envoi, arrondi aux 5 USD supérieurs) s'il est plus bas ».
- Ligne 4, remplacer « plafond 55 USD au plus, ramené à 2 fois la projection sur les compteurs de son essai d'admission si elle est plus basse ; tenu par compteur et par une borne dure en octets par envoi » par « sortie maximale par la règle 7 du texte, 71 680 au plus, borne dure de huit octets par jeton de sortie maximale ; plafond 55 USD au plus, ramené par la règle 5.1 (marge 2) s'il est plus bas ; régime prudent ».
- Ligne 8, remplacer « ramené à 2 fois la projection sur le coût compté à la ligne 7 si elle est plus basse ; mêmes suppositions et mêmes règles que la ligne 7 » par « ramené par la règle 5.1 de ce devis (marge 2 sur le coût compté à la ligne 7, plus la réserve d'un envoi, arrondi aux 5 USD supérieurs) s'il est plus bas ; même sortie maximale, mêmes suppositions et mêmes règles que la ligne 7 ».
- Lignes 2 et 5, remplacer « plafond recalculé par programme à 1,5 fois la projection sur les coûts comptés à ses lots d'épreuve » par « plafond recalculé par programme par la règle 5.1 de ce devis sur les coûts comptés à ses lots d'épreuve (marge 1,5 à l'appariement, 2 à la couverture) » ; ligne 2, ajouter avant « ne part qu'après » : « pire cas tenu par les gardes : le plafond et [valeur] USD ; compté à [entrée] et [sortie] USD par million ; ».

Les textes ainsi corrigés font 545, 523, 547, 529, 548 et 430 signes (lignes 1, 2, 4, 5, 7, 8 ; compté par programme).

**C-7. Décision 6, à ajouter.**
> **Décision 6 — Le pire cas et le versement chez Google pour les lignes du juge.**
> - **Décision** : accepter, pour les lignes 7 et 8, un pire cas de 28,07 USD chacune sans borne dure, et verser sur chaque projet de quoi atteindre le seuil de la ligne ; ou autrement.
> - **Enjeu** : chez Google, recharge automatique activée et aucun plafond de dépense (GO-2026-11-21-68). Lazar a accepté 84,06 USD pour les essais ; l'avenant 2 les porte à 89,67. Les deux lignes du juge ajoutent 56,14 USD au régime prudent : 145,81 avec le pire cas des essais (C). Seuil d'une ligne du juge : 28,07 USD par projet, dépense retirée, soit au moins 26,89 € vus au taux relevé de l'avenant 2 (1,0990 USD pour 1 €, moins 5 %) (C) ; les deux soldes vus avant les essais, 11,93 € et 15,59 €, ne le couvrent pas.
> - **Option (a)** : accepter et verser avant la ligne 7, au solde vu après les essais, pièce de constat neuve. Avantage : la ligne ne s'arrête pas pour une raison de caisse. Inconvénient : un paiement, et un solde immobilisé sur deux projets.
> - **Option (b)** : servir le juge de la course sur une seule clé. Avantage : un seul projet à garnir. Inconvénient : une voie que quatre lectures seulement auront éprouvée (avenant 1, version 3) : à écrire au texte.
> - **Recommandation** : (a). Confiance : moyenne. **Pas de défaut** : c'est un paiement.

## 9. Mineurs

- m-1 : 4.4 et 5.2, « environ 14 900 » → « environ 15 000 » (C : 14 990 ; la section 13 du devis dit 14 994).
- m-2 : signaler en section 10 l'écart « 160 artefacts » / 128 appels de 6.11, et qu'à 160 le maximum de la ligne 4 serait passé.
- m-3 : tableau d'exemples de 4.5 : prendre des prix ronds qui ne soient le tarif d'aucun lecteur de ce devis.
- m-4 : 4.5, « s'il lit lui aussi l'action dans son contexte (S) » → une case du côté habilité : « entrée d'une lecture [case] ».
- m-5 : 4.4, « c'est l'affaire du rédacteur du texte » → « valeurs à inscrire par un lecteur habilité (avenant 2, section 9) ».
- m-6 : garde 7, ajouter `CONTINUATION` aux fins en défaut (couvert par C-4).
- m-7 : le « pire cas tenu par les gardes » compte l'envoi coupé entier ; l'avenant 2 n'en compte que l'excès sur la réserve (27,02 au lieu de 28,07 pour le juge, C). Prudent ; à dire, non à changer.
- m-8 : citer le brouillon 44 (`b30aa902…`), dont la section 6.11 est identique.

## 10. Ce que j'ai ouvert

| pièce | empreinte vérifiée | lu |
|---|---|---|
| mandat du rédacteur | `86c98be8…` | en entier |
| devis vérifié | `70adb048…` | en entier |
| `devis-hors-carte-programmes-v1/` (5 fichiers) | égales aux compagnons | `faire_hc1.py` et l'en-tête de `controle_hc1.py` lus ; `calc_hc1.py` non lu avant mon propre calcul, ni exécuté |
| `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md` | `4f91b535…` | section 6.11 seule, par la commande du mandat |
| `prereg/T0.7-organismes-discrets-v-a-v2-brouillon44.md` | `b30aa902…` | section 6.11 seule, même commande, pour la comparer |
| `devis-bras-a-v2.md` | `83240ca6…` | en entier |
| `devis-essais-admission-mistral-neon-bras-a-v1.md` | `421ee2e6…` | sections 5, 6.1 à 6.5, 7 et l'index des titres |
| `avenant-1-…-v3.md` | `5e255c5f…` | par recherche de lignes (soldes, deux clés) |
| `avenant-2-…-65536-v1.md` | `5f84642a…` | sections 0 à 5, 8 à 10 |
| pages de prix (trois pages, index) | `sha256sum -c` : toutes « OK » | prix de Mistral, ligne de l'inférence régionale, section de Gemini 4 Neon, par programme |
| sept pièces `mots-de-lazar-*` | égales à celles du devis | en entier |
| `CLAUDE.md` sur `origin/main` | — | section « Appels aux modèles de Google », par la commande du mandat |
| `registres/go.md` sur `origin/main` | — | GO-2026-11-21-63, -68, -69, -71, par `grep` de chaque identifiant |

Rien d'autre : aucun chemin cloisonné, aucune pièce du côté habilité, aucun réseau, aucun appel de modèle, aucune clé. Le programme et sa sortie (sha256 `e3c61bee…`) sont dans le bloc-notes de la session, `/tmp/claude-0/-home-user-controle-ia-travail/080a2aff-9781-5a4d-8af3-2aae94066157/scratchpad/verif-hc/` ; leur texte est recopié en annexe. Fichier écrit dans le dépôt : celui-ci seul, sans compagnon d'empreinte.

## Annexe A — `verif_hc.py`

```python
# Vérification indépendante du devis des lectures hors carte, brouillon 1.
# Écrit sans lire calc_hc1.py ; entrées recopiées des pièces (6.11 ; devis des essais 6.2 ; pages de prix).
from fractions import Fraction as F
import math
def r2(x): return f"{float(x):.4f}"
def up(x, pas): return math.ceil(float(x)/pas - 1e-12)*pas
# 1. Volumes, section 6.11
lots = {  # (appels par lecteur, instrument, phase)
 "honnete_app": (640+128+64+64, "a", "epr"),
 "jumeaux_app": (640+640, "a", "epr"),
 "honnete_couv": (64, "c", "epr"),
 "meca_couv": (128, "c", "epr"),
 "jumeaux_couv": (128, "c", "epr"),
 "dec_app": (7*128*10, "a", "dec"),
 "dec_sent": (256+320, "a", "dec"),
 "dec_couv": (896+32, "c", "dec"),
 "revision": (2176, "a", "rev"),
}
n = {(i,p):0 for i in "ac" for p in ("epr","dec","rev")}
for k,(v,i,p) in lots.items(): n[(i,p)] += v
tot = lambda p: n[("a",p)]+n[("c",p)]
print("par phase:", {p: (n[("a",p)], n[("c",p)], tot(p)) for p in ("epr","dec","rev")})
sansrev = tot("epr")+tot("dec"); avec = sansrev+tot("rev")
print("par lecteur", sansrev, avec, "deux lecteurs", 2*sansrev, 2*avec)
print("appariement", sum(n[("a",p)] for p in ("epr","dec","rev")), "couverture", sum(n[("c",p)] for p in ("epr","dec","rev")))
juge = 48+24+8; jrev = 72
print("majorant envois", 3*(2*sansrev + 2*tot("rev") + juge + jrev))
# 2. Longueurs
ea, ec = F(23625,18), F(31591,6); ga, gc = F(5159,6), F(7933,2)
ent = {p: n[("a",p)]*ea + n[("c",p)]*ec for p in ("epr","dec","rev")}
print("entrée par lecteur", {p: float(v) for p,v in ent.items()}, float(sum(ent.values())))
mon = 6400*(2643+223)
jin = 72*ga+8*gc; jinrev = jin + 72*ga
print("juge entrée", float(jin), float(jinrev), "moniteur", mon)
print("total entrée M", float(2*(ent["epr"]+ent["dec"]) + jin + 2*mon)/1e6, float(2*sum(ent.values()) + jinrev + 2*mon)/1e6, float(2*sum(ent.values()) + jinrev + mon + 8960*2866)/1e6)
# 3. Prix
pe, ps = F(77,100), F(231,100); ge, gs = F(3), F(15); kk = 1+F(2,24)
ca = (ea*pe + 2000*ps)/10**6; cc = (ec*pe + 4000*ps)/10**6
m = {p: kk*(n[("a",p)]*ca + n[("c",p)]*cc) for p in ("epr","dec","rev")}
print("Mistral appel", r2(ca), r2(cc), "phases", {p: r2(v) for p,v in m.items()}, "total", r2(sum(m.values())))
print("recoupe essais Mistral 18a+6c", r2(18*ca+6*cc))
gja = (ga*ge+2000*gs)/10**6; gjc = (gc*ge+4000*gs)/10**6
j80 = kk*(72*gja+8*gjc); j72 = kk*72*gja
print("recoupe essais Neon 6a+2c", r2(6*gja+2*gjc), "juge 80", r2(j80), "72", r2(j72))
j80c = kk*80*gjc; j72c = kk*72*gjc
# Premier lecteur
P = F(1464,10)
def rep(rho):
    x = P/(13888+1248*rho)
    return {p: n[("a",p)]*x + n[("c",p)]*rho*x for p in ("epr","dec","rev")}
for rho in (1,2,4): print("lecteur1 rho", rho, {p: r2(v) for p,v in rep(rho).items()})
hi = {p: max(rep(1)[p], rep(4)[p]) for p in ("epr","dec","rev")}
# Réserves
def res_mistral(S, couv=True):  # borne en octets 8S, +64, entrée 24000 octets
    return (24000 if couv else 5000)*pe/10**6 + (8*S+64)*ps/10**6
def res_google(S): return 24000*ge/10**6 + S*gs/10**6
print("réserves Mistral", [r2(res_mistral(S)) for S in (8192,16384,32768)], "Google", [r2(res_google(S)) for S in (32768,65536)])
# Plafonds
pl = {}
pl[1]=up(2*hi["epr"]+1,5); pl[2]=up(2*hi["dec"]+1,5); pl[3]=up(2*hi["rev"]+1,5)
pl[4]=up(3*m["epr"]+F(63,100),5); pl[5]=up(3*m["dec"]+F(63,100),5); pl[6]=up(3*m["rev"]+F(63,100),5)
pl[7]=up(3*j80c+F(106,100),5); pl[8]=up(3*j72c+F(106,100),5)
print("plafonds", pl, "somme", sum(pl.values()), "sans rev", sum(pl.values())-pl[3]-pl[6]-pl[8], "premier", pl[1]+pl[4]+pl[7])
att = P + sum(m.values()) + j80 + j72
print("attendu", r2(att), "sans rev", r2(P-hi["rev"]+m["epr"]+m["dec"]+j80), r2(P-min(rep(1)["rev"],rep(4)["rev"])+m["epr"]+m["dec"]+j80), "premières", r2(rep(1)["epr"]+m["epr"]+j80), r2(rep(4)["epr"]+m["epr"]+j80))
# Envoi coupé
mc = 538000*ps/10**6; gcut = 538000*gs/10**6
print("coupé 2690s Mistral", r2(mc), "Google", r2(gcut), "890s Google", r2(178000*gs/10**6))
# Crédit
for nom, x in (("M epr",pl[4]+mc),("M dec",pl[5]+mc),("M rev",pl[6]+mc),("M 3",pl[4]+pl[5]+pl[6]+3*mc),("G",pl[7]+gcut)):
    c = up(x*F(115,100),0.5); print("crédit", nom, r2(x), c, round(c*1.2,2))
# Majorant vrai Mistral
for S in (8192,16384,32768):
    e_a = 5000*pe/10**6 + S*ps/10**6; e_c = 24000*pe/10**6 + S*ps/10**6
    print("majorant Mistral", S, r2(3*(13888*e_a+1248*e_c)))
for S in (32768,65536):
    print("majorant juge", S, r2(3*80*res_google(S)), r2(3*152*res_google(S)))
# --- Chiffres neufs de la vérification ---
# (a) Marge de 1,5 par instrument : la couverture n'a que 320 lectures réelles aux lots d'épreuve
a_dec = kk*n[("a","dec")]*ca; c_dec = kk*n[("c","dec")]*cc
print("Mistral décisif, 1,5 partout", r2(F(3,2)*m["dec"]+F(63,100)), "->", up(F(3,2)*m["dec"]+F(63,100),5))
print("Mistral décisif, 1,5 app et 2 couv", r2(F(3,2)*a_dec+2*c_dec+F(63,100)), "->", up(F(3,2)*a_dec+2*c_dec+F(63,100),5))
# (b) sortie maximale jusqu'où les maxima tiennent
for nom, base, plaf, couv in (("M epr",3*m["epr"],55,True),("M dec",3*m["dec"],220,True),("M rev",3*m["rev"],45,True)):
    reste = plaf - base  # réserve admise
    S = (reste - 24000*pe/10**6)*10**6/ps/8 - 8
    print("sortie max admise par le maximum,", nom, int(S), "-> multiple de 1024 inférieur", int(S)//1024*1024)
for nom, base in (("juge 80",3*j80c),("juge 72",3*j72c)):
    reste = 20 - base; S = (reste - 24000*ge/10**6)*10**6/gs
    print("sortie max admise,", nom, int(S), int(S)//1024*1024)
print("règle 7 au plus, Mistral (essai à 32 768)", 4*32768, "réserve", r2(res_mistral(4*32768)), "; Neon (essai à 65 536)", 4*65536, "réserve", r2(res_google(4*65536)))
print("juge plafond 80 à réserve 262144:", up(3*j80c+res_google(262144),5))
# (c) Avenant 2 : pire cas Google
print("essais Google, régime prudent avenant 2 + deux lignes juge", r2(F(3297,100)+2*(pl[7]+gcut)), "; pire cas accepté actualisé 89,67 + 56,14 =", r2(F(8967,100)+2*(pl[7]+gcut)))
print("pire cas juge, plafond + (coupé - réserve)", r2(pl[7] + gcut - res_google(65536)))
# (d) seuil en euros au taux relevé de l'avenant 2
t = F(10990,10000)*F(95,100)
print("seuil 28,07 USD en euros vus à 1,0990", math.ceil(float((pl[7]+gcut)/t)*100)/100)
# (e) 14 994 : sortie moyenne que tolère le plafond du juge
print("tolérance juge", float(((20-F(106,100))/80 - gc*ge/10**6)*10**6/gs))
# (f) juge, part couverture si 48+24 = appariement
print("juge 80 si 48 app + 24 couv + 8 couv", r2(kk*(48*gja+32*gjc)))
# (g) 102 lectures par action
print("si 102 appels par action:", 6400*102, "jetons d'entrée M", 6400*102*2866/1e6)
```

## Annexe B — sa sortie

```
par phase: {'epr': (2176, 320, 2496), 'dec': (9536, 928, 10464), 'rev': (2176, 0, 2176)}
par lecteur 12960 15136 deux lecteurs 25920 30272
appariement 13888 couverture 1248
majorant envois 91272
entrée par lecteur {'epr': 4540853.333333333, 'dec': 17402074.666666668, 'rev': 2856000.0} 24798928.0
juge entrée 93640.0 155548.0 moniteur 18342400
total entrée M 80.664296 86.438204 93.775164
Mistral appel 0.0056 0.0133 phases {'epr': '17.8819', 'dec': '71.5332', 'rev': '13.2733'} total 102.6884
recoupe essais Mistral 18a+6c 0.1811
recoupe essais Neon 6a+2c 0.3393 juge 80 3.1643 72 2.5412
lecteur1 rho 1 {'epr': '24.1421', 'dec': '101.2110', 'rev': '21.0469'}
lecteur1 rho 2 {'epr': '25.1625', 'dec': '101.7938', 'rev': '19.4438'}
lecteur1 rho 4 {'epr': '26.7986', 'dec': '102.7281', 'rev': '16.8732'}
réserves Mistral ['0.1700', '0.3214', '0.6242'] Google ['0.5635', '1.0550']
plafonds {1: 55, 2: 210, 3: 45, 4: 55, 5: 220, 6: 45, 7: 20, 8: 20} somme 670 sans rev 560 premier 130
attendu 254.7939 sans rev 217.9325 222.1062 premières 45.1883 47.8449
coupé 2690s Mistral 1.2428 Google 8.0700 890s Google 2.6700
crédit M epr 56.2428 65.0 78.0
crédit M dec 221.2428 254.5 305.4
crédit M rev 46.2428 53.5 64.2
crédit M 3 323.7283 372.5 447.0
crédit G 28.0700 32.5 39.0
majorant Mistral 8192 1088.8747
majorant Mistral 16384 1948.1539
majorant Mistral 32768 3666.7123
majorant juge 32768 135.2448 256.9651
majorant juge 65536 253.2096 481.0982
Mistral décisif, 1,5 partout 107.9298 -> 110
Mistral décisif, 1,5 app et 2 couv 114.6123 -> 115
sortie max admise par le maximum, M epr 72275 -> multiple de 1024 inférieur 71680
sortie max admise par le maximum, M dec 291222 -> multiple de 1024 inférieur 290816
sortie max admise par le maximum, M rev 279306 -> multiple de 1024 inférieur 278528
sortie max admise, juge 80 82275 81920
sortie max admise, juge 72 206901 206848
règle 7 au plus, Mistral (essai à 32 768) 131072 réserve 2.4408 ; Neon (essai à 65 536) 262144 réserve 4.0042
juge plafond 80 à réserve 262144: 25
essais Google, régime prudent avenant 2 + deux lignes juge 89.1100 ; pire cas accepté actualisé 89,67 + 56,14 = 145.8100
pire cas juge, plafond + (coupé - réserve) 27.0150
seuil 28,07 USD en euros vus à 1,0990 26.89
tolérance juge 14990.033333333333
juge 80 si 48 app + 24 couv + 8 couv 4.1867
si 102 appels par action: 652800 jetons d'entrée M 1870.9248
```
