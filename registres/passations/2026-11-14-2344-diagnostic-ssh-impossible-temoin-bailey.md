# Note — témoin de Bailey : diagnostic par `ssh` accordé, impossible depuis cette session — 14 novembre 2026, 23:44 UTC

Session `session_016QhUrudziqEQujXt4ofM8u` (compte neuf), branche `claude/compassionate-meitner-d4ryyk`. Ne se réécrit pas (R12).
Aucune note de sonde ni de juge lue.

## Constat (23:32-23:39Z, lecture seule)
- Instance Vast 60480302 : `running/running`, 37,7 h ; Vast affiche `gpu_util` 0,0, `gpu_temp` 21 °C, `cpu_util` 99,55,
  `vmem_usage` 22,5 Go (relevés Vast, possiblement périmés). Journaux du conteneur : seulement des connexions `ssh` du poste.
- Poste Hetzner 175967712 : réseau ≈ 0,2 à 3,7 Ko/s sur 6 h (sondages seuls, aucun transfert) ; battement à jour.
- Crédit Vast 8,56 USD, `billing_failed` faux, dernier paiement 23:01Z. D = 58,7 USD (calcul sur `poste-v5.json`, pas une
  facture) ; B − 2 vers 2026-11-15 11:46Z.
- Inventaire : 60599797 absente ; 60671759 « neuron-lens-volet-a » (autre chantier, 0,40 USD/h) non touchée.
- `verifier-arbre` : 113 problèmes (111 empreintes compagnons absentes sous `runs/temoin-bailey-v1-20261111/`, 2 sous
  `docs/notes/`) ; consignés, non corrigés.

## Décision et suite
- Mot de Lazar, verbatim : « Je recommande A, avec une confiance moyenne go » (option A : clé `ssh` de session, diagnostic
  en lecture seule).
- Clé créée (Vast, identifiant 1900274, 23:41Z) et attachée à 60480302 par l'interface web de Vast : la garde de calcul
  du dépôt bloque toute création par la ligne de commande Vast (motif prévu pour les lancements payants ; la ligne du GO
  du témoin manque au `registres/go.md` de cette branche) ; aucune instance créée, aucune dépense.
- Connexion refusée (direct 192.165.134.28:10140 et relais ssh4.vast.ai:39648) : le mandataire de la session ne passe
  que le HTTPS ; le `ssh` brut n'est pas pris en charge. Clé détachée et supprimée du compte aussitôt (23:42Z), clé privée
  effacée.
- Diagnostic non fait ; défaut B (garde à B − 2) en vigueur sauf autre mot de Lazar.
