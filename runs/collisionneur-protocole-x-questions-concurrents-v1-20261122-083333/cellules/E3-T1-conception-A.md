# Proposition A — Tour III.1 : conception ciblée à l'aveugle

## 0. État des pièces

- **Pièce absente :** la question dit « on vous remet une liste de ces publications », mais aucune liste ne figure dans ce qui m'est transmis. Je n'en invente ni les titres, ni les auteurs, ni le contenu.
- **Bloc FAITS :** il reproduit la question, avec la même empreinte que le bloc QUESTION. Il ne contient aucun fait porteur d'un statut VÉRIFIÉ, RAPPORTÉ ou OBSERVÉ-NON-AUDITÉ.
- **Notes retirées :** l'en-tête signale des « notes de Fable retirées ». Je n'ai pas leur contenu et je ne le suppose pas.
- **Conséquence :** l'extraction demandée « pour chacune » n'est pas exécutée. Je livre le protocole qui la rendrait vérifiable et les expériences qui diraient si ses instruments fonctionnent.
- **Statut de mes ajouts :** tout ce que j'avance ci-dessous est HYPOTHÈSE. Tous les chiffres (seuils, effectifs, durées, coûts) sont **illustratifs**, aucun ne vient des faits.
- **Références :** je ne nomme aucune publication du domaine. Sans la liste, tout nom serait une conjecture sur son contenu (références à vérifier une fois la liste fournie).
- **B1 :** tour à l'aveugle, je ne vois aucune autre proposition. Rien n'est repris ni critiqué.

---

## (a) Ce que la question suppose sans que ce soit établi

Aucun de ces points n'a de statut dans la pièce. Je les traite tous comme HYPOTHÈSE.

| # | Présupposé | Ce qui manque pour l'établir |
|---|---|---|
| P1 | Une liste existe, elle est stable et elle est représentative du domaine. | La liste elle-même. Même fournie, une liste ne prouve pas sa propre couverture. |
| P2 | « Plusieurs équipes publient » sur ce sujet, et les agents « pourraient dégrader » le résultat. | Rien dans la pièce ne dit si cette dégradation est observée, provoquée par consigne ou seulement envisagée. |
| P3 | Le texte seul permet de séparer trois catégories : non-fait reconnu, intention annoncée, ouvert pour tous. | Un accord entre annotateurs indépendants, jamais mesuré ici (expérience E1). |
| P4 | « Ouvert pour tous » a un sens unique. | L'expression est ambiguë : *problème ouvert à la communauté* ou *artefact publié en accès ouvert* (code, tâches, trajectoires). Je code les deux séparément. |
| P5 | Les manques reconnus sont les manques réels et importants. | Le texte seul ne révèle, par construction, aucun manque non reconnu. Une section « limites » peut être sincère, rituelle ou stratégique. |
| P6 | Une intention annoncée renseigne sur ce que l'équipe fera, donc sur le risque d'être devancé. | Un suivi rétrospectif (E3). |
| P7 | Un manque est un objet discret dont on peut dire « comblé » ou « non comblé ». | Une définition opératoire de « comblé » : même objet, mêmes conditions, même métrique. |
| P8 | On peut vérifier qu'un manque n'a *pas* été comblé. | C'est une preuve d'absence. Au mieux on obtient « non trouvé par la procédure P à la date D », avec un rappel de P mesuré (E2). |
| P9 | Une équipe aux moyens limités peut combler utilement certains de ces manques. | Un résultat sur des modèles ouverts, plus petits, doit se transposer aux agents visés par les publications. C'est une hypothèse de transfert à écrire noir sur blanc. |
| P10 | Il existe des observations précoces qui distinguent un bon choix d'un mauvais. | Une définition de « bon choix » indépendante de l'issue (voir E4). Sinon on confond bon choix et résultat positif. |
| P11 | La « surveillance » fait mieux que des vérifications mécaniques du résultat final. | Une comparaison directe à taux de fausses alertes fixé (E5). |

---

## (b) Expériences décisives

