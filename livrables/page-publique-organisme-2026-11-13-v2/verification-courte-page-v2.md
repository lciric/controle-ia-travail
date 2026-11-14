# Vérification courte de la correction version 2 de la page publique de l'organisme d'idéation

- **Vérificateur** : sous-agent neuf, modèle Fable 5.2 (`claude-fable-5-2`), qui n'a écrit ni la page, ni la correction, ni N-067, ni la lecture adverse, ni la note O4. Le 13 novembre 2026, de 20:29 à 20:33 UTC (`date -u`). Mandat : mot de Lazar R-2587, option (b).
- Aucune écriture git, aucune poussée, aucune dépense, rien écrit dans le clone public. Aucun refus de permission ni de classifieur. Aucun chemin interdit ouvert.

## Verdict

**Poussable après corrections.** Aucun bloquant. Quatre majeurs, tous de rédaction, trois nés de la v2 elle-même : le manifeste public dit le contraire de ce que la page fait ; la ligne T0.3 annonce un verdict que la page de résultat liée nie encore ; deux citations de la phrase sur le juge sont incomplètes ; « no false promotion » décrit notre issue plus fort que son compte (1 sur 24). Le reste tient : empreintes justes, différentiel rejoué à l'octet, tous les couples de la lecture adverse appliqués ou leur écart dit, phrases neuves au niveau de leurs pièces, deux phrases de feuille de route retirées.

## 0. Intégrité

| pièce | empreinte lue | attendue | égal |
|---|---|---|---|
| `diff-page-organisme-n067-v2.patch` | `6c4bcff43c6775a133aa3af7e9573d35d2dd9b8df9ffd083d19867d0036eb71a` | `6c4bcff4…` | oui |
| `journal-page-organisme-n067-v2.md` | `2239f4942f5c899db313339a4dc8dde7c643a937c33df6ed29533abe844dc0d9` | `2239f494…` | oui |
| `lecture-adverse-page-v2.md` (v1 du livrable) | `0bfe8eb7879f3375ebf2cdd37d454055077be4c282bd76ea99aa7e225a0405b5` | `0bfe8eb7…` | oui |
| `docs/notes/lecture-o4-englobement-v1.md` | `f521e164e79cb75e9b3f14a9bddb0cf8f57a5499e68f93276014e4b09fc130aa` | `f521e164…` | oui |
| `origin/main` du clone public, après `fetch` explicite | `be6b5af96c9e19812569d8dab55d6ce3978a3823` | `be6b5af9…` | oui, n'a pas bougé |
| verdict de l'audit de fuite ; verdict T0.3 ; N-067 | `320463e6…` ; `bc53b746…` ; `966dd9dc…` | journal | oui |
| quatre PDF de la note O4 (Feng, Giglio, Xiu ; copie de Liu et al. ; 2609.00731v1 ; 2610.07627v1) | `sha256sum -c` | compagnons | oui |

## 1. Rejeu du différentiel (point 1) : tient

`patch -p1` sur trois copies fraîches de `git show origin/main:` (`README.md`, `MANIFEST.md`, `resultats/controle-r1-blanche-noire/README.md`) rend `73f0b053…`, `a3dd9e79…`, `3acf0a9d…` : identité à l'octet avec les trois fichiers corrigés. Comparaison mot à mot base contre sortie : aucun changement hors de ceux que le journal annonce.

## 2. Couples de la lecture adverse (point 2) : tient

