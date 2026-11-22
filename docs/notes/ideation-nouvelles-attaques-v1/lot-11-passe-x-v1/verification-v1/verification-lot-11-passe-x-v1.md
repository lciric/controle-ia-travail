# Vérification neuve du lot 11 « passe X » (NA-1) — v1

Vérificateur neuf (R2). Aucune requête réseau, aucune clé lue, aucune dépense. Rejeu : `pytest` = 40 passés ; mutations : 21 tuées, T0 survit, `conforme: true`. Empreintes : `garde_google_v3.py` = son compagnon (923679b5…) ; pièce fusionnée = 39fb4e93… (égale à `EMPREINTE_PIECE`). Mes essais : `/tmp/claude-0/-home-user-controle-ia-travail/e2c3ce0b-40f3-55d3-a6bf-333c05f6ccd1/scratchpad/v_artefacts_x.py` (13 essais : 4 passent, 9 échouent ; sur les 9, 7 révèlent un vrai trou et 2 étaient mal réglés de ma part ou sont des réserves).

## Verdict : À CORRIGER

Les 40 essais et les 21 mutations tiennent, mais quatre trous touchent directement les garanties demandées (aucun texte au journal, coût compté au pire, « toutes les clés prêtes », fin propre d'une tentative). Corrections courtes, toutes dans `passe_x_na_v1.py`. Aucun défaut sur l'arrêt n° 12 en parallèle, sur l'arrêt n° 13 pour une tentative neuve, ni sur le repli (limité au refus de classifieur d'une chaîne Claude).

## Points bloquants

**B1. G4 n'est pas liée à la configuration.** `main` exécute la garde de départ sur le plan donné (`--plan-garde`) et ne contrôle que `tout_pret` de ce plan ; rien ne vérifie que chaque couple (clé, modèle) des chaînes de la configuration y figure et est « prêt ». Artefact V3 : plan à une seule clé (CLE_LUC) avec les quatre clés en configuration : `main` rend 0 et **4 requêtes partent**, dont celles de clés jamais éprouvées. Correction : avant `courir`, exiger que {(cle_var, modèle) de toutes les chaînes} soit inclus dans les lignes du plan, chacune « prêt » ; sinon `Refus("G4 : couple non éprouvé")`. Ajouter un essai (plan partiel : refus ; plan complet : départ).

**B2. Coût de Google sous le pire sur un flux coupé proprement ou avec événement d'erreur (A3).** Google envoie `usageMetadata` à chaque fragment ; `cout` lit le dernier cumul vu. Artefact V1 (fragment avec usage, puis `{"error": …}` en statut 200) : classe « erreur de requête », coût 0,028220 contre pire 1,396372, `cout_inconnu` faux. V1b (flux fermé proprement après un fragment, sans `finishReason`) : 0,0282 au lieu du pire. Le sous-compte vide la garde n° 12. Correction : dans `tentative`, si `statut == 200` et (`r["erreur"]` ou `r["fin"] is None`), compter `p_t` avec `inconnu=True`. Essais : les deux cas V1 et V1b. (Anthropic et OpenAI tombent déjà au pire car leur usage final manque ; seul Google, et Kimi si son usage vient par fragment, est touché.)

**B3. Du texte du fournisseur sort au journal : `fin` et `modele_servi` sont écrits tels quels** (V2 : un `finish_reason` et un `model` valant « TEXTE-SECRET-FIN » apparaissent dans `j.jsonl`). Le LISEZMOI (écart 2) dit « liste fermée des raisons d'arrêt » : le code ne la fait pas. Correction : écrire `fin` seulement s'il est dans une liste fermée (end_turn, stop, refusal, max_tokens, pause_turn, tool_use, stop_sequence, length, content_filter, STOP, MAX_TOKENS, SAFETY, RECITATION, …), sinon `"autre"` ; écrire `modele_servi` seulement s'il est égal au modèle demandé ou à `demandé-<suffixe de [A-Za-z0-9._-]{1,40}>`, sinon `"autre"` (la quarantaine garde le brut). Essai : l'artefact V2.

**B4. Une coupure réelle du flux fait tomber la tentative sans ligne ni compagnon.** `http.client.IncompleteRead` (et `HTTPException`, non `OSError`) n'est pas attrapée : V4 (serveur local qui annonce un morceau de 255 octets et ferme) : l'exception sort de `tentative`, aucune ligne au journal, pas de `.sha256` pour le flux brut, la chaîne s'interrompt (en parallèle : le fil meurt avec trace sur la sortie d'erreur). Le coût est bien compté au pire (par défaut de `c`), mais l'attestation manque. Correction : `except (OSError, TimeoutError, ValueError, http.client.HTTPException)` ; en filet, un `except Exception` qui classe « injoignable » avec le seul nom de l'exception ; la fin (compagnon + ligne) doit toujours s'exécuter. Essai : l'artefact V4.

