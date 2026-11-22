# Coupure du réseau chez deux fournisseurs — champ n° 14 du banc fermé — v1

- **Classe** : C. Aucune dépense, aucun compte, aucun appel aux interfaces des fournisseurs.
- **Auteur** : Opus 5.5 neuf. **Date** : 2026-11-22, 13:40 UTC.
- **Pièces lues** : pièce de sécurité du banc fermé v16, lignes 1 à 12 et 87 à 127 (« 2. Confinement »), branche `origin/claude/piece-securite-banc-ferme-v1`. Pages publiques des fournisseurs ci-dessous, lues le 2026-11-22.

Pages : [V1] https://docs.vast.ai/guides/instances/connect/networking ; [V2] https://docs.vast.ai/guides/instances/docker-environment ; [V3] https://docs.vast.ai/guides/reference/faq/instances ; [V4] https://docs.vast.ai/guides/instances/virtual-machines ; [V5] https://docs.vast.ai/guides/templates/introduction ; [H1] https://docs.hetzner.com/cloud/firewalls/overview/ ; [H2] https://docs.hetzner.com/cloud/firewalls/faq/ ; [H3] https://docs.hetzner.com/robot/dedicated-server/firewall/ ; [H4] https://docs.hetzner.com/robot/dedicated-server/server-lines/gpu-server/ ; [H5] https://www.hetzner.com/dedicated-rootserver/matrix-gpu

## Ce que la pièce attend

Pare-feu du fournisseur ou bac intérieur pour l'agent, sinon le fournisseur ne convient pas ; coupure des adresses locales au lien, du service de métadonnées et de la résolution de noms ; seul reste le canal d'administration entrant.

## Vast.ai

| Niveau attendu | Ce que dit la documentation |
|---|---|
| Pare-feu du fournisseur, hors machine, sortant coupé, entrée d'administration gardée | Non établi. Seule phrase trouvée : « Vast.ai docker instances have full internet access » [V1]. |
| Règles locales dans le conteneur (iptables, nftables, capacité NET_ADMIN) | Non établi. « Vast.ai instances run as Linux Docker containers » [V2] ; options documentées : variables, nom d'hôte, ports [V2] ; capacités non mentionnées. |
| Bac intérieur dans une instance conteneur | Exclu : « Vast.ai does not support Docker-in-Docker due to security constraints » [V3]. |
| Bac intérieur dans une machine virtuelle Vast.ai | Possible : environnement Linux complet, « nested containerization », mode SSH seul [V4]. Droits root et pare-feu local : non établis par la page. |
| Service de métadonnées, adresses locales au lien, résolution de noms | Non établi. |
| Image avec pilotes | `vastai/base-image`, `vastai/pytorch`, « CUDA development libraries » [V5] ; pilote de l'hôte non dit. Images de machine virtuelle : `docker.io/vastai/kvm`, avec CUDA [V4]. |
| Limites | Adresse publique partagée, ports internes mappés sur des ports externes au hasard, 64 ports au plus [V1]. Hôte tenu par un tiers. |

## Hetzner

| Niveau attendu | Ce que dit la documentation |
|---|---|
| Hetzner Cloud : pare-feu sortant | Oui : règles entrantes et sortantes [H1] ; une règle sortante fait passer la sortie en refus implicite [H2]. Mais « Metadata server requests also do not go through the firewall », et le trafic vers le résolveur de noms de Hetzner est toujours permis [H2] : deux trous que la pièce nomme. |
| Hetzner Cloud : carte graphique | Non établi ; les offres trouvées sont des serveurs dédiés [H4, H5]. |
| Serveur dédié : pare-feu du fournisseur | Oui, sur le port du commutateur, « incoming and outgoing traffic » [H3]. Sans état : le retour du canal d'administration demande sa propre règle sortante. Dix règles par sens au plus ; paquet sans règle rejeté ; IPv4 seul par défaut, filtrage IPv6 en option ; « ICMPv6 traffic to and from the server is always allowed » [H3]. |
| Serveur dédié : règles locales | « Full root rights, rescue system » [H4] : nftables et conteneur de l'agent sous compte sans privilèges possibles, les gardes sur l'hôte loué. |
| Service de métadonnées, adresses locales au lien | Non établi pour les serveurs dédiés. |
| Image avec pilotes | Systèmes listés (Ubuntu, Debian selon le modèle) [H5] ; « support CUDA technology » [H5] ; pilote préinstallé non établi (à poser soi-même avant la coupure). |
| Carte pour 8 milliards de paramètres | Le plus petit modèle listé : 24 Go de mémoire graphique [H4, H5]. Suffisance avec extraction d'activations : à chiffrer au devis. |
| Limites | Frais d'installation listés pour chaque modèle (le plus petit : 209 € hors taxe), facturation horaire listée [H5] ; durée minimale non dite. |

## Recommandation

- **Décision** : quel fournisseur et quelle forme de machine inscrire au champ n° 14.
- **Enjeu** : ne pas découvrir à prix payant que la coupure à deux niveaux est impossible.
- **Option 1, serveur dédié Hetzner à carte graphique** : avantage, deux niveaux établis par la documentation (pare-feu du commutateur dans les deux sens, root pour nftables et un bac intérieur) ; inconvénient, frais d'installation, pare-feu sans état à dix règles, ICMPv6 non filtré, pilote à poser.
- **Option 2, machine virtuelle Vast.ai** : avantage, prix à l'heure et choix de cartes plus larges, bac intérieur possible ; inconvénient, aucun pare-feu du fournisseur établi, root et pare-feu local non dits, hôte tiers, moins de machines.
- **Option 3, instance conteneur Vast.ai** : avantage, la plus simple ; inconvénient, ni pare-feu du fournisseur ni capacité réseau établis, bac intérieur exclu : ne convient pas au sens de la pièce tant que NET_ADMIN n'est pas établi.
- **Recommandation** : option 1, avec pare-feu du commutateur (entrée et retour limités à l'adresse du poste de l'opérateur, IPv6 filtré, rien d'autre en sortie), nftables sur l'hôte, ICMPv6 bloqué localement, agent dans un conteneur sans réseau ; option 2 en repli si le devis l'exige. **Confiance** : moyenne.

## Réserves

- Citations tirées par un outil qui résume ; textes exacts à relever à la main avant le scellement du préenregistrement.
- « Non établi » n'est pas « impossible ».
- Prix lus le 2026-11-22 ; une recherche du jour citait d'autres montants, non retenus.
- Le service de métadonnées des serveurs dédiés Hetzner n'est pas établi : l'épreuve de la garde 1 doit le sonder sur le banc.
- Les autres gardes de la pièce ne sont pas jugées ici.
