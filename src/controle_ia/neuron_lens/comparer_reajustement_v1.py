"""Comparaison d'une lentille réajustée à celle du 18 novembre (critère d'identité du réajustement, v2) — v1.

Applique `docs/notes/neuron-lens-v1/devis-reajustement/critere-identite-reajustement-lentilles-v2.md` : palier 1 (octets identiques),
palier 2 (différences entre moitiés concordantes à la tolérance près ; octets différents ; matrices non comparables), « différente »,
« non comparable » (un préalable manqué, traité comme « différente »), et l'audit à cinq déclencheurs, le même dans les deux sens.

Lit seulement : les deux résultats d'ajustement (`b-beta-ajustement-<L>.json` du 18 et de la course neuve), les deux manifestes de course,
pour R les deux résultats d'export, et le code source des deux lanceurs pour l'empreinte de la fonction `_split_half_64`. Aucune mesure
de la course (aucun `score`, aucune grandeur, aucun verdict) n'est lue. Aucun repli silencieux (R5) : une valeur non finie, absente ou
de compte différent rend « non comparable » ; jamais avalée par un maximum.

Usage :
  python -m controle_ia.neuron_lens.comparer_reajustement_v1 --ref-ajustement A.json --neuf-ajustement B.json \
      --ref-manifeste M1.json --neuf-manifeste M2.json --lanceur-ref L1.py --lanceur-neuf L2.py \
      [--ref-export E1.json --neuf-export E2.json] [--reprise] --sortie S.json
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import sys
from pathlib import Path

TOLERANCE = 1e-3          # conventionnelle, déclarée telle (critère v2, palier 2)
SEUIL_STABILITE = 0.10    # seuil de stabilité de la tranche (texte gelé, B-1)
N_DOCS_ATTENDU = [466, 466]
NEXT_DOC_ATTENDU = 932
FONCTION = "_split_half_64"

PALIER_1 = "palier 1 — même lentille, octets identiques"
PALIER_2 = "palier 2 — différences entre moitiés concordantes à 10⁻³ près ; octets différents ; matrices non comparables"
DIFFERENTE = "différente"
NON_COMPARABLE = "non comparable (traitée comme différente)"
SUSPENDU = "mention suspendue : anomalie (nœud de Lazar)"


def empreinte_fonction(source: str, nom: str = FONCTION) -> str | None:
    """SHA-256 du texte source exact de la fonction `nom` (None si absente)."""
    arbre = ast.parse(source)
    for n in ast.walk(arbre):
        if isinstance(n, ast.FunctionDef) and n.name == nom:
            seg = ast.get_source_segment(source, n)
            return hashlib.sha256(seg.encode("utf-8")).hexdigest() if seg is not None else None
    return None


def _fini(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def _series(res: dict, champ: str):
    """{cible: liste} ou None si la forme est mauvaise."""
    s = res.get(champ)
    if not isinstance(s, dict) or not s:
        return None
    if not all(isinstance(v, list) for v in s.values()):
        return None
    return s


def preconditions(ref: dict, neuf: dict, mref: dict, mneuf: dict, fref: str | None, fneuf: str | None) -> list[dict]:
    """Chaque préalable : {nom, tenu, detail}. Tous exigés pour le palier 2."""
    p = []

    def ajoute(nom, tenu, detail=""):
        p.append({"nom": nom, "tenu": bool(tenu), "detail": detail})

    for champ in ("diffs_float64", "diffs"):
        sr, sn = _series(ref, champ), _series(neuf, champ)
        forme = sr is not None and sn is not None and set(sr) == set(sn) and all(len(sr[t]) == len(sn[t]) for t in sr)
        ajoute(f"mêmes cibles et mêmes comptes ({champ})", forme,
               "" if forme else f"ref {None if sr is None else {t: len(v) for t, v in sr.items()}} ; "
                                f"neuf {None if sn is None else {t: len(v) for t, v in sn.items()}}")
        if sr is not None and sn is not None:
            nf = [(c, t, i) for c, s in (("ref", sr), ("neuf", sn)) for t, v in s.items() for i, x in enumerate(v) if not _fini(x)]
            ajoute(f"toutes les valeurs finies ({champ})", not nf, "" if not nf else f"{len(nf)} non finie(s), par ex. {nf[:3]}")
        else:
            ajoute(f"toutes les valeurs finies ({champ})", False, "forme illisible")
    mr, mn = ref.get("meta"), neuf.get("meta")
    if isinstance(mr, dict) and isinstance(mn, dict):
        diff = sorted(k for k in set(mr) | set(mn) if mr.get(k, "<absent>") != mn.get(k, "<absent>"))
        ajoute("meta égal champ par champ", not diff, "" if not diff else f"champs différents : {diff}")
    else:
        ajoute("meta égal champ par champ", False, "meta absent")
    for cote, r in (("ref", ref), ("neuf", neuf)):
        ajoute(f"n_docs {N_DOCS_ATTENDU} ({cote})", r.get("n_docs") == N_DOCS_ATTENDU, f"lu {r.get('n_docs')}")
        ajoute(f"next_doc {NEXT_DOC_ATTENDU} ({cote})", r.get("next_doc") == NEXT_DOC_ATTENDU, f"lu {r.get('next_doc')}")
    ajoute("même nom de fichier d'ajustement", ref.get("fichier") is not None and ref.get("fichier") == neuf.get("fichier"),
           f"ref {ref.get('fichier')} ; neuf {neuf.get('fichier')}")
    cvr = (mref.get("config") or {}).get("commit_voisin")
    cvn = (mneuf.get("config") or {}).get("commit_voisin")
    ajoute("même commit du code voisin", cvr is not None and cvr == cvn, f"ref {cvr} ; neuf {cvn}")
    ajoute(f"même texte de la fonction {FONCTION}", fref is not None and fref == fneuf, f"ref {fref} ; neuf {fneuf}")
    return p


def ecarts(ref: dict, neuf: dict, champ: str) -> list[dict]:
    """Table par cible et par couche (écart signé neuf − ref). Suppose les préalables de forme et de finitude tenus."""
    t = []
    for cible in sorted(ref[champ]):
        for i, (a, b) in enumerate(zip(ref[champ][cible], neuf[champ][cible])):
            t.append({"cible": cible, "rang": i, "ref": a, "neuf": b, "ecart": b - a})
    return t


def _max_abs(table) -> float:
    # explicite : jamais de max() sur une valeur non finie (les préalables l'excluent ; garde en plus)
    m = 0.0
    for r in table:
        e = r["ecart"]
        if not math.isfinite(e):
            raise ValueError("écart non fini malgré les préalables")
        m = max(m, abs(e))
    return m


def comparer(ref: dict, neuf: dict, mref: dict, mneuf: dict, fref: str | None, fneuf: str | None, *,
             eref: dict | None = None, eneuf: dict | None = None, reprise: bool = False, tolerance: float = TOLERANCE) -> dict:
    lentille = (ref.get("meta") or {}).get("lens")
    pre = preconditions(ref, neuf, mref, mneuf, fref, fneuf)
    tous = all(x["tenu"] for x in pre)
    declencheurs = []
    out = {"lentille": lentille, "preconditions": pre, "tolerance": tolerance, "reprise": bool(reprise),
           "sha256": {"ref": ref.get("sha256"), "neuf": neuf.get("sha256")},
           "taille": {"ref": ref.get("taille"), "neuf": neuf.get("taille")}}
    octets_egaux = ref.get("sha256") is not None and ref.get("sha256") == neuf.get("sha256")
    # R : empreintes des matrices des moitiés et des exports, comparées couche par couche (forme de l'égalité d'octets)
    anomalie = None
    if lentille == "R" and eref is not None and eneuf is not None:
        mm_r, mm_n = eref.get("matrices_moities") or {}, eneuf.get("matrices_moities") or {}
        egales = sorted(k for k in mm_r if mm_n.get(k) == mm_r[k])
        out["matrices_moities_egales"] = {"couches_egales": len(egales), "couches_ref": len(mm_r)}
        val_r, val_n = eref.get("valeurs") or {}, eneuf.get("valeurs") or {}
        rapport = {}
        for serie in ("npR_notre_R", "identite_notre_R"):
            a, b = val_r.get(serie) or {}, val_n.get(serie) or {}
            communs = sorted(set(a) & set(b), key=lambda s: int(s))
            rapport[serie] = {"couches": len(communs),
                              "ecarts": {k: (b[k] - a[k]) if _fini(a[k]) and _fini(b[k]) else None for k in communs}}
        out["series_export_R_sans_critere"] = rapport
        if octets_egaux and len(egales) != len(mm_r):
            anomalie = "empreinte du fichier égale mais empreinte de matrice des moitiés différente"
    elif lentille == "S":
        out["series_export_R_sans_critere"] = "sans objet : aucune grandeur sensible à la position n'existe pour S dans les pièces du 18"
    if octets_egaux:
        declencheurs.append("(i) palier 1 obtenu")
        if anomalie:
            declencheurs.append(f"(v) {anomalie}")
            out["mention"] = SUSPENDU
        else:
            out["mention"] = PALIER_1 + (" ; reprise sur sauvegarde notée" if reprise else "")
        out["preconditions_toutes_tenues"] = tous
        out["declencheurs"] = declencheurs
        return out
    if not tous:
        declencheurs.append("(iv) non comparable")
        out.update({"mention": NON_COMPARABLE, "preconditions_toutes_tenues": False, "declencheurs": declencheurs})
        return out
    t64 = ecarts(ref, neuf, "diffs_float64")
    t32 = ecarts(ref, neuf, "diffs")
    m64 = _max_abs(t64)
    rel = max(abs(r["ecart"]) / abs(r["ref"]) for r in t64 if r["ref"] != 0)
    cote = [{"cible": r["cible"], "rang": r["rang"], "ref": r["ref"], "neuf": r["neuf"]}
            for r in t32 if (r["ref"] <= SEUIL_STABILITE) != (r["neuf"] <= SEUIL_STABILITE)]
    out.update({"ecart_max_abs_diffs_float64": m64, "ecart_max_rel_diffs_float64": rel,
                "ecart_max_abs_diffs": _max_abs(t32), "changements_de_cote_du_seuil_0_10_sur_diffs": cote,
                "table_ecarts_diffs_float64": t64, "preconditions_toutes_tenues": True})
    if m64 == 0.0:
        declencheurs.append("(ii) écart maximal exactement nul avec des octets différents")
    if m64 <= tolerance:
        out["mention"] = PALIER_2
    else:
        declencheurs.append("(iii) lentille différente")
        out["mention"] = DIFFERENTE
    out["declencheurs"] = declencheurs
    return out


def _lire(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def _resultat(p):
    d = _lire(p)
    return d["resultat"] if isinstance(d, dict) and "resultat" in d else d


def main(argv=None):
    a = argparse.ArgumentParser(description="Critère d'identité du réajustement (v2) : comparaison d'une lentille")
    for n in ("ref-ajustement", "neuf-ajustement", "ref-manifeste", "neuf-manifeste", "lanceur-ref", "lanceur-neuf", "sortie"):
        a.add_argument(f"--{n}", required=True, type=Path)
    a.add_argument("--ref-export", type=Path)
    a.add_argument("--neuf-export", type=Path)
    a.add_argument("--reprise", action="store_true")
    x = a.parse_args(argv)
    fref = empreinte_fonction(x.lanceur_ref.read_text(encoding="utf-8"))
    fneuf = empreinte_fonction(x.lanceur_neuf.read_text(encoding="utf-8"))
    r = comparer(_resultat(x.ref_ajustement), _resultat(x.neuf_ajustement), _lire(x.ref_manifeste), _lire(x.neuf_manifeste),
                 fref, fneuf, eref=_resultat(x.ref_export) if x.ref_export else None,
                 eneuf=_resultat(x.neuf_export) if x.neuf_export else None, reprise=x.reprise)
    if x.sortie.exists():
        sys.exit(f"{x.sortie} existe déjà : on n'écrase jamais (R12)")
    x.sortie.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{r['lentille']} : {r['mention']} ; déclencheurs : {r['declencheurs']}")


if __name__ == "__main__":
    main()
