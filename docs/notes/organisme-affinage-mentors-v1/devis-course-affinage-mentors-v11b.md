# Devis de la course d'affinage des idées des mentors — v11b : seuil de recharge de la clé LUC, prix relevés d'Argon et de Carbon, Carbon en flux, Argon sous la garde des appels à Google, clé Claude LUC (non engagé)

- **v11b**, écrit le 2026-11-22T20:32:31Z (`date -u +%FT%TZ`) : c'est le devis v11 (`docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v11.md`, `34271cb3cb3dba89c897cc076f7a65cbf73630d96f7106f2f40adac9a2590d52`, écrit le 2026-11-22T19:47:59Z, qui reste en place, R12) plus un fait lu par Lazar à la console — le seuil de déclenchement de la recharge automatique de la clé LUC, 5 USD (registre des décisions de `main`, R-5042) — et ce qu'il implique (§ 5 bis, neuf ; une phrase au § 5 et une au § 7). **Aucun chiffre du devis v11 ne change.** Par le rédacteur du préenregistrement v11 (mandat `docs/notes/organisme-affinage-mentors-v1/course-v8/mandat-fable-preenregistrement-affinage-v8.md`, `0f7ddc5487459ecc637db8b29f0fbad6b47deda43d7fa47f79fec4a98a8f9ec2`), sur les décisions de la mère (registre des décisions de `main` : R-5006 et R-5007, points (c) et (d) ; R-5018, prix déclarés) et sur les mots de Lazar inscrits en GO-2026-11-22-124. Registres lus sur `main` au commit `61ec4bb16537d899d431fe7a74d10b0c17053d86` : `registres/decisions.md` `d70dd20afbd5d3b746b1a74ad013a37fec05dde6b25429a67dce4542204855ab`, `registres/go.md` `8f54197a90d07412e4d7e1aa38e482cea57b5429cb0d01d7eb35ab2a85f64453`. **Version 11b** (R12) : les devis v1 à v11 restent en place ; base : devis v10 (`docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v10.md`, `e007a137c73164a56ebccb2c1d7f4f0ee9c77b88d17b5597528d6bfde172d885`, branche `prep/affinage-v10-compte-organisme-v1`). Même composition (deux espèces Claude, Argon, Astra, Carbon ; pas de Kimi), même plafond d'arrêt (150 USD, GO-2026-11-18-14). Aucun appel, aucun réseau, aucune dépense. À contre-lire.
- **Calcul** : chaque chiffre de ce devis qui n'est pas repris d'une pièce citée est recalculé par `docs/notes/organisme-affinage-mentors-v1/course-v11/calcul-devis-course-affinage-mentors-v11b.py` (`cf316ba4db4005e2d64a114f4f4aea93187ebfa372a3bf072594e5513f8cd0e6` ; 131 chiffres contrôlés, aucun écart : les 116 du devis v11, inchangés, et 15 pour le § 5 bis ; `python3 -I` sur ce fichier, sans argument).
- **Ce qui change par rapport au devis v10** : (1) **Argon et Carbon sont comptés à 4 et 20 USD par million de jetons**, prix le plus haut de la page de prix du fournisseur versée au dépôt, au lieu des bornes 8,3 et 41,5 (décision de la mère, R-5018) ; (2) Carbon est au prix plein (appel en flux : plus de facteur de lot) ; (3) Argon passe sous la garde gelée des appels aux modèles de Google (`CLAUDE.md` de `main`, GO-2026-11-21-71) : sa réflexion, comptée au prix de sortie, s'ajoute à ses deux postes, et le **plafond de session des juges est relevé de 0,60 à 1,00 USD** (R-5018) ; (4) les prix d'Astra sont relevés ; (5) clé Claude LUC : la part Claude a un plafond propre de 45 USD. **Ce qui ne change pas** : prix par jeton et hypothèses de jetons des postes Claude, d'Astra et de l'aiguilleur (devis v6, § 1 et § 2) ; budget et plafonds de relais des étapes ; plafond de session des proposeurs (3,00 USD) et de l'aiguilleur (0,25 USD) ; plafond d'arrêt.
- **Résultat en trois lignes** : sans la réflexion d'Argon, la course est estimée à 35,68 USD (39,25 avec la marge de 10 %), en dessous du devis v10 (41,14 et 45,25). La réflexion d'Argon au niveau `high` n'est mesurée nulle part sur ces consignes ; chaque millier de jetons de réflexion moyenne par appel d'Argon ajoute 3,52 USD ; à sa provision entière (16 384 jetons à chacun de ses 176 appels), la course est à 93,36 USD (102,69 avec la marge). Le plafond d'arrêt de 150 USD ne coupe l'étape des juges qu'au-delà d'environ 32 500 jetons de réflexion moyenne par appel d'Argon, presque son plafond de sortie : ce risque, réel aux bornes des v6 à v10 (§ 8), n'a plus de prise réaliste.

