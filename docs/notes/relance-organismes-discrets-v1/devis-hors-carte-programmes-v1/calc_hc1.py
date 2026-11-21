#!/usr/bin/env python3
# calc_hc1.py -- chiffres du devis des lectures hors carte du bras A, brouillon 1.
# Arithmetique exacte (fractions). Aucune lecture de fichier, aucun reseau.
# Entrees : volumes de la section 6.11 du texte (brouillon 43), longueurs de la
# section 6.2 du devis des essais d'admission, tarifs des pages de prix versees.
# Sortie : une trace lisible (stdout) et, avec --json, les valeurs formatees
# que le programme d'assemblage insere dans le devis.
from fractions import Fraction as F
import json
import math
import sys

M = 1_000_000

# ---------------------------------------------------------------- formats
def _arr(x, nd, mode):
    q = F(10) ** nd
    y = F(x) * q
    if mode == "sup":
        n = math.ceil(y)
    elif mode == "inf":
        n = math.floor(y)
    else:  # demi superieur
        n = math.floor(y + F(1, 2))
    return F(n, q)


def fr(x, nd=2, mode="demi"):
    """Nombre au format francais : virgule decimale, espace des milliers."""
    v = _arr(x, nd, mode)
    neg = v < 0
    v = abs(v)
    ent = v.numerator // v.denominator
    dec = v - ent
    s = f"{ent:,}".replace(",", " ")
    if nd > 0:
        d = str(int(dec * (F(10) ** nd))).rjust(nd, "0")
        s = s + "," + d
    return ("-" if neg else "") + s


def ent(n):
    return f"{int(n):,}".replace(",", " ")


def sup5(x):
    return int(math.ceil(F(x) / 5) * 5)


def sup_demi(x):
    return F(math.ceil(F(x) * 2), 2)


OUT = {}
TRACE = []


def t(line=""):
    TRACE.append(line)


def put(key, val):
    if key in OUT:
        raise SystemExit("cle en double : " + key)
    OUT[key] = val


# ---------------------------------------------------------------- 1. volumes
# (nom du texte, appels par lecteur au plus, instrument, phase)
LOTS = [
    ("honnête de l'appariement", 896, "a", "epreuve", "640 + 128 + 64 + 64"),
    ("jumeaux d'épreuve de l'appariement", 1280, "a", "epreuve", "640 + 640"),
    ("honnête de la couverture", 64, "c", "epreuve", "64"),
    ("quatre épreuves mécaniques de la couverture", 128, "c", "epreuve", "128"),
    ("jumeaux d'épreuve de la couverture", 128, "c", "epreuve", "128"),
    ("décisif, appariement", 8960, "a", "decisif", "7 × 128 × 10"),
    ("décisif, sentinelles et relues", 576, "a", "decisif", "256 + 320"),
    ("décisif, couverture et ses sentinelles", 928, "c", "decisif", "896 + 32"),
    ("révision (tâches gardées, lots de l'appariement)", 2176, "a", "revision", "2 176"),
]
assert 640 + 128 + 64 + 64 == 896 and 640 + 640 == 1280 and 7 * 128 * 10 == 8960
assert 256 + 320 == 576 and 896 + 32 == 928

PHASES = ["epreuve", "decisif", "revision"]
NOM_PHASE = {"epreuve": "lots d'épreuve", "decisif": "lots décisifs", "revision": "lots de la révision"}


def compte(phase=None, instr=None, sans_revision=False):
    n = 0
    for nom, k, i, p, _ in LOTS:
        if phase is not None and p != phase:
            continue
        if instr is not None and i != instr:
            continue
        if sans_revision and p == "revision":
            continue
        n += k
    return n


N = {p: (compte(p, "a"), compte(p, "c")) for p in PHASES}
tot_sans = compte(sans_revision=True)
tot_avec = compte()
assert tot_sans == 12960, tot_sans
assert 2 * tot_sans == 25920
assert N["revision"] == (2176, 0) and 2 * 2176 == 4352
assert compte(instr="a") == 13888 and compte(instr="c") == 1248  # grandeur C du devis de l'essai de mesure
assert tot_avec == 15136
JUGE = (48, 24, 8)
JUGE_REV = 72
assert sum(JUGE) == 80 and sum(JUGE) + JUGE_REV == 152
ENVOIS_MAX = 3
assert ENVOIS_MAX * (25920 + 4352 + 152) == 91272  # majorant vrai des envois, 6.11

t("== 1. Volumes (section 6.11 du texte, brouillon 43)")
for nom, k, i, p, f_ in LOTS:
    t(f"  {nom} : {ent(k)} appels par lecteur ({f_}) ; instrument {'appariement' if i == 'a' else 'couverture'} ; {NOM_PHASE[p]} ; deux lecteurs : {ent(2 * k)}")
for p in PHASES:
    a, c = N[p]
    t(f"  {NOM_PHASE[p]} : appariement {ent(a)} + couverture {ent(c)} = {ent(a + c)} par lecteur ; deux lecteurs {ent(2 * (a + c))} ; envois au plus {ent(3 * (a + c))} par lecteur")
t(f"  par lecteur : {ent(tot_sans)} sans révision, {ent(tot_avec)} avec ; appariement {ent(compte(instr='a'))}, couverture {ent(compte(instr='c'))}")
t(f"  deux lecteurs : {ent(2 * tot_sans)} sans révision ; révision {ent(2 * 2176)} ; avec révision {ent(2 * tot_avec)}")
t(f"  juge des ancres : 48 + 24 + 8 = 80 appels ; 72 de plus sous la révision ; 152 au plus")
t(f"  majorant des envois : 3 × (25 920 + 4 352 + 152) = {ent(91272)}")

rows = []
for nom, k, i, p, f_ in LOTS:
    rows.append(f"| {nom} | {'appariement' if i == 'a' else 'couverture'} | {NOM_PHASE[p]} | {f_ if f_.replace(' ', '') != str(k) else ''}{' = ' if f_.replace(' ', '') != str(k) else ''}{ent(k)} | {ent(2 * k)} |")
rows.append(f"| **total sans révision** | | | **{ent(tot_sans)}** | **{ent(2 * tot_sans)}** |")
rows.append(f"| **total avec révision** | | | **{ent(tot_avec)}** | **{ent(2 * tot_avec)}** |")
put("T_VOL", "\n".join(rows))

rows = []
for p in PHASES:
    a, c = N[p]
    rows.append(f"| {NOM_PHASE[p]} | {ent(a)} | {ent(c)} | {ent(a + c)} | {ent(3 * (a + c))} | {ent(2 * (a + c))} |")
