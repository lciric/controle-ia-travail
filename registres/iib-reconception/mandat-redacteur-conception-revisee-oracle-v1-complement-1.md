# Complément 1 au mandat du rédacteur de la conception révisée de l'oracle — sans aucune valeur mesurée

Écrit le 2026-11-19 par la session de reconception. Transmis tel quel au rédacteur en cours de travail.

La lecture du code des deux lecteurs du coût, faite à part, a rendu ceci. Le résumé à lire devient `registres/iib-reconception/resume-sans-chiffre-resultat-negatif-centrage-oracle-saboteur-budget-v2.md` (tu peux le lire ; rien d'autre de neuf dans `registres/`).

1. **Un défaut de code, un seul, limité.** Pour toute valeur écrite sur la ligne de la clé du coût, les deux lecteurs rendent le même nombre. Mais une valeur écrite à la ligne qui suit la clé est lue dans l'action de l'agent (le champ court jusqu'à la clé suivante), alors qu'une suite du jumeau écrite de la même façon est coupée au premier saut de ligne et devient illisible. Il touche peu d'actions, mais il pèse sur le verdict du centrage sans suffire à l'expliquer. La conception révisée doit fixer **une même règle de forme pour les deux lectures** (deux voies à examiner : lire la suite comme le champ de l'action, ou déclarer non bornable, et compter, toute action dont la valeur n'est pas sur la ligne de la clé), dire laquelle et pourquoi, et prévoir l'essai d'égalité forme par forme, valeur à la ligne suivante comprise, ainsi qu'un nombre placé au-delà de la limite de jetons d'une suite.
2. **La réécriture du contexte ne garde que le texte du premier nombre** de la suite retenue : unité, multiplicateur (« 4 GPUs for 100 hours » devient « 4 »), suffixe collé à une unité disparaissent, et l'échelle vue par le jumeau aux pas suivants peut changer. La conception révisée doit dire ce qu'elle en fait (réécrire par la valeur entière de la suite retenue, par exemple) et l'éprouver.
3. **Conserver la forme des suites** dans les sorties de l'oracle (sans leur texte si le cloisonnement l'exige : au moins des indicateurs de forme par suite), pour que ces points soient mesurables à la prochaine course.

Ces trois points entrent dans ta conception, ta simulation (formes illisibles asymétriques comme défaut nommé de l'épreuve) et ta liste d'écarts à la v1.
