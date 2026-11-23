# Fiche de lecture — 2508.00161 — v1

- **Titre** : Watch the Weights: Unsupervised monitoring and control of fine-tuned LLMs (conférence ICLR 2026).
- **Auteurs** : Ziqian Zhong, Aditi Raghunathan. **Identifiant** : arXiv 2508.00161 v3.
- **PDF** : `docs/sources/pdf/mecanisme-adjudant-v1/2508.00161v3.pdf`, sha256 `898dffaf6d1b50badf25c72f0cb89e42ab16e723248e357e94ed2bd48b3948a0` (vérifiée par `sha256sum`, 39 pages).
- **Décision lue** : `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v2.md`, ligne 110 ; puis la v3 (l. 110 et tableau des citations, l. 214) et ses errata 1 à 3, le 3 v2 primant (point 8, forme réécrite, retenue).
- **Lecteur** : Opus 5.5, effort élevé. **Date** : 2026-11-23T08:47Z (`date -u`).

---

## (a) Ce que le papier établit

Les premiers vecteurs singuliers de la différence de poids entre modèle affiné et modèle d'origine portent les comportements acquis ; on surveille les activations le long de ces directions, sans donnée d'affinage (p. 1). Le moniteur garde, par direction, le minimum et le maximum vus ; une entrée hors de cette plage est signalée, **et la plage est élargie** (p. 4, 5). Après n − 1 épisodes ordinaires, le taux de fausses alertes est borné par 2t/n + O(1/n²) pour t directions (p. 5), preuve sous tirages indépendants et échangeables (p. 17). Portes dérobées : 93 % à 100 % des réponses signalées dès la première fois, moins de 1 % de fausses alertes (p. 2, 7) ; un cas à déclencheurs multiples ne signale que 27,27 % des invites (p. 8). Limites : « not adversarially robust », poids d'origine requis (p. 16).

## (b) Ce que la décision voulait, et si le papier le permet

La v3 (l. 110) cite ce moniteur comme contre-indice à « nouveauté seule = mise à jour des témoins » : il « accepte un écart qui grandit pas à pas ». **Le permet en partie.** Le mécanisme est aux pages 4-5, mais un écart qui grandit dépasse à chaque pas l'extrême courant : il est signalé à chaque pas. Ce qui passe en silence est **la répétition d'un écart déjà signalé une fois**, profil même du saboteur diffus. Cette conséquence se lit sur l'algorithme ; les auteurs ne la testent pas. La borne des fausses alertes suppose des tirages échangeables, et un flux qui dérive rompt cette hypothèse (p. 17). L'usage survit en v3 et sous l'erratum 3 v2, point 8 (a).

## (c) Usage pour l'entretien et le billet

Il prévient l'objection « pourquoi des sondes supervisées, quand une surveillance sans données lit l'affinage dans les poids ? ». **Base nommée** pour la famille d'organismes affinés sans consigne (N-053, point 2) ; **sans objet** pour le saboteur instruit du billet, dont les poids ne changent pas. Antériorité : lentilles tirées des poids et surveillance non supervisée de l'affinage, occupées.

## (d) Plus petite action

À la v4 de N-075, récrire la phrase de la l. 110 : « une alerte par extrême neuf ; la répétition d'un écart déjà signalé ne sonne plus (p. 5) ; borne sous échangeabilité (p. 17) ». Dix minutes, aucune dépense. Mesurer la base « lecture des poids » demanderait un devis et un GO.
