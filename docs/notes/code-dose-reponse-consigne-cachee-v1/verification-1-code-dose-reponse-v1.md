# Rapport de la vérification 1 des corrections du code de la dose–réponse (classe B)

Pièce versée par le développeur, à l’identique du rapport rendu par le même contre-lecteur que la contre-lecture 1 (sous-agent, Sonnet 5.5, effort élevé), sur le commit a02b6540070aa5731875d07fbbe124f2dbe27f3b.

---

# Vérification des corrections (commit a02b6540), un seul lot

**Verdict : prêt, sous quatre réserves mineures (V2-01 à V2-04).** Aucun défaut bloquant ni majeur n'est introduit, et les dix constats CL-02 à CL-11 sont corrigés. CL-01 est hors code et tranché.

J'ai rejoué `tests/test_dose_reponse_v2.py` : 45 passent en 198 s, ce qui correspond à `ATTENDUS="45"` de l'amorce v2. L'empreinte de `scripts/tests-cibles-dose-reponse-v2.txt` est `5126a738…`, égale à `LISTE_SHA256`. Les compagnons `.sha256` des fichiers v2 sont conformes, `bash -n` est OK sur les deux scripts, et les fichiers v1 sont inchangés (diff vide).

## État de chaque constat

| CL | État | Preuve |
|---|---|---|
| CL-01 | hors code, tranché | Lazar a reporté les deux contrôles croisés à une course suivante (R-5280, relayé par la mère). Le code joue quinze conditions, comme le texte scellé et le devis. |
| CL-02 | corrigé | `course_v2.py` : le contrôle négatif est compté par bloc dans `bloc.json` (`ecrire_bloc`, champ `controle_negatif_equivalence`) et additionné à la fin. Les blocs repris sont inclus (`reprendre` → `controles_negatifs_repris`). `_exiger_controle_negatif_final` n'arrête qu'au bilan : moins de 10 comparables donne « non concluant », au-delà une fraction sous 0,95 arrête. Plus aucun arrêt en cours de course. L'essai `test_cl02_controle_negatif_juge_a_la_fin` couvre le cas sain, le cas « non concluant » et l'artefact. |
| CL-03 | corrigé | Rejoué : `{"score": 3} "sonde": 1` dans `textes.jsonl` ne déclenche rien. `score_sonde` est arrêté dans `mesures.jsonl`, y compris imbriqué dans des listes et des dictionnaires. Le nom de fichier contenant `sonde` ou `score` est toujours arrêté. La lecture se fait en JSON sur `mesures.jsonl`, `episodes.json` et `bloc.json` seulement. |
| CL-04 | corrigé | `controles_v2.controler_textes_avant_creation` appelle `charger_piece_jointe` (forme stricte) et `longueurs_en_jetons`, avec le tokeniseur seul de l'agent à la révision figée. Il ne rend que des comptes, rien n'est imprimé de plus. `lancer_dose_reponse_v2.sh controles` l'exécute avant toute création. Il échoue en position fermée si `transformers` ou le jeton HF manquent. L'essai `test_cl04` couvre le cas sain, la forme altérée et le rapport supérieur à 1,15. |
| CL-05 | corrigé | `exiger_config(config, racine)` exige `config == configuration(...)`, reconstruite depuis la configuration 7b dont l'empreinte est vérifiée. Rejoué : `fraction_min_controle_negatif=0`, `actions_min_controle_negatif=10**9`, `fils=64`, `noyau_attention`, `memoire_vive_min_go=0`, `variables_gabarit={}` sont tous refusés. La désignation est portée en option par `scripts/ecrire_configuration_dose_reponse_v2.py` (`--designation`, avec les clés `chemin`, `sha256`, `lignes_registre`). |
| CL-06 | corrigé | `controler_registre` exige que la ligne CODE cite `commit_code` (essai : ligne présente sans le commit, refus « CL-06 »). `exiger_code_importe_sous` est appelé en mode réel dans `controles()`. Je valide votre raisonnement sur `exiger_code_cite` : le texte scellé ne cite aucun commit de code, et le lien passe par la ligne CODE, `commit_code` et `git diff` du lanceur et de l'amorce. |
| CL-07 | corrigé | `lire()` court-circuite en C1 si `exiger_table` n'est pas conforme : aucun effet n'est calculé, et une action manquante donne C1 au lieu d'un arrêt. Une inversion non calculable ou une tendance non calculable rend l'échelle « non établie », avec le motif « lecture non calculable (inversions) » ; la valeur de `etablie` exige maintenant `tend["calculable"]` et `not inv_non_calc`. Essais : `test_cl07_effectif_en_defaut_donne_C1_sans_effet` et `test_cl07_lecture_non_calculable_n_etablit_pas_l_echelle`. |
| CL-08 | corrigé | `executer_lecture` compare `verifier(PREREG)` à `PREREG_SHA256`. Une lecture décisive exige un préenregistrement et (64 tâches, 10 000, 10 000). La ligne de commande exige `--prereg`. Une lecture d'essai passe par `jouet=True`, sans préenregistrement, et écrit `lecture-cout-dose-reponse-jouet.json`. `exiger_premiere_lecture` globe `lecture-cout-dose-reponse*.json`. |
| CL-09 | corrigé | L'en-tête de reprise hache `CLES_SCIENTIFIQUES` (`reglages`, `agent`, `prereg`, `piece_jointe`, `consignes_premier_test`, `banque`, `modules_repris`, `commit_code`, `mode`), sans `lancement`. `lecture_v2.charger_course` compare toujours `config_sha256` entre blocs, ce qui reste cohérent. |
| CL-10 | corrigé | `test_cl10_niveaux_corriges_figes` fige les quatre niveaux et lit `niveau` dans les sorties (gradation, inversions, DR-1). Une mutation à 0,95 y est détectée. Ajoutés : ligne C4 et séquence DR-6, déclencheurs d'audit 1, 3, 4, 5 et 6, sélectivité et sa réserve, contrôle négatif final, et la garde d'offre réellement employée (`session_v1 choisir`). |
| CL-11 | corrigé | `exiger_calendrier` refuse après le 2026-12-12 (rejoué : le 12 est accepté, le 13 refusé). Le lanceur le joue dans `controles` et fait en plus, à la création, la comparaison sur la date réelle du jour (`[ "$(date -u +%F)" \< "2026-12-13" ]`, vérifiée en bash). |
| Point (b) | sans objet pour le code | La sélectivité « établie » reste la conjonction des deux proportions. Il reste à la nommer dans la ligne CODE, ce qui est un acte de la mère. |

