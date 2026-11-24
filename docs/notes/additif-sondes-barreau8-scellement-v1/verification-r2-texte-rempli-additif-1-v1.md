# Vérification R2 finale du texte rempli candidat au scellement — Additif 1 aux sondes du barreau 8 (v1)

- **Vérificateur** : sous-agent R2 neuf du côté des moniteurs (`14d827e0cd96a5312eca5d2c6f4f37b2`), strictement aveugle.
- **Date et heure (UTC)** : `2026-11-24T04:14:30Z` (`date -u`).
- **Dépôt contrôlé (lecture seule)** : `/home/antigravity/lciric/controle-ia-travail`, branche `main`, commit `b90f1b48a70a0098541a4976db2f61e5593fe971` (`git status --porcelain` vide, `PYTHONDONTWRITEBYTECODE=1`).
- **Candidat contrôlé** : `/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/scellement-additif-b8-final/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-candidat-rempli.md` (`623` lignes, `195 155` octets, SHA-256 `0268711768756414642d8a93247336c4d00e3cf5ac132d6fdd5836ee9d19c413`, compagnon `.sha256` égal).

---

## Verdict

**NON CONFORME EN L'ÉTAT — LISTE FERMÉE DE 2 ERREURS D'EMPREINTES SHA-256 À LA LIGNE 619 (`Contre-lecture 2`)**

