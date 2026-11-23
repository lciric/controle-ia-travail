# Vérification du côté exposé — champs de l'additif aux sondes du barreau 8 — v1

- **Qui** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf du côté exposé, sous-agent lancé depuis la session session_016QhUrs5yLghTY6Gthp4k3P (celle de la lettre (e)).
- **Heure** : 2026-11-23T23:31:45Z (`date -u`) ; lecture commencée à 2026-11-23T23:26:29Z.
- **Branche principale lue** : `git fetch origin main`, `FETCH_HEAD` = `fd4e259c16bfc640f15c366db7dbe077085b9c3b` ; lecture par `git show FETCH_HEAD:<chemin>`, sans changer de branche.
- **Fichiers ouverts (en entier ou par recherche), empreinte sha256 à ce commit** :
  - `registres/decisions.md` — `cad3b4888245391e2ed5fb475a01f447c89a55bcb4c0b8677149c192fa217719`
  - `registres/go.md` — `389a8076710415449f5688cc205eedda2fbf69271c919ea9874e9c95fb8ea374`
  - `registres/qui-a-lu-quoi-v22.md` — `7b758ff0fe0c38a8f663946f40304213a151258371fcbeffb684b34d6d8aeed4`
  - `registres/sondes-iib-v1.md` — `c8e57b5026ebfb97e72589f322924795beb5a5e5a9fc5889b31b20171622a568`
  - `registres/iib-reconception/mandat-reconception-oracle-iib-v1.md` — `c1cd485a86bc651c1fcad154480a87ae6cd4a488bda5feec7acd31b4bd36219e` (titres seulement)
  - `brouillons/ii-b-saboteur-budget-v5/additif-course-v1/additif-ordre-course-voie-A-v1.md` — `8e1d340a2e676b722489e6ae68b6ed9cd7d96bcf95d42e3490557ab3db7fb6c9` (titres et recherche de mots)
  - `brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1.md` — `43a7a050d769792f3c5d7859509b69f34e082f953840909a1f59a1535bf01b3e` (titres seulement)
  - `registres/passations/2026-11-22-2310-executante-saboteur-voie-A.md` — `5d46d917c8459cf1c89d54d8b4d63554f61c724a7be034f46186d935fd7bc9d4` (une ligne, par recherche)
  - noms de fichiers seulement : `docs/notes/barreau8-cote-moniteurs-entrees-v1/`
- Aucune sortie de course, aucune branche essai/ ni calcul/, rien sous `docs/verdicts/`, `runs/`, `diag/` n'a été ouvert.

## Q1 — Exclus

**Non trouvée.** Aucune liste « Qui lit, qui juge » en § 8 de l'ordre neuf de la course voie A sur la branche principale. Cherché dans : `brouillons/ii-b-saboteur-budget-v5/` (tous sous-dossiers), `brouillons/ii-b-saboteur-budget-v1/`, `registres/iib-reconception/`, `registres/iib-executante/`, `docs/notes/saboteur-budget-ordre-etalonnage-v5/`, et recherche de « Qui lit, qui juge » sur toute la branche principale (hors `docs/verdicts/`, `runs/`, `diag/`).

## Q2 — Qui a lu quoi

- Empreinte de `registres/qui-a-lu-quoi-v22.md` : `7b758ff0fe0c38a8f663946f40304213a151258371fcbeffb684b34d6d8aeed4` ; compagnon `.sha256` : identique (conforme).
- Un agent de la liste L inscrit comme lecteur d'une sortie de la course voie A, de son étalonnage, ou d'un état des lectures du dommage et de la diffusion : **non**.
- Inscriptions par lettre :
  - (a) non inscrit.
  - (b) non inscrit.
  - (c) non inscrit.
  - (d) non inscrits (correcteurs et relecteur).
  - (e) inscrit : ligne 384 du tableau (ligne 469 du fichier).
  - (f) session_016QhUrvi45g3jX5saFefVED inscrite : ligne 379 du tableau (ligne 464 du fichier) ; session_01Qi7Gr3eYmAhDEJzqLgWcv1 non inscrite en propre (deux de ses sous-agents, autres que (a), aux lignes 313 et 314 du tableau, lignes 398 et 399 du fichier).
  - (g) inscrits : conductrice côté moniteurs session_013QMayjujdhnn94JyDTmgSs, lignes 246 et 278 du tableau ; rédacteur de son texte, lignes 258 et 279 ; contre-lecteurs du texte, ligne 280 ; développeurs des codes de la passe de recalcul et de la lecture des sondes, et contre-lecteurs de ces codes, ligne 281 (ligne 366 du fichier).
- Réserve : l'absence d'inscription de (a), (b), (c), (d) et de la session_01Qi7Gr3eYmAhDEJzqLgWcv1 en propre n'est pas une preuve d'absence de lecture.

## Q3 — Lectures du dommage et de la diffusion de la course voie A jouées

**Aucune trace** dans `registres/decisions.md` de R-5150 à R-5208 ni dans les lignes GO-2026-11-23-* de `registres/go.md`. Lignes du saboteur voie A vues dans la plage : R-5155, R-5165, R-5166, R-5167, R-5171, R-5173, R-5181, R-5182, R-5185, R-5186, R-5200 ; GO-2026-11-23-01, -02, -06, -15, -16, -30.

## Q4 — Extrait des seuls états pour le côté des moniteurs

**Non.** `registres/sondes-iib-v1.md` ne porte aucune ligne de clé `ETATS-COURSE-IIB` (une seule clé, `SCELLEMENT-SONDES-IIB`) ; ce registre n'a pas de compagnon `.sha256` sur la branche principale (vérifié par `git ls-tree`). `docs/notes/barreau8-cote-moniteurs-entrees-v1/` ne contient que trois notes d'interface (v3, v5, v6) et leurs compagnons.

## Q5 — Passe de recalcul de l'activité interne partie

**Non.** Aucune clé `CODE-PASSE-IIB` ni `LIVRAISON-PASSE-IIB` dans `registres/sondes-iib-v1.md`. Dans `registres/decisions.md`, lignes à l'appui : R-5173 et GO-2026-11-23-32 ; aucune ligne de création ou de départ d'une passe de recalcul après R-5173.

contenu transmis : aucun
