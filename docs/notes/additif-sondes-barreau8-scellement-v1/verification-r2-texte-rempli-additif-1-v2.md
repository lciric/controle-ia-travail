# Vérification R2 finale du texte rempli candidat au scellement — Additif 1 aux sondes du barreau 8 (v2)

- **Vérificateur** : sous-agent R2 neuf du côté des moniteurs (`14d827e0cd96a5312eca5d2c6f4f37b2`), strictement aveugle.
- **Date et heure (UTC)** : `2026-11-24T04:19:15Z` (`date -u`).
- **Rapport précédent (`v1`)** : `verification-r2-texte-rempli-additif-1-v1.md` (`f28c5ee010178ee352a23bfee4c1e8e8897b7f840ec297b4f067bffdec9a724b`), qui relevait une liste fermée de deux empreintes SHA-256 erronées (`E-1`, `E-2`) en ligne `619` sur le candidat précédent (`02687117…`).
- **Dépôt contrôlé (lecture seule)** : `/home/antigravity/lciric/controle-ia-travail`, branche `main` (`git status --porcelain` vide, `PYTHONDONTWRITEBYTECODE=1`).
- **Candidat corrigé contrôlé** : `/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/scellement-additif-b8-final/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-candidat-rempli.md` (`623` lignes, `195 155` octets, SHA-256 `fc5b0610ed004ea4b1565e7a50567d7538b0f9e66b129c874c2f8c5bc2a4d8c2`, compagnon `.sha256` égal).

---

## Verdict

**`CONFORME POUR SCELLEMENT IMMÉDIAT`**

Les deux erreurs `E-1` et `E-2` de la ligne `619` relevées en `v1` sont **2/2 corrigées à l'octet**, sans aucune autre modification. Les 5 contrôles mécaniques exigés passent à **100 %** (`0` erreur, `0` réserve bloquante au scellement).

---

## Résultats des 5 contrôles exécutés par programme

### 1. Différentiel ligne à ligne contre `brouillon7.md` (`eb8b36e4…`) — **CONFORME**
- `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md` (`eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b`) : `623` lignes ; candidat corrigé (`fc5b0610…`) : `623` lignes.
- Lignes modifiées : **exactement `[172, 173, 174, 175, 176, 177, 536, 619]`** (`0` autre ligne touchée).
- Sur `172` à `177` (`AD-1` à `AD-6`), seule la 3e colonne (`état`) a changé ; les colonnes `id` et `champ` sont identiques à l'octet au brouillon 7. Conforme à la règle du scellement (ligne `136`) et à la liste d'arrêt (ligne `18`).

### 2. Validateur `controle_ia.prereg` et absence de marqueurs / émojis — **CONFORME**
- `controle_ia.prereg.problemes(candidat-rempli.md)` == `[]`.
- `controle_ia.scellement.verifier(candidat-rempli.md)` == `fc5b0610ed004ea4b1565e7a50567d7538b0f9e66b129c874c2f8c5bc2a4d8c2`.
- Occurrences de `À REMPLIR` : `0` ; de `<<` : `0` ; de `>>` : `0` ; émojis : `0`.

### 3. Empreintes SHA-256 à 64 hex dans `AD-2`, `AD-3`, `AD-4`, `536` et `619` contre `main` — **CONFORME (9/9 exactes + 4/4 préfixes courts en `L536`)**

