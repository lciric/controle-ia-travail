"""Mutations qui doivent rendre un essai rouge : chaque mutation est appliquée au fichier (remplacement unique), les
essais désignés sont joués, le fichier est rendu à l'octet."""
import subprocess
import sys
from pathlib import Path

R = Path("/home/user/controle-ia-travail/.claude/worktrees/agent-a89be1d2701a117b9")
S = Path("/tmp/claude-0/-home-user-controle-ia-travail/b09e1b49-1473-5167-b0d5-946b1adabcb0/scratchpad")
PY = "/home/user/controle-ia-travail/.venv/bin/python"
OUV = "src/controle_ia/barreau5_familles/ouverture_suffixes_v1.py"
CMD = "src/controle_ia/barreau5_familles/commande_lecture_v3.py"
TI = "tests/test_amorce_b5f_lecture_identification_v1.py"

MUTATIONS = [
    ("traduire avant l'engagement", OUV,
     '''    engagement = _empreinte_engagee(en.lignes_du_registre(texte_registre))
    _exiger(en.empreinte_table(table) == engagement, "table : empreinte ≠ ENGAGEMENT-B5F (engagement) : refus, aucune "
            "traduction")
    if racine is not None:
        code_au_commit_v3(racine, texte_registre)
    decision = decider(''',
     '''    engagement = _empreinte_engagee(en.lignes_du_registre(texte_registre))
    graphies(table)
    _exiger(en.empreinte_table(table) == engagement, "table : empreinte ≠ ENGAGEMENT-B5F (engagement) : refus, aucune "
            "traduction")
    if racine is not None:
        code_au_commit_v3(racine, texte_registre)
    decision = decider(''',
     ["tests/test_ouverture_suffixes_v1.py", "-k", "artefacts and retouchee"]),
    ("tirer c(base) de la table", OUV,
     '    return {b: _familles_formees(racine_formation, b, relance)[1] for b in sorted(graphies(table))}',
     '    return {b: g for b, g in graphies(table).items()}',
     ["tests/test_ouverture_suffixes_v1.py", "-k", "variante_et_preparer_artefacts"]),
    ("tirer c(base) de la table (résumé)", OUV,
     '        sortie[b] = exiger_copie_lue(b, formation[b].get("copie"), relance)',
     '        sortie[b] = graphies(table)[b]',
     ["tests/test_ouverture_suffixes_v1.py", "-k", "artefacts_d_ouverture or en_b_avec_racine"]),
    ("admettre deux graphies", OUV,
     '        _exiger(vues.setdefault(b, x["famille"]) == x["famille"],',
     '        _exiger(vues.setdefault(b, x["famille"]) == x["famille"] or True,',
     ["tests/test_ouverture_suffixes_v1.py", "-k", "deux_graphies or decision_artefacts"]),
    ("oublier -r1", OUV,
     '_GRAPHIE = re.compile(r"(?P<base>T(?:0[1-9]|10))(?P<relance>-x1)?(?P<retirage>-r1)?")',
     '_GRAPHIE = re.compile(r"(?P<base>T(?:0[1-9]|10))(?P<relance>-x1)?")',
     ["tests/test_ouverture_suffixes_v1.py", "-k", "cas_sain_b or graphie_cas_sains"]),
    ("jouer la cohérence sur T_nu", OUV,
     '    table_nu = table_traduite(table, decision)\n    exiger_lignes_du_plan(table_nu)',
     '    table_nu = table_traduite(table, decision)\n    en.exiger_table_coherente(table_nu)\n    exiger_lignes_du_plan(table_nu)',
     ["tests/test_ouverture_suffixes_v1.py", "-k", "cas_sain_b"]),
    ("épinglage : espace initiale admise", CMD,
     '    if m is None or not ligne.startswith(PREFIXE_EPINGLAGE) or not unicodedata.is_normalized("NFC", ligne):',
     '    m = _EPINGLAGE.fullmatch(ligne.lstrip())\n    if m is None:',
     ["tests/test_commande_lecture_v3.py", "-k", "d_prime_artefacts"]),
    ("épinglage : deux lignes admises", CMD,
     '    if len(candidates) != 1:', '    if len(candidates) > 2:',
     ["tests/test_commande_lecture_v3.py", "-k", "d_prime_artefacts"]),
    ("(c'2) : mode non vérifié", CMD,
     '        if m["apres"] not in MODES_ADMIS:', '        if False:',
     ["tests/test_commande_lecture_v3.py", "-k", "c_prime_2"]),
    ("(c'1) omise", CMD,
     '    exiger_commande_issue_du_code_fige(racine, commit_lecture, v2)\n    exiger_v3_issu_de_v2',
     '    exiger_v3_issu_de_v2',
     ["tests/test_commande_lecture_v3.py", "-k", "c_prime_1"]),
    ("(b') omise", CMD,
     '    exiger_session_au_commit_de_commande(racine, v3)\n    return v2, v3', '    return v2, v3',
     ["tests/test_commande_lecture_v3.py", "-k", "b_prime or autre_commit"]),
    ("amorce figée embarquée", CMD,
     '    amorce = amorce_corrigee(_montrer(racine, commit, AMORCE))', '    amorce = _montrer(racine, commit, AMORCE)',
     ["tests/test_commande_lecture_v3.py", "-k", "difference_fermee or montage_complet"]),
    ("lanceur v3 : condition C12 retirée", "scripts/lancer_b5f_lecture_v3.sh",
     '        [ "$sha" = "$CORRIGEE" ] || {', '        true || {',
     ["tests/test_commande_lecture_v3.py", "-k", "c12"]),
    ("amorce : ligne ajoutée retirée", TI,
     '    corrigee.write_bytes(cl3.amorce_corrigee(AMORCE_FIGEE.read_bytes()))',
     '    corrigee.write_bytes(AMORCE_FIGEE.read_bytes())',
     [TI, "-k", "cas_sain or garde_neuve"]),
    ("amorce : ligne placée après l'extraction", TI,
     '    corrigee.write_bytes(cl3.amorce_corrigee(AMORCE_FIGEE.read_bytes()))',
     '    _o = AMORCE_FIGEE.read_bytes(); _a, _n = cl3.PAIRE_AMORCE; _x = _n[len(_a):]\n'
     '    _c = [l for l in _o.split(b"\\n")]; _i = next(i for i, l in enumerate(_c) if b"checkout -q \\"$ENTREES_COMMIT\\"" in l)\n'
     '    corrigee.write_bytes(b"\\n".join(_c[:_i + 1] + [_x.rstrip(b"\\n")] + _c[_i + 1:]))',
     [TI, "-k", "cas_sain or garde_neuve"]),
]


