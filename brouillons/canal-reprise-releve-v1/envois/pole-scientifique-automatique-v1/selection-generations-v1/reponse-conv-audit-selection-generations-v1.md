# Réponse de conv-audit — la boucle de sélection génération à génération de l'organisme d'idéation — v1

Lignée conv-audit, concepteur neuf (Opus), 1er novembre 2026 ; écrit à partir du relevé `date -u` de **09:50:58 UTC** (calcul
exécuté à 10:01 UTC). Réponse propre de conv-audit à la question scellée
`question-selection-generations-v1.md` (`c899221888d14e2df0640ac1b405cef286ca3bd84b45bec998519ac53fccbfcd`), à comparer puis
fusionner avec celles d'Argon, du collisionneur et de GPT-6 Astra. Niveau méthode ; aucune pièce du bras d'attaque ; rien sur
l'auto-organisation inspirée d'Avalon (sujet suspendu). Rien lu sous `donnees/`, aucun appel de modèle, aucun commit, aucun
compagnon `.sha256` écrit, aucun fichier existant modifié. Tout chiffre de littérature est « à vérifier sur PDF » (règle R7 :
aucun chiffre sans PDF empreinté, page citée) ; je n'en reprends aucun.

Conventions : **« pôle »** = la boucle de test par calcul (loi gelée, agent expérimentateur, juge figé statistique) ;
**« tests de mort »** = l'étage de la course qui exécute en bac à sable le critère de mort d'une fiche (codé, jamais activé) ;
**« pont »** = la traduction fiche → loi rendue ce matin ; **« tranche »** = un lot d'épisodes d'épreuve scellé ;
**« e-BH »** = règle de Benjamini-Hochberg appliquée à des e-valeurs (contrôle du taux de fausses découvertes sous dépendance
quelconque), déjà codée (`cycle.appliquer_multiplicite`, `pari_apparie.ebh_pondere`) ; **« n80 »** = nombre d'épisodes
d'épreuve pour qu'une fiche vraie soit promue avec probabilité 0,8.

---

## Verdict

1. **La conjonction « survit au test de mort et promue par le pôle » est juste pour la promotion, mais deux états ne suffisent
   pas, ni trois : il en faut cinq** — morte (réfutée), non concluante, en attente d'épisodes (loi gelée par le pont),
   hors pôle (renvoi motivé), promue. Seule la promue se reproduit. Sans « non concluante » distincte de « morte », la mémoire
   enterre des idées vraies jugées sur trop peu d'épisodes.
2. **La règle e-BH ne tue pas la puissance à 20-40 fiches ; elle coûte des épisodes** : à effet moyen (log-rapport de cotes
   0,6 par écart type), n80 passe de 215 (seuil par fiche) à 312, 330 et 337 épisodes pour 20, 30 et 40 fiches (+45 à +57 %) ;
   passer de 20 à 40 fiches ne coûte que +8 %. **Le vrai tueur de puissance est l'effet surestimé par la fiche** (×2 : n80
   1 310 à 1 414) ; le **pari à fraction**, déjà codé en v7, le ramène à 365-387 pour +8 % de coût quand l'effet est juste.
3. **La contrainte qui lie n'est pas statistique, c'est l'épreuve fraîche.** Le pont l'a établi : presque aucune fiche n'est
   testable aujourd'hui. Sans tranche fraîche, la génération 1 promeut zéro fiche et la boucle « sélectionne » sur le jugement
   des juges, en silence. Règle proposée : **banque croissante** — une tranche neuve par génération, rétrogradée en
   développement après lecture (≈ 330 épisodes par génération à effet 0,6 ; ≈ 1 300 à effet 0,3).
4. **L'ablation « génération 2 avec et sans filtre du pôle » à 20-40 fiches par bras n'est pas jugeable** : puissance 0,02 à
   0,25 si le filtre double la part de fiches vraies ; 0,09 à 0,67 s'il la triple. Il faut 80 à 160 fiches par bras,
   ou un **témoin interne d'immigrants** (fiches sans parents dans chaque génération) lu après 4 à 6 générations.
5. **Les tests de mort, placés avant le pôle, n'achètent presque pas de puissance** (le seuil dépend de log m) et en coûtent
   leur taux de fausse mort (0,98 → 0,89 à 600 épisodes, taux de fausse mort illustratif de 10 %) : leur valeur est le coût
   évité et la couverture de ce que le pôle ne teste pas, pas le contrôle d'erreur. Leur taux de fausse mort n'est mesuré
   nulle part aujourd'hui (le pré-pilote ne le mesure pas, dossier factuel § 11.2) : il faut des témoins vrais qui les
   traversent.

Neuf décisions pour toi (section h) ; trois sont des nœuds (dépense) : la tranche fraîche, l'activation des tests de mort sur
machine jetable, et le dessin de l'ablation.

---

## Réponses aux sept questions (format du tour 1)

### Q1 — Règle de survie

- **Option retenue.** Cinq états, décidés par un programme sur des verdicts scellés, jamais par un modèle :

  | état | condition (toutes gelées) | se reproduit ? | servi à g + 1 |
  |---|---|---|---|
  | **morte** | test de mort « éliminée » avec sévérité vérifiée (voir garde) ; ou loi vide (renvoi N5 du pont) ; ou réfutée par le pôle (e-processus de mort, option) | non | titre + code de raison |
  | **non concluante** | test de mort « non concluant » ; ou ni promue ni réfutée au terme de sa tranche ; porte l'effectif requis | non | titre + effectif requis |
  | **en attente d'épisodes** | pont sortie 2 (loi gelée, couche 3 : épisodes ou moniteurs neufs à produire) ou sortie 1 différée (épreuve fraîche manquante) | non | titre + « loi gelée, attend ses épisodes » |
  | **hors pôle** | pont sortie 3 (renvoi N1 « rien à mesurer », N2 « pas de chiffre », N3 « affaire de preuve » → pôle théorie, N4 « mode nouveau » → hors du pôle ; ou défaut du pont N6 à N11) | non | titre + code ; taux de testabilité par proposeur |
  | **promue** | retenue par e-BH au niveau 0,05 sur une **tranche fraîche** (m fixé avant toute issue) **et** non tuée par un test de mort à sévérité vérifiée | **oui** | fiche, loi gelée, état, effet estimé sur la tranche rétrogradée |

  **« Non tuée » plutôt que « survit »** : un test de mort non concluant (faute de données dans la tranche exploratoire, cas
  fréquent) ne bloque pas une fiche que le pôle promeut sur tranche fraîche, test plus sévère et seul à contrôler l'erreur ;
  un test de mort qui tue bloque ; un désaccord (tuée par le test de mort, retenue par le pôle) n'est pas promu et va au
  lecteur. C'est un écart à ta conjonction, dit ici pour que tu le tranches (décision D-S1).

  **Sort de la « vivante non testée »** (la seconde de ta question) : sa spécification est gelée maintenant (empreinte) ; elle
  ne se reproduit pas ; elle est jugée sur la **première tranche ouverte après son gel** et compte alors dans le m de cette
  génération-là ; elle n'a jamais d'avance sur une fiche neuve. **Contrôle des fausses découvertes** : e-BH au niveau 0,05
  sur la génération, déjà codée, valide sous dépendance quelconque (toutes les fiches partagent la même tranche, la
  dépendance est certaine) ; m = fiches entrées au pôle + témoins faux, fixé avant toute issue ; témoins vrais hors famille.
  Pas de partage du niveau par famille (axe, proposeur) : il divise le niveau sans rien protéger de plus.
- **Confiance** : 0,65 (sur la machine à états) ; 0,8 (sur « e-BH ne tue pas la puissance », calcul annexe A et C).
- **Pire cas nommé et garde.** *Génération vide qui se remplit par le jugement* : zéro promue, et la génération suivante
  reçoit quand même des parents, choisis par l'étiquette « notable » des juges (c'est ce que sert aujourd'hui
  `GenerationV54.texte_heritage` : titre, résumé, « notable »). Garde : aucun repli ; zéro promue → la génération suivante ne
  reçoit **aucun parent** (immigrants seulement) et le journal écrit « sélection par l'expérience : vide », comme le signal
  « pas de dents » ; essayée sur un cas sain (au moins une promue) et sur un artefact (zéro promue, aucun « notable » servi).
  Second pire cas : *preuve héritée sur la même tranche* (la mémoire ajoute le log W cumulé de la classe à l'e-valeur ; deux
  lectures de la même tranche ne se multiplient pas) → la mémoire ne cumule que sur des tranches distinctes, identifiants de
  tranche dans l'enregistrement de classe.
