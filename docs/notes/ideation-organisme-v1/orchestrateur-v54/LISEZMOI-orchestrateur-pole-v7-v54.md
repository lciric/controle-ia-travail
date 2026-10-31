# Orchestrateur du pôle, v7 — version 54 : corrections de CL18, annexe du bras méta, étapes du pré-pilote

- Date : 2026-10-31. Auteur : sous-agent neuf de la lignée conv-audit (Claude Opus 5.5), branche `canal/conv-audit-n04`.
  **Non contre-lue** (R2 : à faire par un sous-agent neuf, d'un autre modèle de préférence, avant tout lancement réel).
- Base : la v53 telle quelle (`EMPREINTES-orchestrateur-pole-v7-v53.txt`, 361 empreintes, `sha256sum -c` : 361 OK avant la
  copie). **Aucun fichier de la v53 n'est modifié** (R12) : l'arbre v53 est copié, 22 fichiers nouveaux et ce LISEZMOI sont
  ajoutés ; l'essai `test_v54_prepilote.TestR12` vérifie chaque empreinte de la liste v53 sur l'arbre v54.
- Entrées : contre-lecture CL18 (`../contre-lecture-cl18-orchestrateur-v53-v1.md`, 17 constats) ; annexe du bras méta,
  brouillon 1 (`brouillons/…/pre-pilote-course-2-v1/annexe-bras-meta-v1-brouillon1.md`, compagnon conforme), section 10
  (I-1 à I-10) et section 8 (format du bloc) ; préenregistrement du pré-pilote, **brouillon 7** (`799b9ca9…`, compagnon
  conforme ; Plan, Liste d'arrêt, table R5) — **seul fichier de spécification cité par la v54** (CL18-09) ;
  `registres/go.md` (format des lignes) ; `.claude/hooks/garde_calcul.py`.
- Aucun appel payant, aucune clé lue ni cherchée, aucun réseau : essais sous `unshare -n` (seule la boucle locale est levée
  par un petit programme hors dépôt, `ioctl SIOCSIFFLAGS`, faute de commande `ip` ; un essai de connexion vers l'extérieur
  échoue « Network is unreachable ») ; moteur simulé et faux relais seulement. Rien lu sous `donnees/`. Rien committé.
- **Aucun seuil n'est fixé dans le code** : toute valeur (y compris les choix de code remontés à Lazar) vient de la
  configuration ; « À REMPLIR » ou une clé absente refusent le départ avant tout appel.

## Ce qui change

1. **Noyau commun** (`pole/noyau_v54.py`) : tout appel passe par `Orchestre.appel` (consommation notée au coffre dans un
   `finally`, pire cas si l'adaptateur lève ; durée, modèle servi, statut) ; coupure de budget marquée ; A3, A11, A14 par
   rôle ; passeport sur empreinte recalculée ; garde A4 configurable sur la fiche puis sur l'entrée complète ; sessions
   opaques ; juges croisés sous ce noyau.
2. **Course 2** (`pole/course2_v54.py`) : mêmes six étapes, mais paires choisies dans l'étape protégée `etiquettes` (avec S24,
   S28, puis lecture du désaccord) ; `fusions` n'écrit plus que les fusions ; **nœud** au premier « non mesuré » ; paires
   par bras au coffre (plus au manifeste de fin) ; tâches de graines au préfixe injecté.
3. **Pré-pilote** (`pole/prepilote_v54.py`) : plan É1 à É9b du brouillon 7, rôles imposés (protégées, sacrifiables,
   réductible, protégée hors porte), étapes incluses selon L1, L2, D-g ; É5 (boîte : ambigus, S6, S20/A6, S18/S19/A7) ;
   fin de la phase de mesure **après É9 et É9b** ; M1 calculée après la fin.
4. **É0** (`pole/gardes_e0_v54.py`) : la table R5 est rejouée en mémoire avant tout appel (lanceur, `--verifier-seulement`
   compris) ; une ligne exigée non rejouée refuse le départ (A12).
5. **A15** (`pole/configuration_v54.py`) : ligne de GO au montant **exact**, un seul montant, pas « par lancement » ; DEP4 en
   pièce empreintée ; décisions d'A15 au pré-pilote.
6. **Bras méta** (`pole/bisociateur_v54.py`) : I-1 à I-10 (table ci-dessous) ; lecture du format réel de l'annexe.
7. **Mesures** (`pole/mesures_v54.py`) : kappas « non définis » sur marges constantes ; verdicts absents ; S18/S19 (régression
   logistique, validation croisée par fond, aire de Mann et Whitney) ; S20.
8. **Lanceur** `demonstrations/ideation_v6.py` : `--course-2 … --generations N` ou `--pre-pilote …` ; sans ces options, rend la
   main au lanceur v5 (inchangé), qui la rend au v4.
9. **Essais** : `conftest.py` redirige les dossiers temporaires hors de l'arbre et coupe le cache d'octets (CL18-15).

## Constat → correction → fichier

| constat | correction | fichier(s) | essai(s) |
|---|---|---|---|
| CL18-01 journal incomplet | une consommation par appel, juges compris, dans un `finally` ; pire cas sur exception ; rejeu `rejouer_consommations` sur **la vraie sortie du coffre** comparé au journal réel du budget (cas sain et cas coupé) | `noyau_v54.py`, `budget_v54.py` | `TestCL18_01JournalComplet` (4) |
| CL18-02 protégée coupée « jouée » | marque `coupure` (montant 0) au journal ; `apres_etape(…, coupee)` ; `cumul ≥ plafond − EPS` ; nœud : génération arrêtée, course arrêtée (`NoeudArret`, bilan écrit) | `noyau_v54.py`, `budget_v54.py`, `course2_v54.py` | `TestCL18_02CoupureEtNoeud` (3) |
| CL18-03 A15 laxiste | un seul montant, USD, égal au requis ; « par lancement », plusieurs montants, autre monnaie, identifiant non exact refusés ; lignes reconstituées au format du registre (sans lire son contenu réel) | `configuration_v54.py` | `TestCL18_03LigneDeGo` (3, 10 sous-essais) |
| CL18-04 pré-pilote non jouable | plan É1–É9b ; A3, A11, A14 ; rejeu R5 à É0 ; DEP4 ; fin d'É9 après É9b ; squelettes qui refusent (ci-dessous) | `prepilote_v54.py`, `suivi_roles_v54.py`, `gardes_e0_v54.py`, `bras_attaque_v54.py` | `test_v54_prepilote.py` (22) |
| CL18-05 passeport nominal | empreinte recalculée à chaque contrôle | `noyau_v54.py` | `TestCL18_05Passeport` |
| CL18-06 A4 pluriels ; arrêt sur mot légitime | `a4.mode` (préfixe) ; `a4.action` (arrêt ou fiche exclue, comptée) | `fiches_v54.py`, `noyau_v54.py` | `TestCL18_06A4` (3) |
| CL18-07 noms de tâches | préfixe injecté ; `pp2-bisoc-ordre` (bras puis fusions, même générateur), `-gk`, `-meta`, `-n`, `-anonymisation-…`, `-classes-axes`, `-indices`, `-fournisseurs`, `-partition`, `-reduction-e9` ; **tâche ajoutée déclarée** : `pp2-paraphrases` | `course2_v54.py`, `prepilote_v54.py` | `TestCL18_07Graines`, pré-pilote sain |
| CL18-08 entrée du bisociateur ; passe « tableau » jugée | `bisociateur.fournisseurs_entree` ; `tableau.juger_passe_tableau` | `course2_v54.py` | `TestCL18_08Lectures` |
| CL18-09 brouillon 6 cité | brouillon 7 seul cité (chemin et empreinte vérifiés) ; DEP4 = pièce exigée au lancement réel | `configuration_v54.py` | `TestCL18_09Specification` (2) |
| CL18-10 garde de Kimi | `garde_kimi.refus_aiguilleur` ; `garde_kimi.arret_metteur_fusion` | `noyau_v54.py`, `course2_v54.py` | `TestCL18_10GardeKimi` (2) |
| CL18-11 plafond par génération | `budget.portee_plafond` ; `montant_requis` | `configuration_v54.py` | `TestCL18_03LigneDeGo` |
| CL18-12 fuites par les chemins | dossiers de session opaques (correspondance au coffre) ; nature « vocabulaire » ; A4 sur l'entrée complète | `noyau_v54.py`, `course2_v54.py`, `fiches_v54.py` | `TestCL18_12Fuites` (2) |
| CL18-13 machine jetable | `POLE_MACHINE_JETABLE_V54` ; noms contenant SECRET, TOKEN, PASSWORD, PASSWD, CREDENTIAL, API_KEY, ACCESS_KEY, PRIVATE_KEY ou finissant par `_KEY` refusés | `etage_entre_generations_v54.py` | `TestCL18_13MachineJetable` |
| CL18-14 kappas dégénérés | `None` (« non défini ») ; verdicts absents retirés et comptés | `mesures_v54.py` | `TestCL18_14Accords` (2) |
| CL18-15 essais | essais ajoutés (trois paires à n = 2, A18 en génération, kappas) ; commentaire faux non recopié ; `conftest.py` | `essais/` | `TestCL18_15Essais` (3) |
| CL18-16 cumul écrêté ; M6b coupée | cumul réel, dépassement au journal ; M6b coupée → « non mesurée hors porte », C13 inchangée (lecture du brouillon 7, M6b) | `budget_v54.py` | `TestCL18_16Budget` |
| CL18-17 héritage ; n global ; `KeyError` | héritage sous A4 ; n par case ; départage absent refusé nommément | `course2_v54.py`, `bisociateur_v54.py` | `TestCL18_17Heritage` (2) |
| I-1 noms de structures | identifiant de la liste fermée **et** nom = identifiant ; refus compté (`refus_lectures`) | `bisociateur_v54.py` | `TestI1NomsDeStructures` (2) |
| I-2 désaccord | lu par paire après le dépôt scellé des paires (paire retenue puis suivantes, `paires_max`), deux lecteurs, journal au coffre, ordre vérifié ; garde par valeur (`desaccord`, `d`, `**kw`) ; affirmation centrale du lecteur conservée | `bisociateur_v54.py`, `course2_v54.py` | `TestI2Desaccord` (3) |
| I-3 S28 | calculé (`accords.json`) ; seuils de l'annexe ou de la configuration (`bisociateur.meta.s28`) | idem | `TestI3S28` (2) |
| I-4 définitions | `bisociateur.meta.definitions` : `annexe` (servies au lecteur) ou `consigne` (identifiants vérifiés dans la consigne figée) | idem | `TestI4Definitions` (2) |
| I-5 divergence | `regle_divergence`, `structures` configurables | idem | `TestI5Divergence` |
| I-6 types et signes | contrôles de types, poids ≥ 0, `nombre_min` ≥ 1, types ⊆ grille | `bisociateur_v54.py` | `TestI6Types` (7 sous-essais) |
| I-7 causes C12 | « niches indistinctes sur ce lot », « aucune paire éligible », comptées (`c12`) | `bisociateur_v54.py`, `course2_v54.py` | `TestI7I8Paires` |
| I-8 n = 2 | bras de priorité 1 seul ; sans note : sa cause, les autres « effectif » | `bisociateur_v54.py` | `TestI7I8Paires` |
| I-9 contre-lecture, approbation | deux SHA-256 distinctes ; `R-NNN` | `bisociateur_v54.py` | `TestI9I10Annexe` |
| I-10 non-vacuité à É0 | bloc `jeu_essai_non_vacuite` de l'annexe rejoué (dans le profil, hors profil, argmax) ; sinon A20 | `bisociateur_v54.py`, `course2_v54.py` | `TestI9I10Annexe`, `TestAnnexeReelle` |
| format réel de l'annexe | le brouillon 1 est refusé (« À REMPLIR ») ; une copie remplie est acceptée ; la vraie fonction retrouve **5 / 36 / 4, argmax e01–e04 à 2,0** (chiffres de l'annexe, section 6) | — | `TestAnnexeReelle` |

## Étapes du pré-pilote codées, et squelettes qui refusent (CL18-04)

Codé : plan des fonds (tirages R9, contraintes injectées) ; É1 rédacteur (squelettes de 12 à 16 ancres et couples, déclarations
contrôlées par programme, produits du rédacteur : difficiles, voisines, axe 7) ; É2 ; É3 rendus (consigne neutre, S6 ancres et
couples, A8, une reprise, A5) ; É4 aiguilleur (rendus, passe 1, difficiles) et second lecteur ; É5 relecteur, S6 « défaut vu »,
S20/A6, S18/S19/A7, nœud É5bis ; É6 ; É7a (tableau, passe, aiguilleur, second lecteur, adjudicateur sur les désaccords) ; É7b ;
É7c (étage 1 sur les fusions) ; É7d (table seule) ; É8 (paraphrases, bardeaux PB, NA, NB ; t* laissé à l'analyse) ; É9 (réduite
par tirage stratifié) ; É9b (garde 31) ; A13 (squelettes et témoins revérifiés).

Ne part pas sans décision ou pièce (refus, motif exact, aucun repli) :

| quoi | refus | motif |
|---|---|---|
| analyseur de l'étage 1 (DEP3) | `EtageUnAbsent` (lanceur et `PrePiloteV54`) | aucun analyseur n'existe ; un objet injecté (`signaler`, `cas_sain`, `artefact`) est exigé ; les essais injectent un faux |
| lots du bras d'attaque (12 concrets) | `bras_attaque_v54.refuser_lots` si `prepilote.concrets` est posé | interface de service par session-depot non spécifiée ; DEP5 « À REMPLIR » ; sans lot : M4 « non étalonné (sans témoins concrets) » |
| lignes R5 6 (sans analyseur), 8, 9, 10, 17, 19 | `GardesE0Refusees` (A12) | non rejouables par l'orchestrateur ; acceptées depuis un résultat externe scellé et empreinté (`prepilote.gardes_externes`) |
| seconde version de témoins (É5bis) | `NoeudArret` « relancer avec `temoins.version = 2` » ; à la version 2 : « C5 non satisfaite » | replanter des témoins demande un nouveau run du rédacteur |
| lancement réel du pré-pilote | `decisions_a15` (confidentialité, D-f, D-g à D-j, GO de lancement) et DEP4 | A15 du brouillon 7 |
| mode « modèle » de Gu et Krenn ; plongement de M3 | refus v53 inchangés | non fournis |

## Choix de code

Remontés à Lazar, **configurables** (« À REMPLIR » refusé) : choix 1 `budget.portee_plafond` ; choix 6
`garde_kimi.refus_aiguilleur` ; choix 7 `garde_kimi.arret_metteur_fusion` ; choix 10 `bisociateur.meta.regle_divergence` et
`.structures` ; choix 11 `tableau.juger_passe_tableau` ; CL18-08 a `bisociateur.fournisseurs_entree` ; CL18-06 `a4.mode`,
`a4.action` ; CL18-07 `graines.prefixe` ; I-2 `bisociateur.meta.desaccord` ; I-3 `.s28` ; I-4 `.definitions` ; A3, A11, A14
`arrets.*` (les valeurs du brouillon — 3 échecs, 300 s et 1 800 s, 25 % — sont des valeurs de configuration, jamais du code).

Pris seuls (à confirmer) :
1. Nœud : la génération (et le pré-pilote) s'arrêtent au premier « non mesuré » ; les étapes suivantes ne sont pas lancées ;
   la fin de la phase de mesure et le classement sont faits quand même (0 USD).
2. A3 : un appel au-delà de son délai n'est jamais lu, même s'il a rendu un texte. A11 : la « limite hebdomadaire » arrête le
   rôle en attente (aucune attente réelle, aucune bascule). A14 : part cumulée sur le run, lue à la fin de chaque étape, pour
   les rôles appelés dans l'étape.
3. Pré-pilote : la garde de Kimi de la course (arrêt au-dessus de S12) n'est pas jouée ; M5 est une mesure lue après É9.
4. É5 lit la clé des classes **par programme** (ambigus, S19, défaut vu) ; seules la décision et des comptes en sortent (coffre).
   É9 réduite lit les strates de la clé d'antériorité par programme pour le tirage stratifié. À trancher par Lazar (A21).
5. É5 : un N dont le relecteur ne voit pas le défaut est exclu (A5, S6) ; pas de nouveau rendu à ce stade.
6. Adjudicateur de M5 : joué en É7a seulement ; si É7a est retirée ou L1 = « retirée », M5 se lit sur l'union et l'intersection.
7. I-9 : deux empreintes distinctes exigées dans `contre_lecture` (brouillon relu et rapport, annexe § 9.5).
8. I-8 : à n = 2, aucun report au bras suivant (lecture littérale du brouillon ; remplace le choix 9 de la v53).
9. Multi-cases à n_max = 2 (course) : une seule paire en tout, la mieux notée du bras de priorité 1.
10. Indices de forme : longueur et chiffres sur le texte des valeurs de la fiche ; nombre de champs = champs du contenu ;
    régression avec pénalité de crête injectée (`controles_forme.ridge`).
11. Paraphrases d'É8 choisies par la tâche `pp2-paraphrases` (absente de la liste du brouillon 7 : écart déclaré).
12. Une « coupure » rencontrée dans une étape sacrifiable la retire (même si une partie a été jouée).

## Essais

Machine : Python 3.13.18, numpy 2.5.3, pytest 9.1.1 ; `bwrap` absent ; `unshare -n` (boucle locale levée) ;
`env -i PATH=/usr/bin:/bin:/usr/local/bin HOME=/tmp LANG=C.UTF-8 python3 -B -m pytest essais -q -p no:cacheprovider`, dans le
dossier de livraison (les essais R12 lisent `../EMPREINTES-orchestrateur-v52b.txt` et la liste v53 de la livraison).

- **v54 seule** (`test_v54_*`) : **69 essais, 69 OK, 43 sous-essais** (corrections 31, annexe 16, pré-pilote 22). Avec les 56
  essais de la v53 : 125 OK.
- **Suite entière, sans variable** : **676 essais : 663 OK, 13 en échec** — exactement les 13 de la v53 sur une machine sans
  `bwrap` (`test_v51_01, 02, 04, 05, 06, 08, 11, 12`, `test_v52b_02`, `test_v48_22`, `test_v49_19`, `test_v50_15`, `test_v50_16`,
  CL15-04 : échec voulu sans bac réel).
- **Suite entière avec `POLE_ESSAI_BAC_REEL_NON_JOUE=1`** : **663 OK, 12 ignorés (« ESSAI RÉEL NON JOUÉ »), 1 échec**
  (`test_v51_06`, déterministe sans `bwrap`, préexistant, CL18 section F).
- Remarque : sous `unshare -rn` (espace utilisateur) 7 essais anciens de plus échouent (`test_v51_03, 05, 13`, `test_v50_02, 04,
  05, 06` : `setpriv`, identités) ; les comptes ci-dessus sont sous `unshare -n` en superutilisateur, comme CL18.
- **Mutations en mémoire** (`essais/mutations_v54.py`, aucun fichier modifié : la fonction visée est recompilée avec un
  fragment remplacé et substituée dans les modules chargés, puis restaurée) : **56 mutations, 56 tuées**, témoin 64 essais OK
  avant et après. Elles couvrent chaque garde nouvelle : CL18-01 (2), 02 (3), 03 (4), 05, 06 (2), 08 (2), 10 (2), 12 (2), 13,
  14 (2), 16 (2), 17 (2), I-1, I-2 (2), I-3, I-4 (2), I-5, I-6 (2), I-7, I-8, I-9 (2), I-10 (2), A3 (2), A11 (2), A14, A5,
  S6, A8, A6, A7, A13, ligne 31, refus d'É0, DEP3, DEP4, plan du pré-pilote. Six survivantes au premier passage (marque de
  coupure, I-6 ×2, I-10 ×2, DEP4) : les essais passaient **par une garde suivante** ; ils vérifient maintenant le motif exact.
