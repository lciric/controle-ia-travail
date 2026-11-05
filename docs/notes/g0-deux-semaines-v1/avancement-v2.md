# Avancement du lanceur de T0.6 v2 (fichier de reprise ; branche `prep/t06-lanceur-v2` par-dessus `4448fa9a`)

Règle : chaque ligne passe à « fait » quand le fichier est sur le disque et committé ; un redémarrage reprend à la première
ligne « à faire ». Noms neufs (R12) : aucun fichier de la v1 n'est modifié.

| point | état | fichier(s) |
|---|---|---|
| C01 PROGRES sans état de sonde | fait (J1) | `t06/lanceur_v2.py` (`test_croise_v2`, `progres` neutres) ; essai `tests/test_t06_v2_lanceur_jouet.py::test_repetition_jouet_v2_par_la_commande_sans_fuite` |
| C02 `ligne_A` hors PROGRES, lignes A/B/C hors de `run.json` | fait (J1) | `t06/lanceur_v2.py` (`resume_imprimable`) ; même essai |
| C03 activations float16 + garde de disque | fait (J1) | `t06/lanceur_v2.py` (`ActivationsDemi`, `exiger_place_disque`) ; essais `test_place_disque_simulee`, `test_activations_demi_precision_sans_arrondi_silencieux` |
| C04 clés non lues refusées, `temoin_lexical`/`sondes_figees_p3` nuls exigés, `fils_test_croise` exigé | fait (J1) | `t06/configuration_v2.py` ; essais `tests/test_t06_v2_configuration.py` |
| C05 mémoire vive 128 000 Mo | fait (J1) | `config-t06-reel-v1-brouillon2.json` (`memoire_vive_min_go` 128, `offre.memoire_vive_min_mo` 128000) |
| C06 réserves par adaptateur + contrôle négatif sous A | fait (J1) | `t06/lecture_v2.py` ; essai `test_reserves_cout_par_adaptateur_et_controle_negatif` |
| C07 jeux par `jeu_ou_echec` | fait (J1) | `t06/lanceur_v2.py` ; vérifié dans la répétition jouet v2 |
| C08 dépense cumulée (antérieure + téléchargement), heure d'épuisement passée à l'amorce | fait (module) | `t06/session_v2.py` ; `lancer_t06_v2.sh`, `amorce_instance_t06_v2.sh` à faire |
| C09 garde illisible → ALERTE, arrêt après trois échecs | à faire | `lancer_t06_v2.sh` |
| C10 artefacts des poussées, disque simulé dans l'essai | à faire | `tests/test_t06_v2_scripts.py` |
| C11 sous-ensemble en morceaux < 90 Mo + manifeste ; refus > 90 Mo avant commit ; données légères en commit à part | fait (lanceur) | `t06/lanceur_v2.py` ; amorce à faire |
| C12 offre relue et vérifiée (carte, mémoire, cœurs, disque, prix, téléchargement), instances du programme | fait (module) | `t06/session_v2.py` ; `lancer_t06_v2.sh` à faire |
| C13 second démarrage après fin normale : poussée puis sleep infinity ; stopped → sleep infinity | à faire | `amorce_instance_t06_v2.sh` |
| C14 échéance : consigner et pousser avant le DELETE | à faire | `amorce_instance_t06_v2.sh` |
| C15 prix maximal par carte en configuration, carte en argument | fait (module) | `configuration_v2.py`, `session_v2.py` ; `lancer_t06_v2.sh` à faire |
| C16 libération des activations, durée par couple | fait (code) | `t06/lanceur_v2.py` |
| L04 unité du lot et pas déclarés (480) | fait (J1) | `configuration_v2.py` (`unite_du_lot`, `pas_declares` lu et vérifié avant le manifeste : `exiger_pas_declares`) ; essais |
| L05 règle « non interprétable » en configuration | fait (J1) | `configuration_v2.py`, `lecture_v2.py` ; essai `test_etat_du_jeu_v2_selon_la_regle` |
| L11 dernier jour de création et fin du GO en configuration | fait (code, J1) | `configuration_v2.py` (`calendrier`), `session_v2.py calendrier` (vérifié contre le registre des GO) ; scripts à faire (J2) |
| configurations v2 (réelle brouillon 2, jouet v3) | fait (J1) | `config-t06-reel-v1-brouillon2.json`, `config-t06-jouet-v3.json` |
| essais v2 | partiel (J1 : configuration, session, lanceur jouet) | `tests/test_t06_v2_*.py` ; scripts à faire (J3) |
| banc v2 | à faire | `scripts/banc_mutations_t06_v2.py` |
| E0 (test croisé synthétique, 0 USD) | à faire | `scripts/epreuve_e0_t06_v2.py`, journal scellé |
| E1 (jouet sous l'amorce v2, 0 USD) | à faire | `scripts/epreuve_e1_t06_v2.sh`, journal scellé |
| rapport v2 | à faire | `rapport-developpeur-lanceur-T0.6-v2.md` |
