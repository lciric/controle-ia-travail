# Proposition B, tour III.1 : conception ciblée (à l'aveugle)

## Pièces absentes ou coupées

- **Pièce C** (rapport de méta-conception v6.3 `96d12112…` et relecture `9a791017…`) : absente. Les faits annoncent un « résumé dans la question », mais la question ne donne que les noms et les empreintes. Je n'utilise rien de leur contenu.
- **Code source v6.2.1** (`principal.py` et modules) : non joint. Seules la conception et les corrections sont lisibles.
- **Propositions A et C du collisionneur** : je ne les vois pas, le tour se joue à l'aveugle. Je ne peux donc ni les attaquer ni m'en servir. Dans ce texte, « faits A/B/C/D » désigne les pièces de faits, pas les cellules.
- **Numérotation de la conception** : un « § 3 » et un « § 4 » s'intercalent entre les § 2.10, 2.11 et 2.12. C'est un désordre de pièce, sans effet sur le fond, et je le signale seulement.

**Position, statut HYPOTHÈSE.** Les expériences de (b) doivent trancher la question suivante : ce qui manque au pôle est-il un *substrat d'exécution*, que la littérature fournit, ou un *critère de sélection valide*, qu'aucun des systèmes cités ne fournit d'après les faits B ? Je tiens la seconde lecture pour plus probable. Je la soumets à réfutation en E1 et E4.

---

## (a) Ce que la question suppose sans que ce soit établi

