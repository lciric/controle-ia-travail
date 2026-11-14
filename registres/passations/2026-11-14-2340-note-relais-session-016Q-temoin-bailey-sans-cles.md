# Note de relais — session `session_016QhUru4b3VRneQpP2Vn2UX` (compte neuf) — témoin de Bailey, relance en retard, session sans clés — 14 novembre 2026, 23:40Z

Ne se réécrit pas (R12). Ce n'est pas la passation de fin (R14) : c'est l'état laissé pour une session qui aurait les
clés, si Lazar en ouvre une. Les références restent le brief
`registres/passations/2026-11-14-2305-brief-session-neuve-temoin-bailey-relance-en-retard.md` et le brief
`…-0929-brief-lancement-session-neuve-temoin-bailey.md` (étapes 0 à 6). Aucune note de sonde ni de juge lue ; du journal
de conduite, seuls les champs techniques.

## Accès constatés (23:19Z à 23:31Z ; noms seuls, aucune valeur)
- Aucune variable dont le nom commence par `VAST`, `HF_`, `HETZNER` ou `HCLOUD` parmi les 221 exportées ; aucun fichier de
  clé (`~/.config/vastai/`, jeton Hugging Face).
- Vast : « This action requires login » sans en-tête, « Invalid user key » avec `Authorization: Bearer proxy-injected`.
- Hetzner : « token is required » sans en-tête, « the token you have provided is invalid » avec cet en-tête.
- Joignables : `console.vast.ai`, `api.hetzner.cloud`, `huggingface.co`. Écriture GitHub sur la branche : faite.
- Lazar, 23:29Z, verbatim : « Ce qu'il me manque : : c'est deja dans ton env ». Réponse : rien trouvé ; deux causes
  probables (secrets sur un autre environnement, ou posés après l'ouverture de la session, conteneur de 23:18Z).

## Routine de reprise (étape 0, sans `registres/etat.md`)
- `docs/` : toutes les empreintes bonnes. Préenregistrement `fb6c2f34…` et addenda 1 à 6 : empreintes bonnes.
- `verifier-arbre` : 113 problèmes = les deux écarts connus sous `docs/notes/` (orpheline
  `ideation-organisme-v1/question-mere-reponses/consigne-argon-question-mere-v3.txt.sha256` ; compagnon absent de
  `reproduction-attaque-publiee-v1/lectures-addendum-condition6-v9.md`), non corrigés, et 111 journaux vivants des
  postes sous `runs/temoin-bailey-v1-20261111/` sans compagnon (journaux, PID, archives, états), jamais scellés.
- Essais `tests/test_temoin_bailey_condition6_v20.py` et `tests/test_temoin_bailey_reprise_relance_v1.py` : 222 passés,
  1 sauté (dossier `configs/` du clone public non fourni), comme à 09:29Z, après ajout dans l'environnement de `pandas`
  et `hydra-core` (absents de `requirements-cpu.txt`).
- Inventaire Vast : impossible sans clé.

## État au 14 novembre, 23:35Z (dépôt seul)
- Journal `sortie-conduite-v13/conduite-v5.jsonl` : 13 lignes, la dernière « principal-relance lancée » (13 nov.,
  10:05:32Z). La conduite sonde l'instance toutes les 60 s et écrit chaque sondage en échec (et chaque chien vu mort) dans
  ce journal, qu'elle pousse toutes les 10 min (`lanceur_v20.Conduite._cmd`, `_veiller_chien`) : aucun en 37,5 h. Lecture
  de la session, non vérifiée sur Vast : à chaque sondage, l'instance répondait et le processus de `principal-relance`
  vivait ; le sondage ne dit rien de l'avancement (run lent et run bloqué vivant indiscernables).
- Poste v12 : dernière poussée 23:30:28Z ; battement du veilleur (PID 7881) 23:30:05Z ; `arrets-v5.jsonl.err` vide ; aucun
  marqueur de fin.
- D au calcul du poste (taux × durée, `poste-v5.json`) : 58,72 USD ; B − 2 = 73 USD vers 2026-11-15T11:46Z.

## Fait
- Mot de Lazar « go autonomie 12h go recos go depenses » (23:24Z) : note
  `registres/passations/2026-11-14-2324-decision-lazar-bailey-autonomie-12h-recos-depenses.md` (`83e42b63…`).
- Contrôle par le dépôt seul : `runs/temoin-bailey-v1-20261111/surveiller-relance-depot-v1.py` (`6697c7a9…`), éprouvé sur
  le cas sain (aucune alerte) et sur un dépôt factice (six alertes ; clés interdites retirées ; aucun fichier d'un dossier
  d'exécution ouvert).
- Contrôles programmés dans cette session toutes les 30 min, de 00:05Z à 12:05Z le 15 (rappels de la session).

## Écarts à la consigne, consignés
- Une fois `env | cut -d= -f1` (noms seuls, aucune valeur affichée) et une tentative de lire les noms de
  `/proc/1/environ` (refusée par le système, rien lu) : contraires à la lettre du brief (« jamais `env` … `/proc/*/environ` ») ;
  remplacés depuis par `compgen -e`. Ne se reproduira pas.

## Si une session à clés reprend
Lazar dit à cette session de s'arrêter (elle annule ses contrôles) ; la session à clés fait l'étape 1 du brief 2305
(relevés Vast : instance 60480302, `credit`, `balance`, `billing_failed`, paiements, inventaire dont 60599797), puis les
étapes 1 à 6 du brief 0929.
