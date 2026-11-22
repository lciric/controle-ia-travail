# Vérification du lot 4 v2 (véhicule NA-1) — vérificateur Sonnet neuf

Verdict : **À CORRIGER** (un point bloquant : le crédit épuisé signalé en HTTP 400 n'arrête pas la course).

## Bloquant
B1. Point 4. Faux serveur sur 127.0.0.1, adaptateur direct réel (`essai_point4.py`, dans ce dossier) :
- 400 `invalid_request_error` « credit balance is too low » : classe « erreur de statut », 400, type `invalid_request_error`, non crédit ;
- 402 `billing_error` (contrôle) : « crédit d'amont » ; 429 : « erreur de statut ».
Dans `appel_garde_na_v2.py` (l. 88, 602), le n° 13 ne se lève que si la classe est dans `ERREURS_CREDIT` = (crédit d'amont, plafond du relais). Le 400 va donc à « réponse illisible, cause non établie » et la course continue : chaque appel suivant échoue de même, sans arrêt. Le n° 13 reste inatteignable sur le cas réel que Lazar a vu. La lettre (NO §2, PA A-6) dit « type d'erreur de facturation » ; l'hypothèse 402 est non vérifiée (rapport §4.7). Correction : reconnaître aussi un 400 `invalid_request_error` dont le message contient « credit balance is too low » (comparaison stricte, message non recopié au journal), et l'éprouver par un artefact 400 ; ou nœud à Lazar.
Limite : la chaîne complète n'a pas été jouée (voir N1) ; la conclusion repose sur le code d'`appel_garde` lu et l'adaptateur exécuté.

## À noter
N1. Rejeu impossible dans la liste fermée : le programme d'application exige les lots 2 v5, 3 v3, 4 v1 ; la base `a41b7b5` n'a pas `garde_motifs_na_v4`, `journal_na_v3`, `requete_na_v3`, `routage_na_v1` (ModuleNotFoundError), ni `aides_na_v4`, `aides_na_lot4_v1`. Je n'ai donc pas rejoué les 89 essais ni les 61 mutations ; je ne peux confirmer que leurs journaux (248 passés ; 61/61 tuées, témoins corrects : lus, empreintes bonnes).
N2. Point 1 : table d'empreintes, 13 fichiers OK ; 13 compagnons `.sha256` OK.
N3. Point 2 (lecture du code) conforme : repli seulement sur l'événement `refusal`, chaîne fermée rôle, premier, second ; une requête identique exigée ; trois refus = n° 1 ; servi par repli = verdict du rôle (`modele_servi_repli`, `par_repli`) ; chaque tentative consignée avec modèle demandé, servi, catégorie.
N4. Point 3 conforme à la lecture : `max_retries=0` relu avant envoi, corps à liste fermée, ni repli ni en-tête bêta, trace de repli = n° 31, coût inconnu = plafond, réponse brute conservée par tentative (refus et erreurs), catégorie absente = « catégorie non lue », réglages par (rôle, modèle), rien ajouté à l'enveloppe.
N5. Point 5 : `x-api-key` = jeton factice public `relais-local-sans-cle` (relais.py l. 14), pas la clé réelle : aucune fuite. Observé : Authorization (Bearer, même jeton factice) et x-api-key, un seul de chacun ; pas de doublon de x-api-key. Les deux en-têtes portent le même jeton : bénin.
N6. La voie du flux n'est éprouvée qu'au faux client (rapport §6.5).
