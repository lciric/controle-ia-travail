# Réponse de conv-audit à la question 3 (fertilité d'un croisement, transition de phase, essaims) — version 2

- Version 2, 31 octobre 2026, 01:25 à 02:10 heure UTC, sous-agent neuf Opus 5.5 (lignée conv-audit), auteur ni de la v1, ni des relectures, ni de la synthèse. La v1 reste intacte ; erreurs dans `erratum-reponses-v1-v1.md`.
- Niveau méthode ; aucune décision. Statuts comme en réponse 1 v2.
- Décision proposée n° 4 de la synthèse appliquée ici **comme règle de rédaction, non comme décision** : « transition de phase » est une **hypothèse suspendue jusqu'à E2′** ; le pic de variance d'une issue binaire n'est **pas** une signature de criticité.
- Pièces intégrées (sha256sum) :
  - `question-3-fertilite-v1.md` — `2ad43f6972951abb90ae49447fd887d5f65d3dacb552ca7454ca2c0c5027b06a`
  - `reponse-conv-audit-question-3-v1.md` — `c7ca393513ed1ffd443f622f8ee8eb64d7766cbc34a177c3a64d61b3f80f4f47`
  - `relecture-fable-reponse-3-v1.md` — `556bc9d5f7eb12ef12b4ba2b284eb2ef5fd52acac815a0b0ff26489264e04129`
  - `reponse-fable-independante-question-3-v1.md` — `ddbf079eeb7b64df7954fea335b6dd9d4738fd79404b4f05088b7b80b3be40d9`
  - `revue-biblio-fertilite-v1.md` — `307b4f2fe6e53dcfa517c6da5d2591a6cee1e1508cd8197f4778fe014d6b718f`
  - `construction-essaim-et-722-v1.md` — `32846cff77abb3391d899f0f9f9f5a748c2c3890ff361809c02d3767d3e98b8d`
  - réponse d'Argon (commit `b1a21a07`) — `c2a991060f0ef87887e97e482009a754121ce29415d1f2a2159df24d35159ed7` ; `lecture-reponse-argon-bisociation-v1.md` — `3271d0e25cafa6a5df048547249debf958bd9a830c0099afd38cac4a88de8b96`
  - synthèse v2 du collisionneur — `23c2888ddd924b85a0bbd0009a17f64723399d69ffd17669f56c4fddf7d18a86`
  - `docs/sources/pdf/bisociation-fertilite-v1/PROVENANCE-bettencourt-v1.md` — `ab654a87f9aebd8baad5927d2959255f52f76d47f4933353921ca115756c7533`
  - `docs/sources/pdf/bisociation-fertilite-v1/arxiv-1504.00319-bettencourt-kaiser-2015.pdf` — `2fb9aab049631cdffe59631ce5196b800220dbeb584afd179ce8e6623485a523` (8 pages ; texte intégral extrait par `pdftotext` page par page et cherché ; pages 1, 3, 5, 6, 7 lues aux passages cités, références de la page 8 lues)
  - `docs/sources/pdf/bisociation-fertilite-v1/bettencourt-cintron-arias-kaiser-castillo-chavez-2006-power-good-idea-arxiv-physics-0502067v3.pdf` — `ec3cef8e362ae0c833cd5f84c93a16821c185e3598944b9a1e219fdb3bdfd352` (recherche plein texte et lecture des pages 12 et 15)
  - `docs/sources/pdf/bisociation-fertilite-v1/arxiv-2402.08640-gu-krenn-2024.pdf` (empreinte vérifiée par son compagnon ; page 1 lue)
  - `registres/decisions.md`, lignes R-616, R-648, R-669.

## Réponse courte

