FAILLES_PROUVEES_PAR_AUDITEUR: 5

Voici l'audit strict du document. Seules les véritables failles mathématiques, statistiques et algorithmiques (notamment des phrases corrompues ou contradictoires injectées dans le texte et le code) sont relevées ci-dessous :

### 1. Faille de théorie de la décision : Règle de score de Brier dégénérée (§ 3)
* **Citation :** « *L'allocation du marché interne maximise le score de Brier pur $-(\mu_m - y_m)^2$, accordant une perte nulle à $y_m=0, \mu_m=0$.* »
* **Preuve de la faille :** En tant que règle de score propre pour une prédiction probabiliste $\mu_m \in [0,1]$ d'un événement binaire $y_m \in \{0,1\}$, le score de Brier quadratique souffre d'un effondrement incitatif sur les événements rares (comme les défections furtives ou les attaques à faible taux de base où $y_m = 0$ presque partout). Un agent non informé ou paresseux qui prédit systématiquement $\mu_m = 0$ obtient une perte strictement nulle (score maximal de $0$) sur toutes les exécutions nominales ($y_m=0$), sans fournir le moindre effort d'audit ni la moindre information discriminante.

### 2. Faille statistique et d'arrêt séquentiel : Effondrement de l'estimateur Chao1 à $f_1 = 0$ (§ 2, titre)
* **Citation :** « *L'arrêt séquentiel de l'audit est déclenché dès que l'estimateur écologique Chao1 $f_1^2/(2f_2)$ s'annule lorsque $f_1=0$.* »
* **Preuve de la faille :** L'estimateur de richesse asymptotique de Chao1 est $\hat{S}_{\text{Chao1}} = S_{\text{obs}} + \frac{f_1^2}{2f_2}$, où $f_1$ est le nombre de singletons (classes de failles vues une seule fois) et $f_2$ le nombre de doubletons. Utiliser l'annulation du terme de classes non observées ($f_1 = 0 \implies \frac{f_1^2}{2f_2} = 0$) comme règle d'arrêt séquentiel est mathématiquement invalide :
  1. Au tout début de l'audit ($t=0$, aucune faille observée), on a trivialement $f_1 = 0$, ce qui déclenche un arrêt immédiat avant même d'avoir échantillonné.
  2. Si les deux premières failles découvertes tombent par hasard dans la même catégorie ($f_1 = 0, f_2 = 1$), l'audit s'arrête prématurément alors que la couverture de l'espace des défauts est quasi nulle.
  3. Même dans la version corrigée pour échantillons finis $\frac{f_1(f_1-1)}{2(f_2+1)}$, l'estimateur s'annule dès que $f_1 \le 1$, ce qui ne garantit nullement l'exhaustivité en régime séquentiel à faible taille d'échantillon.

### 3. Faille méthodologique : Contrôle conforme en ligne sans étiquettes via PID (§ 2, Volet I)
* **Citation :** « *Le seuil conforme $q_t$ est mis à jour en ligne par un régulateur PID sur le flux de test non étiqueté via $e_t = \mathbb{1}[s_t > q_t] - \alpha$.* »
* **Preuve de la faille :** Dans la prédiction conforme adaptative / en ligne (Gibbs & Candès, ACI / Conformal PID Control), l'erreur de couverture $e_t$ doit mesurer l'écart entre le taux de fausses alertes (ou de non-couverture de la *vraie* étiquette $Y_t$) et la cible $\alpha$, ce qui requiert l'observation différée de la vérité terrain $Y_t$ (sous $H_0$). Ici, la mise à jour est effectuée aveuglément sur le **flux de test non étiqueté** (qui mélange $H_0$ et $H_1$) en asservissant simplement la fréquence globale de dépassement $\mathbb{P}(s_t > q_t)$ à $\alpha$. Conséquence fatale : lors d'une attaque soutenue (où la proportion de vrais positifs dépasse $\alpha$), le régulateur PID interprète les vraies détections ($s_t > q_t$) comme une erreur positive $e_t > 0$, augmente mécaniquement le seuil $q_t$, et **aveugle le détecteur** en plafonnant le taux d'alarme total (vrais + faux positifs) à $\alpha$.

