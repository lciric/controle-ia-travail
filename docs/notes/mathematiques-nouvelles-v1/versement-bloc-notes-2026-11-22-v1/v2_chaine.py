import os, tempfile, json
from controle_ia.oracles_plantes_v2.parametres import charger
from controle_ia.oracles_plantes_v2.banque import construire_banque
from controle_ia.oracles_plantes_v2.tests_de_mort import appliquer_batterie, sortie_de_texte, appliquer_t6
from controle_ia.oracles_plantes_v2.lignee import Registre
p,_ = charger()
banque = construire_banque(11, p)
def reg(): return Registre(os.path.join(tempfile.mkdtemp(), "r.jsonl"))
def essai(m, t, **kw):
    r = appliquer_batterie(sortie_de_texte(t), m, **kw)
    print("  ", t[:120], "->", r.statut, [(i.test, i.type.value, i.motif[:60]) for i in r.issues][-1])
    return r
for w in range(8, 12):
    m, plantes = banque[w]
    for pl in plantes:
        if pl.etiquette != "VERITE_PLANTEE" or pl.gabarit not in ("periode_modulaire", "cassini"): continue
        T = pl.texte
        corps = T.split(", ", 1)[1]
        print("monde", w, pl.gabarit, "|", T)
        R = reg()
        essai(m, f"pour tout n dans NAT, ({corps}) et n != 2", registre=R)
        essai(m, f"pour tout n dans NAT, ({corps}) et (n != 2 ou u(1000) > 0)", registre=R)
        essai(m, T, registre=R)
# survie d'une morte reformulée : piège tué par T6, puis reformulations
m, plantes = banque[8]
pg = next(x for x in plantes if x.etiquette == "PIEGE" and x.gabarit == "seuil_u")
print("piège", pg.texte, pg.instance)
R = reg()
r = essai(m, pg.texte, registre=R)
iss = appliquer_t6(json.dumps({"verdict": "faux", "contre_exemples": [{"n": int(pg.instance["n"])}], "raison": "x"}), r.arbre, m, R)
print("   T6:", iss.type.value)
c = pg.texte.split("< ")[1]
for t in [f"pour tout k dans NAT, u(k) <= {c} - 1",
          f"pour tout n dans NAT, pour tout m dans NAT, m = n implique u(m) < {c}",
          f"pour tout n dans NAT, pour tout j dans [0 .. 0], u(n + j) < {c}",
          f"pour tout n dans NAT, u(n) < {c} et 0 * w(n + 1) = 0",
          f"pour tout n dans NAT, u(n) < {c} et u(n) >= 0",
          f"pour tout n dans NAT, 2 * u(n) < 2 * {c}"]:
    essai(m, t, registre=R)
