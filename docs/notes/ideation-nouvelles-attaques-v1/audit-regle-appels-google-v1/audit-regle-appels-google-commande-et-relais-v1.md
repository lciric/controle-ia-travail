# Audit de la règle « Appels aux modèles de Google » — commande d'appel v6 et relais Google local (port 8805) — v1

- **Nature** : audit hostile, en lecture seule, par un auditeur neuf qui n'a écrit aucun des codes lus. Aucun code exécuté, aucun appel, aucune clé lue, aucune dépense, aucune écriture hors du dossier de l'auditeur. 21 novembre 2026. Classe C (pièce de travail).
- **Règle appliquée** : `CLAUDE.md` sur `origin/main`, section « Appels aux modèles de Google » (GO-2026-11-21-71), lue par `git show origin/main:CLAUDE.md`. Numérotation reprise de l'audit précédent (`docs/notes/ideation-nouvelles-attaques-v1/audit-regle-appels-google-v1/audit-regle-appels-google-orchestrateur-v56-lots-na-v1.md`) : **E1** réflexion explicite dans le corps (niveau le plus haut admis ou budget prévu) ; **E2** plafond de sortie ≥ réflexion + 16 000 jetons de texte ; **E3** limite de mots de l'invite tenue dans le plafond de texte ; **E4** après réponse : zéro jeton de pensée, fin en MAX_TOKENS, SAFETY, RECITATION ou texte vide = défaut journalisé, jamais une réponse ; **E5** garde commune de `src/controle_ia/` employée, ou reproduite avec essais et mutations.
- **Périmètre** : la commande d'appel v6 et le relais 8805, que l'audit précédent n'a pas lus ; et, parce que le relais ne construit pas lui-même le corps, la fonction du collisionneur v7 qu'il charge et qui l'écrit.
- **Limite dite** : mon mandat ne m'ouvre que `docs/notes/`, `scripts/` et mon dossier. Je n'ai pas vérifié l'absence d'une garde commune sous `src/controle_ia/` (fait reçu de l'audit précédent, point « Fait reçu »).

## 1. Pièces lues et empreintes

| pièce | empreinte calculée (`sha256sum`) | compagnon `.sha256` |
|---|---|---|
| `docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_argon_v56_nuit_v6.py` | `5eae1a0468430e243c3c4e099b3969f949f62add688531aafdd7f0f44e036e55` | identique ; identique à la valeur `5eae1a04…6e55` citée par l'audit précédent et par `configuration-boucle-reelle-v8.json` l. 327-330 |
| copies `docs/notes/organisme-boucle-reelle-v1/code-v66/configuration-v6/commandes-v6/…_v6.py`, `…/ecart-1-sortie-proposeur-v1/configuration-v7/commandes-v6/…_v6.py`, `…/configuration-v8/commandes-v6/…_v6.py` | `5eae1a04…6e55` (les trois) | — |
| `docs/notes/organisme-boucle-reelle-v1/collisionneur-v7/collisionneur_v7.py` | `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc` | présent ; égal à `SHA_COLLISIONNEUR` de la commande v6 (l. 233), exigé par `charger_collisionneur` (l. 250-258) |
| `commande_argon_v56_nuit_v5.py`, `_v4.py`, `_v3.py` (même dossier que la v6) | `0b52aba8…6a52`, `5c6d5149…4081`, `95fa4064…af73` | identiques |
| `docs/notes/organisme-boucle-reelle-v1/ecart-1-sortie-proposeur-v1/configuration-v8/configuration-boucle-reelle-v8.json` | non recalculée (lue l. 266-337) | présent |
| `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-v2.md` | non recalculée (lue l. 690-730) | — |

## 2. Recherche du relais Google et du relais en service

Recherches faites (contenu) : `generativelanguage|generateContent|thinkingConfig|thinkingBudget|thinkingLevel|maxOutputTokens|finishReason|thoughtsTokenCount` sur `docs/notes/` (169 fichiers, dont beaucoup de textes et de relevés JSON) et `scripts/` (14 fichiers) ; `8805` sur `scripts/` (zéro) et, restreint aux `*.py, *.sh, *.json` avec `:8805|port 8805|--port 8805|"8805"`, sur `docs/notes/` (24 fichiers) ; `servir --port 8805` sur `docs/notes/` (toutes extensions de texte) ; par nom, `**/commande_argon_v56_nuit_v*.py` et `**/collisionneur_v7*.py` sur tout le dépôt.

Fichiers trouvés qui servent ou peuvent servir de relais Google local :

| fichier | rôle | relais 8805 ? |
|---|---|---|
| `commande_argon_v56_nuit_v6.py`, sous-commande `servir` (l. 247-404) | relais HTTP local `POST /appel` sur `127.0.0.1` ; appelle `collisionneur_v7.appeler_gemini(…, attentes=(0,))` (l. 376) | **oui, en service selon le texte de course** (ci-dessous) |
| `commande_argon_v56_nuit_v2.py` | relais 8805 d'origine, selon l'en-tête de la v6 (l. 33-34, 75-76, 199-200) | **absent du disque** : `Glob **/commande_argon_v56_nuit_v*.py` sur tout le dépôt ne rend que v3 à v6 (et les trois copies de la v6) ; `git log origin/main` sur `docs/notes/**` et `scripts/**` pour ce nom : rien. Empreinte citée par la v3 (l. 129) : `221df610…`, invérifiable ici (R11 : cherché sur disque et dans l'historique de `origin/main`) |
| `commande_argon_v56_nuit_v3.py` à `_v5.py`, `servir` | même bloc, dit identique octet pour octet hors `VERSION` | non désignés par le texte de course |
| `docs/notes/ideation-organisme-v1/lancement-v2/relais_gemini_v1.py`, `…/argon-recherche-v1/relais_gemini_v2.py` | mandataires de transit vers l'interface de Google | **non** : port d'usage 8788 (l. 36 et l. 51 respectivement), autre protocole |
| `collisionneur_v7.py`, `appeler_gemini` (l. 423-449) | **construit et envoie le corps réel** à l'interface de Google | n'est pas un relais ; chargé par le relais 8805 |

**Preuve du relais en service.** La configuration de course `configuration-boucle-reelle-v8.json` (l. 266-299) fait lancer par l'orchestrateur `commandes-v6/commande_argon_v56_nuit_v6.py appeler --url-relais http://127.0.0.1:8805 --modele <modèle de Google> … --max-sortie-proposeur 32000 --max-sortie-court 4000 --sortie-min-jetons 1000 --max-sortie-lecteur 1000 --sortie-min-jetons-lecteur 200`, avec l'empreinte `5eae1a04…6e55` (l. 327-330). Le préenregistrement v2 de la boucle réelle, § 12.3 (`preenregistrement-boucle-reelle-organisme-v1-v2.md` l. 691 et 711-713), désigne le relais : `python3 -I -B commandes-v6/commande_argon_v56_nuit_v6.py servir --port 8805 --plafond-usd 7 --max-appels 39 --journal JOURNAL_ARGON --collisionneur CHEMIN_DU_COLLISIONNEUR_V7 --sha-collisionneur c9725f02…98dc` ; même ligne dans `course-v67/consigne-poste-local-course-v67-v4.md` l. 78. **Divergence** : l'en-tête de la v6 dit que « le relais 8805 reste servi depuis `commande_argon_v56_nuit_v2.py` » (l. 33-34) ; le texte de course dit la v6. Les deux mènent au même appelant (`appeler_gemini` du collisionneur v7 à `c9725f02…`, exigé dans la v3 à la v6, l. 105, 157, 201, 233), si le bloc `servir` de la v2 est bien identique comme l'en-tête l'affirme (non vérifiable : v2 absente). Je n'ai trouvé aucun relevé qui dise quel fichier a réellement tenu le port 8805 dans une course passée.

## 3. Chemin d'appel : un seul, en trois maillons

Orchestrateur → **M1** commande `appeler` (processus lancé par appel) → HTTP local → **M2** relais `servir` (port 8805, tient la clé) → **M3** `collisionneur_v7.appeler_gemini` → interface de Google ; puis retour M3 → M2 → M1 → orchestrateur.

| maillon, fichier et lignes | ce que fait le code |
|---|---|
| M1 `commande_argon_v56_nuit_v6.py` l. 433-441 (`bornes_de_sortie`), l. 492-501 | choisit (maxi, mini) par rôle : proposeur 32 000/1 000 ; juge et expérimentateur 4 000/1 000 ; vérificateur 1 000/200 (défauts l. 590-594, mêmes valeurs dans la configuration v8). Puis `mt = min(maxi, int((PLAFOND_SESSION_USD − coût d'entrée) × 1e6 / 50))` (l. 494) : **le plafond est abaissé à ce que la session paie**, refus seulement sous `mini` (l. 495-497) |
| M1 l. 526-527 | corps vers le relais : `{"modele", "prompt", "max_tokens": mt, "pire_cas_usd"}` ; aucun champ de réflexion |
| M2 l. 314-347 | lit ce corps, vérifie consigne non vide, `max_tokens > 0`, modèle permis, plafond et nombre d'appels ; appelle `appelant(modele, prompt, mt)` ; aucun autre réglage |
| M3 `collisionneur_v7.py` l. 427-429 | **corps réel envoyé à Google** : `{"contents": [{"role": "user", "parts": [{"text": prompt}]}], "generationConfig": {"maxOutputTokens": max_tokens}}` vers `…/v1beta/models/{modele}:generateContent` |
| M3 l. 452-467 (`lire_reponse_gemini`) | `usage.sortie = candidatesTokenCount + thoughtsTokenCount` (l. 455) : **le compte des pensées est fondu dans la sortie et perdu** ; `promptFeedback.blockReason` → fin `BLOCAGE_PROMPT` ; pas de candidat → `AUCUN_CANDIDAT` ; texte = parties non `thought` ; fin = `finishReason` |
| M3 l. 527-557 (`statut_reponse`) | fin ∈ {SAFETY, PROHIBITED_CONTENT, BLOCKLIST, SPII, RECITATION, IMAGE_SAFETY, BLOCAGE_PROMPT} → `REFUS` ; `MAX_TOKENS` → `TRONQUE` si texte, `VIDE` sinon ; `STOP` → `OK` si texte, `VIDE` sinon ; `AUCUN_CANDIDAT` → `VIDE` ; toute autre fin → `ANOMALIE` |
| M2 l. 351-363 | rend au client `{texte, modele_servi, fin, statut, usage, cout_usd, …}` ; journal JSON par ligne (l. 355-359) : `statut`, `fin`, `usage` (fondu), jamais le texte |
| M1 l. 546-570 | `echec` → code 3 ; modèle servi ≠ demandé → 5 ; `REFUS` → 5 (`refus: true`) ; **`TRONQUE` pour `experimentateur_test` ou `lecteur_test` à l'usage lu → code 0 avec le texte, `coupee: true`** (l. 563-564, changement 1 de la v6) ; `TRONQUE`, `VIDE`, `ANOMALIE` sinon → 5 ; usage absent → 5 ; sinon 0. Chaque fin est consignée au registre de dépense (`reg.regler`, l. 513-514) avec son statut |

## 4. Les cinq exigences, par maillon

Légende : T tenue ; NT non tenue ; SO sans objet ; ND non déterminable dans le périmètre.

| maillon | E1 réflexion dans le corps | E2 plafond ≥ réflexion + 16 000 | E3 limite de mots ≤ plafond de texte | E4 défauts après réponse | E5 garde commune |
|---|---|---|---|---|---|
| M1 commande `appeler` | **NT** : aucun champ de réflexion dans le corps transmis (l. 526), aucune option de réflexion (l. 587-597) | **NT** : aucun plancher à 16 000 ; vérificateur 1 000, juge et expérimentateur 4 000 (< 16 000 quel que soit le budget de réflexion) ; proposeur 32 000 au plus, mais abaissé au budget de session jusqu'à 1 000 (l. 494-497) ; aucun budget de réflexion connu, donc aucune somme vérifiable | **NT** : la consigne n'est mesurée qu'en caractères pour le coût (l. 493, 498) ; aucune lecture d'une limite de mots | **NT partiel** : SAFETY et RECITATION (via `REFUS`) → code 5, T ; texte vide (`VIDE`) → 5, T ; MAX_TOKENS → 5 pour proposeur et juge, T, mais **→ code 0, réponse rendue, pour `experimentateur_test` et `lecteur_test`** (l. 563-564), NT ; et la commande accepte même un `TRONQUE` à texte vide en code 0 (essai `test_reponse_coupee_vide_ou_sans_usage`, `test_commandes_tour_ferme_v6.py` l. 1381-1387), faille latente que seul M3 ferme en classant ce cas `VIDE` ; **zéro pensée : NT**, jamais lu | **NT** : n'importe que la bibliothèque standard et le registre (l. 207-226) ; aucune reproduction ; essais et mutations v6 : zéro occurrence de `thinking|thoughts|reflexion|réflexion|pensee|pensée|RECITATION|SAFETY|limite de mots` (`grep -c`, § 6 pas 9) |
| M2 relais `servir` | **NT** : transmet `max_tokens` seul à l'appelant (l. 347) ; ne pose ni n'exige de réflexion | **NT** : accepte tout `max_tokens > 0` (l. 325) | **NT** : aucune vérification | **NT** pour le zéro pensée (il ne reçoit que l'usage fondu, l. 455 de M3 ; son journal ne peut pas montrer le défaut) ; pour les fins et le vide, il rend un `statut` exact et le journalise, la décision étant prise par M1 : T pour le journal | **NT** |
| M3 `appeler_gemini`, `lire_reponse_gemini`, `statut_reponse` | **NT** : `generationConfig` ne porte que `maxOutputTokens` (l. 428) ; la réflexion est laissée au défaut du modèle | **NT** : `maxOutputTokens` = `mt` reçu, sans contrôle ; si la réflexion se compte dans `maxOutputTokens` (supposé, d'après la documentation de l'interface de Google, non relue ici ; cohérent avec le pire cas qui compte `max_tokens` au prix de sortie, l. 568-569), un plafond de 1 000 ou 4 000 laisse la réflexion par défaut consommer tout ou partie du texte | **NT** | classement des fins : T pour SAFETY, RECITATION, MAX_TOKENS, vide (l. 527-557) ; **NT pour le zéro pensée** : `thoughtsTokenCount` additionné à `candidatesTokenCount` (l. 455), jamais lu seul, `types_blocs` non transmis | **NT** |
| configuration v8 l. 286-296 | NT (aucun argument de réflexion) | **NT** : 4 000 et 1 000 transmis ; 32 000 sans plancher | NT | SO | NT |

**Lecture d'ensemble.** Sur le seul chemin réel vers Google, E1, E2, E3 et E5 ne sont tenues à aucun maillon ; E4 est tenue pour SAFETY, RECITATION et le texte vide, tenue pour MAX_TOKENS au proposeur et au juge, **non tenue pour MAX_TOKENS au vérificateur et à l'expérimentateur de l'étage de tests (réponse coupée rendue en code 0, par choix de la v6)**, et non tenue pour le zéro jeton de pensée à tous les maillons (l'information est détruite en M3). Le constat qui a fait naître la règle (« envoyé sans réglage de réflexion : zéro jeton de pensée sur 22 réponses ») est exactement ce que M3 l. 427-428 et l. 455 produisent et cachent.

## 5. Origine des écarts selon les versions (v3 à v6)

- Corps sans réflexion, plafond abaissé au budget, aucun contrôle de mots : présents à l'identique en v3 (`mt` l. 339, corps l. 369), v4 (l. 414, 446), v5 (l. 458, 490) ; le corps réel vient du collisionneur v7, épinglé à la même empreinte `c9725f02…` de la v3 à la v6. **Antérieurs à la v3** (hérités de la v2 et du collisionneur v7).
- Bornes par rôle 4 000 et 1 000 (`bornes_de_sortie`) : **introduites en v3** (en-tête v3, point 2 ; l. 296 de la v3).
- Réponse coupée rendue en code 0 pour les rôles de l'étage de tests : **introduite en v6** (`diff-argon-v5-v6.patch` l. 100-101 ; en-tête v6 point 1). Les v3 à v5 rendaient code 5 (l. 405, 483, 527).

## 6. Corrections proposées, en lot neuf (R12 : fichiers neufs ; rien n'est écrit ici)

**Commun, `src/controle_ia/` (préalable)** : la garde commune nommée par la règle (avant envoi : réflexion explicite, plafond ≥ réflexion + 16 000, limite de mots de l'invite ≤ plafond de texte ; après réponse : pensée nulle, fin MAX_TOKENS/SAFETY/RECITATION, texte vide → défaut nommé) ; table R5 (un cas sain, un artefact par refus) et une mutation qui tue chaque exigence. Si elle existe déjà (non vérifié ici), les fichiers ci-dessous l'importent.

**`collisionneur_v8_…` ou un module d'appel neuf, par exemple `appel_google_v1.py` (au lieu de toucher `collisionneur_v7.py`, gelé et épinglé)** :
- corps : `generationConfig.thinkingConfig` explicite (niveau le plus haut admis ou budget prévu, valeur reçue en argument, jamais par défaut) ; `maxOutputTokens` = budget de réflexion + texte, refus si texte < 16 000 ;
- appel de la garde commune sur le corps exact avant `urlopen` ;
- lecture : garder `thoughtsTokenCount` à part (`usage.pensee`), à côté de la somme qui sert au coût ; rendre `types_blocs` ;
- statut : pensée nulle ou absente → défaut nommé ; MAX_TOKENS → défaut quel que soit le texte.

**`commande_argon_v56_nuit_v7.py` (neuf, au-dessus de la v6)** :
- `appeler` : options obligatoires de réflexion et de plafond de texte par rôle ; refus avant envoi (code 2 ou 4, `cause_refus` neuve) si plafond de texte < 16 000 ou si le budget de session ne paie pas réflexion + 16 000 — **refus au lieu de l'abaissement de `mt`** (l. 494) ;
- limite de mots de l'invite : lue par programme dans la consigne servie (ou passée par l'orchestrateur), comparée au plafond de texte ; refus sinon ;
- corps vers le relais : porter la réflexion et le plafond de texte ;
- réponse : retirer `ROLES_COUPEE_ADMISE` (l. 413, 563-564) ou le réduire à un défaut journalisé lu « non concluant » par l'étage, jamais un texte rendu en code 0 ; refuser tout `TRONQUE` à texte vide ; refuser pensée nulle ; écho dans la dernière ligne de `reflexion_demandee`, `plafond_sortie`, `jetons_pensee`, `jetons_texte`, `raison_fin` (demande de l'audit précédent, § 3) ;
- `servir` : charger le module d'appel neuf (empreinte épinglée), exiger dans `POST /appel` les champs de réflexion et de plafond, appeler la garde commune, journaliser `jetons_pensee` et le défaut ;
- essais et mutations neufs (`test_commandes_tour_ferme_v7.py`, `mutations_commandes_tour_ferme_v7.py`) : un cas sain et un artefact par exigence ; mutations qui retirent `thinkingConfig`, rétablissent l'abaissement de `mt`, rétablissent le code 0 coupé, fondent de nouveau les pensées dans la sortie — chacune doit faire échouer la suite ;
- en-tête : corriger la phrase « le relais 8805 reste servi depuis `commande_argon_v56_nuit_v2.py` », contraire au texte de course qui sert depuis la v6 ; dire un seul fichier.

**Configuration de course suivante (`configuration-boucle-reelle-v9.json` ou celle qui suivra)** : arguments de réflexion et plafonds de texte ≥ 16 000 pour tous les rôles de Google ; retirer de Google le vérificateur et les rôles courts s'ils ne peuvent pas payer ce plafond sous leur plafond de session (0,10 USD pour le vérificateur selon l'en-tête v3 point 2) ; épingler l'empreinte de la commande v7 et du module d'appel.

