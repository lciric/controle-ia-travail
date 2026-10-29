# RAPPORT D'INSPECTION — ESSAIM `Sillon-1-Gouvernance-M3-Wald-Canaris-Bandit` (Vague 1/2)

Périmètre : étages M3 et M1 du script candidat, confrontés aux lois T4 (Fable T4 §1 : observable conjonctive ancrée au nul, zéro zone morte, contre-modèle obligatoire ; Argon T4 §2 : interdiction de l'interrogation adaptative du coffre-fort, $T^*$ défini ; Opus T2 : « la faille devient une porte »). Tout chiffre ci-dessous hors équations est `illustratif`.

---

`BUG_L_STAR_V2: [M3-Bandit] route_predator_m3 est un argmax figé sans exploration minimale $\varepsilon_t$ ni mise à jour de PREDATION_MATRIX`
`PREUVE_NON_CONFORMITE: Un bandit de prédation exige une politique $\pi_t$ avec $\varepsilon_t > 0$ pour tout $t$ (sinon le regret sur un bras jamais tiré est non borné et le bras « prédateur efficace » est inobservable). `cands[0][0]` tire toujours le premier candidat : la matrice n'apprend rien, la Récompense de Brier calculée en aval n'est jamais réinjectée, et la condition « exploration minimale $\varepsilon_t$ » de la fusée est violée en tout $t$. Pire : l'ordre de `cands` étant déterministe, le défenseur peut prédire son attaquant (fuite Kerckhoffs vers M3-Canaris).`
`CORRECTIF_PYTHON_EXACT:`
```python
import math, random

def epsilon_t(t, n_arms, eps_min=0.05):
    # exploration minimale strictement positive, décroissante en O(sqrt(K ln t / t))
    return max(eps_min, min(1.0, math.sqrt(n_arms * math.log(max(2, t)) / max(1, t))))

class PredationBandit:
    def __init__(self, arms, seed):
        self.arms = list(arms)
        self.n = {a: 0 for a in self.arms}
        self.q = {a: 0.0 for a in self.arms}
        self.t = 0
        self.rng = random.Random(seed)

    def select(self):
        self.t += 1
        eps = epsilon_t(self.t, len(self.arms))
        if self.rng.random() < eps:
            return self.rng.choice(self.arms), eps
        best = max(self.q.values())
        ties = [a for a in self.arms if self.q[a] == best]
        return self.rng.choice(ties), eps        # bris d'égalité aléatoire, jamais cands[0][0]

    def update(self, arm, reward):
        self.n[arm] += 1
        self.q[arm] += (reward - self.q[arm]) / self.n[arm]

PREDATION_BANDITS = {}  # un bandit par défenseur, remplace PREDATION_MATRIX statique

def route_predator_m3(defender, cands, round_seed):
    arms = [c[0] for c in cands if c[0] != defender]
    key = defender
    if key not in PREDATION_BANDITS:
        PREDATION_BANDITS[key] = PredationBandit(arms, seed=hash((defender, round_seed)) & 0xFFFFFFFF)
    arm, eps = PREDATION_BANDITS[key].select()
    return arm, eps

def feedback_predator_m3(defender, arm, reward):
    PREDATION_BANDITS[defender].update(arm, reward)
```

---

`BUG_L_STAR_V2: [M3-Brier] unilateral_anti_failure_reward n'est ni borné ni unilatéral : mu_conf non clampé, coût constant sans effet sur l'argmax`
`PREUVE_NON_CONFORMITE: (i) Sans projection de $\mu$ sur $[0,1]$, $\mu=2$ avec $y=1$ donne $1-(2-1)^2=0$ et $\mu=-1$ avec $y=0$ donne $-1$ : la règle de score cesse d'être propre hors du domaine et un prédateur peut émettre une confiance absurde sans sanction supérieure à celle d'un $\mu$ légitime. (ii) `gamma*cost_norm` est une constante : elle ne dépend pas du bras, donc n'intervient pas dans le classement des bras du bandit — le terme « coût » est décoratif. (iii) Le terme « unilatéral » du T4 signifie que la surconfiance ($\mu>y$, c.-à-d. annonce de corpus propre réfutée) doit être pénalisée davantage que la sous-confiance ; la formule est symétrique en Brier pur.`
`CORRECTIF_PYTHON_EXACT:`
```python
def unilateral_anti_failure_reward(y_success, mu_conf, tokens_used, token_budget,
                                   gamma=0.10, lam=0.50):
    if y_success not in (0, 1):
        raise ValueError("y_success doit être 0/1")
    mu = min(1.0, max(0.0, float(mu_conf)))          # domaine de Brier
    if token_budget <= 0:
        raise ValueError("token_budget > 0 requis")
    brier = (mu - y_success) ** 2                    # score propre, borné dans [0,1]
    overconf = max(0.0, mu - y_success) ** 2         # hinge unilatéral (surconfiance seule)
    cost_norm = min(1.0, tokens_used / token_budget) # coût dépendant de l'action
    return 1.0 - brier - lam * overconf - gamma * cost_norm   # borné dans [-lam-gamma, 1]
```

---

`BUG_L_STAR_V2: [M3-L*v2] score_jev_l_star_v2 autorise 20 % de troncature (kappa ≥ 0,80), bannit les contrôles négatifs et ne retranche pas l'annexe des canaris`
`PREUVE_NON_CONFORMITE: La loi T4 (Fable, réserve 7 ; Opus, E0-Méta M1/M3) impose « livré complet, sans troncature » : le seuil de recevabilité doit être $\kappa \ge 1 - \eta$ avec $\eta$ au niveau du bruit d'encodage, non $0{,}80$. Le score $\text{rigor}+\text{falsifiable\_duels}-\text{hypothesis\_as\_result}$ bannit `negative_controls` alors que chaque correctif T4 exige « contre-modèle rival nommé » : un texte sans contrôle négatif devrait être pénalisé, non récompensé par l'absence du terme. Enfin, `len(txt)` inclut les canaris concaténés : $\kappa$ est gonflé artificiellement par du texte qui n'appartient pas au candidat.`
`CORRECTIF_PYTHON_EXACT:`
```python
import re

def strip_canaries(txt, canary_ids):
    for cid in canary_ids:
        txt = re.sub(r"\[\[CAN:%s\]\].*?\[\[/CAN\]\]" % re.escape(cid), "", txt, flags=re.S)
    return txt

def score_jev_l_star_v2(txt, prev_len, canary_ids, eta=0.02, w_neg=1.0, w_hyp=1.0):
    core = strip_canaries(txt, canary_ids)
    kappa = len(core) / max(1, prev_len)
    if kappa < 1.0 - eta:                # troncature : porte fermée, verdict défini
        return {"verdict": "INVALIDE-troncature", "kappa": kappa, "score": None}
    rigor = count_rigor_markers(core)
    duels = count_falsifiable_duels(core)
    hyp_as_result = count_hypothesis_as_result(core)
    neg_controls = count_negative_controls(core)      # contre-modèles rivaux nommés
    score = rigor + duels + w_neg * neg_controls - w_hyp * hyp_as_result
    if neg_controls == 0:
        return {"verdict": "INVALIDE-sans-contre-modele", "kappa": kappa, "score": score}
    return {"verdict": "RECEVABLE", "kappa": kappa, "score": score}
```

---

`BUG_L_STAR_V2: [M3-Canaris] BLIND_CANARIES_M3 sont fixes, en fin de texte, sous un titre voyant : ils sont aveugles pour personne`
`PREUVE_NON_CONFORMITE: Un canari « aveugle » doit être indiscernable du corpus pour le défenseur **et** pour le prédateur (Kerckhoffs) : trois phrases identiques à chaque tour, placées au même endroit sous « ANNEXE DE CALIBRATION MÉTHODOLOGIQUE », sont mémorisées dès le tour 2. $\rho_{\text{can}}$ converge alors vers 1 par reconnaissance et non par détection : la condition $\rho_{\text{can}}\ge 2/3$ du compteur de Wald est satisfaite trivialement, ce qui vide de sens le bonus $2{,}5\,\rho_{\text{can}}$. Il faut un pool, un tirage secret par tour, une insertion à position aléatoire sans balise visible dans le texte exposé, et une clé de révélation détenue seulement par M3.`
`CORRECTIF_PYTHON_EXACT:`
```python
import hashlib, random

CANARY_POOL = [  # phrases plausibles contenant chacune une erreur détectable (≥ 12, illustratif)
    "Le test de McNemar est ici appliqué à des échantillons indépendants (référence à vérifier).",
    "La borne de Ville garantit un contrôle de l'erreur de type II à niveau alpha.",
    "Le d_z de Cohen est invariant au changement de signe du registre.",
    # ... compléter le pool
]

def plant_blind_canaries(txt, round_id, master_secret, k=3):
    seed = int(hashlib.sha256(f"{master_secret}:{round_id}".encode()).hexdigest(), 16)
    rng = random.Random(seed)
    chosen = rng.sample(range(len(CANARY_POOL)), k)
    paras = [p for p in txt.split("\n\n") if p.strip()]
    ledger = []                                      # conservé par M3 seul
    for idx in chosen:
        pos = rng.randrange(1, max(2, len(paras)))   # jamais en tête, jamais en annexe fixe
        paras.insert(pos, CANARY_POOL[idx])
        ledger.append((idx, pos))
    return "\n\n".join(paras), ledger                # aucun titre, aucune balise exposée

def rho_can_from_report(report_failles, ledger):
    hits = 0
    for idx, _ in ledger:
        key = CANARY_POOL[idx][:40]
        if any(key in f for f in report_failles):
            hits += 1
    return hits / len(ledger)
```

---

`BUG_L_STAR_V2: [M1-Dolev] Tours 2..4 : un seul prédateur par défenseur, aucune attaque conjointe ; l'isolation de Dolev n'est pas implémentée`
`PREUVE_NON_CONFORMITE: L'isolation de Dolev exige $m\ge 2$ attaquants par défenseur, chacun sur un canal indépendant (aucun ne voit l'attaque de l'autre avant émission), et le défenseur reçoit l'union. Avec un seul prédateur, une faille non vue par ce prédateur est structurellement une zone morte (règle B4), et un prédateur complaisant suffit à faire converger le compteur. La loi T4 nomme explicitement « Fable+Argon contre Opus ».`
`CORRECTIF_PYTHON_EXACT:`
```python
def dolev_assign(branches, round_id, seed):
    rng = random.Random(seed + 7919 * round_id)
    plan = {}
    for d in branches:
        attackers = [b for b in branches if b != d]
        rng.shuffle(attackers)
        plan[d] = attackers[:max(2, len(branches) - 1)]  # ≥ 2 attaquants, tous ici (3 branches)
    return plan

def run_attacks_dolev(plan, defender_texts, attack_fn):
    reports = {}
    for d, attackers in plan.items():
        isolated = []
        for a in attackers:
            # canal isolé : l'attaquant ne reçoit que le texte du défenseur, jamais les autres rapports
            isolated.append((a, attack_fn(a, defender_texts[d])))
        reports[d] = isolated                         # union livrée au défenseur après clôture
    return reports

def merge_failles(isolated_reports):
    seen, merged = set(), []
    for a, failles in isolated_reports:
        for f in failles:
            key = f.strip().lower()[:80]
            if key not in seen:
                seen.add(key); merged.append((a, f))
    return merged
```

---

`BUG_L_STAR_V2: [M1-Wald-Ville] Convergence déclarée au premier tour à 0 faille ; barrière de Ville $\ln(n_{\text{adm}}/\alpha)$ absente ; pénalité ×1,5 sur $S^-$ quand $F_t\ge F_{t-1}$ absente ; bonus $2{,}5\,\rho_{\text{can}}$ non borné`
`PREUVE_NON_CONFORMITE: Un SPRT (Wald, référence à vérifier) ne s'arrête que lorsque la somme des log-vraisemblances franchit $A=\ln\frac{1-\beta}{\alpha}$ ; l'inégalité de Ville borne $P(\sup_t e^{S_t}\ge 1/\alpha)\le\alpha$ pour une supermartingale de test, et avec $n_{\text{adm}}$ règles d'arrêt admissibles la barrière devient $\ln(n_{\text{adm}}/\alpha)$ (Bonferroni). Le script ajoute $2{,}5\,\rho_{\text{can}}$ (jusqu'à $2{,}5$ par tour) et déclare `converged` dès un tour propre : avec $\alpha=0{,}01$, $n_{\text{adm}}=3$, la barrière vaut $\ln 300\approx 5{,}70$, jamais atteinte en un tour par un incrément de LLR honnête. La stagnation ($F_t\ge F_{t-1}$) devrait pénaliser $S^-$ (×1,5) ; elle est ignorée, donc un défenseur qui réintroduit autant de failles qu'il en corrige n'est jamais sanctionné.`
`CORRECTIF_PYTHON_EXACT:`
```python
import math

def ville_barrier(alpha, n_adm):
    return math.log(n_adm / alpha)

class WaldVilleDouble:
    def __init__(self, alpha=0.01, n_adm=3, p0=0.5, p1=0.1, k_min=2, rho_min=2/3):
        self.A = ville_barrier(alpha, n_adm)
        self.llr_clean = math.log((1 - p1) / (1 - p0))     # > 0 : tour sans faille
        self.llr_dirty = math.log(p1 / p0)                 # < 0 : tour avec faille(s)
        self.S_plus, self.S_minus = 0.0, 0.0
        self.F_prev, self.clean_streak = None, 0
        self.k_min, self.rho_min = k_min, rho_min
        self.converged = False

    def step(self, F_t, rho_can):
        # témoin aveugle : un tour "propre" sans détection des canaris n'est pas une preuve
        if F_t == 0 and rho_can >= self.rho_min:
            self.S_plus += self.llr_clean * rho_can        # incrément borné ≤ llr_clean
            self.clean_streak += 1
        else:
            pen = 1.5 if (self.F_prev is not None and F_t >= self.F_prev) else 1.0
            if F_t == 0:                                    # propre mais canaris non vus : évidence nulle
                self.S_minus += pen * abs(self.llr_dirty) * (1 - rho_can)
            else:
                self.S_minus += pen * abs(self.llr_dirty) * F_t
            self.clean_streak = 0
        self.F_prev = F_t
        S = self.S_plus - self.S_minus
        self.converged = (S >= self.A) and (self.clean_streak >= self.k_min)
        self.rejected = (S <= -self.A)
        return {"S": S, "A": self.A, "converged": self.converged, "rejected": self.rejected}
```

---

`BUG_L_STAR_V2: [M3/M1-Boucle] La Récompense de Brier, le bandit et le compteur de Wald ne sont pas raccordés : trois états sans tenseur commun`
`PREUVE_NON_CONFORMITE: La fusée exige qu'un tour produise une observation unique $(F_t,\rho_{\text{can}},\mu)$ qui alimente simultanément (i) le compteur de Wald-Ville, (ii) la récompense du prédateur, (iii) la mise à jour du bandit. Dans le script, `route_predator_m3` ne consomme rien, `unilateral_anti_failure_reward` n'est appelée nulle part dans la boucle M1, et `converged` est calculé en aval sur un état disjoint. Chaque étage est donc « correct » isolément mais la gouvernance est non fermée (règle B4 : zone morte entre étages).`
`CORRECTIF_PYTHON_EXACT:`
```python
def governance_round(round_id, branches, texts, master_secret, seed, wald, attack_fn,
                     confidence_fn, token_budget):
    plan = dolev_assign(branches, round_id, seed)
    planted, ledgers = {}, {}
    for d in branches:
        planted[d], ledgers[d] = plant_blind_canaries(texts[d], round_id, master_secret)
    reports = run_attacks_dolev(plan, planted, attack_fn)
    out = {}
    for d in branches:
        merged = merge_failles(reports[d])
        failles_txt = [f for _, f in merged]
        rho = rho_can_from_report(failles_txt, ledgers[d])
        canary_keys = {CANARY_POOL[i][:40] for i, _ in ledgers[d]}
        real = [f for f in failles_txt if not any(k in f for k in canary_keys)]
        F_t = len(real)
        state = wald[d].step(F_t, rho)
        for a, failles in reports[d]:
            y = 1 if any(not any(k in f for k in canary_keys) for f in failles) else 0
            mu, tokens = confidence_fn(a, d)
            r = unilateral_anti_failure_reward(y, mu, tokens, token_budget)
            if d in PREDATION_BANDITS:
                feedback_predator_m3(d, a, r)
        out[d] = {"F_t": F_t, "rho_can": rho, **state}
    return out
```

---

Synthèse du sillon : 7 non-conformités, dont 3 fatales pour la gouvernance (bandit figé, convergence sans barrière de Ville, canaris non aveugles) qui, combinées, permettent à un défenseur de « converger » au tour 2 sans qu'aucune évidence sequentielle valide n'ait été accumulée. Les correctifs ci-dessus ferment la boucle sur un tenseur d'observation commun $(F_t,\rho_{\text{can}},\mu,\text{coût})$ et rendent chaque sortie définie (zéro zone morte).

FIN-INSPECTION-ESSAIM
