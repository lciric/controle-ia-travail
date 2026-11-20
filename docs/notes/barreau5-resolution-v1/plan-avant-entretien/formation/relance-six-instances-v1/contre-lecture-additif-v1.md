# Contre-lecture de l'additif 1 « relance des six instances » (barreau 5) — v1

Pièce lue : `additif-1-relance-six-instances-v1.md`, sha256 491b60d43a8573fa5db8e9c9d76f2268210df6f892a4d51ae0743f5e42649e73 (vérifiée, égale). Lu aussi : le mandat, les extraits permis du texte scellé, le rapport du développeur, le différentiel (sha256 8e8c927c…a7e033a3, égal au rapport), la ligne GO-2026-11-20-51. Rien d'autre.

**Verdict : scellable après ces couples** (deux bloquants, faciles à lever ; le code v2 dit la même chose que l'additif sur tous les points que l'additif lui confie).

Vérifié et juste : H + 30 = 2026-11-21T07:30:16Z, H + 54 = 2026-11-22T07:30:16Z, H + 65 = 2026-11-22T18:30:16Z (H = 2026-11-20T01:30:16Z) ; 5 × 26 + 17 = 147 ; 200 − 147 − 7,02 = 45,98 ; 5,4 × 1,30 = 7,02 ; contenu « commit <40 signes> » lu à la lettre par le code ; ordre GO-FORMATION < CODE-RELANCE < GO-RELANCE tenu strictement par le code ; accord de la ligne de relance égal à celui de GO-FORMATION-B5F ; six instances et 147 dollars au plus ; plafond commun appliqué à une relance ; première marche comparée au code v1, relance au code v2, sur l'instance et à la commande ; entropie et graines inchangées.

## Couples

**1. Les premières copies des instances tombées ne sont pas « versées ».**
Constat : § 3, tiret « La lecture de la seule copie -x1 », dit « Les premières copies des instances 1, 2, 3, 4, 5 et 7 sont versées, inventoriées ». Or, par GO-2026-11-20-51 point 2 (option a), leurs disques ont été inventoriés par les seules commandes du loueur, inventaire versé, puis détruits par identifiant : le contenu des disques n'a pas été versé. Seul ce qui avait été poussé sur leurs branches de sortie avant l'arrêt existe. Le texte scellé dit « La première copie est versée » et « Aucune sortie n'est supprimée avant son versement » : c'est un écart, accordé par Lazar, que l'additif doit écrire au lieu d'affirmer le contraire.
Correction : remplacer la phrase par « Pour les instances 1, 2, 3, 4, 5 et 7, ce que leurs premières marches avaient poussé sur leurs branches de sortie est gardé, jamais lu ni noté ; leurs disques ont été inventoriés par les seules commandes du loueur, l'inventaire versé, puis détruits par identifiant (`GO-2026-11-20-51`, point 2 : écart accordé à « la première copie est versée » et à « aucune sortie n'est supprimée avant son versement ») ». Ajouter en § 1 : « Leurs disques ont été inventoriés puis détruits (GO-2026-11-20-51, point 2). » Et en § 2, une ligne C8 qui nomme cet écart.
Gravité : bloquant.

**2. Le § 6 fait du code v2 lui-même un nœud.**
Constat : § 6 range en nœud « tout changement du code autre que ceux de la section 2 ». Le code v2 change aussi `MIN_ESSAIS` de l'amorce (235 → 242), forcé par un essai d'égalité, les commentaires du lanceur, et des essais retouchés. Aucun n'est dans la section 2. Lu à la lettre, l'additif scellé rend la ligne `CODE-RELANCE-FORMATION-B5F` contraire à lui-même.
Correction : en C5, après « plus les seuls changements que cet additif exige », ajouter « , avec les essais qui les éprouvent, le plancher d'essais de l'amorce que leur nombre force, et les commentaires qui les décrivent ». En § 6, écrire « tout changement du code autre que ceux de la section 2 et de leurs suites nommées en C5 ».
Gravité : bloquant.

