import os, tempfile, json
from controle_ia.gardes import GardeArret
from controle_ia.oracles_plantes_v6.parametres import charger
from controle_ia.oracles_plantes_v6.banque import construire_banque
from controle_ia.oracles_plantes_v6.tests_de_mort import appliquer_batterie, sortie_de_texte, appliquer_t6
from controle_ia.oracles_plantes_v6.lignee import Registre
p,_ = charger()
banque = construire_banque(11, p)
def reg(): return Registre(os.path.join(tempfile.mkdtemp(), "r.jsonl"))
def essai(m, t, **kw):
    try:
        r = appliquer_batterie(sortie_de_texte(t), m, **kw)
        print("  ", t[:110], "->", r.statut, "collision" if r.collision else "", [(i.test, i.type.value, i.motif[:45]) for i in r.issues][-1])
        return r
    except Exception as e:
        print("  ", t[:110], "-> EXCEPTION", type(e).__name__, str(e)[:100])
m, plantes = banque[8]
T = next(x.texte for x in plantes if x.gabarit == "duplication")
corps = T.split(", ", 1)[1]
B = f"pour tout n dans NAT, ({corps}) et w(n - 1) * 0 = 0"
print("16 : morte puis vérité, vérité-morte-vérité"); R = reg(); essai(m, B, registre=R); essai(m, T, registre=R); essai(m, B, registre=R); essai(m, T, registre=R)
print("piège tué par T6, puis même texte et réécritures")
pg = next(x for x in plantes if x.gabarit == "seuil_u"); c = pg.texte.split("< ")[1]
R = reg(); r = essai(m, pg.texte, registre=R)
print("   T6:", appliquer_t6(json.dumps({"verdict":"faux","contre_exemples":[{"n": int(pg.instance["n"])}],"raison":"x"}), r.arbre, m, R).type.value)
for t in [pg.texte, f"pour tout k dans NAT, u(k) < {c}", f"pour tout k dans NAT, ((u(k) < {c}))", f"pour tout n dans NAT, non (u(n) >= {c})",
          f"pour tout k dans NAT, u(k) <= {c} - 1",
          f"pour tout n dans NAT, u(n) < {c} et (n + 1)^16 * (n + 2)^16 * (n + 3)^16 >= 0",
          f"pour tout n dans NAT, u(n) < {c} et (n + 1)^16 * (n + 2)^16 * (n + 3)^16 * (n + 4)^16 * (n + 5)^16 >= 0",
          f"pour tout n dans NAT, u(n) + 0 * {'9'*1500} < {c}"]:
    essai(m, t, registre=R)
print("vérité plantée sous forme brute, après une morte brute")
big = "(n + 1)^16 * (n + 2)^16 * (n + 3)^16 * (n + 4)^16 * (n + 5)^16 >= 0"
R = reg()
essai(m, f"pour tout n dans NAT, ({corps}) et ({big}) et n != 2", registre=R)
essai(m, f"pour tout n dans NAT, ({corps}) et ({big})", registre=R)
essai(m, T, registre=R)
