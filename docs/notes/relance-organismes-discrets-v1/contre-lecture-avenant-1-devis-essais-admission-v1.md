# Contre-lecture de l'avenant 1 au devis des deux essais d'admission (recharge gardée, deux clés) — v1

- **Objet** : `docs/notes/relance-organismes-discrets-v1/avenant-1-devis-essais-admission-recharge-et-deux-cles-v1.md`, sha256 `14d479d70ee57ccfcb80bc582c51acdeda92b2de67b3ae7c82936a878093603d` (recalculée, égale à son compagnon), lu avec le devis accepté `devis-essais-admission-mistral-neon-bras-a-v1.md`, sha256 `421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc` (recalculée, égale à son compagnon).
- **Contre-lecteur** : agent neuf, Claude Opus 5.5, qui n'a écrit ni le devis, ni l'avenant, ni le programme. Écrit le 2026-11-21. Non scellé.

## Verdict : engageable après corrections

Les trente et une citations de la section 1 sont exactes à leur ligne (vérifié par programme). Aucun plafond de ligne, excès d'un envoi ni critère d'admission n'est changé en douce. Mais : (1) le chiffre neuf qui devient la borne de tête, 72,94 USD pour la file du juge au cas des neuf excès, ne compte que les neuf envois coupés et oublie la dépense comptée des autres envois : la borne est **76,70 USD** à la file, **80,38 USD** avec la vérification ; (2) une vingtaine de lignes du devis que la recharge ou les deux clés touchent ne sont pas déclarées ; (3) le plafond de dépense à la console n'est pas « exactement » le rôle du solde ; (4) la règle du devis « toute recharge après le constat se constate par un constat neuf » n'est pas traitée ; (5) le lien entre variable et projet repose sur la seule mémoire de Lazar, alors qu'un contrôle sans coût existe avant la file ; (6) la décision de Lazar du 21 novembre (porter le solde à 23,00 USD) n'est pas nommée dans la décision 3. La recommandation « une seule clé, l'autre en réserve » tient.

## Corrections

Les corrections vont dans une version neuve de l'avenant, sous un nom neuf (R12) ; l'avenant v1 est scellé comme écrit et ne se réécrit pas.

### C-1. La borne de la file au cas des neuf excès est 76,70 USD, non 72,94

**Défaut.** 72,77 et 72,94 USD (devis, lignes 389 et 893) sont le coût réel des neuf envois coupés seuls : 9 × 8,085, ou 6 × 8,085 + 3 × 8,142. Ils ne comptent pas les autres envois de la file (les reprises finies), que le compteur laisse passer jusqu'à son plafond. Tant que le solde bornait la perte, l'écart était sans effet ; l'avenant en fait la borne de tête (« le cas calculé le plus haut est 76,62 USD »), et elle est trop basse.