Tous les autres contrôles (différentiel strict des 8 lignes autorisées, validateur `controle_ia.prereg.problemes == []`, empreintes de `AD-2`/`AD-3`/`AD-4`/préfixes de `536`, forme normative de `AD-3`, concordance de `AD-1`/`AD-4`/`AD-6`, étanchéité de l'ordre neuf et schéma JSON fermé à 9 clés de `D-6`) sont **100 % conformes**. Dès remplacement des deux empreintes erronées de la ligne `619` ci-dessous et recalcul du `.sha256`, le texte est prêt pour le scellement.

---

## Liste fermée des erreurs bloquantes (2 erreurs, toutes deux en ligne 619)

1. **`E-1` — Ligne `619` (`Contre-lecture 2`) : empreinte SHA-256 erronée pour `docs/notes/additif-sondes-barreau8-scellement-v1/contre-lecture-additif-1-brouillon6-opus-v1.md`**
   - Valeur écrite en ligne `619` : `f9379270db379fd5189166a6571f13edbb905e4d4cc10de0f0ac53430e5d4c55` (seul le préfixe à 8 caractères `f9379270` est exact ; contredit en outre la ligne `28` du même fichier).
   - Empreinte réelle sur `main` (`b90f1b48a`) et dans son `.sha256` (ainsi qu'en ligne `28`) :
     `f9379270cddf80f25eb35f3079e03f0b423a6932e53075f0f592de53de857714`.

2. **`E-2` — Ligne `619` (`Contre-lecture 2`) : empreinte SHA-256 erronée pour `docs/notes/additif-sondes-barreau8-scellement-v1/corrections-brouillon6-vers-brouillon7-v1.py`**
   - Valeur écrite en ligne `619` : `3b46c67a0479df747f4570b47ba14002ab428fc41b9fa11fa8c4076850ba501a` (seul le préfixe à 8 caractères `3b46c67a` est exact).
   - Empreinte réelle sur `main` (`b90f1b48a`) et dans son `.sha256` :
     `3b46c67a7fa6b839e66a3d2f8b96faa580de09cc42e9dde6091ea4a7e8bca2b3`.

---

## Résultats détaillés des 5 contrôles exécutés par programme

### 1. Différentiel ligne à ligne contre `brouillon7.md` (`eb8b36e4…`) — **CONFORME**
- Nombre de lignes identique : `623` dans `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md` (`eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b`) et `623` dans `candidat-rempli.md`.
- Lignes modifiées : **exactement `[172, 173, 174, 175, 176, 177, 536, 619]`** (`0` autre ligne touchée).
- Sur les lignes `172` à `177` (`AD-1` à `AD-6`), seule la 3e cellule (`état`) a changé ; les cellules `id` et `champ` sont identiques à l'octet au brouillon 7. Conforme à la règle du scellement (ligne `136`) et à la liste d'arrêt (ligne `18`).

### 2. Validateur `controle_ia.prereg` et marqueurs résiduels — **CONFORME**
- `controle_ia.prereg.problemes(candidat-rempli.md)` == `[]` (8/8 sections présentes et non vides, section `Contre-lecture` valide).
- `controle_ia.scellement.verifier(candidat-rempli.md)` == `0268711768756414642d8a93247336c4d00e3cf5ac132d6fdd5836ee9d19c413`.
- Occurrences de `À REMPLIR` : `0` ; de `<<` : `0` ; de `>>` : `0` ; émojis / symboles `So` : `0`.

### 3. Empreintes SHA-256 à 64 hex dans `AD-2`, `AD-3`, `AD-4`, `536` et `619` contre `main` (`b90f1b48a`) — **NON CONFORME EN LIGNE 619 (7/9 exactes, 2/9 erronées)**

| Lieu | Pièce citée | SHA-256 cité dans `candidat-rempli.md` | SHA-256 réel sur `main` (`b90f1b48a`) + `.sha256` | Statut |
|---|---|---|---|---|
| `AD-2` (`L173`) | `docs/notes/barreau8-cote-moniteurs-entrees-v1/verification-exclus-ad2-sans-secret-v1.md` | `6b15e1dcb3ec4dd95d64bd2550c806d1b7de257ed4c5432a6eff76bc75e488d7` | `6b15e1dcb3ec4dd95d64bd2550c806d1b7de257ed4c5432a6eff76bc75e488d7` | **OK** |
| `AD-3` (`L174`) | `registres/qui-a-lu-quoi-v22.md` | `7b758ff0fe0c38a8f663946f40304213a151258371fcbeffb684b34d6d8aeed4` | `7b758ff0fe0c38a8f663946f40304213a151258371fcbeffb684b34d6d8aeed4` | **OK** |
| `AD-3` (`L174`) | `docs/notes/additif-sondes-barreau8-scellement-v1/verification-cote-expose-champs-additif-v1.md` | `b371a110680b612acc2170980588c721ea5ad0972171306c220f164fea16b841` | `b371a110680b612acc2170980588c721ea5ad0972171306c220f164fea16b841` | **OK** |
| `AD-4` (`L175`) | `docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-ordre-course-lue-additif-1-v1.json` | `8f6b502581cb32d546e84cf13d52d07f1faa011484ef585bde3635f56e86e76a` | `8f6b502581cb32d546e84cf13d52d07f1faa011484ef585bde3635f56e86e76a` | **OK** |
| `L536` | *(aucun hash à 64 hex ; 4 préfixes à 8 hex : `f9379270…`, `3b46c67a…`, `7b758ff0…`, `b371a110…`)* | — | 4/4 préfixes conformes | **OK** |
| `L619` | `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon6.md` | `bf10784207e6d74944d7d4804817c03eb8515d38e130ce282a577b4c96970b5e` | `bf10784207e6d74944d7d4804817c03eb8515d38e130ce282a577b4c96970b5e` | **OK** |
| `L619` | `docs/notes/additif-sondes-barreau8-scellement-v1/contre-lecture-additif-1-brouillon6-opus-v1.md` | `f9379270db379fd5189166a6571f13edbb905e4d4cc10de0f0ac53430e5d4c55` | `f9379270cddf80f25eb35f3079e03f0b423a6932e53075f0f592de53de857714` | **ERREUR (`E-1`)** |
| `L619` | `docs/notes/additif-sondes-barreau8-scellement-v1/corrections-brouillon6-vers-brouillon7-v1.py` | `3b46c67a0479df747f4570b47ba14002ab428fc41b9fa11fa8c4076850ba501a` | `3b46c67a7fa6b839e66a3d2f8b96faa580de09cc42e9dde6091ea4a7e8bca2b3` | **ERREUR (`E-2`)** |
| `L619` | `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md` | `eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b` | `eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b` | **OK** |
| `L619` | `docs/notes/additif-sondes-barreau8-scellement-v1/verification-r2-additif-barreau8-fable-brouillon7-v1.md` | `3d53c115226934535022bb5dee4f47f7bb0bc1493cd1c1e6aeca85d5f86c628d` | `3d53c115226934535022bb5dee4f47f7bb0bc1493cd1c1e6aeca85d5f86c628d` | **OK** |

### 4. Forme normative de `AD-3`, concordance `AD-1`/`AD-4`/`AD-6` et étanchéité de l'ordre neuf — **CONFORME**
- **`AD-3` (`L174` vs forme normative `L568`)** : les 8 segments de premier niveau séparés par `;` suivent dans l'ordre exact tous les préfixes prescrits par la ligne `568` (`première sortie de l'étalonnage : … (tous lancements compris ; nombre de lancements de l'étalonnage : 3)` ; `première sortie de la course : 2026-11-23T04:41:59Z` ; `fin de la course : 2026-11-23T13:20:20Z` ; `attestation écrite à : 2026-11-24T04:07:30Z` ; `lectures du dommage et de la diffusion jouées avant le scellement : non` ; `bornes (b1), (b2), (b3) et (b4) tenues : oui` ; `source de (b1) : …` ; `Lazar avait-il vu une sortie avant ses mots : non`), sans heure de scellement (qui relève de `SCELLEMENT-ADDITIF-1-SONDES-IIB`), et en concordance exacte avec `R-4726`, `R-4728`, `R-4747`, `R-5035`, `R-5173`, `R-5186` et `R-5217`.
- **`AD-1` (`L172`)** : cite `GO-2026-11-23-32` (et `GO-2026-11-23-16`, `-17` point 4, `-30`, `-33`, `-38`) avec les mots exacts de Lazar consignés dans `registres/go.md` (`L870`).
- **`AD-6` (`L177`)** : `GO-2026-11-22-75`, strictement égal à `ligne_de_calcul` de `attestation-ordre-course-lue-additif-1-v1.json` et conforme à `GO-2026-11-22-75`, `GO-2026-11-22-93`, `GO-2026-11-23-02` et `R-5035`.
- **Étanchéité (`L179`)** : `0` occurrence dans tout `candidat-rempli.md` des chemins, empreintes à 64 hex ou préfixes à 8 hex des trois pièces de l'ordre neuf (`8e1d340a…`, `7219083a…`, `a9d43d59…`, `brouillons/ii-b-saboteur-budget-v5/…`).

### 5. Schéma JSON fermé à 9 clés de `attestation-ordre-course-lue-additif-1-v1.json` (`8f6b5025…`) contre `D-6` (`L298`–`L300`) — **CONFORME**
- Décodage strict sans clé dupliquée : exactement les 9 clés `avertissement`, `agent`, `ordre`, `ligne_de_calcul`, `sections`, `faits`, `exclus`, `etalonnage`, `verdict_mecanique`.
- `avertissement` égal à la constante exigée ; `agent` = `{"session": "8f679a46f0f8fa95d2b414f233ddfa91", "a_ecrit_l_ordre": "non"}` ; `ordre` à 4 clés (`scelle: "oui"`, `pieces` à 2 entrées `scelle: "oui"`, empreintes 64 hex valides) ; `sections` à 5 clés exactes (`0`, `0 bis`, `7`, `8`, `13`) dans `{"changée", "absente"}` ; `faits` à 7 clés `O-1`..`O-7` avec `lieu` au format `<rang>:<numéro>` (`0:4.5`, `0:4.1`, `1:8`, `1:7` pour les 4 faits `"tient"`, `""` pour `O-3`, `O-5`, `O-6` `"non dit"`) ; `exclus` = `{"section": "1:8"}` ; `etalonnage` = `{"une_action_entre_dans_les_fichiers_de_l_evaluation": "non"}`.
- `verdict_mecanique == "écart"` est le résultat exact exigé par la règle de la ligne `298` dès lors que `O-3`, `O-5`, `O-6` valent `"non dit"`. Conformément à « Deux temps, deux versions (règle R12) » (ligne `300`), à `AD-4` (ligne `175`) et à la liste d'arrêt (lignes `16` et `18`), cet état ne bloque **pas** le scellement de l'additif, mais bloque mécaniquement le départ de la passe et de la lecture jusqu'à une `v2` conforme ou un mot de Lazar sur la ligne `16`.

---

## Ligne « qui a lu quoi »

- **Agent** : sous-agent vérificateur R2 neuf côté moniteurs `14d827e0cd96a5312eca5d2c6f4f37b2` (`2026-11-24T04:14:30Z`).
- **Lu** : `candidat-rempli.md` (`02687117…`) et son `.sha256` ; sur `main` (`b90f1b48a`) : `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md` (`eb8b36e4…`), `prereg/lecture-sondes-barreau8-v1.md` (`8e432cdc…`, empreinte), `docs/notes/barreau8-cote-moniteurs-entrees-v1/verification-exclus-ad2-sans-secret-v1.md` (`6b15e1dc…`), `docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-ordre-course-lue-additif-1-v1.json` (`8f6b5025…`), `docs/notes/additif-sondes-barreau8-scellement-v1/verification-cote-expose-champs-additif-v1.md` (`b371a110…`), `docs/notes/additif-sondes-barreau8-scellement-v1/contre-lecture-additif-1-brouillon6-opus-v1.md` (`f9379270…`), `docs/notes/additif-sondes-barreau8-scellement-v1/verification-r2-additif-barreau8-fable-brouillon7-v1.md` (`3d53c115…`), `registres/qui-a-lu-quoi-v22.md` (`7b758ff0…`, lignes `246`, `278`–`281`, `379`, `384`, `391`), `registres/sondes-iib-v1.md` (`c8e57b50…`), `registres/go.md` (seules lignes `GO-2026-11-22-75`, `-93`, `GO-2026-11-23-02`, `-16`, `-17`, `-30`, `-32`, `-33`, `-38`), `registres/decisions.md` (seules lignes `R-4726`, `R-4728`, `R-4747`, `R-5035`, `R-5173`, `R-5186`, `R-5215` à `R-5217`), `src/controle_ia/prereg.py` (`3b2e3ee5…`), et calcul d'empreintes des fichiers référencés de `prereg/`, `docs/`, `src/`, `registres/` et `CLAUDE.md`.
- **Non ouvert** : `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/`, `essai/`, `brouillons/ii-b*`, `consigne-privee*`, `conception-ii-b*`. Aucune modification dans `/home/antigravity/lciric/controle-ia-travail`.
