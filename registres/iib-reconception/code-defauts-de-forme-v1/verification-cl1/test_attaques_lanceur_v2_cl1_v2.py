"""Essais d'attaque du contre-lecteur, version 2 (vérification des corrections du commit 806bce0f). Chaque essai affirme le
comportement SÛR attendu : un échec = un défaut. Faux outil de location seulement, aucun réseau, aucune instance."""
import json
import shutil
import sys
from pathlib import Path

ARBRE = Path("/tmp/claude-0/-home-user-controle-ia-travail/43943324-c96f-5191-9f95-633db6e7fd97/scratchpad/developpeur-forme/arbre")
sys.path.insert(0, str(ARBRE / "tests"))

from test_iib_lanceur_forme_v2 import ID, LANCEUR_V2, _apres, _appels, _lancer, _traces, poste  # noqa: F401,E402

AUTRE = 58936096


def _consigne(p):
    return [l for l in (p["d"] / "lancement.txt").read_text(encoding="utf-8").splitlines() if l.startswith("instance ")]


def _inv(p):
    return [i["id"] for i in json.loads(p["inv"].read_text(encoding="utf-8"))]


def _sans_instance(p):
    t = (p["d"] / "lancement.txt").read_text(encoding="utf-8")
    (p["d"] / "lancement.txt").write_text("\n".join(l for l in t.splitlines() if not l.startswith("instance ")) + "\n", encoding="utf-8")


# --- les sept attaques de la contre-lecture, rejouées ----------------------------------------------------------------------
def test_a1_reponse_piegee(poste):
    _sans_instance(poste)
    _, r = _apres(poste, '{"msg": "previous new_contract: %d released", "success": true, "new_contract": 777777}' % AUTRE, 0)
    print("A1 :", r.returncode, r.stdout.strip().splitlines()[-1][:160], "| consigné :", _consigne(poste))
    assert r.returncode == 4 and _consigne(poste) == []
    (poste["d"] / "lancement.txt").write_text((poste["d"] / "lancement.txt").read_text() + f"instance {AUTRE}\n")   # pire cas : ligne fausse
    r2 = _lancer(poste, "destruction", AUTRE, poste["d"])
    print("A1 bis (ligne instance fausse) :", r2.returncode, r2.stdout.strip().splitlines()[-1][:160])
    assert AUTRE in _inv(poste) and r2.returncode == 2


