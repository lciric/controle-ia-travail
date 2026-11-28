# Notes des corrections VCB — plan B des juges (T0.5), v1

Traitement de la vérification des corrections du code et du brouillon 4 (constats VCB-01 à VCB-08). Date : 2026-10-20, de 04:55 à 05:45 UTC environ.

## 1. Cadre

- Rédacteur : sous-agent neuf. Il n'a écrit ni le code du plan B, ni ses relectures R2, ni ses corrections, ni leur vérification, ni les brouillons 1 à 4.
- Lus en entier : le rapport de vérification (`verification-corrections/verification-corrections-R2-code-plan-B-v1.md`, `a751e43c…`) et le traitement. Lus en partie : le brouillon 4 (en-tête, « Métrique », « Plan d'analyse », « Liste d'arrêt », « Code à écrire et tests », « Transparence », « Contre-lecture », introduction de l'annexe A), les modules et tests touchés, les pilotes de mutants de la vérification, `LISEZMOI.md` de l'invite.
- Aucune donnée scellée ouverte, sauf par les contrôles mécaniques : empreintes de fichiers et configuration du manifeste du pilote (comme au brouillon 4).
- Aucun commit, aucune poussée, aucune commande Vast.ai, aucun service payant, aucun modèle réel. Tous les lancements Python sous `nice -n 19`, avec `-B`, `-p no:cacheprovider`, `--basetemp` et `TMPDIR` dans le bloc-notes.
- Modules gelés : non touchés. Seuls `requalifier_juges.py`, `lire_requalification.py` et trois fichiers de tests ont changé ; `rubrique_simplifiee.py`, `juges_simplifies.py`, `test_plan_b_juges_simplifies.py` et `test_plan_b_integration.py` sont inchangés.
- Copies d'avant ces corrections (pour les différences) : `corrections-v1/originaux-vcb/` (neuf fichiers, empreintes ci-dessous).

## 2. Fichiers (sha256)

| fichier | avant (originaux-vcb) | après |
|---|---|---|
| `src/controle_ia/environnements/requalifier_juges.py` | `75346dc03e2da428ef131039110cd17bcec66ad7f06ac71a8b07ccad57ce0341` | `a0b1d15fb96e3cee06f78c395bf507931c745458f18f4cf27a61f3e13f369ba8` |
| `src/controle_ia/environnements/lire_requalification.py` | `440a9778833c472f0ed489817bc7bc5ec26f2683a9dd2f3062f076debcbaa507` | `4ee817c6be09a9a79e7fd2134ef08add47fbb26f923bb1f08c3f2de7a6f5736d` |
| `src/controle_ia/environnements/rubrique_simplifiee.py` | `beeb1017…` | inchangé |
| `src/controle_ia/environnements/juges_simplifies.py` | `01a4e0c4…` | inchangé |
| `tests/test_plan_b_requalifier.py` | `fa39c2c3ea4efcd2a52196cf7a658d6bdf626d02b62dbbdce57ca1504fd9723d` | `1b8aa9beda7af5f9ced8836be97e2b199b13a94acec589be7f539e838b1da0ae` |
| `tests/test_plan_b_lecteur.py` | `a9cac945b98aae5e3728de61694bac543524bc42b402cb6be92e68d41ae2ae69` | `1693cbe1beae5401570d1c1718b4b21077a079f9c26fb2f3efa9a9fb5c7f7e1a` |
| `tests/test_plan_b_rubrique_simplifiee.py` | `f925fbfca92433f9bd8748c170ca14a868045614c8b7e17a401bb3da597250f7` | `c04c1735162c9705e4b7412c3cccf29354fc9c86edecc73e38bb1cc30ef8326e` |
| `tests/test_plan_b_juges_simplifies.py` | `403e1461…` | inchangé |
| `tests/test_plan_b_integration.py` | `0c1ea90f…` | inchangé |
| brouillon 4 (source, intact) | `528a238667a7a5220a207982487682f677a1687f2ecbea1beac6ae247e2225b1` | — |
| brouillon 5 (`plan-b-juges/T0.5-plan-B-juges-v1-brouillon5.md`, 666 lignes) | — | `1d6f1932d8597421caeedeff16e7d0175003921c40bc0173c133cbdb3ef768f2` |

Tests : 389 avant, 413 après (24 ajoutés : 1 pour VCB-01, 14 pour VCB-03, 7 pour VCB-02, 1 pour VCB-04, 1 pour VCB-07). Aucune fonction de test retirée (comparaison des noms par `ast`) ; les seules lignes retirées des tests sont trois docstrings, réécrites et complétées.

## 3. Corrections, constat par constat

- **VCB-01** (graine par appel du témoin). Test neuf `test_temoin_graine_posee_avant_chaque_appel` (T-rq). Deux prises : un espion sur `torch.manual_seed` et `generate` exige, à chaque appel, `[("manual_seed", graine), ("generate",)]` ; les jetons générés, capturés en enveloppant `generate`, sont égaux pour deux appels de même graine faits depuis deux états différents du générateur global, et différents sous une autre graine. Essai préalable sur le jouet : graines 12, 12, 13, 14, 15 depuis des états globaux 1 à 5 : jetons égaux pour 12 et 12, différents ailleurs ; rangées réduites toutes `[(6, True), (6, True)]` (c'est pourquoi l'ancienne égalité ne voyait rien). RQ-17 meurt sur l'espion, seul et après les autres tests du témoin (`mutants-v2/sortie-rq17-v2.txt`) : la raison est écrite, elle ne dépend pas de l'état du générateur.
- **VCB-02** (`lot_juge` au lecteur). `exiger_config_de_l_etape` exige `lot_juge` présent (`_champ`) et entier positif (booléen refusé), après les autres gardes de la configuration, avant toute lecture des fichiers du run ; elle le rend, et `lire_requalification` le passe à `lots_du_rejeu`. L'ancienne lecture sous condition (`_champ(m_b["config"], "lot_juge", …)` seulement si un fichier du rejeu est écrit) est retirée. Tests neufs (T-lr) : `test_lot_juge_exige_par_le_lecteur_cas_sain_et_artefacts` (six artefacts) et `test_lot_juge_exige_meme_sans_fichier_du_rejeu` (cas sain et artefact sans fichier du rejeu ; l'artefact passait avant la correction). VCB-M01 ne trouve plus son ancien texte : porté (VCB-M01p, même défaut à la place neuve), tué. Mutant neuf VCB-M19 (non entier accepté) : tué.
- **VCB-03** (un artefact par intitulé). Test neuf paramétré `test_chaque_intitule_de_citation_absent_repete_ou_different` (T-rq), un paramètre par intitulé (14), trois formes chacun (l'entropie, sans valeur attendue : deux), message attendu propre à la citation, aucun run créé ; cas sain par paramètre. **Trou trouvé en écrivant le test** : un commit cité deux fois avec deux valeurs (la juste d'abord) passait, car la fonction gelée `exiger_code_cite` ne lit que la première occurrence, et `exiger_citations_planb` ne lisait pas le commit. Le texte (l. 9 et liste d'arrêt « Avant le manifeste ») exige une seule valeur par intitulé, commit compris. Correction dans le module neuf : `exiger_citations_planb` exige aussi une valeur unique de `COMMIT_CITE` (motif gelé importé), après les autres citations ; message « commit du code d'analyse cité(e) plusieurs fois, différemment ». Le refus du brouillon tel quel garde son premier motif (« configuration cité(e) nulle part »). Mutants : VCB-M14 à VCB-M17 tués ; VCB-M18 (neuf : la garde du commit retirée) tué. Le contrôle mécanique sur le brouillon 5 montre le trou et sa garde : commit cité deux fois, `exiger_code_cite` rend le commit, `exiger_citations_planb` arrête.
- **VCB-04** (cadre du rejeu au lecteur). Test neuf `test_cadre_du_rejeu_plafond_et_dernier_lot_incomplet` (T-lr) : 44 notations synthétiques écrites en clair ; cadre attendu [0, 3, 4], égal à `rq.cadre_du_rejeu` ; tirage égal à celui de `rq.tirer_lots` ; artefacts : tirages consignés sur les cadres d'un lanceur fautif ([0, 1, 3, 4], [0, 3, 4, 5]) : arrêt. VCB-M02 et VCB-M03 tués.
- **VCB-05** (rôles de l'ancrage). Texte seulement, sur la consigne de la session (point ouvert 1 du traitement) : « Métrique » (l. 144) et « Ordre des phases », étape 5 (l. 259). Le code (`ancrage_noyaux` : `ecarts_par_jeton(a_defaut, a_math)`, rôles consignés) et son test des rôles sont inchangés.
- **VCB-06** (échéances). Docstring du lanceur (l. 25) et de `_avant` complétées. Texte « Dépassement » (l. 264) : les cinq points de contrôle ; dépassement d'au plus l'étape commencée ; les durées de la conversion et du repère, de l'ancrage et d'un rechargement ne sont pas mesurées et sont comptées sous la borne d'un lot ou d'un appel de la même phase (point ouvert VCB-a du traitement). Sans ces contrôles, elles s'ajouteraient au lot précédent : la borne écrite supposait déjà ces étapes courtes.
- **VCB-07** (annexe A). Test neuf `test_annexe_a_premiere_ligne_de_debut_derniere_ligne_de_fin` (T-rs) : quatre artefacts (fin en double juste après l'annexe : « ≠ RS1.txt » ; fin en double après l'annexe B : « sans le retrait » ; début en double juste avant : « ≠ RS1.txt » ; début en double dans l'introduction : « sans le retrait ») et un cas sain de la règle (fin isolée avant l'annexe : extraction égale à `RS1.txt`). Sur chaque texte, la commande de `LISEZMOI.md`, extraite du fichier et jouée telle qu'écrite (`sys.executable -I -c`), rend l'empreinte de `RS1.txt` exactement quand la garde passe. VCB-M11, VCB-M12 et VCB-M13 tués. Code inchangé.
- **VCB-08** (rédaction). (a) docstring du lecteur : tirage des lots, extraction de l'annexe A, exigence des décalages ; `lot_juge` dans ses gardes ; (b) réserve « ancrage au-dessus de 1e-3 ou illisible aux couches … » (commentaire : un R_S illisible n'est pas sous 1e-3) ; les tests qui lisent cette réserve (`"['7']"`, `"['15']"` dans le libellé) passent ; (c) docstring de `annexe_a_comme_au_texte` sans numéros de ligne. Texte inchangé pour VCB-08.
- Docstrings des modules de tests complétées (VCB-01, VCB-02, VCB-03, VCB-04, VCB-07). Lignes neuves de 120 caractères au plus (les dépassements restants sont anciens).

## 4. Brouillon 5

- Construit par `plan-b-juges/travail-b5/construire_brouillon5.py` (`988bd4bf…`) : 31 remplacements exacts, chacun trouvé une seule fois dans le brouillon 4 (empreinte du brouillon 4 contrôlée d'abord) ; le bloc de l'annexe A (de la ligne de début à la dernière ligne de fin) est comparé avant et après : identique. Sortie : `travail-b5/sortie-construction-brouillon5.txt`. Le brouillon 4 est intact (`528a2386…`).
- Changements : titre ; auteur et provenance (brouillon 5, rapport VCB) ; lignes de citation (commit unique, VCB-03) ; « Métrique », ancrage (VCB-05) ; « Ordre des phases », étape 5 (VCB-05) ; « Dépassement » (VCB-06) ; « Lecture », gardes (VCB-02) ; table « Configuration », ligne `lot_juge` (troisième colonne seulement : valeurs et empreinte canonique inchangées) ; « Avant le scellement » (vérification faite, restes, contrôles refaits, versement, registres) ; liste d'arrêt « À la lecture » (VCB-02) ; « État au brouillon 5 » ; points 4 et 5 du code ; tests (invite RS1 : VCB-07 ; témoin : VCB-01 ; gardes d'avant le manifeste : VCB-03 ; lecteur : VCB-02, VCB-04) ; « Transparence » (pour le brouillon 5 ; du brouillon 4 au brouillon 5) ; « Contre-lecture » (vérification des corrections ; à venir) ; introduction de l'annexe A (brouillons 2 à 5 ; contrôle sur les brouillons 4 et 5).
- Contrôles mécaniques : `travail-b5/controles_brouillon5.py` (`1cc63a5a…`), sortie `travail-b5/sortie-controles-brouillon5.txt` (`823203f7…`). Annexe A : commande de `LISEZMOI.md` jouée telle qu'écrite, dans `travail-b5/controles/lisezmoi/` sur une copie nommée `T0.5-plan-B-juges-v1.md` (empreinte de la copie = brouillon 5) : `b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7` = `RS1.txt` (`sortie-commande-lisezmoi-brouillon5.txt`) ; `exiger_annexe_a_egale_a_rs1` : même empreinte ; artefacts : arrêt. Table « Configuration » : acceptée par le lanceur et le lecteur, `lot_juge` rendu = 8, empreinte canonique `8ff777cf903a104a94e9759d0b7dc1240d8e6c68ae58a0e52d225d4e80837b76` (inchangée). Citations : texte tel quel refusé ; copie remplie acceptée, puis effacée ; artefacts « résumé cité deux fois » et « commit cité deux fois » : arrêt.

## 5. Mutants rejoués (`corrections-v1/mutants-v2/`)

Pilote `muter_v2.py` (`0c0753fb…`), repris de celui de la vérification : la base est le clone (jamais écrit ; chaque module muté est restauré depuis lui et comparé octet pour octet) ; `src/`, `tests/` et `pyproject.toml` copiés dans `wN`, les autres entrées du clone liées (sans `.git`). Mêmes substitutions et mêmes tests ciblés (`-x`) que la vérification (`liste_mutants_verification.py`, copie exacte, `5747332534241b99c553757fb823b28f622111724b34f727346b98703ef7b0e9`). Deux travailleurs et le témoin en parallèle, sous `nice -n 19`. Copies `w0`, `w1`, `wT`, `wR` et `tmp` effacées après usage (`rm -r` : les liens seuls).

| mutant | origine | résultat | premier échec |
|---|---|---|---|
| témoin (copie non mutée) | — | `413 passed in 649.93s` | — |
| RQ-17 (témoin sans graine) | survivant | **tué** | `test_temoin_graine_posee_avant_chaque_appel` |
| VCB-M01p (`lot_juge` absent accepté, 8 par défaut ; porté) | survivant | **tué** | `test_lot_juge_exige_par_le_lecteur_cas_sain_et_artefacts[absent]` |
| VCB-M02 (cadre sans la condition du plafond) | survivant | **tué** | `test_cadre_du_rejeu_plafond_et_dernier_lot_incomplet` |
| VCB-M03 (cadre avec le dernier lot incomplet) | survivant | **tué** | idem |
| VCB-M11 (fin contrôlée sur la première ligne de fin) | survivant | **tué** | `test_annexe_a_premiere_ligne_de_debut_derniere_ligne_de_fin` |
| VCB-M12 (bloc arrêté à la première ligne de fin) | survivant | **tué** | idem |
| VCB-M13 (dernière ligne de début) | survivant | **tué** | idem |
| VCB-M14 (épisodes du pilote jamais comparés) | survivant | **tué** | `test_chaque_intitule_…[épisodes du pilote]` |
| VCB-M15 (tâches jamais comparées) | survivant | **tué** | `…[tâches]` |
| VCB-M16 (manifeste des notations jamais comparé) | survivant | **tué** | `…[manifeste des notations]` |
| VCB-M17 (run du pilote jamais comparé) | survivant | **tué** | `…[run du pilote]` |
| VCB-M04 (clés sans leur ordre) | témoin positif | tué | `test_tirage_des_lots_recalcule_cas_sain_et_artefacts` |
| VCB-M18 (commit répété accepté) | neuf | tué | `…[commit du code d'analyse]` |
| VCB-M19 (`lot_juge` non entier accepté) | neuf | tué | `test_lot_juge_exige_par_le_lecteur_cas_sain_et_artefacts[nul]` |

Bilan : les 11 survivants nommés par le rapport meurent tous ; 14 rejoués, 14 tués. Pièces : `resultats-w0.jsonl` (`2c1c7046…`), `resultats-w1.jsonl` (`a2821a39…`), `journal-temoin.txt` (`546b4799…`), `sortie-rq17-v2.txt` (`cb39d460…`), `liste_mutants_v2.py` (`68fbe4ea…`), `rejouer_rq17_v2.py` (`2ccd39a9…`).

## 6. Tests du plan B, à la fin (clone)

Commande : `cd plan-b-code/depot && nice -n 19 env PYTHONPATH=src … python -B -m pytest -q -p no:cacheprovider --basetemp=<bloc-notes> tests/test_plan_b_rubrique_simplifiee.py tests/test_plan_b_juges_simplifies.py tests/test_plan_b_requalifier.py tests/test_plan_b_lecteur.py tests/test_plan_b_integration.py`. Sortie : `corrections-v1/pytest-plan-b-vcb.txt`.

- Résultat : `413 passed in 195.80s (0:03:15)`, code 0 (`pytest-plan-b-vcb.txt`, `a06cf1ee207457219c33f9829be9713fe5e6e3a2576d9fbd4fcc82dccb733789`). Avant ces corrections : 389.
- Clone à la fin : `git status --short` montre les 10 entrées non suivies (les mêmes qu'avant) ; `git diff --stat HEAD` est vide ; aucun `__pycache__`. Dossiers temporaires de pytest effacés (`vcb-travail/bt`, `vcb-travail/tmp`) ; restent les deux scripts d'essai (`vcb-travail/essais/`).

## 7. Points ouverts

Dans le traitement, section « Vérification des corrections (VCB) » : VCB-a (durées non mesurées de la conversion et du repère, de l'ancrage et d'un rechargement), VCB-b (`max_nouveaux_juge` lu sans garde de forme par le lecteur : `KeyError`, non `GardeArret` ; non corrigé, hors des constats), VCB-c (vérification de ces corrections par un sous-agent neuf, à décider).
