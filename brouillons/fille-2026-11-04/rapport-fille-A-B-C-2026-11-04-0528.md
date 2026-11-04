# Rapport de la fille neuve — tâches A, B, C — 2026-11-04-0528 UTC (date -u)

Session fille `session_01Qi7Gr3s7JVgpRP17VcSyAf`. Ordre principal `docs/procedures/ordre-fille-neuve-2026-11-04-v1.md` (6b366b95…). Ordre C : `docs/procedures/ordre-fille-collisionneur-sparks-v1.md` (cdc1d19d…).

## Tâche A — appel unique à Astra (GO-2026-11-04-01) : faite
- Code 0 ; modèle servi `gpt-6-astra` (égal au modèle demandé) ; fin « stop » ; une seule tentative, aucune relance.
- Effort de raisonnement : réglage par défaut de l'interface. La commande 8807 n'en transmet aucun.
- Jetons : 9 949 en entrée ; 3 199 en sortie, dont 512 de raisonnement.
- Dépense : appel 0,25944 USD + appel de contrôle 0,00034 USD = **0,25978 USD**.
- Branche `donnees/appel-astra-sparks-v1`, commit `31c0af1642df3dfdb7fd53c6d24379065fbe210d`.
- Liste `EMPREINTES-appel-astra-sparks-v1.txt` : `9481e3211f5ebc098fadc990f20d935f35ee30ca7cc60c3566122b68e2acf444`. Prompt `66346ed0…`. Réponse brute `b9050edc…`.

## Tâche B — seconde course d'A1-v3 (GO-2026-11-03-01) : INTERROMPUE par l'infrastructure
- Vérification `--verifier-seulement` en code 0. Garde de session éprouvée sur `sleep 900` (PID 1985, fin détectée à 02:02:45Z). Contrôle d'Argon fait sur un relais temporaire distinct (port 8815), code 0, 0,00064 USD.
- Départ à 02:03 UTC. Processus : lanceur 4322, relais 8805 2885, guetteur 4406.
- Le conteneur de la fille a redémarré. Dernier relevé de garde à 03:44:11Z, lanceur vivant. Dernier appel au relais à 03:45:18Z. Après le redémarrage (démarrage 05:22:53), plus aucun processus.
- Code de sortie du lanceur : **aucun**. Le processus est mort avec le conteneur ; ni `wait` ni `/proc` ne sont possibles après coup.
- Écart d'enregistrement déclaré et accepté par la mère : le lanceur avait été détaché sans enveloppe qui écrit son code.
- Compteurs du relais (statuts seulement) : 620 appels, 615 OK, 5 ECHEC. Les échecs étaient passagers : connexion réinitialisée, coupure distante, HTTP 503. Les alertes du guetteur sont à 03:13 et 03:38. Aucune cause durable, donc aucun message pendant la course.
- Le relevé horaire du guetteur a rendu une fois une erreur de lecture JSON, visible dans son journal.
- Dépense : **48,49583 USD** selon le relais, plus le contrôle 0,00064 USD.
- État interrompu scellé avant lecture : `EMPREINTES-sortie-a1-v3-seconde-interrompue-v1.txt` `fd66feb72b46b6a088c2d01b9d6aaefe38ef151713e8eee6cba7b8e4e863dae0` (19 fichiers).
- Branche neuve `donnees/attaque-goodhart-v3-a1v3-seconde-interrompue-v1`, commit `cef64e676ec50cd300dfd3c07c23f8b6041998e2`. Nom calqué sur le précédent de la première course, au lieu de `…-seconde-v1` prévu pour une course finie.
- Rien n'a été relancé. La sortie n'a pas été lue.

## Tâche C — collisionneur v9 sur Sparks, sans Argon (GO-2026-11-04-02) : finie
- Lancée à 02:04:34Z, finie à 03:04:49Z, code 0. `verifier` en code 0, fait avant le scellement. Aucune « ALERTE » de clé au journal du lanceur.
- Deux défauts de la commande exacte du LISEZMOI, corrigés à l'exécution :
  - (1) La course entre `echo $!` et la boucle R12. Correction acceptée par la mère : le fichier PID orphelin (contenu 4493, sha256 7993945b…) a été supprimé, puis la boucle a tourné au premier plan.
  - (2) `setsid` s'est dédoublé, donc `$!` = 4767 est le parent sorti aussitôt. Enveloppe réelle : 4769, consignée dans `lanceur-sparks-v9-sans-argon-v1.pid-reel`.
- 12 cellules, toutes OK, modèle servi égal au modèle demandé, aucune relance. Les trois cellules C sont en « absence acceptée ».
- Clé Anthropic utilisée par le lanceur : `RR_ANTHROPIC_API_KEY_3`, selon `controle-sparks-sans-argon-v1.json`. Le LISEZMOI exigeait `…_LUC`.
- Le préambule servi dit toujours « cinq modèles ».
- Dépense par espèce :

  | Espèce | Coût |
  |---|---|
  | A Fable 5.1 | 4,1979 USD |
  | B Opus 5.5 | 1,9990 USD |
  | D Kimi K3.1 Pro | 0,7347 USD (relais : 0,735708 USD, 4 appels) |
  | E GPT-6 Astra | 1,9176 USD |
  | Tour | **8,8492 USD** |
  | Contrôle ABDE | 0,0022 USD |
- Branche `donnees/collisionneur-v9-sparks-v1-run` (partie de 54538ee6), commit `3f8be5c0d67531793ac0496b0bcdc066577e790d`.
- Liste `EMPREINTES-tour-sparks-v9-sans-argon-v1.txt` : `fb7ce8fa2c86ca57d1ddbce75c5ee044503d770b1a2bf67e5d7bb1d35346a079` (50 fichiers).
- Aucun relais restant : conteneur redémarré.

## Autres
- Inventaire Vast à 01:50 : trois instances « R8 » actives, aucune arrêtée.
- `HF_TOKEN` → `google/gemma-3-270m-it` : HTTP 200.
- Garde des secrets : 0 avant chaque poussée.
- Outils de la fille, hors dépôt :
  - `garde_secrets_v1.py` 606902b9…, éprouvée sur un cas sain et sur deux artefacts ;
  - `garde_session_v1.sh` 9de216b0… ;
  - `guetteur_a1v3_seconde_v1.sh` 5729515e….
- **Dépense totale de la session : 0,25978 + 48,49647 + 8,8514 ≈ 57,61 USD.**
