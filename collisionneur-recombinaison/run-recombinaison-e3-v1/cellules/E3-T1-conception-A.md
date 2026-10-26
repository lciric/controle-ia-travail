# Cellule A — Tour III.1 : trancher l'étage de recombinaison bisociative

**Pièce manquante** : C4 (mondes à ponts plantés de conv-audit) est absente au départ du tour ; rien de ce qui suit n'en suppose le contenu.

**Statut global des pièces** : C1, C2, C3a, C3b et la synthèse R-525 sont RAPPORTÉ (pièces du programme, non auditées par moi). C3a dit lui-même que les verdicts de génération 0 ne sont « pas encore vérifiés par un agent d'une autre famille » : je les traite comme RAPPORTÉ, jamais comme VÉRIFIÉ.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Que le tirage ait une importance en soi.** La forme corrigée (similarité de domaine dans S, qualité à part, paire d'opérateur forcée après tirage, variante c5) atteint 0,995–1,000 de « bisoc » — mais **par construction** : la paire est garantie après coup. La diversité de domaine (0,89–0,95) n'a été comparée qu'à un tirage *uniforme* (0,74–0,79) et à un tri par qualité (C3b, essai 3). Elle n'a jamais été comparée à un **tirage stratifié par étiquette de domaine**, qui donne une diversité de domaine proche de 1 trivialement. Statut : RAPPORTÉ pour les chiffres ; HYPOTHÈSE que la répulsion déterminantale apporte quoi que ce soit au-delà de la stratification. C'est la supposition centrale, et elle est non testée.

2. **Que les étiquettes d'opérateur et de domaine existent.** Les méthodes c3–c5 « utilisent les étiquettes d'opérateur, supposées extraites » (C3b, §5). Les vecteurs d_i, o_i de l'essai 3 sont des prototypes synthétiques bruités, pas des textes. Les cinq castes avouent qu'à partir de résumés < 150 mots, l'interface est vide ou bruitée dans 25–35 % des tirages (C1 ; chiffres déclarés, non mesurés). Statut : HYPOTHÈSE. Sans extracteur mesuré, la forme corrigée n'a pas d'entrée.

3. **Que « domaine éloigné + opérateur partagé » soit la bonne définition d'un pont.** C'est la thèse bisociative (Koestler) reprise par toutes les castes ; aucune pièce ne la teste contre une autre définition (pont par terme-B de Swanson, isomorphisme relationnel). R-525 classe « que la bisociation batte un tirage stratifié » en HYPOTHÈSE. Statut : HYPOTHÈSE.

4. **Que le filtre de compatibilité fonctionne sur du réel.** C3b : contradictions acceptées 57,4 % → 0,0 % sur lexique propre (le lexique planté est celui du détecteur, C3b §5 le reconnaît), 55,9 % → 34,4 % en régime réaliste avec rappel 0,608. Et 65–67 % des interfaces B non vides n'ont *aucun* pont planté (C4 réfutée). Statut : RAPPORTÉ ; la « garantie » est éliminée, le réducteur est indécis.

5. **Que « prédire plus que ses parents » soit mesurable.** La question le suppose ; la seule définition disponible (R-525 : risque déclaré × couverture du domaine) est « écrite, non courue ». Statut : HYPOTHÈSE.

6. **Que l'étage amont (sélection par réfutation) ne promeuve pas du faux.** R-525 fait de ce point la *première* expérience, non réalisée. Recombiner des survivantes d'un filtre non validé peut recombiner des artefacts de Goodhart. Statut : HYPOTHÈSE.

7. **Que la rétrodiction soit faisable sans fuite.** Un modèle de langue entraîné après t₀ connaît les ponts réalisés ; le nul « même consigne, même filtre » ne corrige pas la fuite, il la partage. Statut : HYPOTHÈSE, et c'est la menace principale sur le test 4.

8. **Que la forme corrigée dérive d'une analyse du code réel.** C3a/C3b : `_score_pertinence_texte`, Cholesky et le log-déterminant « n'existent pas dans la v6.2.1 » (F1, F2 réfutées). La forme corrigée a été définie par conv-audit (C2) en réaction à un rapport bâti sur un code imaginaire ; elle n'hérite pas du défaut, mais la **ligne de base v6.2.1 réelle** (moissonnage + tri réels) n'a jamais été mesurée. Statut : RAPPORTÉ.

