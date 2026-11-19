# Fiche de lecture ciblée — Qian et al. (2026), « Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI » (« MetaSkill ») — v1

## En-tête

- **Qui écrit** : lecteur neuf du groupe C, lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » (GO-2026-11-19-10) ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni ses compléments, ni la note de lecture de Yu et al.
- **Identifiant** : arXiv 2609.38143, pris dans la bibliographie de Yu et al. (p. 12 du PDF `a8299ba5b16577dd328d602e32f35b914b9393ffb38148d2410f358d4d90ff3d`), vérifié par l'interface publique d'arXiv le 19 novembre 2026 : titre concordant, cinq auteurs (Qian, Zhu, Li, Wang, Ji), les quatre premiers concordent.
- **Version lue** : version 2, datée du 1er octobre 2026 sur la page 1. Le premier dépôt, 29 septembre 2026, vient de la réponse de l'interface d'arXiv, hors pièce empreintée.
- **Fichier** : `docs/sources/arxiv-2609.38143-v1/arxiv-2609.38143v2.pdf`, empreinte `12bc2cab29bde4cef6abe44ba70afa461c1005b4a7ec6e8f31c9b73b92100174`, 22 pages.
- **Pages lues** (lecture ciblée, `pdftotext -layout`) : 1 à 12 (résumé, méthode, expériences, analyses, conclusion) ; 14 à 18 et le début de 19 (annexes A à C : portée, clarifications, reproductibilité, bases). **Non lues** : 13 (bibliographie), la suite de 19 à 22 (études de cas, déclaration d'usage). Les nombres de la figure 3(b) viennent du texte que `pdftotext` extrait de la figure (p. 8) ; ils redonnent les écarts écrits dans le texte (p. 9).
- **Vocabulaire de cette fiche** : le « bâtisseur » est le modèle qui construit un harnais pour chaque tâche (« Builder ») ; la « cible » est le modèle qui exécute la tâche dans ce harnais (« Target ») ; un « principe » est une entrée de la mémoire du bâtisseur (« meta-skill ») ; la « banque » est l'ensemble des principes. Les deux bancs sont Harness-Bench et NewtonBench.
- Aucune dépense, aucun appel à un modèle. Réseau : arxiv.org et export.arxiv.org seulement. Aucun refus d'outil.

## Les neuf réponses

**Q1. Ce qui est gardé, et qui l'écrit.**
Une banque de principes à trois champs — quand un soutien est nécessaire, quoi fournir, comment la cible doit s'en servir (p. 3) —, 192 jetons au plus par principe (p. 16). Elle est écrite **par le bâtisseur lui-même** : après chaque lot, il relit sa banque, les harnais qu'il a produits et le retour public de l'exécution, puis prend une seule décision — garder, réviser un principe, en ajouter un — qui doit citer une preuve du lot (p. 4, p. 16-17). Les versions remplacées restent archivées (p. 17). C'est une mémoire du **concepteur** : des principes pour construire un soutien, non des conseils pour résoudre la tâche (p. 1).

**Q2. Transmis à travers un changement, ou tenu pendant une course ?**
Tenue pendant deux passages sur les tâches de développement (un dixième de chaque banc), puis **gelée** et servie pour les tâches d'essai du même banc (p. 2, p. 5, p. 16). Une étude la transmet aussi à travers un changement de bâtisseur, et de bâtisseur et de cible à la fois (p. 9). Pas de transmission entre bancs : les auteurs la laissent à plus tard (p. 15).

**Q3. Héritage séparé de la tenue ?**
En partie : les deux sont comparés côte à côte, non croisés. Pour un même bâtisseur receveur (Gemini-3.1-Pro) et une même cible (Qwen-Flash), quatre bras (p. 9 ; figure 3(b), p. 8) :
- **sans banque** : le témoin, lancé en même temps que chaque bras ;
- **banque importée et gelée** : apprise par un autre bâtisseur (GPT-5.6-Sol) sur la même cible ; le receveur ne l'a ni écrite ni mise à jour ;
- **banque propre** : le receveur part d'une banque vide et l'apprend lui-même sur les tâches de développement, puis la gèle ;
- **banque importée d'un autre couple** : apprise par l'autre bâtisseur sur une autre cible.
Résultats, score sans banque → score avec banque : sur NewtonBench, banque importée 51,71 → 47,26 (−4,45) ; banque propre 51,71 → 57,19 (+5,48). Sur Harness-Bench, banque importée 65,93 → 68,65 (+2,72) ; banque propre 70,27 → 72,34 (+2,07). Les auteurs écrivent que la banque propre dépasse la banque importée de 9,93 points sur NewtonBench et de 3,69 sur Harness-Bench (p. 9).
**Il manque le bras croisé** : une banque importée que le receveur continuerait de mettre à jour. Les auteurs le proposent comme suite (p. 9, p. 11), ne le font pas. Et aucune banque n'est tenue pendant l'essai : toutes sont gelées avant (p. 16).

**Q4. La mémoire est-elle ablatée ?**
Oui : le bâtisseur à banque vide, même espace de construction et même budget (p. 6, p. 18), contre le bâtisseur à banque entière : 56,36 contre 65,31 en moyenne de six réglages, soit 8,95 points (tableau 3, p. 6). Aussi : banque après zéro, un ou deux passages (figure 2, p. 7), et banque entière contre deux principes au plus choisis par recherche lexicale (p. 4, tableau 3). Une seule exécution par tâche et par condition (p. 12, p. 17) ; des apprentissages indépendants et des exécutions répétées sont renvoyés à plus tard (p. 16) ; 95 et 292 tâches d'essai (p. 5). Comparaisons appariées par tâche, intervalles à 95 % par rééchantillonnage des tâches (20 000 tirages), non corrigés ; ils disent la variation entre tâches, non entre exécutions répétées (p. 17). Les écarts entre campagnes ne sont donnés qu'à titre descriptif (p. 17-18).

**Q5. Des prédictions écrites avant l'essai ?**
Non trouvé dans les pages lues. Une mise à jour doit citer une preuve observée (p. 4) ; rien n'est prédit ni confronté.

**Q6. Les essais rejetés ou échoués sont-ils gardés ?**
Les versions remplacées d'un principe sont archivées (p. 17) ; les pages lues ne disent pas qu'elles sont relues. Un harnais qui échoue à la construction compte zéro et reste au dénominateur (p. 5, p. 17).

**Q7. Quel modèle conçoit, quel modèle exécute ?**
Bâtisseur : GPT-5.6-Sol, pour la construction et pour la mise à jour de la banque. Cibles : Gemini-3.6-Flash, Qwen3.8-Flash, GPT-OSS-120B (p. 5, p. 17). Dans trois réglages, le même modèle tient les deux rôles (Gemini-3.6-Flash, Gemini-3.1-Pro ; p. 8). Température nulle (p. 5).

**Q8. Coût.**
Le budget de la **cible** est fixe et le même dans toutes les conditions : 30 tours, 30 appels d'outils et 96 000 jetons par tâche sur Harness-Bench ; 12 tours, 10 appels et 192 000 jetons sur NewtonBench (tableau 5, p. 17). Le calcul du bâtisseur est hors budget (p. 3) ; son allocation de construction est la même avec et sans banque (p. 14, p. 18). Le coût de l'apprentissage et de la construction n'est pas rapporté ; les auteurs renvoient à plus tard la mesure du gain rapporté à ce coût (p. 12).

**Q9. Objet du résultat, causalité.**
Le score de deux bancs. Les auteurs parlent avec réserve et disent leurs bornes : un bâtisseur principal, deux bancs, une exécution par tâche et par condition (p. 12) ; ils renvoient à plus tard des apprentissages indépendants et des exécutions répétées (p. 16). Sur le transfert, ils écrivent que tous les intervalles contiennent zéro (p. 9).

## Une remarque de ce lecteur (à relire avant tout usage)

Sur Harness-Bench, les témoins sans banque du même bâtisseur receveur, pour la même cible, valent 65,93 (bras de la banque importée), 70,27 (bras de la banque propre) et 63,32 (bras de la banque d'un autre couple) (figure 3(b), p. 8). Les deux premiers diffèrent de 4,34 points, plus que l'avantage de 3,69 points que le texte donne à la banque propre ; les trois s'étalent sur 6,95 points. Mesuré contre son propre témoin, le gain de la banque importée (+2,72) y est même un peu plus grand que celui de la banque propre (+2,07). Le sens « la banque propre fait mieux » ne tient donc, à témoin égal, que sur NewtonBench.

## Trois citations

1. « Skill learning begins with an empty skill bank S0. » (p. 3)
2. « Gemini-Pro’s own bank outperforms the imported Sol-to-Qwen bank by 3.69 points on Harness-Bench and 9.93 points on NewtonBench, with positive gains over its no-skill controls on both benchmarks. » (p. 9)
3. « These results support the feasibility of cross-Builder reuse, although all confidence intervals include zero, leaving the performance benefits uncertain. » (p. 9)

## Ce que ce papier occupe par rapport à notre question de l'héritage séparé de la tenue

- Il occupe, pour une mémoire du **concepteur** et pour le score d'un banc, la comparaison « banque **héritée et gelée** » contre « banque **née vide et apprise par soi** » contre « aucune banque », à travers un changement de concepteur ; une exécution par bras, intervalles du transfert contenant zéro.
- Il n'a pas le bras « héritée puis tenue », et sa banque n'est jamais tenue pendant l'essai : l'héritage et l'apprentissage propre sont deux bras séparés, sans que l'on puisse lire ce que l'un ajoute à l'autre.
- Pour nous : le voisin le plus proche du plan à trois bras parmi les huit lus ; à citer pour ce contraste, avec « une exécution par bras » et la remarque sur les témoins.

## Réserves

1. Les scores de la figure 3(b) sont lus dans le texte extrait de la figure ; leur attribution aux barres est celle que les écarts du texte (p. 9) confirment. Les bornes des intervalles n'ont pas été relevées.
2. Les études de cas (p. 19-22) ne sont pas lues.
3. Un seul lecteur ; aucune contre-lecture à ce jour.
