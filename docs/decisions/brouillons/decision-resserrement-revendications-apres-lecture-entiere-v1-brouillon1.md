# BROUILLON 1 — Resserrement des revendications 9, 14 et 12 (b) après la lecture entière de trois travaux — v1

- **Statut : brouillon, non contre-lu, sans numéro de décision.** Rien ici ne modifie une revendication : seul Lazar le fait. Tout « texte après » est une proposition, au conditionnel. Un contre-lecteur neuf d'un autre modèle doit le relire avant qu'il soit soumis.
- **Accord cité par le coordinateur** : `GO-2026-11-20-29`. Le rédacteur ne l'a pas vérifié dans `registres/go.md` (fichier hors de son périmètre de lecture) ; la mère le vérifie et inscrit le mot verbatim avant toute mise au propre.
- **Rédigé par** le lecteur des quatre travaux (Claude Fable 5.2), le 20 novembre 2026 vers 08:20 UTC.
- **Fondement** : `docs/notes/veille-organismes-ideation-v2/lecture-entiere-quatre-travaux-v1.md` (`65175e9121ff7db9332b8983eafc05fd164f389ea094a6d4f5daf0ffe8cf10c2`), elle-même non contre-lue. PDF empreintés, lus en entier : Terekhov et al., arXiv 2606.08892v3 (`8858355c…63b4beb`, 84 p.) ; Gideoni, Risi, Gal, arXiv 2602.16805v2 (`42514c0b…9a4b20913`, 21 p.) ; Zhang et al., arXiv 2607.26828v4 (`67028e61…9027d6549`, 28 p.). Aucun chiffre n'est opposable au-delà de ces lectures, page citée (R7).
- **Textes complétés, gardés tels quels (R12)** : `docs/notes/veille-exploration-idees-v1/revendications-v1.md` (`59c754ff…`), points 9, 12 (b) et 14 ; `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` (`b95688df…`), § 1 et § 2.

## 0. Portée

Ce texte **ne ferait que restreindre** ce que le programme présente comme sien. Il ne changerait aucune hypothèse, aucun critère de porte, aucun préenregistrement scellé. Rien n'y est déclaré « libre » : « non trouvé dans ce papier » ne dit rien des autres (R8). Il ne touche pas la revendication 8 : la lecture entière d'Escher-Loop n'y a rien trouvé à resserrer (note de lecture, section 3).

## 1. Revendication 9 — « le séquentiel doit battre le meilleur de N tirages indépendants, à budget égal »

**Constat.** Gideoni, Risi et Gal comparent des tirages indépendants et un séquentiel simple à des chaînes d'évolution de code, sous la même contrainte de budget, sur quatre domaines : « in all settings and under the same budget constraints, at least one of the baselines matches or exceeds a purpose-built code evolution pipeline » (p. 2). Ils emploient un témoin « vote majoritaire à k » (p. 7) et trouvent que toutes les méthodes de recherche font moins bien que lui sur le test (légende de la figure 3, p. 6). Ils mesurent le bruit d'évaluation avant de sélectionner (figure 4 et texte, p. 7). Ils dimensionnent le témoin par le coût moyen mesuré d'un tirage et calculent le meilleur de k parmi n par une formule exacte rapportée à Chen et al. 2021 (p. 15-16). Leur part tenue à l'écart est une autre année du même concours (p. 6-7), non une famille. Le test A/A n'y est pas nommé.