- Plus aucun `essais/_tmp/` ni `__pycache__/` : redirection par `conftest.py` ; reste connu : `TestV46` relance `unittest`
  dans un sous-processus à environnement filtré, qui laisse `essais/_tmp` **vide** ; le `conftest` le retire en fin de session
  et le dit sur la sortie.

## Réserves

- **Non contre-lue (R2).** **Jamais lancée sur moteur réel.** Les contrats de sortie des rôles du pré-pilote (rédacteur
  `{"squelette", "declaration"}`, metteur `{"fiches"}`, relecteur `{"notable", "item", "champs", "defaut_present"}`, désaccord
  `{"desaccord"}`, vérificateur `{"references"}`, produits `{<clé>: [...]}`) sont à écrire dans les consignes figées ; non éprouvés.
- Contre-lecture de l'annexe : la v54 lit son format réel, mais l'annexe n'est ni contre-lue ni approuvée ; tant que ses deux
  champs portent « À REMPLIR », le bras méta est « non produit (annexe non conforme) » (A20), comme prévu.
- Sessions opaques : vérifié pour le noyau et le moteur simulé ; savoir si un agent réel voit son dossier courant reste à
  vérifier (CL18-12). L'adaptateur du kit peut écrire ses traces dans le dossier de session (réserve v53 inchangée).