## Constats neufs introduits par la v2 (tous mineurs)

- **V2-01.** `controles_v2.py` `configuration()` fige `go_admis = [GO_ORIGINE]` et `dernier_jour_creation`, et `exiger_config` exige l'égalité stricte. Une prolongation de GO ou un report du dernier jour de création demande donc un nouveau code, un nouveau commit et une nouvelle ligne CODE. C'est cohérent avec R12, mais c'est une rigidité à connaître : un GO prolongé se traite par une version v3.
- **V2-02.** `exiger_sans_score_de_sonde` ne parcourt plus que les trois noms de fichiers listés dans `FICHIERS_STRUCTURES`, plus les noms de fichiers. Un fichier JSON ajouté plus tard sous un autre nom ne serait pas scanné. Sans effet aujourd'hui, car la course n'en écrit pas d'autre dans `donnees/<run>/blocs`.
- **V2-03.** Dans le lanceur v2, l'étape CL-04 de `controles` n'attrape que `GardeArret`, `OSError`, `ValueError` et `KeyError`. Un `ImportError` (par exemple `transformers` absent du `python3` de la session) sort en trace, avec un code non nul et une trace non filtrée sur la sortie. Le résultat reste « pas de création », donc rien n'est dépensé. Il faudrait aussi attraper `ImportError`, pour garder la sortie courte.
- **V2-04.** En-têtes et docstrings v2 : `controles_v2.py`, `course_v2.py`, `lecture_v2.py` et les commentaires des deux scripts citent encore `controles_v1`, `lecture_v1`, `course_v1`. Le code lancé est bien v2 (vérifié dans l'amorce : `course_v2`, `controles_v2`, liste de 45 essais). Cela n'a pas d'effet, mais peut tromper un futur lecteur.

## Déclaration de cloisonnement

Je n'ai lu ni texte privé, ni score, ni verdict, ni sortie de course. Je n'ai ouvert ni `consignes-privees-dose-reponse-consigne-cachee-v4.json` ni `prereg/P3-consignes-v1.md`. Je n'ai lu ni `diag/`, ni `runs/`, ni `donnees/`, ni `registres/etat.md`, ni une passation. Je n'ai créé aucune instance, aucune génération sous texte privé, aucun fichier du dépôt modifié ni commité. Mes essais et mes scripts sont dans le bloc-notes, hors dépôt.