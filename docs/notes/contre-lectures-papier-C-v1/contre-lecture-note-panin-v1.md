# Contre-lecture neuve de la note « Lecture du voisin Panin » — v1

- **Contre-lecteur** : sous-agent neuf. Je n'ai écrit ni la note, ni sa provenance, ni aucun brouillon du préenregistrement
  du papier C. Le 2026-10-20, vers 19:40 UTC.
- **Pièce relue** : `docs/notes/lecture-voisin-panin-v1-brouillon.md`
  (`5d4261ffe765864fba3438648a4051aef2c9ba99e56d8c722b4e39ad1f55d231`, empreinte recalculée, conforme au compagnon).
- **Source** : `docs/sources/pdf/ssrn-7424179-panin-2026-v1.pdf`
  (`27f88ed7d3b438f596b3b8cbb5ef8805b057e332c1444d8faebd0bd4b3e9a5c0`, recalculée ; 38 pages, 737 796 octets, `pdfinfo`).
  Lu **en entier** par `pdftotext -layout`, pages 1 à 38 : corps p. 1 à 14, bibliographie p. 14 à 17, matériel
  supplémentaire (annexes A à H) p. 17 à 38. Les numéros imprimés en pied de page égalent les numéros du PDF.
- **Provenance** : `docs/sources/pdf/provenance-voisin-panin-v1.md`
  (`66787c140d5e543a30f2615833eb8a8e8bea7a3f414a98ab9c148c9ff5c05295`, conforme).
- **Références** : décisions N-005 et N-006 (`cd49afbc…`), N-013 (`157d388e…`), N-023 (`1297f509…`), empreintes
  recalculées et conformes ; `registres/veille.md` (ligne 2026-W43) ; brouillon 3 du préenregistrement, l. 11
  (`3cc25dcd…`).
- **Outils** (dans `contre-lectures/outils-panin/`, empreintes dans `empreintes-outils-panin-v1.sha256`) :
  `verifier_citations_panin_v1.py` (`7a17e6ba…`) et sa sortie (`299ef2e4…`) : 52 citations cherchées page par page,
  52 trouvées. Normalisation déclarée : apostrophes et guillemets typographiques ramenés à leur forme droite, blancs
  réduits, coupure de fin de ligne recollée.
- **Limites respectées** : dépôt en lecture seule ; aucun fichier interdit lu ; aucun réseau ; aucun service payant.

## Verdict

**Non occupé confirmé.** Panin n'occupe aucune composante de la pièce revendiquée de HC1 (destination libre ĉ, testée
contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre familles, dans des moniteurs de contrôle
sous attaque, par régression sur plusieurs intensités par famille). Les deux déclencheurs de la réserve de N-005 sont
absents : aucune destination libre estimée, aucun nul de retour à la moyenne. La porte GC n'est pas déclenchée.

La note doit pourtant être corrigée avant sa version finale : 14 constats (3 majeurs, 6 mineurs, 5 de forme). Les trois
majeurs portent sur ce que la note décrit mal ou omet : Panin fait varier le **niveau** d'un bilan de compétence (deux
niveaux, addendum exploratoire), il manipule des indices voisins de deux familles d'attaque de HC1 et d'une composante
de HC3, et son poids du conseil est **quasi binaire** (contre-indice pour la lecture de g comme fraction continue).
Aucun de ces points ne change le verdict.

## 1. Les dix citations de la note

