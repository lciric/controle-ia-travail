"""Lanceur de l'organisme retenu, v5 : étalonnage, conditions et désignation, course du maître (texte scellé, section 13)."""
import json
import shutil
from pathlib import Path

import pytest
from iib_v5_outils import ENTREES, ecrire_scelle

from controle_ia.gardes import GardeArret
from controle_ia.iib import configuration_v5 as cf
from controle_ia.iib import lanceur_v5 as la
from controle_ia.iib.jouet_v5 import SIGNAL_FLAGRANT, SIGNAL_MAITRE, ModeleJouetDeLangue
from controle_ia.scellement import sceller, verifier

DEPOT = Path(__file__).resolve().parents[1]


def _monde(racine: Path, entropie: int = 20261121) -> dict:
    """Configuration jouet complète sous `racine` : module de lecture copié, fichier d'entrées scellé, consignes factices citées."""
    (racine / "src/controle_ia/iib").mkdir(parents=True)
    shutil.copy(DEPOT / cf.MODULE_DE_LECTURE, racine / cf.MODULE_DE_LECTURE)
    import hashlib

    sha_module = hashlib.sha256((racine / cf.MODULE_DE_LECTURE).read_bytes()).hexdigest()
    c = cf.gabarit("jouet")
    sha_e = ecrire_scelle(racine / "entrees/entrees-iib-v5.json", ENTREES)
    for k, lettre in (("consigne_maitre_N", "1"), ("consigne_maitre_P", "2"), ("consigne_flagrant", "3"), ("taches_reserve", "4"), ("taches_evaluation", "5")):
        c["pieces"][k] = {"chemin": f"entrees/{k}-factice.md", "sha256": lettre * 64}
    c["pieces"]["entrees"] = {"chemin": "entrees/entrees-iib-v5.json", "sha256": sha_e}
    c.update({"entropie": entropie, "prefixe_graines": "essai/", "instances_intouchables": [58936096], "go_id": None,
              "marqueurs_de_consigne": [], "jouet": {}})
    c["code"] = {"branche": "prep/iib-code-v5-local", "commit": "0" * 40, "module_de_lecture": {"chemin": cf.MODULE_DE_LECTURE, "sha256": sha_module}}
    c["marqueurs"] = {"EMPREINTES_CODE_IIB": f"{cf.MODULE_DE_LECTURE} {sha_module}"}
    return c


@pytest.fixture(scope="module")
def course(tmp_path_factory):
    """Étalonnage, conditions, course : joués une fois sur le monde jouet (modèle jouet de langue, maître jouet qui s'ancre)."""
    racine = tmp_path_factory.mktemp("iib-v5")
    config = _monde(racine)
    modele, monde = ModeleJouetDeLangue(), la.MondeJouet()
    etal = la.phase_etalonnage(config, racine, racine / "course", modele, monde, carte=False)
    cond = la.phase_conditions(config, racine, racine / "course")
    res = la.phase_course(config, racine, "course", modele, monde, carte=False) if cond["issue"] in ("N", "P") else None
    return {"racine": racine, "config": config, "modele": modele, "monde": monde, "etalonnage": etal, "conditions": cond, "course": res}


def test_etalonnage_sorties_scellees_sans_texte(course):
    d = course["racine"] / "course"
    e = json.loads((d / la.NOMS["etalonnage"]).read_text(encoding="utf-8"))
    verifier(d / la.NOMS["etalonnage"])
    assert set(e) == {"schema", "lignes", "taches", "durees", "depense_etalonnage_usd"} and e["schema"] == cf.SCHEMA_ETALONNAGE
    compte = {}
    for l in e["lignes"]:
        compte[(l["oracle"], l["phase"])] = compte.get((l["oracle"], l["phase"]), 0) + 1
    assert compte == {("P", "etalonnage-honnete"): 640, ("N", "etalonnage-honnete"): 640, ("P", "etalonnage-regenere"): 640,
                      ("N", "etalonnage-regenere"): 640, ("N", "etalonnage-plante"): 640, ("P", "etalonnage-flagrant"): 320,
                      ("N", "etalonnage-flagrant"): 320}                    # 3 840 actions d'oracle (section 12)
    assert sum(compte.values()) == 3840 and e["durees"]["episode_genere_h"] > 0 and e["durees"]["action_oracle_h"] > 0
    for nom in ("etalonnage", "rapportes_etalonnage"):
        brut = (d / la.NOMS[nom]).read_text(encoding="utf-8")
        assert "COST" not in brut and "PROPOSAL" not in brut and SIGNAL_MAITRE not in brut and SIGNAL_FLAGRANT not in brut
    r = json.loads((d / la.NOMS["rapportes_etalonnage"]).read_text(encoding="utf-8"))
    assert r["controle_premier_cout"]["honnetes"]["validite"] in ("valide", "non_valide") and "regeneres/N" in r["par_condition_et_par_oracle"]
    assert r["lecture_de_la_troisieme_donnee"]["ecart_type_par_tiers"] and r["par_condition_et_par_oracle"]["honnetes/N"]["ancrage"]["couples"] > 300
    m = json.loads((d / "graines-etalonnage-iib-v5.json").read_text(encoding="utf-8"))
    assert m["entropie"] == str(course["config"]["entropie"]) and any(k.startswith("essai/iib/jumeau/N/") for k in m["graines"])
    assert any(k.startswith("essai/iib/regenere/") for k in m["graines"]) and any(k.startswith("essai/iib/plante/") for k in m["graines"])
    assert not any("/jumeau/N/" in k and k.endswith(("pas0", "pas1")) for k in m["graines"])     # suites communes aux deux premières actions


def test_conditions_et_designation_scellees_issue_nommee_par_la_regle(course):
    d = course["racine"] / "course"
    c = course["conditions"]
    assert c["issue"] in dg_issues() and verifier(d / la.NOMS["branches"]) == c["sorties"][la.NOMS["branches"]]
    des = json.loads((d / la.NOMS["designation"]).read_text(encoding="utf-8"))
    b = json.loads((d / la.NOMS["branches"]).read_text(encoding="utf-8"))
    attendu = "N" if b["oracles"]["N"]["remplit"] else "P" if b["oracles"]["P"]["remplit"] else "ne_part_pas"
    assert des["issue"] == attendu == c["issue"] and des["etalonnage"]["sha256"] == verifier(d / la.NOMS["etalonnage"])
    # sur le jouet de langue (agent qui s'ancre entièrement), l'instrument régénéré est accepté par l'oracle au contexte de l'agent
    assert b["oracles"]["P"]["grandeurs"]["k_R"] >= 3 * max(b["oracles"]["P"]["grandeurs"]["k_H"], 1)


def dg_issues():
    from controle_ia.iib.designation_v5 import ISSUES

    return ISSUES


def test_second_passage_des_conditions_refuse(course):
    with pytest.raises(GardeArret, match="second passage"):
        la.phase_conditions(course["config"], course["racine"], course["racine"] / "course")
    # même si le seul résultat de la désignation a disparu, le résultat scellé des conditions suffit à refuser
    with pytest.raises(GardeArret, match="déjà joué"):            # poste simulé sans carte (correctif 0011)
        la.phase_etalonnage(course["config"], course["racine"], course["racine"] / "course", course["modele"], course["monde"], carte=False)


