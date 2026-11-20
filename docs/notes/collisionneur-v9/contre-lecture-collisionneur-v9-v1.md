# Contre-lecture du collisionneur v9, version 1

Écrite le 20 novembre 2026 par un contre-lecteur neuf (Claude Fable 5.2, identifiant `claude-fable-5-2`), autre modèle que le développeur (Claude Opus 5.5). Pièce de classe B (instrument). Aucun appel à un fournisseur de modèle, aucune dépense, aucun commit, aucun autre fichier du dépôt modifié.

## Verdict

**Conforme après ces corrections.** Quatre corrections sont bloquantes : deux trous de la garde de dépense (B1, B4), des fuites possibles à travers la garde de motifs (B2) et un refus à tort de cette garde sur une écriture mathématique courante (B3). Le reste du script fait ce que le rapport dit. Les 73 essais passent. Les neuf couples ci-dessous, appliqués à une copie, laissent les 73 essais passer et ferment les trous montrés.

Pièces relues, empreintes recalculées et égales aux compagnons :

| fichier | empreinte |
|---|---|
| `collisionneur_v9_v1.py` | `977d416682daeff04d8c252f5b31e47b04ecb52440b90c0602d3d07080e055b7` |
| `test_collisionneur_v9_v1.py` | `81e2572cfe387a955f0561a9721a302ee4e23596a4ed80504cf1426d0426252b` |
| `rapport-developpeur-collisionneur-v9-v1.md` | `8ba7eb0956590bb3da01542abc8e6158c02c1b6c1197c5b42445fd8ca1ef2d19` |
| point de départ, `collisionneur_v8_plafonds_bas_v1.py` | `4ad78ccce8228aed2679c854eaec7ee4d2ab8f867098218387024adfeb1e7756` |

## Corrections bloquantes

### B1. Chez Anthropic, une sortie non lue est comptée pour un jeton

Raison. Le script lit la sortie dans l'événement de début (`message_start`), où elle vaut un ou deux jetons, puis la remplace par la valeur cumulée de l'événement de fin (`message_delta`). Si cet événement ne porte pas d'usage, ou s'il manque, la valeur du début reste, et l'usage est déclaré lu. Démontré hors réseau : statut `OK`, coût compté 0,001 dollar, pour un pire cas de 1,11 dollar. La documentation publique montre un exemple de flux dont le `message_delta` n'a pas d'usage. Le rapport dit qu'un usage absent est compté au pire « pour toutes les espèces » : c'est faux dans ce cas.

Avant :
```python
    texte, types, etat = [], [], {"servi": None, "id": None, "fin": None, "categorie": None, "entree": None,
                                  "sortie": None, "fini": False}
```
Après :
```python
    texte, types, etat = [], [], {"servi": None, "id": None, "fin": None, "categorie": None, "entree": None,
                                  "sortie": None, "sortie_finale": False, "fini": False}
```
Avant :
```python
                    if entier(u.get("output_tokens")) is not None:
                        etat["sortie"] = u["output_tokens"]
```
Après :
```python
                    if entier(u.get("output_tokens")) is not None:
                        etat["sortie"], etat["sortie_finale"] = u["output_tokens"], True
```
Avant :
```python
    lu = etat["entree"] is not None and etat["sortie"] is not None
```
Après :
```python
    lu = etat["entree"] is not None and etat["sortie"] is not None and etat["sortie_finale"]
```
Essai à ajouter : un flux sain dont le `message_delta` n'a pas d'usage doit donner `USAGE_ABSENT`, coût égal au pire cas, code 6.

### B2. La garde de motifs laisse partir des formes du nom et des chemins du dépôt

Raison. Sonde hors réseau sur la copie. Passent sans refus : le prénom et le nom collés (« LazarCiric »), reliés par un tiret bas (« lazar_ciric »), le nom avec un seul des deux accents (« Ćiric », « Cirić »), le nom en accents décomposés, le nom en cyrillique. Passent aussi : tout chemin sous `docs/` hors de `docs/notes/` et `docs/decisions/` (par exemple `docs/sources/…`, `docs/sha256sums-lancement-v2.txt`), `runs/…`, `scripts/…`, et le nom `CLAUDE.md`. Les deux questions de version 3 ne sont refusées aujourd'hui que parce que le nom de leur fichier contient « controle-ia ».

Avant :
```python
    ("nom de personne", re.compile(r"(?i)(?<![\w])(?:lazar|ciric|ćirić|lciric|rigaud)(?![\w])")),
```
Après :
```python
    ("nom de personne", re.compile(r"(?i)(?<![^\W_])(?:lazar|лазар)(?![^\W_])"
                                   r"|(?:[cćč]|c[\u0300-\u036f])iri(?:[cćč]|c[\u0300-\u036f])|[ћч]ири[ћч]|rigaud")),
```
Le couple pour les chemins est celui de B3 (même ligne).

