# Contre-lecture du lanceur v11b de la course d'affinage (pièce de classe B, code)

- Contre-lecteur neuf, Opus 5.5, qui n'a écrit aucune des pièces relues. Hors ligne : aucun appel de modèle ni d'interface payante, aucune valeur de clé lue, aucune poussée, aucune pièce relue modifiée. Fichier écrit, non committé.
- Dépôt `/home/user/wt-organisme`, branche `lot/compte-organisme-v1`, commit `584b872e2`.
- Références lues : lanceur v10 (`origin/prep/affinage-v10-compte-organisme-v1`, `b0829025…`, différence v10 → v11b lue en entier) ; garde commune `src/controle_ia/garde_google_v3.py` de `origin/main` (`923679b5…`) ; brouillon 3 du préenregistrement v11 et son annexe « phrases du brouillon 2 qui supposent une garde du lanceur v11 » (`origin/prep/preenregistrement-affinage-v8-v1`) ; `registres/go.md` et `registres/decisions.md` d'`origin/main` (GO-2026-11-18-14, -21-71, -22-80, -22-107, -22-124 ; R-5007, R-5018, R-5042) ; relais Claude épinglé `relais_reel.py` (`1b90b020…`) ; relais Gemini v3 (`2cf6bc6d…`) ; page versée de Google sur la réflexion (`docs/sources/google-gemini-reflexion-v1/gemini-thinking-generate-content-2026-11-21-v1.md.txt`, `fe0b8d88…`, sceau tenu) ; lecture du GO par l'orchestrateur épinglé (`configuration_v55.py`, `2e6237c0…`, clone à `a41b7b50`).

## Verdict

Scellable après corrections.

Le code tient les exigences de clé, de plafonds, de GO et de garde des appels à Google, essais à l'appui ; mais le lanceur et le texte qu'il doit tenir (brouillon 3) divergent sur quatre points qui touchent la mesure ou une garde promise (constats 1 à 4), et la relecture finale du relais Claude promise par le texte manque (constat 5).

## Empreintes vérifiées (compagnon `.sha256` égal au fichier)

| pièce | empreinte |
|---|---|
| `scripts/lancer_course_affinage_mentors_v11b.py` | `a6f64e79ef1f6e480b0b64ebd04a9643d63ee1833f455bb961cd38bf329c7b1a` |
| `tests/test_lancer_course_affinage_mentors_v11b.py` | `673a20d240ecae5ac6ce8442c1a1f4e3bfcef15478efcf7c56fa7d79fe6fcc04` |
| `course-v11/configuration-course-affinage-mentors-v11b.json` | `c69620daa06a9c39b129038788ebdfd7f6530123d9726674ee14a3244f4795f2` |
| `course-v11/declaration-relais-gabarit-course-affinage-v11.json` | `b6e0968081d6554c062481858a7bba12e1e55705ff0e72101f4994e7f1674adb` |
| `course-v11/rapport-developpeur-lanceur-v11b.md` | `1393712d8dfe14fac400eea96c4e96398d3a9700729a73d0ea97c19e6294c353` |
| `course-v11/rapport-developpeur-lanceur-v11.md` | `0d8f91bdbe9480f1f337afb631ca87995670a9e1a773cda0e779e62fa58b8da5` |
| `scripts/commande_gemini_flux_v1.py` | `6aaf235df31eccd7199c0bcea1e8b68009d56d03c66a01427d05ae8137fdbf55` |
| `tests/test_commande_gemini_flux_v1.py` | `e92ff4c99d1eb54b6a49efa9b3ad9c052a780082593bf048192bc3be7be3af0f` |
| `scripts/sonde_astra_affinage_v3.py` | `32366123751ba1d1620cadf4dd4cfda039c0bf35af614a75b49e2d9c04dad7ff` |
| `scripts/sonde_astra_courses_v2.py` | `80074c82c8ea79d059c9f74b3ae89f7f50635283672a4bd26f1c2e77c27d6704` |
| `tests/test_sonde_astra_courses_v2.py` | `742f66beef23b83d8b0a5ab31495e2d343309dd15112d6f98664d36adaf6a44c` |
| `tests/test_orchestrateur_refus_relais_claude_v11.py` | `d64af76174071fde85a585054661a8467a44b4407e612e30c6b3fb0da81717a2` |

La sonde v3 n'a pas de fichier d'essais propre : elle est jouée par les essais de la sonde commune v2 (cas sain : rapport `version` = `sonde_astra_affinage_v3`).

