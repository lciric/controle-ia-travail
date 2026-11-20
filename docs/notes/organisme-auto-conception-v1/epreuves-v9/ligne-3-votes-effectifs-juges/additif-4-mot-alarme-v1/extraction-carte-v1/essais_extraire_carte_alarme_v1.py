# -*- coding: utf-8 -*-
"""Essais de `extraire_carte_alarme_v1.py` — v1. Fichiers synthétiques seulement, jamais le vrai fichier.

Forme des fichiers synthétiques : celle que lit le masque scellé `masque_style_cartes_v1.py` —
objet de premier niveau {identifiant: {"contenu": {...}, "meta": {...}, "empreinte": "..."}}.
Les autres cartes, les autres identifiants et `meta` sont semés de chaînes repérables, cherchées
dans la sortie et à l'écran. Chaque garde est essayée sur le cas sain et sur un artefact (R5).
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile

import pytest

import extraire_carte_alarme_v1 as ex

ICI = os.path.dirname(os.path.abspath(__file__))
PROGRAMME = os.path.join(ICI, "extraire_carte_alarme_v1.py")
BASE_TEMPORAIRE = os.path.join(ICI, "essais-temporaires")

CIBLE = "idcible0000x1"
SEMIS_AUTRES_CARTES = "AUTRECARTESEMEE"
SEMIS_AUTRES_IDS = "AUTREIDENTSEME"
SEMIS_META = "METASECRETSEME"
TEXTE_CIBLE = "TEXTEDELACIBLEREPERABLE"

CARTE_CIBLE = {
    "contenu": {"titre": TEXTE_CIBLE + " titre", "mecanisme": "accents é à ç « guillemets »",
                "liste": [1, 2.5, None, True, {"imbrique": "valeur"}]},
    "meta": {"espece": SEMIS_META + "-cible", "graine": 12345},
    "empreinte": "abcdef0123",
}
ATTENDU = {k: v for k, v in CARTE_CIBLE.items() if k != "meta"}


def autre_enregistrement(i):
    return {"contenu": {"titre": f"{SEMIS_AUTRES_CARTES}-{i:03d}", "mecanisme": f"{SEMIS_AUTRES_CARTES} m{i}"},
            "meta": {"espece": f"{SEMIS_META}-{i:03d}"}, "empreinte": f"e{i:03d}"}


def texte_json(paires):
    """Objet JSON écrit à la main, pour pouvoir y mettre des clés en double."""
    return "{" + ", ".join(json.dumps(k, ensure_ascii=False) + ": " + json.dumps(v, ensure_ascii=False)
                           for k, v in paires) + "}"


def paires_saines(n=94, cible=CIBLE, carte=None):
    paires = [(f"{SEMIS_AUTRES_IDS}{i:03d}", autre_enregistrement(i)) for i in range(n - 1)]
    paires.insert(len(paires) // 2, (cible, CARTE_CIBLE if carte is None else carte))
    return paires


@pytest.fixture
def dossier():
    os.makedirs(BASE_TEMPORAIRE, exist_ok=True)
    return tempfile.mkdtemp(prefix="essai-", dir=BASE_TEMPORAIRE)


def ecrire_fiches(dossier, contenu):
    octets = contenu.encode("utf-8") if isinstance(contenu, str) else contenu
    chemin = os.path.join(dossier, "fiches-synthetiques.json")
    with open(chemin, "xb") as f:
        f.write(octets)
    return chemin, hashlib.sha256(octets).hexdigest()


def jouer(fiches, sortie, empreinte, identifiant=CIBLE, nombre=94):
    return ex.executer(fiches, sortie, empreinte, identifiant, nombre)


def sans_semis(texte):
    for s in (SEMIS_AUTRES_CARTES, SEMIS_AUTRES_IDS, SEMIS_META, "meta", "Traceback"):
        assert s not in texte, s


def refus_attendu(capsys, code, motif, sortie, fiches_pour_semis=True):
    ecran = capsys.readouterr()
    assert ecran.out == ""
    assert ecran.err.startswith("REFUS : ") and motif in ecran.err, ecran.err
    sans_semis(ecran.out + ecran.err)
    assert TEXTE_CIBLE not in ecran.err
    assert not os.path.lexists(sortie) and not os.path.lexists(sortie + ".sha256")
    return ecran.err


# ----------------------------------------------------------------------------- cas sain

def test_cas_sain(dossier, capsys):
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 0
    ecran = capsys.readouterr()
    assert ecran.out == "FAIT\n" and ecran.err == ""
    with open(sortie, "rb") as f:
        octets = f.read()
    objet = json.loads(octets.decode("utf-8"))
    assert list(objet) == ["carte", "empreinte_fiches", "identifiant"]
    assert objet["carte"] == ATTENDU
    assert list(objet["carte"]) == ["contenu", "empreinte"]
    assert objet["empreinte_fiches"] == emp and objet["identifiant"] == CIBLE
    texte = octets.decode("utf-8")
    sans_semis(texte)
    assert TEXTE_CIBLE in texte
    with open(sortie + ".sha256", encoding="utf-8") as f:
        assert f.read() == f"{hashlib.sha256(octets).hexdigest()}  carte.json\n"


def test_cas_sain_sans_meta_dans_la_carte(dossier, capsys):
    carte = {k: v for k, v in CARTE_CIBLE.items() if k != "meta"}
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines(carte=carte)))
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 0
    with open(sortie, encoding="utf-8") as f:
        assert json.load(f)["carte"] == ATTENDU


def test_meta_jamais_converti(dossier, capsys, monkeypatch):
    """La valeur de `meta` n'est jamais passée à la conversion : elle n'est pas « usée »."""
    vus = []
    origine = ex._en_objets

    def espion(v):
        vus.append(json.dumps(v, ensure_ascii=False, default=str))
        return origine(v)
    monkeypatch.setattr(ex, "_en_objets", espion)
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    assert jouer(fiches, os.path.join(dossier, "carte.json"), emp) == 0
    assert vus and all(SEMIS_META not in v and SEMIS_AUTRES_CARTES not in v for v in vus)


# ----------------------------------------------------------------------------- empreinte

def test_empreinte_fausse_rien_n_est_decode(dossier, capsys, monkeypatch):
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    sortie = os.path.join(dossier, "carte.json")

    def interdit(*a, **k):
        raise AssertionError("décodage tenté malgré une empreinte fausse")
    monkeypatch.setattr(ex, "decoder", interdit)
    faux = ("0" if emp[0] != "0" else "1") + emp[1:]
    assert jouer(fiches, sortie, faux) == 2
    err = refus_attendu(capsys, 2, "empreinte différente", sortie)
    assert emp not in err and faux not in err


def test_empreinte_d_un_octet_change(dossier, capsys):
    texte = texte_json(paires_saines())
    _, emp = ecrire_fiches(dossier, texte)
    autre = tempfile.mkdtemp(prefix="essai-", dir=BASE_TEMPORAIRE)
    fiches2, _ = ecrire_fiches(autre, texte + " ")
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches2, sortie, emp) == 2
    refus_attendu(capsys, 2, "empreinte différente", sortie)


# ----------------------------------------------------------------------------- compte

@pytest.mark.parametrize("n", [93, 95, 1])
def test_compte_faux(dossier, capsys, n):
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines(n=n)))
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "nombre de cartes", sortie)


# ----------------------------------------------------------------------------- identifiant

def test_identifiant_absent(dossier, capsys):
    paires = [(f"{SEMIS_AUTRES_IDS}{i:03d}", autre_enregistrement(i)) for i in range(94)]
    fiches, emp = ecrire_fiches(dossier, texte_json(paires))
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "identifiant gelé absent", sortie)


def test_identifiant_proche_ne_compte_pas(dossier, capsys):
    """Un identifiant qui contient la cible, ou que la cible contient, n'est pas la cible."""
    paires = [(f"{SEMIS_AUTRES_IDS}{i:03d}", autre_enregistrement(i)) for i in range(92)]
    paires += [(CIBLE + "z", autre_enregistrement(500)), (CIBLE[:-1], autre_enregistrement(501))]
    fiches, emp = ecrire_fiches(dossier, texte_json(paires))
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "identifiant gelé absent", sortie)


