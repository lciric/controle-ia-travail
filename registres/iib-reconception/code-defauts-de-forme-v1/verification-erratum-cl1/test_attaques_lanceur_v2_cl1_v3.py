"""Essais d'attaque du contre-lecteur, version 3 : ce que l'erratum 1 (commit 11cdc0a9) ouvre de neuf. Chaque essai affirme le
comportement SÛR attendu : un échec = un défaut. Faux outil seulement, aucun réseau, aucune instance."""
import hashlib
import json
import shutil
import sys
from pathlib import Path

ARBRE = Path("/tmp/claude-0/-home-user-controle-ia-travail/43943324-c96f-5191-9f95-633db6e7fd97/scratchpad/developpeur-forme/arbre")
sys.path.insert(0, str(ARBRE / "tests"))

from test_iib_lanceur_forme_v2 import ID, LANCEUR_V2, EMPREINTE_MODULE, _appels, _lancer, poste  # noqa: F401,E402

AUTRE = 58936096
MODULE = ARBRE / "src" / "controle_ia" / "iib" / "location_v1.py"


def _inv(p):
    return [i["id"] for i in json.loads(p["inv"].read_text(encoding="utf-8"))]


def _ligne_instance_fausse(p):
    (p["d"] / "lancement.txt").write_text((p["d"] / "lancement.txt").read_text() + f"instance {AUTRE}\n")


def test_e1_prefixe_partage_sans_l_autre_dans_les_intouchables(poste):
    """L'autre machine n'est pas dans la liste (liste incomplète) ; son étiquette commence par celle du saboteur : l'égalité exacte doit refuser."""
    poste["inv"].write_text(json.dumps([{"id": int(ID), "label": "iib-explo-v1", "actual_status": "exited"},
                                        {"id": AUTRE, "label": "iib-explo-v1-autre-chantier", "actual_status": "exited"}]), encoding="utf-8")
    _ligne_instance_fausse(poste)
    r = _lancer(poste, "destruction", AUTRE, poste["d"], IIB_INSTANCES_INTOUCHABLES="61000001")
    print("E1 :", r.returncode, r.stdout.strip().splitlines()[-1][:140])
    assert r.returncode == 2 and AUTRE in _inv(poste)


def test_e2_attestation_aucune_intouchable_alors_que_le_compte_porte_d_autres_machines(poste):
    """IIB_AUCUNE_INTOUCHABLE=oui alors que l'inventaire d'avant montre d'autres machines : l'attestation est démentie par l'inventaire.
    Cas aggravé : une autre machine porte exactement la même étiquette, et la ligne `instance` est fausse."""
    poste["inv"].write_text(json.dumps([{"id": int(ID), "label": "iib-explo-v1", "actual_status": "exited"},
                                        {"id": AUTRE, "label": "iib-explo-v1", "actual_status": "exited"},
                                        {"id": 61000001, "label": "a1-v4", "actual_status": "running"}]), encoding="utf-8")
    _ligne_instance_fausse(poste)
    r = _lancer(poste, "destruction", AUTRE, poste["d"], IIB_INSTANCES_INTOUCHABLES=None, IIB_AUCUNE_INTOUCHABLE="oui")
    print("E2 :", r.returncode, r.stdout.strip().splitlines()[-1][:140], "| inventaire :", _inv(poste))
    assert r.returncode != 0 and AUTRE in _inv(poste)


def test_e3_attestation_mal_formee_ou_contradictoire(poste):
    for sup in ({"IIB_INSTANCES_INTOUCHABLES": None}, {"IIB_INSTANCES_INTOUCHABLES": "", "IIB_AUCUNE_INTOUCHABLE": "yes"},
                {"IIB_AUCUNE_INTOUCHABLE": "oui"}, {"IIB_INSTANCES_INTOUCHABLES": None, "IIB_AUCUNE_INTOUCHABLE": "OUI"}):
        r = _lancer(poste, "destruction", ID, poste["d"], **sup)
        print("E3", sup, "->", r.returncode)
        assert r.returncode == 2 and not any(a.startswith("destroy") for a in _appels(poste))


