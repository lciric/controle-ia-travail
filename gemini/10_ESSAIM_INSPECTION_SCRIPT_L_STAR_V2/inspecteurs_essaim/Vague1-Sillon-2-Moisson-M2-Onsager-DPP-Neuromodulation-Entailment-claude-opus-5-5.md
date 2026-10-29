# Inspection de l'étage M2 : Onsager, DPP, Yu-Dayan, Abstract Entailment

**Portée de l'inspection.** Le code source n'a pas été transmis verbatim. J'inspecte donc **le comportement décrit** du script, et les correctifs remplacent les fonctions décrites. Les numéros de ligne sont impossibles à vérifier.

**Discipline de statut M3.** Elle est appliquée aux correctifs eux-mêmes :
- Toute constante numérique introduite ci-dessous porte la mention `illustratif`.
- Toute étude citée porte la mention `(référence à vérifier)` : Yu & Dayan 2005 ; Kulesza & Taskar 2012 ; Chen, Zhang & Zhou 2018 pour le MAP glouton DPP ; Thouless-Anderson-Palmer 1977 pour le terme d'Onsager.

**Précision honnête.** La projection orthogonale demandée par la mission n'est pas littéralement le terme de réaction TAP/AMP. Il s'agit de l'opérateur spécifié par L\*v2, et je l'implémente comme tel.

**Dépendances.** Les correctifs forment une chaîne. Les blocs 1 et 2 sont réutilisés par les blocs 3 à 7.

---

BUG_L_STAR_V2: [M2-Onsager/Prétraitement] La soustraction cavitaire échoue silencieusement sur le texte corrompu (« ? » à la place des accents)

PREUVE_NON_CONFORMITE :
- Les lois M3 signalent elles-mêmes la corruption d'encodage. Elle devient le critère M2 de E0-Méta (Opus T2 : « le signalement de la corruption des accents (« ? ») »).
- Un tokeniseur `\w+` découpe `m?thode` en `m` et `thode`. Un mot accentué du `set` statique, par exemple `hypothèse`, ne rencontre donc **jamais** `hypoth?se` dans le texte réel. La différence ensembliste ne retire rien, et aucun signal d'erreur n'est émis.
- Toute projection vectorielle construite en aval hérite du même défaut si le prompt et la sortie ne partagent pas la **même** canonicalisation.
- Le correctif applique trois règles :
  - le « ? » intra-mot est conservé dans le token ;
  - la canonicalisation est décidée **conjointement** sur le prompt et la sortie ;
  - en mode corrompu, toute lettre non ASCII est repliée sur « ? ». Ce repli est avec perte mais cohérent : `méthode` et `m?thode` donnent tous deux `m?thode`.

CORRECTIF_PYTHON_EXACT :
```python
import re
import unicodedata

CORRUPTION_THRESHOLD = 0.002  # illustratif

_CORRUPT_INTRAWORD = re.compile(r"(?<=[^\W\d_])\?|\?(?=[^\W\d_])|\uFFFD")
_TOKEN_RE = re.compile(r"(?:[^\W\d_]|(?<=[^\W\d_])\?|\?(?=[^\W\d_])|\uFFFD)+")


def corruption_rate(txt):
    words = txt.split()
    if not words:
        return 0.0
    bad = sum(1 for w in words if _CORRUPT_INTRAWORD.search(w))
    return bad / len(words)


def joint_corruption_flag(*texts):
    """Décision UNIQUE pour prompt + sortie : sinon les deux espaces vectoriels divergent."""
    return corruption_rate(" ".join(texts)) > CORRUPTION_THRESHOLD


def canon_token(tok, corrupted):
    tok = unicodedata.normalize("NFC", tok).casefold()
    if not corrupted:
        return tok
    return "".join(
        "?" if (ch in "?\uFFFD" or (ch.isalpha() and not ch.isascii())) else ch
        for ch in tok
    )


def tokenize(txt, corrupted):
    txt = unicodedata.normalize("NFKC", txt)
    return [canon_token(t, corrupted) for t in _TOKEN_RE.findall(txt)]
```

---

