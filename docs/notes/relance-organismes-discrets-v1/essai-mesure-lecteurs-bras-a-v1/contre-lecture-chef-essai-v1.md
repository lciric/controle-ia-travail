# Contre-lecture du chef de l'essai de mesure des lecteurs du bras A — v1

- **Pièce** : classe B (instrument). Le chef d'essai envoie de vraies requêtes payantes en trois files : Claude, Carbon et GPT (lignes de calcul GO-2026-11-19-34, -35 et -36, qui échoient le 2026-11-20).
- **Contre-lecteur** : agent neuf, Claude Opus 5.5. Il n'a écrit aucune des pièces ; l'auteur est Claude Fable 5.2. Relu le 2026-11-19, dans un arbre séparé, au commit `14d2acc2` de la branche `claude/pensive-bardeen-1fv7hw`.
- **Interdits tenus** : aucune commande réelle lancée, aucune requête envoyée à un fournisseur, aucune clé lue ni affichée (seule la présence des noms de variables a été testée) ; aucun fichier « consigne-privee » ou « conception-ii-b » ouvert, ni le paquet `iib` ; rien committé. Les seuls appels réseau sont un `git fetch` et une requête de connexion vers `example.com`, qui n'est pas un fournisseur.

## Verdict

**Engageable.** Le chef ne fait rien de plus que ce que dit le devis, à deux écarts près, déclarés et sans effet sur l'argent : le corps des appels Claude porte `stream: true`, et les arguments du relais d'OpenAI sont plus serrés que ceux du devis.

- Le plafond de chaque ligne tient dans tous les cas examinés. La seule exception est celle que le devis accepte : un envoi de Carbon dont le service ne respecterait pas le budget de réflexion.
- Les clés ne passent que par leur nom.
- Le relais est arrêté par son identifiant de processus.
- Chaque garde mord quand on la retire, sauf trois points où l'essai qui la couvre manque. Aucun des trois ne touche l'argent, les secrets ou les arrêts.

Il reste trois conditions à remplir avant le départ, et un geste obligatoire au moment du versement. Ce ne sont pas des corrections du code ; ils sont décrits plus bas.

## Empreintes vérifiées (sha256)

| pièce | empreinte | conforme |
|---|---|---|
| `scripts/chef_essai_mesure_lecteurs_bras_a_v1.py` | `7184187f2c018dde3367c5d44a526f0e67894c5a3d28da6e639d67ca3898de51` | oui |
| `tests/test_chef_essai_mesure_lecteurs_bras_a_v1.py` | `5a8a7b1ac92248729e556c61299dc5a452aecdd6835dfa33f7662bfaddd67118` | oui |
| `scripts/fabriquer_entrees_essai_mesure_v1.py` | `f9f53832e24a0ee88f2d8d5d940ba8cf6856d2ece1fbc00e720b1f1c2c0d5efe` | oui |
| configuration | `e047c502ca711b188b435092537cb620a2650ff52cb25c7403afa37020ddf194` | oui |
| entrées | `15b62bb44d9f8e57bbbebf020b08cb681fbd0f5f65cc89dadee9edc7faba467e` | oui ; **le générateur, relancé, rend la même empreinte** |
| devis, brouillon 3 | `533ad5b15e6de1bdfe81c35f8501dbad376f52f907be84094c3fd8621b349592` | oui |
| relais Claude, ses deux pièces, relais de Google, relais d'OpenAI, lanceur, page de prix de Google | empreintes égales à celles de la configuration | oui |
| relevé de vérification de la clé Claude | `7ce262ba…` ; compagnon conforme | oui |

**Essais** : 120 passés en 58 s. Ils ne passent que sur une branche nommée : sur une tête détachée, 8 échouent, et c'est la garde du rien-de-personnel qui les arrête (voir le point 7, « tête détachée »).

## 1. Le chef fait-il ce que dit le devis, et rien de plus ?

