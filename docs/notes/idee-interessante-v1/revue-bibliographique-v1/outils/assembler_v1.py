"""Assemblage de la revue bibliographique v1 (classe B, outil de travail).

1. Lit les fiches des sous-agents (`<scr>/agents/*.json`, liste d'objets).
2. Fusionne les doublons par identifiant normalisé.
3. Revérifie chaque identifiant par `biblio_v1.resoudre` (journal central), compare
   titre (similarité) et année (écart toléré d'un an : prépublication contre parution).
4. Écrit : tables par hypothèse, liste « nouveau depuis 2024 », table de vérification,
   fiches fusionnées (JSON).

Usage : BIBLIO_JOURNAL=<journal central> python -I assembler_v1.py <scr> <dossier_sortie>
"""
from __future__ import annotations

import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import biblio_v1  # noqa: E402

CIBLES = ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10",
          "M4a", "M4b", "M5", "M6a", "M6b", "M6c", "M6d", "M6e", "M6f"]
NOMS = {
    "H1": "mariage éloigné (distance de surface, proximité cachée)",
    "H2": "cascades et transferts",
    "H3": "serrure et clé (alignement des réseaux, invariant conservé)",
    "H4": "ni trop près ni trop loin",
    "H5": "champ d'interaction et air du temps",
    "H6": "connexion et distinction (fausses identités)",
    "H7": "profondeur de l'idée fille (nœuds, unification)",
    "H8": "émergence, transition de phase, percolation",
    "H9": "structure cachée du langage",
    "H10": "signal de surprise lisible dans un agent",
    "M4a": "le champ croît quand la distance diminue, mais exige des collisions actives",
    "M4b": "le champ croît à l'approche de la bonne invariance",
    "M5": "le champ combine invariants et probabilités de rencontre",
    "M6a": "le champ comme direction de comparabilité ouverte par un cadre nouveau",
    "M6b": "invariant conservé sous l'application d'alignement (systématicité) ; mesurer les invariances par rapprochement des structures",
    "M6c": "homomorphisme de graphes typés ou équivariance discrète comme équivalent de Noether",
    "M6d": "modéliser un substrat commun (horloges d'Einstein et de Poincaré)",
    "M6e": "trous structuraux entre réseaux denses",
    "M6f": "le langage miroiterait la structure du monde",
}


def norm_id(i: str) -> str:
    i = (i or "").strip()
    i = re.sub(r"^https?://(dx\.)?doi\.org/", "doi:", i, flags=re.I)
    i = re.sub(r"^https?://arxiv\.org/(abs|pdf)/", "arxiv:", i, flags=re.I)
    g, _, v = i.partition(":")
    g = g.lower()
    if g == "doi":
        v = v.lower()
        m = re.match(r"10\.48550/arxiv\.(.+)", v)
        if m:
            return "arxiv:" + re.sub(r"v\d+$", "", m.group(1))
        return "doi:" + v
    if g == "arxiv":
        return "arxiv:" + re.sub(r"v\d+$", "", v.lower())
    return i


def norm_titre(t: str) -> str:
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", t).split())


