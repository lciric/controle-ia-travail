# Question

**Cadre.** Un système automatisé d'idéation scientifique fait proposer, par plusieurs modèles de langage, des fiches d'idées : hypothèses, rapprochements entre concepts éloignés, objets mathématiques candidats, protocoles d'épreuve. Il lit des graphes de concepts datés construits sur des corpus scientifiques, du type décrit dans les faits. Il est jugé hors des modèles : par un oracle sur des mondes synthétiques où l'organisateur a caché une structure connue de lui seul ; par un juge statistique calculé par programme contre un nul formé des lois déjà connues ; par le coût de calcul. L'avis d'un modèle ne sert jamais de preuve, et aucun score de juge n'entre dans le choix des modèles ni de leur agencement. Les moyens sont modestes : calcul sur processeur d'abord, préenregistrement de toute épreuve avant la lecture d'un résultat.

On te pose cinq questions liées. Chacune est ouverte : tu peux conclure qu'une piste est vide, mal posée ou déjà occupée par des travaux publiés. Pour toute expérience que tu proposes : deux hypothèses exclusives, la métrique, le seuil, le contrôle négatif et l'issue qui falsifie chacune. Ne fais pas une réponse plus longue, fais-la plus profonde.

## 1. Quatre étapes de procédure, lues comme oracles

Dans une autre partie d'un travail d'évaluation, quatre étapes ont été adoptées ; on ne t'en donne que la forme :
(i) établir, par une procédure indépendante de la partie jugée, si l'effet allégué d'une production est réellement présent ;
(ii) une répétition générale de toute la chaîne d'évaluation sur des objets dont l'issue est connue d'avance, avant toute lecture d'un résultat réel ;
(iii) un essai pilote qui mesure ce que le générateur sait produire, accompagné d'un témoin où l'effet doit être absent ;
(iv) un second classement des mêmes objets par un lecteur aveugle à la condition, d'une autre famille de modèles que le premier.

Comment transposer la forme de chacune en oracle du système d'idéation ? Pour chacune : sa fonction de mesure ; ce qu'elle apporte que l'oracle des mondes synthétiques et le juge statistique n'apportent pas déjà, ou rien ; son entrée et sa sortie ; un objet qui doit la faire échouer ; son repli écrit d'avance. Dis lesquelles de leurs sorties pourraient légitimement servir à choisir une configuration du système, et lesquelles ne doivent servir qu'à mesurer ; si les règles du cadre se contredisent, dis-le sans trancher.

*Ce qui réfuterait la piste* : sur des mondes à structure connue, l'oracle transposé ne change aucune décision par rapport aux oracles existants, ou il admet des idées sur un monde sans structure cachée.

## 2. La profondeur d'une idée comme surprise retirée ailleurs

Le fait 3 associe un concept de départ très connecté à des idées jugées moins intéressantes. Thèse à éprouver : la profondeur d'une idée n'est pas le voisinage d'un nœud, c'est la surprise qu'elle retire ailleurs. Un modèle formel écrit la portée d'une idée comme la somme, sur les autres liens du graphe, de la baisse de surprise qu'elle leur apporte, pondérée par leur centralité.

(a) Ce que le fait 3 établit et n'établit pas pour cette thèse. (b) Une définition de la « surprise retirée ailleurs » calculable avant toute épreuve, une autre après coup, ce que « ailleurs » exclut, et le rôle de la pondération. (c) Deux ou trois estimateurs concurrents, chacun avec ses données, son calcul, son coût et le cas où il se trompe. (d) L'usage possible dans le système (tri, exploration, ou mesure seulement rapportée) et le risque qu'un proposeur apprenne à gonfler la mesure.

*Ce qui réfuterait la thèse* : à centralité et voisinage contrôlés, aucune mesure de la surprise retirée ne prédit mieux qu'un témoin une issue externe, datée après la mesure ; ou la mesure n'est pas nulle sur des témoins qui ne doivent rien apporter.

## 3. Une cinétique chimique des collisions d'idées

On propose de décrire la naissance des idées comme une cinétique : des idées qui se rencontrent, un champ d'interaction, une énergie d'activation, des catalyseurs. Un modèle existe déjà : le taux de naissance d'un lien entre deux concepts y est le produit d'une probabilité de rencontre en surface et de l'exponentielle de la somme d'un terme de compatibilité de structure et d'un terme de champ.

