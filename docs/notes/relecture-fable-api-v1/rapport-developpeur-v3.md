# Relecture d'une correction par Fable 5.2 appelé par l'interface d'Anthropic — rapport du développeur, v3

Développeur neuf, Claude Opus 5.5, 21 novembre 2026. Pièce d'instrument (classe B) : à contre-lire par un autre modèle,
puis vérification des corrections par le même contre-lecteur. Ordre de la mère, pour la décision de Lazar
GO-2026-11-21-84 (Fable à sa limite d'usage dans Claude Code jusqu'au 24 novembre 05:00Z : les corrections sont écrites
par Opus, relues par Fable 5.2 appelé directement par l'interface d'Anthropic, puis scellées).

v2 (même développeur, 21 novembre 2026) : copie du rapport v1 (`rapport-developpeur-v1.md`, be900d1c…, inchangé,
R12), mise à jour après la contre-lecture `contre-lecture-outil-relecture-fable-api-opus-v1.md` (99eb9fdc…, verdict « à
corriger ») : ses deux textes de remplacement (§ 2, point 6 ; § 6, réserve 1) sont repris mot pour mot ; le reste n'est
changé que pour dire la v2 (noms des fichiers, essais, points 3, 4 et 8 du § 2, § 7 neuf). Le module et les essais v2 sont
la copie corrigée de référence du contre-lecteur (module acf9ddd2…, essais efa04f00…, ses sept corrections C1 à C7
appliquées par ses différences unifiées, vérifiées par `patch --dry-run` sur la v1), aux noms près : titre « version 2 »,
`VERSION = "relecture_fable_api_v2"`, nom du module dans l'emploi et dans `prog`, titre et importation des essais. La v1
(module 056bc4ef…, essais a3f649cf…) reste intacte.

v3 (même développeur, 21 novembre 2026, ordre de la mère après un défaut de réglage constaté sur la v2) : copie du
rapport v2 (`rapport-developpeur-v2.md`, 0a3bd162…, inchangé, R12), mise à jour pour la v3 ; le détail des changements
est au § 8. La v2 (module c8e8506f…, essais 89f91fa2…) reste intacte.

## 1. Fichiers

| Fichier | Rôle |
|---|---|
| `src/controle_ia/relecture_fable_api_v3.py` | l'outil (`python -m controle_ia.relecture_fable_api_v3 relire …`) |
| `tests/test_relecture_fable_api_v3.py` | 95 essais sans réseau |
| `src/controle_ia/relecture_fable_api_v2.py`, `tests/test_relecture_fable_api_v2.py` | la v2, gardée (R12) |
| `src/controle_ia/relecture_fable_api_v1.py`, `tests/test_relecture_fable_api_v1.py` | la v1, gardée (R12) ; l'appel de fumée a été fait avec elle |
| `docs/notes/relecture-fable-api-v1/fumee-v1/` | entrées de l'appel de fumée (consigne, pièce, remarques) et sa sortie (`sortie/`) |
| `docs/notes/relecture-fable-api-v1/journal-depense-fumee-v1.jsonl` | journal de dépense de l'appel de fumée (une ligne) |

Chaque fichier neuf a son compagnon `.sha256` ; les empreintes sont dans le rendu de la session à la mère.

## 2. Ce que fait l'outil

Commande :

```
python -m controle_ia.relecture_fable_api_v3 relire --piece P [--piece P2 …] --remarques R [--remarques R2 …]
    [--avant V] --consigne C --sortie DOSSIER --cle NOM_DE_VARIABLE [--espace NOM_DE_VARIABLE]
    --plafond-ligne USD --journal-depense FICHIER [--max-sortie N] [--fumee]
    [--effort low|medium|high|xhigh|max]
```

Dans cet ordre ; tout refus arrête l'outil **avant l'envoi**, code non nul, une ligne `refus_avant_envoi` au journal
(coût 0 ; v2, C7 : si cette ligne ne peut pas être écrite, un avertissement le dit, jamais de silence) :

1. **Entrées.** Lit les fichiers donnés, et eux seuls, en UTF-8 strict. Pièce absente : refus (code 3). Compagnon
   `F.sha256` présent : l'empreinte doit lui être égale, sinon refus (code 3) ; compagnon mal formé : refus. Sans
   compagnon : admis, déclaré « absent » dans l'en-tête et au journal.
2. **Invite.** La consigne telle quelle, puis chaque pièce entre
   `<piece role="correction|remarques|avant" chemin="…" sha256="…">` et `</piece>`. Une pièce qui contient elle-même
   `</piece>` est refusée (balise ambiguë).
