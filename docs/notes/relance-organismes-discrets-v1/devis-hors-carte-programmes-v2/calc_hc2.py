#!/usr/bin/env python3
# calc_hc2.py -- chiffres du devis des lectures hors carte du bras A, brouillon 2.
# Repris de calc_hc1.py (388ec1d9...), qui reste inchange. Ce qui est neuf ou change
# depuis le brouillon 1 est marque « brouillon 2 » : verification du brouillon 1
# (b0f04bd5...) et avenant 2 au devis des essais d'admission (5f84642a...).
# Arithmetique exacte (fractions). Aucune lecture de fichier, aucun reseau.
# Entrees : volumes de la section 6.11 du texte (brouillon 43), longueurs de la
# section 6.2 du devis des essais d'admission, tarifs des pages de prix versees,
# et, au brouillon 2, les chiffres de l'avenant 2 nommes en section 14.
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
t(f"  juge, 72 appels d'appariement et 8 de couverture (réponse de la session du bras A, par inférence de 6.11) : {ent(round(tok_juge_80))} ; avec la révision (144 et 8) : {ent(round(tok_juge_152))}")
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
t(f"  80 appels, 72 d'appariement et 8 de couverture : {fr(j80)} ; avec redemandes {fr(j80 * K_RED)}")
j80_alt = 48 * ca_n + 32 * cc_n  # brouillon 2 : si 24 des 72 etaient de couverture (verification, point 5)
t(f"  brouillon 2 : si 24 des 72 étaient de couverture (48 d'appariement, 32 de couverture) : avec redemandes {fr(j80_alt * K_RED)}")
put("J_EK_80_ALT", fr(j80_alt * K_RED))
t(f"  brouillon 2 : envois au plus du juge, trois par appel : 3 × 80 = {ent(3 * 80)} ; 3 × 72 = {ent(3 * 72)} ; 3 × 152 = {ent(3 * 152)}")
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


# brouillon 2 : l'essai du juge se joue a 65 536 sous une borne de reflexion declaree de 49 536 (avenant 2)
TEXTE_MIN = 16000      # regle permanente des appels a Google : 16 000 jetons de texte au moins
BORNE_DECL = 49536     # borne de reflexion declaree a l'essai (avenant 2, section 4), supposee
SMAX_ESSAI_J = 65536   # sortie maximale de l'essai du juge et de ses verifications de cle (avenant 2)
assert BORNE_DECL + TEXTE_MIN == SMAX_ESSAI_J
DELAI_RELAIS = 2690
t(f"  pour mémoire, sortie maximale 32 768 (valeur du devis des essais, remplacée chez Google par l'avenant 2) : réserve d'un envoi {fr(reserve_neo(32768), 3, 'sup')}")
rows = []
for smax in (65536, 81920, 262144):
    r = reserve_neo(smax)
    maj80 = ENVOIS_MAX * 80 * r
    maj152 = ENVOIS_MAX * 152 * r
    debit = F(smax, DELAI_RELAIS)
    t(f"  sortie maximale {ent(smax)} : texte au moins {ent(TEXTE_MIN)}, borne de réflexion déclarée au plus {ent(smax - TEXTE_MIN)} ; réserve d'un envoi {fr(r, 3, 'sup')} ; une sortie pleine finit en 2 690 s à {fr(debit, 1, 'sup')} jetons par seconde ou plus ; majorant vrai, trois envois pleins : 80 appels {fr(maj80, 0)} ; 152 appels {fr(maj152, 0)}")
    rows.append(f"| {ent(smax)} | {ent(smax - TEXTE_MIN)} | {fr(r, 3, 'sup')} | {fr(debit, 1, 'sup')} | {fr(maj80, 0)} | {fr(maj152, 0)} |")
    put(f"J_RES3_{smax}", fr(r, 3, "sup"))
    put(f"J_MAJ80_{smax}", fr(maj80, 0))
    put(f"J_MAJ152_{smax}", fr(maj152, 0))
