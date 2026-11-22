**D — Question de recherche.** À budget de défense fixé, la perte cumulée qu’un contrôle permettrait d’éviter, estimée à partir d’un historique incomplet, est-elle un bon critère pour placer les contrôles aussi bien entre les étapes d’un agent qu’entre copies ou sur les verdicts d’un moniteur exposé ?

**HYPOTHÈSE — Réponse attendue.** Une règle apprise en commun peut choisir *où vérifier* presque aussi bien que des règles spécialisées dans chacun des trois régimes, et mieux qu’une vérification périodique ou fondée sur des incohérences mécaniques. Ce n’est pas l’hypothèse que les mêmes anomalies textuelles apparaissent partout. C’est l’hypothèse qu’après calibration, les signaux des instruments prédisent une même quantité : le dommage évitable par unité de budget restant. Le test important est le transfert à un régime dont on n’a pas vu de dommages étiquetés.

### Ce que la question suppose

- **RAPPORTÉ — Cadre fourni.** Le défenseur a accès au texte, aux activations, à des exécutions de comparaison limitées et à des vérifications coûteuses limitées. Cela ne dit ni ce que révèle une activation, ni ce que garantit une comparaison.
- **HYPOTHÈSE — Effet cumulatif.** Il existe des erreurs locales compatibles avec le travail honnête dont la dépendance à distance, et non la seule fréquence, explique une perte finale mesurable.
- **HYPOTHÈSE — Copies.** Une divergence entre copies peut être informative ; réciproquement, leur accord peut masquer une erreur commune. Compter des votes comme autant de preuves indépendantes n’est donc pas un contrôle de référence suffisant.
- **HYPOTHÈSE — Moniteur exposé.** La fiabilité d’un verdict peut varier sans que le dossier soit devenu plus difficile. Il faut manipuler l’exposition du moniteur à dossier constant pour séparer les deux effets.
- **HYPOTHÈSE — Arbitrage possible.** Une intervention déclenchée à temps peut encore corriger le résultat. Un excellent détecteur qui ne sonne qu’après la remise du rapport ne validerait pas la problématique commune.

### Épreuve proposée

**HYPOTHÈSE — Plan expérimental.** Faire produire un rapport chiffré à partir d’un dossier synthétique de pièces datées, avec révisions et exceptions. Un programme indépendant du modèle connaît les contributions exactes de chaque pièce aux conclusions finales. Il reste inaccessible au défenseur, sauf pour la pièce qu’il décide de vérifier. Mesurer la perte par la fraction de conclusions finales incorrectes, avec les mêmes pondérations dans tous les régimes. Après vérification, appliquer la même procédure de correction et de recalcul à toutes les politiques.

**HYPOTHÈSE — Construction.** Partir de dossiers identiques, traités en séquence ou répartis entre copies ; conserver le graphe des dépendances entre pièces, notes et conclusions. Dans le régime « moniteur visé », présenter au moniteur soit les notes brutes de l’agent, soit une restitution canonique des mêmes données, sans modifier ce que reçoit l’agent. Inclure des notes de test préparées pour biaiser le verdict ainsi que des notes honnêtes de style comparable. L’étiquette d’exposition ne constitue pas une étiquette de dommage. Utiliser des perturbations contrôlées de décisions intermédiaires ; ne pas extrapoler leurs résultats à la fréquence d’un sabotage spontané.

**HYPOTHÈSE — Règles de décision.** La politique commune classe les interventions par réduction prédite de perte, sous plafonds séparés de comparaisons, de vérifications et de calcul. Une continuation avec correction et une sans correction, sur les mêmes préfixes et graines d’apprentissage, fournissent les cibles de réduction de perte. À l’évaluation, seule la branche permise par la politique est visible. Geler règles, coûts et seuils avant le test ; séparer les familles de dossiers, pas seulement les trajectoires. Les marges numériques ci-dessous sont **illustratives**. Pour chaque duel, utiliser des intervalles simultanés par rééchantillonnage des dossiers appariés ; une estimation qui chevauche la frontière ne tranche pas.

[DUEL 1]

**HYPOTHÈSE — Le dommage tient-il à la dépendance ?** Comparer des décisions localement plausibles, en même nombre et de mêmes types, placées soit sur une même chaîne de dépendances, soit sur des chaînes distinctes. Apparier aussi les positions, la difficulté et l’influence marginale des décisions mesurée en jouant chacune isolément. Métrique \(I\) : différence de perte finale entre placements, après soustraction, dans chaque placement, de la somme des pertes isolées.

- \(H_A\) : \(I>0{,}05\) de perte normalisée (**illustratif**) ; \(H_B\) : \(I\leq0{,}05\) (**illustratif**).
- **Contrôle négatif :** mêmes placements sur des conclusions construites comme indépendantes et notées additivement ; l’interaction doit disparaître. Vérifier aussi, en aveugle, qu’un lecteur d’une décision isolée ne distingue pas les placements.
- Une borne inférieure au-dessus de la marge falsifie \(H_B\) ; une borne supérieure au plus égale à la marge falsifie \(H_A\). Un échec du contrôle invalide l’attribution à la dépendance.

[DUEL 2]