Essais à ajouter : un témoin par forme (collée, tiret bas, un seul accent, accents décomposés, `docs/sources/x`, `runs/x`, `scripts/x`, `CLAUDE.md`), et un témoin sain (« Lazarsfeld », une adresse publique qui contient `/docs/`).

Limite qui reste, à dire à Lazar : la liste des noms est fermée. Tout autre nom de personne (mentor, auteur d'un mot rapporté) passe. La mère doit la compléter, ou les questions doivent être relues à la main sur ce point.

### B3. La garde refuse à tort une écriture mathématique courante

Raison. Le motif de chemin de Windows (`\b[A-Za-z]:\\`) reconnaît toute lettre isolée suivie de deux-points et d'une barre oblique inversée. Or `$f:\mathbb{R}^d\to\mathbb{R}$` et `$T:\Omega\to\Omega$` s'écrivent ainsi. Les tours demandent des objets mathématiques et des lois de probabilité. Une cellule qui contient cette écriture ferait refuser, au tour suivant, l'envoi à toutes les autres espèces (code 7), après la dépense du premier tour. Elle arrêterait aussi l'audit de Jev, dont un échec ne doit pas arrêter le passage.

Avant :
```python
    ("chemin interne", re.compile(r"(?<![\w.])/(?:home|root|tmp|Users|mnt|srv|workspace)/|\b[A-Za-z]:\\|\.claude/"
                                  r"|\bcontrole-ia(?:-travail)?\b|\b(?:docs/notes|docs/decisions|registres|prereg|diag|"
                                  r"src/controle_ia|archives-reponses-modeles|livrables|papiers)/")),
```
Après :
```python
    ("chemin interne", re.compile(r"(?<![\w.])/(?:home|root|tmp|Users|mnt|srv|workspace)/"
                                  r"|\b[A-Za-z]:\\(?:Users|Windows|Documents and Settings|Program Files|ProgramData)\\"
                                  r"|\.claude/|\bCLAUDE\.md\b"
                                  r"|\bcontrole-ia(?:-travail)?\b|\b(?:docs/notes|docs/decisions|registres|prereg|diag|"
                                  r"src/controle_ia|archives-reponses-modeles|livrables|papiers)/"
                                  r"|(?<![\w/.-])(?:docs|runs|scripts)/")),
```
Essai à ajouter au témoin sain : les deux écritures mathématiques ci-dessus ne déclenchent rien.

### B4. Un envoi interrompu ou sans usage complet peut être compté sous ce que l'usage lu montre

Raison. Dans ces deux cas le script compte le pire cas, même quand l'usage partiel déjà lu coûte plus. Démontré hors réseau chez Argon : flux clos sans fin après 60 000 jetons de réflexion lus (provision 8 192) : compté 1,33 dollar, alors que l'usage lu vaut 3,02 dollars. Même chose quand seul le total manque. La condition (a) veut le coût réel quand la réflexion dépasse la provision.

Avant :
```python
    if rep.interrompue:
        return "INTERROMPU", pire
```
Après :
```python
    if rep.interrompue:
        return "INTERROMPU", max(pire, cout(m["prix"], rep.usage))
```
Avant :
```python
    if not rep.usage_lu:
        return "USAGE_ABSENT", pire
```
Après :
```python
    if not rep.usage_lu:
        return "USAGE_ABSENT", max(pire, cout(m["prix"], rep.usage))
```
Essai à ajouter : flux de Google clos sans raison de fin, avec un usage partiel plus cher que le pire cas ; le coût compté est celui de l'usage.

## Corrections non bloquantes

### C1. Jev : réponse sans usage comptée à zéro

Raison. Comportement hérité du v8, mais le rapport annonce le pire cas pour tout usage absent. Démontré : audit `OK` sans usage, 30 000 caractères, compté 0 au lieu de 0,10 dollar.

Avant :
```python
    cout_jev = pire if statut == "INTERROMPU" else (usage.get("input_tokens") or 0) / 1e6 * JEV["prix_entree"]
```
Après :
```python
    jetons_jev = entier(usage.get("input_tokens"))
    au_pire = statut == "INTERROMPU" or (statut != "ECHEC" and jetons_jev is None)
    cout_jev = pire if au_pire else (jetons_jev or 0) / 1e6 * JEV["prix_entree"]
```

### C2. Identifiant de session : forme nue non vue, mot courant refusé à tort

Raison. L'identifiant sans son préfixe (« 01 » suivi de 22 lettres ou chiffres) passe. À l'inverse, un nom de variable comme `session_embeddings` est refusé.

Avant :
```python
    ("identifiant de session", re.compile(r"(?i)\bsession_[0-9a-z]{8,}|claude\.ai/code/session")),
```
Après :
```python
    ("identifiant de session", re.compile(r"(?i)\bsession_(?=[0-9a-z]*\d)[0-9a-z]{8,}|claude\.ai/code/session"
                                          r"|(?<![0-9a-z])01[0-9a-z]{22}(?![0-9a-z])")),
```

### C3. Essais vides ou manquants (épreuves par retrait)

Dix retraits faits sur des copies. Six cassent au moins un essai. Quatre ne cassent rien :

1. Garde de motifs retirée de `verifier` : 73 essais passent. Ajouter un essai : un prompt archivé qui contient un motif donne un problème nommé.
2. Garde de motifs retirée de `jev-test` : 73 passent. Ajouter un essai, ou retirer cette garde, qui ne voit que deux textes fixes du script.
3. Restriction de l'adresse d'OpenAI retirée : 73 passent. Ajouter un essai : une adresse tierce dans `OPENAI_BASE_URL` donne un échec sans appel.
4. Jev interrompu compté à zéro au lieu du pire : 73 passent. L'essai `test_garde_c_jev_sans_renvoi_compte_au_pire_et_le_run_continue` est vide : son texte de 11 caractères donne un pire cas arrondi à 0. Avant : `"Texte sain."` (les deux fois). Après : un texte d'au moins 3 000 caractères, et `assert e["cout_usd"] > 0`.

### C4. Entrée gardée hors de Google : à trancher par Lazar

Constat. Hors de Google, l'entrée est comptée à 3 caractères par jeton et rien ne contrôle l'entrée facturée. Démontré : 3 000 jetons facturés pour 4 000 caractères chez Fable, statut `OK`, aucun signal. Le pire cas n'est donc pas une borne de l'entrée pour Fable, Opus, Astra et Kimi. L'écart reste petit : au plus long tour, l'entrée de Fable vaut 0,48 dollar. Options : (a) étendre le contrôle `ENTREE_HORS_GARDE` à toutes les espèces et garder 3 ; risque d'arrêts si le français dépasse un jeton pour 3 caractères ; (b) passer toutes les espèces à 2,5 et étendre le contrôle ; le devis monte un peu ; (c) laisser et l'écrire au devis. Recommandation : (b). Ce choix change un réglage du devis : il appartient à Lazar.

### C5. Adresse locale reconnue par son début seulement (hérité du v8)

`OPENAI_BASE_URL` et `KIMI_RELAIS_URL` sont acceptées si elles commencent par `http://127.0.0.1:` ou `http://localhost:`. Une adresse de la forme `http://127.0.0.1:1@tiers.exemple/` commence ainsi et désigne un tiers ; la clé d'OpenAI y partirait. Ces variables sont posées par l'opérateur, et le v8 avait déjà ce défaut. À corriger dans une version suivante : comparer le nom d'hôte rendu par `urllib.parse.urlsplit` à `127.0.0.1` ou `localhost`.

### C6. Errata du rapport du développeur

- Point 4 : « Un usage absent ou mal formé donne `USAGE_ABSENT` […] pour toutes les espèces » : faux chez Anthropic avant B1, et Jev n'est pas couvert avant C1.
- Changements non listés, sans effet sur la mesure : l'exemple retiré de la description de l'étage III ; le corps envoyé à Google écrit sans échappement des caractères accentués ; les lignes d'espèces en tête de la sortie de `devis` ; la branche `AUCUN_CHOIX` de `statut_reponse`, qui n'est plus atteinte.

## Ce qui a été vérifié

### 1. Garde de dépense

Pire cas recalculé à la main, puis comparé au script : égal à six décimales pour les six espèces. Prompt de 144 478 caractères (faits 7 989, 6 000, question 7 989, cinq pièces de 3 500 mots à 7 caractères).

| espèce | entrée gardée (jetons) | calcul du premier essai | premier essai | relance |
|---|---|---|---|---|
| Fable 5.2 | 48 159,33 | 0,481593 + 22 000 × 50 ÷ 10⁶ | 1,581593 | 3,681593 |
| Opus 5.5 | 48 159,33 | 0,192637 + 22 000 × 20 ÷ 10⁶ | 0,632637 | 1,472637 |
| Argon | 57 791,2 | 0,577912 + (18 000 + 8 192) × 50 ÷ 10⁶ | 1,887512 | 2,587512 |
| Kimi | 48 159,33 | 0,096319 + 32 000 × 10 ÷ 10⁶ | 0,416319 | 0,751679 |
| Astra | 48 159,33 | 0,481593 + 8 000 × 50 ÷ 10⁶ | 0,881593 | 2,081593 |
| Carbon | 57 791,2 | 0,231165 + (65 536 + 32 768) × 20 ÷ 10⁶ | 2,197245 | 2,197245 |

- Réflexion de Google : budget posé, provision comptée avant l'envoi, arrêt avec coût réel si la réflexion rendue dépasse la provision. Tient, sous B4 pour le flux interrompu.
- Total des jetons : lu ; écart positif compté au prix de sortie et arrêt ; total absent compté au pire. Tient, sous B4.
- Entrée à 2,5 caractères par jeton : tient chez Google (contrôle après coup, coût réel compté). Hors de Google : voir C4.
- Aucun renvoi silencieux : tient. Seule l'erreur 429 est reprise. Délai, coupure, erreurs 502, 503 et 504, erreur dans le flux, flux sans fin : un seul envoi, compté au pire, arrêt. Les relevés d'OpenAI sont des lectures, pas des renvois. L'annulation part une fois. Un opérateur qui relance la commande renvoie la cellule interrompue : c'est son geste, pas celui du script.
- Délais : explicites par espèce ; 600 secondes au plus entre deux morceaux d'un flux ; le délai total n'est contrôlé qu'à l'arrivée d'un morceau, donc dépassé de 600 secondes au plus. Tient.
- Plafonds de sortie : chez Anthropic et chez OpenAI, la documentation dit que le plafond comprend la réflexion. Le pire cas y est donc une borne de la sortie.

### 2. Formes des appels, relues sur la documentation publique

Anthropic, flux continu. Conformes : `"stream": true`, en-têtes `x-api-key`, `anthropic-version` et `content-type`, ordre des événements, usage cumulé dans `message_delta`, événement `error` dans le flux, événements `ping` ignorés, `stop_reason` « refusal » avec `stop_details.category`, effort dans `output_config`, pas de réglage de réflexion. Différences : (i) les exemples publics portent la version `2026-10-21` ; le script envoie `2023-06-01`, encore acceptée ; rien à changer, à savoir ; (ii) un exemple public montre un `message_delta` sans usage, d'où B1 ; (iii) la place de `stop_details` dans le flux n'est pas montrée ; le script lit les deux places possibles ; (iv) un refus avant toute sortie est facturé pour certaines catégories : le script compte l'usage rendu, ce qui convient ; (v) l'en-tête d'espace de travail, hérité du v8, n'a pas été retrouvé dans les pages lues.

Google, flux continu. Conformes : chemin `…:streamGenerateContent`, champs `thinkingConfig` (`thinkingBudget`, `includeThoughts`), marque `thought` des parties, champs de l'usage, définition du total (entrée, outil, réflexion, réponse), raisons de fin et de blocage. Différences : (i) la page publique sur la réflexion ne décrit plus que le niveau de réflexion (`thinking_level` ; bas, moyen, haut pour Carbon et Argon, moyen par défaut) et une interface plus récente ; `thinkingBudget` reste dans la référence de l'ancienne interface, sans liste des modèles qui l'acceptent ; (ii) le seul appel réel à Carbon de ce dépôt (`appel-carbon-v1.json`) est passé avec le niveau « high » ; le budget n'y a pas été essayé ; un refus du budget donnerait une erreur 400, comptée à zéro, sans repli : c'est sain, mais le passage ne partirait pas ; (iii) la page dit que le plafond de sortie comprend la réflexion et coupe net ; la leçon du dépôt dit l'inverse pour Argon ; le pire cas du script couvre les deux lectures ; (iv) sortie d'un appel en flux de Carbon ou d'Argon : 65 536 jetons au plus, ce qui convient au réglage ; (v) raisons de refus nouvelles (`IMAGE_PROHIBITED_CONTENT`, par exemple) absentes de la liste du script : elles donnent `ANOMALIE`, sans relance.

OpenAI, arrière-plan et relevés. Conformes : `background`, lecture par `GET /v1/responses/{id}`, annulation par `POST /v1/responses/{id}/cancel` (sans effet la seconde fois), statuts (`queued`, `in_progress`, `completed`, `incomplete`, `failed`, `cancelled`), raisons d'une réponse incomplète, champs de l'usage, forme des sorties et du refus. Différences : (i) `store` n'est pas exigé ; l'envoyer ne gêne pas ; (ii) le plafond de sortie comprend le raisonnement, et le compte de sortie aussi : le script ajoute le raisonnement une seconde fois ; c'est prudent, mais le coût compté d'Astra est surévalué et le plafond du passage peut se déclencher plus tôt ; (iii) deux raisons nouvelles (`max_messages`, `steered`) donnent `ANOMALIE`, sans relance ; (iv) aucune page lue ne dit ce que coûte une réponse annulée : le pire cas compté convient.

Les identifiants `gemini-4-carbon` et `gemini-4-argon` figurent sur la page publique de Google. Je n'ai pas vérifié `gpt-6.2-astra` ni `kimi-k3.1-pro` sur une page publique. Les prix d'Anthropic lus dans la référence fournie à cette session (8 et 40 pour Fable 5.2, 4 et 20 pour Opus 5.5) concordent avec la table.

### 3. Garde de motifs

- Passe avant chaque envoi d'une cellule et de Jev ; aucun autre texte ne part (les relevés et l'annulation d'OpenAI ne portent que l'identifiant de la réponse). Le prompt refusé n'est pas archivé.
- Refus nommé : catégorie et position, jamais le texte trouvé ; rien n'est retiré du texte ; le refus est consigné.
- Témoins positifs : un par catégorie, sept sur sept, et chacun casse si la garde est retirée.
- Trous et refus à tort : B2, B3, C2. Autres refus à tort possibles, rares, laissés : `diag/` dans une formule, « R-100 » comme nom de modèle.
- À savoir : la garde lit aussi les cellules des modèles quand elles sont injectées au tour suivant. Une adresse de courriel ou un chemin `/tmp/` écrit par un modèle arrête le passage (code 7). C'est l'exigence ; la décision revient alors à l'arbitre.