3. **Garde de motifs**, sur l'invite entière telle qu'elle partirait ; elle doit être vide (code 4 sinon). L'outil ne
   nettoie jamais. Le journal et le message d'erreur donnent le nom du motif, le segment (consigne, balise ou pièce) et
   la ligne, **jamais le texte trouvé**. Motifs :
   - noms de personnes « Lazar », « Ciric » : sous-chaîne, sans casse ni accent (« Ćirić » est pris ; « Lazarus » aussi,
     faux positif accepté par prudence) ;
   - identifiant de session `session[_-][0-9A-Za-z]{20,}`, sans casse (v2, C5) ; identifiant au format UUID (v2, C5) ;
     adresse de courriel ; les caractères invisibles (catégorie Unicode Cf, par exemple l'espace sans chasse) sont
     retirés de la ligne avant toute recherche (v2, C5) ;
   - partout, sans casse ni accent, séparateurs « - », « _ » ou espace admis : « consigne-privee »,
     « conception-ii-b » (v2, C5 : « . », « ( », « ) » admis aussi comme séparateurs, et plus de garde arrière, donc
     `conception-ii-b1-v1.md` est pris), « donnees/ » (donc aussi « données/ ») ;
   - « verite », « rendu », « scores » **dans un chemin ou un nom** : jeton qui contient « / », « \ », « _ », « - » ou
     finit par une extension (`scores.json`, `rendu-v1.md`, `verite_dommage/…`, `vérité-cachée.md`), ou texte entre
     accents graves (`` `rendu` ``). Le mot seul dans la prose (« le rendu est bon », « les scores montent », « la
     vérité du dommage ») passe : lecture retenue de « un chemin ou nom contenant » ; sans elle, presque toute
     correction en français serait refusée. **Point à trancher par la mère** (voir § 6).
4. **Sorties neuves.** Refus (code 9) si `relecture-fable-api.md`, `compteurs.json`, le fichier de texte partiel ou l'un
   de leurs compagnons `.sha256` existe déjà dans DOSSIER (v2, C3 : contrôle par `lexists`, compagnons écrits en mode
   « x ») : on n'écrase jamais (R12) ; un nouvel essai prend un nouveau dossier.
5. **Clé** lue dans la variable dont le nom est donné (nom contrôlé : majuscules, chiffres, « _ ») ; jamais affichée,
   jamais écrite, masquée dans tout message d'erreur ; absente : refus (code 6). `--espace` : envoyé seulement s'il est
   donné (paramètre `workspace_id` du kit, en-tête `anthropic-workspace-id`) ; demandé et absent : refus.
6. **Pire coût et plafond.** Entrée comptée par `messages.count_tokens` (même modèle, même message, même réglage ; appel
   gratuit, distinct de l'appel de génération), garde ⌈n × 1,01⌉ + 32 ; si le comptage
   échoue, pour quelque raison que ce soit : refus (code 10), rien n'est envoyé ; clé refusée au
   comptage : arrêt, rien n'est envoyé (code 8). Sortie comptée au maximum demandé. Refus (code 5) si le cumul des
   `cout_compte_usd` du journal plus ce pire dépasse `--plafond-ligne`. Journal illisible ou dossier du journal absent :
   refus (pas de cumul nul silencieux).
7. **Un seul envoi**, en flux (`client.messages.stream` puis `get_final_message()`), au modèle `claude-fable-5-2`,
   `output_config.effort` donné par `--effort` (v3 ; valeurs fermées low, medium, high, xhigh, max ; défaut `high`),
   `thinking = {type: "adaptive", display: "omitted"}`,
   `max_tokens` 128 000 par défaut (le plafond du modèle). Client : clé explicite (aucune variable d'identité de
   l'environnement n'est lue), `max_retries=0`, délai de lecture d'une heure entre deux morceaux, sans traces. Aucun
   paramètre `fallbacks`.
8. **Défauts, jamais une réponse** : erreur d'envoi ou flux coupé (code 8), clé refusée (code 8), usage absent, arrêt en
   `max_tokens`, `refusal` (catégorie consignée), toute autre raison d'arrêt que `end_turn`, modèle servi autre que
   celui demandé, texte vide (code 7). Ligne `defaut` au journal ; `compteurs.json` (statut « defaut ») ; le texte
   partiel éventuel est gardé dans `defaut-texte-partiel-PAS-UNE-RELECTURE.md`, en-tête qui le dit (récupérer ce qui est
   récupérable), jamais dans `relecture-fable-api.md`. v2, C6 : une interruption pendant l'envoi (Ctrl-C, ou SIGTERM,
   changé en interruption le temps de l'envoi puis rendu à son gestionnaire d'avant) est consignée au journal, statut
   « defaut », au pire, avant que l'interruption ne remonte ; SIGKILL ou coupure de la machine restent hors d'atteinte.
9. **Réponse saine** : ligne `reponse` au journal **d'abord** (la dépense est consignée avant toute écriture), puis
   `relecture-fable-api.md` (en-tête : outil et empreinte du module, modèle demandé et servi, identifiant du message,
   heure UTC, réglages, chaque entrée avec rôle, chemin, empreinte et état du compagnon, empreinte de l'invite, jetons
   d'entrée, de sortie et de réflexion, raison d'arrêt, coût compté et base) et son compagnon, `compteurs.json` et son
   compagnon. Le texte de la réflexion n'est ni demandé (`display: "omitted"`) ni lu ni écrit : seuls les blocs `text`
   sont gardés.

**Coût compté** : usage lu (entrée × 8 + sortie × 40, USD par million ; la réflexion est dans la sortie ; écriture de
cache × 2 et lecture à 0,20 par prudence, aucune mise en cache n'étant demandée) ; « pire » (le pire cas d'avant l'envoi)
pour une coupure, une erreur 5xx, un délai dépassé, une erreur dans le flux ou un imprévu ; « zero » pour un refus 4xx
avant traitement ou une connexion impossible avant l'ouverture.

**Ligne de journal** (JSON Lines) : `heure_utc`, outil et empreinte du module, modèle, effort, réflexion, `max_tokens`,
fumée, plafond, entrées (rôle, chemin, empreinte, compagnon), empreinte et taille de l'invite, entrée comptée, garde et
source, pire, cumul d'avant, `envoye`, statut, défaut, modèle servi, identifiants du message et de la requête, raison
d'arrêt, catégorie de refus, jetons (entrée, sortie, réflexion, cache), coût compté et base, empreinte de la relecture.

## 3. Sources des réglages

Compétence « claude-api » de Claude Code, chargée le 21 novembre 2026 (table des modèles mise en cache le 2026-11-03,
section « Claude Fable 5.2 », tableau « Thinking & Effort », fichiers `python/claude-api/README.md`,
`python/claude-api/streaming.md`, `shared/token-counting.md`, `shared/cost-optimization.md`) : identifiant
`claude-fable-5-2` ; 128K de sortie au plus ; **8 USD par million de jetons d'entrée, 40 en sortie**, lectures de cache
0,20 ; réflexion toujours active, `adaptive` ou omise, `disabled` et `budget_tokens` refusés (400) ; effort de `low` à
`max` ; affichage `omitted` par défaut ; `refusal` possible ; `usage.output_tokens_details.thinking_tokens` ; comptage
par `messages.count_tokens`. Le catalogue du collisionneur (`collisionneur_v9_v8c.py`, lignes 309-311) porte 10 / 50 :
la compétence est retenue (ordre de la mère) ; 10 / 50 serait plus prudent de 25 %.

Kit Python d'Anthropic : `anthropic` 2.12.0, **installé ce jour dans `.venv`** (absent jusque-là ; voir § 6), version
d'interface `2026-10-21` ; il envoie la clé en `Authorization: Bearer …` (et non `x-api-key`), ce qu'ont montré le faux
serveur local et l'appel réel (accepté).

## 4. Essais

`PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_relecture_fable_api_v3.py -p no:cacheprovider
--basetemp=<dossier temporaire neuf>` : **95 passés** (les 76 de la v2, deux attentes d'effort passées de `max` à `high`,
et 19 neufs pour l'effort, § 8). Rejoués le même jour sur des dossiers neufs : v1 60 passés, v2 76 passés, v3 95 passés.

Chaque garde sur un cas sain et un artefact (R5) :

| Garde | Artefact (refusé, rien n'est envoyé) | Sain (envoyé) |
|---|---|---|
| motifs | 23 lignes : Lazar, LAZAR, Ciric, Ćirić, « La\u200bzar » (espace sans chasse U+200B) (v2), identifiant de session (aussi en majuscules et avec « - », v2), identifiant UUID (v2), courriel, consigne-privee (trois graphies), conception-ii-b (aussi `conception-ii-b1-v1.md`, v2), verite / vérité dans un chemin, rendu dans un chemin et entre accents graves, scores dans un nom de fichier et entre accents graves, donnees/ et données/ ; motif dans le chemin de la pièce ; motif dans la consigne | 7 lignes de prose (rendu, scores, vérité, `session_court`, `a@b`, « rendu. ») ; pièce `piece-v1.md` |
| empreinte | compagnon inégal ; compagnon mal formé ; pièce absente ; pièce contenant `</piece>` | compagnons égaux ; sans compagnon (déclaré « absent ») |
| plafond | pire 5,12 USD > 0,10 ; cumul du journal + pire > plafond ; journal illisible ; dossier du journal absent | journal vide, fumée à 2 000 jetons sous 0,10 |
| comptage | clé refusée au comptage : arrêt sans envoi ; comptage impossible ou exception imprévue au comptage : refus, code 10, rien envoyé, secret masqué (v2, C1) ; 500 au comptage par le vrai kit : une seule requête, refus (v2) | comptage sain : envoi |
| réponse | texte vide ; `max_tokens` (texte partiel gardé à part) ; `refusal` (catégorie) ; `stop_sequence`, `pause_turn`, `tool_use`, raison absente (v2, C2) ; modèle servi autre ; usage absent ; erreur après envoi (au pire, clé masquée) ; exception imprévue (au pire) ; Ctrl-C et SIGTERM pendant l'envoi (au pire, consignés, gestionnaire de SIGTERM rendu ; v2, C6) | `end_turn` avec texte |
| ordre | journal écrit avant chaque sortie, sur le chemin sain et sur celui d'un défaut (v2, C4) | — |
| clé | variable absente ; nom de variable mal formé ; espace demandé et absent | clé présente ; espace présent envoyé |
| sortie | relecture déjà présente, jamais écrasée ; compagnon orphelin `relecture-fable-api.md.sha256` ou `compteurs.json.sha256`, jamais écrasé (v2, C3) | dossier neuf |
| `--max-sortie` | 2 000 hors fumée | 64 000 hors fumée ; 2 000 en fumée, marquée |
| `--effort` (v3) | `MAX`, `maximum`, vide, `ultra`, `high ` (espace), `none`, `disabled` refusés par l'analyseur ; `MAX`, `ultra`, absent refusés par `relire` sans envoi, ligne au journal ; `--budget-reflexion 16000` et `0` refusés (option inconnue) | low, medium, high, xhigh, max : chacun envoyé, consigné au journal, aux compteurs et à l'en-tête, pire inchangé ; défaut `high` ; par le vrai kit, `medium` porté par le comptage et la génération |

Chemin réel du kit, contre un faux serveur local (127.0.0.1, sans mandataire) : flux sain (deux requêtes exactement,
comptage puis génération ; corps : modèle, `stream`, `max_tokens`, effort `max`, réflexion adaptative, aucun
`fallbacks` ; en-tête d'autorisation, `x-stainless-retry-count: 0`, pas d'en-tête d'espace ; jetons dont réflexion lus ;
coût) ; 401 au comptage (une seule requête, aucune relance, rien envoyé) ; 500 à la génération (aucune relance, compté au
pire) ; 400 (compté zéro) ; erreur dans le flux après le début (compté au pire, aucune relecture écrite) ; espace envoyé
en en-tête aux deux requêtes. Le secret d'essai n'apparaît dans aucun fichier écrit ni sur la sortie.

Suite complète du dépôt non lancée (seul le fichier d'essais demandé l'a été).

## 5. Appel de fumée (un seul, réel, fait avec la v1)

L'appel de fumée a été fait avec la v1 (module `056bc4ef…`) ; la v2 n'a fait aucun appel réel. Un appel de fumée de la
v2 est à décider par la mère (un appel, sous le même GO).

Commande (clé `RR_ANTHROPIC_API_KEY_MINUIT` par son nom, sans espace de travail, plafond 0,10 USD, `GO_ID` du
GO-2026-11-21-84 en tête pour la traçabilité) : consigne « Appel de fumée. Réponds seulement : OK », une pièce d'une
ligne, des remarques d'une ligne (l'outil exige au moins un `--remarques`), `--fumee --max-sortie 2200`.

| Compteur | Valeur |
|---|---|
| heure (UTC) | 2026-11-21T20:49:22Z |
| modèle demandé / servi | `claude-fable-5-2` / `claude-fable-5-2` |
| identifiant du message / de la requête | `msg_011ChGjQasMy7XbEi66PEpHJ` / `req_011ChGjQa7DtvoBq6aCzRPx8` |
| entrée comptée avant l'envoi / garde / facturée | 273 / 308 / 273 |
| sortie (dont réflexion) | 45 (41) |
| raison d'arrêt | `end_turn` |
| texte | « OK » |
| pire d'avant l'envoi | 0,090464 USD |
| **coût compté** | **0,003984 USD** (273 × 8 + 45 × 40, par million) |
| empreinte de l'invite | `3339076d…` |
| empreinte de la sortie | `eb3535b7…` (compagnon vérifié par `sha256sum -c`) |
| empreinte du module au moment de l'appel | `056bc4ef…` (le module n'a pas changé depuis) |

La clé a été acceptée ; le comptage et la génération sont passés par le mandataire de l'environnement sans réglage.

## 6. Limites et réserves

1. **Comptage échoué : refus.** L'appel de fumée a
   donné 1,76 caractère par jeton (480 caractères, 273 jetons) ; la borne de repli de 2,5 de la v1 sous-comptait l'entrée.
   La v2 refuse l'envoi si le comptage échoue, pour quelque raison que ce soit (code 10, ligne `refus_avant_envoi` à coût
   nul) ; il n'y a plus de borne de repli.
2. **« 32 000 jetons de texte au-delà de la réflexion » n'est pas garanti** : Fable 5.2 n'admet aucun budget de
   réflexion (§ 8). Le défaut `max_tokens` 128 000 (le plafond du modèle) ne le tient que si la réflexion reste sous
   96 000 ; hors fumée, `--max-sortie` est refusé sous 64 000. Un arrêt en `max_tokens` reste un défaut. Pire cas d'une
   relecture : environ 5,12 USD de sortie plus l'entrée ; le plafond de ligne doit le couvrir. Défaut constaté sur la v2
   à l'effort `max` (rapport de la mère) : la réflexion a pris toute la sortie sur deux lots (128 000 et 96 000 jetons,
   aucun texte, 11,68 USD perdus) et 95 000 à 115 000 jetons sur les trois relectures réussies ; la v3 passe le défaut à
   `high`, sans garantie : seul l'effort règle la profondeur, et l'effet de `high` sur nos relectures n'est pas mesuré.
