# Journal de l'exécutante du saboteur à budget — v4

Session `session_013QMaymHf2YhybDs3MJ62xr`, branche `claude/iib-executante-v1`. Suite du journal v3 (`registres/iib-executante/journal-v3.md`, `888c0b5b…3305`), qui reste tel quel. Exploratoire, non opposable (R-522).

## 2026-11-19, vers 04:37Z — règle précisée de la passe de recalcul (mère ; remplace la formulation de R-3598 portée au journal v3)
- Du côté exposé, aucune personne ni aucun programme autre que le code de la passe n'ouvre les fichiers de scores ni le sous-échantillon d'activité brute de la livraison, avant comme après leur envoi.
- Il reste permis de les copier, de les déposer, de les transmettre et d'en calculer l'empreinte.

## 2026-11-19, vers 04:37Z — champ `run_id` des deux extraits (question de la mère)
- Extrait de la passe (`scripts/extrait_iib_cote_moniteurs_v2.py`) : `run_id` écrit depuis l'argument `--run-id` (l. 101) ; le programme refuse si le `run_id` de `runs/<run>/manifeste.json` scellé diffère de cet argument (l. 57-59).
- Extrait des états (`scripts/extrait_iib_etats_lectures_cote_moniteurs_v2.py`) : `run_id` écrit depuis l'argument `--run-id` (l. 131) ; contrôlé par la forme du lancement (`_RUN_ID`) et par la présence des deux lectures scellées sous `diag/<run>/` ; aucune comparaison au manifeste.
- Même valeur au caractère près : oui, par procédure et non par le code seul. Engagement : les deux programmes reçoivent la même chaîne, le `run_id` du manifeste scellé de la course ; après écriture, les deux champs `run_id` (et eux seuls) sont comparés par programme, et l'égalité est consignée ici avant tout versement.
