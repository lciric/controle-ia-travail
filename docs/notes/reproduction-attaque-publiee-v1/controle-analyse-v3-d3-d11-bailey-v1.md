# Contrôle point par point des corrections D-3 à D-11 : `analyse_v2.py` → `analyse_v3.py` (témoin Bailey) — v1

- Date : Tue Nov 10 17:51:14 UTC 2026 (`date -u`). Relecteur neuf (R2), auteur d'aucune pièce lue. Non scellé.
- Je reçois d'office le `CLAUDE.md` du dépôt (consignes permanentes), injecté dans mon contexte.
- Branche `claude/compassionate-meitner-d4ryyk`, commit `62e29af5`.

Pièces lues et empreintes (SHA-256) :

| Pièce | Empreinte |
|---|---|
| `docs/notes/reproduction-attaque-publiee-v1/relecture-differentiel-analyse-v2-bailey-v1.md` (sections 2 à 4) | `8895a5a7ad497e7bbb6c566d1c89ea9ac3afdedaa039d8c6bda620d26e679889` |
| `prereg/temoin-attaque-publiee-bailey-v1.md` (« Métrique », « Seuil », « Critères de lecture gelés ») | `fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3` |
| `src/controle_ia/temoin_bailey/analyse_v2.py` | `5dad0bd0eb2e6cc411d68d0831c7ccbb80d65e0ceaa4e49c1e1d6e31ed55e3b2` |
| `src/controle_ia/temoin_bailey/analyse_v3.py` | `c28c6821629a6d4eec657c376a3df2d5361de2e46c4441361f43e0e8f423f2ca` |
| `tests/test_temoin_bailey_analyse_v3.py` | `8cca01f18b61f81fc805dc3c89847e997db66c05609f644a08a5929b3f440d47` |
| `tests/test_temoin_bailey_analyse_v1.py` (l. 185-205 seulement, pour D-7) | — |
| `src/controle_ia/temoin_bailey/conventions_v1.py` (en-tête, `etiquettes_attendues`) ; `conventions_v2.py`/`v3.py` (ligne `EVALUATIONS_PAR_TOUR`) ; `lecture_v8.py` (l. 630-742, appels à `analyse_v3`) ; `src/controle_ia/gardes.py` (l. 1-20) | — |

Empreintes vérifiées seulement, non relues : `relecture-differentiel-code-condition6-v2-bailey-v1.md` (`4f079ece…`),
`contre-lecture-addendum-1-condition6-bailey-v1.md` (`c68dcec4…`). Les fichiers `lectures-*addendum-condition6-v*.md`
ont été seulement cherchés par `grep` (« dépend »), non lus.

Non lu (cloisons) : `donnees/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`, `diag/`, tout
résultat, note ou seuil de sonde ou de moniteur du programme, résultats A1-v3/A1-v4, R-604 à R-610 de
`registres/decisions.md`, `registres/etat.md`. Aucune clé, aucune requête réseau, aucun refus de classifieur.

Outils : `diff -u` v2/v3 ; `pytest -q tests/test_temoin_bailey_analyse_v3.py` (**36 passés**, 0,18 s) ; une sonde
Python hors dépôt : `/tmp/claude-0/-home-user-controle-ia-travail/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/ctrl-d3-d11/sonde_d3_d11.py`
(`4aeedbd4…`), sortie `…/ctrl-d3-d11/sonde_d3_d11.sortie.txt` (`f4148805…`).

## Verdict

**D-3 à D-11 non entièrement conformes ; aucun point bloquant.** Une correction exigée reste à faire (D-6 sur
`mentions_audit`), deux essais exigés manquent (D-7), le reste est conforme ou appelle des précisions sans effet sur une
issue (D-3, D-4, D-8, D-9, D-10, D-11).

## Table

Lignes de `analyse_v3.py` ; essais de `tests/test_temoin_bailey_analyse_v3.py`.

