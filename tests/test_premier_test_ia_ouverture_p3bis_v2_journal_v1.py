"""Écrivain du journal des ouvertures de `premier_test_ia.ouverture_p3bis_v2`, corrigé d'après l'essai de concordance du
journal avec le lecteur de T0.7 (`docs/notes/g0-deux-semaines-v1/concordance-journal-p3bis-t07-v1/
rapport-concordance-journal-v1.md`, `c867a1b2…` ; décisions de la mère R-2103). Essais R5, un cas sain et au moins un
artefact par correction :
- D-1 : dates du journal non décroissantes ; horloge antérieure à la dernière ligne : refus sans ligne (code 2), rien
  d'ouvert ; date égale permise ; dernière ligne hors format tenue pour antérieure ; `inscrire` refuse aussi ;
- D-2 : `pleine-anticipee` refusée dès que `SCORES-T07` et `SONDES-T07` sont inscrites et conformes (le mode suit le
  registre, jamais l'opérateur) ; permise sous « ouvrir pleinement » sans elles ;
- D-3 : fichier vide hors format, jamais remis à zéro (aucun en-tête écrit dans un fichier vide) ; formes du tableau D-3
  du rapport refusées, CRLF seul admis ;
- D-4 : `SCELLEMENT-T07` et la garde adaptée citent `prereg/T0.7-sondes-v0-v1.md`, sinon `garde-adaptee-absente` ;
- clé `RENDEZ-VOUS-P3BIS-N` au motif `[1-9][0-9]*` du lecteur (`-01`, `-0` : `cle-inconnue`).
Aucun module de T0.7 n'est importé : le motif du lecteur est recopié du rapport (section 2)."""
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.premier_test_ia import ouverture_p3bis_v2 as ob
from test_premier_test_ia_ouverture_p3bis_v2 import (  # noqa: F401  (fixtures `clone` et `ouvrable` réutilisées)
    DATE_DECISION_LIGNE, DATE_PAQUET, INSTANT, OUV_PLEINE, OUV_REDUITE, PLUS_TARD, REFUS_SAIN, RUN, SHA_A, SHA_B,
    _ecrire_scelle, _journal, _lj, _monter, _ouvrir, _refus, _remplacer, _texte_journal, clone, ouvrable)

MOTIF_CLE_RDV_DU_LECTEUR = r"RENDEZ-VOUS-P3BIS-([1-9][0-9]*)"     # rapport de concordance, section 2 (lecteur 8dc1cb09)
RDV_OUVRIR = ("ouvrir", "2026-11-20T12:20:00Z", DATE_DECISION_LIGNE)
RDV_OUVRIR_PLEINEMENT = ("ouvrir pleinement", "2026-11-20T12:10:00Z")


def _octets(d):
    p = d / ob.JOURNAL_OUVERTURES
    return p.read_bytes() if p.exists() else None


# ================================================================================================= D-1
def test_d1_format_dates_non_decroissantes_saine_et_artefact():
    egale = _lj("REFUS-OUVERTURE-P3BIS", "2026-11-24T12:00:00Z", "pleine", "-", "-", "deja-ouverte : x")
    assert len(ob.exiger_format_journal(_texte_journal(REFUS_SAIN, egale, OUV_REDUITE, OUV_PLEINE))) == 4   # égalité permise
    recule = REFUS_SAIN.replace("2026-11-24T12:00:00Z", "2026-11-24T11:59:59Z")
    with pytest.raises(GardeArret, match=r"ligne 4 : date 2026-11-24T11:59:59Z antérieure à celle de la ligne 3"):
        ob.exiger_format_journal(_texte_journal(REFUS_SAIN, recule))
    p_sain = _texte_journal(REFUS_SAIN, OUV_PLEINE)
    with pytest.raises(GardeArret, match="dates non décroissantes"):                 # recul après une ligne hors format
        ob.exiger_format_journal(_texte_journal(OUV_PLEINE, "| main |", REFUS_SAIN))
    assert len(ob.exiger_format_journal(p_sain)) == 2


