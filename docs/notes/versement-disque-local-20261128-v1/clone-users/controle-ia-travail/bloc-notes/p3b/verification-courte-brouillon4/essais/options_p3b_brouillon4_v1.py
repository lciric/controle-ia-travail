# Test mecanique des versions de repli du brouillon 4 de P3b (verificateur court, R2).
# Produit EN MEMOIRE le texte de chaque combinaison d'options des six decisions en attente, selon la regle de la puce
# « Statut », puis le controle : garde du scellement (blancs reduits, casse ignoree), debris de ponctuation,
# contradictions ciblees, doublons, `problemes` du validateur (appele sur le texte en memoire). Rien n'est ecrit.
# Lance par : PYTHONDONTWRITEBYTECODE=1 python3 -B -I options_p3b_brouillon4_v1.py [--detail COMBO]
import itertools
import re
import sys
from collections import Counter

sys.path.insert(0, "/home/user/controle-ia-travail/src")
import controle_ia.prereg as PR  # noqa: E402

TEXTE = ("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3b/brouillon4/"
         "P3b-seconde-lecture-v1-brouillon4.md")
T0 = open(TEXTE, encoding="utf-8").read()


class Echec(Exception):
    pass


def pat(s):
    return r"\s+".join(re.escape(x) for x in re.split(r"\s+", s))


def un(t, s, debut=0, fin=None):
    fin = len(t) if fin is None else fin
    ms = list(re.finditer(pat(s), t[debut:fin]))
    if len(ms) != 1:
        raise Echec(f"{len(ms)} occurrence(s) : {s[:70]!r}")
    return debut + ms[0].start(), debut + ms[0].end()


def rep(t, old, new, debut=0, fin=None):
    a, b = un(t, old, debut, fin)
    return t[:a] + new + t[b:]


def corps_guillemets(t, i):
    """t[i] == '«' : renvoie la fin (exclue) du texte entre guillemets equilibres."""
    if t[i] != "«":
        raise Echec("guillemet attendu")
    p = 0
    for j in range(i, len(t)):
        if t[j] == "«":
            p += 1
        elif t[j] == "»":
            p -= 1
            if p == 0:
                return j + 1
    raise Echec("guillemets non fermes")


def entre(t, ancre):
    """Premier texte entre guillemets apres l'ancre (sans les guillemets exterieurs)."""
    a, b = un(t, ancre)
    i = t.index("«", b)
    j = corps_guillemets(t, i)
    return t[i + 1:j - 1].strip()


def pos0(s):
    return re.search(pat(s), T0).start()


def norm(s):
    return re.sub(r"\s+", " ", s)


# ---------------------------------------------------------------- marqueurs
def retirer_marqueur(t, ident):
    # marqueur en gras seul (avec le « ; » qui l'introduit dans une parenthese), ou dans un titre en gras
    r1 = re.compile(r"(?: ;)?\s*\*\*\[Décision de Lazar\s+en\s+attente\s+:\s+" + re.escape(ident) + r"\b[^\]]*\]\*\*")
    r2 = re.compile(r"\s*\[Décision de Lazar\s+en\s+attente\s+:\s+" + re.escape(ident) + r"\b[^\]]*\](?=\*\*)")
    t, n1 = r1.subn("", t)
    t, n2 = r2.subn("", t)
    return t, n1 + n2


# ---------------------------------------------------------------- versions entre guillemets, en bloc
ETIQ = re.compile(r"(Version\s+\(A\),\s+écrite\s+ici|Version\s+\(A\),\s+recommandée|Version\s+\(a\)|Version\s+de\s+repli\s+\((?:B|C|C′|b|c|A)\)"
                  r"(?:\s+ou\s+\(C\))?\s+de\s+(?:P-017|P-016|N-031|N-032|P-024))\s+:\s*«")


def bloc_versions(t, debut_ancre, fin_ancre, garder):
    """Dans [debut_ancre, fin_ancre) : chaque version etiquetee et entre guillemets est retiree (avec l'espace qui la
    precede) sauf celle dont l'etiquette commence par `garder`, qui perd son etiquette et ses guillemets."""
    a = un(t, debut_ancre)[0]
    b = un(t, fin_ancre, a)[0] if fin_ancre else len(t)
    seg = t[a:b]
    out, k, vu = [], 0, []
    for m in ETIQ.finditer(seg):
        if m.start() < k:
            continue
        i = seg.index("«", m.start())
        j = corps_guillemets(seg, i)
        etiq = norm(m.group(1))
        vu.append(etiq)
        s = m.start()
        while s > k and seg[s - 1] in " \n":
            s -= 1
        out.append(seg[k:s])
        if garder is not None and etiq.startswith(garder):
            out.append(" " + seg[i + 1:j - 1].strip())
        k = j
    out.append(seg[k:])
    return t[:a] + "".join(out) + t[b:], vu


# ---------------------------------------------------------------- ecarts a la proposition 010
ROM = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]