rows.append(f"| **par lecteur, sans révision** | {ent(compte(instr='a', sans_revision=True))} | {ent(compte(instr='c'))} | **{ent(tot_sans)}** | {ent(3 * tot_sans)} | **{ent(2 * tot_sans)}** |")
rows.append(f"| **par lecteur, avec révision** | {ent(compte(instr='a'))} | {ent(compte(instr='c'))} | **{ent(tot_avec)}** | {ent(3 * tot_avec)} | **{ent(2 * tot_avec)}** |")
put("T_PHASE", "\n".join(rows))

# ---------------------------------------------------------------- 2. longueurs
EA = F(23625, 18)   # jetons d'entree, appariement, compte de Claude (somme / 18 entrees)
EC = F(31591, 6)    # couverture, compte de Claude (somme / 6 entrees)
GA = F(5159, 6)     # appariement, compte de Google, six entrees de la file du juge
GC = F(7933, 2)     # couverture, compte de Google, deux entrees de la file du juge
BA, BC = 5000, 24000  # bornes en octets du corps (S), un jeton par octet au pire
SA, SC = 2000, 4000   # sorties supposees (S), comme au devis des essais d'admission

t()
t("== 2. Longueurs (devis des essais d'admission, 6.2 ; 24 entrées synthétiques)")
t(f"  compte de Claude : appariement 23 625 / 18 = {fr(EA, 2)} ; couverture 31 591 / 6 = {fr(EC, 2)} ; rapport {fr(EC / EA, 2)}")
t(f"  compte de Google (file du juge) : appariement 5 159 / 6 = {fr(GA, 2)} ; couverture 7 933 / 2 = {fr(GC, 2)}")
put("EA", fr(EA, 1))
put("EC", fr(EC, 1))
put("GA", fr(GA, 1))
put("GC", fr(GC, 1))
put("RATIO_E", fr(EC / EA, 2))


def jetons_entree(a, c, ea=EA, ec=EC):
    return a * ea + c * ec


tok = {p: jetons_entree(*N[p]) for p in PHASES}
tok_lecteur_avec = sum(tok.values())
tok_lecteur_sans = tok["epreuve"] + tok["decisif"]
for p in PHASES:
    t(f"  jetons d'entrée par lecteur, {NOM_PHASE[p]} : {ent(round(tok[p]))}")
t(f"  par lecteur : {ent(round(tok_lecteur_sans))} sans révision ; {ent(round(tok_lecteur_avec))} avec")
t(f"  deux lecteurs : {ent(round(2 * tok_lecteur_sans))} sans révision ; {ent(round(2 * tok_lecteur_avec))} avec")
tok_juge_80 = 72 * GA + 8 * GC
tok_juge_152 = 144 * GA + 8 * GC
t(f"  juge, répartition inférée 72 d'appariement et 8 de couverture : {ent(round(tok_juge_80))} ; avec la révision (144 et 8) : {ent(round(tok_juge_152))}")
CTX, ACT = 2643, 223
LECT_MON = CTX + ACT
assert LECT_MON == 2866
tok_mon = 6400 * LECT_MON
tok_mon_temoins = 8960 * LECT_MON
t(f"  moniteur par action en contexte : 6 400 × (2 643 + 223) = {ent(tok_mon)} ; 8 960 × 2 866 = {ent(tok_mon_temoins)} si les deux témoins sont lus ; consigne non comptée")
tot_tok_avec = 2 * tok_lecteur_avec + tok_juge_152 + 2 * tok_mon
tot_tok_sans = 2 * tok_lecteur_sans + tok_juge_80 + 2 * tok_mon
t(f"  total d'entrée, un envoi par appel : sans révision {fr(tot_tok_sans / M, 1)} millions ; avec révision {fr(tot_tok_avec / M, 1)} millions ; avec les témoins au moniteur {fr((tot_tok_avec - tok_mon + tok_mon_temoins) / M, 1)} millions")
put("TOK_L_EPR", fr(tok["epreuve"] / M, 2))
put("TOK_L_DEC", fr(tok["decisif"] / M, 2))
put("TOK_L_REV", fr(tok["revision"] / M, 2))
put("TOK_L_SANS", fr(tok_lecteur_sans / M, 1))
put("TOK_L_AVEC", fr(tok_lecteur_avec / M, 1))
put("TOK_2L_SANS", fr(2 * tok_lecteur_sans / M, 1))
put("TOK_2L_AVEC", fr(2 * tok_lecteur_avec / M, 1))
put("TOK_JUGE_80", ent(round(tok_juge_80)))
put("TOK_JUGE_152", ent(round(tok_juge_152)))
put("TOK_MON", fr(F(tok_mon, M), 1))
put("TOK_MON_EXACT", ent(tok_mon))
put("TOK_MON_TEMOINS", fr(F(tok_mon_temoins, M), 1))
put("TOK_2MON", fr(F(2 * tok_mon, M), 1))
put("TOT_TOK_SANS", fr(tot_tok_sans / M, 0))
put("TOT_TOK_AVEC", fr(tot_tok_avec / M, 0))
put("TOT_TOK_TEMOINS", fr((tot_tok_avec - tok_mon + tok_mon_temoins) / M, 0))

# ---------------------------------------------------------------- 3. tarifs
MIS_PE_LISTE, MIS_PS_LISTE = F(70, 100), F(210, 100)
MIS_PE, MIS_PS = MIS_PE_LISTE * F(11, 10), MIS_PS_LISTE * F(11, 10)
assert (MIS_PE, MIS_PS) == (F(77, 100), F(231, 100))
NEO_PE, NEO_PS = F(3), F(15)
K_RED = F(13, 12)  # un envoi, plus le taux de non-conformite le plus haut que l'admission permet (2 sur 24)

t()
t("== 3. Tarifs comptés (USD par million de jetons)")
t(f"  Mistral Large 4 : fiche 0,70 et 2,10 ; point d'accès européen × 1,1 = {fr(MIS_PE)} et {fr(MIS_PS)}")
t(f"  gemini-4-neon, offre payante, service courant : {fr(NEO_PE, 0)} et {fr(NEO_PS, 0)}")
t(f"  redemandes : k = 1 + 2/24 = {fr(K_RED, 4)}")


def cout_appel(e, s, pe, ps):
    return (e * pe + s * ps) / M


def cout(a, c, pe, ps, ea, ec, sa=SA, sc=SC, k=F(1)):
    return k * (a * cout_appel(ea, sa, pe, ps) + c * cout_appel(ec, sc, pe, ps))


