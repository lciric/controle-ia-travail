# Contre-lecture du lanceur de la course « Regard ou raisons » de l'organisme d'idéation — v1

Contre-lecteur neuf, **modèle B** (autre que l'auteur du lanceur d'origine ; je n'ai écrit aucune des pièces lues),
sous-agent de la session mère. 14 novembre 2026, de 09:49 à 10:02 UTC (heures relevées par `date -u`). **Aucune course
lancée, aucun modèle appelé, aucun appel réseau, aucune dépense ; aucune valeur de clé lue ni affichée ; rien commité, rien
poussé ; aucun fichier lu n'est modifié** (lanceur revérifié à son compagnon à 09:59 UTC ; clone de l'orchestrateur resté
propre, fichiers ignorés compris ; aucun dossier de production créé). Non ouverts : `bilan-mere-v1.md`, `collisionneur-v1/`,
le dossier de run et les dossiers `lecture-*` de la course précédente. Aucun refus de permission.

## Verdict

**« Lançable sous conditions »** (six conditions, § Conditions). **0 bloquant, 1 majeur d'emploi, 8 mineurs.** Aucune
correction du code n'est exigée avant le lancement ; les corrections valent pour un v2 éventuel (R12).

Réponses aux sept points, dans l'ordre demandé :

1. **Dépense.** Dépôt intact, le lanceur ne peut pas engager plus de **17 USD** : une course est bornée à 14,9, et la
   relance n'est admise que si la première tentative, finie proprement et sans fiche, a un relevé lisible d'au plus 2,1.
   La ligne à 25 USD ne relève pas cette borne. **Exception (constat A)** : si le dossier de run est perdu avant d'être
   commité et poussé, le lanceur repart de zéro et peut engager 14,9 + 17 = **31,9 USD, au-dessus de la ligne**.
2. **Ligne de GO.** Trouvée par son contenu, seule : **GO-2026-11-14-01, calcul, 25 USD, Lazar, jusqu'au 30 novembre**
   (joué en lecture seule sur le registre réel à 09:50 UTC ; aucune autre ligne du registre ne contient « regard ou raisons »).
3. **Gardes héritées.** Intactes : le différentiel versé est égal, ligne pour ligne, à celui que je recalcule (116 lignes
   changées, toutes lues) ; il ne touche ni l'environnement, ni le bac à sable, ni le verrou, ni l'orphelin, ni la clôture.
   A2 n'est pas sans danger ici (constat A) ; m1, m2, m7 et m8 sont sans danger pour l'argent sous les conditions C2 à C4.
4. **Question servie.** Fond identique à `question-v1.md`, octet pour octet (vérifié par mon programme) ; forme ajoutée
   neutre ; aucune phrase destinée à tromper un modèle ; aucun chiffre non publié du projet ; faits servis = `faits-v1.md`
   lui-même, par son chemin et son empreinte.
5. **Témoins.** Aucune affirmation fausse ; deux affirmations non établies (constat m4) ; servis au seul juge.
6. **Devis.** Tous les calculs recalculés sont justes.
7. **Mutants.** 26 mutants à moi, distincts des 61 du préparateur : **20 tués, 6 survivants** (lacunes d'essai ; le code
   est juste à la lecture et aux épreuves).

## Ce que j'ai lu et vérifié

- Empreintes contre compagnons, avant lecture, toutes « OK » : lanceur `3b2dcb117cd4a3074099000374f8b0608ad301d9306da07d25cb360bcce1302f`,
  essais `509fc85d…`, question servie `2c19b11c…`, témoins `b5854643…`, devis `1d9628bc…`, rapport du préparateur
  `b870d03f…`, deux différentiels (`411b7dd2…`, `2ccc7c6f…`), les sept pièces de `outils/`, `faits-v1.md` `87086190…`,
  `question-v1.md` `f0481482…` (les deux dernières égales à celles de R-2682).
