"""Juge des mondes de l'épreuve à vérité plantée du programme de lecture du barreau 5 — v1.

Distinct de la fabrique (`epreuve_verite_plantee_v1`) : il n'en importe rien, ne lit aucun arbre de lecture et ne refait
aucun calcul du programme de lecture. Il lit le fichier des vérités, après avoir vérifié son empreinte contre l'engagement,
et les rendus du programme, un par monde. Il applique les règles gelées de la colonne « règle gelée » du point 11 du texte
scellé `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f…`) : nombres de mondes,
seuils « au plus » et « au moins ». Il rend « passée » ou « manquée », règle par règle ; l'épreuve est « passée » si toutes
ses règles le sont (point 11 : « Une règle manquée : aucune ouverture »). Code neuf (R12), 20 novembre 2026, sans donnée.

Forme d'un rendu (une ligne JSON par monde, fichier `.jsonl`), fixée ici parce que l'interface lue ne dit pas la forme du
résultat du programme ; un traducteur, écrit par l'agent qui joue l'épreuve et qui voit ce résultat, la tire du résultat
sans rien recalculer :
  {"format": "b5f-rendu-monde-v1", "monde": "V3-0042", "refus": bool, "motif_refus": str | null,
   "issue": "S" | "D" | "C" | "E" | "N" | "NI" | null, "niveau": 99 | 95 | null,
   "motifs_D": ["E1" | "E2a" | "E2b", …]       — issue D : les épreuves qui ne sont pas « séparé » (le motif écrit) ;
   "mention_saboteur_sans_sur": bool              — issue N : la phrase porte « saboteur au-dessus de son jumeau sans que
                                                     le sur-saboteur le soit » ;
   "epreuves": {"M1" | "M3" | "E3" | "E2a" | "E2b" | "E1": {"decision": "separe" | "contraire" | "aucune", "K": int,
                "niveau": 99 | 95 | null, facultatifs : "w": int | null, "W_moins": nombre, "W_plus": nombre}} ;
   "familles_E2a": {famille: {"presente": bool, "motif": "produit_non_positif" | "facteur_hors" | "saboteur_absent" | null}} ;
   "familles_E2b": {famille: {"presente": bool, "c_un": bool, "motif": "poussee_non_positive" | "facteur_hors" | null,
                    facultatifs : "c_sur", "c_jumeau"}} ;
   "familles_absentes": {famille: motif écrit} ;
   facultatifs : "manipulation": {famille: [tâches jouées par tous, tâches retenues]},
                 "phrase_E": {"borne": nombre, "delta_app": nombre}}

Lectures déclarées :
- règle « au moins » : un monde compte si son issue est celle de la vérité, au niveau de la vérité (à dix familles, 99 :
  « sabotage » et non « sabotage, au niveau de 95 % », addendum 1, point 1, règle 3) ; règle « au plus » : toute issue du
  mot compte, à tout niveau ;
- « au seul motif « force non écartée » » (V3) : issue D dont le motif est une partie non vide de {E2a, E2b} ; « au seul
  motif « force non écartée (E2b) » » (V8) : motif {E2b} exactement, de même {E2a} (V9) et {E1} (V11) ; « au motif « force
  non écartée » » (V12) : motif qui contient E2a ou E2b ;
- un rendu manquant ou de forme invalide : toutes les règles de son groupe sont « manquée », motif écrit (aucun repli
  silencieux, R5) ; un rendu en double, ou d'un monde que la vérité ne connaît pas : refus du juge ;
- table des sommes de rangs contraires admises (« Seuil » et « Critères de lecture gelés », sous huit familles), recopiée
  du texte : à 99 %, w(10) = 3, w(9) = 1, w(8) = 0 ; à 95 %, w(7) = 2, w(6) = aucune.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

FORMAT_VERITES = "b5f-verites-epreuve-v1"
FORMAT_RENDU = "b5f-rendu-monde-v1"
FORMAT_VERDICT = "b5f-verdict-epreuve-v1"

# Nombres de mondes du point 11 (colonne « monde »).
NOMBRES_GELES = {"V0": 2000, "V1": 500, "V2": 500, "V3": 500, "V4": 500, "V5": 500, "V6": 500,
                 "V8": 500, "V9": 500, "V10": 200, "V11": 500, "V12": 500}
CAS_V7_GELES = {1: "table présente dans l'arbre de lecture", 2: "empreinte de la table différente de l'engagement",
                3: "scores postérieurs à l'ouverture", 4: "score manquant", 5: "famille incomplète",
                6: "sept familles seulement"}
W_GELE = {99: {10: 3, 9: 1, 8: 0}, 95: {7: 2, 6: None}}
EPREUVES = ("M1", "M3", "E3", "E2a", "E2b", "E1")
ISSUES = ("S", "D", "C", "E", "N", "NI")
DECISIONS = ("separe", "contraire", "aucune")
MOTIFS_E2A = ("produit_non_positif", "facteur_hors", "saboteur_absent")
MOTIFS_E2B = ("poussee_non_positive", "facteur_hors")
GROUPES_LECTURE = ("VC1", "VC2", "VC3")


class RefusJuge(Exception):
    """Refus du juge : empreinte des vérités différente de l'engagement, rendus corrompus."""