# recoupe des chiffres du devis des essais d'admission (6.3)
r_mis = cout(18, 6, MIS_PE, MIS_PS, EA, EC)
r_neo = cout(6, 2, NEO_PE, NEO_PS, GA, GC)
assert fr(r_mis) == "0,18" and fr(r_neo) == "0,34", (fr(r_mis), fr(r_neo))
res_mis_a = (BA * MIS_PE + 32768 * MIS_PS) / M
res_mis_c = (BC * MIS_PE + 32768 * MIS_PS) / M
res_neo_a = (BA * NEO_PE + 32768 * NEO_PS) / M
res_neo_c = (BC * NEO_PE + 32768 * NEO_PS) / M
assert (fr(res_mis_a, 3), fr(res_mis_c, 3)) == ("0,080", "0,094")
assert (fr(res_neo_a, 3, "sup"), fr(res_neo_c, 3, "sup")) == ("0,507", "0,564")
t(f"  recoupe du devis des essais d'admission : attendu file Mistral {fr(r_mis)} (devis : 0,18) ; file Neon {fr(r_neo)} (devis : 0,34) ; envoi à 32 768 : Mistral {fr(res_mis_a, 3)} et {fr(res_mis_c, 3)} (devis : 0,080 ; 0,094) ; Neon {fr(res_neo_a, 3, 'sup')} et {fr(res_neo_c, 3, 'sup')} (devis : 0,507 ; 0,564)")

# ---------------------------------------------------------------- 4. lecteur 2 (Mistral)
t()
t("== 4. Second lecteur, Mistral Large 4 (0,77 et 2,31 ; sorties supposées 2 000 et 4 000)")
ca_m = cout_appel(EA, SA, MIS_PE, MIS_PS)
cc_m = cout_appel(EC, SC, MIS_PE, MIS_PS)
t(f"  coût d'un appel, un envoi : appariement {fr(ca_m, 6)} ; couverture {fr(cc_m, 6)} ; rapport {fr(cc_m / ca_m, 2)}")
put("CA_M", fr(ca_m * 1000, 2))
put("CC_M", fr(cc_m * 1000, 2))
E2 = {}
E2K = {}
for p in PHASES:
    a, c = N[p]
    E2[p] = cout(a, c, MIS_PE, MIS_PS, EA, EC)
    E2K[p] = cout(a, c, MIS_PE, MIS_PS, EA, EC, k=K_RED)
    ent_usd = (a * EA + c * EC) * MIS_PE / M
    sor_tok = a * SA + c * SC
    sor_usd = sor_tok * MIS_PS / M
    t(f"  {NOM_PHASE[p]} : entrée {ent(round(a * EA + c * EC))} jetons = {fr(ent_usd)} USD ; sortie {ent(sor_tok)} jetons = {fr(sor_usd)} USD ; un envoi par appel {fr(E2[p])} ; avec redemandes {fr(E2K[p])}")
    put(f"L2_SOR_{p.upper()}", fr(F(sor_tok, M), 2))
    put(f"L2_E1_{p.upper()}", fr(E2[p]))
    put(f"L2_EK_{p.upper()}", fr(E2K[p]))
e2_sans = E2["epreuve"] + E2["decisif"]
e2_avec = sum(E2.values())
e2k_sans = E2K["epreuve"] + E2K["decisif"]
e2k_avec = sum(E2K.values())
t(f"  total, un envoi par appel : {fr(e2_sans)} sans révision ; {fr(e2_avec)} avec")
t(f"  total, avec redemandes : {fr(e2k_sans)} sans révision ; {fr(e2k_avec)} avec")
sor2_tot = sum(N[p][0] * SA + N[p][1] * SC for p in PHASES)
t(f"  sortie supposée, trois phases : {ent(sor2_tot)} jetons")
put("L2_E1_SANS", fr(e2_sans))
put("L2_E1_AVEC", fr(e2_avec))
put("L2_EK_SANS", fr(e2k_sans))
put("L2_EK_AVEC", fr(e2k_avec))
put("L2_SOR_TOT", fr(F(sor2_tot, M), 2))

# sensibilite a la sortie moyenne
t("  sensibilité à la sortie moyenne (avec redemandes, trois phases) :")
rows = []
for mult in (F(1, 2), F(1), F(2), F(3), F(4)):
    vals = {p: cout(N[p][0], N[p][1], MIS_PE, MIS_PS, EA, EC, sa=SA * mult, sc=SC * mult, k=K_RED) for p in PHASES}
    tt = sum(vals.values())
    t(f"    sorties × {fr(mult, 1)} ({ent(SA * mult)} et {ent(SC * mult)}) : {fr(vals['epreuve'])} + {fr(vals['decisif'])} + {fr(vals['revision'])} = {fr(tt)}")
    rows.append(f"| {ent(SA * mult)} et {ent(SC * mult)} | {fr(vals['epreuve'])} | {fr(vals['decisif'])} | {fr(vals['revision'])} | **{fr(tt)}** |")
put("T_L2_SENS", "\n".join(rows))
_lo = sum(cout(N[p][0], N[p][1], MIS_PE, MIS_PS, EA, EC, sa=SA / 2, sc=SC / 2, k=K_RED) for p in PHASES)
_hi = sum(cout(N[p][0], N[p][1], MIS_PE, MIS_PS, EA, EC, sa=SA * 4, sc=SC * 4, k=K_RED) for p in PHASES)
put("SENS_LO", fr(_lo, 0))
put("SENS_HI", fr(_hi, 0))
_part_sortie = sum((N[p][0] * SA + N[p][1] * SC) for p in PHASES) * MIS_PS / M / e2_avec
t(f"  part de la sortie dans le coût, aux suppositions : {fr(_part_sortie * 100, 1)} %")
put("PART_SORTIE", fr(_part_sortie * 100, 0))

# reserve d'un envoi : borne en octets (8 octets par jeton de sortie maximale, plus 64 jetons)
def reserve_mis(smax, octets, par_octets=True):
    sortie = (8 * smax + 64) if par_octets else smax
    return (octets * MIS_PE + sortie * MIS_PS) / M


rows = []
t("  réserve d'un envoi (entrée à un jeton par octet du corps, 24 000 octets au plus) :")
for smax in (8192, 16384, 32768):
    r_oct = reserve_mis(smax, BC)
    r_max = reserve_mis(smax, BC, par_octets=False)
    t(f"    sortie maximale {ent(smax)} : par la borne en octets ({ent(8 * smax)} octets, plus 64 jetons) {fr(r_oct, 3, 'sup')} ; par la sortie maximale seule {fr(r_max, 3, 'sup')}")
    rows.append(f"| {ent(smax)} | {ent(8 * smax)} | {fr(r_oct, 3, 'sup')} | {fr(r_max, 3, 'sup')} |")
