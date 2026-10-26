# Cellule B — Tour III.2 : équipe rouge croisée

**Pièce absente :** C4 (mondes à ponts plantés de conv-audit) n'a pas été rendue au départ du tour. Rien ci-dessous n'en suppose le contenu.

**Statuts :** les chiffres tirés de C1, C2, C3a, C3b et R-525 sont RAPPORTÉ, car aucune de ces pièces n'est auditée par une autre famille. C3a le dit lui-même. Toutes mes objections sont des HYPOTHÈSES sur la conception des autres propositions. Ce ne sont pas des résultats. Les chiffres qui ne viennent pas des faits sont marqués « illustratif ».

---

## Contre la proposition A

### (a) Failles

**A1. Dans E1, le bras « stratifié » reçoit plus d'information que le bras « noyau ».** Le bras (2) stratifie par cellule domaine × opérateur. Le noyau corrigé c1/c5, lui, ne voit que S = ⟨d,d⟩², donc le domaine (C3b, essai 3, RAPPORTÉ). Toute victoire du bras (2) peut venir de l'accès aux étiquettes d'opérateur, et non de la supériorité de la stratification sur la répulsion. C'est une variable confondante directe : le mécanisme de tirage et l'information d'entrée sont confondus.

**A2. La stratification par étiquettes vraies donne une diversité vraie par construction.** A le reconnaît en (a)1 : un tirage stratifié par étiquette de domaine donne une diversité « proche de 1 trivialement ». Il l'utilise pourtant comme bras comparé, sur des mondes où les étiquettes sont les étiquettes plantées. Le noyau, lui, travaille sur des vecteurs d_i bruités (norme de bruit ≈ 0,6 dans C3b, RAPPORTÉ).

La comparaison loyale demande des **étiquettes estimées** à partir des mêmes d_i, par regroupement à n ∈ [12, 50]. A ne dit jamais comment la v0 obtiendra ses étiquettes de domaine. Sa recommandation (Q5, point 2) repose donc sur un instrument absent de son tableau (c).

**A3. Le contrôle négatif de E1 teste la métrique, pas le tirage.** « Étiquettes de domaine permutées → les trois bras au niveau uniforme. » Le noyau n'utilise pas les étiquettes, il utilise d_i. Deux cas se présentent :
- si la diversité est calculée sur les étiquettes permutées, la chute au niveau uniforme est garantie pour tous les bras, quel que soit leur mérite ;
- si elle est calculée sur les étiquettes vraies, le noyau ne bouge pas et le contrôle « échoue » sans que rien ne soit faux.

Dans les deux cas, le contrôle n'apporte aucune information.

**A4. E1 n'est pas une inférence forte complète (B4).** H_A dit « le noyau fait mieux » ; H_B dit « la stratification égale le noyau ». Si la stratification fait **mieux** de plus de 0,02, les deux sont falsifiées et l'issue n'est pas couverte. Il faut écrire H_B : « le noyau ne fait pas mieux que la stratification ».

**A5. E2 : une hypothèse de continuité ne peut pas être falsifiée sur cette grille.** La grille compte cinq valeurs de ε, avec un pas de 0,2 entre 0,3 et 0,5. La « falaise » est définie par un pas de 0,1 (illustratif). La grille ne contient pas la résolution qui définit H_B. De plus, les homonymes sont « contrôlés par l'axe contrainte du filtre » : on plante des homonymes que le filtre sait détecter. C'est le défaut que C3b §5 avoue pour son propre filtre (lexique planté identique au lexique du détecteur, précision 1,000 sans valeur, RAPPORTÉ).

**A6. E3 compare à une ligne de base qui vaut zéro par construction.** Une juxtaposition gabarit ne peut, par définition, rien prédire hors de l'union des domaines des parents. Sa « détection » de prédictions nouvelles correctes est donc nulle. Le seuil « +15 points sur le gabarit » se réduit à « ≥ 15 % de filles avec une prédiction nouvelle correcte ».

