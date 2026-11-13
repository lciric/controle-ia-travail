# Témoin de Bailey, troisième série — reprise refusée (hôte indisponible) ; nœud — 13 novembre 2026

Session `session_01XJ6MgnEhQMZteN9F8a1BST`. Ne se réécrit pas (R12). Suit `…-0548-…-instance-injoignable-reprise.md`
(`b797cb97…`). Aucune note lue.

## Faits
- Poste de reprise v1 (175945214) : arrêté de lui-même à 05:52:54Z sur une garde reprise par erreur du poste v11
  (« aucune instance du témoin ») ; rien touché ; détruit à 05:53:45Z. Défaut de la session, corrigé en v2.
- Poste de reprise v2 (175945720, `poste-hetzner-reprise-v2.sh`, `6deb5bcb…`) : inventaire conforme, `lanceur_v17
  reprendre` lancé à 05:57:59Z ; **redémarrage refusé par Vast** (`demarrer` lève `GardeArret`, 18,6 s) ; instance
  remise à l'arrêt (arrêt accepté, statut relu `exited`) ; veilleur d'arrêt arrêté par PID ; **pas de transfert, pas de
  destruction** ; bilan `sortie-conduite-v11/reprise-v10/bilan-reprise-v10.json` (scellé par la reprise) : alerte
  « redémarrage refusé (GardeArret) : instance gardée arrêtée ; nœud » ; D = 11,860 USD (compte prudent : les
  intervalles arrêtés comptent au taux c = 1,342 USD/h ; dépense réelle à l'arrêt : stockage seul) ; reste ≈ 46,6 h avant
  la borne B − 0,5. Poste v2 détruit à 06:10:05Z.
- Machine 146915 (hôte de 60417353) : **aucune offre louable** à 06:09Z (`rentable: false` sur ses quatre offres) :
  hôte indisponible, cohérent avec un redémarrage de l'hôte vers 04:21Z. Cause non établie.
- Les journaux de la première exécution (run principal interrompu, K′ inconnu, ≈ 9 à 10 tours attendus d'après la durée
  d'un tour du pilote) sont sur le disque de l'instance arrêtée, non transférés.

## Nœud — décision de Lazar
Enjeu : la lecture 38 interdit toute destruction avant un transfert qui fait foi ; le transfert exige que l'hôte revienne ;
chaque heure d'arrêt compte 1,34 USD dans D (compte prudent) et réduit le K d'une relance.
- (a) **Attendre l'hôte, reprise automatique** : un poste de reprise « en attente » relit l'offre de la machine 146915
  toutes les 10 min, au plus 24 h, et lance `reprendre` dès qu'elle est louable ; aucune dépense de carte avant.
  Avantage : la procédure scellée, intacte. Inconvénient : D monte de ≈ 32 USD par jour d'attente ; l'hôte peut ne pas
  revenir.
- (b) **Relance tout de suite sur une instance neuve**, l'instance 60417353 gardée arrêtée jusqu'au retour de l'hôte (puis
  reprise, scellement sans lecture, destruction). Avantage : le run avance ; seule la relance porte le verdict.
  Inconvénient : K′ < 20 n'est pas mesuré (seulement attendu d'après les durées) ; D compte les deux instances ;
  instance neuve : mot de lancement exprès nécessaire (la lecture de la condition 7 a expiré à 08:14Z).
- (c) **Arrêter le témoin** : pas de verdict ; instance gardée arrêtée jusqu'au transfert, puis détruite.
Recommandation : (a) pour 24 h au plus, puis (b) si l'hôte ne revient pas ; confiance moyenne. Pas de défaut : nœud.
