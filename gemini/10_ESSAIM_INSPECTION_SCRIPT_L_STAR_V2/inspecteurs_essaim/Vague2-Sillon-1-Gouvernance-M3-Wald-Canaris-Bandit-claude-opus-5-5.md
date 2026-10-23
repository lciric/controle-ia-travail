BUG_L_STAR_V2: [Sillon-1-M3-L*v2] `kappa = len(txt)/prev_len` est indéfini quand `prev_len == 0`, et ce cas est documenté dans le corpus

PREUVE_NON_CONFORMITE: Opus T2 l'écrit noir sur blanc : « Le texte de la Branche B au Tour 1 […] contient 0 caractère ». Au Tour 2, `prev_len = 0` produit donc deux issues possibles :
- un `ZeroDivisionError`, qui fait planter M3 sur la seule branche qui avait justement besoin d'être notée ;
- si le code contourne la division par un `or 1` ou un `max(prev_len, 1)`, `kappa` devient énorme et la branche passe la porte anti-troncature sans aucun contrôle.

Dans les deux cas, la porte E0-Méta M1 d'Opus (« texte vide ⇒ `INVALIDE-instrument` ») n'a pas de verdict défini, ce qui crée une zone morte. Ce défaut est distinct du seuil 0,80 déjà signalé : il concerne le domaine de définition du ratio, pas sa valeur.

CORRECTIF_PYTHON_EXACT:
```python
import re, unicodedata

def _nfc(s):
    return unicodedata.normalize("NFC", s or "")

def kappa_safe(txt, prev_txt):
    n, n0 = len(_nfc(txt).strip()), len(_nfc(prev_txt).strip())
    if n0 == 0:
        return None                      # aucune référence : ratio non défini
    return n / n0

def gate_completude(txt, prev_txt, sections_requises, kappa_min):
    t = _nfc(txt)
    if not t.strip():
        return ("INVALIDE-instrument", ["texte vide"])
    manquantes = [s for s in sections_requises if not re.search(s, t, re.I | re.M)]
    if manquantes:
        return ("INVALIDE-instrument", manquantes)
    k = kappa_safe(txt, prev_txt)
    if k is None:
        return ("STRUCTUREL-SEUL", [])   # verdict défini, sans ratio
    return ("OK", []) if k >= kappa_min else ("TRONQUE", [f"kappa={k:.3f}"])
```

---

BUG_L_STAR_V2: [Sillon-1-M3-L*v2] `kappa` ne mesure que la longueur : la duplication et le remplissage satisfont la porte

PREUVE_NON_CONFORMITE: `len(txt)` compte les caractères, pas l'information.
- Un texte tronqué de moitié dont on duplique la partie restante obtient `kappa ≈ 1`.
- Le compteur `rigor + falsifiable_duels` compte les occurrences : dupliquer un paragraphe double aussi le score.

La porte anti-troncature est donc contournable par une simple redondance. C'est l'inverse de « la faille devient une porte ».

CORRECTIF_PYTHON_EXACT:
```python
import re, zlib, hashlib, unicodedata

def contenu_informatif(txt, min_len=40):
    t = unicodedata.normalize("NFC", txt or "")
    vus, garde = set(), []
    for p in re.split(r"\n\s*\n", t):
        q = re.sub(r"\s+", " ", p).strip().lower()
        if len(q) < min_len:
            continue
        h = hashlib.sha256(q.encode("utf-8")).hexdigest()
        if h not in vus:
            vus.add(h)
            garde.append(q)
    corps = "\n".join(garde).encode("utf-8")
    return len(zlib.compress(corps, 9)) if corps else 0

def kappa_informatif(txt, prev_txt):
    n0 = contenu_informatif(prev_txt)
    return None if n0 == 0 else contenu_informatif(txt) / n0

def compter_unique(motifs_re, txt):
    paras = {re.sub(r"\s+", " ", p).strip().lower()
             for p in re.split(r"\n\s*\n", txt or "")}
    return sum(1 for p in paras if re.search(motifs_re, p))
```