---

## (b) Expériences décisives (inférence forte)

Toutes les cellules partagent un corpus, des graines et une consigne de fusion identiques ; chaque seuil est **illustratif** sauf mention.

### E1 — Le noyau sert-il à quelque chose ? (répond à Q1 et Q5)

- **H_A** : la répulsion déterminantale sur S = ⟨d,d⟩² augmente la diversité de domaine ou la qualité des filles au-delà d'un tirage stratifié par cellule (domaine × opérateur) avec la même paire forcée après tirage.
- **H_B** : stratification + paire forcée égale le noyau corrigé, à un bruit près.
- **Bras** : (1) c5 de C3b ; (2) tirage stratifié + c5 ; (3) uniforme + c5 (témoin faible).
- **Métriques** : diversité de domaine, « bisoc » vrai contre vérité plantée, qualité q, et en aval le taux de filles à prédiction nouvelle correcte (défini en E3).
- **Seuil** : différence (1)–(2) < 0,02 sur chaque métrique (illustratif ; de l'ordre des erreurs-types ≤ 0,021 rapportées par C3b) → H_B.
- **Contrôle négatif** : étiquettes de domaine permutées au hasard ; les trois bras doivent tomber au niveau uniforme (0,74–0,79, RAPPORTÉ). Sinon la métrique lit autre chose que le domaine.
- **Issues** : H_B falsifie la pertinence du noyau pour la v0 (on garde la stratification, moins de code, pas de Jacobi). H_A falsifie ma recommandation en (c)/(5).

### E2 — Où la forme corrigée cède (Q1)

- **H_A** : la dégradation du « bisoc » vrai est continue dans le bruit d'étiquette ε (fraction d'opérateurs mal attribués), la séparation de domaine s (distance entre prototypes), la part de hubs h et la taille n ∈ {12, 20, 50}.
- **H_B** : il existe une falaise (perte > 0,3 de bisoc vrai pour un pas de ε de 0,1, illustratif).
- **Grille** : ε ∈ {0 ; 0,1 ; 0,2 ; 0,3 ; 0,5} ; s ∈ {0,2 ; 0,6 ; 1,0} ; h ∈ {0 ; 0,3} ; homonymes plantés (même jeton d'opérateur, deux sémantiques, contrôlé par l'axe « contrainte » du filtre).
- **Métrique** : bisoc *vrai* (contre la vérité plantée, pas contre l'étiquette observée) ; taux de « faux ponts » = paires forcées sur un homonyme.
- **Contrôle négatif** : ε = 1 (étiquettes aléatoires) → bisoc vrai au niveau du hasard ; si le pipeline reste haut, il triche via d_i.
- **Issues** : H_B à ε ≤ 0,2 falsifie l'usage de la forme corrigée sur résumés bruts (il faut d'abord un extracteur mesuré, (c)). H_A falsifie la crainte des castes 2/4/5 sur l'instabilité, et borne ε tolérable.

### E3 — La fille prédit-elle plus ? (Q3)

- **H_A** : une consigne de fusion à **prédiction obligatoire** (ci-dessous) produit, sur mondes plantés, une part de filles à prédiction nouvelle et correcte supérieure à celle d'une juxtaposition gabarit sans modèle.
- **H_B** : part égale ou inférieure ; le modèle ajoute des chimères (prédictions nouvelles fausses) sans ajouter de vraies.
- **Consigne (proposition A)** : la fille doit énoncer (i) l'opérateur partagé O et ses préconditions *dans chacun des parents* ; (ii) **une** observable P et sa valeur prédite ; (iii) l'observation qui réfuterait P ; (iv) l'affirmation que ni A seul ni B seul n'impliquent P. Tout élément manquant → rejet mécanique avant évaluation.
- **Critère mécanique de « juxtaposition »** : sur un monde planté, la fille est une juxtaposition si l'ensemble des instances où sa prédiction est définie est l'union des ensembles des parents, à prédictions égales ; elle « prédit plus » si elle est définie et correcte sur ≥ 1 instance où aucun parent ne prédit (version opérationnelle de la classe des falsificateurs potentiels de Popper, *The Logic of Scientific Discovery*, 1959, chap. VI — référence à vérifier pour le chapitre).
- **Métriques** : taux de filles « plus que les parents et correctes » (détection) ; taux de filles « nouvelles et fausses » (chimères) ; taux de rejets mécaniques.
- **Seuil** : H_A si détection(consigne) − détection(gabarit) ≥ 15 points avec chimères ≤ chimères(gabarit) + 5 points (illustratif).
- **Contrôle négatif** : parents du **même** domaine sans isomorphisme planté → détection ≤ α = 5 % ; parents permutés (A d'une paire, B d'une autre) → idem. Si l'un dépasse α, le fuseur hallucine des ponts.
- **Issues** : H_B falsifie l'idée qu'un modèle de langue est l'opérateur de fusion de la v0 (on garde un gabarit + unification mécanique). H_A falsifie « la fusion est décorative » (verdict de C2 sur le « pushout »).

