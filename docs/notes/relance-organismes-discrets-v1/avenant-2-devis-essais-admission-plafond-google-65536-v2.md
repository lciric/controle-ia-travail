# Organismes discrets, bras A — avenant 2 au devis des deux essais d'admission : plafond de sortie de Google à 65 536 — note d'écart — v2

- **Objet** : dire ce qu'une décision de la session mère change au devis accepté des deux essais d'admission (`docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md`, sha256 `421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc`) et à son avenant 1, version 3 (`docs/notes/relance-organismes-discrets-v1/avenant-1-devis-essais-admission-recharge-et-deux-cles-v3.md`, sha256 `5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac`). Les deux empreintes sont recalculées ici et égales à leurs compagnons. Ni le devis ni l'avenant 1 ne sont réécrits : cet avenant se lit avec eux, et prime là où il les contredit.
- **La décision**, telle que mon mandat me la donne (`docs/notes/relance-organismes-discrets-v1/mandat-redacteur-fable-avenant-2-plafond-65536-v1.md`, sha256 `55a083304f64c3d27d7dd54698f62c631043c898c98352648ec7eeab5c5f5ff3`) : la session mère l'a prise sous GO-2026-11-21-69, en application de la règle permanente de Lazar sur les appels aux modèles de Google (GO-2026-11-21-71). Pour le juge des deux ancres `gemini-4-neon` et pour la vérification de ses deux clés :
  1. le plafond de sortie passe de 32 768 à **65 536** jetons ;
  2. le **niveau de réflexion le plus haut est gardé** ;
  3. la **sonde de borne est exemptée** du contrôle « réflexion plus 16 000 » ;
  4. pour le taux de change, le **dernier fixage publié** est admis quand aucun plus récent n'existe.
- **État** : version 2, brouillon, écrite le 2026-11-21 vers 22:39, temps universel (`date -u`), par un rédacteur neuf (Claude Opus 5.5), sur décision de Lazar (GO-2026-11-21-84) : Opus 5.5 « écrit seulement les corrections, mot pour mot d'après les remarques déjà reçues » ; un Fable 5.2 relira. Il n'a écrit ni le devis, ni les avenants, ni la version 1, ni sa vérification, ni le programme, et n'a lu aucune pièce du côté habilité. **Les corrections viennent de deux sources, et d'elles seules** : la vérification de la version 1 (`docs/notes/relance-organismes-discrets-v1/verification-avenant-2-devis-essais-admission-v1.md`, sha256 `037aa7f7f46aca8aa609fcbf70af4a3a643ff6adc8be1d09ccb039775ebc7776`, égale à son compagnon) ; la décision de la mère sous GO-2026-11-21-69 (R-4682), entrée OD-315 du journal. Chaque changement est dit, avec sa source et son texte avant et après, à la section 13. La version 1 (sha256 `5f84642a…`) n'est pas touchée ; écrite le 2026-11-21 vers 19:02 par un rédacteur neuf (Claude Fable 5.2), elle parle à la première personne : ce « je », dans les passages gardés, est le sien. **Non scellée, non contre-lue, non acceptée.** C'est une pièce de devis : aucune ligne de calcul ne s'appuie sur elle avant sa relecture par un autre modèle.
- **Ce que cet avenant ne change pas** : les trois lignes de Mistral (sortie maximale de 32 768 jetons, bornes en octets, plafonds de 0,25, 4,75 et 0,25 USD, excès, délais) ; les critères et les huit règles d'admission ; le partage de la file du juge entre les deux clés ; les délais en secondes ; le corps de la sonde (256 jetons, message fixe) ; les prix comptés ; l'attendu (≈ 0,57 USD) ; les suppositions du devis sur le débit et sur la coupure d'un envoi ; les vingt-huit clés de la pièce de constat.
- **Marques** : (C) calculé ici, par programme (section 12) ; (D) repris du devis ; (S) supposé, sans mesure ni pièce.

## 0. En une page

