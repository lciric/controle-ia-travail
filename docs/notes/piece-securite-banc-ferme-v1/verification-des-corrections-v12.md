# Vérification des corrections — pièce de sécurité du banc fermé, v13 — v12

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v13.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `0873dd6747e1873b106acfe5477025a72dab6b51`. Empreinte recalculée : `dca22e3091ed784663ad2564f90923b25265935773b9ec8156dfa8074d526833`, égale au `.sha256`. La v12 est intacte (`399f530a…`).
- **Référence** : `verification-des-corrections-v11.md` (`746e3d73…`), point M13.
- **Vérificatrice** : la même contre-lectrice (Opus 5.5). **Date** : 21 novembre 2026, vers 20:05 UTC.
- **Méthode** : différence ligne à ligne entre la v12 et la v13, relue contre la table de la section 19.

## Constat

**M13 : corrigé.**
- **Correction (a)** : la garde 14, à l'envoi, ne lit plus la table de correspondance. Elle contrôle le gabarit, les paramètres, la complétude et l'ordre contre la liste scellée de la tâche du produit. L'égalité entre jumeaux découle de la construction.
- **Correction (b), ajoutée en complément** : le contrôle des paires se fait avant l'envoi, là où est le lot, et seule une attestation par empreinte passe à l'envoyeur.
- **Artefacts neufs de la garde 14** : la table présente chez l'envoyeur, une attestation absente ou d'empreinte inégale, et deux jumeaux portant des tâches différentes.
- **Points 25 et 27** : alignés. La table ne quitte pas le lieu où est le lot, ce qui rend la condition 2 cohérente.

**La question de l'auteur : l'envoyeur connaît la tâche de chaque produit.** Je l'accorde. La correspondance entre produit et tâche ne dit pas la condition, puisque les deux jumeaux partagent la tâche.

**Remarque, sans point** : elle dit en revanche quels produits forment une paire, à savoir les deux qui portent la même tâche. Quelqu'un qui lirait les deux produits d'une paire pourrait alors chercher lequel est le dérivé. Ce reste existait déjà en partie : les journaux d'un fournisseur reconnaissent les jeux de questions (section 3.5, « ce que cela laisse deviner »). Il n'est utile qu'à qui lit les produits. Une version ultérieure pourra ajouter que l'envoyeur ne lit pas les produits qu'il envoie, ou que, s'il les lit, cet accès est consigné au registre des accès. Ce n'est pas un défaut de la v13 : la correspondance est la seule information nécessaire, et la condition 2 la borne.

**Hors du point** : le titre, les lignes « Date » et « Contre-lecture », et la réserve 6. Il n'y a aucun changement non déclaré.

**Contenu d'attaque** : aucun. **Refus de classifieur** : aucun.

## Verdict final

**Accepté** : la pièce de sécurité du banc fermé, v13 (`dca22e30…`).

Bilan de toute la chaîne, de la v1 à la v13 : 3 points bloquants et 17 mineurs relevés par moi, plus une contradiction relevée par la contre-lectrice du préenregistrement ; tout est corrigé.

L'acceptation n'autorise ni construction, ni course, ni envoi, ni dépense. Les préalables sont inchangés.
