"""Base « forme seule » (brouillon 2 du préenregistrement, § Bases à battre et P9) : ce que la forme d'un énoncé révèle de
sa strate, sans aucun calcul de vérité.

1. **Règle fixe** : « faux » si l'énoncé est un seuil littéral ou un résidu évité, c'est-à-dire si, après le préfixe
   universel de tête et la chaîne d'hypothèses, le corps est une seule comparaison :
   - « E op c » ou « c op E » avec op parmi <, <=, >, >=, où c est une expression close (nombres, constantes du monde
     et opérations, sans variable ni fonction) et où E contient une variable NAT du préfixe ;
   - ou « mod(E, c1) != c2 » (ou retourné), c1 et c2 clos, E contenant une variable NAT du préfixe.
   Par construction de la banque (P9) : rappel 1,00 sur les pièges, 0,50 sur les faux tôt, fausses morts 0,50 sur les
   vérités ; tout écart est un défaut de plantation (A1).
2. **Classifieur de style** : bayésien naïf multinomial sur les jetons de l'énoncé (nombres remplacés par « NUM »,
   unigrammes et bigrammes), lissage de Laplace, **en rationnels exacts** (aucun flottant, résultat reproductible à
   l'octet) ; validation croisée par mondes entiers, plis tirés par l'enfant [10] des graines ; il apprend « faux »
   (faux tôt et pièges) contre « vrai » (vérités) ; aire sous la courbe exacte (statistique de Mann-Whitney, ex æquo
   comptés pour moitié), rapportée par strate : pièges contre vérités, faux tôt contre vérités.
"""
from __future__ import annotations

from fractions import Fraction

from .evaluation import hypotheses, prefixe
from .grammaire import lexer


def _contient(e, pred) -> bool:
    if not isinstance(e, tuple) or not e:
        return False
    if not isinstance(e[0], str):  # tuple d'arguments d'une fonction
        return any(_contient(x, pred) for x in e)
    if pred(e):
        return True
    return any(_contient(x, pred) for x in e[1:] if isinstance(x, tuple))


def est_close(e) -> bool:
    """Expression sans variable ni fonction (nombres, constantes du monde, opérations)."""
    return not _contient(e, lambda x: x[0] in ("var", "fn", "somme", "somme_sur"))


def _contient_nat(e, nats) -> bool:
    return _contient(e, lambda x: x[0] == "var" and x[1] in nats)


def analyse_forme(arbre):
    """Rend None si l'énoncé n'est ni un seuil ni un résidu évité ; sinon (genre, côté clos) avec genre « seuil » ou
    « residu »."""
    pre, corps = prefixe(arbre)
    nats = {v for v, d in pre if d[0] == "NAT"}
    if not nats:
        return None
    _hyps, concl = hypotheses(corps)
    if concl[0] != "cmp":
        return None
    op, a, b = concl[1], concl[2], concl[3]
    if op in ("<", "<=", ">", ">="):
        for clos, autre in ((b, a), (a, b)):
            if est_close(clos) and _contient_nat(autre, nats):
                return "seuil", clos
        return None
    if op == "!=":
        for clos, autre in ((b, a), (a, b)):
            if est_close(clos) and autre[0] == "fn" and autre[1] == "mod" and est_close(autre[2][1]) \
                    and _contient_nat(autre[2][0], nats):
                return "residu", clos
    return None


def regle_forme_seule(arbre) -> bool:
    """Verdict de la règle fixe : vrai = « faux » (à tuer)."""
    return analyse_forme(arbre) is not None


def borne_naturelle(arbre) -> bool:
    """Seuil dont le côté clos est 0, 1 ou une constante du monde (brouillon 2 : « borne naturelle »)."""
    f = analyse_forme(arbre)
    if f is None or f[0] != "seuil":
        return False
    c = f[1]
    return c in (("num", Fraction(0)), ("num", Fraction(1))) or c[0] == "cst"


# ---------------------------------------------------------------- classifieur de style
def jetons_de_style(texte: str) -> list[str]:
    toks = ["NUM" if g == "nombre" else v for g, v in lexer(texte)]
    return toks + [f"{x}·{y}" for x, y in zip(toks, toks[1:])]


