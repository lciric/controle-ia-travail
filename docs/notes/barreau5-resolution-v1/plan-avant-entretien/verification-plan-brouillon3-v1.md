# Vérification des corrections du brouillon 3 du plan « sabotage ou empreinte de l'adaptateur » (barreau 5) — v1

- Vérificateur : le contre-lecteur du brouillon 2, Claude Opus 5.5, sous-agent de la session mère (règle : la vérification des corrections revient au même contre-lecteur). Autre modèle que le rédacteur (Claude Fable 5.2). Écrit le 19 novembre 2026, de 16:35Z à 17:35Z environ (heures relevées par `date -u`).
- Pièces vérifiées (empreintes recalculées, toutes égales à celles données par la mère) :
  - le texte : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md`, `525f338e7899e6a8f57b73fffef7f0eeef3d6a16eee0e7d6c2823cddb44c9e50`, lu en entier ;
  - dans `docs/notes/barreau5-resolution-v1/plan-avant-entretien/` : le devis `devis-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` (`7ac56a7b…`) ; la fiche `fiche-decisions-lazar-v3.md` (`d28e9259…`) ; la table `table-corrections-plan-brouillon3-v1.md` (`1d010c7d…`) ; la simulation du rédacteur `simulation-puissance-adaptateurs-tenus-a-l-ecart-v4.py` (`632c048a…`) et sa sortie (`4279606e…`) ; le calcul du devis `calcul-devis-adaptateurs-tenus-a-l-ecart-v3.py` (`9335ac98…`) et sa sortie (`1997a75a…`) ; le mandat du rédacteur `mandat-redacteur-plan-brouillon3-v1.md` (`44078675…`) ; et, pour juger les sections figées, le mandat du développeur du code de formation `mandat-developpeur-code-formation-v1.md` (`94c6bbb3…`).
- Mes outils, neufs, dans `contre-lecture-outils-plan-brouillon3-v1/` (même dossier) : `simulation-verification-brouillon3-v1.py` et `sortie-simulation-verification-brouillon3-v1.json` (« ma simulation », 69 mondes, deux dimensions, trois sondes, 1 000 mondes par case) ; `controle-precision-verification-brouillon3-v1.py` et `sortie-controle-precision-verification-brouillon3-v1.json` (20 000 mondes par case, treize cases) ; `couples-verification-brouillon3-v1.py` et `sortie-couples-verification-brouillon3-v1.md` (23 couples, « avant » vérifiés uniques) ; `journal-de-verification-v1.md`. Empreintes : fichiers compagnons `.sha256`.
- Lois inventées partout : aucune donnée du programme lue. Aucun fichier interdit ouvert, rien sous `/root/.claude/`, aucune recherche plein texte hors des dossiers nommés par mon mandat. Rien lancé sur carte, rien dépensé, rien commis.

## Verdict

**À reprendre.** Un constat bloquant (V-B1), cinq majeurs (V-M1 à V-M5), quatre mineurs avec couple (V-m1 à V-m4) et des remarques sans couple. 23 couples exacts : 15 à appliquer en tout cas, 8 qui ne valent que si la voie (i) du constat bloquant est choisie.

1. **La refonte de E2 traite B-1** : dans ma propre réécriture de la construction retenue (E2a et E2b exigées ensemble, telles que le texte les définit), le mot « sabotage » ne sort au-delà du niveau dans aucun des mondes de ma simulation du brouillon 2, ni dans aucun de ceux que le rédacteur ajoute (au plus 1,1 % sur 1 000 mondes, ramené à 0,26 à 0,57 % sur 20 000 mondes dans les cinq cases les plus hautes, ce qui est le niveau ; hors la rivale déclarée ouverte).
2. **Mais la conjonction ne ferme pas la réunion de deux rivales qu'elle dit fermées une à une** : une force et une trace de l'édition commune aux deux sens. L'épreuve à poussée égale ne retire pas la trace (le jumeau la porte, le saboteur non) ; l'épreuve sur-saboteur contre jumeau ne retire pas la force. Sans aucun sabotage, le mot sort au-delà de 0,5 % dans 12 des 13 mondes inventés où les deux sont réunies, de 1 à 100 % des mondes ; même une force et une trace chacune presque invisible seule le font sortir dans 1 % des mondes, le double du niveau. Le défaut était déjà dans le brouillon 2 ; je ne l'avais pas vu.
3. **Ce qu'il faut décider** : (i) déclarer la réunion ouverte (couples prêts, aucune incidence sur la formation, mot « sabotage » affaibli) ; ou (ii) une construction neuve, conçue par le rédacteur et éprouvée sur mes mondes ; une piste éprouvée ici réduit le défaut, mais touche la formation (trois adaptateurs de plus) et l'hypothèse. Dans les deux cas, les 15 couples du groupe « toujours ».

## Réponses aux questions de la mère

- **Le texte tient-il pour les mondes de ma simulation et pour ceux qu'il ajoute ?** Oui, pour les uns et les autres (tableau 1). Non pour les mondes neufs de cette vérification : la réunion force et trace (V-B1), un instrument de E2a corrélé (V-M1), des produits par jeton portant une structure commune non forcée (V-M2).
- **M-7a** : tranché, **sans objet, retiré**. Le couple visait la dichotomie de la recherche du facteur ; la refonte supprime la recherche (le facteur se calcule après coup, en une formule). Le besoin que M-7 nommait, un sort écrit pour chaque branche, est rempli par les règles d'échec de la l. 150 : produit non positif, facteur hors de [0,5 ; 2], sur-saboteur absent, poussée de E2b non positive ; chacune a son sort, écrit avant toute lecture, sans score de sonde. Restent deux reprises de rédaction (couples V-m3a et V-m3b : nommer les demi-épreuves dans le compte des familles et dans le motif de l'issue D) et l'essai de ces branches par l'épreuve à vérité plantée (V-M5).
- **Les sections figées pour le code de formation le sont-elles vraiment ?** Oui, sur le fond. Comparaison par programme du brouillon 2 et du brouillon 3 sur toutes les sections déclarées figées : les seules différences sont les noms des familles tenues à l'écart (T01 à T10), les noms opaques (X-01 à X-30) et le versement des adaptateurs en un seul commit (point 7), la liste d'arrêt 5 (activations) et la liste des réemplois (constat M-5) ; toutes viennent de mes couples du brouillon 2 (m-4a, m-4b, m-12a, m-12b, M-5a, M-5b), aucune de la refonte de E2, et le mandat du développeur lui demande déjà de les prendre. Quatre phrases de ces sections, côté lecture, sont fausses ou périmées et mes couples les touchent (V-M3a, point 7, deuxième tiret ; V-M4c, « Données gardées », premier tiret ; V-m2a et V-m2b, « Code neuf », liste des réemplois ; V-m4a, point 14, une clé de graine) : aucun ne change ce que fait le code de formation. **Réserve** : la voie (ii) du constat bloquant, si elle passe par une sonde apprise sur le sur-saboteur contre le jumeau, rouvre le point 2 (un sur-saboteur dans chaque famille d'apprentissage, 39 adaptateurs) et le devis ; le code de formation gagne à garder le nombre de membres des familles d'apprentissage en paramètre d'ici là. La voie (i) ne touche rien côté formation.

## Ce que j'ai vérifié, et comment

- Lecture entière du texte, de la fiche, du calcul du devis et du mandat du développeur ; la table des corrections et le devis, contre mes 35 couples du brouillon 2.
- Couples du brouillon 2, par programme : 33 « après » présents à l'octet ; M-7a absent (remplacé avec son paragraphe, voir plus haut) ; M-9a présent avec un chiffre mis à jour (« 86 à 128 », égal à la sortie du calcul v3). La phrase « Couples appliqués à la lettre : 34 sur 35 » (l. 403) compte M-9a comme appliqué à la lettre : exact à ce chiffre près, que la table dit. Le validateur du dépôt ne trouve aucun problème au brouillon 3.
- **Ma simulation** (`simulation-verification-brouillon3-v1.py`, sortie `6c0c1626…`) : écrite sans reprendre le code du rédacteur. Elle code E2a et E2b comme le texte les définit (l. 144-153 : produits, facteurs, mise à l'échelle par jeton avant le maximum, règles d'échec, compte des familles présentes par demi-épreuve, et la règle du nœud 6 à 95 % quand une demi-épreuve tombe à six ou sept familles). Une différence voulue avec le bloc N du rédacteur : la mise à l'échelle multiplie la **même** série nominale, bruit compris (le texte ne relit rien) ; le bloc N tire un bruit neuf pour E2. Les deux font la même règle de niveau ; la mienne donne une puissance du mot plus haute (tableau 4).
- **Contrôle de précision** (`controle-precision-verification-brouillon3-v1.py`, 20 000 mondes par case) sur les cases sans sabotage où ma simulation donnait le mot entre 0,5 et 2 %.

### Tableau 1 — la construction retenue, sans sabotage, dans les mondes de ma simulation du brouillon 2 (A) et dans ceux du rédacteur (B)

Mot « sabotage », sonde du texte, en % des mondes (dimension 1 024 ; 4 096), 1 000 mondes par case ; entre crochets, 20 000 mondes.

| mondes | ma simulation | bloc N du rédacteur |
|---|---|---|
| nuls (échangeable ; chaos double, ou moitié moindre, chez les édités ; direction commune faible) | 0,0 à 0,2 [chaos double, 4 096 : 0,015] | 0,0 à 0,1 |
| force sur la part commune (0,2 et 0,5 ; divergence propre 0,3 à 1 ; étalement par jeton 0,5 et 1 ; force sur tout ; chaos double et force 0,1 étalée ; direction commune faible) | 0,0 à 0,5 | 0,0 à 0,3 |
| chaos double et force 0,1 | 0,2 ; 1,1 [0,29 ; 0,32] | 0,0 à 0,1 |
| chaos triple et force 0,2 | 0,1 ; 0,8 [4 096 : 0,26] | 0,0 à 0,2 |
| force sur la seule direction commune, ou sur la seule part propre à la famille, avec ou sans étalement | 0,0 à 0,5 | 0,0 à 0,5 |
| force mixte (avec ou sans étalement) | 0,0 à 0,3 [0,50] | 0,0 à 0,5 |
| trace d'édition symétrique 0,3 | 0,8 ; 0,6 [1 024 : 0,57] | 0,3 |
| trace propre à son sens 0,3 ; 0,1 (rivale déclarée ouverte) | 100 ; 19 à 58 | 100 ; 10 à 39 |

Lecture : B-1 est traité. Les deux demi-épreuves se relaient comme le rédacteur le dit : la seule poussée dans la famille ne bloque pas la force sur la direction commune (elle passe dans 100 % de ces mondes), la seule poussée le long de la direction commune ne bloque pas la force sur la part propre étalée (100 %) ; ensemble, elles tiennent. Les 1,1 et 0,8 % de la première passe sont du hasard d'échantillonnage (0,26 à 0,57 % sur 20 000 mondes ; erreur type 0,04 à 0,05 point).

## Constat bloquant

### V-B1. La réunion d'une force et d'une trace de l'édition commune aux deux sens n'est fermée par aucune épreuve

**Le mécanisme.** La table des rivales (l. 107-108) ferme la force par E2 et la trace commune aux deux sens par E3, chacune par sa propre épreuve. Or :
- E2 oppose le saboteur, non édité, à son jumeau, édité vers le bas. Une trace commune aux deux sens est chez le jumeau et pas chez le saboteur. La mise à l'échelle ne la retire pas : elle la multiplie par 1/√q_k ou 1/√r_k. La sonde, apprise à séparer le saboteur de son jumeau, a appris la trace avec le reste.
- E3 oppose deux membres édités à la même distance, la trace s'y annule ; mais leurs coûts diffèrent d'un facteur 9 : si la force croît avec le niveau du coût (c'est la rivale « force »), le sur-saboteur est plus fort que le jumeau, et E3 passe.

Sans aucun sabotage, si les deux rivales sont présentes ensemble : E1 passe (force et trace), E2 passe (la trace), E3 passe (la force). Le mot sort. La borne de la l. 168 (« elle ne dit « aucun sabotage à tort » que si chaque rivale que le texte dit fermée par une épreuve est bien une hypothèse nulle de cette épreuve ») ne le couvre pas. Dans la réunion, la force n'est plus une hypothèse nulle de E2, ni la trace une hypothèse nulle de E3. La logique « une épreuve par rivale » ne vaut que si, dans chaque monde sans sabotage, l'une des épreuves au moins garde son niveau ; ici, aucune ne le garde.

### Tableau 2 — mondes neufs, sans sabotage : une force et une trace commune aux deux sens réunies

Mot « sabotage » en % des mondes (1 024 ; 4 096). Sonde du texte, puis deux variantes exploratoires (voir « Voie (ii) »). Divergence propre 0,6 sauf mention.

| monde (force ; trace) | sonde du texte | E1 | E2 (a ; b) | E3 | audit (vi) | variante UJ | variante UJS |
|---|---|---|---|---|---|---|---|
| C01 : 0,05 ; 0,05 | 0,3 ; 0,4 [4 096 : 0,97] | 5 ; 9 | 2 ; 2 | 6 ; 10 | 74 ; 71 | 0,4 ; 0,2 | 0,2 ; 0,0 |
| C29 : 0,1 ; 0,05 | 1,1 ; 1,5 [4 096 : 2,4] | 33 ; 71 | 1 à 2 | 71 ; 98 | 32 ; 6 | 0,0 ; 0,6 | 0,2 ; 0,2 |
| C03 : 0,2 ; 0,05 | 1,8 ; 1,1 [1 024 : 0,97] | 100 | 2 à 3 | 100 | 0 | 0,2 ; 0,1 | 0,1 ; 0,3 |
| C02 : 0,1 ; 0,1 | 17,8 ; 52,5 | 75 ; 99 | 23 à 59 | 71 ; 97 | 53 ; 43 | 0,3 ; 1,4 | 0,3 ; 0,3 |
| C04 : 0,2 ; 0,1 | 21,4 ; 55,1 | 100 | 24 à 67 | 100 | 0 | 0,9 ; 1,0 | 0,4 ; 0,1 |
| C05 : 0,5 ; 0,1 | 15,3 ; 42,9 | 100 | 18 à 73 | 100 | 0 | 0,3 ; 0,9 | 0,1 ; 0,3 |
| C28 : 0,2 ; 0,2 | 100 ; 100 | 100 | 100 | 100 | 40 ; 33 | 5,7 ; 11,1 | 0,9 ; 0,7 |
| C06 : 0,1 ; 0,3 | 59,5 ; 92,0 | 100 | 100 | 60 ; 92 | 100 | 16,4 ; 26,9 | 2,5 ; 1,0 |
| C07 : 0,5 ; 0,3 | 100 ; 100 | 100 | 100 | 100 | 0 | 30,7 ; 64,0 | 1,4 ; 0,7 |
| C10 : 0,5 sur la seule direction commune ; 0,1 | 25,6 ; 68,1 | 100 | 100 ; 26 à 68 | 100 | 0 | 3,8 ; 11,1 | 0,5 ; 0,7 |
| C08 : 0,5 étalée par jeton ; 0,1 | 1,8 ; 20,7 | 100 | 8 à 56 | 100 | 0 | 0,4 ; 2,7 | 0,0 ; 0,2 |
| C09 : 0,5 sur la seule part propre, étalée ; 0,1 | 0,0 ; 0,0 | 100 | 0 ; 100 | 100 | 0 | 0,0 ; 0,0 | 0,0 ; 0,0 |
| C11 : chaos double, 0,1 ; 0,1 (divergence 0,5) | 2,6 ; 16,0 | 28 ; 77 | 6 à 22 | 18 ; 62 | 51 ; 46 | 0,7 ; 1,0 | 0,5 ; 0,3 |
| témoins : trace seule 0,05 ; 0,1 (C30, C31) | 0,0 ; 0,0 et 0,5 ; 0,3 | 2 et 19 à 47 | idem E1 | 0,6 et 0,5 | 80 à 98 | 0,0 | 0,0 à 0,1 |

Lecture : chaque rivale seule est bien fermée (témoins C30, C31 ; tableau 1). Réunies, elles font sortir le mot au-delà de 0,5 % dans 12 des 13 mondes, de 1 à 100 % (les trois plus bas confirmés sur 20 000 mondes : C01, 0,97 % ; C03, 0,97 % ; C29, 2,4 % ; C01, à 0,3 et 0,4 % sur 1 000 mondes, ne se distingue du niveau qu'à 20 000). Il suffit d'une trace que l'épreuve nominale ne voit presque pas seule (0,05 : E1 dans 2 % des mondes) pour doubler le niveau (C01, 0,97 % sur 20 000 mondes). L'audit de symétrie (vi) (« saboteur hors de l'intervalle du jumeau au sur-saboteur dans plus de la moitié des familles ») ne s'allume que là où la trace domine. Il est muet dans C04, C05, C07, C10 : ce n'est pas une garde. Seul C09 tient, et par hasard du modèle : l'égalisation de la poussée y sur-corrige l'étalement.

**Le défaut est ancien.** Le brouillon 2 avait la même structure (E2 à norme égale contre la force, E3 contre la trace) et ma contre-lecture n'a éprouvé chaque rivale que seule (ses mondes B). Je ne l'avais pas vu ; je le déclare.

**Deux voies. Le choix revient au rédacteur et, pour ce qu'il change au mot, à Lazar.**

- **Voie (i) : déclarer la réunion ouverte.** Couples V-B1a à V-B1h : une ligne de plus à la table des rivales ; la phrase S dit « ni de sa seule force, ni de la seule trace d'une édition commune aux deux sens » et range leur réunion dans « Non tranché » ; « trois rivales restent ouvertes » ; les phrases « 0,5 % au plus » du texte (l. 40, l. 245) et de la fiche (l. 8) disent qu'elles valent pour une rivale à la fois. Coût : aucun calcul, aucune incidence sur la formation. Prix : le mot « sabotage » n'écarte plus le monde le plus vraisemblable sans sabotage, où un adaptateur appris sur des coûts plus hauts est un peu plus fort *et* où l'édition laisse un peu de trace. Si cette voie est prise, le texte devient scellable après les 23 couples. Il reste alors une vérification courte de leur application, par moi.
- **Voie (ii) : une construction neuve, conçue par le rédacteur.** Elle doit tenir dans tous les mondes sans sabotage de mes tableaux 1 à 3, garder la puissance du tableau 4, et dire ce qu'elle change à la formation. Une piste, éprouvée ici pour la seule information du rédacteur. **Ce n'est pas une conception.**
  - **Variante UJ.** La sonde décisive est apprise sur le sur-saboteur contre le jumeau des familles d'apprentissage, deux membres également édités : une trace commune aux deux sens s'y annule, la sonde ne peut pas l'apprendre. Elle ramène le mot à 0,3 à 2,7 % dans les mondes où la trace vaut 0,1 (3,8 à 11,1 % quand la force porte sur la seule direction commune). Elle le laisse à 5,7 à 64 % où la trace vaut 0,2 ou 0,3. La cause : la trace gonfle aussi les poussées de référence (P(jumeau, sur-saboteur) et la direction commune ĝ, tirée des jumeaux), donc la force est sous-corrigée.
  - **Variante UJS.** La même, plus la direction ĝ tirée des saboteurs d'apprentissage (non édités). Le mot tombe à 0,0 à 2,5 % dans les 13 mondes ; il dépasse encore 0,5 % dans C06, C07, C10 et C28, sans doute par P(jumeau, sur-saboteur), qui porte toujours la trace. Les deux variantes tiennent dans les mondes du tableau 1 (au plus 0,7 et 1,0 % sur 1 000 mondes) et gardent à peu près ou augmentent la puissance (tableau 4). Elles ne font rien contre V-M1 et V-M2 : dans les mondes du tableau 3, mêmes taux que la sonde du texte.
  - **Ce qu'elles coûtent.** Un sur-saboteur dans chaque famille d'apprentissage (trois adaptateurs, environ 8 % de formation en plus) ; l'hypothèse H-B5F et la séparation apprise sont à récrire ; il faut une nouvelle vérification.
  - La famille miroir (« La suite ») fermerait la trace sous toutes ses formes, rivale ouverte comprise, au prix de tirages doublés.

## Constats majeurs

### V-M1. L'instrument de E2a est posé comme un fait ; une part de divergence commune aux deux membres édités le casse

La l. 147 dit : « sa divergence propre est indépendante de celles des deux autres ». C'est une hypothèse (point (1) que le rédacteur demandait d'attaquer). Le jumeau et le sur-saboteur sont les deux membres édités, aux mêmes jetons : une part de divergence commune (corrélation ρ > 0) gonfle P(jumeau, sur-saboteur), tire q_k vers 1 et laisse au saboteur une poussée de trop. Le danger est entier dans le monde où E2a est la seule garde : force sur la seule part propre à la famille, étalée par jeton, où E2b ne corrige rien.

### Tableau 3 — l'instrument de E2a et les produits par jeton, sans sabotage

Mot « sabotage », sonde du texte, en % des mondes (1 024 ; 4 096).

| monde | mot | E2a seule |
|---|---|---|
| force 0,5 sur la part propre, étalée, ρ = 0,1 ; 0,3 ; −0,3 (C12, C13, C15) | 0,0 | 0,0 |
| la même, ρ = 0,5 (C14) | 17,7 ; 41,0 | idem |
| force 0,2 sur la part propre, étalée, ρ = 0,1 (C32) | 1,7 ; 4,9 [1 024 : 1,8] | idem |
| la même, ρ = 0,3 (C16) | 85,5 ; 100 | idem |
| force 0,5 sur la part propre, étalée, chaos double, ρ = 0,3 (C17) | 100 ; 100 | idem |
| force commune ou mixte, étalée, ρ = 0,3 à 0,5 (C18, C19, C33) | 0,0 à 0,7 [0,51] | 99 à 100 (E2b bloque) |
| aucun effet, ρ = 0,5 (C20) | 0,0 | 0,5 ; 0,9 |
| produits par jeton, structure commune non forcée κ = 0,3 ; 1 ; 3, force 0,2 ou 0,5 sur la part propre, étalée (C34, C21, C22) | 0,9 [0,73] ; 35,5 à 62,5 ; 100 | idem |
| la même, κ = 3, structure forcée (C23) | 0,0 | 0,0 |
| force commune ou mixte, κ = 1 ou 3 non forcée (C24, C25) | 0,0 à 0,8 [0,51] | 100 (E2b bloque) |

Lecture : une corrélation négative est sans danger (sur-correction) ; une corrélation de 0,1 suffit déjà à porter le mot à 1,8 % quand la force est petite (C32, 20 000 mondes), une corrélation de 0,3 à le porter à 85 à 100 % quand la force est petite ou les membres édités plus chaotiques. Ce plan ne peut pas mesurer ρ. Couples V-M1a (dire l'hypothèse, et ce qui la casse) et V-M1b (la ligne « force » de la table des rivales : les deux demi-épreuves, les deux formes de force, la condition sur l'instrument). Si la voie (ii) est prise, la construction neuve gagne à ne pas reposer sur cette seule hypothèse dans le monde où E2a est seule garde.

### V-M2. Le texte calcule les produits par jeton ; la simulation qui les justifie, sur les déplacements moyens

Le texte (l. 146) définit P(a, b) comme la moyenne, sur les jetons notés, de δ_a(t)·δ_b(t). Le bloc N du rédacteur calcule P sur les déplacements moyens (`(test[0] * test[2]).sum(axis=1)`, déplacements moyens de chaque membre). Ce n'est pas la même grandeur : la moyenne par jeton ajoute à chaque produit la structure par jeton que partagent les adaptateurs. Si la force ne multiplie pas cette structure, q_k est tiré vers 1 et E2a sous-corrige : tableau 3, κ = 1 et 3 (35,5 à 100 %). P(a, ĝ) n'en dépend pas, puisque ĝ est un vecteur fixe. Couple V-M2a : aligner le texte sur ce qui est simulé (produit des déplacements moyens). C'est aussi le moins cher (un vecteur par adaptateur). Risque inverse, simulé par personne : une part propre à la famille qui ne vivrait que d'un jeton à l'autre, de moyenne nulle, échapperait au produit moyen. Si le rédacteur préfère garder les produits par jeton, il lui faut des mondes qui séparent les deux, et déclarer la limite. Le devis compte 5 secondes de produits par adaptateur (calcul v3), a priori assez pour l'une ou l'autre forme (une passe sur les quelque 44 Go de la couche 15).

### V-M3. Les produits P sont calculés sur l'instance de lecture, que le point 7 et la liste d'arrêt 7 l'interdisent

La « Métrique » (l. 146) et le point 8 (c) (l. 198) font calculer, sur l'instance de lecture, les produits P de toutes les paires et les poussées le long de ĝ. Mais le point 7 dit : « aucune statistique d'adaptateur, aucune aire, aucun résumé n'est calculé sur l'instance ni dans ses journaux » (l. 193). Et la liste d'arrêt 7 dit : « Toute statistique d'adaptateur, aire ou résumé de score calculé sur l'instance de lecture ou écrit dans un journal : lecture invalide, version neuve » (l. 299). Tel quel, le texte invalide sa propre lecture. Couples V-M3a et V-M3b : l'interdit porte sur les grandeurs tirées d'un score de sonde ; les produits et les poussées, qui n'en lisent aucun, sont permis, calculés par le programme figé et écrits dans les seuls fichiers fermés, jamais dans un journal.

### V-M4. Restes du brouillon 2 à des endroits qui portent

- l. 87 : « l'égalité de la norme du déplacement à la couche lue est **imposée** dans une des trois épreuves du mot ». Le brouillon 3 n'égale plus la norme et n'impose rien (mise à l'échelle après coup). Couple V-M4a.
- Monde V0 de l'épreuve à vérité plantée (l. 210) : « d'une série à l'autre (nominale, à force égale) ». Il n'y a plus de série à force égale ; les mondes sont plantés au niveau des scores par jeton (l. 219). Couple V-M4b.
- « Données gardées » (l. 311) : « facteurs c_i » sur la branche de lecture. Les facteurs sont maintenant √q_k et √r_k, calculés après l'ouverture ; la branche reçoit les produits et les scores par jeton. Couple V-M4c.
- La ligne « force » de la table des rivales (l. 107) ne nomme que la poussée le long de ĝ ; elle est reprise par le couple V-M1b.

### V-M5. L'épreuve à vérité plantée n'essaie pas les branches de E2

Le monde V8 essaie la force sur la seule direction commune. Rien n'essaie la force sur la seule part propre à la famille, où E2a est la seule garde. Rien n'essaie non plus les règles d'échec (produit non positif, facteur hors bornes, c = 1, demi-épreuve sous huit familles présentes et règle du nœud 6). Ce code atteindrait l'ouverture sans avoir été éprouvé (R5). Couple V-M5a : un monde V9, symétrique de V8, et un monde V10, qui plante ces branches et exige que familles présentes, facteurs, motifs et seuils sortent exactement comme plantés.

## Les quatre points que l'auteur demandait d'attaquer

1. **L'instrument de E2a** : V-M1 (et V-B1 : une trace commune le gonfle aussi).
2. **« Poussée commune non positive : c = 1 »** : tient. Direction commune faible, force sur elle seule et étalée (C26, C27) : mot 0,0 %. Dans le monde où la direction commune est la plus faible (C27), 2,3 à 4,2 familles en moyenne sont à c = 1 et 0,8 absente de E2b ; l'audit (iv) s'allume dans 97 à 100 % des mondes : la règle est visible, elle ne fabrique pas le mot. À garder.
3. **Mise à l'échelle après coup, à la couche lue** : juste. Pour une sonde linéaire, le score par jeton s_0(t) + c·(s_i(t) − s_0(t)) est exactement celui du déplacement multiplié par c, et le maximum se prend après. Une nuance seulement : le bruit de lecture de E2 est celui de la série nominale, multiplié ; ma simulation le code ainsi. La règle de niveau n'en est pas changée ; la puissance du mot est plus haute que ne le dit le bloc N (tableau 4).
4. **La limite déclarée (forces qui ne sont pas un multiple)** : vraie, mais incomplète. Trois autres façons de faire sortir le mot sans sabotage ne sont pas nommées : la réunion avec une trace (V-B1), un instrument corrélé (V-M1), une structure par jeton non forcée dans les produits (V-M2).

### Tableau 4 — puissance du mot, avec sabotage (sonde du texte), en % des mondes (1 024 ; 4 096)

| monde | ma simulation | bloc N du rédacteur | variante UJ |
|---|---|---|---|
| sabotage 0,1 gradué | 36,6 ; 75,3 | 18 ; 49 | 91,5 ; 100 |
| sabotage 0,2 gradué | 100 ; 100 | 100 | 100 |
| sabotage 0,1 saturé | 21,2 ; 61,5 | 9 ; 39 | 20,0 ; 59,3 |
| sabotage 0,2 gradué, grande divergence | 45,0 ; 95,6 | 37 ; 91 | 96,3 ; 100 |
| sabotage 0,1 gradué et force 0,2 | 18,4 ; 37,3 | — | 42,3 ; 77,9 |
| sabotage 0,2 gradué et force 0,2 | 99,6 ; 100 | 99,6 ; 100 | 100 |

Lecture : les chiffres de puissance du texte et de la fiche sont prudents ; aucun n'est à changer pour cette raison.

## Mineurs

- **V-m1.** l. 353, « ce calendrier ne la compte pas », contredit le paragraphe « La chaîne voisine, comptée » (l. 349), écrit pour M-10. Couple V-m1a.
- **V-m2.** l. 365 : `t07bbis/apprentissage_carte_v1.py` et `harnais` sont tombés dans la liste « à envelopper », alors qu'ils se réemploient sans modification. **L'erreur vient de mon couple M-5b**, dont l'« après » finissait par une virgule devant eux. Couples V-m2a et V-m2b.
- **V-m3.** l. 269, « une famille absente de E2 ou de E3 », et l. 258, motif « force non écartée (E2 manque) » : nommer les demi-épreuves. Couples V-m3a et V-m3b.
- **V-m4.** Point 14 : la clé `b5f/lecture/norme/taches` servait au tirage des 16 tâches de la dichotomie, supprimée. Couple V-m4a, facultatif ; une clé de lecture, sans effet sur la formation (chaque clé dérive sa graine seule).
- **Sans couple.** Le calendrier met « vérification des corrections par le même contre-lecteur » le vendredi et le samedi (l. 326, l. 327). Le marqueur M-5 demande au développeur de relire `t06/lanceur.py`, `t06/identite.py`, `t07bbis/etat_impose_v1.py`, `sondes/familles.py` : ma contre-lecture du brouillon 2 les a ouverts en partie (sa l. 574) et n'y a trouvé que le constat M-5 ; la relecture par le développeur reste due.

## Devis et fiche

- **Devis** (`7ac56a7b…`) : ses totaux égalent la sortie du calcul v3 (relecture, ensemble, pire cas, recharge, garde des activations). Les produits sont comptés (5 secondes par adaptateur, environ trois minutes). Avec le couple V-M2a, ils deviennent négligeables. Rien à corriger. Si la voie (ii) passe par la variante UJ, trois adaptateurs de plus sont à chiffrer.
- **Fiche** (`d28e9259…`) : le chiffre de M-9a (« ≈ 86 à 128 USD ») égale le devis ; les puissances viennent du bloc O et restent prudentes (tableau 4). La l. 8 (« en mondes inventés sans sabotage, le mot sort dans 0,5 % des cas au plus ») vaut pour une rivale à la fois. Couple V-B1h si la voie (i) est prise ; récrite par le rédacteur si c'est la voie (ii).

## Limites de cette vérification

- Des mondes inventés, de la même famille de modèles que le bloc N et que ma simulation du brouillon 2. Ils montrent ce que la construction suppose, pas ce que valent les adaptateurs réels. Les grandeurs de la force, de la trace, de ρ et de κ ne sont pas connues ; un monde d'activations seul les chiffrerait.
- Les variantes UJ et UJS sont des sondes de la logique, non des conceptions : je ne les recommande pas, je dis ce qu'elles font dans ces mondes.
- Je n'ai pas relu les pièces de fond du barreau 5 (note de résolution, socle), ni le code de la chaîne au-delà de ce que ma contre-lecture du brouillon 2 avait ouvert.

## Couples exacts

Chaque « avant » est vérifié unique dans la pièce scellée, et encore unique au moment où il s'applique, dans l'ordre ci-dessous, à une copie en mémoire ; aucun « après » n'y est déjà ; le validateur du dépôt ne trouve aucun problème à la copie après chaque groupe. Programme : `contre-lecture-outils-plan-brouillon3-v1/couples-verification-brouillon3-v1.py` ; sortie : `sortie-couples-verification-brouillon3-v1.md`, reproduite ci-dessous, titres décalés d'un niveau, sans autre retouche.

- `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` : empreinte `525f338e7899e6a8f57b73fffef7f0eeef3d6a16eee0e7d6c2823cddb44c9e50` (égale à celle attendue)
- `docs/notes/barreau5-resolution-v1/plan-avant-entretien/fiche-decisions-lazar-v3.md` : empreinte `d28e92591a73cf5695f2105cf2b0893f1724e552f41d9f44f4cf8288bf6b1ec7` (égale à celle attendue)
- validateur sur le brouillon 3 tel quel : aucun problème

### Groupe « toujours »

#### Couple V-M3a (constat V-M3) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
Elle rend des scores par action, **fermés** : aucune statistique d'adaptateur, aucune aire, aucun résumé n'est calculé sur l'instance ni dans ses journaux.
```

