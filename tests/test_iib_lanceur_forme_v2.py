"""Saboteur à budget, chaîne de session v2 (`scripts/lancer_iib_v2.sh`) : les trois défauts de forme relevés le 19 novembre 2026,
éprouvés **à blanc** avec un faux outil de location (aucun réseau, aucune instance, aucune dépense), cas sain et artefact (R5) :
 (1) chemin explicite de l'outil de location par la variable VAST (R-3683) : vérifié, dit dans le journal, refus clair s'il est
     introuvable ; sans variable, recherche dans le PATH comme la v1 ;
 (2) la réponse brute du loueur n'est plus supprimée par `apres-creation` (R-3687) : copie datée, empreinte, secrets masqués, dans les
     trois issues (créée, offre refusée, création incertaine) ;
 (3) destruction par le seul identifiant créé, avec l'option de confirmation non interactive `-y`, puis preuve par l'inventaire (R-3722).
Les essais du lanceur v1 qui passent par le script (`tests/test_iib_scripts_v1.py`) sont rejoués ici contre la v2 (non-régression)."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import time
from pathlib import Path

import pytest

import test_iib_scripts_v1 as v1s
from test_iib_scripts_v1 import (  # noqa: F401  (rejoués contre la v2 par le dispositif `lanceur_v2_partout`)
    SAIN, _controles, _env, _instances, monde,
    test_controles_explo_artefacts, test_controles_explo_sain, test_creation_artefact_7b_retiree_du_registre_entre_controles_et_creation,
    test_creation_artefact_instance_iib_presente_refus, test_creation_artefact_relance_h200_en_variante_b_noeud,
    test_creation_relance_permise_en_variante_a, test_creation_sain_commande_imprimee, test_surveillance_fin_et_arret_par_identifiant,
    test_verifier_go_seulement_artefacts, test_verifier_go_seulement_sain_ne_cree_rien)

RACINE = Path(__file__).resolve().parents[1]
LANCEUR_V1 = RACINE / "scripts" / "lancer_iib_v1.sh"
LANCEUR_V2 = RACINE / "scripts" / "lancer_iib_v2.sh"
EMPREINTE_LANCEUR_V1 = "3279e3dcc631519e574c2011f9f143d956d3b668c729a176cd8efc0e99dece8f"      # citée par l'ordre scellé de la première course
ID = "61414494"
JETON_HF, JETON_GH, CLE_LOUEUR = "hf_FACTICEfactice0123456789", "ghp_FACTICEfactice0123456789", "cle-loueur-factice-0123456789abcdef"

# Faux outil de location. `--version` rend une version ; `create instance` rend le fichier FAUX_REPONSE et le code FAUX_CODE ;
# `show instances` rend l'inventaire FAUX_INSTANCES ; `destroy instance ID` EXIGE `-y` : sans cette option il demande une confirmation
# sur l'entrée standard, comme l'outil réel, et échoue si personne ne répond ; avec elle, il retire l'identifiant de l'inventaire, sauf
# FAUX_DESTRUCTION=sans-effet (code 0, instance gardée), =echec (code 1, instance gardée) ou =echec-mais-retire (code 1, retirée).
FAUX_OUTIL = r"""#!/usr/bin/env bash
echo "$*" >> "$FAUX_VASTAI_JOURNAL"
[ "${FAUX_MUET:-}" = 1 ] && [ "$1" = --version ] && exit 3
[ "$1" = --version ] && { echo "vastai 1.8.3-factice"; exit 0; }
case "$1 $2" in
"create instance") cat "$FAUX_REPONSE"; exit "${FAUX_CODE:-0}" ;;
"show instances")
    [ "${FAUX_INVENTAIRE_ILLISIBLE:-}" = 1 ] && { echo "<html>erreur 502</html>"; exit 0; }
    cat "$FAUX_INSTANCES"; exit 0 ;;
"destroy instance")
    oui=non; for a in "$@"; do [ "$a" = -y ] && oui=oui; done
    if [ "$oui" = non ]; then
        printf 'Are you sure you want to destroy instance %s? [y/N] ' "$3"
        read -r rep || { echo "Aborted: no confirmation"; exit 1; }
        [ "$rep" = y ] || { echo "Aborted"; exit 1; }
    fi
    case "${FAUX_DESTRUCTION:-}" in sans-effet) echo "destroying instance $3."; exit 0 ;; echec) echo "failed with error 500 ; Authorization: Bearer $VAST_API_KEY"; exit 1 ;; esac
    python3 - "$FAUX_INSTANCES" "$3" <<'PY'
