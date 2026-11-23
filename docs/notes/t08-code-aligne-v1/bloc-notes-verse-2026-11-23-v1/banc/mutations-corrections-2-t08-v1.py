"""Banc de mutations de la seconde passe de corrections de T0.8 (modèle A) : chaque garde neuve ou appel sans essai
(VCT8-01 à VCT8-07, M35, M38, M61) est retiré ou affaibli dans une copie jetable ; l'essai nommé doit échouer.
Copies sous le bloc-notes ; l'arbre n'est jamais écrit. Usage : python mutations_corrections2.py ARBRE BLOC"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ARBRE, BLOC = Path(sys.argv[1]), Path(sys.argv[2])
PY = "/home/user/controle-ia-travail/.venv/bin/python"
T = "src/controle_ia/t08/"
L, E, TD, EJ, C = T + "lecture_v1.py", T + "entrees_v1.py", T + "temoin_distille_v1.py", T + "essai_jouet_v1.py", T + "course_v1.py"
G, LC = "tests/test_t08_gardes_corrections_v1.py", "tests/test_t08_lecture_course_v1.py"

MUTATIONS = [
    ("V01", "VCT8-01", "réserve « troncature » décidée sur la somme (ancien code)", L,
     ('if e is not None and e["apres_troncature"] > cf.RESERVE_ECARTS_PARTS:',
      'if e is not None and e["somme"] > cf.RESERVE_ECARTS_PARTS:'),
     [f"{G}::test_reserves_masses_et_troncature", f"{G}::test_reserve_troncature_a_la_lettre_cas_c3"]),
    ("V02a", "VCT8-02", "comparateur : clé sha256 non exclue", EJ,
     ("if k != CLE_EXCLUE_LECTURE[1]}", "if True}"),
     [f"{G}::test_comparateur_lecture_exclusion_declaree_et_controle_des_tables"]),
    ("V02b", "VCT8-02", "comparateur : empreinte citée non comparée au fichier sur disque", EJ,
     ('    if empreinte(p) != f["sha256"]:', "    if False:"),
     [f"{G}::test_comparateur_lecture_exclusion_declaree_et_controle_des_tables"]),
    ("V02c", "VCT8-02", "comparateur : contenu_sha256 non comparé au fichier sur disque", EJ,
     ('    if _sha(json.loads(p.read_text(encoding="utf-8"))["resultat"]) != f["contenu_sha256"]:', "    if False:"),
     [f"{G}::test_comparateur_lecture_exclusion_declaree_et_controle_des_tables"]),
    ("V03a", "VCT8-03", "CODE-T08 : commit cité non contrôlé", L,
     ("    if not en.ligne_cite_commit(code, commit):", "    if False:"),
     [f"{G}::test_passage_a_blanc_cas_sain_et_artefacts", f"{LC}::test_etape_a_mode_reel_cas_sain_et_artefacts"]),
    ("V03b", "VCT8-03", "antériorité sur la création du manifeste de la course retirée", L,
     (',\n                  f"début de la course (création du manifeste {man_course[\'run_id\']})": '
      'en.date_utc(man_course["cree_le"])}', "}"),
     [f"{LC}::test_etape_a_mode_reel_cas_sain_et_artefacts"]),
    ("V03c", "VCT8-03", "passage à blanc : COURSE-T08 déjà inscrite tolérée", L,
     ('    if "COURSE-T08" in reg["lignes"]:', "    if False:"),
     [f"{G}::test_passage_a_blanc_cas_sain_et_artefacts"]),
    ("V03d", "VCT8-03", "course-t08.json non rattaché au manifeste de la course", E,
     ('    if sha != corps_course.get("manifeste_sha256") or m.get("run_id") != corps_course.get("run_id"):',
      "    if False:"),
     [f"{LC}::test_etape_a_artefacts_des_entrees"]),
    ("V03e", "VCT8-03", "passage à blanc : antériorité sur l'heure du passage neutralisée", L,
     ('{"l\'heure du passage à blanc": instant}',
      '{"l\'heure du passage à blanc": datetime(9999, 1, 1, tzinfo=timezone.utc)}'),
     [f"{G}::test_passage_a_blanc_cas_sain_et_artefacts"]),
    ("V03f", "VCT8-03", "antériorité non stricte (même seconde admise)", L,
     ("            if not date < borne:", "            if not date <= borne:"),
     [f"{G}::test_passage_a_blanc_cas_sain_et_artefacts", f"{LC}::test_etape_a_mode_reel_cas_sain_et_artefacts"]),
    ("V03g", "VCT8-03", "CODE-T08 à commit en quatrième cellule non lue", E,
     ("        m = _LIGNE.match(s) or _LIGNE_CODE_COMMIT.match(s)", "        m = _LIGNE.match(s)"),
     [f"{G}::test_registre_code_t08_forme_du_commit", f"{G}::test_passage_a_blanc_cas_sain_et_artefacts"]),
    ("V03h", "VCT8-03", "commit cherché sans bornes de mot (préfixe ou prolongement admis)", E,
     ('re.search(r"(?<![0-9A-Fa-f])" + commit + r"(?![0-9A-Fa-f])", str(ligne.get("chemin") or ""))',
      're.search(commit, str(ligne.get("chemin") or ""))'),
     [f"{G}::test_registre_code_t08_forme_du_commit", f"{G}::test_passage_a_blanc_cas_sain_et_artefacts"]),
    ("V05a", "VCT8-05", "registre du texte de validité lu dans tout état", TD,
     ('    if c["etat"] != "present":', "    if False:"),
     [f"{LC}::test_hd_registre_du_texte_de_validite_non_present_non_lu"]),
    ("V05b", "VCT8-05", "formes de 7b absentes : garde d'entrée de (h bis) retirée", TD,
     ("    if formes_7b is None:                      # défaut de chaîne, avant toute ouverture de la pièce HD (VCT8-05 (b))", "    if False:"),
     [f"{LC}::test_hd_formes_de_7b_absentes_arretent"]),
    ("V05c", "VCT8-05", "formes de 7b absentes : comparaison des types sautée dans _mesures", TD,
     ('    if formes_7b is None:\n        raise GardeArret("formes des colonnes de mesures-t06.npz de 7b absentes : types',
      '    if False:\n        raise GardeArret("formes des colonnes de mesures-t06.npz de 7b absentes : types'),
     [f"{LC}::test_hd_formes_de_7b_absentes_arretent"]),
    ("M35", "VCT8-06", "course réelle : appel de exiger_run_7b retiré", C,
     ("        exiger_run_7b(man7b, marqueurs)\n", ""),
     [f"{LC}::test_course_reelle_manifeste_7b_d_un_autre_run"]),
    ("M38", "VCT8-06", "course : appel de exiger_sans_doublon retiré", C,
     ("    doublons = exiger_sans_doublon(graines_et, graines_7b, premieres_et, premieres_h, tache_de_l_episode)\n",
      '    doublons = {"episodes_controles": 0, "taches_controlees": 0, "doublons": 0}\n'),
     [f"{LC}::test_course_jouet_premiere_action_egale_a_celle_de_h_arrete"]),
    ("M61", "VCT8-06", "échangeabilité : hors_bornes toujours faux", L,
     ('"hors_bornes": bool(a is not None and not (cf.ECHANGEABILITE[0] <= a <= cf.ECHANGEABILITE[1]))}',
      '"hors_bornes": False}'),
     [f"{LC}::test_echangeabilite_hors_bornes"]),
    ("M61b", "VCT8-06", "échangeabilité : bords exclus de l'intervalle", L,
     ("not (cf.ECHANGEABILITE[0] <= a <= cf.ECHANGEABILITE[1])", "not (cf.ECHANGEABILITE[0] < a < cf.ECHANGEABILITE[1])"),
     [f"{LC}::test_echangeabilite_hors_bornes"]),
    ("V07a", "VCT8-07", "fichiers_ouverts avec répétitions", L,
     ("        return _sans_repetition(self.lb.ouvertes)", "        return list(self.lb.ouvertes)"),
     [f"{LC}::test_fichiers_ouverts_sans_repetition", f"{LC}::test_lecture_complete_cas_sain"]),
    ("V07b", "VCT8-07", "fichiers ouverts à l'étape (a) avec répétitions", L,
     ('"ouvertes": _sans_repetition(lb.ouvertes)', '"ouvertes": list(lb.ouvertes)'),
     [f"{LC}::test_fichiers_ouverts_sans_repetition", f"{LC}::test_lecture_complete_cas_sain"]),
]


def preparer(k: int) -> Path:
    d = BLOC / f"copie-{k}"
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True)
    shutil.copytree(ARBRE / "src", d / "src")
    (d / "tests").mkdir()
    for p in sorted((ARBRE / "tests").glob("test_t08_*_v1.py")) + [ARBRE / "tests" / "conftest.py"]:
        shutil.copyfile(p, d / "tests" / p.name)
    shutil.copyfile(ARBRE / "pyproject.toml", d / "pyproject.toml")
    for lien in ("docs", "prereg", "brouillons"):
        os.symlink(ARBRE / lien, d / lien)
    return d


def pytest_(d: Path, essais: list[str]) -> tuple[int, str]:
    env = {**os.environ, "PYTHONPATH": str(d / "src"), "PYTHONDONTWRITEBYTECODE": "1"}
    r = subprocess.run([PY, "-m", "pytest", "-q", "-p", "no:cacheprovider", *essais], cwd=d, env=env,
                       capture_output=True, text=True, timeout=1800)
    return r.returncode, (r.stdout.strip().splitlines() or [""])[-1]


def eprouver(k: int, mutations: list) -> list[str]:
    d = preparer(k)
    sortie = []
    for nom, constat, quoi, fichier, (ancien, neuf), essais in mutations:
        p = d / fichier
        texte = p.read_text(encoding="utf-8")
        n = texte.count(ancien)
        if n != 1:
            sortie.append(f"{nom} {constat:8s} INAPPLICABLE ({n} occurrences) : {quoi}")
            continue
        p.write_text(texte.replace(ancien, neuf), encoding="utf-8")
        try:
            code, fin = pytest_(d, essais)
        finally:
            p.write_text(texte, encoding="utf-8")
        etat = "tuée " if code != 0 else "SURVIT"
        sortie.append(f"{nom:5s} {constat:8s} {Path(fichier).name:24s} {etat} : {quoi} — "
                      f"{' ; '.join(e.split('::')[1] for e in essais)} [{fin}]")
    return sortie


if __name__ == "__main__":
    seules = [x for x in os.environ.get("MUTS", "").split(",") if x]
    if seules:
        MUTATIONS[:] = [m for m in MUTATIONS if m[0] in seules]
    d0 = preparer(99)
    code, fin = pytest_(d0, [str(x.relative_to(d0)) for x in sorted((d0 / "tests").glob("test_t08_*_v1.py"))])
    print(f"témoin sans mutation, les huit fichiers d'essais : code {code} ; {fin}", flush=True)
    lots = [MUTATIONS[i::3] for i in range(3)]
    with ThreadPoolExecutor(3) as ex:
        resultats = list(ex.map(lambda a: eprouver(*a), enumerate(lots)))
    ordre = {m[0]: i for i, m in enumerate(MUTATIONS)}
    lignes = sorted((l for r in resultats for l in r), key=lambda l: ordre[l.split()[0]])
    for l in lignes:
        print(l)
    tuees = sum(" tuée " in l for l in lignes)
    print(f"bilan : {len(MUTATIONS)} mutations ; tuées {tuees} ; survivent {sum('SURVIT' in l for l in lignes)} ; "
          f"inapplicables {sum('INAPPLICABLE' in l for l in lignes)}")