---

BUG_L_STAR_V2: [Sillon-1-M3-Gouvernance] `n_real_failles` peut être alimenté par l'en-tête autodéclaré `FAILLES_RESIDUELLES_APRES_CORRECTION: 0`

PREUVE_NON_CONFORMITE: Les trois défenseurs (Fable T4, Opus T2, Argon T4) déclarent tous `0`. Opus précise lui-même : « auto-évaluation […] Elle n'est pas auditée, et l'équipe rouge reste juge ».

Si le compteur de Wald lit cette valeur, alors :
- le défenseur contrôle directement l'événement qui fait converger le système (Goodhart pur) ;
- la condition `n_real_failles == 0` est satisfaite par construction.

Ce défaut est orthogonal à la barrière de Ville : il concerne la **provenance** de l'observation, pas son seuil. Le compte doit être reconstruit à partir des seuls verdicts des prédateurs validés par l'arbitre. L'en-tête ne sert qu'à mesurer une sous-déclaration.

CORRECTIF_PYTHON_EXACT:
```python
import re
HEADER_RE = re.compile(r"FAILLES_RESIDUELLES_APRES_CORRECTION\s*:\s*(\d+)")

def n_failles_reelles(verdicts, defenseur):
    # verdicts : [{"defenseur","id","fatale","valide_par_juge","canari"}]
    return len({v["id"] for v in verdicts
                if v["defenseur"] == defenseur and v["fatale"]
                and v["valide_par_juge"] and not v["canari"]})

def audit_autodeclaration(txt, n_reel):
    m = HEADER_RE.search(txt or "")
    auto = int(m.group(1)) if m else None
    return {"auto": auto, "reel": n_reel,
            "sous_declaration": auto is not None and auto < n_reel,
            "utilisable_par_wald": False}   # jamais une entrée du compteur
```

---

BUG_L_STAR_V2: [Sillon-1-M3-Canaris] `rho_can` mesure la sensibilité seule, sans spécificité : un prédateur qui signale tout obtient `rho_can = 1`

PREUVE_NON_CONFORMITE: `rho_can = canaris_détectés / n_canaris` ne compte que les vrais positifs. Un prédateur paranoïaque qui marque chaque paragraphe comme faille obtient `rho_can = 1`, passe le seuil `≥ 2/3` et débloque le bonus de Wald.

Fable T4 cite pourtant l'indice de Youden `J = sensibilité − taux de faux positifs` dans ses références. Il faut des **leurres sains** (passages corrects insérés aux mêmes conditions) pour estimer le taux de faux positifs. Ce défaut est orthogonal à la visibilité ou à la fixité des canaris : même parfaitement aveugles, ils ne mesurent pas la vigilance sans contrôle négatif.

CORRECTIF_PYTHON_EXACT:
```python
def youden_vigilance(signalements_ids, canaris_ids, leurres_ids):
    s = set(signalements_ids)
    if not canaris_ids or not leurres_ids:
        return None                       # vigilance non mesurable
    tpr = sum(c in s for c in canaris_ids) / len(canaris_ids)
    fpr = sum(l in s for l in leurres_ids) / len(leurres_ids)
    return tpr - fpr                      # J dans [-1, 1]
```

---

BUG_L_STAR_V2: [Sillon-1-M3-Canaris] Avec 3 canaris, `rho_can ≥ 2/3` n'a aucune valeur statistique

PREUVE_NON_CONFORMITE: `rho_can` ne peut prendre que les valeurs {0, 1/3, 2/3, 1}.
- Pour 2 détections sur 3, la borne inférieure unilatérale de Clopper-Pearson à α = 0,05 vaut **≈ 0,135**. Cette valeur se vérifie en résolvant `3p² − 2p³ = 0,05`.
- Même 3 sur 3 ne donne qu'une borne de 0,05^(1/3) ≈ 0,368.