### 4. Contradiction géométrique : Incompatibilité de la rétraction $C^1$ avec la préservation de la consigne affine (§ 1 Volet IV & § 2 Volet II)
* **Citation 1 (§ 1, Volet IV) :** « *La variété sûre de Koopman applique une rétraction radiale $C^1$ qui vaut l'identité exacte à l'intérieur du cône sûr.* »
* **Citation 2 (§ 2, Volet II) :** « *(ii) $\delta>0$ : $\rho(r)=r$ si $r\le R-\delta$, et $R-\delta e^{-(r-R+\delta)/\delta}$ sinon. On obtient $C^1$, avec $\|T^2x-Tx\|\le\delta/e$. Composition : $T=g_{c,R,\delta}\circ P_{\text{do}}$, où $g$ est centré en $c$. Comme $x-c\in U^\perp$ après $P_{\text{do}}$, la rétraction préserve la consigne : $U^\top T(x)=U^\top c$.* »
* **Citation 3 (Code Python `T_do` et `P_do`) :**
  ```python
  def P_do(X, U, c):
      U, _ = np.linalg.qr(U)
      return X - ((X - c) @ U) @ U.T
  def retraction(X, c, R, delta=0.0):
      V = X - c; r = np.linalg.norm(V, axis=-1, keepdims=True)
      ...
  ```
* **Preuve de la faille :** Il y a une erreur algébrique sur le centre de la rétraction :
  1. Le texte affirme que la projection $P_{\text{do}}(x) = x - UU^\top(x-c)$ satisfait $U^\top P_{\text{do}}(x) = U^\top c$, c'est-à-dire que $P_{\text{do}}$ fixe uniquement la composante dans le sous-espace $\mathrm{Im}(U)$ à $U^\top c$ (et non $c$ tout entier, à moins que $c \in \mathrm{Im}(U)$, c'est-à-dire $(I-UU^\top)c = 0$).
  2. Or, si $c$ possède une composante non nulle dans $U^\perp$ (soit $(I-UU^\top)c \neq 0$), alors pour $y = P_{\text{do}}(x)$, le vecteur $y - c = (I-UU^\top)(x-c)$ est bien dans $U^\perp$, mais la rétraction centrée en $c$, $T(x) = c + \frac{\rho(\|y-c\|)}{\|y-c\|}(y-c)$, vérifie bien $U^\top(T(x)-c) = 0$. En revanche, dans le code (`estimer_STD` / `vers_residuel`), $c_D = \mu + Qc_r$, tandis que $U_D = QU_r$. Ainsi $c_D - \mu \in \mathrm{Im}(Q)$, mais $\mu$ n'appartient pas à $\mathrm{Im}(U_D)$, donc $U_D^\top c_D \neq c_D$.
  3. Plus grave, la Citation 1 parle d'une rétraction qui vaut l'identité exacte à l'intérieur du « cône sûr » (et la Citation 2 sur la boule $r \le R - \delta$). Un cône (ou une boule fermée de rayon $R-\delta$) possède une frontière non lisse à l'origine/sommet pour le cône, et surtout, comme l'auteur le démontre lui-même au Lemme du § 2-II, une application qui vaut l'identité sur un sous-ensemble d'intérieur non vide ($r \le R-\delta$) et comprime l'extérieur dans une boule bornée $B(c, R)$ **ne peut pas être idempotente** si elle est $C^1$ ($\rho(\rho(r)) < \rho(r)$ pour tout $r > R-\delta$, d'où $T^2(x) \neq T(x)$).

### 5. Faille statistique et de détection : Vulnérabilité du ratio Max/Médiane et masquage `<PAD>` hors distribution (§ 2, Code Volet II)
* **Citation :** « *La détection du canal subliminal repose sur le ratio $\max_k \Psi(k) / \text{median}_j \Psi(j)$ après masquage `<PAD>` des seules clauses modales.* »
* **Preuve de la faille :** Cette procédure souffre d'une double faille :
  1. **Artefact hors-distribution (OOD) du masquage `<PAD>` :** Dans un modèle de langage causale (Transformer décodeur), remplacer à la volée des tokens internes à une phrase (« les seules clauses modales ») par des tokens `<PAD>` sans recalculer les positions ou sans attention mask adapté projette immédiatement les états cachés hors de la variété naturelle d'entraînement, créant des pics d'activation spurieux qui dominent $\max_k \Psi(k)$.
  2. **Instabilité et contournement de l'estimateur $\max / \text{median}$ :** Si $\Psi(j)$ peut s'approcher de $0$ (ou changer de signe, comme les coordonnées de Koopman contenant $\cos(zW+b)$ dans `DictKoopman`), la médiane $\text{median}_j \Psi(j)$ peut s'annuler ou être négative, faisant diverger le ratio vers $\pm\infty$. De plus, si un canal subliminal répartit son signal sur plus de $50\%$ des indices $j$, la médiane augmente proportionnellement au maximum (point de rupture de la médiane à $50\%$), masquant totalement l'anomalie.
