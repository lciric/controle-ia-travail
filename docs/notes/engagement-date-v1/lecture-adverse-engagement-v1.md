# Lecture adverse du texte d'engagement daté sous embargo — v1

- **Lecteur** : lecteur adverse neuf, modèle B (autre que le rédacteur du texte), sans part à l'écriture du texte, des notes ni des décisions lues.
- **Écrit** le 14 novembre 2026 (UTC). Rien n'est soumis, rien n'est commité, personne n'est contacté, aucun compte n'est touché.
- **Objets lus** : `texte-engagement-date-v1.md` (`630cf444b10f12b05e5a5f22b85ce1471441805bb58466a12bcfb97a2b4d7940`, empreinte recalculée conforme) ; `notes-pour-lazar-v1.md` (`edea9cda0bc00116172fb12fa8bfb95cbfb0f8a686cafa1ebdc37ef7e60a8b11`, conforme) ; les quatre pages archivées sous `sources-osf-20261114/` (empreintes recalculées conformes à leurs compagnons : `5e1ba9b5…`, `98fcf79f…`, `09ad29e8…`, `cff1f9f2…`).
- **Sources lues** : `registres/decisions.md`, lignes R-2554, R-2555, R-2563, R-2567, R-2571, R-2575, R-2580, R-2581, R-2587 ; `docs/decisions/` N-005/N-006, N-007/N-008, N-013, N-055, N-064, N-067 (sections 4, 6, 10), N-068, N-069, N-070 (sections 0 à 4) ; contre-lecture de la synthèse finale (`f1580ddc…` : verdict, B3, M1, M2, M7, mineurs, sections 5 à 7) ; synthèse finale de niveau 3 (sections H1, H2, papier B, H3, H5, H7, HC1, HC2) ; programme v2, l. 93, 111, 113, 114.
- **Non ouvert** : `diag/`, `runs/` de 7a et 7b, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `prereg/T0.7-sondes-v0-v1.md`, le paquet de P3-bis.
- **Limites** : aucun PDF d'article rouvert ; aucun identifiant contrôlé sur arXiv ou SSRN (contrôle interne au dépôt seulement, section 4) ; les règles de l'Open Science Framework sont lues sur les quatre pages archivées, jamais sur l'interface.

## 0. Verdict

**Figeable après corrections.** Le texte ne porte aucun résultat, aucun chiffre de résultat, aucune pièce sous embargo, et aucune des revendications cédées (H9, O4, O2, HC4 absentes). Quatre points bloquent le gel de la version 1 telle quelle ; ils imposent une version 2 (nouveau nom, nouvelle empreinte), jamais une réécriture.