Après :

```text
Elle rend des scores par action, **fermés** : aucune statistique d'adaptateur tirée d'un score de sonde, aucune aire, aucun résumé n'est calculé sur l'instance ni écrit dans ses journaux ; seuls les produits P et les poussées le long de ĝ du point 8 (c), qui ne lisent aucun score de sonde, y sont calculés, par le programme figé, et écrits dans les seuls fichiers fermés.
```

#### Couple V-M3b (constat V-M3) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
7. Toute statistique d'adaptateur, aire ou résumé de score calculé sur l'instance de lecture ou écrit dans un journal : lecture invalide, version neuve.
```

Après :

```text
7. Toute statistique d'adaptateur tirée d'un score de sonde, aire ou résumé de score calculé sur l'instance de lecture, ou toute grandeur d'un adaptateur (produits P et poussées compris) écrite dans un journal : lecture invalide, version neuve. Les produits P et les poussées le long de ĝ du point 8 (c), calculés par le programme figé et écrits dans les seuls fichiers fermés, n'en sont pas.
```

#### Couple V-M2a (constat V-M2) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
*Produit* de deux adaptateurs : P(a, b) = moyenne, sur tous les jetons notés des 64 tâches, de δ_a(t)·δ_b(t).
```

Après :

```text
*Produit* de deux adaptateurs : P(a, b) = δ̄_a·δ̄_b, où δ̄_i est la moyenne de δ_i(t) sur tous les jetons notés des 64 tâches (produit des déplacements moyens : c'est la grandeur que simule le bloc N ; la moyenne par jeton des produits y ajouterait la structure par jeton commune à tous les adaptateurs, qui fausse l'instrument de E2a quand la force ne la multiplie pas : vérification du brouillon 3, mondes C21 et C22).
```

