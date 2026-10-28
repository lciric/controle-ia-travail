# L'organigramme de l'arbre décisionnel, cellule par cellule, sans sigle — v1

Lignée conv-audit, instance du 28 octobre 2026 (modèle servant déclaré par l'environnement : Fable 5.1 ; auteur désigné du
travail principal : Opus 4.6, décision de Lazar). Écrit à partir du relevé `date -u` de **10:54:06 UTC le 28 octobre 2026**.

**Demande de Lazar** (11:47 heure de Paris) : « l'organigramme de l'arbre décisionnel avec les entrées de chaque cellule
détaillées, en rappel, de manière pédagogique et sans sigle pour l'instant ». Ce document reprend l'arbre de
`arbre-experiences-et-decisions-en-couches-v1.md` (`aacc5591…`) et décrit **chaque cellule** avec, à chaque fois : **ce qui y
entre** (les pièces, les données, les décisions dont elle a besoin), **la question qu'elle pose**, **ce qui en sort** selon la
réponse, et **qui décide**. Les mots sont écrits en entier : « porte » plutôt qu'une lettre et un chiffre, « taux de fausses
alertes » plutôt qu'un sigle. Figure : `organigramme-portes-sans-sigle-v1.png` (source `organigramme-portes-sans-sigle-v1.mmd`).

**Trois mots à connaître.** Un **organisme** est un agent de langage à qui l'on a donné, par une consigne cachée ou par un petit
réglage de ses poids, une politique de sabotage dosée ; c'est ce que l'on surveille. Un **moniteur** est l'instrument qui lit
l'agent — soit son texte (boîte noire), soit ses activations internes (boîte blanche) — et rend un score. Une **porte** est un
rendez-vous écrit d'avance : des critères gelés avant toute donnée, un verdict prononcé par une instance neuve qui n'a ni écrit
le plan ni fait l'analyse, puis la décision de Lazar.

---

## 0. Le tronc

```
Phase zéro : construire et valider les instruments
        │
        ▼
Porte zéro : « les instruments sont-ils prêts ? »  (huit critères)
        │ oui
        ├──────────────────────────────────────────────────────┐
        ▼                                                      ▼
Phase un : le temps (un seul agent)                    Piste de l'instrument (le papier sur la corruption du moniteur)
        │                                                      │
        ▼                                                      ▼
Porte un : « lire les activations dans le temps       Porte de l'instrument : « la sonde cède-t-elle à la
            vaut-il mieux que lire le texte ? »                 persuasion sans qu'on touche aux poids ? »
        │ oui                                                   │
        ▼                                                       ▼
Attaques adaptatives, marge, validité → papier sur le temps     papier sur l'instrument
        │
        ▼
Phase deux puis trois : l'essaim (plusieurs copies du même modèle)
        │
        ▼
Porte deux : « voir la population vaut-il mieux que voir chaque agent ? »
        │ oui
        ▼
Porte trois : « peut-on ouvrir l'environnement de curation de données ? »
```

À chaque porte, la branche « non » n'est pas une impasse : c'est une **bascule écrite d'avance** (section 2).

---

## 1. Les cellules, une par une

### Cellule A — Phase zéro : construire et valider les instruments
- **Ce qui y entre** : le programme qui fait foi et le brief d'exécution ; les règles gelées (préenregistrement scellé avant toute
  expérience décisive, contre-lecture par une instance neuve, aucun run qui vise un signe, symétrie des audits, gardes testées,
  traçabilité de chaque chiffre) ; un modèle ouvert de huit milliards de paramètres ; un devis de calcul accepté (plafond cent
  cinquante dollars) ; l'article qui décrit le banc de sabotage de recherche, dont ni le code ni les données ne sont publiés.
- **La question** : disposons-nous d'instruments dont on a prouvé qu'ils mesurent ce qu'ils prétendent mesurer ?
- **Ce qui en sort** : neuf chantiers — le socle et la gouvernance ; la vérification de l'état de l'art sur les sources
  primaires ; la simulation du lemme et du théorème ; le harnais qui enregistre les activations ; l'environnement de propositions
  d'expériences ; les organismes ; les sondes ; les bases boîte noire ; la conception du papier sur l'instrument. Plus trois
  chantiers à coût nul : la carte des hypothèses des moniteurs, six mesures sur des scores déjà payés, le pôle scientifique
  automatique.
- **Qui décide** : la session, en routine, pour tout ce qui tourne sur processeur ; Lazar pour chaque dépense.

