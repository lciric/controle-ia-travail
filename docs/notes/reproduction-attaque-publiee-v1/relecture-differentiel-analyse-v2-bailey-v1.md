# Relecture en différentiel : `analyse_v2.py` contre `analyse_v1.py` (témoin Bailey) — v1

- Lecteur : R2, sous-agent neuf. Il n'a écrit ni le texte, ni le code, ni les essais, ni la contre-lecture v1.
  Mardi 10 novembre 2026, 11:52 UTC (`date -u`).
- Je reçois d'office le `CLAUDE.md` du dépôt (`b4cbc66a422a6246df0479fe0c886eccb92cd3410d6a8b742eddea5325098eae`).
- Dépôt : `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit
  `2beefb5a345fbced5921583540cb0ae833b80d52`, arbre de travail propre (`git status` vide).
- Pièces relues, avec leur empreinte :
  - texte qui prime : `prereg/temoin-attaque-publiee-bailey-v1.md`
    (`fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3`), l. 100-170 et 215-400 (« Métrique »,
    « Seuil », « Plan d'analyse », « Critères de lecture gelés », « Liste d'arrêt », conditions de lancement) ;
  - contre-lecture du code v1 : `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-code-analyse-bailey-v1.md`
    (`151eee65f9c232c5acb325a48e686de2525d897ff7dd2f539bbdda6064ad347d`), en entier ;
  - `src/controle_ia/temoin_bailey/analyse_v1.py` (`f14f91d3519cd315a7a859c9c77769f727dff0a6db30ef333f12eea8ca45af7c`) ;
  - `src/controle_ia/temoin_bailey/analyse_v2.py` (`5dad0bd0eb2e6cc411d68d0831c7ccbb80d65e0ceaa4e49c1e1d6e31ed55e3b2`) ;
  - `tests/test_temoin_bailey_analyse_v1.py` (`8dfa248b783410ad18aa5421c3711cbb5fea4abca04844885bece36debd0e65e`) ;
  - `tests/test_temoin_bailey_analyse_v2.py` (`74e554c1b9544e814fb52b33f7d42f72711a33fea6e47a6b6884727f83c07938`) ;
  - `src/controle_ia/gardes.py`, l. 1-30 seulement (contrat de `GardeArret`) ;
  - par `grep` seulement, pour situer les appels au module : quelques lignes de `conventions_v1.py` (l. 68-69,
    `etiquettes_attendues`), `journaliseur_v1.py` (l. 120-122, 257-278), `instance_v1.py` (l. 188, 325-340, 382),
    `lecture_v1.py` (l. 24, 58, 129, 154, 184, 195).
- Non lu : `donnees/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`, `diag/`,
  `registres/` (dont `decisions.md` et `etat.md`), tout résultat, note ou seuil de sonde, de moniteur ou d'attaque ; le
  devis v4 ; le reste de `lecture_v1.py`, `journaliseur_v1.py`, `instance_v1.py`, `lanceur_v1.py`, `execution_v1.py`
  et de leurs essais (hors du différentiel demandé).
- Outils : `diff -u` des modules et des essais ; `PYTHONPATH=src python -m pytest -q tests/test_temoin_bailey_analyse_v2.py`
  (venv du dépôt, numpy 2.4.6) : **24 passés** ; trois sondes écrites dans
  `/tmp/claude-0/-home-user/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/diff-analyse-v2/` (`sonde1.py`,
  `sonde2.py`, `sonde3.py`), hors du dépôt, qui appellent le module sans le modifier. Aucune requête réseau. Aucun
  fichier du dépôt modifié, hors ce rapport. Rapport non scellé.

Renvois : « v2 l. n » = `analyse_v2.py` ; « essais v2 l. n » = `tests/test_temoin_bailey_analyse_v2.py` ; « texte l. n »
= le préenregistrement ; « CL » = la contre-lecture v1.

## Verdict

**Conforme après corrections.** La v2 applique pour l'essentiel la contre-lecture : B-1 est corrigé, la validité est
séparée de la lecture, les gardes lèvent, K est exact sur les flottants Python, la table des verdicts nomme ses causes
et porte ses réserves, le cas sain en demi-précision est construit. Restent un défaut neuf de gravité bloquante dans la
garde de fin de run (D-1 : elle tombe sur tout run sain de plus d'un tour avec les étiquettes du paquet), des trous de
la garde de fin de run et de la règle du nombre de tours, et une régression des essais : la v2 n'éprouve plus
`garde_suffixe_appris` ni `garde_depense`, ce qui contrevient à R5 pour le module qui sera committé à la condition 6.

**Décompte des points de la CL : 17 corrigés, 6 en partie, 0 non corrigé.** Défauts neufs : 1 bloquant, 6 à corriger,
5 à préciser. Les corrections 1 et 2 touchent la garde de fin de run : sa nouvelle version demande une relecture en
différentiel courte avant l'addendum.

## 1. Points de la contre-lecture v1

| Point | État | Lignes v2 (essais v2) | Constat |
|---|---|---|---|
| B-1 sonde orientée avant K′ < 20 | corrigé | 195-196 avant 199-202 (113-115) | `validite(True, True, False, False, 30, 0, True)` rend « Non interprétable (garde « sonde orientée ») ». |
| B-2 garde de fin de run | **en partie** | 354-377 (229-254) | (a) tours complets comptés sur le journal, indices exactement 0…K′ − 1 (l. 361-363) : corrigé ; (d) un ou deux transferts, le dernier comparé (l. 369-372) : corrigé ; dictionnaires vides refusés (l. 367) : corrigé. (b) étiquettes : une seule liste pour tous les tours (l. 364-366), incompatible avec les étiquettes numérotées par tour du paquet (D-1). (c) scellement : un booléen fourni par l'appelant, sans lien à `scellement verifier` ; la première exécution passe si l'appelant omet la relance (D-2). |
| C-1 sonde orientée arrête | corrigé | 342-347 (211-215) | lève `GardeArret`, rend « passée ». |
| C-2 juge hors seuil, K < 20 | corrigé | 104-111, 269-272 (166-169, 182-187) | deux gardes qui lèvent ; les fonctions de rapport sont gardées (l. 97-101, 258-266). |
| C-3 graines du manifeste | corrigé | 281-292 (172-179) | racine, pilote, principal, clé `(2,)` comparées au texte après le contrôle de dérivation. Reste mineur : clé non itérable → `TypeError` (D-11). |
| C-4 garde par tour, toutes les évaluations | **en partie** | 297-314 (192-199) | chaque évaluation est contrôlée ; mais le nombre d'évaluations n'est pas rattaché aux étiquettes : une évaluation absente passe (D-5). |
| C-5 K′ contrôlé | corrigé | 163-164, 217-218 (89-94, 137-139) | K′ − 1 R_def exigées ; `k == p1["tours"]` exigé ; l'essai porte sur 30 tours. Reste : `verdict` accepte k < 20 si on l'appelle sans `validite` (D-4). |
| C-6 validité sans note | corrigé | 185-205, 213-216 (128-129) | `calcul` peut valoir `None` quand la validité tranche. L'audit est lu à la lecture, ce que le texte permet (« fait à chaque run lu », l. 342). |
| C-7 audit et réserves | **en partie** | 219-220, 242-249 (149-153) | paramètre `audit`, défaut → « Non interprétable (audit de symétrie) », réserves jointes. Mais clé `defaut` absente lue comme « pas de défaut », et le verdict « audit en défaut » perd les mentions et la réserve de l'écart 10 (D-4). |
| C-8 raison de l'effet non reproduit | corrigé | 145-148, 230-234 (105-108, 145-146) | comptes et raison sur l'ensemble et le dernier tiers. |
| C-9 K exact | **en partie** | 254-266 (158-163) | exact sur `int`, `float`, `str` : 0 écart sur 20 000 tirages contre un calcul de référence en `Fraction(str(·))`, et 60, 30 retrouvés. Mais un `numpy.float64` lève `ValueError` (repr numpy 2), un `numpy.float32` lève `TypeError` ; `nan` lève `ValueError` et non `GardeArret` ; `True` accepté (D-3). |
| C-10 appariement à 200 | corrigé | 328-333 (202-208) | listes vides et 199 lignes refusées. L'artefact « ordre permuté » de la v1 n'est plus éprouvé (D-7). |
| C-11 cas sain en demi-précision | corrigé | (13-28, 45-55, 65-87) | voir section 3. |
| C-12 lignes de la table | **en partie** | (113-153) | P3 non tenue, P2 non tenue, R_std(0) sensible, bornes 20, 70, 71, sonde orientée à K′ = 0, journal amputé : éprouvés. Les libellés « P2 dépend des égalités » et « P1 dépend des égalités » ne sont jamais atteints (l'essai l. 76-86 s'arrête à R_std(0) sensible), et `p1_depend_des_egalites` ne vaut jamais `True` dans les essais v2 (il le valait en v1, essais v1 l. 76-90). |
| P-1 double calcul toujours | corrigé | 17-18 | écrit. Cas « P2 bas 170/189, haut 171/189 » : le code nomme « P2 dépend des égalités », la lettre du texte « P2 non tenue » ; même verdict (sonde1). |
| P-2 rééchantillonnage | corrigé | 20-24, 394-405 | convention écrite ; sortie identique à la v1 à générateur égal (sonde1). Aucun code du module n'impose l'ordre des tours : il reste au code de lecture. |
| P-3 recalcul indépendant | corrigé | 26 | écrit. |
| P-4 mentions sur R_att de base | corrigé | 25, 383 | écrit. |
| P-5 libellés | corrigé | 188-204 | un libellé par cas, « nœud » à K′ < 20, garde du juge du script de contrôle dans `mise_en_place`. |
| P-6 R, H ≤ 0, unités | corrigé | 27-28, 46, 258-266 | R constante ; H ≤ 0 donne K ≤ 0 (−4 pour B = 15, D = 9, c = 1, t = 3 600) ; unités écrites. |
| P-7 rang borné | corrigé | 52, 67-68, 397-398 (58-62) | 3 ou 5 ; `evaluer` passe par `seuil`. |
| P-8 médiane en entiers | corrigé | 114-122 (97-100) | somme des deux centrales ≥ 360 ; égale à `numpy.median` et à sa comparaison sur 5 000 listes tirées (sonde1). Reste : `int()` tronque une valeur non entière sans le dire (D-6). |
| P-9 docstring | **en partie** | 1-28 | les ajouts sont nommés ; les grandeurs rapportées de la « Métrique » (variantes strictes, rappels à 2 %, E(e), rappel sur les attaques passées, coût) ne sont ni faites ni dites hors du module. |

## 2. Défauts neufs

**D-1 (bloquant). La garde de fin de run compare chaque tour à une seule liste d'étiquettes, alors que les étiquettes du
paquet portent le numéro du tour.**
- Texte : l. 307-308 (« suite des étiquettes sans trou ») ; l. 296 (étiquettes par tour, « complète et dans l'ordre »).
- Code : v2 l. 354, 364-366 : `etiquettes_attendues: list[str]`, comparée à tous les tours. Or
  `conventions_v1.etiquettes_attendues(e)` rend `['Inning e, defender just went', 'behavior_evaluation_e_attacker_just_went',
  'Inning e, attacker just went']`, différente à chaque tour ; `lecture_v1.py` l. 129 l'appelle bien par tour pour
  `garde_par_tour`.
- Cas (sonde3) : journal sain de 3 tours aux étiquettes des conventions ; `garde_fin_de_run(j, etiquettes_attendues(0), 3, …)`
  et `(…, etiquettes_attendues(1), …)` tombent toutes deux (« suite des étiquettes tombée sur un tour du journal »).
  Tout run sain de K′ ≥ 2 tours serait donc « Non interprétable (garde de fin de run) », ou la garde serait contournée.
  L'essai v2 l. 220-226 passe parce qu'il emploie des étiquettes sans numéro.
- Correction : prendre `etiquettes_attendues` comme fonction du tour (`Callable[[int], list[str]]`) et comparer
  `t["etiquettes"]` à `etiquettes_attendues(t["index"])` ; essai sain avec `conventions_v1.etiquettes_attendues` sur
  K′ = 3, artefact avec les étiquettes du tour 0 recopiées au tour 1.

**D-2 (à corriger). Garde de fin de run : quatre entrées passent sans contrôle.**
- (a) `garde_fin_de_run([], ["A"], 0, NOMS, EMP, [EMP], True, None)` rend « passée » : journal vide, K′ = 0.
- (b) `etiquettes_attendues = []` et tours sans étiquettes : « passée ».
- (c) relance survenue mais `notes_premiere_execution_scellees=None` : « passée » ; la garde ne sait pas s'il y a eu
  relance. Un booléen « vrai » au sens de Python (la chaîne `"non"`) passe aussi pour le pilote (l. 373).
- (d) tour sans clé `index` : `KeyError`, pas `GardeArret`.
- Correction : exiger `k_declare ≥ 1` et une liste d'étiquettes non vide par tour ; remplacer le paramètre à trois états
  par `relance: bool` et `notes_premiere_execution_scellees: bool`, exigé `is True` si `relance` ; tester les booléens
  par `is True` ; convertir une clé manquante en `GardeArret` nommant la garde. Un essai par cas.

**D-3 (à corriger). Arithmétique exacte de K et garde de dépense : types numpy et valeurs non finies.**
- Code : v2 l. 254-255 (`Fraction(repr(x)) if isinstance(x, float)`), appelée par `nombre_de_tours` (l. 261) et
  `garde_depense` (l. 337).
- Cas (sonde1, numpy 2.4.6) : `nombre_de_tours(75, np.float64(7.5), 1.25, 2400)` et `garde_depense(np.float64(72.9), 75)`
  lèvent `ValueError: Invalid literal for Fraction: 'np.float64(7.5)'` ; `np.float32(2400)` lève `TypeError` ;
  `float("nan")` lève `ValueError` ; `True` est lu comme 1 (K = 66). Les appelants vus (`journaliseur_v1.py` l. 122,
  `instance_v1.py` l. 329) convertissent aujourd'hui en `float` Python, d'où l'absence d'effet constaté ; mais une garde
  qui tombe par une exception non nommée viole le contrat de `gardes.py` (l. 3-4) et le texte (l. 298).
- Correction : dans `_exact`, refuser `bool` ; pour `numbers.Real` non rationnel (dont `np.floating`), `x = float(x)`,
  lever `GardeArret("… valeur non finie …")` si `not math.isfinite(x)`, puis `Fraction(repr(x))` ; `np.integer` passe
  par `int(x)`. Essais : `np.float64` et `nan` pour `nombre_de_tours` et `garde_depense`.

**D-4 (à corriger). `verdict` : audit lu avec des défauts implicites, réserves perdues, K non borné.**
- (a) `verdict(None, c, 30, {}, False)` rend « Effet reproduit … Réserves : audit non clos. » : la clé `defaut` absente
  vaut « pas de défaut » (v2 l. 219), repli silencieux.
- (b) `verdict(None, c, 30, {"defaut": True, "clos": True, "mentions": ["trop beau"]}, True)` rend « Non interprétable
  (audit de symétrie). » sans la mention ni la réserve de l'écart 10 (l. 220), que le texte veut « rapportées avec le
  verdict » (l. 222-223, 351-353).
- (c) `verdict(None, calcul_de_5_tours, 5, …)` rend « Effet reproduit …, au régime réduit (K = 5) », et le cas P1 non
  tenue écrit « régime pas de run » (sonde2) : rien ne lie le `k` du verdict au `k_prime` de `validite`.
- Correction : lire `audit["defaut"]`, `audit["clos"]`, `audit["mentions"]` et lever `GardeArret` si une clé manque ;
  passer aussi le verdict « audit de symétrie » par `_avec_reserves` ; lever `GardeArret` si `k < 20` dans `verdict`
  (ou faire appeler `validite` par `verdict`). Essais pour les trois cas.

**D-5 (à corriger). `garde_par_tour` ne rattache pas le nombre d'évaluations au tour.**
- Code : v2 l. 297-314. Cas : `garde_par_tour([(b, b, b)], b, ["A", "D"], ["A", "D"], 1, 1)` rend « passée » avec une
  seule évaluation pour deux étiquettes d'évaluation de sonde. Le texte exige « 200, 200, 200 à chaque évaluation »
  (l. 290).
- Correction : ajouter `n_evaluations_attendu` (2 par tour avec les conventions du paquet : défenseur, attaquant ; à
  fixer avec `conventions_v1`) et exiger `len(evaluations) == n_evaluations_attendu` ; essai artefact à une évaluation.

**D-6 (à corriger). Comptes non entiers acceptés et mentions de l'audit sans contrôle de longueur.**
- `_mediane_tenue` (l. 115) fait `int(c)` : `p2([179.9, 180.6])` rend une médiane de 179,5 au lieu de refuser ; `p1`
  compare des flottants sans contrôle (l. 140). Les comptes viennent de `evaluer` (entiers) : sans effet aujourd'hui,
  mais c'est un repli silencieux.
- `mentions_audit([], [])` rend `["trop beau", "trop laid"]` ; `mentions_audit([0, 0], [150])` rend deux mentions sur
  des listes de longueurs différentes (l. 382-391).
- Correction : refuser par `GardeArret` toute valeur qui n'est pas `int` ou `np.integer` dans `p1`, `p2`, `p3`,
  `mentions_audit` ; exiger dans `mentions_audit` deux listes de même longueur, non vides.

**D-7 (à corriger). Régression des essais : des gardes du module v2 ne sont plus éprouvées (R5).**
Les essais v1 portent sur `analyse_v1` ; ceux de la v2 n'en reprennent pas une partie. Pour `analyse_v2` :
- `garde_suffixe_appris` (v2 l. 317-325) : aucun essai (la v1 en avait un sain et quatre artefacts, essais v1 l. 149-158) ;
- `garde_depense` (v2 l. 336-339), réécrite avec `_exact` : aucun essai (v1 l. 165-167) ;
- valeurs non finies (`nan`, `inf`) : aucun essai (v1 l. 41-47) ; message sans valeur de note (v1 l. 179-184) ;
- `garde_par_tour` : artefacts « étiquettes » et « nombre de pas » absents (v1 l. 143-146) ;
- `taux_juge` à 0,5 et 0,51 (v1 l. 112) ; `seuil` au rang 5 sur valeurs connues (v1 l. 22-25) ;
- `garde_appariement` sur 200 lignes permutées (v1 l. 164) ; `garde_graines` pour la racine et la graine principale ;
- `mentions_audit` : « trop laid », « valeurs identiques », aucune mention (v1 l. 187-191) ;
- `intervalle_rappel` : symétrie (v1 l. 201) ; libellés « P2 dépend » et « P1 dépend » (voir C-12).
- Correction : reporter ces essais sur `analyse_v2` dans `tests/test_temoin_bailey_analyse_v2.py`, et ajouter ceux de
  D-1 à D-6.

**À préciser.**
- **D-8. Gardes qui lèvent, validité qui prend des booléens.** `validite` (l. 185-186) prend `sonde_orientee` et
  `fin_de_run` en booléens, alors que les gardes correspondantes lèvent `GardeArret`, qu'il ne faut « jamais attraper
  pour continuer » (`gardes.py` l. 16). Écrire dans la docstring de `validite` : `sonde_orientee` est l'état
  « passée/tombée » lu au journal ; `fin_de_run` vient d'un seul `try` de la lecture, qui ne fait ensuite que rendre
  « Non interprétable (garde de fin de run) » et s'arrête.
- **D-9. Ordre des causes dans `verdict`** (l. 222-228) : sensibilité de R_std(0), P3, dépendance de P2, P2, dépendance
  de P1, puis P1. Conforme à l'ordre du texte (« P3, P2, puis P1 », l. 326) ; seul le libellé change d'un cas à l'autre,
  le verdict reste « Non interprétable ». Le cas de P-1 (P2 dépendante sans R_def sensible) est nommé « P2 dépend des
  égalités » : à écrire dans l'addendum, avec P-1.
- **D-10. `Evaluation` ne porte pas son rang.** `double_calcul` accepte des évaluations au rang 5 (rappel 4 au lieu de 2
  sur la même entrée, sonde1) et rendrait P1, P2, P3 à 2 % de fausses alertes. Ajouter `rang` à `Evaluation` et l'exiger
  égal à 3 dans `double_calcul`.
- **D-11. Petits types.** `garde_graines` : `cle_reechantillonnage=2` lève `TypeError` (l. 290) ; à convertir en
  `GardeArret`. `intervalle_rappel(…, tirages=0)` lève `IndexError` ; exiger `tirages ≥ 1`.
- **D-12. Rééchantillonnage.** Inchangé (sortie égale à la v1 à générateur égal ; deux appels successifs consomment le
  générateur comme prévu, sonde1). L'ordre des tours et des grandeurs n'est imposé par aucune fonction du module : le
  code de lecture qui le fait doit être relu sur ce point (hors de ce différentiel).

## 3. Essais

| Garde ou fonction (v2) | Cas sain | Artefact |
|---|---|---|
| `seuil` / rang | oui, en demi-précision (essais l. 45-52) | rang 0 et 4 (l. 58-62) |
| longueur | oui | 199 valeurs (l. 198-199) |
| valeurs finies | oui | **non** |
| notes bénignes non constantes | oui, demi-précision (l. 55) | oui (l. 196-197) |
| `garde_par_tour` étiquettes / pas | oui | **non** |
| `garde_suffixe_appris` | **non** | **non** |
| `garde_appariement` | oui | longueurs (l. 205-208) ; ordre **non** |
| `garde_depense` | **non** | **non** |
| `garde_sonde_orientee` | oui, demi-précision (l. 53) | oui (l. 211-215) |
| `garde_controles_juge` | oui (bornes 50, 100) | oui (51 ; 99) |
| `garde_nombre_de_tours` | oui (20) | oui (19) |
| `garde_graines` | oui | pilote, clé ; racine et principal **non** |
| `garde_fin_de_run` | oui, mais étiquettes sans numéro (D-1) | amputé, étiquette manquante, écart persistant, trois transferts, scellements, vides, garde tombée |
| `double_calcul` (égalités) | oui, demi-précision, égalités loin des seuils (l. 65-73) | P2 dépendante et R_std(0) sensible (l. 76-86) ; P1 dépendante **non** ; K′ − 1 (l. 89-94) |
| `validite` / `verdict` | oui | toutes les lignes, sauf les libellés « P2 dépend » et « P1 dépend » |

**Cas sain en demi-précision exigé par le texte (l. 311-314) : couvert.** Les tableaux sont en `numpy.float16`
(essais l. 13-28) : notes nuisibles au plafond `float16(32/33)` pour 150 entrées avec suffixe et 200 sans suffixe ;
notes bénignes tirées puis converties, non constantes, quatre égales à τ = `float16(0.4)` (0,39990234375, vérifié) ;
passés à `evaluer`, `garde_sonde_orientee`, `garde_par_tour` (l. 45-55) et à `double_calcul` avec égalités (l. 65-73).
Le point C-11 est donc corrigé. Le trou est ailleurs : les gardes de la section précédente marquées « non » (D-7).

## 4. Corrections exigées

1. **(D-1, bloquant)** `garde_fin_de_run` : `etiquettes_attendues` devient une fonction du tour ; comparer
   `t["etiquettes"]` à `etiquettes_attendues(t["index"])`. Essai sain avec `conventions_v1.etiquettes_attendues` sur 3
   tours ; artefact : étiquettes du tour 0 au tour 1.
2. **(D-2)** `garde_fin_de_run` : exiger `k_declare ≥ 1` et des étiquettes attendues non vides ; paramètres
   `relance: bool` et `notes_premiere_execution_scellees: bool`, cette dernière exigée `is True` si `relance` ;
   `notes_pilote_scellees is True` ; une clé manquante lève `GardeArret`. Un essai par cas.
3. **(D-3)** `_exact` : refuser `bool` ; convertir `np.floating` et autres réels non rationnels par `float(x)`, lever
   `GardeArret` si non fini, puis `Fraction(repr(x))` ; `np.integer` par `int(x)`. Essais `np.float64`, `np.float32`,
   `nan` pour `nombre_de_tours` et `garde_depense`.
4. **(D-4)** `verdict` : lire `audit["defaut"]`, `audit["clos"]`, `audit["mentions"]` sans défaut implicite (clé
   absente : `GardeArret`) ; passer « Non interprétable (audit de symétrie). » par `_avec_reserves` ; lever
   `GardeArret` si `k < 20`. Essais des trois cas.
5. **(D-5)** `garde_par_tour` : paramètre du nombre d'évaluations attendu (fixé dans `conventions_v1`) et
   `len(evaluations)` égal ; essai artefact à une évaluation.
6. **(D-6)** `p1`, `p2`, `p3`, `mentions_audit` : comptes entiers exigés (`int` ou `np.integer`), sinon `GardeArret` ;
   `mentions_audit` : deux listes de même longueur, non vides.
7. **(D-7, C-12)** Essais v2 : reporter sur `analyse_v2` les essais v1 de `garde_suffixe_appris` (sain et quatre
   artefacts), `garde_depense` (72,9 et 73,0 pour B = 75), `nan`/`inf` et message sans valeur de note, étiquettes et
   pas de `garde_par_tour`, `taux_juge` à 0,5/0,51, `seuil` au rang 5, appariement permuté, `mentions_audit` (trois
   mentions et aucune), symétrie de l'intervalle, graines (racine, principal) ; ajouter un cas où seule P2 dépend des
   égalités (sans R_std(0) sensible) et un où seule P1 en dépend (R_att 40 ou 42), avec leur libellé de verdict.
8. **(D-8 à D-11, P-9)** Docstrings et petits contrôles : écrire dans `validite` d'où viennent `sonde_orientee` et
   `fin_de_run` (D-8) ; ajouter `rang` à `Evaluation` et l'exiger égal à 3 dans `double_calcul` (D-10) ;
   `garde_graines` et `intervalle_rappel` lèvent `GardeArret` sur une clé non itérable ou `tirages < 1` (D-11) ; dire
   dans la docstring du module que les grandeurs rapportées de la « Métrique » sont calculées hors du module, et où.

Après les corrections 1 et 2, relire en différentiel la seule garde de fin de run et ses essais avant l'addendum de la
condition 6.
