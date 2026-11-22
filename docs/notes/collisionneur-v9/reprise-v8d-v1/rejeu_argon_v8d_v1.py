#!/usr/bin/env python3
"""Rejeu à part des cellules d'Argon jouées sans réflexion avant la v8 (GO-2026-11-22-08, réserve de R-4750).

Pièce d'instrument (classe B). N'écrit jamais dans un dossier fini : chaque dossier d'origine reçoit un dossier neuf
`<origine>-rejeu-argon-v8d-v1`. Chaque cellule est renvoyée à Argon avec SON invite d'origine (le fichier
`essais/<cellule>.essai<n>.prompt.txt` de l'essai OK, empreinte contrôlée contre le journal d'origine), par
`executer_cellule` de la v8d importée telle quelle : garde des réglages de Google (garde v3), comptage de l'entrée,
plafond, ligne, relance identique puis dernier recours déclarés, refus d'une réponse sans pensées (code 10), coupure
comptée au pire. Aucune autre espèce n'est appelée.

Commandes (PYTHONPATH=src) :
  devis        liste des cellules et pire coût (hors relances, puis avec relances), sans réseau
  lancer       rejoue, une cellule à la fois ; plafond global --plafond-usd sur la somme des dossiers neufs
  cote-a-cote  table ancienne cellule / cellule rejouée (empreintes, caractères, pensées, coût), sans lire les textes
"""
import argparse
import importlib.util
import json
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
SCRIPT = RACINE / "docs/notes/collisionneur-v9/collisionneur_v9_v8d.py"
SHA_SCRIPT = "b780383874598f12b24c79e4087d335c8e01cda685e295f5116898fa3b1715ac"
SUFFIXE = "-rejeu-argon-v8d-v1"
# Les dix cellules de la réserve de R-4750 (journaux versés : essai OK écrit par collisionneur-v9-v3, sans réflexion).
CIBLES = [
    ("runs/collisionneur-percee-controle-securite-v1-20261121-114810", ["E3-T1-conception-C", "E3-T2-critique-croisee-C"]),
    ("runs/collisionneur-derive-de-regime-v2-20261121-131044", ["E3-T1-conception-C", "E3-T2-critique-croisee-C"]),
    ("runs/collisionneur-methodes-maths-v1-20261121-093850", ["E3-T1-conception-C"]),
    ("runs/collisionneur-anteriorite-pilier-v1-20261121-131029",
     ["E3-T1-conception-C", "E3-T2-critique-croisee-C", "E3-T3-reponse-C"]),
    ("runs/collisionneur-question-de-recherche-fusionnee-v1-20261121-153256",
     ["E3-T1-conception-C", "E3-T2-critique-croisee-C"]),
]
CODE_ARRET = 30