- **Option manquante.** (i) « Non concluante » distincte de « morte » ; (ii) un **e-processus de mort** : pari de la famille
  des fractions de la loi (inférence universelle) contre la loi engagée, lu au seuil 1/α — une loi « réfutée » l'est avec au
  plus 5 % d'erreur, et seulement si aucune fraction de l'effet déclaré ne tient (à simuler avant tout usage, confiance 0,5) ;
  (iii) un **témoin de sévérité** pour chaque test de mort : le même script, rejoué par le noyau sur la tranche dont la colonne
  d'issue est permutée, doit « éliminer » ; sinon la survie vaut « non concluant (test sans dents) ». Cela répond à la
  faiblesse connue des tests de mort : le seuil est celui de l'auteur de la fiche.
- **Pièce qui trancherait.** Une simulation v57 de la machine à états sur le monde de démonstration du cycle v5 (fiches vraies,
  fausses, triviales plantées), plus le taux de fausse mort des tests de mort mesuré sur des témoins vrais passés par le vrai
  bac à sable.

### Q2 — Fuite entre générations

- **Option retenue.** **Banque croissante à tranches** : une tranche neuve, scellée par session-depot, par génération ;
  ouverte seulement après le gel de toutes les fiches de la génération ; lue une fois (ordre secret) ; puis **rétrogradée en
  partie de développement** pour toutes les générations suivantes. Ce qui a été lu peut alors être servi librement à
  g + 1 (estimations d'effet, leçons) puisqu'il ne sera plus jamais une épreuve. Découpage **par tâche**, pas par épisode.
- **Ce qu'apprend g2 sur la même épreuve que g1** : elle apprend l'épreuve. Ses parents ont été choisis parce qu'ils allaient
  bien à cette tranche ; leurs filles y vont bien aussi, vraies ou non (sur-ajustement adaptatif, le problème du tableau de
  classement réutilisé). Le calcul annexe B le chiffre : si seule la liste des retenues (au plus 3 sur 30) fuit, la
  correction valide (borne d'union sur les transcriptions possibles) ajoute log 4 526 = 8,42 nat au seuil ; avec l'aptitude
  en 3 niveaux, 11,64 nat. À effet 0,6 : n80 = 330 sur tranche fraîche, contre 578 en deuxième lecture et 826 en troisième.
- **Coût en données** (n80 à 30 fiches, annexe B) : 159 épisodes par génération à effet 0,9 ; 330 à effet 0,6 ; 1 297 à
  effet 0,3 (pari à fraction : 174 ; 356 ; 1 393). Trois générations à effet 0,6 : 990 épisodes en tranches fraîches,
  contre une tranche unique réutilisée d'au moins 826 — presque le même coût, mais la réutilisation interdit de transmettre
  autre chose que la liste des retenues. En dollars (**illustratif**) : 0,047 dollar par épisode selon l'estimation de
  session-depot (comparaison couche 2, l. 40), ou ≈ 0,18 selon le devis central du pilote v2 (234 dollars pour 1 296 épisodes,
  décision pilote couche 2 v5, l. 128-131) ; soit **16 à 60 dollars par génération** à effet 0,6, 61 à 234 à effet 0,3.
- **Confiance** : 0,75.
- **Pire cas nommé et garde.** *Fuite par la tâche* : deux tranches qui partagent des tâches laissent passer une loi qui
  apprend les bizarreries d'une tâche. Garde : découpage groupé par identifiant de tâche, vérifié par le noyau ; plus la
  disjonction déjà prévue entre la tranche exploratoire des tests de mort et toute tranche non rétrogradée.
- **Option manquante.** La réutilisation corrigée par transcription (calculée ici) comme repli chiffré, et le **témoin de
  dérive** : les mêmes témoins vrais lus sur chaque tranche ; une différence de log W au-delà du bruit dit que les tranches ne
  sont pas échangeables (autre modèle, autre lot de tâches).
- **Pièce qui trancherait.** Les deux premières tranches avec leurs témoins de dérive ; et la mesure réelle du coût par
  épisode (l'écart du simple au quadruple entre les deux estimations).

### Q3 — Héritage

- **Option retenue.** Servir aux proposeurs de g + 1 des **états, pas des rangs** : pour chaque promue, la fiche, sa loi
  gelée en clair, son état, l'effet estimé sur la tranche rétrogradée ; pour chaque autre fiche, son titre et son code de
  raison (morte, non concluante + effectif requis, en attente, hors pôle + code). Ni score de juge, ni rang, ni aptitude
  chiffrée. Le noyau garde tout le reste (archive complète, trajectoires, classes de mémoire, graphe des lignées) sans le
  servir. **La mémoire refuse, pas les proposeurs** : la garde de redite à signature prédictive refuse mécaniquement la redite
  d'une promue (réplication) et fait hériter sa preuve à la redite d'une morte (démonstration du cycle v5, C : 0 double sur
  31 redites avec héritage, 11 sur 40 sans mémoire — dans le monde simulé).
- **Les éliminées avec leur raison : aident-elles ou ancrent-elles ?** Les deux, et on ne le sait pas pour des modèles de
  langage. Un titre plus un code de raison aide à ne pas reproposer ; le détail de l'échec apprend à contourner le test.
  D'où le minimum (titre et code) et une mesure (option manquante).
- **Confiance** : 0,55.
- **Pire cas nommé et garde.** *Effondrement par paraphrase* : les proposeurs réécrivent la promue (« affine X ») ; ses filles
  sont promues sur la tranche neuve parce que la loi est vraie : c'est de la réplication comptée comme des « survivantes
  neuves ». Garde : redite de promue refusée par la mémoire ; la fille doit prédire plus que ses parents (règle déjà codée) ;
  quota de lignée (Q5).
- **Option manquante.** Une **ablation de l'héritage dans la génération** : la moitié des appels de proposeurs, tirée par
  graine, reçoit la liste des mortes, l'autre non ; on lit le taux de redites et le taux de promues. Antériorités, toutes « à
  vérifier sur PDF » : archive de la recherche de nouveauté (Lehman et Stanley, 2011), MAP-Elites (Mouret et Clune, 2015,
  arXiv 1504.04909), îles et base de programmes de FunSearch (Romera-Paredes et al., Nature, 2024), archive ouverte de la
  machine de Gödel darwinienne (arXiv 2505.22954) — aucune n'est un héritage de *preuve statistique*, toutes héritent d'un
  score.
- **Pièce qui trancherait.** Cette ablation dans la génération, sur deux générations.

### Q4 — Sortie vers le programme

- **Option retenue.** Une promue devient **candidate** au programme si, et seulement si, quatre conditions écrites tiennent,
  lues par un lecteur neuf (règle R13 : sous-agent neuf, ni auteur de la fiche, ni traducteur, ni expérimentateur, ni auteur
  de la règle ; d'une autre famille que l'auteur de la fiche), sur un dossier fermé :
  1. **neuve** : sa signature (cible, forme, objets, sens, rendue par le pont) ne coïncide avec celle d'aucune hypothèse du
     programme — H1 à H9, HC1 à HC6, L, T, Tr (liste en section d) — **et** le lecteur ne la lit pas comme cas particulier
     ou conséquence de l'une d'elles ; antériorité vérifiée hors programme (R7, R8 : pas de faux trou) ;
  2. **décisive** : une table à deux lignes dit, si la prédiction tient et si elle échoue, quel critère de quelle porte
     (G0, G1, GC, G2, G3) ou quelle bascule pré-engagée (programme § 13) change ; au moins une ligne change quelque chose
     qu'aucune expérience déjà prévue (E1.x, EC.x, E2.x, E3.x) ne tranche ;
  3. **coût borné** : devis sous un plafond fixé par toi, sur les environnements et organismes existants, sans mode
     adversarial nouveau ;
  4. **dimensionnée contre la malédiction du vainqueur** : l'expérience du programme est dimensionnée sur la borne basse de
     l'effet, jamais sur l'estimation du pôle (une promue est choisie parce que son estimation est haute).

  Puis le chemin réglementaire : préenregistrement scellé (R1), contre-lecture (R2), devis, **ton GO** (feu vert) — ajouter une
  hypothèse est un nœud (modification d'hypothèse). La promotion par le pôle est un **criblage**, jamais une preuve
  opposable à une porte.
- **Confiance** : 0,65.
- **Pire cas nommé et garde.** *Hypothèse du programme déguisée* : une promue qui redit H1 (« gain blanc-sur-noir ») en
  d'autres mots entre comme neuve, et une porte est lue deux fois sur le même effet. Garde : collision de signatures, plus
  lecture d'implication, plus la règle « le criblage ne compte jamais pour une porte ».
- **Option manquante.** **Passer les hypothèses du programme elles-mêmes par le pont** pour obtenir leurs signatures : la
  nouveauté devient en partie mécanique. Et la condition 4 (malédiction du vainqueur).
- **Pièce qui trancherait.** Le pont joué sur H1 à H9, HC1 à HC6 : si la plupart ne se traduisent pas, la condition 1
  repose sur le lecteur seul, et il faut le dire.

### Q5 — Diversité et coût

- **Option retenue.** **Lignées tracées** (chaque fiche porte l'empreinte de ses parents ; lignée = ancêtre de génération 0) ;
  **quota** : aucune lignée ne prend plus du tiers des places de parents ; **immigrants** : 30 % de chaque génération sans
  parents (comme une génération 0, servis l'archive des états) ; indicateur : nombre effectif de lignées (exponentielle de
  l'entropie de Shannon des parts), alarme sous 3 ; grille de cellules (axe × cible × forme × famille du proposeur) suivie
  pour un MAP-Elites plus tard. **Coût par survivante** : un grand livre par fiche et par rôle (appels, jetons, dollars par
  relais, heures de carte, épisodes de tranche, minutes d'horloge, nœuds soumis à toi), tiré de `consommations.json` (budget
  v56) ; coût d'une génération = tout ce qu'elle a dépensé, mortes comprises ; **coût par promue neuve** = coût de la génération
  / promues non redites, avec l'intervalle exact de Poisson sur le compte (pour 0 promue, borne haute 3,7) ; plus l'entonnoir
  (proposées → niveau méthode → notables → antériorité → tests de mort → pont sortie 1 → promues → candidates).
- **Confiance** : 0,6.
- **Pire cas nommé et garde.** *Loi de Goodhart sur le coût* : des fiches bon marché qui redisent le connu avec une
  retouche dominent « par euro ». Garde : la loi doit battre le nul informé (déjà) ; témoins « triviaux » plantés (la
  démonstration v5 en a promu 0 sur 181) ; « neuve » décidée par la mémoire, pas par l'auteur.
- **Option manquante.** Les immigrants servent **deux fois** : garde de diversité et témoin interne continu de l'utilité de la
  sélection (Q6). Sélection des parents pénalisée par leur nombre d'enfants (forme de la machine de Gödel darwinienne, à
  vérifier sur PDF).
- **Pièce qui trancherait.** Le nombre effectif de lignées sur les trois premières générations.

### Q6 — Ablation

- **Option retenue.** Le dessin « génération 2 avec et sans filtre, 20 à 40 fiches par bras » **n'est pas jugeable** (annexe E) :
  si le filtre double la part de fiches vraies (5 → 10 %), puissance 0,02 à 0,10 ; s'il la triple (5 → 15 %), 0,09 à 0,27 ;
  de 10 à 30 %, 0,33 à 0,67. Il faut **80 à 160 fiches par bras** (puissance 0,59 à 0,89 pour 5 → 15 %), ou mieux un
  **témoin interne d'immigrants** : 21 filles et 9 immigrants par génération de 30, même tranche, cumulés — puissance 0,83
  après 4 générations et 0,96 après 6 si les filles sont vraies à 25 % contre 5 % ; 0,34 et 0,54 si elles le sont à 15 %
  (annexe F). Bras de comparaison s'il y a deux bras : **parents choisis par les juges** (« notable »), même nombre de
  parents, plutôt que des parents au hasard — c'est ta question du 29 octobre (des agents qui testent, plutôt que des
  jugements).
- **Métrique qu'un expert choisirait.** La **part de fiches promues sur tranche fraîche**, par fiche, test exact de Fisher
  unilatéral (M1). « Survivantes neuves par euro » est une bonne métrique de gestion mais une mauvaise statistique de test :
  rapport de deux quantités bruitées, numérateur minuscule, dénominateur dominé par les coûts fixes ; à budget égal par bras,
  c'est M1. Contre mon attente, le test des rangs sur log W final (M2) est **moins** puissant que M1 ici (la plupart des fiches
  sont nulles, leurs rangs diluent le signal). Les témoins plantés ne sont pas la métrique : ils valident (mêmes témoins dans
  les deux bras, même tranche, même m : leurs verdicts doivent être identiques ; toute différence est un défaut de plomberie).
- **Confiance** : 0,8 (non jugeable à 20-40) ; 0,6 (le témoin d'immigrants est le meilleur dessin).
- **Pire cas nommé et garde.** *Bras confondus* : dérive dans le temps, version de modèle servie qui change entre les bras,
  tranches différentes. Garde : appels entrelacés par graine, même tranche, contrôle A2 du modèle servi (code v56), témoins
  identiques.
- **Option manquante.** Le témoin interne d'immigrants (gratuit : les immigrants existent déjà pour la diversité) ; et la
  règle « non jugeable » déclarée d'avance si la génération 1 promeut moins de 3 fiches.
- **Pièce qui trancherait.** Le nombre de promues de la génération 1 et les parts réelles de fiches vraies.

### Q7 — Ce qui existe

- **Option retenue.** Personne, à ma connaissance non vérifiée, ne sélectionne génération après génération des **hypothèses**
  par un **test statistique gelé avec contrôle des fausses découvertes sur épreuve fraîche** ; c'est une **question** (règle
  R8), pas une revendication : les zones séduisantes se lisent le plus durement. À reprendre tel quel, sous réserve des PDF :
  - **îles avec remise à zéro périodique des plus faibles** (FunSearch) → nos lignées et quotas ;
  - **cascade d'évaluation, du moins cher au plus cher** (AlphaEvolve, arXiv 2506.13131) → tests de mort avant le pôle comme
    filtre de coût ;
  - **rejet par nouveauté avant évaluation** (ShinkaEvolve, arXiv 2509.19349) → la mémoire refuse avant toute dépense ;
  - **tirage aléatoire de nouveaux cas de test à chaque génération** contre le sur-ajustement (« Random Sampling Technique »,
    Gonçalves et al., EuroGP 2012 ; « interleaved sampling », EuroGP 2013) → tranche neuve par génération ;
  - **sélection par cas de test qui garde la diversité** (sélection « lexicase », Spector ; Helmuth, Spector et Matheson) ;
  - **réutilisation contrôlée d'une épreuve** (« reusable holdout », Dwork et al., Science 2015 et arXiv 1506.02629 ; « Ladder »,
    Blum et Hardt, arXiv 1502.04585) → la correction par transcription de Q2 ;
  - **e-BH** (Wang et Ramdas, arXiv 2009.02824), **contrôle en ligne sur une suite de générations** (e-LOND, Xu et Ramdas,
    AISTATS 2024, arXiv 2311.06412), **e-BH renforcée** (calibrage conditionnel, Lee et Ren, arXiv 2404.17562 ; e-BH « fermée »,
    arXiv 2504.11759).
  Ce que les systèmes nommés font, et ce qui manque (section c, tableau) : AI Scientist v2, Agent Laboratory, Co-scientist,
  Robin sélectionnent par jugement ou dans une seule course ; LLM-SR (arXiv 2404.18400) et POPPER (arXiv 2502.09858) sont
  **les plus proches** (hypothèses éprouvées sur données ; e-valeurs séquentielles) et sont à lire en premier.
- **Confiance** : 0,5 (carte incomplète, rien lu sur PDF).
- **Pire cas nommé et garde.** *La boucle existe déjà* (par exemple une population d'hypothèses de type POPPER ou LLM-SR avec
  contrôle des fausses découvertes et épreuve renouvelée). Garde : R8 ; POPPER, LLM-SR, AlphaEvolve et FunSearch lus sur PDF
  empreinté avant toute phrase de revendication.
- **Option manquante.** La littérature pertinente pour Q2 n'est pas celle des « IA scientifiques » mais celle du
  sur-ajustement en programmation génétique et de l'analyse adaptative des données.
- **Pièce qui trancherait.** Les PDF, pages citées.

---

## Conception de la boucle

### (a) Règle de survie gelée et contrôle des fausses découvertes

**Ordre dans une génération g** (une fiche passe d'un étage au suivant par un verdict scellé ; le noyau tient l'ordre) :

1. Course : proposeurs, garde de forme, aiguilleur (niveau méthode seulement), juges, antériorité — inchangés.
2. **Pont et tests de mort en parallèle, cloisonnés** (décision D-P3 du pont, défaut (a)) : la sélection des fiches à traduire
   et à tester ne dépend d'aucun verdict (règle N-053, « pare-feu » : aucun score de juge dans une sélection) ; aucun des deux
   ne voit l'autre avant les deux scellements ; la tranche exploratoire des tests de mort est disjointe de toute tranche non
   rétrogradée (vérifié par identifiants).
3. Tests de mort avec **témoin de sévérité** : pour chaque fiche, le noyau rejoue le script de l'expérimentateur sur la tranche
   exploratoire dont la colonne d'issue est permutée (graine dérivée de l'empreinte du préenregistrement court) ; « survit »
   ne compte que si le témoin est « éliminé ».
4. Pôle sur la **tranche fraîche** S_g : entrent les fiches en sortie 1 non tuées par un test de mort ; **m = ces fiches +
   témoins faux, fixé avant toute issue** (`m_fixe`, code v11) ; témoins vrais hors famille, lus au seuil m/α ; numérateur à
   **pari à fraction** pour les fiches du pont (décision D-S3).
5. e-BH au niveau 0,05 sur la génération (`appliquer_multiplicite`, inchangé) ; e-processus de mort en option (à simuler).
6. Le programme range chaque fiche dans l'un des cinq états (tableau de Q1) ; scelle le journal des états ; seule la promue
   est parent.

**Ce que cela coûte en puissance à 20 à 40 fiches** (annexe A et C ; monde simulé décrit en annexe) :

| effet (log-rapport de cotes par écart type) | n80 par fiche (seuil 1/α) | n80 à e-BH, m = 20 / 30 / 40 | surcoût en épisodes |
|---|---|---|---|
| 0,9 | 102 | 155 / 159 / 164 | +52 à +61 % |
| 0,6 | 215 | 312 / 330 / 337 | +45 à +57 % |
| 0,3 | 886 | 1 260 / 1 297 / 1 331 | +42 à +50 % |
| 0,6, effet déclaré ×2, pari plein | 796 | 1 310 / 1 367 / 1 414 | — |
| 0,6, effet déclaré ×2, pari à fraction | 265 | 365 / 380 / 387 | — |

- À tranche fixe, le prix se voit seulement près du seuil : à 300 épisodes et effet 0,6, part des vraies retenues 0,93 par
  fiche contre 0,73 à 0,80 sous e-BH ; à 600 épisodes, 0,98 à 0,99 dans tous les cas.
- Taux de fausses découvertes observé : au plus 0,006 dans toutes les cases (le seuil par fiche sans multiplicité donne
  0,007 à 0,034) : e-BH est **conservatrice** ici, et monter le niveau à 0,10 ou 0,20 ne rachète que 5 à 10 points, à
  300 épisodes seulement.
- Les témoins faux comptés dans m (par exemple 30 + 5) coûtent 1 à 2 % d'épisodes : négligeable.
- **Leviers réels**, par ordre d'effet : (1) pari à fraction quand l'effet déclaré est incertain (n80 divisé par 3,6 si
  l'effet déclaré est le double du vrai) ; (2) taille de la tranche ; (3) preuve héritée sur tranches distinctes (produit
  d'e-valeurs) ; (4) e-BH renforcée (calibrage conditionnel ou fermée), à lire sur PDF, gain attendu modeste à m petit.
- **Entre générations** : e-BH garantit le taux par génération, pas sur toute la suite des promotions. Un contrôle en ligne
  (e-LOND) le donnerait ; inutile tant que la promotion n'est qu'un criblage confirmé par une expérience préenregistrée du
  programme (Q4).

### (b) Renouvellement de la partie d'épreuve

**Règle (gelée dans le préenregistrement de la boucle)** :
1. Avant la génération g, session-depot scelle la tranche S_g : identifiants groupés par tâche, taille fixée par le calcul de
   puissance sur un effet cible déclaré d'avance (≈ 330 à 360 épisodes pour 0,6 à 30 fiches), graines par
   `numpy.random.SeedSequence` dont l'entropie = empreinte du préenregistrement de la boucle et une valeur de session-depot
   engagée par son empreinte avant le scellement (forme du premier essai du pont, section g).
2. S_g s'ouvre seulement après le gel de toutes les fiches de g (empreintes et horodatages vérifiés par le noyau).
3. S_g est lue une fois, dans un ordre secret tiré après le gel ; les verdicts sont scellés ; S_g est **rétrogradée en
   développement**.
4. Aucune fiche n'est jamais jugée sur une tranche rétrogradée ; une loi gelée en attente est jugée sur la première tranche
   ouverte après son gel.
5. La preuve héritée (log W cumulé d'une classe de mémoire) ne se multiplie qu'entre tranches distinctes.
6. Le prédicteur « connu » (nul informé) et les seuils sont ajustés sur la partie de calibrage, **gelés par époque** ; un
   réajustement sur des tranches rétrogradées n'a lieu qu'à une frontière d'époque déclarée d'avance (sinon le nul change
   entre générations et les générations ne se comparent plus).
7. Témoins de dérive : les mêmes témoins vrais sur chaque tranche ; écart au-delà du bruit → nœud.

**Ce que cela impose aux couches 2 et 3** (couche 2 = banque de scores avec sabotage ; couche 3 = épisodes ou moniteurs neufs
produits à la demande) : produire la banque **en tranches** scellées et échangeables (même modèle, mêmes familles de tâches,
mêmes modes connus scellés), groupées par tâche, d'une taille fixée avant production ; une partie de calibrage unique ; un
registre des tranches tenu par le noyau (scellée, épreuve de g, rétrogradée) qui alimente aussi le registre des lectures du
pont (sa garde de rétrodiction n'a de valeur que si ce registre est complet) ; pour la couche 3, chaque loi en attente reçoit
ses propres épisodes produits après son gel, qui forment sa tranche. conv-audit ne lit jamais `donnees/` : les tranches sont
chez session-depot.

### (c) Héritage

| objet | servi aux proposeurs de g + 1 | gardé par le noyau (jamais servi) |
|---|---|---|
| promue | fiche (vue anonyme), loi gelée rendue en clair, état, effet estimé sur la tranche rétrogradée, lignée | trajectoire de log W, e-valeur, classe de mémoire, coûts |
| morte | titre + code de raison (tuée par test de mort ; réfutée ; loi vide ; redite) | tout |
| non concluante | titre + effectif requis | tout |
| en attente | titre + « loi gelée, attend ses épisodes » | spécification gelée, demande de couche 3 |
| hors pôle | titre + code N1 à N4 ; taux de testabilité par proposeur | réponses du pont, code N6 à N11 |
| fusions inachevées | rien (règle v56) | archive à part, jamais relue |
| témoins | rien (un témoin reconnaissable cesse de mesurer) | tout |

Jamais servis : score de juge, « notable », rang, aptitude chiffrée, toute information d'une tranche non rétrogradée.
**Archive des éliminées** : complète, jamais effacée, jamais parent ; elle sert contre le biais du survivant et à mesurer le
pôle (ses témoins). **Compatibilité avec la règle N-053** (aucun score dans l'entraînement ou la sélection de l'agent) : la
sélection porte sur des fiches, pas sur des agents, et l'information servie vient de tranches rétrogradées ; à confirmer par
le lecteur.

**Antériorités** (toutes « à vérifier sur PDF », aucun chiffre repris) :

| système | ce qui est hérité | qui sélectionne | à reprendre | ce qui diffère |
|---|---|---|---|---|
| Recherche de nouveauté (Lehman et Stanley, Evolutionary Computation, 2011) | archive des comportements nouveaux | distance à l'archive | nouveauté = distance de signature prédictive à l'archive, mortes comprises | aucune preuve, aucun test |
| MAP-Elites (Mouret et Clune, arXiv 1504.04909) | une élite par cellule de descripteurs | score dans la cellule | grille axe × cible × forme × famille | score déterministe, pas de multiplicité |
| FunSearch (Romera-Paredes et al., Nature, 2024) | base de programmes en îles ; meilleurs programmes dans la consigne | évaluateur programmé | îles, remise à zéro des plus faibles | l'évaluation est l'objectif lui-même : pas de sur-ajustement à contrôler |
| AlphaEvolve (arXiv 2506.13131) | base évolutive inspirée de MAP-Elites et des îles | évaluateurs en cascade | cascade du moins cher au plus cher | idem |
| ELM (Lehman et al., arXiv 2206.08896) ; QDAIF (arXiv 2310.13032) | MAP-Elites avec un modèle de langage comme mutation | score ; retour d'un modèle (QDAIF) | modèle de langage comme opérateur | QDAIF sélectionne par jugement |
| ShinkaEvolve (arXiv 2509.19349) | îles, rejet par nouveauté | évaluateur | rejet avant dépense | idem |
| Machine de Gödel darwinienne (arXiv 2505.22954) | archive ouverte d'agents | banc d'essai ; parent pénalisé par son nombre d'enfants | pénalité de fécondité | agents, pas hypothèses |
| LLM-SR (arXiv 2404.18400) | tampon d'expérience d'équations | ajustement aux données | hypothèses éprouvées sur données | à vérifier : épreuve tenue à part pour la sélection ou seulement pour le rapport final ? |
| POPPER (arXiv 2502.09858) | — (une hypothèse, plusieurs expériences de falsification) | e-valeurs séquentielles | agrégation d'e-valeurs de plusieurs tests d'une même hypothèse | pas de population, pas de générations (à vérifier) |
| Programmation génétique avec test (RST, Gonçalves et al., EuroGP 2012 ; lexicase, Helmuth et al., IEEE TEC 2015) | population | cas de test retirés à chaque génération ; sélection par cas | tranche neuve par génération | score, pas test statistique |
| AI co-scientist (arXiv 2502.18864) ; Robin (arXiv 2505.13400) | hypothèses classées par tournois | jugement de modèles ; expériences humaines | rien pour la sélection | sélection par jugement |
| AI Scientist v2 (arXiv 2504.08066) ; Agent Laboratory (arXiv 2501.04227) | arbre d'expériences dans une course | relecteur modèle | exploration sur le développement | pas de générations d'hypothèses ; l'auteur se juge |

### (d) Règle de sortie vers le programme

**Texte à geler** (empreinte avant la première lecture) :

> Une fiche promue est **candidate** au programme si (1) sa signature ne coïncide avec celle d'aucune des hypothèses H1
> « gain blanc-sur-noir », H2 « accumulation séquentielle sur sondes », H3 « courbe sécurité(N) », H4′ « compromis
> diversification/coordination », H5 « nombre × diversité des moniteurs », H6 « marge asymétrique », H7 « riposte et fuite »,
> H8 « la validité prédit la robustesse », H9 « survie des contraintes à la délégation » (décision N-035), HC1 « loi de
> déférence », HC2 « robustesse des sondes », HC2b « trahison par les activations », HC3 « usurpation », HC4 « taxe de
> déplacement », HC5 « contre-mesures », HC6 « le g bénin prédit la robustesse », L « lemme d'additivité », T « théorème
> négatif », Tr « transposition token → action », dans leurs énoncés retenus (décisions N-013 et suivantes), et n'en est ni
> un cas particulier ni une conséquence ; (2) une table « si vraie / si fausse » montre qu'au moins une issue change un
> critère d'une porte (G0 instruments ; G1 boîte blanche séquentielle contre meilleure boîte noire ; GC porte du papier C ;
> G2 fragmentation et statistique de population ; G3 environnement à vérité différée) ou une bascule du § 13, et qu'aucune
> expérience déjà prévue ne tranche ce point ; (3) son devis tient sous le plafond fixé par Lazar, sur les environnements et
> organismes existants, sans mode adversarial nouveau ; (4) son expérience est dimensionnée sur la borne basse de l'effet.
> Sinon elle est renvoyée avec l'un des codes : « couverte par Hx », « non décisive », « coût hors borne », « antériorité
> prise ».

**Lecteur** : un lecteur neuf (R13) reçoit la règle (empreinte), le dossier de la promue (fiche, loi, verdicts, tranche,
estimation et intervalle), la table des signatures des hypothèses du programme, la table des portes et des bascules ; rend
une ligne d'une liste fermée ; verdict scellé ; puis préenregistrement (R1), contre-lecture (R2), devis, **ton GO** (nœud).
La promotion par le pôle reste un criblage : elle n'est jamais citée comme preuve pour une porte.

### (e) Garde de diversité et comptabilité du coût par survivante

- **Diversité** : lignées tracées ; quota d'un tiers des places de parents par lignée ; 30 % d'immigrants ; nombre effectif de
  lignées (alarme sous 3 → plus d'immigrants à la génération suivante, règle écrite d'avance) ; grille de cellules suivie ;
  sélection des parents pondérée à l'inverse de leur nombre d'enfants (option).
- **Coût** : grand livre par fiche, par rôle et par génération (appels, jetons, dollars par relais, heures de carte, épisodes de
  tranche au prix déclaré, minutes, nœuds) ; coût par promue neuve avec intervalle exact de Poisson ; entonnoir complet ;
  coût par fiche testée ; tout est scellé avec le journal de la génération. **Ordre de grandeur illustratif par génération**
  (30 fiches, effet cible 0,6) : course ≈ 37 dollars (course 1, 29 fiches, dossier factuel § 10) ; pont ≈ 2 à 9 dollars ;
  tests de mort ≤ 0,5 dollar par fiche plus le lecteur ; pôle ≈ 0,5 dollar par fiche jugée (lancement « (a) bis » : 5,89
  dollars pour 11 fiches) ; tranche ≈ 16 à 60 dollars. Soit **≈ 60 à 120 dollars par génération**, et, pour 1 à 3 promues,
  **≈ 20 à 120 dollars par promue** ; sans borne si aucune.

### (f) Ablation préenregistrée « génération 2 avec et sans filtre du pôle »

**Dessin principal recommandé : témoin interne d'immigrants** (sans dépense de plus).
- Question : des parents promus par le pôle donnent-ils plus de fiches promues sur tranche fraîche que des fiches sans
  parents ?
- Unité : la fiche. Bras : filles (21 par génération de 30) contre immigrants (9), **même tranche, même m, même e-BH**.
  Affectation des appels de proposeurs aux deux rôles par graine (`SeedSequence`, entropie = empreinte du préenregistrement et
  valeur engagée de session-depot ; une clé de dérivation par génération, par rôle, par tirage de parents, par ordre secret).
  Les sorties des modèles ne sont pas réglables par graine : la variance irréductible impose des répétitions.
- Métrique primaire M1 : part promue (filles contre immigrants), test exact de Fisher unilatéral sur les comptes cumulés ;
  secondaire M2 : test des rangs sur log W final ; rapportée M3 : promues neuves par dollar.
- Puissance (annexe F) : filles vraies à 25 % contre 5 % : 0,49 après 2 générations, 0,83 après 4, 0,96 après 6 ; à 15 % :
  0,12, 0,34, 0,54 (0,78 après 10) ; à 10 % : 0,02, 0,10, 0,17.
- **Prédiction signée et chiffrée** (à confirmer au scellement) : part promue des filles supérieure à celle des immigrants,
  écart +0,05 (intervalle −0,05 à +0,15) ; confiance 0,4 — rien ne montre aujourd'hui que des lignées fécondes existent hors
  du monde simulé (la démonstration v5 les a construites).
- Témoins plantés, identiques dans les deux rôles : 5 vrais, 5 faux, 3 triviaux, 3 redites plantées (copies de promues de
  g − 1) ; vérité connue ; ils valident la mesure (dents, mémoire), ils ne sont pas la métrique.
- Critères de lecture gelés : moins de 3 promues en génération 1 → « non jugeable » (déclaré d'avance) ; un témoin faux promu
  ou aucun vrai promu → « pas de dents », non lu ; p ≤ 0,05 → « la sélection par l'expérience sert » ; p ≤ 0,05 dans l'autre
  sens → « elle nuit » ; sinon « non concluant, puissance atteinte X ». Symétrie (R4) : un résultat très net dans un sens ou
  dans l'autre déclenche le même audit (comptes par génération, empreintes des tranches, entrelacement des appels).
- Liste d'arrêt : tranche ouverte avant le gel ; modèle servi changé (A2) ; témoins en désaccord entre rôles ; dépense hors
  plafond.
- Lecteur neuf (R13). **Dessin à deux bras** (ta demande) : seulement si tu acceptes 80 à 160 fiches par bras (2 à 4 fois le
  coût d'une génération), bras de comparaison « parents choisis par les juges », même tranche ; à 20-40 par bras, seulement en
  description exploratoire, jamais lu comme un test.

### (g) Ce qui change dans l'orchestrateur v56

Couche **v57** neuve (règle R12 : aucun fichier v56 modifié) :

| module | rôle | s'appuie sur |
|---|---|---|
| `pole/selection_generations_v57.py` | machine à cinq états ; `m_fixe` = fiches entrées au pôle + témoins faux ; appelle `cycle.appliquer_multiplicite` inchangé ; journal des états scellé ; « sélection par l'expérience : vide » sans repli | `cycle.py`, `pari_apparie.ebh_pondere` |
| `pole/tranches_epreuve_v57.py` | registre des tranches (scellée, épreuve de g, rétrogradée) ; refus d'ouvrir avant le gel, de rejuger sur une rétrogradée ; découpage groupé par tâche vérifié ; disjonction avec la tranche des tests de mort ; alimente le registre des lectures du pont | `monde_banque.py`, `pont_v1.garde_retrodiction` |
| `pole/heritage_v57.py` | remplace le texte d'héritage v54 (titre, résumé, « notable ») par les états ; refuse tout score de juge, rang ou information de tranche non rétrogradée | `course2_v54.texte_heritage`, `memoire.py` |
| `pole/memoire_v57.py` | preuve héritée cumulée seulement entre tranches distinctes (identifiant de tranche dans la classe) | `memoire.py` (signature prédictive, seuil 0,30 nat) |
| `pole/diversite_v57.py` | lignées, quotas, immigrants, nombre effectif de lignées, cellules | `recombinaison.py` (tirage stratifié, marchepieds) |
| `pole/tests_de_mort_v4.py` | témoin de sévérité (rejeu sur issues permutées) ; correspondance des trois verdicts vers les cinq états ; rien d'autre ne change | `tests_de_mort_v3.py`, `etage_entre_generations_v56.py` (machine jetable par liste blanche) |
| `pole/e_mort_v57.py` (option) | e-processus de mort contre la famille des fractions de la loi | `selection_pari.trajectoire_numerateur` |
| `pole/comptabilite_v57.py` | grand livre et entonnoir ; recoupe `consommations.json` | `budget_v56.py` |
| `pole/sortie_programme_v57.py` | dossier fermé du lecteur de sortie ; table des signatures des hypothèses (par le pont) ; table des portes | `pont_v1.py` |
| `pole/ablation_filtre_v57.py` | lecture après coup sur l'archive (forme de `ablation.py`) | `ablation.py` |
| `configuration_v57`, `gardes_e0_v57.py` | niveau, fractions par défaut pour les fiches du pont, quotas, part d'immigrants, tailles de tranche — **aucun défaut** ; une ligne R5 (cas sain et artefact) par garde neuve | v56 |

**Inchangés** : juge figé (`selection_pari`, `pari_apparie`, `engagement_apparie`, `nul_filles_v2`), règle e-BH, mondes sur
banque, bac à sable, aiguilleur, juges de la course, bisociateur, budget v56.

### (h) Décisions pour toi

**D-S1 « cinq états »** — Décision : quelle règle de survie geler ? Enjeu : qu'aucune idée non validée ne se reproduise, sans
enterrer des idées vraies jugées sur trop peu d'épisodes. Options : (a) **ta conjonction à deux états** (survit au test de
mort et promue) — avantage : simple ; inconvénient : « non concluante » et « morte » confondues, mémoire faussée, et une fiche
sans données de test de mort ne peut jamais être promue ; (b) **cinq états, seule la promue se reproduit, promue = retenue
par le pôle et non tuée par un test de mort** — avantage : chaque fiche a un sort écrit ; inconvénient : sans tranche fraîche,
aucun parent (la boucle s'arrête) ; (c) (b)
plus des **parents provisoires** (survivantes des tests de mort à sévérité vérifiée) tant qu'aucune tranche n'existe, jamais
vers le programme — avantage : la boucle tourne ; inconvénient : sélection par un seuil choisi par l'auteur. Recommandation :
(b), confiance 0,6. Défaut sous 48 heures : (b).

**D-S2 « niveau du criblage »** — Décision : à quel niveau la règle e-BH promeut-elle par génération ? Enjeu : puissance contre
fausses promotions servies à la génération suivante. Options : (a) **0,05 par génération** (codé) — avantage : rien à
changer ; inconvénient : pas de garantie sur toute la suite ; (b) 0,10 — avantage : +5 à 10 points à tranche courte ;
inconvénient : plus de parents faux ; (c) 0,05 plus contrôle en ligne sur la suite (e-LOND) — avantage : garantie globale ;
inconvénient : à coder, puissance décroissante. Recommandation : (a), confiance 0,7. Défaut sous 48 heures : (a).

**D-S3 « pari à fraction pour les fiches du pont »** — Décision : quel numérateur pour une loi traduite ? Enjeu : une fiche qui
déclare un effet double du vrai demande au pari plein 1 367 épisodes au lieu de 330 (m = 30), au pari à fraction 380.
Options : (a) plein (défaut actuel) — avantage : 8 % d'épisodes en moins si l'effet déclaré est juste ; inconvénient : ruine
sur effet surestimé ; (b) **fractions pour
toutes les fiches du pont** — avantage : robuste (n80 380 contre 1 367 à m = 30) ; inconvénient : +8 % d'épisodes si l'effet
est juste ; (c) fractions partout — avantage : uniforme ; inconvénient : change le comportement des fiches existantes.
Recommandation : (b), confiance 0,7. Défaut sous 48 heures : (b).

**D-S4 « tranche fraîche par génération »** — Décision : quelle règle de renouvellement ? Enjeu : propreté de l'épreuve contre
coût en données. Options : (a) **banque croissante** (neuve par génération, rétrogradée après lecture) — avantage : épreuve
propre, héritage libre ; inconvénient : 330 à 1 300 épisodes par génération ; (b) rotation entre K tranches scellées
d'avance — avantage : production en une fois ; inconvénient : nombre de générations borné par K ; (c) réutilisation corrigée
par transcription — avantage : coût voisin à 3 générations (826 contre 990 épisodes à effet 0,6) ; inconvénient : seul
l'ensemble des retenues peut être servi. Recommandation : (a), et (b) comme forme de production ; confiance 0,75. Défaut sous
48 heures : (a). La production des tranches est une dépense (D-S8).

**D-S5 « ce qu'on hérite »** — Décision : que servir aux proposeurs de g + 1 ? Enjeu : ne pas reproposer sans s'ancrer ni
apprendre à contourner le test. Options : (a) le texte actuel (titre, résumé, « notable ») — avantage : codé ; inconvénient :
c'est une sélection par le jugement ; (b) **états et codes de raison, sans score ni rang** — avantage : conforme à ton
objectif ; inconvénient : à coder (v57) ; (c) (b) plus une ablation de l'héritage dans la génération — avantage : mesure
l'ancrage ; inconvénient : la moitié des appels sans liste des mortes. Recommandation : (b), et (c) dès la génération 2 ;
confiance 0,6. Défaut sous 48 heures : (b).

**D-S6 « règle de sortie »** — Décision : adopter la règle écrite de la section d ? Enjeu : qu'une hypothèse du programme ne
naisse pas d'un criblage seul. Options : (a) **règle à quatre conditions, lecteur neuf, puis ton GO** — avantage : traçable ;
inconvénient : lente ; (b) toute promue va au préenregistrement — avantage : rapide ; inconvénient : hypothèses en double,
portes lues sur du criblage ; (c) aucune sortie avant une version 3 du programme — avantage : programme stable ;
inconvénient : la boucle ne sert à rien. Recommandation : (a), confiance 0,7. Défaut sous 48 heures : (a). Chaque sortie
reste un nœud (modification d'hypothèse).

**D-S7 « diversité »** — Décision : quelle garde contre l'effondrement sur une lignée ? Enjeu : diversité contre force de la
sélection. Options : (a) **quota d'un tiers par lignée et 30 % d'immigrants** — avantage : simple, sert aussi de témoin ;
inconvénient : 30 % de fiches sans héritage ; (b) grille MAP-Elites — avantage : diversité structurée ; inconvénient : il faut
plusieurs générations pour remplir la grille ; (c) rien — avantage : sélection maximale ; inconvénient : effondrement.
Recommandation : (a), (b) à partir de la génération 3 ; confiance 0,6. Défaut sous 48 heures : (a).

**D-S8 « tranches : devis »** — **Nœud (dépense).** Décision : faire produire par session-depot une partie de calibrage et trois
tranches scellées d'environ 350 épisodes (effet cible 0,6), soit ≈ 1 000 à 1 400 épisodes ? Enjeu : sans tranche fraîche,
aucune promotion n'est possible (constat du pont). Options : (a) **sur la couche 2 (banque avec sabotage)**, adossé à son pilote
— avantage : épreuve du programme ; inconvénient : ≈ 50 à 250 dollars selon le prix par épisode (illustratif), dépend du
pilote de couche 2 ; (b) épisodes honnêtes seulement (banque sœur de celle de la tâche T0.5 : notes de juges sur des tâches
de recherche, 13 moniteurs) — avantage : moins cher ;
inconvénient : seules les fiches sur les juges sont testables ; (c) attendre — avantage : rien ; inconvénient : la course 2
promeut zéro fiche. Recommandation : (a), confiance 0,6. Aucun défaut : j'attends ton mot.

**D-S9 « ablation »** — **Nœud (dépense, dessin).** Décision : quel dessin pour mesurer l'utilité de la sélection par
l'expérience ? Enjeu : à 20-40 fiches par bras, le test ne peut rien dire. Options : (a) ton dessin à deux bras, 20-40 par bras
— avantage : rapide ; inconvénient : puissance 0,02 à 0,25 si le filtre double la part de fiches vraies ; (b) deux bras de 80 à 160 — avantage : test réel en une
génération ; inconvénient : 2 à 4 fois le coût d'une génération ; (c) **témoin interne d'immigrants**, lu après 4 à 6
générations — avantage : sans dépense de plus ; inconvénient : lent. Recommandation : (c), (a) en description seulement ;
confiance 0,65. Aucun défaut : j'attends ton mot.

### (i) Ordre et dépendances (devis **illustratif**)

| étape | dépend de | qui | coût illustratif | nature |
|---|---|---|---|---|
| 0. Contre-lectures (R2) du pont v1 et de cette conception ; simulation v57 de la machine à états, du témoin de sévérité, de l'e-processus de mort | — | conv-audit, sous-agents neufs | 0 | routine |
| 1. Premier essai du pont (décision D-P5 du pont : 10 fiches de la course 1 + 6 témoins) | 0 | session-depot | 1 à 4 dollars, plafond 5 | nœud |
| 2. Tests de mort activés : essais de bac réel sur la machine louée jetable (liste blanche v56), puis 10 fiches avec témoin de sévérité et témoins vrais pour le taux de fausse mort | 0 | session-depot | ≈ 6 dollars + quelques heures de machine | nœud |
| 3. Tranches fraîches (D-S8) : calibrage + 3 tranches | pilote de couche 2 | session-depot | ≈ 50 à 250 dollars | nœud, **chemin critique** |
| 4. Course 2 = génération 1 (GO de 160 dollars déjà donné) | pré-pilote | session-depot | ≤ 160 dollars | décidé |
| 5. Pôle sur la tranche 1 (sortie 1 attendue : 5 à 15 % des fiches, estimation du pont) | 1, 3, 4 | session-depot | ≈ 0,5 dollar par fiche jugée | nœud (petit) |
| 6. Génération 2 avec immigrants (témoin interne) ; héritage v57 | 5, couche v57 | session-depot | ≈ 40 à 160 dollars | nœud |
| 7. Lecture de sortie (R13) des promues ; ton GO | 5 ou 6 | lecteur neuf, toi | 0 | nœud |

Sans l'étape 3, les étapes 5 à 7 sont vides : c'est la dépendance qui décide du calendrier. Ordre de grandeur des générations 1
et 2 : ≈ 150 à 600 dollars, dont la course elle-même et les tranches sont les plus grosses parts.

---

## Annexe — calcul de puissance

**Fichiers** : `calcul-puissance-selection-v1.py` (`435a95ec8d0fc9d58ab3429e4e7bd458f8fa1c5347fa060abce14e89531023c5`) et sa
sortie `calcul-puissance-selection-v1-sortie.txt` (`9d3043289a87f11c6a1cad57692716d8c5a5de176c848ef9a81b869fecac8e74`).
**Rejouer** : `cd "$(mktemp -d)" && python3 -I <chemin>/calcul-puissance-selection-v1.py > sortie.txt` ; Python 3.13.18,
numpy 2.5.3, ≈ 14 secondes. **Rejoué deux fois** depuis deux dossiers temporaires neufs : sorties identiques octet pour octet
(empreinte `9d304328…`) ; une exécution d'essai antérieure, avant le retrait de deux lignes mortes du script, donnait déjà la
même sortie. Graines : `numpy.random.SeedSequence`, entropie = SHA-256 du
nom du calcul, une clé de dérivation par tâche (règle R9 : graines dérivées par tâche, consignées).

**Monde simulé** : issue binaire, un trait gaussien, loi vraie P(y = 1 | z) = σ(β·z) ; fiche nulle : même forme affirmée,
issue indépendante du trait ; bibliothèque aveugle du juge v1 réécrite en numpy (urne ; moyennes glissantes 5, 10, 20, 50 à
lissage 0,5 ; uniforme et marginale ajustée dominées par l'urne) ; numérateurs « plein » et « fractions » (grille 0,25 à 1,
marginale en ligne) ; e-valeur arrêtée à m/α comme `appliquer_multiplicite`. Réservoirs de 2 000 trajectoires, générations
formées par tirage avec remise (2 000 par case).

**Résultats** (sections de la sortie) :
- **Contrôles du calcul** (cas sains) : une fiche nulle franchit 1/α sur 1 800 épisodes avec probabilité 0 à 0,0025 (garantie :
  ≤ 0,05) ; taux de fausses découvertes sous e-BH ≤ 0,006 partout.
- **A** : puissance par fiche et n80 (tableau de la section a).
- **A bis — recoupement du pont** : l'approximation du pont (n ≈ 2·log(m/α) / information mutuelle) donne 151, 293 et 551
  épisodes (effet 0,6 à m = 1 ; 0,6 à m = 17 ; 0,3 à m = 1), les nombres du pont ; la simulation donne n80 = 215, 307 et 886.
  **Divergence** : à m = 1 l'approximation est optimiste de 34 à 61 % ; à m ≥ 17 et effet ≥ 0,6 elle tient à 5 % près.
  Elle oriente vers la sortie 2, jamais vers une promotion : sa logique n'est pas touchée, ses effectifs requis à m petit
  sont à relever.
- **B** : coût du renouvellement (Q2).
- **C** : génération entière (section a) ; sensibilité à effet 0,3 : à 600 épisodes, part des vraies retenues 0,19 à 0,26 ; à
  1 800, 0,94 à 0,95.
- **D** : tests de mort en filtre (taux illustratifs : une nulle sur deux tuée, une vraie sur dix) : m passe de 30 à 16 en
  moyenne ; puissance 0,77 → 0,73 (300 épisodes), 0,98 → 0,89 (600).
- **E** : ablation à deux bras (Q6) ; **F** : témoin d'immigrants (section f).

**Ce que le calcul ne dit pas** : la puissance sur les vrais moniteurs (plus de deux issues, nul informé plus fort que la
marginale, effets hétérogènes — tout cela demande plus d'épisodes) ; les parts réelles de fiches vraies ; les taux réels des
tests de mort. Ce sont des ordres de grandeur et des rapports, pas des devis.

---

## Pièces lues (SHA-256 calculés ici)

| pièce (depuis la racine du dépôt ; [P] = `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/`) | SHA-256 |
|---|---|
| [P]`selection-generations-v1/question-selection-generations-v1.md` (entière) | `c899221888d14e2df0640ac1b405cef286ca3bd84b45bec998519ac53fccbfcd` |
| `docs/notes/ideation-organisme-v1/explication-organisme-v1/dossier-factuel-organisme-v1.md` (§ 1, 6, 9, 10, 11, réserves) | `0751fc8cf4aa0a9eaccb23d80cb06220fa3db9805092bd1d854bc68fce7ae250` |
| [P]`integration-proposeurs-ia-v1.md` (§ 0 à 3) | `974b2dbe17b76975f8e9198f5852a36513f8a428b44874740e31395b34124184` |
| [P]`programme-conception-organisme-v7.md` (l. 1-60) | `b7cd2f56bf99357caf51493ca0ed966753711926c91c094f971197b29c7192fd` |
| [P]`premier-lancement-reel/lecture-lancement-reel-a-bis-v1.md` | `cc475e042c15870e526ce322997dcec801652a9cfd79f3020d00f2bca538d9e4` |
| [P]`demonstration-couche1-v7/lecture-couche1-v7-v2.md` | `e2946dd65c573fa00ce8eac90bf1640269b1a800efe6531adb2a9cce108d2c9e` |
| [P]`demonstration-cycle-v5/lecture-demonstration-cycle-v5-v1.md` | `60345b906006b7cfd0381354a2d19ead86a0e659f8d03a7a39b636f5cda440b4` |
| [P]`pont-fiche-loi-v1/conception-pont-fiche-loi-v1.md` (entière) | `5161e199e15dacc728d4b2e7b1769f700e0a293c05fb26d402dfe40d25c4a974` |
| [P]`pont-fiche-loi-v1/pont_v1.py` (en-tête, `puissance`, `traduire_fiche`) | `9fb2d9366e7764d4fc810b921e8565ca2dcae9af5f1b30ec8866efeb5d3eb692` |
| [P]`pont-fiche-loi-v1/LISEZMOI-pont-v1.md` | `7b1c131db760014798af159047849163bedc03b706f2f684dd0962ac4d6bd17a` |
| [P]`erratum-multiplicite-e-bh-v1.md` | `cdf800e95ca78db2b5d08a59d497f28a543380e6a47e9978d7be43858d9aff44` |
| [P]`couche-2-conv-audit-v1/comparaison-couche-2-deux-lignees-v1.md` (l. 36-41) | `a2450b5196c6454868c6fd5b0b5ce013609d0332cf5063e5dd3660fcbf65e17f` |
| [P]`couche-2-conv-audit-v1/decision-pilote-couche-2-v5.md` (lignes de coût) | `255a364e710cd713fc37dd5f84845139a2eb8c15d4b7c13ce49ae46ccd0143f8` |
| `docs/programme-controle-ia-v2.md` (§ 5, 10, 13) | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` |
| `docs/decisions/decision-N-013-v1.md` | `157d388ef5d0f4dff00a5a1801316ed0677959a0709b4575b875e089d11ab7be` |
| `docs/decisions/decision-N-035-v1.md` | `55df073d6918405949f3543308f0de7f90293baeefc5a4525e5f49697b2517e6` |
| `docs/notes/ideation-organisme-v1/orchestrateur-v56/LISEZMOI-orchestrateur-pole-v7-v56.md` | `3e32709ad5f46016461b10b4ab8594e657433d36272f555c07c4f7f97e43d506` |
| `…/orchestrateur-v56/pole/cycle.py` (`appliquer_multiplicite`) | `798f039042e3ee1f18df5c566f5a0ddee5dac5c98225c8ce621e267174c8ee18` |
| `…/orchestrateur-v56/pole/pari_apparie.py` (`ebh_pondere`) | `ec6c2cf64d0c9a3bcb3484f2bc58ca986c89e97829bd45fdb96cbc42bf094fef` |
| `…/orchestrateur-v56/pole/selection_pari.py` (en-tête, bibliothèque, numérateur à fraction) | `359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc` |
| `…/orchestrateur-v56/pole/memoire.py` (en-tête) ; `memoire_v53.py` (en-tête) | `71f1d086…` ; `43b01b43…` |
| `…/orchestrateur-v56/pole/recombinaison.py` (en-tête) ; `ablation.py` (en-tête) | `71faad38…` ; `54373707…` |
| `…/orchestrateur-v56/pole/tests_de_mort_v2.py` (en-tête) ; `tests_de_mort_v3.py` | `363a3725…` ; `ea05eb55…` |
| `…/orchestrateur-v56/pole/etage_entre_generations_v53.py` ; `course2_v54.py` (`texte_heritage`) | `d568d25b…` ; `ac1980d0…` |

Le dossier `pole/` déplié dans le dépôt porte les mêmes empreintes que celles que le LISEZMOI du pont lit dans l'archive v56
(`pari_apparie.py`, `selection_pari.py`, `tests_de_mort_v2.py`, `tests_de_mort_v3.py`) ; je ne l'ai pas recoupé fichier par
fichier avec `EMPREINTES-orchestrateur-pole-v7-v56.txt`.

## Choix pris seuls (à relire)

Cinq états plutôt que trois ; témoin de sévérité par permutation ; e-processus de mort en option ; quota d'un tiers ; 30 %
d'immigrants ; alarme sous 3 lignées effectives ; effet cible 0,6 pour dimensionner les tranches ; 3 promues au minimum pour
qu'une ablation soit jugeable ; bras de comparaison « juges » plutôt que « hasard » ; transcription de fuite limitée à 3
retenues ; taux des tests de mort et parts de fiches vraies illustratifs.

## Réserves

1. Exploratoire : monde binaire à un trait, effet homogène, nul = marginale ; la bibliothèque du juge est **réécrite** en numpy
   d'après la lecture de `selection_pari.py`, pas exécutée depuis le code v56 : un recoupement sur quelques trajectoires contre
   l'évaluateur v56 reste à faire (R4).
2. Coût par épisode : deux estimations du simple au quadruple (0,047 et ≈ 0,18 dollar) ; tous les dollars sont illustratifs.
3. La question cite HC1 à HC5 ; le programme compte aussi HC6, L, T, Tr, H4′, H8, et H9 (décision N-035) : la règle de sortie
   les inclut.
4. Lecture de la règle N-053 (aucun score dans la sélection de l'agent) comme portant sur les agents, pas sur les fiches :
   à confirmer.
5. Antériorités non lues sur PDF ; identifiants contrôlés par recherche sur la toile pour AlphaEvolve, la machine de Gödel
   darwinienne, LLM-SR, POPPER, ShinkaEvolve, e-LOND, e-BH renforcée et fermée, Ladder, « reusable holdout », RST ; contenus
   décrits de mémoire, non opposables.
6. Non lus : `decisions-en-attente-lazar-2026-10-31-v1.md`, le registre `registres/decisions.md`, le préenregistrement du
   pré-pilote (brouillon 10) : une décision déjà prise peut contredire une option ici.

Horodatage : écrit le 2026-11-01 à partir de 09:50:58 UTC (relevé `date -u` avant toute lecture).
