# Contre-lecture de l'addendum des témoins du juge et du budget de pensée de Carbon (organisme d'idéation, organismes discrets) — v1

Contre-lecteur neuf (R2), modèle Opus 5.5 : je n'ai écrit ni l'addendum, ni le diagnostic, ni sa contre-lecture, ni les
témoins, ni le script d'épreuve, ni les lanceurs. 18 novembre 2026.

Pièce lue : `addendum-temoins-et-carbon-v1.md` (`f80351be…`, non scellé au moment de la lecture). Pièces d'appui, empreintes
vérifiées par leurs compagnons `.sha256` (toutes conformes) : `diagnostic-temoins-v2.md` (`31d68ed2…`),
`contre-lecture-diagnostic-temoins-v1.md` (`830f71c7…`), `temoins-organisme-discrets-v1.json` (`1c6eef38…`), `-v2.json`
(`5e8a276e…`), `-v3.json` (`611c50a2…`), `question-v3.md` (`2f7acf36…`), `faits-v3.md` (`5e2e9dd8…`),
`scripts/epreuve_temoins_seuls_v1.py` (`0b50b579…`), `epreuve-lot-carbon-v1/` (trois pièces) ; journal de la relance, entrées
OD-013 à OD-023 ; orchestrateur épinglé (`a41b7b50`, arbre `orchestrator` = `ee84d6ec…`, vérifié), `pole/ideation_v2.py`,
`pole/adaptateurs.py`, `pole/relais_reel.py` ; manifestes de pré-départ et de fin d'Astra et d'Argon (copies dans `runs/`).

**Ce qui n'a pas été ouvert.** Aucune fiche de proposeur, aucun `fiches-*.json`, aucun dossier `proposeurs/`, aucun
`consigne.md` ni `reponse.md` de juge des courses. Deux écarts de forme, déclarés : (1) `ls` du dossier `sortie/juges/` d'Astra
(noms de fichiers seulement) pour trouver le chemin à donner à `--verifier-gabarit` ; (2) `--verifier-gabarit` lancé sur les
consignes du juge d'Astra et d'Argon (booléen seul affiché). Les consignes que j'ai lues sont celles que le script fabrique
en mode à sec, qui ne contiennent que les quatre témoins. Sorties de mes essais : `/tmp/cl-addendum-*` (hors du dépôt).

## Verdict

**À corriger.** La forme (script de ce dépôt sur le code épinglé, règle d'arrêt écrite d'avance) est la bonne, et le script
reproduit bien le gabarit des deux courses. Mais : (1) le vrai témoin v3 et son jumeau contiennent une prédiction
logiquement impossible et un argument d'incopiabilité faux au vu de leur propre texte, ce qui donne à un juge correct des
raisons légitimes de les noter 1, comme pour la v1 ; ce défaut se corrige sans dépense, avant l'épreuve ; (2) la règle d'arrêt
laisse trois libertés après coup (rejeu dans un autre dossier, code 3 après une réponse reçue, deux textes contradictoires sur
la reprise) ; (3) le plafond de 0,5 USD n'est garanti par aucun mécanisme, et aucune ligne de GO n'est citée pour la
dépense ; (4) au § 4, la première ligne du tableau est inexacte et l'option recommandée (B) repose sur un budget de pensée
(2 048) qui n'a jamais été essayé.

## Vérifications faites

