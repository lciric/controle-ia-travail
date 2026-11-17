# Témoin de Bailey — confirmation interrompue faute de crédit Vast ; reprise prête, en attente du crédit

**En tête (addendum 7, § 4 et § 5 (e)) : gel de `src/` sur la branche `claude/compassionate-meitner-d4ryyk`** (arbre
égal à celui de `a904aa39` jusqu'au dernier contrôle final) ; **aucune note ni aucun verdict du témoin n'est lu avant
la clôture de la confirmation** (§ 3).

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, 17 novembre 2026, 20:40Z.

## Fait
- Confirmation lancée sur le mot de Lazar (« go, lance la confirmation ») : poste Hetzner 176451822 créé 09:16:39Z ;
  offre 59431050 (machine 146915 du Texas, 1,33 USD/h carte et stockage) ; mise en place et contrôle du juge passés ;
  règle à 10:36:33Z : t = 1 265 s (garde du § 2.3 passée), K = 72 ; run principal lancé 10:36:37Z.
- Recharge automatique de Vast en échec depuis au moins 15:41Z (`billing_failed` vrai) ; alertes à Lazar ; instance
  61049303 arrêtée par Vast vers 17:12Z (solde négatif).
- Conduite finie à 17:44Z : instance injoignable, transfert impossible, **instance gardée arrêtée, non détruite**
  (`bilan-conduite-v5.json` : « reprise requise » pour toutes les étapes) ; dépense au bilan 11,08 USD ; poste v13 :
  marque de fin et liste `repertoires-sortie-conduite-v15-v1.txt` poussées, puis serveur détruit par identifiant (R10,
  `registres/arrets.md`).
- Pièces de reprise (lecture 38) scellées après contre-lecture : `poste-hetzner-reprise-v4.sh`,
  `construire-donnees-demarrage-reprise-v4.py` (`contre-lecture-reprise-confirmation-bailey-v1.md`) : gardes « conduite
  v15 finie », instance 61049303 arrêtée seule du témoin, crédit Vast positif sans échec ; liste des répertoires du
  dossier de reprise neuf.

## État à 20:38Z
Vast : `credit` 0, `balance` −0,99 USD, `billing_failed` vrai. Instance 61049303 présente, `exited`.

## Reste (prochaine action)
1. Dès que Lazar a crédité Vast (et `billing_failed` faux) : relevé du § 2.5, constructeur reprise v4 dans un dossier
   neuf hors du dépôt, empreinte du script comparée à `poste-hetzner-reprise-v4.sh.sha256`, création du poste de reprise
   sous `GO_ID=GO-2026-11-17-07` ; surveillance ; après la reprise, destruction du poste de reprise par identifiant.
2. Si l'exécution du run principal compte moins de 20 tours complets (champ technique du transfert) : relance de la
   l. 371, pièces neuves contre-lues, dans `GO-2026-11-17-07` (recommandation consignée d'avance, mot du 17 novembre).
3. Si l'instance disparaît avant la reprise : « journaux perdus, pas de verdict de confirmation » (§ 3, cause (ii)) ;
   clôture ; puis la lecture du § 3.
4. À relayer (inchangé) : serveur de sauvegarde Hetzner 176187199 ; dépôt chez le tiers des addenda 3 à 7 ; retrait de
   la clé de déploiement et de la clé ssh Vast 1864483 ; révocation du jeton GitHub.

## Instances actives
Vast : 61049303 (témoin, arrêtée, gardée pour la reprise). Hetzner : 176187199 (sauvegarde). Aucun poste du témoin.
