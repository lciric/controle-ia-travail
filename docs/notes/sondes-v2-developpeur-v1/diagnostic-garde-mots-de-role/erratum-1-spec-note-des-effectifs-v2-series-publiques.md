# Erratum 1 à la spécification v2 de la note des effectifs : séries à nom public (option A)

- **Porte sur** `docs/notes/sondes-v2-concepteur-opus-v1/spec-note-des-effectifs-v2.md` (`0ebc790a…`), qui reste en vigueur ailleurs ; en cas d'écart, cet erratum prime. Classe B.
- **Décision** : option A du diagnostic (`diagnostic-garde-mots-de-role-v1.md`, `cea85ff7…`), retenue par la mère le 2026-11-23 vers 23:50Z (routine sur un instrument, confiance 0,7), après l'arrêt du lecteur habilité sur la garde des mots de rôle (R-5200).
- **Écrit par** le développeur des sondes v2, session_016QhUrtqKazbonFiVhXMm3R, le 2026-11-23T23:27Z. **Aucun résultat.**

1. **§ 2, bloc JSON, section `activations`** : deux champs sont ajoutés.
   - `"series_publiques": {"propre": n, "ancre": n, "autres_a_nom_public": n}` : comptes entiers ≥ 0.
   - `"attestation_series_publiques"` : cette phrase, mot pour mot : « aucune série comptée dans series_publiques n'est membre d'une paire opaque du test sur les adaptateurs jumeaux ; leurs noms ne sont pas écrits ».
2. **§ 2, `series`** : n'y figurent que `nu`, les adaptateurs aux noms opaques de la garde et les séries dont le nom ne porte aucun mot de rôle. Toute série dont le nom porte un rôle public (par exemple `propre-A<k>-saboteur` ou `ancre-<nom>` du format du barreau 5) n'est **jamais nommée**. Elle est comptée dans `series_publiques`, sous « propre », « ancre » ou « autres_a_nom_public ».
3. **§ 1, arrêt** : la session habilitée s'arrête encore, et le dit à la mère sans l'écrire, si un nom de série opaque, un nom de colonne ou une clé laisse lire un rôle, **ou si elle ne peut pas attester la phrase du point 1**.
4. **§ 4, chargeur** : `charger_note_effectifs` exige les deux champs, leurs comptes entiers et la phrase exacte. La garde des noms et des clés reste entière (`formats_v1.py`, `MOTS_DE_ROLE`). Essais : cas sain et six artefacts (`tests/test_sondes_v2_formats.py`).