def _arbre_menteur(tmp_path):
    arbre = tmp_path / "arbre-copie"
    (arbre / "scripts").mkdir(parents=True)
    shutil.copy(LANCEUR_V2, arbre / "scripts" / LANCEUR_V2.name)
    m = arbre / "src" / "controle_ia" / "iib" / "location_v1.py"
    m.parent.mkdir(parents=True)
    m.write_text('import sys\nif sys.argv[1] == "inventaire":\n    open(sys.argv[3], "w").write("{}")\n'
                 '    print("n=2 etat=present etiquette=iib-explo-v1 statut=exited autres_manquants=0")\n'
                 'elif sys.argv[1] == "masquer-en-place":\n    print("0 structure")\n', encoding="utf-8")
    return arbre / "scripts" / LANCEUR_V2.name, hashlib.sha256(m.read_bytes()).hexdigest()


def test_e4_empreinte_du_module_fournie_par_l_environnement_seule(poste, tmp_path):
    """Sans config.json dans le dossier (ou config sans l'empreinte du module), IIB_LOCATION_SHA256 seule fait foi : un module
    remplacé passe si l'environnement donne SON empreinte. L'essai affirme le comportement sûr (refus)."""
    script, h = _arbre_menteur(tmp_path)
    r = _lancer(poste, "destruction", ID, poste["d"], script=script, IIB_LOCATION_SHA256=h)
    print("E4 : module menteur + empreinte de l'environnement ->", r.returncode, r.stdout.strip().splitlines()[-1][:120],
          "| destroy envoyé :", any(a.startswith("destroy") for a in _appels(poste)))
    assert not any(a.startswith("destroy") for a in _appels(poste))


def test_e5_configuration_et_environnement_contradictoires(poste, tmp_path):
    """La configuration du dossier porte l'empreinte du vrai module ; l'environnement en donne une autre : refus. Puis la
    configuration seule (sans variable) contre un module remplacé : refus."""
    (poste["d"] / "config.json").write_text(json.dumps({"marqueurs": {"EMPREINTES_CODE_IIB":
        f"au commit x : scripts/lancer_iib_v2.sh {'0' * 64} ; src/controle_ia/iib/location_v1.py {EMPREINTE_MODULE} ; fin"}}), encoding="utf-8")
    script, h = _arbre_menteur(tmp_path)
    r1 = _lancer(poste, "destruction", ID, poste["d"], script=script, IIB_LOCATION_SHA256=h)
    r2 = _lancer(poste, "destruction", ID, poste["d"], script=script, IIB_LOCATION_SHA256=None)
    r3 = _lancer(poste, "destruction", ID, poste["d"], IIB_LOCATION_SHA256=None)        # sain : vrai module, configuration seule
    print("E5 : contradiction ->", r1.returncode, "| configuration seule, module remplacé ->", r2.returncode, "| sain, configuration seule ->", r3.returncode)
    assert r1.returncode == 4 and r2.returncode == 4 and r3.returncode == 0
    assert [a for a in _appels(poste) if a.startswith("destroy")] == [f"destroy instance {ID} -y"]


def test_e6_refus_de_l_etat_n_ecrit_pas_d_attestation_de_rapatriement(poste):
    """Un refus (état « running ») ne doit pas laisser de ligne `rapatriement_atteste` dans lancement.txt."""
    poste["inv"].write_text(json.dumps([{"id": int(ID), "label": "iib-explo-v1", "actual_status": "running"},
                                        {"id": AUTRE, "label": "a1-v4", "actual_status": "running"}]), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"])
    t = (poste["d"] / "lancement.txt").read_text(encoding="utf-8")
    print("E6 :", r.returncode, "| ligne d'attestation écrite :", "rapatriement_atteste" in t)
    assert r.returncode == 2 and "rapatriement_atteste" not in t
