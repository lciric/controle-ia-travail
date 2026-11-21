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
AUTRE = 58936096          # machine d'un autre chantier (« intouchable »), présente à l'inventaire du poste
MODULE = RACINE / "src" / "controle_ia" / "iib" / "location_v1.py"
EMPREINTE_MODULE = hashlib.sha256(MODULE.read_bytes()).hexdigest()
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
    [ "${FAUX_INVENTAIRE_ERREUR:-}" = 1 ] && { echo "{\"error\": \"unauthorized\"}"; echo "HTTPError 401 ; Authorization: Bearer $VAST_API_KEY" >&2; exit 1; }
    if [ -n "${FAUX_INVENTAIRE_CLIGNOTE:-}" ] && grep -q "^destroy" "$FAUX_VASTAI_JOURNAL"; then
        k=$(grep -c "^show instances" "$FAUX_VASTAI_JOURNAL"); [ $((k % 2)) = 0 ] && { cat "$FAUX_INVENTAIRE_CLIGNOTE"; exit 0; }
    fi
    cat "$FAUX_INSTANCES"; exit 0 ;;
"destroy instance")
    oui=non; for a in "$@"; do [ "$a" = -y ] && oui=oui; done
    if [ "$oui" = non ]; then
        printf 'Are you sure you want to destroy instance %s? [y/N] ' "$3"
        read -r rep || { echo "Aborted: no confirmation"; exit 1; }
        [ "$rep" = y ] || { echo "Aborted"; exit 1; }
    fi
    case "${FAUX_DESTRUCTION:-}" in vide) echo "[]" > "$FAUX_INSTANCES"; echo "destroying instance $3."; exit 0 ;; sans-effet) echo "destroying instance $3."; exit 0 ;; echec) echo "failed with error 500 ; Authorization: Bearer $VAST_API_KEY"; exit 1 ;; esac
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
    env_v1 = v1s._env
    monkeypatch.setattr(v1s, "_env", lambda m, **sup: env_v1(m, **{"IIB_LOCATION_SHA256": EMPREINTE_MODULE, **sup}))


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
                                     f"etiquette iib-explo-v1\ninstance {ID}\ncreation {int(time.time()) - 60}\nprix_carte 1.0\nprix_stockage 0.03\n"
                                     f"telechargement_forfait 1.0\nplafond_creation 55\nmode jouet\n", encoding="utf-8")
    inv = tmp_path / "inventaire.json"
    inv.write_text(json.dumps([{"id": int(ID), "label": "iib-explo-v1", "actual_status": "exited"},
                               {"id": 58936096, "label": "a1-v4", "actual_status": "running"}]), encoding="utf-8")
    (tmp_path / "journal.txt").write_text("AMORCE 2026-11-19T10:00:00Z : fin, code 0\n", encoding="utf-8")
    return {"tmp": tmp_path, "outil": outil, "d": d, "inv": inv, "appels": tmp_path / "appels.txt"}


def _lancer(p, *args, script=None, **sup):
    e = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": str(p["tmp"]), "LANG": os.environ.get("LANG", "C.UTF-8"), "IIB_DEPOT": str(RACINE),
         "VAST": str(p["outil"]), "FAUX_VASTAI_JOURNAL": str(p["appels"]), "FAUX_INSTANCES": str(p["inv"]), "FAUX_JOURNAL": str(p["tmp"] / "journal.txt"),
         "HF_TOKEN": JETON_HF, "CONTROLE_IA_GITHUB_TOKEN_2": JETON_GH, "VAST_API_KEY": CLE_LOUEUR, "INTERVALLE": "1",
         "IIB_DESTRUCTION_ATTENTE_S": "0", "IIB_DESTRUCTION_RELECTURES": "2", "RAPATRIEMENT_VERIFIE": "oui",
         "IIB_INSTANCES_INTOUCHABLES": str(AUTRE), "IIB_LOCATION_SHA256": EMPREINTE_MODULE}
    e.update(sup)
    e = {k: v for k, v in e.items() if v is not None}
    return subprocess.run(["bash", str(script or LANCEUR_V2), *map(str, args)], env=e, capture_output=True, text=True, timeout=120, stdin=subprocess.DEVNULL)


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
    shutil.copy(RACINE / "src" / "controle_ia" / "iib" / "location_v1.py", monde["src"] / "src" / "controle_ia" / "iib" / "location_v1.py")
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
    e = _env(monde, IIB_LOCATION_SHA256=EMPREINTE_MODULE, **sup)
    e.pop("VAST")                                                              # la commande imprimée se suffit : chemin absolu écrit dedans
    r = subprocess.run(["bash", "-c", cmd], env=e, capture_output=True, text=True, timeout=120, cwd=str(monde["src"]))
    assert r.returncode == 0 and "CRÉÉE : instance 777777" in r.stdout and "RÉPONSE BRUTE DU LOUEUR CONSERVÉE" in r.stdout, r.stdout + r.stderr
    (copie,) = _traces({"d": d}, "creation-brute-")
    texte = copie.read_text(encoding="utf-8")
    assert _empreinte_tenue(copie) and "777777" in texte and JETON_HF not in texte and "jeton-gh-factice" not in texte
    assert (d / "creation-brute-essai1.json").read_text(encoding="utf-8") == texte and "creation-brute-essai1.json" in cmd
    assert "etiquette iib-explo-v1\n" in (d / "lancement.txt").read_text(encoding="utf-8")


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
    assert r.returncode == 4 and "CRÉATION INCERTAINE (code 0, identifiant « aucun » ; " in r.stdout and "aucune seconde création avant" in r.stdout, r.stdout + r.stderr
    (copie,) = _traces(poste, "creation-brute-")
    texte = copie.read_text(encoding="utf-8")
    assert f.exists() and f.read_text(encoding="utf-8") == texte and _empreinte_tenue(copie)
    assert "402 Payment Required" in texte and "lacks credit" in texte and "PUT /asks/61361283/" in texte        # la cause reste lisible
    for secret in (JETON_HF, JETON_GH, CLE_LOUEUR, "une-autre-cle-inconnue-de-l-environnement", "hf_AUTREautre0123456789"):
        assert secret not in texte and secret not in r.stdout + r.stderr, secret
    assert "secrets masqués par programme avant conservation (motifs) : " in r.stdout and "0 remplacement(s)" not in r.stdout
    assert "réponse non analysable comme JSON" in r.stdout and "(motifs)" in r.stdout and "n'est pas une garde des secrets" in r.stdout
    assert "instance " not in (poste["d"] / "lancement.txt").read_text(encoding="utf-8").split("creation ")[-1]      # aucun identifiant consigné
    assert _appels(poste) == []


