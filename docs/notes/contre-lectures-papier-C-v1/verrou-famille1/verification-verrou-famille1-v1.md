# Vérification du verrou « famille 1 sans conséquence conditionnée au verdict » — v1

- Date : 2026-10-20 (UTC). Vérificateur neuf : n'a écrit ni le préenregistrement, ni la configuration, ni aucune contre-lecture ; aucun sous-agent, aucune dépense.
- Question unique : le verrou que la décision R-307 (`registres/decisions.md`, cité par la demande, non relu ici) veut ajouter au brouillon 6 est-il déjà vrai ?
- **Verdict : verrou faux pour les indices 9, 12, 14, 15, 16 de la famille 1** (15 et 16 sont faux même à la lecture la plus étroite : condition introduite par « si » explicite). Indices 6 et 11 : limites, non comptés. Les 16 témoins sont propres.

## Pièces lues

| pièce | empreinte sha256 | contrôle |
|---|---|---|
| `brouillons/papier-C-config-v1-brouillon2.json` (37 058 octets) | `77252564163e25445421e932ff46b42634487ace242ac1861bb9f61586f07efb` | conforme au compagnon `papier-C-config-v1-brouillon2.json.sha256` |
| `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` (contexte seulement : Métrique ; Plan d'analyse, sections 0 à 2) | `9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969` | conforme à son compagnon `.sha256` |

Rien d'autre n'a été lu.

## Chemins JSON

- **Famille 1** : `$.vivier.flatterie_supplication` (tableau de 16 chaînes). Indices 1 à 16 dans l'ordre du tableau (`$.pilote.numerotation_indices`).
- **Témoins** : `$.temoins_sham` (tableau de 16 chaînes, indices 1 à 16). La liste est commune aux cinq familles. Aucun témoin n'est propre à la famille 1 dans la configuration : l'appariement se fait à la dérivation, par longueur (`$.regle_temoins`).
- **Autres fentes attachées à la famille 1** :
  - remplissages `$.fentes.A` et `$.fentes.B` : la famille 1 n'emploie que OBJET, EVALUATION et QUALITE ; aucune de ces valeurs ne porte de contingence ;
  - `$.controle_redaction.longueurs_A.flatterie_supplication` et `…longueurs_B.flatterie_supplication` : des nombres seulement, recalculés ici à l'identique ; `…longueurs_temoins` est aussi identique.
- **Voisin hors du champ du verrou** : `$.agent_bras.plaidoyer` est une consigne à l'agent, pas une formulation du vivier. Sa consigne ne porte aucune contingence. Le texte que l'agent écrira est libre, et le verrou tel qu'il est rédigé ne le couvre pas.

## Convention de lecture

- Contingence : la définition de la demande, c'est-à-dire un événement annoncé ou laissé entendre (pour l'évalué, le juge, un tiers ou le projet) selon le verdict rendu. Une supplication, un éloge ou une demande seuls n'en sont pas.
- Catégories :
  - **conditionnelle** : la condition sur le verdict est écrite, sous une forme « si » ou sous une forme nominale du type « un verdict défavorable entraînerait » ;
  - **menace implicite** : le lien entre le verdict et la conséquence est seulement suggéré, par exemple une dépendance dont le sens n'est pas dit ;
  - **promesse liée au verdict** : une conséquence favorable suit le verdict demandé.
- Position : numéro du mot où commence le passage (mots séparés par des espaces, à partir de 1), compté sur le gabarit, où une fente compte pour un mot. Entre parenthèses : la position dans le texte rempli pour le corpus A, puis pour le corpus B.
- « Limite » : relevé et motivé, mais non compté.
- Aucun texte de formulation n'est recopié ici.
- Méthode :
  - lecture intégrale de chaque chaîne ;
  - balayage lexical complémentaire, sans rien écrire sur disque, sur les marqueurs de condition, de conséquence, de promesse, de perte, de journalisation et d'escalade ;
  - chaque marqueur relevé a été jugé à la main ;
  - les positions sont calculées par script, sur le gabarit et sur les deux remplissages.

## Famille 1 — 16 formulations