put("T_J_RES", "\n".join(rows))
RES_N = reserve_neo(SMAX_ESSAI_J)
put("J_RES_ENTREE", fr(reserve_neo(0), 3))
assert fr(F(SMAX_ESSAI_J, DELAI_RELAIS), 1, "sup") == "24,4"  # le debit de l'avenant 2, section 5

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
t(f"  cas ouvert du régime courant pour le juge, s'il était gardé à la course : (80 + 1) envois coupés × {fr(CN, 2)} = {fr(ouvert_juge, 2)} USD (aux essais : neuf envois, et une borne de 80,29 plafond compris, selon l'avenant 2)")
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
# brouillon 2 : la marge se lit par instrument. Les lots d'epreuve comptent 2 176 lectures reelles
# d'appariement (1,5) et 320 de couverture, moins de 1 000 (la couverture reste a 2).
SEUIL_REEL = 1000
assert N["epreuve"][0] >= SEUIL_REEL > N["epreuve"][1] and N["epreuve"] == (2176, 320)
PL2R = {}
for p in ("decisif", "revision"):
    a, c = N[p]
    part_a = K_RED * a * ca_m
    part_c = K_RED * c * cc_m
    assert part_a + part_c == E2K[p]
    brut_uni = M_REEL * E2K[p] + RES_M
    brut = M_REEL * part_a + M_SYNTH * part_c + RES_M
    PL2R[p] = sup5(brut)
    t(f"    second lecteur, {NOM_PHASE[p]}, plafond recalculé si les lots d'épreuve rendaient la supposition : 1,5 × {fr(part_a)} (appariement) + 2 × {fr(part_c)} (couverture) + {fr(RES_M, 2, 'sup')} = {fr(brut)} → {PL2R[p]} (brouillon 1, à 1,5 partout : {fr(brut_uni)} → {sup5(brut_uni)})")
    put(f"PL2R_{p.upper()}", str(PL2R[p]))
assert (PL2R["decisif"], PL2R["revision"]) == (115, 25)
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
put("J_TOL", ent(math.floor(tol)))  # brouillon 2 : la valeur du programme, au jeton inferieur (verification, m-1)
assert math.floor(tol) == 14994
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
t("== 9. Crédit utilisable à avoir chez Mistral (plafond et un envoi coupé, marge de 15 %, demi-dollar supérieur ; taxe de 20 % supposée) ; chez Google, seuil compté par projet (les euros sont en section 14)")
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
put("T_CREDIT", "\n".join(rows))
# brouillon 2 : chez Google, la marge de 15 % du devis des essais ne s'applique plus ; les avenants
# lisent le seuil sur le solde de chaque projet, converti au taux diminue de 5 % (section 14).
for nom, lib in (("80", "juge, 80 appels"), ("72", "juge, 72 appels de la révision")):
    base = PLJ[nom] + CN
    t(f"  Google, {lib} : seuil par projet, plafond et un envoi coupé : {PLJ[nom]} + {fr(CN, 2)} = {fr(base)} USD comptés")
    put(f"SEUIL_J_{nom}", fr(base))

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
# brouillon 2 : aucun prix d'exemple (un prix rond peut etre le tarif d'un lecteur) ; tout est donne
# par USD de prix, et le seuil ou la sortie pese autant que l'entree, a trois rapports de prix.
seuils_s = []
for rap in (3, 4, 5):
    s_eq = F(LECT_MON, rap)
    seuils_s.append(f"{fr(s_eq, 0)} jetons de sortie par lecture si le prix de sortie vaut {rap} fois le prix d'entrée")
    put(f"MON_SEUIL_S{rap}", fr(s_eq, 0))
t("  la sortie coûte autant que l'entrée (consigne non comptée) dès : " + " ; ".join(seuils_s))
t(f"  par USD de prix d'entrée par million : {fr(coef_e, 2)} USD par moniteur, consigne non comptée")
rows = []
for s in (500, 2000, 8000):
    v = F(6400 * s, M)
    t(f"  par USD de prix de sortie par million, à {ent(s)} jetons de sortie par lecture : {fr(v, 2)} USD par moniteur, un envoi par appel")
    rows.append(f"| {ent(s)} | {fr(v, 2)} |")
