# N-073 — Revendications resserrées après la veille sur l'exploration d'idées nouvelles par les modèles de langue — v1

- **Décision de Lazar**, mot direct dans la session mère `session_01XJ6Mgr8BN6UanALsQatc5E`, reçu vers 07:06 UTC le
  18 novembre 2026, verbatim : « Sept décisions pour toi. : go recos » (inscrit en R-3231).
- **Objet du mot** : les sept nœuds de la synthèse `docs/notes/veille-exploration-idees-v1/synthese-v1.md`
  (`dc35b778c257e923df88272bb15f379b04f2691e36122bbf6104e02a8504db9f`), § 6. Ce texte porte les nœuds N1 à N5
  (revendications) ; N6 et N7 (travaux) sont dits au § 7.
- **Rédigé par** la session mère, le 18 novembre 2026, à partir de la synthèse, des douze lectures sur PDF et de leur
  contre-lecture (`docs/notes/veille-exploration-idees-v1/contre-lecture-v1.md`,
  `773a83dcfd4aede2cdc74eaa2de3484334bb2a0b57286f5743f1759ea7bd8c50`), de la note en vigueur sur la machine de
  Huxley-Gödel (`lecture-huxley-godel-v2.md`, `cb8f9ea395901a7b1de3c588e97b1e3a56f4a78b233d19850e3e6456063907bd`) et
  de la liste des revendications (`revendications-v1.md`,
  `59c754ffb7067327d5b290b0999eaebe079c9e233ba873a9d0650ed710386c6d`). **Contre-lecture par un agent neuf (règle R2) :
  à venir** ; tant qu'elle n'est pas rendue, ce texte est la version de travail et non la lettre qui fait foi.

## 0. Portée

Cette décision **ne fait que restreindre** ce que le programme présente comme sien. Elle ne change aucune hypothèse
expérimentale, aucun critère de porte scellé, aucun préenregistrement scellé. Elle ne réécrit aucune décision antérieure
(R12) : elle fixe la lecture de N-044, N-045 v2 et N-049 sur les points nommés. Rien n'y est déclaré « libre » : « non
trouvé dans les pièces lues » ne veut jamais dire « trou du champ » (R8). Les chiffres de la littérature cités ici
viennent des lectures sur PDF, page citée ; aucun n'est opposable au-delà de ce que ces lectures en disent (R7).

## 1. Héritage d'une génération récompensé (N-045 v2, énoncé 5) — principe occupé