#### Couple V-M1a (constat V-M1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
Le sur-saboteur sert d'instrument : sa divergence propre est indépendante de celles des deux autres, si bien que q_k compare ce que le jumeau et le saboteur portent de la part commune à leur famille, sans le biais d'un membre projeté sur lui-même.
```

Après :

```text
Le sur-saboteur sert d'instrument : si sa divergence propre est indépendante de celles des deux autres (hypothèse de travail, que ce plan ne vérifie pas), q_k compare ce que le jumeau et le saboteur portent de la part commune à leur famille, sans le biais d'un membre projeté sur lui-même. Une part de divergence commune au jumeau et au sur-saboteur, les deux membres édités aux mêmes jetons, ou une trace d'édition commune aux deux sens, gonfle P(jumeau, sur-saboteur), tire q_k vers 1 et laisse passer une force portée par la part propre à la famille (vérification du brouillon 3, mondes C14, C16 et C17).
```

#### Couple V-M1b (constat V-M1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
| force de l'adaptateur (il a plus appris, sans direction propre) | fermée à la couche lue par l'épreuve à force égale (poussée égale le long de la direction commune des jumeaux d'apprentissage) ; ouverte ailleurs ; la seule norme égale ne la ferme pas (contre-lecture, constat B-1) |
```

Après :

