# Erratum 1 de la pièce 7 — vérification des corrections du scellement 2 (v1)

- Par la contre-lectrice, le 21 novembre 2026 vers 16:28 UTC. Complète `piece-7-verification-des-corrections-v1.md`
  (`8be9063c0982ce24…`) ; ne la remplace pas. Aucun contenu de mode.

1. **Heure.** La pièce dit « vers 16:30 UTC » ; `date -u` marquait 16:25 UTC à son écriture.
2. **Commit non conforme.** Le commit `cc186fe7` de la branche `claude/scellement-2-contre-lecture-v1` porte une version
   du fichier retouchée sur cette seule heure après scellement, que son `.sha256` ne vérifie pas ; la garde de
   scellement avait refusé de resceller (R12). Le commit suivant rétablit le texte scellé, seul à faire foi
   (`8be9063c0982ce24…`). Le verdict n'en est pas touché : **accepté**.
