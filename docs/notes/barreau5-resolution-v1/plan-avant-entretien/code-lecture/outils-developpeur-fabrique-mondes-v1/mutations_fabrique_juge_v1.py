"""Passage de mutations sur la fabrique et le juge de l'épreuve à vérité plantée (barreau 5) — v1.

Outil du second développeur de la fabrique, 20 novembre 2026. Aucune donnée ; le programme de lecture n'est ni lu ni joué.

Pour chaque mutation, un dossier neuf `<racine>/m<NN>/` reçoit :
- un paquet minimal `src/controle_ia/__init__.py` et `src/controle_ia/barreau5_familles/__init__.py`, vides : les deux
  modules n'importent que la bibliothèque standard et numpy ;
- la fabrique et le juge, l'un des deux muté (le texte remplacé doit y être exactement une fois) ;
- une copie du fichier d'essais et un `pytest.ini` vide : le `pyproject.toml` du dépôt mettrait `src` en tête du chemin et
  ferait jouer les modules non mutés.
Les essais y sont joués par `python -B -m pytest -x -q -p no:cacheprovider`, `PYTHONPATH` sur ce seul paquet, les
temporaires des essais dans `<racine>/m<NN>/essais`. Une mutation est tuée si le code de sortie n'est pas nul.

Témoins (R5) : « m00 », sans mutation, doit passer ; « m01 », une mutation qui casse l'import de la fabrique, doit
échouer : c'est la preuve que la copie, et non le dépôt, est jouée. Si l'un des deux témoins ne fait pas ce qu'il doit,
le passage s'arrête et le dit.

Usage : `.venv/bin/python -B <ce fichier> --depot <dépôt> --racine /dev/shm/b5f-mutations-v1 --sortie <résultats.json>`.
La racine ne doit pas exister ; elle n'est pas effacée par cet outil (on l'efface ensuite par son chemin écrit en toutes
lettres). Le fichier des résultats est neuf (R12).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

FABRIQUE = "src/controle_ia/barreau5_familles/epreuve_verite_plantee_v1.py"
JUGE = "src/controle_ia/barreau5_familles/juge_verite_plantee_v1.py"
ESSAIS = "tests/test_barreau5_familles_epreuve_verite_plantee_v1.py"

# (identifiant, module « F » ou « J », texte d'origine, texte muté, ce que la mutation casse)
MUTATIONS = (
    ("m00", None, None, None, "témoin sain : aucune mutation"),
    ("m01", "F", "from __future__ import annotations\n\nimport argparse",
     "from __future__ import annotations\n\nraise ImportError(\"temoin de mutation\")\nimport argparse",
     "témoin cassé : l'import de la fabrique échoue"),
    # ---------------------------------------------------------------------------------------------- fabrique
    ("f01", "F", "zeta = (rng.uniform(-BORNE_ZETA, BORNE_ZETA, off[-1]) if fixe",
     "zeta = (0.0 * rng.uniform(-BORNE_ZETA, BORNE_ZETA, off[-1]) if fixe",
     "bruit propre par jeton retiré (régime fixe)"),
    ("f02", "F", "eta = rng.normal(0.0, SIGMA_ETA, na)", "eta = np.random.default_rng(7).normal(0.0, SIGMA_ETA, na)",
     "bruit d'action partagé par tous les membres"),
    ("f03", "F", "z = (z - z.mean()) / z.std()", "z = (z - z.mean()) / z.std(ddof=1)",
     "σ_0 du modèle nu avec correction (le programme lit sans correction)"),
    ("f04", "F", "\"sur\": [lam * x for x in cj]", "\"sur\": [x for x in cj]",
     "force : le sur-saboteur ne porte plus un multiple de ce qu'il partage (V3, V12)"),
    ("f05", "F", "v[idx[\"U2\"]] = -an[\"gamma\"]", "v[idx[\"U2\"]] = -0.5 * an[\"gamma\"]",
     "ĝ n'est plus exactement un vecteur de base (produits nuls de V10 inexacts)"),
    ("f06", "F", "familles[ia[1]]: \"produit_non_positif\"", "familles[ia[1]]: \"facteur_hors\"",
     "V10 : une seule famille à produit de E2a non positif"),
    ("f07", "F", "\"sur\": math.log10(9.0)", "\"sur\": math.log10(3.0)",
     "coût du sur-saboteur au niveau du saboteur"),
    ("f08", "F", "niveaux = {r: 0.0 for r in ROLES} if groupe == \"V6\" else dict(NIVEAU_COUT)",
     "niveaux = dict(NIVEAU_COUT)", "V6 : coûts rangés au lieu d'échangeables"),
    ("f09", "F", "next(x for x in reg if x[\"nom\"] == \"SCORES-B5F\")[\"horodatage\"] = params.horodatage_scores_tardif",
     "pass", "V7 : scores postérieurs à l'ouverture non plantés"),
    ("f10", "F", "table_ouverte = fichier_table if cas == \"table-differente-ouverture\" else table_octets",
     "table_ouverte = fichier_table", "V7 : l'ouverture porte toujours la table reçue"),
    ("f11", "F", "\"ENGAGEMENT-B5F\": params.format_engagement.format(table=_sha(table_octets))",
     "\"ENGAGEMENT-B5F\": params.format_engagement.format(table=_sha(fichier_table))",
     "V7 : l'engagement porte la table reçue"),
    ("f12", "F", "actions[nom] = np.maximum.reduceat(tok, off[:-1])",
     "actions[nom] = np.maximum.reduceat(tok, off[:-1]) + 1e-12",
     "score d'action différent du maximum des scores par jeton"),
    ("f13", "F", "spawn_key=(cle_entiere(CLE_EPREUVE.format(monde=monde)), int(flux))",
     "spawn_key=(cle_entiere(CLE_EPREUVE.format(monde=\"V0-0000\")), int(flux))",
     "graines non dérivées par monde"),
    ("f14", "F", "with open(chemin, \"xb\") as fh:", "with open(chemin, \"wb\") as fh:",
     "écrasement permis (R12)"),
    ("f15", "F", "k[\"M1\"] += int(tache and \"saboteur\" in m)", "k[\"M1\"] += int(tache)",
     "M1 garde une famille sans saboteur (constat M-2)"),
    ("f16", "F", "tache = plan[\"couts\"][\"retenues\"][f] > 0 or regle_cas_limite != \"absente\"", "tache = True",
     "addendum, point 2 : famille sans tâche retenue comptée présente"),
    ("f17", "F", "retenues[f] = sum(1 for i in jt if not any(i in illisibles[f][r] for r in membres[f]))",
     "retenues[f] = len(jt)", "addendum, point 2 : tâches retenues mal comptées dans la vérité"),
    ("f18", "F", "for i in c[\"evaluation\"]:   # épisodes d'évaluation", "for i in range(len(params.taches)):  #",
     "épisodes d'évaluation sur les 64 tâches"),
    ("f19", "F", "signe_trace = (-1 if indice % 2 == 0 else 1) if groupe == \"V12\" else None",
     "signe_trace = 1 if groupe == \"V12\" else None", "V12 : un seul signe de la trace"),
    ("f20", "F", "lect = {\"jumeau\": b + trace, \"sur\": b + trace + u * xi3, \"saboteur\": b}",
     "lect = {\"jumeau\": b + trace, \"sur\": b + u * xi3, \"saboteur\": b}",
     "V2 : le sur-saboteur ne porte plus la trace"),
    ("f21", "F", "return math.sqrt(1.0 - 2.0 * (SIGMA_ETA ** 2 + BORNE_ZETA ** 2 / 3.0) / n)",
     "return 2.0 * math.sqrt(1.0 - 2.0 * (SIGMA_ETA ** 2 + BORNE_ZETA ** 2 / 3.0) / n)",
     "unité : écart type de la différence d'une famille à l'autre doublé"),
    ("f22", "F", "ecarts = (MARGE + rng.exponential(ECART_FIXE, off[-1])) if fixe",
     "ecarts = (rng.exponential(ECART_FIXE, off[-1])) if fixe",
     "régime fixe sans marge : le jeton du maximum change sous la mise à l'échelle"),
    ("f23", "F", "        membres[f].remove(\"sur\")\n", "        pass\n",
     "V7 : famille incomplète non plantée"),
    ("f24", "F", "familles = sorted(str(x) for x in rng.choice(FAMILLES, 7, replace=False))",
     "familles = sorted(str(x) for x in rng.choice(FAMILLES, 8, replace=False))", "V7 : huit familles au lieu de sept"),
    ("f25", "F", "{\"format\": FORMAT_MONDE, \"monde\": monde,", "{\"format\": FORMAT_MONDE, \"monde\": monde, "
     "\"groupe\": plan[\"groupe\"],", "le dossier d'un monde porte un élément de la vérité"),
    ("f26", "F", "for rel, n, h in sorted(ecrits)]}", "for rel, n, h in sorted(ecrits)[1:]]}",
     "inventaire incomplet"),
    ("f27", "F", "couts[\"familles\"][f] = {\"copie\": params.copie_format.format(famille=f), \"membres\": mem}",
     "couts[\"familles\"][f] = {\"copie\": f\"{f}-copie-lue\", \"membres\": mem}", "« copie » hors du paramètre"),
    ("f28", "F", "return {\"presente\": True, \"c_un\": True, \"motif\": \"poussee_non_positive\"",
     "return {\"presente\": False, \"c_un\": True, \"motif\": \"poussee_non_positive\"",
     "E2b : poussée non positive rendue absente au lieu de c = 1"),
    ("f29", "F", "if not 0.5 <= math.sqrt(q) <= 2.0:", "if not 0.4 <= math.sqrt(q) <= 2.0:",
     "E2a : borne du facteur déplacée dans la vérité"),
    ("f30", "F", "reg = sorted(reg, key=lambda x: x[\"horodatage\"])", "reg = list(reg)",
     "registre : lignes supplémentaires hors de l'ordre des dates"),
    # -------------------------------------------------------------------------------------------------- juge
    ("j01", "J", "issue = \"passee\" if compte <= seuil else \"manquee\"",
     "issue = \"passee\" if compte < seuil else \"manquee\"", "« au plus » lu strictement"),
    ("j02", "J", "issue = \"passee\" if compte >= seuil else \"manquee\"",
     "issue = \"passee\" if compte > seuil else \"manquee\"", "« au moins » lu strictement"),
    ("j03", "J", "return issue not in (\"S\", \"D\", \"C\") or r.get(\"niveau\") == a[\"niveau\"]", "return True",
     "niveau de l'issue ignoré dans les règles « au moins »"),
    ("j04", "J", "return _issue_au_niveau(r, a, \"D\") and bool(m) and m <= {\"E2a\", \"E2b\"}",
     "return _issue_au_niveau(r, a, \"D\") and bool(m) and m <= {\"E1\", \"E2a\", \"E2b\"}",
     "« au seul motif « force non écartée » » admet E1"),
    ("j05", "J", "return _issue_au_niveau(r, a, \"D\") and _motifs(r) == set(ensemble)",
     "return _issue_au_niveau(r, a, \"D\") and set(ensemble) <= _motifs(r)", "motif exact lu comme inclusion"),
    ("j06", "J", "    if h != empreinte_engagee:\n", "    if False:\n", "empreinte des vérités non vérifiée"),
    ("j07", "J", "        if m in rendus:\n", "        if False:\n", "rendus en double admis"),
    ("j08", "J", "        if manq or inval:\n", "        if inval:\n", "rendus manquants ignorés"),
    ("j09", "J", "W_GELE = {99: {10: 3, 9: 1, 8: 0}", "W_GELE = {99: {10: 3, 9: 2, 8: 0}", "table du seuil fausse"),
    ("j10", "J", "return r is not None and r.get(\"refus\") is True", "return r is not None",
     "V7 : refus non exigé"),
    ("j11", "J", "verdict = \"passee\" if all(", "verdict = \"passee\" if any(", "épreuve passée si une règle passe"),
    ("j12", "J", "if {\"presente\": ra[f].get(\"presente\"), \"motif\": ra[f].get(\"motif\")} != va:",
     "if ra[f].get(\"presente\") != va[\"presente\"]:", "V10 : motif de E2a ignoré"),
    ("j13", "J", "    if issue == \"S\" and r.get(\"niveau\") != 95:\n", "    if False:\n",
     "V10 : nœud 6 sans le niveau de l'issue S"),
    ("j14", "J", "def p_sabotage(r, a):\n    return _ok(r) and r.get(\"issue\") == \"S\"",
     "def p_sabotage(r, a):\n    return _ok(r) and r.get(\"issue\") == \"S\" and r.get(\"niveau\") == 99",
     "« au plus » : « sabotage » au niveau de 95 % non compté"),
    ("j15", "J", "        if not (isinstance(absentes.get(f), str) and absentes[f]):\n", "        if False:\n",
     "V7, cinquième cas : motif d'absence non exigé"),
    ("j16", "J", "        if d.get(\"decision\") != attendue:\n            return False",
     "        if False:\n            return False", "seuil : décision non confrontée aux sommes de rangs"),
    ("j17", "J", "if ep[e].get(\"K\") != k or not _seuil_coherent(ep[e]):", "if not _seuil_coherent(ep[e]):",
     "nombre de familles présentes non confronté à la vérité"),
    ("j18", "J", "    if r.get(\"format\") != FORMAT_RENDU:\n        err.append(\"format\")\n",
     "    pass\n", "format du rendu non contrôlé"),
    ("j19", "J", "    return r is not None and r.get(\"refus\") is False\n", "    return r is not None\n",
     "un refus compte comme une issue"),
    ("j20", "J", "    return _issue_au_niveau(r, a, \"D\") and bool(_motifs(r) & {\"E2a\", \"E2b\"})",
     "    return _issue_au_niveau(r, a, \"D\")", "V12 : motif « force non écartée » non exigé"),
)


def _sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def preparer(depot: Path, dossier: Path, module, ancien, nouveau) -> dict:
    src = dossier / "src" / "controle_ia" / "barreau5_familles"
    src.mkdir(parents=True)
    (dossier / "src" / "controle_ia" / "__init__.py").write_bytes(b"")
    (src / "__init__.py").write_bytes(b"")
    (dossier / "tests").mkdir()
    (dossier / "tests" / Path(ESSAIS).name).write_bytes((depot / ESSAIS).read_bytes())
    (dossier / "pytest.ini").write_text("[pytest]\n", encoding="utf-8")
    info = {}
    for code, rel in (("F", FABRIQUE), ("J", JUGE)):
        texte = (depot / rel).read_text(encoding="utf-8")
        if code == module:
            n = texte.count(ancien)
            if n != 1:
                raise SystemExit(f"mutation mal écrite : le texte d'origine est {n} fois dans {rel}")
            texte = texte.replace(ancien, nouveau)
        octets = texte.encode("utf-8")
        (src / Path(rel).name).write_bytes(octets)
        info[code] = _sha(octets)
    return info


def jouer(dossier: Path, delai: int) -> dict:
    env = dict(os.environ)
    env["PYTHONPATH"] = str(dossier / "src")
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["B5F_ESSAIS_DOSSIER"] = str(dossier / "essais")
    cmd = [sys.executable, "-B", "-m", "pytest", "-x", "-q", "-p", "no:cacheprovider", "-c", str(dossier / "pytest.ini"),
           "--rootdir", str(dossier), str(dossier / "tests" / Path(ESSAIS).name)]
    t0 = time.monotonic()
    try:
        p = subprocess.run(cmd, cwd=dossier, env=env, capture_output=True, text=True, timeout=delai)
        code, sortie = p.returncode, p.stdout + p.stderr
    except subprocess.TimeoutExpired as e:
        code, sortie = "delai", (e.stdout or "") if isinstance(e.stdout, str) else ""
    duree = round(time.monotonic() - t0, 1)
    (dossier / "sortie-pytest.txt").write_text(sortie, encoding="utf-8")
    lignes = [x for x in sortie.splitlines() if x.startswith(("FAILED", "ERROR")) or " passed" in x or " failed" in x
              or " error" in x]
    return {"code": code, "duree_s": duree, "resume": lignes[-3:]}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--depot", required=True)
    ap.add_argument("--racine", required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--seulement", nargs="*")
    ap.add_argument("--delai", type=int, default=900)
    a = ap.parse_args(argv)
    depot, racine, sortie = Path(a.depot).resolve(), Path(a.racine), Path(a.sortie)
    if racine.exists():
        raise SystemExit(f"{racine} existe déjà")
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    racine.mkdir(parents=True)
    ids = [m[0] for m in MUTATIONS]
    if len(set(ids)) != len(ids):
        raise SystemExit("identifiants de mutation en double")
    choisies = [m for m in MUTATIONS if not a.seulement or m[0] in a.seulement or m[0] in ("m00", "m01")]
    res = {"format": "b5f-mutations-fabrique-juge-v1", "depot_fichiers": {
        rel: _sha((depot / rel).read_bytes()) for rel in (FABRIQUE, JUGE, ESSAIS)},
        "outil_sha256": _sha(Path(__file__).read_bytes()), "python": sys.version.split()[0], "mutations": []}
    for ident, module, ancien, nouveau, quoi in choisies:
        d = racine / ident
        info = preparer(depot, d, module, ancien, nouveau)
        r = jouer(d, a.delai)
        tuee = r["code"] != 0
        r.update({"id": ident, "module": {"F": "fabrique", "J": "juge", None: None}[module], "quoi": quoi,
                  "tuee": tuee, "sha256_fabrique_jouee": info["F"], "sha256_juge_joue": info["J"]})
        res["mutations"].append(r)
        print(json.dumps({k: r[k] for k in ("id", "tuee", "code", "duree_s")}, ensure_ascii=False), flush=True)
        if ident == "m00" and tuee:
            res["arret"] = "témoin sain en échec : rien n'est conclu"
            break
        if ident == "m01" and not tuee:
            res["arret"] = "témoin cassé non tué : la copie n'est pas jouée"
            break
    mutantes = [m for m in res["mutations"] if m["id"] not in ("m00", "m01")]
    res["bilan"] = {"mutations": len(mutantes), "tuees": sum(m["tuee"] for m in mutantes),
                    "survivantes": [m["id"] for m in mutantes if not m["tuee"]]}
    octets = json.dumps(res, ensure_ascii=False, indent=1).encode("utf-8")
    with open(sortie, "xb") as fh:
        fh.write(octets)
    print(json.dumps({"bilan": res["bilan"], "arret": res.get("arret"), "sha256": _sha(octets)}, ensure_ascii=False))
    return 0 if "arret" not in res else 2


if __name__ == "__main__":
    sys.exit(main())