def test_d1_derniere_ligne_du_journal(tmp_path):
    p = tmp_path / "j.md"
    assert ob.instant_de_la_derniere_ligne(p) is None                               # absent
    for texte in ("", "\n".join(ob.ENTETE_JOURNAL) + "\n", ob.ENTETE_JOURNAL[0] + "\n", _texte_journal(REFUS_SAIN, ""),
                  _texte_journal(REFUS_SAIN, OUV_PLEINE + " x |")):                 # vide, en-tête, ligne vide, hors format
        p.write_text(texte, encoding="utf-8")
        assert ob.instant_de_la_derniere_ligne(p) is None, texte
    p.write_text(_texte_journal(OUV_PLEINE, REFUS_SAIN), encoding="utf-8")         # dernière ligne, pas la plus tardive
    assert ob.instant_de_la_derniere_ligne(p) == ob.instant_utc("2026-11-24T12:00:00Z")
    p.write_text(_texte_journal(REFUS_SAIN).replace("\n", "\r\n"), encoding="utf-8")   # CRLF : lu comme le lecteur
    assert ob.instant_de_la_derniere_ligne(p) == ob.instant_utc("2026-11-24T12:00:00Z")


def test_d1_horloge_en_arriere_refus_sans_ligne_rien_ouvert(ouvrable, capsys, monkeypatch):
    d = ouvrable["d"]
    _monter(d, normal=False)
    _refus(d, "ni-scores-ni-ouvrir", instant=PLUS_TARD)                             # une ligne datée PLUS_TARD
    _monter(d)
    avant = _octets(d)
    with pytest.raises(ob.HorlogeEnArriere, match="antérieure à la date de la dernière ligne du journal"):
        _ouvrir(d, instant=PLUS_TARD - 1)                                            # artefact : une seconde avant
    assert _octets(d) == avant and not (d.parent / "sortie").exists()
    assert issubclass(ob.HorlogeEnArriere, ob.JournalImpossible)                     # code 2 en ligne de commande
    monkeypatch.setattr(ob.time, "time", lambda: INSTANT)                            # horloge réelle en arrière (CP-08)
    assert ob._main(["ouvrir", "--racine", str(d), "--mode", "pleine", "--run", RUN, "--sortie", str(d.parent / "cli"),
                     "--date-paquet", DATE_PAQUET]) == 2
    assert capsys.readouterr().err.startswith("REFUS : horloge 2026-11-25T12:00:00Z antérieure")
    assert _octets(d) == avant and not (d.parent / "cli").exists()
    r, _ = _ouvrir(d, sortie="s2", instant=PLUS_TARD)                                # cas sain : même seconde permise
    assert r["mode"] == "pleine" and [x["date"] for x in _journal(d)] == ["2026-11-27T12:00:00Z"] * 2
    avant = _octets(d)
    with pytest.raises(ob.HorlogeEnArriere):                                         # après l'ouverture : jamais deja-
        _ouvrir(d, sortie="s3", instant=INSTANT)                                     # ouverte datée en arrière
    assert _octets(d) == avant


def test_d1_derniere_ligne_hors_format_tenue_pour_anterieure(ouvrable):
    d = ouvrable["d"]
    _monter(d)
    tardive = OUV_PLEINE.replace("2026-11-26T12:00:00Z", "2026-11-30T12:00:00Z") + " x |"   # sept cellules, datée après
    (d / ob.JOURNAL_OUVERTURES).write_text(_texte_journal(REFUS_SAIN, tardive), encoding="utf-8")
    with pytest.raises(ob.RefusOuverture) as e:                                      # tenue pour antérieure : pas de
        _ouvrir(d)                                                                   # refus d'horloge, refus de format
    assert e.value.code == "ligne-mal-formee" and not (d.parent / "sortie").exists()
    lignes = (d / ob.JOURNAL_OUVERTURES).read_text(encoding="utf-8").splitlines()
    assert lignes[3] == tardive and ob.lire_ligne_journal(lignes[4])["date"] == "2026-11-25T12:00:00Z"
    with pytest.raises(ob.HorlogeEnArriere):                                         # la ligne neuve est désormais la
        _ouvrir(d, sortie="s2", instant=INSTANT - 1)                                 # dernière : l'horloge s'y compare
    with pytest.raises(ob.RefusOuverture, match="ligne-mal-formee"):
        _ouvrir(d, sortie="s3", instant=INSTANT)


def test_d1_inscrire_refuse_une_ligne_datee_avant_la_derniere(tmp_path):
    (tmp_path / "registres").mkdir()
    l1 = ob.ligne_journal(ob.CLE_REFUS, INSTANT, "pleine", "-", "-", "deja-ouverte : x")
    ob.inscrire(tmp_path, l1)
    ob.inscrire(tmp_path, l1)                                                        # cas sain : même seconde
    avant = _octets(tmp_path)
    with pytest.raises(ob.HorlogeEnArriere):
        ob.inscrire(tmp_path, ob.ligne_journal(ob.CLE_REFUS, INSTANT - 1, "pleine", "-", "-", "deja-ouverte : x"))
    assert _octets(tmp_path) == avant and len(_journal(tmp_path)) == 2