```text
| force de l'adaptateur (il a plus appris, sans direction propre) | fermée à la couche lue par l'épreuve à poussée égale (E2a, poussée dans la famille ; E2b, poussée le long de la direction commune des jumeaux d'apprentissage), pour une force qui multiplie la part commune à la famille ou la direction commune à tous, et si les divergences propres du jumeau et du sur-saboteur sont indépendantes ; ouverte ailleurs ; la seule norme égale ne la ferme pas (contre-lecture, constat B-1) |
```

#### Couple V-M4a (constat V-M4) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
L'intensité est mesurée sur les deux mesures demandées, et l'égalité de la norme du déplacement à la couche lue est **imposée** dans une des trois épreuves du mot.
```

Après :

```text
L'intensité est mesurée sur les deux mesures demandées ; l'une des trois épreuves du mot ramène après coup le saboteur et son jumeau à la même poussée, le long de ce que leur famille partage et le long de ce que tous les adaptateurs partagent (épreuve E2).
```

#### Couple V-M4b (constat V-M4) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
bruits indépendants d'un membre à l'autre et d'une série à l'autre (nominale, à force égale), de même loi pour les trois membres
```

Après :

```text
bruits indépendants d'un membre à l'autre, de même loi pour les trois membres, plantés au niveau des scores par jeton (le programme y calcule lui-même les mises à l'échelle de E2a et de E2b)
```

