# Note — Bailey : inventaire et versement scellé avant toute destruction (2026-11-19, 09:37Z)

**Mot direct de Lazar**, vers 08:47Z, verbatim : « avant toute destruction, inventaire et versement scellé de tout ce qui
reste sur la machine ». À la question de la session (vers 08:50Z : quelle machine ?), il répond : « Poste et instance
Vast ».

**État à 08:46Z.**
- La relance de la confirmation n'est pas finie, alors qu'elle était attendue vers 04:30Z : `principal-relance` court
  depuis le 18 novembre à 03:13:41Z, instance 61170458 en marche, poste v14 vivant, aucune marque de fin.
- Crédit Vast : 7,52 USD. Seule 61170458 est en marche. Recharge automatique configurée : seuil 5, montant 5.
- La surveillance du crédit était arrêtée depuis 04:10Z (redémarrage du processus de la session) ; relancée à 08:46Z.

**Contraintes.** Ce conteneur ne peut ouvrir ni ssh ni TCP brut vers l'instance ou le poste (refus du réseau sortant).
Le poste v14 n'a aucune clé de la session. Tout inventaire passe donc par un serveur qui exécute un script.

**Ce qui est fait.**
- **Instance** : poste d'inventaire v1 (`poste-inventaire-instance-v1.sh`, `14d3f1b3…` ; constructeur `05d7b744…` ;
  commit `cf8ba9cd`), serveur Hetzner 176778587, créé à 09:36:19Z sous GO-2026-11-17-07. Il fonctionne en lecture seule
  sur l'instance.
  - Une passe toutes les 20 min tant qu'elle existe : inventaire de tous les fichiers ; copie des fichiers de 25 Mio au
    plus hors poids, caches et clés ; contrôle des secrets ; versement dans
    `runs/temoin-bailey-v1-20261111/versement-instance-61170458-v1/`.
  - À la disparition de l'instance : index scellé, journal versé, marque `poste-fini-inventaire-instance-v1.json`.
  - Essais locaux de la sélection et du contrôle des secrets : un cas sain et des artefacts, conformes.
  - **Écart déclaré** : la contre-lecture (R2) suit le lancement au lieu de le précéder. Raison : la conduite scellée
    détruit l'instance dès la fin de la course, après son transfert, et cette fin peut venir à tout moment.
- **Limite, déclarée à Lazar dans la question.** En fin normale, la conduite transfère puis détruit l'instance seule ; la
  dernière passe d'inventaire précède donc la destruction de 20 min au plus. Dans les étapes, ce que la conduite
  transfère est scellé par elle.

**Ce qui suit.**
- **Poste v14** (176575468) : pas de destruction avant son inventaire. Il n'a pas d'accès entrant. Voie prévue : à sa
  fin, un instantané de son disque par l'API Hetzner ; un serveur neuf tiré de l'instantané inventorie et verse, scellé,
  tout ce qu'il contient, sans la valeur des clés ; destruction ensuite. Pièces à écrire et contre-lire.
- **Repli B′** : si le crédit tombe à 2,6 USD, le poste v14 est **éteint** (et non détruit), ce qui arrête la conduite.
  On attend une passe d'inventaire de l'instance postérieure à l'extinction, puis vient la reprise v7, qui transfère et
  détruit l'instance. La procédure est à mettre à jour.
- **Postes d'inventaire et de reprise** : chacun verse son journal avant sa propre destruction.
