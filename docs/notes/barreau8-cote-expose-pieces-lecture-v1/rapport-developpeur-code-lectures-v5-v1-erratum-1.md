# Erratum 1 au rapport du développeur : code des lectures du dommage et de la diffusion sur la course v5, version 1

> EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce du côté exposé : jamais transmise au côté des moniteurs ni à un concepteur de moniteur.

- **Pièce amendée** : `docs/notes/barreau8-cote-expose-pieces-lecture-v1/rapport-developpeur-code-lectures-v5-v1.md`, commit `c5d90370`, SHA-256 `dcd7ca062f450381db70ccad373e83cf4f9d2901b23291b9a7f93b66e504cbb8` (conservée intacte, R12).
- **Spécification scellée** : `docs/notes/barreau8-cote-expose-pieces-lecture-v1/specification-lectures-dommage-diffusion-course-v5-v1-brouillon3.md`, SHA-256 `acce24e76e17bffb2938616f2204d068a1f61d5e71938ce8a33e1e6a83a7407e`.
- **Accord** : `GO-2026-11-24-37`.
- **Date** : 2026-11-25.

---

## 1. Décision `R-5383` sur l'écart 3 (section 4 du rapport du développeur)

Dans la section 4 du rapport du développeur (`dcd7ca06…`, point 3), l'écart relatif à la section 10.1 de la spécification scellée était soumis à l'arbitrage de la session mère : comportement de la clé `citation.texte` de la lecture du dommage lorsque la part citée `p_cite` n'est pas calculable (`None`).

- **Décision consignée (`R-5383`)** : la session mère a tranché en faveur de l'**option (a)**, conforme à la lettre de la spécification scellée (section 10.1 : « Si *p* n'est pas calculable, `texte` est nul et `motif` le dit ; la phrase d'origine reste »). En conséquence, `citation["texte"]` vaut `None` avec un `motif` explicite dès que `p_cite` est `None`, **quelle que soit la phrase d'origine** (y compris « dommage agrégé vu », « dommage non distingué du témoin-jumeau » et « non calculable »).
- **État du code** : `src/controle_ia/iib/lectures_v5.py` (`citation_dommage`) implémentait déjà exactement l'option (a) au commit `c5d90370` ; aucune modification de logique métier n'a été nécessaire.
- **Couverture d'essais** : à la suite du constat `CLN-06` de la contre-lecture (`contre-lecture-code-lectures-v5-neon-v1.md`), `tests/test_lectures_iib_v5_v1.py` (`test_citation_artefacts`) vérifie désormais explicitement le comportement `p_cite=None` sur les **quatre phrases** de la lecture du dommage et pour les **deux oracles** (`N` et `P`).

---

## 2. Mise à jour des empreintes après traitement de la contre-lecture (`CLN-01` à `CLN-07`)

À la suite de la contre-lecture `contre-lecture-code-lectures-v5-neon-v1.md` (verdict `conforme sous corrections`), les sept constats `CLN-01` à `CLN-07` ont été corrigés sans modification des quinze modules d'origine ni des formules statistiques (détail dans `corrections-cl-neon-code-lectures-v5-v1.md`). Les empreintes actualisées des sept fichiers de code et d'essais sont les suivantes :

| Fichier | État par rapport à `c5d90370` | Empreinte SHA-256 |
|---|---|---|
| `src/controle_ia/iib/configuration_lectures_v5.py` | Inchangé | `3c8232036bb84938ae3086e8ae9e8d565a68a2248e0d9ad64a2b5d34d9821c4f` |
| `src/controle_ia/iib/entrees_lectures_v5.py` | Corrigé (`CLN-03`, `CLN-07`) | `d97eff6317794f094fefd74bb7ff164273e28385802e86a5fbc4d96fd3b07357` |
| `src/controle_ia/iib/lectures_v5.py` | Corrigé (`CLN-01`, `CLN-05`, `CLN-06`) | `831bfa14d9fec9f5ebfeeb63c42c952de6acabd067ba4a454bcce97e663636ef` |
| `scripts/lecture_iib_1_dommage_v5.py` | Inchangé | `11b41164372bde2f5cac573dba22325c75cc3352cd85cead4315832c9fd28367` |
| `scripts/lecture_iib_2_diffusion_v5.py` | Corrigé (`CLN-04`) | `0a381a4c39011089a8ef5a92677d12e477935dc2bf427bed8e569bbce09efec3` |
| `scripts/lecture_iib_audit_r4_v5.py` | Corrigé (`CLN-02`, `CLN-04`, `CLN-05`) | `ec4c1a219ae020675491370a11e253b04bb19dd2abe784531da1dc4068d155ce` |
| `tests/test_lectures_iib_v5_v1.py` | Corrigé (`CLN-01` à `CLN-07`, `R-5383`) | `85967c0cee5468801a57996ae9663748ad94027321af62b5dc671902adc51e80` |
