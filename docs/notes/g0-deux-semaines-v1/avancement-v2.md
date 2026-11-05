# Avancement du lanceur de T0.6 v2 (fichier de reprise ; branche `prep/t06-lanceur-v2` par-dessus `4448fa9a`)

Règle : chaque ligne passe à « fait » quand le fichier est sur le disque et committé ; un redémarrage reprend à la première
ligne « à faire ». Noms neufs (R12) : aucun fichier de la v1 n'est modifié.

| point | état | fichier(s) |
|---|---|---|
| C01 PROGRES sans état de sonde | fait (code) | `t06/lanceur_v2.py` (`test_croise_v2`, `progres` neutres) ; essai à faire |
| C02 `ligne_A` hors PROGRES, lignes A/B/C hors de `run.json` | fait (code) | `t06/lanceur_v2.py` (`resume_imprimable`) ; essai à faire |
| C03 activations float16 + garde de disque | fait (code) | `t06/lanceur_v2.py` (`ActivationsDemi`, `exiger_place_disque`) ; essai à faire |
| C04 clés non lues refusées, `temoin_lexical`/`sondes_figees_p3` nuls exigés, `fils_test_croise` exigé | fait (code) | `t06/configuration_v2.py` ; essai à faire |
| C05 mémoire vive 128 000 Mo | à faire | `config-t06-reel-v1-brouillon2.json` |
| C06 réserves par adaptateur + contrôle négatif sous A | fait (code) | `t06/lecture_v2.py` ; essai à faire |
| C07 jeux par `jeu_ou_echec` | fait (code) | `t06/lanceur_v2.py` ; essai à faire |
| C08 dépense cumulée (antérieure + téléchargement), heure d'épuisement passée à l'amorce | fait (module) | `t06/session_v2.py` ; `lancer_t06_v2.sh`, `amorce_instance_t06_v2.sh` à faire |
| C09 garde illisible → ALERTE, arrêt après trois échecs | à faire | `lancer_t06_v2.sh` |
| C10 artefacts des poussées, disque simulé dans l'essai | à faire | `tests/test_t06_v2_scripts.py` |
| C11 sous-ensemble en morceaux < 90 Mo + manifeste ; refus > 90 Mo avant commit ; données légères en commit à part | fait (lanceur) | `t06/lanceur_v2.py` ; amorce à faire |
| C12 offre relue et vérifiée (carte, mémoire, cœurs, disque, prix, téléchargement), instances du programme | fait (module) | `t06/session_v2.py` ; `lancer_t06_v2.sh` à faire |
| C13 second démarrage après fin normale : poussée puis sleep infinity ; stopped → sleep infinity | à faire | `amorce_instance_t06_v2.sh` |
| C14 échéance : consigner et pousser avant le DELETE | à faire | `amorce_instance_t06_v2.sh` |
| C15 prix maximal par carte en configuration, carte en argument | fait (module) | `configuration_v2.py`, `session_v2.py` ; `lancer_t06_v2.sh` à faire |
| C16 libération des activations, durée par couple | fait (code) | `t06/lanceur_v2.py` |
| L04 unité du lot et pas déclarés (480) | fait (code) | `configuration_v2.py` (`unite_du_lot`, `pas_de_distillation_declares`) |
| L05 règle « non interprétable » en configuration | fait (code) | `configuration_v2.py`, `lecture_v2.py` |
| L11 dernier jour de création et fin du GO en configuration | fait (code) | `configuration_v2.py` (`calendrier`) ; scripts à faire |
| configurations v2 (réelle brouillon 2, jouet v3) | à faire | `docs/notes/g0-deux-semaines-v1/` |
| essais v2 | à faire | `tests/test_t06_v2_*.py` |
| banc v2 | à faire | `scripts/banc_mutations_t06_v2.py` |
| E0 (test croisé synthétique, 0 USD) | à faire | `scripts/epreuve_e0_t06_v2.py`, journal scellé |
| E1 (jouet sous l'amorce v2, 0 USD) | à faire | `scripts/epreuve_e1_t06_v2.sh`, journal scellé |
| rapport v2 | à faire | `rapport-developpeur-lanceur-T0.6-v2.md` |