def test_course_du_maitre_oracle_de_la_regle_seul_puis_oracle_non_designe_sur_les_acceptes(course):
    res, d = course["course"], course["racine"] / "course"
    assert res is not None and res["oracle_de_la_regle"] == course["conditions"]["issue"]
    o = res["oracle_de_la_regle"]
    autre = "P" if o == "N" else "N"
    resume = json.loads((d / la.NOMS["course"]).read_text(encoding="utf-8"))
    oc = json.loads((d / la.NOMS["oracle_course"]).read_text(encoding="utf-8"))
    assert {l["oracle"] for l in oc["lignes"]} == {o} and len(oc["lignes"]) == 320 * len(resume["tours"])        # un seul oracle par tour
    assert resume["configuration_de_course"]["oracle_de_la_regle"]["valeur"] == o
    assert set(resume["controle_premier_cout"]) >= {"tour 1", "cumul à la fin"}
    if res["arret"] is None:
        hors = oc["lignes_de_l_oracle_non_designe_sur_les_acceptes"]
        assert {l["oracle"] for l in hors} == {autre} and len(hors) == 10 * res["acceptes"] <= 10 * 128
        assert 48 <= res["acceptes"] and "épisodes acceptés" in resume["controle_premier_cout"]
        temoins = json.loads((d / la.NOMS["temoins"]).read_text(encoding="utf-8"))
        assert len(temoins["ids"]) == res["acceptes"] and res["reste"].startswith("distillation et évaluation non jouées")
    else:
        assert res["phrase"].startswith("Sous la thèse «") and res["phrase"].endswith("voir le contrôle du premier coût.")
    for nom in ("course", "oracle_course"):
        brut = (d / la.NOMS[nom]).read_text(encoding="utf-8")
        assert "COST" not in brut and SIGNAL_MAITRE not in brut


def test_evaluation_les_deux_oracles_et_le_controle_du_premier_cout(course, tmp_path):
    """Évaluation jouée avec un distillateur factice (aucune distillation : le modèle jouet sert toutes les conditions)."""
    class Factice:
        charges = []

        def distiller(self, *a):
            self.charges.append("distille")

        def charger(self, condition):
            self.charges.append(condition)
    o = course["conditions"]["issue"]
    if o not in ("N", "P"):
        pytest.skip("la course jouet n'est pas partie")
    g = la.graines_de(course["config"])
    r = la.evaluer(course["config"], course["racine"], tmp_path, course["modele"], course["monde"], Factice(), g, o, "valide", {})
    e = json.loads((tmp_path / la.NOMS["evaluation"]).read_text(encoding="utf-8"))
    assert len(e["lignes"]) == 2 * 4 * 8 * 10 and {l["oracle"] for l in e["lignes"]} == {"N", "P"}         # deux oracles, quatre conditions
    assert set(e["controle_premier_cout"]) == {"H", "B50", "B100", "TJ100"} and r["resume"]["episodes"] == 32
    assert Factice.charges == ["H", "B50", "B100", "TJ100", "H"]                                             # dose 0 rendue aux jumeaux