def charger_v8d():
    import hashlib
    h = hashlib.sha256(SCRIPT.read_bytes()).hexdigest()
    if h != SHA_SCRIPT:
        raise SystemExit(f"ARRÊT : empreinte de la v8d {h} différente de {SHA_SCRIPT}")
    spec = importlib.util.spec_from_file_location("collisionneur_v9_v8d", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def journal(dossier):
    return [json.loads(l) for l in (RACINE / dossier / "journal.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]


def essai_origine(dossier, cid):
    """L'essai OK d'origine : doit être unique, écrit sans réflexion (aucun niveau, aucun budget), invite scellée."""
    oks = [e for e in journal(dossier) if e.get("cellule") == cid and e.get("statut") == "OK" and "essai" in e]
    if len(oks) != 1:
        raise SystemExit(f"ARRÊT : {dossier} {cid} : {len(oks)} essai(s) OK au journal, un seul attendu")
    e = oks[0]
    if e.get("espece") != "argon" or e.get("niveau_reflexion") or e.get("script") != "collisionneur-v9-v3":
        raise SystemExit(f"ARRÊT : {dossier} {cid} : essai OK hors réserve (espèce {e.get('espece')}, script "
                         f"{e.get('script')}, niveau {e.get('niveau_reflexion')})")
    chemin = RACINE / dossier / "essais" / f"{cid}.essai{e['essai']}.prompt.txt"
    texte = chemin.read_text(encoding="utf-8")
    import hashlib
    h = hashlib.sha256(texte.encode("utf-8")).hexdigest()
    sceau = (Path(str(chemin) + ".sha256")).read_text(encoding="utf-8").split()[0]
    if not (h == e["sha256_prompt"] == sceau):
        raise SystemExit(f"ARRÊT : {dossier} {cid} : invite d'origine {h} ≠ journal {e['sha256_prompt']} ou sceau {sceau}")
    return e, texte


def composer(v, dossier, cle_anthropic, cle_openai):
    comp = json.loads((RACINE / dossier / "especes.json").read_text(encoding="utf-8"))
    v.fixer_composition(comp["especes"], cle_anthropic, "ANTHROPIC_WORKSPACE_ID", cle_openai)
    if v.MODELES["C"]["espece"] != "argon":
        raise SystemExit(f"ARRÊT : {dossier} : la lettre C n'est pas Argon")
    return comp["especes"]


def devis(v, a):
    tot, tot_rel = 0.0, 0.0
    print("| dossier d'origine | cellule | essai d'origine | invite (car.) | pire sans relance | pire avec relances |")
    print("|---|---|---|---|---|---|")
    for dossier, cids in CIBLES:
        composer(v, dossier, a.cle_anthropic, a.cle_openai)
        m = v.MODELES["C"]
        relances = 2 if v.reglage_de_relance(m)[1] else 1
        for cid in cids:
            e, texte = essai_origine(dossier, cid)
            pire = v.cout_pire_cas(m, len(texte), m["max"])
            pire_rel = pire + relances * v.cout_pire_cas(m, len(texte), m["max_relance"])
            tot += pire
            tot_rel += pire_rel
            print(f"| {Path(dossier).name} | {cid} | {e['essai']} | {len(texte)} | {pire:.4f} | {pire_rel:.4f} |")
    print(f"\nTotal : {tot:.4f} USD au pire sans relance ; {tot_rel:.4f} USD si chaque cellule épuisait ses relances "
          f"({relances} chez Argon : relance identique, puis dernier recours), refusé avant l'envoi par le plafond.")
    print(f"Argon : niveau {m.get('niveau_reflexion')!r}, plafond {m['max']}, provision {m['provision']}, prix {m['prix']}")
    return 0


def depense_neufs(v):
    s = 0.0
    for dossier, _ in CIBLES:
        neuf = RACINE / (dossier + SUFFIXE)
        if (neuf / "journal.jsonl").exists():
            s += v.depense(neuf)
    return s


def lancer(v, a):
    for dossier, cids in CIBLES:
        especes = composer(v, dossier, a.cle_anthropic, a.cle_openai)
        v.verifier_cles()
        neuf = RACINE / (dossier + SUFFIXE)
        v.verser_une_fois(neuf / "faits.md", RACINE / dossier / "faits.md", "faits d'origine")
        v.verser_une_fois(neuf / "question-etage3.md", RACINE / dossier / "question-etage3.md", "question d'origine")
        v.sceller_composition(neuf)
        v.declarer_script(neuf, False)
        if not (neuf / "journal.jsonl").exists():
            v.ajouter_journal(neuf, {"rejeu_a_part": {"go": a.go, "origine": dossier, "cellules": cids,
                                                      "especes": especes, "programme": Path(__file__).name},
                                     "quand": v.maintenant()})
        for cid in cids:
            if v.cellule_valide(neuf, cid):
                print(f"{cid} ({neuf.name}) : déjà rejouée, sautée", flush=True)
                continue
            e, prompt = essai_origine(dossier, cid)
            tour = next(t for t in v.TOURS if cid.startswith(t))
            plafond = a.plafond_usd - (depense_neufs(v) - v.depense(neuf))  # plafond global sur la somme des neufs
            try:
                statut = v.executer_cellule(str(neuf), tour, "C", prompt, e.get("pieces", []), plafond, v.APPELANTS)
            except v.Arret as x:
                v.ecrire_etat(str(neuf))
                print(f"ARRÊT (code {x.code}) : {x}", file=sys.stderr, flush=True)
                return x.code
            if statut != "OK":
                v.ecrire_etat(str(neuf))
                print(f"ARRÊT : {cid} : statut {statut}", file=sys.stderr, flush=True)
                return CODE_ARRET
        v.ecrire_etat(str(neuf))
    print(f"Rejeu fini ; dépense des dossiers neufs {depense_neufs(v):.2f} USD.", flush=True)
    return 0


def pensees(e):
    u = e.get("usage") or {}
    return u.get("reflexion")


def cote_a_cote(v, a):
    print("| dossier d'origine | cellule | ancienne : sha256 texte | car. | pensées | réglage | rejouée : sha256 texte "
          "| car. | pensées | niveau | coût USD |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for dossier, cids in CIBLES:
        neuf = RACINE / (dossier + SUFFIXE)
        jn = journal(dossier + SUFFIXE) if (neuf / "journal.jsonl").exists() else []
        for cid in cids:
            e, _ = essai_origine(dossier, cid)
            ok = [x for x in jn if x.get("cellule") == cid and x.get("statut") == "OK" and "essai" in x]
            r = ok[-1] if ok else None
            reglage = f"budget {e.get('budget_reflexion')}" if e.get("budget_reflexion") else "aucun niveau"
            print(f"| {Path(dossier).name} | {cid} | `{e['sha256_texte']}` | {e['caracteres']} | {pensees(e)} | {reglage} | "
                  + (f"`{r['sha256_texte']}` | {r['caracteres']} | {pensees(r)} | {r.get('niveau_reflexion')} | "
                     f"{r['cout_usd']:.4f} |" if r else "non rejouée | | | | |"))
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("commande", choices=["devis", "lancer", "cote-a-cote"])
    p.add_argument("--cle-anthropic", default="RR_ANTHROPIC_API_KEY_LUC")
    p.add_argument("--cle-openai", default="OPENAI_API_KEY_2")
    p.add_argument("--plafond-usd", type=float, default=20.0)
    p.add_argument("--go", default="GO-2026-11-22-08")
    a = p.parse_args(argv)
    v = charger_v8d()
    return {"devis": devis, "lancer": lancer, "cote-a-cote": cote_a_cote}[a.commande](v, a)


if __name__ == "__main__":
    sys.exit(main())
