# Contre-lecture de l'option A de la garde des mots de rôle (v1)

- **Contre-lecteur** : Opus 5.5 (claude-opus-5-5), sous-agent neuf, qui n'a pas écrit la correction. Classe B. **Date** : 2026-11-23T23:31Z (`date -u`).
- **Objet** : branche `sondes-v2/code-v2`, commit `c7fb6ca3d`, diff `8351e49b4..c7fb6ca3d -- src tests`. Aucun fichier du dépôt modifié. Arbre propre après lecture.
- **Lu (sha256)** :
  - `docs/notes/sondes-v2-developpeur-v1/diagnostic-garde-mots-de-role/diagnostic-garde-mots-de-role-v1.md` : `cea85ff7fd7b8a2085f88abe7437b39a382d96fa0f1ea858944862f4181bebe7`
  - `docs/notes/sondes-v2-developpeur-v1/diagnostic-garde-mots-de-role/erratum-1-spec-note-des-effectifs-v2-series-publiques.md` : `96f444b58e1cf569b801a673d0e6b4b225a92cf58d26e194f1ddbf1ae1f4e28d`
  - `docs/notes/sondes-v2-concepteur-opus-v1/spec-note-des-effectifs-v2.md` : `0ebc790aacf9dcd3c52ac497d699e22ac5cf4c05c182a388a82871d90c66585b`
  - `src/controle_ia/sondes_v2/formats_v1.py` : `c314e135e60224c186ae77c9d89ed627f6839f7bc7a7e75c762cba35b870c563` (tout le fichier, y compris `charger_table_ouvreur`)
  - `tests/test_sondes_v2_formats.py` : `19977282a194173723641db22ebba52c06e2087e39ccf2f9e079a28d0ac3bddc` (lignes 1 à 135)
  - En appui : `src/controle_ia/sondes_v2/programme_monde_plante_v4.py`, lignes 380 à 420 (seul appel de `charger_note_effectifs`).
  - Compagnons `.sha256` du code, des essais, du diagnostic et de l'erratum : tous « OK ».
- **Non lu** : rien sous `diag/`, `runs/`, `docs/verdicts/`, `coffre/`, `donnees/`, aucun document du barreau 5, aucune autre branche, aucun résultat.

## Verdict : bon après corrections

Le code applique l'erratum fidèlement (question A : oui, sans écart). Les corrections portent sur deux points. D'abord les essais : quatre chemins de garde n'ont pas d'artefact propre (défaut 5). Ensuite, et surtout, l'attestation est une phrase qu'aucun programme ne contrôle, et que son signataire ne peut pas vérifier depuis les noms seuls (défaut 1). Rien ne bloque la relance de la note. Le défaut 1 doit être fermé avant l'ouverture de la table de l'ouvreur.

## Réponses aux questions

**A. Fidélité à l'erratum : conforme.**
- Les deux champs sont exigés : ils sont ajoutés aux champs exacts de `activations` (`formats_v1.py:111-113`). J'ai éprouvé leur absence : « champs manquants ».
- Les comptes sont entiers ≥ 0. Il y a exactement trois clés (`formats_v1.py:118-120`) et `_entier` refuse les booléens. Éprouvé : `-1`, `True`, `1.5`, une liste et une clé neutre en trop arrêtent tous.
- La phrase est exacte. Je l'ai extraite de l'erratum, entre « » : elle est égale octet pour octet à `ATTESTATION_SERIES_PUBLIQUES` (`formats_v1.py:30-31`). La comparaison est stricte (`:121`). Une espace finale ou une apostrophe typographique arrête : le défaut est fermé, il n'y a pas de repli.
- La garde des noms et des clés reste intacte. `MOTS_DE_ROLE` n'a pas changé. `_sans_mot_de_role` tourne encore sur toute la section avant les champs exacts (`:110`). Le contrôle des noms de `series` est inchangé (`:150`). Les trois nouvelles clés ne contiennent aucun mot de rôle (vérifié). La phrase contient « paire » et « jumeaux », mais c'est une valeur, et les valeurs ne sont pas parcourues : pas de faux arrêt.

**B. Aveuglement.**
- Un nom à rôle ne peut plus passer par `series_publiques`. Ses clés sont exactes et ses valeurs entières, donc aucun nom ne peut s'y écrire. Dans `series`, la garde est celle d'avant.
- En revanche, il reste deux trous :
  - Une série opaque peut être retirée de `series` et comptée dans `autres_a_nom_public`. Éprouvé : la note passe. Rien ne le détecte, ni à la lecture de la note ni à l'ouverture (défaut 1).
  - Les textes libres ne sont pas gardés : réserves, `definition`, chaînes de `chemin_de_calcul`, `scores_bbis.colonnes`. Éprouvé : « A3-saboteur » dans une réserve passe. La spécification, § 3, demande même de nommer en réserve une série dont le chemin diffère (défaut 2).
- Le plus simple pour contrôler l'attestation est un contrôle de couverture, sans nom à rôle écrit :
  1. **Avant le verdict, par le programme** : `charger_note_effectifs` reçoit le chemin de la garde. Il vérifie que l'empreinte de la garde est égale à `garde_sha256`. Il vérifie que les noms de `series` font partie des séries de la garde (`_series_de_la_garde`, qui existe déjà). Il vérifie enfin que `len(series) + somme(series_publiques)` est égal au nombre de séries de la garde. Cela attrape l'omission et le double compte.
  2. **À l'ouverture, par le programme** : `charger_table_ouvreur` reçoit la note. Il arrête si une série de rôle `saboteur` ou `jumeau` de la table n'est pas nommée dans `note.series` avec la catégorie `adaptateur`. C'est le contrôle mécanique de la phrase, que le diagnostic confiait au concepteur (question 2) : plus personne n'a besoin de lire les noms. Les deux contrôles se font en quelques lignes et s'éprouvent chacun sur un cas sain et sur un artefact.

