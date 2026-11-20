# -*- coding: utf-8 -*-
"""Essais de masque_style_cartes_v1.py — cartes SYNTHÉTIQUES, inventées ici ; aucune vraie carte.

Pour chaque garde : un cas sain et un artefact (R5).
Lancement : python3 -B -m pytest -q essais_masque_style_cartes_v1.py
"""
import copy
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masque_style_cartes_v1 as M  # noqa: E402

CHAMPS = ["titre", "mecanisme", "epreuve", "ce_qui_la_refuterait"]
SENTINELLE = "ESPECE-SENTINELLE-NE-PAS-LIRE"


def configuration(**k):
    c = {"champs": list(CHAMPS), "plafond": {"titre": 60, "mecanisme": 120, "epreuve": 120, "ce_qui_la_refuterait": 120},
         "formules": ["non vérifié"], "intertitres": ["pourquoi cela compte"],
         "seuil_formule_recitee": 0.5, "minimum_formule_recitee": 3, "hors_choix": []}
    c.update(k)
    return c


def fiches():
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
    return {i: {"contenu": c, "empreinte": "e-" + i, "meta": {"proposeur": SENTINELLE}} for i, c in base.items()}


def masquer(f=None, **k):
    conf = M.valider_configuration(configuration(**k))
    contenus = M.extraire_contenus(f or fiches(), conf["champs"], conf["hors_choix"])
    cartes, rapport = M.masquer(contenus, conf)
    M.verifier_sortie(cartes, conf, rapport["plafonds"])
    return cartes, rapport, conf


def textes(cartes):
    return {c["id"]: dict(c["champs"]) for c in cartes}


def test_cas_sain_ordre_fixe_gras_intertitres_formules():
    cartes, rapport, _ = masquer()
    t = textes(cartes)
    assert [c["id"] for c in cartes] == ["s-a", "s-b", "s-c", "s-d"]
    assert all([k for k, _ in c["champs"]] == CHAMPS for c in cartes)          # ordre des champs fixe
    assert t["s-a"]["titre"] == "Minuteur de dégel"                              # gras retiré
    assert t["s-a"]["mecanisme"] == "Un minuteur compte les cycles de dégel du banc de cuivre."   # intertitre retiré
    assert "non vérifié" not in t["s-a"]["epreuve"] and "Bras un : minuteur." in t["s-a"]["epreuve"]
    assert not t["s-a"]["epreuve"].startswith("-")                               # puces retirées
    assert t["s-a"]["ce_qui_la_refuterait"] == "le sablier suffit. Sinon couper le minuteur."     # étiquette en gras
    assert t["s-b"]["ce_qui_la_refuterait"] == "rien ne change. Le sablier seul fait aussi bien."  # intertitre de la configuration
    assert t["s-d"]["epreuve"] == "Deux bras, même eau. Lecture : écart de cycles."
    assert '"sablier double"' in t["s-b"]["epreuve"] or "sablier double" in t["s-b"]["epreuve"]
    assert "—" not in t["s-c"]["ce_qui_la_refuterait"]                           # typographie ramenée à une seule
    assert rapport["cartes"] == 4 and rapport["formules_de_la_configuration_retirees"] == 1
    assert rapport["intertitres_retires"] >= 2


def test_phrase_recitee_par_la_moitie_des_cartes_retiree():
    cartes, rapport, _ = masquer()
    t = textes(cartes)
    assert all("Le monde plante douze cycles" not in t[i]["epreuve"] for i in t)   # trois cartes sur quatre la récitent
    assert rapport["formules_recitees_distinctes"] == 1 and rapport["phrases_recitees_retirees"] == 3
    assert "On compare" in t["s-b"]["epreuve"]
    cartes2, rapport2, _ = masquer(seuil_formule_recitee=None)                     # cas sain : détection éteinte, dit
    assert any("Le monde plante douze cycles" in textes(cartes2)[i]["epreuve"] for i in ("s-a", "s-b", "s-c"))
    assert rapport2["formules_recitees_distinctes"] == 0
    # le rapport ne porte pas le texte d'une formule, seulement une empreinte
    assert "douze" not in json.dumps(rapport, ensure_ascii=False)