def test_apres_creation_artefact_code_non_nul_et_identifiant_present_incertain_conserve(poste):
    f, r = _apres(poste, REPONSE_SAINE, 1)
    assert r.returncode == 4 and "CRÉATION INCERTAINE (code 1, identifiant « 777777 » ; " in r.stdout and "aucun identifiant consigné" in r.stdout, r.stdout + r.stderr
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
    # masquage impossible (aucun python3 dans le PATH) : la sortie brute est gardée ENTIÈRE, marquée, droits restreints ; aucun champ imprimé
    b = tmp_path / "bin-sans-python"
    b.mkdir()
    for outil in ("bash", "grep", "date", "cat", "head", "sed", "tail", "mkdir", "cp", "mv", "sha256sum", "cut", "basename", "dirname", "realpath",
                  "timeout", "chmod", "mktemp"):
        (b / outil).symlink_to(shutil.which(outil))
    f, r = _apres(poste, REPONSE_ILLISIBLE, 0, PATH=str(b))
    assert r.returncode == 4 and "masquage de la réponse brute en échec" in r.stdout and "NON MASQUÉE" in r.stdout, r.stdout + r.stderr
    garde = Path(str(f) + ".NON-MASQUE")
    assert garde.read_text(encoding="utf-8") == REPONSE_ILLISIBLE and (garde.stat().st_mode & 0o777) == 0o600 and str(garde) in r.stdout
    assert _traces(poste, "creation-brute-") == [] and "champs de premier niveau" not in r.stdout
    for secret in (JETON_HF, JETON_GH, CLE_LOUEUR):
        assert secret not in r.stdout + r.stderr


def test_le_programme_ne_supprime_aucune_sortie_de_la_location():
    """Garde de forme : dans la v2, `rm` ne porte que sur les deux fichiers de tâches des contrôles, jamais sur une sortie de la location."""
    code = [l for l in LANCEUR_V2.read_text(encoding="utf-8").splitlines() if not l.lstrip().startswith("#")]
    assert [l.strip() for l in code if "rm -" in l or " rm " in l] == ['rm -f "$D/reserve.json" "$D/evaluation.json"']
    # seuls écrasements restants : le dernier relevé du journal de la surveillance (point laissé à trancher, dit au rapport)
    assert [l.strip().split('"')[1] for l in code if "mv -f" in l or "cp -f" in l] == ["$D/journal-dernier.tmp", "$D/journal-dernier.txt"]
    assert not any("2>/dev/null |" in l and "show instances" in l for l in code)                                    # aucun inventaire lu dans un tube
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
    assert r.returncode == 0 and f"DÉTRUITE : instance {ID} absente de deux relectures concordantes de l'inventaire" in r.stdout, r.stdout + r.stderr
    assert f"{poste['outil']} destroy instance {ID} -y" in r.stdout
    appels = _appels(poste)
    assert [a for a in appels if a.startswith("destroy")] == [f"destroy instance {ID} -y"]
    assert appels.index("show instances --raw") < appels.index(f"destroy instance {ID} -y") < len(appels) - 1 and appels[-1] == "show instances --raw"
    assert [i["id"] for i in json.loads(poste["inv"].read_text(encoding="utf-8"))] == [58936096]                   # l'autre instance n'est pas touchée
    assert "destruction_verifiee " in (poste["d"] / "lancement.txt").read_text(encoding="utf-8")
    journal = (poste["d"] / "destruction.txt").read_text(encoding="utf-8")
    assert f"destroy instance {ID} -y : code 0" in journal and f"instance {ID} absent" in journal and "outil de location employé" in journal
    for prefixe, nombre in (("destruction-sortie-", 1), ("instances-avant-destruction-", 1), ("instances-apres-destruction-", 2)):
        traces = _traces(poste, prefixe)
        assert len(traces) == nombre and all(_empreinte_tenue(x) for x in traces), prefixe
    assert "absente de deux relectures concordantes" in r.stdout and f"instances intouchables : {AUTRE}" in r.stdout
    assert f"instances intouchables : {AUTRE}" in journal and "RAPATRIEMENT_VERIFIE=oui" in journal and "liste fermée) : exited stopped" in journal


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


