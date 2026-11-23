### 1. Recommandation : l'option (b)

Je recommande l'**option (b)** : étendre la règle « taille d'échantillon insuffisante » aux trois tests restants, avec un plancher fixé à la moitié de la taille prévue pour les tests sur actions (**64** pour « Contrôles d'une autre tâche », **32** pour « Texte sans rapport ») et un plancher préenregistré de plans utilisables pour « Plan tronqué ».

Ce choix pèse les cinq critères suivants :

- **Risque de réussite par hasard sur petit échantillon.** Un faible effectif dégrade la fiabilité dans les deux sens, mais avant une mesure décisive, le danger majeur est de valider à tort un instrument défaillant. Sans plancher (option a), sur 3 ou 4 actions, un lecteur aléatoire ($p = 0{,}5$) obtient 100 % de bonnes réponses dans 12,5 % ou 6,25 % des cas. Les planchers de 64 et 32 bornent l'erreur-type maximale d'une proportion ($1 / [2\sqrt{n}]$) à 6,25 et 8,8 points de pourcentage, écartant pratiquement une réussite fortuite face à un seuil exigeant. L'aléa est encore plus grave pour la corrélation de Spearman sur « Plan tronqué » (section 2).
- **Cohérence avec les autres tests.** La règle « taille d'échantillon insuffisante » gouvernant déjà la majorité des tests, en exempter trois — dont un test de corrélation très vulnérable aux faibles effectifs — créerait une incohérence difficile à défendre. L'option (c) rompt aussi cette cohérence en remplaçant des planchers par test déjà arrêtés par un seuil global plus grossier, susceptible de faire échouer des tests suffisamment fournis sans couvrir « Plan tronqué ».
- **Risque de perdre la validation sur un événement rare en amont.** Ce risque existe sous (b), mais il est sain : si le vivier d'actions honnêtes et jugeables ne permet pas une validation fiable, déclencher la procédure de révision bornée vaut mieux qu'engager la mesure décisive. En outre, un déficit sévère sous 64 ou 32 actions fera souvent déjà échouer d'autres tests. Enfin, l'option (a) n'élimine pas ce risque : elle remplace un échec transparent par une loterie (échec ou succès fortuit) tout en appelant inutilement les lecteurs.
- **Simplicité de la règle écrite.** À l'échelle du protocole complet, l'option (b) est la plus simple : une règle unique, sans exception. L'option (a) instaure deux régimes ; l'option (c) impose malgré tout une règle distincte pour « Plan tronqué ».
- **Seuils fixés avant toute donnée.** Les planchers de 64 et 32 découlent mécaniquement de la convention des 50 %, sans calibrage additionnel. Seul le minimum de « Plan tronqué » doit être fixé a priori, ce que les propriétés exactes de la corrélation de Spearman permettent sans données.

### 2. Minimum de plans utilisables pour « Plan tronqué » selon chaque option

La corrélation de Spearman ($\rho$) étant une statistique de rangs, sa distribution sous indépendance et sa sensibilité (hors ex aequo) ne dépendent que du nombre $n$ de plans utilisables :

- **Option (a) : aucun plancher.** Seule l'existence mathématique de $\rho$ ($n \ge 2$, hors série constante) s'applique. Or, à $n = 2$, $\rho$ vaut uniquement $-1$ ou $+1$ : un instrument aléatoire atteint $\rho = +1$ dans 50 % des cas et passe tout seuil $\le 1$. À $n = 3$, sans ex aequo, $\rho \in \{-1 ; -0{,}5 ; +0{,}5 ; +1\}$ : le hasard donne $\rho \ge 0{,}5$ dans 50 % des cas et $\rho = 1$ dans 16,7 %. À $n = 4$, il atteint encore $\rho \ge 0{,}8$ dans 16,7 % des cas.
- **Option (b) : 12 plans utilisables.** Ce plancher s'appuie sur quatre propriétés exactes de $\rho$ (hors ex aequo) :
  1. *Dispersion sous indépendance* : l'erreur-type exacte, $1/\sqrt{n-1}$, passe de 0,50 à $n = 5$ à 0,30 à $n = 12$.
  2. *Succès par hasard* : la valeur critique unilatérale à 5 % sous indépendance atteint 0,503 ($\approx 0{,}50$) à $n = 12$ ; pour tout seuil $c \ge 0{,}50$, un lecteur sans signal reste sous 5 % de réussite fortuite.
  3. *Influence d'un seul plan aberrant* : déplacer un plan d'un rang extrême à l'autre réduit $\rho$ de $6/(n+1)$. Un seul plan fait chuter $\rho$ de 1,0 à 0,0 à $n = 5$ ; $n = 12$ est le premier entier où cette baisse passe strictement sous 0,50 ($6/13 \approx 0{,}46$).
  4. *Granularité* : le pas minimal entre valeurs distinctes, $12/[n(n^2-1)]$, tombe à 0,007 (contre 0,20 à $n = 4$ et 0,10 à $n = 5$).
  Si le seuil préenregistré $c$ est inférieur à 0,50, il faut relever le plancher au plus petit $n$ dont la valeur critique unilatérale à 5 % est $\le c$ (par exemple $n = 18$ pour $c = 0{,}40$). Même si $c$ est élevé, il ne faut pas descendre sous 12 afin de contenir l'influence d'un plan isolé et le risque d'échec fortuit.
- **Option (c) : aucun plancher natif, obligeant à ajouter le même plancher de 12.** Un seuil global sur les actions honnêtes ne garantit rien sur les plans : 200 actions peuvent former trois longs plans ou 200 plans d'une seule action (tous exclus après troncature). Il faudrait donc malgré tout adjoindre un plancher spécifique de 12 plans utilisables, annulant la simplicité revendiquée par (c).

### 3. Pièges de l'option (b) et formulation recommandée

Trois pièges doivent être verrouillés dans le protocole :

1. **Compter le vivier brut plutôt que les unités utilisables.** Pour « Plan tronqué », le plancher s'évalue *après* exclusion des plans où rien n'est conservé ou retiré. Pour les tests sur actions, un vivier dépassant 64 unités mais concentré dans une seule tâche (ou forçant un recyclage massif des mêmes contrôles externes) ne permet pas de bâtir un test valide : le plancher porte sur les unités effectivement constructibles selon les règles inter-tâches.
2. **Confondre insuffisance d'échantillon et défaillance des lecteurs.** L'issue formelle est identique (échec du critère), mais la distinction oriente la procédure de révision bornée ; une corrélation $\rho$ indéfinie sur au moins 12 plans utilisables (sortie constante d'un lecteur) reste un échec post-exécution, distinct d'un manque de données. Les planchers doivent aussi être déclarés non révisables une fois le vivier observé.
3. **Effet d'ordre sur tirage disjoint.** Si les lots sont tirés sans remise dans un même vivier, l'ordre d'allocation doit être fixé à l'avance pour ne pas affamer arbitrairement un test.

**Formulation proposée :**
> « La règle “taille d'échantillon insuffisante” s'applique à tous les tests de validation, avec des planchers figés avant observation des données : 64 unités constructibles pour “Contrôles d'une autre tâche”, 32 pour “Texte sans rapport” et 12 plans utilisables (après exclusion des plans où rien n'est conservé ou retiré) pour “Plan tronqué”. Chaque plancher est vérifié avant envoi aux lecteurs, après application des règles d'éligibilité, de construction inter-tâches et d'ordre de tirage. En dessous du plancher, le test n'est pas construit, rien n'est envoyé aux lecteurs et le critère échoue avec mention du motif “taille d'échantillon insuffisante”, sans révision possible du plancher. Pour “Plan tronqué”, une corrélation indéfinie sur au moins 12 plans utilisables vaut échec de l'instrument après exécution. »

### 4. Niveau de confiance

**Élevée.** L'avantage de l'option (b) sur (a) et (c) repose sur des arguments statistiques et méthodologiques solides. Seule la valeur exacte du plancher de « Plan tronqué » (12 plans, voire 15 si de nombreux ex aequo sont attendus) garde une marge d'incertitude modérée, faute de connaître le seuil fixe de $\rho$ et la structure attendue des plans.