3. **Aucun repli serveur (`fallbacks`)**, contre le défaut de la compétence, à dessein : une relecture servie par un
   autre modèle ne serait pas celle de Fable ; un refus est un défaut.
4. **Lecture de la garde pour « verite », « rendu », « scores »** : refusés dans un chemin ou un nom (jeton à séparateur
   ou extension, ou texte entre accents graves), non dans la prose. Si la mère veut les refuser partout, c'est une
   ligne à changer (v3), au prix de refuser presque toute correction en français ; la contre-lecture juge cette lecture
   bonne. Les noms sont cherchés en sous-chaîne (« Lazarus », « Lazare » refusés), et « compte-rendu » avec trait
   d'union est refusé : prévoir des copies nettoyées.
5. **Kit `anthropic` 2.12.0 installé dans `.venv`** pour cet outil (la compétence demande le kit officiel en Python) ;
   il n'est pas inscrit dans `requirements-cpu.txt`, laissé tel quel en v2 (la contre-lecture ne demande pas de le
   changer ; elle le signale comme à inscrire par la mère) : une machine neuve doit `pip install anthropic==2.12.0`.
6. **5xx et 529 comptés au pire** (aucune pièce n'établit qu'ils ne sont pas facturés) : un tel échec consomme le pire
   cas du plafond de la ligne et peut bloquer un second essai sous le même plafond ; c'est voulu (prudence), à savoir.