put("T_MON_UNIT", "\n".join(rows))
# le juge d'une autre lignee : la longueur que le devis de course lui comptait (sa section 6)
assert 2560 * LECT_MON == 7336960 and fr(F(2560 * LECT_MON, M), 0) == "7"
t(f"  juge d'une autre lignée, au devis de course : 2 560 lectures, « ≈ 7 millions » de jetons d'entrée ; 2 560 × 2 866 = {ent(2560 * LECT_MON)} : la même longueur par lecture que le moniteur par action en contexte")
t(f"  si « 102 points de lecture par action » voulait dire 102 appels par action : 6 400 × 102 = {ent(6400 * 102)} lectures ; à 2 866 jetons d'entrée par lecture, {fr(F(6400 * 102 * LECT_MON, 1000 * M), 2)} milliard de jetons d'entrée")
put("MON_102_TOK", fr(F(6400 * 102 * LECT_MON, 1000 * M), 2))
# si un moniteur est un modele de Google : reserve de sortie d'un envoi, a la borne declaree de l'essai du juge
put("MON_RES_G", fr(F(BORNE_DECL + TEXTE_MIN, M), 3, "sup"))
t(f"  si un moniteur est un modèle de Google, à une borne de réflexion déclarée de {ent(BORNE_DECL)} : sortie maximale d'au moins {ent(BORNE_DECL + TEXTE_MIN)} jetons, soit une réserve de sortie de {fr(F(BORNE_DECL + TEXTE_MIN, M), 3, 'sup')} × ps USD par envoi")
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
t(f"  Google, régime prudent : deux lignes du juge à la course {fr(expo_course)} (avec les essais d'admission : section 14)")
put("EXPO_J", fr(expo_course))
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
    ligne("le même, à huit appels à la fois : le plafond et huit envois coupés (C)", lambda p: fr(PL2[p] + 8 * CM), "—"),  # brouillon 2
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

# ================================================================ brouillon 2 : sections neuves
# ---------------------------------------------------------------- 13. sortie maximale de la course et maxima
t()
t("== 13. Sortie maximale de la course, règle 7 du texte, et maxima des lignes (brouillon 2 ; vérification, C-3)")


def regle7(max_observe):
    """Regle 7 du texte : la plus grande de 8 192 et de quatre fois le maximum observe, arrondie aux 1 024 superieurs."""
    return int(math.ceil(F(max(8192, 4 * max_observe), 1024)) * 1024)


assert regle7(0) == 8192 and regle7(2048) == 8192 and regle7(2049) == 9216
SMAX_ESSAI_M = 32768   # sortie maximale de l'essai d'admission de Mistral (devis des essais, 5.1 ; inchangee par l'avenant 2)
R7_MAX_M = regle7(SMAX_ESSAI_M)
R7_MAX_J = regle7(SMAX_ESSAI_J)
assert (R7_MAX_M, R7_MAX_J) == (131072, 262144)
t(f"  règle 7, tant que la sortie maximale de l'essai borne la sortie observée : de {ent(regle7(0))} à {ent(R7_MAX_M)} chez Mistral (essai joué à {ent(SMAX_ESSAI_M)}) ; de {ent(regle7(0))} à {ent(R7_MAX_J)} chez le juge (essai joué à {ent(SMAX_ESSAI_J)}, avenant 2)")
put("R7_MIN", ent(regle7(0)))
put("R7_MAX_M", ent(R7_MAX_M))
put("R7_MAX_J", ent(R7_MAX_J))


def seuil_smax(base, plafond, reserve):
    """Plus grande sortie maximale, multiple de 1 024, ou base + reserve(S) tient sous le plafond (la reserve croit avec S)."""
    assert base + reserve(1024) <= plafond
    s = 1024
    while base + reserve(s + 1024) <= plafond:
        s += 1024
    assert sup5(base + reserve(s)) <= plafond < sup5(base + reserve(s + 1024))
    return s


def res_m_oct(s):
    return reserve_mis(s, BC)


