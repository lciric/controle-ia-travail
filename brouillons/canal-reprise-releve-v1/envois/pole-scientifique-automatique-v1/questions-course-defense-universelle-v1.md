# Sept questions pour entrer dans la course en nous distinguant — proposition au programme — v1

Lignée conv-audit, 28 octobre 2026, 12:35 UTC (`date -u`). **Proposition**, pas modification du programme : conv-audit
propose, Lazar décide (interdit « modifier le programme »). Sur le mot de Lazar (13:32 heure de Paris) : « je veux traiter
les 7 questions, verse le dans le prog ». Versé ici dans la branche `canal/conv-audit-n04` ; le pliage dans le programme
qui fait foi (`docs/programme-controle-ia-v2.md`, sur `main`) est à faire par session-depot sur décision de Lazar.

**Cadre.** Les recherches d'antériorité (versées : `anteriorite-universalite-metriques-v1.md`,
`anteriorite-coevolution-et-boite-blanche-v1.md`) ont montré deux choses : la course aux armements co-évolutive est
**partiellement occupée** (SafeCoEvo l'occupant le plus proche), et la croyance « la boîte blanche seule fait notre
originalité » est **réfutée**. Ce qui nous distingue n'est donc pas une astuce à ajouter : c'est la **contrainte que nous
portons déjà** — nous **ne construisons pas d'attaquant qui tourne librement** (R-597, R-611). Tous les occupants le
construisent. Ce refus nous **force** trois choses qu'aucun ne fait : fournir les angles morts **par la théorie**, tenir
le juge **figé et garanti**, et faire de la **boucle elle-même** l'objet mesuré. Les sept questions en sortent. Toutes
sont **défensives et au niveau méthode** ; aucune ne demande de produire une recette d'attaque.

**Statut R7/R8.** Les jugements « ouvert / occupé » viennent des antériorités (RAPPORTÉ, non vérifié sur PDF). Toute zone
dite ouverte est une **zone séduisante** : à vérifier plus durement sur PDF avant toute revendication (R8).

---

## Les sept questions

**Q1 — L'approvisionnement théorique bat-il l'approvisionnement empirique pour la généralisation ?**
Une défense co-évoluée contre des **conditions prédites** (dérivées des hypothèses statistiques des moniteurs) généralise-
t-elle *mieux* à des familles tenues à l'écart qu'une défense co-évoluée contre un adversaire qui tourne ? Intuition : un
adversaire empirique surajuste à sa propre distribution ; une condition prédite est sans distribution. Deux bras,
falsifiable, **sans construire d'attaque**. *Distinction :* les occupants n'ont que l'approvisionnement empirique.
*Prérequis :* l'expérience-pont (Q-pont ci-dessous). *Traçabilité :* haute (processeur).

**Q2 — Le juge figé et garanti empêche-t-il l'effondrement de Goodhart quand la défense évolue ?**
Que doit-on tenir fixe pour que la mesure reste valide pendant que la défense évolue ? Les occupants laissent l'évaluateur
dériver (un modèle, ou une validation en-distribution). Nous avons un juge figé avec borne de fausses promotions démontrée
(inférence universelle, inégalité de Ville). Bras : co-évolution sous juge figé garanti **contre** sous juge-modèle qui
co-évolue — mesurer la généralisation tenue à l'écart et le taux de fausses « améliorations ». *Distinction :*
contribution sur l'**évaluateur**, que personne n'adresse. *Traçabilité :* haute.

**Q3 — Peut-on prédire ses propres angles morts avant de les rencontrer ?**
Le pôle théorie (vérificateur Lean) prédit-il, **avant le test**, **sur quelle famille tenue à l'écart une défense évoluée
donnée va échouer**, à un taux au-dessus du hasard ? Prédictions par famille préenregistrées, lues une fois. *Distinction :*
la plus forte et la plus neuve — « une défense qui connaît ses limites avant d'être attaquée » ; c'est le but dit par
Lazar (prédire plutôt que rencontrer par hasard) rendu falsifiable. *Traçabilité :* la plus difficile (demande le pôle
théorie mûr). 

**Q4 — Le diffus est-il un axe de généralisation à part ?**
Une défense qui généralise sur des menaces **par épisode** transfère-t-elle au **diffus** (réparti entre épisodes), ou le
diffus est-il un axe fondamentalement séparé ? Notre lemme du plafond d'horizon suggère qu'il est séparé. *Distinction :*
les deux papiers « notre cadre exact » (tâches floues ; attaques distribuées) sont 100 % boîte noire et n'évoluent pas.
*Traçabilité :* moyenne (demande la banque de la couche 2 dimensionnée).

**Q5 — L'universalité de la *boucle*, pas du moniteur.**
Devant une famille toute neuve, combien de générations et de budget la boucle met-elle à produire une défense qui
généralise — et ce coût **baisse-t-il** de famille en famille (la boucle apprend-elle à défendre) ? *Distinction :* les
occupants évaluent le moniteur final ; nous évaluons le **générateur** de moniteurs — « la machine est la contribution »
rendu falsifiable (héritage récompensé de N-045 en courbe d'apprentissage). *Traçabilité :* moyenne.

**Q6 — Co-évolution contrôlée pour l'artefact de source.**
Une défense « généralise »-t-elle en détectant le **sabotage**, ou l'**artefact du générateur** de la famille ? (Le papier
LODO montre que des bancs sont séparables par le seul artefact de source ; aucun travail de co-évolution ne le contrôle.)
Protocole de co-évolution **contrôlé pour l'artefact**, avec le bras « fuite textuelle » de N-053. *Distinction :*
différenciateur de **rigueur** — exactement ce qu'un relecteur sérieux cherche. *Traçabilité :* haute.

**Q7 — Le mélange des canaux co-évolue-t-il ?**
Le mélange boîte blanche / boîte noire co-évolue-t-il, et l'avantage de la boîte blanche **grandit-il ou s'inverse-t-il**
au fil des générations ? *Distinction :* dynamique, jamais posée, mais moins distante de l'occupé (le joint statique est
déjà fait trois fois). *Traçabilité :* moyenne (demande la composition apprise de N-045).

