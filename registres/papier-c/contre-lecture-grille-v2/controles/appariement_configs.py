"""Contre-lecteur de la grille (rapport v2) : appariement des seize temoins par la regle des temoins du texte, sur les
longueurs d'une ou plusieurs configurations ; la premiere donnee est la reference (celle de la grille, brouillon 3).
Ne lit que controle_redaction.longueurs_temoins et controle_redaction.longueurs_A. Reecrit sans importer les programmes
de la grille.
Usage : python3 -B appariement_configs.py REFERENCE.json [AUTRE.json ...]
Au scellement : REFERENCE = archive/papier-C-config-v1-brouillon3.json de la grille, AUTRE = prereg/papier-C-config-v1.json.
Code de sortie 0 si tous les appariements egalent la reference, 1 sinon."""
import hashlib, json, os, sys
FAM = ["flatterie_supplication", "revendication_autorite", "approbations_forgees", "usurpation_stylistique", "ordres_en_bande"]
INDICES = ([1, 8, 16], [1, 4, 8, 12, 16])


def app(cfg, idxs):
    cr = cfg.get("controle_redaction", {})
    if "longueurs_temoins" not in cr or "longueurs_A" not in cr:
        return None
    lt = cr["longueurs_temoins"]
    out = {}
    for f in FAM:
        lf = cr["longueurs_A"][f]
        pris, l = set(), []
        for i in idxs:  # rangs croissants ; temoin de longueur la plus proche non encore pris dans la famille ; egalite : plus petit indice
            b = min((abs(lt[t] - lf[i - 1]), t) for t in range(16) if t not in pris)
            pris.add(b[1])
            l.append(b[1])
        out[f] = l
    return out


def main(chemins):
    ref, tous_egaux = {}, True
    for n, ch in enumerate(chemins):
        brut = open(ch, "rb").read()
        cfg = json.loads(brut.decode("utf-8"))
        cr = cfg.get("controle_redaction", {})
        print(f"{os.path.basename(ch)}  sha256 {hashlib.sha256(brut).hexdigest()}")
        for idxs in INDICES:
            a = app(cfg, idxs)
            if n == 0:
                ref[tuple(idxs)] = a
                verdict = "(reference)"
            elif a is None:
                verdict, tous_egaux = "LONGUEURS ABSENTES", False
            elif a == ref[tuple(idxs)]:
                verdict = "IDENTIQUE a la reference"
            else:
                verdict, tous_egaux = "DIFFERENT de la reference", False
            print("   indices", idxs, ": temoins par famille", None if a is None else [a[f] for f in FAM], verdict)
        if "longueurs_temoins" in cr:
            print("   longueurs des temoins :", cr["longueurs_temoins"])
            print("   longueurs des formulations du corpus A aux indices 1, 4, 8, 12, 16 :",
                  {f: [cr["longueurs_A"][f][i - 1] for i in (1, 4, 8, 12, 16)] for f in FAM})
    print("TOUS IDENTIQUES A LA REFERENCE" if tous_egaux else "AU MOINS UN APPARIEMENT DIFFERE")
    return 0 if tous_egaux else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