| Lieu | Pièce citée sur `main` | SHA-256 vérifié (fichier, `.sha256` et candidat) | Statut |
|---|---|---|---|
| `AD-2` (`L173`) | `docs/notes/barreau8-cote-moniteurs-entrees-v1/verification-exclus-ad2-sans-secret-v1.md` | `6b15e1dcb3ec4dd95d64bd2550c806d1b7de257ed4c5432a6eff76bc75e488d7` | **OK** |
| `AD-3` (`L174`) | `registres/qui-a-lu-quoi-v22.md` | `7b758ff0fe0c38a8f663946f40304213a151258371fcbeffb684b34d6d8aeed4` | **OK** |
| `AD-3` (`L174`) | `docs/notes/additif-sondes-barreau8-scellement-v1/verification-cote-expose-champs-additif-v1.md` | `b371a110680b612acc2170980588c721ea5ad0972171306c220f164fea16b841` | **OK** |
| `AD-4` (`L175`) | `docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-ordre-course-lue-additif-1-v1.json` | `8f6b502581cb32d546e84cf13d52d07f1faa011484ef585bde3635f56e86e76a` | **OK** |
| `L536` | *(4 préfixes courts : `f9379270…`, `3b46c67a…`, `7b758ff0…`, `b371a110…`)* | 4/4 conformes | **OK** |
| `L619` | `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon6.md` | `bf10784207e6d74944d7d4804817c03eb8515d38e130ce282a577b4c96970b5e` | **OK** |
| `L619` | `docs/notes/additif-sondes-barreau8-scellement-v1/contre-lecture-additif-1-brouillon6-opus-v1.md` | `f9379270cddf80f25eb35f3079e03f0b423a6932e53075f0f592de53de857714` | **OK (`E-1` résolue, = `L28`)** |
| `L619` | `docs/notes/additif-sondes-barreau8-scellement-v1/corrections-brouillon6-vers-brouillon7-v1.py` | `3b46c67a7fa6b839e66a3d2f8b96faa580de09cc42e9dde6091ea4a7e8bca2b3` | **OK (`E-2` résolue)** |
| `L619` | `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md` | `eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b` | **OK** |
| `L619` | `docs/notes/additif-sondes-barreau8-scellement-v1/verification-r2-additif-barreau8-fable-brouillon7-v1.md` | `3d53c115226934535022bb5dee4f47f7bb0bc1493cd1c1e6aeca85d5f86c628d` | **OK** |

### 4. Forme normative de `AD-3` (`L568`), concordance `AD-1`/`AD-6` et étanchéité de l'ordre neuf (`L179`) — **CONFORME**
- `AD-3` (`L174`) respecte strictement dans l'ordre exact les 8 segments de premier niveau du patron normatif de la ligne `568` (sans heure de scellement, portée par `SCELLEMENT-ADDITIF-1-SONDES-IIB`), en concordance avec `R-4726`, `R-4728`, `R-4747`, `R-5035`, `R-5173`, `R-5186` et `R-5217`.
- `AD-1` (`L172`) cite exactement `GO-2026-11-23-32` (et `-16`, `-17` point 4, `-30`, `-33`, `-38`).
- `AD-6` (`L177`) == `GO-2026-11-22-75` == `D-6.ligne_de_calcul`.
- Étanchéité (`L179`) : `0` occurrence dans tout l'additif des chemins, empreintes à 64 hex ou préfixes à 8 hex des trois pièces de l'ordre neuf.

### 5. Schéma JSON fermé à 9 clés de `attestation-ordre-course-lue-additif-1-v1.json` (`8f6b5025…`) — **CONFORME**
- Schéma strict à 9 clés sans doublon conforme à `D-6` (`L298`), y compris les `lieu` au format `<rang>:<numéro>` (`0:4.5`, `0:4.1`, `1:8`, `1:7`) et `exclus.section == "1:8"`.
- `verdict_mecanique == "écart"` (dû à `O-3`, `O-5`, `O-6 == "non dit"`) est conforme à la règle `L298`, couvert au scellement par « Deux temps, deux versions (règle R12) » (`L300`), et ne bloque que le départ de la passe et de la lecture jusqu'à `v2` conforme ou mot de Lazar sur la ligne `16`.

---

## Ligne « qui a lu quoi »

- **Agent** : sous-agent vérificateur R2 neuf côté moniteurs `14d827e0cd96a5312eca5d2c6f4f37b2` (`2026-11-24T04:19:15Z`).
- **Lu en `v2`** : candidat corrigé `lecture-sondes-barreau8-v1-addendum-organisme-change-v1-candidat-rempli.md` (`fc5b0610…`) et son `.sha256` ; rejeu des 5 contrôles contre les seules mêmes pièces autorisées qu'en `v1`.
- **Non ouvert** : `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/`, `essai/`, `brouillons/ii-b*`, `consigne-privee*`, `conception-ii-b*`. Aucune modification dans `/home/antigravity/lciric/controle-ia-travail`.