put("T_L2_RES", "\n".join(rows))
RES_M = reserve_mis(32768, BC)  # la plus haute des reserves de Mistral
assert fr(RES_M, 3, "sup") == "0,625"
put("RES_M", fr(RES_M, 2, "sup"))

# majorant vrai, sans les gardes : trois envois par appel, sortie maximale pleine
def majorant(a, c, pe, ps, smax):
    return ENVOIS_MAX * (a * (BA * pe + smax * ps) + c * (BC * pe + smax * ps)) / M


rows = []
t("  majorant vrai sans les gardes (trois envois par appel, sortie maximale pleine, un jeton par octet) :")
for smax in (8192, 16384, 32768):
    v = {p: majorant(N[p][0], N[p][1], MIS_PE, MIS_PS, smax) for p in PHASES}
    t(f"    sortie maximale {ent(smax)} : {fr(v['epreuve'], 0)} + {fr(v['decisif'], 0)} + {fr(v['revision'], 0)} = {fr(sum(v.values()), 0)}")
    rows.append(f"| {ent(smax)} | {fr(v['epreuve'], 0)} | {fr(v['decisif'], 0)} | {fr(v['revision'], 0)} | {fr(sum(v.values()), 0)} |")
    put(f"L2_MAJ_{smax}", fr(sum(v.values()), 0))
put("T_L2_MAJ", "\n".join(rows))

# ---------------------------------------------------------------- 5. lecteur 1 (projection de 6.11)
C1 = F(1464, 10)
t()
t("== 5. Premier lecteur : projection de 6.11, 146,4 USD pour 13 888 lectures d'appariement et 1 248 de couverture")
t(f"  coût moyen par appel : 146,4 / 15 136 = {fr(C1 / 15136, 5)} USD")
put("C1_MOYEN", fr(C1 / 15136 * 1000, 2))
parts = {}
for rho in (F(1), F(2), F(4)):
    x = C1 / (13888 + 1248 * rho)
    parts[rho] = {p: x * (N[p][0] + rho * N[p][1]) for p in PHASES}
    tt = sum(parts[rho].values())
    assert tt == C1
    t(f"  rapport de coût couverture / appariement = {fr(rho, 0)} : appariement {fr(x, 5)} par appel ; "
      + " ; ".join(f"{NOM_PHASE[p]} {fr(parts[rho][p])} ({fr(parts[rho][p] / C1 * 100, 2)} %)" for p in PHASES))
L1 = {}
for p in PHASES:
    lo = min(parts[r][p] for r in (F(1), F(4)))
    hi = max(parts[r][p] for r in (F(1), F(4)))
    L1[p] = (lo, hi)
    put(f"L1_LO_{p.upper()}", fr(lo))
    put(f"L1_HI_{p.upper()}", fr(hi))
    put(f"L1_PLO_{p.upper()}", fr(lo / C1 * 100, 1))
    put(f"L1_PHI_{p.upper()}", fr(hi / C1 * 100, 1))
l1_sans_lo = C1 - L1["revision"][1]
l1_sans_hi = C1 - L1["revision"][0]
t(f"  sans révision : {fr(l1_sans_lo)} à {fr(l1_sans_hi)}")
put("L1_SANS_LO", fr(l1_sans_lo, 0))
put("L1_SANS_HI", fr(l1_sans_hi, 0))

# ---------------------------------------------------------------- 6. juge des ancres (Neon)
t()
t("== 6. Juge des deux ancres, gemini-4-neon (3 et 15 ; sorties supposées 2 000 et 4 000)")
ca_n = cout_appel(GA, SA, NEO_PE, NEO_PS)
cc_n = cout_appel(GC, SC, NEO_PE, NEO_PS)
t(f"  coût d'un appel, un envoi : appariement {fr(ca_n, 6)} ; couverture {fr(cc_n, 6)}")
j80 = 72 * ca_n + 8 * cc_n
j72 = 72 * ca_n
j80c = 80 * cc_n
j72c = 72 * cc_n
t(f"  80 appels, répartition inférée 72 et 8 : {fr(j80)} ; avec redemandes {fr(j80 * K_RED)}")
t(f"  72 appels de la révision, appariement : {fr(j72)} ; avec redemandes {fr(j72 * K_RED)}")
t(f"  tous comptés comme des lectures de couverture : 80 appels {fr(j80c)} ; avec redemandes {fr(j80c * K_RED)} ; 72 appels {fr(j72c)} ; avec redemandes {fr(j72c * K_RED)}")
put("J_E1_80", fr(j80))
put("J_EK_80", fr(j80 * K_RED))
put("J_E1_72", fr(j72))
put("J_EK_72", fr(j72 * K_RED))
put("J_EK_80C", fr(j80c * K_RED))
put("J_EK_72C", fr(j72c * K_RED))
put("J_EK_152", fr((j80 + j72) * K_RED))
put("J_EK_152C", fr((j80c + j72c) * K_RED))


def reserve_neo(smax, octets=BC):
    return (octets * NEO_PE + smax * NEO_PS) / M


rows = []
for smax in (32768, 65536):
    r = reserve_neo(smax)
    maj80 = ENVOIS_MAX * 80 * r
    maj152 = ENVOIS_MAX * 152 * r
    t(f"  sortie maximale {ent(smax)} : part de texte au plus {ent(16000)}, provision de réflexion {ent(smax - 16000)} ; réserve d'un envoi {fr(r, 3, 'sup')} ; majorant vrai, trois envois pleins : 80 appels {fr(maj80, 0)} ; 152 appels {fr(maj152, 0)}")
    rows.append(f"| {ent(smax)} | {ent(smax - 16000)} | {fr(r, 3, 'sup')} | {fr(maj80, 0)} | {fr(maj152, 0)} |")
    put(f"J_RES_{smax}", fr(r, 2, "sup"))
    put(f"J_MAJ152_{smax}", fr(maj152, 0))
put("T_J_RES", "\n".join(rows))
RES_N = reserve_neo(65536)

# ---------------------------------------------------------------- 7. envoi coupe (debit declare de 200 jetons par seconde)
t()
t("== 7. Envoi coupé, compté au débit déclaré de 200 jetons par seconde (S)")
DEBIT = 200
COUPE = {}
rows = []
for delai in (890, 2690):
    jet = delai * DEBIT
    cm = jet * MIS_PS / M
    cn = jet * NEO_PS / M
    COUPE[delai] = (cm, cn)
    t(f"  délai du relais {ent(delai)} s : {ent(jet)} jetons ; Mistral {fr(cm, 2)} ; Google {fr(cn, 2)}")
    rows.append(f"| {ent(delai)} | {ent(jet)} | {fr(cm, 2)} | {fr(cn, 2)} |")