def main():
    seul = sys.argv[1:]
    bilan = []
    for i, (nom, f, ancien, neuf, essais) in enumerate(MUTATIONS):
        if seul and str(i) not in seul:
            continue
        p = R / f
        orig = p.read_bytes()
        texte = orig.decode("utf-8")
        assert texte.count(ancien) == 1, (nom, texte.count(ancien))
        try:
            p.write_text(texte.replace(ancien, neuf), encoding="utf-8")
            bt = S / f"bt-mut-{i}"
            subprocess.run(["rm", "-rf", str(bt)])
            r = subprocess.run([PY, "-m", "pytest", "-q", "--tb=no", "-rN", "-p", "no:cacheprovider", f"--basetemp={bt}",
                                *essais], cwd=R, env={"PYTHONPATH": "src", "PATH": "/usr/bin:/bin",
                                                     "PYTHONDONTWRITEBYTECODE": "1", "HOME": "/root"},
                               capture_output=True, text=True, timeout=900)
            ligne = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-300:]
            rouge = r.returncode != 0 and "failed" in ligne
            bilan.append((i, nom, "ROUGE" if rouge else "VERT (mutation non attrapée)", ligne))
            print(bilan[-1], flush=True)
        finally:
            p.write_bytes(orig)
    print("\n".join(f"{i}\t{n}\t{e}\t{l}" for i, n, e, l in bilan))


if __name__ == "__main__":
    main()
