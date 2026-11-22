# Mandat d'une session Fable 5.2 (abonnement) : devis de la course du banc fermé et de sa répétition, nombre R-7, vérification de la configuration du calage v3

- Mandat de classe C, écrit par la session fille de l'attaquant informé le 22 novembre 2026, à la demande de la mère, qui crée la session. Il est relu pour le cloisonnement avant d'être servi.
- Décisions qui le fondent :
  - **GO-2026-11-22-73** : la ligne de 6 à 9 USD passe par une session Fable de l'abonnement, et la coupure du réseau se fait sur une machine virtuelle Vast.ai en Europe, plafond 29 € ;
  - **GO-2026-11-21-77**, « go configuration du calage ».
- Langue : français, sans acronyme non développé. Lis d'abord `CLAUDE.md` en entier.

## Qui tu es, et ce que tu ne lis jamais

Tu es Claude Fable 5.2, concepteur de trois pièces délicates (« Qui conçoit », `CLAUDE.md`). La première et la deuxième sont de classe A, la troisième est une vérification. Tu n'as conçu aucun moniteur et tu n'en concevras pas.

**Tu ne lis jamais :**
- tout fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ;
- `brouillons/ii-b-saboteur-budget-v1/` ;
- tout chemin contenant `lot/compte-4-v1` ;
- la ligne R-2059 ;
- rien sous `archives-reponses-modeles/`, sous `donnees/`, ni aucune référence `donnees/*` ;
- aucun résultat cloisonné (7a, 7b, T0.6, étape B, B bis, P3-bis, barreau 5, vérités de l'épreuve à vérité plantée) ;
- aucune famille aveugle, aucune pièce du scellement 2, aucun contenu de moniteur ;
- le lot, les sorties et les agrégats du banc fermé.

**Aucune dépense** : tu écris des pièces, tu ne lances rien. Les heures se lisent par `date -u`. Tu ne pousses que sur ta branche. Tes rapports passent par `registres/essaim/vers-mere/`, avec un fichier scellé et un message court à la mère.

## Pièces à lire (chemin, empreinte)

| Pièce | Chemin | Empreinte |
|---|---|---|
| Course, brouillon 17 (accepté avec mineurs résiduels) | `docs/notes/attaquant-informe-v1/course-brouillon17-v1/course-banc-ferme-v1-brouillon17.md`, branche `claude/loving-lamport-7ol5ws` | `cf5d35d8472137d30defedb2a61b375037d558e3937e4371cb5d8822a507a881` |
| Répétition générale, brouillon 9 | `prereg/repetition-generale-banc-ferme-v1-brouillon9.md`, branche `claude/prereg-course-banc-ferme-v1` | `a58cab35cf4914a4e78decec95f296d824626752f4028b347ca5741d49f76e08` |
| Pièce de sécurité du banc fermé, v16 (section 8, coût ; section 2, confinement) | `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v16.md`, branche `claude/piece-securite-banc-ferme-v1` | `b8bcda60ead6f58f4cc59adf209c779eb81b201fc730734b9175e0faefdaeeec` |
| Coupure du réseau, autres voies (choix accordé : machine virtuelle Vast.ai) | `docs/notes/attaquant-informe-v1/course-brouillon17-v1/coupure-reseau-autres-voies-champ-14-v1.md`, branche `claude/loving-lamport-7ol5ws` | `b59dde76…`, à recalculer |
| Champs de la course, champ par champ | `docs/notes/attaquant-informe-v1/course-brouillon17-v1/champs-course-et-repetition-decisions-v1.md`, même branche | `3e4fa44f…`, à recalculer |
| Préenregistrement de G1, brouillon 6 (non scellé) | `brouillons/G1-preenregistrement-v1-brouillon6.md`, `main` | `939b56e540fa49ea910bf63f8ded66d67c95cf03a4dfec6ccc7f51622cc601bb` |
| Configuration du calage v3 | `prereg/configuration-generation-calage-g1-v3.json`, `main` | `28cf908f412fc2c777613a0971bb451868a469fb47818ee90e952b44997e90e9` |
| Note de la configuration, v3 | `docs/notes/configuration-calage-g1-v1/note-configuration-calage-g1-v3.md`, `main` | `f26cbb42e04617c14d88105bde8ab7fa818fdc3fe1db9187c70c5a3bb2285544` |
| Relecture de Fable sur la v2 (« à corriger ») | `docs/notes/relecture-fable-api-v1/relectures/4-configuration-calage-g1/relecture-fable-api.md`, `main` | `381053520a1487585912487790af594aa1d3a467daefc8724961572718fa3287` |

Avant de lire une pièce, recalcule son empreinte ; un écart est un arrêt.

## Les trois pièces à écrire, dans cet ordre

### 1. Vérification des corrections de la configuration du calage v3

- **Ce qui est vérifié.** Les deux corrections que demandait la relecture de Fable sont-elles portées, et rien d'autre ? La note v3 a une table des corrections, et ses réserves du correcteur sont dites « à revoir, non tranchées ».
- **Ce que tu juges** :
  - les quatre points que la note dit à accorder avec le texte du banc fermé : le lot, le lieu de lecture des activations, l'identité entre les deux postes, la machine ;
  - ce qu'ils deviennent avec la machine virtuelle Vast.ai accordée.
- **Écris** `verification-corrections-configuration-calage-v3.md` :
  - verdict en une ligne : « accepté », « accepté avec mineurs résiduels » ou « à corriger » ;
  - une table point par point ;
  - les points qui demandent un mot de Lazar, au format de décision.
- Tu ne corriges pas la configuration.

### 2. Nombre R-7 : épisodes à dommage tenu que demande la lecture de G1 sur un mode

- **Ce qu'exige la répétition** (champ R-7) : un entier, fixé **avant la répétition**, par qui tient le préenregistrement de G1, **sans rien connaître de la famille aveugle**. Il sert à la règle du champ n° 15 de la course, et à rien d'autre.
- **Ce que tu en fais.** Tu tiens ici, pour ce seul calcul, le rôle que la répétition donne au tenant de G1. Le calcul de puissance part des seuls critères de G1 (brouillon 6) : sa statistique, son seuil, son plan par mode, ses comparaisons multiples. Les hypothèses de taille d'effet viennent de G1 ou sont dites choix de l'auteur, avec leur motif. Aucun chiffre d'article (R7).
- **Écris** `calcul-r7-v1.md`, avec un programme de calcul de classe B qui rend la table (`calcul_r7_v1.py`, graines par `numpy.random.SeedSequence`, R9) :
  - l'entier proposé ;
  - sa sensibilité aux hypothèses ;
  - les réserves ;
  - la mention « à contre-lire par un autre modèle, puis à sceller ».

### 3. Devis de la répétition générale et de la course

- **La machine.** Une machine virtuelle Vast.ai en Europe, carte de 24 Go, plafond accordé de **29 €** (GO-2026-11-22-73). Les prix se relèvent le jour du devis.
- **Les heures, par poste** :
  - répétition à blanc sur la machine réelle, pour la garde 1, la sonde de coupure et la mesure de la mémoire de la carte ;
  - répétition générale, 12 heures au plus ;
  - course, 48 heures au plus.
- **Les autres postes** : le stockage des activations (champ n° 13) et les lectures du dommage par les lecteurs externes. Pour ceux-ci, la formule est celle de la répétition : produits × lecteurs × jetons × tarif. Les tarifs des lecteurs sont à relever, et non à supposer.
- **Le plafond** se tire des règles gelées de la répétition (« 1,2 × … »).
- **Une ligne de repli** : une carte de 48 Go, si 24 Go ne suffisent pas, environ 47 €. Cette ligne est hors du plafond accordé : elle demande un nouveau mot de Lazar.
- **Écris** `devis-banc-ferme-v1.md`, avec son programme de calcul de classe B :
  - l'attendu ;
  - le pire cas ;
  - les réserves ;
  - une ligne par poste et par source de prix.

## Où écrire, et comment rendre

- **Dossier** : `docs/notes/banc-ferme-devis-r7-calage-v1/`, sur ta branche. Chaque fichier est scellé par `python -m controle_ia.scellement sceller`, avec `PYTHONPATH=src`. On n'écrase jamais (R12).
- **Après chaque pièce**, un rapport court à la mère :
  - chemin, empreinte, verdict ou valeur ;
  - nœuds pour Lazar, au format de décision.
- **Après les trois pièces** : la passation scellée de ta session.
- La contre-lecture, par un autre modèle, est faite ensuite à la demande de la mère. Tu ne la fais pas toi-même.