import json, sys
l = json.load(open(sys.argv[1]))
json.dump([i for i in l if str(i["id"]) != sys.argv[2]], open(sys.argv[1], "w"))
PY
    [ "${FAUX_DESTRUCTION:-}" = echec-mais-retire ] && { echo "erreur de lecture de la réponse"; exit 1; }
    echo "destroying instance $3."; exit 0 ;;
esac
if [ "$1" = logs ]; then cat "$FAUX_JOURNAL"; exit 0; fi
echo "appel inattendu : $*" >&2; exit 3
"""


@pytest.fixture(autouse=True)
def lanceur_v2_partout(monkeypatch):
    """Les essais repris de la v1 lancent la v2."""
    monkeypatch.setattr(v1s, "LANCEUR", LANCEUR_V2)


@pytest.fixture
def poste(tmp_path):
    """Poste de l'exécutante : outil de location installé HORS du PATH (comme `/home/user/outil-vastai-v1/bin/vastai`), dossier de session."""
    outil = tmp_path / "outil-vastai-factice" / "bin" / "vastai"
    outil.parent.mkdir(parents=True)
    outil.write_text(FAUX_OUTIL, encoding="utf-8")
    outil.chmod(0o755)
    d = tmp_path / "session"
    d.mkdir()
    (d / "lancement.txt").write_text(f"controles-explo iib v1 x\nmachine_proposee 101\ncarte course\nanterieure 0\necheance 4102444800\n"
                                     f"instance {ID}\ncreation {int(time.time()) - 60}\nprix_carte 1.0\nprix_stockage 0.03\n"
                                     f"telechargement_forfait 1.0\nplafond_creation 55\nmode jouet\n", encoding="utf-8")
    inv = tmp_path / "inventaire.json"
    inv.write_text(json.dumps([{"id": int(ID), "label": "iib-explo-v1", "actual_status": "exited"},
                               {"id": 58936096, "label": "a1-v4", "actual_status": "running"}]), encoding="utf-8")
    (tmp_path / "journal.txt").write_text("AMORCE 2026-11-19T10:00:00Z : fin, code 0\n", encoding="utf-8")
    return {"tmp": tmp_path, "outil": outil, "d": d, "inv": inv, "appels": tmp_path / "appels.txt"}


def _lancer(p, *args, **sup):
    e = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": str(p["tmp"]), "LANG": os.environ.get("LANG", "C.UTF-8"), "IIB_DEPOT": str(RACINE),
         "VAST": str(p["outil"]), "FAUX_VASTAI_JOURNAL": str(p["appels"]), "FAUX_INSTANCES": str(p["inv"]), "FAUX_JOURNAL": str(p["tmp"] / "journal.txt"),
         "HF_TOKEN": JETON_HF, "CONTROLE_IA_GITHUB_TOKEN_2": JETON_GH, "VAST_API_KEY": CLE_LOUEUR, "INTERVALLE": "1",
         "IIB_DESTRUCTION_ATTENTE_S": "0", "IIB_DESTRUCTION_RELECTURES": "2"}
    e.update(sup)
    e = {k: v for k, v in e.items() if v is not None}
    return subprocess.run(["bash", str(LANCEUR_V2), *map(str, args)], env=e, capture_output=True, text=True, timeout=120, stdin=subprocess.DEVNULL)


def _appels(p) -> list:
    return p["appels"].read_text(encoding="utf-8").splitlines() if p["appels"].exists() else []


def _traces(p, prefixe) -> list:
    return sorted(f for f in (p["d"] / "traces-location").glob(prefixe + "*") if not f.name.endswith(".sha256"))


def _empreinte_tenue(f: Path) -> bool:
    return (f.parent / (f.name + ".sha256")).read_text(encoding="utf-8").split()[0] == hashlib.sha256(f.read_bytes()).hexdigest()


