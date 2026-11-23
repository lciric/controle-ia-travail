

# === v11b : GO de la course = GO-2026-11-22-80 (prolongation de GO-2026-11-18-14) ============================================
REV_80 = "| GO-2026-11-22-141 | 2026-11-22 | révocation | révoque GO-2026-11-22-80 | — | — | Lazar | — |\n"
REV_14 = "| GO-2026-11-22-142 | 2026-11-22 | révocation | révoque GO-2026-11-18-14 | — | — | Lazar | — |\n"
CONF_131 = "GO-2026-11-22-131"


def _sans_ligne(texte, go_id):
    lignes = [l for l in texte.splitlines(keepends=True) if not l.startswith(f"| {go_id} |")]
    assert len(lignes) == len(texte.splitlines(keepends=True)) - 1
    return "".join(lignes)


def test_v11b_go_de_la_course_et_commande_de_lancement():
    assert L.GO_ID == "GO-2026-11-22-80" == L.GO_PROLONGATION_COURSE and L.GO_COURSE_INITIAL == "GO-2026-11-18-14"
    assert "GO_ID=GO-2026-11-22-80 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v11b.py" in L.__doc__
    assert FIXE["changements_v11"]["go_course"] == "GO-2026-11-22-80"
    garde, _, _ = L.environnement_filtre({"GO_ID": "GO-2026-11-18-14"}, Path("/nulle-part"))
    assert garde["GO_ID"] == "GO-2026-11-22-80"                       # passé tel quel à l'orchestrateur


def test_v11b_depart_sain_avec_go_80(monde):
    assert lancer(monde["r"]) == 0


def test_v11b_depart_refuse_si_go_80_absent(monde):
    monde["r"].registre_go.write_text(_sans_ligne(ligne_go(), "GO-2026-11-22-80"), encoding="utf-8")
    assert lancer(monde["r"]) == 2
    assert not monde["r"].dossier_runs.exists()


def test_v11b_depart_refuse_si_go_80_revoque(monde):
    monde["r"].registre_go.write_text(ligne_go() + REV_80, encoding="utf-8")
    assert lancer(monde["r"]) == 2
    assert not monde["r"].dossier_runs.exists()


def test_v11b_depart_refuse_si_go_14_absent_ou_revoque(monde):
    monde["r"].registre_go.write_text(_sans_ligne(ligne_go(), "GO-2026-11-18-14"), encoding="utf-8")
    assert lancer(monde["r"]) == 2
    monde["r"].registre_go.write_text(ligne_go() + REV_14, encoding="utf-8")
    assert lancer(monde["r"]) == 2
    assert not monde["r"].dossier_runs.exists()


def test_v11b_go_80_qui_ne_prolonge_pas_go_14_refuse(tmp_path):
    l80 = L80.replace("Prolongation de GO-2026-11-18-14 (affinage", "Course (affinage")
    with pytest.raises(L.Refus, match="ne dit pas prolonger GO-2026-11-18-14"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, l80, L107, L124), dt.date(2026, 11, 24), _fixe_confirmation(None))


def test_v11b_go_80_accorde_par_un_autre_refuse(tmp_path):
    l80 = L80.replace("| 2026-12-15 | Lazar |", "| 2026-12-15 | la mère |")
    with pytest.raises(L.Refus, match="accordée par"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, l80, L107, L124), dt.date(2026, 11, 24), _fixe_confirmation(None))


def test_v11b_depart_accepte_au_26_avec_go_80_et_confirmation_nommee(tmp_path):
    o = L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), dt.date(2026, 11, 26), _fixe_confirmation(CONF_131))
    assert o["go"]["id"] == "GO-2026-11-22-80" and o["go"]["plafond_lu"] == 150.0
    assert o["confirmation_107"]["nommee"] == CONF_131 and o["exception_cle"]["id"] == "GO-2026-11-22-107"


def test_v11b_depart_refuse_au_26_sans_confirmation(tmp_path):
    with pytest.raises(L.Refus, match="GO-2026-11-22-107 hors de sa période"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), dt.date(2026, 11, 26), _fixe_confirmation(None))


def test_v11b_go_de_la_configuration_autre_refuse(tmp_path):
    for valeur in ("GO-2026-11-18-14", None):
        f = _fixe_confirmation(CONF_131)
        f["changements_v11"]["go_course"] = valeur
        with pytest.raises(L.Refus, match="go_course"):
            L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), dt.date(2026, 11, 26), f)


@pytest.mark.parametrize("plafond, issue", [
    ("150 USD (plafond de GO-2026-11-18-14)", "sain"), ("150 USD", "sain"),
    ("150 USD (ou 200)", "refus"), ("140 USD (plafond de GO-2026-11-18-14)", "refus"), ("150 USD (plafond) 20", "refus"),
])
def test_v11b_plafond_de_go_80(tmp_path, plafond, issue):
    l80 = L80.replace("| 150 USD (plafond de GO-2026-11-18-14) |", f"| {plafond} |")
    reg = _registre_go_essai(tmp_path, L14, l80)
    if issue == "sain":
        assert L.verifier_go(reg, dt.date(2026, 11, 26))["plafond_lu"] == 150.0
    else:
        with pytest.raises(L.Refus):
            L.verifier_go(reg, dt.date(2026, 11, 26))