- Machine jetable : la variable reste déclarative (CL18-13) ; le contrôle de l'opérateur (devis, destruction) est au registre.
- Le cache des essais anciens qui lancent des sous-processus à environnement filtré n'est pas joignable par le `conftest`.
- Commit non lu au manifeste (arbre hors dépôt) : à porter au registre du run.

## Ce qui reste

1. Contre-lecture R2 de la v54.
2. Décisions de Lazar : valeurs des clés configurables ci-dessus ; choix pris seuls 1 à 12 ; S1 à S31, D-e à D-j, L1 à L7 ; DEP4
   (session-depot) ; DEP5 ; lecture « clé des classes par programme en É5 » (A21).
3. Pièces à produire : analyseur de l'étage 1 (DEP3) ; garde de forme de M5 ; consignes figées au contrat ci-dessus ; résultats
   scellés des lignes R5 8, 9, 10, 17, 19 ; interface du bras d'attaque ; fiches d'antériorité et leur clé ; sources de M6b
   (DEP2c) ; annexe du bras méta contre-lue, approuvée, scellée ; source de S31.
4. Code d'analyse : intervalles (Clopper-Pearson, rééchantillonnage par fond), t* sur la partition (S7), M3, M5 (union,
   intersection, adjudication), M6, verdict par instrument ; complément conditionnel (hors budget).