SEUILS = {}
for n_, nom, base, plaf, res in (
    (4, "second lecteur, lots d'épreuve", M_SUPPOSE * E2K["epreuve"], PL2["epreuve"], res_m_oct),
    (5, "second lecteur, lots décisifs", M_SUPPOSE * E2K["decisif"], PL2["decisif"], res_m_oct),
    (6, "second lecteur, lots de la révision", M_SUPPOSE * E2K["revision"], PL2["revision"], res_m_oct),
    (7, "juge, 80 appels", M_SUPPOSE * j80c * K_RED, PLJ["80"], reserve_neo),
    (8, "juge, 72 appels de la révision", M_SUPPOSE * j72c * K_RED, PLJ["72"], reserve_neo),
):
    s = seuil_smax(base, plaf, res)
    SEUILS[n_] = s
    t(f"  ligne {n_}, {nom} : le maximum de {plaf} USD tient jusqu'à une sortie maximale de {ent(s)} jetons (3 × attendu {fr(base)} + réserve {fr(res(s), 3, 'sup')}) ; à {ent(s + 1024)}, la règle rend {fr(base + res(s + 1024), 3)} → {sup5(base + res(s + 1024))}")
    put(f"SMAX_L{n_}", ent(s))
assert SEUILS == {4: 71680, 5: 290816, 6: 278528, 7: 81920, 8: 206848}
OBS_M, OBS_J = SEUILS[4] // 4, SEUILS[7] // 4
assert regle7(OBS_M) == SEUILS[4] and regle7(OBS_M + 1) > SEUILS[4]
assert regle7(OBS_J) == SEUILS[7] and regle7(OBS_J + 1) > SEUILS[7]
t(f"  soit un maximum observé à l'essai d'admission d'au plus {ent(OBS_M)} jetons chez Mistral et {ent(OBS_J)} chez le juge (un jeton de plus : règle 7 à {ent(regle7(OBS_M + 1))} et {ent(regle7(OBS_J + 1))})")
put("OBS_M", ent(OBS_M))
put("OBS_J", ent(OBS_J))
pl4_r7 = sup5(M_SUPPOSE * E2K["epreuve"] + reserve_mis(R7_MAX_M, BC))
pl5_r7 = sup5(M_SUPPOSE * E2K["decisif"] + reserve_mis(R7_MAX_M, BC))
pl6_r7 = sup5(M_SUPPOSE * E2K["revision"] + reserve_mis(R7_MAX_M, BC))
pl7_r7 = sup5(M_SUPPOSE * j80c * K_RED + reserve_neo(R7_MAX_J))
pl8_r7 = sup5(M_SUPPOSE * j72c * K_RED + reserve_neo(R7_MAX_J))
t(f"  à la sortie maximale la plus haute de la règle 7 : Mistral, réserve {fr(reserve_mis(R7_MAX_M, BC), 3, 'sup')}, la règle rendrait {pl4_r7}, {pl5_r7} et {pl6_r7} aux lignes 4, 5 et 6 (maxima : {PL2['epreuve']}, {PL2['decisif']}, {PL2['revision']}) ; juge, réserve {fr(reserve_neo(R7_MAX_J), 3, 'sup')}, la règle rendrait {pl7_r7} et {pl8_r7} aux lignes 7 et 8 (maxima : {PLJ['80']}, {PLJ['72']})")
assert (pl4_r7, pl5_r7, pl6_r7, pl7_r7, pl8_r7) == (60, 220, 45, 25, 25)
res_m_seule_r7 = reserve_mis(R7_MAX_M, BC, par_octets=False)
pl4_r7_seule = sup5(M_SUPPOSE * E2K["epreuve"] + res_m_seule_r7)
assert pl4_r7_seule == PL2["epreuve"]
t(f"  si le compteur réservait par la sortie maximale seule, l'essai ayant établi qu'elle borne aussi la réflexion : à {ent(R7_MAX_M)}, réserve {fr(res_m_seule_r7, 3, 'sup')}, la règle rendrait {pl4_r7_seule} à la ligne 4")
put("RES_M_SEULE_R7", fr(res_m_seule_r7, 3, "sup"))
put("PL4_R7", str(pl4_r7))
put("PL7_R7", str(pl7_r7))
put("PL8_R7", str(pl8_r7))
rows = []
for smax in (8192, 16384, 32768, SEUILS[4], R7_MAX_M):
    r_oct = reserve_mis(smax, BC)
    r_max = reserve_mis(smax, BC, par_octets=False)
    t(f"  second lecteur, sortie maximale {ent(smax)} : borne de {ent(8 * smax)} octets ; réserve par la borne en octets {fr(r_oct, 3, 'sup')} ; par la sortie maximale seule {fr(r_max, 3, 'sup')}")
    rows.append(f"| {ent(smax)} | {ent(8 * smax)} | {fr(r_oct, 3, 'sup')} | {fr(r_max, 3, 'sup')} |")