**Constat.** La machine de Huxley-Gödel (Wang, Piękos, Li, Laakom, Chen, Ostaszewski, Zhuge, Schmidhuber, arXiv
2510.21614, version 1 du 24 octobre 2025, soit un an avant l'énoncé 5) crédite un agent par les résultats agrégés de sa
descendance plutôt que par son score immédiat, et qualifie la sélection gloutonne de « overly greedy » (p. 2, p. 5-6).
La forme « K générations, actualisées » est un rendement à plusieurs pas (Sutton et Barto, cités par les auteurs p. 15).
Les auteurs décrivent (p. 11, seconde main) un algorithme de 1996 où une règle qui se modifie est créditée au long terme.

**Ne plus écrire comme idée ou constat du programme** (liste de la note Huxley-Gödel v2, § 5) :
- « récompenser l'héritage d'une génération », « créditer une génération (ou un agent) par les résultats de sa
  descendance », « le mérite d'une génération inclut ce que ses descendants obtiennent » ;
- « le score immédiat est un mauvais guide du potentiel d'amélioration à long terme », « la sélection gloutonne sur le
  score immédiat est trop courte », « exclure le bandit à un pas » présenté comme un apport ;
- « un signal sur plusieurs générations, tronqué à K et actualisé » présenté comme une idée ;
- « faire compter dans le mérite d'une génération ce qu'elle construit et qui ne sert qu'aux suivantes », quel que soit
  l'objet ;
- « ce qui conçoit est jugé sur plusieurs générations » quand ce qui conçoit est sélectionné ; « servir tout l'historique
  au concepteur » (attribué par les auteurs à Robeyns et al.).

**Lettre retenue pour l'énoncé 5 dans tout texte sortant** (note Huxley-Gödel v2, § 5) : « Suivant Wang et al. (2025),
qui créditent un agent par les résultats agrégés de sa descendance (métaproductivité de clade) pour guider une recherche
d'auto-modifications, afin que compte ce qu'un agent prépare pour ses successeurs, et l'antériorité qu'ils décrivent
(Schmidhuber et Zhao 1996 ; Schmidhuber, Zhao et Wiering 1997), nous rendons au concepteur un signal qui porte sur
K générations, actualisé — un rendement à plusieurs pas au sens de Sutton et Barto. Nous appliquons ce principe à
d'autres objets (une mémoire transmise, des sondes et adaptateurs entraînés à une génération et servis à la suivante) et
à un concepteur entraîné plutôt que sélectionné, avec le coût dans le signal. Nous posons une question que ce travail ne
pose pas : l'archive héritée cause-t-elle les découvertes ? »

**Ce qui reste, décrit sans être dit nouveau ni propre** tant que les voisins nommés ne sont pas lus sur source : les
objets (mémoire transmise, sondes et adaptateurs servis à la génération suivante) ; le concepteur entraîné, avec le coût
dans le signal ; la question causale. La lecture 05 a été durcie par la contre-lecture (« occupé en partie » pour le
destinataire du signal, tirage de Thompson sur la descendance, p. 6-7).

**Indice contraire à dire avec la prémisse** : chez Qin et al. (arXiv 2611.05108), ce qui est légué rapporte surtout au
départ (+24,0 au quart du budget) et presque plus à l'échéance (+1,2) (p. 6, tableau 8 p. 21, selon la lecture sur PDF).

**Citations obligatoires dans tout texte qui touche à l'énoncé 5** : Wang et al., « Huxley-Gödel Machine », arXiv
2510.21614 ; Zhang, Hu, Lu, Lange, Clune, « Darwin Gödel Machine », arXiv 2505.22954 ; Robeyns, Szummer, Aitchison, « A
self-improving coding agent », arXiv 2504.15228 ; Sutton et Barto ; Schmidhuber et Zhao (1996), Schmidhuber, Zhao et
Wiering (1997), Kirsch et Schmidhuber (2022) — **ces trois derniers à lire sur source avant de les citer** comme
antériorité.

## 2. « Le séquentiel doit battre le meilleur de N tirages, à budget égal » (N-045 v2, énoncés 4 et 6) — protocole occupé

**Constat.** Oved, Pony, Naparstek, Barzelay (arXiv 2610.23977, 13 octobre 2026, douze jours avant N-045 v2) refont la
comparaison de l'évolution de programmes aux tirages indépendants à coût en jetons égal : avance de 5 % ou moins sur 12
paires sur 15, de 23 à 28 % sur les 3 autres, toutes sur une seule tâche (p. 1, p. 4-5, tableau 2). Leur compagnon
(arXiv 2609.19799, 17 septembre 2026) trace déjà une ligne « meilleur de N sans évolution ». Le protocole est **occupé** ;
l'issue est **occupée en partie** (selon la tâche et le modèle ; « contredit » était trop fort). Les gardes de la porte
(familles tenues à l'écart, témoin « un modèle, vote à k ») sont **très probablement prises aussi**, d'après des notices
seulement (Wang et al., arXiv 2607.12227 ; Gideoni, Risi, Gal, arXiv 2602.16805 ; Jwalapuram et al., arXiv 2606.13003 ;
Pan Li, arXiv 2607.04108) : à lire sur PDF avant toute phrase publique, Gideoni et al. et Wang et al. d'abord.

**Lecture fixée.** La porte reste une **condition du programme** avant toute voie chère ; elle se présente comme une
**pratique publiée, citée**, jamais comme une idée du programme.

**Six lignes gelées dans tout préenregistrement de cette porte** (lecture 07, § 9) :
1. *Unité* : le budget se compte en jetons facturés (invite, complétion, raisonnement), sommés sur tous les appels du
   bras, relances et appels de pilotage compris, lus dans le journal des appels ; par modèle, convertis en dollars à un
   barème gelé.
2. *Taille du témoin* : N = budget du bras séquentiel divisé par le coût mesuré d'un tirage indépendant, et non le nombre
   de générations.
3. *Nombre de lignées* : gelé d'avance, ou choisi sur une moitié des graines et lu sur l'autre ; jamais maximisé sur les
   données lues.
4. *Même contrôle de validité sur les deux bras* avant de prendre un maximum, et lecture sur la part tenue à l'écart
   (N-049, N-050).
5. *Qui la fenêtre favorise* : le gain du dernier doublement du budget est rapporté pour chacun des deux bras.
6. *Calcul* : espérance du meilleur de k parmi n graines journalisées par statistique d'ordre exacte ; intervalle par
   rééchantillonnage des deux côtés, par sous-échantillonnage quand k = n.

## 3. « Familles inédites contre items inédits des familles vues » (N-044, objectif ultime) — distinction occupée

**Constat.** Srikanth et al. (arXiv 2609.26457 ; billet du 14 juillet 2026, article de septembre) exécutent le schéma
« se concevoir, puis se figer » pour des agents de recherche et font eux-mêmes cette distinction, en mots propres (p. 6) ;
leur mesure est mince (une famille inédite, une tâche, trois graines, p. 7). MetaEvoForge suit le même schéma, connu par
son seul résumé.

**Lecture fixée.** La distinction n'est plus présentée comme une idée du programme ; elle se cite. Ce qui se décrit
comme notre mise en œuvre, sans priorité : la **mesure par famille préenregistrée** — nombre minimal de familles fixé
d'avance, statistique par famille, deux points de contrôle figés de la même lignée (synthèse, idée 6).

## 4. Banque sœur (N-049) — phrase lue plus étroitement, audit du générateur d'abord

**Constat.** N-049 porte, de la main de Lazar : « Le sur-ajustement porte sur les 36 textes, pas sur la famille », et
« elle sépare "adapté aux 60 textes" de "adapté à la famille" ». Zhu et al. (« Bad Genius », arXiv 2609.18366, p. 5)
montrent qu'un lot tiré du même générateur ne voit pas un raccourci propre au générateur ; c'est un **contredit faible**
(preuve nette sur un banc synthétique, une méthode, une ligne ajoutée en version 3). La lecture unique du lot final est
une pratique ancienne (Zhu et al. p. 6, p. 24) : elle se cite, elle ne se revendique pas.

**Lecture fixée.** Une banque sœur du même générateur sépare « adapté aux textes » de « adapté à la famille **telle que
ce générateur la rend** » ; elle ne sépare pas « adapté à la famille » de « adapté au générateur ». En conséquence,
**avant toute construction ou lecture d'une banque sœur, le générateur dont elle est tirée est audité**, sur processeur,
sous préenregistrement : prédicteur sur les seuls traits de présentation (position, ordre, longueurs, format) face à la
vérité ; chercheur non paramétrique bon marché sur les tâches à vérité négative ; deux étiquettes de vérité (conception et
effet) (synthèse, idée 2). Un second rendu à traits de présentation permutés (synthèse, idée 9) reste à décider sur devis.

## 5. Proposeurs de plusieurs fournisseurs (N-045 v2, énoncés 1 à 3 ; N-067) — indice contraire cité dès maintenant

**Constat.** Ferreira, Liu, Zheng (« Beyond Symmetric Agents », arXiv 2609.35875, 26 septembre 2026) affirment, sans
table qui le teste, que « teams do not benefit from spanning more model families once member strength is accounted for »
(p. 7). Leur terrain : réponses fermées, petits modèles ouverts, aucune production d'idées, aucun modèle de frontière ; ils
écrivent eux-mêmes que les domaines qui récompensent la nouveauté pourraient valoriser autrement la diversité (p. 9). Le
recalcul du lecteur sur leurs tables (non apparié, non opposable) place le vote d'une équipe mixte près du vote du
meilleur modèle de son palier, seul, au même nombre de générations.

**Lecture fixée.** L'énoncé reste « voisin » et parmi ceux à ne pas déclarer libres publiquement ; **tout texte qui
présente la diversité des fournisseurs cite cet indice contraire, avec sa borne de terrain**, à côté des deux déjà au
dépôt (tirage au hasard, arXiv 2611.04420 ; a priori fixe sans modèle, CADS). **À l'étape 2, sur devis** : deux bras
témoins jugés sur l'oracle du monde planté et le coût — « même effectif, sans échange » et « chaque fournisseur seul,
k tirages, coût apparié » —, une garde de troncature par bras (réponses vides ou tronquées comptées, lecture refusée si
les taux diffèrent) et un coût en jetons totaux lus et produits.

## 6. Ce que cette décision ne décide pas

- Aucune dépense, aucun changement de préenregistrement scellé, aucune déclaration « libre ».
- Elle ne tranche pas la portée de N-053 (point 5) et de N-058 sur le contenu d'une consigne de proposeur (nœud ouvert,
  porté avec le projet d'essai des trois règles).
- Elle ne dit rien des revendications 13 (collisionneur), 14 (juges de la recherche automatisée sous attaque, déjà
  resserrée par N-065 et N-067) et 15 (banc de tricheurs), que la voie adverse de la veille n'a pas examinées.

## 7. Travaux accordés par le même mot (N6, N7)

- **N6** : les quatre premiers audits sans dépense de la synthèse (§ 4, idées 1 à 4) — témoins « vrais mais dérivables »
  dans chaque monde planté, audit du générateur des mondes plantés, table d'éligibilité, gel de « budget égal » à partir
  des comptes de jetons des journaux passés — chacun préenregistré (R1) et contre-lu (R2) avant toute lecture ; confiés
  au compte de l'organisme, après la course d'affinage des idées des mentors.
- **N7** : second passage de recherche limité à la périphérie du juge (finance empirique, découverte de modèles, billets
  de laboratoire) et lecture sur PDF des voisins nommés, **après le 22 novembre 2026, 02:00 UTC** (quota d'usage).
