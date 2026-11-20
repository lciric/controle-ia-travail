# -*- coding: utf-8 -*-
"""Essais de masque_style_cartes_v2.py — cartes SYNTHÉTIQUES, inventées ici ; aucune vraie carte.

Chaque garde neuve est essayée sur un cas sain et sur un artefact (R5). Le masque v1 est chargé
depuis une copie posée à côté, vérifiée à son empreinte, pour comparer les sorties.
Lancement, hors du dépôt : python3 -B -m pytest -q -p no:cacheprovider essais_masque_style_cartes_v2.py
"""
import copy
import json
import os
import sys

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import masque_style_cartes_v1 as M1  # noqa: E402
import masque_style_cartes_v2 as M2  # noqa: E402

SHA_V1 = "07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e"
CHAMPS = ["titre", "mecanisme", "epreuve", "ce_qui_la_refuterait"]
SENTINELLE_META = "ESPECE-SENTINELLE-NE-PAS-LIRE"
# valeurs semées dans les clés retirées : aucune ne doit sortir, ni dans un fichier ni à l'écran
SEMIS = {"_": "SEMIS-SOULIGNE-7Q4", "cout_note": "SEMIS-COUT-NOTE-2K9", "epreuve_hors_ligne": "SEMIS-EPREUVE-HL-5X1"}
RETIREES = {"_": 2, "cout_note": 1, "epreuve_hors_ligne": 1}


_ABSENTE = object()


def configuration(retirees=_ABSENTE, **k):
    c = {"champs": list(CHAMPS), "plafond": {"titre": 60, "mecanisme": 120, "epreuve": 120, "ce_qui_la_refuterait": 120},
         "formules": ["non vérifié"], "intertitres": ["pourquoi cela compte"],
         "seuil_formule_recitee": 0.5, "minimum_formule_recitee": 3, "hors_choix": []}
    c.update(k)
    if retirees is not _ABSENTE:
        c[M2.CLE_RETIREES] = retirees
    return c


def fiches():
    """Les cartes synthétiques des essais v1, sans clé hors des champs."""
    base = {
        "s-a": {"titre": "**Minuteur de dégel**", "mecanisme": "## Idée\nUn minuteur compte les cycles de dégel du banc de cuivre.",
                "epreuve": "- Bras un : minuteur.\n- Bras deux : sablier (non vérifié).\nLe monde plante douze cycles.",
                "ce_qui_la_refuterait": "**Pourquoi cela compte :** le sablier suffit. Sinon couper le minuteur."},
        "s-b": {"titre": "Sablier double", "mecanisme": "Deux sabliers se relaient ; l'un mesure, l'autre repose. " * 6,
                "epreuve": "Le monde plante douze cycles. On compare « sablier double » au sablier seul.",
                "ce_qui_la_refuterait": "Pourquoi cela compte : rien ne change. Le sablier seul fait aussi bien."},
        "s-c": {"titre": "Cadran solaire", "mecanisme": "Un cadran lit l'ombre du banc de cuivre.",
                "epreuve": "Le monde plante douze cycles. Le cadran est comparé au minuteur.",
                "ce_qui_la_refuterait": "Le cadran ne bat pas le minuteur — garder le minuteur."},
        "s-d": {"titre": "Clepsydre", "mecanisme": "Une clepsydre goutte dans le banc de cuivre.",
                "epreuve": "Deux bras, même eau. __Lecture__ : écart de cycles.",
                "ce_qui_la_refuterait": "La clepsydre gèle. Retirer la clepsydre."},
    }
    return {i: {"contenu": c, "empreinte": "e-" + i, "meta": {"proposeur": SENTINELLE_META}} for i, c in base.items()}


def fiches_porteuses():
    """Mêmes cartes ; `_` sur deux cartes, `cout_note` et `epreuve_hors_ligne` sur une chacune.
    Les valeurs semées ne sont pas toutes des textes : le masque ne doit pas les regarder."""
    f = fiches()
    f["s-a"]["contenu"]["_"] = SEMIS["_"]
    f["s-c"]["contenu"]["_"] = {"note": SEMIS["_"]}
    f["s-b"]["contenu"]["cout_note"] = SEMIS["cout_note"]
    f["s-c"]["contenu"]["epreuve_hors_ligne"] = [SEMIS["epreuve_hors_ligne"], 3]
    return f


def masquer(M, f, conf):
    conf = M.valider_configuration(conf)
    if M is M2:
        contenus = M.extraire_contenus(f, conf["champs"], conf["hors_choix"], conf.get(M2.CLE_RETIREES))
    else:
        contenus = M.extraire_contenus(f, conf["champs"], conf["hors_choix"])
    cartes, rapport = M.masquer(contenus, conf)
    M.verifier_sortie(cartes, conf, rapport["plafonds"])
    return cartes, rapport