put("T_L2_RES5", "\n".join(rows))
put("RES_M_SEUIL", fr(reserve_mis(SEUILS[4], BC), 3, "sup"))
# premier lecteur : la reserve d'un envoi que ses maxima tolerent (sa reserve est une case)
tol_r1 = {p: PL1[p] - M_SYNTH * L1[p][1] for p in PHASES}
t("  premier lecteur : ses maxima tiennent tant que la réserve d'un envoi reste sous " + " ; ".join(f"{fr(tol_r1[p], 2, 'inf')} USD ({NOM_PHASE[p]})" for p in PHASES))
put("RES1_MAX", fr(tol_r1["epreuve"], 2, "inf"))
# huit appels en vol (decision 3, option b) : le compteur retient huit reserves
VOL = 8
a, c = N["epreuve"]
mult1 = (PL2["epreuve"] - RES_M) / E2K["epreuve"]
t(f"  ligne 4, un appel à la fois, sortie maximale 32 768 : la ligne va au bout tant que le cumul compté reste sous {fr(PL2['epreuve'] - RES_M, 2, 'inf')} USD, soit {fr(mult1, 2, 'inf')} fois l'attendu")
put("MULT1_L4", fr(mult1, 2, "inf"))
for smax, cle in ((32768, "32768"), (SEUILS[4], "SEUIL")):
    r = reserve_mis(smax, BC)
    cum = PL2["epreuve"] - VOL * r
    mult = cum / E2K["epreuve"]
    num8 = (F(PL2["epreuve"]) - VOL * r) / K_RED * M - (a * EA + c * EC) * MIS_PE
    tol8 = num8 / ((a * SA + c * SC) * MIS_PS)
    t(f"  ligne 4, huit appels en vol, sortie maximale {ent(smax)} : huit réserves {fr(VOL * r, 2, 'sup')} ; la ligne va au bout tant que le cumul compté reste sous {fr(cum, 2, 'inf')} USD, soit {fr(mult, 2, 'inf')} fois l'attendu, ou des sorties moyennes de {fr(tol8, 2, 'inf')} fois la supposition")
    put(f"CUM8_{cle}", fr(cum, 2, "inf"))
    put(f"MULT8_{cle}", fr(mult, 2, "inf"))
    put(f"TOL8_{cle}", fr(tol8, 1, "inf"))
# si la regle comptait huit reserves au lieu d'une (reserve 15 du devis) : ce que deviendraient les maxima du second lecteur
pl_8res = {p: sup5(M_SUPPOSE * E2K[p] + VOL * RES_M) for p in PHASES}
t(f"  si la règle comptait huit réserves au lieu d'une, à 32 768 de sortie maximale : second lecteur {pl_8res['epreuve']}, {pl_8res['decisif']} et {pl_8res['revision']} USD (maxima : {PL2['epreuve']}, {PL2['decisif']}, {PL2['revision']})")
assert (pl_8res["epreuve"], pl_8res["decisif"], pl_8res["revision"]) == (60, 220, 45)
put("PL4_8RES", str(pl_8res["epreuve"]))
rows = []
cum8 = F(0)
for p in PHASES:
    v8 = PL2[p] + VOL * CM
    cr8 = sup_demi(v8 * MARGE)
    cum8 += v8
    t(f"  Mistral, {NOM_PHASE[p]}, huit appels en vol : pire cas tenu par les gardes {PL2[p]} + 8 × {fr(CM, 2)} = {fr(v8, 2)} ; crédit {fr(cr8)} ; avec taxe {fr(cr8 * TAXE)}")
    put(f"PIRE2V_{p.upper()}", fr(v8, 2))
    put(f"CREDIT_M8_{p.upper()}", fr(cr8))
    rows.append(f"| Mistral | second lecteur, {NOM_PHASE[p]} | {PL2[p]} | {fr(VOL * CM, 2)} | {fr(v8, 2)} | **{fr(cr8)}** | {fr(cr8 * TAXE)} |")