# ================================================================================================= D-2
def test_d2_pleine_anticipee_permise_sans_lignes_de_t07(ouvrable):
    d = ouvrable["d"]
    _monter(d, normal=False, rdv=[RDV_OUVRIR_PLEINEMENT])                            # cas sain : branche 2
    r, _ = _ouvrir(d, "pleine-anticipee")
    assert r["mode"] == "pleine-anticipee" and r["chemin"].startswith("branche 2")


def test_d2_pleine_anticipee_refusee_des_que_scores_et_sondes_conformes(ouvrable):
    d = ouvrable["d"]
    _monter(d, normal=True, rdv=[RDV_OUVRIR_PLEINEMENT])                            # artefact : croisement E-8 (S06a)
    refus, ligne = _refus(d, "ni-scores-ni-ouvrir", "pleine-anticipee", motif="le mode suit le registre")
    assert "D-2" in ligne["motif"] and ligne["appui"].startswith("RENDEZ-VOUS-P3BIS-1=")
    _monter(d, normal=True)                                                         # sans décision : même refus, même texte
    _refus(d, "ni-scores-ni-ouvrir", "pleine-anticipee", sortie="s1", motif="seule « pleine » est permise")
    _monter(d, normal=True, rdv=[RDV_OUVRIR_PLEINEMENT])
    r, _ = _ouvrir(d, "pleine", sortie="s2")                                         # le registre décide : pleine
    assert r["mode"] == "pleine" and r["chemin"] == "chemin normal (rendez-vous sans objet)"
    assert [x["mode"] for x in _journal(d) if x["cle"] == ob.CLE_OUVERTURE] == ["pleine"]


def test_d2_complement_apres_la_reduite_suit_le_registre(ouvrable):
    """E-9 : « ouvrir », réduite, puis « ouvrir pleinement » ; SCORES-T07 et SONDES-T07 conformes : `pleine-anticipee`
    refusée, `pleine` (complément) seule permise."""
    d = ouvrable["d"]
    _monter(d, normal=False, rdv=[RDV_OUVRIR], garde=True, scellement_t07=True)
    _ouvrir(d, "reduite")
    _monter(d, normal=True, rdv=[RDV_OUVRIR, ("ouvrir pleinement", "2026-11-26T10:00:00Z")], garde=True,
            scellement_t07=True)
    _refus(d, "ni-scores-ni-ouvrir", "pleine-anticipee", sortie="s1", instant=PLUS_TARD, motif="D-2")
    r, _ = _ouvrir(d, "pleine", sortie="s2", instant=PLUS_TARD)
    assert r["chemin"] == "complément de l'ouverture réduite"


def test_d2_lignes_de_t07_non_conformes_pas_de_croisement(ouvrable):
    """Lignes inscrites mais non conformes (compagnon autre) : « inscrites et conformes » non rempli, la branche 2 reste
    ouverte sous « ouvrir pleinement » (lecture littérale de R-2103, déclarée)."""
    d = ouvrable["d"]
    _monter(d, normal=True, rdv=[RDV_OUVRIR_PLEINEMENT])
    (d / "diag/t07-run/scores-actions-t07.npz.sha256").write_text("d" * 64 + "  scores-actions-t07.npz\n", encoding="utf-8")
    assert _ouvrir(d, "pleine-anticipee")[0]["mode"] == "pleine-anticipee"


# ================================================================================================= D-3
def test_d3_fichier_vide_hors_format_jamais_remis_a_zero(ouvrable):
    d = ouvrable["d"]
    _monter(d)
    j = d / ob.JOURNAL_OUVERTURES
    j.write_bytes(b"")                                                               # artefact : fichier vide
    with pytest.raises(ob.RefusOuverture) as e:
        _ouvrir(d)
    assert e.value.code == "ligne-mal-formee" and "fichier vide" in e.value.texte and not (d.parent / "sortie").exists()
    lignes = j.read_text(encoding="utf-8").splitlines()
    assert len(lignes) == 1 and ob.lire_ligne_journal(lignes[0])["motif"].startswith("ligne-mal-formee : ")   # sans en-tête
    with pytest.raises(ob.RefusOuverture, match="en-tête"):                          # reste hors format
        _ouvrir(d, sortie="s1")
    assert not (d.parent / "s1").exists()
    j.unlink()                                                                       # cas sain : journal absent
    r, _ = _ouvrir(d, sortie="s2")
    assert r["mode"] == "pleine" and j.read_text(encoding="utf-8").splitlines()[:2] == list(ob.ENTETE_JOURNAL)
    j.write_bytes(b"")                                                               # journal vidé après une ouverture :
    with pytest.raises(ob.RefusOuverture, match="fichier vide"):                     # jamais une seconde ouverture
        _ouvrir(d, sortie="s3", instant=PLUS_TARD)
    assert not (d.parent / "s3").exists()


