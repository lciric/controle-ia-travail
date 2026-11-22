# Rapport du développeur — lanceur v11 de la course d'affinage des idées des mentors

- Écrit le 22 novembre 2026 par un sous-agent développeur (Opus 5.5) de la session du compte organisme. Pièce de classe C ; les pièces qu'il décrit sont de classe B (code), à contre-lire par un autre modèle.
- Hors ligne : aucun appel payant, aucune valeur de clé lue ni écrite, aucun relais réel lancé, rien de committé ni poussé. Aucun fichier sous `archives-reponses-modeles/`, aucune sortie de course, aucune réponse de modèle lus. Le dépôt public `lciric/ideation-organism` (commit `a41b7b50`) a été cloné en lecture dans le bloc-notes, hors dépôt, pour le point 7 ; la branche `prep/affinage-v10-compte-organisme-v1` a été ouverte dans un worktree détaché du bloc-notes pour rejouer ses essais.
- Fondements, dans l'ordre d'arrivée ; le dernier prime : GO-2026-11-22-107, -110, -111 ; ordre de la mère (numéro 11, base v10) ; R-4995 (45 USD) ; points techniques du brouillon 1 du préenregistrement v11 ; décision de la mère sur Argon ; GO-2026-11-22-124 (règle de LUC simplifiée) ; exigences du préenregistrement (premier 4xx de l'interface, code 5 ; prolongations des GO) ; devis v11 ; R-5018 (prix de Google 4 / 20).

## 1. Fichiers écrits (tous neufs ; rien d'existant n'est modifié)

| fichier | rôle |
|---|---|
| `scripts/lancer_course_affinage_mentors_v11.py` | lanceur v11, dérivé du lanceur v10 de `prep/affinage-v10-compte-organisme-v1` (`b0829025…`, vérifié à son compagnon) par un programme de remplacements comptés (gardé dans mon bloc-notes) |
| `tests/test_lancer_course_affinage_mentors_v11.py` | essais v10 (`4e651669…`) portés, plus les essais propres à la v11 |
| `scripts/commande_gemini_flux_v1.py` | commande externe Gemini en flux, sous la garde commune des appels à Google (Carbon et Argon) |
| `tests/test_commande_gemini_flux_v1.py` | essais de la commande devant le **vrai** relais Gemini v3 de `main` et un faux amont en flux |
| `scripts/sonde_astra_affinage_v3.py`, `scripts/sonde_astra_courses_v2.py` | sondes d'Astra pour `gpt-6.2-astra`, prix 8 / 40 |
| `tests/test_sonde_astra_courses_v2.py` | essais de la sonde commune v1 adaptés, plus quatre mutations |
| `tests/test_orchestrateur_refus_relais_claude_v11.py` | point 7 : un refus du relais Claude compte comme échec du rôle (A3, A14), sur la vraie classe de l'orchestrateur |
| `course-v11/configuration-course-affinage-mentors-v11.json` | copie de la configuration v9 (`e7378f89…`) : clés, notes, paramètres nommés de la part Claude, de la confirmation de GO-107 et des juges |
| `course-v11/declaration-relais-gabarit-course-affinage-v11.json` | gabarit de déclaration des relais |
| `course-v11/rapport-developpeur-lanceur-v11.md` | ce rapport |

Les fichiers d'abord écrits sous des noms v8 ont été retirés du worktree (copie dans mon bloc-notes, jamais versée). `course-v8/mandat-fable-preenregistrement-affinage-v8.md` (de la mère) n'a pas été touché.

## 2. Ce qui change par rapport au v10

### 2.1 Clé Claude : LUC
- Tous les appels Claude passent par `RR_ANTHROPIC_API_KEY_LUC` ; Minuit rejoint Rigaud dans les clés exclues (déclaration, configuration, environnement : refus).
- **GO-2026-11-22-124** : le solde de LUC n'est pas lu et n'est pas une condition de départ ; ni plancher ni couverture (les versions intermédiaires de ce travail les portaient : retirées, avec leurs essais). La ligne de LUC du relevé, si elle est écrite, est recopiée pour information. « Minuit compté au prix relevé » est retiré.
- **Plafond propre de la part Claude : 45 USD** (R-4995), paramètre nommé `changements_v11.plafond_part_claude_usd`, égal à la constante du lanceur (retiré, relevé, abaissé : refus ; `part_de_la_couverture` réintroduite : refus). Le relais Claude doit être lancé à `--plafond-usd 45` exactement et avec `--journal` (chemin absolu).
- **Arrêt au fil de l'eau, garde neuve** (`SurveillanceCleClaude`) : toutes les 10 s, état du relais Claude (part engagée = `depense_usd` + `engage_usd`, dépense plus montants réservés des appels en vol ; `refus`) et lignes neuves de son **journal** (le relais épinglé `1b90b020…` relaie les refus d'Anthropic sans les lire et garde le statut, pas le message). Arrêt propre — SIGTERM à l'orchestrateur par son PID, message sur la sortie d'erreur, `alerte-arret-part-claude.json` scellée (le **statut**, pas la cause), manifeste de fin, **code 5, sans relance** — au premier statut **4xx autre que 429** au journal (un refus faute de crédit est un 400, R-4833), au premier refus du relais (`refus` > 0 : son 402 à 45 USD), à une part engagée qui atteint 45 USD, ou à un état ou un journal illisible trois fois de suite. Une lecture manquée isolée est comptée, jamais tue. Le code 5 garde aussi son sens de la v10 (garde de crédit d'un relais dispensé) ; le fichier d'alerte dit lequel.

### 2.2 Lignes de GO et prolongations
- `verifier_les_go` lit : **GO-2026-11-18-14** (plafond 150 USD lu exactement), prolongé par **GO-2026-11-22-80** au 15 décembre si cette ligne est valide (Lazar, non révoquée, en période, qui dit prolonger GO-14) ; **GO-2026-11-22-124** (Lazar, en période, non révoquée, qui nomme GO-107 et 45 USD) ; **GO-2026-11-22-107** (exception déclarée à GO-2026-11-22-70 : LUC, la règle, la course), prolongé à l'échéance de GO-124 **seulement si la ligne de confirmation de Lazar est nommée dans la configuration** (`changements_v11.confirmation_prolongation_go_107`, null aujourd'hui) **et inscrite au registre** (Lazar, non révoquée, en période, qui nomme GO-107). Nommée mais absente ou invalide : refus. Non nommée : au-delà du 25 novembre, refus.
- Une prolongation absente ou invalide n'est jamais tue : son motif est écrit au manifeste et le GO visé garde sa propre échéance.
- **Identifiants à trois chiffres de rang** (brouillon 2, point a) : la lecture héritée du v10 (`verifier_go`, `ecrire_registre_derive`) ne voyait que deux chiffres de rang ; GO-2026-11-22-107, -124 et toute révocation à trois chiffres lui étaient invisibles. Les deux expressions lisent désormais deux ou trois chiffres (les lectures neuves de v11 le faisaient déjà). Essais : ligne à trois chiffres lue (et ligne à deux chiffres toujours lue), révocation à trois chiffres vue (refus), registre dérivé qui la garde, artefact (l'ancienne expression absente du lanceur). La garde de calcul `.claude/hooks` (même défaut, R-5013) **n'est pas touchée** ; la commande de lancement garde `GO_ID=GO-2026-11-18-14`.
- **Ce que l'orchestrateur épinglé accepte au registre dérivé** (brouillon 2, point b ; lecture de `a41b7b50`) : `demonstrations/ideation_v8.py` (`2e2be8d7…`) appelle `configuration_v56.verifier_go_v56` = `configuration_v55.verifier_go_v55` (`2e6237c0…`) sur `GO_ID` de l'environnement (le lanceur y met GO-2026-11-18-14) et sur le registre dérivé. Cette lecture (via `configuration_v53`, `ef72ffbf…`) : identifiant à **deux** chiffres de rang seulement (`GO_ID` et `LIGNE_GO`, les lignes à trois chiffres sont ignorées sans refus) ; type « calcul », Lazar ; **période de la seule ligne `GO_ID`** (`accorde ≤ aujourd'hui ≤ echeance`), sans notion de prolongation ; révocations de type « révocation » qui nomment `GO_ID` ; montant exactement égal au plafond requis (150). Le registre dérivé porte la ligne de GO-14 (échéance 2026-11-25) et ses révocations, pas GO-80. **Conséquence : après le 25 novembre, l'orchestrateur refuse le départ (A15, « hors de sa période de validité »), même si le lanceur a accepté la prolongation par GO-80** ; le refus vient avant tout appel de modèle (aucune dépense), mais la course ne part pas. GO-80 serait accepté par l'orchestrateur comme `GO_ID` (deux chiffres, calcul, Lazar, 150 USD, échéance 15 décembre) s'il était passé en `GO_ID` et gardé au registre dérivé : changement de la commande de lancement, non fait ici (décision de la mère ; la garde de calcul du dépôt lit aussi `GO_ID`).

### 2.3 Astra : gpt-6.2-astra sur OPENAI_API_KEY_2
- Modèle, prix (8 / 40, R-4905) et clé (`OPENAI_API_KEY_2`) dans les arguments épinglés et la déclaration ; `commande_astra_v1.py` inchangée (modèle et prix en arguments).
- Sondes neuves `sonde_astra_affinage_v3.py` (`32366123…`) et `sonde_astra_courses_v2.py` (`80074c82…`), rapports du jour sous `course-v11/` seulement ; version et modèle servi relus.
- Palier de prix : l'entrée la plus longue servie (octets + 1 024) reste sous 272 000 jetons (8 785).
- Ligne d'Astra du devis interne : 0,276 USD par appel (ligne commune « proposeur hors Claude », supposée pour Astra) : inchangée.

### 2.4 Carbon et Argon en flux, sous la garde Google
- **Relais** : le relais Gemini **v3** de `main` (`relais_gemini_v3.py`, `2cf6bc6d…`), qui tient la clé, lit l'amont en flux et pose `includeThoughts`. Aucun relais neuf. La passe X n'avait pas de relais (son exécutant appelait Google clé en main).
- **Commande neuve** `scripts/commande_gemini_flux_v1.py` (`6aaf235d…`) : aucune clé ; garde commune `garde_google_v3.py` (`923679b5…`, vérifiée) **avant l'envoi** (corps exact, mode « flux ») et **après la réponse** (zéro pensée, MAX_TOKENS, SAFETY, RECITATION, texte vide, invite bloquée : défaut nommé, code 5, jamais une réponse) ; la sortie n'est jamais abaissée (refus, code 4, si le pire cas dépasse le plafond de session). **La commande compte la réflexion dans la sortie maximale** : pire cas = entrée gardée × prix d'entrée + `maxOutputTokens` × prix de sortie.
- **Prix (R-5018)** : Argon et Carbon à 4 USD par million d'entrée et 20 de sortie, réflexion comprise (page de prix versée sur `main`, `d3aa716e…`) ; les bornes 8,3 / 41,5 ne valent plus. Le relais v3 ne porte aucun prix (il borne des appels).
- **Carbon** : niveau « high », provision 28 672 (≥ 1,25 × 20 696), sortie 65 536 (limite en flux ; texte 36 864 ≥ 16 000 et > 2 × 9 000 caractères), délai 1 500 s + 60 s (+ 30 s ≤ 1 800 s), relais au port 8791 : `--max-appels` ≥ 40, `--delai-silence-s` ≤ 240, `--delai-amont-s` ≥ 1 500, explicites, sans `--sans-pensees-amont`.
- **Calcul (point 3 de la mère)** : plafond de session des proposeurs 3,00 USD (configuration v9) ; entrée la plus longue servie 7 478 caractères → ⌈7 478 / 3 × 1,05⌉ = 2 618 jetons ; pire cas d'un appel = 2 618 × 4 / 10⁶ + 65 536 × 20 / 10⁶ = 0,010472 + 1,310720 = **1,321192 USD ≤ 3,00** ; si la réflexion était facturée en plus de la sortie maximale : + 28 672 × 20 / 10⁶ = 1,894632, toujours sous 3,00. Le devis v11 annonce 2,30 au pire pour Carbon : d'autres réglages que les miens (à recouper). Un compte réel par `countTokens` au-dessus de caractères / 3 fait refuser la commande (code 4) plutôt que dépasser.
- **Argon** (décision de la mère : sous la garde, proposeur et second juge) : même commande (`--espece argon`), relais v3 au port 8788 (`--max-appels` ≥ 2 × (16 + 32 × espèces), mêmes délais) ; niveau « high », **provision 24 576 (HYPOTHÈSE)**, sortie 45 056 (texte 20 480) ; l'enveloppe v5 (`commande_argon_v3d.py`) est refusée à la déclaration, et la garde la refuse aussi. Pire cas d'un juge = 4 030 × 4 / 10⁶ + 45 056 × 20 / 10⁶ = **0,917240 USD** (plafond minimal 0,92) ; d'un proposeur 0,911592. **Emplacement nommé** `argon_v11.plafond_session_juge_usd` = **1,00** (devis v11) ; vide, le lanceur refuse le départ ; rempli, il remplace `plafonds_session.juge` (rôle « juge » : vaut aussi pour le juge Claude). Le devis donne 0,70 « si la réflexion est comptée dans le plafond de sortie » : c'est le cas de ma commande, mais avec ces réglages 0,70 ne suffit pas (0,92 exigé) ; 0,70 demanderait une sortie d'environ 34 000 jetons, dont le texte (≈ 9 400 au-delà de la provision) n'atteint pas 16 000 : refusé par la garde. 1,00 tient. **Option appliquée : réflexion comptée dans le plafond de sortie (`maxOutputTokens` = 45 056, jamais abaissé ; aucune provision ajoutée en plus), emplacement 1,00 USD** (et non 1,10). Le pire cas de la mère (0,6708) suppose d'autres réglages que les miens (0,917240 avec une sortie de 45 056).
- Devis interne : Carbon 0,4805 USD par appel (2 618 × 4 + 23 500 × 20, par million) ; base sans marge 40,848 USD pour cinq espèces. Lignes d'Argon (0,276 et 0,0347) non recalculées.

### 2.5 Garde des appels à Google dans le lanceur
- `controler_chemins_google` : chaque commande Google déclarée est jouée hors ligne devant un faux amont local qui capture le corps de génération (rien ne part) ; le corps passe `verifier_reglages_google` et, pour un proposeur, la limite de l'invite ; moteur réel : refus ; simulé : écrit au manifeste. Sur les vraies pièces : Carbon et Argon en flux conformes ; Argon v3d et l'ancien lot de Carbon refusés.

### 2.6 Point 7 : un refus du relais Claude compte comme échec du rôle
- Lu : `pole/noyau_v56.py` (`eb5a003e…`) ne lit le texte que si `r.statut == "ok"` ; `pole/suivi_roles_v54.py` (`62022597…`) compte alors un échec (A3 : trois consécutifs arrêtent le rôle) et un inexploitable (A14). Essais sur la vraie classe `SuiviRoles` : sain (trois refus → rôle arrêté, A14 à 1,0) et artefact (refus entrecoupés → rôle non arrêté, A14 à 0,5). Sautés sans orchestrateur ; joués ici avec `ORCHESTRATEUR_AFFINAGE_ESSAI` sur le clone. Non vérifié par exécution : que l'adaptateur Claude rende un statut autre que « ok » sur un 402 du relais (lu : « erreur » par défaut, `adaptateurs.py` l. 481) ; l'arrêt du lanceur (code 5) n'en dépend pas.

## 3. Part Claude estimée et borne haute

Devis v10, § 4 (prix du devis v6) : **estimation 20,65 USD** (16 × 0,141 + 16 × 0,3525 + 160 × 0,031 + 160 × 0,037 = 18,776 ; × 1,1), **haut 74,62 USD** (16 × 0,400 + 16 × 1,000 + 160 × 0,132 + 160 × 0,152 = 67,84 ; × 1,1). Le haut n'est pas une borne : sous les plafonds de session (proposeurs 3,00, aiguilleur 0,25, juge 1,00 avec l'emplacement), la part Claude pourrait atteindre 32 × 3,00 + 160 × 0,25 + 160 × 1,00 = 296 USD ; **la borne effective est le plafond propre de 45 USD**, puis 150 pour la course. Le haut (74,62) dépasse 45 : dans ce régime, la course s'arrêterait au code 5.

