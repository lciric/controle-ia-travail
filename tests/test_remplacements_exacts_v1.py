import pytest

from controle_ia.remplacements_exacts_v1 import RefusRemplacement, appliquer, lire_blocs, main

SOURCE = "Titre\nLigne A une seule fois.\nLigne B.\nLigne B.\nFin.\n"


def blocs(*paires):
    morceaux = ["Préambule ignoré."]
    for k, (a, n) in enumerate(paires, start=1):
        morceaux += [f"<<<ANCIEN {k}", a, f"===NOUVEAU {k}", n, f">>>FIN {k}"]
    return "\n".join(morceaux) + "\n"


def test_cas_sain_deux_blocs():
    b = lire_blocs(blocs(("Ligne A une seule fois.", "Ligne A changée."), ("Fin.", "Fin, version 2.")))
    assert appliquer(SOURCE, b) == "Titre\nLigne A changée.\nLigne B.\nLigne B.\nFin, version 2.\n"


def test_nouveau_vide_supprime():
    b = lire_blocs("<<<ANCIEN 1\nTitre\n===NOUVEAU 1\n>>>FIN 1\n")
    assert appliquer(SOURCE, b).startswith("\nLigne A")


def test_refus_ancien_absent():
    with pytest.raises(RefusRemplacement, match="0 fois"):
        appliquer(SOURCE, lire_blocs(blocs(("Ligne Z.", "x"))))


def test_refus_ancien_double():
    with pytest.raises(RefusRemplacement, match="2 fois"):
        appliquer(SOURCE, lire_blocs(blocs(("Ligne B.", "x"))))


def test_refus_chevauchement():
    with pytest.raises(RefusRemplacement, match="chevauchent"):
        appliquer(SOURCE, lire_blocs(blocs(("Ligne A une seule", "x"), ("une seule fois.", "y"))))


def test_refus_aucun_bloc():
    with pytest.raises(RefusRemplacement, match="aucun bloc"):
        lire_blocs("rien ici\n")


def test_refus_numeros_non_consecutifs():
    t = "<<<ANCIEN 2\nFin.\n===NOUVEAU 2\nx\n>>>FIN 2\n"
    with pytest.raises(RefusRemplacement, match="consécutifs"):
        lire_blocs(t)


def test_refus_bloc_non_ferme():
    with pytest.raises(RefusRemplacement, match="FIN 1"):
        lire_blocs("<<<ANCIEN 1\nFin.\n===NOUVEAU 1\nx\n")


def test_refus_ancien_vide():
    with pytest.raises(RefusRemplacement, match="vide"):
        lire_blocs("<<<ANCIEN 1\n===NOUVEAU 1\nx\n>>>FIN 1\n")


def test_refus_marqueur_orphelin():
    with pytest.raises(RefusRemplacement, match="hors d'ordre"):
        lire_blocs("===NOUVEAU 1\nx\n")


def test_nouveau_texte_jamais_repris():
    # le nouveau texte du bloc 1 contient l'ancien du bloc 2 : positions prises sur la source d'origine
    b = lire_blocs(blocs(("Ligne A une seule fois.", "Fin."), ("Fin.", "FIN")))
    assert appliquer(SOURCE, b) == "Titre\nFin.\nLigne B.\nLigne B.\nFIN\n"


def test_main_refuse_sortie_existante(tmp_path):
    s = tmp_path / "s.md"; s.write_text(SOURCE, encoding="utf-8")
    r = tmp_path / "r.md"; r.write_text(blocs(("Fin.", "x")), encoding="utf-8")
    o = tmp_path / "o.md"; o.write_text("déjà là", encoding="utf-8")
    assert main([str(s), str(r), str(o)]) == 3
    assert o.read_text(encoding="utf-8") == "déjà là"


def test_main_refus_n_ecrit_rien(tmp_path):
    s = tmp_path / "s.md"; s.write_text(SOURCE, encoding="utf-8")
    r = tmp_path / "r.md"; r.write_text(blocs(("Ligne B.", "x")), encoding="utf-8")
    o = tmp_path / "o.md"
    assert main([str(s), str(r), str(o)]) == 4
    assert not o.exists()


def test_main_cas_sain(tmp_path):
    s = tmp_path / "s.md"; s.write_text(SOURCE, encoding="utf-8")
    r = tmp_path / "r.md"; r.write_text(blocs(("Fin.", "Fin 2.")), encoding="utf-8")
    o = tmp_path / "o.md"
    assert main([str(s), str(r), str(o)]) == 0
    assert o.read_text(encoding="utf-8").endswith("Fin 2.\n")
