# BROUILLON 2 — Resserrement des revendications 9, 14 et 12 (b) après la lecture entière de quatre travaux — v1

- **Statut : brouillon 2, sans numéro de décision.** Rien ici ne modifie une revendication : seul Lazar le fait. Tout « texte après » est une proposition, au conditionnel. Le brouillon 1 (`f6143faedd17cceff691f21b2d755218698a86f902fd13e0196ef8b6252f83d0`, gardé tel quel, R12) a été contre-lu par un agent neuf d'un autre modèle (Claude Opus 5.5) : `docs/decisions/brouillons/contre-lecture-decision-resserrement-revendications-v1.md` (`7ffc9d89844e5a9a6c19745c4cc8884c01e5165ab1afa21bdf20b303976002bc`), verdict « soumissible après ces couples ». Ce brouillon 2 applique ses 16 couples (table ci-dessous). **La vérification des corrections par le même contre-lecteur reste à faire** avant la soumission à Lazar.
- **Accord** : `GO-2026-11-20-29`, ligne lue dans `registres/go.md` par le rédacteur et par le contre-lecteur. Objet : « revendication 9 réduite à ce qui reste (familles tenues à l'écart, test A/A), Gideoni, Risi et Gal en citation obligatoire ; 14 et 12 (b) resserrées sur ce qui n'est pas pris. Contre-lecture Opus, puis soumission à Lazar, qui seul modifie une revendication. » Mot de Lazar tel que la ligne le rapporte : « Je recommande (a), confiance 0,7  go ».
- **Rédigé par** un rédacteur Claude Fable 5.2 (`claude-fable-5-2`), le 20 novembre 2026, à partir du brouillon 1 (écrit vers 08:20 UTC par le lecteur des quatre travaux, même modèle). Pages citées relues sur les PDF empreintés (`sha256sum -c`, cinq « OK » ; texte tiré par `pdftotext`, page par page).
- **Fondement** : `docs/notes/veille-organismes-ideation-v2/lecture-entiere-quatre-travaux-v1.md` (`65175e9121ff7db9332b8983eafc05fd164f389ea094a6d4f5daf0ffe8cf10c2`), elle-même non contre-lue. PDF empreintés, lus en entier : Terekhov et al., arXiv 2606.08892v3 (`8858355c…63b4beb`, 84 p.) ; Gideoni, Risi, Gal, arXiv 2602.16805v2 (`42514c0b…9a4b20913`, 21 p.) ; Zhang et al., arXiv 2607.26828v4 (`67028e61…9027d6549`, 28 p.) ; et, sans effet sur ce brouillon, Liu et al., « Escher-Loop », arXiv 2604.23472v2 (`a033a75c…70ae0357`, 21 p.). Aucun chiffre n'est opposable au-delà de ces lectures, page citée (R7).
- **Textes complétés, gardés tels quels (R12)** : `docs/notes/veille-exploration-idees-v1/revendications-v1.md` (`59c754ff…`), points 9, 12 (b) et 14 ; `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` (`b95688df…`), § 1 et § 2.

## Table des couples de la contre-lecture

Seize couples reçus ; **seize appliqués, aucun refusé**. Deux sont appliqués avec un amendement de lettre, déclaré ; un est complété. Chaque page a été relue sur le PDF.

| Couple | Objet | Sort | Raison |
|---|---|---|---|
| 1 | Titre et fondement : quatre travaux, Escher-Loop nommé | appliqué | l'en-tête disait « trois » pour une note de quatre ; tampon « 2604.23472v2 », 21 pages, vérifiés |
| 2 | 1.1 : coût du vote à k | appliqué, amendé | la p. 19 dit « For all methods the scaffold was limited to use up to 10 LLM calls per question » : écrit « pour l'échafaudage de toute méthode » au lieu de « pour les échafaudages trouvés » ; votes à 5 et à 10 : légende de la figure 3, p. 6 |
| 3 | 1.1 : test A/A, pratique courante | appliqué | évite la lecture « trou du champ » (R8) |
| 4 | 1.1 bis : lettre du point 9 | appliqué, complété | lettre citée en entier plutôt que tronquée ; un point signalé à Lazar ajouté sur « coût apparié » |
| 5 | 1.2 : ligne 6, probabilité et non espérance | appliqué | p. 15-16 : « the probability of sampling one that matches or outperforms Shinka's score », « this probability estimate » ; le constat du § 1 est corrigé de même |
| 6 | 1.3 : borne et deux domaines défavorables | appliqué, amendé | « 8/10 » exact (p. 9) ; la phrase « SCS' average performance being worse » ne nomme pas son terme de comparaison : citée telle quelle, lecture du contre-lecteur donnée comme lecture ; « seemingly » gardé pour la figure 3 |
| 7 | 1.4 : jour contre contenu | appliqué | tampon « arXiv:2602.16805v2 [cs.AI] 12 Oct 2026 », p. 1 |
| 8 | 2.1 : notes du juge et de la vérité approchée | appliqué | p. 42-43 : « weak=… strong=… combined=… » |
| 9 | 2.1 : « sans être dit nouveau ni propre » | appliqué | réserve portée dans la phrase même |
| 10 | 2.1 : point CONFIRM rebordé | appliqué | revendications-v1, points 4 et 14, relus : deux éléments restants sur trois touchent la part cédée, le premier peut-être |
| 11 | § 3, constat : un modèle de base par réglage | appliqué | p. 21 : « generator and guide model choices are fixed […] under each backbone » |
| 12 | 3.1 : « sans le dire nouveau ni propre » | appliqué | réserve du 3.3 portée dans la phrase même |
| 13 | 3.3 : attribution de Liu et al. | appliqué | p. 3 : « expose remaining resources to guide tool use or jointly select models and budgets » ; titre à la bibliographie, p. 11 (page ajoutée) |
| 14 | Ne pas écrire : notices, deux mauvaises lectures, bruit | appliqué | Wang et al. lu sur PDF pour la mémoire (N-073, complément 3) |
| 15 | Ne pas écrire : mondes négatifs, bras servi, ablation, juge durci | appliqué | p. 23-25 ; p. 7-8 |
| 16 | Ne pas écrire : allocation par gain sur coût, contrôleur aveugle au coût | appliqué | p. 6 ; proposition 1, p. 4 ; bandits à sac à dos, p. 3 |

**Changements hors couples, déclarés** : statut, accord et rédacteur de l'en-tête mis à jour (le rédacteur a lu la ligne du GO) ; constat du § 1 corrigé comme le couple 5 (probabilité, non meilleur de k) ; renvoi du 2.4 porté à la note d'entretien v2 ; Chen et al. 2021 ajouté aux textes non lus du § 5 ; § 6 ajouté (points pour Lazar). La remarque sans couple du contre-lecteur (« un seul modèle par réglage ») est couverte par le couple 11.

## 0. Portée

Ce texte **ne ferait que restreindre** ce que le programme présente comme sien. Il ne changerait aucune hypothèse, aucun critère de porte, aucun préenregistrement scellé. Rien n'y est déclaré « libre » : « non trouvé dans ce papier » ne dit rien des autres (R8). Il ne touche pas la revendication 8 : la lecture entière d'Escher-Loop n'y a rien trouvé à resserrer (note de lecture, section 3).

## 1. Revendication 9 — « le séquentiel doit battre le meilleur de N tirages indépendants, à budget égal »

**Constat.** Gideoni, Risi et Gal comparent des tirages indépendants et un séquentiel simple à des chaînes d'évolution de code, sous la même contrainte de budget, sur quatre domaines : « in all settings and under the same budget constraints, at least one of the baselines matches or exceeds a purpose-built code evolution pipeline » (p. 2). Ils emploient un témoin « vote majoritaire à k » (p. 7) et trouvent que toutes les méthodes de recherche font moins bien que lui sur le test (légende de la figure 3, p. 6). Ils mesurent le bruit d'évaluation avant de sélectionner (figure 4 et texte, p. 7). Ils dimensionnent le témoin par le coût moyen mesuré d'un tirage et calculent, par une formule combinatoire exacte rapportée à Chen et al. 2021, la **probabilité** qu'un des k tirages parmi n égale ou dépasse le score de la chaîne (« the probability of sampling one that matches or outperforms Shinka's score », « this probability estimate », p. 15-16) ; l'espérance du meilleur de k n'y est pas calculée. Leur part tenue à l'écart est une autre année du même concours (p. 6-7), non une famille. Le test A/A n'y est pas nommé.

**1.1 Les gardes de la porte.**
- *Avant* (N-073, § 2) : « Les gardes de la porte (familles tenues à l'écart, témoin « un modèle, vote à k ») sont **très probablement prises aussi**, d'après des notices seulement (Wang et al., arXiv 2607.12227 ; Gideoni, Risi, Gal, arXiv 2602.16805 ; Jwalapuram et al., arXiv 2606.13003 ; Pan Li, arXiv 2607.04108) : à lire sur PDF avant toute phrase publique, Gideoni et al. et Wang et al. d'abord. »
- *Après (proposé)* : « Le témoin "un modèle, vote à k" est pris (Gideoni, Risi, Gal, p. 6-7), avec un coût borné à dix appels par question pour l'échafaudage de toute méthode (« up to 10 LLM calls per question », p. 19), votes à 5 et à 10 (figure 3, p. 6), et non apparié en jetons ; la mesure du bruit d'évaluation avant sélection est prise dans son principe (p. 7). Ne seraient plus décrits, sans être dits nouveaux ni propres, que deux éléments non trouvés dans ce papier : la lecture sur des **familles** tenues à l'écart et le **test A/A** avant la comparaison, pratique courante des comparaisons expérimentales, simplement non nommée dans ce papier. Jwalapuram et al. et Pan Li resteraient à lire sur PDF ; Wang et al. resterait à relire sur ce point précis. »
- *Pages* : p. 6-7, p. 19.

**1.1 bis La lettre du point 9.**
- *Avant* (revendications-v1, point 9) : « Aucune voie à concepteur entraîné par renforcement n'est payée avant qu'une voie bon marché ait montré, sur familles tenues à l'écart, que l'apprentissage de génération en génération bat le meilleur de N tirages indépendants et le témoin « un modèle, vote à k, coût apparié » ; pilote de bruit et test A/A d'abord ; recherche bibliographique 2025–2026 obligatoire avant de revendiquer. »
- *Après (proposé)* : même lettre, suivie de « Protocole, témoin "vote à k" et pilote de bruit : pratique publiée, citée (Oved et al. ; Gideoni, Risi, Gal, p. 2, 6-7) ; ne restent décrits, sans être dits nouveaux ni propres, que la lecture sur familles tenues à l'écart et le test A/A. »
- *Pages* : p. 2, 6-7 ; Oved et al. d'après N-073, § 2.
- *Point signalé à Lazar* : la lettre du point 9 dit le témoin « coût apparié » ; chez Gideoni et al. le coût du vote à k est borné, non apparié (1.1). L'appariement en coût du témoin n'est donc pas trouvé dans ce papier. Le rédacteur ne l'ajoute pas à ce qui reste décrit : le mot de Lazar n'en nomme que deux (familles tenues à l'écart, test A/A), et un témoin apparié en coût est une pratique ordinaire.

**1.2 Les lignes gelées 2 et 6.**
- *Avant* (N-073, § 2) : « 2. *Taille du témoin* : N = budget du bras séquentiel divisé par le coût mesuré d'un tirage indépendant, et non le nombre de générations. » ; « 6. *Calcul* : espérance du meilleur de k parmi n graines journalisées par statistique d'ordre exacte […] ».
- *Après (proposé)* : mêmes lignes, inchangées dans ce qu'elles gèlent, suivies, pour la ligne 2, de « (pratique publiée : Gideoni, Risi, Gal, p. 15-16) » et, pour la ligne 6, de « (pratique voisine publiée : Gideoni, Risi, Gal, p. 15-16, calculent par la même combinatoire exacte la probabilité qu'un des k tirages parmi n égale ou dépasse une référence, d'après Chen et al. 2021, à lire sur source avant de la citer ; l'espérance du meilleur de k n'y est pas calculée) ».
- *Pages* : p. 15-16.

**1.3 Citation obligatoire.** S'ajouterait, dans tout texte qui touche à la porte : Gideoni, Risi, Gal, « Simple Baselines are Competitive with Code Evolution », arXiv 2602.16805. Avec sa borne : une seule course de la chaîne comparée par problème mathématique (p. 4) ; ampleurs non comparées pour les bornes et les compétitions (p. 21). Et avec sa nuance : le séquentiel simple, sans sélection par la note (p. 3), égale ou dépasse la chaîne sur 6 problèmes sur 9 contre 4 sur 9 pour les tirages indépendants (p. 5), et sur 6 compétitions sur 10 contre 2 sur 10 (tableau 2, p. 8) ; mais en optimisation combinatoire les deux témoins battent la chaîne sur 8 problèmes sur 10, la moyenne du séquentiel étant dite « worse chiefly due to poor performance on problem ahc039 » (p. 9 ; la phrase ne nomme pas son terme de comparaison, et la légende de la figure 5 donne aux deux témoins une moyenne plus haute que celle de la chaîne : lu comme « sous celle des tirages indépendants »), et pour les échafaudages les tirages indépendants font le mieux des méthodes de recherche (« seemingly », légende de la figure 3, p. 6).

**1.4 Réserve sur l'antériorité.** Le PDF lu est la version 2, datée du 12 octobre 2026 (tampon, p. 1). Le jour de la version 1 (18 février 2026) vient de la veille, d'après la page arXiv ; il n'est sur aucun PDF empreinté. L'identifiant imprimé sur le tampon (2602, p. 1) atteste seulement un premier dépôt en février 2026, sans rien dire de son contenu. Les expériences de la version 1 n'ont pas été lues : on ne sait pas lesquelles des pages citées ici y figuraient déjà. **Tant que la version 1 n'est pas téléchargée, empreintée et lue**, aucun texte ne devrait écrire que ce travail précède Oved et al. (13 octobre 2026) ; la phrase permise serait « Gideoni, Risi et Gal (version 2 du 12 octobre 2026) ». Cette réserve ne change rien au resserrement : le protocole est occupé dans les deux ordres.

## 2. Revendication 14 — juges de la recherche automatisée sous attaque

**Constat.** Terekhov et al. opposent à un juge-modèle de propositions de recherche un proposeur fort dont la consigne est optimisée pour le tromper. L'attaque « relies on knowledge of the blue team strategy » (p. 3) : l'optimiseur reçoit la liste des dix critères du juge (p. 6, p. 23, p. 41) et les notes rendues, celles du juge faible et celles de la vérité approchée (p. 41-43). Sans les critères, « it cannot discover effective attack strategies » (p. 23). Trois juges (le même modèle faible sous trois consignes) sont attaqués chacun par une attaque refaite, et le résultat est une frontière continue (p. 6, p. 7, p. 25-26). La vérité est un juge-modèle qui lit l'article (p. 3), non validé contre des personnes (p. 10). Les notes sont toujours rendues ; aucun juge n'est statistique.

**2.1 La forme de l'attaque.**
- *Avant* (revendications-v1, point 14) : « Forme encore revendiquée de l'attaque : mesure, sur des mondes où toute promotion est fausse, d'un juge statistique face à un proposeur modèle de langue chargé de le tromper, qui lit la description exacte du juge, libre dans ses propositions, avec un bras qui reçoit les verdicts et un bras qui ne les reçoit pas ; la partie « verdicts servis, mondes négatifs, zéro promotion » est cédée à CONFIRM. »
- *Après (proposé)* : « Suivant Terekhov et al. (2026), qui opposent à un juge-modèle de propositions de recherche un proposeur fort à consigne optimisée, informé des critères du juge et servi en notes du juge et de la vérité approchée, et qui mesurent par ablation ce que cette information apporte (p. 3, 6, 23), nous mesurerions la même attaque contre un **juge statistique**, sur des **mondes plantés où toute promotion est fausse** — la vérité étant celle du monde et non celle d'un juge-modèle —, avec **un bras qui reçoit les verdicts et un bras qui ne les reçoit pas**. La partie « verdicts servis, mondes négatifs, zéro promotion » resterait cédée à CONFIRM. Le proposeur chargé de tromper, informé du juge et libre dans ses propositions ne serait plus présenté comme ce qui distingue la forme ; ce qui reste serait décrit sans être dit nouveau ni propre. »
- *Pages* : p. 3, 6, 23, 41-43 ; p. 3 et 10 pour la vérité.
- *Point à trancher par Lazar* : ce qui reste est la réunion de trois éléments, dont deux voisinent la partie déjà cédée à CONFIRM (« mondes négatifs, zéro promotion » pour le deuxième, « verdicts servis » pour le troisième) ; le premier peut-être aussi, puisque revendications-v1, point 4, range CONFIRM parmi les travaux qui prennent le calcul hors des agents et la multiplicité. Ce que ce brouillon cède à Terekhov et al. (le proposeur chargé de tromper, informé du juge) était peut-être ce qui séparait la forme de CONFIRM ; après les deux cessions, il pourrait ne rester que le bras sans verdicts, et la réunion. Le rédacteur n'a pas lu CONFIRM et ne peut pas dire ce que cette réunion laisse.

**2.2 Les deux juges sous la même attaque.**
- *Avant* : « un juge statistique et un juge-tournoi génératif à la manière de Co-Scientist sont mesurés sous la même attaque par les seules notes rendues (forme du résultat : gain continu comparé des deux juges). »
- *Après (proposé)* : même phrase, suivie de « La comparaison de plusieurs juges sous une attaque refaite contre chacun, en résultat continu, est pratiquée pour des juges-modèles (Terekhov et al., p. 6, 7, 25-26) ; ce que nous décririons est la paire comparée, un juge statistique contre un juge génératif. »
- *Pages* : p. 6, 7, 25-26.

**2.3 Précédents et citations.** *Avant* : « Précédents cités de la prémisse du bras « juge génératif » : 2611.04556 et 2611.00643. » *Après (proposé)* : s'y ajouterait Terekhov et al., arXiv 2606.08892 (tableau de la figure 1, p. 2 ; p. 5), qui entrerait aussi dans les citations obligatoires de tout texte présentant l'attaque. Wang, Arcuschin, Conmy, arXiv 2602.15222, que les auteurs disent leur voisin le plus proche (p. 10), serait à lire sur source avant tout texte qui en parle.

**2.4 Hors de ce brouillon.** Le même papier écarte la détection au profit de l'entraînement contre les menaces diffuses (p. 2, p. 9). Cela touche les papiers du programme sur les sondes, non la revendication 14 ; voir `docs/notes/veille-organismes-ideation-v2/note-entretien-controle-diffus-v2.md`, lue avec son erratum 1 (elle remplace la version 1, gardée). Aucune proposition ici.

## 3. Revendication 12 (b) — composition apprise, coût dans le signal

**Constat.** CostAda crédite chaque pas d'une recherche par son progrès divisé par un facteur du coût réalisé et du budget dépensé (équation 1, p. 5), pour que coût et budget restant « shape the search rather than serving only as accounting variables or a stopping rule » (p. 1) ; il alloue le budget entre lignes de recherche par une règle à borne de confiance sur ce crédit (p. 6). Le contrôleur est à constantes fixes (p. 15, p. 17), court sous un seul modèle de base par réglage, choix du générateur et du guide fixés (p. 7, p. 20-21), deux lignes de recherche (p. 17), et exclut l'évaluateur du coût (p. 3, p. 20).

**3.1 Le coût dans le signal.**
- *Avant* (revendications-v1, point 12 b) : « La composition est une variable apprise : nombre de parties, rôles, modèle par rôle (frontière ou instrument local), règle d'agrégation, mémoire transmise, part de budget ; le coût entre dans le signal rendu ; la nécessité de la frontière est une sortie mesurée ».
- *Après (proposé)* : « La composition serait une variable apprise : nombre de parties, rôles, modèle par rôle (frontière ou instrument local), règle d'agrégation, mémoire transmise, part de budget. Suivant Zhang et al. (2026, CostAda), qui créditent chaque pas d'une recherche par son progrès rapporté au coût réalisé et au budget restant et répartissent le budget entre lignes de recherche sur ce crédit (p. 5-6), le coût entrerait dans le signal rendu ; ce que nous décririons, sans le dire nouveau ni propre (AgentTTS, BAMAS et Liu et al. non lus), est l'objet de ce signal — la composition de l'organisme, apprise —, non le principe. La nécessité de la frontière resterait une sortie mesurée. »
- *Pages* : p. 1, 5, 6 ; p. 7, 15, 17 pour ce que le papier ne fait pas.

**3.2 Même mot dans la lettre de l'énoncé 5.**
- *Avant* (N-073, § 1, lettre retenue) : « […] et à un concepteur entraîné plutôt que sélectionné, avec le coût dans le signal. »
- *Après (proposé)* : « […] et à un concepteur entraîné plutôt que sélectionné, avec le coût dans le signal, à la manière dont Zhang et al. (2026) le font entrer dans le crédit d'un contrôleur de recherche. »
- *Page* : p. 5.

**3.3 Ce qui n'est pas resserré, et pourquoi.** « Composition apprise », « modèle par rôle » et « nécessité de la frontière mesurée » ne sont pas dans CostAda. Ils ne sont pas pour autant dits libres : CostAda cite des travaux qui exposent le budget restant pour guider l'usage d'outils ou choisissent ensemble modèles et budgets (Liu et al., « Budget-aware tool-use enables effective agent scaling », arXiv 2511.17006 ; Wang et al., AgentTTS ; p. 3 ; bibliographie p. 11 et 12) et un système multi-agents sous budget (BAMAS, p. 3 ; bibliographie p. 12), et la veille en nomme d'autres (ligne A13) ; aucun n'est lu. Ils seraient à lire sur source avant toute phrase publique sur la composition apprise sous coût. Citation obligatoire proposée pour tout texte qui touche à 12 (b) : Zhang et al., arXiv 2607.26828.

## 4. Ne pas écrire (proposé, pour tout texte sortant)

- « le séquentiel contre le meilleur de N à budget égal » comme idée du programme (déjà dans N-073) ; « le témoin vote à k », « le pilote de bruit », « dimensionner le témoin par le coût mesuré d'un tirage », « le meilleur de k parmi n par formule exacte » comme apports ;
- « Gideoni, Risi et Gal précèdent Oved et al. », « dès février 2026 », tant que la version 1 n'est pas lue sur PDF empreinté ;
- « les témoins simples battent l'évolution de code » sans « au moins un des deux, selon le domaine » (p. 2) ; « les tirages indépendants suffisent » (4 sur 9 et 2 sur 10, p. 5 et p. 8) ;
- « personne n'a tenu des familles à l'écart », « personne ne fait de test A/A » (non trouvé dans un papier ; Jwalapuram et al. et Pan Li non lus ; Wang et al. lu pour la mémoire, non relu sur ce point) ;
- « Gideoni et al. calculent l'espérance du meilleur de k » (c'est la probabilité d'égaler ou dépasser une référence, p. 15-16) ; « Gideoni et al. apparient le vote à k en jetons » (borne de dix appels par question, p. 19) ; « le bruit d'évaluation fait choisir de mauvais candidats » comme constat du programme (p. 7) ;
- « un proposeur chargé de tromper un juge », « un attaquant qui lit la description du juge », « libre dans ses propositions », « comparer des juges sous la même attaque », « un résultat continu plutôt qu'un taux » comme ce qui distingue notre attaque ;
- « Terekhov et al. servent la description exacte du juge » (c'est la liste des dix critères, p. 23 et 41) ; « leur attaquant ne voit que les notes du juge » (il voit aussi la note de vérité, p. 41) ;
- « leur vérité est fausse » ou « invalide » (elle est non validée contre des personnes, p. 10) ; « leur juge durci est robuste » sans « contre leur attaque » (p. 7-8, p. 10) ;
- « premier juge statistique attaqué », « zone libre », pour ce qui reste de la revendication 14 ; « mondes où toute promotion est fausse » ou « un bras servi en verdicts » comme ce qui nous distingue, tant que CONFIRM n'est pas relu sur ce point ;
- « mesurer par ablation ce que l'information sur le juge apporte à l'attaquant », « durcir le juge contre l'attaque puis le réattaquer » comme apports (Terekhov et al., p. 23-25 ; p. 7-8) ;
- « faire entrer le coût dans le signal » comme idée du programme ; « CostAda apprend » (constantes fixes, p. 15) ; « CostAda choisit le modèle par rôle » (un modèle par réglage, p. 7) ; « CostAda compte le coût du juge » (évaluateur exclu, p. 3) ;
- « personne n'apprend la composition sous coût » (voisins nommés, non lus) ; « répartir le budget entre lignes ou parties selon le gain rapporté au coût » comme idée du programme (p. 6 ; bandits à sac à dos, p. 3) ; « un contrôleur aveugle au coût perd de la valeur » comme constat du programme (proposition 1, p. 4) ;
- tout chiffre de ces trois papiers sans sa page, et tout chiffre calculé par un lecteur présenté comme chiffre des auteurs.

## 5. Ce que ce brouillon ne ferait pas

- Aucune dépense, aucun changement de préenregistrement, aucune déclaration « libre », aucun numéro de décision.
- Il ne lit ni la version 1 de Gideoni et al., ni CONFIRM, ni Chen et al. 2021, ni les voisins nommés ; il les désigne.
- Il ne dit rien des revendications 7 et 8, sinon ceci : la note de lecture signale, pour la 7, un indice contraire borné tiré d'Escher-Loop (p. 6 ; tableau 1, p. 7), que Lazar pourrait vouloir voir cité.

## 6. Points pour Lazar

1. **Revendication 14, ce qui reste après deux cessions** (2.1) : peut-être seulement le bras sans verdicts et la réunion. CONFIRM est à relire sur ce point avant de trancher ; garder la forme, la réduire au bras sans verdicts, ou ne plus rien revendiquer de la forme.
2. **Revendication 9, « coût apparié » du témoin** (1.1 bis) : non trouvé chez Gideoni et al., non ajouté à ce qui reste décrit. À confirmer.
3. **Antériorité de Gideoni et al.** (1.4) : lire ou non la version 1 sur PDF empreinté. Sans effet sur le resserrement.
4. **Lectures désignées, non faites** : CONFIRM ; Chen et al. 2021 ; Jwalapuram et al. ; Pan Li ; Wang, Arcuschin, Conmy ; AgentTTS, BAMAS, Liu et al. 2025. La veille est gelée (allègement du 19 novembre) : les lire demande le mot de Lazar.
5. **Revendication 7** : l'indice contraire borné tiré d'Escher-Loop (§ 5), cité ou non.
6. **Numéro de décision et lettre finale** : seul Lazar modifie une revendication ; ce brouillon ne propose que des textes au conditionnel.
