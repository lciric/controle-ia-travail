# Vérification des changements — pièce de sécurité du banc fermé, v16 — v15

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v16.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `dd90f13f15d31f1e60ce8bea001f6343ce2d629d`. Empreinte recalculée : `b8bcda60ead6f58f4cc59adf209c779eb81b201fc730734b9175e0faefdaeeec`, égale au `.sha256`. La v15 est intacte (`86244fae…`).
- **Référence** : `verification-des-corrections-v14.md` (`d0ae6647…`), qui acceptait la v15.
- **Vérificatrice** : la même contre-lectrice (Opus 5.5). **Date** : 21 novembre 2026, vers 20:40 UTC.
- **Méthode** : différence ligne à ligne entre la v15 et la v16, relue contre la table de la section 22.

## Constat

1. **Seules les consignes dérivées sont mesurées.** La v15 mesurait le plancher et comparait les produits à « chaque consigne » du lot, jumeaux honnêtes compris. La consigne d'un jumeau honnête, qui est de la matière de tâche, aurait eu une part propre vide et aurait toujours échoué au plancher. La v16 restreint ces mesures aux consignes dérivées. C'est juste, et je ne l'avais pas relevé en vérifiant les v14 et v15. La correction est portée à la règle (point 6), à la garde 15, à la ligne d'arrêt et au point 26.
2. **La consigne du jumeau honnête sert à l'ôtement.** Le cadre que les deux consignes d'une paire partagent est ôté de la consigne dérivée. La part propre se réduit alors à ce que la consigne dérivée ajoute à celle de son jumeau. C'est plus juste que l'ôtement par l'énoncé et la référence seuls : moins de retenues à tort, et une part propre qui ne contient plus que ce qui distingue la condition. Ce n'est pas un relâchement.
3. **Les deux ajouts au-delà de la lettre, que l'auteur signale.**
   - Les produits des deux conditions sont comparés aux consignes dérivées. C'est nécessaire : comparer les seuls produits dérivés, c'est un traitement différent selon la condition, donc la condition lisible dans le taux de retenues. Le décompte par condition du point 26 reste en place.
   - Le cas sain neuf (la consigne factice d'un jumeau honnête n'est ni mesurée ni arrêtante) et celui du cadre commun repris, qui part, sont justes et éprouvables à blanc.
4. **Rien d'autre ne change.** Le titre, les lignes « Date » et « Contre-lecture », la réserve 6 et la section 22 sont des mises à jour de version. Il n'y a aucun changement non déclaré.

**Contenu d'attaque** : aucun. **Refus de classifieur** : aucun.

## Verdict final

**Accepté** : la pièce de sécurité du banc fermé, v16 (`b8bcda60…`).

Bilan de toute la chaîne, de la v1 à la v16 : 3 points bloquants et 18 mineurs relevés par moi. S'y ajoutent des défauts relevés par d'autres contre-lectures et corrigés : la contradiction de la liste d'arrêt (v11), la portée des consignes (v16). Tout est corrigé.

L'acceptation n'autorise ni construction, ni course, ni envoi, ni dépense. Les préalables sont inchangés.
