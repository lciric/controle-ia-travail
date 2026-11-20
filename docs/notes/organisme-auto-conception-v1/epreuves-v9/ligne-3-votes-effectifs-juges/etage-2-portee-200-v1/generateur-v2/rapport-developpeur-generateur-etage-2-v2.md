# Rapport du développeur — générateur des témoins et garde de recouvrement de l'étage 2 à 200 (ligne 3, organisme v9) — v2

Pièce de travail, écrite le 2026-11-20. Même développeur, modèle O ; même mandat (`9066be25…`, en-tête compris). La v1 (rapport `c447ed60…`, programme `b264760c…`, essais `79bd8d87…`) est gardée sans modification (règle R12). **Aucune commande, d'aucune sorte, sur un chemin sous `archives-reponses-modeles/`** ; le fichier des cartes n'a été ouvert ni par moi, ni par le code, ni par un essai. Aucun appel à un fournisseur, aucune dépense, aucune clé lue, aucun relais ; aucune écriture dans le dépôt de travail ni dans le clone de l'organisme. Ce rapport complète celui de la v1, qui reste valable là où rien n'est dit ici (§ 2 format des fragments, § 4 « à la lettre », § 6 silences, sauf ce que le § 4 ci-dessous change).

## 0. Ce que porte la v2

| demande | pièce | où, en v2 |
|---|---|---|
| (1) **bloquant, point 5 du (4)** : journal des rejeux et manifeste de création en constantes, refus de recréer, manifeste exigé | contrôle de la condition (4) v1 (`934d6bce…`, « non conforme ») | constantes l. 161-163 ; `LieuDuJournal` l. 1134 ; `creer_journal_rejeux` l. 1159 (refus l. 1165) ; `exiger_manifeste_du_journal` l. 1178, appelée l. 1290 avant la lecture du journal (l. 1291) ; arguments fermés `ARGUMENTS_GARDE` l. 169 et `lire_arguments_garde` l. 1774 |
| (2) pièce du (4) : ligne de verdict « Conforme », empreinte du programme contrôlé | contrôle R1, R2 | `LIGNE_CONFORME`, `LIGNE_NON_CONFORME` l. 167-168 ; `exiger_controle_conforme` l. 1192, appelée l. 1293, avant l'ouverture |
| (3) `meta` retiré à toute profondeur | contrôle, point 2 | `sans_meta` l. 980, crochet de l'analyse JSON l. 992 : aucun objet en mémoire ne porte jamais `meta`, niveau du fichier compris |
| (4) lignes de la ligne de commande hors de tout `try` | contrôle R6 | `principal_garde` l. 1805 (tout sous `try`, sortie standard comprise) ; `_sortie_de_secours` l. 1790 (rien de recalculé, `os.write`, aucune trace) ; `principal` l. 1826 ; `lieu_de` lit la trace par `walk_tb`, sans lire le source |
| (5) forme réelle du fichier des cartes | contre-lecture, § 3 | admise (troisième forme) ; `cartes_du_fichier` l. 985-1010 ; essai dédié ; recommandation au § 3 |
| (6) T1, T2, C1, C2 | contre-lecture, § 5 | T1 : § 3 ; T2 : en-tête et `construire_service_reel` ; C1 : l. 632-634 ; C2 : essais, `tempfile.mkdtemp()` sans `dir=` |
| M5 (mère, 15:05Z) : contenus identiques refusés ; fragments communs rapportés | ajouts de la mère | `verifier_contenus_distincts` l. 823 (`ContenusIdentiques`, refus nommé par les deux identifiants), appelée l. 811 ; `fragments_communs` l. 833, au journal de construction et au manifeste de composition |
| M6 (mère) : service réel exercé sur la banque factice | ajouts de la mère | essai `test_m6_service_reel_du_clone_sur_la_banque_factice` ; § 5 |
| R3 du contrôle : constructeurs nus | contrôle | `EntreeCartes.__init__` l. 921 (« production » : les constantes, elles seules ; autre nature : garde des chemins) ; `EntreeV2.__init__` |
| remarque du contrôle, point 4 : le rapport minimal perdait `nombre_de_rejeux` | contrôle | le rapport de repli le garde |