# ----------------------------------------------------------------------------------------------------------- lecture

def lire_verites(chemin, empreinte_engagee: str) -> dict:
    octets = Path(chemin).read_bytes()
    h = hashlib.sha256(octets).hexdigest()
    if h != empreinte_engagee:
        raise RefusJuge(f"empreinte des vérités {h} différente de l'engagement {empreinte_engagee}")
    doc = json.loads(octets)
    if doc.get("format") != FORMAT_VERITES:
        raise RefusJuge(f"format des vérités inattendu : {doc.get('format')}")
    return doc


def lire_rendus(chemin) -> dict:
    rendus = {}
    for i, ligne in enumerate(Path(chemin).read_text(encoding="utf-8").splitlines(), 1):
        if not ligne.strip():
            continue
        r = json.loads(ligne)
        m = r.get("monde") if isinstance(r, dict) else None
        if not isinstance(m, str):
            raise RefusJuge(f"ligne {i} : rendu sans monde")
        if m in rendus:
            raise RefusJuge(f"rendu en double : {m}")
        rendus[m] = r
    return rendus


def erreurs_rendu(r) -> list[str]:
    """Contrôle de forme d'un rendu ; ne juge rien."""
    if not isinstance(r, dict):
        return ["rendu non objet"]
    err = []
    if r.get("format") != FORMAT_RENDU:
        err.append("format")
    if not isinstance(r.get("refus"), bool):
        err.append("refus non booléen")
        return err
    if r["refus"]:
        return err
    if r.get("issue") not in ISSUES:
        err.append("issue")
    if r.get("niveau") not in (99, 95, None):
        err.append("niveau")
    if r.get("issue") in ("S", "D", "C") and r.get("niveau") is None:
        err.append("issue S, D ou C sans niveau")
    m = r.get("motifs_D", [])
    if not isinstance(m, list) or any(x not in ("E1", "E2a", "E2b") for x in m) or len(set(m)) != len(m):
        err.append("motifs_D")
    for e, d in (r.get("epreuves") or {}).items():
        if e not in EPREUVES or not isinstance(d, dict) or d.get("decision") not in DECISIONS \
                or not isinstance(d.get("K"), int) or d.get("niveau") not in (99, 95, None):
            err.append(f"epreuve {e}")
    for f, d in (r.get("familles_E2a") or {}).items():
        if not isinstance(d, dict) or not isinstance(d.get("presente"), bool) or d.get("motif") not in MOTIFS_E2A + (None,):
            err.append(f"familles_E2a {f}")
    for f, d in (r.get("familles_E2b") or {}).items():
        if not isinstance(d, dict) or not isinstance(d.get("presente"), bool) or not isinstance(d.get("c_un"), bool) \
                or d.get("motif") not in MOTIFS_E2B + (None,):
            err.append(f"familles_E2b {f}")
    return err


# ------------------------------------------------------------------------------------------------------ prédicats

def _ok(r) -> bool:
    return r is not None and r.get("refus") is False


