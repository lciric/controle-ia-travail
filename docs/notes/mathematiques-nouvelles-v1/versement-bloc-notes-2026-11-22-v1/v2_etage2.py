import os, tempfile
from controle_ia.oracles_plantes_v2.parametres import charger
from controle_ia.oracles_plantes_v2.banque import construire_banque
from controle_ia.oracles_plantes_v2.tests_de_mort import appliquer_batterie, sortie_de_texte
from controle_ia.oracles_plantes_v2.lignee import Registre
p,_ = charger()
banque = construire_banque(11, p)
def essai(m, t, **kw):
    r = appliquer_batterie(sortie_de_texte(t), m, **kw)
    print("  ", t[:130], "->", r.statut, [(i.test, i.type.value, i.motif[:70]) for i in r.issues][-1])
for w in (8, 9):
    m, plantes = banque[w]
    for pl in plantes:
        if pl.etiquette == "VERITE_PLANTEE" and pl.gabarit in ("duplication", "addition"):
            T = pl.texte
            R = Registre(os.path.join(tempfile.mkdtemp(), "r.jsonl"))
            print("monde", w, pl.gabarit)
            if pl.gabarit == "duplication":
                corps = T.split(", ", 1)[1]
                essai(m, f"pour tout n dans NAT, ({corps}) et (w(n - 1) > 0 ou w(n - 1) <= 0)", registre=R)
            else:
                corps = T.split(", ", 2)[2]
                essai(m, f"pour tout n dans NAT, pour tout m dans NAT, ({corps}) et (w(m - 1) > 0 ou w(m - 1) <= 0)", registre=R)
            essai(m, T, registre=R)
m, _ = banque[8]
R = Registre(os.path.join(tempfile.mkdtemp(), "r.jsonl"))
essai(m, "pour tout n dans NAT, w(n - 1) > 0 ou w(n - 1) <= 0", registre=R)
essai(m, "pour tout n dans NAT, n >= 1 implique (w(n - 1) > 0 ou w(n - 1) <= 0)", registre=R)
