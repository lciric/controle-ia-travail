# Lecture des fiches par Kimi, seconde tentative — commandes exactes, écrites avant tout appel

Opérateur : session fille de la session mère, 14 novembre 2026, écrit à 06:55 UTC (`date -u`), sous la ligne
GO-2026-11-13-06 (réserve du lecteur 4 USD, 6 appels ; plafond du relais 3,5 USD, R-2646). Première tentative arrêtée au
premier appel (compte Moonshot sans solde, R-2645, R-2646) ; Lazar a changé la clé (R-2648).

## Vérifié avant (06:53 à 06:55 UTC)

- outil v2 `a58fb8b99edb…`, classement v2 `2cb65f33f0f5…`, attestation `de94e86ea981…`, copie des fiches
  `a9f9594e2dc3…`, relais `relais_kimi_v4.py` `67f369518102…` : égaux à leurs compagnons ;
- `KIMI_API_KEY` présente, vérifiée par son nom seulement (`[ -n "${KIMI_API_KEY:+x}" ]`) ; `HTTP_PROXY` absente ;
- envois de la première tentative (`lecture-g1-v1/envois/`, 30 fichiers, tous conformes à leurs compagnons) **recopiés à
  l'octet** (`cp -p`) dans `lecture-g1-v2/envois/` et revérifiés ; ils ne sont pas régénérés (`preparer` n'est pas relancé)
  et le dossier v1 reste intact (R12). Pire cas de la pile : 3,031796 USD, 6 appels, `max_tokens` 32 768.

## Commandes (depuis la racine du dépôt)

1. Relais, environnement réduit aux noms présents (ni `ANTHROPIC_BASE_URL` ni `CLAUDE_CODE_REMOTE`) :

       env -i PATH="$PATH" HOME="$HOME" HTTPS_PROXY="$HTTPS_PROXY" NO_PROXY="$NO_PROXY" SSL_CERT_FILE="$SSL_CERT_FILE" \
         REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" KIMI_API_KEY="$KIMI_API_KEY" \
         /usr/local/bin/python3 -I -B docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py --port 8789 \
         --modeles-permis kimi-k3.1-pro --plafond-usd 3.5 --prix-entree 2 --prix-sortie 10 --prix-cache 2 \
         --max-appels 6 --max-recherches 0 --delai-amont-s 1800 --delai-silence-s 600 \
         --journal docs/notes/organisme-conception-propre-v1/lecture-g1-v2/relais/journal-relais-kimi-lecture-g1-v2.jsonl \
         > docs/notes/organisme-conception-propre-v1/lecture-g1-v2/relais/relais-kimi-lecture-g1-v2.log 2>&1 &

   PID noté (`$!`), vérifié par `curl -sS --noproxy 127.0.0.1 http://127.0.0.1:8789/relais/etat` (champ `pid`).

2. Dans `docs/notes/organisme-conception-propre-v1/lecture-g1-v2/envois/`, pour L1 lot 1, 2, 3 puis L2 lot 1, 2, 3, l'un
   après l'autre, **arrêt au premier statut autre que 200** :

       curl -sS --noproxy 127.0.0.1 --max-time 1900 -X POST -H 'Content-Type: application/json' \
         --data-binary @envoi-<L>-lot<k>-v2.corps.json http://127.0.0.1:8789/v1/chat/completions \
         -o reponse-<L>-lot<k>-v2.json -w '%{http_code}'

   puis `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <réponse>` (racine du dépôt). Jamais
   `pile-interne-v2.json`, `cle-lectures-v2.json` ni le manifeste envoyés. Un corps d'erreur n'est ni versé ni lu au-delà
   du statut et du type d'erreur (il peut porter des identifiants du compte) : déplacé hors du dépôt.

3. `.venv/bin/python -I -B docs/notes/organisme-conception-propre-v1/lecture-classement-v2/outil_lecteur_conception_propre_v2.py verifier --envois docs/notes/organisme-conception-propre-v1/lecture-g1-v2/envois`

4. Condition C1 : compte, dans les deux `lecture-verifiee-L*-v2.json`, des critères à valeur brute nulle (`brut` vaut
   `null`), par programme, sans lire les fiches ; seul le compte est rendu.

5. Arrêt du relais par son PID : `kill -INT <PID>`, vérifié arrêté ; relevé de la dépense (`/relais/etat` avant l'arrêt et
   journal), scellé.

Aucune relecture d'un lot ; le classement n'est pas lancé (la mère s'en charge) ; aucune instance Vast ni serveur Hetzner
touché. Arrêt et compte rendu sur tout refus de garde, lecture illisible, erreur de l'amont ou dépense proche de 3,5 USD.