### E4 — Rétrodiction sur littérature réelle (Q4)

- **H_A** : le pipeline (tirage + filtre + fusion) place la paire de champs réellement reliée après t₀ parmi ses k premières propositions plus souvent que le nul stratifié à même consigne et même filtre.
- **H_B** : écart < 12 points (seuil repris de R-525, RAPPORTÉ).
- **Données** : OpenAlex (déjà source de l'organisme, RAPPORTÉ) ; paires de concepts (niveau 1–2) sans co-occurrence d'auteur ni co-citation avant t₀, avec ≥ 20 articles joints entre t₀ et t₀ + 3 ans (illustratif) ; 50 paires positives, 50 paires « jumelles » appariées en taille et croissance mais restées disjointes.
- **Métrique** : Hit@10 de la paire réalisée ; AUC positives contre jumelles.
- **Fuite** : t₀ doit être *postérieur* à la coupe d'entraînement du fuseur, ou le fuseur n'intervient qu'après l'appariement (le tirage et le filtre sont mécaniques, donc sans fuite) ; sonde de fuite = le modèle, interrogé à froid sur la paire, cite-t-il le pont réalisé ? Toute paire citée est exclue.
- **Contrôle négatif** : t₀ décalé de −10 ans sur les mêmes paires (le lien n'existe pas encore dans les données servies) → Hit@10 au niveau du nul ; et paires « jumelles » → ≤ nul.
- **Issues** : H_B falsifie la valeur de l'appariement par opérateur sur du réel (restent la stratification et le filtre). H_A falsifie l'objection « chimères verbales » au niveau de l'appariement — pas au niveau de la fille, qui exige E3.

### E5 — Duel de mécanismes (Q2)

- **H_A** : l'appariement par opérateur partagé trouve plus de ponts plantés que le modèle A–B–C de Swanson par terme intermédiaire, à même nul.
- **H_B** : Swanson égale ou dépasse.
- **Métrique** : rappel des ponts plantés à budget de paires égal ; taux de faux ponts sur homonymes plantés (où Swanson est attendu fragile — argument de la caste 4, RAPPORTÉ, non mesuré).
- **Contrôle négatif** : mondes sans pont planté → les deux à ≤ α.
- **Issues** : chaque issue élimine un mécanisme de la v0.

---

## Q2 — Trois mécanismes, et lequel produit des ponts vrais

**Découverte fondée sur la littérature (Swanson, A–B–C).** Source : Swanson, 1986, « Fish oil, Raynaud's syndrome, and undiscovered public knowledge », *Perspectives in Biology and Medicine*. Le pont est un terme B partagé par deux littératures qui ne se citent pas. Force : nul naturel par rétrodiction, données publiques. Faiblesse : B est un **jeton**, donc l'homonymie inter-domaines fabrique des ponts verbaux (caste 4, RAPPORTÉ) ; C3b montre en outre que les « ponts » lexicaux sont dominés par mots-outils et gabarit (35 ex aequo, 0 pivot). Produit des *candidats* vrais au niveau du couple de littératures, pas des hypothèses filles.

**Appariement de structures (analogie structurelle).** Source : Gentner, 1983, « Structure-Mapping: A Theoretical Framework for Analogy », *Cognitive Science* ; moteur SME : Falkenhainer, Forbus & Gentner, 1989, « The Structure-Mapping Engine: Algorithm and Examples », *Artificial Intelligence*. Le pont est une correspondance de **relations** (systématicité), indépendante des jetons : c'est le seul des trois dont le critère de pont est mécanique et aveugle aux homonymes. Faiblesse : il exige des représentations relationnelles, c'est-à-dire exactement l'extraction d'opérateurs qui manque (point (a)2). C'est le mécanisme le plus proche de « pont vrai », et le plus coûteux en entrée.

**Grille qualité-diversité domaine × opérateur.** Source : Mouret & Clune, 2015, « Illuminating search spaces by mapping elites » (référence à vérifier ; aucun identifiant donné). Chaque cellule (domaine, opérateur) garde son meilleur élément ; le tirage est une stratification. Remarque décisive : **c'est précisément le nul « tirage stratifié » de la question**. Si E1 donne H_B, le nul *est* le mécanisme de la v0, et la grille apporte en plus l'archive (une case par cellule, remplissage mesurable).

Mélange conceptuel (Fauconnier & Turner, 2002, *The Way We Think*) et recherche de nouveauté (Lehman & Stanley, 2011, « Abandoning Objectives: Evolution through the Search for Novelty Alone », *Evolutionary Computation*) : le premier n'a pas de critère mécanique de pont (C2 l'a noté : « somme amalgamée » décorative) ; la seconde optimise l'éloignement, qui est le symptôme même de la chimère. Verdict : HYPOTHÈSE que l'appariement structurel produise le plus de ponts vrais ; E5 tranche contre Swanson, E1 contre la grille.

---

## (c) Instruments : mesure minimale de fonctionnement

| Instrument | Détection | Fausse alerte | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| **Extracteur d'opérateurs** (entrée de tout le reste) | rappel par opérateur sur 100 résumés étiquetés à la main (4 h humaines, illustratif) | taux d'opérateurs « hub » génériques attribués (*matrix*, *bound*) | résumés appariés en longueur et en champ, moitié avec opérateur réel, moitié avec mention incidente | la liste de 25 motifs regex de la caste 1 (C1) ; à battre d'au moins 15 points de F1, illustratif |
| **Noyau corrigé / stratification** | bisoc vrai contre vérité plantée (E1, E2) | paires forcées sur homonyme ou sur domaines réellement identiques mais mal étiquetés | corpus à ε, s, h, n croisés ; étiquettes permutées comme plancher | tirage stratifié + paire forcée (E1) |
| **Filtre de compatibilité** | rappel sur paires contradictoires (C3b réaliste : 0,608, RAPPORTÉ) | rejets à tort sur paires compatibles (5,1 %, RAPPORTÉ) | paires même opérateur, même longueur, une contradictoire sur un seul axe, une non ; paraphrases et mentions négatives dans les deux | rejet aléatoire au même taux (plancher) ; cible v0 : rappel ≥ 0,80 à ≤ 5 % de rejets à tort (illustratif) ; le lexique d'évaluation doit être écrit par un autre agent que celui du filtre (C3b §5) |
| **Fuseur (modèle de langue)** | taux de filles « plus que les parents et correctes » sur mondes plantés (E3) | taux de chimères ; taux de ponts « détectés » sur parents sans isomorphisme (≤ α) | mêmes parents, consigne à prédiction obligatoire contre gabarit ; parents permutés | gabarit de juxtaposition + unification mécanique sur le monde planté |
| **Critère « prédit plus »** | sur mondes plantés : instances nouvelles correctes | filles classées « nouvelles » dont la prédiction est entraînée par un parent seul (vérifiable par unification) | filles vraies / juxtapositions déguisées (conjonctions reformulées) | comparaison d'ensembles d'instances, zéro appel de modèle |
| **Mondes plantés** (si C4 est rendue, à auditer ainsi) | un vérificateur mécanique retrouve 100 % des isomorphismes plantés | un classifieur à recouvrement lexical seul ne doit pas dépasser α + 10 points (illustratif) : sinon le monde récompense les jetons, pas la structure | mondes avec/sans pont, même vocabulaire de fond | recouvrement lexical, TF-IDF |
| **Rétrodiction** | Hit@10 positives (E4) | Hit@10 sur jumelles restées disjointes ; Hit@10 à t₀ − 10 ans | positives et jumelles appariées en taille et croissance | nul stratifié ; sonde de fuite par interrogation à froid |

Deux remarques d'attaque. Le filtre tel qu'évalué dans C3b a été conçu et jugé par le même agent, avec le même lexique : sa précision 1,000 en régime propre ne dit rien ; seule la ligne « réaliste » est informative, et elle le classe comme réducteur partiel. Le fuseur est l'instrument sans aucune mesure dans les pièces : toute la valeur revendiquée (« la fille prédit plus ») repose sur lui.

---

## (d) Ancrage matériel

- **Mondes plantés, E1, E2, E5, critère mécanique** : processeur seul, Python ; C3a rapporte 0 $ pour la génération 0 (RAPPORTÉ). Estimation : < 1 h de calcul par grille (illustratif).
- **Fuseur ouvert pour E3** : un modèle ouvert de 7 à 8 milliards de paramètres (familles Mistral, Llama ou Qwen, versions à vérifier au moment du run) sur un seul GPU grand public ; ~2 000 fusions × ~1 500 jetons ≈ 3 millions de jetons, soit quelques heures (illustratif). Par API : 5–15 USD (illustratif). Le gabarit de juxtaposition coûte 0.
- **E4** : OpenAlex, API gratuite ; 100 paires × 3 fenêtres temporelles, extraction sur processeur ; fusion limitée aux 100 paires retenues (< 1 USD, illustratif). Contrainte dure : coupe d'entraînement du fuseur < t₀, sinon on n'utilise le modèle que *après* appariement mécanique, et la sonde de fuite exclut les paires connues.
- **Étiquetage humain** : 100 résumés pour l'extracteur, 4 h (illustratif), seul coût non automatisable.
- **Total** : < 20 USD et 2–3 jours (illustratif), compatible avec l'enveloppe de la première expérience de R-525.

---

## Q5 — Recommandation pour la version 0, et ce qui me ferait changer d'avis

**Forme à retenir** : (1) grille domaine × opérateur alimentée par un extracteur *mesuré* ((c), ligne 1) ; (2) tirage **stratifié** par cellule, paire d'opérateur forcée après tirage — pas de noyau déterminantal, pas de Jacobi, pas de Sinkhorn ; (3) filtre de compatibilité minimal en premier étage, déclaré « réducteur » et non « garantie », avec son lexique d'évaluation écrit par un autre agent ; (4) fusion sous consigne à prédiction obligatoire, suivie du **rejet mécanique des juxtapositions** par comparaison d'ensembles d'instances ; (5) rétrodiction uniquement avec appariement mécanique et sonde de fuite.

**Pourquoi** : tout ce qui, dans la forme corrigée, est établi au sens de C3b (diversité de domaine, paire garantie) est obtenu *par construction* par (2) ; ce qui reste au noyau est une hypothèse non testée (a)1. La v0 doit porter le moins de mécanismes non mesurés possible, parce que l'étage amont (sélection) n'est lui-même pas validé (a)6.

**Ce qui me ferait changer d'avis** : E1 à H_A (le noyau bat la stratification de ≥ 0,02 sur bisoc vrai ou sur le taux de filles correctes) → réintroduire le noyau sur S seul, γ fixé, sans Sinkhorn sur L (A7, RAPPORTÉ). E3 à H_B → retirer le modèle de langue de la fusion en v0 et ne garder que le gabarit + unification. E5 à H_B → remplacer l'appariement par opérateur par un A–B–C de Swanson avec filtre d'homonymie. E4 à H_B après E1/E3 à H_A → l'écart réel/synthétique n'est pas comblé ; suspendre la recombinaison jusqu'à un banc de rétrodiction corrigé.

**Ce que je ne sais pas** : si C4 existe et contient déjà E1 ou E3, mes seuils doivent être réalignés sur les siens avant tout run ; et je n'ai pas de mesure de la ligne de base v6.2.1 réelle, que personne n'a courue.

FIN-DE-CELLULE