**Q-pont (préalable transversal, gratuit) — les épisodes synthétiques prédisent-ils le réel ?**
Des épisodes synthétiques portant une propriété P (corrélation, effet d'épisode) prédisent-ils les taux de détection sur
des épisodes **réels** portant P ? Si oui, la théorie devient un **générateur d'angles morts validé** — abondant, sûr — et
Q1, Q3, Q5 reposent dessus. Si non, la voie synthétique est cosmétique. Sur processeur, décisif, préenregistrable.
**À traiter en premier.**

## Ce que l'organisme doit gagner pour traiter ces questions (première passe — à compléter par la nouvelle instance)

Besoin commun à presque toutes : l'organisme doit faire **évoluer des moniteurs** (pas seulement des fiches d'hypothèses)
— c'est la **couche 3** (« moniteurs neufs à la demande ») plus la **réécriture de soi restreinte sous bac à sable**
(noyau, gardes, bornes jamais réécrits ; C-17 l'avait retirée, à reconcevoir). Plus la machinerie **familles tenues à
l'écart** (N-044) avec le protocole de **rotation** (leave-one-category-out) et le **rapport par famille** (normalisation
de la robustesse aux attaques non prévues, jamais la moyenne). Plus la **troisième instance** pour la séparation de
quarantaine (qui fait évoluer les moniteurs ≠ qui conçoit le mode tenu à l'écart ≠ qui juge).

Par question : **Q1, Q3, Q5** demandent la voie (i) (épisodes synthétiques depuis des conditions prédites) câblée au pôle
théorie, et dépendent de Q-pont. **Q2** demande un bras d'ablation juge-figé-garanti contre juge-modèle, et l'invariant
« aucun score de moniteur dans l'entraînement » tenu (N-053). **Q3** demande le pôle théorie (Lean) produisant des
prédictions d'échec **par famille**, préenregistrées (la carte des hypothèses opérationnalisée). **Q4** demande le
moniteur séquentiel/diffus et le lemme du plafond d'horizon câblés à la taxonomie des familles, familles diffus vs
par-épisode tenues à l'écart. **Q6** demande des familles bâties **sans** différence d'artefact de source, et le bras
« fuite textuelle » (N-053) en contrôle. **Q7** demande la composition apprise (N-045) traitant le mélange des canaux
comme variable apprise suivie au fil des générations.

## Réserves

1. Toutes les zones dites « ouvertes » sont **à vérifier sur PDF** (R8) ; la plus exposée est Q3 (prédire ses angles
   morts), à vérifier le plus durement.
2. Choisir parmi ces questions, ou en faire l'énoncé central, est une **modification de revendication → nœud → GO de
   Lazar**. Cette proposition ne tranche rien.
3. Aucune ne demande de produire une recette d'attaque ; Q1/Q3/Q5 n'avancent que si Q-pont tient, et restent au niveau
   méthode (conditions mesurables, pas trajectoires).
