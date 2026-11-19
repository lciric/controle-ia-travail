"""Comparaison d'une lentille réajustée à celle du 18 novembre (critère d'identité du réajustement, v4 et suivants) — v3.

v3 = v2 (`comparer_reajustement_v2.py`, `23311588…`) qui porte dans le programme les contrôles hors programme H1 à H5 et H7 du critère
d'identité v4 (`critere-identite-reajustement-lentilles-v4.md`, `60df6c53…`, § 7), et H6 comme déclencheur, d'après les sondes du
rédacteur Fable du critère v4 (T1 à T4) :
- H1 : la sortie porte les empreintes de toutes les pièces lues (résultat d'ajustement neuf, manifeste neuf, export neuf, lanceur neuf)
  et le commit de la branche de résultats passé en argument ;
- H2 : pour R, l'export neuf est rattaché à la course neuve (même identifiant de course, même empreinte de manifeste) et diffère de
  celui du 18 ;
- H3 : pour R, les clés des deux séries sont exactement 0 à 27 des deux côtés ;
- H4 : au premier palier, pour R, le plus grand changement de chaque série vaut exactement zéro, sinon mention suspendue ;
- H5 : « même code » : `config.drowse` et `config.precision` égaux, `versions` égales hors `plateforme`, contenu des cinq correctifs
  d'empreinte égale aux deux commits des manifestes (lu dans le dépôt par `git show`) ;
- H6 : au deuxième palier, pour R, 31 matrices égales sur 31 ou une série inchangée à zéro exact : déclencheur (vi), audit requis ;
- H7 : écart sur `diffs` au-delà de 10⁻³ au deuxième palier ou de 10⁻⁶ au premier : déclencheur (vii), mention suspendue.

v2 = v1 (`comparer_reajustement_v1.py`, `247b6959…`) corrigée selon la vérification du critère v2
(`docs/notes/neuron-lens-v1/verification-critere-identite-reajustement-v2-v1.md`, `8a6045bb…`, corrections D1 à D4) :
- D1 : au premier palier, les préalables et la table des écarts sont calculés aussi ; toute incohérence suspend la mention ;
- D2 : préalables de provenance (empreintes et tailles bien formées, `finies`, pièces de référence vérifiées par leur empreinte, course
  neuve distincte, manifeste neuf égal à celui que porte le résultat, six champs de configuration égaux) ;
- D3 : pour R, les pièces d'export sont obligatoires et complètes (31 couches de matrices, 28 couches par série, valeurs finies) ;
- D4 : la tolérance est une constante (la mention est bâtie sur elle) ; toutes les gardes sont essayées.

Lit seulement : les deux résultats d'ajustement (`b-beta-ajustement-<L>.json`), les deux manifestes, pour R les deux résultats d'export,
le code source des deux lanceurs (empreinte de `_split_half_64`). Aucune mesure de la course n'est lue. Aucun repli silencieux (R5).
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import re
import sys
from pathlib import Path

TOLERANCE = 1e-3            # conventionnelle, déclarée telle (critère v3, palier 2) ; constante, non paramètre
COHERENCE_PALIER_1 = 1e-9   # à empreinte égale, les mêmes sommes donnent la même valeur, à l'arrondi près
DIFFS_PALIER_1 = 1e-6       # H7 : simple précision, valeurs d'au plus 0,12
DIFFS_PALIER_2 = 1e-3       # H7
SEUIL_STABILITE = 0.10
N_DOCS_ATTENDU = [466, 466]
NEXT_DOC_ATTENDU = 932
FONCTION = "_split_half_64"
CHAMPS_CONFIG = ("ajustement", "correctifs", "graines", "modele", "revision", "corpus")
COUCHES_MATRICES_R = 31
COUCHES_SERIES_R = 28
SERIES_R = ("npR_notre_R", "identite_notre_R")

# Pièces du 18 novembre (critère v3, § 1) : vérifiées par leur empreinte avant toute comparaison.
REFERENCES = {
    "ajustement-R": "129c43b020854fd395cb0e969dd7f8956844417684e1e3a1099fee5e7f16d2ab",
    "ajustement-S": "2dce646e32177941c02987a8ba3a0a67fd45d17f335e58ba9e321d3e0367c297",
    "export-R": "17304c936792e4b79e9a47d78abf5bb6966310c36b92f387b3303b23891eedf1",
    "manifeste": "b90c15140074e9d41a3cf93e8bcaf55f80cc025d07d2d46432239d1c6b6e3444",
}
CLES_SERIES_R = {str(i) for i in range(COUCHES_SERIES_R)}

_TOL = f"{TOLERANCE:.0e}".replace("1e-03", "10⁻³")
PALIER_1 = "palier 1 — même lentille, octets identiques"
PALIER_2 = f"palier 2 — différences entre moitiés concordantes à {_TOL} près ; octets différents ; matrices non comparables"
DIFFERENTE = "différente"
NON_COMPARABLE = "non comparable (traitée comme différente)"
SUSPENDU = "mention suspendue : anomalie (nœud de Lazar)"
_HEX64 = re.compile(r"^[0-9a-f]{64}$")


def empreinte_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def empreinte_fonction(source: str, nom: str = FONCTION) -> str | None:
    """SHA-256 du texte source exact de la fonction `nom` (None si absente)."""
    for n in ast.walk(ast.parse(source)):
        if isinstance(n, ast.FunctionDef) and n.name == nom:
            seg = ast.get_source_segment(source, n)
            return empreinte_octets(seg.encode("utf-8")) if seg is not None else None
    return None


def _fini(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def _series_ok(res: dict, champ: str):
    s = res.get(champ)
    if not isinstance(s, dict) or not s or not all(isinstance(v, list) and v for v in s.values()):
        return None
    return s


class _Pre:
    def __init__(self):
        self.liste = []

    def __call__(self, nom, tenu, detail=""):
        self.liste.append({"nom": nom, "tenu": bool(tenu), "detail": str(detail)})

    @property
    def tous(self):
        return all(p["tenu"] for p in self.liste)


def preconditions(c: dict) -> list[dict]:
    """`c` : ref, neuf (résultats), env_ref, env_neuf (enveloppes : run_id, manifeste_sha256), mref, mneuf (manifestes),
    sha_pieces (empreintes calculées des fichiers lus : ajustement de référence, manifeste de référence, manifeste neuf, export de
    référence pour R), fref, fneuf (empreintes de la fonction), lentille, eref, eneuf (exports, R)."""
    p = _Pre()
    ref, neuf = c["ref"], c["neuf"]
    L = c["lentille"]
    # provenance (D2)
    for cote, r in (("ref", ref), ("neuf", neuf)):
        sha, taille = r.get("sha256"), r.get("taille")
        p(f"empreinte du fichier d'ajustement bien formée ({cote})", isinstance(sha, str) and bool(_HEX64.match(sha)), sha)
        p(f"taille présente ({cote})", isinstance(taille, int) and not isinstance(taille, bool) and taille > 0, taille)
        p(f"`finies` vrai ({cote})", r.get("finies") is True, r.get("finies"))
    attendu = REFERENCES.get(f"ajustement-{L}")
    p("pièce d'ajustement de référence d'empreinte égale au critère", attendu is not None and c["sha_pieces"].get("ajustement_ref") == attendu,
      f"lu {c['sha_pieces'].get('ajustement_ref')} ; attendu {attendu}")
    p("manifeste de référence d'empreinte égale au critère", c["sha_pieces"].get("manifeste_ref") == REFERENCES["manifeste"],
      c["sha_pieces"].get("manifeste_ref"))
    p("manifeste neuf égal à celui que porte le résultat neuf",
      c["sha_pieces"].get("manifeste_neuf") is not None and c["sha_pieces"].get("manifeste_neuf") == c["env_neuf"].get("manifeste_sha256"),
      f"lu {c['sha_pieces'].get('manifeste_neuf')} ; porté {c['env_neuf'].get('manifeste_sha256')}")
    rid_r, rid_n = c["env_ref"].get("run_id"), c["env_neuf"].get("run_id")
    deb_r, deb_n = ref.get("debut_utc"), neuf.get("debut_utc")
    p("course neuve distincte (identifiant et heure de début)", bool(rid_r) and bool(rid_n) and rid_r != rid_n and bool(deb_r)
      and bool(deb_n) and deb_r != deb_n, f"{rid_r}/{deb_r} contre {rid_n}/{deb_n}")
    cr, cn = c["mref"].get("config") or {}, c["mneuf"].get("config") or {}
    for k in CHAMPS_CONFIG:
        p(f"configuration du manifeste : `{k}` égal", k in cr and k in cn and cr[k] == cn[k], f"ref {str(cr.get(k))[:60]} ; neuf {str(cn.get(k))[:60]}")
    # « même code » (H5)
    dr, dn = cr.get("drowse"), cn.get("drowse")
    p("H5 : `config.drowse` égal (version et empreinte de la roue), présent", bool(dr) and dr == dn, f"{dr} ; {dn}")
    pr_, pn_ = cr.get("precision"), cn.get("precision")
    p("H5 : `config.precision` égal, présent", bool(pr_) and pr_ == pn_, f"{pr_} ; {pn_}")
    vr = {k: v for k, v in (c["mref"].get("versions") or {}).items() if k != "plateforme"}
    vn = {k: v for k, v in (c["mneuf"].get("versions") or {}).items() if k != "plateforme"}
    p("H5 : `versions` égales hors `plateforme`, présentes", bool(vr) and vr == vn,
      sorted(k for k in set(vr) | set(vn) if vr.get(k) != vn.get(k)))
    er_, en_ = c.get("correctifs_ref"), c.get("correctifs_neuf")
    ok_corr = (isinstance(er_, dict) and isinstance(en_, dict) and bool(er_) and set(er_) == set(cr.get("correctifs") or [])
               and set(en_) == set(cn.get("correctifs") or []) and er_ == en_
               and all(isinstance(v, str) and _HEX64.match(v) for v in er_.values()))
    p("H5 : contenu des correctifs d'empreinte égale aux deux commits", ok_corr,
      "non lu" if not (isinstance(er_, dict) and isinstance(en_, dict)) else
      sorted(k for k in set(er_) | set(en_) if er_.get(k) != en_.get(k)))
    # forme et finitude (D4)
    for champ in ("diffs_float64", "diffs"):
        sr, sn = _series_ok(ref, champ), _series_ok(neuf, champ)
        forme = sr is not None and sn is not None and set(sr) == set(sn) and all(len(sr[t]) == len(sn[t]) for t in sr)
        p(f"mêmes cibles, mêmes comptes, séries non vides ({champ})", forme,
          f"ref {None if sr is None else {t: len(v) for t, v in sr.items()}} ; neuf {None if sn is None else {t: len(v) for t, v in sn.items()}}")
        nf = [] if (sr is None or sn is None) else [(cote, t, i) for cote, s in (("ref", sr), ("neuf", sn))
                                                      for t, v in s.items() for i, x in enumerate(v) if not _fini(x)]
        p(f"toutes les valeurs finies et numériques, des deux côtés ({champ})", sr is not None and sn is not None and not nf,
          "forme illisible" if sr is None or sn is None else f"{len(nf)} : {nf[:3]}")
    mr, mn = ref.get("meta"), neuf.get("meta")
    ok_meta = isinstance(mr, dict) and isinstance(mn, dict) and bool(mr) and mr == mn
    p("meta présent et égal champ par champ", ok_meta,
      "absent" if not (isinstance(mr, dict) and isinstance(mn, dict)) else sorted(k for k in set(mr) | set(mn) if mr.get(k, "<absent>") != mn.get(k, "<absent>")))
    for cote, r in (("ref", ref), ("neuf", neuf)):
        p(f"n_docs {N_DOCS_ATTENDU} ({cote})", r.get("n_docs") == N_DOCS_ATTENDU, r.get("n_docs"))
        p(f"next_doc {NEXT_DOC_ATTENDU} ({cote})", r.get("next_doc") == NEXT_DOC_ATTENDU, r.get("next_doc"))
    p("même nom de fichier d'ajustement, présent", bool(ref.get("fichier")) and ref.get("fichier") == neuf.get("fichier"),
      f"{ref.get('fichier')} ; {neuf.get('fichier')}")
    cvr, cvn = cr.get("commit_voisin"), cn.get("commit_voisin")
    p("même commit du code voisin, présent", bool(cvr) and cvr == cvn, f"{cvr} ; {cvn}")
    p(f"même texte de la fonction {FONCTION}, présent", bool(c["fref"]) and c["fref"] == c["fneuf"], f"{c['fref']} ; {c['fneuf']}")
    # pièces d'export de R (D3)
    if L == "R":
        p("export de référence d'empreinte égale au critère", c["sha_pieces"].get("export_ref") == REFERENCES["export-R"],
          c["sha_pieces"].get("export_ref"))
        for cote, e in (("ref", c.get("eref")), ("neuf", c.get("eneuf"))):
            ok = isinstance(e, dict)
            mm = (e or {}).get("matrices_moities") if ok else None
            ok_mm = isinstance(mm, dict) and len(mm) == COUCHES_MATRICES_R and all(
                isinstance(v, list) and len(v) == 2 and all(isinstance(h, str) and _HEX64.match(h) for h in v) for v in mm.values())
            p(f"export de R présent avec {COUCHES_MATRICES_R} couches de matrices ({cote})", ok_mm, None if mm is None else len(mm))
            val = (e or {}).get("valeurs") if ok else None
            for s in SERIES_R:
                serie = val.get(s) if isinstance(val, dict) else None
                ok_s = isinstance(serie, dict) and len(serie) == COUCHES_SERIES_R and all(_fini(v) for v in serie.values())
                p(f"série {s} présente, {COUCHES_SERIES_R} couches finies ({cote})", ok_s, None if not isinstance(serie, dict) else len(serie))
                p(f"série {s} : clés exactement 0 à 27 (H3, {cote})", isinstance(serie, dict) and set(serie) == CLES_SERIES_R,
                  None if not isinstance(serie, dict) else sorted(set(serie) ^ CLES_SERIES_R))
        # H2 : export neuf rattaché à la course neuve, différent de celui du 18
        ee = c.get("env_eneuf") or {}
        p("H2 : export neuf de la course neuve (identifiant de course)", bool(ee.get("run_id")) and ee.get("run_id") == c["env_neuf"].get("run_id"),
          f"{ee.get('run_id')} ; {c['env_neuf'].get('run_id')}")
        p("H2 : export neuf du même manifeste que le résultat neuf", bool(ee.get("manifeste_sha256"))
          and ee.get("manifeste_sha256") == c["env_neuf"].get("manifeste_sha256"), f"{ee.get('manifeste_sha256')}")
        p("H2 : export neuf différent de celui du 18", bool(c["sha_pieces"].get("export_neuf"))
          and c["sha_pieces"].get("export_neuf") != REFERENCES["export-R"], c["sha_pieces"].get("export_neuf"))
    return p.liste


def _table(ref, neuf, champ):
    return [{"cible": t, "rang": i, "ref": a, "neuf": b, "ecart": b - a}
            for t in sorted(ref[champ]) for i, (a, b) in enumerate(zip(ref[champ][t], neuf[champ][t]))]


def _max_abs(table) -> float:
    m = 0.0
    for r in table:
        if not math.isfinite(r["ecart"]):
            raise ValueError("écart non fini malgré les préalables")
        m = max(m, abs(r["ecart"]))
    return m


def _series_r(eref, eneuf) -> dict:
    out = {}
    for s in SERIES_R:
        a, b = eref["valeurs"][s], eneuf["valeurs"][s]
        couches = sorted(set(a) & set(b), key=int)
        ecarts = {k: b[k] - a[k] for k in couches}
        out[s] = {"couches": len(couches), "ecarts": ecarts, "ecart_max_abs": max(abs(v) for v in ecarts.values()),
                  "ref_min": min(a.values()), "ref_max": max(a.values())}
    return out


def comparer(c: dict, *, reprise: bool = False) -> dict:
    """Voir `preconditions` pour les clés de `c`. Rend la mention, les déclencheurs, les préalables et les tables."""
    ref, neuf, L = c["ref"], c["neuf"], c["lentille"]
    pre = preconditions(c)
    tous = all(x["tenu"] for x in pre)
    out = {"lentille": L, "tolerance": TOLERANCE, "reprise": bool(reprise), "preconditions": pre, "preconditions_toutes_tenues": tous,
           "pieces_lues": dict(c.get("sha_pieces") or {}), "commit_resultats": c.get("commit_resultats"),
           "sha256": {"ref": ref.get("sha256"), "neuf": neuf.get("sha256")}, "taille": {"ref": ref.get("taille"), "neuf": neuf.get("taille")}}
    declencheurs = []
    sha_ok = all(isinstance(r.get("sha256"), str) and _HEX64.match(r["sha256"]) for r in (ref, neuf))
    octets_egaux = sha_ok and ref["sha256"] == neuf["sha256"]
    # tables et séries de R, seulement si la forme le permet (jamais de maximum sur une valeur non finie)
    forme_ok = all(p["tenu"] for p in pre if p["nom"].startswith(("mêmes cibles", "toutes les valeurs finies")))
    if forme_ok:
        t64, t32 = _table(ref, neuf, "diffs_float64"), _table(ref, neuf, "diffs")
        m64 = _max_abs(t64)
        out.update({"ecart_max_abs_diffs_float64": m64,
                    "ecart_max_rel_diffs_float64": max((abs(r["ecart"]) / abs(r["ref"]) for r in t64 if r["ref"] != 0), default=None),
                    "ecart_max_abs_diffs": _max_abs(t32), "table_ecarts_diffs_float64": t64,
                    "changements_de_cote_du_seuil_0_10_sur_diffs": [
                        {k: r[k] for k in ("cible", "rang", "ref", "neuf")} for r in t32
                        if (r["ref"] <= SEUIL_STABILITE) != (r["neuf"] <= SEUIL_STABILITE)]})
    export_ok = L != "R" or all(p["tenu"] for p in pre if "export" in p["nom"] or p["nom"].startswith("série "))
    if L == "R" and export_ok:
        mm_r, mm_n = c["eref"]["matrices_moities"], c["eneuf"]["matrices_moities"]
        egales = sum(1 for k in mm_r if mm_n.get(k) == mm_r[k])
        out["matrices_moities_egales"] = {"couches_egales": egales, "couches_ref": len(mm_r)}
        out["series_export_R_sans_critere"] = _series_r(c["eref"], c["eneuf"])
    elif L == "S":
        out["series_export_R_sans_critere"] = "sans objet : aucune grandeur sensible à la position n'existe pour S dans les pièces du 18"
    if octets_egaux:
        declencheurs.append("(i) palier 1 obtenu")
        anomalies = []
        if not tous:
            anomalies.append("préalable manqué : " + "; ".join(p["nom"] for p in pre if not p["tenu"]))
        if ref.get("taille") != neuf.get("taille"):
            anomalies.append("taille différente")
        if forme_ok and out["ecart_max_abs_diffs_float64"] > COHERENCE_PALIER_1:
            anomalies.append(f"écart sur diffs_float64 de {out['ecart_max_abs_diffs_float64']:.3e} à empreinte égale")
        if L == "R" and export_ok and out["matrices_moities_egales"]["couches_egales"] != out["matrices_moities_egales"]["couches_ref"]:
            anomalies.append("empreinte du fichier égale mais empreinte de matrice des moitiés différente")
        if L == "R" and export_ok and any(v["ecart_max_abs"] != 0.0 for v in out["series_export_R_sans_critere"].values()):
            anomalies.append("H4 : une série de R change au premier palier")
        if forme_ok and out["ecart_max_abs_diffs"] > DIFFS_PALIER_1:
            anomalies.append(f"H7 : écart sur diffs de {out['ecart_max_abs_diffs']:.3e} au premier palier")
            declencheurs.append("(vii) écart sur diffs au-delà de 10⁻⁶ au premier palier")
        if anomalies:
            declencheurs.append("(v) " + " ; ".join(anomalies))
            out["mention"] = SUSPENDU
        else:
            out["mention"] = PALIER_1 + (" ; reprise sur sauvegarde notée" if reprise else "")
        out["declencheurs"] = declencheurs
        return out
    if not tous:
        declencheurs.append("(iv) non comparable")
        out.update({"mention": NON_COMPARABLE, "declencheurs": declencheurs})
        return out
    m64 = out["ecart_max_abs_diffs_float64"]
    if m64 == 0.0:
        declencheurs.append("(ii) écart maximal exactement nul avec des octets différents")
    if m64 <= TOLERANCE:
        out["mention"] = PALIER_2
        if out["ecart_max_abs_diffs"] > DIFFS_PALIER_2:
            declencheurs.append("(vii) écart sur diffs au-delà de 10⁻³ au deuxième palier")
            out["mention"] = SUSPENDU
        if L == "R":
            s = out["series_export_R_sans_critere"]
            if (out["matrices_moities_egales"]["couches_egales"] == out["matrices_moities_egales"]["couches_ref"]
                    or any(v["ecart_max_abs"] == 0.0 for v in s.values())):
                declencheurs.append("(vi) trop propre au deuxième palier : 31 matrices égales ou série inchangée à zéro exact")
                out["audit_requis"] = True
    else:
        declencheurs.append("(iii) lentille différente")
        out["mention"] = DIFFERENTE
    out["declencheurs"] = declencheurs
    return out


def empreintes_correctifs(depot: Path, commit: str, chemins) -> dict | None:
    """{chemin: SHA-256 du contenu au commit} lu par `git show` ; None si un chemin manque."""
    import subprocess
    out = {}
    for ch in chemins or []:
        r = subprocess.run(["git", "-C", str(depot), "show", f"{commit}:{ch}"], capture_output=True)
        if r.returncode != 0:
            return None
        out[ch] = empreinte_octets(r.stdout)
    return out


def charger(ref_ajustement: Path, neuf_ajustement: Path, ref_manifeste: Path, neuf_manifeste: Path, lanceur_ref: Path,
            lanceur_neuf: Path, ref_export: Path | None = None, neuf_export: Path | None = None, depot: Path | None = None,
            commit_resultats: str | None = None) -> dict:
    """Lit les fichiers et calcule leurs empreintes ; rend le dictionnaire `c` de `comparer`."""
    def lire(p):
        b = Path(p).read_bytes()
        return json.loads(b.decode("utf-8")), empreinte_octets(b)

    env_ref, sha_ar = lire(ref_ajustement)
    env_neuf, sha_an = lire(neuf_ajustement)
    mref, sha_mr = lire(ref_manifeste)
    mneuf, sha_mn = lire(neuf_manifeste)
    ref, neuf = env_ref.get("resultat", {}), env_neuf.get("resultat", {})
    lentille = (ref.get("meta") or {}).get("lens")
    c = {"ref": ref, "neuf": neuf, "env_ref": env_ref, "env_neuf": env_neuf, "mref": mref, "mneuf": mneuf, "lentille": lentille,
         "sha_pieces": {"ajustement_ref": sha_ar, "ajustement_neuf": sha_an, "manifeste_ref": sha_mr, "manifeste_neuf": sha_mn,
                        "lanceur_neuf": empreinte_octets(Path(lanceur_neuf).read_bytes())},
         "commit_resultats": commit_resultats, "env_eneuf": None, "correctifs_ref": None, "correctifs_neuf": None,
         "fref": empreinte_fonction(Path(lanceur_ref).read_text(encoding="utf-8")),
         "fneuf": empreinte_fonction(Path(lanceur_neuf).read_text(encoding="utf-8")), "eref": None, "eneuf": None}
    if ref_export is not None:
        e, sha_e = lire(ref_export)
        c["eref"], c["sha_pieces"]["export_ref"] = e.get("resultat"), sha_e
    if neuf_export is not None:
        e, sha_en = lire(neuf_export)
        c["eneuf"], c["env_eneuf"], c["sha_pieces"]["export_neuf"] = e.get("resultat"), e, sha_en
    if depot is not None:
        c["correctifs_ref"] = empreintes_correctifs(depot, mref.get("commit"), (mref.get("config") or {}).get("correctifs"))
        c["correctifs_neuf"] = empreintes_correctifs(depot, mneuf.get("commit"), (mneuf.get("config") or {}).get("correctifs"))
    return c


def main(argv=None):
    a = argparse.ArgumentParser(description="Critère d'identité du réajustement (v4 et suivants) : comparaison d'une lentille")
    for n in ("ref-ajustement", "neuf-ajustement", "ref-manifeste", "neuf-manifeste", "lanceur-ref", "lanceur-neuf", "sortie"):
        a.add_argument(f"--{n}", required=True, type=Path)
    a.add_argument("--ref-export", type=Path)
    a.add_argument("--neuf-export", type=Path)
    a.add_argument("--reprise", action="store_true", help="reprise sur sauvegarde lue au journal de la course")
    a.add_argument("--depot", type=Path, required=True, help="dépôt git où lire les correctifs aux deux commits (H5)")
    a.add_argument("--commit-resultats", required=True, help="commit de la branche de résultats poussée par la machine (H1)")
    x = a.parse_args(argv)
    if x.sortie.exists():
        sys.exit(f"{x.sortie} existe déjà : on n'écrase jamais (R12)")
    c = charger(x.ref_ajustement, x.neuf_ajustement, x.ref_manifeste, x.neuf_manifeste, x.lanceur_ref, x.lanceur_neuf,
                x.ref_export, x.neuf_export, x.depot, x.commit_resultats)
    r = comparer(c, reprise=x.reprise)
    r["ligne_de_commande"] = sys.argv if argv is None else ["comparer_reajustement_v3", *argv]
    x.sortie.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{r['lentille']} : {r['mention']} ; déclencheurs : {r['declencheurs']}")


if __name__ == "__main__":
    main()
