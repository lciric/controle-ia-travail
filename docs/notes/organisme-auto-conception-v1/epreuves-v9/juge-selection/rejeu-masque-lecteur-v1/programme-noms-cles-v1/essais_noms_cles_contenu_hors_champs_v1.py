# -*- coding: utf-8 -*-
"""Essais de noms_cles_contenu_hors_champs_v1.py — v1.

Fichiers SYNTHÉTIQUES seulement, jamais le vrai fichier des cartes. Ils s'écrivent sous le dossier de
ces essais, dans `fichiers-essais-v1/`, un dossier neuf par essai ; rien ne s'écrit ailleurs (le masque
scellé est lu pour comparaison et exécuté depuis ses octets, sans fichier compilé).
Lancement : env -C DOSSIER python3 -B -m pytest -q -p no:cacheprovider essais_noms_cles_contenu_hors_champs_v1.py

Les empreintes gelées se remplacent par l'appel interne `lancer(…, sha_fiches=…, sha_configuration=…)` ;
la ligne de commande n'accepte que les constantes (essais dédiés).
Valeurs et identifiants sont semés de marques repérables : aucune ne doit sortir, ni dans la sortie,
ni dans son compagnon, ni à l'écran.
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import types

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
CHEMIN_PROGRAMME = os.path.join(ICI, "noms_cles_contenu_hors_champs_v1.py")
CHEMIN_MASQUE = ("/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/"
                 "juge-selection/criteres-v4/masque_style_cartes_v1.py")
SHA_MASQUE = "07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e"
BASE_ESSAIS = os.path.join(ICI, "fichiers-essais-v1")

MARQUE_VALEUR = "qzvaleursemeeqz"
MARQUE_IDENT = "qzidentsemeqz"
CHAMPS = ["question", "contexte", "hypothese", "prediction", "methode",
          "mesure", "seuil", "risques", "cout", "nouveaute"]          # dix champs, comme la configuration A
GARDE = "(nom non rapporté : longueur {})"


def _charger_depuis_octets(nom, chemin, sha_attendu=None):
    """Charge un module depuis ses octets, sans écrire de fichier compilé (rien sous le dépôt)."""
    with open(chemin, "rb") as f:
        source = f.read()
    if sha_attendu is not None:
        assert hashlib.sha256(source).hexdigest() == sha_attendu, f"empreinte de {nom} différente"
    module = types.ModuleType(nom)
    module.__file__ = chemin
    exec(compile(source, chemin, "exec"), module.__dict__)
    return module


prog = _charger_depuis_octets("noms_cles_contenu_hors_champs_v1", CHEMIN_PROGRAMME)


def masque_scelle():
    return _charger_depuis_octets("masque_style_cartes_v1", CHEMIN_MASQUE, SHA_MASQUE)


# ----------------------------------------------------------------------------- fabrique synthétique

def configuration(hors_choix=(), **remplace):
    c = {"champs": list(CHAMPS), "plafond": "mediane", "formules": ["comme indiqué plus haut"],
         "intertitres": ["Résumé"], "seuil_formule_recitee": 0.5, "minimum_formule_recitee": 2,
         "hors_choix": list(hors_choix)}
    c.update(remplace)
    return c


def ident(n):
    return f"carte-{MARQUE_IDENT}-{n:03d}"


def carte(n, en_plus=()):
    contenu = {k: f"Texte {MARQUE_VALEUR} de la carte {n}, champ {k}." for k in CHAMPS}
    for nom in en_plus:
        contenu[nom] = f"Valeur {MARQUE_VALEUR} en plus, carte {n}."
    return {"contenu": contenu,
            "meta": {"espece": f"{MARQUE_VALEUR}-espece-{n}", "auteur": f"{MARQUE_VALEUR}-auteur"},
            "empreinte": f"{MARQUE_VALEUR}-empreinte-{n}"}


def fiches(n=6, en_plus=None):
    en_plus = en_plus or {}
    return {ident(i): carte(i, en_plus.get(i, ())) for i in range(n)}


@pytest.fixture
def dossier(request):
    os.makedirs(BASE_ESSAIS, exist_ok=True)
    return tempfile.mkdtemp(prefix=request.node.name[:48] + "-", dir=BASE_ESSAIS)


def _ecrire(dossier, nom, objet_ou_octets):
    octets = objet_ou_octets if isinstance(objet_ou_octets, bytes) else \
        json.dumps(objet_ou_octets, ensure_ascii=False, indent=1).encode("utf-8")
    chemin = os.path.join(dossier, nom)
    with open(chemin, "xb") as f:
        f.write(octets)
    return chemin, hashlib.sha256(octets).hexdigest()


def jouer(dossier, capsys, les_fiches, la_conf, *, sha_fiches=None, sha_configuration=None, sortie=None):
    ici = tempfile.mkdtemp(dir=dossier)
    chemin_f, sha_f = _ecrire(ici, "fiches-synthetiques.json", les_fiches)
    chemin_c, sha_c = _ecrire(ici, "configuration-synthetique.json", la_conf)
    sortie = sortie or os.path.join(ici, "sortie.json")
    code = prog.lancer(chemin_f, chemin_c, sortie,
                       sha_fiches=sha_fiches or sha_f, sha_configuration=sha_configuration or sha_c)
    ecran = capsys.readouterr()
    return types.SimpleNamespace(code=code, sortie=sortie, out=ecran.out, err=ecran.err,
                                 sha_f=sha_f, sha_c=sha_c, chemin_f=chemin_f, chemin_c=chemin_c)


def lire_sortie(sortie):
    with open(sortie, "rb") as f:
        octets = f.read()
    with open(sortie + ".sha256", encoding="utf-8") as f:
        compagnon = f.read()
    assert compagnon == f"{hashlib.sha256(octets).hexdigest()}  {os.path.basename(sortie)}\n"
    assert octets.isascii()
    objet = json.loads(octets.decode("utf-8"))
    assert list(objet) == ["cles_hors_champs", "nombre_de_cartes", "empreintes"]      # trois champs seulement
    return objet, octets.decode("utf-8"), compagnon


def sans_fuite(*textes):
    for t in textes:
        assert MARQUE_VALEUR not in t
        assert MARQUE_IDENT not in t
        assert "carte-" not in t


def rien_ecrit(sortie):
    assert not os.path.exists(sortie)
    assert not os.path.exists(sortie + ".sha256")


def journaliser(monkeypatch):
    journal = []
    lire, decoder, compter = prog.lire_octets_verifies, prog.decoder_json, prog.compter_noms_hors_champs

    def lire_j(chemin, sha, role):
        journal.append(("octets", role))
        return lire(chemin, sha, role)

    def decoder_j(octets, role):
        journal.append(("decodage", role))
        return decoder(octets, role)

    def compter_j(les_fiches, champs, hors_choix):
        journal.append(("cles", tuple(champs)))
        return compter(les_fiches, champs, hors_choix)

    monkeypatch.setattr(prog, "lire_octets_verifies", lire_j)
    monkeypatch.setattr(prog, "decoder_json", decoder_j)
    monkeypatch.setattr(prog, "compter_noms_hors_champs", compter_j)
    return journal


# ----------------------------------------------------------------------------- essais

def test_constantes_gelees():
    assert prog.SHA_FICHES == "ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481"
    assert prog.SHA_CONFIGURATION == "8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4"


def test_forme_synthetique_celle_que_le_masque_scelle_attend():
    masque = masque_scelle()
    conf = masque.valider_configuration(configuration())
    assert len(conf["champs"]) == 10
    contenus = masque.extraire_contenus(fiches(), conf["champs"], conf["hors_choix"])
    assert len(contenus) == 6 and all(list(c) == CHAMPS for c in contenus.values())
    # le refus que ce programme vient éclairer, reproduit sur une carte synthétique
    with pytest.raises(masque.Refus, match=r"champ\(s\) hors de la configuration \(1\)"):
        masque.extraire_contenus(fiches(en_plus={2: ["commentaire"]}), conf["champs"], conf["hors_choix"])


@pytest.mark.parametrize("conf", [
    configuration(),
    configuration(plafond={k: 50 for k in CHAMPS}, seuil_formule_recitee=None),
    {**configuration(), "autre": 1},
    configuration(champs=CHAMPS + ["question"]),
    configuration(champs=CHAMPS + ["meta"]),
    configuration(champs=[]),
    configuration(plafond={"question": 3}),
    configuration(hors_choix=[""]),
    configuration(seuil_formule_recitee=0),
    configuration(minimum_formule_recitee=1),
    [],
], ids=["saine", "plafond-entier", "cle-de-trop", "doublon", "meta", "vide", "plafond-partiel",
        "hors-choix-vide", "seuil-nul", "minimum-1", "pas-un-objet"])
def test_configuration_validee_exactement_comme_le_masque(conf):
    masque = masque_scelle()
    try:
        masque.valider_configuration(json.loads(json.dumps(conf)))
        attendu = None
    except masque.Refus as e:
        attendu = str(e)
    try:
        prog.valider_configuration(json.loads(json.dumps(conf)))
        obtenu = None
    except prog.Refus as e:
        obtenu = str(e)
    assert obtenu == attendu


def test_cas_sain_liste_vide(dossier, capsys):
    r = jouer(dossier, capsys, fiches(), configuration())
    assert r.code == 0
    assert r.out == "FAIT\n" and r.err == ""
    objet, brut, compagnon = lire_sortie(r.sortie)
    assert objet == {"cles_hors_champs": [], "nombre_de_cartes": 6,
                     "empreintes": {"fiches": r.sha_f, "configuration": r.sha_c}}
    sans_fuite(brut, compagnon, r.out, r.err)


def test_une_cle_de_plus_sur_une_carte(dossier, capsys):
    r = jouer(dossier, capsys, fiches(en_plus={3: ["commentaire"]}), configuration())
    assert r.code == 0 and r.out == "FAIT\n" and r.err == ""
    objet, brut, compagnon = lire_sortie(r.sortie)
    assert objet["cles_hors_champs"] == [{"nom": "commentaire", "nombre_de_cartes": 1}]
    assert objet["nombre_de_cartes"] == 6
    sans_fuite(brut, compagnon, r.out, r.err)


def test_deux_cles_de_plus_sur_des_nombres_de_cartes_differents(dossier, capsys):
    en_plus = {0: ["zeta"], 1: ["zeta", "beta"], 4: ["zeta"]}
    r = jouer(dossier, capsys, fiches(en_plus=en_plus), configuration())
    assert r.code == 0 and r.out == "FAIT\n" and r.err == ""
    objet, brut, compagnon = lire_sortie(r.sortie)
    assert objet["cles_hors_champs"] == [{"nom": "beta", "nombre_de_cartes": 1},
                                         {"nom": "zeta", "nombre_de_cartes": 3}]   # triée par nom
    assert objet["nombre_de_cartes"] == 6
    sans_fuite(brut, compagnon, r.out, r.err)


def test_garde_nom_long_ou_a_saut_de_ligne(dossier, capsys):
    n64, n65 = "a" * 64, "b" * 65
    long_seme = (MARQUE_VALEUR + " ") * 10                     # 160 caractères de « contenu »
    en_plus = {0: [n64, n65, long_seme, "deux\nlignes", "remarqué"],
               1: ["retour\rchariot", "sep ligne", "c" * 70],
               2: ["c" * 70, "d" * 70]}
    r = jouer(dossier, capsys, fiches(en_plus=en_plus), configuration())
    assert r.code == 0 and r.out == "FAIT\n" and r.err == ""
    objet, brut, compagnon = lire_sortie(r.sortie)
    assert objet["cles_hors_champs"] == [
        {"nom": GARDE.format(11), "nombre_de_cartes": 1},      # « deux\nlignes »
        {"nom": GARDE.format(14), "nombre_de_cartes": 1},      # « retour\rchariot »
        {"nom": GARDE.format(160), "nombre_de_cartes": 1},     # nom long semé de la marque des valeurs
        {"nom": GARDE.format(65), "nombre_de_cartes": 1},
        {"nom": GARDE.format(70), "nombre_de_cartes": 1},      # « d » × 70 : compte gardé à part
        {"nom": GARDE.format(70), "nombre_de_cartes": 2},      # « c » × 70
        {"nom": GARDE.format(9), "nombre_de_cartes": 1},       # « sep U+2028 ligne »
        {"nom": n64, "nombre_de_cartes": 1},                   # 64 caractères : écrit tel quel
        {"nom": "remarqué", "nombre_de_cartes": 1},            # échappé en ASCII, exact une fois décodé
    ]
    assert "remarqu\\u00e9" in brut
    for mot in ("lignes", "chariot", "bbbb", "cccc", "dddd"):
        assert mot not in brut
    sans_fuite(brut, compagnon, r.out, r.err)


def test_empreinte_fausse_de_la_configuration(dossier, capsys):
    r = jouer(dossier, capsys, fiches(en_plus={1: ["x"]}), configuration(), sha_configuration="0" * 64)
    assert r.code == 2 and r.out == ""
    assert r.err == "REFUS : configuration : empreinte différente de l'empreinte gelée\n"
    rien_ecrit(r.sortie)
    sans_fuite(r.out, r.err)


def test_empreinte_fausse_des_fiches(dossier, capsys):
    r = jouer(dossier, capsys, fiches(en_plus={1: ["x"]}), configuration(), sha_fiches="f" * 64)
    assert r.code == 2 and r.out == ""
    assert r.err == "REFUS : fiches : empreinte différente de l'empreinte gelée\n"
    rien_ecrit(r.sortie)
    sans_fuite(r.out, r.err)


def test_empreinte_gelee_mal_formee(dossier, capsys):
    r = jouer(dossier, capsys, fiches(), configuration(), sha_fiches="ABC")
    assert r.code == 2 and "fiches : empreinte gelée illisible" in r.err
    rien_ecrit(r.sortie)


def test_empreintes_comparees_avant_tout_decodage(dossier, capsys, monkeypatch):
    journal = journaliser(monkeypatch)
    pas_du_json = b'{"carte": "\xff' + MARQUE_VALEUR.encode()
    # cartes illisibles et empreinte fausse : refus d'empreinte, aucun décodage, pas même la configuration
    r = jouer(dossier, capsys, pas_du_json, configuration(), sha_fiches="1" * 64)
    assert r.code == 2 and r.err == "REFUS : fiches : empreinte différente de l'empreinte gelée\n"
    assert journal == [("octets", "configuration"), ("octets", "fiches")]
    rien_ecrit(r.sortie)
    # configuration illisible et empreinte fausse : refus d'empreinte, les cartes ne sont pas même lues
    journal.clear()
    r = jouer(dossier, capsys, fiches(), pas_du_json, sha_configuration="2" * 64)
    assert r.code == 2 and r.err == "REFUS : configuration : empreinte différente de l'empreinte gelée\n"
    assert journal == [("octets", "configuration")]
    rien_ecrit(r.sortie)
    # cartes illisibles, empreinte juste : refus de décodage, sans l'octet fautif ni rien du contenu
    journal.clear()
    r = jouer(dossier, capsys, pas_du_json, configuration())
    assert r.code == 2 and r.err == "REFUS : fiches : JSON illisible\n"
    assert "0xff" not in r.err and "\\xff" not in r.err
    assert journal == [("octets", "configuration"), ("octets", "fiches"),
                       ("decodage", "configuration"), ("decodage", "fiches")]
    rien_ecrit(r.sortie)
    sans_fuite(r.out, r.err)


def test_ordre_configuration_puis_cartes(dossier, capsys, monkeypatch):
    journal = journaliser(monkeypatch)
    r = jouer(dossier, capsys, fiches(en_plus={2: ["commentaire"]}), configuration())
    assert r.code == 0
    assert journal == [("octets", "configuration"), ("octets", "fiches"),
                       ("decodage", "configuration"), ("decodage", "fiches"),
                       ("cles", tuple(CHAMPS))]               # les champs viennent de la configuration
    # configuration d'empreinte juste mais refusée par la validation du masque : les cartes ne sont pas décodées
    journal.clear()
    r = jouer(dossier, capsys, fiches(), {**configuration(), "autre": 1})
    assert r.code == 2 and r.err.startswith("REFUS : configuration : clés attendues")
    assert journal == [("octets", "configuration"), ("octets", "fiches"), ("decodage", "configuration")]
    rien_ecrit(r.sortie)
    # la configuration absente : les cartes ne sont pas lues
    journal.clear()
    ici = tempfile.mkdtemp(dir=dossier)
    chemin_f, sha_f = _ecrire(ici, "fiches-synthetiques.json", fiches())
    sortie = os.path.join(ici, "sortie.json")
    code = prog.lancer(chemin_f, os.path.join(ici, "configuration-absente.json"), sortie,
                       sha_fiches=sha_f, sha_configuration="3" * 64)
    ecran = capsys.readouterr()
    assert code == 2 and ecran.err == "REFUS : configuration : fichier absent\n"
    assert journal == [("octets", "configuration")]
    rien_ecrit(sortie)


def test_sortie_existante(dossier, capsys, monkeypatch):
    journal = journaliser(monkeypatch)
    ici = tempfile.mkdtemp(dir=dossier)
    sortie = os.path.join(ici, "sortie.json")
    with open(sortie, "xb") as f:
        f.write(b"ancien\n")
    r = jouer(dossier, capsys, fiches(en_plus={1: ["x"]}), configuration(), sortie=sortie)
    assert r.code == 2 and r.err == "REFUS : sortie déjà présente : on n'écrase jamais (règle R12)\n"
    with open(sortie, "rb") as f:
        assert f.read() == b"ancien\n"
    assert not os.path.exists(sortie + ".sha256")
    assert journal == []                                       # rien n'est lu avant ce contrôle
    # le compagnon seul suffit à refuser
    sortie2 = os.path.join(ici, "sortie2.json")
    with open(sortie2 + ".sha256", "xb") as f:
        f.write(b"ancien compagnon\n")
    r = jouer(dossier, capsys, fiches(), configuration(), sortie=sortie2)
    assert r.code == 2 and "sortie déjà présente" in r.err
    assert not os.path.exists(sortie2)
    with open(sortie2 + ".sha256", "rb") as f:
        assert f.read() == b"ancien compagnon\n"
    assert journal == []


def test_dossier_de_sortie_absent(dossier, capsys, monkeypatch):
    journal = journaliser(monkeypatch)
    sortie = os.path.join(dossier, "dossier-qui-n-existe-pas", "sortie.json")
    r = jouer(dossier, capsys, fiches(), configuration(), sortie=sortie)
    assert r.code == 2 and r.err == "REFUS : dossier de la sortie absent\n"
    assert journal == []
    rien_ecrit(sortie)


def test_aucune_valeur_ni_identifiant_ne_sort(dossier, capsys):
    les_fiches = fiches(n=6, en_plus={3: ["commentaire"], 5: ["piege_hors_choix"]})
    # des valeurs de toute espèce JSON, semées : le programme ne les regarde pas
    les_fiches[ident(0)]["contenu"]["question"] = {MARQUE_VALEUR: [MARQUE_VALEUR, 1, None, True]}
    les_fiches[ident(1)]["contenu"]["methode"] = None
    les_fiches[ident(2)]["contenu"]["mesure"] = [3.5, MARQUE_VALEUR]
    les_fiches[ident(3)]["contenu"]["commentaire"] = {"sous": {MARQUE_VALEUR: ident(4)}}
    les_fiches[ident(4)]["meta"] = {"identifiant": ident(4), "espece": MARQUE_VALEUR}
    r = jouer(dossier, capsys, les_fiches, configuration(hors_choix=[ident(5)]))
    assert r.code == 0 and r.out == "FAIT\n" and r.err == ""
    objet, brut, compagnon = lire_sortie(r.sortie)
    assert objet["cles_hors_champs"] == [{"nom": "commentaire", "nombre_de_cartes": 1}]
    assert objet["nombre_de_cartes"] == 5
    for mot in ("Texte", "Valeur", "espece", "auteur", "empreinte-", "sous", "3.5"):
        assert mot not in brut
    sans_fuite(brut, compagnon, r.out, r.err)


def test_cartes_hors_du_choix_non_ouvertes_comme_dans_le_masque(dossier, capsys):
    les_fiches = fiches(n=6, en_plus={1: ["piege"]})
    les_fiches[ident(4)] = {"sans_contenu": MARQUE_VALEUR}            # hors du choix : jamais ouverte
    conf = configuration(hors_choix=[ident(1), ident(4)])
    masque = masque_scelle()
    assert len(masque.extraire_contenus(json.loads(json.dumps(les_fiches)), conf["champs"], conf["hors_choix"])) == 4
    r = jouer(dossier, capsys, les_fiches, conf)
    assert r.code == 0 and r.out == "FAIT\n" and r.err == ""
    objet, brut, compagnon = lire_sortie(r.sortie)
    assert objet["cles_hors_champs"] == [] and objet["nombre_de_cartes"] == 4
    sans_fuite(brut, compagnon, r.out, r.err)


def _sans_contenu(f):
    f[ident(2)] = {"meta": {"espece": MARQUE_VALEUR}}
    return f


def _pas_un_objet(f):
    f[ident(2)] = f"texte {MARQUE_VALEUR}"
    return f


def _contenu_liste(f):
    f[ident(2)]["contenu"] = [MARQUE_VALEUR]
    return f


@pytest.mark.parametrize("les_fiches, conf, motif", [
    ([{"contenu": {}}], configuration(), "cartes : objet {identifiant: enregistrement} non vide attendu"),
    ({}, configuration(), "cartes : objet {identifiant: enregistrement} non vide attendu"),
    (_sans_contenu(fiches()), configuration(), "cartes : un enregistrement est sans `contenu`"),
    (_pas_un_objet(fiches()), configuration(), "cartes : un enregistrement est sans `contenu`"),
    (_contenu_liste(fiches()), configuration(), "cartes : un `contenu` n'est pas un objet de champs"),
    (fiches(n=2), configuration(hors_choix=[ident(0), ident(1)]), "cartes : aucune carte ouverte (toutes hors du choix)"),
], ids=["liste", "vide", "sans-contenu", "pas-un-objet", "contenu-liste", "toutes-hors-du-choix"])
def test_refus_de_structure(dossier, capsys, les_fiches, conf, motif):
    r = jouer(dossier, capsys, les_fiches, conf)
    assert r.code == 2 and r.out == "" and r.err == f"REFUS : {motif}\n"
    rien_ecrit(r.sortie)
    sans_fuite(r.out, r.err)


def test_erreur_imprevue_message_non_rapporte(dossier, capsys, monkeypatch):
    def piege(*a, **k):
        raise ValueError(f"nom {MARQUE_VALEUR} de la {ident(1)}")
    monkeypatch.setattr(prog, "compter_noms_hors_champs", piege)
    r = jouer(dossier, capsys, fiches(), configuration())
    assert r.code == 2 and r.out == ""
    assert r.err == "REFUS : erreur imprévue (ValueError), message non rapporté\n"
    rien_ecrit(r.sortie)
    sans_fuite(r.out, r.err)


def test_main_ne_passe_que_les_constantes(monkeypatch):
    vu = {}

    def lancer_espion(*a, **k):
        vu["a"], vu["k"] = a, k
        return 0
    monkeypatch.setattr(prog, "lancer", lancer_espion)
    assert prog.main(["--fiches", "F", "--configuration", "C", "--sortie", "S"]) == 0
    assert vu["a"] == ("F", "C", "S")
    assert vu["k"] == {"sha_fiches": prog.SHA_FICHES, "sha_configuration": prog.SHA_CONFIGURATION}


def _ligne_de_commande(*args):
    return subprocess.run([sys.executable, "-B", CHEMIN_PROGRAMME, *args],
                          capture_output=True, text=True, timeout=120)


def test_ligne_de_commande_refuse_des_fichiers_synthetiques(dossier):
    ici = tempfile.mkdtemp(dir=dossier)
    chemin_f, _ = _ecrire(ici, "fiches-synthetiques.json", fiches(en_plus={1: ["x"]}))
    chemin_c, _ = _ecrire(ici, "configuration-synthetique.json", configuration())
    sortie = os.path.join(ici, "sortie.json")
    p = _ligne_de_commande("--fiches", chemin_f, "--configuration", chemin_c, "--sortie", sortie)
    assert p.returncode == 2 and p.stdout == ""
    assert p.stderr == "REFUS : configuration : empreinte différente de l'empreinte gelée\n"
    rien_ecrit(sortie)
    sans_fuite(p.stdout, p.stderr)


@pytest.mark.parametrize("args, motif", [
    ([], "the following arguments are required"),
    (["--fiches", "F", "--configuration", "C"], "the following arguments are required"),
    (["--fiches", "F", "--configuration", "C", "--sortie", "S", "--sha-fiches", "0" * 64], "unrecognized arguments"),
    (["--fich", "F", "--configuration", "C", "--sortie", "S"], "the following arguments are required"),
], ids=["aucun-argument", "sans-sortie", "empreinte-en-argument", "abreviation"])
def test_ligne_de_commande_sans_defaut_ni_empreinte_en_argument(args, motif):
    p = _ligne_de_commande(*args)
    assert p.returncode == 2 and p.stdout == ""
    assert motif in p.stderr
