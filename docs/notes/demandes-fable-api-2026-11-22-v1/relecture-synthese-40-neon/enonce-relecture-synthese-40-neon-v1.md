Tu es contre-lecteur. Ci-dessous, une synthèse de quatre réponses de modèles (lettres F, A, C, N) à une même question de mathématiques : comment garantir qu'un générateur aléatoire produise puis fasse reconnaître des objets rares. Les quatre réponses suivent la synthèse. L'une des quatre réponses (N) est peut-être la tienne : juge-la comme les autres, sans indulgence.

Vérifie :
1. Fidélité : chaque affirmation attribuée à F, A, C ou N est-elle dans la réponse citée ? Attributions fausses, apports importants oubliés, accords présentés à tort.
2. Mathématiques : refais les calculs que la synthèse dit avoir vérifiés ; juge le seuil n·r·Δ ≥ L·ln 2 + ln(1/α) et la garantie q(c) ≥ ε·u(c) ; dis sous quelles hypothèses ils sont justes.
3. Le verdict (« on ne peut forcer qu'au sens d'un théorème, en fabriquant soi-même le minorant ») est-il soutenu par les quatre réponses ou surtout par F ? Est-il exagéré ?
4. Les décisions D1 à D5 suivent-elles des sources ?
5. Les faits non vérifiés présentés sans marque ; les références que tu sais fausses ou mal attribuées (dis ce que tu sais et ce que tu supposes).
Classe chaque remarque : défaut fort, moyen, faible, ou remarque ; pour chaque défaut, la phrase visée, le problème et la correction en une phrase.
Réponds en français, en 2000 mots au plus. Termine par « FIN DE LA RÉPONSE ».


======== PIÈCE À RELIRE : synthèse ========

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


======== SOURCE F : réponse de Fable ========

# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChJ3jn3T1rbxPqDjPtDtu`
- Heure (UTC) : 2026-11-22T13:34:55Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 106000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-40-methodes-mathematiques-puits-etroits-v1.md` — sha256 8fcdb2f4f62764cf11b4ccb8eb54126f11bbd72f65d582c4220e5aa7b6763d89 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-28-effort-max/relecture-fable-api.md` — sha256 1261c8eeb9f00711ec3a5e8a7438bb3c26ec5d04d6af342ceaa7ec766daa52b4 (compagnon : vérifié)
  - remarques : `docs/notes/organisme-bassins-etroits-v1/recoupement-methodes-v1.md` — sha256 eecd98fab0beff8c99414380a5d12b18feafd1581d38c7fe54b94491327ab172 (compagnon : vérifié)
  - remarques : `docs/notes/collisionneur-v9/syntheses-protocole-x-v1/note-synthese-idees-originales-v1.md` — sha256 10448cd446cf6934095c709d6fd30af657432724ded40ece188cc6f7fb6a5583 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 33d61e37477d3a03a40562568a0a57a4eb0de3e314dca522cdef7d469bba4ed4
- Jetons : entrée 32533, sortie 28413 (dont réflexion 18776), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.396784 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 40 — méthodes mathématiques qui forcent l'exploration des puits étroits : réponse par la méthode « demande approfondie »