def _ecrire(tmp, nom, obj):
    p = os.path.join(str(tmp), nom)
    with open(p, "w", encoding="utf-8") as fo:
        json.dump(obj, fo, ensure_ascii=False)
    with open(p, "rb") as fo:
        return p, M2.sha_octets(fo.read())


def _lire(p):
    with open(p, "rb") as fo:
        return fo.read()


def _sha_fichier(p):
    return M2.sha_octets(_lire(p))


def _aucun_semis(texte):
    return all(v not in texte for v in SEMIS.values())


# ----------------------------------------------------------------------------- v1 à côté

def test_copie_du_v1_a_son_empreinte():
    assert _sha_fichier(os.path.join(ICI, "masque_style_cartes_v1.py")) == SHA_V1
    assert M1.VERSION == "masque_style_cartes_v1" and M2.VERSION == "masque_style_cartes_v2"


# ----------------------------------------------------------------------------- sans la huitième clé : le v1

@pytest.mark.parametrize("reglages", [{}, {"plafond": "mediane"}, {"seuil_formule_recitee": None},
                                      {"hors_choix": ["s-d"]}, {"plafond": "mediane", "seuil_formule_recitee": 0.25}])
def test_sans_huitieme_cle_sortie_egale_au_v1_a_l_octet(tmp_path, capsys, reglages):
    c = _ecrire(tmp_path, "cartes.json", fiches())
    k = _ecrire(tmp_path, "conf.json", configuration(**reglages))
    s1, s2 = os.path.join(str(tmp_path), "v1.json"), os.path.join(str(tmp_path), "v2.json")
    assert M1.main(["--cartes", *c, "--configuration", *k, "--sortie", s1]) == 0
    e1 = capsys.readouterr()
    assert M2.main(["--cartes", *c, "--configuration", *k, "--sortie", s2]) == 0
    e2 = capsys.readouterr()
    o1, o2 = _lire(s1), _lire(s2)
    # deux valeurs diffèrent par nature : le nom de la pièce et l'empreinte du programme ; rien d'autre
    sha_v2 = _sha_fichier(os.path.join(ICI, "masque_style_cartes_v2.py"))
    assert o2.count(b'"piece": "masque_style_cartes_v2"') == 1 and o2.count(sha_v2.encode()) == 1
    ramene = o2.replace(b'"piece": "masque_style_cartes_v2"', b'"piece": "masque_style_cartes_v1"').replace(
        sha_v2.encode(), SHA_V1.encode())
    assert ramene == o1
    d1, d2 = json.loads(o1), json.loads(o2)
    assert d2["en_tete"] == d1["en_tete"] == M1.EN_TETE                     # deux lignes, comme le v1
    assert d2["cartes"] == d1["cartes"] and d2["rapport"] == d1["rapport"]
    assert e1.out.splitlines()[0] == e2.out.splitlines()[0]                # rapport à l'écran identique
    assert e1.err == e2.err == ""


@pytest.mark.parametrize("mut", [
    lambda f: f["s-a"]["contenu"].update(champ_surprise="x"),
    lambda f: f["s-a"]["contenu"].pop("epreuve"),
    lambda f: f["s-a"]["contenu"].update(epreuve=["liste"]),
    lambda f: f["s-a"].pop("contenu"),
    lambda f: f["s-a"].update(contenu="texte"),
    lambda f: f["s-c"]["contenu"].update({k: "**  **" for k in CHAMPS}),
    lambda f: f["s-a"]["contenu"].update(_="sans huitième clé, `_` reste un refus"),
])
def test_sans_huitieme_cle_memes_refus_que_le_v1(mut):
    f = fiches()
    mut(f)
    with pytest.raises(M1.Refus) as r1:
        masquer(M1, copy.deepcopy(f), configuration())
    with pytest.raises(M2.Refus) as r2:
        masquer(M2, copy.deepcopy(f), configuration())
    assert str(r1.value) == str(r2.value)


@pytest.mark.parametrize("cle,val", [
    ("champs", []), ("champs", ["titre", "titre"]), ("champs", ["titre", "meta"]), ("plafond", 100),
    ("plafond", {"titre": 60}), ("formules", [""]), ("seuil_formule_recitee", 0), ("minimum_formule_recitee", 1),
    ("hors_choix", "s-a"), ("reglage_cache", True)])
