# Relecture d'une correction par Fable 5.2 appelé par l'interface d'Anthropic — rapport du développeur, v1

Développeur neuf, Claude Opus 5.5, 21 novembre 2026. Pièce d'instrument (classe B) : à contre-lire par un autre modèle,
puis vérification des corrections par le même contre-lecteur. Ordre de la mère, pour la décision de Lazar
GO-2026-11-21-84 (Fable à sa limite d'usage dans Claude Code jusqu'au 24 novembre 05:00Z : les corrections sont écrites
par Opus, relues par Fable 5.2 appelé directement par l'interface d'Anthropic, puis scellées).

## 1. Fichiers

| Fichier | Rôle |
|---|---|
| `src/controle_ia/relecture_fable_api_v1.py` | l'outil (`python -m controle_ia.relecture_fable_api_v1 relire …`) |
| `tests/test_relecture_fable_api_v1.py` | 60 essais sans réseau |
| `docs/notes/relecture-fable-api-v1/fumee-v1/` | entrées de l'appel de fumée (consigne, pièce, remarques) et sa sortie (`sortie/`) |
| `docs/notes/relecture-fable-api-v1/journal-depense-fumee-v1.jsonl` | journal de dépense de l'appel de fumée (une ligne) |

Chaque fichier neuf a son compagnon `.sha256` ; les empreintes sont dans le rendu de la session à la mère.

## 2. Ce que fait l'outil

Commande :

```
python -m controle_ia.relecture_fable_api_v1 relire --piece P [--piece P2 …] --remarques R [--remarques R2 …]
    [--avant V] --consigne C --sortie DOSSIER --cle NOM_DE_VARIABLE [--espace NOM_DE_VARIABLE]
    --plafond-ligne USD --journal-depense FICHIER [--max-sortie N] [--fumee]
```

Dans cet ordre ; tout refus arrête l'outil **avant l'envoi**, code non nul, une ligne `refus_avant_envoi` au journal
(coût 0) :

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
   - identifiant de session `session_[0-9A-Za-z]{20,}` ; adresse de courriel ;
   - partout, sans casse ni accent, séparateurs « - », « _ » ou espace admis : « consigne-privee »,
     « conception-ii-b », « donnees/ » (donc aussi « données/ ») ;
   - « verite », « rendu », « scores » **dans un chemin ou un nom** : jeton qui contient « / », « \ », « _ », « - » ou
     finit par une extension (`scores.json`, `rendu-v1.md`, `verite_dommage/…`, `vérité-cachée.md`), ou texte entre
     accents graves (`` `rendu` ``). Le mot seul dans la prose (« le rendu est bon », « les scores montent », « la
     vérité du dommage ») passe : lecture retenue de « un chemin ou nom contenant » ; sans elle, presque toute
     correction en français serait refusée. **Point à trancher par la mère** (voir § 6).
4. **Sorties neuves.** Refus (code 9) si `relecture-fable-api.md`, `compteurs.json` ou le fichier de texte partiel existe
   déjà dans DOSSIER : on n'écrase jamais (R12) ; un nouvel essai prend un nouveau dossier.
5. **Clé** lue dans la variable dont le nom est donné (nom contrôlé : majuscules, chiffres, « _ ») ; jamais affichée,
   jamais écrite, masquée dans tout message d'erreur ; absente : refus (code 6). `--espace` : envoyé seulement s'il est
   donné (paramètre `workspace_id` du kit, en-tête `anthropic-workspace-id`) ; demandé et absent : refus.
