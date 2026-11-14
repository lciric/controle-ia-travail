# Contre-lecture de la synthèse finale de niveau 3 de l'état de l'art — v1

Date : 2026-11-13, rédigée de 18:27 à 18:54 UTC (heures relevées par `date -u`). Contre-lecteur : sous-agent neuf
(Claude Opus 5.5), autre modèle que l'auteur de la synthèse (Claude Fable 5.2) ; je n'ai écrit ni le programme, ni les
décisions, ni aucun des vingt-sept rapports, ni la synthèse, ni son journal.

**Objet.**
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, sha256 `e30a013d08b03e8ddc07637b186e38e2051bd221958b713cc27facd1abf45892`
  (recalculé, conforme au compagnon) ; ci-dessous « la synthèse », lignes numérotées comme dans le fichier.
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-journal.md`, sha256 `b9511aeaa92662a1ba8ba038cf1f223d328c70cd238423835c631aa751486780`
  (recalculé, conforme).

**Usage visé** : un horodatage public des pièces libres des papiers A, B, C et de l'organisme (mot de Lazar, R-2555).
Une affirmation fausse de liberté y serait publiée ; je lis donc les zones dites libres en premier et plus durement
(R4, R8).

---

## 0. Verdict

**Utilisable après corrections**, et pour une partie seulement des énoncés. Trois conditions, toutes nécessaires :
1. corriger les trois constats bloquants (section 2) ;
2. ne déclarer publiquement libre aucun énoncé de la liste de la section 6 ;
3. assortir chaque énoncé déclaré libre de sa date et de deux mentions : « non trouvé dans les pièces lues », et « les
   travaux qui citent 2606.08892, 2512.07810 et 2606.10456 (lot 9) n'ont pas été recherchés ; rien n'a été cherché du
   10 au 13 novembre 2026 ».

Les pages et chiffres que j'ai contrôlés sur les fichiers des articles tiennent tous (section 1.3 : 34 contrôles, aucun
échec). Le défaut n'est pas dans les citations : il est dans **trois phrases plus fortes que leur pièce**, dans des
**formulations « libres » amputées d'un qualificatif** que les rapports donnent, et surtout dans une **section 9
incomplète** : des pièces versées au dépôt, que les lecteurs eux-mêmes désignent comme les voisins les plus probables
de L, T, H6, Tr, HC1, HC5, HC6, O4 et du rôle 1, n'y sont pas nommées.

**Bloquants, une ligne chacun.**
- B1 — H9 : « le profil de la perte par rang de relais » est donné pour non trouvé ; MasDrift publie la répartition du
  premier relais fautif par rang, pour trois profondeurs contrôlées (2608.07556, tableau 18, p. 23).
- B2 — Prononcé 1 et phrase d'ensemble : « aucun énoncé occupé en entier » et « contre chacun de nos énoncés » sont
  contredits par la synthèse elle-même (O20 « occupé comme méthode » ; O5, O6, O15 et rôle 3 non réexaminés) ; la
  phrase porte un nombre non vérifié.
- B3 — H5 : « l'instrument existe hors attaque » ; il existe aussi sous attaque, entre trois architectures de sondes
  (2609.36490, p. 8), pièce que la synthèse cite elle-même.

**Majeurs, une ligne chacun.**
- M1 — H1 : la phrase pour un jury omet « à fausses alarmes égales et à agrégation égale » et la comparaison publiée sur
  une sous-performance d'agent.
- M2 — Statistique de population : la pièce dite libre perd « sur scores de sondes de copies d'un même modèle » et
  élargit « adversaire entraîné » en « adversaire ».
- M3 — H8 : la phrase pour un jury est plus forte que la pièce (2610.17301 a préenregistré sur un second modèle un échec
  sous injection tiré du construit) ; le fait cité est en outre inexact sur la page 37.
- M4 — L et T : les sources que le rapport C2 désigne comme collision la plus probable sont versées au lot 8 et non
  lues (1906.08938, 2605.16140, math/0410072, Koning, Ramdas, Vovk) ; la synthèse n'en nomme qu'une partie.
- M5 — H6 : Ctrl-Z (2504.10374, au dépôt) publie une baisse du succès des attaques de 58 % à 7 % pour 5 % de
  performance perdue par rééchantillonnage ; jamais confronté à H6 ; « libre » ne tient pas en l'état.
- M6 — Tr : la pièce libre n'est pas énoncée ; Constitutional Classifiers++ (lot 11) et deux articles de sondes pendant
  la génération (lot 10), signalés par C5, ne sont pas nommés.
- M7 — HC1 : « l'opposition juge contre sonde » est dite libre alors que 2607.00415, désignée par C3 et S-7C pour
  cette pièce exacte, est versée au lot 10 et non lue.
- M8 — HC4 : « La comparaison de coût avec un juge n'est pas publiée » est absolu ; les pièces ne portent que « non
  trouvée dans nos lectures », la zone est peu cherchée, et un point de coût au même budget existe (2602.08877).
- M9 — HC5 : le quorum de juges et de sondes est dit libre ; un système publié combine sondes linéaires et
  classifieurs externes sous attaque (2601.04603, lot 11, non lu) ; pistes de S-7C omises.
- M10 — HC6 : 2608.11247 (« frontière résistance–réceptivité »), qui « touche HC5 et HC6 » selon C3, est versée et non
  lue ; non signalée sous HC6.
- M11 — O4 : la piste la plus dure (SSRN 6569258, hypothèses de modèle testées contre 209 anomalies publiées) et les
  pièces versées non lues (2609.00731, 2110.00115, 2103.08402) ne sont pas nommées.
- M12 — Rôle 1 : la pièce propre est dite libre alors que le lot 4-B, consacré à ces juges, n'a pas été rendu et que
  six pièces versées sur la tromperie de relecteurs modèles n'ont été lues par personne.
- M13 — Section 9 : description fausse du lot 11, pièces non lues des lots 3, 4, 8, 10, 11 et 2 non nommées ni
  rattachées aux énoncés.
- M14 — H4′, HC2b, HC4 : la synthèse les dit « peu cherchés » (l. 643) sans porter cette réserve dans leurs verdicts.

---

## 1. Méthode

### 1.1 Sources lues et empreintes
- Récupération : `git fetch origin refs/heads/<branche>:refs/remotes/origin/<branche>` pour les deux branches nommées
  (aucun autre appel réseau) ; têtes `f0aaf0d1b3f18764d4f728faf6ec5ce9b5cc6854` (`prep/etat-de-l-art-niveau3-v1`) et
  `10016a61c3e42ea3889cf0b0089c2cfbde50402f` (`prep/etat-de-l-art-niveau3-pieces-v1`), identiques à celles du journal.
- Les vingt-sept rapports, extraits par `git show` dans mon dossier temporaire : empreintes recalculées, conformes à leur
  compagnon `.sha256` et aux empreintes du journal (27 sur 27).
- Passation de la session à réseau (`registres/passations/2026-11-10-1115-pieces-reseau-niveau3.md`, branche des pièces,
  `75218434…`) : contenu prévu des lots 8 à 11.
- Sur `main` : `docs/decisions/decision-N-013-v1.md` (énoncés de H5, H6, H7, HC3), `decision-N-015-v1.md` (H6),
  `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` (H6, Ctrl-Z), les deux notes de veille sur 2611.04556.
- Lecture des rapports : en-têtes, tables de verdicts, sections « ce qui reste revendicable », pistes non lues ;
  passages précis cherchés par mots. **Pas en entier** : les fiches pièce par pièce et les annexes de citations.

### 1.2 Fichiers d'articles
- 190 fichiers extraits par `git show` : 189 de la branche des pièces (181 du dossier `docs/sources/pdf/niveau3-v1/`,
  8 de `docs/sources/pdf/`) et un de `main` (`docs/sources/pdf/veille-2611.04556-v1/2611.04556.pdf`) : empreintes
  recalculées, **toutes conformes** à leur compagnon.
- Titres des pièces des lots non lus : première page seulement (`pdftotext -l 1`). Pour une seule pièce,
  Constitutional Classifiers++ (2601.04603), j'ai lu aussi le résumé de la première page, à cause de sa portée sur HC5.
- Après extraction des titres, j'ai effacé la plupart des fichiers (le disque du conteneur était plein) ; les 26 fichiers
  utiles aux contrôles ont été gardés.

### 1.3 Contrôles sur les fichiers (34, aucun échec)
Script `cherche_page.py` (dossier temporaire privé, lancé par `python3 -I`) : texte de chaque page par `pdftotext`, avec
et sans `-layout`, normalisation (forme Unicode compatible, apostrophes, tirets, césures, blancs) ; une citation passe si
elle figure à la page attendue. Les lectures de tableaux sont faites en `-layout` et relues à l'œil. Un premier script,
écrit dans le dossier temporaire partagé, a été réécrit entre deux appels par un autre processus ; tous les contrôles
ci-dessous ont été refaits avec le script privé.

| n° | pièce, page | ce qui est contrôlé | pour | résultat |
|---|---|---|---|---|
| 1 | 2610.12445v4, p. 34 | « because its side task is a proportion of bookings over the episode, not a discrete action, so its steps cannot be labeled one at a time » | H1 | conforme |
| 2 | 2610.12445v4, p. 34 | « The other 11 private scenarios, left out by hand, have side-task steps that are difficult to label one step at a time. » | H1 | conforme |
| 3 | 2610.12445v4, p. 8 | « Each detector’s threshold is set in sample (the 99th percentile of negative steps). » | H1 | conforme |
| 4 | 2610.12445v4, p. 26 | tableau 6, Kimi K3 à 1 % : sonde EFC 64,5, Sol 6.1* 65,1 | H1 | conforme |
| 5 | 2610.12445v1, p. 7 | « Opus 5.5 refuses on 2,638 of the 5,014 positive steps. » | H1 | conforme |
| 6 | 2610.12445v1, p. 6 | « The 14 scenarios are those left after we drop 11 in which a judge cannot tell side-task work from main-task work in a single step » | H1 | conforme |
| 7 | 2610.12445v1, p. 19 | même phrase que le n° 1 | H1 | conforme |
| 8 | 2606.17478v1, p. 30 | « Agentic 0.500/0.000/0.000 0.776/0.571/0.714 » | H1 | conforme |
| 9 | 2611.10620v1, p. 14 | tableau 3 : pic 0.86, ca-glr 0.85, ca-t 0.76 | G2, papier B | conforme |
| 10 | 2611.10620v1, p. 11 | « a running total that builds up evidence round by round » (somme cumulée de Page définie) ; aucune occurrence de « anytime », « e-value », « e-process », « martingale », « always valid » dans tout l'article | papier B, H2 | conforme |
| 11 | 2611.02153v1, p. 7 | « J-PACT reaches an AUROC of 0.921 on Core (mean of four models), which is 85% of the supervised NARCBench probe » ; mêmes mots absents de tout l'article | papier B | conforme |
| 12 | 2606.05384v1, p. 2 | « shows no net target-directed steering beyond neutral reconsideration » ; 0.194 et −0.018 | HC1 | conforme |
| 13 | 2610.29178v1 | aucune sonde parmi les moniteurs : trois occurrences de « probe », toutes au sens d'appels d'essai | HC5 | conforme |
| 14 | 2611.00643v1, p. 1 | « Optimizing the harness for an LLM judge raised judge scores while sharply cutting precision for every generator. » | rôle 1 | conforme |
| 15 | 2611.00643v1, p. 2 | « while cutting precision by 46 » | rôle 1 | conforme |
| 16 | 2611.00643v1, p. 6 | « It is not surprise to experts or to the literature, which we did not measure. » | O4 | conforme |
| 17 | 2611.04556, p. 10 | « robustness to overt pressure offers little assurance against deception » | HC6 | conforme |
| 18 | 2611.04556, p. 48 | environnement E3 : +0.1039, +0.1361, +0.0856 | rôle 1 | conforme |
| 19 | 2608.07556v3, p. 23 | « First handoff at which the constraint is lost, over undefended runs judged as constraint loss » ; ensemble 88.2 / 7.1 / 4.7 ; lignes Cent L1, L2, L3 | H9 | conforme ; **voir B1** |
| 20 | 2605.08647v1, p. 34 | « Per-hop tracer drop rate for linear chain and converging DAG » ; 16 %, 8 %, 3 %, 40 % | H9 | conforme |
| 21 | 2606.10304v1, p. 20 | « The low overall fidelity rate (6/120, 5%) reflects the aligned Qwen-7B attacker model’s refusal behaviour » | HC2 | conforme |
| 22 | 2606.10304v1, p. 21 | « Of the remaining 54 compliant attacks, 31 (57.4%) exceed » | HC2 | conforme |
| 23 | 2610.17301v1, p. 37 | « We predicted this before the confirmation data: the readout was built on informed violations » | H8 | conforme, **mais la phrase porte sur les violations non informées** (« Uninformed violations (preregistered). », même page) ; voir M3 |
| 24 | 2610.17301v1, p. 37 | « preregistered on Gemma-4 after discovery on gpt-oss, 90% CI upper bound 0.51, so not significant » | H8 | conforme ; voir M3 |
| 25 | 2606.07624v1, p. 3 | « with internal representations used only as optional refinements » | H2 | conforme |
| 26 | 2608.12645v2, p. 7 | « L6 is more dissociated still (ρ = 0.33–0.40 with everything else). » | HC6 | conforme |
| 27 | 2602.00750v2, p. 1 | « a single suffix achieves attack success rates of 93.91% and 99.63% in successfully evading all detectors simultaneously » | HC2 | conforme |
| 28 | 2608.21664v1, p. 6 | « falls to 5–21% while think about stays near ceiling » | HC2 | conforme |
| 29 | 2609.20211v1, p. 20 | « Marker visible 0.03 0.68 » | HC5 | conforme |
| 30 | 2609.36490v1, p. 8 | « Cross-architecture transfer: three model organisms trained against different monitor architectures » ; « TPR @ 1% FPR » | H5 | conforme ; **voir B3** |
| 31 | 2504.10374v1, p. 1 | « reducing the success rate of attacks from 58% to 7% at a 5% cost to the performance of a non-malicious agent » | H6 | conforme ; **voir M5** |
| 32 | 2605.26047v2, p. 1 | « gives only a small empirical safety gain in our setting (+3.9 pp, with the confidence interval overlapping zero) » | H6 | conforme |
| 33 | 2604.01151v2, p. 9 | « via SAVI [Howard et al., 2022] for example, would yield formal stopping guarantees. » ; absent de la version 1 | H2, bascule | conforme ; voir m6 |
| 34 | 2604.01151v5 | « sequential » aux pages 3, 6, 18, 19, 25, 26, 35, 37, 38 ; couvre les pages 3, 18, 19, 26 citées par C1 | H2, bascule | conforme |

Bilan : **les citations des rapports tiennent sur les fichiers**. Deux nuances : la lecture du n° 23 par S-7A, reprise
par la synthèse, est inexacte (M3) ; le n° 19 contredit une phrase « non trouvé » de la synthèse (B1).

### 1.4 Ce que je n'ai pas fait
- Aucune lecture des pièces non lues au-delà de leur titre (et d'un résumé, n° 1.2).
- `verifier-arbre` non lancé (il traverserait des chemins interdits au mandat) ; essais du dépôt non lancés.
- Aucune écriture git, aucune dépense, aucun appel de modèle, aucune valeur de clé lue ; aucun chemin interdit ouvert
  (listes de fichiers restreintes à `docs/etat-de-l-art/niveau3-v1`, `docs/sources/lecture-pdf-niveau3`,
  `docs/sources/pdf` et `docs/sources`, filtrées contre les motifs interdits). Aucun refus de permission ni de
  classifieur.

---

## 2. Constats bloquants

### B1 — H9 : « profil de la perte par rang de relais » donné pour non trouvé

MasDrift imprime, page 23, tableau 18, « First handoff at which the constraint is lost » : part des pertes au relais 1,
au relais 2, au relais 3 et plus, pour des hiérarchies de profondeur 1, 2 et 3 (« Cent L1 », « Cent L2 », « Cent L3 » :
88,1 / 11,7 / 0,2 ; 84,4 / 8,8 / 6,7 ; 71,9 / 7,4 / 20,7), et l'ensemble 88,2 / 7,1 / 4,7 (contrôle n° 19). C'est un
profil de la perte par rang de relais, à profondeur contrôlée, pour une contrainte jugée perdue. Le rapport S-12
(section 4, C2) ne laisse libre que le **taux conditionnel** par rang (i), sur **chaînes linéaires de longueur
contrôlée et à tâche égale** (ii), pour la **force graduée** d'une contrainte de sécurité (iii), et nomme « la
répartition du premier relais fautif de MasDrift » comme base à battre (section 5, point 3). Le verdict affaiblit ces
qualificatifs (ni « conditionnel », ni « linéaires », ni « à tâche égale ») ; la phrase pour un jury les supprime tous.

Texte actuel (l. 309-311) :
```text
- **Libre dans les pièces lues.** Un moniteur qui lit chaque passation, traité comme facteur croisé avec la profondeur ;
  le profil du taux de perte par rang de relais, sur chaînes de longueur contrôlée, pour la force d'une contrainte ;
  l'érosion sous un agent qui sabote ; la lecture interne du sous-agent (hors de l'énoncé actuel).