- Lanceur lu en entier (1 249 lignes) ; lanceur de référence par le différentiel ; contre-lecture précédente lue en entier.
- Gardes de production jouées **en lecture seule** par `/usr/local/bin/python3 -I -B`, sans lancement : ligne de GO ; cinq
  pièces à leur empreinte ; aucun run, aucun dossier de sorties ; sommes 9,9 ≤ 10 et 7,6 < 8, exposition externe 4,9 ;
  garde de cumul 0 + 14,9 ≤ 17 ; gardes de taille recalculées sur la mesure versée, égales à la pièce versée.
- Orchestrateur : arbre `ee84d6eca7a4c9b25f4e297ca29c6d9f24af5d70` (relu par `git rev-parse`), le même que celui de la
  course précédente. J'y ai lu trois choses seulement : le chargement des témoins, le filtre lexical, le code de sortie.

## Constats

### Majeur (d'emploi ; aucun défaut neuf du code)

**A — A2 repris tel quel casse la ligne, et non plus seulement la borne.** Lanceur l. 778 (`if not d_runs.is_dir(): return []`),
l. 937-945, l. 948-963. Le lanceur ne connaît la dépense passée que par `runs/course-ideation-regard-ou-raisons-v1/`,
dans l'arbre de travail. Si ce dossier est perdu avant commit et poussée (conteneur remplacé : c'est arrivé le
13 novembre), il ne voit aucun run : course neuve (14,9), puis relance. Pire cas : 14,9 perdus + 17 = **31,9 USD > 25**.
Le lanceur ne lit pas `registres/depenses.md`. *Emploi* : C2 et C3.

### Mineurs