**1.1 Les gardes de la porte.**
- *Avant* (N-073, § 2) : « Les gardes de la porte (familles tenues à l'écart, témoin « un modèle, vote à k ») sont **très probablement prises aussi**, d'après des notices seulement (Wang et al., arXiv 2607.12227 ; Gideoni, Risi, Gal, arXiv 2602.16805 ; Jwalapuram et al., arXiv 2606.13003 ; Pan Li, arXiv 2607.04108) : à lire sur PDF avant toute phrase publique, Gideoni et al. et Wang et al. d'abord. »
- *Après (proposé)* : « Le témoin "un modèle, vote à k" est pris (Gideoni, Risi, Gal, p. 6-7), avec un coût apparié en nombre d'appels par question (p. 19) et non en jetons ; la mesure du bruit d'évaluation avant sélection est prise dans son principe (p. 7). Ne seraient plus décrits, sans être dits nouveaux ni propres, que deux éléments non trouvés dans ce papier : la lecture sur des **familles** tenues à l'écart et le **test A/A** avant la comparaison. Jwalapuram et al. et Pan Li resteraient à lire sur PDF ; Wang et al. resterait à relire sur ce point précis. »
- *Pages* : p. 6-7, p. 19.

**1.2 Les lignes gelées 2 et 6.**
- *Avant* (N-073, § 2) : « 2. *Taille du témoin* : N = budget du bras séquentiel divisé par le coût mesuré d'un tirage indépendant, et non le nombre de générations. » ; « 6. *Calcul* : espérance du meilleur de k parmi n graines journalisées par statistique d'ordre exacte […] ».
- *Après (proposé)* : mêmes lignes, inchangées dans ce qu'elles gèlent, suivies de « (pratique publiée : Gideoni, Risi, Gal, p. 15-16 ; formule d'après Chen et al. 2021, à lire sur source avant de la citer) ».
- *Pages* : p. 15-16.

**1.3 Citation obligatoire.** S'ajouterait, dans tout texte qui touche à la porte : Gideoni, Risi, Gal, « Simple Baselines are Competitive with Code Evolution », arXiv 2602.16805. Avec sa borne : une seule course de la chaîne comparée par problème mathématique (p. 4) ; ampleurs non comparées (p. 21). Et avec sa nuance : le séquentiel simple, sans sélection par la note (p. 3), égale ou dépasse la chaîne sur 6 problèmes sur 9 contre 4 sur 9 pour les tirages indépendants (p. 5), et sur 6 compétitions sur 10 contre 2 sur 10 (tableau 2, p. 8).

**1.4 Réserve sur l'antériorité.** Le PDF lu est la version 2, datée du 12 octobre 2026 (tampon, p. 1). La date de la version 1 (18 février 2026) vient de la veille, d'après la page arXiv ; elle n'est sur aucun PDF empreinté. Les expériences de la version 1 n'ont pas été lues : on ne sait pas lesquelles des pages citées ici y figuraient déjà. **Tant que la version 1 n'est pas téléchargée, empreintée et lue**, aucun texte ne devrait écrire que ce travail précède Oved et al. (13 octobre 2026) ; la phrase permise serait « Gideoni, Risi et Gal (version 2 du 12 octobre 2026) ». Cette réserve ne change rien au resserrement : le protocole est occupé dans les deux ordres.

## 2. Revendication 14 — juges de la recherche automatisée sous attaque

**Constat.** Terekhov et al. opposent à un juge-modèle de propositions de recherche un proposeur fort dont la consigne est optimisée pour le tromper. L'attaque « relies on knowledge of the blue team strategy » (p. 3) : l'optimiseur reçoit la liste des dix critères du juge (p. 6, p. 23, p. 41) et les notes rendues, celles du juge faible et celles de la vérité approchée (p. 41-43). Sans les critères, « it cannot discover effective attack strategies » (p. 23). Trois juges (le même modèle faible sous trois consignes) sont attaqués chacun par une attaque refaite, et le résultat est une frontière continue (p. 6, p. 7, p. 25-26). La vérité est un juge-modèle qui lit l'article (p. 3), non validé contre des personnes (p. 10). Les notes sont toujours rendues ; aucun juge n'est statistique.

