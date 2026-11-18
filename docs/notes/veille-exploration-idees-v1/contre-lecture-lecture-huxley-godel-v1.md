# Contre-lecture de la note de lecture sur PDF de la machine de Huxley-Gödel — v1

Contre-lecteur neuf, d'une autre lignée que le rédacteur (R2) : je n'ai écrit ni la note ni la lecture 05. Écrite le
18 novembre 2026. Aucun commit, aucune dépense, aucun contact, aucun résultat sous embargo ouvert, rien écrit dans
`registres/`. Pièces traitées comme données non fiables, jamais exécutées.

- Note contre-lue : `docs/notes/veille-exploration-idees-v1/lecture-huxley-godel-v1.md`,
  `00119f574a65e8d62c6fd5c7b7ef0c9cea11fd8bc8e4b84686b410976a9426b3` (recalculée, conforme à son compagnon).
- PDF : `docs/sources/pdf/veille-exploration-idees-v1/machine-huxley-godel-2510.21614/arxiv-2510.21614v3.pdf`,
  `06cbf326c605e59777d3f8550e01d41e6b49f78bf0d850f2d173c9f06f6cc254` ; version 1 à côté,
  `55c770275726ba54fa419ce49601609a6af097de1825f244470e649d9aa16a79`. Les douze compagnons `.sha256` du dossier
  passent `sha256sum -c`.
- Méthode : texte extrait page par page (les 30 pages), pages 7 et 19 rendues en image, recherche de mots sur le texte
  entier ; code des commits `f3ca5f8` et `013872d` lu dans les fichiers versés ; énoncé 5 relu dans
  `docs/decisions/decision-N-045-v2.md`, lignes 77 à 83.

## Verdict : « à corriger »