## 4. Essais retirés des essais v10 (et pourquoi)

- La fin du fichier v10 (à partir de « majeur 2, commandes exactes v7 ») : essais v6b portés, v8, v9, v10, qui relisent des pièces des seules branches `prep` (lanceurs v7 à v9, commandes, gabarits et essai à blanc v10) ou portent sur la commande par lot.
- `test_carbon_relais_max_lots_insuffisant_refuse` (lots), `test_v7_sonde_d_un_autre_jour_sous_course_v7`, `test_v7_rapports_reels_du_18_novembre_acceptes_ce_jour_seulement`, `test_v7_sonde_commune_saine_et_artefacts` (chemins de sondes des v7 à v10), les quatre essais « Minuit » (règle retirée).
- Les essais v10 restent verts dans leur branche (compte au compte rendu).

### Essais passés (22 novembre, hors ligne)
- `tests/test_lancer_course_affinage_mentors_v11.py` : **255 réussis, 4 sautés, 0 échec** (après la lecture des GO à trois chiffres).
- `test_commande_gemini_flux_v1.py`, `test_sonde_astra_courses_v2.py`, `test_orchestrateur_refus_relais_claude_v11.py` (orchestrateur épinglé lu dans un clone à `a41b7b50`) : **48 réussis**.
- Essais v10 dans leur branche (`b0829025…`, lanceur et essais v10 non modifiés) : 259 réussis, 5 sautés.
- Essais v6 du dépôt (non modifiés) : 137 réussis, 4 sautés, **3 échecs préexistants** de `test_astra_carbon_declares_affinage_v6b.py` (relevé daté du 18 novembre comparé à la date du jour), sans lien avec ce travail.