7. Le comptage est un appel distinct, gratuit, fait avant l'envoi ; « un seul appel par commande » s'entend de la
   génération.
8. Chemins affichés relatifs au dossier courant : lancer l'outil depuis la racine du dépôt, sinon les chemins absolus
   partent dans l'invite (la garde les contrôle aussi).
9. Pièce de classe B : la v1 a été contre-lue (verdict « à corriger ») ; la v2 applique les sept corrections ; la v2 et
   la v3 restent à faire vérifier par le même contre-lecteur.
10. Le cumul ne garde pas deux commandes lancées en même temps sur le même journal : en lancer une à la fois.
    L'entrée facturée peut dépasser la garde ⌈n × 1,01⌉ + 32 (marqué `entree_au_dela_de_la_garde`, non essayé).

## 7. Corrections de la v2 (contre-lecture, C1 à C7)

| Correction | Ce qui change |
|---|---|
| C1 | comptage échoué, pour quelque raison que ce soit : refus (code 10), rien n'est envoyé ; borne de repli retirée |
| C2 | essai des raisons d'arrêt autres que `end_turn`, `max_tokens` et `refusal` |
| C3 | compagnons `.sha256` contrôlés avant l'envoi et écrits en mode « x » : jamais écrasés |
| C4 | essai de l'ordre « journal avant toute sortie » |
| C5 | garde : identifiant de session sans casse et avec « - », UUID, caractères invisibles retirés, `conception-ii-b` élargi |
| C6 | interruption (Ctrl-C, SIGTERM) pendant l'envoi : consignée au pire avant la sortie |
| C7 | refus non consigné au journal : avertissement, jamais de silence |

