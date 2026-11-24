"""Audit de symétrie (R4) du barreau 5, point 2 : alignement des clés et des étiquettes.

Pour chacun des 30 adaptateurs tenus à l'écart (lignes de la table) : copie lue de sa famille (règle de la relance du
programme figé), empreinte du fichier `adaptateur-<membre>.pt` (calculée ici) contre son compagnon `.sha256`, l'inventaire
de la marche et le résultat de la famille (`diag/<marche>/famille-<copie>.json`, champ `adaptateurs.<membre>.sha256`) ;
empreinte des tenseurs (même définition que `organismes.lora.empreinte_adaptateurs`, recalculée ici depuis le fichier)
contre le résultat de la famille (`empreinte`), le résumé `retenus/formation.json` (`empreintes`) et
`intensites.json[nom opaque].empreinte` (seul champ lu de ce fichier). N'écrit que des comptes ; aucune paire nom
opaque / famille ou membre n'est écrite. Joué avec PYTHONPATH=<racine>/src.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import torch

from controle_ia.barreau5_familles import lecture_v1 as le

BN = Path(sys.argv[1])
SORTIE = Path(sys.argv[2])
TABLE = Path("/dev/shm/b5f-ouverture-v1/table/table-etiquettes-b5f-v1.json")
DEPOT = Path("/home/user/controle-ia-travail")
COMMIT = "8c758785d2d618b3666e909aa206a503b4a9f77a"
INTENSITES = BN / "arbre-lecture/donnees/20261123-044043-b5f-lecture/lecture/intensites.json"


def sha_fichier(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def empreinte_tenseurs(etat: dict, dtype) -> str:
    h = hashlib.sha256()
    for cle, t in sorted(etat.items()):
        t = t.to(dtype) if dtype is not None else t
        h.update(cle.encode("utf-8"))
        h.update((t.view(torch.int16) if t.dtype == torch.bfloat16 else t).contiguous().numpy().tobytes())
    return h.hexdigest()


def main() -> None:
    table = json.loads(TABLE.read_text(encoding="utf-8"))
    texte = subprocess.run(["git", "-C", str(DEPOT), "show", f"{COMMIT}:registres/barreau5-familles-jumelles-v1.md"],
                           capture_output=True, text=True, check=True).stdout
    relance = le.relance_du_registre(texte)
    formation_f = BN / "retenus/formation.json"
    formation_sha_ok = (sha_fichier(formation_f) == (BN / "retenus/formation.json.sha256").read_text().split()[0])
    formation = json.loads(formation_f.read_text(encoding="utf-8"))["familles"]
    intensites = {k: (v or {}).get("empreinte") for k, v in
                  json.loads(INTENSITES.read_text(encoding="utf-8"))["adaptateurs"].items()}
    c = {k: 0 for k in ("lignes", "copie_trouvee", "copie_egale_resume", "pt_egal_compagnon", "pt_egal_inventaire",
                        "pt_egal_diag", "tenseurs_egal_diag", "diag_egal_formation_json", "formation_json_egal_intensites",
                        "tenseurs_egal_intensites", "les_trois_egales")}
    dtypes_qui_egalent = {}
    shas_pt, emps = [], []
    discordances = []
    for k, x in enumerate(table):
        c["lignes"] += 1
        f, m, nom = x["famille"], x["membre"], x["nom"]
        n = le.instance_de(f)
        prefixe = le.prefixe_de_copie(f, relance)
        suffixe = "-x1" if relance and n in relance else ""
        marches = sorted(p for p in (BN / "formation/donnees").glob(f"*-b5f-formation-{n}{suffixe}") if p.is_dir())
        dossiers = [d for mm in marches for d in (mm / prefixe, mm / f"{prefixe}-r1") if d.is_dir()]
        if len(marches) != 1 or len(dossiers) != 1:
            discordances.append(f"ligne {k}: copie introuvable ou multiple")
            continue
        c["copie_trouvee"] += 1
        dossier, marche = dossiers[0], marches[0]
        c["copie_egale_resume"] += formation[f]["copie"] == dossier.name
        pt = dossier / f"adaptateur-{m}.pt"
        s = sha_fichier(pt)
        shas_pt.append(s)
        c["pt_egal_compagnon"] += s == (dossier / f"adaptateur-{m}.pt.sha256").read_text().split()[0]
        inv = json.loads((marche / "inventaire.json").read_text(encoding="utf-8"))["fichiers"]
        rel = f"donnees/{marche.name}/{dossier.name}/adaptateur-{m}.pt"
        c["pt_egal_inventaire"] += any(y["chemin"] == rel and y["sha256"] == s for y in inv)
        diag = json.loads((BN / "formation/diag" / marche.name / f"famille-{prefixe}.json").read_text(encoding="utf-8"))
        ad = diag["resultat"]["adaptateurs"][m]
        c["pt_egal_diag"] += ad["sha256"] == s and ad["chemin"] == pt.name
        etat = torch.load(pt, map_location="cpu", weights_only=True)
        emp_diag = ad["empreinte"]
        trouve = None
        for nom_d, d in (("tel_quel", None), ("bfloat16", torch.bfloat16), ("float16", torch.float16),
                         ("float32", torch.float32)):
            if empreinte_tenseurs(etat, d) == emp_diag:
                trouve = nom_d
                break
        types_fichier = sorted({str(t.dtype) for t in etat.values()})
        cle_t = f"fichier {','.join(types_fichier)} -> {trouve}"
        dtypes_qui_egalent[cle_t] = dtypes_qui_egalent.get(cle_t, 0) + 1
        c["tenseurs_egal_diag"] += trouve is not None
        e_form = formation[f]["empreintes"].get(m)
        e_int = intensites.get(nom)
        c["diag_egal_formation_json"] += emp_diag == e_form
        c["formation_json_egal_intensites"] += e_form == e_int
        c["tenseurs_egal_intensites"] += trouve is not None and emp_diag == e_int
        ok3 = trouve is not None and emp_diag == e_form == e_int
        c["les_trois_egales"] += ok3
        emps.append(emp_diag)
        if not ok3:
            discordances.append(f"ligne {k}: empreinte des tenseurs discordante")
    r = {"comptes": c, "relance": relance, "formation_json_sha_compagnon": formation_sha_ok,
         "types_et_recalcul": dtypes_qui_egalent,
         "empreintes_fichier_pt_distinctes": len(set(shas_pt)), "empreintes_tenseurs_distinctes": len(set(emps)),
         "noms_dans_intensites": len(intensites), "noms_de_la_table_dans_intensites": sum(x["nom"] in intensites for x in table),
         "intensites_sans_empreinte": sum(v is None for v in intensites.values()),
         "membres_par_famille_dans_formation_json": {f: sorted(v["empreintes"]) == sorted(le.MEMBRES)
                                                     for f, v in formation.items()},
         "discordances": discordances}
    # alignement par la fonction du programme figé, sur les mêmes fichiers
    try:
        a = le.exiger_alignement(table, formation, json.loads(INTENSITES.read_text(encoding="utf-8"))["adaptateurs"])
        r["exiger_alignement"] = f"passe ({a['adaptateurs_alignes']} alignés)"
    except Exception as x:          # noqa: BLE001
        r["exiger_alignement"] = f"refus : {type(x).__name__}"
    SORTIE.write_text(json.dumps(r, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
