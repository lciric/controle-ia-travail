import json
import unicodedata

import pytest

from controle_ia.remplacements_exacts_v2 import RefusRemplacement, appliquer, lire_blocs, main, remettre_marques

SOURCE = "Titre\nLigne A une seule fois.\nLigne B.\nLigne B.\nFin.\n"


def blocs(*paires, final="\n"):
    morceaux = ["Préambule ignoré."]
    for k, (a, n) in enumerate(paires, start=1):
        morceaux += [f"<<<ANCIEN {k}", a, f"===NOUVEAU {k}", n, f">>>FIN {k}"]
    return "\n".join(morceaux) + final


# --- cas sains ---

def test_cas_sain_deux_blocs():
    b = lire_blocs(blocs(("Ligne A une seule fois.", "Ligne A changée."), ("Fin.", "Fin, version 2.")))
    assert appliquer(SOURCE, b) == "Titre\nLigne A changée.\nLigne B.\nLigne B.\nFin, version 2.\n"


def test_nouveau_sans_ligne_supprime():
    b = lire_blocs("<<<ANCIEN 1\nTitre\n===NOUVEAU 1\n>>>FIN 1\n")
    assert appliquer(SOURCE, b).startswith("\nLigne A")


def test_ordre_inverse_des_blocs():
    b = lire_blocs(blocs(("Fin.", "F."), ("Titre", "T")))
    assert appliquer(SOURCE, b) == "T\nLigne A une seule fois.\nLigne B.\nLigne B.\nF.\n"


def test_blocs_adjacents_acceptes():
    b = lire_blocs(blocs(("Titre", "T"), ("\nLigne A", "|A")))
    assert appliquer(SOURCE, b).startswith("T|A une seule")


def test_nouveau_texte_jamais_repris():
    b = lire_blocs(blocs(("Ligne A une seule fois.", "Fin."), ("Fin.", "FIN")))
    assert appliquer(SOURCE, b) == "Titre\nFin.\nLigne B.\nLigne B.\nFIN\n"


def test_liste_sans_saut_final():
    b = lire_blocs(blocs(("Fin.", "F."), final=""))
    assert appliquer(SOURCE, b).endswith("F.\n")


def test_deux_lignes_vides_valent_un_saut():
    b = lire_blocs("<<<ANCIEN 1\nFin.\n\n===NOUVEAU 1\nF.\n\n>>>FIN 1\n")
    assert appliquer(SOURCE, b).endswith("F.\n")


# --- artefacts : refus ---

def test_refus_ancien_absent():
    with pytest.raises(RefusRemplacement, match="0 fois"):
        appliquer(SOURCE, lire_blocs(blocs(("Ligne Z.", "x"))))


def test_refus_ancien_double():
    with pytest.raises(RefusRemplacement, match="2 fois"):
        appliquer(SOURCE, lire_blocs(blocs(("Ligne B.", "x"))))


def test_refus_occurrences_qui_se_chevauchent():
    with pytest.raises(RefusRemplacement, match="2 fois"):
        appliquer("B\nB\nB", lire_blocs(blocs(("B\nB", "x"))))
    with pytest.raises(RefusRemplacement, match="2 fois"):
        appliquer("xaaay", lire_blocs(blocs(("aa", "x"))))


def test_refus_chevauchement_entre_blocs():
    with pytest.raises(RefusRemplacement, match="chevauchent"):
        appliquer(SOURCE, lire_blocs(blocs(("Ligne A une seule", "x"), ("une seule fois.", "y"))))


def test_refus_deux_blocs_meme_ancien():
    with pytest.raises(RefusRemplacement, match="chevauchent"):
        appliquer(SOURCE, lire_blocs(blocs(("Fin.", "x"), ("Fin.", "y"))))


def test_refus_aucun_bloc():
    with pytest.raises(RefusRemplacement, match="aucun bloc"):
        lire_blocs("rien ici\n")


def test_refus_numeros_non_consecutifs_ou_doubles():
    with pytest.raises(RefusRemplacement, match="consécutifs"):
        lire_blocs("<<<ANCIEN 2\nFin.\n===NOUVEAU 2\nx\n>>>FIN 2\n")
    t = "<<<ANCIEN 1\nFin.\n===NOUVEAU 1\nx\n>>>FIN 1\n<<<ANCIEN 1\nTitre\n===NOUVEAU 1\ny\n>>>FIN 1\n"
    with pytest.raises(RefusRemplacement, match="consécutifs"):
        lire_blocs(t)


def test_refus_numeros_non_ascii_ou_zero_de_tete():
    with pytest.raises(RefusRemplacement, match="hors d'ordre"):
        lire_blocs("<<<ANCIEN ١\nFin.\n===NOUVEAU 1\nx\n>>>FIN 1\n")
    with pytest.raises(RefusRemplacement, match="inattendu"):
        lire_blocs("<<<ANCIEN 1\nFin.\n===NOUVEAU 1\nx\n>>>FIN 01\n")


def test_refus_marqueur_mal_numerote():
    with pytest.raises(RefusRemplacement, match="NOUVEAU 1"):
        lire_blocs("<<<ANCIEN 1\nFin.\n===NOUVEAU 2\nx\n>>>FIN 1\n")