**Calcul (C).** Un envoi coupé coûte réellement sa réserve plus 7,578 USD (8,085 − 0,507 à l'appariement ; 8,142 − 0,564 à la couverture : devis, lignes 307 et 380, délai du relais 2 690 s, 200 jetons par seconde, 15 USD par million en sortie, 3 en entrée). Le compteur refuse un envoi dès que le cumul compté passe le plafond moins la réserve, au plus 8,50 − 0,564 = 7,936 USD avant le dernier envoi (devis, ligne 370). Au pire : cumul compté de 7,936 avant le dernier envoi, ce dernier envoi coupé ou fini au coût plein d'un envoi de couverture, 8,142, et huit envois coupés plus tôt, chacun de 7,578 au-delà de ce qui en a été compté : 7,936 + 8,142 + 8 × 7,578 = **76,702 USD**, soit 8,50 + 9 × 7,578. Avec la vérification de la clé de Google (3,68) : **80,38 USD**. Avec une seconde vérification : **84,06 USD**.

**Texte de remplacement.**
- Section 0, point 1, la phrase « Dans le seul cas où […] plus rien de dur ne l'arrête. » devient : « Dans le seul cas où la file part après une sonde « comprise » et où la borne de sortie se comporte autrement à 32 768 qu'à 256, la perte calculée monte à **76,70 USD** pour la file — le plafond compté de 8,50 USD et neuf excès de 7,578 USD —, **80,38 USD** avec la vérification, au débit déclaré : plus rien de dur ne l'arrête. Le devis donnait 72,77 et 72,94 USD, qui ne comptent que les neuf envois coupés. »
- Section 2.2, dernière ligne du tableau, quatrième colonne : « **76,70** (C : 8,50 + 9 × 7,578) ; les neuf envois coupés seuls font 72,77, ou 72,94 si trois des neuf sont des envois de couverture (D, ligne 389) ».
- Section 2.2, totaux, deuxième et troisième puces : « supposition manquante au régime courant : 3,68 + 76,70 = **80,38 USD** » ; « si une seconde vérification de clé est accordée […] : 3,68 de plus, soit **23,44 USD** et **84,06 USD** ».
- Section 2.5, dernière puce : « le cas à 72,94 USD » devient « le cas à 76,70 USD ».
- Section 8, décision 1, enjeu : « le cas calculé le plus haut est 76,62 USD » devient « le cas calculé le plus haut est 80,38 USD (76,70 à la file du juge, 3,68 à la vérification) » ; option 2 : « le cas à 72,94 USD » devient « le cas à 76,70 USD ».
- Section 6, ligne 4 : « (72,77 USD au débit déclaré) » devient « (jusqu'à 76,70 USD pour la file au débit déclaré, plafond compté compris) ».
- Section 9, quatrième puce, devient : « **Le chiffre de 76,70 USD** est calculé par la contre-lecture de cet avenant ; il remplace, comme borne de la file, les 72,77 (contre-lus) et 72,94 USD (non contre-vérifiés) du devis, qui ne comptent que les neuf envois coupés. »

### C-2. Lignes du devis touchées, non déclarées

**Défaut.** Les tableaux 1.1 et 1.2 omettent des lignes qui disent, à la lettre, que le solde borne la perte, que le solde est porté à 23,00 USD sur un seul compte, ou qu'une recharge exige un constat neuf. Ajouter ces lignes :

| ligne | section | ce que le devis écrit | ce que le mot de Lazar en fait |
|---|---|---|---|
| 5 | en tête | « **chez Google, 23,00 USD de crédit prépayé, en une fois** » ; « seul le solde borne alors la perte, au risque de couper une file qui tiendrait » | les deux phrases tombent : écart 1 et écart 2 |
| 181 | 4.4, texte dit à Lazar sur la file Neon | « La perte est bornée par le solde prépayé, plus tout autre crédit Google Cloud admissible du compte » | de même que la ligne 24 |
| 183 | 4.4 | « la recharge en une fois à 23,00 USD le laisse, même au pire (19,32 ; 6.5) » | vrai seulement si le projet qui joue est porté à 23,00 USD (décision 3, option 1) |
| 386 | 6.4, supposition 2 | « c'est la seule borne d'un envoi, hors le solde prépayé » | ce « hors » tombe (déjà dit en 2.2, à porter au tableau) |
| 394 | 6.4 | « Le solde prépayé borne la perte, sous ces réserves ; il ne protège pas l'essai. » | la première moitié tombe ; la seconde demeure, atténuée par la recharge |
| 411 | 6.5 | « **Décision de Lazar : chez Google, une seule recharge, à 23,00 USD** » | décision antérieure de Lazar, dont le sort est à dire (C-6) |
| 412 à 418 | 6.5, tableau des soldes de départ | « solde de départ S », en USD, sur un seul compte | à relire par projet, en USD convertis |
| 423 | 6.5 | « Sur les seuls 16 USD, la vérification pourrait partir » | le solde vu est en euros (mineur m-4) |
| 426 | 6.5, point 1 | « **le solde prépayé borne la perte chez Google** » | tombe |
| 435 | 6.5 | « **une recharge d'au moins 0,44 USD est alors due** » ; « Toute recharge faite après le constat se constate par un constat neuf, daté, sous un nom neuf. » | une recharge automatique ne se constate pas d'avance : C-4 |
| 438 | 6.5 | « le solde est ce qui peut être perdu si tout va mal ; 23,00 USD y sont exposés » | faux : l'exposition est celle de la section 2.2 |
| 446 | 6.5 | « Le solde prépayé borne la perte, sous les réserves de 6.4 » | tombe |
| 515 | 9 | « le crédit porté à 23,00 le passe » | par projet, converti |
| 538 | 10, garde 9 | cas sain « crédit prépayé de Google à 23,00 » ; artefact « `google_credit_utilisable_usd` à 16,00, l'état de départ avant la recharge » | à reprendre par projet ; l'artefact à 16,00 reste un artefact sous la décision 3, option 1 |
| 599 | 12, point 3 | « **crédit de Google porté à 23,00 USD**, recharge automatique désactivée » | contredit par l'écart 1 ; par projet pour l'écart 2 |
| 640 | 13, point 28 | « c'est **le solde restant au départ de la file** qui borne alors la perte » | tombe |
| 641 | 13, point 29 | « Le solde prépayé comme borne de la perte » ; « l'absence de recharge automatique ne [sont] pas écrit[e]s non plus » | tombe |
| 645 | 13, point 33 | « la borne du solde ne vaut que si aucune recharge automatique ne joue » | la condition manque désormais |
| 646 | 13, point 34 | « Le solde de 16 USD est un mot de Lazar (« il reste 16 dollars » […]) » | le solde vu est en euros |
| 648 | 13, point 36 | « une recharge faite après le constat demande un constat neuf » | C-4 |

### C-3. Le plafond de dépense à la console ne reprend pas « exactement » le rôle du solde

**Défaut.** Un plafond qui refuse les appels n'agit, au mieux, qu'à l'admission d'un appel, sur une dépense que la console compte avec un délai que le devis dit inconnu (ligne 437, m-3). Chez Google, lu sans flux, un envoi en cours dure jusqu'à 45 minutes ; rien n'écrit qu'un plafond le coupe. Au cas des neuf excès, les envois se suivent : un compte en retard peut en laisser passer plusieurs au-delà du plafond. S'il compte par mois, un constat fait en novembre et une file jouée en décembre lui donnent une autre base.

**Texte de remplacement.**
- Section 0, point 2, la phrase « Il reprend exactement le rôle que tenait le solde de 23,00 USD » devient : « Il reprend le rôle que tenait le solde de 23,00 USD, à deux réserves près : il ne coupe sans doute pas un envoi déjà parti, et il compte la dépense avec un délai que la console doit dire. »
- Section 2.5, première puce, ajouter à la fin : « Ce n'est une borne dure qu'au délai de compte de la console près, et à un envoi en cours près (au plus 8,14 USD à la file du juge, au débit déclaré) ; si la console ne dit pas ce délai, la borne est écrite sous cette réserve, à la ligne de calcul. »
- Section 2.4, ajouter : « 8. si le plafond coupe un appel en cours, ou seulement refuse les suivants, et **avec quel délai** il voit la dépense ; 9. si le plafond compte par mois civil : les lignes de Google se jouent dans le mois du constat, ou bien la dépense du mois est relevée de nouveau au premier jour du mois suivant, par un constat neuf. »
- Section 8, décision 1, option 1, inconvénient, ajouter : « borne au délai de compte de la console près et à un envoi en cours près ».

### C-4. Les recharges automatiques et la règle « recharge après le constat, constat neuf »

**Défaut.** Le devis (lignes 435 et 648) veut qu'une recharge faite après le constat se constate par un constat neuf. Avec la recharge active, une recharge peut survenir sans geste entre le constat et la file. L'avenant n'en dit rien hors de la garde 20.

**Texte à ajouter**, en section 4.5, après la puce de la garde 10 : « **Recharges survenues après le constat** : une recharge automatique ne demande pas de constat neuf. La garde 10 ne la compte pas : elle part du crédit du dernier constat, ce qui est du côté prudent, sauf sous la décision 3, option 2, où un seul montant de recharge, relevé au constat, est ajouté, jamais davantage. La règle des lignes 435 et 648 du devis reste pour toute recharge faite à la main par Lazar. » Et ajouter les lignes 435 et 648 au tableau de la section 1 (C-2).

### C-5. Le lien entre variable et projet se contrôle avant la file

**Défaut.** La réserve 9, deuxième puce, écrit qu'une variable prise pour l'autre ferait valoir le constat d'un projet pour les envois d'un autre, et laisse la parade « non exigée ». Or la vérification n'envoie que des messages fixes (`Reply with the single word: OK`, la sonde), aucun texte d'essai ; la file en envoie seize. Regarder, entre les deux, sur quel projet la dépense de la vérification apparaît ne coûte rien et protège les textes de la file.

**Texte de remplacement**, réserve 9, deuxième puce, la dernière phrase devient : « Parade, **exigée** : après la vérification et avant la file, Lazar regarde à la console sur quel projet la dépense de la vérification apparaît, et le dit dans un mot que la pièce porte à la lettre ; la file ne part pas sans cette pièce, qui nomme le projet constaté. » En section 8, décision 2, ajouter à « À dire avec la décision » : « et l'accord sur ce contrôle d'après la vérification ». En section 7, point 7, ajouter : « la garde 10 exige de plus la pièce de ce contrôle, d'empreinte inscrite à la configuration ; artefact : pièce qui nomme l'autre projet. »

### C-6. La décision de Lazar du 21 novembre est à nommer dans la décision 3

**Défaut.** La pièce `mots-de-lazar-compte-google-prepaye-bras-a-2026-11-21-v1.md` (487b5a72…, devis ligne 411) porte une décision de Lazar : porter le solde prépayé de Google à 23,00 USD. L'avenant la dit « non fait ; remplacé par la décision 3 » (tableau 1.2, ligne 422). Ce n'est pas à l'avenant de la remplacer, et « on va combiner les deux » peut se lire comme la retirant.

**Texte de remplacement**, section 8, décision 3, option 1 : « Option 1 : solde seul, comme au devis ; **la décision de Lazar du 21 novembre (pièce `487b5a72…`) reste, appliquée au projet qui joue** : son crédit est porté à 23,00 USD, convertis au taux diminué de la marge de change. Avantage : […] » (suite inchangée). Et dans le tableau 1.2, ligne 422, « non fait ; remplacé par la décision 3 » devient « non fait ; son sort sur le projet qui joue est la décision 3 ».

## Mineurs

- **m-1. Seuils de taux arrondis au plus proche au lieu de par excès** (section 3). Un seuil de taux doit s'arrondir vers le haut : à 1,0314 USD par euro, 15,59 € ne font que 16,0795 USD, sous 16,08. Lire : 0,3085 ; 1,0210 ; 0,7813 ; 1,3479 ; **1,0315** ; **1,6564** ; 1,2675 ; **0,7181** ; avec une marge de 5 % : **1,0858**, 1,3342, **0,7559**. Et « sans un euro à plus de 1,2675 USD » devient « sans un euro d'au moins 1,2675 USD (1,26748 exactement) » ; « si l'euro vaut plus de 1,0314 » devient « d'au moins 1,0315 ». Aucune conclusion ne change.
- **m-2. « À un taux de change plausible »** (0, point 4 ; section 3) : jugement sans pièce. Écrire « au taux qu'il faudrait, que la pièce du taux dira ».
- **m-3. Devise en clé du tableau** : la vérification du programme (`557c15da…`, section 4, point 1) demande une ligne **hors tableau**, « qui ne change pas les treize clés du tableau du devis » ; l'avenant en fait des clés (`google_devise_affichee_projet_N`, `mistral_devise_affichee`) et l'attribue à cette vérification. C'est un choix défendable, mais à déclarer comme écart à la proposition du vérificateur. Le même point 3 préfère comme source le taux que la console affiche elle-même : à reprendre en section 5.
- **m-4. Le « 16 dollars » de la pièce 487b5a72** est très probablement le solde de 15,59 € du compte B, lu en dollars. L'avenant ne le dit pas. Il ne faut pas en tirer quelle variable va avec quel compte (la pièce dit « clé par défaut ») : seul Lazar le dit (décision 2). Le tableau des soldes de départ (devis, lignes 416 à 418) repose sur 16,00 USD.
- **m-5. Décision 1, option 3** (régime prudent imposé à la file partie après une sonde « comprise ») retire la reprise unique que la règle 1 donne à cet envoi (devis, ligne 346 : « un modèle pourrait échouer sur un seul délai, par une règle de compte du devis »). C'est un écart au texte des règles d'admission, comme (a1) : à écrire dans l'inconvénient. Elle ne borne de plus rien si la coupure n'arrête pas la facturation.
- **m-6. Les 16,08 et 19,76 USD ne sont eux-mêmes bornés que sous les suppositions 1 et 2.** Sans le solde, un débit de 400 jetons par seconde (devis, ligne 381) donne au régime prudent 1,50 + 4,85 + 8,50 + 15,65 = **30,50 USD**, et, au cas des neuf excès, 8,50 + 9 × 15,65 ≈ **149 USD** (C, au grain des excès du devis). Une phrase en 2.2 suffit.
- **m-7. En-tête, « Ce que cet avenant ne change pas » : « aucun réglage »** — l'avenant ajoute un réglage de console (le plafond) et des refus neufs (section 7, points 2, 9, 10). Écrire « aucun réglage des modèles ; des gardes s'ajoutent (section 7) ».
- **m-8. État** : l'avenant se dit « Non scellé », alors que son compagnon `.sha256` existe (commit 9dee27629, « scellé comme écrit »). La version neuve dit « scellé comme brouillon ».
- **m-9. Décision 2, enjeu** : dire en clair que l'option recommandée, (b), ne fait pas ce que le mot « on va combiner les deux » demande, et qu'aucune option sans écart aux règles d'admission ne le fait (ce que dit déjà 4.4).
- **m-10. Décision 4, recommandation** : le format veut une recommandation ; écrire « Recommandation : 5 %, celle de la session mère ; le rédacteur écarte seulement l'option 3. »
- **m-11. Section 2.2, troisième colonne de la dernière ligne** : « jusqu'à neuf envois coupés » ; écrire « neuf excès de 7,58 au plus ».
- **m-12. Section 2.3** : la formule suppose une recharge déclenchée au passage sous T et créditée aussitôt ; elle est dite (S), c'est juste ; ajouter qu'un moyen de paiement refusé laisse la coupure par solde à court entière.

## Réponses aux six questions

1. **Écarts déclarés et cités** : oui pour les trente et une citations, toutes exactes à leur ligne ; non pour l'inventaire, incomplet (C-2). Aucun seuil, plafond ni critère ne change sans le dire ; ce qui change sans être nommé : la règle « recharge après le constat » (C-4) et le sort d'une décision antérieure de Lazar (C-6).
2. **Chiffres** : 3,68 ; 16,08 ; 19,76 ; 72,94 (comme coût des neuf envois) ; 76,62 ; 1,2675 : justes au calcul. 72,94 et 76,62 ne sont pas des bornes : 76,70 et 80,38 (C-1).
3. **Sans le solde** : la perte n'est bornée par le programme que sous les suppositions 1 et 2 (débit, coupure qui arrête la facturation), et, au régime courant, sous la troisième ; sinon rien ne la borne (m-6). Le plafond de console n'est une vraie borne que s'il refuse les appels, et encore au délai de compte et à un envoi en cours près (C-3). Sans plafond proposé, il ne reste que l'acceptation écrite de Lazar (option 2) ou le régime prudent (option 3, écart aux règles, m-5).
4. **Deux clés** : l'analyse de « huit sur huit » sous une file coupée est juste ; les points 1, 2 et 4 de 4.3 suffiraient. La recommandation (b) tient. Constater le projet de réserve n'est pas dû tant qu'il n'est appelé ; contrôler le lien entre variable et projet l'est (C-5).
5. **Décisions** : bien posées. Il manque le sort de la décision du 21 novembre (C-6, versé dans la décision 3) et l'accord sur le contrôle d'après la vérification (C-5, versé dans la décision 2) ; aucune de trop.
6. **Texte neuf des lignes 2 et 4** : citable une fois C-1 et C-3 portés. À la ligne 2, « et, au-delà, par [le plafond de dépense réglé à la console de ce projet, de [valeur] | …] » devient « et, au-delà, par [le plafond de dépense réglé à la console de ce projet, de [valeur], au délai de compte de la console et à un envoi en cours près | …] » ; même ajout à la ligne 4 après « de [valeur] ».

## Chiffres recalculés

Par un programme jetable du bloc-notes (`calc.py`, nombres décimaux exacts), hors du dépôt.

| chiffre | recalcul | verdict |
|---|---|---|
| 3,68 | 1,50 + 2,18 | juste |
| 16,08 | 8,50 + 7,58 | juste |
| 19,76 | 3,68 + 16,08 | juste |
| coût d'un envoi coupé | 2 690 × 200 × 15 ÷ 10⁶ + entrée : 8,085 (appariement), 8,142 (couverture) ; excès 7,578 dans les deux cas | juste (devis) |
| 72,77 ; 72,94 | 9 × 8,085 ; 6 × 8,085 + 3 × 8,142 | justes comme coût des neuf envois coupés ; **non comme borne** |
| borne de la file, neuf excès | 7,936 + 8,142 + 8 × 7,578 = 76,702 | **76,70** (C-1) |
| 76,62 ; 76,45 | 3,68 + 72,94 ; 3,68 + 72,77 | justes au calcul ; **80,38** comme borne |
| 23,44 ; 80,30 | 19,76 + 3,68 ; 76,62 + 3,68 | 23,44 juste ; **84,06** comme borne |
| 27,99 | 8,23 + 19,76 ; 8,23 = 1,42 + 1,42 + 5,39 | juste |
| 22,72 ; 26,96 ; 4,23 | × 1,15 | justes ; arrondis 23,00 ; 27,00 ; 4,50 justes |
| 1,2675 | 19,76 ÷ 15,59 = 1,267479 | juste ; « au moins », non « plus de » (m-1) |
| taux de la section 3 | quotients exacts | justes au plus proche ; par excès : 1,0315 ; 1,6564 ; 0,7181 ; 1,0858 ; 0,7559 (m-1) |
| 27,52 | 11,93 + 15,59 | juste |
| 16,75 ; 14,92 ; 31,67 | 15,25 + 1,50 ; 12,74 + 2,18 ; somme | justes |
| clés du constat | Google 7 + 5 = 12 ; Mistral 6 + 1 = 7 ; 19 ; 2 × 12 + 7 = 31 | justes |
| 400 jetons par seconde | 1,50 + 4,85 + 8,50 + 15,65 = 30,50 ; 8,50 + 9 × 15,65 = 149,35 | neufs (m-6) |

Les trente et une citations des tableaux 1.1 et 1.2 ont été confrontées par programme (`cit.py`) à leur ligne du devis : toutes présentes à la ligne dite.

## Ce que j'ai ouvert

- L'avenant, en entier ; son compagnon `.sha256`.
- Le devis accepté : lignes 4, 5, 14, 16, 24, 88, 93, 181, 183, 184, 259, 300 à 315, 337, 346, 368 à 400, 405 à 452, 460, 490 à 516, 538 à 549, 557 à 599, 639 à 652, et les lignes rendues par une recherche de « solde », « recharge », « GEMINI_API_KEY », « 23,00 », « 19,76 », « 16,08 », « projet », « devise », « euro », « 7,58 », « 72,77 », « 72,94 » ; son compagnon `.sha256`.
- `mots-de-lazar-compte-google-prepaye-bras-a-2026-11-21-v1.md`, en entier, et son compagnon.
- `verification-corrections-programme-essais-admission-livraison2-v1.md` : les lignes rendues par une recherche de « marge », « 2 % », « 5 % », « 24 heures », « devise » ; empreinte recalculée (557c15da…).
- `journal-relance-organismes-discrets-v1.md` : les lignes OD-285 à OD-290, par recherche.
- `registres/go.md` : sur la branche de travail, une recherche de « GO-2026-11-21-66 » ne rend rien (le registre de la branche s'arrête aux GO du 18 novembre) ; sur `origin/main` (commit 595c6525a), la seule ligne GO-2026-11-21-66, dont les deux mots cités par l'avenant sont exacts à la lettre. Les soldes en euros n'y figurent pas.
- `git log` et `git show --stat` du commit 9dee27629 ; la liste des noms de fichiers du dossier de la relance.
- **Non ouverts** : aucune clé, aucun réseau, aucun chemin de la liste interdite, aucun code du programme.
