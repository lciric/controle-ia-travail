# Fiche de lecture — Wang et al. (2026), « Rethinking the Evaluation of Harness Evolution for Agents » — v1

## En-tête

- **Qui écrit** : lecteur neuf du groupe C, lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » (GO-2026-11-19-10) ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni ses compléments, ni la note de lecture de Yu et al.
- **Identifiant** : arXiv 2607.12227, pris dans la bibliographie de Yu et al. (p. 12 du PDF `a8299ba5b16577dd328d602e32f35b914b9393ffb38148d2410f358d4d90ff3d`), vérifié par l'interface publique d'arXiv le 19 novembre 2026 : titre concordant, onze auteurs (Wang, Zhu, Hu, Yuan, Chen, Senthil, Hajishirzi, Tsvetkov, Smith, Dasigi, Xiao), les quatre premiers concordent.
- **Version lue** : version 4, datée du 5 octobre 2026 sur la page 1. Le premier dépôt, 14 juillet 2026, vient de la réponse de l'interface d'arXiv, hors pièce empreintée. La bibliographie de Yu et al. ne dit pas quelle version ils citent.
- **Fichier** : `docs/sources/arxiv-2607.12227-v1/arxiv-2607.12227v4.pdf`, empreinte `a65805f7a4cc6a522055a3f696b72a787b3deb504d7d855f60b54afc5b696fc7`, 26 pages.
- **Pages lues** : 1 à 26, en entier, par `pdftotext -layout`, page par page (bibliographie p. 10-11 parcourue). La page 26 ne porte que les courbes de la figure 6 ; aucun chiffre n'en est tiré.
- **Vocabulaire de cette fiche** : l'« exécutant » résout les tâches ; l'« agent de révision » modifie le harnais (« meta agent ») ; un « essai » est une exécution complète d'une tâche. Les quatre méthodes comparées : l'« échantillonnage parallèle » (plusieurs essais indépendants, harnais fixe), le « raffinement séquentiel » (chaque essai lit un résumé du précédent, harnais fixe), l'« évolution du harnais » (un harnais commun révisé sur un lot de tâches) et la « révision du harnais par tâche » (« Harness Scaling » : un harnais révisé pour une seule tâche). Le « taux de réussite par essai » est « pass@1 » ; la « réussite en cinq essais » est « pass@5 » (p. 13).
- Aucune dépense, aucun appel à un modèle. Réseau : arxiv.org et export.arxiv.org seulement. Aucun refus d'outil.

## Q8 d'abord : quelles bases appariées, et que montrent-elles ?

**Ce qui est apparié.** Un « budget de calcul » K, compté en essais par tâche : K = 5 pour les quatre méthodes ; pour l'évolution du harnais, un essai par tâche et par tour, pour égaler ce compte (p. 5). Le même harnais de départ pour tous, celui d'Agentic Harness Engineering (Lin et al.) : un seul outil de terminal, ni compétences, ni intergiciel, ni mémoire persistante (p. 5, p. 12). Le même régime de retours : sans cas de test, ou avec (p. 3-5). Le même modèle dans tous les rôles, 128 000 jetons de génération au plus, effort de raisonnement élevé (p. 5, tableau 6 p. 12). Banc : Terminal-Bench 2.1, 89 tâches ; trois modèles ; moyenne de deux courses indépendantes (p. 5).

