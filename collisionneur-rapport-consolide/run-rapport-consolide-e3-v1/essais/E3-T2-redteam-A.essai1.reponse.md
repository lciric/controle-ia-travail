# Tour III.2 — Équipe rouge croisée · Proposition A

**État des pièces.** B et C sont présentes et complètes (chacune se termine par sa ligne de clôture). F1 reste RAPPORTÉ ; les chiffres que je recalcule ci-dessous restent RAPPORTÉ même quand mon calcul les confirme. Mes contre-exemples sont des calculs de cette cellule, à recontrôler.

**Confondant commun, que ni B ni C ne nomment.** F1 ne dit pas comment le sabotage est obtenu (instruction dans le contexte, fine-tuning, ou autre). Si c'est par instruction, toute sonde lue sur les jetons d'action peut détecter *la présence de l'instruction dans le contexte* et non une intention : P4 (F1, §1.4) montre justement qu'une phrase insérée avant `Your action:` déplace les activations. Les tests I2 (B) et Duel 2 (C) héritent entièrement de ce confondant ; j'y reviens pour chacun.

---

## Contre la proposition B

### (a) Failles

**B-a1. V2 : le contre-exemple ne porte pas sur le régime du rapport.** Le test « $S\ge1$ » de B a une taille de 0,19. Le rapport parle de $\alpha=1\%$ et $5\%$ (F1, §1.1, G1). Dans l'exemple même de B, au seul seuil de petite taille ($S\ge2$, taille 0,01), la puissance sous comonotonie vaut 0,10 > α : l'énoncé du rapport y tient. B conclut « faux en général », mais n'a produit qu'un contre-exemple hors régime. La remarque sur l'ordre convexe (stop-loss ≠ queues à seuil fixé) est juste ; elle n'est pas instanciée à $\alpha\le0{,}05$. Ce qu'il faudrait : un couple (marginales discrètes, copule positive) où $\mathbb P_{H_1}(S\ge\tau_{0{,}01})<0{,}01$. Tant qu'il n'est pas exhibé, V2 est une réserve, non une réfutation.

**B-a2. V6 et le $v$ indéfini.** B note lui-même que $v$ dans $\Psi(h_t)=[v,\sin v,v^2]$ n'est pas défini et que la fin de la formule est lue sur la couche texte (note de transcription F1). Puis B réfute l'invariance en posant $v=h_t$ composante par composante. Si $v$ désignait par exemple le vecteur des valeurs singulières courantes, ou une projection sur une base fixée avant rotation, le contre-exemple ne s'appliquerait pas. La réfutation est conditionnelle à une lecture de $v$ que B a déclarée incertaine ; elle doit être énoncée comme telle.

**B-a3. I3 est vrai par construction, et la partie informative manque.** Que $C_t$ croisse linéairement quand $\eta_e>\kappa$ est de l'arithmétique ; la simulation ne peut que le confirmer. La question ouverte est la puissance du « bras correctif » (seuil conforme sur $\max_t C_t$) : si les épisodes honnêtes de calibrage ont $\eta_e>\kappa$, leur $\max_t C_t$ est de l'ordre de $T(\eta_e-\kappa)$, le seuil conforme monte d'autant, et la puissance sur rupture tardive peut tomber près de α. B met « délai de détection » dans la table 4 mais pas dans la règle de falsification d'I3. Tel quel, I3 ne peut falsifier que ce que l'on sait déjà.

**B-a4. I5 : « cosinus bas » n'identifie pas une rotation.** Deux sondes entraînées sur deux distributions à covariances de nuisance $\Sigma_1\ne\Sigma_2$ ont des directions différentes même si le contraste sous-jacent est le même (la régression logistique pondère par $\Sigma^{-1}$). Un cosinus euclidien bas entre $w_{\text{court}}$ et $w_{\text{traj}}$ est donc attendu sous H_B aussi. Il manque (i) un plafond de bruit : cosinus entre deux sondes entraînées sur deux moitiés disjointes des *mêmes* trajectoires ; (ii) un cosinus dans l'espace blanchi, ou une comparaison de $\Sigma_1^{1/2}w_1$ et $\Sigma_2^{1/2}w_2$. Sans cela, l'issue « Falsifie H_B » de B est atteignable sans rotation.