**3. La réserve de la relecture ne suffit pas, et la répétition peut couper une relance.**
Constat : la règle de C4 réserve 7,02 dollars, le coût estimé de 5,4 heures. Or le garde s'arrête dès que « cumul plus un quart d'heure » atteint le plafond. Avec exactement 7,02 dollars, la relecture s'arrête vers 5,15 heures, avant la fin : l'étape décisive serait coupée. Ensuite, la règle ne s'applique qu'à l'inscription de la ligne. Rien n'empêche ensuite une répétition générale, ou le stockage, de manger la part des relances pendant qu'elles tournent. Le plafond atteint arrêterait alors une relance (C4). Enfin, 5,4 heures et 1,30 dollar de l'heure ne renvoient à aucun chemin ni à aucune empreinte (R6). Le rapport le dit : le devis n'a pas été lu.
Correction : remplacer « plus 7,02 dollars gardés pour la relecture (5,4 heures d'une carte à 1,30 dollar de l'heure au plus) » par « plus la coupure de la relecture fixée par le devis (chemin, empreinte, section citée), quart d'heure compris », et recalculer le seuil. Ajouter : « Tant qu'une relance est à créer ou en cours, aucune autre pièce (répétition générale, stockage) ne part si le cumul relevé, plus les coupures restantes des relances, plus la réserve de la relecture, plus la coupure de cette pièce, dépasse 200 dollars. » Supprimer « et le stockage » de la dernière phrase de C4, ou écrire « si le stockage est compté sous ce plafond ». Le prix du volume relève du nœud de GO-2026-11-19-88.
Gravité : important.

**4. Ce que l'additif impute à Lazar est la lecture de la mère, et « go 30 usd » n'est pas lu.**
Constat : les mots de Lazar consignés dans GO-2026-11-20-51 sont « go a pour les disques, go 30 usd; c'est bon j'ai de quoi tout recharger j'ai 200 euros relance les instances ». « Sous le plafond commun de 200 USD » et « avant la fin des créations » sont la rédaction de la mère, non les mots de Lazar. « go 30 usd » n'est repris nulle part dans la décision. Si ces mots bornaient la relance, 147 dollars de coupures les dépasseraient. C7 dit déjà « tel que la session mère le relaie » ; C4 et l'en-tête ne le disent pas.
Correction : dans l'en-tête « Autorité » et en C4, écrire « tel que le consigne la session mère dans la ligne GO-2026-11-20-51 ». Avant le scellement, la mère confirme dans une ligne ce que couvre « go 30 usd » (autre accord, nommé), et l'additif ajoute en § 1 : « « go 30 usd » porte sur <objet>, étranger à la relance. » Si ces mots portent sur la relance : nœud.
Gravité : important.

**5. La ligne de relance doit précéder la première création, donc H + 30, et non H + 54.**
Constat : C7 impose la création des relances avant H + 30. Le code exige la ligne `GO-RELANCE-FORMATION-B5F` au registre du commit de course avant toute commande de relance. Or § 3 et § 4 (point 3) disent encore « au plus tard à H + 54 heures ». Inscrite entre H + 30 et H + 54, la ligne serait légale, mais aucune relance ne pourrait plus partir, et seule la copie `-x1`, inexistante, serait lue.
Correction : au § 4, point 3, écrire « inscrite par la session mère avant la création de la première relance, donc avant H + 30 heures (2026-11-21T07:30:16Z) ; la borne de H + 54 heures du texte reste, sans effet ici ». Même phrase au § 3, tiret « Les échéances ».
Gravité : important.