BUG_L_STAR_V2: [M2-Onsager] La différence ensembliste sur 14 mots statiques remplace la projection orthogonale `v_p - (<v_p,v_Q>/||v_Q||²)·v_Q`

PREUVE_NON_CONFORMITE : `raw - PROMPT_CAVITY_TOKENS` diverge de l'opérateur spécifié sur quatre points.
1. **Prompt réel ignoré.** La « cavité » est un vocabulaire figé, indépendant du prompt effectivement envoyé. L'écho d'un prompt différent n'est jamais retiré.
2. **Opération binaire.** Les fréquences sont perdues. Un mot répété 40 fois par écho du prompt pèse autant qu'une occurrence unique.
3. **Pas de soustraction proportionnelle.** La composante colinéaire au prompt n'est pas retirée en proportion de $\langle v_p, v_Q\rangle$. Un mot de contenu légitime figurant dans la liste est amputé à 100 %.
4. **Orthogonalité invérifiable.** Le résultat $\langle r, v_Q\rangle = 0$ ne peut pas être contrôlé.

Avec plusieurs segments de prompt (système, utilisateur, lois M3), il faut projeter sur leur **sous-espace engendré**, par Gram-Schmidt modifié, et non sur chacun indépendamment.

CORRECTIF_PYTHON_EXACT :
```python
import math
from collections import Counter


def tf_vector(tokens):
    c = Counter(tokens)
    return {t: 1.0 + math.log(n) for t, n in c.items()}


def dot(u, v):
    if len(u) > len(v):
        u, v = v, u
    return sum(x * v.get(k, 0.0) for k, x in u.items())


def norm(u):
    return math.sqrt(dot(u, u))


def onsager_cavity_projection(v_p, v_q, eps=1e-12):
    """r = v_p - (<v_p, v_q> / ||v_q||^2) * v_q, avec contrôle d'orthogonalité."""
    qq = dot(v_q, v_q)
    if qq <= eps:
        return dict(v_p), 0.0
    coef = dot(v_p, v_q) / qq
    res = {k: x - coef * v_q.get(k, 0.0) for k, x in v_p.items()}
    for k, y in v_q.items():
        if k not in res:
            res[k] = -coef * y
    res = {k: x for k, x in res.items() if abs(x) > eps}
    residual_dot = dot(res, v_q)
    if abs(residual_dot) > 1e-9 * max(1.0, norm(v_p) * math.sqrt(qq)):
        raise ArithmeticError(f"Projection non orthogonale : <r, v_Q> = {residual_dot!r}")
    return res, coef


def project_out_span(v_p, prompt_vectors, eps=1e-12):
    """Gram-Schmidt modifié : retire toute la composante dans span(v_Q1, ..., v_Qm)."""
    basis = []
    for v in prompt_vectors:
        w = dict(v)
        for b in basis:
            w, _ = onsager_cavity_projection(w, b)
        if norm(w) > eps:
            basis.append(w)
    res = dict(v_p)
    for b in basis:
        res, _ = onsager_cavity_projection(res, b)
    return res


def m2_cavity_residual(output_txt, prompt_txts):
    flag = joint_corruption_flag(output_txt, *prompt_txts)
    v_p = tf_vector(tokenize(output_txt, flag))
    v_qs = [tf_vector(tokenize(t, flag)) for t in prompt_txts]
    res = project_out_span(v_p, v_qs)
    n_p = norm(v_p)
    echo_ratio = 1.0 - (norm(res) / n_p) ** 2 if n_p > 0 else 1.0  # part d'énergie expliquée par le prompt
    return res, echo_ratio, flag
```

---

BUG_L_STAR_V2: [M2-DPP] L'heuristique `qual*(1-max_sim²)` n'est pas le gain marginal de `det(L_Y)`, et un contre-exemple inverse la sélection

PREUVE_NON_CONFORMITE : Le gain exact d'un candidat $i$ sachant $Y$ est le complément de Schur
$$d_i^2 = L_{ii} - L_{iY}L_Y^{-1}L_{Yi} = q_i^2\big(1 - s_{iY}^\top S_Y^{-1} s_{iY}\big).$$
L'heuristique commet deux erreurs.
- **Seule la similarité maximale est prise en compte.** Elle ignore la redondance **conjointe** avec plusieurs éléments déjà choisis. Elle n'est exacte que pour $|Y| = 1$.
- **La qualité entre à la puissance 1 au lieu de 2.** Le classement entre candidats de qualités différentes est déformé.

