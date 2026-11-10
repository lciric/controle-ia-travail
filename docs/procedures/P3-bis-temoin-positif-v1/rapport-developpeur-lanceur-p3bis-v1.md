# Rapport du développeur : lanceur de P3-bis et sa chaîne de session — v1

- **Auteur** : développeur neuf (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère
  `session_01QPDgKgACWyCkCN8HjqwNXy` ; je n'ai écrit ni le code de P3-bis, ni ses brouillons, ni ses contre-lectures, ni
  T0.6, ni T0.7.
- **Heures** (toutes relevées par `date -u`) : début 2026-11-10 05:20:40 UTC ; arbre créé à 05:21 ; message de la mère
  (GO-2026-11-10-02, 23 novembre) reçu vers 06:10 et appliqué au jalon 6 (06:18:21) ; @@HEURES@@
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-lanceur-p3bis-v1.md`
  (`b0c7d5088d826d730d380410330edf2e4759d7e0526d49a4d986069da1d6b135`, vérifiée) ; noms communs
  `noms-communs-p3bis-v2.md` (`766992f4ea5eea8b5e319fd315e2ea0cb646c8f0e0400bf32a2bf5fdcb83d06a`, vérifiée) ; interdits
  communs (`851028fc2f425cee8e64613db20f6a2e2a7c289d07dd5441a9993d24630682a6`, vérifiés) ; message de la mère reçu en
  cours de travail : GO-2026-11-10-02 (R-2077, commit `39a3a506` de `main`, lu par `git show main:…` seulement) et date
  limite du 2026-11-23.
- **Lu** : brouillon 9 (`eb65773f…`, vérifiée : en-tête, plan, liste d'arrêt, code, devis, marqueurs) ; contre-lecture du
  code (`7a074ad1…`, vérifiée, entière) ; chaîne de P3 `docs/procedures/P3-premier-test-v2/` (lanceur, module commun,
  contrôles, surveillance, contrôle à cinq minutes, récupération, scellement, répétitions, bancs) ; garde de calcul (lecture
  seule) ; ligne GO-2026-11-02-29 de `registres/go.md` ; lignes GO-2026-11-10-02 et R-2077 sur `main` ; scripts de
  l'instance v1, `ouverture_p3bis_v1.py` (interface, paquets), `run_v2.py` (garde de configuration), `prereg.py`,
  `scellement.py`, `harnais/validation_reelle.py` (`CHEMINS_GELES`, `exiger_code_cite`).
- **Interdits tenus** : aucun fichier ni branche interdits ouverts (aucun `diag/` ni `runs/` de 7a, aucun
  `lecture-sondes-t06.json`, aucune lecture B, aucun fichier de T0.7, ni l'étiqueteur, ni le bras d'attaque, ni
  `extraire_mesures_epreuve_t06_v1.py`) ; aucun `vastai` réel (l'outil n'existe pas sur cette machine ; tous les essais
  jouent un faux outil sur un PATH fermé par `env -i`), aucune création, aucune dépense, aucun appel externe ; instances
  58936096, 58936099 et 58936100 présentes seulement comme constante `ARRETEES_TOLEREES` (les bancs vérifient qu'aucun
  verbe ne les vise) ; garde de calcul et `registres/go.md` non modifiés (registres temporaires fabriqués dans les essais) ;
  aucune lecture d'environnement ni de valeur de clé ; commits locaux sur `prep/p3bis-lanceur-v1` seulement, ni fetch ni
  push ; aucune écriture hors de mon arbre et de mon bloc-notes ; garde des secrets à 0 avant chaque commit ; place disque
  regardée avant chaque passage d'essais (jamais sous 4,5 Go libres) ; **aucun refus de permissions ni de classifieur**.
- **Non vérifié, déclaré** : le module d'ouverture v2 et les scripts de l'instance v2 n'existent pas encore (autre
  chantier) : la chaîne est écrite contre leurs noms et leur interface (section « Dépendances ») ; les bancs jouent un
  bouchon d'`ouverture_p3bis_v2` qui appelle la logique réelle d'`ouverture_p3bis_v1`. Une anomalie préexistante de
  `main`, étrangère à ce travail : `verifier-arbre` signale une empreinte orpheline
  (`docs/notes/ideation-organisme-v1/question-mere-reponses/consigne-argon-question-mere-v3.txt.sha256`).

## Verdict

Chaîne écrite, éprouvée et répétée sur jouet : tous les contrôles du point 6 de la contre-lecture du code ont un cas sain
et un artefact ; @@COMPTES@@. Elle n'est **pas lançable** avant le candidat : épingles `A_EPINGLER` des contrôles et de la
récupération (refus de tout lancement tant qu'il en reste une, éprouvé), code corrigé v2, brouillon 10 (écarts ci-dessous),
journaux canoniques des bancs et des deux répétitions rejoués après épinglage, contre-lecture R2 de la chaîne.

## Fichiers et empreintes

@@EMPREINTES@@

## Contrôles : texte → code → essai

| exigence (point 6 de la contre-lecture du code ; consigne, mandat 1 ; texte, brouillon 9) | code | essais (cas sain ; artefacts) |
|---|---|---|
| GO cité = GO-2026-11-10-02 (message de la mère ; brouillon 9 : GO-2026-11-02-29), ligne unique au registre, type calcul, Lazar, octroi, plafond et échéance mot pour mot | `verifications_p3bis_v1.py go` ; lanceur (avant et après les contrôles, avant la création) ; contrôles bloc 5 | pytest `test_go_*` (sain : jour 10, dernier jour 23, registre réel de `main` ; artefacts : GO autre, GO-29 du brouillon 9, `GO_ID` autre, ligne double, mal formée, absente, type, accord, plafond, échéance, octroi réécrits, 9 colonnes) ; banc du lanceur L00, L05 ; contrôles K00, K11 |
| aucune révocation (forme exacte : ligne « révocation » qui nomme le GO dans son périmètre ou sa référence) ; révocation du GO d'origine GO-2026-11-02-29 aussi refusée | module `go` (`revocations`) ; garde de calcul rejouée | pytest (périmètre, référence, GO d'origine ; sains : autre GO, identifiant voisin, type « décision ») ; lanceur L04, L04b ; contrôles K12 |
| date au plus tard le 23 novembre 2026, en constante (`DATE_LIMITE_CREATION`, lanceur et module) | lanceur `date_permise` (départ, après les contrôles, avant chaque essai d'offre, avant la création) ; module `go` | pytest (24 refusé, 23 sain, constante seule) ; lanceur L06 (24), L06b (23 sain), L07 (date franchie pendant l'attente des offres) |
| texte scellé sans marqueur | contrôles bloc 4 (aucun `<<…>>`, `problemes()` vide, sceaux) ; scellement | contrôles K00 ; K06 (marqueur restant), K07 (`problemes()`) ; scellement (fumée) |
| commit cité = arbre gelé du commit de scellement ; commit cité = code relu | contrôles bloc 2 (`git diff --quiet <code> S -- CHEMINS_GELES`, ancêtre, cité une fois) ; bloc 3 (identité avec P3 : ajouts seuls) ; scellement | K00 ; K02 (cité deux fois), K03 (autre commit), K04 (arbre gelé modifié), K05 (fichier de P3 modifié) |
| essai de fermeture conforme au commit du code, sinon aucune création | contrôles bloc 6 : sortie versée (empreinte épinglée, scellée, citée, dernière ligne CONFORME, aucune ligne NON CONFORME) puis **rejouée au commit S** | K00 ; K14 (sortie non conforme), K15 (non citée), K16 (rejouée non conforme) ; lanceur L08 (contrôles en échec : aucune création) |
| longueurs remesurées | contrôles bloc 7 (vrai tokeniseur : A, T, B ; consigne et indication, seules et dans le gabarit ; 60 tâches) ; module `longueurs` (A = T tâche par tâche ; résumé = longueurs attendues épinglées, citées) | pytest `test_longueurs_*` ; K00 ; K17 (A ≠ T), K18 (résumé autre), K19 (non citées) ; mesure réelle : bouchon du banc, jouée par la répétition finale |
| compte N des essais | contrôles bloc 8 (N cité une fois ; liste v2 d'empreinte égale à `LISTE_SHA256` du script de l'instance ; « N passed » exact dans PY ; versions de PY égales aux dépendances de S) ; bloc 12 (lecture précoce) | K00 ; K20 (N autre), K21 (essai en échec), K22 (liste altérée), K23 (versions), K29 (citation en double) |
| offre dans les bornes du texte et repli écrit | module `offres` (A100 SXM4 ≥ 79 000 Mo, une carte, CUDA ≥ 13, fiabilité ≥ 0,98, ≤ 2,10 USD/h, ≥ 30 cœurs, ≥ 128 000 Mo, disque ≥ 80 Go, stockage ≤ 0,08, téléchargement ≤ 0,05 ; EPYC 7513 exigé, sauf repli) ; lanceur (douze essais à 900 s, puis repli : seule la condition du processeur retirée, ligne écrite) | pytest `test_offres_*` (bornes exactes saines ; 17 artefacts hors bornes ; repli qui ne relâche que le processeur ; moins chère non conforme écartée ; réponse illisible, doublon) ; lanceur L19 (repli écrit), L20 (aucune, même en repli), L21 (offre au troisième essai), L22 |
| crédit ≥ 20 USD + 10 h du prix des instances nommées en marche | module `credit` ; lanceur | pytest `test_credit*` ; lanceur L25 (34,00 avec une instance à 1,40), L25b, L27 (19,99), L27b (20,00), L28 |
| instances du compte : arrêtées et dans `ARRETEES_TOLEREES`, ou en marche et nommées avec leur GO | module `instances` ; lanceur (argument `ID:GO-…`) | pytest `test_instances_*` ; lanceur L23, L24, L25, L26, L26b ; L35 et bancs : aucun verbe sur les instances tolérées |
| `DEPOT_URL` du dépôt de travail | constantes du lanceur, des contrôles, de la récupération (module `constantes`) ; `--env` de la création ; ligne « Lancement » ; scripts de l'instance (jamais la copie publique) | lanceur L00 (env passé), L16 ; contrôles K30, K26 (constante autre) |
| branche de calcul absente du dépôt distant | lanceur (vN absente ; relance : vN−1 présente) ; contrôles bloc 13 ; scellement | lanceur L01, L02, L03 ; K31 |
| surveillance sans arrêt à durée ; alerte à deux heures sans PROGRES | `surveiller_p3bis_v1.sh` (aucun plafond ; `ALERTE_SANS_PROGRES_S=7200`, une alerte par fenêtre, sans sortie) | surveillance M12 (run de 30 h sans arrêt), M13 (une alerte, pas d'arrêt), M14 (PROGRES neuve : aucune alerte) |
| arrêts par identifiant d'instance (R10) | surveillance `arreter` et contrôle à cinq minutes (garde `identifiant` : instance du lanceur, hors tolérées ; `vastai stop instance <id>`) ; destruction (`destroy instance <id>`) | M00 à M11 (un seul arrêt chacun), M15 (arrêt en échec), M16 (autre identifiant), M17 (instance tolérée) ; C03 à C15 ; D00, D05, D06 |
| arrêt à 80 USD | module `depense` (projection au prochain relevé ; dépense antérieure en argument) | pytest `test_depense_*` ; M10 (39 h à 2,10), M11 (antérieure 79), M09 (prix illisible : borne) |
| code 5 du second paquet = instance gardée | module `motif` (`GARDER`) ; surveillance (`instance-gardee`, arrêt sans destruction) ; destruction refusée | pytest `test_motif_garder*` ; M01, M02, M03 (aucun arrêt avant la fin de l'amorce) ; D01, D01b ; répétition, tentative 2 |
| motifs gardés de P3 : fin, échec d'amorce, redémarrage, état terminal ; processus mort | module `motif` ; surveillance | M00, M04, M05, M06, M07, M08 (hors ligne passager), M09 (état illisible) |
| récupération par clone de la branche de calcul, jamais `main` | `recuperation_p3bis_v1.sh` (clone d'une seule branche, `calcul/p3bis-reel-v[123]`, branche courante relue) | R00 ; R01 (`main`), R01b |
| `lectures-fermees --prereg --entropie` | récupération bloc 4 (entropie citée une fois, égale à celle de P3) | R00 (arguments relus), R13 (entropie autre), R12 (second paquet altéré : dépliage refusé), R14 (lecture en échec) |
| commit du seul paquet et de son compagnon | récupération bloc 5 (index : exactement deux chemins ; poussée ; relecture du distant) ; aucun reste en clair (non suivis et ignorés) | R00 ; R03, R04 (fichier du run en clair sur la branche : aucune lecture), R12, R14 (aucun commit) ; répétition, tentative 1 |
| contrôle à cinq minutes (liste d'arrêt) | `controle_cinq_minutes_p3bis_v1.sh` | C00 à C18, V01 à V04 ; répétition, tentatives 1 à 3 |
| destruction en fin normale, après la récupération vérifiée | `detruire_p3bis_v1.sh` | D00 à D09 ; répétition, tentatives 1 et 2 |
| scripts égaux aux copies versées à S ; preuves des essais | lanceur (blocs 2, 2 bis) ; scellement | L11, L12, L12b, L13 ; R15 |

## Essais

@@ESSAIS@@

## Écarts au texte (brouillon 9) et à la consigne, déclarés

1. **GO et date** (message de la mère, R-2077) : GO-2026-11-10-02 et le 23 novembre 2026, au lieu de GO-2026-11-02-29 et
   du 16 novembre. Le brouillon 10 doit porter : ligne « - GO : **GO-2026-11-10-02** … », `GO_ID=GO-2026-11-10-02` dans la
   ligne « Lancement », « création au plus tard le 23 novembre 2026 » (forme lue par le module, sous-commande `valeurs`),
   et l'échéance du GO. Le module refuse aussi une révocation de GO-2026-11-02-29 (plus strict, déclaré) et exige la ligne
   GO-2026-11-10-02 mot pour mot (octroi 2026-11-10, plafond « 80 USD (plafond de GO-2026-11-02-29, non cumulé) »,
   échéance 2026-11-23). La dépense antérieure passée à la surveillance comprend toute dépense sous GO-2026-11-02-29.
2. **Ligne d'accord du jour de P3** : retirée (DB-5 (a) : le GO en tient lieu).
3. **Modèle** : la consigne nomme `docs/procedures/P3-premier-test-v1/`, le texte (code, point 6) `…-v2/` ; les deux ne
   diffèrent que par le dossier des copies versées (comparés : mêmes logiques) ; la chaîne suit `…-v2/`.
4. **Noms hors du tableau commun** (à signaler à la mère) : `detruire_p3bis_v1.sh` (destruction par identifiant, après la
   récupération vérifiée ; P3 n'en avait pas) ; `controle_cinq_minutes_p3bis_v1.sh` (comme P3) ;
   `essais_verifications_p3bis_v1.py` (banc pytest du module commun) — placé sous `docs/` et non sous `tests/` :
   `tests/` est dans l'arbre gelé (`CHEMINS_GELES`) que fixe le commit du code corrigé ; y ajouter un fichier ferait
   diverger l'arbre gelé de S. Aucun fichier de l'autre développeur n'est renommé.
5. **Surveillance** : elle arrête elle-même l'instance par son identifiant (P3 : la session) et écrit la ligne à consigner ;
   le motif « processus mort » est lu à la fin de l'amorce (la consignation et la poussée de l'instance ne sont jamais
   coupées) ; un processus mort sans que le script de l'instance le voie relève de l'état terminal ou de l'alerte ;
   l'alerte n'arrête rien et ne fait pas sortir la surveillance (sortie standard et `alertes.txt`, à lire par la session).
6. **80 USD** : arrêt quand la dépense **projetée au prochain relevé** atteint 80 USD (pour ne jamais dépasser) ; prix pris
   = le plus haut du prix relu et de celui de l'offre (2,10 USD/h si illisible, écrit) ; téléchargement relevé par
   `inet_down_billed × inet_down_cost` (+ montée), majorant 2,00 USD écrit s'il est illisible (devis) ; le disque est
   supposé compris dans `dph_total` en marche (champ de l'outil, hypothèse déclarée).
7. **Repli du processeur** : écrit au journal du lancement et dans `repli-processeur.txt` ; la ligne du registre des
   dépenses est inscrite par la session (aucun script n'écrit les registres).
8. **Recharge automatique du compte** : non lisible par la chaîne, non contrôlée.
9. **Instances nommées** : argument fermé `ID:GO-…` ; une instance nommée trouvée arrêtée, ou absente du compte, est
   refusée (lecture littérale de la liste d'arrêt) ; le GO d'une instance nommée doit exister, être de calcul, accordé par
   Lazar, non révoqué (sa date n'est pas exigée : course en cours).
10. **Aucun délai** : ni plage horaire 23:30-00:00 (P3 : suite complète), ni `timeout` des contrôles.
11. **S en argument du lanceur**, contenu dans une branche du dépôt distant (pas forcément `main`, conforme à l'en-tête) ;
    tentative N en argument (1 à 3) ; une relance exige la branche de la tentative précédente ; « aucun épisode joué, code
    inchangé » reste à la session (nœud).
12. **Formes de citation exigées du texte** (à porter au brouillon 10 au remplissage des marqueurs) : `` `<chemin>`
    (`<sha256>` `` pour l'amorce et le script de l'instance v2 (forme de P3), la sortie de l'essai de fermeture et le
    fichier des longueurs attendues ; noms v2 dans la ligne « Lancement » et dans `EMPREINTES_CODE_P3BIS`.
13. **Longueurs** : la chaîne exige un fichier JSON des longueurs attendues (forme `resume_longueurs` du module : quatre
    mesures × trois emplacements, valeur → nombre de tâches), versé à S, épinglé et cité ; A = T exigé tâche par tâche,
    B rapporté.
14. **Récupération** : le paquet est commité par « session de pilotage (P3-bis) » sur la branche de calcul et poussé en
    avance rapide ; run sans résumé ou aucun run : aucune lecture, code 4 ; rapport écrit à côté du clone.
15. **Destruction** : seulement après le motif FIN et une récupération conforme de la branche du lancement ; refusée après
    un code 5 et après tout autre motif (nœud de Lazar).
16. **Scellement** : S n'ajoute que six fichiers (règle de P3) ; la ligne `SCELLEMENT-P3BIS` n'est pas écrite par le script
    (imprimée, inscrite par la mère dans un commit suivant) ; la chaîne, ses journaux et les pièces épinglées doivent donc
    être versés sur la branche de scellement **avant** S.
17. **Journaux** : mes passages sont versés sous `journaux-developpeur-v1/` (noms `…-dev.log`) ; les noms canoniques
    (`banc-*-p3bis-v1.log`, `repetition-*-p3bis-v1.log`), exigés par le lanceur à S, restent libres pour les passages au
    candidat, après épinglage (les empreintes des contrôles et de la récupération changent avec leurs épingles ; R12).
18. **PY** (contrôles, récupération) : épingle `A_EPINGLER` ; un environnement aux dépendances épinglées de S (le bloc 8
    le vérifie) ; N doit être compté dans le même environnement que la liste jouée par les contrôles.

## Dépendances envers le code corrigé (autre chantier)

1. **Noms v2** : `scripts/amorce_instance_p3bis_v2.sh`, `scripts/p3bis_instance_v2.sh`, `scripts/essais-cibles-p3bis-v2.txt`,
   `scripts/essai_fermeture_p3bis_v2.py`, module `controle_ia.premier_test_ia.ouverture_p3bis_v2` (si l'amorce garde son
   nom v1, changer la constante `A` du lanceur et `AMORCE` des contrôles).
2. **`ouverture_p3bis_v2 lectures-fermees --racine . --run R --lecture RL --lecture-complementaire RLC --prereg P
   --entropie E`** : n'imprime que les cinq lignes de v1 (« code dépliage du second paquet : N », « code lecture de P3 :
   N », « code lecture complémentaire : N », « code mise en paquet : N », « paquet des lectures : <sha256> »), rien sur la
   sortie d'erreur ; code 0 si les quatre codes valent 0 ; paquet `diag/p3bis-ferme-<run>/paquet-ferme-v1.tar` de
   16 783 360 octets, compagnon « `<sha256>  paquet-ferme-v1.tar` » ; aucun fichier en clair restant (non suivi ni ignoré) ;
   second paquet `diag/<run>/paquet-run-ferme-v1.tar.NNN` et `paquet-run-ferme-v1.json`, scellés.
3. **Script de l'instance v2** : une ligne `LISTE_TESTS="scripts/essais-cibles-p3bis-v2.txt"` et une ligne
   `LISTE_SHA256="<sha256>"` ; `DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"` ; lanceur
   `controle_ia.premier_test_ia.run_v2` ; aucune commande `timeout` ; l'amorce v2 appelle
   `bash amorce-depot/scripts/p3bis_instance_v2.sh`.
4. **Lignes du journal de l'instance** lues par la surveillance et le contrôle à cinq minutes : « `AMORCE <date> : commit
   <S>` », « `AMORCE : …` », « `AMORCE <date> : fin, code N` », « `début : ETUDE=p3bis MODE=reel COMMIT=<S> BRANCHE=<b>` »,
   « `préenregistrement lu : N tests attendus` », ligne de `nvidia-smi` (« …A100…SXM4…, NNNNN MiB »), « `branche <b>
   poussée avant l'installation` », `PROGRES …` (motif de P3), « `run : processus P fini, code C` », « `résumé écrit sans
   arrêt consigné : run complet` », « `SECOND PAQUET EN ÉCHEC` » ; code de sortie 5 quand le second paquet échoue, y compris
   pendant un arrêt (CP-17).
5. **Branche de calcul poussée** : chemins permis de la récupération (`runs/<run>/manifeste.json`, `diag/<run>/
   {sondes-figees,resume,arret}.json`, second paquet, `traces/p3bis-*/{journal.txt, tests.txt, tests.err, run.json,
   run.err, nvidia-smi.txt, pip-freeze.txt, processeur.txt, second-paquet.txt, empreintes.sha256}`, compagnons) ; auteur
   « instance de calcul (P3-bis) » ; run `AAAAMMJJ-HHMMSS-p3bis-reel`. Tout autre chemin ajouté par le code corrigé
   demande d'étendre `PERMIS` (version neuve de la récupération).
6. **Essai de fermeture v2** : `essai_fermeture_p3bis_v2.py DOSSIER_NEUF SORTIE.txt`, code 0, dernière ligne
   « ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME », aucune ligne commençant par « NON CONFORME » ; s'il joue aussi le mode
   décisif sous un texte scellé, le bloc 6 des contrôles couvre la chaîne fermée décisive (aucun autre essai ne le peut
   avant la course).
7. `run_v2.exiger_config_p3bis` (bloc 9 des contrôles) ; `controle_ia.prereg.problemes` ; `CHEMINS_GELES`.
8. Rejouer, au code corrigé : les bancs de la récupération et la répétition jouet avec le vrai `ouverture_p3bis_v2` (le
   bouchon des bancs disparaît), et la répétition finale.

## Ce que la mère mettra au marqueur `<<CHAINE_P3BIS>>`

@@CHAINE@@

## Ce qui reste

1. Au candidat : remplir les épingles `A_EPINGLER` (contrôles : candidat, configuration et consignes relus, code relu,
   essai de fermeture, longueurs attendues, rapports, PY ; récupération : PY), puis rejouer les cinq bancs, la répétition
   jouet et la **répétition finale en mode décisif** (écrite, non jouée), sous les noms canoniques, scellés et versés
   avant S.
2. Contre-lecture R2 de la chaîne par un sous-agent neuf d'un autre modèle (fichiers à lui donner : ce rapport, la chaîne,
   le brouillon 10, la contre-lecture du code).
3. Brouillon 10 : écarts 1, 12, 13 et 16 ; noms v2.
4. Jouer la chaîne contre le code corrigé dès qu'il existe (dépendances 1 à 8).
5. Scellement : aucun banc dédié ; essai de fumée (cas sain, refus R12, puis contrôles conformes sur le S produit) ; joué
   en entier par la répétition finale.
