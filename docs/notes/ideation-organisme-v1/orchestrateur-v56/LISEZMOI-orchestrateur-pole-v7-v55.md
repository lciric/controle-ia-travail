# Orchestrateur du pôle, v7 — version 55 : corrections de la contre-lecture CL19 sans décision de Lazar

- Date : 2026-10-31. Auteur : sous-agent neuf de la lignée conv-audit (Claude Opus 5.5), branche `canal/conv-audit-n04`.
  **Non contre-lue** (R2 : à faire par un sous-agent neuf, d'un autre modèle de préférence, avant tout lancement réel).
- Base : la v54 telle quelle (`EMPREINTES-orchestrateur-pole-v7-v54.txt`, 387 empreintes, `sha256sum -c` : 387 OK avant la
  copie et après le travail). **Aucun fichier de la v54 n'est modifié** (R12) : l'arbre v54 est copié, 13 fichiers nouveaux
  et ce LISEZMOI sont ajoutés ; l'essai `test_v55_corrections.TestR12V55` vérifie les 387 empreintes v54 sur l'arbre v55.
- Entrées : contre-lecture CL19 (`../contre-lecture-cl19-orchestrateur-v54-v1.md`, 13 constats, sections A à G) ;
  préenregistrement du pré-pilote, **brouillon 7** (`799b9ca9…` ; A19, A20, A21, O12, S6, table R5, ligne 30) — seul
  fichier de spécification cité ; modules `pole/*_v54.py` touchés.
- Aucun appel payant, aucune clé lue ni cherchée, aucun réseau : essais sous `unshare -n`, boucle locale levée par un petit
  programme hors dépôt (`/tmp/v55smoke/lo.py`, `0b7043a0…`, `ioctl SIOCSIFFLAGS`) ; une connexion vers l'extérieur échoue
  « Network is unreachable ». Moteur simulé et faux relais seulement. Rien lu sous `donnees/`. Rien committé.
- **Aucun seuil n'est fixé dans le code** : le seul nouveau plafond (`prepilote.s6.nombres_ajoutes_max`) et la phrase de
  DEP4 (`dependances.dep4_phrase`) viennent de la configuration, sans défaut.

## Ce qui change (par module)

1. `pole/coffre_v55.py` — `CoffreV55` : lecture par programme d'une clé avant la fin d'É9 **seulement** par
   `lire_pour_garde(nom, rôle, raison)`, pour un couple (nom, rôle) déclaré, journalisée (horodatage UTC, rôle, raison), sortie
   jointe au journal par `noter_sortie_garde` (nombres, booléens, `None` ; tout identifiant refusé). Couple non déclaré :
   incident + `LectureAvantFinE9`.
2. `pole/noyau_v55.py` — mélange `OrchestreV55` : sessions sous `<base>/sessions/<opaque>`, base hors de la sortie (dossier
   temporaire neuf, ou injectée), chemins normalisés et vérifiés ; A2 « modèle servi absent » = arrêt pour tous les rôles ;
   coffre v55 ; dossiers de session **vides** retirés en fin de run (comptés au manifeste ; un dossier qui porte une trace
   est gardé).
3. `pole/course2_v55.py` — `GenerationV55` : rien d'ouvert après un nœud ; déclaration des bras v55 (cause « source
   absente » gardée ; bras méta lu avec I-9 durci) ; `verifier_bascule_gk` (ligne 21) joué avant les lectures d'étiquettes ;
   causes (iii) et (iv) de M9 ; `executer_course_v55`.
4. `pole/prepilote_v55.py` — `PrePiloteV55` : rien d'ouvert après un nœud ; plus de copie de la clé des classes ; deux
   lectures journalisées (É3, É5) ; détail par témoin scellé au coffre ; É6 par identifiant opaque ; É9 réduite par liste
   scellée ; attestation É5bis pour `temoins.version = 2` ; S6 avec bornes et nombres ajoutés ; entrée de rendu gardée
   entière ; relecteur muet = « non relu (technique) ».