**Contre-exemple.** Soit $Y = \{A, B\}$ avec $s_{AB} = 0$.
- Candidat $C$ : $s_{CA} = s_{CB} = 0{,}7$. L'heuristique donne $1 - 0{,}49 = 0{,}51$. Le gain exact est $\det(S_{ABC}) = 0{,}02$.
- Candidat $D$ : $s_{DA} = 0{,}72$, $s_{DB} = 0$. L'heuristique et le gain exact donnent tous deux $0{,}4816$.

L'heuristique choisit $C$, presque entièrement redondant, alors que le DPP choisit $D$. Le test ci-dessous rend ce contre-exemple exécutable.

Le correctif implémente le MAP glouton par Cholesky incrémental, en $O(nk^2)$. Il contre-vérifie le log-déterminant final par une décomposition de Cholesky complète de $L_Y$. Le noyau cosinus sur vecteurs TF est une matrice de Gram, donc semi-définie positive par construction.

CORRECTIF_PYTHON_EXACT :
```python
import math


def cosine_kernel(vectors):
    n = len(vectors)
    norms = [norm(v) for v in vectors]
    S = [[0.0] * n for _ in range(n)]
    for i in range(n):
        S[i][i] = 1.0 if norms[i] > 0 else 0.0
        for j in range(i + 1, n):
            if norms[i] > 0 and norms[j] > 0:
                s = dot(vectors[i], vectors[j]) / (norms[i] * norms[j])
            else:
                s = 0.0
            S[i][j] = S[j][i] = s
    return S


def cholesky_logdet(M, eps=1e-12):
    n = len(M)
    C = [[0.0] * n for _ in range(n)]
    logdet = 0.0
    for i in range(n):
        for j in range(i + 1):
            s = M[i][j] - sum(C[i][k] * C[j][k] for k in range(j))
            if i == j:
                if s <= eps:
                    return float("-inf")
                C[i][i] = math.sqrt(s)
                logdet += 2.0 * math.log(C[i][i])
            else:
                C[i][j] = s / C[j][j]
    return logdet


def dpp_greedy_map_cholesky(quality, S, k, eps=1e-10):
    """MAP glouton exact de det(L_Y), L = diag(q) S diag(q), Cholesky incrémental."""
    n = len(quality)
    if any(q <= 0 or math.isnan(q) for q in quality):
        raise ValueError("Qualités DPP strictement positives exigées")
    d2 = [quality[i] ** 2 * S[i][i] for i in range(n)]
    c = [[] for _ in range(n)]
    selected, logdet = [], 0.0
    remaining = set(range(n))
    while len(selected) < k and remaining:
        j = max(sorted(remaining), key=lambda i: d2[i])
        if d2[j] <= eps:
            break
        selected.append(j)
        remaining.discard(j)
        logdet += math.log(d2[j])
        dj = math.sqrt(d2[j])
        for i in remaining:
            L_ji = quality[j] * S[j][i] * quality[i]
            e_i = (L_ji - sum(a * b for a, b in zip(c[j], c[i]))) / dj
            c[i].append(e_i)
            d2[i] -= e_i * e_i
    L_Y = [[quality[a] * S[a][b] * quality[b] for b in selected] for a in selected]
    ref = cholesky_logdet(L_Y) if selected else 0.0
    if selected and abs(ref - logdet) > 1e-6 * max(1.0, abs(ref)):
        raise ArithmeticError(f"Incohérence Cholesky incrémental ({logdet}) vs complet ({ref})")
    return selected, logdet


def dpp_onsager_select(output_texts, prompt_txts, quality, k):
    residuals = [m2_cavity_residual(t, prompt_txts)[0] for t in output_texts]
    return dpp_greedy_map_cholesky(quality, cosine_kernel(residuals), k)


def _test_contre_exemple_max_sim():
    def det3(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    S_ABC = [[1.0, 0.0, 0.7], [0.0, 1.0, 0.7], [0.7, 0.7, 1.0]]
    S_ABD = [[1.0, 0.0, 0.72], [0.0, 1.0, 0.0], [0.72, 0.0, 1.0]]
    approx_C, approx_D = 1 - 0.7 ** 2, 1 - 0.72 ** 2
    exact_C, exact_D = det3(S_ABC), det3(S_ABD)  # det(S_AB) = 1
    assert approx_C > approx_D, "l'heuristique choisit C"
    assert exact_D > exact_C, "le DPP exact choisit D"
    assert abs(exact_C - 0.02) < 1e-9 and abs(exact_D - 0.4816) < 1e-9
```

