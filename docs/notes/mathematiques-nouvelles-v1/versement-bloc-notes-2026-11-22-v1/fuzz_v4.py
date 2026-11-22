import os, sys, tempfile, json, traceback, importlib
import numpy as np
PK = sys.argv[1] if len(sys.argv) > 1 else "oracles_plantes_v4"
M = lambda n: importlib.import_module(f"controle_ia.{PK}.{n}")
p,_ = M("parametres").charger(); tdm = M("tests_de_mort"); L = M("lignee"); ba = M("base_aleatoire")
pb = 0
for racine in (11, 3):
    banque = M("banque").construire_banque(racine, p)
    reg = L.Registre(os.path.join(tempfile.mkdtemp(), "r.jsonl"))
    rng = np.random.default_rng(racine)
    for m, plantes in banque:
        cfg = dict(p["base_aleatoire"], par_monde=60, profondeur_max=5, quantificateurs_max=3, litteral_max=60)
        textes = ba.tirer_base(rng, m, cfg)
        for pl in plantes:
            toks = pl.texte.split(" ")
            for _ in range(6):
                t = list(toks); i = int(rng.integers(0, len(t)))
                op = int(rng.integers(0, 4))
                if op == 0: del t[i]
                elif op == 1: t.insert(i, t[int(rng.integers(0, len(t)))])
                elif op == 2: j = int(rng.integers(0, len(t))); t[i], t[j] = t[j], t[i]
                else: t[i] = t[i] + "0"
                textes.append(" ".join(t))
            n = pl.texte.count("pour tout ")
            if n:
                tete = pl.texte[: len(pl.texte) - len(pl.texte.split(", ", n)[n])]
                corps = pl.texte.split(", ", n)[n]
                v = pl.texte.split("pour tout ")[1].split(" dans")[0]
                part = {"F1": [f"vt({v} - 1)"], "F2": [f"pfa_t(OU, {v} - 1)"], "F3": [f"u({v} - 1)", f"w({v} - 1)", f"v({v} - 1)"]}[m.famille]
                for extra in [f"{x} * 0 = 0" for x in part] + [f"{v} * 0 = 0", f"(u(1000) - u(1000)) * {v} = 0" if m.famille == "F3" else "0 = 0",
                              f"1 / ({v} + 1) > 0", f"{v} ^ 2 >= 0"]:
                    textes += [f"{tete}({corps}) et {extra}", f"{tete}{extra} et ({corps})"]
            textes.append(pl.texte)
        verites = {pl.texte for pl in plantes if pl.etiquette == "VERITE_PLANTEE"}
        for t in textes:
            try:
                r = tdm.appliquer_batterie(tdm.sortie_de_texte(t), m, registre=reg)
                if t in verites and r.statut != "vivante":
                    pb += 1; print("VÉRITÉ NON VIVANTE", racine, m.indice, t[:100], r.issues[-1].motif[:80])
                if r.arbre is not None and rng.random() < 0.3:
                    inst = [{k: int(rng.integers(-3, 3 * m.N + 3)) for k in r.forme.noms_prefixe}]
                    tdm.appliquer_t6(json.dumps({"verdict": "faux", "contre_exemples": inst, "raison": "x"}), r.arbre, m, reg)
            except Exception as e:
                pb += 1
                if pb <= 8: print("PROBLÈME", racine, m.indice, repr(t)[:150], type(e).__name__, str(e)[:150])
    print("racine", racine, "lignes", len(reg.lignes), flush=True)
print("problemes", pb)