## 5. Points ouverts pour le contre-lecteur et la mère

1. **Provision d'Argon** (24 576) et entrée d'un juge (+ 1 000 caractères) : hypothèses ; elles fixent le plafond minimal des juges (0,92).
2. **Pire cas de Carbon** : 1,32 USD ici contre 2,30 au devis v11 : réglages à recouper avec Fable.
3. **Le relais v3 n'applique pas la garde** (elle vit dans la commande, avant et après) ; la procédure interdit tout autre client du port.
4. **Statuts lus au journal** : tout 4xx sauf 429 arrête, y compris un 400 de requête mal formée (prudence). Les 5xx n'arrêtent pas.
5. **Plafond des juges** : un seul plafond par rôle dans l'orchestrateur ; 1,00 vaut aussi pour le juge Claude (borné par les 45 USD de LUC).
6. **Confirmation de GO-107** : `confirmation_prolongation_go_107` est null ; après le 25 novembre, le lanceur refuse tant qu'elle n'est pas nommée et inscrite (et la configuration change alors d'empreinte : nouvelle épingle).
7. **Préenregistrement v11** : `PREREG_SHA256` vide ; tout lancement (essai à blanc compris) est refusé jusqu'à ce qu'il soit posé (cycle d'empreintes gardé).
8. Constantes du lot sans usage (`MIN_RELEVES_CARBON`, `INTERVALLE_CARBON_S`…) et textes du v10 qui parlent du lot (code 7 de la commande par lot) : inertes.
9. `garde_google_v3.py` est une pièce de `main`, absente de cette branche : le lanceur l'exige dans le dépôt de travail ; les essais l'extraient de `origin/main`.
10. Le relevé des crédits garde son format v10 pour les autres clés (dispense R-3237 pour Argon, Carbon ; Astra lisible ou dispensée).
11. **Orchestrateur et prolongation** (§ 2.2) : après le 25 novembre, l'orchestrateur épinglé refuse GO-2026-11-18-14 (échéance de sa ligne) quelle que soit GO-80 ; à trancher par la mère avant tout départ après cette date (passer `GO_ID=GO-2026-11-22-80` et garder sa ligne au registre dérivé, ou autre voie).
12. **Garde de calcul du dépôt** (`.claude/hooks`, R-5013) : même lecture à deux chiffres ; non touchée, comme demandé.