def ecarts(t):
    a = un(t, "- **Écarts à la proposition 010**")[0]
    b = un(t, "Les numéros de ligne renvoient", a)[0]
    seg = norm(t[a:b])
    k = seg.index(") : (i) ") + 4
    tete, corps = seg[:k], seg[k:]
    morceaux = re.split(r"(?:^|(?<=; ))\(((?:i|ii|iii|iv|v|vi|vii|viii|ix|x))\) ", corps)
    items = []
    for n, x in zip(morceaux[1::2], morceaux[2::2]):
        x = x.strip()
        x = x[:-1].strip() if x.endswith(";") else x
        items.append([n, x])
    return a, b, tete, items


def ecarts_ecrire(t, a, b, tete, items):
    x = tete + " ; ".join(f"({n}) {c}" for n, c in items)
    if not x.endswith("."):
        x += "."
    return t[:a] + x + " " + t[b:]


# ---------------------------------------------------------------- operations des versions ecrites en remplacements
def op_p016_B_point1(t, v):
    corps = entre(v, "à la place du texte qui précède depuis « les 20 premiers » :")
    a = un(t, "1. **Partition** (R9)")[0]
    i = un(t, "les 20 premiers forment la découverte, les 40 suivants", a)[0]
    j = un(t, "La partition est écrite dans le manifeste", a)[0]
    return t[:i] + corps + " " + t[j:]


def op_n031(t, v, opt):
    # 1. G5 et premiere ligne de la synthese apres le prealable : « diagnostic » devient ...
    nouv = "tentative de détection non aveugle (N-031)"
    a, b = un(t, "| G5 : retenue")
    fl = t.index("\n", a)
    t = t[:a] + t[a:fl].replace("diagnostic", nouv, 1) + t[fl:]
    a, b = un(t, "| une sonde générique en G5 |")
    fl = t.index("\n", a)
    if t[a:fl].count("diagnostic") != 1:
        raise Echec("synthese G5 : diagnostic absent ou multiple")
    t = t[:a] + t[a:fl].replace("diagnostic", nouv, 1) + t[fl:]
    # 2. ecart (iv) : celui qui porte le numero (iv) au moment ou la version s'applique
    neuf = entre(v, "L'écart (iv) devient, en (b),") if opt == "b" else entre(v, "et, en (c),")
    a, b, tete, items = ecarts(t)
    k = [n for n, _ in items].index("iv")
    items[k][1] = neuf[len("(iv) "):]
    t = ecarts_ecrire(t, a, b, tete, items)
    # 3. reserves
    t = rep(t, "puissance du nul ;", "puissance du nul ; tentative non aveugle (N-031) ;")
    # 4. en (b), troisieme ligne de la synthese
    if opt == "b":
        a = un(t, "| oracle en O7, les deux sondes")[0]
        fl = t.index("\n", a)
        t = t[:a] + t[a:fl].replace("(diagnostic ;", "(tentative de détection non aveugle pour les sondes génériques, "
                                     "diagnostic pour l'oracle ;", 1) + t[fl:]
    return t


def op_n032_A(t, v):
    t = rep(t, "N-032 sans réponse vaut (C)) ; candidat",
            entre(v, "Version de repli (A) de N-032 :") + " candidat")
    t = rep(t, "contrôles avant dépense, dont M-P3b-2 (reconstitution sur processeur, règle de P3b-P0) ;",
            "contrôles avant dépense ;")
    return t


def op_p024_C_suite(t, v):
    a = un(t, "6. états à t_cost, 32 couches")[0]
    fl = un(t, "7. oracle :", a)[0]
    return rep(t, "jamais poussés", "poussés seuls, en morceaux, à leurs chemins et empreintes", a, fl)


def lecture_cellule_ajout(t, ligne, ajout):
    a = un(t, ligne)[0]
    fl = t.index("\n", a)
    l = t[a:fl]
    if not l.rstrip().endswith("|"):
        raise Echec("cellule")
    l = l.rstrip()[:-1].rstrip() + ajout + " |"
    return t[:a] + l + t[fl:]


def puce_contenu(t, debut, suivant):
    debut, suivant = debut.strip(), suivant.strip()
    a, b = un(t, debut)
    c = b + re.search(pat(suivant), t[b:]).start()
    return a, c


def op_p023_C(t, v):
    a, b, tete, items = ecarts(t)
    items = [it for it in items if it[0] != "vii"]
    t = ecarts_ecrire(t, a, b, tete, items)
    etiq = entre(v, "étiquettes :")
    a, c = puce_contenu(t, "  - étiquettes d'apprentissage (Q-06, Q-07) :", "  - choix (découverte seulement)")
    t = t[:a] + "- étiquettes d'apprentissage (Q-06, Q-07) : " + etiq + "\n  " + t[c:]
    aj = entre(v, "O6 et O7 ajoutent, à la fin de la lecture :")
    t = lecture_cellule_ajout(t, "| O6 :", " " + aj)
    t = lecture_cellule_ajout(t, "| O7 :", " " + aj)
    t = rep(t, "Action de la mention, ou toute étiquette de T1, dans un apprentissage de l'oracle : oracle en échec, motif écrit.",
            entre(v, "« Action de la mention, ou toute étiquette de T1 » devient :"))
    return t