def test_identifiant_en_double(dossier, capsys):
    paires = paires_saines()                       # 94 identifiants distincts
    paires.append((CIBLE, CARTE_CIBLE))            # la cible une seconde fois : 95 paires, 94 distincts
    fiches, emp = ecrire_fiches(dossier, texte_json(paires))
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "présent plus d'une fois", sortie)


def test_identifiant_en_double_avec_cartes_differentes(dossier, capsys):
    paires = paires_saines()
    paires.append((CIBLE, autre_enregistrement(900)))
    fiches, emp = ecrire_fiches(dossier, texte_json(paires))
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "présent plus d'une fois", sortie)


def test_autre_cle_en_double(dossier, capsys):
    paires = paires_saines()
    paires.append((f"{SEMIS_AUTRES_IDS}007", autre_enregistrement(7)))
    fiches, emp = ecrire_fiches(dossier, texte_json(paires))
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "autre clé du premier niveau est en double", sortie)


# ----------------------------------------------------------------------------- structure

def test_premier_niveau_pas_un_objet(dossier, capsys):
    fiches, emp = ecrire_fiches(dossier, json.dumps([[k, v] for k, v in paires_saines()]))
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "premier niveau", sortie)


def test_carte_pas_un_objet(dossier, capsys):
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines(carte=[TEXTE_CIBLE])))
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "n'est pas un objet", sortie)


