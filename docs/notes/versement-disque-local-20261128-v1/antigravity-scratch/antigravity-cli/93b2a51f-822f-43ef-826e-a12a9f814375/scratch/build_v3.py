from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch\wt-dr-v3")


def read_lf(rel: str) -> str:
    data = (ROOT / rel).read_bytes()
    assert b"\r" not in data, f"CR found in source {rel}"
    return data.decode("utf-8")


def write_lf_and_sha(rel: str, text: str) -> str:
    assert "\r" not in text, f"CR found in output {rel}"
    if not text.endswith("\n"):
        text += "\n"
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    raw = text.encode("utf-8")
    p.write_bytes(raw)
    sha = hashlib.sha256(raw).hexdigest()
    sha_path = Path(str(p) + ".sha256")
    sha_path.write_bytes(f"{sha}  {p.name}\n".encode("utf-8"))
    return sha


def replace_once(src: str, old: str, new: str, label: str) -> str:
    n = src.count(old)
    assert n == 1, f"{label}: expected 1 occurrence of {old!r}, got {n}"
    return src.replace(old, new, 1)


# 1. src/controle_ia/dose_reponse/controles_v3.py
c2 = read_lf("src/controle_ia/dose_reponse/controles_v2.py")
c3 = replace_once(
    c2,
    '"""[v2, après la contre-lecture 1',
    '"""[v3 (écart matériel minimal autorisé par Lazar : GO-2026-11-25-01, R-5397) ; nom neuf, R12 : `controles_v2.py` reste\n'
    'tel quel. Seul changement fonctionnel : `stockage_max_usd_h` passe de `0.08` à `0.10` USD de l\'heure dans `OFFRE["offre"]`\n'
    'et dans `configuration()` ; rien d\'autre.]\n'
    '[v2, après la contre-lecture 1',
    "controles_v3 header",
)
c3 = replace_once(
    c3,
    "  stockage au plus 0,08 USD de l'heure, téléchargement au plus 0,05 USD par Go) et plafond (90 USD) de la configuration ;",
    "  stockage au plus 0,10 USD de l'heure, téléchargement au plus 0,05 USD par Go) et plafond (90 USD) de la configuration ;",
    "controles_v3 docstring 0,10",
)
c3 = replace_once(
    c3,
    '                   "stockage_max_usd_h": 0.08, "telechargement_max_usd_go": 0.05}}',
    '                   "stockage_max_usd_h": 0.10, "telechargement_max_usd_go": 0.05}}',
    "controles_v3 OFFRE",
)
c3 = replace_once(
    c3,
    '                                "memoire_vive_min_mo": 128000, "stockage_max_usd_h": 0.08, "telechargement_go_prevu": 40,',
    '                                "memoire_vive_min_mo": 128000, "stockage_max_usd_h": 0.10, "telechargement_go_prevu": 40,',
    "controles_v3 configuration()",
)
assert "0.08" not in c3.split('"""', 2)[2], "0.08 still present in controles_v3 body"
sha_c3 = write_lf_and_sha("src/controle_ia/dose_reponse/controles_v3.py", c3)
print("controles_v3.py", sha_c3)

# 2. src/controle_ia/dose_reponse/course_v3.py
co2 = read_lf("src/controle_ia/dose_reponse/course_v2.py")
co3 = replace_once(
    co2,
    '"""[v2, après la contre-lecture 1',
    '"""[v3 (écart matériel minimal autorisé par Lazar : GO-2026-11-25-01, R-5397) ; nom neuf, R12 : `course_v2.py` reste\n'
    'tel quel. Changent seulement : import de `controles_v3` (`stockage_max_usd_h` relevé de `0.08` à `0.10` USD/h) et\n'
    '`COMMANDE` (`controle_ia.dose_reponse.course_v3`) ; rien d\'autre.]\n'
    '[v2, après la contre-lecture 1',
    "course_v3 header",
)
co3 = replace_once(co3, "from . import controles_v2 as ct", "from . import controles_v3 as ct", "course_v3 import")
co3 = replace_once(
    co3,
    'COMMANDE = "python -m controle_ia.dose_reponse.course_v2"',
    'COMMANDE = "python -m controle_ia.dose_reponse.course_v3"',
    "course_v3 COMMANDE",
)
sha_co3 = write_lf_and_sha("src/controle_ia/dose_reponse/course_v3.py", co3)
print("course_v3.py", sha_co3)

