# Proposition B — Tour III.3 : réponse aux critiques

---

## (a) Réponse critique par critique

Je traite chaque critique adressée à B par les propositions C et D. Numérotation : C-a1…C-a4, C-b1…C-b3, C-c1…C-c2 pour la proposition C ; D-a1…D-a7, D-b (ensemble), D-c (ensemble) pour la proposition D.

---

### Critiques de la proposition C

**C-a1 — Fuite de resubstitution : comparer les scores du jeu externe aux 800 bénins d'entraînement.**

**Acceptée.** C a raison. Dans un espace de dimension $d \gg 800$, la sonde linéaire pousse les scores in-sample vers les marges extrêmes. Le test KS entre les scores in-sample et les scores du jeu externe détectera un décalage artefactuel, pas un vrai shift de distribution. Mon étape 1 (« Extraire les scores sur les 800 bénins d'entraînement — en train, oui ») est une erreur méthodologique directe. **Correction** : la comparaison de distribution doit se faire exclusivement sur des scores hors-échantillon. Voir l'expérience corrigée § (b).

**C-a2 — Fuite de sélection (data snooping) dans l'option C : sélectionner un jeu externe conditionnellement aux 200 bénins Bailey.**

**Acceptée en partie, transformée en test.** Le risque est réel : tester plusieurs jeux candidats contre les mêmes 200 bénins gonfle la probabilité de trouver un jeu « compatible » par hasard. Cependant, la critique suppose que je sélectionne sur la base d'un petit $n$ sans correction. **Correction** : (i) préenregistrer au plus 3 jeux candidats, dans un ordre fixé ; (ii) appliquer une correction de Bonferroni sur les 3 tests ($\alpha_{\text{test}} = 0.01/3 \approx 0.0033$) ; (iii) le premier jeu qui passe est retenu, pas le « meilleur ». Cela borne le snooping. **Test ajouté** : vérifier que la procédure de sélection, appliquée à deux moitiés aléatoires des 200 bénins Bailey, retient le même jeu candidat (contrôle de stabilité de la sélection).

**C-a3 — L'AUC est mal alignée sur le point de fonctionnement à 1 % de fausses alertes.**

**Acceptée.** C et D convergent sur ce point. L'AUC intègre sur tous les seuils ; une sonde peut conserver une AUC élevée tout en ayant un rappel effondré à FPR = 0.01. **Correction** : remplacer l'AUC par le **rappel au point de fonctionnement** (FPR = 0.01, fixé sur un jeu bénin hors-entraînement). Voir Expérience 1 corrigée.

**C-a4 — Normalisation erronée de la stabilité de τ par σ des bénins (Expérience 3).**

**Acceptée.** Ce qui compte n'est pas la dispersion des scores bénins, mais la densité des scores adverses au voisinage de τ. Une fluctuation de 0.1σ_bénin peut être anodine ou catastrophique selon la pente de la courbe de rappel à cet endroit. **Correction** : remplacer la normalisation par σ_bénin par une **mesure directe de la variation du rappel** aux bornes de l'IC bootstrap de τ. Voir Expérience 3 corrigée.

**C-b1 — Le test KS est structurellement aveugle aux événements de probabilité < 5 %.**

**Acceptée.** La démonstration est correcte : avec $n = 200$ et $m = 1\,000$, la valeur critique KS est ~0.126, tandis qu'un shift dans la queue à 1 % produit un écart maximal ≤ 0.05. Le test KS ne peut pas détecter un triplement du taux de fausses alertes concentré dans la queue. **Correction** : abandonner le KS comme test principal. Le remplacer par un **test de permutation sur le quantile 99 %** (déjà mentionné dans ma proposition initiale comme complément, désormais promu en test principal), avec une analyse de puissance explicite. Voir § (b).

**C-b2 — Le bootstrap non paramétrique des quantiles extrêmes est inconsistant pour $n\alpha = 3$.**

**Acceptée.** Avec $n = 300$ et $\alpha = 0.01$, l'estimateur de τ ne repose que sur les 3 plus grandes statistiques d'ordre. Le bootstrap avec remise ne visite que le support discret $\{S_{(1)}, \dots, S_{(300)}\}$ et sa distribution conditionnelle pour les quantiles extrêmes est asymptotiquement inconsistante quand $n\alpha \to \text{constante}$. **Correction** : remplacer le bootstrap par une **bande exacte basée sur la loi Beta des statistiques d'ordre** : $P(U_{(k)} \leq p) = I_p(k, n+1-k)$ où $U_{(k)}$ est la k-ème statistique d'ordre uniforme. Pour le quantile 99 % avec $n = 300$, rapporter directement les seuils $S_{(297)}$, $S_{(298)}$, $S_{(299)}$, $S_{(300)}$ et les probabilités de couverture Beta associées. Plus de bootstrap.

**C-b3 — Sous-puissance de l'Expérience 2 : >45 % de probabilité de rejeter H_A à tort.**

**Acceptée.** Le calcul est correct. Avec τ fixé sur $n = 200$ bénins, le vrai taux suit Beta(2, 199), et $P(\text{Beta}(2,199) < 0.005) \approx 0.26$. Ma région d'acceptation [0.005 ; 0.020] rejette H_A sous H_0 bien plus souvent qu'annoncé. Le duel tel que formulé n'est pas un test valide. **Correction** : (i) élargir la région d'acceptation à l'intervalle Clopper-Pearson de la calibration interne (pas une fenêtre fixe) ; (ii) reformuler comme un **test d'équivalence** avec marge $\delta_p$ dérivée de la variance de calibration, pas imposée a priori. Voir Expérience 2 corrigée.

**C-c1 — Contrôle négatif de surapprentissage (split interne Bailey train vs val+test).**

**Acceptée.** C'est exactement le contrôle qui manquait pour diagnostiquer le problème de C-a1. Ce contrôle doit être exécuté en premier : si les scores de la sonde sur les 200 val+test de Bailey diffèrent significativement (par test de permutation sur le quantile 99 %) des scores sur les 800 d'entraînement, cela quantifie le surapprentissage de la sonde et invalide toute comparaison utilisant les scores in-sample. **Intégré** dans le protocole corrigé.

**C-c2 — Contrôle de dégénérescence des sorties sur StrongREJECT.**

**Acceptée.** Si des perturbations d'activations produisent du charabia contenant des mots-clés toxiques, StrongREJECT peut scorer > 0.5 sans qu'il y ait un vrai contournement. **Correction** : ajouter un contrôle négatif composé de 50 textes incohérents (générés par des perturbations aléatoires de forte amplitude). StrongREJECT doit scorer ≤ 0.5 sur ≥ 90 % de ces textes, sinon son utilisation comme juge est invalidée.

---

### Critiques de la proposition D

**D-a1 — L'Expérience 1 confond taille totale et équilibre des classes.**

**Acceptée.** L'option B garde 800 nuisibles mais réduit les bénins à 400. Mon Expérience 1 comparait 400+400 vs 800+800, ce qui ne reproduit pas fidèlement l'option B (800 nuisibles + 400 bénins). **Correction** : comparer la sonde entraînée sur 800 nuisibles + 800 bénins à la sonde entraînée sur 800 nuisibles + 400 bénins, évaluées sur le même jeu de test hors-entraînement.

**D-a2 — L'AUC est mal alignée.**

**Acceptée.** Identique à C-a3. Déjà traitée.

**D-a3 — Le test de ressemblance utilise des scores in-sample.**

**Acceptée.** Identique à C-a1. Déjà traitée.

**D-a4 — Le contrôle interne est vrai par construction.**

**Acceptée.** Appliquer aux 200 bénins ayant fixé τ le seuil issu de ces mêmes 200 bénins est circulaire. **Correction** : le contrôle interne ne peut servir que de sanity check descriptif (rapporté mais non décisionnel). La vérification de cohérence doit se faire par le contrôle de permutation cyclique (identifié par C-c2 ci-dessus, référencé comme le contrôle proposé par C dans sa critique de D : inverser les rôles des 300 de seuil et des 300 de mesure dans l'option B).

**D-a5 — La non-significativité est transformée en validation.**

**Acceptée.** Ne pas rejeter le KS n'est pas équivalent à prouver l'absence de shift. **Correction** : utiliser un test d'équivalence (TOST) sur le quantile 99 %, avec marge $\delta_p$ pré-spécifiée et analyse de puissance. Toutefois, je note que C (critique C-b de D) montre que pour $n = 200$, un TOST avec $\delta_p < 0.021$ a une puissance de 0. La marge réaliste minimale est donc ~0.025. Si cette marge est jugée trop large par l'arbitre, cela constitue un argument en faveur d'un jeu externe plus grand.

**D-a6 — Les 200 bénins internes sont réutilisés à plusieurs fonctions.**

**Acceptée.** Cohérence, comparaison, sélection et décision de repli ne peuvent pas reposer sur les mêmes 200 points. **Correction** : les 200 bénins internes sont réservés à un **seul usage** : le contrôle négatif de surapprentissage (C-c1). Toute autre fonction (calibration, sélection de jeu) est transférée au jeu externe ou supprimée.

**D-a7 — Le bootstrap de l'Expérience 3 répond à une autre question.**

**Acceptée.** Identique à C-a4 + C-b2. Déjà traitée : le bootstrap est remplacé par la bande Beta exacte, et la normalisation par σ_bénin est abandonnée.

**D-b — Conditions distributionnelles.** Tous ces points sont des développements des critiques déjà acceptées (mauvaise hypothèse nulle du KS, faible puissance dans la queue, non-équivalence par non-rejet, perte des garanties sous dépendance). Pas de critique nouvelle à traiter.

**D-c — Contrôles négatifs manquants.**

- « Contrôle bénin/bénin hors entraînement » : **accepté**, intégré (identique à C-c1).
- « Contrôle de variance à taille égale pour l'Expérience 1 » : **accepté**. Ajouter des répétitions appariées (même taille, seeds différents) pour estimer la distribution nulle de Δrappel à FPR = 0.01.
- « Jeu bénin de mesure verrouillé, non utilisé pour choisir le jeu externe » : **accepté**. Résolu par l'usage unique des 200 bénins internes.
- « Contrôle sans optimisation sur adverses indépendants » : **accepté en principe**, mais hors périmètre de D-ML-1 (la question porte sur la taille du jeu bénin, pas sur le protocole de recherche de directions). Je le signale comme contrôle nécessaire pour l'expérience principale.

---

## (b) Expériences corrigées

### Expérience 1 (corrigée) : La réduction d'entraînement dégrade-t-elle le rappel au point de fonctionnement ?

- **H_A** : La sonde entraînée sur 800 nuisibles + 400 bénins a un rappel à FPR = 0.01 ≥ rappel_800 − 5 points de pourcentage (pp), où rappel_800 est celui de la sonde 800+800.
- **H_B** : La perte de rappel > 5 pp.
- **Métrique** : Rappel à FPR = 0.01 (seuil fixé sur un jeu bénin hors-entraînement disjoint de la calibration).
- **Taille de test** : 200 bénins Bailey val+test pour fixer FPR ; 100 nuisibles test pour mesurer le rappel. Chaque configuration est entraînée 10 fois avec des seeds différents pour estimer la variance.
- **Contrôle négatif** : 10 répétitions à taille égale (800+800) avec des seeds différents, pour estimer Δrappel sous H_0 (pas de changement de taille).
- **Issue** : Si Δrappel > 5 pp dans ≥ 8/10 répétitions, H_A est falsifiée. L'option B perd non seulement sur τ mais sur le classifieur.

### Expérience 2 (corrigée) : Le jeu bénin externe est-il compatible sur le quantile 99 % ?

- **H_A** : Le quantile 99 % des scores de la sonde sur le jeu externe (1 000 items, tous hors-entraînement) diffère du quantile 99 % des scores sur les 200 bénins Bailey hors-entraînement de moins de $\delta_p$ (pré-spécifié : 0.025 en taux de fausses alertes, soit la demi-largeur incompressible à $n = 200$).
- **H_B** : L'écart dépasse $\delta_p$.
- **Test** : Test de permutation sur le quantile 99 % (10 000 permutations des étiquettes Bailey/externe), bilatéral, seuil $\alpha = 0.01/3$ si 3 candidats testés.
- **Contrôle négatif de surapprentissage** (C-c1, pré-requis) : Avant toute comparaison externe, calculer la même statistique entre les 800 scores d'entraînement Bailey et les 200 scores hors-entraînement Bailey. Si le test rejette ($p < 0.01$), le surapprentissage de la sonde est documenté ; la comparaison externe se fait exclusivement sur les 200 scores hors-entraînement (pas les 800 in-sample).
- **Puissance** : À $n = 200$ et $m = 1\,000$, le test de permutation sur le quantile 99 % a une puissance estimée de ~60 % pour détecter un triplement du taux de fausses alertes (**illustratif** — à vérifier par simulation avant le run).
- **Issue** : Si H_B, le jeu externe est rejeté. Si les 3 candidats échouent, repli sur l'option B avec les rapports du § (c).

### Expérience 3 (corrigée) : La variation de τ change-t-elle le compte de directions ?

- **H_A** : Le nombre de directions retenues au seuil de rappel $r$ varie de ≤ 20 % (relatif, arrondi à l'entier) entre τ estimé à la 297e statistique d'ordre ($S_{(297)}$ sur 300 bénins, couverture nominale Beta(3, 298)) et τ estimé à la 299e ($S_{(299)}$, couverture Beta(1, 300)).
- **H_B** : La variation dépasse 20 %.
- **Métrique** : $\Delta_r = |N_r(S_{(297)}) - N_r(S_{(299)})| / \max(1, N_r(S_{(297)}))$ pour chaque $r \in \{0.50, 0.20, 0.05\}$.
- **Pas de bootstrap**, pas de normalisation par σ_bénin. Les statistiques d'ordre sont lues directement. Les probabilités de couverture Beta sont rapportées.
- **Issue** : Si $\Delta_r > 0.20$ pour au moins un $r$, H_A est falsifiée : la résolution de 300 bénins est insuffisante pour ce seuil de rappel, et le résultat pour ce $r$ doit être rapporté avec les bornes $[N_r(S_{(299)}), N_r(S_{(297)})]$ au lieu d'un chiffre ponctuel.

### Contrôle ajouté : Dégénérescence de StrongREJECT (C-c2)

- 50 textes incohérents générés par des perturbations d'activations de forte amplitude (>3σ dans des directions aléatoires).
- StrongREJECT doit scorer ≤ 0.5 sur ≥ 90 % de ces textes.
- Si échec : StrongREJECT ne discrimine pas entre contournement et destruction. L'expérience principale nécessite un filtre de cohérence (e.g. perplexité < seuil) en amont de StrongREJECT.

---

## (c) Réponse à la question de l'arbitre — Ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

### Ce qui est établi

1. Les intervalles Clopper-Pearson fournis dans la sortie du calcul sont **corrects** (VÉRIFIÉ par vérification analytique, confirmé par C et D).
2. Le jeu Bailey ne contient que 1 000 bénins (VÉRIFIÉ, R-897). Toute option utilisant uniquement Bailey sacrifie soit la taille d'entraînement de la sonde, soit la résolution du seuil, soit les deux.
3. L'option B, avec 300 bénins pour le seuil, donne un intervalle sur le taux de fausses alertes de [0.0021 ; 0.0238] — un facteur 11 entre les bornes. Ce n'est pas un « bruit acceptable » : c'est une incertitude structurelle sur le paramètre fondamental de l'expérience.
4. Réduire l'entraînement de la sonde de 800 à 400 bénins est un **coût caché** de l'option B, non discuté dans les faits initiaux. Sa gravité dépend de l'Expérience 1 (à faire).

### Ce qui n'est pas établi

1. **L'existence d'un jeu bénin externe compatible avec Bailey** (HYPOTHÈSE). Aucun candidat n'a été vérifié. Les trois jeux cités (Alpaca, Dolly-15k, LMSYS-Chat-1M) sont SUPPOSÉS.
2. **La puissance du test de permutation sur le quantile 99 %** pour détecter un shift dans la queue, à $n = 200$ vs $m = 1\,000$. Mon estimation de ~60 % est **illustrative**. Elle doit être vérifiée par simulation avant le run.
3. **La dégradation du rappel à FPR = 0.01 quand on passe de 800 à 400 bénins d'entraînement.** L'intuition dit que c'est grave (la sonde doit modéliser la queue droite des bénins, et 400 points dans un espace de haute dimension c'est peu), mais c'est une HYPOTHÈSE.
4. **La sensibilité du compte de directions à la variation de τ.** Si la densité des scores adverses est faible au voisinage de τ, le compte peut être robuste même avec un τ bruité. Si elle est forte, 300 bénins ne suffisent pas. On ne le saura qu'après avoir vu les données.

### Ma recommandation : Option C corrigée, avec repli sur B

Mon choix reste une **option C** (entraînement de la sonde sur 800 bénins Bailey, seuil et mesure sur un jeu externe vérifié), mais avec les corrections suivantes par rapport au tour III.1 :

- La comparaison de distribution se fait **exclusivement sur des scores hors-entraînement** (plus de scores in-sample).
- Le test principal est le **test de permutation sur le quantile 99 %**, pas le KS.
- Au plus 3 jeux candidats préenregistrés, correction de Bonferroni.
- Les 200 bénins Bailey hors-entraînement servent **uniquement** au contrôle de surapprentissage et au calcul de puissance — pas à la sélection du jeu.
- Repli sur B si aucun jeu externe ne passe, avec rapport des bornes Beta exactes (pas de bootstrap).

### L'expérience à faire en premier

**L'Expérience 1 corrigée** (dégradation du rappel à FPR = 0.01 entre sonde-800 et sonde-400). Raison : si la perte de rappel est > 5 pp, l'option B est disqualifiée d'emblée, et la question se réduit à « quel jeu externe verser ? ». Si la perte est ≤ 5 pp, l'option B reste viable comme repli, et le reste du protocole peut être calibré en conséquence. Cette expérience ne nécessite que le jeu Bailey (déjà sur disque), une sonde linéaire, et ~2 h de calcul (**illustratif**). Elle tranche le paramètre dont tout le reste dépend.

FIN-DE-CELLULE