def test_carte_sans_contenu(dossier, capsys):
    carte = {"corps": TEXTE_CIBLE, "meta": {"espece": SEMIS_META}}
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines(carte=carte)))
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "pas de `contenu`", sortie)


def test_carte_avec_meta_en_double(dossier, capsys):
    carte_txt = ('{"contenu": {"titre": "' + TEXTE_CIBLE + '"}, "meta": {"a": "' + SEMIS_META
                 + '1"}, "meta": {"a": "' + SEMIS_META + '2"}}')
    paires = paires_saines()
    texte = texte_json(paires).replace(json.dumps(CIBLE) + ": " + json.dumps(CARTE_CIBLE, ensure_ascii=False),
                                       json.dumps(CIBLE) + ": " + carte_txt)
    assert carte_txt in texte
    fiches, emp = ecrire_fiches(dossier, texte)
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "clé en double au premier niveau de l'enregistrement", sortie)


def test_cle_en_double_dans_le_contenu(dossier, capsys):
    carte_txt = '{"contenu": {"titre": "' + TEXTE_CIBLE + '1", "titre": "' + TEXTE_CIBLE + '2"}, "meta": {}}'
    texte = texte_json(paires_saines()).replace(
        json.dumps(CIBLE) + ": " + json.dumps(CARTE_CIBLE, ensure_ascii=False), json.dumps(CIBLE) + ": " + carte_txt)
    assert carte_txt in texte
    fiches, emp = ecrire_fiches(dossier, texte)
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "clé en double dans un objet de la carte", sortie)


def test_json_illisible_sans_texte_dans_le_message(dossier, capsys):
    texte = texte_json(paires_saines())
    coupe = texte.index(", " + json.dumps(f"{SEMIS_AUTRES_IDS}050"))   # entre deux paires : JSON cassé à coup sûr
    texte = texte[:coupe] + " " + SEMIS_AUTRES_CARTES + "-casse " + texte[coupe:]
    fiches, emp = ecrire_fiches(dossier, texte)
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "JSON illisible", sortie)


def test_octets_non_utf8(dossier, capsys):
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()).encode("utf-8") + b"\xff\xfe")
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "UTF-8 ou JSON illisible", sortie)


def test_fiches_absent(dossier, capsys):
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(os.path.join(dossier, "absent.json"), sortie, "0" * 64) == 2
    refus_attendu(capsys, 2, "fichier absent", sortie)


# ----------------------------------------------------------------------------- sortie

