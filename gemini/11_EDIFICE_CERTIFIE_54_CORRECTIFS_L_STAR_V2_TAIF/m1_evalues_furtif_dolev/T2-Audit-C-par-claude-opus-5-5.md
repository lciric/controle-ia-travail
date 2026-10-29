FAILLES_PROUVEES_PAR_AUDITEUR: 9

Ce décompte est le mien. Je n'ai repris aucun chiffre déclaré par l'auteur. Je ne compte que les failles que je peux démontrer, par un calcul ou un contre-exemple.

---

## Failles retenues

### F1 — Volet I : le contraste à k=0 est dégénéré par causalité
- **Le problème.** Les trois conditions (σ_r0, P2, P4) partagent « exactement le même préfixe lexical jusqu'en k=0 », sans modification des tokens de surface. Or un transformeur causal déterministe calcule h_{l,k} = f_θ(x_{1..k}).
- **Conséquence.** À poids et préfixe identiques, on obtient s^(P2) = s^(P4) = σ_r0. Donc Δ_b = −σ_{r,b}0. Le terme « intention » (P2 − P4) est identiquement nul, et le test ne mesure plus aucune intention.
- **Dilemme.**
  - Si les conditions diffèrent réellement (instruction latente dans le contexte, poids distincts), l'hypothèse « même préfixe » est fausse.
  - Si elles ne diffèrent pas, la dissociation revendiquée est vide.
- **Dans le code.** `std_delta + 1e-15` masque le cas s_Δ = 0 au lieu de le rejeter. Pour un Δ constant non nul, d_z ≈ 1015.

### F2 — Volet II : le Do-Clamp déployé n'est pas idempotent
- **Ce qui est correct.** La preuve P_do2 = P_do est valide pour l'application affine seule.
- **Ce qui ne l'est pas.** L'opérateur réellement appliqué est C(u) = μ* + R_{C1}(P0(u − μ*)). Pour ρ > R, la norme image vaut ρ' = R(1 + tanh((ρ−R)/R)) avec R < ρ' < ρ. Comme v' reste dans Im P0, une seconde application rétracte à nouveau.
- **Contre-exemple** (R = 0,5, ρ = 1) :
  - ρ' = 0,5(1 + tanh 1) ≈ 0,881 ;
  - ρ'' = 0,5(1 + tanh 0,762) ≈ 0,821 ≠ ρ'.
  - Donc C∘C ≠ C.
- **Conséquence.** L'étiquette « Affine Idempotent » ne s'applique pas à l'opérateur composé. Par ailleurs, la borne d'amplitude obtenue est 2R, et non R.

### F3 — Volet II : le bras contrôle `rand-parc` est mal apparié et non parcimonieux
- **Support.** u − P_do(u) = (I − P0)(u − μ*) appartient au noyau d'un projecteur oblique dense. Génériquement ‖·‖0 = m : la perturbation « parcimonieuse » est en fait pleine.
- **Normes incohérentes.**
  - k_supp est calculé sur la correction **non rétractée** P_do(u) − u.
  - ‖δ_rand‖_∞ est calé sur la correction **rétractée** R(·) + μ* − u.
  - Le contrôle n'est donc apparié à aucun opérateur unique.
- **Conséquence.** Il ne peut pas isoler l'effet géométrique revendiqué.

### F4 — Volet III : le mélange de la JSD est incohérent avec la correction Miller-Madow
- **L'incohérence.** Le texte pose m = (p̂ + q̂)/2, mais « estimé sur l'échantillon joint N_P + N_Q ». La loi empirique jointe vaut (N_P p̂ + N_Q q̂)/(N_P + N_Q), ce qui diffère de (p̂ + q̂)/2 dès que N_P ≠ N_Q.
  - Exemple : N_P = 100, N_Q = 900 donne des poids 0,1 / 0,9 au lieu de 0,5 / 0,5.
- **Effet sur la correction.** Le terme (K̂+ − 1)/(2N ln 2) avec N = N_joint suppose un échantillon multinomial unique de la loi entropisée. Ce n'est pas le cas de (p̂ + q̂)/2 quand les effectifs sont inégaux.
- **Conséquence.** La correction de biais n'annule plus le biais du plug-in sous H0, et le seuil de 0,05 bit perd sa calibration.
- **Portée.** La formule n'est cohérente que si N_P = N_Q, contrainte jamais énoncée.

### F5 — Seuil conforme en ligne régulé par PID sur un flux non étiqueté
- **La règle.** e_t = 1[s_t > q_t] − α utilise le taux d'alarme, et non une erreur de couverture : sans étiquettes, il n'y a aucun signal de mauvaise couverture.
- **Conséquence.** Le régulateur force le taux d'alarme vers α quelle que soit la réalité. Une dérive adverse persistante est absorbée par la remontée de q_t : le détecteur s'aveugle exactement sur l'attaque visée. Toute garantie de type conforme est perdue.
- **Contradictions internes.**
  - La règle contredit le seuil q_α « gelé hors-ligne » énoncé au Volet III.
  - Insérée en prose dans le code Python, elle provoque une `SyntaxError`.

