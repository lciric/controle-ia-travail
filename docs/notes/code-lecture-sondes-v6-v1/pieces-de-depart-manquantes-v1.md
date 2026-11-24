# Pièces de départ qui manquent encore pour lancer la lecture des sondes du barreau 8 (code de la lecture v6)

Écrite le 2026-11-24 par le développeur du côté des moniteurs (session fille de la mère `session_01Qi7Gr3Ggccg85kjmP654WC`). Pièce de travail (classe C). Constats faits **par les noms et l'existence des fichiers seulement** : aucune pièce de la course n'a été ouverte. Les conditions sont celles que le code contrôle, dans l'ordre où il les contrôle (notice `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-lecture-sondes-v7.md`, « Conditions de départ »).

## Déjà en place (constaté)

- Lignes `SCELLEMENT-SONDES-IIB`, `SCELLEMENT-ADDITIF-1-SONDES-IIB` (2026-11-24T04:21:08Z), `SCELLEMENT-ADDITIF-2-SONDES-IIB` (2026-11-24T10:34:26Z), `CODE-PASSE-IIB` (11:31:45Z) et `LIVRAISON-PASSE-IIB` (13:08:00Z) au registre propre `registres/sondes-iib-v1.md` ; les deux dernières sont bien postérieures à la ligne de l'additif 2.
- Table neuve des constantes et pièces de la condition D-14 (contrôlées par le code sur le dépôt réel : présentes, à leurs empreintes, « report »).
- Pièce d'attestation de l'ordre (D-6 lue avec M-3), à l'empreinte `8f6b5025…e76a` ; acceptée par le code (trois « non dit » O-3, O-5, O-6).
- Verdict du témoin positif planté et sa pièce d'issue (D-9) : présents par leur nom ; leurs empreintes sont contrôlées par le code au lancement.

## Ce qui manque, et qui le produit

| # | pièce ou ligne | condition | qui la produit | quand |
|---|---|---|---|---|
| 1 | **Identifiant de l'accord de lecture des sondes**, et sa ligne au registre des accords `registres/go.md`, première cellule = l'identifiant seul | D-4 | mot de Lazar ; la session mère l'inscrit et me donne l'identifiant (question posée le 2026-11-24) | avant le bordereau du code |
| 2 | **Bordereau du code de la lecture** (neuf clés) et **ligne `CODE-LECTURE-SONDES-IIB`**, strictement après la ligne de l'additif 2 | M-5 ; liste d'arrêt, lignes 5, 23, 30 | bordereau : le développeur (commande `bordereau-code`, après « conforme » de la contre-lecture et l'identifiant de l'accord) ; ligne : la session mère | après la contre-lecture |
| 3 | **Mandats scellés du lecteur et du juge** : chacun cite l'empreinte de la liste des exclus et celle du registre « qui a lu quoi » ; celui du lecteur cite en plus l'empreinte de l'attestation de l'ordre (`8f6b5025…`), celle de l'attestation de la course et de l'oracle (pièce 6), et celle de la référence boîte noire si elle existe. Les projets de mandats existants (brouillon 2, dans `docs/notes/barreau8-cote-moniteurs-sorties-v1/`) précèdent les deux additifs : à compléter | D-5 ; D-6 ; D-15 | session mère | après la pièce 6 |
| 4 | **Aires minimales détectables** : sortie de la commande `puissance`, scellée, committée | D-10 | côté moniteurs (conductrice ou lecteur), sur processeur ; 1,6 à 4,8 heures estimées, budget 12 heures ; la commande exige déjà la ligne `CODE-LECTURE-SONDES-IIB` | après la pièce 2 |
| 5 | **Extrait des seuls états** `docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json` et son compagnon (13 états à la version 6), et **ligne `ETATS-COURSE-IIB`** | D-12 ; RP-10 ; liste d'arrêt, ligne 3 | extrait : le programme du côté exposé, après les lectures du dommage et de la diffusion et après la pièce 6 ; ligne : la session mère | ordre (v) de l'additif 2 |
| 6 | **Pièce d'attestation de la course et de l'oracle** `docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-course-et-oracle-additif-1-v1.json`, scellée, forme fermée, « conforme » | D-15 ; liste d'arrêt, ligne 22 | un agent du côté exposé | après les lectures du dommage et de la diffusion, avant la lecture des sondes |
| 7 | **Heure de remise de la note d'interface version 7**, attestée, passée par `--remise-note-v7` | RP-14, ligne (vi) | session mère | au lancement |
| 8 | Référence boîte noire `docs/notes/barreau8-cote-moniteurs-entrees-v1/reference-boite-noire-course-lue-additif-1-v1.json` (**facultative** : absente, la lecture descriptive LD-4 est « non jouée », sans effet) | LD-4 | côté exposé, sur texte scellé avant le calcul des scores | avant la lecture, si elle est faite |

## Risques à vérifier par la session mère, par les noms seuls

- **Dossier de la livraison.** La garde r2 exige que le dossier du bordereau de livraison ne contienne que les fichiers de la livraison et leurs compagnons. La ligne `LIVRAISON-PASSE-IIB` cite un chemin sous `versement/` : si ce dossier porte aussi un inventaire, un journal ou un autre fichier, la réception refusera (`[r2]`). Je n'ai rien ouvert sous `versement/`.
- **Arbre de travail propre.** Les commandes `puissance` et `lecture` écrivent un manifeste et refusent un arbre git non propre : livraison, extrait, registre, bordereaux et sortie de la recette doivent être committés (ou ignorés par git) avant la lecture.
- **Lignes « postérieures ».** Toute ligne comptée doit être strictement postérieure, par le rang et par l'heure, à la ligne de l'additif 2 ; une ligne antérieure ne compte pas et est écrite telle dans la sortie.