def op_p023_B(t, v):
    # B1 ecarts
    a, b, tete, items = ecarts(t)
    items = [it for it in items if it[0] not in ("i", "ii", "v", "vi", "vii")]
    aj1 = entre(v, "deux écarts ajoutés à la liste :")
    aj2 = entre(v, "(écart déclaré) » et")
    items = [[ROM[k], c] for k, (_, c) in enumerate(items)]
    items += [[ROM[len(items)], aj1], [ROM[len(items) + 1], aj2]]
    t = ecarts_ecrire(t, a, b, tete, items)
    # B2 Seuil, premiere puce
    s1 = entre(v, "« Seuil », première puce :")
    a, c = puce_contenu(t, "- **« Au-dessus du plancher »**", "- **Famille principale")
    t = t[:a] + "- " + s1 + "\n" + t[c:]
    # B3 reserves de robustesse
    t = rep(t, entre(v, "« Réserves de robustesse reprises de l'addendum 1 de P3 » :"), entre(v, "spécification) » devient"))
    # B4 tableau hors perimetre
    a = un(t, "| excès d'aire apparié par tirage, en lecture décisive |")[0]
    fl = t.index("\n", a)
    t = t[:a] + t[fl + 1:]
    # B5 Oracle, entree et choix
    bloc = entre(v, "elle\n    sert au lecteur (a)) :")
    k = bloc.index("; choix (découverte seulement)")
    e_txt, c_txt = bloc[:k + 1].strip(), bloc[k + 2:].strip()
    a, c = puce_contenu(t, "  - entrée : état du flux résiduel au jeton t_cost", "  - estimateur :")
    t = t[:a] + "- " + e_txt + "\n  " + t[c:]
    a, c = puce_contenu(t, "  - choix (découverte seulement) :", "  - **validation croisée par tâche**")
    t = t[:a] + "- " + c_txt + " ;\n  " + t[c:]
    # B6 bandes
    t = rep(t, "Elles servent à l'oracle et à la double comptabilité.", entre(v, "« Bandes de couches », dernière phrase :"))
    # B7 etiquettes
    etiq = entre(v, "; étiquettes :")
    a, c = puce_contenu(t, "  - étiquettes d'apprentissage (Q-06, Q-07) :", "  - choix (découverte seulement)")
    t = t[:a] + "- étiquettes d'apprentissage (Q-06, Q-07) : " + etiq + " ;\n  " + t[c:]
    # B8 ligne O3b
    o3b = entre(v, "table O, ligne neuve après O3 :")
    a = un(t, "| O3 : au-dessus, non interprétable |")[0]
    fl = t.index("\n", a)
    t = t[:fl + 1] + o3b + "\n" + t[fl + 1:]
    # B9 O6 et O7
    aj = entre(v, "O6 et O7 ajoutent :")
    t = lecture_cellule_ajout(t, "| O6 :", " " + aj)
    t = lecture_cellule_ajout(t, "| O7 :", " " + aj)
    # B10, B11 : G6 et O5 (chaines citees dans la version, retirees telles quelles)
    for s in ["sinon T4 résiduel non calculable (recouvrement) → « le plan ne sépare pas le score du nombre écrit "
              "(recouvrement insuffisant) » ; ",
              "sinon T4 résiduel non établi (spécification) → « séparation qui dépend de la forme de la régression : "
              "non établie » ; ",
              " (ou « recouvrement insuffisant », motif écrit)",
              "T4 résiduel non établi (spécification) → « séparation qui dépend de la forme de la régression : non "
              "établie » ; sinon "]:
        if norm(s).strip() not in norm(v):
            raise Echec("chaine absente de la version (B) : " + s[:50])
        t = rep(t, s, "", un(t, "**Sondes génériques sur la fenêtre")[0])
    # B12 H-P3b-1
    t = rep(t, " (T4 de P3 corrigé du coût de la tâche et des coûts déjà déclarés, R-295)", "")
    # B13 H-P3b-2, G5, O7
    for anc, nouv in [("dans H-P3b-2,", "(T4 de P3 ; tâche et coûts déjà déclarés non contrôlés) »"),
                      ("dans G5,", "tâche et\n    coûts déjà déclarés non contrôlés) »"),
                      ("dans O7,", "(tâche et coûts déjà déclarés non contrôlés) »")]:
        a, b = un(v, anc)
        i = v.index("«", b); jf = corps_guillemets(v, i); old = v[i + 1:jf - 1].strip()
        k = v.index("devient", jf); i = v.index("«", k); jf = corps_guillemets(v, i); new = v[i + 1:jf - 1].strip()
        t = rep(t, old, new)
    # B14 puce T4 de P3
    a, c = puce_contenu(t, "- **T4 de P3** (descriptif)", "- **Double comptabilité**")
    t = t[:a] + "- " + entre(v, "puce « T4 de P3 (descriptif) » devient") + "\n" + t[c:]
    # B15 puce T4 residuel
    t = rep(t, "- **T4 résiduel** (R-295) :", "- (descriptif) **T4 résiduel** (R-295) :")
    # B16 renommage
    zones = [("- **H-P3b-1", "- **H-P3b-2"), ("- **H-P3b-2", "- **H-P3b-3"), ("| P3b-P2 ", "| P3b-P3 "),
             ("| P3b-P5 ", "| P3b-P6 "), ("- **Famille principale", "- **États d'un jeu"),
             ("3. **Lecture sur processeur**", "4. **Puissance**"), ("leur contrôle est T4 résiduel", None),
             ("**Sondes génériques sur la fenêtre pré-chiffre", "**Double comptabilité (lentille"),
             ("**Synthèse**", "Réserves (toujours écrites à part)")]
    for d, f in zones:
        a = un(t, d)[0]
        b = un(t, f, a)[0] if f else un(t, d)[1]
        seg = t[a:b]
        if "T4 résiduel" not in seg:
            raise Echec("renommage : rien dans " + d)
        t = t[:a] + seg.replace("T4 résiduel", "T4 de P3") + t[b:]
    # B17 P3b-P5
    t = rep(t, "aire du résidu de l'oracle au-dessus de son plancher",
            "aire de l'oracle stratifiée par quintiles du coût déclaré (T4 de P3) au-dessus de son plancher")
    # B18 partout, dans cet ordre
    for old in ["non séparé du nombre écrit, de la tâche ou de l'historique des coûts",
                "non séparé du nombre écrit, de la tâche ou de l'historique"]:
        n = len(re.findall(pat(old), t))
        if n == 0:
            raise Echec("partout : 0 " + old)
        t = re.sub(pat(old), "non séparé du nombre écrit", t)
    a = un(t, "| P3b-P5 ")[0]
    t = rep(t, "non séparé du nombre, de la tâche ou de l'historique", "non séparé du nombre écrit", a, t.index("\n", a))
    # B19 P3b-P9
    t = rep(t, "T4 de P3 (quintiles)", "T4 résiduel (deux spécifications, recouvrement)")
    # B20 liste d'arret
    t = rep(t, "Action de la mention, ou toute étiquette de T1, dans un apprentissage de l'oracle : oracle en échec, motif écrit.",
            entre(v, "liste d'arrêt, la puce qui commence par « Action de la mention, ou toute étiquette de T1 »\n    devient :"))
    # B21 phrase retiree
    t = rep(t, PHRASE_CHOIX, "")
    return t


