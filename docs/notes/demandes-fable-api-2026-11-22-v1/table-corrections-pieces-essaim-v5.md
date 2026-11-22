# Table des corrections 44 à 58 (pièces de la comparaison essaim contre isolé, version 5)

22 novembre 2026, Opus 5.5 (règle GO-2026-11-21-84 : corrections portées mot pour mot, rien d'inventé). Remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/relecture-pieces-essaim-v4/relecture-fable-api.md` (sha256 c1cebee3a8abec9cc142c458a6eb05800f2095fcef576fc99c0a93a974c7b4d7). Base : `pieces-comparaison-essaim-v4.md` (sha256 48caa135c62e82b50f27fd698a37f5d2554163e6af9a3a97d887f2a1dc510ab3). Résultat : `pieces-comparaison-essaim-v5.md` (sha256 681d341cbbb8700c7af6591247969cee4ba6d03abd5f979cf48946042602301a).

**Bilan : 15 corrections portées sur 15** (44 à 58), en 17 opérations : 13 remplacements, dont 4 donnés « de … à … », et 4 ajouts sans ANCIEN. Chaque ANCIEN, chaque borne et chaque ancre a été trouvé exactement une fois. Rien n'a été deviné ; trois places d'ajout ont été choisies, signalées ci-dessous.

**Numérotation.** La relecture c1cebee3… numérote ses corrections à partir de 44. Or la relecture précédente (44b7d86e…) avait déjà une correction 44, portée en v4 (pièce 2 (b), point 5). Ici, « correction 44 » désigne toujours celle de c1cebee3… (conclusion, pièce 1).

**Méthode.** Script `portage_pieces_essaim_v5_v1.py` (sha256 1d78af81e30630271d78a441e9c4469854fa34551923c59703548ee8ad437edf), lancé par `python3 -I`, code de sortie 0. Chaque ANCIEN et chaque NOUVEAU est lu par programme dans la relecture, entre le premier « et le dernier » de la ligne. Le script s'arrête, sans rien écrire, si un ANCIEN, une borne ou une ancre ne se trouve pas exactement une fois.

**Vérifications par programme** (sortie : `portage-pieces-essaim-v5-sortie-v1.json`, sha256 0311a9dadf93686895f1448639df74b3be041a1888839a70f4c81b809f87c22c) :
- chaque NOUVEAU est présent dans la v5 ;
- chaque ANCIEN en est absent, sauf pour les corrections 47 et 53, où l'ANCIEN est contenu dans le NOUVEAU et figure une seule fois ;
- chaque ajout suit son ancre ;
- défaire les 17 opérations, dans l'ordre inverse, rend exactement le corps de la v4.

Hors du corps de la pièce, seul l'en-tête change : un en-tête neuf (un titre et six puces), puis l'en-tête de la v4 gardé tel quel.

| N° | Lieu | ANCIEN trouvé | Porté | Remarque |
|---|---|---|---|---|
| 44 | Conclusion, pièce 1 | oui, 1 | oui | Remplacement. |
| 45 | Réserves, troisième puce | oui, 1 | oui | Remplacement. Le NOUVEAU cite « épreuve aveugle 5fc15fc0… » : c'est la v1 du rapport, dont les nombres étaient faux ; l'erratum est la v2 (8720522f…). Porté tel quel (point ouvert 7). |
| 46 | Section 3, première puce | oui, 1 | oui | Remplacement. |
| 47 | Article 1, fin | oui, 1 | oui | « La même phrase, suivie de » : ANCIEN gardé, ajout après une espace. |
| 48 | Article 2, trois premières puces | oui : début 1, fin 1 | oui | Plage remplacée par les quatre puces du NOUVEAU. La puce « Minimum » reste. |
| 49 | Article 3, les trois puces | oui : début 1, fin 1 | oui | Plage remplacée par les deux puces du NOUVEAU. « Les clauses sur Argon passent à l'article 14 » est une consigne de portage, non un texte ; elle est tenue par la puce « Argon » de l'article 14. Deux phrases de la v4 n'y passent pas mot pour mot (point ouvert 6). |
| 50 | Article 4, en entier | oui : début 1, fin 1 | oui | Plage remplacée. Les deux motifs sont identiques à ceux du code de référence (vérifié par `epreuve_motifs_v5_v1.py`). |
| 51 | Article 9, puce « Motifs » | oui : début 1, fin 1 | oui | Plage remplacée (« Motifs » devient « Balises »). |
| 52 | Article 10, ajout en tête | sans ANCIEN | oui | **Place choisie** : première puce, sous le titre de l'article, à la forme des autres puces (« - **Champ.** … »). |
| 52 | Article 10, « cellules d'Argon exclues, » | oui, 1 | oui | Remplacement. |
| 53 | Article 11, tableau | oui, 1 | oui | « La même ligne, suivie de » : rangée ajoutée sous « Verdict « facultatif » ». |
| 54 | Article 12, première puce | oui, 1 | oui | Remplacement. |
| 55 | Article 13 | oui, 1 | oui | Remplacement. |
| 56 | Article 14, nouveau | sans ANCIEN | oui | Inséré après l'article 13, avant l'annexe à l'article 5, sans les guillemets extérieurs. L'ancre est la fin de l'article 13, unique. |
| 57 | Pièce 2 (a), plan, ajout | sans ANCIEN | oui | **Place choisie** : dernière puce du plan, après celle de l'enveloppe. |
| 57 | Pièce 2 (a), liste d'arrêt | oui, 1 | oui | Remplacement. |
| 58 | Décision 1, recommandation | oui, 1 | oui | Remplacement. La phrase ne figure qu'une fois dans la v4. |
| — | Ajout hors pièces (consignes des tours III.1 et III.3) | sans ANCIEN | non | Hors de la pièce, par la relecture elle-même. Rien n'est modifié dans le collisionneur (points ouverts, partie B). |
| — | Code de référence de l'article 4 | — | non | Non porté dans la pièce : la relecture ne le donne pas comme texte de la pièce. Il est exécuté tel quel par les deux scripts d'épreuve. |
| — | Décisions 6 et 7 | — | non | Données par la relecture comme décisions du directeur, sans ANCIEN ni NOUVEAU ; non ajoutées à la liste des décisions de la pièce (points ouverts 1 et 2). |

**Suite** : `epreuves-pieces-essaim-v5-v1.md` (épreuves) et `points-ouverts-pieces-essaim-v5-v1.md` (points ouverts).