def test_d3_inscrire_n_ecrit_pas_d_en_tete_dans_un_fichier_vide(tmp_path):
    (tmp_path / "registres").mkdir()
    l1 = ob.ligne_journal(ob.CLE_REFUS, INSTANT, "pleine", "-", "-", "deja-ouverte : x")
    ob.inscrire(tmp_path, l1)                                                        # cas sain : absent, en-tête écrit
    assert _octets(tmp_path).decode() == _texte_journal(l1)
    (tmp_path / ob.JOURNAL_OUVERTURES).write_bytes(b"")
    ob.inscrire(tmp_path, l1)                                                        # artefact : vide, ligne seule
    assert _octets(tmp_path).decode() == l1 + "\n"


A, Z = "a" * 64, "f" * 64
FORMES_D3 = {   # tableau D-3 du rapport de concordance : formes que l'écrivain refuse (une ligne écrite à la main)
    "ligne vide entre deux lignes": _texte_journal(REFUS_SAIN, "", OUV_PLEINE),
    "ligne vide en fin": _texte_journal(REFUS_SAIN) + "\n",
    "sans saut de ligne final": _texte_journal(REFUS_SAIN)[:-1],
    "espace en tête d'une ligne": _texte_journal(" " + REFUS_SAIN),
    "séparation de table alignée": "\n".join((ob.ENTETE_JOURNAL[0], "| --- | --- | --- | --- | --- | --- |",
                                               REFUS_SAIN)) + "\n",
    "OUVERTURE à paquets « - »": _texte_journal(_lj("OUVERTURE-P3BIS", "2026-11-22T00:00:00Z", "pleine-anticipee",
                                                    f"RENDEZ-VOUS-P3BIS-1={A}", "-", "-")),
    "OUVERTURE à appui « - »": _texte_journal(_lj("OUVERTURE-P3BIS", "2026-11-22T00:00:00Z", "pleine", "-", f"{A} {Z}",
                                                  "-")),
    "OUVERTURE à motif autre que « - »": _texte_journal(_lj("OUVERTURE-P3BIS", "2026-11-22T00:00:00Z", "pleine",
                                                            f"SCORES-T07={A} SONDES-T07={Z}", f"{A} {Z}",
                                                            "paquet-faux : texte")),
    "REFUS à motif hors de la liste fermée": _texte_journal(_lj("REFUS-OUVERTURE-P3BIS", "2026-11-22T00:00:00Z", "pleine",
                                                                "-", "-", "code-inconnu : texte")),
    "REFUS à motif sans code": _texte_journal(_lj("REFUS-OUVERTURE-P3BIS", "2026-11-22T00:00:00Z", "pleine", "-", "-",
                                                  "texte libre")),
    "REFUS à appui hors forme": _texte_journal(_lj("REFUS-OUVERTURE-P3BIS", "2026-11-22T00:00:00Z", "pleine",
                                                   "texte libre", "-", "deja-ouverte : texte")),
    "date impossible": _texte_journal(_lj("REFUS-OUVERTURE-P3BIS", "2026-02-30T00:00:00Z", "pleine", "-", "-",
                                          "deja-ouverte : t")),
    "mode inconnu": _texte_journal(_lj("REFUS-OUVERTURE-P3BIS", "2026-11-22T00:00:00Z", "Pleine", "-", "-",
                                       "deja-ouverte : t")),
    "clé inconnue": _texte_journal(_lj("OUVERTURE-P3BIS-2", "2026-11-22T00:00:00Z", "pleine", "-", "-", "-")),
    "ordre interdit": _texte_journal(OUV_PLEINE, OUV_REDUITE.replace("2026-11-25", "2026-11-27")),
    "dates décroissantes (D-1)": _texte_journal(OUV_REDUITE, REFUS_SAIN),
}


def test_d3_formes_admises_cas_sains(tmp_path):
    p = tmp_path / "j.md"
    for texte, n in ((_texte_journal(REFUS_SAIN, OUV_REDUITE, OUV_PLEINE), 3), ("\n".join(ob.ENTETE_JOURNAL) + "\n", 0)):
        p.write_text(texte, encoding="utf-8")
        assert len(ob.lire_journal(p)) == n
        p.write_bytes(texte.replace("\n", "\r\n").encode())                          # CRLF : admis des deux côtés
        assert len(ob.lire_journal(p)) == n
    assert ob.lire_journal(tmp_path / "absent.md") == []