PHRASE_CHOIX = ("Les choix de sonde de la version (A) (position W, Q-04 ; tous les pas en principal, Q-05 ; négatifs, Q-06 ; "
                "positifs, Q-07 ; bandes, Q-15) sont écrits en « Métrique », chacun avec un renvoi à P-023.")


# ---------------------------------------------------------------- construction d'un candidat
def candidat(o, ordre_inverse=False, litteral=True):
    """o : dict des options. Renvoie (texte, journal). `litteral` : les passages de la version (A) ou (C) qui ne portent
    pas d'etiquette restent (lecture a la lettre de la regle) ; sinon ce verificateur les remplace (lecture voulue)."""
    t = T0
    j = []
    attente = []  # versions retenues ecrites en remplacements : (position dans le texte d'origine, nom, fonction)
    # ---- marqueurs
    for ident, n_att in [("P-017", 1), ("P-016", 1), ("P-023", 5), ("N-031", 1), ("N-032", 1), ("P-024", 1)]:
        t, n = retirer_marqueur(t, ident)
        if n != n_att:
            raise Echec(f"marqueurs {ident} : {n}")
    # ---- P-017
    g = {"A": "Version (A), écrite ici", "B": "Version de repli (B) ou (C) de P-017", "C": "Version de repli (B) ou (C) de P-017",
         "C′": "Version de repli (C′) de P-017"}[o["P-017"]]
    t, vu = bloc_versions(t, "- **Périmètre au-delà de N-028.**", "- **Partition**", g)
    # ---- P-016
    g = {"A": "Version (A), recommandée", "B": "Version de repli (B) de P-016", "C": "Version de repli (C) de P-016"}[o["P-016"]]
    a = un(t, "- **Partition** :")[0]
    m = re.search(pat(g) + r" :\s*«", T0)
    i = T0.index("«", m.start())
    texte_partition = T0[i + 1:corps_guillemets(T0, i) - 1].strip()
    t, vu = bloc_versions(t, "- **Partition** :", "- **Écarts à la proposition 010**", g)
    # remplissage du marqueur de gabarit par le seul texte retenu (Q-02, CR-P3b-texte-15)
    t = t.replace("`<<PARTITION_P016>>`", texte_partition, 1)
    # passages en ligne de P-016
    B = o["P-016"] == "B"
    sites = [("(60 tâches ; Version de repli (B) de P-016 : 40)", "(60 tâches ; 40)", "(60 tâches)", "(40 tâches)"),
             ("`plis/lecture-60`, Version de repli (B) de P-016 : `plis/lecture-40` ; oracle",
              "`plis/lecture-60`, `plis/lecture-40` ; oracle", "`plis/lecture-60` ; oracle", "`plis/lecture-40` ; oracle"),
             ("sur 60 tâches (Version de repli (B) de P-016 : 40)", "sur 60 tâches (40)", "sur 60 tâches", "sur 40 tâches"),
             ("`plis/lecture-60` (Version de repli (B) de P-016 : `plis/lecture-40`)", "`plis/lecture-60` (`plis/lecture-40`)",
              "`plis/lecture-60`", "`plis/lecture-40`")]
    for old, lit_b, a_txt, voulu_b in sites:
        t = rep(t, old, (lit_b if litteral else voulu_b) if B else a_txt)
    # versions entre guillemets en ligne (base de lecture, leurre, validation croisee, synthese, liste d'arret)
    gB = "Version de repli (B) de P-016" if B else None
    for d, f in [("- **Action** :", "- **Pas lus**"), ("  - **validation croisée par tâche**", "  - **plancher de l'oracle**"),
                 ("| oracle en O7, les deux sondes", "| oracle en O4, O5 ou O6"), ("- Version de repli (B) de P-016 : « tout", "- Contrôle avant dépense M-P3b-2")]:
        t, vu = bloc_versions(t, d, f, gB)
    if not B:
        t = rep(t, "en descriptif ;)", "en descriptif)")
        t = re.sub(r"\n-[ \t]*\n(?=- Contrôle avant dépense M-P3b-2)", "\n", t)  # puce d'arret de la version (B) retiree
        t = re.sub(pat("\n-  tout chargement"), "\n- tout chargement", t)
    else:
        t = re.sub(r"\n-\s+tout chargement", "\n- tout chargement", t)
    if not litteral and B:
        t = rep(t, "les bras génériques (P3b-P1, P3b-P2) et la double comptabilité se lisent sur les 60 tâches",
                "les bras génériques (P3b-P1, P3b-P2) et la double comptabilité se lisent sur les 40 tâches")
        t = rep(t, " Plis de T4 résiduel des bras génériques : clé `plis/lecture-60`, 5 plis de 12 tâches.", "")
        t = rep(t, " 40 tâches pour les bras génériques et la double comptabilité ; plis de T4 résiduel des bras génériques : clé "
                "`plis/lecture-40`, 5 plis de 8 tâches.", " Plis de T4 résiduel des bras génériques : clé `plis/lecture-40`, 5 plis de 8 tâches.")
        t = rep(t, " Le leurre de la double comptabilité est tiré parmi les 60 tâches qu'elle lit, une fois par tâche.", "")
        t = rep(t, "sur la confirmation : 5 plis de 8 tâches ; l'oracle du pli k apprend, au réglage choisi, sur la découverte "
                "et les 4 autres plis, et note", "sur la confirmation : 5 plis de 4 tâches de confirmation ; l'oracle du pli k "
                "apprend sur la découverte et les 16 autres tâches de confirmation, et note")
        t = rep(t, " 5 plis de 4 tâches de confirmation ; l'oracle du pli k apprend sur la découverte et les 16 autres tâches "
                "de confirmation.", "")
        t = rep(t, "bras génériques lus sur 60 tâches, oracle sur les 40 de la confirmation, bras génériques sur la confirmation "
                "seule cités à côté, en descriptif ; bras génériques lus sur 40 tâches, oracle sur les 20 de la confirmation",
                "bras génériques lus sur 40 tâches, oracle sur les 20 de la confirmation, bras génériques sur la confirmation "
                "seule cités à côté, en descriptif")
    # point 1 du plan d'analyse : version ecrite en remplacements
    a, b = un(t, "Version de repli (B) de P-016, à la place du texte qui précède depuis « les 20 premiers » :")
    i = t.index("«", b)
    jfin = corps_guillemets(t, i)
    v016 = t[a:jfin]
    t = t[:a].rstrip(" ") + t[jfin:]
    if B:
        attente.append((pos0("Version de repli (B) de P-016, à la place"), "P-016 (B) point 1", lambda t, v=v016: op_p016_B_point1(t, v)))
    # ---- N-031
    g = {"a": "Version (a)", "b": "Version de repli (b) de N-031", "c": "Version de repli (c) de N-031"}[o["N-031"]]
    t, vu = bloc_versions(t, "- **Ce que P3b ne revendique pas.**", "## Hypothèse", g)
    a, b = un(t, "Versions de repli (b) et (c) de N-031, suite :")
    f = un(t, "## Hypothèse", a)[0]
    vsuite = t[a:f]
    t = t[:a].rstrip(" ") + "\n\n" + t[f:]
    t = re.sub(r"\n\n\n+## Hypothèse", "\n\n## Hypothèse", t)
    if o["N-031"] in "bc":
        attente.append((pos0("Versions de repli (b) et (c) de N-031, suite"), "N-031 suite",
                        lambda t, v=vsuite, x=o["N-031"]: op_n031(t, v, x)))
    # ---- N-032
    gA = {"A": "Version de repli (A) de N-032", "B": "Version de repli (B) de N-032", "C": None}[o["N-032"]]
    for d, f in [("  **Contrôle avant dépense M-P3b-2", "  **Contrôle négatif de la tolérance"),
                 ("- Contrôle avant dépense M-P3b-2 hors", "- Reconstitution au-delà des seuils")]:
        t, vu = bloc_versions(t, d, f, gA)
        if not litteral and o["N-032"] in "AB":
            # lecture voulue : la version (C) en clair est remplacee
            if d.startswith("  **"):
                a = un(t, "  **Contrôle avant dépense M-P3b-2")[0]
                b = t.index("nœud de Lazar.", a) + len("nœud de Lazar.")
                t = t[:a] + "  " + t[b:].lstrip()
            else:
                t = rep(t, "- Contrôle avant dépense M-P3b-2 hors de la règle de P3b-P0 : aucune création d'instance, nœud de "
                        "Lazar (N-032). ", "- ")
    a, b = un(t, "(Version de repli (A) de N-032 :")
    f = un(t, "- **Ce que la passe garde**", a)[0]
    par = t[a:f]
    vA = par[:par.index("Version de repli\n  (B)") if "Version de repli\n  (B)" in par else re.search(pat("Version de repli (B) de N-032"), par).start()]
    vB = par[re.search(pat("Version de repli (B) de N-032"), par).start():]
    if o["N-032"] == "A":
        attente.append((pos0("(Version de repli (A) de N-032 :"), "N-032 (A) ordre", lambda t, v=vA: op_n032_A(t, v)))
        t = t[:a].rstrip(" \n") + "\n" + t[f:]
    elif o["N-032"] == "B":
        reste = norm(vB)[len("Version de repli (B) de N-032 : "):].strip()
        reste = reste[:-2] if reste.endswith(".)") else reste
        if litteral:
            # la version (B) ne contient aucun des mots de la regle (« devient », « à la place de », « est retiré »,
            # « remplacements mot pour mot ») : elle reste, sans son etiquette
            t = t[:a] + "(" + reste + ".)\n" + t[f:]
        else:
            t = t[:a].rstrip(" \n") + "\n" + t[f:]
            mesure = entre(vB, "avec")
            vA2 = vA.replace("mesure M-P3b-2 avant le scellement (par\n  condition, règle de P3b-P0, sortie\n  brute scellée)", mesure)
            vA2 = re.sub(pat("mesure M-P3b-2 avant le scellement (par condition, règle de P3b-P0, sortie brute scellée)"), mesure, vA2)
            attente.append((pos0("(Version de repli (A) de N-032 :"), "N-032 (B) ordre", lambda t, v=vA2: op_n032_A(t, v)))
    else:
        t = t[:a].rstrip(" \n") + "\n" + t[f:]
    # ---- P-024
    gP = {"A": "Version (A), écrite ici", "B": "Version de repli (B) de P-024", "C": "Version de repli (C) de P-024"}[o["P-024"]]
    t, vu = bloc_versions(t, "- **États à t_cost.", "## Contre-lecture", gP)
    a, b = un(t, "Version de repli (C) de P-024, suite :")
    f = un(t, "Dans tous", a)[0]
    vs = t[a:f]
    t = t[:a].rstrip(" ") + " " + t[f:]
    if o["P-024"] == "C":
        attente.append((pos0("Version de repli (C) de P-024, suite"), "P-024 (C) suite", lambda t, v=vs: op_p024_C_suite(t, v)))
    PB = o["P-024"] == "B"
    for old, lit, a_txt, voulu in [
            ("(borne de l'étape : 7,5 USD ; Version de repli (B) de P-024 : 8,6 USD)", "(borne de l'étape : 7,5 USD ; 8,6 USD)",
             "(borne de l'étape : 7,5 USD)", "(borne de l'étape : 8,6 USD)"),
            ("borne de l'étape 7,5 USD (Version de repli (B) de P-024 : 8,6 USD)", "borne de l'étape 7,5 USD (8,6 USD)",
             "borne de l'étape 7,5 USD", "borne de l'étape 8,6 USD"),
            ("+ 1,2 USD (Version de repli (B) de P-024 : + 2,16 USD)", "+ 1,2 USD (+ 2,16 USD)", "+ 1,2 USD", "+ 1,2 USD + 2,16 USD"),
            ("(7,5 USD ; Version de repli (B) de P-024 : 8,6 USD)", "(7,5 USD ; 8,6 USD)", "(7,5 USD)", "(8,6 USD)")]:
        t = rep(t, old, (lit if litteral else voulu) if PB else a_txt)
    # ---- P-023 : versions (C) et (B) en sous-puces, ecrites en remplacements
    a = un(t, "  - **Version de repli (C) de P-023**")[0]
    b = un(t, "  - **Version de repli (B) de P-023**", a)[0]
    f = un(t, "- **Hors périmètre, sauf décision contraire de Lazar**", b)[0]
    vC, vBB = t[a:b], t[b:f]
    t = t[:a] + t[f:]
    if o["P-023"] == "C":
        attente.append((pos0("**Version de repli (C) de P-023**"), "P-023 (C)", lambda t, v=vC: op_p023_C(t, v)))
    if o["P-023"] == "B":
        attente.append((pos0("**Version de repli (B) de P-023**"), "P-023 (B)", lambda t, v=vBB: op_p023_B(t, v)))
    # ---- phase 2 : versions retenues ecrites en remplacements
    attente.sort(key=lambda x: x[0], reverse=ordre_inverse)
    for _, nom, fn in attente:
        t = fn(t)
        j.append(nom)
    # ---- phase 3 : phrases retirees (liste de la puce « Statut ») ; absence toleree (deja retiree par une version)
    for s in [" Au candidat, pour chaque décision marquée « [Décision de Lazar en attente : …] », le marqueur et les "
              "versions non retenues sont retirés ; la version retenue reste seule, mot pour mot, sans son étiquette "
              "(« Version (A), écrite ici : », « Version (A), recommandée : », « Version (a) : », « Version de repli … : ») ni ses "
              "guillemets ; une version retenue écrite comme des remplacements (« devient », « à la place de », « est retiré », "
              "« remplacements mot pour mot ») ne reste pas : elle s'applique mot pour mot au texte principal, après le retrait "
              "des marqueurs et des autres versions, puis elle est retirée.",
              " Au candidat, les phrases qui ne décrivent que ce retrait ou des versions non retenues (la phrase « Au candidat, "
              "pour chaque décision marquée … puis elle est retirée. », celle-ci, la dernière phrase de la puce « Partition », "
              "la phrase « Les choix de sonde de la version (A) … chacun avec un renvoi à P-023. » et les trois renvois "
              "« (Version de repli (B) de P-023 … section « Périmètre ».) » de « Seuil », de la table O et de la liste "
              "d'arrêt) sont retirées aussi : le scellement refuse « en attente » et « de repli », sans égard à la casse ni "
              "aux retours à la ligne.",
              " Chaque passage qui dépend de la partition porte sa version (B) à côté, sous la mention « Version de repli (B) "
              "de P-016 » ; le texte scellé ne garde que la version retenue.",
              " " + PHRASE_CHOIX,
              " (Version de repli (B) de P-023 : section « Périmètre ».)",
              "\n(Version de repli (B) de P-023 et Version de repli (C) de P-023, pour O3b, O6 et O7 : section « Périmètre ».)\n",
              "\n (Version de repli (B) de P-023 et Version de repli (C) de P-023 : section « Périmètre ».)"]:
        ms = list(re.finditer(pat(s), t)) if not s.startswith("\n") else list(re.finditer(r"\s*" + pat(s.strip()), t))
        if len(ms) > 1:
            raise Echec("phrase retiree multiple")
        if ms:
            t = t[:ms[0].start()] + t[ms[0].end():]
    return t, j


