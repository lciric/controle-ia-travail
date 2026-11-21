# Vérification du programme de vérité des dix-sept témoins imposés (course « seuil et moniteurs ») — v1

Vérificateur du programme de vérité des témoins, modèle S. Écrit le 2026-11-21. Pièce de travail pour la mère seule : elle contient des valeurs vraies refaites ; elle ne sort pas vers l'auteur ni vers une machine jetable. Aucun appel, aucune clé, aucune dépense, aucun commit. Aucun refus de permission ni de garde.

## 0. Verdict

**Conforme, prêt à sceller.** Aucune correction n'est exigée avant le scellement. Cinq réserves non bloquantes (§ 6) et six points pour la mère (§ 7), dont aucun ne change une valeur de la table.

- Les 17 témoins : la définition du § 3.1 est codée fidèlement ; toutes les valeurs refaites par une autre méthode concordent (écart maximal sur les exactes : 4 × 10⁻¹³ ; sur les encadrées : 2 × 10⁻⁹, très sous leur borne écrite).
- 184 essais passent ; table jouée deux fois, `cmp` muet, empreinte `cea076d9…` ; exemple de recalcul rejoué, `cmp` muet.
- Les mots de la mère de 09:15Z sont suivis par le programme (§ 5).

## 1. Empreintes et rejeu