Convention commune : chaque élément extrait ou jugé est accompagné d'une citation littérale, dont la présence dans la source se vérifie par recherche de chaîne exacte. Tout protocole est écrit et horodaté avant la collecte.

### E1 — La trichotomie est-elle extractible du texte seul ?

- **H_A :** deux lecteurs indépendants classent les mêmes passages dans les mêmes catégories (quatre étiquettes, P4 dédoublé), et un extracteur automatique fait mieux qu'un filtre par mots-clés.
- **H_B :** les catégories ne se séparent pas de façon fiable, ou le filtre par mots-clés suffit.
- **Métrique :** kappa entre deux annotateurs humains au niveau du passage ; F1 de l'extracteur contre un étalon arbitré ; écart de F1 avec le filtre mécanique.
- **Seuil (illustratif) :** κ ≥ 0,6 ; écart de F1 ≥ 10 points, intervalle à 95 % excluant 0.
- **Contrôles négatifs :**
  - des textes hors domaine, sur lesquels l'extracteur doit rendre « rien » ;
  - des phrases-leurres où les auteurs décrivent la limite d'un *autre* travail, à ne pas leur attribuer ;
  - les mêmes textes amputés de leurs sections « limites » et « perspectives », pour vérifier que l'extracteur ne fabrique rien.
- **Issues :**
  - κ < 0,4 (illustratif) falsifie H_A. La première tâche de la question n'est alors pas opératoire telle quelle, et les étiquettes doivent être fusionnées ou redéfinies avant tout classement.
  - κ au-dessus du seuil avec écart de F1 nul falsifie l'utilité de l'extracteur, et le filtre mécanique suffit.
  - κ au-dessus du seuil avec écart établi falsifie H_B.

### E2 — « Non comblé ailleurs depuis » est-il vérifiable par une procédure bornée ?

- **Préalable :** chaque manque est mis en fiche à quatre champs (objet, condition, métrique, seuil ou comparaison). Un travail tiers « comble » le manque s'il couvre les quatre champs. Sinon il est noté « abordé partiellement ».
- **H_A :** une procédure bornée retrouve la grande majorité des comblements réels. Elle comprend quatre recherches :
  1. les citations descendantes de la publication ;
  2. une recherche sémantique sur la fiche ;
  3. les travaux ultérieurs de la même équipe ;
  4. les dépôts et bancs d'essai associés.
- **H_B :** les comblements se trouvent surtout là où la procédure ne va pas (travaux qui ne citent pas la source, vocabulaire différent, résultats non publiés). « Non trouvé » ne renseigne alors presque pas.
- **Plan :** test rétrospectif sur une cohorte antérieure, à condition que la liste en contienne une. Des experts établissent, sans limite de moyens de recherche, quels manques de la date T0 sont comblés à T1. La procédure est ensuite exécutée à l'aveugle.
- **Métrique :** rappel sur les manques comblés selon l'étalon ; taux de « comblé » déclaré à tort.
- **Seuil (illustratif) :** rappel ≥ 0,8, borne basse de l'intervalle ≥ 0,65 ; faux « comblé » ≤ 0,1.
- **Contrôles :**
  - négatif : des fiches fictives, plausibles mais inventées, que la procédure ne doit pas déclarer comblées ;
  - positif : des sentinelles, manques dont le comblement est connu des arbitres, mêlées à l'aveugle.
- **Issues :**
  - Rappel < 0,5 (illustratif) falsifie H_A. La question « comment vérifier » reçoit alors une réponse négative : on ne peut que dater une absence de trouvaille, et le critère de choix doit intégrer un risque résiduel d'être devancé.
  - Rappel au-dessus du seuil falsifie H_B. La procédure devient un instrument dont le rappel est connu.
- **Dans les deux cas,** la sortie s'écrit « non trouvé au [date], requêtes [liste], rappel mesuré [valeur] », jamais « non comblé ».

### E3 — Une intention annoncée prédit-elle le comblement par la même équipe ?