## Réserves (à corriger si possible avant le lancement, sinon à consigner)

R1. **Crédit non reconnu hors de la forme `{"error": {…}}`.** V6 : statut 429 avec `{"error": "insufficient balance…"}` ou 403 avec `{"message": "credit balance is too low"}` : classé « erreur de requête », n° 13 non levé. La garde de départ, elle, cherche le motif dans le corps brut. Correction : sur statut ≠ 200, appliquer `MOTIFS_CREDIT` au corps brut lu en mémoire (non gardé hors quarantaine) ; ajouter à `MOTIFS_CREDIT` « depleted|prepayment » pour Google. Aussi : `r["credit"]` est réécrit par un événement d'erreur ultérieur ; utiliser `or`.
R2. **Modèle substitué : égalité par préfixe `m + "-"`.** V7 : demandé `gpt-6-astra`, servi `gpt-6-astra-mini` : « réponse rendue ». Exiger un suffixe de date (`-\d{4}-?\d{2}-?\d{2}` ou jeton court numérique) ou la liste des modèles servis admis en configuration. Même défaut dans la garde de départ v2 (n° 31). À l'inverse, un flux Google sans `modelVersion` est classé « modèle substitué » (sûr mais gaspille la réponse) : à relire sur l'essai réel.
R3. **Journalisation avant envoi absente (P6, V9 l. 77).** Le journal n'est écrit qu'à la fin de la tentative : un arrêt brutal (kill, coupure de la machine) perd réservation, cumul et empreinte de la requête ; la reprise est refusée (« on n'écrase jamais »), donc pas de double dépense, mais le cumul réel est perdu. Écrire une ligne « envoi » (empreinte de la requête assemblée, rang, modèle demandé, pire réservé) avant `transport`. Écart non déclaré.
R4. **G4 : fichier `…garde-depart.jsonl`.** `GD.executer` lève `FileExistsError` après avoir envoyé ses essais si ce fichier existe ; `main` ne contrôle que `journal`. Contrôler son absence avant. Il n'y a pas non plus de contrôle de la quarantaine « hors du dépôt » (LISEZMOI, écart 4) : le code accepte tout chemin ; ajouter un refus si `realpath` est sous le dépôt de travail ou sous `main-lecture`.
R5. **Réservation au pire calculé, non à 6,05 (P4 : « non baissé »).** `_reserver` réserve `pire(maillon)` (ex. ≈ 2,4 USD pour un maillon 5/25 à 96 000) ; V8 (huit proposeurs, une clé à 13,00 USD, tous en parallèle, barrière) : 5 envois, total ≤ 13,00 : l'arrêt n° 12 tient sous concurrence. Mais les sous-parts du devis (72,60 = 12 × 6,05) supposent 6,05 fixe ; le texte de P4 dit « non baissé » : écart non déclaré, sans risque tant que les tarifs de la configuration sont justes. Aussi `cout` borne le coût réel à `pire_t` (`min`) : un dépassement réel serait masqué ; journaliser le coût déclaré brut en plus.
R6. **Arrêt n° 13 : fenêtre de course.** Le drapeau est lu avant `_reserver`, non sous le verrou ; une tentative qui a passé la lecture juste avant le `set` part quand même. Relire le drapeau dans `_reserver`. Les tentatives déjà en vol ne sont pas interrompues (inévitable, à dire).
R7. **Redirections HTTP.** `urlopen` suit les redirections en renvoyant les en-têtes (clé comprise) ; installer un gestionnaire qui refuse toute redirection. Aucun `User-Agent` fixé (« Python-urllib ») : certains frontaux bloquent ; à garder si l'essai de la garde de départ a déjà passé.
R8. **Kimi : usage en flux.** Le code lit `usage` au niveau du fragment ; si Moonshot le met dans `choices[0].usage`, le coût tombera au pire (sûr, mais gonfle le cumul de CLE_K). À confirmer sur l'essai réel ; accepter les deux emplacements.
R9. **Maillons Claude de repli.** `sortie_max` est libre par maillon : vérifier au scellement de la configuration que 96 000 est admis par Opus 4.6 et Sonnet 4.6 (une erreur 400 coûte zéro mais perd le repli) ; la chaîne `ajout_opus46` du devis (`opus46, opus46, sonnet46`) doit être écrite avec le saut (`SAUT`), le code ne le force pas.
R10. Exceptions non `Refus` avant tout envoi (`D(str(v))` sur une sous-part mal formée, `KeyError` sur `google`) : plantent proprement avant l'envoi, mais sans le message « REFUS ». Cosmétique.

## Gardes G1 à G12 : tenues ou non, et preuve

| garde | tenue par le code | preuve (sain / artefact) |
|---|---|---|
| G1 | oui (empreinte, motifs ligne à ligne) | oui / oui (octet changé, motifs forcés) |
| G2 | oui | oui / oui (8 artefacts, empreinte altérée) |
| G3 | oui (préfixe exact `| GO-… |`) | oui / oui |
| G4 | **non, voir B1** | essai prouve seulement le cas « manque » du plan |
| G5 | oui | oui / oui |
| G6 | oui (avant : à l'init, corps recalculé identique ; après : défaut) | oui / oui (96 000, niveau bas ; 4 défauts) ; zéro pensée et pensée absente : V9 confirme « défaut Google » |
| G7 | oui, atomique sous verrou ; V8 : huit fils, une clé : tient | oui / oui (mais aucun essai à huit fils ; V8 le comble) |
| G8 | oui pour une tentative neuve (réserve R6) ; crédit dans un flux 200 : V5 levé ; crédit hors forme : R1 | oui / oui |
| G9 | oui (seul « refus du modèle (classifieur) » d'un fournisseur anthropic, jamais sur erreur) | oui / oui |
| G10 | flux brut + compagnon : oui ; texte absent du journal : **non, B3** (fin, modèle) ; quarantaine hors dépôt : non contrôlée (R4) | partiel |
| G11 | clés par nom, jamais affichées ; message d'erreur non gardé : oui ; clé jamais dans l'URL (Google en en-tête) | oui |
| G12 | oui avec la réserve R2 | oui / oui |

Réponses aux questions posées : texte au journal/rendu/sortie : seulement par `fin` et `modele_servi` (B3) ; fragment de clé : non (message jamais gardé ; l'exception n'est journalisée que par son nom) ; n° 12 en parallèle : tient (V8) ; n° 13 : tient (R6) ; repli hors refus de classifieur : non ; erreur au milieu du flux : comptée au pire sauf Google (B2) ; Google à zéro jeton de pensée ou champ absent : refusé (« défaut Google ») ; statut 200 avec événement d'erreur : classé « erreur de requête » ou « crédit épuisé » (V5, V5b), n° 13 levé, coût au pire sauf Google (B2). Corps de requête : conformes (Anthropic Messages `stream:true` avec `max_tokens` ; OpenAI `max_completion_tokens` + `stream_options.include_usage` ; Kimi `max_tokens` + `stream_options` ; Google `streamGenerateContent?alt=sse`, clé en `x-goog-api-key`, `thinkingLevel` + `includeThoughts`, `maxOutputTokens`).

## Concordance avec X-1 à X-11, P1 à P17, A1 à A7

Tenus : X-2 (pièce seule, sans champ système, à l'octet), X-3/X-4 (empreinte, motifs), X-5 en partie (flux brut tel quel, avec compagnon ; trie après la troisième génération hors code), X-6 à X-8 (aucune lecture de réponse), X-9 (repli attribué au modèle servi, `par_repli`), X-10/X-11 (P_X = 96,80, n° 12 et 13), P1, P2, P3 (seul le refus de classifieur est rejoué), A1 (aucune relance), A2 (modèle servi comparé), A3 (sauf B2), A4, A6, A7.
Écarts déclarés au LISEZMOI : (1) Google 65 536 au lieu de 96 000 (la garde v3 refuse 96 000 : constaté) ; (2) transport propre ; (3) configuration à sceller ; (4) quarantaine stricte.
Écarts **non déclarés** : (a) huit proposeurs (devis v3) là où X-1 et X-10 disent cinq, P_X ≥ 54,45 : le montant 96,80 vient des GO 46/48/54, à faire dire dans le LISEZMOI ; (b) classes « erreur de requête » et « injoignable » là où A6/P-intro disent « réponse illisible, sous-compte cause non établie » (simple correspondance de noms à écrire) ; (c) P6 : pas de ligne « envoi » avant l'envoi (R3) ; (d) P4 « non baissé » (R5) ; (e) A5 : la catégorie du refus n'est pas lue dans le flux (reste dans la quarantaine) ; (f) aucun essai de A-6 pour une erreur d'accès (401/403) qui ne lève pas le n° 13 : à ajouter (le code le tient pour les formes testées ; attention à « suspended » et « billing » du motif, qui arrêtent la passe par prudence).

## Artefacts écrits par moi (hors essais du lot)

| essai | ce qu'il éprouve | issue |
|---|---|---|
| V1, V1b | Google : usage partiel puis erreur / flux coupé proprement | **tombent** (B2) |
| V2 | `finish_reason` et `model` portant un texte | **tombe** (B3) |
| V3 | plan de garde de départ partiel | **tombe** (B1) |
| V4 | serveur local, coupure chunked | **tombe** (B4) |
| V5, V5b | crédit dans un flux 200 ; erreur au milieu d'un flux Anthropic (pire, pas de repli) | passent |
| V6 | crédit hors forme (429/403) | **tombent** (R1) |
| V7 | `gpt-6-astra-mini` servi | **tombe** (R2) |
| V8 | huit fils, une clé, budget serré | passe (5 envois, ≤ 13,00) |
| V9 | Google sans `thoughtsTokenCount` | passe (« défaut Google ») |
