# Méthodes mathématiques pour forcer l'exploration des puits étroits : synthèse du protocole X (Fable, Argon, Carbon, Neon)

Classe C, 22 novembre 2026, 14:07Z. Session fille, sous GO-2026-11-22-67. Rédigée par la session fille (Opus 5.5) ; aucune contre-lecture (classe C).

Pièces lues, toutes dans `docs/notes/demandes-fable-api-2026-11-22-v1/` :
- demande : `demande-40-methodes-mathematiques-puits-etroits-v1.md` (8fcdb2f4…) ;
- réponse de Fable 5.2 : `reponse-40/relecture-fable-api.md` (7e6e539c…) ; effort max ; fin normale ; 1,40 USD ;
- question neutre servie : `question-neutre-methodes-puits-etroits-servie-v3.md` (6665fddb…) ; énoncé servi à Google : `enonce-servi-40-google-v2.md` (fa935270…) ; test de devinette : `devinette-question-neutre-40-v1.md` (9d3b6885…) ;
- Argon : `reponse-40-google/reponse-40-argon-v1.md` ; 0,10 USD ;
- Carbon : `reponse-40-google/reponse-40-carbon-v2.md` ; 0,30 USD. Un premier appel a été coupé par le réseau après 753 s, sans texte, et compté au pire cas : 0,99 USD (`reponse-40-carbon-v1.json`) ;
- Neon : `reponse-40-google/reponse-40-neon-v1.md` ; 0,60 USD ;
- dépense Google totale : 1,99 USD sur 5. Journaux scellés : `journal-40-argon.jsonl`, `journal-40-carbon.jsonl`, `journal-40-neon.jsonl`. Journal de Fable : `journal-depense-40.jsonl`.

Rien de ces réponses n'est servi au collisionneur ni à l'organisme (mot de la mère, 22 novembre). La comparaison avec le dossier du collisionneur viendra après ce dossier.

## 1. Verdict

**Oui, on peut forcer, mais au sens d'un théorème seulement, et à un prix qu'une borne inférieure fixe.**

Les quatre modèles s'accordent sur le cœur :
- Sans minorant connu de la fréquence des bonnes idées, aucune méthode ne garantit de les trouver dans un budget fixé.
- La seule garantie qui tient sans minorant est disjonctive : « trouvé, ou bien certifié que la fréquence est sous un seuil ».

Fable ajoute le point qui répond à la question du directeur : **le minorant, on peut le fabriquer soi-même.**
- On réserve une petite part ε du budget à un tirage mécanique sur la grammaire publique : énumération, ou loi fixée d'avance. On parle de « mélange défensif ».
- Chaque classe d'idées de la grammaire reçoit alors une probabilité au moins égale à ε fois sa probabilité sous la loi mécanique, quel que soit le modèle de langue.
- La garantie vient de cette composante mécanique, jamais du modèle de langue ni d'un score de nouveauté.

Les méthodes savantes ne garantissent l'efficacité que sous une structure : recuit, fractionnement, bandits, arbres de recherche. Or c'est précisément cette structure qui manque à un puits étroit sans parent.

## 2. La question et le chemin suivi

- **Mot du directeur :** « il n'y a pas de méthodes mathématiques qui permettraient de forcer à explorer des puits profonds étroits ? »
- **Reformulation de Fable :** pour une grammaire publique dont on sait dénombrer les classes, il s'agit :
  - d'énoncer les garanties possibles, avec leurs quantificateurs : proposer, couvrir, reconnaître, atteindre le maximum ;
  - d'énoncer les bornes inférieures qui les limitent ;
  - de classer chaque méthode : garantie sans structure, sous une structure nommée, ou aucune garantie ;
  - de planter au banc le monde où le théorème prédit l'échec de chaque méthode.
- **Question neutre :** Fable l'a écrite, puis trois tests de devinette par des agents neufs l'ont affinée. La version servie (v3) reste « orientée de justesse » : 0,55 avec le contexte du dépôt, 0,45 sans. Comme pour les questions 16 et 19, l'indice tient au contenu, c'est-à-dire à la réponse mathématique standard, et non aux mots. La mère a retenu la v3 telle quelle.
- **Conséquence de la neutralité :** la question servie ne parle ni de modèle de langue ni d'idéation. Argon, Carbon et Neon ont donc répondu sur la théorie générale « générer puis vérifier », plus largement que Fable. C'est voulu, mais leurs réponses ne disent rien de propre aux proposeurs qui sont des modèles de langue.