put("T_COUPE", "\n".join(rows))
assert fr(COUPE[2690][1], 2) == "8,07" and fr(COUPE[890][1], 2) == "2,67"  # chiffres du devis des essais d'admission
assert fr(COUPE[2690][0], 2) == "1,24"
CM, CN = COUPE[2690]
put("CM_2690", fr(CM, 2))
put("CN_2690", fr(CN, 2))
put("CM_890", fr(COUPE[890][0], 2))
put("CN_890", fr(COUPE[890][1], 2))
# cas ouvert du regime courant, s'il etait garde a la course : un envoi coupe par appel, et un de plus
ouvert_juge = (80 + 1) * CN
t(f"  cas ouvert du régime courant pour le juge, s'il était gardé à la course : (80 + 1) envois coupés × {fr(CN, 2)} = {fr(ouvert_juge, 2)} USD (aux essais : neuf, 76,70 plafond compris)")
put("OUVERT_JUGE", fr(ouvert_juge, 0))

# ---------------------------------------------------------------- 8. plafonds
t()
t("== 8. Plafonds (arrondis aux 5 USD supérieurs ; marge × projection + réserve d'un envoi)")
M_SUPPOSE, M_SYNTH, M_REEL = 3, 2, F(3, 2)
PL2 = {}
for p in PHASES:
    brut = M_SUPPOSE * E2K[p] + RES_M
    PL2[p] = sup5(brut)
    t(f"  second lecteur, {NOM_PHASE[p]} : 3 × {fr(E2K[p])} + {fr(RES_M, 2, 'sup')} = {fr(brut)} → {PL2[p]}")
    put(f"PL2_{p.upper()}", str(PL2[p]))
# apres admission, exemple a la supposition : marge 2
PL2S = {}
for p in PHASES:
    brut = M_SYNTH * E2K[p] + RES_M
    PL2S[p] = sup5(brut)
    t(f"    second lecteur, {NOM_PHASE[p]}, à la marge de 2, si les compteurs d'admission rendaient la supposition : {fr(brut)} → {PL2S[p]}")
    put(f"PL2S_{p.upper()}", str(PL2S[p]))
# exemple du plafond recalcule sur textes reels, a la supposition
PL2R = {}
for p in ("decisif", "revision"):
    brut = M_REEL * E2K[p] + RES_M
    PL2R[p] = sup5(brut)
    t(f"    second lecteur, {NOM_PHASE[p]}, plafond recalculé à 1,5, si les lots d'épreuve rendaient la supposition : {fr(brut)} → {PL2R[p]}")
    put(f"PL2R_{p.upper()}", str(PL2R[p]))
RES_1 = F(1)  # reserve d'un envoi du premier lecteur : inconnue ici, prise a 1 USD (S)
PL1 = {}
for p in PHASES:
    brut = M_SYNTH * L1[p][1] + RES_1
    PL1[p] = sup5(brut)
    t(f"  premier lecteur, {NOM_PHASE[p]} : 2 × {fr(L1[p][1])} + 1,00 = {fr(brut)} → {PL1[p]}")
    put(f"PL1_{p.upper()}", str(PL1[p]))
PLJ = {}
for nom, v in (("80", j80c * K_RED), ("72", j72c * K_RED)):
    brut = M_SUPPOSE * v + RES_N
    PLJ[nom] = sup5(brut)
    t(f"  juge, {nom} appels comptés comme des lectures de couverture : 3 × {fr(v)} + {fr(RES_N, 2, 'sup')} = {fr(brut)} → {PLJ[nom]}")
    put(f"PLJ_{nom}", str(PLJ[nom]))
# ce que le plafond de repli du juge tolere en sortie moyenne (un envoi par appel, entree de couverture)
tol = ((F(PLJ["80"]) - RES_N) / 80 - GC * NEO_PE / M) * M / NEO_PS
t(f"  le plafond de {PLJ['80']} USD du juge tient jusqu'à une sortie moyenne de {ent(math.floor(tol))} jetons par appel (un envoi par appel, entrée de couverture)")
put("J_TOL", ent(math.floor(tol / 100) * 100))
# idem second lecteur, lots d'epreuve
a, c = N["epreuve"]
num = (F(PL2["epreuve"]) - RES_M) / K_RED * M - (a * EA + c * EC) * MIS_PE
tol2 = num / ((a * SA + c * SC) * MIS_PS)
t(f"  le plafond de {PL2['epreuve']} USD des lots d'épreuve du second lecteur tient jusqu'à des sorties moyennes de {fr(tol2, 2)} fois la supposition (avec redemandes)")
put("L2_TOL", fr(tol2, 1, "inf"))

tot_pl1 = sum(PL1.values())
tot_pl2 = sum(PL2.values())
tot_plj = sum(PLJ.values())
t(f"  somme des plafonds : premier lecteur {tot_pl1} ({PL1['epreuve'] + PL1['decisif']} sans la révision) ; second lecteur {tot_pl2} ({PL2['epreuve'] + PL2['decisif']}) ; juge {tot_plj} ({PLJ['80']})")
tot_pl = tot_pl1 + tot_pl2 + tot_plj
tot_pl_sans = PL1["epreuve"] + PL1["decisif"] + PL2["epreuve"] + PL2["decisif"] + PLJ["80"]
tot_pl_epr = PL1["epreuve"] + PL2["epreuve"] + PLJ["80"]
t(f"  somme des plafonds du côté de la relance : {tot_pl} ; sans les trois lignes de la révision : {tot_pl_sans} ; premières lignes seules (épreuves et ancres) : {tot_pl_epr}")
put("TOT_PL1", str(tot_pl1))
put("TOT_PL2", str(tot_pl2))
put("TOT_PLJ", str(tot_plj))
put("TOT_PL", str(tot_pl))
put("TOT_PL_SANS", str(tot_pl_sans))
put("TOT_PL_EPR", str(tot_pl_epr))
put("TOT_PL1_SANS", str(PL1["epreuve"] + PL1["decisif"]))
put("TOT_PL2_SANS", str(PL2["epreuve"] + PL2["decisif"]))