def test_la_v1_citee_par_l_ordre_scelle_est_intacte():
    """R12 : la version lancée le 19 novembre n'est pas réécrite ; la v2 est un fichier neuf."""
    assert hashlib.sha256(LANCEUR_V1.read_bytes()).hexdigest() == EMPREINTE_LANCEUR_V1
    assert LANCEUR_V2.read_bytes() != LANCEUR_V1.read_bytes()


# --- (1) chemin de l'outil de location --------------------------------------------------------------------------------------
def test_outil_sain_chemin_explicite_hors_du_path(poste):
    r = _lancer(poste, "outil")
    assert r.returncode == 0, r.stdout + r.stderr
    assert f"outil de location employé : {poste['outil']} (version : vastai 1.8.3-factice ; trouvé par : variable VAST)" in r.stdout
    assert _appels(poste) == ["--version", "--version"]                       # aucun autre appel : rien n'est créé ni lu


def test_outil_sain_chemin_relatif_rendu_absolu(poste):
    lien = poste["tmp"] / "lien-vastai"
    lien.symlink_to(poste["outil"])
    r = _lancer(poste, "outil", VAST=str(lien))
    assert r.returncode == 0 and f"employé : {poste['outil']} " in r.stdout, r.stdout + r.stderr


@pytest.mark.parametrize("cas, motif", [("absent", "n'existe pas"), ("non_executable", "n'est pas exécutable"), ("muet", "ne rend pas sa version"),
                                        ("nom_nu", "n'est pas un chemin"), ("dossier", "n'est pas un fichier"), ("espace", "hors de [A-Za-z0-9_./+-]")])
def test_outil_artefacts_refus_clair(poste, cas, motif):
    sup = {}
    if cas == "absent":
        sup["VAST"] = str(poste["tmp"] / "nulle-part" / "vastai")
    elif cas == "non_executable":
        poste["outil"].chmod(0o644)
    elif cas == "muet":
        sup["FAUX_MUET"] = "1"
    elif cas == "nom_nu":
        sup["VAST"] = "vastai"
    elif cas == "dossier":
        sup["VAST"] = str(poste["outil"].parent)
    elif cas == "espace":
        autre = poste["tmp"] / "dossier avec espace" / "vastai"
        autre.parent.mkdir()
        shutil.copy(poste["outil"], autre)
        autre.chmod(0o755)
        sup["VAST"] = str(autre)
    r = _lancer(poste, "outil", **sup)
    assert r.returncode == 2 and motif in r.stdout and "VÉRIFIÉ" not in r.stdout, (cas, r.stdout + r.stderr)
    # le refus vaut aussi pour la destruction et la surveillance : aucun appel au loueur au-delà de la demande de version
    for sous_commande in ("destruction", "surveillance"):
        r = _lancer(poste, sous_commande, ID, poste["d"], **sup)
        assert r.returncode == 2 and motif in r.stdout, (cas, sous_commande, r.stdout + r.stderr)
    assert all(a == "--version" for a in _appels(poste))


def test_outil_sans_variable_recherche_dans_le_path_comme_la_v1(poste):
    r = _lancer(poste, "outil", VAST=None)                                     # artefact : ni variable ni outil dans le PATH
    assert r.returncode == 2 and "introuvable dans le PATH" in r.stdout and "VAST=/chemin" in r.stdout, r.stdout + r.stderr
    r = _lancer(poste, "outil", VAST=None, PATH=f"{poste['outil'].parent}:/usr/local/bin:/usr/bin:/bin")       # sain
    assert r.returncode == 0 and f"employé : {poste['outil']} (version : vastai 1.8.3-factice ; trouvé par : PATH)" in r.stdout, r.stdout + r.stderr
    # outil du PATH qui ne rend pas sa version : accepté comme en v1, et dit
    r = _lancer(poste, "outil", VAST=None, PATH=f"{poste['outil'].parent}:/usr/local/bin:/usr/bin:/bin", FAUX_MUET="1")
    assert r.returncode == 0 and "version : non rendue" in r.stdout, r.stdout + r.stderr


def test_surveillance_dit_l_outil_dans_son_journal_et_imprime_son_chemin(poste):
    r = _lancer(poste, "surveillance", ID, poste["d"])
    assert r.returncode == 0 and f"{poste['outil']} stop instance {ID}" in r.stdout, r.stdout + r.stderr
    assert f"outil de location employé : {poste['outil']} (version : vastai 1.8.3-factice" in (poste["d"] / "surveillance.txt").read_text(encoding="utf-8")