**Ce qui n'est pas apparié.** Le coût de la modification du harnais est laissé hors du compte (p. 13) ; ni jetons ni dollars ne sont rapportés. Les auteurs disent que le compter renforcerait leur conclusion (p. 13). « Budget apparié » veut donc dire, dans ce papier : même nombre d'essais (Terminal-Bench), même nombre d'actions (2 000, jeux ARC-AGI-3, p. 9 et p. 17), ou même durée d'horloge (douze heures, jeux d'EdgeBench, temps de révision compris, p. 24). Sur ARC-AGI-3, seules les actions dans le jeu comptent ; le raisonnement et la lecture sont gratuits (p. 16).

**L'évolution du harnais évaluée ici** est celle d'Agentic Harness Engineering, agent d'exploration désactivé, parce qu'il importe des harnais déjà réglés pour le banc (p. 4, p. 12).

**Ce que les bases montrent sur Terminal-Bench 2.1** (moyenne des trois modèles) :

| condition | sans cas de test, taux par essai (tableau 1, p. 6) | avec cas de test, taux par essai (tableau 2, p. 6) | avec cas de test, réussite en cinq essais (tableau 2, p. 6) |
|---|---|---|---|
| un essai, harnais de départ | 68,2 | 67,6 | — |
| échantillonnage parallèle | 72,3 | 82,0 | 82,0 |
| raffinement séquentiel | 69,3 | 76,9 | 87,1 |
| évolution du harnais | 67,4 | 69,7 | 79,0 |
| révision du harnais par tâche | 71,8 | 75,5 | 85,6 |

Avec cas de test, les tests servent à la fois de retour et d'oracle qui choisit l'essai rendu (p. 6) ; recherche et mesure portent sur les mêmes 89 tâches.

**Tenue à l'écart** (tableau 3, p. 7) : 45 tâches d'entraînement, 10 de validation, 34 d'essai ; harnais évolué sur l'entraînement, choisi sur la validation, mesuré sur l'essai. Harnais de départ 63,2 ; harnais évolué 63,2 (écarts par modèle : +1,2 ; 0,0 ; −1,4). Les trois autres méthodes ne s'y appliquent pas : elles ne produisent pas d'objet réutilisable (p. 7).

**Budget doublé** (K = 10, Claude Opus 4.6 seul, deux courses, p. 15) : sans cas de test (tableau 7), échantillonnage parallèle 73,6 ; raffinement séquentiel 71,6 ; évolution du harnais 71,9 ; révision du harnais par tâche 73,6 — aucune méthode à harnais ne dépasse la meilleure base. Avec cas de test (tableau 8), la révision du harnais par tâche passe devant (90,5 contre 89,6 et 88,7 en taux par essai) et la légende dit l'écart dans la variation entre courses. Tenue à l'écart (tableau 9) : 63,3 → 63,0.

**Sur les jeux, le sens s'inverse.** ARC-AGI-3, 25 jeux publics, efficacité d'action relative à l'humain (tableau 4, p. 8) : avec Claude Opus 4.8, 43,3 sans mémoire, 59,3 avec la mémoire tenue, 77,5 quand l'agent peut aussi écrire compétences, outils et crochets ; avec GPT-5.6 Terra, 21,1 ; 25,9 ; 38,2. EdgeBench, cinq tâches de jeu, deux courses (tableau 5, p. 9) : 48,3 → 54,7 (Claude Opus 4.8) et 45,9 → 49,8 (GPT-5.4).

## Les autres réponses

**Q1. Ce qui est gardé, et qui l'écrit.**
Sur Terminal-Bench : une « réserve d'expérience », à laquelle chaque tour ajoute le harnais du tour, ses essais et, s'il y a des cas de test, leurs issues (p. 4) — écrite par la boucle, donc par un programme. Une fonction de résumé, tenue par le même modèle que l'exécutant, en tire ce que lit l'agent de révision (p. 3) ; en pratique, l'agent d'analyse des traces d'Agentic Harness Engineering écrit un rapport par tâche et une vue d'ensemble, les traces brutes restant consultables (p. 12). Sur ARC-AGI-3 : deux fichiers écrits **par l'agent lui-même**, par des outils de lecture et d'écriture — un guide du jeu gardé d'un niveau à l'autre, et un brouillon remis à zéro à chaque niveau (p. 17) ; dans la variante complète, aussi des compétences, des outils et des crochets (p. 17).

**Q2. Transmis à travers un changement, ou tenu pendant une course ?**
Tenu pendant une course. Rien n'est porté à travers un changement de banc, de modèle ou de génération. Le seul passage est celui du **harnais** évolué vers 34 tâches du même banc tenues à l'écart (p. 7). Sur les jeux, chaque moteur est lancé séparément sur chaque jeu (p. 16).

**Q3. Héritage séparé de la tenue ?**
Non : aucun bras n'hérite d'une mémoire. Une moitié de la séparation existe, la tenue seule, à nombre d'actions égal (tableau 4, p. 8 ; p. 16-17) : le bras sans mémoire (guide et brouillon désactivés) contre le bras à mémoire tenue pendant la course. Écart : +16,0 points avec Claude Opus 4.8, +4,8 avec GPT-5.6 Terra (p. 8-9). Le papier ne dit pas en toutes lettres que cette mémoire naît vide.

**Q4. La mémoire est-elle ablatée ?**
Oui, sur ARC-AGI-3 : sont retirés le guide, le brouillon et les outils qui les tiennent (p. 17). Le nombre de courses derrière le tableau 4 n'est pas dit (les deux courses indépendantes sont annoncées pour Terminal-Bench, p. 5, et pour EdgeBench, tableau 5 p. 9). Mêmes 25 jeux dans tous les bras ; aucune analyse appariée, aucun intervalle, aucun test. L'effet n'est pas uniforme : sur certains jeux la mémoire fait baisser le score (avec GPT-5.6 Terra, m0r0 passe de 71,8 à 8,8 et sb26 de 100 à 66,6 ; avec Claude Opus 4.8, sp80 passe de 47,6 à 4,8 ; tableau 4, p. 8).

**Q5. Des prédictions écrites avant l'essai ?**
Non trouvé dans les pages lues (1 à 26).

**Q6. Les essais rejetés ou échoués sont-ils gardés ?**
La réserve garde tous les harnais essayés et leurs essais, issues comprises (p. 4) ; l'annexe regarde quelles modifications sont gardées ou défaites (p. 13). Sur les jeux, le guide écrit par l'agent consigne des pistes déjà écartées (exemple p. 19).

**Q7. Quel modèle conçoit, quel modèle exécute ?**
Le même : exécutant, agent d'analyse des traces et agent de révision partagent le modèle (p. 3, p. 5 ; tableau 6, p. 12). Terminal-Bench : Claude Opus 4.6, GPT-5.4, GPT-5.4 mini. Jeux : Claude Opus 4.8, GPT-5.6 Terra, GPT-5.4 (p. 8).

**Q9. Objet du résultat, causalité.**
Le score de bancs. Les auteurs concluent que, sur Terminal-Bench, les gains de l'évolution du harnais tiennent pour l'essentiel au fait d'essayer plusieurs fois (p. 7). Le plan : même nombre d'essais, deux courses, pas d'intervalle. Ils regardent aussi les modifications elles-mêmes : beaucoup inscrivent dans la consigne ou la mémoire des faits propres à une tâche (ordre de commandes, propriétés d'un jeu de données) (p. 13-15). Ils donnent deux raisons possibles de l'absence de gain sur ce banc : scores déjà hauts, et peu de sensibilité au harnais (p. 7).

