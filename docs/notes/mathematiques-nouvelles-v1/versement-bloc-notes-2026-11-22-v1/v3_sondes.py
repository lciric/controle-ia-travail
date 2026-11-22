import os, tempfile, json
from controle_ia.gardes import GardeArret
from controle_ia.oracles_plantes_v3.parametres import charger
from controle_ia.oracles_plantes_v3.banque import construire_banque
from controle_ia.oracles_plantes_v3.tests_de_mort import appliquer_batterie, sortie_de_texte, appliquer_t6
from controle_ia.oracles_plantes_v3.normalisation import normaliser
from controle_ia.oracles_plantes_v3.lignee import Registre
p,_ = charger()
banque = construire_banque(11, p)
def reg(): return Registre(os.path.join(tempfile.mkdtemp(), "r.jsonl"))
def essai(m, t, **kw):
    try:
        r = appliquer_batterie(sortie_de_texte(t), m, **kw)
        print("  ", t[:120], "->", r.statut, [(i.test, i.type.value, i.motif[:50]) for i in r.issues][-1])
        return r
    except GardeArret as e:
        print("  ", t[:120], "-> ARRÊT", e)
m, plantes = banque[8]
T = next(x.texte for x in plantes if x.gabarit == "duplication")
corps = T.split(", ", 1)[1]
B = f"pour tout n dans NAT, ({corps}) et w(n - 1) * 0 = 0"
f1, f2 = normaliser(m.analyser(T), m, m.ev), normaliser(m.analyser(B), m, m.ev)
print("même empreinte :", f1.empreinte == f2.empreinte)
print("cas 1 : B puis vérité plantée"); R = reg(); essai(m, B, registre=R); essai(m, T, registre=R)
print("cas 2 : vérité, B, vérité"); R = reg(); essai(m, T, registre=R); essai(m, B, registre=R); essai(m, T, registre=R)
print("cas 3 : énoncé vrai simple")
R = reg(); essai(m, "pour tout n dans NAT, n >= 1 implique w(n - 1) >= 0", registre=R)
essai(m, "pour tout n dans NAT, (n >= 1 implique w(n - 1) >= 0) et w(n - 1) * 0 = 0", registre=R)
essai(m, "pour tout n dans NAT, n >= 1 implique w(n - 1) >= 0", registre=R)
print("rejeu des chaînes v2 sur v3")
for w in (8, 9):
    m, plantes = banque[w]
    for pl in plantes:
        if pl.gabarit in ("cassini", "periode_modulaire"):
            c = pl.texte.split(", ", 1)[1]; R = reg()
            essai(m, f"pour tout n dans NAT, ({c}) et n != 2", registre=R)
            essai(m, f"pour tout n dans NAT, ({c}) et (n != 2 ou u(1000) > 0)", registre=R)
            essai(m, pl.texte, registre=R)
        if pl.gabarit in ("duplication", "addition"):
            R = reg()
            if pl.gabarit == "duplication":
                c = pl.texte.split(", ", 1)[1]
                essai(m, f"pour tout n dans NAT, ({c}) et (w(n - 1) > 0 ou w(n - 1) <= 0)", registre=R)
            else:
                c = pl.texte.split(", ", 2)[2]
                essai(m, f"pour tout n dans NAT, pour tout m dans NAT, ({c}) et (w(m - 1) > 0 ou w(m - 1) <= 0)", registre=R)
            essai(m, pl.texte, registre=R)
print("héritage du piège tué par T6")
m, plantes = banque[8]
pg = next(x for x in plantes if x.gabarit == "seuil_u")
R = reg(); r = essai(m, pg.texte, registre=R)
print("   T6:", appliquer_t6(json.dumps({"verdict":"faux","contre_exemples":[{"n": int(pg.instance["n"])}],"raison":"x"}), r.arbre, m, R).type.value)
c = pg.texte.split("< ")[1]
for t in [pg.texte.replace("n", "k").replace("NAT", "NAT"), f"pour tout k dans NAT, u(k) <= {c} - 1", f"pour tout n dans NAT, 2 * u(n) < 2 * {c}",
          f"pour tout n dans NAT, u(n) < {c} et u(n) >= 0", f"pour tout n dans NAT, {c} > u(n)"]:
    essai(m, t, registre=R)
print("vacuité")
R = reg(); essai(m, "pour tout n dans NAT, n > N + 5 implique 0 = 0", registre=R); essai(m, "1 = 1", registre=R)
essai(m, "pour tout n dans NAT, n > N + 5 implique 0 = 0", registre=R)
