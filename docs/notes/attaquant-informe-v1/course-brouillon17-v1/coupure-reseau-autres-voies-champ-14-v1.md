# Machine du banc (champ n° 14) : les voies moins chères pour couper le réseau

- Note de classe C, écrite par la session fille de l'attaquant informé le 22 novembre 2026, à la demande de la mère, après le refus de Lazar : le serveur dédié à 209 € d'installation est « trop cher ».
- Elle complète la note `coupure-reseau-fournisseurs-champ-14-v1.md` (`bcb9e341…`) sans la remplacer.
- Aucune location ni aucun compte n'a été fait. Les prix de Vast.ai ont été relevés le 22 novembre vers 14:05Z par son interface de recherche d'offres, en lecture seule. Les autres prix viennent des pages officielles, lues par un outil de lecture qui résume. Ils sont **à relever mot pour mot le jour du devis**.
- Conversion à **0,92 € par dollar**, taux approximatif, à relever le jour du devis. Tous les prix sont hors taxes.

## Ce qu'exige la pièce de sécurité, et ce qui change tout

La pièce de sécurité v16, section 2, demande « deux niveaux, toujours ». Ce sont soit **le pare-feu du fournisseur**, soit **un bac intérieur pour l'agent, les gardes vivant dans l'enveloppe louée**. **Le pare-feu du fournisseur n'est donc pas obligatoire.** Une machine où nous avons les droits root suffit, à trois conditions :
- un pare-feu posé par nous dans la machine ;
- l'agent dans un conteneur sans aucune interface réseau ;
- une preuve par un test.

La coupure doit couvrir le réseau sortant, les adresses locales au lien, le service de métadonnées et la résolution de noms. Seul reste le canal d'administration entrant.

## Les heures à payer

| Poste | Heures | Source |
|---|---|---|
| Répétition à blanc sur la machine réelle | environ 4, estimation à fixer au devis | course, ligne « Répétition à blanc », GO à part |
| Répétition générale | 12 au plus | répétition, plafond |
| Course | 48 au plus | course, champ n° 7 |
| **Total** | **environ 64 au plus** | |

Les plafonds sont des maximums. La durée réelle se fixe à la répétition, par la règle « épisodes × durée médiane × 1,5 ».

## Les voies, avec leur coût total pour environ 64 heures

| Voie | Prix horaire relevé | Coût total estimé | Ce que la documentation établit | Conforme à la pièce ? |
|---|---|---|---|---|
| **(a) Machine virtuelle Vast.ai, carte de 24 Go en Europe, coupure faite par nous** | 0,243 $ (RTX 4500 Ada, Danemark, offre `61496095`) ; 0,368 $ (RTX 3090, Québec) ; 0,47 $ (RTX 4090, Espagne) | **environ 16 €** au moins cher, de **22 à 29 €** sinon, disque compris (60 Go, environ 1,5 $) | root par SSH ; machine virtuelle complète, avec systemd (`docs.vast.ai/documentation/instances/virtual-machines`). Pare-feu côté fournisseur : non établi. iptables et nftables : non établis par la documentation, mais attendus d'un noyau complet | **oui**, si le test le prouve : pare-feu dans la machine, plus un bac de l'agent sans réseau |
| (b) Conteneur Vast.ai | dès 0,14 $ | environ 10 € | capacité NET_ADMIN non établie, conteneur dans le conteneur exclu (note précédente) | **non** : aucun des deux niveaux n'est établi |
| (c) Scaleway L4 24 Go, Paris | 0,79 € | **environ 51 €** | groupes de sécurité, sortie par défaut réglable en refus (`outbound-default-policy=drop`). Root : non établi. Deux pages se contredisent sur le groupe par défaut. Les pages ont répondu 403, d'où des extraits de recherche seulement | **oui** : pare-feu du fournisseur, plus un bac de l'agent |
| (d) Lambda, Quadro RTX 6000 24 Go | 0,69 $ | environ 41 € | pare-feu entrant seulement ; sortant non établi ; root non établi | oui, seulement si la coupure est faite par nous comme en (a) ; plus cher que (a) |
| (e) RunPod, conteneurs | dès 0,16 $ (A5000, Community Cloud) | environ 10 à 30 € | conteneurs seulement, on ne peut pas lancer son propre Docker, NET_ADMIN non établi | **non** : pas de bac intérieur possible |
| (f) OVHcloud L4 | environ 0,91 $, non confirmé | environ 54 € | non établi | non établi |
| Hetzner Cloud | — | — | aucune carte graphique facturée à l'heure | sans objet |

