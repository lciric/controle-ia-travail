# Vérification des corrections (202f6379), même contre-lecteur

Lu : diff 04b4edfa..202f6379 (src/controle_ia/t08, tests/test_t08_*), noms des mutations A18-A24 dans mutations-alignement-t08-v2.py. Aucun écart src/tests entre 202f6379 et HEAD. Non ouvert : interdits habituels. Banc v2 : sortie non encore disponible, non vérifiée par moi.
Rejoué : alignement + tokeniseur (T08_EXIGER_TOKENISEUR=1) + mots_et_cout : 32 passés ; test_lecture_reelle_charge_la_piece : 1 passé ; passage à blanc (gardes_corrections) : 2 passés.

- CA-01 vérifié : `charger_piece` restaure `sys.modules` (ancien capturé avant le chargement) si `Piece(...)` refuse ; `test_chargement_contrat_incomplet` passe par `_exiger_arret` (contrôle `sys.modules`). Le test du jouet (`test_t08_mots_et_cout_v1`) ne contrôle toujours pas `sys.modules` : couvert par A18 seulement via le contrat incomplet, suffisant.
- CA-02 vérifié : comparaison des cinq clés inscription/marqueur ; artefact réel (pièce contrôlée sur le marqueur du brouillon 11, configuration factice) refusé.
- CA-03 vérifié : l'espion enregistre les lectures et les appels, exige l'ensemble lu inclus dans CONTRAT plus PIECE_JOUET, l'ordre exact des six appels, les actions/y/centres passés tels quels (identité d'objet). Probant. L'assertion tautologique restée dans l'ancien essai est sans effet : la retirer (remarque, facultatif).
- CA-04 vérifié : test_copie_saine ajouté à A12 (sans fixture), à confirmer dans la sortie du banc.
- CA-05 vérifié : non-Exception relevées telles quelles après restauration ; test SystemExit contrôle `sys.modules`.
- CA-06 vérifié : balayage de `string.printable` sur le tokeniseur réel, constat figé `A_CHEVAL_ASCII`, détection jamais manquée.
- CA-07 vérifié : `piece_points_joues` dans le compte rendu.

**CA-09 — remarque (rapport, à écrire)** : le balayage montre que le constat est plus large que ce que dit le rapport § 3 : 41 lettres sur 52 (par exemple `>Answer`) fusionnent aussi avec `>`, pas seulement saut de ligne et ponctuation. Le rapport final doit le dire (et que la fréquence dans les générations des juges est inconnue) ; la règle de l'état « à cheval » reste un nœud pour la mère.

Reste : sortie du banc v2 (A18-A24 tuées, A12 avec test_copie_saine) à lire dans le rapport final ; marqueurs <<…>> à remplir.

## Verdict : corrections **vérifiées**, sous réserve de la sortie du banc v2 et de CA-09 dans le rapport.
