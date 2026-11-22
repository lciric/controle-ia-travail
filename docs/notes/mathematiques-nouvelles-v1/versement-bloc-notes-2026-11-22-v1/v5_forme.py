import collections
from controle_ia.oracles_plantes_v5.parametres import charger
from controle_ia.oracles_plantes_v5.banque import construire_banque
from controle_ia.oracles_plantes_v5.forme_seule import regle_forme_seule, borne_naturelle, analyse_forme
p,_ = charger()
for racine in (11, 20261122):
    b = construire_banque(racine, p)
    c = collections.Counter(); n = collections.Counter(); rep = collections.defaultdict(set)
    for w, (m, pl) in enumerate(b):
        for x in pl:
            if x.etiquette not in ("VERITE_PLANTEE", "FAUX_TOT", "PIEGE"): continue
            a = m.analyser(x.texte)
            raffinee = regle_forme_seule(a) and not borne_naturelle(a)
            c[x.etiquette] += raffinee; n[x.etiquette] += 1
            rep[x.texte].add((w, x.etiquette))
    print(racine, "règle « seuil à borne non naturelle » :", {k: f"{c[k]}/{n[k]}" for k in n})
    multi = collections.Counter(next(iter(v))[1] for t, v in rep.items() if len({w for w, _ in v}) > 1)
    print("   textes identiques dans plusieurs mondes, par strate :", dict(multi))
