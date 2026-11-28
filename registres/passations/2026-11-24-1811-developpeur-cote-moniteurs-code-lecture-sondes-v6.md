# Passation — développeur du côté des moniteurs, code de la lecture des sondes v6 du barreau 8 — 2026-11-24 18:11Z

Session fille de la mère `session_01Qi7Gr3Ggccg85kjmP654WC`, modèle Opus 5.5, branche `barreau8/code-lecture-sondes-v6-v1`. Mandat : message de la mère du 2026-11-24 vers 13:10Z (classe B). Passation écrite ici et non sous `registres/passations/`, le mandat interdisant de pousser sous `registres/` (hors la ligne à verser) ; la session mère la recopie si elle le veut.

## Fait

1. **Code de la lecture v6** : `src/controle_ia/barreau8_moniteurs/lecture_sondes_v6.py` (`8b39af4b…`) et module à part des lectures descriptives de l'additif 1 `src/controle_ia/barreau8_moniteurs/lectures_descriptives_additif_1_v1.py` (`1135731c…`). Texte scellé lu avec les additifs 1 et 2 : constantes de forme lues dans la seule table neuve ; registre propre à huit clés ; bordereau à neuf clés ; conditions D-6 (lue avec M-3), D-14, D-15, D-17 ; règles RP-1 à RP-14 ; lectures LD-1 à LD-5 à l'étape (g bis), hors verdict ; lignes de tête RP-14 ; commande de réception seule (gardes r1 à r8, condition D-11) ; seconde lecture refusée. La lecture v5 n'est pas touchée.
2. **Essais** : `tests/test_barreau8_moniteurs_lecture_v6.py` (`f0f9617b…`), données factices seulement, **151 essais, tous passent**. Chaque garde et chaque refus sur cas sain et sur artefact ; lecture de bout en bout à réponse connue ; seconde lecture refusée ; pièces réelles sans contenu de la course (table neuve, pièces D-14, attestation de l'ordre) acceptées.
3. **Notice v7** : `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-lecture-sondes-v7.md` (`2b03ebeb…`) ; durée mesurée sur données factices aux tailles réelles : 104 s de calcul pour la lecture décisive, 123 s avec les lectures descriptives, pic d'environ 800 Mo.
4. **Contre-lecture de conformité** (Sonnet 5.5, effort élevé, sous-agent neuf) : `contre-lecture-conformite-lecture-v6-sonnet-v1.md` (`aeb4d8b8…`), « conforme », sept mineurs ; corrections (`corrections-contre-lecture-lecture-v6-v1.md`, `5e610b15…`) ; vérification par le même contre-lecteur `verification-corrections-lecture-v6-sonnet-v1.md` (`429b5917…`), « conforme » ; erratum 1 (essai du refus des rapports v5, `ee8f1504…`). Tous dans `docs/notes/code-lecture-sondes-v6-v1/`.
5. **Bordereau du code** `docs/notes/code-lecture-sondes-v6-v1/bordereau-code-lecture-sondes-barreau8-v6.json` (`dd816daf…2d4e`), accord réservé `GO-2026-11-24-28` ; ligne proposée `registres/lignes-a-verser/code-lecture-sondes-v6-v1.md` (`0a1aad67…`). **La session mère a fusionné la branche sur `main` et inscrit la ligne `CODE-LECTURE-SONDES-IIB` (R-5313)**, et l'accord sous condition (mot du 2026-11-24 vers 15:45Z).
6. **Pièces de départ manquantes** : `pieces-de-depart-manquantes-v2.md` (`f8d1e966…`) ; « qui a lu quoi » v1 et v2 (`48a3a387…`).
7. Compte rendu à la mère envoyé le 2026-11-24 vers 15:40Z.

## Suite complète des essais du dépôt

Jouée en quatre tranches parallèles (fichiers répartis à tour de rôle ; le fichier de la lecture v6, joué à part, en est retiré), sur la tête `99820382` : **15 930 réussis, 212 échecs, 115 sautés, 213 échecs attendus (greffon des échecs connus)**. Une passe d'un seul tenant, arrêtée au premier échec, avait donné 1 533 réussis puis un échec ; la passe d'un seul tenant sans arrêt a été coupée par sa limite de 7 000 secondes.

Aucun des 212 échecs ne touche un module de ce travail :
- 207 dans `test_neuron_lens_comparer_reajustement_v4.py` (183) et `_v3.py` (24) : pièces lues à des commits que ce clone partiel ne porte pas (v4 : « commit de la branche de résultats … lisible dans le dépôt » non tenu ; v3 : correctifs « non lu », d'où « non comparable ») ; le fichier v3 rejoué seul échoue pareil (24 sur 123) ;
- 1 dans `test_t07_lecture_v1.py` : commit `8cb539f9` absent du clone partiel ;
- 1 dans `test_t08_alignement_piece_v1.py` : un module déjà importé par un autre fichier de la même tranche (effet d'ordre entre fichiers) ;
- 3 dans `test_cibles_invisibles_v4.py` et `_v5.py` : l'inventaire des lecteurs de la référence cachée nomme `passe_recalcul_v6.py` (`_table_en_specification`) et deux modules t08, déjà présents sur `main` avant ce travail ;
- l'échec de la passe arrêtée au premier échec (`test_barreau8_moniteurs_lecture_v5.py::test_refus_de_tourner[registre des accords absent]`) n'est pas revenu : il passe seul et dans sa tranche.

## Reste

Rien dans ce mandat. La réunion des pièces de départ est confiée à la conductrice du côté des moniteurs (branche `barreau8/conductrice-lecture-sondes-v1`), d'après la session mère.

## Réserves

- Vérification de l'arbre des sceaux au début de la session : douze échecs déjà présents sur `main` (dont `journal-etage3.txt` à empreinte différente, trois passations aux compagnons mal nommés), signalés à la mère, non corrigés (hors mandat).
- Inventaire « cibles » : trois modules de `main` (passe v6, deux modules t08) hors de sa liste ; à porter par la session mère à qui tient cet inventaire.
- L'heure de remise de la note d'interface version 7 n'a pas de source scellée ; la session mère l'atteste (pièces manquantes, v2, point 7).

## Prochaine action

Aucune pour cette session : arrêt, sur le mot de la mère. Pour la suite de la lecture : pièces 1 à 8 de `pieces-de-depart-manquantes-v2.md`.

## Instances actives

Aucune : aucune machine louée, aucune dépense. Inventaire des instances de calcul payantes non fait par cette session fille (aucun accès ni mandat de calcul).

## Cloisonnement

Rien lu de la course ; aucune branche de course ou de lecture rapatriée (un seul `git fetch`, de la branche `main`, pour constater la fusion) ; rien ouvert sous `versement/`, `donnees/`, `diag/`, `runs/` ; le contre-lecteur a reçu les mêmes interdits.