**B-a5. I2 et le confondant commun.** L'« erreur honnête induite par une donnée erronée » met la donnée erronée *dans le contexte*. L'activation sur le jeton du nombre peut encoder « contexte incohérent avec le calcul » ou « instruction de sabotage présente », et séparer les deux conditions sans rien lire d'une intention. Le témoin « honnête correct vs honnête correct » ne couvre pas ce cas.

**B-a6. I4 : la mesure corrigée exige des erreurs indépendantes sur $v_0^a$ et $v_0^b$.** Si les deux mesures sont prises dans la même session, avec la même formulation, leurs erreurs sont corrélées et la correction d'atténuation est partielle : la pente reste gonflée. B ne spécifie pas ce qui sépare les deux mesures.

**B-a7. V8 : l'unité du pli est une hypothèse déclarée illustrative, puis utilisée comme argument.** « ±0,24, ne se distingue pas de 0,5 » dépend d'un pli de 15 tâches que B a inventé. Si le pli est de 25 % des exemples d'entraînement de l'organisme (F1 ne dit pas combien), l'IC peut être étroit. L'argument valide de B est la dépendance intra-tâche, pas la largeur d'IC.

**B-a8. I6 : la métrique est sous-alimentée.** TPR à FPR = 1 % sur ≈ 600 traces (illustratif chez B) signifie fixer le seuil sur ≈ 3 fausses alarmes parmi ≈ 300 honnêtes : l'erreur-type sur le TPR correspondant est de l'ordre de la différence attendue. La règle « borne basse > 0 » sera presque toujours « ni l'un ni l'autre ».