def test_sans_huitieme_cle_memes_refus_de_configuration_que_le_v1(cle, val):
    c = configuration(**{cle: val})
    with pytest.raises(M1.Refus) as r1:
        M1.valider_configuration(copy.deepcopy(c))
    with pytest.raises(M2.Refus) as r2:
        M2.valider_configuration(copy.deepcopy(c))
    assert str(r1.value) == str(r2.value)


# ----------------------------------------------------------------------------- clé retirée, bon nombre

def test_cles_retirees_sur_le_bon_nombre_de_cartes(tmp_path, capsys):
    c = _ecrire(tmp_path, "cartes.json", fiches_porteuses())
    k = _ecrire(tmp_path, "conf.json", configuration(retirees=dict(RETIREES)))
    s = os.path.join(str(tmp_path), "masquees.json")
    assert M2.main(["--cartes", *c, "--configuration", *k, "--sortie", s]) == 0
    ecran = capsys.readouterr()
    d = json.loads(_lire(s))
    # les cartes rendues sont celles que le v1 rend sur les mêmes cartes privées des trois clés
    attendu, rapport_attendu = masquer(M1, fiches(), configuration())
    assert d["cartes"] == attendu and d["rapport"] == rapport_attendu
    assert all([n for n, _ in carte["champs"]] == CHAMPS for carte in d["cartes"])
    assert d["piece"] == "masque_style_cartes_v2" and d["ordre_des_champs"] == CHAMPS
    assert set(d) == {"piece", "en_tete", "ordre_des_champs", "rapport", "empreintes", "cartes"}   # forme du v1
    assert _aucun_semis(_lire(s).decode("utf-8")) and _aucun_semis(ecran.out + ecran.err)
    assert SENTINELLE_META not in _lire(s).decode("utf-8")


def test_compte_par_cle_a_l_en_tete_avec_l_empreinte_de_la_configuration(tmp_path, capsys):
    c = _ecrire(tmp_path, "cartes.json", fiches_porteuses())
    k = _ecrire(tmp_path, "conf.json", configuration(retirees=dict(RETIREES)))
    s = os.path.join(str(tmp_path), "masquees.json")
    assert M2.main(["--cartes", *c, "--configuration", *k, "--sortie", s]) == 0
    capsys.readouterr()
    d = json.loads(_lire(s))
    assert d["en_tete"][:2] == M2.EN_TETE and len(d["en_tete"]) == 3
    assert d["en_tete"][2] == (
        "Clés de `contenu` hors des champs, retirées sans que leur valeur soit lue ni écrite ; nombre de "
        "cartes porteuses par clé (jamais par carte), vérifié égal à l'attendu : "
        '"_" : 2 ; "cout_note" : 1 ; "epreuve_hors_ligne" : 1. '
        f"Configuration : sha256 {k[1]}.")
    assert d["empreintes"]["configuration"] == k[1]
    assert not any(i in d["en_tete"][2] for i in ("s-a", "s-b", "s-c", "s-d"))   # aucun identifiant de carte
    with open(s + ".sha256") as fo:
        assert fo.read().split()[0] == _sha_fichier(s)


def test_carte_hors_du_choix_non_comptee():
    f = fiches_porteuses()
    # s-a porte `_` ; hors du choix, elle n'est pas ouverte : `_` n'est plus porté que par une carte ouverte
    with pytest.raises(M2.Refus):
        masquer(M2, copy.deepcopy(f), configuration(retirees=dict(RETIREES), hors_choix=["s-a"]))
    cartes, _ = masquer(M2, copy.deepcopy(f), configuration(retirees=dict(RETIREES, _=1), hors_choix=["s-a"]))
    assert [x["id"] for x in cartes] == ["s-b", "s-c", "s-d"]


# ----------------------------------------------------------------------------- garde du nombre attendu

@pytest.mark.parametrize("attendu,raison", [
    (dict(RETIREES, _=3), "une carte de plus attendue que portée"),
    (dict(RETIREES, _=1), "une carte de moins attendue que portée"),
    (dict(RETIREES, cout_note=2), "en plus, sur une autre clé"),
    (dict(RETIREES, nom_absent=1), "nom attendu porté par aucune carte"),
])
def test_nombre_faux_refuse(tmp_path, capsys, attendu, raison):
    masquer(M2, fiches_porteuses(), configuration(retirees=dict(RETIREES)))           # cas sain
    with pytest.raises(M2.Refus) as r:
        masquer(M2, fiches_porteuses(), configuration(retirees=attendu))
    assert "nombre de cartes porteuses" in str(r.value) and _aucun_semis(str(r.value)), raison
    c = _ecrire(tmp_path, "cartes.json", fiches_porteuses())
    k = _ecrire(tmp_path, "conf.json", configuration(retirees=attendu))
    s = os.path.join(str(tmp_path), "masquees.json")
    assert M2.main(["--cartes", *c, "--configuration", *k, "--sortie", s]) == 2
    ecran = capsys.readouterr()
    assert "REFUS" in ecran.err and _aucun_semis(ecran.out + ecran.err)
    assert not os.path.exists(s) and not os.path.exists(s + ".sha256")