La fertilité se **définit avant de se calculer** en séparant trois objets : la fertilité **d'une paire** mesurée après coup (reprise par des tiers hors des deux niches, à horizon gelé), son **prédicteur** avant coup (déjà estimé par Gu et Krenn 2024 sur des paires de concepts), et le **rendement d'un processus** (essaim, modèle unique). Elle dépend du quadruplet paire, procédé, budget, juge : « propriété de la paire » reste une HYPOTHÈSE. « Transition de phase » est **suspendue jusqu'à E2′** ; ce qui est mesuré dans la littérature, ce sont des cloches ou des monotones pour la paire, et une transition de percolation pour la **structure sociale** d'un champ (Bettencourt et Kaiser 2015), pas un « allumage ». Les essaims n'ont d'argument que s'ils battent le meilleur de N agents indépendants à calcul égal.

## Ce qui change par rapport à la v1

| Constat | Sort | Correction |
|---|---|---|
| RL3-01 Gu et Krenn 2024 (arXiv 2402.08640) manqué ; la zone « P(reprise | paire) » est largement occupée | accepté | Référence à battre ; **vérifié sur PDF** (p. 1 : plus de 21 millions d'articles, aire sous la courbe « au-delà de 0,9 pour la plupart des expériences »). Ce qui reste peut-être libre : courbe entière avec test de non-linéarité, reprise traversante, niches comme unités. |
| RL3-02 cloche et seuil confondus ; « bord du chaos » non nommé | accepté | Deux hypothèses distinctes, deux morts (section 3). |
| RL3-03 marques de transition non discriminantes | accepté | Trois cadres séparés, tests de criticité standard, alternatives nommées (section 3). |
| RL3-04 « densité → cloche » présentée comme neuve | accepté | Déjà simulée (Lazer-Friedman 2007, Fang-Lee-Schilling 2010), observée (Derex-Boyd 2016), contredite (Mason-Watts 2012). Reste à tester : unité « niche », agents de langage, reprise plutôt que performance. |
| RL3-05 reformulation sans chiffre | accepté | Critère de mort chiffré ci-dessous. |
| RL3-06 moyenne contre queue | accepté | Le bisociateur filtre : il vise la queue ; le seuil k de la cascade est fixé d'après la distribution des témoins. |
| RL3-07 paire et processus remélangés ; paires sans contact hors du support | accepté | Deux quantités, deux protocoles ; extrapolation déclarée ; confusions du ponteur (taille d'équipe, position, revue) contrôlées. |
| RL3-08 « nos courses » rangées hors de nous ; « cinq traditions qui s'ignorent » | accepté | Retiré ; traditions qui se citent en partie. |
| RL3-09 convergence des essaims déjà mesurée | accepté | Lorenz 2011, Doshi-Hauser 2024, Ashery-Aiello-Baronchelli 2025 cités (section 4). |
| RL3-10 non-linéarités mesurées ignorées ; fertilité constante dans le temps | accepté | Dépendance au temps (maturité, découvertes multiples) ajoutée (section 1). |
| RL3-11 « Bettencourt allumage » introuvable ; « brevets (Uzzi) » ; Servedio omis ; « statistique d'ordre » | accepté **en partie** | Le mot est bien absent (vérifié sur les PDF, section 5) ; mais un seuil existe dans cette famille : R₀ > 1 (2006) et un seuil de connectivité de percolation (2015). Uzzi 2013 porte sur des articles ; Tria, Loreto, Servedio, Strogatz ; « paramètre d'ordre ». |
| RL3-12 l'inventaire des antériorités est demandé, pas « non demandé » | accepté | Section Antériorités. |
| RL3-13 définition avant coup et biais du juge manquants | accepté | Section 1 ; biais contre la nouveauté du juge figé (Wang-Veugelers-Stephan 2017) à tester. |
| RL3-14 paysage de forme NK sur recombinaisons déjà mesuré | accepté | Fleming et Sorenson 2001 (notice). |
| Synthèse : pic de variance p(1−p) pris pour criticité (A, C, D) | accepté | Retiré comme signature. |
| Synthèse : sur-additivité F faussée par le budget et la combinatoire | accepté | F n'est gardée qu'à budget et nombre de prémisses constants, avec témoin d'union aléatoire (section 2). |

## 1. Définir la fertilité avant de la calculer

- **Après coup (la mesure)** : probabilité qu'un contact entre deux niches produise au moins une **reprise par un tiers hors des deux niches** dans un horizon h gelé. Proposé, à geler : h ≥ 4 ans sur la littérature réelle, parce que les articles très nouveaux sont moins souvent très cités sous trois ans (Wang, Veugelers, Stephan, document NBER, p. 15, pages citées par la revue v1). L'étiquette ne doit pas être une citation croisée (défaut A0 et circularité, synthèse, A).
- **Avant coup (le prédicteur)** : structure partagée (Gentner 1983, SUPPOSÉ), propension sous plongement (Shi-Evans 2023), classifieur de Gu-Krenn 2024. On teste l'avant-coup contre l'après-coup, jamais l'inverse : sinon le prédicteur devient la définition (réponse Fable indépendante 3).
- **Rendement d'un processus** : survivantes aux tests de mort par unité de budget, dans nos courses. Ce n'est pas une fertilité de paire ; la reprise par nos propres juges n'est pas une reprise par des tiers.
- **Fonctionnel** : moyenne, variance ou quantile ne classent pas les paires dans le même ordre (Fleming 2001 : la distance baisse la moyenne et élève la variance ; revue v1, pages citées). Le bisociateur filtre : il vise la queue.
- **Temps** : une paire peut être stérile à une date et mûre plus tard ; les découvertes multiples indépendantes dans une fenêtre courte sont un observable de maturité (Merton 1961, notice ; Li, Lin, Wu 2025, page en ligne).

La **sur-additivité** proposée par la réponse Fable 3, F(A, B) = R(A ∪ B) − R(A) − R(B) + R(A ∩ B), a trois défauts relevés au collisionneur : elle mesure l'allocation du budget (T2-A, T2-C), elle peut être vraie par construction combinatoire (T2-D), et son contrôle par copie renommée n'a pas d'issue sûre (négative selon C, positive par double comptage selon A). Trois corrections différentes existent (A : unions aléatoires appariées ; C : budget et prémisses constants plus union aléatoire ; D : fertilité structurelle séparée de l'avantage de processus) ; aucune définition commune. À choisir au préenregistrement, en mondes inventés seulement.

## 2. Ce que mesure la littérature

- Distance et succès : **cloche** chez Uzzi 2013 (renversement après le 85e à 95e percentile de conventionnalité) et Yegros-Yegros 2015 (SUPPOSÉ) ; **monotone** croissante chez Shi-Evans 2023 ; **contre** la distance pour l'intérêt jugé chez Gu-Krenn (arXiv 2405.17044) ; pour la variance chez Fleming 2001 (revue v1, section 2).
- Densité de contacts : cloche en simulation et en expérience, contredite par Mason-Watts 2012.
- **Aucune** source lue ne rapporte une transition de phase dans la probabilité qu'une paire produise une idée reprise (revue, section 5 ; synthèse, B : « jamais sur P(reprise | paire) », A, B, C).

## 3. La transition de phase : hypothèse suspendue

- **Cloche lisse** et **criticité** sont deux hypothèses. La première n'exige aucune transition. La seconde (fertilité maximale au voisinage d'un seuil, hypothèse du « bord du chaos », SUPPOSÉ) exige un paramètre d'ordre, un paramètre de contrôle, une susceptibilité qui croît avec la taille et des exposants reliés.
- Trois cadres à ne pas mêler (relecture 3) : avalanches en loi de puissance (criticité auto-organisée) ; signaux précoces (variance et autocorrélation avant une bifurcation de basse dimension) ; seuil de percolation (statique).
- **Ce qui ne prouve rien** : une loi de puissance seule (elle existe sans criticité : attachement préférentiel) ; le pic de variance d'une issue binaire, qui culmine à p = 0,5 quelle que soit la courbe (trouvé séparément par A, C, D au collisionneur) ; le « ralentissement critique » d'Argon, qui se confond avec l'indécidabilité (T1-C a3) ; une sortie sigmoïde de modèle (relecture 4).
- **Ce qui compterait** : effondrement des courbes à plusieurs tailles ; relation entre exposants de taille et de durée des cascades ; rapport de branchement d'un processus auto-excité proche de 1 ; contre des alternatives log-normale et sous-critique. La signature de variance retenue n'est pas commune au collisionneur : surdispersion entre réplicats φ = variance observée / variance binomiale (C, D) ou variance au-dessus d'un nul d'urne de Tria à moyenne égale (A).
- **Littérature réelle** : la taille n'y est pas identifiable selon A ; B garde les tests à partir de cinq tailles ; C et D restent en mondes inventés. La synthèse propose (décision n° 4) la suspension jusqu'à E2′, puis le retrait si E2′ échoue ; c'est un **nœud** de Lazar (énoncé de son hypothèse), non tranché ici.