class BayesNaif:
    def __init__(self, lissage: Fraction):
        self.alpha = Fraction(lissage)

    def apprendre(self, textes, etiquettes):
        self.compte = {True: {}, False: {}}
        self.total = {True: 0, False: 0}
        self.n = {True: 0, False: 0}
        vocab = set()
        for t, y in zip(textes, etiquettes):
            self.n[y] += 1
            for j in jetons_de_style(t):
                self.compte[y][j] = self.compte[y].get(j, 0) + 1
                self.total[y] += 1
                vocab.add(j)
        self.V = len(vocab) + 1
        return self

    def score(self, texte) -> Fraction:
        """Rapport de vraisemblance exact P(faux | texte) / P(vrai | texte), à une constante près."""
        r = Fraction(self.n[True] + 1, self.n[False] + 1)
        for j in jetons_de_style(texte):
            pf = (self.compte[True].get(j, 0) + self.alpha) / (self.total[True] + self.alpha * self.V)
            pv = (self.compte[False].get(j, 0) + self.alpha) / (self.total[False] + self.alpha * self.V)
            r *= pf / pv
        return r


def aire_sous_la_courbe(scores_positifs, scores_negatifs) -> Fraction | None:
    """Statistique de Mann-Whitney exacte : P(score positif > score négatif) + 1/2 P(égalité)."""
    if not scores_positifs or not scores_negatifs:
        return None
    s = Fraction(0)
    for p in scores_positifs:
        for q in scores_negatifs:
            s += 1 if p > q else (Fraction(1, 2) if p == q else 0)
    return s / (len(scores_positifs) * len(scores_negatifs))


def mesurer(banque: list, rng_plis, plis: int, lissage) -> dict:
    """`banque` : [(monde, plantes)]. Règle fixe sur toute la banque ; classifieur en validation croisée par mondes."""
    from .exact import frac_vers_texte
    compte = {"VERITE_PLANTEE": [0, 0], "FAUX_TOT": [0, 0], "PIEGE": [0, 0], "TEMOIN_TRIVIAL": [0, 0],
              "TEMOIN_GROSSIER": [0, 0]}
    for m, plantes in banque:
        for p in plantes:
            c = compte[p.etiquette]
            c[0] += int(regle_forme_seule(m.analyser(p.texte)))
            c[1] += 1
    regle = {k: {"declares_faux": a, "plantes": n, "taux": frac_vers_texte(Fraction(a, n)) if n else None}
             for k, (a, n) in compte.items()}
    # plis par mondes entiers, tirés par l'enfant [10]
    ordre = [int(i) for i in rng_plis.permutation(len(banque))]
    pli_de = {w: k % plis for k, w in enumerate(ordre)}
    scores = {"VERITE_PLANTEE": [], "FAUX_TOT": [], "PIEGE": []}
    for k in range(plis):
        app = [(p.texte, p.etiquette != "VERITE_PLANTEE") for w, (_m, pl) in enumerate(banque) if pli_de[w] != k
               for p in pl if p.etiquette in scores]
        modele = BayesNaif(Fraction(lissage)).apprendre([t for t, _ in app], [y for _, y in app])
        for w, (_m, pl) in enumerate(banque):
            if pli_de[w] == k:
                for p in pl:
                    if p.etiquette in scores:
                        scores[p.etiquette].append(modele.score(p.texte))
    auc_p = aire_sous_la_courbe(scores["PIEGE"], scores["VERITE_PLANTEE"])
    auc_f = aire_sous_la_courbe(scores["FAUX_TOT"], scores["VERITE_PLANTEE"])
    return {"regle_fixe": regle,
            "classifieur_de_style": {"plis": plis, "lissage": str(lissage), "plis_par_monde": [pli_de[w] for w in range(len(banque))],
                                     "aire_pieges_contre_verites": None if auc_p is None else frac_vers_texte(auc_p),
                                     "aire_faux_tot_contre_verites": None if auc_f is None else frac_vers_texte(auc_f)}}


def ecarts_p9(mesure: dict) -> list[str]:
    """P9 : rappel 1 sur les pièges, 1/2 sur les faux tôt, fausses morts 1/2 sur les vérités, exactement."""
    r = mesure["regle_fixe"]
    attendu = {"PIEGE": Fraction(1), "FAUX_TOT": Fraction(1, 2), "VERITE_PLANTEE": Fraction(1, 2)}
    sortie = []
    for k, v in attendu.items():
        a, n = r[k]["declares_faux"], r[k]["plantes"]
        if n == 0 or Fraction(a, n) != v:
            sortie.append(f"A1 (P9) : règle « forme seule » sur {k} : {a}/{n} au lieu de {v}")
    return sortie