**6. Les passages remplacés du point 14 et de la borne de la relance ne sont pas écrits.**
Constat : C4 n'annule qu'une phrase du point 14. Mais « les pièces du devis s'arrêtent toutes à son plafond, que leur seule dépense compte » change aussi de sens. D'autres passages changent de même : le paragraphe « Borne de la relance » (« n'entre pas sous le plafond du devis », « pas de troisième compteur », « le plafond atteint arrête les pièces du devis, non une relance en cours », « chaque relance porte la ligne GO-RELANCE-FORMATION-B5F, qui cite cet accord [GO-2026-11-19-87] »), et la phrase de « Calcul et dépense » « à part, une enveloppe de relance de 56 USD au plus ». L'en-tête dit que l'additif « prime sur les seuls points listés à la section 2 » : ces passages doivent y être nommés.
Correction : ajouter en fin de § 2 une table « passage du texte → point de l'additif », et le nouveau libellé du point 14 : « Dépense : chaque instance, relances comprises, s'arrête dès que son cumul relevé plus un quart d'heure atteint sa coupure ; les pièces du devis et les relances s'arrêtent toutes au plafond commun, que leur dépense à toutes compte ; arrêt et destruction par identifiant (R10), après versement de ce qui est récupérable. » Corriger en conséquence, au § 3, « liste d'arrêt hors de la phrase du point 14 citée en C4 » en « hors du point 14, réécrit en § 2 ».
Gravité : important.

**7. C5 et C1 sont des écarts au texte scellé qui ne sont pas des mots de Lazar.**
Constat : GO-2026-11-20-51 accorde l'écart « deux instances au plus » et la relance sous le plafond. Il ne dit rien des autres écarts : une clé neuve au registre, le code changé après « ne changent plus après la vérification de ce brouillon », ni « tombée » étendue à l'arrêt faute de crédit. Ce sont des suites nécessaires, mais un écart à un préenregistrement scellé est un nœud.
Correction : ajouter en tête du § 2 : « C1, C5 et C6 sont les suites nécessaires de l'exécution de GO-2026-11-20-51, non des décisions propres de Lazar ; la session mère les lui porte, une ligne chacune, avec l'additif scellé. »
Gravité : important.

**8. C1 pose une règle générale plus étroite que nécessaire.**
Constat : « arrêt … faute de crédit, avant qu'une famille soit formée » fait dépendre la qualification d'un état de sortie (une famille formée ou non). C'est inutile ici, puisque la relance est entière et que seule la copie `-x1` est lue, et c'est hors de la portée annoncée (« la relance, et rien d'autre »).
Correction : écrire « Les instances 1, 2, 3, 4, 5 et 7, arrêtées le 20 novembre 2026 à 12:12Z faute de crédit chez le loueur, sont tombées au sens de la règle de la relance ; l'arrêt faute de crédit est une cause qui ne lit aucune sortie. » Retirer « avant qu'une famille soit formée ».
Gravité : mineur.

**9. Le contenu exact de la ligne de relance n'est tenu par personne de nommé.**
Constat : le code borne le compte et la somme, mais accepte par exemple « 6,1,2,3,4 » (132 dollars) ou « 6,7 » (rapport, point 8). Le § 5 ne confie pas à la session le contenu exact.
Correction : au § 5, sous « La session de formation et la session mère », ajouter « le contenu exact de la ligne de relance, `GO-2026-11-19-86 ; instances 1,2,3,4,5,7`, sans l'instance 6, que le code ne vérifie pas ».
Gravité : mineur.

**10. La validité de l'accord de calcul n'est pas vérifiée d'avance.**
Constat : toutes les relances sont créées sous `GO_ID=GO-2026-11-19-86`. Si la ligne de cet accord porte une échéance antérieure au 21 novembre à 07:30:16Z, la garde de calcul refusera les dernières créations.
Correction : au § 5, ajouter pour la session « vérifie, avant d'inscrire la ligne de relance, que GO-2026-11-19-86 est en vigueur jusqu'à la dernière création ; sinon, nœud ».
Gravité : mineur.

**11. Les lectures déclarées sont incomplètes, et les chiffres d'appui ne renvoient à rien.**
Constat : « Ce que le rédacteur a lu » omet ce que le rapport déclare avoir lu : `engagement_v1.py`, la définition de `CHEMINS_GELES` dans `harnais/validation_reelle.py`, les essais du lanceur et des amorces, et une liste de noms de fichiers. Les « environ 18,5 dollars » ne renvoient à aucune ligne du registre des dépenses (R6). H n'est pas écrite.
Correction : ajouter à « Ce que le rédacteur a lu » : « et les fichiers de code de la même chaîne listés au rapport du développeur, § 8, point 1 ». Citer la ligne du registre des dépenses pour 18,5 dollars. Écrire en § 3 « H = 2026-11-20T01:30:16Z, création de l'instance 6 ».
Gravité : mineur.

**12. Le chemin de scellement de l'additif et le nom des fichiers ne sont pas fixés.**
Constat : l'additif ne dit pas sous quel chemin il est scellé. Le commit de course, qui ne diffère du code v2 que par `registres/`, ne le contiendra pas. Le code v2 garde les noms « v1 » des fichiers, ce que la règle des noms versionnés (R12) peut contester (rapport, point 2).
Correction : écrire en tête « scellé sous `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-additif-1-relance-six-instances-v1.md` (ou le nom choisi par la mère) ; le code ne le lit pas ; la ligne CODE-RELANCE-FORMATION-B5F en cite le chemin et l'empreinte ». Ajouter en C5 : « La version du code est portée par le commit et la clé neuve ; les noms de fichiers restent ceux du code des premières marches. »
Gravité : mineur.
