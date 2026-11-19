# Fiche de lecture ciblée — Yuan et al. (2026), « Meta² : Precomputing Reusable Knowledge for Online Harness Evolution in Long-Horizon Agents » — v1

## En-tête

- **Qui écrit** : lecteur neuf du groupe C, lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » (GO-2026-11-19-10) ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni ses compléments, ni la note de lecture de Yu et al.
- **Identifiant** : arXiv 2611.05139, pris dans la bibliographie de Yu et al. (p. 13 du PDF `a8299ba5b16577dd328d602e32f35b914b9393ffb38148d2410f358d4d90ff3d`), vérifié par l'interface publique d'arXiv le 19 novembre 2026 : titre concordant (l'interface l'écrit « Meta$^2$ »), huit auteurs (Yuan, Cai, Liu, Yang, Han, Lee, Sehwag, Huang), tous concordants.
- **Version lue** : version 1, datée du 3 novembre 2026 sur la page 1 ; seule version déposée d'après l'interface d'arXiv (hors pièce empreintée). Dix jours avant Yu et al.
- **Fichier** : `docs/sources/arxiv-2611.05139-v1/arxiv-2611.05139v1.pdf`, empreinte `da9c9e0d2eddb7bce0b10596ee93fcfe7558604bb33f5d9324f6d9e0f5e583ae`, 45 pages.
- **Pages lues** (lecture ciblée, `pdftotext -layout`) : 1 à 9 (résumé, méthode, expériences, travaux voisins, conclusion) ; 18 et 19 (annexe C : bancs, bases, réglages) ; 22 et 23 (répétitions, coût, limites) ; 24, les sections F.2 et F.3 seulement ; 37 (structure d'une entrée). **Non lues** : 10 à 17 (bibliographie, notation, algorithmes), 20 et 21 (études de cas), le reste de 24, 25 à 36 (comparaison des régimes, consignes), 38 à 45.
- **Vocabulaire de cette fiche** : l'« exécutant » résout la tâche ; l'« ajusteur » est un second agent, tenu par le même modèle, qui regarde la course à des points de contrôle et peut modifier le harnais (« evolver ») ; le « recueil de règles d'ajustement » est le savoir appris hors ligne et gelé (« Meta-Skill ») ; une « retouche » est une modification du harnais faite pendant une tâche (« edit »).
- Aucune dépense, aucun appel à un modèle. Réseau : arxiv.org et export.arxiv.org seulement. Aucun refus d'outil.

## Les neuf réponses

**Q1. Ce qui est gardé, et qui l'écrit.**
Deux objets, de vie différente.
- **Le recueil de règles d'ajustement**, appris hors ligne puis gelé. Une entrée porte : identifiant et titre ; type — agir, s'abstenir, ou éviter telle intervention ; moment (début, cours, fin) ; condition observable ; consigne d'ajustement ; raison, c'est-à-dire le schéma vu sur les tâches d'entraînement ; jusqu'à trois exemples de tâches d'entraînement distinctes (tableau 8, p. 37). Il est écrit par trois étapes d'appels au même modèle que l'exécutant : réfléchir sur des groupes de courses, agréger entre tâches, mettre à jour le recueil en ajoutant, fusionnant, affinant ou supprimant (p. 5-6). La matière : pour chaque tâche d'entraînement, trois courses du même exécutant — sans ajusteur, avec l'ajusteur guidé par le recueil courant, avec un ajusteur qui voit le vérificateur — comparées par leurs issues (p. 5).
- **L'état de la course en cours** : l'ajusteur garde sa conversation d'un point de contrôle à l'autre et reçoit le sort de sa retouche précédente — chargée, gardée ou défaite (p. 4-5, p. 19). Tout cela est jeté à la fin de la tâche (p. 19).

**Q2. Transmis à travers un changement, ou tenu pendant une course ?**
Le recueil est transmis des tâches d'entraînement aux tâches tenues à l'écart du **même banc** (un tiers et deux tiers ; 29 et 60 tâches sur Terminal-Bench 2.1, 38 et 75 sur DeepSWE 1.1 ; p. 6, p. 18). Il n'est porté ni vers un autre banc ni vers un autre modèle : un recueil distinct est construit pour chaque couple banc-modèle (p. 7, p. 19). Les retouches, elles, ne vivent que le temps d'une tâche (p. 6).

**Q3. Héritage séparé de la tenue ?**
Oui pour deux objets différents ; non pour un même objet. Cinq bras (p. 8 ; figure 4, p. 9), scores sur Terminal-Bench 2.1 puis DeepSWE 1.1 :
1. l'exécutant seul : 66,33 et 34,67 ;
2. avec l'ajusteur, **sans aucun savoir appris** — il n'a que ce qu'il voit pendant la tâche : 74,67 et 36,44 ;
3. avec l'ajusteur et un recueil tiré des seules courses de l'ajusteur, sans contraste : 77,00 et 35,56 ;
4. avec l'ajusteur et le recueil tiré des contrastes (la méthode) : 81,00 et 44,44 ;
5. comme 4, mais chaque tâche part du harnais laissé par la tâche précédente, retouches gardées : 78,33 et 39,11.
Le bras 4 moins le bras 2 donne ce que le savoir **hérité et gelé** ajoute à l'ajustement **tenu pendant la tâche** : +6,33 et +8,00 points. Le bras 5 moins le bras 4 donne ce que fait l'**héritage des retouches** d'une tâche à la suivante : −2,67 et −5,33 points.
Ce qui est hérité (le recueil) n'est jamais mis à jour pendant l'essai (p. 6) ; ce qui est tenu (conversation, retouches) n'est jamais hérité, sauf au bras 5. Aucun bras ne tient **le recueil** pendant l'essai, ni ne le fait naître vide pour le tenir ; les auteurs le proposent comme suite (p. 24).

**Q4. La mémoire est-elle ablatée ?**
Oui : le bras 2 retire le recueil, le bras 3 le remplace par une version sans contraste (p. 8). Répétitions : cinq exécutions par tâche d'essai sur Terminal-Bench (300 exécutions par méthode), trois sur DeepSWE (225) ; mêmes tâches et même nombre pour toutes les méthodes (p. 18). L'écart-type entre répétitions est donné pour les méthodes du tableau principal — pour la méthode, 81,00 ± 0,91 et 44,44 ± 0,77 ; pour le harnais de départ, 66,33 ± 2,17 et 34,67 ± 1,33 (tableau 5, p. 22) — mais pas pour les bras 2, 3 et 5. Le nombre de constructions indépendantes du recueil n'est pas dit dans les pages lues. Aucun test.

**Q5. Des prédictions écrites avant l'essai ?**
Non trouvé dans les pages lues. Le papier range parmi ses voisins un travail qui lie les modifications à des prédictions vérifiables (p. 9) ; lui-même ne rend à l'ajusteur que le sort technique de la retouche précédente (p. 4-5).

**Q6. Les essais rejetés ou échoués sont-ils gardés ?**
Oui, sous forme de règles : les entrées de type « éviter » viennent des cas où la course avec ajusteur échoue quand la course sans lui réussit, ou des cas où l'ajusteur informé par le vérificateur fait moins bien (p. 5). L'étape de mise à jour peut aussi supprimer des entrées (p. 5). Les décisions prises pendant l'essai et leurs issues ne sont pas réécrites dans le recueil (p. 6).

**Q7. Quel modèle conçoit, quel modèle exécute ?**
Le même modèle tient tous les rôles dans chaque réglage (p. 4, p. 6) : GPT-5.6-Terra, effort moyen, ou DeepSeek-V4-Flash-0731, effort élevé (p. 6).

**Q8. Coût.**
Rapporté en dollars, hors ligne et en ligne séparés, calculé sur les frais par appel (p. 6 ; tableau 1, p. 7). Pour la méthode : 110,19 + 64,72 = 174,91 dollars sur Terminal-Bench 2.1 ; 238,52 + 129,34 = 367,86 sur DeepSWE 1.1. Pour le harnais de départ seul : 34,09 et 62,67. Pour Meta-Harness : 160,51 + 38,34 et 781,56 + 89,19. Le coût n'est pas apparié entre méthodes ; les auteurs tracent un front de compromis (p. 22). Le coût des bras d'ablation n'est pas trouvé dans les pages lues.

**Q9. Objet du résultat, causalité.**
Le score de deux bancs. Les auteurs disent eux-mêmes que leurs contrastes donnent une direction sans établir l'effet d'une décision prise à un point de contrôle, les courses comparées pouvant diverger avant l'intervention (p. 2, p. 5, p. 22-23). Sur les composants, ils écrivent que les ablations « soutiennent » leurs choix (p. 9).

## Une remarque de ce lecteur (à relire avant tout usage)

Le tableau principal compare des méthodes qui diffèrent aussi par leur régime de mémoire à l'essai (p. 6, p. 19) : deux bases continuent de mettre à jour leur réserve d'expérience pendant l'essai ; une troisième part d'un harnais évolué à l'entraînement et garde ses retouches d'une tâche à l'autre ; trois autres gèlent tout après l'entraînement ; la méthode gèle le recueil et remet le harnais à zéro à chaque tâche. Ces régimes ne sont pas croisés avec les méthodes : le tableau principal ne sépare donc rien. Seuls les cinq bras de la figure 4 le font, à méthode fixée.

## Trois citations

1. « Online decisions, task-specific edits, and outcomes are not written back to ℳ; neither held-out verifier feedback nor an LLM-as-a-judge signal is used to update it. » (p. 6)
2. « These contrasts provide directional evidence to act, avoid, or hold without establishing the causal effect of any single checkpoint decision. » (p. 2)
3. « We construct a separate Meta-Skill for each backbone, so this experiment evaluates robustness across backbones rather than zero-shot transfer of a frozen Meta-Skill between models. » (p. 7)

## Ce que ce papier occupe par rapport à notre question de l'héritage séparé de la tenue

- Il occupe, pour le score d'un banc et **à l'échelle d'une tâche**, le contraste « ajustement tenu pendant la tâche, avec un savoir hérité et gelé » contre « le même ajustement sans savoir hérité » (+6,33 et +8,00 points), et montre qu'hériter des retouches de la tâche précédente coûte (−2,67 et −5,33).
- L'héritage y passe des tâches d'entraînement aux tâches d'essai du même banc, avec le même modèle ; ce qui est hérité n'est pas ce qui est tenu ; le recueil n'est jamais tenu pendant l'essai.
- Pour nous : avec MetaSkill, l'un des deux voisins lus qui posent une moitié du plan à trois bras ; à citer avec « savoir gelé, même banc, même modèle, écart-type des bras d'ablation non donné ».

## Réserves

1. Lecture ciblée : les algorithmes de l'annexe B et les consignes (p. 15-17, 25-36) ne sont pas lus ; le détail de ce que voit l'ajusteur au bras 2 vient du texte principal seul (p. 8).
2. Les différences entre bras (+6,33 ; +8,00 ; −2,67 ; −5,33) sont des soustractions faites par ce lecteur sur les scores de la page 8.
3. Un seul lecteur ; aucune contre-lecture à ce jour.