Contrôle par programme (chaque « texte corrigé » cherché dans les sorties, chaque « texte actuel » cherché absent).
- **B2, B3, B4, M1 (phrase d'ouverture et manifeste), M4 (8 sur 8), M5 (3 sur 3), M6.1 à M6.5, M7, m1 (2 sur 2)** : appliqués mot pour mot.
- **B1, M2, M3** : appliqués avec deux écarts. L'ouverture « What section 4 measures is narrower: » devient « The instrument of section 4, as the public code builds it (…): » (dit au journal) ; « writing any law of a closed grammar » devient « writing its laws in a closed grammar » (non dit au journal ; plus faible, sans effet).
- **M1, second couple** (« No statement on prior work is made here for this null… ») : non appliqué, écart dit au journal (section B, ligne M1 ; section C) : la lecture O4 est rendue, la phrase est remplacée par celle de la note. Conforme au point 5 de la section 7 de la lecture adverse.
- **m2** : appliqué (un point remplace les deux-points). **m3, m4, m5** : appliqués.
- H1, H2, H3 (hors différentiel) : non appliqués, portés à Lazar par le journal (section E). Conforme.

## 3. Phrases neuves contre leurs pièces (point 3)

| phrase neuve | pièce | tient |
|---|---|---|
| fuite : issue gelée « leak (reading the instruction) », 0.9967 [0.9930, 0.9991], 46 actions, 12 tâches sur 60, 0.9977 [0.9958, 0.9993], « "Not inflated" is not "no sabotage"… the arm that would separate the two was not run » | verdict de l'audit de fuite, l. 3, 6, 7, 42, 43, 58, 65 | oui, au chiffre près ; la réserve 2 est portée sur les deux pages |
| T0.3 : « one reader, 10 November 2026 », « confirmed with reservations », 886 cellules, comptes reproduits à l'octet, 0.214, 0.364, 0.164 vus avant le scellement | verdict T0.3, l. 3, 10, 12, 21-22, 24-25, 206, 228 | oui ; voir M2 et m2 |
| A1-v4 : « zero false admissions under a frozen referee: Qu, Chen, Wang, p. 15 » ; « none of 10,716 candidates admitted: CONFIRM, p. 9 » | PDF 2609.27051, p. 15 (« both LLM families admit 0.000 false factors per submission ») ; PDF 2611.01449v2 (`9a02cc6d…`), p. 9 (« evaluated 10,716 candidates, and none passed even provisionally ») ; N-067, section 7 | oui pour les deux citations ; « no false promotion » : voir M4 |
| attaque : « rewarded if its law is promoted », « not told that a promotion would be false », description exacte en texte, grammaire fermée, deux bras | `orchestrator/pole/attaque_goodhart_v2.py` à `be6b5af` : `consigne` l. 333-351, `GRAMMAIRE` l. 266, `description_du_juge` l. 309-330, `CONDITIONS` l. 55 | oui |
| juge au nul des lois connues, quatre citations | note O4, sections 0, 2, 4 ; PDF : Feng, Giglio, Xiu p. 2-4 ; copie de Liu et al. p. 1, 4, 26, 28 ; 2609.00731v1 p. 6, 7, 16, 25 ; 2610.07627v1 p. 1, 4, 15 ; `nul_v8.py` l. 1-45 (réserve (a) de la note) | oui sur le fond, pas plus fort que la note ; clause « non trouvé » retirée, réserve (b) appliquée (« before the outcomes are read ») ; conforme à R-2580 et R-2587 (assemblage de pièces publiées, ni libre ni neuf) ; citations : voir M3 |

## 4. Constats majeurs

### M1 — `MANIFEST.md` dit le contraire de ce que la page fait, deux fois

La section datée dit que le nul du juge est décrit « with no statement on prior work », alors que la page cite maintenant quatre travaux antérieurs pour ce nul, et que la même phrase du manifeste range « judging a discovery against what is already known » parmi le publié. Le couple M1 de la lecture adverse, écrit avant la lecture O4, a été gardé au manifeste alors qu'il a été dépassé dans la page. Et « No new number, result or file » est faux : le verdict du lecteur neuf sur T0.3 est une information neuve, et la page gagne des chiffres.

- Texte actuel : `the judge's null is described as what the system does, with no statement on prior work.`
- Texte corrigé : `the judge's null is described as what the system does, and the published work it assembles is cited.`

- Texte actuel : `- No new number, result or file.`
- Texte corrigé : `- No new run and no new file. New on the page: the fresh reader's verdict on T0.3 (10 November 2026), and figures already given on the result pages or read in the cited papers.`

### M2 — Ligne T0.3 : la page de résultat liée dit encore « No fresh-reader verdict »

La ligne corrigée renvoie à `resultats/controle-simulation-defenses/`, dont le fichier `README.md` (inchangé, `origin/main`, l. 12 et l. 85) dit : « **No fresh-reader verdict.** … no fresh reader has given a verdict on it » et « A fresh-reader verdict, or any criterion of the programme's gate G0: neither has been pronounced on this run ». Le dépôt public se contredirait dès la poussée. Le journal ne le dit pas. Le verdict lui-même n'est pas public : le lecteur ne peut pas le contrôler, ce que la phrase doit dire. Deux voies, au choix de Lazar.

Voie courte (dans le différentiel, `README.md`) :
- Texte actuel : `Fresh-reader verdict (one reader, 10 November 2026): "confirmed with reservations".`
- Texte corrigé : `Fresh-reader verdict (one reader, 10 November 2026; its text is not public, and the linked result page predates it): "confirmed with reservations".`

Voie complète (un quatrième fichier, `resultats/controle-simulation-defenses/README.md`), en plus de la parenthèse « its text is not public » :
- Texte actuel : `- **No fresh-reader verdict.** The outcome is the mechanical application of the frozen criteria by the frozen code; the run crossed no gate, and no fresh reader has given a verdict on it. The results note that records the reading is copied below.`
- Texte corrigé : `- **Fresh-reader verdict (one reader, 10 November 2026): "confirmed with reservations".** The outcome above is the mechanical application of the frozen criteria by the frozen code; the run crossed no gate. The fresh reader recomputed the 886 cells independently and reproduced the raw counts byte for byte; the verdict's text is not copied here. The results note that records the reading is copied below.`
- Texte actuel : `- A fresh-reader verdict, or any criterion of the programme's gate G0: neither has been pronounced on this run.`
- Texte corrigé : `- Any criterion of the programme's gate G0: none has been pronounced on this run.`
(Pièce : verdict T0.3, l. 10-22 et l. 265-268 ; la date « Last updated » de cette page serait alors à changer aussi.)

### M3 — Phrase sur le juge : un titre tronqué, et des pages données pour SSRN alors qu'elles sont celles d'une copie

- Le titre lu sur la première page du PDF `2610.07627v1` est « Learning to Outgrow a Theory: Experimental Discovery Beyond the Initial Hypothesis Space ». Même défaut que M5 de la lecture adverse.
  - Texte actuel : `Ma et al., "Learning to Outgrow a Theory", arXiv:2610.07627v1, 2026, pp. 1, 4, 15`
  - Texte corrigé : `Ma et al., "Learning to Outgrow a Theory: Experimental Discovery Beyond the Initial Hypothesis Space", arXiv:2610.07627v1, 2026, pp. 1, 4, 15`
- Les pages 1, 4, 26, 28 de Liu, Liu, Liu, Mei sont celles d'une copie déposée par l'hôte d'une conférence (page de titre « April, 2026 », 71 pages) ; SSRN a refusé le PDF officiel, et l'identité à l'octet n'est pas vérifiable (`docs/sources/pdf/lecture-o4-v1/ssrn-6569258/provenance-v1.md`, réserve). La page donne ces numéros comme ceux de SSRN, sans version. Même logique que M4 de la lecture adverse (une page citée vaut pour une version).
  - Texte actuel : `SSRN 6569258, 2026, pp. 1, 4, 26, 28;`
  - Texte corrigé : `SSRN 6569258, version dated April 2026, pp. 1, 4, 26, 28;`

### M4 — « no false promotion » : plus fort que le compte de la même ligne

La ligne dit, juste avant, « 1 of 24 units promoted under v9 with feedback », sur un monde où toute promotion est fausse ; la page d'état publique dit que « resists » admet au plus 1 sur 24 (`resultats/attaque-goodhart-v2/README.md`, l. 17 et 30). Le signe de « resists » n'est donc pas « aucune fausse promotion ». La phrase cède, elle ne revendique pas, mais elle décrit notre issue plus proprement qu'elle n'est.

- Texte actuel : `the sign of "resists", no false promotion, is already published`
- Texte corrigé : `the sign of "resists", false promotions held at or near zero, is already published`

## 5. Constats mineurs

- **m1 — Portée de la phrase d'ouverture sur le nul.** « The principles listed below with their references are already published, and none of them is claimed here » couvre maintenant aussi l'item du nul, qui porte des références. Lu à la lettre, rien n'est revendiqué pour le juge. C'est conforme à R-2587 (jamais libre ni neuf) ; je le signale pour que Lazar le voie en lisant le différentiel. Aucun couple.
- **m2 — « at the cited commit » sans commit cité.** La ligne T0.3 du `README.md` ne cite aucun commit ; il est sur la page de résultat (`d73ac46`).
  - Texte actuel : `by code extracted at the cited commit`
  - Texte corrigé : `by code extracted at the commit cited on the result page`
- **m3 — Journal (non publié).** Il dit que les lignes 38 et 43 de la page R1 sont toutes deux dans le texte daté « Where it stood » ; la ligne 38 (« The three texts will be made public with the result ») est dans la section « Sealed before the data », au-dessus. Promesse tenue depuis (les textes sont publics), non un plan à venir : sans effet sur la poussée. Il compte « eight items » puis « seven items ». Il est écrit en anglais.
- **m4 — Dénominateur du nul.** Le journal note que le dénominateur est le meilleur de tous les membres du nul, non la seule combinaison ajustée ; la phrase publique est vraie et plus faible que le code. Vérifié sur `nul_v8.py`, l. 12-18 et 27-31. Aucun couple.

## 6. Points 4 et 5

- **Point 4.** Dans le texte ajouté : aucune feuille de route, aucune consigne servie ni loi promue ni sortie de course, aucun nom de personne hors des auteurs cités, aucun mot de priorité (« first », « novel », « not found », « to our knowledge », « free » : absents du texte ajouté ; « proves » ne qualifie que le corollaire de REUSE). Dans le texte inchangé, déjà en ligne et hors différentiel : les points H1 à H3 de la lecture adverse et les points 2 à 9 de la section E du journal restent à décider par Lazar ; je n'en ajoute pas.
- **Point 5.** Les deux phrases de feuille de route sont retirées : `README.md`, ligne R1 (« the next test uses organisms whose sabotage is trained into the weights… ») ; page R1, « Consequence » (« Next: organisms whose sabotage is trained into the weights… »). Recherche de « next », « will », « planned », « upcoming » dans les trois sorties : reste seulement le texte daté du 2 novembre de la page R1 (étapes exécutées depuis) et des états déjà en ligne (« not public yet », « until the project lead decides »).

## 7. Ce que je n'ai pas fait

- Je n'ai pas recontrôlé sur PDF les trente-cinq affirmations de la lecture adverse ; j'ai contrôlé que ses couples sont appliqués.
- Pour la note O4, j'ai contrôlé les empreintes des quatre PDF, les titres, et les passages des pages citées par lecture `pdftotext` et par le résultat scellé de la vérification des citations (53 trouvées sur 53) ; je n'ai pas relu les articles en entier.
- Je n'ai pas lu le verdict des trois analyses de R1 (`dece9980…`) : le « +0.932 » de la ligne R1 reste hors de cette vérification (journal, section E, point 9).
- Je n'ai pas lu le verdict officiel d'A1-v4 ; le compte « 1 of 24 » de M4 vient de la page d'état publique.