## 1. Prix, avec leur source

| espèce | USD par million de jetons, entrée et sortie | source | statut |
|---|---|---|---|
| première espèce Claude (proposeur, aiguilleur, juge) | 4,00 et 20,00 | barème du relais épinglé (`pole/relais_reel.py`, `1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153`) | à relever le jour du départ (condition de GO-2026-11-18-14) |
| seconde espèce Claude (proposeur) | 10,00 et 50,00 | même barème | idem |
| Argon, `gemini-4-argon` (proposeur, second juge) | **4 et 20**, jetons de réflexion compris dans la sortie | page de prix du fournisseur versée sur `main` : `docs/sources/prix/page-prix-gemini-api-20261122T104129Z.html`, `d3aa716e33e77c7df9da385258dac241f7a608926669f190f42293961201c017`, l. 372-382 : entrée 2,00 jusqu'au 30 novembre 2026 et 4,00 à partir du 1er décembre ; sortie, réflexion comprise, 10,00 puis 20,00 ; le prix le plus haut est retenu (R-5018) | relevé sur une page versée, non lu à la console de facturation ; en v6 à v10 : bornes 8,3 et 41,5 (§ 8) |
| Carbon, `gemini-4-carbon` (proposeur) | **4 et 20**, prix plein, jetons de réflexion compris dans la sortie | même page, l. 153-163 : mêmes prix, mêmes dates ; le prix le plus haut est retenu (R-5018) ; le facteur de lot 0,5 ne vaut plus | idem ; en v5 à v10 : bornes 8,3 et 41,5 (§ 8) |
| Astra, `gpt-6.2-astra` (proposeur) | 8 et 40 (16 et 60 au-delà de 272 000 jetons d'entrée) | R-4905 | relevé ; le palier haut est hors d'atteinte (corps d'un appel : 8 011 octets au plus, devis v10, § 2) |

Jusqu'au 30 novembre 2026, les prix déclarés d'Argon et de Carbon sont le double du prix de la page : avant le 1er décembre, la dépense comptée sur la clé de Google est le double de la dépense facturée, si la page dit vrai. Le plafond d'arrêt et les plafonds de session portent sur la dépense comptée.

## 2. Plafond de session des juges : 1,00 USD au lieu de 0,60

**Pourquoi il change.** La garde gelée refuse tout envoi à un modèle de Google dont le plafond de sortie n'atteint pas la provision de réflexion plus 16 000 jetons de texte. Aux réglages d'Argon sous cette garde (ci-dessous), le pire cas d'un appel de juge dépasse 0,60 USD quelle que soit la façon de compter la réflexion ; au plus petit plafond de sortie que la garde admet à cette provision (32 384 jetons), il vaut encore 0,6631 USD. Sous 0,60 USD, aucun appel de juge d'Argon ne peut donc tenir à la fois la garde et son plafond. Le plafond de session est fixé par rôle, non par espèce : le relever pour Argon le relève aussi pour le juge Claude.

**Réglages d'Argon retenus pour le chiffrer** : niveau de réflexion `high`, sans budget ; plafond de sortie 32 768 jetons ; provision de réflexion 16 384 jetons ; texte restant 16 384 jetons. Ce sont les réglages d'Argon sous la même garde dans le collisionneur (`docs/notes/collisionneur-v9/verification-corrections-collisionneur-v9-v8-fable-v1.md` sur `main`, `9cf6799fcf8d48acec9f505929caaf97d516c7d8f443b9df3fbf7d115dbd9a86`, § 3) ; 32 768 est aussi la limite de sortie d'Argon hors flux dans la garde commune (`src/controle_ia/garde_google_v3.py` sur `main`, `923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91`) : Argon n'a pas besoin du flux. Un budget de réflexion n'est pas une issue : sous un budget de 8 192 jetons, Argon n'a rendu aucun jeton de pensée sur 22 réponses (`docs/notes/collisionneur-v9/contre-lecture-collisionneur-v9-v7-fable-v1.md` sur `main`, `f6342515fffdb0d31895bee21afdf04638b4cfbe3baefb90a8a3072cd856b512`, § 3), ce que la garde lit comme un défaut.

**Entrée d'un appel de juge** : consigne du juge 1 514 caractères (1 563 octets ; `course-v1/consigne-juge-course-affinage-mentors-v1.md`, `a32583b14845343a613514cdcba3c24831a274b48ecc95fe0d884f017d27d346`) + une carte de 9 000 caractères au plus (consigne du proposeur, l. 20) + 500 caractères de cadre (supposé) = 11 014 caractères ; à 3 caractères par jeton et 5 % de marge : 3 855 jetons, 0,0154 USD (à 4 caractères par jeton, défaut de la commande d'Argon des v6 à v10 : 2 892 jetons).

**Pire cas d'un appel de juge d'Argon, selon la façon de compter la réflexion** :

| façon de compter | formule | sortie comptée | pire cas | plafond qui en découle |
|---|---|---|---|---|
| la réflexion compte dans le plafond de sortie (lecture de la garde commune et de la documentation du fournisseur) | entrée + plafond de sortie | 32 768 × 20 / 10⁶ = 0,6554 | 0,6708 USD | 0,70 USD |
| **la provision s'ajoute au plafond de sortie** (convention de la commande d'Argon des v6 à v10, `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py`, `46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46`, l. 202 et 855, et de la commande de Carbon par lot des v8 à v10 : elle tient dans les deux lectures) | entrée + (plafond de sortie + provision) | 49 152 × 20 / 10⁶ = 0,9830 | 0,9985 USD | **1,00 USD** |

