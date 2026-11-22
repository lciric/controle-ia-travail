# Attestation du contre-lecteur des pièces du monteur de l'oracle, cycle 1 du scellement 2, relance (v1)

- Classe C. Écrite le 2026-11-22 à 15:08 UTC par le contre-lecteur des pièces du monteur de l'oracle du cycle 1,
  relance (`session_01XJ6MgnTuQWL6zGoz1a9C2c`), session neuve ouverte par la mère
  (`session_01XJ6Mgr4LgbMsg5zLyRZCpG`) le 2026-11-22 à 15:04 UTC, branche
  `claude/scellement-2-oracle-cycle-1-contre-lecture-v1`.
- **Écrite avant toute lecture du coffre.** Sans contenu de famille ni d'oracle : des chemins, des empreintes et des
  engagements.
- Modèle : celui que désignent le mandat (ligne 11) et la ligne d'accès R-4929. La session rapporte, par
  `get_session`, un modèle configuré et un modèle servi conformes à cette désignation à l'heure de l'attestation.

## 1. Ce que cette session a fait avant d'écrire cette attestation

1. Mandat lu en entier : `docs/procedures/mandat-contre-lecteur-monteur-oracle-relance-cycle-1-v1.md`, branche
   `claude/scellement-2-oracle-cycle-1-v1`, commit `78c640af75fe33c864e8daf361cab7a8418b6c2e`. Empreinte recalculée
   avant lecture : `f9841f780f9d40f5eec238cb0388ead46451528d2be191ab902a89dbb5247d0a`, conforme à celle que la mère a
   transmise.
2. `CLAUDE.md` lu en entier sur `origin/main` (commit `e63495d687a3497e8ca215bff18576a6ef372245`, empreinte
   `dca4fb6cc7eb8f8cb97e66e2e7d2d4a7e7d288f7a39b446933b0e3db5e487c7f`), règle « Appels aux modèles de Google »
   comprise.
3. `git fetch origin main` fait à 15:05 UTC. Sur `origin/main`, dans `registres/decisions.md`, la ligne R-4929
   (ligne 5068 du fichier, datée 2026-11-22T15:04:19Z) porte « Accès au coffre du bras d'attaque » et mon identifiant
   de session. Elle a été trouvée par la recherche de mon seul identifiant : aucune autre ligne du registre n'a été
   affichée ni lue.
4. Hors coffre, lu aussi : `src/controle_ia/scellement.py` (lignes 1 à 80), pour l'outil de scellement ; `.gitignore`
   (30 premières lignes).
5. Du coffre : rien. Ni liste du dossier, ni nom de fichier autre que ceux du mandat, ni contenu. Seul geste : la
   création du dossier `contre-lecture-relance-v1/`, vide, pour y poser cette attestation.

## 2. Attestation

J'atteste que :

1. je n'ai conçu aucun moniteur — ni sonde, ni agrégateur, ni trait de texte, ni seuil, ni note de lentille, ni base,
   ni juge — et que je n'en concevrai aucun, ni pendant cette contre-lecture, ni après elle ;
2. je ne suis ni l'attaquant informé, ni l'auteur d'une famille, ni la contre-lectrice d'une famille, ni le juge des
   recettes, ni l'agent qui juge l'ancre des épreuves ;
3. je n'ai lu aucune sortie de la course « nouvelles attaques » ;
4. je n'ai lu aucune famille, ni aucune pièce d'un autre cycle que le cycle 1.

Portée : cette session est neuve. Elle ne porte la mémoire d'aucune autre session ; tout ce qu'elle a lu depuis son
ouverture est énuméré à la section 1.

## 3. Engagements pour la suite

1. Je recalcule l'empreinte de chaque pièce avant de la lire ; tout écart est un arrêt, signalé à la mère.
2. Je ne lis du coffre que le dossier du cycle 1 et les pièces de la famille du cycle 1 que cite le mandat ; jamais la
   pièce 2 de la famille (texte du mode) ; jamais la branche `claude/scellement-2-famille-reserve-cycle-2-v1` ni sa
   contre-lecture ; aucune pièce d'un autre cycle.
3. Je ne lis ni les lignes R-604 à R-610 de `registres/decisions.md`, ni `registres/etat.md`, ni les passations du
   programme, ni aucune sortie de la course « nouvelles attaques ».
4. Aucun envoi à un lecteur externe, aucun appel de modèle, aucune dépense, aucun épisode, aucun plan saboté, aucun
   code d'attaque. Je ne modifie aucune pièce du monteur : j'écris les miennes, en fichiers neufs, scellés.
5. Aucun contenu de famille ni d'oracle dans un message : des chemins et des empreintes seulement. L'attaquant
   informé ne reçoit rien de moi.
6. Je ne contourne aucun refus d'outil, de classifieur ou de garde : je le consigne et je le signale.
7. Je tiens un journal des accès (heure UTC, chemin, empreinte, motif), scellé à la fin.