cr8_tout = sup_demi(cum8 * MARGE)
t(f"  Mistral, les trois lignes en une fois, huit appels en vol : à couvrir {fr(cum8, 2)} ; crédit {fr(cr8_tout)} ; avec taxe {fr(cr8_tout * TAXE)}")
rows.append(f"| Mistral | les trois lignes, en une fois | {tot_pl2} | {fr(3 * VOL * CM, 2)} | {fr(cum8, 2)} | **{fr(cr8_tout)}** | {fr(cr8_tout * TAXE)} |")
put("T_CREDIT8", "\n".join(rows))

# ---------------------------------------------------------------- 14. avenant 2 : recoupe, lignes du juge, euros
t()
t("== 14. Avenant 2 au devis des essais (sortie maximale de Google à 65 536) : recoupe, lignes du juge, seuils en euros (brouillon 2 ; vérification, C-1 et C-7)")
SORTIE_PLEINE_J = SMAX_ESSAI_J * NEO_PS / M
assert SORTIE_PLEINE_J == F(98304, 100000)


def c2sup(x):
    return _arr(x, 2, "sup")


EXC_FILE = COUPE[2690][1] - SORTIE_PLEINE_J     # exces d'un envoi de la file du juge, a l'essai
EXC_VERIF = COUPE[890][1] - SORTIE_PLEINE_J     # exces d'un envoi de verification de cle
PLAF_FILE, PLAF_VERIF = F(1650, 100), F(3)      # M : avenant 2, section 2 (plafonds de la file et d'une verification)
BORNE_VERIF = PLAF_VERIF + c2sup(EXC_VERIF)
BORNE_FILE = PLAF_FILE + c2sup(EXC_FILE)
NEUF_EXCES = c2sup(PLAF_FILE + 9 * EXC_FILE)
AV2_PRUDENT = 2 * BORNE_VERIF + BORNE_FILE
AV2_PIRE = 2 * BORNE_VERIF + NEUF_EXCES
assert (c2sup(EXC_FILE), c2sup(EXC_VERIF)) == (F(709, 100), F(169, 100))
assert (BORNE_VERIF, BORNE_FILE, NEUF_EXCES) == (F(469, 100), F(2359, 100), F(8029, 100))
assert (AV2_PRUDENT, AV2_PIRE) == (F(3297, 100), F(8967, 100))
ACCEPTE = F(8406, 100)   # M : GO-2026-11-21-68, « pire cas 84,06 USD sans borne dure (accepté) »
assert AV2_PIRE - ACCEPTE == F(561, 100)
t(f"  recoupe de l'avenant 2 sur ses entrées (plafonds 16,50 et 3,00 ; envoi coupé 8,07 et 2,67 ; sortie pleine {fr(SORTIE_PLEINE_J, 5)}) : excès {fr(EXC_FILE, 2, 'sup')} et {fr(EXC_VERIF, 2, 'sup')} ; plafond et excès {fr(BORNE_FILE)} et {fr(BORNE_VERIF)} ; file aux neuf excès {fr(NEUF_EXCES)} ; essais chez Google, régime prudent {fr(AV2_PRUDENT)} ; pire cas sans borne dure {fr(AV2_PIRE)} (avenant 2 : 32,97 et 89,67)")
t(f"  pire cas accepté par Lazar pour les essais (GO-2026-11-21-68) : {fr(ACCEPTE)} ; dépassé de {fr(AV2_PIRE - ACCEPTE)}")
put("AV2_PRUDENT", fr(AV2_PRUDENT))
put("AV2_PIRE", fr(AV2_PIRE))
put("ACCEPTE", fr(ACCEPTE))
put("AV2_DEPASSE", fr(AV2_PIRE - ACCEPTE))
put("AV2_NEUF", fr(NEUF_EXCES))
expo_prudent = expo_course + AV2_PRUDENT
expo_pire = expo_course + AV2_PIRE
t(f"  les deux lignes du juge à la course, au régime prudent : {fr(expo_course)} ; avec les essais au régime prudent : {fr(expo_prudent)} ; avec le pire cas des essais : {fr(expo_pire)}")
assert (expo_course, expo_prudent, expo_pire) == (F(5614, 100), F(8911, 100), F(14581, 100))
put("EXPO_PRUDENT", fr(expo_prudent))
put("EXPO_PIRE", fr(expo_pire))
# le pire cas d'une ligne du juge, compte comme l'avenant 2 (le plafond, et l'exces sur la reserve seulement)
pire_exces = PLJ["80"] + CN - RES_N
t(f"  ligne du juge, comptée comme l'avenant 2 (plafond, et excès de l'envoi coupé sur sa réserve) : {PLJ['80']} + {fr(CN)} − {fr(RES_N, 5)} = {fr(pire_exces, 2, 'sup')} ; ce devis garde {fr(PLJ['80'] + CN)}, plus prudent")
put("PIREJ_EXCES", fr(pire_exces, 2, "sup"))
# la regle 7 si un compte de pensee passait la borne declaree
r7_pensee = regle7(BORNE_DECL + 1)
assert r7_pensee == 198656 and r7_pensee > SEUILS[7]
t(f"  si le plus grand compte de pensée de l'essai passait {ent(BORNE_DECL)}, la sortie observée le passerait aussi : la règle 7 rendrait au moins {ent(r7_pensee)}, au-dessus de {ent(SEUILS[7])}")
put("R7_SI_PENSEE", ent(r7_pensee))
put("BORNE_DECL", ent(BORNE_DECL))
put("SMAX_ESSAI_J", ent(SMAX_ESSAI_J))
# seuils en euros, a la regle des avenants : plancher au centime de [solde en euros x taux x 0,95]
TAUX = F(10990, 10000)   # M : avenant 2, section 7 (fixage du 2026-11-20, 1,0990 USD pour 1 euro)
T95 = TAUX * F(95, 100)
assert T95 == F(104405, 100000)


