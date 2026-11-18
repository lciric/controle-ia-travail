# Procédure — relais persistants des clés d'interface (Claude, compatible OpenAI, Gemini sans flux et en flux) — v1

Écrite le 18 novembre 2026 par la session de relance des organismes discrets, à la demande de la session mère (07:19Z), pour
qu'une autre course de l'organisme d'idéation lance ses relais sans rien lire d'un sujet. **Neutre** : aucune question,
aucun fait, aucun témoin, aucune fiche. Tout chemin est relatif à la racine du dépôt de travail
(`/home/user/controle-ia-travail`), sauf le relais Claude, qui vit dans le clone épinglé de l'orchestrateur.

## 0. Principe

Un relais est un petit serveur local (boucle locale seulement) qui détient **seul** la vraie clé d'interface, lue au
démarrage dans **son** environnement par le **nom** de sa variable, puis effacée de cet environnement. Les commandes et les
agents ne reçoivent qu'une adresse locale et un jeton factice. Le relais borne la dépense (plafond en dollars, ou nombre
d'appels pour Gemini), journalise chaque appel sans clé ni texte, et répond à `GET /relais/etat`.

Jamais : `env`, `printenv`, une valeur de clé sur une ligne de commande, un relais lancé sans journal, un autre client que la
course sur le port pendant qu'elle tourne, un arrêt par motif de ligne de commande (R10 : par PID seulement).

## 1. Les programmes

| relais | chemin | empreinte | sur `main` | port d'usage | variable de clé |
|---|---|---|---|---|---|
| Claude (Anthropic) | `/home/user/lciric/ideation-organism/orchestrator/pole/relais_reel.py` (clone de `lciric/ideation-organism`, commit `a41b7b50`, arbre `orchestrator/` `ee84d6ec…`) | `1b90b020…` | hors dépôt (clone) | 8787 | au choix : `RR_ANTHROPIC_API_KEY_MINUIT` pour la course d'affinage |
| compatible OpenAI (Moonshot pour Kimi, OpenAI pour Astra) | `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py` | `67f36951…` | oui | 8789 (Moonshot), 8790 (OpenAI) | `KIMI_API_KEY` ; `OPENAI_API_KEY` |
| Gemini v2, sans flux | `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py` | `2b0043bc…` | oui | 8788 | `GEMINI_API_KEY` |
| Gemini v3, en flux | `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v3.py` | `2cf6bc6d…` | **non** : branche `claude/eloquent-tesla-e52a0b`, commit `b1acd890` | 8791 | `GEMINI_API_KEY` |
| lanceur de relais | `scripts/lancer_relais_local_v1.py` | `d365affc…` | **non** : même branche, commit `4d52efc7` | — | — |

Vérifier chaque empreinte avant le lancement (`sha256sum -c <fichier>.sha256` dans son dossier ; le clone par
`git -C /home/user/lciric/ideation-organism rev-parse HEAD:orchestrator`).

## 2. Lancement : toujours par le lanceur de relais

```
cd <DOSSIER_HORS_DEPOT> && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py <DOSSIER_HORS_DEPOT>/console-<nom>.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!<NOM_DE_LA_VARIABLE> -- <COMMANDE DU RELAIS>
```
- L'environnement du relais est réduit aux noms listés ; `!NOM` = exigé (absent ou vide : rien ne part, code 2).
- Session de processus neuve ; console jamais écrasée ; le lanceur imprime une ligne JSON avec le `pid`.
- Refusés d'office : `ANTHROPIC_BASE_URL`, `CLAUDE_CODE_REMOTE`, tout nom en `CLAUDE…` ou `CCR…`.

### 2.1 Claude (Anthropic)
```
/usr/bin/python3 -I -B /home/user/lciric/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_MINUIT --port 8787 --plafond-usd <PLAFOND> --modeles-permis <MODELE1>,<MODELE2> --journal <DOSSIER_HORS_DEPOT>/journal-relais-claude.jsonl
```
`--plafond-usd` est **obligatoire** ; `--modeles-permis` donne les noms exacts (liste vide : tout refusé) ; réserve par appel
0,4 USD par défaut (`--reserve-par-appel`). L'orchestrateur exige que les modèles permis soient **exactement** ses modèles
internes. Attendu dans la console : « relais prêt sur http://127.0.0.1:8787 (… plafond … modèles permis : …) ».