---

BUG_L_STAR_V2: [M2-Yu-Dayan] `NE = min(0.95, 0.22 + 2.4·jaccard)` inverse le signal d'incertitude inattendue et n'a aucun ACh

PREUVE_NON_CONFORMITE : Dans le modèle de Yu & Dayan `(référence à vérifier)`, deux signaux distincts coexistent.
- **ACh** code l'incertitude **attendue**, c'est-à-dire la non-fiabilité connue du modèle courant.
- **NE** code l'incertitude **inattendue**, c'est-à-dire une erreur de prédiction supérieure à ce que l'ACh explique. Ce signal déclenche une réinitialisation de contexte.

La formule du script présente quatre défauts.
1. **Elle croît avec la similarité Jaccard entre tours.** Un contexte stable déclenche donc l'exploration, alors qu'il devrait produire un NE bas. Le sens est inversé.
2. **Aucune prédiction n'est confrontée à une observation.** Il n'existe donc pas d'erreur de prédiction.
3. **ACh est absent.** La bascule n'a pas de second pôle.
4. **Les constantes 0,22, 2,4 et 0,95 ne sont pas calibrées.** Elles ne sont pas non plus marquées `illustratif`.

Le transfert vers un LLM reste une HYPOTHÈSE. Sa rivale est un simple taux d'erreur glissant sans distinction attendue/inattendue. Le correctif fonde le signal sur une observable auditable : le taux de citations compatibles avec leur résumé, issu de la porte d'entailment (bloc 6).

CORRECTIF_PYTHON_EXACT :
```python
import math


class YuDayanNeuromodulator:
    """ACh = incertitude attendue ; NE = incertitude inattendue (HYPOTHÈSE de transfert,
    Yu & Dayan 2005, référence à vérifier). Observable : taux de soutien des citations."""

    def __init__(self, prior_mean=0.5, prior_var=0.05, lr=0.2, z_reset=2.5, var_floor=1e-4):
        # toutes constantes : illustratif
        self.prior_mean, self.prior_var = prior_mean, prior_var
        self.mean, self.var = prior_mean, prior_var
        self.lr, self.z_reset, self.var_floor = lr, z_reset, var_floor
        self.ach, self.ne, self.n_resets = 0.0, 0.0, 0

    def update(self, observed_support):
        if observed_support is None or math.isnan(observed_support) or not (0.0 <= observed_support <= 1.0):
            raise ValueError("observed_support doit être une proportion dans [0, 1]")
        err = observed_support - self.mean
        sd = math.sqrt(max(self.var, self.var_floor))
        z = abs(err) / sd
        # NE : surprise EXCÉDANT ce que l'incertitude attendue explique (z > 1)
        self.ne = 1.0 - math.exp(-max(0.0, z - 1.0))
        if z > self.z_reset:
            self.mean, self.var = observed_support, self.prior_var  # changement de contexte
            self.n_resets += 1
        else:
            self.mean += self.lr * err
            self.var = (1.0 - self.lr) * self.var + self.lr * err * err
        # ACh : écart-type attendu normalisé (écart-type max d'une proportion = 0,5)
        self.ach = min(1.0, math.sqrt(max(self.var, self.var_floor)) / 0.5)
        return self.ach, self.ne
```

---

BUG_L_STAR_V2: [M2-Yu-Dayan] La bascule est inerte : ni la température, ni top_p, ni la structure des requêtes API ne changent