def test_creation_de_bout_en_bout_avec_un_outil_hors_du_path(monde, tmp_path):
    """La commande de création imprimée porte le chemin absolu de l'outil, pour la création comme pour `apres-creation` ; exécutée telle
    quelle, sans outil dans le PATH, elle crée (faux outil), conserve la réponse brute masquée et rend « CRÉÉE »."""
    shutil.copy(LANCEUR_V2, monde["src"] / "scripts" / LANCEUR_V2.name)
    outil = tmp_path / "outil-vastai-factice" / "bin" / "vastai"
    outil.parent.mkdir(parents=True)
    outil.write_text(FAUX_OUTIL, encoding="utf-8")
    outil.chmod(0o755)
    (monde["bin"] / "vastai").rename(monde["tmp"] / "vastai-du-path-retire")        # plus aucun `vastai` dans le PATH
    reponse = tmp_path / "reponse.json"
    reponse.write_text(json.dumps({"success": True, "new_contract": 777777, "requete": f"-e HF_TOKEN={JETON_HF} -e GH_TOKEN=jeton-gh-factice"}), encoding="utf-8")
    sup = dict(VAST=str(outil), FAUX_INSTANCES=_instances(monde, []), FAUX_REPONSE=str(reponse), HF_TOKEN=JETON_HF)
    d, r = _controles(monde, **sup)
    assert r.returncode == 0, r.stdout + r.stderr
    # artefact : sans la variable, et sans outil dans le PATH, refus clair et aucune commande imprimée
    r = v1s._lancer(monde, "creation", "auto", "course", "0", d, **{**sup, "VAST": None})
    assert r.returncode == 2 and "introuvable dans le PATH" in r.stdout and "COMMANDE DE CRÉATION" not in r.stdout, r.stdout + r.stderr
    # la recherche des offres du faux outil de ce fichier n'existe pas : celle des essais de la v1 est reprise par un outil complet
    outil.write_text(FAUX_OUTIL.replace('case "$1 $2" in\n"create instance")', 'case "$1 $2" in\n"search offers") cat "$FAUX_OFFRES"; exit 0 ;;\n"create instance")', 1), encoding="utf-8")
    r = v1s._lancer(monde, "creation", "auto", "course", "0", d, **sup)
    assert r.returncode == 0, r.stdout + r.stderr
    assert f"outil de location employé : {outil} (version : vastai 1.8.3-factice ; trouvé par : variable VAST)" in r.stdout
    assert f"outil_location {outil}\n" in (d / "lancement.txt").read_text(encoding="utf-8")
    cmd = r.stdout.splitlines()[-1]
    assert f"timeout -k 10 300 {outil} create instance " in cmd and f"; VAST={outil} bash {monde['src']}/scripts/lancer_iib_v2.sh apres-creation " in cmd
    assert "lancer_iib_v1.sh" not in cmd and JETON_HF not in cmd and "jeton-gh-factice" not in cmd
    assert len(_traces({"d": d}, "offres-")) == 1 and len(_traces({"d": d}, "instances-")) == 1         # sorties de la location versées
    e = _env(monde, **sup)
    e.pop("VAST")                                                              # la commande imprimée se suffit : chemin absolu écrit dedans
    r = subprocess.run(["bash", "-c", cmd], env=e, capture_output=True, text=True, timeout=120, cwd=str(monde["src"]))
    assert r.returncode == 0 and "CRÉÉE : instance 777777" in r.stdout and "RÉPONSE BRUTE DU LOUEUR CONSERVÉE" in r.stdout, r.stdout + r.stderr
    (copie,) = _traces({"d": d}, "creation-brute-")
    texte = copie.read_text(encoding="utf-8")
    assert _empreinte_tenue(copie) and "777777" in texte and JETON_HF not in texte and "jeton-gh-factice" not in texte
    assert (d / "creation-brute.json").read_text(encoding="utf-8") == texte