# attendu d'ensemble
att_avec = C1 + e2k_avec + (j80 + j72) * K_RED
att_sans_lo = l1_sans_lo + e2k_sans + j80 * K_RED
att_sans_hi = l1_sans_hi + e2k_sans + j80 * K_RED
att_epr_lo = L1["epreuve"][0] + E2K["epreuve"] + j80 * K_RED
att_epr_hi = L1["epreuve"][1] + E2K["epreuve"] + j80 * K_RED
t(f"  attendu du côté de la relance : avec révision {fr(att_avec)} ; sans révision {fr(att_sans_lo)} à {fr(att_sans_hi)} ; premières lignes seules {fr(att_epr_lo)} à {fr(att_epr_hi)}")
put("ATT_AVEC", fr(att_avec, 0))
put("ATT_SANS_LO", fr(att_sans_lo, 0))
put("ATT_SANS_HI", fr(att_sans_hi, 0))
put("ATT_EPR_LO", fr(att_epr_lo, 0))
put("ATT_EPR_HI", fr(att_epr_hi, 0))

# pire cas tenu par les gardes : le plafond et un envoi coupe
t("  pire cas tenu par les gardes (plafond et un envoi coupé au délai de 2 690 s) :")
for p in PHASES:
    v = PL2[p] + CM
    t(f"    second lecteur, {NOM_PHASE[p]} : {PL2[p]} + {fr(CM, 2)} = {fr(v, 2)}")
    put(f"PIRE2_{p.upper()}", fr(v, 2))
for nom in ("80", "72"):
    v = PLJ[nom] + CN
    v2 = PLJ[nom] + COUPE[890][1]
    t(f"    juge, {nom} appels : {PLJ[nom]} + {fr(CN, 2)} = {fr(v, 2)} ; au délai de 890 s : {fr(v2, 2)}")
    put(f"PIREJ_{nom}", fr(v, 2))
    put(f"PIREJ890_{nom}", fr(v2, 2))

# ---------------------------------------------------------------- 9. credit
t()
t("== 9. Crédit utilisable à avoir (plafond et un envoi coupé, marge de 15 %, demi-dollar supérieur ; taxe de 20 % supposée)")
MARGE = F(115, 100)
TAXE = F(120, 100)


def credit(plafond, coupe):
    base = plafond + coupe
    cr = sup_demi(base * MARGE)
    return base, cr, cr * TAXE


rows = []
cum = F(0)
for p in PHASES:
    base, cr, tx = credit(PL2[p], CM)
    cum += base
    t(f"  Mistral, {NOM_PHASE[p]} : à couvrir {fr(base, 2)} ; crédit {fr(cr)} ; avec taxe {fr(tx)}")
    rows.append(f"| Mistral | second lecteur, {NOM_PHASE[p]} | {PL2[p]} | {fr(CM, 2)} | {fr(base, 2)} | **{fr(cr)}** | {fr(tx)} |")
cr_tout = sup_demi(cum * MARGE)
t(f"  Mistral, les trois lignes en une fois : à couvrir {fr(cum, 2)} ; crédit {fr(cr_tout)} ; avec taxe {fr(cr_tout * TAXE)}")
rows.append(f"| Mistral | les trois lignes, en une fois | {tot_pl2} | {fr(3 * CM, 2)} | {fr(cum, 2)} | **{fr(cr_tout)}** | {fr(cr_tout * TAXE)} |")
for nom, lib in (("80", "juge, 80 appels"), ("72", "juge, 72 appels de la révision")):
    base, cr, tx = credit(PLJ[nom], CN)
    t(f"  Google, {lib} : à couvrir {fr(base)} sur chaque projet ; crédit {fr(cr)} ; avec taxe {fr(tx)}")
    rows.append(f"| Google, sur chaque projet | {lib} | {PLJ[nom]} | {fr(CN, 2)} | {fr(base)} | **{fr(cr)}** | {fr(tx)} |")
    put(f"SEUIL_J_{nom}", fr(base))
put("T_CREDIT", "\n".join(rows))
# seuil du juge en euros vus, a trois taux d'exemple (taux diminue de 5 %)
seuil = PLJ["80"] + CN
ex = []
for taux in (F(100, 100), F(110, 100), F(120, 100)):
    eur = seuil / (taux * F(95, 100))
    eur = _arr(eur, 2, "sup")
    ex.append(f"{fr(eur)} € à {fr(taux)} USD par euro")
t(f"  seuil du juge, {fr(seuil)} USD comptés, en euros vus (taux diminué de 5 %), exemples : " + " ; ".join(ex))
put("SEUIL_J_EUR", " ; ".join(ex))

# ---------------------------------------------------------------- 10. duree
t()
t("== 10. Durée (S : durée d'un appel non mesurée)")
rows = []
for d in (30, 60):
    seq = tot_avec * (d + 10)
    par8 = F(tot_avec * d, 8)
    seq_e = sum(N["epreuve"]) * (d + 10)
    par8_e = F(sum(N["epreuve"]) * d, 8)
    t(f"  {d} s par appel : un appel à la fois avec dix secondes de pause, {fr(F(seq, 3600), 0)} h par lecteur ({fr(F(seq, 86400), 1)} jours), dont {fr(F(seq_e, 3600), 1)} h pour les lots d'épreuve ; huit appels en parallèle sans pause, {fr(par8 / 3600, 1)} h, dont {fr(par8_e / 3600, 1)} h")
    rows.append(f"| {d} s | {fr(F(seq, 3600), 0)} h, soit {fr(F(seq, 86400), 1)} jours | {fr(F(seq_e, 3600), 1)} h | {fr(par8 / 3600, 1)} h | {fr(par8_e / 3600, 1)} h |")
put("T_DUREE", "\n".join(rows))
req_min = F(60 * 8, 30)
tpm_a = req_min * (EA + SA)
tpm_c = req_min * (EC + SC)
t(f"  huit appels en parallèle de 30 s : {fr(req_min, 0)} requêtes par minute ; {ent(round(tpm_a))} jetons par minute à l'appariement ; {ent(round(tpm_c))} à la couverture")
put("REQ_MIN", fr(req_min, 0))
put("TPM_A", ent(math.ceil(tpm_a / 1000) * 1000))
put("TPM_C", ent(math.ceil(tpm_c / 1000) * 1000))