**Conventions.** Le statut par défaut est dit en tête de chaque section, et les exceptions sont marquées dans la phrase. Toute antériorité a le statut « rapporté, non vérifié sur PDF » (fichier de l'article non relu). La certitude (élevée, moyenne) porte sur l'existence de la référence et le sens de son résultat. Aucun chiffre publié n'est repris. Seuls des auteurs d'antériorités sont nommés. Je ne peux lancer ni session fille ni collisionneur : je fournis la question à servir (C7).

**Réponse courte** (HYPOTHÈSE d'analyse, détaillée en C). Oui, des méthodes forcent au sens d'un théorème. Mais leur garantie vient toujours d'une composante mécanique que l'on contrôle (énumération, mélange défensif, rejet exact, stratification), jamais du modèle de langue ni d'un score de nouveauté. Son prix est fixé par une borne inférieure. Les méthodes savantes (recuit, fractionnement, bandits, arbres) ne garantissent l'efficacité que sous une structure, et c'est cette structure qui manque à un puits étroit sans parent.

## A. Les quatre points préalables (PROPOSITIONS)

**1. Ce qu'un expert ferait et qui n'est pas demandé.**
- Écrire « forcer » avec ses quantificateurs : pour tout puits d'une classe nommée, au budget B, la probabilité de succès est au moins 1 − δ. Demander à chaque méthode lequel elle tient : pire cas, moyenne sous un a priori, ou asymptotique.
- Chercher d'abord la borne inférieure, ensuite la méthode qui l'atteint.
- Séparer trois budgets : appels de génération, calcul de vérification, tirages frais. Forcer la proposition n'est pas forcer la découverte.
- Vérifier dans l'organisme les hypothèses de chaque théorème : classe décidable, noyau qui conserve la loi conditionnelle, fonction de progression publique.
- Construire, pour chaque méthode, le monde adverse où son théorème prédit l'échec, et le planter au banc.

**2. Données brutes de départ.**
- La grammaire publique elle-même, pour dénombrer les classes canoniques par longueur de description.
- Les propositions brutes canonisées.
- Les log-probabilités jeton par jeton, là où elles existent, sous décodage contraint par la grammaire.
- Les rapports de vraisemblance du juge, tirage par tirage.
- Les énoncés des théorèmes dans les articles d'origine, non leurs résumés.

**3. Méthodes et outils.** Bornes minimax par argument d'aiguille, recherche universelle, échantillonnage préférentiel à mélange défensif, rejet exact et tirage sans remise, valeurs e pondérées, indice de réserve pour l'ordre de vérification, calcul exhaustif sur petites grammaires, assistant de preuve pour les énoncés courts.

**4. Vérification hors du directeur et du modèle qui répond.**
- Preuves relues par un mathématicien tiers, ou formalisées dans un assistant de preuve.
- Calculs exhaustifs rejouables, comme pour la borne 11 du recoupement.
- Mondes adverses conçus par un tiers, clé scellée.
- Contrôle par un tiers des énoncés cités, sur les articles.
- Réplication sur graines neuves.

## B. Demande reformulée

« Pour une grammaire publique dont les classes canoniques sont dénombrables par programme :
(a) énoncer, avec quantificateurs et hypothèses, les garanties possibles sur la proposition, la couverture, la détection et le maximum, et les bornes inférieures qui les limitent ;
(b) classer chaque méthode selon que sa garantie tient sans structure, sous une structure nommée, ou n'existe pas ;
(c) dire d'où vient la garantie quand le tireur est un modèle de langue boîte noire et que la vérification domine le coût ;
(d) composer les garanties et en dire le prix en appels, en calcul et en tirages frais ;
(e) planter, pour chaque méthode, le monde où le théorème prédit son échec, et écrire d'avance ce qui la réfute. »

## C. Réponse

### 1. Ce que « forcer » peut vouloir dire

Les énoncés sont des FAITS RAPPORTÉS (calculs élémentaires ou résultats cités). Leur transposition à l'organisme est une HYPOTHÈSE.

Notations : M classes canoniques de longueur de description au plus L ; q(c) la probabilité qu'un tirage tombe dans la classe c ; k candidats vérifiés ; r, Δ et n comme dans la réponse 28.

**Garanties formulables.**
- **(a) Pire cas.** La probabilité de proposer c en k tirages vaut 1 − (1 − q(c))^k. Le maximum sur q du minimum sur c de q(c) vaut 1/M, atteint par la loi uniforme sur les classes. Dans le pire cas, la meilleure garantie est donc celle d'un énumérateur sans modèle. Un modèle n'améliore qu'une moyenne sous un a priori.
- **(b) Pondérée par la longueur.** On peut garantir q(c) ≥ 2^(−L(c)) pour toutes les classes à la fois, avec un code préfixe. Le temps d'atteinte est alors de l'ordre de 2^(L(c)) essais (Levin, 1973, *Universal sequential search problems*, élevée).
- **(c) Mélange défensif.** Avec q = (1 − ε)·p + ε·u, où u est une loi mécanique, q(c) ≥ ε·u(c) quel que soit le modèle. On perd au plus la fraction ε du budget (Hesterberg, 1995, *Weighted Average Importance Sampling and Defensive Mixture Distributions*, élevée).
- **(d) Rejet exact.** Écarter par programme un ensemble S de classes donne la loi conditionnelle exacte. Le gain vaut 1/(1 − p(S)), et pas davantage. Le tirage sans remise garantit k classes distinctes.
- **(e) Couverture à la résolution τ.** Avec N ≥ (1/τ)·ln(1/(τ·δ)) tirages indépendants, toutes les classes de largeur au moins τ sont vues avec probabilité 1 − δ (borne d'union sur au plus 1/τ classes). La masse restante se certifie (McAllester et Schapire, 2000, *On the Convergence Rate of Good-Turing Estimators*, élevée).
- **(f) Détection.** Avec des poids 2^(−L(c)) fixés avant les données, on retient c quand sa valeur e pondérée dépasse 1/α. Le contrôle vient de l'inégalité de Markov et de la borne d'union. Un puits est retenu dès que n·r·Δ dépasse environ L(c)·ln 2 + ln(1/α). C'est la forme du rasoir d'Occam (Blumer, Ehrenfeucht, Haussler et Warmuth, 1987, *Occam's Razor*, élevée). HYPOTHÈSE : la validité sous le nul composite de l'organisme reste à prouver.
- **(g) Maximum.** Un regret borné existe sous une hypothèse de queue paramétrique (Carpentier et Valko, 2014, *Extreme bandits*, moyenne).
- **(h) Ordre de vérification.** Sous a priori connus et indépendants, une règle d'indice est optimale (Weitzman, 1979, *Optimal Search for the Best Alternative*, élevée).

**Ce qu'aucune méthode ne garantit sans structure.**
- **Aiguille.** Si le puits est placé uniformément parmi M candidats indiscernables et que le vérificateur ne répond que oui ou non, tout algorithme, même adaptatif et aléatoire, réussit avec probabilité au plus k/M. Forme générale : Wolpert et Macready, 1997, *No Free Lunch Theorems for Optimization* (élevée).
- **Conservation.** La somme des q(c) vaut au plus 1 (borne 2 du recoupement).
- **Parité.** Une interaction d'ordre élevé sans marges demande un nombre exponentiel de requêtes statistiques. Références : Kearns, 1998, déjà cité ; Blum, Furst, Jackson, Kearns, Mansour et Rudich, 1994, *Weakly learning DNF and characterizing statistical query learning using Fourier analysis* (élevée).
- **Maximum.** Sans hypothèse de queue, aucune politique n'a de regret garanti (Nishihara, Lopez-Paz et Bottou, 2016, *No Regret Bound for Extreme Bandits*, moyenne).
- **Adaptativité.** Guider la recherche par le juge consomme sa validité (Dwork et collaborateurs, 2015, *The reusable holdout: Preserving validity in adaptive data analysis*, élevée).

**Conséquence** (HYPOTHÈSE). On peut forcer la proposition à prix connu. On ne force la découverte que si l'évidence disponible paie la longueur de description.

### 2. Méthode par méthode

Les propriétés sont des FAITS RAPPORTÉS, les échecs « ici » des HYPOTHÈSES, les épreuves des PROPOSITIONS.

**Bases communes :**
- proposeur seul répété ;
- énumérateur aléatoire (uniforme sur les classes) ;
- énumérateur ordonné par longueur croissante ;
- placebo.

**Critère commun R.** Les bras sont appariés par monde et les trois budgets sont égaux. La méthode est réfutée si la borne supérieure de l'intervalle de son écart de récupération contre la meilleure base passe sous la marge fixée d'avance. Elle l'est aussi si les fausses promotions dépassent le niveau annoncé sur les mondes nuls.

1. **Énumération, mélange défensif, recherche universelle.**
   - Principe : une part ε du budget suit une loi mécanique sur la grammaire.
   - Garantit : (b) et (c), sans hypothèse sur le modèle.
   - Ne garantit rien hors de la grammaire, ni au-delà de la longueur atteignable par le calcul.
   - Échec ici : le nombre de classes explose, et les candidats mécaniques durcissent le seuil du juge.
   - Épreuve : puits plantés à longueur croissante. Réfutée si un puits satisfaisant l'inégalité (f) est manqué plus souvent que le taux annoncé.

2. **Rejet exact et tirage sans remise.**
   - Principe : canoniser, puis écarter les classes déjà vues ou fréquentes.
   - Garantit : (d). Avec accès aux logits, tirage sans remise exact (Kool, van Hoof et Welling, 2019, *Stochastic Beams and Where to Find Them: The Gumbel-Top-k Trick for Sampling Sequences Without Replacement*, élevée).
   - Ne garantit pas plus que 1/(1 − p(S)). Un puits de largeur infime le reste.
   - Échec ici : une canonisation imparfaite laisse passer les reformulations.
   - Épreuve : gain mesuré contre gain prédit. Réfutée si le gain mesuré sort de l'intervalle prédit.

3. **Échantillonnage contre la vraisemblance** (température, pénalité de probabilité).
   - Principe : aplatir la loi jeton par jeton.
   - Garantit : rien sur les classes. Sous décodage contraint, la température infinie redonne une loi sans modèle : cette famille interpole entre deux bases.
   - Échec ici : hors contrainte, la masse part vers des chaînes invalides ; bizarrerie.
   - Épreuve : courbe de récupération selon la température, sous contrainte. Réfutée si aucun point intérieur ne bat les deux extrémités selon R.

4. **Stratification, histogramme plat, qualité-diversité, recherche de nouveauté.**
   - Principe : allouer par cellule d'un descripteur public, non selon la masse.
   - Garantit : chaque cellule reçoit son quota, et la largeur du puits devient sa largeur conditionnelle à la cellule. Parenté : Wang et Landau, 2001, *Efficient, Multiple-Range Random Walk Algorithm to Calculate the Density of States* (élevée).
   - Ne garantit rien si le puits est étroit dans toutes les cellules. La recherche de nouveauté n'a pas de borne de temps d'atteinte que je connaisse (question, non revendication).
   - Échec ici : un descripteur assorti au monde planté.
   - Épreuve : descripteur fixé avant tirage du monde, contre descripteur placebo. Critère R.

5. **Processus répulsifs et ensembles à faible dispersion.**
   - Principe : dépendance négative entre tirages.
   - Garantit : dépendance négative forte des processus déterminantaux (Borcea, Brändén et Liggett, 2009, *Negative dependence and the geometry of polynomials*, élevée). Un ensemble à faible dispersion touche toute boule de volume donné (Niederreiter, 1992, *Random Number Generation and Quasi-Monte Carlo Methods*, élevée).
   - Ne garantit rien si le puits n'est pas une boule de la métrique choisie. Le coût est exponentiel en la dimension.
   - Échec ici : répulsion entre paraphrases dans un espace de plongement.
   - Épreuve : contre tirage sans remise uniforme. Critère R.

6. **Fractionnement multiniveau.**
   - Principe : dupliquer les trajectoires qui franchissent des niveaux d'une fonction de progression.
   - Garantit : un estimateur sans biais pour toute fonction (Bréhier, Gazeau, Goudenège, Lelièvre et Rousset, 2016, *Unbiasedness of some generalized adaptive multilevel splitting algorithms*, élevée). L'efficacité exige une fonction proche de la probabilité d'aboutir.
   - Ne garantit rien sans palier. Il se réduit alors au tirage brut.
   - Échec ici : si la fonction est le juge, adaptativité, donc effondrement sur le juge.
   - Épreuve : mondes à parent, puis sans parent. Réfutée si elle ne bat pas les bases avec parent. Un gain sans parent ouvre une enquête de fuite.

7. **Entropie croisée et échantillonnage préférentiel adaptatif.**
   - Principe : recentrer la loi de tirage sur les meilleurs échantillons (Rubinstein, 1999, *The Cross-Entropy Method for Combinatorial and Continuous Optimization*, élevée).
   - Garantit : une convergence dans une famille paramétrique, pas l'optimum global.
   - Échec ici : la loi se referme sur le premier bassin trouvé, donc le plus large.
   - Épreuve : monde à bassin large médiocre et puits étroit profond. Réfutée si la concentration finale porte sur le bassin large plus souvent que sous la base.

8. **Recuit et tempering parallèle.**
   - Garantit : convergence du recuit si le refroidissement est logarithmique, de constante au moins égale à la profondeur de barrière. Le temps est donc exponentiel (Hajek, 1988, *Cooling Schedules for Optimal Annealing*, élevée).
   - Contre-résultat décisif : le tempering mélange lentement précisément quand un mode étroit côtoie un mode large (Woodard, Schmidler et Huber, 2009, *Sufficient conditions for torpid mixing of parallel and simulated tempering*, élevée pour l'existence, moyenne pour la portée).
   - Échec ici : il faut une énergie, donc un verdict servi.
   - Épreuve : hors ligne, sur un monde d'étalonnage reproduisant ce cas. Critère R.

9. **Bandits et recherche arborescente.**
   - Garantit : un regret borné sous régularité autour de l'optimum (Bubeck, Munos, Stoltz et Szepesvári, 2011, *X-armed bandits*, élevée), ou sous queue paramétrique pour le maximum.
   - Contre : un optimum profond caché derrière une branche trompeuse peut coûter un temps plus qu'exponentiel (Coquelin et Munos, 2007, *Bandit algorithms for tree search*, moyenne).
   - Échec ici : récompense tirée du juge.
   - Épreuve : allocation entre vues, hors ligne. Réfutée si elle ne bat pas l'allocation uniforme.

10. **Théorie de l'information.**
    - Garantit : pour la longueur de description, le point (f). Pour le gain d'information, des bornes sous un a priori correct (Russo et Van Roy, 2014, *Learning to Optimize via Information-Directed Sampling*, moyenne).
    - Ne garantit rien pour la surprise, maximale sur le bruit (réponse 28).
    - Épreuve : poids par longueur contre poids uniformes dans le seuil. Critère R.

11. **Stein et transport optimal.**
    - Principe : déplacer des particules vers une densité cible avec répulsion (Liu et Wang, 2016, *Stein Variational Gradient Descent: A General Purpose Bayesian Inference Algorithm*, élevée).
    - Garantit : rien ici. Il faut le gradient d'une cible connue, dans un espace continu.
    - Usage restant : mesurer l'écart entre deux lots, non chercher.

12. **Contrôle en ligne des fausses découvertes et ordre de vérification.**
    - Garantit : le niveau d'erreur d'une génération à l'autre (Javanmard et Montanari, 2018, déjà cité ; Wang et Ramdas, 2022, *False discovery rate control with e-values*, élevée). Garantit aussi l'optimalité de l'indice de réserve sous ses hypothèses (h).
    - Ne garantit pas la puissance. Le seuil croît comme le logarithme du nombre de tests.
    - Épreuve : ordre par indice contre ordre d'arrivée, a priori étalonnés sur mondes frères. Critère R.

### 3. Modèle boîte noire et vérification dominante (HYPOTHÈSES, sauf mention)

- La garantie doit reposer sur la composante mécanique. Pour atteindre un puits, il suffit d'une borne inférieure sur la probabilité de tirage, et le mélange défensif la donne sans connaître la loi du modèle. Les poids d'importance exacts ne servent qu'à estimer une probabilité.
- Une log-probabilité porte sur une chaîne, non sur une classe. La masse d'une classe est la somme sur toutes ses écritures. Elle n'est calculable que sous décodage contraint à écriture canonique unique, donc pour des modèles dont on tient les logits.
- Exclure par l'invite n'est pas conditionner. Seul le rejet par programme donne la loi conditionnelle. L'écart entre les deux se mesure.
- FAIT RAPPORTÉ (recoupement) : les appels se font en session neuve. Les formules binomiales valent donc par proposeur, non entre familles.
- Si la génération est bon marché, le rejet, le dédoublonnage et le certificat de couverture (e) sont presque gratuits. La ressource rare devient l'évidence.
- Si le juge est un calcul sur des tirages partagés, tester M candidats coûte du calcul et un seuil relevé de ln M. Si chaque vérification exige une expérience propre, la borne k/M s'applique en entier.

### 4. Combinaisons à garantie, et leur prix (PROPOSITIONS ; garanties sous réserve de preuve)

- **A. Mélange défensif sur la grammaire, rejet canonique, valeurs e pondérées par la longueur, contrôle en ligne.**
  - Garantie : tout puits de longueur au plus L est proposé en un temps borné, et retenu si son évidence dépasse le seuil (f), à niveau d'erreur tenu entre générations.
  - Prix : la part ε, un calcul exponentiel en L, un seuil relevé, la preuve sous nul composite. Rien hors grammaire.
- **B. Stratification publique, rejet, certificat de masse restante par cellule.**
  - Garantie : chaque cellule est épuisée à la résolution τ.
  - Prix : nombre de cellules multiplié par (1/τ)·ln(1/(τ·δ)) appels.
- **C. Fractionnement sur le graphe public de prérequis, plus processus de valeurs e.**
  - Garantie : absence de biais ; efficacité seulement avec parents détectables.
  - Prix : aucun guidage par le juge. S'il y en a un, des tirages frais réservés par niveau, comptés au budget.
- **D. Indice de réserve pour l'ordre de vérification.**
  - Garantie : optimalité, si les a priori étalonnés se transportent, ce qui n'est pas établi.

### 5. Ce qui a l'air de forcer et ne force rien (HYPOTHÈSES appuyées sur C2)

- Température et pénalité de vraisemblance : agissent sur les jetons, non sur les classes.
- Surprise et curiosité : attirées par le bruit.
- Répulsion dans un espace de plongement : diversité de paraphrases.
- Liste d'exclusion par invite : ce n'est pas la loi conditionnelle.
- Tempering : lent exactement sur le cas visé.
- Entropie croisée : se referme sur le bassin large.
- Recherche arborescente optimiste : sans régularité, pire que l'uniforme sur arbres trompeurs.
- Méthodes de Stein : pas de cible.
- Théorèmes « pas de repas gratuit » : ils interdisent, ils ne fournissent aucune méthode.

### 6. Ordre d'essai, du moins cher au plus cher (PROPOSITIONS)

0. **Calcul sans modèle** : nombre de classes canoniques par longueur, et inégalité (f) pour les budgets du juge. Décide jusqu'à quelle longueur la force brute suffit.
1. **Énumérateur ordonné et valeurs e pondérées**, sur mondes nuls et plantés. Décide si la garantie A tient en pratique. C'est la base que l'organisme doit battre.
2. **Rejet exact contre exclusion par invite**. Décide si l'invite approche la loi conditionnelle.
3. **Famille de températures sous décodage contraint**. Décide s'il existe un optimum intérieur.
4. **Stratification contre allocation proportionnelle**, avec descripteur placebo. Décide si un descripteur public élargit le puits.
5. **Fractionnement sur prérequis**, mondes avec et sans parent. Décide si la structure de paliers est exploitable.
6. **Ordre de vérification par indice**. Décide si des a priori se transportent.
7. **Chaînes sur plusieurs générations** avec contrôle en ligne. Décide le prix réel de la garantie complète.

### 7. Question neutre

« Un générateur aléatoire, accessible seulement par appels, produit des objets écrits dans une grammaire publique. Un vérificateur indépendant et coûteux dit si un objet possède une propriété recherchée. Certains objets qui la possèdent sont produits très rarement.
1. Que peut signifier, mathématiquement, garantir que de tels objets seront produits puis reconnus dans un budget donné ? Écrivez les énoncés possibles, avec quantificateurs et hypothèses.
2. Existe-t-il des méthodes qui donnent une telle garantie ? Pour chacune : énoncé, hypothèses, prix.
3. Existe-t-il des résultats d'impossibilité ? Énoncez-les.
4. Qu'est-ce qui change si les probabilités du générateur sont inconnues, et si vérifier coûte bien plus que produire ?
5. Quelles méthodes réputées utiles n'apportent aucune garantie, et pourquoi ?
6. Quelle expérience, sur des cas à réponse connue, vous donnerait tort ?
Citez auteurs, année et titre ; séparez ce que vous savez de ce que vous supposez ; aucun chiffre sans source. »

## D. Décisions pour le directeur

**D1. Fixer le sens contractuel de « forcer ».**
- Enjeu : sans quantificateur, toute méthode peut se dire garantie.
- Option (a), garantie de pire cas dans la grammaire publique, prix affiché — avantage : démontrable et vérifiable par un tiers ; inconvénient : muette hors grammaire.
- Option (b), gain moyen sous un a priori étalonné — avantage : couvre l'apport du modèle ; inconvénient : dépend du transport de l'a priori.
- Option (c), heuristiques seules — avantage : aucune contrainte ; inconvénient : rien d'opposable.
- Recommandation : (a) pour la revendication, (b) comme mesure. Confiance : 0,8.

**D2. Autoriser un bras sans modèle (énumérateur ordonné et valeurs e pondérées) comme premier essai et base obligatoire.**
- Enjeu : c'est la seule garantie complète. Elle peut montrer que le modèle n'apporte rien aux courtes longueurs.
- Option (a), oui, avant tout essai de méthode — avantage : peu coûteux, fixe la frontière de la force brute ; inconvénient : résultat possiblement gênant.
- Option (b), plus tard — avantage : élan sur les méthodes ; inconvénient : comparaisons sans plancher.
- Recommandation : (a). Confiance : 0,85.

**D3. Dire si une recherche peut être guidée par le juge statistique.**
- Enjeu : le fractionnement et les bandits l'exigent pour être efficaces, et la validité du juge en dépend.
- Option (a), interdit — avantage : garde intacte ; inconvénient : pas de paliers hors du graphe public.
- Option (b), permis sur des tirages d'exploration distincts, comptés au budget — avantage : mesure propre ; inconvénient : coût en données.
- Option (c), permis sur les tirages du juge — avantage : simple ; inconvénient : validité perdue.
- Recommandation : (a) en course, (b) au banc. Confiance : 0,7.

**D4. Servir la question C7 telle quelle au collisionneur (Argon, Carbon, Neon), en exigeant énoncés et contre-exemples.**
- Enjeu : obtenir des théorèmes contrôlables, non des listes de méthodes.
- Option (a), question neutre seule — avantage : ne souffle rien ; inconvénient : réponses possiblement génériques.
- Option (b), question plus la présente réponse — avantage : critique ciblée ; inconvénient : ancrage.
- Recommandation : (a) au premier temps, (b) au temps de critique. Confiance : 0,7.

FIN DE LA RÉPONSE


======== SOURCE A : réponse d'Argon ========

Voici une analyse formelle du problème de la génération aléatoire sous contrainte budgétaire avec vérification déportée. 

Afin de respecter strictement vos contraintes, chaque section sépare explicitement **ce qui est établi** (théorèmes, preuves publiées) de **ce qui est supposé** (modélisations, hypothèses de travail, extrapolations heuristiques), et aucune valeur numérique empirique n'est avancée sans être une constante mathématique issue d'une source citée.

---

### Formalisation préliminaire
**[Supposé : Cadre de modélisation]**
Soit une grammaire formelle publique $G$ au sens de Noam Chomsky (1956), *Three models for the description of language*, engendrant un langage $L(G)$. 
* Le **générateur** est un processus stochastique boîte noire produisant une suite de variables aléatoires $(X_1, X_2, \dots)$ à valeurs dans $L(G)$, de loi marginale $\mu$. Chaque tirage coûte $c_g > 0$.
* Le **vérificateur** est un oracle déterministe $V : L(G) \to \{0, 1\}$. L'ensemble des objets recherchés est $S = \{x \in L(G) \mid V(x) = 1\}$. Chaque appel à $V$ coûte $c_v > 0$.
* La **fréquence** est la mesure de probabilité $p = \mu(S) \in [0, 1]$, qui est inconnue.
* Une **stratégie** (ou algorithme) $\mathcal{A}$ observe les tirages du générateur, décide séquentiellement pour chaque tirage s'il faut payer $c_v$ pour l'évaluer par $V$, et s'arrête au temps d'arrêt $\tau$. Si $N_g$ est le nombre de tirages générés et $N_v$ le nombre d'appels au vérificateur à l'instant $\tau$, la dépense totale est $C(\tau) = c_g N_g + c_v N_v$. Le budget alloué est $B > 0$.

---

### 1. Significations mathématiques d'une « garantie » dans un budget donné

**[Établi]**
Dans le cadre de la théorie de la décision séquentielle — Abraham Wald (1945), *Sequential Tests of Statistical Hypotheses* — et de la théorie de l'apprentissage probablement approximativement correct (PAC) — Leslie G. Valiant (1984), *A Theory of the Learnable* —, la notion de « garantie » ne peut pas être simultanément déterministe en succès, bornée en budget dans le pire cas, et indépendante de $p$ sur un espace infini.

**[Supposé : Taxonomie des énoncés formels]**
On peut formuler cinq types de garanties mathématiques distinctes pour la reconnaissance d'au moins un objet valide ($\exists i \le \tau$ tel que $X_i$ a été soumis à $V$ et $V(X_i) = 1$, événement que nous noterons $\text{Succès}(\mathcal{A})$) :

1. **Garantie PAC à budget fixe (Probabiliste en succès, déterministe en budget)**
   On exige que le budget ne soit jamais dépassé et que la probabilité d'échec soit bornée, sous l'hypothèse d'une borne inférieure connue sur $p$ :
   $$\forall p_0 \in (0, 1], \forall \delta \in (0, 1), \exists B(p_0, \delta) > 0, \exists \mathcal{A}, \forall \mu \text{ telle que } \mu(S) \ge p_0 :$$
   $$\mathbb{P}_{\mu}\big(C(\tau) \le B(p_0, \delta) \land \text{Succès}(\mathcal{A})\big) \ge 1 - \delta$$

2. **Garantie de type Las Vegas (Déterministe en succès, probabiliste en budget / budget en espérance)**
   L'algorithme ne s'arrête que lorsqu'il a trouvé un objet, mais son coût moyen est garanti inférieur au budget :
   $$\forall p_0 \in (0, 1], \exists B(p_0) > 0, \exists \mathcal{A}, \forall \mu \text{ telle que } \mu(S) \ge p_0 :$$
   $$\mathbb{P}_{\mu}\big(\text{Succès}(\mathcal{A})\big) = 1 \quad \land \quad \mathbb{E}_{\mu}[C(\tau)] \le B(p_0)$$

3. **Garantie disjonctive ou de certification (Découverte ou réfutation)**
   Lorsque $p$ peut être nul ou arbitrairement proche de zéro, la garantie porte sur le fait de trouver un objet *ou* de certifier avec haute confiance que la fréquence $p$ est inférieure à un seuil critique $\epsilon$ fixé par le budget :
   $$\forall B > 0, \forall \delta \in (0, 1), \exists \epsilon(B, \delta) \in (0, 1), \exists \mathcal{A}, \forall \mu : \quad C(\tau) \le B \text{ p.s.}$$
   $$\land \quad \mathbb{P}_{\mu}\big(\text{Succès}(\mathcal{A}) \lor (\mu(S) < \epsilon(B, \delta))\big) \ge 1 - \delta$$

4. **Garantie déterministe absolue (Énumération exhaustive)**
   Elle exige que le langage soit fini, que le budget couvre l'intégralité du support et que le générateur finisse par couvrir ce support :
   $$\text{Si } |L(G)| < \infty \land \exists \mathcal{A} \text{ sans remise}, \forall \mu \text{ telle que } \mu(S) > 0, \exists B = (c_g + c_v)|L(G)| :$$
   $$C(\tau) \le B \implies \mathbb{P}_{\mu}\big(\text{Succès}(\mathcal{A})\big) = 1$$

5. **Garantie conditionnelle par filtrage syntaxique (Réduction de l'espace de vérification)**
   On intercale un filtre syntaxique calculable $F : L(G) \to \{0, 1\}$ de coût négligeable, construit à partir de la grammaire publique $G$. La garantie dépend alors de la sensibilité (rappel) $\eta = \mathbb{P}_{\mu}(F(X)=1 \mid V(X)=1)$ et de la sélectivité $\gamma = \mathbb{P}_{\mu}(F(X)=1)$ :
   $$\forall p_0, \eta_0, \gamma_0 \in (0, 1], \forall \delta \in (0, 1), \exists B > 0, \forall \mu \text{ vérifiant } (\mu(S) \ge p_0 \land \eta \ge \eta_0 \land \gamma \le \gamma_0) :$$
   $$\mathbb{P}_{\mu}\big(C(\tau) \le B \land \text{Succès}(\mathcal{A})\big) \ge 1 - \delta$$

---

### 2. Résultats établis (positifs et négatifs)

#### A. Résultats négatifs (Impossibilités)

**[Établi]**
* **Impossibilité d'un budget borné sans borne inférieure sur $p$ :** Paul R. Halmos (1946), *The theory of unbiased estimation*, démontre qu'il n'existe aucun estimateur sans biais de fonctionnelles inverses de $p$ (comme le temps d'attente $1/p$) ayant une taille d'échantillon bornée a priori lorsque $p$ peut s'approcher arbitrairement de zéro. Par conséquent, si $p \in (0, 1]$ est totalement inconnu et non minoré par un $p_0 > 0$ connu, aucun budget fini $B$ fixé à l'avance ne peut garantir $\mathbb{P}(\text{Succès}) \ge 1 - \delta$.
* **Absence de méthode universelle d'exploration boîte noire :** David H. Wolpert et William G. Macready (1997), *No Free Lunch Theorems for Optimization*, établissent que si l'on ne fait aucune hypothèse sur la corrélation entre la structure syntaxique des éléments de $L(G)$ et la fonction de vérification $V$, aucun algorithme de sélection des candidats à soumettre au vérificateur ne fait mieux, en moyenne sur toutes les fonctions $V$ possibles, qu'un tirage purement aléatoire uniforme.

#### B. Résultats positifs (Méthodes avec garanties)

**[Établi]**

**1. Échantillonnage par rejet (Monte-Carlo classique)**
* *Référence :* John von Neumann (1951), *Various techniques used in connection with random digits*.
* *Énoncé :* On génère et vérifie systématiquement chaque objet tiré jusqu'à trouver $V(X_i) = 1$ ou épuiser le budget.
* *Hypothèses :* Tirages indépendants et identiquement distribués (i.i.d.) ; connaissance d'une borne inférieure $p \ge p_0 > 0$.
* *Prix (Budget requis) :* La variable d'arrêt suit une loi géométrique de paramètre $p$. Pour garantir un succès avec probabilité $1 - \delta$, le nombre d'essais $n$ doit vérifier $(1 - p_0)^n \le \delta$, soit :
  $$B = (c_g + c_v) \left\lceil \frac{\ln(1/\delta)}{\ln\big(1/(1-p_0)\big)} \right\rceil \le (c_g + c_v) \left\lceil \frac{\ln(1/\delta)}{p_0} \right\rceil$$

**2. Théorème de la règle d'arrêt optimale (Estimation séquentielle de $p$ inconnu)**
* *Référence :* Paul Dagum, Richard Karp, Michael Luby et Sheldon Ross (2000), *An Optimal Algorithm for Monte Carlo Estimation*.
* *Énoncé :* Pour estimer $p$ inconnu à une erreur relative $\epsilon \in (0, 1)$ près avec probabilité $1 - \delta$, l'algorithme s'arrête dès qu'il a observé un nombre fixe $k$ de succès ($V(X_i) = 1$), où $k$ ne dépend que de $\epsilon$ et $\delta$. Pour trouver au moins un objet, il suffit de fixer $k=1$, ou d'utiliser leur borne pour certifier que $p$ est inférieur à un seuil si le budget est atteint avant $k$ succès.
* *Hypothèses :* Tirages i.i.d. dans $[0, 1]$.
* *Prix :* Le théorème démontre que le nombre d'appels attendu est optimal à une constante universelle près : proportionnel à $\frac{1}{p \epsilon^2} \ln(1/\delta)$, avec une constante multiplicative explicite de $4(e - 2)$ pour l'estimation générale.

**3. Filtrage en cascade et apprentissage actif (Réduction du coût de vérification)**
* *Références :* Vladimir Vapnik et Alexey Chervonenkis (1971), *On the Uniform Convergence of Relative Frequencies of Events to Their Probabilities* ; David Cohn, Les Atlas et Richard Ladner (1994), *Improving generalization with active learning*.
* *Énoncé :* Si l'on dispose d'une famille de pré-vérificateurs rapides $\mathcal{H}$ (basés sur la grammaire $G$, de coût $c_f \approx 0$) de dimension de Vapnik-Chervonenkis $d_{VC} < \infty$, on peut apprendre ou sélectionner un filtre $F \in \mathcal{H}$ qui rejette les objets avant d'appeler $V$.
* *Hypothèses :* Tirages i.i.d. ; existence d'un filtre $F \in \mathcal{H}$ ayant un taux de faux négatifs borné (il laisse passer au moins une fraction $\eta > 0$ des objets valides) et un taux d'acceptation global $\gamma \ll 1$.
* *Prix :* Une phase initiale d'étalonnage si le filtre est appris, puis un coût espéré pour trouver un objet valide réduit à :
  $$\mathbb{E}[C(\tau)] = \frac{c_g + \gamma c_v}{\eta p}$$

---

### 3. Dépendance aux paramètres du problème

#### A. Ce que l'on sait du générateur
* **[Établi]** Si le générateur est une **boîte noire totale**, on est contraint par la mesure $\mu$ telle quelle. En revanche, si l'on connaît la loi $\mu$ (par exemple si le générateur est une grammaire hors-contexte probabiliste publique — PCFG — dont on connaît les poids, même sans pouvoir les modifier), on peut calculer la vraisemblance $\mu(x)$ de chaque objet tiré. Cela permet d'appliquer l'**échantillonnage préférentiel** (*Importance Sampling*) théorisé par Herman Kahn et Andy W. Marshall (1953), *Methods of reducing sample size in Monte Carlo computations*, pour ré-estimer la probabilité d'événements rares, ou de rejeter a priori les branches syntaxiques sur-représentées par le générateur.
* **[Supposé]** Dans notre énoncé, on ne peut *qu'obtenir des tirages* du générateur : on ne peut donc pas modifier sa distribution interne, mais connaître analytiquement $\mu(x)$ permet de ne soumettre au vérificateur coûteux $V$ que les objets rares sous $\mu$, si l'on soupçonne que la propriété recherchée est diluée par des tirages redondants de haute probabilité.

#### B. La taille de la grammaire et du langage $L(G)$
* **[Établi]** Selon la hiérarchie de Noam Chomsky (1956), *Three models for the description of language*, la présence de règles récursives rend $L(G)$ dénombrablement infini. 
  * Si $|L(G)| < \infty$, on peut mémoriser les tirages déjà vus. Le problème se ramène au **problème du collectionneur de vignettes** étudié par Paul Erdős et Alfréd Rényi (1961), *On a classical problem of probability theory*. On ne paie jamais deux fois le coût $c_v$ pour le même objet.
  * Si $|L(G)| = \infty$, une distribution $\mu$ sur un langage infini présente nécessairement une queue de distribution où $\mu(x) \to 0$ lorsque la taille de l'arbre de dérivation croît — phénomène formalisé pour les grammaires probabilistes par Taylor L. Booth et Richard A. Thompson (1973), *Applying probability measures to abstract languages*. Si les objets valides $S$ ne se trouvent qu'au-delà d'une certaine profondeur syntaxique, $p$ décroît exponentiellement avec cette profondeur.

#### C. La corrélation entre les tirages
* **[Établi]** Si les tirages $(X_1, X_2, \dots)$ ne sont pas indépendants mais forment, par exemple, une chaîne de Markov sur l'espace des arbres syntaxiques (avec un temps de mélange ou un trou spectral $1 - \lambda > 0$), les bornes géométriques classiques tombent en défaut. David Gillman (1998), *A Chernoff Bound for Random Walks on Expander Graphs*, démontre une borne de type Chernoff pour les chaînes de Markov : le nombre de tirages nécessaires pour garantir la visite d'un sous-ensemble de mesure stationnaire $p$ avec probabilité $1 - \delta$ est multiplié par un facteur inversement proportionnel au trou spectral $\frac{1}{1-\lambda}$ et dépend de la distance entre la distribution initiale et la distribution stationnaire.
* **[Supposé]** Si la corrélation est positive (le générateur reste bloqué dans un sous-espace de la grammaire), le coût de génération $c_g N_g$ explose. Toutefois, si l'on filtre les doublons exacts avant d'appeler $V$, le coût de vérification $c_v N_v$ reste protégé contre l'auto-corrélation locale.

#### D. Le rapport entre le coût de vérification et le coût de production ($c_v / c_g$)
**[Supposé : Analyse asymptotique déduite de la fonction de coût $C = c_g N_g + c_v N_v$]**
* **Régime $c_v / c_g \to 0$ (Vérification gratuite) :** La stratégie optimale consiste à vérifier immédiatement chaque objet généré ($N_v = N_g$). Toute pré-analyse syntaxique de coût supérieur à $c_v$ est sous-optimale.
* **Régime $c_v / c_g \to \infty$ (Génération quasi-gratuite, vérification prohibitive) :** La stratégie optimale dissocie $N_g$ et $N_v$ ($N_g \gg N_v$). Il devient mathématiquement rentable de :
  1. Générer un très grand bassin de candidats de taille $N_g \le \frac{B}{c_g}$.
  2. Éliminer tous les doublons syntaxiques (analyse lexicale et construction de l'arbre syntaxique abstrait via la grammaire publique $G$, par exemple avec l'algorithme de Jay Earley (1970), *An efficient context-free parsing algorithm*).
  3. Ordonner ou filtrer les candidats restants pour ne soumettre au vérificateur qu'au plus $N_v \le \frac{B - c_g N_g}{c_v}$ objets distincts.

---

### 4. Garanties apportées par les méthodes répandues

**[Établi pour les propriétés théoriques / Supposé pour leur transposition au schéma générateur-vérificateur]**

| Méthode répandue | Principe dans ce cadre | Garantie mathématique apportée | Référence fondatrice |
| :--- | :--- | :--- | :--- |
| **Génération et test (*Best-of-$N$* / Échantillonnage par rejet)** | Tirer $N$ objets, les soumettre tous à $V$. | **Probabiliste conditionnelle :** Garantit un succès avec probabilité $1-\delta$ si et seulement si $N \ge \frac{\ln(1/\delta)}{p}$ et tirages i.i.d. Aucune garantie si $p \to 0$. | John von Neumann (1951), *Various techniques used in connection with random digits*. |
| **Dédoublonnage syntaxique (Mise en cache / Mémoïsation)** | Parser chaque tirage avec $G$, ne soumettre à $V$ que les objets jamais vus. | **Économie de budget sur $c_v$ :** Garantit que $N_v \le |\text{Support}(\mu)|$. Si $L(G)$ est fini et $\mu$ couvre $L(G)$, garantit le succès en un nombre fini d'appels à $V$. Ne réduit pas $N_g$. | Donald Michie (1968), *"Memo" Functions and Machine Learning*. |
| **Filtrage par modèle de substitution (*Surrogate filtering* / Cascade)** | Entraîner ou définir un classifieur rapide $\hat{V}$ sur les arbres de $G$ ; n'appeler $V$ que si $\hat{V}(x)=1$. | **Aucune garantie sans hypothèse de régularité :** Si $\hat{V}$ a un taux de faux négatifs nul ($\hat{V}(x)=0 \implies V(x)=0$), garantit le maintien de la probabilité de succès tout en réduisant $N_v$. Sinon, risque d'éliminer totalement $S$ ($p_{\text{filtré}} = 0$). | Paul Viola et Michael Jones (2001), *Rapid Object Detection using a Boosted Cascade of Simple Features*. |
| **Tests séquentiels de rapport de vraisemblance (SPRT)** | Observer les résultats de $V(X_i)$ et arrêter dès qu'une frontière de décision est franchie. | **Garantie d'arrêt optimal (Certification) :** Garantit avec confiance $1-\delta$ de trancher entre $H_0 : p \ge p_0$ et $H_1 : p \le p_1$ avec le nombre minimal d'appels espéré à $V$. | Abraham Wald (1945), *Sequential Tests of Statistical Hypotheses*. |
| **Échantillonnage par quotas structurels (Stratification sur $G$)** | Partitionner $L(G)$ en strates syntaxiques $L_1, \dots, L_k$ via $G$, et limiter les appels à $V$ par strate. | **Réduction de variance et couverture :** Garantit que le budget $c_v N_v$ n'est pas intégralement consommé par la strate majoritaire de $\mu$. Garantit un succès si $S$ est concentré dans une strate rare sous $\mu$ mais que $N_g$ est assez grand pour l'atteindre. | Jerzy Neyman (1934), *On the Two Different Aspects of the Representative Method*. |

*Note sur les méthodes de type Monte-Carlo par chaînes de Markov (Nicholas Metropolis et al. (1953), Equation of State Calculations by Fast Computing Machines) ou Programmation Génétique sur grammaires :* **[Établi]** Ces méthodes nécessitent de pouvoir *conditionner* ou *muter* les tirages précédents pour orienter le générateur. Or, votre énoncé stipule un générateur « dont on ne peut qu'obtenir des tirages » (accès passif uniquement). Ces méthodes sont donc inapplicables pour modifier la production, sauf à être utilisées a posteriori comme heuristiques de sélection au sein d'un lot déjà généré.

---

### 5. Observations, expériences ou preuves pour trancher

Pour décider quelle formulation (Section 1) et quelle méthode (Sections 2 et 4) s'appliquent à une instance concrète de ce problème, il faut soumettre le système à quatre tests décisifs — trois empiriques (qui consomment uniquement le coût de génération $c_g$ ou un budget minimal de $c_v$) et un formel.

#### 1. Expérience sur l'entropie et les collisions du générateur (Coût : $c_g$ uniquement, $N_v = 0$)
* **Protocole :** Tirer un échantillon de taille $M$ du générateur, analyser syntaxiquement les objets avec la grammaire publique $G$ et compter le nombre de collisions (doublons exacts).
* **Fondement théorique **[Établi]** :** Tugkan Batu, Lance Fortnow, Ronitt Rubinfeld, Warren D. Smith et Patrick White (2000), *Testing that distributions are close*, montrent que le taux de collision permet d'estimer la norme $\ell_2$ de la distribution $\mu$ (liée à l'entropie de Rényi d'ordre deux, Alfréd Rényi (1961), *On Measures of Entropy and Information*) en un nombre de tirages sous-linéaire par rapport à la taille du support.
* **Décision **[Supposé]** :** 
  * Si le taux de collision est élevé, le générateur est concentré sur un petit sous-ensemble effectif de $L(G)$ : le **dédoublonnage syntaxique** (mémoïsation) avant vérification est indispensable et permettra d'économiser la majeure partie du budget $c_v$.
  * Si le taux de collision est nul, le support effectif est vaste devant le budget : la mémoïsation est inutile.

#### 2. Observation de l'auto-corrélation syntaxique (Coût : $c_g$ uniquement, $N_v = 0$)
* **Protocole :** Représenter la suite des tirages $(X_1, \dots, X_M)$ par des descripteurs issus de la grammaire $G$ (profondeur de l'arbre de dérivation, fréquences d'utilisation des règles de production) et calculer la fonction d'auto-corrélation empirique ainsi que la taille d'échantillon effective (*Effective Sample Size*).
* **Fondement théorique **[Établi]** :** Charles J. Geyer (1992), *Practical Markov Chain Monte Carlo*, établit comment la somme des auto-corrélations détermine la perte d'efficacité d'un processus corrélé par rapport à un tirage i.i.d.
* **Décision **[Supposé]** :** Si une corrélation positive significative est détectée, les bornes de la loi géométrique (Section 2.B.1) sont invalidées. Il faut appliquer un sous-échantillonnage (*thinning*, consistant à jeter $k$ tirages au prix $c_g$ entre deux appels au prix $c_v$) pour restaurer une quasi-indépendance avant de payer $c_v$, et utiliser les bornes markoviennes de David Gillman (1998), *A Chernoff Bound for Random Walks on Expander Graphs*.

#### 3. Preuve formelle de décomposabilité de la propriété $V$ sur la grammaire $G$ (Coût : $0$ en tirages, purement analytique)
* **Protocole :** Analyser la définition mathématique ou algorithmique du vérificateur $V$ (si sa spécification est connue bien que son exécution soit coûteuse) au regard des règles de production de la grammaire publique $G$.
* **Fondement théorique **[Établi]** :** Bruno Courcelle (1990), *The monadic second-order logic of graphs. I. Recognizable sets of finite graphs*, démontre que toute propriété exprimable dans la logique monadique du second ordre sur des structures arborescentes (comme les arbres de dérivation d'une grammaire hors-contexte) peut être vérifiée en temps linéaire par un automate d'arbres fini. Plus généralement, Donald E. Knuth (1968), *Semantics of context-free languages*, formalise l'évaluation des propriétés par des grammaires attribuées.
* **Décision **[Supposé]** :** 
  * *Preuve positive :* Si l'on prouve que la négation de la propriété $V(x)=1$ dépend de conditions nécessaires locales sur les sous-arbres de $G$ (ex. : certains motifs syntaxiques interdisent formellement $V(x)=1$), on peut compiler un filtre syntaxique exact $F$ de coût quasi nul ($c_f \ll c_v$) à taux de faux négatifs strictement nul ($\eta = 1$). On bascule alors dans la Garantie 5 (Section 1).
  * *Preuve négative (ou vérificateur boîte noire) :* Si la propriété vérifiée par $V$ est indécidable statiquement ou théoriquement irréductible (par le théorème de Henry Gordon Rice (1953), *Classes of recursively enumerable sets and their decision problems*, si $G$ engendre des programmes Turing-complets et que $V$ teste une propriété sémantique non triviale), aucun filtre syntaxique exact sans faux négatifs n'existe. On est alors mathématiquement contraint à l'échantillonnage aveugle (Garanties 1, 2 ou 3) ou à l'apprentissage statistique risqué.

#### 4. Expérience d'apprenabilité par échantillon pilote (Coût : une fraction initiale du budget $B_0 < B$ incluant $c_v$)
* **Protocole :** Si $V$ est une boîte noire mais que $c_v \gg c_g$, consacrer un budget pilote $B_0$ à évaluer un échantillon stratifié selon la grammaire $G$. Tester si la réussite $V(x)=1$ est corrélée à la distance syntaxique dans $G$ (test d'indépendance du $\chi^2$ de Karl Pearson (1900), *On the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling*, entre les règles de production utilisées et la sortie de $V$).
* **Décision **[Supposé]** :** Si l'hypothèse d'indépendance est rejetée, la propriété recherchée présente une localité syntaxique. Il est alors optimal d'utiliser le reste du budget $B - B_0$ en stratifiant les appels à $V$ au profit des branches de la grammaire ayant montré une fréquence empirique supérieure (formalisé par les algorithmes de bandits à plusieurs bras sous budget, Tze Leung Lai et Herbert Robbins (1985), *Asymptotically efficient adaptive allocation rules*). Si l'indépendance n'est pas rejetée (ou si aucun objet valide n'est trouvé dans $B_0$), le théorème *No Free Lunch* de David H. Wolpert et William G. Macready (1997) s'applique pleinement : aucune méthode ne surpassera le tirage aléatoire dédoublonné, et l'on ne pourra offrir que la garantie disjonctive (Garantie 3) bornant supérieurement la fréquence inconnue $p$.

FIN DE LA RÉPONSE

======== SOURCE C : réponse de Carbon ========

### Préambule : Modélisation formelle et séparation épistémique

Soit $\Sigma$ un alphabet fini et $G$ une grammaire formelle publique engendrant un langage $\mathcal{L}(G) \subseteq \Sigma^*$ au sens de **Noam Chomsky (1956)**, *Three Models for the Description of Language*. Sur un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$ où les probabilités prennent leurs valeurs dans $[0, 1]$ et les fonctions indicatrices dans $\{0, 1\}$ suivant l'axiomatisation d'**Andrey Kolmogorov (1933)**, *Grundbegriffe der Wahrscheinlichkeitsrechnung*, le générateur $\mathcal{G}$ est un oracle d'échantillonnage produisant une suite aléatoire $(X_t)_{t \in \mathbb{N}^*}$ à valeurs dans $\mathcal{L}(G)$ sans accès à son code ni à sa loi interne. Soit $R \subseteq \mathcal{L}(G)$ l'ensemble des objets possédant la propriété recherchée et $\mathcal{V} : \mathcal{L}(G) \to \{0, 1\}$ le vérificateur. Un algorithme séquentiel $\mathcal{A}$, arrêté au temps d'arrêt $\tau$, engage un coût total $C(\tau) = c_{\text{gen}} N_{\text{gen}}(\tau) + c_{\text{ver}} N_{\text{ver}}(\tau) + C_{\text{aux}}(\tau)$ borné par un budget $B > 0$, où $c_{\text{gen}} > 0$ est le coût d'un tirage, $c_{\text{ver}} > 0$ celui d'une vérification, et $C_{\text{aux}}(\tau)$ celui des traitements syntaxiques sur $G$.

Conformément à la consigne, je sépare partout deux registres :
* **[Ce que je sais — Établi]** : théorèmes démontrés de probabilité, d'analyse séquentielle, de théorie de l'apprentissage et de complexité des requêtes, indépendants de toute incarnation technologique.
* **[Ce que je suppose — Modélisé]** : hypothèses nécessaires pour lever les sous-spécifications de l'énoncé. Plus précisément, je suppose dans le modèle nominal que : (a) « dit si un objet possède une propriété » signifie que $\mathcal{V}$ est exact ($\forall x \in \mathcal{L}(G), \mathcal{V}(x) = \mathbf{1}_{x \in R}$), tout en signalant ce qui s'effondre si $\mathcal{V}$ est bruité ou incomplet ; (b) « produits puis reconnus » impose qu'un objet restitué ait été validé par $\mathcal{V}(\hat{x}) = 1$ (je distingue le régime strict où $\hat{x}$ doit provenir d'un tirage de $\mathcal{G}$ du régime relâché où $\mathcal{A}$ contourne $\mathcal{G}$ en énumérant $G$) ; (c) l'analyse syntaxique via $G$ a un coût $c_{\text{syn}}$ connu, modéré devant $c_{\text{ver}}$.

Notons $\mathcal{S}(\tau)$ l'événement : « au temps $\tau$, $\mathcal{A}$ restitue au moins un objet $\hat{x} \in R$ vérifié par $\mathcal{V}(\hat{x}) = 1$ ».

---

### Première question : Significations mathématiques d'une garantie dans un budget donné

**[Ce que je sais — Établi]** Le verbe « garantir » recouvre six énoncés formels non équivalents selon l'ordre des quantificateurs, la classe $\mathcal{P}$ des lois admissibles pour $\mathcal{G}$, la nature du budget (dur ou en espérance) et le statut de la fréquence inconnue $p(\mathbb{P})$.

* **Énoncé A — Garantie déterministe dans le pire cas :**
  *Hypothèses :* $\mathcal{V}$ exact ; classe de lois $\mathcal{P}$ ; budget dur $B > 0$.
  $$\exists \mathcal{A},\ \forall \mathbb{P} \in \mathcal{P},\ \mathbb{P}\big(\mathcal{S}(\tau) \land C(\tau) \le B\big) = 1.$$
  *(Constante $1$ de certitude au sens de **Kolmogorov, 1933**.)*

* **Énoncé B — Garantie probablement approximativement correcte (PAC) uniforme sans seuil sur $p$ :**
  *Hypothèses :* $\mathcal{V}$ exact ; sous-classe $\mathcal{P}_+ = \{\mathbb{P} \in \mathcal{P} : p(\mathbb{P}) > 0\}$ ; tolérance d'échec $\delta \in (0, 1)$.
  $$\forall \delta \in (0, 1),\ \exists B > 0,\ \exists \mathcal{A},\ \forall \mathbb{P} \in \mathcal{P}_+,\ \mathbb{P}\big(\mathcal{S}(\tau) \land C(\tau) \le B\big) \ge 1 - \delta.$$

* **Énoncé C — Garantie PAC conditionnelle à une fréquence minimale $p_{\min}$ :**
  *Hypothèses :* Tirages indépendants et identiquement distribués (i.i.d.) de marginale $\mu$ sur $\mathcal{L}(G)$ avec $p = \mu(R)$ ; $\mathcal{V}$ exact ; seuil postulé $p_{\min} \in (0, 1]$.
  $$\forall p_{\min} \in (0, 1],\ \forall \delta \in (0, 1),\ \forall B \ge B_{\min}(p_{\min}, \delta, c_{\text{gen}}, c_{\text{ver}}),\ \exists \mathcal{A},\ \forall \mu,\ \Big(\mu(R) \ge p_{\min} \implies \mathbb{P}_\mu\big(\mathcal{S}(\tau) \land C(\tau) \le B\big) \ge 1 - \delta\Big).$$

* **Énoncé D — Garantie Las Vegas à budget en espérance :**
  *Hypothèses :* $\mathcal{V}$ sans faux positifs ($\mathcal{V}(x) = 1 \implies x \in R$) ; tirages i.i.d. avec $\mu(R) \ge p_{\min} > 0$ ; contrainte budgétaire portant sur l'espérance mathématique.
  $$\exists \mathcal{A},\ \forall \mu\text{ telle que }\mu(R) \ge p_{\min},\ \Big(\mathbb{P}_\mu\big(\mathcal{S}(\tau)\big) = 1 \ \land\ \mathbb{E}_\mu[C(\tau)] \le B\Big).$$

* **Énoncé E — Garantie disjonctive honnête uniforme sur tout $p \in [0, 1]$ :**
  *Hypothèses :* Tirages i.i.d. selon $\mu$ ; $\mathcal{V}$ exact ; aucune borne inférieure sur $\mu(R) \in [0, 1]$ ; droit d'abstention certifiée $\bot$.
  $$\forall B > 0,\ \forall \delta \in (0, 1),\ \exists \mathcal{A},\ \exists p_{\text{sup}}(B, \delta) \in (0, 1],\ \forall \mu,$$
  $$\mathbb{P}_\mu\Big(C(\tau) \le B \ \land\ \big[\mathcal{S}(\tau) \ \lor\ (\text{sortie} = \bot \land \mu(R) < p_{\text{sup}}(B, \delta))\big]\Big) \ge 1 - \delta.$$

* **Énoncé F — Garantie bayésienne intégrée :**
  *Hypothèses :* $\mathcal{V}$ exact ; mesure a priori $\Pi$ sur $\mathcal{P}$ concentrant une masse inférieure à $\delta$ au voisinage de $p = 0$.
  $$\forall \delta \in (0, 1),\ \exists B > 0,\ \exists \mathcal{A},\ \int_{\mathcal{P}} \mathbb{P}\big(\mathcal{S}(\tau) \land C(\tau) \le B\big)\,\mathrm{d}\Pi(\mathbb{P}) \ge 1 - \delta.$$

**[Ce que je suppose — Modélisé]** En pratique, lorsqu'un utilisateur exige une « garantie à budget donné » sans connaître $p$, il espère implicitement l'Énoncé B ; or seul l'Énoncé E est inconditionnellement tenable en boîte noire, tandis que l'Énoncé C exige un engagement externe sur $p_{\min}$.

---

### Deuxième question : Résultats positifs et négatifs établis

#### Résultats négatifs (impossibilités et bornes inférieures)

**[Ce que je sais — Établi]**
* **Réfutation de l'Énoncé B en échantillonnage pur :** Si $\mathcal{A}$ n'obtient d'objets que par tirages i.i.d. depuis $\mathcal{G}$, il effectue au plus $N \le \lfloor B / c_{\text{gen}} \rfloor$ tirages. La probabilité de n'obtenir aucun élément de $R$ vaut $(1 - p)^N$ d'après la loi binomiale de **Jakob Bernoulli (1713)**, *Ars Conjectandi*. Comme $\lim_{p \to 0^+} (1 - p)^N = 1$, pour tout budget fini $B$ et tout $\delta \in (0, 1)$, il existe $p > 0$ tel que la probabilité de succès soit strictement inférieure à $1 - \delta$. Plus généralement, l'impossibilité d'une procédure séquentielle à échantillon borné garantissant une puissance uniforme sans zone d'indifférence découle d'**Abraham Wald (1945)**, *Sequential Tests of Statistical Hypotheses*, et, dans le cadre non paramétrique, de **Raghu Raj Bahadur et Leonard J. Savage (1956)**, *The Nonexistence of Certain Statistical Procedures in Nonparametric Problems*.
* **Borne inférieure du coût espéré à $p$ inconnu :** Pour produire un élément de $R$ avec probabilité au moins $1 - \delta$ sous tirages i.i.d. indiscernables avant $\mathcal{V}$, il faut au moins $\ln(1/\delta)/\ln(1/(1-p))$ vérifications. Pour estimer simultanément $p$ inconnu à erreur relative $\epsilon \in (0, 1)$ avec probabilité $1 - \delta$, tout algorithme séquentiel requiert en espérance $\Omega\big(\frac{\ln(1/\delta)}{\epsilon^2 p}\big)$ appels d'après **Paul Dagum, Richard Karp, Michael Luby et Sheldon Ross (2000)**, *An Optimal Algorithm for Monte Carlo Estimation* (d'où provient l'exposant quadratique en $\epsilon$).
* **Bornes inférieures de recherche dans la grammaire (contournement de $\mathcal{G}$) :** Si $p = 0$ ou $p$ est infime et que l'on explore un sous-langage fini $\mathcal{L}' \subseteq \mathcal{L}(G)$ de cardinal $M$ avec $\mathcal{V}$ en boîte noire, tout algorithme déterministe requiert $M$ appels à $\mathcal{V}$ dans le pire cas, et tout algorithme randomisé à erreur bornée en requiert $\Omega(M)$ d'après **Noam Nisan et Mario Szegedy (1994)**, *On the Degree of Boolean Functions as Real Polynomials*. Même si le code d'un vérificateur polynomial $\mathcal{V}$ était ouvert, décider $\mathcal{L}' \cap R \neq \emptyset$ sur les mots de longueur bornée est NP-complet d'après **Stephen A. Cook (1971)**, *The Complexity of Theorem-Proving Procedures*.

#### Résultats positifs (méthodes offrant une garantie)

**[Ce que je sais — Établi]** Chaque méthode ci-dessous possède un domaine de validité strict :

* **Échantillonnage par rejet séquentiel couplé à la borne exacte de Clopper-Pearson** — **John von Neumann (1951)**, *Various Techniques Used in Connection with Random Digits*, et **Charles J. Clopper et Egon S. Pearson (1934)**, *The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial*.
  * *Hypothèses :* Tirages i.i.d. selon $\mu$ ; $\mathcal{V}$ exact.
  * *Énoncé :* Tirer et vérifier séquentiellement au plus $N = \lfloor B / (c_{\text{gen}} + c_{\text{ver}}) \rfloor$ objets en s'arrêtant au premier succès réalise l'Énoncé C dès que $N \ge \frac{\ln(1/\delta)}{\ln(1/(1-p_{\min}))}$ (**Bernoulli, 1713**), l'Énoncé D sans troncature si $B \ge (c_{\text{gen}} + c_{\text{ver}})/p_{\min}$ (**Wald, 1945**), et l'Énoncé E pour tout $p \in [0, 1]$ avec $p_{\text{sup}}(B, \delta) = 1 - \delta^{1/N}$ en cas de zéro succès observé (**Clopper et Pearson, 1934**).
  * *Prix :* Pire cas dur $N(c_{\text{gen}} + c_{\text{ver}}) \le B$ ; espérance non tronquée $(c_{\text{gen}} + c_{\text{ver}})/p$.

* **Mémoïsation syntaxique (déduplication avant vérification)** — **Donald Michie (1968)**, *“Memo” Functions and Machine Learning*.
  * *Hypothèses :* $\mathcal{V}$ déterministe ; test d'égalité dans $\mathcal{L}(G)$ de coût $c_{\text{hash}} \ll c_{\text{ver}}$.
  * *Énoncé :* Tabuler les objets déjà vus pour n'interroger $\mathcal{V}$ que sur les tirages inédits conserve intégralement l'événement de succès sur $N_{\text{gen}}$ tirages tout en plafonnant le nombre de vérifications au cardinal $D(N_{\text{gen}}) \le \min(N_{\text{gen}}, |\mathcal{L}(G)|)$ des objets distincts produits.
  * *Prix :* $c_{\text{gen}} N_{\text{gen}} + c_{\text{ver}} D(N_{\text{gen}}) + c_{\text{hash}} N_{\text{gen}}$.

* **Règle d'arrêt optimale $\mathcal{AA}$** — **Paul Dagum, Richard Karp, Michael Luby et Sheldon Ross (2000)**, *An Optimal Algorithm for Monte Carlo Estimation*.
  * *Hypothèses :* Tirages i.i.d. ; $\mathcal{V}$ exact ; $p \in (0, 1]$.
  * *Énoncé :* Poursuivre les essais jusqu'à observer $\Upsilon(\epsilon, \delta) = 1 + (1+\epsilon)\frac{4(e-2)\ln(2/\delta)}{\epsilon^2}$ objets positifs (constantes $1$, $2$, $4$ et $e-2$ issues du théorème de la règle d'arrêt de **Dagum et al., 2000**) garantit avec probabilité au moins $1 - \delta$ à la fois la production certifiée de ces objets et un encadrement $|\hat{p} - p| \le \epsilon p$.
  * *Prix :* Coût espéré majoré par $\frac{\Upsilon(\epsilon, \delta)}{p}(c_{\text{gen}} + c_{\text{ver}})$, optimal à facteur constant près (**Dagum et al., 2000**).

* **Cascade par pré-filtrage conforme** — **Vladimir Vovk, Alex Gammerman et Glenn Shafer (2005)**, *Algorithmic Learning in a Random World*.
  * *Hypothèses :* Suite de tirages *échangeable* ; $\mathcal{V}$ exact ; fonction de score syntaxique $s : \mathcal{L}(G) \to \mathbb{R}$ de coût $c_s \ll c_{\text{ver}}$ ; échantillon préalable de calibration comportant $m_+$ objets vérifiés positifs et autorisant un taux de perte $\alpha \ge \frac{1}{m_+ + 1}$ (borne de rang fini de **Vovk, Gammerman et Shafer, 2005**).
  * *Énoncé :* En ne transmettant à $\mathcal{V}$ que les tirages franchissant le quantile conforme empirique de niveau $1 - \alpha$ des positifs calibrés, tout futur tirage positif franchit le filtre avec probabilité au moins $1 - \alpha$ sans aucune hypothèse sur $\mu$, tandis que $\mathcal{V}$ élimine tout faux positif résiduel.
  * *Prix :* Coût de calibration $C_{\text{cal}}$, puis espérance par objet reconnu égale à $\frac{c_{\text{gen}} + c_s + q c_{\text{ver}}}{(1-\alpha)p}$, où $q = \mathbb{P}(s(X) \ge \hat{t})$ est le taux de passage du filtre.

* **Stratégie universelle de redémarrage** — **Michael Luby, Alistair Sinclair et David Zuckerman (1993)**, *Optimal Speedup of Las Vegas Algorithms*.
  * *Hypothèses :* $\mathcal{G}$ engendre des trajectoires corrélées réinitialisables indépendamment, de distribution de temps d'atteinte de $R$ inconnue.
  * *Énoncé :* La suite universelle de coupures de **Luby, Sinclair et Zuckerman (1993)** garantit l'arrêt sur un élément de $R$ (si la probabilité d'atteinte finie est non nulle) avec une espérance de coût optimale à un facteur logarithmique près sans connaître le seuil optimal $\ell^\star$.
  * *Prix :* Espérance en $O(\ell^\star \log \ell^\star)(c_{\text{gen}} + c_{\text{ver}})$ (**Luby et al., 1993**).

* **Énumération syntaxique directe de $G$** — **Noam Chomsky (1956)**, *Three Models for the Description of Language*, et **Noam Nisan et Mario Szegedy (1994)**, *On the Degree of Boolean Functions as Real Polynomials*.
  * *Hypothèses :* $|\mathcal{L}(G)| = M < \infty$ ; $R \cap \mathcal{L}(G) \neq \emptyset$ ; $\mathcal{V}$ exact ; **[Modélisé]** droit de produire les candidats par dérivation dans $G$ sans tirer dans $\mathcal{G}$.
  * *Énoncé :* Réalise l'Énoncé A (certitude $1$, même si $p(\mathcal{G}) = 0$).
  * *Prix :* $M c_{\text{ver}} + C_{\text{enum}}$ dans le pire cas.

---

### Troisième question : Dépendance aux quatre paramètres structurels

**[Ce que je sais — Établi]** et **[Ce que je suppose — Modélisé]** :

* **Savoir préalable sur le générateur $\mathcal{G}$ :**
  * **[Établi]** Sans information sur $\mathcal{G}$, $p = 0$ est possible même si $R \neq \emptyset$ (effondrement de support) : seul l'Énoncé E tient. En revanche, savoir que $\mathcal{G}$ charge uniformément par le bas un sous-langage contenant au moins $k$ solutions ($\forall x, \mu(x) \ge \mu_{\min} > 0$) fournit analytiquement $p_{\min} = k \mu_{\min}$, activant l'Énoncé C.
  * **[Supposé]** Si l'on postule que les régularités internes de $\mathcal{G}$ alignent $R$ avec une classe d'hypothèses syntaxiques de dimension finie au sens de **Vladimir N. Vapnik et Alexey Ya. Chervonenkis (1971)**, *On the Uniform Convergence of Relative Frequencies of Events to Their Probabilities*, l'apprentissage PAC de **Leslie G. Valiant (1984)**, *A Theory of the Learnable*, permet d'apprendre un filtre en amont de $\mathcal{V}$.

* **Taille de la grammaire $|\mathcal{L}(G)|$ :**
  * **[Établi]** En rejet i.i.d. pur sans déduplication, le budget requis ne dépend *que* de $p$ et $\delta$, nullement de $|\mathcal{L}(G)|$ (**Bernoulli, 1713** ; **Wassily Hoeffding, 1963**, *Probability Inequalities for Sums of Bounded Random Variables*) : que $|\mathcal{L}(G)|$ soit fini ou infini dénombrable ne change rien. En revanche, dès que $|\mathcal{L}(G)| = M \le B / c_{\text{ver}}$, la finitude de la grammaire autorise l'Énoncé A par énumération ou plafonne le coût de vérification à $M c_{\text{ver}}$ par mémoïsation (**Michie, 1968**). Si $|\mathcal{L}(G)|$ est exponentiel ou infini, l'énumération échoue (**Nisan et Szegedy, 1994**), mais $G$ demeure utile pour rejeter à faible coût tout objet syntaxiquement invalide ou hors d'une sur-approximation syntaxique connue de $R$.

* **Corrélation entre tirages :**
  * **[Établi]** À marginale constante $\mathbb{P}(X_t \in R) = p$, une corrélation positive dégrade les garanties. Pour une chaîne de Markov stationnaire réversible de trou spectral absolu $\gamma \in (0, 1]$, les inégalités de concentration markoviennes de **Daniel Gillman (1998)**, *A Chernoff Bound for Random Walks on Expander Graphs*, et **Daniel Paulin (2015)**, *Concentration Inequalities for Markov Chains by Marton Couplings and Spectral Methods*, montrent que le nombre de tirages requis pour atteindre le risque $\delta$ est multiplié par un facteur de l'ordre de $1/\gamma$ (temps de mélange). Pire : si la suite est échangeable mais non ergodique, le théorème de représentation de **Bruno de Finetti (1937)**, *La prévision : ses lois logiques, ses sources subjectives*, l'identifie à un mélange de lois i.i.d. de fréquence aléatoire $P$ ; si $\mathbb{P}(P = 0) > \delta$, aucun budget fini ne garantit jamais $1 - \delta$. À l'opposé, pour des tirages négativement associés (tels que l'échantillonnage sans remise), **Kumar Joag-Dev et Frank Proschan (1983)**, *Negative Association of Random Variables with Applications*, établissent que $\mathbb{P}(\forall t \le N, X_t \notin R) \le (1 - p)^N$ : la garantie domine strictement le cas i.i.d.

* **Rapport des coûts $\rho = c_{\text{ver}} / c_{\text{gen}}$ :**
  * **[Établi]** Si $\rho$ est petit, vérifier chaque tirage est quasi optimal ($N \approx B / c_{\text{gen}}$). Lorsque $\rho$ est très grand (« vérificateur coûteux »), vérifier systématiquement divise la capacité d'exploration par $1 + \rho$. On dissocie alors massivement $N_{\text{gen}} \gg N_{\text{ver}}$ grâce à trois leviers : (a) la déduplication syntaxique (**Michie, 1968**) ; (b) la cascade conforme (**Vovk et al., 2005**) dès que $q \ll 1 - \alpha$ ; (c) **[Supposé : structure algébrique additionnelle]** si $G$ et $R$ admettent un opérateur syntaxique groupant plusieurs candidats en une seule requête disjonctive à $\mathcal{V}$, le test par groupes de **Robert Dorfman (1943)**, *The Detection of Defective Members of Large Populations*, abaisse le coût espéré de vérification par candidat en $O(\sqrt{p}\, c_{\text{ver}})$ lorsque $p$ est faible.

---

### Quatrième question : Garanties apportées par les méthodes répandues

**[Ce que je sais — Établi]**
* **Échantillonnage répété avec vérification (*Best-of-$N$ / Pass@$k$*)** — formalisé en synthèse de code par **Mark Chen et collaborateurs (2021)**, *Evaluating Large Language Models Trained on Code*, sur le schéma de **von Neumann (1951)** :
  *Garantie :* Zéro faux positif si $\mathcal{V}$ est formellement exact (**aucune** garantie sémantique si $\mathcal{V}$ se réduit à une suite incomplète de tests d'exemples). Sur la complétude dans le budget $B$, apporte exactement les Énoncés C et E sous indépendance, et **aucune** garantie si $p$ est arbitrairement petit ou nul.
* **Vote majoritaire (*Self-Consistency*) ou tri par modèle de score sans appel final à $\mathcal{V}$** — analysable par le théorème du jury de **Nicolas de Condorcet (1785)**, *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix* :
  *Garantie :* **Aucune** dans notre cadre ! **Condorcet (1785)** prouve que la majorité ne converge vers la vérité que si la probabilité individuelle d'exactitude excède la moitié (ou surpasse toute erreur modale) ; lorsque $p$ est faible, le vote majoritaire converge exponentiellement vite vers une sortie fausse. Employé en pré-tri avant $\mathcal{V}$ sans calibration, il rétablit la justesse via $\mathcal{V}$, mais peut annuler $p > 0$ s'il filtre à tort tous les éléments de $R$.
* **Fuzzing aléatoire et test basé sur les propriétés** — **Koen Claessen et John Hughes (2000)**, *QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs* :
  *Garantie :* Uniquement l'Énoncé C ou E relativement à la mesure induite par $\mathcal{G}$, **sans aucune** garantie de couverture hors des zones favorisées par $\mathcal{G}$.
* **Élagage par sous-grammaire publique $G' \subseteq G$** — **Noam Chomsky (1956)** :
  *Garantie :* Si l'on prouve $R \subseteq \mathcal{L}(G')$, écarter $x \notin \mathcal{L}(G')$ avant $\mathcal{V}$ offre une économie **déterministe sans perte** (zéro faux négatif) sur $c_{\text{ver}}$. En revanche, contrairement au décodage contraint en boîte blanche, le générateur boîte noire ne pouvant être modifié, cela ne réduit pas $c_{\text{gen}}$.
* **Recherche locale, recuit ou évolution guidée par $\mathcal{V}$ binaire** — **Nicholas Metropolis, Arianna W. Rosenbluth, Marshall N. Rosenbluth, Augusta H. Teller et Edward Teller (1953)**, *Equation of State Calculations by Fast Computing Machines* :
  *Garantie :* **Aucune** amélioration sur le pire cas tant que $\mathcal{V}$ ne renvoie qu'un bit dans $\{0, 1\}$. Avant d'avoir trouvé un premier point de $R$, le paysage vaut uniformément $0$ : la chaîne n'a aucun gradient, perd la loi $\mu$ de $\mathcal{G}$ et subit la borne inférieure en $\Omega(M)$ de **Nisan et Szegedy (1994)**.
* **Apprentissage d'un substitut (*Surrogate*) de $\mathcal{V}$** — **Valiant (1984)** ; **Vapnik et Chervonenkis (1971)** :
  *Garantie :* Borne PAC sur l'erreur moyenne sous $\mu$, mais en régime rare ($p$ très faible), le classifieur identiquement nul atteint déjà une erreur globale au plus $p$ sans repérer aucun élément de $R$. Seule une calibration sur les positifs de type **Vovk, Gammerman et Shafer (2005)** garantit le rappel conditionnel.

---

### Cinquième question : Observations, expériences ou preuves permettant de trancher

Pour déterminer quelle réponse (et quelle méthode) s'applique à une instance donnée, trois types d'arbitrages tranchent rigoureusement :

* **Preuves mathématiques hors budget d'oracle (sur les objets publics $G$, $R$ et la spécification de $\mathcal{V}$) :**
  * **[Établi]** Calculer par combinatoire sur $G$ le cardinal $|\mathcal{L}(G)|$ (ou celui d'une sur-approximation syntaxique prouvée $G' \supseteq R$). Si $|\mathcal{L}(G')| \le B / c_{\text{ver}}$ et qu'une preuve non constructive établit $R \neq \emptyset$, cela **tranche définitivement** en faveur de l'Énoncé A par énumération. À l'inverse, démontrer par réduction depuis SAT (**Cook, 1971**) la NP-dureté de $R$ sur $\mathcal{L}(G)$ réfute (sous $\text{P} \neq \text{NP}$) l'existence d'un filtre syntaxique polynomial exact remplaçant $\mathcal{V}$.
  * **[Établi]** Prouver l'existence ou l'impossibilité d'un homomorphisme dans $G$ vérifiant $\mathcal{V}(g(x, y)) = \mathcal{V}(x) \lor \mathcal{V}(y)$ tranche algébriquement l'applicabilité du test groupé de **Dorfman (1943)**.

* **Expériences statistiques sans appel à $\mathcal{V}$ (coût négligeable lorsque $c_{\text{gen}} \ll c_{\text{ver}}$) :**
  * **[Établi] Test empirique de collisions :** Tirer un échantillon de $\mathcal{G}$ sans appeler $\mathcal{V}$ et mesurer la fréquence empirique de paires identiques, estimateur sans biais de l'indice de concentration $\sum_{x \in \mathcal{L}(G)} \mu(x)^2$ d'**Edward H. Simpson (1949)**, *Measurement of Diversity*. Un taux élevé de collisions prouve que $\mathcal{G}$ est concentré sur peu d'objets : cela **tranche** en faveur de la mémoïsation (**Michie, 1968**) et signale un danger aigu de $p = 0$ hors de ces modes. Un taux nul prouve que la déduplication n'économisera rien.
  * **[Établi] Test séquentiel d'indépendance syntaxique :** Projeter les tirages $(X_t)$ sur des observables issues de leurs arbres de dérivation dans $G$ et appliquer le test non paramétrique des séquences d'**Abraham Wald et Jacob Wolfowitz (1940)**, *On a Test Whether Two Samples are from the Same Population*. Le rejet de l'hypothèse d'indépendance/échangeabilité **invalide** les bornes binomiales de **Clopper et Pearson (1934)** ainsi que la calibration de **Vovk et al. (2005)**, forçant l'adoption des bornes markoviennes (**Paulin, 2015**) ou du redémarrage de **Luby et al. (1993)**.

* **Expérience pilote séquentielle avec $\mathcal{V}$ sur une fraction initiale du budget :**
  * **[Établi]** Consacrer un budget pilote $B_{\text{pilote}} < B$ à $N_{\text{pilote}}$ vérifications séquentielles (**Wald, 1945** ; **Dagum et al., 2000**).
    * *Observation de plusieurs succès :* Estime $p$ avec garantie PAC (**Dagum et al., 2000**) et permet de tester par la statistique de rangs de **Frank Wilcoxon (1945)**, *Individual Comparisons by Ranking Methods*, si un score syntaxique rapide sépare les objets vérifiés positifs des négatifs — tranchant empiriquement la rentabilité de la cascade conforme (**Vovk et al., 2005**) pour le reste du budget.
    * *Observation de zéro succès :* Certifie immédiatement $p < 1 - \delta^{1/N_{\text{pilote}}}$ (**Clopper et Pearson, 1934**). Si cette borne supérieure rend $(1 - p)^{N_{\text{restant}}} > \delta$ sur le budget résiduel, l'observation **prouve statistiquement** que poursuivre l'échantillonnage naïf de $\mathcal{G}$ ne pourra pas offrir de garantie PAC : il faut soit s'arrêter en délivrant le certificat négatif de l'Énoncé E, soit basculer sur l'énumération de $G$.

FIN DE LA RÉPONSE

======== SOURCE N : réponse de Neon ========

### Cadre formel et séparation épistémique

Soit $\Gamma$ une grammaire formelle publique engendrant un langage $\mathcal{X} = L(\Gamma)$ (fini ou dénombrable), $G$ un générateur aléatoire boîte noire produisant une suite de tirages $(X_t)_{t \ge 1}$ dans $\mathcal{X}$, et $V : \mathcal{X} \to \{0,1\}$ un vérificateur indépendant testant l'appartenance à un ensemble cible $S \subseteq \mathcal{X}$. On note $p = \mathbb{P}(X_t \in S) \in [0,1]$ (inconnue) la fréquence marginale des objets valides, $c_g > 0$ le coût d'un tirage de $G$, $c_v > 0$ le coût d'un appel à $V$, $r = c_v / c_g$ leur rapport, et $B > 0$ le budget. Un algorithme $\mathcal{A}$ réalise $M$ tirages et $K$ appels à $V$ sur un sous-ensemble $\mathcal{Q}(\mathcal{A})$ d'objets, pour un coût total $C(\mathcal{A}) = M c_g + K c_v$ (hors éventuel coût auxiliaire $c_{\text{aux}}$). L'événement « au moins $k \ge 1$ objets valides distincts sont produits puis reconnus » s'écrit $E_k = \{|\{x \in \mathcal{Q}(\mathcal{A}) : x \in S \wedge V(x)=1\}| \ge k\}$.

**Séparation épistémique globale.** Dans ce qui suit, on sépare explicitement ce qui est **établi** (théorèmes, bornes prouvées et résultats publiés) de ce qui est **supposé** (choix de modélisation non imposés par l'énoncé : indépendance des tirages, exactitude déterministe de $V$, coût négligeable du calcul syntaxique sur $\Gamma$, existence d'un score auxiliaire, etc.).

---

### 1. Significations mathématiques d'une garantie dans un budget donné

**Établi (logique des quantificateurs).** Lorsque $p$ est inconnue, l'expression « garantir dans un budget $B$ » correspond à plusieurs énoncés mathématiques inéquivalents selon l'ordre des quantificateurs et la classe d'instances $\mathcal{H}$ contenant $\mathcal{I} = (\mu, V)$, où $\mu$ est la loi des tirages et $p(\mathcal{I}) = \mu(S)$.

1. **Garantie déterministe (pire cas absolu)** :
   $$\exists \mathcal{A},\; \forall \mathcal{I} \in \mathcal{H},\quad \mathbb{P}_{\mathcal{A},\mathcal{I}}\big(C(\mathcal{A}) \le B \;\wedge\; E_k\big) = 1.$$
   *Hypothèses* : $\mathcal{X}$ fini, $|S| \ge k$ garanti par $\mathcal{H}$, $V$ déterministe exact, $B \ge |\mathcal{X}| c_v$ (inaccessible par tirages aléatoires i.i.d. dès que $p < 1$).

2. **Garantie probabiliste uniforme sur une classe minorée ($\mathcal{H}_{p_{\min}} = \{\mathcal{I} : p(\mathcal{I}) \ge p_{\min}\}$, $p_{\min} > 0$ connu)** :
   $$\forall \delta \in (0,1),\; \forall p_{\min} \in (0,1],\; \exists B = B(p_{\min},\delta,k,c_g,c_v),\; \exists \mathcal{A},\; \forall \mathcal{I} \in \mathcal{H}_{p_{\min}},$$
   $$\mathbb{P}_{\mathcal{A},\mathcal{I}}\big(C(\mathcal{A}) \le B \;\wedge\; E_k\big) \ge 1 - \delta.$$
   Si l'on supprime $p_{\min}$ ($\mathcal{H}_{>0} = \{\mathcal{I} : p(\mathcal{I}) > 0\}$) tout en gardant $B$ indépendant de $\mathcal{I}$, l'énoncé devient faux (section 2.1).

3. **Garantie paramétrique à budget fixe (dépendante de $p$ inconnu)** :
   $$\exists \mathcal{A},\; \forall B > 0,\; \forall \mathcal{I} \in \mathcal{H},\quad C(\mathcal{A}) \le B \;\text{ p.s. et }\; \mathbb{P}_{\mathcal{A},\mathcal{I}}(E_k) \ge \phi\big(B, p(\mathcal{I}), k, c_g, c_v\big).$$
   L'algorithme ignore $p$, respecte un budget dur, et certifie une loi de rendement minimale $\phi$.

4. **Garantie disjonctive uniforme sur tout $p \in [0,1]$ (découverte OU certificat de rareté)** :
   $$\forall \delta \in (0,1),\; \forall B > 0,\; \exists \mathcal{A},\; \forall \mathcal{I} \in \mathcal{H}_{[0,1]},$$
   $$C(\mathcal{A}) \le B \;\text{ p.s. et }\; \mathbb{P}_{\mathcal{A},\mathcal{I}}\Big(E_k \;\vee\; \big\{p(\mathcal{I}) \le u(B,\delta,k)\big\}\Big) \ge 1 - \delta.$$
   C'est la forme maximale de garantie uniforme à budget fixe sans connaissance préalable sur $p$ (y compris $p=0$).

5. **Garantie adaptative à budget aléatoire (Las Vegas / confiance fixe)** :
   $$\forall \delta \in (0,1),\; \exists \mathcal{A},\; \forall \mathcal{I} \in \mathcal{H}_{>0},\quad \mathbb{P}_{\mathcal{A},\mathcal{I}}\Big(E_k \;\wedge\; C(\mathcal{A}) \le f\big(p(\mathcal{I}),\delta,k,c_g,c_v\big)\Big) \ge 1 - \delta,$$
   ou en espérance : $\mathbb{P}(E_k) = 1$ et $\mathbb{E}[C(\mathcal{A})] \le g(p(\mathcal{I}),k,c_g,c_v)$. Le budget n'est plus fixé *a priori* indépendamment de $p$.

6. **Garantie bayésienne ou en espérance** : moyenne sur une loi *a priori* $\Pi$ sur $\mathcal{H}$, $\mathbb{E}_{\mathcal{I}\sim\Pi}[\mathbb{P}_{\mathcal{A},\mathcal{I}}(C(\mathcal{A})\le B \wedge E_k)] \ge 1-\delta$ ; ou borne sur l'espérance du nombre d'objets reconnus $\mathbb{E}[N_{\text{val}}] \ge \psi(B,p)$, strictement plus faible qu'une borne en forte probabilité.

**Supposé (hypothèses à expliciter dans chaque énoncé).** L'énoncé initial laisse ouverts des points décisifs qu'il faut fixer dans $\mathcal{H}$ : (i) loi des tirages (i.i.d. vs corrélés/non stationnaires) ; (ii) fidélité de $V$ (exact déterministe : taux de faux positifs $\alpha = 0$ et de faux négatifs $\beta = 0$, ou bruité) ; (iii) sens de l'indépendance de $V$ (indépendant de $G$ et de l'historique conditionnellement à $x$) ; (iv) nature du budget (dur presque sûr $C \le B$ vs en espérance $\mathbb{E}[C] \le B$) ; (v) coût auxiliaire $c_{\text{aux}}$ du parsing, du hachage ou d'un pré-filtre sur $\Gamma$.

---

### 2. Résultats établis : négatifs et positifs

#### 2.1. Résultats négatifs (établis)

- **Impossibilité d'une garantie uniforme à budget fixe sur $\mathcal{H}_{>0}$ et borne inférieure minimax.** Par la méthode à deux points de Le Cam — Lucien Le Cam (1973), « Convergence of Estimates Under Dimensionality Restrictions », et Alexandre B. Tsybakov (2009), *Introduction to Nonparametric Estimation* —, la distance en variation totale entre $n$ tirages i.i.d. de Bernoulli de paramètre $0$ et de paramètre $p$ vaut $1 - (1-p)^n \le np$. Plus généralement, si $\mathcal{X}$ est infini (ou de cardinal $N > K_{\max} = \lfloor B/c_v \rfloor$) et si $\mathcal{H}$ autorise tout singleton $S = \{x^*\}$ sur un sous-ensemble $\mathcal{X}_0 \subseteq \mathcal{X}$ de taille $N$ muni de la loi uniforme $\mu$, tout algorithme $\mathcal{A}$ effectuant au plus $K_{\max}$ appels à $V$ satisfait $\mathbb{E}_{x^*}[\mathbb{P}(E_1)] \le K_{\max}/N = K_{\max} p$. En faisant $N \to \infty$, $\inf_{\mathcal{I}\in\mathcal{H}_{>0}} \mathbb{P}_{\mathcal{A},\mathcal{I}}(E_1) = 0$. Sur $\mathcal{H}_{p_{\min}}$ sans lien structurel entre syntaxe et $V$, obtenir $\mathbb{P}(E_1) \ge 1-\delta$ impose dans le pire cas $K \ge \frac{\ln(1/\delta)}{\ln(1/(1-p_{\min}))} = \Omega\!\left(\frac{\ln(1/\delta)}{p_{\min}}\right)$ vérifications. En domaine fini sous loi uniforme sur les fonctions cibles, David H. Wolpert et William G. Macready (1997), « No Free Lunch Theorems for Optimization », établissent de même qu'aucune heuristique de recherche sans remise ne domine en moyenne le tirage aléatoire.
- **Impossibilité d'accélération générique par apprentissage actif ou pré-filtrage.** Sanjoy Dasgupta (2005), « Coarse Sample Complexity Bounds for Active Learning », et Steve Hanneke (2014), « Theory of Disagreement-Based Active Learning », établissent que sans hypothèse structurelle (coefficient de désaccord fini), la recherche d'une région rare par requêtes adaptatives ne bat pas asymptotiquement $\Omega(1/p)$. De plus, dans le cadre PAC — Leslie G. Valiant (1984), « A Theory of the Learnable » ; Vladimir N. Vapnik et Alexey Ya. Chervonenkis (1971), « On the Uniform Convergence of Relative Frequencies of Events to Their Probabilities » —, un classifieur substitut d'erreur globale $\varepsilon \ge p$ peut être identiquement nul et manquer tous les positifs (rappel nul).
- **Limite sémantique de la grammaire publique.** D'après Henry G. Rice (1953), « Classes of Recursively Enumerable Sets and Their Decision Problems », si $L(\Gamma)$ encode un langage Turing-complet, aucune propriété sémantique non triviale n'est décidable par analyse statique de $\Gamma$ : connaître $\Gamma$ ne permet pas de remplacer $V$ en général.
- **Effondrement sous faux positifs de $V$.** Si $V$ possède un taux de faux positifs $\alpha > 0$ et de faux négatifs $\beta < 1$, la formule de Bayes donne $\mathbb{P}(X \in S \mid V(X)=1) = \frac{p(1-\beta)}{p(1-\beta)+(1-p)\alpha}$, qui tend vers $0$ lorsque $p \ll \alpha$ : une reconnaissance unique par $V$ ne garantit plus la validité réelle.

#### 2.2. Résultats positifs (méthodes avec garantie : énoncé, hypothèses, prix)

1. **Générer-et-vérifier direct (échantillonnage i.i.d.)**
   - *Références* : William Feller (1968), *An Introduction to Probability Theory and Its Applications* ; Herman Chernoff (1952), « A Measure of Asymptotic Efficiency for Tests of a Hypothesis Based on the sum of Observations » ; Wassily Hoeffding (1963), « Probability Inequalities for Sums of Bounded Random Variables » ; Stéphane Boucheron, Gábor Lugosi et Pascal Massart (2013), *Concentration Inequalities: A Nonasymptotic Theory of Independence* ; Charles J. Clopper et Egon S. Pearson (1934), « The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial » ; Aaditya Ramdas, Peter Grünwald, Vladimir Vovk et Glenn Shafer (2023), « Game-Theoretic Statistics and Safe Anytime-Valid Inference ».
   - *Hypothèses* : tirages i.i.d. selon $\mu$, $V$ déterministe exact, $n = \lfloor B/(c_g+c_v) \rfloor$.
   - *Énoncé* : pour $k=1$, $\mathbb{P}(E_1) = 1 - (1-p)^n \ge 1 - e^{-np}$, d'où $\mathbb{P}(E_1) \ge 1-\delta$ sur $\mathcal{H}_{p_{\min}}$ dès que $n \ge \lceil \ln(1/\delta)/p_{\min} \rceil$. Pour $k \ge 1$ et $np > k$, la borne multiplicative de Chernoff donne $\mathbb{P}(E_k^c) \le \exp\!\left(-\frac{(np-k)^2}{2np}\right)$. Sans connaître $p$, Clopper et Pearson (1934) garantissent $\forall p \in [0,1]$, $\mathbb{P}(E_1 \vee \{p \le 1 - \delta^{1/n}\}) \ge 1-\delta$ (et son analogue exact pour tout $k \ge 1$ via la queue binomiale ; des bornes valides à tout temps d'arrêt sont établies par Ramdas et al., 2023).
   - *Prix* : budget dur $B = n(c_g+c_v) = \Theta\!\left(\frac{k+\ln(1/\delta)}{p_{\min}}(c_g+c_v)\right)$ ; en mode Las Vegas, coût espéré exact $\frac{k}{p}(c_g+c_v)$.

2. **Générer-et-vérifier avec déduplication / canonisation sur $\Gamma$**
   - *Références* : Irving J. Good (1953), « The Population Frequencies of Species and the Estimation of Population Parameters » ; David McAllester et Luis Ortiz (2003), « Concentration Inequalities for the Missing Mass and for Histogram Rule Error ».
   - *Hypothèses* : $V$ déterministe exact (ou invariant sous une relation d'équivalence syntaxique décidable sur $\Gamma$), coût de hachage négligeable devant $c_v$.
   - *Énoncé* : ne soumettre à $V$ que les objets jamais vérifiés conserve exactement $E_k$ sur $M$ tirages tout en n'appelant $V$ que $U_M \le M$ fois (nombre d'objets distincts). On obtient donc $\mathbb{P}_{\text{dédup}}(E_k) \ge \mathbb{P}_{\text{direct}}(E_k)$ à budget fixé, sans hypothèse supplémentaire sur $\mu$. Si aucun objet valide n'est trouvé parmi les $U_M$ vus, $p$ est majoré par la masse manquante $\sum_{x \notin \{X_1,\dots,X_M\}} \mu(x)$, dont McAllester et Ortiz (2003) prouvent une borne de concentration non asymptotique autour de l'estimateur de Good (1953).
   - *Prix* : $C = M c_g + U_M c_v \le B$ plus la mémoire en $O(U_M)$.

3. **Énumération ou échantillonnage sans remise sur $\Gamma$ (et portefeuille hybride)**
   - *Références* : Philippe Flajolet, Paul Zimmermann et Bernard Van Cutsem (1994), « A Calculus for the Random Generation of Labelled Combinatorial Structures » ; Philippe Duchon, Philippe Flajolet, Guy Louchard et Gilles Schaeffer (2004), « Boltzmann Samplers for the Random Generation of Combinatorial Structures ».
   - *Hypothèses* : tranche finie énumérable $\mathcal{X}_m \subseteq L(\Gamma)$ contenant au moins $k$ solutions, $V$ exact.
   - *Énoncé* : l'énumération exhaustive garantit $\mathbb{P}(E_k) = 1$ (même si $p=0$ sous $G$) dès que $B \ge |\mathcal{X}_m| c_v$. Le tirage uniforme sans remise sur $\mathcal{X}_m$ donne une garantie hypergéométrique strictement meilleure que l'i.i.d. de même fréquence. Allouer une fraction $\lambda \in (0,1)$ du budget à $G$ dédupliqué et $1-\lambda$ à $\Gamma$ conserve chacune des deux garanties au prix d'un facteur multiplicatif $1/\lambda$ ou $1/(1-\lambda)$ sur le budget.
   - *Prix* : $|\mathcal{X}_m| c_v$ au pire ; impraticable dès que $|\mathcal{X}_m| \gg B/c_v$.

4. **Estimation adaptative et tests séquentiels optimaux**
   - *Références* : Abraham Wald (1945), « Sequential Tests of Statistical Hypotheses » ; Paul Dagum, Richard Karp, Michael Luby et Sheldon Ross (2000), « An Optimal Algorithm for Monte Carlo Estimation ».
   - *Hypothèses* : tirages i.i.d., $V$ exact, temps d'arrêt adaptatif (budget aléatoire).
   - *Énoncé* : Dagum, Karp, Luby et Ross (2000) estiment $p$ à erreur relative $\varepsilon$ près avec probabilité $\ge 1-\delta$ sans connaître $p$, en prouvant l'optimalité jusqu'à une constante de la complexité $O\!\left(\frac{\ln(1/\delta)}{\varepsilon^2 p}\right)$. Le test SPRT de Wald (1945) décide entre $p \le p_0$ et $p \ge p_1$ en minimisant le nombre espéré d'appels sous $p_0$ et $p_1$ ; appliqué à des appels répétés de $V$ sur un même objet, il certifie aussi la décision face à un vérificateur bruité ($\alpha < 1-\beta$).
   - *Prix* : $O\!\left(\frac{\ln(1/\delta)}{\varepsilon^2 p}(c_g+c_v)\right)$ en espérance/forte probabilité ; ne lève pas l'impossibilité à budget fixe.

5. **Redémarrages universels pour générateurs avec état corrélé**
   - *Référence* : Michael Luby, Alistair Sinclair et David Zuckerman (1993), « Optimal Speedup of Las Vegas Algorithms ».
   - *Hypothèses* : possibilité de réinitialiser indépendamment le générateur sur une loi de temps d'atteinte inconnue.
   - *Énoncé* : la séquence universelle de seuils $(1, 1, 2, 1, 1, 2, 4, \dots)$ garantit un coût espéré $O(\ell^* \log \ell^*)$ où $\ell^*$ est le coût espéré optimal en connaissant la loi.
   - *Prix* : surcoût logarithmique $O(\log \ell^*)$ ; exige l'opération de réinitialisation.

6. **Filtrage calibré à risque contrôlé et inférence assistée**
   - *Références* : Jerzy Neyman et Egon S. Pearson (1933), « On the Problem of the Most Efficient Tests of Statistical Hypotheses » ; Vladimir Vovk, Alex Gammerman et Glenn Shafer (2005), *Algorithmic Learning in a Random World* ; Stephen Bates, Anastasios Angelopoulos, Lihua Lei, Jitendra Malik et Michael Jordan (2021), « Distribution-Free, Risk-Controlling Prediction Sets » ; Anastasios N. Angelopoulos, Stephen Bates, Clara Fannjiang, Michael I. Jordan et Tijana Zrnic (2023), « Prediction-Powered Inference ».
   - *Hypothèses* : score auxiliaire bon marché $s : \mathcal{X} \to \mathbb{R}$ fixé indépendamment, tirages échangeables, et jeu de calibration vérifié par $V$ (pour contrôler le risque conditionnel, ce qui suppose d'y observer des positifs).
   - *Énoncé* : un filtre $F = \{s(x) \ge \tau\}$ de sélectivité $q = \mathbb{P}(X \in F)$ et de rappel $r_{\text{rec}} = \mathbb{P}(X \in F \mid V(X)=1)$ induit (par l'identité de Wald, 1945, à coût de filtrage négligeable) un coût espéré par succès $\frac{c_g + q c_v}{p \, r_{\text{rec}}}$ ; Neyman et Pearson (1933) caractérisent le seuil optimal lorsque les lois conditionnelles sont connues. Sans connaître les lois, Bates et al. (2021) garantissent le contrôle fini du risque du filtre avec probabilité $\ge 1-\delta$ à partir d'un jeu de calibration échangeable, et Angelopoulos et al. (2023) fournissent des intervalles valides sur $p$ à variance réduite.
   - *Prix* : coût de calibration ($\Omega(1/p)$ vérifications pour borner un rappel rare sans information *a priori*), coût d'évaluation de $s$, et perte totale de garantie si $r_{\text{rec}} = 0$.

7. **Allocation adaptative entre plusieurs générateurs ou strates**
   - *Références* : Tze Leung Lai et Herbert Robbins (1985), « Asymptotically Efficient Adaptive Allocation Rules » ; Donald A. Berry, Robert W. Chen, Alan Zame, David C. Heath et Larry A. Shepp (1997), « Bandit Problems with Infinitely Many Arms » ; Jean-Yves Audibert, Sébastien Bubeck et Rémi Munos (2010), « Best Arm Identification in Multi-Armed Bandits ».
   - *Hypothèses* : accès à $J$ générateurs (ou sous-grammaires) interrogeables indépendamment, ou réservoir infini de bras.
   - *Énoncé* : identification du meilleur générateur à probabilité d'erreur exponentiellement décroissante en le budget divisé par la complexité des écarts (Audibert, Bubeck & Munos, 2010), ou compromis optimal exploration/exploitation en infinité de bras (Berry et al., 1997).
   - *Prix* : coût d'exploration croissant avec $J$ et l'inverse des écarts ; inapplicable à un unique générateur indivisible.

---

### 3. Dépendance aux quatre paramètres structurels

**3.1. Ce que l'on sait du générateur $G$.**
*Établi* : en boîte noire pure sans minorant $p_{\min}$, l'échantillonnage préférentiel — Herman Kahn et Andy W. Marshall (1953), « Methods of Reducing Sample Size in Monte Carlo Computations » ; Art B. Owen (2013), *Monte Carlo Theory, Methods and Examples* — et la méthode d'entropie croisée — Reuven Y. Rubinstein (1999), « The Cross-Entropy Method for Combinatorial and Continuous Optimization » — sont inapplicables faute d'accès aux densités $\mu(x)$ ou aux paramètres. La connaissance de $p_{\min} > 0$ fait basculer de la garantie disjonctive à la garantie uniforme à budget fixe. L'accès « boîte grise » (probabilités, redémarrages, paramètres modifiables) ouvre les redémarrages universels (Luby, Sinclair & Zuckerman, 1993), le recalibrage adaptatif ou l'allocation multi-bras. *Supposé* : si $G$ a une faible entropie mais intersecte $S$, la déduplication compense les collisions ; si $S$ est hors de son support effectif, aucune stratégie sur $G$ seul ne réussit.

**3.2. Taille et structure de la grammaire $\Gamma$.**
*Établi* : lorsque $|\mathcal{X}| \le B/c_v$ (ou sur une tranche finie $\mathcal{X}_m$ contenant $S$), l'énumération sur $\Gamma$ rend $G$ superflu et offre une garantie déterministe. Si une sous-grammaire nécessaire $\Gamma' \subseteq \Gamma$ telle que $S \subseteq L(\Gamma')$ est prouvée, le rejet syntaxique gratuit garantit $r_{\text{rec}} = 1$ et divise les appels à $V$ par $1/\mu(L(\Gamma'))$. Lorsque $|\mathcal{X}| \gg B/c_v$ (ou infini), la grammaire ne peut plus remplacer $G$ et sert principalement à la canonisation/déduplication ; pour une grammaire Turing-complète, Rice (1953) exclut tout pré-filtre sémantique exact universel.

**3.3. Corrélation entre tirages.**
*Établi* : pour des événements $E^{(t)} = \{V(X_t)=1\}$ de même probabilité $p > 0$ et de corrélations de paires $\rho_{ij} = \operatorname{Corr}(\mathbf{1}_{E^{(i)}}, \mathbf{1}_{E^{(j)}})$, l'inégalité de Kai Lai Chung et Paul Erdős (1952), « On the Application of the Borel-Cantelli Lemma », donne :
$$\mathbb{P}\!\left(\bigcup_{t=1}^n E^{(t)}\right) \ge \frac{np}{1 + (n-1)p + (1-p)\,\frac{1}{n}\sum_{i \neq j} \rho_{ij}}.$$
Une **corrélation positive** ($\rho_{ij} > 0$ : effondrement de mode, chaîne lente, graine commune) augmente le dénominateur et dégrade la probabilité d'atteinte, jusqu'à la réduire à $p$ indépendamment de $n$ si $\rho_{ij} = 1$. Pour une chaîne de Markov ergodique, les bornes de concentration se dégradent proportionnellement au temps de mélange ou à l'inverse du trou spectral — Pascal Lezaud (1998), « Chernoff-type Bound for Finite Markov Chains » ; David A. Levin, Yuval Peres et Elizabeth L. Wilmer (2009), *Markov Chains and Mixing Times* ; Daniel Paulin (2015), « Concentration Inequalities for Markov Chains by Marton Couplings and Spectral Methods ». À l'inverse, une **corrélation négative** ($\rho_{ij} < 0$ : tirage sans remise, diversification, processus ponctuels déterminantaux — Alex Kulesza et Ben Taskar, 2012, *Determinantal Point Processes for Machine Learning*) améliore strictement la garantie par rapport à l'i.i.d. *Supposé* : sur un générateur strictement boîte noire, on ne peut pas forcer $\rho_{ij} < 0$ au tirage, seulement éviter de payer $c_v$ sur les doublons.

**3.4. Rapport $r = c_v / c_g$ entre vérification et production.**
*Établi* : lorsque $r \ll 1$, le coût est dominé par $M c_g$ : il est optimal de vérifier chaque tirage, et le filtrage n'apporte aucun gain significatif. Lorsque $r \gg 1$, le budget autorise bien plus de tirages ($B/c_g$) que de vérifications ($B/c_v$). Un filtre de sélectivité $q$ et de rappel $r_{\text{rec}}$ (à coût négligeable devant $c_g$) abaisse strictement le coût espéré par succès si et seulement si
$$r_{\text{rec}} > \frac{c_g + q c_v}{c_g + c_v} = \frac{1 + q r}{1 + r}.$$
Quand $r \to 0$, ce seuil tend vers $1$ (aucun filtre imparfait n'est rentable) ; quand $r \to \infty$, il tend vers $q$ (tout enrichissement $r_{\text{rec}}/q > 1$ devient rentable, sous réserve de ne pas saturer le budget en génération). Enfin, même un filtre **parfait** ($r_{\text{rec}}=1, q=p$) conserve un coût espéré incompressible de $c_g/p + c_v$, limitant le gain maximal sur la vérification directe à un facteur $\frac{1+r}{1+pr} \le 1+r$ : aucun filtrage ne compense un $p$ trop petit devant $c_g/B$.

---

### 4. Garanties apportées par les méthodes répandues

- **Best-of-$N$ vérifié (et estimation `pass@k`)** — Mark Chen et al. (2021), « Evaluating Large Language Models Trained on Code » : *Établi* : sous i.i.d. et $V$ exact, apporte la garantie paramétrique $1-(1-p)^N$ et le certificat disjonctif de Clopper et Pearson (1934) ; l'estimateur $1-\binom{n-c}{k}/\binom{n}{k}$ est sans biais pour la probabilité de succès en $k$ essais. Aucune garantie uniforme si $p$ est sans minorant.
- **Vote majoritaire / auto-cohérence (*self-consistency*)** — Nicolas de Condorcet (1785), *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix* ; Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery et Denny Zhou (2023), « Self-Consistency Improves Chain of Thought Reasoning in Language Models » : *Établi* : le théorème de Condorcet (1785) ne garantit la convergence vers la bonne réponse que sous indépendance (ou faible corrélation) et dominance de la bonne réponse ($p > 1/2$ en binaire, ou mode unique valide). Si $p$ est faible et qu'une erreur fréquente domine, le vote converge vers l'erreur : aucune garantie générale, et risque de perte de rappel s'il filtre l'entrée de $V$.
- **Reranking par modèle de récompense / cascades** — Paul Viola et Michael Jones (2001), « Rapid Object Detection using a Boosted Cascade of Simple Features » ; Charlie Snell, Jaehoon Lee, Kelvin Xu et Aviral Kumar (2024), « Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters » : *Établi* : méthodes empiriques sans garantie distribution-free en l'absence de calibration vérifiée (Vovk, Gammerman & Shafer, 2005 ; Bates et al., 2021) ; sujettes au décalage de distribution et au rappel nul sur les objets rares.
- **MCMC, recuit simulé, recherche locale, évolutionnaire, MCTS** — Nicholas Metropolis, Arianna W. Rosenbluth, Marshall N. Rosenbluth, Augusta H. Teller et Edward Teller (1953), « Equation of State Calculations by Fast Computing Machines » ; W. Keith Hastings (1970), « Monte Carlo Sampling Methods Using Markov Chains and Their Applications » : *Établi* : inapplicables directement à un $G$ purement boîte noire ; sur $\Gamma$, la convergence asymptotique ne donne aucune garantie de temps d'atteinte en budget fini sans borne sur le trou spectral (Levin, Peres & Wilmer, 2009) ni hypothèse de régularité contournant Wolpert et Macready (1997).
- **Déduplication et pré-filtrage syntaxique nécessaire** : *Établi* : garantie exacte de non-régression (dominance stochastique) sous $V$ déterministe et $S \subseteq L(\Gamma')$. En revanche, modifier la loi interne d'un générateur par décodage contraint sans renormalisation exacte peut biaiser $\mu$ et ne bénéficie pas de cette garantie.
- **Apprentissage actif et renforcement (RL) guidé par $V$** — Richard S. Sutton et Andrew G. Barto (2018), *Reinforcement Learning: An Introduction* : *Établi* : le RL est inapplicable si $G$ n'est pas modifiable ; même si $G$ l'est, avant le premier succès (récompense creuse), la borne $\Omega(1/p)$ demeure. L'apprentissage actif n'offre de garantie de gain que sous hypothèses structurelles (Hanneke, 2014), nulles au pire cas rare (Dasgupta, 2005).
- **Portefeuille hybride (fraction $\lambda$ en vérification directe dédupliquée, $1-\lambda$ en heuristique)** : *Établi* : conserve rigoureusement la garantie de l'échantillonnage direct au budget effectif $\lambda B$ tout en exploitant les gains éventuels de l'heuristique.

---

### 5. Preuves, observations et expériences permettant de trancher

**5.1. Ce qu'une preuve mathématique tranche définitivement (indépendamment de l'expérience).**
Une preuve tranche déjà (i) l'impossibilité d'une garantie uniforme à budget fixe sur $\mathcal{H}_{>0}$, (ii) la dominance de la déduplication sous $V$ déterministe, (iii) la borne disjonctive de Clopper–Pearson, (iv) la condition exacte de rentabilité d'un filtre $r_{\text{rec}} > (1+qr)/(1+r)$ et le plancher $c_g/p+c_v$. Sur un problème concret, une preuve portant sur $(\Gamma, S)$ peut aussi trancher l'existence d'une sous-grammaire nécessaire $\Gamma'$, la finitude de $|\mathcal{X}_m| \le B/c_v$ (rendant l'énumération optimale), ou l'indécidabilité d'un pré-filtre exact (Rice, 1953).

**5.2. Observations et expériences contrôlées tranchant entre les régimes sur un système réel $(G,V,\Gamma)$.**
Pour décider quelle hypothèse est satisfaite et quelle garantie s'applique en pratique, cinq protocoles diagnostiques sont décisifs :

1. **Mesure des collisions et de la masse manquante (sans appeler $V$, puis sur pilote vérifié)** : générer $M_0$ tirages pour observer $U_{M_0}/M_0$ et le nombre de singletons (Good, 1953 ; McAllester & Ortiz, 2003), puis vérifier un échantillon pilote (ou exécuter un SPRT de Wald, 1945). *Décision* : un fort taux de collisions combiné à $r \gg 1$ quantifie le gain immédiat de la déduplication ; une masse manquante bornée faible après vérification sans succès certifie l'échec de $G$ et impose de recourir à $\Gamma$ ; zéro succès en $K_0$ vérifications borne $p \le 1 - \delta^{1/K_0}$ et tranche si $B$ est insuffisant en régime direct.
2. **Test d'autocorrélation et de variance par blocs sur $(X_t, V(X_t))$** : comparer la variance empirique par blocs à la variance binomiale et estimer $\hat{\rho}_h$. *Décision* : une autocorrélation positive significative invalide les bornes i.i.d. (Clopper–Pearson, Chernoff) et impose redémarrages (Luby, Sinclair & Zuckerman, 1993) ou bornes markoviennes (Paulin, 2015).
3. **Étalonnage d'un filtre $s$ et test du mode sur échantillon pilote aléatoire non filtré** : estimer sur des tirages vérifiés indépendants de l'entraînement la courbe $(q(\tau), r_{\text{rec}}(\tau))$ avec intervalles de confiance finis (Clopper & Pearson, 1934 ; Bates et al., 2021), et vérifier la validité du mode majoritaire. *Décision* : le filtrage n'est validé que si la borne inférieure de confiance sur $r_{\text{rec}}(\tau)$ dépasse $\frac{1+q(\tau)r}{1+r}$ ; l'échec du mode alors que des tirages minoritaires réussissent réfute l'hypothèse de Condorcet.
4. **Audit de déterminisme et de taux d'erreur $(\alpha, \beta)$ de $V$** : soumettre des objets identiques de façon répétée à $V$ et tester $V$ sur des cas témoins certifiés. *Décision* : un non-déterminisme invalide la déduplication sans ré-interrogation ; un $\alpha$ non négligeable devant $\hat{p}$ invalide la reconnaissance en un seul appel et impose la répétition (Wald, 1945 ; Hoeffding, 1963).
5. **Test de corrélation entre distance grammaticale sur $\Gamma$ et succès $V$** : appliquer des perturbations syntaxiques locales à partir d'objets tirés et tester l'enrichissement local. *Décision* : l'absence d'enrichissement confirme le régime sans structure où la recherche locale n'a pas de fondement ; un enrichissement fort justifie un portefeuille combinant recherche locale et filet de sécurité direct.

---

### Synthèse épistémique

- **Ce qui est établi** : aucune garantie uniforme à budget fixe n'existe sur $p \in (0,1]$ sans hypothèse supplémentaire ; les seules garanties rigoureuses sans connaître $p$ à budget fixe sont la garantie disjonctive (découverte ou borne supérieure sur $p$) et, si $|\mathcal{X}| \le B/c_v$, l'énumération sur $\Gamma$ ; la déduplication domine sans surcoût d'hypothèse sous $V$ déterministe ; le gain d'un filtre est gouverné par $r_{\text{rec}} > (1+qr)/(1+r)$ et borné par $1+r$ ; la corrélation positive dégrade les garanties i.i.d. ; la majorité des heuristiques répandues (vote majoritaire, reranking non calibré, recherche locale) n'apportent aucune garantie en régime rare sans hypothèses additionnelles.
- **Ce qui reste supposé (dépendant de l'instance réelle)** : l'exactitude et le déterminisme effectifs de $V$, l'indépendance ou le bon mélange des tirages de $G$, l'ordre de grandeur réel de $p$ et de $r = c_v/c_g$, le caractère négligeable du coût syntaxique, et l'existence d'un signal auxiliaire réellement corrélé à $S$ sur la distribution de $G$ — points que seules les preuves spécifiques à $(\Gamma,S)$ et les expériences de la section 5 peuvent trancher.

FIN DE LA RÉPONSE