# Vérification des changements — pièce de sécurité du banc fermé, v14 — v13

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v14.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `690b93d51cc58f0fd24c3ce6ad7141e233be7fa2`. Empreinte recalculée : `64fd2662b2f7b9ba4f671cabd15eb7e98b1ba8b23231952ced9d551c14c31843`, égale au `.sha256`. La v13 est intacte (`dca22e30…`).
- **Référence** : `verification-des-corrections-v12.md` (`74ec125b…`), qui acceptait la v13.
- **Vérificatrice** : la même contre-lectrice (Opus 5.5). **Date** : 21 novembre 2026, vers 20:15 UTC.
- **Méthode** : différence ligne à ligne entre la v13 et la v14, relue contre la table de la section 20.

## Constat

- **Le blocage est réel, et sa levée est juste.** Un jeu de questions exhaustif et une garde de fuite qui lit les questions se bloquaient dès qu'une consigne nommait un contrôle. La v14 ne retient ni l'une ni l'autre des deux issues faciles, retirer la question ou relâcher le seuil, et la pièce dit pourquoi chacune est mauvaise.
- **Questions gardées par leur provenance (points 2 et 5).** Chaque paramètre est identique, au caractère près, à une entrée de la référence. Un programme vérifie l'identité, la complétude et l'ordre là où se trouve la référence, et la garde 14 exige l'attestation. Je partage l'avis de l'auteur (son point 1) : c'est plus strict qu'un seuil de ressemblance. Une question ne peut contenir aucun mot qui ne soit pas dans la référence, et la garde 14 a les artefacts qu'il faut (un écart d'un caractère, le mot témoin, une entrée manquante, une attestation absente).
- **La réserve 20 change de sens** (point 4 de l'auteur) : elle est exacte. L'exhaustivité se vérifie désormais par programme.
- **Produits comparés à la part propre (point 6, garde 15).** La restriction est dite telle (réserve 22, point 2 de l'auteur). Elle est justifiée : ce que la consigne partage avec la tâche sort déjà par les questions. Le cas sain neuf (un produit honnête qui cite un contrôle que la consigne nomme aussi part) et l'artefact sur la part propre sont justes. La règle d'ôtement et le seuil sont fixés avant la course, sans retouche après un produit retenu. Les retenues sont décomptées par condition (point 26). C'est bien.
- **Taux de retenues à tort** (réserve 23, point 3 de l'auteur) : c'est une mesure de la répétition, rapportée, et qui ne règle pas le seuil. C'est conforme à R4 et à l'esprit de R1.
- **Condition 2** : ma remarque sur la v13 est prise. L'envoyeur n'ouvre pas les produits ; toute ouverture est un accès consigné et un nœud. Le point 27 est aligné.
- **Contenu d'attaque** : aucun. **Refus de classifieur** : aucun.

## Point

**M14 — mineur — Le plancher de la part propre n'existe que dans une réserve.** La réserve 22 exige qu'un plancher de longueur de la part propre soit fixé au préenregistrement, et dit qu'en dessous c'est un nœud avant la course. Mais cette règle n'est ni dans la règle des questions (point 6 de 3.5), ni dans la garde 15, ni dans la liste d'arrêt, ni dans la liste du vérificateur. Une réserve dit une limite ; elle ne s'applique pas et ne se vérifie pas. Telle quelle, une consigne dont la part propre est presque vide passerait la garde 15 sans rien retenir, sans qu'aucune ligne n'arrête.

**Correction demandée.**
- Au point 6 de 3.5 : « un plancher de longueur de la part propre est fixé au préenregistrement ; une consigne dont la part propre est sous ce plancher fait un nœud avant la course, et ses épisodes ne partent pas sans le mot de Lazar ».
- À la garde 15, un artefact : une consigne factice dont la part propre est sous le plancher, qui doit arrêter.
- À la liste d'arrêt, une ligne : part propre d'une consigne sous le plancher, donc aucun envoi des produits de cette consigne ; nœud.
- Au point 26, ajouter : plancher fixé, et décompte des consignes sous le plancher.

## Verdict

**À corriger** : un point mineur (M14), aucun bloquant. Le fond de la v14 est accepté. Une v15 qui ne corrige que M14 sera vérifiée sur sa seule différence (`verification-des-corrections-v14.md`).
