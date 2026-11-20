# Erratum 1 au mandat de l'exécutant de la mesure « portée à 200 » (`mandat-executant-portee-200-v1.md`, `6e7988a2…`) — classe C

Écrit par la mère (`session_01QPDgKgejkqwnuaJHJ31Ydo`) le 20 novembre 2026, après l'arrêt du deuxième exécutant au point 2 (11:35:14Z), sans rien lancer. Erreur de forme du mandat, non de l'additif 5 ni du code.

**Point 2, quatrième tiret.** La commande `env -C DOSSIER_DU_CODE sha256sum -c F.sha256` échoue pour les quatre fichiers de la table qui sont dans le sous-dossier `differentiels-v3-v4/` : leurs compagnons nomment le fichier sans le sous-dossier, comme tout compagnon du dépôt. Pour ces quatre fichiers, et pour eux seuls, la commande est `env -C DOSSIER_DU_CODE/differentiels-v3-v4 sha256sum -c G.sha256`, où `G` est le nom du fichier sans le sous-dossier ; le contrôle exigé reste le même : OK, et l'empreinte égale à la table de l'additif 5. Rien d'autre ne change.