**Texte de course (préenregistrement suivant)** : désigner le relais par fichier et empreinte, et relever au rapport de course la ligne « relais prêt » et `GET /relais/etat` (champ `version`), pour que le fichier en service soit prouvé et non seulement prescrit.

## Relevé de méthode

**Chaîne de raisonnement.**
1. La règle à l'octet : `git -C /home/user/controle-ia-travail show origin/main:CLAUDE.md`, section « Appels aux modèles de Google ».
2. La commande v6 auditée est celle de la course : `sha256sum` rend `5eae1a04…6e55`, égal à son compagnon et à `configuration-boucle-reelle-v8.json` l. 327-330 (§ 1).
3. La configuration v8 fait appeler la commande vers `http://127.0.0.1:8805` avec les bornes 32 000, 4 000, 1 000 (l. 273-298).
4. Le relais 8805 en service est prescrit `commande_argon_v56_nuit_v6.py servir` par le préenregistrement v2 l. 711-713 et la consigne de poste v67-v4 l. 78 ; l'en-tête de la v6 dit la v2 (l. 33-34) ; v2 absente du disque et de l'historique de `origin/main` sous `docs/notes/` et `scripts/` (§ 2).
5. Le relais délègue à `collisionneur_v7.appeler_gemini(attentes=(0,))` (v6 l. 376), dont l'empreinte est exigée égale à `c9725f02…` (l. 233, 250-254) ; le fichier versé a cette empreinte (§ 1).
6. Le corps réel ne porte que `maxOutputTokens` (`collisionneur_v7.py` l. 427-428) : E1 NT (lecture directe).
7. `maxOutputTokens` = `mt`, abaissé au budget de session jusqu'à `mini` (v6 l. 494-497), bornes 4 000 et 1 000 par rôle (l. 433-441) : E2 NT pour ces rôles sans hypothèse ; pour le proposeur, NT faute de tout plancher.
8. Aucune lecture de limite de mots dans M1, M2, M3 (lecture des trois blocs, § 3) : E3 NT.
9. Les pensées sont fondues dans la sortie (`collisionneur_v7.py` l. 455) et jamais lues seules en M1 ni M2 ; essais et mutations v6 sans aucune des notions de la règle (`grep -n -i -c "thinking\|thoughts\|reflexion\|réflexion\|pensee\|pensée\|RECITATION\|SAFETY\|limite de mots"` sur `test_commandes_tour_ferme_v6.py` et `mutations_commandes_tour_ferme_v6.py` : 0 et 0) : E4 (pensée) et E5 NT.
10. `REFUS_GEMINI` contient SAFETY et RECITATION, `MAX_TOKENS` et vide sont classés `TRONQUE`/`VIDE` (l. 527-557), et M1 rend 5 sur `REFUS`, `VIDE`, et `TRONQUE` hors rôles de tests (v6 l. 560-567) : E4 T pour ces cas.
11. M1 rend code 0 sur `TRONQUE` pour `experimentateur_test` et `lecteur_test` (l. 413, 563-564), éprouvé comme voulu par `test_commandes_tour_ferme_v6.py` l. 1360-1387 : E4 NT pour MAX_TOKENS sur ces rôles ; introduit en v6 (`diff-argon-v5-v6.patch` l. 100-101).
12. Les écarts E1-E3 existent à l'identique en v3, v4, v5 (`grep` des lignes `mt = min(maxi…` et du corps, § 5).