# ---------------------------------------------------------------- 11. moniteurs (cote habilite)
t()
t("== 11. Moniteurs à modèle de langue : formule, tarif en case")
coef_e = F(6400 * LECT_MON, M)
coef_c = F(6400, M)
coef_s = F(6400 * 1000, M)
t(f"  6 400 lectures : part d'entrée = {fr(coef_e, 2)} × pe + {fr(coef_c, 4)} × c × pe ; part de sortie = {fr(coef_s, 1)} × ps par millier de jetons de sortie")
put("MON_COEF_E", fr(coef_e, 2))
put("MON_COEF_C", fr(coef_c, 4))
put("MON_COEF_S", fr(coef_s, 1))
seuil_s = F(LECT_MON, 5)
t(f"  la sortie coûte autant que l'entrée dès {fr(seuil_s, 0)} jetons de sortie par lecture, si le prix de sortie vaut cinq fois le prix d'entrée (consigne non comptée)")
put("MON_SEUIL_S", fr(seuil_s, 0))
rows = []
for pe, ps in ((1, 5), (3, 15)):
    for s in (500, 2000):
        v = 6400 * (LECT_MON * F(pe) + s * F(ps)) / M
        t(f"  exemple, non un tarif : {pe} et {ps} USD par million, {ent(s)} jetons de sortie par lecture : {fr(v, 0)} USD par moniteur, un envoi par appel, consigne non comptée")
        rows.append(f"| {pe} et {ps} | {ent(s)} | {fr(6400 * LECT_MON * F(pe) / M, 0)} | {fr(6400 * s * F(ps) / M, 0)} | {fr(v, 0)} |")
put("T_MON_EX", "\n".join(rows))
t(f"  devis v2, section 6 : 6 400 × 2 866 = {ent(tok_mon)} jetons d'entrée (« ≈ 18 millions ») ; à 1 USD par million {fr(F(tok_mon, M), 2)}")

# ---------------------------------------------------------------- 12. tableaux d'ensemble
t()
t("== 12. Tableaux d'ensemble")
rows = []
for nom, k, i, p, f_ in LOTS:
    if p != "epreuve":
        continue
    a, c = (k, 0) if i == "a" else (0, k)
    jt = jetons_entree(a, c)
    v = cout(a, c, MIS_PE, MIS_PS, EA, EC, k=K_RED)
    t(f"  lot d'épreuve « {nom} » : {ent(k)} appels par lecteur ; {ent(round(jt))} jetons d'entrée par lecteur ; second lecteur {fr(v)} USD avec redemandes")
    rows.append(f"| {nom} | {'appariement' if i == 'a' else 'couverture'} | {ent(k)} | {ent(2 * k)} | {fr(jt / M, 2)} | {fr(v)} |")
a, c = N["epreuve"]
rows.append(f"| **les cinq lots** | | **{ent(a + c)}** | **{ent(2 * (a + c))}** | **{fr(tok['epreuve'] / M, 2)}** | **{fr(E2K['epreuve'])}** |")
put("T_EPR", "\n".join(rows))

LIGNES = [
    (1, "premier lecteur, lots d'épreuve", sum(N["epreuve"]), f"{fr(L1['epreuve'][0])} à {fr(L1['epreuve'][1])}", f"{PL1['epreuve']}", "le plafond et un envoi coupé [case]"),
    (2, "premier lecteur, lots décisifs", sum(N["decisif"]), f"{fr(L1['decisif'][0])} à {fr(L1['decisif'][1])}", f"{PL1['decisif']}, recalculé", "de même"),
    (3, "premier lecteur, lots de la révision (conditionnelle)", sum(N["revision"]), f"{fr(L1['revision'][0])} à {fr(L1['revision'][1])}", f"{PL1['revision']}, recalculé", "de même"),
    (4, "second lecteur, lots d'épreuve", sum(N["epreuve"]), f"{fr(E2K['epreuve'])} (S)", f"{PL2['epreuve']}", fr(PL2["epreuve"] + CM)),
    (5, "second lecteur, lots décisifs", sum(N["decisif"]), f"{fr(E2K['decisif'])} (S)", f"{PL2['decisif']}, recalculé", fr(PL2["decisif"] + CM)),
    (6, "second lecteur, lots de la révision (conditionnelle)", sum(N["revision"]), f"{fr(E2K['revision'])} (S)", f"{PL2['revision']}, recalculé", fr(PL2["revision"] + CM)),
    (7, "juge des deux ancres", 80, f"{fr(j80 * K_RED)} (S)", f"{PLJ['80']}", fr(PLJ["80"] + CN)),
    (8, "juge, ancres de la révision (conditionnelle)", 72, f"{fr(j72 * K_RED)} (S)", f"{PLJ['72']}", fr(PLJ["72"] + CN)),
]
rows = []
tot_app = 0
for n_, nom, app, att, pl, pire in LIGNES:
    tot_app += app
    rows.append(f"| {n_} | {nom} | {ent(app)} | {ent(3 * app)} | {att} | {pl} | {pire} |")
    t(f"  ligne {n_}, {nom} : {ent(app)} appels ; {ent(3 * app)} envois au plus ; attendu {att} ; plafond {pl} ; pire cas tenu par les gardes {pire}")
assert tot_app == 2 * tot_avec + 152 == 30424 and 3 * tot_app == 91272
rows.append(f"| | **total du côté de la relance** | **{ent(tot_app)}** | **{ent(3 * tot_app)}** | **≈ {fr(att_avec, 0)}** | **{tot_pl}** | |")
t(f"  total : {ent(tot_app)} appels ; {ent(3 * tot_app)} envois au plus ; attendu ≈ {fr(att_avec, 0)} ; plafonds {tot_pl}")
put("T_RESUME", "\n".join(rows))
put("TOT_APPELS", ent(tot_app))
# exposition chez Google sous le regime prudent : essais (23,44, avenant 1) et lignes du juge a la course
expo_course = (PLJ["80"] + CN) + (PLJ["72"] + CN)
t(f"  Google, régime prudent : deux lignes du juge à la course {fr(expo_course)} ; avec les lignes des essais d'admission (23,44, avenant 1) : {fr(expo_course + F(2344, 100))}")
put("EXPO_J", fr(expo_course))
put("EXPO_J_ESSAIS", fr(expo_course + F(2344, 100)))
# part de la carte
t(f"  rapport à la carte : attendu des lectures du côté de la relance {fr(att_avec, 0)} USD, contre 20 à 25 USD attendus pour les deux lignes de carte du devis v2 : {fr(att_avec / 25, 0)} à {fr(att_avec / 20, 0)} fois")
put("RAPPORT_CARTE_LO", fr(att_avec / 25, 0))
put("RAPPORT_CARTE_HI", fr(att_avec / 20, 0))

# tableaux par lecteur
MAJ2 = {smax: {p: majorant(N[p][0], N[p][1], MIS_PE, MIS_PS, smax) for p in PHASES} for smax in (8192, 32768)}
cols = PHASES
def ligne(titre, f, total):
    return "| " + titre + " | " + " | ".join(f(p) for p in cols) + " | " + total + " |"