## 4. Les essaims

- L'argument a un contenu seulement si l'essaim bat, à calcul égal, le **meilleur de N agents indépendants** et un agent unique à budget N fois plus grand, et s'il **perd son avantage quand on coupe les messages** (réponse Fable 3, section 3c).
- Le risque inverse est documenté : l'influence sociale réduit la diversité (Lorenz et collègues 2011, notice) ; des populations d'agents de langage convergent vers des conventions et une minorité engagée fait basculer la majorité (Ashery, Aiello, Baronchelli 2025, page arXiv, relecture 3) ; la génération assistée réduit la diversité collective (Doshi et Hauser 2024, notice).
- Les annonces de 2026 ne publient aucune mesure d'émergence, de diversité ou d'ablation (revue 2.7 ; construction 1.4 ; Kimi A7).
- Un système fini n'a pas de transition, seulement un croisement : sans balayage en taille, « émergence » reste un mot (relecture 3, point c6 ; Schaeffer et collègues 2023, SUPPOSÉ).

## 5. Ce que dit vraiment Bettencourt et Kaiser 2015 (arXiv 1504.00319) sur l'« allumage »

Texte intégral extrait et cherché (8 pages ; pages du fichier PDF = pagination arXiv) ; passages cités lus en contexte.

- **« Ignition » : zéro occurrence** dans le texte intégral (recherche plein texte). **Aucune mention de R₀, de nombre de reproduction, ni d'« auto-entretien »** (« self-sustain » : zéro).
- **« Threshold » : deux occurrences**, toutes deux pour un seuil de **connectivité du réseau de coauteurs** :
  - p. 3 : « fields with α > 1 might percolate when their average degree, ⟨k⟩, crosses some field-dependent critical threshold, k_c », en renvoyant à leur travail de 2009 ([16]) ; le paramètre critique est τ = ⟨k⟩/k_c − 1 (éq. 3) ;
  - p. 7 (conclusion) : les réseaux se densifient « until the average connectivity per author crosses a critical threshold. Near that critical point, scientific fields undergo a topological transition, akin to percolation ».
