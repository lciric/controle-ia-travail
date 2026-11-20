# Contre-lecture du brouillon 1 de la décision de resserrement des revendications 9, 14 et 12 (b) — v1

**Verdict : soumissible après ces couples.** Toutes les citations sont exactes, mot pour mot et à la page. Le brouillon reste au conditionnel. Trois points cèdent trop ou mal : le calcul de la ligne gelée 6, le « coût apparié » du témoin, et le point sur CONFIRM, qui est posé trop étroitement (deux éléments sur trois touchent la part déjà cédée, pas un seul). Il manque la lettre du point 9 lui-même et quelques entrées de « Ne pas écrire ».

- **Contre-lecteur** : agent neuf, Claude Opus 5.5 (`claude-opus-5-5`), le 20 novembre 2026. Je n'ai écrit aucune des pièces lues. Pièce de classe A, contre-lecture R2.
- **Pièce contre-lue** : `docs/decisions/brouillons/decision-resserrement-revendications-apres-lecture-entiere-v1-brouillon1.md` (`f6143faedd17cceff691f21b2d755218698a86f902fd13e0196ef8b6252f83d0`, vérifiée).
- **Lu, empreintes vérifiées** :
  - la note de lecture entière `docs/notes/veille-organismes-ideation-v2/lecture-entiere-quatre-travaux-v1.md` (`65175e91…f10c2`) ;
  - les revendications `docs/notes/veille-exploration-idees-v1/revendications-v1.md` (`59c754ff…6c6d`) ;
  - la décision N-073 (`b95688df…3ecd`) et ses compléments 1 (`61903909…4478`), 2 (`5707dbd8…8e8e`) et 3 (`4ca0ce7b…03e5`), tous contrôlés par `sha256sum -c` contre leur fichier compagnon ;
  - les quatre PDF de `docs/notes/veille-organismes-ideation-v2/pdf/`, contrôlés par `sha256sum -c` (les quatre « OK »). Texte tiré par `pdftotext`, page par page (`-f N -l N`).
  - la seule ligne `GO-2026-11-20-29` de `registres/go.md`. Elle existe ; son objet correspond au brouillon (« revendication 9 réduite à ce qui reste (familles tenues à l'écart, test A/A), Gideoni, Risi et Gal en citation obligatoire ; 14 et 12 (b) resserrées sur ce qui n'est pas pris »). La réserve de l'en-tête du brouillon (ligne 4) peut donc être levée par la mère.
- **Non ouvert** : CONFIRM, la note d'entretien citée en 2.4, aucun travail cité par les papiers, aucune page du web.

## 1. Les citations (R7)

Chaque passage cité par le brouillon a été retrouvé à sa page :

- **Gideoni, Risi, Gal** :
  - p. 2, « in all settings and under the same budget constraints, at least one of the baselines matches or exceeds a purpose-built code evolution pipeline » : exact ;
  - p. 3, absence de sélection par la note : exact ;
  - p. 4, une seule course de ShinkaEvolve : exact ;
  - p. 5, 4 problèmes sur 9 et 6 sur 9, dans l'ordre « IID RS and SCS respectively » : exact ;
  - p. 6, légende de la figure 3 : exact ;
  - p. 7, vote à k et bruit : exact ;
  - p. 8, tableau 2, 2 sur 10 et 6 sur 10 : exact ;
  - p. 15-16, formule d'après Chen et al. : exact ;
  - p. 19, dix appels par question : exact ;
  - p. 21, ampleurs : exact ;
  - tampon de la p. 1, « v2 [cs.AI] 12 Oct 2026 » : exact.
- **Terekhov et al.** :
  - p. 3, « relies on knowledge of the blue team strategy » : exact ;
  - p. 6, les dix critères : exact ;
  - p. 23, « it cannot discover effective attack strategies » (légende de la figure 12) : exact ;
  - p. 41-43 : les deux notes rendues ; dix exemples portent « weak= » ;
  - p. 7-8, frontière diagonale : exact ;
  - p. 25-26, « separate red team optimization » : exact ;
  - p. 10, limites et voisin le plus proche : exact ;
  - p. 2 et p. 9, détection écartée : exact ;
  - Wang, Arcuschin, Conmy, arXiv 2602.15222 : confirmé à la bibliographie, p. 14.
- **CostAda** :
  - p. 1, « shape the search rather than serving only as accounting variables or a stopping rule » : exact ;
  - équation 1, p. 5 : exact ;
  - règle à borne de confiance, p. 6 : exact ;
  - constantes fixes, p. 15 : exact ;
  - « Kt = 2 throughout », p. 17 : exact ;
  - GLM-5 et GPT-5.4, p. 7 : exact ;
  - évaluateur exclu, p. 3 et p. 20 : exact ;
  - BAMAS : à la bibliographie, p. 12, et cité dans le corps, p. 3 (« Yang et al., 2026a »).

Trois paraphrases sont inexactes ou trop larges :

- **(a) La ligne gelée 6.** Gideoni et al. ne calculent pas l'espérance du meilleur de k parmi n. Ils calculent la **probabilité qu'un des k tirages égale ou dépasse le score de ShinkaEvolve**, soit 1 − C(n−c, k)/C(n, k) (p. 15-16, « this probability estimate »). La combinatoire exacte est la même, mais la statistique diffère. Écrire que la ligne 6 est « pratiquée » cède trop. La ligne 2 (taille du témoin par le coût moyen d'un tirage) est, elle, bien pratiquée (p. 16).
- **(b) Le « coût apparié » du vote à k.** La p. 19 donne une **borne** : « up to 10 LLM calls per question » pour les échafaudages trouvés. Les votes sont faits à 5 et à 10 (p. 6). Le coût n'est pas apparié au sens strict.
- **(c) Les voisins de CostAda.** Dans la phrase de la p. 3, Liu et al. (arXiv 2511.17006) porte, d'après sa bibliographie, sur l'usage d'outils sous budget (« Budget-aware tool-use enables effective agent scaling »). Le choix joint des modèles et des budgets revient plutôt à AgentTTS. Le brouillon attribue le choix joint aux deux.

**Remarque sans couple.** Sur CostAda, « un seul modèle par réglage » est une lecture raisonnable : un seul barème de prix par modèle de base (p. 20). Mais le texte dit seulement que le choix du générateur et celui du guide sont fixés (p. 20-21) ; il ne dit pas en clair que ce sont le même modèle.

## 2. Justesse du resserrement (R8)

- **Revendication 9.** Le resserrement est juste dans son ensemble et suit le mot de Lazar. Deux défauts, plus un oubli :
  - il cède un peu trop sur la ligne 6 (point 1 a) ;
  - sa nuance de citation ne retient que les deux domaines favorables au séquentiel. Or en optimisation combinatoire, les deux témoins battent la chaîne sur 8 problèmes sur 10, et la moyenne du séquentiel est sous celle des tirages indépendants (p. 9). Pour les échafaudages, les tirages indépendants font le mieux des méthodes de recherche (p. 6). Taire ces deux domaines tire la citation vers la prémisse « le séquentiel bat le meilleur de N » : c'est un trop beau (R4) ;
  - le test A/A, gardé comme reste, est une pratique courante des comparaisons expérimentales. Le dire en clair évite toute lecture de trou du champ (R8).
- **La lettre du point 9.** L'en-tête annonce que le point 9 de revendications-v1 est complété, mais aucun « avant / après » ne porte sur sa lettre : seul N-073, § 2, est touché. Il faut une ligne pour la lettre du point 9 (couple 4).
- **Revendication 14.** La cession à Terekhov et al. est juste : le proposeur chargé de tromper, informé des critères, libre, servi en notes, l'ablation, et les juges comparés sous une attaque refaite. Ce qui reste est fidèle à ce que le papier ne fait pas : aucun juge statistique, une vérité qui est un juge-modèle, aucun bras sans notes. J'ai vérifié que les deux ablations (p. 23 ; p. 24-25, figure 15) portent sur la grille de critères et jamais sur le fait de recevoir les notes. Deux défauts :
  - la phrase proposée ne dit pas que l'attaquant reçoit aussi la note de vérité (p. 41-43). La différence compte : sur un monde planté, notre attaquant ne voit pas l'oracle ;
  - le point sur CONFIRM est posé trop étroitement (section 3).
- **Revendication 12 (b).** La cession du principe « coût dans le signal » est juste, et nullement excessive : le principe est ancien, et les auteurs eux-mêmes citent les bandits à sac à dos (p. 3). Mais le texte proposé pour la revendication ne porte pas, en ligne, la réserve du 3.3 : AgentTTS, BAMAS et Liu et al. sont non lus. Lu seul, il présenterait l'objet du signal comme nôtre. Il faut y ajouter « sans le dire nouveau ni propre », comme pour la revendication 9.

## 3. Conditionnel et points signalés à Lazar

- **Le conditionnel.** Le brouillon reste au conditionnel et ne tranche rien. Les « est pris » de 1.1 sont à l'intérieur d'un texte proposé, dans le style de N-073 : c'est conforme.
- **L'antériorité de Gideoni et al.** Le point est bien posé, et la conclusion est juste : « le protocole est occupé dans les deux ordres ». On peut le préciser :
  - l'identifiant 2602 imprimé sur le tampon (p. 1) atteste un premier dépôt en février 2026 ; ce qui n'est pas vérifié, c'est le **contenu** de la version 1, non sa date ;
  - même la version 2 (12 octobre) précède d'un jour la date que N-073, § 2, donne pour Oved et al. (13 octobre). Un écart d'un jour ne fonde aucune antériorité utile : je ne propose rien de plus.
- **CONFIRM.** Le point est **mal borné**. Revendications-v1, point 14, cède à CONFIRM « verdicts servis, mondes négatifs, zéro promotion ». Cette part touche donc le **deuxième** élément restant (mondes où toute promotion est fausse) autant que le troisième (bras servi en verdicts). Le premier élément (juge statistique) est peut-être touché aussi : revendications-v1, point 4, range CONFIRM parmi les travaux qui prennent le calcul hors des agents et la multiplicité. Le proposeur informé chargé de tromper, cédé ici à Terekhov et al., était peut-être ce qui séparait la forme de CONFIRM. Après les deux cessions, il pourrait ne rester que le bras sans verdicts, et la réunion. Lazar doit le voir ainsi. Je n'ai pas lu CONFIRM.

## 4. Liste « Ne pas écrire »

La liste est presque complète. Il y manque :

- les mondes à promotion fausse et le bras servi en verdicts, présentés comme distinctifs ;
- l'ablation de l'information de l'attaquant et le juge durci puis réattaqué, présentés comme des apports (Terekhov et al., p. 23-25 et p. 7-8) ;
- les deux mauvaises lectures de Gideoni et al. relevées au point 1 (espérance du meilleur de k ; appariement en jetons), et le constat du bruit d'évaluation présenté comme nôtre (p. 7) ;
- l'allocation du budget par gain rapporté au coût (p. 6 ; p. 3) et le constat du contrôleur aveugle au coût (proposition 1, p. 4), présentés comme nôtres.

Il faut aussi corriger « trois notices non lues » : Wang et al., arXiv 2607.12227, a été lu sur PDF pour la mémoire (N-073, complément 3), même s'il ne l'a pas été sur ce point.

## 5. Couples (fichier : `docs/decisions/brouillons/decision-resserrement-revendications-apres-lecture-entiere-v1-brouillon1.md`)

Chaque « avant » est présent une seule fois dans le fichier (vérifié par `grep -c -F`).

1. **Titre et fondement** (quatre travaux).
   - avant : `après la lecture entière de trois travaux — v1`
   - après : `après la lecture entière de quatre travaux — v1`
   - avant : `` Zhang et al., arXiv 2607.26828v4 (`67028e61…9027d6549`, 28 p.). ``
   - après : `` Zhang et al., arXiv 2607.26828v4 (`67028e61…9027d6549`, 28 p.) ; et, sans effet sur ce brouillon, Liu et al., « Escher-Loop », arXiv 2604.23472v2 (`a033a75c…70ae0357`, 21 p.). ``
2. **1.1 Après : le coût du témoin.**
   - avant : `avec un coût apparié en nombre d'appels par question (p. 19) et non en jetons`
   - après : `avec un coût borné à dix appels par question pour les échafaudages trouvés (p. 19), votes à 5 et à 10 (p. 6), et non apparié en jetons`
3. **1.1 Après : le test A/A.**
   - avant : `la lecture sur des **familles** tenues à l'écart et le **test A/A** avant la comparaison.`
   - après : `la lecture sur des **familles** tenues à l'écart et le **test A/A** avant la comparaison, pratique courante des comparaisons expérimentales, simplement non nommée dans ce papier.`
4. **La lettre du point 9** (insertion avant 1.2).
   - avant : `**1.2 Les lignes gelées 2 et 6.**`
   - après : `**1.1 bis La lettre du point 9.**` + saut de ligne + `- *Avant* (revendications-v1, point 9) : « […] bat le meilleur de N tirages indépendants et le témoin « un modèle, vote à k, coût apparié » ; pilote de bruit et test A/A d'abord ; recherche bibliographique 2025–2026 obligatoire avant de revendiquer. »` + saut de ligne + `- *Après (proposé)* : même lettre, suivie de « Protocole, témoin "vote à k" et pilote de bruit : pratique publiée, citée (Oved et al. ; Gideoni, Risi, Gal, p. 2, 6-7) ; ne restent décrits, sans être dits nouveaux ni propres, que la lecture sur familles tenues à l'écart et le test A/A. »` + ligne vide + `**1.2 Les lignes gelées 2 et 6.**`
5. **1.2 : la ligne 6.**
   - avant : `suivies de « (pratique publiée : Gideoni, Risi, Gal, p. 15-16 ; formule d'après Chen et al. 2021, à lire sur source avant de la citer) ».`
   - après : `suivies, pour la ligne 2, de « (pratique publiée : Gideoni, Risi, Gal, p. 15-16) » et, pour la ligne 6, de « (pratique voisine publiée : Gideoni, Risi, Gal, p. 15-16, calculent par la même combinatoire exacte la probabilité qu'un des k tirages parmi n égale ou dépasse une référence, d'après Chen et al. 2021, à lire sur source avant de la citer ; l'espérance du meilleur de k n'y est pas calculée) ».`
6. **1.3 : la borne et la nuance.**
   - avant : `ampleurs non comparées (p. 21).`
   - après : `ampleurs non comparées pour les bornes et les compétitions (p. 21).`
   - avant : `et sur 6 compétitions sur 10 contre 2 sur 10 (tableau 2, p. 8).`
   - après : `et sur 6 compétitions sur 10 contre 2 sur 10 (tableau 2, p. 8) ; mais en optimisation combinatoire les deux témoins battent la chaîne sur 8 problèmes sur 10, la moyenne du séquentiel sous celle des tirages indépendants (p. 9), et pour les échafaudages les tirages indépendants font le mieux des méthodes de recherche (légende de la figure 3, p. 6).`
7. **1.4 : la date contre le contenu.**
   - avant : `La date de la version 1 (18 février 2026) vient de la veille, d'après la page arXiv ; elle n'est sur aucun PDF empreinté.`
   - après : `Le jour de la version 1 (18 février 2026) vient de la veille, d'après la page arXiv ; il n'est sur aucun PDF empreinté. L'identifiant imprimé sur le tampon (2602, p. 1) atteste seulement un premier dépôt en février 2026, sans rien dire de son contenu.`
8. **2.1 Après : ce que l'attaquant reçoit.**
   - avant : `informé des critères du juge et servi en notes, et qui mesurent`
   - après : `informé des critères du juge et servi en notes du juge et de la vérité approchée, et qui mesurent`
9. **2.1 Après : la réserve en ligne.**
   - avant : `ne serait plus présenté comme ce qui distingue la forme. »`
   - après : `ne serait plus présenté comme ce qui distingue la forme ; ce qui reste serait décrit sans être dit nouveau ni propre. »`
10. **2.1 : le point à trancher.**
    - avant : `- *Point à trancher par Lazar* : ce qui reste est la réunion de trois éléments dont le troisième voisine la partie déjà cédée à CONFIRM. Le rédacteur n'a pas lu CONFIRM et ne peut pas dire ce que cette réunion laisse.`
    - après : `- *Point à trancher par Lazar* : ce qui reste est la réunion de trois éléments, dont deux voisinent la partie déjà cédée à CONFIRM (« mondes négatifs, zéro promotion » pour le deuxième, « verdicts servis » pour le troisième) ; le premier peut-être aussi, puisque revendications-v1, point 4, range CONFIRM parmi les travaux qui prennent le calcul hors des agents et la multiplicité. Ce que ce brouillon cède à Terekhov et al. (le proposeur chargé de tromper, informé du juge) était peut-être ce qui séparait la forme de CONFIRM ; après les deux cessions, il pourrait ne rester que le bras sans verdicts, et la réunion. Le rédacteur n'a pas lu CONFIRM et ne peut pas dire ce que cette réunion laisse.`
11. **Constat du § 3 : le modèle.**
    - avant : `court avec un seul modèle par réglage (p. 7, p. 20-21)`
    - après : `court sous un seul modèle de base par réglage, choix du générateur et du guide fixés (p. 7, p. 20-21)`
12. **3.1 Après : la réserve en ligne.**
    - avant : `ce que nous décririons est l'objet de ce signal — la composition de l'organisme, apprise —, non le principe.`
    - après : `ce que nous décririons, sans le dire nouveau ni propre (AgentTTS, BAMAS et Liu et al. non lus), est l'objet de ce signal — la composition de l'organisme, apprise —, non le principe.`
13. **3.3 : les voisins.**
    - avant : `CostAda cite des travaux qui choisissent ensemble modèles et budgets (Liu et al., arXiv 2511.17006 ; Wang et al., AgentTTS ; p. 3) et un système multi-agents sous budget (BAMAS, p. 12)`
    - après : `CostAda cite des travaux qui exposent le budget restant pour guider l'usage d'outils ou choisissent ensemble modèles et budgets (Liu et al., « Budget-aware tool-use enables effective agent scaling », arXiv 2511.17006 ; Wang et al., AgentTTS ; p. 3) et un système multi-agents sous budget (BAMAS, p. 3 ; bibliographie p. 12)`
14. **Ne pas écrire : familles et A/A.**
    - avant : `(non trouvé dans un papier ; trois notices non lues) ;`
    - après : `(non trouvé dans un papier ; Jwalapuram et al. et Pan Li non lus ; Wang et al. lu pour la mémoire, non relu sur ce point) ;` + saut de ligne + `- « Gideoni et al. calculent l'espérance du meilleur de k » (c'est la probabilité d'égaler ou dépasser une référence, p. 15-16) ; « Gideoni et al. apparient le vote à k en jetons » (borne de dix appels par question, p. 19) ; « le bruit d'évaluation fait choisir de mauvais candidats » comme constat du programme (p. 7) ;`
15. **Ne pas écrire : revendication 14.**
    - avant : `- « premier juge statistique attaqué », « zone libre », pour ce qui reste de la revendication 14 ;`
    - après : `- « premier juge statistique attaqué », « zone libre », pour ce qui reste de la revendication 14 ; « mondes où toute promotion est fausse » ou « un bras servi en verdicts » comme ce qui nous distingue, tant que CONFIRM n'est pas relu sur ce point ;` + saut de ligne + `- « mesurer par ablation ce que l'information sur le juge apporte à l'attaquant », « durcir le juge contre l'attaque puis le réattaquer » comme apports (Terekhov et al., p. 23-25 ; p. 7-8) ;`
16. **Ne pas écrire : revendication 12 (b).**
    - avant : `- « personne n'apprend la composition sous coût » (voisins nommés, non lus) ;`
    - après : `- « personne n'apprend la composition sous coût » (voisins nommés, non lus) ; « répartir le budget entre lignes ou parties selon le gain rapporté au coût » comme idée du programme (p. 6 ; bandits à sac à dos, p. 3) ; « un contrôleur aveugle au coût perd de la valeur » comme constat du programme (proposition 1, p. 4) ;`

Les couples 1, 6 (première moitié), 11 et 13 sont de forme. Les couples 2, 4, 5, 6 (seconde moitié), 9, 10, 12 et 14 à 16 touchent au fond.