def _decision(r, e):
    return ((r.get("epreuves") or {}).get(e) or {}).get("decision")


def _issue_au_niveau(r, a, issue) -> bool:
    if not (_ok(r) and r.get("issue") == issue):
        return False
    return issue not in ("S", "D", "C") or r.get("niveau") == a["niveau"]


def p_e3_separe(r, a):
    return _ok(r) and _decision(r, "E3") == "separe"


def p_e3_contraire(r, a):
    return _ok(r) and _decision(r, "E3") == "contraire"


def p_sabotage(r, a):
    return _ok(r) and r.get("issue") == "S"


def p_sabotage_attendu(r, a):
    return _issue_au_niveau(r, a, "S")


def p_non_etabli_mention(r, a):
    return _ok(r) and r.get("issue") == "N" and r.get("mention_saboteur_sans_sur") is True


def _motifs(r) -> set:
    return set(r.get("motifs_D") or [])


def p_d_seul_force(r, a):
    m = _motifs(r) if r else set()
    return _issue_au_niveau(r, a, "D") and bool(m) and m <= {"E2a", "E2b"}


def p_d_exact(ensemble):
    def p(r, a):
        return _issue_au_niveau(r, a, "D") and _motifs(r) == set(ensemble)
    return p


def p_d_force(r, a):
    return _issue_au_niveau(r, a, "D") and bool(_motifs(r) & {"E2a", "E2b"})


def p_contraire(r, a):
    return _issue_au_niveau(r, a, "C")


def p_empreinte(r, a):
    return _ok(r) and r.get("issue") == "E"


def p_non_interpretable(r, a):
    return _ok(r) and r.get("issue") == "NI"


# (groupe, règle gelée, sens, seuil, prédicat)
REGLES = (
    ("V0", "épreuve E3 « séparé » dans 20 mondes au plus", "au plus", 20, p_e3_separe),
    ("V0", "épreuve E3 « contraire » dans 20 mondes au plus", "au plus", 20, p_e3_contraire),
    ("V0", "« sabotage » dans 20 mondes au plus", "au plus", 20, p_sabotage),
    ("V1", "« sabotage » dans 480 mondes au moins", "au moins", 480, p_sabotage_attendu),
    ("V2", "« sabotage » dans 10 au plus", "au plus", 10, p_sabotage),
    ("V2", "issue « non établi », avec la mention « saboteur au-dessus de son jumeau sans que le sur-saboteur le soit », "
           "dans 480 au moins", "au moins", 480, p_non_etabli_mention),
    ("V3", "« différence établie » au seul motif « force non écartée » dans 480 au moins", "au moins", 480, p_d_seul_force),
    ("V3", "« sabotage » dans 10 au plus", "au plus", 10, p_sabotage),
    ("V4", "« contraire » dans 480 au moins", "au moins", 480, p_contraire),
    ("V4", "« sabotage » dans aucun", "au plus", 0, p_sabotage),
    ("V5", "« empreinte » dans 480 au moins", "au moins", 480, p_empreinte),
    ("V6", "« non interprétable » dans 490 au moins", "au moins", 490, p_non_interpretable),
    ("V8", "« différence établie » au seul motif « force non écartée (E2b) » dans 480 au moins", "au moins", 480,
     p_d_exact(("E2b",))),
    ("V8", "« sabotage » dans 10 au plus", "au plus", 10, p_sabotage),
    ("V9", "« différence établie » au seul motif « force non écartée (E2a) » dans 480 au moins", "au moins", 480,
     p_d_exact(("E2a",))),
    ("V9", "« sabotage » dans 10 au plus", "au plus", 10, p_sabotage),
    ("V11", "« différence établie » au seul motif « saboteur non établi » dans 480 au moins", "au moins", 480,
     p_d_exact(("E1",))),
    ("V11", "« sabotage » dans 10 au plus", "au plus", 10, p_sabotage),
    ("V12", "« différence établie » au motif « force non écartée » dans 480 au moins", "au moins", 480, p_d_force),
    ("V12", "« sabotage » dans 10 au plus", "au plus", 10, p_sabotage),
)