# ---------------------------------------------------------------- controles
GARDE = re.compile(r"en attente|de repli|proposition en attente")
DEBRIS = {"parenthèse vide": r"\(\s*\)", "« ; » avant « ) »": r"\s;\s*\)", "« ( » puis « ; »": r"\(\s*;",
          "« ; ; »": r";\s*;", "« . . »": r"\.\s+\.(?!\.)", "double point": r"(?<!\.)\.\.(?!\.)", "espace avant « . »": r"[^\s\d] \.(?!\d)",
          "« ) . »": r"\)\s+\.", "« ;. »": r";\s*\.", "« , ; »": r",\s*;", "triple saut": r"\n\n\n",
          "double espace": r"(?<=\S)  +(?=\S)", "puce vide": r"\n-\s*\n"}
MOTS = [r"[Vv]ersion \(", r"version retenue", r"versions? non retenues?", r"écrite ici", r"recommandée\b", r"\boptions? de P-0",
        r"\ben \((?:A|B|C|b|c|C′)\)", r"\bsuite :", r"de même, avec", r"défaut \(A\)", r"\(B\) de P-0", r"\(C\) de P-0"]


def debris(t):
    return Counter({k: len(re.findall(p, t)) for k, p in DEBRIS.items()})


BASE_DEBRIS = debris(T0)


