# Erratum 2 à la spécification v2 de la note des effectifs : couverture des séries publiques

- **Porte sur** la spécification v2 (`0ebc790a…`) et son erratum 1 (`erratum-1-spec-note-des-effectifs-v2-series-publiques.md`), qui restent en vigueur ailleurs ; en cas d'écart, cet erratum prime. Classe B.
- **Déclenché par** la contre-lecture de l'option A par un Opus neuf (« bon après corrections » : 1 moyen, 4 faibles ; `contre-lecture-option-a-v1.md`, versé dans ce dossier).
- **Écrit par** le développeur des sondes v2, session_016QhUrtqKazbonFiVhXMm3R, le 2026-11-23T23:34Z. **Aucun résultat.**

1. **Rôle public** : une série « porte un rôle public » si son nom contient un mot de `MOTS_DE_ROLE` (« saboteur », « jumeau », « paire », « famille »). Une telle série est comptée dans `series_publiques`. Une série est nommée ou comptée, jamais les deux. Une ancre dont le nom ne contient aucun de ces mots est nommée dans `series`, avec la catégorie « adaptateur ».
2. **Textes libres** : aucune valeur textuelle de la section `activations` ne porte un mot de rôle, hormis la phrase d'attestation. En réserve, une série publique se désigne par sa catégorie et un rang (« propre n° 2 »), jamais par son nom.
3. **Contrôle de l'attestation, avant l'inscription de la note** : `verifier_couverture_note(note, garde)`, appelé par la mère sur la garde des activations. Il vérifie :
   - que l'empreinte de la garde est égale à `garde_sha256` ;
   - que chaque série nommée figure dans la garde ;
   - que les séries nommées et les séries comptées font ensemble le nombre de séries de la garde.
4. **Contrôle à l'ouverture** : `charger_table_ouvreur` exige la note des effectifs. Il arrête si la note porte une autre garde, ou si un membre d'une paire n'y est pas nommé comme adaptateur.
5. **Non tranché, pour la mère** : un booléen `non_propres_aux_cles_communes` (les ancres et les « autres » portent-ils les clés communes ?) changerait le format de la note. Il n'est pas ajouté sans ton mot.
