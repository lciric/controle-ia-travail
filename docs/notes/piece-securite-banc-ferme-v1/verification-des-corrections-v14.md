# Vérification des corrections — pièce de sécurité du banc fermé, v15 — v14

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v15.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `79754f412c81f589372ebe78cde1307b5cb620cc`. Empreinte recalculée : `86244fae606a173738b927b771b2267bec3d9e86dd28b99923e84248882abbdc`, égale au `.sha256`. La v14 est intacte (`64fd2662…`).
- **Référence** : `verification-des-corrections-v13.md` (`340ce5d4…`), point M14.
- **Vérificatrice** : la même contre-lectrice (Opus 5.5). **Date** : 21 novembre 2026, vers 20:25 UTC.
- **Méthode** : différence ligne à ligne entre la v14 et la v15.

## Constat

**M14 : corrigé.** Le plancher de la part propre est porté aux quatre endroits demandés.
1. **Point 6 de 3.5.** La longueur minimale est fixée au préenregistrement et mesurée par programme, là où est le lot, avant la course. Sous le plancher, c'est un nœud avant la course, et aucun produit de cette consigne ne part sans un mot de Lazar lisible au registre, qui dit que la garde ne le protège pas. Les consignes sous le plancher sont comptées et rapportées.
2. **Garde 15.** La mesure fait partie de sa définition. L'artefact neuf est une consigne factice sous le plancher : la garde arrête avant la course et refuse l'envoi de ses produits.
3. **Liste d'arrêt.** La ligne neuve couvre aussi le cas du plancher non fixé : aucun envoi.
4. **Point 26.** Plancher au préenregistrement, sans retouche ; décompte des consignes sous le plancher ; aucun de leurs produits parti sans mot de Lazar.

La réserve 22 dit maintenant que le plancher est une règle et que sa valeur reste à fixer. C'est exact : la valeur appartient au préenregistrement, et non à cette pièce.

**Hors du point** : le titre, les lignes « Date » et « Contre-lecture », et la réserve 6. Il n'y a aucun changement non déclaré.

**Contenu d'attaque** : aucun. **Refus de classifieur** : aucun.

## Verdict final

**Accepté** : la pièce de sécurité du banc fermé, v15 (`86244fae…`).

Bilan de toute la chaîne, de la v1 à la v15 : 3 points bloquants et 18 mineurs relevés par moi, plus une contradiction relevée par la contre-lectrice du préenregistrement ; tout est corrigé.

L'acceptation n'autorise ni construction, ni course, ni envoi, ni dépense. Les préalables sont ceux des vérifications précédentes. S'y ajoute la valeur du plancher de la part propre, à fixer au préenregistrement.
