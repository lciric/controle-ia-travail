# Témoin de Bailey — option (c), poste Hetzner : mot de Lazar, plan et pièces — 12 novembre 2026, 12:50 UTC

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Suit `2026-11-12-0905-…`
(`72181cde…`). Ne se réécrit pas (R12).

## Mot de Lazar
« go c » (≈ 12:20 UTC), sur l'option (c) : « une petite machine louée à l'heure (Hetzner, comme pour l'organisme,
quelques centimes de l'heure) ; dépense hors ligne de GO : GO requis ». **Ligne de GO à inscrire sur `main` par la
mère** (proposition : type calcul, « poste de pilotage Hetzner du témoin de Bailey », plafond **5 USD**, échéance
2026-11-30, accordé par Lazar, référence : cette note). Coût attendu : `cx23` à Falkenstein, 0,01056 EUR/h TTC
(API Hetzner, 12:30Z), moins de 1 EUR pour trois jours.

## Constat qui fixe le plan
Aucun `ssh` ne sort de la session : port 22 refusé ; sur le 443, le mandataire répond « HTTP/1.1 400 Bad Request » au
lieu du serveur (essai `ssh -p 443 git@ssh.github.com`). La session ne peut donc pas piloter la machine louée par `ssh` :
la machine est **autonome**, créée par l'API Hetzner (HTTPS), démarrée par ses données de démarrage, et rend compte par
`git` sur cette branche. La session surveille par `git fetch`, l'API Hetzner et `vastai show instances`, et détruit la
machine par l'API à la fin.

## Pièces
- `runs/temoin-bailey-v1-20261111/lancer-conduite-v5.py` : sortie, bilan, PID neufs (v5) ; instances antérieures
  60280913, 60326443, 60330510 (D antérieure 1,537 USD, égale au bilan v4).
- `runs/temoin-bailey-v1-20261111/poste-hetzner-v1.sh` : script de démarrage (secrets posés en fichiers 600, jamais
  imprimés ; Debian 12, Python 3.11 ; clone de la branche au même chemin absolu ; `main` en refspec explicite ;
  empreintes du script v5 et du manifeste vérifiées ; commit 4988f3f4 présent ; inventaire Vast sans instance du poste ;
  offre la moins chère du filtre de l'ordre v4, carte et 200 Go de stockage compris, écrite dans
  `offre-choisie-v5.json` avant la création ; conduite sous `GO_ID=GO-2026-11-10-10` ; journaux poussés toutes les
  10 minutes ; marque `poste-fini-v1.json`). Aucune reprise ni relance automatique.
- `runs/temoin-bailey-v1-20261111/construire-donnees-demarrage-v1.py` : assemble les données de démarrage hors du
  dépôt (fichier 600), n'imprime aucun secret, refuse au-delà de 32 Kio. Essai : 9 634 octets, syntaxe correcte.

## Accès requis
- Clé de l'API Hetzner : enregistrée par Lazar (formulaire sécurisé, 12:30Z) ; lecture vérifiée (aucune machine).
- **Clé de déploiement GitHub avec écriture** sur `lciric/controle-ia-travail` : à ajouter par Lazar (ou sur son mot) :
  `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGVJDYc+972P7NaapXAQeyZoepOfXNbDBIAv3VHzFQ1i poste-hetzner-temoin-bailey-20261112`
  (empreinte `SHA256:VW9jZJAwK2LruuNz9eGdJkp4uyhbjyfz3anq8gLitF4`). À retirer en fin de run, avec la clé Vast 1864483.
- Secrets déposés sur la machine Hetzner (données de démarrage, stockées chez Hetzner) : clé Vast, jeton Hugging Face,
  clé de déploiement, clé `ssh` de session. La machine est détruite en fin de run.
