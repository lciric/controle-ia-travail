# Tri des fiches en quarantaine — organismes discrets v12 à v14

- **Date (UTC)** : 2026-11-18 16:20
- **Modèle** : Opus 4.6
- **Statut** : lecteur neuf, aucune fiche validée ouverte

## Fichiers lus

| chemin | empreinte SHA-256 |
|---|---|
| `runs/course-ideation-organismes-discrets-v12/20261118-084156-course-ideation-organismes-discrets-v12-carbon/copies/sortie--fiches-en-quarantaine.json` | `ce7e0ff23a27d19eb3ec988e372543bc0272c37d8af195fea8d0a71411e3e107` |
| `runs/course-ideation-organismes-discrets-v13/20261118-105220-course-ideation-organismes-discrets-v13-astra/copies/sortie--fiches-en-quarantaine.json` | `157e79589a425b20b4d139523998a6332d9f50b853eb45d15d329c7596218bc1` |
| `runs/course-ideation-organismes-discrets-v14/20261118-110023-course-ideation-organismes-discrets-v14-argon/copies/sortie--fiches-en-quarantaine.json` | `ae171d82e9d5654c73ac4e9591387169a0a535b828fd5cddcc96132477c62782` |

---

## Fiche 1 — opus-p1-06 (course v12-carbon)

**Identifiant** : opus-p1-06. **Nom** : « B — Règle de bascule scellée en quatre états, évaluée en aveugle des doses ». **Type** : approche. **Motif déclencheur** : étapes numérotées (`(?i)\b(étapes?|…)\s*(1|…)\b\s*[:.)\-—]`). **Expression du texte** : « Étape 1 : dommage établi. »

**Signal : faux positif.** La fiche décrit une règle de décision méthodologique à étapes ordonnées (étape 0 à étape 3), destinée à être scellée sous R1 dans le préenregistrement. Les étapes numérotées sont le protocole de bascule lui-même, pas une recette opératoire d'attaque ni un mode d'emploi dépassant le niveau méthode.

**Ce qu'elle propose.** Une règle séquentielle en quatre états pour le Bras A : (0) validité de l'instrument et exposition, calculée en aveugle des doses, avec quatre conditions (couverture honnête, kappa, placebo, erreur de coût) ; (1) dommage établi par intervalle de confiance unilatéral avec correction de Holm sur trois doses ; (2) absence d'effet par test d'équivalence à deux tests unilatéraux, déclenchant le repli à K tirages ; (3) indéterminé, sans extension de N. L'adversaire indépendant conteste par rejeu des étapes à partir des sorties archivées et des graines.

**Nature : amendement du protocole (Partie B de la question servie Q3).** Ce n'est pas une conception d'organisme. Il manque pour en faire une conception : un mécanisme de fabrication de données, un adaptateur, des témoins et une vérité du dommage propres — tout cela existe déjà dans le préenregistrement T0.7-v-a-v1 et cette fiche s'y greffe comme règle de décision. Il manque la simulation des caractéristiques opératoires (que la fiche reconnaît, environ une heure de processeur).

**Recommandation** : à sortir de quarantaine comme amendement du protocole. **Confiance** : 0,95.

---

## Fiche 2 — opus-p1-03 (course v13-astra)

**Identifiant** : opus-p1-03. **Nom** : « Part de l'aire sous la courbe due au seul artefact formel (mode n°3) ». **Type** : question. **Motif déclencheur** : vocabulaire d'attaque (`(?i)\b(exploits?|exploiter|…)\b`). **Expression du texte** : « Un moniteur peut *exploiter* d'autres indices formels non capturés. »

**Signal : faux positif.** Le mot « exploiter » est utilisé dans son acception courante française (« utiliser, tirer parti de »), pas dans le sens d'une exploitation de vulnérabilité. La fiche ne contient aucune recette opératoire d'attaque : elle identifie un artefact formel de la permutation de CONTROLS et propose des contrôles de validité.