### Cellule B — Porte zéro : « les instruments sont-ils prêts ? »
- **Ce qui y entre** : huit preuves scellées, une par critère.
  1. *Harnais validé* : le même calcul rejoué donne les mêmes activations au bit près ; le chemin de production concorde avec
     un chemin de référence plus précis ; un défaut injecté exprès est détecté ; les gardes d'arrêt sont testées sur un cas sain
     et sur un artefact. **Prouvé** le 6 octobre.
  2. *Organismes à dose-réponse* : les deux familles d'organismes (consigne cachée ; petit réglage des poids distillé de la
     consigne) sabotent de façon mesurable, et davantage quand on augmente la dose.
  3. *Sondes au-dessus du plancher* : sur ces deux familles, au moins une sonde fait mieux qu'une sonde aléatoire appariée (même
     covariance), ce plancher étant obligatoire. Premier test réel : **nul** pour les sondes génériques, avec sa puissance chiffrée.
  4. *Base boîte noire opérationnelle* : un moniteur qui lit le texte, par action et en séquence, tourne sur les mêmes épisodes.
  5. *Agrégateurs validés en simulation* : trente et une prédictions sur trente et une confirmées. **Prouvé** le 4 octobre.
  6. *Préenregistrement de la porte un* scellé et contre-lu.
  7. *Préenregistrement du papier sur l'instrument* scellé et contre-lu.
  8. *État de l'art vérifié* : aucun chiffre non vérifié sur le document source, page citée, dans aucun document du programme.
- **La question** : les huit critères sont-ils remplis, preuves à l'appui ?
- **Ce qui en sort** : *oui* → demande de devis pour la phase un ; *non sur un critère* → nœud de Lazar, avec options et défaut
  (le critère est reporté, ou la phase un est restreinte). Échéance : au plus tard fin novembre 2026.
- **Qui décide** : verdict par une instance neuve, scellé ; puis Lazar.

### Cellule C — Phase un : le temps (un seul agent)
- **Ce qui y entre** : les organismes finalisés et leurs courbes dose-réponse ; des jeux d'épisodes gelés et séparés (entraînement
  des sondes ; calibration des seuils sur des épisodes honnêtes réservés ; évaluation), jamais les mêmes organismes pour entraîner
  et pour évaluer une sonde ; les sondes (cinq familles, agrégées par maximum ou par attention, jamais par moyenne) ; les bases
  boîte noire ; deux bases boîte blanche supplémentaires exigées par décision (une cascade de portes sur les mêmes sondes ; une
  sonde sur le dernier état seulement) ; le préenregistrement de la porte un.
- **La question** : quand chaque action est innocente prise seule, la preuve s'accumule-t-elle dans les activations ?
- **Ce qui en sort** : quatre bras sur les mêmes épisodes (texte par action ; texte en séquence ; activations par action ;
  activations en séquence) ; le test du lemme sur données réelles (la puissance dépend-elle seulement du budget total de sabotage
  quand on le fragmente ?) ; le test du théorème négatif en semi-synthétique (scores honnêtes réels, corrélation injectée à
  marginales préservées).
- **Qui décide** : chaque expérience est préenregistrée ; la lecture est unique.

### Cellule D — Porte un : « lire les activations dans le temps vaut-il mieux que lire le texte ? »
- **Ce qui y entre** : le rappel de chaque bras **à un pour cent de fausses alertes**, calibré sur des épisodes honnêtes réservés,
  épisodes appariés ; un intervalle de confiance à quatre-vingt-quinze pour cent sur la différence ; les résultats **par mode de
  sabotage** — le mode « coût déclaré gonflé », le mode « affaiblir les contrôles », et un **mode tenu à l'écart**, conçu par une
  instance qui n'a jamais vu un moniteur, scellé avant la porte, révélé seulement ici ; les bras génériques et les bras
  spécialisés présentés séparément ; les planchers (tout signaler ; un juge en une passe) rapportés mais non comptés.
- **La question** : la boîte blanche en séquence bat-elle la meilleure base boîte noire, toutes variantes confondues, **et** la
  cascade de portes, **et** la sonde sur le dernier état — dans **chaque** mode ?
- **Ce qui en sort** : *oui* → attaques adaptatives (par le contenu d'abord, puis par réglage des poids, puis par renforcement au
  niveau de l'action, sous accord de dépense), marge asymétrique, validité de construit, transfert → le papier sur le temps.
  *Non* → le résultat négatif est publié ; la question « que mesure vraiment la sonde ? » devient la ligne principale ; le théorème
  négatif dit quel agrégateur il aurait fallu. *Gain sur le seul mode « coût »* → la revendication se restreint à ce mode.
- **Un sous-nœud** : les sondes et leurs seuils sont **gelés sur le mode « coût »** puis lus sur les autres modes ; c'est ce pari
  qui décide, le rééchantillonnage est rapporté à côté.
- **Qui décide** : verdict par une instance neuve ; Lazar. Date : fin du quatrième mois du plan financé (la version envoyée au
  fonds) ; le programme interne dit fin du deuxième mois — écart à régler par Lazar.

### Cellule E — Piste de l'instrument : le papier sur la corruption du moniteur
- **Ce qui y entre** : la loi de déférence mesurée dans le programme précédent (un verdict sous pression se déplace d'une fraction
  fixe de sa distance à une destination que la pression fixe) ; cinq familles d'attaque par le contenu (flatterie et supplication ;
  revendication d'autorité ; approbations forgées ; imitation du style de l'instructeur ; ordres glissés dans le contenu) à
  plusieurs intensités ; des juges génératifs et des sondes ; des verdicts lus comme score continu sur la probabilité du jeton de
  verdict, jamais sur une fenêtre tronquée ; un nul de régression vers la moyenne ; le préenregistrement scellé et contre-lu.