**Objets de contrôle.** Mon mécanisme est la recherche par motifs plus la lecture. (a) Objet où « ce fichier pose la réflexion dans le corps » est **vrai** par construction : `scripts/lancer_course_auto_conception_v10.py` contient `thinkingConfig|thinkingBudget|thinkingLevel` ; prédit : mon motif le trouve ; rendu : 1 occurrence (`Grep` en mode compte sur `scripts/`). (b) Objet où c'est **faux** : `collisionneur_v7.py` ; prédit : 0 occurrence de ces motifs, et seul `maxOutputTokens` ; rendu : la recherche insensible à la casse de `thinking` n'y rend que l. 404, un commentaire de l'appel à Claude, et `maxOutputTokens` en l. 428. (c) Pour « ce fichier est le relais 8805 » : vrai attendu sur la v6 `servir` (rendu : `HTTPServer((HOTE, args.port)…)` l. 391, port désigné par le préenregistrement l. 711) ; faux attendu sur `relais_gemini_v1.py` (rendu : trouvé par les motifs Google, écarté par son port d'usage 8788, l. 36). Limite : un relais lancé par une ligne que je n'ai pas lue, hors `docs/notes/` et `scripts/`, m'échapperait.

**Premier pas non justifié.** Pas 4 : quel fichier a réellement tenu le port 8805 n'est que prescrit (texte de course), non prouvé par un relevé de course ; le justifierait un relevé `GET /relais/etat` (champ `version`) ou la ligne « relais prêt » d'une course effectuée. Et, au pas 7, que la réflexion se compte dans `maxOutputTokens` est supposé (documentation de l'interface de Google non relue sur pièce) ; la conclusion NT de E2 n'en dépend pas pour les bornes 4 000 et 1 000.

**Mode d'échec affecté.** Sans objet : audit de conformité sur mandat direct, sans ligne de la table des relecteurs.

**Dérivation de l'énoncé seul.** Sans objet : je ne suis pas un agent de re-dérivation.

**Trouvaille de côté.**
- Quatre lanceurs de `scripts/` (`lancer_course_auto_conception_v7.py` à `_v10.py`) portent un réglage de réflexion ; les `epreuve_temoins_auto_conception_v4.py` à `_v9.py`, `sonde_carbon_synchrone_v1.py` et `lancer_course_auto_conception_v4.py` à `_v6.py` touchent l'interface de Google sans motif de réflexion trouvé : autres chemins vers Google, hors de mon périmètre, à auditer à part.
- `collisionneur_v8.py` et `collisionneur_v8_plafonds_bas_v1.py` (`docs/notes/…/course-2/collisionneur-v8/`, `…/collisionneur-experimentateur-v1/script-v1/`) contiennent aussi les motifs Google : autres appelants possibles, non lus.
- L'en-tête de la v3 (dernier paragraphe de l'historique) note que `COLLISIONNEUR_DEFAUT` ne pointe sur rien depuis ce dossier : `servir` exige `--collisionneur` explicite, ce que fait le texte de course.

**Évaluateur et conseil.** Ce qui juge cette pièce : la lettre de la règle et son lecteur. Témoins : les trois objets de contrôle ci-dessus. Par où elle pourrait obtenir un bon jugement sans le mériter : en tenant pour « relais en service » le fichier que le texte prescrit, sans relevé de course (dit au premier pas non justifié) ; en déclarant E4 tenue pour le vide sur la foi de M3 alors que M1 seul ne la tient pas (dit au § 4) ; en manquant un appelant Google construit sans aucun de mes motifs.

Note : les noms de fichiers et les motifs de recherche cités contiennent des noms de famille de modèles ; ils sont gardés tels quels pour que les chemins et les commandes se rejouent. Aucun identifiant de modèle n'est écrit ici.