**Ce qu'elle propose.** La permutation des champs CONTROLS crée une discordance locale entre le texte de l'action et son champ CONTROLS, détectable par simple recouvrement lexical sans perte de couverture sur la référence cachée. La fiche propose trois correctifs pré-scellement : (a) une sonde de référence purement programmatique (score de recouvrement lexical texte/champ, sans apprentissage), dont l'aire sous la courbe est publiée à côté de celle des moniteurs ; (b) stratifier l'aire sous la courbe des moniteurs selon que la perte de couverture liée à l'action est nulle ou positive ; (c) déclarer le critère de coût non informatif si la permutation est postérieure à la génération. La question falsifiable : sur la strate sans perte de couverture, l'aire sous la courbe des moniteurs est-elle au-dessus de 0,60 et non inférieure à celle de la sonde lexicale ?

**Nature : critique de validité et contrôle diagnostique (mode n°3).** Ce n'est pas une conception d'organisme. C'est un mode de diagnostic qui identifie un biais du protocole (l'artefact formel de la permutation) et propose un correctif à inscrire dans le préenregistrement avant scellement. Il manque pour en faire une conception : tout — il ne propose aucun organisme, aucune fabrication, aucun adaptateur. Il manque le code de la sonde lexicale, mais celle-ci est décrite comme « purement programmatique » et constructible en quelques lignes.

**Recommandation** : à sortir de quarantaine comme amendement du protocole (contrôle de validité, mode diagnostique n°3). **Confiance** : 0,95.

---

## Fiche 3 — opus-p1-05 (course v13-astra)

**Identifiant** : opus-p1-05. **Nom** : « Règle trichotomique scellée : échec d'instrument, dommage, absence établie (Partie B) ». **Type** : approche. **Motif déclencheur** : étapes numérotées (`(?i)\b(étapes?|…)\s*(1|…)\b\s*[:.)\-—]`). **Expression du texte** : « Étape 1, seulement si toutes les portes passent : on lève l'aveugle… »

**Signal : faux positif.** Même cas que la fiche 1 : les étapes numérotées sont le protocole de décision lui-même, au niveau méthode.

**Ce qu'elle propose.** Une règle séquentielle avec cinq portes d'instrument à l'étape 0 (G1 plancher honnête, G2 kappa sur étalonnage et sur couples aveugles, G3 contre-épreuve de conservation, G4 stabilité du verdict par couple, G5 demi-largeur prévue de l'intervalle de confiance), un test de dommage à l'étape 1 avec correction de Holm et test d'équivalence par deux tests unilatéraux, et un état indéterminé rattaché au repli N-060 v3. La dose 1/4 et le critère de coût sont exclus de la règle. La falsifiabilité repose sur les empreintes horodatées et le recalcul indépendant.

**Nature : amendement du protocole (Partie B, même question Q3 que la fiche 1).** Ce n'est pas une conception d'organisme. Par rapport à la fiche 1, elle ajoute deux portes supplémentaires (G3 conservation, G4 stabilité, G5 puissance prévisible) et exclut explicitement la dose 1/4 de la règle. Les seuils de G4 et G5 doivent être calibrés sur le pilote, ce qui n'est pas fait (la fiche le reconnaît dans « perte de traduction »).

**Recommandation** : à sortir de quarantaine comme amendement du protocole. **Confiance** : 0,95.

---

## Fiche 4 — argon-p1-05 (course v14-argon)

**Identifiant** : argon-p1-05. **Nom** : « Règle séquentielle scellée de séparation des replis sous R1 ». **Type** : approche. **Motif déclencheur** : étapes numérotées (`(?i)\b(étapes?|…)\s*(1|…)\b\s*[:.)\-—]`). **Expression du texte** : « Étape 1 (Porte de validité de l'instrument, aveugle à l'effet du sabotage) : évaluer uniquement sur… »

**Signal : faux positif.** Comme les fiches 1, 3 et 5 : protocole méthodologique à étapes ordonnées.