# --- (2) réponse brute du loueur conservée ----------------------------------------------------------------------------------
REPONSE_SAINE = {"success": True, "new_contract": 777777}
REPONSE_REFUS = {"success": False, "error": "no_such_ask", "msg": "offre retirée"}
REPONSE_ILLISIBLE = ("Traceback (most recent call last):\n  requests.exceptions.HTTPError: 402 Payment Required\n"
                     f"request: PUT /asks/61361283/ headers={{'Authorization': 'Bearer {CLE_LOUEUR}'}}\n"
                     f"env: -e HF_TOKEN={JETON_HF} -e GH_TOKEN={JETON_GH} api_key={CLE_LOUEUR}\n"
                     '{"detail": "lacks credit", "api_key": "une-autre-cle-inconnue-de-l-environnement", "jeton_prefixe": "hf_AUTREautre0123456789"}\n')


def _apres(p, contenu, code, **sup):
    f = p["d"] / "creation-brute.json"
    f.write_text(contenu if isinstance(contenu, str) else json.dumps(contenu), encoding="utf-8")
    return f, _lancer(p, "apres-creation", f, code, p["d"], **sup)


def test_apres_creation_sain_creee_reponse_conservee(poste):
    (poste["d"] / "lancement.txt").write_text("machine_proposee 101\n", encoding="utf-8")
    f, r = _apres(poste, REPONSE_SAINE, 0)
    assert r.returncode == 0 and "CRÉÉE : instance 777777" in r.stdout, r.stdout + r.stderr
    (copie,) = _traces(poste, "creation-brute-")
    assert f.exists() and json.loads(copie.read_text(encoding="utf-8")) == REPONSE_SAINE and _empreinte_tenue(copie)
    assert f"RÉPONSE BRUTE DU LOUEUR CONSERVÉE : {copie} (empreinte {hashlib.sha256(copie.read_bytes()).hexdigest()})" in r.stdout
    assert "0 remplacement(s)" in r.stdout and "instance 777777" in (poste["d"] / "lancement.txt").read_text(encoding="utf-8")
    assert _appels(poste) == []                                                # aucun appel au loueur


def test_apres_creation_artefact_reponse_sans_identifiant_lisible_reste_sur_disque(poste):
    """Le cas du 19 novembre (R-3687) : ni `new_contract` ni `success` lisibles. Code 4, et la réponse brute reste, masquée."""
    f, r = _apres(poste, REPONSE_ILLISIBLE, 0)
    assert r.returncode == 4 and "CRÉATION INCERTAINE (code 0, identifiant « aucun »)" in r.stdout and "aucune seconde création avant" in r.stdout, r.stdout + r.stderr
    (copie,) = _traces(poste, "creation-brute-")
    texte = copie.read_text(encoding="utf-8")
    assert f.exists() and f.read_text(encoding="utf-8") == texte and _empreinte_tenue(copie)
    assert "402 Payment Required" in texte and "lacks credit" in texte and "PUT /asks/61361283/" in texte        # la cause reste lisible
    for secret in (JETON_HF, JETON_GH, CLE_LOUEUR, "une-autre-cle-inconnue-de-l-environnement", "hf_AUTREautre0123456789"):
        assert secret not in texte and secret not in r.stdout + r.stderr, secret
    assert "secrets masqués par programme avant conservation : " in r.stdout and "0 remplacement(s)" not in r.stdout
    assert "success=absent ; new_contract=absent" in r.stdout
    assert _appels(poste) == []


def test_apres_creation_artefact_code_non_nul_et_identifiant_present_incertain_conserve(poste):
    f, r = _apres(poste, REPONSE_SAINE, 1)
    assert r.returncode == 4 and "CRÉATION INCERTAINE (code 1, identifiant « 777777 »)" in r.stdout, r.stdout + r.stderr
    assert f.exists() and len(_traces(poste, "creation-brute-")) == 1


def test_apres_creation_offre_refusee_reponse_conservee_et_rang_suivant_en_v2(poste):
    poste["inv"].write_text("[]", encoding="utf-8")
    f, r = _apres(poste, REPONSE_REFUS, 1)
    assert r.returncode == 5 and "OFFRE REFUSÉE À LA CRÉATION" in r.stdout, r.stdout + r.stderr
    assert f"VAST={poste['outil']} bash {RACINE}/scripts/lancer_iib_v2.sh creation auto course 0 {poste['d']} 4102444800" in r.stdout
    (copie,) = _traces(poste, "creation-brute-")
    assert f.exists() and json.loads(copie.read_text(encoding="utf-8")) == REPONSE_REFUS
    assert len(_traces(poste, "instances-apres-")) == 1 and "show instances --raw" in _appels(poste)