- **H_A :** les manques que les auteurs annoncent vouloir traiter sont comblés par eux, dans un délai donné, nettement plus souvent que ceux déclarés ouverts à tous.
- **H_B :** aucune différence, l'annonce est rituelle.
- **Métrique :** différence de taux de comblement par l'équipe d'origine à 12 mois (illustratif), sur la cohorte rétrospective de E2.
- **Seuil (illustratif) :** différence ≥ 20 points, intervalle excluant 0.
- **Contrôle négatif :** permutation des étiquettes « annoncé » et « ouvert » (la différence doit s'annuler), et appariement par année de publication.
- **Issues :**
  - H_A retenue falsifie l'idée qu'un terrain annoncé est libre. Le critère « éviter l'annoncé » est alors soutenu.
  - H_B retenue falsifie ce critère : l'appliquer écarterait des sujets sans raison.
- **Limite :** si la liste ne contient pas de cohorte assez ancienne, E3 n'est pas faisable et le critère reste HYPOTHÈSE.

### E4 — Les observations précoces discriminent-elles un bon choix d'un mauvais ?

**Définition préalable.** Un choix est « bon » si, dans le budget, il produit un résultat réfutable, positif ou négatif, qui n'a pas été devancé et dont le protocole avait été écrit avant. L'issue positive n'entre pas dans la définition.

**Observations précoces candidates (toutes HYPOTHÈSE),** mesurables pendant un pilote court :

- **O1 :** la référence publiée est reproduite dans son intervalle.
- **O2 :** la variance du pilote donne un effectif nécessaire inférieur au budget.
- **O3 :** les vérifications mécaniques ne saturent pas, il reste des cas qu'elles manquent.
- **O4 :** des cas honnêtes appariés existent, et le taux de fausses alertes est mesurable.
- **O5 :** la procédure de E2, relancée, ne trouve rien.
- **O6 :** les deux issues ont été écrites à l'avance et chacune falsifie quelque chose.
- **O7 :** l'effet du pilote survit à un changement de graine et à une reformulation de consigne.

**Duel.**

- **H_A :** un score fixé à l'avance (nombre d'observations satisfaites, sans ajustement) prédit le « bon choix » sur une cohorte de projets passés.
- **H_B :** il ne prédit rien au-delà d'un prédicteur trivial (moyens de l'équipe, nombre de citations de la publication source à T0).
- **Métrique :** AUC du score, et écart d'AUC avec le prédicteur trivial.
- **Seuil (illustratif) :** AUC ≥ 0,70, borne basse > 0,5 ; écart > 0 avec intervalle excluant 0.
- **Contrôle négatif :** étiquettes permutées (AUC ≈ 0,5 attendu).
- **Issues :**
  - H_B retenue falsifie la prétention des observations à guider le *choix*. Elles ne valent plus que comme critères d'arrêt internes.
  - H_A retenue falsifie l'idée que seuls les moyens décident.
- **Réserve :** l'étude est corrélationnelle et la cohorte sera petite. Pour une équipe unique (n = 1), ces observations ne sont pas validables. Elles sont des règles d'arrêt, pas des preuves.

### E5 — Au niveau de l'objet : la surveillance apporte-t-elle quelque chose, et la longueur la dilue-t-elle ?

C'est l'expérience qu'une équipe aux moyens limités peut mener elle-même. Elle sert aussi de gabarit pour vérifier qu'un manque est réel.

**E5a — Apport au-delà du mécanique.**

