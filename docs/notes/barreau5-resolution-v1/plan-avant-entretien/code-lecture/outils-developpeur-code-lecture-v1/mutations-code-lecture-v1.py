"""Passage de mutations du code de lecture du barreau 5 (développeur du code de lecture, 20 novembre 2026).

Des défauts sont réintroduits un à un dans une copie de travail (une seule à la fois, sous le bloc-notes) ; pour chacun, les
essais visés sont joués sur la copie ; la mutation est « attrapée » si au moins un essai échoue. Chaque « avant » doit
paraître exactement une fois dans le fichier d'origine (sinon : « introuvable », compté à part). Le fichier muté est remis à
l'identique après chaque essai. Les mutations équivalentes ou redondantes (sorties ou refus inchangés, par une seconde garde)
ne sont pas jouées : elles sont nommées dans le rapport, avec leur raison, et ne comptent ni comme attrapées ni comme
manquées.

Usage : python -B mutations-code-lecture-v1.py COPIE BASETEMP [IDENTIFIANTS…]
  COPIE : dossier neuf sous le bloc-notes ; BASETEMP : dossier sous /dev/shm. Imprime le bilan en JSON (rien n'est écrit
  hors de COPIE et de BASETEMP ; le rapport recopie ce bilan).
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

DEPOT = Path(__file__).resolve().parents[6]
P = "src/controle_ia/barreau5_familles/"
L, S, R, LA = (f"{P}lecture_v1.py", f"{P}sondes_v1.py", f"{P}relecture_v1.py", "scripts/lancer_b5f_lecture_v1.sh")
EL, ES, ER, ELA = ("tests/test_barreau5_familles_lecture_v1.py", "tests/test_barreau5_familles_sondes_v1.py",
                   "tests/test_barreau5_familles_relecture_v1.py", "tests/test_lancer_b5f_lecture_v1.py")
RAPIDE = "not bout_en_bout and not produits_ecrits and not deplacement_moyen"
A_COPIER = ["src", "tests/conftest.py", EL, ES, ER, ELA, LA, "prereg/T0.6-organismes-config-7b-v1.json",
            "prereg/T0.6-organismes-config-7b-v1.json.sha256", "pyproject.toml", "docs/sources/invites-2606.08892-v1"]

MUTATIONS = [
    # --- lecture_v1 : épreuve exacte ---
    ("L01", L, "zéro compté pour « séparé »", "w_moins = somme_rangs_contre(d, lambda x: x <= 0)",
     "w_moins = somme_rangs_contre(d, lambda x: x < 0)", [EL]),
    ("L02", L, "zéro compté pour « contraire »", "w_plus = somme_rangs_contre(d, lambda x: x >= 0)",
     "w_plus = somme_rangs_contre(d, lambda x: x > 0)", [EL]),
    ("L03", L, "égalités rangées dans l'ordre favorable", "key=lambda i: (abs(d[i]), 1 if contre(d[i]) else 0))",
     "key=lambda i: (abs(d[i]), 0 if contre(d[i]) else 1))", [EL]),
    ("L04", L, "seuil strict (P(W ≤ w) < α)", "if Fraction(cumul, total) <= alpha:", "if Fraction(cumul, total) < alpha:", [EL]),
    ("L05", L, "99 % dès sept familles", "    if K >= 8:", "    if K >= 7:", [EL]),
    ("L06", L, "95 % dès cinq familles", "    if K >= 6:", "    if K >= 5:", [EL]),
    # --- lecture_v1 : épreuves ---
    ("L07", L, "E2a : q inversé", "c = math.sqrt(pj / ps)", "c = math.sqrt(ps / pj)", [EL]),
    ("L08", L, "E2a : facteurs des membres échangés", 'd["E2a"][f] = dec.statistique(sur, c) - dec.statistique(jum, 1.0 / c)',
     'd["E2a"][f] = dec.statistique(sur, 1.0 / c) - dec.statistique(jum, c)', [EL]),
    ("L09", L, "E2b : poussée non positive rend la famille absente (au lieu de c = 1)", 'd["E2b"][f] = t_sur - t_jum',
     "pass", [EL]),
    ("L10", L, "bornes du facteur [0,25 ; 4]", "BORNES_FACTEUR = (0.5, 2.0)", "BORNES_FACTEUR = (0.25, 4.0)", [EL]),
    ("L11", L, "mise à l'échelle du maximum (au lieu du maximum de la mise à l'échelle)",
     "return np.maximum.reduceat(s0 + c * (self.jetons[serie] - s0), self.debuts)",
     "return self.actions[SERIE_NU] + c * (self.actions[serie] - self.actions[SERIE_NU])", [EL]),
    ("L12", L, "σ_0 non lu (1)", "self.sigma0 = float(np.std(s0))", "self.sigma0 = 1.0", [EL]),
    ("L13", L, "E3 de signe inversé", 'd["E3"][f] = t_sur - t_jum', 'd["E3"][f] = t_jum - t_sur', [EL]),
    ("L14", L, "plis échangés", "return sorted(perm[:len(ids) // 2]), sorted(perm[len(ids) // 2:])",
     "return sorted(perm[len(ids) // 2:]), sorted(perm[:len(ids) // 2])", [EL]),
    ("L15", L, "Δ_app : borne basse au quantile 2,5 %", "np.quantile(tirages, 0.005)", "np.quantile(tirages, 0.025)", [EL]),
    ("L16", L, "séparation établie sans la borne basse", '"etablie": all(v > 0 for v in diff.values()) and bas > 0}',
     '"etablie": all(v > 0 for v in diff.values())}', [EL]),
    ("L17", L, "manipulation établie sans M3", '"etablie": M1["separe"] and M3["separe"]}', '"etablie": M1["separe"]}', [EL]),
    # --- lecture_v1 : issues ---
    ("L18", L, "issue C jamais rendue", 'if E3["contraire"]:', 'if False and E3["contraire"]:', [EL]),
    ("L19", L, "motif « saboteur non établi » omis", 'motifs.append("saboteur non établi")', "pass", [EL]),
    ("L20", L, "seuil de l'issue E et du diagnostic à 1", "SEUIL_EMPREINTE = 0.5", "SEUIL_EMPREINTE = 1.0", [EL]),
    ("L21", L, "issue E si une seule famille sous le seuil", "all(abs(v) < SEUIL_EMPREINTE", "any(abs(v) < SEUIL_EMPREINTE", [EL]),
    ("L22", L, "liste d'arrêt 13 à cinq familles", "if n_e3 < 6:", "if n_e3 < 5:", [EL]),
    ("L23", L, "niveau de S sans M1 ni M3", '"niveau": _niveau_min(manip["M1"], manip["M3"], E1, E2a, E2b, E3)',
     '"niveau": _niveau_min(E1, E2a, E2b, E3)', [EL]),
    ("L24", L, "π inversé (f/e)", "pi = {f: e_k[f] / f_k[f] for f in f_k}", "pi = {f: f_k[f] / e_k[f] for f in f_k}", [EL]),
    # --- lecture_v1 : gardes d'ouverture ---
    ("L25", L, "table repérée par son empreinte : garde ôtée", "if empreinte(p) == empreinte_engagement:", "if False:", [EL]),
    ("L26", L, "table repérée par sa forme : garde ôtée", "if _ressemble_a_une_table(x):", "if False:", [EL]),
    ("L27", L, "empreinte du programme non comparée", '_exiger(sha == reg["code_lecture"]["lecture"],', "_exiger(True,", [EL]),
    ("L28", L, "engagement avant les sorties de la formation admis",
     '_avant(lignes, "SORTIES-FORMATION-B5F", "ENGAGEMENT-B5F")', "pass", [EL]),
    ("L29", L, "engagement avant la relance admis", '_avant(lignes, "GO-RELANCE-FORMATION-B5F", "ENGAGEMENT-B5F")', "pass",
     [EL]),
    ("L30", L, "copie lue non contrôlée", '_exiger(str(nom_forme) in (p, f"{p}-r1"),', "_exiger(True,", [EL]),
    ("L31", L, "produits écrits non recalculés", "        exiger_produits_ecrits(prod, recalcule)", "        pass", [EL]),
    ("L32", L, "score d'action ≠ maximum par jeton admis",
     "_exiger(bool(np.array_equal(np.maximum.reduceat(tout, debuts), self.actions[nom])),", "_exiger(True,", [EL]),
    ("L33", L, "score manquant non vu (ensembles d'actions)", '_exiger(set(s["actions"]) == set(cles),', "_exiger(True,", [EL]),
    ("L34", L, "fichier hors de l'inventaire admis", "_exiger(not intrus,", "_exiger(True,", [EL]),
    # --- sondes_v1 ---
    ("S01", S, "adaptateur tenu à l'écart admis dans un apprentissage", "if _TENU.fullmatch(s) or _ANCRE.fullmatch(s):",
     "if False:", [ES]),
    ("S02", S, "score d'action par la moyenne des jetons", "a = score_action(sonde, acts, 0, acts.shape[0])",
     "a = float(np.mean(sj))", [ES]),
    ("S03", S, "régularisation 0,1", "L2 = 0.01", "L2 = 0.1", [ES]),
    ("S04", S, "sonde du pli k apprise sur le pli k",
     "            seqs, y = donnees_d_apprentissage(d, lecteur, cles, plis[1 - k])\n            try:",
     "            seqs, y = donnees_d_apprentissage(d, lecteur, cles, plis[k])\n            try:", [ES]),
    ("S05", S, "sonde en échec écrite « echec » dans le seul pli en échec", "            if echec:",
     "            if appris[(d.nom, k)] is None:", [ES]),
    ("S06", S, "contrôle carte-processeur à tolérance 1", "choisies, TOLERANCE_CARTE, EPOQUES)", "choisies, 1.0, EPOQUES)",
     [ES]),
    ("S07", S, "pli noté : actions des deux plis", "            if c.rsplit(\"/p\", 1)[0] not in taches:\n                continue",
     "            pass", [ES]),
    # --- relecture_v1 ---
    ("R01", R, "chemin : cas sain non exigé", "    if differentes or not egales:", "    if False:", [(ER, RAPIDE)]),
    ("R02", R, "chemin : artefact non exigé", "    if not art:", "    if False:", [(ER, RAPIDE)]),
    ("R03", R, "identité à dose 0 et artefact à dose 1 sautés",
     "    identite = controle_identite(modele, ids_controle, logits_base, {nom: lo.etat_lora(modele)})[nom]",
     '    identite = {"empreinte": lo.empreinte_adaptateurs(modele), "dose_0_identique": True, "dose_1_differente": True}',
     [(ER, RAPIDE)]),
    ("R04", R, "table dans l'arbre de la session : garde ôtée",
     "if empreinte_engagement is not None and empreinte(p) == empreinte_engagement:", "if False:", [(ER, RAPIDE)]),
    ("R05", R, "marche de la formation dans l'arbre : garde ôtée",
     'if p.is_dir() and re.fullmatch(r"[0-9]{8}-[0-9]{6}-b5f-formation-[1-7](?:-x1)?", p.name):', "if False:",
     [(ER, RAPIDE)]),
    ("R06", R, "référence git de la formation : garde ôtée",
     'if any("barreau5-familles-jumelles-v1-formation" in x for x in r.stdout.splitlines()):', "if False:", [(ER, RAPIDE)]),
    ("R07", R, "engagement non comparé à la création de l'instance",
     "    en.verifier_engagement_avant_lecture(None, creation, lignes=lignes)", "    pass", [(ER, RAPIDE)]),
    ("R08", R, "accord de lecture non comparé", 'if lignes.get("GO-LECTURE-B5F", {}).get("contenu") != config["go_id"]:',
     "if False:", [(ER, RAPIDE)]),
    ("R09", R, "nombre à virgule admis au journal", "        if isinstance(v, float):", "        if False:", [(ER, RAPIDE)]),
    ("R10", R, "sorties hors liste blanche admises", "            if _SORTIE.fullmatch(rel) is None:", "            if False:",
     [(ER, RAPIDE)]),
    ("R11", R, "copie lue des épisodes propres non contrôlée", '        lv.exiger_copie_lue(famille, str(x["famille"]), relance)',
     "        pass", [(ER, RAPIDE)]),
    ("R12", R, "fichier d'entrée non admis toléré (première garde ôtée ; la seconde, d'engagement_v1, reste)",
     "                raise GardeArret(f\"entrées de lecture : fichier non admis {rel} (liste d'arrêt, point 8) : refus, nœud\")",
     "                continue", [(ER, RAPIDE)]),
    ("R13", R, "δ̄ et normes sur la simple précision (et non sur la demi-précision gardée)",
     "                    a16 = {k: demi(acts[k]) for k in couches}",
     "                    a16 = {k: np.asarray(acts[k], dtype=np.float32) for k in couches}", [ER]),
    ("R14", R, "divergence sans repasser à la dose 0 (loi du modèle nu non lue)",
     "                    lo.fixer_dose(modele, 0.0)\n                    l0 = logits_aux_positions(modele, ids, pos)",
     "                    l0 = logits_aux_positions(modele, ids, pos)", [ER]),
    ("R15", R, "direction commune tirée de tous les saboteurs, tenus à l'écart compris",
     'saboteurs = sorted(n for n in dep_plan if re.fullmatch(r"A[1-3]-saboteur", n))',
     'saboteurs = sorted(n for n in dep_plan if n.endswith("-saboteur") or n.startswith("X-"))', [ER]),
    # --- lanceur ---
    ("LA1", LA, "config sans accord admise", '[ -n "${GO_ID:-}" ] || { echo "B5F REFUS : GO_ID absent de l\'environnement (aucune marche sans accord)" >&2; exit 2; }',
     ":", [ELA]),
]


def copier(copie: Path) -> None:
    if copie.exists():
        raise SystemExit(f"{copie} existe déjà : une seule copie de travail, neuve")
    for rel in A_COPIER:
        s, d = DEPOT / rel, copie / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        if s.is_dir():
            shutil.copytree(s, d, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy2(s, d)


def jouer(copie: Path, base: Path, nom: str, essais) -> dict:
    cibles = []
    for e in essais:
        if isinstance(e, tuple):
            cibles += [e[0], "-k", e[1]]
        else:
            cibles.append(e)
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": str(copie / "src"), "TMPDIR": "/dev/shm",
           "PYTHONDONTWRITEBYTECODE": "1", "HOME": os.environ.get("HOME", "/root")}
    debut = time.time()
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-x", "--basetemp",
                        str(base / nom), *cibles], cwd=str(copie), env=env, capture_output=True, text=True)
    lignes = [x for x in r.stdout.splitlines() if x.strip() and not x.startswith("PROGRES")]
    echec = [x for x in lignes if x.startswith("FAILED") or x.startswith("ERROR")]
    return {"code": r.returncode, "duree_s": round(time.time() - debut, 1), "fin": lignes[-1] if lignes else "",
            "premier_echec": echec[0] if echec else None}


def main(argv: list[str]) -> int:
    copie, base = Path(argv[0]), Path(argv[1])
    choix = set(argv[2:])
    copier(copie)
    bilan = {"temoins": {}, "mutations": []}
    for essais in ([EL], [ES], [(ER, RAPIDE)], [ELA]):
        cle = " ".join(e if isinstance(e, str) else f"{e[0]} -k {e[1]!r}" for e in essais)
        bilan["temoins"][cle] = jouer(copie, base, f"temoin-{len(bilan['temoins'])}", essais)
    for mid, fichier, quoi, avant, apres, essais in MUTATIONS:
        if choix and mid not in choix:
            continue
        origine = (DEPOT / fichier).read_text(encoding="utf-8")
        n = origine.count(avant)
        x = {"id": mid, "fichier": fichier, "defaut": quoi}
        if n != 1:
            x.update({"etat": "introuvable", "occurrences": n})
            bilan["mutations"].append(x)
            continue
        cible = copie / fichier
        cible.write_text(origine.replace(avant, apres), encoding="utf-8")
        try:
            r = jouer(copie, base, mid, essais)
        finally:
            cible.write_text(origine, encoding="utf-8")
        x.update({"etat": "attrapée" if r["code"] != 0 else "MANQUÉE", **r})
        bilan["mutations"].append(x)
        print(f"{mid} {x['etat']} ({r['duree_s']} s)", file=sys.stderr, flush=True)
    joues = [m for m in bilan["mutations"] if m["etat"] != "introuvable"]
    bilan["compte"] = {"jouees": len(joues), "attrapees": sum(m["etat"] == "attrapée" for m in joues),
                       "manquees": [m["id"] for m in joues if m["etat"] == "MANQUÉE"],
                       "introuvables": [m["id"] for m in bilan["mutations"] if m["etat"] == "introuvable"]}
    print(json.dumps(bilan, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