**2.1 La forme de l'attaque.**
- *Avant* (revendications-v1, point 14) : « Forme encore revendiquée de l'attaque : mesure, sur des mondes où toute promotion est fausse, d'un juge statistique face à un proposeur modèle de langue chargé de le tromper, qui lit la description exacte du juge, libre dans ses propositions, avec un bras qui reçoit les verdicts et un bras qui ne les reçoit pas ; la partie « verdicts servis, mondes négatifs, zéro promotion » est cédée à CONFIRM. »
- *Après (proposé)* : « Suivant Terekhov et al. (2026), qui opposent à un juge-modèle de propositions de recherche un proposeur fort à consigne optimisée, informé des critères du juge et servi en notes, et qui mesurent par ablation ce que cette information apporte (p. 3, 6, 23), nous mesurerions la même attaque contre un **juge statistique**, sur des **mondes plantés où toute promotion est fausse** — la vérité étant celle du monde et non celle d'un juge-modèle —, avec **un bras qui reçoit les verdicts et un bras qui ne les reçoit pas**. La partie « verdicts servis, mondes négatifs, zéro promotion » resterait cédée à CONFIRM. Le proposeur chargé de tromper, informé du juge et libre dans ses propositions ne serait plus présenté comme ce qui distingue la forme. »
- *Pages* : p. 3, 6, 23, 41-43 ; p. 3 et 10 pour la vérité.
- *Point à trancher par Lazar* : ce qui reste est la réunion de trois éléments dont le troisième voisine la partie déjà cédée à CONFIRM. Le rédacteur n'a pas lu CONFIRM et ne peut pas dire ce que cette réunion laisse.

**2.2 Les deux juges sous la même attaque.**
- *Avant* : « un juge statistique et un juge-tournoi génératif à la manière de Co-Scientist sont mesurés sous la même attaque par les seules notes rendues (forme du résultat : gain continu comparé des deux juges). »
- *Après (proposé)* : même phrase, suivie de « La comparaison de plusieurs juges sous une attaque refaite contre chacun, en résultat continu, est pratiquée pour des juges-modèles (Terekhov et al., p. 6, 7, 25-26) ; ce que nous décririons est la paire comparée, un juge statistique contre un juge génératif. »
- *Pages* : p. 6, 7, 25-26.

**2.3 Précédents et citations.** *Avant* : « Précédents cités de la prémisse du bras « juge génératif » : 2611.04556 et 2611.00643. » *Après (proposé)* : s'y ajouterait Terekhov et al., arXiv 2606.08892 (tableau de la figure 1, p. 2 ; p. 5), qui entrerait aussi dans les citations obligatoires de tout texte présentant l'attaque. Wang, Arcuschin, Conmy, arXiv 2602.15222, que les auteurs disent leur voisin le plus proche (p. 10), serait à lire sur source avant tout texte qui en parle.

**2.4 Hors de ce brouillon.** Le même papier écarte la détection au profit de l'entraînement contre les menaces diffuses (p. 2, p. 9). Cela touche les papiers du programme sur les sondes, non la revendication 14 ; voir `docs/notes/veille-organismes-ideation-v2/note-entretien-controle-diffus-v1.md`. Aucune proposition ici.

## 3. Revendication 12 (b) — composition apprise, coût dans le signal

**Constat.** CostAda crédite chaque pas d'une recherche par son progrès divisé par un facteur du coût réalisé et du budget dépensé (équation 1, p. 5), pour que coût et budget restant « shape the search rather than serving only as accounting variables or a stopping rule » (p. 1) ; il alloue le budget entre lignes de recherche par une règle à borne de confiance sur ce crédit (p. 6). Le contrôleur est à constantes fixes (p. 15, p. 17), court avec un seul modèle par réglage (p. 7, p. 20-21), deux lignes de recherche (p. 17), et exclut l'évaluateur du coût (p. 3, p. 20).

**3.1 Le coût dans le signal.**
- *Avant* (revendications-v1, point 12 b) : « La composition est une variable apprise : nombre de parties, rôles, modèle par rôle (frontière ou instrument local), règle d'agrégation, mémoire transmise, part de budget ; le coût entre dans le signal rendu ; la nécessité de la frontière est une sortie mesurée ».
- *Après (proposé)* : « La composition serait une variable apprise : nombre de parties, rôles, modèle par rôle (frontière ou instrument local), règle d'agrégation, mémoire transmise, part de budget. Suivant Zhang et al. (2026, CostAda), qui créditent chaque pas d'une recherche par son progrès rapporté au coût réalisé et au budget restant et répartissent le budget entre lignes de recherche sur ce crédit (p. 5-6), le coût entrerait dans le signal rendu ; ce que nous décririons est l'objet de ce signal — la composition de l'organisme, apprise —, non le principe. La nécessité de la frontière resterait une sortie mesurée. »
- *Pages* : p. 1, 5, 6 ; p. 7, 15, 17 pour ce que le papier ne fait pas.