def test_carte_en_plus_porteuse_refusee():
    f = fiches_porteuses()
    f["s-d"]["contenu"]["cout_note"] = SEMIS["cout_note"]                  # deux cartes, une attendue
    masquer(M2, fiches_porteuses(), configuration(retirees=dict(RETIREES)))
    with pytest.raises(M2.Refus) as r:
        masquer(M2, f, configuration(retirees=dict(RETIREES)))
    assert "'cout_note' : 2 au lieu de 1" in str(r.value)


def test_carte_en_moins_porteuse_refusee():
    f = fiches_porteuses()
    del f["s-c"]["contenu"]["_"]                                            # une carte, deux attendues
    with pytest.raises(M2.Refus) as r:
        masquer(M2, f, configuration(retirees=dict(RETIREES)))
    assert "'_' : 1 au lieu de 2" in str(r.value)


# ----------------------------------------------------------------------------- toute autre clé hors champs

def test_autre_cle_hors_champs_reste_un_refus(tmp_path, capsys):
    masquer(M2, fiches_porteuses(), configuration(retirees=dict(RETIREES)))           # cas sain
    f = fiches_porteuses()
    f["s-d"]["contenu"]["champ_surprise"] = "x"
    with pytest.raises(M2.Refus) as r:
        masquer(M2, f, configuration(retirees=dict(RETIREES)))
    assert "hors de la configuration (1)" in str(r.value)
    c = _ecrire(tmp_path, "cartes.json", f)
    k = _ecrire(tmp_path, "conf.json", configuration(retirees=dict(RETIREES)))
    s = os.path.join(str(tmp_path), "masquees.json")
    assert M2.main(["--cartes", *c, "--configuration", *k, "--sortie", s]) == 2
    ecran = capsys.readouterr()
    assert _aucun_semis(ecran.out + ecran.err) and not os.path.exists(s)


def test_champ_manquant_ou_non_texte_reste_un_refus_avec_la_huitieme_cle():
    for mut in (lambda f: f["s-a"]["contenu"].pop("epreuve"), lambda f: f["s-a"]["contenu"].update(epreuve=["liste"])):
        f = fiches_porteuses()
        mut(f)
        with pytest.raises(M2.Refus):
            masquer(M2, f, configuration(retirees=dict(RETIREES)))


# ----------------------------------------------------------------------------- validation de la huitième clé

@pytest.mark.parametrize("valeur,raison", [
    ({"titre": 1}, "nom retiré qui est aussi un champ"),
    ({"_": 2, "mecanisme": 1}, "un des noms est un champ"),
    ({"meta": 1}, "`meta` nommé"),
    ({"empreinte": 1}, "`empreinte` nommé"),
    ({"_": 0}, "valeur 0"),
    ({"_": -1}, "valeur négative"),
    ({"_": 1.5}, "valeur non entière"),
    ({"_": 2.0}, "valeur flottante entière"),
    ({"_": True}, "booléen"),
    ({"_": "2"}, "texte"),
    ({"_": None}, "null"),
    ({"": 1}, "nom vide"),
    ({3: 1}, "nom qui n'est pas un texte"),
    ({}, "objet vide"),
    (["_"], "liste au lieu d'un objet"),
    (None, "null au lieu d'un objet"),
])
def test_huitieme_cle_mal_formee_refusee(valeur, raison):
    M2.valider_configuration(configuration(retirees=dict(RETIREES)))                  # cas sain
    M2.valider_configuration(configuration())                                          # cas sain sans la clé
    with pytest.raises(M2.Refus):
        M2.valider_configuration(configuration(retirees=valeur))
    assert raison


def test_toute_autre_cle_neuve_reste_un_refus():
    c = configuration(retirees=dict(RETIREES))
    M2.valider_configuration(copy.deepcopy(c))
    c["reglage_cache"] = True
    with pytest.raises(M2.Refus):
        M2.valider_configuration(c)
    c = configuration()
    c["cles_hors_champs_retirée"] = {"_": 2}                                   # nom voisin, non reconnu
    with pytest.raises(M2.Refus):
        M2.valider_configuration(c)


