# Contre-lecture du module des lots du bras A, version 2 (pièce de classe B) — v1

- **Objet** : `src/controle_ia/organismes_discrets/lots_bras_a_v2.py` (`a14b86d6780ea32843629e00498b557c1bda396946813ba00d8175dce78085b1`, empreinte vérifiée) et `tests/test_lots_bras_a_v2.py`, contre `prereg/T0.7-organismes-discrets-v-a-v2-brouillon51.md` (lignes 551-552, 702, 714, 719, 799, 806, 808, 812, 815, 819, 821-822, 846, 1172), la note du code v2, la note v1 et `quatre-regles-effectifs-fable-v1.md`.
- **Lecteur** : agent neuf, qui n'a écrit ni le module ni les essais. Processeur seul, aucune dépense, rien committé. Aucune pièce cloisonnée ouverte.
- **Essais rejoués** : `PYTHONPATH=src python3 -m pytest -q -p no:cacheprovider tests/test_lots_bras_a_v2.py tests/test_lots_bras_a_v1.py` : 68 passés. Quelques sondes à la main (hors dépôt) à l'appui des défauts ci-dessous.

## Verdict : à corriger (aucun bloquant ; deux défauts majeurs, quatre mineurs)

Les cinq planchers, le constat, les gardes de la couverture et du lot décisif, la voie de service et les graines sont conformes à la lettre. Les deux majeurs sont des écarts de couverture entre le texte et le code, non des erreurs de plancher.

## (1) Planchers et issue « effectif insuffisant » : conforme

