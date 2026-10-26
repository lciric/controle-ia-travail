# Corrections de l'organisme écrit par Gemini — v5 des corrections, sur la v6.2 de Gemini

Écrit le 26 octobre 2026 (à partir de 23:30 UTC le 25) par la lignée « conv-audit », sur le mot direct de Lazar dans sa
session (26 octobre, 00:27 Paris : « tu ne peux pas corriger toi-même pour lever les réserves stp ? tu as mon accord pour
retoucher la version de gemini »), après la vérification de la v6.2 (sous-agent neuf, 25 octobre 2026, 22:58–23:21 UTC ;
`verification-v62-poussee-v1/LISEZMOI-v1.md`, `e4ce11c95df2022bf376498b9ff4608e2346f0b9dda85a9e3832461d4609b05f`) : aucun
défaut bloquant, 7 des 13 points levés, 6 en partie (3, 4, 5, 7, 9 et 10). Les corrections C-01 à C-13
(`CORRECTIONS-v1.md` à `CORRECTIONS-v4.md`) valent toujours. La conception de Gemini ne change pas hors des quatre
corrections ci-dessous.

- **Source** : la v6.2 poussée par Gemini, commit `3bbb78c1991baf17feb421529fa1957be7edec59` (branche
  `canal/gemini-organisme-v6-2`, fils unique de `fedb065`), chemin `organisme/`, 24 fichiers, empreinte d'arbre
  `3b2d8d5a9af75b5457579c847d4ea9510f9da92818805123ed037f7c8436c946`.
- **Exécutions** : seulement en isolation (copie à part passée à l'utilisateur `nobody`, réseau coupé par `unshare -n`,
  environnement vide, `python -P -s -B`).
- **Version** : manifeste `6.2.1`, `VERSION = "organisme-gemini-m3-v6-2-1"`, lignée toujours déclarée « assistée ».

| correction | où (lignes de la v6.2.1) | point de la vérification et défaut | correction | essais (`tests/test_corrections_v5.py`) |
|---|---|---|---|---|
| **C-14** | `principal.py`, `_traiter_tache`, branche sans sonde | point 3 : sans sonde, `besoin_arbitrage = (conf_c1 < seuil_c1) or (len(castes) > 1)` ; l'arbitrage exigeant plus d'une caste, le terme de confiance est sans effet (redondant), choix gardé sans raisons | `besoin_arbitrage = len(castes) > 1` : le terme redondant est retiré, **le comportement ne change pas** (toutes les castes recrutées ouvrent la délibération, arrêt anticipé inchangé). Raisons de garder ce comportement plutôt que d'arbitrer selon la confiance : c'est celui de la v5.3 et de la v6.2 sans sonde ; le changer changerait le nombre d'appels et la décision de l'organisme dans toute configuration à deux castes ou plus, au-delà de la correction d'un défaut ; le mécanisme que visait la réserve d'origine (une sonde incertaine force l'arbitrage) exige une sonde, et la v6.2 l'a rendu effectif dans la branche avec sonde. `seuil_confiance_caste1` ne sert donc au routage qu'avec une sonde (dit dans `CONCEPTION.md` § 2.14). | `test_c14_sans_sonde_declencheur_sans_terme_redondant` (l'expression est `len(castes) > 1`) ; `test_c14_sans_sonde_comportement_inchange_toutes_les_castes_deliberent` ; `test_c14_une_seule_caste_aucun_arbitrage` |
| **C-15** | `principal.py`, `_entrainer_et_predire_sondes_traits` (fin du traitement d'une famille) et `executer` (appel du routage) | point 4 : repli silencieux sur l'exactitude d'entraînement quand la famille a moins de 4 tâches ou quand la prédiction de validation n'est pas exploitable ; et le routage relisait `exactitudes` (entraînement) quand `exactitudes_validation` était vide | sans exactitude de validation, la famille n'en a aucune, sa sonde ne vote pas, et la raison est consignée (« exactitude de validation indisponible pour … : aucun pli de validation … / prédiction de validation non OK … ; la sonde de cette famille ne vote pas ») ; le routage ne lit que `exactitudes_validation` | `test_c15_moins_de_4_taches_aucune_exactitude_de_validation_et_raison_consignee` ; `test_c15_prediction_de_validation_non_ok_aucune_exactitude_et_raison_consignee` ; `test_c15_cas_sain_validation_presente_lue_par_la_garde` |
| **C-16** | `principal.py`, `_expression_mots_cles` (nouvelle) et gabarit de `_synthetiser_mutation_politique_endogene` ; import des constantes de `memoire_isvd` | point 5 : trois copies des mots-clés multi-familles (constantes de `memoire_isvd.py`, littéraux du module initial, littéraux du gabarit) ; le gabarit n'était pas essayé | une seule source, `memoire_isvd.MOTS_CLES_EVAL_FAMILLE` et `MOTS_CLES_CTRL_FAMILLE` ; le gabarit écrit son expression depuis elles (même texte, mot pour mot, qu'en v6.2) et refuse un mot hors `[a-z][a-z-]*` ; la copie du module initial (en toutes lettres : la liste blanche n'admet que `import math`) est vérifiée égale à la source. **Choix gardé, avec ses raisons** : la détection reste faite sur les mots du texte, parce que la propriété détectée (une trace qui parle des deux familles) est une propriété du texte, et que le module réécrit n'a accès à rien d'autre ; une autre détection serait une conception nouvelle (Lazar décide). | `test_c16_mots_cles_une_seule_source_module_initial_et_gabarit` (module initial et module écrit par le gabarit, lus par l'arbre syntaxique) ; `test_c16_mot_cle_invalide_refuse_par_le_gabarit` |
| **C-17** | `principal.py`, `_synthetiser_mutation_politique_endogene` (réponse de l'architecte) et `_propager_successeur` | points 7, 9 et 10 : par le chemin du code brut (un bloc de code de l'architecte définissant `recompense_interne`), la validation exécutait un code arbitraire dans le fil principal sans borne de temps ; le filtre statique laissait passer des opérations au coût sans borne ; le contrôle de propreté acceptait une règle impropre entre les points lus ; le séparateur du bloc du vérificateur pouvait figurer dans une chaîne d'un candidat | le chemin du code brut est retiré : une telle réponse est refusée (`rejet_validation: code brut refusé (C-17)`, raison consignée) **sans validation ni exécution** ; seul l'objet JSON des trois paramètres bornés passe, par le gabarit, dont la forme est fixe (un JSON entre accents graves reste accepté, comme en v6.2) ; l'assemblage refuse un code muté qui porterait `import ast`. La validation ne voit plus que le code du gabarit, aux paramètres bornés : son temps est borné (essayé aux bornes et au-delà). | `test_c17_code_brut_refuse_sans_validation_ni_execution` (la validation, remplacée par un espion, n'est jamais appelée ; le successeur garde le module d'origine) ; `test_c17_json_fenced_toujours_accepte_par_le_gabarit` ; `test_c17_gabarit_aux_bornes_et_au_dela_accepte_et_valide_en_temps_borne` (quatre jeux de paramètres) ; `test_c17_assemblage_refuse_un_code_mute_qui_importe_ast` |