(a) Pour chaque terme de la cinétique, la grandeur mesurable qui lui correspond et ses données brutes, ou « écarté, aucune grandeur » ; et où ce dictionnaire redonne le modèle existant sous un autre nom. (b) Les prédictions que la cinétique ferait et que le modèle existant ne fait pas, chacune avec son test. (c) À quelle condition une énergie d'activation serait identifiable, dans un corpus et dans le système d'idéation ; dans ce dernier, quels réglages, s'il y en a, joueraient les rôles de la cinétique. (d) Ton verdict : garder, garder en partie ou écarter, avec ta confiance.

*Ce qui réfuterait la piste* : sur des données tenues à l'écart, tout ce que prédit la cinétique est prédit aussi bien par le modèle existant, à nombre de paramètres égal.

## 4. Une couche de questions ouvertes et d'anomalies

Le modèle des fiches décrit les idées comme des mariages entre concepts éloignés. Or beaucoup d'idées naissent d'une anomalie (un écart entre théorie et mesure) ou d'une question ouverte, non d'un mariage. On envisage d'ajouter une couche de questions ouvertes et d'anomalies pondérées, et de représenter l'ensemble par un hypergraphe.

(a) Les types d'objets de cette couche, leurs données brutes publiques et datées, et leur extraction. (b) De quoi le poids est fait, comment chaque facteur se mesure avant coup, comment il évolue dans le temps. (c) Comment la couche entre dans le taux de naissance des idées, et quelle prédiction elle ajoute au modèle des mariages. (d) La structure de représentation : fixe d'abord tes critères de comparaison, puis compare au moins deux structures distinctes, l'hypergraphe compris, et nomme une épreuve où elles prédisent des choses différentes.

*Ce qui réfuterait la piste* : sur une période tenue à l'écart, la couche n'améliore pas la prédiction des naissances d'idées datées par rapport au modèle des mariages seul ; ou ses poids ne peuvent être fixés qu'après coup.

## 5. Repérer les tensions par les relations, non par les mots

On cherche à repérer, dans un corpus scientifique daté, les zones de tension : désaccords entre théorie et mesure, résultats contradictoires, problèmes qui résistent, endroits où un objet ou un concept semble manquer. Un essai antérieur a compté des marqueurs de vocabulaire (aveux d'approximation, d'heuristique, de fragilité) dans des articles d'une année donnée pour prédire quels sous-domaines seraient ensuite reformulés de façon plus théorique. Il a échoué : le signal suivait surtout le style d'écriture propre à chaque discipline.

Propose des familles de méthodes distinctes qui partent des **relations** entre énoncés, entités, résultats ou articles, et non des mots. Par exemple, sans t'y limiter : relations de signe opposé établies par des groupes indépendants ; cycles de relations signées incohérents ; liens attendus par un modèle de la structure du graphe et pourtant absents ; deux chaînes de résultats qui relient les mêmes extrémités avec des conclusions incompatibles ; correspondances presque exactes entre deux domaines qui échouent toujours au même endroit ; citations de désaccord.

Pour chaque famille :
1. le principe et les hypothèses ;
2. les données brutes, publiques et datées, et l'extraction possible sans modèle entraîné après la date de coupure ;
3. la confusion de style ou de discipline qu'elle évite, et celle qu'elle n'évite pas ;
4. un contrôle négatif : un cas où elle doit ne rien trouver (relations permutées, graphe recâblé, données synthétiques sans tension introduite à dessein) ;
5. l'épreuve la moins chère qui pourrait la réfuter, avec une issue datée définie indépendamment de la méthode ;
6. ses modes d'échec.

Termine par les deux familles que tu essaierais d'abord et pourquoi.

*Ce qui réfuterait la piste* : comparées à l'intérieur d'un même champ, aucune famille ne prédit l'issue datée mieux que le comptage de vocabulaire, ou toutes trouvent autant de tensions sur le graphe recâblé que sur le vrai.

## 6. Pour finir

Les liens que tu vois entre les cinq parties, ou leur absence ; puis l'ordre dans lequel tu éprouverais ces pistes, la première épreuve à faire et son coût, marqué « illustratif ».

Règles : n'invente aucun chiffre ni aucune référence ; cite les travaux par leurs auteurs, leur année et leur titre, sans identifiant donné de mémoire, et écris « référence à vérifier » quand tu n'es pas sûr ; cherche les travaux antérieurs avant de dire une méthode nouvelle, et dis « question ouverte » plutôt que « lacune » quand tu ne trouves rien ; distingue ce qui est établi de ce qui est ta proposition ; dis « je ne sais pas » quand c'est le cas ; aucune épreuve n'est lancée, tu décris.