- **Modèles et ordre** :
  - file Claude : Opus 5.5 à l'effort bas, Sonnet 5.5 à l'effort bas, Opus 5.5 à l'effort moyen, Sonnet 5.5 à l'effort moyen, puis Haiku 5.5 à l'effort bas, en dernier ;
  - file Carbon : budget de réflexion de 1 024, puis de 2 048 ;
  - file GPT : `gpt-6.2-astra` seul, au réglage par défaut du service.

  C'est le tableau 5.1 du devis. Les entrées sont jouées par blocs (A-b1, C-b1, A-b2, C-b2, A-b3) : un arrêt laisse un préfixe équilibré.
- **Nombre d'appels** : le contrôle avant départ, refait ici, compte 120, 48 et 8 appels. Le pire cas compté par le chef vaut 27,66, 13,38 et 6,18 dollars, sous le pire cas du devis (29,23, 14,41 et 6,44), qui arrondit vers le haut. La file GPT prend six entrées de l'appariement (A-b1-01 à 06) et deux de la couverture (C-b1-02 et 03) ; le devis ne dit pas lesquelles.
- **Corps Claude** : `model`, `max_tokens: 8192`, `output_config: {"effort": "low"|"medium"}`, un seul message d'utilisateur et `stream: true`.
  - Il n'y a ni température, ni `top_p`, ni `top_k`, ni `thinking`, ni en-tête bêta, ni repli sur un autre modèle.
  - `anthropic-version: 2023-06-01`.
  - La référence de l'interface de Claude, consultée ici, confirme que l'effort se règle dans `output_config`, sans en-tête bêta, pour Opus 5.5, Sonnet 5.5 et Haiku 5.5, et que les identifiants de modèles ne sont pas datés.
- **Corps Carbon** : `maxOutputTokens: 4096`, `thinkingConfig.thinkingBudget` écrit à chaque appel, température 0 au premier envoi.
- **Corps GPT** : `max_completion_tokens: 8192`, température 0 au premier envoi.
- **Relais Carbon** : ses arguments sont ceux du devis (section 5.3) à la lettre.
- **Relais d'OpenAI** : il porte en plus `--max-appels 17` (8 appels × 2 envois + l'essai de la température), les trois prix 8, 40 et 8 (le cache est compté au prix plein, ce qui est une borne haute) et `--max-jetons-sortie-pire-cas 8192`. Ce relais exige ses prix pour démarrer ; ces ajouts ne font que serrer les barrières. **Écart acceptable**, à dire au rapport de l'essai.
- **Relais Claude** : ses arguments sont ceux du devis (garde du plafond de dépense, G1) à la lettre : modèles permis exacts, plafond de 9,25 dollars, réserve de 0,27 par appel.

## 2. Les plafonds

Le compteur tient deux cumuls, un par modèle et un pour la file. Il refuse un envoi **avant** son départ si le cumul compté plus le pire cas de cet envoi dépasse l'un des deux plafonds. Le pire cas compte un jeton par octet du corps réel, plus la sortie maximale comptée. Le refus est vérifié avant chaque envoi, y compris l'envoi repris.

| cas | ce que fait le chef | le plafond tient ? |
|---|---|---|
| envoi sans compteur lisible : délai, coupure, réponse 200 illisible, flux interrompu, signal pendant l'envoi | compté au pire cas ; une seule reprise | oui |
| plafond atteint en cours de file, de modèle ou de file | refus avant départ ; le faux fournisseur ne reçoit rien ; la file s'arrête | oui |
| réponse facturée sous un nom de modèle autre, daté par exemple | Claude et Carbon : coût réel compté sur les compteurs, puis arrêt de la file. GPT : le relais retient la réponse et rend un code 502 portant le modèle servi ; le chef compte le pire cas et arrête la file | oui |
| refus de la température par un code 400 | GPT : compté au pire cas. Carbon : compté zéro. C'est ce que disent les sections 5.5 et 6.3 du devis | oui |
| refus rendu par le relais avant l'amont : plafond ou borne d'appels, code 402 ou 429 | compté zéro ; arrêt de la file | oui |
| surcharge, ou code 502 du relais (amont injoignable) | compté au pire cas ; une reprise, puis arrêt du réglage | oui (prudent) |
| Carbon rend des compteurs au-delà de 4 096 + son budget | compté au réel ; arrêt de la file | **à un envoi près**, comme l'accepte le devis (section 6.3) |