- Génériques (l. 331-373) : n ≥ 64 tirage ; 32 à 63 toutes, sans tirage des actions, parts égales ; n < 32 constat, lot construit sans eux, rien de complété. Conforme à 799/806.
- Ancres (376, 425) : plancher 24 par population, constat avant tout tirage, suite A5 / A7. Le second plancher de l'ancre sur plans honnêtes (autres tâches) est redondant avec le premier (ligne 808 le dit), sans effet.
- Couverture (463) : les deux planchers de 32 jugés après la partition à 64 (garde 1172 d'abord), constat, aucun lot. Au plancher de 32 plans, les plans mécaniques sont au moins 16 : vérifié (somme de min(4, n_t) ≥ 16), donc la garde de `_tirer` de l'ancre (8) reste inatteignable.
- Relues (576) : gardes d'entrée jouées avant le constat ; constat si l'une des classes est sous 80 ; lot non construit, retour d'un `Constat`. Conforme à 846.
- Aucun repli silencieux : `_tirer` arrête (`GardeArret`) si inatteignable ; `Constat` refuse un constat sans compte sous plancher ; `inscrire_au_manifeste` ne réécrit pas (R12). Sondé : un constat de couverture passé comme lot honnête au lot décisif arrête.

## (2) Lectures « à la lettre »

- **160 juste (719/846) : seule lecture littérale.** « S'il en existe moins » ne vise pas une classe de 160 ; le complet est « tirées par graine ». Mais le résultat de la classe suivante dépend de l'état du générateur : la lecture est déterminante pour les octets. Mineur m-1 : l'inscrire dans le texte (13.1 ou ligne 719) plutôt que dans la seule note.
- **806, 32-63 sans tirage, 64 tiré** : lecture littérale. Mais voir M-2 : la même logique n'est pas appliquée aux deux autres épreuves jointes.
- **822, un seul constat** (note, lecture 4) : lecture raisonnable (« la suite est celle du lot honnête »), non unique : le constat s'écrit « l'objet, le compte, le plancher » au singulier (806) et l'objet « couverture » n'est ni épreuve jointe, ni ancre, ni lot, ni relecture. Mineur m-2 : une phrase au texte (« un seul constat, objet couverture, qui porte les deux comptes »).
- **815/821** : conforme (une seule tâche sans plan est laissée hors moyenne et « comptée » : le code ne compte par tâche que `episodes-sans-plan` ; voir m-4).

## (3) Voie de service du juge (ligne 552)

Rang à partir de 1 par lot, impair sous `GEMINI_API_KEY`, pair sous `GEMINI_API_KEY_2`, tableau ne dépendant que de l'effectif, aucun item nommé, reprise sous la clé du premier envoi, ordre (d) plans honnêtes puis couverture, (e′) jumeaux, révision sans couverture : conforme. Défaut M-1 ci-dessous pour le chemin du constat à (e′).

## (4) Graines et déterminisme (R9) : conforme

Tout aléa vient de `g.generateur_de(g.cle(...))` ou des briques `ordre_des_appels`, `identifiants_opaques`, `cle_alea`, `cle_sentinelles` ; aucun `random`, aucun `numpy` global (grep). Essai `test_aucun_autre_alea` et déterminisme octet pour octet présents et passés.

## (5) Ambiguïtés restantes : conforme

Aucune action donneuse d'une autre tâche : `AmbiguiteDuTexte` (testé). Moins de 896 plans des conditions au lot décisif : `AmbiguiteDuTexte` (testé). Plus de 896 est impossible (7 × 8 × 16 distincts) ; un doublon arrête par `GardeArret`.

## (6) Essais : couverture suffisante, trois manques (voir m-3, M-1, M-2)

Chaque plancher est essayé au-dessus, sur et sous lui ; chaque garde de 1172 sur cas sain et artefact ; mutations (49) déclarées par la note, non rejouées ici.

## Défauts

### Majeurs

- **M-1 : l'issue « effectif insuffisant » de l'ancre des jumeaux n'a pas de voie à l'étape (e′).** `voie_de_service_de_l_etape_d` accepte un constat à la place de chaque ancre, mais `voie_de_service_du_juge(constat_ancre_jumeaux)` lève `GardeArret` (« pas un lot du juge »). Sondé. Le chemin légitime de 812 (« aucun jumeau n'est remis au juge ») arrête donc le programme au lieu de ne rien envoyer. Correction : une fonction `voie_de_service_de_l_etape_e_prime(objet)` (lot : tableau ; constat d'`ancre-jumeaux` : liste vide ; tout autre objet : arrêt), avec essais sain et artefact.
- **M-2 : lecture à l'égalité non déclarée pour deux épreuves jointes (lignes 343 et 353).** `rec = h if len(h) <= N … else tirage` ne tire pas à 128 (autres tâches) ni à 64 (texte sans rapport) exacts, alors que la note déclare « 64 est le cas complet, tiré » pour les génériques et « 160 juste tiré » pour les relues. À 128 exactement, le tirage n'a pas lieu et l'état du générateur qui sert ensuite aux donneuses change (sondé : 127/128/129 donnent trois lots distincts ; l'effet est réel à 128). Comportement hérité de la v1 (mêmes octets), mais incohérent avec les lectures déclarées et sans essai à 128 ni à 64. Correction : soit aligner (`<` et tirage à l'égalité, à porter alors comme écart de la v1), soit déclarer dans la note et au texte que « moins » vise strictement l'inférieur et que l'égalité sans tirage est le code de la v1 ; dans les deux cas, un essai à l'égalité.

### Mineurs

- **m-1** : 160 juste tiré (voir (2)) ; porter la lecture au texte.
- **m-2** : un seul constat de couverture (voir (2)) ; porter au texte.
- **m-3 : `lot_jumeaux_couverture` (l. 553) ne compare que les comptes** (`len(d)`, `len(lh)`) au lot honnête, alors que le docstring dit « ceux comptés ». Sondé : deux plans déplacés échangés contre trois laissés honnêtes, mêmes effectifs, sont acceptés. La ligne 1172 écrit « les comptes ne font pas 64 », donc conforme à la lettre ; mais le lot honnête pourrait garder l'empreinte des deux ensembles (`comptes`) et le lot des jumeaux la comparer.
- **m-4** : « une tâche sans aucun plan est laissée hors des moyennes et comptée » (815, 822) : le module ne compte pas les tâches sans plan ; à écrire dans les comptes de `plans_mecaniques` ou de `lot_honnete_couverture`, ou à renvoyer à la couche d'analyse.

### Question de texte (non du code)

Si l'ancre sur plans honnêtes est à effectif insuffisant, le critère de l'ancre des jumeaux (812) lit « les 24 honnêtes de la première partie » : qu'en est-il ? Le code livre alors l'ancre des jumeaux (24 jumeaux à effet) au juge sans honnêtes. À trancher par le texte avant le scellement (choix de Lazar, non du code).

## Conclusion

Conforme sur les planchers, le constat, la voie de service par lot, les graines et les ambiguïtés ; **à corriger** pour M-1 et M-2 (puis vérification des corrections par le même lecteur, selon l'allègement de procédure).