# 3. scripts/ecrire_configuration_dose_reponse_v3.py
ec2 = read_lf("scripts/ecrire_configuration_dose_reponse_v2.py")
ec3 = replace_once(
    ec2,
    '"""[v2, après la contre-lecture 1',
    '"""[v3 (écart matériel minimal autorisé par Lazar : GO-2026-11-25-01, R-5397) ; nom neuf, R12 : la v2 reste telle quelle.\n'
    'Changent seulement : import de `controles_v3` (`stockage_max_usd_h` relevé de `0.08` à `0.10` USD/h) et sortie par défaut\n'
    '`prereg/T0.6-dose-reponse-configuration-course-v2.json` (R12) ; rien d\'autre.]\n'
    '[v2, après la contre-lecture 1',
    "ecrire_config header",
)
ec3 = replace_once(
    ec3,
    "Vérifiée par `controles_v2.exiger_config` avant écriture ; R12.",
    "Vérifiée par `controles_v3.exiger_config` avant écriture ; R12.",
    "ecrire_config doc exiger_config",
)
ec3 = replace_once(
    ec3,
    "PYTHONPATH=src python scripts/ecrire_configuration_dose_reponse_v2.py",
    "PYTHONPATH=src python scripts/ecrire_configuration_dose_reponse_v3.py",
    "ecrire_config usage",
)
ec3 = replace_once(
    ec3,
    "from controle_ia.dose_reponse import controles_v2 as ct",
    "from controle_ia.dose_reponse import controles_v3 as ct",
    "ecrire_config import",
)
ec3 = replace_once(
    ec3,
    'SORTIE = "prereg/T0.6-dose-reponse-configuration-course-v1.json"',
    'SORTIE = "prereg/T0.6-dose-reponse-configuration-course-v2.json"',
    "ecrire_config SORTIE",
)
sha_ec3 = write_lf_and_sha("scripts/ecrire_configuration_dose_reponse_v3.py", ec3)
print("ecrire_configuration_dose_reponse_v3.py", sha_ec3)

# 4. tests/test_dose_reponse_v3.py
tv2 = read_lf("tests/test_dose_reponse_v2.py")
tv3 = replace_once(
    tv2,
    '"""[v2, après la contre-lecture 1 : mêmes essais que la v1, sur les modules v2 (`controles_v2`, `course_v2`, `lecture_v2`,\n'
    'scripts v2), plus les essais des corrections CL-02 à CL-11 et des trous d\'essais de CL-10.]',
    '"""[v3 (écart matériel minimal GO-2026-11-25-01, R-5397 : `stockage_max_usd_h` relevé de `0.08` à `0.10` USD/h) ; nom\n'
    'neuf, R12 : `test_dose_reponse_v2.py` reste tel quel. Mêmes essais sur `controles_v3`, `course_v3`, `lecture_v2`,\n'
    '`amorce_instance_dose_reponse_v4.sh` et `lancer_dose_reponse_v4.sh`, plus les essais explicites de borne R5 sur\n'
    '`stockage_max_usd_h`.]\n'
    '[v2, après la contre-lecture 1 : mêmes essais que la v1, sur les modules v2 (`controles_v2`, `course_v2`, `lecture_v2`,\n'
    'scripts v2), plus les essais des corrections CL-02 à CL-11 et des trous d\'essais de CL-10.]',
    "test_v3 header",
)
tv3 = replace_once(
    tv3,
    "from controle_ia.dose_reponse import controles_v2 as ct  # noqa: E402",
    "from controle_ia.dose_reponse import controles_v3 as ct  # noqa: E402",
    "test_v3 import ct",
)
tv3 = replace_once(
    tv3,
    "from controle_ia.dose_reponse import course_v2 as co  # noqa: E402",
    "from controle_ia.dose_reponse import course_v3 as co  # noqa: E402",
    "test_v3 import co",
)
tv3 = replace_once(
    tv3,
    'scripts/amorce_instance_dose_reponse_v2.sh',
    'scripts/amorce_instance_dose_reponse_v4.sh',
    "test_v3 amorce v4",
)
tv3 = replace_once(
    tv3,
    'scripts/lancer_dose_reponse_v2.sh',
    'scripts/lancer_dose_reponse_v4.sh',
    "test_v3 lanceur v4",
)