def test_sortie_existante(dossier, capsys):
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    sortie = os.path.join(dossier, "carte.json")
    with open(sortie, "w", encoding="utf-8") as f:
        f.write("ancien\n")
    assert jouer(fiches, sortie, emp) == 2
    ecran = capsys.readouterr()
    assert "existe déjà" in ecran.err and ecran.out == ""
    with open(sortie, encoding="utf-8") as f:
        assert f.read() == "ancien\n"
    assert not os.path.lexists(sortie + ".sha256")


def test_compagnon_existant(dossier, capsys):
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    sortie = os.path.join(dossier, "carte.json")
    with open(sortie + ".sha256", "w", encoding="utf-8") as f:
        f.write("ancien\n")
    assert jouer(fiches, sortie, emp) == 2
    assert "existe déjà" in capsys.readouterr().err
    assert not os.path.lexists(sortie)


def test_sortie_lien_pendant(dossier, capsys):
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    sortie = os.path.join(dossier, "carte.json")
    os.symlink(os.path.join(dossier, "cible-inexistante"), sortie)
    assert jouer(fiches, sortie, emp) == 2
    assert "existe déjà" in capsys.readouterr().err
    assert not os.path.lexists(os.path.join(dossier, "cible-inexistante"))


def test_sortie_sous_dossier_archives(dossier, capsys):
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    interdit = os.path.join(dossier, "archives-reponses-modeles", "sous")
    os.makedirs(interdit)
    sortie = os.path.join(interdit, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "archives-reponses-modeles", sortie)


def test_sortie_par_lien_vers_dossier_archives(dossier, capsys):
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    interdit = os.path.join(dossier, "archives-reponses-modeles")
    os.makedirs(interdit)
    lien = os.path.join(dossier, "lien-anodin")
    os.symlink(interdit, lien)
    sortie = os.path.join(lien, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "archives-reponses-modeles", sortie)


def test_sortie_sous_le_depot(dossier, capsys):
    """Chemin sous le dépôt dont le dossier n'existe pas : même une garde fautive n'y écrirait rien."""
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    sortie = os.path.join(ex.DEPOT, "dossier-inexistant-essai-extraction", "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "sous le dépôt", sortie)


def test_sortie_le_depot_lui_meme_par_detour(dossier, capsys):
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    sortie = ex.DEPOT + "/./dossier-inexistant-essai-extraction/../dossier-inexistant-essai-2/carte.json"
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "sous le dépôt", sortie)