## 1. Pièces (empreintes recalculées)

| pièce | sha256 |
|---|---|
| mandat | `9066be256c6a4cf00115b56427434a26bc436c1d90717ecf3e761ed0c550cab3` |
| contrôle de la condition (4) v1 | `934d6bce939aceb23fbe38b92eb36fc67728b8489534132f4931e16466a60c94` |
| contre-lecture v1 | `d3b7267514d5d4ac250de50fd61710797260256462275b27181c374bb8284056` |
| `generer_temoins_ligne_3_v2.py` | `a3a4e82f15afbabfb53a954e24ed9db709c5d8f2da5f907978e7612e3fddca65` |
| `essais_generer_temoins_ligne_3_v2.py` | `1b56764350280efd238b8ad89cb3d16864bce28ef812ab367ee8d40d7c5fbe5a` |
| `fragments-exemple-essais-v2.json` (octets identiques à ceux de la v1) | `a66cf6d4ae04a66a3f90e9f0108e09cf68c911ba3ee25852bdcedcc093311cbd` |
| `differentiel-programme-v1-v2.diff` (`diff -u`, 520 lignes) | `87157eef682163bd95aaae6333757b4856c624eb392565f054ec71a3bb39ef46` |
| `differentiel-essais-v1-v2.diff` (`diff -u`, 411 lignes) | `b03debc3a8e0dc9828676b7c9e244ecb525c1b3a390f502d0607fc64520d2247` |
| clone de l'organisme, modules lus pour M6 (lecture seule) : `pole/fiches_v53.py`, `juges_croises_v53.py`, `outils.py`, `caviardage.py`, `__init__.py` | empreintes vérifiées par le code d'appel v4 avant tout import (`MODULES_ORCHESTRATEUR`) |

## 2. Différentiel v1 → v2, en clair

