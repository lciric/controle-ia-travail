# Note de vérification courte — correctif 0010 (coupure propre de l'étalonnage à 12 USD) — cl1

Date : 2026-11-21. Classe B. Même contre-lecteur (Claude Opus 5.5), même mandat (`47b53672…`). Correctif `correctifs-v5/0010-….patch` (compagnon vérifié) appliqué après le 0009 dans `arbre-final`. **Même arborescence que celle annoncée : `ed9b0e48be36…`.** Rien poussé, aucune dépense, aucune machine, aucun refus d'outil.

**Verdict : étalonnage autorisable.** La règle fait ce que disent la ligne (GO-2026-11-21-70) et le devis scellé. Deux mineurs, que l'ordre peut déclarer ou que le code peut corriger d'une ligne : l'origine du compte (point 1) et la phrase du motif (point 2).

- **Ce qu'elle fait** :
  - la sous-commande `session_v5 coupure-etalonnage` est jouée à chaque relevé de la surveillance de `lancer_iib_v3.sh`, après la garde de la ligne (55), qui prime, et seulement hors ARRET, FIN ou REFUS ;
  - pendant l'étalonnage, à 12 USD de dépense comptée : alerte, motif écrit et copié daté, puis la commande **`stop instance <identifiant>`** imprimée (R10, jamais par motif) et le code 3 ;
  - hors étalonnage elle ne joue pas, une phase illisible arrête, et la fin du run prime.
- **Ce qu'elle ne touche pas** : l'amorce et sa minuterie (aucune ligne changée), la liste figée (`342ee21d…`). Douze lignes sont ajoutées au lanceur de session, sans aucune retirée.
- **Essais** : les quatre essais (cas sain, artefact, autre phase avec phase illisible, règle seule) font partie de la liste figée. **J'ai rejoué la répétition locale à liste figée** (`sorties/sortie-repetition-locale-liste-figee-cl-v2.txt`) : code 0, **271 essais réussis en 7 min dans l'amorce**. La surveillance y écrit « phase etalonnage » et finit par « FIN » ; destruction par identifiant, machine de l'autre chantier non touchée, désignation P à 12 tours.
- **Point 3 de la note du développeur** : c'est conforme au devis (« la surveillance alerte, l'exécutante arrête la machine par son identifiant, et c'est un nœud ») et à la coupure à 55 déjà revue. Il ne faut rien de plus dans le code. L'ordre doit dire que la session surveille sans interruption pendant l'étalonnage et qu'elle exécute l'arrêt dès le code 3. Sinon, c'est la minuterie de l'amorce, à 55, qui coupe.

## Les deux points du rédacteur de l'ordre (brouillon 3, § 12 point 8)

1. **Dépassement au moment de la coupure.** La règle compte depuis le début de l'amorce, au prix réel lu. La dépense réelle la dépasse :
   - du temps entre la création et le début de l'amorce, soit environ 0,1 USD pour 5 minutes à 1,38 (calcul : 12,01 comptés pour 12,12 depuis la création) ;
   - d'au plus un intervalle de surveillance (60 s, soit 0,02 USD) ;
   - du temps de réaction de la session, environ 0,23 USD par 10 minutes.

   Le forfait de téléchargement n'est pas encouru avant le rapatriement ; il est dans les 0,92 de consignation du devis. Le dépassement reste donc **de l'ordre de 0,1 à 0,4 USD**, sous les 16,76 USD que tiennent les gardes. Recommandation : **correction d'une ligne**, compter toujours depuis la création (`debut = cree`), ce qui est la lecture littérale de « dépense relevée » et supprime une lecture à déclarer. À défaut, l'ordre la déclare.
2. **Après la coupure : arrêt, rapatriement, nœud, pas de destruction automatique.** Le code le permet tel quel :
   - la surveillance n'imprime qu'un **arrêt** (`stop`), jamais une destruction ;
   - la destruction ne se fait que par la sous-commande `destruction`, appelée à la main, avec `RAPATRIEMENT_VERIFIE=oui` et ses gardes ;
   - une machine arrêtée ne fait pas tourner la minuterie de l'amorce.

   **Mineur** : la phrase du motif (« … puis la détruire par la sous-commande « destruction » ») prescrit une destruction que le devis renvoie au nœud. *Correction* : « arrêter l'instance par son identifiant (R10), rapatrier ; nœud : aucune destruction sans le mot de Lazar ». À défaut, l'ordre dit qu'elle ne s'applique pas.