def test_a2_inventaire_vide(poste):
    poste["inv"].write_text("[]", encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"])
    print("A2 :", r.returncode, r.stdout.strip().splitlines()[-1][:120])
    assert r.returncode == 7 and "destruction_verifiee" not in (poste["d"] / "lancement.txt").read_text(encoding="utf-8")


def test_a3_erreur_apres_destruction_puis_inventaire_illisible(poste):
    f = poste["outil"].read_text(encoding="utf-8").replace('[ "${FAUX_INVENTAIRE_ILLISIBLE:-}" = 1 ]', 'grep -q "^destroy" "$FAUX_VASTAI_JOURNAL"', 1)
    poste["outil"].write_text(f, encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"], FAUX_DESTRUCTION="echec-mais-retire")
    print("A3 :", r.returncode, r.stdout.strip().splitlines()[-1][:120])
    assert r.returncode == 4 and "DÉTRUITE" not in r.stdout
    assert [a for a in _appels(poste) if a.startswith("destroy")] == [f"destroy instance {ID} -y"]


def test_a4_identifiants_pieges(poste):
    for ident in (f"0{ID}", f"{ID} ", f"{ID}\n", "", "-1"):
        r = _lancer(poste, "destruction", ident, poste["d"])
        print("A4", repr(ident), "->", r.returncode)
        assert r.returncode == 2 and not any(a.startswith("destroy") for a in _appels(poste))


def test_a5_secret_d_une_autre_machine(poste):
    secret = "sk-autreChantier-0123456789abcdef"
    poste["inv"].write_text(json.dumps([{"id": int(ID), "label": "iib-explo-v1", "actual_status": "exited"},
                                        {"id": AUTRE, "label": "a1-v4", "actual_status": "running", "jupyter_token": "jt0123456789abcdef0123",
                                         "extra_env": [["WANDB_ENTITY", "neutre-0123456789"], ["OPENAI_API_KEY", secret]]}]), encoding="utf-8")
    _lancer(poste, "destruction", ID, poste["d"])
    tout = "".join(f.read_text(encoding="utf-8", errors="replace") for f in poste["d"].rglob("*") if f.is_file())
    print("A5 secret / jeton / valeur neutre dans le dossier :", secret in tout, "jt0123456789abcdef0123" in tout, "neutre-0123456789" in tout)
    assert secret not in tout and "jt0123456789abcdef0123" not in tout


def test_a6_secret_en_paire(poste):
    secret = "sk-inconnu-0123456789abcdef"
    autre = "zz-sansprefixe-0123456789"
    _apres(poste, json.dumps({"success": False, "error": "x", "extra_env": [["MY_API_KEY", secret], ["My_Db_Passwd", autre]]}), 1)
    (copie,) = _traces(poste, "creation-brute-")
    t = copie.read_text(encoding="utf-8")
    print("A6 :", secret in t, autre in t)
    assert secret not in t and autre not in t


def test_a7_destruction_rejouee_aucune_ecrasee(poste):
    r1 = _lancer(poste, "destruction", ID, poste["d"], FAUX_DESTRUCTION="echec")
    r2 = _lancer(poste, "destruction", ID, poste["d"])
    sorties = sorted(p.name for p in poste["d"].glob("destruction-sortie-*"))
    traces = _traces(poste, "destruction-sortie-")
    print("A7 :", r1.returncode, r2.returncode, "| sorties de travail :", len(sorties), "| traces :", len(traces))
    assert r1.returncode == 6 and r2.returncode == 0 and len(traces) == 2 and traces[0].read_bytes() != traces[1].read_bytes()


# --- ce que les corrections ouvrent de neuf --------------------------------------------------------------------------------
def test_n1_etats_arret_elargis_detruisent_une_instance_qui_tourne(poste):
    """IIB_DESTRUCTION_ETATS_ARRET élargie à « running » : la garde d'état tombe (porte explicite, point à trancher 3)."""
    poste["inv"].write_text(json.dumps([{"id": int(ID), "label": "iib-explo-v1", "actual_status": "running"},
                                        {"id": AUTRE, "label": "a1-v4", "actual_status": "running"}]), encoding="utf-8")
    r0 = _lancer(poste, "destruction", ID, poste["d"])
    r = _lancer(poste, "destruction", ID, poste["d"], IIB_DESTRUCTION_ETATS_ARRET="running")
    print("N1 : défaut ->", r0.returncode, "| élargie à running ->", r.returncode, r.stdout.strip().splitlines()[-1][:100])
    assert r0.returncode == 2
    assert r.returncode == 2, "un réglage d'environnement suffit à détruire une instance qui tourne"


def test_n2_etiquette_d_une_autre_machine_au_meme_prefixe(poste):
    """Autre machine dont l'étiquette commence par celle du saboteur, avec une ligne `instance` fausse."""
    poste["inv"].write_text(json.dumps([{"id": int(ID), "label": "iib-explo-v1", "actual_status": "exited"},
                                        {"id": AUTRE, "label": "iib-explo-v1-autre-chantier", "actual_status": "exited"}]), encoding="utf-8")
    (poste["d"] / "lancement.txt").write_text((poste["d"] / "lancement.txt").read_text() + f"instance {AUTRE}\n")
    r = _lancer(poste, "destruction", AUTRE, poste["d"])
    print("N2 : préfixe partagé ->", r.returncode, r.stdout.strip().splitlines()[-1][:100])
    assert r.returncode == 2 and AUTRE in _inv(poste)


def test_n3_listes_d_intouchables_mal_formees(poste):
    for liste in (f" {AUTRE}", f"{AUTRE},", f"0{AUTRE}", f"{AUTRE};{ID}", "a1-v4"):
        r = _lancer(poste, "destruction", ID, poste["d"], IIB_INSTANCES_INTOUCHABLES=liste)
        print("N3", repr(liste), "->", r.returncode)
        assert r.returncode == 2 and not any(a.startswith("destroy") for a in _appels(poste))


def test_n4_reponses_json_pieges(poste):
    _sans_instance(poste)
    cas = {"cle_en_double": '{"success": true, "new_contract": %d, "new_contract": 777777}' % AUTRE,
           "identifiant_en_chaine": '{"success": true, "new_contract": "777777"}',
           "imbrique": '{"success": true, "new_contract": 777777, "detail": {"new_contract": %d}}' % AUTRE,
           "echappe_dans_texte": '{"success": true, "new_contract": 777777, "msg": "new_contract\\": %d"}' % AUTRE,
           "repr_python": "{'success': True, 'new_contract': 777777}",
           "decimal": '{"success": true, "new_contract": 777777.0}',
           "texte_avant": 'Started. {"success": true, "new_contract": 777777}'}
    for nom, rep in cas.items():
        _, r = _apres(poste, rep, 0)
        print("N4", nom, "->", r.returncode, _consigne(poste))
        assert r.returncode == 4 and _consigne(poste) == [], nom


def test_n5_module_de_lecture_absent_ou_remplace(poste, tmp_path):
    """Lanceur copié dans un arbre sans `src/controle_ia/iib/location_v1.py`, puis avec un module remplacé qui ment."""
    arbre = tmp_path / "arbre-copie"
    (arbre / "scripts").mkdir(parents=True)
    shutil.copy(LANCEUR_V2, arbre / "scripts" / LANCEUR_V2.name)
    script = arbre / "scripts" / LANCEUR_V2.name
    _sans_instance(poste)
    f = poste["d"] / "creation-brute-x.json"
    f.write_text('{"success": true, "new_contract": 777777, "api_key": "sk-secret-0123456789abcdef"}', encoding="utf-8")
    r = _lancer(poste, "apres-creation", f, 0, poste["d"], script=script)
    print("N5 module absent, après création ->", r.returncode, "| consigné :", _consigne(poste), "| fichiers :", sorted(x.name for x in poste["d"].glob("creation-brute-x*")))
    assert r.returncode == 4 and _consigne(poste) == []
    (poste["d"] / "lancement.txt").write_text((poste["d"] / "lancement.txt").read_text() + f"instance {ID}\n")
    r = _lancer(poste, "destruction", ID, poste["d"], script=script)
    print("N5 module absent, destruction ->", r.returncode, r.stdout.strip().splitlines()[-1][:110])
    assert r.returncode == 4 and not any(a.startswith("destroy") for a in _appels(poste))
    # module remplacé qui ment (rend toujours « present », étiquette et état conformes) : le lanceur lui fait confiance
    (arbre / "src" / "controle_ia" / "iib").mkdir(parents=True)
    (arbre / "src" / "controle_ia" / "iib" / "location_v1.py").write_text(
        'import sys\nif sys.argv[1] == "inventaire":\n    open(sys.argv[3], "w").write("{}")\n'
        '    print("n=2 etat=present etiquette=iib-explo-v1 statut=exited autres_manquants=0")\n'
        'elif sys.argv[1] == "masquer-en-place":\n    print("0 structure")\n', encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"], script=script)
    print("N5 module menteur, destruction ->", r.returncode, r.stdout.strip().splitlines()[-1][:110])
    # pas d'affirmation de sûreté ici : le module fait partie du code de confiance ; l'essai montre seulement qu'il n'est pas vérifié