def euros_a_voir(usd):
    return _arr(F(usd) / T95, 2, "sup")


def credit_compte(eur):
    return _arr(F(eur) * T95, 2, "inf")


seuil_j = PLJ["80"] + CN
eur_j = euros_a_voir(seuil_j)
assert credit_compte(eur_j) >= seuil_j > credit_compte(eur_j - F(1, 100))
t(f"  taux relevé (avenant 2) : 1,0990 USD pour 1 € ; diminué de 5 % : {fr(T95, 5)}")
t(f"  seuil d'une ligne du juge : {fr(seuil_j)} USD comptés, soit {fr(eur_j)} € vus par projet ({fr(eur_j)} € comptent pour {fr(credit_compte(eur_j))} USD ; {fr(eur_j - F(1, 100))} € pour {fr(credit_compte(eur_j - F(1, 100)))})")
put("EUR_J", fr(eur_j))
put("EUR_J_MOINS", fr(eur_j - F(1, 100)))
put("CC_J_MOINS", fr(credit_compte(eur_j - F(1, 100))))
put("T95", fr(T95, 5))
SOLDES = (F(1193, 100), F(1559, 100))   # M : avenant 1, version 3 (captures du 2026-11-21T16:24:17Z)
manques = [eur_j - s for s in SOLDES]
assert all(m_ > 0 for m_ in manques)
t(f"  aux soldes vus avant les essais (11,93 € et 15,59 €) : il manquerait {fr(manques[0])} € et {fr(manques[1])} €, soit {fr(sum(manques))} € en tout")
put("MANQUE_A", fr(manques[0]))
put("MANQUE_B", fr(manques[1]))
put("MANQUE_TOT", fr(sum(manques)))
# si chaque projet a ete porte au solde que l'avenant 2 demande pour les essais
EUR_AV2 = F(3158, 100)   # M : avenant 2, section 3.3
assert euros_a_voir(AV2_PRUDENT) == EUR_AV2
cc_av2 = credit_compte(EUR_AV2)
assert cc_av2 == AV2_PRUDENT
marge_essais = cc_av2 - seuil_j
ATT_ESSAIS_G = F(38, 100)   # M : avenant 2, section 12 (attendu chez Google seul)
assert marge_essais == F(490, 100) and marge_essais > ATT_ESSAIS_G
t(f"  si chaque projet a été porté à {fr(EUR_AV2)} € pour les essais (avenant 2) : crédit compté {fr(cc_av2)} USD ; la ligne 7 passe son seuil tant que les essais n'ont pas compté plus de {fr(cc_av2)} − {fr(seuil_j)} = {fr(marge_essais)} USD chez Google (attendu des essais chez Google : {fr(ATT_ESSAIS_G)})")
put("EUR_AV2", fr(EUR_AV2))
put("CC_AV2", fr(cc_av2))
put("MARGE_ESSAIS", fr(marge_essais))
put("ATT_ESSAIS_G", fr(ATT_ESSAIS_G))
eur_2l = euros_a_voir(expo_course)
t(f"  lignes 7 et 8 sans pièce de constat neuve entre les deux, la ligne 7 au pire : {fr(expo_course)} USD comptés, soit {fr(eur_2l)} € vus par projet")
put("EUR_2L", fr(eur_2l))
rows = [
    f"| juge, 80 appels (ligne 7) | {PLJ['80']} | {fr(CN, 2)} | **{fr(seuil_j)}** | **{fr(eur_j)} €** |",
    f"| juge, 72 appels de la révision (ligne 8), après une pièce de constat neuve | {PLJ['72']} | {fr(CN, 2)} | **{fr(PLJ['72'] + CN)}** | **{fr(euros_a_voir(PLJ['72'] + CN))} €** |",
    f"| lignes 7 et 8 sans pièce de constat neuve entre les deux, la ligne 7 au pire | {PLJ['80'] + PLJ['72']} | {fr(2 * CN, 2)} | {fr(expo_course)} | {fr(eur_2l)} € |",
]
put("T_CREDIT_G", "\n".join(rows))

