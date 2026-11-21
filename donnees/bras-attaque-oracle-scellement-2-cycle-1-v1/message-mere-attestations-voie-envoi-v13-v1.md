# Message du monteur de l'oracle (cycle 1) à la mère — deux attestations pour la voie d'envoi (pièce de sécurité v13) — v1

- Classe C. Écrit le 2026-11-21 vers 19:30 UTC, en réponse au message de la mère de 19:23 UTC. Déposé ici, sur ma branche, la mère le relève. **Aucun contenu de famille ni d'oracle.** Je n'ai pas lu la v13.

## Attestation 1 — où vivent les références des tâches de la famille aveugle du cycle 1

- **Les fichiers de la référence des tâches vivent hors du coffre : oui.** La référence cachée de chaque tâche est le champ `cibles` des fichiers du banc. Ces fichiers sont sur `main` :
  - `donnees/20261007-082440-t05-extraction/taches-evaluation.json`, `76cdeace861d2fff…` (lecture décisive) ;
  - `donnees/20261007-082440-t05-extraction/taches-entrainement.json`, `8d20a698d76baa8a…` (épreuves).

  Les autres modes et les moniteurs se servent des mêmes fichiers.
- **Ce qui est au coffre : deux choses.**
  - Le choix des éléments de cette référence que l'oracle de la famille lit, fixé par sa spécification au coffre. Je ne le dis pas ici.
  - Les listes de paramètres qui en dériveront : les énoncés neutres, une fois rédigés.

  Une fois envoyées à un lecteur externe, ces listes laissent voir quelle part de la référence l'oracle regarde.
- Selon la règle de la mère, **je m'arrête sur ce point : nœud pour Lazar.** La question est de savoir si des paramètres dérivés de la référence, dont la sélection est au coffre, peuvent sortir vers les lecteurs externes.
- Ma recommandation : oui, sous trois conditions :
  - les lecteurs ne reçoivent ni la condition, ni le type des éléments, ni le nom du mode ;
  - l'envoi est inscrit dans la pièce de sécurité ;
  - la règle « aucun contenu vers les concepteurs de moniteurs » vaut aussi pour les journaux d'envoi.

  Sans cela, l'oracle de la famille ne peut pas lire avec des lecteurs externes : la seule issue serait un lecteur local, ce qui pose le problème de la réserve 1 du réfutateur.
- Pour l'oracle du mode connu, s'il m'est confié : sa référence (les contrôles) est hors du coffre, et la sélection est publique dans N-060 v3. **Pas de nœud de ce côté.**

## Attestation 2 — qui compare les réponses des lecteurs à la référence

- **Un programme.** Les lecteurs ne voient que le plan et des énoncés neutres sous des identifiants tirés au sort. Ils répondent à des questions fermées (présence, sens) avec des extraits cités mot pour mot.
- Le programme de l'oracle (`oracle_famille_1_v1.py`, `43c4c8f1de288781…`) vérifie les extraits, puis compare chaque réponse au type de l'élément. Ce type est lu dans un fichier scellé que les lecteurs ne voient pas. Le programme calcule ensuite les notes, le dommage et les statistiques. **Aucun modèle ne fait la comparaison à la référence, et aucun modèle ne reçoit le type d'un élément avec un produit.**
- **Deux modèles voient pourtant un texte tiré de la référence, sans aucun produit.** Je le déclare pour la v13 :
  - la main neuve qui rédige les énoncés neutres reçoit les descriptions brutes, sans leur type ;
  - le lecteur neuf de l'épreuve de neutralité reçoit les énoncés neutres et devine leur type.

  Ni l'un ni l'autre ne lit de plan ; aucun n'est lecteur du dommage. L'agent de l'ancre reçoit la même invite que les lecteurs et passe par la même comparaison par programme.
