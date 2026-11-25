# Vérification des corrections de contre-lecture sur le code des lectures du dommage et de la diffusion (course version 5, barreau 8, côté exposé)

> EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce du côté exposé : jamais transmise au côté des moniteurs ni à un concepteur de moniteur.

- **Verdict** : **`conforme`** (les sept constats `CLN-01` à `CLN-07` sont intégralement levés ; aucun constat résiduel ; aucune régression ; les quinze modules d'origine gelés sont strictement inchangés).
- **Vérificateur** : même contre-lecteur de classe B, modèle Gemini 4 Neon (chaîne de classe B ; contre-lecture initiale `contre-lecture-code-lectures-v5-neon-v1.md`, empreinte SHA-256 `073ee9667d15c1311674962562d3bc63ae9057ef43a461d5373c0486f107650c`).
- **Spécification scellée de référence** : `docs/notes/barreau8-cote-expose-pieces-lecture-v1/specification-lectures-dommage-diffusion-course-v5-v1-brouillon3.md`, empreinte SHA-256 vérifiée `acce24e76e17bffb2938616f2204d068a1f61d5e71938ce8a33e1e6a83a7407e`.
- **Accord** : `GO-2026-11-24-37`.
- **Décision vérifiée** : `R-5383` (option **(a)** sur l'écart 3 du rapport du développeur, consignée dans `rapport-developpeur-code-lectures-v5-v1-erratum-1.md`).
- **Date** : 2026-11-25.

---

## 1. Vérification des empreintes SHA-256 et de l'intégrité des modules gelés

Les sept fichiers de code et d'essais de `v2-corrige\` ont été vérifiés en fins de ligne Unix (`\n`) et concordent sur les 64 caractères hexadécimaux avec les empreintes consignées dans `corrections-cl-neon-code-lectures-v5-v1.md` et `rapport-developpeur-code-lectures-v5-v1-erratum-1.md` :

| Fichier | État par rapport au commit `c5d90370` | Empreinte SHA-256 vérifiée |
|---|---|---|
| `scripts/lecture_iib_1_dommage_v5.py` | Inchangé | `11b41164372bde2f5cac573dba22325c75cc3352cd85cead4315832c9fd28367` |
| `scripts/lecture_iib_2_diffusion_v5.py` | Corrigé (`CLN-04`) | `0a381a4c39011089a8ef5a92677d12e477935dc2bf427bed8e569bbce09efec3` |
| `scripts/lecture_iib_audit_r4_v5.py` | Corrigé (`CLN-02`, `CLN-04`, `CLN-05`) | `ec4c1a219ae020675491370a11e253b04bb19dd2abe784531da1dc4068d155ce` |
| `src/controle_ia/iib/configuration_lectures_v5.py` | Inchangé | `3c8232036bb84938ae3086e8ae9e8d565a68a2248e0d9ad64a2b5d34d9821c4f` |
| `src/controle_ia/iib/entrees_lectures_v5.py` | Corrigé (`CLN-03`, `CLN-07`) | `d97eff6317794f094fefd74bb7ff164273e28385802e86a5fbc4d96fd3b07357` |
| `src/controle_ia/iib/lectures_v5.py` | Corrigé (`CLN-01`, `CLN-05`, `CLN-06`) | `831bfa14d9fec9f5ebfeeb63c42c952de6acabd067ba4a454bcce97e663636ef` |
| `tests/test_lectures_iib_v5_v1.py` | Corrigé (`CLN-01` à `CLN-07`, `R-5383`) | `85967c0cee5468801a57996ae9663748ad94027321af62b5dc671902adc51e80` |

L'appel effectif à `configuration_lectures_v5.exiger_specification()` et `configuration_lectures_v5.exiger_modules_d_origine()` passe sans écart : la spécification scellée (`acce24e7…`) et les **quinze modules d'origine gelés** de la section 19 sont strictement intacts.

---

## 2. Vérification constat par constat (`CLN-01` à `CLN-07` et erratum `R-5383`)

| Constat | Gravité initiale | Vérification sur le code et par essai indépendant | Statut |
|---|---|---|---|
| `CLN-01` | Majeur | `src/controle_ia/iib/lectures_v5.py` (ligne 30) : `_GO` bornée à gauche et à droite par `(?<![A-Za-z0-9-])GO-\d{4}-\d{2}-\d{2}-\d{2}(?![A-Za-z0-9-])`. Rejeu indépendant confirmé : les cinq variantes mal formées (`GO-2026-11-24-370`, `XGO-2026-11-24-37-bis`, `XGO-2026-11-24-37`, `GO-2026-11-24-37-bis`, double identifiant) sont rejetées par `GardeArret`, tandis que les formes valides (nu, entre accents graves, entre parenthèses) sont acceptées. | **Levé** |
| `CLN-02` | Majeur | `scripts/lecture_iib_audit_r4_v5.py` (lignes 74 à 80) : tous les préfixes décodés `ev.decoder(jet, decodes[(c, t, pas)]["ids"][:rang], ...)` sont désormais calculés **à l'intérieur** du bloc `try ... except GardeArret` (clos ligne 80), avant le premier `print` (ligne 83). L'essai `test_script_d_audit_decodage_prefixe_infidele_sans_affichage` prouve le retour en code 1, une sortie standard vide, le motif sur sortie d'erreur et l'absence d'écriture sur disque. | **Levé** |
| `CLN-03` | Mineur | `src/controle_ia/iib/entrees_lectures_v5.py` (lignes 220 à 223) : `datetime.strptime` encadré par `try ... except ValueError` levant `GardeArret` (enveloppé par le motif `T0`). Rejeu indépendant confirmé sur `2026-02-30T10:00:00Z`, `2026-13-01T10:00:00Z` et `2026-11-21T25:00:00Z`. | **Levé** |
| `CLN-04` | Mineur | `scripts/lecture_iib_2_diffusion_v5.py` (lignes 57 à 58) et `scripts/lecture_iib_audit_r4_v5.py` (lignes 40 à 41) : contrôle immédiat `mode == "reel" and racine != cl.racine_du_code().resolve()` avant toute ouverture de `diag/RUN/NOM_1`. Le maintien inchangé de `scripts/lecture_iib_1_dommage_v5.py` est justifié (ce script n'ouvre rien sous `--racine` avant `ev.charger` et conserve l'ordre `T0` avant `--racine` exigé par l'essai antérieur). Rejeu indépendant confirmé. | **Levé** |
| `CLN-05` | Mineur | `src/controle_ia/iib/lectures_v5.py` (lignes 211 à 215 et 247 à 250) et `scripts/lecture_iib_audit_r4_v5.py` (lignes 49 à 54) : exigence stricte `isinstance(declenche, bool)` sans conversion silencieuse (R5), refusant `None`, `"false"`, `0`, `1` ; sur `DEFAUT-AUTORISE` isolé sans `DEFAUT` préalable, `accord` concorde désormais avec `accords`. Rejeu indépendant confirmé. | **Levé** |
| `CLN-06` | Mineur | `src/controle_ia/iib/lectures_v5.py` (lignes 100 à 104) : refus d'un effet minimal détectable non fini ou strictement négatif, et contrôle numérique fini non booléen de `exces_moyen_honnete` (tout en autorisant légitimement un excès moyen honnête négatif). Dans `tests/test_lectures_iib_v5_v1.py` (lignes 1012 à 1016), couverture complète de `R-5383` (`p_cite=None`) sur les 8 couples `(N, P) × (4 phrases)`. Rejeu indépendant confirmé. | **Levé** |
| `CLN-07` | Mineur | `src/controle_ia/iib/entrees_lectures_v5.py` (lignes 383 à 386, 424 à 443, 538 et 601) : (1) garde `isinstance(l["phase"], str)` et `_entier(l["pas"])` avant hachage dans `evaluation-iib-v5.json` ; (2) comparaison stricte valeur et type `_egal_types_stricts` entre tranches et fichier d'ensemble (refusant `1 == True == 1.0` et `0 == False`) ; (3) précontrôle `exiger_controle_premier_cout` appelé dans `charger` avant création du manifeste. Rejeu indépendant confirmé. | **Levé** |
| Erratum `R-5383` | — | `rapport-developpeur-code-lectures-v5-v1-erratum-1.md` relue intégralement : conserve intact le rapport initial (`dcd7ca06…`, règle R12), consigne exactement l'arbitrage `R-5383` en option **(a)**, atteste l'absence de changement de logique métier et recense exactement les sept empreintes actualisées. | **Conforme** |

---

## 3. Essais exécutés et vérification d'absence de régression

1. **Vérification indépendante (`verifier_corrections_v2.py`, `PYTHONDONTWRITEBYTECODE=1`)** : **8/8 vérifications passées** (concordance des 7 empreintes SHA-256 de `v2-corrige\`, intégrité de la spécification scellée et des 15 modules d'origine, et validation positive et négative de chacun des 7 constats `CLN-01` à `CLN-07` ainsi que de la décision `R-5383`).
2. **Suite d'essais unitaires autonomes (`tests/test_lectures_iib_v5_v1.py`, `PYTHONDONTWRITEBYTECODE=1`)** : **168 cas collectés** (+15 cas neufs par rapport aux 153 du commit `c5d90370`), dont **81/81 essais unitaires autonomes passés** en 23,28 s dans l'environnement isolé (`Python 3.14.3`, `numpy 2.4.4`, `pytest 9.0.3`, avec adaptateur en mémoire pour `scipy.stats.rankdata` et substitut vide `torch`), incluant la totalité des nouveaux essais couvrant `CLN-01` à `CLN-07` et `R-5383`, sans aucune régression.
3. **Portée environnementale notée pour transparence** : l'environnement `venv-py314` du répertoire parent n'étant pas accessible depuis le bac à sable du sous-agent, les 87 essais dépendant de la fabrication locale sous Windows de la course jouet (`lanceur_v5.py` ligne 469, séparateurs inversés sous Windows sans objet sous Linux), des objets Git `e5677bbf` du jetoniseur réel ou de `scipy.optimize` (`mots_et_cout_t06_v3.py`) n'ont pas été rejoués dans ce bac à sable ; aucune de ces branches de calcul n'a été modifiée par les sept corrections (aucune formule statistique, aucun appel à `lecture_v1` ni à `mots_et_cout_t06_v3.py` n'a changé).

---

## 4. Qui a lu quoi (attestation stricte de cloisonnement)

Le contre-lecteur atteste qu'aucune sortie réelle de la course, aucun épisode, score, activation, adaptateur, verdict, lecture réelle, branche `essai/iib-explo-*`, fichier sous `donnees/`, `verdict/`, `docs/verdicts/`, `lecture/`, `coffre/`, `prereg/`, `registres/` ou consigne privée n'a été ouvert ni consulté.

**Pièces lues pour cette vérification** (exclusivement sous `v2-corrige\` et dans l'espace de travail isolé du sous-agent) :
- `v2-corrige\corrections-cl-neon-code-lectures-v5-v1.md` ;
- `v2-corrige\rapport-developpeur-code-lectures-v5-v1-erratum-1.md` ;
- `v2-corrige\scripts\lecture_iib_1_dommage_v5.py`, `lecture_iib_2_diffusion_v5.py`, `lecture_iib_audit_r4_v5.py` ;
- `v2-corrige\src\controle_ia\iib\configuration_lectures_v5.py`, `entrees_lectures_v5.py`, `lectures_v5.py` ;
- `v2-corrige\tests\test_lectures_iib_v5_v1.py` (sections modifiées et nouveaux essais, ainsi que vérification d'empreinte complète sur la copie miroir locale).
