# Manifeste — lancement des relais de l'étage 2, ligne 3 (v1)

Agent des relais de l'étage 2. Demande de la mère sous GO-2026-11-20-68. Lettre suivie : § 9 de `prereg/organisme-auto-conception-v9/additif-6-code-etage-2-preenregistrement-ligne-3-v2.md` (empreinte e2afc7b987ab64dfc270c6c20d49ef5e0d8eaf603ffb2f647a0ea0dee6ca4f01, égale à son compagnon).

## Heures (UTC)
- Début : Sat Nov 21 06:39:01 UTC 2026
- Fin : Sat Nov 21 06:39:45 UTC 2026

## Pièce de référence
- Déclaration de l'épreuve des témoins v9 (`/home/user/controle-ia-travail-organisme/docs/notes/organisme-auto-conception-v1/course-v4/declaration-relais-epreuve-temoins-auto-conception-v9.json`) : empreinte 23c4a1c02ca512e8e3f97b250ebca66ebdcf283440ea56522c7ea7b3f99c145f, égale à son compagnon ; MODELES_CLAUDE relevé à sa ligne 5.

## Commandes
```
mkdir /home/user/relais-ligne-3-etage-2-portee-200-v1
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/relais-ligne-3-etage-2-portee-200-v1/console-relais-claude-v1.txt 'PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_LUC' -- /usr/bin/python3 -I -B /home/user/lciric/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_LUC --port 8787 --plafond-usd 88.36 --modeles-permis MODELES_CLAUDE --journal /home/user/relais-ligne-3-etage-2-portee-200-v1/journal-relais-claude-v1.jsonl
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/relais-ligne-3-etage-2-portee-200-v1/console-relais-argon-v1.txt 'PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY' -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle GEMINI_API_KEY --port 8788 --max-appels 2410 --journal /home/user/relais-ligne-3-etage-2-portee-200-v1/journal-relais-argon-v1.jsonl
env -C /home/user/relais-ligne-3-etage-2-portee-200-v1 sha256sum declaration-relais-ligne-3-etage-2-v1.json > /home/user/relais-ligne-3-etage-2-portee-200-v1/declaration-relais-ligne-3-etage-2-v1.json.sha256
```

## Codes de sortie
- mkdir : 0 (dossier absent avant)
- Lanceur du relais Claude : 0 (`noms_absents` vide)
- Lanceur du relais Argon : 0 (`noms_absents` vide)
- Compagnon de la déclaration : 0

## Identifiants de processus
- PID_CLAUDE : 7533
- PID_ARGON : 7563

## Déclaration
- Chemin : `/home/user/relais-ligne-3-etage-2-portee-200-v1/declaration-relais-ligne-3-etage-2-v1.json` (forme du bloc du § 9, terminée par un saut de ligne comme le précédent)
- Empreinte : 58cec5678b174d2929e50b22be9c13514316d8a4e308fb75c5c129ed794be376

Aucune requête aux relais, aucune valeur de clé lue ni écrite, aucune écriture dans un dépôt.