def test_sortie_par_lien_vers_le_depot(dossier, capsys):
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    lien = os.path.join(dossier, "lien-anodin")
    os.symlink(os.path.join(ex.DEPOT, "dossier-inexistant-essai-extraction"), lien)  # lien pendant
    sortie = os.path.join(lien, "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "sous le dépôt", sortie)


def test_depot_voisin_n_est_pas_le_depot():
    assert not ex._sous(ex.DEPOT + "-autre/x.json", ex.DEPOT)
    assert ex._sous(ex.DEPOT + "/x.json", ex.DEPOT) and ex._sous(ex.DEPOT, ex.DEPOT)


def test_sortie_dossier_parent_absent(dossier, capsys):
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    sortie = os.path.join(dossier, "absent", "carte.json")
    assert jouer(fiches, sortie, emp) == 2
    refus_attendu(capsys, 2, "dossier parent absent", sortie)


def test_sortie_verifiee_avant_lecture_des_fiches(dossier, capsys, monkeypatch):
    def interdit(*a, **k):
        raise AssertionError("fiches lues malgré une sortie interdite")
    monkeypatch.setattr(ex, "lire_octets_verifies", interdit)
    sortie = os.path.join(ex.DEPOT, "dossier-inexistant-essai-extraction", "carte.json")
    assert jouer(os.path.join(dossier, "x.json"), sortie, "0" * 64) == 2
    assert "sous le dépôt" in capsys.readouterr().err


# ----------------------------------------------------------------------------- paramètres et écran

@pytest.mark.parametrize("emp, ident, n", [("ABC", CIBLE, 94), ("A" * 64, CIBLE, 94), ("0" * 64, "", 94),
                                           ("0" * 64, CIBLE, 0), ("0" * 64, CIBLE, True)])
def test_parametres_mal_formes(dossier, capsys, emp, ident, n):
    sortie = os.path.join(dossier, "carte.json")
    assert ex.executer(os.path.join(dossier, "x.json"), sortie, emp, ident, n) == 2
    assert "paramètres" in capsys.readouterr().err


def test_erreur_imprevue_sans_message_ni_trace(dossier, capsys, monkeypatch):
    def piege(*a, **k):
        raise KeyError(SEMIS_AUTRES_IDS + " " + SEMIS_AUTRES_CARTES + " " + SEMIS_META + " " + TEXTE_CIBLE)
    monkeypatch.setattr(ex, "garder_la_seule_carte", piege)
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    sortie = os.path.join(dossier, "carte.json")
    assert jouer(fiches, sortie, emp) == 3
    ecran = capsys.readouterr()
    assert ecran.err == "REFUS : erreur imprévue (KeyError) ; aucun détail affiché\n"
    assert TEXTE_CIBLE not in ecran.err
    sans_semis(ecran.out + ecran.err)
    assert not os.path.lexists(sortie)


def test_constantes_gelees():
    assert ex.EMPREINTE_FICHES == "ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481"
    assert ex.IDENTIFIANT_CARTE == "fcbf4a2dd1a57"
    assert ex.NOMBRE_CARTES == 94


def test_ligne_de_commande_n_accepte_que_les_constantes(dossier, capsys):
    """Un fichier synthétique sain est refusé par la ligne de commande : elle n'a que l'empreinte gelée."""
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines(cible=ex.IDENTIFIANT_CARTE)))
    assert emp != ex.EMPREINTE_FICHES
    sortie = os.path.join(dossier, "carte.json")
    assert ex.main(["--fiches", fiches, "--sortie", sortie]) == 2
    refus_attendu(capsys, 2, "empreinte différente", sortie)
    for options in (["--fiches", fiches, "--sortie", sortie, "--empreinte", emp],
                    ["--fiches", fiches, "--sortie", sortie, "--identifiant", CIBLE],
                    ["--fich", fiches, "--sortie", sortie],
                    ["--sortie", sortie]):
        with pytest.raises(SystemExit) as e:
            ex.main(options)
        assert e.value.code == 2
    assert not os.path.lexists(sortie)


def test_ligne_de_commande_en_processus(dossier):
    """Écran réel d'un refus par la ligne de commande : motif seul, aucune trace, aucun semis."""
    fiches, _ = ecrire_fiches(dossier, texte_json(paires_saines(cible=ex.IDENTIFIANT_CARTE)))
    sortie = os.path.join(dossier, "carte.json")
    r = subprocess.run([sys.executable, "-B", PROGRAMME, "--fiches", fiches, "--sortie", sortie],
                       capture_output=True, text=True, cwd=dossier)
    assert r.returncode == 2 and r.stdout == ""
    assert r.stderr == "REFUS : fiches : empreinte différente de l'empreinte gelée ; rien n'est décodé\n"
    sans_semis(r.stdout + r.stderr)
    assert not os.path.lexists(sortie)


def test_ecran_du_cas_sain_en_processus(dossier):
    """Le cas sain par le moyen interne, dans un processus à part : écran « FAIT » et rien d'autre."""
    fiches, emp = ecrire_fiches(dossier, texte_json(paires_saines()))
    sortie = os.path.join(dossier, "carte.json")
    lanceur = os.path.join(dossier, "lanceur_essai.py")
    with open(lanceur, "x", encoding="utf-8") as f:
        f.write("import sys\nsys.path.insert(0, sys.argv[1])\nimport extraire_carte_alarme_v1 as ex\n"
                "sys.exit(ex.executer(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], 94))\n")
    r = subprocess.run([sys.executable, "-B", lanceur, ICI, fiches, sortie, emp, CIBLE],
                       capture_output=True, text=True, cwd=dossier)
    assert (r.returncode, r.stdout, r.stderr) == (0, "FAIT\n", "")
    with open(sortie, encoding="utf-8") as f:
        assert json.load(f)["carte"] == ATTENDU