extra_tests = '''

# --- écart matériel minimal GO-2026-11-25-01 / R-5397 : bornes de stockage_max_usd_h = 0.10 (R5) -----------------------

def test_stockage_max_010_offre_lue_et_config():
    c = _config_reelle()
    assert ct.OFFRE["offre"]["stockage_max_usd_h"] == 0.10
    assert c["lancement"]["offre"]["stockage_max_usd_h"] == 0.10
    assert co.COMMANDE == "python -m controle_ia.dose_reponse.course_v3"
    ct.exiger_config(c, RACINE)
    bonne = {"gpu_name": "A100_SXM4", "num_gpus": 1, "gpu_ram": 81920, "cpu_ram": 129000, "cpu_cores_effective": 16,
             "disk_space": 300, "dph_total": 1.25, "storage_total_cost": 0.0822, "inet_down_cost": 0.01}
    assert ct.exiger_offre_lue(bonne, c)["conforme"]
    assert ct.exiger_offre_lue({**bonne, "storage_total_cost": 0.10}, c)["conforme"]
    with pytest.raises(GardeArret, match="stockage"):
        ct.exiger_offre_lue({**bonne, "storage_total_cost": 0.1001}, c)
    # R5 : une configuration portant l'ancienne borne (0.08) ou au-delà (0.11) est refusée
    for val in (0.08, 0.11):
        c2 = json.loads(json.dumps(c))
        c2["lancement"]["offre"]["stockage_max_usd_h"] = val
        with pytest.raises(GardeArret, match="reconstruite"):
            ct.exiger_config(c2, RACINE)
    c_trop = json.loads(json.dumps(c))
    c_trop["lancement"]["offre"]["stockage_max_usd_h"] = 0.11
    with pytest.raises(GardeArret, match="stockage_max_usd_h"):
        ct.exiger_offre(c_trop)


def test_stockage_max_010_chaine_session(tmp_path):
    import io
    from contextlib import redirect_stdout

    from controle_ia.lancement_t08 import session_v1 as s
    (tmp_path / "vue.json").write_text(json.dumps(s.vue_offre(_config_reelle())), encoding="utf-8")
    bonne = {"id": 8, "machine_id": 80, "gpu_name": "A100 SXM4", "num_gpus": 1, "gpu_ram": 81920, "cpu_ram": 129000,
             "cpu_cores_effective": 16, "disk_space": 300, "dph_total": 1.25, "storage_total_cost": 0.0822, "inet_down_cost": 0.01,
             "reliability": 0.99, "cuda_max_good": 13.0, "inet_down": 1000}

    def choisir(o):
        (tmp_path / "offres.json").write_text(json.dumps([o]), encoding="utf-8")
        f = io.StringIO()
        with redirect_stdout(f):
            code = s.main(["choisir", str(tmp_path / "offres.json"), str(tmp_path / "vue.json"), "course", ""])
        return code, f.getvalue()
    assert choisir(bonne)[0] == 0, choisir(bonne)[1]
    assert choisir({**bonne, "storage_total_cost": 0.10})[0] == 0
    assert choisir({**bonne, "storage_total_cost": 0.1001})[0] != 0
'''

tv3 = tv3.rstrip("\n") + "\n" + extra_tests.lstrip("\n")
sha_tv3 = write_lf_and_sha("tests/test_dose_reponse_v3.py", tv3)
print("test_dose_reponse_v3.py", sha_tv3)