| pièce | résultat |
|---|---|
| mandat du développeur | `05df0a86…`, égale au compagnon |
| mandat de l'auteur v3 | `816313cb…`, égale au compagnon |
| note de conception | copie `lectures/note-conception.md` `4f3ae86f…` ; `git show` de `origin/main:docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-experimentateurs-tests-de-mort-v1.md` après `fetch origin main` : `4f3ae86f…`, égale |
| programme de calcul de la note | copie `301c0f52…` ; `origin/main` : `301c0f52…`, égale |
| table d'empreintes du livrable | `sha256sum -c` : les 8 lignes OK ; les 9 compagnons `.sha256` OK (le livrable copié chez moi est identique à l'original) |
| essais | `…/.venv/bin/python -B -m pytest -q -p no:cacheprovider` : **184 passed** en 58 s (annoncés : 184 ; 64 artefacts, 64 mutations de garde, 11 mutations de calcul, 1 registre de gardes : relus, les mutations sont réelles — la ligne de garde est neutralisée dans une copie du code, ou le calcul remplacé, et l'essai doit échouer) |
| table, deux jeux chez moi | `table-a.json` et `table-b.json` : `cmp` muet ; empreinte `cea076d94621347d811921fff5ba7846434a97acae58e1b80943c66c090f4d69`, égale à la table du livrable |
| exemple de recalcul | rejoué chez moi : `cmp` muet avec `exemple-sortie-recalcul-v1.json` |

Remarque de forme : le texte du livrable écrit en dur « 184 essais » ; le test lui-même annonce « six mutations de calcul » dans son en-tête (ligne 13) alors qu'il en porte onze. Cosmétique.

## 2. Les dix-sept témoins : définition codée, valeur refaite

Programmes de contrôle écrits chez moi : `refaire_valeurs_v1.py` (scipy, numpy, simulation à graine fixe `SeedSequence(20261121)`), `refaire_exemples_v1.py`, `essais_moteur_v1.py`, `essais_limites_v1.py`. Sorties : celles de la session, reproduisibles. Les intervalles de simulation sont de niveau environ 99,99 % (Wilson).

| id | définition du § 3.1 | codée à | valeur de la table | refaite par | verdict |
|---|---|---|---|---|---|
| T01 | 3ᵉ plus grand de 300, confiance 5 % | l. 1486, 182, 185 | 0,577936082460 | `binom.sf(2, 300, 0,01)` et `beta.cdf(0,01 ; 3, 298)` : 0,577936082460 | oui |
| T02 | plus grand de 299 | 1487 | 0,950463743362 | 1 − 0,99²⁹⁹ | oui ; tient (0,95046 ≥ 0,95) |
| T03 | 3ᵉ plus grand de 300, en moyenne | 1488, 188-190 | 0,009966777409 | 3/301 ; simulation 200 000 tirages de 300 : 0,009960, écart-type estimé 1,3 × 10⁻⁵ | oui |
| T04 | 6ᵉ plus grand de 1 000 | 1489 | 0,933860488393 | `binom.sf(5, 1000, 0,01)` | oui |
| T05 | jamais alerter, n = 200, en moyenne | 1311-1316, 1355-1358 | taux 0 ; écarts à la base −0,027874250846 ; −0,073346314501 ; −0,349974785092 | − puissance de la base par `quad` : −0,027874250373 ; −0,073346314018 ; −0,349974785070 (écart ≤ 5 × 10⁻¹⁰, borne écrite ≤ 10⁻⁵) | oui |
| T06 | plus grand de 200 | 1491 | 0,866020325142 | 1 − 0,99²⁰⁰ | oui |
| T07 | la base, n = 200 et n = 400, en moyenne | 1492-1493 | 1/201 = 0,004975124378 ; 1/401 = 0,002493765586 ; puissances 0,027874250846 ; 0,073346314501 ; 0,349974785092 ; sachant le taux tenu 0,021360109735 ; 0,059784878751 ; 0,318260377439 ; écart à la base 0 exact | 1/201 et 1/401 par division ; puissances par `quad` de ∫ Φ̄(x−d)·200φΦ¹⁹⁹ dx (d = √2 Φ⁻¹(aire)) et par simulation à 4 × 10⁶ tirages du maximum par inversion (0,027877 ± 1,1 × 10⁻⁵ ; 0,073351 ± 2,4 × 10⁻⁵ ; 0,349974 ± 6,6 × 10⁻⁵) ; conditionnelles par `quad` : 0,021360107767 ; 0,059784878121 ; 0,318260377449 | oui, aux deux tailles |
| T08 | quantile empirique à 99 %, n = 400 | 193-199, 1494 | 0,371161420329, rang 5ᵉ plus grand | rang par entiers : ⌈400 × 99/100⌉ = 396, donc k = 400 − 396 + 1 = 5 ; `binom.sf(4, 400, 0,01)` ; simulation directe de 120 000 échantillons de 400, seuil = 396ᵉ plus petit : 0,37352, IC [0,3681 ; 0,3790] | oui |
| T09 | plus grand de 299, décalage qui triple 1 % | 1418-1423, 1496 | décalage 0,445554265890 ; couverture 0,565831810076 (borne 1,3 × 10⁻¹⁰) | d = Φ⁻¹(0,99) − Φ⁻¹(0,97) = 0,445554265890 ; 1 − (1 − Φ̄(z₉₉ + d))²⁹⁹ = 0,565831810076 ; simulation 10⁶ : 0,56533, IC [0,5634 ; 0,5673] | oui |
| T10 | H, plus grand de 300, 3 × 100 | 1047-1082, 1498 | 0,816660009932 (borne 1,3 × 10⁻⁵) | `quad` de 1 − (E_U[Φ((g−√ρU)/√(1−ρ))¹⁰⁰])³ : 0,816660010180 ; simulation de 800 000 échantillons complets : 0,81692, IC [0,8152 ; 0,8186] | oui |
| T11 | H, 30 × 10 | 1500 | 0,935149318473 (borne 9,2 × 10⁻⁶) | `quad` : 0,935149318865 ; simulation : 0,93521, IC [0,9341 ; 0,9363] | oui |
| T12 | S, test binomial exact, queue droite, strictement sous 0,01 | 206-224, 249-267, 1502 | 0,077002065529 | programmation dynamique en flottants avec seuils de compte par `scipy.stats.binom.sf` (P(X ≥ k) < 0,01) : 0,077002065529 ; simulation 10⁶ trajectoires : 0,077045, IC [0,0760 ; 0,0781] | oui ; du bon côté (avec P(X > k) à la place, on obtiendrait 0,3188 : la différence est visible) |
| T13 | S, pari 0,30 contre 0,20, richesse ≥ 100 | 232-246, 1506 | 0,007609939012 ; sonne contre 0,30 : 0,887855888433 ; sous dérive 0,25 : 0,271685685077 | programmation dynamique en log-richesse : 0,007609939012 ; 0,887855888433 ; 0,271685685077 ; simulation : 0,00782, IC [0,0075 ; 0,0082]. L'égalité richesse = 100 est impossible (3ᵏ7ᵗ⁻ᵏ contre 100·2ᵏ8ᵗ⁻ᵏ : le facteur 5 manque), donc la tolérance de ma version en logs ne tranche rien | oui |
| T14 | C, calibré sur tous, lu sur ceux qui échouent | 1614-1622, 1438-1447 | aucune valeur ; π critique 0,009969146793 | 1 − 0,05^(1/299) = 0,009969146793 | oui (mot de la mère : suffisant) |
| T15 | C, lu sur tous | 1623-1629 | 0,950463743362 | idem T02 | oui |
| T16 | C, calibré et lu sur ceux qui échouent | 1630-1635 | 0,950463743362 ; taux conditionnel 1/300 | idem T02 ; 1/(299 + 1) = taux moyen du plus grand de 299 | oui ; tient |
| T17 | I, comme T14 | 1636-1649 | 0,138893757160 limite ; haute 0,151678205341 | 1 − (1 − 0,01·0,05)²⁹⁹ ; 1 − (1 − 0,0005 − 0,00005)²⁹⁹. Je refais aussi le raisonnement : à 0,001 près, la part des réussites au-dessus du quantile à 99 % vaut au plus 0,00005 ; π ≤ 0,00055 | oui, mais cette valeur dépend de P(échec) = 0,05 (§ 7, point 3) |

Fidélité des définitions : sens et strictesse (« strictement supérieur », « atteint ou dépasse », « strictement sous 0,01 », valeur p queue droite), rang du quantile en entiers exacts (la mutation par flottants est détectée), taux moyen k/(n+1), portées de garantie et population de calibration (`tous_les_honnetes` partout, `honnetes_qui_echouent` pour T16, portée conditionnelle pour T14, T16, T17 : cela se lit dans `table_des_temoins`, non dans un champ de sortie propre — le mandat de l'auteur le porte dans ses propres champs, sans objet pour ce programme). Les 17 issues attendues : T01, T04, T06, T08, T09, T10, T11, T12, T17 `morte_invalide` ; T02, T03, T13, T15, T16 `tient` ; T05, T07 `morte_sans_gain` ; T14 sans issue. Cohérent avec D-M16 (seuls T05 et T07 lus « sans gain » ; la base T02 se lit sur la garantie seule : T02 `tient`).

## 3. Le moteur

- **Borne de discrétisation** (l. 879-906, 985-1007, 1047-1082) : rigoureuse. Pour l'espérance du taux d'un seuil au k-ième plus grand, l'intégrande ψ(x) = P(s < x) est croissante ; somme inférieure avec l'extrémité gauche, supérieure avec l'extrémité droite ; queue basse comptée à ψ(x₀) en haut et 0 en bas, queue haute comptée à ψ(x_fin) en bas et au supremum en haut. Pour les grappes, l'intégrande est décroissante en U et le sens des extrémités est bon ; la couverture 1 − Π f(g*) est encadrée avec g* encadré aussi (borne basse de couverture : g_haut, borne haute : g_bas). Pour le khi-deux, bornes par `min`/`max` des deux extrémités, queues comprises. Vérifié aussi en voie flottante contre la valeur exacte : le taux moyen de (n, k) = (300, 3), (200, 1), (1 000, 6), (40, 1) est dans l'encadrement (largeurs 1,1 à 1,9 × 10⁻⁵), et T07/T05/T10/T11/T09 contre mes `quad` (§ 2).
- **Tolérance de 10⁻¹²** : raisonnable à ce qu'elle couvre, mais pas démontrée et un peu courte à grande taille. Contre l'exact : la queue binomiale flottante a un pire écart de 1,1 × 10⁻¹² (n = 2 000, k = 5, p = 0,001), supérieur à la tolérance déclarée mais à une taille hors du mandat (≤ 1 000) ; la bêta incomplète contre scipy : 8,7 × 10⁻¹³ (a = b = 1 000, x = 0,5) ; la gamma incomplète : 3 × 10⁻¹⁴ ; la loi normale et Student : 10⁻¹⁶. À 0,001 d'enjeu, la marge est de neuf ordres de grandeur ; sans effet sur une issue. Réserve 6.1.
- **Refus des flottants** : tient. `rationnel` refuse `0.99`, `1.0`, `"0,99"`, `True`, `None` avec le code `nombre_non_rationnel` ; `lire_json` lit `0.99`, `9.9e-1`, `99e-2`, `0.990` comme le même rationnel 99/100 ; appelé en mémoire avec un flottant comme niveau de quantile, `recalculer_temoin` refuse. Le rang du quantile en entiers exacts est vérifié contre le plafond exact de `Fraction` sur 9 600 couples (n de 1 à 1 200 ; niveaux 0,99, 0,95, 0,07, 0,14, 0,28, 0,55, 0,56, 0,999) : tous justes ; le plafond en flottants se tromperait sur 128 des 7 200 couples des six niveaux à piège.

## 4. Le mode `--recalculer`

- Exemple du livrable : rejoué, `cmp` muet.
- Mes douze témoins (`entree-verif-recalcul-v1.json`, sortie `sortie-verif-recalcul-v1.json`) : le témoin juste (plus grand de 299, annonce 0,950463743362) rend un écart nul `en_deca_de_0_001`, issue d'accord ; le témoin faux de plus de 0,001 (3ᵉ de 300, annoncé 0,5790, vrai 0,577936…) rend `au_dela_de_0_001`, écart 0,00106391754, issue annoncée `tient` contre `morte_invalide` : désaccord d'issue compté ; annoncé 0,5788 : écart 0,00086, `en_deca` ; en voie encadrée (T09), 0,5669 : écart 0,001068 `au_dela`, 0,566831 : écart 0,000999 `en_deca` ; en séquentiel (T12), 0,0785 : écart 0,001498 `au_dela`, `valeur_annoncee` juste : écart nul ; quantile à 0,07 sur n = 200 : rang 187, taux 0,930348 (le piège flottant est évité), annoncé 0 : `au_dela`.
- Frontière (`entree-verif-recalcul-v2.json`) : annoncé 0,5668318100 (écart 0,000999999924, à cheval avec la borne) : `indecis_a_la_borne`, avec `ecart_min` et `ecart_max` ; annoncé 0,566832 : `au_dela` ; en exact, annoncé juste au-delà de l'écart : `au_dela`. Les comptes de fin (calculés, refusés, au-delà, indécis, désaccords) sont exacts : 9 / 3 / 4 / 0 / 2 sur ma première entrée.
- Trois refus propres, sans arrêter le lot : règle hors grammaire (`regle_hors_grammaire`), niveau écrit en chaîne (`nombre_non_rationnel`), `k > n` (`k_superieur_a_n`).
- « Compté et nommé » : chaque témoin porte sa comparaison, mais le bloc `comptes` ne donne que des nombres, sans la liste des identifiants en écart. Voir réserve 6.4.
- Trois autres exemples du livrable refaits : famille C (mélange, lecture sur ceux qui échouent) 0,154662017196, formule fermée 0,154662017196 ; dérive Laplace 0,771888782789, formule fermée 0,771888782789 ; tranche voisine 0,009894057927, `quad` 0,009894056526 (borne écrite 5,2 × 10⁻⁶) ; réseau 0,01105777012, simulation 4 × 10⁵ : 0,011055 (compatible).

## 5. Les mots de la mère de 09:15Z

| mot | le programme le suit-il ? |
|---|---|
| T09 : décalage vers le haut | Oui. `spec_decalage` translate la loi de lecture de + d (l. 503-511, 1425-1426) ; d = q₉₉ − q₉₇. Le sens compte : le décalage inverse donnerait une couverture de 0,99989 (`tient`), soit une issue contraire. Je l'ai refait : vers le haut, 0,5658 `morte_invalide`. |
| T05 et T07 : deux puissances, la puissance sans condition décide, la conditionnelle informe | Oui. L'issue (`issue_du_temoin`, l. 1138-1152) lit `ecarts_a_la_base`, calculés sur les puissances sans condition (l. 1349-1363) ; la puissance sachant le taux tenu est rendue à côté (l. 1310, 1576) sans entrer dans l'issue. La table ne dit pas, dans son texte, que la conditionnelle est une information ; le nom du champ le dit. |
| T14 : la condition exacte suffit | Oui. La table donne π critique encadré en rationnels (l. 1438-1447, 1614-1622) et laisse valeur et issue au recalcul. |
| `indecise_a_la_borne` : issue du recalcul, jamais de l'auteur ; « famille écartée » à la mise en fiches | Oui pour le programme : l'issue ne sort qu'à la rencontre d'un encadrement à cheval sur une coupure (l. 1141-1142, 1151) ; aucun des 16 témoins calculés de la table ne la porte. La traduction en « famille écartée » est hors du programme et se lit dans l'erratum 1 du mandat, non encore écrit. |
| correspondance sortie de l'auteur vers entrée du recalcul | Hors de ma vérification, selon le mot de la mère. Un point la touche : § 7, point 2. |

## 6. Réserves non bloquantes

1. **Tolérance déclarée dépassée de peu hors mandat** : 1,1 × 10⁻¹² à n = 2 000. Soit on garde « déclarée, non démontrée » telle quelle, soit on écrit au rapport que la tolérance vaut pour n ≤ 1 000 ; correction facultative, classe B, par erratum.
2. **Arrêt non propre sur des entrées extrêmes** : un `sigma` de 10⁴⁰⁰ lève `OverflowError`, que `recalculer` n'attrape pas (seul `Refus` l'est) : tout le lot s'arrête avec une trace, sans repli silencieux mais sans code de refus. `RuntimeError` (non-convergence) et `ZeroDivisionError` sont dans le même cas. Aucune taille n'est plafonnée : `n` = 10⁶ n'a pas fini en 250 s. Rien de tout cela ne touche les valeurs ; à écarter en amont si l'entrée vient de l'auteur (le mandat borne n à 200, 300, 400, 1 000).
3. **Même loi écrite de deux façons** : `canonique` (l. 389-390) distingue `0` et `0.0` lu du JSON (le premier est un entier, le second une `Fraction` rendue en chaîne par `default=str`), donc deux lois identiques, l'une lue `0`, l'autre `0.0`, ne passent pas par la voie exacte : valeur juste mais mode `flottant_borne`, borne 1,5 × 10⁻¹¹, issue juste. Seule une valeur à moins de 10⁻¹¹ d'une coupure en deviendrait `indecise_a_la_borne`.
4. **« Nommé »** : ajouter au bloc `comptes` la liste des identifiants en écart (`au_dela_de_0_001`, `indecis_a_la_borne`, désaccord d'issue) ; aujourd'hui le nom est dans l'entrée de chaque témoin.
5. **Forme** : décalage de T09 non arrondi dans `valeurs_de_plus` (0,4455542658895908) ; rang de T08 écrit 5.0 ; valeur exacte de T08 écrite en une fraction de plusieurs milliers de chiffres ; en-tête du test (« six mutations »). Sans effet.

## 7. Les dix-sept remarques du § 7 du rapport : y en a-t-il une que le programme tranche à tort ?

Aucune. Je les range.

**Déjà tranchées par la mère (09:15Z), le programme suit** : 4 (T09, sens), 5 (puissance de T05 et T07), 2 (T14 sans valeur), 13 (`indecise_a_la_borne`), 8 (correspondance).

**Sans effet sur les valeurs ni sur une issue, à laisser telles quelles** : 1 (lois de l'auteur à la loi de référence, marquées `depend_de_la_loi_de_l_auteur`), 6 (tailles de signal), 7 (loi des composantes d'une famille H), 9 (arrondi « au plus proche », un autre choix décale le réseau d'un demi-pas), 11 (α = 1 %), 12 (T12 : deux niveaux égaux à 0,01, tenue lue sur celui de la garantie), 15 (égalités sur seuil fixe ou atome refusées), 16 (famille D : rapport à part), 17 (familles hors moteur refusées avec code).

**Qui exigent un mot de la mère avant le scellement, ou à tout le moins avant la lecture de la sortie de l'auteur** :

1. **Remarque 10, convention de l'écart type** de `moyenne_plus_k_ecarts_types` : la comparaison automatique ne lit que la version n − 1 ; si l'auteur écrit un tel témoin avec la convention n, l'écart serait compté à tort, ou l'inverse. Je ne trouve pas dans la lettre de quoi trancher. Option sûre : comparer à la version n − 1 **et** à la version n, et compter « accord » si l'une des deux est à moins de 0,001, en nommant laquelle. Le programme rend déjà les deux versions.
2. **Remarque 14, identifiants** : D-M16 se lit par identifiant. Un témoin libre de l'auteur nommé T05 ou T07 serait lu « sans gain » ; un témoin imposé renommé échapperait à la lecture. Décider que les identifiants T01 à T17 sont réservés (refus du programme de vérification de la sortie si un témoin libre en porte un) — c'est une garde de la pièce qui lit la sortie, hors de ce programme.
3. **Remarque 3, T17 (et T09 à T11, puissances de T05 et T07)** : la table donne ces valeurs « à la loi de référence » ou « sous hypothèse ». Si le comparateur de la sortie de l'auteur lit la valeur de la table pour ces témoins, il comptera un écart à tort (ces valeurs changent avec la loi de l'auteur, et P(échec) peut valoir de 0,02 à 0,10 : à 0,10, la couverture limite de T17 vaudrait environ 0,2585 contre 0,1389). Décider que, pour ces témoins, seule la valeur du **recalcul** sur les lois de l'auteur est opposable, la table ne donnant que l'issue et la condition ; la table porte déjà le drapeau `depend_de_la_loi_de_l_auteur` à lire.
4. **Mixte de signes** pour T05 et T07 (§ 3.1 : « l'écart n'est pas strictement positif ») : pour un témoin dont l'écart serait positif à une taille de signal et non positif à une autre, le programme rend `tient` seulement si toutes les tailles sont tranchées et qu'une est positive, `morte_sans_gain` seulement si toutes sont non positives, sinon `indecise_a_la_borne`. Sans objet pour T05 et T07 eux-mêmes (écarts structurellement ≤ 0, T07 exactement nul) ; à dire dans l'erratum 1 si on veut le fixer pour d'autres lectures.

## 8. Autres vérifications demandées

- **Aucun nom de modèle, aucune clé** dans le livrable (hors `lectures/`) : recherche de « claude », « anthropic », « opus », « sonnet », « haiku », « fable », « gpt », « openai », « api key », « sk- », « secret », « token ». Une seule occurrence, dans le chemin du dossier de travail cité en § 9 du rapport (`…/-home-user-controle-ia-travail/…`), qui contient « claude-0 » : un nom de répertoire, non un identifiant de modèle. Les signatures « modèle O » et « modèle S » sont des étiquettes de rôle. Rien n'est lu sous `/root/.claude/`.
- Le dossier `lectures/` n'est pas un livrable (`essai-table-1.json` est un état antérieur du programme, signalé comme tel au rapport, § 8.4).

## 9. Mes fichiers

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verif-verite-temoins-mondes/` : `verification-programme-verite-temoins-v1.md` (cette pièce) et son compagnon ; `refaire_valeurs_v1.py`, `refaire_exemples_v1.py`, `essais_moteur_v1.py`, `essais_limites_v1.py` ; `entree-verif-recalcul-v1.json`, `sortie-verif-recalcul-v1.json`, `entree-verif-recalcul-v2.json`, `sortie-verif-recalcul-v2.json` ; `table-a.json`, `table-b.json`, `exemple-rejoue-s.json` ; `livrable/` (copie intacte du livrable) et `origin-note.md`, `origin-calculs.py` (versés de `origin/main`).

vérificateur du programme de vérité des témoins, modèle S