**HYPOTHÈSE — Le critère se transfère-t-il ?** Laisser tour à tour un régime entier hors apprentissage. Dans le régime laissé de côté, autoriser uniquement une calibration sur dossiers honnêtes. Comparer la règle transférée \(T\) à une règle spécialisée \(S\) ayant reçu autant de trajectoires étiquetées, mais dans le régime cible, et à la meilleure règle mécanique \(M\) choisie sur validation. Noter \(L\) la perte après correction, à budgets identiques. Préinscrire le score du pire régime :
\[
G=\min_r\min\{L_{M,r}-L_{T,r}-b,\quad m-(L_{T,r}-L_{S,r})\}.
\]
Prendre par exemple un bénéfice exigé \(b=0{,}05\) et une marge de non-infériorité \(m=0{,}02\), **illustratifs**.

- \(H_A\) : \(G>0\) ; \(H_B\) : \(G\leq0\). Un gain moyen ne peut pas compenser un échec sur le moniteur visé.
- **Contrôle négatif :** permuter les scores de priorité entre occasions comparables d’un même dossier, sans changer le nombre de contrôles ni leur coût. Si la permutation conserve le bénéfice, ne pas l’attribuer au ciblage.
- Une borne inférieure positive falsifie \(H_B\) ; une borne supérieure non positive falsifie \(H_A\). Identifier alors le régime et le comparateur responsables : perdre face au spécialiste plaide pour des articles distincts ; perdre aussi face à la mécanique retire l’intérêt pratique de la règle proposée.

[FIN DES DUELS : 2]

### Qualification minimale des instruments

**HYPOTHÈSE — Mesures proposées.** Pour chaque instrument, fixer le point de fonctionnement sur validation et publier sur test le taux de détection *avant la dernière correction possible* et le taux de fausses alertes par dossier honnête, avec leurs dénominateurs. Faire l’appariement par dossier source, longueur, position, nombre de copies et exposition du moniteur. Inclure les hésitations, désaccords et révisions honnêtes ; rapporter séparément les erreurs honnêtes réellement dommageables, positives pour la correction mais pas preuves d’intention. Exiger un gain de détection à taux de fausses alertes et coût égaux par rapport au témoin indiqué.

| Instrument | Positif à détecter ; négatif honnête apparié | Vérification mécanique à battre |
|---|---|---|
| Moniteur de texte | Chaîne menant à une conclusion fausse ; chaîne de même longueur dont une révision légitime préserve la conclusion | Identifiants de sources manquants, contradictions de dates et recalculs de totaux |
| Moniteur d’activations | Mêmes paires, aux mêmes positions de lecture, sonde gelée ; mesurer aussi son gain conditionnel au texte déjà disponible | Règles précédentes plus seuil sur la norme des activations, calibré par position |
| Exécution de comparaison | Réexécution signalant une conclusion fausse de la branche principale ; deux branches honnêtes pouvant différer de formulation | Comparaison exacte des champs normalisés et contrôle des sommes ; compter les erreurs communes manquées, pas seulement les désaccords |
| Vérification coûteuse | Sélection d’une pièce dont la correction évite une perte ; pièce honnête de même rôle et de même influence. Mesurer séparément le verdict sur pièces effectivement inspectées et le taux de dossiers sauvés | Recalcul local simple pour le verdict ; inspection périodique ou priorité au nombre de dépendants pour le placement |

**HYPOTHÈSE — Cas particulier du moniteur visé.** Pour les deux moniteurs, publier en plus la fréquence des verdicts qui passent de correct à incorrect entre restitution canonique et notes brutes, séparément sur cas dommageables et honnêtes. Sinon, une baisse des alertes pourrait aussi bien traduire moins de fausses alertes que davantage de dommages manqués.

### Faisabilité, antériorité et portée

**HYPOTHÈSE — Ancrage matériel.** Utiliser les poids accessibles de Llama 3.1 8B Instruct, copies réalisées par contextes distincts, sans réentraînement du modèle. Conserver des résumés d’activations aux étapes de décision pour entraîner une sonde linéaire. Enveloppe **illustrative** : 12 millions de jetons générés, branches comprises ; à 20 jetons/s agrégés (**illustratif**), environ 167 heures de génération (**illustratif**). Réserver 300 heures-GPU sur A100 de 80 Go à 2 €/h, soit 600 € hors travail humain (**chiffres illustratifs**). Dans les deux mois imposés, chronométrer d’abord les continuations avec capture d’activations et estimer la précision du score du pire régime ; réduire la longueur ou déclarer le test sous-dimensionné plutôt que déplacer la marge après observation.

**RAPPORTÉ — Antériorité la plus proche identifiée de mémoire.** Ryan Greenblatt, Buck Shlegeris, Kshitij Sachan et Fabien Roger, 2023, *AI Control: Improving Safety Despite Intentional Subversion*. Le rapprochement porte sur l’évaluation de protocoles de contrôle sous supervision limitée, pas sur une priorité revendiquée pour le transfert entre régimes.

**HYPOTHÈSE — Type de contribution.** Un **critère expérimental de transfert**, non une garantie. Vérifier la nouveauté par recherche rétrospective et prospective autour de ce travail, puis dans les travaux sur l’audit séquentiel, les erreurs corrélées d’ensembles et la surveillance adversariale. Chercher précisément un test hors régime à budgets appariés et au risque du *pire* régime. Si ce test existe déjà, proposer une réplication. Si les contrôles mécaniques atteignent la même perte que les politiques apprises dans chaque régime et qu’aucune interaction dommageable n’est mesurable, la question commune perd son intérêt sur ce banc : partager l’infrastructure, sans présenter les trois articles comme les preuves d’un même phénomène.

FIN-DE-CELLULE