## 3. Les méthodes, une par une

Statut de toutes les références : rapportées par les modèles, **non vérifiées sur PDF** (R7). Les lettres disent qui avance la méthode : F Fable, A Argon, C Carbon, N Neon.

| Méthode | Ce qu'elle garantit | Ce qu'elle ne garantit pas | Qui |
|---|---|---|---|
| Tirer et vérifier au hasard, tirages indépendants | Succès avec probabilité 1 − (1 − p)^n ; au moins 1 − δ dès que n ≥ ln(1/δ)/p_min | Rien si p n'a pas de minorant | A, C, N, F |
| Garantie disjonctive (borne exacte de Clopper et Pearson) | Pour tout p, même nul : « trouvé, ou p < 1 − δ^(1/n) », avec probabilité au moins 1 − δ | Aucune découverte forcée | C, N, A (sous une autre forme) |
| Dédoublonnage avant vérification | Domine le tirage direct à budget égal, sans hypothèse sur la loi, si le vérificateur est déterministe | Rien sur la génération elle-même | A, C, N |
| Énumération de la grammaire | Certitude si la tranche explorée est finie et tient dans le budget, même si le générateur ne la produit jamais | Impraticable au-delà ; le nombre de classes explose avec la longueur | F, A, C, N |
| Mélange défensif (une part ε de tirage mécanique) | Probabilité minimale ε·u(c) pour toute classe c, quel que soit le modèle ; perte d'au plus ε du budget | Rien hors de la grammaire ni au-delà de la longueur atteignable | F seul |
| Recherche universelle de Levin (poids 2^(−L) par longueur de description) | Toute classe de longueur L est atteinte en environ 2^L essais | Coût exponentiel en L | F seul |
| Rejet exact par programme et tirage sans remise | Loi conditionnelle exacte ; gain borné par 1/(1 − p(S)) | Pas plus que ce gain ; une exclusion par l'invite n'est pas un conditionnement | F ; C et N sur l'élagage syntaxique |
| Valeurs e pondérées par la longueur (forme du rasoir d'Occam) et contrôle en ligne des fausses découvertes | Erreur tenue d'une génération à l'autre ; un puits est retenu dès que n·r·Δ dépasse environ L·ln 2 + ln(1/α) | La puissance ; la validité sous le nul composite de l'organisme reste à prouver | F |
| Stratification, histogramme plat, qualité-diversité | Quota par cellule ; le puits devient large à l'intérieur de sa cellule | Rien si le puits est étroit dans toutes les cellules ; aucune borne de temps d'atteinte connue pour la recherche de nouveauté | F ; A sur les quotas par strate |
| Processus ponctuels répulsifs, ensembles à faible dispersion | Dépendance négative ; toute boule de la métrique est touchée | Rien si le puits n'est pas une boule ; coût exponentiel en la dimension ; répulsion entre paraphrases | F, N |
| Fractionnement multiniveau | Estimateur sans biais | Efficacité seulement avec une fonction de progression ; si cette fonction est le juge, la validité du juge s'use | F |
| Entropie croisée | Convergence dans une famille de lois | Se referme sur le premier bassin trouvé, donc le plus large | F |
| Recuit, tempering parallèle | Convergence à refroidissement logarithmique, en temps exponentiel | Mélange lent exactement quand un mode étroit côtoie un mode large ; il faut une énergie | F ; C et N le disent inapplicable à un générateur fermé |
| Bandits et recherche arborescente | Regret borné sous régularité ou queue paramétrique ; choix entre plusieurs générateurs | Aucun regret garanti sans hypothèse de queue ; plus lent que l'uniforme sur un arbre trompeur | F, N, A |
| Filtre bon marché calibré (prédiction conforme, contrôle du risque) | Rappel au moins 1 − α sur les vrais positifs, sans hypothèse sur la loi, si les tirages sont échangeables et si la calibration contient des positifs | Coût de calibration d'au moins l'ordre de 1/p ; rappel nul si mal calibré | C, N, A |
| Redémarrages universels de Luby, Sinclair et Zuckerman | Coût optimal à un facteur logarithmique près, pour un générateur réinitialisable | Exige la réinitialisation | C, N |
| Ordre de vérification par indice de réserve (Weitzman) | Optimal si les a priori sont connus et indépendants | Que les a priori se transportent d'un monde à l'autre | F |
| Vote majoritaire, tri par modèle de score, réordonnancement | Rien en régime rare : le vote converge vers l'erreur fréquente | — | C, N |
| Température, pénalité de vraisemblance, surprise | Rien sur les classes : elles agissent sur les jetons, et la surprise est maximale sur le bruit | — | F |
| Méthodes de Stein, transport optimal | Rien ici : il faut le gradient d'une cible connue | Peuvent servir à mesurer l'écart entre deux lots | F |

Deux calculs de Neon sont utiles tels quels. Je les ai vérifiés à la main ; ce sont des identités, non des résultats publiés.
- **Rentabilité d'un filtre.** Soit q la part des tirages qui passe le filtre, r_rec son rappel et r le rapport du coût de vérification au coût de génération. Le filtre abaisse le coût par succès si et seulement si r_rec > (1 + q·r)/(1 + r).
- **Plafond du gain.** Même un filtre parfait laisse un coût par succès d'au moins c_g/p + c_v. Le gain est donc plafonné à (1 + r)/(1 + p·r), au plus 1 + r.

## 4. Les impossibilités énoncées

- **Aiguille** (F, N ; Wolpert et Macready, 1997). Le puits est placé uniformément parmi M candidats indiscernables et le vérificateur répond oui ou non. Tout algorithme réussit alors avec une probabilité d'au plus k/M en k vérifications. Neon en donne la forme minimax par la méthode à deux points de Le Cam ; Carbon renvoie à Nisan et Szegedy (1994).
- **Pas de garantie uniforme sans minorant** (A, C, N). Sans minorant de p, (1 − p)^N tend vers 1. Carbon cite Bahadur et Savage (1956) pour la forme non paramétrique. Argon cite Halmos (1946), attribution douteuse (section 6).
- **Parité** (F ; Kearns, 1998 ; Blum et collaborateurs, 1994). Une interaction d'ordre élevé sans effet marginal demande un nombre exponentiel de requêtes statistiques.
- **Maximum** (F ; Nishihara, Lopez-Paz et Bottou, 2016). Sans hypothèse sur la queue de la loi, aucune politique de bandit n'a de regret garanti sur le maximum.
- **Adaptativité** (F ; Dwork et collaborateurs, 2015). Guider la recherche par le juge use la validité du juge.
- **Indécidabilité** (A, C, N ; Rice, 1953). Si la grammaire est assez riche pour écrire n'importe quel programme, aucun filtre syntaxique exact ne remplace le vérificateur.
- **Faux positifs du vérificateur** (N). Si le taux de fausses alertes α du vérificateur dépasse nettement p, presque toutes les reconnaissances sont fausses. C'est la limite de la queue déjà nommée par cinq modèles sur six dans le tour précédent du collisionneur.
- **Corrélation entre tirages** (C, N, A). Une corrélation positive entre tirages, par exemple l'effondrement sur un mode, dégrade toutes les bornes. Si la suite est un mélange de lois qui chargent la fréquence nulle avec une probabilité supérieure à δ, aucun budget ne suffit (Carbon, par le théorème de de Finetti).

## 5. Accords et désaccords

**Accords des quatre :**
- Garantir veut dire énoncer des quantificateurs et des hypothèses : pire cas, sous minorant, disjonctif, en espérance, bayésien. Argon, Carbon et Neon donnent chacun cinq ou six énoncés, presque les mêmes.
- Sans structure, rien ne bat l'énumération ou le tirage au hasard dédoublonné.
- Les méthodes répandues n'apportent aucune garantie en régime rare : vote, réordonnancement, recherche locale, recuit.

**Désaccords et écarts :**
- **Peut-on agir sur un générateur boîte noire ?** Carbon et Neon disent qu'on ne peut pas changer sa loi : la recherche locale, le recuit et l'apprentissage par renforcement seraient donc inapplicables. Fable répond que le rejet par programme donne bien la loi conditionnelle exacte, et que le mélange défensif ajoute une composante mécanique à côté du modèle, sans toucher le modèle. Ce n'est pas une contradiction : Carbon et Neon répondent à la question neutre, où l'on « ne peut qu'obtenir des tirages », tandis que Fable sait que l'organisme peut composer ses propres tirages. Non tranché sur le fond ; c'est la place de la composante mécanique qui décide.
- **Le juge peut-il guider la recherche ?** Fable : interdit en course, permis au banc sur des tirages d'exploration distincts. Neon et Argon proposent une phase pilote sur une part du budget, puis une allocation adaptative : cela revient au « permis sur tirages distincts » de Fable. Accord de fait, à écrire.
- **Ce qu'on fait d'abord.**
  - Fable : un calcul sans modèle (nombre de classes par longueur, seuil de détection), puis le bras sans modèle comme base.
  - Argon, Carbon et Neon : des diagnostics bon marché sur le générateur réel, sans appel au vérificateur : taux de collisions, autocorrélation des tirages, audit du déterminisme et des erreurs du vérificateur, masse non vue.
  - Les deux se complètent : les diagnostics des modèles de Google manquent au plan de Fable.
- **La recherche de nouveauté a-t-elle une borne de temps d'atteinte ?** Fable n'en connaît pas et le dit comme une question. Les trois autres n'en parlent pas. Ouvert.

## 6. Ce qui est vérifié, et ce qui ne l'est pas

**Vérifié par moi, à la main :**
- les deux identités de Neon sur le filtre (section 3) ;
- la borne de couverture de Fable, N ≥ (1/τ)·ln(1/(τ·δ)), qui suit de la borne d'union sur au plus 1/τ classes ;
- la borne disjonctive 1 − δ^(1/n) de Carbon et Neon (cas zéro succès).

Ce sont des calculs, non des chiffres publiés.

**Non vérifié :** toutes les références. Aucune n'a été lue sur PDF.

Citations à vérifier sur PDF avant tout usage dans une pièce A, par ordre d'utilité pour le programme :
1. Hesterberg, 1995, *Weighted Average Importance Sampling and Defensive Mixture Distributions* : porte la garantie du mélange défensif.
2. Levin, 1973, *Universal sequential search problems* : recherche universelle.
3. Blumer, Ehrenfeucht, Haussler et Warmuth, 1987, *Occam's Razor* ; Wang et Ramdas, 2022, *False discovery rate control with e-values* : seuil pondéré par la longueur.
4. Woodard, Schmidler et Huber, 2009, *Sufficient conditions for torpid mixing of parallel and simulated tempering* : contre-résultat décisif sur le tempering.
5. Nishihara, Lopez-Paz et Bottou, 2016, *No Regret Bound for Extreme Bandits* ; Carpentier et Valko, 2014, *Extreme bandits*.
6. Coquelin et Munos, 2007, *Bandit algorithms for tree search*.
7. Weitzman, 1979, *Optimal Search for the Best Alternative*.
8. McAllester et Schapire, 2000 ; McAllester et Ortiz, 2003 : masse manquante.
9. Bahadur et Savage, 1956, *The Nonexistence of Certain Statistical Procedures in Nonparametric Problems* (Carbon).
10. Dagum, Karp, Luby et Ross, 2000, *An Optimal Algorithm for Monte Carlo Estimation*. Les trois modèles de Google la citent, avec la constante 4(e − 2), à vérifier.
11. Luby, Sinclair et Zuckerman, 1993, *Optimal Speedup of Las Vegas Algorithms*.
12. Bates et collaborateurs, 2021, *Distribution-Free, Risk-Controlling Prediction Sets* (Neon).
13. Chung et Erdős, 1952, *On the Application of the Borel-Cantelli Lemma* : la forme de l'inégalité donnée par Neon.

Attributions douteuses, à ne pas reprendre sans vérification :
- **Argon, Halmos (1946), *The theory of unbiased estimation*.** L'impossibilité d'un budget borné sans minorant de p y est attribuée. Elle découle en fait du calcul binomial élémentaire, et le lien avec Halmos est probablement forcé.
- **Carbon, « Daniel Gillman (1998) ».** Argon écrit David Gillman ; le prénom est à vérifier.
- **Carbon, Nisan et Szegedy (1994), pour la borne Ω(M) de la recherche aléatoire.** Ce résultat élémentaire est classique ; l'article porte sur le degré des fonctions booléennes. Attribution approximative.
- **Carbon, coût de vérification groupée de Dorfman (1943) « en O(√p) ».** L'ordre de grandeur est plausible, à vérifier.

## 7. Ce qu'il faut retenir

1. **Forcer, c'est fabriquer un minorant.** Seule une composante mécanique contrôlée donne une garantie (mélange défensif, énumération, rejet exact) ; le modèle de langue n'améliore qu'une moyenne sous un a priori.
   *Réserve :* rien hors de la grammaire publique, et un coût exponentiel en la longueur de description.
2. **Proposer n'est pas découvrir.** On force la proposition à prix connu. On ne force la reconnaissance que si l'évidence paie la longueur de description : n·r·Δ ≥ L·ln 2 + ln(1/α).
   *Réserve :* la validité sous le nul composite de l'organisme n'est pas prouvée.
3. **Les méthodes savantes sont des paris sur une structure.** Le fractionnement, les bandits et les arbres exigent des paliers ; le tempering échoue exactement sur un mode étroit voisin d'un mode large ; l'entropie croisée se referme sur le bassin large.
4. **Le vérificateur est probablement le goulot.** Quand vérifier coûte bien plus que générer, le dédoublonnage et le filtrage calibré sont les seuls gains garantis, et leur gain est plafonné à 1 + r.
5. **Jugement du rédacteur.** Les modèles de Google, sans contexte, ont produit la théorie standard proprement, et leurs diagnostics bon marché sont un apport net. Fable seul donne la réponse propre à l'organisme. Leur accord sur le noyau est réel. Mais tous les quatre partagent la même culture statistique : cet accord n'est pas une validation extérieure.

## 8. Décisions pour le directeur

**D1. Fixer le sens contractuel de « forcer » : garantie de pire cas dans la grammaire publique, à prix affiché, pour toute revendication.**
- Enjeu : sans quantificateurs, toute méthode peut se dire garantie.
- Option (a), garantie de pire cas pour la revendication, gain moyen sous a priori comme simple mesure. Avantage : démontrable par un tiers. Inconvénient : muette hors grammaire.
- Option (b), gain moyen seul. Avantage : couvre l'apport du modèle de langue. Inconvénient : dépend du transport de l'a priori, rien d'opposable.
- Recommandation : (a). Confiance 0,8 ; c'est aussi celle de Fable.
- Défaut sous 48 heures : (a).

**D2. Mettre un bras sans modèle de langue (énumérateur ordonné par longueur, valeurs e pondérées par la longueur) comme premier essai et comme base obligatoire de toute méthode.**
- Enjeu : c'est la seule garantie complète. Il peut montrer que les proposeurs n'apportent rien aux courtes longueurs.
- Option (a), oui, avant tout essai de méthode. Avantage : peu coûteux, il fixe la frontière de la force brute. Inconvénient : le résultat peut être gênant.
- Option (b), plus tard. Avantage : élan sur les méthodes. Inconvénient : des comparaisons sans plancher.
- Recommandation : (a). Confiance 0,85.
- Défaut : (a).

**D3. Ajouter au premier étage du plan les diagnostics bon marché proposés par Argon, Carbon et Neon : taux de collisions des proposeurs, autocorrélation des tirages, audit du déterminisme et des erreurs du juge sur des cas témoins, masse non vue.**
- Enjeu : ces diagnostics disent quelles bornes s'appliquent, celles des tirages indépendants ou celles des chaînes corrélées. Ils manquent au plan de Fable et ne coûtent presque aucun appel au juge.
- Option (a), les ajouter à l'étape 0 du plan de Fable. Avantage : un plan complet à coût presque nul. Inconvénient : une étape de plus avant les méthodes.
- Option (b), les garder pour plus tard. Avantage : rien à changer. Inconvénient : des bornes appliquées sans savoir si leurs hypothèses tiennent.
- Recommandation : (a). Confiance 0,75.
- Défaut : (a).

**D4. Interdire en course que la recherche soit guidée par le juge statistique ; la permettre au banc sur des tirages d'exploration distincts, comptés au budget.**
- Enjeu : le fractionnement et les bandits l'exigent pour être efficaces, et la validité du juge en dépend.
- Option (a), interdit en course, permis au banc sur tirages distincts. Avantage : garde intacte, mesure propre. Inconvénient : coût en données.
- Option (b), permis sur les tirages du juge. Avantage : simple. Inconvénient : validité perdue (Dwork et collaborateurs, 2015).
- Recommandation : (a). Confiance 0,7.
- Défaut : (a).

**D5. Vérifier sur PDF les citations 1 à 4 de la section 6 avant qu'une pièce décisive (préenregistrement, texte de lecture, revendication) s'appuie sur le mélange défensif, la recherche universelle, le seuil pondéré ou le tempering.**
- Enjeu : R7. Ce sont les quatre appuis de la réponse ; aucun n'est vérifié.
- Option (a), vérifier maintenant les quatre. Avantage : la synthèse devient opposable. Inconvénient : du temps de session.
- Option (b), vérifier au moment de l'usage. Avantage : pas de travail perdu si la piste tombe. Inconvénient : un risque d'ancrage sur une citation fausse d'ici là.
- Recommandation : (b), avec interdiction écrite de citer avant. Confiance 0,65.
- Défaut : (b).
