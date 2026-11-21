"""Essais d'attaque du contre-lecteur (lanceur v2). Chaque essai affirme le comportement SÛR attendu : un échec = un défaut trouvé.
Faux outil de location seulement (celui des essais du développeur), aucun réseau, aucune instance."""
import json
import sys
from pathlib import Path

ARBRE = Path("/tmp/claude-0/-home-user-controle-ia-travail/43943324-c96f-5191-9f95-633db6e7fd97/scratchpad/developpeur-forme/arbre")
sys.path.insert(0, str(ARBRE / "tests"))

from test_iib_lanceur_forme_v2 import ID, _apres, _appels, _lancer, _traces, poste  # noqa: F401,E402

AUTRE = 58936096      # machine d'un autre chantier (« intouchable »), présente à l'inventaire du poste


def _lancement_sans_instance(p):
    (p["d"] / "lancement.txt").write_text("machine_proposee 101\ncarte course\nanterieure 0\necheance 4102444800\nmode jouet\n", encoding="utf-8")


def test_attaque_1_reponse_piegee_ne_doit_pas_faire_detruire_une_autre_machine(poste):
    """Réponse du loueur piégée : un message cite « new_contract: <autre> » AVANT le vrai champ. Le lanceur ne doit ni consigner
    l'autre identifiant ni pouvoir ensuite le détruire."""
    _lancement_sans_instance(poste)
    reponse = '{"msg": "previous new_contract: %d released", "success": true, "new_contract": 777777}' % AUTRE
    _, r = _apres(poste, reponse, 0)
    consigne = [l for l in (poste["d"] / "lancement.txt").read_text(encoding="utf-8").splitlines() if l.startswith("instance ")]
    print("APRES-CREATION :", r.returncode, r.stdout.strip().splitlines()[-1], "| consigné :", consigne)
    r2 = _lancer(poste, "destruction", str(AUTRE), poste["d"])
    restantes = [i["id"] for i in json.loads(poste["inv"].read_text(encoding="utf-8"))]
    print("DESTRUCTION de l'autre :", r2.returncode, r2.stdout.strip().splitlines()[-1], "| inventaire :", restantes)
    assert AUTRE in restantes, "la machine d'un autre chantier a été détruite"
    assert consigne == ["instance 777777"] or r.returncode != 0


def test_attaque_2_inventaire_vide_par_erreur_ne_vaut_pas_preuve(poste):
    """Inventaire rendu vide (liste vide, par exemple sur une erreur du compte ou un filtre) alors que l'instance existe :
    le lanceur ne doit pas conclure par le code 0 « déjà absente » ni écrire `destruction_verifiee`."""
    poste["inv"].write_text("[]", encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"])
    print("INVENTAIRE VIDE :", r.returncode, r.stdout.strip())
    assert not (r.returncode == 0 and "destruction_verifiee" in (poste["d"] / "lancement.txt").read_text(encoding="utf-8"))


def test_attaque_3_outil_en_erreur_apres_avoir_detruit_et_inventaire_illisible_ensuite(poste):
    """L'outil détruit puis rend le code 1 ; l'inventaire devient ensuite illisible : jamais « DÉTRUITE », code 4, une seule commande."""
    faux = poste["outil"].read_text(encoding="utf-8")
    faux = faux.replace('[ "${FAUX_INVENTAIRE_ILLISIBLE:-}" = 1 ]', 'grep -q "^destroy" "$FAUX_VASTAI_JOURNAL"', 1)
    poste["outil"].write_text(faux, encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"], FAUX_DESTRUCTION="echec-mais-retire")
    print("ERREUR APRES DESTRUCTION :", r.returncode, r.stdout.strip().splitlines()[-1])
    assert r.returncode == 4 and "DÉTRUITE" not in r.stdout
    assert [a for a in _appels(poste) if a.startswith("destroy")] == [f"destroy instance {ID} -y"]


def test_attaque_4_identifiants_pieges(poste):
    """Zéro de tête, espace final, ligne `instance` en double (deux créations) : refus ou seul le dernier identifiant consigné."""
    for ident in (f"0{ID}", f"{ID} ", f"{ID}\n", "", "-1"):
        r = _lancer(poste, "destruction", ident, poste["d"])
        print("IDENTIFIANT", repr(ident), "->", r.returncode, r.stdout.strip()[:90])
        assert r.returncode == 2 and not any(a.startswith("destroy") for a in _appels(poste))


def test_attaque_5_secret_d_une_autre_machine_dans_l_inventaire_verse(poste):
    """L'inventaire du compte porte les variables d'environnement des autres machines (forme des paires de l'outil réel :
    `extra_env`), avec des secrets inconnus de l'environnement du poste. Ils ne doivent pas être versés en clair aux traces."""
    secret = "sk-autreChantier-0123456789abcdef"
    inv = [{"id": int(ID), "label": "iib-explo-v1", "actual_status": "exited"},
           {"id": AUTRE, "label": "a1-v4", "actual_status": "running", "jupyter_token": "jt0123456789abcdef0123",
            "extra_env": [["OPENAI_API_KEY", secret], ["-e WANDB", "x"]]}]
    poste["inv"].write_text(json.dumps(inv), encoding="utf-8")
    _lancer(poste, "destruction", ID, poste["d"])
    fuites = [t.name for t in _traces(poste, "instances-") if secret in t.read_text(encoding="utf-8") or "jt0123456789abcdef0123" in t.read_text(encoding="utf-8")]
    print("TRACES D'INVENTAIRE AVEC SECRET EN CLAIR :", fuites)
    assert fuites == []


def test_attaque_6_secret_en_paire_dans_la_reponse_de_creation(poste):
    """Réponse de création qui renvoie l'environnement en paires (forme `extra_env`), secret absent de l'environnement local."""
    secret = "sk-inconnu-0123456789abcdef"
    _apres(poste, json.dumps({"success": False, "error": "x", "extra_env": [["MY_API_KEY", secret]]}), 1)
    (copie,) = _traces(poste, "creation-brute-")
    print("SECRET EN PAIRE DANS LA COPIE :", secret in copie.read_text(encoding="utf-8"))
    assert secret not in copie.read_text(encoding="utf-8")


def test_attaque_7_destruction_rejouee_n_ecrase_aucune_trace(poste):
    """R12 : une seconde destruction (code 6 la première fois) ne doit écraser aucun fichier de sortie du dossier."""
    _lancer(poste, "destruction", ID, poste["d"], FAUX_DESTRUCTION="echec")
    premiere = (poste["d"] / "destruction-sortie.txt").read_text(encoding="utf-8")
    _lancer(poste, "destruction", ID, poste["d"])
    seconde = (poste["d"] / "destruction-sortie.txt").read_text(encoding="utf-8")
    print("destruction-sortie.txt, 1re puis 2e :", repr(premiere[:40]), "->", repr(seconde[:40]),
          "| copies datées :", len(_traces(poste, "destruction-sortie-")))
    assert premiere == seconde