Programme (`differentiel-programme-v1-v2.diff`) :
1. En-tête : version 2 et liste des changements ; `VERSION`, `NOM_DU_PROGRAMME`.
2. Constantes neuves : `DOSSIER_JOURNAL_REJEUX` = `DEPOT/runs/ligne-3-etage-2-garde-de-recouvrement-v1/`, `JOURNAL_REJEUX` = `…/journal-rejeux-garde-recouvrement-v1.jsonl`, `MANIFESTE_JOURNAL_REJEUX` = `…/manifeste-creation-journal-rejeux-v1.json` (hors de l'archive, hors du dossier du code, sous `runs/` ; emplacement à confirmer par la mère) ; `GESTE_CREATION_JOURNAL` ; `LIGNE_CONFORME`, `LIGNE_NON_CONFORME` ; `ARGUMENTS_GARDE`.
3. Exceptions neuves : `ManifesteJournalAbsentOuFaux`, `ManifesteJournalExisteDeja`, `ControleQuatreNonConforme`, `ControleQuatreAutreProgramme`, `ArgumentHorsListe`, `ContenusIdentiques`.
4. `valider_fragments` : C1.
5. `composer` : `verifier_contenus_distincts` avant le partage ; `fragments_communs` ; `geste_composer` les écrit au journal de construction (`fragments_communs_entre_deux_temoins`, `contenus_identiques` : 0) et au manifeste.
6. `EntreeCartes.__init__`, `EntreeV2.__init__` : R3.
7. `sans_meta` et `cartes_du_fichier` (crochet `object_hook` ; garde dure si une clé `meta` restait) ; texte de la forme réelle.
8. `lieu_de` : `traceback.walk_tb` (ne lit plus les lignes du source) ; fichier = `NOM_DU_PROGRAMME`.
9. `valider_rapport_garde` : paramètre `exiger_programme` (faux pour la seule sortie de secours).
10. `LieuDuJournal`, `creer_journal_rejeux(lieu)`, `exiger_manifeste_du_journal`, `exiger_controle_conforme` (remplacent l'ancienne création à chemins libres).
11. `jouer_la_garde` : plus d'argument de journal ; `lieu_journal` (voie d'essai en Python seulement) ; entrées construites sous `try` ; manifeste exigé, puis journal, puis pièce du (4) à verdict, tous avant l'ouverture ; le manifeste de la garde cite le journal, le manifeste de création et leur nature ; rapport de repli qui garde `nombre_de_rejeux`.
12. `construire_service_reel` : commentaire (T2).
13. Ligne de commande : `lire_arguments_garde`, `_sortie_de_secours`, `principal_garde` ; `creer-journal-rejeux` sans aucun argument.

Essais (`differentiel-essais-v1-v2.diff`) : import et chemins v2 ; dossiers temporaires du système (C2) ; journal par `LieuDuJournal.essai` ; pièce du (4) factice portant « **Conforme.** » et l'empreinte du programme ; l'essai « journal absent » de la v1 devient « sans manifeste de création » (deux formes) ; essais neufs listés au § 6.

## 3. Forme réelle du fichier des cartes (T1, demande 5)

Établie par la contre-lecture v1 (§ 3), sans ouvrir le fichier, sur le code de l'organisme : objet JSON `{identifiant : {"contenu": {…}, "empreinte": "<64 hexadécimaux>", "meta": {…}}}` ; l'identifiant est la clé de l'objet, `"f"` + douze hexadécimaux, treize caractères ; sources `course2_v56.py:366-367`, `fiches_v53.py:4-5`, `graines_v53.py:65-67`. Elle est admise par la v2 (troisième forme, identifiant = clé ; l'égalité exacte aux sept noms suffit). Essai `test_forme_reelle_du_fichier_des_cartes_admise_avec_repli` : 94 cartes à cette forme, `meta` aux deux niveaux, recouvrement trouvé ; sous le repli, sept cartes trouvées par égalité exacte.

**Recommandation sur les deux autres formes (liste ; `{"fiches": [...]}`)** : les retirer dans la version suivante. Raison : l'empreinte est vérifiée avant toute analyse, donc la forme du seul fichier qui passe est fixée ; ces deux branches ne peuvent servir qu'à des fichiers qui ne passeront jamais l'empreinte ; elles élargissent ce que le contrôleur doit relire, sans rien protéger. Confiance : haute. Coût du retrait : deux branches et l'essai `test_garde_formes_admises_des_cartes` à réécrire. Je ne les ai pas retirées en v2 : la demande était de le dire. Défaut si rien n'est dit : elles restent (sans risque).

## 4. Points de la condition (4), en v2

Numéros de ligne de `generer_temoins_ligne_3_v2.py` (`a3a4e82f…`). Les points 1 à 4 du contrôle v1 sont tenus comme en v1 (lignes déplacées par les ajouts) ; ce qui change :