Le seuil 2/3 est donc compatible avec un prédateur dont la vigilance réelle est d'environ 13 %. Pour garantir une borne d'au moins 0,5 avec un sans-faute, il faut au moins **5 canaris** (0,05^(1/5) ≈ 0,549).

CORRECTIF_PYTHON_EXACT:
```python
from math import comb

def binom_sf(k, n, p):
    return sum(comb(n, i) * p**i * (1 - p)**(n - i) for i in range(k, n + 1))

def cp_lower(k, n, alpha=0.05):
    if k == 0:
        return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if binom_sf(k, n, mid) < alpha:
            lo = mid
        else:
            hi = mid
    return lo

def n_canaris_min(seuil=0.5, alpha=0.05, nmax=500):
    for n in range(1, nmax + 1):
        if cp_lower(n, n, alpha) >= seuil:
            return n
    return None

def vigilance_suffisante(k, n, seuil=0.5, alpha=0.05):
    return n >= n_canaris_min(seuil, alpha) and cp_lower(k, n, alpha) >= seuil
```

---

BUG_L_STAR_V2: [Sillon-1-M3-Canaris] Détection par simple présence du canari, et double comptage dans `n_real_failles`

PREUVE_NON_CONFORMITE: Deux problèmes se combinent.
1. **Fausse détection.** Si un canari est jugé « détecté » dès que son texte apparaît dans le rapport du prédateur, il suffit de citer l'annexe pour être crédité, sans aucun diagnostic.
2. **Double comptage.** Un canari correctement signalé comme faille fatale est compté à la fois dans `rho_can` et dans `n_real_failles`.

La même observation pousse alors simultanément vers la convergence (via `rho_can`) et contre elle (via `n_real_failles`). Il faut une partition disjointe des signalements par chevauchement d'intervalles de texte, avec un diagnostic attendu par canari.

CORRECTIF_PYTHON_EXACT:
```python
def classer_signalements(signalements, spans_canaris):
    # signalement : {"debut","fin","diagnostic"} ; spans_canaris : {id: (a, b, diag_attendu)}
    detectes, reels, ambigus = set(), [], []
    for s in signalements:
        hit = next((cid for cid, (a, b, _) in spans_canaris.items()
                    if s["debut"] < b and a < s["fin"]), None)
        if hit is None:
            reels.append(s)
        elif s.get("diagnostic") == spans_canaris[hit][2]:
            detectes.add(hit)
        else:
            ambigus.append(s)   # ni détection, ni faille réelle
    return detectes, reels, ambigus
```

---

BUG_L_STAR_V2: [Sillon-1-M3-Canaris/Kerckhoffs] Pas d'engagement cryptographique sur le placement, et les canaris fuient vers le défenseur par le rapport rouge

PREUVE_NON_CONFORMITE: Selon le principe de Kerckhoffs, l'algorithme d'insertion peut être public mais la clé de placement doit rester secrète **et** être engagée avant le tour. Sans cela, l'orchestrateur peut repositionner les canaris *a posteriori* pour favoriser une branche, et personne ne peut le prouver.

Par ailleurs, les rapports des prédateurs qui citent les canaris sont renvoyés au défenseur au tour suivant. Le défenseur apprend ainsi la forme exacte des canaris, et sa détection devient de la mémorisation. Ce défaut porte sur l'engagement et sur l'assainissement du canal de retour, non sur la fixité déjà signalée.

CORRECTIF_PYTHON_EXACT:
```python
import hmac, hashlib, secrets, random

def engager_canaris(frontieres_paragraphes, n, cle=None):
    cle = cle or secrets.token_bytes(32)
    graine = hmac.new(cle, b"canaris-M3", hashlib.sha256).digest()
    rng = random.Random(graine)
    positions = sorted(rng.sample(list(frontieres_paragraphes), n))
    engagement = hashlib.sha256(cle + repr(positions).encode()).hexdigest()
    return cle, positions, engagement        # seul l'engagement est publié avant le tour

def verifier_revelation(cle, positions, engagement):
    calc = hashlib.sha256(cle + repr(positions).encode()).hexdigest()
    return hmac.compare_digest(calc, engagement)

def assainir_retour(texte, spans_canaris):
    for a, b in sorted(spans_canaris, reverse=True):
        texte = texte[:a] + texte[b:]
    return texte                              # à appliquer au texte ET aux rapports rouges
```

