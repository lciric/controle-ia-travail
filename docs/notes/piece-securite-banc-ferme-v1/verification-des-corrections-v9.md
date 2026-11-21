# Vérification des changements — pièce de sécurité du banc fermé, v10 — v9

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v10.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `d4ebacd48b4d35043f44718944a3ac35585996a0`. Empreinte recalculée : `bf19bdd078cfed9b32df4f6031d42b77e16a8fc5ca343cb7247bfe3de7c811e1`, égale au `.sha256`. La v9 est intacte (`3eb3b85f…`).
- **Référence** : `verification-des-corrections-v8.md` (`06f40f57…`), qui acceptait la v9.
- **Vérificatrice** : la même contre-lectrice (Opus 5.5). **Date** : 21 novembre 2026, vers 19:35 UTC.
- **Méthode** : différence ligne à ligne entre la v9 et la v10, relue contre la table de la section 16.
- **Source neuve [CF]** : `docs/notes/banc-ferme-choix-contre-lecture-fable-v1/contre-lecture-trois-choix-banc-ferme-fable-v1.md`, sur `main` au commit `c40eee73`. Empreinte recalculée `bc9ec0fd…`, égale. J'en ai lu les sections 1.3 et 1.4 seules, comme l'auteur.

## Constat, point par point

| Lieu | Constat |
|---|---|
| Condition 1, « vers des lecteurs nommés » | Conforme à [CF] 1.3, « Ce qui doit exister », point 1. |
| Condition 2, opérateur et poste de transit | Conforme au point 5 de [CF]. Le lieu où produits, clés et réseau se rencontrent est nommé au préenregistrement, et seulement pour les produits extraits. La garde 17 est éprouvée sur un artefact neuf (clé présente sur le poste de transit), et une ligne d'arrêt est ajoutée. |
| Condition 5, journal en deux parts | Conforme au point 1 de [CF] (« journal des appels par empreintes hors quarantaine, contenus dedans »). La part versable ne porte ni texte, ni condition, ni identifiant d'origine. Le nouvel artefact de la garde 17 le vérifie. |
| Condition 10, appel sans mémoire | Conforme à [CF] (« Si un lecteur est un modèle Claude »), et étendue à tout lecteur. C'est plus strict. |
| Condition 11, famille des moniteurs et des juges | La règle générale est juste et va du côté prudent. **Remarque, sans point** : [CF] pose le cas de la famille Mistral **sous condition** (« si ce panel les lit »). La v10 écrit que les deux mesures du papier C « lisent ces épisodes », en tenant la condition pour remplie. Comme l'exclusion vaut jusqu'à l'audit des lignées et que la réserve 17 dit que le statut du panel n'est pas vérifié, l'effet est le même. Une version ultérieure pourra rétablir le conditionnel. |
| Condition 12, lecteurs de l'oracle éprouvé | Conforme au point 4 de [CF]. |
| Champ n° 18 | Il exige une version datée (jamais un alias), et la famille est attestée contre les moniteurs et les juges. Conforme. |
| Gardes 15 à 17 | Les deux artefacts que demande [CF], une charge portant un mot témoin et un destinataire hors liste, sont ajoutés tels quels. S'y ajoutent l'alias sans version datée, le lecteur appelé par une session, le texte dans la part versable et la clé sur le poste de transit. Ils sont tous éprouvables contre le faux fournisseur local. |
| 4.2, deux lignes neuves | Elles sont cohérentes avec les conditions 2, 10, 11 et 12. |
| Point 14 de 6.1 | Récrit selon [CF] : version datée, rétention, journal en deux parts, règle du refus. |
| Points 24, 27 et 29 | Ils sont complétés en cohérence avec ce qui précède. |
| 6.4, replis | L'ordre est celui de [CF] 1.4 : un second lecteur à poids ouverts sur machine fermée, avec devis et GO, puis les deux juges du programme. Les inconvénients sont dits. Le repli reste un nœud. |
| Réserves 17 et 18 | Elles sont exactes. La réserve 18 dit honnêtement que l'environnement de l'envoyeur n'est pas confiné comme le banc, mais seulement borné à l'entrée et à la sortie. |
| Section 16 | Elle décrit fidèlement la différence. Il n'y a aucun changement non déclaré, et rien n'est relâché par rapport à la v9. |

## La question de l'auteur sur son cloisonnement (point 1)

Je n'y vois **aucun manquement**. Le cloisonnement de l'auteur interdit les conceptions, les résultats et les seuils des moniteurs. Le nom d'un modèle d'un panel de juges n'est rien de cela. Il figure déjà en clair sur `main`, dans le registre et dans le code que [CF] cite, et ce n'est pas l'identité du moniteur témoin que [PR] cache à l'attaquant informé. L'auteur l'a déclaré, et c'est ce qu'il fallait faire.

Prudence pour la suite, sans point : une pièce de sécurité gagne à écrire ses règles de famille en termes généraux, et à laisser les noms à l'audit des lignées de la mère.

**Contenu d'attaque** : aucun. **Refus de classifieur** : aucun.

## Verdict final

**Accepté** : la pièce de sécurité du banc fermé, v10 (`bf19bdd0…`). Aucun point sur les changements de la v10. La v9 avait été acceptée avant (`verification-des-corrections-v8.md`).

Bilan de toute la chaîne, de la v1 à la v10 : 3 points bloquants et 16 mineurs, tous corrigés.

L'acceptation n'autorise ni construction, ni course, ni envoi, ni dépense. Les préalables à l'envoi restent ceux qu'énumère `verification-des-corrections-v8.md`. S'y ajoutent l'audit des lignées, pour la condition 11, et le nom du lieu de l'envoyeur au préenregistrement.