# 5. tests/test_dose_reponse_amorce_v4.py
ta3 = read_lf("tests/test_dose_reponse_amorce_v3.py")
ta4 = replace_once(
    ta3,
    '"""Essais de l\'amorce v3 de la course de dose–réponse (extraction du texte de désignation pour le critère 3 sur l\'instance)\n'
    'et de `dose_reponse.extraction_v1` (R5 : cas sain et artefact). Aucune donnée d\'organisme, aucun texte privé : fichiers\n'
    'factices dans un dépôt git temporaire."""',
    '"""[v4 (écart matériel minimal GO-2026-11-25-01, R-5397) ; nom neuf, R12 : `test_dose_reponse_amorce_v3.py` reste tel\n'
    'quel.]\n'
    'Essais de l\'amorce v4 et du lanceur v4 de la course de dose–réponse (`controles_v3`, extraction du texte de désignation\n'
    'pour le critère 3 sur l\'instance, `dose_reponse.extraction_v1` ; R5 : cas sain et artefact). Aucune donnée d\'organisme,\n'
    'aucun texte privé : fichiers factices dans un dépôt git temporaire."""',
    "test_amorce_v4 header",
)
ta4 = replace_once(
    ta4,
    "from controle_ia.dose_reponse import controles_v2 as ct",
    "from controle_ia.dose_reponse import controles_v3 as ct",
    "test_amorce_v4 import ct",
)
ta4 = replace_once(
    ta4,
    "def test_amorce_v3_extrait_la_designation_et_la_garde_passe(tmp_path):",
    "def test_amorce_v4_extrait_la_designation_et_la_garde_passe(tmp_path):",
    "test_amorce_v4 fn1",
)
ta4 = replace_once(
    ta4,
    '    # cas sain : configuration désignée, amorce v3\n'
    '    _, c2 = _depot(tmp_path / "b", sain)\n'
    '    r = _extraire(c2, "amorce_instance_dose_reponse_v3.sh")',
    '    # cas sain : configuration désignée, amorce v4\n'
    '    _, c2 = _depot(tmp_path / "b", sain)\n'
    '    r = _extraire(c2, "amorce_instance_dose_reponse_v4.sh")',
    "test_amorce_v4 fn1 call",
)
ta4 = replace_once(
    ta4,
    'def test_amorce_v3_course_sans_designation(tmp_path):\n'
    '    _, c = _depot(tmp_path, None)\n'
    '    r = _extraire(c, "amorce_instance_dose_reponse_v3.sh")',
    'def test_amorce_v4_course_sans_designation(tmp_path):\n'
    '    _, c = _depot(tmp_path, None)\n'
    '    r = _extraire(c, "amorce_instance_dose_reponse_v4.sh")',
    "test_amorce_v4 fn2",
)
ta4 = replace_once(
    ta4,
    'def test_amorce_v3_refuse_une_configuration_illisible(tmp_path):\n'
    '    _, c = _depot(tmp_path, {"chemin": "/etc/passwd"})\n'
    '    r = _extraire(c, "amorce_instance_dose_reponse_v3.sh")',
    'def test_amorce_v4_refuse_une_configuration_illisible(tmp_path):\n'
    '    _, c = _depot(tmp_path, {"chemin": "/etc/passwd"})\n'
    '    r = _extraire(c, "amorce_instance_dose_reponse_v4.sh")',
    "test_amorce_v4 fn3",
)
ta4 = replace_once(
    ta4,
    'def test_lanceur_v3_cite_l_amorce_v3():\n'
    '    t = (RACINE / "scripts/lancer_dose_reponse_v3.sh").read_text(encoding="utf-8")\n'
    '    assert "\\nA=scripts/amorce_instance_dose_reponse_v3.sh\\n" in t and "lancer_dose_reponse_v2.sh" not in t',
    'def test_lanceur_v4_cite_l_amorce_v4_et_controles_v3():\n'
    '    t = (RACINE / "scripts/lancer_dose_reponse_v4.sh").read_text(encoding="utf-8")\n'
    '    assert "\\nA=scripts/amorce_instance_dose_reponse_v4.sh\\n" in t\n'
    '    assert \'\\nCONFIG="${DR_CONFIG:-prereg/T0.6-dose-reponse-configuration-course-v2.json}"\\n\' in t\n'
    '    assert "from controle_ia.dose_reponse import controles_v3 as ct" in t\n'
    '    assert "lancer_dose_reponse_v3.sh" not in t and "lancer_dose_reponse_v2.sh" not in t\n'
    '    a = (RACINE / "scripts/amorce_instance_dose_reponse_v4.sh").read_text(encoding="utf-8")\n'
    '    assert "AMORCE DR v4 DEMARRAGE" in a\n'
    '    assert "from controle_ia.dose_reponse import controles_v3 as ct" in a\n'
    '    assert "python -m controle_ia.dose_reponse.course_v3" in a\n'
    '    assert \'LISTE_TESTS="scripts/tests-cibles-dose-reponse-v4.txt"\' in a',
    "test_amorce_v4 fn4",
)
sha_ta4 = write_lf_and_sha("tests/test_dose_reponse_amorce_v4.py", ta4)
print("test_dose_reponse_amorce_v4.py", sha_ta4)

# 6. scripts/tests-cibles-dose-reponse-v4.txt
tc4 = "tests/test_dose_reponse_v3.py\ntests/test_dose_reponse_amorce_v4.py\n"
sha_tc4 = write_lf_and_sha("scripts/tests-cibles-dose-reponse-v4.txt", tc4)
print("tests-cibles-dose-reponse-v4.txt", sha_tc4)