- **Ce que le papier affirme** : une **transition topologique** (apparition d'une composante géante contenant la plupart des auteurs, p. 1 résumé et p. 3) dans neuf champs, avec des exposants communs « suggestive evidence for universality » (p. 5) ; β/ν = 0,46 (intervalle à 95 % [0,22 ; 0,69]) et γ/ν = 0,19 ([0,12 ; 0,25]) en figure 3 (p. 5) ; meilleur ajustement ν ≃ 1,125, β/ν = 0,44, γ/ν = 0,12, dimension effective d ≃ 1 (légende de la figure 5, p. 6). Les auteurs reconnaissent une mise à l'échelle « limited and noisy » en τ pour la plupart des champs (p. 5).
- **Ce qu'il interprète** : la transition « signale une étape importante » : un champ distinct semble émerger quand existe un ensemble partagé de questions, concepts et méthodes ; elle « pourrait fournir un signal » qu'un sujet devient un champ (p. 3). C'est prudent ; ce n'est pas « le moment exact où le champ devient autonome et auto-entretenu » écrit par Argon (section G).
- **Lien épidémique** : p. 6, rappel de leurs travaux antérieurs ([15] 2008, [20] 2006, [21] 2011) où l'arrivée d'auteurs est modélisée comme un processus de contact épidémique avec incubation ; rapprochement de leurs exposants avec ceux de processus de contact à interactions longues et de transitions vers un état absorbant (références [23], [24]). C'est une piste de micro-dynamique, pas un seuil d'allumage.
- **Où est le seuil R₀ > 1** : dans la prépublication de 2006 (arXiv physics/0502067v3, pagination arXiv), p. 12 (définition du nombre de reproduction de base) et p. 15 : « If R₀ = I(t_idea)/I(t₀) > 1 then the idea will spread » (vérifié sur PDF ; l'extraction perd la lettre « c », défaut d'encodage signalé par la provenance). C'est un seuil **d'invasion d'une idée** (diffusion des diagrammes de Feynman), pas d'allumage d'un champ. La « bistabilité » attribuée par Argon n'est **pas trouvée** par recherche plein texte dans cette prépublication (aucune occurrence de « bistab » ni « backward ») ; le papier de 2008 (*Scientometrics*) n'est pas versé (fermé) : non vérifiable ici.
- **Arbitrage** : la relecture 3 (R-616) avait raison sur le **mot** (absent) ; Argon a raison sur l'existence de **deux formalisations de seuil** dans cette famille (invasion R₀ > 1 en 2006, vérifiée ; seuil de percolation de la connectivité en 2015, vérifié) ; « allumage » reste une métaphore de Lazar. Le seuil de 2015 porte sur la **structure sociale** d'un champ, non sur la fertilité d'une paire.

## Convergences et divergences avec la réponse Fable indépendante 3

- **Convergent** : la fertilité dépend de (paire, procédé, budget, juge) ; définir l'après-coup avant le prédicteur ; rivales de forme gelées d'avance ; essaims contre meilleur-de-N et agent unique, avec ablation des messages ; un événement rare est non linéaire sans être critique.
- **Divergent** : Fable fait de la sur-additivité F la définition ; le collisionneur y a trouvé trois défauts (section 1) ; je la garde comme candidate en mondes inventés seulement. Fable retient « la variance culmine » comme signature (ii) : faux pour une issue binaire ; pour un compte, seulement au-dessus d'un nul à moyenne égale.
- **Argon** : « R₀ de la lignée issue du pont » comme fertilité après coup est une idée utile (nombre de travaux indépendants réutilisant la paire) ; ses signatures (susceptibilité, ralentissement critique, bimodalité) sont en partie réfutées au collisionneur (T1-C a3 ; pic binomial).

## Antériorités

| Auteur, année | Support | Statut |
|---|---|---|
| Gu et Krenn 2024 (2402.08640) | prépublication | **vérifié sur PDF**, p. 1 |
| Gu et Krenn 2024 (2405.17044) | prépublication | page en ligne (revue v1) |
| Bettencourt et Kaiser 2015 (1504.00319) | prépublication | **vérifié sur PDF**, p. 1, 3, 5, 6, 7 |
| Bettencourt, Cintrón-Arias, Kaiser, Castillo-Chávez 2006 | *Physica A* ; arXiv physics/0502067v3 | **vérifié sur PDF** (prépublication), p. 12 et 15 ; version de revue non lue |
| Bettencourt, Kaiser, Kaur 2009 | *Journal of Informetrics* | PDF versé (manuscrit d'auteur), non lu |
| Bettencourt et collègues 2008 | *Scientometrics* | notice seulement (non versé, fermé) |
| Ham, Bettencourt et collègues 2007 | *Journal of Computational Neuroscience* | notice seulement (Argon) |
| Weitzman 1998 | *Quarterly Journal of Economics* | PDF versé ; « fonction de succès », p. 345, citée par la revue v1, non relue ici |
| Simonton 2003 | *Psychological Bulletin* | manuscrit en ligne (revue v1) |
| Fleming 2001 ; Fleming et Sorenson 2001 | *Management Science* ; *Research Policy* | PDF versé pour 2001, pages citées par la revue v1 ; notice pour 2001b |
| Uzzi et collègues 2013 ; Wang, Veugelers, Stephan 2017 | *Science* ; NBER w22180 | PDF versés, pages citées par la revue v1, non relues ici |
| Shi et Evans 2023 ; Sourati et Evans 2023 | revues | page en ligne (revue v1) |
| Guimerà, Uzzi, Spiro, Amaral 2005 | *Science* | version avant publication en ligne (revue v1) |
| Tria, Loreto, Servedio, Strogatz 2014 | *Scientific Reports* | PDF versé, lu par la revue v1 en ligne |
| Lazer et Friedman 2007 ; Mason et Watts 2012 | revues | SUPPOSÉ |
| Fang, Lee, Schilling 2010 ; Derex et Boyd 2016 ; Ke et collègues 2015 | revues | PDF versés, chiffres cités par la revue v1, non relus ici |
| Chu et Evans 2021 ; Li, Lin, Wu 2025 | *PNAS* ; arXiv 2502.06190 | page en ligne (relecture 3) |
| Merton 1961 ; Lorenz et collègues 2011 ; Doshi et Hauser 2024 ; Crane et Sornette 2008 ; Touboul et Destexhe 2017 | revues | notice seulement |
| Ashery, Aiello, Baronchelli 2025 | arXiv 2410.08948 | page en ligne (relecture 3) |
| Clauset, Shalizi, Newman 2009 ; Scheffer et collègues 2009 ; Schaeffer et collègues 2023 ; Kauffman 1993 ; McMullin ; Kuhn 1977 | divers | SUPPOSÉ (McMullin : notice) |

## Critère de mort chiffré

Seuils **proposés, à geler** ; issus des cellules du collisionneur, illustratifs selon leurs auteurs (synthèse, iii).

1. **E2′, étalonnage des tests de criticité sur mondes plantés** (préalable à tout emploi du mot). Le mot « transition de phase » sort du préenregistrement si le test retenu n'atteint pas un taux de détection ≥ 0,9 avec fausses alertes ≤ 0,1 (A), ou, dans la variante de C, si sur 5 tailles couvrant deux décades et 50 réplicats on n'obtient pas φ > 2,0 au point critique et une erreur de superposition < 5 % sur une taille tenue à l'écart ; falsification si φ ≤ 1,2 (C).
2. **Si E2′ passe**, en mondes inventés ou en courses : l'hypothèse de criticité meurt si aucune des trois preuves n'est obtenue (effondrement par tailles, relation d'exposants, rapport de branchement proche de 1) ; reste alors « non-linéarité » (changement de pente avec intervalle de confiance).
3. **Cloche** : meurt si la courbe fertilité-distance estimée entière est monotone sur toute l'étendue, intervalle excluant un changement de signe de la pente (relecture 3).
4. **E6′, fertilité de paire au-delà de la popularité** : l'idée qu'une paire porte une fertilité propre, prédictible au-delà des tailles, meurt si le gain conditionnel au-dessus du modèle « popularité seule », dans la strate de distance supérieure à 3, n'est pas positif avec un intervalle excluant zéro (T3-A).
5. **Essaims** : voir la réponse 2 v2 (≥ 20 % sur le meilleur des témoins ; arrêt sous 50 survivantes par cellule).

## Ce qui reste ouvert

- La signature de variance (surdispersion entre réplicats ou excès sur nul d'urne) n'est pas choisie.
- La définition de la sur-additivité n'est pas commune ; aucune n'est sûre.
- Le papier Bettencourt 2008 n'est pas lisible ici ; la « bistabilité » reste non vérifiée.
- Le juge figé note à horizon zéro et peut reproduire le biais contre la nouveauté (Wang 2017) : test non fait.
- Décision n° 4 (retrait, maintien ou suspension du mot) : nœud de Lazar.