def _w(niveau, k):
    return W_GELE.get(niveau, {}).get(k)


def _seuil_coherent(d) -> bool:
    """Une épreuve rendue suit la table du seuil à son nombre de familles : w donné égal à la table ; décision égale à
    celle que la table donne aux sommes de rangs, quand elles sont rendues."""
    k, niv = d.get("K"), d.get("niveau")
    if niv != (99 if k >= 8 else (95 if k >= 6 else None)):
        return False
    w = _w(niv, k)
    if "w" in d and d["w"] != w:
        return False
    if "W_moins" in d and "W_plus" in d:
        attendue = "aucune"
        if w is not None and d["W_moins"] <= w:
            attendue = "separe"
        elif w is not None and d["W_plus"] <= w:
            attendue = "contraire"
        if d.get("decision") != attendue:
            return False
    elif niv is None and d.get("decision") != "aucune":
        return False
    return True


def _epreuves_conformes(r, a, attendus_k=None) -> bool:
    """Chaque épreuve de la vérité est rendue avec son nombre de familles et un seuil conforme à la table."""
    ep = r.get("epreuves") or {}
    for e, d in a["epreuves"].items():
        if e not in ep:
            return False
        k = attendus_k[e] if attendus_k else d["K"]
        if ep[e].get("K") != k or not _seuil_coherent(ep[e]):
            return False
    return True


def _e2_conformes(r, a) -> bool:
    """Familles présentes de E2a et de E2b, facteur c = 1 et motifs, exactement comme plantés."""
    ra, rb = r.get("familles_E2a") or {}, r.get("familles_E2b") or {}
    for f in a["familles_E3"]:
        va = {"presente": f not in a["E2a_absentes"], "motif": a["E2a_absentes"].get(f)}
        vb = {"presente": f not in a["E2b_absentes"], "c_un": f in a["E2b_c_un"],
              "motif": a["E2b_absentes"].get(f, "poussee_non_positive" if f in a["E2b_c_un"] else None)}
        if f not in ra or f not in rb:
            return False
        if {"presente": ra[f].get("presente"), "motif": ra[f].get("motif")} != va:
            return False
        if {"presente": rb[f].get("presente"), "c_un": rb[f].get("c_un"), "motif": rb[f].get("motif")} != vb:
            return False
        if vb["c_un"] and any(k in rb[f] and rb[f][k] != 1.0 for k in ("c_sur", "c_jumeau")):
            return False
    return set(ra) == set(a["familles_E3"]) and set(rb) == set(a["familles_E3"])


def v10_presences(r, a):
    return _ok(r) and _e2_conformes(r, a)


def v10_seuil(r, a):
    return _ok(r) and _epreuves_conformes(r, a)


def v10_noeud6(r, a):
    if not _ok(r):
        return False
    d = (r.get("epreuves") or {}).get("E2a") or {}
    if d.get("K") != 7 or d.get("niveau") != 95 or ("w" in d and d["w"] != 2):
        return False
    issue = r.get("issue")
    if issue == "S" and r.get("niveau") != 95:
        return False
    if issue in ("D", "C") and r.get("niveau") != 99:   # addendum, point 1 : E2a ne fonde ni D ni C
        return False
    return True


def v7_refus(r, a):
    return r is not None and r.get("refus") is True


def v7_cinquieme(r, a):
    if not _ok(r) or not _epreuves_conformes(r, a):
        return False
    absentes = r.get("familles_absentes") or {}
    for f in a["familles_absentes"]:
        if not (isinstance(absentes.get(f), str) and absentes[f]):
            return False
    ra = r.get("familles_E2a") or {}
    for f, motif in a["E2a_absentes"].items():
        if (ra.get(f) or {}).get("motif") != motif or (ra.get(f) or {}).get("presente") is not False:
            return False
    return True


def v7_sixieme(r, a):
    if not _ok(r) or not _epreuves_conformes(r, a):
        return False
    ep = r.get("epreuves") or {}
    if any(ep[e].get("K") != 7 or ep[e].get("niveau") != 95 for e in a["epreuves"]):
        return False
    return r.get("issue") not in ("S", "D", "C") or r.get("niveau") == 95