1. **Chez Google, les plafonds en dollars doublent à peu près.** File du juge : **16,50 USD** au lieu de 8,50. Chaque vérification de clé : **3,00 USD** au lieu de 1,50. L'excès possible d'un seul envoi baisse : 7,09 USD à la file (7,58), 1,69 USD à une vérification (2,18). Somme des six plafonds : **27,75 USD** au lieu de 16,75 (C). Rien ne change chez Mistral.
2. **Pire cas chez Google : 89,67 USD au régime courant, sans borne dure. Lazar en a accepté 84,06** (GO-2026-11-21-68). Le chiffre accepté est dépassé de 5,61 USD : **c'est un écart au GO-2026-11-21-68 et un nœud de Lazar. Aucune ligne de Google ne part sur ce chiffre sans son mot, ou sans un levier qui le ramène sous 84,06 (section 10).** Au régime prudent, ou si la supposition de la sonde tient : 32,97 USD au lieu de 23,44 (C). **Le nœud est tranché** : la mère, sous GO-2026-11-21-69 (R-4682 ; journal, entrée OD-315), a retenu le levier (a) de la vérification (option (B) de sa décision 1) : « régime prudent pour les lignes de Google, en vérification comme en file » ; **le pire cas chez Google est de 32,97 USD**, sous les 84,06 acceptés (C, section 12.2).
3. **Seuils de crédit, par projet** : **28,28 USD** avant chaque vérification de clé (19,76 à l'avenant 1), **23,59 USD** avant la file (16,08). Ils se lisent sur le solde seul de chaque projet, la somme des deux dépenses retirée (C).
4. **Il manque de l'argent sur les deux projets, et aucune ligne de Google ne part en l'état, pas même une vérification.** Au taux relevé (1,0990 USD pour 1 €, diminué de 5 %), pour que les trois lignes passent même au pire, chaque projet doit montrer **31,58 €**. Il manque **19,65 €** au projet à 11,93 € et **15,99 €** au projet à 15,59 €, soit 35,64 € en tout. Après le versement accordé sous GO-2026-11-21-74 (10,47 € et 6,81 €), il manque 9,18 € sur chacun. Au plus juste : 27,11 € par projet, soit 15,18 € et 11,52 € à verser. Verser est un paiement : il reste à Lazar (section 3).
5. **La borne de réflexion à déclarer est 49 536 jetons, et elle ne se justifie pas sans relevé ; les pages de Google versées ne la fondent pas : elle reste supposée** (section 4). C'est 65 536 moins 16 000 : la plus grande valeur que la garde accepte. Aucune pièce lue ne borne la réflexion du niveau le plus haut, pas même ces pages. La garde d'avant l'envoi vérifie alors une soustraction ; ce qui protège, ce sont les contrôles d'après la réponse : une réflexion facturée au-delà de la borne est un défaut, qui arrête la file sans qu'elle tienne, et rend une vérification non saine (nœud de Lazar).
6. **Délais : inchangés en secondes. Ils ne tiennent à 65 536 que si le service rend 24,4 jetons par seconde ou plus**, contre 12,2 au devis ; ce débit n'est pas mesuré (section 5). Le plafond neuf ne fait échouer aucune lecture qui tenait à 32 768, si la réflexion du modèle ne dépend pas du plafond envoyé (S).
7. **L'exemption de la sonde est écrite en section 6.** Elle ne couvre que le contrôle du plafond d'avant l'envoi. La sonde garde un réglage de réflexion explicite et ne produit aucune lecture jugée.
8. **Âge du taux** : la règle neuve est écrite en section 7, sous une forme que le programme peut vérifier sans réseau.
9. **À dire à Lazar** (section 10) : le pire cas dépassé, et le nœud tranché par la mère (journal, entrée OD-315) ; le versement ; et ceci : la décision remplace, pour Google, un mot de Lazar (« goreco », 32 768) par une décision de la mère, sur un point que la confrontation à la règle rangeait parmi les nœuds de Lazar, comme l'exemption de la sonde.

## 1. Les écarts, cités à la lettre

Les numéros de ligne sont ceux des fichiers cités, aux empreintes dites. Les 127 citations de cet avenant sont confrontées par programme à leur source (section 11). Les sections 16 à 19 du devis et 10 à 13 de l'avenant 1 racontent des versions passées ou portent des calculs : elles ne sont pas citées.

### 1.1 La sortie maximale envoyée à Google : le mot « goreco » remplacé, pour Google seulement

Le devis fixait 32 768 jetons « aux deux » par un mot de Lazar, « goreco » (devis, lignes 34 à 37 ; pièce `mots-de-lazar-devis-essais-admission-bras-a-2026-11-21-v1.md`, `9b9ee5ca…` selon le devis, non ouverte ici). La décision le remplace **pour Google seulement**. **Chez Mistral, rien ne bouge** : 32 768 jetons, les bornes de 262 144 et de 32 768 octets, les trois plafonds.

| ligne | section | ce que le devis écrit | ce que la décision en fait |
|---|---|---|---|
| 17 | 0, point 5 | « **Sortie maximale envoyée : 32 768 jetons aux deux** (décidé par Lazar) » | Google : 65 536 ; Mistral : 32 768, inchangé |
| 36 | 1, mot « goreco », décision 2 | « **la sortie maximale envoyée aux deux files est de 32 768 jetons**, à revoir si les délais ne tiennent pas » | remplacé pour Google seulement |
| 101 | 4.2, appel A | « **Son corps porte exactement les réglages de la file** : même sortie maximale » | lettre inchangée : les appels A et A′ de Google portent donc 65 536 |
| 130 | 4.4, ligne 2 | « Google : `outputTokenLimit` rendu par l'appel de liste, sous 32 768 » | « sous 65 536 » : aucun appel payant, et la décision est à reprendre |
| 162 | 4.6 | « Sortie maximale : **256** (`max_tokens: 256` ; `maxOutputTokens: 256`) » | inchangé : la sonde garde 256, sous l'exemption de la section 6 |
| 188 | 4.6, limites | « elle suppose que la borne se comporte de même à 32 768 » | « à 65 536 » |
| 201 | 5.1 | « niveau de réflexion le plus haut, `xhigh` \| **32 768** \| sans flux » | 65 536 ; le niveau le plus haut est gardé |
| 211 | 5.3 | « `generationConfig.maxOutputTokens: 32768` » | `65536` |
| 215 | 5.4 | « **32 768 jetons aux deux : décidé par Lazar** (section 1) » | de même que la ligne 17 |
| 221 | 5.4, part 1 | « **Une sortie facturée au-dessus de 32 768 n'arrête plus la file** » | chez Google : au-dessus de 65 536 |
| 263 | 5.6 | « une réponse de 32 768 jetons tient dans 2 690 secondes si le service rend **12,2 jetons par seconde ou plus** (C) » | Google : 65 536 jetons, 24,4 jetons par seconde (section 5) |
| 337 | 6.4 | « Google, file \| 32 768 jetons, la sortie maximale envoyée \| 0,507 ; 0,564 » | 65 536 jetons ; 0,999 ; 1,056 |
| 338 | 6.4 | « Google, vérification \| 32 768 jetons \| 0,492 » | 65 536 jetons ; 0,984 |
| 343 | 6.4, régime courant | « chez Google, 32 768 jetons de sortie » ; « sous la supposition que la borne se comporte à 32 768 comme à 256 » | 65 536, aux deux endroits |
| 532 | 10, garde 3 | « le corps porte la sortie maximale de sa ligne (32 768 ; 256 à la sonde) » ; « corps sans sortie maximale, à 65 536 » | à Google, 65 536 est la valeur saine et 32 768 un artefact ; chez Mistral, rien ne change |
| 571 | 11 | « **la sortie maximale de 32 768 ne tient dans les délais que si le service rend 12,2 jetons par seconde ou plus, débit non mesuré** » | ligne 4 : 65 536 et 24,4 ; ligne 3 : inchangée |

### 1.2 Les chiffres en dollars du devis qui en découlent

| ligne | section | ce que le devis écrit | valeur neuve (C, section 2) |
|---|---|---|---|
| 13 | 0, point 1 | « File Neon : 8 appels, 16 envois au plus, plafond **8,50 USD**. » | 16,50 USD |
| 14 | 0, point 2 | « Google, plafond **1,50 USD** » | 3,00 USD, pour chacune des deux vérifications |
| 24 | 0, point 12 | « au plus 2,18 USD à la vérification, 7,58 USD à la file » | 1,69 et 7,09 USD |
| 134 | 4.4, ligne 6 | « cela passe le plafond de la ligne, chez Google (2,68 USD contre 1,50) » | 2,68 ne passe plus 3,00 ; la ligne s'arrête quand même : 3,66 avec la réserve de l'envoi suivant (2.4) |
| 181 | 4.6, texte porté à Lazar | « le plafond de 8,50 USD est tenu par compteur si la sortie maximale borne la réflexion ; sinon, excès possible d'un seul envoi, au plus 7,58 USD au débit déclaré de 200 jetons par seconde (S), soit 16,08 USD au plus pour la file » ; « **un envoi coupé au délai de 45 minutes arrête la file, sans reprise, et elle ne tient pas** » | 16,50 ; 7,09 ; 23,59 ; la seconde phrase ne vaut plus telle quelle (2.4) |
| 183 | 4.6 | « est d'au moins 16,08 USD (plafond et excès de la file) » | 23,59 USD, par projet (section 3) |
| 192 | 4.6, limites | « c'est l'excès de la ligne 2 (6.4), 2,18 USD au débit déclaré » | 1,69 USD |
| 307 | 6.3 | « 0,507 ; 0,564 \| 8,33 \| 0,507 ; 0,564 \| **8,50** \| 7,58 \| 12,50 » | 0,999 ; 1,056 ; 16,20 ; 16,50 ; 7,09 ; 24,30 |
| 310 | 6.3 | « 0,492 \| 1,48 \| 0,492 \| **1,50** \| 2,18 » | 0,984 ; 2,96 ; 3,00 ; 1,69 |
| 311 | 6.3 | « 14,26 \| \| **15,25** \| 12,74 » | à six lignes : 26,57 ; 27,75 ; 13,45 |
| 345 | 6.4 | « Un envoi qui dure moins de 164 secondes chez Google » ; « Un appel de vérification de Google coupé à 890 secondes est compté 2,68 USD, au-dessus du plafond de 1,50 » ; « avec la réserve de l'envoi suivant, cela passe 8,50, et **la file s'arrête, sans reprise** » | 328 secondes ; 2,68, sous 3,00, l'envoi suivant refusé ; à 16,50, la reprise part (2.4) |
| 346 | 6.4 | « le régime prudent compterait 8,09 USD un envoi de Neon coupé au délai de 45 minutes, et la file s'arrêterait sans la reprise que la règle 1 lui donne » | ne vaut plus pour un premier envoi coupé (2.4) |
| 370 | 6.4, cas 3 | « 7,93 USD chez Neon (envoi de couverture) » ; « Chez Neon, 8,33 au plus, sous 8,50. » | 15,44 ; 16,20 au plus, sous 16,50 |
| 380 | 6.4 | « \| 1,50 \| **2,18** \| 0,85 \| 4,85 \| » | 3,00 ; 1,69 ; 0,36 ; 4,36 |
| 381 | 6.4 | « \| 8,50 \| **7,58** \| 3,55 \| 15,65 \| » | 16,50 ; 7,09 ; 3,06 ; 15,16 |
| 383 | 6.4 | « 3,68 USD pour la ligne 2 ; 16,08 pour la ligne 4 » | 4,69 ; 23,59 |
| 389 | 6.4 | « soit 72,77 USD au débit déclaré, contre 4,56 comptés » | 72,77 inchangé ; 8,99 comptés ; borne de la file : 80,29 |
| 433 | 6.5 | « crédit prépayé vu d'au moins **19,76 USD** » | 28,28 USD, par projet |
| 434 | 6.5 | « au moins **16,08 USD**, plafond et excès de la file » | 23,59 USD, par projet |
| 450 | 6.6 | « plafond 8,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi 7,58 USD à 200 jetons par seconde » | 16,50 et 7,09 ; pour une vérification, 3,00 et 1,69 |
| 530 | 10, garde 1 | « 32 768 jetons chez Google » ; « le premier est compté au-dessus du plafond, le deuxième n'est pas envoyé, la ligne s'arrête » ; « file Neon partie sur un mot de Lazar, envoi coupé à son délai total : la reprise est refusée, file arrêtée à son plafond » | 65 536 ; le premier est compté sous le plafond (2,68), le deuxième n'est pas envoyé ; la reprise part, et un second envoi coupé à 45 minutes arrête la file |
| 539 | 10, garde 10 | « est d'au moins 16,08 USD » | 23,59 USD |
| 558 | 11 | « **1,50 USD** \| 2,18 USD, si la sortie maximale ne borne pas la réflexion » | 3,00 USD ; 1,69 USD |
| 560 | 11 | « **8,50 USD** \| 7,58 USD, si la sortie maximale ne borne pas la réflexion » | 16,50 USD ; 7,09 USD |
| 563 | 11 | « Total des plafonds : **15,25 USD** » ; « Plafonds et excès ensemble : 27,99 USD » | à six lignes : 27,75 ; 41,20 |
| 565 | 11 | « au plus 2,18 USD (ligne 2, délai de 900 secondes) ou 7,58 USD (ligne 4) » | 1,69 ou 7,09 |
| 571 | 11 | « à la ligne 4, un envoi coupé au délai de 45 minutes arrête la file, sans reprise » | ne vaut plus telle quelle (2.4) |
| 624 | 13, point 12 | « elle peut coûter jusqu'à 0,49 USD par appel chez Google » | 0,99 USD |
| 640 | 13, point 28 | « son prix serait une file Neon arrêtée sur un seul délai de 45 minutes, sans la reprise de la règle 1 » | ne vaut plus : à 16,50, la reprise part après un premier envoi coupé (2.4) |

Les lignes 586 et 588 du devis (textes des lignes de calcul 2 et 4) ont déjà été récrites par l'avenant 1 : c'est son texte que la section 8 remplace. Les chiffres du schéma de la recharge à 23,00 USD (23,00 ; 22,72 ; 19,32 ; 12,32 ; 15,98 ; 22,98 ; 3,76 ; 0,44 ; 12,18 ; 23,66) ne sont pas refaits : l'avenant 1 les a retirés (ses tableaux 1.2 et 1.3).

### 1.3 L'avenant 1, version 3

| ligne | section | ce que l'avenant 1 écrit | ce que la décision en fait |
|---|---|---|---|
| 9 | en-tête | « aucun plafond de ligne (0,25 ; 1,50 ; 4,75 ; 8,50 ; 0,25 USD), aucun excès d'un envoi » ; « les valeurs des seuils de crédit (19,76 et 16,08 USD) » | les deux plafonds de Google, leurs excès et les deux seuils changent : 3,00 et 16,50 ; 1,69 et 7,09 ; 28,28 et 23,59 |
| 14 | 0, point 1 | « **Pire cas chez Google : 84,06 USD, sans borne dure, accepté par Lazar** (GO-2026-11-21-68) » ; « 76,70 USD, et deux vérifications de clé à 3,68 USD (C) » ; « Au régime prudent, ou si la supposition de la sonde tient : 23,44 USD. » | 89,67 ; 80,29 et 4,69 ; 32,97 |
| 15 | 0, point 2 | « un seul plafond de 8,50 USD » ; « (1,50 USD de plafond) » | 16,50 ; 3,00 |
| 17 | 0, point 4 | « **Seuils de crédit** : 19,76 et 16,08 USD, inchangés » ; « **plus une recharge automatique, une seule** » | 28,28 et 23,59 ; la recharge n'est pas comptée (1.5) |
| 129 | 2.2 | « \| 1,50 \| 2,18 \| **3,68** (D, ligne 383) » | 3,00 ; 1,69 ; 4,69 |
| 130 | 2.2 | « \| 8,50 \| 7,58 \| **16,08** (D, ligne 383) » | 16,50 ; 7,09 ; 23,59 |
| 131 | 2.2 | « si la borne se comporte à 32 768 comme à 256 » | à 65 536 |
| 132 | 2.2 | « **76,70** (C : 8,50 + 9 × 7,578 = 76,702) » | 80,29 (16,50 + 9 × 7,08696) |
| 137 | 2.2 | « soit **23,44 USD** et **84,06 USD** » | 32,97 et 89,67 |
| 143 | 2.2 | « 1,50 + 4,85 + 8,50 + 15,65 = **30,50 USD** » ; « 8,50 + 9 × 15,65 = **149,35 USD** » | 39,02 et 152,92 (une seule vérification, à 400 jetons par seconde) |
| 161 | 2.4 | « **23,44 USD** au régime prudent, **84,06 USD** au cas des neuf excès (C) » | 32,97 et 89,67 |
| 162 | 2.4 | « À 400 jetons par seconde : 36,85 USD au régime prudent, 162,05 USD au cas des neuf excès (C). » | 46,38 et 167,64 |
| 163 | 2.4 | « il retirerait la reprise unique que la règle 1 donne » | ne vaut plus pour un premier envoi coupé (2.4) |
| 217 | 4.1 | « (4,17 USD d'envois finis par clé, 8,34 pour les deux, sous 8,50 ; C) » | 8,10 par clé, 16,20 pour les deux, sous 16,50 |
| 220 | 4.1 | « un plafond de 8,50 USD » | 16,50 |
| 229 | 4.2 | « le plafond est celui de la file entière, 8,50 USD » | 16,50 |
| 255 | 4.4 | « Les valeurs ne changent pas : **19,76 USD** avant une vérification de clé, **16,08 USD** avant la file (devis, 6.5). » | elles changent : 28,28 et 23,59 |
| 261 | 4.4, point 3 | « `crédit compté(P) − dépense retirée ≥ 19,76` » ; « la première a pu prendre jusqu'à 3,68 USD » | 28,28 ; 4,69 |
| 262 | 4.4, point 4 | « `crédit compté(P) − dépense retirée ≥ 16,08` » | 23,59 |
| 264 | 4.4, point 6 | « 2 × 3,68 + 16,08 = 23,44 USD » | 2 × 4,69 + 23,59 = 32,97 |
| 265 | 4.4, point 7 | « 16,08 + 7,36 = **23,44 USD** » | 23,59 + 9,38 = 32,97 |
| 333 | 6, ligne 2 | « plafond 1,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 2,18 USD » ; « avec une recharge automatique [valeur] » | texte neuf en section 8 |
| 335 | 6, ligne 6 | « plafond 1,50 USD, excès possible d'un seul envoi de 2,18 USD » | texte neuf en section 8 |
| 337 | 6, ligne 4 | « plafond 8,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 7,58 USD » ; « où un envoi coupé à 45 minutes arrête la file sans reprise » ; « pire cas chez Google, pour les lignes 2, 4 et 6 telles qu'accordées, 84,06 USD, accepté » | texte neuf en section 8 |
| 339 | 6, sommes | « plafonds, 15,25 + 1,50 = **16,75 USD** » ; « 12,74 + 2,18 = **14,92 USD** » ; « ensemble, **31,67 USD** » | 27,75 ; 13,45 ; 41,20 |
| 343 | 6, geste de paiement | « les deux soldes vus (11,93 € et 15,59 €) et une recharge automatique par projet doivent couvrir 19,76 USD sur chaque projet » | texte neuf en section 8 |
| 355 | 7, point 7 | « Avant toute vérification de Google, les deux projets à 19,76 ; avant la file, les deux projets à 16,08 » ; « la file part (19,76 − 3,68 = 16,08) » ; « la file ne part pas (19,76 − 3,70 = 16,06) » | 28,28 et 23,59 ; 28,28 − 4,69 = 23,59 ; 28,28 − 4,71 = 23,57 |
| 415 | 9, point 4 | « **Pire cas de 84,06 USD sans borne dure**, accepté. » ; « à 400 jetons par seconde, 162,05 USD » | 89,67 ; 167,64 |
| 423 | 9, point 12 | « toute ligne nouvelle de vérification y ajoute 3,68 USD » | 4,69 USD |

### 1.4 Toutes les lignes touchées, par chiffre

Relevé par programme : chaque chiffre est cherché comme un nombre entier, dans les sections 0 à 15 du devis (lignes 1 à 685) et 0 à 9 de l'avenant 1 (lignes 1 à 423). Toutes ces lignes se lisent désormais avec la valeur neuve. Parmi elles, les lignes 407 à 443 du devis portent le schéma de la recharge à 23,00 USD, que l'avenant 1 a retiré : elles sont listées pour que le relevé soit complet.

**Devis.**
- sortie maximale envoyée à Google : 32 768 devient **65 536** — lignes 5, 17, 24, 36, 130, 188, 201, 214, 215, 221, 224, 263, 302, 304, 337, 338, 343, 370, 389, 390, 530, 532, 565, 568, 571, 588, 591, 614, 619, 640.
- le même nombre, dans le corps de l'appel : 32768 devient **65536** — ligne 211.
- plafond de la file du juge : 8,50 devient **16,50** — lignes 13, 181, 201, 307, 345, 370, 381, 407, 414, 433, 450, 560, 588, 647.
- plafond d'une vérification de clé : 1,50 devient **3,00** — lignes 14, 134, 310, 345, 380, 407, 433, 558, 586.
- excès d'un envoi de la file : 7,58 devient **7,09** — lignes 24, 181, 262, 307, 381, 407, 423, 433, 450, 560, 565, 588.
- excès d'un envoi de vérification : 2,18 devient **1,69** — lignes 24, 192, 262, 310, 380, 407, 433, 558, 565, 586, 624.
- plafond et excès de la file, seuil d'avant la file : 16,08 devient **23,59** — lignes 5, 181, 183, 184, 383, 389, 414, 434, 437, 515, 539, 647.
- plafond et excès d'une vérification : 3,68 devient **4,69** — lignes 383, 412, 414, 416, 434, 435, 539.
- seuil d'avant une vérification : 19,76 devient **28,28** — lignes 407, 416, 422, 423, 433, 435, 443, 506, 515, 538, 570, 586, 647.
- réserve d'un envoi d'appariement : 0,507 devient **0,999** — lignes 307, 337.
- réserve d'un envoi de couverture : 0,564 devient **1,056** — lignes 307, 337.
- réserve d'un envoi de vérification : 0,492 devient **0,984** — lignes 310, 338.
- pire cas des seize envois : 8,33 devient **16,20** — lignes 307, 370.
- pire cas des trois envois d'une vérification : 1,48 devient **2,96** — ligne 310.
- débit qui tient la sortie pleine, pour Google : 12,2 devient **24,4** — lignes 19, 36, 263, 571, 591, 619.
- seuil de refus du compteur : 7,93 devient **15,44** — ligne 370.
- trois envois par appel, pour information : 12,50 devient **24,30** — ligne 307.
- neuf envois coupés, comptés à leur réserve : 4,56 devient **8,99** — ligne 389.
- coût d'un appel de vérification à sortie pleine : 0,49 devient **0,99** — ligne 624.
- excès de la file à 400 jetons par seconde : 15,65 devient **15,16** — ligne 381.
- excès de la file à 100 jetons par seconde : 3,55 devient **3,06** — ligne 381.
- excès d'une vérification à 400 jetons par seconde : 4,85 devient **4,36** — ligne 380.
- excès d'une vérification à 100 jetons par seconde : 0,85 devient **0,36** — ligne 380.
- pire cas à la sortie maximale, tous envois, à six lignes : 14,26 devient **26,57** — ligne 311.
- somme des plafonds, à six lignes : 15,25 devient **27,75** — lignes 15, 311, 563, 623.
- la même, sans la ligne 5 : 15,00 devient **27,50** — lignes 15, 563.
- somme des excès, à six lignes : 12,74 devient **13,45** — lignes 311, 563.
- la même, sans la ligne 5 : 11,57 devient **12,28** — ligne 563.
- plafonds et excès ensemble, à six lignes : 27,99 devient **41,20** — lignes 563, 623.
- les mêmes, sans la ligne 5 : 26,57 devient **39,78** — ligne 563.

Sont écartées de toutes les listes trois phrases d'histoire des brouillons (lignes 315, 321 et 424) ; pour « 32 768 », les lignes qui ne parlent que de Mistral ou de ses bornes en octets (169, 192, 200, 336, 350, 352, 353, 359, 368, 369, 545, 548, 585) ; pour « 32768 », la ligne 206, qui est le corps de l'appel à Mistral. Là où une ligne gardée parle des deux fournisseurs, Mistral garde 32 768. Aux lignes 19, 36, 263, 571, 591 et 619, le débit de 12,2 jetons par seconde reste celui de Mistral ; pour Google, il devient 24,4. Les 72,77 et 72,94 USD des neuf envois coupés seuls (lignes 5, 24, 389, 565, 568, 588, 597, 639, 640, 652) ne changent pas : c'est la borne de la file qui change (80,29).

**Avenant 1.**
- sortie maximale envoyée à Google : 32 768 devient **65 536** — lignes 131, 337.
- plafond de la file du juge : 8,50 devient **16,50** — lignes 9, 15, 125, 130, 131, 132, 143, 217, 220, 229, 337.
- plafond d'une vérification de clé : 1,50 devient **3,00** — lignes 9, 15, 129, 143, 333, 335, 339.
- excès d'un envoi de la file : 7,58 devient **7,09** — lignes 130, 131, 132, 337.
- le même, à trois décimales : 7,578 devient **7,08696** — lignes 125, 132.
- excès d'un envoi de vérification : 2,18 devient **1,69** — lignes 129, 333, 335, 339.
- plafond et excès de la file, seuil d'avant la file : 16,08 devient **23,59** — lignes 9, 17, 52, 54, 57, 130, 131, 135, 143, 179, 182, 184, 255, 262, 264, 265, 337, 355.
- plafond et excès d'une vérification : 3,68 devient **4,69** — lignes 14, 129, 135, 136, 137, 177, 261, 264, 265, 333, 355, 423.
- deux vérifications au pire : 7,36 devient **9,38** — lignes 264, 265.
- seuil d'avant une vérification : 19,76 devient **28,28** — lignes 9, 17, 51, 53, 56, 135, 139, 143, 180, 184, 188, 190, 255, 261, 265, 267, 333, 343, 355, 391.
- Google, deux vérifications, régime prudent ; crédit à avoir au pire : 23,44 devient **32,97** — lignes 14, 137, 161, 264, 265, 391, 402.
- file, neuf excès : 76,70 devient **80,29** — lignes 14, 125, 132, 136, 337, 420.
- Google, une vérification, neuf excès : 80,38 devient **84,98** — ligne 136.
- Google, deux vérifications, pire cas : 84,06 devient **89,67** — lignes 7, 14, 137, 161, 162, 337, 372, 415, 423.
- à 400 jetons par seconde, une vérification, régime prudent : 30,50 devient **39,02** — ligne 143.
- à 400 jetons par seconde, une vérification, neuf excès : 149,35 devient **152,92** — ligne 143.
- à 400 jetons par seconde, deux vérifications, régime prudent : 36,85 devient **46,38** — ligne 162.
- à 400 jetons par seconde, deux vérifications, neuf excès : 162,05 devient **167,64** — lignes 162, 415.
- envois finis d'une clé, sortie pleine : 4,17 devient **8,10** — ligne 217.
- envois finis des deux clés : 8,34 devient **16,20** — ligne 217.
- avec Mistral, une seule vérification de Google : 27,99 devient **36,51** — ligne 139.
- somme des six plafonds : 16,75 devient **27,75** — ligne 339.
- somme des excès : 14,92 devient **13,45** — ligne 339.
- plafonds et excès ensemble : 31,67 devient **41,20** — ligne 339.

La ligne 7 de l'avenant 1 cite le registre : le chiffre accepté, 84,06, reste ce qu'il est ; il est dépassé au régime courant. **Sous la décision de la mère (GO-2026-11-21-69, R-4682 ; journal, entrée OD-315), le régime prudent vaut pour les lignes de Google, en vérification comme en file : le pire cas chez Google est de 32,97 USD, sous ce chiffre. Les 80,29, 84,98, 89,67, 152,92 et 167,64 USD de ces tableaux et de ces listes sont ceux du régime courant, que la décision écarte.** Les seuils de taux de sa section 3 et de ses lignes 265 et 391 (1,2337 ; 1,0400) reposent sur une recharge comptée : ils sont sans objet depuis que la recharge ne l'est plus (1.5).

### 1.5 Les trois autres parts de la décision, et un écart déjà ouvert

- **Niveau de réflexion le plus haut, gardé.** Aucun écart au devis, qui écrit : « Neon, niveau de réflexion le plus haut (`xhigh`) » (ligne 17). C'est un écart à la recommandation de la confrontation à la règle (`confrontation-regle-google-livraison3-v1.md`, sha256 `b49688eb17e9d1dda94fda5bf1292111c0d12dc4a7a6951abcf077ab12b8be16`, ligne 50) : « (a) si l'interface admet le budget avec Neon » ; « (b) seulement comme repli, en connaissance du doublement des plafonds ». La décision prend (b).
- **Sonde exemptée.** Aucun écart au devis : la sonde garde son corps (ligne 162). C'est un écart à la règle permanente, qui refuse l'envoi si « le plafond de sortie n'atteint pas réflexion plus 16 000 jetons de texte » (section « Appels aux modèles de Google » de `CLAUDE.md`, branche principale, référence locale au commit `f64d95ac9`). L'exemption est écrite en section 6.
- **Âge du taux.** Écart à l'avenant 1 : « `t` est le taux en USD par euro de la pièce de constat, daté d'au plus 24 heures avant elle. » (ligne 259) ; « L'heure du taux est au plus 24 heures avant l'heure de la pièce qui le cite, jamais après. » (ligne 327). Et à la note de la livraison 4 du programme (`note-programme-essais-admission-bras-a-v3.md`, sha256 `fbb30439db64e1a80abfeb937610ba5bc12106490d1936537f1ee33f53bfc7de`, ligne 36) : « borne écrite : l'heure du taux est au plus 24 heures avant l'heure de la pièce, au plus 6 heures après, jamais après l'envoi ». La règle neuve est en section 7.
- **Déjà ouvert, repris ici : la recharge automatique n'est pas comptée.** L'avenant 1 comptait « le solde vu, plus le montant d'une recharge si la page affiche un montant » (ligne 259). La session mère a décidé, sous GO-2026-11-21-69, que chaque projet est borné par son solde seul (journal, entrée OD-301) ; la livraison 4 l'a codé : le champ `recharge_comptee` est « **exigé à `false` en définitive** » (note, ligne 57). Les seuils de la section 3 et le texte des lignes (section 8) le portent.

## 2. Les chiffres refaits

Tout est refait par programme, en nombres décimaux exacts ; la sortie du programme est en section 12. Un coût, une réserve, un excès, un besoin : arrondis vers le haut. À 32 768, le programme redonne les chiffres du devis et de l'avenant 1 (section 12, partie 1).

| grandeur, en USD sauf mention | devis et avenant 1 | **avenant 2** | calcul |
|---|---|---|---|
| sortie maximale envoyée à Google : file du juge, appels A et A′ | 32 768 jetons | **65 536 jetons** | décision |
| sortie maximale de la sonde | 256 jetons | 256 jetons | inchangée |
| réserve d'un envoi de la file, appariement ; couverture | 0,507 ; 0,564 | **0,999 ; 1,056** | 0,015 + 0,98304 ; 0,072 + 0,98304 |
| réserve d'un envoi de vérification, sonde comprise | 0,492 | **0,984** | 0,00048 + 0,98304 |
| pire cas des seize envois de la file, sortie pleine | 8,33 | 16,20 | 2 × (6 × 0,99804 + 2 × 1,05504) = 16,19664 |
| pire cas des trois envois d'une vérification | 1,48 | 2,96 | 3 × 0,98352 = 2,95056 |
| **plafond de la file du juge (ligne 4)** | 8,50 | **16,50** | demi-dollar supérieur du pire cas |
| **plafond d'une vérification de clé (lignes 2 et 6)** | 1,50 | **3,00** | de même |
| excès possible d'un seul envoi, file | 7,58 | **7,09** | 8,07 − 0,98304 = 7,08696 |
| excès possible d'un seul envoi, vérification | 2,18 | **1,69** | 2,67 − 0,98304 = 1,68696 |
| plafond et excès d'une vérification : ce que le compteur borne | 3,68 | **4,69** | 3,00 + 1,69 |
| plafond et excès de la file | 16,08 | **23,59** | 16,50 + 7,09 |
| file, neuf excès, si la supposition de la sonde manque, au régime courant (écarté par la mère, OD-315) | 76,70 | **80,29** | 16,50 + 9 × 7,08696 = 80,28264 |
| **Google, deux vérifications, au régime prudent retenu par la mère (GO-2026-11-21-69, R-4682 ; journal, OD-315) : pire cas** | 23,44 | **32,97** | 2 × 4,69 + 23,59 |
| Google, deux vérifications, au régime courant (écarté par la mère, OD-315), neuf excès, sans borne dure | 84,06 | 89,67 | 2 × 4,69 + 80,29 |
| seuil de crédit avant chaque vérification, par projet | 19,76 | **28,28** | 4,69 + 23,59 |
| seuil de crédit avant la file, par projet | 16,08 | **23,59** | plafond et excès de la file |
| somme des six plafonds ; sans la ligne 5 | 16,75 ; 16,50 | **27,75 ; 27,50** | 5,25 de Mistral + 22,50 de Google |
| somme des excès, un par ligne ; sans la ligne 5 | 14,92 | **13,45 ; 12,28** | 2,98 + 10,47 |
| plafonds et excès ensemble ; sans la ligne 5 | 31,67 | **41,20 ; 39,78** | 27,75 + 13,45 |
| pire cas à la sortie maximale, tous envois (colonne du devis, 6.3) | 14,26 ; 15,74 avec la seconde vérification | 26,57 | 3,99 + 16,20 + 0,23 + 0,23 + 2,96 + 2,96 |
| attendu | ≈ 0,57 | ≈ 0,57 | il ne dépend pas de la sortie maximale |

### 2.1 Réserve d'un envoi

- La réserve est celle du devis (6.4) : l'entrée à un jeton par octet du corps réel, plus la sortie maximale envoyée, aux prix comptés (3 et 15 USD par million). Seule la sortie change : 65 536 jetons valent 0,98304 USD, contre 0,49152.
- **Les trois envois d'une vérification, sonde comprise, sont réservés à 65 536 jetons.** Le devis réservait déjà la sonde à la sortie maximale de la file (ligne 338) : avant elle, rien ne dit que sa borne de 256 tient la réflexion.
- Le corps d'un appel de vérification est pris à 160 octets (S). Le devis ne l'écrit pas : c'est la borne qui redonne sa réserve de 0,492 USD. Le programme calcule sur le corps réel ; le plafond de 3,00 USD laisse passer trois envois tant qu'un corps ne passe pas 5 653 octets (C).

### 2.2 Plafonds

- **Règle appliquée** : le pire cas de tous les envois de la ligne à sortie pleine, porté au demi-dollar supérieur. Elle redonne les deux plafonds de Google du devis (8,50 et 1,50), et les deux estimations de la confrontation (ligne 45 : « d'environ 16,50 au lieu de 8,50 » ; « d'environ 3,00 au lieu de 1,50 »).
- **Pourquoi le plafond d'une vérification monte** : à 1,50, deux envois comptés à leur réserve font 1,97 USD ; le second serait refusé. À 3,00, trois passent (2,96) et un quatrième est refusé.
- **La garantie du devis est gardée** (ligne 370) : un modèle dont chaque envoi est compté au plus à 65 536 jetons de sortie n'est jamais refusé. Les seize envois font 16,20 USD au plus, sous 16,50 ; chaque clé en porte 8,10. Le compteur refuse un envoi de couverture quand le cumul compté passe 15,44 USD. La marge de 0,30336 USD tient tant que les huit corps ne passent pas ensemble 128 560 octets ; les bornes du devis en font 78 000.

### 2.3 Excès possible d'un seul envoi

- Un envoi coupé au délai de son relais a pu rendre, à 200 jetons par seconde, 538 000 jetons à la file (8,07 USD) et 178 000 à une vérification (2,67 USD). **Ces coûts ne changent pas** : ils dépendent du délai, non du plafond.
- L'excès est ce coût, moins la sortie de réserve déjà comptée. La réserve double ; l'excès baisse d'autant : **7,09 USD** à la file, **1,69 USD** à une vérification. À 100 jetons par seconde : 3,06 et 0,36 ; à 400 : 15,16 et 4,36.
- **Les neuf envois coupés seuls coûtent toujours 72,77 USD** (72,94 si trois sont de couverture). La borne de la file monte peu, de 76,70 à **80,29** : 8,00 de plafond en plus, moins neuf fois 0,49152 de réserve en plus, déjà comptée.

### 2.4 Régime prudent du compteur : ce que le plafond neuf change, par calcul

Aucune règle du compteur ne change. Trois de ses effets, que le devis écrivait comme des faits, changent avec les chiffres.

- **Durée sous laquelle un envoi sans compteur lisible est compté à sa réserve** : 328 secondes, au lieu de 164.
- **Vérification de clé.** Un appel coupé à 890 secondes est compté 2,68 USD. Le devis écrivait que cela passait le plafond de la ligne (ligne 134). À 3,00, ce n'est plus vrai. **La ligne s'arrête quand même au premier délai** : avec la réserve de l'envoi suivant, 3,66 USD. Un appel coupé avant 672 secondes laisse partir l'envoi suivant.
- **File partie sur un mot de Lazar.** Un envoi coupé à 45 minutes est compté 8,09 ou 8,15 USD. À 8,50, la réserve de la reprise ne passait jamais, et la file s'arrêtait sans reprise. **À 16,50, la reprise part**, si le cumul compté avant l'envoi coupé ne passe pas 7,30 USD ; un second envoi coupé à 45 minutes arrête la file. Les phrases qui disent qu'un tel envoi arrête la file sans reprise ne valent donc plus telles quelles (devis, lignes 181, 345, 530, 571 et 588 ; avenant 1, ligne 337). La borne « plafond et un excès » tient toujours : 23,59 USD.
- **Fait neuf, que je signale sans rien proposer.** Le devis garde deux régimes parce qu'au régime prudent « la file s'arrêterait sans la reprise que la règle 1 lui donne » (ligne 346) ; l'avenant 1 écarte pour la même raison le régime prudent imposé à la file (ligne 163). À 16,50, cette raison ne vaut plus pour un premier envoi coupé. Imposer le régime prudent à la file ramènerait le pire cas chez Google de 89,67 à 32,97 USD ; son prix serait une file arrêtée au second envoi coupé à 45 minutes, où que ce soit dans la file. C'est un choix de règle, non un chiffre : il n'est pas pris ici. **Il est pris par la mère** : sous GO-2026-11-21-69 (R-4682 ; journal, entrée OD-315), « régime prudent pour les lignes de Google, en vérification comme en file » ; le pire cas chez Google est de 32,97 USD (C, section 12.2).

### 2.5 Ce que ces chiffres supposent

Les trois suppositions du devis demeurent (ligne 384 et suivantes), aucune mesurée : le service ne rend pas plus de 200 jetons par seconde ; la coupure d'un envoi arrête la génération et la facturation ; les compteurs d'un envoi fini disent ce qui est facturé. À 400 jetons par seconde : 46,38 USD au régime prudent, 167,64 au cas des neuf excès (avenant 1 : 36,85 et 162,05). Si la coupure n'arrête pas la facturation, aucun chiffre ne vaut. Une ligne nouvelle de vérification ajoute 4,69 USD au pire cas.

## 3. Seuils de crédit par projet, et manque en euros

### 3.1 La règle, gardée

C'est celle de l'avenant 1 (4.4), telle que la livraison 4 la porte, la recharge non comptée :

`crédit compté(P) = plancher au centime de [ solde vu de P, en euros × t × 0,95 ]`

- **avant chaque vérification de clé de Google** : `crédit compté(P) − dépense retirée ≥ 28,28`, sur **chacun des deux projets** ;
- **avant le premier envoi de la file** : `crédit compté(P) − dépense retirée ≥ 23,59`, sur chacun des deux projets ;
- **dépense retirée** : la somme des dépenses comptées sous les deux clés depuis la pièce de constat, sauf si la pièce porte `oui` à `google_deux_projets_distincts` **et** constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` (livraison 5, C-1). Sous le constat que GO-2026-11-21-68 permet, ces deux clés sont levées, et la somme est toujours retirée. La mère garde la somme (journal, entrée OD-301).

28,28 vaut 4,69 plus 23,59 : comme au devis (ligne 433), le seuil d'avant une vérification couvre aussi la file. Le taux `t` est celui de la pièce de constat ; ici, le taux relevé : 1,0990 USD pour 1 €, soit 1,04405 après la marge de 5 %.

### 3.2 Ce que comptent les deux soldes vus

| projet | solde vu | crédit compté | passe 28,28 | passe 23,59 | couvre le plafond seul de la file, 16,50 |
|---|---|---|---|---|---|
| projet à 11,93 € | 11,93 € | 12,45 USD | non | non | non |
| projet à 15,59 € | 15,59 € | 16,27 USD | non | non | non |
| chacun des deux, après le versement accordé sous GO-2026-11-21-74 (10,47 € et 6,81 €), s'il est fait | 22,40 € | 23,38 USD | non | non | oui |

**En l'état, aucune ligne de Google ne part, pas même une vérification** : c'est ce que donne la règle de l'avenant 1 (4.4, point 3), que la note de la livraison 4 dit portée par le programme — « 19,76 dollars avant une vérification de Google, 16,08 avant la file, par projet » (ligne 51). C'était déjà vrai à ces seuils-là : 19,76 USD demandent 18,93 € par projet. À l'ancien plafond de 8,50, les deux soldes couvraient au moins le plafond de la file ; ils ne le couvrent plus.

### 3.3 Le manque, avant chaque ligne de Google

« Pire » : chaque vérification déjà jouée a pris son plafond et son excès, 4,69 USD. « Attendu » : elle a coûté 0,02 USD (D).

| avant la ligne | seuil | dépense retirée | crédit compté à avoir | solde à voir, par projet | manque au projet à 11,93 € | manque au projet à 15,59 € | manque sur chacun, après le versement de GO-2026-11-21-74 (22,40 €) |
|---|---|---|---|---|---|---|---|
| vérification de la clé 1 (ligne 2), première ligne de Google | 28,28 | 0 | 28,28 USD | **27,09 €** | **15,16 €** | **11,50 €** | **4,69 €** |
| vérification de la clé 2 (ligne 6), la première au pire | 28,28 | 4,69 | 32,97 USD | **31,58 €** | **19,65 €** | **15,99 €** | **9,18 €** |
| la même, la première à son attendu | 28,28 | 0,02 | 28,30 USD | 27,11 € | 15,18 € | 11,52 € | 4,71 € |
| file du juge (ligne 4), les deux vérifications au pire | 23,59 | 9,38 | 32,97 USD | **31,58 €** | **19,65 €** | **15,99 €** | **9,18 €** |
| la même, les deux à leur attendu | 23,59 | 0,04 | 23,63 USD | 22,64 € | 10,71 € | 7,05 € | 0,24 € |

(C. Solde à voir : le crédit compté à avoir, divisé par 1,04405, au centime supérieur ; contrôlé : 31,58 € comptent pour 32,97 USD, 31,57 € pour 32,96. Manque après le versement : le solde à voir moins 22,40 €. Les mêmes seuils, éprouvés par la fonction du chef v7 qui décide si une ligne part : section 12.2.)

**Lecture, pour Lazar.**
- **Pour que les trois lignes passent quoi qu'il arrive** : 31,58 € vus sur chaque projet avant la première ligne. À verser : **19,65 €** et **15,99 €**, soit **35,64 €** en tout.
- **Au plus juste** : 27,11 € par projet. À verser : 15,18 € et 11,52 €, soit 26,70 €. Mais alors la seconde vérification ne part que si la première est comptée 0,02 USD au plus. Une première vérification comptée 1,00 USD demande déjà 28,05 € ; au-delà du solde, il faut verser de nouveau et refaire une pièce de constat.
- **Recommandation** : le premier versement, une fois. Confiance : moyenne. C'est le seul qui ne puisse pas bloquer une ligne en route ; il immobilise 63,16 € sur deux projets pour une dépense attendue chez Google de 0,38 USD. Sans versement, rien ne part : il n'y a pas de défaut.
- **D'où vient ce manque** : de trois règles ensemble — les seuils lus sur chaque projet, la somme des deux dépenses retirée, la recharge non comptée. Les deux dernières sont des choix de la mère sous GO-2026-11-21-69 ; je les garde, comme le mandat le demande.
- **Ce n'est pas une dépense de calcul** : c'est un solde prépayé, qui reste au compte s'il n'est pas consommé. **C'est un paiement, et il reste à Lazar** : la ligne GO-2026-11-21-69 écrit « contact, publication, paiement restent à Lazar ». Un versement fait à la main demande une pièce de constat neuve (avenant 1, 4.4, point 5).
- Le plafond neuf demande 18,24 € de versement de plus que l'ancien (35,64 contre 17,40).
- **Le manque dépend du taux** : il se refait au taux de la pièce de constat. Formule : solde à voir = (seuil + dépense retirée) ÷ (t × 0,95), au centime supérieur.
- **Le versement déjà accordé.** Lazar a accordé sous GO-2026-11-21-74 le versement de 10,47 € et de 6,81 € (17,28 €), chiffré par le journal (OD-301) pour le plafond de 32 768. S'il est fait, chaque projet montre 22,40 €. Il en faut 31,58 : il reste **9,18 € à verser sur chaque projet, 18,36 € en tout**, ce qui demande un mot de paiement de plus. Même à 32 768, 22,40 € ne comptaient que 23,38 USD, sous les 23,44 exigés au pire. Les soldes qui comptent sont ceux de la pièce de constat neuve qui suivra le versement.
- **Rien de plus avant les pièces vérifiées.** Selon le journal (entrée OD-315), « Lazar ne verse rien de plus avant les deux pièces vérifiées » : cette version 2 de l'avenant 2, et le brouillon 2 du devis des lectures hors carte.

### 3.4 Deux écarts avec le journal, à connaître

L'entrée OD-301 du journal chiffre le manque autrement que la règle ne le calcule.
1. **La formule.** Elle multiplie le besoin par 1,05, puis divise par le taux : 23,44 USD donnent 22,40 €. La règle de l'avenant 1, que le programme applique, diminue le taux de 5 % et arrondit le crédit vers le bas : 22,40 € ne comptent que pour 23,38 USD ; il en faut 22,46. L'écart est de six centimes d'euro ; il suffit à faire refuser une ligne.
2. **Le seuil d'une vérification.** Elle écrit qu'une vérification demande 3,68 USD et « passe sur les deux projets ». La règle demande, avant chaque vérification, de quoi couvrir aussi la file : 19,76 USD à l'avenant 1, 28,28 ici. Le besoin propre d'une vérification (4,69 USD, soit 4,50 €) est bien couvert par les deux soldes ; le seuil de la règle ne l'est pas. Si la mère veut le seuil propre, c'est un changement de règle et de code, non un chiffre de cet avenant.

Au bout du compte, les deux lectures demandent la même somme pour aller jusqu'à la file au pire : 32,97 USD par projet.

## 4. La borne de réflexion à déclarer

**La règle** refuse l'envoi si « le plafond de sortie n'atteint pas réflexion plus 16 000 jetons de texte ». Sous un budget de réflexion, l'inégalité se vérifie. Sous un niveau, la réflexion n'a pas de borne écrite : le programme demande alors une « borne de réflexion déclarée à la configuration » (note de la livraison 4, ligne 64), et refuse l'envoi si le plafond n'atteint pas cette borne plus 16 000.

**La valeur à déclarer : 49 536 jetons** (C : 65 536 − 16 000). C'est la plus grande borne que la garde accepte, au jeton près. Le plafond de texte est alors de 16 000 jetons, exactement.

**Pourquoi la plus grande.** Déclarer une borne, c'est affirmer que la réflexion du niveau le plus haut ne la passe pas. Toute valeur plus basse affirme davantage, sans pièce de plus. 49 536 est l'affirmation la plus faible qui satisfasse la règle.

**Elle ne se justifie pas sans relevé.** Aucune pièce que j'ai lue ne borne la réflexion de `gemini-4-neon` au niveau `xhigh`. La confrontation l'écrit de cette option : « non vérifiable : il faut supposer une borne de la réflexion (≤ 49 536), qu'aucune pièce ne donne » (ligne 43). Les sorties mesurées sur ces entrées l'ont été « à des efforts plus bas » : « de 49 à 1 239 jetons, réflexion comprise » (devis, ligne 215). **La borne de 49 536 est donc supposée (S).**

**Ce que disent les pages de Google versées.** La mère a versé sur la branche principale deux pages publiques de Google (`docs/sources/google-gemini-reflexion-v1/`, pièce de provenance `provenance-v1.md`, sha256 `2cc1bdc8d6fc58fc75d9cc530f841ccc84d27b870c77b18e2995767cfbe8aaa9`) : la page « Gemini thinking », variante `generateContent` (`gemini-thinking-generate-content-2026-11-21-v1.md.txt`, sha256 `fe0b8d8820b2ab7b8079bf1477e7871f850f6f5450f92f6b844866cade105892`), et la référence de `generateContent` (`reference-generate-content-2026-11-21-v1.md.txt`, sha256 `829dabb8cb4b90bcbff71c53197ba8d834fc5dfb136294eaa9a1364a1b39a215`), chacune égale à son compagnon, en texte et non en PDF. Elles sont lues par `git show origin/main:<chemin>`, seule ouverture de `docs/sources/` que la mère permet (journal, entrée OD-315). Les quatre choses que la vérification demande d'y lire (sa section 3, point 2) :
1. **un maximum de jetons de pensée par niveau** : aucun. La page de la réflexion dit de `xhigh` : « Most tokens, deepest reasoning » (ligne 689) ; la référence dit de `thinkingLevel` : « Controls the maximum depth of the model's internal reasoning process before it produces a response. » (ligne 2838), sans nombre ;
2. **si `thinkingBudget` est admis avec Neon, et son maximum** : non. « In Gemini 4 models (`gemini-4-carbon`, `gemini-4-argon`, `gemini-4-neon`, and `gemini-4-hydrogen`), `thinkingBudget` (`thinking_budget`) is deprecated. » ; seul, il se ramène au niveau le plus proche, avec un avertissement ; avec `thinkingLevel`, il rend une erreur 400 (page de la réflexion, ligne 939). L'option (a) de la confrontation à la règle, un budget explicite, « la seule vérifiable avant l'envoi » (vérification, section 3), n'est donc pas offerte ;
3. **la limite de sortie du modèle** : « A single request returns up to `65,536` tokens on `gemini-4-neon` and `gemini-4-hydrogen` (streaming and non-streaming) » (ligne 931). Le plafond de la décision est cette limite ;
4. **si `maxOutputTokens` de `generateContent` comprend la pensée** : oui, selon la page, variante `generateContent` : la sortie maximale « sets the maximum number of tokens a response can generate, including thought tokens » (lignes 915 et 916) et agit comme « a hard cutoff enforced by the infrastructure » (ligne 918) ; atteinte pendant la réflexion, la génération finit en `MAX_TOKENS`, la pensée restant facturée (lignes 922 à 924). C'est ce que le devis disait « **non établi pour les deux appels de ce devis.** » (ligne 219) : c'est désormais documenté pour Google, non mesuré.

**La borne de 49 536 ne se fonde donc pas sur ces pages : elle reste supposée (S).** La vérification l'écrit (sa section 3) : « Si la pensée est comprise dans le plafond, 65 536 borne tout envoi, mais rien ne réserve 16 000 jetons au texte. » ; les pages disent que la pensée y est comprise.

**Ce que vaut alors la garde d'avant l'envoi.** Elle vérifie que 49 536 plus 16 000 ne passe pas 65 536. C'est une soustraction, non un fait sur le modèle. Elle refuse encore un corps dont le plafond aurait été baissé, ou une configuration sans borne ; elle n'empêche pas une réflexion plus longue que la borne ; le programme la constate après la réponse (C-2) et arrête la ligne. **Ce qui protège, ce sont les contrôles d'après la réponse** : une réflexion qui mange le texte finit en `MAX_TOKENS`, défaut journalisé, jamais une réponse ; la file s'arrête et ne tient pas (règle 2 du texte). Si les deux sondes disent « comprise », et si la borne se comporte à 65 536 comme à 256, le service tient réflexion et réponse ensemble sous 65 536 ; il ne garantit pas 16 000 jetons au texte.

**Ce qu'il faut relever**, du moins cher au plus cher :
1. **Sans dépense, sur pièce — fait en partie.** Deux des quatre pages que nomme la vérification (sa section 3, point 2) sont versées, en texte et non en PDF : la page de la réflexion et la référence de `generateContent` (ci-dessus) ; `…/docs/whats-new-gemini-4-neon` et `…/docs/models/gemini-4-neon` ne le sont pas. Les quatre choses à y lire ont leur réponse ci-dessus. Deux relevés déjà au dépôt, non opposables (provenance par transcription), sont à citer (vérification, m-2) : `releve-api-mistral-gemini-essais-admission-v1.md` (`291341e2…`), ligne 18 : `maxOutputTokens` « caps combined thinking and output tokens for a response » ; mais « ces phrases visent `max_output_tokens` de l'API Interactions ; pour `generateContent`, confirmation directe non trouvée » ; `juge-des-ancres-identifiant-gemini-v1.md` (`ac8bb15e…`), ligne 15 : quatre niveaux, `xhigh` le plus haut, aucune borne en jetons.
2. **Sans dépense, par programme** : `outputTokenLimit`, rendu par l'appel de liste avant tout appel payant (devis, 4.4, ligne 2). Sous 65 536 : rien ne part, et la décision est à reprendre.
3. **Sans appel de plus, sur les appels déjà prévus** : `thoughtsTokenCount` de chaque envoi à Google, que le relevé et le rapport portent déjà (devis, 5.5). Le plus grand compte de pensée et « borne de réflexion déclarée dépassée, oui ou non » : déjà au programme (livraison 5, C-2 : `borne_de_reflexion_dementie` à la fiche, `bornes_de_reflexion_dementies` au relevé) ; rien à changer. Et l'issue des deux sondes.

**Ce que le relevé permettrait.** Un maximum documenté d'au plus 49 536 jetons : il devient la borne déclarée, et elle est justifiée. Un maximum plus grand, ou aucun : la borne reste supposée ; la justifier demanderait un plafond plus haut ou un budget explicite, et c'est une autre décision. Les pages versées n'en donnent aucun, et la page de la réflexion déprécie le budget chez Neon (ligne 939) : la borne reste supposée.

**Si un envoi dépasse la borne** — plus de 49 536 jetons de pensée facturés —, le programme de la livraison 5 en fait un défaut (C-2, `borne_dementie`). Dans la file : défaut journalisé, l'envoi n'est ni jugé ni compté parmi les réponses, la file s'arrête et ne tient pas. À une vérification : ligne 13 du classement, non saine, nœud de Lazar. À la sonde : une mesure. La borne est donc une déclaration éprouvée après chaque réponse. Son prix est qu'un juge qui réfléchit plus longtemps échoue pour un chiffre de configuration : c'est pourquoi elle est déclarée à la plus haute valeur admise.

**Conséquence pour la limite de mots.** Le contrôle « `consignes.<nom>.limite_de_mots` × `fournisseurs.google.jetons_par_mot` ≤ plafond − réflexion » (note, ligne 65) se lit sur 16 000 jetons : il passe pour 8 000 mots à 2 jetons par mot, 5 333 à 3, 4 000 à 4 (C). Je n'ai pas lu les consignes : la limite et le rapport sont à inscrire par un lecteur habilité. Si une limite ne tient pas, rien ne part ; la borne devrait alors descendre, ce qui affirme davantage.

## 5. Débit requis et délais

**Ce que la décision ne touche pas** : les délais par envoi (file : 2 700 secondes, relais à 2 690 ; vérification : 900 secondes, relais à 890), la reprise unique, l'attente sur un code 429, le délai global (48 680 secondes pour la file, 3 300 par lancement de vérification).

**Le débit requis double.** Une réponse de 65 536 jetons tient dans 2 690 secondes si le service rend **24,4 jetons par seconde ou plus** (C : 65 536 ÷ 2 690 = 24,3628). Le devis écrivait 12,2 pour 32 768 (ligne 263). Aucun des deux débits n'est mesuré (S).

**Les délais tiennent-ils ?** Oui en secondes : rien n'est à relever pour que la décision s'applique. Ils ne tiennent une lecture à sortie pleine que si le service rend 24,4 jetons par seconde. En dessous, voici ce qui se passe, selon le débit `r` du service :

| débit du service | lecture de 32 768 jetons au plus | lecture de 32 768 à 65 536 jetons |
|---|---|---|
| 24,4 jetons par seconde ou plus | finit dans le délai, comme avant | finit dans le délai ; à 32 768, elle finissait par sortie maximale atteinte, et la file ne tenait pas |
| de 12,2 à 24,4 | finit dans le délai, comme avant | finit si elle fait moins de 2 690 × `r` jetons ; sinon coupée à 45 minutes, reprise, puis file arrêtée ; à 32 768, elle ne tenait pas non plus |
| moins de 12,2 | finit si elle fait moins de 2 690 × `r` jetons ; sinon coupée : comme avant | coupée à 45 minutes : comme avant |

**Donc : le plafond neuf ne fait échouer aucune lecture qui tenait à 32 768.** Il en sauve : celles qui font de 32 768 à 65 536 jetons et finissent dans le délai. Au-delà de 65 536 jetons, rien ne change de nature : fin par sortie maximale atteinte, ou coupure au délai si le service est plus lent. Cela suppose que la réflexion du modèle ne dépend pas du plafond envoyé (S) : si le niveau le plus haut réfléchit plus longtemps quand on lui laisse plus de place, une lecture peut durer plus qu'avant.

**Ce qui change.**
1. **La phrase de la ligne 4** : « la sortie maximale de 65 536 ne tient dans le délai de 45 minutes que si le service rend 24,4 jetons par seconde ou plus, débit non mesuré ». La ligne 3, de Mistral, garde la sienne.
2. **La façon dont une lecture trop longue échoue.** À 32 768, elle finissait par sortie maximale atteinte, après 32 768 jetons facturés au plus si la borne tient la réflexion. À 65 536, sous 24,4 jetons par seconde, elle peut courir jusqu'au délai : envoi coupé, reprise, second envoi coupé, file arrêtée. Soit 90 minutes, deux envois comptés au régime prudent que la mère a retenu (journal, entrée OD-315), 8,09 ou 8,15 USD chacun, si le compteur laisse partir la reprise (2.4), et la lecture de la console par Lazar avant toute autre ligne de Google (garde 20).
3. **La durée d'une lecture pleine** : 2 685,9 secondes à 24,4 jetons par seconde, 1 310,7 à 50. La durée attendue d'une file n'est pas mesurée ; le devis la suppose de moins d'une heure.

**Relever le délai pour garder 12,2 jetons par seconde ? Je ne le propose pas.** Il faudrait 5 400 secondes par envoi (relais à 5 390). L'excès d'un envoi de la file passerait de 7,09 à 15,19 USD ; la borne de la file, de 23,59 à 31,69 ; le pire cas chez Google, au régime prudent que la mère a retenu (OD-315), de 32,97 à 41,07 (au régime courant, de 89,67 à 162,57) ; le délai global, de 48 680 à 91 880 secondes (25 h 31 min). Et une connexion muette de 90 minutes risque plus d'être coupée en route qu'une de 45 (devis, 13, point 6). La décision ne le demande pas.

**Appels de vérification** : 900 secondes, inchangés. Un appel A à sortie pleine ne tiendrait en 890 secondes qu'à 73,7 jetons par seconde ; le devis ne l'exige pas : « sa réponse est courte » (ligne 101).

## 6. L'exemption de la sonde, écrite exactement

> **Exemption de la sonde de borne.** L'appel B de chaque vérification de clé de Google (devis, 4.6) est exempté d'un seul contrôle de la règle permanente « Appels aux modèles de Google » : celui qui refuse l'envoi quand le plafond de sortie n'atteint pas la réflexion plus 16 000 jetons de texte. Sa sortie maximale reste de 256 jetons : mesurer si la réflexion compte dans cette borne est son objet.
>
> 1. **La sonde garde un réglage de réflexion explicite.** Son corps porte `generationConfig.thinkingConfig.thinkingLevel`, au niveau le plus haut, à l'orthographe de l'appel sain. Le contrôle d'avant l'envoi et le relais refusent une sonde sans ce champ, comme tout autre envoi à Google.
> 2. **La sonde ne produit aucune lecture jugée.** Son texte n'est ni extrait pour être jugé, ni compté parmi les réponses, ni rapporté. Elle rend une seule issue, par programme, sur les compteurs, le motif de fin et la réflexion constatée : « comprise », « non comprise » ou « indécidée ». Aucune règle d'admission ne la lit.
> 3. **Le corps exempté est le corps exact de la sonde** : celui de l'appel sain, sauf deux champs, la sortie maximale à 256 et le message fixe du devis. Tout autre corps sous le plafond exigé est refusé : un envoi de la file, un appel A ou A′, une sonde à un autre plafond ou à un autre message.
> 4. **Après la réponse, les constats de la règle valent mesure, jamais réponse.** Ils se lisent sur le tableau des issues du devis (4.6), inchangé : fin en `MAX_TOKENS` avec réflexion constatée et au plus 256 jetons facturés, « comprise » ; plus de 256 jetons facturés, « non comprise » ; à 256 jetons facturés au plus, zéro jeton de pensée, `SAFETY`, `RECITATION` ou texte vide, « indécidée », motif au relevé.
> 5. **Marques.** À la configuration : `exemption_de_la_sonde` à vrai, et `exemption_de_la_sonde_go`. Au relais des seules vérifications : `--plafond-exempte`. Sans elles, la sonde n'est pas envoyée, et la file du juge ne part pas.
> 6. **Portée.** Les vérifications de clé de Google de ce devis : les lignes 2 et 6, et toute ligne nouvelle de vérification de Google accordée sur ce devis. Aucun autre script, aucun autre modèle, aucune autre course.

**D'où viennent les deux conditions.** Le devis les portait déjà : « Même réglage de raisonnement, même mode de lecture, même traitement de la température que l'appel sain. » (ligne 162) ; « Le texte des réponses de code 200 n'est ni lu ni rapporté. » (ligne 95) ; l'issue se lit « par programme, sur la sortie facturée de 5.5, le motif de fin et la réflexion constatée » (ligne 163). L'exemption ne leur ajoute rien : elle s'y adosse.

**Un point que la décision ne nomme pas : le contrôle de la limite de mots.** La règle refuse aussi l'envoi si « la limite de mots de l'invite ne tient pas dans le plafond de texte ». Ce plafond de texte est le plafond de sortie moins la borne de réflexion : sous 256, il est négatif. C'est la même inégalité, vue du côté du texte ; je lis donc l'exemption comme la couvrant, pour la sonde seule, dont le message demande un produit et non un texte borné en mots. La décision ne le dit pas, et la note de la livraison 4 ne dit pas ce que le programme fait de ce contrôle à la sonde : à confirmer par la mère, et à vérifier par le contre-lecteur du code.

**Qui l'accorde.** La confrontation écrivait : « Il faut une **exemption nommée de la règle**, accordée par Lazar : c'est un écart à une règle permanente, donc un nœud. » (ligne 77). Mon mandat la donne pour accordée par la mère, sous GO-2026-11-21-69. La valeur de `exemption_de_la_sonde_go` est donc `GO-2026-11-21-69` ; la ligne de ce GO ne nomme pas l'exemption (section 10, point 3).

## 7. Âge du taux de change : la règle neuve

**Le fait.** Le relevé versé est le fichier quotidien des taux de référence de l'euro de la Banque centrale européenne, pris le 2026-11-21 à 17:49:40Z selon le journal (entrée OD-301) : `docs/notes/relance-organismes-discrets-v1/taux-de-change-v1/bce-eurofxref-daily-releve-2026-11-21T1749Z.xml`, sha256 `a234540a78d0bccccc3642bfe604b138310a03741361434907aa4cf3e7622e8a`, égale à son compagnon. Il porte le fixage du **2026-11-20** : **1,0990 USD pour 1 €**. Il ne porte que le jour du fixage, non son heure. Le 21 novembre est un samedi : aucun fixage neuf avant le lundi 23. Selon le journal, la règle « 24 heures au plus » refuse déjà ce relevé.

**La décision** : le dernier fixage publié est admis quand aucun plus récent n'existe.

**Forme proposée, que le programme vérifie sans réseau.** Le fichier quotidien de la banque porte toujours son dernier fixage publié : le relevé lui-même établit qu'aucun plus récent n'existait à l'heure où il a été pris. D'où quatre contrôles :
1. la ligne de taux de la pièce de constat porte le taux, la source, **le jour du fixage**, **l'heure du relevé** en temps universel, et l'empreinte du fichier relevé ;
2. le programme relit le fichier : même empreinte ; le jour et le taux du dollar qu'il porte sont ceux de la ligne ;
3. **la borne d'âge se lit sur l'heure du relevé, non sur le jour du fixage** : relevé au plus 24 heures avant l'heure de la pièce qui le cite, au plus 6 heures après, jamais après l'envoi — les bornes de la livraison 4, inchangées ;
4. le jour du fixage est au plus cinq jours avant le jour du relevé, jamais après lui.

Le chef v4 ne lit que « - taux : T USD par EUR ; source : … ; heure du taux (UTC) : … » (`MOTIF_TAUX`). Sans code neuf, la pièce de constat écrit : « - taux : 1.0990 USD par EUR ; source : Banque centrale européenne, fixage du 2026-11-20, fichier a234540a78d0bccccc3642bfe604b138310a03741361434907aa4cf3e7622e8a ; heure du taux (UTC) : 2026-11-21T17:49Z ». L'heure du taux y est l'heure du relevé, que bornent les contrôles de la livraison 5 (m-5). Les contrôles 2 et 4 sont alors faits par le vérificateur de la pièce, non par le programme ; les coder est une livraison de plus.

**Ce que cette forme suppose (S)** : cinq jours est la plus longue fermeture que je connaisse au calendrier de la banque, celle de Pâques, du jeudi au mardi ; aucune pièce ne l'établit ici. Le contrôle 4 ne sert qu'à refuser un fichier périmé. **La règle des cinq jours est à relever avec la page de ce calendrier, ou à retirer si le contrôle n'est pas codé** (vérification, m-3).

**Sa limite.** Entre le relevé et la pièce, un fixage neuf a pu paraître, un jour ouvré, dans l'après-midi. La forme proposée admet alors l'ancien pendant 24 heures au plus ; la marge de 5 % est là pour cet écart. Si la mère veut la lettre stricte de la décision, le relevé se refait après la publication du jour : c'est une ligne de plus au contrôle 3, que le vérificateur peut exiger.

**Application.** L'heure d'une pièce de constat est, pour le programme, « la plus tardive des heures des valeurs vues » (note de la livraison 4, ligne 89). Les deux captures des soldes sont de « 2026-11-21T16:24:17Z » (avenant 1, ligne 8) ; le relevé est de 17:49:40Z, soit moins de 6 heures après : il est admis pour elles. Pour des valeurs vues plus tard — après un versement, par exemple —, il vaut jusqu'au 22 novembre à 17:49:40Z. Au-delà, un relevé neuf est dû ; il portera le même fixage jusqu'à la publication du lundi 23. Le manque de la section 3 se refait alors au taux neuf.

## 8. Texte neuf des lignes de calcul touchées, à citer tel quel

Les lignes 1, 3 et 5 (Mistral) ne changent pas. Les lignes 2, 6 et 4 remplacent celles de l'avenant 1 (sa section 6, lignes 333, 335 et 337 du fichier). Le texte à citer commence après le nom de la ligne. Aucun crochet n'y reste ouvert : l'avenant 1 en laissait un pour la valeur d'une recharge, qui n'est plus comptée. Chaque texte est entier, cite les empreintes du devis, de sa vérification et de l'avenant 1, version 3, et porte les marques de sa ligne au gabarit (`marques_du_perimetre`) : placé tel quel au périmètre de sa ligne du registre, il passe la garde 8 du chef v7 (forme ci-dessous ; épreuve par programme, section 12.2).

**Ligne 2. Vérification de la clé 1 de Google** : bras A, vérification de la clé de `gemini-4-neon` lue sous `GEMINI_API_KEY`, trois appels au plus, soit trois envois au plus, sonde de borne et seconde orthographe du niveau de réflexion comprises, délai de 900 secondes par appel ; devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc, vérification du devis 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca, avenant 1 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac ; sortie maximale envoyée de 65 536 jetons aux appels A et A′, au niveau de réflexion le plus haut, sous une borne de réflexion déclarée de 49 536 jetons, supposée et non relevée, éprouvée après chaque réponse : une réflexion facturée au-delà est un défaut, qui arrête la file sans qu'elle tienne, et rend une vérification non saine (nœud de Lazar) ; sonde de borne à 256 jetons, exemptée du contrôle d'avant l'envoi « plafond de sortie au moins égal à la réflexion plus 16 000 jetons de texte », dans les termes de la section 6 de l'avenant 2, à réglage de réflexion explicite et sans lecture jugée (décision de la session mère sous GO-2026-11-21-69, en application de la règle de GO-2026-11-21-71) ; plafond 3,00 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 1,69 USD au débit déclaré de 200 jetons par seconde, tout envoi sans compteur lisible étant compté à ce débit sur sa durée, ce qui arrête la ligne au premier délai, sous la supposition, non documentée, que la coupure arrête la génération et la facturation, compté à 3 et 15 USD par million, payé sur le crédit prépayé du projet de cette clé, dont la recharge automatique reste activée et qui n'a aucun plafond de dépense, par décision de Lazar (GO-2026-11-21-68) : le solde ne borne pas la perte ; elle n'est bornée que par le compteur, à 4,69 USD sous les suppositions dites, et par rien de dur au-delà ; conditions d'envoi : offre payante vue sur capture ; partage et durée des journaux, et lien entre la clé et son projet, non constatés, levés par le même GO ; avant la ligne, le solde vu de chacun des deux projets, en euros, converti au dernier fixage publié de la Banque centrale européenne diminué de 5 %, sans compter la recharge automatique (GO-2026-11-21-69), moins la dépense retirée de la section 3.1 de l'avenant 2 — la somme des dépenses comptées sous les deux clés depuis la pièce de constat, sauf si la pièce porte `oui` à `google_deux_projets_distincts` et constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` —, atteint 28,28 USD ; une ligne nouvelle de vérification, sur l'une ou l'autre clé, ajoute 4,69 USD au pire cas et exige de nouveau 28,28 USD, lus de même.

**Ligne 6. Vérification de la clé 2 de Google** : bras A, vérification de la clé de `gemini-4-neon` lue sous `GEMINI_API_KEY_2`, trois appels au plus, soit trois envois au plus, sonde de borne et seconde orthographe du niveau de réflexion comprises, délai de 900 secondes par appel ; devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc, vérification du devis 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca, avenant 1 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac ; sortie maximale envoyée de 65 536 jetons aux appels A et A′, au niveau de réflexion le plus haut, sous une borne de réflexion déclarée de 49 536 jetons, supposée et non relevée, éprouvée après chaque réponse : une réflexion facturée au-delà est un défaut, qui arrête la file sans qu'elle tienne, et rend une vérification non saine (nœud de Lazar) ; sonde de borne à 256 jetons, exemptée du contrôle d'avant l'envoi « plafond de sortie au moins égal à la réflexion plus 16 000 jetons de texte », dans les termes de la section 6 de l'avenant 2, à réglage de réflexion explicite et sans lecture jugée (décision de la session mère sous GO-2026-11-21-69, en application de la règle de GO-2026-11-21-71) ; plafond 3,00 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 1,69 USD au débit déclaré de 200 jetons par seconde, tout envoi sans compteur lisible étant compté à ce débit sur sa durée, ce qui arrête la ligne au premier délai, sous la supposition, non documentée, que la coupure arrête la génération et la facturation, compté à 3 et 15 USD par million, payé sur le crédit prépayé du projet de cette clé, dont la recharge automatique reste activée et qui n'a aucun plafond de dépense, par décision de Lazar (GO-2026-11-21-68) : le solde ne borne pas la perte ; elle n'est bornée que par le compteur, à 4,69 USD sous les suppositions dites, et par rien de dur au-delà ; conditions d'envoi : offre payante vue sur capture ; partage et durée des journaux, et lien entre la clé et son projet, non constatés, levés par le même GO ; avant la ligne, le solde vu de chacun des deux projets, en euros, converti au dernier fixage publié de la Banque centrale européenne diminué de 5 %, sans compter la recharge automatique (GO-2026-11-21-69), moins la dépense retirée de la section 3.1 de l'avenant 2 — la somme des dépenses comptées sous les deux clés depuis la pièce de constat, sauf si la pièce porte `oui` à `google_deux_projets_distincts` et constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` —, atteint 28,28 USD ; une ligne nouvelle de vérification, sur l'une ou l'autre clé, ajoute 4,69 USD au pire cas et exige de nouveau 28,28 USD, lus de même.

**Ligne 4. File Neon** : bras A, essai d'admission du juge des deux ancres, 8 appels, 16 envois au plus, partagés entre les deux clés par une règle fixe : rangs impairs sous `GEMINI_API_KEY`, rangs pairs sous `GEMINI_API_KEY_2`, la reprise sur la clé de son appel ; une seule file, un seul compteur ; devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc, vérification du devis 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca, avenant 1 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac ; sortie maximale envoyée de 65 536 jetons, au niveau de réflexion le plus haut, sous une borne de réflexion déclarée de 49 536 jetons, supposée et non relevée, éprouvée après chaque réponse : une réflexion facturée au-delà est un défaut, qui arrête la file sans qu'elle tienne, et rend une vérification non saine (nœud de Lazar) (décision de la session mère sous GO-2026-11-21-69, en application de la règle de GO-2026-11-21-71) ; plafond 16,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 7,09 USD au débit déclaré de 200 jetons par seconde : au régime prudent, où un envoi coupé à 45 minutes est compté 8,09 ou 8,15 USD, où sa reprise part si le cumul compté avant lui vaut au plus 7,30 USD (7,41 pour un envoi d'appariement), et où un second envoi coupé à 45 minutes arrête la file ; la recharge automatique restant activée et aucun plafond de dépense n'étant réglé, par décision de Lazar (GO-2026-11-21-68) : la file est comptée au régime prudent, quelle que soit l'issue des sondes (décision de la session mère sous GO-2026-11-21-69, R-4682) ; pire cas chez Google, pour les lignes 2, 4 et 6 telles qu'accordées, 32,97 USD, sous le chiffre accepté (GO-2026-11-21-68) ; le tout sous la supposition, non documentée, que la coupure arrête la génération et la facturation ; compté à 3 et 15 USD par million, payé sur le crédit prépayé des deux projets ; elle ne part qu'après les deux vérifications saines, au même nom servi et aux mêmes orthographes ; « huit sur huit » se lit sur les huit lectures ensemble, quatre par clé ; la sortie maximale de 65 536 ne tient dans le délai de 45 minutes que si le service rend 24,4 jetons par seconde ou plus, débit non mesuré ; conditions d'envoi : comme à la ligne 2 ; au départ de la file, le solde vu de chacun des deux projets, converti de même, sans compter la recharge automatique, moins la dépense retirée de la section 3.1 de l'avenant 2, lue comme à la ligne 2, atteint 23,59 USD.

**Lignes du registre, à la forme que lit la garde 8** (note de la livraison 7, `note-programme-essais-admission-bras-a-v6.md`, sha256 `5a6a41f5e3d0c5183e542a87c70b90a7cef853dfd44f1f7561f988dffbcc9aa8`, section 6 (c)) : huit cellules séparées par « ` | ` » ; le périmètre est le texte de la ligne, tel quel ; le plafond, à la lettre de `plafond_registre` ; `type` « calcul », `par` « Lazar ».

```
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | <texte de la ligne 2, tel quel> | 3,00 USD | AAAA-MM-JJ | Lazar | <référence> |
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | <texte de la ligne 6, tel quel> | 3,00 USD | AAAA-MM-JJ | Lazar | <référence> |
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | <texte de la ligne 4, tel quel> | 16,50 USD | AAAA-MM-JJ | Lazar | <référence> |
```

**Sommes des six lignes** (C) : plafonds, **27,75 USD** (27,50 sans la ligne 5) ; excès possibles, un par ligne, **13,45 USD** ; ensemble, **41,20 USD**. Attendu : ≈ 0,57 USD, inchangé.

**Chaque ligne ajoute**, comme au devis et à l'avenant 1 : la lecture de la console par Lazar après tout envoi coupé, avant toute autre ligne chez ce fournisseur — chez Google, sur les deux projets — ; et les empreintes du devis accepté, de l'avenant 1 accepté, **de cet avenant 2 accepté**, de la pièce de constat, du relevé du taux, du fichier des règles (lignes 3 et 4), des pages de prix, des relevés documentaires, de la pièce « goreco ». **La ligne 3 garde sa phrase** : la sortie maximale de 32 768 ne tient dans les délais que si le service rend 12,2 jetons par seconde ou plus, débit non mesuré. Les lignes 3 et 4 disent toujours : deux envois par appel.

**Avec les lignes, le geste de paiement**, à la place de celui de l'avenant 1 (sa ligne 343) : 9,50 USD de crédit utilisable chez Mistral, inchangé ; chez Google, les soldes vus des deux projets, sans compter la recharge automatique, doivent couvrir sur chaque projet 28,28 USD avant chaque vérification et 23,59 USD avant la file, dépense déjà comptée retirée : au pire 32,97 USD, soit 31,58 € au taux relevé. Chaque projet doit montrer au moins 31,58 € à la pièce de constat. Aux soldes du 21 novembre (11,93 € et 15,59 €), il manque 19,65 € et 15,99 € ; après le versement accordé sous GO-2026-11-21-74 (10,47 € et 6,81 €), il manque 9,18 € sur chacun. Verser est un geste de Lazar ; un versement demande une pièce de constat neuve. La recharge automatique reste activée : chaque recharge est un paiement sans geste de Lazar, d'un montant qui n'est pas relevé, et qui ne compte pour aucun seuil.

## 9. Valeurs de configuration définitive, champ par champ

Les noms des champs sont ceux de la note de la livraison 4 (sections 5 et 8). Je n'ai ouvert ni le gabarit de configuration ni le programme : la place exacte de chaque champ dans le fichier est la leur. La note donne `fournisseurs.google` pour parent de `jetons_par_mot` ; je suppose le même parent aux autres champs de Google.

| champ | valeur définitive | fondement | état |
|---|---|---|---|
| `sortie_max` de Google : file du juge, appels A et A′ des deux vérifications | `65536` | décision de la mère, GO-2026-11-21-69 | décidé |
| sortie maximale de la sonde | `256` | devis, 4.6 | inchangé |
| `reflexion` : forme | « niveau » | niveau le plus haut gardé | décidé |
| `reflexion` : orthographes du niveau | `XHIGH`, puis `xhigh` | devis, 4.4, ligne 11 | inchangé |
| `reflexion` : borne déclarée | `49536` | section 4 | **supposée, non relevée** |
| `marge_de_texte_jetons` | `16000` | règle permanente | déjà au gabarit, selon la note |
| `exemption_de_la_sonde` | `true` | section 6 | décidé |
| `exemption_de_la_sonde_go` | `GO-2026-11-21-69` | mandat | voir section 10, point 3 |
| `fournisseurs.google.jetons_par_mot` | non donné ici | consignes non lues | à inscrire par un lecteur habilité |
| `consignes.<nom>.limite_de_mots` | non donné ici ; un mot pour l'appel « OK », selon la note | consignes non lues | à inscrire par un lecteur habilité ; contrainte : limite × rapport ≤ 16 000 |
| `marge_de_change` ; `marge_de_change_go` | `0.05` ; `GO-2026-11-21-68` | avenant 1 | inchangé |
| `recharge_comptee` | `false` | mère, GO-2026-11-21-69 ; journal, OD-301 | inchangé depuis la livraison 4 |
| `regime_file_google` | `"prudent"` | mère, GO-2026-11-21-69 (R-4682) ; journal, OD-315 | décidé ; une configuration définitive l'exige (chef v7) |
| `google_deux_projets_distincts`, à la pièce de constat | `non relevé` : la somme des deux dépenses est retirée, sauf si la pièce porte `oui` à `google_deux_projets_distincts` **et** constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` (livraison 5, C-1) ; sous le constat que GO-2026-11-21-68 permet, ces deux clés sont levées, et la somme est toujours retirée | mandat ; avenant 1, 4.4, point 4 | inchangé |
| ligne de taux de la pièce de constat | 1,0990 USD pour 1 € ; Banque centrale européenne ; fixage du 2026-11-20 ; relevé le 2026-11-21 à 17:49:40Z ; fichier `a234540a…` | section 7 | forme neuve : jour du fixage et heure du relevé |
| identifiants des six lignes de calcul | à inscrire quand elles sont accordées | — | en attente |
| empreintes citées par les lignes | devis ; sa vérification ; avenant 1 ; cet avenant, une fois accepté | note, section 8 | à compléter |

**Champs du gabarit, par la vérification de la version 1 (correction 5).**

| champ | valeur définitive | état |
|---|---|---|
| `fournisseurs.google.sortie_max` | `65536` | décidé |
| `fournisseurs.google.reflexion` | `{"forme": "niveau", "borne_declaree": 49536}` | borne supposée, éprouvée par C-2 |
| `fournisseurs.google.exemption_de_la_sonde` ; `_go` | `true` ; `"GO-2026-11-21-69"` (forme seule contrôlée) | décidé ; à consigner (section 10, point 3) |
| `fournisseurs.google.credit_min_avant_verification_usd` ; `credit_min_avant_file_usd` | `28.28` ; `23.59` | à changer (gabarit : 19.76 et 16.08) |
| `fournisseurs.google.credit_a_avoir_usd` | `32.97`, pour ne pas dire faux | non lu par le chef v4 ; gabarit : 23.0, valeur du schéma de recharge retiré |
| `lignes.verification-google-cle-1` et `-cle-2` : `plafond_usd` ; `plafond_registre` ; `exces_possible_d_un_envoi_usd` | `3.0` ; `"3,00 USD"` ; `1.69` | à changer (1.5 ; « 1,50 USD » ; 2.18) |
| `lignes.file-neon` : `plafond_usd` ; `plafond_registre` ; `exces_possible_d_un_envoi_usd` | `16.5` ; `"16,50 USD"` ; `7.09` | à changer (8.5 ; « 8,50 USD » ; 7.58) |
| `lignes.<ligne de Google>.reserve_sortie_jetons` | `null` ou `65536` (le chef la déduit de `sortie_max`) | rien à inscrire |
| `lignes.file-neon.delais` | inchangé (2 700 et 2 690) | décision 1 tranchée par le levier (a), régime prudent (journal, OD-315) : le levier (d) n'est pas pris |
| arguments `--borne-reflexion` et `--plafond-exempte` | passés par le chef (lignes 3025 à 3027), non à la main | rien à passer |
| `avenant` | la garde 8 n'en lit qu'un : code neuf, un second champ pour l'avenant 2, vérifié sur disque et cité par la ligne du registre | **à coder** |

**Ce que le programme doit changer.** Rien n'est écrit ni essayé ici ; chaque garde changée garde un cas sain et un artefact (R5).
1. **Garde 8** : les plafonds à la lettre des trois lignes de Google, `3,00 USD`, `3,00 USD` et `16,50 USD` ; le périmètre ou la référence cite aussi cet avenant.
2. **Seuils de crédit** (`fournisseurs.google.credit_min_avant_verification_usd` et `fournisseurs.google.credit_min_avant_file_usd`) : 28,28 et 23,59 USD, en décimal exact. Essai chiffré de l'avenant 1 (section 7, point 7), valeurs neuves : cas sain, deux projets distincts, dépenses de 4,69 et 0,02, crédit compté de 28,28, la file part (28,28 − 4,69 = 23,59) ; artefact, somme retirée, la file ne part pas (28,28 − 4,71 = 23,57).
3. **Garde 3** : la sortie maximale par fournisseur. À Google, 65 536 à la file et aux appels A et A′, 256 à la sonde ; un corps de Google à 32 768 devient un artefact. Chez Mistral, 32 768 reste la valeur saine et 65 536 un artefact.
4. **Classement de la vérification, ligne 2** : `outputTokenLimit` sous 65 536, aucun appel payant ; artefact neuf : `outputTokenLimit` à 32 768.
5. **Réserve et régime courant** : un envoi de Google est réservé, et un envoi coupé compté, à 65 536 jetons de sortie.
6. **Garde 1, essais à refaire chez Google** : vérification, premier envoi sans réponse jusqu'au délai, compté 2,68 USD sous le plafond, deuxième envoi refusé ; file partie sur un mot de Lazar, envoi coupé à son délai total, la reprise part ; second envoi coupé, la file s'arrête à son plafond.
7. **Âge du taux** : les quatre contrôles de la section 7. Cas sain : fixage du vendredi, relevé du samedi, pièce du samedi. Artefacts : relevé de plus de 24 heures avant la pièce ; fixage de plus de cinq jours avant le relevé ; fixage daté d'après le relevé ; taux de la ligne autre que celui du fichier ; empreinte autre.
8. **Relevés et rapport** : déjà au programme (livraison 5, C-2 : `borne_de_reflexion_dementie` à la fiche, `bornes_de_reflexion_dementies` au relevé) ; rien à changer.
9. **Limite de mots à la sonde** : déjà tranchée par le programme ; l'exemption couvre les contrôles (2) et (3) pour le corps exact de la sonde (chef v4, lignes 1486 à 1497).

## 10. À dire à Lazar, et réserves

**À dire à Lazar.**
1. **Le pire cas chez Google passe de 84,06 à 89,67 USD**, au régime courant, sans borne dure. Il a accepté 84,06 (GO-2026-11-21-68). Au grain des lignes, l'écart est de 5,61 USD (5,60 en valeurs exactes). C'est un nœud : décision, enjeu, options et leviers chiffrés à la vérification de cet avenant (`verification-avenant-2-devis-essais-admission-v1.md`, section 2 et décision 1). Les deux chiffres supposent 200 jetons par seconde au plus et une coupure qui arrête la facturation. **Tranché** : la mère, sous GO-2026-11-21-69 (R-4682 ; journal, entrée OD-315), a retenu le levier (a) de la vérification (option (B) de sa décision 1) : « régime prudent pour les lignes de Google, en vérification comme en file » ; pire cas chez Google, 32,97 USD, sous les 84,06 acceptés, sous les mêmes suppositions.
2. **Le versement** de la section 3 : 19,65 € et 15,99 €, ou, au plus juste, 15,18 € et 11,52 €. Sans lui, aucune ligne de Google ne part. Après le versement accordé sous GO-2026-11-21-74 (10,47 € et 6,81 €), il manque 9,18 € sur chacun.
3. **Qui a décidé.** Le mot « goreco » fixait 32 768 ; c'est un mot de Lazar. La confrontation à la règle recommandait de le garder, avec un budget de réflexion explicite, et rangeait les trois options, comme l'exemption de la sonde, parmi les nœuds de Lazar (lignes 50 et 77). La mère a retenu le plafond relevé, qui garde le niveau le plus haut que Lazar avait décidé. Elle l'a fait sous GO-2026-11-21-69, dont la ligne donne douze heures d'autonomie et accorde les recommandations en attente et les dépenses sur devis, sans nommer ni le plafond, ni l'exemption, ni le taux. Je rapporte la décision telle que mon mandat la donne ; je ne la juge pas. **Je propose qu'elle soit consignée** par une ligne ou une pièce qui nomme ses quatre parts, pour que la configuration cite un texte qui dit ce qu'il autorise.

**Réserves.**
4. **La borne de réflexion est supposée** (section 4). Les pages de Google versées ne donnent aucun maximum de pensée par niveau : rien ne la justifie.
5. **`outputTokenLimit` n'est pas connu.** S'il est sous 65 536, rien ne part chez Google et la décision est à reprendre ; c'est le premier constat, gratuit.
6. **Le débit de 24,4 jetons par seconde n'est pas mesuré** (section 5), et l'effet du plafond sur la longueur de la réflexion non plus.
7. **Les limites de mots ne sont pas lues** : le contrôle de la limite de mots dépend de deux valeurs que seul un lecteur habilité peut inscrire.
8. **La forme de la règle du taux est la mienne** (section 7) : la décision tient en une phrase ; les quatre contrôles et la borne de cinq jours sont une proposition.
9. **Les seuils sont plus durs que le journal ne les lit** (section 3.4) : en l'état, le programme refuserait même une vérification.
10. **L'échéance de GO-2026-11-21-69 (2026-11-22) n'est pas contrôlée pour l'exemption** : le chef ne contrôle que la forme de `exemption_de_la_sonde_go` (ligne 1441). L'échéance contrôlée est celle du GO de chaque ligne de calcul (garde 8).
11. **La règle 7 du texte** (sortie maximale à la course : quatre fois le maximum observé à l'essai) lira un essai joué à 65 536 : elle peut rendre un plafond de course au-dessus de la sortie maximale du modèle, et la règle des appels à Google s'y appliquera aussi. C'est l'affaire du devis de la course.
12. **Le corps d'un appel de vérification est pris à 160 octets** : supposé ; sans effet sur le plafond tant qu'un corps ne passe pas 5 653 octets.
13. **Tous les chiffres hérités du devis restent non opposables** (R7) : prix, débit déclaré, comportement de la coupure. Cet avenant n'en vérifie aucun.
14. **Cet avenant n'est ni scellé, ni contre-lu.** Ses chiffres sont à refaire par le vérificateur ; ses citations, à confronter de nouveau.
15. **Les textes des lignes 2 et 4 sont longs** : plus de deux mille signes chacun, comme ceux de l'avenant 1. Les consignes permanentes bornent une ligne de registre à 600 signes : la ligne du registre peut renvoyer au texte de la section 8 par l'empreinte de cet avenant, plutôt que le recopier.

## 11. Ce que j'ai ouvert

### 11.1 Version 1, par son rédacteur (inchangé)

- **Le mandat**, en entier, après vérification de son empreinte (`55a08330…`, égale à l'attendu et à son compagnon).
- **Le devis accepté**, en entier, sections 16 à 19 comprises ; **l'avenant 1, version 3**, en entier ; **sa vérification** (`verification-avenant-1-v3-devis-essais-admission-v1.md`, sha256 `8232e22e2c588d753b9f8c9b92d21d66be269ca3d5f52418c4545951e92edd2e`), en entier ; **la confrontation à la règle**, en entier ; **la note de la livraison 4**, en entier. Les cinq empreintes sont égales à leurs compagnons.
- **La règle** : par la commande du mandat, sur la référence locale `origin/main` (commit `f64d95ac9`), sans `git fetch`.
- **Le registre** : les trois lignes GO-2026-11-21-68, -69 et -71, par `git show origin/main:registres/go.md | grep`, la recherche ancrée sur l'identifiant en début de ligne. Chacune porte aussi des décisions sur d'autres travaux, vues en passant : je n'en fais rien et n'en recopie rien.
- **Le journal** : les deux entrées OD-301 et OD-302, par la commande du mandat ; fichier non ouvert.
- **Trois extraits gardés au bloc-notes**, pour y confronter les citations : la section de la règle, les trois lignes du registre, les deux entrées du journal. Ils ne sont pas versés au dépôt.
- **Le dossier du taux** : sa liste (deux fichiers), le relevé et son compagnon.
- **Débords, déclarés.** Deux commandes ont parcouru le dossier de la relance sans en afficher aucun nom : un compte de ses entrées (528), et, après une première composition de cette pièce, un compte des noms égaux à celui du fichier livré (1). Le mandat ne demandait aucune liste ; ni l'une ni l'autre n'a montré un nom. Dans l'arbre de travail : `git rev-parse HEAD` (`45b8ebcfb…`), `git rev-parse origin/main`, et `git status --short`, qui ne rend que le fichier livré. Cette pièce a été composée deux fois : la première composition (sha256 `7a701ba3…`) disait ce débord de façon incomplète ; elle est gardée au bloc-notes, non livrée.
- **Non ouverts** : le gabarit de configuration, le programme et ses essais ; les pièces des mots de Lazar ; les relevés documentaires ; le texte du préenregistrement ; la vérification du devis ; les versions 1 et 2 de l'avenant 1 et leurs contre-lectures.
- **Cloisonnement** : aucun chemin de la liste du mandat n'a été ouvert, listé, cherché ni empreinté. Les pièces lues citent des chemins cloisonnés ; je ne les ai pas suivis, et cet avenant n'en recopie aucun, hors la commande du registre que le mandat donne. Hors les trois lignes nommées, `registres/` n'a pas été ouvert ; `.claude/settings.json` non plus.
- **Registre** : cet avenant ne nomme aucune ligne de GO d'un autre jour que le 21 novembre.
- Aucun réseau, aucun `git fetch`, aucune clé lue ni affichée, aucun appel de modèle, aucun sous-agent, aucune dépense. Rien scellé, rien committé.
- **Programmes**, dans le bloc-notes de la session, hors du dépôt (`/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/redacteur-avenant-2/`) : `calc_av2.py` (sha256 `83d296efcd1d6504e6676e9c9b3e26e11ef66194dff5d68b1e057274ef3efb41`), qui calcule ; `faire_av2.py`, qui compose cette pièce et confronte chaque citation à sa ligne ; `verif_av2.py`, qui relit la pièce composée — chaque nombre à virgule y est cherché dans la sortie du calcul ou dans les pièces lues.

### 11.2 Version 2, par son rédacteur

- **Le mandat de cette version** : le message de la session mère, non versé au dépôt (copie au bloc-notes, `entrees/mandat-mere-v2.txt`, pour confronter les citations de la section 13). Pour mes interdits, le mandat du rédacteur de la version 1 (`mandat-redacteur-fable-avenant-2-plafond-65536-v1.md`, sha256 `55a08330…`, égale à son compagnon), lu en entier.
- **Lus en entier** : la version 1 (`5f84642a…`) ; sa vérification (`037aa7f7…`) ; la note de la livraison 8 (`note-programme-essais-admission-bras-a-v7.md`, `d8efceb2…`) ; la note de la livraison 7 (`note-programme-essais-admission-bras-a-v6.md`, `5a6a41f5…`). Chacune égale à son compagnon.
- **Lus en partie** :
  - la note de la livraison 6 (`note-programme-essais-admission-bras-a-v5.md`, `d72788d7…`), sections 1 à 6 : les notes des livraisons 8 et 7 disent que le reste des notes d'avant vaut encore ;
  - le chef v7 (`scripts/chef_essais_admission_bras_a_v7.py`, `7c63d051…`) : lignes 1 à 135, 440 à 660, 905 à 1010, 1669 à 1800, 1860 à 1960, 2335 à 2356, 2495 à 2512, 2772 à 2786 et 2846 à 3000, plus des recherches de noms ;
  - le gabarit v7 (`configuration-essais-admission-bras-a-v7-gabarit.json`, `e1da2133…`), par programme : ses clés, les champs de `fournisseurs.google`, les trois lignes de Google, quatre notes. Il cite des chemins sous `runs/`, non suivis ;
  - le devis (`421ee2e6…`), lignes 213 à 221 ; l'avenant 1, version 3 (`5e255c5f…`), ses titres et ses lignes 329 à 345 ;
  - les deux relevés que nomme m-2 : `releve-api-mistral-gemini-essais-admission-v1.md` (`291341e2…`), lignes 10 à 25 ; `juge-des-ancres-identifiant-gemini-v1.md` (`ac8bb15e…`), lignes 1 à 30. Le second cite une pièce de mots de Lazar, non suivie ;
  - le dossier des programmes de la version 1 (`avenant-2-programmes-v1/`), sa liste ; son programme de calcul (`calc_av2.py`, `83d296ef…`), lignes 1 à 200, non exécuté.
- **Empreintes seules**, toutes égales à leurs compagnons : la vérification du devis (`0bec479f…`), la confrontation à la règle (`b49688eb…`), la vérification de l'avenant 1 v3 (`8232e22e…`), la note de la livraison 4 (`fbb30439…`), `faire_av2.py` et `verif_av2.py` de la version 1. Le relevé du taux (`a234540a…`) est lu par programme : jour du fixage et taux du dollar.
- **Journal** : la seule entrée OD-315, par `grep -E '^- OD-315 '` ; fichier non ouvert.
- **Registre** : les lignes GO-2026-11-21-68, -69 et -71, par `git show origin/main:registres/go.md | grep -E '^\| GO-2026-11-21-(68|69|71) \|'`. Elles portent aussi des décisions sur d'autres travaux, vues en passant : je n'en recopie rien. Les lignes GO-2026-11-21-74 et -84 ne sont pas lues : la première est citée d'après la vérification, la seconde d'après le mandat.
- **Ouverture hors liste, autorisée par la mère** (mandat, R-4684 ; journal, entrée OD-315) : `docs/sources/google-gemini-reflexion-v1/`, et lui seul sous `docs/sources/`. Sa liste par `git ls-tree -r -l origin/main -- docs/sources/google-gemini-reflexion-v1/` ; ses trois fichiers et leurs compagnons par `git show origin/main:<chemin>`, sur la référence locale `origin/main` (commit `1fa3a5a3…`), sans `git fetch`, copiés au bloc-notes pour être lus ; empreintes égales aux compagnons. Lus : la provenance, en entier ; de la page de la réflexion, les lignes 1 à 40, 130 à 142, 581 à 700, 740 à 760 et 896 à 1015, plus des recherches de mots ; de la référence, les lignes 1 à 12, 130 à 145, 258 à 290, 2622 à 2635 et 2825 à 2860, plus des recherches de mots.
- **Git** : `git status --short`, `git log --oneline -5`, `git rev-parse origin/main`, `git log -1 origin/main`.
- **Débord, déclaré.** Ma première commande a listé le dossier de la relance (`ls … | head -100`, puis le compte de ses entrées : 571) : elle a affiché ses cent premiers noms, dans l'ordre alphabétique, jusqu'à `credits-essai-google-et-gemini-releve-v1.md`. Aucun ne porte un motif interdit, et le dossier cloisonné de la relance n'y figure pas. Le mandat ne demandait aucune liste.
- **Cloisonnement** : aucun chemin de la liste du mandat n'a été ouvert, listé, cherché ni empreinté. Les pièces lues citent des chemins cloisonnés ou sous `runs/` : je ne les ai pas suivis, et cette pièce n'en ajoute aucun. Hors les trois lignes dites, `registres/` n'a pas été ouvert ; `.claude/settings.json` non plus.
- **Registre** : cette pièce ne recopie rien de ce que le mandat défend d'y recopier, et ne nomme aucune ligne de GO d'un autre jour que le 21 novembre.
- Aucun réseau, aucun `git fetch`, aucune clé lue ni affichée, aucun appel de modèle, aucun sous-agent, aucune dépense. Rien scellé, rien committé.
- **Programmes**, au bloc-notes, hors du dépôt (`/tmp/claude-0/-home-user-controle-ia-travail/080a2aff-9781-5a4d-8af3-2aae94066157/scratchpad/redacteur-av2-v2/programmes/`) : `calc_av2_v2.py`, `epreuves_chef_v7.py`, `faire_av2_v2.py`, `verif_av2_v2.py` (empreintes et sorties en section 12.2). `epreuves_chef_v7.py` charge le module du chef v7 sans le lancer, les variables de clé retirées de l'environnement, et n'appelle que trois fonctions : `convertir` ; `controler_credit_de_google`, sa lecture des dépenses remplacée par des valeurs fixées (aucun dossier lu) ; `verifier_ligne_de_calcul`, sur un registre factice, en mémoire.

## 12. Calculs, par programme

### 12.1 Version 1 : sortie de `calc_av2.py` (inchangée)

Sortie de `calc_av2.py`, entière. Nombres décimaux exacts ; « -> » marque un arrondi, vers le haut sauf mention. Entrées : les prix, les délais, le débit déclaré et les bornes d'octets du devis ; les soldes des deux projets ; le taux du relevé, lu dans le fichier.

```
=== 1. Contrôle du programme : à 32 768, il redonne les chiffres du devis et de l'avenant 1
réserve d'un envoi de la file : 0,015 + 0,49152 = 0,50652 (devis : 0,507) ; 0,072 + 0,49152 = 0,56352 (devis : 0,564)
réserve d'un envoi de vérification, corps de 160 octets : 0,00048 + 0,49152 = 0,492 (devis : 0,492)
pire cas des seize envois : 2 × (6 × 0,50652 + 2 × 0,56352) = 8,33232 (devis : 8,33, au plus proche) ; demi-dollar supérieur : 8,50 (devis : 8,50)
pire cas des trois envois de vérification : 3 × 0,492 = 1,476 (devis : 1,48) ; demi-dollar supérieur : 1,50 (devis : 1,50)
excès d'un envoi : file, 8,07 − 0,49152 = 7,57848 (devis : 7,58) ; vérification, 2,67 − 0,49152 = 2,17848 (devis : 2,18)
plafond et excès : 1,50 + 2,18 = 3,68 (devis : 3,68) ; 8,50 + 7,58 = 16,08 (devis : 16,08) ; ensemble 19,76 (devis : 19,76)
file, neuf excès : 8,50 + 9 × 7,57848 = 76,70632 ; l'avenant 1 écrit 76,70, calculé sur 7,578 (76,702)
Google, deux vérifications : régime prudent, 2 × 3,68 + 16,08 = 23,44 (avenant 1 : 23,44) ; neuf excès, 2 × 3,68 + 76,70 = 84,06 (avenant 1 et registre : 84,06)
débit qui tient 32 768 jetons en 2 690 secondes : 12,1814 -> 12,2 (devis : 12,2)
durée sous laquelle un envoi est compté à sa réserve : 32 768 ÷ 200 = 163,84 -> 164 secondes (devis : 164)
seuil de refus du compteur, envoi de couverture : 8,50 − 0,56352 = 7,93648 (devis : 7,93)
journal, entrée OD-301 : 3,68 × 1,05 ÷ 1,0990 = 3,5159 -> 3,52 € ; 23,44 × 1,05 ÷ 1,0990 = 22,3949 -> 22,40 € ; manque 10,47 et 6,81 €

=== 2. Chiffres neufs, sortie maximale envoyée à Google : 65 536 jetons
sortie pleine : 65 536 × 15 ÷ 1 000 000 = 0,98304 USD (à 32 768 : 0,49152)
réserve d'un envoi de la file, appariement : 0,015 + 0,98304 = 0,99804 -> 0,999
réserve d'un envoi de la file, couverture : 0,072 + 0,98304 = 1,05504 -> 1,056
réserve d'un envoi de vérification (appels A, A′ et sonde), corps de 160 octets : 0,00048 + 0,98304 = 0,98352 -> 0,984
pire cas des seize envois de la file, sortie pleine : 2 × (6 × 0,99804 + 2 × 1,05504) = 16,19664 -> 16,20
   par clé (trois lectures d'appariement, une de couverture, deux envois) : 2 × (3 × 0,99804 + 1,05504) = 8,09832 -> 8,10 ; les deux : 16,19664
pire cas des trois envois d'une vérification : 3 × 0,98352 = 2,95056 -> 2,96
plafond de la file, demi-dollar supérieur du pire cas : 16,50 USD (marge 0,30336)
plafond d'une vérification, demi-dollar supérieur du pire cas : 3,00 USD (marge 0,04944)
   le plafond de 3,00 laisse passer trois envois tant que le corps d'un appel ne passe pas (3,00 ÷ 3 − 0,98304) × 1 000 000 ÷ 3 = 5 653 octets
   au plafond de 1,50 gardé, deux envois comptés à leur réserve : 2 × 0,98352 = 1,96704 -> 1,97, au-dessus de 1,50 : le second serait refusé
   coût d'un appel de vérification à sortie pleine : 0,98352 -> 0,99 (devis, 13, point 12 : 0,49)
   un quatrième envoi : 4 × 0,98352 = 3,93408, au-dessus de 3,00 : refusé
   le plafond de 16,50 tient les seize envois à sortie pleine tant que les huit corps ne passent pas ensemble (16,50 − 16 × 0,98304) × 1 000 000 ÷ 3 ÷ 2 = 128 560 octets (bornes du devis : 6 × 5 000 + 2 × 24 000 = 78 000)
   pour information, trois envois par appel (colonne du devis) : 3 ÷ 2 × 16,19664 = 24,29496 -> 24,30 (devis : 12,50)
seuil de refus du compteur avant un envoi de couverture : 16,50 − 1,05504 = 15,44496 -> 15,44 (vers le bas)
sortie d'un envoi coupé, à 200 jetons par seconde : file, 2 690 × 200 × 15 ÷ 1 000 000 = 8,07 ; vérification, 890 × 200 × 15 ÷ 1 000 000 = 2,67 (inchangées)
excès possible d'un seul envoi, file : 8,07 − 0,98304 = 7,08696 -> 7,09
excès possible d'un seul envoi, vérification : 2,67 − 0,98304 = 1,68696 -> 1,69
   à 100 jetons par seconde : file 3,06 ; vérification 0,36
   à 400 jetons par seconde : file 15,16 ; vérification 4,36
plafond et excès, ce que le compteur borne : vérification, 3,00 + 1,69 = 4,69 ; file, 16,50 + 7,09 = 23,59
coût d'un envoi de la file coupé à 2 690 secondes : 8,085 (appariement) ; 8,142 (couverture) -> 8,09 ; 8,15 (inchangé)
neuf envois coupés seuls : 9 × 8,085 = 72,765 ; 6 × 8,085 + 3 × 8,142 = 72,936 (inchangé : 72,77 et 72,94)
   ces neuf envois, comptés à leur réserve au régime courant : 9 × 0,99804 = 8,98236 -> 8,99 (devis : 4,56)
file, neuf excès : 16,50 + 9 × 7,08696 = 80,28264 -> 80,29
   écart avec l'ancien : 80,28264 − 76,70632 = 3,57632 -> 3,58 = 8,00 de plafond − 9 × 0,49152
Google, deux vérifications, régime prudent ou supposition tenue : 2 × 4,69 + 23,59 = 32,97
Google, deux vérifications, neuf excès : 2 × 4,69 + 80,29 = 89,67 (exact : 89,65656)
   au-dessus du pire cas accepté sous GO-2026-11-21-68 : 89,67 − 84,06 = 5,61
   en valeurs exactes : 89,65656 − 84,06328 = 5,59328 -> 5,60
   une ligne nouvelle de vérification ajoute 4,69
   avec une seule vérification : 4,69 + 23,59 = 28,28 ; 4,69 + 80,29 = 84,98 (avenant 1 : 19,76 et 80,38)

=== 2 bis. Régime prudent du compteur, à 65 536
durée sous laquelle un envoi est compté à sa réserve : 65 536 ÷ 200 = 327,68 -> 328 secondes
appel de vérification coupé à 890 secondes : compté 2,67048 -> 2,68, sous le plafond de 3,00 ; avec la réserve de l'envoi suivant, 3,654 -> 3,66, au-dessus : l'envoi suivant est refusé
   un appel coupé avant (3,00 − 0,98352 − 0,00048) ÷ 0,003 = 672 secondes laisse partir l'envoi suivant (à 1,50 : 335,84)
file partie sur un mot de Lazar, envoi coupé à 2 690 secondes : compté 8,085 ou 8,142
   la reprise part si le cumul compté avant l'envoi coupé est d'au plus 16,50 − 8,085 − 0,99804 = 7,41696 (appariement) ; 16,50 − 8,142 − 1,05504 = 7,30296 (couverture) ; au plus bas des deux, vers le bas : 7,30
   à 8,50 : 8,50 − 8,085 − 0,50652 = −0,09152 : négatif, la reprise était toujours refusée
   deux envois coupés à 2 690 secondes : 2 × 8,085 = 16,17 ; avec la réserve du suivant, 17,16804, au-dessus de 16,50 : la file s'arrête à son plafond
   borne de la dépense au régime prudent : (16,50 − 1,05504) + 8,142 = 23,58696 -> 23,59 = plafond et un excès

=== 3. Sommes des six lignes de calcul
plafonds : Mistral 0,25 + 4,75 + 0,25 = 5,25 ; Google 3,00 + 3,00 + 16,50 = 22,50 ; ensemble 27,75 (sans la ligne 5 : 27,50) ; avenant 1 : 16,75
excès, un par ligne : Mistral 1,17 + 0,64 + 1,17 = 2,98 ; Google 1,69 + 1,69 + 7,09 = 10,47 ; ensemble 13,45 (sans la ligne 5 : 12,28) ; avenant 1 : 14,92
plafonds et excès : 27,75 + 13,45 = 41,20 (sans la ligne 5 : 39,78) ; avenant 1 : 31,67 ; recoupe 8,23 + 32,97 = 41,20
   avec les lignes de Mistral et une seule vérification de Google : 8,23 + 28,28 = 36,51 (devis, ligne 563 : 27,99)
pire cas à la sortie maximale, tous envois (colonne du devis, 6.3) : 3,99 + 16,20 + 0,23 + 0,23 + 2,96 + 2,96 = 26,57 (devis : 14,26 ; avec la seconde vérification à 1,48 : 15,74)
attendu : inchangé, ≈ 0,57 USD (devis 0,55, plus 0,02 pour la seconde vérification) : il ne dépend pas de la sortie maximale
   attendu chez Google seul : 0,34 + 0,02 + 0,02 = 0,38 USD (devis, 6.3)

=== 4. Seuils de crédit par projet, et manque en euros
taux relevé : 1,0990 USD pour 1 €, fixage du 2026-11-20 ; diminué de 5 % : 1,0990 × 0,95 = 1,04405
seuil avant chaque vérification de clé : 4,69 + 23,59 = 28,28 USD (avenant 1 : 19,76)
seuil avant la file du juge : 23,59 USD (avenant 1 : 16,08)
crédit compté aujourd'hui, solde seul : projet à 11,93 € : 11,93 × 1,04405 = 12,4555165 -> 12,45 USD ; projet à 15,59 € : 15,59 × 1,04405 = 16,2767395 -> 16,27 USD (un crédit se compte vers le bas)
   ni l'un ni l'autre n'atteint 23,59, ni même le plafond seul de la file, 16,50 ; à l'ancien plafond de 8,50, les deux le couvraient
ligne | seuil | dépense retirée (pire ; attendue) | crédit compté à avoir | euros à voir | manque à 11,93 € | manque à 15,59 €
vérification de la clé 1 (ligne 2), première ligne de Google | 28,28 | pire : 0,00 | 28,28 + 0,00 = 28,28 USD | 28,28 ÷ 1,04405 = 27,0868 -> 27,09 € | 15,16 € | 11,50 €
vérification de la clé 1 (ligne 2), première ligne de Google | 28,28 | attendu : 0,00 | 28,28 + 0,00 = 28,28 USD | 28,28 ÷ 1,04405 = 27,0868 -> 27,09 € | 15,16 € | 11,50 €
vérification de la clé 2 (ligne 6) | 28,28 | pire : 4,69 | 28,28 + 4,69 = 32,97 USD | 32,97 ÷ 1,04405 = 31,5789 -> 31,58 € | 19,65 € | 15,99 €
vérification de la clé 2 (ligne 6) | 28,28 | attendu : 0,02 | 28,28 + 0,02 = 28,30 USD | 28,30 ÷ 1,04405 = 27,1059 -> 27,11 € | 15,18 € | 11,52 €
file du juge (ligne 4) | 23,59 | pire : 9,38 | 23,59 + 9,38 = 32,97 USD | 32,97 ÷ 1,04405 = 31,5789 -> 31,58 € | 19,65 € | 15,99 €
file du juge (ligne 4) | 23,59 | attendu : 0,04 | 23,59 + 0,04 = 23,63 USD | 23,63 ÷ 1,04405 = 22,6330 -> 22,64 € | 10,71 € | 7,05 €
pour passer les trois lignes même au pire : 31,58 € vus sur chaque projet ; manque 19,65 € et 15,99 €, soit 35,64 € en tout
   contrôle : 31,58 € comptent pour 32,97 USD ; 31,57 € pour 32,96 USD ; les deux projets ensemble : 2 × 31,58 = 63,16 €
au plus juste, vérifications à leur attendu de 0,02 USD chacune : 27,11 € vus sur chaque projet ; manque 15,18 € et 11,52 €, soit 26,70 € en tout
   alors la seconde vérification ne part que si la première est comptée au plus 0,02 USD, et la file que si les deux le sont au plus 4,71 USD ensemble
   première vérification comptée 0,25 USD : 28,53 USD, soit 27,33 € vus par projet
   première vérification comptée 1,00 USD : 29,28 USD, soit 28,05 € vus par projet
pour mémoire, aux seuils de l'avenant 1, avant une vérification, la première : 19,76 USD -> 18,93 € ; manque 7,00 € et 3,34 €
pour mémoire, aux seuils de l'avenant 1, avant la seconde vérification ou la file, au pire : 23,44 USD -> 22,46 € ; manque 10,53 € et 6,87 €
   le journal (OD-301) écrit 22,40 € pour 23,44 USD : 22,40 € comptent pour 23,38 USD, sous 23,44 ; la règle de l'avenant 1 demande 22,46 €
   versement de plus que le plafond neuf demande, au pire : 35,64 − (10,53 + 6,87 = 17,40) = 18,24 €
   besoin propre d'une vérification, sans la file : 4,69 USD -> 4,50 € : les deux soldes le couvrent
essai chiffré de la règle (avenant 1, section 7, point 7), valeurs neuves : cas sain, dépenses de 4,69 et 0,02, deux projets distincts, crédit compté de 28,28 : 28,28 − 4,69 = 23,59, la file part ; artefact, somme retirée : 28,28 − 4,71 = 23,57, sous 23,59

=== 5. Débit requis et délais
débit qui tient 65 536 jetons en 2 690 secondes : 65 536 ÷ 2 690 = 24,3628 -> 24,4 jetons par seconde (à 32 768 : 12,2)
à 12,2 jetons par seconde, 2 690 secondes rendent 32 818 jetons ; à 24,4 : 65 636
appel de vérification à sortie pleine en 890 secondes : 65 536 ÷ 890 = 73,6359 -> 73,7 jetons par seconde (à 32 768 : 36,9) ; le devis ne l'exige pas
délai global de la file du juge : 8 × (2 × 2 700 + 600 + 10) + 600 = 48 680 secondes ; d'un lancement de vérification : 3 × 900 + 600 = 3 300 : inchangés
durée d'une lecture de 65 536 jetons : à 24,4 jetons par seconde, 2 685,9 secondes ; à 12,2, 5 371,8 ; à 50, 1 310,7
pour information, délai qui garderait 12,2 jetons par seconde : 65 536 ÷ 12,2 = 5 371,8 secondes -> relais 5 390, délai 5 400 (65 536 ÷ 5 390 = 12,1588)
   alors : sortie d'un envoi coupé 16,17 ; excès 15,18696 -> 15,19 ; plafond et excès de la file 31,69 ; neuf excès 153,19 ; Google, deux vérifications : 41,07 et 162,57 ; délai global 8 × (2 × 5 400 + 600 + 10) + 600 = 91 880 secondes

=== 6. Borne de réflexion et plafond de texte
plus grande borne de réflexion qui passe la garde : 65 536 − 16 000 = 49 536 jetons ; plafond de texte : 65 536 − 49 536 = 16 000
à l'ancien plafond : 32 768 − 16 000 = 16 768 (la valeur d'essai de la livraison 4)
   limite de mots qui tient dans 16 000 jetons à 1,5 jeton(s) par mot : 10 666 mots
   limite de mots qui tient dans 16 000 jetons à 2 jeton(s) par mot : 8 000 mots
   limite de mots qui tient dans 16 000 jetons à 3 jeton(s) par mot : 5 333 mots
   limite de mots qui tient dans 16 000 jetons à 4 jeton(s) par mot : 4 000 mots

=== 7. Sensibilité au débit déclaré : 400 jetons par seconde au lieu de 200
excès : vérification 4,35696 -> 4,36 ; file 15,15696 -> 15,16
Google, deux vérifications, régime prudent : 2 × (3,00 + 4,36) + 16,50 + 15,16 = 46,38 (avenant 1 : 36,85)
Google, deux vérifications, neuf excès : 2 × 7,36 + 16,50 + 9 × 15,15696 = 167,63264 -> 167,64 (avenant 1 : 162,05)
avec une seule vérification : 3,00 + 4,36 + 16,50 + 15,16 = 39,02 ; 16,50 + 9 × 15,15696 = 152,91264 -> 152,92 (avenant 1 : 30,50 et 149,35)

fin : toutes les assertions passent
```

### 12.2 Version 2 : calculs et épreuves, par programme

Programmes au bloc-notes, hors du dépôt (`/tmp/claude-0/-home-user-controle-ia-travail/080a2aff-9781-5a4d-8af3-2aae94066157/scratchpad/redacteur-av2-v2/programmes/`) : `calc_av2_v2.py` (sha256 `342648e44f78dd0c57185eb953e4a03083ab2d4575a2911aae4d203ddf3cc721`), `epreuves_chef_v7.py` (sha256 `5c44924853a9b727d07660301dcd576751a40d705db95f6fa1664bf06d06509c`), `faire_av2_v2.py` (sha256 `e3e3a5a11593d688ad9bf4f68fcdf8f0502394bba22f2884b11b3eaae5f7cbbd`), `verif_av2_v2.py` (sha256 `6f7e22e0f83b44bbd64e6a7fa047a245f36473576922f01da7970cae5f9fda3f`), `assembler_12_2.py` (sha256 `cf79481678f214def897c08381372e9657dd11e30a0eeb0d1dcf3acafa48923c`). Nombres décimaux exacts ; « -> » marque un arrondi, vers le haut sauf mention. Entrées : celles de la version 1 (prix, délais, débit déclaré et bornes d'octets du devis ; soldes des deux projets ; taux lu dans le fichier du relevé), plus le versement accordé sous GO-2026-11-21-74 (10,47 € et 6,81 €, d'après la vérification, correction 3) et le régime prudent de la mère (journal, entrée OD-315). Règle du programme qui fait foi (chef v7, `convertir`) : crédit compté = montant × taux × 0,95, au centime inférieur ; les seuils, vers le haut.

Commandes, depuis la racine du dépôt (`P` : le dossier des programmes ; `E` : celui des entrées, avec l'entrée OD-315 et le mandat de la mère ; `G` : la copie des pages de Google ; `TAUX` : `docs/notes/relance-organismes-discrets-v1/taux-de-change-v1/bce-eurofxref-daily-releve-2026-11-21T1749Z.xml`) :
- `python3 -I P/calc_av2_v2.py TAUX`
- `env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 python3 -I -B P/epreuves_chef_v7.py . <cette pièce> TAUX`
- `python3 -I P/verif_av2_v2.py . <cette pièce> E G <sortie du calcul>`

#### Sortie de `calc_av2_v2.py`, entière

```

=== 1. Plafonds et excès, sortie maximale de Google à 65 536 jetons (inchangés depuis la version 1)
sortie pleine : 65 536 × 15 ÷ 1 000 000 = 0,98304 USD
réserve d'un envoi : appariement 0,015 + 0,98304 = 0,99804 ; couverture 0,072 + 0,98304 = 1,05504 ; vérification 0,00048 + 0,98304 = 0,98352
pire cas des seize envois de la file : 2 × (6 × 0,99804 + 2 × 1,05504) = 16,19664 ; demi-dollar supérieur : 16,50 USD
pire cas des trois envois d'une vérification : 3 × 0,98352 = 2,95056 ; demi-dollar supérieur : 3,00 USD
sortie d'un envoi coupé, à 200 jetons par seconde : file 2 690 × 200 × 15 ÷ 1 000 000 = 8,07 ; vérification 890 × 200 × 15 ÷ 1 000 000 = 2,67
excès possible d'un seul envoi : file 8,07 − 0,98304 = 7,08696 -> 7,09 ; vérification 2,67 − 0,98304 = 1,68696 -> 1,69
plafond et un excès : vérification 3,00 + 1,69 = 4,69 (exact 4,68696) ; file 16,50 + 7,09 = 23,59 (exact 23,58696)

=== 2. Régime prudent pour les lignes de Google, en vérification comme en file (mère, R-4682 ; journal, OD-315)
règle du compteur (chef v7, `Compteur`) : avant l'envoi, refus si cumul compté + réserve > plafond ; un envoi sans compteur lisible est compté à 200 jetons de sortie par seconde de sa durée, et au moins à sa réserve
vérification : un appel coupé à 890 secondes est compté 0,00048 + 2,67 = 2,67048 -> 2,68 ; avec la réserve de l'envoi suivant, 2,67048 + 0,98352 = 3,654 > 3,00 : l'envoi suivant est refusé
   dépense comptée au plus d'une vérification : (3,00 − 0,98352) + 2,67048 = 4,68696 -> 4,69 = plafond et un excès
file : un envoi coupé à 2 690 secondes est compté 8,085 (appariement) ou 8,142 (couverture) -> 8,09 ou 8,15
   sa reprise part si le cumul compté avant lui vaut au plus 16,50 − 8,085 − 0,99804 = 7,41696 -> 7,41 (appariement) ; 16,50 − 8,142 − 1,05504 = 7,30296 -> 7,30 (couverture) ; vers le bas
   deux envois coupés : 2 × 8,085 = 16,17 ; avec la réserve du suivant, 17,16804 > 16,50 : la file s'arrête à son plafond
   dépense comptée au plus de la file : (16,50 − 1,05504) + 8,142 = 23,58696 ; (16,50 − 0,99804) + 8,085 = 23,58696 -> 23,59 = plafond et un excès
PIRE CAS CHEZ GOOGLE, deux vérifications et la file, au régime prudent : 2 × 4,69 + 23,59 = 32,97 USD (exact : 2 × 4,68696 + 23,58696 = 32,96088 -> 32,97)
   sous le pire cas accepté sous GO-2026-11-21-68 : 84,06 − 32,97 = 51,09 USD de marge
   une ligne nouvelle de vérification ajoute 4,69 : 37,66 USD
pour mémoire, régime courant que la décision écarte : file, neuf excès, 16,50 + 9 × 7,08696 = 80,28264 -> 80,29 ; Google, 2 × 4,69 + 80,29 = 89,67 USD (exact 89,65656) ; au-dessus de 84,06 de 5,61 au grain des lignes
   deux envois coupés de la file, au régime prudent (section 5 de l'avenant) : 8,09 ou 8,15 USD chacun, au lieu de 0,999 ou 1,056 à leur réserve au régime courant
délai de la file relevé à 5 400 secondes (relais à 5 390) : excès 16,17 − 0,98304 = 15,18696 -> 15,19 ; plafond et excès de la file 31,69 ; pire cas chez Google au régime prudent 2 × 4,69 + 31,69 = 41,07 (au régime courant : 162,57)

=== 3. Seuils de crédit, par projet, vers le haut (inchangés)
avant chaque vérification de clé : 4,69 + 23,59 = 28,28 (exact 28,27392 -> 28,28) USD, sur chacun des deux projets
avant la file : 23,59 (exact 23,58696 -> 23,59) USD, sur chacun des deux projets

=== 4. Crédit compté et manque en euros, au taux relevé
taux relevé : 1,0990 USD pour 1 €, fixage du 2026-11-20 ; crédit compté = montant × 1,0990 × 0,95 = montant × 1,04405, au centime inférieur
projet à 11,93 € : 11,93 × 1,04405 = 12,4555165 -> 12,45 USD ; après le versement de GO-2026-11-21-74, 11,93 + 10,47 = 22,40 € ; 22,40 × 1,04405 = 23,38672 -> 23,38 USD
projet à 15,59 € : 15,59 × 1,04405 = 16,2767395 -> 16,27 USD ; après le versement de GO-2026-11-21-74, 15,59 + 6,81 = 22,40 € ; 22,40 × 1,04405 = 23,38672 -> 23,38 USD
   23,38 USD : sous 28,28 et sous 23,59 ; au-dessus du plafond seul de la file, 16,50 : aucune ligne de Google ne part encore
ligne | seuil | dépense retirée | crédit compté à avoir | euros à voir | manque au 21 novembre (11,93 € ; 15,59 €) | manque après le versement de GO-74 (22,40 € sur chacun)
vérification de la clé 1 (ligne 2), première ligne de Google | 28,28 | pire : 0,00 | 28,28 + 0,00 = 28,28 USD | 28,28 ÷ 1,04405 = 27,0868… -> 27,09 € | 15,16 € ; 11,50 € | 4,69 €
vérification de la clé 1 (ligne 2), première ligne de Google | 28,28 | attendu : 0,00 | 28,28 + 0,00 = 28,28 USD | 28,28 ÷ 1,04405 = 27,0868… -> 27,09 € | 15,16 € ; 11,50 € | 4,69 €
vérification de la clé 2 (ligne 6) | 28,28 | pire : 4,69 | 28,28 + 4,69 = 32,97 USD | 32,97 ÷ 1,04405 = 31,5789… -> 31,58 € | 19,65 € ; 15,99 € | 9,18 €
vérification de la clé 2 (ligne 6) | 28,28 | attendu : 0,02 | 28,28 + 0,02 = 28,30 USD | 28,30 ÷ 1,04405 = 27,1059… -> 27,11 € | 15,18 € ; 11,52 € | 4,71 €
file du juge (ligne 4) | 23,59 | pire : 9,38 | 23,59 + 9,38 = 32,97 USD | 32,97 ÷ 1,04405 = 31,5789… -> 31,58 € | 19,65 € ; 15,99 € | 9,18 €
file du juge (ligne 4) | 23,59 | attendu : 0,04 | 23,59 + 0,04 = 23,63 USD | 23,63 ÷ 1,04405 = 22,6330… -> 22,64 € | 10,71 € ; 7,05 € | 0,24 €
contrôle : 31,58 € comptent 32,97 USD ; 31,57 € n'en comptent que 32,96
pour que les trois lignes passent même au pire : 31,58 € vus sur chaque projet ; aux soldes du 21 novembre, manque 19,65 € et 15,99 €, soit 35,64 € ; après le versement de GO-2026-11-21-74, manque 9,18 € et 9,18 €, soit 18,36 €
au plus juste (première vérification comptée 0,02 USD) : 27,11 € par projet ; aux soldes du 21 novembre, manque 15,18 € et 11,52 €, soit 26,70 € ; après le versement, 4,71 € et 4,71 €, soit 9,42 €
avant la première vérification seule : 27,09 € ; après le versement, manque 4,69 € sur chacun

=== 5. Sommes des six lignes de calcul (inchangées)
plafonds : 5,25 + 3,00 + 3,00 + 16,50 = 27,75 ; excès, un par ligne : 2,98 + 1,69 + 1,69 + 7,09 = 13,45 ; ensemble 41,20
débit qui tient 65 536 jetons en 2 690 secondes : 24,3628… -> 24,4 jetons par seconde (inchangé)

fin : toutes les assertions passent
```

#### Sortie de `epreuves_chef_v7.py`, entière

Le module du chef v7 est chargé sans être lancé. Les identifiants `GO-2099-01-01-01` à `-03` et les dates de 2099 sont ceux d'un registre factice, en mémoire : ils ne désignent aucune ligne réelle.

```
=== 1. Crédit compté, par `convertir` du chef v7 (marge 0,05, centime inférieur)
11,93 € -> 12,45 USD
15,59 € -> 16,27 USD
22,40 € -> 23,38 USD
27,08 € -> 28,27 USD
27,09 € -> 28,28 USD
27,10 € -> 28,29 USD
27,11 € -> 28,30 USD
31,57 € -> 32,96 USD
31,58 € -> 32,97 USD

=== 2. Seuils et manques, par `controler_credit_de_google` du chef v7 (dépense retirée fixée à la main ; somme des deux)
verification-google-cle-1, 27,09 € sur chaque projet, dépenses {'GEMINI_API_KEY': '0', 'GEMINI_API_KEY_2': '0'} : part (seuil 28.28, retirée 0, la somme des deux (deux projets distincts : non relevé))
verification-google-cle-1, 27,08 € sur chaque projet, dépenses {'GEMINI_API_KEY': '0', 'GEMINI_API_KEY_2': '0'} : ne part pas : projet a de Google : crédit compté 28.27 USD (aucune : recharge non comptée (configuration), solde vu seul) moins dépense retirée 0 USD (la somme des deux (deux projets distincts : non relevé)) = 28.27, sous 28.28 : la ligne ne part pas
verification-google-cle-1, 22,40 € sur chaque projet, dépenses {'GEMINI_API_KEY': '0', 'GEMINI_API_KEY_2': '0'} : ne part pas : projet a de Google : crédit compté 23.38 USD (aucune : recharge non comptée (configuration), solde vu seul) moins dépense retirée 0 USD (la somme des deux (deux projets distincts : non relevé)) = 23.38, sous 28.28 : la ligne ne part pas
verification-google-cle-2, 31,58 € sur chaque projet, dépenses {'GEMINI_API_KEY': '4.69', 'GEMINI_API_KEY_2': '0'} : part (seuil 28.28, retirée 4.69, la somme des deux (deux projets distincts : non relevé))
verification-google-cle-2, 31,57 € sur chaque projet, dépenses {'GEMINI_API_KEY': '4.69', 'GEMINI_API_KEY_2': '0'} : ne part pas : projet a de Google : crédit compté 32.96 USD (aucune : recharge non comptée (configuration), solde vu seul) moins dépense retirée 4.69 USD (la somme des deux (deux projets distincts : non relevé)) = 28.27, sous 28.28 : la ligne ne part pas
verification-google-cle-2, 27,11 € sur chaque projet, dépenses {'GEMINI_API_KEY': '0.02', 'GEMINI_API_KEY_2': '0'} : part (seuil 28.28, retirée 0.02, la somme des deux (deux projets distincts : non relevé))
verification-google-cle-2, 27,11 € sur chaque projet, dépenses {'GEMINI_API_KEY': '0.03', 'GEMINI_API_KEY_2': '0'} : ne part pas : projet a de Google : crédit compté 28.30 USD (aucune : recharge non comptée (configuration), solde vu seul) moins dépense retirée 0.03 USD (la somme des deux (deux projets distincts : non relevé)) = 28.27, sous 28.28 : la ligne ne part pas
file-neon, 31,58 € sur chaque projet, dépenses {'GEMINI_API_KEY': '4.69', 'GEMINI_API_KEY_2': '4.69'} : part (seuil 23.59, retirée 9.38, la somme des deux (deux projets distincts : non relevé))
file-neon, 31,57 € sur chaque projet, dépenses {'GEMINI_API_KEY': '4.69', 'GEMINI_API_KEY_2': '4.69'} : ne part pas : projet a de Google : crédit compté 32.96 USD (aucune : recharge non comptée (configuration), solde vu seul) moins dépense retirée 9.38 USD (la somme des deux (deux projets distincts : non relevé)) = 23.58, sous 23.59 : la ligne ne part pas
file-neon, 22,64 € sur chaque projet, dépenses {'GEMINI_API_KEY': '0.02', 'GEMINI_API_KEY_2': '0.02'} : part (seuil 23.59, retirée 0.04, la somme des deux (deux projets distincts : non relevé))
file-neon, 22,40 € sur chaque projet, dépenses {'GEMINI_API_KEY': '0.02', 'GEMINI_API_KEY_2': '0.02'} : ne part pas : projet a de Google : crédit compté 23.38 USD (aucune : recharge non comptée (configuration), solde vu seul) moins dépense retirée 0.04 USD (la somme des deux (deux projets distincts : non relevé)) = 23.34, sous 23.59 : la ligne ne part pas

=== 3. Texte neuf des lignes de Google au périmètre d'une ligne du registre, par `verifier_ligne_de_calcul` (garde 8)
verification-google-cle-1 : 2731 signes ; marques ['vérification de la clé de `gemini-4-neon` lue sous `GEMINI_API_KEY`', 'trois appels au plus'] présentes ; devis, vérification du devis et avenant 1 cités ; aucune barre ; aucun crochet
verification-google-cle-2 : 2733 signes ; marques ['vérification de la clé de `gemini-4-neon` lue sous `GEMINI_API_KEY_2`', 'trois appels au plus'] présentes ; devis, vérification du devis et avenant 1 cités ; aucune barre ; aucun crochet
file-neon : 2501 signes ; marques ["essai d'admission du juge des deux ancres", '8 appels', 'rangs impairs sous `GEMINI_API_KEY`', 'rangs pairs sous `GEMINI_API_KEY_2`'] présentes ; devis, vérification du devis et avenant 1 cités ; aucune barre ; aucun crochet
cas sain, verification-google-cle-1 : passe
cas sain, verification-google-cle-2 : passe
cas sain, file-neon : passe
artefact, verification-google-cle-2, texte de la ligne 2 sous l'identifiant de la ligne 6 : refusée : garde 8 : la ligne GO-2099-01-01-02 ne nomme pas verification-google-cle-2 (marques du périmètre absentes)
artefact, verification-google-cle-1, plafond de l'ancien devis, 1,50 USD : refusée : garde 8 : la ligne GO-2099-01-01-01 porte le plafond « 1,50 USD » au lieu de « 3,00 USD »
artefact, file-neon, plafond de l'ancien devis, 8,50 USD : refusée : garde 8 : la ligne GO-2099-01-01-03 porte le plafond « 8,50 USD » au lieu de « 16,50 USD »
artefact, file-neon, texte sans l'empreinte de l'avenant 1 : refusée : garde 8 : la ligne GO-2099-01-01-03 ne cite pas l'empreinte de l'avenant 1 au devis
artefact, verification-google-cle-1, texte sans l'empreinte de la vérification du devis : refusée : garde 8 : la ligne GO-2099-01-01-01 ne cite pas l'empreinte de la vérification du devis

fin : toutes les épreuves passent
```

#### Sortie de `verif_av2_v2.py`, entière

```
1. version 1 intacte : 5f84642a… ; vérification : 037aa7f7…
2. section 13.2 : 62 changements lus ; 61 paires réappliquées à la version 1 redonnent la pièce, mot pour mot, jusqu'à la section 12.2
3. sources citées en 13.2, toutes trouvées à la lettre dans leur fichier : vérification 48, journal (OD-315) 24, mandat 39
4. 14 phrases des pages de Google, du devis et des deux relevés trouvées à la ligne dite ; 9 d'entre elles citées à la lettre dans la pièce, et bien présentes
5. nombres décimaux neufs des passages « après » : 28 ; absents de la sortie du calcul, de la version 1, de la vérification, du journal, du mandat et des pages citées : aucun
6. motifs cloisonnés ajoutés par la version 2 : aucun

fin : toutes les relectures passent
```

## 13. Changements depuis la v1

Écrite en marge, comme le mandat le demande : pour chaque changement, la remarque source, citée à la lettre, et le passage de la version 1 puis celui de la version 2, tels quels. Trois sortes de sources : **vérification** — la vérification de la version 1 (`verification-avenant-2-devis-essais-admission-v1.md`, sha256 `037aa7f7f46aca8aa609fcbf70af4a3a643ff6adc8be1d09ccb039775ebc7776`), citée par son numéro de correction (section 6), de mineur (m-1 à m-3), ou par sa section ; **journal** — l'entrée OD-315 (`journal-relance-organismes-discrets-v1.md`, lue par `grep -E '^- OD-315 '`) ; **mandat** — le message de la session mère qui commande cette version 2, non versé au dépôt, cité tel qu'il m'a été donné. Les citations de la vérification et du journal sont confrontées à leur fichier, les « avant » à la version 1, les « après » à cette version, par `verif_av2_v2.py` (section 12.2).

### 13.1 Réserves du rédacteur de la version 2

Ces réserves ne changent rien au corps de la pièce : elles disent ce que j'ai vu en appliquant les remarques, pour le relecteur.

1. **La vérification a lu la livraison 5 ; le programme qui fait foi est le chef v7.** Le programme qui fait foi est `scripts/chef_essais_admission_bras_a_v7.py` (sha256 `7c63d051406989e7928c0f6796ac6edb2033920fe18bfd12798e6e7227024806`, égale à son compagnon), avec sa note (`note-programme-essais-admission-bras-a-v7.md`, `d8efceb2…`). La vérification renvoie au chef v4. Ses textes de remplacement sont écrits à la lettre, numéros de ligne du chef v4 compris. Je les ai confrontés au chef v7 :
   - borne démentie (correction 2) : `borne_dementie`, lignes 1764 à 1770 ; dans la file, défaut et arrêt, lignes 2872 à 2875 ; à une vérification, ligne 13 du classement, lignes 2348 à 2350 ; champs `borne_de_reflexion_dementie` (ligne 2507) et `bornes_de_reflexion_dementies` (lignes 2781 et 3101). Conforme. **À la sonde** : une borne démentie y est bien une mesure, à la fiche (lignes 2505 à 2507), mais toute borne démentie, sonde comprise, fait aussi du relevé de vérification un « nœud de Lazar » (lignes 2779 et 2780). La phrase « À la sonde : une mesure » est à lire avec cela ;
   - exemption de la sonde (correction 5, point 9) : `garde_google_avant_envoi` rend la main pour le corps de la sonde avant les contrôles (2) et (3), lignes 1745 à 1755 (au chef v4 : lignes 1486 à 1497). Conforme ;
   - forme seule de `exemption_de_la_sonde_go` (correction 7) : ligne 1687 (au chef v4 : ligne 1441). Conforme ;
   - arguments `--borne-reflexion` et `--plafond-exempte` (correction 5) : passés par le chef, lignes 3292 à 3294 (au chef v4 : lignes 3025 à 3027). Conforme ;
   - la garde 8 ne lit toujours qu'un avenant (correction 5) : lignes 503 à 505, et 1282 à 1290 pour une configuration définitive. Conforme : le champ de l'avenant 2 reste à coder ;
   - `credit_a_avoir_usd` (correction 5) : le chef v7 ne le lit pas non plus ;
   - dépense retirée (correction 4) : `controler_credit_de_google`, lignes 929 à 970 ; la plus grande des deux n'est retirée que si les deux projets sont distincts **et** le lien entre clé et projet constaté (lignes 948 et 949). Conforme ;
   - régime prudent (journal, OD-315) : déjà codé au chef v7, champ `regime_file_google` (note de la livraison 7, section 2 ; « prudent » exigé d'une configuration définitive). Le compteur compte un envoi sans compteur lisible à 200 jetons de sortie par seconde de sa durée, au moins à sa réserve (classe `Compteur`, ligne 1888 et suivantes) : c'est ce que calcule la section 12.2.
2. **Correction 6 : la ligne de taux qu'elle donne serait refusée par le chef v7.** Depuis la livraison 6, `MOTIF_TAUX` exige « ; fixage publié le : AAAA-MM-JJ » à la fin de la ligne de taux (chef v7, lignes 519 et 520), et la note de la livraison 6 l'écrit (`note-programme-essais-admission-bras-a-v5.md`, `d72788d7…`, section 3) : « L'ancienne forme, sans la date du fixage, est refusée. » La ligne que la correction 6 donne « sans code neuf » n'a pas ce champ : le chef v7 la refuserait, et rien ne partirait (aucune dépense). Je l'ai écrite à la lettre, comme mon mandat le veut ; la forme que lit le chef v7 ne vient d'aucune de mes deux sources, et je ne l'ajoute pas. **À trancher par le relecteur.**
3. **m-3 et la correction 6 tirent en sens contraires.** m-3 : la règle des cinq jours est « à relever avec la page de ce calendrier, ou à retirer si le contrôle n'est pas codé ». Je ne peux pas relever la page : aucun réseau, aucune pièce permise. Le contrôle des cinq jours n'est codé ni au chef v4 (la correction 6 le dit fait « par le vérificateur de la pièce ») ni au chef v7, qui borne l'âge du fixage autrement (`age_max_du_fixage`, ligne 553). Le retirer rendrait fausse la phrase de la correction 6 « Les contrôles 2 et 4 sont alors faits par le vérificateur de la pièce ». J'écris donc l'alternative de m-3 sans la trancher.
4. **m-2 : la place.** m-2 dit « Point 3 de la section 4 ». La seule place de la section 4 qui parle des relevés déjà au dépôt est le point 1 de « Ce qu'il faut relever » (« Le relevé des niveaux de réflexion que cite le devis … je ne l'ai pas ouvert ») : j'y cite les deux relevés. Le point 3 de cette liste (`thoughtsTokenCount`) ne les reçoit pas. Il porte, en revanche, la « proposition de la section 4 » que reprenait le point 8 de la section 9 : laissé tel quel, il aurait dit « à ajouter » ce que la correction 2 dit « déjà au programme ». J'y porte les mots de la correction 2 (13.2).
5. **Ce que la décision de la mère touche, au-delà du texte de la correction 1.** La correction 1 donne, pour la ligne 4, une forme « sous le levier (a) » et un passage à retirer. Trois choses en suivent, que j'écris avec la décision pour source (journal, OD-315), chacune dite en 13.2 :
   - dans la ligne 4, les mots « quand la file part sur un mot de Lazar, », qui ouvraient le régime prudent, disaient une condition qui n'en est plus une : je les retire ;
   - la ligne 4 dit sa référence : « (décision de la session mère sous GO-2026-11-21-69, R-4682) », comme le mandat le demande (« avec sa référence ») ;
   - là où la version 1 donnait 89,67 USD pour le pire cas, je le dis du régime courant, et j'écris le nœud tranché (sections 0, 1.4, 2, 2.4, 5 et 10). Deux chiffres de la section 5 changent avec le régime, recalculés en 12.2 : les deux envois coupés comptés 8,09 ou 8,15 USD chacun au lieu de 0,999 ou 1,056 ; et, sous un délai relevé à 5 400 secondes, un pire cas de 41,07 USD au lieu de 162,57.
6. **Les pages de Google versées** sont deux des quatre que nomme la vérification, en texte et non en PDF, alors qu'elle les demandait « en PDF empreinté, page citée (R7) » ; je cite leurs lignes. Elles disent que la sortie maximale comprend la pensée ; elles ne bornent pas la pensée seule. La borne reste donc marquée « supposée », comme le mandat le permet.
7. **Les versements** : la vérification ne donne que le versement au pire après celui de GO-2026-11-21-74 (9,18 € sur chacun). Le mandat demande le manque après ce versement pour chaque ligne : il est recalculé par programme et porté au tableau de 3.3 (dernière colonne) et à celui de 3.2 (une ligne). Au plus juste, il manque 4,71 € sur chacun.
8. **Les textes des lignes 2, 6 et 4** passent la garde 8 du chef v7 tels quels, placés au périmètre d'une ligne du registre factice ; les artefacts sont refusés (section 12.2). Ils restent longs (réserve 15, gardée) : plus de deux mille signes chacun.

### 13.2 Les changements, un par un

**C-01 — titre.**

Sources :
- Mandat de la session mère : « écrire `docs/notes/relance-organismes-discrets-v1/avenant-2-devis-essais-admission-plafond-google-65536-v2.md`, version 2 de l'avenant 2. »

Avant :

````text
plafond de sortie de Google à 65 536 — note d'écart — v1
````

Après :

````text
plafond de sortie de Google à 65 536 — note d'écart — v2
````

**C-02 — en-tête, état.**

Sources :
- Mandat de la session mère : « écrire `docs/notes/relance-organismes-discrets-v1/avenant-2-devis-essais-admission-plafond-google-65536-v2.md`, version 2 de l'avenant 2. »
- Mandat de la session mère : « Lazar a décidé, pendant la limite de Fable (GO-2026-11-21-84), qu'Opus 5.5 en effort maximal **écrit seulement les corrections, mot pour mot d'après les remarques déjà reçues** ; un Fable 5.2 appelé par l'API relira ensuite. »
- Mandat de la session mère : « Les corrections viennent, **mot pour mot**, de deux sources, et de rien d'autre »

Avant :

````text
- **État** : version 1, brouillon, écrite le 2026-11-21 vers 19:02, temps universel (`date -u`), par un rédacteur neuf (Claude Fable 5.2). Il n'a écrit ni le devis, ni l'avenant 1, ni le programme, ni leurs contre-lectures, et n'a lu aucune pièce du côté habilité. **Non scellée : le mandat l'interdit au rédacteur. Non contre-lue, non acceptée.** C'est une pièce de devis : aucune ligne de calcul ne s'appuie sur elle avant sa contre-lecture par un autre modèle.
````

Après :

````text
- **État** : version 2, brouillon, écrite le 2026-11-21 vers 22:39, temps universel (`date -u`), par un rédacteur neuf (Claude Opus 5.5), sur décision de Lazar (GO-2026-11-21-84) : Opus 5.5 « écrit seulement les corrections, mot pour mot d'après les remarques déjà reçues » ; un Fable 5.2 relira. Il n'a écrit ni le devis, ni les avenants, ni la version 1, ni sa vérification, ni le programme, et n'a lu aucune pièce du côté habilité. **Les corrections viennent de deux sources, et d'elles seules** : la vérification de la version 1 (`docs/notes/relance-organismes-discrets-v1/verification-avenant-2-devis-essais-admission-v1.md`, sha256 `037aa7f7f46aca8aa609fcbf70af4a3a643ff6adc8be1d09ccb039775ebc7776`, égale à son compagnon) ; la décision de la mère sous GO-2026-11-21-69 (R-4682), entrée OD-315 du journal. Chaque changement est dit, avec sa source et son texte avant et après, à la section 13. La version 1 (sha256 `5f84642a…`) n'est pas touchée ; écrite le 2026-11-21 vers 19:02 par un rédacteur neuf (Claude Fable 5.2), elle parle à la première personne : ce « je », dans les passages gardés, est le sien. **Non scellée, non contre-lue, non acceptée.** C'est une pièce de devis : aucune ligne de calcul ne s'appuie sur elle avant sa relecture par un autre modèle.
````

**C-03 — section 0, point 2 (pire cas : écart et nœud).**

Sources :
- Vérification, correction 1 : « Section 0, point 2. Remplacer « Le chiffre accepté est dépassé de 5,61 USD : c'est à lui dire. » par : « Le chiffre accepté est dépassé de 5,61 USD : **c'est un écart au GO-2026-11-21-68 et un nœud de Lazar. Aucune ligne de Google ne part sur ce chiffre sans son mot, ou sans un levier qui le ramène sous 84,06 (section 10).** » »

Avant :

````text
Le chiffre accepté est dépassé de 5,61 USD : c'est à lui dire.
````

Après :

````text
Le chiffre accepté est dépassé de 5,61 USD : **c'est un écart au GO-2026-11-21-68 et un nœud de Lazar. Aucune ligne de Google ne part sur ce chiffre sans son mot, ou sans un levier qui le ramène sous 84,06 (section 10).**
````

**C-04 — section 0, point 2 (régime du chiffre).**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Le nœud du pire cas est donc tranché par cette décision : écris-le comme tranché, avec sa référence. »

Avant :

````text
2. **Pire cas chez Google : 89,67 USD, sans borne dure.
````

Après :

````text
2. **Pire cas chez Google : 89,67 USD au régime courant, sans borne dure.
````

**C-05 — section 0, point 2 (nœud tranché).**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Le nœud du pire cas est donc tranché par cette décision : écris-le comme tranché, avec sa référence. »
- Vérification, section 2, levier (a) : « | (a) **régime prudent imposé à la file** | »
- Vérification, section 7, décision 1, option (B) : « (B) régime prudent imposé à la file : 32,97 USD, égal à ce que couvrent déjà les seuils de crédit. »

Avant :

````text
Au régime prudent, ou si la supposition de la sonde tient : 32,97 USD au lieu de 23,44 (C).
````

Après :

````text
Au régime prudent, ou si la supposition de la sonde tient : 32,97 USD au lieu de 23,44 (C). **Le nœud est tranché** : la mère, sous GO-2026-11-21-69 (R-4682 ; journal, entrée OD-315), a retenu le levier (a) de la vérification (option (B) de sa décision 1) : « régime prudent pour les lignes de Google, en vérification comme en file » ; **le pire cas chez Google est de 32,97 USD**, sous les 84,06 acceptés (C, section 12.2).
````

**C-06 — section 0, point 4 (versement de GO-2026-11-21-74).**

Sources :
- Vérification, correction 3 : « Section 0, point 4 et section 10, point 2 : ajouter la même phrase sur les 9,18 € par projet. »
- Vérification, correction 3 : « Section 8, geste de paiement. Remplacer « Il manque 19,65 € au projet à 11,93 € et 15,99 € au projet à 15,59 €. » par : « Chaque projet doit montrer au moins 31,58 € à la pièce de constat. Aux soldes du 21 novembre (11,93 € et 15,59 €), il manque 19,65 € et 15,99 € ; après le versement accordé sous GO-2026-11-21-74 (10,47 € et 6,81 €), il manque 9,18 € sur chacun. » »

Avant :

````text
soit 35,64 € en tout. Au plus juste : 27,11 € par projet,
````

Après :

````text
soit 35,64 € en tout. Après le versement accordé sous GO-2026-11-21-74 (10,47 € et 6,81 €), il manque 9,18 € sur chacun. Au plus juste : 27,11 € par projet,
````

**C-07 — section 0, point 5 (borne : les pages).**

Sources :
- Mandat de la session mère : « la borne de réflexion fondée sur les pages de `docs/sources/google-gemini-reflexion-v1/`, ou marquée « supposée ». »
- Journal, OD-315 : « la mère fonde la borne de réflexion sur des pages de Google versées sur main sous `docs/sources/google-gemini-reflexion-v1/` »

Avant :

````text
5. **La borne de réflexion à déclarer est 49 536 jetons, et elle ne se justifie pas sans relevé** (section 4).
````

Après :

````text
5. **La borne de réflexion à déclarer est 49 536 jetons, et elle ne se justifie pas sans relevé ; les pages de Google versées ne la fondent pas : elle reste supposée** (section 4).
````

**C-08 — section 0, point 5 (aucune pièce).**

Sources :
- Mandat de la session mère : « la borne de réflexion fondée sur les pages de `docs/sources/google-gemini-reflexion-v1/`, ou marquée « supposée ». »
- Journal, OD-315 : « la mère fonde la borne de réflexion sur des pages de Google versées sur main sous `docs/sources/google-gemini-reflexion-v1/` »

Avant :

````text
Aucune pièce lue ne borne la réflexion du niveau le plus haut.
````

Après :

````text
Aucune pièce lue ne borne la réflexion du niveau le plus haut, pas même ces pages.
````

**C-09 — section 0, point 5 (borne démentie).**

Sources :
- Vérification, correction 2 : « Textes des lignes 2 et 4. Après « supposée et non relevée », insérer : « , éprouvée après chaque réponse : une réflexion facturée au-delà est un défaut, qui arrête la file sans qu'elle tienne, et rend une vérification non saine (nœud de Lazar) ». »

Avant :

````text
ce qui protège, ce sont les contrôles d'après la réponse.
````

Après :

````text
ce qui protège, ce sont les contrôles d'après la réponse : une réflexion facturée au-delà de la borne est un défaut, qui arrête la file sans qu'elle tienne, et rend une vérification non saine (nœud de Lazar).
````

**C-10 — section 0, point 9.**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Le nœud du pire cas est donc tranché par cette décision : écris-le comme tranché, avec sa référence. »

Avant :

````text
9. **À dire à Lazar** (section 10) : le pire cas dépassé ; le versement ;
````

Après :

````text
9. **À dire à Lazar** (section 10) : le pire cas dépassé, et le nœud tranché par la mère (journal, entrée OD-315) ; le versement ;
````

**C-11 — section 1.4, fin (chiffre accepté).**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Le nœud du pire cas est donc tranché par cette décision : écris-le comme tranché, avec sa référence. »

Avant :

````text
le chiffre accepté, 84,06, reste ce qu'il est ; il est dépassé.
````

Après :

````text
le chiffre accepté, 84,06, reste ce qu'il est ; il est dépassé au régime courant. **Sous la décision de la mère (GO-2026-11-21-69, R-4682 ; journal, entrée OD-315), le régime prudent vaut pour les lignes de Google, en vérification comme en file : le pire cas chez Google est de 32,97 USD, sous ce chiffre. Les 80,29, 84,98, 89,67, 152,92 et 167,64 USD de ces tableaux et de ces listes sont ceux du régime courant, que la décision écarte.**
````

**C-12 — section 2, tableau (file, neuf excès).**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Le nœud du pire cas est donc tranché par cette décision : écris-le comme tranché, avec sa référence. »

Avant :

````text
| file, neuf excès, si la supposition de la sonde manque | 76,70 |
````

Après :

````text
| file, neuf excès, si la supposition de la sonde manque, au régime courant (écarté par la mère, OD-315) | 76,70 |
````

**C-13 — section 2, tableau (pire cas au régime prudent).**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Le nœud du pire cas est donc tranché par cette décision : écris-le comme tranché, avec sa référence. »

Avant :

````text
| Google, deux vérifications, régime prudent ou supposition tenue | 23,44 | **32,97** |
````

Après :

````text
| **Google, deux vérifications, au régime prudent retenu par la mère (GO-2026-11-21-69, R-4682 ; journal, OD-315) : pire cas** | 23,44 | **32,97** |
````

**C-14 — section 2, tableau (régime courant).**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Le nœud du pire cas est donc tranché par cette décision : écris-le comme tranché, avec sa référence. »

Avant :

````text
| **Google, deux vérifications, pire cas sans borne dure** | 84,06 | **89,67** |
````

Après :

````text
| Google, deux vérifications, au régime courant (écarté par la mère, OD-315), neuf excès, sans borne dure | 84,06 | 89,67 |
````

**C-15 — section 2.4, fait neuf (choix pris).**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Le nœud du pire cas est donc tranché par cette décision : écris-le comme tranché, avec sa référence. »

Avant :

````text
C'est un choix de règle, non un chiffre : il n'est pas pris ici.
````

Après :

````text
C'est un choix de règle, non un chiffre : il n'est pas pris ici. **Il est pris par la mère** : sous GO-2026-11-21-69 (R-4682 ; journal, entrée OD-315), « régime prudent pour les lignes de Google, en vérification comme en file » ; le pire cas chez Google est de 32,97 USD (C, section 12.2).
````

**C-16 — section 3.1, dépense retirée.**

Sources :
- Vérification, correction 4 : « Section 3.1, troisième point. Remplacer « tant que cette pièce ne porte pas `oui` à `google_deux_projets_distincts` » par : « sauf si la pièce porte `oui` à `google_deux_projets_distincts` **et** constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` (livraison 5, C-1). Sous le constat que GO-2026-11-21-68 permet, ces deux clés sont levées, et la somme est toujours retirée ». Même changement à la ligne `google_deux_projets_distincts` du tableau de la section 9. »

Avant :

````text
tant que cette pièce ne porte pas `oui` à `google_deux_projets_distincts`. La mère garde la somme
````

Après :

````text
sauf si la pièce porte `oui` à `google_deux_projets_distincts` **et** constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` (livraison 5, C-1). Sous le constat que GO-2026-11-21-68 permet, ces deux clés sont levées, et la somme est toujours retirée. La mère garde la somme
````

**C-17 — section 3.2, tableau (après le versement).**

Sources :
- Vérification, correction 3 : « Section 3.3. Après le paragraphe « **Le manque dépend du taux** », ajouter : « **Le versement déjà accordé.** Lazar a accordé sous GO-2026-11-21-74 le versement de 10,47 € et de 6,81 € (17,28 €), chiffré par le journal (OD-301) pour le plafond de 32 768. S'il est fait, chaque projet montre 22,40 €. Il en faut 31,58 : il reste **9,18 € à verser sur chaque projet, 18,36 € en tout**, ce qui demande un mot de paiement de plus. Même à 32 768, 22,40 € ne comptaient que 23,38 USD, sous les 23,44 exigés au pire. Les soldes qui comptent sont ceux de la pièce de constat neuve qui suivra le versement. » »
- Mandat de la session mère : « Recalcule par programme, calcul montré, tout chiffre que ces corrections touchent : plafonds, excès, pire cas, seuils par projet, manque en euros après le versement de GO-74. »

Avant :

````text
| projet à 15,59 € | 15,59 € | 16,27 USD | non | non | non |
````

Après :

````text
| projet à 15,59 € | 15,59 € | 16,27 USD | non | non | non |
| chacun des deux, après le versement accordé sous GO-2026-11-21-74 (10,47 € et 6,81 €), s'il est fait | 22,40 € | 23,38 USD | non | non | oui |
````

**C-18 — section 3.3, tableau (manque après le versement).**

Sources :
- Vérification, correction 3 : « Section 3.3. Après le paragraphe « **Le manque dépend du taux** », ajouter : « **Le versement déjà accordé.** Lazar a accordé sous GO-2026-11-21-74 le versement de 10,47 € et de 6,81 € (17,28 €), chiffré par le journal (OD-301) pour le plafond de 32 768. S'il est fait, chaque projet montre 22,40 €. Il en faut 31,58 : il reste **9,18 € à verser sur chaque projet, 18,36 € en tout**, ce qui demande un mot de paiement de plus. Même à 32 768, 22,40 € ne comptaient que 23,38 USD, sous les 23,44 exigés au pire. Les soldes qui comptent sont ceux de la pièce de constat neuve qui suivra le versement. » »
- Mandat de la session mère : « Recalcule par programme, calcul montré, tout chiffre que ces corrections touchent : plafonds, excès, pire cas, seuils par projet, manque en euros après le versement de GO-74. »

Avant :

````text
| avant la ligne | seuil | dépense retirée | crédit compté à avoir | solde à voir, par projet | manque au projet à 11,93 € | manque au projet à 15,59 € |
|---|---|---|---|---|---|---|
| vérification de la clé 1 (ligne 2), première ligne de Google | 28,28 | 0 | 28,28 USD | **27,09 €** | **15,16 €** | **11,50 €** |
| vérification de la clé 2 (ligne 6), la première au pire | 28,28 | 4,69 | 32,97 USD | **31,58 €** | **19,65 €** | **15,99 €** |
| la même, la première à son attendu | 28,28 | 0,02 | 28,30 USD | 27,11 € | 15,18 € | 11,52 € |
| file du juge (ligne 4), les deux vérifications au pire | 23,59 | 9,38 | 32,97 USD | **31,58 €** | **19,65 €** | **15,99 €** |
| la même, les deux à leur attendu | 23,59 | 0,04 | 23,63 USD | 22,64 € | 10,71 € | 7,05 € |
````

Après :

````text
| avant la ligne | seuil | dépense retirée | crédit compté à avoir | solde à voir, par projet | manque au projet à 11,93 € | manque au projet à 15,59 € | manque sur chacun, après le versement de GO-2026-11-21-74 (22,40 €) |
|---|---|---|---|---|---|---|---|
| vérification de la clé 1 (ligne 2), première ligne de Google | 28,28 | 0 | 28,28 USD | **27,09 €** | **15,16 €** | **11,50 €** | **4,69 €** |
| vérification de la clé 2 (ligne 6), la première au pire | 28,28 | 4,69 | 32,97 USD | **31,58 €** | **19,65 €** | **15,99 €** | **9,18 €** |
| la même, la première à son attendu | 28,28 | 0,02 | 28,30 USD | 27,11 € | 15,18 € | 11,52 € | 4,71 € |
| file du juge (ligne 4), les deux vérifications au pire | 23,59 | 9,38 | 32,97 USD | **31,58 €** | **19,65 €** | **15,99 €** | **9,18 €** |
| la même, les deux à leur attendu | 23,59 | 0,04 | 23,63 USD | 22,64 € | 10,71 € | 7,05 € | 0,24 € |
````

**C-19 — section 3.3, contrôle du tableau.**

Sources :
- Mandat de la session mère : « Recalcule par programme, calcul montré, tout chiffre que ces corrections touchent : plafonds, excès, pire cas, seuils par projet, manque en euros après le versement de GO-74. »

Avant :

````text
(C. Solde à voir : le crédit compté à avoir, divisé par 1,04405, au centime supérieur ; contrôlé : 31,58 € comptent pour 32,97 USD, 31,57 € pour 32,96.)
````

Après :

````text
(C. Solde à voir : le crédit compté à avoir, divisé par 1,04405, au centime supérieur ; contrôlé : 31,58 € comptent pour 32,97 USD, 31,57 € pour 32,96. Manque après le versement : le solde à voir moins 22,40 €. Les mêmes seuils, éprouvés par la fonction du chef v7 qui décide si une ligne part : section 12.2.)
````

**C-20 — section 3.3, versement déjà accordé.**

Sources :
- Vérification, correction 3 : « Section 3.3. Après le paragraphe « **Le manque dépend du taux** », ajouter : « **Le versement déjà accordé.** Lazar a accordé sous GO-2026-11-21-74 le versement de 10,47 € et de 6,81 € (17,28 €), chiffré par le journal (OD-301) pour le plafond de 32 768. S'il est fait, chaque projet montre 22,40 €. Il en faut 31,58 : il reste **9,18 € à verser sur chaque projet, 18,36 € en tout**, ce qui demande un mot de paiement de plus. Même à 32 768, 22,40 € ne comptaient que 23,38 USD, sous les 23,44 exigés au pire. Les soldes qui comptent sont ceux de la pièce de constat neuve qui suivra le versement. » »
- Journal, OD-315 : « Lazar ne verse rien de plus avant les deux pièces vérifiées. »

Avant :

````text
Formule : solde à voir = (seuil + dépense retirée) ÷ (t × 0,95), au centime supérieur.
````

Après :

````text
Formule : solde à voir = (seuil + dépense retirée) ÷ (t × 0,95), au centime supérieur.
- **Le versement déjà accordé.** Lazar a accordé sous GO-2026-11-21-74 le versement de 10,47 € et de 6,81 € (17,28 €), chiffré par le journal (OD-301) pour le plafond de 32 768. S'il est fait, chaque projet montre 22,40 €. Il en faut 31,58 : il reste **9,18 € à verser sur chaque projet, 18,36 € en tout**, ce qui demande un mot de paiement de plus. Même à 32 768, 22,40 € ne comptaient que 23,38 USD, sous les 23,44 exigés au pire. Les soldes qui comptent sont ceux de la pièce de constat neuve qui suivra le versement.
- **Rien de plus avant les pièces vérifiées.** Selon le journal (entrée OD-315), « Lazar ne verse rien de plus avant les deux pièces vérifiées » : cette version 2 de l'avenant 2, et le brouillon 2 du devis des lectures hors carte.
````

**C-21 — section 4, ce que disent les pages.**

Sources :
- Mandat de la session mère : « la borne de réflexion fondée sur les pages de `docs/sources/google-gemini-reflexion-v1/`, ou marquée « supposée ». »
- Journal, OD-315 : « la mère fonde la borne de réflexion sur des pages de Google versées sur main sous `docs/sources/google-gemini-reflexion-v1/` »
- Journal, OD-315 : « la lecture de ce seul sous-dossier (pages publiques de Google) est admise, à déclarer par le rédacteur comme ouverture hors liste autorisée par la mère. »
- Mandat de la session mère : « Une seule exception, autorisée par la session mère (R-4684) : le sous-dossier `docs/sources/google-gemini-reflexion-v1/`, à lire par `git show origin/main:<chemin>` et à déclarer. »
- Vérification, section 3 : « **Pages à verser en PDF empreinté, page citée (R7)**, par un agent de lecture, sans clé ni dépense : `aistudio.google.com/docs/thinking`, `…/docs/whats-new-gemini-4-neon`, `…/docs/models/gemini-4-neon`, `…/api-reference/generate-content`. Quatre choses à y lire : »
- Vérification, section 3 : « si `thinkingBudget` est admis avec Neon, et son maximum : c'est l'option (a) de la confrontation, la seule vérifiable avant l'envoi ; »
- Vérification, section 3 : « Si la pensée est comprise dans le plafond, 65 536 borne tout envoi, mais rien ne réserve 16 000 jetons au texte. »

Avant :

````text
« de 49 à 1 239 jetons, réflexion comprise » (devis, ligne 215). **La borne de 49 536 est donc supposée (S).**
````

Après :

````text
« de 49 à 1 239 jetons, réflexion comprise » (devis, ligne 215). **La borne de 49 536 est donc supposée (S).**

**Ce que disent les pages de Google versées.** La mère a versé sur la branche principale deux pages publiques de Google (`docs/sources/google-gemini-reflexion-v1/`, pièce de provenance `provenance-v1.md`, sha256 `2cc1bdc8d6fc58fc75d9cc530f841ccc84d27b870c77b18e2995767cfbe8aaa9`) : la page « Gemini thinking », variante `generateContent` (`gemini-thinking-generate-content-2026-11-21-v1.md.txt`, sha256 `fe0b8d8820b2ab7b8079bf1477e7871f850f6f5450f92f6b844866cade105892`), et la référence de `generateContent` (`reference-generate-content-2026-11-21-v1.md.txt`, sha256 `829dabb8cb4b90bcbff71c53197ba8d834fc5dfb136294eaa9a1364a1b39a215`), chacune égale à son compagnon, en texte et non en PDF. Elles sont lues par `git show origin/main:<chemin>`, seule ouverture de `docs/sources/` que la mère permet (journal, entrée OD-315). Les quatre choses que la vérification demande d'y lire (sa section 3, point 2) :
1. **un maximum de jetons de pensée par niveau** : aucun. La page de la réflexion dit de `xhigh` : « Most tokens, deepest reasoning » (ligne 689) ; la référence dit de `thinkingLevel` : « Controls the maximum depth of the model's internal reasoning process before it produces a response. » (ligne 2838), sans nombre ;
2. **si `thinkingBudget` est admis avec Neon, et son maximum** : non. « In Gemini 4 models (`gemini-4-carbon`, `gemini-4-argon`, `gemini-4-neon`, and `gemini-4-hydrogen`), `thinkingBudget` (`thinking_budget`) is deprecated. » ; seul, il se ramène au niveau le plus proche, avec un avertissement ; avec `thinkingLevel`, il rend une erreur 400 (page de la réflexion, ligne 939). L'option (a) de la confrontation à la règle, un budget explicite, « la seule vérifiable avant l'envoi » (vérification, section 3), n'est donc pas offerte ;
3. **la limite de sortie du modèle** : « A single request returns up to `65,536` tokens on `gemini-4-neon` and `gemini-4-hydrogen` (streaming and non-streaming) » (ligne 931). Le plafond de la décision est cette limite ;
4. **si `maxOutputTokens` de `generateContent` comprend la pensée** : oui, selon la page, variante `generateContent` : la sortie maximale « sets the maximum number of tokens a response can generate, including thought tokens » (lignes 915 et 916) et agit comme « a hard cutoff enforced by the infrastructure » (ligne 918) ; atteinte pendant la réflexion, la génération finit en `MAX_TOKENS`, la pensée restant facturée (lignes 922 à 924). C'est ce que le devis disait « **non établi pour les deux appels de ce devis.** » (ligne 219) : c'est désormais documenté pour Google, non mesuré.

**La borne de 49 536 ne se fonde donc pas sur ces pages : elle reste supposée (S).** La vérification l'écrit (sa section 3) : « Si la pensée est comprise dans le plafond, 65 536 borne tout envoi, mais rien ne réserve 16 000 jetons au texte. » ; les pages disent que la pensée y est comprise.
````

**C-22 — section 4, ce que vaut la garde.**

Sources :
- Vérification, correction 2 : « Même section. Remplacer « elle n'arrête pas une réflexion plus longue que la borne. » par « elle n'empêche pas une réflexion plus longue que la borne ; le programme la constate après la réponse (C-2) et arrête la ligne. » »

Avant :

````text
elle n'arrête pas une réflexion plus longue que la borne.
````

Après :

````text
elle n'empêche pas une réflexion plus longue que la borne ; le programme la constate après la réponse (C-2) et arrête la ligne.
````

**C-23 — section 4, ce qu'il faut relever, point 1.**

Sources :
- Vérification, m-2 : « m-2. Point 3 de la section 4 : citer les deux relevés de la section 3 ci-dessus, déjà au dépôt. »
- Vérification, section 3 : « **Pièces déjà au dépôt, que l'avenant n'a pas ouvertes** (non opposables, provenance par transcription) : »
- Vérification, section 3 : « **Pages à verser en PDF empreinté, page citée (R7)**, par un agent de lecture, sans clé ni dépense : `aistudio.google.com/docs/thinking`, `…/docs/whats-new-gemini-4-neon`, `…/docs/models/gemini-4-neon`, `…/api-reference/generate-content`. Quatre choses à y lire : »
- Mandat de la session mère : « la borne de réflexion fondée sur les pages de `docs/sources/google-gemini-reflexion-v1/`, ou marquée « supposée ». »

Avant :

````text
1. **Sans dépense, sur pièce** : la page de la documentation de Google sur la réflexion de ce modèle, versée en PDF empreinté, page citée (R7). Quatre choses à y lire : un nombre maximal de jetons de pensée pour le niveau le plus haut, s'il est écrit ; si ce modèle admet un budget de réflexion en jetons, et son maximum ; si `maxOutputTokens` de `generateContent` comprend la pensée, ce que le devis dit « **non établi pour les deux appels de ce devis.** » (ligne 219) ; la sortie maximale du modèle. Le relevé des niveaux de réflexion que cite le devis (`juge-des-ancres-identifiant-gemini-v1.md`) n'est pas dans ma liste : je ne l'ai pas ouvert.
````

Après :

````text
1. **Sans dépense, sur pièce — fait en partie.** Deux des quatre pages que nomme la vérification (sa section 3, point 2) sont versées, en texte et non en PDF : la page de la réflexion et la référence de `generateContent` (ci-dessus) ; `…/docs/whats-new-gemini-4-neon` et `…/docs/models/gemini-4-neon` ne le sont pas. Les quatre choses à y lire ont leur réponse ci-dessus. Deux relevés déjà au dépôt, non opposables (provenance par transcription), sont à citer (vérification, m-2) : `releve-api-mistral-gemini-essais-admission-v1.md` (`291341e2…`), ligne 18 : `maxOutputTokens` « caps combined thinking and output tokens for a response » ; mais « ces phrases visent `max_output_tokens` de l'API Interactions ; pour `generateContent`, confirmation directe non trouvée » ; `juge-des-ancres-identifiant-gemini-v1.md` (`ac8bb15e…`), ligne 15 : quatre niveaux, `xhigh` le plus haut, aucune borne en jetons.
````

**C-24 — section 4, ce qu'il faut relever, point 3 (proposition déjà au programme).**

Sources :
- Vérification, correction 2 : « Section 9, point 8 (« Relevés et rapport »). Remplacer par : « 8. **Relevés et rapport** : déjà au programme (livraison 5, C-2 : `borne_de_reflexion_dementie` à la fiche, `bornes_de_reflexion_dementies` au relevé) ; rien à changer. » »
- Vérification, correction 2 : « Section 4. Remplacer tout le paragraphe qui commence par « **Si un envoi dépasse la borne et finit normalement** » par : « **Si un envoi dépasse la borne** — plus de 49 536 jetons de pensée facturés —, le programme de la livraison 5 en fait un défaut (C-2, `borne_dementie`). Dans la file : défaut journalisé, l'envoi n'est ni jugé ni compté parmi les réponses, la file s'arrête et ne tient pas. À une vérification : ligne 13 du classement, non saine, nœud de Lazar. À la sonde : une mesure. La borne est donc une déclaration éprouvée après chaque réponse. Son prix est qu'un juge qui réfléchit plus longtemps échoue pour un chiffre de configuration : c'est pourquoi elle est déclarée à la plus haute valeur admise. » »

Avant :

````text
À ajouter, par ligne : le plus grand compte de pensée, et « borne de réflexion déclarée dépassée, oui ou non ». Et l'issue des deux sondes.
````

Après :

````text
Le plus grand compte de pensée et « borne de réflexion déclarée dépassée, oui ou non » : déjà au programme (livraison 5, C-2 : `borne_de_reflexion_dementie` à la fiche, `bornes_de_reflexion_dementies` au relevé) ; rien à changer. Et l'issue des deux sondes.
````

**C-25 — section 4, ce que le relevé permettrait.**

Sources :
- Mandat de la session mère : « la borne de réflexion fondée sur les pages de `docs/sources/google-gemini-reflexion-v1/`, ou marquée « supposée ». »
- Journal, OD-315 : « la mère fonde la borne de réflexion sur des pages de Google versées sur main sous `docs/sources/google-gemini-reflexion-v1/` »

Avant :

````text
la justifier demanderait un plafond plus haut ou un budget explicite, et c'est une autre décision.
````

Après :

````text
la justifier demanderait un plafond plus haut ou un budget explicite, et c'est une autre décision. Les pages versées n'en donnent aucun, et la page de la réflexion déprécie le budget chez Neon (ligne 939) : la borne reste supposée.
````

**C-26 — section 4, borne démentie.**

Sources :
- Vérification, correction 2 : « Section 4. Remplacer tout le paragraphe qui commence par « **Si un envoi dépasse la borne et finit normalement** » par : « **Si un envoi dépasse la borne** — plus de 49 536 jetons de pensée facturés —, le programme de la livraison 5 en fait un défaut (C-2, `borne_dementie`). Dans la file : défaut journalisé, l'envoi n'est ni jugé ni compté parmi les réponses, la file s'arrête et ne tient pas. À une vérification : ligne 13 du classement, non saine, nœud de Lazar. À la sonde : une mesure. La borne est donc une déclaration éprouvée après chaque réponse. Son prix est qu'un juge qui réfléchit plus longtemps échoue pour un chiffre de configuration : c'est pourquoi elle est déclarée à la plus haute valeur admise. » »

Avant :

````text
**Si un envoi dépasse la borne et finit normalement** — plus de 49 536 jetons de pensée, texte entier, fin `STOP` —, la règle n'en fait pas un défaut, et je n'en ajoute pas : la lecture vaut. Mais la supposition est démentie. Je propose que le rapport le dise, et que la borne de la course soit refaite sur le plus grand compte observé, par un nœud.
````

Après :

````text
**Si un envoi dépasse la borne** — plus de 49 536 jetons de pensée facturés —, le programme de la livraison 5 en fait un défaut (C-2, `borne_dementie`). Dans la file : défaut journalisé, l'envoi n'est ni jugé ni compté parmi les réponses, la file s'arrête et ne tient pas. À une vérification : ligne 13 du classement, non saine, nœud de Lazar. À la sonde : une mesure. La borne est donc une déclaration éprouvée après chaque réponse. Son prix est qu'un juge qui réfléchit plus longtemps échoue pour un chiffre de configuration : c'est pourquoi elle est déclarée à la plus haute valeur admise.
````

**C-27 — section 5, ce qui change, point 2.**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Recalcule par programme, calcul montré, tout chiffre que ces corrections touchent : plafonds, excès, pire cas, seuils par projet, manque en euros après le versement de GO-74. »

Avant :

````text
deux envois comptés à leur réserve au régime courant (0,999 ou 1,056 USD chacun)
````

Après :

````text
deux envois comptés au régime prudent que la mère a retenu (journal, entrée OD-315), 8,09 ou 8,15 USD chacun, si le compteur laisse partir la reprise (2.4)
````

**C-28 — section 5, délai relevé.**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Recalcule par programme, calcul montré, tout chiffre que ces corrections touchent : plafonds, excès, pire cas, seuils par projet, manque en euros après le versement de GO-74. »

Avant :

````text
le pire cas chez Google, de 89,67 à 162,57
````

Après :

````text
le pire cas chez Google, au régime prudent que la mère a retenu (OD-315), de 32,97 à 41,07 (au régime courant, de 89,67 à 162,57)
````

**C-29 — section 7, forme proposée (ligne de taux sans code neuf).**

Sources :
- Vérification, correction 6 : « À la fin de « Forme proposée » (section 7), ajouter : « Le chef v4 ne lit que « - taux : T USD par EUR ; source : … ; heure du taux (UTC) : … » (`MOTIF_TAUX`). Sans code neuf, la pièce de constat écrit : « - taux : 1.0990 USD par EUR ; source : Banque centrale européenne, fixage du 2026-11-20, fichier a234540a78d0bccccc3642bfe604b138310a03741361434907aa4cf3e7622e8a ; heure du taux (UTC) : 2026-11-21T17:49Z ». L'heure du taux y est l'heure du relevé, que bornent les contrôles de la livraison 5 (m-5). Les contrôles 2 et 4 sont alors faits par le vérificateur de la pièce, non par le programme ; les coder est une livraison de plus. » »

Avant :

````text
4. le jour du fixage est au plus cinq jours avant le jour du relevé, jamais après lui.
````

Après :

````text
4. le jour du fixage est au plus cinq jours avant le jour du relevé, jamais après lui.

Le chef v4 ne lit que « - taux : T USD par EUR ; source : … ; heure du taux (UTC) : … » (`MOTIF_TAUX`). Sans code neuf, la pièce de constat écrit : « - taux : 1.0990 USD par EUR ; source : Banque centrale européenne, fixage du 2026-11-20, fichier a234540a78d0bccccc3642bfe604b138310a03741361434907aa4cf3e7622e8a ; heure du taux (UTC) : 2026-11-21T17:49Z ». L'heure du taux y est l'heure du relevé, que bornent les contrôles de la livraison 5 (m-5). Les contrôles 2 et 4 sont alors faits par le vérificateur de la pièce, non par le programme ; les coder est une livraison de plus.
````

**C-30 — section 7, ce que cette forme suppose.**

Sources :
- Vérification, m-3 : « m-3. La règle des cinq jours (section 7, contrôle 4) est une supposition sur le calendrier de la Banque centrale européenne : à relever avec la page de ce calendrier, ou à retirer si le contrôle n'est pas codé. »

Avant :

````text
Le contrôle 4 ne sert qu'à refuser un fichier périmé.
````

Après :

````text
Le contrôle 4 ne sert qu'à refuser un fichier périmé. **La règle des cinq jours est à relever avec la page de ce calendrier, ou à retirer si le contrôle n'est pas codé** (vérification, m-3).
````

**C-31 — section 8, introduction.**

Sources :
- Mandat de la session mère : « Le texte neuf des lignes de calcul de Google doit être citable tel quel, à la forme de la garde 8 (note v6, section 6 (c) : `note-programme-essais-admission-bras-a-v6.md`). Chaque ligne cite les empreintes du devis, de sa vérification et de l'avenant 1 v3. »
- Vérification, section 5 : « **Le texte des lignes n'est pas citable tel quel.** »

Avant :

````text
Aucun crochet n'y reste ouvert : l'avenant 1 en laissait un pour la valeur d'une recharge, qui n'est plus comptée.
````

Après :

````text
Aucun crochet n'y reste ouvert : l'avenant 1 en laissait un pour la valeur d'une recharge, qui n'est plus comptée. Chaque texte est entier, cite les empreintes du devis, de sa vérification et de l'avenant 1, version 3, et porte les marques de sa ligne au gabarit (`marques_du_perimetre`) : placé tel quel au périmètre de sa ligne du registre, il passe la garde 8 du chef v7 (forme ci-dessous ; épreuve par programme, section 12.2).
````

**C-32 — section 8, ligne 2 (empreintes).**

Sources :
- Mandat de la session mère : « Le texte neuf des lignes de calcul de Google doit être citable tel quel, à la forme de la garde 8 (note v6, section 6 (c) : `note-programme-essais-admission-bras-a-v6.md`). Chaque ligne cite les empreintes du devis, de sa vérification et de l'avenant 1 v3. »

Avant :

````text
**Ligne 2. Vérification de la clé 1 de Google** : bras A, vérification de la clé de `gemini-4-neon` lue sous `GEMINI_API_KEY`, trois appels au plus, soit trois envois au plus, sonde de borne et seconde orthographe du niveau de réflexion comprises, délai de 900 secondes par appel ; sortie maximale envoyée de 65 536 jetons aux appels A et A′
````

Après :

````text
**Ligne 2. Vérification de la clé 1 de Google** : bras A, vérification de la clé de `gemini-4-neon` lue sous `GEMINI_API_KEY`, trois appels au plus, soit trois envois au plus, sonde de borne et seconde orthographe du niveau de réflexion comprises, délai de 900 secondes par appel ; devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc, vérification du devis 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca, avenant 1 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac ; sortie maximale envoyée de 65 536 jetons aux appels A et A′
````

**C-33 — section 8, ligne 2 (borne démentie).**

Sources :
- Vérification, correction 2 : « Textes des lignes 2 et 4. Après « supposée et non relevée », insérer : « , éprouvée après chaque réponse : une réflexion facturée au-delà est un défaut, qui arrête la file sans qu'elle tienne, et rend une vérification non saine (nœud de Lazar) ». »

Avant :

````text
49 536 jetons, supposée et non relevée ; sonde de borne à 256 jetons
````

Après :

````text
49 536 jetons, supposée et non relevée, éprouvée après chaque réponse : une réflexion facturée au-delà est un défaut, qui arrête la file sans qu'elle tienne, et rend une vérification non saine (nœud de Lazar) ; sonde de borne à 256 jetons
````

**C-34 — section 8, ligne 2 (dépense retirée).**

Sources :
- Vérification, correction 4 : « Section 3.1, troisième point. Remplacer « tant que cette pièce ne porte pas `oui` à `google_deux_projets_distincts` » par : « sauf si la pièce porte `oui` à `google_deux_projets_distincts` **et** constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` (livraison 5, C-1). Sous le constat que GO-2026-11-21-68 permet, ces deux clés sont levées, et la somme est toujours retirée ». Même changement à la ligne `google_deux_projets_distincts` du tableau de la section 9. »
- Vérification, section 5 : « Il lit la dépense retirée selon la règle de la livraison 4 (correction 4). »

Avant :

````text
moins la dépense retirée de l'avenant 1 (4.4, point 4), atteint 28,28 USD
````

Après :

````text
moins la dépense retirée de la section 3.1 de l'avenant 2 — la somme des dépenses comptées sous les deux clés depuis la pièce de constat, sauf si la pièce porte `oui` à `google_deux_projets_distincts` et constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` —, atteint 28,28 USD
````

**C-35 — section 8, ligne 6 (écrite entière).**

Sources :
- Mandat de la session mère : « Le texte neuf des lignes de calcul de Google doit être citable tel quel, à la forme de la garde 8 (note v6, section 6 (c) : `note-programme-essais-admission-bras-a-v6.md`). Chaque ligne cite les empreintes du devis, de sa vérification et de l'avenant 1 v3. »
- Vérification, section 5 : « **Le texte des lignes n'est pas citable tel quel.** »
- Vérification, correction 2 : « Textes des lignes 2 et 4. Après « supposée et non relevée », insérer : « , éprouvée après chaque réponse : une réflexion facturée au-delà est un défaut, qui arrête la file sans qu'elle tienne, et rend une vérification non saine (nœud de Lazar) ». »
- Vérification, correction 4 : « Section 3.1, troisième point. Remplacer « tant que cette pièce ne porte pas `oui` à `google_deux_projets_distincts` » par : « sauf si la pièce porte `oui` à `google_deux_projets_distincts` **et** constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` (livraison 5, C-1). Sous le constat que GO-2026-11-21-68 permet, ces deux clés sont levées, et la somme est toujours retirée ». Même changement à la ligne `google_deux_projets_distincts` du tableau de la section 9. »

Avant :

````text
**Ligne 6. Vérification de la clé 2 de Google** : même texte que la ligne 2, sous `GEMINI_API_KEY_2`, plafond 3,00 USD, excès possible d'un seul envoi de 1,69 USD.
````

Après :

````text
**Ligne 6. Vérification de la clé 2 de Google** : bras A, vérification de la clé de `gemini-4-neon` lue sous `GEMINI_API_KEY_2`, trois appels au plus, soit trois envois au plus, sonde de borne et seconde orthographe du niveau de réflexion comprises, délai de 900 secondes par appel ; devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc, vérification du devis 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca, avenant 1 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac ; sortie maximale envoyée de 65 536 jetons aux appels A et A′, au niveau de réflexion le plus haut, sous une borne de réflexion déclarée de 49 536 jetons, supposée et non relevée, éprouvée après chaque réponse : une réflexion facturée au-delà est un défaut, qui arrête la file sans qu'elle tienne, et rend une vérification non saine (nœud de Lazar) ; sonde de borne à 256 jetons, exemptée du contrôle d'avant l'envoi « plafond de sortie au moins égal à la réflexion plus 16 000 jetons de texte », dans les termes de la section 6 de l'avenant 2, à réglage de réflexion explicite et sans lecture jugée (décision de la session mère sous GO-2026-11-21-69, en application de la règle de GO-2026-11-21-71) ; plafond 3,00 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 1,69 USD au débit déclaré de 200 jetons par seconde, tout envoi sans compteur lisible étant compté à ce débit sur sa durée, ce qui arrête la ligne au premier délai, sous la supposition, non documentée, que la coupure arrête la génération et la facturation, compté à 3 et 15 USD par million, payé sur le crédit prépayé du projet de cette clé, dont la recharge automatique reste activée et qui n'a aucun plafond de dépense, par décision de Lazar (GO-2026-11-21-68) : le solde ne borne pas la perte ; elle n'est bornée que par le compteur, à 4,69 USD sous les suppositions dites, et par rien de dur au-delà ; conditions d'envoi : offre payante vue sur capture ; partage et durée des journaux, et lien entre la clé et son projet, non constatés, levés par le même GO ; avant la ligne, le solde vu de chacun des deux projets, en euros, converti au dernier fixage publié de la Banque centrale européenne diminué de 5 %, sans compter la recharge automatique (GO-2026-11-21-69), moins la dépense retirée de la section 3.1 de l'avenant 2 — la somme des dépenses comptées sous les deux clés depuis la pièce de constat, sauf si la pièce porte `oui` à `google_deux_projets_distincts` et constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` —, atteint 28,28 USD ; une ligne nouvelle de vérification, sur l'une ou l'autre clé, ajoute 4,69 USD au pire cas et exige de nouveau 28,28 USD, lus de même.
````

**C-36 — section 8, ligne 4 (empreintes).**

Sources :
- Mandat de la session mère : « Le texte neuf des lignes de calcul de Google doit être citable tel quel, à la forme de la garde 8 (note v6, section 6 (c) : `note-programme-essais-admission-bras-a-v6.md`). Chaque ligne cite les empreintes du devis, de sa vérification et de l'avenant 1 v3. »

Avant :

````text
la reprise sur la clé de son appel ; une seule file, un seul compteur ; sortie maximale envoyée de 65 536 jetons
````

Après :

````text
la reprise sur la clé de son appel ; une seule file, un seul compteur ; devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc, vérification du devis 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca, avenant 1 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac ; sortie maximale envoyée de 65 536 jetons
````

**C-37 — section 8, ligne 4 (borne démentie).**

Sources :
- Vérification, correction 2 : « Textes des lignes 2 et 4. Après « supposée et non relevée », insérer : « , éprouvée après chaque réponse : une réflexion facturée au-delà est un défaut, qui arrête la file sans qu'elle tienne, et rend une vérification non saine (nœud de Lazar) ». »

Avant :

````text
49 536 jetons, supposée et non relevée (décision de la session mère
````

Après :

````text
49 536 jetons, supposée et non relevée, éprouvée après chaque réponse : une réflexion facturée au-delà est un défaut, qui arrête la file sans qu'elle tienne, et rend une vérification non saine (nœud de Lazar) (décision de la session mère
````

**C-38 — section 8, ligne 4 (régime prudent, toujours).**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Vérification, correction 1 : « sous le levier (a) : « la file est comptée au régime prudent, quelle que soit l'issue des sondes ; pire cas chez Google, pour les lignes 2, 4 et 6 telles qu'accordées, 32,97 USD, sous le chiffre accepté (GO-2026-11-21-68) ; ». »

Avant :

````text
par seconde : quand la file part sur un mot de Lazar, au régime prudent, où un envoi coupé
````

Après :

````text
par seconde : au régime prudent, où un envoi coupé
````

**C-39 — section 8, ligne 4 (reprise).**

Sources :
- Vérification, m-1 : « m-1. Le texte de la ligne 4 dit « sa reprise part si le cumul compté avant lui ne passe pas 7,30 USD ». C'est une condition suffisante (7,41 pour un envoi d'appariement) : écrire « au plus 7,30 USD (7,41 pour un envoi d'appariement) ». »

Avant :

````text
où sa reprise part si le cumul compté avant lui ne passe pas 7,30 USD,
````

Après :

````text
où sa reprise part si le cumul compté avant lui vaut au plus 7,30 USD (7,41 pour un envoi d'appariement),
````

**C-40 — section 8, ligne 4 (régime courant retiré).**

Sources :
- Vérification, correction 1 : « Retirer alors de la même ligne : « et, quand elle part après deux sondes « comprises », sous la supposition que la borne se comporte à 65 536 comme à 256, faute de quoi jusqu'à neuf envois peuvent porter un excès (jusqu'à 80,29 USD pour la file au débit déclaré, plafond compté compris), que rien de dur ne borne, ». »

Avant :

````text
arrête la file ; et, quand elle part après deux sondes « comprises », sous la supposition que la borne se comporte à 65 536 comme à 256, faute de quoi jusqu'à neuf envois peuvent porter un excès (jusqu'à 80,29 USD pour la file au débit déclaré, plafond compté compris), que rien de dur ne borne, la recharge automatique
````

Après :

````text
arrête la file ; la recharge automatique
````

**C-41 — section 8, ligne 4 (pire cas).**

Sources :
- Vérification, correction 1 : « sous le levier (a) : « la file est comptée au régime prudent, quelle que soit l'issue des sondes ; pire cas chez Google, pour les lignes 2, 4 et 6 telles qu'accordées, 32,97 USD, sous le chiffre accepté (GO-2026-11-21-68) ; ». »
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Le nœud du pire cas est donc tranché par cette décision : écris-le comme tranché, avec sa référence. »

Avant :

````text
pire cas chez Google, pour les lignes 2, 4 et 6 telles qu'accordées, 89,67 USD ; les 84,06 USD acceptés sous ce GO sont dépassés de 5,61 USD ;
````

Après :

````text
la file est comptée au régime prudent, quelle que soit l'issue des sondes (décision de la session mère sous GO-2026-11-21-69, R-4682) ; pire cas chez Google, pour les lignes 2, 4 et 6 telles qu'accordées, 32,97 USD, sous le chiffre accepté (GO-2026-11-21-68) ;
````

**C-42 — section 8, ligne 4 (dépense retirée).**

Sources :
- Vérification, correction 4 : « Section 3.1, troisième point. Remplacer « tant que cette pièce ne porte pas `oui` à `google_deux_projets_distincts` » par : « sauf si la pièce porte `oui` à `google_deux_projets_distincts` **et** constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` (livraison 5, C-1). Sous le constat que GO-2026-11-21-68 permet, ces deux clés sont levées, et la somme est toujours retirée ». Même changement à la ligne `google_deux_projets_distincts` du tableau de la section 9. »
- Vérification, section 5 : « Il lit la dépense retirée selon la règle de la livraison 4 (correction 4). »

Avant :

````text
moins la dépense retirée de l'avenant 1 (4.4, point 4), atteint 23,59 USD.
````

Après :

````text
moins la dépense retirée de la section 3.1 de l'avenant 2, lue comme à la ligne 2, atteint 23,59 USD.
````

**C-43 — section 8, lignes du registre (forme de la garde 8).**

Sources :
- Mandat de la session mère : « Le texte neuf des lignes de calcul de Google doit être citable tel quel, à la forme de la garde 8 (note v6, section 6 (c) : `note-programme-essais-admission-bras-a-v6.md`). Chaque ligne cite les empreintes du devis, de sa vérification et de l'avenant 1 v3. »

Avant :

````text
**Sommes des six lignes** (C) :
````

Après :

````text
**Lignes du registre, à la forme que lit la garde 8** (note de la livraison 7, `note-programme-essais-admission-bras-a-v6.md`, sha256 `5a6a41f5e3d0c5183e542a87c70b90a7cef853dfd44f1f7561f988dffbcc9aa8`, section 6 (c)) : huit cellules séparées par « ` | ` » ; le périmètre est le texte de la ligne, tel quel ; le plafond, à la lettre de `plafond_registre` ; `type` « calcul », `par` « Lazar ».

```
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | <texte de la ligne 2, tel quel> | 3,00 USD | AAAA-MM-JJ | Lazar | <référence> |
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | <texte de la ligne 6, tel quel> | 3,00 USD | AAAA-MM-JJ | Lazar | <référence> |
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | <texte de la ligne 4, tel quel> | 16,50 USD | AAAA-MM-JJ | Lazar | <référence> |
```

**Sommes des six lignes** (C) :
````

**C-44 — section 8, geste de paiement.**

Sources :
- Vérification, correction 3 : « Section 8, geste de paiement. Remplacer « Il manque 19,65 € au projet à 11,93 € et 15,99 € au projet à 15,59 €. » par : « Chaque projet doit montrer au moins 31,58 € à la pièce de constat. Aux soldes du 21 novembre (11,93 € et 15,59 €), il manque 19,65 € et 15,99 € ; après le versement accordé sous GO-2026-11-21-74 (10,47 € et 6,81 €), il manque 9,18 € sur chacun. » »

Avant :

````text
Il manque 19,65 € au projet à 11,93 € et 15,99 € au projet à 15,59 €.
````

Après :

````text
Chaque projet doit montrer au moins 31,58 € à la pièce de constat. Aux soldes du 21 novembre (11,93 € et 15,59 €), il manque 19,65 € et 15,99 € ; après le versement accordé sous GO-2026-11-21-74 (10,47 € et 6,81 €), il manque 9,18 € sur chacun.
````

**C-45 — section 9, tableau (trois lignes remplacées : relais et réserve).**

Sources :
- Vérification, correction 5 : « Remplacer, dans le tableau de la section 9, les lignes « plafonds des six lignes », « seuils de crédit de Google », « relais de Google, `--borne-reflexion` », « relais de Google, `--plafond-exempte` » et « réserve de sortie » par : »

Avant :

````text
| `exemption_de_la_sonde_go` | `GO-2026-11-21-69` | mandat | voir section 10, point 3 |
| relais de Google, `--borne-reflexion` | `49536`, aux quatre relais | section 4 | à passer au lancement |
| relais de Google, `--plafond-exempte` | présent aux relais des deux vérifications ; absent aux deux relais de la file | section 6 | à passer au lancement |
| réserve de sortie des trois lignes de Google | `65536` jetons par envoi, sonde comprise | section 2.1 | à inscrire si le programme ne la déduit pas |
````

Après :

````text
| `exemption_de_la_sonde_go` | `GO-2026-11-21-69` | mandat | voir section 10, point 3 |
````

**C-46 — section 9, tableau (régime des lignes de Google).**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »

Avant :

````text
| `recharge_comptee` | `false` | mère, GO-2026-11-21-69 ; journal, OD-301 | inchangé depuis la livraison 4 |
````

Après :

````text
| `recharge_comptee` | `false` | mère, GO-2026-11-21-69 ; journal, OD-301 | inchangé depuis la livraison 4 |
| `regime_file_google` | `"prudent"` | mère, GO-2026-11-21-69 (R-4682) ; journal, OD-315 | décidé ; une configuration définitive l'exige (chef v7) |
````

**C-47 — section 9, tableau (deux projets distincts).**

Sources :
- Vérification, correction 4 : « Section 3.1, troisième point. Remplacer « tant que cette pièce ne porte pas `oui` à `google_deux_projets_distincts` » par : « sauf si la pièce porte `oui` à `google_deux_projets_distincts` **et** constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` (livraison 5, C-1). Sous le constat que GO-2026-11-21-68 permet, ces deux clés sont levées, et la somme est toujours retirée ». Même changement à la ligne `google_deux_projets_distincts` du tableau de la section 9. »

Avant :

````text
| `google_deux_projets_distincts`, à la pièce de constat | `non relevé` : la somme des deux dépenses est retirée |
````

Après :

````text
| `google_deux_projets_distincts`, à la pièce de constat | `non relevé` : la somme des deux dépenses est retirée, sauf si la pièce porte `oui` à `google_deux_projets_distincts` **et** constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` (livraison 5, C-1) ; sous le constat que GO-2026-11-21-68 permet, ces deux clés sont levées, et la somme est toujours retirée |
````

**C-48 — section 9, tableau (deux lignes remplacées : plafonds et seuils ; champs du gabarit).**

Sources :
- Vérification, correction 5 : « Remplacer, dans le tableau de la section 9, les lignes « plafonds des six lignes », « seuils de crédit de Google », « relais de Google, `--borne-reflexion` », « relais de Google, `--plafond-exempte` » et « réserve de sortie » par : »

Avant :

````text
| plafonds des six lignes de calcul, à la lettre | `0,25 USD` ; `0,25 USD` ; `3,00 USD` ; `3,00 USD` ; `4,75 USD` ; `16,50 USD` | section 2 | **à changer** : la note porte `1,50 USD` et `8,50 USD` |
| seuils de crédit de Google | `28.28` avant une vérification ; `23.59` avant la file | section 3 | **à changer** : la note porte 19,76 et 16,08 |
| identifiants des six lignes de calcul | à inscrire quand elles sont accordées | — | en attente |
| empreintes citées par les lignes | devis ; sa vérification ; avenant 1 ; cet avenant, une fois accepté | note, section 8 | à compléter |
````

Après :

````text
| identifiants des six lignes de calcul | à inscrire quand elles sont accordées | — | en attente |
| empreintes citées par les lignes | devis ; sa vérification ; avenant 1 ; cet avenant, une fois accepté | note, section 8 | à compléter |

**Champs du gabarit, par la vérification de la version 1 (correction 5).**

| champ | valeur définitive | état |
|---|---|---|
| `fournisseurs.google.sortie_max` | `65536` | décidé |
| `fournisseurs.google.reflexion` | `{"forme": "niveau", "borne_declaree": 49536}` | borne supposée, éprouvée par C-2 |
| `fournisseurs.google.exemption_de_la_sonde` ; `_go` | `true` ; `"GO-2026-11-21-69"` (forme seule contrôlée) | décidé ; à consigner (section 10, point 3) |
| `fournisseurs.google.credit_min_avant_verification_usd` ; `credit_min_avant_file_usd` | `28.28` ; `23.59` | à changer (gabarit : 19.76 et 16.08) |
| `fournisseurs.google.credit_a_avoir_usd` | `32.97`, pour ne pas dire faux | non lu par le chef v4 ; gabarit : 23.0, valeur du schéma de recharge retiré |
| `lignes.verification-google-cle-1` et `-cle-2` : `plafond_usd` ; `plafond_registre` ; `exces_possible_d_un_envoi_usd` | `3.0` ; `"3,00 USD"` ; `1.69` | à changer (1.5 ; « 1,50 USD » ; 2.18) |
| `lignes.file-neon` : `plafond_usd` ; `plafond_registre` ; `exces_possible_d_un_envoi_usd` | `16.5` ; `"16,50 USD"` ; `7.09` | à changer (8.5 ; « 8,50 USD » ; 7.58) |
| `lignes.<ligne de Google>.reserve_sortie_jetons` | `null` ou `65536` (le chef la déduit de `sortie_max`) | rien à inscrire |
| `lignes.file-neon.delais` | inchangé (2 700 et 2 690), ou 2 491 et 2 481 sous le levier (d) | selon la décision 1 |
| arguments `--borne-reflexion` et `--plafond-exempte` | passés par le chef (lignes 3025 à 3027), non à la main | rien à passer |
| `avenant` | la garde 8 n'en lit qu'un : code neuf, un second champ pour l'avenant 2, vérifié sur disque et cité par la ligne du registre | **à coder** |
````

**C-49 — section 9, champs du gabarit (délais de la file : décision 1 tranchée ; ligne de la correction 5, posée au changement précédent).**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Le nœud du pire cas est donc tranché par cette décision : écris-le comme tranché, avec sa référence. »

Avant :

````text
| `lignes.file-neon.delais` | inchangé (2 700 et 2 690), ou 2 491 et 2 481 sous le levier (d) | selon la décision 1 |
````

Après :

````text
| `lignes.file-neon.delais` | inchangé (2 700 et 2 690) | décision 1 tranchée par le levier (a), régime prudent (journal, OD-315) : le levier (d) n'est pas pris |
````

**C-50 — section 9, ce que le programme doit changer, point 2.**

Sources :
- Vérification, correction 5 : « au point 2, citer les champs `credit_min_avant_*_usd` ; »

Avant :

````text
2. **Seuils de crédit** : 28,28 et 23,59 USD, en décimal exact.
````

Après :

````text
2. **Seuils de crédit** (`fournisseurs.google.credit_min_avant_verification_usd` et `fournisseurs.google.credit_min_avant_file_usd`) : 28,28 et 23,59 USD, en décimal exact.
````

**C-51 — section 9, ce que le programme doit changer, point 8.**

Sources :
- Vérification, correction 2 : « Section 9, point 8 (« Relevés et rapport »). Remplacer par : « 8. **Relevés et rapport** : déjà au programme (livraison 5, C-2 : `borne_de_reflexion_dementie` à la fiche, `bornes_de_reflexion_dementies` au relevé) ; rien à changer. » »

Avant :

````text
8. **Relevés et rapport** : par ligne de Google, le plus grand compte de pensée, et « borne de réflexion déclarée dépassée, oui ou non » (proposition de la section 4).
````

Après :

````text
8. **Relevés et rapport** : déjà au programme (livraison 5, C-2 : `borne_de_reflexion_dementie` à la fiche, `bornes_de_reflexion_dementies` au relevé) ; rien à changer.
````

**C-52 — section 9, ce que le programme doit changer, point 9.**

Sources :
- Vérification, correction 5 : « remplacer le point 9 par : « 9. **Limite de mots à la sonde** : déjà tranchée par le programme ; l'exemption couvre les contrôles (2) et (3) pour le corps exact de la sonde (chef v4, lignes 1486 à 1497). » »

Avant :

````text
9. **Exemption de la sonde** : le contrôle de la limite de mots à la sonde, à trancher (section 6).
````

Après :

````text
9. **Limite de mots à la sonde** : déjà tranchée par le programme ; l'exemption couvre les contrôles (2) et (3) pour le corps exact de la sonde (chef v4, lignes 1486 à 1497).
````

**C-53 — section 10, point 1 (régime du chiffre).**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Le nœud du pire cas est donc tranché par cette décision : écris-le comme tranché, avec sa référence. »

Avant :

````text
1. **Le pire cas chez Google passe de 84,06 à 89,67 USD**, sans borne dure.
````

Après :

````text
1. **Le pire cas chez Google passe de 84,06 à 89,67 USD**, au régime courant, sans borne dure.
````

**C-54 — section 10, point 1 (écart et nœud).**

Sources :
- Vérification, correction 1 : « Section 10, point 1. Remplacer « En valeurs exactes, l'écart est de 5,60 USD. » par : « Au grain des lignes, l'écart est de 5,61 USD (5,60 en valeurs exactes). C'est un nœud : décision, enjeu, options et leviers chiffrés à la vérification de cet avenant (`verification-avenant-2-devis-essais-admission-v1.md`, section 2 et décision 1). » »

Avant :

````text
En valeurs exactes, l'écart est de 5,60 USD.
````

Après :

````text
Au grain des lignes, l'écart est de 5,61 USD (5,60 en valeurs exactes). C'est un nœud : décision, enjeu, options et leviers chiffrés à la vérification de cet avenant (`verification-avenant-2-devis-essais-admission-v1.md`, section 2 et décision 1).
````

**C-55 — section 10, point 1 (tranché).**

Sources :
- Journal, OD-315 : « **Mère, sous GO-2026-11-21-69 (R-4682)** : option (a), régime prudent pour les lignes de Google, en vérification comme en file (pire cas 32,97 USD). »
- Mandat de la session mère : « Le nœud du pire cas est donc tranché par cette décision : écris-le comme tranché, avec sa référence. »
- Vérification, section 7, décision 1, option (B) : « (B) régime prudent imposé à la file : 32,97 USD, égal à ce que couvrent déjà les seuils de crédit. »

Avant :

````text
Les deux chiffres supposent 200 jetons par seconde au plus et une coupure qui arrête la facturation.
````

Après :

````text
Les deux chiffres supposent 200 jetons par seconde au plus et une coupure qui arrête la facturation. **Tranché** : la mère, sous GO-2026-11-21-69 (R-4682 ; journal, entrée OD-315), a retenu le levier (a) de la vérification (option (B) de sa décision 1) : « régime prudent pour les lignes de Google, en vérification comme en file » ; pire cas chez Google, 32,97 USD, sous les 84,06 acceptés, sous les mêmes suppositions.
````

**C-56 — section 10, point 2 (versement de GO-2026-11-21-74).**

Sources :
- Vérification, correction 3 : « Section 0, point 4 et section 10, point 2 : ajouter la même phrase sur les 9,18 € par projet. »
- Vérification, correction 3 : « Section 8, geste de paiement. Remplacer « Il manque 19,65 € au projet à 11,93 € et 15,99 € au projet à 15,59 €. » par : « Chaque projet doit montrer au moins 31,58 € à la pièce de constat. Aux soldes du 21 novembre (11,93 € et 15,59 €), il manque 19,65 € et 15,99 € ; après le versement accordé sous GO-2026-11-21-74 (10,47 € et 6,81 €), il manque 9,18 € sur chacun. » »

Avant :

````text
ou, au plus juste, 15,18 € et 11,52 €. Sans lui, aucune ligne de Google ne part.
````

Après :

````text
ou, au plus juste, 15,18 € et 11,52 €. Sans lui, aucune ligne de Google ne part. Après le versement accordé sous GO-2026-11-21-74 (10,47 € et 6,81 €), il manque 9,18 € sur chacun.
````

**C-57 — section 10, réserve 4.**

Sources :
- Mandat de la session mère : « la borne de réflexion fondée sur les pages de `docs/sources/google-gemini-reflexion-v1/`, ou marquée « supposée ». »
- Journal, OD-315 : « la mère fonde la borne de réflexion sur des pages de Google versées sur main sous `docs/sources/google-gemini-reflexion-v1/` »

Avant :

````text
4. **La borne de réflexion est supposée** (section 4). Rien ne la justifie avant un relevé.
````

Après :

````text
4. **La borne de réflexion est supposée** (section 4). Les pages de Google versées ne donnent aucun maximum de pensée par niveau : rien ne la justifie.
````

**C-58 — section 10, réserve 10.**

Sources :
- Vérification, correction 7 : « Remplacer la réserve 10 par : « 10. **L'échéance de GO-2026-11-21-69 (2026-11-22) n'est pas contrôlée pour l'exemption** : le chef ne contrôle que la forme de `exemption_de_la_sonde_go` (ligne 1441). L'échéance contrôlée est celle du GO de chaque ligne de calcul (garde 8). » »

Avant :

````text
10. **La ligne GO-2026-11-21-69 porte une échéance au 2026-11-22**, et son autonomie court jusqu'à 05:30Z ce jour-là. Si le programme contrôle l'échéance du GO inscrit à `exemption_de_la_sonde_go`, une vérification lancée plus tard serait refusée : la note de la livraison 4 ne le dit pas ; à vérifier.
````

Après :

````text
10. **L'échéance de GO-2026-11-21-69 (2026-11-22) n'est pas contrôlée pour l'exemption** : le chef ne contrôle que la forme de `exemption_de_la_sonde_go` (ligne 1441). L'échéance contrôlée est celle du GO de chaque ligne de calcul (garde 8).
````

**C-59 — section 11 (version 1 gardée, version 2 ajoutée).**

Sources :
- Mandat de la session mère : « ce que tu as ouvert. »
- Mandat de la session mère : « Une seule exception, autorisée par la session mère (R-4684) : le sous-dossier `docs/sources/google-gemini-reflexion-v1/`, à lire par `git show origin/main:<chemin>` et à déclarer. »
- Journal, OD-315 : « la lecture de ce seul sous-dossier (pages publiques de Google) est admise, à déclarer par le rédacteur comme ouverture hors liste autorisée par la mère. »

Avant :

````text
## 11. Ce que j'ai ouvert

- **Le mandat**, en entier,
````

Après :

````text
## 11. Ce que j'ai ouvert

### 11.1 Version 1, par son rédacteur (inchangé)

- **Le mandat**, en entier,
````

**C-60 — section 11.2 (version 2).**

Sources :
- Mandat de la session mère : « ce que tu as ouvert. »

Avant :

````text
## 12. Calculs, par programme
````

Après :

````text
### 11.2 Version 2, par son rédacteur

- **Le mandat de cette version** : le message de la session mère, non versé au dépôt (copie au bloc-notes, `entrees/mandat-mere-v2.txt`, pour confronter les citations de la section 13). Pour mes interdits, le mandat du rédacteur de la version 1 (`mandat-redacteur-fable-avenant-2-plafond-65536-v1.md`, sha256 `55a08330…`, égale à son compagnon), lu en entier.
- **Lus en entier** : la version 1 (`5f84642a…`) ; sa vérification (`037aa7f7…`) ; la note de la livraison 8 (`note-programme-essais-admission-bras-a-v7.md`, `d8efceb2…`) ; la note de la livraison 7 (`note-programme-essais-admission-bras-a-v6.md`, `5a6a41f5…`). Chacune égale à son compagnon.
- **Lus en partie** :
  - la note de la livraison 6 (`note-programme-essais-admission-bras-a-v5.md`, `d72788d7…`), sections 1 à 6 : les notes des livraisons 8 et 7 disent que le reste des notes d'avant vaut encore ;
  - le chef v7 (`scripts/chef_essais_admission_bras_a_v7.py`, `7c63d051…`) : lignes 1 à 135, 440 à 660, 905 à 1010, 1669 à 1800, 1860 à 1960, 2335 à 2356, 2495 à 2512, 2772 à 2786 et 2846 à 3000, plus des recherches de noms ;
  - le gabarit v7 (`configuration-essais-admission-bras-a-v7-gabarit.json`, `e1da2133…`), par programme : ses clés, les champs de `fournisseurs.google`, les trois lignes de Google, quatre notes. Il cite des chemins sous `runs/`, non suivis ;
  - le devis (`421ee2e6…`), lignes 213 à 221 ; l'avenant 1, version 3 (`5e255c5f…`), ses titres et ses lignes 329 à 345 ;
  - les deux relevés que nomme m-2 : `releve-api-mistral-gemini-essais-admission-v1.md` (`291341e2…`), lignes 10 à 25 ; `juge-des-ancres-identifiant-gemini-v1.md` (`ac8bb15e…`), lignes 1 à 30. Le second cite une pièce de mots de Lazar, non suivie ;
  - le dossier des programmes de la version 1 (`avenant-2-programmes-v1/`), sa liste ; son programme de calcul (`calc_av2.py`, `83d296ef…`), lignes 1 à 200, non exécuté.
- **Empreintes seules**, toutes égales à leurs compagnons : la vérification du devis (`0bec479f…`), la confrontation à la règle (`b49688eb…`), la vérification de l'avenant 1 v3 (`8232e22e…`), la note de la livraison 4 (`fbb30439…`), `faire_av2.py` et `verif_av2.py` de la version 1. Le relevé du taux (`a234540a…`) est lu par programme : jour du fixage et taux du dollar.
- **Journal** : la seule entrée OD-315, par `grep -E '^- OD-315 '` ; fichier non ouvert.
- **Registre** : les lignes GO-2026-11-21-68, -69 et -71, par `git show origin/main:registres/go.md | grep -E '^\| GO-2026-11-21-(68|69|71) \|'`. Elles portent aussi des décisions sur d'autres travaux, vues en passant : je n'en recopie rien. Les lignes GO-2026-11-21-74 et -84 ne sont pas lues : la première est citée d'après la vérification, la seconde d'après le mandat.
- **Ouverture hors liste, autorisée par la mère** (mandat, R-4684 ; journal, entrée OD-315) : `docs/sources/google-gemini-reflexion-v1/`, et lui seul sous `docs/sources/`. Sa liste par `git ls-tree -r -l origin/main -- docs/sources/google-gemini-reflexion-v1/` ; ses trois fichiers et leurs compagnons par `git show origin/main:<chemin>`, sur la référence locale `origin/main` (commit `1fa3a5a3…`), sans `git fetch`, copiés au bloc-notes pour être lus ; empreintes égales aux compagnons. Lus : la provenance, en entier ; de la page de la réflexion, les lignes 1 à 40, 130 à 142, 581 à 700, 740 à 760 et 896 à 1015, plus des recherches de mots ; de la référence, les lignes 1 à 12, 130 à 145, 258 à 290, 2622 à 2635 et 2825 à 2860, plus des recherches de mots.
- **Git** : `git status --short`, `git log --oneline -5`, `git rev-parse origin/main`, `git log -1 origin/main`.
- **Débord, déclaré.** Ma première commande a listé le dossier de la relance (`ls … | head -100`, puis le compte de ses entrées : 571) : elle a affiché ses cent premiers noms, dans l'ordre alphabétique, jusqu'à `credits-essai-google-et-gemini-releve-v1.md`. Aucun ne porte un motif interdit, et le dossier cloisonné de la relance n'y figure pas. Le mandat ne demandait aucune liste.
- **Cloisonnement** : aucun chemin de la liste du mandat n'a été ouvert, listé, cherché ni empreinté. Les pièces lues citent des chemins cloisonnés ou sous `runs/` : je ne les ai pas suivis, et cette pièce n'en ajoute aucun. Hors les trois lignes dites, `registres/` n'a pas été ouvert ; `.claude/settings.json` non plus.
- **Registre** : cette pièce ne recopie rien de ce que le mandat défend d'y recopier, et ne nomme aucune ligne de GO d'un autre jour que le 21 novembre.
- Aucun réseau, aucun `git fetch`, aucune clé lue ni affichée, aucun appel de modèle, aucun sous-agent, aucune dépense. Rien scellé, rien committé.
- **Programmes**, au bloc-notes, hors du dépôt (`/tmp/claude-0/-home-user-controle-ia-travail/080a2aff-9781-5a4d-8af3-2aae94066157/scratchpad/redacteur-av2-v2/programmes/`) : `calc_av2_v2.py`, `epreuves_chef_v7.py`, `faire_av2_v2.py`, `verif_av2_v2.py` (empreintes et sorties en section 12.2). `epreuves_chef_v7.py` charge le module du chef v7 sans le lancer, les variables de clé retirées de l'environnement, et n'appelle que trois fonctions : `convertir` ; `controler_credit_de_google`, sa lecture des dépenses remplacée par des valeurs fixées (aucun dossier lu) ; `verifier_ligne_de_calcul`, sur un registre factice, en mémoire.

## 12. Calculs, par programme
````

**C-61 — section 12.1 (titre).**

Sources :
- Mandat de la session mère : « Recalcule par programme, calcul montré, tout chiffre que ces corrections touchent : plafonds, excès, pire cas, seuils par projet, manque en euros après le versement de GO-74. »

Avant :

````text
## 12. Calculs, par programme

Sortie de `calc_av2.py`, entière.
````

Après :

````text
## 12. Calculs, par programme

### 12.1 Version 1 : sortie de `calc_av2.py` (inchangée)

Sortie de `calc_av2.py`, entière.
````

**C-62 — section 12.2 (ajoutée).**

Sources :
- Mandat de la session mère : « Recalcule par programme, calcul montré, tout chiffre que ces corrections touchent : plafonds, excès, pire cas, seuils par projet, manque en euros après le versement de GO-74. »
- Mandat de la session mère : « Le texte neuf des lignes de calcul de Google doit être citable tel quel, à la forme de la garde 8 (note v6, section 6 (c) : `note-programme-essais-admission-bras-a-v6.md`). Chaque ligne cite les empreintes du devis, de sa vérification et de l'avenant 1 v3. »

Avant :

````text
(rien : la section 12 finissait par la sortie de `calc_av2.py`)
````

Après :

````text
### 12.2 Version 2 : … (toute la section 12.2, ci-dessus)
````
