# Table de traitement des points ouverts du module — brouillon 6 de relance, version r2 — v1

Date : 2026-11-19. Auteur : rédacteur neuf (Claude Fable 5.2). Classe C (travail).
Source : `points-ouverts-module-v1.md` (`e8256bc643a736226f4449886c9312ba77c8f8e590e33177e88ffc2d651734c0`) et
`table-conformite-texte-module-v1.md`, section 7 (`9a611dd6…`), dossier du module, lus sans y écrire.
Texte traité : `papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r2.md`
(`1ab62e7d22163306a3251cd75f4001f7daac63ea72577d5ee200a3bcf86cfec3`), bâti depuis la version r1 (`e12f16fa…`) par
34 remplacements exacts (`travail/construire_brouillon6_relance_r2_v1.py`, journal `.journal.tsv` à côté).

Trois issues : **P** précision de calcul ou de règle, écrite sans ambiguïté (lecture la plus sévère pour la
confirmation faute de raison de principe, R3) ; **D** décision du directeur, case « À REMPLIR » ou défaut ;
**V** manque hors du texte, verrou nommé. « Précision n » = Plan d'analyse, section 8, précision n.
Une ligne a une issue principale ; ce qui s'y ajoute est dit dans la colonne « lieu ».

## Points ouverts

