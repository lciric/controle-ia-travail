# Table des corrections 23 à 42 (pièces de la comparaison essaim contre isolé, version 3)

22 novembre 2026, Opus 5.5 (règle GO-2026-11-21-84 : corrections portées mot pour mot, rien d'inventé). Remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/relecture-pieces-essaim-v2/relecture-fable-api.md` (sha256 0cec14ce096574666db1c4b4368b6cf89d3f471e8e2d5c5aed29080c764ccb0f), section 3. Base : `pieces-comparaison-essaim-v2.md` (sha256 20f487e2d28f4be59efb2087f0cebed00479217b6e93e8d828e1215a4ae66938). Résultat : `pieces-comparaison-essaim-v3.md` (sha256 3931390197977729947f87cf66cd7ce8e388639f10de18692d618ed786886734).

Bilan : 20 corrections portées sur 20 (19 remplacements, 1 insertion) ; aucune non portée. Chaque ANCIEN a été trouvé exactement une fois ; le script de portage échouait sinon, sans deviner. Hors du corps de la pièce, seul l'en-tête a changé : première ligne prescrite, puis les empreintes de la base et des remarques ; l'en-tête de la version 2 est gardé tel quel en dessous.

Méthode : les blocs ANCIEN / NOUVEAU ont été lus par script dans la relecture et remplacés tels quels. Seul retrait : l'alignement de huit espaces des lignes de suite de NOUVEAU (largeur du préfixe « NOUVEAU »), à la correction 28, dont la seconde ligne devient une puce de l'article 9 au même niveau que les autres.

| N° | Lieu | Portée | Pourquoi / remarque |
|---|---|---|---|
| 23 | Réserves | oui | ANCIEN unique ; remplacé mot pour mot. |
| 24 | Section 2 | oui | ANCIEN unique ; remplacé mot pour mot. |
| 25 | Section 3 | oui | ANCIEN unique ; remplacé mot pour mot. |
| 26 | Article 3 | oui | ANCIEN unique (fin de phrase) ; remplacé mot pour mot. |
| 27 | Article 4 | oui | ANCIEN unique ; remplacé mot pour mot. |
| 28 | Article 9 | oui | ANCIEN unique ; remplacé par les deux puces de NOUVEAU (alignement retiré, voir Méthode). L'épreuve des motifs prescrite a été jouée : **elle échoue** (6 textes sur 10), voir `epreuve-motifs-correction-28-v1.md`. Selon la correction 28, les motifs ne sont pas scellables tant que l'épreuve n'est pas réussie ; le motif de duel est à retoucher par quelqu'un qui a lu les consignes. Non fait ici. |
| 29 | Article 5 | oui | ANCIEN unique (la phrase suivante, « Il est calculé… », reste) ; remplacé mot pour mot. |
| 30 | Article 6 | oui | ANCIEN unique ; remplacé mot pour mot. |
| 31 | Article 10 | oui | ANCIEN unique ; remplacé mot pour mot. |
| 32 | Article 10 | oui | ANCIEN unique ; remplacé mot pour mot. |
| 33 | Article 11 | oui | ANCIEN unique ; remplacé mot pour mot. |
| 34 | Article 11 | oui | ANCIEN unique ; 0,15 devient 0,05. Fable signale que c'est la seule correction hors de la lettre de la consigne ; son repli (garder 0,15 noté « antérieur à la contre-lecture ») n'est pas porté, la correction elle-même l'étant. Décision à la mère ou au directeur si le repli est préféré. |
| 35 | Article 12 | oui | ANCIEN unique ; remplacé mot pour mot. Plus aucune mention de « balise » hors de la réserve de la correction 23, qui la nie. |
| 36 | Annexe | oui | Insertion, non un remplacement : le bloc est placé après l'article 13, juste avant « **Pourquoi pas mieux [HYPOTHÈSE].** » (ancre trouvée une fois), séparé par une ligne vide. Texte du bloc gardé tel quel. |
| 37 | Pièce 2 (a), règle | oui | ANCIEN unique ; remplacé mot pour mot. |
| 38 | Pièce 2 (a), arrêt | oui | ANCIEN unique ; remplacé mot pour mot. |
| 39 | Pièce 2 (b), point 5 | oui | ANCIEN unique ; remplacé mot pour mot. Réserve de Fable gardée ouverte : si la garde de motifs ne peut ni lire un fichier hors du dépôt ni se limiter aux textes du programme, supprimer la puce. Le fonctionnement de la garde n'a pas été vérifié ici ; question à trancher avant le scellement. |
| 40 | Pièce 2 (c), avertissement | oui | ANCIEN unique ; remplacé mot pour mot. |
| 41 | Pièce 2 (c), détection | oui | ANCIEN unique ; remplacé mot pour mot. |
| 42 | Pièce 2 (c), mode isolé | oui | ANCIEN unique ; remplacé mot pour mot. |

Ce qui reste hors du texte (section 4 de la relecture, sans changement de texte) : le marqueur « false » près de « false alarm » ou « false positive », et les décimales de la valeur vraie (« 36,4 % », « 95,1 % »), à éprouver avec les dix phrases synthétiques et au pilote. Rien n'a été porté pour ces deux points.