## Essai hérité adapté (dit, avec sa cause)

`tests/test_emprunts_v5_3.py::test_v5_3_sondes_traits_entrainer_predire_et_routage_faible_vers_fort` (essai de la v5.3,
identique en v6.2) entraînait la sonde sur **deux** tâches et attendait qu'elle vote sur son exactitude d'entraînement
(`routage_sonde_accord_precoce` vrai pour `te_clair`). Sous C-15, une sonde sans pli de validation ne vote plus : l'essai
d'origine échoue sur la v6.2.1 à cette assertion, pour cette raison (témoin ci-dessous). Adaptation : **deux tâches
d'entraînement de plus** (`tr_3`, `tr_4`), pour qu'un pli de validation existe ; le faux noyau donne aux tâches du pli
une probabilité conforme à leur vérité ; l'assertion « données d'entraînement == {tr_1, tr_2} » devient « deux tâches,
hors vivier, hors pli de validation, les quatre tâches couvertes » ; une assertion s'ajoute (exactitude de validation
1,0). Les deux assertions de routage (`te_clair` vrai, `te_ambigu` faux) et toutes les autres sont gardées telles quelles.
Aucun autre essai de Gemini n'est changé.

## Résultats (en isolation)

- **v6.2.1** : 68 essais passent (les 53 de la v6.2, dont l'essai hérité adapté, et les 15 de `test_corrections_v5.py`).
- **Témoin, `test_corrections_v5.py` sur la v6.2 (`3bbb78c`)** : 7 échecs, 8 réussites — échouent les 7 essais qui visent
  une correction (C-14 : l'expression ; C-15 : les deux absences de validation ; C-16 : les deux ; C-17 : le code brut et
  l'assemblage) ; passent ceux qui essaient un comportement que la correction ne change pas (C-14 : délibération, une
  caste ; C-15 : cas sain ; C-17 : JSON entre accents graves, gabarit aux bornes et au-delà).
- **Témoin, l'essai hérité d'origine sur la v6.2.1** : 1 échec (l'assertion `routage_sonde_accord_precoce`), 4 réussites.
- **Sous la configuration du pilote 4** (lecture) : aucune de ces corrections ne change les appels — une caste par tâche
  en génération notée (`--appels-max 160` pour les 120 tâches servies, 60 de `test` et 60 de `test_final` de la banque
  v3 : `budget_par_tache` = (160 − 6) // 120 = 1 ; en simulation, une génération fait 123 appels = 1 induction +
  2 vérifications + 120 tâches), donc aucun arbitrage (et C-14 ne change rien, même à plusieurs castes) ; aucune sonde
  sans traits (C-15) ; les mêmes mots (C-16) ; l'architecte est prié de répondre par un objet JSON, que le gabarit
  accepte comme en v6.2 (C-17 ne refuse qu'un bloc de code définissant `recompense_interne`).

Journaux : dossier `/var/tmp/essais-v621-conv-audit-v1/` de la lignée conv-audit (`v621-c.log`,
`temoin-c5-sur-3bbb78c.log`, `temoin-v53-origine-sur-v621.log`), recopiés dans les pièces du préenregistrement du pilote 4.