def test_pas_de_course_sans_resultat_de_conditions_scelle_part(tmp_path):
    racine = tmp_path
    config = _monde(racine)
    modele, monde = ModeleJouetDeLangue(), la.MondeJouet()
    with pytest.raises(GardeArret, match="pas de course sans résultat"):
        la.phase_course(config, racine, "course", modele, monde, carte=False)
    # issue « ne part pas » scellée : refus
    ecrire_scelle(racine / "course" / la.NOMS["designation"], {"schema": cf.SCHEMA_DESIGNATION, "issue": "ne_part_pas"})
    with pytest.raises(GardeArret, match="pas de course"):
        la.phase_course(config, racine, "course", modele, monde, carte=False)
    # résultat écrit à la main, sans sceau : refus
    (racine / "course2").mkdir()
    (racine / "course2" / la.NOMS["designation"]).write_text(json.dumps({"schema": cf.SCHEMA_DESIGNATION, "issue": "P"}), encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte compagnon"):
        la.phase_course(config, racine, "course2", modele, monde, carte=False)


def test_etalonnage_refuse_sans_entropie_ni_intouchables_ni_accord(tmp_path):
    config = _monde(tmp_path)
    modele, monde = ModeleJouetDeLangue(), la.MondeJouet()
    with pytest.raises(GardeArret, match="à remplir par la mère"):
        la.phase_etalonnage({**config, "entropie": None}, tmp_path, tmp_path / "c", modele, monde, carte=False)
    with pytest.raises(GardeArret, match="instances_intouchables"):
        la.phase_etalonnage({**config, "instances_intouchables": []}, tmp_path, tmp_path / "c", modele, monde, carte=False)
    # mode jouet sur une machine payante (accord posé, ou carte visible) : refus (contre-lecture, m7)
    with pytest.raises(GardeArret, match="mode jouet sur une machine payante"):
        la.phase_etalonnage(config, tmp_path, tmp_path / "c", modele, monde, {"IIB_GO_ID": "GO-2099-01-01-01"}, carte=False)
    with pytest.raises(GardeArret, match="mode jouet sur une machine payante"):
        la.phase_etalonnage(config, tmp_path, tmp_path / "c", modele, monde, {}, carte=True)
    # accord cité : exigé en mode réel, sur la machine
    reel = {"mode": "reel", "go_id": "GO-2099-01-01-01"}
    assert la.exiger_accord(reel, {"IIB_GO_ID": "GO-2099-01-01-01"}) == "GO-2099-01-01-01" and la.exiger_accord({"mode": "jouet"}, {}, False) is None
    for env in ({}, {"IIB_GO_ID": "GO-2099-01-01-02"}):
        with pytest.raises(GardeArret, match="accord cité"):
            la.exiger_accord(reel, env)
    with pytest.raises(GardeArret, match="accord cité"):
        la.exiger_accord({"mode": "reel", "go_id": None}, {"IIB_GO_ID": None})
    assert not (tmp_path / "c").exists()                          # aucun refus n'a rien écrit
    # correctif 0012 (relecture, majeur 2) : rien, dans le code de production, ne neutralise la garde — aucun `carte=False` et
    # aucune affectation de `CUDA_VISIBLE_DEVICES` sous src/ et scripts/ (le dossier des moniteurs, interdit aux rôles côté
    # saboteur, n'est pas lu : écart déclaré) ; le détecteur est d'abord éprouvé sur des artefacts et des cas sains (R5)
    import re
    carte_false = re.compile(r"\bcarte\s*=\s*False\b")
    affecte_cuda = re.compile(r"""CUDA_VISIBLE_DEVICES['"]?\s*\]?\s*(:|=(?!=))|export\s+CUDA_VISIBLE_DEVICES|(setdefault|putenv)\(\s*['"]CUDA_VISIBLE_DEVICES""")
    for artefact in ('f(c, carte=False)', 'os.environ["CUDA_VISIBLE_DEVICES"] = ""', '{"CUDA_VISIBLE_DEVICES": ""}', 'CUDA_VISIBLE_DEVICES= python -m x',
                     'export CUDA_VISIBLE_DEVICES', 'os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")', 'env.update(CUDA_VISIBLE_DEVICES="")'):
        assert carte_false.search(artefact) or affecte_cuda.search(artefact), artefact
    for sain in ('f(c, carte=None)', 'os.environ.get("CUDA_VISIBLE_DEVICES") != ""', 'os.environ["CUDA_VISIBLE_DEVICES"] == "0"', 'carte_visible()'):
        assert not carte_false.search(sain) and not affecte_cuda.search(sain), sain
    production = [f for d in ("src", "scripts") for f in sorted((DEPOT / d).rglob("*")) if f.suffix in (".py", ".sh") and f.is_file()
                  and "barreau8_moniteurs" not in f.parts and "__pycache__" not in f.parts]
    lus = {str(f.relative_to(DEPOT)) for f in production}
    assert {"src/controle_ia/iib/lanceur_v5.py", "scripts/amorce_instance_iib_v5.sh", "scripts/lancer_iib_v3.sh"} <= lus
    fautifs = [str(f.relative_to(DEPOT)) for f in production
               if carte_false.search(t := f.read_text(encoding="utf-8", errors="replace")) or affecte_cuda.search(t)]
    assert fautifs == [], fautifs


def test_arret_des_machines_par_identifiant_hors_des_intouchables():
    config = {"instances_intouchables": [58936096, 61000001]}
    assert la.commande_d_arret(61414494, config) == ["vastai", "stop", "instance", "61414494"]
    with pytest.raises(GardeArret, match="intouchables"):
        la.commande_d_arret(58936096, config)
    with pytest.raises(GardeArret, match="R10"):
        la.commande_d_arret("python -m controle_ia.iib.lanceur_v5", config)


def test_environnement_du_lanceur_de_session_porte_les_intouchables(tmp_path):
    config = _monde(tmp_path)
    config["instances_intouchables"] = [58936096, 61000001]
    env = la.environnement_du_lanceur_de_session(config)
    assert env == {"IIB_INSTANCES_INTOUCHABLES": "58936096,61000001"} and "IIB_AUCUNE_INTOUCHABLE" not in env
    with pytest.raises(GardeArret, match="instances_intouchables"):
        la.environnement_du_lanceur_de_session({**config, "instances_intouchables": []})
    # la forme est celle que le lanceur de session en version 2 accepte
    import re
    assert re.fullmatch(r"([1-9][0-9]*(,[1-9][0-9]*)*)", env["IIB_INSTANCES_INTOUCHABLES"])
    assert "IIB_INSTANCES_INTOUCHABLES" in (DEPOT / "scripts/lancer_iib_v2.sh").read_text(encoding="utf-8")


def test_aucune_sortie_supprimee_avant_versement_scelle(tmp_path):
    sortie = tmp_path / "oracle-course-iib-v5.json"
    sortie.write_text("{}\n", encoding="utf-8")
    sha = sceller(sortie)
    manifeste = tmp_path / "versement.json"
    with pytest.raises(GardeArret):                                # aucun manifeste de versement : refus
        la.supprimer_apres_versement(sortie, manifeste)
    manifeste.write_text(json.dumps({"verses": {"autre.json": sha}}), encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte compagnon"):  # manifeste non scellé : refus
        la.supprimer_apres_versement(sortie, manifeste)
    sceller(manifeste)
    with pytest.raises(GardeArret, match="aucun versement scellé"):
        la.supprimer_apres_versement(sortie, manifeste)
    assert sortie.exists()
    bon = tmp_path / "versement-2.json"
    ecrire_scelle(bon, {"verses": {sortie.name: sha}})
    la.supprimer_apres_versement(sortie, bon)
    assert not sortie.exists()
    with pytest.raises(GardeArret, match="activations"):
        la._ecrire(tmp_path, "activations-x.json", {})


def test_aucune_suppression_ailleurs_dans_le_code_v5():
    """Garde statique : aucun module v5 du saboteur ne supprime de fichier, hors `supprimer_apres_versement`. Correctif 0014 :
    seul `versement_v5.py` lance des sous-processus, et seulement `git` en lecture (`ls-files`, `status`, `rev-parse`) et le
    script de consignation de l'amorce par `bash` ; la garde le vérifie sur son texte (cas sain et artefacts du détecteur)."""
    import re

    appel = re.compile(r"subprocess\.(run|Popen|call|check_call|check_output)\(\s*(\[[^\]]*\])")
    permis = {'["bash", str(self.script), f"versement {motif}"]', '["git", "-C", str(self.racine), *args]'}
    for artefact in ('subprocess.run(["rm", "-rf", x])', 'subprocess.Popen(["git", "clean", "-fdx"])'):
        assert appel.search(artefact) and appel.search(artefact).group(2) not in permis, artefact
    for f in sorted((DEPOT / "src/controle_ia/iib").glob("*_v5.py")):
        source = f.read_text(encoding="utf-8")
        for interdit in ("shutil.rmtree", "os.remove", "os.unlink", ".rmdir(") + (() if f.name == "versement_v5.py" else ("subprocess",)):
            assert interdit not in source, (f.name, interdit)
        if f.name == "versement_v5.py":
            vus = [m.group(2) for m in appel.finditer(source)]
            assert set(vus) == permis and source.count("subprocess.") - len(vus) == source.count("subprocess.DEVNULL") + source.count(
                "subprocess.PIPE") + source.count("subprocess.TimeoutExpired"), vus
            sous = set(re.findall(r'self\._git\("([a-z-]+)"', source))
            assert sous == {"ls-files", "status", "rev-parse"}, sous            # git en lecture seule
        assert source.count(".unlink(") == (1 if f.name == "lanceur_v5.py" else 0), f.name


def test_fichier_d_entrees_relu_par_son_empreinte_citee(tmp_path):
    config = _monde(tmp_path)
    assert la.lire_entrees(config, tmp_path)["actions_oracle_hors_tours"] == 3830            # cas sain
    faux = {**config, "pieces": {**config["pieces"], "entrees": {"chemin": "entrees/entrees-iib-v5.json", "sha256": "f" * 64}}}
    with pytest.raises(GardeArret, match="empreinte citée"):
        la.lire_entrees(faux, tmp_path)
    absent = {**config, "pieces": {**config["pieces"], "entrees": {"chemin": "entrees/pas-la.json", "sha256": "f" * 64}}}
    assert la.lire_entrees(absent, tmp_path) is None                                         # absent : « non calculable » à la désignation


# ------------------------------------------------------------------------------------------------------------------------------
# Corrections de la contre-lecture : versement par lot (M1), marques de progrès (M2), point d'entrée et essai à blanc (B1)
# ------------------------------------------------------------------------------------------------------------------------------
def _depot_jouet(racine: Path) -> tuple[dict, Path]:
    """Dépôt git jouet sous `racine` (le manifeste du run lit le commit), configuration jouet écrite et scellée."""
    import subprocess

    config = _monde(racine)
    chemin = racine / "entrees/config-iib-v5-jouet.json"
    chemin.write_text(json.dumps(config, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(chemin)
    for args in (("init", "-q", "-b", "main"), ("config", "user.email", "t@example.invalid"), ("config", "user.name", "t"), ("add", "-A"),
                 ("commit", "-q", "-m", "monde jouet")):
        subprocess.run(["git", "-C", str(racine), *args], check=True, capture_output=True)
    return config, chemin


def test_versement_par_lot_et_marques_de_progres(course, capfd):
    """M1, M2 : chaque lot est écrit et scellé à mesure ; les lots réunis sont l'étalonnage ; une ligne PROGRES par lot."""
    d = course["racine"] / "course"
    lots = sorted((d / "lots").glob("lot-*.json"))
    assert len(lots) == 8 * 3 + 4 == course["etalonnage"]["lots"]         # huit lots d'honnêtes, de régénérés, de plantés ; quatre de flagrants
    lignes = []
    for f in lots:
        verifier(f)
        verifier(d / "lots" / f"ids-{f.name}")
        brut = f.read_text(encoding="utf-8")
        assert "COST" not in brut and SIGNAL_FLAGRANT not in brut
        lignes += json.loads(brut)["lignes"]
    e = json.loads((d / la.NOMS["etalonnage"]).read_text(encoding="utf-8"))
    assert lignes == e["lignes"]
    r = json.loads((d / la.NOMS["rapportes_etalonnage"]).read_text(encoding="utf-8"))
    par = r["duree_d_une_action_d_oracle_par_oracle_h"]
    assert set(par) == {"P", "N"} and e["durees"]["action_oracle_h"] == max(par.values())       # la plus longue des deux (m1)
    assert la.duree_d_une_action_d_oracle({"oracle_P_s": 36.0, "oracle_P_actions": 100, "oracle_N_s": 72.0, "oracle_N_actions": 100})["retenue_h"] == pytest.approx(0.0002)
    la.progres(etape="etalonnage", phase="etalonnage-honnete", lot=3, texte="deux mots")
    ligne = capfd.readouterr().err.strip().splitlines()[-1]
    import re
    assert re.fullmatch(r"PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-zA-Z0-9_-]+=[^ ]+)+", ligne), ligne   # motif de l'amorce


def test_une_garde_qui_arrete_laisse_les_lots_et_ecrit_le_motif(tmp_path):
    """M1 : marqueur de consigne dans un préfixe du jumeau au troisième lot d'honnêtes → arrêt ; les lots déjà joués restent,
    scellés ; `arret.json` porte le motif et la liste de ce qui est écrit ; aucune issue, aucun étalonnage complet."""
    config, _ = _depot_jouet(tmp_path)

    class MondePiege(la.MondeJouet):
        vus = 0

        def environnement(self, condition, tache):
            env = super().environnement(condition, tache)
            if condition == "honnete" and tache == "r9":           # tâche du troisième lot : une observation porte un texte « privé »
                vrai = env.observation
                env.observation = lambda a, pas, j: vrai(a, pas, j) + " " + SIGNAL_MAITRE
            return env
    with pytest.raises(GardeArret, match="texte privé"):
        la.executer("etalonnage", config, tmp_path, "20991231-000000-iib-jouet", ModeleJouetDeLangue(), MondePiege(), {}, carte=False)
    d = tmp_path / "diag/20991231-000000-iib-jouet"
    arret = json.loads((d / "arret.json").read_text(encoding="utf-8"))["resultat"]
    verifier(d / "arret.json")
    assert arret["etape"] == "etalonnage" and "texte privé dans un préfixe du jumeau" in arret["motif"] and arret["issue"].startswith("aucune")
    lots = sorted(f.name for f in (d / "lots").glob("lot-*.json"))
    assert lots == [f"lot-{n:03d}-etalonnage-{p}.json" for n, p in enumerate(("honnete", "regenere", "plante") * 2, start=1)]
    assert all(f"diag/20991231-000000-iib-jouet/lots/{n}" in arret["ecrits_avant_l_arret"] for n in lots)
    assert not (d / la.NOMS["etalonnage"]).exists() and not (d / "resume.json").exists() and not (d / la.NOMS["designation"]).exists()
    for f in (d / "lots").glob("*.json"):
        verifier(f)
    # second lancement dans le même run : refus (R12), rien n'est écrasé
    with pytest.raises(GardeArret, match="existe déjà"):
        la.executer("etalonnage", config, tmp_path, "20991231-000000-iib-jouet", ModeleJouetDeLangue(), la.MondeJouet(), {}, carte=False)


def test_essai_a_blanc_de_bout_en_bout_par_le_point_d_entree(tmp_path, tmp_path_factory):
    """B1 : `python -m controle_ia.iib.lanceur_v5 --phase etalonnage`, puis `--phase conditions`, sur le monde jouet, comme
    l'amorce les appelle (répertoire courant = racine du dépôt cloné ; sorties sous runs/, diag/, donnees/). Le sous-processus
    joue sur un poste simulé sans carte ni accord, écrit par l'essai (correctif 0011 : sur la machine louée, `/usr/bin:/bin`
    portait `nvidia-smi` et torch voyait la carte)."""
    import os
    import subprocess
    import sys

    from iib_v5_outils import environnement_sans_carte

    config, chemin = _depot_jouet(tmp_path)
    run = "20991231-000001-iib-jouet"
    env = environnement_sans_carte(tmp_path_factory.mktemp("poste-sans-carte"), os.environ)     # hors du dépôt jouet : il reste propre
    env["PYTHONPATH"] = str(DEPOT / "src")
    base = [sys.executable, "-m", "controle_ia.iib.lanceur_v5", "--config", "entrees/config-iib-v5-jouet.json", "--run-id", run]
    r = subprocess.run(base + ["--phase", "etalonnage"], cwd=tmp_path, env=env, capture_output=True, text=True, timeout=300)
    assert r.returncode == 0, r.stderr[-800:]
    assert json.loads(r.stdout) == {"run": run, "phase": "etalonnage", "lots": 28}
    progres = [l for l in r.stderr.splitlines() if l.startswith("PROGRES ")]
    assert len(progres) >= 28 + 3 and "etape=chargement" in progres[0] and "phase=fin" in progres[-1]
    assert sum("phase=etalonnage-honnete" in l for l in progres) == 8 and sum("phase=etalonnage-flagrant" in l for l in progres) == 4
    resume = json.loads((tmp_path / "diag" / run / "resume.json").read_text(encoding="utf-8"))
    manifeste = json.loads((tmp_path / "runs" / run / "manifeste.json").read_text(encoding="utf-8"))
    assert resume["resultat"]["arret"] is None and resume["resultat"]["lots"] == 28 and manifeste["commande"] == la.COMMANDE
    assert manifeste["config"]["entropie"] == config["entropie"] and manifeste["decisif"] is False
    assert (tmp_path / "donnees" / run / "lots" / "ids-lot-001-etalonnage-honnete.json").is_file()
    for nom, sha in resume["resultat"]["empreintes"].items():
        f = tmp_path / ("donnees" if nom.startswith("lots/ids-") else "diag") / run / nom
        assert verifier(f) == sha, nom
    c = subprocess.run(base + ["--phase", "conditions"], cwd=tmp_path, env=env, capture_output=True, text=True, timeout=120)
    assert c.returncode == 0, c.stderr[-800:]
    issue = json.loads(c.stdout)
    des = json.loads((tmp_path / "diag" / run / la.NOMS["designation"]).read_text(encoding="utf-8"))
    assert issue["issue"] == des["issue"] in ("N", "P", "ne_part_pas") and issue["phase"] == "conditions"
    # second passage des conditions par le point d'entrée : refus, code 1
    c2 = subprocess.run(base + ["--phase", "conditions"], cwd=tmp_path, env=env, capture_output=True, text=True, timeout=120)
    assert c2.returncode == 1 and "second passage" in c2.stderr
    # la course n'a pas de point d'entrée ; une configuration non scellée est refusée
    sans = subprocess.run(base + ["--phase", "course"], cwd=tmp_path, env=env, capture_output=True, text=True)      # correctif 0015 : point d'entrée
    assert sans.returncode == 1 and "--etalonnage" in sans.stderr                     # de la course, run de l'étalonnage exigé
    (tmp_path / "entrees/config-nue.json").write_text(json.dumps(config), encoding="utf-8")
    nu = subprocess.run([sys.executable, "-m", "controle_ia.iib.lanceur_v5", "--config", "entrees/config-nue.json", "--run-id", "20991231-000002-iib-jouet"],
                        cwd=tmp_path, env=env, capture_output=True, text=True)
    assert nu.returncode == 1 and "empreinte compagnon" in nu.stderr and not (tmp_path / "runs/20991231-000002-iib-jouet").exists()
    # accord posé sur la machine avec une configuration jouet : refus avant tout manifeste
    paye = subprocess.run(base[:-1] + ["20991231-000003-iib-jouet"], cwd=tmp_path, env={**env, "IIB_GO_ID": "GO-2099-01-01-01"}, capture_output=True, text=True)
    assert paye.returncode == 1 and "mode jouet sur une machine payante" in paye.stderr and not (tmp_path / "runs/20991231-000003-iib-jouet").exists()


def test_amorce_v5_et_lanceur_de_session_v3_differences_bornees_aux_changements_declares():
    """B1 : l'amorce en version neuve appelle le lanceur v5 et la liste d'essais ciblés v5 ; elle et le lanceur de session en
    version 3 ne diffèrent de leurs originaux (intacts) que par les lignes déclarées."""
    import difflib
    import hashlib
    import subprocess

    s = DEPOT / "scripts"
    for f in ("amorce_instance_iib_v5.sh", "lancer_iib_v3.sh"):
        assert subprocess.run(["bash", "-n", str(s / f)], capture_output=True).returncode == 0, f
    amorce = (s / "amorce_instance_iib_v5.sh").read_text(encoding="utf-8")
    liste = s / "tests-cibles-iib-v5-v6.txt"                     # version 6 de la liste : poussée par lot (correctif 0014)
    v7 = s / "tests-cibles-iib-v5-v7.txt"                        # correctif 0022 : l'amorce cite la v7 = v6 + l'essai du tirage sur la carte
    assert f'LISTE_TESTS="scripts/{v7.name}"; LISTE_SHA256="{hashlib.sha256(v7.read_bytes()).hexdigest()}"' in amorce
    assert v7.read_text(encoding="utf-8").split() == sorted(liste.read_text(encoding="utf-8").split() + ["tests/test_tirage_carte_v1.py"])
    fichiers = liste.read_text(encoding="utf-8").split()
    # tous les fichiers d'essais en version 5, distillateur compris, sauf celui du tokeniseur réel et celui du moteur à torch du
    # distillateur (sautés sans leurs dépendances : « N passed, 1 skipped » ne passerait pas le contrôle du nombre de tests
    # attendus de l'amorce, et le nombre doit être le même sur le poste et sur la machine)
    hors = ("tokeniseur_reel", "distillation_torch")
    assert fichiers == sorted(str(f.relative_to(DEPOT)) for f in (DEPOT / "tests").glob("test_iib_*_v5.py") if not any(h in f.name for h in hors))
    assert len(fichiers) == 25 and not any(h in f for f in fichiers for h in hors)
    assert {"tests/test_iib_configuration_distillation_v5.py", "tests/test_iib_distillation_v5.py",
            "tests/test_iib_distillation_bout_en_bout_v5.py", "tests/test_iib_environnement_machine_v5.py", "tests/test_iib_versement_v5.py"} <= set(fichiers)
    assert amorce.count("controle_ia.iib.lanceur_v5 --phase etalonnage --config") == 1 and "controle_ia.iib.lanceur_v1 --config" not in amorce
    assert 'IIB_DEBUT_UTC_S="$(date +%s)"' in amorce and "donnees/*/lots/ids-lot-*.json" in amorce

    def changees(a, b):
        d = list(difflib.unified_diff((s / a).read_text(encoding="utf-8").splitlines(), (s / b).read_text(encoding="utf-8").splitlines(), n=0, lineterm=""))
        return [l for l in d if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    da = changees("amorce_instance_iib_v1.sh", "amorce_instance_iib_v5.sh")
    # correctif 0014 : une ligne de plus de chaque côté (le choix de la trace selon le motif « versement … » du lanceur)
    # correctif 0021 : une ligne ajoutée de plus (le tirage passé par l'ordre, IIB_TIRAGE)
    assert len([l for l in da if l[0] == "-"]) == 11 and len([l for l in da if l[0] == "+" and not l[1:].lstrip().startswith("#")]) == 11
    assert any("TRACE_CONSIGNATION=1 consigner_partiel" in l for l in da if l[0] == "-")
    dl = changees("lancer_iib_v2.sh", "lancer_iib_v3.sh")
    # correctif 0021 : une ligne de plus, la commande de création (`-e IIB_TIRAGE=$TIRAGE` passé à la machine)
    assert len([l for l in dl if l[0] == "-"]) == 16 and all(any(m in l for m in ("lancer_iib_v", "amorce_instance_iib_v", "iib-explo-v", "session_v",
                                                                                     "taches_", "pieces.", "consigne", "$cle.", "AUCUNE", "INTOUCHABLES",
                                                                                     "    else", "    fi", "create instance")) for l in dl if l[0] == "-")
    assert sum("create instance" in l for l in dl if l[0] == "-") == 1 and sum("-e IIB_TIRAGE=$TIRAGE" in l for l in dl if l[0] == "+") == 1
    # version 3 : l'attestation « aucune intouchable » n'existe plus (vérification de la contre-lecture, n1)
    assert "IIB_AUCUNE_INTOUCHABLE n'existe plus dans cette version" in (s / "lancer_iib_v3.sh").read_text(encoding="utf-8")
    assert "attesté par IIB_AUCUNE_INTOUCHABLE=oui\"" not in (s / "lancer_iib_v3.sh").read_text(encoding="utf-8")
    v3 = (s / "lancer_iib_v3.sh").read_text(encoding="utf-8")
    assert "session_v5.main" in v3 and "A=scripts/amorce_instance_iib_v5.sh" in v3 and "consigne_maitre_N consigne_maitre_P consigne_flagrant entrees" in v3
    # correctif 0012 (relecture, majeur 1) : la branche « surveillance » ne passe à `$SESSION` (session_v5) que la règle de
    # coupure, sous-commande qui ne charge pas numpy, jamais `config` ; la garde de dépense de la ligne passe par `$SESSION3`
    import re
    appel = r'-c "\$SESSION" ([A-Za-z0-9_-]+)'
    branche = re.search(r"^surveillance\)\n(.*?)^destruction\)", v3, re.M | re.S)
    assert branche and set(re.findall(appel, branche.group(1))) == {"coupure-etalonnage"}
    assert branche.group(1).count('"$SESSION"') == len(re.findall(appel, branche.group(1)))     # aucun autre emploi de `$SESSION`
    assert set(re.findall(appel, branche.group(1) + '\npython3 -I -B -c "$SESSION" config "$D/config.json"\n')) != {"coupure-etalonnage"}  # artefact
    # les originaux sont intacts (empreintes relevées avant ce développement)
    assert hashlib.sha256((s / "lancer_iib_v2.sh").read_bytes()).hexdigest() == "dba3e09769e97e7304600924c4d6c43077412e25347edb76dee193c627947c96"


# ---- règle de coupure propre de l'étalonnage à 16 USD (relevée de 12, correctif 0013), dans la surveillance du lanceur de session (GO-2026-11-21-70) ----
def test_coupure_de_l_etalonnage_regle_cas_sain_artefact_et_autre_phase():
    from controle_ia.iib import session_v5 as se

    cree = 1_795_000_000
    amorce = "AMORCE IIB v1 DEMARRAGE 1 : " + __import__("datetime").datetime.fromtimestamp(cree + 600, __import__("datetime").timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ") + ", machine m, commit c\nPROGRES 2026-11-21T00:00:00Z phase=etalonnage lot=1\n"
    prix = (1.30, 0.08)                                                    # prix borne du devis : 1,38 USD par heure
    h = lambda heures: cree + 600 + heures * 3600                          # noqa: E731
    sain = se.coupure_etalonnage("etalonnage", amorce, h(11.59), *prix, cree)
    assert sain["joue"] and not sain["arret"] and sain["depuis"] == "début de l'amorce" and 15.98 < sain["depense_usd"] < 16
    assert se.ligne_de_coupure(sain).startswith("RIEN : dépense comptée de l'étalonnage 15.99 USD < 16 USD")
    art = se.coupure_etalonnage("etalonnage", amorce, cree + 600 + 16 / 1.38 * 3600 + 1, *prix, cree)      # artefact : la dépense atteint 16
    assert art["arret"] and art["depense_usd"] >= 16 and se.COUPURE_ETALONNAGE_USD == 16.0
    ligne = se.ligne_de_coupure(art)
    assert ligne.startswith("ARRET coupure de l'étalonnage : dépense comptée 16.00 USD ≥ 16 USD") and "par son identifiant (R10)" in ligne
    assert "prix réel lu" in ligne and "destruction" in ligne
    # le prix est le prix réel lu, non le prix borne : à 0,69 USD par heure la même durée ne coupe pas
    assert not se.coupure_etalonnage("etalonnage", amorce, h(12.0), 0.65, 0.04, cree)["arret"]
    # début de l'amorce non encore relevé, ou antérieur à la création (artefact) : la dépense se compte depuis la création, jamais moins
    for texte in ("", "AMORCE IIB v1 DEMARRAGE 1 : 2001-01-01T00:00:00Z, machine m\n"):
        r = se.coupure_etalonnage("etalonnage", texte, cree + 12 * 3600, *prix, cree)
        assert r["arret"] and r["depuis"].startswith("création") and r["debut_utc_s"] == cree
    # un second démarrage ne remet pas le compte à zéro : seule la ligne du premier démarrage compte
    assert se.coupure_etalonnage("etalonnage", amorce + "AMORCE IIB v1 DEMARRAGE 2 : 2099-01-01T00:00:00Z, machine m\n", h(12.0), *prix, cree)["arret"]
    # hors de l'étalonnage la règle ne joue pas, même très au-delà de 16 USD
    for phase in ("course", "conditions"):
        r = se.coupure_etalonnage(phase, amorce, h(30.0), *prix, cree)
        assert not r["joue"] and not r["arret"] and "ne joue pas" in se.ligne_de_coupure(r)
    # refus : phase illisible, prix nul ou illisible, maintenant avant le début
    for mauvais in (("illisible", amorce, h(1), *prix, cree), ("", amorce, h(1), *prix, cree), ("etalonnage", amorce, h(1), 0, 0.08, cree),
                    ("etalonnage", amorce, h(1), "x", 0.08, cree), ("etalonnage", amorce, cree, *prix, cree), ("etalonnage", amorce, float("nan"), *prix, cree)):
        with pytest.raises(GardeArret, match="coupure de l'étalonnage"):
            se.coupure_etalonnage(*mauvais)
    assert se.main(["coupure-etalonnage", "etalonnage"]) == 2 and se.main(["coupure-etalonnage", "illisible", "/nul", "1", "1", "0", "0"]) == 1


def _surveiller(tmp_path, phase, heures, journal_de_fin=False, duree=5):
    """La sous-commande « surveillance » du lanceur de session en version 3, faux outil de location, aucun réseau ; rend
    (code, sortie, texte de la surveillance, appels au faux outil, dossier). Le `python3` que la surveillance trouve en tête
    du chemin est celui d'un environnement virtuel vide : sans numpy, il simule le python3 du système de la machine louée sans
    en être un (même version que l'interpréteur des essais ; le vrai python3 du système est joué par l'essai de la règle de
    coupure, correctif 0012) ; sur le poste, celui du système voyait numpy et cachait le défaut (correctif 0011)."""
    import subprocess
    import time
    from datetime import datetime, timezone

    from iib_v5_outils import python_sans_numpy
    from test_iib_lanceur_forme_v2 import FAUX_OUTIL

    sans_numpy = python_sans_numpy(tmp_path / "python-du-systeme")
    d = tmp_path / "session"
    d.mkdir(parents=True)
    outil = tmp_path / "outil" / "vastai"
    outil.parent.mkdir()
    outil.write_text(FAUX_OUTIL, encoding="utf-8")
    outil.chmod(0o755)
    cree = int(time.time() - heures * 3600)
    instant = datetime.fromtimestamp(cree + 1, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    maintenant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    (tmp_path / "journal.txt").write_text(f"AMORCE IIB v1 DEMARRAGE 1 : {instant}, machine m, commit c\nPROGRES {maintenant} phase=etalonnage lot=3\n"
                                          + (f"AMORCE {maintenant} : fin, code 0\n" if journal_de_fin else ""), encoding="utf-8")
    (d / "lancement.txt").write_text("mode jouet\nprix_carte 1.300000\nprix_stockage 0.080000\ntelechargement_forfait 0.0300\nanterieure 0\n"
                                     f"plafond_creation 55\ninstance 61414494\ncreation {cree}\n", encoding="utf-8")
    if phase is not None:
        (d / "amorce.sh").write_text("#!/usr/bin/env bash\n# commentaire : controle_ia.iib.lanceur_v5 --phase autre --config x\n"
                                     f'PYTHONPATH=src python -m controle_ia.iib.lanceur_v5 --phase {phase} --config "$CONFIG" --run-id "$RUN" &\n', encoding="utf-8")
    e = {"PATH": f"{sans_numpy}:/usr/local/bin:/usr/bin:/bin", "HOME": str(tmp_path), "LANG": "C.UTF-8", "VAST": str(outil), "INTERVALLE": "1",
         "FAUX_VASTAI_JOURNAL": str(tmp_path / "appels.txt"), "FAUX_JOURNAL": str(tmp_path / "journal.txt"),
         "CONTROLE_IA_GITHUB_TOKEN_2": "ghp_FACTICEfactice0123456789", "VAST_API_KEY": "cle-loueur-factice-0123456789abcdef"}
    r = subprocess.run(["timeout", "-k", "2", str(duree), "bash", str(DEPOT / "scripts" / "lancer_iib_v3.sh"), "surveillance", "61414494", str(d)],
                       env=e, capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=120)
    appels = (tmp_path / "appels.txt").read_text(encoding="utf-8").splitlines()
    return r.returncode, r.stdout + r.stderr, (d / "surveillance.txt").read_text(encoding="utf-8"), appels, d


def test_surveillance_cas_sain_depense_sous_16_rien(tmp_path):
    code, sortie, texte, appels, d = _surveiller(tmp_path, "etalonnage", 11.0)               # 11 h à 1,38 : 15,18 USD
    assert code == 124, sortie                                                                 # la surveillance poursuit : seule la durée de l'essai l'interrompt
    assert "règle de coupure de l'étalonnage : phase etalonnage" in texte and "POURSUIVRE" in texte and "ARRET" not in texte
    assert not (d / "coupure-etalonnage.txt").exists() and all(a.startswith(("logs 61414494", "--version")) for a in appels)


def test_surveillance_artefact_depense_a_16_coupure_motif_ecrit_arret_par_l_identifiant(tmp_path):
    code, sortie, texte, appels, d = _surveiller(tmp_path, "etalonnage", 12.0)               # 12 h à 1,38 : 16,56 USD, sous la coupure de la ligne (55)
    assert code == 3, sortie
    assert "ARRET coupure de l'étalonnage : dépense comptée 16.5" in sortie and "ARRET depense" not in texte
    assert "ALERTE coupure de l'étalonnage atteinte" in texte and "ARRET coupure de l'étalonnage" in texte
    motif = (d / "coupure-etalonnage.txt").read_text(encoding="utf-8")
    assert "ARRET coupure de l'étalonnage" in motif and "instance 61414494" in motif and "phase etalonnage" in motif
    assert list((d / "traces-location").glob("coupure-etalonnage-*.txt")) and list((d / "traces-location").glob("fin-de-surveillance-surveillance-*.txt"))
    # R10 : l'arrêt est nommé par l'identifiant ; la surveillance n'a appelé le loueur que pour lire (aucun arrêt, aucune destruction, aucun motif)
    assert sortie.count("stop instance 61414494") == 1 and "pkill" not in sortie and "killall" not in sortie
    assert appels and all(a.startswith(("logs 61414494", "--version")) for a in appels)
    source = (DEPOT / "scripts" / "lancer_iib_v3.sh").read_text(encoding="utf-8")
    assert "pkill" not in source and "killall" not in source


def test_surveillance_hors_etalonnage_la_regle_ne_joue_pas_et_phase_illisible_arrete(tmp_path):
    code, sortie, texte, appels, d = _surveiller(tmp_path / "course", "course", 12.0)
    assert code == 124 and "phase course" in texte and "POURSUIVRE" in texte and "ARRET" not in texte and not (d / "coupure-etalonnage.txt").exists()
    # la fin du run prime : étalonnage fini, dépense au-delà de 16 USD → FIN, pas de coupure
    code, sortie, texte, appels, d = _surveiller(tmp_path / "fin", "etalonnage", 12.0, journal_de_fin=True)
    assert code == 0 and "FIN" in sortie and "coupure de l'étalonnage : dépense" not in texte
    # la coupure de la ligne reste, et prime : 41 h à 1,38 USD dépassent 55 USD
    code, sortie, texte, appels, d = _surveiller(tmp_path / "ligne", "course", 41.0)
    assert code == 3 and "ARRET depense" in sortie and not (d / "coupure-etalonnage.txt").exists()
    # phase illisible (amorce absente du dossier de la session) : arrêt, aucun repli silencieux
    code, sortie, texte, appels, d = _surveiller(tmp_path / "illisible", None, 1.0)
    assert code == 3 and "règle de coupure de l'étalonnage illisible" in sortie and "phase illisible" in texte


def test_replis_de_la_forme_du_lot_des_suites_ecrits_jamais_silencieux(tmp_path, capfd):
    """Correctif 0016 : un repli consigné par le modèle (`modele_v1` : `cache_duplique` vers `prerempli_par_suite`) est écrit
    au résumé et aux rapportés de l'étalonnage, et compté dans chaque marque de progrès de lot ; cas sain : modèle sans repli,
    liste vide et « replis=0 » ; un modèle qui ne tient pas de liste (jouet) rend une liste vide, jamais une erreur avalée."""
    config, _ = _depot_jouet(tmp_path)
    modele = ModeleJouetDeLangue()
    assert la.replis_de(modele) == [] and la.replis_de(None) == []
    modele.replis = [{"de": "cache_duplique", "vers": "prerempli_par_suite", "motif": "RuntimeError: essai (artefact planté)"}]
    r = la.executer("etalonnage", config, tmp_path, "20991231-000030-iib-jouet", modele, la.MondeJouet(), {}, carte=False)
    assert r["replis_forme_lot_suites"] == modele.replis
    d = tmp_path / "diag" / "20991231-000030-iib-jouet"
    assert json.loads((d / "resume.json").read_text(encoding="utf-8"))["resultat"]["replis_forme_lot_suites"] == modele.replis
    assert json.loads((d / la.NOMS["rapportes_etalonnage"]).read_text(encoding="utf-8"))["replis_forme_lot_suites"] == modele.replis
    lots = [l for l in capfd.readouterr().err.splitlines() if l.startswith("PROGRES ") and " lot=" in l and "etape=etalonnage" in l]
    assert len(lots) == 28 and all(l.endswith(" replis=1") for l in lots)
    sain = tmp_path / "sain"
    sain.mkdir()
    config2, _ = _depot_jouet(sain)
    r2 = la.executer("etalonnage", config2, sain, "20991231-000031-iib-jouet", ModeleJouetDeLangue(), la.MondeJouet(), {}, carte=False)
    assert r2["replis_forme_lot_suites"] == []
    assert all(l.endswith(" replis=0") for l in capfd.readouterr().err.splitlines() if l.startswith("PROGRES ") and " lot=" in l
               and "etape=etalonnage" in l)


def test_amorce_de_la_course_differences_bornees_a_celle_de_l_etalonnage_et_choix_par_le_lanceur_de_session(tmp_path):
    """Correctif 0017 : l'amorce de la course ne diffère de celle de l'étalonnage que par les lignes déclarées (c1 à c5) ; sa
    liste figée est celle de l'étalonnage plus l'essai du moteur à torch ; le lanceur de session v3 la choisit par IIB_AMORCE,
    et refuse toute autre valeur (cas sain : variable absente ou égale à l'amorce de l'étalonnage)."""
    import difflib
    import hashlib
    import os
    import subprocess

    s = DEPOT / "scripts"
    a, c = (s / "amorce_instance_iib_v5.sh").read_text(encoding="utf-8"), (s / "amorce_instance_iib_course_v5.sh").read_text(encoding="utf-8")
    assert subprocess.run(["bash", "-n", str(s / "amorce_instance_iib_course_v5.sh")], capture_output=True).returncode == 0
    d = [l for l in difflib.unified_diff(a.splitlines(), c.splitlines(), n=0, lineterm="") if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    code = [l for l in d if not l[1:].lstrip().startswith("#")]
    moins = [l[1:] for l in code if l[0] == "-"]
    plus = [l[1:] for l in code if l[0] == "+"]
    # correctif 0019 (c6) : dix lignes de plus, les neuf de `engager_course` et son appel (`ENGAGEE=` est sur la ligne de RUN_ETAL)
    assert len(moins) == 5 and len(plus) == 18, (moins, plus)
    corps = c.split("# --- (c6) engagement de la course\n", 1)[1].split("# --- fin (c6)\n", 1)[0]
    assert len([l for l in corps.splitlines() if not l.lstrip().startswith("#")]) == 9 and plus.count('engager_course "$ENGAGEE"') == 1
    assert all(any(m in l for m in ("LISTE_TESTS=", 'RUN="$(date', 'journal "run : $RUN', "lanceur_v5 --phase etalonnage", 'ajouter "runs/$RUN"')) for l in moins)
    assert sum(l.startswith(("DES=", "{ [ -n \"$DES\" ]", "RUN_ETAL=")) for l in plus) == 3
    vivantes = [l for l in c.splitlines() if "controle_ia.iib.lanceur_v5 --phase" in l and not l.lstrip().startswith("#")]
    assert len(vivantes) == 1 and '--phase course --config "$CONFIG" --run-id "$RUN" --tirage "$TIRAGE" --etalonnage "$RUN_ETAL"' in vivantes[0]
    assert 'IIB_CONSIGNER="$R/iib-consigner.sh"' in vivantes[0] and 'ajouter "runs/$RUN" "diag/$RUN" "diag/$RUN_ETAL"' in c
    liste = s / "tests-cibles-iib-course-v5-v2.txt"                     # correctif 0020 : plus l'essai du tirage sur la carte
    assert liste.read_text(encoding="utf-8").split() == sorted((s / "tests-cibles-iib-v5-v6.txt").read_text(encoding="utf-8").split()
                                                              + ["tests/test_iib_distillation_torch_v5.py", "tests/test_tirage_carte_v1.py"])
    assert f'LISTE_TESTS="scripts/{liste.name}"; LISTE_SHA256="{hashlib.sha256(liste.read_bytes()).hexdigest()}"' in c
    # la phase lue par la surveillance du lanceur de session (même commande que `lancer_iib_v3.sh`, ligne PHASE=) : « course »
    lue = subprocess.run(["bash", "-c", "grep -v '^[[:space:]]*#' \"$1\" | sed -n 's/.*controle_ia\\.iib\\.lanceur_v5 --phase \\([a-z_]*\\) .*/\\1/p' | sort -u",
                          "_", str(s / "amorce_instance_iib_course_v5.sh")], capture_output=True, text=True).stdout.split()
    assert lue == ["course"]
    # le lanceur de session : une valeur inconnue de IIB_AMORCE est un refus avant toute sous-commande
    env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "IIB_DEPOT": str(DEPOT)}
    r = subprocess.run(["bash", str(s / "lancer_iib_v3.sh"), "outil"], env={**env, "IIB_AMORCE": "scripts/amorce_instance_iib_v1.sh"},
                       capture_output=True, text=True, timeout=60)
    assert r.returncode == 2 and "ni l'amorce de l'étalonnage ni celle de la course" in r.stdout + r.stderr
    v3 = (s / "lancer_iib_v3.sh").read_text(encoding="utf-8")
    assert "scripts/amorce_instance_iib_course_v5.sh) A=\"$IIB_AMORCE\"" in v3 and "A=scripts/amorce_instance_iib_v5.sh" in v3


def test_amorce_de_la_course_engagement_unique_par_etalonnage(tmp_path):
    """Correctif 0019 (cl1, M1) : la fonction `engager_course` de l'amorce de la course, jouée telle qu'écrite contre une origine
    nue locale. Cas sain : référence absente, poussée. Artefact : référence présente (une course déjà engagée sur cet
    étalonnage, depuis une autre machine) : refus, rien n'est poussé de plus."""
    import re
    import subprocess

    texte = (DEPOT / "scripts" / "amorce_instance_iib_course_v5.sh").read_text(encoding="utf-8")
    bloc = re.search(r"# --- \(c6\) engagement de la course\n(.*?)# --- fin \(c6\)\n", texte, re.S).group(1)
    assert 'engager_course "$ENGAGEE"' in texte and 'ENGAGEE="refs/heads/essai/iib-course-engagee-$RUN_ETAL"' in texte
    origine, d = tmp_path / "o.git", tmp_path / "d"
    subprocess.run(["git", "init", "-q", "--bare", str(origine)], check=True)
    subprocess.run(["git", "init", "-q", str(d)], check=True)
    for a in (("config", "user.email", "t@x.invalid"), ("config", "user.name", "t"), ("commit", "-q", "--allow-empty", "-m", "c"),
              ("remote", "add", "origin", str(origine))):
        subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)
    script = tmp_path / "e.sh"
    script.write_text("T=$1; cd $2\nrefus() { echo \"REFUS : $1\"; exit 2; }\njournal() { echo \"$*\"; }\n" + bloc +
                      'engager_course "refs/heads/essai/iib-course-engagee-20991231-000020-iib-jouet"\necho FIN\n', encoding="utf-8")
    sain = subprocess.run(["bash", str(script), str(tmp_path), str(d)], capture_output=True, text=True, timeout=120)
    assert sain.returncode == 0 and "course engagée" in sain.stdout and "FIN" in sain.stdout, sain.stdout + sain.stderr
    refs = subprocess.run(["git", "-C", str(origine), "for-each-ref", "--format=%(refname)"], capture_output=True, text=True).stdout.split()
    assert refs == ["refs/heads/essai/iib-course-engagee-20991231-000020-iib-jouet"]
    deux = subprocess.run(["bash", str(script), str(tmp_path), str(d)], capture_output=True, text=True, timeout=120)
    assert deux.returncode == 2 and "course déjà engagée sur cet étalonnage" in deux.stdout and "FIN" not in deux.stdout


def test_tirage_choisi_explicitement_defaut_inchange(tmp_path):
    """Correctif 0020 : le tirage sur la carte est un chemin neuf, choisi explicitement (`tirage="carte"`, `--tirage carte`) ; le
    défaut reste le tirage d'origine et il est écrit au résumé ; « carte » en mode jouet est refusé avant tout manifeste."""
    config, _ = _depot_jouet(tmp_path)
    with pytest.raises(GardeArret, match="mode réel seulement"):
        la.executer("etalonnage", config, tmp_path, "20991231-000040-iib-jouet", ModeleJouetDeLangue(), la.MondeJouet(), {}, carte=False,
                    tirage="carte")
    assert not (tmp_path / "runs" / "20991231-000040-iib-jouet").exists()
    r = la.executer("etalonnage", config, tmp_path, "20991231-000041-iib-jouet", ModeleJouetDeLangue(), la.MondeJouet(), {}, carte=False)
    assert r["tirage"] == "processeur"


def test_meme_tirage_a_l_etalonnage_et_a_la_course_et_variable_de_l_ordre(tmp_path):
    """Correctif 0021 (voie (A), GO-2026-11-22-73) : la course tire comme l'étalonnage dont elle part ; le tirage est passé par
    une variable explicite de l'ordre (IIB_TIRAGE), à l'étalonnage comme à la course, et refusé s'il est inconnu."""
    import os
    import subprocess

    from controle_ia.scellement import sceller

    run = "20991231-000050-iib-reel"
    r = tmp_path / "diag" / run / "resume.json"
    r.parent.mkdir(parents=True)
    assert la.exiger_meme_tirage(tmp_path, run, "processeur") == "processeur"           # résumé absent : processeur seulement
    with pytest.raises(GardeArret, match="tirent de même"):
        la.exiger_meme_tirage(tmp_path, run, "carte")
    for vu, demande, ok in (("carte", "carte", True), ("processeur", "processeur", True), ("carte", "processeur", False),
                            ("processeur", "carte", False), (None, "processeur", True), (None, "carte", False)):
        if r.exists():
            r.unlink()
            Path(str(r) + ".sha256").unlink()
        r.write_text(json.dumps({"resultat": {} if vu is None else {"tirage": vu}}) + "\n", encoding="utf-8")
        sceller(r)
        if ok:
            assert la.exiger_meme_tirage(tmp_path, run, demande) == demande
        else:
            with pytest.raises(GardeArret, match="tirent de même"):
                la.exiger_meme_tirage(tmp_path, run, demande)
    s = DEPOT / "scripts"
    for f in ("amorce_instance_iib_v5.sh", "amorce_instance_iib_course_v5.sh"):
        t = (s / f).read_text(encoding="utf-8")
        assert 'TIRAGE="${IIB_TIRAGE:-processeur}"; case "$TIRAGE" in processeur|carte) ;;' in t, f
        vivante = [l for l in t.splitlines() if "controle_ia.iib.lanceur_v5 --phase" in l and not l.lstrip().startswith("#")]
        assert len(vivante) == 1 and '--tirage "$TIRAGE"' in vivante[0], f
    v3 = (s / "lancer_iib_v3.sh").read_text(encoding="utf-8")
    assert "-e IIB_TIRAGE=$TIRAGE " in v3
    env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "IIB_DEPOT": str(DEPOT)}
    mauvais = subprocess.run(["bash", str(s / "lancer_iib_v3.sh"), "outil"], env={**env, "IIB_TIRAGE": "gpu"}, capture_output=True, text=True, timeout=60)
    assert mauvais.returncode == 2 and "IIB_TIRAGE=gpu" in mauvais.stdout


def test_vitesse_du_premier_lot_scellee_sans_texte(course, capfd):
    """Correctif 0022 : dès la fin du premier lot, la durée de génération par épisode et la durée par action d'oracle de chaque
    oracle sont écrites et scellées (aucun texte, aucun jeton, aucune sortie d'oracle), et dites par une marque de progrès.
    Artefact : une durée non mesurée est un refus, jamais un zéro."""
    import re

    f = course["racine"] / "course" / la.VITESSE
    v = json.loads(f.read_text(encoding="utf-8"))
    assert verifier(f) and v["lot"] == 1 and v["episodes_generes"] == 8 and v["oracle_P_actions"] > 0 and v["oracle_N_actions"] > 0
    assert set(v) == {"avertissement", "lot", "episodes_generes", "generation_s_par_episode", "oracle_P_actions", "oracle_P_s_par_action",
                      "oracle_N_actions", "oracle_N_s_par_action", "tirage"}
    assert all(isinstance(v[k], float) and v[k] > 0 for k in ("generation_s_par_episode", "oracle_P_s_par_action", "oracle_N_s_par_action"))
    brut = f.read_text(encoding="utf-8")
    assert "COST" not in brut and '"ids"' not in brut and '"lignes"' not in brut and SIGNAL_MAITRE not in brut
    with pytest.raises(GardeArret, match="aucune durée inventée"):
        la.vitesse_du_premier_lot({"generation_s": 1.0, "episodes_generes": 8, "oracle_P_s": 2.0, "oracle_P_actions": 0}, None)
    m = la.vitesse_du_premier_lot({"generation_s": 4.0, "episodes_generes": 8, "oracle_P_s": 2.0, "oracle_P_actions": 80, "oracle_N_s": 3.0,
                                   "oracle_N_actions": 80}, type("M", (), {"tirage": "carte-x"})())
    assert m["generation_s_par_episode"] == 0.5 and m["oracle_P_s_par_action"] == 0.025 and m["tirage"] == "carte-x"
    la.progres(etape="vitesse", lot=1, generation_s_par_episode=0.5, oracle_P_s_par_action=0.025, oracle_N_s_par_action=0.0375)
    ligne = capfd.readouterr().err.strip().splitlines()[-1]
    assert re.fullmatch(r"PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-zA-Z0-9_-]+=[^ ]+)+", ligne)
    assert not re.search(r"au-dessus|interpr|échec|echec|aire=|bas=|haut=|ligne_|table_|plancher", ligne, re.I)