| n° | Supposition implicite | Statut | Ce qui la trancherait |
|---|---|---|---|
| a1 | L'organisme « peut tester ses hypothèses ». Or la note dit qu'il « n'exécute pas d'expériences arbitraires » et que sa réécriture se limite depuis C-17 à un gabarit de trois paramètres bornés. | RAPPORTÉ (note A, C-17) | Perfectionner signifie *ajouter* l'exécution, pas la régler. E4 |
| a2 | L'organisme « apprend de génération en génération ». La correction v1 constate « code jamais réécrit (successeur = copie et mémoire) ». Aucun score de pilote n'est servi, et l'effet de la mémoire ISVD n'est mesuré nulle part. | RAPPORTÉ (C-v1) ; l'apprentissage reste une HYPOTHÈSE | Ablation de la mémoire. E6 |
| a3 | Les castes contradictoires sont un atout de l'organisme. Sous la configuration du pilote 4, on a « une caste par tâche […] donc aucun arbitrage ». | RAPPORTÉ (C-v5) | L'atout n'a pas été exercé dans la configuration notée. E5 |
| a4 | Les mécanismes nommés (Koopman, Onsager, Shannon-Gram, mitose spectrale) apportent quelque chose au-delà de leur nom. | HYPOTHÈSE, aucune mesure dans les faits | Ablations E5 et E6 |
| a5 | Les prouesses du dossier de passation (882 agents, 241 castes, A/B « 0 % contre 94,4 % ») sont utilisables. | RAPPORTÉ comme **sans pièce** sur `origin/main` | Rien. Elles restent hors de toute comparaison |
| a6 | Le programme sait déjà éviter l'évaluation par construction. Contre-exemple interne : la métrique de Gemini « ne lit jamais la vérité », elle a été jugée non discriminante et écartée. | RAPPORTÉ (C-v1, C-v2) | Le risque de Goodhart s'est déjà réalisé une fois dans ce programme. E1, E2 |
| a7 | « Hypothèses fortes » et « prédictions justes » sont compatibles sans arbitrage. Une hypothèse plus risquée est plus souvent fausse, ce qui oblige à mesurer contenu et calibration ensemble. | HYPOTHÈSE (analyse) | Aptitude par pari, E1 |
| a8 | Une sélection par réfutation converge vers des hypothèses fortes. Une survie binaire peut récompenser celles qui ne prédisent rien. | HYPOTHÈSE | E1, contrôle « tautologies » |
| a9 | La bisociation rend plus fertile qu'un tirage stratifié. | HYPOTHÈSE, et la pièce C est absente | E3 |
| a10 | Les systèmes de la littérature apportent une évaluation solide. Les auteurs d'Agentic Scientist v3 rapportent eux-mêmes des « raccourcis qui violent la méthode », des grilles imparfaites, une dérive vers le réglage et une corrélation de 0,44 entre notes des relecteurs-agents et performance. | RAPPORTÉ (faits B) | Le « scellé » existe, sa résistance n'est pas établie. Instrument c4 |
| a11 | Le chiffre de Kosmos (79,4 % d'affirmations jugées exactes) mesure ce que nous voulons. Il porte sur l'exactitude d'énoncés, pas sur leur force ni sur la survie à des tests sévères. | RAPPORTÉ (chiffre) ; HYPOTHÈSE (sa non-transférabilité) | Il n'entre pas dans le duel des voies |
| a12 | Agentic Scientist v3 est compatible avec la règle des clés du noyau. Le README avertit que ses agents ont pleins droits dans Docker et héritent des clés fournies, alors que le noyau ne les expose jamais. | RAPPORTÉ (faits B, note A) | Incompatible en l'état ; il faudrait un relais de clés hors bac à sable. E4 |
| a13 | ShinkaEvolve et OpenEvolve « réécrivent leur propre code ». À ma connaissance, ces systèmes font évoluer un *programme cible* contre un évaluateur écrit par l'humain, et non le système lui-même. | HYPOTHÈSE, à vérifier sur les README `8adc053` et `66856ac` | Si c'est exact, leur évaluateur est un test figé par construction, ce qui est un atout pour la question 2 |
| a14 | Des résultats sur simulation ou semi-synthétique se transfèrent aux activations d'un modèle réel. | HYPOTHÈSE | Instrument c1, paires appariées sur modèle ouvert |
| a15 | Un juge par modèle est utilisable pour la fertilité ou la nouveauté. L'organisme refuse l'auto-notation par LLM-juge (§ 2.11), et le billet du point D rapporte des justifications sabotées qui trompent les juges. | RAPPORTÉ (conception) ; RAPPORTÉ, non opposable (D) | Toute métrique de (b) se calcule sans juge par modèle |
| a16 | Un chercheur seul peut maîtriser l'organisme. Il a fallu 17 corrections en cinq pièces, dont un interblocage (C-12) et une étiquette lue à la présence d'un mot (C-02). | RAPPORTÉ | C'est un coût de lisibilité, non chiffré ici |

---

## (b) Expériences décisives (inférence forte)

### Substrat commun : un « monde planté » scellé dans le noyau (HYPOTHÈSE de conception)

Le noyau tient caché un générateur de domaines qui imitent le programme de contrôle :

- **D1, sondes** : des vecteurs d'« activations » synthétiques, avec une direction plantée pour la propriété et un indice textuel corrélé de force réglable ;
- **D2, séquentiel** : des flux nuls (i.i.d., AR(1), dérive lente) et des alternatives à rupture plantée ;
- **D3, moniteurs** : des traces honnêtes et leurs jumelles qui ne diffèrent que par une modification plantée.

Chaque domaine porte une **table de vérité** cachée, faite de lois vraies et de lois fausses mais plausibles. Le pôle ne voit que l'interface d'expérience. Comme la vérité est connue, aucune métrique n'a besoin d'un juge. Ce substrat ne dit rien du transfert au réel (a14), qui est traité à part en (c).

### Aptitude proposée, à départager en E1 (HYPOTHÈSE)

Chaque hypothèse *h* doit émettre une loi prédictive p_h sur l'issue de chaque test. Le noyau fige *avant* l'expérience un modèle de référence p_0 (« l'effet nul »). L'aptitude est le logarithme d'une richesse de pari :

log W_h = Σ_t log p_h(x_t)/p_0(x_t)

Cette somme ne porte que sur des tests dont la configuration a été **engagée par empreinte avant l'exécution**.

- Une hypothèse qui ne prédit rien (p_h = p_0) garde W = 1, quoi qu'il arrive. Elle ne peut pas être promue.
- Une hypothèse forte et fausse s'appauvrit vite.
- Une hypothèse forte et vraie s'enrichit.

Les règles qui en découlent :

- **Promotion** si W_h ≥ 1/α (inégalité de Ville, valide sous arrêt et choix adaptatif des tests).
- **Élimination** par le pari inverse W'_h = Π p_rival/p_h ≥ 1/α. L'élimination à tort d'une hypothèse vraie est alors bornée par α.
- **Multiplicité** dans la population : e-BH.

Références : Shafer (2021), « Testing by betting: a strategy for statistical and scientific communication », *JRSS A* ; Ramdas, Grünwald, Vovk & Shafer (2023), « Game-theoretic statistics and safe anytime-valid inference », *Statistical Science* ; Wang & Ramdas (2022), « False discovery rate control with e-values », *JRSS B*.

---

### E1. Aptitude par pari contre survie binaire

- **H_A** : l'aptitude par pari réduit la part de survivants vides de contenu sans augmenter l'élimination à tort des lois vraies.
- **H_B** : la survie binaire à une batterie figée suffit. Les survivants vides n'apparaissent pas quand les tests sont figés d'avance.
- **Protocole** : même population initiale, même budget d'appels, deux sélecteurs. On injecte 20 % (illustratif) d'hypothèses *tautologiques* (p_h = p_0, ou une région prédite couvrant tout l'espace des issues) et 20 % de lois *fausses plausibles* tirées de la table.
- **Métrique** : contenu empirique moyen des survivants après K générations (part de l'espace des issues interdite par l'hypothèse), part de survivants vrais, et taux d'élimination à tort des lois vraies plantées.
- **Seuil** (illustratif) : H_A est retenue si la part de tautologies parmi les survivants est ≤ 2 % avec le pari contre ≥ 30 % en binaire, avec une élimination à tort ≤ α + 2 points.
- **Contrôle négatif** : un monde *sans loi* (vérité mélangée). Aucune hypothèse ne devrait être promue au-delà de α. Si l'un des deux sélecteurs en promeut davantage, il est cassé et son bras est invalide.
- **Ce qui falsifie H_A** : des tautologies survivent au même taux sous les deux sélecteurs, ou le pari élimine plus de lois vraies que le binaire au-delà du seuil.
- **Ce qui falsifie H_B** : le binaire laisse survivre les tautologies au-delà de 30 % (illustratif) pendant que le pari les retient.

### E2. Qui écrit le test

- **H_A** : un test écrit par l'agent qui défend l'hypothèse gonfle sa survie (effet Goodhart), même engagé par empreinte avant l'exécution.
- **H_B** : l'engagement préalable suffit. Le rédacteur du test (auteur, adversaire ou tirage scellé du noyau) ne change pas la survie des lois fausses plausibles.
- **Protocole** : trois bras.
  1. Tests de l'auteur.
  2. Tests d'un agent adverse, récompensé quand il fait monter W'_h.
  3. Tirage aléatoire dans un réservoir scellé par le noyau.
- **Métrique** : taux de promotion des lois *fausses* plantées, par bras.
- **Seuil** (illustratif) : le bras auteur dépasse le bras scellé de ≥ 10 points.
- **Contrôle négatif** : les lois fausses sont remplacées par des lois vraies. Le taux de promotion des trois bras doit alors être égal à ± 5 points près (illustratif). Un écart à ce stade révèle un défaut du réservoir, pas un effet de Goodhart.
- **Ce qui falsifie H_A** : écart auteur/scellé < 3 points.
- **Ce qui falsifie H_B** : écart ≥ 10 points.
- **Issue de conception** : si H_A tient, seul le bras scellé compte pour l'aptitude, et le bras adverse sert à explorer, pas à noter.

### E3. Recombinaison bisociative contre tirage stratifié

Forme minimale testée (HYPOTHÈSE ; la pièce C est absente, je ne prétends pas la suivre) :

- **tirage** de paires de survivants de domaines différents qui partagent un *opérateur* déclaré (par exemple « normalisation par variance glissante ») ;
- **filtre** de compatibilité : les contraintes des deux parents sont satisfiables ensemble, ce qui se vérifie mécaniquement sur la table d'interface du monde planté ;
- **fusion** en une hypothèse qui émet une loi prédictive propre.

Le duel :

- **H_A** : l'appariement par opérateur rend plus de descendants promus *et* plus riches en contenu que le tirage stratifié, à budget égal.
- **H_B** : le gain éventuel vient du seul filtre, ou de rien.
- **Protocole** : trois bras.
  1. Tirage stratifié par domaine, sans filtre.
  2. Tirage stratifié avec filtre.
  3. Appariement par opérateur avec filtre.

  Le monde contient des isomorphismes plantés (une même loi vraie dans D1 et D2).
- **Métrique de fertilité**, sans juge : part des descendants qui (i) sont promus sur les tests scellés, (ii) ont un contenu ≥ au maximum de leurs parents, (iii) ont une prédiction qu'aucun des deux parents n'implique seul. Ce dernier point se vérifie sur la table de vérité.
- **Seuil** (illustratif) : le bras 3 dépasse le bras 2 d'un facteur ≥ 1,5 sur la fertilité.
- **Contrôle négatif** : un monde *sans isomorphisme planté*. Le bras 3 ne doit pas y battre le bras 2. S'il le bat, il exploite autre chose (longueur, fuite par le filtre) et sa victoire dans le monde planté ne compte pas.
- **Ce qui falsifie H_A** : bras 3 ≤ bras 2 dans le monde planté, ou bras 3 > bras 2 dans le monde sans isomorphisme.
- **Ce qui falsifie H_B** : bras 3 ≥ 1,5 × bras 2 dans le monde planté, sans écart dans le monde témoin.

### E4. Expériences en langage borné ou en code libre (le duel des voies)

C'est le cœur de l'arbitrage, parce que C-17 a retiré le code brut *pour la sûreté* (RAPPORTÉ). Ouvrir l'exécution d'expériences arbitraires rouvre ce que C-17 a fermé.

- **H_A** : un langage d'expérience borné (paramètres et opérateurs en liste blanche, dans l'esprit du gabarit) suffit pour tester le programme.
- **H_B** : il faut du code libre, à la manière de ShinkaEvolve, OpenEvolve ou Agentic Scientist v3.
- **Protocole** :
  - avant toute course, figer une batterie de 30 hypothèses cibles du programme réel (sondes, garanties séquentielles, moniteurs) ;
  - mesurer la part testable en langage borné ;
  - dans le monde planté, comparer l'exactitude d'élimination (lois vraies gardées, fausses éliminées) des deux substrats sous la *même* aptitude E1. On croise substrat (organisme étendu / OpenEvolve dans le bac à sable du noyau) × aptitude (défaut / pari).
- **Métrique** : couverture de la batterie, exactitude d'élimination, et effet principal du substrat comparé à celui de l'aptitude.
- **Seuil** (illustratif) : couverture ≥ 80 % et écart d'exactitude ≤ 5 points entre les substrats.
- **Contrôle négatif** : une batterie de lois *non testables par construction* (elles portent sur des quantités que l'interface n'expose pas). Les deux substrats doivent les déclarer non testées. Un substrat qui les « teste » produit des résultats par construction.
- **Ce qui falsifie H_A** : couverture < 60 %, ou exactitude du code libre supérieure de plus de 10 points.
- **Ce qui falsifie H_B** : couverture ≥ 80 % sans perte d'exactitude, avec un effet de l'aptitude supérieur à celui du substrat. Cette issue réfute aussi ma propre hypothèse inverse : si le substrat l'emporte sur l'aptitude, mon avis tombe.

### E5. Castes contradictoires contre auto-cohérence, à budget égal

- **H_A** : la délibération contradictoire (analyse, croisement, critique, arbitre) améliore la calibration des prédictions d'issue de test.
- **H_B** : à nombre d'appels égal, des tirages répétés d'une seule caste agrégés par moyenne font aussi bien.
- **Protocole** : chaque bras prédit P(issue) pour 500 tests scellés (illustratif) du monde planté.
- **Métrique** : score de Brier (règle propre, comme la récompense de l'organisme, RAPPORTÉ § 2.3), décomposé en calibration et résolution.
- **Seuil** (illustratif) : différence de Brier ≥ 0,02 avec intervalle bootstrap excluant 0.
- **Contrôle négatif** : un prédicteur constant égal au taux de base. Les deux bras doivent le battre. Sinon la comparaison ne dit rien.
- **Ce qui falsifie H_A** : intervalle centré sur 0 ou en faveur de l'auto-cohérence.
- **Ce qui falsifie H_B** : gain ≥ 0,02 pour les castes.

### E6. La mémoire inter-générationnelle porte-t-elle de l'information ?

- **H_A** : la mémoire ISVD transmise améliore l'aptitude de la génération g+1.
- **H_B** : un successeur à mémoire vide, ou à mémoire mélangée (permutation des traces entre domaines), fait aussi bien.
- **Protocole** : trois bras sur 5 générations (illustratif) : mémoire réelle, vide, mélangée.
- **Métrique** : richesse log W cumulée des survivants à la génération 5.
- **Seuil** (illustratif) : la mémoire réelle dépasse la meilleure des deux témoins d'au moins 10 %.
- **Contrôle négatif** : c'est le bras mélangé lui-même. S'il égale la mémoire réelle, l'effet vient de la quantité de texte et non de son contenu.
- **Ce qui falsifie H_A** : réelle ≈ mélangée.
- **Ce qui falsifie H_B** : réelle > mélangée et vide au-delà du seuil.
- **Portée** : si H_B tient en E5 *et* en E6, « perfectionner l'organisme » revient à garder le noyau et la discipline de correction, pas ses mécanismes propres.

### E7. Résistance du scellé à une sous-déclaration (méthode seulement)

- **H_A** : un résultat ne compte que s'il est **ré-exécuté par le noyau** depuis le code engagé et sa graine. Cela détecte une sous-déclaration plantée sous un taux de fausses alertes fixé.
- **H_B** : un moniteur par modèle sur le rapport de l'agent fait aussi bien. Le billet D, RAPPORTÉ et non opposable, laisse prévoir le contraire à bas taux de faux positifs.
- **Protocole** : sous-déclaration *scriptée, non apprise* d'un effet connu du monde planté. Je ne donne aucune procédure au-delà de ce principe.
- **Métrique** : taux de détection à 1 % de fausses alertes (illustratif).
- **Contrôle négatif** : des rapports honnêtes avec variance de graine naturelle. La ré-exécution ne doit pas dépasser 1 % de fausses alertes.
- **Ce qui falsifie H_A** : détection < 80 % (illustratif).
- **Ce qui falsifie H_B** : le moniteur par modèle reste en dessous de la ré-exécution d'au moins 20 points à fausses alertes égales.

### Règle de décision fixée avant les résultats (HYPOTHÈSE)

- **E4 donne H_A et E1 donne H_A** : perfectionner. On ajoute à l'organisme un exécuteur en langage borné et le sélecteur par pari, dans le noyau.
- **E4 donne H_B** : voie hybride. OpenEvolve ou ShinkaEvolve sert de moteur de mutation dans le bac à sable du noyau, sans clé ; l'évaluateur est la richesse de pari scellée du noyau. Agentic Scientist v3 est écarté tant que ses agents héritent des clés (a12).
- **E5 et E6 donnent H_B** : les mécanismes propres de l'organisme sont retirés du chemin critique, quelle que soit la voie.

---

## (c) Mesure minimale pour chaque instrument

Toutes les valeurs de fausses alertes ci-dessous sont **illustratives**.

**c1. Sondes sur les activations**

- *Mesure* : taux de détection à 1 % et à 5 % de fausses alertes.
- *Cas honnêtes appariés* : paires minimales de même texte, qui ne diffèrent que par l'indice d'évaluation ou d'usage réel, avec l'indice lexical tenu constant dans la paire. Plus des tâches témoins à étiquettes aléatoires (Hewitt & Liang, 2019, « Designing and Interpreting Probes with Control Tasks ») pour mesurer la sélectivité.
- *Vérifications mécaniques à battre* : régression logistique sur sac de mots du seul texte ; longueur ; la liste `MOTS_CLES_*` de l'organisme. C-16 rappelle que la détection multi-familles s'y fait « sur les mots du texte » (RAPPORTÉ).
- *Conditions de validité* : une sonde qui ne bat pas le sac de mots sur les paires appariées ne mesure pas les activations. Il faut aussi rapporter la tenue sur une famille ou une distribution tenue à l'écart.

**c2. Garanties séquentielles de fausses alarmes**

- *Mesure* : taux empirique de fausses alarmes **sur tout l'horizon**, avec arrêt optionnel, sous des flux nuls, à comparer à α. Puis délai de détection sous alternative.
- *Cas honnêtes appariés* : flux honnêtes *dépendants et non stationnaires* (AR(1), dérive lente), car c'est là que les garanties i.i.d. cèdent. Chaque flux est apparié à son jumeau avec rupture plantée au même instant.
- *Vérifications mécaniques à battre* : test à taille fixe répété à chaque pas, qui doit gonfler α et sert de témoin positif de l'inflation ; Bonferroni ; CUSUM à seuil calibré par simulation.
- *Conditions de validité* : la garantie tient si le taux reste ≤ α sous dépendance. Elle est utile si le délai n'excède pas celui du CUSUM de plus d'un facteur fixé d'avance.
- *Référence* : Howard, Ramdas, McAuliffe & Sekhon (2021), « Time-uniform, nonparametric, nonasymptotic confidence sequences », *Annals of Statistics*.

**c3. Moniteurs et leurs tests d'acceptation**

- *Mesure* : taux de détection à 0,1 % et à 1 % de fausses alertes sur des sabotages plantés. Le billet D rapporte que le régime à bas taux est celui où les moniteurs promptés défaillent.
- *Cas honnêtes appariés* : la même tâche, la même trace, sans la modification plantée.
- *Vérifications mécaniques à battre* : exécution des tests unitaires ; règles sur le diff ; mots-clés.
- *Test d'acceptation du test* : il doit **rejeter** un moniteur constant, un moniteur aléatoire et un moniteur inversé. C'est l'extension de la règle de discriminance CA-19 (sortie parfaite contre sortie inversée), RAPPORTÉ, qui a déjà écarté la métrique de forme.

**c4. Évaluation scellée du pôle**

- *Mesure* : écart de score entre la part publique et la part scellée, et taux auquel un agent « tricheur » dépasse le meilleur agent honnête.
- *Cas honnêtes appariés* : le même agent, avec et sans accès à la part publique.
- *Vérifications mécaniques à battre* : jetons-témoins dans la part scellée, recherchés dans les sorties ; empreinte du réservoir vérifiée avant et après.
- *Seuil de défaillance* : tout jeton-témoin retrouvé invalide la course.

**c5. Aptitude darwinienne**

- *Mesure* : taux de promotion des lois fausses plantées (fausse survie), taux d'élimination des lois vraies plantées (fausse élimination), et poids des tautologies.
- *Cas honnêtes appariés* : loi vraie et loi fausse de même forme et de même contenu.
- *Vérifications mécaniques à battre* : sélection aléatoire et survie binaire (E1).

**c6. Filtre de compatibilité bisociatif**

- *Mesure* : précision et rappel sur des paires compatibles et incompatibles plantées.
- *Vérifications mécaniques à battre* : similarité cosinus de plongements de texte ; tirage au hasard.
- *Conditions de validité* : un filtre qui ne bat pas la similarité cosinus n'est pas un filtre de *contraintes*.

**c7. Validation des réécritures de code**

- *Mesure* : taux de rejet d'un corpus de mutations interdites plantées (code brut définissant `recompense_interne`, `import ast`, coût sans borne) et taux de rejet à tort de mutations légitimes du gabarit.
- *Point de départ* : les essais C-17 existent, RAPPORTÉ. La mesure sur corpus n'est pas dans les faits.

**c8. Grille ou juge par modèle (Agentic Scientist v3, si adopté)**

- *Mesure* : corrélation avec la vérité scellée du monde planté, à comparer aux 0,44 rapportés par les auteurs entre notes de relecteurs-agents et performance.
- *Vérification mécanique à battre* : le score scellé lui-même. Un juge qui n'ajoute rien au score scellé ne sert pas.

---

## (d) Ancrage matériel

Tout ce qui suit est **illustratif** : aucun chiffre ne vient des faits, hors les bornes du noyau rapportées.

- **Monde planté et E1 à E7** : Python pur sur processeur. Générer et évaluer 10⁵ tests synthétiques prend de quelques minutes à une heure sur 16 cœurs.
- **Appels aux modèles** pour formuler, recombiner et prédire :
  - par bras et par expérience, de l'ordre de 1 500 à 3 000 appels de 2 000 à 4 000 jetons, soit 15 à 20 bras et environ 40 000 appels au total ;
  - dans le noyau, sous ses bornes d'appels et de coût (RAPPORTÉ : le noyau borne appels, coûts et temps ; `max_tokens` inclut la réflexion, § 2.9) ;
  - coût en argent non estimé ici faute de tarif dans les faits. À calculer sur `budget()`.
- **Modèles ouverts pour c1** :
  - famille Pythia (Biderman et al., 2023, « Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling »), de 160M à 1B, pour une extraction d'activations sur processeur en quelques heures pour 10⁴ invites courtes ;
  - un modèle de 7 à 8 milliards de paramètres à poids ouverts, quantifié en 8 bits (par exemple de la famille Qwen2.5 ou OLMo), en lecture seule des activations : de l'ordre de 1 s par invite de 200 jetons sur processeur, soit environ 3 h pour 10⁴ invites.
- **Bac à sable** : celui du noyau, sans réseau et sans clé (RAPPORTÉ : isolation `unshare -n`, utilisateur `nobody`, environnement vide, dans les corrections). Pour la voie hybride, OpenEvolve tourne *sous* ce bac à sable ; les appels de modèle passent par le relais du noyau.
- **Délai** :
  - E1 à E3 : trois à quatre jours, en comptant la construction du monde planté ;
  - E4 à E6 : deux jours de plus ;
  - E7 : un jour.

  Cela tient à peine dans la semaine demandée. Si le temps manque, E1, E3 et E4 passent en premier.

### Ce qui me ferait changer d'avis

- **Le substrat domine** : en E4, l'effet du substrat dépasse celui de l'aptitude. Le manque est alors un substrat d'exécution, et adopter un moteur de la littérature passe devant l'écriture d'un critère.
- **E2 ne montre aucun effet de Goodhart** : l'engagement préalable suffit, et le réservoir scellé est un coût inutile.
- **Le contrôle négatif de E1 échoue pour le pari** : la richesse de pari promeut des hypothèses dans un monde sans loi, et l'aptitude proposée est fausse dans sa mise en œuvre.

FIN-DE-CELLULE