**Valeur retenue : 1,00 USD** (R-5018), la plus petite valeur au dixième qui tient dans les deux façons de compter. **Marge étroite, à connaître** : quand la provision s'ajoute au plafond de sortie, 1,00 USD laisse passer une entrée de juge de 4 240 jetons au plus, soit 385 jetons de plus que l'entrée attendue au compte le plus prudent (3 855 jetons, dont le cadre de 500 caractères est supposé) ; au-delà, la commande ne peut plus tenir à la fois la garde et le plafond, et l'appel est refusé avant l'envoi : échec du juge, compté pour A3 et A14. À 1,10 USD, l'entrée couverte serait de 29 240 jetons. Quand la réflexion compte dans le plafond de sortie, 1,00 USD couvre une entrée de 86 160 jetons, et 0,70 USD suffirait. **Recommandation du rédacteur** : 1,10 USD si la commande d'Argon sous la garde ajoute la provision au plafond de sortie ; 1,00 USD sinon. Dans les deux cas, le contrôle fait par le lanceur avant le départ (pire cas d'un appel de juge sur la plus longue entrée de juge admise, sous le plafond de session) montre une marge insuffisante avant tout appel payant.

**Proposeurs de Google, sous leur plafond de session de 3,00 USD (inchangé)**, sur l'entrée la plus longue de la course (2 618 jetons, devis v10, § 1) : Argon aux mêmes réglages, 0,9935 USD au pire quand la provision s'ajoute au plafond de sortie (0,6658 quand la réflexion y est comptée) ; Carbon en flux, 1,3212 USD au plafond de sortie le plus haut que la garde admet (65 536 jetons) quand la réflexion y est comptée, et 2,3042 USD quand s'y ajoute la provision de Carbon sous la même garde dans le collisionneur (49 152 jetons ; même note de vérification, § 3). Les réglages de Carbon de cette table tiennent donc sous 3,00 USD dans les deux façons de compter ; aux bornes des v6 à v10, le second cas valait 4,7813 USD et n'y tenait pas (§ 8).

**Ce que ce relèvement ne change pas** : les estimations (elles viennent des jetons, non du plafond) ; le plafond d'arrêt. **Ce qu'il change** : ce qu'un appel de juge peut coûter, pour Argon comme pour Claude ; la borne des plafonds de session, 80 × 3,00 + 160 × 0,25 + 320 × 1,00 = 600 USD (472 au devis v10), très au-dessus de 150 : seul le plafond d'arrêt borne la dépense.

## 3. Estimation (composition déclarée, cinq espèces)

| poste | devis v10 | v11, sans la réflexion d'Argon | calcul |
|---|---|---|---|
| proposeurs Claude | 7,896 | 7,896 | 16 × 0,141 + 16 × 0,3525 (devis v6, § 2) |
| proposeur Argon | 4,416 | **2,128** | 16 × 0,276 × 20 / 41,5 : le prix par appel du devis v6 (§ 1 ; 0,276 USD, mesuré aux bornes, sans la garde) ramené aux prix déclarés, soit 0,1330 USD par appel |
| proposeur Astra | 4,416 | 4,416 | 16 × 0,276 (supposé ; aucun chiffre ne dépend des prix relevés d'Astra) |
| proposeur Carbon | 7,976 | **7,688** | 16 × 0,4805 : (2 618 × 4 + 23 500 × 20) / 10⁶, hypothèses du devis v10, § 2 (réflexion 20 000 jetons, réponse 3 500, entrée 2 618), au prix plein déclaré |
| aiguilleur | 4,96 | 4,96 | 160 × 0,031 |
| juge Claude | 5,92 | 5,92 | 160 × 0,037 |
| juge Argon | 5,552 | **2,676** | 160 × 0,0347 × 20 / 41,5 : le prix par appel du devis v6 (§ 1 ; 0,0347 USD, mesuré aux bornes, sans réflexion) ramené aux prix déclarés, soit 0,0167 USD par appel |
| **sous-total** | **41,136** | **35,683** | |
| marge de 10 % | 4,11 | 3,57 | |
| **total** | **45,25** | **39,25** | |

Les deux postes d'Argon sont ramenés aux prix déclarés par une règle de trois : les deux prix changent du même rapport (2,075), donc le coût d'un même appel change d'autant.

**La réflexion d'Argon, poste non mesuré.** Sous la garde, Argon réfléchit au niveau `high` à chacun de ses 176 appels (16 de proposeur, 160 de juge) ; cette réflexion est comptée au prix de sortie et ne figure dans aucune mesure du devis v6. Pour une réflexion moyenne de T jetons par appel : proposeur + 16 × T × 20 / 10⁶, juge + 160 × T × 20 / 10⁶, soit **3,52 USD par millier de jetons** (0,32 pour le proposeur, 3,20 pour le juge).

| réflexion moyenne d'Argon par appel | proposeur Argon, en plus | juge Argon, en plus | sous-total | avec la marge de 10 % |
|---|---|---|---|---|
| 0 (base de l'écart au devis) | 0 | 0 | 35,68 | 39,25 |
| 2 000 jetons | 0,64 | 6,40 | 42,72 | 47,00 |
| 4 096 jetons | 1,31 | 13,11 | 50,10 | 55,11 |
| 8 192 jetons | 2,62 | 26,21 | 64,52 | 70,97 |
| 16 384 jetons (la provision) | 5,24 | 52,43 | 93,36 | 102,69 |

Aucune de ces lignes n'est une estimation : la réflexion d'Argon au niveau `high` sur une consigne de juge n'est mesurée dans aucune pièce lue. Toutes tiennent sous 150 USD. La **base de l'écart au devis** du manifeste de fin est la première ligne, 35,683 USD sans marge : l'écart mesuré dira la réflexion d'Argon.

**Carbon, si sa réflexion est plus forte.** L'estimation (20 000 jetons de réflexion) reprend trois lots d'une autre course (devis v10, § 6). Dans le collisionneur, sur d'autres consignes, 21 réponses réelles de Carbon en flux portaient 19 727 à 44 101 jetons de pensées (`docs/notes/collisionneur-v9/contre-lecture-collisionneur-v9-v7-fable-v1.md` sur `main`, `f6342515fffdb0d31895bee21afdf04638b4cfbe3baefb90a8a3072cd856b512`, § 3 ; comptes de jetons seulement, aucun contenu lu) : au haut de cette plage, un appel de Carbon coûterait 0,9625 USD et le poste 15,40 USD, soit 7,71 USD de plus que l'estimation, sous le plafond de session. Argon à sa provision entière à chaque appel et Carbon à cette réflexion, ensemble : 101,07 USD, 111,17 avec la marge de 10 %.

Le « haut » du devis v10 (convention mixte, non une borne) n'est pas reconduit. La borne est le pire cas, 150 USD.

## 4. Ce que le plafond d'arrêt fait de ces chiffres

Le budget des étapes ne change pas (configuration : proposition, attendu 25 et plafond de relais 60 ; aiguillage, 6 et 30 ; juges, 14 et 50) ; les seuils du devis v10, § 3 bis, tiennent : l'aiguillage est lancé si la proposition a coûté au plus 120 USD, les juges si la proposition et l'aiguillage ont coûté ensemble au plus 100 USD, et l'étape des juges reçoit alors un plafond dur de 150 USD moins le cumul.

- Aux estimations sans réflexion d'Argon, le cumul avant les juges est 27,09 USD (22,13 + 4,96) : les juges sont lancés, avec un plafond dur de 122,91 USD ; ils coûtent 8,60 USD, plus 3,20 USD par millier de jetons de réflexion moyenne par appel de juge d'Argon.
- La course tient sous 150 USD tant que 35,683 + 176 × T × 20 / 10⁶ ≤ 150, soit **T ≤ 32 476 jetons** de réflexion moyenne par appel d'Argon (31 462 si tous les autres postes prennent leur marge de 10 %), à la marge d'un appel près. Ce seuil est au-dessus de la provision (16 384) et presque égal au plafond de sortie d'Argon lui-même (32 768) : si la réflexion compte dans ce plafond, il n'est pas atteignable avec un texte utile.
- À la provision entière (16 384 jetons à chaque appel d'Argon), rien n'est coupé : 93,36 USD.

Aux bornes des v6 à v10, le même seuil était à 13 812 jetons et la provision entière coupait l'étape des juges (§ 8) : le changement de prix retire ce risque sans aucune dépense de mesure.

## 5. Part au pire par clé

| clé (nom de variable) | relais, rôles | estimation, marge comprise | **part au pire** |
|---|---|---|---|
| `RR_ANTHROPIC_API_KEY_LUC` | Claude : deux proposeurs, aiguilleur, premier juge | 20,65 (inchangée) | **45,00**, plafond propre de la part Claude, tenu par le relais Claude (R-5007, point (a) ; GO-2026-11-22-124), au dépassement du relais près ; ni plancher de départ, ni lecture du solde (GO-2026-11-22-124) |
| `GEMINI_API_KEY`, partagée par Argon et Carbon | Argon : proposeur, second juge ; Carbon : proposeur | Argon 5,28 + Carbon 8,46 = 13,74, sans la réflexion d'Argon (+ 3,87 par millier de jetons de réflexion moyenne) | **198,00** (150 + 16 × 3,00), inchangée : borne écrite, non une dépense possible ; clé sous la dispense R-3237 |
| `OPENAI_API_KEY_2` (clé injectée par le secret de réseau) | Astra : proposeur | 4,86 | **48,00** (16 × 3,00), inchangée |

Somme des estimations par clé, sans la réflexion d'Argon : 20,65 + 13,74 + 4,86 = 39,25. La part Claude estimée ne dépend ni des prix de Google ni de la réflexion d'Argon ; elle tient sous son plafond de 45 USD. Le relais Claude refuse un appel dès que la part engagée (dépense plus montants réservés des appels en vol) dépasse 44,60 USD (45 moins sa réserve par appel de 0,40 USD) ; le haut de la part Claude du devis v10 (74,62 USD, convention non reconduite) n'y tient pas : la course s'arrête alors, comme le préenregistrement v11 le prévoit. La clé LUC part sans lecture de son solde, sur la recharge automatique (jusqu'à 40 euros, GO-2026-11-22-111 et GO-2026-11-22-124) : ce devis ne dit pas ce qu'elle peut couvrir. Seuil de déclenchement de cette recharge : 5 USD (R-5042 ; § 5 bis).

## 5 bis. Seuil de recharge de la clé LUC, et refus pendant le délai de recharge (neuf en v11b)

**Fait.** Le seuil de déclenchement de la recharge automatique de la clé LUC est de 5 USD, lu par Lazar à la console de facturation le 22 novembre 2026 (registre des décisions de `main`, R-5042). La recharge disponible a été dite « jusqu'à 40 euros » (GO-2026-11-22-111). Ne sont dans aucune pièce lue : le délai entre le déclenchement et le crédit, le montant de chaque recharge, et ce que fait la recharge quand le solde est déjà sous le seuil.

**Ce que le seuil implique.** Le préenregistrement v11 arrête la course au premier refus de l'interface. Si le solde est au-dessus de 5 USD, la recharge se déclenche quand il passe sous ce seuil, alors qu'il reste près de 5 USD, à un appel près : un refus pendant le délai de recharge suppose que la part Claude dépense ce reste avant que la recharge soit créditée.

| ce que font 5 USD, aux prix par appel du devis | nombre d'appels | appels de ce rôle dans la course |
|---|---|---|
| proposeur de la première espèce Claude (0,141 USD par appel) | 36 | 16 |
| proposeur de la seconde espèce Claude (0,3525 USD par appel) | 15 | 16 |
| aiguilleur (0,031 USD par appel) | 162 | 160 |
| juge Claude (0,037 USD par appel) | 136 | 160 |

Aux prix du devis, 5 USD valent 27 % de la part Claude de toute la course sans marge (18,776 USD), 63 % de sa part dans la proposition (7,896 USD), un peu plus que tout l'aiguillage (4,96 USD) et 84 % de sa part dans les juges (5,92 USD). À ces prix, un refus pendant le délai de recharge n'arrive que si la recharge tarde à l'échelle d'une étape entière, ou n'aboutit pas.

**Ce que le seuil ne couvre pas.** (1) Des sessions près de leur plafond : 5 USD font deux sessions de proposeur à 3,00 USD, cinq de juge à 1,00 USD ou vingt d'aiguilleur à 0,25 USD ; si plusieurs sessions tournent ensemble près de leur plafond, le reste peut partir en quelques appels. (2) Un solde déjà sous 5 USD au départ : le solde n'est pas lu (GO-2026-11-22-124), et la marge est alors ce solde, non 5 USD. (3) Une recharge qui échoue, ou qui a épuisé ses 40 euros : le refus suit, et c'est l'arrêt prévu. Dans tous ces cas la règle ne change pas : arrêt au premier refus, sans relance. Le seuil ne change aucun chiffre de ce devis.

## 6. Plafond demandé

**150 USD**, plafond d'arrêt de toute la course, **inchangé** (GO-2026-11-18-14, prolongée par GO-2026-11-22-80 ; exception de la clé LUC : GO-2026-11-22-107, précisée par GO-2026-11-22-124). Aucune ligne neuve n'est demandée par ce devis.

## 7. Ce qui n'est pas établi

- La réflexion d'Argon au niveau `high`, par appel de proposeur et par appel de juge : non mesurée ; c'est le premier poste d'incertitude du coût (§ 3), sans prise réaliste sur le plafond d'arrêt (§ 4).
- La façon dont l'interface de Google compte la réflexion dans le plafond de sortie : la documentation la compte dedans ; une note de la commande d'Argon des v6 à v10 dit avoir vu le contraire sur un appel (`commande_argon_v3d.py`, l. 260-261). Le plafond de 1,00 USD tient dans les deux cas, avec une marge étroite dans le second (§ 2).
- Les prix d'Argon et de Carbon : ils viennent d'une copie versée de la page du fournisseur, non d'une lecture de la console de facturation. Si un prix réel dépassait le prix déclaré, la dépense serait sous-comptée, ce que les bornes des v6 à v10 excluaient et que ce devis n'exclut pas : la page est à relire le jour du départ.
- Les postes d'Argon ramenés aux prix déclarés supposent le même nombre de jetons qu'à la mesure du devis v6.
- La réflexion de Carbon en flux sur ces consignes (§ 3).
- Le coût réel des sessions Claude sous un plafond de proposeur de 3,00 USD et de juge de 1,00 USD : estimations du devis v6, par jetons.
- Le cadre de 500 caractères autour de la carte servie au juge est supposé ; l'entrée réelle est comptée par la commande avant l'envoi.
- Ce que la clé LUC peut payer : son solde n'est pas lu (GO-2026-11-22-124) ; le délai de sa recharge automatique, le montant de chaque recharge et ce qu'elle fait quand le solde est déjà sous son seuil de 5 USD ne sont dans aucune pièce lue (§ 5 bis).

## 8. Comparaison : les bornes des v6 à v10, et la page jusqu'au 30 novembre

| grandeur | prix déclarés (4 et 20) | bornes des v6 à v10 (8,3 et 41,5) | page jusqu'au 30 novembre (2 et 10) |
|---|---|---|---|
| pire cas d'un appel de juge d'Argon, provision en plus du plafond de sortie | 0,9985 | 2,0718 | 0,4992 |
| plafond de session des juges qui en découle, au dixième | **1,00** | 2,10 | 0,50 |
| borne des plafonds de session | 600 | 952 | — |
| Carbon, par appel estimé ; poste | 0,4805 ; 7,688 | 0,9970 ; 15,952 | — |
| Carbon, pire cas à 65 536 de plafond et 49 152 de provision, provision en plus | 2,3042 | 4,7813 (au-dessus de 3,00) | 1,1521 |
| proposeur Argon ; juge Argon (sans réflexion) | 2,128 ; 2,676 | 4,416 ; 5,552 | — |
| sous-total sans la réflexion d'Argon ; avec la marge de 10 % | **35,683 ; 39,25** | 49,112 ; 54,02 | 29,438 ; 32,38 |
| réflexion d'Argon, par millier de jetons moyens par appel | 3,52 | 7,30 | 1,76 |
| sous-total si Argon réfléchit 16 384 jetons à chaque appel | 93,36 | 168,78 (coupé) | 58,27 |
| réflexion moyenne par appel d'Argon au-delà de laquelle le sous-total passe 150 USD | 32 476 jetons | 13 812 jetons | 68 501 jetons |

Les bornes (commande d'Argon des v6 à v10, l. 345-346, et son enveloppe `rapports/fille-ideation-1-v1/appel-argon-v5.sh`, `37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a`, l. 29 ; pour Carbon, bornes hautes de R-3271 citées par le préenregistrement v10, § Espèces) valent 2,075 fois les prix déclarés et 4,15 fois les prix de la page jusqu'au 30 novembre. Aux bornes, la course pouvait être coupée « pour budget » par la seule réflexion d'Argon (13 812 jetons de moyenne ; 13 140 avec les marges ; juges à 11,47 USD sans elle), alors que la dépense facturée serait restée deux à quatre fois plus basse ; la mesure préalable de cette réflexion, envisagée un temps, est sans objet aux prix déclarés (R-5018).