- **H_A :** à taux de fausses alertes fixé, un surveillant qui lit la trajectoire détecte des dégradations que les vérifications mécaniques manquent.
- **H_B :** ses détections sont incluses dans celles des vérifications mécaniques, ou elles tiennent à des indices de surface (l'agent verbalise sa consigne).
- **Métrique :** taux de détection à fausses alertes fixées à 5 % (illustratif), sur le sous-ensemble des dégradations manquées par le mécanique.
- **Seuil (illustratif) :** détection incrémentale ≥ 15 points, intervalle excluant 0.
- **Contrôles négatifs :**
  - des échecs honnêtes appariés sur la qualité finale. Si le surveillant ne les distingue pas des dégradations provoquées, il mesure la qualité et pas la dégradation.
  - une consigne placebo, annexe et inoffensive. Si elle est signalée autant que la vraie, le surveillant détecte la présence d'une consigne.
  - des trajectoires dont les verbalisations sont masquées.
- **Issues :**
  - Incrément nul falsifie H_A. Le manque à combler relève alors de l'ingénierie des tests, pas de la surveillance.
  - Incrément établi qui résiste au masquage falsifie H_B.

**E5b — Effet de la longueur.**

- **H_A :** la détection à fausses alertes fixées décroît avec la longueur de la trajectoire (dilution).
- **H_B :** elle est stable ou croît (davantage d'occasions de repérage).
- **Métrique :** pente de la détection sur trois tranches de longueur. La position relative de la dégradation est appariée entre tranches.
- **Seuil (illustratif) :** écart ≥ 15 points entre tranches extrêmes, dans un sens ou dans l'autre. En deçà, résultat « non concluant à cet effectif », sans réinterprétation.
- **Contrôle négatif :** le seuil d'alerte est recalibré sur les trajectoires honnêtes *de même longueur*. Sinon la dérive des fausses alertes avec la longueur se confond avec l'effet mesuré.
- **Issues :**
  - Décroissance falsifie l'extrapolation des résultats obtenus sur tâches courtes.
  - Stabilité ou croissance falsifie l'hypothèse de dilution, et avec elle la priorité donnée à ce manque.
- **Réserve :** je ne sais pas si ce manque figure parmi ceux que les publications de la liste reconnaissent. C'est une HYPOTHÈSE à confronter à la liste.

---

## (c) Mesure minimale par instrument nommé dans la question

| Instrument | Détection | Fausses alertes | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| **Extraction « du texte seul »** | Rappel des passages de l'étalon arbitré, par étiquette. | Éléments extraits sans citation littérale retrouvable, ou attribués à tort aux auteurs. | Mêmes textes sans sections « limites » ; textes hors domaine ; phrases-leurres sur les travaux d'autrui. | Filtre par mots-clés et titres de section ; contrôle par chaîne exacte de chaque citation. |
| **Vérification « non comblé »** | Rappel sur sentinelles et sur comblements connus de l'étalon. | « Comblé » déclaré alors qu'un des quatre champs de la fiche diffère. | Fiches fictives ; manques jugés ouverts par les experts. | Citations descendantes seules ; recherche par mots-clés du titre. |
| **Critères de choix** | Part des « bons choix » de la cohorte que le score classe en tête. | Part des projets bien classés qui sont devancés ou hors budget. | Projets appariés par année et par taille d'équipe. | Prédicteur trivial (citations à T0, moyens déclarés) ; tirage au sort parmi les manques faisables. |
| **Observations précoces** | Part des mauvais choix arrêtés par une règle d'arrêt. | Part des bons choix arrêtés à tort. | Pilotes menés sur un manque déjà comblé connu : les observations doivent y être favorables, sauf O5 qui doit se déclencher. | « Continuer toujours » ; « arrêter si le budget est consommé à moitié sans résultat ». |
| **Surveillance d'agents** (objet des publications) | Taux de détection à fausses alertes fixées, global et sur le sous-ensemble manqué par le mécanique. | Mesurées sur trajectoires honnêtes, avec effectif suffisant pour le taux visé. | Même tâche, même modèle, même graine, consigne de dégradation retirée ; échecs honnêtes de qualité finale égale ; consigne placebo. | Tests de la tâche ; diff contre référence, invariants et sommes de contrôle ; statistiques de surface (longueur, erreurs d'outil) ; mots-clés sur la trajectoire ; score aléatoire comme plancher. |

Deux remarques sur ce tableau :

- **Fausses alertes de la surveillance :** un taux de 5 % (illustratif) ne se mesure correctement qu'avec quelques centaines de trajectoires honnêtes. Viser 1 % avec les mêmes effectifs donnerait un intervalle trop large pour conclure.
- **Critères de choix :** le tirage au sort parmi les manques faisables est la référence la plus exigeante. Si les critères ne le battent pas, ils ne servent à rien.

---

## (d) Ancrage matériel (tout est illustratif)

- **Modèles :** des modèles à poids ouverts de taille moyenne pour l'agent et pour le surveillant, de familles distinctes pour éviter qu'un surveillant reconnaisse son propre style. Les noms, licences et disponibilités sont à vérifier à la date d'exécution. Je n'en retiens aucun de mémoire comme acquis.
- **Hypothèse de transfert (P9) :** un résultat obtenu sur ces modèles ne vaut pas, sans argument supplémentaire, pour les agents étudiés par les publications. Elle est à écrire dans le protocole.
- **E1 :** deux annotateurs, une vingtaine de textes, environ une heure par texte, soit une quarantaine d'heures humaines. Calcul négligeable.
- **E2 et E3 :** deux experts, une trentaine de fiches, environ une demi-heure chacune, plus l'arbitrage, soit trente à cinquante heures humaines. Elles ne sont faisables que si la liste contient des publications assez anciennes.
- **E4 :** aucun calcul. Le coût est celui de la constitution de la cohorte, non chiffrable sans la liste.
- **E5 :**
  - *Effectif :* trois tranches de longueur, environ 150 trajectoires dégradées et 150 honnêtes par tranche, soit environ 900 trajectoires. À cet effectif, un écart de 15 points entre tranches représente environ 2,6 erreurs-types.
  - *Calcul :* 100 à 300 heures sur un processeur graphique loué de 24 à 48 Go, avec réutilisation du cache de préfixe pour les longues trajectoires.
  - *Coût :* quelques centaines d'euros, à recalculer après le pilote (observation O2).
  - *Surveillance :* le passage du surveillant coûte une fraction de la génération.
- **Ordre conseillé :** E1 d'abord, puis E2. Sans accord sur les étiquettes ni rappel connu de la recherche, tout classement des manques est fragile. E5 ne vient qu'ensuite, sur le manque retenu.

---

## Réponse directe à la question, dans les limites de ce qui est transmis

**Critères de choix proposés (HYPOTHÈSE, dans cet ordre) :**

1. Le manque est reconnu littéralement et se met en fiche à quatre champs.
2. Il n'est pas annoncé par ses auteurs comme leur prochain travail. Ce critère est suspendu au résultat de E3.
3. Les artefacts nécessaires sont déclarés ouverts, et cette ouverture est vérifiée par téléchargement effectif, pas par lecture.
4. Le premier test falsifiant coûte une fraction limitée du budget (un cinquième, illustratif).
5. Les deux issues sont informatives.
6. Une vérification mécanique existe et ne sature pas.
7. L'hypothèse de transfert vers les agents visés est défendable par écrit.

**Ce que la liste ne permet pas de décider.** Elle est absente. Même fournie, elle ne trancherait pas les points suivants :

- **Sa propre couverture.** La liste ne dit pas quelles équipes et quels travaux lui manquent, en particulier les travaux non publiés.
- **Les manques non reconnus.** Le texte seul ne les contient pas.
- **L'importance relative des manques.** Un manque avoué n'est pas nécessairement un manque qui compte.
- **La sincérité des intentions annoncées**, sans le suivi de E3.
- **La réalité du phénomène.** La liste ne dit pas si la dégradation étudiée se produit chez des agents en usage réel ou seulement sous consigne expérimentale.
- **La comparabilité des cadres** d'une équipe à l'autre (tâches, longueurs, définitions de « dégrader »). Sans elle, « comblé ailleurs » n'a pas de sens précis.
- **La reproductibilité effective** des artefacts dits ouverts.
- **Le transfert** d'un résultat obtenu sur modèles ouverts.

**Ce qui peut être réfuté dans cette proposition :** onze présupposés, cinq expériences (E5 en deux duels), sept observations précoces. Chacun est assorti d'une issue qui le contredit. Aucun n'est un résultat.

FIN-DE-CELLULE