"""Essais du lot 10 a du véhicule NA-1 : colonne « matière première », chargement et garde (`matiere_premiere_na_v1`).

Chaque garde a son cas sain et son artefact (R5), sur le registre d'essai aux lignes inertes (`aides_na_lot10a_v1`) ; le
registre servi réel n'est pas ouvert. La garde au pas 3 est éprouvée contre le vrai `appel` du noyau et la vraie surcharge
du lot 4 (montage des essais du lot 4).
"""

import dataclasses
import hashlib
import inspect
import json
import os
import shutil
import sys
import tempfile

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
for _p in (ICI, os.path.dirname(ICI)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_lot10a_v1 as M  # noqa: E402
import aides_na_lot3_v3 as L3  # noqa: E402
import aides_na_lot4_v1 as L4  # noqa: E402
import aides_na_v4 as A  # noqa: E402
from pole import appel_garde_na_v1 as ag  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import matiere_premiere_na_v1 as mp  # noqa: E402
from pole import requete_na_v3 as rq  # noqa: E402

TEXTES = M.tous_les_textes()


def sans_contenu(*objets):
    """Aucun nom ni énoncé du registre d'essai dans la forme écrite de ces objets."""
    texte = " ".join(str(o) + repr(o) for o in objets)
    return not any(t in texte for t in TEXTES)


@pytest.fixture
def dossier():
    d = tempfile.mkdtemp(prefix="essais-na-lot10a-")
    yield d
    shutil.rmtree(d, ignore_errors=True)


# --- chargeur -----------------------------------------------------------------------------------------------------------

class TestChargeur:
    def test_cas_sain_trente_cinq_empreintes_seules(self):
        col = M.colonne()
        assert col.entrees == 35 and len(col.empreintes) == 35
        assert all(len(e) == 64 and set(e) <= set("0123456789abcdef") for e in col.empreintes)
        assert all(len(i) == 18 for i in col.identifiants())
        assert col.registre_sha256 == M.registre_octets()[1]

    def test_ni_nom_ni_enonce_ni_autre_champ_garde(self):
        col = M.colonne()
        gardes = [col.registre_sha256, col.entrees, dict(col._par_empreinte), repr(col), col.ligne_manifeste(1)]
        assert sans_contenu(*gardes)
        assert set(type(col).__slots__) == {"registre_sha256", "entrees", "_par_empreinte", "_normaliseur"}
        assert "visée factice" not in repr(gardes) and "défense factice" not in repr(gardes)

    def test_la_colonne_ne_change_pas(self):
        col = M.colonne()
        with pytest.raises(AttributeError):
            col.entrees = 1

    def test_empreinte_fausse_refusee_avant_toute_lecture(self):
        o, s = M.registre_octets()
        with pytest.raises(mp.ColonneNonChargee) as e:
            mp.lire_registre(b"pas du json {", s, **M.reglages())
        assert e.value.numero == 14
        with pytest.raises(mp.ColonneNonChargee) as e:
            mp.lire_registre(o + b" ", s, **M.reglages())
        assert e.value.numero == 14

    def test_registre_d_une_autre_empreinte_depuis_le_disque(self, dossier):
        o, s = M.registre_octets()
        chemin = os.path.join(dossier, "registre-essai.json")
        with open(chemin, "wb") as f:
            f.write(o)
        assert mp.charger_registre(chemin, s, **M.reglages()).entrees == 35
        with pytest.raises(mp.ColonneNonChargee) as e:
            mp.charger_registre(chemin, hashlib.sha256(b"autre").hexdigest(), **M.reglages())
        assert e.value.numero == 14

    @pytest.mark.parametrize("enonce, cause", [
        ("Énoncé factice\nsur deux lignes.", "plusieurs lignes"),
        ("Énoncé factice avec une marque `de code`.", "marque de code"),
        ("Énoncé factice, 1. une étape numérotée.", "étape"),
        ("Énoncé factice qui dit : réponds par oui.", "consigne"),
        ("Énoncé factice trop long. " * 20, "borne"),
    ])
    def test_enonce_non_conforme_colonne_non_chargee_sans_retrait(self, enonce, cause):
        liste = M.entrees()
        liste[7]["enonce"] = enonce
        o, s = M.registre_octets(liste)
        with pytest.raises(mp.ColonneNonChargee) as e:
            mp.lire_registre(o, s, **M.reglages())
        assert e.value.numero == 19
        assert [r for r, _ in e.value.defauts] == [8] * len(e.value.defauts)
        assert any(cause in c for _, c in e.value.defauts)
        assert sans_contenu(e.value, e.value.defauts) and enonce not in str(e.value)

    def test_etiquette_seule_du_n9_ne_refuse_pas_la_forme_du_n19(self):
        liste = M.entrees()
        liste[3]["enonce"] = "Énoncé factice qui porte une note : inerte."
        o, s = M.registre_octets(liste)
        assert mp.lire_registre(o, s, **M.reglages()).entrees == 35

    @pytest.mark.parametrize("change", ["champ_de_plus", "champ_manquant", "pas_un_objet", "enonce_non_chaine",
                                        "vide_apres_normalisation"])
    def test_entree_d_une_autre_forme(self, change):
        liste = M.entrees()
        if change == "champ_de_plus":
            liste[0]["autre"] = "x"
        elif change == "champ_manquant":
            del liste[0]["renvoi"]
        elif change == "pas_un_objet":
            liste[0] = ["liste"]
        elif change == "enonce_non_chaine":
            liste[0]["enonce"] = 12
        else:
            liste[0]["enonce"] = "​⁠"
        o, s = M.registre_octets(liste)
        with pytest.raises(mp.ColonneNonChargee) as e:
            mp.lire_registre(o, s, **M.reglages())
        assert e.value.defauts and e.value.defauts[0][0] == 1

    def test_nombre_d_entrees_attendu(self):
        o, s = M.registre_octets(M.entrees()[:34])
        with pytest.raises(mp.ColonneNonChargee):
            mp.lire_registre(o, s, **M.reglages())
        assert mp.lire_registre(o, s, **M.reglages(entrees_attendues=34)).entrees == 34

    def test_cle_des_entrees_et_cle_en_double(self):
        o = json.dumps({"entrees": M.entrees()}, ensure_ascii=False).encode("utf-8")
        assert mp.lire_registre(o, M.sha(o), **M.reglages(cle_des_entrees="entrees")).entrees == 35
        with pytest.raises(mp.ColonneNonChargee):
            mp.lire_registre(o, M.sha(o), **M.reglages())
        d = b'[{"nom": "a", "nom": "b", "enonce": "x", "sorte": "y", "renvoi": "z"}]'
        with pytest.raises(mp.ColonneNonChargee):
            mp.lire_registre(d, M.sha(d), **M.reglages(entrees_attendues=None))

    def test_normalisation_celle_de_la_garde_de_motifs_exigee(self):
        o, s = M.registre_octets()
        with pytest.raises(mp.ColonneNonChargee):
            mp.lire_registre(o, s, **M.reglages(normaliseur=object()))


class TestIdentifiantDeLigne:
    """E5 : la source des octets est reçue par une fonction ; deux fonctions d'essai différentes."""

    def test_deux_fonctions_differentes_memes_empreintes(self):
        c1, c2 = M.colonne(M.ident_par_rang), M.colonne(M.ident_par_empreinte_salee)
        assert c1.empreintes == c2.empreintes
        assert set(c1.identifiants()).isdisjoint(c2.identifiants())
        assert len(set(c1.identifiants())) == len(set(c2.identifiants())) == 35

    def test_la_garde_rend_l_identifiant_de_la_fonction_donnee(self):
        for f in (M.ident_par_rang, M.ident_par_empreinte_salee):
            col = M.colonne(f)
            assert col.examiner_ligne(M.enonce(4)) == (mp.ident.encoder_octets(f(5, None)),)

    def test_aucune_source_fixee_par_le_module(self):
        p = inspect.signature(mp.lire_registre).parameters["octets_identifiant_ligne"]
        assert p.default is inspect.Parameter.empty
        o, s = M.registre_octets()
        r = M.reglages()
        del r["octets_identifiant_ligne"]
        with pytest.raises(TypeError):
            mp.lire_registre(o, s, **r)
        with pytest.raises(mp.ColonneNonChargee):
            mp.lire_registre(o, s, **M.reglages(None))

    @pytest.mark.parametrize("fonction", [
        lambda rang, e: rang.to_bytes(5, "big"),
        lambda rang, e: "texte",
        lambda rang, e: b"\x00" * 6,
        lambda rang, e: 1 / 0,
    ])
    def test_identifiant_refuse_colonne_non_chargee(self, fonction):
        with pytest.raises(mp.ColonneNonChargee) as e:
            M.colonne(fonction)
        assert e.value.defauts

    def test_la_fonction_ne_peut_pas_changer_l_entree(self):
        def f(rang, entree):
            with pytest.raises(TypeError):
                entree["enonce"] = "autre"
            return rang.to_bytes(6, "big")
        assert M.colonne(f).entrees == 35


# --- garde de la colonne ------------------------------------------------------------------------------------------------

FORMES_RAMENEES = [
    lambda t: t.upper(),
    lambda t: t.replace(" ", " "),
    lambda t: "  " + t + "   ",
    lambda t: t.replace("entrée", "en​trée"),
    lambda t: t.replace(" ", "\t"),
    lambda t: "- " + t,
    lambda t: t.replace("É", "É"),
]


class TestGardeEnonceEntier:
    def test_cas_sain_voulu_nom_court_partie_reformulation_passent(self):
        col = M.colonne()
        e = M.enonce(2)
        for ligne in (M.nom_court(2), e[:30], e.replace("inerte", "sans effet"), "Avant. " + e, e + " Après.",
                      M.mot(2)):
            assert col.examiner_ligne(ligne) == ()

    def test_ligne_entiere_en_clair_mord(self):
        col = M.colonne()
        assert col.examiner_ligne(M.enonce(9)) == (mp.ident.encoder_octets((10).to_bytes(6, "big")),)

    @pytest.mark.parametrize("forme", FORMES_RAMENEES)
    def test_forme_que_la_normalisation_ramene_mord(self, forme):
        assert M.colonne().examiner_ligne(forme(M.enonce(30))) != ()

    def test_lignes_vides_ne_mordent_pas(self):
        col = M.colonne()
        assert col.examiner_texte("\n\n \n\t\n") == []

    def test_texte_rang_de_la_ligne(self):
        col = M.colonne()
        c = col.examiner_texte("une\ndeux\n" + M.enonce(0) + "\nquatre")
        assert [x.rang_ligne for x in c] == [3]


class TestGardeAuPasTrois:
    """Tenue (ii), contre le vrai `appel` du noyau et la surcharge du lot 4."""

    def test_cas_sain_requete_de_proposeur_part(self):
        m = M.MontageColonne(M.depart(1))
        r = L4.requete_proposeur(1, 0, M.synthese_avec(M.nom_court(1), M.enonce(1)[:25]))
        a = m.appeler("proposeur-espece-3", r)
        assert a["issue_na"] == "ok"
        assert [l["evenement"] for l in m.lignes()] == ["envoi"]
        assert len(m.recus()) == 1

    @pytest.mark.parametrize("forme", [lambda t: t] + FORMES_RAMENEES[:3])
    def test_artefact_ligne_egale_non_envoye_cout_nul_arret_nomme(self, forme):
        m = M.MontageColonne(M.depart(1))
        r = L4.requete_proposeur(1, 0, M.synthese_avec(forme(M.enonce(12))))
        etat = m.etat()
        with pytest.raises(mp.ArretColonneNA) as e:
            m.appeler("proposeur-espece-3", r, etat=etat)
        lignes = m.lignes()
        assert [l["evenement"] for l in lignes] == ["non envoyé"]
        assert lignes[0]["arret"] == mp.ARRET_COLONNE and lignes[0]["cout_usd"] == 0.0
        assert m.recus() == [] and m.gen.coffre.consommations() == [] and etat["cout"] == 0.0
        assert m.journal.comptes_colonne == {"proposeur-espece-3": 1}
        assert jn.comptes(lignes)["non_envoyes"] == {"proposeur-espece-3": {mp.ARRET_COLONNE: 1}}
        assert sans_contenu(e.value, lignes)

    def test_cumul_de_la_cle_inchange(self):
        m = M.MontageColonne(M.depart(1))
        avant = json.dumps(m.cumul.etat(), sort_keys=True)
        with pytest.raises(mp.ArretColonneNA):
            m.appeler("proposeur-espece-3", L4.requete_proposeur(1, 0, M.synthese_avec(M.enonce(3))))
        assert json.dumps(m.cumul.etat(), sort_keys=True) == avant

    def test_garde_avant_la_garde_de_motifs(self):
        m = M.MontageColonne(M.depart(1))
        r = L4.requete_proposeur(1, 0, M.synthese_avec("une graine factice", M.enonce(3)))
        with pytest.raises(mp.ArretColonneNA):
            m.appeler("proposeur-espece-3", r)

    def test_journal_en_panne_requete_journalisee(self):
        m = M.MontageColonne(M.depart(1))
        os.remove(m.journal.chemin)
        with pytest.raises(ag.ArretRequeteJournaliseeNA):
            m.appeler("proposeur-espece-3", L4.requete_proposeur(1, 0, M.synthese_avec(M.enonce(3))))
        assert m.recus() == []

    def test_sonde_gardee(self, dossier):
        gab = A.GABARIT_FACTICE + (M.enonce(6) + "\n").encode("utf-8")
        g = rq.charger_gabarit(gab, M.sha(gab))
        sortie = A.tirage_factice(gab).jouer(A.garde_essai())
        c = rq.cases_du_tirage(sortie, g)["1"][0]
        j = mp.JournalRequetesColonneNA(dossier, "j.jsonl", depart=M.depart(1))
        with pytest.raises(mp.ArretColonneNA):
            j.journaliser_envoi(rq.assembler_sonde_refus(g, c), A.garde_essai(), role="sonde-espece-1", cle="cle_a")
        j2 = mp.JournalRequetesColonneNA(dossier, "j2.jsonl", depart=M.depart(1))
        j2.journaliser_envoi(rq.assembler_sonde_refus(L3.gabarit(), L3.cases()["1"][0]), A.garde_essai(),
                             role="sonde-espece-1", cle="cle_a")

    def test_portier_et_juge_hors_de_la_tenue_ii(self, dossier):
        consigne = rq.charger_piece("consigne des juges", (M.enonce(6) + "\n").encode("utf-8"),
                                    M.sha((M.enonce(6) + "\n").encode("utf-8")))
        c = L3.cases()["1"][0]
        r = rq.assembler_juge(consigne, L3.contenu_fiche(c), L3.identifiant_juge(), c.identifiant, 1)
        j = mp.JournalRequetesColonneNA(dossier, "j.jsonl", depart=M.depart(1))
        j.journaliser_envoi(r, A.garde_essai(), role="juge-espece-3", cle="cle_a")
        assert j.comptes_colonne == {}

    def test_etat_zero_rien_n_est_garde(self):
        m = M.MontageColonne(M.depart(0))
        a = m.appeler("proposeur-espece-3", L4.requete_proposeur(1, 0, M.synthese_avec(M.enonce(12))))
        assert a["issue_na"] == "ok"

    def test_journal_exige_le_controle_de_depart(self, dossier):
        with pytest.raises(jn.JournalRefuse):
            mp.JournalRequetesColonneNA(dossier, "j.jsonl", depart=None)
        with pytest.raises(jn.JournalRefuse):
            mp.JournalRequetesColonneNA(dossier, "k.jsonl", depart=mp.DepartColonne(1, None, {}))

    def test_cent_soixante_cinq_requetes_egales_a_l_octet_etat_1_et_etat_0(self, dossier):
        cs = L3.cases()
        n = sum(len(cs[str(g)]) for g in (1, 2, 3))
        assert n * len(M.ROLES_PROPOSEURS) == 165
        rendu = {}
        for etat in (0, 1):
            j = mp.JournalRequetesColonneNA(dossier, f"j{etat}.jsonl", depart=M.depart(etat))
            for g in (1, 2, 3):
                for i in range(len(cs[str(g)])):
                    for role in M.ROLES_PROPOSEURS:
                        j.journaliser_envoi(L4.requete_proposeur(g, i), A.garde_essai(), role=role, cle="cle_a")
            rendu[etat] = [(l["sha256"], l["taille"]) for l in jn.verifier_journal(j.chemin)]
        assert len(rendu[1]) == 165 and rendu[0] == rendu[1]


# --- tenue (iii) et pièces fixes ----------------------------------------------------------------------------------------

class TestRegistreServi:
    def test_cas_sain(self):
        o = M.registre_servi([f"Idée factice passée, {M.mot(k)}." for k in range(4)])
        assert mp.garder_registre_servi(M.depart(1), o, 2) == 4

    @pytest.mark.parametrize("forme", [lambda t: t, FORMES_RAMENEES[0], FORMES_RAMENEES[1]])
    def test_artefact_la_generation_ne_part_pas_aucune_ligne_retiree(self, forme):
        o = M.registre_servi(["Idée factice passée.", forme(M.enonce(20)), "Autre idée factice."])
        copie = bytes(o)
        with pytest.raises(mp.GenerationRefuseeColonneNA) as e:
            mp.garder_registre_servi(M.depart(1), o, 3)
        assert [c.rang_ligne for c in e.value.constats] == [2] and o == copie
        assert sans_contenu(e.value)

    def test_etat_zero_et_generation_un(self):
        o = M.registre_servi([M.enonce(20)])
        assert mp.garder_registre_servi(M.depart(0), o, 2) == 0
        with pytest.raises(mp.RefusColonneNA):
            mp.garder_registre_servi(M.depart(1), o, 1)


class TestPiecesFixes:
    def test_cas_sain_sans_un_refus(self):
        assert mp.controler_pieces_fixes(M.colonne(), M.pieces_fixes()) == 5

    @pytest.mark.parametrize("piece", ["partie servie (gabarit)", "synthèse servie", "consigne du portier",
                                       "consigne des juges", "témoins"])
    def test_piece_qui_porte_un_enonce_entier_depart_refuse(self, piece):
        p = M.pieces_fixes()
        p[piece] = p[piece] + ("\n" + M.enonce(33) + "\n").encode("utf-8")
        with pytest.raises(mp.DepartRefuseColonneNA) as e:
            mp.controler_pieces_fixes(M.colonne(), p)
        assert piece in str(e.value) and sans_contenu(e.value)
        with pytest.raises(mp.DepartRefuseColonneNA):
            M.depart(1, pieces=p)

    def test_pieces_absentes_refusees(self):
        with pytest.raises(mp.DepartRefuseColonneNA):
            mp.controler_pieces_fixes(M.colonne(), {})


# --- sixième ligne et interrupteur -------------------------------------------------------------------------------------

class TestSixiemeLigne:
    def test_cas_sain(self):
        o, s = M.piece_releves()
        l = mp.lire_sixieme_ligne(o, s)
        assert (l.etat, l.registre_sha256, l.rang) == (1, M.registre_octets()[1], 6)

    @pytest.mark.parametrize("cas", ["absente", "double", "autre_libelle", "autre_libelle_en_plus", "mal_formee",
                                     "nom_d_etat_faux", "etat_3"])
    def test_ligne_refusee_depart_refuse(self, cas):
        if cas == "autre_libelle_en_plus":
            o, s = M.piece_releves(M.ligne_etat(), M.ligne_etat(libelle="colonne matière première :"))
        elif cas == "absente":
            o, s = M.piece_releves(sans_sixieme=True)
        elif cas == "double":
            o, s = M.piece_releves(M.ligne_etat(), M.ligne_etat())
        elif cas == "autre_libelle":
            o, s = M.piece_releves(M.ligne_etat(libelle="colonne matière première :"))
        elif cas == "mal_formee":
            o, s = M.piece_releves(M.ligne_etat().replace(" ; date ", " ; jour "))
        elif cas == "nom_d_etat_faux":
            o, s = M.piece_releves(M.ligne_etat(etat=1, nom="allumée"))
        else:
            o, s = M.piece_releves(M.ligne_etat(etat=1).replace("état 1 (garde seule)", "état 3 (garde seule)"))
        with pytest.raises(mp.DepartRefuseColonneNA):
            mp.lire_sixieme_ligne(o, s)
        with pytest.raises(mp.DepartRefuseColonneNA):
            mp.preparer_depart(piece_releves=o, empreinte_piece_releves=s,
                               empreinte_registre_attendue=M.registre_octets()[1], configuration={},
                               pieces_fixes=M.pieces_fixes(), charger=M.colonne, environ={})

    def test_empreinte_de_la_piece_fausse(self):
        o, s = M.piece_releves()
        with pytest.raises(mp.DepartRefuseColonneNA) as e:
            mp.lire_sixieme_ligne(o + b"x", s)
        assert e.value.numero == 14

    def test_empreinte_du_registre_fausse_dans_la_ligne(self):
        o, s = M.piece_releves(empreinte=hashlib.sha256(b"autre registre").hexdigest())
        with pytest.raises(mp.DepartRefuseColonneNA) as e:
            mp.preparer_depart(piece_releves=o, empreinte_piece_releves=s,
                               empreinte_registre_attendue=M.registre_octets()[1], configuration={},
                               pieces_fixes=M.pieces_fixes(), charger=_jamais, environ={})
        assert e.value.numero == 14

    def test_registre_charge_d_une_autre_empreinte_que_la_ligne(self):
        o, s = M.piece_releves()
        autre = M.entrees()[:34]
        with pytest.raises(mp.DepartRefuseColonneNA):
            mp.preparer_depart(piece_releves=o, empreinte_piece_releves=s,
                               empreinte_registre_attendue=M.registre_octets()[1], configuration={},
                               pieces_fixes=M.pieces_fixes(),
                               charger=lambda: M.colonne(liste=autre, entrees_attendues=34), environ={})


def _jamais():
    raise AssertionError("le chargeur ne doit pas être appelé")


class TestInterrupteur:
    def test_etat_1_sans_autre_condition_que_son_empreinte(self):
        d = M.depart(1)
        assert d.etat == 1 and isinstance(d.colonne, mp.Colonne)
        assert d.manifeste["etat"] == 1 and d.manifeste["entrees"] == 35 and sans_contenu(d.manifeste)

    def test_etat_0_rien_n_est_charge(self):
        o, s = M.piece_releves(etat=0)
        d = mp.preparer_depart(piece_releves=o, empreinte_piece_releves=s,
                               empreinte_registre_attendue=M.registre_octets()[1], configuration={},
                               pieces_fixes={}, charger=_jamais, environ={})
        assert d.etat == 0 and d.colonne is None

    def test_etat_2_refuse_sans_additif(self):
        with pytest.raises(mp.EtatRefuseNA) as e:
            M.depart(2)
        assert e.value.etat == 2

    def test_etat_2_cas_sain_toutes_conditions(self, dossier):
        d = M.depart(2, conditions_allumage=M.conditions(dossier))
        assert d.etat == 2 and isinstance(d.colonne, mp.Colonne)

    @pytest.mark.parametrize("manifeste", [None, {"format": mp.FORMAT_MANIFESTE_LECTURE_FIN},
                                           {"format": mp.FORMAT_MANIFESTE_LECTURE_FIN,
                                            mp.CLE_EMPREINTE_ADDITIF: hashlib.sha256(b"autre").hexdigest()}],
                             ids=["manifeste_absent", "empreinte_absente", "empreinte_fausse"])
    def test_e4_manifeste_artefacts(self, dossier, manifeste):
        with pytest.raises(mp.EtatRefuseNA) as e:
            M.depart(2, conditions_allumage=M.conditions(dossier, manifeste=manifeste))
        assert any(m.startswith("(b)") for m in e.value.manques)

    def test_e4_empreinte_posee_dans_la_configuration_seulement(self, dossier):
        conf = {mp.CLE_EMPREINTE_ADDITIF: M.EMPREINTE_ADDITIF_ESSAI, "additif": M.EMPREINTE_ADDITIF_ESSAI}
        c = M.conditions(dossier, manifeste={"format": mp.FORMAT_MANIFESTE_LECTURE_FIN})
        with pytest.raises(mp.EtatRefuseNA):
            M.depart(2, configuration=conf, conditions_allumage=c)
        c2 = dataclasses.replace(M.conditions(tempfile.mkdtemp(dir=dossier)), empreinte_additif_attendue=None)
        with pytest.raises(mp.EtatRefuseNA):
            M.depart(2, configuration=conf, conditions_allumage=c2)

    @pytest.mark.parametrize("remplace", [
        {"ligne_accord_lazar": None},
        {"ligne_accord_lazar": f"accord factice : colonne_matiere_premiere, état 1, registre {M.registre_octets()[1]}"},
        {"ligne_accord_lazar": "accord factice : colonne_matiere_premiere, état 2, registre d'une autre empreinte"},
        {"devis_ligne_a_part": None},
        {"devis_ligne_a_part": {"ligne": "course", "plafond_usd": 5.0, "hors_parts_de_la_course": True}},
        {"lecteurs_inscrits": ()},
        {"lecteurs_inscrits": ("proposeur de l'espèce 3",)},
        {"branche_orpheline": False},
        {"branche_orpheline": "oui"},
    ])
    def test_etat_2_chaque_condition_manquante(self, dossier, remplace):
        with pytest.raises(mp.EtatRefuseNA):
            M.depart(2, conditions_allumage=M.conditions(dossier, **remplace))

    def test_aucun_etat_par_variable_d_environnement(self, dossier):
        for env in ({"COLONNE_MATIERE_PREMIERE": "2"}, {"na_matiere_premiere_etat": "1"}):
            with pytest.raises(mp.EtatRefuseNA):
                M.depart(1, environ=env)
            with pytest.raises(mp.EtatRefuseNA):
                M.depart(2, environ=env, conditions_allumage=M.conditions(tempfile.mkdtemp(dir=dossier)))
        assert M.depart(1, environ={"PATH": "/bin", "LANG": "C.UTF-8"}).etat == 1

    def test_aucun_etat_par_la_configuration_seule(self):
        with pytest.raises(mp.EtatRefuseNA):
            M.depart(1, configuration={mp.CLE_CONFIGURATION: 2})
        with pytest.raises(mp.EtatRefuseNA):
            M.depart(1, configuration={mp.CLE_CONFIGURATION: 0})
        assert M.depart(1, configuration={mp.CLE_CONFIGURATION: 1}).etat == 1

    def test_refuse_avant_toute_ecriture_et_sans_chargement(self, dossier):
        o, s = M.piece_releves(etat=2)
        avant = sorted(os.listdir(dossier))
        with pytest.raises(mp.EtatRefuseNA):
            mp.preparer_depart(piece_releves=o, empreinte_piece_releves=s,
                               empreinte_registre_attendue=M.registre_octets()[1], configuration={},
                               pieces_fixes=M.pieces_fixes(), charger=_jamais, environ={})
        assert sorted(os.listdir(dossier)) == avant

    def test_l_etat_ne_se_lit_qu_a_la_sixieme_ligne(self):
        with pytest.raises(mp.EtatRefuseNA):
            mp.decider_etat(1, configuration={})


# --- taux de faux refus et absence ---------------------------------------------------------------------------------------

class TestFauxRefus:
    def test_taux_mesure_sur_l_essai_nul(self):
        m = mp.mesurer_faux_refus(M.colonne(), M.requetes_de_l_essai(),
                                  [M.registre_servi([f"Idée factice passée, {M.mot(k)}." for k in range(3)])])
        assert m["requetes"] == 100 and m["lignes_de_requete"] > 0
        assert m["lignes_refusees"] == 0 and m["enonces_refuses"] == 0 and m["taux_de_faux_refus"] == 0.0

    def test_la_mesure_voit_un_refus_plante(self):
        r = L4.requete_proposeur(1, 0, M.synthese_avec(M.enonce(1)))
        m = mp.mesurer_faux_refus(M.colonne(), [r], [M.registre_servi([M.enonce(2)])])
        assert m["lignes_refusees"] == 1 and m["enonces_refuses"] == 1 and m["taux_de_faux_refus"] > 0


class TestRienNeFuit:
    def test_ni_nom_ni_enonce_dans_la_sortie_le_run_ni_l_ecran(self, capsys):
        d = M.depart(1)
        m = M.MontageColonne(d)
        messages = []
        m.appeler("proposeur-espece-3", L4.requete_proposeur(1, 0))
        try:
            m.appeler("proposeur-espece-4", L4.requete_proposeur(1, 1, M.synthese_avec(M.enonce(5))))
        except mp.ArretColonneNA as e:
            messages.append(str(e))
        try:
            mp.garder_registre_servi(d, M.registre_servi([M.enonce(6)]), 2)
        except mp.GenerationRefuseeColonneNA as e:
            messages.append(str(e))
        run = os.path.join(m.dossier, "run")
        os.makedirs(run)
        with open(os.path.join(run, "manifeste-depart.json"), "x", encoding="utf-8") as f:
            f.write(json.dumps(d.manifeste, ensure_ascii=False))
        print(json.dumps(d.manifeste, ensure_ascii=False))
        print(messages)
        sortie = capsys.readouterr()
        assert len(messages) == 2
        assert mp.rechercher_textes([m.sortie, run], TEXTES) == {"fichiers_ou_trouve": 0, "trouvailles": 0}
        assert not any(t in sortie.out + sortie.err for t in TEXTES)

    def test_la_recherche_voit_un_texte_plante(self, dossier):
        with open(os.path.join(dossier, "plante.txt"), "x", encoding="utf-8") as f:
            f.write("x " + M.enonce(8) + " y")
        assert mp.rechercher_textes([dossier], TEXTES)["fichiers_ou_trouve"] == 1