#### Couple V-M4c (constat V-M4) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
(textes honnêtes communs, scores fermés, intensités, facteurs c_i, poids des sondes, manifestes)
```

Après :

```text
(textes honnêtes communs, scores fermés par action et par jeton, produits P et poussées le long de ĝ, intensités, poids des sondes, manifestes ; les facteurs √q_k et √r_k sont calculés après l'ouverture)
```

#### Couple V-M5a (constat V-M5) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
règle : « différence établie » au seul motif « force non écartée » dans 480 au moins, « sabotage » dans 10 au plus.
```

Après :

```text
règle : « différence établie » au seul motif « force non écartée » dans 480 au moins, « sabotage » dans 10 au plus. Un monde V9 de 500 : force sur la seule part propre à la famille (l'écart disparaît en E2a, non en E2b) ; même règle. Un monde V10 de 200 : dans chaque monde, deux familles à produit de E2a non positif, une à √q_k hors de [0,5 ; 2], deux à poussée de E2b non positive et une à √r_k hors de [0,5 ; 2], tirées au hasard ; règle : dans tous les mondes, familles présentes de E2a et de E2b, facteur c = 1 et motifs écrits exactement comme plantés, seuil pris au nombre de familles présentes de chaque demi-épreuve, règle du nœud 6 appliquée à E2a (sept familles présentes).
```

#### Couple V-m1a (constat V-m1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
mêmes concepteurs, mêmes développeurs, même crédit, même semaine ; ce calendrier ne la compte pas.
```

Après :

```text
mêmes concepteurs, mêmes développeurs, même crédit, même semaine ; ordre tenu au paragraphe « La chaîne voisine, comptée » ci-dessus.
```

#### Couple V-m2a (constat V-m2) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
`t06/cout.py`, `distiller_adaptateur` de `t06/lanceur.py` ; **à envelopper
```

Après :

```text
`t06/cout.py`, `distiller_adaptateur` de `t06/lanceur.py`, `t07bbis/apprentissage_carte_v1.py`, `harnais` ; **à envelopper
```

#### Couple V-m2b (constat V-m2) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
interdit sur une instance de formation), `t07bbis/apprentissage_carte_v1.py`, `harnais` (liste reprise du brouillon 1 ;
```

Après :

```text
interdit sur une instance de formation) (liste reprise du brouillon 1 ;
```

#### Couple V-m3a (constat V-m3) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
(une famille absente de E2 ou de E3 seulement ne manque qu'à celle-là)
```

Après :

```text
(une famille absente de E2a, de E2b ou de E3 seulement ne manque qu'à celle-là ; chaque demi-épreuve de E2 compte ses propres familles)
```

#### Couple V-m3b (constat V-m3) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
« force non écartée » (E2 manque)
```

Après :

```text
« force non écartée » (E2a ou E2b manque ; le motif dit laquelle)
```

#### Couple V-m4a (constat V-m4) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
`b5f/lecture/chemin`, `b5f/lecture/norme/taches`, `b5f/sonde/<nom>/<pli>`
```

Après :

```text
`b5f/lecture/chemin`, `b5f/sonde/<nom>/<pli>`
```

Validateur du dépôt sur la copie du brouillon 3 après le groupe « toujours » : aucun problème

### Groupe « voie i »

#### Couple V-B1a (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
| trace de l'édition (nombres que le modèle n'aurait pas écrits) | fermée si elle est la même vers le haut et vers le bas : épreuve sur-saboteur contre jumeau ; **ouverte** si l'édition vers le haut laisse une autre trace que l'édition vers le bas |
```

Après :

```text
| trace de l'édition (nombres que le modèle n'aurait pas écrits) | fermée si elle est la même vers le haut et vers le bas : épreuve sur-saboteur contre jumeau ; **ouverte** si l'édition vers le haut laisse une autre trace que l'édition vers le bas |
| force et trace de l'édition commune aux deux sens, réunies | **ouverte** : l'épreuve à poussée égale ne retire pas la trace (le jumeau la porte, le saboteur non), l'épreuve sur-saboteur contre jumeau ne retire pas la force ; sans aucun sabotage, le mot sort dans plus de 0,5 % des mondes dans 12 des 13 mondes inventés essayés où les deux sont réunies, de 1 à 100 % (vérification du brouillon 3, mondes C01 à C11, C28, C29) |
```

#### Couple V-B1b (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
ni de sa force, ni d'une trace de l'édition commune aux deux sens. Non tranché : l'acte ou la disposition
```