def test_plafond_par_champ_et_coupe_au_mot():
    cartes, rapport, _ = masquer()
    t = textes(cartes)
    assert len(t["s-b"]["mecanisme"]) <= 120 and not t["s-b"]["mecanisme"].endswith(" ")
    assert t["s-b"]["mecanisme"].split()[-1] in ("Deux", "sabliers", "se", "relaient", ";", "l'un", "mesure,", "l'autre", "repose.")
    assert rapport["champs_coupes_par_champ"]["mecanisme"] == 1
    assert M.plafonner("un deux trois", 7) == ("un deux", True)
    assert M.plafonner("un deux trois", 6) == ("un", True)
    assert M.plafonner("un deux", 50) == ("un deux", False)
    assert M.plafonner("abcdefgh", 3) == ("abc", True)


def test_plafond_a_la_mediane():
    cartes, rapport, _ = masquer(plafond="mediane")
    for k in CHAMPS:
        longueurs = sorted(len(dict(c["champs"])[k]) for c in cartes)
        assert longueurs[-1] <= rapport["plafonds"][k]
    assert rapport["champs_coupes_par_champ"]["mecanisme"] >= 1
    assert M.mediane_entiere([1, 9, 5]) == 5 and M.mediane_entiere([2, 5]) == 3 and M.mediane_entiere([0, 0]) == 1


def test_meta_jamais_lu_ni_ecrit():
    acces = []

    class Espion(dict):
        def __getitem__(self, k):
            acces.append(k)
            return dict.__getitem__(self, k)

        def __contains__(self, k):
            acces.append(k)
            return dict.__contains__(self, k)

        def get(self, k, d=None):
            acces.append(k)
            return dict.get(self, k, d)

        def items(self):
            acces.append("<parcours>")
            return dict.items(self)

        def values(self):
            acces.append("<parcours>")
            return dict.values(self)

        def keys(self):
            acces.append("<parcours>")
            return dict.keys(self)

        def __iter__(self):
            acces.append("<parcours>")
            return dict.__iter__(self)

    f = {i: Espion(rec) for i, rec in fiches().items()}
    cartes, rapport, _ = masquer(f)
    assert set(acces) == {"contenu"}
    sortie = json.dumps({"cartes": cartes, "rapport": rapport}, ensure_ascii=False)
    assert SENTINELLE not in sortie and "meta" not in sortie and "e-s-a" not in sortie


def test_carte_hors_du_choix_non_ouverte():
    f = fiches()
    f["s-d"] = {"meta": {"proposeur": SENTINELLE}}        # sans `contenu` : ne gêne pas, elle n'est pas ouverte
    cartes, _, _ = masquer(f, hors_choix=["s-d"])
    assert [c["id"] for c in cartes] == ["s-a", "s-b", "s-c"]
    with pytest.raises(M.Refus):
        masquer(fiches(), hors_choix=["inconnue"])


@pytest.mark.parametrize("mut", [
    lambda f: f["s-a"]["contenu"].update(champ_surprise="x"),       # champ hors de la configuration
    lambda f: f["s-a"]["contenu"].pop("epreuve"),                   # champ absent
    lambda f: f["s-a"]["contenu"].update(epreuve=["liste"]),        # champ qui n'est pas un texte
    lambda f: f["s-a"].pop("contenu"),
    lambda f: f["s-a"].update(contenu="texte"),
    lambda f: f["s-c"]["contenu"].update({k: "**  **" for k in CHAMPS}),   # carte vide après le masque
])
def test_cartes_refusees(mut):
    masquer(fiches())                                               # cas sain
    f = fiches()
    mut(f)
    with pytest.raises(M.Refus):
        masquer(f)


@pytest.mark.parametrize("cle,val", [
    ("champs", []), ("champs", ["titre", "titre"]), ("champs", ["titre", "meta"]), ("plafond", 100),
    ("plafond", {"titre": 60}), ("plafond", {"titre": 0, "mecanisme": 1, "epreuve": 1, "ce_qui_la_refuterait": 1}),
    ("formules", [""]), ("seuil_formule_recitee", 0), ("seuil_formule_recitee", 1.5),
    ("minimum_formule_recitee", 1), ("hors_choix", "s-a")])
def test_configuration_refusee(cle, val):
    M.valider_configuration(configuration())
    with pytest.raises(M.Refus):
        M.valider_configuration(configuration(**{cle: val}))
    c = configuration()
    c["reglage_cache"] = True
    with pytest.raises(M.Refus):
        M.valider_configuration(c)