Toutes trouvées mot pour mot, à la page dite (sortie de l'outil, lignes `[N]`).

| n° | page | citation (début) | verdict |
|---|---|---|---|
| 1 | 1 | « asks whether the models that pass a deference screen… » | exacte ; apostrophe typographique dans le PDF |
| 2 | 3 | « the advice weight w = (E2 − E1)/(A − E1) is the outcome… » | exacte (légende de la figure 1) |
| 2b | 3 | « Advice — A = E1 ± band » | exacte |
| 3 | 3 et 4 | « \|A − E1\| ∈ {0.15, 0.35, 0.60} of the scale span » ; « by-band and by-type splits are confounded and descriptive only » | exactes |
| 4 | 4 | « 400 numeric-estimation items from four generator families… » | exacte |
| 5 | 1 | « The registered tests did not establish… Source-field effect. » | exacte (coupure « Source-/field » recollée) |
| 6 | 2 | « to our knowledge, this is the first controlled test… » | exacte ; apostrophe typographique |
| 7 | 3 | « Nearest is Bajaj & Tiganj (2026)… » | exacte ; voisin bien présent à la veille, 2026-W43 |
| 8 | 11 | « a deference screen must not threshold the outcome » | exacte ; glose de la note juste (le PDF le dit lui-même p. 12 : « a deference screen selects on the dependent variable ») |

Absences affirmées par la note (l. 52 et l. 53) : vérifiées sur le texte entier, coupures recollées. Zéro occurrence de
« destination », « fixed point », « attract », « monitor », « oversight ». J'ajoute : zéro pour « attack »,
« intensit », « toward the mean », « mean revers », « regression to », « midpoint » ; « regress » une fois, dans le
titre de Rebholz et al. 2024 (p. 16) ; « adversar » trois fois (p. 8 et p. 32 : borne « la plus défavorable » d'une
analyse de sensibilité ; p. 13 : « the one an adversary controls (Greshake et al., 2023) »).

## 2. Jugement de collision, composante par composante (R8, vérifié plus durement)

| composante de la pièce revendiquée | ce que Panin a de plus proche (page) | occupée ? |
|---|---|---|
| destination ĉ **estimée**, non imposée | la cible A est imposée : « Advice — A = E1 ± band » (p. 3) ; w se définit par A ; les composantes du mélange se définissent par rapport à E1 et A : « Mixture components: ignore \|w\| < 0.1; adopt \|w − 1\| < 0.1; away w < −0.1; remainder compromise. » (p. 5). Le poids est quasi binaire : « the judge keeps E1 or copies A exactly » (p. 6). Quand le juge bouge, il va donc à la valeur suggérée : analogue qualitatif de « destination = cible », mais cible imposée, aucune autre destination testée, hors moniteur et hors attaque | non |
| testée contre la cible de l'attaquant v* | aucun attaquant ; A est un conseil, moitié vers la vérité, moitié à l'opposé : « sign stratified toward/away from truth 50/50 » (p. 3) | non |
| testée contre la moyenne du corpus (nul de retour à la moyenne) | absent ; la troisième référence de Panin est la **vérité** (strates de signe, p. 3 ; justesse de E1, p. 11, annexes H.6 p. 35 et 36, H.10 p. 38), jamais une moyenne | non |
| comparée entre familles | neuf cellules d'un **seul** indice, un bilan de compétence « 8/10 » dont varient la source attribuée et la voix (p. 4 ; textes p. 18 et 19) ; c'est le poids (analogue de g, destination imposée) qui est comparé, pas une destination. Chez Panin, « families » désigne les générateurs d'items (p. 4) et les gabarits de formulation (« each with five crossed template families », p. 4), jamais des familles d'attaque | non |
| moniteurs de contrôle sous attaque | juges d'estimation numérique au sens du paradigme juge–conseiller (p. 2), cadrés comme agents qui décident « how far to defer to a peer » (p. 2) ; l'adversaire n'apparaît qu'en discussion (p. 13) ; limite déclarée : « nothing tests a non-verifiable task » (p. 13) | non |
| régression sur plusieurs intensités par famille | distance du conseil en trois bandes, lue en descriptif (p. 3 et 4 ; annexe C.4, p. 22) ; **niveau du bilan** à deux valeurs, 8/10 et 99/100, dans l'addendum X1 : « X1 is exploratory: no verdict rules, no verdict changed. » (p. 11), différences appariées, aucune loi (annexe F, p. 28 à 30) | non |
| opposition juge / sonde | aucune activation ; chez Panin, « probe » veut dire un appel au modèle (« 59,000 probes », p. 1) | non |

**Prédictions de HC1.** Venkatesh et al. avaient pris, en qualitatif, le contenu de la prédiction 1 dans un moniteur
portier (N-023). Panin ne prend le contenu d'aucune prédiction **dans le domaine** de HC1 (moniteurs de contrôle sous
attaque). Hors du domaine, la masse de w en 1 est l'analogue qualitatif de « destination = valeur suggérée », comme la
littérature humaine du poids du conseil déjà citée (N-005). Sa comparaison de neuf variantes d'un même indice est un
analogue lointain de la prédiction 2 (structure de g), hors domaine et à destination imposée.

