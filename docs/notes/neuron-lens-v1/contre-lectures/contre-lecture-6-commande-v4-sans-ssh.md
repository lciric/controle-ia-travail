# Contre-lecture 6 de la commande v4 sans ssh (amorce v1, dépôt réduit v5, essai à blanc v1) — rapport (résumé fidèle)

Contre-lecteur : sous-agent neuf, « modèle D », lancé après le commit 1d5b75a8, rapport lu avant 13:04 UTC ; lecture seule (`bash -n`,
`diff`, `sha256sum`). Compagnons conformes ; dépôt réduit v5 limité à trois changements (amorce scellée, mode 755, en-tête).

**Verdicts** : commande v4 après corrections (1, 2, 3) ; amorce v1 après corrections (4, 5, 6) ; dépôt réduit v5 **scellable en
l'état** ; journal de l'essai à blanc après correction mineure (11).

**Remarques**
1. Bloquante — `vastai show instance(s) --raw` restitue la configuration de l'instance (variables d'environnement, jeton compris) :
   interdire les sorties brutes, filtrer les champs, balayer chaque sortie.
2. Bloquante à vérifier — sérialisation de `--entrypoint bash --args -c '…'` par l'outil non éprouvée : lire la source de l'outil ou
   ne pas dépendre des guillemets.
3. Moyenne — version CUDA de la roue par défaut de `torch` 2.14.1 peut dépasser le filtre `cuda_max_good>=12.8`.
4. Moyenne — échec de poussée jamais fatal et cause masquée : première poussée fatale (code 14, avant la carte graphique), cause
   affichée, branche des résultats exigée absente.
5. Moyenne — poussée finale de 4 essais en 30 s : la rendre persistante.
6. Mineure — jeton dans l'environnement de `pip` et `pytest` ; `tail -30` des essais en échec.
7. Info — jeton à droit d'écriture sur tout le dépôt, `main` compris : préférer un jeton restreint s'il existe (à signaler).
8. Info — bornes du feu respectées. 9. Info — arbre propre au manifeste : conforme. 10. Info — conteneur sorti facturé en stockage
   (détecter « exited ») ; fichiers de plus de 100 Mo refusés par l'hébergeur.
11. Mineure — le journal de l'essai à blanc ne contient pas le balayage du jeton ni les artefacts : les joindre.
Signal : listes d'essais du dépôt réduit et de l'amorce différentes, sans conséquence.

**Suites données** : 1 → `suivi_vast_v1.py` (champs filtrés, balayage, essais) et commande v5 ; 2 → source de l'outil 1.11.0 lue :
`--args` est une liste (`argparse.REMAINDER`) transmise telle quelle dans la charge (`json_blob["args"]`) ; 3 → métadonnées
publiques de PyPI : la roue dépend de `nvidia-nccl-cu13`, filtre porté à `cuda_max_good>=13.0` ; 4, 5, 6, 10 → amorce v2 ; 7 →
signalé à la mère ; 11 → essai à blanc v2, journal complet.