### F6 — Volet IV : test de Jonckheere-Terpstra appliqué à une série autocorrélée
- **L'hypothèse violée.** Var(J) = [N2(2N+3) − Σni2(2ni+3)]/72 n'est exacte que pour des observations indépendantes (et sans ex-aequo).
- **La contradiction.** Le document affirme lui-même que s_{d,t} « présente une autocorrélation native qui fausserait » la détection. Il blanchit pour le CUSUM, mais pas pour le JT.
- **Conséquence.** Une autocorrélation positive sous-estime Var(J) et gonfle Z_JT. On obtient un excès de révocations (Π → ∅) sous H0.

### F7 — Volet V : règle d'arrêt dégénérée fondée sur Chao1
- **Indéfinition.** f12/(2f2) vaut 0/0 si f2 = 0, notamment dès le départ. La forme corrigée f1(f1−1)/(2(f2+1)) s'annule déjà pour f1 = 1.
- **Mauvaise interprétation.** Chao1 est une **borne inférieure** de la richesse. Un terme non vu estimé à 0 ne certifie pas l'exhaustivité de l'audit.
- **Arrêt optionnel.** Stopper dès que f1 = 0 est un arrêt optionnel non contrôlé, qui biaise les tests CMH/TOST calculés ensuite.

### F8 — Volet V : HMP de Wilson présentée comme valide « sous dépendance arbitraire »
- **Ce que dit Wilson (2019).** La validité y est asymptotique, avec M grand et des hypothèses de dépendance restreintes. Le seuil p̊ ≤ α est anti-conservateur, d'où la calibration de type Landau proposée par Wilson.
- **Sous dépendance réellement arbitraire.** Vovk & Wang (2020) montrent que la moyenne harmonique doit être multipliée par un facteur de l'ordre de e·ln M pour rester valide. Avec M = 5 (petit), aucune garantie asymptotique ne tient sans correction.
- **Remèdes.** Utiliser ce facteur, ou un Bonferroni 5·min pm.

### F9 — Détection du canal subliminal par masquage partiel
- **Masquage incomplet.** Masquer « les seules clauses modales » laisse intacts les porteurs stéganographiques usuels : choix lexicaux, ponctuation, formatage, ordre des champs. Le canal survit au masquage par construction.
- **Ratio non calibré.** max/médiane n'a aucune distribution nulle, donc aucun taux de fausse alarme contrôlé.
- **Ambiguïté de notation.** Ψ désigne déjà le relèvement de Koopman, à valeurs dans Rm. Un ratio de vecteurs n'est pas défini.

---

## Remarques secondaires (non comptées)
- **CUSUM.** La paire k = 0,5, h = 4,77 donne bien ARL0 ≈ 370 en **bilatéral**. Mais la règle de révocation ne teste que S+ : l'ARL0 effectif est alors d'environ 740, et les dérives descendantes sont ignorées.
- **Commit-Reveal.** `bytes(A) ‖ bytes(B)` n'engage ni les formes ni le dtype. Encoder longueur, forme et dtype rendrait l'engagement non ambigu.
- **Sous-espace S_TD.** « < 1 % des paramètres » (intro) et « r/D < 1 % » de la dimension du flux résiduel (§2) mesurent deux choses différentes.
- **Zone de rétraction.** La rétraction est l'identité sur une **boule** ‖v‖ ≤ R, et non sur un « cône ».
- **Code.** Le script est tronqué (`pe`) et contient de la prose injectée. L'affirmation « directement exécutable » est donc fausse, mais ce point est logiciel et non mathématique.
- **Antériorité.** Toutes les références sont marquées « à vérifier » (dont les ID 2026 et Jhaveri/Tagliabue sans identifiant). « White space 100 % vierge » est une affirmation non démontrée, sans contre-exemple d'antériorité que je puisse établir.

## Éléments vérifiés et sains (non signalés)
- **Volet I :**
  - facteur de Hedges J(df) exact et son approximation 1 − 3/(4df − 1) ;
  - p-valeur exacte par retournement de signe (identité incluse, inégalité ≥).
- **Volet II :**
  - preuve d'idempotence de P_do seul ;
  - continuité et raccord C1 en ρ = R (dérivées radiale et tangentielle égales à 1).
- **Volet III :**
  - Merkle préfixé 0x00/0x01, conforme au RFC 6962 ;
  - scellement avant rapport ;
  - quantile conforme ⌈(n+1)(1−α)⌉/n gelé hors-ligne.
- **Volet IV :**
  - estimateur φ̂1 de Yule-Walker ;
  - moments E[J] et Var(J) du JT (sous indépendance) ;
  - monotonie Π_{d+1} = Π_d ∩ A_{d+1}.
- **Volet V :**
  - espérance et variance hypergéométriques du CMH, correction de continuité, OR de Mantel-Haenszel ;
  - équation quadratique et variance de Breslow-Day ;
  - bornes de Wilson, intervalle de Newcombe à 90 % équivalent au TOST à α = 0,05 ;
  - N = 9 ≥ 3f + 1 ;
  - panel de stratification externe gelé.
- **Introduction :** score de Brier −(μ − y)2, règle propre avec perte nulle en (0, 0).