5. Étage réel sur la machine jetable : rejouer `test_v52b_02` et la suite sous vrai `bwrap` là-bas.

## Fichiers nouveaux (rôle, empreinte)

Voir `EMPREINTES-orchestrateur-pole-v7-v54.txt` (tout l'arbre sauf elle-même et son compagnon) ; code :
`CODE-orchestrateur-pole-v7-v54.zip` (`conception-v7-v1.md`, `demonstrations/`, `essais/`, `exemples/`, `pole/`).

| fichier | rôle | SHA-256 |
|---|---|---|
| `pole/noyau_v54.py` | orchestration, appels comptés, aiguilleur, juges, A4 | `711a32679164bd63605f0bcc2a96f37d53260c479004d04d887d8228ac7d431b` |
| `pole/course2_v54.py` | génération et course 2 | `ac1980d04eb88d8fbb9a073902e47146ab9eadd3375a41cd72835fa5acf20342` |
| `pole/prepilote_v54.py` | pré-pilote É1–É9b | `77056684e5d1b2149521878da396d51bb3f16834de85ca9e86acdc7e1998592d` |
| `pole/gardes_e0_v54.py` | table R5 rejouée à É0 | `83b54b816b3277d97f5340ad4a316094a492bc2090c782b3e134092a97ca1edf` |
| `pole/configuration_v54.py` | clés v54, A15, DEP4 | `3424ca7fa8911e5c2656cb56632f7d74c958008b9366af0ac45e6a62e4d16d66` |
| `pole/budget_v54.py` | coupure, cumul réel, rejeu sur consommations | `220d25e6ce5a7eed008c095ef1a9f66e84b4e98f801dfee2f74bdda02ba5ac62` |
| `pole/bisociateur_v54.py` | I-1 à I-10 | `20d938b2dcafcd4bb7c9777a0182a3590b390a146a8375590905741ea0e250f8` |
| `pole/suivi_roles_v54.py` | A3, A11, A14 | `620225973d68670a56ca913cdd02709fa576fa43e1393d166915ea67c1d7c3bb` |
| `pole/fiches_v54.py` | A4 en préfixe, entrée complète | `1ab0796dd5d9de14ea84953b0307a065572bc300ebe45209ca207d7880bbaebf` |
| `pole/mesures_v54.py` | kappas, M1, S18/S19, S20 | `8f3f57fc98972fbcf6aefb27fd37298ac67f249cd295c7127b47ab8e77626c08` |
| `pole/etage_entre_generations_v54.py` | machine jetable durcie | `86a6bec00c3fee9b4ea510cf8dad8d899b9c96adef1e5ae4f8a8281d658143e5` |
| `pole/simulation_v54.py` | moteur simulé (rôles du pré-pilote) | `de2232922516f0d3fa2ca664ff80800d0ac53ff8e823b784864aab375e01941c` |
| `pole/bras_attaque_v54.py` | squelette qui refuse | `a4a70be0090f5c94852dae7b6192486a97b50ec5c901b27ed01ccb40fdde9368` |
| `demonstrations/ideation_v6.py` | lanceur | `4c302e5b97b229d5b3edd9e9a427f1e50796c10f7081f63132165ffeef854ba4` |
| `essais/aides_v54.py` | configurations d'essai (valeurs d'essai seulement) | `c65e1979ee38cd4f6516b0c5b0436e4339dbb7bfc0d1b6eee32ce35529f94d37` |
| `essais/conftest.py` | dossiers temporaires hors de l'arbre | `c60e041de98e46e2ff116f6811d19121156bb2f888b30961147e1f2ce3d2de3b` |
| `essais/mutations_v54.py` | 56 mutations en mémoire | `5891d3922b3d092f7c11e251112887b124a5482a4e446f52921b3295a53603de` |
| `essais/test_v54_corrections.py` | 31 essais | `789d1a774c139c928fc6eae90d2de15d1d74835b0bee7900a00bf5cae907582a` |
| `essais/test_v54_annexe.py` | 16 essais | `b9c4ba3d2e299c2776447a233e743d89a0ebd35392f97da3485f9ad0742ef41a` |
| `essais/test_v54_prepilote.py` | 22 essais | `ad21f895cd690b9ab773ad7a48bef98c8174bc93257653a24b48607136407712` |

