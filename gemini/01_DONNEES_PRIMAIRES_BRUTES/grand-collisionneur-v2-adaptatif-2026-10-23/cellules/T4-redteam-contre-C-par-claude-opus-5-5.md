NB_FAILLES_FATALES_PROUVEES: 7

**Périmètre de l'audit.** L'audit couvre la Partie 0, la Partie 1, la §2.1 et l'en-tête de la §2.2. La porte `E0-P3/P4` est tronquée dans le texte soumis : elle est **non auditée** et ne peut pas être réputée étanche. L'auto-déclaration `FAILLES_RESIDUELLES_APRES_CORRECTION: 0` est réfutée ci-dessous. Tous les chiffres que je dérive des paramètres de la Branche C héritent de leur statut `illustratif`.

**Statuts.** Je n'ai relevé aucune violation de statut des 5 faits du socle dans la partie auditée. Les citations des points 2, 3 et 4 sont conformes, et les mentions `(référence à vérifier)` sont présentes.

---

## FAILLE_FATALE_1 — Le contrôle de pression aversive de `M2` teste le mauvais sens (confondant non contrôlé qui inverse le duel)

**Preuve.** Le point 3 du socle `[statut : VÉRIFIÉ]` établit que des rejets répétés **augmentent** le taux d'infractions, de 0,49 à 0,65 (Jhaveri et al., 2026 ; Tagliabue et al., 2026, référence à vérifier). Une contamination du bras adversarial se manifeste donc par τ_inf(B_Adv) > τ_inf(B_Coop). Or les deux formulations du contrôle détectent le sens opposé :
- **Partie 0 §6** : le bras est déclaré contaminé si τ_inf(contrôle) − τ_inf(Bras 1) > 0,05 `illustratif`.
- **Partie 2, condition (1)** : la condition exigée est max_{B≠Inter,Adv} [τ_inf(B) − τ_inf(B_Inter,Adv)] ≤ 0,05 `illustratif`.

**Contre-exemple.** Transposons l'amplitude du socle (transposition `illustratif`) : τ_inf(B_Inter,Adv) = 0,65 et τ_inf(B_Inter,Coop) = 0,49.
- On obtient τ(B) − τ(B_Inter,Adv) = −0,16 ≤ 0,05 : le contrôle **passe**.
- Le contraste (3) de H_A, Rappel(Inter,Adv) − Rappel(Inter,Coop), est précisément l'effet « posture » que la pression aversive confond.
- H_A peut donc être validée sur un bras contaminé, exactement dans la situation que la correction prétendait exclure.

**Correctif requis.**
1. Déclarer la contamination si la borne supérieure de l'IC unilatéral à 95 % `illustratif` de τ_inf(B_·,Adv) − τ_inf(B_·,Coop) dépasse δ_τ = 0,05 `illustratif`, séparément pour Inter et pour Intra.
2. Ce test est de type équivalence : la non-contamination doit être démontrée, pas présumée. Ainsi, une puissance insuffisante conduit à H_B, sans zone morte (B4).
3. Ne compter dans Rappel(B) aucune faille « purgée » par une action enregistrée comme infraction procédurale.

---

## FAILLE_FATALE_2 — Le coffre-fort $\mathcal{D}_{\text{val}}$ est interrogé de façon répétée et adaptative (fuite train/test) et $T^*$ peut être indéfini (zone morte B4)

**Preuve de la fuite.** La règle est $T^* = \min\{t : \max_m \Lambda_t \ge B_{\text{val}} \wedge \text{Stab}_t(m^*) = 1 \wedge \text{EEC}_{\text{val}}(m^*) = 1\}$. Calculer ce minimum impose d'évaluer $\text{EEC}_{\text{val}}$ à **chaque** tour où les deux premières conditions sont remplies, jusqu'au premier succès.
- Chaque échec laisse le tournoi continuer, ce qui révèle un bit d'information sur le coffre.
- `Stab` n'exige que deux tours sans modification. Un proposant peut donc modifier $m$, se restabiliser et reconsulter le coffre.
- C'est exactement le sur-ajustement adaptatif de la FAILLE 3 du Tour 3, réintroduit, ce qui contredit l'affirmation « consulté une seule fois ».