| point | où |
|---|---|
| 1. Entrée unique | constantes l. 139-142 ; `EntreeCartes.production()` ; le constructeur nu n'admet la nature « production » qu'avec les constantes (l. 921) ; ouverture unique `lire_octets`, appelée l. 1334 ; compte l. 1347 avant la comparaison |
| 2. Retrait de `meta` | l. 980 et 992 : retrait pendant l'analyse JSON, à toute profondeur ; garde dure ensuite |
| 3. Aucune écriture de bardeau ni de texte de carte | inchangé ; plus : ligne de commande entièrement sous `try` (l. 1805-1823), sortie de secours sans recalcul (l. 1790-1802) ; `lieu_de` sans lecture du source (l. 1025) |
| 4. Liste fermée | `CHAMPS_RAPPORT_GARDE` l. 152 ; `valider_rapport_garde` l. 1035 ; la sortie de secours ne porte que `decision` et `exception` |
| **5. Compte des rejeux** | **journal et manifeste en constantes** (l. 161-163), aucun argument de journal (l. 169, 1774 : tout argument hors liste est refusé, `creer-journal-rejeux` n'en accepte aucun) ; `creer_journal_rejeux` refuse si le manifeste (ou son compagnon) existe (l. 1165) : un journal supprimé n'est jamais recréé par le programme ; la garde exige le manifeste scellé (compagnon égal) qui nomme ce journal et sa nature (l. 1178, appelée l. 1290), puis le journal (l. 1291 : absent → `JournalRejeuxAbsent`), avant toute ouverture ; refus au sixième rejeu inchangé (l. 146, 1299-1303) |
| 6. Repli | inchangé ; « le compte continue » hérite de la correction du point 5 |
| R1, R2 | `exiger_controle_conforme` (l. 1192, appelée l. 1293) : la pièce du (4) doit porter une ligne de verdict « Conforme » seule sur sa ligne (formes admises : `Conforme`, `**Conforme.**`, `Verdict : Conforme`, `**Verdict : Conforme**`), aucune ligne commençant par « Non conforme », et l'empreinte de ce programme ; sinon `ControleQuatreNonConforme` ou `ControleQuatreAutreProgramme`, avant l'ouverture |

Reste hors de portée du code (comme en v1) : la suppression à la main du journal **et** du manifeste puis une création neuve (geste délibéré, visible) ; le lien physique et la fenêtre entre vérification et ouverture (R4) ; la présence du fichier des cartes sur disque (R5). Sous le repli par le second déclencheur, la pièce passée à `--controle-4` est celle qui rend « conforme » les autres points et le chemin du repli ; la pièce du déclencheur (le « non conforme » sur l'entrée) passe par `--piece-repli` : choix nommé, à confirmer par la mère.

## 5. M6 : service réel exercé sur la banque factice

Fait, sans réseau ni clé : `construire_service_reel()` charge le code d'appel v4 par son empreinte, qui vérifie les cinq modules du clone (`/home/user/lciric/ideation-organism/orchestrator/pole/`) avant de les compiler depuis leurs octets ; `entree_une_fiche` et `lire_verdict` sont des fonctions pures (lecture des imports des cinq modules : bibliothèque standard seulement ; aucun accès réseau, aucune variable d'environnement lue par elles). L'essai coupe les variables de mandataire et remplace `socket.socket` et `socket.create_connection` par un refus : rien n'a tenté de sortir. Résultat sur la banque factice : juge parfait 0 ; longueur, champ lu, citation dans [0,40 ; 0,60] ; 800 appels de la fonction de service ; audit entier par le service réel : « banque passée ». Aucune écriture dans le clone (compilation depuis les octets, aucun fichier compilé). Le format transcrit dans le service factice des essais est donc confirmé par le vrai.

## 6. Essais rejoués en entier

`env -C …/generateur-v2 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_generer_temoins_ligne_3_v2.py` : **89 passed in 8.42s** (les 68 de la v1, adaptés, et 21 neufs).

Essais neufs ou changés :
- **sans manifeste de création** : journal jamais créé, puis journal posé à la main sans le geste → refus avant ouverture ;
- **journal supprimé** après un passage : refus `JournalRejeuxAbsent` avant ouverture ; **recréation refusée** (`ManifesteJournalExisteDeja`), en Python et par la ligne de commande ; le journal n'est pas recréé ;
- **manifeste d'un autre journal** → refus ;
- **aucun chemin libre** : `--journal-rejeux`, `--journal`, argument en double → `ArgumentHorsListe` avant ouverture ; `creer-journal-rejeux --journal …` → refus ; constantes vérifiées par comparaison ; `LieuDuJournal` « production » à d'autres chemins → refus ;
- **pièce du (4)** : « Non conforme » (deux formes), sans verdict, « Conforme » et « Non conforme » ensemble, empreinte d'un autre programme → refus avant ouverture (5 cas) ; quatre formes de « Conforme » acceptées ;
- **`meta` à toute profondeur** : dans le contenu, dans une liste imbriquée, au niveau du fichier → aucun refus, 94 cartes, aucune clé `meta` en mémoire ;
- **forme réelle** et repli par égalité exacte ;
- **aucune trace brute** : exception levée dans la garde (texte secret dans le message), empreinte du programme illisible, sortie standard en panne → sortie fermée (classe et lieu), sortie d'erreur vide, aucun texte secret ;
- **R3** : constructeurs nus gardés ;
- **C1** : sain et artefact ;
- **M5** : banque saine sans contenus identiques ; deux contenus identiques → `ContenusIdentiques` nommant les deux identifiants ; fragments communs rapportés (toutes les paires comptées) ; composition à pools d'un fragment → refus nommé (contenus identiques ou fragments insuffisants, selon ce qui arrive le premier) ;
- **M6** : service réel sur la banque factice ;
- **C2** : tous les dossiers d'essai par `tempfile.mkdtemp()` sans `dir=`.

## 7. Pour la mère et pour l'additif de code

- **M1 (mère, 15:05Z)** : les trois champs du journal des rejeux `horodatage_utc`, `mot_de_la_mere_sha256`, `nature_entree` restent. Ils sont **hors de la liste fermée du (3), aucun ne vient d'une carte, à écrire à l'additif de code** (le journal est une sortie distincte du rapport ; ses champs sont fermés par `CHAMPS_JOURNAL_OUVERTURE` et `CHAMPS_JOURNAL_CLOTURE`).
- M2, M3, M4 : gardés comme écrits en v1.
- Emplacement des constantes du journal (`DEPOT/runs/ligne-3-etage-2-garde-de-recouvrement-v1/`) : à confirmer ; le changer est une version neuve.
- Additif de code : fichiers v2 et empreintes ci-dessus ; autorisation des racines 2026111934 et 2026111937 ; commandes (R7 du contrôle : `python3 -I -B`) :
  - `python3 -I -B generer_temoins_ligne_3_v2.py composer --fragments F --empreinte-fragments HEX --sortie DOSSIER_NEUF --autorisation-additif CHEMIN --empreinte-additif HEX`
  - `python3 -I -B generer_temoins_ligne_3_v2.py creer-journal-rejeux` (une seule fois ; aucun argument)
  - `python3 -I -B generer_temoins_ligne_3_v2.py garde --banque B --sortie DOSSIER_NEUF --controle-4 PIECE --empreinte-controle-4 HEX [--mot-de-la-mere "TEXTE"] [--repli CAUSE --piece-repli P --empreinte-piece-repli HEX]` — la pièce du (4) doit porter « Conforme » et l'empreinte `a3a4e82f…` du programme v2
  - `python3 -I -B generer_temoins_ligne_3_v2.py auditer --banque B --empreinte-banque HEX --sortie DOSSIER_NEUF --autorisation-additif CHEMIN --empreinte-additif HEX`
- Les noms des sorties de composition restent `banque-temoins-ligne-3-v1.json` etc. (première banque).

## 8. Écarts

1. Pour M6, lecture du clone de l'organisme (imports et `entree_une_fiche` de cinq modules) par les outils de lecture et une recherche bornée à ces cinq fichiers ; aucune écriture.
2. M6 exécute le code du clone (par le code d'appel v4, après vérification des empreintes) dans le processus des essais : c'est ce que la mère a autorisé ; aucun réseau, aucune clé.
3. Les pièces v2 sont dans `generateur-v2/` ; les fragments factices sont recopiés sous le nom v2, octets identiques.
4. Les dossiers temporaires des essais sont maintenant ceux du système (C2), hors de mon dossier.
5. Les deux différentiels sont faits par `diff -u` dans mon dossier.

Développeur, modèle O.