def test_apres_creation_deux_reponses_deux_copies_aucune_ecrasee(poste):
    _apres(poste, REPONSE_ILLISIBLE, 0)
    _apres(poste, {"success": False, "error": "x"}, 7, VAST=str(poste["tmp"] / "absent" / "vastai"))     # outil introuvable : incertain, dit
    copies = _traces(poste, "creation-brute-")
    assert len(copies) == 2 and all(_empreinte_tenue(c) for c in copies) and copies[0].read_bytes() != copies[1].read_bytes()


def test_apres_creation_artefacts_reponse_absente_et_masquage_en_echec(poste, tmp_path):
    r = _lancer(poste, "apres-creation", poste["d"] / "absente.json", 0, poste["d"])
    assert r.returncode == 4 and "réponse brute du loueur absente" in r.stdout and "CRÉATION INCERTAINE" in r.stdout, r.stdout + r.stderr
    # masquage impossible (aucun python3 dans le PATH) : rien n'est supprimé, l'original est laissé tel quel et le programme le dit
    b = tmp_path / "bin-sans-python"
    b.mkdir()
    for outil in ("bash", "grep", "date", "cat", "head", "sed", "tail", "mkdir", "cp", "mv", "sha256sum", "cut", "basename", "dirname", "realpath", "timeout"):
        (b / outil).symlink_to(shutil.which(outil))
    f, r = _apres(poste, REPONSE_ILLISIBLE, 0, PATH=str(b))
    assert r.returncode == 4 and "masquage de la réponse brute en échec" in r.stdout and "NON MASQUÉ" in r.stdout, r.stdout + r.stderr
    assert f.read_text(encoding="utf-8") == REPONSE_ILLISIBLE and _traces(poste, "creation-brute-") == []


def test_le_programme_ne_supprime_aucune_sortie_de_la_location():
    """Garde de forme : dans la v2, `rm` ne porte que sur les deux fichiers de tâches des contrôles, jamais sur une sortie de la location."""
    code = [l for l in LANCEUR_V2.read_text(encoding="utf-8").splitlines() if not l.lstrip().startswith("#")]
    assert [l.strip() for l in code if "rm -" in l or " rm " in l] == ['rm -f "$D/reserve.json" "$D/evaluation.json"']
    assert any('rm -f -- "$F"' in l for l in LANCEUR_V1.read_text(encoding="utf-8").splitlines())                # l'artefact : la v1 supprimait


# --- (3) destruction par l'identifiant, option de confirmation, preuve par l'inventaire -------------------------------------
def test_le_faux_outil_exige_la_confirmation(poste):
    """Artefact du 19 novembre (R-3722), rejoué sur le faux outil : sans `-y`, la destruction échoue sur la demande de confirmation."""
    e = {"PATH": "/usr/bin:/bin", "FAUX_VASTAI_JOURNAL": str(poste["appels"]), "FAUX_INSTANCES": str(poste["inv"])}
    r = subprocess.run([str(poste["outil"]), "destroy", "instance", ID], env=e, capture_output=True, text=True, stdin=subprocess.DEVNULL)
    assert r.returncode == 1 and "Are you sure" in r.stdout and "Aborted" in r.stdout
    assert any(i["id"] == int(ID) for i in json.loads(poste["inv"].read_text(encoding="utf-8")))


def test_destruction_sain_option_y_par_identifiant_et_absence_verifiee(poste):
    r = _lancer(poste, "destruction", ID, poste["d"])
    assert r.returncode == 0 and f"DÉTRUITE : instance {ID} absente de l'inventaire" in r.stdout, r.stdout + r.stderr
    assert f"{poste['outil']} destroy instance {ID} -y" in r.stdout
    appels = _appels(poste)
    assert [a for a in appels if a.startswith("destroy")] == [f"destroy instance {ID} -y"]
    assert appels.index("show instances --raw") < appels.index(f"destroy instance {ID} -y") < len(appels) - 1 and appels[-1] == "show instances --raw"
    assert [i["id"] for i in json.loads(poste["inv"].read_text(encoding="utf-8"))] == [58936096]                   # l'autre instance n'est pas touchée
    assert "destruction_verifiee " in (poste["d"] / "lancement.txt").read_text(encoding="utf-8")
    journal = (poste["d"] / "destruction.txt").read_text(encoding="utf-8")
    assert f"destroy instance {ID} -y : code 0" in journal and f"instance {ID} absent" in journal and "outil de location employé" in journal
    for prefixe in ("destruction-sortie-", "instances-avant-destruction-", "instances-apres-destruction-"):
        (trace,) = _traces(poste, prefixe)
        assert _empreinte_tenue(trace)