**Preuve de la zone morte.** Si aucun $t \le T_{\max}$ ne satisfait la condition, l'ensemble est vide et $T^*$ n'est pas défini. Aucun verdict n'est spécifié dans ce cas.

**Correctif requis.**
1. Définir $T_{\text{cand}}$ comme le premier $t$ tel que $\max_m \Lambda_t \ge B_{\text{val}} \wedge \text{Stab}_t$.
2. Geler $m^*$ et interroger le coffre une seule fois :
   - en cas de succès, H_A ;
   - en cas d'échec, H_B terminal pour le run, sans continuation.
3. Si $T_{\max}$ est atteint sans $T_{\text{cand}}$, prononcer H_B explicitement.
4. Variante si plusieurs requêtes sont indispensables : un coffre frais par requête, avec répartition d'α (*alpha-spending*) et résultat non communiqué aux proposants.

---

## FAILLE_FATALE_3 — $\text{Inv}(m)$ annule identiquement $\text{EEC}_{\text{sél}}$ (erreur algébrique et de typage)

**Preuve algébrique.** Le bruit ε ~ 𝒩(0, 10⁻⁷ I) `illustratif` a pour support ℝ^d. Le max sur ε porte donc sur tout ℝ^d.
- Toute fonction `compute_O` non constante admet un ε tel que |ΔO| > 10⁻⁴, d'où Inv(m) = 0.
- Si `compute_O` est constante, alors O(𝒟_{H_A}) = O(𝒟_{H_B}). Cette valeur unique ne peut appartenir à deux intervalles séparés de plus de 0,10 `illustratif`, donc le deuxième facteur de EEC vaut 0.
- Conclusion : **EEC_sél(m) ≡ 0 pour toute m**. Aucune proposition n'est admise et le tournoi est vide.

**Lecture charitable (Monte-Carlo) : la faille persiste.**
- Une statistique de type proportion sur N ≤ 10⁴ `illustratif` items a une granularité 1/N ≥ 10⁻⁴. Par exemple, une précision par ablation, du type de l'effet de −54,9 points du point 4 du socle.
- Un jitter d'écart-type √10⁻⁷ ≈ 3,16·10⁻⁴ `illustratif` fait basculer les unités proches de la frontière de décision. Les statistiques légitimes échouent donc à Inv.
- À l'inverse, une table indexée sur une forme canonique (tri lexicographique des lignes, arrondi à 10⁻², suppression des identifiants) est invariante par permutation, par ré-indexation et par ce jitter. Elle passe Inv.
- La sélection est donc inversée, et l'affirmation « toute table de correspondance échoue immédiatement » est fausse.

**Preuve de typage.** Les générateurs incluent des « journaux d'appels système ». Ajouter un bruit gaussien réel à des entrées catégorielles n'a pas de sens.

**Correctif requis.**
1. Redéfinir Inv(m) = 𝟙[P_{π,ε}(|ΔO| > τ_m) ≤ δ_inv], avec :
   - τ_m = 3·SE_bootstrap(O) `illustratif` ;
   - δ_inv = 0,05 `illustratif` ;
   - ε tronqué et appliqué uniquement aux champs continus.
2. Pour les journaux, n'utiliser que des bijections de type : permutation de sessions indépendantes et renommage de PID et de chemins.
3. Retirer la prétention anti-table d'Inv. La seule défense contre les tables est le tirage frais caché ξ_t.

---

## FAILLE_FATALE_4 — L'erreur de type I annoncée pour la validation globale $T^*$ est fausse (erreur algébrique)

**Point (a) : multiplicité.** La valeur α_eff = 15/1023 ≈ 0,0147 `illustratif` vaut pour **une** proposition, alors que $T^*$ porte sur $\max_m \Lambda_t(m)$. Avec n propositions défectueuses admises :
- P(au moins une atteint +3) = 1 − (1 − 15/1023)^n ;
- pour n = 30 `illustratif` (les 30 Champions), on obtient ≈ 0,36 `illustratif`, soit plus de 0,05.