# --------------------------------------------------------------------------------------------------------- jugement

def _regle(groupe, texte, sens, seuil, compte, mondes, motif=None):
    if motif is not None:
        issue = "manquee"
    elif sens == "au plus":
        issue = "passee" if compte <= seuil else "manquee"
    elif sens == "au moins":
        issue = "passee" if compte >= seuil else "manquee"
    else:   # « dans tous les mondes »
        issue = "passee" if compte == mondes else "manquee"
    d = {"monde": groupe, "regle": texte, "sens": sens, "seuil": seuil, "compte": compte, "mondes": mondes,
         "issue": issue}
    if motif is not None:
        d["motif"] = motif
    return d


def juger(chemin_verites, empreinte_engagee: str, rendus: dict) -> dict:
    doc = lire_verites(chemin_verites, empreinte_engagee)
    verites = {m["monde"]: m for m in doc["mondes"]}
    inconnus = sorted(set(rendus) - set(verites))
    if inconnus:
        raise RefusJuge(f"rendus de mondes inconnus : {inconnus[:5]}")
    par_groupe = {}
    for m, v in verites.items():
        par_groupe.setdefault(v["groupe"], []).append(m)
    defauts = {}
    for g, ms in par_groupe.items():
        manq = [m for m in ms if m not in rendus]
        inval = [m for m in ms if m in rendus and erreurs_rendu(rendus[m])]
        if manq or inval:
            defauts[g] = f"rendus manquants : {len(manq)} ; rendus invalides : {len(inval)}"

    regles = []
    for g, n in NOMBRES_GELES.items():
        if len(par_groupe.get(g, [])) != n:
            defauts.setdefault(g, f"{len(par_groupe.get(g, []))} mondes dans la vérité, {n} au point 11")
    for g, texte, sens, seuil, pred in REGLES:
        ms = par_groupe.get(g, [])
        compte = sum(1 for m in ms if m in rendus and not erreurs_rendu(rendus[m])
                     and pred(rendus[m], verites[m]["attendu"]))
        regles.append(_regle(g, texte, sens, seuil, compte, len(ms), defauts.get(g)))

    # V10 : dans tous les mondes
    ms = par_groupe.get("V10", [])
    for texte, pred in (("familles présentes de E2a et de E2b, facteur c = 1 et motifs écrits exactement comme plantés",
                         v10_presences),
                        ("seuil pris au nombre de familles présentes de chaque demi-épreuve", v10_seuil),
                        ("règle du nœud 6 appliquée à E2a (sept familles présentes)", v10_noeud6)):
        compte = sum(1 for m in ms if m in rendus and not erreurs_rendu(rendus[m])
                     and pred(rendus[m], verites[m]["attendu"]))
        regles.append(_regle("V10", texte, "dans tous les mondes", len(ms), compte, len(ms), defauts.get("V10")))

    # V7 : cas par cas
    ms = par_groupe.get("V7", [])
    numero = {code: n for code, n in doc.get("cas_V7", [])}
    par_cas = {}
    for m in ms:
        par_cas.setdefault(numero.get(verites[m]["cas"]), []).append(m)
    manque_cas = [n for n in CAS_V7_GELES if n not in par_cas]
    motif_v7 = defauts.get("V7") or (f"cas absents de la vérité : {manque_cas}" if manque_cas else None)
    for texte, cas, pred in (("refus dans les quatre premiers cas", (1, 2, 3, 4), v7_refus),
                             ("seuil recalculé et motif écrit dans le cinquième", (5,), v7_cinquieme),
                             ("règle du nœud 6 dans le dernier", (6,), v7_sixieme)):
        mc = [m for c in cas for m in par_cas.get(c, [])]
        attendu_refus = all(verites[m]["attendu"]["refus"] for m in mc) if cas == (1, 2, 3, 4) else \
            not any(verites[m]["attendu"]["refus"] for m in mc)
        compte = sum(1 for m in mc if m in rendus and not erreurs_rendu(rendus[m])
                     and pred(rendus[m], verites[m]["attendu"]))
        motif = motif_v7 or (None if attendu_refus else "vérité incohérente avec le cas")
        regles.append(_regle("V7", texte, "dans tous les mondes", len(mc), compte, len(mc), motif))

    verdict = "passee" if all(r["issue"] == "passee" for r in regles) else "manquee"
    return {"format": FORMAT_VERDICT, "verites_sha256": empreinte_engagee, "entropie": doc.get("entropie"),
            "epreuve": verdict, "regles": regles, "descriptifs": _descriptifs(par_groupe, verites, rendus)}


