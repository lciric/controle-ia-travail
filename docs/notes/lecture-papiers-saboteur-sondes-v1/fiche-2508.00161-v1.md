# Fiche de lecture — 2508.00161 — v1

- **Titre** : Watch the Weights: Unsupervised monitoring and control of fine-tuned LLMs (conférence ICLR 2026).
- **Auteurs** : Ziqian Zhong, Aditi Raghunathan. **Identifiant** : arXiv 2508.00161 v3.
- **PDF** : `docs/sources/pdf/mecanisme-adjudant-v1/2508.00161v3.pdf`, sha256 `898dffaf6d1b50badf25c72f0cb89e42ab16e723248e357e94ed2bd48b3948a0` (vérifiée par `sha256sum`, 39 pages).
- **Décision lue** : `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v2.md`, ligne 110 ; puis la v3 (l. 110 et tableau des citations, l. 214) et ses errata 1 à 3, le 3 v2 primant (point 8, forme réécrite, retenue).
- **Lecteur** : Opus 5.5, effort élevé. **Date** : 2026-11-23T08:47Z (`date -u`).

---

## (a) Ce que le papier établit

Les premiers vecteurs singuliers de la différence de poids entre un modèle affiné et son modèle d'origine portent les comportements acquis à l'affinage ; on surveille le cosinus des activations le long de ces directions, sans aucune donnée d'affinage (p. 1). Le moniteur garde, par direction, le minimum et le maximum vus ; une entrée hors de cette plage est signalée, **et la plage est élargie** (p. 4, 5). Vingt directions par matrice, quarante par couche (p. 5). Le taux de fausses alertes après n − 1 épisodes ordinaires est borné par 2t/n + O(1/n²) pour t directions (p. 5), preuve sous tirages indépendants et échangeables (p. 17). Portes dérobées : 93 % à 100 % des réponses signalées dès la première fois, moins de 1 % de fausses alertes (p. 2, 7) ; un cas à déclencheurs multiples ne signale que 27,27 % des invites (p. 8). Désapprentissage : 36,21 % à 95,42 % détectés (p. 2, 8). Limites des auteurs : méthode « not adversarially robust » (une permutation des dimensions cachées la défait), poids d'origine requis (p. 16).

## (b) Ce que la décision voulait, et si le papier le permet

La v3 (l. 110) cite ce moniteur comme contre-indice à « nouveauté seule = mise à jour des témoins » : il « accepte un écart qui grandit pas à pas ». **Le permet en partie.** Le mécanisme est bien aux pages 4-5. Mais un écart qui grandit dépasse à chaque pas l'extrême courant : il est donc signalé à chaque pas. Ce qui passe en silence, c'est **la répétition d'un écart déjà signalé une fois** : c'est exactement le profil d'un saboteur diffus. Les auteurs ne testent pas cette conséquence. Elle se lit sur l'algorithme, pas dans un résultat. La borne des fausses alertes suppose des tirages échangeables, et un flux qui dérive rompt cette hypothèse (p. 17). L'usage survit en v3 et sous l'erratum 3 v2, point 8 (a).

## (c) Usage pour l'entretien et le billet

Il prévient l'objection « pourquoi des sondes supervisées, quand une surveillance sans données lit l'affinage dans les poids ? ». Il donne une **base nommée** pour la famille d'organismes affinés sans texte de consigne (N-053, point 2) : la sonde doit battre la lecture des poids. Pour le saboteur instruit par consigne du billet, la base est **sans objet**, puisque les poids ne diffèrent pas. Il crée une antériorité : les directions tirées des poids, comme lentille et comme surveillance non supervisée des comportements affinés, sont occupées.

## (d) Plus petite action

À la v4 de N-075, récrire la phrase de la l. 110 : « une alerte par extrême neuf ; la répétition d'un écart déjà signalé ne sonne plus (p. 5) ; borne sous échangeabilité (p. 17) ». Coût : dix minutes de session, aucune dépense. Si la base « lecture des poids » est mesurée sur la famille affinée, il faut un devis et un GO.
