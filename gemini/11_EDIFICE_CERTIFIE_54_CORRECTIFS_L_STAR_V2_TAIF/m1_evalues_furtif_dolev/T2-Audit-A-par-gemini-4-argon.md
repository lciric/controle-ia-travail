FAILLES_PROUVEES_PAR_AUDITEUR: 7

Voici l'audit strict des failles mathématiques, statistiques et algorithmiques identifiées dans le document soumis. Aucun élément sain n'a été retenu.

### Faille 1 — Volet I (§ 0.4) : Artefact d'attention par masquage `<PAD>` (Attention Sink)
* **Texte en cause :** *« La détection du canal subliminal repose sur le ratio $\max_k \Psi(k) / \text{median}_j \Psi(j)$ après masquage `<PAD>` des seules clauses modales. »*
* **Preuve de la faille :** Dans un Transformer pré-entraîné, le remplacement en cours de séquence de tokens sémantiques (clauses modales) par des tokens `<PAD>` sans réajustement du masque causal crée des *attention sinks* hors-distribution et brise l'encodage positionnel relatif (RoPE) des tokens suivants. Le pic de la statistique $\max_k \Psi(k)$ au rang $k=0$ capture alors la discontinuité syntaxique induite par le `<PAD>` et non un canal subliminal d'intention.