def test_v11b_registre_derive_garde_go_80_et_go_14_et_leurs_revocations(tmp_path):
    autre = "| GO-2026-11-20-03 | 2026-11-20 | calcul | autre course | 10 USD | 2026-11-30 | Lazar | — |\n"
    d = L.ecrire_registre_derive(_registre_go_essai(tmp_path, L14, L80, autre, L107, REV_80, REV_14), tmp_path / "derive.md")
    texte = (tmp_path / "derive.md").read_text(encoding="utf-8")
    assert d["nombre_de_lignes"] == 4
    for go in ("GO-2026-11-18-14", "GO-2026-11-22-80", "GO-2026-11-22-141", "GO-2026-11-22-142"):
        assert f"| {go} |" in texte
    assert "GO-2026-11-20-03" not in texte and "| GO-2026-11-22-107 |" not in texte


def test_v11b_sur_le_vrai_registre_de_main(tmp_path):
    p = subprocess.run(["git", "-C", str(RACINE), "show", "refs/remotes/origin/main:registres/go.md"], capture_output=True)
    if p.returncode != 0 or b"| GO-2026-11-22-80 |" not in p.stdout:
        pytest.skip("registre de main sans la ligne GO-2026-11-22-80")
    reg = tmp_path / "go.md"
    reg.write_bytes(p.stdout)
    assert L.verifier_go(reg, dt.date(2026, 11, 26))["id"] == "GO-2026-11-22-80"
    assert L.lire_prolongation(reg, dt.date(2026, 11, 26), L.GO_ID, L.GO_COURSE_INITIAL)["valide"] is True
    assert L.verifier_go_initial(reg)["id"] == "GO-2026-11-18-14"
    with pytest.raises(L.Refus):
        L.verifier_go(reg, dt.date(2026, 12, 16))
    with pytest.raises(L.Refus, match="GO-2026-11-22-107 hors de sa période"):     # aucune confirmation nommée au 26
        L.verifier_les_go(reg, dt.date(2026, 11, 26), _fixe_confirmation(None))
    d = L.ecrire_registre_derive(reg, tmp_path / "derive.md")
    texte = (tmp_path / "derive.md").read_text(encoding="utf-8")
    assert "| GO-2026-11-22-80 |" in texte and "| GO-2026-11-18-14 |" in texte


# --- l'orchestrateur épinglé lit le registre dérivé v11b (vraie lecture, `configuration_v55.verifier_go_v55`) ------------------
EMPREINTES_LECTURE_GO = {"pole/configuration_v55.py": "2e6237c0a8b1c823fa17ddd6c680357a59ec4030bfbe9ac6ba970a700a864071",
                         "pole/configuration_v53.py": "ef72ffbf"}


def _lecture_go_orchestrateur():
    cands = [Path(os.environ["ORCHESTRATEUR_AFFINAGE_ESSAI"])] if os.environ.get("ORCHESTRATEUR_AFFINAGE_ESSAI") else []
    cands += list(L.ORCHESTRATEURS_CANDIDATS)
    for o in cands:
        if all((o / rel).is_file() and hashlib.sha256((o / rel).read_bytes()).hexdigest().startswith(sha)
               for rel, sha in EMPREINTES_LECTURE_GO.items()):
            sys.path.insert(0, str(o))
            ancien, sys.dont_write_bytecode = sys.dont_write_bytecode, True
            try:
                from pole.configuration_v55 import verifier_go_v55
                from pole.configuration_v53 import GoRefuse
            finally:
                sys.path.remove(str(o))
                sys.dont_write_bytecode = ancien
            return verifier_go_v55, GoRefuse
    pytest.skip("orchestrateur épinglé (a41b7b50) absent : variable ORCHESTRATEUR_AFFINAGE_ESSAI")


def test_v11b_orchestrateur_accepte_go_80_au_26_et_refusait_go_14(tmp_path):
    verifier_go_v55, GoRefuse = _lecture_go_orchestrateur()
    d = L.ecrire_registre_derive(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), tmp_path / "derive.md")
    g = verifier_go_v55(L.GO_ID, d["derive"], 150.0, aujourd_hui=dt.date(2026, 11, 26))
    assert g["identifiant"] == "GO-2026-11-22-80" and g["plafond_lu_usd"] == 150.0 and g["echeance"] == "2026-12-15"
    with pytest.raises(GoRefuse, match="période"):                              # ce que v11 lui passait
        verifier_go_v55("GO-2026-11-18-14", d["derive"], 150.0, aujourd_hui=dt.date(2026, 11, 26))
    with pytest.raises(GoRefuse, match="période"):
        verifier_go_v55(L.GO_ID, d["derive"], 150.0, aujourd_hui=dt.date(2026, 12, 16))


def test_v11b_orchestrateur_refuse_go_80_revoque_au_registre_derive(tmp_path):
    verifier_go_v55, GoRefuse = _lecture_go_orchestrateur()
    rev2 = "| GO-2026-11-22-41 | 2026-11-22 | révocation | révoque GO-2026-11-22-80 | — | — | Lazar | — |\n"  # deux chiffres : lisible par lui
    d = L.ecrire_registre_derive(_registre_go_essai(tmp_path, L14, L80, rev2), tmp_path / "derive.md")
    with pytest.raises(GoRefuse, match="révoqué"):
        verifier_go_v55(L.GO_ID, d["derive"], 150.0, aujourd_hui=dt.date(2026, 11, 26))