### 4. Rien d'autre ne change

Différence relue ligne à ligne entre le v8 et le v9. Tours, rôles, consignes, injection des pièces, portes, relance unique, refus, format des sorties et `verifier` sont inchangés, hors les points du rapport et les quatre points de C6. Le préambule ne porte plus de nom.

### 5. Rejeu

Copie dans le bloc-notes, empreintes égales. 73 essais passés sur l'original et sur la copie. Dix épreuves par retrait : six cassent, quatre non (C3). Corrections appliquées à une copie : 73 essais passés, sondes relancées, trous fermés.

Outils et sorties, dans `/tmp/claude-0/-home-user-controle-ia-travail/fc9e4fb9-7931-58b9-a66b-caf66718eee3/scratchpad/contre-lecture-collisionneur-v9/` (bloc-notes, non durable) : `outils/sonde_motifs.py` (`a92475cd…`), `outils/sonde_depense.py` (`047d0a95…`), `outils/epreuves_retrait.py` (`878f31c6…`), `outils/appliquer_corrections.py` (`28b1e935…`), copie corrigée `corrige/collisionneur_v9_v1.py` (`6ec86d08…`).

## Réserves du développeur : avis

- Questions de version 3 refusées par la garde : confirmé, et la garde corrigée les refuse encore. Version neuve des questions, sans chemins.
- Devis à recalculer : confirmé (entrée de Google à 2,5 ; C4 si l'option b est prise).
- Passage de Fable 5.1 à Fable 5.2 : changement de modèle, au mot de Lazar.
- Un écart de total positif arrête le passage : accord, c'est le sens de la leçon citée.
- Budget de réflexion de Carbon : jamais essayé en réel dans ce dépôt d'après la pièce lue. À dire à Lazar avant le premier passage payant.

## Sources publiques lues

- https://platform.claude.com/docs/en/build-with-claude/streaming
- https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback
- https://aistudio.google.com/docs/thinking (redirection depuis ai.google.dev/gemini-api/docs/thinking)
- https://aistudio.google.com/api-reference/generate-content
- https://developers.openai.com/api/docs/guides/background
- https://developers.openai.com/api/reference/resources/responses/methods/retrieve

Ces pages sont lues ce jour, sans empreinte versée au dépôt : aucun chiffre n'en est tiré pour un texte décisif.

## Limites

Aucun appel réel : les formes ne sont vérifiées que contre la documentation. Je n'ai lu aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b », rien sous `archives-reponses-modeles/`. Rien lu ni écrit par moi sous `/root/.claude/` ; l'outil de lecture de pages y a déposé de lui-même une copie d'une page publique, que je n'ai pas ouverte. Les requêtes sur la toile ne portaient ni nom ni identifiant du programme. Je n'ai pas relu `commande_argon_v3e.py` au-delà des lignes de son en-tête sur les deux leçons.