6. **Pire coût et plafond.** Entrée comptée par `messages.count_tokens` (même modèle, même message, même réglage ; appel
   gratuit, distinct de l'appel de génération), garde ⌈n × 1,01⌉ + 32 ; si le comptage échoue autrement que par une clé
   refusée : borne déclarée de 1 jeton pour 2,5 caractères (avertissement, et source au journal) ; clé refusée au
   comptage : arrêt, rien n'est envoyé (code 8). Sortie comptée au maximum demandé. Refus (code 5) si le cumul des
   `cout_compte_usd` du journal plus ce pire dépasse `--plafond-ligne`. Journal illisible ou dossier du journal absent :
   refus (pas de cumul nul silencieux).
7. **Un seul envoi**, en flux (`client.messages.stream` puis `get_final_message()`), au modèle `claude-fable-5-2`,
   `output_config.effort = "max"` (le plus haut admis), `thinking = {type: "adaptive", display: "omitted"}`,
   `max_tokens` 128 000 par défaut (le plafond du modèle). Client : clé explicite (aucune variable d'identité de
   l'environnement n'est lue), `max_retries=0`, délai de lecture d'une heure entre deux morceaux, sans traces. Aucun
   paramètre `fallbacks`.
8. **Défauts, jamais une réponse** : erreur d'envoi ou flux coupé (code 8), clé refusée (code 8), usage absent, arrêt en
   `max_tokens`, `refusal` (catégorie consignée), toute autre raison d'arrêt que `end_turn`, modèle servi autre que
   celui demandé, texte vide (code 7). Ligne `defaut` au journal ; `compteurs.json` (statut « defaut ») ; le texte
   partiel éventuel est gardé dans `defaut-texte-partiel-PAS-UNE-RELECTURE.md`, en-tête qui le dit (récupérer ce qui est
   récupérable), jamais dans `relecture-fable-api.md`.
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

`PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_relecture_fable_api_v1.py -p no:cacheprovider
--basetemp=<dossier temporaire neuf>` : **60 passés** (3 essais de suite, dossiers neufs ; le dernier après le dernier
changement du module et des essais).

Chaque garde sur un cas sain et un artefact (R5) :

| Garde | Artefact (refusé, rien n'est envoyé) | Sain (envoyé) |
|---|---|---|
| motifs | 18 lignes : Lazar, LAZAR, Ciric, Ćirić, identifiant de session, courriel, consigne-privee (trois graphies), conception-ii-b, verite / vérité dans un chemin, rendu dans un chemin et entre accents graves, scores dans un nom de fichier et entre accents graves, donnees/ et données/ ; motif dans le chemin de la pièce ; motif dans la consigne | 7 lignes de prose (rendu, scores, vérité, `session_court`, `a@b`, « rendu. ») ; pièce `piece-v1.md` |
| empreinte | compagnon inégal ; compagnon mal formé ; pièce absente ; pièce contenant `</piece>` | compagnons égaux ; sans compagnon (déclaré « absent ») |
| plafond | pire 5,12 USD > 0,10 ; cumul du journal + pire > plafond ; journal illisible ; dossier du journal absent | journal vide, fumée à 2 000 jetons sous 0,10 |
| comptage | clé refusée au comptage : arrêt sans envoi | comptage impossible : borne déclarée, envoi |
| réponse | texte vide ; `max_tokens` (texte partiel gardé à part) ; `refusal` (catégorie) ; modèle servi autre ; usage absent ; erreur après envoi (au pire, clé masquée) ; exception imprévue (au pire) | `end_turn` avec texte |
| clé | variable absente ; nom de variable mal formé ; espace demandé et absent | clé présente ; espace présent envoyé |
| sortie | relecture déjà présente, jamais écrasée | dossier neuf |
| `--max-sortie` | 2 000 hors fumée | 64 000 hors fumée ; 2 000 en fumée, marquée |

Chemin réel du kit, contre un faux serveur local (127.0.0.1, sans mandataire) : flux sain (deux requêtes exactement,
comptage puis génération ; corps : modèle, `stream`, `max_tokens`, effort `max`, réflexion adaptative, aucun
`fallbacks` ; en-tête d'autorisation, `x-stainless-retry-count: 0`, pas d'en-tête d'espace ; jetons dont réflexion lus ;
coût) ; 401 au comptage (une seule requête, aucune relance, rien envoyé) ; 500 à la génération (aucune relance, compté au
pire) ; 400 (compté zéro) ; erreur dans le flux après le début (compté au pire, aucune relecture écrite) ; espace envoyé
en en-tête aux deux requêtes. Le secret d'essai n'apparaît dans aucun fichier écrit ni sur la sortie.

Suite complète du dépôt non lancée (seul le fichier d'essais demandé l'a été).

## 5. Appel de fumée (un seul, réel)

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

1. **Borne de repli de l'entrée non prudente.** L'appel de fumée a donné 480 caractères pour 273 jetons, soit
   1,76 caractère par jeton (empreintes de 64 caractères hexadécimaux) ; la borne de 2,5 demandée aurait sous-compté
   l'entrée. Elle ne sert que si le comptage échoue, et la sortie domine le pire cas ; mais elle n'est pas une borne.
   Le collisionneur relevait déjà 2,227 au plus bas. Une v2 pourrait refuser l'envoi quand le comptage échoue (comme le
   collisionneur v9-v3) ou prendre 1,5 ; à décider par la mère. L'entrée facturée au-delà de la garde est marquée au
   journal (`entree_au_dela_de_la_garde`).
2. **« 32 000 jetons de texte au-delà de la réflexion » n'est pas garanti** : Fable 5.2 n'admet aucun budget de
   réflexion. Le défaut `max_tokens` 128 000 (le plafond du modèle) ne le tient que si la réflexion reste sous 96 000 ;
   hors fumée, `--max-sortie` est refusé sous 64 000. Un arrêt en `max_tokens` reste un défaut. Pire cas d'une
   relecture : environ 5,12 USD de sortie plus l'entrée ; le plafond de ligne doit le couvrir.
3. **Aucun repli serveur (`fallbacks`)**, contre le défaut de la compétence, à dessein : une relecture servie par un
   autre modèle ne serait pas celle de Fable ; un refus est un défaut.
4. **Lecture de la garde pour « verite », « rendu », « scores »** : refusés dans un chemin ou un nom (jeton à séparateur
   ou extension, ou texte entre accents graves), non dans la prose. Si la mère veut les refuser partout, c'est une
   ligne à changer (v2), au prix de refuser presque toute correction en français. Les noms sont cherchés en
   sous-chaîne (« Lazarus », « Lazare » refusés).
5. **Kit `anthropic` 2.12.0 installé dans `.venv`** pour cet outil (la compétence demande le kit officiel en Python) ;
   il n'est pas inscrit dans `requirements-cpu.txt` (non touché) : une machine neuve doit `pip install anthropic`.
6. **5xx et 529 comptés au pire** (aucune pièce n'établit qu'ils ne sont pas facturés) : un tel échec consomme le pire
   cas du plafond de la ligne et peut bloquer un second essai sous le même plafond ; c'est voulu (prudence), à savoir.
7. Le comptage est un appel distinct, gratuit, fait avant l'envoi ; « un seul appel par commande » s'entend de la
   génération.
8. Chemins affichés relatifs au dossier courant : lancer l'outil depuis la racine du dépôt, sinon les chemins absolus
   partent dans l'invite (la garde les contrôle aussi).
9. Pièce de classe B non encore contre-lue par un autre modèle.