PREUVE_NON_CONFORMITE :
- `NE_level` est calculé puis n'est consommé par rien. Les trajectoires de génération et de recherche sont donc identiques quel que soit le régime neuromodulatoire.
- Le mécanisme est décoratif et non réfutable : aucune observable ne dépend de lui. Cela viole l'exigence d'un opérateur ayant un effet testable.
- Le correctif définit trois régimes :

| Régime | Condition | Température | Requêtes |
| :--- | :--- | :--- | :--- |
| `EXPLORATION_RESET` | NE haut | haute | disjonctives (`OR`), larges |
| `VERIFICATION_CIBLEE` | ACh haut | basse | conjonctives, phrase exacte dans `abs:`, peu de résultats |
| `EXPLOITATION` | sinon | intermédiaire | intermédiaires |

- Les tokens corrompus (contenant « ? ») sont exclus des requêtes, car ils cassent la recherche.
- Un test vérifie que les plans diffèrent effectivement selon le régime.

CORRECTIF_PYTHON_EXACT :
```python
from urllib.parse import urlencode

ARXIV_API = "http://export.arxiv.org/api/query"
S2_SEARCH = "https://api.semanticscholar.org/graph/v1/paper/search"
S2_FIELDS = "title,abstract,year,authors,externalIds"


def neuromodulated_plan(terms, phrase, ach, ne, t_lo=0.2, t_hi=1.0, ne_explore=0.5, ach_verify=0.4):
    # seuils et températures : illustratif
    terms = [t for t in terms if t and "?" not in t and "\uFFFD" not in t]
    phrase = (phrase or "").replace('"', "").strip()
    if ne >= ne_explore:
        mode, temperature, top_p, max_results = "EXPLORATION_RESET", t_lo + (t_hi - t_lo) * ne, 0.95, 25
        arxiv_q = " OR ".join(f"all:{t}" for t in terms[:6])
        s2_q = " ".join(terms[:6])
    elif ach >= ach_verify:
        mode, temperature, top_p, max_results = "VERIFICATION_CIBLEE", t_lo, 0.8, 5
        parts = ([f'abs:"{phrase}"'] if phrase else []) + [f"abs:{t}" for t in terms[:3]]
        arxiv_q = " AND ".join(parts)
        s2_q = phrase or " ".join(terms[:3])
    else:
        mode, temperature, top_p, max_results = "EXPLOITATION", t_lo + 0.25 * (t_hi - t_lo), 0.9, 10
        arxiv_q = " AND ".join(f"all:{t}" for t in terms[:4])
        s2_q = " ".join(terms[:4])
    if not arxiv_q:
        raise ValueError("Aucun terme de requête exploitable (tous corrompus ou vides)")
    return {
        "mode": mode,
        "temperature": round(temperature, 4),
        "top_p": top_p,
        "arxiv_url": ARXIV_API + "?" + urlencode({"search_query": arxiv_q, "start": 0, "max_results": max_results}),
        "s2_url": S2_SEARCH + "?" + urlencode({"query": s2_q, "fields": S2_FIELDS, "limit": max_results}),
    }


def generate_with_plan(llm_call, prompt, plan):
    """llm_call : callable(prompt, temperature=..., top_p=...) fourni par l'infrastructure (HYPOTHÈSE)."""
    return llm_call(prompt, temperature=plan["temperature"], top_p=plan["top_p"])


def _test_bascule_effective():
    terms, phrase = ["rejection", "violation", "steering"], "linear steering"
    p_exp = neuromodulated_plan(terms, phrase, ach=0.1, ne=0.9)
    p_ver = neuromodulated_plan(terms, phrase, ach=0.9, ne=0.1)
    p_ext = neuromodulated_plan(terms, phrase, ach=0.1, ne=0.1)
    assert len({p_exp["mode"], p_ver["mode"], p_ext["mode"]}) == 3
    assert p_exp["temperature"] > p_ext["temperature"] > p_ver["temperature"]
    assert len({p_exp["arxiv_url"], p_ver["arxiv_url"], p_ext["arxiv_url"]}) == 3
```

---

BUG_L_STAR_V2: [M2-Entailment] Aucune vérification algorithmique que la citation est résolue et que son résumé arXiv/S2 soutient l'affirmation

