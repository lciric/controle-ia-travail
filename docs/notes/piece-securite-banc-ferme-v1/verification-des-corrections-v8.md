# Vérification des corrections — pièce de sécurité du banc fermé, v9 — v8

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v9.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `6765b3a3405717d96126dbb6de18bb55b70e8e1c`. Empreinte recalculée : `3eb3b85f23401347ec63f97de2af058e0292499e9fff89bddf7837b5aa241546`, égale au `.sha256`. Les v1 à v8 sont intactes, toutes recalculées.
- **Référence** : `verification-des-corrections-v7.md` (`98b3fa64…`) et son erratum 1 (`f18dc52e…`).
- **Vérificatrice** : la même contre-lectrice (Opus 5.5). **Date** : 21 novembre 2026, vers 19:25 UTC.
- **Méthode** : différence ligne à ligne entre la v8 et la v9, relue contre la table de la section 15.
- **Source contrôlée** : `registres/go.md` sur `main` au commit `c40eee73`. Empreinte recalculée `19da46e1…`, égale à celle que cite la pièce. La ligne 675 (GO-2026-11-21-76), déjà lue, porte bien « ses six conditions » et cite la note au commit `f011f9fff`.

## Points

| Point | Vérifié | Constat |
|---|---|---|
| B3, lecture humaine chez le fournisseur | **corrigé** | Le champ n° 18 a une rubrique neuve : oui, non ou non établi, avec le texte du fournisseur cité par adresse, date et empreinte, et le régime sans conservation ni revue, en vigueur ou non sur le compte employé. La règle de 3.5 dit : « oui » ou « non établi » fait tomber le trait pour ce lecteur. Il n'y a alors que deux issues : ce lecteur ne lit pas, ou Lazar dit en toutes lettres, sans défaut, que l'envoi est un partage, et rien ne part avant ce mot au registre. La garde 16 est éprouvée sur trois artefacts (rubrique vide, « non établi », « oui » sans mot). Le point 24, une ligne d'arrêt, le trait 3 de 6.4 et la réserve 13 sont mis à jour. Le trait est maintenant établi lecteur par lecteur, et gardé. |
| M8, questions fermées | **corrigé** | Les questions viennent d'une liste fermée scellée avant la course. Elles sont identiques pour tous les produits, ne dépendent ni de la condition ni du produit, et ne citent ni consigne ni mode. Leur empreinte est contrôlée à chaque appel par la garde 14 ; l'artefact est une question propre à une condition ou absente de la liste. Le point 25 est mis à jour. |
| M9, calendrier en deux temps | **corrigé** | Deux lignes d'arrêt : points 24, 25, 27 et 28 avant le premier envoi ; 26, 29 et 30 avant la levée de l'embargo. Elles sont cohérentes avec la fin de 6.1 et avec l'ordre des gestes. |
| M10, comptes anciens | **corrigé** | La section 6.3, point 1, dit « treize à la date de ce mot, dix-sept depuis la v8, toutes exigées ». La réserve 11 dit dix-sept, et la confirmation est renvoyée à la mère. |
| M11, contrôle avant envoi | **corrigé** | L'option est écartée, pour trois raisons écrites : l'ordre des deux temps du juge, le biais de tri entre conditions et un lecteur de plus. La pièce dit aussi ce qu'il faudrait si Lazar la voulait : un nœud, un lecteur neuf aveugle à la condition et un biais déclaré. Le raisonnement est juste. La remarque que la garde 15 a le même défaut en plus petit, et que ses retenues se comptent donc par condition, est un bon ajout. |
| M12, registre | **corrigé** | GO-2026-11-21-76 est cité dans l'en-tête, les sources, la liste d'arrêt, l'ordre des gestes et la réserve 12. |

## Les deux ajouts que l'auteur signale

1. **Réserve 13.** Elle me rend le constat sur la revue humaine, comme plausible et non vérifié par l'auteur. C'est exact : c'est un constat général de ma part sur des conditions d'usage courantes, je n'ai lu le texte d'aucun fournisseur précis. La conséquence qu'elle en tire est juste et utile à Lazar : le nœud ou le repli vers les deux juges pourrait être le cas ordinaire.
2. **Réserve 12.** L'écart entre les « six conditions » du registre et les neuf conditions de la pièce, plus la règle de lecture humaine, est exact. Les trois conditions de plus, et la règle, sont plus strictes ; elles ne relâchent rien.

**Hors des six points** : le titre, les lignes « Date » et « Contre-lecture », et la réserve 6. Il n'y a aucun changement non déclaré.

**Contenu d'attaque** : aucun. **Refus de classifieur** : aucun.

## Verdict final

**Accepté** : la pièce de sécurité du banc fermé, v9 (`3eb3b85f…`).

Bilan de toute la chaîne, de la v1 à la v9 : 3 points bloquants et 16 mineurs, tous corrigés.

L'acceptation porte sur le dossier, voie d'envoi comprise. Elle n'autorise ni construction, ni course, ni envoi, ni dépense. Pour la voie d'envoi, restent :
- le champ n° 18 scellé, avec la rubrique « lecture humaine » établie pour chaque lecteur, et le nœud à Lazar là où elle ne dit pas « non » ;
- la liste des questions fermées, scellée ;
- le code de l'envoi, contre-lu ;
- les épreuves des gardes 14 à 17 ;
- l'appel anodin par lecteur, sur devis et GO ;
- les deux temps de la pièce du vérificateur ;
- la confirmation par la mère des dix-sept gardes pour GO-2026-11-21-71.