# ---------------------------------------------------------------- 15. « 160 artefacts » ou 128 appels (verification, m-2)
t()
t("== 15. « 160 artefacts » à la ligne des quatre épreuves mécaniques de 6.11, pour 128 appels par lecteur à son tableau (brouillon 2 ; vérification, m-2)")
EXTRA = 160 - 128
e2k_epr_160 = E2K["epreuve"] + K_RED * EXTRA * cc_m
pl4_160 = sup5(M_SUPPOSE * e2k_epr_160 + RES_M)
x_rho4 = C1 / (13888 + 1248 * 4)
l1_hi_160 = L1["epreuve"][1] + EXTRA * 4 * x_rho4
pl1_160 = sup5(M_SYNTH * l1_hi_160 + RES_1)
t(f"  si le lot comptait 160 appels par lecteur, soit {EXTRA} lectures de couverture de plus : second lecteur, lots d'épreuve {fr(e2k_epr_160)} USD attendus, la règle rend {fr(M_SUPPOSE * e2k_epr_160 + RES_M)} → {pl4_160} (maximum : {PL2['epreuve']})")
t(f"  premier lecteur, lots d'épreuve, au rapport de coût de 4 : jusqu'à {fr(l1_hi_160)} USD, la règle rend {fr(M_SYNTH * l1_hi_160 + RES_1)} → {pl1_160} (maximum : {PL1['epreuve']})")
assert pl4_160 > PL2["epreuve"] and pl1_160 > PL1["epreuve"]
t(f"  lectures des deux lecteurs : {ent(2 * (tot_sans + EXTRA))} sans révision ; majorant des envois : 3 × ({ent(2 * (tot_sans + EXTRA))} + 4 352 + 152) = {ent(3 * (2 * (tot_sans + EXTRA) + 4352 + 152))}")
put("L2_EPR_160", fr(e2k_epr_160))
put("EXTRA_160", str(EXTRA))
put("L1_EPR_160", fr(l1_hi_160))
put("PL_160", str(pl4_160))
assert pl4_160 == pl1_160 == 60

# ---------------------------------------------------------------- sortie
if __name__ == "__main__":
    if "--json" in sys.argv:
        json.dump({"valeurs": OUT, "trace": TRACE}, sys.stdout, ensure_ascii=False, indent=1)
    else:
        print("\n".join(TRACE))