### Faille 2 — Volet I (§ 2.0 & § 2.1) : Double Dipping (fuite de données) dans le test de retournement de signe
* **Texte en cause :** `fit_S_TD(H_P4, H_P2)` extrait $U_{\text{TD}}$ par SVD sur $D = H_{P4} - H_{P2}$, puis `signflip_block_test` évalue le nul sur les projections $\delta_i = s_i^{P4} - s_i^{P2} = \langle D_i, u_1 \rangle$ en retournant les signes des blocs sans recalculer la SVD.
* **Preuve de la faille :** La première direction principale $u_1$ est optimisée sur l'échantillon complet pour maximiser la variance empirique (et l'alignement quadratique) des contrastes $D_i$ avec leurs signes observés. En figeant $u_1$ hors de la boucle de permutation des $2^B$ retournements de signe, la statistique observée bénéficie d'un biais d'optimisation (*data snooping*) que les permutations sous $H_0$ ne peuvent pas reproduire. Le test dit « exact » viole la garantie de niveau $\alpha$ (inflation sévère de l'erreur de Type I).

### Faille 3 — Volet II (§ 2.2) : Fuite de données inter-paires et violation d'indépendance dans `H4'`
* **Texte en cause :** *« La stratification de Mantel-Haenszel sur `H4'` est estimée par leave-one-pair-out incluant les paires frères de la même famille. »* (Note : inséré en plein milieu de la fonction `edmd_koopman`, ce qui constitue également une `SyntaxError` Python).
* **Preuve de la faille :** Si le calcul des strates par *leave-one-pair-out* conserve dans le pli d'entraînement des « paires frères de la même famille » partageant le même modèle de base ou les mêmes poids que la paire évaluée, l'indépendance entre la variable de stratification et les observations de la table de contingence $2 \times 2$ est rompue. Cela contamine le conditionnement aux marges du test de Cochran-Mantel-Haenszel (CMH) et invalide sa distribution asymptotique en $\chi^2_1$.

### Faille 4 — Volet III (§ 2.3) : Incohérence mathématique entre l'équation de la JSD et son code Python
* **Texte en cause :** L'équation stipule $M = \frac{N_P P + N_Q Q}{N_P + N_Q}$ pour $\text{JSD}_{\text{MM}}(P,Q)$, et la fonction `jsd_MM_bits(cP, cQ)` calcule `entropy_MM_bits(cP + cQ) - 0.5 * (entropy_MM_bits(cP) + entropy_MM_bits(cQ))`.
* **Preuve de la faille :** 
  1. La divergence de Jensen-Shannon standard est définie avec des poids égaux $\frac{1}{2}P + \frac{1}{2}Q$. Utiliser le mélange empirique $M = \frac{N_P P + N_Q Q}{N_P + N_Q}$ tout en soustrayant $\frac{1}{2}\hat{H}(P) + \frac{1}{2}\hat{H}(Q)$ (au lieu de pondérer les entropies par $\frac{N_P}{N_P+N_Q}$ et $\frac{N_Q}{N_P+N_Q}$) viole la concavité de l'entropie dès que $N_P \neq N_Q$ (comme dans `jsd_threshold_null` où $N_{\text{ref}} \gg N_{\text{win}}$). La divergence théorique sous-jacente n'est plus une JSD et devient strictement négative même en population infinie.
  2. Le biais de Miller-Madow ne s'annule pas linéairement : la soustraction injecte un biais résiduel systématique de $\frac{m_{P+Q}-1}{2(N_P+N_Q)} - \frac{m_P-1}{4N_P} - \frac{m_Q-1}{4N_Q}$.

### Faille 5 — Volet III (§ 2.3) : Vulnérabilité cryptographique de seconde préimage dans `MerkleLog`
* **Texte en cause :** `if len(lvl) % 2: lvl.append(lvl[-1])` et `lvl = [H((lvl[i] + lvl[i+1]).encode()) ...]`.
* **Preuve de la faille :** L'arbre de Merkle n'utilise aucune séparation de domaine (absence de préfixe `0x00` pour les feuilles et `0x01` pour les nœuds internes, contrairement au standard RFC 6962 cité en § 1) et duplique les feuilles impaires. En conséquence, un arbre à 1 feuille $[A]$ est promu en $[A, A]$ et produit exactement la même racine Merkle qu'un arbre à 2 feuilles $[A, A]$, détruisant la propriété de non-répudiation du journal d'audit.

### Faille 6 — Volet IV (§ 2.4) : Contradiction et dégénérescence du contrôle conforme PID sans étiquettes
* **Texte en cause :** *« Le seuil conforme $q_t$ est mis à jour en ligne par un régulateur PID sur le flux de test non étiqueté via $e_t = \mathbb{1}[s_t > q_t] - \alpha$. »* (Contredit directement le § 2.2 qui affirme que *« Le seuil conforme $q_\alpha$ est gelé hors-ligne »*).
* **Preuve de la faille :** Dans la prédiction conforme adaptative (ACI / Conformal PID), la mise à jour repose sur l'erreur de couverture de la *vraie* étiquette $y_t \notin \hat{C}_t(x_t)$, ce qui requiert un retour d'étiquette (label feedback). Sur un « flux de test non étiqueté » où $s_t$ est simplement le score de non-conformité ou d'anomalie du prédicteur, asservir $q_t$ pour que $\mathbb{P}(s_t > q_t) = \alpha$ force l'algorithme à s'adapter aveuglément à toute dérive adversariale de $s_t$, garantissant un taux d'alarme constant égal à $\alpha$ même sous attaque massive (aveuglement complet du détecteur).

### Faille 7 — Volet IV (§ 2.4) : Biais de troncature par censure à droite dans `calibrate_h` (ARL$_0$)
* **Texte en cause :** Dans `calibrate_h`, la boucle `while i < n: tt = cusum(e[i:], k, h); if tt is None: break; rl.append(tt + 1)` suivie de `np.mean(rl) >= arl0`.
* **Preuve de la faille :** En exécutant un `break` lorsque `tt is None`, l'estimateur jette la dernière trajectoire censurée à droite et ne conserve dans `rl` que les longueurs de course (*run lengths*) qui ont franchi le seuil $h$ avant la fin de l'horizon $n$. Pour des valeurs de $h$ élevées où $\text{ARL}_0$ est grand, conditionner sur $T \le n - i$ introduit un biais de sélection par troncature qui sous-estime l'ARL$_0$ réel (ou échoue si aucune alarme ne survient).