def test_postcondition_cas_sain_et_artefacts():
    cartes, rapport, conf = masquer()
    assert M.verifier_sortie(cartes, conf, rapport["plafonds"]) is True

    def casse(mut):
        c = copy.deepcopy(cartes)
        mut(c)
        with pytest.raises(M.Refus):
            M.verifier_sortie(c, conf, rapport["plafonds"])
    casse(lambda c: c[0]["champs"].reverse())                              # ordre des champs
    casse(lambda c: c[0]["champs"][1].__setitem__(1, "x" * 500))           # plafond dépassé
    casse(lambda c: c[0]["champs"][1].__setitem__(1, "du **gras** resté"))
    casse(lambda c: c[0]["champs"][1].__setitem__(1, "# intertitre resté"))
    casse(lambda c: c[0]["champs"][1].__setitem__(1, "deux\nlignes"))
    casse(lambda c: c[0]["champs"][1].__setitem__(1, "résultat (Non  Vérifié) resté"))
    casse(lambda c: c[0].update(meta={"proposeur": "x"}))                  # clé de trop
    casse(lambda c: c.append(copy.deepcopy(c[0])))                         # doublon
    conf2 = dict(conf, hors_choix=["s-a"])
    with pytest.raises(M.Refus):
        M.verifier_sortie(cartes, conf2, rapport["plafonds"])


def test_formule_sous_une_autre_graphie_comptee_non_cachee():
    f = fiches()
    f["s-c"]["contenu"]["epreuve"] = "Résultat non-verifie. Le cadran est comparé au minuteur."
    cartes, rapport, _ = masquer(f)
    assert rapport["formules_restees_sous_une_autre_graphie"] == 1
    assert masquer(fiches())[1]["formules_restees_sous_une_autre_graphie"] == 0


def test_deux_styles_meme_fond_donnent_la_meme_carte():
    sobre = {"titre": "Niveau à bulle", "mecanisme": "Une bulle lit la pente du banc.",
             "epreuve": "Deux bras. La bulle est comparée au fil à plomb.", "ce_qui_la_refuterait": "Le fil suffit. Sinon couper la bulle."}
    charge = {"titre": "**Niveau à bulle**", "mecanisme": "### Mécanisme\n*Une bulle* lit la pente du banc.",
              "epreuve": "- Deux bras.\n- La bulle est comparée au fil à plomb.",
              "ce_qui_la_refuterait": "**Réfutation :** Le fil suffit. Sinon couper la bulle."}
    f = {"x1": {"contenu": sobre}, "x2": {"contenu": charge}}
    cartes, _, _ = masquer(f, seuil_formule_recitee=None)
    assert cartes[0]["champs"] == cartes[1]["champs"]


def _ecrire(tmp, nom, obj):
    p = os.path.join(str(tmp), nom)
    with open(p, "w", encoding="utf-8") as fo:
        json.dump(obj, fo, ensure_ascii=False)
    with open(p, "rb") as fo:
        return p, M.sha_octets(fo.read())


def test_commande_cas_sain_empreinte_et_refus_d_ecraser(tmp_path, capsys):
    c = _ecrire(tmp_path, "cartes.json", fiches())
    k = _ecrire(tmp_path, "conf.json", configuration())
    s = os.path.join(str(tmp_path), "masquees.json")
    assert M.main(["--cartes", *c, "--configuration", *k, "--sortie", s]) == 0
    with open(s, encoding="utf-8") as fo:
        d = json.load(fo)
    assert d["piece"] == M.VERSION and d["ordre_des_champs"] == CHAMPS and SENTINELLE not in json.dumps(d)
    with open(s + ".sha256") as fo, open(s, "rb") as fb:
        assert fo.read().split()[0] == M.sha_octets(fb.read())
    assert M.main(["--cartes", *c, "--configuration", *k, "--sortie", s]) == 2          # on n'écrase jamais
    s2 = os.path.join(str(tmp_path), "autre.json")
    assert M.main(["--cartes", c[0], "0" * 64, "--configuration", *k, "--sortie", s2]) == 2
    assert M.main(["--cartes", *c, "--configuration", k[0], "abc", "--sortie", s2]) == 2
    assert M.main(["--cartes", os.path.join(str(tmp_path), "absent.json"), c[1], "--configuration", *k, "--sortie", s2]) == 2
    assert not os.path.exists(s2) and not os.path.exists(s2 + ".sha256")
    assert "REFUS" in capsys.readouterr().err