def sim(a: str, b: str) -> float:
    a, b = norm_titre(a), norm_titre(b)
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def main(scr: str, sortie: str) -> None:
    scr, sortie = Path(scr), Path(sortie)
    fiches: dict[str, dict] = {}
    sans_id = []
    for f in sorted((scr / "agents").glob("*.json")):
        try:
            liste = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"ILLISIBLE {f}: {e}", file=sys.stderr)
            continue
        for x in liste:
            x.setdefault("famille", f.stem)
            nid = norm_id(x.get("identifiant", ""))
            if not nid.startswith(("doi:", "arxiv:")):
                sans_id.append(x)
                continue
            if nid in fiches:
                y = fiches[nid]
                y["familles"] = sorted(set(y["familles"]) | {x["famille"]})
                y["statuts"] += x.get("statuts", [])
                y["chiffres"] += x.get("chiffres", [])
                if len(x.get("etablit", "")) > len(y.get("etablit", "")):
                    y["etablit"] = x["etablit"]
            else:
                x = dict(x)
                x["identifiant"] = nid
                x["familles"] = [x["famille"]]
                x.setdefault("statuts", [])
                x.setdefault("chiffres", [])
                fiches[nid] = x
    # revérification centrale
    for nid, x in fiches.items():
        r = biblio_v1.resoudre(nid)
        best, annee_api = 0.0, None
        for fi in r["fiches"]:
            s = sim(x.get("titre", ""), fi.get("titre") or "")
            if s > best:
                best = s
                annee_api = fi.get("annee") or (fi.get("date") or "")[:4] or None
        try:
            ecart = abs(int(annee_api) - int(x.get("annee"))) if annee_api else None
        except (TypeError, ValueError):
            ecart = None
        x["verification_centrale"] = {
            "resolu": r["resolu"], "interfaces": r["interfaces"], "similarite_titre": round(best, 3),
            "annee_interface": annee_api, "ecart_annee": ecart,
            "concorde": bool(r["resolu"] and best >= 0.8 and (ecart is None or ecart <= 1)),
        }
    (sortie / "fiches-fusionnees-v1.json").write_text(
        json.dumps({"fiches": list(fiches.values()), "sans_identifiant": sans_id}, ensure_ascii=False, indent=1),
        encoding="utf-8")
    # tables
    def ref(x):
        a = x.get("auteurs", "")
        a = a if len(a) < 60 else a[:57] + "…"
        return f"{a}, « {x.get('titre','')} »"

    def ident(x):
        v = x["verification_centrale"]
        mark = "vérifié" if v["concorde"] else ("à vérifier : discordance" if v["resolu"] else "à vérifier : non résolu")
        return f"`{x['identifiant']}` ({mark} ; {', '.join(v['interfaces']) or 'aucune'})"

    lignes = ["# Tables par hypothèse — revue bibliographique v1", "",
              "Pièce de travail (classe C). Une ligne par couple (référence, hypothèse). « Identifiant » : résolu par les interfaces nommées (OpenAlex, Semantic Scholar, arXiv, Crossref), titre et année concordants ; sinon « à vérifier ». Aucun chiffre ici : les chiffres vérifiés sur page de PDF sont dans `chiffres-verifies-v1.md`.",
              "", "Statuts : **soutient**, **contredit**, **nuance**, **occupe** (le travail fait déjà ce que l'hypothèse propose).", ""]
    for c in CIBLES:
        rows = []
        for x in fiches.values():
            for s in x["statuts"]:
                if s.get("cible") == c:
                    rows.append((x, s))
        rows.sort(key=lambda t: (str(t[1].get("statut")), -int(t[0].get("annee") or 0)))
        lignes += [f"## {c} — {NOMS[c]}", ""]
        if not rows:
            lignes += ["Aucune référence retenue ; voir la synthèse (zone à éprouver, R8).", ""]
            continue
        lignes += ["| Référence | Année | Identifiant | Ce que le travail établit | Statut |", "|---|---|---|---|---|"]
        vus = set()
        for x, s in rows:
            k = (x["identifiant"], s.get("statut"))
            if k in vus:
                continue
            vus.add(k)
            cell = lambda t: str(t or "").replace("|", "/").replace("\n", " ")
            lignes.append(f"| {cell(ref(x))} | {x.get('annee','')} | {ident(x)} | {cell(x.get('etablit'))} | **{s.get('statut')}** : {cell(s.get('pourquoi'))} |")
        lignes.append("")
    if sans_id:
        lignes += ["## Références sans DOI ni arXiv (livres, chapitres) — non vérifiées par interface", "",
                   "| Référence | Année | Identifiant donné | Ce que le travail établit | Cibles |", "|---|---|---|---|---|"]
        for x in sans_id:
            cib = "; ".join(f"{s.get('cible')} {s.get('statut')}" for s in x.get("statuts", []))
            lignes.append(f"| {ref(x)} | {x.get('annee','')} | {x.get('identifiant','') or '—'} (à vérifier) | {str(x.get('etablit','')).replace('|','/')} | {cib} |")
        lignes.append("")
    (sortie / "tables-par-hypothese-v1.md").write_text("\n".join(lignes), encoding="utf-8")
    # nouveau depuis 2024
    nv = sorted([x for x in fiches.values() if int(x.get("annee") or 0) >= 2024],
                key=lambda x: (-int(x.get("annee") or 0), x.get("titre", "")))
    L = ["# Nouveau depuis 2024 — revue bibliographique v1", "",
         "Pièce de travail (classe C). Références datées de 2024 à novembre 2026, par année décroissante.", "",
         "| Année | Référence | Identifiant | Ce que le travail établit | Cibles |", "|---|---|---|---|---|"]
    for x in nv:
        cib = ", ".join(sorted({f"{s.get('cible')} ({s.get('statut')})" for s in x["statuts"]}))
        L.append(f"| {x.get('annee')} | {ref(x)} | {ident(x)} | {str(x.get('etablit','')).replace('|','/')} | {cib} |")
    (sortie / "nouveau-depuis-2024-v1.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    n_ok = sum(x["verification_centrale"]["concorde"] for x in fiches.values())
    print(json.dumps({"fiches": len(fiches), "concordantes": n_ok, "sans_identifiant": len(sans_id),
                      "depuis_2024": len(nv)}, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