Seconde barrière, indépendante du chef : chaque relais a sa propre borne. Le relais Claude bloque à 9,25 dollars avec la réserve de 0,27 ; le relais d'OpenAI à 2,50 dollars, avec le pire cas de chaque requête réservé ; le relais de Google à 97 appels.

**D'une course à l'autre**, la seule protection est le refus de rejouer une file qui a déjà un dossier de course. C'est elle qui empêche une seconde course de dépenser une seconde fois le plafond de la même ligne.

## 3. Épreuve par retrait des gardes

Méthode : sur une copie, une garde est retirée à la fois, puis on lance les essais de la pièce. La copie est remise à son empreinte après chaque retrait ; cela a été vérifié.

| garde retirée | un essai échoue ? |
|---|---|
| plafond de dépense, refus avant l'envoi (G1) | oui |
| plafond de dépense, compte d'un envoi sans compteur au pire cas (G1) | oui |
| plafond de dépense par modèle (G1) | oui |
| délais, délai global de la file (G2) | oui |
| délais, trois délais de suite arrêtent le réglage (G2) | oui |
| **délais, délai total d'une réponse en flux (G2)** | **non** : aucun essai ne le couvre. Le code existe : relu, il borne bien à 600 secondes, vérifié entre deux lectures |
| sortie maximale, corps sans sortie maximale ou plus haute (G3) | oui |
| sortie maximale, compteurs au-delà de la borne (G3) | oui |
| **refus, branche « refus de compte » (G4)** | **non** : sans elle, les codes 401 à 429 tombent dans la branche « autre code », qui arrête aussi la file sans reprise et au même compte. Seul le motif change, avec lui le nombre de refus du rapport. Effet nul sur l'argent |
| refus de contenu (G4) | oui |
| modèle servi autre (G4) | oui |
| surcharge, second échec (G4) | oui |
| autre code, 404 (G4) | oui |
| autre code 400 (G4) | oui |
| rien de personnel, contrôle de ce qui part (G5) | oui |
| rien de personnel, liste locale exigée (G5) | oui |
| clés, clé exigée par son nom au lanceur (G6) | oui |
| clés, recherche des formes de clé (G6) | oui |
| clés, ouvrier refusé avec un nom de clé (G6) | oui |
| clés, environnement réduit de l'ouvrier (G6) | oui |
| ligne de calcul (G7) | oui |
| ligne de calcul, échéance (G7) | oui |
| ligne de calcul, file déjà jouée (G7) | oui |
| clé Claude vérifiée (G8) | oui |
| clé Claude vérifiée, empreinte de l'attestation (G8) | oui |
| arrêt du relais par identifiant de processus (R10) | oui ; ce retrait a laissé un relais d'essai (clé factice, faux amont), arrêté ensuite par son identifiant de processus |
| le chef ne parle qu'à la boucle locale | oui |
| **le rapport ne contient aucune sous-chaîne d'une réponse** | **non** : aucun essai ne couvre le branchement. Le rapport n'est fait que de champs du journal, sans texte de réponse ; c'est une défense de second rang |

## 4. Les arrêts

- **Le relais** est lancé directement par le lanceur, dans une session de processus neuve. L'identifiant rendu est donc celui du relais lui-même. Il est arrêté par `os.kill(pid, …)` seulement : interruption, puis terminaison, puis arrêt forcé, avec cinq secondes d'attente entre chaque. Aucun motif de ligne de commande n'est employé : la règle R10 est tenue.
- **L'ouvrier** est arrêté par son objet de processus. Si l'amorce est tuée sans pouvoir réagir, le relais survit ; son identifiant est dans `journal-amorce.jsonl` (événement `relais_lance`), écrit juste après son lancement, pour un arrêt à la main.
- **Un refus 403 arrête-t-il toute la file Claude ?** Oui. Un 403 de l'amont (clé refusée pour un modèle) arrête toute la file sans reprise, avec un compte au pire cas. Un 403 du relais (modèle non permis) l'arrête aussi, avec un compte nul. Un 404 l'arrête par la branche « autre code ».
- **Consignation** : la consignation dans `registres/arrets.md` reste à faire par la mère, d'après `journal-amorce.jsonl`.

