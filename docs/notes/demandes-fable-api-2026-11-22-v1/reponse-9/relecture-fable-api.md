# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHS7u3Yab9ZQSfeTfsL9`
- Heure (UTC) : 2026-11-22T05:47:18Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-9-these-apres-lecture-steganographie-v1.md` — sha256 dba7dbdd9f22091e12e6069ae58539078872b9410574d7069cccf52369f2cca9 (compagnon : vérifié)
  - remarques : `docs/notes/lecture-steganographie-comptabilite-v1.md` — sha256 6d52ba5d033d5a71237337a6c27f6f257d80c8ecbfb7a32dbae30cc569ce8ac6 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-4/relecture-fable-api.md` — sha256 cf55c7e073a1b99d2229bd08a96eb29e63878477379311b49227c5c5b6950344 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-8/relecture-fable-api.md` — sha256 d81a74d3c62220488d873a5d102dafc126b6d7f985777ec55723e9dc4fd6e9b5 (compagnon : vérifié)
  - remarques : `docs/programme-controle-ia-v2.md` — sha256 2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c (compagnon : vérifié)
- Empreinte de l'invite envoyée : 133082e3a1de5099f80ad3e63920f290b98ff83209e446f8f4671efdfd9729fc
- Jetons : entrée 38972, sortie 23765 (dont réflexion 13980), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.262376 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 9 — la thèse après lecture sur PDF de la stéganographie : réponse approfondie

**Conclusion d'abord.** La recommandation des réponses 4 et 8 survit comme cadre, non comme thèse. La loi est occupée et, bien écrite, élémentaire : citée, elle devient le modèle nul du papier A. Ce qui peut rester propre est une mesure, celle des termes que le modèle binaire indépendant ne contient pas : dépendance des pas, hétérogénéité des tâches, choix de la référence, constante par moniteur, complémentarité. Le théorème négatif n'est pas la meilleure candidate : tel qu'il est écrit, il me paraît inexact pour la somme et le maximum ; corrigé, il est trivial ou occupé. Sa question empirique (le sabotage réel déplace-t-il la marginale ou la dépendance ?) est en revanche la meilleure ouverture du papier B. Ma confiance d'ensemble baisse de 0,6 à 0,55.

**Réserves.**
- Je n'ai lu aucun PDF. La note de lecture est mon seul accès aux pages : ses verdicts sont des faits rapportés.
- Les antériorités que j'ajoute sont citées de mémoire : « rapporté, non vérifié sur PDF ».
- Je ne confirme aucun identifiant arXiv de 2026.
- Je ne connais pas le texte de N-076, donc pas l'unité dans laquelle m y est compté.
- Je n'ai pas recalculé les empreintes.
- « Sans nom de personne » : je ne nomme que les auteurs des travaux cités.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Vérifier l'énoncé du théorème négatif avant d'en chercher l'antériorité** [PROPOSITION]. La loi d'une somme ou d'un maximum dépend de la loi jointe, non des seules marginales (voir question 2).
- **Récrire la loi héritée dans les unités du programme** [PROPOSITION]. Chez Ker 2010, m et n comptent les mêmes objets [FAIT RAPPORTÉ, note, p. 7]. Si le programme compte m en exécutions honnêtes et n en actions, le corollaire 1 ne se transpose pas tel quel.
- **Dresser la table de transport, hypothèse par hypothèse** [PROPOSITION] : objets indépendants contre pas dépendants, loi binaire contre score continu, charge contre dommage jugé, source unique contre tâches hétérogènes.
- **Tester par simulation la forme séquentielle du lemme** [PROPOSITION]. Je la crois fausse comme invariance (question 1).
- **Corriger ses propres réponses** [PROPOSITION]. Les réponses 4 et 8 contiennent des phrases que la lecture réfute (question 4).

## 2. Données brutes de départ

- Les pages elles-mêmes : Ker 2010, p. 7, 11, 13 à 15 ; Avenhaus et Jaech, p. 25, 30 et 31. La note n'y suffit pas.
- Les scores de sonde et de juge de texte pas à pas, sur des exécutions honnêtes jumelles, avec l'identifiant de tâche, le rang du pas et le nombre de jumelles par tâche.
- Les mêmes scores pour plusieurs moniteurs sur les mêmes actions (table appariée de la réponse 8).
- Le texte de N-076, pour l'unité de m.
- Les PDF d'une seconde série de lectures (décision 3).

## 3. Méthodes et outils

- **Modèle à composantes de variance** (tâche, exécution, pas) sur les scores honnêtes ; rééchantillonnage par tâche.
- **Grille à deux entrées** : sous-échantillonner la référence (m) et l'horizon (n), puis ajuster la surface du seuil d'alarme honnête à la forme nulle héritée.
- **Variance d'Allan et estimateur de mémoire longue**, pour séparer la dépendance courte (elle change la constante) de la dérive (elle change l'exposant).
- **Données de substitution par permutation des pas dans une trajectoire** [PROPOSITION]. La permutation garde les marginales et détruit la dépendance sérielle : c'est le nul naturel de la question marginale contre corrélation (Theiler et collaborateurs, 1992, « Testing for nonlinearity in time series: the method of surrogate data » ; rapporté, non vérifié sur PDF).
- **Simulation du lemme séquentiel** : même budget total, sabotage concentré tôt, tard, ou étalé.
- **Tableau de revendications** contre les pages, tenu par un lecteur autre que l'auteur de la note.

## 4. Ce qui vérifie hors du directeur et de Claude

- Un spécialiste de stéganalyse, sur deux questions : « notre transport de votre théorème est-il juste ? » et « la mesure sur agents existe-t-elle déjà ? »
- Un statisticien des garanties nucléaires, pour la littérature séquentielle des bilans, non cherchée.
- Un statisticien de la détection de dépendances, pour l'énoncé corrigé du théorème négatif.
- Un second lecteur des pages décisives.
- L'essai « jumeau contre jumeau » et les données de substitution, dont l'issue ne dépend d'aucun avis.
- La prévision scellée, puis une seconde famille de modèles.

## Demande reformulée

« Après lecture, sépare dans le papier A ce qui est cité (énoncé, auteurs, page), ce qui est un modèle nul à mesurer, et ce qui est une question propre. Écris la loi dans les unités du programme, avec ses hypothèses de transport. Vérifie l'énoncé du théorème négatif avant d'en chercher l'antériorité. Classe les thèses candidates par ce qu'une issue négative laisserait. Donne la liste des phrases à retirer, y compris dans tes réponses précédentes. »

---

## (1) Ce qu'il reste, et la question réécrite

### La forme exacte de la loi

- [FAIT RAPPORTÉ, note, Ker 2010, théorème 2 et corollaires] Avec n objets surveillés et m objets de référence, la charge cachée critique est d'ordre n·√(1/m + 1/n), soit √(n + n²/m). Elle vaut √n dès que m ≥ n, n/√m quand m est petit devant n, et n'est linéaire qu'à m borné ou si la référence est fautive et que l'auteur le sait.
- [HYPOTHÈSE, dérivation de ma main, à faire vérifier] C'est la variance d'une comparaison à deux échantillons : la somme de n scores a une variance n·σ², n fois une moyenne estimée sur m scores ajoute n²·σ²/m. La loi est donc élémentaire. Le reproche « évident » vise maintenant la loi entière.
- [HYPOTHÈSE] Conséquence pour l'unité : si la référence est faite de r exécutions jumelles de même longueur que l'exécution surveillée, alors m = r·n ≥ n. On reste dans le régime en racine, avec un facteur √(1 + 1/r), et le terme n/√m n'apparaît jamais par simple bruit d'échantillonnage. Il n'apparaît que si une référence courte est extrapolée à un horizon plus long, ce qui suppose des pas stationnaires.
- [HYPOTHÈSE] Dans ce modèle, la constante du moniteur (σ divisé par le déplacement δ par acte) multiplie les deux régimes de la même façon. La sonde ne peut pas déplacer la transition n ≈ m ; le facteur k doit être le même des deux côtés. C'est une prévision réfutable.

### Ce qui est hérité et se cite

| Élément | Source rapportée par la note | Statut dans le papier |
|---|---|---|
| Indifférence à la répartition, pour la somme seulement | Avenhaus et Jaech 1981, p. 25, 30 et 31 ; Ker 2006, p. 6, 7, 9 | Cité ; rappelé avec sa limite |
| Bruit honnête en racine | Ker 2007 ; Ker et collaborateurs 2008 ; Bash et collaborateurs 2013 | Cité |
| Référence estimée, régime n/√m | Ker 2010, p. 7 et 11 | Cité ; modèle nul |
| Règle « horizon au plus m » | Ker 2010, corollaire 1 | Cité ; N-076 en devient l'application |
| Référence fautive, loi linéaire | Ker 2010, p. 13 et 15 | Cité ; sans borne chiffrée |
| Unité du temps et de l'espace | Avenhaus et Jaech 1981, p. 25 | Cité |

### Ce qui serait propre : des questions, non des revendications

- **Mesure sur des agents** [HYPOTHÈSE]. La note ne trouve pas de scores de sondes sur activations réelles dans les six pièces. Ce n'est pas une recherche affirmative. Chance que la mesure reste inédite après recherche : 0,5.
- **Exposant du bruit honnête dépendant** [HYPOTHÈSE]. Ma prévision de la réponse 4 (« l'exposant dépasse un demi parce que les trajectoires sont dépendantes ») était mal fondée. Une dépendance à mémoire courte garde l'exposant un demi et gonfle la constante. La loi en racine est rapportée pour des couvertures markoviennes (Filler, Ker, Fridrich, 2009, « The square root law of steganographic capacity for Markov covers » ; rapporté, non vérifié sur PDF). Seules une mémoire longue ou une dérive le long de la tâche changent l'exposant. La question propre devient : les trajectoires d'agents dérivent-elles ?
- **Référence par régime contre par tâche** [HYPOTHÈSE]. Le modèle hérité n'a pas de tâches. Une référence par régime ajoute un terme n·τ, où τ est l'écart-type entre tâches du score honnête moyen : il est linéaire et ne décroît pas avec m. Une référence par tâche l'annule mais coûte r jumelles par tâche et n'existe pas pour une tâche nouvelle en déploiement. Laquelle défend le plus long horizon à coût égal ? Voisin à lire : Meng 2018, déjà cité.
- **Forme séquentielle** [HYPOTHÈSE]. Pour un processus e, la richesse finale ne dépend que de la somme, mais l'alarme est un franchissement à un instant quelconque. Un sabotage concentré tôt franchit plus souvent qu'un sabotage étalé de même total. L'invariance me paraît donc fausse en séquentiel ; l'énoncé juste serait une inégalité (l'étalement est le cas le moins favorable au défenseur). Voisins à lire, mémoire incertaine : Speed et Culpin, 1986, « The role of statistics in nuclear materials accounting: issues and problems » ; les travaux sur la comptabilité en temps quasi réel et le test de Page.
- **Constante par moniteur et complémentarité** [PROPOSITION]. Elles restent telles que la réponse 8 les pose, contrôle « seconde boîte noire » et résidu de sonde compris. C'est la seule part du papier qui parle de l'accès interne. Parent direct à lire : Parrack, Attubato, Heimersheim, 2025 (rapporté, non vérifié sur PDF).
- **Plancher d'audit et somme des trois termes** [HYPOTHÈSE]. « Non trouvé dans six pièces » est une question. Voisin probable : Avenhaus, von Stengel, Zamir, 2002, « Inspection games » (rapporté, non vérifié sur PDF). Des variances s'ajoutent sous la racine ; le « plus grand des trois termes » n'est qu'un encadrement à un facteur √3 près.

### La question du papier A, réécrite

[PROPOSITION]

> « La stéganographie et la comptabilité des matières donnent le dommage qu'un saboteur diffus peut cacher : de l'ordre de √(n + n²/m) pour des pas indépendants et une référence de m pas (Ker 2010 ; Avenhaus et Jaech 1981). Sur de vrais agents, quels termes de ce bilan tiennent, lesquels s'ajoutent (dérive le long de la tâche, hétérogénéité entre tâches), quelle référence (par régime ou par tâche) défend le plus long horizon, et que vaut la constante de chaque moniteur, seule puis jointe ? »

Forme nulle à ajuster [HYPOTHÈSE] : budget caché au carré ≈ z²·(σ²·n^(2H) + σ²·n²/m + τ²·n²), où H est l'exposant mesuré, τ nul avec une référence par tâche, et σ propre au moniteur.

Prévisions à sceller [HYPOTHÈSE ; chances en jugement] :
- H entre 0,5 et 0,6 une fois la dépendance courte retirée (0,55) ; au-delà, dérive.
- Avec une référence par régime, le terme τ domine avant n = m (0,6).
- Le rapport k entre sonde et juge de texte est le même des deux côtés de la transition (0,5).
- La capture résiduelle de la sonde dépasse celle d'une seconde boîte noire (0,4, repris de la réponse 8).

Le versant honnête décide les trois premières sans saboteur. Les deux issues restent publiables : si le nul tient, on a une règle de dimensionnement à constantes mesurées ; s'il ne tient pas, on sait quel terme les agents ajoutent.

---

## (2) Le théorème négatif : meilleure candidate ?

### L'énoncé est inexact dans sa lettre

[HYPOTHÈSE, contre-exemples élémentaires, à confirmer par simulation]

- La loi d'une somme dépend de la loi jointe. Avec n scores de marginale préservée et de corrélation commune ρ, la variance de la somme vaut n·σ²·(1 + (n − 1)·ρ). Un seuil sur la somme a alors une puissance supérieure à α si ρ > 0, inférieure si ρ < 0.
- La loi du maximum aussi : une corrélation positive réduit le nombre effectif de tirages, donc la puissance tombe sous α.
- Ce qui est exact : l'espérance de toute statistique additive Σ f(s) est inchangée. Il n'y a donc pas de dérive à accumuler, et la détectabilité est du second ordre. La statistique efficace est quadratique : autocovariance, carré de la somme, co-élévation.

« Puissance égale au taux de fausses alertes » n'est vrai que pour une statistique dont la loi ne dépend que d'une marginale, classe à peu près vide. L'énoncé honnête est une cécité au premier ordre.

### L'énoncé corrigé est occupé ou trivial

[FAIT RAPPORTÉ pour l'existence, HYPOTHÈSE pour la proximité ; tout est rapporté, non vérifié sur PDF]

- **Décomposition marginales et dépendance** : Sklar, 1959, « Fonctions de répartition à n dimensions et leurs marges ». La cécité des marginales à la copule est une définition.
- **Stéganalyse par dépendances** : Provos, 2001, « Defending against statistical steganalysis » (insertion qui préserve l'histogramme) ; Fridrich, Goljan, Hogea, 2002, « Attacking the OutGuess » (défaite par une statistique du second ordre) ; Pevný, Bas, Fridrich, 2010, « Steganalysis by subtractive pixel adjacency matrix » ; Fridrich, Kodovský, 2012, « Rich models for steganalysis of digital images ». C'est l'histoire même du théorème négatif et de sa parade.
- **Limites de détection d'une corrélation à marginales fixées** : Arias-Castro, Bubeck, Lugosi, 2012, « Detection of correlations » ; les mêmes, 2015, « Detecting positive correlations in a multivariate sample ». Ma mémoire est que les marginales y sont identiques sous les deux hypothèses et que le carré de la somme y est puissant en régime dense. Si c'est exact, c'est le parent direct de la co-élévation entre agents, et il contredit la lettre du théorème.
- **Tests d'indépendance et de corrélation sérielle** : Hoeffding, 1948, « A non-parametric test of independence » ; Ljung, Box, 1978, « On a measure of lack of fit in time series models » ; Székely, Rizzo, Bakirov, 2007, « Measuring and testing dependence by correlation of distances ».
- **Changement de corrélation** : Wied, Krämer, Dehling, 2012, « Testing for a change in correlation at an unknown point in time » (mémoire incertaine).
- **Agrégateur toujours valide** : Podkopaev, Blöbaum, Kasiviswanathan, Ramdas, 2023, « Sequential kernelized independence testing » ; Vovk, 2021, « Testing randomness online ». La méthode de l'agrégateur de corrélation existe.
- **Borne supérieure** : Cachin, 1998 ; Ker 2010, p. 1 [FAIT RAPPORTÉ, note] : préserver toutes les statistiques rend une charge linéaire indétectable. Préserver les seules marginales est le cas intermédiaire.
- arXiv 2606.10456, cité par le programme, reste à lire ; je ne le confirme pas.

### Verdict

- **Comme théorème** [PROPOSITION] : ni pour A ni pour B. Chance que l'énoncé corrigé soit neuf : 0,1.
- **Comme question empirique** [PROPOSITION] : oui, et c'est l'hypothèse pivot du programme. « Sur de vraies activations, le sabotage des organismes déplace-t-il la marginale des scores, leur dépendance, ou les deux ? » Elle se mesure par un test de position contre un test de dépendance, étalonnés sur les données de substitution. Chance qu'elle reste inédite : 0,5, sous réserve de 2606.10456.
- **Pour A** : une section de diagnostic, avec E1.4.
- **Pour B** : la meilleure ouverture [HYPOTHÈSE]. Des copies à poids partagés font de la co-élévation le signal naturel, et la frontière de détection héritée donne le nul : quelle taille d'essaim et quelle corrélation rendent la co-élévation détectable.
- **Limite** [FAIT RAPPORTÉ, réponse 8] : N-077 écarte toute revendication contre un saboteur qui choisirait de préserver ses marginales. On mesure ce que font les organismes, non ce qu'un attaquant optimal ferait.

---

## (3) Recommandation finale

[PROPOSITION]

| Candidate | Ce qu'une issue négative laisse | Chance d'un contenu propre | Rang |
|---|---|---|---|
| Loi héritée, citée en nul, bilan mesuré | Les constantes et le terme manquant | 0,5 | 1 |
| Complémentarité avec contrôle « seconde boîte noire » | « Une seconde boîte noire suffit » | 0,4 | 2, même papier |
| Question marginale ou dépendance | L'agrégateur à employer | 0,5 | 3 : section de A, tête de B |
| Théorème négatif tel qu'écrit | Rien | 0,1 | Retiré |

**Thèse recommandée pour A** : « Le bilan d'incertitude d'un moniteur d'accumulation chez des agents : la loi héritée comme nul, ses écarts mesurés, et la part propre à l'accès interne. » La complémentarité monte d'un rang par rapport à la réponse 8 : c'est désormais le seul élément du papier qui ne soit pas hérité dans sa forme.

**Ce qui a changé depuis les réponses 4 et 8.**
- La loi passe de « thèse » à « modèle nul cité ».
- La « bascule » n'est plus une prévision : à unités égales, elle est en n ≈ m par construction.
- Le terme d'hétérogénéité entre tâches devient l'inconnue principale.
- Le lemme, noté 0,75 en originalité par le programme, tombe pour son énoncé central ; sa forme séquentielle devient douteuse.

**Ce qui me ferait changer.**
- Une mesure sur agents déjà publiée : la complémentarité prend la tête.
- Un essai « jumeau contre jumeau » sans dérive ni hétérogénéité : le nul tient partout, et le papier se réduit à une note de dimensionnement plus la complémentarité.
- Des organismes dont le sabotage laisse la marginale intacte : la question de dépendance prend le titre de A.

Confiance d'ensemble : 0,55.

---

## (4) Les phrases à ne plus écrire

Aux deux phrases de la note s'ajoutent celles-ci [PROPOSITION] :

1. « La stéganographie prédit une croissance en racine si la référence est connue, puis linéaire si elle est estimée » (résumé de la réponse 4). Écrire : « en √(n + n²/m) ; linéaire seulement à référence bornée ou fautive ».
2. « Ces lois supposent une couverture ou une valeur comptable connue » (réponse 4). Faux : Ker 2010 traite la référence estimée.
3. « Personne ne l'a relevé » (réponse 4). C'était affirmer une zone vierge sans recherche.
4. « La bascule se situe entre m et m divisé par le taux d'audit » (réponse 4). Rien ne fonde la division par le taux d'audit.
5. « L'exposant dépasse un demi parce que les trajectoires sont dépendantes. » La dépendance courte change la constante.
6. « La loi de la référence, résultat mesuré du programme » et « la règle N-076 » sans citation. Écrire : « application du corollaire 1 de Ker 2010 ».
7. « Toute statistique de marginales (maximum, moyenne, somme cumulée) a une puissance égale au taux de fausses alertes. » Écrire : « l'espérance des statistiques additives est inchangée ».
8. « La puissance ne peut venir que d'une relation entre mâchoires » (réponse 8), tant que l'énoncé n'est pas corrigé.
9. « Le même objet mathématique dans le temps et entre agents » comme apport : Avenhaus et Jaech le disent en 1981.
10. « Trois planchers » et « borne par le plus grand des trois » comme résultat. « Non trouvé dans six pièces » ne vaut pas nouveauté.
11. « La puissance du processus e ne dépend pas de la répartition dans le temps », tant que la simulation séquentielle n'a pas tranché.
12. « La sonde change la constante, non l'exposant » comme constat. C'est une prévision.

---

## Décisions qui reviennent au directeur

**Décision 1 — Fixer la thèse du papier A après lecture.**
- *Enjeu.* Le titre, le résumé et la prévision scellée ; la thèse de la réponse 4 ne peut plus s'écrire telle quelle.
- *Option a : loi héritée citée comme nul, bilan mesuré, complémentarité en second axe.* Avantage : deux issues publiables, aucune nouveauté de théorème à défendre. Inconvénient : papier de mesure, exposé au reproche « évident ».
- *Option b : complémentarité en thèse.* Avantage : seule part propre à l'accès interne. Inconvénient : parent direct non lu ; chance de tenir 0,4.
- *Option c : théorème négatif et agrégateur de corrélation.* Avantage : continuité avec la version 2. Inconvénient : énoncé inexact, méthode occupée.
- *Recommandation.* Option a. Confiance : 0,55.

**Décision 2 — Fixer le statut du théorème négatif et du lemme.**
- *Enjeu.* La « colonne vertébrale théorique » de la version 2 et les notes d'originalité.
- *Option a : retirer les deux comme résultats ; citer le lemme ; récrire le théorème en cécité au premier ordre ; garder la question empirique, section de A et tête de B.* Avantage : rien à rétracter plus tard. Inconvénient : le programme perd ses théorèmes.
- *Option b : les garder en attendant un avis de statisticien.* Avantage : aucune réécriture immédiate. Inconvénient : une prévision scellée sur un énoncé peut-être faux.
- *Option c : chercher un théorème neuf en séquentiel (inégalité d'étalement).* Avantage : apport théorique possible. Inconvénient : littérature des bilans séquentiels non lue ; exige un coauteur.
- *Recommandation.* Option a, l'option c restant ouverte après lecture. Confiance : 0,7.

**Décision 3 — Lancer une seconde lecture sur PDF avant de sceller.**
- *Enjeu.* Les antériorités de cette réponse sont de mémoire ; quatre décident des énoncés.
- *Option a : lecture ciblée de quatre pièces (Filler, Ker, Fridrich 2009 ; Arias-Castro, Bubeck, Lugosi 2012 ; Parrack et collaborateurs 2025 ; arXiv 2606.10456), puis scellement.* Avantage : quelques jours, énoncés sûrs. Inconvénient : le reste demeure non vérifié.
- *Option b : lecture complète, bilans séquentiels et jeux d'inspection compris.* Avantage : cadrage complet. Inconvénient : délai sur les cinq semaines restantes.
- *Option c : sceller maintenant.* Avantage : aucun retard. Inconvénient : risque de sceller une phrase déjà réfutée, comme cela vient d'arriver.
- *Recommandation.* Option a, le reste avant la rédaction. Confiance : 0,7.

**Décision 4 — Fixer l'unité de m et le plan de référence de l'essai « jumeau contre jumeau ».**
- *Enjeu.* Sans unité commune à m et n, la règle N-076 ne correspond pas au corollaire cité ; le plan de référence commande le coût en exécutions honnêtes.
- *Option a : référence par tâche, r jumelles.* Avantage : pas de terme d'hétérogénéité. Inconvénient : coût multiplié ; indisponible pour une tâche nouvelle.
- *Option b : référence par régime, en pas.* Avantage : déployable. Inconvénient : terme linéaire en τ.
- *Option c : mesurer les deux sur les mêmes exécutions, comparaison scellée.* Avantage : la comparaison est elle-même le résultat propre. Inconvénient : analyse plus lourde.
- *Recommandation.* Option c. Confiance : 0,65.

**Décision 5 — Publier un erratum interne sur les réponses 4 et 8 et sur la section 3 du programme.**
- *Enjeu.* Douze phrases fautives circulent dans des pièces à empreinte.
- *Option a : note d'erratum maintenant, avec notes d'originalité révisées.* Avantage : les prochaines demandes partent d'un texte juste. Inconvénient : une pièce de plus.
- *Option b : attendre la version 3 du programme.* Avantage : un seul document. Inconvénient : les phrases restent citables d'ici là.
- *Recommandation.* Option a. Confiance : 0,8.

FIN DE LA RÉPONSE