Ce seuil est battu par un fuseur qui émet des prédictions **au taux de base**. Si la classe majoritaire d'un monde planté vaut 60 % (illustratif), une fille qui prédit cette classe sur une instance hors des parents est « nouvelle et correcte » dans 60 % des cas, sans aucun pont. Le critère « ≥ 1 instance correcte où aucun parent ne prédit » n'est corrigé ni pour le hasard ni pour le nombre d'instances tentées.

**A7. Le champ (iv) de la consigne E3 est déclaratif.** « Ni A ni B n'impliquent P » est une affirmation du fuseur. Le mécanisme ne la vérifie pas, sauf sur monde planté, où l'unification sert alors aussi de juge.

**A8. E4 : la métrique n'est pas définie et deux fuites restent ouvertes.**
- Le Hit@10 n'a pas de taille de piscine candidate. Sans elle, Hit@10 n'a pas de sens.
- Le contrôle « t₀ décalé de −10 ans → Hit@10 au niveau du nul » n'est pas un contrôle négatif propre. Un bon prédicteur peut annoncer un lien qui se réalisera treize ans plus tard. L'échec du contrôle peut donc signaler une vertu.
- La sonde de fuite (« le modèle cite-t-il le pont à froid ? ») ne détecte que la fuite verbalisée. Elle crée en outre un biais de sélection : ne restent que les ponts obscurs, pas les ponts typiques.
- HYPOTHÈSE à vérifier : l'étiquetage en concepts d'OpenAlex est produit par un classifieur appliqué rétroactivement. Si c'est le cas, les étiquettes de domaine d'avant t₀ sont calculées avec un modèle postérieur à t₀, ce qui est une fuite temporelle dans l'instrument d'entrée.
- La contrainte « coupe d'entraînement du fuseur antérieure à t₀ » avec « ≥ 20 articles joints entre t₀ et t₀ + 3 ans » restreint le choix à des modèles anciens. A ne chiffre pas ce que cela coûte en qualité de fusion.

**A9. E5 est truqué en faveur de l'appariement par opérateur.** Sur des mondes où le pont est *défini* comme un opérateur partagé et où des homonymes sont plantés « là où Swanson est attendu fragile », le résultat est écrit d'avance. Le duel n'est loyal que si le générateur de mondes plante aussi des ponts de type A–B–C par terme intermédiaire qui ne passent pas par un opérateur.

**A10. Le seuil de 12 points est importé sans étalonnage.** Le « ~12 points » de R-525 (RAPPORTÉ) est un seuil rond, exactement ce que C2 reproche aux protocoles de C1. A le réutilise en E4 sans plancher A/A, alors que R-525 met l'étalonnage A/A en tête de sa première expérience.

### (b) Scénarios d'évasion

L'agent adverse est soit le fuseur, soit l'étage amont qui rédige les hypothèses ou résumés parents.

| Instrument de A | Évasion | Coût |
|---|---|---|
| Extracteur d'opérateurs (100 résumés étiquetés) | Saturer le texte de jetons d'opérateur rares mais vides (« cohomologie », « symplectique ») : rappel élevé sur l'annotation humaine, qui marque la présence, pas l'usage | ≈ 0 ; quelques mots |
| Tirage stratifié domaine × opérateur | Écrire dans un jargon atypique pour être classé dans une cellule peu peuplée, donc tiré plus souvent | ≈ 0 |
| Filtre de compatibilité | Paraphraser hors lexique : C3b mesure déjà 34,4 % de contradictions qui passent en régime réaliste, rappel 0,608 (RAPPORTÉ) | ≈ 0 |
| Critère « prédit plus » (≥ 1 instance) | Émettre de nombreuses prédictions au taux de base hors des domaines des parents ; quelques-unes seront correctes | ≈ 0 en tokens ; seul le nombre d'instances évaluées limite l'attaque |
| Rétrodiction | Ne pas citer le pont à froid (passer la sonde) tout en l'ayant mémorisé | 0 ; c'est le comportement par défaut d'un modèle peu bavard |

