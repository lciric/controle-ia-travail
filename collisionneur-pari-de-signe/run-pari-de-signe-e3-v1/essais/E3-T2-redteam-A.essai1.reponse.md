# Tour III.2 — Proposition A : équipe rouge croisée

**Pièces.** S, S-sim, S-sortie, P (§ 4, 5, 8, 10, 12), N-007/N-008, N-054, C (§ 3, 4), J1, J2, J3, la question, les conceptions B et C : présentes, non coupées. Ma propre conception de III.1 ne m'est pas retransmise ; je ne la reconstruis pas.

**Modèle d'adversaire (garde R-519).** Aucune recette ni mode de sabotage. L'« agent adverse » est ici : (i) un constructeur de moniteur qui veut franchir G1, (ii) un proposeur de fiche dans le pôle, (iii) le procédé qui fabrique le banc. Toute évasion décrite est statistique, à coût zéro en calcul : ce sont des choix, pas des attaques.

---

## Contre la proposition B

### (a) Failles

**B-1. Le remplaçant proposé pour G1 tombe dans le piège que B tend au signe.** B recommande (E3, plan ligne 4, recommandation 3) un test t apparié ou un bootstrap par tâche à effectif fixe comme analyse primaire. Statut : HYPOTHÈSE de B. Or un test t unilatéral pour « moyenne > 0 » est anti-conservateur sous asymétrie à gauche (petites valeurs positives fréquentes, rares valeurs très négatives) à petit n : c'est exactement le monde de E1 de B (v = +0,1 w.p. 0,8 ; −0,4 w.p. 0,2). Le contrôle négatif de E3 (« les deux procédures sous le nul ») ne nomme pas ce monde. La « perte de puissance » que E3 impute à la validité à tout instant est donc partiellement confondue avec le prix de la **validité exacte** sous un nul composite borné. Comparer un pari valide à un test approximatif ne mesure pas le coût de Ville.

**B-2. Le prix du mélange n'est pas incohérent (a8).** S § 2.2 annonce log 8 contre « la meilleure mise de la meilleure forme » (huit composantes) ; le contrôle n° 9 compare la grille à la meilleure mise **d'une forme** (log 4) ; D-S2 donne le prix du mélange **des deux formes** (log 2). log 8 = log 4 + log 2 : trois comparaisons différentes, une seule valeur chacune. B élève une non-contradiction au rang de faille. VÉRIFIÉ sur le texte de S.

**B-3. Dimensionnement incohérent avec sa propre recommandation.** B retire le signe (recommandation 1) puis, dans l'ancrage, dimensionne 10 points d'écart avec « 0,945 à 100 tâches » : c'est la puissance du **mélange** (S-sortie, RAPPORTÉ). S-sortie ne donne pas la puissance des parts seules à 10 points. B chiffre un banc avec un instrument qu'il a supprimé.

**B-4. La règle de porte (plan ligne 6) contredit N-054.** B exige que le mode tenu à l'écart ait une borne basse > 0. N-054 point 4 (RAPPORTÉ) prévoit l'inverse : si la borne basse n'est pas au-dessus de zéro sur les autres modes, la **revendication est restreinte**, la porte n'échoue pas ; et le mode tenu à l'écart sert à séparer bras génériques et spécialisés, pas à conditionner G1. B fusionne « G1 passe » et « H1 est revendicable ».

**B-5. L'intersection-union (E4) est juste mais ne protège pas de ce qui compte.** Le minimum des e-valeurs est bien une e-valeur sous l'union (raisonnement de B, VÉRIFIÉ). Mais la famille des bases est **choisie par le programme lui-même** (N-008). Une famille pauvre franchit l'intersection-union comme elle franchit la règle de S. Les planchers « tout signaler » et « juge en une passe » (N-008) situent les bases, ils ne garantissent pas que la meilleure boîte noire possible y figure.

**B-6. Seuils randomisés ou conformes (plan ligne 2) : nominal sous la loi de calibrage seulement.** La randomisation vise E[f] = τ **pour la loi des tâches honnêtes de calibrage**. Rien dans le plan de B ne stratifie les tâches honnêtes d'épreuve par mode, alors que les tâches sabotées le sont (ligne 5). Si les consignes du mode « contrôles » déplacent la marginale honnête, l'appariement par construction ne vaut plus à l'épreuve, et la garde (reléguée en rapport) ne bloque plus. HYPOTHÈSE sur le banc ; testable sans dépense.