rows = [
    ligne("appels (M)", lambda p: ent(sum(N[p])), ent(tot_avec)),
    ligne("envois au plus (M : trois par appel)", lambda p: ent(3 * sum(N[p])), ent(3 * tot_avec)),
    ligne("jetons d'entrée, en millions (C ; compte de Claude, faute de mesure du découpage de Mistral)", lambda p: fr(tok[p] / M, 2), fr(tok_lecteur_avec / M, 1)),
    ligne("jetons de sortie supposés, réflexion comprise, en millions (S)", lambda p: fr(F(N[p][0] * SA + N[p][1] * SC, M), 2), fr(F(sor2_tot, M), 2)),
    ligne("attendu, un envoi par appel (C sur S)", lambda p: fr(E2[p]), fr(e2_avec)),
    ligne("**attendu, avec redemandes** (C sur S)", lambda p: "**" + fr(E2K[p]) + "**", "**" + fr(e2k_avec) + "**"),
    ligne("**plafond de ce brouillon, un maximum** (C ; section 5)", lambda p: "**" + str(PL2[p]) + "**", "**" + str(tot_pl2) + "**"),
    ligne("pire cas tenu par les gardes : le plafond et un envoi coupé (C)", lambda p: fr(PL2[p] + CM), "—"),
    ligne("majorant vrai sans les gardes, sortie maximale de 8 192 à 32 768 (C)", lambda p: fr(MAJ2[8192][p], 0) + " à " + fr(MAJ2[32768][p], 0), fr(sum(MAJ2[8192].values()), 0) + " à " + fr(sum(MAJ2[32768].values()), 0)),
]
put("T_L2", "\n".join(rows))
rows = [
    ligne("appels (M)", lambda p: ent(sum(N[p])), ent(tot_avec)),
    ligne("envois au plus (M : trois par appel)", lambda p: ent(3 * sum(N[p])), ent(3 * tot_avec)),
    ligne("jetons d'entrée, en millions (C sur M ; compte de Claude)", lambda p: fr(tok[p] / M, 2), fr(tok_lecteur_avec / M, 1)),
    ligne("part de la projection (C sur S)", lambda p: fr(L1[p][0] / C1 * 100, 1) + " à " + fr(L1[p][1] / C1 * 100, 1) + " %", "100 %"),
    ligne("**attendu** (M réparti ; C sur S)", lambda p: "**" + fr(L1[p][0]) + " à " + fr(L1[p][1]) + "**", "**≈ 146,4**"),
    ligne("**plafond de ce brouillon, un maximum** (C ; section 5)", lambda p: "**" + str(PL1[p]) + "**", "**" + str(tot_pl1) + "**"),
]
put("T_L1", "\n".join(rows))
put("L2_EK_AVEC_0", fr(e2k_avec, 0))
put("L2_EK_SANS_0", fr(e2k_sans, 0))
put("J_EK_152_0", fr((j80 + j72) * K_RED, 0))
put("J_EK_80_0", fr(j80 * K_RED, 0))
put("K_RED", fr(K_RED, 4))
put("ENVOIS_LECTEUR", ent(3 * tot_avec))
put("PL_L2_SUPP2", f"{PL2S['epreuve']}, {PL2S['decisif']} et {PL2S['revision']}")
put("TOT_PL_REV", str(PL1["revision"] + PL2["revision"] + PLJ["72"]))
put("RES_N", fr(RES_N, 2, "sup"))
t(f"  somme des trois plafonds de la révision : {PL1['revision'] + PL2['revision'] + PLJ['72']}")

# valeurs citees dans la prose
put("MON_102", ent(6400 * 102))
put("PAR8_CM", fr(8 * CM))
t(f"  huit appels en vol chez Mistral, tous coupés au délai de 2 690 s : 8 × {fr(CM)} = {fr(8 * CM)} USD au-delà du plafond, au plus")
put("COEF_COUPE", fr(F(2690 * DEBIT, M), 3))
put("ENVOIS_EPR_2L", ent(2 * 3 * sum(N["epreuve"])))
put("CREDIT_M_EPR", fr(sup_demi((PL2["epreuve"] + CM) * MARGE)))
put("DUREE_J_LO", fr(F(tot_avec * (30 + 10), 86400), 0))
put("DUREE_J_HI", fr(F(tot_avec * (60 + 10), 86400), 0))
put("DUREE_PAR_HI", fr(F(tot_avec * 60, 8 * 3600), 0))
t(f"  trois envois coupés du juge au délai de 2 690 s : {fr(3 * CN)} USD, pour un plafond de {PLJ['80']} ; le quatrième envoi est refusé ({fr(3 * CN)} + {fr(RES_N, 2, 'sup')} passe {PLJ['80']})")
assert 2 * CN + RES_N <= PLJ["80"] < 3 * CN + RES_N

# par objet du mandat : epreuves et ancres ; lots decisifs de l'oracle ; revision
def fourchette(lo, hi):
    a, b = fr(lo, 0), fr(hi, 0)
    return a if a == b else a + " à " + b
obj = [
    ("les cinq lots d'épreuve, et les ancres", f"{ent(2 * sum(N['epreuve']))} et 80",
     L1["epreuve"][0] + E2K["epreuve"] + j80 * K_RED, L1["epreuve"][1] + E2K["epreuve"] + j80 * K_RED,
     PL1["epreuve"] + PL2["epreuve"] + PLJ["80"], "1, 4 et 7"),
    ("les lots décisifs de l'oracle", f"{ent(2 * sum(N['decisif']))}",
     L1["decisif"][0] + E2K["decisif"], L1["decisif"][1] + E2K["decisif"],
     PL1["decisif"] + PL2["decisif"], "2 et 5"),
    ("la révision, si elle est ouverte", f"{ent(2 * sum(N['revision']))} et 72",
     L1["revision"][0] + E2K["revision"] + j72 * K_RED, L1["revision"][1] + E2K["revision"] + j72 * K_RED,
     PL1["revision"] + PL2["revision"] + PLJ["72"], "3, 6 et 8"),
]
rows = []
for nom, lect, lo, hi, pl, lg in obj:
    rows.append(f"| {nom} | {lect} | ≈ {fourchette(lo, hi)} | {pl} | {lg} |")
    t(f"  par objet, {nom} : lectures {lect} ; attendu {fr(lo)} à {fr(hi)} ; plafonds {pl} ; lignes {lg}")
assert sum(o[4] for o in obj) == tot_pl
put("T_OBJET", "\n".join(rows))
put("ATT_DEC", fourchette(obj[1][2], obj[1][3]))
put("PL_DEC", str(obj[1][4]))

# ---------------------------------------------------------------- sortie
if __name__ == "__main__":
    if "--json" in sys.argv:
        json.dump({"valeurs": OUT, "trace": TRACE}, sys.stdout, ensure_ascii=False, indent=1)
    else:
        print("\n".join(TRACE))
