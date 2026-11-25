# Corrections de contre-lecture sur le code des lectures de la course v5 (barreau 8, côté exposé)

> EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce du côté exposé : jamais transmise au côté des moniteurs ni à un concepteur de moniteur. Pièce de classe B/C consignant les corrections appliquées à la suite de la contre-lecture de conformité.

- **Contre-lecture traitée** : `contre-lecture-code-lectures-v5-neon-v1.md` (verdict `conforme sous corrections` : 0 bloquant, 2 majeurs `CLN-01` à `CLN-02`, 5 mineurs `CLN-03` à `CLN-07`).
- **Base de code corrigée** : commit `c5d90370` de la branche `barreau8/code-lectures-v5-cote-expose-v1`.
- **Spécification scellée de référence** : `docs/notes/barreau8-cote-expose-pieces-lecture-v1/specification-lectures-dommage-diffusion-course-v5-v1-brouillon3.md`, SHA-256 `acce24e76e17bffb2938616f2204d068a1f61d5e71938ce8a33e1e6a83a7407e` (vérifiée inchangée).
- **Accord** : `GO-2026-11-24-37`.
- **Décision prise en compte** : `R-5383` (option **(a)** sur l'écart 3, consignée dans `rapport-developpeur-code-lectures-v5-v1-erratum-1.md`).
- **Date** : 2026-11-25.

---

## 1. Tableau des sept corrections (`CLN-01` à `CLN-07`)

Aucun des quinze modules d'origine gelés (section 19 de la spécification) n'a été modifié. Aucune formule statistique, aucun seuil, ni aucune clé attendue par le programme d'extrait des états n'est changé.

| Constat | Gravité | Fichier(s) modifié(s) | Diff résumé | Nouveaux essais ajoutés (`tests/test_lectures_iib_v5_v1.py`) |
|---|---|---|---|---|
| `CLN-01` | Majeur | `src/controle_ia/iib/lectures_v5.py` | Expression régulière `_GO` bornée à gauche et à droite : `(?<![A-Za-z0-9-])GO-\d{4}-\d{2}-\d{2}-\d{2}(?![A-Za-z0-9-])`. Rejette tout préfixe ou suffixe alphanumérique ou tiret tout en acceptant espaces, parenthèses et accents graves. | 5 cas d'artefact ajoutés dans `test_garde_de_l_audit_artefacts` : `GO-2026-11-24-370`, `XGO-2026-11-24-37-bis`, `XGO-2026-11-24-37`, `GO-2026-11-24-37-bis`, et double identifiant sur une même ligne. |
| `CLN-02` | Majeur | `scripts/lecture_iib_audit_r4_v5.py` | Précalcul de tous les préfixes décodés `ev.decoder(jet, decodes[(c, t, pas)]["ids"][:rang], ...)` dans le bloc `try ... except GardeArret`, avant tout `print` sur la sortie standard ; la boucle d'affichage ne fait plus que lire `prefixes[(c, t, pas)]`. | `test_script_d_audit_decodage_prefixe_infidele_sans_affichage` : vérifie qu'une divergence sur le seul préfixe tronqué retourne le code 1, laisse `stdout` vide, écrit le motif sur `stderr` et n'écrit rien sur disque. |
| `CLN-03` | Mineur | `src/controle_ia/iib/entrees_lectures_v5.py` | Dans `exiger_ordre_du_temps`, interception de `ValueError` autour de `datetime.strptime(heure, "%Y-%m-%dT%H:%M:%SZ")` et levée de `GardeArret(f"{cle_t0} : heure illisible (AAAA-MM-JJTHH:MM:SSZ)") from None`. | 2 cas d'artefact ajoutés dans `test_t0_artefacts` : `date_impossible` (`2026-02-30T10:00:00Z`) et `mois_impossible` (`2026-13-01T10:00:00Z`). |
| `CLN-04` | Mineur | `scripts/lecture_iib_2_diffusion_v5.py`, `scripts/lecture_iib_audit_r4_v5.py` | Ajout de `if mode == "reel" and racine != cl.racine_du_code().resolve(): raise GardeArret(...)` dès le début de `main()` (juste après `cl.pour(...)`), avant toute ouverture de `diag/RUN/NOM_1` en mode réel. Note : `scripts/lecture_iib_1_dommage_v5.py` n'ouvre rien sous `--racine` avant `ev.charger` (qui porte déjà ce contrôle en tête) et conserve l'ordre `T0` avant `--racine` vérifié par `test_scripts_mode_reel_refuse_les_options_d_essai_et_une_racine_autre`. | `test_scripts_mode_reel_refuse_racine_etrangere_avant_lecture_1` : vérifie que `lecture_iib_2_diffusion_v5.main` et `lecture_iib_audit_r4_v5.main` en mode réel refusent une racine étrangère portant `diag/RUN/NOM_1` (`declenche=False`) avec le motif `racine du code` (et non `audit non déclenché`). |
| `CLN-05` | Mineur | `src/controle_ia/iib/lectures_v5.py`, `scripts/lecture_iib_audit_r4_v5.py` | Dans `exiger_audit_consigne` (et dans `lecture_iib_audit_r4_v5.py` par cohérence), exigence stricte `isinstance(declenche, bool)` avant test (plus de conversion silencieuse `bool(None) -> False`). Lorsque `DEFAUT-AUTORISE` apparaît sans ligne `DEFAUT` préalable, `accord` est renseigné à partir des lignes `DEFAUT-AUTORISE` en cohérence avec `accords`. | `test_garde_de_l_audit_declenche_non_booleen_et_autorise_isole` : vérifie le refus pour `declenche` dans `(None, "false", 0, 1)` et la cohérence `accord == "GO-2026-11-24-37"` / `accords == ["GO-2026-11-24-37"]` sur un `DEFAUT-AUTORISE` isolé. |
| `CLN-06` | Mineur | `src/controle_ia/iib/lectures_v5.py`, `tests/test_lectures_iib_v5_v1.py` | Dans `puissance`, ajout de `not math.isfinite(emd) or emd < 0` à la garde sur `EMD`, et contrôle de type numérique fini non booléen sur `exces_moyen_honnete`. | Dans `test_puissance_trois_parts_et_part_citee` : refus de `EMD` dans `(-0.05, NaN, +inf, -inf, True, "0.05")` et de `exces_moyen_honnete` dans `(True, "0.02", NaN, +inf)`. Dans `test_citation_artefacts` : essai `p_cite=None` étendu aux 4 phrases (`PHRASES_1`) et aux 2 oracles (`N`, `P`), couvrant complètement `R-5383`. |
| `CLN-07` | Mineur | `src/controle_ia/iib/entrees_lectures_v5.py` | (1) Dans `exiger_lignes_de_l_evaluation` (E8), contrôle `isinstance(l["phase"], str)` et `_entier(l["pas"])` avant construction de la clé de `index_ev`. (2) Dans `_charger_identifiants` (E10), comparaison valeur et type stricts `_egal_types_stricts(ens[k], reunion[k])` refusant `1 == True == 1.0`. (3) Ajout de `exiger_controle_premier_cout` appelé dans `charger` avant création du manifeste (présence des 4 conditions et des clés `phrase`, `validite`, `alerte`). | 3 cas dans `test_e8_artefacts` (`pas_liste_evaluation`, `pas_booleen_evaluation`, `phase_liste_evaluation`) ; `test_e8_precontrole_controle_premier_cout` ; `test_e10_types_stricts_tranche_vs_ensemble` (cas sain `1` et artefacts `True`, `1.0`). |

---

## 2. Empreintes SHA-256 des sept fichiers de code et d'essais

| Fichier | État | Taille (octets) | SHA-256 au commit `c5d90370` | SHA-256 après corrections |
|---|---|---:|---|---|
| `scripts/lecture_iib_1_dommage_v5.py` | Inchangé | 5 370 | `11b41164372bde2f5cac573dba22325c75cc3352cd85cead4315832c9fd28367` | `11b41164372bde2f5cac573dba22325c75cc3352cd85cead4315832c9fd28367` |
| `scripts/lecture_iib_2_diffusion_v5.py` | Modifié (`CLN-04`) | 8 490 | `15ffa52fe475c8619c9c4a3439c2fbb7aed83f75e6fb546f68d9882acd324e1e` | `0a381a4c39011089a8ef5a92677d12e477935dc2bf427bed8e569bbce09efec3` |
| `scripts/lecture_iib_audit_r4_v5.py` | Modifié (`CLN-02`, `CLN-04`, `CLN-05`) | 6 692 | `92c5e0770e888245d6f76d542556d7adadb2329ff047dc10ce71fb147527a0f4` | `ec4c1a219ae020675491370a11e253b04bb19dd2abe784531da1dc4068d155ce` |
| `src/controle_ia/iib/configuration_lectures_v5.py` | Inchangé | 15 882 | `3c8232036bb84938ae3086e8ae9e8d565a68a2248e0d9ad64a2b5d34d9821c4f` | `3c8232036bb84938ae3086e8ae9e8d565a68a2248e0d9ad64a2b5d34d9821c4f` |
| `src/controle_ia/iib/entrees_lectures_v5.py` | Modifié (`CLN-03`, `CLN-07`) | 45 927 | `8e1846c3e76fe7e3eb7ad355c2eb05808f7605f2bf42dcc5e42aa99d603d4adf` | `d97eff6317794f094fefd74bb7ff164273e28385802e86a5fbc4d96fd3b07357` |
| `src/controle_ia/iib/lectures_v5.py` | Modifié (`CLN-01`, `CLN-05`, `CLN-06`) | 26 090 | `0f48f8ec5dbf5afd76d85b950eb6c7b10077544c688a3d8f77a98b5ce82659ca` | `831bfa14d9fec9f5ebfeeb63c42c952de6acabd067ba4a454bcce97e663636ef` |
| `tests/test_lectures_iib_v5_v1.py` | Modifié (`CLN-01` à `CLN-07`) | 96 884 | `47c04f22516e7ae8a964a9b58641c154fbd4eb7a9f7ee660a0459eea643400bb` | `85967c0cee5468801a57996ae9663748ad94027321af62b5dc671902adc51e80` |

Fins de ligne vérifiées en LF (`\n`) sur les sept fichiers ; aucun répertoire `__pycache__` produit (`PYTHONDONTWRITEBYTECODE=1`).

---

## 3. Vérifications exécutées

1. **Spécification scellée et quinze modules d'origine** : `configuration_lectures_v5.exiger_specification()` et `configuration_lectures_v5.exiger_modules_d_origine()` passent sans écart.
2. **Vérification par programme des sept constats (`CLN-01` à `CLN-07`)** : chacun des sept cas reproducteurs exacts du rapport `contre-lecture-code-lectures-v5-neon-v1.md` est vérifié corrigé (y compris contrôle AST et exécution réelle sur `CLN-02`).
3. **Suite d'essais unitaires autonomes (`tests/test_lectures_iib_v5_v1.py`)** : 168 cas collectés (contre 153 au commit `c5d90370`, soit +15 cas neufs) ; **81/81 essais unitaires autonomes passés** en 8,76 s dans l'environnement Windows isolé (`Python 3.14.3`, `numpy 2.4.4`, `pytest 9.0.3`, avec adaptateur en mémoire pour `scipy.stats.rankdata` et substitut `torch`, sans exécution des essais dépendant de la course jouet `lanceur_v5` sur Windows ni des objets du jetoniseur réel).

---

## 4. Attestation de cloisonnement

Travail exécuté exclusivement dans le répertoire isolé du sous-agent sur les pièces du mandat et les modules de code source pur du commit `c5d90370`. Aucune sortie réelle de la course, aucun épisode, score, activation, verdict, lecture réelle, branche `essai/iib-explo-*`, ni aucun fichier sous `donnees/`, `verdict/`, `lecture/`, `coffre/`, `prereg/`, `registres/` ou `consignes/` n'a été ouvert ni consulté.