## 5. Les secrets

- **Le relais** reçoit seulement les noms listés ; la clé y est exigée par son nom, préfixée de `!`. Les noms commençant par `CLAUDE` ou `CCR` sont refusés.
- **L'ouvrier**, qui fait les envois, part avec `PATH`, `HOME`, `LANG` et `GO_ID` seulement. Il refuse de partir si un nom de son environnement contient `KEY`, `TOKEN` ou `SECRET`.
- **GPT** : le relais reçoit la valeur factice de la configuration, quelle que soit la valeur présente. Une variable `OPENAI_API_KEY` existe bien dans ce conteneur ; elle n'est jamais transmise, et un essai le vérifie.
- **Ce que le chef écrit** : aucune valeur de clé n'est écrite dans le manifeste, le journal, l'inventaire ou le rapport.
  - Les termes de la liste du rien-de-personnel ne quittent pas la mémoire : seuls leur nombre et leur empreinte vont au manifeste.
  - Les messages d'arrêt n'en donnent que le rang.
  - Ce qui part au relais est vérifié avant chaque envoi.
- **Formes échappées** : non couvertes, sans effet pratique ici.
  - Le relais de Google masque la clé exacte en octets bruts seulement ; c'est une limite écrite dans son en-tête. Le relais Claude ne masque rien.
  - La recherche finale des formes de clé lit le texte brut : une clé écrite en échappement `\uXXXX` ou en encodage d'adresse `%2D` lui échapperait.
  - Aucun des chemins réels n'écrit de clé sous ces formes : `json.dumps` n'échappe ni `-` ni les caractères alphanumériques, et les fournisseurs ne recopient pas la clé.
  - Correction facultative, plus bas.

## 6. Le versement

- **Écritures** : chaque envoi écrit son corps puis sa ligne de journal, vidés sur le disque, **avant** de partir ; chaque réponse est écrite avant d'être analysée. Les noms ne sont jamais écrasés.
- **À la fin** (fin normale, garde, signal ou panne), dans cet ordre : état du relais, arrêt par identifiant de processus, recherche des formes de clé, rapport, inventaire de tout le dossier avec taille et empreinte. L'inventaire est scellé par son empreinte compagnon. **Rien n'est supprimé.**
- **Lacune pour le versement** : seul l'inventaire porte une empreinte compagnon. Le rapport technique, les corps envoyés, les réponses brutes et les journaux n'en ont pas. Or `runs/` est un dossier scellé : `verifier-arbre` y exige un compagnon par fichier. La vérification du début de chaque session en relèverait des centaines.
- **Geste obligatoire, avant tout commit d'un dossier de course** :

  ```
  find runs/essai-mesure-lecteurs-bras-a-v1/<dossier> -type f ! -name '*.sha256' -print0 \
    | xargs -0 env PYTHONPATH=src python3 -B -m controle_ia.scellement sceller
  ```

  Le scellement est idempotent et n'écrase jamais un compagnon existant, celui de l'inventaire compris.

## 7. Les six points posés par l'auteur