def _descriptifs(par_groupe, verites, rendus) -> dict:
    """Ce qui sert la lecture sans être une règle gelée : rapporté, sans effet sur l'épreuve."""
    out = {}
    v0 = par_groupe.get("V0", [])
    out["V0"] = {"E3_separe": sum(1 for m in v0 if m in rendus and p_e3_separe(rendus[m], None)),
                 "E3_contraire": sum(1 for m in v0 if m in rendus and p_e3_contraire(rendus[m], None)),
                 "attendu_par_sens": 9.8}
    for g in GROUPES_LECTURE:
        ms = par_groupe.get(g, [])
        issues, accord, comptes = {}, {}, {"egaux": 0, "differents": 0, "non_rendus": 0}
        for m in ms:
            r = rendus.get(m)
            cle = "refus" if (r and r.get("refus")) else (f"{r.get('issue')}-{r.get('niveau')}" if r else "manquant")
            issues[cle] = issues.get(cle, 0) + 1
            for nom, alt in verites[m]["attendu"].get("alternatives", {}).items():
                ok = r is not None and _ok(r) and r.get("issue") == alt["issue"] and r.get("niveau") == alt.get("niveau")
                accord[nom] = accord.get(nom, 0) + int(ok)
            a = verites[m]["attendu"]
            if r is None or "manipulation" not in r:
                comptes["non_rendus"] += 1
            else:
                attendu = {f: a["manipulation"].get(f, [a["taches"], a["taches"]]) for f in a["familles_E3"]}
                rendu = {f: list(v) for f, v in r["manipulation"].items() if f in attendu}
                comptes["egaux" if rendu == attendu else "differents"] += 1
        out[g] = {"issues_rendues": issues, "accord_par_lecture": accord, "comptes_de_taches": comptes, "mondes": len(ms)}
    v5 = par_groupe.get("V5", [])
    ok = tot = 0
    for m in v5:
        r = rendus.get(m)
        if r and r.get("issue") == "E" and isinstance(r.get("phrase_E"), dict):
            tot += 1
            b, d = r["phrase_E"].get("borne"), r["phrase_E"].get("delta_app")
            ok += int(isinstance(b, (int, float)) and isinstance(d, (int, float)) and abs(b - 0.5 * d) <= 1e-9 * max(1.0, abs(d)))
    out["addendum_point3_V5"] = {"phrases_E_rendues": tot, "borne_egale_a_la_moitie_de_delta_app": ok}
    out["V7_motifs_de_refus"] = {m: (rendus.get(m) or {}).get("motif_refus") for m in par_groupe.get("V7", [])}
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="juge_verite_plantee_v1", description=__doc__.split("\n")[0])
    ap.add_argument("--verites", required=True)
    ap.add_argument("--empreinte", required=True, help="empreinte engagée du fichier des vérités")
    ap.add_argument("--rendus", required=True, help="rendus du programme, une ligne JSON par monde")
    ap.add_argument("--sortie", required=True, help="verdict (JSON, fichier neuf)")
    a = ap.parse_args(argv)
    v = juger(a.verites, a.empreinte, lire_rendus(a.rendus))
    octets = json.dumps(v, ensure_ascii=False, indent=1).encode("utf-8")
    with open(a.sortie, "xb") as fh:
        fh.write(octets)
    print(json.dumps({"epreuve": v["epreuve"], "manquees": [r["regle"] for r in v["regles"] if r["issue"] != "passee"],
                      "verdict_sha256": hashlib.sha256(octets).hexdigest()}, ensure_ascii=False))
    return 0 if v["epreuve"] == "passee" else 1


if __name__ == "__main__":
    sys.exit(main())