5. `pole/gardes_e0_v55.py` — table R5 rejouée (reprise de la v54 ligne à ligne) : statut « sans objet (déclarée) » pour 20
   (source absente) et 22b, 23, 24 (annexe non conforme) ; `_arrete(f, types, motif)` ; artefacts réels pour 1 (modèle
   servi absent), 5, 21, 22b, 30 ; lignes externes vérifiées par sceau, identifiant et script empreinté.
6. `pole/configuration_v55.py` — ligne de GO lue au montant entier ; DEP4 par phrase ; cohérence de D-g ; spécification
   recalculée.
7. `pole/bisociateur_v55.py` — I-9 sur pièces (brouillon relu, rapport) et différence limitée aux deux champs.
8. `pole/etage_entre_generations_v55.py` — noms de clé (CL19-11).
9. `pole/simulation_v55.py` — le metteur simulé n'ajoute plus de nombre au titre (pour que le cas sain du contrôle v55 des
   nombres ajoutés passe).
10. `demonstrations/ideation_v7.py` — lanceur ; sans `--course-2` ni `--pre-pilote`, rend la main au v6 (inchangé), puis v5,
    v4.
11. Essais : `essais/test_v55_corrections.py` (46 essais), `essais/aides_v55.py`, banc `essais/mutations_v55.py`.

## Constat → correction → fichier → essai