**C. R5.**
- Le cas sain est mis à jour (`tests/test_sondes_v2_formats.py:50-51`).
- Les six artefacts de l'erratum existent et arrêtent avec le bon motif (`:95-102`).
- Il manque des artefacts propres pour quatre chemins : la clé neutre en trop dans `series_publiques`, le compte négatif, le booléen et l'attestation absente. Je les ai éprouvés à part : tous arrêtent (défaut 5).

**D. Régressions** : `PYTHONPATH=src python -m pytest -q tests/test_sondes_v2_*.py` donne **207 réussis, 1 sauté**, en 92 s. Le seul appelant, `programme_monde_plante_v4.py:400`, ne lit pas `series` : il n'y a pas d'effet sur les cases.

## Défauts

1. **Moyenne — l'attestation n'est contrôlée par personne, et son signataire ne peut pas la vérifier.** `formats_v1.py:118-123` ; erratum, points 1 et 3.
   - La session habilitée n'ouvre pas la table de l'ouvreur (spécification, § 1). Elle ne peut donc pas savoir qu'une série à nom public n'est pas membre d'une paire. Elle ne peut que le déduire du nom, et le diagnostic le dit lui-même (« Je ne peux pas vérifier cette condition », ligne 12).
   - Le code ne vérifie qu'une égalité de chaînes. Rien n'empêche une série opaque d'être cachée dans `autres_a_nom_public` : éprouvé, la note passe.
   - **Correction** : ajouter les deux contrôles de couverture décrits en B (garde avant le verdict, table de l'ouvreur à l'ouverture), chacun avec un cas sain et un artefact. Au choix de la mère, compléter la phrase par « jugé par les noms de la garde », pour qu'elle dise ce que le signataire peut attester.
2. **Faible — les noms de séries peuvent s'écrire dans les textes libres, et la spécification le demande.** `formats_v1.py:80-89` et `:107-108` ; spécification, § 3, ligne 70 (« Une série dont le chemin diffère est nommée en réserve »), en contradiction avec l'erratum, point 2 (« jamais nommée »).
   - **Correction** : un point de plus dans l'erratum. En réserve, une série publique est désignée par sa catégorie et un rang, jamais par son nom.
   - Dans le code, `_sans_mot_de_role` peut aussi parcourir les valeurs textuelles de `activations`, sauf `attestation_series_publiques`. Pour les réserves, la règle reste écrite : les noms des cases (« adaptateur|saboteur ») y sont légitimes et feraient de faux arrêts.
3. **Faible — « rôle public » n'est pas défini pareil dans l'erratum et dans le code ; le double compte n'est pas exclu.** Erratum, point 2 ; `formats_v1.py:146` et `:150`.
   - L'erratum donne `ancre-<nom>` en exemple de nom à rôle. Le code ne refuse que les mots de `MOTS_DE_ROLE` : `ancre-R1` passe dans `series` (éprouvé). Et il n'existe pas de catégorie « ancre ».
   - Une série propre à nom neutre peut être nommée dans `series` et comptée aussi dans `series_publiques.propre`.
   - **Correction** (erratum) : « porte un rôle public » veut dire « contient un mot de `MOTS_DE_ROLE` » ; une série est soit nommée, soit comptée, jamais les deux. Le contrôle de couverture du défaut 1 attrape le double compte.
4. **Faible — l'identité des clés communes ne se lit plus pour les séries comptées non propres.** Spécification, § 3, première règle ; erratum, point 1.
   - Les ancres et les « autres » sont des séries non propres. Leurs clés devraient être les clés communes, mais la note ne porte plus leur compte de clés.
   - **Correction** : un booléen de plus, par exemple `"non_propres_aux_cles_communes": true` dans `series_publiques` (réserve exigée si faux, comme `nu_relit_les_cles_communes`), ou bien une réserve écrite. À trancher par la mère, car c'est un changement de format.
5. **Faible — quatre chemins de garde sans artefact propre (R5).** `tests/test_sondes_v2_formats.py:95-102`.
   - L'artefact `propre_a1_saboteur=1` est arrêté par la garde des rôles avant les champs exacts : le chemin « en trop » de `series_publiques` n'est pas éprouvé. Il manque aussi un compte négatif, un booléen et l'attestation absente.
   - **Correction** : ajouter quatre lignes au paramétrage :
     - `update(autres=1)` → « en trop » ;
     - `update(propre=-1)` → « entier » ;
     - `update(ancre=True)` → « entier » ;
     - `pop("attestation_series_publiques")` → « manquants ».
   - Les quatre arrêtent déjà (éprouvé dans le bloc-notes).

**Remarques hors du diff, non comptées** :
- La garde des noms est une liste noire par sous-chaîne : des abréviations comme `X-07-sab` passent (éprouvé). C'est connu et sans régression.
- La docstring de `_sans_mot_de_role` (`:81`) dit contrôler les noms de séries, alors que c'est la ligne 150 qui le fait.

Sondes ad hoc : `/tmp/claude-0/-home-user-controle-ia-travail/f6a0de81-4b86-5f89-b882-c755727ab92d/scratchpad/sonde_option_a.py`.

**Verdict : bon après corrections — 0 bloquant, 1 moyen, 4 faibles.**