## Deux remarques de ce lecteur (à relire avant tout usage)

1. La même condition « un essai, harnais de départ » est rapportée deux fois, par deux séries de courses : 75,3 et 75,9 pour GPT-5.4, 59,4 et 56,9 pour GPT-5.4 mini, 69,9 deux fois pour Claude Opus 4.6 (tableaux 1 et 2, p. 6). L'écart entre deux mesures de la même chose atteint donc 2,5 points.
2. Sur 34 tâches tenues à l'écart, une tâche vaut 2,9 points (100 / 34) : les écarts du tableau 3 (+1,2 ; 0,0 ; −1,4) sont sous une tâche. Le tableau ne distingue pas « aucun gain » de « gain plus petit qu'une tâche ».

## Trois citations

1. « Does harness evolution yield generalizable improvements in harness design, or are its gains primarily due to repeated sampling? » (p. 2)
2. « In our cost estimation, we did not include the cost of modifying the harness. » (p. 13)
3. « The core issue is that most edits memorize fixes rather than distilling strategies. » (p. 14)

## Ce que ce papier occupe par rapport à notre question de l'héritage séparé de la tenue

- Il occupe la **tenue seule**, sans héritage : une mémoire écrite par l'agent pendant la course contre aucune, à nombre d'actions égal, sur le score de jeux (+16,0 et +4,8 points, nombre de courses non dit).
- Il occupe la **base à nombre d'essais égal** : dépenser les mêmes essais sur les tâches elles-mêmes fait aussi bien ou mieux que réviser le harnais, sur Terminal-Bench 2.1, K = 5, deux courses.
- Il ne transmet aucune mémoire à travers un changement et n'a aucun bras hérité ; son appariement ne porte ni sur les jetons ni sur les dollars.

## Réserves

1. Le nul sur tâches tenues à l'écart vaut pour cinq tours à un essai par tâche (dix dans l'annexe, un seul modèle) ; il ne dit rien d'un budget plus grand.
2. Version 4 lue ; les versions 1 à 3 n'ont pas été comparées.
3. Un seul lecteur ; aucune contre-lecture à ce jour.