1. **`stream: true` dans le corps Claude**, absent de la liste du devis (section 5.2). **Acceptable.**
   - La garde des délais (G2 : « le flux reste muet pendant la réflexion ») et le versement (section 8.2 : « flux partiels d'un envoi coupé ») supposent déjà un flux.
   - L'interface l'admet, et le relais Claude relaie le flux morceau par morceau en lisant l'usage.
   - L'écart est déclaré dans l'en-tête du chef et dans la configuration scellée (`"flux": true`). Il reste à le dire au rapport de l'essai.
2. **Un plafond atteint arrête toute la file.** **Conforme à la lettre du devis** : l'artefact de la garde du plafond dit « la file s'arrête », et la section 6.3 dit « sa file s'arrête au plafond ».
   - Coût de ce choix : si Opus 5.5 atteint ses 6 dollars pendant l'effort moyen, Sonnet 5.5 à l'effort moyen et Haiku 5.5 ne sont pas mesurés, alors qu'il leur reste du budget.
   - Arrêter le seul modèle serait un écart au devis ; je ne le recommande pas sans un mot de Lazar.
3. **Un envoi sans compteur lisible est compté au pire cas.** **Conforme** à la garde du plafond, et prudent.
   - Si le flux de Claude devenait illisible de façon systématique, chaque lecture serait envoyée deux fois et comptée deux fois au pire cas (environ 0,4 dollar par lecture pour Opus 5.5), et la file s'arrêterait vite à son plafond, sans le dépasser.
   - Le lecteur de flux suit la forme standard des événements (`message_start`, `message_delta`, `message_stop`) ; les blocs de réflexion sont ignorés.
4. **`relais_reel.py` ouvre une connexion directe vers le fournisseur, sans passer par le mandataire HTTPS.** **Acceptable.**
   - Une connexion HTTPS directe aboutit depuis ce conteneur : code 200 sur un hôte neutre, avec le magasin de certificats donné par `SSL_CERT_FILE`, que le relais reçoit.
   - Ce même relais a servi 16 appels sur la clé Rigaud le 18 novembre (journal de la relance, entrée OD-022).
   - Si la route directe était fermée, le relais rendrait un 502 « amont injoignable » sans rien avoir envoyé. Le chef compterait le pire cas, ferait une reprise puis arrêterait chaque réglage : aucune dépense, mais la file serait « déjà jouée » (voir la correction facultative 1).
   - Les relais de Google et d'OpenAI, eux, passent par le mandataire ; sa forme (`http://hôte:port`, sans identifiants) leur convient.
5. **La liste locale des interdits du rien-de-personnel (G5), hors du dépôt.** **Acceptable** : elle porte des noms de personnes, elle n'a pas sa place dans un dépôt versé, et son empreinte va au manifeste.
   - **Elle n'existe pas encore** dans ce conteneur (`/home/user/hors-depot/essai-mesure-lecteurs-bras-a-v1/interdits-g5-v1.txt` absent). Sans elle, le chef refuse avant tout envoi et avant de créer un dossier : c'est sans frais.
   - Le contrôle de tous les corps, rejoué avec les termes tirés de l'arbre principal et de l'environnement présent (liste locale factice), passe pour les trois files.
   - **Tête détachée** : si le dépôt est sur une tête détachée, git rend « HEAD » comme nom de branche. « head » devient alors un terme interdit, que les textes portent (« retrieval head »), et le contrôle refuse tout, avant tout envoi. Il faut lancer depuis une branche nommée.
6. **Un modèle servi sous une chaîne datée arrêterait la file après un envoi facturé.** **Acceptable** : cet envoi est compté, au réel ou au pire cas, sous le plafond, et un seul envoi est perdu, au plus 0,52 dollar compté.
   - Indices relevés : Haiku 5.5 a été servi sous `claude-haiku-5-5` (relevé de vérification de la clé) ; dans les relevés du dépôt, Opus 5.5 est servi sous `claude-opus-5-5` (2 251 fois), `gpt-6-astra` sous son nom nu (222 fois), Carbon sous `gemini-4-carbon`.
   - La référence de l'interface de Claude dit que ses identifiants ne sont pas datés.
   - Reste un doute sur Sonnet 5.5, qu'aucune pièce ne montre servi, et sur `gpt-6.2-astra`.

## Conditions avant le départ (aucune n'est une correction du code)

1. **Créer la liste locale du rien-de-personnel** à son chemin, avec au moins un terme de quatre caractères ou plus. Elle n'est jamais versée.
2. **Lancer depuis une branche nommée** qui porte le commit `14d2acc2` ou un commit postérieur sans changement de ces pièces. Faire `git fetch origin main` juste avant, pour que la ligne de calcul et une éventuelle révocation soient lues à jour.
3. Inscrire les lignes d'engagement dans `registres/depenses.md`, et, **pour la file Claude seulement**, poser la règle de permission étroite sur un mot de Lazar. Elle vaut pour la seule commande `GO_ID=GO-2026-11-19-34 python3 -I -B scripts/chef_essai_mesure_lecteurs_bras_a_v1.py claude`.

Au versement : sceller tout le dossier de course (section 6), puis consigner l'arrêt du relais dans `registres/arrets.md`.

## Corrections facultatives (mineures ; à appliquer seulement si le temps le permet, avec une vérification par le même contre-lecteur, puisque l'empreinte du chef changerait)

**1. Ne pas « brûler » une file qu'une panne de démarrage a arrêtée sans aucun envoi.** Aujourd'hui, un relais qui ne s'annonce pas en 20 secondes, ou un état initial inattendu, laisse un dossier de course. La file est alors « déjà jouée » et demande une ligne nouvelle, alors que rien n'est parti.

Avant :
```python
def dossiers_deja_joues(base: Path, nom: str) -> list:
    return sorted(str(p) for p in base.glob(f"*-file-{nom}")) if base.is_dir() else []
```
Après :
```python
def dossiers_deja_joues(base: Path, nom: str) -> list:
    """Une file est jouée dès qu'un envoi est parti : la ligne `envoi` du journal est écrite, vidée sur le disque, avant
    l'envoi. Un dossier sans journal d'essai ou sans envoi (panne au démarrage) ne compte pas, et il est gardé."""
    if not base.is_dir():
        return []
    joues = []
    for p in sorted(base.glob(f"*-file-{nom}")):
        try:
            lignes = lire_journal(p / "journal-essai.jsonl")
        except (OSError, ValueError):
            joues.append(str(p))  # journal illisible : prudence, compté comme joué
            continue
        if any(l.get("evenement") == "envoi" for l in lignes):
            joues.append(str(p))
    return joues
```
Il faut un essai de plus : un dossier sans journal d'essai ne bloque pas, un dossier avec un envoi bloque.

**2. Recherche des formes de clé, formes échappées comprises.**

Avant :
```python
        contenu = chemin.read_bytes().decode("utf-8", errors="replace")
        if any(re.search(forme, contenu) for forme in FORMES_DE_CLE):
```
Après :
```python
        contenu = chemin.read_bytes().decode("utf-8", errors="replace")
        normalise = urllib.parse.unquote(re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), contenu))
        if any(re.search(forme, texte) for texte in (contenu, normalise) for forme in FORMES_DE_CLE):
```

**3. Essais manquants** : le délai total d'une réponse en flux (un faux fournisseur qui envoie un octet toutes les secondes au-delà du délai total raccourci) ; le branchement du contrôle « aucune sous-chaîne » dans l'écriture du rapport ; le motif « refus de compte » distinct de « autre code ».

**4. Rapport** : à la projection `C`, une lecture reprise compte aujourd'hui son envoi sans compteur pour zéro, alors que le devis (section 7.3) veut « par ses deux envois ». La sous-estimation est faible ; il suffit de la dire au rapport. Pour GPT, le réglage de raisonnement n'est pas rendu par la réponse : écrire « défaut du service, non rendu » plutôt que « relevé ».

## Fichiers lus

Le chef, ses essais, le générateur, la configuration et les entrées ; le devis, brouillon 3 ; les lignes GO-2026-11-19-34 à -36 de `registres/go.md` sur la branche principale ; `relais_reel.py`, `relais.py`, `relais_gemini_v3.py` (en-tête et traitement d'une requête), `relais_kimi_v4.py` (en-tête, mandataire, traitement d'une requête) ; `scripts/lancer_relais_local_v1.py` ; le relevé de vérification de la clé Claude ; les entrées OD-020 à OD-024 et OD-104 à OD-116 du journal de la relance ; `src/controle_ia/scellement.py`.