### 2.2 Compatible OpenAI (Kimi chez Moonshot ; Astra chez OpenAI)
```
/usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py --amont https://api.moonshot.ai --variable-cle KIMI_API_KEY --port 8789 --modeles-permis kimi-k3.1-pro --plafond-usd <PLAFOND> --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels <N> --delai-amont-s 3400 --journal <DOSSIER_HORS_DEPOT>/journal-relais-moonshot.jsonl
```
Pour OpenAI : `--amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8790 --modeles-permis gpt-6-astra
--prix-entree 10 --prix-sortie 50 --prix-cache 1`. Les trois prix sont exigés quand `--plafond-usd` est posé (le cache est
compté au prix donné : borne haute si on le met au prix plein). L'amont est **toujours lu en flux** (la coupure à 300 s
d'une connexion muette ne l'atteint pas) ; `--delai-silence-s` 600 par défaut, `--delai-amont-s` 1 800 par défaut (le
relever si la commande a un délai plus long : relais ≥ commande). Prix : Kimi 2 / 10 (vérifiés le 30 octobre, page
`c62210a0…`) ; Astra 10 / 1 / 50 (`docs/notes/organisme-conception-propre-v1/prix-astra-v2.md`, `bf211a07…`).
Appel gratuit de contrôle de la clé : `… relais_kimi_v4.py --amont … --variable-cle … --lister-modeles`.

### 2.3 Gemini v2, sans flux
```
/usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --port 8788 --max-appels <N> --modele <MODELE1> [--modele <MODELE2>] --journal <DOSSIER_HORS_DEPOT>/journal-relais-gemini.jsonl
```
Pas de plafond en dollars : la borne est `--max-appels` (au-delà : 429) ; la dépense est bornée par la garde de chaque
commande Gemini (pire cas avant envoi contre `PLAFOND_SESSION_USD`). **Limite connue** : une connexion muette plus de 300 s
est coupée sur le réseau de ces conteneurs ; avec un budget de pensée élevé (8 192 jetons), un modèle peut rester muet au-delà
(observé le 18 novembre) : borner le budget de pensée de la commande, ou passer en flux (v3), ou par lot.

### 2.4 Gemini v3, en flux
```
/usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v3.py --port 8791 --max-appels <N> --modele <MODELE> --delai-silence-s 240 --journal <DOSSIER_HORS_DEPOT>/journal-relais-gemini-v3.jsonl
```
Relaie `generateContent` vers `streamGenerateContent?alt=sse` et rend au client une réponse entière ; pose
`includeThoughts` (retirer par `--sans-pensees-amont`) ; tout flux incomplet, illisible, ou muet plus de
`--delai-silence-s` donne 502 (jamais une réponse tronquée). **Le flux n'aide pas** si le modèle n'envoie rien pendant qu'il
pense : seul le premier octet compte ; il n'a rien envoyé en 240 s avec un budget de 8 192 (18 novembre).

## 3. Vérification après lancement (réglages lus par PID, jamais l'environnement)
```
tr '\0' ' ' < /proc/<PID>/cmdline; echo
/usr/bin/python3 -I -B -c 'import json,urllib.request; op=urllib.request.build_opener(urllib.request.ProxyHandler({})); print(json.loads(op.open("http://127.0.0.1:<PORT>/relais/etat",timeout=5).read()))'
```
Attendu : 0 appel, 0 dépense, plafond et modèles permis conformes ; `variable_cle_encore_presente` faux (relais Gemini).
Toute autre réponse : arrêt par PID, rien ne part.

## 4. Plafond par étape

Le plafond d'un relais vaut pour **toute sa vie**. Pour un plafond par étape : un relais par étape (lancé avant l'étape au
plafond de l'étape, lu puis arrêté par PID à sa fin), ou un relais pour la ligne entière au plafond de la ligne, l'étape
étant bornée par les plafonds de session de l'orchestrateur (`--budget…`) et par la garde de la commande. Dans les deux cas,
le plafond du relais ne dépasse jamais le montant de la ligne de GO, et la somme des plafonds de session tient dessous.

## 5. Relevé des coûts

- Avant et après chaque course : `GET /relais/etat` (Claude et compatible OpenAI : `depense_usd`, `engage_usd`, `appels`,
  `refus` ; Gemini : `appels`, `reponses_par_statut`) ; consigner l'écart.
- Le journal de chaque relais (JSON par ligne : heure, modèle, modèle servi, statut, durée, usage) se rapproche du relevé de
  la course ; tout écart se consigne.
- Soldes : Moonshot par l'appel gratuit `GET https://api.moonshot.ai/v1/users/me/balance` (clé lue par son nom dans le
  processus, jamais affichée) ; Anthropic, OpenAI et Google : pas d'appel de solde connu ; solde donné par Lazar.
- Les coûts comptés « au pire cas » par une commande sur une coupure (usage absent) sont des bornes, pas des factures.

## 6. Arrêt

```
kill -INT <PID>        # puis, s'il vit encore après quelques secondes :
kill -TERM <PID>
```
Lire `/relais/etat` **avant** l'arrêt (le compte est perdu ensuite). Arrêter tout relais sans tâche en cours (R10) et le
consigner.