| Point | État | Lignes v3 | Essai qui l'éprouve | Remarque |
|---|---|---|---|---|
| D-3 `_exact` : bool, numpy, non finis | **fait** | 283-302 (appelée l. 308, 382) | `test_nombre_de_tours_types_numpy_et_refus` (l. 280-292) : `np.int64`, `np.float64`, `np.float32`, chaînes, `nan`, `inf`, `True`, `None`, `"x"` ; `garde_depense` `nan` et `np.float64(72.9)` | `np.float32` non éprouvé sur `garde_depense` (sonde S3a : « passée », correct). Régression neuve sur `Fraction`, voir E-2. |
| D-4 (a) clés d'audit exigées | **fait** | 243-245, 273-275 | l. 295-301 | Type des valeurs non contrôlé, voir E-3. |
| D-4 (b) réserves sur « audit de symétrie » | **fait** | 248-249 | l. 304-305 (mention et écart 10) | l. 151-153 : cas sans réserve, texte nu, correct. |
| D-4 (c) K′ ≥ 20 dans `verdict` | **fait** | 241-242, 246-247 | l. 302-303 ; l. 139-141 (K′ ≠ tours de P1) | |
| D-5 nombre d'évaluations par tour | **fait** | 347-352 | l. 359-366 (une évaluation : tombe) | Constante dans `conventions_v2.py` l. 77 et `conventions_v3.py` l. 89 (`EVALUATIONS_PAR_TOUR = 2`), passée par `lecture_v8.py` l. 701-702. Le défaut `= 2` de la signature (l. 348) double la constante : voir E-5. |
| D-6 comptes entiers dans `p1`, `p2`, `p3` | **fait** | 123-129, 133, 157, 176 | `test_comptes_entiers_exiges` (l. 339-346) | |
| D-6 `mentions_audit` : listes appariées, non vides | **fait** | 446-447 | l. 349-353 | |
| D-6 `mentions_audit` : comptes entiers | **non fait** | 444-455 (aucun appel à `_entiers`) | aucun | Sonde S1 : voir E-1. |
| D-7 report des essais (R5) | **en partie** | — | `garde_suffixe_appris` sain + 4 artefacts (l. 379-384) ; `garde_depense` 72,9/73 (l. 290-292) ; `nan`/`inf` et message sans valeur (l. 371-376) ; étiquettes et pas (l. 367-370) ; `taux_juge` 0,5/0,51 et `seuil` rang 5 (l. 393-397) ; appariement permuté (l. 385-390) ; graines racine et principal (l. 400-408) ; libellés « P2 dépend » (l. 308-311, par drapeau) et « P1 dépend » (l. 317-329, par `double_calcul`) ; trois mentions (l. 354-356, 420) | **Manquent** : `mentions_audit` sans aucune mention (v1 l. 190 : `== []`) ; symétrie de l'intervalle (v1 l. 204 : `abs((100 − bas) − (haut − 100)) ≤ 4`), la v3 l. 424-425 ne garde que les bornes. |
| D-8 docstring de `validite` | **fait** | 211-214 | sans objet | Docstring du module (P-9), l. 17-18 : renvoie à `lecture_v1.py`, voir E-4. |
| D-9 ordre des causes, libellé | **fait au code ; addendum non trouvé** | 251-257 (inchangées) | l. 308-314, 317-329 | Ordre conforme au texte (« validité d'abord … P3, P2 », puis P1). L'écriture du libellé « P2 dépend des égalités » avec P-1 dans l'addendum n'apparaît dans aucun `lectures-*addendum-condition6-v*.md` (recherche `grep` de « dépend » : aucune ligne). À porter à l'addendum. |
| D-10 `rang` dans `Evaluation`, exigé 3 | **fait** | 89, 98, 185-186 | `test_double_calcul_exige_rang_3` (l. 332-336) | Défaut `rang: int = 3` : voir E-6. |
| D-11 `garde_graines` clé non itérable | **fait** | 336-342 | l. 404-408 (`cle_reechantillonnage = 2`, manifeste `None`) | |
| D-11 `intervalle_rappel` tirages ≥ 1 | **fait** | 465-466 | l. 411-414 (`tirages = 0`) | `tirages=True` passe le contrôle : voir E-7. |

## Défauts neufs ou restes (sonde `sonde_d3_d11.py`)

**E-1 (à corriger : reste de la correction 6 exigée ; sans effet sur une issue).** `mentions_audit` accepte des comptes
non entiers et des booléens. Sonde S1 : `mentions_audit([0.0, 0.0], [150.5, 150.5])` rend `["trop beau", "valeurs
identiques à tous les tours"]` ; `([0.4, 0.2], [190.5, 191])` rend `["trop beau"]` alors que R_att n'est pas nul ;
`([True, True], [150, 150])` rend une mention. Les mentions sont des réserves, pas des issues, et l'appelant
(`lecture_v8.py` l. 742) passe des comptes de `evaluer` et `taux_juge` ; mais le texte veut « toutes les comparaisons à un
seuil … sur des comptes entiers » (« Métrique », point 1) et la correction 6 le nommait. Correction : `r_att, j =
_entiers(r_att, "audit, R_att"), _entiers(j, "audit, J")` après l. 447 ; essai avec un flottant et un booléen.

**E-2 (à préciser).** Régression de `_exact` sur les `Fraction` : la v2 les rendait exactement (`Fraction(x)`), la v3
les fait passer par `float` (l. 296-302). Sonde S2 : `nombre_de_tours(30, Fraction(5, 6), 1, 2000)` rend K = 29 en v3,
30 en v2 et en arithmétique exacte (`72 000 × (30 − 10 − 5/6) / (23 × 2 000) = 30`) ; la chaîne `"5/6"` rend 30. Les
appelants vus passent des `float` Python (`lanceur_v9.py` l. 1223 : `round(d, 4)`) : sans effet aujourd'hui.
Correction : `if isinstance(x, numbers.Rational): return Fraction(x)` avant la conversion par `float`, ou refuser
`Fraction` ; essai sur le cas S2.

**E-3 (à préciser).** `verdict` lit les clés de l'audit sans contrôler leur type. Sonde S4 : `mentions="trop beau"`
(chaîne) donne neuf réserves d'une lettre (« à examiner : t ; à examiner : r ; … ») ; `defaut="non"` rend « Non
interprétable (audit de symétrie). » ; `audit=None` lève `TypeError` et non `GardeArret`. L'appelant construit l'audit
avec `bool(...)` et une liste (`lecture_v8.py` l. 742) : sans effet. Correction : exiger `audit` dict,
`defaut is True or defaut is False`, `clos` de même, `mentions` liste de chaînes, sinon `GardeArret` ; un essai.

**E-4 (à préciser).** La docstring du module (l. 17-18) dit les grandeurs rapportées calculées « par `lecture_v1.py` ».
`lecture_v1.py` importe `analyse_v2` (l. 24) ; les lectures qui emploient `analyse_v3` sont `lecture_v2.py` à
`lecture_v8.py` (calcul des grandeurs : `lecture_v8.py` l. 634-662). Correction : nommer la lecture en vigueur, ou écrire
« par le module de lecture qui importe celui-ci ».

**E-5 (à préciser).** `garde_par_tour(…, evaluations_attendues: int = 2)` : la valeur par défaut double la constante de
`conventions_v2`/`v3`. Un appelant qui l'omet reçoit 2 sans le dire (sonde S7 : il tombe bien sur une seule évaluation).
Valeur égale aujourd'hui : sans effet. Correction : paramètre sans défaut, ou défaut lu de la convention.

**E-6 (à préciser).** `Evaluation.rang` a pour défaut 3 (l. 89). Une `Evaluation` bâtie à la main au seuil de rang 5
sans dire son rang passe `double_calcul` (sonde S5b : rend K′ = 2 ; avec `rang=5` explicite, S5c : `GardeArret`). Seul
`evaluer` construit des `Evaluation` dans le paquet (recherche `Evaluation(` : l. 96 seulement) : sans effet.
Correction : champ sans défaut.

**E-7 (à préciser).** `intervalle_rappel(…, tirages=True)` passe le contrôle `isinstance(tirages, int)` (l. 465) puis
lève `TypeError` dans `rng.integers` (sonde S6b), au lieu de `GardeArret`. À l'inverse, `np.int64(10)` est refusé
(S6a). L'appelant (`lecture_v8.py` l. 674-677) passe le défaut 10 000 : sans effet. Correction : refuser `bool`,
accepter `np.integer`, comme `_entiers`.

## Corrections

1. **(à corriger, E-1 / D-6)** `mentions_audit` : comptes entiers exigés par `_entiers` ; essai flottant et booléen.
2. **(à corriger, D-7)** Essais : `mentions_audit` sans aucune mention (`[10, 20, 5]`, `[150, 120, 170]` → `[]`) ;
   symétrie de l'intervalle (`abs((100 − bas) − (haut − 100)) ≤ 4`, comme v1 l. 204). Facultatif : `np.float32` sur
   `garde_depense`.
3. **(à préciser, E-2)** `_exact` : `Fraction` rendue exactement (ou refusée) ; essai du cas S2.
4. **(à préciser, E-3)** `verdict` : types de `audit` contrôlés, `GardeArret` sinon.
5. **(à préciser, E-4)** Docstring du module : lecture en vigueur nommée.
6. **(à préciser, D-9)** Addendum de la condition 6 : écrire le libellé « P2 dépend des égalités » avec P-1.
7. **(à préciser, E-5, E-6, E-7)** Retirer les défauts `evaluations_attendues = 2` et `rang = 3` ; `tirages` : refuser
   `bool`, accepter `np.integer`.

Aucune de ces corrections ne change une issue de la table « Critères de lecture gelés » sur les entrées que produisent
les appelants vus ; la correction 1 achève une correction déjà exigée.