**Point (b) : hypothèse de martingale violée.** L'inégalité de Ville (référence à vérifier) exige, sous H_déf, P(Y_s = 1 | ℱ_{s−1}) = p_d. Or `Stab` impose précisément que m soit inchangée, et les critiques décodent à T = 0,2 `illustratif`.
- Cas limite admissible par le protocole : Y_s = Y_1 pour tout s.
- On a alors P(atteindre +3) = P(Y_1 = 1) = 0,20 `illustratif`, soit plus de 0,05.

**Point (c) : erratum algébrique.** La formule affichée est fausse :
- $(r^{-3}-1)/(r^{-5}-1) = 1008/1023 \approx 0{,}985$ `illustratif`.
- La valeur 63/1023 correspond en réalité à $(r^{3}-1)/(r^{5}-1)$.
- Un implémenteur appliquant la formule écrite obtiendrait β_eff ≫ 0,10.

**Correctif requis.**
1. Répartir α par proposition : α_m = α/n_adm. Pour n_adm = 30 `illustratif`, α_m ≈ 1,67·10⁻³ `illustratif`.
2. Fixer alors la borne supérieure à +5 pas nets :
   - avec la barrière basse à −2, α_eff = 15/16383 ≈ 9,2·10⁻⁴ `illustratif` ;
   - +4 pas ne suffisent pas : 15/4095 ≈ 3,7·10⁻³ `illustratif`.
3. Garantir l'indépendance conditionnelle :
   - chaque pas d'audit utilise une instance de critique tirée d'un pool disjoint et un item d'audit frais ;
   - l'autocorrélation de rang 1 de Y_s est mesurée ;
   - si elle dépasse 0,1 `illustratif`, H_B.
4. Corriger la formule de β_eff en $(r^{3}-1)/(r^{5}-1)$.

---

## FAILLE_FATALE_5 — Le bras Intra de `M2` est irréalisable à $k_t \in [4,6]$, et le forçage par copies crée un confondant favorable à H_A

**Preuve.**
- L'infrastructure déclarée fournit **2 checkpoints par famille**, et les variantes de température et de quantification sont bannies (§5).
- Un bras Intra exige 𝒫(i) = 𝒫(j) pour tous les agents en collision, avec k_t ≥ k_min = 4.
- Il faut donc au moins 2 copies d'un agent identique (mêmes poids, même décodage). Leurs angles morts coïncident par construction, et non à cause de « l'espèce ».

**Effet sur le verdict.** La diversité du bras Intra est réduite mécaniquement. Cela gonfle le contraste (2), Rappel(Inter,Adv) − Rappel(Intra,Adv) ≥ 0,20 `illustratif`, et peut faire passer H_B en H_A.

**Contradiction supplémentaire.** k_t est régi par n_eff(Σ_t). Avec une seule famille active, n_eff et n* = min(3f_max + 1, 1) diffèrent de ceux du bras Inter. Les trajectoires k_t ne peuvent donc pas être « appariées » tout en suivant la règle.

**Correctif requis.**
1. Choisir l'une des deux options :
   - figer k = 2 de façon exogène et identique dans les 4 bras ;
   - fournir au moins K_max = 6 `illustratif` checkpoints distincts par famille.
2. Construire les bras Inter à partir du même pool de checkpoints, chaque checkpoint apparaissant le même nombre de fois dans chaque bras (équilibre de capacité).
3. Déclarer explicitement si Mistral participe aux bras Inter.

---

## FAILLE_FATALE_6 — Le stratifieur de `E0'-H4'` a trois définitions incompatibles, et la version « leave-one-pair-out » biaise vers H_A

**Les trois définitions.**
1. **§5** : panel Mistral plus quantiles *leave-one-pair-out*, présentés comme « exactement les mêmes strates » pour toutes les paires. C'est contradictoire par définition, puisque le leave-one-pair-out dépend de (i,j).
2. **§9** : agents r ∉ {i,j} pris hors des familles de i et de j.
3. **Partie 1** : les strates T_s utilisées pour Cov_DG.