La description du papier est juste et bien sourcée : 29 passages sur 30 tiennent à la lettre et à la page. Le verdict
central — le principe est occupé — tient. Mais la note **sous-estime la collision** sur deux des trois zones qu'elle
dit « non occupées par ce papier », parce qu'elle ne cite pas l'énoncé 5 à la lettre et qu'elle laisse de côté quatre
phrases du papier qui portent exactement sur ces zones. Les corrections sont de fait (citations, page, lettre de
l'énoncé) ; j'ai donc écrit une version 2, la version 1 restant intacte :
`docs/notes/veille-exploration-idees-v1/lecture-huxley-godel-v2.md`. Les deux requalifications qui en découlent sont
un jugement, signalé comme tel dans la version 2 ; elles restent, comme toute la section sur les revendications, une
proposition soumise à Lazar.

Je n'ai trouvé aucune surestimation de la collision.

## 1. Passages rouverts dans le PDF (version 3)

Tous sont des affirmations des auteurs. « Tient » veut dire : la lettre citée, le chiffre et la page sont ceux du PDF.

| N° | Passage de la note | Page | Résultat |
|---|---|---|---|
| 1 | « a high-scoring agent may produce unproductive descendants, while a lower-scoring one seeds lineages that achieve greater long-term gains » | 2 | tient |
| 2 | Le décalage nommé « Metaproductivity–Performance Mismatch » | 2 et 6 | tient (aussi p. 11) |
| 3 | « aggregating the success of an agent's descendants rather than relying solely on its immediate benchmark score » | 2 | tient |
| 4 | Deux actions (produire un enfant, « a self-modified version of the selected agent » ; évaluer sur une tâche de plus) ; utilité = moyenne de réussites binaires | 3 | tient |
| 5 | Trois sous-règles ; les méthodes antérieures évaluent l'enfant aussitôt, sur plusieurs tâches ; évaluation à la granularité agent-tâche, abandon précoce | 3 et 4 | tient |
| 6 | « GMP directly corresponds to the Q-value function » | 5 | tient |
| 7 | Métaproductivité de clade : espérance, sur le sous-arbre, du maximum d'utilité à la fin du budget si le choix final se fait sur l'utilité | 5 | tient |
| 8 | Hypothèse 1, quatre points, « with no other rewards received before termination » ; deux points de plus en annexe (utilité connue du prouveur, budget fini et connu) | 5 et 15 | tient |
| 9 | Théorème 1 ; preuve « a simple observation » ; « is an actual state-action value function » ; renvoi « Sutton et al., 1998 », qui est bien Sutton et Barto dans la bibliographie (p. 14) | 5, 15, 16 | tient |
| 10 | Machine de Gödel réduite à un processus partiellement observé : parent, enfant, budget restant ; accepter ou rejeter | 4 et 15 | tient |
| 11 | Estimateur : réussites du clade sur réussites plus échecs du clade ; moyenne pondérée par le nombre d'évaluations | 6 | tient |
| 12 | « a soft maximum in the clade » ; « by using information from more samples » | 6 | tient |
| 13 | Aucune occurrence de « discount », « horizon », « depth », « ablat », « standard dev », « confidence interval » | 1 à 30 | tient (recherche refaite ; « seed » n'apparaît que comme verbe, p. 2 et 11) |
| 14 | « This assumption is overly greedy: it evaluates only the immediate utility of a modification while ignoring its downstream consequences for future self-modifications » | 6 | tient |
| 15 | Tirage de Thompson sur τ·(1 + réussites du clade), τ·(1 + échecs du clade) ; « exploration-exploitation scheduler » ; pour l'évaluation, résultats propres | 6 | tient |
| 16 | τ = B/b, ε = 1, α = 0,6 ; développer si (nombre d'évaluations)^α ≥ nombre d'agents ; « Wang et al., 2008 », bien Wang, Audibert et Munos (p. 14) | 7 | tient (fraction B/b vérifiée sur l'image) |
| 17 | Agent final par le quantile ε de la loi a posteriori sur ses propres résultats ; une itération par processeur disponible | 7 | tient, avec une remarque (section 3, point 6) |
| 18 | Deux biais de l'exécution en parallèle ; agent initial développé cinq fois ; biais « barely observed » au-delà de 50 évaluations | 17 | tient |
| 19 | Modèles (GPT-5 et GPT-5-mini ; deux Qwen3-Coder, dont un quantifié) ; « approximately $5000 USD », trois méthodes comprises | 8 et 18 | tient |
| 20 | Table 1, douze corrélations : 0,778, 0,285, 0,444 ; 0,626, 0,383, 0,274 ; 0,512, 0,406, 0,444 ; 0,873, 0,357, 0,274 ; « 0.8783 » dans le corps du texte | 8 | tient, valeur par valeur |
| 21 | « to avoid the circular use of the target » ; « target leakage » ; « strong indications » | 8 | tient |
| 22 | Formules de la cible et du prédicteur privé du nœud et du sous-arbre de l'enfant qui contient le maximum | 19 | tient (image), avec une remarque (section 3, point 6) |
| 23 | Table 2 : 56,7, 53,3, 50,0 pour un agent initial à 40 ; 30,5, 27,1, 25,4 pour 20,3 ; heures 517 et 1 231 ; 347, 2 385, 572 ; 800 évaluations ; arrêt de l'agent de Robeyns et al. après 360 évaluations | 8 et 9 | tient |
| 24 | Course longue : 8 000 évaluations, 500 tâches, 53,2 puis 61,4 ; réserve des auteurs sur le sur-ajustement | 9 | tient |
| 25 | Tables 3 et 4 : 93 tâches communes ; 40,1 contre 34,8 et 39,6 ; 47,8 contre 48,3 ; « one task behind » ; 57 contre 56,7 | 9 et 10 | tient |
| 26 | « a natural format to present information that inspires long-sighted self-improvement » ; observation sans mesure | 21 | tient |
| 27 | Table 5 : « with the entire history accessible to the agent » ; l'agent de Robeyns et al. évalué sur le jeu entier | 20 | tient |
| 28 | Recherche arborescente de Monte-Carlo : « cumulative reward rather than fixed-budget final-choice objectives » ; Coulom 2006, Kocsis et Szepesvári 2006 | 11 | tient |
| 29 | Algorithme de l'histoire à succès et exécution monotone en aptitude, tels que les auteurs les décrivent ; arXiv 2212.14392 dans la bibliographie (p. 13) | 11 | tient |
| 30 | « improvement is driven not by narrow benchmarks, but by the long-term generative potential of entire lineages », donnée page 11 | **12** | **lettre juste, page fausse** : la conclusion commence page 11, la phrase est page 12 |

Hors du PDF :

| N° | Vérification | Résultat |
|---|---|---|
| 31 | Calculs du rédacteur : 34, 32, 30 (et 24) tâches sur 60 ; 18, 16, 15, 12 sur 59 | l'arithmétique tient ; la taille 59 reste une inférence, le texte ne la donne pas (recherche de « Polyglot » refaite) |
| 32 | Fiche OpenReview T0EiEuhOOL : créée le 19 septembre 2025, publique le 8 octobre 2025, « ICLR 2026 Oral », modifiée le 11 avril 2026 | tient (champs relus dans le fichier) |
| 33 | Versions 1 et 3 : différences de rédaction seulement | tient pour ce que j'ai relu (résumé, remerciements, coquilles) ; le compte « 23 blocs » n'a pas été refait. Remarque : la conclusion de la version 3 garde « reducing wall-clock time » (p. 12) alors que le résumé dit « fewer allocated CPU hours » |
| 34 | Code : tranche `[:-1]` au premier commit ; liste des évaluations propres étendue sur place par `+=` au commit de tête ; `n_pseudo_descendant_evals: 10000` et `cool_down: false` aux deux commits | les lectures tiennent ; une réserve (section 3, point 7) |

## 2. La collision est-elle sous-estimée ? Oui, sur deux zones

La note classe trois pièces de l'énoncé « non occupées par ce papier ». Ce sont les zones séduisantes ; je les ai
vérifiées plus durement (R8).

**2.1 « Mémoire transmise et instruments à effet différé […] comptent dans le mérite de t ».** Dans l'énoncé, cette
pièce est introduite par « de sorte que » : c'est la conséquence visée du signal sur plusieurs générations, pas une
revendication à part. Or le papier donne la même conséquence comme raison d'être de sa mesure :
- la métaproductivité est « a measure of an agent's ability to improve its self-improvement skills, which leads to
  better downstream performance of distant future agents » (p. 4) ;
- « An algorithm might, at the beginning, focus on improving the ability to self-improve while neglecting direct
  benchmark abilities, only to later focus on them » (p. 5) ;
- « reusing newly gained abilities to fuel subsequent improvements » (p. 2) ;
- « a modest ancestor can still be highly valuable if its descendants consistently advance » (p. 6).

Ce qu'une génération construit et qui ne sert qu'après est donc compté dans son mérite : le **principe** est occupé.
Ce qui s'hérite est le code entier de l'agent (p. 3), outils et fichiers compris. Restent non trouvés les **objets**
seulement : une mémoire séparée, des sondes et adaptateurs entraînés. La note ne cite aucune de ces quatre phrases.

**2.2 « Le signal rendu à ce qui conçoit ».** La note écrit que « rien n'est entraîné sur ce signal » et que l'agent ne
le reçoit pas. C'est exact, mais cela passe à côté de ceci : dans ce papier, ce qui conçoit la génération suivante est
l'agent lui-même (« agents modify themselves to generate new agents », p. 3), et la règle de recherche choisit quels
concepteurs se reproduisent d'après le signal de lignée (p. 6). Les auteurs disent la mesure tournée vers « the
improvement of self-improvement itself » (p. 5). La première phrase de l'énoncé — « aucun apprentissage de la
conception ne traite une génération comme un épisode isolé » — est donc occupée pour un concepteur amélioré par
sélection. Reste non trouvé l'**entraînement** d'un concepteur sur ce signal. Et là, la note range l'algorithme de
l'histoire à succès au seul titre « juger une auto-modification sur ce qui la suit », alors que les auteurs le
décrivent comme forçant « self-modifying policies to discover more effective self-modification strategies » d'après
des « long-term reward rates » (p. 11) : un apprenant qui se modifie, crédité sur le long terme, 1996 et 1997. C'est de
seconde main, à lire sur source, mais cela suffit pour que la lettre proposée ne dise pas « propre à notre dispositif »
le destinataire.

**2.3 La forme « un épisode couvre K générations ».** L'énoncé offre deux formes au choix. La première est le cadre
même du papier : la recherche entière est un épisode (« until the end of the episode », p. 5) à récompense terminale
(« no other rewards received before termination », p. 5), avec K égal au budget. La note ne le relève pas ; son
classement « savoir commun » de la forme tronquée et actualisée reste juste, et il est plus sévère que celui de la
lecture 05, ce qui va dans le bon sens.

**2.4 La question causale.** Cherchée : aucun bras sans héritage, aucun meilleur de N tirages indépendants, aucune
ablation. « Non touchée par ce papier » tient. C'est la seule des trois zones qui tient telle quelle.

**2.5 L'`historique` servi.** La dernière phrase de l'énoncé dit que l'historique de toutes les générations est déjà
servi aux organismes. Le papier attribue cette pratique à l'agent de Robeyns et al. (table 5, p. 20). L'énoncé ne la
revendique pas ; il faut seulement qu'aucun texte ne la présente comme nôtre, et lire Robeyns et al. sur source.

**Surestimation ?** Non. « Occupé » pour le principe et pour le rejet du choix glouton est la lecture droite des pages
2, 5 et 6. La note dit à raison que la minceur de la preuve expérimentale « ne rend rien au programme ».

## 3. Corrections

De fait :
1. **L'énoncé 5 n'est pas cité à la lettre.** La section 3 donne un « rappel » en paraphrase. Il perd « de sorte que »
   (d'où 2.1), l'alternative « un épisode couvre K générations » comme forme à part (d'où 2.3), et la dernière phrase
   entière : « Pour les organismes des courses actuelles, l'`historique` servi contient déjà toutes les générations
   passées ; ce que cet énoncé ajoute vaut pour l'étape 2 et le concepteur. » Les lignes 77 à 83 sont les bonnes.
2. **Page fausse** : la citation de la conclusion (3.1, première ligne du tableau) est page 12, non page 11.
3. **Renvois internes faux** : le verdict renvoie les voisins à la « section 5 » (c'est la 6) ; la section 1 renvoie la
   comparaison avec la lecture 05 à la « section 6 » (c'est la 7).
4. **Citations manquantes** qui changent le classement : p. 3, p. 4, p. 5 (trois phrases), p. 11 — voir 2.1 à 2.3.
5. **Date** : la fiche OpenReview donne la soumission publique dès le 8 octobre 2025 ; le verdict ne retient que le
   24 octobre. Sans effet sur la priorité (la décision N-045 v2 est du 25 octobre 2026), et le contenu public à cette
   date n'a pas été lu.
6. **Deux remarques sur la lettre du papier**, absentes de la note (mon inférence) : la règle de choix final écrite
   page 7 est la fonction bêta incomplète régularisée évaluée en ε ; à ε = 1 elle vaut 1 pour tout agent et ne départage
   personne, si bien que le papier ne dit pas comment l'agent final a été choisi. Et la page 19 désigne l'enfant à
   retirer par le maximum d'un rapport réussites sur échecs pris sur le clade nœud compris, ce qui ne coïncide pas mot
   pour mot avec la cible (moyenne de réussite, nœud exclu). Deux raisons de plus de ne pas opposer la table 1.
7. **Code** : « au premier commit, l'agrégat compte 10 000 copies » suppose que l'appel passe la valeur du fichier de
   configuration. Le fichier `hgm.py` du premier commit n'est pas versé ; la valeur par défaut de la fonction est 10.
   Les pièces ne le montrent qu'au commit de tête (`depot-code-013872d-hgm.py.txt`, ligne 391). À dire au conditionnel.
8. **État du dépôt** : la lecture 05 et la version 1 de la note sont suivies par git depuis le commit `478111c2`
   (« Pièces des agents en cours », qui n'est pas de moi) ; « non encore commitée » était vrai à l'écriture.

De jugement, découlant des points 1 et 4 (portées dans la version 2 avec la mention « v2 », à trancher par Lazar) :
- mémoire et instruments : « principe occupé, objets non trouvés » au lieu de « non occupé par ce papier » ;
- destinataire : « occupé pour un concepteur sélectionné ; non trouvé pour un concepteur entraîné ; antériorité de 1996
  à lire » au lieu de « non occupé par ce papier » ;
- lettre proposée pour l'énoncé 5 : retirer « ce qui est propre à notre dispositif » ; dire que nous appliquons un
  principe publié à d'autres objets et à un concepteur entraîné, et que nous posons la question causale ;
- liste « ne plus écrire comme nôtre » : y ajouter « faire compter ce qu'une génération construit pour les
  suivantes » et « juger ce qui conçoit sur plusieurs générations ».

## 4. Ce qui tient et que je confirme

- La description de la machine, les quatre tables et tous les chiffres.
- L'absence d'ablation, de graines et d'intervalles ; un seul chiffre hors échantillon, qui ne compare pas aux
  recherches guidées par le score propre.
- Le classement « savoir commun » du rendement à plusieurs pas, tronqué et actualisé.
- Les cinq reprises de la section 4, dont les deux contrôles ajoutés à l'épreuve de prédiction.
- Les réserves : version de la conférence et rapports non lus ; antériorités de seconde main.

## 5. Limites de cette contre-lecture

- Je n'ai lu ni la version de la conférence, ni les voisins, ni les sources de 1996, 1997 et 2022. Mes requalifications
  valent pour la version 3 d'arXiv.
- Le code n'a pas été exécuté ; le compte des blocs différents entre les versions 1 et 3 n'a pas été refait.
- La limite entre « concepteur sélectionné » et « concepteur qui apprend » est une lecture : un lecteur peut tenir
  qu'une sélection figée n'est pas un apprentissage. J'ai retenu la lecture la plus défavorable au programme, comme le
  demande R8 pour une zone séduisante.