PREUVE_NON_CONFORMITE :
- Le script ne récupère aucun résumé. Il ne vérifie ni l'existence de la référence (auteur et année), ni la compatibilité entre l'affirmation et le résumé.
- Les lois M3 marquent toute étude externe `(référence à vérifier)`, par exemple « Jhaveri et al., 2026 ; Tagliabue et al., 2026 ». M2 est précisément l'étage censé tenter cette vérification. Sans lui, la marque reste perpétuelle et une citation hallucinée passe.

Le correctif obéit à six règles.
1. **Résolution.** La référence est cherchée par nom d'auteur et année, ou par identifiant arXiv.
2. **Contrôle lexical.** On mesure la couverture des termes clés et la présence de **tous** les nombres cités, avec équivalence entre `0,49`, `0.49` et `49%`.
3. **Contrôle de polarité.** Une négation dans la phrase la plus pertinente du résumé rétrograde le verdict.
4. **Verdict tri-état sans zone morte.** Les trois issues sont `COMPATIBLE_LEXICAL`, `NON_SOUTENU` et `INVERIFIABLE`.
5. **Échec fermé.** Toute erreur réseau ou de parsing produit `INVERIFIABLE`, jamais « soutenu ».
6. **Pas de traduction implicite.** Les affirmations sont en français et les résumés majoritairement en anglais. L'appelant doit donc fournir des termes clés dans la langue du résumé ; une comparaison translingue produirait des `NON_SOUTENU` systématiques et faux.

**Limite déclarée.** `COMPATIBLE_LEXICAL` est une condition **nécessaire**, pas une implication logique. Il ne remplace pas une vérification humaine ou NLI.