# 8. scripts/lancer_dose_reponse_v4.sh
l3 = read_lf("scripts/lancer_dose_reponse_v3.sh")
l4 = replace_once(
    l3,
    "#!/usr/bin/env bash\n# [v3 ; nom neuf, R12 : la v2 reste telle quelle.",
    "#!/usr/bin/env bash\n"
    "# [v4 (écart matériel minimal autorisé par Lazar : GO-2026-11-25-01, R-5397) ; nom neuf, R12 : la v3 reste telle quelle.\n"
    "# Changent seulement : l'amorce citée (`scripts/amorce_instance_dose_reponse_v4.sh`), la configuration par défaut alignée\n"
    "# (`prereg/T0.6-dose-reponse-configuration-course-v2.json`, R12), `controles_v3 as ct` (`stockage_max_usd_h` relevé de\n"
    "# `0.08` à `0.10` USD/h) et la bannière v4 ; rien d'autre.]\n"
    "# [v3 ; nom neuf, R12 : la v2 reste telle quelle.",
    "lancer_v4 header",
)
for old, new, lbl in [
    ("bash scripts/lancer_dose_reponse_v3.sh controles", "bash scripts/lancer_dose_reponse_v4.sh controles", "usage controles"),
    ("bash scripts/lancer_dose_reponse_v3.sh creation", "bash scripts/lancer_dose_reponse_v4.sh creation", "usage creation"),
    ("bash scripts/lancer_dose_reponse_v3.sh apres-creation", "bash scripts/lancer_dose_reponse_v4.sh apres-creation", "usage apres"),
    ("bash scripts/lancer_dose_reponse_v3.sh surveillance DOSSIER", "bash scripts/lancer_dose_reponse_v4.sh surveillance DOSSIER", "dummy"),
]:
    if lbl == "dummy":
        continue
    l4 = replace_once(l4, old, new, lbl)
l4 = replace_once(l4, "bash scripts/lancer_dose_reponse_v3.sh surveillance ID", "bash scripts/lancer_dose_reponse_v4.sh surveillance ID", "usage surv")
l4 = replace_once(l4, "bash scripts/lancer_dose_reponse_v3.sh --verifier-go-seulement", "bash scripts/lancer_dose_reponse_v4.sh --verifier-go-seulement", "usage verif")
l4 = replace_once(l4, "\nA=scripts/amorce_instance_dose_reponse_v3.sh\n", "\nA=scripts/amorce_instance_dose_reponse_v4.sh\n", "lancer_v4 A")
l4 = replace_once(
    l4,
    '\nCONFIG="${DR_CONFIG:-prereg/T0.6-dose-reponse-configuration-course-v1.json}"\n',
    '\nCONFIG="${DR_CONFIG:-prereg/T0.6-dose-reponse-configuration-course-v2.json}"\n',
    "lancer_v4 CONFIG",
)
l4 = replace_once(
    l4,
    "from controle_ia.dose_reponse import controles_v2 as ct",
    "from controle_ia.dose_reponse import controles_v3 as ct",
    "lancer_v4 ct",
)
l4 = replace_once(l4, "controles dose-reponse v3 %s", "controles dose-reponse v4 %s", "lancer_v4 controles banner")
l4 = replace_once(
    l4,
    "bash $DEPOT/scripts/lancer_dose_reponse_v3.sh apres-creation",
    "bash $DEPOT/scripts/lancer_dose_reponse_v4.sh apres-creation",
    "lancer_v4 cmd apres",
)
l4 = replace_once(
    l4,
    "bash scripts/lancer_dose_reponse_v3.sh surveillance $ID $D",
    "bash scripts/lancer_dose_reponse_v4.sh surveillance $ID $D",
    "lancer_v4 echo surv",
)
l4 = replace_once(
    l4,
    "bash $DEPOT/scripts/lancer_dose_reponse_v3.sh creation auto course",
    "bash $DEPOT/scripts/lancer_dose_reponse_v4.sh creation auto course",
    "lancer_v4 echo creation",
)
l4 = replace_once(l4, "surveillance dose-réponse v3 de $ID", "surveillance dose-réponse v4 de $ID", "lancer_v4 surv banner")
assert "lancer_dose_reponse_v3.sh" not in l4, "lancer_dose_reponse_v3.sh still in l4"
sha_l4 = write_lf_and_sha("scripts/lancer_dose_reponse_v4.sh", l4)
print("lancer_dose_reponse_v4.sh", sha_l4)
