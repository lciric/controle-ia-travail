# Collisionneurs v8d, compte rendu 56 : dossier des bancs plantés parti sur la v8m (13:15:46Z)

Écrit à 2026-11-22T13:16:18Z (`date -u`).

- La v8m est conforme. Son seul bloquant était un essai manquant : il est ajouté dans `test_collisionneur_v9_v8m_v2.py`, le code est inchangé (420394f9…), le mutant J3 est pris, et la confirmation vient du même contre-lecteur (`verification-corrections-collisionneur-v9-v8m-opus-v1.md`).
- **Départ à 13:15:46Z** : `runs/collisionneur-protocole-x-bancs-plantes-cinq-decisions-v1-20261122-131546`, enchaîneur v15, voie 3 (11349), GO-2026-11-22-53, plafond et ligne de 120 USD. Neuf modèles : Fable 5.2, Opus 5.5, Argon, Kimi (appel direct), Astra, Carbon, Neon, Opus 4.6, Fable 5.1. Options `--sortie-max --effort-max` ; délais de 10 800 s journalisés comme supposés ; rejeu unique en « xhigh » chez Anthropic. Mistral est déclaré absent.
- **Garde sur la clé Luc** (`garde_luc_v1.sh`, 11373) : seuil de 28 USD, pour 35 au plus avec un envoi en vol. Au-delà, elle arrête l'enchaîneur et la course par leur numéro.
- Incident sans effet : un premier lancement s'est arrêté au contrôle d'empreinte (chemin relatif) avant tout départ. Seul le verseur avait été relancé ; il l'est de nouveau (`registres/arrets.md`).
- Les cinq autres dossiers attendent ton mot, un par un. La v8n est en écriture.
