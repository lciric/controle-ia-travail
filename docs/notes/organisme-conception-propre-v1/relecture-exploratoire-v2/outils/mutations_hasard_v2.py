#!/usr/bin/env python3
"""Banc de mutations du générateur d'idées au hasard v2 et des contrôles des témoins v2 — relecture exploratoire.

Écrit le 14 novembre 2026 (vers 12:38 UTC, `date -u`) par le préparateur (modèle A). Chaque mutant est une copie des deux
programmes dans un dossier temporaire hors du dépôt, une seule chaîne remplacée (présente exactement une fois) ; les essais
`essais_temoins_et_hasard_v2.py` sont joués contre lui (`LC_OUTILS`). Tué si les essais échouent ; la base doit passer.
Sous `unshare -n`, environnement réduit (PATH, LANG, LC_ALL, TZ, TMPDIR, HOME).

    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B mutations_hasard_v2.py SORTIE.json
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
GEN, CTRL = "tirer_fiches_hasard_v2.py", "controler_temoins_v2.py"
ESSAIS = ICI / "essais_temoins_et_hasard_v2.py"
MUTANTS = [
    ("gabarits tirés avec remise", GEN, 'gab[nom] = [int(x) for x in rng.permutation(len(res))[:NOMBRE]]',
     'gab[nom] = [int(x) for x in rng.integers(len(res), size=NOMBRE)]'),
    ("urnes tirées avec remise", GEN, 'urnes[champ] = [u[int(i)] for i in rng.permutation(len(u))[:NOMBRE]]',
     'urnes[champ] = [u[int(i)] for i in rng.integers(len(u), size=NOMBRE)]'),
    ("chaîne forcée cohérente avec le signe", GEN, 'sens_metrique = d1 * (d12 if deux_maillons else 1) * d2',
     'sens_metrique = -1 if signe == "0" else +1'),
    ("cohérence consignée toujours vraie", GEN, '"coherente_avec_le_signe": sens_metrique == sens_predit}',
     '"coherente_avec_le_signe": True}'),
    ("longueur cible hors de l'intervalle interquartile", GEN, 'return int(rng.integers(int(q["q1"]), int(q["q3"]) + 1))',
     'return int(rng.integers(int(q["min"]), int(q["max"]) + 1))'),
    ("graine changée", GEN, 'ENTROPIE = 2026111411', 'ENTROPIE = 2026111301'),
    ("garantie du juge omise", GEN, 'self.gab("demande_garantie") if levier == "juge" else self.gab("demande_rien")',
     'self.gab("demande_rien")'),
    ("statistiques non épinglées", GEN, 'if hashlib.sha256(brut).hexdigest() != STATS_SHA256:', 'if False:'),
    ("écrasement permis", GEN, '    if sortie.exists():\n        print(f"{sortie} existe déjà (R12)"',
     '    if False:\n        print(f"{sortie} existe déjà (R12)"'),
    ("contraction absente", GEN, '            return (de if prep == "de" else a) + gn[len(art):]', '            return f"{prep} {gn}"'),
    ("contrôle : suite commune non bornée", CTRL, 'max(suites.values()) <= SUITE_MAX', 'True'),
    ("contrôle : phrases communes hasard-lecteur ignorées", CTRL,
     'res["controles"]["aucune_phrase_commune_hasard_et_lecteur"] = not any(communes_hl.values())',
     'res["controles"]["aucune_phrase_commune_hasard_et_lecteur"] = True'),
    ("contrôle : médianes non contrôlées", CTRL,
     'res["controles"]["hasard_medianes_dans_l_intervalle_interquartile"] = not hors_iqr_h',
     'res["controles"]["hasard_medianes_dans_l_intervalle_interquartile"] = True'),
    ("contrôle : phrases de soixante mots au moins", CTRL, 'MOTS_PHRASE_MIN = 6', 'MOTS_PHRASE_MIN = 60'),
    ("contrôle : totaux non bornés", CTRL, 'hors_bornes = {k: v for k, v in totaux.items() if not (tot["min"] <= v <= tot["max"])}',
     'hors_bornes = {}'),
]


def jouer(dossier: Path, delai=600) -> tuple[bool, str]:
    env = {k: v for k, v in os.environ.items() if k in ("PATH", "LANG", "LC_ALL", "TZ", "HOME")}
    env.update({"LC_OUTILS": str(dossier), "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(dossier.parent)})
    c = subprocess.run(["unshare", "-n", sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider",
                        "--basetemp", str(dossier.parent / "pytest"), str(ESSAIS)],
                       capture_output=True, text=True, env=env, timeout=delai, cwd=str(ICI.parents[4]))
    lignes = c.stdout.strip().splitlines() or [""]
    echec = next((l for l in lignes if l.startswith("FAILED") or l.startswith("ERROR")), "")
    return c.returncode == 0, lignes[-1] + (" | " + echec[:160] if echec else "")


def main(sortie: str) -> int:
    debut = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    resultats = []
    with tempfile.TemporaryDirectory(prefix="mut-hasard-v2-") as tmp:
        tmp = Path(tmp)
        base = tmp / "base" / "outils"
        base.mkdir(parents=True)
        for n in (GEN, CTRL):
            shutil.copyfile(ICI / n, base / n)
        ok, ligne_base = jouer(base)
        if not ok:
            print("la base échoue : " + ligne_base, file=sys.stderr)
            return 1
        for k, (nom, fichier, ancien, nouveau) in enumerate(MUTANTS, 1):
            d = tmp / f"m{k:03d}" / "outils"
            shutil.copytree(base, d)
            texte = (d / fichier).read_text(encoding="utf-8")
            if texte.count(ancien) != 1:
                r = {"mutant": k, "nom": nom, "statut": "inapplicable", "occurrences": texte.count(ancien)}
            else:
                (d / fichier).write_text(texte.replace(ancien, nouveau), encoding="utf-8")
                survit, ligne = jouer(d)
                r = {"mutant": k, "nom": nom, "fichier": fichier, "statut": "survivant" if survit else "tue",
                     "sortie": ligne}
            resultats.append(r)
            print(f"{k:03d} {dict(tue='tué', survivant='SURVIT', inapplicable='INAPPLICABLE')[r['statut']]} — {nom}",
                  flush=True)
    tues = sum(r["statut"] == "tue" for r in resultats)
    res = {"banc": "mutations-hasard-v2", "debut_utc": debut, "fin_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "base": ligne_base, "isolement": "unshare -n ; environnement réduit", "mutants": len(MUTANTS), "tues": tues,
           "survivants": [r["nom"] for r in resultats if r["statut"] == "survivant"],
           "inapplicables": [r["nom"] for r in resultats if r["statut"] == "inapplicable"], "detail": resultats}
    Path(sortie).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{tues} tués sur {len(MUTANTS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