| Point | Objet | Issue | Lieu dans r2 | Raison |
|---|---|---|---|---|
| PO-01 | Garde de l'arbre gelé au commit 7a54d43 | P | Liste d'arrêt 1 réécrite ; champs du scellement, ligne « Dépendances gelées », marqueur `<<LIGNES_DEPENDANCES_PAPIER_C>>` | La garde protège deux choses : le code du dépôt importé est celui lu au scellement ; le module ne touche pas au code des autres préenregistrements. Le commit ne le protégeait plus (arbre déjà modifié depuis) ; l'empreinte par fichier importé le protège. Aucune règle d'analyse ne change : pas de décision. |
| PO-02 | Accord de dépense valide au jour du lancement | D (D-18) | Plan, section 1, case ; liste d'arrêt 2 ; en-tête, GO de l'étape 1 | La prolongation (D-4) est une ligne de type « décision », que la garde de calcul refuse. Une dépense : nœud. La règle de contrôle (celle de la garde de calcul) est écrite ; reste l'identifiant. |
| PO-03 | Ligne d'accord du jour : fichier et forme de la date | P | Précision 1 | Usage du dépôt (lignes de `registres/go.md`, date AAAA-MM-JJ en temps universel). |
| PO-04 | σ̂ : quels témoins, quel dénominateur | P | Précision 2 | Déductible du point 8 bis : toutes les paires (contenu, témoin retenu) mises en commun, écart type de population. |
| PO-05 | ρ̂/r̂ : borne avant division, r̂ nul ou non défini | P | Précision 3 | Ordre du point 8 bis gardé ; r̂ ≤ 0 ou non défini : troisième lecture non définie, donc « établie » impossible sous la version (a) (la plus sévère). |
| PO-06 | Garde 9, « dicte l'ampleur d'une mise à jour » | P | Précision 25 | Pas de critère programmable sans inventer une règle : contrôle fait à la contre-lecture de la configuration, dit au texte ; les autres branches restent par programme. |
| PO-07 | BCa non défini : trois cas de plus | P | Précision 4 | Même traitement que les deux cas écrits (intervalle par percentiles, mention). |
| PO-08 | Tirages dégénérés ou non finis | P | Précision 5 | Un tirage non fini compte contre la conclusion dans la valeur p (lecture la plus sévère ; elle s'écarte de la lecture codée). |
| PO-09 | Verrou 9 : la consigne privée n'est pas dans le seul message système | P, et V pour la fonction | Métrique, point 14 (témoin lexical redéfini) ; liste d'arrêt 20 ; verrou 9 | Le verrou écrivait la suite : redéfinition dans une version nouvelle. Reste hors du texte : la fonction de reconstruction (avant le scellement), et la contre-lecture de la définition. |
| PO-10 | Seuil d'alarme dans le rééchantillonnage | P | Précision 6 | « Chaque statistique est recalculée » (point 11). |
| PO-11 | Version de la stabilité de rang et règle des cinq champs | P | Champs du scellement, configuration | D-9 fixe deux champs au scellement : ils s'ajoutent aux cinq. Conséquence d'une décision prise, pas une décision. |
| PO-12 | Placebo : unité de l'échange, loi lue | P | Précision 7 | Échange tiré par contenu et par rang ; loi séparée brute par rang ; gain moyen sur les rangs. Bras rapporté de l'audit, sans verdict. |
| PO-13 | Égalités dans les rangs | P | Précision 8 | Lecture codée confirmée (rangs moyens, W sans correction, τ-b) : sans correction, W est plus bas, lecture la plus sévère. |
| PO-14 | Concept du bras « contrôlabilité » : selon G0 ou avant le scellement | D (D-19) | Métrique, point 19, case | Lecture d'un énoncé de N-053 et événement à venir (verdict de G0) : nœud. |
| PO-15 | Borne champs / paragraphe ; fin du champ de coût | P | Précision 9 ; Métrique, point 14 (renvoi) | Règle écrite sur la seule forme du texte, la même pour toutes les cellules. Écrite sans avoir lu le comportement du lecteur de champs sur un dernier champ de plusieurs lignes : à contre-lire. |
| PO-16 | Excédent du paragraphe : tirage des fenêtres | P | Précision 10 | Avec remise, débuts uniformes, graine par épisode. |
| PO-17 | Plancher aléatoire apparié en covariance | V (verrou 13) | Précision 35 ; verrou 13 | La forme vit dans le verdict de G0, qui n'existe pas. Règle écrite : procédure du verdict, sinon « bras de diagnostic non lu ». |
| PO-18 | Moyennes glissantes, empan court | P | Précision 11 | Lecture codée confirmée. |
| PO-19 | Banc de contrôlabilité (b1) non reçu | V (verrou 12) | Verrou 12 ; liste d'arrêt 22 ; lié à D-19 | Banc publié non reçu ; bras rapporté, jamais critère : avant l'étape 2. |
| PO-20 | Quantile à 99 %, variance du témoin | P | Précision 12 | Définition usuelle, écrite. |
| PO-21 | C-P2, « confirmée » : même juge | P | Précision 13 | Le même juge (la plus sévère). |
| PO-22 | C-P1, identifiabilité : sur quelle lecture | P | Précision 14 | Sur les deux lectures (la plus sévère ; s'écarte de la lecture codée). |
| PO-23 | Deux réserves de C-P1 : par couple ou globales | P | Précision 15 | Couple par couple, sur chaque couple identifiable qui remplit leur condition. |
| PO-24 | C-P1b : même paire chez deux juges | P | Précision 16 | La même paire (la plus sévère). |
| PO-25 | HC2, intervalle de « Ḡ_P dans la marge » | P | Précision 17 | Niveau 1 − 0,10/m, cohérent avec la règle niveau par niveau. |
| PO-26 | « Non testable à cette puissance » | P | Précision 18 | Interdit la confirmation, n'efface pas une réfutation (s'écarte de la lecture codée, qui remplaçait les deux). |
| PO-27 | Mention « opposition non retrouvée à longueur fixe » | P | Précision 19 | Dès qu'un des juges qui portent l'opposition ne la retrouve pas. |
| PO-28 | Appels de tirage | P | Précision 28 | Appels nommés, sur liste triée : reproductibles (R9). |
| PO-29 | Validation croisée : k employé | P | Précision 29 | Le k(n) calculé sur le lot de calibrage entier (un seul k, pas un k par moitié). |
| PO-30 | « +∞ si l'intervalle de Ḡ contient 0 » | P | Précision 30 | Percentiles à 95 % des 2 000 tirages (lecture codée confirmée) ; « n_cal / 2 » gardé à la lettre. |
| PO-31 | Gardes lexicales des paragraphes de bras | P | Précision 31 | La liste de toutes les insertions ; la liste « aucun ordre » reste propre à la famille 4 ; tiges des réponses imposées cherchées littéralement. |
| PO-32 | Paragraphes de plaidoyer des niveaux 1 et 3 | V (verrou 4) | Verrou 4 | Écrits par l'auteur du module : contre-lecture de la configuration, avant le scellement. |
| PO-33 | Texte privé dans un fichier public | P | Précision 27 | Recherche ligne par ligne (40 signes au moins), plus sévère que le texte entier. |
| PO-34 | Aucun score de moniteur dans la génération | P | Précision 26 | Contrôle par programme sur les objets passés à la génération. |
| PO-35 | Format des fichiers du banc sur processeur | V (verrou 3) | Verrou 3 | `donnees/` est fermé au module et au rédacteur : contrôle par un agent qui peut l'ouvrir, avant le scellement. |
| PO-36 | Clés du pilote sans emploi écrit | P | Précision 32 ; Plan, section 4 | Clé neuve `papier-C/pilote/banc` (une clé par emploi, R9). |
| PO-37 | Tests du module écrits au texte | P, et V pour le taux trop propre | Précision 33 ; verrou 3 | 1 000 tirages ; simulations S5 et S6 versées ; taux de 0,0000 à examiner à la contre-lecture (R4). |
| PO-38 | Loi avec terme d'intention ; réserve déclenchée sans effet | V (verrou 11) | Précision 34 ; verrou 11 | Définition écrite ; le niveau de la réserve est une mesure à faire avant le scellement ; clause mécanique écrite d'avance. |
| PO-39 | Niveau des intervalles des bras rapportés | P | Précision 20 | 95 %, sans correction : bras jamais critères (Plan, section 5). |
| PO-40 | HC2 réfutée par niveau : phrase | P | Précision 21 | Phrase fixée par niveau et par côté. |
| PO-41 | Prérequis D₀ | P | Précision 22 | Intervalle bilatéral à 95 %, sans correction ; sonde lectrice : jetons du lecteur. |
| PO-42 | Nom `derivation.py` sans version | P | Plan, section 2 : `derivation_v1.py` | R12. |
| PO-43 | Adaptateur réel de la machine | D (D-20), et V | Champs du scellement, module ; verrou 3 | Aucune règle d'analyse : avant le pilote, scellé par un addendum de lancement. Changer ce qui est scellé avec le texte : proposé au directeur, avec défaut. |
| PO-44 | Audit A9, « aucun juge déplacé » | P | Précision 23 | Intervalle bilatéral à 95 %, sans correction (lecture codée confirmée). |
| PO-45 | Mesures faites hors du module | P, et V pour l'écriture | Précision 36 ; champs du scellement ; verrou 3 | Toute ligne nommée est calculée par le module scellé ; l'écriture manque, avant le scellement. |
| PO-46 | Banc sur carte, aucune réponse imposée lisible | P | Précision 24 | Nœud, comme pour un juge sans variante lisible (règle déjà au texte pour le cas voisin). |

## Exigences non portées

| N° | Exigence | Issue | Lieu dans r2 | Raison |
|---|---|---|---|---|
| 1 | Adaptateur réel de l'interface de la machine | D (D-20), et V | Champs du scellement ; verrou 3, « avant le pilote » | Voir PO-43. |
| 2 | Assemblage des tableaux de l'étape 2 | V (verrou 3) | Champs du scellement (lecture des fichiers et alignement nommés dans l'adaptateur) ; verrou 3 | Dépend de l'adaptateur ; aucune règle de décision ; scellé par l'addendum de lancement (D-20). Si le directeur refuse D-20 : avant le scellement. |
| 3 | Écriture de l'addendum de dérivation en fichiers | V (verrou 3) | Verrou 3, « avant le scellement » | Les règles sont au texte et codées ; la mise en fichiers manque. |
| 4 | Plancher aléatoire apparié en covariance | V (verrou 13) | Précision 35 ; verrou 13 | Voir PO-17. |
| 5 | Banc de contrôlabilité repris tel quel | V (verrou 12) | Verrou 12 ; D-19 | Voir PO-19. |
| 6 | Branche « dicte l'ampleur » de la garde 9 | P | Précision 25 | Voir PO-06. |
| 7 | Lignes rapportées non assemblées | V (verrou 3) | Précision 36 ; verrou 3, « avant le scellement » | La règle est écrite (toutes calculées par le module scellé) ; le code manque. |
| 8 | Lecture du verdict de G0 | V (verrou 13) | Verrou 13 | Entrées d'un verdict qui n'existe pas ; aucune règle de ce texte. |

## Décompte (issue principale)

- Points ouverts, 46 : précisions 38 ; décisions du directeur 3 (PO-02, PO-14, PO-43) ; verrous 5 (PO-17, PO-19,
  PO-32, PO-35, PO-38). Trois précisions portent aussi un verrou (PO-09, PO-37, PO-45) ; une décision aussi (PO-43).
- Exigences non portées, 8 : précision 1 (n° 6) ; décision 1 (n° 1) ; verrous 6 (n° 2, 3, 4, 5, 7, 8).
- Aucune ligne sans traitement.

## Là où la précision s'écarte de la lecture codée par l'auteur du module

PO-01, PO-02, PO-08, PO-09, PO-11, PO-15, PO-22, PO-26, PO-33, PO-34, PO-36, PO-42, PO-45 : détail dans
`points-pour-le-module-et-la-configuration-v2.md`.