**Ce qui n'a pas pu être lu.** Les enregistrements sur OSF : « Both embargoed until 2027-09; the embargo is lifted no
later than the preprint. » (p. 1) ; ils portent sur cette étude (p. 14). Les journaux : « Per-probe transcripts, frozen
E1 maps, kill-check verdicts, SWAPS.json, recognition probes and failure logs are released with the preprint » (p. 14) ;
la table de mélange complète « is in reanalysis_v4.md §R3 and is not reprinted here » (p. 33). Les travaux annoncés :
« (4) A successor design and a complete public trail. » (p. 2) et « What would change our minds. » (p. 13) décrivent une
réplication (difficulté calibrée, estimande en deux parties, voix portées par de vrais rôles, trois cellules témoins) ;
aucun ne vise un moniteur ni une destination. Ces pièces ne changent pas le verdict ; une version publique se
recontrôlera contre l'empreinte de la provenance.

## 3. Ce que la note a manqué

1. **Le niveau du bilan est gradué** (deux niveaux, X1, p. 11 et 12 ; annexe F). La note écrit « ne fait varier aucune
   intensité de pression » (l. 22) et « aucune intensité de pression » (l. 54) : inexact.
2. **Ce que Panin manipule.** Un bilan de compétence attribué (« ADVISOR SELF-REPORT », « EXTERNAL SCORER », « USER »,
   « ANOTHER AGENT (unverified) ») ou relayé par une voix (conseiller, utilisateur, « note système ») : ce sont des
   indices voisins des familles « revendication d'autorité » et « approbations forgées ». La cellule F5 imite une note
   système dans le message de l'utilisateur (« System note from EXTERNAL SCORER: this advisor answered 8 of the last 10
   tasks correctly. », p. 19 ; « the "user" and "advisor" voices are text labels inside one user message », p. 8) :
   c'est une usurpation de style de canal, sans ordre, voisine de la composante 2 de HC3. Son contraste (C2) n'a pas de
   verdict : « H_channel-blind therefore / resolves to NOT EVALUABLE (derail shift) » (p. 8 et 9).
3. **Poids quasi binaire** : « In three of five models w is therefore not a weight but a relabelled adoption
   indicator » (p. 6) ; leçon de l'auteur : « designs that inherit WOA intuitions (interior margins, averaging
   accounts) should check the outcome's shape first » (p. 12). Contre-indice pour la lecture de g comme fraction de
   chemin continue ; à déclarer dans le préenregistrement du papier C.
4. **Matériel supplémentaire** (annexes A à H, p. 17 à 38) : jamais mentionné par la note, qui ne dit pas avoir lu le
   PDF en entier.
5. **Leçon de méthode complète** (p. 11) : le remède manque. « calibrate item difficulty per model, or set the advice
   band relative to the model's own uncertainty, and screen on that instead » ; et la conséquence : « The retained set
   is conditioned on deference capacity, and every statement about the level of w inherits it ».