def test_configuration_a_v2_reelle_acceptee_par_la_validation():
    """La configuration A v2 écrite par le rédacteur (pièce de travail, non une carte) passe la validation."""
    a_v2 = {"champs": ["titre", "axe", "module_change", "mecanisme", "plus_proche_voisin", "ce_qui_distingue",
                       "epreuve_monde_plante", "cout", "ce_qui_la_refuterait", "limites"],
            "plafond": "mediane", "formules": ["non vérifié"], "intertitres": [], "seuil_formule_recitee": 0.2,
            "minimum_formule_recitee": 3, "hors_choix": [],
            "cles_hors_champs_retirees": {"_": 2, "cout_note": 1, "epreuve_hors_ligne": 1}}
    assert M2.valider_configuration(copy.deepcopy(a_v2)) == a_v2
    with pytest.raises(M1.Refus):
        M1.valider_configuration(copy.deepcopy(a_v2))


# ----------------------------------------------------------------------------- aucune valeur retirée lue

class EspionContenu(dict):
    """`contenu` qui note toute lecture d'une valeur ; le parcours des seuls noms est permis."""

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.lues = []

    def __getitem__(self, k):
        self.lues.append(k)
        return dict.__getitem__(self, k)

    def get(self, k, d=None):
        self.lues.append(k)
        return dict.get(self, k, d)

    def values(self):
        self.lues.append("<valeurs>")
        return dict.values(self)

    def items(self):
        self.lues.append("<valeurs>")
        return dict.items(self)

    def pop(self, *a):
        self.lues.append("<pop>")
        return dict.pop(self, *a)

    def copy(self):
        self.lues.append("<copie>")
        return dict.copy(self)


def test_aucune_valeur_d_une_cle_retiree_n_est_lue():
    f = fiches_porteuses()
    espions = {}
    for i in f:
        espions[i] = EspionContenu(f[i]["contenu"])
        f[i]["contenu"] = espions[i]
    cartes, rapport = masquer(M2, f, configuration(retirees=dict(RETIREES)))
    lues = [k for e in espions.values() for k in e.lues]
    assert not set(lues) & set(RETIREES), "une valeur retirée a été lue"
    assert "<valeurs>" not in lues and "<pop>" not in lues and "<copie>" not in lues
    assert set(lues) == set(CHAMPS)
    for i, e in espions.items():                                    # le fichier d'entrée n'est pas modifié
        assert all(k in e for k in fiches_porteuses()[i]["contenu"])
    assert _aucun_semis(json.dumps({"cartes": cartes, "rapport": rapport}, ensure_ascii=False))


def test_aucune_valeur_retiree_dans_la_sortie_ni_a_l_ecran(tmp_path, capsys):
    c = _ecrire(tmp_path, "cartes.json", fiches_porteuses())
    assert not _aucun_semis(_lire(c[0]).decode("utf-8"))           # l'entrée porte bien les semis
    k = _ecrire(tmp_path, "conf.json", configuration(retirees=dict(RETIREES)))
    s = os.path.join(str(tmp_path), "masquees.json")
    assert M2.main(["--cartes", *c, "--configuration", *k, "--sortie", s]) == 0
    ecran = capsys.readouterr()
    assert _aucun_semis(_lire(s).decode("utf-8")) and _aucun_semis(_lire(s + ".sha256").decode("utf-8"))
    assert _aucun_semis(ecran.out) and ecran.err == ""


# ----------------------------------------------------------------------------- refus d'écraser, inchangé

def test_commande_refus_d_ecraser_et_empreintes_inchanges(tmp_path, capsys):
    c = _ecrire(tmp_path, "cartes.json", fiches_porteuses())
    k = _ecrire(tmp_path, "conf.json", configuration(retirees=dict(RETIREES)))
    s = os.path.join(str(tmp_path), "masquees.json")
    assert M2.main(["--cartes", *c, "--configuration", *k, "--sortie", s]) == 0
    assert M2.main(["--cartes", *c, "--configuration", *k, "--sortie", s]) == 2
    s2 = os.path.join(str(tmp_path), "autre.json")
    assert M2.main(["--cartes", c[0], "0" * 64, "--configuration", *k, "--sortie", s2]) == 2
    assert M2.main(["--cartes", *c, "--configuration", k[0], "0" * 64, "--sortie", s2]) == 2
    assert not os.path.exists(s2) and not os.path.exists(s2 + ".sha256")
    ecran = capsys.readouterr()
    assert "REFUS" in ecran.err and _aucun_semis(ecran.out + ecran.err)
