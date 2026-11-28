"""Mise en forme par programme des tables de É5 (aucun chiffre recopié à la main)."""
import json
from pathlib import Path

def pc(x, d=0):
    return "—" if x is None else (f"{100 * x:.{d}f}".replace(".", ",") + " %")

def t(l, k, champ="taux"):
    v = l.get(k)
    return None if v is None else v.get(champ)

def ic(l, k):
    v = l.get(k)
    if v is None: return ""
    a, b = v["ic95"]
    return f" [{100*a:.0f} ; {100*b:.0f}]"

def pts(x):
    return "—" if x is None else f"{100 * x:+.1f}".replace(".", ",")

def aire(x):
    return f"{x:.2f}".replace(".", ",")

NOMS_NULS = {
 "H1-nul-aucun-signal": "aucun signal dans la sonde",
 "H1-nul-vehicule-temoin-parfait": "empreinte de l'adaptateur seule, témoin-jumeau parfait",
 "H1-nul-vehicule-temoin-imparfait-sonde-deux-fois-plus-chargee": "empreinte seule, témoin imparfait (0,3), sonde 2 fois plus sensible à l'empreinte qu'une direction de plancher",
 "H1-nul-vehicule-temoin-imparfait-sonde-trois-fois-plus-chargee": "empreinte seule, témoin imparfait (0,3), sonde 3 fois plus sensible",
 "H1-nul-vehicule-temoin-imparfait-sonde-quatre-fois-plus-chargee": "empreinte seule, témoin imparfait (0,3), sonde 4 fois plus sensible",
 "H2-nul-aucun-signal": "aucun signal dans la sonde",
 "H2-nul-blanc-egal-noir": "sonde et boîte noire de même force (0,75)",
 "H2-nul-vehicule-temoin-imparfait-sonde-deux-fois-plus-chargee": "empreinte seule, témoin imparfait (0,3), sonde 2 fois plus sensible",
 "H2-nul-vehicule-temoin-imparfait-sonde-trois-fois-plus-chargee": "empreinte seule, témoin imparfait (0,3), sonde 3 fois plus sensible",
 "H2-nul-vehicule-temoin-imparfait-sonde-quatre-fois-plus-chargee": "empreinte seule, témoin imparfait (0,3), sonde 4 fois plus sensible",
}

def table_h1(lignes):
    s = ["| aire de la sonde, action sabotée | aire de la boîte noire | tâches | mondes | sonde « Porteuse » | gain moyen de rappel (points) | borne basse du gain > 0 | **H1 tenue** [IC 95 %] |", "|---|---|---|---|---|---|---|---|"]
    for l in lignes:
        if l["cellule"] != "H1-puissance": continue
        p = l["parametres"]
        s.append(f"| {aire(p['aire_sonde'])} | {aire(p['aire_noire'])} | {l['taches']} | {l['mondes']} | {pc(t(l,'porteuse'))} | {pts(t(l,'delta_tpr','moyenne'))} | {pc(t(l,'h1_gain'))} | **{pc(t(l,'H1_TENUE'))}**{ic(l,'H1_TENUE')} |")
    return "\n".join(s)

def table_h1_nuls(lignes):
    s = ["| monde nul (aucun effet du sabotage sur la sonde) | tâches | mondes | clause 1 | clause 3 | borne basse du gain > 0 | alerte de la combinaison sur le témoin-jumeau | **H1 tenue à tort** [IC 95 %] |", "|---|---|---|---|---|---|---|---|"]
    for l in lignes:
        if not l["cellule"].startswith("H1-nul"): continue
        s.append(f"| {NOMS_NULS.get(l["cellule"], l["cellule"])} | {l['taches']} | {l['mondes']} | {pc(t(l,'c1'))} | {pc(t(l,'c3'))} | {pc(t(l,'h1_gain'))} | {pc(t(l,'alerte_jumeau_combinaison','moyenne'),1)} | **{pc(t(l,'H1_TENUE'),1)}**{ic(l,'H1_TENUE')} |")
    return "\n".join(s)

def table_h2(lignes):
    s = ["| aire de la sonde | aire de la boîte noire | tâches | mondes | sonde « Porteuse » | bat le dernier état | bat le maximum | bat la cascade | bat l'accumulation noire | bat le maximum noir | bat TRACE-lite | six à la fois | gain net face au jumeau | **rang 1 tenu** [IC 95 %] | rang 2 (cinq à la fois) |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for l in lignes:
        if not l["cellule"].startswith("H2-puissance"): continue
        p = l["parametres"]
        note = " (avec présage : même décalage avant le premier pas saboté)" if "presage" in p else ""
        s.append(f"| {aire(p['aire_sonde'])}{note} | {aire(p['aire_noire'])} | {l['taches']} | {l['mondes']} | {pc(t(l,'porteuse'))} | {pc(t(l,'bat_S_last'))} | {pc(t(l,'bat_S_max'))} | {pc(t(l,'bat_S_casc'))} | {pc(t(l,'bat_S_BB_seq'))} | {pc(t(l,'bat_S_BB_max'))} | {pc(t(l,'bat_TRACE_lite'))} | {pc(t(l,'rang1_six'))} | {pc(t(l,'gain_net'))} | **{pc(t(l,'H2_RANG1_TENUE'))}**{ic(l,'H2_RANG1_TENUE')} | {pc(t(l,'rang2_cinq'))} |")
    return "\n".join(s)

def table_h2_nuls(lignes):
    s = ["| monde nul | mondes | sonde « Porteuse » | six comparateurs battus | gain net face au jumeau | alerte de l'accumulateur sur le témoin-jumeau | **rang 1 tenu à tort** [IC 95 %] |", "|---|---|---|---|---|---|---|"]
    for l in lignes:
        if not l["cellule"].startswith("H2-nul"): continue
        s.append(f"| {NOMS_NULS.get(l["cellule"], l["cellule"])} | {l['mondes']} | {pc(t(l,'porteuse'))} | {pc(t(l,'rang1_six'))} | {pc(t(l,'gain_net'))} | {pc(t(l,'alerte_jumeau_G2N','moyenne'),1)} | **{pc(t(l,'H2_RANG1_TENUE'),1)}**{ic(l,'H2_RANG1_TENUE')} |")
    return "\n".join(s)

def cellule(lignes, nom, archi, **p):
    for l in lignes:
        if l["cellule"] == nom and l["architecture"] == archi and all(abs(l["parametres"].get(k, -9) - v) < 1e-9 for k, v in p.items()):
            return l
    return None

if __name__ == "__main__":
    import sys
    d = json.loads(Path(sys.argv[1]).read_text())
    L = d["lignes"]
    print(table_h1(L)); print(); print(table_h1_nuls(L)); print(); print(table_h2(L)); print(); print(table_h2_nuls(L))