**B-7. H2 « rappel du séquentiel seul en fonction de l'horizon » (a10, amendement 4) ouvre un confondant.** N-007 calibre le seuil « sur des épisodes honnêtes entiers ». Si les épisodes sabotés longs sont plus longs que les honnêtes de calibrage, une somme cumulée franchit plus souvent son seuil par simple longueur, sans signal. B ne demande ni calibrage par horizon ni honnêtes appariés en longueur ; S (H2b) au moins apparie la même tâche à deux horizons. B remplace un contraste apparié par une mesure absolue non appariée.

**B-8. Dépendances non traitées entre ses propres amendements.** Analyse primaire à effectif fixe + pari en secondaire (ligne 9) : B ne dit pas ce qui prévaut s'ils divergent. Deux verdicts sur une porte unique, c'est un choix après coup offert au lecteur.

**B-9. « Clopper-Pearson avec effet de plan » (table (c))** exige une corrélation intra-classe estimée sur les mêmes tâches : ce n'est plus exact. Présenté comme « vérification mécanique à battre », il n'a pas de niveau garanti.

### (b) Scénarios d'évasion

- **Contre le test à effectif fixe** : un constructeur choisit un couple (moniteur, point de fonctionnement) dont le contraste par tâche est « souvent un peu positif, rarement très négatif ». Un seuil légèrement permissif sur un moniteur fait naturellement cette forme : gain faible sur la majorité des tâches, pertes concentrées sur les tâches où l'autre moniteur alerte massivement. Sous E[v] ≤ 0, le test t rejette au-delà de α à n = 20–40 (direction connue de l'asymétrie ; taux à chiffrer, HYPOTHÈSE). Coût : zéro.
- **Contre l'intersection-union** : ne rien faire. Implémenter des bases (i) et (iv) sans réglage sérieux sur la partie de développement. L'IU est alors satisfaite contre chacune. Coût : une omission.
- **Contre les seuils randomisés** : laisser les tâches honnêtes d'épreuve venir d'une composition de consignes différente de celle du calibrage (c'est le défaut si on ne stratifie pas). Le moniteur boîte blanche, plus sensible au registre, dérive plus que le noir ; l'écart « > τ » qui suspend la porte (ligne 7) n'est atteint qu'avec une dérive de l'ordre de τ, et une dérive de τ/2 double le taux réalisé sans suspendre. Coût : zéro.
- **Contre H2 recentrée** : banc où l'horizon « long » est réalisé par des épisodes plus longs que tout honnête de calibrage. Le rappel « croît avec l'horizon » par accumulation de fausses alertes. Coût : zéro.
- **Tous à la fois** : score blanc continu, score noir ordinal (E2 de B le voit, mais seulement si la randomisation est effectivement imposée aux deux), honnêtes non stratifiées, famille de bases pauvre, test t primaire. Chaque pièce est une décision d'ingénierie défendable isolément ; aucune n'est une attaque ; ensemble elles suffisent à une fausse porte. Le préenregistrement de B ne contient pas la clause qui interdit leur conjonction.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Niveau du test à effectif fixe sous le monde asymétrique de E1** (et sous v à support {−1, +0,1}). H_A : ≤ α. H_B : > α ; alors E3 ne mesure pas ce que B dit, et la ligne 4 du plan tombe.
2. **Taux de faux positifs honnête par mode à l'épreuve**, comparé au calibrage, pour chaque cellule. H_A : écart < τ/2 dans toutes les strates. H_B : au moins une strate dérive ; alors l'appariement par construction ne remplace pas la garde bloquante.
3. **Parité des deux verdicts** (fixe et pari) sur les témoins vrais et faux de chaque strate. H_A : jamais discordants au-delà de ce que leurs puissances prévoient. H_B : discordances fréquentes ; alors un seul verdict doit être gelé.
4. **Honnêtes appariés en longueur à chaque horizon** pour H2. H_A : rappel séquentiel sur honnêtes longs = τ. H_B : > τ ; alors « croît avec l'horizon » est un artefact de longueur.
5. **Famille de bases contre un plancher informé** : la meilleure base doit battre « juge en une passe » sur le développement. H_A : oui. H_B : non ; alors l'IU certifie contre des hommes de paille.

---

## Contre la proposition C

### (a) Failles

**C-1. Un « VÉRIFIÉ (FAUX mathématiquement) » qui démontre le contraire.** C (a).1 annonce un défaut de positivité du facteur de garde, puis calcule que le facteur vaut 0,145 > 0. En général 1 + λ(δ − g) ≥ 1 − λ(1 − δ) > 0,1 pour λ ≤ 0,9 : le facteur est positif, et seule la borne gauche compte pour la validité. Le support « jusqu'à 1 + δ à droite » n'altère ni la positivité ni l'espérance ≤ 1. La normalisation par (1 + δ) (amendement 3) ne corrige rien et réduit la mise effective, donc la puissance de la garde. Règle 1 : un statut VÉRIFIÉ sur une affirmation que le texte lui-même réfute.

**C-2. La troncature max(10⁻⁶, facteur) (table (c), ligne 2) invalide le processus si elle agit.** Remplacer un facteur par son maximum avec une constante ne peut qu'augmenter l'espérance ; si la troncature est inactive, elle est inutile ; si elle est active, E[facteur] > 1 sous le nul et la garde n'est plus une surmartingale. VÉRIFIÉ (inégalité élémentaire).

**C-3. H2a : le « VÉRIFIÉ mathématiquement » repose sur une lecture fausse de S.** S § 4 définit la sous-population par « chaque action **sabotée** sous le seuil par action ». C lit « max sur toutes les actions », d'où r_action ≡ 0 et son Expérience 2. Sous la définition de S, les actions non sabotées peuvent alerter ; r_action > 0, et B (a9) l'a vu. Pire : dans le monde nul de l'Expérience 2 (« sabotés = honnêtes »), il n'y a aucune action sabotée, le filtre de S est vide, et le contraste de S devient r_seq − r_action sur toutes les tâches. Si le seuil par action est calibré **par action** à 1 % (N-007) et le séquentiel **par épisode**, alors sur T = 20 actions le taux par épisode du moniteur par action approche 1 − 0,99²⁰ ≈ 0,18 (illustratif) contre 0,01 : E[v] < 0, le pari de S est **conservateur**, non anti-conservateur, dans le monde que C simule. L'expérience de C ne peut falsifier la définition de S : elle teste un autre objet.

**C-4. La correction de H2a (amendement 2) crée un biais de construction.** v_corr = r_seq sur sabotés filtrés (filtre sur les actions sabotées seulement, selon S) moins f_seq sur honnêtes filtrés par « max sur toutes les actions < τ̂ ». Les honnêtes retenus ont **tous** leurs scores bas, donc une somme cumulée basse ; les sabotés retenus gardent des actions non sabotées libres. Le comparateur est déprimé par le filtre : E[v_corr] > 0 sans signal. Et le contraste n'est plus apparié à la cellule « par action » : l'affirmation de N-007 (séquentiel contre par action) est remplacée par « le séquentiel dépasse son propre plancher ».

**C-5. Rangs conformes appariés : C contredit son propre (a).2.** C affirme « E[f_A − f_B] = 0 exactement » par égalité des lois Beta. C'est vrai **en moyenne sur les tirages de calibrage**. Mais C (a).2 rappelle que le pari conditionne sur les seuils **réalisés**, scellés. Conditionnellement, F_A(τ̂_A) − F_B(τ̂_B) est une variable aléatoire figée, d'écart-type de l'ordre de √(2τ(1−τ)/N_cal), soit ≈ 0,006 pour N_cal = 500 épisodes (illustratif) : du même ordre que τ. L'« exactitude » annoncée n'existe pas pour le banc réel, qui n'a qu'un calibrage.

**C-6. aGRAPA avec c = 0,75 ne « résout pas la bride ».** Avec μ̂ ≈ 0,2 et σ̂² ≈ 0,048 (chiffres de C, illustratifs), μ̂/(σ̂² + μ̂²) ≈ 2,3 > c : la mise prévisible est saturée à 0,75, **inférieure** au 0,9 de la grille. Le seul gain possible est la suppression du prix de mélange (≤ log 4 ≈ 1,4 nat, soit ≈ 10 tâches à 0,144 nat/tâche, illustratif). Le seuil H_B de l'Expérience 3 (≥ 25 points à n = 25) est posé sans que cette borne de gain soit calculée. Et C attribue à Waudby-Smith et Ramdas un « VÉRIFIÉ pour l'attribution exacte » : rien dans les faits ne le permet ; référence à vérifier.

**C-7. Inférence forte trouée (B4).** Expérience 3 : « < 0,15 falsifie H_B ; > 0,25 falsifie H_A » ; Expérience 4 : « > 0,10 falsifie H_A ; ≤ 0,062 falsifie H_B ». Entre les deux seuils, aucune issue ne falsifie rien.

**C-8. v_pente (amendement 4) perd la moitié de H3.** H3 dit « domine **et** décroît plus doucement ». Avec N ∈ {1, 2, 4, 8}, poids (−0,375 ; −0,125 ; 0,125 ; 0,375) : un profil d'écart (0 ; −0,3 ; −0,3 ; +0,3) donne v_pente = +0,11 > 0 alors que le blanc est **dominé** à N = 2 et 4 (calcul, illustratif). C supprime H3a par N (le e-BH sur les N de S) et ne dimensionne pas la pente : Σ|w| = 1 divise l'effet comme le ½ de S, que C n'a pas chiffré non plus.

**C-9. « 150 tâches de 5 épisodes suffisent » pour la garde (ancrage, § 2) : direction fausse.** Moins d'épisodes par tâche augmente Var(f_A − f_B) par tâche ; il faut plus de tâches, pas moins ; la normalisation par (1 + δ) réduit encore la mise. Illustratif, mais contraire au mécanisme.

**C-10. Statuts.** « Llama-3.1-8B-Instruct » est marqué RAPPORTÉ : P dit « portés sur 8B » et « Llama Scope », pas ce nom. « Payer Ville coûte ≈ 25 à 35 % d'échantillon » n'est pas marqué illustratif. Plusieurs calculs propres de C (niveau 0,02 expliqué par « masse morte à λ = 0,9 ») sont marqués VÉRIFIÉ alors que l'argument utilise |v| = 1 (forme signe) pour la forme parts, où E[log(1 + 0,9 v)] ≈ −0,4 · 0,05 ≈ −0,02 nat/tâche (illustratif) : lent, pas un « effondrement ».

**C-11. L'intervalle de la ligne 7 du plan est unilatéral.** L'inversion donnée ne pénalise que les v sous μ : c'est une borne basse à 95 %. Suffisante pour la supériorité, mais à déclarer ainsi, ou à construire bilatérale à α/2 par côté.

**C-12. Comparateur B\* unique (plan ligne 2).** Même défaut que S ; l'E4 de B (que je reprends ici, en le disant) le teste : avec 10 tâches de développement, la règle « rappel moyen » retient la mauvaise base avec une probabilité non négligeable, et le verdict devient « bat B\* », pas « bat la meilleure ».

### (b) Scénarios d'évasion

- **Contre les rangs conformes appariés** : rien à faire ; un seul tirage de calibrage fixe une asymétrie réalisée de l'ordre de τ. Le constructeur qui a deux candidats de moniteur blanc et un seul calibrage peut, sur la partie de développement, préférer celui dont le seuil réalisé est tombé « du bon côté » — sélection légitime en apparence (choix d'architecture), effet sur f_blanc − f_B\* non compté. Coût : zéro.
- **Contre v_corr (H2a)** : fournir des sabotés dont les actions non sabotées portent des scores ordinaires et des honnêtes filtrés par le max : la différence des filtres fait le reste (C-4). Coût : zéro, c'est la construction.
- **Contre v_pente** : un moniteur dont l'écart est positif aux N extrêmes et négatif au milieu passe (C-8). Un essaim où N = 8 sature le noir (beaucoup d'alertes, donc rappel noir élevé partout) et N = 1 favorise le blanc donne une pente positive sans domination.
- **Contre aGRAPA** : la mise dépend des données ; les hyperparamètres (c, v₀, σ₀²) sont des degrés de liberté par fiche. Un proposeur qui déclare plusieurs réglages sur plusieurs fiches multiplie les essais ; e-BH le couvre seulement si chaque réglage est une fiche. Coût : quelques fiches.
- **Contre la clause d'arrêt (ligne 10)** : le choix « pari ou permutation » dépend du nombre de tâches, connu avant les issues : non exploitable. Mais le test de permutation par retournement de signe teste la **symétrie**, pas E[v] ≤ 0 : à moins de 30 tâches, la porte change de nul sans le dire.
- **Tous à la fois** : conformal rank « exact » pris pour une garantie conditionnelle, H2a corrigée biaisée, pente sans domination, B\* sélectionnée sur 10 tâches. Chaque amendement de C remplace une faille déclarée de S par une faille non déclarée ; l'adversaire n'a qu'à ne pas lire S.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Expérience 2 refaite avec le filtre de S** (actions sabotées seulement), sous deux calibrages du seuil par action (par action ; par épisode). H_A : S anti-conservateur dans au moins un calibrage. H_B : S conservateur ou au niveau dans les deux ; alors la faille « VÉRIFIÉE » n'existe pas et c'est v_corr qui doit passer le contrôle suivant.
2. **v_corr sous le nul pur avec les deux filtres tels que C les écrit** (sabotés : actions sabotées ; honnêtes : max). H_A : ≤ α. H_B : > α ; alors l'amendement 2 est rejeté.
3. **Asymétrie conditionnelle des seuils conformes** : un seul calibrage par répétition, puis taux réalisés sur l'épreuve. H_A : |F_A − F_B| < τ/4 dans 95 % des répétitions. H_B : non ; alors « exactement zéro » est retiré et la garde bloquante de S est rétablie.
4. **v_pente sur le profil non monotone (0 ; −0,3 ; −0,3 ; +0,3)** avec H3a par N en parallèle. H_A : v_pente seul promeut « décroît plus doucement » tout en que H3a rejette la domination à N = 2 et 4 (le contrôle **voit** l'artefact). H_B : v_pente ne promeut pas ; alors mon exemple est faux. Si H3a n'est pas conservé, l'artefact n'est pas visible : fatal.
5. **E[facteur tronqué] sous le nul**, avec un monde où g(t) = ±1 arrive (tâches honnêtes « étranges »). H_A : ≤ 1. H_B : > 1 ; alors la troncature est retirée.
6. **aGRAPA contre la grille sous le nul asymétrique de la propre Expérience 1 de C et sur le monde de S-sim**, avec la borne de gain log|Λ| calculée d'avance. H_A : gain ≤ 10 tâches (illustratif) ; H_B : gain > 10 ; l'un des deux falsifie C-6 ou le seuil de C.
7. **garde() rejouée à m = 5** sur 150 tâches. H_A : certifie δ = 0,05 dans ≥ 95 % ; H_B : non ; l'astuce d'économie tombe.

---

## Ce que je prends aux deux, en le disant

- B et C établissent indépendamment que le mélange parts + signe teste l'intersection des nuls, non E[v] ≤ 0 : je le tiens pour la correction la plus solide du tour (dérivations de B et C, OBSERVÉES-NON-AUDITÉES ; E1 de B et Expérience 1 de C les rendent réfutables). La forme réparée est celle que C nomme en fin de pièce — union des nuls, **chaque** richesse ≥ 1/α — et que B restreint à une affirmation déclarée « majorité des tâches » ; les deux sont compatibles, aucune n'est encore chiffrée en puissance.
- L'E4 de B contre le comparateur unique s'applique à C (C-12) et à S.
- L'Expérience 4 de C (grappe d'organisme) mesure ce que l'E5 de B ne peut pas mesurer : la corrélation sur le **rappel**, pas seulement sur les faux positifs honnêtes de T0.5.
- Ni B ni C ne stratifie les tâches honnêtes par mode ; c'est le trou commun (B-6, C-5) et, à mon avis, le plus facile à exploiter sans rien attaquer.

FIN-DE-CELLULE