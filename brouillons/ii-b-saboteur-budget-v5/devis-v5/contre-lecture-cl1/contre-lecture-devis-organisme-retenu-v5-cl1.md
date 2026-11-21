# Contre-lecture 1 du devis de l'étalonnage et de la course de l'organisme retenu (v5)

Écrite le 2026-11-21 par un contre-lecteur neuf (Claude Opus 5.5, côté saboteur). Mandat : `registres/iib-reconception/mandat-contre-lecteur-devis-organisme-retenu-v5-v1.md` (35860e22e161…, vérifié). Pièce : `brouillons/ii-b-saboteur-budget-v5/devis-v5/devis-ii-b-v5-brouillon1.md`, `calcul-devis-ii-b-v5.py`, `sortie-calcul-devis-ii-b-v5.txt` (compagnons vérifiés). Texte scellé : `conception-organisme-retenu-ii-b-v5-scellee-v1.md` (c1dc54597a1a…, vérifié).

## Verdict : remettable après corrections

Aucun bloquant ; trois majeurs, neuf mineurs. Arithmétique exacte : le script rejoué rend sa sortie à l'octet (`rejeu.txt`). Comptes d'appels conformes au texte scellé. Durées et prix réels bien lus.

## Ce qui a été vérifié

- Rejeu : `python3 -I -B calcul-devis-ii-b-v5.py` : sortie identique à la sortie versée.
- Comptes (section 12, 10.1, nœud 7 (b')) : étalonnage 160 épisodes générés (64 + 64 + 32 ; plantés non générés) et 3 840 actions d'oracle ; par tour 32 épisodes et 320 actions d'un seul oracle ; hors tours 3 520 (960 + 2 560) ; évaluation 256 épisodes et 2 560 actions de l'oracle désigné ; 12 tours : 800 épisodes et 13 760 actions, chiffre même de la section 12 sous (b') ; 24 tours : 1 184 et 17 600 (14 080 + 3 520). Formule du plafond de tours conforme à 10.2 sous (b').
- Première course (branche `origin/claude/iib-executante-v1`, durées, prix, dépense seulement) : douze marques de progrès 09:08:15 à 10:05:34, fin de l'oracle 10:13:45, 960 actions ; prix 1,186667 + 0,033333 (surveillance, ligne 1) ; 4 835,89 s facturées à 10:14:26, arrêt 10:14:33, destruction 10:20:55 ; une seule instance créée (les tentatives antérieures n'ont rien créé). Bornes de l'ordre de la première course : 1,30 + 0,08 dollar par heure, 0,05 par gigaoctet, 40 gigaoctets prévus pour la minuterie, consignation 2 400 s.
- Ligne GO-2026-11-21-66 sur `origin/main` : « ligne de calcul neuve de l'étalonnage puis de la course : go, plafond inscrit sur le devis remis après scellement » ; aucune échéance écrite.
- Sondage de douze chiffres, recalculés indépendamment (`sondage-chiffres-devis-v5-cl1.py`, sortie `sortie-sondage-chiffres-devis-v5-cl1.txt`) : 39,08 s ; 0,511 s ; 550 s de fixe ; 2,44 h et 2,97 dollars d'étalonnage ; 3 840, 13 760, 17 600 actions ; 800 et 1 184 épisodes ; 0,479 dollar par tour ; coût fixe 4,33 (6,33 avec le téléchargement) ; 83 et 94 tours ; 59,76 tenus par les gardes ; 43,4 et 38,4 h sous la coupure ; 1,64 dollar de la première course. Tous conformes.
- Marges du pire : × 2 sur tout (hôte), × 1,5 de plus sur l'oracle (deux oracles jamais chronométrés), × 3 sur le fixe : justifiées par ce qui est mesuré (écart des lots + 16 %, une seule machine vue) ; le pire de l'oracle (1,53 s) reste sous celui du premier devis (3,0 s), ce qui est cohérent avec 0,511 s mesuré.

## Remarques majeures

**M1. Le dépassement du plafond de tours est réglé par le texte, que le devis renvoie à vérifier (§ 6).** 10.3, étape 6 : R > R_plafond donne « ne part pas, motif tours » pour cet oracle, calculé une fois, par programme, avant toute configuration de course. Par 5.1 : si c'est [N], la règle passe à [P] ; si c'est [P] (ou les deux), la course ne part pas, phrase de 10.6, résultats versés et scellés. Il n'y a donc pas de course qui « dépasse » le plafond de tours : une course partie a R ≤ R_plafond, et aucun tour n'est ajouté (section 15). *Correction* : écrire ces deux phrases au § 6 à la place du renvoi ; garder le paragraphe sur la dépense (réserve, minuterie, arrêt par identifiant, versement).

**M2. La réserve de 5 dollars est mince devant ce que la formule laisse faire.** Le plafond de tours se calcule sur les durées de l'étalonnage, c'est-à-dire sur l'agent honnête ; les épisodes du maître (consigne privée dans le contexte) n'ont aucune durée mesurée. Avec le fichier d'entrées à 50 et les durées attendues, la course peut aller à 83 tours, soit environ 49,7 dollars planifiés : les tours ne peuvent alors être que **13 % plus lents** que mesuré avant que la minuterie ne coupe à 55, c'est-à-dire avant la distillation et l'évaluation, et la course est perdue [sondage S11]. *Correction proposée* : plafond du fichier d'entrées à **45** (73 tours au plus, tolérance 29 %, k_R ≥ 6 au lieu de 5) ; ou 50 avec un coût fixe pris au pire (12,29), qui donne une tolérance voisine. Le dire dans le devis, avec la tolérance chiffrée.

**M3. Le « total au pire » de la ligne (§ 0, 53,4 dollars) n'est pas le pire de la ligne.** Il vaut pour 24 tours ; or la course peut aller jusqu'au plafond de tours, et le devis lui-même dit 39 h de location à ce plafond. Le pire de la ligne est celui que tiennent les gardes : 59,76 dollars [L39]. *Correction* : une ligne au § 0 : « au pire, la ligne entière est bornée par les gardes à 59,76 dollars ; 53,4 est le pire d'une course de 24 tours ».

## Remarques mineures

- **m1.** La ligne « 6 tours » (§ 4, [L24] [L27] [L30], [L46]) n'est pas une configuration possible : 10.3, étape 7, fait partir « à la taille d'origine » (12 tours) dès que R ≤ 12. Le moins possible est 12 tours. *Correction* : retirer la ligne ou la marquer « inaccessible » ; récrire [L46].
- **m2.** Le coût fixe, le prix horaire et le plafond sont des **nombres** du fichier d'entrées scellé avant l'étalonnage (10.2) ; le devis ne donne pas le nombre du coût fixe ni le jeu de durées dont il sort (6,33 attendu, 12,29 au pire). *Correction* : l'écrire (voir M2).
- **m3.** 10.2 écrit « la durée d'une action d'oracle » au singulier ; sous (b'), l'oracle désigné joue par tour et l'autre hors tours, et les deux n'ont pas forcément la même durée. *Correction* : dire dans le devis (et pour l'ordre neuf) que le programme prend la plus longue des deux durées mesurées ; ce n'est pas un écart au texte.
- **m4.** Lecture des marques de progrès : si la marque « lot n » s'écrit au début du lot et non à la fin, le chargement vaut 543 s et l'action d'oracle environ 0,19 s ; la moyenne d'un épisode ne change pas. La lecture du devis est la prudente pour l'oracle ; le dire en une phrase.
- **m5.** Coupure propre de l'étalonnage (12, plafond 17) : bien posée, mais elle demande de toucher à la minuterie, code revu. *Correction proposée* : une règle de la surveillance (alerte à 12 dollars avant la fin de l'étalonnage, arrêt par identifiant, nœud) plutôt qu'une ligne de code ; « 17 » se lit alors comme la dépense tenue si la course ne part pas, non comme une seconde ligne.
- **m6.** La ligne neuve n'a pas d'échéance écrite (GO-2026-11-21-66) ; la minuterie en demande une. *Correction* : proposer une échéance et l'échéance de la minuterie (au moins deux jours de location plus 48 h d'arrêt après la création), point pour Lazar.
- **m7.** `fixe_course_s` ajoute 36 s sans commentaire (le 0,01 h de la distillation du premier devis) ; le commenter.
- **m8.** L'heure de création retenue (08:53:52) diffère de l'époque de la surveillance (1795078446 = 08:54:06) ; la facturation commence vers 08:53:50 (4 835,89 s à 10:14:26). Quatorze secondes, sans effet ; corriger le commentaire « époque 1795078446 » du script.
- **m9.** L'en-tête dit que le registre des accords n'a pas été ouvert : le contre-lecteur l'a lu sur `origin/main` ; la ligne dit bien « plafond inscrit sur le devis » ; on peut citer la ligne.

## Les quatre choix rendus par le rédacteur

| choix | bien posé ? | recommandation |
|---|---|---|
| plafond 60, coupure 55 | oui : 59,76 tenus par les gardes, 51 h d'arrêt au plus, même forme que la première ligne | **garder**, confiance forte |
| coupure propre de l'étalonnage (12 ; 17) | oui sur le chiffre ; non chiffré sur sa mise en œuvre | **règle de la surveillance**, non une ligne de code (m5), confiance moyenne |
| fichier d'entrées à 50 | oui, mais la tolérance n'est pas dite | **45** (ou 50 avec coût fixe au pire), tolérance écrite (M2), confiance moyenne |
| dépense passée 0 | oui : la première course est sur GO-2026-11-10-08 ; l'étalonnage est déduit à part par la formule | **0**, en y ajoutant toute dépense de la ligne neuve antérieure à la location (création manquée), confiance forte |

## Fichiers rendus

`contre-lecture-devis-organisme-retenu-v5-cl1.md`, `sondage-chiffres-devis-v5-cl1.py`, `sortie-sondage-chiffres-devis-v5-cl1.txt`, `rejeu.txt`, chacun avec son compagnon `.sha256`. Rien d'autre n'a été lu de la première course que durées, prix et dépense ; aucune pièce côté sondes ; aucune donnée mesurée.