**Toutes à la fois.** Un fuseur reçoit des parents rédigés avec des opérateurs rares (passe le tirage), sans marqueur de contradiction (passe le filtre). Il produit une fille qui recopie les deux parents et ajoute dix prédictions au taux de base sur des instances nouvelles (passe E3), sans jamais nommer le pont réel (passe la sonde de E4). Coût marginal : quelques centaines de tokens par fille (illustratif). Aucun instrument de A ne fait payer la multiplicité des prédictions.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Fille au taux de base** (E3) : remplacer la fille par un prédicteur constant sur les instances nouvelles. Si elle franchit le seuil, le critère est vide.
2. **A/A** (E1, E4) : deux courses du même bras, graines différentes, pour fixer le plancher de bruit avant tout seuil.
3. **Stratification sur étiquettes estimées** (E1) : même extracteur et même regroupement pour les deux bras ; sinon A1 et A2 suffisent à expliquer l'issue.
4. **Mondes à ponts non-opérateurs** (E5) : ponts de type terme-B plantés. Sans eux, la victoire de l'appariement par opérateur est acquise par construction.
5. **Piscine de rétrodiction de taille fixée et publiée** avant le run (E4).

---

## Contre la proposition C

### (a) Failles

**C1. C change des statuts (règle 1).** Les références de Mouret et Clune (2015), Gentner (1983), Falkenhainer, Forbus et Gentner (1989) et Swanson (1986) sont marquées **VÉRIFIÉ**. Aucune pièce ne les vérifie. Les attributions me semblent correctes, mais VÉRIFIÉ est un statut de fait audité, et l'attribution de C ne le gagne pas. Plus grave : C qualifie de « validée au tour précédent » la mesure de contenu « risque × couverture », alors que R-525 la classe en « écrite, non courue » (RAPPORTÉ, et HYPOTHÈSE pour sa validité). Enfin, l'explication « paradoxe des anniversaires » de la réussite de c5 est étiquetée OBSERVÉ-NON-AUDITÉ. C'est une inférence de C, donc une HYPOTHÈSE.

**C2. C décrit mal c5.** Selon C, c5 « cherche une paire partageant un opérateur parmi les 6 paires tirées ». Si c'était le cas, c5 vaudrait c1 sur « bisoc » (0,415 à 0,770, RAPPORTÉ). Or C3b rapporte 0,995 à 1,000 pour c5, « paire garantie après tirage ». c5 modifie donc l'ensemble ; il ne fait pas que chercher dedans.

L'argument central de C contre c5 (« à nombreux opérateurs fins, aucune paire dans les 4 tirés ») vise donc une méthode qui n'est pas c5. La vraie question, non testée, est autre : **combien la garantie coûte-t-elle en diversité quand les opérateurs sont nombreux ?** C3b ne mesure ce coût (0,005 à 0,011) qu'à 8 opérateurs (RAPPORTÉ).

**C3. L'argument Jacobi est hors sujet.** La sélection gloutonne de C3b est déterministe (1 ensemble sur 50, RAPPORTÉ). Elle n'exige pas de décomposition spectrale : un déterminant de taille k = 4 se calcule par élimination. La non-convergence de Jacobi à 120 rotations (RAPPORTÉ) concerne l'instrument de l'organisme, pas le noyau corrigé. Le procès en « complexité inutile » peut être juste, mais il n'est pas établi par ce fait.

**C4. L'expérience 1 confond représentation et mécanisme.** Elle oppose « c5 sur SimHash/n-grammes » à « grille sur arbres syntaxiques canonisés + b+ ». Deux facteurs changent à la fois. Si la grille gagne, on ne saura pas si c'est la grille ou la canonisation.

Pire, les isomorphismes plantés sont définis comme « même équation génératrice sous renommage des variables ». Un canoniseur d'arbres qui renomme les variables retrouve exactement la définition du générateur. C'est une fuite entre l'instrument et l'évaluation : le bras H_B est jugé par sa propre définition. Il faut un plan 2 × 2 (tirage × représentation), avec un générateur de mondes écrit par un autre agent que le canoniseur.