CORRECTIF_PYTHON_EXACT :
```python
import json
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import urlencode

_ATOM = {"a": "http://www.w3.org/2005/Atom"}
_UA = {"User-Agent": "m2-entailment-checker/1.0 (mailto:contact@example.org)"}
_NEG = {"not", "no", "without", "never", "none", "neither", "nor", "cannot", "fail", "fails", "failed",
        "ne", "pas", "sans", "aucun", "aucune", "jamais", "non"}
_NUM_RE = re.compile(r"\d+(?:[.,]\d+)?")


def _http_get(url, timeout=15.0):
    req = urllib.request.Request(url, headers=_UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")


def fetch_arxiv_entries(url, polite_delay=3.0):
    root = ET.fromstring(_http_get(url))
    out = []
    for e in root.findall("a:entry", _ATOM):
        out.append({
            "title": " ".join(e.findtext("a:title", "", _ATOM).split()),
            "abstract": " ".join(e.findtext("a:summary", "", _ATOM).split()),
            "year": e.findtext("a:published", "", _ATOM)[:4],
            "authors": [a.findtext("a:name", "", _ATOM) for a in e.findall("a:author", _ATOM)],
            "source": "arXiv",
        })
    time.sleep(polite_delay)  # délai de courtoisie demandé par arXiv
    return out


def fetch_s2_entries(url):
    data = json.loads(_http_get(url))
    return [{
        "title": p.get("title") or "",
        "abstract": p.get("abstract") or "",
        "year": str(p.get("year") or ""),
        "authors": [a.get("name", "") for a in (p.get("authors") or [])],
        "source": "S2",
    } for p in (data.get("data") or [])]


def _num_canon(s):
    return f"{float(s.replace(',', '.')):g}"


def _num_forms(tok):
    x = float(tok.replace(",", "."))
    forms = {f"{x:g}"}
    if 0 < x <= 1:
        forms.add(f"{x * 100:g}")
    if 1 < x <= 100:
        forms.add(f"{x / 100:g}")
    return forms


def _present(term, toks):
    if term in toks:
        return True
    if len(term) > 4:
        prefix = term[:max(4, len(term) - 2)]
        return any(a.startswith(prefix) for a in toks)
    return False


def check_abstract_entailment(claim_terms, claim_numbers, abstract, claim_negated=False, tau=0.8):
    # tau : illustratif
    if not abstract or not abstract.strip():
        return "INVERIFIABLE", {"raison": "résumé absent"}
    terms = [canon_token(t, False) for t in claim_terms if t]
    if not terms:
        return "INVERIFIABLE", {"raison": "aucun terme clé fourni dans la langue du résumé"}
    abs_toks = set(tokenize(abstract, False))
    coverage = sum(_present(t, abs_toks) for t in terms) / len(terms)
    abs_nums = {_num_canon(n) for n in _NUM_RE.findall(abstract)}
    missing = [n for n in claim_numbers if not (_num_forms(n) & abs_nums)]
    sentences = [s for s in re.split(r"(?<=[.!?;])\s+", abstract) if s.strip()]
    best = max(sentences, key=lambda s: sum(_present(t, set(tokenize(s, False))) for t in terms))
    neg_in_best = bool(set(tokenize(best, False)) & _NEG)
    polarity_doubt = neg_in_best != claim_negated
    details = {"couverture": round(coverage, 3), "nombres_manquants": missing,
               "phrase_pivot": best, "polarite_douteuse": polarity_doubt}
    if coverage >= tau and not missing and not polarity_doubt:
        return "COMPATIBLE_LEXICAL", details
    if coverage >= tau and not missing and polarity_doubt:
        return "INVERIFIABLE", details
    return "NON_SOUTENU", details


def resolve_and_check(surname, year, claim_terms, claim_numbers=(), claim_negated=False,
                      arxiv_id=None, year_tol=0):
    base = {"reference": f"{surname} et al., {year}", "statut": "(référence à vérifier)"}
    try:
        if arxiv_id:
            cands = fetch_arxiv_entries(ARXIV_API + "?" + urlencode({"id_list": arxiv_id}))
        else:
            q = " ".join([surname] + [t for t in claim_terms if "?" not in t][:5])
            cands = fetch_s2_entries(S2_SEARCH + "?" + urlencode({"query": q, "fields": S2_FIELDS, "limit": 20}))
    except (urllib.error.URLError, TimeoutError, ET.ParseError, json.JSONDecodeError, ValueError) as exc:
        return {**base, "verdict": "INVERIFIABLE", "raison": f"réseau/parsing : {exc!r}"}
    sn = canon_token(surname, False)
    matched = [c for c in cands
               if c["year"].isdigit() and abs(int(c["year"]) - int(year)) <= year_tol
               and any(sn in tokenize(a, False) for a in c["authors"])]
    if not matched:
        return {**base, "verdict": "INVERIFIABLE", "raison": "référence non résolue (auteur/année)"}
    rank = {"COMPATIBLE_LEXICAL": 2, "INVERIFIABLE": 1, "NON_SOUTENU": 0}
    best = None
    for c in matched:
        v, d = check_abstract_entailment(claim_terms, list(claim_numbers), c["abstract"], claim_negated)
        if best is None or rank[v] > rank[best[0]]:
            best = (v, d, c)
    v, d, c = best
    statut = base["statut"] + (" — résumé lexicalement compatible" if v == "COMPATIBLE_LEXICAL" else "")
    return {**base, "statut": statut, "verdict": v, "details": d,
            "titre": c["title"], "source": c["source"]}
```

---

BUG_L_STAR_V2: [M2-Intégration] La porte M2 n'a ni verdict défini, ni couplage à la neuromodulation, ni garde contre l'escalade de statut

PREUVE_NON_CONFORMITE :
- **Pas de chaînage.** Même corrigés isolément, les blocs 4 à 6 restent décoratifs s'ils ne sont pas chaînés. L'observable d'entailment doit alimenter Yu-Dayan, et les `NON_SOUTENU` doivent remonter comme failles réelles vers M1 (`n_real_failles`).
- **Pas de verdict de porte.** Le cas « aucune citation résolue » est une zone morte interdite par la règle B4.
- **Escalade de statut possible.** Seuls les 5 faits du socle peuvent porter `VÉRIFIÉ`. Une citation dont le résumé est compatible reste `(référence à vérifier)`.
- **Pas d'injection de fausse observation.** Si aucune citation n'est résolue, le modulateur n'est pas mis à jour. Injecter 0,5 fabriquerait une donnée.

CORRECTIF_PYTHON_EXACT :