@pytest.mark.parametrize("mode, code, motif", [("sans-effet", 6, "DESTRUCTION NON OBTENUE : la commande a rendu le code 0"),
                                               ("echec", 6, "DESTRUCTION EN ÉCHEC : la commande a rendu le code 1"),
                                               ("echec-mais-retire", 4, "DESTRUCTION INCERTAINE : la commande de destruction a échoué (code 1)")])
def test_destruction_artefacts_echec_dit_sans_repli(poste, mode, code, motif):
    r = _lancer(poste, "destruction", ID, poste["d"], FAUX_DESTRUCTION=mode)
    assert r.returncode == code and motif in r.stdout and "DÉTRUITE" not in r.stdout, (mode, r.stdout + r.stderr)
    appels = _appels(poste)
    assert [a for a in appels if a.startswith("destroy")] == [f"destroy instance {ID} -y"]                         # une seule commande, aucun second essai
    assert not any(a.startswith(("stop", "create")) for a in appels)
    assert "destruction_verifiee" not in (poste["d"] / "lancement.txt").read_text(encoding="utf-8")
    if mode != "echec-mais-retire":
        assert "encore à l'inventaire après 2 relecture(s)" in r.stdout and appels.count("show instances --raw") == 3
    if mode == "echec":                                                        # la sortie de l'outil est gardée, clé masquée
        (trace,) = _traces(poste, "destruction-sortie-")
        assert "failed with error 500" in trace.read_text(encoding="utf-8") and CLE_LOUEUR not in trace.read_text(encoding="utf-8")


def test_destruction_artefact_inventaire_illisible_avant_aucune_destruction(poste):
    r = _lancer(poste, "destruction", ID, poste["d"], FAUX_INVENTAIRE_ILLISIBLE="1")
    assert r.returncode == 4 and "DESTRUCTION NON TENTÉE : inventaire d'avant illisible" in r.stdout, r.stdout + r.stderr
    assert not any(a.startswith("destroy") for a in _appels(poste))


def test_destruction_artefact_inventaire_illisible_apres_incertain(poste):
    # l'inventaire devient illisible après la destruction : l'absence n'est pas établie, le programme ne dit pas « détruite »
    poste["outil"].write_text(FAUX_OUTIL.replace('[ "${FAUX_INVENTAIRE_ILLISIBLE:-}" = 1 ]', 'grep -q "^destroy" "$FAUX_VASTAI_JOURNAL"', 1), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"])
    assert r.returncode == 4 and "l'absence de l'instance" in r.stdout and "n'est pas établie" in r.stdout and "DÉTRUITE" not in r.stdout, r.stdout + r.stderr


def test_destruction_instance_deja_absente_aucune_commande(poste):
    poste["inv"].write_text(json.dumps({"instances": None}), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"])
    assert r.returncode == 0 and "DÉJÀ ABSENTE DE L'INVENTAIRE : aucune commande de destruction envoyée" in r.stdout, r.stdout + r.stderr
    assert not any(a.startswith("destroy") for a in _appels(poste))


@pytest.mark.parametrize("identifiant, motif", [("58936096", "≠ instance créée"), ("iib-explo-v1", "chiffres seuls"), ("iib*", "chiffres seuls"),
                                                (f"{ID} 58936096", "chiffres seuls")])
def test_destruction_artefacts_jamais_une_autre_instance_ni_un_motif(poste, identifiant, motif):
    """R10 : seul l'identifiant consigné à la création est détruit ; une étiquette, un motif ou une autre instance sont refusés avant tout appel."""
    r = _lancer(poste, "destruction", identifiant, poste["d"])
    assert r.returncode == 2 and motif in r.stdout and "aucune destruction" in r.stdout, r.stdout + r.stderr
    assert _appels(poste) == [] and len(json.loads(poste["inv"].read_text(encoding="utf-8"))) == 2