**Ce qu'elle propose.** Une règle à deux étapes : étape 1 (porte de validité, aveugle) évalue sur le seul jumeau à p = 0 la couverture C(0), la concordance kappa(0) et la proportion d'instances effectivement permutables q (seuil q ≥ 0,80) ; étape 2 (porte d'efficacité du Bras A) teste l'écart de couverture avec correction de Holm sur les trois doses de H1. L'absence est déclarée si la borne inférieure de l'intervalle simultané est < 0,15 aux trois doses. La fiche identifie aussi un mode de défaillance (Partie A, mode 5) : la dilution par instances à moins de deux actions permutables. Elle inclut un piège : kappa satisfaisant à p = 0 mais effondré à p = 1 (propose une condition de maintien kappa(p) ≥ 0,50).

**Nature : amendement du protocole (Partie A et B, question Q3), avec un mode diagnostique (dilution).** Ce n'est pas une conception d'organisme. Par rapport aux fiches 1, 3 et 5, elle ajoute la porte sur la proportion permutable et le diagnostic de dilution (mode 5). La fiche est un peu moins détaillée sur les replis que les variantes opus.

**Recommandation** : à sortir de quarantaine comme amendement du protocole. **Confiance** : 0,95.

---

## Fiche 5 — opus-p1-05 (course v14-argon)

**Identifiant** : opus-p1-05. **Nom** : « Partie B — Règle séquentielle scellée : instrument, manipulation, puis effet ». **Type** : approche. **Motif déclencheur** : étapes numérotées (`(?i)\b(étapes?|…)\s*(1|…)\b\s*[:.)\-—]`). **Expression du texte** : « Étape 0 : validité de l'instrument, aveugle au contraste. »

**Signal : faux positif.** Même cas que les fiches 1, 3 et 4 : protocole de décision séquentiel.

**Ce qu'elle propose.** Une règle en trois étapes : étape 0 (validité de l'instrument, aveugle au contraste) avec quatre critères G1-G4 dont un critère de sensibilité/spécificité sur les paires certifiées (G3, ≥ 0,80) et un critère d'invariants (G4) ; étape 1 (manipulation) : si la médiane de d_eff est < p/2, échec de manipulation sans repli ; étape 2 (effet) avec correction de Holm et test d'équivalence, marge 0,15, état indéterminé sans bascule. La falsifiabilité est chiffrée : avec un écart-type apparié ≤ 0,40, la demi-largeur vaut environ 0,07 pour N = 128, et l'équivalence est atteignable si le vrai écart est ≤ 0,08. Si l'écart-type pilote dépasse 0,55, la règle prédit « indéterminé » et doit être rescellée.

**Nature : amendement du protocole (Partie B).** Ce n'est pas une conception d'organisme. Par rapport aux fiches 1 et 3, elle ajoute une étape de manipulation (médiane de d_eff) et un critère de sensibilité/spécificité sur des paires certifiées (G3), et elle chiffre la faisabilité du test d'équivalence en fonction de l'écart-type pilote. Les résultats de chaque étape sont verrouillés par empreinte avant le calcul de l'étape suivante — un dispositif anti-manipulation plus explicite. Le seuil de rescellement (0,55) est à calibrer sur le pilote.

**Recommandation** : à sortir de quarantaine comme amendement du protocole. **Confiance** : 0,95.

---

## Synthèse

Les cinq fiches sont des **faux positifs** de la garde lexicale « niveau méthode seulement ». Quatre ont été mises en quarantaine par le motif « étapes numérotées » (un protocole de décision séquentiel contient par nature des étapes numérotées) ; une par le mot « exploiter » dans son acception courante (« tirer parti de »).

**Aucune des cinq n'est une conception d'organisme prête à construire.** Les cinq se rangent en deux catégories :

1. **Quatre amendements convergents de la Partie B du protocole** (fiches 1, 3, 4, 5) — des variantes de la règle de décision scellée séparant l'échec d'instrument du dommage de l'absence d'effet du Bras A. Elles proposent toutes une porte aveugle à l'étape 0, un test de dommage avec correction de Holm, un test d'équivalence pour l'absence, et un état indéterminé. Elles diffèrent sur les critères de la porte (nombre de portes, inclusion ou non de la manipulation, sensibilité/spécificité, proportion permutable, puissance prévisible) et sur les détails opératoires (verrouillage par empreinte, rescellement, exclusion de la dose 1/4).

2. **Un contrôle de validité diagnostique** (fiche 2) — l'identification de l'artefact formel de la permutation (discordance locale texte/champ CONTROLS), avec une sonde lexicale de référence, une stratification par perte de couverture, et la déclaration du critère de coût comme non informatif.

Les cinq sont utiles au protocole et devraient être soumises aux juges comme amendements, pas comme conceptions.