def test_refus_bloc_non_ferme():
    with pytest.raises(RefusRemplacement, match="FIN 1"):
        lire_blocs("<<<ANCIEN 1\nFin.\n===NOUVEAU 1\nx\n")


def test_refus_ancien_vide_et_ancien_egal_nouveau():
    with pytest.raises(RefusRemplacement, match="vide"):
        lire_blocs("<<<ANCIEN 1\n===NOUVEAU 1\nx\n>>>FIN 1\n")
    with pytest.raises(RefusRemplacement, match="égal"):
        lire_blocs(blocs(("Fin.", "Fin.")))


def test_refus_marqueurs_orphelins():
    with pytest.raises(RefusRemplacement, match="hors d'ordre"):
        lire_blocs("===NOUVEAU 1\nx\n")
    with pytest.raises(RefusRemplacement, match="hors d'ordre"):
        lire_blocs(">>>FIN 1\n")


def test_refus_ligne_de_marqueur_dans_un_bloc():
    with pytest.raises(RefusRemplacement, match="inattendu"):
        lire_blocs("<<<ANCIEN 1\nFin.\n>>>FIN 1\n===NOUVEAU 1\nx\n>>>FIN 1\n")


def test_refus_retour_chariot():
    with pytest.raises(RefusRemplacement, match="retour chariot"):
        appliquer("a\r\nb\r\n", lire_blocs(blocs(("b", "B"))))
    with pytest.raises(RefusRemplacement, match="retour chariot"):
        lire_blocs(blocs(("Fin.", "x")).replace("\n", "\r\n"))


def test_refus_bom_dans_la_liste():
    with pytest.raises(RefusRemplacement, match="BOM"):
        lire_blocs("﻿" + blocs(("Fin.", "x")))


def test_refus_non_nfc():
    nfd = unicodedata.normalize("NFD", "un café\n")
    with pytest.raises(RefusRemplacement, match="NFC"):
        appliquer(nfd, lire_blocs(blocs(("un", "deux"))))
    with pytest.raises(RefusRemplacement, match="NFC"):
        lire_blocs(blocs((unicodedata.normalize("NFD", "café"), "thé")))


def test_refus_coupe_un_caractere_combinant():
    # source NFC qui garde un combinant isolé après une lettre sans forme composée
    source = "q́ fin\n"
    assert unicodedata.is_normalized("NFC", source)
    with pytest.raises(RefusRemplacement, match="combinant"):
        appliquer(source, lire_blocs(blocs(("q", "z"))))


def test_marques_remises_en_clair():
    table = {"⟦D⟧": "Nom", "⟦S1⟧": "session_x"}
    assert remettre_marques("de ⟦D⟧ (⟦S1⟧)", table) == "de Nom (session_x)"
    with pytest.raises(RefusRemplacement, match="restante"):
        remettre_marques("⟦S2⟧", table)


# --- main ---

def _ecrire(p, texte):
    p.write_bytes(texte.encode("utf-8"))
    return str(p)


def test_main_cas_sain_octets_conserves(tmp_path):
    s = _ecrire(tmp_path / "s.md", "Titre\nFin.")
    r = _ecrire(tmp_path / "r.md", blocs(("Titre", "T")))
    o = tmp_path / "o.md"
    assert main([s, r, str(o)]) == 0
    assert o.read_bytes() == b"T\nFin."
    assert not [p for p in tmp_path.iterdir() if p.name.endswith(".tmp")]


def test_main_avec_marques(tmp_path):
    s = _ecrire(tmp_path / "s.md", "auteur : session_abc.\n")
    r = _ecrire(tmp_path / "r.md", blocs(("auteur : ⟦S1⟧.", "auteur : ⟦S1⟧, revu.")))
    t = _ecrire(tmp_path / "t.json", json.dumps({"marques": {"⟦S1⟧": "session_abc"}}))
    o = tmp_path / "o.md"
    assert main([s, r, str(o), "--marques", t]) == 0
    assert o.read_text(encoding="utf-8") == "auteur : session_abc, revu.\n"


def test_main_refuse_sortie_existante(tmp_path):
    s = _ecrire(tmp_path / "s.md", SOURCE)
    r = _ecrire(tmp_path / "r.md", blocs(("Fin.", "x")))
    o = tmp_path / "o.md"; o.write_text("déjà là", encoding="utf-8")
    assert main([s, r, str(o)]) == 3
    assert o.read_text(encoding="utf-8") == "déjà là"


def test_main_refus_n_ecrit_rien(tmp_path):
    s = _ecrire(tmp_path / "s.md", SOURCE)
    for liste in (blocs(("Ligne B.", "x")), "<<<ANCIEN 1\nFin.\n"):
        r = _ecrire(tmp_path / "r.md", liste)
        o = tmp_path / "o.md"
        assert main([s, r, str(o)]) == 4
        assert not o.exists()


def test_main_source_non_utf8_ou_absente(tmp_path):
    s = tmp_path / "s.md"; s.write_bytes(b"\xff\xfe\x00")
    r = _ecrire(tmp_path / "r.md", blocs(("Fin.", "x")))
    assert main([str(s), r, str(tmp_path / "o.md")]) == 4
    assert main([str(tmp_path / "absent.md"), r, str(tmp_path / "o.md")]) == 4
