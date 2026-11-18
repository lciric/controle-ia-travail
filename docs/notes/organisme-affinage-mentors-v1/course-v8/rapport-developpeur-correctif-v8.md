# Rapport du développeur — correctif v8 de la course d'affinage des idées des mentors

- Écrit le 2026-11-18T21:58:43Z (`date -u +%FT%TZ`) par le modèle L', sur demande de la mère. Branche `prep/affinage-v8-compte-organisme-v1`, partie de `origin/prep/affinage-v7-compte-organisme-v1` (`2c31fc6f`, contre-lecture v7 « Scellable. ») ; `origin/main` (`3ea97bc7`) et `origin/lot/compte-organisme-v1` récupérées par `git fetch` ciblé.
- **Aucune dépense, aucun appel réseau vers un fournisseur, aucun relais réel, aucun lanceur sans `--a-blanc`.** Exécuté : essais hors ligne ; un essai à blanc du lanceur v8 (moteur simulé de l'orchestrateur épinglé, dossier neuf hors dépôt). Aucune valeur de clé lue. L'orchestrateur `/home/user/ideation-organism` (`a41b7b50…`) n'a été que lu (`PYTHONDONTWRITEBYTECODE=1`, `-B`). Rien n'est lu ni écrit sous `diag/`, `donnees/`, `registres/`, `attestations/`, ni sous les sorties et journaux de la course d'auto-conception ; seul le diagnostic `510312b1…` (faits techniques) a été lu, par `git show`.
- Ajouts seuls (R12) ; aucun fichier existant modifié.

## Verdict du développeur

La correction demandée **ne peut pas être faite telle quelle** sur deux points, pour des raisons que le code épinglé établit ; la v8 porte la correction la plus proche qui tienne, et les deux écarts sont des points ouverts pour la mère :

1. **Provision de pensée de 32 768 : impossible sous le plafond par appel de l'affinage.** La garde avant envoi de la commande de Carbon (`commande_gemini_lot_v1.py`, `9484dce0…`, l. 167-173) exige, au prix plein, entrée × 8,3 / 10⁶ + (sortie + provision) × 41,5 / 10⁶ ≤ `PLAFOND_SESSION_USD`, et l'orchestrateur passe à chaque proposeur min(1,50 ; reste de l'étape) (`pole/noyau_v56.py` l. 161 ; configuration v6, `plafonds_session.proposeur` = 1,5). Avec 32 768 : (4 096 + 32 768) × 41,5 / 10⁶ = 1,5299 USD **avant l'entrée** (1,5516 avec le fil le plus long) : **chaque appel de Carbon rendrait le code 4, rien envoyé** — vérifié aussi en jouant la vraie commande de `main` hors réseau (essai `test_v8_provision_32768_la_vraie_commande_refuse_chaque_appel`). Le calcul du diagnostic (2,38 USD sous 3 USD) vaut pour le plafond de la course d'auto-conception, pas pour l'affinage. **Retenu en v8 : provision 28 672** (28 × 1 024 ; marge 1,385 sur la plus forte pensée observée, 20 696), sortie maximale 16 384 comme demandé (la commande la ramène à 6 948 à 7 174 jetons sous 1,50 USD).
2. **Délai de 3 000 s : impossible sans une version neuve de l'orchestrateur.** L'adaptateur de commande externe tue le groupe de processus à 1 800 s (`pole/adaptateurs.py` l. 622, `DELAI_COMMANDE_S = 1800`) et la course 2 le construit sans délai (`demonstrations/ideation_v8.py` l. 74) : ce délai n'est réglable ni par la configuration ni par la ligne de commande ; A3 (`arrets.a3_delai_s` = 1 800 s, configuration v6) compterait aussi l'appel comme coupé. Au-delà, l'orchestrateur tuerait la commande **avant** qu'elle n'annule le lot (lot laissé courir, plafond de session compté). **Retenu en v8 : délai de lot 1 620 s** (+ 120 s), délai de requête 60 s (au lieu de 120 par défaut) : durée maximale 1 620 + 30 + 2 × 60 = 1 770 s, la même qu'en v7, 30 s sous 1 800.
3. **Astra : aucune reprise en v8** (voir § Astra).

Hypothèse (aucune), mesures, seuils (aucun), plafond d'arrêt (150 USD), composition (deux Claude, Argon, Astra, Carbon ; pas de Kimi), clé Claude (Minuit seule), configuration v6, orchestrateur, commandes épinglées : **inchangés**.

## Pièces versées (toutes scellées, compagnon `.sha256`)

| pièce | sha256 |
|---|---|
| `scripts/lancer_course_affinage_mentors_v8.py` (lanceur v8) | `76c45b8e6188944bc78a5175d183aa066df21c33f31f04712c316c7875fa4eda` |
| `course-v8/preenregistrement-course-affinage-mentors-v8.md` (épinglé par le lanceur v8) | `fb71f5006c102162eaa78cdbf3c0888627d413f08846239896e87d62c2350a20` |
| `devis-course-affinage-mentors-v8.md` | `91171ea56e0c3b9eb6486a5f8d0444f1017cdf4a00b5f4e5c5b3f540529aa97f` |
| `course-v8/commandes-exactes-course-affinage-v8.md` | `1ac4fbebfc0e72c7f07e5fd945973e600e61dc568c3eb369c7eb6bb535938544` |
| `tests/test_lancer_course_affinage_mentors_v8.py` | `b3ee7522a83ce0b82461fbb308b39515e3cf4c37bdfaae36af0007876e808ea0` |
| `course-v8/declaration-relais-gabarit-course-affinage-v8.json` | `0c0b43460c63b28291ea84b3bcba55ae587dc73bbc9a157891fe39e7cc11c84c` |
| `course-v8/releve-credits-gabarit-course-affinage-v8.json` | `ccc7380dfcb9fdadb9ee32449372ab8c3d3cdc25c69e6e4b5730c791ef9a977f` |
| `course-v8/releve-prix-claude-gabarit-course-affinage-v8.json` | `ce6ee804428ce7d4b6cdf868a6e595a5114b2ea4c5576289a0567c9e35e5088c` |
| `course-v8/essai-a-blanc-v8/…` (15 fichiers : lanceur, orchestrateur, pièces d'essai) | voir leurs compagnons `.sha256` |

(`course-v8/` = `docs/notes/organisme-affinage-mentors-v1/course-v8/`.)

**Préenregistrement v8 : nécessaire**, parce que le texte v7 écrit les arguments de Carbon (provision 8 192, délai 1 500 s, 1 770 s par 1 500 + 30 + 2 × 120), nomme le lanceur v7 et le chemin de la contre-lecture v7. Ce qui change (différentiel v7 → v8, en fin de texte) : paragraphe de Carbon (réglages, pire cas d'un appel 1,50 USD, risque dit), liste d'arrêt (gardes v8), devis v8 et base de l'écart (41,136), chemins `course-v8/`, une seule course de v1 à v8. Rien d'autre.

**Contre-lecture exigée par le lanceur v8** : `docs/notes/organisme-affinage-mentors-v1/course-v8/contre-lecture-preenregistrement-course-affinage-mentors-v8.md`, scellée, du modèle K, citant en entier `fb71f5006c102162eaa78cdbf3c0888627d413f08846239896e87d62c2350a20` (préenregistrement v8) et `76c45b8e6188944bc78a5175d183aa066df21c33f31f04712c316c7875fa4eda` (lanceur v8), première ligne sous `## Verdict` exactement `Scellable.`.

## Ce que fait le lanceur v8 de plus que le v7 (gardes neuves, toutes en refus, code 2)

1. **Options de Carbon exigées** (`lire_reglages_carbon`, à la déclaration, avant l'égalité aux arguments épinglés) : `--prix-entree`, `--prix-sortie`, `--facteur-lot`, `--max-sortie-jetons`, `--sortie-min-jetons`, `--provision-pensee-jetons`, `--intervalle-s`, `--delai-s`, `--delai-requete-s`, chacune **une fois**, réel fini > 0 ; absente → refus « absentes » (le défaut de la commande — 8 192, 1 500 s — est refusé). La déclaration qui porte les arguments v7 est refusée avec ce motif.
2. **Provision** ≥ ⌈1,25 × 20 696⌉ = 25 870 jetons.
3. **Durée** : délai + intervalle + 2 × délai de requête + 30 s ≤ min(1 800 s de l'adaptateur, A3 de la configuration pour Carbon) ; **délai de lot ≥ 1 620 s** (le délai v7 est refusé).
4. **Pire cas** (`controler_pire_cas_carbon`, au départ, sur les seize fils réels expurgés et la consigne servie telle que `pole/course2_v53.py` l. 228-229 la compose) : pire cas minimal (sortie 4 096 + provision) ≤ plafond de session, sinon refus « code 4 » ; pire cas d'un appel, sortie demandée et borne au prix du lot écrits au manifeste de départ (`reglages_carbon_v8`).
5. **Relais de Carbon** : « releves » nul et `releves_restants` ≥ 1 120 (= 20 lots × (⌈1 620 / 30⌉ + 2)) dans `/relais/etat` ; les commandes v8 lancent le relais avec `--max-releves 2000` (défaut du relais Gemini v4).
6. **Devis** : `prop-carbon` 0,4985 USD par appel (au lieu de 0,276) ; base de l'écart au devis : 41,136 USD pour les cinq espèces déclarées.

**Pire cas d'un appel de Carbon** (dit par le lanceur et recoupé sur la vraie commande) : **1,499959 USD au prix plein**, sous le plafond par appel de l'affinage (1,50) ; 0,74998 au prix du lot ; sortie demandée 6 948 (fil le plus long, 7 478 caractères, entrée gardée 2 618) à 7 174 (fil le plus court). **Parts par clé du devis : elles tiennent, inchangées** : `RR_ANTHROPIC_API_KEY_MINUIT` 150 ; `GEMINI_API_KEY` (Argon et Carbon) 150 + 24 = 174 (Carbon : 16 × 1,50 = 24, ce que la garde du pire cas vérifie) ; clé d'OpenAI (secret de réseau, `OPENAI_API_KEY`, Astra) 24.

## Astra : reprise unique sur 502 « amont coupé » — non faite, proposition

Faisable sans toucher la commande épinglée (`986cf71e…`) par une enveloppe neuve entre la garde de crédit et la commande (la commande rend le code 5 et `erreur` = « HTTP 502 : … amont coupé après envoi … »). Mais **pas proprement sous le plafond de session de 1,50 USD** :
- la commande remplit le plafond (`max_completion_tokens` ≈ 28 000 jetons) et l'appel coupé est compté au pire cas (≈ 1,50 USD, que le relais impute aussi) ; une reprise porterait le coût de l'appel à ≈ 3 USD : l'orchestrateur lirait un coût au-dessus du plafond de session (statut « budget_depasse », texte non servi, `pole/adaptateurs.py` l. 772-774) et le relais d'Astra (plafond 24 = 16 × 1,50) refuserait les derniers appels (402) ;
- rendre seulement le coût du second essai cacherait une dépense à l'orchestrateur (repli silencieux, R5) : exclu ;
- partager le plafond entre deux essais (0,75 chacun) réduirait de moitié la sortie d'Astra à **chaque** appel (≈ 13 000 jetons au lieu de ≈ 28 000) : changement des conditions d'Astra, pas une correction ciblée.

Dans l'affinage, une coupure seule ne rend pas l'étape non mesurée : A14 tolère 5 appels inexploitables sur 16, A3 n'arrête le rôle qu'à trois échecs consécutifs (une coupure sur 11 appels observée le 18 novembre).

**Décision proposée à la mère** — reprise d'Astra dans l'affinage. Enjeu : une coupure d'amont perd une case d'Astra (≈ 1,50 USD comptés). Options : (a) accepter l'aléa (aucun changement ; coût : une case perdue par coupure) ; (b) enveloppe de reprise neuve, plafond partagé (0,75 par essai ; coût : sortie d'Astra réduite de moitié partout, risque de réponses tronquées) ; (c) plafond par appel des proposeurs relevé à 3 USD dans une configuration neuve, avec l'enveloppe (coût : parts au pire d'Astra 48, de Carbon 48, devis et préenregistrement neufs, contre-lecture). **Recommandation : (a)**, confiance moyenne. Défaut sous 48 heures : (a).

## Points ouverts (pour la mère)

1. **Provision de Carbon** (décision). Enjeu : la pensée de Carbon en lot n'est pas tenue par le fournisseur (diagnostic § 3) ; sous 1,50 USD, 28 672 est un compromis (marge de pensée 1,385, sortie 2 fois la plus forte observée). Options : (a) v8 telle quelle ; (b) 30 720 (marge 1,48, sortie 4 900, 1,44 fois) — une version suivante ; (c) configuration neuve à plafond par appel de proposeur ≥ 2,10 USD pour permettre 32 768 + 16 384 (2,06 USD au prix plein avec l'entrée la plus longue) — touche tous les proposeurs (plafond par rôle, non par espèce) : parts d'Astra et de Carbon 33,60, clé de Google 183,60, devis, préenregistrement et contre-lecture neufs. Recommandation : (a), confiance moyenne. Défaut sous 48 heures : (a).
2. **Pensée comptée dans `maxOutputTokens` ?** Non vérifié (documentation du fournisseur non lue ; aucun réseau). Si oui, la sortie demandée de 6 948 jetons couperait la réponse dès ≈ 3 500 jetons de pensée (code 5) et **aucun réglage sous 1,50 USD ne tient** avec cette commande : seule l'option 1 (c) le permettrait. Les compteurs du diagnostic ne tranchent pas (pensée + sortie ≈ 22 000 < 32 768 demandés dans l'autre course). Proposition : la mère fait lire la documentation du fournisseur (lecture, sans dépense), ou autorise un lot d'épreuve à 0,75 USD au plus avec les réglages v8 (dépense : mot de la mère, ligne de GO) avant la course.
3. **Délai de Carbon** (nœud technique) : relever au-delà de 1 620 s demande un orchestrateur neuf (délai de l'adaptateur pris dans `fournisseurs.<nom>.delai_s`, A3 par fournisseur dans la configuration), ses 25 empreintes ré-épinglées et une contre-lecture. Non fait ici (orchestrateur en lecture seule).
4. **Délai de requête de 60 s** : si la création d'un lot dépasse 60 s au relais, la commande rend le code 3 au pire cas et le lot peut tourner sans être annulé (même risque qu'à 120 s, sur une fenêtre plus courte). Les créations observées sont courtes ; non mesuré ici.
5. **Annulations** : le relais Gemini v4 en permet 16 par défaut (`--max-annulations`) pour 20 lots ; A3 arrête Carbon bien avant (trois échecs consécutifs). Information.
6. **Sonde d'Astra** : le 18 novembre, celle de 13:58Z est lue et ne doit pas être refaite (deux rapports du jour font refuser le départ) ; tout autre jour, une sonde neuve sous `course-v8/` (les commandes v8, § 5), ou celle du jour faite pour l'autre course si elle existe à l'un des chemins lus.
7. **Dates des essais** : les essais qui jouent la sonde commune et la ligne de GO d'essai datent par `date -u` et valent du 18 au 30 novembre.
8. **Refus du crochet d'isolement de l'arbre de travail** (deux fois, aucune permission contournée) : une commande `git show` dans une boucle `for`, refusée comme « trop complexe », rejouée en commandes simples ; une lecture `git -C /home/user/ideation-organism status`, refusée parce qu'elle vise un dépôt hors de l'arbre : non rejouée (le lanceur v8 contrôle lui-même l'arbre de l'orchestrateur par sous-processus avant et après, et les essais le jouent ; l'essai à blanc a rendu le code 0).

## Décomptes d'essais (rien n'est sauté)

Commande (celle du § 4 des commandes v8) : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src /usr/local/bin/python3 -B -m pytest -q -rs -p no:cacheprovider tests/test_lancer_course_affinage_mentors_v8.py tests/test_lancer_course_affinage_mentors_v7.py tests/test_lancer_course_affinage_mentors_v6.py tests/test_astra_carbon_declares_affinage_v6b.py tests/test_sonde_astra_courses_v1.py`

> **554 passed in 431.91s**, 0 skipped, 0 failed (235 essais v8 + 175 v7 + 125 v6 + 5 v6b + 14 de la sonde commune).

- `tests/test_lancer_course_affinage_mentors_v8.py` seul : **235 passed**, 0 skipped — 175 essais v7 portés (monde ajusté : état du relais de Carbon avec « releves » et « releves_restants » ; chemins `course-v8/` ; base du devis 41,136 au lieu de 37,576, six espèces 48,8384 au lieu de 45,2784 ; mutation du mineur 3 sur la ligne v8 des champs), plus **60 essais neufs v8** (paramétrages compris).
- `tests/test_lancer_course_affinage_mentors_v7.py`, `…_v6.py`, `test_astra_carbon_declares_affinage_v6b.py`, `test_sonde_astra_courses_v1.py` (inchangés) : passent encore.

Essais neufs par garde (cas sain, artefacts, mutation) :

| garde | cas sain | artefacts | mutation (le code fautif réintroduit fait échouer l'essai) |
|---|---|---|---|
| options exigées | `test_v8_options_carbon_sain` | chaque option absente (9), doublée, illisible, nulle, `nan`, négative ; arguments v7 et options retirées de bout en bout | `test_mutation_v8_options_exigees` ; appel retiré de la déclaration : `test_mutation_v8_options_lues_a_la_declaration` |
| provision | 28 672 et la borne 25 870 | 8 192, 20 696, 25 869 | `test_mutation_v8_provision` |
| durée et délai | 1 770 + 30 ≤ 1 800 | 3 000 s, délai de requête 120, 1 700 s, intervalle 61, délai v7 1 500 ; A3 de 1 700 s ; A3 illisible | `test_mutation_v8_duree_sous_l_orchestrateur`, `test_mutation_v8_delai_releve` |
| pire cas | 6 948 / 7 174 jetons, 1,499959 USD, part 24 ; recoupé sur la vraie commande (sortie et pensée demandées, coût rendu) | provision 32 768 (lanceur et vraie commande : code 4, rien envoyé), sortie minimale 8 192, prix 50, plafond 1,2 | `test_mutation_v8_pire_cas_minimal` ; garde retirée du départ : `test_mutation_v8_garde_du_pire_cas_appelee_au_depart` (le mutant part avec une Carbon muette) |
| relevés du relais de Carbon | 2 000 et la borne 1 120 | 1 119, absent, illisible, « releves » 3, « releves » absent | `test_mutation_v8_releves_restants`, `test_mutation_v8_releves_nuls` |
| commandes v8 | toutes les exigences (lanceur, contre-lecture, `setsid`, `bwrap`, `socat`, sonde sous `course-v8/`, 28672, 1620, `releves_restants`, exclusion des deux courses) | — | `test_mutation_v8_commandes_sans_lancement_detache` |

## Essai à blanc v8

`/usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v8.py --a-blanc <dossier neuf du bloc-notes de la session, hors dépôt>` : **code 0**, sortie d'erreur vide ; orchestrateur réel épinglé, moteur simulé, relais factices ; commandes de Carbon et d'Astra extraites de `origin/main` et vérifiées ; cinq espèces (Kimi absent) ; 160 cartes à passeport ; coût simulé 5,6 USD ; base du devis **41,136**, écart −35,536 ; parts 150 / 150 / 24 / 24 ; `reglages_carbon_v8` au manifeste de départ (sortie demandée 6 948 et 7 174, pire cas 1,499959 USD) ; acte de gel au nom du lanceur v8 (`76c45b8e…`) et du préenregistrement v8 (`fb71f500…`) ; `plafond_arret.depasse` faux. Versé sous `course-v8/essai-a-blanc-v8/` (lanceur, orchestrateur, pièces d'essai ; les copies des commandes de `main` ne sont pas versées).

## Ce qui n'est pas vérifié

- Aucun relais réel, aucun appel amont ; la tenue de la pensée par le fournisseur, la durée réelle des lots de l'affinage et la sémantique de `maxOutputTokens` restent inconnues (points ouverts 2 et 3).
- Le prix estimé de Carbon (0,4985 USD par appel) repose sur trois lots d'une autre course ; la pensée sur les consignes de l'affinage n'est pas mesurée.
- `runs/` du dépôt n'a pas été lu : une course d'auto-conception partie sans manifeste de fin y ferait refuser le lanceur v8 (voulu).
- Les commandes v8 ont été écrites et relues, non jouées (rien n'est lancé ici) ; le lancement détaché (`setsid nohup … &`) n'a pas été essayé dans la session d'exécution.