- **m1 — m1 de la contre-lecture précédente, même enjeu que A.** L. 808 et 950 : un départ au code 5 suivi de la perte du
  dossier hors dépôt compte 0 USD et ne compte pas parmi les deux courses. Double panne. Mon mutant R01 (une course sans
  manifeste de départ n'est plus comptée) **survit** : aucun essai ne joue « code 5, puis deux courses ». *Emploi* : C4.
- **m2 — Le bloc « bilan de l'organisme » dépend du juge.** L. 1101 : le bloc n'est écrit que si l'orchestrateur sort
  au code 0. Or l'orchestrateur sort au code 4 quand le juge ne lit pas les témoins comme attendu
  (`demonstrations/ideation_v2.py` l. 1501 et 1508), et le préparateur dit lui-même que des témoins honnêtes éprouvent
  moins le juge. Sans effet sur l'argent ni sur les fiches : `fiches-validees.json` est écrit avant le juge
  (`pole/ideation_v2.py` l. 2538, juges l. 2545) et copié quel que soit le code (lanceur l. 906-910). Mais la question
  servie promet que les notes du juge ne servent à rien. *Emploi* : C6.
- **m3 — Six gardes sans essai qui les isole** (mutants survivants, § Mutants) : trois lectures du dossier de contrôle
  (l. 849, 853, 857), la frontière de la garde de cumul entre 2,0 et 2,2 USD (l. 942), la forme exacte du plafond
  (l. 325), le compte des courses sans manifeste de départ (l. 950).
- **m4 — Témoins : deux affirmations non établies, aucune fausse.** Témoin « vrai », champ `perte_traduction` : « faute
  d'accès à ces données » ; les faits ne disent pas que les données d'entraînement sont inaccessibles. Témoin « faux
  d'antériorité », champ `enonce` : le constat du travail [9] est écrit comme un fait général, alors que les faits le
  donnent comme rapporté (la fiche le dit dans `perte_traduction` et `originalite`). Le champ `auteur_tiers`, inexact
  (erratum du préparateur), n'est ni lu ni servi : `charger_temoins` ne lit que la liste `temoins`
  (`pole/ideation_v2.py` l. 595-617). Les témoins ne vont qu'au juge (l. 2546) ; lanceur l. 981.
- **m5 — La question servie va aussi au juge**, qui y lit « Tu es un proposeur » et la contrainte d'écriture
  (lanceur l. 979 : une seule pièce `--question`). Sans effet sur les fiches ; peut peser sur m2. Elle porte des renvois internes
  (numéros de registre, début d'empreinte), déjà présents dans `question-v1.md` : aucun chiffre du projet.
- **m6 — Révocation reconnue seulement par une ligne de type « révocation » qui cite l'identifiant** (l. 356-361 ;
  épreuve 06 : une révocation écrite dans le périmètre d'une ligne « calcul » passe). C'est la convention de l'en-tête
  du registre. Une ligne « extension » n'est pas lue (épreuve 08) : sans effet, la borne reste 17.
- **m7 — m2, m7, m8 repris tels quels.** m2 (clôture non reprenable, l. 1090 et 1108) : sens fermé, nœud à la main.
  m7 (fenêtre d'orphelin) : argent gardé par les plafonds. m8 (garde de soi contre l'accident, l. 315) : la ligne de GO
  ne porte pas l'empreinte du lanceur, à la différence de la précédente ; la comparer à R-2691 et à ce rapport (C1).
- **m8 — Écritures sans effet.** L. 70 et 1189 : le commentaire et le champ `decision` du pré-départ citent R-2679 et
  R-2680, non R-2682 (l'identifiant du GO est dans le champ `go`). L. 940 : `min(BORNE, plafond)` vaut toujours 17,
  puisque la ligne est refusée sous 17 (l. 377).

### Ce qui tient

- **Borne.** `garde_cumul` : relevé + 14,9 ≤ min(17, plafond). Épreuves à la frontière, ligne à 25 USD : première
  tentative à 2,1 admise (engagement 17,0), à 2,2 refusée. Deux courses au plus ; relance seulement après code scellé,
  aucune fiche (validée, refusée ou en quarantaine), relevé lisible. Dépense illisible : plafond entier, relance fermée.
- **Marge de la ligne.** Si le juge externe différé était joué (il ne l'est pas : aucun bras, drapeau interdit), une
  course vaudrait 10 + 7,6 = 17,6 et 19,7 relance comprise : sous 25.
- **Ligne de GO.** Vingt épreuves : seconde ligne aux deux expressions, révocation en forme, révocation sous le même
  identifiant, ligne citante mal formée, espace insécable, plafond sous 17, en euros ou à suffixe, hors période, autre
  type, autre accordant : **refus** ; ligne réelle seule, ou avec une ligne voisine sans « organisme d'idéation » : admise.
- **Environnement.** Cinq noms permis, trois fixés par le lanceur ; noms exclus jamais écrits ; aucun mandataire, aucune
  adresse d'hôte, aucune clé (mutants E01, E02, E04, E05, K01 tués). Bac à sable actif et `/proc` neuf exigés (B01 tué).
- **Question.** Bloc de 2 418 caractères (2 504 octets) présent une fois, à l'octet. La forme ajoutée ne porte que des
  dates et des renvois. La contrainte d'écriture décrit fidèlement le filtre (`MOTIFS_NIVEAU_METHODE`, l. 212-222) ; elle
  omet deux familles peu probables ici (« jailbreak », « stéganographie »).
- **Devis.** 0,4 + 4 + 4 + 1,5 = 9,9 ; 1,7 + 1,3 + 1,9 = 4,9 ; 14,9 ; 2,1 ; 17,0 ; relais 10,4 et 6,6 ; option 16,1 ;
  planchers d'Argon 1,346, 0,573, 0,713 ; plancher de la passe 2 à 1,62 ; marge 112 048 ; tailles 10 786 et 8 644.

## Conditions (vérifiables par programme)

- **C1** — Avant de lancer : `cd scripts && sha256sum -c lancer_course_ideation_regard_ou_raisons_v1.py.sha256` rend « OK »
  et l'empreinte est `3b2dcb117cd4a3074099000374f8b0608ad301d9306da07d25cb360bcce1302f`.
- **C2** — Avant la première course : `test ! -e runs/course-ideation-regard-ou-raisons-v1`,
  `test ! -e /home/user/sorties-course-ideation-regard-ou-raisons-v1` et `grep -c GO-2026-11-14-01 registres/depenses.md`
  rend 0. Si l'un des trois échoue alors qu'aucun run n'est au dépôt : nœud, aucun lancement.
- **C3** — Dès le code 0 « lancée, détachée », puis dès la clôture : commit et poussée du dossier de run ;
  `git status --porcelain runs/course-ideation-regard-ou-raisons-v1` vide et `git rev-list --count origin/main..HEAD` à 0.
  Aucune relance tant que ces deux commandes ne le rendent pas. Dépense consignée dans `registres/depenses.md`.
- **C4** — Code de sortie du lancement lu (`echo $?`) : 5 ou une trace → clôture dans le même conteneur, sinon nœud,
  aucune relance.
- **C5** — Lancement au premier plan ; après le lancement, le champ `SigIgn` de `/proc/<PID du superviseur>/status` n'a
  pas le bit de SIGINT (valeur 2). Arrêt : `kill -INT <PID>` d'abord, `kill -TERM` seulement s'il ne finit pas. Relais
  réglés comme au § 8 du rapport du préparateur (plafond 10 USD, huit appels), lus dans leur ligne de commande par PID,
  jamais dans leur environnement ; non relancés entre une course et sa relance.
- **C6** — Le bilan de l'organisme est `copies/sortie--fiches-validees.json`, vérifié par `sha256sum -c`, que
  l'orchestrateur ait rendu 0 ou 4. Les copies des notes du juge, de la lecture de la course et du manifeste de fin de
  l'orchestrateur restent fermées au lecteur du croisement.

## Mutants et épreuves (`contre-lecture-outils/`, scellés)

Banc `mutants_contre_lecteur_regard_ou_raisons_v1.py` (`43bdeb4d…`), joué de 09:53 à 09:58 UTC dans un dossier
temporaire hors du dépôt ; base : 151 passés ; résultat `resultat-mutants-contre-lecteur-regard-ou-raisons-v1.json`
(`845f14db…`).

| Famille | Tués | Survivants |
|---|---|---|
| Dépense (9) | coût externe oublié au manifeste de fin (C01) et au contrôle (C02) ; manifeste de fin illisible compté 0 (C03) ; coût négatif (C06) ; total externe relevé (C12) | tentative illisible ignorée (C04) ; fichier inattendu ignoré (C05) ; tolérance du cumul à 0,05 USD (C07) ; refus de taille au sceau faux ignoré (C10) |
| Ligne de GO (5) | type (G03) ; deux lignes au même identifiant (G04) ; ligne citante mal formée (G05) ; GO échu (G06) | plafond à suffixe (G07) |
| Relance (4) | trois courses (R02) ; fiches refusées non comptées (R03) ; superviseur sans PID tenu pour rien (R08) | course sans manifeste de départ non comptée (R01) |
| Environnement, bac, soi (8) | mandataire permis (E01) ; préfixe d'essai libre (E02) ; environnement entier au superviseur (E04) et aux sous-processus (E05) ; `/proc` neuf (B01) ; noms exclus écrits (K01) ; drapeau abrégé (D01) ; lanceur hors de sa place (S01) | aucun |

Lecture des survivants. C04, C05, C10 : dossier de contrôle sans sortie ; la dépense réelle y est au plus celle des
contrôles (2,1), donc la borne de 17 tient même sous ces mutants. C07 : enjeu de 0,05 USD. G07 : le code réel refuse
(épreuve 15). R01 : le seul qui touche une règle (m1).

Épreuves `epreuves_ligne_de_go_v1.py` (`87f24385…`), 09:54 UTC, résultat `resultat-epreuves-ligne-de-go-v1.json`
(`a9fa87b4…`) : vingt cas de registre, six cas de garde de cumul.

## Non vérifié

Tout ce que la contre-lecture précédente a lu dans l'orchestrateur et que je n'ai pas relu (même arbre) : une tentative de
contrôle par invocation, coûts de contrôle compris dans le journal, juge externe jamais joué, réaction à SIGINT ; la borne
en dollars d'un appel d'Argon au-delà de la garde avant envoi ; l'état et les réglages des relais ; la dépense de la course
précédente (lue dans `registres/depenses.md` seulement) ; l'accord des faits avec leur source, qui n'est pas au dépôt ; les
références citées. Le différentiel des essais n'est lu que pour ses essais retirés (un, remplacé) et ajoutés (quinze).
