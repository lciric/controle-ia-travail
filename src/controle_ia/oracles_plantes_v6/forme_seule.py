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


def regle_borne_non_naturelle(arbre) -> bool:
    """P10 (brouillon 3) : « faux » si l'énoncé est un seuil dont le côté clos n'est ni 0, ni 1, ni une constante du
    monde, ou un résidu évité."""
    f = analyse_forme(arbre)
    if f is None:
        return False
    return f[0] == "residu" or not borne_naturelle(arbre)


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


def _taux(a, n):
    from .exact import frac_vers_texte
    return frac_vers_texte(Fraction(a, n)) if n else None


def mesurer(banque: list, rng_plis, plis: int, lissage, seuil_aire=Fraction(3, 4)) -> dict:
    """`banque` : [(monde, plantes)]. Règles P9 et P10 sur toute la banque et par monde ; classifieur de style en
    validation croisée par mondes (plis tirés par l'enfant (10, 0)) ; v6 (brouillon 3, § Métrique) : aires par pli, aires
    hors textes déjà vus à l'apprentissage (scores mis en commun), aire qui fait foi = la plus grande des aires par
    strate hors textes vus, comparée au seuil d'emploi ; textes plantés identiques entre mondes, par strate."""
    from .exact import frac_vers_texte
    etiquettes = ("VERITE_PLANTEE", "FAUX_TOT", "PIEGE", "TEMOIN_TRIVIAL", "TEMOIN_GROSSIER")
    regles = {"P9": regle_forme_seule, "P10": regle_borne_non_naturelle}
    sortie = {}
    for nom, regle in regles.items():
        tot = {e: [0, 0] for e in etiquettes}
        par_monde = []
        for m, plantes in banque:
            c = {e: [0, 0] for e in etiquettes}
            for p in plantes:
                v = int(regle(m.analyser(p.texte)))
                c[p.etiquette][0] += v
                c[p.etiquette][1] += 1
                tot[p.etiquette][0] += v
                tot[p.etiquette][1] += 1
            par_monde.append({e: [a, n] for e, (a, n) in c.items()})
        sortie[nom] = {"banque": {e: {"declares_faux": a, "plantes": n, "taux": _taux(a, n)} for e, (a, n) in tot.items()},
                       "par_monde": par_monde}
    # textes identiques entre mondes, par strate
    mondes_du_texte = {}
    for w, (_m, plantes) in enumerate(banque):
        for p in plantes:
            mondes_du_texte.setdefault((p.etiquette, p.texte), set()).add(w)
    repetes = {e: sum(1 for (et, _t), ws in mondes_du_texte.items() if et == e and len(ws) > 1) for e in etiquettes}
    # classifieur de style
    ordre = [int(i) for i in rng_plis.permutation(len(banque))]
    pli_de = {w: k % plis for k, w in enumerate(ordre)}
    analys = ("VERITE_PLANTEE", "FAUX_TOT", "PIEGE")
    tous = {e: [] for e in analys}
    hors_vus = {e: [] for e in analys}
    par_pli = []
    for k in range(plis):
        app = [(p.texte, p.etiquette != "VERITE_PLANTEE") for w, (_m, pl) in enumerate(banque) if pli_de[w] != k
               for p in pl if p.etiquette in analys]
        vus = {t for t, _ in app}
        modele = BayesNaif(Fraction(lissage)).apprendre([t for t, _ in app], [y for _, y in app])
        sc = {e: [] for e in analys}
        for w, (_m, pl) in enumerate(banque):
            if pli_de[w] == k:
                for p in pl:
                    if p.etiquette in analys:
                        s_ = modele.score(p.texte)
                        sc[p.etiquette].append(s_)
                        tous[p.etiquette].append(s_)
                        if p.texte not in vus:
                            hors_vus[p.etiquette].append(s_)
        par_pli.append({"pli": k, "aire_pieges_contre_verites": _f(aire_sous_la_courbe(sc["PIEGE"], sc["VERITE_PLANTEE"])),
                        "aire_faux_tot_contre_verites": _f(aire_sous_la_courbe(sc["FAUX_TOT"], sc["VERITE_PLANTEE"]))})
    aires_hv = {"pieges": aire_sous_la_courbe(hors_vus["PIEGE"], hors_vus["VERITE_PLANTEE"]),
                "faux_tot": aire_sous_la_courbe(hors_vus["FAUX_TOT"], hors_vus["VERITE_PLANTEE"])}
    definies = [a for a in aires_hv.values() if a is not None]
    foi = max(definies) if definies else None
    regle9 = sortie["P9"]["banque"]
    return {"regle_fixe": regle9, "regle_fixe_par_monde": sortie["P9"]["par_monde"],
            "borne_non_naturelle": sortie["P10"]["banque"], "borne_non_naturelle_par_monde": sortie["P10"]["par_monde"],
            "textes_identiques_entre_mondes": repetes,
            "classifieur_de_style": {
                "plis": plis, "lissage": str(lissage), "plis_par_monde": [pli_de[w] for w in range(len(banque))],
                "aire_pieges_contre_verites": _f(aire_sous_la_courbe(tous["PIEGE"], tous["VERITE_PLANTEE"])),
                "aire_faux_tot_contre_verites": _f(aire_sous_la_courbe(tous["FAUX_TOT"], tous["VERITE_PLANTEE"])),
                "par_pli": par_pli,
                "hors_textes_vus": {"aire_pieges_contre_verites": _f(aires_hv["pieges"]),
                                    "aire_faux_tot_contre_verites": _f(aires_hv["faux_tot"]),
                                    "effectifs": {e: len(v) for e, v in hors_vus.items()}},
                "aire_qui_fait_foi": _f(foi), "seuil_d_emploi": frac_vers_texte(Fraction(seuil_aire)),
                "au_dessus_du_seuil": None if foi is None else foi > Fraction(seuil_aire)}}


def _f(x):
    from .exact import frac_vers_texte
    return None if x is None else frac_vers_texte(x)


def _ecarts(nom, banque_taux, par_monde, attendu):
    sortie = []
    for k, v in attendu.items():
        a, n = banque_taux[k]["declares_faux"], banque_taux[k]["plantes"]
        if n == 0 or Fraction(a, n) != v:
            sortie.append(f"A1 ({nom}) : sur la banque, {k} : {a}/{n} au lieu de {v}")
    for w, c in enumerate(par_monde):
        for k, v in attendu.items():
            a, n = c[k]
            if n == 0 or Fraction(a, n) != v:
                sortie.append(f"A1 ({nom}) : monde {w}, {k} : {a}/{n} au lieu de {v}")
    return sortie


def ecarts_p9(mesure: dict) -> list[str]:
    """P9 (sur la banque et dans chaque monde, brouillon 3) : 1 sur les pièges, 1/2 sur les faux tôt et les vérités."""
    return _ecarts("P9", mesure["regle_fixe"], mesure.get("regle_fixe_par_monde", []),
                   {"PIEGE": Fraction(1), "FAUX_TOT": Fraction(1, 2), "VERITE_PLANTEE": Fraction(1, 2)})


def ecarts_p10(mesure: dict) -> list[str]:
    """P10 (brouillon 3) : 1 sur les pièges, 1/2 sur les faux tôt, 1/4 sur les vérités, sur la banque et par monde."""
    return _ecarts("P10", mesure["borne_non_naturelle"], mesure.get("borne_non_naturelle_par_monde", []),
                   {"PIEGE": Fraction(1), "FAUX_TOT": Fraction(1, 2), "VERITE_PLANTEE": Fraction(1, 4)})
