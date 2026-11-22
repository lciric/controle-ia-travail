# Mandat d'une session Fable 5.2 (abonnement) : conception et devis d'une banque sœur de tâches fraîches pour le banc fermé

- Mandat de classe C, écrit le 22 novembre 2026 par la session fille de l'attaquant informé, à la demande de la mère, qui crée la session. Il est relu pour le cloisonnement avant d'être servi.
- Fondement : le mot du directeur du programme « go aux trois », point B : une banque sœur d'au moins 58 tâches fraîches, selon N-049, forme (b) (`docs/decisions/decision-N-049-v1.md`, `8a5bf5e57e2bb447467388acb572e032d1a6a578a868db1b7304263a1c9d4460`).
- Langue : français, sans acronyme non développé. Lis d'abord `CLAUDE.md` en entier. Cette lecture n'autorise rien de la liste ci-dessous, qui prime.

## Pourquoi

- La répétition générale du banc fermé tire 50 tâches « de réserve, hors coffre, au format de la course », et la vérification de concordance avec le calage de G1 en demande 8. Il faut donc **au moins 58 tâches**.
- Les 96 tâches de T0.5 ont toutes servi : il n'en reste aucune de conforme (R-4723).
- N-049 (b) demande une banque sœur : même générateur, tâches neuves, construite d'avance par une instance qui n'a lu aucun score, lue une seule fois.

## Ce que tu ne lis jamais

- tout fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ;
- `brouillons/ii-b-saboteur-budget-v1/` ;
- tout chemin contenant `lot/compte-4-v1` ;
- la ligne R-2059 ;
- rien sous `archives-reponses-modeles/`, sous `donnees/`, ni aucune référence `donnees/*` : **les 96 tâches de T0.5 et leurs cibles cachées comprises** ;
- aucun résultat ni score de T0.5, de T0.6, de T0.7, de P3, de P3-bis, de 7a, de 7b, des étapes B et B bis, du barreau 5, de l'épreuve à vérité plantée ;
- aucune famille aveugle, aucune pièce du scellement 2, aucun moniteur ;
- le lot, les sorties et les agrégats du banc fermé.

**Tu n'as lu aucun score : c'est la condition de N-049 (b).** Si tu en rencontres un, arrête-toi et dis-le à la mère.

## Ce que tu lis (chemin, empreinte)

Recalcule chaque empreinte avant de lire ; un écart est un arrêt.

| Pièce | Chemin | Empreinte |
|---|---|---|
| Procédure d'extraction de T0.5, scellée : sources, énoncés, classifications, cibles semées, exclusions, invites | `docs/procedures/T0.5-extraction-v1.md` et son dossier `docs/procedures/T0.5-extraction-v1/` (les consignes seulement), `main` | `d23bd62fe1611b8737ccb38a404d96a41746158a7930bef0a065590bd072c26c` |
| Conception de l'environnement (a) | `brouillons/T0.5-conception-environnement-a-v0-brouillon1.md`, `main` | `cf2c508e61d75ae137606601fbc90c0b48478e4d7de82786c0f202436c1dc705` |
| N-049 | ci-dessus | ci-dessus |
| Répétition générale, brouillon 9 : champ R-4 et « Tirage des tâches » | `prereg/repetition-generale-banc-ferme-v1-brouillon9.md`, branche `claude/prereg-course-banc-ferme-v1` | `a58cab35cf4914a4e78decec95f296d824626752f4028b347ca5741d49f76e08` |
| Course, brouillon 17 : D2 (la tâche) et « Vérification de concordance avec le calage » | `docs/notes/attaquant-informe-v1/course-brouillon17-v1/course-banc-ferme-v1-brouillon17.md`, branche `claude/loving-lamport-7ol5ws` | `cf5d35d8472137d30defedb2a61b375037d558e3937e4371cb5d8822a507a881` |
| Harnais : forme d'un épisode | `src/controle_ia/harnais/episode.py`, `main` | à relever |

## Ce que tu écris, dans `docs/notes/banque-soeur-taches-banc-ferme-v1/` sur ta branche

### 1. La conception de la banque

Écris-la en classe A : elle fixe ce que la répétition tirera.

- **Le générateur.** Il est le même que celui de T0.5, selon la procédure scellée. Les sources sont neuves, disjointes des 96 par leurs identifiants.
  - Les identifiants des 96 sont dans le coffre : tu ne les lis pas.
  - Tu écris le programme de disjonction (classe B). Il ne rend qu'une issue, « disjointe » ou « non disjointe », et le nombre de recouvrements, sans aucun identifiant. Il est exécuté par une session que la mère désigne et qui a l'accès.
  - Le recouvrement se juge par les identifiants publics des sources, et la conception dit lesquels.
- **Le nombre de tâches.** Au moins 58, avec une marge pour les exclusions de la procédure, comme `theory_only`. Le nombre visé et la règle d'arrêt sont fixés d'avance.
- **Le format.** Celui de la course et du harnais, cibles cachées comprises, extraites et contre-vérifiées comme pour T0.5.
- **Qui construit.** Une instance qui n'a lu aucun score. La conception dit lesquelles conviennent, sans les désigner.
- **Le rangement.** Énoncés et cibles cachées vont dans un dossier fermé, à règle d'ouverture écrite. Seule la liste des identifiants, avec son empreinte, sort pour le champ R-4. Qui peut ouvrir quoi, et quand : le dire.
- **Les épreuves avant usage.**
  - Contrôles de forme par programme.
  - Disjonction avec les 96.
  - Le tirage de la répétition est rejoué à blanc sur une liste factice.
  - Chaque épreuve se fait sur un cas sain et sur un artefact (R5).
- **Ce qui reste inchangé** : la banque v6 scellée et la famille tenue à l'écart (N-049, point 3). Aucune tâche de cette banque ne sert un organisme.

### 2. Le devis de sa construction

- Les appels de l'extracteur et du contre-vérificateur, par tâche.
- Les jetons d'entrée et de sortie et le tarif de chaque modèle, à relever le jour du devis et jamais à supposer.
- Les tentatives et les exclusions attendues.
- L'attendu, le pire cas et le délai en heures.
- Un programme de calcul de classe B, qui rend la table.
- Le plafond à proposer, en euros et en dollars.

### 3. Les nœuds pour le directeur

Format de décision ; par exemple si la procédure de T0.5 ne peut pas être suivie à la lettre.

## Règles

- **Aucune dépense** : tu ne génères aucune tâche et n'appelles aucun fournisseur. La construction attend le devis et le mot du directeur.
- Chaque fichier est scellé (`PYTHONPATH=src python -m controle_ia.scellement sceller`), et on n'écrase jamais (R12).
- Tu ne pousses que sur ta branche.
- Un rapport court va à la mère après chaque pièce, par `registres/essaim/vers-mere/`, avec chemin, empreinte et nœuds. Une passation scellée clôt la session.
- La contre-lecture, par un autre modèle, puis la vérification des corrections par le même contre-lecteur, viennent ensuite, à la demande de la mère.
