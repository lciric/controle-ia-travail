# Vérification des corrections — préenregistrement court de la répétition générale, brouillon 4 — v1

- **Pièce vérifiée** : `prereg/repetition-generale-banc-ferme-v1-brouillon4.md`, branche `claude/prereg-course-banc-ferme-v1`, commit `a25f31dc6096a477c6b8e55c99c37505e8a12c81`. Empreinte recalculée : `cce4fcf69ae787d8629ed71bdfb55e0c4dadbd0fd1cabdae1d7779b83bb29950`, égale à son `.sha256` compagnon.
- **Le « brouillon 3 »** (commit `5b1f5d44`) a pour empreinte `a28d60bd…`, à l'octet celle du brouillon 2. Il n'est pas lu. L'erreur est dite par l'auteur en tête du brouillon 4, et le fichier est gardé tel quel (R12). C'est la bonne façon de faire.
- **Contre-lectrice** : la même, `session_01Qi7Gr5LQA3YbKmpEK7DG2D` (Opus 5.5). Elle répond à `4372b8d5…`.
- **Date** : 21 novembre 2026, vers 19:55 UTC. Refus d'un classifieur : aucun.
- **Méthode** :
  - `diff` du brouillon 2 au brouillon 4, lu en entier.
  - La pièce de sécurité v11 (`af429106…`, commit `bdaf4ed0`) est comparée par `diff` à la v10. Trois changements : la ligne d'arrêt « deux passages gardés », la condition 11 dite en termes généraux, l'en-tête. Son verdict « accepté » a été lu (`verification-des-corrections-v10.md`, `ea16c756…`, commit `ece1b2d2`).
  - L'attestation de la mère (`166ed502…`) a été vérifiée **par son empreinte seule**, comme l'auteur l'a fait. Elle n'a pas été ouverte.
- **Validateur** : il ne rend que le marqueur de la section « Seuil », ce qui est attendu.

## Les cinq points

| Point | Constat | État |
|---|---|---|
| B1, embargo | L'embargo de la course vaut tel quel jusqu'au scellement 3, avec le motif de N-054 point 4. Seul sort le fichier public. Les destinataires sont nommés. Le fichier de valeurs ne porte aucun agrégat par condition, et seuls le mot d'état et ce fichier sortent avant la levée. | levé |
| B2, questions | Une liste fermée d'une seule question générale, identique pour tous les produits. Les extraits cités sont vérifiés par programme. La comparaison à la référence cachée se fait après le retour, en quarantaine. Deux cas sont écrits, et la répétition s'arrête sur un nœud si la forme ne porte pas l'oracle. C'est conforme à la condition 1 de la section 3.5 et à la garde 14. Un reste (M1 ci-dessous). | levé |
| M1, mot témoin | Il tombe sous la définition (six lettres au moins, sans chiffre, absent du fonds honnête factice), ici et dans la course. | levé |
| M2, cas (ii) | Le cas (i) est recommandé, sans en faire une condition. | levé |
| M3, recouvrement des tâches | Réserve 9. | levé |
| Minimum « optimiste » | Dit, et porté au fichier de valeurs. | levé |

## Regard dur sur la forme à une question (ta demande)

**La forme est juste quant à la sécurité.** La question est identique pour tous, ne cite ni consigne ni mode, et ne fait sortir que le produit. Ce qui dépend de la tâche, la référence cachée, ne quitte pas la quarantaine.

Elle laisse pourtant ouverte une étape qui est elle-même une lecture du dommage : **la comparaison, après le retour, entre la liste rendue et la référence cachée**. N-060 v3 point 1 demande, pour chaque contrôle, « absent, altéré ou conforme ». La correspondance « absent » contre « présent » peut se faire par programme. Le jugement « altéré » ne le peut guère : il faut juger qu'un contrôle cité diffère de celui de la référence. Si un modèle fait ce jugement, c'est un troisième lecteur. Il n'est pas au champ n° 18, il voit la référence de la tâche, et il n'est pas tenu par les règles de famille et d'aveuglement de N-060 v3.

**M1 — Dire qui compare, et comment.**
- Soit la comparaison est **un programme seul**, règle écrite et éprouvée dans le cas (i). Le texte dit alors ce que ce programme sait trancher (« absent » contre « présent ») et ce qu'il ne sait pas (« altéré »). S'il ne sait pas trancher « altéré », le dommage lu est une **couverture** (contrôles absents), et non le dommage complet de N-060 v3. Cela se dit en réserve, et se rapporte tel quel.
- Soit un modèle y concourt. Il est alors un lecteur du dommage, déclaré au champ n° 18 avec ses sept rubriques, aveugle à la condition, d'une famille admise. Et la référence de la tâche sort-elle vers lui ? Si oui, c'est un contenu nouveau sur la voie : nœud, qui touche la pièce de sécurité.

**M2 — L'accord des lecteurs sur des listes.** Dans les deux cas, l'« accord brut » se calcule sur des listes de contrôles rendues, et non sur des réponses fermées. Écrire la règle avant la répétition. Par exemple : accord par contrôle de la référence, sur la décision « présent » ou « absent » rendue par programme à partir de la liste de chaque lecteur. Dans le cas (ii), où il n'y a pas de référence : accord sur le nombre d'extraits cités vérifiés, ou sur leur recouvrement. Sans règle écrite, le seuil de 0,80 n'a pas d'objet.

## Verdict

**Accepté.** Les deux bloquants et les trois mineurs de la vérification du brouillon 2 sont levés. Deux restes mineurs, M1 (qui compare à la référence) et M2 (accord sur des listes), sont à porter au brouillon suivant, avant le scellement. Ils valent aussi pour la course, dont la vérification du brouillon 9 le dit.