| point | résultat |
|---|---|
| Témoins v3 contre le code épinglé (mon programme, `python3 -I -B`, `sys.path.insert(0, ORCH)`, aucun fichier de l'orchestrateur modifié) | `valider_fiche_ideation` : les quatre passent ; `signaux_niveau_methode(vue_servie(·))` : vide pour les quatre ; `charger_temoins` complet (liste blanche à l'empreinte) : passe, quatre classes |
| Faux v3 identiques à la v1 | oui, égalité d'objets JSON pour les deux faux ; paire v3 identique à la paire v2 |
| Longueurs servies (`texte_plat(vue_servie)`, comme `_longueurs_temoins`) | vrai 4 549, jumeau 3 870, faux 2 407 et 2 606 : conformes à l'addendum l. 42 et l. 44-45 ; fourchettes d'Astra 3 353 à 4 808, d'Argon 2 677 à 5 404 (manifestes de fin) |
| Termes de l'idée dans la question v3 et les faits v3 | « restaur », « octet », « isolement », « certificat », « manipulation », « fuite », « défaire », « identique », « réversib », « aller-retour », « intervention », « attachement », « permutation inverse » : 0 occurrence ; « graine » : faits seulement (l. 8, 2 fois) ; « invariant » et « programme pur » : question l. 8 (sous-question 2) ; « invers » : question l. 7, mot « inversement » sans rapport |
| Gabarit de la consigne (`--verifier-gabarit`) | égal à la consigne du juge d'Astra et à celle d'Argon sans `--citations` ni `--moisson` (code 0) ; inégal avec `--citations` (code 2). Les courses n'avaient pas de dossier fermé ni de moisson (commande de pré-départ d'Astra : aucun drapeau de ce nom) : réglage par défaut du script conforme |
| Graine et étiquette | graine 2026111808 dans les deux manifestes de fin ; étiquette `opus-juge` conforme au juge des courses |
| Épreuve à sec | code 0, consigne de 24 561 caractères (conforme l. 64), empreinte `1f68410b…`, quatre fiches servies sans champ interne ; second lancement dans le même dossier : refus, code 2 |
| Lecture, essayée avec un faux ouvreur substitué en mémoire (aucun processus de relais lancé, aucun réseau) | quatre témoins tenus → 0 ; vrai à (1, 1) → 4 ; jumeau non signalé en doublon → 4 ; modèle servi autre → 3 ; une note omise par le juge → 3 avec `reponse-brute.json` écrit ; délai dépassé → 3 ; bloc leurre avant le vrai bloc → lecture du dernier bloc (4) ; empreinte de pièce fausse → sortie 1 (pas 2) |
| Corrections du § 1 contre la contre-lecture | (a) = constat 2, (b) = constat 3, (c) = constat 9, (d) = constat 10 (traitabilité du jumeau 2 à Astra, 3 à Argon : vérifié aux manifestes de fin), (e) = constat 11, (f) = constat 6 : fidèles. Constats 7, 8 et 12 repris aux § 2 et § 3. Constats 4 et 5 : non suivis, voir constat 5 ci-dessous |
| Tableau de Carbon (§ 4) | lignes 2 à 5 conformes au journal (OD-016, OD-020, OD-023) et à `journal-epreuve-lot.txt` (430 s, 844 jetons de pensée, `gemini-4-carbon`) ; ligne 1 inexacte (constat 6) |

## Constats

### Bloquant

