"""Diagnostic de forme des réponses de la passe X classées « défaut » par la garde de coupure — v1.

Accordé par la mère (13:12Z), après la passe, à ses conditions : programme écrit et contre-lu avant d'être lancé ; il ne
lit que les flux classés « défaut » ; il ne rend que des comptes de motifs fixés d'avance (titres, ligne finale, langue
des titres) ; aucun extrait de texte ne sort ; sa sortie est versée et scellée.

Entrées : le journal de la passe (métadonnées) et le dossier de quarantaine. Pour chaque ligne « garde de coupure » dont
la cause n'est pas nulle, le flux est celui de la dernière tentative « réponse rendue » du même proposeur et du même
texte servi, retrouvé par son empreinte (`flux_sha256`). Le texte est reconstitué par `lire_flux` du lot 11 v4, en
mémoire seulement. Sortie : un JSON de comptes, par flux, sans aucun texte. Aucun réseau.

    python3 -B diagnostic_forme_passe_x_v1.py --journal J --quarantaine Q --sortie S.json
"""
import argparse, hashlib, importlib.util, json, os, re, sys

LOT = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/lot-11-passe-x-v4/passe_x_na_v4.py"
EMPREINTE_LOT = None  # contrôlée contre le compagnon du module

# Motifs fixés d'avance (comptes seulement). Chaque motif compte des lignes.
MOTIFS = {
    "titre_reponse_k": r"^[ \t#*_>]*Réponse[ \t]+\d+\b",          # forme demandée (celle de la garde)
    "titre_reponse_k_autre_espace": r"^[ \t#*_>]*R[ée]ponse[\s  ]*\d+",
    "titre_answer_k": r"^[ \t#*_>]*(Answer|Response)[\s ]*\d+",
    "titre_piece_k": r"^[ \t#*_>]*(\[?Pi[èe]ce|Question)[\s ]*\d+",
    "titre_numero_seul": r"^[ \t#*_>]*\d+[.):][ \t]",
    "titre_markdown": r"^#{1,6}[ \t]",
    "titre_gras_seul": r"^\*\*[^*]+\*\*[ \t]*$",
    "ligne_finale_exacte": r"^[ \t*_#>]*FIN DES RÉPONSES[ \t*_]*$",
    "ligne_finale_ponctuee": r"^[ \t*_#>]*FIN DES R[ÉE]PONSES[ \t*_]*[.!]?[ \t*_]*$",
    "ligne_finale_casse": r"(?i)^[ \t*_#>]*fin des r[ée]ponses",
    "ligne_finale_anglaise": r"(?i)^[ \t*_#>]*end of (the )?(answers|responses)",
}
LANGUE = {"fr": r"(?i)\b(réponse|pièce|question)\b", "en": r"(?i)\b(answer|response|piece)\b"}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def charger_lot():
    b = open(LOT, "rb").read()
    if open(LOT + ".sha256").read().split()[0] != sha(b):
        sys.exit("REFUS : module du lot 11 v4 différent de son compagnon")
    spec = importlib.util.spec_from_file_location("passe_x_na_v4", LOT)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def evenements(octets):
    for ligne in octets.split(b"\n"):
        l = ligne.strip()
        if l.startswith(b"data:"):
            c = l[5:].strip()
            if c == b"[DONE]":
                continue
            try:
                yield json.loads(c)
            except ValueError:
                continue


def defauts(journal):
    """Rend [(proposeur, texte_servi, fournisseur, flux_sha256, cause)] pour chaque garde en défaut."""
    derniere, out = {}, []
    for l in open(journal, encoding="utf-8"):
        d = json.loads(l)
        t = d.get("type_ligne")
        if t == "tentative" and d.get("classe") == "réponse rendue":
            derniere[(d["proposeur"], d["texte_servi"])] = d
        elif t == "garde de coupure" and d.get("cause"):
            ten = derniere.get((d["proposeur"], d["texte_servi"]))
            if ten is None:
                sys.exit("REFUS : garde sans tentative rendue associée")
            out.append((d["proposeur"], d["texte_servi"], ten["fournisseur"], ten["flux_sha256"], d["cause"]))
    return out


def comptes(texte, rangs):
    lignes = texte.split("\n")
    c = {k: sum(1 for l in lignes if re.search(v, l)) for k, v in MOTIFS.items()}
    titres = [l for l in lignes if re.search(r"^[ \t]*(#{1,6}|\*\*|\d+[.):])", l)]
    c["langue_des_titres"] = {k: sum(1 for l in titres if re.search(v, l)) for k, v in LANGUE.items()}
    nonvides = [l for l in lignes if l.strip()]
    der = nonvides[-1] if nonvides else ""
    c["derniere_ligne"] = {k: bool(re.search(MOTIFS[k], der)) for k in
                           ("ligne_finale_exacte", "ligne_finale_ponctuee", "ligne_finale_casse", "ligne_finale_anglaise")}
    c["numeros_de_pieces_cites_en_titre"] = sorted({int(n) for l in titres for n in re.findall(r"\b(\d{1,2})\b", l)
                                                    if int(n) in rangs})
    c["lignes"] = len(lignes)
    c["signes"] = len(texte)
    return c


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--journal", required=True)
    a.add_argument("--quarantaine", required=True)
    a.add_argument("--sortie", required=True)
    o = a.parse_args(argv)
    if os.path.exists(o.sortie):
        sys.exit("REFUS : sortie déjà présente")
    lot = charger_lot()
    par_sha = {}
    for f in sorted(os.listdir(o.quarantaine)):
        if f.endswith(".flux"):
            par_sha[sha(open(os.path.join(o.quarantaine, f), "rb").read())] = f
    res = []
    for prop, texte_servi, fourn, h, cause in defauts(o.journal):
        if h not in par_sha:
            sys.exit("REFUS : flux introuvable par son empreinte")
        r = lot.lire_flux(fourn, evenements(open(os.path.join(o.quarantaine, par_sha[h]), "rb").read()))
        res.append({"proposeur": prop, "texte_servi": texte_servi, "fournisseur": fourn, "flux_sha256": h,
                    "cause": cause, "comptes": comptes(r["texte"], lot.RANGS_TEXTES[texte_servi])})
    sortie = {"version": "diagnostic-forme-passe-x-v1", "motifs": MOTIFS, "langue": LANGUE, "flux": res}
    s = json.dumps(sortie, ensure_ascii=False, indent=1, sort_keys=True)
    with open(o.sortie, "x", encoding="utf-8") as f:
        f.write(s + "\n")
    print(json.dumps({"flux_diagnostiques": len(res)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
