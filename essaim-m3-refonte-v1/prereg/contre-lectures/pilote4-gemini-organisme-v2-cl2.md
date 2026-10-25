# Contre-lecture 2 du préenregistrement du quatrième pilote descriptif (`pilote4-gemini-organisme-v2.md`) — v1

- **Texte relu** : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v2.md`,
  `8657fcd272decfc79d0c2595a4a461e16605e6df1a11e928fb8f515943744144` (empreinte vérifiée sur disque avant lecture ;
  commit cité par la demande : `f8bbd89`, non vérifié, pas de `git`).
- **Contre-lecteur** : sous-agent neuf (`claude-opus-5-5`), lancé par conv-audit, le 25 octobre 2026. Début lu sur
  `date -u` : 19:09:06 UTC ; ce rapport est écrit à partir de 19:31 UTC (heure lue sur `date -u` juste avant). Je n'ai
  écrit ni ce texte, ni la v1, ni P3, ni T2, ni la contre-lecture 1, ni le lanceur, ni la batterie, ni le script de
  scellement.
- **Lu** : la v2 en entier ; la v1 en entier et l'écart v1 → v2 ; la contre-lecture 1 en entier (`3dd09acb…`) ; P3
  (`57c8535a…`) en entier ; T2 (`d2944654…`) l. 140–319 et 405–564 ; l'écart du lanceur v3 au v4, les parties utiles du
  lanceur v4 (l. 1–110, 225–262, 400–460, 630–710) ; les deux scripts de dérivation (lanceur v4, batterie v5) ; la batterie
  v5 (l. 1–160 et ses ajouts) ; le journal de la série v6 en entier et son fichier d'heures ; `simulation-lanceur-v4/`
  (deux `LANCEMENT`, deux extraits : manifeste et événements) ; `sceller_pilote4_v1.py` et `_v2.py`, leurs essais et
  leur journal ; `faits-pilote3-v1/` en entier (deux scripts, deux fichiers de faits, lignes de `LANCEMENT.md` et du
  registre des dépenses) ; `EMPREINTES-pieces-pilote4-v3.txt` ; `contre-lecture-1-v1/` (empreintes, lanceur redérivé) ;
  le noyau : `boucle.py` (l. 40–79, 200–290, 580–640, 700–930), `cli.py` (l. 25–55, 115–130, 260–272, 370–410),
  `contrat.py` (l. 138–152), `archive.py` (l. 70–82, 229–234), `serveur.py` (l. 15–95), `moisson.py` et `recherche.py`
  (constantes et bornes) ; dans `tests/test_noyau.py`, deux essais nommés (l. 290–296 et 2372–2392, plus les lignes
  1816–1846 trouvées par recherche du mot « conception ») ; le code extrait de la v6.1 et de la v5.3 (lignes citées et
  voisines ; `memoire_isvd.py` des deux objets en entier pour la fonction de mise à jour), et, pour une seule ligne, la v6
  (`/var/tmp/verif-pousses-v53-v6/v6/organisme/principal.py` l. 915–918) ; la référence de provenance (script et
  sortie), la référence de paire (sortie) ; la contre-lecture de la banque v5 (BC5-01 à BC5-04) ; `LISEZMOI-v9.md`
  (l. 1–125).
- **Non lu ni ouvert** (consignes) : aucun fichier `…-cle.json` ni `…-secret.json` (ni lu ni haché), aucun dossier
  `donnees/`, `runs/`, `diag/`, aucun `P3-consignes-v1.md` ni fichier `textes-actions-…`, aucune archive
  `ferme.tar.gz`, aucun fichier `reponse-question*`, `journal-appels*` ou `extrait-mecanique*` des pilotes réels. Ni le
  rapport de vérification de la v6.1, ni la demande de v6.2, ni la note N-046, ni les messages du canal, ni les registres
  de `main` (hors des lignes recopiées dans `faits-pilote3-v1/`) : ce qu'ils portent n'est pas vérifié ici.
- **Exécuté** (sorties sous `/var/tmp/contre-lecture-pilote4-v2/` seulement) : `sha256sum` sur les pièces ;
  `deriver_lanceur_pilote4_v4.py` sur le lanceur v3 et `deriver_essais_pilote4_v5.py` sur la batterie v4
  (`rederive/`) ; `diff -u` du lanceur v3 au v4 ; `sceller_pilote4_v2.py` sur deux copies d'essai de la v2
  (`essai-scellement/` : leurs valeurs d'entropie et de graines sont **tirées pour l'essai, ce ne sont pas celles du
  pilote** ; le fichier `…-cl2.md` qui s'y trouve est un fichier d'essai d'une ligne, pas ce rapport) ; mon propre code,
  lecture seule (`outils/`) : empreintes d'arbre des deux objets, plus proche voisin de la référence de provenance
  recalculé sur la banque seule, vérification des copies scellées comme le lanceur les lit. **Rien** du lanceur, de la
  batterie, du noyau ni du code des organismes n'a été exécuté. Aucun sous-agent, aucun `git`.

## Verdict

**Scellable après corrections mineures.** Les quatre constats majeurs de la contre-lecture 1 sont levés : la ligne de GO
nomme la banque v3 et se vérifie aussi par `157a2b45` (P4C1-01) ; la garantie de deux heures de T2 est déclarée caduque,
la borne de 900 s par ronde est dans le lanceur v4 et acceptée par la garde du noyau (885 s ≤ 900 s), le minuteur est
préenregistré, fait ce que dit le texte et est essayé sur un cas sain et sur un artefact, le risque est soumis à Lazar
(P4C1-02, levé en grande partie) ; le devis cite ses sources et ses chiffres sont justes (P4C1-03) ; la condition (i) du
moment de lecture est réécrite (P4C1-04). Le lanceur v4 et la batterie v5 se redérivent octet pour octet ; la série v6
est complète (162 sur 162).

Il n'y a pas de constat majeur nouveau. Neuf mineurs et cinq remarques suivent ; les mineurs sont des corrections de
texte (et une vérification à la main avant scellement) que l'auteur peut faire sans nouvelle relecture, **à condition de
ne changer ni le lanceur ni la batterie** : l'option (b) de P4C2-01 (lanceur v5) demanderait une série nouvelle et une
relecture courte. Le plus important : un `STOP` du minuteur posé pendant g003 laisse quatre générations finies, mais la
porte refuse alors la v6.1 ; avec la fourchette du texte lui-même (≈ 50 à 105 minutes), le minuteur (95 minutes) tombe
dans le cas attendu ; cela doit être dit, et porté par le mot de Lazar (P4C2-01).

## Traitement des constats de la contre-lecture 1

| constat | statut | ce que j'ai vérifié |
|---|---|---|
| P4C1-01 (majeur) | **levé** | Ligne de GO, l. 279 : `banque confrontation-v3 157a2b45a8d9…0011d` ; vérification par session-depot avec `157a2b45` en plus (l. 281–282, comme T2 l. 287). Les `grep` du lanceur (v4 l. 440–444) trouvent `calcul`, `8b1c7511`, `6251ab21` / `ae331d1d` et les 16 premiers caractères du texte sur cette ligne. |
| P4C1-02 (majeur) | **levé en grande partie** | (a) garantie caduque dite (l. 227–230), ligne de T2 remplacée (l. 333) ; (b) cas attendu refait avec les durées réelles, chiffres justes (§ Chiffres) ; (c) `--temps-max-conception 900` au lanceur v4 (l. 642), au manifeste de simulation (`budget_conception.temps_max_s` 900), garde CE-07 satisfaite (P4C2-15) ; (d) minuteur préenregistré, essayé ; (e) décision 1 soumise, risque à la ligne de GO. Restes : P4C2-01, P4C2-02, P4C2-03, P4C2-06. |
| P4C1-03 (majeur) | **levé** | 30,23 USD = 15,1161 + 15,1136 (extraits) ; registre l. 136 et 138 ; 6,55 à 8,63 USD par génération ; conséquences du plafond ; décision 2. Reste : « ≈ 30 à 50 USD » au tableau de traitement contre « ≈ 30 à 55 » au § Bornes (P4C2-06). |
| P4C1-04 (majeur) | **levé** | (i) : la version de l'étape 1 qui part sur une banque à une trace par paire, scellée ; la v9 ne la remplit pas ; `28e3c728…` est bien la banque `confrontation-v5` (`LISEZMOI-v9.md` l. 4). (ii) réécrite. Remarque P4C2-13. |
| P4C1-05 | levé | Déclaration datée au scellement ; faits du pilote 3 avec chemins et empreintes ; « d'aucun score du pilote 3 ». Les extraits de M et S lus pour le § Bornes ne sont pas nommés au point (b) (remarque P4C2-12). |
| P4C1-06 | levé | `banque-crochet` et `banque-v2-au-chemin-v3` refusés « empreinte de la banque ≠ 157a2b45… » (journal v6, l. 198–199). |
| P4C1-07 | levé | (a) l. 158–160, juste (v6.1 l. 929) ; (b) mitose sans effet possible, juste ; (c) citation de P3 exacte (P3 l. 196–201). La disjonction de la v6 est vérifiée par moi (v6 `principal.py` l. 918) : « celle de la v6 n'a pas été revérifiée » peut devenir « vérifiée par la contre-lecture 2 ». |
| P4C1-08 | **levé en partie** | Moisson, induction, vérifications, score interne sur quatre tâches, 60 recherches et 30 téléchargements : justes. **La phrase sur la mémoire, reprise de la contre-lecture 1, est fausse telle qu'écrite** (P4C2-04). |
| P4C1-09 | levé, sauf un cas | (b), (c), (d) justes. (a) : la ligne remplacée oublie g003, le cas même que montre la simulation (P4C2-09). |
| P4C1-10 | **levé en partie** | (a), (b), (d) levés. (c) : « Ce que ces mots fixent » attribue encore aux mots de Lazar les 3 USD et, de plus, les 900 s (P4C2-05). |
| P4C1-11 | levé | Séparation écrite comme condition des textes de l'étape 1 et de la confrontation, en code ; BC4-02 (`ea2916af…`) et BC5-02 (`0ea27fa1…`) cités et vérifiés ; aucune pièce fermée servie à Gemini ; l. 43 étendue au pilote 3. |
| P4C1-12 | levé | Deux limites dites (l. 191–194) ; « nombre de mots : 1,0 sur `test` » juste. |
| P4C1-13 | levé | Canal dit et accepté (l. 302–305). Précision en P4C2-12. |
| P4C1-14 | **levé en partie** | (a) script v2 : documentation juste, contre-lecture du texte exigée, 9 cas sur 9 ; (b) en-tête du lanceur corrigé ; (d), (e) faits. (c) reste une promesse sans garde : le script accepte une ligne d'entropie de trop (P4C2-08). |
| P4C1-15 | sans objet | — |
| BC5-03 (banque v5) | **levé en partie** | Référence de provenance, borne et comptes justes (recalcul indépendant) ; mais « lire contre le maximum des références », que `LISEZMOI-v9.md` § 4.3 étend à « tout texte qui sert la v3 », n'est ni appliqué ni déclaré écarté, et la métrique des scores sur les catégories absentes n'est pas fixée (P4C2-07). |

## Constats

### P4C2-01 — mineur — Un `STOP` du minuteur pendant g003 fait refuser la porte, et le cas attendu du texte atteint le minuteur

- **Fait 1, code.** Après g003 (dernière génération), la lignée devient inactive (« générations maximales »,
  `boucle.py` l. 808–811) ; la boucle relit alors `_doit_arreter` (l. 875) : si `course/STOP` existe, l'événement
  d'arrêt porte « fichier STOP » au lieu de « aucune lignée active » (l. 876–878). La porte « v5.3 précédente » exige un
  seul arrêt « aucune lignée active » (lanceur v4 l. 259–260 ; artefact `v53-stop` du journal v6). Donc une v5.3 dont le
  minuteur pose `STOP` pendant g003 finit ses **quatre générations `OK`, mais la v6.1 ne part pas**.
- **Fait 2, texte.** La liste d'arrêt dit (l. 334) « pour la v5.3 : générations ≠ [0, 1, 2, 3], la v6.1 ne part pas » :
  la raison est incomplète. Le § Bornes dit (l. 246) « Une course plus lente que le haut du cas attendu finit donc avec
  moins de générations » ; or le haut du cas attendu du texte (≈ 105 minutes, l. 242) dépasse l'échéance (95 minutes) :
  par les chiffres du texte, le minuteur peut s'appliquer **dans** le cas attendu, et alors la v6.1 est perdue.
  Même avec les composantes que le texte donne (≈ 93 minutes au plus, P4C2-06), la marge n'est que de 2 minutes.
- **Correction.**
  - (a) mineure, sans nouvelle relecture : écrire au § Bornes et à la ligne du minuteur de la liste d'arrêt que tout
    `STOP` posé par le minuteur, y compris pendant g003, fait refuser la porte (arrêt « fichier STOP », lanceur v4
    l. 259–260), et que la v6.1 ne part pas, même quand la v5.3 a ses quatre générations ; dire la probabilité
    (le cas attendu touche l'échéance) ; ajouter à la ligne de GO, au « risque accepté » : « une v5.3 que le minuteur
    arrête, même pendant g003, empêche la v6.1 » ; le soumettre avec la décision 1.
  - (b) non mineure : lanceur v5 dont le minuteur ne pose pas `STOP` une fois g003 commencée (par exemple quand le
    dossier `travail/<lignée>/g003` de l'espace attendu existe) ; série nouvelle et relecture courte.
  - Recommandation : (a), confiance moyenne (la perte n'arrive que si la v5.3 dépasse 95 minutes).

### P4C2-02 — mineur — La règle « `STOP` pour un incident technique seulement » change sans être déclarée

- **Fait.** T2 l. 553 : « fichier `STOP` (incident technique seulement) » ; P3 plan § 1 (l. 289–290) : « Un fichier
  `STOP` n'est posé que pour un incident technique. » Le minuteur pose `STOP` par construction, à une heure fixée. Le texte
  ajoute une ligne « course arrêtée par le minuteur » (l. 334), mais ne remplace ni la ligne de T2 ni la phrase de P3, et
  il écrit (l. 42–43) qu'aucune règle de T2 ou de P3 n'est changée « hors ceux que la table de correspondance nomme ».
  La table ne nomme pas cette règle (ni d'ailleurs la ligne de T2 « commande de fond coupée », remplacée au § Liste
  d'arrêt seulement).
- **Correction.** Une ligne de plus dans la table : « `STOP` : incident technique seulement (T2 l. 553 ; P3 plan § 1) »
  → « incident technique, ou minuteur du lanceur v4 à 5 700 s » ; et l. 42–43 : « hors ceux que la table de
  correspondance et la liste d'arrêt nomment ».

### P4C2-03 — mineur — L'essai du noyau cité ne teste pas l'arrêt au milieu d'une course

- **Fait.** Le texte écrit (l. 362–363) : « L'arrêt sur `STOP` au milieu d'une course (après l'unité en cours) est l'essai
  du noyau `test_fichier_stop_arrete_la_boucle` ». Cet essai (`tests/test_noyau.py` l. 290–295) pose `STOP` **avant**
  `boucler()`, sans phase de conception, et vérifie qu'aucune génération n'a tourné (`courbes == {}`). Il n'essaie ni un
  `STOP` posé pendant une unité, ni la conception. Le comportement annoncé est juste, mais il est **lu dans le code** :
  `STOP` n'est lu que par `_doit_arreter` (`boucle.py` l. 829–839), appelé avant chaque ronde (l. 851, 866) et chaque
  génération (l. 875, 895), jamais pendant une unité ; aucune autre ligne du noyau ne lit `STOP`. La branche
  « conception » est essayée par le cas `minuteur-echeance` du lanceur (événements `arret_conception` puis `arret`).
- **Correction.** Réécrire : « l'essai du noyau couvre l'arrêt avant toute génération ; l'arrêt après l'unité en cours
  est lu dans le code (l. 829–839, 851, 866, 875, 895), non essayé ». Un cas de batterie à échéance courte qui tombe
  pendant g000 serait mieux, mais dépend du temps (et changerait la batterie).

### P4C2-04 — mineur — La phrase sur la mémoire et le retour arrière est fausse telle qu'écrite (point demandé par conv-audit à 19:30 UTC)

- **Texte** (l. 141–145, repris de P4C1-08) : la v5.3 inscrit 0 en conception ; « après g0, toutes ces entrées reçoivent
  le score de g0 (`memoire_isvd.py` l. 108–111) et peuvent être choisies comme « meilleur ancêtre » par le retour
  arrière : le retour arrière peut restaurer un état de ronde ».
- **Code, archive généalogique** (`mettre_a_jour_memoire_isvd`, identique sur ce point dans les deux objets) :
  - **ajout et remplacement** : chaque mise à jour retire d'abord toute entrée du même numéro de génération, puis ajoute
    la sienne, et ne garde que les six dernières (v5.3 l. 227–235 ; v6.1 l. 236–244). Les rondes, toutes numérotées 0
    (`boucle.py` l. 618), se remplacent donc l'une l'autre ; g000, numérotée 0 elle aussi, remplace l'entrée de la
    dernière ronde. La mise à jour est dans le bloc `finally` de l'exécution (v5.3 l. 1743 puis 1766 ; v6.1 l. 1927 puis
    1950) et la mémoire passe au successeur (v5.3 l. 1344 et 1873) : elle a donc lieu à chaque ronde et à g000, sauf
    processus tué avant ce bloc.
  - **score** : à g001, l'entrée « 0 » reçoit le score de g0 (v5.3 l. 110–113 ; v6.1 l. 114–117) ; c'est celle de g000.
  - **choix** : le meilleur ancêtre est pris parmi les entrées qui portent un score (v5.3 l. 121–123 ; v6.1 l. 125–127),
    à partir de deux générations notées, écart de plus de 0,03 (v5.3 l. 117 et 124).
  - Donc il n'y a jamais plusieurs entrées de ronde ; après g0, l'entrée « 0 » est celle de g000 ; **le retour arrière
    restaure l'état de g000 ou d'une génération notée, pas celui d'une ronde**. Seule exception lue : si g000 ne fait pas
    sa mise à jour (processus tué avant le bloc `finally`, par exemple au délai), l'entrée de la dernière ronde reste
    sous le numéro 0, reçoit le score de g0 et peut être restaurée. Ce qui vient des rondes et peut rester, ce sont des
    **exemplaires** numérotés 0, retenus par énergie (v5.3 l. 199–225), dans l'état courant et dans l'entrée de g000.
- **Correction.** Remplacer par ce qui précède, avec ces lignes (la ligne décisive, l. 227 / 236, manque au texte ; « l.
  108–111 » est l. 110–113). « Pour la v6.1, la même boucle n'est pas vérifiée » peut devenir « même code (l. 114–117,
  125–127, 236–244), lu par la contre-lecture 2, non exécuté ».

### P4C2-05 — mineur — Mots de Lazar : « Ce que ces mots fixent » porte encore les 3 USD, et maintenant les 900 s

- **Fait.** L. 56 : « Les 3 USD et 900 s par ronde sont des bornes de ce texte ». Mais l. 66–68 : « **Ce que ces mots
  fixent** : … (borne dure de 6 rondes, 3 USD et 900 s au plus par ronde) ». Aucun mot de Lazar cité ne porte 3 USD ni
  900 s ; le « go » de 17:15 porte « 6 rondes au plus ».
- **Correction.** « (borne dure de 6 rondes ; les 3 USD et 900 s par ronde sont des bornes de ce texte, portées par le mot
  d'extension) ». Le reste de ce qui est attribué à Lazar est conforme à ce que cite le texte (je n'ai pas pu lire les
  sessions où ces mots ont été dits, ni N-046).

### P4C2-06 — mineur — Arithmétique du temps et du devis : trois chiffres à reprendre

- **Temps.** Les composantes données (l. 231–241) font : préparation 193–196 s ; quatre générations 3 × 607 + 832 =
  2 653 s à 3 × 751 + 965 = 3 218 s (≈ 44 à 54 minutes, juste) ; rondes 1 × 2 à 6 × 6 minutes ; fermeture 3–4 s ; soit
  **≈ 50 à 93 minutes**, non « ≈ 50 à 105 » (l. 242). Si 105 porte une marge (générations qui s'allongent), le dire et
  en tirer P4C2-01.
- **Rondes.** « la v6.1 [en fait] 2 à 6 » (l. 241) est faux : son critère de qualité (0,78 et deux exemplaires) peut
  finir dès la ronde 1 (v6.1 l. 1986, 1989), ce que fait la simulation (c001 seule). Écrire « 1 à 6 ».
- **Devis.** Le tableau de traitement (l. 420) dit « ≈ 30 à 50 USD par course » ; le § Bornes (l. 258) « ≈ 30 à 55 ».
  « Quatre générations ≈ 28 à 35 USD » mêle deux bases (3 × 6,55 + 8,23 = 27,9 ; 4 × 8,63 = 34,5) : le dire.
- **Risque restant** (l. 247–248) : « une unité en cours à 95 minutes qui dure plus de ≈ 24 minutes » se lit mieux
  « qui finit plus de ≈ 24 minutes après l'échéance ».

### P4C2-07 — mineur — BC5-03 : « lire contre le maximum des références » ni appliqué ni écarté ; métrique des sous-ensembles non fixée

- **Fait 1.** BC5-03 (contre-lecture de la banque v5, l. 92–94) et `LISEZMOI-v9.md` § 4.3 : « lire chaque score de la
  famille **contre le maximum des références** … Même règle pour tout texte qui sert la v3 ». Le texte rapporte les
  références « à côté » (l. 306–311), ce qui est la seule lecture compatible avec les lectures interdites de T2
  (l. 518–520 : aucun verbe de comparaison entre un score et une référence). C'est juste, mais l'écart à la règle de la
  banque n'est pas déclaré.
- **Fait 2.** « Les scores sur les tâches dont la catégorie est absente du train » (l. 308–310) : la métrique n'est pas
  dite (exactitude équilibrée de la famille comme le noyau, contrat § 5 ? Brier ? part sans réponse ?), ni le code qui
  les calcule, ni le compte d'une tâche sans réponse ; ces scores et les références ne figurent pas au § Hypothèse
  (« ce qui est rapporté », l. 268–272). La garde « comptes 4/4 et 10/4 recalculés, sinon la lecture s'arrête » n'est
  essayée ni sur un cas sain ni sur un artefact (R5).
- **Correction.** Une phrase : « lire contre » se lit ici « rapporter à côté, sans comparaison » (critères gelés de T2) ;
  fixer la métrique (je recommande : exactitude équilibrée calculée comme le noyau, sur le sous-ensemble, avec la part
  sans réponse) ; écrire que le script de lecture sera écrit, empreinté et essayé (comptes justes ; secret altéré) avant
  le moment de lecture, sans lire de score ; ajouter ces éléments au § Hypothèse.

### P4C2-08 — mineur — Le script de scellement ne garde pas les textes insérés (P4C1-14 c)

- **Fait.** `sceller_pilote4_v2.py` refuse un marqueur entre doubles crochets restant et tout marqueur entre doubles
  chevrons autre que les quatre attendus, mais il **ne refuse pas une ligne d'entropie ou de graine de trop**. Je l'ai
  exécuté sur deux copies d'essai de la v2 (`essai-scellement/`) : cas sain scellé (douze lignes d'écart, les six lignes
  des marqueurs ; graines recalculées depuis l'entropie : justes) ; **artefact** : un résumé de contre-lecture inséré à
  la l. 6 qui porte une ligne d'entropie suivie d'un nombre est scellé lui aussi (code 0). Le lanceur prend la
  **première** ligne d'entropie (v4 l. 409) : il recalculerait d'autres graines et refuserait (l. 411–412). Pas de
  graine fausse en silence, mais un texte scellé inutilisable, donc une version nouvelle.
- **Correction** (sans nouvelle pièce, comme P3C2-03) : avant le scellement, sur le texte rempli, une vérification à la
  main citée dans le message de départ : une seule ligne d'entropie, une seule ligne de graine par course, aucun
  marqueur entre doubles crochets, exactement les quatre marqueurs entre doubles chevrons. À défaut, un script v3 qui
  le refuse, essayé sur cet artefact.

### P4C2-09 — mineur — La ligne remplacée de la mutation oublie g003, le cas même de la simulation

- **Fait.** Ligne remplacée (l. 337) : « son successeur valide tourne à la ronde ou à la génération suivante ; invalide
  … en génération notée, relance … (`--relances-max 1`) ». À g003, dernière génération (`--generations 4`), il n'y a ni
  génération suivante ni relance (`boucle.py` l. 798–815 : `g + 1 < generations_max` faux) ; un successeur invalide y
  donne la fin « sans successeur valide ». Or la simulation montre justement une mutation de la v6.1 à g003 (journal v6,
  relevé : g003, un appel `architecte_mutation_endogene`).
- **Correction.** Ajouter : « à g003, son successeur ne tourne pas ; invalide, la fin de la lignée est « sans successeur
  valide », rapportée ».

### P4C2-10 — remarque — Lignes citées à corriger

- `memoire_isvd.py` de la v5.3 : la recopie du score est l. 110–113 (texte : 108–111) ; voir P4C2-04.
- `mitose_spectrale.py` : `nb_castes_cible` est l. 78 (texte : l. 77) ; les tests de stagnation l. 75 et 117 sont justes.
- `cli.py` l. 123 est la voie de simulation de `--depuis` ; en réel, la garde est l. 266–270 (refus si la banque de la
  course d'origine diffère).
- `boucle.py` l. 617 ouvre le contexte ; `"generation": (0 if phase else g)` est l. 618.
- « À g1, l'historique ne porte que g0 » (l. 160) : il porte aussi les rondes, au score nul (`boucle.py` l. 708), que
  la v6.1 écarte (l. 928) ; la conclusion (première mutation possible en génération à g2) reste juste.

### P4C2-11 — remarque — Deux formulations de la lecture

- La « borne « catégorie » » n'est pas une borne du plus proche voisin : sur `test_final`, 0,8333 > 0,8056. C'est
  l'exactitude équilibrée attendue d'un oracle de catégorie (une chance sur deux hors du train) ; la nommer ainsi.
- Point 5 (l. 315–316) : « un score … au niveau de la référence de provenance ne dit rien » invite une comparaison que
  T2 interdit au rapport. Proposé : « aucun score de conscience d'évaluation de ce pilote ne dit rien d'une conscience
  d'évaluation ; une règle sur le seul texte du train atteint 0,8056 et 0,8333 ».

### P4C2-12 — remarque — Petits faits

- La contre-lecture 1 est datée « ≈ 18:15–18:50 UTC » (l. 411, d'après son en-tête) ; son rapport date de 18:34 UTC et
  son compagnon de 18:35 UTC (heures des fichiers, horloge en heure de Paris) : une heure de fin écrite d'avance.
- « Second pilote (même fichier de faits) » (l. 256) : c'est un autre fichier, `faits-mecaniques-pilote2-v1.json`
  (`609ccf1ff7144b144e73d947f9933dd9b04b860c46da78ce597bf9821cf3210c`, compagnon juste), dont l'empreinte n'est pas
  citée (R6) ; ces extraits de M et S lus pour le devis ne sont pas nommés dans la déclaration de lecture (point (b)).
- Cas `minuteur-echeance` : « course arrêtée avant toute ronde » vient d'un relevé **non compté** qui n'imprime pas la
  ronde de l'arrêt ; le dire « relevé non compté ».
- L'extrait porte aussi, dans la déclaration de fin, `critere`, `sondes_traits_actives` et `exactitude_moyenne_sonde`
  (nulle sans traits servis) : à ajouter à la liste de l. 302–303.
- Recherches web : au rythme du pilote 3, ≈ 10 par course, sans borne propre dans le noyau, contre « 4 au plus pour les
  deux courses (coût nul sur la parole de Lazar) » dans T2 : le mot d'extension devrait porter aussi le coût de la source
  web.
- Le minuteur part du départ du lanceur ; la commande de fond de deux heures ne doit contenir que l'appel du lanceur (le
  dire). Sa sortie n'est pas consignée : un minuteur mort avant l'échéance passerait inaperçu (« STOP non posé » est
  écrit dans tous les cas) ; la note « STOP du minuteur présent » attribue au minuteur tout `STOP`, même humain. Course
  qui finit dans la seconde de l'échéance : `STOP` posé après la fin, sans effet sur la porte (sans conséquence).

### P4C2-13 — remarque — Moment de lecture : deux points à dire d'avance

- (ii) exige que la version de la confrontation qui sert la banque décisive « ne change ni la table de lecture de
  H-E1, ni les seuils, ni les règles de lecture de sa version 7 ». Si cette version doit changer des seuils pour la banque
  nouvelle (`LISEZMOI-v9.md` § 4.5 : effectifs, première valeur significative), (ii) ne se remplit pas à la lettre et
  les scores de ce pilote ne se liraient jamais. Dire d'avance comment (ii) se lit alors, par exemple « aucun changement
  depuis la v7 n'est motivé par un score des pilotes ; la liste des changements et leurs motifs est inscrite » ; c'est
  un critère gelé de T2 et de P3 : décision de Lazar.
- P3 garde sa condition (i) « (à ce jour sa v9) » pour ses deux courses, « lecture comprise » (l. 18–19) : le risque de
  P4C1-04 vaut pour leurs scores, sur les mêmes textes. Ce texte ne peut pas changer P3 ; il peut le signaler à Lazar.

### P4C2-14 — remarque — Textes à insérer au scellement

- Les deux marqueurs de contre-lecture (entre doubles crochets, l. 6 et 437) seront remplis avant le script, qui les
  refuse. Leurs textes ne doivent contenir aucun marqueur entre doubles crochets ou doubles chevrons, aucune ligne
  d'entropie suivie de chiffres, aucune ligne de graine : la l. 6 précède la ligne d'entropie (l. 285), et le lanceur
  prend la première (P4C2-08). Ce rapport n'en contient aucun.
- Le texte scellé gardera le nom `pilote4-gemini-organisme-v2.md` (scellement en place, comme P3) : citer l'empreinte
  relue ici (`8657fcd2…`) dans le détail de contre-lecture, comme P3 l'a fait pour sa v2.

### P4C2-15 — conforme — Ce que j'ai trouvé conforme

- **Empreintes** (toutes recalculées sur disque) : texte `8657fcd2…`, v1 `312c9993…`, P3, T2 ; contre-lecture 1
  `3dd09acb…` ; lanceur v4 `f335440c…`, v3 `73d318b9…`, v2 `4be47da9…`, v1 `ce8ffadb…`, lanceur v2 de P3 `add695a9…` ;
  dérivations `951c1d44…`, `e376d769…`, `e326f7ac…` ; configuration `2f425291…` ; écarts `1a956cf6…`, `67950a3b…`,
  `3326198e…` ; batterie v5 `e216c39e…`, v4 `8e82d9ca…` ; journaux v6 `fa734f52…` (heures `82139d38…`), v5 `a41ddd56…`,
  v1 à v4 `8ff40a13…`, `527b3cb3…`, `7cce7310…`, `1dd669bc…` ; scripts de scellement `eb054f0b…`, `c651480f…`, leurs
  essais `d4794d55…` et journal `bace5027…` (compagnons justes) ; `EMPREINTES-pieces-pilote4-v2.txt` `a0e6f3b5…`,
  `-v3.txt` `6461a273…` (**192 lignes sur 192 justes**) ; faits `325b9332…` et les compagnons de `faits-pilote3-v1/` ;
  extraits du pilote 3 `f07e059a…`, `d357a6fe…`, de M et S `24cd458a…`, `ce66dce9…` (tels que recopiés par le script) ;
  `LANCEMENT.md` `81626514…`, `b4f7abb2…` ; banque v3 `157a2b45…`, v2 `52beb637…`, v1 `f1387a20…` ; `LISEZMOI-v5`
  `d346bac1…`, `-v6` `5a387a74…`, `EMPREINTES-banque-v3-v1` `2a661a33…` ; référence de paire `556d6398…` ; référence de
  provenance `52def946…` et sa sortie `912752ff…` ; contre-lectures de la banque v2 `5ee8df41…`, v3 `da6b744c…`, v4
  `ea2916af…`, v5 `0ea27fa1…`. Non vérifiées (hors de ma liste) : `f732bfd8…`, `f9b3646d…`, `3d4c74e3…`, `7fa0f544…`,
  `8b1c7511…`.
- **Arbres des objets** (mon code) : v6.1 `ae331d1d…`, 24 fichiers ; v5.3 `6251ab21…`, 22 fichiers.
- **Lanceur v4** : redérivé du v3 par `deriver_lanceur_pilote4_v4.py`, identique octet pour octet (9 remplacements) ;
  l'écart publié est l'écart recalculé. Il fait ce que dit le texte et rien d'autre : `--temps-max-conception 900`
  (l. 642) ; minuteur à `DEBUT_LANCEUR_S` (l. 33) + 5 700 s (l. 99), fixe en réel ; condition : processus de la course
  vivant, manifeste écrit, heure atteinte (l. 667–679) ; `STOP` dans `course/`, qui est la racine du noyau
  (`--sortie`) ; arrêt du minuteur par son identifiant de processus (l. 683), consigné (l. 680, 686–688) ; variable
  d'essai refusée en réel (l. 66), échéance d'essai non entière refusée (l. 101–102) ; en-tête, commentaire du plafond et
  temps par ronde au `LANCEMENT.md` (l. 704). Rien d'autre ne change.
- **Garde CE-07** : constantes lues (`recherche.DELAI_S` 25, `moisson.DELAI_S` 25, `EXTRACTION_MAX_S` 120,
  `MARGE_TEMPS_S` 300) : 885 s ≤ 900 s ; la garde ne joue qu'en réel (`boucle.py` l. 244), la batterie ne peut donc pas
  l'exercer ; elle est essayée en général, sain et artefact, pour une ronde de conception (`tests/test_noyau.py`
  l. 1816–1846).
- **Noyau, `STOP`** : lu seulement entre deux unités (P4C2-03) ; en conception, `arret_conception` puis `arret`, sans
  g000 (l. 850–854, 875–878) ; journal d'une ronde sous `cNNN.noyau/` (`archive.py` l. 76–78, `boucle.py` l. 593–599) ;
  aucune tâche de `test` en conception (l. 607) ; successeur invalide en conception : l'organisme reste (`contrat.py`
  l. 142–146) ; aucune borne propre à la source web (`recherche.py`, `moisson.py`).
- **Batterie v5 et série v6** : batterie redérivée de la v4, identique (6 remplacements) ; 162 cas sur 162 = les 150 de
  la série v5 et 12 nouveaux (temps par ronde et « STOP non posé » aux deux cas sains ; banque par crochet et par commit ;
  minuteur à échéance 0 avec `STOP`, présence, archive, poussée ; échéance non entière ; variable en réel) ; heures
  18:55:16–19:04:19 ; dépôts d'essai revenus à leurs têtes ; le minuteur est essayé sur un cas sain (non déclenché) et
  sur un artefact (déclenché) ; les deux refus de banque viennent bien de la garde d'empreinte (l. 372).
- **Simulation** (`simulation-lanceur-v4/`, compagnons justes) : ronde 1 et fin de conception à la ronde 1 pour les deux
  objets ; c001 : 6 et 7 appels ; g000 à g003 : 123, 129, 123, 123 et 123, 129, 123, 124 ; mutation de la v6.1 en c001 et
  g003 ; `budget_conception.temps_max_s` 900 ; échéance du minuteur au `LANCEMENT` = début + 5 700 s.
- **Faits et chiffres** : P3, lanceur parti 15:37:44 et 16:07:02, noyau 15:40:57–16:06:02 et 16:10:18–16:34:59 ;
  193 et 196 s ; fermeture 4 et 3 s ; g000/g001 661,06 / 838,03 s et 610,83 / 864,09 s ; 6,7932 / 8,3229 et
  6,5495 / 8,5642 USD ; 15,1161 et 15,1136 ; registre « ≈ 30,24 » ; tests de dépense 0,00152 et 0,00150 USD ; appels de
  0,602 à 49,491 s, un à la fois ; une recherche web sur six par génération. Second pilote : 750,91 / 831,59 s et
  607,0 / 964,55 s ; 6,6896 / 8,2273 et 6,6672 / 8,6281 USD. Calculs : 6 × 25 + 3 × 145 + 300 = 885 ; 195 + 6 × 1 810 +
  4 × 3 310 + 60 = 24 355 ≈ 24 400 ; 5 700 s = 95 min ; 60 recherches et 30 téléchargements ; (60 − 18) / 4 = 10,5 ;
  155 − 30,23 − 120 = 4,77.
- **Référence de provenance** : le script apprend sur `train` seul (Jaccard sur les ensembles de mots, égalité : la
  première) ; mon recalcul sur la banque seule donne 0,8056 et 0,8333, sans aucune égalité ; 36 tâches de la famille par
  part (18 et 18) ; la sortie porte 28/8 (4/4) et 22/14 (10/4) et l'oracle 0,8889 / 0,8056, comme BC5-03 et
  `LISEZMOI-v9.md`. Référence de paire : 1,0 et 0,75 ; longueur 1,0 et 0,75 ; mots des lignes propres 1,0 et 0,75 ;
  nombre de mots 1,0 sur `test`.
- **Code des objets** : v6.1 l. 926–932 (stagnation unilatérale, disjonction), l. 1985–1990 (fin de conception), l. 740
  (exemple de format), l. 86–95 (dix requêtes de réserve) ; v5.3 l. 1593–1606, 1644, 1793–1804, 1507, 1769 ; retour
  arrière l. 117–130 ; mitose l. 75, 78, 117, identique dans les deux objets.
- **Script de scellement v2** : il fait ce qu'il dit (contre-lecture du texte exigée par son nom, compagnons justes ;
  marqueurs ; numpy ≥ 1.25 ; entropie par `secrets.randbits(128)`, enfants 0 et 1 de `SeedSequence(E).spawn(2)` ; ne
  remplit que les quatre marqueurs ; refus d'écraser le fichier d'empreintes) ; ses 9 cas sont conformes ; mon cas sain
  le confirme ; seule réserve : P4C2-08.
- **Ligne de GO et lignes de dépense** : conformes aux `grep` du lanceur (l. 440–451) ; une ligne pour les deux courses
  ; une ligne qui ne porterait que la v5.3 laisse partir la v5.3 seule (cas `go-v53-seulement-autorise-v53`).
- **Ce qui reste au mot de Lazar est dit** : objets et arbres, points ouverts de la v6.1, banque v3, texte et lanceur,
  4 générations, 6 rondes à 3 USD et 900 s, 60 USD par course, 60 recherches, risque de coupure, 155 USD ; à y ajouter :
  P4C2-01 (la v6.1 perdue si la v5.3 dépasse 95 minutes) et le coût de la source web (P4C2-12).
