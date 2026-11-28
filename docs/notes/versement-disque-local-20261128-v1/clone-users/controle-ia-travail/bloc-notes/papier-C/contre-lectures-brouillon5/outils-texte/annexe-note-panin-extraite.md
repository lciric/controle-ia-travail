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
