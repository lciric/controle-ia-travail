# Outil des remplacements exacts — chaîne de contre-lecture (classe B)

- Note de classe C, écrite par la session fille de l'attaquant informé le 22 novembre 2026 vers 13:00 UTC. Les rapports eux-mêmes ont été rendus dans la session et ne sont pas versés comme fichiers ; cette note en garde la teneur.
- v1, `src/controle_ia/remplacements_exacts_v1.py` : deux contre-lectures neuves.
  - Sonnet : « conforme après corrections », 1 bloquant et 1 majeur. Le bloquant : les occurrences qui se chevauchent n'étaient pas vues. Le majeur : les fins de ligne étaient normalisées.
  - Opus : « à reprendre », 1 bloquant, 2 majeurs et 5 mineurs. Il trouve les mêmes défauts, plus des cas Unicode (formes NFC et NFD, caractère combinant).
- v2, `remplacements_exacts_v2.py` : vérification par le même Opus, « conforme après corrections ». Deux majeurs : un nouveau texte pouvait commencer par un caractère combinant, et la remise des marques dépendait de l'ordre de la table. Deux mineurs : les erreurs système à l'écriture, et une marque déjà présente dans la source.
- v3, `remplacements_exacts_v3.py` : vérification courte par le même Opus, « **conforme** », points A à D levés, aucun défaut nouveau, 37 tests. Remarque sans effet : passer `--marques` deux fois mène à un refus (code 2).
- Version d'usage : **v3**. La v1 et la v2 restent inchangées (R12).