def faux_chemin(texte):
    class F:
        def read_text(self, encoding=None):
            return texte
    return F()


PR.Path = lambda x: x  # le validateur lit le texte en memoire (aucun fichier ecrit)
BASE_PB = PR.problemes(faux_chemin(T0))


def gabarits(pb):
    for p in pb:
        if p.startswith("marqueurs de gabarit restants"):
            return set(p.split(" : ", 1)[1].split(", "))
    return set()


def contradictions(t, o):
    n = norm(t)
    r = []

    def absent(s, motif):
        if s in n:
            r.append(motif + f" : « {s} » présent")
    if o["P-016"] == "B":
        for s in ["plis/lecture-60", "5 plis de 12 tâches", "les 40 suivants", "sur 60 tâches", "(60 tâches", "oracle sur les 40",
                  "(5 × 8)", "5 plis de 8 tâches ; l'oracle", "parmi les 60 tâches"]:
            absent(s, "P-016 (B)")
    else:
        for s in ["plis/lecture-40", "tâches réservées", "20 derniers", "16 autres tâches", "tâche réservée (score"]:
            absent(s, f"P-016 ({o['P-016']})")
    if o["N-032"] in "AB":
        for s in ["Contrôle avant dépense M-P3b-2", "dont M-P3b-2", "de même, avec"]:
            absent(s, f"N-032 ({o['N-032']})")
        if o["N-032"] == "B" and "Mesure avant le scellement" not in n:
            r.append("N-032 (B) : mesure absente")
    else:
        for s in ["Mesure avant le scellement", "Mesure M-P3b-2 avant", "Compte unique M-P3b-2"]:
            absent(s, "N-032 (C)")
    if o["P-024"] == "B":
        for s in ["7,5 USD"]:
            absent(s, "P-024 (B)")
    else:
        for s in ["8,6 USD", "2,16 USD"]:
            absent(s, f"P-024 ({o['P-024']})")
    if o["P-024"] == "C" and "disque de l'instance seulement** (scellés, poussés" in n:
        r.append("P-024 (C) : étape 2.6 « sur le disque de l'instance seulement » et « poussés »")
    if o["P-023"] in "BC":
        absent("T1 reste un test : les étiquettes de T1 n'entrent dans aucun apprentissage", f"P-023 ({o['P-023']})")
    if o["P-023"] == "B":
        for s in ["sur les 32 couches, est au-dessus", "T4 résiduel établis |", "et T4 résiduel ;", "passe T1, T3 et T4 résiduel"]:
            absent(s, "P-023 (B)")
    if o["P-023"] == "C" and "(vi)" in n and "(vii)" not in n and "(viii)" in n:
        r.append("P-023 (C) : écarts numérotés (vi) puis (viii)")
    if o["N-031"] in "bc":
        absent("lecture en diagnostic, aucune revendication ni règle pour G0", f"N-031 ({o['N-031']})")
        if "graines dérivées de l'entropie de P3b" not in n:
            r.append(f"N-031 ({o['N-031']}) : écart des graines remplacé")
        if "tentative de détection déclarée non aveugle" not in n:
            r.append(f"N-031 ({o['N-031']}) : écart (iv) neuf absent")
    if o["P-017"] == "B":
        absent("(et, en (C), le rejeu contrefactuel 2 × 2)", "P-017 (B)")
    # doublons
    if o["P-016"] in "AB":
        g = {"A": "Version (A), recommandée", "B": "Version de repli (B) de P-016"}[o["P-016"]]
        m = re.search(pat(g) + r" :\s*«", T0)
        i = T0.index("«", m.start())
        x = norm(T0[i + 1:corps_guillemets(T0, i) - 1].strip())
        if n.count(x) > 1:
            r.append(f"P-016 ({o['P-016']}) : texte de la partition écrit {n.count(x)} fois")
    return r