## Essais lancés (fichiers touchés seulement ; `.venv` du dépôt de travail, `PYTHONPATH=src`, orchestrateur épinglé lu dans un clone à `a41b7b50` par `ORCHESTRATEUR_AFFINAGE_ESSAI`)

| fichier | compte |
|---|---|
| `tests/test_commande_gemini_flux_v1.py` | 27 réussis |
| `tests/test_sonde_astra_courses_v2.py` | 18 réussis |
| `tests/test_orchestrateur_refus_relais_claude_v11.py` | 3 réussis |
| `tests/test_lancer_course_affinage_mentors_v11b.py` | 274 réussis, 4 sautés (essais hérités qui cherchent l'orchestrateur aux emplacements fixes, absents de cette machine), 0 échec, 19 min 12 s |

Hors des essais, rejoués par moi sur le vrai registre de `main` : `verifier_les_go` accepte le 22 et le 25 novembre, refuse le 26 et le 15 décembre (GO-2026-11-22-107 hors période, confirmation non nommée), refuse le 16 décembre (GO-80 hors période) ; `lire_plafond` de l'orchestrateur épinglé lit « 150 USD (plafond de GO-2026-11-18-14) » à 150 USD ; pire cas calculé par le lanceur : Carbon 1,321192 USD (entrée la plus longue), Argon proposeur 0,911592, Argon juge 0,917240 sous 1,00.

## Exigences

| exigence | code | essai, cas sain | essai, artefact |
|---|---|---|---|
| Clé `RR_ANTHROPIC_API_KEY_LUC` pour tout Claude | tenue (`CLE_CLAUDE`, déclaration, configuration, Minuit et Rigaud exclues, variable absente ou faite d'espaces refusée) | oui (`test_luc_ligne_du_releve_non_lue_go_124`) | oui (Rigaud, Minuit en déclaration, en configuration, en environnement ; autre clé) |
| Part Claude plafonnée à 45 USD par le relais (`--plafond-usd 45`) | tenue : plafond lu par PID et dans l'état, égal à 45 au centime ; configuration et constante égales, sinon refus | oui | oui (150 ; plafond retiré, relevé, abaissé ; constante relevée) — voir constat 8 sur le dépassement possible du relais |
| Arrêt au premier refus : 400 à 499 sauf 429, et 402 du relais ; sans relance ni repli | tenu pendant la course (lecture toutes les 10 s, SIGTERM par PID, alerte scellée, code 5) ; **pas tenu après la fin de l'orchestrateur** (constat 5) ; arrête aussi sur des statuts propres au relais que le texte exclut (constat 7) | oui (200 et 429 n'arrêtent pas) | oui (400, 401, 402 au journal ; `refus` > 0 ; mutation « journal non lu ») |
| Plafond de la course 150 USD | tenu (configuration, ligne de GO lue à 150, porte `--plafond-ligne 150`, code 4) | oui | oui |
| Astra `gpt-6.2-astra`, 8 / 40 USD par million, `OPENAI_API_KEY_2` | tenu pour le relais de la course (modèle, prix de l'état égaux à la commande, nom de clé) ; palier de 272 000 jetons contrôlé | oui | oui (ancien modèle, prix 10 / 50, autre clé) — la clé du relais jeté de la sonde n'est pas contrôlée (constat 9) |
| Argon et Carbon sous la garde Google, 4 / 20 USD par million ; Carbon en flux | tenu : arguments épinglés exacts, corps réel capturé hors ligne devant un faux amont et passé à `verifier_reglages_google` ; commande en flux qui rejoue la garde avant l'envoi et après la réponse | oui | oui (réflexion absente, budget, niveau bas, `includeThoughts` absent, plafond trop bas, au-delà de 65 536, ancienne enveloppe d'Argon, commande par lot) |
| Plafond de session des juges 1,00 USD | tenu par la configuration épinglée (`argon_v11.plafond_session_juge_usd` = 1.0 appliqué) ; le code admet toute valeur de ]0 ; 3,00] (constat 10) | oui | oui (0,60 refusé par le pire cas d'Argon) |
| `GO_ID` = GO-2026-11-22-80 ; GO à trois chiffres lus ; refus après le 25 sans confirmation de la prolongation de GO-107 | tenu (vérifié aussi sur le vrai registre) | oui | oui (GO-80 absent, révoqué, non de Lazar, ne prolongeant pas ; confirmation absente, non inscrite, d'un autre que Lazar ; 16 décembre) |
| `PREREG_SHA256` vide : tout départ refusé | tenu (`verifier_preenregistrement`, refus nommé avant toute autre lecture) | — | oui (`test_v11_preenregistrement_non_pose_refuse`) |

## Constats

1. **Majeur — base de l'écart au devis différente du texte.** `scripts/lancer_course_affinage_mentors_v11b.py` l. 503-504 et 512 : `prop-argon` reste 0,276 et `juge-argon` 0,0347 (prix 8,3 / 41,5) ; `devis_estimation` rend **40,848 USD** pour cinq espèces (rejoué). Le brouillon 3 écrit « base de l'écart au devis : 35,683 » (Argon ramené à 4 / 20 : 0,276 × 20 / 41,5 et 0,0347 × 20 / 41,5 ; annexe, I2). L'écart au devis du manifeste de fin serait donc calculé sur une autre base que celle du texte. Correction : `prop-argon` 0,133012, `juge-argon` 0,016723 (ou les valeurs exactes du calcul du devis v11b), `DEVIS_V5_TOTAL` recalculé ; essai d'égalité au millième avec 35,683.

2. **Majeur — réglages d'Argon du lanceur différents de ceux sur lesquels le texte chiffre.** l. 400-401 et `ARGUMENTS_COMMANDES["argon"]` : provision 24 576, sortie 45 056, en flux. Le brouillon 3 (§ Espèces, « Argon ») chiffre sur provision 16 384, sortie 32 768, hors flux, et en tire : 93,36 USD si Argon réfléchit à sa provision entière, coupure des juges seulement au-delà d'environ 32 476 jetons de réflexion moyenne, « presque le plafond de sortie d'Argon lui-même : la réflexion d'Argon n'a pas de prise ». Avec une sortie de 45 056 jetons, la réflexion d'Argon peut dépasser 32 476 jetons par appel : la phrase devient fausse sous les réglages du lanceur. Le choix du développeur a une raison (à 32 768, le texte, 16 384 jetons, ne dépasse pas la limite de l'invite de 2 × 9 000 caractères que le lanceur contrôle) ; c'est donc le texte et le devis qui doivent être refaits sur 24 576 / 45 056 en flux, ou la limite de l'invite revue. Décision de la mère et de Fable ; le lanceur ne peut pas être scellé contre un texte qui chiffre d'autres réglages.

3. **Majeur — garde promise sur la ligne de LUC dans le relevé des crédits, absente.** l. 1387-1394 : pour la clé LUC, la ligne du relevé est recopiée telle quelle, sans condition. Le brouillon 3 (§ Liste d'arrêt et « Règle des clés », point 1) refuse le départ si l'entrée de LUC est absente, ne dit pas « solde non lu » avec la référence GO-2026-11-22-124, ou porte un solde. L'essai `test_v11_releve_sans_ligne_de_luc_part` (l. 2291) affirme le contraire (ligne absente : départ). Correction : exiger l'entrée, la mention et la référence, refuser tout champ de solde ; renverser l'essai et ajouter les deux artefacts (autre référence, solde présent). Ou faire changer le texte ; jamais un écart silencieux.

4. **Majeur — contre-lecture du préenregistrement : libellé du modèle.** l. 975 exige « modèle K ». Le brouillon 3 dit, pour la v11, « un Opus neuf ; modèle K en v2 à v10 », libellé encore à inscrire (emplacement 6). Tel quel, une contre-lecture conforme au texte (« Opus neuf ») serait refusée, ou il faudrait qu'elle se dise « modèle K ». Correction : fixer le libellé avec la mère, puis la constante et l'essai `test_contre_lecture_sans_modele_k_refusee`.

5. **Majeur — pas de relecture finale de l'état et du journal du relais Claude.** l. 2566-2591 : `surveillance.depasse()` n'est appelé que dans la boucle d'attente, au plus toutes les 10 s ; quand l'orchestrateur s'arrête de lui-même (par exemple A3 après trois refus consécutifs, en quelques secondes), la boucle sort sans dernière lecture. Un 400 de l'interface ou un 402 du relais écrit après la dernière lecture donne alors le code 6, sans alerte `alerte-arret-part-claude.json`. Le brouillon 3 (§ Liste d'arrêt) promet : « le lanceur relit l'état et le journal du relais à la fin : un refus (a) ou (b) y vaut le code 5 et l'alerte ». Correction : après la boucle, si `surveillance` existe et `arret_luc` est vide, un dernier `depasse()` ; essai : faux orchestrateur qui écrit un 400 au journal et sort aussitôt en code non nul → code 5, alerte.

6. **Mineur — journal du run et manifeste de fin moins complets que le texte.** `SurveillanceCleClaude.bilan` (l. 2143) ne garde que la dernière lecture. Le brouillon 3 promet un journal du run de chaque lecture (montants, comptes, statuts), le compte des appels du relais Claude par statut et le dépassement lu dans l'état (`depassement_max_usd`, `appels_au_dessus_de_la_reserve`) au manifeste de fin. Correction : écrire chaque lecture dans un fichier du run, scellé à la fin, et recopier ces champs.

7. **Mineur — déclencheurs d'arrêt plus larges que le texte.** `est_refus_interface` (l. 2087) et `refus > 0` (l. 2121) arrêtent aussi sur les refus propres au relais (401 jeton, 403 modèle non permis, 404 chemin, 413 corps), que l'annexe (D3) dit exclure ; s'y ajoutent deux arrêts que le texte ne nomme pas : part engagée au plafond, et état ou journal illisible trois fois de suite. C'est plus prudent, mais c'est un écart : l'écrire dans le texte, ou distinguer les lignes de journal qui portent un champ `motif` (refus du relais) des appels relayés. Le motif de l'alerte dit « statut 402 » pour tout `refus` > 0 : à corriger en « refus du relais ».

8. **Mineur — plafond de 45 USD tenu par réservation, non strict.** Le relais réserve 0,40 USD par appel (réserve non lue ni bornée par le lanceur, `RESERVE_APPEL_CLAUDE_USD` l. 430 inutilisée) ; un appel de proposeur peut coûter jusqu'à 3,00 USD : la dépense peut dépasser 45 USD d'au plus (coût − réserve) par appel en vol. Le texte le dit ; le lanceur devrait lire `--reserve-par-appel` par PID et l'écrire au manifeste, et la constante morte être retirée.

9. **Mineur — clé du relais jeté de la sonde d'Astra non contrôlée.** `scripts/sonde_astra_courses_v2.py` l. 121 : l'identité du relais jeté ne lit pas `--variable-cle` ; le brouillon 3 refuse une sonde « faite avec une autre variable de clé ». Correction : exiger `--variable-cle OPENAI_API_KEY_2` dans la ligne de commande lue par PID ; essai d'artefact.

10. **Mineur — plafond de session des juges non exigé égal à 1,00.** l. 905 admet toute valeur de ]0 ; 3,00]. La configuration épinglée tient 1,00, donc rien ne part autrement aujourd'hui ; mais le texte (« plafond de session des juges de la configuration autre que 1,00 USD » → refus) demande une égalité. Correction : refus si différent de 1,00.

11. **Mineur — garde Google rejouée sur la seule entrée la plus longue, et un corps de juge qui n'est pas une entrée de juge.** l. 2025 et suivantes : capture sur `plus_long` seul ; pour le rôle juge, la consigne du juge est enveloppée comme une consigne de proposeur. Les réglages contrôlés ne dépendent pas de l'entrée, d'où un risque faible ; le texte demande la plus longue et la plus courte, et une entrée de juge. Le pire cas du juge (l. 1316) suppose 1 000 caractères de cadre (SUPPOSÉ) au lieu du « cadre réel » du texte ; la marge (0,083 USD, environ 20 000 jetons d'entrée) couvre largement. Correction : deux captures et une entrée de juge bâtie comme l'orchestrateur la bâtit, ou phrase du texte ajustée.

12. **Mineur — l'hypothèse « réflexion dans la sortie maximale » n'est pas surveillée après la réponse.** `scripts/commande_gemini_flux_v1.py` l. 176-177 : si `candidatesTokenCount + thoughtsTokenCount` dépassait `maxOutputTokens`, le coût serait compté (et refusé au-delà du plafond de session, code 7), mais rien ne signale que l'hypothèse du pire cas de 1,32 USD est tombée. Correction : champ `hypothese_sortie_maximale_tenue` dans la ligne rendue, et signalement au journal.

13. **Mineur — essais de la commande en flux à d'autres réglages que la production.** `tests/test_commande_gemini_flux_v1.py` l. 27 : Carbon joué à 8,3 / 41,5 et sortie 49 152 (commentaire « réglages du lanceur v11 » périmé) ; Argon juge à 2,00 USD (l. 217). Aucun essai de la commande elle-même aux réglages de production (4 / 20, 65 536 ; juge à 1,00). La capture du lanceur couvre les réglages, pas la réponse. Correction : un cas sain par espèce aux arguments exacts de `ARGUMENTS_COMMANDES`.

14. **Mineur — précondition de lieu.** Le lanceur exige `src/controle_ia/garde_google_v3.py` dans son dépôt (pièce épinglée) et le dépôt `/home/user/controle-ia-travail` ; la branche `lot/compte-organisme-v1` ne porte pas cette garde : lancé depuis elle seule, il refuse (refus nommé, pas de repli). À dire dans les commandes exactes : le départ se fait sur un arbre qui porte la garde de `main` et la commande en flux.

15. **Rédaction.** Configuration v11b, `changements_v11.plafond_part_claude_source` : « code 7 » ; le lanceur rend 5. `PART_CLAUDE_HAUT_USD = 74.62` (l. 428) écrit au manifeste un « haut » que le brouillon 3 retire (« aucun « haut » »). `verifier_go_simplification` (l. 775) accepte toute sous-chaîne « 45 » : lecture fragile, à remplacer par la lecture du montant. En-tête du lanceur, point 7 du v11 : « Argon et Carbon déclarés à 4 / 20 » est vrai des commandes, pas du devis interne (constat 1).

## Point technique : la réflexion de Carbon est-elle comptée dans le plafond de sortie ?

- **Ce que disent le code et la garde.** La commande en flux envoie `maxOutputTokens` = 65 536 avec `thinkingLevel` « high », et calcule le pire cas `entrée gardée × 4 + 65 536 × 20` par million = **1,3212 USD** ; la garde commune contrôle `maxOutputTokens ≥ provision + 16 000`, c'est-à-dire qu'elle suppose la réflexion **dans** la sortie maximale. Le relais Gemini v3 ne touche pas `maxOutputTokens` (il ne pose que `includeThoughts`).
- **Ce que dit la documentation versée, donc vérifiable hors ligne.** La page de Google sur la réflexion, versée et scellée sur `main` (`fe0b8d88…`), l. 914-916 : `max_output_tokens` « sets the maximum number of tokens a response can generate, including thought tokens » ; l. 920-925 : coupure dure, fin `MAX_TOKENS`, « while still billing for any thinking tokens generated » ; l. 1220-1222 : « response pricing is the sum of output tokens and thinking tokens » (`thoughtsTokenCount`) ; l. 1273-1274 : « `max_output_tokens` applies to the combined total of thinking tokens and output tokens » ; l. 931 : 65 536 par requête en flux pour Carbon et Argon. Lecture : réflexion **comprise** dans le plafond, pire cas **1,32 USD** ; le 2,30 du devis (réflexion de 49 152 jetons **en plus**) est une borne prudente que la documentation versée ne soutient pas. Le rapport du développeur (§ 5) dit ce point invérifiable hors ligne : la source versée le tranche, au moins pour ce que Google écrit.
- **Ce qui n'est pas vérifiable hors ligne.** Que le service facture effectivement ainsi en flux, par ce relais (seule une course réelle, ou la facture, le montre ; les journaux versés du collisionneur, « sortie facturée 55 125 sous un plafond de 65 536 », vont dans ce sens sans le prouver) ; qu'aucun appel ne passe en `CONTINUATION` (avec `maxOutputTokens` égal au plafond par requête, la page dit que non ; la garde après réponse traiterait de toute façon `FIN_CONTINUATION` comme un défaut).
- **Ce qui protège dans les deux lectures.** La commande refuse avant l'envoi tout pire cas au-delà du plafond de session (3,00 USD) et rend le code 7 si le coût lu le dépasse ; 1,32 et 2,30 sont tous deux sous 3,00. L'écart ne touche donc que le chiffre écrit du pire cas, pas la sûreté ; le constat 12 propose de rendre visible une réponse qui contredirait l'hypothèse.

## Défauts cherchés hors de la liste, non trouvés

- Repli silencieux : aucun dans la commande en flux (tout défaut Google est un échec rendu, coût compté au pire ou à l'usage) ; un `refus` ou une dépense absents de l'état du relais Claude sont lus comme zéro (l. 2119-2121), mais l'état neuf est contrôlé au départ avec ces champs, et le relais épinglé les rend toujours.
- Gardes contournables : arguments des commandes de Google épinglés par égalité exacte, commandes à leur empreinte, garde Google chargée à son empreinte par le lanceur et par la commande ; en moteur simulé, la non-conformité Google n'est qu'écrite, ce qui est voulu (aucune dépense).
- Calculs de coût : pire cas de Carbon et d'Argon rejoués et justes ; coût lu de la commande = entrée × prix d'entrée + (sortie + réflexion) × prix de sortie, conforme à la page versée.
- Essais à vide : les essais de l'arrêt sur la part Claude jouent un faux orchestrateur qui attend le signal et vérifient la réception du SIGTERM ; une mutation « journal non lu » montre que l'essai mord.