| constat | correction | fichier(s) | essai(s) |
|---|---|---|---|
| **CL19-01** A19 refusé au départ | bras Gu-Krenn « non produit (source absente) » déclaré à É0, compté C12 ; ligne 20 « sans objet (déclarée) », départ accepté ; quand la source est là, l'artefact « source à empreinte différente » est rejoué sur la vraie source ; un « non produit » **sans** cause déclarée refuse toujours. A20 : annexe absente → bras méta « non produit (annexe non conforme) », 22b/23/24 « sans objet », sans arrêt | `course2_v55.py`, `gardes_e0_v55.py` | `TestCL19_01SourcesAbsentes` (5 : sain ; source absente, avec la preuve que la v54 refusait ; sans cause : refus ; annexe absente ; lanceur `--verifier-seulement`) |
| **CL19-02** lecture après nœud | au nœud (C13, A5, A6, A7, É5bis…) : ni `declarer_fin_e9`, ni `ouvrir`, ni verdict, ni `analyse-m1.json` / `classement.json` / `memoire.json` / `fiches.json` ; clés de sessions et d'anonymisation déposées (non ouvertes) ; manifeste de fin ; `NoeudArret` (pré-pilote) ou bilan + `NoeudArret` (course) | `prepilote_v55.py`, `course2_v55.py` | `TestCL19_02RienApresNoeud` (4 : sain ; **plafond bas** 25 USD à 2 USD l'appel, nœud à É4 ; nœud É5 ; course) |
| **CL19-03** (partie code) | clé des classes : aucune copie en mémoire après É1 ; deux lectures par programme journalisées au coffre (É3 : exemption A8 de G ; É5 : boîte), comptes seulement ; détail par témoin déposé scellé (`pp2-e5-detail`), ouvert après la fin d'É9 ; `primaires_non_ambigus` supprimé de la sortie ; É6 dans l'ordre des identifiants opaques ; É9 réduite par **liste scellée** (`prepilote.anteriorite.liste_reduite`), clé d'antériorité jamais lue avant la fin d'É9 ; ligne 30 étendue (lecture non déclarée, sortie à identifiants). **L'amendement d'A21 reste à Lazar** (ci-dessous) | `coffre_v55.py`, `prepilote_v55.py`, `gardes_e0_v55.py` | `TestCL19_03CleDesClasses` (5) |
| **CL19-04** sessions voisines du coffre | base hors de la sortie ; refus si la base est sous la sortie, si la sortie est sous la base, ou si le chemin passe par un lien ; depuis une session, `..` ne voit que des sessions, `../..` ne voit que `sessions/` | `noyau_v55.py` | `TestCL19_04Sessions` (3) |
| **CL19-05** GO, DEP4 | montant lu entier (groupes de 3 chiffres séparés par espace, espace fine U+2009, fine insécable U+202F, insécable U+00A0) ; aucun autre nombre que le montant dans la cellule (identifiants de GO et dates ISO retirés) ; « ≈ », « ~ », « environ », « approx » refusés ; « par génération », « par étape » ajoutés aux unités refusées ; DEP4 : phrase de confirmation `dependances.dep4_phrase` exigée dans la pièce | `configuration_v55.py`, `ideation_v7.py` | `TestCL19_05LigneDeGo` (3 ; 6 + 10 sous-essais ; preuve que la v54 lisait 45), `TestLanceurV7.test_ligne_de_go_v55_au_lanceur` |
| **CL19-06** externes par la forme ; version de témoins | résultat externe : pièce **scellée** (compagnon) et à son empreinte, `identifiant` égal à celui déclaré (`prepilote.gardes_externes = {ligne: {piece, identifiant}}`), `script` = nom d'une pièce empreintée dont l'empreinte est citée et recalculée ; ligne 6 : empreinte de l'analyseur si l'analyseur en porte une. `temoins.version = 2` exige la pièce `temoins.sortie_v1` = attestation scellée `temoins-v1-e5bis.json`, écrite par le pré-pilote v55 au nœud É5bis | `gardes_e0_v55.py`, `prepilote_v55.py` | `TestCL19_06Externes` (3) |
| **CL19-07** S6 par sous-chaîne | ancres cherchées avec bornes de mot Unicode ; après un chiffre final, ni « ,d » ni « .d » ; avant un chiffre initial, ni « d, » ni « d. » ; casse et ponctuation gardées (comme la v54) ; nombres du rendu absents du squelette comptés (`nombres_ajoutes`), plafond `prepilote.s6.nombres_ajoutes_max` ; artefacts de la ligne 5 : 12 → 13, 12 → 123, 0,3 → 0,35, couple incomplet, nombre ajouté | `prepilote_v55.py`, `gardes_e0_v55.py` | `TestCL19_07S6` (3 ; 7 sous-essais) |
| **CL19-08** gardes sans leur artefact ; banc | `_arrete(f, types, motif)` ; ligne 21 : déclaration absente à É0 → arrêt, changée après É0 → arrêt (et jouée par la génération) ; ligne 22b : annexe absente, non contre-lue, à empreinte différente (lecture réelle sur copie) ; banc : fabrique qui fournit `__class__`, et **raison** de chaque échec vérifiée par motif | `gardes_e0_v55.py`, `course2_v55.py`, `mutations_v55.py` | `TestCL19_08Artefacts` (4), `TestBancMutationsV55` |
| **CL19-09** I-9 de forme ; spécification | brouillon relu et rapport = pièces (`bisociateur.meta.annexe.brouillon_relu`, `.rapport_contre_lecture`), empreintes recalculées et citées ; `R-0…0` refusé ; annexe = brouillon relu sauf `contre_lecture` et `approbation_lazar` ; tout écart : A20 (non produit), pas un arrêt. Spécification recalculée au lancement : exigée conforme pour le moteur réel | `bisociateur_v55.py`, `course2_v55.py`, `configuration_v55.py`, `ideation_v7.py` | `TestCL19_09Annexe` (3) |
| **CL19-10** écarts | A2 « modèle servi absent » : arrêt pour tous les rôles, artefact à la ligne 1 ; causes (iii) « moins de 2 fiches étiquetées » (méta) et (iv) « moins de 2 fiches notables » (Gu-Krenn) ; autres écarts **déclarés** ci-dessous | `noyau_v55.py`, `course2_v55.py`, `gardes_e0_v55.py` | `TestCL19_10Ecarts` (3) |
| **CL19-11** machine jetable | `GH_PAT` (`*_PAT`), `*_KEY_*`, `SSH_AUTH_SOCK`, `AUTH`, `*_AUTH` refusés ; `TOKENIZERS_PARALLELISM` accepté (liste fermée `NOMS_SANS_SECRET`) | `etage_entre_generations_v55.py` | `TestCL19_11MachineJetable` (8 sous-essais) |
| **CL19-12** mineurs | entrée de rendu gardée entière (consigne comprise) ; relecteur sans sortie = « non relu (technique) » : ni ambigu, ni « défaut non vu », hors S20, hors A5, non jugé, compté ; `decisions_a15.d_g` doit désigner la même lettre que `prepilote.d_g` ; boîte d'É5 sans liste par classe (CL19-03) ; « bisociative » / « bisociation » : affaire de la liste injectée (configuration), non du code | `prepilote_v55.py`, `configuration_v55.py` | `TestCL19_12Mineurs` (3) |
| **CL19-13** couverture | essais ajoutés : pré-pilote en nœud, A19 à É0, S18 dans le flux (effectif minimal d'essai abaissé), reprise après A8 réussie | `test_v55_corrections.py` | `TestCL19_13Couverture` (2), `TestCL19_02…`, `TestCL19_01…` |

## Décisions ouvertes pour Lazar

### CL19-03 — A21 et la ligne 30 face au Plan d'É5 (la question de fond)

Le brouillon 7 se contredit : A21 interdit « l'ouverture de la clé des classes […] avant la fin d'É9, par quiconque » et la
ligne 30 dit « les clés restent scellées » ; le Plan exige en É5, « avant tout juge », S6 (défaut vu), S20/A6 et S18/S19/A7,
impossibles sans la classe de chaque témoin (et l'exemption A8 de la classe G en É3). La v55 rend la lecture **visible et
bornée** (journal du coffre, rôle déclaré, raison, comptes seulement, aucune copie) mais ne la supprime pas.

- **Lecture 1 — amender A21 et la ligne 30 (brouillon 8)** : « lecture par programme de la clé des classes à É3 (A8) et à É5
  (S6, S18, S19, S20, A5 à A7), journalisée au coffre, sortie limitée à la décision et à des comptes ; jamais par un agent ni
  une personne » ; l'artefact de la ligne 30 couvre « lecture hors journal ». C'est ce que fait la v55 (défaut de CL19).
  Avantage : rien à construire. Inconvénient : A21 n'est plus vrai à la lettre ; l'aveugle repose sur le code.
- **Lecture 2 — ne jamais livrer la clé à l'orchestrateur** : la boîte d'É5 (et l'exemption A8) devient un programme tenu
  par session-depot, qui détient la clé et rend « passe / nœud + comptes » ; A21 reste vrai à la lettre. Avantage : aucune
  exception. Inconvénient : une pièce de plus, une interface de plus, à éprouver (cas sain, artefact).
- Recommandation de CL19 (0,7) : lecture 1 + journal + liste d'É9 scellée + ordre d'É6 trié — tout ce qui est code est fait
  ici. Défaut de CL19 si aucune réponse : comportement de la v55 (journalisé).

### Choix de CL19, section G, à trancher

| n° | choix (v54, inchangé en v55 sauf mention) | enjeu |
|---|---|---|
| 1 | Nœud : arrêt au premier « non mesuré ». **Second membre corrigé** : plus de fin de phase de mesure ni de classement au nœud (CL19-02, lecture O12 « rien n'en a été lu ») | confirmer que le nœud ne produit aucune lecture, et que le rejeu O12 se fait sur GO |
| 4 | Clé des classes lue par programme (É3, É5) — voir CL19-03 ; **É9 ne lit plus la clé d'antériorité** (liste scellée de session-depot) | A21 ; qui écrit la liste d'É9 (session-depot, tâche `pp2-reduction-e9`) |
| 5 | Un N dont le relecteur ne voit pas le défaut est **exclu** (compte pour A5) | change l'ensemble des témoins ; le brouillon ne dit pas que « défaut non vu » est une exclusion |
| 8 | I-8 : à n = 2, aucun report au bras suivant | change les probabilités de C12 ; à écrire au brouillon 8 |
| 10 | Indices de forme (longueur, chiffres, nombre de champs) et crête injectée | S18/S19 sont des critères d'arrêt (A7) : définition et crête à geler au préenregistrement |

### Autres points qui demandent un mot de Lazar (nouveaux ou signalés par CL19)

- **S6, nombres ajoutés** (`prepilote.s6.nombres_ajoutes_max`) : critère recommandé par CL19-07, absent du texte de S6 ;
  valeur à geler (les essais utilisent 0).
- **DEP4, phrase de confirmation** (`dependances.dep4_phrase`) : texte à fixer avec session-depot.
- **I-2** : désaccord lu sur au plus `paires_max` paires (le brouillon dit « chaque paire candidate », CA1-10).
- **A14 sur petits effectifs** (choix 2, signalé par CL19) : un seul appel inexploitable de l'adjudicateur ou du relecteur
  peut dépasser 25 %.
- **Relecteur sans sortie** (pris seul en v55, ci-dessous) : « non relu (technique) », hors A5 ; A14 garde la part technique.
- I-11 (paires déjà prises retirées, non chiffré par P14) et I-13 (dépense du désaccord absente du devis) : à l'annexe v2 ou
  au script de puissance ; non traités, non revendiqués.

## Écarts au brouillon 7, déclarés (CL19-10)

- Tâches de graines hors de la liste du brouillon : `pp2-ident-fond-<n>`, `pp2-ident-<passe>-<case>-<proposeur>-<k>`,
  `pp2-ident-fusion-<n>`, `pp2-anonymisation-<juge>-<fiche>` (le brouillon liste `pp2-anonymisation` seul), `pp2-paraphrases`.
  `pp2-reduction-e9` n'est plus tirée par l'orchestrateur : c'est la tâche de session-depot qui écrit la liste scellée d'É9.
- Désaccord : texte servi = champ `champ_affirmation` de la fiche ; la recopie du lecteur est conservée, non utilisée.
- M7 : jetons « non lus (l'adaptateur ne les rend pas) » au journal de consommation.
- Fiches d'antériorité et de M6b : lues comme **pièces** (le brouillon dit « rédacteur, É1 ») ; leur coût n'est donc pas dans
  É1.
- A15 : décisions et montant contrôlés par le **lanceur** ; `PrePiloteV55` appelé directement n'en vérifie rien (déclaré).

## Choix pris seuls en v55 (à confirmer)

1. Base des sessions : dossier temporaire neuf par génération ou pré-pilote (`pole-sessions-v55-…`), racine injectable ;
   dossiers vides retirés en fin de run, dossiers à traces gardés et leur base écrite au manifeste et au coffre.
2. A2 « modèle servi absent » : arrêt (pas « inexploitable ») pour tous les rôles.
3. Relecteur sans sortie : témoin « non relu (technique) », hors S20, hors A5, non jugé en É6, compté (`non_relus`).
4. Liste d'É9 : pièce `{"idents": [...]}` scellée, longueur = somme de `anteriorite.reduite`, identifiants distincts des fiches.
5. Attestation É5bis : `{version, version_temoins_epuisee: 1, noeud: "É5bis", configuration_sha256}`, scellée dans la sortie.
6. `NOMS_SANS_SECRET` = { `TOKENIZERS_PARALLELISM` } (liste fermée, code).
7. Exclusions par la boîte d'É5 : motif générique au manifeste (« exclu par la boîte d'É5 (motif scellé au coffre) ») ;
   détail au coffre.

## Essais

Machine : Python 3.13.18, numpy 2.5.3, pytest 9.1.1 ; `bwrap` absent ; superutilisateur ; `unshare -n` + boucle locale levée ;
`env -i PATH=/usr/bin:/bin:/usr/local/bin HOME=/tmp LANG=C.UTF-8 POLE_ESSAI_BAC_REEL_NON_JOUE=1 python3 -B -m pytest essais -q
-p no:cacheprovider`, dans le dossier de livraison.

- **v55 seule** (`test_v55_corrections.py`) : **46 essais, 46 OK, 36 sous-essais**. Avec les essais v54 (`test_v54_*`) :
  **115 OK, 79 sous-essais**.
- **Suite entière** : **709 réussis, 12 ignorés (« ESSAI RÉEL NON JOUÉ »), 1 échec, 461 sous-essais** (4 min 28 s).
  L'échec est `test_v51_bac_reel.py::test_v51_06` (« bwrap absent »), préexistant, déterministe sans `bwrap`, nommé par CL18
  et CL19. 709 = 663 (comptes de la v54, inchangés) + 46.
- Sans la boucle locale levée (simple `unshare -n`), 29 essais anciens de plus échouent (relais local) : à ne pas confondre.
- Après la suite : `conftest` (v54) retire `essais/_tmp` vide laissé par `TestV46` ; aucun `__pycache__`, aucun
  `.pytest_cache`, aucun `essais/_tmp` ; aucun dossier `pole-sessions-v55-*` ni `pole-mutations-*` laissé dans `/tmp`.

## Banc de mutations (`essais/mutations_v55.py`)

`python3 -B essais/mutations_v55.py` (mêmes conditions) : **témoin 106 essais, 0 en échec ; 103 mutations (56 de la v54, sur le
code et les essais v54 ; 47 de la v55) ; 103 tuées pour la raison attendue ; 0 tuée pour une autre raison ; 0 défaut du
banc ; 0 survivante ; 0 non appliquée ; témoin après restauration 106 essais, 0 en échec.**

- `super()` : le source muté est compilé dans `def __fabrique_mutation__(__class__): …` appelée avec la classe qui définit la
  méthode ; « DEP3 analyseur non exigé » est maintenant tuée par `EtageUnAbsent not raised` (et non plus par « __class__
  cell not found ») ; `TestBancMutationsV55` le vérifie.
- Raison : chaque mutation porte un motif (texte d'assertion, ligne de source de l'essai ou nom du sous-essai) ; classement
  « tuée » / « tuée pour une autre raison » / « défaut du banc » / « survivante ». Au premier passage : 8 « autre raison »
  (motifs v54 mal anticipés : vérifiés à la main un par un, échecs légitimes, motifs corrigés), 1 survivante (« extension
  décimale » : l'essai ne la couvrait pas — cas « 12.5 » et « 12,5 » ajoutés, ce qui a révélé que le contrôle passait par une
  normalisation qui effaçait la ponctuation : corrigé), 1 essai qui échouait pour une raison étrangère (dépôt absent :
  corrigé), 2 fragments mal indentés (corrigés). Les motifs génériques (« AssertionError ») ont ensuite été resserrés sur la
  ligne d'assertion réelle.
- Mutations v55 : CL19-01 (3), 02 (3), 03 (9), 04 (3), 05 (5), 06 (4), 07 (4), 08 (4), 09 (4 dont la spécification au
  lanceur), 10 (3), 11 (2), 12 (3).

## Réserves

- **Non contre-lue (R2).** **Jamais lancée sur moteur réel.** Contrats de sortie des rôles du pré-pilote non éprouvés (réserve
  v54 inchangée).
- Sessions : la base est hors de la sortie et sans voisin à deux niveaux, mais un agent qui lit tout le système de fichiers
  atteint la sortie par chemin absolu ; l'isolement réel reste celui du bac (`bwrap`) sur la machine du run.
- Lecture de la clé des classes par programme : visible et bornée, pas supprimée (décision CL19-03).
- Le contrôle des résultats externes vérifie le sceau, l'identifiant et l'empreinte d'un script ; il ne peut pas prouver que
  le script a réellement produit le résultat (pièce à produire et à faire contre-lire avec chaque script).
- Le contrôle de la spécification au lancement suppose l'arbre dans le dépôt (la spécification est cherchée en remontant
  depuis le lanceur) ; hors du dépôt, le moteur réel est refusé.
- Machine jetable : contrôle déclaratif (inchangé).

## Ce qui reste

1. Contre-lecture R2 de la v55.
2. Décisions de Lazar : CL19-03 (lecture 1 ou 2), choix 1, 4, 5, 8, 10, points ci-dessus ; S1 à S31, D-e à D-j, L1 à L7 ;
   clés configurables de la v54 ; valeur de `prepilote.s6.nombres_ajoutes_max` ; phrase de DEP4.
3. Pièces : analyseur de l'étage 1 (DEP3) ; résultats scellés des lignes 8, 9, 10, 17, 19 avec leurs scripts empreintés ;
   liste de réduction d'É9 (session-depot) ; consignes figées au contrat ; fiches d'antériorité et clé, fiches et sources de
   M6b ; source de S31 ; annexe du bras méta contre-lue et approuvée, avec brouillon relu et rapport en pièces ; DEP4.
4. Code d'analyse (inchangé : intervalles, t*, M3, M5, M6, verdict par instrument).
5. Étage réel sur la machine jetable sous vrai `bwrap` (`test_v51_06`, `test_v52b_02`).

## Fichiers nouveaux (rôle, empreinte)

Voir `EMPREINTES-orchestrateur-pole-v7-v55.txt` (tout l'arbre sauf elle-même et son compagnon) ; code :
`CODE-orchestrateur-pole-v7-v55.zip` (`conception-v7-v1.md`, `demonstrations/`, `essais/`, `exemples/`, `pole/`).

| fichier | rôle | SHA-256 |
|---|---|---|
| `pole/coffre_v55.py` | lectures par programme journalisées (CL19-03) | `ef10fe044608fda51d5cd4b3b855da677845be83d1367ca3aa33fe45337e33fd` |
| `pole/noyau_v55.py` | sessions hors de la sortie, A2, coffre v55 | `ca0f2dda980777da9c549519c6b15994309722353b22f88d117e95aa2c2d4035` |
| `pole/course2_v55.py` | génération et course : nœud, bras, ligne 21, causes | `ee6a861e7f8db32a9545372a51f902389cdbea809b0ba354e621a3681e541a70` |
| `pole/prepilote_v55.py` | pré-pilote : nœud, clé, S6, É6, É9, É5bis | `e91e07e4f3bf67cd5106129586048abb3b06284eb9812f8e4da4082087859f05` |
| `pole/gardes_e0_v55.py` | table R5 v55 | `e46c5cd0a301c89830d97c098ee52b33ead6b01cafe15ab8454e6b7957c54db1` |
| `pole/configuration_v55.py` | GO, DEP4, D-g, spécification | `2e6237c0a8b1c823fa17ddd6c680357a59ec4030bfbe9ac6ba970a700a864071` |
| `pole/bisociateur_v55.py` | I-9 sur pièces | `d9521311a96384494871e9f9fcd4b4554548b9f45fdc28e8e75ca30d4c54d22f` |
| `pole/etage_entre_generations_v55.py` | noms de clé | `865bd7e5734618a2e989bdd14726ff7db53e014963cbc93b48be1892c7ab4dd9` |
| `pole/simulation_v55.py` | moteur simulé (titre sans nombre) | `91ac1c345c3670dd232b0c1da63825608aac1a840192639dd01e7fb175efbf4f` |
| `demonstrations/ideation_v7.py` | lanceur | `7b90e65e1308b1c230b3f804743cfc42b9dc571d93b73ed6c5f3f8c9d2b481b2` |
| `essais/aides_v55.py` | configurations d'essai v55 (valeurs d'essai seulement) | `ad7a4c11a1f0f9ca672a7579bf6566ae27a35f7004052614834a92703984e254` |
| `essais/test_v55_corrections.py` | 46 essais | `9a06fee98039aa281e647caefb47c9d34a0e9bc87b7708b00047e4a5093f04fa` |
| `essais/mutations_v55.py` | 103 mutations, raison vérifiée | `3026b0698cc6ff5318fc5a72820bb0a4752ea794961a25a398684ab319c6ef03` |

## Lancement

```
python -I -B demonstrations/ideation_v7.py --course-2 CONF.json SORTIE_NEUVE --generations N --verifier-seulement
python -I -B demonstrations/ideation_v7.py --course-2 CONF.json SORTIE_NEUVE --generations N --moteur simule
GO_ID=GO-AAAA-MM-JJ-NN python -I -B demonstrations/ideation_v7.py --course-2 CONF.json SORTIE_NEUVE --generations N \
    --moteur reel --registre-go registres/go.md --confirmer-moteur-reel
python -I -B demonstrations/ideation_v7.py --pre-pilote CONF.json SORTIE_NEUVE --verifier-seulement   # refus DEP3 tant
                                                                                                        # qu'aucun analyseur n'existe
```

Clés de configuration ajoutées à celles de la v54 : `bisociateur.meta.annexe.{brouillon_relu, rapport_contre_lecture}`
(`{chemin, sha256}` ; absentes → bras méta non produit, A20) ; `prepilote.s6.nombres_ajoutes_max` ;
`prepilote.anteriorite.liste_reduite` (pièce scellée) ; `prepilote.temoins.sortie_v1` (si `version = 2`) ;
`prepilote.gardes_externes = {ligne: {piece, identifiant}}` ; `dependances.dep4_phrase` (moteur réel). Forme complète :
`essais/aides_v55.py`.