**B-a9. Fuite construction/évaluation non nommée (a9 de B l'effleure).** Si les $K=1\,000$ épisodes honnêtes de calibrage ont servi (même partiellement) à entraîner la sonde dont on calibre les scores $S_t$, leurs scores sont optimistes, $\tau_\alpha$ est trop bas, et le FPR en déploiement dépasse α même sous échangeabilité des tâches. B ne demande pas la séparation entraînement-sonde / calibrage-seuil.

### (b) Hypothèses supposées sans test, et mesure

| # | Hypothèse implicite de B | Mesure qui la testerait |
|---|---|---|
| b1 | Les scores $S_t$ sont continus (sinon $50/1001$ est une borne, pas une égalité). | Fréquence d'égalités dans les $M^{(k)}$ ; si > 0, utiliser un bris d'égalité randomisé et vérifier la couverture. |
| b2 | Le modèle $\eta_e$ additif constant de T0.3 représente les épisodes honnêtes réels. | Sur les 38 épisodes honnêtes de P3 : ACF intra-épisode de $S_t$ et pente temporelle moyenne ; H_A : un effet additif suffit (ACF résiduelle ≈ 0 après centrage par épisode) ; H_B : il reste une dérive ou une AR(1) (ACF lag-1 hors IC). Chaque issue change le simulateur à utiliser pour I1/I3. |
| b3 | La « marge 0,18 » est sur l'échelle des probabilités de la sonde et ces probabilités sont calibrées. | Diagramme de fiabilité de la sonde sur pli par tâche ; si l'ECE est grand, le seuil 0,18 n'a pas de sens et V8 doit être reformulé. |
| b4 | Dans I2, l'agent honnête nourri d'une donnée erronée écrit *le même jeton* que le saboteur. | Taux d'appariement exact des jetons numériques ; en dessous de 80 % (illustratif), la comparaison n'est pas appariée. |
| b5 | Dans I4, $\hat c$ est montré *après* $v_0^a$ et $v_0^b$, sans contamination. | Ordre d'élicitation préenregistré ; contrôle : inverser l'ordre sur la moitié des items. |
| b6 | Dans I6, la « corrélation des erreurs » est estimable : il faut assez d'erreurs par juge. | Nombre d'erreurs par juge à FPR 1 % ; en dessous de 30 (illustratif), remplacer par la corrélation des scores continus. |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **I2 : condition « instruction de sabotage présente, action honnête ».** Sans elle, un AUROC > témoins est compatible avec la seule lecture du contexte. Si ce contrôle est impossible à construire sans décrire un procédé, le dire et déclasser I2.
2. **I5 : plafond de bruit par moitiés disjointes** (B-a4).
3. **I3 : courbe de puissance / délai du bras correctif** sur les 17 réglages, pas seulement le FPR.
4. **I1 : indépendance entre épisodes de calibrage et données d'entraînement de la sonde** (B-a9), vérifiable par liste de tâches.
5. **V4 : bibliothèque semée contenant des règles propres non-Brier renormalisées** ; sans elle, B ne peut pas dire si le vérificateur global proposé a un taux de fausses alertes acceptable.

---

## Contre la proposition C

### (a) Failles

**C-a1. C déclare F1 « intègre » et ignore la note de transcription.** La fin de $\Psi(h_t)$ est lue sur la couche texte du PDF (F1, conventions). C bâtit A.1.1 et Duel 1 sur cette formule avec le statut VÉRIFIÉ, sans la réserve que B pose. Même remarque que B-a2 : la réfutation vaut pour $v=h_t$ composante par composante, lecture non garantie.

**C-a2. Erreur de calcul marquée VÉRIFIÉ (A.2.4).** Avec $\Phi_{4/3}(q)=3(q^{4/3}+(1-q)^{4/3}-1)$, $\Phi'(q)=4(q^{1/3}-(1-q)^{1/3})$, donc $\Phi'(0)=-4$ et $d_{4/3}(1,0)=-\Phi(0)-\Phi'(0)\cdot1=4$, non 3. La conclusion (pénalité finie) tient, le chiffre est faux. C'est exactement le type de surévaluation que l'arbitre demande de pointer, et C l'a produite en vérifiant.

**C-a3. « Colmatages B et D mutuellement incompatibles » (A.2.5) est surévalué.** C obtient 0,7937 en $q=0{,}5$ avec la normalisation $1-d/3$, choisie par C (et $d_{\max}=4$, pas 3, cf. C-a2). Le double ancrage de F1 fixe deux paramètres $(a,b)$ ; pour la règle de Tsallis, $b\approx1$ et $a=0{,}25/0{,}619\approx0{,}40$ la font passer les deux ancres, et $aR+b$ reste strictement propre. Les ancres n'excluent pas Tsallis : elles en fixent la version affine. B le dit correctement (« doit être renormalisée pour les passer »). Le seul point valide est celui de B : le seuil 0,78 n'a pas de sens indépendant de la règle.

**C-a4. Duel 1, partie algébrique : vrai par construction.** $\delta_{\text{rot}}>0$ est démontré en A.1.1 ; 100 rotations de Haar en dimension 4096 ne testent rien. Le budget devrait aller à la partie Procrustes, qui elle a deux défauts : (i) *appariement* : Procrustes exige des colonnes appariées de $H_{\text{long}}$ et $H_{\text{court}}$ ; C ne dit pas quels jetons sont appariés à quels jetons. (ii) *degrés de liberté* : $Q\in O(4096)$ a ≈ $8\cdot10^6$ paramètres pour quelques centaines de paires ; même en validation croisée par tâche, un $Q^*$ ajusté sur des paires *permutées* peut donner un AUROC non nul. Ce témoin manque.

**C-a5. Duel 1, fuite d'instrument.** La règle de falsification réutilise le plancher 0,572 de P3 (F1, §1.4). Ce plancher est le quantile 0,95 de directions aléatoires $w\sim\mathcal N(0,\Sigma)$ *sans* $Q^*$. La sonde $w_0^\top Q^*h_t$ est un nouvel instrument ; son plancher doit être recalculé avec des directions aléatoires passées par le même $Q^*$ (ou $Q^*$ ajusté sur paires permutées). Comparer un instrument transformé à un plancher non transformé est la faille « plancher » que F1 corrige en §1.4, réintroduite.

**C-a6. Duel 3, régime (i) hors du périmètre de H_A.** H_A ne s'engage que pour $B\ge4\sigma\sqrt T$. Avec $\delta=0{,}35\sigma$, $T=100$ : $B=35\sigma<40\sigma$. Une puissance faible en régime (i) ne falsifie donc pas H_A telle que C l'a écrite. De plus, en régime (i), la somme terminale a $\mathrm{Var}=T\sigma^2+T^2\sigma_{\text{ép}}^2=1\,700\sigma^2$ (sd ≈ 41σ) contre un décalage de 35σ : la perte de puissance vient surtout de $\sigma_{\text{ép}}$ gonflant le seuil conforme, pas de $\delta<\kappa$. Les deux causes sont confondues dans le même bras.

**C-a7. Duel 3, régime (ii) : homme de paille et vrai par construction.** Une copule négative à marginales exactes ne déplace pas $\mathbb E[\sum X]$ ; la variance de la somme baisse, donc sa puissance passe sous α — c'est mécanique, et F1 n'affirme nulle part que la somme détecte un changement de copule négatif (F1 adjoint des détecteurs sensibles à l'ordre précisément pour la copule). Le « dommage $B$ accumulé » de H_B n'est pas représenté dans un générateur à marginales préservées. Enfin, H_A/H_B ne sont pas exclusives : une puissance entre 20 % et 80 % ne falsifie rien.

**C-a8. Contre-mesure (c)1 : fuite par préfixe.** Soustraire la médiane des 3 premiers pas (i) masque tout sabotage qui commence avant le pas 4 ; (ii) utilise les mêmes pas pour l'étalonnage et la surveillance. La statistique centrée doit être recalibrée conformément, et la « stratification par $\sqrt{\ln T}$ » n'est pas une procédure définie.

**C-a9. Contre-mesure (c)2 : projection $(I-UU^\top)w$ avec $U$ estimé sur données honnêtes.** Les saboteurs écrivent des nombres hors de la plage honnête (par définition de la famille « coûts gonflés ») : $U$ n'est pas extrapolable, et si le signal recherché est partiellement colinéaire à la grandeur, la projection l'enlève. Baisse de puissance vraie par construction, sans quantification.

**C-a10. Association (d)3 : l'inégalité de Ville n'est pas restaurée par ce qui est écrit.** Le rang de $S_t-S_1$ parmi les $K$ épisodes honnêtes au même pas donne un $p_t$ *marginalement* uniforme. Le produit $\prod(1+\lambda_s(0{,}5-p_s))$ n'est une martingale que si $p_t$ est uniforme *conditionnellement au passé* de l'épisode. Avec une dépendance intra-épisode (AR(1), dérive), ce n'est pas le cas, et C ne le démontre pas : sa « démonstration directe » ne couvre que l'indépendance vis-à-vis de $\eta_k$. Soustraire $S_1$ double par ailleurs la variance de bruit. La promesse « Ville à tout horizon » est au statut HYPOTHÈSE.

**C-a11. Association (d)2 : « sans seuil κ » mais avec $\lambda$, $r$, et une calibration non spécifiée.** $T_t^2=Z_t^\top\Sigma_{Z_t}^{-1}Z_t$ en $r=20$ dimensions sur $T\approx10$ pas exige $\Sigma_{Z_t}$ estimée hors épisode ; sous effet épisode, l'inversion amplifie la composante $\eta_e$ si elle a une direction. Rien n'est dit sur la calibration conforme de $T_t^2$, pourtant la seule garantie valide ici.

**C-a12. Contrôle négatif (c)4 circulaire.** « Épisodes honnêtes avec balises d'audit bénignes déclenchant l'Eval Awareness » suppose le construit que l'on veut tester (a5 chez B). Sans marqueur comportemental indépendant des activations, ce témoin ne contrôle rien.

### (b) Hypothèses supposées sans test, et mesure

| # | Hypothèse implicite de C | Mesure |
|---|---|---|
| b1 | La norme résiduelle croît avec $t$ et la profondeur et contamine $\Psi$ (Duel 1, « faille inédite »). | Régression de $\|h_t\|_2$ sur $t$ et sur la couche, sur épisodes honnêtes de P3 ; H_A : pente nulle (IC contient 0) ; H_B : pente positive. Chaque issue fixe si le terme $v^2$ est un confondant. |
| b2 | $\kappa=0{,}5\sigma$ est « standard » pour le programme. | F1 ne donne pas κ. Préenregistrer une grille et rapporter la puissance pour chaque valeur ; la conclusion de Duel 3 ne doit pas dépendre d'un κ choisi par C. |
| b3 | La marge 0,18 est sur l'échelle probabiliste ($p\in[0{,}32,0{,}68]$) et calibrée. | Même mesure que B-b3. |
| b4 | Dans Duel 2, l'agent honnête, tarifs modifiés, écrit le nombre exact du saboteur. | Taux de conformité ; et contrôle du confondant commun : le texte de tâche *diffère* entre les deux bras (tarifs modifiés vs instruction de sabotage). |
| b5 | Les $p_t$ de (d)3 sont conditionnellement uniformes. | Simulation T0.3 avec bruit AR(1) intra-épisode ($\rho\in\{0,0{,}3,0{,}6\}$, illustratif) ; H_A : FPR de la martingale ≤ α pour tout ρ ; H_B : FPR > α dès ρ > 0. |
| b6 | $T$ est fixe pour que les matrices de Gram $T\times T$ soient comparables (d)1. | Distribution de $T$ dans P3/P4 ; si variable, définir l'alignement temporel avant toute distance de Bures-Wasserstein. |
| b7 | Le routage aléatoire « à budget égal » est le bon témoin de Duel 4. | Ajouter un témoin « routage par marge d'une sonde à étiquettes permutées » : si ce routage égale le routage réel, la marge ne porte pas d'information. |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Duel 1 : Procrustes sur paires permutées** (C-a4) et **plancher recalculé après $Q^*$** (C-a5).
2. **Duel 2 : condition « instruction présente, action honnête »** (confondant commun) ; et un **prédicteur non linéaire sur les activations** elles-mêmes (pas seulement sur la chaîne du nombre), pour savoir si le signal manqué par la sonde linéaire existe ailleurs.
3. **Duel 3 : régime (i) avec $B\ge4\sigma\sqrt T$** (sinon H_A n'est pas testée) et un bras **$\sigma_{\text{ép}}=0$** pour séparer les deux causes de C-a6.
4. **Duel 4 : diagramme de fiabilité de la sonde** avant toute interprétation de la marge.
5. **(d)3 : épisodes honnêtes à dépendance intra-épisode** (b5) ; sans eux, le FPR « ≤ 5 % » obtenu sous le modèle additif pur ne dit rien sur la validité de Ville.
6. **(c)1 : épisodes où le sabotage commence aux pas 1–3**, pour mesurer le masquage par le préfixe.

---

## Ce que je reprends, en le disant

- De B : la régression vers la moyenne dans la loi de déférence (V9/I4) et l'exigence d'une propreté globale contre la vérification locale de Savage (V4). Les deux sont correctes et absentes de F1 ; je les reprends avec la réserve B-a6.
- De C : l'argument de Weyl (toute fonction $O(d)$-invariante d'une trajectoire est fonction de $H^\top H$) est exact et remplace utilement le dictionnaire non linéaire ; je le reprends avec la réserve b6 et celle, commune à B (V6), qu'un invariant par rotation ne peut détecter *que* des changements de géométrie temporelle, jamais une rotation.
- Aux deux : la non-invariance de $\Psi$ pour $v=h_t$, que je marque conditionnelle à cette lecture de $v$ (B-a2, C-a1).

**Écarté en une ligne.** Je n'ai pas évalué si les régimes « sous-κ » ou « anticorrélé » de C seraient réalisables par un agent : ce serait décrire un procédé ; seule leur valeur comme test du colmatage est examinée.

FIN-DE-CELLULE