def test_destruction_artefact_instance_absente_avant_n_est_pas_une_preuve(poste):
    poste["inv"].write_text(json.dumps({"instances": None}), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"])
    assert r.returncode == 7 and "ABSENCE NON CONFIRMÉE" in r.stdout and "aucune commande de destruction envoyée" in r.stdout, r.stdout + r.stderr
    assert not any(a.startswith("destroy") for a in _appels(poste)) and "destruction_verifiee" not in (poste["d"] / "lancement.txt").read_text(encoding="utf-8")


@pytest.mark.parametrize("identifiant, motif", [("58936096", "≠ instance créée"), ("iib-explo-v1", "chiffres seuls"), ("iib*", "chiffres seuls"),
                                                (f"{ID} 58936096", "chiffres seuls")])
def test_destruction_artefacts_jamais_une_autre_instance_ni_un_motif(poste, identifiant, motif):
    """R10 : seul l'identifiant consigné à la création est détruit ; une étiquette, un motif ou une autre instance sont refusés avant tout appel."""
    r = _lancer(poste, "destruction", identifiant, poste["d"])
    assert r.returncode == 2 and motif in r.stdout and "aucune destruction" in r.stdout, r.stdout + r.stderr
    assert _appels(poste) == [] and len(json.loads(poste["inv"].read_text(encoding="utf-8"))) == 2


# === Corrections de la contre-lecture du 19 novembre (un bloquant, trois majeurs, mineurs) ===================================
# Les sept attaques du contre-lecteur (`test_attaques_lanceur_v2_cl1.py`) sont reprises ici ; chaque essai affirme le comportement sûr.
def _lancement_sans_instance(p):
    (p["d"] / "lancement.txt").write_text("machine_proposee 101\ncarte course\nanterieure 0\necheance 4102444800\nmode jouet\netiquette iib-explo-v1\n", encoding="utf-8")


def _lignes_instance(p) -> list:
    return [l for l in (p["d"] / "lancement.txt").read_text(encoding="utf-8").splitlines() if l.startswith("instance ")]


def _restantes(p) -> list:
    return [i["id"] for i in json.loads(p["inv"].read_text(encoding="utf-8"))]


def _tous_les_fichiers(p) -> dict:
    return {str(f.relative_to(p["d"])): f.read_bytes() for f in sorted(p["d"].rglob("*")) if f.is_file()}


def test_attaque_1_reponse_piegee_ne_fait_ni_consigner_ni_detruire_une_autre_machine(poste):
    """BLOQUANT. Un message cite « new_contract: <autre> » avant le vrai champ : plusieurs valeurs candidates, donc refus (code 4),
    aucun identifiant consigné ; et la destruction de l'autre machine est refusée avant tout appel."""
    _lancement_sans_instance(poste)
    _, r = _apres(poste, '{"msg": "previous new_contract: %d released", "success": true, "new_contract": 777777}' % AUTRE, 0)
    assert r.returncode == 4 and "plusieurs valeurs candidates" in r.stdout and "CRÉÉE" not in r.stdout, r.stdout + r.stderr
    assert _lignes_instance(poste) == []
    r = _lancer(poste, "destruction", AUTRE, poste["d"])
    assert r.returncode == 2 and "aucune destruction" in r.stdout, r.stdout + r.stderr
    assert AUTRE in _restantes(poste) and not any(a.startswith("destroy") for a in _appels(poste))


def test_attaque_1_bis_autre_machine_consignee_par_erreur_refusee_par_l_etiquette_et_par_la_liste(poste):
    """Seconde ligne de défense : même si l'identifiant d'une autre machine était consigné dans `lancement.txt`, l'inventaire la montre
    avec une étiquette qui n'est pas celle du saboteur à budget : refus sans appel ; refus aussi par la liste des intouchables."""
    with (poste["d"] / "lancement.txt").open("a", encoding="utf-8") as f:
        f.write(f"instance {AUTRE}\n")
    poste["inv"].write_text(poste["inv"].read_text(encoding="utf-8").replace('"running"', '"exited"'), encoding="utf-8")       # l'état ne la protège pas : l'étiquette, si
    r = _lancer(poste, "destruction", AUTRE, poste["d"], IIB_INSTANCES_INTOUCHABLES="61000001")
    assert r.returncode == 2 and "porte l'étiquette « a1-v4 », qui n'est pas exactement « iib-explo-v1 »" in r.stdout, r.stdout + r.stderr
    r = _lancer(poste, "destruction", AUTRE, poste["d"], IIB_INSTANCES_INTOUCHABLES=f"61000001,{AUTRE}")
    assert r.returncode == 2 and "dans la liste des instances intouchables" in r.stdout, r.stdout + r.stderr
    assert sorted(_restantes(poste)) == sorted([int(ID), AUTRE]) and not any(a.startswith("destroy") for a in _appels(poste))


def test_attaque_2_inventaire_vide_par_erreur_ne_vaut_pas_preuve(poste):
    """MAJEUR. Inventaire rendu vide alors que l'instance existe : ni code 0, ni ligne `destruction_verifiee`, ni commande."""
    for vide in ("[]", '{"instances": null}', '{"instances": []}'):
        poste["inv"].write_text(vide, encoding="utf-8")
        r = _lancer(poste, "destruction", ID, poste["d"])
        assert r.returncode == 7 and "ABSENCE NON CONFIRMÉE" in r.stdout and "ce n'est pas une preuve" in r.stdout, (vide, r.stdout + r.stderr)
    assert "destruction_verifiee" not in (poste["d"] / "lancement.txt").read_text(encoding="utf-8")
    assert not any(a.startswith("destroy") for a in _appels(poste))


def test_attaque_2_bis_inventaire_vide_apres_la_destruction_alors_que_d_autres_machines_existaient(poste):
    """Après la commande, l'inventaire revient VIDE alors que le compte portait une autre machine : inventaire amputé, pas une preuve."""
    r = _lancer(poste, "destruction", ID, poste["d"], FAUX_DESTRUCTION="vide")
    assert r.returncode == 4 and "un inventaire vide ou amputé n'est pas une preuve" in r.stdout and "DÉTRUITE" not in r.stdout, r.stdout + r.stderr
    assert "destruction_verifiee" not in (poste["d"] / "lancement.txt").read_text(encoding="utf-8")


def test_destruction_sain_compte_a_une_seule_instance_inventaire_vide_relu_deux_fois(poste):
    """Cas sain du même contrôle : le compte ne portait que l'instance du saboteur ; vide deux fois de suite, appel sans erreur : détruite."""
    poste["inv"].write_text(json.dumps([{"id": int(ID), "label": "iib-explo-v1", "actual_status": "exited"}]), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"])
    assert r.returncode == 0 and "DÉTRUITE" in r.stdout and _appels(poste).count("show instances --raw") == 3, r.stdout + r.stderr


def test_destruction_artefact_une_seule_relecture_absente_ne_suffit_pas(poste):
    """L'inventaire d'après clignote (absente, présente, absente, présente) : jamais deux relectures concordantes, jamais « DÉTRUITE »."""
    avec = poste["tmp"] / "inventaire-avec.json"
    avec.write_text(poste["inv"].read_text(encoding="utf-8"), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"], FAUX_INVENTAIRE_CLIGNOTE=str(avec), IIB_DESTRUCTION_RELECTURES="4")
    assert r.returncode == 4 and "DÉTRUITE" not in r.stdout and "sans deux relectures concordantes" in r.stdout, r.stdout + r.stderr
    assert _appels(poste).count("show instances --raw") == 5 and "destruction_verifiee" not in (poste["d"] / "lancement.txt").read_text(encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"], IIB_DESTRUCTION_RELECTURES="1")
    assert r.returncode == 2 and "deux relectures concordantes exigées" in r.stdout, r.stdout + r.stderr


def test_attaque_3_outil_en_erreur_apres_avoir_detruit_et_inventaire_illisible_ensuite(poste):
    poste["outil"].write_text(FAUX_OUTIL.replace('[ "${FAUX_INVENTAIRE_ILLISIBLE:-}" = 1 ]', 'grep -q "^destroy" "$FAUX_VASTAI_JOURNAL"', 1), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"], FAUX_DESTRUCTION="echec-mais-retire")
    assert r.returncode == 4 and "DÉTRUITE" not in r.stdout and "n'est pas établie" in r.stdout, r.stdout + r.stderr
    assert [a for a in _appels(poste) if a.startswith("destroy")] == [f"destroy instance {ID} -y"]
    # l'inventaire illisible est gardé entier, marqué, droits restreints, hors des traces à verser
    gardes = sorted(poste["d"].glob("instances-apres-destruction-*.NON-MASQUE"))
    assert len(gardes) == 2 and all((g.stat().st_mode & 0o777) == 0o600 and "erreur 502" in g.read_text(encoding="utf-8") for g in gardes)
    assert _traces(poste, "instances-apres-destruction-") == []


@pytest.mark.parametrize("identifiant", [f"0{ID}", f"{ID} ", f"{ID}\n", "", "-1", "0", f"+{ID}", f"{ID}.0"])
def test_attaque_4_identifiants_pieges(poste, identifiant):
    r = _lancer(poste, "destruction", identifiant, poste["d"])
    assert r.returncode == 2 and "aucune destruction" in r.stdout and not any(a.startswith("destroy") for a in _appels(poste)), r.stdout + r.stderr
    assert _appels(poste) == []


def test_attaque_4_bis_deux_lignes_instance_seul_le_dernier_identifiant_consigne(poste):
    with (poste["d"] / "lancement.txt").open("a", encoding="utf-8") as f:
        f.write("instance 61999999\n")
    r = _lancer(poste, "destruction", ID, poste["d"])
    assert r.returncode == 2 and "≠ instance créée" in r.stdout and _appels(poste) == [], r.stdout + r.stderr


def test_attaque_5_secret_d_une_autre_machine_jamais_verse_ni_garde(poste):
    """MAJEUR. L'inventaire du compte porte les secrets des autres machines : ni les traces, ni aucun fichier du dossier de session ne
    les gardent ; les traces ne portent que les champs filtrés de la seule instance du saboteur."""
    secret, jeton = "sk-autreChantier-0123456789abcdef", "jt0123456789abcdef0123"
    inv = [{"id": int(ID), "label": "iib-explo-v1", "actual_status": "exited", "dph_total": 1.041, "machine_id": 126194, "storage_cost": 0.15,
            "jupyter_token": "jt-du-saboteur-0123456789", "extra_env": [["HF_TOKEN", JETON_HF]], "ssh_host": "ssh9.exemple"},
           {"id": AUTRE, "label": "a1-v4", "actual_status": "running", "jupyter_token": jeton, "machine_id": 555,
            "extra_env": [["OPENAI_API_KEY", secret], ["-e WANDB", "x"]]}]
    poste["inv"].write_text(json.dumps(inv), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"])
    assert r.returncode == 0, r.stdout + r.stderr
    for nom, contenu in _tous_les_fichiers(poste).items():
        for interdit in (secret, jeton, "jt-du-saboteur-0123456789", JETON_HF, "OPENAI_API_KEY", "ssh9.exemple"):
            assert interdit.encode() not in contenu, (nom, interdit)
    (avant,) = _traces(poste, "instances-avant-destruction-")
    trace = json.loads(avant.read_text(encoding="utf-8"))
    assert trace["instances_du_saboteur_champs_filtres"] == [{"id": int(ID), "label": "iib-explo-v1", "actual_status": "exited", "dph_total": 1.041,
                                                                "storage_cost": 0.15, "machine_id": 126194}]
    assert trace["nombre_d_instances_du_compte"] == 2 and str(AUTRE) not in avant.read_text(encoding="utf-8") and "555" not in avant.read_text(encoding="utf-8")
    # le fichier de travail du dossier ne garde, pour chaque instance, qu'identifiant, étiquette et état
    (travail,) = sorted(poste["d"].glob("instances-avant-destruction-*.json"))
    assert json.loads(travail.read_text(encoding="utf-8")) == [{"id": int(ID), "label": "iib-explo-v1", "actual_status": "exited"},
                                                               {"id": AUTRE, "label": "a1-v4", "actual_status": "running"}]


def test_attaque_6_secret_en_paire_dans_la_reponse_de_creation(poste):
    """MAJEUR. Environnement renvoyé en paires (forme `extra_env`), secret inconnu de l'environnement local, jeton de bloc-notes."""
    secret = "sk-inconnu-0123456789abcdef"
    f, r = _apres(poste, json.dumps({"success": False, "error": "x", "extra_env": [["MY_API_KEY", secret], ["AUTRE", "gardé"]],
                                     "jupyter_token": "jt0123456789", "args": {"env": {"DB_PASSWORD": "motdepasse-1234"}}}), 1)
    (copie,) = _traces(poste, "creation-brute-")
    texte = copie.read_text(encoding="utf-8")
    for interdit in (secret, "jt0123456789", "motdepasse-1234"):
        assert interdit not in texte and interdit not in f.read_text(encoding="utf-8") and interdit not in r.stdout
    assert "(structure) : " in r.stdout and "0 remplacement(s)" not in r.stdout and json.loads(texte)["extra_env"] == [["MY_API_KEY", "***"], ["AUTRE", "gardé"]]


def test_attaque_7_destruction_rejouee_n_ecrase_aucun_fichier(poste):
    """R12 : une seconde destruction (code 6 la première fois) n'écrase ni ne retire aucun fichier écrit par la première, hors les deux
    journaux, qui ne font que grandir."""
    r = _lancer(poste, "destruction", ID, poste["d"], FAUX_DESTRUCTION="echec")
    assert r.returncode == 6
    premiers = _tous_les_fichiers(poste)
    r = _lancer(poste, "destruction", ID, poste["d"])
    assert r.returncode == 0, r.stdout + r.stderr
    seconds = _tous_les_fichiers(poste)
    for nom, contenu in premiers.items():
        assert nom in seconds, nom
        if nom in ("destruction.txt", "lancement.txt"):
            assert seconds[nom].startswith(contenu), nom
        else:
            assert seconds[nom] == contenu, nom
    assert len(_traces(poste, "destruction-sortie-")) == 2 and len(seconds) > len(premiers)


# --- gardes de la destruction, cas sain (essai sain plus haut) et artefacts ---------------------------------------------------
@pytest.mark.parametrize("cas, sup, motif", [
    ("rapatriement_non_atteste", {"RAPATRIEMENT_VERIFIE": None}, "RAPATRIEMENT_VERIFIE=oui exigé"),
    ("rapatriement_autre_mot", {"RAPATRIEMENT_VERIFIE": "non"}, "RAPATRIEMENT_VERIFIE=oui exigé"),
    ("intouchable", {"IIB_INSTANCES_INTOUCHABLES": f"{AUTRE},{ID}"}, "dans la liste des instances intouchables"),
    ("liste_illisible", {"IIB_INSTANCES_INTOUCHABLES": "a1-v4;iib"}, "IIB_INSTANCES_INTOUCHABLES illisible"),
    ("liste_absente", {"IIB_INSTANCES_INTOUCHABLES": None}, "liste des instances intouchables vide ou absente"),
    ("liste_vide", {"IIB_INSTANCES_INTOUCHABLES": ""}, "liste des instances intouchables vide ou absente"),
    ("attestation_autre_mot", {"IIB_INSTANCES_INTOUCHABLES": None, "IIB_AUCUNE_INTOUCHABLE": "non"}, "« oui » ou rien"),
    ("attestation_contredite", {"IIB_AUCUNE_INTOUCHABLE": "oui"}, "contredit une liste"),
    ("etats_elargis_par_variable", {"IIB_DESTRUCTION_ETATS_ARRET": "running exited stopped"}, "IIB_DESTRUCTION_ETATS_ARRET n'existe plus")])
def test_destruction_gardes_artefacts_refus_avant_tout_appel(poste, cas, sup, motif):
    r = _lancer(poste, "destruction", ID, poste["d"], **sup)
    assert r.returncode == 2 and motif in r.stdout and "aucune destruction" in r.stdout, (cas, r.stdout + r.stderr)
    assert _appels(poste) == [] and len(_restantes(poste)) == 2


def test_destruction_liste_des_intouchables_saine_dite_au_journal(poste):
    r = _lancer(poste, "destruction", ID, poste["d"], IIB_INSTANCES_INTOUCHABLES=f"{AUTRE},61000001")
    assert r.returncode == 0 and f"instances intouchables : {AUTRE},61000001" in r.stdout, r.stdout + r.stderr
    assert f"instances intouchables : {AUTRE},61000001" in (poste["d"] / "destruction.txt").read_text(encoding="utf-8") and _restantes(poste) == [AUTRE]


@pytest.mark.parametrize("cas, motif", [("en_marche", "est à l'état « running »"), ("etat_absent", "est à l'état « aucun »"),
                                        ("etiquette_autre", "porte l'étiquette « t06-7b »"), ("sans_etiquette", "porte l'étiquette « aucun »"),
                                        ("etiquette_iib_d_une_autre_course", "porte l'étiquette « iib-autre-v9 »"),
                                        ("etiquette_au_meme_debut", "porte l'étiquette « iib-explo-v1-autre-chantier », qui n'est pas exactement « iib-explo-v1 »"),
                                        ("etiquette_plus_courte", "porte l'étiquette « iib-explo », qui n'est pas exactement"),
                                        ("etat_d_arret_d_un_autre_nom", "est à l'état « offline », hors de la liste fermée")])
def test_destruction_gardes_d_inventaire_artefacts_refus_sans_appel_de_destruction(poste, cas, motif):
    entree = {"id": int(ID), "label": "iib-explo-v1", "actual_status": "exited"}
    entree.update({"en_marche": {"actual_status": "running"}, "etat_absent": {"actual_status": None}, "etiquette_autre": {"label": "t06-7b"},
                   "sans_etiquette": {"label": None}, "etiquette_iib_d_une_autre_course": {"label": "iib-autre-v9"},
                   "etiquette_au_meme_debut": {"label": "iib-explo-v1-autre-chantier"}, "etiquette_plus_courte": {"label": "iib-explo"},
                   "etat_d_arret_d_un_autre_nom": {"actual_status": "offline"}}[cas])
    poste["inv"].write_text(json.dumps([entree, {"id": AUTRE, "label": "a1-v4", "actual_status": "running"}]), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"])
    assert r.returncode == 2 and motif in r.stdout and "aucune destruction" in r.stdout, (cas, r.stdout + r.stderr)
    assert not any(a.startswith("destroy") for a in _appels(poste)) and len(_restantes(poste)) == 2


def test_destruction_artefact_etiquette_de_la_creation_inconnue(poste):
    f = poste["d"] / "lancement.txt"
    f.write_text(f.read_text(encoding="utf-8").replace("etiquette iib-explo-v1\n", ""), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"])
    assert r.returncode == 2 and "étiquette posée à la création illisible" in r.stdout and _appels(poste) == [], r.stdout + r.stderr
    (poste["d"] / "config.json").write_text(json.dumps({"offre": {"etiquette": "t06-v2"}}), encoding="utf-8")       # étiquette d'un autre chantier
    r = _lancer(poste, "destruction", ID, poste["d"])
    assert r.returncode == 2 and "hors du préfixe « iib »" in r.stdout and _appels(poste) == [], r.stdout + r.stderr
    (poste["d"] / "config.json").write_text(json.dumps({"offre": {"etiquette": "iib-explo-v1"}}), encoding="utf-8")  # sain : repli écrit sur la configuration
    r = _lancer(poste, "destruction", ID, poste["d"])
    assert r.returncode == 0, r.stdout + r.stderr


def test_destruction_artefact_appel_d_inventaire_en_erreur_sortie_d_erreur_gardee(poste):
    """L'appel d'inventaire échoue (code 1) : pas une preuve, aucune destruction ; sa sortie d'erreur est gardée, clé du loueur masquée."""
    r = _lancer(poste, "destruction", ID, poste["d"], FAUX_INVENTAIRE_ERREUR="1")
    assert r.returncode == 4 and "DESTRUCTION NON TENTÉE" in r.stdout and "appel de l'inventaire en échec (code 1)" in r.stdout, r.stdout + r.stderr
    (err,) = sorted(poste["d"].glob("instances-avant-destruction-*.err"))
    assert "HTTPError 401" in err.read_text(encoding="utf-8") and CLE_LOUEUR not in err.read_text(encoding="utf-8")
    assert not any(a.startswith("destroy") for a in _appels(poste)) and _traces(poste, "instances-") == []


def test_l_essai_sain_mord_sur_l_option_de_confirmation(poste, tmp_path):
    """Dans la suite, et non plus à la main : le même lanceur privé de `-y` échoue sur le même faux outil (code 6, instance gardée)."""
    mutant = tmp_path / "arbre-mutant" / "scripts" / "lancer_iib_v2.sh"
    mutant.parent.mkdir(parents=True)
    (tmp_path / "arbre-mutant" / "src" / "controle_ia" / "iib").mkdir(parents=True)
    shutil.copy(RACINE / "src" / "controle_ia" / "iib" / "location_v1.py", tmp_path / "arbre-mutant" / "src" / "controle_ia" / "iib" / "location_v1.py")
    texte = LANCEUR_V2.read_text(encoding="utf-8")
    assert texte.count('destroy instance "$ID" -y >') == 1
    mutant.write_text(texte.replace('destroy instance "$ID" -y >', 'destroy instance "$ID" >'), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"], script=mutant)
    assert r.returncode == 6 and "DESTRUCTION EN ÉCHEC" in r.stdout and int(ID) in _restantes(poste), r.stdout + r.stderr
    assert [a for a in _appels(poste) if a.startswith("destroy")] == [f"destroy instance {ID}"]


# --- lecture par programme (`src/controle_ia/iib/location_v1.py`), sans lanceur -----------------------------------------------
def _location():
    import importlib.util
    spec = importlib.util.spec_from_file_location("location_v1", RACINE / "src" / "controle_ia" / "iib" / "location_v1.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("reponse, verdict, motif", [
    ('{"success": true, "new_contract": 777777}', "cree", "seule valeur candidate"),
    ('{"success": false, "error": "no_such_ask", "msg": "offre retirée"}', "refusee", "aucun identifiant"),
    ("{'success': True, 'new_contract': 777777}", "incertain", "non analysable comme JSON"),                          # forme Python : refus
    ('Started. {"success": true, "new_contract": 777777}', "incertain", "non analysable comme JSON"),
    ('[{"success": true, "new_contract": 777777}]', "incertain", "n'est pas un objet"),
    ('{"success": true}', "incertain", "absente du premier niveau"),
    ('{"success": true, "new_contract": "777777"}', "incertain", "pas un entier positif"),
    ('{"success": true, "new_contract": true}', "incertain", "pas un entier positif"),
    ('{"success": true, "new_contract": 0}', "incertain", "pas un entier positif"),
    ('{"success": true, "new_contract": -5}', "incertain", "pas un entier positif"),
    ('{"success": true, "new_contract": 7.0}', "incertain", "pas un entier positif"),
    ('{"success": true, "new_contract": 777777, "new_contract": 58936096}', "incertain", "clé en double"),
    ('{"success": true, "new_contract": 777777, "detail": {"new_contract": 58936096}}', "incertain", "plusieurs valeurs candidates"),
    ('{"success": true, "new_contract": 777777, "detail": {"new_contract": 777777}}', "incertain", "plusieurs valeurs candidates"),
    ('{"msg": "previous new_contract: 58936096 released", "success": true, "new_contract": 777777}', "incertain", "plusieurs valeurs candidates"),
    ('{"success": false, "msg": "new_contract=58936096"}', "incertain", "citée ailleurs"),
    ('{"success": false, "new_contract": 777777}', "incertain", "n'est pas vrai"),
    ('{"success": "true", "new_contract": 777777}', "incertain", "n'est pas vrai"),
    ("", "incertain", "non analysable comme JSON")])
def test_verdict_de_la_reponse_de_creation_cle_de_premier_niveau_seulement(reponse, verdict, motif):
    v, ident, raison, _ = _location().verdict_creation(reponse)
    assert v == verdict and motif in raison and (ident == 777777) == (verdict == "cree"), (v, ident, raison)


@pytest.mark.parametrize("forme", [
    '{"extra_env": [["MY_API_KEY", "SECRET"]]}',                                             # paires, JSON
    '{"extra_env": {"WANDB_API_KEY": "SECRET"}}',                                            # clé nommée, JSON
    '{"jupyter_token": "SECRET", "ok": 1}',
    '{"a": {"b": [{"Db_PassWord": "SECRET"}]}}',
    '{"onstart": "export HF_TOKEN=SECRET && python run.py"}',                                # affectation dans une chaîne
    '{"corps": "{\\"api_key\\": \\"SECRET\\"}"}',                                            # JSON échappé dans une chaîne
    '{"corps": "[[\\"MY_API_KEY\\", \\"SECRET\\"]]"}',
    '{"en_tetes": {"Authorization": "Bearer SECRET"}}',
    '{"secret_numerique": {"api_key": 1234567890123}}',
    "Traceback\n env=[['MY_API_KEY', 'SECRET'], ['A', 'b']]\n",                              # paires, forme Python, hors JSON
    'erreur : extra_env=[["OPENAI_API_KEY", "SECRET"]] fin',                                 # paires, hors JSON
    'requête : {\\"jupyter_token\\": \\"SECRET\\"} fin',                                     # échappé, hors JSON
    "headers={'Authorization': 'Bearer SECRET'}",
    "env: -e GH_TOKEN=SECRET -e MODE=reel",
    '{"api_key": "SECRET", "api_key": "SECRET"}'])                                           # clé en double : motifs
def test_masquage_formes_que_la_contre_lecture_a_trouvees_ouvertes(forme):
    secret = "s3cr3t-Valeur_0123456789"
    texte = forme.replace("SECRET", secret).replace("1234567890123", "9876543210987")
    masque, n, mode = _location().masquer(texte)
    assert secret not in masque and "9876543210987" not in masque and n >= 1, (mode, masque)


def test_masquage_valeur_de_l_environnement_sous_forme_echappee(monkeypatch):
    valeur = "cle/avec+barre=é-0123456789"
    monkeypatch.setenv("VAST_API_KEY", valeur)
    loc = _location()
    for texte in ("vu : " + valeur, "vu : " + json.dumps(valeur)[1:-1], "vu : " + json.dumps(valeur)[1:-1].replace("/", "\\/"),
                  "vu : " + json.dumps(valeur, ensure_ascii=False)[1:-1], json.dumps({"note": "vu " + valeur}), json.dumps({"x": json.dumps({"y": valeur})})):
        masque, n, _ = loc.masquer(texte)
        assert "0123456789" not in masque and n >= 1, texte


def test_masquage_sain_rien_d_autre_n_est_retire():
    reponse = {"success": False, "error": "insufficient_credit", "msg": "Your account lacks credit; see the billing page.", "ask_id": 61361283}
    masque, n, mode = _location().masquer(json.dumps(reponse))
    assert json.loads(masque) == reponse and n == 0 and mode == "structure"
    texte = "Traceback (most recent call last):\n  HTTPError: 402 Payment Required for url: /api/v0/asks/61361283/\n"
    assert _location().masquer(texte) == (texte, 0, "motifs")


@pytest.mark.parametrize("inventaire", ["", "<html>502</html>", '{"error": "unauthorized"}', "null", '{"instances": "x"}', '[{"label": "iib"}]',
                                        '[{"id": "61414494"}]', '[{"id": 1}, {"id": 1}]', '[{"id": 1}], [{"id": 2}]'])
def test_inventaire_illisible_n_est_jamais_lu_comme_vide(inventaire, tmp_path):
    brut = tmp_path / "brut.json"
    brut.write_text(inventaire, encoding="utf-8")
    assert _location().main(["inventaire", str(brut), str(tmp_path / "trace.json"), "iib", ID]) == 1
    assert brut.read_text(encoding="utf-8") == inventaire and not (tmp_path / "trace.json").exists()                  # sortie brute intacte, aucune trace


def test_inventaire_trace_jamais_ecrasee(tmp_path):
    brut = tmp_path / "brut.json"
    brut.write_text("[]", encoding="utf-8")
    (tmp_path / "trace.json").write_text("déjà là", encoding="utf-8")
    assert _location().main(["inventaire", str(brut), str(tmp_path / "trace.json"), "iib"]) == 1
    assert (tmp_path / "trace.json").read_text(encoding="utf-8") == "déjà là" and brut.read_text(encoding="utf-8") == "[]"


# === Erratum 1 (vérification des corrections : quatre mineurs neufs, et deux recommandations) =================================
def test_erratum_n1_aucune_variable_ne_fait_detruire_une_instance_qui_tourne(poste):
    """N1. Liste fermée des états d'arrêt : ni la variable retirée, ni aucune autre, ne fait détruire une instance « running »."""
    poste["inv"].write_text(json.dumps([{"id": int(ID), "label": "iib-explo-v1", "actual_status": "running"},
                                        {"id": AUTRE, "label": "a1-v4", "actual_status": "running"}]), encoding="utf-8")
    for sup in ({}, {"IIB_DESTRUCTION_ETATS_ARRET": "running"}, {"ETATS_ARRET": "running"}):
        r = _lancer(poste, "destruction", ID, poste["d"], **sup)
        assert r.returncode == 2 and "aucune destruction" in r.stdout and int(ID) in _restantes(poste), (sup, r.stdout + r.stderr)
    assert not any(a.startswith("destroy") for a in _appels(poste))
    assert "une instance qui tourne n'est jamais détruite par cette sous-commande" in _lancer(poste, "destruction", ID, poste["d"]).stdout


def test_erratum_n2_etiquette_egale_et_autre_machine_au_meme_debut(poste):
    """N2 (attaque du contre-lecteur) : autre machine à l'étiquette de même début, ligne `instance` fausse, hors de la liste : refus."""
    poste["inv"].write_text(json.dumps([{"id": int(ID), "label": "iib-explo-v1", "actual_status": "exited"},
                                        {"id": AUTRE, "label": "iib-explo-v1-autre-chantier", "actual_status": "exited"}]), encoding="utf-8")
    with (poste["d"] / "lancement.txt").open("a", encoding="utf-8") as f:
        f.write(f"instance {AUTRE}\n")
    for sup in ({"IIB_INSTANCES_INTOUCHABLES": "61000001"}, {"IIB_INSTANCES_INTOUCHABLES": None, "IIB_AUCUNE_INTOUCHABLE": "oui"}):
        r = _lancer(poste, "destruction", AUTRE, poste["d"], **sup)
        assert r.returncode == 2 and "n'est pas exactement « iib-explo-v1 »" in r.stdout and AUTRE in _restantes(poste), r.stdout + r.stderr
    assert not any(a.startswith("destroy") for a in _appels(poste))


def test_erratum_intouchables_absentes_avec_attestation_dite_au_journal(poste):
    """Cas sain de la garde : aucune liste, mais attestation explicite ; elle est dite sur la sortie et au journal."""
    r = _lancer(poste, "destruction", ID, poste["d"], IIB_INSTANCES_INTOUCHABLES=None, IIB_AUCUNE_INTOUCHABLE="oui")
    assert r.returncode == 0 and "instances intouchables : aucune, attesté par IIB_AUCUNE_INTOUCHABLE=oui" in r.stdout, r.stdout + r.stderr
    assert "aucune, attesté par IIB_AUCUNE_INTOUCHABLE=oui" in (poste["d"] / "destruction.txt").read_text(encoding="utf-8")


def test_erratum_rapatriement_atteste_ecrit_dans_le_lancement(poste):
    """L'attestation est écrite en une ligne (quand, valeur, instance, qui) ; jamais quand une garde a refusé."""
    r = _lancer(poste, "destruction", ID, poste["d"], RAPATRIEMENT_VERIFIE=None)
    assert r.returncode == 2 and "rapatriement_atteste" not in (poste["d"] / "lancement.txt").read_text(encoding="utf-8")
    poste["inv"].write_text(poste["inv"].read_text(encoding="utf-8").replace('"exited"', '"running"'), encoding="utf-8")
    assert _lancer(poste, "destruction", ID, poste["d"]).returncode == 2 and "rapatriement_atteste" not in (poste["d"] / "lancement.txt").read_text(encoding="utf-8")
    poste["inv"].write_text(poste["inv"].read_text(encoding="utf-8").replace(f'"id": {ID}, "label": "iib-explo-v1", "actual_status": "running"',
                                                                             f'"id": {ID}, "label": "iib-explo-v1", "actual_status": "exited"'), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"])
    assert r.returncode == 0, r.stdout + r.stderr
    import re
    (ligne,) = [l for l in (poste["d"] / "lancement.txt").read_text(encoding="utf-8").splitlines() if l.startswith("rapatriement_atteste ")]
    assert re.fullmatch(r"rapatriement_atteste \d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ RAPATRIEMENT_VERIFIE=oui instance=%s par=[A-Za-z0-9_.?-]+@[A-Za-z0-9_.?-]+" % ID, ligne), ligne


@pytest.mark.parametrize("cas", ["empreinte_absente", "empreinte_autre", "empreinte_illisible", "module_change", "module_absent", "contredit_la_configuration"])
def test_erratum_n4_module_de_lecture_non_verifie_refus(poste, tmp_path, cas):
    """N4. Le module de lecture est vérifié par son empreinte avant tout emploi : sinon aucune création, aucune destruction, et la
    réponse de création est gardée entière, non lue."""
    arbre = tmp_path / "arbre-copie"
    (arbre / "scripts").mkdir(parents=True)
    (arbre / "src" / "controle_ia" / "iib").mkdir(parents=True)
    script = arbre / "scripts" / LANCEUR_V2.name
    shutil.copy(LANCEUR_V2, script)
    if cas != "module_absent":
        shutil.copy(MODULE, arbre / "src" / "controle_ia" / "iib" / "location_v1.py")
    sup = {}
    if cas == "empreinte_absente":
        sup["IIB_LOCATION_SHA256"] = None
    elif cas == "empreinte_autre":
        sup["IIB_LOCATION_SHA256"] = "0" * 64
    elif cas == "empreinte_illisible":
        sup["IIB_LOCATION_SHA256"] = "abc"
    elif cas == "module_change":                                               # module menteur du contre-lecteur (attaque N5)
        (arbre / "src" / "controle_ia" / "iib" / "location_v1.py").write_text(
            'import sys\nif sys.argv[1] == "inventaire":\n    open(sys.argv[3], "w").write("{}")\n'
            '    print("n=2 etat=present etiquette=iib-explo-v1 statut=exited autres_manquants=0")\n'
            'elif sys.argv[1] == "masquer-en-place":\n    print("0 structure")\n', encoding="utf-8")
    elif cas == "contredit_la_configuration":
        (poste["d"] / "config.json").write_text(json.dumps({"marqueurs": {"EMPREINTES_CODE_IIB": "… ; src/controle_ia/iib/location_v1.py " + "1" * 64 + " ; …"}}), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"], script=script, **sup)
    assert r.returncode == 4 and "DESTRUCTION NON TENTÉE" in r.stdout and "aucune commande de destruction envoyée" in r.stdout, (cas, r.stdout + r.stderr)
    assert not any(a.startswith(("destroy", "show")) for a in _appels(poste))
    f = poste["d"] / "creation-brute-x.json"
    reponse = '{"success": true, "new_contract": 777777, "api_key": "sk-secret-0123456789abcdef"}'
    f.write_text(reponse, encoding="utf-8")
    _lancement_sans_instance(poste)
    r = _lancer(poste, "apres-creation", f, 0, poste["d"], script=script, **sup)
    assert r.returncode == 4 and _lignes_instance(poste) == [] and "aucune lecture par programme" in r.stdout, (cas, r.stdout + r.stderr)
    assert Path(str(f) + ".NON-MASQUE").read_text(encoding="utf-8") == reponse and "sk-secret" not in r.stdout


def test_erratum_n4_empreinte_lue_dans_la_configuration_cas_sain(poste):
    """Sans variable, l'empreinte attendue vient de la liste des empreintes du code de la configuration de la course."""
    (poste["d"] / "config.json").write_text(json.dumps({"marqueurs": {"EMPREINTES_CODE_IIB": "scripts/lancer_iib_v2.sh " + "a" * 64 + " ; src/controle_ia/iib/location_v1.py "
                                                                      + EMPREINTE_MODULE + " ; tests/x.py " + "b" * 64}}), encoding="utf-8")
    r = _lancer(poste, "destruction", ID, poste["d"], IIB_LOCATION_SHA256=None)
    assert r.returncode == 0 and "module de lecture vérifié" in (poste["d"] / "destruction.txt").read_text(encoding="utf-8"), r.stdout + r.stderr


def test_erratum_n3_un_refus_de_creation_ne_consomme_pas_un_essai(monde, tmp_path):
    """N3. Refus de `creation` (réponse d'essai déjà présente, R12 ; module non vérifié) : aucune ligne `essai_creation` n'est écrite ;
    cas sain : la création suivante porte l'essai numéro 1."""
    d, r = _controles(monde)
    assert r.returncode == 0, r.stdout + r.stderr
    sup = dict(FAUX_INSTANCES=_instances(monde, []), FAUX_RETIRE="0")
    (d / "creation-brute-essai1.json").write_text("déjà là", encoding="utf-8")
    r = v1s._lancer(monde, "creation", "auto", "course", "0", d, **sup)
    assert r.returncode == 2 and "existe déjà (R12)" in r.stdout and "COMMANDE DE CRÉATION" not in r.stdout, r.stdout + r.stderr
    assert "essai_creation" not in (d / "lancement.txt").read_text(encoding="utf-8")
    (d / "creation-brute-essai1.json").rename(d / "creation-brute-essai1-ecartee.json")
    avant = (monde["tmp"] / "appels.txt").read_text(encoding="utf-8")
    r = v1s._lancer(monde, "creation", "auto", "course", "0", d, IIB_LOCATION_SHA256="0" * 64, **sup)
    assert r.returncode == 2 and "empreinte attendue" in r.stdout and "essai_creation" not in (d / "lancement.txt").read_text(encoding="utf-8"), r.stdout + r.stderr
    assert (monde["tmp"] / "appels.txt").read_text(encoding="utf-8")[len(avant):].split() in ([], ["--version"], ["--version", "--version"])      # refus avant toute recherche d'offres
    r = v1s._lancer(monde, "creation", "auto", "course", "0", d, **sup)
    assert r.returncode == 0 and "COMMANDE DE CRÉATION" in r.stdout, r.stdout + r.stderr
    lancement = (d / "lancement.txt").read_text(encoding="utf-8")
    assert lancement.count("essai_creation ") == 1 and "essai_creation 1\n" in lancement and "creation-brute-essai1.json" in r.stdout


def test_erratum_surveillance_copie_datee_des_journaux_a_la_fin_et_a_l_arret(poste):
    """À FIN (cas sain) : une copie datée, avec empreinte, de chaque journal de la surveillance ; rien d'autre ne change au régime."""
    r = _lancer(poste, "surveillance", ID, poste["d"])
    assert r.returncode == 0 and "FIN" in r.stdout and "journaux de la surveillance copiés" in r.stdout, r.stdout + r.stderr
    for nom in ("surveillance", "progres", "journal-dernier", "journal-instance"):
        (copie,) = _traces(poste, f"fin-de-surveillance-{nom}-")
        assert _empreinte_tenue(copie) and copie.read_bytes() == (poste["d"] / f"{nom}.txt").read_bytes()[:len(copie.read_bytes())], nom
    # ARRET (garde de dépense illisible trois fois : prix illisible dans lancement.txt) : copie aussi, et rien d'écrasé
    f = poste["d"] / "lancement.txt"
    f.write_text(f.read_text(encoding="utf-8").replace("prix_carte 1.0", "prix_carte x"), encoding="utf-8")
    r = _lancer(poste, "surveillance", ID, poste["d"])
    assert r.returncode == 3 and "ARRET" in r.stdout and f"stop instance {ID}" in r.stdout, r.stdout + r.stderr
    assert len(_traces(poste, "fin-de-surveillance-surveillance-")) == 2 and all(_empreinte_tenue(c) for c in _traces(poste, "fin-de-surveillance-"))
