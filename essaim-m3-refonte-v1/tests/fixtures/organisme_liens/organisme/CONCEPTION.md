# Organisme d'essai « poseur de liens » (R-372)

Écrit par « session-depot » pour éprouver la garde du noyau contre les liens symboliques et les tubes nommés : à chaque
génération, il pose `lien-environ` (vers `/proc/self/environ`), `lien-cmdline` (vers `/proc/self/cmdline`), `lien-cible`
et `metrique_proposee.json` (vers le fichier JSON nommé dans `cible.txt`, que l'essai rend illisible pour lui), un
tube nommé `reponses_test.json`, puis relit sa vue et consigne ce qu'il y trouve dans `vu.json`. Simulation seulement.