**C5. L'expérience 1 n'est pas une inférence forte (B4).** H_A (« c5 suffit quand les vocabulaires sont disjoints ») et H_B (« c5 est aveugle en présence d'homonymes ou de notations disjointes ») portent sur des **régimes différents** : les deux peuvent être vraies ensemble. Les seuils laissent aussi une région où aucune n'est falsifiée. Par exemple (illustratif) : c5 à un rappel de 0,6 avec +13 points sur le nul, et la grille à 0,85 avec +16 points de précision. Les deux survivent.

**C6. L'expérience 2 retire la partie difficile du problème.** La piscine (2 parents réels + 14 + 14 articles des deux domaines du pont) est construite en connaissant l'issue : le choix des **deux domaines** parmi tous, qui est le vrai problème de découverte, est donné.

Deux autres fuites s'ajoutent :
- la métrique accepte « une paire partageant exactement le même opérateur formel que J_AC » : l'opérateur cible est extrait de l'article postérieur, puis sert à noter un sélecteur qui apparie justement par opérateur ;
- les triplets (opérateur, contrainte, variable) de J_AC seront extraits par un modèle de langue, probablement de la même famille que le fuseur, ce qui corrèle juge et jugé.

Quant à l'anonymisation des entités, elle laisse intact le vocabulaire d'opérateur, qui est le signal. Elle écrase en revanche les vecteurs de domaine d_i calculés sur le texte. La seconde passe ne teste donc pas « le même sélecteur sans fuite » mais un autre sélecteur.

**C7. L'expérience 3 repose sur un banc qui n'existe pas.** Les « 50 paires parentes survivantes du banc R-525 » supposent la première expérience de R-525 faite. Elle ne l'est pas (R-525, RAPPORTÉ).

Le témoin max(P_A, P_C) n'est pas une loi prédictive normalisée : la richesse de martingale n'est pas définie dessus sans renormalisation, qui n'est pas spécifiée. Et « taux de promotion des chimères ≤ α » ignore la multiplicité. Avec N filles testées, l'inégalité de Ville borne chaque fille séparément, et l'espérance du nombre de promotions à tort atteint N·α.

**C8. Le critère Popper–Lakatos de C récompense ce qu'il veut exclure.**
- Contenu = KL(P_H ‖ P₀) × |D(H)| : la fille maximise le KL en étant **plus confiante** et maximise la couverture en **déclarant** un domaine large. Les deux termes sont sous le contrôle de l'agent.
- La divergence JS ≥ δ par rapport aux deux parents sur leur intersection récompense le désaccord, pas le contenu. Une sortie aléatoire la satisfait.
- Seule l'étape 3 (tirages frais) sanctionne. Le filtre *ex ante* censé économiser ces tirages ne trie donc rien d'utile.

**C9. b+ adossé à l'archive de l'organisme.** C3b dit explicitement que l'usage de l'archive comme corpus de fond n'est « pas vérifié » (RAPPORTÉ). L'archive est biaisée vers ce que l'organisme a déjà exploré. HYPOTHÈSE : un opérateur réellement fertile mais déjà souvent employé par l'organisme dépassera f_fond = 0,10 et sera rejeté comme hub. Le seuil 0,10 vient d'un réglage synthétique de C3b.

**C10. La grille « ne rate jamais un pont rare » seulement si l'extraction est exacte.** C'est l'hypothèse que C attaque chez c5 (réserve de C3b §5, RAPPORTÉ). La grille exige aussi une discrétisation des domaines (k-means à n = 12 à 50) et un seuil dur ⟨d,d⟩² < 0,25 : deux paramètres sans étalonnage. Elle est déterministe : mêmes paires à chaque génération, sans exploration.

### (b) Scénarios d'évasion

| Instrument de C | Évasion | Coût |
|---|---|---|
| Filtre anti-hubs b+ | Remplacer un hub par un synonyme rare (« gradient » → périphrase) : la fréquence de fond tombe sous 0,10 | ≈ 0 |
| Grille domaine × opérateur | Le même synonyme rare crée une colonne d'opérateur artificielle, peuplée dans deux domaines : pont « déterministe » vide | ≈ 0 |
| Filtre de contraintes à deux étages | Étage lexical : paraphrase (34,4 % passent, RAPPORTÉ). Étage arbre C-17 : déclarer des plages de paramètres larges qui s'intersectent toujours | ≈ 0 |
| Test de divergence (instrument 5) | Rejet si H_AC ∈ {H_A, H_C, ½(H_A+H_C)} sur > 80 % des points : une moyenne pondérée 0,51/0,49, ou une perturbation de 10⁻³, passe | 0 |
| Gain de contenu *ex ante* | Gonfler la confiance (KL) et le domaine déclaré | 0 |
| Survie de Ville | Générer N variantes de la même fille : ≈ N·α promotions à tort sous le nul | N fusions, soit quelques centimes chacune (illustratif) |

**Toutes à la fois.** L'agent écrit des parents dont les opérateurs sont des périphrases rares. Il passe b+, crée une colonne de grille et un « pont » déterministe. Il déclare des plages larges pour passer le vérificateur C-17. Il émet une fille surconfiante, à domaine déclaré maximal, égale à un mélange 0,51/0,49 des parents légèrement perturbé. Il la décline en 20 variantes (illustratif). Coût total : 20 fusions. Espérance à α = 0,05 : environ une promotion fausse par lot, et seul l'étage 3 limite les dégâts. Les étages 1 et 2, présentés comme mécaniques, ne filtrent rien.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Plan 2 × 2** (c5 contre grille, SimHash contre arbres canonisés) dans l'expérience 1, avec un générateur de mondes écrit par un autre agent que le canoniseur.
2. **Fille « mélange perturbé »** (0,51/0,49 + ε) et **fille surconfiante à domaine large** : elles doivent être rejetées. Sinon, le critère *ex ante* est vide.
3. **Contrôle de multiplicité** : budget fixe de filles par paire, ou contrôle du taux de fausses découvertes par e-valeurs (procédure e-BH ; référence à vérifier). Sans cela, « ≤ α » est faux dès la deuxième fille.
4. **Piscine de rétrodiction non conditionnée** sur les deux domaines du pont : le sélecteur doit aussi choisir les domaines. Et opérateur cible extrait **avant** t₀, ou par un extracteur aveugle à J_AC.
5. **Synonymes rares de hubs plantés** : b+ doit les rejeter. Sinon, la grille fabrique des ponts sur commande.
6. **A/A** avant tout seuil, comme pour A.

---

## Ce que l'attaque révèle sur le point où A et C s'accordent, et un test qui le tranche

Je m'en sers sans fusionner les deux propositions. A et C recommandent tous deux d'abandonner le noyau au profit d'une stratification ou d'une grille. Chez l'un comme chez l'autre, cette conclusion repose sur des étiquettes de domaine et d'opérateur supposées disponibles, qu'aucun des deux ne mesure (A1, A2, C10). Le seul instrument qui fasse foi dans les pièces, le correctif de C3b, a lui aussi été évalué sur étiquettes plantées (C3b §5, RAPPORTÉ).

**Test (inférence forte).**
- **H_A** : à étiquettes **estimées** par le même extracteur et le même regroupement, la stratification avec paire garantie atteint une proportion de « bisoc vrai » (contre la vérité plantée) au moins égale à celle de c5, moins un bruit fixé par A/A.
- **H_B** : c5 dépasse la stratification de plus que ce bruit, parce que la répulsion continue sur d_i absorbe les erreurs de frontière de domaine que la discrétisation propage.
- **Grille** : n ∈ {12 ; 30 ; 50} ; bruit d'étiquette d'opérateur ε ∈ {0 ; 0,1 ; 0,2 ; 0,3} ; nombre d'opérateurs ∈ {8 ; 40} (illustratif).
- **Contrôle négatif** : mondes sans pont planté, où les deux bras doivent tomber au niveau du hasard.

Chaque issue falsifie une recommandation : H_A falsifie le maintien du noyau, H_B falsifie la v0 « grille seule » de A et de C. Le test se court sur processeur seul, en réutilisant le code de C3b (coût 0 USD selon C3a, RAPPORTÉ).

FIN-DE-CELLULE