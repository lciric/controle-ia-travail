# Contre-lecture du code de l'étage sur processeur, palier 0b, version 2 — v1

Pièce de travail (classe C). Contre-lecteur, modèle S, neuf. Mandat : `mandat-contre-lecteur-code-palier-0b-v2-v1.md` (`f9f9aaa5…`, empreinte vérifiée par son compagnon). Textes vérifiés par empreinte avant lecture : préenregistrement v6 (`4aee136b…`, OK), rapport du développeur (`ca61bf7e…`, OK), six modules du code (compagnons OK : mondes, audit, proposeurs, mecanique, statistique, registre). Code lu en entier : les 23 modules de `heritage_etage_processeur_v1/`, les tests `gardes`, `mondes`, `mecanique`, `outils`, `etapes`, `zz`, des passages de `statistique` et d'`organisme`, `outils-dev/mutations_v1.py`, `diagnostic_conflits_etrangers.py`. Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille joué par moi ; aucune écriture dans le dépôt ; aucun refus d'outil.

## 0. Verdict

**Conforme après corrections.** Le code suit l'annexe C et B1 à B9 sans écart de logique trouvé ; la suite passe (70 sur 70) ; le défaut du bras 4b est corrigé et son défaut réintroduit est vu. Trois corrections de détail (§ 4), aucune ne touche un critère, un seuil ou une valeur gelée. Les trois écarts du développeur sont de vraies questions de texte ou de conception, non des défauts du code ; l'un d'eux (B7 bis à la dose 0,5) est plus grave que le rapport ne le dit (§ 5).

## 1. Essais passés et échoués chez moi (copie dans mon dossier, `PYTHONPATH=src`, variables `HERITAGE_DEPOT` et `HERITAGE_COPIE_ORGANISME` sur la copie du commit 94bfd92 du dépôt)

- Suite entière, une commande : **70 passés, 0 échoué, 766 s.** Identique au rapport.
- Fichier par fichier, un par appel : `mecanique` 8 passés (293 s) ; `gardes` 17 (29 s) ; `outils` 15 ; `mondes` 9 (321 s) ; `statistique` 10 ; `etapes` 5 ; `organisme` 5 (126 s) ; `zz_aucune_graine_decisive` : **1 ÉCHOUÉ quand il est lancé seul** (voir correction C1) ; 8+17+15+9+10+5+5 = 69, plus 1 = 70, comme en suite entière où il passe.
- Banc des défauts `mutations_v1.py` rejoué sur ma copie, **non terminé à l'heure de la remise** : les 34 premiers défauts sur 41 (jusqu'à « organisme-elimine-tient » inclus, dont les gardes 2 à 27 hors S8) sont tous appliqués et tous **vus** ; restaient en cours les 7 derniers (S8 (i), S8 (ii), graines des bras, M10, S9, « atteint », sorties non vérifiées), dont les essais sont lourds ; leur résultat n'est donc pas confirmé par moi (celui du développeur : 41 sur 41, témoins au vert, `mutations-sortie-v2.json` : `defauts_vus` 41, `temoins_tous_au_vert` vrai ; mes témoins ont été verts aussi, sans quoi le banc n'aurait pas joué de défaut)
- Contrôles à moi : diagnostic des conflits face à la source étrangère rejoué (dose 0,5, 12 tours) : probabilité moyenne d'un tour sans conflit 0,19 (ordre des rangs) et 0,084 (deux ordres), dans la fourchette du rapport (0,013 à 0,086) ; bruit de l'exactitude de forme sous le nul, calcul à moi (`outils-cl/bruit_nul_doses.py`, graines locales, aucune couche du dispositif) : voir § 5.3.

## 2. Ce que j'ai vérifié, point du mandat par point

