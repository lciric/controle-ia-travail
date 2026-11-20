# Notice — lanceur de l'étape de discrétion du bras A, côté moniteurs (demande 18), et confirmation sur les positions du juge — v1

**Pièce habilitée, à ne pas transmettre à une session non habilitée.** Ce qui est transmissible est dans `reponses-sans-interne-demandes-18-19-24a-v1.md`, même dossier.

Écrit par le développeur habilité côté moniteurs (agent neuf, mandat v3 `registres/bras-a-habilite/mandat-developpeur-habilite-bras-a-v3.md`, `374af2488f6804c0dcf94218a2993bd42710116305cd5ae5877c0ac22e982dbc`, et les sections qu'il désigne des mandats v1 et v2), le 20 novembre 2026, sous GO-2026-11-20-21. Classe B : à contre-lire par un autre modèle, puis vérification des corrections par le même. Copie de travail `/home/user/bras-a-habilite`, tête `f5d0e9c92`. Ni commit ni poussée.

Pièces de la relance lues, à leur empreinte vérifiée : les demandes v8 (`ba81227fcea1b6419fad012f83711e61a54c7c01dce6a34d3319266d4aaaf579`), l'extrait du lanceur v3 (`5d2a48c0f9b6b8a36b20cc466508c44fe1c2aad84a17b98cfb1190f85c631bed`) et le module d'entrée v2 (`cb668bb95a9c0a37b1a08a91f304e1b756ef5b0ebddc0a3f193be0692e0bfa10`), par `git show` sur `origin/claude/pensive-bardeen-1fv7hw`. **Rien d'autre de la relance n'a été ouvert** : ni le texte du préenregistrement, ni aucun module `graines_bras_a_v*`, ni passation. Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`. Aucun poids chargé, aucune dépense, aucun réseau hors `git show` local. Aucun outil refusé.

## 1. Fichiers

| rôle | chemin | empreinte |
|---|---|---|
| lanceur, version 1 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite_lanceur/lanceur_discretion_v1.py` | `96ac8d8b8370967e7e87bce26681008dffc776321cf65c217923b7e356d57e73` |
| paquet du lanceur | `src/controle_ia/organismes_discrets/bras_a_v2_habilite_lanceur/__init__.py` | `0cd2928442dea2035ee5c64252d5853d7c3b0cd117c4ae527e0421d1ad16088c` |
| essais du lanceur | `tests/test_bras_a_v2_habilite_lanceur_discretion_v1.py` | `0bef30a50010ee67e13840b9b91201519741f0cde5f43d6b592fedd4e66abdba` |
| préparation des lectures, version 3 (aucune position tirée) | `src/controle_ia/organismes_discrets/bras_a_v2_habilite_preparation/preparation_des_lectures_v3.py` | `c0021298c21d027a713b1947d2668ac928f2a856b1a696686dd35b83a9515c45` |
| ses essais | `tests/test_bras_a_v2_habilite_preparation_des_lectures_v3.py` | `70badfe1d058b72ab3f8450a3b9271fe97a7ce14a009334200f2e7858bd8a877` |
| module des autres moniteurs, version 11 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v11.py` | `e1130dadd1ee7f7ac1c8c19ab3edf69ca837f0fc016d681f0ef3e6956a927fda` |
| ses essais | `tests/test_bras_a_v2_habilite_autres_moniteurs_v11.py` | `92711976e9ee949b08719b791cafc53932763ab96a04b6c01d34b0068cc3c776` |
| gabarit de la configuration du lanceur (non jouable : valeurs à fixer nulles) | `docs/notes/bras-a-moniteurs-v1/config-lanceur-discretion-bras-a-gabarit-v1.json` | `0da610c43edf15eb0b28c361882ea0536dc11bedfcc4cc35cf1254376e062a4b` |
| épreuve par retrait : script et relevé | `docs/notes/bras-a-moniteurs-v1/epreuve-par-retrait-lanceur-discretion-v1/` | script `epreuve_retraits_lanceur_v1.py`, `f439b9784c8c55757af7986c125ff831f4008671aaeead975600a363a437e01c` ; première passe `releve-retraits-lanceur-premiere-passe-v1.md`, `9f792ee86bd3df86fd2c5d617721d90bcb0bea9c31d17d00ee5e75d81acf1ef0` ; seconde passe `releve-retraits-lanceur-seconde-passe-v1.md`, `27532165a59154d72f2f5d360e6ca569b119e8efc6bcd67bf2aaef8b0314ba52` |

Essais ciblés (`PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider <fichier>`), dernières lignes : lanceur `18 passed` (les trois fichiers ensemble : `30 passed in 34.05s`) ; préparation v3 `8 passed` ; module v11 `4 passed`.

## 2. Confirmation demandée par la relance : la préparation ne tire-t-elle plus de positions pour le juge ?

**Non, pas dans la version 2**, que cite la version 10 du module des autres moniteurs : `src/controle_ia/organismes_discrets/bras_a_v2_habilite_preparation/preparation_des_lectures_v2.py` (`6dfd2bfc…`), **lignes 89 et 90** :

```
    if moniteur == JUGE:
        positions = {t: set(ml.positions_du_juge_pour(entropie, t, N_EPISODES, T)) for t in taches}
```

(32 positions sur 80 par tâche ; les autres comptées « hors du sous-échantillon »). La version 1 fait de même (lignes 86 et 87).

**Oui dans la version 3**, écrite ici pour que le lanceur suive l'étape 3 de l'extrait : la branche du juge et le compte « hors du sous-échantillon » sont retirés ; les deux moniteurs ont une demande par action lue, mêmes messages, chacun ses graines (clé du moniteur, sans la condition). Rien d'autre ne change. Comme la version 10 inscrit l'empreinte de la préparation v2 dans `PROGRAMMES_DE_PRODUCTION` et refuse tout manifeste de production qui en porte une autre, une **version 11** du module des autres moniteurs ne change que cette empreinte (différentiel de 26 lignes, `attestation-autres-moniteurs-v7-a-v10-v1/differentiel-autres-moniteurs-v10-a-v11.diff`). **Conséquence pour la relance** : la livraison sera produite par la version 11 ; c'est son empreinte, `e1130dad…`, que porte `piece_source.sha256` et que la configuration de l'analyse doit inscrire, à la place de celle de la version 10. Le juge lit alors 6 400 actions au plus : la ligne « 6 400 » du chiffrage déjà rendu s'applique (4,9 à 11,5 heures de carte pour la lecture seule).

## 3. Ce que fait le lanceur

Trois sous-commandes, une configuration scellée (compagnon vérifié, clés fermées, aucune valeur nulle au premier niveau) :

| sous-commande | ce qu'elle fait |
|---|---|
| `extraire` | extraction des six conditions lues (`extraction_base_v2`), écrite sous le dossier d'extraction, puis la ligne `CONFIG-BRAS-A-V2` qui désigne la configuration écrite (refus si la ligne existe déjà) |
| `base` | la base « mots et coût » par son lanceur inscrit, `scripts/lancer_mots_et_cout_bras_a_v2.sh --mode reel --racine-entrees <extraction> --registre <registre>` ; code de sortie et lignes imprimées (chemins et empreintes) consignés |
| `discretion` | les six étapes de l'extrait, en une seule exécution (table ci-dessous) |
| `relever-fins` | jetons de fin du moniteur boîte noire à sa révision, par la configuration de génération et le tokeniseur seuls (aucun poids), pour remplir la configuration avant son scellement |

| étape de l'extrait | dans le lanceur |
|---|---|
| 1. garde de production | `autres_moniteurs_v11.exiger_production_permise` en tête, puis de nouveau juste avant le premier appel de chaque moniteur (`produire`) ; refus aussi si une ligne d'ouverture d'un des cinq moniteurs existe |
| 2. table | entropie propre `numpy.random.SeedSequence().entropy` ; `admettre_l_entropie_propre_de_la_table_des_identifiants` appelée **avant** le tirage, avec les sept arguments de l'extrait, son dictionnaire consigné tel quel au manifeste du lanceur ; table tirée par `tirer_la_table_opaque(clés, entropie)`, contrôle que l'entropie écrite est celle admise ; fichier scellé dans le dossier à part ; engagement inscrit `ENGAGEMENT-TABLE-OPAQUE-BRAS-A`, daté, avant toute production |
| 3. préparation | `preparation_des_lectures_v3` : seule à lire les textes et la table ; aucune position tirée ; demandes à trois champs dans le dossier des demandes, bilans dans le dossier à part |
| 4. production | `produire(moniteur, demandes, consigne, engagement, …)` : ne reçoit rien d'autre de la préparation ; lectures par morceaux d'un lot, dans l'ordre des identifiants, chaque morceau scellé dès sa production ; manifeste de production de la v11 (empreintes canonique des scores, de la table engagée, des deux programmes de production) posé et inscrit `MANIFESTE-PRODUCTION-BRAS-A-<MONITEUR>` dès son écriture |
| 5. ouvertures | `inscrire_ouverture` pour les cinq, dans l'ordre lexical, surface, boîte noire, agrégateur, juge ; l'empreinte des scores est celle que la v11 lit au manifeste de production |
| 6. lecture commune | `lire_les_cinq` de la v11, entropie de la configuration du bras, échange par paire, forme « rang » ; sortie et rangs écrits sous les provisoires des dossiers de la sortie et des rangs, puis posés |

**Quatre conditions de l'extrait** : (1) aucun score avant la garde, éprouvée cas sain et artefact ; (2) morceaux scellés dès leur production, empreinte canonique au manifeste scellé ; (3) personne n'ouvre les scores avant la ligne : le lanceur ne fait que les concaténer pour le manifeste, et ne remet aucun fichier à un agent ; (4) les ouvertures précèdent la lecture commune, qui les exige.

**Écriture.** Tout fichier scellé par le lanceur ou par les modules qu'il appelle s'écrit sous `<dossier>/.provisoire/<exécution>/`, y est scellé, puis passe à son nom, compagnon d'abord. Un reste provisoire n'est ni lu ni écrasé. Rien n'est supprimé. Les dossiers du lanceur sont deux à deux disjoints.

**Reprise après une panne de transport.** Les morceaux déjà scellés ne sont pas redemandés ; un relevé scellé (morceaux attendus, morceaux déjà scellés, numéro de la reprise) est inscrit `REPRISE-PRODUCTION-BRAS-A`. La table n'est pas retirée (ligne d'engagement relue, fichier à son empreinte) ; une préparation faite est reprise telle quelle. Aucune reprise après une ligne d'ouverture : arrêt et nœud.

**Manifeste du lanceur** : commande, empreinte du lanceur, de la configuration et de chaque module appelé, heure de chaque étape, empreinte de chaque fichier écrit, lignes inscrites, reprises, dictionnaire de l'accord, rendu de la base, motif d'arrêt ; scellé à la fin de chaque sous-commande, arrêt compris (sauf arrêt brutal du processus).

## 4. Ce qui ne peut pas s'écrire sans en savoir plus, et les écarts à l'extrait, pour la mère et le contre-lecteur

1. **« Il enchaîne l'extraction pour la base, la base, … » en une exécution : ne peut pas s'écrire sans en savoir plus.** La base, en mode réel, exige un arbre de dépôt propre et la ligne `CONFIG-BRAS-A-V2` déjà versée, datée avant elle ; la ligne `ISSUE-MOTS-ET-COUT-BRAS-A`, qu'exige l'étape 1, s'inscrit après la lecture de la base (et, si l'audit de la base se déclenche, après une relecture). D'où trois sous-commandes, avec, entre elles, des gestes de la session principale : verser l'extraction et la ligne, puis lire la base et inscrire son issue. L'« une seule exécution » de l'extrait est tenue pour la sous-commande `discretion`.
2. **Qui inscrit `CONFIG-BRAS-A-V2`** : ici, `extraire`, qui y désigne la configuration à six clés qu'elle écrit. Si la relance inscrit cette clé pour la configuration du bras, `extraire` refuse : à trancher.
3. **La table se tire sur les clés des actions** (les 6 400 des cinq conditions lues) : l'étape 2 lit donc les clés du fichier des textes, et non le seul accord, comme sa ligne de l'extrait le dit.
4. **Énoncés des tâches** : pris au champ `questions` d'un fichier des tâches scellé que la configuration nomme. Que ce champ soit exactement l'énoncé que voit l'agent est une hypothèse à vérifier par le contre-lecteur.
5. **Séparation de la préparation et de la production** : dans le même processus, par les arguments (la fonction de production ne reçoit que le chemin des demandes, la consigne, l'engagement, le registre, les réglages et le chargeur). Pas de processus à part.
6. **Fenêtres étroites sans réparation automatique** : une panne entre l'écriture d'un fichier par un module sous le provisoire et sa pose, ou entre la pose de la table et l'inscription de l'engagement, donne un refus à la relance suivante, jamais une suppression : nœud pour la mère.
7. **Graines des lectures** : dérivées par la préparation de l'entropie de la configuration du bras, une par moniteur et par position ; aucun tirage par le module d'entrée, aucun autre tirage que la table.
8. **Chemin réel non éprouvé** : `chargeur_reel` et `relever_fins` (chargement sur la carte, jetons de fin relevés et comparés) ne sont éprouvés que par des doublures ; aucun poids chargé ici. Le module d'entrée est absent de cette branche : les essais emploient une doublure à ses noms ; le lanceur vérifie son empreinte (configuration) et que le module importé est le fichier de la racine.
9. **Dossiers proposés sous `donnees/`** (ignoré par git) : la base refuse un arbre où traîneraient des fichiers non suivis ; sous `donnees/`, les sorties ne la gênent pas ; leur versement se fait par `git add -f`, comme pour les autres jeux de données.
10. **Le module de graines que le module d'entrée importe** n'est pas cité par empreinte dans la configuration : je ne l'ouvre pas, et l'extrait ne le demande pas. L'empreinte du module d'entrée couvre son nom, non son contenu. À faire citer par la session principale, si elle le veut, en ajoutant une clé au lanceur (version neuve).
11. **Clés de registre neuves** : `ENGAGEMENT-TABLE-OPAQUE-BRAS-A`, `MANIFESTE-PRODUCTION-BRAS-A-MONITEUR-BOITE-NOIRE`, `MANIFESTE-PRODUCTION-BRAS-A-JUGE`, `REPRISE-PRODUCTION-BRAS-A`, au format `| clé | date | chemin | sha256 |`.

## 5. Réponses aux sections 5 et 6 de l'extrait

- **Dossier du fichier des rangs** : celui que fixe la clé `dossiers.rangs` de la configuration ; le gabarit propose `donnees/bras-a-v2-discretion/rangs-par-unite`, à lui seul, disjoint de la sortie (`donnees/bras-a-v2-discretion/sortie-lecture-commune`) et de tous les autres dossiers du lanceur (garde). Aucun programme du lanceur ne le parcourt ni n'ouvre le fichier après son écriture : il est écrit par la lecture commune, puis renommé (compagnon d'abord), sans être lu.
- **Programmes qui nomment le fichier des rangs**, sous `src` et `scripts` : **5** — les versions 8, 9, 10 et 11 du module des autres moniteurs (constante `FICHIER_RANGS`) et le lanceur (par cette constante). Tous sous des dossiers dont le nom commence par `bras_a_v2_habilite`. Si la garde de l'analyse compare les noms de dossiers à l'identique, ajouter `bras_a_v2_habilite_lanceur` (et `bras_a_v2_habilite_preparation`, déjà signalé).
- **Garde d'équivalence du jeu d'épisodes** : le lanceur ne joue aucun épisode de l'agent ; elle ne le concerne pas.
- **Pièce qui rejoue un lot** : non écrite (non commandée).

## 6. Reste à fixer dans la configuration avant son scellement

Texte scellé (empreinte) ; registre des accords figé (chemin, empreinte, commit) ; rejeu, configuration du bras, fichier des tâches (chemins, empreintes) ; statistique de l'agrégateur ; les cinq réglages de la lecture ; jetons de fin du moniteur boîte noire (`relever-fins`). Les valeurs de chargement du gabarit sont celles recommandées par la note `a-citer-au-texte-moniteurs-a-modele-de-langue-v1.md` et son erratum (date de l'agent, `sdpa`, `bfloat16`) : à confirmer.

## 7. Essais et retraits

- Essais du lanceur (18) : chaîne entière sur un dépôt d'essai (extraction de 7 680 lignes, puis les six étapes, avec doublures du module d'entrée, du chargeur et de la lecture) ; reprise après une panne de transport au milieu du juge (deux morceaux scellés, reprise des seuls restants, table non retirée, reprise inscrite) ; garde de production juste avant le premier appel (sain et artefact) ; gardes d'ordre, de doublon et de morceau de la production ; gardes d'état (entropie, bilan, engagement en double ou d'un autre fichier, sortie peuplée, extraction d'une autre configuration du bras, sorties d'extraction présentes) ; aucune reprise après une ouverture ; configuration (vingt-quatre artefacts) ; dossiers disjoints ; modules à leur empreinte ; comptes de positions du module d'entrée ; pose provisoire ; morceaux ; registre ; base par son lanceur ; refus du mode jouet en ligne de commande ; garde statique (aucun module de graines, importations internes fermées).
- **Épreuve par retrait** : 46 retraits listés (45 gardes du lanceur, la garde neuve du bilan de la préparation v3), joués un à un, essais ciblés après chaque retrait. Première passe : 44 mordent ; deux ne mordaient pas (« dossiers » de la configuration : aucun artefact ; « production déjà inscrite » : le refus venait plus tard, du registre, avec le même motif). Deux essais renforcés (artefacts de dossiers manquant ou de trop ; aucun appel du chargeur ni de la lecture avant ce refus). Seconde passe, sur tout, après ces corrections et le réglage paresseux du déterminisme de la carte : **46 mordent sur 46**. Fichiers remis à l'identique, empreintes vérifiées (celles de la partie 1).
- Écart de méthode : une modification du script de l'épreuve n'a pas pris (texte non unique) ; la seconde passe a donc rejoué les 46 retraits au lieu des deux visés. Aucun refus d'outil.