**3.2 Même mot dans la lettre de l'énoncé 5.**
- *Avant* (N-073, § 1, lettre retenue) : « […] et à un concepteur entraîné plutôt que sélectionné, avec le coût dans le signal. »
- *Après (proposé)* : « […] et à un concepteur entraîné plutôt que sélectionné, avec le coût dans le signal, à la manière dont Zhang et al. (2026) le font entrer dans le crédit d'un contrôleur de recherche. »
- *Page* : p. 5.

**3.3 Ce qui n'est pas resserré, et pourquoi.** « Composition apprise », « modèle par rôle » et « nécessité de la frontière mesurée » ne sont pas dans CostAda. Ils ne sont pas pour autant dits libres : CostAda cite des travaux qui choisissent ensemble modèles et budgets (Liu et al., arXiv 2511.17006 ; Wang et al., AgentTTS ; p. 3) et un système multi-agents sous budget (BAMAS, p. 12), et la veille en nomme d'autres (ligne A13) ; aucun n'est lu. Ils seraient à lire sur source avant toute phrase publique sur la composition apprise sous coût. Citation obligatoire proposée pour tout texte qui touche à 12 (b) : Zhang et al., arXiv 2607.26828.

## 4. Ne pas écrire (proposé, pour tout texte sortant)

- « le séquentiel contre le meilleur de N à budget égal » comme idée du programme (déjà dans N-073) ; « le témoin vote à k », « le pilote de bruit », « dimensionner le témoin par le coût mesuré d'un tirage », « le meilleur de k parmi n par formule exacte » comme apports ;
- « Gideoni, Risi et Gal précèdent Oved et al. », « dès février 2026 », tant que la version 1 n'est pas lue sur PDF empreinté ;
- « les témoins simples battent l'évolution de code » sans « au moins un des deux, selon le domaine » (p. 2) ; « les tirages indépendants suffisent » (4 sur 9 et 2 sur 10, p. 5 et p. 8) ;
- « personne n'a tenu des familles à l'écart », « personne ne fait de test A/A » (non trouvé dans un papier ; trois notices non lues) ;
- « un proposeur chargé de tromper un juge », « un attaquant qui lit la description du juge », « libre dans ses propositions », « comparer des juges sous la même attaque », « un résultat continu plutôt qu'un taux » comme ce qui distingue notre attaque ;
- « Terekhov et al. servent la description exacte du juge » (c'est la liste des dix critères, p. 23 et 41) ; « leur attaquant ne voit que les notes du juge » (il voit aussi la note de vérité, p. 41) ;
- « leur vérité est fausse » ou « invalide » (elle est non validée contre des personnes, p. 10) ; « leur juge durci est robuste » sans « contre leur attaque » (p. 7-8, p. 10) ;
- « premier juge statistique attaqué », « zone libre », pour ce qui reste de la revendication 14 ;
- « faire entrer le coût dans le signal » comme idée du programme ; « CostAda apprend » (constantes fixes, p. 15) ; « CostAda choisit le modèle par rôle » (un modèle par réglage, p. 7) ; « CostAda compte le coût du juge » (évaluateur exclu, p. 3) ;
- « personne n'apprend la composition sous coût » (voisins nommés, non lus) ;
- tout chiffre de ces trois papiers sans sa page, et tout chiffre calculé par un lecteur présenté comme chiffre des auteurs.

## 5. Ce que ce brouillon ne ferait pas

- Aucune dépense, aucun changement de préenregistrement, aucune déclaration « libre », aucun numéro de décision.
- Il ne lit ni la version 1 de Gideoni et al., ni CONFIRM, ni les voisins nommés ; il les désigne.
- Il ne dit rien des revendications 7 et 8, sinon ceci : la note de lecture signale, pour la 7, un indice contraire borné tiré d'Escher-Loop (p. 6 ; tableau 1, p. 7), que Lazar pourrait vouloir voir cité.
