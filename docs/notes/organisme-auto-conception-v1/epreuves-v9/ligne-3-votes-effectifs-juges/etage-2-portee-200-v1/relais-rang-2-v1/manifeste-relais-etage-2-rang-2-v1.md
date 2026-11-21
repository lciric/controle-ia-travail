# Manifeste — lancement des relais de rang 2 de l'étage 2, ligne 3 (v1)

Session du compte organisme. Accord : GO-2026-11-20-68 ; mot de Lazar donné dans cette session le 2026-11-21 vers 09:44Z (« je confirme : lance les deux relais de rang 2 et la relance de l'étage 2, sous GO-2026-11-20-68 ») ; mot de la mère de 09:04Z (relance selon l'additif 6, § 9, et le mot de départ : relais neufs aux mêmes ports, fichiers de rang 2, déclaration v2). Procédure suivie à l'identique de `relais-geste-8-v1/manifeste-relais-etage-2-v1.md` (`4d877381…`), rang 2. Le premier essai de lancement du relais Claude, vers 09:10Z, avait été refusé par le classifieur avant le mot de Lazar (R-4472) ; rien n'était parti.

## Heures (UTC)
- Lancement du relais Claude : Sat Nov 21 09:44:29 UTC 2026
- Déclaration v2 et compagnon : 09:45:02

## Commandes
```
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/relais-ligne-3-etage-2-portee-200-v1/console-relais-claude-v2.txt 'PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_LUC' -- /usr/bin/python3 -I -B /home/user/lciric/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_LUC --port 8787 --plafond-usd 88.36 --modeles-permis MODELES_CLAUDE --journal /home/user/relais-ligne-3-etage-2-portee-200-v1/journal-relais-claude-v2.jsonl
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/relais-ligne-3-etage-2-portee-200-v1/console-relais-argon-v2.txt 'PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY' -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle GEMINI_API_KEY --port 8788 --max-appels 2410 --journal /home/user/relais-ligne-3-etage-2-portee-200-v1/journal-relais-argon-v2.jsonl
env -C /home/user/relais-ligne-3-etage-2-portee-200-v1 sha256sum declaration-relais-ligne-3-etage-2-v2.json > /home/user/relais-ligne-3-etage-2-portee-200-v1/declaration-relais-ligne-3-etage-2-v2.json.sha256
```
`MODELES_CLAUDE` : la liste relevée à la déclaration v1 (ligne 5 de la déclaration de l'épreuve des témoins v9), inchangée.

## Codes de sortie
- Lanceur du relais Claude : 0 (`noms_absents` vide)
- Lanceur du relais Argon : 0 (`noms_absents` vide)
- Compagnon de la déclaration : 0

## Identifiants de processus
- PID_CLAUDE : 23274
- PID_ARGON : 23457
- Preuve qu'ils vivent : `stat -c %n /proc/23274` et `/proc/23457` répondent.

## État relevé juste après le lancement (`/relais/etat`)
- Claude, port 8787 : plafond 88,36 ; dépense 0 ; appels 0 ; refus 0.
- Argon, port 8788 : appels 0 ; refus 0 ; 2 410 appels restants.

## Plafond du relais Claude
88,36 USD à la lettre (option b de la mère, 09:08Z) : le code d'appel v4 exige l'égalité du plafond du relais avec la constante `PLAFOND_C` (lanceur v9, `controler_relais_vivant`). Écart accepté par la mère : la garde de la ligne est le compteur du programme, qui reprend son journal à 18,848097 USD ; relevé du relais par la mère avant le lancement et à mi-course.

## Déclaration v2
- Chemin : `/home/user/relais-ligne-3-etage-2-portee-200-v1/declaration-relais-ligne-3-etage-2-v2.json` (forme de la v1 à la lettre ; seuls changent la version et les deux identifiants de processus ; terminée par un saut de ligne).
- Empreinte (`HEX_DECLARATION` v2) : 5617d47adf71d0b4e3c2197b5211aeea63ecc5fa2673ec8a792331dd78c69664

Aucune requête aux relais hors `/relais/etat`, aucune valeur de clé lue ni écrite. Rien n'est lancé du programme d'appel avant le mot de relance scellé de la mère.