```
Texte corrigé :
```text
- **Libre dans les pièces lues.** Un moniteur qui lit chaque passation et juge si la contrainte y survit, traité comme
  facteur croisé avec la profondeur, avec son taux de faux positifs ; le taux de perte conditionnel à chaque rang de
  relais (parmi les chaînes où la contrainte a survécu jusque-là), sur chaînes linéaires de longueur contrôlée et à
  tâche égale, pour la force graduée d'une contrainte de sécurité (S-12, section 4) ; l'érosion sous un agent qui
  sabote ; la lecture interne du sous-agent (hors de l'énoncé actuel). **Publiés, à citer comme bases** : la
  répartition du premier relais fautif par rang pour des hiérarchies de profondeur 1, 2 et 3 (MasDrift, tableau 18,
  p. 23) ; le taux de perte par relais, tous rangs confondus, sur chaînes linéaires (AgentCollabBench, tableau 23,
  p. 34, S-12).
```
Texte actuel (l. 321-323) :
```text
- **Phrase pour un jury.** « La perte d'une contrainte au passage entre agents est mesurée par d'autres depuis 2026, et
  elle se produit surtout au premier relais. Nous n'en revendiquons pas la mesure. Ce qui n'est pas trouvé : un moniteur
  qui lit chaque passation, croisé avec la profondeur, et le profil de la perte par rang de relais. »
```
Texte corrigé :
```text
- **Phrase pour un jury.** « La perte d'une contrainte au passage entre agents est mesurée par d'autres depuis mai 2026,
  et elle se produit surtout au premier relais ; sa répartition par rang de relais, selon la profondeur, est publiée.
  Nous n'en revendiquons pas la mesure. Ce qui n'est pas trouvé dans nos lectures : un moniteur qui lit chaque
  passation, croisé avec la profondeur, et le taux de perte conditionnel à chaque rang de relais sur des chaînes
  linéaires de longueur contrôlée, pour la force graduée d'une contrainte. »
```

### B2 — « Aucun énoncé occupé en entier », « contre chacun de nos énoncés », « plus de cent cinquante »

La table de la section 5 donne pour O20 le verdict final « **occupé** comme méthode ; restent les chiffres propres »
(l. 491), le premier échelon de l'échelle de la synthèse ; C4 (bloc de collision, point 3) écrit que « seuls les
chiffres propres de l'organisme restent », et tient O1 pour « occupée … même en entier si on la lit comme un principe
d'architecture sans objet » (point 2). La section 9, point 10, dit O5, O6, O15 et le rôle 3 non réexaminés : la lecture
n'a pas porté « contre chacun » des énoncés. Le nombre « plus de cent cinquante » est, selon la synthèse elle-même
(l. 709-710), un ordre de grandeur non recompté (201 avant retrait des doublons, journal, point 3.5) : il ne peut pas
entrer dans une phrase publique (R6, R7). Enfin les quatre resserrements ne sont pas encore décidés par écrit (section 7).

Texte actuel (l. 41-42) :
```text
1. **Aucun énoncé du programme n'est trouvé occupé en entier** dans les pièces lues. Ce résultat est celui que le
   programme préfère ; il est donc à lire avec la section 9 (ce qui n'a pas été lu) sous les yeux (R4).
```
Texte corrigé :
```text
1. **Aucun énoncé des papiers A, B et C n'est trouvé occupé en entier** dans les pièces lues ; dans l'organisme, O20
   est occupé comme méthode (seuls ses chiffres propres restent) et O1 l'est dans son principe. Ce résultat est celui
   que le programme préfère ; il est donc à lire avec la section 9 (ce qui n'a pas été lu) sous les yeux (R4).
```
Texte actuel (l. 704-707) :
```text
« Nous avons fait lire sur source, par des lecteurs qui n'avaient pas écrit le programme, plus de cent cinquante pièces
contre chacun de nos énoncés. Aucun n'est trouvé occupé en entier ; presque tous le sont en partie, et quatre l'ont été
assez pour que nous resserrions ce que nous revendiquons. Nous disons nous-mêmes les résultats publiés qui vont contre
nos prédictions, les erreurs de notre texte envoyé, et ce que nous n'avons pas lu. »
```
Texte corrigé :
```text
« Nous avons fait lire sur source, par des lecteurs qui n'avaient pas écrit le programme, les pièces les plus proches
de nos énoncés, sauf ceux que nous disons non réexaminés. Aucun énoncé de nos trois papiers n'y est trouvé occupé en
entier ; presque tous le sont en partie, et quatre collisions partielles nous conduisent à resserrer ce que nous
revendiquons. Dans l'organisme d'idéation, éprouver le juge sur une vérité plantée est une méthode publiée. Nous disons
nous-mêmes les résultats publiés qui vont contre nos prédictions, les erreurs de notre texte envoyé, et ce que nous
n'avons pas lu. »
```
Et supprimer le paragraphe des lignes 709-710, devenu sans objet. La phrase corrigée ne vaut qu'une fois les quatre
décisions de R-2555 écrites, contre-lues et scellées.

### B3 — H5 : « l'instrument existe hors attaque »

2609.36490, p. 8, figure 4 (a) : trois organismes entraînés chacun contre une architecture de moniteur, évalués contre
les moniteurs tenus à l'écart de chaque architecture, en taux de vrais positifs à 1 % de faux positifs (contrôle n° 30).
C'est la matrice de transfert d'une attaque sur un panel de sondes, sous attaque. N-013 (section 7) la cite déjà comme
l'instrument de H5, et la synthèse la liste parmi les pièces de H5 (l. 271). La phrase pour un jury laisse entendre que
l'instrument sous attaque est libre.

Texte actuel (l. 275-276) :
```text
- **Phrase pour un jury.** « Le résultat existe sur des juges et il est contraire à l'intuition ; sur un panel de
  sondes, l'instrument existe hors attaque, pas la loi. »
```
Texte corrigé :
```text
- **Phrase pour un jury.** « Sur des juges, le résultat existe et il est contraire à l'intuition. Sur des sondes,
  l'instrument existe, hors attaque (2604.13386) et sous attaque entre trois architectures (2609.36490) ; la loi, elle,
  n'est pas trouvée dans nos lectures. »
```

---

## 3. Constats majeurs

### M1 — H1 : phrase pour un jury

Le « le » de « ne le mesure » renvoie au gain, sans « à fausses alarmes égales » ni « à agrégation égale » ; or
l'institut britannique a mesuré sonde contre moniteur boîte noire sur une sous-performance d'agent, sur 17
transcriptions, en aire sous la courbe (S-2A, section 0, point 3 ; synthèse l. 74-76). Les seuils de 2610.12445 sont pris
dans l'échantillon (contrôle n° 3). Le verdict (l. 64-66) est juste ; la phrase pour un jury doit le suivre.

Texte actuel (l. 95-98) :
```text
- **Phrase pour un jury.** « Le gain des sondes sur un moniteur de texte est publié pour du sabotage d'agent noté étape
  par étape, à 1 % de fausses alarmes ; le banc le plus proche écarte lui-même le sabotage étalé. Personne, dans ce que
  nous avons lu, ne le mesure quand aucune étape prise seule n'est étiquetable, et deux bancs publiés montrent qu'au
  seuil strict la sonde peut perdre. »
```
Texte corrigé :
```text
- **Phrase pour un jury.** « Le gain des sondes sur un moniteur de texte est publié pour du sabotage d'agent noté étape
  par étape, à 1 % de fausses alarmes réglées dans l'échantillon ; le banc le plus proche écarte lui-même le sabotage
  étalé. Une comparaison sur une sous-performance d'agent existe, en aire sous la courbe seulement. Dans ce que nous
  avons lu, personne ne mesure ce gain à fausses alarmes égales et à agrégation égale sur la trajectoire quand aucune
  étape prise seule n'est étiquetable, et deux bancs publiés montrent qu'au seuil strict la sonde peut perdre. »
```
Exposition (titres seulement) : lot 9 jamais rendu (travaux citant 2606.08892, qui définit le diffus : les plus
probables concurrents de H1) ; lot 10 (2603.04069, « Monitoring Emergent Reward Hacking During Generation via Internal
Activations » ; 2609.19101, « Monitoring and Discovering Reward Hacking with Internal Representations during LLM
Evaluations », que C5 désigne « à lire contre H1 et H2 ») ; lot 8 (2610.31593, « Simulated Control Evaluations », et
2604.15384, LinuxArena : S-2A, point 4, place la comparaison en sabotage concentré « à une table près ») ; lot 3
(2610.39766, « Activation Probes Are Reliable With a Handful of Positive Examples »).

### M2 — Statistique de population : la pièce libre perd son objet

Lue seule, la phrase en gras revendique toute statistique conjointe à garantie toujours valide. 2601.05427 (S-5A,
section 0, point 2) combine déjà des processus toujours valides entre agents, en boîte noire. S-7B (section 0.1,
point 2) écrit « ni ne teste un adversaire entraîné » ; 2611.10620 a un adversaire faible (agents prévenus, priés
d'évader) et 2609.03035 un adversaire « par le contexte seul » (S-7B, table 0.3). La proposition de section 7, point 3,
dit « sur scores de sondes de copies d'un même modèle ».

Texte actuel (l. 214-217) :
```text
- **Verdict : occupé en partie — collision en cours de décision (R-2555).** La coupe transversale entre agents est
  occupée. La forme « temps × agents » sur scores de sondes est posée. **Une statistique conjointe à garantie toujours
  valide, sur horizon long, démontrée supérieure au séquentiel par agent et à la coupe à fausses alarmes égales, sous
  adversaire : libre dans les pièces lues.**
```
Texte corrigé :
```text
- **Verdict : occupé en partie — collision en cours de décision (R-2555).** La coupe transversale entre agents est
  occupée. La forme « temps × agents » sur scores de sondes est posée. Le squelette toujours valide entre agents existe
  en boîte noire (2601.05427). **Une statistique conjointe sur scores de sondes de copies d'un même modèle, à garantie
  toujours valide, sur horizon long, démontrée supérieure au séquentiel par agent et à la coupe à fausses alarmes
  égales, sous un adversaire entraîné contre elle : libre dans les pièces lues** (S-7B, section 0.1).
```

### M3 — H8 : phrase pour un jury plus forte que la pièce ; fait cité inexact

Sur la page 37 de 2610.17301 (contrôles n° 23 et 24), la phrase « We predicted this before the confirmation data »
porte sur les violations **non informées** ; pour l'injection, l'échec est « preregistered on Gemma-4 after discovery
on gpt-oss, 90% CI upper bound 0.51, so not significant ». Il y a donc bien une prédiction préenregistrée, sur un
second modèle, d'un échec sous attaque tiré du construit identifié — un cas, non significatif, sans attaquant adaptatif.
S-7A laisse à la mère la lecture dure « occupe en partie » (point 2) et ne libère que « la prédiction, mesurée d'abord
et sur plusieurs sondes, de la robustesse adverse par le construit, sur l'axe intention contre conscience
d'évaluation, face à un attaquant adaptatif » (table finale). La phrase pour un jury perd ces qualificatifs.

Texte actuel (l. 198-199) :
```text
  p. 15) ; la sonde « consigne » alarme 21 % et 28 % des contrôles quand la sonde « décision » garde son seuil (p. 19)
  (S-7B). 2610.17301 : construit identifié, échec sous injection prédit puis observé, sur un cas (p. 37, S-7A).
```
Texte corrigé (seconde phrase seulement) :
```text
  (S-7B). 2610.17301 : construit identifié ; sous injection, échec découvert sur un modèle puis préenregistré sur un
  second, non significatif, sur un cas (p. 37, S-7A ; contrôlé sur le fichier par la contre-lecture).
```
Texte actuel (l. 204-206) :
```text
- **Phrase pour un jury.** « Que les sondes lisent la consigne ou la situation plutôt que l'intention est décrit par
  plusieurs équipes, et le lien avec la tenue hors distribution est publié. Prédire la robustesse face à un adversaire
  à partir du construit mesuré ne l'est pas dans nos lectures. »
```
Texte corrigé :
```text
- **Phrase pour un jury.** « Que les sondes lisent la consigne ou la situation plutôt que l'intention est décrit par
  plusieurs équipes, et le lien avec la tenue hors distribution est publié ; un échec sous injection a été prévu à
  partir du construit, sur un cas. Prédire d'avance, sur plusieurs sondes, la robustesse face à un attaquant adaptatif
  à partir du construit mesuré, sur l'axe intention contre conscience d'évaluation, ne l'est pas dans nos lectures. »
```
Texte actuel (l. 194-196) :
```text
- **Verdict : occupé en partie** pour le socle (ce que lit la sonde décide où elle échoue ; lien construit → tenue du
  seuil hors distribution, publié). **La prédiction de la robustesse adverse par un construit mesuré d'abord, sur l'axe
  intention contre conscience d'évaluation : libre dans les pièces lues.**
```
Texte corrigé :
```text
- **Verdict : occupé en partie** pour le socle (ce que lit la sonde décide où elle échoue ; lien construit → tenue du
  seuil hors distribution, publié). **La prédiction d'avance, sur plusieurs sondes, de la robustesse face à un
  attaquant adaptatif par un construit mesuré d'abord, sur l'axe intention contre conscience d'évaluation : libre dans
  les pièces lues** ; la lecture dure de S-7A (« occupe en partie » par 2610.17301) reste à trancher (divergence 9).
```
Exposition (titres) : lot 3, 2610.27577 (« Why Static Probes Fail: Context Determines Deception Feature
Composition ») ; lot 2, Kumar 2026 (« Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry
of Deceptive Representations »), versé et cité par aucun rapport ; lot 8, 2609.15994 (« Latent Undertow: How Ordinary
Typos Break Probes »).

### M4 — L et T : la collision la plus probable est versée et non lue

Le rapport C2 (section 7) nomme comme « voisin le plus probable d'un énoncé à budget borné ; collision possible avec
L3 » Ramtin et collègues (inaccessible) et Huang, Wang et Poor ; comme source de la dichotomie somme contre maximum,
Donoho et Jin ; pour T2, Ramdas, Ruf, Larsson et Koolen, et Vovk. Le lot 8 contient : 1906.08938 (« LPD
Communication: A Sequential Change-Point Detection Perspective », Huang, Wang et collègues ; probablement la pièce de
Huang, Wang et Poor visée par C2, que la passation des pièces range au lot 8 — titre différent, identité non
vérifiée), 2605.16140 (« Covert Bayesian Quickest Change Detection »), math/0410072 (Donoho et Jin, « Higher
criticism for detecting sparse… »), 2102.00630, 1906.09256, 2310.01153, 2501.03982 (« Anytime Validity is Free:
Inducing Sequential Tests »). La synthèse nomme Koning, Ramdas et Vovk (l. 613), pas les deux pièces dont les titres
portent sur un émetteur qui veut rester discret face à un détecteur séquentiel de rupture — la situation même de L.
C2 juge lui-même les composantes libres « élémentaires » (section 4).

Texte actuel (l. 151-152) :
```text
- **Phrase pour un jury.** « Le cœur statistique est classique et nous le citons. Notre apport est l'énoncé adverse à
  budget total borné et sa mesure sur des activations ; il est modeste sur le plan mathématique. »
```
Texte corrigé :
```text
- **Phrase pour un jury.** « Le cœur statistique est classique et nous le citons. Nous visons l'énoncé adverse à
  budget total borné et sa mesure sur des activations ; il est modeste sur le plan mathématique, et la littérature de
  la communication discrète face à un détecteur de rupture, que nous n'avons pas encore lue, en est le voisin le plus
  probable. »
```
Texte actuel (l. 168-170) :
```text
- **Phrase pour un jury.** « Zhang et Gao l'ont posé avant nous pour un agent, en boîte noire. Ce qui nous sépare : la
  distinction entre préserver le multi-ensemble des scores et préserver la loi de chaque pas, l'écriture commune du
  temps et des agents, et la mesure sur activations. »
```
Texte corrigé :
```text
- **Phrase pour un jury.** « Zhang et Gao l'ont posé avant nous pour un agent, en boîte noire. Ce qui nous sépare, dans
  nos lectures : la distinction entre préserver le multi-ensemble des scores et préserver la loi de chaque pas,
  l'écriture commune du temps et des agents, et la mesure sur activations. Les tests d'échangeabilité et d'invariance
  de groupe par e-valeurs, que nous n'avons pas encore lus, peuvent contenir cette écriture commune. »
```
L et T vont dans la liste de la section 6 jusqu'à la lecture du lot 8.

### M5 — H6 : un voisin au dépôt jamais confronté

Ctrl-Z (2504.10374, au dépôt, lu au niveau 2 pour d'autres énoncés) : « reducing the success rate of attacks from 58%
to 7% at a 5% cost to the performance of a non-malicious agent » (p. 1, contrôle n° 31) — la forme même de la marge
asymétrique, pour un rééchantillonnage d'agent, mais déclenché par le moniteur et non « non spécifique » au sens de
N-013 et N-015. 2605.26047 (au dépôt, non relu contre H6) : exécuter l'échantillon le moins suspect ne donne que
« +3.9 pp, with the confidence interval overlapping zero » (p. 1, contrôle n° 32) et contredit Ctrl-Z sur ce point.
Aucun rapport du niveau 2 ni du niveau 3 ne confronte Ctrl-Z à H6 (`anteriorite-v1.md`, section H6, l. 152-164).

Texte actuel (l. 174-175) :
```text
- **Verdict : libre dans les pièces lues sur PDF.** Une lecture dure sur billet reste à trancher : « occupé en partie
  pour le rééchantillonnage, en sabotage concentré » (S-2A).
```
Texte corrigé :
```text
- **Verdict : non tranché ; à ne pas déclarer libre en l'état.** Aucune pièce lue sur PDF ne l'occupe, mais deux PDF
  au dépôt n'ont pas été relus contre H6 : Ctrl-Z, 2504.10374 (rééchantillonnage déclenché par le moniteur : succès des
  attaques de 58 % à 7 % pour 5 % de performance honnête perdue, p. 1) et 2605.26047 (exécuter l'échantillon le moins
  suspect : +3,9 points, intervalle couvrant zéro, p. 1). Lecture dure sur billet : « occupé en partie pour le
  rééchantillonnage, en sabotage concentré » (S-2A).
```
Texte actuel (l. 180-181) :
```text
- **Phrase pour un jury.** « Non trouvé dans nos lectures sur PDF ; un résultat voisin sur le rééchantillonnage en
  sabotage concentré est à lire contre cette hypothèse. Non prioritaire. »
```
Texte corrigé :
```text
- **Phrase pour un jury.** « Une baisse du succès des attaques bien plus rapide que celle de l'utilité est publiée pour
  un rééchantillonnage déclenché par le moniteur. Pour une intervention non ciblée, à intensité fixe, nous ne l'avons
  pas trouvée, mais deux articles voisins n'ont pas encore été relus contre cet énoncé. »
```

### M6 — Tr : pièce libre non énoncée ; voisins versés non nommés

La synthèse ne dit pas ce qui est libre. C5 (table finale) : « Tr, jeton → action sous attaquant adaptatif | libre ;
un voisin sans attaquant » ; S-7A : « Aucun attaquant adaptatif, aucune comparaison d'agrégations au niveau de
l'action ». C5 (section 5) désigne Constitutional Classifiers++ « à lire contre H2 et Tr (score de sonde au fil des
jetons en production) » : versé au lot 11 (2601.04603), non lu. 2603.04069 et 2609.19101 (lot 10, sondes pendant la
génération) non lus.

Texte actuel (l. 185-190) :
```text
- **Verdict : libre dans les pièces lues ; voisins.**
- **Pièces.** Agrégations au niveau de l'action sans attaquant adaptatif : 2610.17301, 2610.40588, 2610.39377 (S-7A) ;
  2610.12445 (p. 3, C5) ; billets (maximum par action puis par trajectoire, l. 136, 252, S-2A).
- **Non lu.** « What the Monitor Saw » (atelier de NeurIPS 2026 ; activations du moniteur, mise en commun et
  combinaison des preuves) : PDF refusé par le site (section 9).
- **Phrase pour un jury.** « Angle mort que nous avons nommé ; une pièce voisine n'a pas pu être obtenue. »
```
Texte corrigé :
```text
- **Verdict : libre dans les pièces lues ; voisins.** Pièce libre : la comparaison, sous attaquant adaptatif, des
  agrégations au niveau de l'action (C5 ; S-7A).
- **Pièces.** Agrégations au niveau de l'action sans attaquant adaptatif : 2610.17301, 2610.40588, 2610.39377 (S-7A) ;
  2610.12445 (p. 3, C5) ; billets (maximum par action puis par trajectoire, l. 136, 252, S-2A).
- **Non lu.** « What the Monitor Saw » (atelier de NeurIPS 2026 ; activations du moniteur, mise en commun et
  combinaison des preuves) : PDF refusé par le site (section 9). Versés et non lus : Constitutional Classifiers++,
  2601.04603 (lot 11 ; score de sonde au fil des jetons, C5), 2603.04069 et 2609.19101 (lot 10).
- **Phrase pour un jury.** « Non trouvé dans nos lectures ; trois pièces voisines versées n'ont pas encore été lues et
  une autre n'a pas pu être obtenue. »
```

### M7 — HC1 : « l'opposition juge contre sonde »

C3 (pistes, l. 456 de C3) : 2607.00415 « touche l'opposition juge / sonde » ; S-7C (section 7) : « HC1, pièce (d) :
lecture interne de la déférence à l'autorité ». Versée au lot 10, non lue. La synthèse la nomme en section 9 sans la
rattacher à HC1 et déclare la pièce (d) libre.

Texte actuel (l. 331-334) :
```text
- **Verdict : occupé en partie, plus qu'au niveau 2.** La forme à destination imposée et le phénomène sont occupés
  (déjà cités comme publiés). **La pièce revendiquée — destination libre testée contre la cible de l'attaquant et
  contre la moyenne du corpus, par famille, dans un moniteur de contrôle, et l'opposition juge contre sonde — est libre
  dans les pièces lues. La porte GC n'est pas déclenchée** (C3, C9, S-7C, V2).
```
Texte corrigé :
```text
- **Verdict : occupé en partie, plus qu'au niveau 2.** La forme à destination imposée et le phénomène sont occupés
  (déjà cités comme publiés). **La pièce revendiquée — destination libre testée contre la cible de l'attaquant et
  contre la moyenne du corpus, par famille, dans un moniteur de contrôle, par régression sur plusieurs intensités — est
  libre dans les pièces lues. L'opposition juge contre sonde n'est pas tranchée** : 2607.00415, désignée pour cette
  pièce par C3 et S-7C, est versée au lot 10 et non lue. **La porte GC n'est pas déclenchée** (C3, C9, S-7C, V2).
```
Texte actuel (l. 357-359) :
```text
- **Phrase pour un jury.** « Nous n'apportons ni la forme ni le phénomène. Nous apportons le test de la destination,
  par famille d'attaque, dans des moniteurs de contrôle, face à des sondes. Un test binaire voisin de notre prédiction
  centrale existe et il est négatif, sur deux juges ; nous rapportons donc la distribution et pas seulement la pente. »
```
Texte corrigé :
```text
- **Phrase pour un jury.** « Nous n'apportons ni la forme ni le phénomène. Nous apportons le test de la destination,
  par famille d'attaque, dans des moniteurs de contrôle. Un test binaire voisin de notre prédiction centrale existe et
  il est négatif, sur deux juges ; nous rapportons donc la distribution et pas seulement la pente. »
```
Exposition (titres) : lot 3, 2610.35930 (« Who Convinced Whom? Tracing How LLMs Change Their Minds in Multi-Agent
Systems ») ; lot 10, 2602.21262 (« Under the Influence… », forme de g selon la passation des pièces), 2305.11888 ;
lot 11, Kumaran et collègues 2026, 2507.03120, Rebholz et collègues 2023, 2502.08177.

### M8 — HC4 : phrase pour un jury absolue

C9 (table finale) : « **occupée en partie** (points de coût épars) ; la comparaison reste libre ; **prémisse
entamée** » — libre dans les pièces lues, donc. La phrase pour un jury dit « n'est pas publiée », sans « dans nos
lectures », pour une zone que la synthèse dit peu cherchée (l. 643). S-7C (section 5) : par une consigne seule, « même
budget que pour les méthodes boîte noire » (2602.08877, budget de 100 évaluations, p. 4, 17-18) — un point de coût
dans un même cadre, quoique sans sonde de tromperie ni juge de contrôle.

Texte actuel (l. 428-430) :
```text
- **Phrase pour un jury.** « La comparaison de coût avec un juge n'est pas publiée. Notre prémisse, elle, est contestée
  des deux côtés : une consigne suffit parfois à déplacer une sonde, et un juge durci n'est pas gratuit à déplacer. Nous
  l'écrivons par régime d'accès et à durcissement égal. »
```
Texte corrigé :
```text
- **Phrase pour un jury.** « Nous n'avons pas trouvé de comparaison du coût d'attaque d'un juge et d'une sonde dans un
  même cadre et à durcissement égal ; des points de coût épars existent, dont une consigne qui, au même budget de cent
  évaluations, trompe des lectures internes et des méthodes boîte noire. Notre prémisse, elle, est contestée des deux
  côtés : une consigne suffit parfois à déplacer une sonde, et un juge durci n'est pas gratuit à déplacer. Nous
  l'écrivons par régime d'accès et à durcissement égal. »
```
Exposition (titres) : lot 11, 2601.04603 (coût des sondes contre classifieurs externes ; 1 700 heures d'équipe
rouge, résumé), 2309.10253 et 2310.08419 (coûts d'attaques boîte noire, sources prévues des chiffres invérifiables de
l'état de l'art v1, l. 140, B2), 2502.19537 (attaques par réglage fin, régime « poids »). HC4 est aussi « peu cherché »
(M14).

### M9 — HC5 : le quorum de juges et de sondes

Le résumé de 2601.04603 (lot 11, non lu) : « we train efficient linear probe classifiers and ensemble them with
external classifiers to simultaneously improve robustness and reduce computational costs », sous « over 1,700 hours »
d'équipe rouge. Ce n'est pas un quorum de moniteurs de contrôle lisant un agent, mais c'est un ensemble de sondes et de
classifieurs externes éprouvé sous attaque. S'y ajoutent les pistes de S-7C (section 7) que la synthèse n'a pas
reprises : He et Yu (quorums à fautes corrélées), « BRANCH », « Screwtape », et 2608.11247 (C3 : « touche HC5 et HC6 »).

Texte actuel (l. 445-447) :
```text
- **Phrase pour un jury.** « Le transfert des attaques entre juges et le quorum avec un moniteur d'un autre type sont
  publiés. Le quorum de juges et de sondes qui lisent l'agent, et sa matrice, ne sont pas trouvés ; et une réécriture de
  confiance peut effacer l'indice qui protégeait le moniteur. »
```
Texte corrigé :
```text
- **Phrase pour un jury.** « Le transfert des attaques entre juges et le quorum avec un moniteur d'un autre type sont
  publiés. Le quorum de juges et de sondes qui lisent l'agent, et sa matrice, ne sont pas trouvés dans nos lectures ;
  un système publié qui combine sondes et classifieurs externes contre le débridage reste à lire. Et une réécriture de
  confiance peut effacer l'indice qui protégeait le moniteur. »
```

### M10 — HC6 : une pièce versée sur la même relation, non signalée

2608.11247 (« Conformity Mitigations in Large Language Models Lie on a Single Resistance–Receptivity Frontier »),
versée au lot 10, non lue, désignée par C3 comme touchant HC6. Une frontière entre réceptivité (déplacement sous
pression bénigne) et résistance (tenue sous manipulation) est, par son titre, la relation que HC6 prédit.

Texte actuel (l. 459-460) :
```text
- **Phrase pour un jury.** « La question est posée par d'autres au niveau de l'item, et la corrélation qu'ils trouvent
  est faible. Notre prédiction par moniteur n'est pas trouvée ; elle doit battre un prédicteur publié. »
```
Texte corrigé :
```text
- **Phrase pour un jury.** « La question est posée par d'autres au niveau de l'item, et la corrélation qu'ils trouvent
  est faible. Notre prédiction par moniteur n'est pas trouvée dans nos lectures, et une pièce sur la frontière entre
  réceptivité et résistance reste à lire ; elle doit battre un prédicteur publié. »
```

### M11 — O4 : la piste la plus dure n'est pas nommée

C4 (section 5, piste 6, « haute » pour O4) : SSRN 6569258, « Can AI Do Financial Research? LLM-Guided Hypothesis
Discovery in Asset Pricing », dont le résumé du moteur dit « tests de nouveauté par englobement contre 209 anomalies
publiées » — un nul formé de lois connues, sur des hypothèses de modèle (piste non opposable). C4 piste 7 :
2609.00731, versé au lot 10, non lu. C4 pistes 8 et 9 : 2110.00115 et 2103.08402 (nul composite « ne fait pas mieux
que »), versés au lot 10, non lus. C7 (section 5) : Clerico 2606.06769, AlphaSchema 2607.26642, Harvey, Liu et Zhu
2016, « Phantom gains: Auditing self-improvement against a measured null » 2608.20290. Lot 4, titres non lus :
2610.07627 (« Learning to Outgrow a Theory… »), 2610.00314 (« Predictive Credit: Measuring What Scientific Explanations
Add to Experimental Forecasts »). La synthèse n'en nomme aucun (l. 633-634 : Martin et « la littérature de finance »).

Texte actuel (l. 514-519) :
```text
**Phrase pour un jury.** « Séparer qui propose de qui juge, calculer la statistique hors des agents, sceller le plan
par empreinte avant les données, contrôler la multiplicité, éprouver le juge sur vérité plantée : tout cela est publié
en 2025 et 2026, et nous le citons. Ce que nous n'avons pas trouvé ailleurs : un juge dont le nul est formé des lois
déjà connues, sur des hypothèses libres, et sa mesure sous un proposeur chargé de le tromper qui en lit la règle. Cette
dernière phrase vaut pour les pièces lues, pas pour le champ : la littérature de finance sur les facteurs redondants
n'a pas été lue. »
```
Texte corrigé :
```text
**Phrase pour un jury.** « Séparer qui propose de qui juge, calculer la statistique hors des agents, sceller le plan
par empreinte avant les données, contrôler la multiplicité, éprouver le juge sur vérité plantée : tout cela est publié
en 2025 et 2026, et nous le citons. Nous n'avons pas trouvé dans nos lectures un juge dont le nul est formé des lois
déjà connues, sur des hypothèses libres, mesuré sous un proposeur chargé de le tromper qui en lit la règle. Cela ne
vaut que pour les pièces lues : en finance, des hypothèses de modèle sont déjà testées contre des centaines d'anomalies
publiées, et ces travaux ne sont pas encore lus. »
```
O4 va dans la liste de la section 6.

### M12 — Rôle 1 : la pièce propre est dite libre sans le lot qui la vise

Le lot 4-B (« juges de la recherche automatisée », passation des pièces, point des sous-agents) n'a pas été rendu.
Lot 4, titres versés et cités par aucun rapport : 2510.18003 (« BadScientist: Can a Research Agent Write Convincing
but Unsound Papers that Fool LLM Reviewers? »), 2606.13044 (« No Hidden Prompts Needed! You Can Game AI Peer Review
with… »), 2608.08975 (« How Can Rhetoric Reward-Hack AI Reviewers? »), 2611.10791 (« Winning Reviews, Losing
Discovery? »), 2609.28614 (« Reward Hacking Challenges Oversight of Autonomous Research Agents »), 2604.22080 (« Sound
Agentic Science Requires Adversarial… »).

Texte actuel (l. 506-509) :
```text
  (p. 19, 48, V2 ; un seul manuscrit) ; 2611.00643 — optimiser un harnais contre un juge modèle fait monter sa note en
  coupant la précision de 46 à 68 % (p. 1, 2, 12, S-4A). **La pièce propre (juge statistique, gain continu, même
  attaque sur les deux juges) : libre dans les pièces lues.** Décision déjà prise par Lazar sur 2611.04556 : citée
  comme précédent de la prémisse, énoncé inchangé (R-2554). 2611.00643 n'a fait l'objet d'aucune décision.
```
Texte corrigé :
```text
  (p. 19, 48, V2 ; un seul manuscrit) ; 2611.00643 — optimiser un harnais contre un juge modèle fait monter sa note en
  faisant baisser la précision de 46 à 68 % selon le générateur (p. 1, 2, 12, S-4A). **La pièce propre (juge
  statistique, gain continu, même attaque sur les deux juges) : non trouvée dans les pièces lues ; le lot 4-B,
  consacré à ces juges, n'a pas été rendu, et six pièces versées sur la tromperie de relecteurs modèles n'ont été lues
  par personne : à ne pas déclarer libre.** Décision déjà prise par Lazar sur 2611.04556 : citée comme précédent de la
  prémisse, énoncé inchangé (R-2554). 2611.00643 n'a fait l'objet d'aucune décision.
```
(La reprise « coupant la précision de 46 à 68 % » se lit comme « de 46 % à 68 % » ; l'article dit « by 46–68% »,
contrôle n° 15 ; c'est le constat mineur m5, corrigé ici en même temps.)

### M13 — Section 9 : ce qui n'a pas été lu est incomplet et en partie mal décrit

1. **Lot 11** : la synthèse le décrit « sources des chiffres invérifiables de l'état de l'art v1, classiques de
   détection séquentielle ». Les 13 fichiers ne contiennent aucun classique de détection séquentielle (Lorden et
   Moustakides, prévus par la passation, n'y sont pas) ; ils contiennent 2601.04603 (HC5, HC4, Tr, H2), 2411.00348 et
   2510.14005 (détection d'injection par traits internes : HC2b, HC3), 2403.14720 et 2505.23643 (protocoles
   « contenu = données » : HC3), 2309.10253, 2310.08419, 2502.19537 (coûts d'attaque : HC4), 2502.08177, 2507.03120,
   Kumaran 2026, Rebholz 2023 (forme de la déférence : HC1), 2604.23459 (« Architecture Matters for Multi-Agent
   Security » : H4′, H9).
2. **Lot 8** : sept des treize fichiers ne sont pas nommés, dont les deux qui comptent le plus pour L (M4) et
   2506.12913 (« Jailbreak Transferability Emerges from Shared Representations » : H5, HC5).
3. **Lot 10** : « et d'autres » cache 2609.00731, 2110.00115, 2103.08402 (O4), 2606.27687 et 2606.11217 (O3, O17,
   O12 ; C4 pistes 4 et 11), 2603.24792 (O2), 2603.04069, 2609.19101, 2406.00799, 2605.28553 (sondes pendant la
   génération : H1, H2, Tr, HC2b), 2608.11247 (HC5, HC6), 2305.11888 (HC1), 2604.19784 (papier B), 2409.07985 (H3,
   H7), 2404.13208 et 2503.18813 (HC3). Le lot 10-A était justement « sondes pendant la génération » (passation des
   pièces) ; la synthèse ne le dit que pour l'histoire des versions.
4. **Lot 3** : « 7 lus (S-3A) » ; S-3A en a lu six de ce lot (son septième, 2606.30449, est au lot 2), cinq autres
   sont lus ailleurs (S-5A, S-7A, S-7B, C5, C8), 2512.22154 n'est cité que comme référence d'un billet (S-2A), et sept
   ne sont cités par aucun rapport : 2609.33102 (ORBIT), 2610.09138 (SwarmReconGuard, « Black-Box Detection of
   Distributed Collective Reconnaissance by Individually Benign-Looking Agent Populations » : papier B, H3, H1 en boîte
   noire), 2610.22723 (LEMON), 2610.27577 (H8, HC2), 2610.35930 (HC1, H9), 2610.37849 (« Detecting Covert Collusion
   between AI Agents… » : papier B, HC2b), 2610.39766 (H1).
5. **Lot 4** : 30 des 41 fichiers (28 travaux) ne sont cités par aucun rapport (liste en section 5) ; ceux qui touchent
   O4, O12 et le rôle 1 sont aux constats M11 et M12.
6. **Lot 2** : onze versions publiées, absentes de la section 9 ; Kumar 2026 (M3) n'est cité par aucun rapport.

Texte actuel (l. 612-619) :
```text
1. **Lots dont les pièces sont versées et qu'aucun lecteur n'a lus** (aucun rapport sur la branche, tête `10016a61`) :
   - lot 8 (13 PDF), dont Koning 2310.01153, Ramdas et collègues 2102.00630, Vovk 1906.09256, 2609.15994, 2604.15384,
     2610.31593 ;
   - lot 10 (23 PDF) : histoire des versions de NARCBench (lot 10-A, qui date l'annonce du séquentiel), 2602.21262,
     2607.00415, et d'autres ;
   - lot 11 (13 PDF) : sources des chiffres invérifiables de l'état de l'art v1, classiques de détection séquentielle ;
   - lot 4 : 41 PDF versés, 9 lus (S-4A) ; lot 4-B (juges de la recherche automatisée) non rendu ;
   - lot 3 : 19 PDF versés, 7 lus (S-3A) ; lot 7 : 39 PDF versés, lus en partie (C8, C9, S-7A à S-7D).
```
Texte corrigé : remplacer ces lignes par la liste des points 1 à 6 ci-dessus, et rattacher chaque pièce à l'énoncé
qu'elle peut toucher (section 5 de cette contre-lecture).

Texte actuel (l. 633-637) :
```text
7. **Pistes nommées par les lecteurs et non lues** : pour O4, Martin, « Regularized e-processes », et la littérature de
   finance sur les facteurs redondants ; Gençay 2608.27734 (O11, O20) ; pour H2, 2602.11409, 2606.07624 (lu par S-5A
   seulement), 2607.02510 et 2606.06223 lus par C5 ; pour le papier B, 2607.06807, 2510.04303 ; pour H8, 2602.01425 ;
   pour HC1, 2607.05545, 2605.03255 ; pour HC5, Pandey et collègues ; pour H4′, Keppo et collègues ; pour H9, la
   référence 38 d'AgentCollabBench et les versions 1 de MasDrift et de Sun.
```
Texte corrigé :
```text
7. **Pistes nommées par les lecteurs et non lues** : pour O4, SSRN 6569258 (priorité haute, C4), Clerico 2606.06769,
   AlphaSchema 2607.26642, Harvey, Liu et Zhu 2016, 2608.20290 (C7), Martin, « Regularized e-processes », et la
   littérature de finance sur les facteurs redondants ; pour O12, Asher et collègues (C4) ; Gençay 2608.27734 (O11,
   O20) ; pour L et T, Ramtin et collègues (inaccessible) et les pièces du lot 8 désignées par C2, section 7 ; pour H2,
   2602.11409 ; pour Tr, H2 et HC5, Constitutional Classifiers++ (versé, lot 11 ; C5) ; pour le papier B, 2607.06807,
   2510.04303 ; pour H8, 2602.01425 ; pour HC1, 2607.05545, 2605.03255, 2607.00415 (versé, lot 10) ; pour HC5,
   Pandey et collègues, He et Yu, « BRANCH », « Screwtape », 2608.11247 (versé, lot 10) ; pour H4′, Keppo et
   collègues ; pour H9, la référence 38 d'AgentCollabBench et les versions 1 de MasDrift et de Sun. Lus par un seul
   lecteur, non recoupés : 2606.07624 (S-5A), 2607.02510 et 2606.06223 (C5).
```

### M14 — H4′, HC2b, HC4 : « peu cherché » absent de leurs verdicts

La synthèse écrit « Peu de requêtes pour H4′, H6, HC2b, HC4 » (l. 643), mais seul H4′ porte la mention dans son
verdict ; HC2b est dit « libre … ; un voisin proche » sans elle, et HC4 « libre » pour la comparaison de coût. Sous R8,
un énoncé peu cherché ne se déclare pas libre en public.

Texte actuel (l. 387) :
```text
- **Verdict : libre dans les pièces lues ; un voisin proche.**
```
Texte corrigé :
```text
- **Verdict : non trouvé dans les pièces lues pour un agent qui tente de persuader son moniteur ; un voisin proche
  pour la dissimulation (NARCBench « Stego »). Peu cherché (section 9, point 9).**
```
Texte actuel (l. 414-416) :
```text
- **Verdict : la comparaison de coût juge contre sonde dans un même cadre est libre dans les pièces lues ; la prémisse
  est entamée des deux côtés.** Le rapport C9 écrit « occupée en partie (points de coût épars) » ; le complément 1
  écrivait « pièce revendiquée libre, prémisse entamée » : même substance, deux mots (section 10).
```
Texte corrigé :
```text
- **Verdict : la comparaison de coût juge contre sonde dans un même cadre est libre dans les pièces lues ; la prémisse
  est entamée des deux côtés.** Le rapport C9 écrit « occupée en partie (points de coût épars) » ; le complément 1
  écrivait « pièce revendiquée libre, prémisse entamée » : même substance, deux mots (section 10). Peu cherché
  (section 9, point 9).
```

---

## 4. Constats mineurs

**m1 — H7 : la pièce libre perd « information mutuelle » et « sur plusieurs tours ».** S-2B (table finale) : « la
**mesure** de la fuite (information mutuelle), la **pente** d'adaptation sur plusieurs tours, la prédiction de l'une
par l'autre, et la comparaison de politiques **ordonnée par cette mesure** ».

Texte actuel (l. 280-282) :
```text
- **Verdict : occupé en partie** (mécanisme, comparaison de politiques de retour, niveaux d'information comparés sur
  sondes). **La mesure de la fuite, la pente d'adaptation et la prédiction de l'une par l'autre : libres dans les pièces
  lues.**
```
Texte corrigé :
```text
- **Verdict : occupé en partie** (mécanisme, comparaison de politiques de retour, niveaux d'information comparés sur
  sondes). **La mesure de la fuite par l'information mutuelle entre l'état de détection et les observations de
  l'attaquant, la pente d'adaptation sur plusieurs tours, la prédiction de l'une par l'autre et la comparaison des
  politiques de riposte ordonnée par cette mesure : libres dans les pièces lues** (S-2B ; S-7B ; C5).
```

**m2 — HC2 : reformulation silencieuse.** « le déplacement continu en fonction de l'intensité » n'est dans aucun
rapport ; S-1 (en-tête) et S-3A (en-tête) écrivent « la mesure continue g en plan apparié » (S-3A ajoute que le plan
apparié existe déjà côté lecteur, ce que la section 7, point 2, rapporte).

Texte actuel (l. 363-365) :
```text
- **Verdict : occupé en partie — collision en cours de décision (R-2555).** **Reste libre dans les pièces lues : la
  sonde qui lit l'agent auteur et adversaire, le déplacement continu en fonction de l'intensité, la comparaison aux
  juges sous les mêmes attaques.**
```
Texte corrigé :
```text
- **Verdict : occupé en partie — collision en cours de décision (R-2555).** **Reste libre dans les pièces lues : la
  sonde qui lit l'agent auteur et adversaire, la mesure continue du déplacement (g) en plan apparié, la comparaison aux
  juges sous les mêmes attaques** (S-1 ; S-3A, qui note que le plan apparié existe déjà côté lecteur, 2610.18408).
```

**m3 — Prononcé 5 et divergence 5 n'attribuent pas le même compte.** l. 50-51 : « deux et une formulation à
restreindre selon C2 » ; l. 659 : « Synthèse provisoire : deux et une formulation contestable ». C2 ne compte pas des
erreurs de fait ; il donne « trois contre-résultats » (section 0).

Texte actuel (l. 50-51) :
```text
5. **Le texte envoyé au fonds contient des erreurs de fait** sur des travaux d'autrui : trois selon B1, deux et une
   formulation à restreindre selon C2 (section 8). Le socle de preuves demande quatre corrections (B3).
```
Texte corrigé :
```text
5. **Le texte envoyé au fonds contient des erreurs de fait** sur des travaux d'autrui : trois selon B1 ; la synthèse
   provisoire en retenait deux et une formulation à restreindre, appuyée sur C2 (section 8). Le socle de preuves demande
   quatre corrections (B3).
```

**m4 — Section 9, point 7 : des pièces lues rangées parmi les non lues** (2606.07624, 2607.02510, 2606.06223). Corrigé
dans le texte de M13.

**m5 — 2611.00643, « coupant la précision de 46 à 68 % ».** Corrigé dans le texte de M12.

**m6 — Prononcé 4 : HELIOS et NARCBench sont un seul article, et l'annonce du séquentiel se date.** Les quatre
fichiers 2604.01151 (versions 1, 2, 4 et 5) portent le même titre ; C1 a lu les versions 3 et 5. Par comptage de mots
seulement (contrôles n° 33 et 34) : la version 1 (1er avril 2026) ne contient pas « sequential » ; la version 2
(9 mai 2026) écrit, p. 9, « Sequential detection. Accumulating evidence across multiple interactions [Kulkarni, 2026],
via SAVI [Howard et al., 2022] for example, would yield formal stopping guarantees. »

Texte actuel (l. 48-49) :
```text
4. **Aucune bascule et aucune porte n'est déclenchée** par les pièces lues (section 6). L'histoire des versions de
   NARCBench, qui date l'annonce du séquentiel, n'a pas été lue (lot 10-A non rendu).
```
Texte corrigé :
```text
4. **Aucune bascule et aucune porte n'est déclenchée** par les pièces lues (section 6). HELIOS et NARCBench désignent
   le même article (2604.01151) ; son annonce du séquentiel figure dès la version 2 du 9 mai 2026 (p. 9, relevé par
   mots de la contre-lecture, non lu en entier) ; les versions 1, 2 et 4 (lot 10-A) n'ont pas été lues.
```
Pour H2, les pièces devraient citer 2611.10620, qui définit une somme cumulée de Page sur scores de sondes d'agents
sans en publier de résultat (p. 11, contrôle n° 10 ; S-7B), et Xie (2606.07624, p. 3), qui propose l'alarme séquentielle
toujours valide avec les représentations internes en raffinement optionnel (contrôle n° 25 ; S-5A).

Texte actuel (l. 132-135) :
```text
- **Phrase pour un jury.** « La somme cumulée sur états internes existe sans garantie et contre une autre menace ; la
  garantie à tout instant existe en boîte noire. Leur réunion sur les sondes de l'agent, contre un sabotage tenu sous le
  seuil, n'est pas trouvée, et l'équipe de NARCBench l'annonce. Les mesures voisines disent que l'accumulation pèse peu
  quand le score par pas est faible : c'est le risque que nous mesurons. »
```
Texte corrigé :
```text
- **Phrase pour un jury.** « La somme cumulée sur états internes existe sans garantie et contre une autre menace ; la
  garantie à tout instant existe en boîte noire. Leur réunion sur les sondes de l'agent, contre un sabotage tenu sous le
  seuil, n'est pas trouvée dans nos lectures ; l'équipe de NARCBench l'annonce depuis mai 2026, une autre équipe en
  définit la forme sans résultat, et une discussion publiée la propose. Les mesures voisines disent que l'accumulation
  pèse peu quand le score par pas est faible : c'est le risque que nous mesurons. »
```

**m7 — Divergences non listées** (section 10) :
19. H1 : S-2A, « aucune occupation ; voisin fort », lecture dure « occupée en partie » pour la comparaison de
    l'institut britannique (section 0, point 3) ; la synthèse la cite (l. 76) sans la ranger parmi les divergences.
20. H2 : S-2A, « occupée en partie, pour la configuration de référence seulement », lecture douce « voisin fort »
    (section 0, point 1) ; la synthèse cite la pièce (l. 113-115) sans verdict.
21. HC2 : S-1 propose « g en plan apparié » ; S-3A dit le plan apparié déjà publié côté lecteur ; rapporté en section 7,
    point 2, pas en section 10.
22. H8 : S-7A écrit à la fois « échec prédit puis observé » et « après coup pour l'injection » (point 2) ; le fichier
    tranche pour la seconde lecture (M3).

**m8 — Un choix tacite sur H8.** S-7A demande à la mère de trancher entre « voisin fort » et « occupe en partie » ; le
verdict de la synthèse (l. 194-196) range l'occupation sur le socle et déclare libre la pièce revendiquée, ce qui
tranche de fait pour la lecture douce. La divergence 9 le dit ; le verdict devrait le dire aussi.

---

## 5. Ce qui n'a pas été lu, énoncé par énoncé (titres seulement)

« Peut toucher » veut dire : le titre d'une pièce versée et non lue, ou la piste nommée par un lecteur, porte sur la
même question. Ce n'est jamais un verdict. Lot 9 : aucune pièce versée, donc aucun titre ; il visait les travaux citant
2606.08892 (diffus), 2512.07810 (boîte blanche de l'institut britannique) et 2606.10456 (théorème de Zhang et Gao), et
les listes d'arXiv du 1er au 10 novembre. Du 10 au 13 novembre : rien de cherché, hors 2611.04556.

| énoncé « libre » | lot 8 | lot 10 | lot 11 | lot 4 et 4-B | lot 3 (non cités) | lot 9 et 10-13 nov. | exposition |
|---|---|---|---|---|---|---|---|
| H1, diffus | 2610.31593, 2604.15384 | 2603.04069, 2609.19101 | — | — | 2610.39766 ; SwarmReconGuard (boîte noire) | oui, au premier chef | moyenne à forte |
| H2, conjonction | 2501.03982 | versions de NARCBench, 2603.04069, 2609.19101, 2103.08402, 2110.00115 | 2601.04603 | 2605.12947, 2410.22318 (sur sorties) | — | oui | moyenne |
| L, parties libres | **1906.08938, 2605.16140, math/0410072** | — | — | — | — | oui (2606.10456) | **forte** |
| T, parties libres | **2310.01153, 2102.00630, 1906.09256** | — | — | — | — | oui (2606.10456) | **forte** |
| H6 | — | — | — | — | — | — | **forte** (deux PDF au dépôt, M5) |
| Tr | — | 2603.04069, 2609.19101 | **2601.04603** | — | LEMON | oui | moyenne à forte |
| H8, prédiction | 2609.15994 | — | — | — | **2610.27577** | — | moyenne (plus lot 2 : Kumar 2026) |
| statistique conjointe, papier B | — | versions de NARCBench, 2604.19784 | — | — | **SwarmReconGuard, 2610.37849**, ORBIT | oui | moyenne |
| H3, deux courbes | 2610.31593 | 2409.07985 | 2604.23459 | — | SwarmReconGuard, ORBIT | oui | faible à moyenne |
| H4′ | — | — | 2604.23459 | — | — | — | moyenne (peu cherché) |
| H5, loi | 2506.12913 | 2608.11247 | 2601.04603 | — | — | — | moyenne |
| H7, fuite et pente | — | 2409.07985 | — | — | — | — | faible |
| H9, moniteur et taux par rang | — | — | 2604.23459 | — | 2610.35930 | — | faible à moyenne |
| HC1, pièce | — | 2602.21262, **2607.00415**, 2305.11888 | Kumaran, 2507.03120, Rebholz, 2502.08177 | — | **2610.35930** | — | moyenne (forte pour l'opposition juge contre sonde) |
| HC2b | — | 2607.00415, 2406.00799 | 2411.00348, 2510.14005 (côté lecteur) | — | 2610.37849 | — | moyenne (peu cherché) |
| HC4, comparaison de coût | 2609.15994 | — | **2601.04603**, 2309.10253, 2310.08419, 2502.19537 | — | — | — | moyenne à forte (peu cherché) |
| HC5, quorum juges et sondes | 2506.12913 | **2608.11247** | **2601.04603** | — | — | — | **forte** |
| HC6, par moniteur | — | **2608.11247** | 2507.03120, Kumaran | — | — | — | moyenne à forte |
| O4 | — | **2609.00731**, 2110.00115, 2103.08402 | — | 2610.07627, 2610.00314 ; SSRN 6569258 (piste) | — | — | **forte** |
| O8 | — | — | — | 2602.18710, 2510.08619, 2606.16999 | — | — | moyenne (énoncé générique) |
| rôle 1, pièce propre | — | — | — | **lot 4-B non rendu ; 2510.18003, 2606.13044, 2608.08975, 2611.10791, 2609.28614, 2604.22080** | — | — | **forte** |

Lot 4, fichiers cités par aucun rapport (30) : 1906.07801, 1912.06116, 1912.11436, 2107.07322, 2311.06412,
2402.18810, 2410.22318, 2410.23614, 2507.00310, 2509.08713, 2510.08619, 2510.18003, 2510.25770, 2511.13825,
2602.18710, 2604.22080, 2605.12947, 2606.13044, 2606.16999, 2607.01131, 2607.09195, 2608.08975, 2608.09855,
2609.28614, 2610.00314, 2610.07627, 2610.25767, 2611.10791, et les versions publiées de Chen 2025 et Dhillon 2026.

---

## 6. Énoncés à ne pas déclarer libres publiquement en l'état

| énoncé | raison principale | ce qui lèverait la réserve |
|---|---|---|
| L, parties libres | collision la plus probable versée et non lue (M4) | lire 1906.08938, 2605.16140, math/0410072 |
| T, parties libres | sources d'invariance et d'échangeabilité versées et non lues (M4) | lire 2310.01153, 2102.00630, 1906.09256 |
| H6 | Ctrl-Z et 2605.26047 au dépôt, jamais confrontés (M5) | les relire contre l'énoncé de N-015 |
| Tr | pièce libre non énoncée ; trois voisins versés non lus (M6) | énoncer la pièce ; lire 2601.04603, 2603.04069, 2609.19101 |
| H8, prédiction | un cas publié de prévision tirée du construit (M3) ; lecture dure laissée à trancher | trancher S-7A ; lire 2610.27577 et Kumar 2026 |
| H4′ | peu cherché (l. 643) | recherche dédiée |
| HC2b | peu cherché ; voisin proche publié | recherche dédiée ; lire 2607.00415, 2610.37849 |
| HC4, comparaison de coût | peu cherché ; points de coût épars (C9) ; lot 11 non lu (M8) | lire 2601.04603 et les sources de coût du lot 11 |
| HC5, quorum juges et sondes | ensemble sondes et classifieurs publié, non lu (M9) | lire 2601.04603, 2608.11247 et les pistes de S-7C |
| HC6, par moniteur | 2608.11247 versée, non lue (M10) | la lire |
| HC1, opposition juge contre sonde | 2607.00415 versée, non lue (M7) | la lire |
| O4 | pistes dures non nommées ; pièces versées non lues (M11) | lire SSRN 6569258 (à récupérer), 2609.00731, 2110.00115, 2103.08402, 2610.07627, 2610.00314 |
| O8 | énoncé générique, aucune recherche dédiée, contre-indices sur sa valeur | recherche dédiée |
| rôle 1, pièce propre | lot 4-B non rendu ; six pièces versées non lues (M12) | rendre le lot 4-B |
| H9, « profil par rang de relais » dans sa rédaction actuelle | contredit par MasDrift, tableau 18 (B1) | adopter la rédaction corrigée de B1 |

**Déclarables, une fois les corrections faites, avec les mentions de la condition 3 du verdict** : H1 (texte de M1),
H2 (conjonction, avec l'annonce de NARCBench datée, m6), statistique conjointe du papier B (texte de M2), H3 (deux
courbes à budget total constant), H5 (la loi, texte de B3), H7 (texte de m1), H9 (moniteur à chaque passation et taux
conditionnel par rang, texte de B1), HC1 (pièce sans l'opposition juge contre sonde, texte de M7). Pour chacun,
l'exposition de la section 5 reste à dire ; pour H1 et H2, le lot 9 est le manque le plus lourd.

---

## 7. Réponses aux quatre questions du mandat

1. **Les phrases « libres » sont-elles celles des rapports ?** Pour H1, H2, L, T, H3, H4′, H5, H6, HC1 (hors
   opposition juge contre sonde), HC5, HC6, O4, O8 et le rôle 1 : oui, à quelques mots près — ce qui ne les rend pas
   déclarables (section 6). Non pour H9 (B1), la statistique conjointe (M2), H8 (M3), Tr (pièce absente, M6), H7 (m1),
   HC2 (m2), HC2b et HC4 (réserve « peu cherché » omise, M14). Les citations des rapports tiennent sur les fichiers
   (34 contrôles).
2. **Les 18 divergences** sont toutes dites en section 10, conformes au journal. Quatre de plus sont à ajouter (m7).
   Tranchés en silence : la reformulation de HC2 (m2), l'élargissement « adversaire » de la statistique conjointe (M2),
   le choix de la lecture douce pour la pièce revendiquée de H8 (m8).
3. **Le « non vérifié » n'est pas complet** (M13) ; exposition énoncé par énoncé en section 5.
4. **Phrases pour un jury plus fortes que leur pièce** : H9 (B1), phrase d'ensemble (B2), H5 (B3), H1 (M1), H8 (M3),
   L et T (M4), H6 (M5), HC4 (M8). HC5, HC6, Tr et la phrase de l'organisme tiennent sur les pièces lues mais doivent
   dire ce qui reste à lire (M6, M9, M10, M11). Les autres (H2, H3, H7, HC1 corrigée, HC2, HC2b, HC3) tiennent.

---

Version 1 ; ne sera jamais réécrite (R12). Fichiers de travail (script, titres) dans le dossier temporaire de la
session, hors dépôt.