def controler(t, o):
    pb = PR.problemes(faux_chemin(t))
    garde = sorted(set(m.group(0).lower() for m in GARDE.finditer(norm(t).lower())))
    d = debris(t) - BASE_DEBRIS
    neuf_pb = [p for p in pb if not p.startswith("marqueurs de gabarit") and p not in BASE_PB]
    gab_neufs = gabarits(pb) - gabarits(BASE_PB)
    return {"garde": garde, "debris": dict(d), "contradictions": contradictions(t, o), "problemes_neufs": neuf_pb + sorted(gab_neufs)}


OPTIONS = {"N-031": ["a", "b", "c"], "N-032": ["A", "B", "C"], "P-016": ["A", "B", "C"], "P-017": ["A", "B", "C", "C′"],
           "P-023": ["A", "B", "C"], "P-024": ["A", "B", "C"]}
RECO = {"N-031": "a", "N-032": "C", "P-016": "A", "P-017": "A", "P-023": "A", "P-024": "A"}


def nom(o):
    return " ".join(f"{k}={v}" for k, v in o.items())


def main():
    detail = "--detail" in sys.argv
    print("problemes du brouillon 4 (base) :", BASE_PB[0], "+", len(gabarits(BASE_PB)), "marqueurs de gabarit")
    for litteral in (True, False):
        lab = "LECTURE A LA LETTRE" if litteral else "LECTURE VOULUE (passages sans etiquette remplaces par ce verificateur)"
        print("\n==========", lab)
        bilan = Counter()
        exemples = {}
        n_ordre = 0
        combos = list(itertools.product(*OPTIONS.values()))
        for c in combos:
            o = dict(zip(OPTIONS, c))
            try:
                t1, j1 = candidat(o, False, litteral)
                t2, j2 = candidat(o, True, litteral)
            except Echec as e:
                bilan["echec mecanique : " + str(e)[:90]] += 1
                exemples.setdefault("echec mecanique : " + str(e)[:90], nom(o))
                continue
            if t1 != t2:
                n_ordre += 1
                exemples.setdefault("ordre", nom(o))
            r = controler(t1, o)
            for g in r["garde"]:
                bilan["garde : " + g] += 1
                exemples.setdefault("garde : " + g, nom(o))
            for k, v in r["debris"].items():
                if v > 0:
                    bilan["debris : " + k] += 1
                    exemples.setdefault("debris : " + k, nom(o))
            for x in r["contradictions"]:
                bilan["contradiction : " + x] += 1
                exemples.setdefault("contradiction : " + x, nom(o))
            for x in r["problemes_neufs"]:
                bilan["probleme neuf : " + x] += 1
                exemples.setdefault("probleme neuf : " + x, nom(o))
            if not (r["garde"] or any(v > 0 for v in r["debris"].values()) or r["contradictions"] or r["problemes_neufs"]):
                bilan["combinaison sans defaut detecte"] += 1
        print(f"combinaisons essayees : {len(combos)} (chacune dans deux ordres d'application des versions en remplacements)")
        print(f"resultat different selon l'ordre : {n_ordre}" + (f" (ex. {exemples['ordre']})" if n_ordre else ""))
        for k, v in sorted(bilan.items()):
            print(f"  {v:4d}  {k}" + (f"   [ex. {exemples.get(k)}]" if k in exemples else ""))
    if detail:
        for c in [RECO] + [dict(RECO, **{k: v}) for k in OPTIONS for v in OPTIONS[k] if v != RECO[k]]:
            t, _ = candidat(c, False, True)
            r = controler(t, c)
            print("\n--", nom(c), r)
            n = norm(t)
            for mot in MOTS:
                for m in re.finditer(mot, n):
                    x = n[max(0, m.start() - 70):m.end() + 50]
                    if norm(x) not in norm(T0) or True:
                        print("   mot", repr(mot), ":", x)


if __name__ == "__main__":
    main()
