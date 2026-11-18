# Diagnostic de la sonde d'Astra, reproduit hors ligne — v1

Écrit le 18 novembre 2026 par la session du compte organisme (modèle I), sur le mot du directeur (vers 10:50Z : « je veux astra et carbon dans la course debugge »). Aucun appel réel, aucune clé, aucun réseau hors de la boucle locale.

## Verdict

La sonde d'Astra ne pouvait pas passer pour deux raisons indépendantes, toutes deux de réglage, aucune d'Astra : (1) le relais jeté, lancé sans `--reserve-par-appel`, réserve 0,40 USD par appel au-dessus de son plafond de 0,05 USD — **402 certain**, rien n'est envoyé ; (2) la commande d'Astra, sous `PLAFOND_SESSION_USD=0.05` et avec ses sorties par défaut (au moins 4 096 jetons à 50 USD le million), refuse au **code 4**. Réglages qui passent : relais `--plafond-usd 0.05 --reserve-par-appel 0.01 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 1` ; commande `PLAFOND_SESSION_USD=0.05 --max-sortie-jetons 4096 --sortie-min-jetons 16`, réduits par la commande à **768 jetons**, pire cas **0,04998 USD** (relais et commande, même formule, mêmes octets : corps de 134 octets).

## Pièces

| pièce | sha256 |
|---|---|
| `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py` (dépôt et `main`) | `67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e` |
| `docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py` (`main`) | `986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71` |
| `tests/test_sonde_astra_courses_v1.py` (essais du diagnostic) | `0ff8ba72d999d9fd97d08707b7cc9fe91b9ce7a17bf9b42918e2f76c8189fefd` |

## Règle lue dans le relais épinglé

`_relayer` (l. 707-714) : `reserve = max(compteur.reserve_min, bareme.pire_cas(longueur, demande))`, puis `compteur.admettre(reserve)` refuse en 402 si `depense + engage + reserve > plafond + 1e-12`. `RESERVE_PAR_APPEL_DEFAUT = 0.40`. `Bareme.pire_cas` = ((octets du corps + 1 024) × prix d'entrée + `max_completion_tokens` × prix de sortie) / 10⁶ — la formule de `max_tokens_permis` de la commande.

## Reproduction (relais factice = code du relais épinglé)

Le relais factice des essais n'est pas une recopie : `Compteur`, `Bareme` et le gestionnaire de `fabriquer_gestionnaire` sont importés du fichier épinglé (empreinte vérifiée à l'import) et servis dans le processus de l'essai, avec une clé factice, devant un faux amont local au format de flux OpenAI. L'égalité de la règle est donc de construction.

| cas | résultat |
|---|---|
| relais à réserve par défaut (0,40), plafond 0,05 ; commande réglée comme la sonde v2 | commande code 3, `HTTP 402`, `envoye` faux ; amont : 0 requête ; relais : 0 appel, 1 refus |
| commande sous `PLAFOND_SESSION_USD=0.05`, sorties par défaut | code 4 (« pire cas au-dessus du plafond »), rien envoyé |
| commande sans `PLAFOND_SESSION_USD` | code 2 |
| relais `--reserve-par-appel 0.01`, commande `--max-sortie-jetons 4096 --sortie-min-jetons 16` | code 0 ; 768 jetons demandés à l'amont ; pire cas commande = pire cas relais = 0,04998 ≤ 0,05 ; dépense ≤ 0,05 même si l'amont facture tout le maximum |

Essais : `test_diagnostic_relais_jete_sans_reserve_reglee_refuse_en_402`, `test_diagnostic_commande_code_4_sous_le_plafond_par_defaut`, `test_configuration_qui_passe_pire_cas_sous_005` (deux cas).

## Ce qui était déjà juste

La sonde v2 de l'affinage (`scripts/sonde_astra_affinage_v2.py`, `17994492…`) et le § 5 des commandes de l'affinage v6 portaient déjà ces réglages (R-3279). Il leur manquait le contrôle du relais jeté avant l'appel ; les commandes de l'auto-conception v2 ne donnaient aucun réglage de sonde. Correction : `scripts/sonde_astra_courses_v1.py`, commune aux deux courses ; commandes `course-v2/commandes-exactes-course-auto-conception-v2b.md` et `course-v6/commandes-exactes-course-affinage-v6b.md`.

## Hypothèse non éprouvée

768 jetons de sortie (raisonnement compris) suffisent à une réponse triviale d'Astra : SUPPOSÉ, non mesuré. Une troncature rend « sonde non réussie » (code 5 de la commande), qui se lit comme telle : Astra non déclarée, tentative non brûlée.
