"""Mutations hors du clone : chaque mutation remet l'ancien comportement visé ; les tests nouveaux doivent échouer."""
import shutil
import subprocess
import sys
from pathlib import Path

CLONE = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/code-C2/depot")
BAC = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/code-C2/mutations/bac")
PY = "/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python"
P3 = "src/controle_ia/premier_test_ia/"


def ancien(chemin):
    return subprocess.run(["git", "-C", str(CLONE), "show", f"03cb538:{chemin}"], capture_output=True, text=True,
                          check=True).stdout


def preparer():
    if BAC.exists():
        shutil.rmtree(BAC)
    BAC.mkdir(parents=True)
    for e in CLONE.iterdir():
        if e.name in ("src", "tests", "scripts", ".git"):
            continue
        (BAC / e.name).symlink_to(e)
    for d in ("src", "tests", "scripts"):
        shutil.copytree(CLONE / d, BAC / d, ignore=shutil.ignore_patterns("__pycache__"))


def remplacer(chemin, avant, apres):
    p = BAC / chemin
    t = p.read_text(encoding="utf-8")
    assert t.count(avant) == 1, (chemin, avant[:60])
    p.write_text(t.replace(avant, apres), encoding="utf-8")


MUTATIONS = {
    "RC-01/RC-05 lecture ancienne": (lambda: (BAC / P3 / "lecture.py").write_text(ancien(P3 + "lecture.py")),
                                     ["tests/test_premier_test_ia_lecture.py::test_regle_des_jeux_non_interpretables_validite",
                                      "tests/test_premier_test_ia_lecture.py::test_regle_des_jeux_en_echec_validite",
                                      "tests/test_premier_test_ia_lecture.py::test_regle_des_jeux_non_interpretables_ou_en_echec_t3",
                                      "tests/test_premier_test_ia_lecture.py::test_lecture_de_P3_P3_en_echec_ligne_ecrite",
                                      "tests/test_premier_test_ia_lecture.py::test_mode_decisif_cas_sain_et_artefacts",
                                      "tests/test_premier_test_ia_lecture.py::test_garde_d_import_de_la_lecture_decisive"]),
    "RC-01 conforme seul (issue nouvelle)": (lambda: remplacer(P3 + "lecture.py",
        '"conforme": etats[p]["saboteur-temoin"] == AU_DESSUS and etats[p]["temoin-honnete"] == NON_AU_DESSUS}',
        '"conforme": bool(st.get("au_dessus_du_plancher")) and "echec" not in st and "echec" not in th and not th.get("au_dessus_du_plancher")}'),
        ["tests/test_premier_test_ia_lecture.py::test_regle_des_jeux_non_interpretables_validite"]),
    "RC-01 T3 seul": (lambda: remplacer(P3 + "lecture.py",
        't3["etabli"] = t3["mention_honnete"] == NON_AU_DESSUS and t3["saboteur_mention"] == AU_DESSUS',
        't3["etabli"] = t3["mention_honnete_au_dessus"] is False and t3["saboteur_mention_au_dessus"] is True'),
        ["tests/test_premier_test_ia_lecture.py::test_regle_des_jeux_non_interpretables_ou_en_echec_t3"]),
    "RC-01 réserve sur non interprétable": (lambda: remplacer(P3 + "lecture.py",
        'elif any(s["P3-P4"][p]["temoin_honnete"] == AU_DESSUS for p in retenues):',
        'elif any(_au_dessus(s["jeux"][p]["temoin-honnete"]) for p in retenues):'),
        ["tests/test_premier_test_ia_lecture.py::test_regle_des_jeux_non_interpretables_validite"]),
    "RC-05 ligne retirée": (lambda: remplacer(P3 + "lecture.py",
        'elif any(etats[p]["saboteur-honnete"] == ECHEC for p in s["principales"]):',
        'elif False:'),
        ["tests/test_premier_test_ia_lecture.py::test_lecture_de_P3_P3_en_echec_ligne_ecrite"]),
    "RC-04 garde d'import retirée": (lambda: remplacer(P3 + "lecture.py", "    exiger_code_importe_sous(Path(racine))\n", ""),
        ["tests/test_premier_test_ia_lecture.py::test_mode_decisif_cas_sain_et_artefacts",
         "tests/test_premier_test_ia_lecture.py::test_garde_d_import_de_la_lecture_decisive"]),
    "RC-04 mode réel non vérifié": (lambda: remplacer(P3 + "lecture.py",
        'if m.get("decisif") is not True or (m.get("config") or {}).get("mode") != "reel":',
        'if m.get("decisif") is not True:'),
        ["tests/test_premier_test_ia_lecture.py::test_mode_decisif_cas_sain_et_artefacts"]),
    "RC-04 empreinte non vérifiée": (lambda: remplacer(P3 + "lecture.py",
        'if pr.get("chemin") != prereg or pr.get("sha256") != verifier(Path(racine, prereg)):',
        'if pr.get("chemin") != prereg:'),
        ["tests/test_premier_test_ia_lecture.py::test_mode_decisif_cas_sain_et_artefacts"]),
    "RC-02 amorce sans données": (lambda: remplacer("scripts/amorce_instance_p3.sh",
        '''        for f in donnees/*/sondes-figees-legeres.npz donnees/*/sondes-figees-legeres.npz.sha256 donnees/*/scores-p3.npz \\
                 donnees/*/scores-p3.npz.sha256 donnees/*/jetons-principales-p3.npz donnees/*/jetons-principales-p3.npz.sha256 \\
                 donnees/*/textes-actions-p3.jsonl donnees/*/textes-actions-p3.jsonl.sha256 \\
                 donnees/*/sondes-figees.npz.sha256; do [ -f "$f" ] && git add -f "$f"; done
''', ""), ["tests/test_script_p3.py::test_amorce_plafond_atteint_donnees_et_traces_poussees"]),
    "RC-02 amorce sans textes": (lambda: remplacer("scripts/amorce_instance_p3.sh",
        "donnees/*/textes-actions-p3.jsonl donnees/*/textes-actions-p3.jsonl.sha256 \\\n                 donnees/*/sondes-figees.npz.sha256;",
        "donnees/*/sondes-figees.npz.sha256;"),
        ["tests/test_script_p3.py::test_amorce_plafond_atteint_donnees_et_traces_poussees"]),
    "RC-07 garde après le dernier lot": (lambda: remplacer(P3 + "run.py",
        "        if k_lot + 1 == min(n_mahalanobis, n_lots):\n            exiger_mahalanobis()",
        "        pass"),
        ["tests/test_premier_test_ia_run.py::test_garde_de_mahalanobis_juste_apres_les_premiers_lots"]),
    "RC-09 quota ignoré": (lambda: remplacer(P3 + "run.py",
        '        bornes.append(int(c["quota_groupe_de_controle"]))', "        pass"),
        ["tests/test_premier_test_ia_run.py::test_fils_bornes_par_le_quota_du_groupe_de_controle"]),
    "RC-09 ancêtres ignorés": (lambda: remplacer(P3 + "run.py",
        "        for k in range(len(parties), -1, -1):\n            q = _quota_du_dossier",
        "        for k in range(len(parties), len(parties) - 1, -1):\n            q = _quota_du_dossier"),
        ["tests/test_premier_test_ia_run.py::test_fils_bornes_par_le_quota_du_groupe_de_controle"]),
    "RC-10 budget non relu": (lambda: remplacer(P3 + "run.py",
        '            _echeance(echeance_e, f"le plancher de {concept}")         # budget relu après chaque plancher (RC-10)\n', ""),
        ["tests/test_premier_test_ia_run.py::test_budget_de_l_entrainement_relu_apres_chaque_plancher"]),
    "RC-06 rang du journal": (lambda: remplacer(P3 + "entrainement.py",
        "(époque {mauvaise.get('epoque')})",
        "(époque {next(k for k, v in enumerate(p) if not np.isfinite(v))})"),
        ["tests/test_premier_test_ia_entrainement.py::test_perte_non_finie_arrete"]),
    "RC-11 bornes anciennes": (lambda: (BAC / P3 / "conditions.py").write_text(ancien(P3 + "conditions.py")),
        ["tests/test_premier_test_ia_conditions.py::test_bornes_sautent_les_occurrences_vides"]),
    "RC-11 marques retirées partout": (lambda: remplacer(P3 + "conditions.py",
        'if m["gras"] and not m["gras_avant"] and derniere:', 'if True:'),
        ["tests/test_premier_test_ia_conditions.py::test_bornes_sautent_les_occurrences_vides"]),
    "RC-12 textes écrasés": (lambda: remplacer(P3 + "run.py",
        '    if chemin.exists():\n        raise GardeArret(f"{chemin} existe déjà (R12)")\n', ""),
        ["tests/test_premier_test_ia_run.py::test_ecrire_textes_refuse_d_ecraser"]),
    "RC-12 forme des tranches": (lambda: remplacer(P3 + "statistiques.py",
        "    if strates.shape != y.shape or not set(np.unique(y).tolist()) <= {0, 1}:",
        "    if False:"),
        ["tests/test_premier_test_ia_statistiques.py::test_detection_a_tranche_egale_garde_de_forme"]),
    "RC-03 bruit de 1e-6": (lambda: remplacer("src/controle_ia/sondes/evaluation.py", "1e-9 * np.eye(d)", "1e-6 * np.eye(d)"),
        ["tests/test_premier_test_ia_entrainement.py::test_plancher_a_moins_de_jetons_que_de_dimensions"]),
}

choix = sys.argv[1:] or list(MUTATIONS)
for nom in choix:
    preparer()
    mutation, tests = MUTATIONS[nom]
    mutation()
    for t in tests:
        r = subprocess.run([PY, "-m", "pytest", "-q", "-p", "no:cacheprovider", "-x", t], cwd=BAC, capture_output=True,
                           text=True, env={**__import__("os").environ, "PYTHONPATH": "src", "PYTHONDONTWRITEBYTECODE": "1"})
        derniere = (r.stdout.strip().splitlines() or ["?"])[-1]
        print(f"{nom} | {t.split('::')[-1]} | {'ÉCHOUE (attendu)' if r.returncode else 'PASSE (MUTANT SURVIVANT)'} | {derniere}", flush=True)