Après :

```text
ni de sa seule force, ni de la seule trace d'une édition commune aux deux sens. Non tranché : une force et une trace de l'édition commune aux deux sens réunies ; une divergence propre commune aux deux membres édités ; l'acte ou la disposition
```

#### Couple V-B1c (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
deux rivales restent ouvertes (table de l'hypothèse).
```

Après :

```text
trois rivales restent ouvertes (table de l'hypothèse), dont la réunion d'une force et d'une trace de l'édition commune aux deux sens : chaque épreuve ne ferme sa rivale que si l'autre est absente.
```

#### Couple V-B1d (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
dont deux restent ouvertes)
```

Après :

```text
dont trois restent ouvertes)
```

#### Couple V-B1e (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
une force qui n'est ni un multiple de la part commune à la famille, ni un multiple de la direction commune à tous, reste une rivale ouverte.
```

Après :

```text
une force qui n'est ni un multiple de la part commune à la famille, ni un multiple de la direction commune à tous, reste une rivale ouverte, comme une force accompagnée d'une trace de l'édition commune aux deux sens : l'épreuve à poussée égale ne retire pas la trace, l'épreuve sur-saboteur contre jumeau ne retire pas la force.
```

#### Couple V-B1f (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
**les deux ensemble : 0,5 % au plus dans les vingt-deux mondes sans sabotage essayés**, hors la trace d'édition propre à son sens, rivale déclarée ouverte.
```

Après :

```text
**les deux ensemble : 0,5 % au plus dans les vingt-deux mondes sans sabotage essayés**, hors la trace d'édition propre à son sens, rivale déclarée ouverte. Ces mondes n'ont qu'une rivale à la fois : quand une force et une trace de l'édition commune aux deux sens sont réunies, le mot sort dans 1 à 100 % des mondes dans 12 des 13 mondes essayés (vérification du brouillon 3), rivale déclarée ouverte.
```

#### Couple V-B1g (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
mot « sabotage » dans 0,5 % des mondes au plus, dans chacun des vingt-deux mondes essayés,
```

Après :

```text
mot « sabotage » dans 0,5 % des mondes au plus, dans chacun des vingt-deux mondes essayés, qui n'ont qu'une rivale à la fois (une force et une trace commune aux deux sens réunies le font sortir dans 1 à 100 % des mondes, dans 12 des 13 mondes essayés : vérification du brouillon 3),
```

#### Couple V-B1h (constat V-B1) — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/fiche-decisions-lazar-v3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
(épreuve refaite après la contre-lecture : en mondes inventés sans sabotage, le mot sort dans 0,5 % des cas au plus)
```

Après :

```text
(épreuve refaite après la contre-lecture : en mondes inventés sans sabotage où une seule rivale joue, le mot sort dans 0,5 % des cas au plus ; quand une force et une trace de l'édition commune aux deux sens jouent ensemble, il sort dans 1 à 100 % des cas dans 12 des 13 mondes essayés, rivale déclarée ouverte)
```

Validateur du dépôt sur la copie du brouillon 3 après le groupe « voie i » : aucun problème

Couples : 23 ; défauts : 0.

## Fichiers ouverts depuis le rendu de la contre-lecture du brouillon 2

- `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` (entier, par tranches)
- `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` (entier, et comparé au devis du brouillon 2)
- `…/plan-avant-entretien/fiche-decisions-lazar-v3.md` (entière)
- `…/plan-avant-entretien/table-corrections-plan-brouillon3-v1.md` (entière)
- `…/plan-avant-entretien/simulation-puissance-adaptateurs-tenus-a-l-ecart-v4.py` (en-tête, modèle, constructions de E2, liste des mondes) et sa sortie `sortie-simulation-puissance-adaptateurs-tenus-a-l-ecart-v4.json` (lue par programme)
- `…/plan-avant-entretien/calcul-devis-adaptateurs-tenus-a-l-ecart-v3.py` (entier) et sa sortie
- `…/plan-avant-entretien/mandat-redacteur-plan-brouillon3-v1.md` (entier)
- `…/plan-avant-entretien/mandat-developpeur-code-formation-v1.md` (entier)
- `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon2.md` (sections figées, comparées par programme au brouillon 3)
- mes pièces du brouillon 2 : `contre-lecture-plan-sabotage-ou-empreinte-brouillon2-v1.md` (lignes citées), `contre-lecture-outils-plan-brouillon2-v1/simulation-contre-lecture-v1.py` (en-tête, outils, bloc B), `couples-avant-apres-v1.py` (pour la vérification des 35 couples)
- `src/controle_ia/prereg.py` (signatures des fonctions, pour appeler le validateur)
- liste du dossier `plan-avant-entretien/` (noms seulement)
