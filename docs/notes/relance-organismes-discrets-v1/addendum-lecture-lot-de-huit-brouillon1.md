# Addendum de lecture au préenregistrement des organismes discrets, bras A — « lot de 8 » — BROUILLON 1, non scellé au registre

- **Texte visé** : `prereg/T0.7-organismes-discrets-v-a-v1.md`, `06ab6a2f6e173bb1258f45ffeded7a419b05ecc2f59920666cea91aafcc7cf05` (inchangé, R12).
- **Date (UTC)** : 2026-11-18T17:52:08Z. **Rédaction** : session de relance (`session_013QMaymFtcZwVwjxVAF3gmH`), autrice du code de fabrication ; à contre-lire par un agent neuf (R2) avant inscription par la session mère.
- **Pièce d'appui** : note de lecture déclarée d'un lecteur neuf, `docs/notes/relance-organismes-discrets-v1/lecture-declaree-lot-de-huit-v1.md`, `6bbda68f9db01750853d3f2a31c177776d2d1c6885da3625ca82f6ffec3aceee`.
- **Décision** : mot direct de Lazar dans la session de relance, le 18 novembre 2026, verbatim « lecture A, et option 1 pour les fiches », en réponse aux trois lectures A, B, C exposées par la note.
- **Moment** : avant toute génération, toute fabrication sur données réelles, toute distillation et toute lecture de résultat du bras A. Aucune course du bras A n'a eu lieu ; seul du code sur processeur et des essais sur données d'essai existent.

## 1. Ce que dit la lettre, et ce qui est retenu

Lignes 39 et 164 du texte scellé : « lot de 8 candidats », graines « dérivées par (tâche, épisode, pas, candidat) », « une seule passe de tirage de candidats : 16 tâches × 8 épisodes × 10 pas × 8 candidats ».

**Lecture retenue (A)** : le « lot de 8 » est celui de la configuration de référence citée par le texte (`prereg/T0.6-organismes-config-7b-v1.json`, `b7a5c1ba…`) et de la conception v2 qui fait foi (section 1.1) : **huit épisodes joués en parallèle, une action générée par épisode et par pas, aucun tirage multiple, aucun choix entre des actions**. Les graines d'action sont dérivées par (tâche, épisode, pas).

## 2. Écart à la lettre, déclaré

Trois éléments écrits du texte scellé restent **sans exécution** : le mot « candidats » (lignes 39 et 164), le facteur « × 8 candidats » (ligne 164), l'indice « candidat » de la dérivation des graines (lignes 39 et 164). Ils viennent de la première conception (choix parmi plusieurs actions tirées), que la conception v2 a retirée du protocole principal (section 1.3 de la conception ; ligne 44 du texte scellé).

## 3. Ce qui ne change pas

- Tailles et puissance : 16 tâches de vérification × 8 épisodes par tâche et par condition = 128 épisodes, 1 280 actions par condition, 16 moyennes de tâche (section 6.1) — ces nombres ne comptaient pas de candidats.
- Appariement au jumeau honnête : mêmes graines d'action pour une même tâche d'une condition à l'autre.
- Grille des doses, témoins, ordre d'exécution, contrôles de manipulation, métriques, seuils, critères de lecture, liste d'arrêt : inchangés.
- Le repli de deuxième ligne par tirages honnêtes multiples (section 9.2) reste un repli déclaré : ses tirages ne sont **pas** faits pendant la course principale ; il demanderait sa propre passe de génération et son propre avenant.

## 4. Deux autres lectures fixées par le même addendum (relevées par le lecteur neuf)

- **Épisodes par tâche** : le texte scellé dit 8 épisodes par tâche (section 6.1, et section 1.1 de la conception) ; la configuration de référence porte 5 épisodes par tâche pour la distillation de l'organisme précédent. **Le texte scellé prime : 8.** La configuration de référence ne vaut que pour les réglages que le texte lui emprunte expressément (lot, jetons, température, adaptateur, distillation).
- **Renvoi** : la ligne 44 renvoie à une « section 5.2 » qui n'existe pas ; le repli visé est la **section 9.2**.

## 5. Conséquences pour l'exécution

- Plan de génération du bras A : une action par (tâche, épisode, pas) ; multiplicateur 1 par rapport à la conception v2.
- Devis : le devis `docs/notes/organismes-discrets-v1/devis-organismes-discrets-v1.md` chiffre la première conception ; **un devis neuf, accordé à la conception v2 et à cette lecture, est à écrire et à contre-lire avant toute ligne de calcul**.

## 6. Ce que cet addendum ne fait pas

Il ne modifie aucune hypothèse, aucune prédiction, aucun seuil, aucun critère de lecture. Il n'ouvre aucune dépense.