## Lancement

```
python -I -B demonstrations/ideation_v6.py --course-2 CONF.json SORTIE_NEUVE --generations N --verifier-seulement
python -I -B demonstrations/ideation_v6.py --course-2 CONF.json SORTIE_NEUVE --generations N --moteur simule
GO_ID=GO-AAAA-MM-JJ-NN python -I -B demonstrations/ideation_v6.py --course-2 CONF.json SORTIE_NEUVE --generations N \
    --moteur reel --registre-go registres/go.md --confirmer-moteur-reel
python -I -B demonstrations/ideation_v6.py --pre-pilote CONF.json SORTIE_NEUVE --verifier-seulement   # refus DEP3 tant
                                                                                                        # qu'aucun analyseur n'existe
```

Clés de configuration : celles de la v53, plus `budget.portee_plafond`, `garde_kimi.{refus_aiguilleur, arret_metteur_fusion}`,
`tableau.juger_passe_tableau`, `bisociateur.fournisseurs_entree`, `bisociateur.meta.{regle_divergence, structures, definitions,
s28, desaccord}`, `a4.{mode, action}`, `graines.prefixe`, `arrets.{a3_echecs_consecutifs, a3_delai_s, a14_part_max,
a11_modeles}`, `dependances.dep4` (réel), et au pré-pilote `prepilote.*`, `decisions_a15` (réel), `plafonds_session.{redacteur,
metteur, relecteur, verificateur}` (forme complète : `essais/aides_v54.py`).