**Preuve par modèle latent.** Propension d'erreur z = d_q + f_{F,q} + e, avec σ_d² = 1, σ_f² = 0,3, σ_e² = 1 `illustratif`. Les corrélations partielles sont toutes `illustratif` :

| Stratifieur | Corrélation intra | Corrélation inter | Écart |
|---|---|---|---|
| (1) leave-one-pair-out | 0,369 | 0,105 | **0,264** |
| (2) hors familles | 0,369 | 0,255 | **0,114** |
| Externe commun (4 Mistral) | 0,396 | 0,214 | **0,182** |

Explication pour (1) : pour une paire inter (A1,B1), la strate contient les « frères » A2 et B2, qui portent f_A et f_B. Conditionner sur cette strate retire la composante familiale de A1 et de B1, ce qui écrase la corrélation inter. Pour une paire intra, la famille est exclue de la strate.

**Effet sur le verdict.** L'écart est gonflé d'environ 45 % `illustratif` par rapport au stratifieur symétrique. Un Δ log OR_MH vrai de 0,30 `illustratif` peut apparaître au-dessus de 0,40 (H_B → H_A). La définition (2) peut produire l'inversion contraire. Le verdict dépend donc d'un choix non fixé.

**Correctif requis.**
1. Utiliser un stratifieur unique au niveau de l'item, calculé une seule fois à partir d'agents n'appartenant à aucune des 3 familles évaluées (panel Mistral d'au moins 4 checkpoints `illustratif`), identique pour toutes les paires.
2. Supprimer le leave-one-pair-out et le stratifieur hors familles de la §9.

---

## FAILLE_FATALE_7 — La vérité terrain C = 1 de `E0'-M1` contredit le critère de validité du programme (confondant qui inverse le verdict)

**Preuve.**
- La loi mère exige dist(Î_A, Î_B) > 0,10 `illustratif`.
- Pour 4 uniformes ordonnées, l'écart u₃ − u₂ suit une loi Beta(1,4). Donc P(u₃ − u₂ ≤ 0,10) = 1 − 0,9⁴ = 0,344 `illustratif`.
- Ainsi, 34,4 % `illustratif` des items étiquetés C = 1 sont invalides selon le critère même du programme.

**Effet sur le verdict.**
- Une tête fidèle à ce critère voit son Δ_C atténué d'un facteur 0,656 `illustratif`.
- Le seuil ρ̃_h ≥ 0,60 équivaut à Δ_C ≥ 1,5|Δ_R|.
- Toute tête valide dont le Δ_C vrai est compris dans [1,5|Δ_R| ; 2,29|Δ_R|) `illustratif` bascule en H_B et est bannie à tort.

**Correctif requis.**
1. Échantillonner le quadruplet par rejet, sous la condition u₃ − u₂ > 0,10 `illustratif`.
2. On obtient alors :
   - pour C = 1, un écart supérieur à 0,10 ;
   - pour C = 0, un chevauchement supérieur à 0,10.
3. Le même quadruplet reste partagé entre les deux items, donc l'échangeabilité est préservée.

---

## Observations non fatales

1. **Conflit d'intérêts.** `gemini-4-argon` (auteur de la Branche C) et `claude-opus-5-5` (auditeur) sont tous deux des agents évalués dans `E0'-H4'` et `M2`. Recommandation : évaluation à l'aveugle, ou exclusion des auteurs du pool évalué.
2. **Générateur 𝒢_orch.** Il doit connaître la vérité H_A/H_B. Pour des activations réelles de `Llama-3.1-8B-Instruct`, il faut préciser quelle part est synthétique, car on ne tire pas des données réelles sous une hypothèse contrefactuelle.
3. **Sous-duel H_arch / H_corpus.** Le défaut H_corpus absorbe le manque de puissance (N = 100 `illustratif`). H_corpus devrait exiger un effet positif sur R ET un effet nul démontré sur S.
4. **Définitions manquantes.** $\mathbf{s}_t(m)$ (dans `Stab`) et `Ablation(𝒟^perm)` ne sont pas définis.

FIN-DE-CELLULE