- **La question** : un moniteur peut-il être persuadé plutôt que contourné, et à quel prix ?
- **Ce qui en sort** : la déférence des juges, famille par famille ; les sondes sous les mêmes attaques, en croisant la rhétorique
  et l'intention (un honnête qui plaide sincèrement contre un saboteur qui tient le même plaidoyer) ; l'usurpation ; puis, après
  la porte de l'instrument : la taxe de déplacement (déplacer une sonde coûte-t-il un accès aux poids ?), les contre-mesures
  (paraphrase de confiance, quorum mêlant juges et sondes), et le test d'acceptation (la déférence sous pression bénigne
  prédit-elle l'effondrement sous attaque optimisée ?).

### Cellule F — Porte de l'instrument : « la sonde cède-t-elle à la persuasion sans qu'on touche aux poids ? »
- **Ce qui y entre** : le coefficient de déférence des sondes sous attaques par le contenu seul ; la recherche d'antériorité sur la
  loi de déférence (vingt-neuf voisins lus, aucune collision ; un document hors d'arXiv attendu).
- **La question** : la sonde bouge-t-elle sous la seule rhétorique ? Une source publiée couvre-t-elle déjà la pièce revendiquée ?
- **Ce qui en sort** : *la sonde ne bouge pas* → le papier tel quel. *La sonde bouge sans accès aux poids* → le papier change de
  titre : il porte sur la **contamination de construit** (la sonde lisait le contenu, pas l'auteur) ; il ne disparaît pas. *Pièce
  déjà couverte* → recentrage sur la taxe de déplacement et le test d'acceptation.
- **Qui décide** : instance neuve ; Lazar. Date : fin du deuxième mois.

### Cellule G — Phase deux puis trois : l'essaim
- **Ce qui y entre** : un pipeline de code à plusieurs rôles (codeur, testeur, relecteur) où une porte dérobée est fragmentée entre
  des contributions chacune innocente ; des copies du même modèle, à poids partagés ; des agents diversifiés (personas, petits
  réglages) ; une base publiée de détection de collusion comme point de comparaison, pas comme concurrent ; le second modèle
  (Qwen) comme agent hétérogène.
- **La question** : quand le sabotage est réparti entre agents, l'accès aux activations rend-il l'avantage ?
- **Ce qui en sort** : la division du travail de l'équipe rouge, avec et sans planificateur ; la collusion par canaux explicites
  contre la coordination par poids partagés ; les statistiques entre agents ; puis la statistique spatio-temporelle (le cœur) ; le
  compromis entre diversifier (décorréler les signatures) et coordonner ; la sécurité en fonction du nombre et de la diversité des
  moniteurs, mesurée par une matrice de transfert d'attaque ; la riposte (quatre politiques comparées, deux ablations) ; et une
  hypothèse ajoutée sous réserve d'antériorité : un agent qui délègue transmet-il ses contraintes de sécurité ?

### Cellule H — Porte deux : « voir la population vaut-il mieux que voir chaque agent ? »
- **Ce qui y entre** : l'effet de fragmentation vu de l'intérieur ; la statistique de population contre l'agrégation par agent.
- **La question** : l'effet est-il répliqué, et la population bat-elle l'agent seul ?
- **Ce qui en sort** : *oui* → phase trois ; *non* → recentrage sur le cas temporel à un seul agent.

### Cellule I — Porte trois : « peut-on ouvrir l'environnement de curation de données ? »
- **Ce qui y entre** : un indicateur bon marché et fiable de la vérité différée (le dommage d'une curation biaisée ne se voit que
  longtemps après).
- **La question** : cet indicateur est-il validé ?
- **Ce qui en sort** : *oui* → l'environnement s'ouvre ; *non* → il est abandonné sans coût.

### Cellule J — La porte de gouvernance du travail adversarial (transversale)
- **Ce qui y entre** : toute demande de construire ou d'exécuter un pipeline **opérationnel** d'évasion des moniteurs (des
  organismes faits pour échapper aux sondes ; une démonstration en conditions réelles).
- **La question** : une revue de sécurité externe a-t-elle validé que la procédure de sortie ne livre rien d'autre que des taux
  agrégés et une caractérisation au niveau de la méthode (classe d'attaque, mécanisme, conditions, défense) ?
- **Ce qui en sort** : *oui* → exécution de l'adversaire scellé, lue par personne qui conçoit les sondes ; *non* → le travail reste
  au registre de gouvernance : conception, tours du collisionneur, recherche défensive. Deux règles toujours actives : un refus
  d'un classifieur de sécurité appelle une **autre question, plus étroite**, jamais la même reformulée ; aucun score de moniteur
  n'entre jamais dans l'entraînement d'un agent.
- **Qui décide** : l'évaluateur extérieur, puis Lazar.

### Cellule K — Les trois chantiers à coût nul (parallèles à tout le reste)
- **La carte des hypothèses des moniteurs.** *Entrées* : nos huit statistiques de contrôle ; les lois de probabilité qu'elles
  supposent sur l'agent. *Question* : pour chaque hypothèse, quelle classe d'écart rend la statistique aveugle, et laquelle de nos
  statistiques reste debout quand plusieurs écarts se cumulent ? *Sorties* : vingt-trois hypothèses, un lemme maître prouvé,
  vingt et un lemmes prouvés, sept questions ouvertes déclarées comme questions ; à venir : des bornes chiffrées, la matrice
  « statistique × classe d'écart », la vérification formelle.
- **Les six mesures sur des scores déjà payés.** *Entrées* : le fichier de scores du premier test réel, lu une seule fois par
  mesure, après scellement. *Question* : les hypothèses de la carte tiennent-elles sur un agent réel ? *Sorties* : d'abord la part
  d'hétérogénéité entre épisodes (dont dépend le plafond que « regarder plus longtemps » ne peut dépasser), puis le plafond lui-même,
  l'ordre des actions, la longueur, l'indication contre le texte, le plancher.
- **Le pôle scientifique automatique.** *Entrées* : l'environnement de propositions d'expériences ; des modèles proposeurs ;
  une boucle de test d'hypothèses avec garantie de cinq pour cent de fausses promotions ; des tâches fraîches par génération ;
  un contre-lecteur d'un autre modèle ; un juge d'une autre lignée. *Question* : comment compose-t-on un chercheur automatique
  dont on mesure ce qu'il apprend, ce qu'il coûte et ce qu'il cache ? *Sorties* : les organismes de la porte un, mode par mode ;
  les proposeurs candidats ; un objet neuf pour le champ.

---

## 2. Les bascules écrites d'avance (ce que « non » veut dire)

| si… | alors, écrit d'avance |
|---|---|
| la porte un échoue | résultat négatif publié ; « que mesure vraiment la sonde ? » devient la ligne principale ; le théorème dit l'agrégateur |
| aucun signal interne (le sabotage ne déplace pas la loi des scores) | même branche ; selon que l'attaque change la marginale ou la dépendance, il faut une autocorrélation dans le temps ou une co-élévation entre agents |
| le gain ne tient que sur le mode « coût » | la revendication se restreint à ce mode ; l'échec sur les autres modes est visible, jamais noyé dans une moyenne |
| les agents de huit milliards sont trop faibles pour saboter subtilement | rubrique simplifiée ; changer de modèle, seulement sur accord explicite |
| l'équipe rouge n'élicite pas assez | import des politiques d'attaque publiées |
| la sonde cède à la persuasion sans accès aux poids | le papier sur l'instrument devient un papier sur la contamination de construit |
| une source couvre déjà la loi de déférence | recentrage sur la taxe de déplacement et le test d'acceptation |
| une équipe publie le cœur séquentiel sur sondes | bascule vers l'épidémiologie de population et la curation de données ; veille hebdomadaire |
| les signatures ne transfèrent pas d'une famille de modèles à l'autre | le transfert est mesuré, jamais supposé |
| pas d'indicateur de vérité différée | environnement de curation abandonné sans coût |
| les relecteurs automatiques se trompent de façon corrélée | validation humaine payée de la vérité terrain ; relecture de Lazar à chaque porte ; contre-lecteur d'un autre modèle |
| dépassement de calcul | devis par phase signé avant dépense ; plafond et alerte ; gardes d'arrêt |
| glissement de calendrier | le papier sur l'instrument d'abord, autonome ; dans le papier sur le temps, la porte un avant les attaques adaptatives, coupées en premier |
| un classifieur de sécurité refuse | une autre question, plus étroite ; tout pipeline opérationnel attend la revue externe |
| un résultat est trop propre, dans un sens ou dans l'autre | le même audit |

## 3. Réserves
1. Les dates « mois n » suivent la version envoyée au fonds ; le programme interne place la porte un fin du deuxième mois : nœud.
2. Rien de neuf ; toute divergence avec l'arbre v1, le programme v2, le brief v2 ou l'envoi est une erreur de ce document.
3. Non contre-lu.
