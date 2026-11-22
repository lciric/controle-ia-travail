# Vérification des corrections de la chaîne de lancement de T0.8 — v1

- **Nature** : vérification courte des corrections (classe B, même contre-lecteur que la contre-lecture `contre-lecture-chaine-de-lancement-t08-v1.md`, `e52658a26c3a59837a8bafd5fcad7a00988f2d574fd036a063dc6445051ae9f6`) ; une seule passe.
- **Contre-lecteur** : session `session_013QMaymC2hofayrH8ySBw7N` (Opus 5.5), le 2026-11-22 vers 21:35 à 21:50 UTC.
- **Pièce** : branche `t08/chaine-de-lancement-v1`, commit `c061e40b2` ; rapport v3 `docs/notes/t08-chaine-de-lancement-v1/rapport-chaine-de-lancement-t08-v3.md` (`a65b8bc3a9911e23cc208f9daaf207562e57ec3ed777b0c41382b1692bdfb125`, vérifiée), section 0. Ordre de course au brouillon 9 (`91f9e3d622c6d1fb29a3977cfd44dabb4f53357c198e103e041533daa5f37b8c`, branche `prep/t08-texte-complet-fable-v1`), lignes de P7, de l'étape 11 et du commit `S`.
- Aucune machine, aucun appel au loueur, aucune dépense ; aucun résultat de course ni verdict lu.

## Avis

**Corrections conformes ; chaîne scellable au commit `c061e40b2`, sous la seule condition M-7 (le commit cité par `CODE-T08` est ce commit ou un descendant qui ne change pas les fichiers ci-dessous).** Aucun constat neuf bloquant ni majeur ; une remarque mineure sur P7.

## Constats

| constat | vérifié |
|---|---|
| B-1 | l'amorce appelle `exiger_instance_sans_interdits(".", run_7b)` ; `run_7b` est tiré du chemin du manifeste de 7b et exigé égal à `RUN_7B` en mode réel (`amorce…:474-480`) ; le code aligné est fusionné (`9efa1c28`) ; `ATTENDUS="252"` ; essais de l'amorce rejoués (artefact sous le run de 7b, cas sain avec `resume.json` étrangers) : passés |
| M-2 | étiquette lue dans `vue-offre.json` (`lancer…:242`) ; essai `test_offre_refusee_a_la_creation_code_5_et_machine_exclue` : code 5 ; passé |
| M-3 | minuterie : à l'épuisement du plafond restant, consignation puis destruction (plus de « stopped ») ; fin normale et second démarrage : destruction après le versement prouvé (`ls-remote` = tête locale), sinon arrêt, disque gardé ; surveillance « FIN » : destruction par l'amorce, `destroy` en recours. Conforme au texte |
| M-4 | écrit au rapport (§ 8) et à l'ordre, brouillon 9 (ligne 109 : texte, configuration et compagnons dans le même commit `S`) |
| M-5 | échéance de la machine = heure du plafond restant ; une échéance donnée ne peut que l'avancer (`lancer…:220-221`) ; la fin de validité de l'accord ne borne plus que le jour de création |
| M-6 | rapport et en-têtes rattachés à la consigne v3 et au brouillon 15 |
| M-7 | à la mère (inchangé) |
| m-1 | `construire` exige `--commit-code` = `COMMIT_CODE_T08` (`construire…:299-301`) |
| m-3 | frontière après l'identifiant d'origine (`session_v1.py:116`) ; essai d'un identifiant plus long : refusé |
| m-4 | `lire_v1` : toute exception sort en « ARRÊT : <type> : <motif> » |
| m-2, m-5, m-6 | pris |

