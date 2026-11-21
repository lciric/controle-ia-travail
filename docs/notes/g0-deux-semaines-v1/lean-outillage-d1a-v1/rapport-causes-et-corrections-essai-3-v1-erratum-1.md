# Essai Lean D-1a, troisième essai : erratum 1 du rapport des causes et des corrections

- **Pièce corrigée** : `rapport-causes-et-corrections-essai-3-v1.md` (`887cf4c949e289a9d108b2e9b99bdba75fc6228c51dcfc5bba7ba627c8e9f9d9`),
  § 7, l. 186 et 187. Le rapport reste versé tel quel (R12) ; cet erratum prime sur ces deux phrases.
- **Source** : contre-lecture Fable 5.2, `contre-lecture-corrections-essai-3-v1.md` (`59b0ec03…`), § 3.4 et recommandation R3.
- **Qui** : le développeur du rapport, Claude Opus 5.5, le 21 novembre 2026.

## 1. Le relevé échantillonné, minorant (l. 186)

**Écrit** : « Le pic échantillonné est un minorant : un pic bref entre deux relevés (0,1 s) peut manquer. »

**À lire** : « Le pic échantillonné est un minorant. `memory.peak` est un plus-haut que le noyau tient pour le cgroupe : un pic
bref entre deux relevés n'est pas perdu, le relevé suivant le porte. Seul est perdu ce qui monte après le dernier relevé,
c'est-à-dire pendant au plus une période (0,1 s) avant la fin de l'unité. »

La l. 141 du rapport le disait déjà juste (« `memory.peak` ne décroît pas ; ce qui monte après le dernier relevé est perdu ») ;
la l. 186 la contredisait.

## 2. La somme des trois pics (l. 187)

**Écrit** : « Pour la mémoire à trois processus en parallèle (`mesurer`), chaque unité a son pic ; leur somme majore le pic
simultané des trois sans le mesurer. »

**À lire** : « Pour la mémoire à trois processus en parallèle (`mesurer`), chaque unité a son pic relevé. La somme de trois pics
exacts majorerait le pic simultané ; la somme de trois minorants ne majore rien, et ne dit donc pas la mémoire de la machine
entière. »

Suite donnée : l'épreuve v8 mesure cette mémoire à part, dans une tranche réservée qui porte les trois passages : `memory.peak`
de la tranche, recoupé par `MemAvailable` de `/proc/meminfo`, avec des critères écrits d'avance (procédure du poste local v12,
section 8). Sans cette mesure conforme, aucun passage en parallèle n'est compté.