**Ne couper que pendant la phase qui en a besoin** : c'est déjà le cas dans le texte. Le réseau reste ouvert pour la pose (poids, dépendances, code), puis il est coupé avant l'arrivée du lot. Les moniteurs lisent hors du banc, après coup. Cette option ne change donc pas le prix, qui ne dépend que des heures. En revanche, une phase de lecture des activations sur une autre machine plus petite, après la coupure, ne réduirait la facture que si cette phase est longue, ce qu'elle n'est pas ici.

## La coupure faite par nous, et sa preuve (voie a)

1. **Niveau 1, la machine.** Un pare-feu nftables posé par l'opérateur avant l'arrivée du lot :
   - en sortie, politique « refuser » ;
   - seules exceptions : les réponses de la connexion SSH entrante déjà établie ;
   - blocage explicite des adresses locales au lien (dont 169.254.169.254, le service de métadonnées), d'IPv6 et des résolveurs de noms.
2. **Niveau 2, le bac de l'agent.** Le conteneur de l'agent est lancé sans interface réseau (`--network none`). Les gardes, le journal et le chien de garde tournent hors du conteneur, dans la machine.
3. **La sonde**, la garde 1. Un programme de classe B tente depuis la machine et depuis le bac :
   - une connexion TCP vers une adresse publique, une requête UDP, une requête de noms, une sortie ICMP ;
   - l'accès au service de métadonnées ;
   - l'accès en IPv6.
   Il attend un échec pour chacune, et il vérifie que l'accès SSH entrant de l'opérateur répond. Il est **éprouvé sur un cas sain et sur un artefact** (R5) : pare-feu volontairement ouvert, il doit signaler la fuite. Il tourne à la répétition à blanc, puis à chaque pose.
4. **Réserve propre à Vast.ai.** L'accès SSH peut passer par un relais de Vast.ai, et couper la sortie pourrait casser ce relais. La machine virtuelle avec SSH direct est donc la voie à prendre. Elle s'établit à la répétition à blanc, sur environ 4 heures payées : si elle ne tient pas, on bascule sur (c) avant toute course.

## Décision

- **Décision** : quelle machine pour le banc, à la place du serveur dédié ?
- **Enjeu** : tenir les deux niveaux de coupure de la pièce de sécurité sous 30 €.
- **Option (a), machine virtuelle Vast.ai en Europe, coupure par nous, prouvée par la sonde.**
  - Avantage : environ 16 à 29 € pour tout, sans frais d'installation, et le programme connaît déjà Vast.ai.
  - Inconvénient : aucun pare-feu côté fournisseur, donc tout repose sur notre coupure et sur sa preuve. L'hôte est tenu par un tiers. Le relais SSH reste à établir.
- **Option (c), Scaleway.**
  - Avantage : pare-feu sortant du fournisseur, documenté, plus le bac de l'agent ; hébergement à Paris.
  - Inconvénient : environ 51 €, au-dessus de la cible. La documentation est à relire, car deux pages se contredisent.
- **Option (d), Lambda avec coupure par nous.**
  - Avantage : un fournisseur établi.
  - Inconvénient : environ 41 €, pour le même mode de coupure qu'en (a).
- **Recommandation** : (a), confiance 0,65, avec (c) en repli si la répétition à blanc montre que la coupure ou le SSH direct ne tiennent pas. Les 4 heures de répétition à blanc coûtent environ 1 € et lèvent le doute avant la course.
- **Défaut** : aucun, c'est une dépense ; le devis vient ensuite.

## Réserves

- **Mémoire de la carte** : il n'est pas établi que 24 Go suffisent pour le modèle de 8 milliards de paramètres avec l'extraction des activations. En demi-précision, les poids font environ 16 Go. À mesurer à la répétition à blanc ; sinon, une carte de 48 Go coûte environ 0,80 $ de l'heure chez Vast.ai, soit environ 47 € pour 64 heures.
- **Prix** : ceux de Vast.ai sont des offres d'un marché, qui changent d'heure en heure ; l'offre citée peut disparaître. Les autres prix viennent de résumés de pages.
- **Lieu** : les offres moins chères hors d'Europe et d'Amérique du Nord (Shanghai, 0,16 $) sont écartées par prudence, mais sans règle écrite qui l'exige. C'est à dire au devis.
- **Écart de mot** : la note précédente recommandait le serveur dédié parce que le pare-feu du fournisseur y est documenté. La présente note s'appuie sur l'autre branche que la pièce admet, le bac intérieur.
