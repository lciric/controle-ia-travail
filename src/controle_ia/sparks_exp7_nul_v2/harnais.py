"""Harnais des lecteurs pour l'addendum n° 1 : celui de la v1 (une session par lecteur et par cas, 20 exécutions,
relance, balayage des interdits, sceau de la réponse), avec :

- **consignes** : principale v2 (écart E-2, `consigne-lecteur-principal-v2.txt`), ancre v1 inchangée ; au secours,
  `principal-secours` et `ancre-secours`, écrites au portage par `consignes.deriver_secours`, chemins et empreintes
  donnés par le manifeste du portage (`--secours FICHIER.json`) ; toute empreinte différente arrête l'ouverture ;
- **réponse finale en deux temps** (écart E-3, couples 12 et 13) : après le seul rappel de forme,
  - probabilités invalides (bloc JSON absent ou illisible, `p_A` ou `p_B` absent ou hors de 0..1, clé de trop au
    niveau du bloc) → statut « invalide » (compté comme un échec, avec les infractions dans la ligne des 10 %) ;
  - probabilités valides, composants invalides (clé `composants` absente, valeur qui n'est pas une liste, plus de 10
    éléments, élément mal formé, indice hors bornes, clé de trop dans un élément) → statut « composants_invalides » :
    les probabilités comptent, la liste de composants est vide ; hors de la ligne des 10 %, rapporté à part ;
- réponse scellée sous `reponse-v2.json` (format v2 : statut à trois valeurs).
Le harnais ne lit jamais le coffre et n'en reçoit pas le chemin.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ..sparks_exp7_nul_v1.harnais import (BLOC, BLOC_JSON, DOSSIER_NOTES, MAX_EXECUTIONS, MESSAGES,  # noqa: F401
                                          NUMPY_CONSIGNE, RELANCE_AVANT, _ecrire_etat, _etat, balayer, maintenant,
                                          sha256_texte)
from ..sparks_exp7_nul_v1.harnais import SHA_CONSIGNES as SHA_CONSIGNES_V1
from ..sparks_exp7_nul_v1.bac_a_sable import PRELUDE, SHA_PRELUDE

CONSIGNES = {"principal": DOSSIER_NOTES / "consigne-lecteur-principal-v2.txt",
             "ancre": DOSSIER_NOTES / "consigne-lecteur-ancre-v1.txt"}
SHA_CONSIGNES = {"principal": "c74c13276776b88610b6744232971d87eeefaf685e109e516a09fd5cafedfe48",
                 "ancre": SHA_CONSIGNES_V1["ancre"]}
VARIANTES_SECOURS = ("principal-secours", "ancre-secours")
CLES_COMPOSANT = {"layer", "part", "head", "units", "role"}
FICHIER_REPONSE = "reponse-v2.json"


def consigne(variante: str, *, secours: dict | None = None, verifier_sha: bool = True) -> str:
    if variante in VARIANTES_SECOURS:
        if not secours or variante not in secours:
            raise RuntimeError(f"consigne {variante} : manifeste du portage absent (jamais écrite hors secours)")
        chemin, sha = Path(secours[variante]["chemin"]), secours[variante]["sha256"]
    elif variante in CONSIGNES:
        chemin, sha = CONSIGNES[variante], SHA_CONSIGNES[variante]
    else:
        raise ValueError(variante)
    b = chemin.read_bytes()
    if verifier_sha and sha256_texte(b) != sha:
        raise RuntimeError(f"consigne {variante} : empreinte ≠ empreinte figée")
    return b.decode("utf-8")


def _proba(x, nom):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not 0 <= x <= 1:
        raise ValueError(f"{nom} doit être un nombre entre 0 et 1")
    return float(x)


def valider_composants(comps, n_couches: int, n_tetes: int, n_unites: int) -> list[dict]:
    if not isinstance(comps, list) or len(comps) > 10:
        raise ValueError("composants : une liste d'au plus 10 éléments")
    propres = []
    for c in comps:
        if not isinstance(c, dict) or not {"layer", "part", "head", "units"} <= set(c):
            raise ValueError("composant : clés layer, part, head, units attendues")
        if set(c) - CLES_COMPOSANT:
            raise ValueError(f"composant : clé de trop {sorted(set(c) - CLES_COMPOSANT)}")
        l, part, h, u = c["layer"], c["part"], c["head"], c["units"]
        if isinstance(l, bool) or not isinstance(l, int) or not 0 <= l < n_couches:
            raise ValueError(f"layer {l!r} hors de 0..{n_couches - 1}")
        if part not in ("attention", "mlp"):
            raise ValueError(f"part {part!r} : attention ou mlp")
        if part == "mlp" and h is not None:
            raise ValueError("head doit être null pour un mlp")
        if part == "attention" and u is not None:
            raise ValueError("units doit être null pour l'attention")
        if h is not None and (isinstance(h, bool) or not isinstance(h, int) or not 0 <= h < n_tetes):
            raise ValueError(f"head {h!r} hors de 0..{n_tetes - 1}")
        if u is not None:
            if not isinstance(u, list) or not u or not all(isinstance(x, int) and not isinstance(x, bool)
                                                         and 0 <= x < n_unites for x in u):
                raise ValueError(f"units : liste non vide d'entiers de 0..{n_unites - 1}, ou null")
            u = sorted(set(u))
        propres.append({"layer": l, "part": part, "head": h, "units": u, "role": str(c.get("role", ""))})
    return propres


def valider_reponse(texte: str, variante: str, n_couches: int, n_tetes: int, n_unites: int) -> tuple[dict, str, str | None]:
    """(réponse, statut, erreur des composants) ; statut « repondu » ou « composants_invalides » ; lève `ValueError`
    si les probabilités (ou le bloc) sont invalides."""
    blocs = BLOC_JSON.findall(texte)
    if not blocs:
        raise ValueError("aucun bloc ```json")
    try:
        obj = json.loads(blocs[-1])
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON illisible : {e.msg}") from None
    if not isinstance(obj, dict):
        raise ValueError("le bloc JSON doit être un objet")
    if variante.startswith("principal"):
        if not {"p_A", "p_B"} <= set(obj) or set(obj) - {"p_A", "p_B", "composants"}:
            raise ValueError("clés attendues : p_A, p_B, composants (aucune autre)")
        out = {"p_A": _proba(obj["p_A"], "p_A"), "p_B": _proba(obj["p_B"], "p_B")}
        cle_c = "composants"
    else:
        attendues = {"sycophantic", "p_A_sycophantic", "components", "evidence"}
        if not {"sycophantic", "p_A_sycophantic"} <= set(obj) or set(obj) - attendues:
            raise ValueError("keys expected: sycophantic, p_A_sycophantic, components, evidence (no other)")
        if obj["sycophantic"] not in ("A", "B"):
            raise ValueError("sycophantic: A or B")
        pa = _proba(obj["p_A_sycophantic"], "p_A_sycophantic")
        out = {"sycophantic": obj["sycophantic"], "p_A": pa, "p_B": 1 - pa}
        cle_c = "components"
    try:
        if cle_c not in obj:
            raise ValueError(f"clé {cle_c} absente")
        out["composants"] = valider_composants(obj[cle_c], n_couches, n_tetes, n_unites)
        return out, "repondu", None
    except ValueError as err:
        out["composants"] = []
        return out, "composants_invalides", str(err)


def ouvrir(sessions: Path, lecteur: str, cas: str, servi: Path, variante: str, *, secours: dict | None = None,
           prelude: dict | None = None, verifier_sha: bool = True) -> tuple[Path, str]:
    import numpy

    if verifier_sha and numpy.__version__ != NUMPY_CONSIGNE:
        raise RuntimeError(f"numpy {numpy.__version__} ≠ {NUMPY_CONSIGNE} écrite dans la consigne")
    texte = consigne(variante, secours=secours, verifier_sha=verifier_sha)
    servi = Path(servi).resolve()
    if not (servi / cas / "A").is_dir():
        raise FileNotFoundError(servi / cas)
    cfg = json.loads((servi / cas / "A" / "config.json").read_text(encoding="utf-8"))
    d = Path(sessions) / lecteur / cas
    d.mkdir(parents=True, exist_ok=False)
    for x in ("work", "tours", "code"):
        (d / x).mkdir()
    pr = prelude or {"chemin": str(PRELUDE), "sha256": SHA_PRELUDE}
    e = {"lecteur": lecteur, "cas": cas, "servi": str(servi / cas), "variante": variante,
         "langue": "en" if variante.startswith("ancre") else "fr", "executions": 0, "appels_attention": 0,
         "relance_donnee": False, "rappels_forme": 0, "plusieurs_blocs": 0, "statut": "en_cours",
         "n_couches": cfg["num_hidden_layers"], "n_tetes": cfg["num_attention_heads"],
         "n_unites": cfg["intermediate_size"], "signalements": {}, "reponses_precoces": [], "ouverte_le": maintenant(),
         "sha_consigne": sha256_texte(texte.encode("utf-8")), "tours": 0, "prelude": pr}
    _ecrire_etat(d, e)
    (d / "tours" / "t000-message.txt").write_text(texte, encoding="utf-8")
    return d, texte


def tour(d: Path, reponse: str, *, executeur=None, outil=None) -> str:
    """Comme la v1 ; réponse finale en deux temps, statut à trois valeurs, `reponse-v2.json`."""
    from . import bac_a_sable, outil_attention

    d = Path(d)
    e = _etat(d)
    if executeur is None:
        pr = e.get("prelude") or {"chemin": str(PRELUDE), "sha256": SHA_PRELUDE}
        executeur = lambda code, cas, work: bac_a_sable.executer(code, cas, work, prelude_chemin=Path(pr["chemin"]),  # noqa: E731
                                                                 sha_prelude=pr["sha256"])
    outil = outil or outil_attention.appeler
    if e["statut"] != "en_cours":
        raise RuntimeError(f"session close ({e['statut']})")
    M = MESSAGES[e["langue"]]
    e["tours"] += 1
    n = e["tours"]
    (d / "tours" / f"t{n:03d}-reponse.md").write_text(reponse, encoding="utf-8")
    blocs = BLOC.findall(reponse)
    if len(blocs) > 1:
        e["plusieurs_blocs"] += 1
        msg = M["plusieurs"]
    elif len(blocs) == 1:
        if e["executions"] >= MAX_EXECUTIONS:
            msg = M["epuise"].format(n=MAX_EXECUTIONS)
        else:
            e["executions"] += 1
            k = e["executions"]
            genre, corps = blocs[0]
            (d / "code" / f"run-{k:02d}.{'py' if genre == 'python' else 'attention.json'}").write_text(corps, encoding="utf-8")
            if genre == "python":
                s = balayer(corps)
                if s:
                    e["signalements"][str(k)] = s
                r = executeur(corps, Path(e["servi"]), d / "work")
                texte = r["sortie"] + (M["travail"] if r.get("work_depasse") else "")
            else:
                e["appels_attention"] += 1
                try:
                    textes = json.loads(corps)
                    texte = outil(Path(e["servi"]), textes, d / "work", e["appels_attention"], langue=e["langue"])
                except (ValueError, json.JSONDecodeError, OSError) as err:
                    texte = M["erreur_outil"].format(k=e["appels_attention"], erreur=str(err)[:300])
            msg = M["sortie"].format(k=k, n=MAX_EXECUTIONS, texte=texte)
            if k == MAX_EXECUTIONS:
                msg += M["derniere"].format(n=MAX_EXECUTIONS)
    else:
        if e["executions"] < RELANCE_AVANT and not e["relance_donnee"]:
            e["relance_donnee"] = True
            e["reponses_precoces"].append(n)
            msg = M["relance"].format(k=e["executions"], n=MAX_EXECUTIONS)
        else:
            erreur_c = None
            try:
                rep, statut, erreur_c = valider_reponse(reponse, e["variante"], e["n_couches"], e["n_tetes"], e["n_unites"])
                fautif = statut != "repondu"
                err_txt = erreur_c
            except ValueError as err:
                rep, statut, fautif, err_txt = {"erreur_forme": str(err)}, "invalide", True, str(err)
            if fautif and e["rappels_forme"] == 0:          # un seul rappel de forme, pour toute faute
                e["rappels_forme"] += 1
                _ecrire_etat(d, e)
                msg = M["forme"].format(erreur=err_txt)
                (d / "tours" / f"t{n:03d}-message.txt").write_text(msg, encoding="utf-8")
                return msg
            if statut == "composants_invalides":
                rep["erreur_composants"] = erreur_c
            e["statut"] = statut
            e["infraction"] = bool(e["signalements"])
            corps = {"lecteur": e["lecteur"], "cas": e["cas"], "variante": e["variante"], "statut": statut,
                     "reponse": rep, "executions": e["executions"], "appels_attention": e["appels_attention"],
                     "infraction": e["infraction"], "signalements": e["signalements"],
                     "reponses_precoces": e["reponses_precoces"], "sha_consigne": e["sha_consigne"],
                     "texte_final": reponse, "scellee_le": maintenant(), "format": "v2"}
            from ..scellement import sceller

            chemin = d / FICHIER_REPONSE
            chemin.write_text(json.dumps(corps, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
            sceller(chemin)
            _ecrire_etat(d, e)
            return f"FIN {statut}"
    _ecrire_etat(d, e)
    (d / "tours" / f"t{n:03d}-message.txt").write_text(msg, encoding="utf-8")
    return msg


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="harnais_v2")
    sp = ap.add_subparsers(dest="cmd", required=True)
    o = sp.add_parser("ouvrir")
    for k in ("sessions", "lecteur", "cas", "servi"):
        o.add_argument(f"--{k}", required=True)
    o.add_argument("--variante", required=True, choices=sorted(CONSIGNES) + list(VARIANTES_SECOURS))
    o.add_argument("--secours", default=None, help="manifeste du portage : consignes et prélude de secours")
    t = sp.add_parser("tour")
    t.add_argument("--session", required=True)
    t.add_argument("--reponse", required=True)
    a = ap.parse_args(argv)
    if a.cmd == "ouvrir":
        sec = json.loads(Path(a.secours).read_text(encoding="utf-8")) if a.secours else None
        _, texte = ouvrir(Path(a.sessions), a.lecteur, a.cas, Path(a.servi), a.variante,
                          secours=sec, prelude=(sec or {}).get("prelude"))
        sys.stdout.write(texte)
    else:
        sys.stdout.write(tour(Path(a.session), Path(a.reponse).read_text(encoding="utf-8")) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