---

BUG_L_STAR_V2: [Sillon-1-M3-Brier] Une fois calibrée, la récompense espérée vaut `p²` : elle mesure la faiblesse du défenseur, pas l'habileté du prédateur

PREUVE_NON_CONFORMITE: Pour un vrai taux de succès `p` et `mu = p`, la formule `R = y(1−(mu−1)²) − (1−y)mu²` donne :
`E[R] = p − p(1−p)² − (1−p)p² = p − p(1−p) = p²`.

La règle est bien propre (l'optimum est en `mu = p`), mais son **niveau** croît avec le taux de base. Trois conséquences :
- un prédateur assigné à un défenseur fragile gagne davantage, à calibration identique ;
- la récompense est sommée sur les revendications, sans normalisation : chaque revendication supplémentaire rapporte en moyenne `p² > 0`, ce qui pousse à multiplier les signalements ;
- le bandit apprend donc « qui est faible » au lieu de « qui attaque bien ».

Ce défaut est orthogonal au bornage et à l'unilatéralité déjà signalés. La correction consiste à utiliser un score de compétence de Brier, moyenné par revendication, rapporté à une référence climatologique. Cette référence est estimée sur les **autres** prédateurs du même défenseur (exclusion du prédateur évalué).

CORRECTIF_PYTHON_EXACT:
```python
def brier_skill(ys, mus, p_ref):
    n = len(ys)
    if n == 0 or p_ref is None:
        return 0.0
    mus = [min(1.0, max(0.0, m)) for m in mus]
    bs = sum((m - y) ** 2 for m, y in zip(mus, ys)) / n          # moyenne par revendication
    bs_ref = sum((p_ref - y) ** 2 for y in ys) / n
    if bs_ref == 0.0:
        return 0.0
    return max(-1.0, min(1.0, 1.0 - bs / bs_ref))

def p_ref_exclusion(verdicts, defenseur, predateur):
    autres = [v["y"] for v in verdicts
              if v["defenseur"] == defenseur and v["predateur"] != predateur]
    return sum(autres) / len(autres) if autres else None
```

---

BUG_L_STAR_V2: [Sillon-1-M3-Bandit] `PREDATION_MATRIX` est indexée par prédateur, sans contexte défenseur ; les égalités sont tranchées par l'ordre d'insertion, et l'auto-prédation n'est pas exclue

PREUVE_NON_CONFORMITE: Trois défauts, distincts de l'absence d'exploration déjà signalée.
1. **Pas de contexte.** Un bras doit être un couple `(prédateur, défenseur)`, car l'efficacité d'Argon contre Opus ne dit rien de son efficacité contre Fable.
2. **Biais d'égalité.** À l'initialisation, toutes les entrées sont égales. Le tri stable de Python conserve l'ordre du dictionnaire, donc `cands[0][0]` choisit systématiquement la première branche insérée (Fable) : c'est un biais déterministe par position.
3. **Auto-prédation.** Rien n'empêche `prédateur == défenseur`.

CORRECTIF_PYTHON_EXACT:
```python
import random

def init_matrice(branches):
    return {(p, d): {"n": 0, "s": 0.0}
            for p in branches for d in branches if p != d}

def _moyenne(v):
    return v["s"] / v["n"] if v["n"] else float("inf")   # bras jamais tiré : prioritaire

def choisir_predateur(matrice, defenseur, rng):
    cands = [(p, v) for (p, d), v in matrice.items() if d == defenseur and p != defenseur]
    meilleur = max(_moyenne(v) for _, v in cands)
    ex_aequo = sorted(p for p, v in cands if _moyenne(v) == meilleur)
    return rng.choice(ex_aequo)                            # rng = random.Random(graine engagée)

def mettre_a_jour(matrice, predateur, defenseur, recompense):
    c = matrice[(predateur, defenseur)]
    c["n"] += 1
    c["s"] += recompense
```

---

BUG_L_STAR_V2: [Sillon-1-M1-Diversité] Fable et Opus appartiennent au même fournisseur (`claude-*`) : leurs verdicts sont corrélés et comptés comme indépendants

PREUVE_NON_CONFORMITE: Même avec l'attaque conjointe de Dolev, deux cas posent problème :
- quand Argon défend, la coalition Fable+Opus est mono-fournisseur ; leurs angles morts communs produisent un « 0 faille » corrélé ;
- quand Opus défend, Fable partage sa famille, ce qui ouvre un risque de complaisance.

Compter deux confirmations du même fournisseur comme deux preuves gonfle artificiellement l'évidence, dans les deux directions. Ce défaut est orthogonal au nombre de prédateurs : il concerne leur **indépendance**.

CORRECTIF_PYTHON_EXACT:
```python
def fournisseur(nom):
    return nom.split("-")[0]

def poids_confirmation(faille_id, rapports):
    return len({fournisseur(r["predateur"]) for r in rapports if faille_id in r["failles"]})

def zero_faille_credible(rapports, defenseur):
    # « 0 faille » n'est recevable que si au moins un fournisseur différent de celui du défenseur l'atteste
    vides = [r for r in rapports if not r["failles"]]
    return any(fournisseur(r["predateur"]) != fournisseur(defenseur) for r in vides)
```

---

BUG_L_STAR_V2: [Sillon-1-M1-Wald-Ville] Les incréments additifs ne sont pas des log-e-valeurs : l'inégalité de Ville ne s'applique pas au double compteur

PREUVE_NON_CONFORMITE: L'inégalité de Ville, `P(sup_t M_t ≥ 1/α) ≤ α`, exige que `M_t = exp(S_t)` soit une surmartingale positive sous H0, c'est-à-dire `E_H0[exp(incrément)] ≤ 1`.

Or l'incrément `+2,5·rho_can` est **déterministe et positif** pour tout `rho_can > 0`, donc `E_H0[exp(·)] > 1`. Même en ajoutant la barrière ln(n_adm/α) déjà réclamée, le seuil n'aurait aucune garantie de niveau.

Il y a aussi une erreur de rôle. La vigilance (`rho_can`, `J`) est une **condition de validité** de l'observation, pas une preuve de convergence. Elle doit filtrer l'observation (incrément nul, soit e-valeur égale à 1, si la vigilance est insuffisante), et non s'y ajouter. Ce défaut est orthogonal au bornage du bonus : même borné, il viole la propriété de surmartingale.

CORRECTIF_PYTHON_EXACT:
```python
import math

def increment_log_e(y_faille, p0, p1):
    # H0 : taux de faille p0 (non convergé) ; H1 : p1 < p0 (convergé). Rapport de vraisemblance de Bernoulli.
    return math.log(p1 / p0) if y_faille else math.log((1 - p1) / (1 - p0))

def est_e_valeur(p0, p1, tol=1e-12):
    return abs(p0 * (p1 / p0) + (1 - p0) * ((1 - p1) / (1 - p0)) - 1.0) < tol   # E_H0[LR] = 1

def pas_wald(log_e, y_faille, p0, p1, vigilance_ok):
    if not vigilance_ok:
        return log_e                     # observation invalide : e-valeur = 1, aucun bonus
    return log_e + increment_log_e(y_faille, p0, p1)
```

---

BUG_L_STAR_V2: [Sillon-1-M1-Wald-Ville] Pas de verdict terminal au Tour 4 (SPRT tronqué), pas de règle si les deux barrières sont franchies, et un drapeau `converged` global

PREUVE_NON_CONFORMITE: Le protocole s'arrête au Tour 4. Trois situations restent sans verdict :
- **Aucune barrière franchie à `T_max`.** Il n'existe aucune décision pour ce cas, ce qui viole la règle B4 (« zéro zone morte »).
- **`S⁺` et `S⁻` franchissent leurs seuils au même tour.** Aucune priorité n'est définie.
- **Un seul booléen `converged` pour trois défenseurs.** Une branche convergée peut masquer les deux autres.

Le verdict doit être calculé par défenseur, avec priorité à la réfutation, un verdict conservateur en cas de troncature, et une conjonction finale sur les trois défenseurs.

CORRECTIF_PYTHON_EXACT:
```python
import math

def verdict_defenseur(S_plus, S_minus, n_adm, alpha, beta, t, T_max):
    haut = math.log(n_adm / alpha)
    bas = math.log(1.0 / beta)
    if S_minus >= bas:
        return "NON-CONVERGE"            # la réfutation l'emporte en cas de double franchissement
    if S_plus >= haut:
        return "CONVERGE"
    if t >= T_max:
        return "NON-CONVERGE-TRONQUE"    # troncature conservatrice : H0 maintenue
    return "CONTINUER"

def verdict_global(etats, n_adm, alpha, beta, t, T_max):
    v = {d: verdict_defenseur(e["S_plus"], e["S_minus"], n_adm, alpha, beta, t, T_max)
         for d, e in etats.items()}
    if all(x == "CONVERGE" for x in v.values()):
        return "CONVERGE", v
    if any(x == "CONTINUER" for x in v.values()):
        return "CONTINUER", v
    return "NON-CONVERGE", v
```

---

BUG_L_STAR_V2: [Sillon-1-M3-L*v2] `hypothesis_as_result` n'audite ni les étiquettes `VÉRIFIÉ` hors socle ni les chiffres non marqués `illustratif`

PREUVE_NON_CONFORMITE: Les règles 1 à 6, rappelées par Fable T4 §0 et Argon T4, imposent deux contraintes :
- seuls les 5 faits du socle cités verbatim peuvent porter `VÉRIFIÉ` ;
- tout chiffre hors socle doit porter `illustratif`.

Fable T4 documente d'ailleurs trois omissions réelles : « les 7 Argon », « 4 époques », « méd_h(27) ».

Un compteur lexical ne vérifie pas l'**ancrage** de l'étiquette. De plus, sur le texte corrompu, la chaîne `VÉRIFIÉ` devient `V?RIFI?` et échappe à une recherche littérale. Ce défaut est distinct de l'échec cavitaire en M2 : ici, c'est le juge M3 qui sous-compte les violations de statut.

CORRECTIF_PYTHON_EXACT:
```python
import re, unicodedata

def _plier(s):
    s = unicodedata.normalize("NFC", s or "")
    return "".join(c if ord(c) < 128 else "?" for c in s)   # « é », « ? » et U+FFFD sont confondus

VERIFIE_RE = re.compile(r"V\?RIFI\?|VERIFIE", re.I)
NUM_RE = re.compile(r"(?<![\w.§])\d+(?:[.,]\d+)?\s*%?")

def violations_statut(txt, socle_verbatim, fenetre=600):
    t = _plier(txt)
    socle = [_plier(s) for s in socle_verbatim]
    return sum(1 for m in VERIFIE_RE.finditer(t)
               if not any(s in t[max(0, m.start() - fenetre): m.end() + fenetre] for s in socle))

def chiffres_non_marques(txt, socle_verbatim, fenetre=80):
    t = _plier(txt)
    for s in socle_verbatim:
        t = t.replace(_plier(s), " ")
    t = "\n".join(l for l in t.splitlines() if not l.lstrip().startswith("#"))
    return [m.group(0) for m in NUM_RE.finditer(t)
            if "illustratif" not in t[max(0, m.start() - fenetre): m.end() + fenetre].lower()]
```

FIN-INSPECTION-ESSAIM
