# Saboteur à budget → mère — versement, coupure et rythme de l'étalonnage, d'après le code à 43d6d067 seulement

Lecture du code par l'Opus contre-lecteur du code (`brouillons/ii-b-saboteur-budget-v5/code-v5/contre-lecture-cl1/note-lecture-code-versement-coupure-rythme-v1.md`, 13f494d5704876c5…), sans aucune sortie lue.

1. **Aucune poussée par lot.** Chaque lot est scellé sur le disque de la machine seulement (`lanceur_v5.phase_etalonnage`, `verser`). L'amorce ne pousse qu'à des points de passage : au départ, à la fin normale, sur une sortie en erreur du lanceur, par la minuterie à 55 USD ou à l'échéance, et à un second démarrage. **« Versé et poussé par lot » dans l'ordre (§§ 3 et 7) est faux pour la poussée** : erreur de rédaction de l'ordre, que ni l'Opus ni moi n'avions relevée.
2. **Coupure à 12 USD.** Les lots restent sur le disque de la machine arrêtée ; rien n'est poussé. Pour les récupérer, il faut redémarrer la machine : chemin « run interrompu » de l'amorce, qui pousse runs, diag et identifiants puis demande la destruction. **Il faut ton mot.**
3. **Un étalonnage coupé n'est pas exploitable.** Le fichier des sorties d'oracle n'est écrit qu'à la fin. Les conditions de départ s'arrêtent alors sur une garde, sans issue scellée ; sur le fond, ce serait « non calculable » (texte 10.3, étape 1). Les flagrants viennent en dernier.
4. **Le rythme ne signe aucun réglage faux.** Modèle en bfloat16 sur la carte, lot de 8, 400 et 16 jetons, cache dupliqué : comme à la première course ; les correctifs 0011 et 0012 n'y touchent pas. L'observé est 5 à 7 fois plus long que le devis, à peu près uniformément (environ 3,75 s par action d'oracle contre 0,511). Cause compatible : l'échantillonnage se fait jeton par jeton sur le processeur de l'hôte, sur environ 128 000 jetons ; **c'est l'hôte qui est lent**, pas le code.
5. **Défaut à part, sans effet sur le rythme** : un repli silencieux du cache dupliqué ne serait pas consigné (la v5 n'écrit jamais `modele.replis`). À corriger avant la course.
6. **Ce qui en découle.**
   - Si la coupure à 12 USD tombe avant la fin, on dépense environ 12 USD pour rien d'exploitable.
   - Arrêter maintenant pour corriger le code ne sert à rien : le code n'est pas en faute. La seule correction serait un hôte plus rapide, donc une nouvelle location et un nouveau chargement.
7. **Options.**
   - (a) **Relever la coupure propre de l'étalonnage de 12 à 16 USD**, sous le plafond de 17 USD de l'étape 1 au devis scellé et sous la ligne GO-2026-11-21-70. Cela laisse finir l'étalonnage à 10 à 12 h de projection. **C'est un changement d'un seuil accordé : mot de Lazar requis.**
   - (b) Laisser courir telle quelle : l'étalonnage finit seulement si la projection basse tient ; sinon environ 12 USD perdus.
   - (c) Arrêter maintenant par l'identifiant et relouer un hôte plus rapide : recharge, délai, et la dépense déjà faite est perdue.
8. **Ma recommandation : (a)**, confiance moyenne. Le résultat est exploitable seulement si l'étalonnage finit, et la dépense reste sous le plafond du devis.
9. **Avant la course**, à corriger : la poussée par lot (code ou ordre) et le repli du cache consigné.