**r-9 (empreinte de `course-t08.json`)** : tenu. `ecrire_configuration_lecture_t08_v1.py:69-79` lit la ligne `COURSE-T08`, exige le chemin `diag/<run>/course-t08.json`, vérifie le fichier contre son compagnon (`verifier`) et exige que cette empreinte égale celle de la ligne ; les six fichiers de la course n'entrent dans la configuration de la lecture qu'aux empreintes de `resultat.fichiers` de cette enveloppe, sous `donnees/<run de la course>/`. Un fichier recomposé de morceaux n'est donc admis qu'à l'égalité de ces empreintes.

**n-2 (deux commandes de P7)** : confirmées, avec une remarque.
- `sha256sum scripts/amorce_instance_t08_v1.sh scripts/lancer_t08_v1.sh scripts/construire_branche_entree_t08_v1.py scripts/tests-cibles-t08-v1.txt` : valeurs attendues au commit `c061e40b2` (compagnons vérifiés) :
  - `7572f9128e87a27fd2dd9e205a8590b77455ebe509853d458f06767f497b9611` `scripts/amorce_instance_t08_v1.sh`
  - `acfe5a757a626f6f254527d7f0009e2af43b5b95833c7fd1cbe68f2f9bf7b03c` `scripts/lancer_t08_v1.sh`
  - `051c73d23ec85668d263165e089643c9792970d1d6f05d30e3de7fdb133a76cc` `scripts/construire_branche_entree_t08_v1.py`
  - `5b6db29b7434c3bd38c6178d04b790572e96f767c1ba36410694fcb2a0000c2c` `scripts/tests-cibles-t08-v1.txt` (égale à `LISTE_SHA256` de l'amorce)
- `PYTHONPATH=src python3 -m pytest -q "tests/test_t08_entrees_rendu_v1.py::test_amorce_instance_clone_de_l_arbre_aligne"` : joué au commit `c061e40b2`, **1 passé** ; c'est bien l'essai que l'amorce écarte (`--deselect`, `amorce…:513`).
- **Remarque mineure (n-2a)** : le lanceur exécute aussi `src/controle_ia/lancement_t08/session_v1.py` depuis le dépôt local, et la mère joue `ecrire_configuration_course_t08_v1.py` ; P7 gagnerait à les ajouter à la commande d'empreintes et à exiger que la session lance depuis un clone au commit `C` : `bce5f4c9ae82eeb10d90b9cfd4c86ce6b061ac1deb0182723d67d30830dbdb0e` `src/controle_ia/lancement_t08/session_v1.py` ; `6b2a219f78e07c4527adea175729ece15178a60a5896032d7c912c8e11885749` `scripts/ecrire_configuration_course_t08_v1.py` ; `e721a9d64042ade1cfc17b3deeade937e1f29558adc807699e69aba75d731bb9` `scripts/ecrire_configuration_lecture_t08_v1.py`.

**Étape 11 de l'ordre** : confirmée ; la machine se détruit elle-même en fin normale (versement prouvé) et à l'épuisement du plafond restant ; `vastai destroy instance $ID` ne sert qu'en recours.

## Essais rejoués (au commit `c061e40b2`, dans un arbre de travail à part)

- Liste figée (`scripts/tests-cibles-t08-v1.txt`, 13 fichiers) plus `tests/test_t08_chaine_amorce_v1.py`, l'essai écarté désélectionné : **264 passés, 1 désélectionné**, 258 s.
- Essai écarté de P7 : **1 passé**, 51 s.
- Essai de bout en bout : non rejoué (une seule passe courte, économie) ; le rapport v3 le déclare rejoué.

## Lu

Le rapport v3 (en-tête et section 0) ; aux lignes citées, `amorce_instance_t08_v1.sh`, `lancer_t08_v1.sh`, `session_v1.py`, `construire_branche_entree_t08_v1.py`, `lire_v1.py`, `ecrire_configuration_lecture_t08_v1.py`, la liste figée ; de l'ordre de course (brouillon 9), les lignes de statut, de P7, 103, 109, 116, 123 et 125 ; les noms des essais de `test_t08_chaine_lancement_v1.py`. Rien de `diag/`, `runs/`, `donnees/` réels, aucun verdict.
