# Vérification des changements — pièce de sécurité du banc fermé, v6 — v5

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v6.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `f1ada61b4637d8cb50aeb4c403d837048f08e08b`. Empreinte recalculée : `f3bb30525f0a79bbe3c9b80f8e61662325f278478eb3bb1e2ed89592a11404db`, égale au `.sha256`. Les v1 à v5 sont intactes, toutes recalculées.
- **Référence** : `verification-des-corrections-v4.md` (`67f3ea5e…`), qui acceptait la v5.
- **Vérificatrice** : la même contre-lectrice (Opus 5.5). **Date** : 21 novembre 2026, vers 19:05 UTC.
- **Méthode** : différence ligne à ligne entre la v5 et la v6, relue contre la table de la section 12.

## Sources neuves contrôlées

- **[GO71]** : `registres/go.md` au commit `ece586d2`. Empreinte du fichier recalculée : `bfedf019…`, égale. Seule la ligne 670 (GO-2026-11-21-71) a été lue. Le mot verbatim (« Option 2 : … (GO-2026-11-20-50). go »), la lecture « écart déclaré à R-611 et à N-057 point 4 » et la condition (contre-lecture de la pièce `a4d515fc…`, corrections vérifiées, « douze gardes » éprouvées à blanc sur un cas sain et un artefact) sont tous fidèlement repris.
- **[ML2]** : `registres/passations/2026-11-21-1800-attaquant-informe-mot-lazar-verificateur-opus-neuf.md`, commit `d239b5a8`. Empreinte recalculée `8da822e4…`, égale à son compagnon. Comme c'est une passation, je n'en ai extrait que les lignes du titre, du mot verbatim (l. 4), du vérificateur (l. 8), de la proposition et de sa confiance (l. 9 à 11) et de la réserve (l. 13). Le mot verbatim, la proposition (opérateur Opus 5.5 neuf, juge Fable 5.2 neuf, second juge Opus 5.5 neuf), la confiance 0,6 et la réserve de lignée sont fidèlement repris et attribués à la note, non à Lazar.

## Les cinq points que l'auteur signale

1. **Cumul des trois mots** (six garde-fous, gardes de la pièce, vérificateur Opus 5.5 neuf) : juste. [GO71] et [ML] ne se contredisent pas. Le sixième garde-fou de GO-2026-11-20-50 exige déjà une revue externe avant toute sortie hors quarantaine, ce qui rejoint « mise de côté jusqu'à publication ».
2. **« Douze gardes » contre treize** : la lecture de l'auteur, une condition qui porte sur la pièce corrigée, est la seule cohérente avec « ses corrections vérifiées » dans [GO71]. L'exigence des treize est plus stricte et ne relâche rien. Le renvoi à la mère pour confirmation (réserve 11) est bien posé.
3. **Tension de lignée** : bien posée, sans trancher. La pièce ne lit aucun moniteur et dit ce qui prime si l'écart existe, à savoir le mot de Lazar ; l'écart sera alors déclaré. La question fermée du risque 11 reste posée à un lecteur d'une autre lignée. C'est juste : c'est un autre rôle, celui du cinquième garde-fou.
4. **Liste d'arrêt** : la ligne remplacée est devenue sans objet, puisque le mot est au registre. Les deux lignes neuves sont exactes. La seconde (aucune construction des gardes avant le préenregistrement scellé) est plus stricte que [GO71] et cohérente avec l'ordre des gestes de 6.3.
5. **Opérateur et juge** : rapportés comme la proposition de la note, avec sa confiance, et non comme un mot de Lazar. C'est conforme.

## Autres changements

- **En-tête, ligne 6** : les trois mots sont exacts et cités par leurs sources. « La construction des gardes n'attend plus que le préenregistrement de la course » est cohérent avec la liste d'arrêt et 6.3.
- **Lignes 8 et 9** : l'empreinte de ma pièce `67f3ea5e…` et le commit `16576575` sont exacts.
- **Réserves 8 et 9** : réécrites conformément au registre.
- **Section 12** : elle décrit fidèlement la différence. Aucun changement non déclaré.

**Contenu d'attaque** : aucun. **Refus de classifieur** : aucun.

## Verdict final

**Accepté** : la pièce de sécurité du banc fermé, v6 (`f3bb3052…`). Aucun point bloquant ni mineur sur les changements de la v6.

Bilan de toute la chaîne, de la v1 à la v6 : 2 points bloquants et 11 mineurs, tous corrigés.

Cette acceptation vaut, pour la condition de [GO71], « contre-lecture de la pièce, corrections vérifiées ». Elle n'autorise ni construction, ni course, ni dépense. Restent :
- le préenregistrement de la course ;
- le code des gardes, contre-lu ;
- les treize épreuves à blanc ;
- le devis et le GO de la répétition ;
- la pièce du vérificateur Opus 5.5 neuf ;
- le GO de la course ;
- deux confirmations de la mère : lignée des moniteurs (réserve 10), lecture « treize gardes » (réserve 11).