**Bloquants.**
- B1 — S9 enregistre la comparaison « sonde contre juges sous les mêmes attaques » : c'est l'opposition juge contre sonde que R-2567 interdit de déclarer tant que 2607.00415 n'est pas lue ; S8 dit qu'elle n'est pas enregistrée, S9 l'enregistre. Nœud de Lazar.
- B2 — S8, prédiction « g is stable for a given monitor » : autre et plus forte que la prédiction 3 de N-005 (stabilité de rang entre moniteurs, magnitudes non revendiquées stables), et un contre-indice publié la vise (R-2554).
- B3 — Section 2, « each claim of prior work checked on the PDF, page cited » : faux pour plusieurs pièces citées par le texte lui-même (billets, relevé par mots, sources « not yet read »).
- B4 — Deux champs vides (« [DATE TO BE CHOSEN] », « [TO BE CHOSEN] ») et deux phrases sur l'embargo inexactes d'après les pages archivées (la fin d'embargo est automatique à la date choisie).

**Majeurs** : M1 à M8 (section 2). **Mineurs** : m1 à m7 (section 3). **Règles de l'Open Science Framework** : section 5 ; trois des six points « à vérifier » des notes ont leur réponse dans les pages archivées.

---

## 1. Constats bloquants

### B1 — S9 : la comparaison aux juges est l'opposition que R-2567 retient

- R-2567, section 6 : « HC1, opposition juge contre sonde — 2607.00415 versée, non lue (M7) — ce qui lèverait la réserve : la lire ». La table d'exposition (section 5) dit « forte pour l'opposition juge contre sonde ».
- N-068, section 4, écrite après, range « la comparaison aux juges génératifs sous les mêmes attaques » parmi « ce qui est propre » ; sa section 8 met HC2 dans l'enregistrement. N-067 à N-070 n'ont pas levé la réserve de R-2567 ; `registres/decisions.md` ne porte aucune lecture de 2607.00415 depuis (seules occurrences : R-306, non opposable, et R-2567).
- Le texte cumule les deux : S8 écrit « No comparison between judges and probes is registered under this statement » et S9 l'enregistre deux lignes plus bas, avec la ligne de statut « not found in the sources we read » — mention que R-2567 n'a accordée ni à HC2 ni à cette pièce (HC2 est absente de ses deux listes).
- Les notes le posent (3.1) sans le trancher. Ma lecture : tant que 2607.00415 n'est pas lue, la clause ne se fige pas sous une mention « not found ».

Option (c) des notes, la plus sûre : lire 2607.00415 avant de figer. Sinon, couple de l'option (b) :

Avant (S9) :
```text
measured in a paired design (same task with and without adversarial content; rhetoric crossed with intention), compared with the g of
generative judges under the same attacks, for several aggregations including a robust one, on trajectories.
```
Après :
```text
measured in a paired design (same task with and without adversarial content; rhetoric crossed with intention), for several
aggregations including a robust one, on trajectories. The g of generative judges under the same attacks is measured alongside as a
reference; no claim on the judge-versus-probe comparison is registered here (arXiv 2607.00415, deposited, not yet read, may bear on it).
```
Si Lazar garde la clause (option (a)), la ligne de statut de S9 doit le dire :

Avant :
```text
- Status, 13 November 2026: not found in the sources we read; works citing […]
```
Après :
```text
- Status, 13 November 2026: not found in the sources we read, except that the judge-versus-probe comparison is not settled (arXiv
  2607.00415 not yet read); no dedicated inventory of unread sources was made for this statement; works citing […]
```

### B2 — S8 : prédiction de stabilité autre que la source

- N-005, section 1, prédiction 3 : « stabilité de **rang** de g entre moniteurs, invariance à l'attaquant et au corpus. Les magnitudes ne sont pas revendiquées stables ».
- R-2554 et la synthèse (HC1, contre-indices) : la prédiction 3 a des contre-indices publiés (2608.12645 ; 2611.04556, p. 58-59).
- R-2567 ne rend déclarable que « la pièce » (destination libre testée, par famille, par régression), pas les prédictions.

Avant :
```text
Prediction: ĉ is the attacker's target, and g is stable for a given monitor.
```
Après (lettre de N-005) :
```text
Prediction: ĉ is the attacker's target rather than the corpus mean; the rank order of g across monitors is stable (magnitudes are
not predicted to be stable). Published counter-indications to both predictions exist (arXiv 2606.05384; 2608.12645; 2611.04556).
```
Ou, plus court : ne garder que « Prediction: ĉ is the attacker's target rather than the corpus mean », avec la même phrase de contre-indices.

### B3 — Section 2 : « each claim of prior work checked on the PDF »

Contredit par le texte et ses sources : deux billets (institut britannique, 10 juillet 2025 ; Hopman, Lemoine et Tracy, 27 mai 2025) sont des textes archivés, pas des PDF ; l'annonce de 2604.01151 version 2 est un « relevé par mots […] non lu en entier » (contre-lecture, m6) ; chaque énoncé porte une ligne « Not yet read » ; la contre-lecture rend « utilisable après corrections, pour une partie seulement » ; les notes (section 5) disent que les numéros n'ont pas été relus sur PDF par le rédacteur.

Avant :
```text
The statements below are those retained by the program director's internal decisions as of 13 November 2026, after a three-level
verification of prior work on primary sources (each claim of prior work checked on the PDF, page cited).
```
Après :
```text
The statements below are those retained by the program's internal decisions and verification reports as of 13 November 2026, after
three rounds of reading of prior work. What is said of prior work below relies on readers' reports on archived copies (PDFs; archived
text for blog posts). Sources deposited but not read are named under each statement.
```
(« the program director's internal decisions » est aussi trop fort : les qualificatifs du 13 novembre de S1, S5, S7 et le retrait de l'opposition dans S8 viennent de la contre-lecture R-2567, pas d'un mot de Lazar — les notes le disent pour HC1. Le montrer à Lazar avant le gel en fait sa décision ; d'ici là, la phrase « après » est la seule exacte.)

### B4 — Champs vides et phrases d'embargo

- « [DATE TO BE CHOSEN] » et « [TO BE CHOSEN] » : la version 1 ne peut pas être jointe « telle quelle » (notes, 3.8) ; les remplir change l'empreinte. Version 2 obligatoire.
- D'après les pages archivées, l'embargo **finit de lui-même** à la date choisie (section 5, point 2). Le texte doit être écrit comme un texte qui sera public, au plus tard quatre ans après la soumission, sans geste de personne.

Avant (en-tête) :
```text
It is visible only to its contributors until the end of the embargo, and will be made public later, at a date chosen by the authors
(scheduled end: [DATE TO BE CHOSEN]).
```
Après :
```text
It is not publicly accessible during the embargo. It becomes public automatically at the scheduled end of the embargo
(AAAA-MM-JJ), or earlier if the authors end the embargo.
```
Avant (section 6) :
```text
This registration is under embargo and will be opened later by the authors. Its content will not be changed; any later change of
wording will be registered separately and will cite this registration.
```
Après :
```text
This registration is under embargo until the scheduled end date above. The attached file will not be changed; any later change of
wording will be recorded as a dated update or as a separate registration that cites this one.
```
(La page du guide prévoit des « updates » avec justification et historique ; les fichiers joints, eux, ne changent jamais.)

---

## 2. Constats majeurs

### M1 — S8, « Not claimed » : pièces que N-005 dit « citées comme publiées » absentes

N-005, section 1 : la **forme algébrique** est le « poids du conseil » de la psychologie du jugement ; le **coefficient continu de déférence par modèle sur intensités graduées** est publié (2606.07897 version 2) ; la hausse continue par technique de persuasion aussi (2508.07805). Le texte ne cède que « the law with an imposed destination (Panin ; 2603.15809) ».

Avant :
```text
- Not claimed: the law with an imposed destination (Panin, SSRN 7424179; arXiv 2603.15809); the displacement […]
```
Après :
```text
- Not claimed: the algebraic form (the "weight of advice" of the judgment literature); the law with an imposed destination (Panin,
  SSRN 7424179; arXiv 2603.15809); a continuous per-model deference coefficient over graded intensities, outside control monitors
  (arXiv 2606.07897 version 2; 2508.07805); the displacement […]
```
« Not yet read » de S8 : la table de la contre-lecture (section 5, ligne HC1) porte aussi le lot 11.

Avant : `- Not yet read: arXiv 2602.21262, 2607.00415, 2305.11888, 2610.35930.`
Après : `- Not yet read: arXiv 2602.21262, 2607.00415, 2305.11888, 2610.35930, 2507.03120, 2502.08177; Kumaran et al. 2026; Rebholz et al. 2023.`

### M2 — S6 (H5), « Not claimed » : une pièce de la synthèse manque

Synthèse, H5 : « Une sonde contre dix sous pression d'optimisation (2510.21531, p. 1, 7, 9) », avec le contre-indice « gain de la diversité minimal ». C'est la pièce la plus proche de la loi sur des sondes sous attaque.

Avant : `[…] the corresponding result on ensembles of generative judges (2608.16190).`
Après : `[…] the corresponding result on ensembles of generative judges (2608.16190); one probe against ten under optimisation pressure (2510.21531).`

### M3 — S4 : contrôles empruntés non attribués ; liste « Not yet read » recopiée de S3

- N-069, section 4, point 1 (d) : « avec les contrôles de construit **de 2611.10620** ». Le texte les liste dans l'énoncé sans les attribuer.
- N-069, section 9, nomme des pistes citées et non lues propres à cette pièce ; S4 est absente de la table d'exposition de R-2567.

Avant :
```text
with construct controls (instruction received and refused, instruction removed, score read before the outcome).
```
Après :
```text
with the construct controls of arXiv 2611.10620 (instruction received and refused, instruction removed, score read before the outcome).
```
Avant : `- Not yet read: versions 1, 2 and 4 of arXiv 2604.01151; 2604.19784; 2610.37849.`
Après : `- Not yet read: versions 1, 2 and 4 of arXiv 2604.01151; 2604.19784; 2610.37849; 2607.06807. Leads cited by others and not obtained: 2510.04303; 2609.00180. No dedicated inventory of unread sources was made for this statement.`

(Contrôle par nom de fichier : 2607.06807 est versé ; 2510.04303 et 2609.00180 ne le sont pas ; les autres identifiants que je propose d'ajouter — 2606.07897, 2508.07805, 2510.21531, 2605.12947, 2410.22318, 2507.03120, 2502.08177, 2609.05797, 2602.08877, 2608.12645 — ont chacun un PDF au dépôt.)

Ajouter aussi à « Not claimed » de S4 et de S3 : `cross-sectional detection on activations (arXiv 2604.01151 version 5)` — S3 cède la coupe transversale sans la référence, S4 ne la cède pas.

### M4 — S2 : la version 2 de 2604.01151 est à la fois citée et « non lue »

Avant :
```text
sequential detection announced as future work by the authors of arXiv 2604.01151 (version 2, 9 May 2026);
```
Après :
```text
sequential detection announced as future work by the authors of arXiv 2604.01151 (from version 2, 9 May 2026; located by word
search, that version not read in full);
```
Et à « Not claimed » de S2, la configuration de référence publiée (synthèse, H2) : `the per-action threshold on the acting agent's probes with a maximum over the trajectory (LessWrong post of 30 October 2026)` ; à « Not yet read » : `2605.12947, 2410.22318` (table de la contre-lecture, ligne H2).

### M5 — S9 : MIRAGE « cited as published » sans « non opposable » ; contre-indices tronqués

N-068, section 6 : MIRAGE est cité « comme publié **et non opposable** » ; les contre-indices « à dire avec la prédiction » sont au nombre de huit lignes, le texte en nomme deux.

Avant : `(MIRAGE, arXiv 2606.10304, cited as published)`
Après : `(MIRAGE, arXiv 2606.10304 version 1, cited as published; we do not rely on its figures)`

Avant : `Published counter-indications to the prediction exist (2608.21664; 2602.00750).`
Après : `Published counter-indications to the prediction exist (2608.21664; 2602.00750; 2609.05797; 2611.10620; 2602.08877; 2610.18408).`

Avant : `g of a robustly aggregated probe is about zero, and at most null`
Après : `g of a robustly aggregated probe is about zero, and not positive` (« au plus nul » de N-068).

### M6 — Section 1 : le but déclaré sort du cadre accepté par le registre et livre un motif

Guide archivé, « Submissions to OSF Registry » : sont acceptés des « Plans for research that is underway, with explanation of the current state of the study » ; refusés, les « commentaries, proofs, or other theoretical pieces ». La phrase « fixes […] the date of the program's ideas before any substantive exchange with outside researchers » présente le dépôt comme une prise de date, et sera publique.

Avant :
```text
This document fixes, with a registry timestamp, the date of the program's ideas before any substantive exchange with outside
researchers.
```
Après :
```text
This document registers, with a registry timestamp, the hypotheses and planned measurements of a research program that is underway.
```

### M7 — Notes, 3.7 : « from scratch » doit devenir un interdit, pas une recommandation

Le guide : « If registering from a project, be aware any files associated with the Project […] will be attached to your registration up to 5 GB ». Le registre (R-2384, R-2397) dit que les manifestes déposés dans `dr57c` listent les chemins et empreintes du préenregistrement des sondes de T0.7 et du texte de P3-bis. Comme l'embargo finit seul et qu'une registration publique ne redevient jamais privée, enregistrer depuis `dr57c` rendrait ces chemins publics à l'échéance, sans retour.

Avant (notes, 3.7) : « Recommandation forte : créer la registration « from scratch », pas depuis `dr57c` »
Après : « Interdit : ne jamais créer la registration depuis `dr57c` ; « from scratch » seulement, un seul fichier joint (le texte), rien d'autre. »

### M8 — Lignes « Wording fixed internally » incomplètes

S5 : « total » et « la comparaison des deux courbes » datent de la synthèse et de R-2567 (13 novembre), pas du 4 octobre. S7 : « over several rounds » et « in the order given by this measure » datent de R-2567, constat m1. S6 : la cession de l'instrument sous attaque date de R-2567, constat B3.

Avant (S5) : `- Wording fixed internally: 4 October 2026.`
Après : `- Wording fixed internally: 4 October 2026; qualifiers made explicit on 13 November 2026.`
Même ajout à S6 et S7.

---

## 3. Constats mineurs

- **m1 — Section 3, définition de g.** « the displacement of a monitor's score » ; dans S8, g est un gain (fraction de l'écart à la destination). Après : `**g**: the displacement of a monitor's score under attack, as a continuous quantity; in S8, normalised by the distance to the destination (a gain).`
- **m2 — Section 5, « adopts and cites ».** Le texte ne cite aucune de ces pratiques. Après : `are published practices that the program adopts; it claims none of them.` (Évite aussi de « présenter » l'organisme sans les citations obligatoires de N-067, section 6.)
- **m3 — Versions.** Les énoncés dépendent des versions lues (R-2581 l'a relevé pour la page publique) : ajouter « version 1 » ou le numéro lu à 2610.12445 (versions 1 et 4), 2611.10620 (1), 2611.02153 (1), 2601.05427 (3), 2605.11135 (2), 2606.10304 (1), 2610.18408 (1), 2608.21664 (1), 2602.00750 (2).
- **m4 — S1, S3, S5, « Not yet read ».** La table de la contre-lecture nomme aussi SwarmReconGuard et ORBIT (sans identifiant). Ajouter : `and two deposited sources without an arXiv identifier`.
- **m5 — S2.** « the guarantee is uniform over the episode horizon and calibrated on whole honest episodes » : N-007 en fait une « lecture » portée au préenregistrement de G1, qui « ne change pas l'énoncé » ; la synthèse l'inclut dans la conjonction dite libre. Acceptable ; le signaler à Lazar.
- **m6 — S1.** « of the acting agent » n'est pas dans la lettre du programme (l. 93) ; restriction, donc sans risque.
- **m7 — Section 2, « Pilot and instrument-validation runs exist ».** Le registre nomme de telles courses ; je n'ai ouvert aucun dossier de course. À confirmer par Lazar, comme les notes le demandent.

---

## 4. Références et identifiants

- **Contrôle fait** : les 58 identifiants arXiv du texte et le numéro SSRN 7424179 figurent chacun dans la synthèse finale, la contre-lecture ou une décision, **et** un fichier PDF portant l'identifiant existe par son nom dans le dépôt (branche `main` ou branches `prep/etat-de-l-art-niveau3-*`). Aucun identifiant orphelin.
- **Contrôle non fait** : aucune vérification sur arXiv ni sur SSRN ; aucun PDF rouvert ; la correspondance identifiant-contenu repose sur les rapports des lecteurs. Les identifiants des lignes « Not yet read » ne sont connus que par leur titre.
- **Références non vérifiables par un tiers, à compléter** :
  - `UK AI Security Institute, blog post of 10 July 2025` : ajouter le titre et l'adresse.
  - `Hopman, Lemoine and Tracy, blog post of 27 May 2025` : ajouter le titre, le site et l'adresse.
  - `Venkatesh, Jiralerspong and Kondrup, "Where Empathy Goes Wrong", 2026` : ajouter le titre entier, « preprint of 2 October 2026, NeurIPS 2026 workshop » (N-023).
  - `the judgment literature` (si M1 est appliqué) : N-005 nomme Harvey et Fischer 1997, Yaniv et Kleinberger 2000, « PDF à lire (R7) » ; ne citer les noms qu'après lecture, sinon garder la formule générique.

---

## 5. Règles de l'Open Science Framework : la lecture des notes est-elle exacte ?

Exacte sur : embargo choisi à la soumission ; quatre ans au plus ; « page not found » pour les tiers ; lien en lecture seule ; approbation des administrateurs, automatique après 48 heures, date retenue = date de soumission ; levée anticipée ; DOI pour les seules registrations publiques ; fichiers figés, 5 Go ; retrait irréversible, embargo à lever d'abord ; jamais de retour au privé ; liste des soumissions acceptées et refusées ; gabarits ; transition.

Quatre écarts, tous dans la liste « à vérifier » ou ses conséquences :

1. **Fin d'embargo (point 1 des notes) : les pages archivées ne se contredisent pas ; la fin est automatique.**
   - Guide, « Privacy Settings » : « enter your registration into embargo, which will make it private until the end of the embargo date ».
   - Guide, « Embargo » : « Select a date that the embargo will end and the registration will be made public » ; « the registration embargo will end at midnight ».
   - Page 768 : « It will continue as usual, including any scheduled end to an embargo » ; « Embargoed registrations will remain embargoed until their scheduled end date ».
   - La phrase opposée (« The only way to make a registration public is to actively end the embargo ») répond à une autre question : « If I make my project public, will that make my registrations public, too? ». Elle dit que rendre le projet public n'ouvre pas la registration.
   - Conséquence : tout ce qui est figé sera public à l'échéance, quatre ans au plus, sans geste. Non observé sur l'interface.
2. **Création après le 16 novembre (point 3 des notes) : la réponse est dans la page 768.** « You can continue creating new registrations through the OSF Registration workflow after new projects can no longer be created. An OSF Project is not required to create a registration. » ; l'enregistrement depuis un projet existant reste ouvert jusqu'au 19 février 2027 (« registering using an existing project will be disabled on Feb 19, 2027 »). Reste une tension avec le guide (« a project will be made available for you ») : ce que devient ce projet lié après le 16 novembre n'est écrit nulle part. L'année du « November 16 » n'est pas écrite ; la page 770 est datée « Last updated on September 30, 2026 ». « After November 16 » : le 16 compris ou non, non écrit.
3. **Refus par un modérateur (point 6 des notes) : la réponse est dans le guide.** « OSF registrations are a non-moderated service. This means that you are in charge of accepting your submission » ; « Registrations that are not submitted to a Community-run Registry are reviewed and approved by the administrators on the registration ». Pas de modération à l'entrée du registre général ; la règle d'acceptation reste opposable après coup (d'où M6).
4. **Durée : trois formules pour le point de départ.** « from the first submission » (page 634), « from creation date » (guide, préparation), « from the date of submission » (guide, questions). Les notes en citent deux. Choisir une date de fin bien en deçà de quatre ans rend l'écart sans effet.

Restent vraiment non lus, comme les notes le disent : visibilité du titre, des contributeurs et de la description pendant l'embargo (point 2) ; conditions d'utilisation et licence (point 4) ; fuseau de la date (point 5 ; le guide ne dit que « from midnight »). Le gabarit « Open-Ended registration » est décrit par le guide comme « Only use if another template doesn't fit your study design or registering a completed project » : choix défendable, à dire à Lazar.

---

## 6. Réponses aux cinq questions du mandat

1. **Énoncé plus fort ou autre que sa source** : S8, prédiction de stabilité (B2) ; section 2, vérification « sur PDF » et « décisions du directeur » (B3) ; S4, contrôles non attribués (M3) ; S9, MIRAGE sans « non opposable » et « at most null » (M5) ; dates de lettre (M8). S1, S2, S3, S5, S6, S7 suivent leur source à quelques mots près (m5, m6).
2. **À ne pas figer** : aucun résultat, aucun chiffre de résultat (seuls nombres : dates, identifiants, versions, seuil de conception de 1 %) ; aucune pièce sous embargo, ni son existence ; pas de feuille de route au-delà des trois papiers et de la règle « un préenregistrement par test ». À retirer : le motif « before any substantive exchange with outside researchers » (M6). À ne jamais joindre : les notes, le projet `dr57c` (M7).
3. **Revendications cédées ou occupées** : H9, O4, O2, HC4 absentes ; l'organisme n'a qu'une ligne, sans revendication. **L'opposition juge contre sonde revient par S9 (B1).**
4. **Identifiants** : tous tracés dans le dépôt, aucun vérifié hors du dépôt ; trois références sans titre ni adresse (section 4).
5. **Règles de l'Open Science Framework** : lecture exacte sauf la « contradiction » sur la fin d'embargo, qui n'en est pas une (fin automatique), et deux questions données pour ouvertes dont la réponse est archivée (section 5).

Version 1 ; ne sera jamais réécrite (R12).