@pytest.mark.parametrize("forme", sorted(FORMES_D3) + ["fichier vide (0 octet)"])
def test_d3_formes_refusees_comme_au_tableau_du_rapport(tmp_path, forme):
    p = tmp_path / "j.md"
    p.write_bytes(FORMES_D3.get(forme, "").encode())
    with pytest.raises(ob.RefusOuverture) as e:
        ob.lire_journal(p)
    assert e.value.code == "ligne-mal-formee" and "hors format" in e.value.texte


# ================================================================================================= D-4
def _autre_chemin_du_texte_de_t07(d, scellement=True, garde=True):
    """Même texte de T0.7 (même empreinte), scellé sous un autre chemin, cité par SCELLEMENT-T07 et/ou la garde adaptée."""
    contenu = (d / ob.PREREG_T07).read_bytes()
    _ecrire_scelle(d, "prereg/T0.7-autre-v1.md", contenu)
    if scellement:
        _remplacer(d, ob.REGISTRE_SCELLEMENTS, f"| {ob.SCELLEMENT_T07} | 2026-11-18T10:00:00Z | {ob.PREREG_T07} |",
                   f"| {ob.SCELLEMENT_T07} | 2026-11-18T10:00:00Z | prereg/T0.7-autre-v1.md |")
    if garde:
        _remplacer(d, ob.REGISTRE_PREALABLES, f"| {ob.CLE_GARDE_ADAPTEE} | 2026-11-19T10:00:00Z | {ob.PREREG_T07} |",
                   f"| {ob.CLE_GARDE_ADAPTEE} | 2026-11-19T10:00:00Z | prereg/T0.7-autre-v1.md |")


def test_d4_scellement_et_garde_citent_le_texte_de_t07(ouvrable):
    d = ouvrable["d"]
    assert ob.PREREG_T07 == "prereg/T0.7-sondes-v0-v1.md"
    for k, (scellement, garde) in enumerate(((True, True), (True, False), (False, True))):
        _monter(d, normal=False, rdv=[RDV_OUVRIR], garde=True, scellement_t07=True)
        _autre_chemin_du_texte_de_t07(d, scellement, garde)                          # artefacts (D04 du rapport)
        _refus(d, "garde-adaptee-absente", "reduite", sortie=f"r{k}", motif="'prereg/T0.7-sondes-v0-v1.md' attendu (D-4")
    assert not [x for x in _journal(d) if x["cle"] == ob.CLE_OUVERTURE]
    _monter(d, normal=False, rdv=[RDV_OUVRIR], garde=True, scellement_t07=True)    # cas sain
    assert _ouvrir(d, "reduite", sortie="sain")[0]["mode"] == "reduite"


# ================================================================================================= clé de rendez-vous
def test_cle_rendez_vous_au_motif_du_lecteur():
    assert ob.RENDEZ_VOUS.pattern == MOTIF_CLE_RDV_DU_LECTEUR
    assert [ob.RENDEZ_VOUS.fullmatch(f"RENDEZ-VOUS-P3BIS-{n}").group(1) for n in ("1", "9", "10", "123")] == \
        ["1", "9", "10", "123"]
    assert [ob.RENDEZ_VOUS.fullmatch(f"RENDEZ-VOUS-P3BIS-{n}") for n in ("0", "01", "007", "", "1a")] == [None] * 5


@pytest.mark.parametrize("numero", ["01", "0"])
def test_cle_rendez_vous_numero_hors_motif_cle_inconnue(ouvrable, numero):
    d = ouvrable["d"]
    _monter(d, normal=False, rdv=[RDV_OUVRIR_PLEINEMENT])
    _remplacer(d, ob.REGISTRE_PREALABLES, "| RENDEZ-VOUS-P3BIS-1 |", f"| RENDEZ-VOUS-P3BIS-{numero} |")
    _refus(d, "cle-inconnue", "pleine-anticipee", motif=f"RENDEZ-VOUS-P3BIS-{numero}")
    _monter(d, normal=False, rdv=[RDV_OUVRIR_PLEINEMENT])                            # cas sain : RENDEZ-VOUS-P3BIS-1
    assert _ouvrir(d, "pleine-anticipee", sortie="sain")[0]["mode"] == "pleine-anticipee"

