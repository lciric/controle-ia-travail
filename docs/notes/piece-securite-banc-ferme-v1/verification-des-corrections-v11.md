# Vérification des changements — pièce de sécurité du banc fermé, v12 — v11

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v12.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `d60beae4523942d5b4fb259f705030d5ab481d3a`. Empreinte recalculée : `399f530a9de403e41704924e06fe623c584d1202e976db9bf5bf67339e000d32`, égale au `.sha256`. La v11 est intacte (`af429106…`).
- **Référence** : `verification-des-corrections-v10.md` (`ea16c756…`), qui acceptait la v11.
- **Vérificatrice** : la même contre-lectrice (Opus 5.5). **Date** : 21 novembre 2026, vers 19:55 UTC.
- **Méthode** : différence ligne à ligne entre la v11 et la v12, relue contre la table de la section 18.
- **Source [N60]** : `docs/decisions/decision-N-060-v3.md`, empreinte recalculée `2b448f69…`, égale à celle que cite la pièce. J'en ai lu les lignes 22 et 23 seules, qui disent ce qu'est la question fermée de l'oracle : « pour chaque contrôle expérimental de l'article (`cibles.controls`), une question fermée — absent, altéré ou conforme dans le plan de l'agent ». Le conflit que la v12 corrige est donc réel. Mon point M8 de la v8, appliqué à la lettre (questions identiques pour tous les produits), aurait arrêté le premier envoi. C'était une erreur de ma part de formuler M8 comme une identité entre toutes les tâches, alors que ce qu'il fallait protéger était l'indépendance à la condition.

## Constat

- **La règle neuve protège ce que M8 voulait protéger.** Les questions sont fonction de la tâche seule : gabarit unique scellé, paramètres tirés de la référence par une règle exhaustive et ordonnée, listes scellées avant la course. Les deux jumeaux d'une paire partagent la tâche et reçoivent donc le même jeu. Aucune question ne peut distinguer les conditions. L'exhaustivité empêche une liste de pointer le contrôle visé ; la réserve 20 dit honnêtement qu'elle se vérifie sur la règle et l'attestation, non sur le contenu de la référence.
- **Garde 15 étendue aux questions.** Elle les lit avant le scellement de la liste et à l'envoi, avec un artefact neuf. C'est juste.
- **Ce qui sort de plus** : les contrôles de la référence d'une tâche, qui sont de la matière de tâche et non du coffre, sous les conditions de conservation et de lecture humaine du champ n° 18. Ce qui se devine : deux appels d'une même tâche se reconnaissent, sans que l'on sache lequel est l'honnête. Tout cela est dit, et rattaché au risque 13. Je partage l'avis de la section 18 : la règle n'est pas affaiblie sur ce qu'elle protège.
- **Réserves 19 à 21** : exactes. La réserve 19 pose bien le nœud si l'oracle d'une famille ne se ramène pas au gabarit.
- **Point 4 de l'auteur**, la lecture de [N60] : ce n'est pas un manquement. [N60] est une décision de Lazar sur `main`, citée par CLAUDE.md. L'auteur n'y a lu aucune conception, aucun résultat, aucun seuil de moniteur ; il le déclare et la pièce ne reprend aucun des noms.
- **Point 5 de l'auteur** (le tableau de la section 15 laissé tel quel) : accepté.
- **Contenu d'attaque** : aucun. **Refus de classifieur** : aucun.

## Point

**M13 — mineur — Où se fait la comparaison entre jumeaux (point 3 de l'auteur).** La garde 14 compare les jeux des deux membres d'une paire « avec la table de correspondance scellée, par programme, sans qu'aucun lecteur ni l'envoyeur ne la voie ». Mais la garde 14 s'applique « à chaque appel », donc dans l'environnement de l'envoyeur. Or la condition 2 exige que l'envoyeur n'ait pas la table des conditions. Si le programme lit la table dans cet environnement, la table y est, et la phrase « sans que l'envoyeur la voie » n'est qu'une promesse. C'est une brèche possible dans l'aveuglement.

**Correction demandée.** L'égalité entre jumeaux est une conséquence de deux contrôles qui n'ont pas besoin de la table : chaque produit reçoit exactement la liste scellée de **sa tâche**, et les deux jumeaux partagent la tâche. La garde 14, à l'envoi, n'a donc besoin que de la correspondance entre produit et tâche, qui ne dit pas la condition. Il faut écrire l'un des deux :
- (a) la comparaison entre jumeaux par la table est retirée de la garde 14 à l'envoi, et remplacée par la conformité à la liste de la tâche ;
- (b) elle est faite, si on la garde, **avant** l'envoi, là où se trouve le lot (comme la garde 15). Seule une attestation par empreinte passe alors à l'envoyeur, et la table ne quitte jamais la quarantaine.

Il faut aussi ajouter à la garde 17 ou à la garde 14 un artefact : la table de correspondance présente dans l'environnement de l'envoyeur. Je recommande (a), qui est plus simple et ne déplace rien.

## Verdict

**À corriger** : un point mineur (M13), aucun bloquant. Le fond de la règle des questions est accepté. Une v13 qui ne corrige que M13 sera vérifiée sur sa seule différence (`verification-des-corrections-v12.md`).