Remarques de la contre-lecture sans correction demandée (noms en cyrillique, `ANTHROPIC_CUSTOM_HEADERS`, journal qui
échoue après un envoi payé, kit à inscrire dans la liste des dépendances, fumée de la v2) : non appliquées, à la mère.

## 8. Changements de la v3 (option d'effort ; aucun budget de réflexion)

Copie de `relecture_fable_api_v2.py` (c8e8506f…, inchangée). Changements, et seulement ceux-là :

1. **`--effort`**, valeurs fermées `low`, `medium`, `high`, `xhigh`, `max`, défaut `high`. Source : compétence
   « claude-api », `shared/model-migration.md`, « Migrating to Claude Fable 5.2 », « Choosing an effort level - start at
   `high`, and re-run the sweep » : « All five levels are supported and the default is `high` » ; « Most of the
   capability gain arrives by `high` […] gains above `high` are uneven » ; `xhigh` « used many more tokens » ; `max`
   « Turns are slow and use many more tokens than at `xhigh` ». Valeur hors liste : refus de l'analyseur (code 2), et
   refus de `relire` avant tout envoi (code 2, ligne `refus_avant_envoi`) si elle lui parvient autrement. L'effort est
   envoyé au comptage et à la génération.
2. **Aucune option de budget de réflexion : la compétence ne permet pas de borner la réflexion de `claude-fable-5-2`.**
   Ce qu'elle dit :
   - tableau « Thinking & Effort » de SKILL.md, ligne Fable 5 / 5.1 / 5.2 : `budget_tokens` « Removed -
     `{type: "enabled", budget_tokens: N}` returns 400 » ; `{type: "disabled"}` aussi refusé ;
   - section « Claude Fable 5.2 » : « Thinking is always on […] Control depth with `output_config.effort` » ;
   - « Migrating to Claude Fable 5.2 » : `max_tokens` « is a hard limit on total output (thinking plus response text) » ;
     une demande à petit `max_tokens` « can now stop with `stop_reason: "max_tokens"` after a `thinking` block and before
     any text » ; les consignes de penser moins « don't work at `medium` and above » ;
   - budgets de tâche (`output_config.task_budget`, bêta `task-budgets-2026-03-13`, Fable 5.2 compris, au moins
     20 000) : « a **suggestion the model is aware of**, not a hard cap » (« New feature: Task Budgets (beta) ») ; ils
     comptent réflexion et texte ensemble et ne garantissent aucun nombre de jetons de texte ; non employés.
   Aucun réglage documenté ne garantit donc 16 000 jetons de texte sous `max_tokens`. L'option `--budget-reflexion`
   n'existe pas ; l'analyseur la refuse (option inconnue, code 2), essais à l'appui.
3. **Pire coût et journal inchangés** : le pire reste ⌈entrée comptée × 1,01⌉ + 32 au prix d'entrée plus `max_tokens`
   au prix de sortie, quel que soit l'effort ; les champs du journal sont les mêmes, `effort` porte l'effort demandé
   (aussi dans `compteurs.json` et l'en-tête de la relecture).
4. **Essais** (19 neufs ; deux attentes d'effort de la v2 passées de `max` à `high`) : chaque valeur admise sur un cas
   sain ; sept valeurs refusées par l'analyseur, trois par `relire` ; défaut `high` ; `--budget-reflexion` refusé ;
   effort porté par les deux requêtes du vrai kit contre le faux serveur local. Mutations essayées dans une copie (témoin
   95 passés) : contrôle de `relire` retiré (3 échecs), défaut remis à `max` (3 échecs), effort figé à `high` dans la
   requête (5 échecs) ; toutes tuées.

Aucun appel réel n'a été fait avec la v3.
