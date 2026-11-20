# Rapport du développeur — code d'appel de l'étage 2 à 200 témoins (ligne 3, organisme v9) — v1

Pièce d'instrument (classe B), à contre-lire par un autre modèle (modèle S). Écrite le 2026-11-20 par le développeur, modèle O,
sur le mandat `mandat-developpeur-code-appel-etage-2-v1.md` (`d20e40d50549520faa7bd7a1838de1d39d15f675e884ff6db58a28c1487dbd9f`,
recalculée égale à son compagnon). **Rien de ce code n'a tourné contre un vrai juge** : aucun appel à un fournisseur, aucune clé
lue, aucun relais lancé, mode réel jamais lancé, aucune écriture dans le dépôt de travail ni dans le clone de l'orchestrateur.

## 1. Pièces lues, empreintes vérifiées

| pièce | empreinte | contrôle |
|---|---|---|
| texte v7, L3 (sections « Étage 2 » l. 243-305, « Liste d'arrêt » l. 352-378, « Plafond » l. 380-388, annexe A l. 554-563 ; en-tête et § 0 lus aussi) | `4e3680d9…` | égale au compagnon |
| additif 3 v3, `origin/main` (`a77ab95f…`), `prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md` (chemin pris dans le verdict de portée, la ligne R-4183 ne le donne pas), § 4.1, § 4.2, § 7 | `71b7a876…` | égale au compagnon de `main` |
| verdict « portée à 200 » v2, `origin/main`, `prereg/organisme-auto-conception-v9/ligne-3/verdict-portee-200/verdict-portee-200-ligne-3-v2.md` (issue B, cité ; sans effet sur ce code) | `02928723…` | égale au compagnon de `main` |
| inventaire, L3/`etage-2-portee-200-v1/` | `a2039f7d…` | égale au compagnon |
| calcul du plafond v2 et sa sortie, même dossier | `86440df6…` ; `fe58be3a…` | égales aux compagnons ; vérifiées aussi par les essais |
| `juges_croises_v53.py` et ce qu'il importe, clone `/home/user/lciric/ideation-organism` au commit `a41b7b50…` : `pole/__init__.py` `f7341b96…`, `outils.py` `966d9553…`, `caviardage.py` `78abfd47…` (importé par `fiches_v53`), `fiches_v53.py` `7cfcf832…`, `juges_croises_v53.py` `c4c6ab12…` | — | `c4c6ab12…` égale au texte ; les quatre autres prises par moi, mises en constantes du code |
| précédent, `scripts/epreuve_temoins_auto_conception_v9.py` | `5be161fa…` | égale au texte |
| lanceur v9, `scripts/lancer_course_auto_conception_v9.py` (cité par le précédent) | `1b47c1cf…` | prise par moi |
| consigne figée du juge, `course-v1/consigne-juge-auto-conception-v1.md` | `b03f33b8…` | égale au texte |
| préenregistrement de la course v2, `course-v2/preenregistrement-course-auto-conception-v2.md` | `0d51e0b3…` | égale au texte |
| configuration de la course v9, `course-v4/configuration-course-auto-conception-v5.json` (épinglée par le lanceur v9) | `3f662ee8…` | égale à l'épingle du lanceur |
| témoins v2, `course-v2/temoins-juge-auto-conception-v2.json` | `84a1e0ea…` | égale au texte |
| commande d'Argon v3d ; enveloppes d'Argon v5 et sans troncature (épinglées par le lanceur) | `46c91df4…` ; `37c0205e…` ; `7c3d8847…` | égales aux épingles |
| `registres/go.md` et `registres/decisions.md` de `origin/main` (lignes GO-2026-11-20-26, -36 ; R-4183, R-4246, R-4272) | — | lus par `git show` redirigé |

Lus aussi, en partie, sans empreinte au texte : `pole/adaptateurs.py` (construction des options du kit, adaptateur à commande
externe), `pole/relais_reel.py` (plafond du relais), `demonstrations/ideation_v8.py` (`adaptateurs_reels_v56`). Rien n'a été
touché sous `archives-reponses-modeles/`.

## 2. Ce que je reprends du précédent

Branche `lot/compte-organisme-v1`, tête `04131464ca37b34d17443354ffa2339894cb0cfd` ; dernier commit des deux fichiers repris :
`04ffdca296f91d6146ba5ac53a675e018ca6b19f`. Les deux modules sont chargés par le mode réel **après vérification de leur empreinte**
(constantes `PRECEDENT_V9` et `LANCEUR_V9`), compilés depuis les octets vérifiés.

- Du précédent (`5be161fa…`) : `charger_orchestrateur` (orchestrateur épinglé sur le chemin d'import), `exiger_bac_a_sable` et
  `environnement_de_sonde` (sonde du bac à sable, `actif` et `proc_neuf` exigés), `verifier_borne_argon` (borne du relais d'Argon
  relue par PID et par l'état, relais neuf), `preparer_appels` (adaptateurs réels `adaptateurs_reels_v56`, racine des dossiers
  d'appel sous la sortie interdite en lecture, garde `verifier_dossiers_d_appel` jouée avant tout appel), la forme
  `adaptateur.lancer("juge_ideation", consigne, dossier, plafond_session, 1, modele=…)`, la lecture `texte_brut or texte_final`
  sur un statut « ok », la garde « refus pour crédit » (fichier `arret-credit-*`), la forme de l'écriture scellée.
- Du lanceur v9 (`1b47c1cf…`) : `Reglages.production`, `verifier_pieces` (pièces épinglées, dont la configuration, la consigne,
  la garde de crédit, la porte de plafond, la procédure des relais, la commande et les enveloppes d'Argon, l'enveloppe de
  conservation des réponses brutes), `verifier_orchestrateur` (commit `a41b7b50…` et empreintes de l'orchestrateur),
  `verifier_declaration`, `appels_relais_gemini_requis` (**deux actions de relais par jugement d'Argon**, plus 2),
  `verifier_procedure_relais` (relais vivants contrôlés par PID ; plafond du relais Claude égal au plafond de ligne, ici
  88,36), `porte_a_blanc`, `envelopper_commandes`, `DOSSIER_CONSERVATION_NOM`, `LANCEUR_ORCHESTRATEUR`.
- **Plafond de session 0,60 USD** : celui de la configuration (`plafonds_session.juge` = 0,6), relu en exact au mode réel.
- Non repris, écart déclaré : `verifier_go` du lanceur (il compare le plafond en flottant et exige des mots de périmètre de la
  course) ; la garde « ligne de GO » de ce programme est écrite à part, en centimes exacts (§ 6).

## 3. Le moyen du plafond de session de 0,60 USD à chaque appel

Fonction `exiger_moyen_du_plafond_de_session` (appelée par `executer` avant la création du journal et avant tout envoi ; sans
moyen reconnu : refus, « pas de départ ») et `budget_de_session` (le `budget_usd` passé à chaque `lancer`, 0,6, dont l'écriture
décimale est contrôlée égale à 0,60 exactement).

- **Juge Argon (adaptateur à commande externe) : borne de jetons produits.** L'adaptateur met `PLAFOND_SESSION_USD` = 0,6 dans
  l'environnement de la commande (`AdaptateurCommandeExterne.environnement_commande`, `pole/adaptateurs.py` l. 648-664) ; la
  commande d'Argon v3d (`46c91df4…`, l. 796-857) fixe `maxOutputTokens` = min(`--max-sortie-jetons`, reste du plafond au prix de
  sortie moins la provision de pensée), refuse sans envoi si le pire cas dépasse (code 4), et rend un échec si le coût calculé
  dépasse (code 10). Le programme rejoue `environnement_commande(0,6, …)` et exige `PLAFOND_SESSION_USD` = 0,60.
- **Juge Opus (adaptateur du kit) : plafond du service.** `construire_options` (`pole/adaptateurs.py` l. 272-350) pose
  `max_budget_usd` = 0,6, `max_turns` = 1 et aucun outil ; le kit rend « budget_depasse » au-delà. Le programme construit ces
  options (fonction pure, aucun appel) et les relit.
- **Ce que l'essai montre** : l'adaptateur factice consigne le `budget_usd` et le nombre de tours de chaque appel ; les essais
  sains vérifient 0,6 et 1 sur les 1 004 appels (`test_plafond_cas_sain_tout_part`) ; l'artefact (adaptateur sans moyen
  déclaré, ou factice présenté au mode réel) est refusé avant toute création du journal (`test_moyen_du_plafond_de_session_artefact`).
  Le chemin réel (relecture de l'environnement de la commande, des options du kit) n'est pas exercé par les essais.
- **Réserve, à la contre-lecture** : pour le juge du kit, `max_budget_usd` est un contrôle du kit sur la dépense de la session,
  non une borne de jetons de la réponse ; je n'ai pas lu le kit. Une réponse seule pourrait dépasser 0,60 avant l'arrêt du kit ;
  le compteur la compte alors à son coût et arrête le programme (texte l. 382 : « sinon, à … plus le coût du dernier envoi »).
  Dire si ce moyen suffit à l. 382 (i) revient à la contre-lecture et à la mère.

## 4. Format de la banque de témoins (fichier de données)

Un fichier JSON scellé (compagnon `.sha256` égal à l'empreinte passée en argument `--banque-sha`) :

```
{"temoins": [ {"identifiant_interne": "…", "classe": "bon"|"mauvais", "item": null|<item de la consigne>,
               "niveau": null|"declare"|"net"|"discret", "citation": true|false, "moitie": "lecture"|"etalonnage",
               "contenu": {"<champ>": "<texte>", …}} , … ]}
```

Champs minimaux exigés ; d'autres champs d'un témoin et d'autres clés de tête sont permis, jamais servis. Règles :
identifiant interne unique, `[A-Za-z0-9._:-]{1,64}` ; un bon témoin n'a ni item ni niveau ; un mauvais a un item de la consigne
et un niveau ; 200 témoins, 100 par moitié ; `contenu` non vide, textes non vides, aucune clé réservée (`identifiant`, `meta`,
`classe`, `item`, `niveau`, `citation`, `moitie`…). **Seul `contenu` est servi.** Conséquence pour le générateur : la fiche
servie ne doit porter ni le mot « classe » ni un nom d'item de la consigne (`module_nomme`…), ni l'identifiant interne, sinon la
garde « vérité non servie » refuse de servir et le programme s'arrête avant l'envoi. Les onze témoins v2 passent cette garde
(`test_temoins_v2_de_la_plomberie_passent_la_garde`).

## 5. Sortie des essais

Commande exacte (sur ma copie) :

`env -C /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-code-appel-etage-2/code-appel-v1 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_epreuve_juges_reels_ligne_3_v1.py`

Résultat : **85 passed in 110.09s**, puis, second passage sur les fichiers dont la table donne l'empreinte (programme
`586bc7e6…`, essais `d68e2c14…`), **85 passed in 170.71s** (85 essais passés, aucun échec, aucun saut ; joués en tâche de fond). Trop propre à la règle R4 ? Chaque artefact exige son motif de refus nommé ou son
nombre exact ; aucun essai n'accepte « une erreur quelconque ».

Ce que les essais reproduisent du calcul v2 (sortie `fe58be3a…`, lue par empreinte), sur service factice aux coûts exacts du
calcul (tarif moyen par appel de la course v9 × facteur du cas ; tarifs du programme vérifiés égaux à `tarifs()` du calcul) :
- estimation et cas haut : 1 004 envois, aucune coupure, cumul compté égal au total exact du plan (32,9044 ; 44,7783 USD) et à
  la somme des coûts servis ;
- pire cas : coupure au témoin 198 du bloc B (moitié « étalonnage »), 996 envois sur 1 004, 197 témoins complets (100 de la
  moitié « lecture », 97 de l'autre), témoin partiel au rang 198, 87,7701 USD comptés ; dernier envoi parti et premier envoi
  interdit égaux à ceux du calcul ;
- tout refusé : 147 envois, 88,20 USD comptés, aucun rendu obtenu, dernier envoi et premier interdit égaux (bloc A, témoin 35,
  juge Argon, essais 1 et 2) — **joué avec l'arrêt de la plomberie levé, en mode essai seulement** (écart, § 7, point 1) ;
- selon les envois refusés, 0, 1, 2, 3, 5, 10, 20, 40, 60, 80 et 100, aux trois cas (33 lignes) : envois partis, témoins
  complets du bloc A, du bloc B et de la moitié « lecture », tous égaux ;
- au seuil d'arrêt de la plomberie (trois fois le tarif) : 630 envois, 87,9542 USD, 75 témoins complets au bloc B ; un
  milliardième au-dessus, arrêt de la plomberie après le premier envoi ;
- ordre des envois : celui que le calcul v2 a supposé (`sequence`), à l'identique — bloc A par témoin, juge Opus puis juge
  Argon ; bloc B moitié « lecture » d'abord, rendu 2 du juge Opus puis rendus 2 et 3 du juge Argon. Aucun écart.

Gardes, cas sain et artefact : plafond (dont coût relevé à 0,61 : arrêt après l'envoi, compté tel quel ; frontière 147 × 0,60) ;
compteur (coût relevé ; tout refusé ; sans coût lisible gardé, compté 0,60, non rejoué ; exception d'envoi comptée 0,60 et
rejouée) ; relance (engagement sans règlement compté 0,60 à la relance, rejeu en essai 2, journal jamais remis à zéro, manifeste
de relance ; relance refusée après un arrêt, après la fin, sur journal coupé, hors forme ou absent) ; verdict illisible (juge
« non mesuré » au-delà de 10 %) ; plomberie (illisible ; trois fois le tarif) ; modèle servi (arrêt du rôle, l'autre rôle
continue) ; réponses identiques (part 0 et part 1) ; identifiant opaque neuf ; vérité non servie (mot « classe », nom d'item,
identifiant interne ; dans l'exécution : arrêt sans envoi) ; moyen du plafond de session ; verdicts de la v9 ; banque scellée ;
ligne de GO (absente, échue, autre périmètre, autre montant, autre type, révoquée, forme) ; mode réel refusé avant toute
construction de service (sans `--go-id`, ligne invalide, `GO_ID` différent, banque d'une autre empreinte, déclaration absente ou
d'une autre empreinte, nom de clé dans l'environnement) ; empreinte d'un module de l'orchestrateur modifiée : refus avant import ;
dépôt scellé et manifeste.

## 6. Ce que le programme tient, en bref

- Service : `entree_une_fiche` et `lire_verdict` de `juges_croises_v53.py`, chargés après vérification des cinq empreintes,
  compilés depuis les octets vérifiés, sous un nom de paquet privé ; une fiche servie par appel (`{"contenu": …}` seul) ; un
  dossier d'appel neuf par rendu, nommé par l'identifiant opaque (jamais par l'identifiant interne).
- Identifiant opaque neuf par rendu (« F » + cinq chiffres hexadécimaux, forme du service de la course), jamais repris (journal
  compris) ; identifiant interne du rendu « témoin|juge|rN », jamais servi.
- Compteur : `Journal` (ajout seul, `fsync` par ligne, création exclusive) et `Compteur` (fractions exactes ; plafond et réserve
  en centimes entiers ; `PLAFOND_C = 8836` seule constante du plafond).
- Ligne de GO : `verifier_ligne_de_go(registre, go_id, jour)` — la ligne passée en argument, une seule ligne principale, huit
  colonnes, type « calcul », Lazar, non révoquée, dans sa période, périmètre « ligne 3 » et « étage 2 », montant égal à 8 836
  centimes. Elle ne dit pas quelle ligne vaut départ (inventaire § 5, remarque 3).
- Dépôt, par exécution : verdicts de la plomberie, de la moitié « lecture », de la moitié « étalonnage » (sans aucun champ de
  vérité), état des juges, rapport d'exécution, tous scellés ; manifeste d'exécution scellé (règle R9 : configuration et
  empreinte, versions, graines, commits, empreintes des modules, de la consigne servie, de la configuration servie des juges,
  de la banque, moyen du plafond de session, lecture du journal au lancement) ; réponses brutes et fiches servies gardées.

## 7. Ce que je n'ai pas pu tenir, et pourquoi

1. **« Tout refusé » contre l'arrêt de la plomberie.** La liste d'arrêt veut, sur un adaptateur qui refuse tout, « 41 envois
   partent, puis arrêt » (147 à 200, calcul v2) ; mais « plomberie illisible : arrêt » arrête bien avant : avec l'arrêt de la
   plomberie, le programme s'arrête après l'envoi et le rejeu du premier rendu de plomberie (2 envois, 1,20 USD). Les 147 envois
   sont reproduits par la même boucle avec `arret_de_plomberie=False`, permis en mode essai seulement (refus sinon ; le mode
   réel ne le passe jamais). À trancher par la mère.
2. **Le chemin réel n'est exercé par aucun essai** au-delà de ses refus d'entrée : `construire_service_reel` (relais, bac à
   sable, adaptateurs réels, porte de plafond) n'a jamais tourné. Sa contre-lecture se fait sur le code seul.
3. Le précédent ne s'appelle pas fonction par fonction sur 1 004 dossiers : sa garde `verifier_dossiers_d_appel` compare chaque
   dossier à tous les autres (quadratique). Je la joue sur deux dossiers témoins sous la même racine interdite ; chaque dossier
   réel est créé sous cette racine, nommé par l'identifiant opaque.
4. Cas limite non couvert : une panne tombée entre le règlement d'un rendu de plomberie et le contrôle de la plomberie ; à la
   relance, ce rendu est fini et son contrôle n'est pas rejoué. Le rapport de la relance porte le coût et la lisibilité relevés
   au journal ; la contre-lecture dira s'il faut rejouer ce contrôle à la relance.

## 8. Silences du texte, nommés sans les trancher (à la mère)

1. **Les deux témoins v2 de la plomberie** ne sont pas nommés : argument `--plomberie tXX,tYY` ; leur ordre est tiré.
2. **Plomberie, lecture du coût** : un coût non lisible empêche de lire « coût par appel » ; mon code arrête (choix prudent).
   L'arrêt se prend au premier rendu fautif, pas après les quatre.
3. **« Envoi refusé par le fournisseur »** : un statut « refus » sans changement de modèle est traité comme refusé (compté 0,60,
   rejoué) ; un refus qui porte un changement de modèle arrête le rôle. « Arrêt du rôle » est lu : ce juge n'est plus servi,
   l'autre continue ; le rendu au modèle changé est « absent ».
4. **Envoi en erreur avec un coût relevé au-dessus de 0,60** : le texte dit « compté 0,60 » ; mon code le compte à son coût et
   arrête (jamais sous-compté).
5. **Base des « plus de 10 % d'absents »** : rendus tentés des blocs A et B ensemble (non partis exclus) ; **« réponses
   identiques »** : toutes les paires de rendus d'un témoin par juge (les paires 1-2 sont rapportées à part).
6. **Racine des identifiants opaques** : aucune n'est écrite ; j'emploie 2026111935 avec la clé 4 (« identifiants-opaques »).
7. **Chemin du coffre de la course v9** non écrit : liste du code (composant `archives-reponses-modeles`, composant qui commence
   par « coffre », sortie `/home/user/sorties-course-auto-conception-v9`, run `runs/20261119-094145-course-auto-conception-v9`).
8. **Ligne de GO** : type « calcul » et mots « ligne 3 », « étage 2 » sont mes choix ; GO-2026-11-20-26 telle qu'écrite passe la
   garde, ce qui ne tranche pas la remarque 3 de l'inventaire.
9. **Clé du juge Opus** : aucune pièce ne l'attribue ; le nom passe en argument `--nom-cle-claude`. La `verifier_declaration` du
   lanceur exige une « pièce de départ » qui n'existe pas pour l'étage 2 : j'en passe une réduite (nom de la clé, aucune commande
   épinglée, aucune espèce optionnelle).
10. **Relance en mode réel** : les gardes reprises exigent des relais neufs (zéro appel) ; une relance demande donc des relais
    relancés et une déclaration neuve ; le plafond d'étape (88,36) est retransmis aux relais, le compteur seul garde le cumul.
11. **Borne du relais d'Argon** : 2 × (602 jugements + autant de rejeux) + 2 = 2 410 actions, mon choix au pire.
12. **Verdicts de la moitié « lecture »** : déposés dans leur fichier scellé ; le journal et les réponses brutes les portent
    aussi. « Restent scellés, non ouverts » se lit sur les programmes d'étalonnage et de lecture.
13. **Configuration servie** : celle que le lanceur v9 épingle (v5, `3f662ee8…`) ; le texte dit « configuration de la course v9 ».
14. **Interpréteur du mode réel** : l'annexe A dit `/usr/local/bin/python3` ; les essais tournent sous `.venv` (mandat).

## 9. Ce que l'additif de code de l'étage 2 doit porter pour ce programme

- Fichiers et empreintes (table `table-empreintes-code-appel-v1.txt`) : `epreuve_juges_reels_ligne_3_v1.py`,
  `essais_epreuve_juges_reels_ligne_3_v1.py`, ce rapport ; le commit qui les verse.
- Commande des essais (§ 5) et son résultat attendu (85 passés).
- Commande réelle, après la banque scellée et la ligne de départ :
  `GO_ID=GO-… /usr/local/bin/python3 -I -B epreuve_juges_reels_ligne_3_v1.py --reel --go-id GO-… --banque BANQUE.json
  --banque-sha SHA --declaration DECLARATION.json --declaration-sha SHA --sortie DOSSIER --plomberie tXX,tYY --nom-cle-claude NOM`
  (codes : 0 exécution écrite ; 2 refus avant envoi ; 3 arrêt écrit).
- **Racine 2026111935 autorisée**, table des clés gelée : ordre du bloc P = 1, du bloc A = 2, du bloc B = 3, identifiants
  opaques = 4 ; règle `numpy.random.SeedSequence(racine, spawn_key=(clé,))`, numpy ≥ 1.25.
- Constantes à comparer au texte : `PLAFOND_C = 8836` (égale à la ligne de GO), `SESSION_C = 60`, tarifs des cartes
  (3431597/47000000 et 51253/2000000 USD par appel), facteur d'arrêt de la plomberie 3, seuils 1/10 et 1/2 ; empreintes des
  cinq modules de l'orchestrateur et commit `a41b7b50…` ; consigne `b03f33b8…` ; témoins v2 `84a1e0ea…` ; configuration
  `3f662ee8…` ; lanceur v9 `1b47c1cf…` ; précédent `5be161fa…`.
- Les réponses de la mère aux silences du § 8 et à l'écart du § 7, point 1.

## 10. Écarts à mon mandat

1. Une recherche par motif sur un **dossier** hors du mien : `def variables_agent` dans `…/ideation-organism/orchestrator/pole/`
   (pour trouver la fonction de `construire_options`) ; lecture seule, une ligne rendue. Les autres recherches ont porté sur un
   seul fichier nommé.
2. Une commande `python -I -B -m pip list` sur l'interpréteur de `.venv` (pour lire la version de numpy) : un `-m` hors de la
   commande d'essais du mandat.
3. Un outil de travail hors des pièces rendues, `…/developpeur-code-appel-etage-2/outils/tarifs_exacts.py`, qui charge le calcul
   v2 en lecture et imprime ses tarifs exacts ; et des copies de `origin/main` (registres, additif 3, verdict de portée et leurs
   compagnons) tirées par `git show` redirigé dans mon dossier.
4. Les essais écrivent dans le dossier temporaire de pytest (`/tmp/pytest-of-…`), hors de mon dossier ; rien dans le dépôt.
5. Aucun refus de permission, de classifieur ou de garde n'a eu lieu.

Développeur, modèle O.