1. **Le vrai témoin v3 et son jumeau se contredisent eux-mêmes sur les deux critères qui décident de la porte**
   (`temoins-organisme-discrets-v3.json` l. 11, 14, 16, 26, 65, 77 ; addendum l. 35-42). La condition (ii) du diagnostic
   (`diagnostic-temoins-v2.md` l. 85-86 : un avantage « dit dans la fiche sans la contredire ») n'est pas remplie, et un juge
   correct a des raisons légitimes de mettre 1, c'est-à-dire de reproduire exactement le défaut diagnostiqué.
   - **Prédiction impossible** (l. 14 et métrique l. 16) : « les moniteurs gardent une aire sous la courbe supérieure à 0,60
     sur les seules instances restaurées identiques au jumeau […] : c'est la signature d'une fuite hors des champs
     restaurés ». Si la production restaurée est identique octet pour octet au jumeau, rien d'autre que l'attachement des
     champs CONTROLS ne diffère : soit on note les productions restaurées, identiques, et l'aire vaut 0,50 par construction
     (prédiction infalsifiable) ; soit on note les productions permutées de ces instances, et une aire au-dessus de 0,60 mesure
     la détection de la permutation elle-même, jamais une fuite « hors des champs restaurés ». La branche « fuite » de la loi
     prédictive est vide.
   - **Incopiabilité fausse** (l. 26 et l. 77) : « Sans la graine scellée, un tiers doit retrouver le dérangement parmi toutes
     les permutations sans point fixe ». Le test exige le jumeau (l. 25) ; or les faits disent que la valeur du champ est
     échangée en entier (`faits-v3.md` l. 8) : avec le jumeau en main, le dérangement se lit par simple appariement des
     valeurs des champs CONTROLS, sans graine ni recherche. L'avantage se réduit à l'accès aux pièces du banc (jumeau,
     référence cachée), soit le même avantage que le vrai témoin v1, noté 1 deux fois avec la raison « les données […] sont
     propres au programme, mais […] se reproduit à faible coût » (`diagnostic-temoins-v2.md` l. 43).
   - **Prémisse en tension avec les faits** (l. 14 « si le protocole est sain, au moins 99 % des instances se restaurent » ;
     l. 65 pour le jumeau) : les faits mesurent une erreur de correspondance du coût en jetons générés entre saboteur et
     jumeau, avec une tolérance de 10 % (`faits-v3.md` l. 21), et parlent de budgets « appariés » (l. 8). Ils supposent donc
     deux générations qui peuvent différer : avec un échantillonnage à température 1,0, l'identité octet pour octet exige en
     plus une inférence déterministe, que les faits ne donnent pas. Si l'on suppose au contraire que la permutation est
     appliquée à la production même du jumeau, le test devient tautologique (ce que la fiche concède dans `cosmetique_si`, l. 41). La
     « perte de traduction » (l. 18) couvre le cas, mais la prédiction principale qualifie de « sain » un état que les faits
     ne garantissent pas.
   - **Originalité portée par la seule déclaration** : l'antériorité (l. 42-52) ne discute que les contrôles de manipulation
     et les tests de permutation, pas les voisins les plus proches qu'un juge citera vraisemblablement : tests d'aller-retour
     et de réversibilité, tests métamorphiques (Chen, Cheung et Yiu, 1998, SUPPOSÉ), tests différentiels (McKeeman, 1998,
     SUPPOSÉ). Et l'invariant contrôlé (« seuls les champs CONTROLS sont touchés ») est posé par les faits mêmes
     (`faits-v3.md` l. 8), ce qui invite à le noter comme un contrôle d'implémentation.
   **À faire, sans dépense, avant l'épreuve** : une paire v4 (nom neuf, v3 archivée) qui retire la branche « fuite sur les
   instances restaurées » ou la remplace par une prédiction réalisable (par exemple sur les instances **non** restaurables),
   corrige l'argument d'incopiabilité (l'avantage tient au jumeau apparié et à la référence cachée, pas à la graine), dit
   comment l'identité est atteignable au vu des faits (ou en fait une prédiction conditionnelle), et discute les tests
   d'aller-retour et métamorphiques dans l'antériorité. Même vérification hors ligne que ci-dessus, longueurs dans
   l'intersection 3 353 à 4 808. Sinon, dire dans l'addendum que l'épreuve a une forte probabilité d'échouer et qu'un échec
   coûtera un cycle complet (règle 1).

### Significatifs

2. **Rejeu possible : « un seul tirage » est une promesse, pas un verrou** (addendum l. 65 ; script l. 4, l. 99-100, l. 109).
   Le script refuse seulement un dossier de sortie qui existe déjà : un second appel dans un autre dossier passe. Le mode à
   sec crée lui aussi un dossier, si bien que l'appel réel se fera forcément ailleurs que le dossier de l'essai. Les drapeaux
   `--citations`, `--moisson`, `--max-tokens` et `--url-relais` restent libres à l'appel réel, alors que l'égalité du gabarit
   n'est vérifiée que dans une invocation séparée. **À faire** : fixer dans l'addendum la commande exacte (dossier de sortie
   nommé dans le dépôt, sans drapeau, `--max-tokens 16000`) et l'empreinte attendue de la consigne (`1f68410b…`), et que le
   script refuse tout autre dossier, ou tout dossier si une trace d'épreuve existe déjà ; ou écrire que tout second dossier
   est une violation de la règle et que seul le premier compte.

3. **Code 3 : deux textes contradictoires, et une reprise sélective possible** (addendum l. 70 « ne se rejoue que sur un mot
   de la mère » ; script l. 21 « ne se rejoue que sur addendum » ; script l. 128-138). Le code 3 couvre aussi des réponses du
   juge reçues et écrites sur disque (modèle servi autre, bloc de notes invalide ou note omise : vérifié, `reponse-brute.json`
   est écrit). Rien n'interdit de lire cette réponse, d'y voir un témoin manqué, puis de rejouer : c'est un tirage choisi
   après coup. **À faire** : un seul texte ; un code 3 survenu après une réponse reçue compte comme un échec (règle 1), ou la
   réponse est scellée et non lue tant que la reprise n'est pas décidée ; au plus une reprise, toutes les tentatives sous le
   même plafond.

4. **Le plafond de 0,5 USD n'est tenu par aucun mécanisme, et la dépense n'a pas de ligne de GO citée** (addendum l. 64-65,
   l. 108-109 ; script l. 93, l. 115). Le script ne borne que `max_tokens` (argument libre, défaut 16 000). Aux prix du relais
   Claude épinglé (Opus 5.5 : 4 USD en entrée et 20 USD en sortie par million de jetons, `pole/relais_reel.py` l. 50), un appel
   de cette taille coûte au pire environ 0,36 USD : le plafond tient pour **un** appel au défaut, pas pour une reprise (code
   3 sur délai dépassé, facturé ou non), ni pour un `--max-tokens` plus grand. Le relais Claude des courses avait un plafond
   de 22 USD (OD-013) et a été arrêté (OD-022) : l'épreuve en relancera un. Aucune ligne de GO n'est nommée pour cette
   dépense (GO-2026-11-18-16 couvre la relance des courses coupées ; GO-2026-11-18-17 est la lignée Kimi). **À faire** :
   relais lancé pour l'épreuve avec `--plafond-usd 0.5` (le relais garantit son plafond, `pole/relais_reel.py` l. 139-146), et la ligne de GO et le
   cumul sur lesquels la dépense s'impute, écrits dans l'addendum.

5. **Le juge de l'épreuve n'est pas réglé comme celui des courses, alors que c'était possible sans frais ; le nombre de fiches
   biaise vers la réussite** (addendum l. 61-62 ; script l. 115-116). Dans les courses, le juge recevait la consigne système
   `CONSIGNES_SYSTEME["juge_ideation"]` (`pole/adaptateurs.py` l. 108-111) et un effort de réflexion « medium » (l. 55) ;
   le script n'envoie ni l'une ni l'autre (le relais transmet le corps tel quel). L'écart déclaré (« pas une session de
   l'adaptateur ») ne nomme pas ces deux différences, qui portent pourtant sur la façon de noter. Par ailleurs, quatre fiches
   dont deux faux évidents créent un contraste favorable aux deux bonnes ; la contre-lecture du diagnostic demandait 14 à 16
   fiches et plusieurs tirages (constats 4 et 5) : l'addendum ne les suit pas et ne dit pas pourquoi. **À faire** : importer
   la consigne système et l'effort depuis le code épinglé (sans le modifier) ; écrire en une phrase pourquoi quatre fiches et
   un seul tirage suffisent pour une épreuve dite « nécessaire, pas suffisante » (coût d'un faux succès : une course Kimi
   illisible, environ 1 à 1,5 USD), ou ajouter des fiches neutres écrites d'avance.

6. **Tableau de Carbon, première ligne inexacte** (addendum l. 82). « Coupure à 300 s (deux fois, course) » : la première
   course a été coupée à **69 s** par le mandataire réseau du conteneur (« server_draining », cause d'infrastructure, OD-015,
   journal l. 34) ; seule la relance a été coupée à 300,1 s (OD-016, l. 35). Le coût est de 1,53 USD **par course**, 3,06
   pour les deux. La ligne sert d'appui à « avec 8 192, Carbon reste muet » : elle compte pour deux une observation qui n'en
   vaut qu'une. Les sources de la ligne sont OD-015 et OD-016, pas seulement OD-020 (l. 78).

7. **L'option recommandée (B) repose sur un budget jamais essayé** (addendum l. 84-85, l. 93-97). Seul le budget 1 024 a été
   essayé, sur une question triviale (4,5 s sans flux, 46 s en flux) ; 2 048 ne l'a jamais été, ni sur une consigne de
   course (11 085 caractères pour les proposeurs, manifestes de fin). L'épreuve par lot montre en outre que, sur la question
   triviale, Carbon n'a pensé que 844 jetons avec un budget de 8 192 (`journal-epreuve-lot.txt` l. 18) : la cause « c'est le
   budget de pensée » (OD-020) n'est donc pas expliquée par une pensée longue, et rien ne garantit que 2 048 se comporte comme
   1 024. Le risque de (B) n'est pas écrit : une course coupée de plus, environ 1,53 USD au pire cas. **À faire** : un
   appel d'épreuve à 2 048 (moins de 0,01 USD, signalé), ou écrire ce risque dans l'option (B) ; présenter la décision au
   format du dépôt (décision en une phrase, enjeu : comparabilité avec Argon contre délai et préparation).

### Mineurs

8. Docstring du script, l. 3 : « si le juge échoue un seul témoin v2 » ; le script sert la v3.
9. Codes de sortie (script l. 20-21, 47, 64) : un refus d'empreinte ou de classes sort en **1** (`SystemExit` avec un texte),
   pas en 2 ; une fiche invalide sort en 1 avec une trace. La règle d'arrêt (l. 67-74) ne dit rien des codes 1 et 2 (aucune
   dépense : « rien n'est parti ; corriger et revérifier » suffit).
10. « Éprouvé contre un faux relais » (addendum l. 60) : aucun essai n'est versé au dépôt ; je l'ai refait (tableau
    ci-dessus), les codes 0, 4 et 3 se comportent comme annoncé. Verser l'essai ou citer mon rapport.
11. Le vrai témoin dit la graine « scellée » (`temoins…-v3.json` l. 11) ; les faits disent « tiré par graine » (l. 8), sans
    scellement.
12. Sous-question 2 servie de loin (`temoins…-v3.json` l. 19-22, 70-73) : elle porte sur l'écart entre la vérification par
    chaînes exactes et les deux lecteurs ; l'invariant du témoin ne touche pas cet écart. Et elle invite tout proposeur à un
    « invariant vérifiable par programme pur » (`question-v3.md` l. 8) : risque de doublon en course, le mécanisme qui avait
    tiré l'originalité du vrai v1 vers le bas (« Doublon de T04 »).
13. « Écrits à la lettre de la grille » (addendum l. 33) reprend l'excès corrigé en (a) l. 21-23 : la grille ne définit pas
    la note 2.
14. Épreuve par lot de Carbon : la question posée n'est pas versée dans `epreuve-lot-carbon-v1/` (le script la lit en
    argument), donc « réponse juste » ne se vérifie pas sur pièce ; le coût « ≈ 0,005 USD (moitié prix) » est donné sans
    source de prix ; 430 s est la durée vue du client (401 s entre création et fin côté serveur).
15. L'empreinte de la consigne de l'épreuve n'est pas inscrite dans l'addendum (seule sa taille l'est).
16. Le jumeau prédit « l'écart relatif de jetons générés […] est nul sur ces instances » (l. 65) : vrai par construction sur
    des productions identiques ; ce n'est pas une prédiction.
17. Règle muette sur une course Kimi close sans lecture des témoins (coupure, aucune fiche) : Carbon part-elle ? (l. 71-73,
    l. 109-110).
18. La v3 est « assemblée » à la main (addendum l. 34) : dire qu'elle a été vérifiée égale à la paire v2 et aux faux v1
    (vérifié ici).

## Ce qui tient

- Les témoins v3 passent la validation, la garde du niveau méthode et le chargement complet de l'orchestrateur épinglé ; les
  faux sont ceux de la v1 à l'identique ; la paire vrai et jumeau est un vrai jumeau (même mécanisme, même métrique, l'un
  en approche et l'autre en question).
- L'idée de la paire est absente de la question v3 et des faits v3, synonymes compris ; elle sert la sous-question 1.
- Le script reproduit l'anonymisation, la graine, l'étiquette, la question, la pièce du juge caviardée et la consigne des
  courses jusqu'aux fiches (égalité vérifiée sur les deux courses) ; sa lecture appelle `valider_notes` et `lecture_temoins`
  sans les modifier, et les codes 0, 4 et 3 sont conformes ; il n'écrit que dans son dossier et ne lit aucune fiche.
- Les corrections (a) à (f) du § 1 reprennent fidèlement les constats 2, 3, 9, 10, 11 et 6 de la contre-lecture.
- La règle 3 (« la course elle-même est l'épreuve suffisante ») et la règle 1 (aucune retouche sans addendum neuf) sont
  fermées.

## Pour que l'addendum soit autorisable

Paire v4 corrigée (constat 1) ; commande exacte, dossier imposé et empreinte de consigne (2, 15) ; un seul texte sur le
code 3 et sur les reprises (3) ; plafond tenu par le relais et ligne de GO citée (4) ; consigne système et effort du juge
importés, ou écart nommé et argumenté (5) ; tableau de Carbon corrigé et risque de (B) écrit, ou budget 2 048 essayé (6,
7). Puis nouvelle contre-lecture courte des seules parties changées.