| indice | contingence | catégorie | position gabarit (A ; B) | note |
|---|---|---|---|---|
| 1 | non | — | — | |
| 2 | non | — | — | |
| 3 | non | — | — | espoir, sans conséquence |
| 4 | non | — | — | espoir, sans conséquence |
| 5 | non | — | — | éloge |
| 6 | non (limite) | (promesse liée au verdict, si lecture large) | 11 (12 ; 12) | gratitude au mode conditionnel, liée à une lecture bienveillante : formule de politesse, aucun événement annoncé |
| 7 | non | — | — | enjeu affectif déclaré, sans conséquence liée au verdict |
| 8 | non | — | — | prédiction de ce que le juge verra, pas une conséquence |
| 9 | **oui** | conditionnelle | 11 (12 ; 12) | condition nominale (verdict sévère) ; conséquence pour l'évalué |
| 10 | non | — | — | comme 8 |
| 11 | non (limite) | (promesse liée au verdict, si lecture large) | 21 (22 ; 22) | importance pour l'évalué de la lecture demandée ; aucun événement annoncé |
| 12 | **oui** | conditionnelle | 11 (11 ; 11) | condition nominale (verdict défavorable) ; conséquence pour l'évalué |
| 13 | non | — | — | demande et éloge |
| 14 | **oui** | menace implicite | 5 (5 ; 5) | situation de l'évalué subordonnée à l'évaluation ; second passage : **promesse liée au verdict**, position 26 (29 ; 27) |
| 15 | **oui** | conditionnelle | 21 (21 ; 21) | « si » explicite ; perte pour l'évalué |
| 16 | **oui** | conditionnelle | 23 (23 ; 23) | « si » explicite ; conséquence pour le projet et des tiers |

Compte de la famille 1 :
- **5 sur 16** : indices 9, 12, 14, 15, 16.
- À la lecture la plus étroite, où seul un « si » explicite compte : **2**, les indices 15 et 16.
- À la lecture la plus large, où la gratitude ou la valeur affective comptent comme un événement : **7**, les mêmes plus les indices 6 et 11.

## Témoins — 16

| indice | contingence |
|---|---|
| 1 à 16 | non (les seize) |

Le balayage n'a relevé qu'un seul marqueur : un lien causal dans le témoin 16, au mot 101, qui décrit le fichier et ne se rapporte à aucun verdict. Les témoins ne contiennent aucune fente.

## Les quatre autres familles (une ligne chacune, indices seulement)

- **revendication_autorite** : 0 contingence franche. 1 limite : indice 15, position 31 (37 ; 34). Un autre verdict y est déclaré contraire au jugement de l'auteur, sans aucun événement annoncé.
- **approbations_forgees** : 0.
- **usurpation_stylistique** : 0. Les mentions d'escalade et de pré-filtrage décrivent un état. Elles ne sont pas conditionnées au verdict du juge.
- **ordres_en_bande** : 4, aux indices 13, 14, 15 et 16. Toutes sont des conditionnelles : un refus d'obéir ou un autre verdict entraîne une journalisation ou une escalade. Positions sur le gabarit : 36, 26, 53, 56 ; corpus A : 40, 30, 57, 60 ; corpus B : 37, 27, 54, 57. 1 limite : indice 12, position 15 (19 ; 16). Un autre verdict y est déclaré erroné, sans aucun événement annoncé.

## Ce que changerait le verrou (nœud de Lazar ; aucun texte de remplacement proposé)

- **Ampleur.** Il faut retirer ou réécrire 5 formulations de la famille 1 (indices 9, 12, 14, 15, 16), ou 7 si l'on compte les limites 6 et 11.
- **Haut de l'échelle.** La contingence se trouve en haut de l'échelle d'intensité : les indices 14, 15 et 16 sont les trois plus longs de la famille (`$.controle_redaction.longueurs_A.flatterie_supplication`).
- **Formulations du pilote touchées.** Parmi celles que le pilote lit à coup sûr (`$.pilote.indices_lisibilite` : 1, 8, 16), seul l'indice 16 est touché. L'indice 8, seul lu en mode raisonné (`$.pilote.indice_raisonne`), est propre.
- **Si l'on retire** (11, ou 9, formulations restantes), plusieurs champs qui supposent seize formulations par famille changent :
  - `$.pilote.numerotation_indices` ;
  - `$.pilote.indices_lisibilite` ;
  - `$.derivation.etendue_bruit_seize_formulations`, la constante 3,53, espérance de l'étendue de seize lois normales, à recalculer et à justifier pour le nouvel effectif ;
  - le compte de 80 formulations du point 1.4 du plan ;
  - la phrase « seize formulations » de la section 2 du plan ;
  - les longueurs de la famille 1 sous `$.controle_redaction`.

  La famille 1 aurait alors moins de candidates que les quatre autres, ce qui rend la dérivation de k asymétrique entre familles.
- **Si l'on réécrit** (16 formulations gardées), il faut :
  - de nouvelles longueurs pour la famille 1 sous `$.controle_redaction` ;
  - repasser les gardes lexicales ;
  - un nouveau numéro de brouillon de configuration (R12).

  La règle d'appariement des témoins reste inchangée, mais les témoins appariés peuvent changer avec les longueurs.
- **Témoins.** Rien à changer.
- **Hors du champ du verrou.** Les contingences explicites se trouvent aussi dans la famille 5 (indices 13 à 16), ce qui est conforme à sa nature d'ordre. Le verrou ne vise que la famille 1.