1. **Annexe C et gardes de B9.** Lu garde par garde : les 27 ont un essai avec cas sain et artefact (table du rapport § 2 exacte, sauf la réserve de la correction C2 sur la garde 27 au bras 4b). Strate vide : `exiger_strates` et `_f` arrêtent ; aucun repli silencieux trouvé (la sur-sévérité de la correction C3 va dans le sens de l'arrêt). Générateur (B1 a à e), forme unique, partage servi/épreuve, comparateur sans juge, exécuteur à forme imposée et contre-calcul, retrait v1 et v2 (vectorisé identique au séquentiel, testé), règles de Holm, Pratt (rangs doublés), unilatéral, Clopper-Pearson (inversions correctes), règle de confirmation (5 236), S7, S9, M10, n, m, plan des 72 cases de C1 et de C4, familles A à H : conformes au texte.
2. **Bras 4b.** `est_de_la_continuation` exige origine, source et bras ; `propre_servi` vaut zéro au 4b dans la couche statistique ; le registre servi au 4b est celui du bras 2 d'une autre source, donc aucune entrée « de sa continuation ». Défaut réintroduit (« tenue-sur-entrees-etrangeres ») : vu chez moi (41,3 s).
3. **Graines.** `SeedSequence(2026111902, spawn_key=quatre mots de SHA-256 de l'étiquette)` ; couches « decisif » et « confirmation » refusées sans `Autorisation` (deux verrous : `Graines.sequence` et `exiger_autorisation_pour`, avant tout dossier) ; essai final au vert en suite entière.
4. **Suite et banc** : § 1.
5. **Les trois écarts** : § 5.
6. **Les quatorze silences** : § 6.
7. **Rien de décisif** : le journal des graines de la suite ne contient que « essai » et « essai-de-forme » ; refus consignés tous décisifs (test `zz`, en suite entière).

## 3. Défauts vus

Aucun défaut de logique qui change un résultat. Réserves de code, par gravité décroissante :

- **D1 (essai).** `tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py`, ligne 14 : `assert GR.REFUS and all(...)` échoue quand le fichier est joué seul (aucun refus consigné), alors que le mandat et le rapport demandent chaque fichier un par appel. Il ne vaut que joué après les autres essais du même processus. Sans gravité pour la porte, mais l'essai est faux en solo.
- **D2 (garde 27).** `registre.verifier_registre_etranger` ne dit rien du bras 4b : la copie servie au 4b (`vues_etrangeres_4b`, mécanique `jouer_source`) n'a ni empreinte ni vérification ; servir au 4b le registre propre du bras 2 (ce serait le bras 2) ne serait vu par aucun essai, et le banc de 41 défauts n'en contient pas. Le texte (B9, 27) ne cite pas d'artefact au 4b ; mais B7 bis veut que « son empreinte est celle du registre de la source étrangère ».
- **D3 (couche statistique).** `statistique.Mondes.__init__` tire `p_passage_vraie` (via `_f`) dès que la dose est non nulle, pour tout proposeur, alors que `frequences.strates_requises` ne l'exige que d'un lecteur aux bras 3 ou 4a. Un sourd à dose non nulle serait donc arrêté par une strate vide dont il n'a pas besoin ; c'est dans le sens de l'arrêt, pas un repli, mais les deux fonctions se contredisent.
- **D4 (analyse).** `analyse.table_des_criteres` : une garde absente du dictionnaire `gardes` n'est pas comptée en échec ni « non établie » (seule la 17 est traitée). Une table incomplète passerait « C6 tenu ».
- **D5 (résistance).** `rangs_signes._loi_exacte` : `lru_cache(maxsize=200_000)` de deux tableaux de plusieurs milliers d'entiers par entrée : jusqu'à de l'ordre de 8 Go de mémoire à 48 sources si les 200 000 places se remplissent. À regarder à l'essai de forme (temps), qui ne mesure pas la mémoire.
- **D6 (graines).** `graines.Autorisation` ne compare pas l'empreinte du préenregistrement à `PREENREGISTREMENT_SHA256` des constantes : tout texte doté d'un compagnon et d'un erratum qui cite son empreinte ouvre la couche décisive ; elle ne peut pas non plus vérifier que l'erratum est « contre-lu ».
- **D7 (jeu B7 bis).** `mondes.generer_jeu_avec_etrangeres` perd les compteurs de génération des sources du jeu (B1 (iii) n'y est pas rapporté).
- **D8 (étalonnage).** `etalonnage.etalonner` : une taille « nan » (écart-type entre jumelles nul) tombe dans « non atteignable » au lieu d'arrêter.
- **D9 (audit).** `audit.exactitude_equilibree` : plis non stratifiés ; une classe rare peut manquer d'un pli d'entraînement (moyenne vide, `nan`, `argmin` silencieux). Sans effet aux tailles prévues.

## 4. Corrections demandées (« Conforme après corrections »)

- **C1.** `tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py`, ligne 14 : retirer `GR.REFUS and` (ou provoquer un refus dans l'essai) pour que le fichier passe seul sans perdre son sens.
- **C2.** `registre.py`, `verifier_registre_etranger` (l. 255-269) et `mecanique.py`, `jouer_source` (l. 282-287) : au bras 4b, comparer l'empreinte canonique de chaque vue servie à celle de la vue correspondante du bras 2 de la source étrangère (copie scellée déposée avec son empreinte), avec un artefact (registre propre servi au 4b : arrêt) et l'ajouter au banc.
- **C3.** `statistique.py`, l. 54 : n'exiger `p_passage_vraie` que si `strates_requises` l'exige (aligner les deux).
- D4 à D9 : consigner ; pas bloquant. D4 se corrige en une ligne (comparer à l'ensemble attendu des gardes 1 à 27).

## 5. Les trois écarts : ce que chacun demande avant le scellement

**5.1 — B7 bis à la dose 0,5 : question de texte, plus grave que décrite.** Le code arrête comme la liste d'arrêt (point 2) le veut ; ce n'est pas un défaut. Mon rejeu du diagnostic donne un tour sans conflit à 8 % (deux ordres). Mais l'estimation du rapport est par source étrangère fixée et sur un seul jeu d'instances d'oracle ; la recherche réelle est couplée : quand la suite k échoue, la source k change et la suite k − 1 doit être refaite contre la nouvelle source (`generer_jeu_avec_etrangeres`, l. 433-440), sur un cycle de sources. Il faut une compatibilité simultanée de S paires ordonnées, chacune à quelques pour cent : l'effort croît comme une puissance de 1/p, la borne `tours × S` s'épuise (l'essai à trois sources l'a vu). Et chaque monde a son propre oracle : ses conflits diffèrent d'un monde à l'autre. Avant scellement, un erratum doit trancher, au choix : (a) **fixer la dose du jeu de la garde 27 à 0,25** (recommandé : la garde 27 ne contrôle que des registres servis, la dose n'y est pas en cause ; la famille H en couche statistique n'écrit aucune loi et joue la dose 0,5 sans cette marge) et dire que la marge face à la source étrangère n'est pas revendiquée à 0,5 sur la couche mécanique ; (b) restreindre la marge étrangère aux lois indépendantes et fausses, et rapporter celle des dépendantes ; (c) élargir les bornes (déconseillé : coût non borné). Et corriger la réserve 20 : ce point est maintenant éprouvé et il échoue à 0,5.

**5.2 — Audit de présentation, traits de forme : question de conception, et l'arrêt à pleine taille est probable.** Mes recoupements confirment la cause décrite : `audit.jetons` absorbe le signe moins dans le jeton « nombre » (nombre à quatre décimales ou plus) ; seule la longueur du texte en garde la trace ; le filtre sévère des sous-lois de la source change la répartition des signes des lois dépendantes. Les chiffres du développeur sont cohérents : différence de 0,76 caractère pour un écart-type voisin de 2,4 (nombre de signes d'une loi), soit d de l'ordre de 0,3 et une exactitude de l'ordre de 0,56 ; à 50 suites par dose (environ 1 800 lois dépendantes contre 3 000 indépendantes) l'incertitude est de l'ordre de 0,01 : un effet de 0,56 y dépasserait 0,55 de façon stable, pas par hasard. Ce n'est pas un défaut de code : « la longueur du texte » est dans le texte. Mais le texte appelle « forme » un trait qui lit le contenu (le signe). Il faut avant scellement : (a) un erratum qui définit la longueur sur le texte où chaque nombre est remplacé par son jeton (le signe relevant du contenu, déjà lu par les traits de contenu, rapportés sans arrêt) ; ou (b) rendre aux lois indépendantes le même filtre que les sous-lois de la source (changement du dessin gelé, plus lourd). Je recommande (a).

**5.3 — Bruit de l'audit des doses par paires : question de conception, chiffrable.** Mon calcul sous le nul (traits gaussiens indépendants, 65 traits, plus proche centre, cinq plis, 1 000 répétitions) : à 200 mondes contre 200 (une paire de doses à 50 suites par dose, quatre mondes par suite), **moyenne 0,500, écart-type 0,032 (et non 0,025), 4,8 % des audits au-dessus de 0,55** ; à 400 contre 400, écart-type 0,023 et 1,1 %. Trois paires de doses lues sur les traits de forme : un générateur parfait déclenche l'arrêt avec une probabilité de l'ordre de 11 à 14 % (trois lectures proches de 4,8 % chacune, partiellement corrélées). La règle « chacune au plus 0,55 » sans autre précaution est donc mal calibrée. Avant scellement : un erratum fixe la règle (au choix : moyenne de l'exactitude sur de nombreux plis aléatoires avec seuil sur la borne basse d'un intervalle à 95 %, ou 0,55 plus deux écarts-types du nul calculés sur permutation des étiquettes, ou plus de suites par dose) ; sans cela, un arrêt de l'étape 3 ne dira rien du générateur.

## 6. Les quatorze choix de la § 4 du rapport

1. Un lot, un domaine : silence réel (B4 dit « lots de douze au plus » sans parler de domaine) ; compatible avec le test de la garde 14 ; à inscrire.
2. Garde 17 : identifiants opaques, doublure « rien envoyé » pour les échecs, bouchon pour scipy : silence réel, repris du palier 0a.
3. B7 bis « dans les deux sens » : **pas un silence** : les deux ordres de composition sont dans B7 bis et la plus petite des deux divergences est la définition de la séparation (section Seuil). Le développeur n'a rien choisi ; à dire ainsi.
4. Dose du jeu de la garde 27 : silence réel : c'est l'écart 5.1.
5. S8 (ii), estimation de l'intervalle : silence réel, raisonnable (rééchantillonnage de 20 000 moyennes).
6. Étalonnage (40 pas, non convergé arrête, écarts-types aux taux 0 et 0,5) : silence réel ; voir D8.
7. Génération finale, même règle et même budget : silence réel, cohérent avec B6.
8. M12, une loi engagée par plusieurs bras compte une fois, origine de la première tentative dans l'ordre des bras joués : la règle par tentative est écrite (annexe F, point 4), l'ordre entre bras est un silence réel, sans effet attendu sur M1.
9. Graines, champ `tour` : **pas un silence** : B8 nomme déjà le « tour du générateur » ; les rôles listés sont des silences réels mineurs.
10. Audit de présentation, jetons, longueur, variance nulle : silences réels ; la façon d'absorber le signe dans le jeton est le fond de l'écart 5.2 : à écrire.
11. Le lecteur aux deux réglages tiré à la seule taille 1 et au taux 0,25 : **écart à nommer** : la table B8 range ce proposeur en famille B avec les mêmes tailles et taux que les lecteurs ; il reste sans critère, mais l'erratum doit le dire.
12. Manifeste, étiquettes résumées (nombre, empreinte de la liste triée, couches) : **écart léger à nommer** : B8 demande les étiquettes dans le manifeste ; la liste doit au moins exister dans un fichier scellé à côté, sinon l'empreinte ne se rejoue pas à la main.
13. M10 à chaque nombre lu sur les k premières sources de tous les tirages : silence réel, naturel.
14. Généraliste, entrées servies portant une classe : silence réel sans effet (le statut de budget n'apparaît jamais, B6).

## 7. Refus d'outil

Aucun.

*Contre-lecteur, modèle S.*
