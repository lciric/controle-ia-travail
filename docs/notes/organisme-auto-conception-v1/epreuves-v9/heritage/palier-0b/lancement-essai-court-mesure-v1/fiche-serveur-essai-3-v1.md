# Fiche du serveur loué pour l'essai 3 du palier 0b — v1

Pièce de travail (classe C), écrite par la session du compte organisme le 2026-11-22 vers 02:25Z. **Fiche retenue par la mère dans son message de 02:21Z, qu'elle cite (R-4753).** Elle complète le devis v5 (`devis-serveur-loue-palier-0b-essai-3-v5.md`, même dossier). Elle ne change ni le devis, ni le GO, ni la dépense.

| Champ de la requête de création | Valeur | Source |
|---|---|---|
| `name` | `essai-3-palier-0b` | cette fiche |
| `server_type` | `cpx42` (8 cœurs partagés, 16 Go, 320 Go de disque, 0,1134 EUR/h) | devis v5, ligne 15 |
| `location` | `hel1` | devis v5, ligne 15 |
| `image` | `debian-13` | devis v5, ligne 17 |
| `public_net.enable_ipv4` | vrai (0,00096 EUR/h) | devis v5, ligne 15 |
| `public_net.enable_ipv6` | vrai | cette fiche (voir 1.) |
| `start_after_create` | vrai | cette fiche |
| `ssh_keys` | aucune (liste vide) | cette fiche (voir 2.) |
| `user_data` | données du fabricant v8 (`a91f3403…`), contrôlées et envoyées par l'outil de contrôle de sortie, sans relecture | pile retenue par la mère, 02:02Z |

1. **IPv6.** La réponse de prix relevée le 2026-11-21 (`prix-releve-v1/reponse-pricing-hetzner-2026-11-21T181602Z.json`) ne donne de prix aux adresses primaires que pour l'IPv4. Aucune ligne n'y figure pour l'IPv6, donc aucun coût n'est affiché.
2. **Aucune clé SSH.** La machine est autonome : elle se pilote par ses données de démarrage et rend ses résultats par poussée HTTPS. De plus, le port 22 sortant est fermé depuis la session. Sans clé, Hetzner crée un mot de passe root :
   - il paraît dans la réponse de création, d'où l'outil l'expurge avant tout relevé ;
   - il est envoyé par courriel au titulaire du compte, et ce courriel reste chez Lazar.
3. **Garde-fous de durée, inchangés.** L'arrêt du programme est fixé à H0 + 94 h, par le gardien et par un filet sur le groupe de processus. La destruction se fait à H0 + 98 h, par l'identifiant du serveur, depuis la session du compte organisme. Elle est consignée dans `registres/arrets.md`.
