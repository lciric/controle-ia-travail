# Journal de la synthèse finale du niveau 3 de l'état de l'art — v1

Écrit le 2026-11-13, de 18:16 à 18:26 UTC (heures relevées par `date -u` ; l'horloge du conteneur avance très lentement
par rapport au travail fait, comme l'avait noté le rapport C7 : ces heures ne mesurent pas la durée réelle). Auteur :
lecteur neuf (sous-agent, Claude Fable 5.2), dans la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`. Compagnon de
`etat-de-l-art-verifie-niveau3-v1.md`. Mandat : mot de Lazar, `registres/decisions.md`, R-2555, point D.

## 1. Sources et empreintes

Récupération : `git fetch origin refs/heads/<branche>:refs/remotes/origin/<branche>` pour les deux branches nommées,
puis `git show` vers un dossier temporaire hors dépôt. Aucun autre appel réseau.

| branche | tête lue |
|---|---|
| `prep/etat-de-l-art-niveau3-v1` | `f0aaf0d1b3f18764d4f728faf6ec5ce9b5cc6854` |
| `prep/etat-de-l-art-niveau3-pieces-v1` | `10016a61c3e42ea3889cf0b0089c2cfbde50402f` |
| `main` (notes de veille, décisions) | `07b4d7c567223f3645aa143f9ba5738084fabeab` |

Chaque fichier ci-dessous a été recalculé par `sha256sum` et comparé à son compagnon `.sha256` : **tous conformes**.

| fichier | sha256 |
|---|---|
| `etat-de-l-art-verifie-niveau3-v1-provisoire1.md` | `8adb561d52b728114cfd0c3065fe6c6230262f1befaeb2fd9d9824270ecdc3ad` |
| `etat-de-l-art-verifie-niveau3-v1-provisoire1-complement1.md` | `a4176d46d5ec24406b38c82e8c653916ee0369a9b4a540f7da6fa4b108c0e33f` |
| `registres/passations/2026-11-10-1112-etat-de-l-art-niveau3.md` | `cb5edb6a7b22fd2b71def44a28ba0445d6d699694469b37f22b235fe09b43589` |
| `registres/passations/2026-11-10-1115-pieces-reseau-niveau3.md` | `75218434ef3292a7608523dca288812288f5182bb6c06a2496e30d3e31d98f23` |
| `niveau3-v1/consignes/consigne-commune-lecteurs-v1.md` | `551118525db692e375b2eede8fa0f26e701cda084798d1284e8be0a82d6a2fd8` |
| `docs/notes/lecture-veille-2611.04556-influence-inter-agents-v1.md` | `211a6448e1ba10642c5e3532d0c8e8f874ed7b1deceb112455b12dd645257515` |
| `docs/notes/contre-lecture-veille-2611.04556-v1.md` | `af2fcb07d67cd5455ec1fe9c22ca91faae8b0ffb961de6df80a2128450e3aadf` |
| `docs/sources/pdf/niveau3-v1/provenance-niveau3-lot8-listes-fille-hors-archives-v1.md` (consultée par recherche de termes seulement) | `6ba353eaab71532b096e86404f0349c3e0efe8e5d9b99c946b4fbb1984174dc8` |
| `rapport-B1-tracabilite-programme-texte-envoye-v1.md` | `812f1b535427595c2d8216d7d63a6aa06e34ffac7bfbe8c2bfcba0be0c63e6aa` |
| `rapport-B2-tracabilite-etat-de-l-art-v1-et-hors-archive-v1.md` | `ac0d3e29aa850e464416b58871fd7b1463a15d060251ac6a86792cf6a24bfd27` |
| `rapport-B3-tracabilite-socle-v1.md` | `30f409c944ca1de5f5d001f5e83104696f9e3f70049f2cb2064c8dff16649966` |
| `rapport-C1-voisin-proche-helios-H1-H2-H3-v1.md` | `89e2edad5dd6c08d6a81bc856d729df2d5f961bf98c2b1d8d93d8ba2c685b452` |
| `rapport-C2-lemme-theoreme-v1.md` | `76475485116b026fd1c966c70f924eb021a8fb1764347e9db85d37e263fcad73` |
| `rapport-C3-loi-de-deference-papier-C-v1.md` | `d7efc7f252b6c9416702952871e5b67a2327ef61f1e4598135602bfa90266bba` |
| `rapport-C4-organisme-ideation-O1-O20-v1.md` | `164502a3ed94e0adf177e4e15bfd61fc95ea24633dc1c4a2b0cacf9effab1245` |
| `rapport-C5-pieces-recentes-au-depot-v1.md` | `804cd3a77202d4841d310328ea7b4d7ca7afdd794953aa496f411351173aeddc` |
| `rapport-C6-H9-cemri-hammond-references-statistiques-v1.md` | `36d26d20e284fbf9ecccb219df06765ffc9af025650cbaa520aaf79dceccabfa` |
| `rapport-C7-contre-lecture-qu-chen-wang-dossier-c8-v1.md` | `63d8373761d28c62b556f35839bd7b9f277decf4dc2d6d1ad44ad1f2266f8fb2` |
| `rapport-C8-pieces-neuves-papier-A-v1.md` | `30cae1c40885c110b0432a6e80cb13c3392cbb8dadee16c6a50948d62d42110b` |
| `rapport-C9-pieces-neuves-papiers-C-B-v1.md` | `23ec1f6ef8c4445cbb350ac249a8d37cc2d438da9f9253959a3d30821a2b3d54` |
| `rapport-D1-recherche-affirmative-papier-A-v1.md` | `726cc036479c14b2874c2548da426638bce31b3b06999198e563552b6d62e996` |
| `rapport-D2-recherche-affirmative-papier-C-v1.md` | `dc2943441b6c684934de1fb490ebea024df69a6c68ac23ac2c88d75612021dd6` |
| `rapport-D3-recherche-affirmative-papier-B-H9-v1.md` | `a189a005494cd34546602016d20dca2bc61e1aa1f0cf64f9ecdc1e26eead8dab` |
| `rapport-lot1-HC2-mirage-karne-v1.md` | `9996f40cf5614e32c74bc4c97c79a8e88d65c76c6c4635d8ea38d034315c0f4b` |
| `rapport-lot12-pistes-H9-v1.md` | `382ed6e419074a19eecf54f173e551f26c4495e7555b845c65bdcf71ceeec9dd` |
| `rapport-lot2A-billets-boite-blanche-v1.md` | `042db21e2d0bb987cb09f6afb1834cdc21020b67df0b18a602ff505e65b52b02` |
| `rapport-lot2B-billets-moniteurs-attaque-v1.md` | `8b4b5af1f105f70c36650e9cc8febabcaa2c8bf87cea4fe485dfebf9fe5c6a41` |
| `rapport-lot3A-sondes-sabotage-injection-v1.md` | `64b728d63927e8c55a77c0e2372637f3ea9f769477e98bdd46db1d9481264b03` |
| `rapport-lot4A-organisme-O2-v1.md` | `5dfd5251b0592723a1481f0c3178e451f306c63e977b9b6bba4ce8d35b0abafa` |
| `rapport-lot5A-sequentiel-multi-agents-v1.md` | `aef81e6e43b63f7aa0b2277308495dc9a7b0ccaea6e5c37a3d876fd5aac7b88f` |
| `rapport-lot5B-sondes-agents-diffus-v3-v1.md` | `6fd780e1ad5423be3dc82a01e28b0b9fd2ce26dd74c28a8cea210bc7561cd0ba` |
| `rapport-lot7A-sondes-agents-H1-H2-v1.md` | `8a6dd0e0184a7afbf3cbc10e08eb9685817135ed7bcb9503ae095f9f169c3f1e` |
| `rapport-lot7B-collusion-papier-B-v1.md` | `bf9b6af8f2d8a51ae406e8bcd2c53c3eff698826ecf916700ec7ae0dd206633c` |
| `rapport-lot7C-juges-papier-C-v1.md` | `2b03ede00f21e4b5f72cd4b4fb3b3356746e90ff5eefdf73a020661e44cd106f` |
| `rapport-lot7D-delegation-H9-v1.md` | `9f4c3b94203da70075c5cee057fe6f32ea8086b4369081692898009aebf394f2` |

Rapports attendus par la passation de la session sœur et **absents de la branche** : 4-B, 10-A, lecteurs des lots 8, 9
et 11. Les archives de fichiers de travail (`.tar`) des lots n'ont pas été ouvertes.

Lus aussi, sur `main`, pour les énoncés : `docs/programme-controle-ia-v2.md` (sections 5, 13, 16),
`docs/decisions/decision-N-005-N-006-v1.md`, `decision-N-035-v1.md`, `decision-N-065-v1.md` ; `registres/decisions.md`,
lignes R-2176 à R-2186 et R-2551 à R-2555.

## 2. Ce que j'ai lu, et comment

- En entier : la synthèse provisoire, son complément, les deux passations, la lecture de veille, R-2551 à R-2555.
- Pour chaque rapport : l'en-tête (verdict, signalements), les tables de verdicts par énoncé, les sections de
  contre-résultats et « ce qui reste revendicable », les réserves et les refus. **Pas en entier** : les fiches pièce
  par pièce et les annexes de citations, consultées par recherche de termes quand il fallait une page.
- Contre-lecture de veille : sections 0 à 5 et 8 à 10 ; la section 7 (63 citations) non relue.
- **Aucun PDF rouvert.** Toute page citée dans la synthèse est celle du rapport nommé.

## 3. Contrôles faits

1. Empreintes : 27 rapports, 2 synthèses, 2 passations, 2 notes, 1 consigne — toutes conformes (section 1).
2. Complément 1 contre les rapports 7-B, 7-C, 7-D : résultat en section 10 de la synthèse.
3. Chiffres repris de la synthèse provisoire, recherchés dans le rapport d'origine avant reprise : 0,571 et 0,000
   (C1, p. 30) ; 18,67 % (C1, p. 6) ; 0,38 (C1, p. 18) ; 0,88 et 0,737 (C1, p. 27, 30) ; 0,851 à 0,982 (C3, p. 17) ;
   0,194 et −0,018 (C9, p. 2) ; 93,91 % et 99,63 % (C9, p. 1) ; 507 heures (C9, p. 8) ; « about a quarter » (C8, p. 2) ;
   42,3 % et 0,066 (C8, p. 1) ; « triples » (C8, p. 7) ; 0,006 (C8, p. 1) ; 96,5 % et 95,1 % (C8, p. 7) ; 77 % et 12 %
   (C5, p. 1) ; 0,921 et 0,993 (S-7B, p. 7) ; 0,33 à 0,40 (S-7C, p. 7).
4. **Écarts trouvés entre la synthèse provisoire et les rapports**, corrigés dans la synthèse finale :
   - « rappel de 42,3 % à α = 0,10 » : le rapport C8 cite un taux de fausse alarme réalisé de 0,066 ; je donne ce dernier ;
   - « le sabotage réussi tombe de 77 % à 12 % » : la citation de C5 porte sur la réussite conjointe des deux objectifs ;
   - contre-indice de 2507.08794 sur HC6 : pages 7 et 8 (S-5B), non 7 à 9 ;
   - date du billet de l'institut britannique, « invérifiable » : lue depuis par S-2A (10 juillet 2025).
5. Ordre de grandeur « plus de cent cinquante pièces » (section 11 de la synthèse) : somme des comptes déclarés par
   les rapports (C5 : 38 ; dossier c8 : 21 ; S-2A : 17 ; S-2B : 15 ; C9 : 14 ; C3 : 10 ; B3 : 10 ; S-4A : 9 ; C8 : 9 ;
   C1, C2, S-3A : 7 chacun ; S-5A : 6 ; C6, S-7B, S-7C, S-7D : 5 chacun ; S-5B : 4 ; S-7A : 3 ; S-1, S-12 : 2 chacun),
   soit 201 avant retrait des doublons, **que je n'ai pas retirés**. Non opposable comme chiffre exact.
6. Non fait : `verifier-arbre` (il traverserait des chemins interdits à ce mandat) ; essais du dépôt ; relecture
   par un second lecteur. **Cette synthèse n'a pas été contre-lue.**

## 4. Choix de rédaction à connaître

- Échelle à quatre mots du mandat. Les rapports emploient aussi « occupée dans son principe », « occupée comme
  méthode », « contre-indice », « ne touche pas » ; j'ai rangé « dans son principe » sous « occupé en partie » et gardé
  le mot du rapport dans la colonne de sa lecture.
- Organisme : quand C7 et S-4A divergent, le verdict final est le plus dur des deux ; les deux lectures sont montrées.
- HC4 et H6 n'entrent pas proprement dans l'échelle ; le verdict est donné en deux membres, avec la divergence.
- Aucune revendication n'est tranchée ; les formulations « reste libre » décrivent les pièces, non l'énoncé à venir.

## 5. Divergences

Dix-huit divergences entre lecteurs, listées en section 10 de la synthèse. Les plus lourdes pour une décision : O2
(deux, trois composantes) et la forme de O12 (C7 contre S-4A) ; « synthetic » (B1 contre C2) ; H8 (S-7A, S-7B, S-3A) ;
H6 (S-2A).

## 6. Refus et interdits

Aucun refus d'un contrôle de permissions ni d'un classifieur pendant ce travail. Aucune écriture git, aucune dépense,
aucun appel de modèle, aucune valeur de clé lue. Aucun des chemins interdits par le mandat n'a été ouvert ; les
recherches ont porté sur des fichiers nommés, jamais sur l'arbre. Fichiers écrits : la synthèse, ce journal et leurs
compagnons `.sha256`, sous `docs/etat-de-l-art/` ; copies de lecture dans le dossier temporaire de la session.