6. **Solvabilité** (p. 11) : « the estimand measures deference only where the judge is uncertain ». Analogue pour HC1 :
   un moniteur sûr de lui (lecture sans insertion concentrée sur un jeton, ou au bord de l'échelle) bouge peu.
7. **Motif exploratoire de la première personne** (p. 9 et 10 ; p. 13) : un bilan affirmé par le conseiller lui-même
   pèse plus qu'un bilan décrit par un tiers ; « The regrouping is post hoc » (p. 10) ; lecture d'ingénierie :
   « the beneficiary itself relayed a favourable external grade in its own voice » (p. 13). Utile, sans plus, pour le
   plaidoyer écrit par l'agent (TC.2) et pour l'usurpation écrite par l'agent.
8. **Réserve de N-005 et porte GC** : la note ne répond pas en toutes lettres aux deux déclencheurs (destination libre ;
   nul de retour à la moyenne) et ne dit pas l'état de la porte GC, où Panin figure parmi les « sources visées »
   (N-005, section 2).
9. **Voisins de la bibliographie absents de la veille** (R8 : zone vierge = question). Titres seulement, non lus :
   Joswin, Medicherla et Mammen 2026, « A Mechanistic View of Authority Hierarchy in LLM Sycophancy », arXiv 2607.00415
   (p. 15) ; Hu et Qu 2026, « Most LLM Conformity Needs No Speaker: Measuring the Speaker-Free Floor in Peer-Pressure
   Benchmarks », arXiv 2607.05545 (p. 15) ; Robinson et al. 2026, « Under the Influence: Quantifying Persuasion and
   Vigilance in Large Language Models », arXiv 2602.21262 (p. 16) ; Hussain et Nielbo 2026, « Conformity Mitigations
   in Large Language Models Lie on a Single Resistance–Receptivity Frontier », arXiv 2608.11247 (p. 15) ; Kumaran et al.
   2026, « Competing Biases underlie Overconfidence and Underconfidence in LLMs » (p. 15) ; Khan et al. 2026, « In
   Agents We Trust, but Who Do Agents Trust? Latent Source Preferences Steer LLM Generations », arXiv 2602.15456
   (p. 15) ; Pan et al. 2026, « User-Assistant Bias in LLMs » (p. 16) ; Zeng 2025, « Who is In Charge? Dissecting Role
   Conflicts in Instruction Following », arXiv 2510.01228 (p. 16) ; Barkett 2026, « Status Hierarchies in Language
   Models », arXiv 2601.17577 (p. 14). Aucun n'apparaît dans `registres/veille.md` ni dans
   `docs/etat-de-l-art-controle-ia-v1.md` (recherche par identifiant et par nom d'auteur). Déjà connu : Mammen, Joswin
   et Venkitachalam 2026, arXiv 2601.13433 (p. 15 ; cité par N-013). À regarder en premier : Joswin et al. (autorité,
   lecture mécaniste : risque sur l'opposition juge / sonde) et Hu et Qu (déplacement sans locuteur : risque sur la loi
   témoin).
10. **Mots trompeurs pour une recherche par mots-clés** : « probe » (un appel au modèle) et « families » (générateurs
    d'items, gabarits de formulation). Le noter évite une fausse collision plus tard.
11. **Bonne pratique utile au papier C** : items décisifs « disjoint from the pilot pool » (p. 4).

## 4. Constats sur la note

Lignes : celles de `docs/notes/lecture-voisin-panin-v1-brouillon.md`.

- **CN-panin-01 — majeur — l. 20 à 23 et l. 54.** Preuve : addendum X1, deux niveaux du bilan, « the registered
  N1/N2/F2/F3 templates with "8 of the last 10" replaced by "99 of the last 100" » (p. 11) ; distance du conseil en trois
  bandes (p. 3). Correction, l. 21 à 23 : remplacer « ne porte sur aucun moniteur de contrôle, ne fait varier aucune
  intensité de pression ni aucune famille d'attaque » par « ne porte sur aucun moniteur de contrôle ni sur aucune
  attaque ; il fait varier la source et la voix d'un bilan de compétence, et, dans un addendum exploratoire, le niveau de
  ce bilan (8/10 et 99/100) ; il n'ajuste aucune loi sur ces niveaux ». Correction, l. 54, colonne Panin : « aucune
  attaque ; niveau du bilan à deux valeurs (X1, exploratoire, une répétition, différences sans loi ; p. 11 et 12 ;
  annexe F) ; distance du conseil en trois bandes, lue en descriptif (p. 3 et 4) ».
- **CN-panin-02 — majeur — l. 27 à 46 (section « Ce que fait le papier ») et l. 54.** Preuve : p. 4 (neuf cellules),
  p. 18 et 19 (textes), p. 8 (étiquettes de texte), p. 8 et 9 (C2 sans verdict). Correction : ajouter les points 2 et 9
  de la version finale (annexe) ; ajouter dans le tableau la ligne « familles « revendication d'autorité » et
  « approbations forgées » ; HC3, composante 2 ».
- **CN-panin-03 — majeur — l. 55.** Preuve : « In three of five models w is therefore not a weight but a relabelled
  adoption indicator » (p. 6) ; p. 12. Correction, colonne Panin : « w = (E2 − E1)/(A − E1), forme déjà citée (N-005) ;
  w quasi binaire chez trois modèles sur cinq (p. 6) : contre-indice pour la lecture de g comme fraction continue, à
  déclarer au préenregistrement du papier C » ; colonne « occupé ? » : « déjà cité ; contre-indice ».
- **CN-panin-04 — mineur — l. 6 à 8.** Preuve : annexes A à H, p. 17 à 38, absentes de la note. Correction : « Lu en
  entier : corps p. 1 à 14, bibliographie p. 14 à 17, matériel supplémentaire (annexes A à H) p. 17 à 38 ».
- **CN-panin-05 — mineur — l. 18 à 25.** Preuve : N-005, réserve (« S'il estime une destination libre ou un nul de retour
  à la moyenne… ») et section 2 (Panin parmi les sources visées). Correction : ajouter « Les deux déclencheurs de la
  réserve de N-005 sont absents (aucune destination libre, aucun nul de retour à la moyenne) ; porte GC non
  déclenchée. »
- **CN-panin-06 — mineur — l. 18 à 25.** Preuve : N-023, section 1 (« Ce qu'il prend »). Correction : ajouter « Il ne
  prend le contenu d'aucune prédiction de HC1 dans son domaine ; hors du domaine, la masse de w en 1 est l'analogue
  qualitatif de « destination = valeur suggérée », comme le poids du conseil humain déjà cité. » C'est ce qui fonde
  l'ajout comme routine (point A2 du rédacteur).
- **CN-panin-07 — mineur — après l. 56.** Preuve : p. 1, p. 2, p. 13, p. 14, p. 33. Correction : ajouter la section « Ce
  qui n'a pas pu être lu » de la version finale.
- **CN-panin-08 — mineur — après l. 56.** Preuve : bibliographie p. 14 à 17 ; veille et état de l'art sans ces
  identifiants. Correction : ajouter la section « Voisins signalés par la bibliographie » de la version finale, et une
  ligne à la veille (2026-W43).
- **CN-panin-09 — mineur — l. 45 et 46.** Preuve : p. 11 (remède et conséquence ; solvabilité). Correction : compléter
  le point 8 par les deux citations du point 12 de la version finale.
- **CN-panin-10 — forme — l. 3.** Preuve : lecture faite vers 11:43 UTC (PDF déposé vers 11:41, provenance). Correction :
  « 11:50 » devient « 11:43 ».
- **CN-panin-11 — forme — l. 13 et 14.** Preuve : N-005, N-013 et N-023 citent d'autres sources. Correction : « Cité comme
  publié : listes de N-005 § 1, N-013 § 1 et N-023 § 1 (entre autres : … ) ».
- **CN-panin-12 — forme — l. 63 à 66.** Preuve : les deux voisins de la veille ont leur note
  (`docs/notes/lecture-voisins-HC1-bajaj-silent-judge-v1-brouillon.md`, `9beecd71…`). Correction : section
  « Conséquences » de la version finale.
- **CN-panin-13 — forme — l. 53 et l. 56.** Preuve : p. 1 (« 59,000 probes ») ; p. 4 (« families »). Correction : ajouter
  la phrase du point 10 ci-dessus.
- **CN-panin-14 — forme — l. 29 et l. 40.** Preuve : le PDF porte l'apostrophe typographique (« advisor’s »).
  Correction : la recopier, ou déclarer la normalisation en tête de section.

## 5. Point A2 du rédacteur (ajout aux « cités comme publiés »)

Pour Panin, la routine me paraît juste : aucune revendication ne change, aucune zone revendiquée n'est trouvée occupée,
et, à la différence de N-023, Panin ne prend le contenu d'aucune prédiction de HC1 dans son domaine. La consignation au
registre des décisions doit le dire en une phrase (constat CN-panin-06).

## Annexe — version finale proposée de la note (texte complet)

Chemin proposé : `docs/notes/lecture-voisin-panin-v1.md` (nom neuf, R12 ; le brouillon reste tel quel). Les champs entre
chevrons se remplissent au versement.

---

# Lecture du voisin Panin (SSRN 7424179) et jugement de collision avec HC1 — v1

Session 14, 2026-10-20 ; lecture du PDF vers 11:43 UTC (PDF déposé vers 11:41 UTC). Brouillon :
`docs/notes/lecture-voisin-panin-v1-brouillon.md` (`5d4261ffe765864fba3438648a4051aef2c9ba99e56d8c722b4e39ad1f55d231`),
gardé tel quel (R12). Cette version reprend le brouillon et les corrections de sa contre-lecture par un sous-agent neuf
(R8 : collision jugée « non occupée », donc vérifiée plus durement) : `<chemin du rapport versé>` (`<empreinte>`).

- **PDF lu** : `docs/sources/pdf/ssrn-7424179-panin-2026-v1.pdf`
  (`27f88ed7d3b438f596b3b8cbb5ef8805b057e332c1444d8faebd0bd4b3e9a5c0`, 38 pages ; provenance
  `docs/sources/pdf/provenance-voisin-panin-v1.md`). Lu en entier : corps p. 1 à 14, bibliographie p. 14 à 17, matériel
  supplémentaire (annexes A à H) p. 17 à 38. Pages : numéros de page du PDF, lus par `pdftotext -layout`. Citations
  contrôlées par script à la contre-lecture ; apostrophes et guillemets typographiques ramenés à leur forme droite.
- **Revendication confrontée** : HC1, loi de déférence des moniteurs de contrôle (`docs/decisions/decision-N-005-N-006-v1.md`,
  section 1 ; précisée par `docs/decisions/decision-N-013-v1.md`, section 1). Pièce revendiquée (N-013) : « la destination
  libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre familles, dans des
  moniteurs de contrôle sous attaque, par régression sur plusieurs intensités par famille ». Cité comme publié : listes
  de N-005 § 1, N-013 § 1 et N-023 § 1 (entre autres : la forme algébrique du poids du conseil, (v − v₀)/(v* − v₀) ; un
  coefficient continu de déférence par modèle, 2606.07897).
- **Raison de la lecture** : le préenregistrement du papier C ne se scelle pas avant cette lecture
  (`brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon3.md`, l. 11). Réserve de N-005 : « S'il estime une
  destination libre ou un nul de retour à la moyenne sur des grands modèles de langage, la pièce revendiquée est
  occupée : nœud immédiat (R8), sans attendre la porte. »

## Verdict

**Non occupé.** Panin mesure le poids d'un conseil vers une cible **imposée** (le conseil A), sur des tâches
d'estimation numérique, en faisant varier la source attribuée et la voix d'un bilan de compétence ; dans un addendum
exploratoire, il fait aussi varier le niveau de ce bilan (8/10 et 99/100). Il n'estime aucune destination libre et
aucun nul de retour à la moyenne ; il ne porte sur aucun moniteur de contrôle ni sur aucune attaque ; il n'ajuste aucune
loi sur des intensités. Les deux déclencheurs de la réserve de N-005 sont absents ; la porte GC n'est pas déclenchée
(N-005, section 2, où Panin figure parmi les sources visées). Il ne prend le contenu d'aucune prédiction de HC1 dans son
domaine (moniteurs de contrôle sous attaque), à la différence de Venkatesh et al. (N-023) ; hors du domaine, la masse
de son poids en 1 est l'analogue qualitatif de « destination = valeur suggérée », comme le poids du conseil humain déjà
cité. Il **s'ajoute aux sources citées comme publiées** de HC1. Aucune zone revendiquée n'est trouvée occupée : pas de
nœud.

## Ce que fait le papier (citations exactes, page du PDF)

1. **Objet** (p. 1, résumé) : « asks whether the models that pass a deference screen weight advice by who an advisor's
   8/10 record is attributed to, or by who relays it ».
2. **Dessin** (p. 1) : « five retained models (four open-weight, one proprietary), 400 items, 59,000 probes » ; ici,
   « probe » veut dire un appel au modèle, pas une sonde d'activations. Neuf cellules : un bilan « 8/10 » attribué à une
   source (piste neutre : « ADVISOR SELF-REPORT », « EXTERNAL SCORER », « USER », « ANOTHER AGENT (unverified) ») ou
   relayé par une voix (piste relais : le conseiller, l'utilisateur, une « note système »), plus une cellule sans bilan
   (p. 4 ; textes en annexe A.3, p. 18 et 19), chacune avec cinq gabarits croisés (« each with five crossed template
   families », p. 4). Ces indices sont voisins des familles « revendication d'autorité » et « approbations forgées » de
   HC1.
3. **Mesure** (p. 3, légende de la figure 1) : « the advice weight w = (E2 − E1)/(A − E1) is the outcome. Only the
   attributed Source (neutral track) or the relaying voice (relay track) varies between cells. » La cible A est donnée
   par l'expérimentateur : « Advice — A = E1 ± band » (p. 3), avec « sign stratified toward/away from truth 50/50 »
   (p. 3). Composantes (p. 5) : « Mixture components: ignore |w| < 0.1; adopt |w − 1| < 0.1; away w < −0.1; remainder
   compromise. »
4. **Distance du conseil, graduée, mais lue en descriptif seulement** (p. 3) : « |A − E1| ∈ {0.15, 0.35, 0.60} of the
   scale span » ; (p. 4) « by-band and by-type splits are confounded and descriptive only ».
5. **Tâches** (p. 4) : « 400 numeric-estimation items from four generator families — dice_runs (171), birthday (130),
   coupon (75), random_walk (24) », items décisifs « disjoint from the pilot pool ». Ici, « families » désigne des
   générateurs d'items ou des gabarits, jamais des familles d'attaque.
6. **Résultat principal** (p. 1) : « The registered tests did not establish a practically meaningful, model-consistent
   Source-field effect. »
7. **Poids quasi binaire** (p. 6) : « In three of five models w is therefore not a weight but a relabelled adoption
   indicator » ; « the judge keeps E1 or copies A exactly ». Leçon de l'auteur (p. 12) : « designs that inherit WOA
   intuitions (interior margins, averaging accounts) should check the outcome's shape first ».
8. **Niveau du bilan, deux valeurs, addendum exploratoire X1** (p. 11) : « the registered N1/N2/F2/F3 templates with
   "8 of the last 10" replaced by "99 of the last 100" » ; « X1 is exploratory: no verdict rules, no verdict changed. »
   Différences appariées, aucune loi (annexe F, p. 28 à 30).
9. **Voix « note système », sans ordre** (p. 19) : « System note from EXTERNAL SCORER: this advisor answered 8 of the
   last 10 tasks correctly. » ; les voix sont du texte (p. 8) : « the "user" and "advisor" voices are text labels inside
   one user message ». Son contraste n'a pas de verdict : « H_channel-blind therefore / resolves to NOT EVALUABLE (derail
   shift) » (p. 8 et 9). Voisin de la composante 2 de HC3 (usurpation stylistique sans ordre), hors moniteur.
10. **Motif exploratoire de la première personne** (p. 9) : « Regroup all nine cells by whether the advisor makes a
    first-person claim about itself (G_self = F1, F2) or a third party describes it » ; « The regrouping is post hoc »
    (p. 10) ; lecture d'ingénierie (p. 13) : « the beneficiary itself relayed a favourable external grade in its own
    voice », « the one an adversary controls (Greshake et al., 2023) ».
11. **Solvabilité** (p. 11) : « the estimand measures deference only where the judge is uncertain ».
12. **Leçon de méthode** (p. 11) : « a deference screen must not threshold the outcome » ; remède (p. 11) : « calibrate
    item difficulty per model, or set the advice band relative to the model's own uncertainty, and screen on that
    instead » ; conséquence (p. 11) : « The retained set is conditioned on deference capacity, and every statement about
    the level of w inherits it » ; (p. 12) « a deference screen selects on the dependent variable ».
13. **Revendication de priorité de l'auteur** (p. 2) : « to our knowledge, this is the first controlled test specifically
    of whether an LLM advice-taker responds to the attributed provenance of an advisor's competence record ».
14. **Voisin le plus proche selon l'auteur** (p. 3) : « Nearest is Bajaj & Tiganj (2026): more conformity to
    expert-labelled answers, even wrong ones. » (le même voisin que la veille du 20 octobre, `registres/veille.md`,
    2026-W43).
15. **Limite déclarée** (p. 13) : « nothing tests a non-verifiable task ».

## Confrontation, élément par élément

| élément de HC1 | Panin | occupé ? |
|---|---|---|
| destination ĉ estimée sans être imposée (régression), testée contre v* et contre la moyenne du corpus | cible imposée (A = E1 ± bande) ; aucun point fixe, aucune destination estimée, aucun nul de retour à la moyenne ; la troisième référence est la vérité (strates de signe, p. 3 ; justesse de E1, p. 11) ; aucune occurrence de « destination », « fixed point », « attract », « toward the mean », « mean revers » ; « regress » seulement dans un titre (p. 16) | non |
| moniteurs de contrôle (juges qui notent des actions d'agents), sous attaque | juges d'estimation numérique (dés, anniversaires, coupons, marches aléatoires) ; aucune attaque, l'adversaire n'apparaît qu'en discussion (p. 13) ; aucune occurrence de « monitor », « oversight », « attack » | non |
| intensité de pression graduée, par famille d'attaque (cinq familles), loi sur les intensités | aucune famille d'attaque ; niveau du bilan à deux valeurs (X1, exploratoire, une répétition, différences sans loi ; p. 11 et 12 ; annexe F) ; distance du conseil en trois bandes, lue en descriptif (p. 3 et 4) | non |
| familles « revendication d'autorité » et « approbations forgées » ; HC3, composante 2 | indices voisins : source attribuée et voix d'un bilan de compétence ; « note système » écrite dans le message de l'utilisateur, sans ordre, sans verdict (p. 8, 9 et 19) | non ; précédent partiel, hors moniteur |
| g comme fraction du chemin, continue | w = (E2 − E1)/(A − E1), forme déjà citée (N-005) ; w quasi binaire chez trois modèles sur cinq (p. 6) | déjà cité ; contre-indice à déclarer |
| opposition sonde / juge (HC2, HC2b) | aucune sonde d'activations ; « probe » = un appel au modèle (p. 1) | non |

## Ce qui n'a pas pu être lu

- Les enregistrements sur OSF (protocole de phase 0, enregistrement confirmatoire) : « Both embargoed until 2027-09;
  the embargo is lifted no later than the preprint. » (p. 1). Ils portent sur cette étude (p. 14).
- Les journaux et transcriptions, « released with the preprint » (p. 14) ; la table de mélange complète, « is in
  reanalysis_v4.md §R3 and is not reprinted here » (p. 33).
- Les travaux annoncés : « (4) A successor design and a complete public trail. » (p. 2) ; « What would change our
  minds. » (p. 13) : réplication à difficulté calibrée, estimande en deux parties, voix portées par de vrais rôles,
  trois cellules témoins. Aucun ne vise un moniteur ni une destination.
- Ces pièces ne changent pas le verdict. Une version publique se recontrôle contre l'empreinte de la provenance.

## Voisins signalés par la bibliographie de Panin, absents de la veille (questions, R8)

Titres seulement (bibliographie, p. 14 à 17), non lus. À contrôler au niveau du résumé avant le scellement du
préenregistrement du papier C ; lecture sur PDF si un résumé parle de moniteur, de destination ou de point fixe, d'une
loi sur des intensités graduées, ou de sondes d'activations.
- Joswin, Medicherla et Mammen 2026, « A Mechanistic View of Authority Hierarchy in LLM Sycophancy », arXiv 2607.00415
  (p. 15). En premier : famille « revendication d'autorité », lecture mécaniste (opposition juge / sonde).
- Hu et Qu 2026, « Most LLM Conformity Needs No Speaker: Measuring the Speaker-Free Floor in Peer-Pressure
  Benchmarks », arXiv 2607.05545 (p. 15). En premier : déplacement sans locuteur (loi témoin).
- Robinson et al. 2026, « Under the Influence: Quantifying Persuasion and Vigilance in Large Language Models », arXiv
  2602.21262 (p. 16).
- Hussain et Nielbo 2026, « Conformity Mitigations in Large Language Models Lie on a Single Resistance–Receptivity
  Frontier », arXiv 2608.11247 (p. 15).
- Kumaran et al. 2026, « Competing Biases underlie Overconfidence and Underconfidence in LLMs », Nature Machine
  Intelligence (p. 15).
- Khan et al. 2026, « In Agents We Trust, but Who Do Agents Trust? Latent Source Preferences Steer LLM Generations »,
  arXiv 2602.15456 (p. 15).
- Pan et al. 2026, « User-Assistant Bias in LLMs » (p. 16) ; Zeng 2025, « Who is In Charge? Dissecting Role Conflicts in
  Instruction Following », arXiv 2510.01228 (p. 16) ; Barkett 2026, « Status Hierarchies in Language Models », arXiv
  2601.17577 (p. 14).
- Déjà connu du programme : Mammen, Joswin et Venkitachalam 2026, arXiv 2601.13433 (p. 15 ; cité par N-013).

## Conséquences proposées

- Ajouter Panin aux « cités comme publiés » de HC1 : poids du conseil chez des grands modèles de langage, préenregistré,
  vers une cible imposée ; poids quasi binaire ; leçon de méthode. Formulation de la revendication de HC1 inchangée.
  Routine : aucune revendication changée, aucune zone trouvée occupée, aucune prédiction prise dans le domaine ; à
  consigner au registre des décisions avec cette phrase.
- Préenregistrement du papier C : déclarer deux contre-indices (R4) : poids quasi binaire (p. 6) ; déférence mesurée là
  seulement où le juge est incertain (p. 11). Appliquer la leçon de méthode en entier (p. 11 et 12) : aucun juge filtré
  ni remplacé sur une fonction de l'issue, et aucune variable de dessin qui suppose la destination à tester.
- HC3, composante 2 : la voix « note système » de Panin (p. 8, 9 et 19) peut se citer comme précédent partiel, sans
  verdict et hors moniteur. Aucun énoncé changé.
- Veille (2026-W43) : ajouter les voisins de la bibliographie ci-dessus ; contrôle des résumés avant le scellement du
  préenregistrement du papier C.
- Verrou « lecture de Panin » du préenregistrement du papier C : levé avec cette version finale. Bajaj et Tiganj, et
  « The Silent Judge », ont leur note : `docs/notes/lecture-voisins-HC1-bajaj-silent-judge-v1-brouillon.md`
  (`9beecd71485678fd5d894825e1223fca42ca3a9dcb9fd24b7dea8388a7e062a5`), à sa propre contre-lecture.
