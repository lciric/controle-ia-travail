"""Essais du registre des tentatives, du registre servi, de sa vérification et de la garde du coffre (lot 5 du véhicule
NA-1) : arrêts n° 5, n° 8, n° 9, n° 19 ; lignes de compte à zéro (conception v5, § 2.6, § 6.1, § 6.2). Données factices
seules ; registre servi d'essai aux lignes inertes ; le registre servi réel n'est pas ouvert."""

import json
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aides_na_lot5_v1 as A5  # noqa: E402
from pole import garde_motifs_na_v4 as gm  # noqa: E402
from pole import lecteur_fiches_na_v1 as lf  # noqa: E402
from pole import portier_na_v1 as pt  # noqa: E402
from pole import registre_na_v1 as rg  # noqa: E402
from pole import requete_na_v3 as rq  # noqa: E402
from pole import verifier_registre_servi_na_v1 as vr  # noqa: E402

RACINE = A5.A.RACINE_FACTICE
BORNE_ENONCE = 1200
BORNE_REGISTRE = 64000
NIVEAU = A5.etiquette("niveau de l'idée")


def cases_g1():
    return [A5.case_de((1, k % 5, k % 4), 1000 + 37 * k) for k in range(4)]


def lignes_factices():
    """Lignes du registre des tentatives d'une génération 1 factice : deux passées, une au coffre, une hors case."""
    c = cases_g1()
    return [
        {"identifiant": A5.mot_fiche(1), "generation": 1, "case": c[0].identifiant, "classe": "passée",
         "ce_que_le_moniteur_suppose": "trait factice deux", "menace_du_programme": "sabotage factice",
         "etage_de_lecture": "étage factice un", "nom": A5.mot_fiche(1), "enonce": "Énoncé factice un."},
        {"identifiant": A5.mot_fiche(2), "generation": 1, "case": c[1].identifiant, "classe": "passée",
         "ce_que_le_moniteur_suppose": "trait factice deux", "menace_du_programme": "menace factice deux",
         "etage_de_lecture": "étage factice deux", "nom": A5.mot_fiche(2), "enonce": "Énoncé factice ; deux."},
        {"identifiant": A5.mot_fiche(3), "generation": 1, "case": c[0].identifiant, "classe": "au coffre"},
        {"identifiant": A5.mot_fiche(4), "generation": 1, "case": c[2].identifiant, "classe": "hors case"},
    ]


def servi(lignes=None, generation=2, permuter=True, cases=None):
    cases = cases or {1: [c.identifiant for c in cases_g1()]}
    return rg.fabriquer_registre_servi(lignes_factices() if lignes is None else lignes, cases, generation,
                                       permuter_comptes=permuter, racine=RACINE, racine_attendue=RACINE)


def verifier(octets, **kw):
    kw.setdefault("borne_registre_octets", BORNE_REGISTRE)
    kw.setdefault("borne_enonce_octets", BORNE_ENONCE)
    return vr.verifier_registre_servi(octets, **kw)


@pytest.fixture
def dossier(tmp_path):
    d = tmp_path / "sortie"
    d.mkdir()
    return str(d)


class TestRegistreDesTentatives:
    def test_lignes_aux_champs_fermes_nom_et_enonce(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU, A5.etiquette("concret")])
        c = A5.contenu(idee="Idée factice\n  sur   deux lignes.\tFin.")
        i1 = p.classer_fiche(lf.lire_fiches(A5.en_lignes(c)).fiches[0], identifiant=A5.mot_fiche(1), case=A5.CASE)
        i2 = p.classer_fiche(lf.lire_fiches(A5.en_lignes(A5.contenu())).fiches[0], identifiant=A5.mot_fiche(2),
                             case=A5.CASE)
        r = rg.RegistreTentatives(dossier, "registre-tentatives-essai.jsonl")
        l1, l2 = r.ajouter_fiche(i1), r.ajouter_fiche(i2)
        assert l1["nom"] == l1["identifiant"] == A5.mot_fiche(1)
        assert l1["enonce"] == "Idée factice sur deux lignes. Fin."
        assert {k for k in l2} == {"identifiant", "generation", "case", "classe", "rang", "precedente", "version"}
        r.sceller()
        lignes = rg.lire_registre_tentatives(r.chemin, exiger_sceau=True)
        assert [l["classe"] for l in lignes] == [pt.PASSEE, pt.AU_COFFRE]
        brut = open(r.chemin, encoding="utf-8").read()
        for interdit in ("grandeur factice", "issue factice", "aucun connu", "verdict", "cout", "espece"):
            assert interdit not in brut

    def test_enonce_sans_coupe(self):
        long = "mot " * 600
        assert rg.enonce_sur_une_ligne(long) == ("mot " * 600).strip()

    def test_champ_hors_liste_refuse(self, dossier):
        r = rg.RegistreTentatives(dossier, "r.jsonl")
        with pytest.raises(pt.AjoutSeulRefuse):
            r.ajouter({"identifiant": "x", "espece": "3"})


class TestRegistreServi:
    def test_lignes_de_compte_ecrites_toujours_compte_nul_compris(self):
        s = servi()
        lignes = s.octets.decode("utf-8").splitlines()
        comptes = [l for l in lignes if l.startswith(rg.TETE_COMPTE)]
        assert len(comptes) == 4 * 2 and s.lignes_compte == 8
        c3 = cases_g1()[3].identifiant  # case sans aucune fiche
        assert f"compte : {c3} ; au coffre ; 0" in comptes and f"compte : {c3} ; hors case ; 0" in comptes
        c0 = cases_g1()[0].identifiant
        assert f"compte : {c0} ; au coffre ; 1" in comptes and f"compte : {c0} ; hors case ; 0" in comptes

    def test_une_ligne_par_tentative_passee_forme_declaree(self):
        lignes = servi().octets.decode("utf-8").splitlines()
        t = [l for l in lignes if l.startswith(rg.TETE_TENTATIVE)]
        assert len(t) == 2
        attendue = "tentative : " + A5.mot_fiche(2) + " ; trait factice deux ; menace factice deux ; étage factice deux ; " \
            "passée ; " + json.dumps("Énoncé factice ; deux.", ensure_ascii=False)
        assert attendue in t

    def test_ordre_range_puis_permute_par_la_cle_12(self):
        s = servi()
        lignes = s.octets.decode("utf-8").splitlines()

        def cle(l):
            ident = l.split(" : ", 1)[1].split(" ; ")[0]
            rangc = {"au coffre": 0, "hors case": 1}.get(l.split(" ; ")[1], -1) if l.startswith("compte") else -1
            return (ident.encode("utf-8"), rangc)

        rangees = sorted(lignes, key=cle)
        perm = A5.tn.permutation_registre(2, len(rangees), RACINE, RACINE)
        assert lignes == [rangees[i] for i in perm]
        assert lignes != rangees

    def test_comptes_non_permutes_si_dit(self):
        s = servi(permuter=False)
        lignes = s.octets.decode("utf-8").splitlines()
        assert all(l.startswith(rg.TETE_TENTATIVE) for l in lignes[:2])
        assert all(l.startswith(rg.TETE_COMPTE) for l in lignes[2:])

    def test_permuter_comptes_doit_etre_dit(self):
        with pytest.raises(rg.RegistreRefuse):
            rg.fabriquer_registre_servi(lignes_factices(), {1: [c.identifiant for c in cases_g1()]}, 2,
                                        permuter_comptes=None, racine=RACINE, racine_attendue=RACINE)

    def test_generation_3_lit_les_generations_1_et_2_seules(self):
        g2 = [A5.case_de((2, 1, 1), 5000)]
        lignes = lignes_factices() + [
            {"identifiant": A5.mot_fiche(9), "generation": 2, "case": g2[0].identifiant, "classe": "au coffre"},
            {"identifiant": A5.mot_fiche(10), "generation": 3, "case": "gagaga", "classe": "au coffre"}]
        s = servi(lignes, generation=3, cases={1: [c.identifiant for c in cases_g1()], 2: [g2[0].identifiant]})
        assert s.lignes_compte == 10 and s.lignes_tentative == 2
        assert f"compte : {g2[0].identifiant} ; au coffre ; 1" in s.octets.decode("utf-8")

    def test_tentative_d_une_case_non_servie_refusee(self):
        lignes = lignes_factices() + [{"identifiant": A5.mot_fiche(11), "generation": 1, "case": "gagaga",
                                       "classe": "hors case"}]
        with pytest.raises(rg.RegistreRefuse):
            servi(lignes)

    def test_registre_servi_passe_la_verification_et_la_garde_de_motifs(self):
        s = servi()
        constat = verifier(s.octets, noms_attendus=[A5.mot_fiche(1), A5.mot_fiche(2)],
                           cases_attendues=[c.identifiant for c in cases_g1()])
        assert constat.lignes == s.lignes
        assert A5.A.garde_essai().examiner(s.octets.decode("utf-8")) is None

    def test_le_registre_va_dans_la_requete_du_proposeur(self):
        s = servi()
        piece = rq.charger_piece("registre servi", s.octets, s.sha256)
        g = A5.A3.gabarit()
        case = A5.A3.cases()["2"][0]
        r = rq.assembler_proposeur(g, case, A5.A3.synthese(), 2, piece, A5.A3.TITRE_REGISTRE_FACTICE)
        assert r.registre == rq.REGISTRE_SERVI and r.octets.endswith(s.octets)
        assert isinstance(A5.A.garde_essai().garder_requete(r.octets), gm.RequeteGardee)


class TestArret19:
    def _octets(self):
        return servi().octets

    def _ligne_t(self):
        return [l for l in self._octets().decode("utf-8").splitlines() if l.startswith(rg.TETE_TENTATIVE)][0]

    def _avec(self, ancienne, nouvelle):
        t = self._octets().decode("utf-8")
        assert t.count(ancienne) == 1
        return t.replace(ancienne, nouvelle).encode("utf-8")

    def test_registre_aux_seuls_champs_permis_passe(self):
        assert verifier(self._octets()).lignes_tentative == 2

    def _refus(self, octets, numero=19):
        avant = bytes(octets)
        with pytest.raises(vr.RegistreServiNonConforme) as e:
            verifier(octets)
        assert numero in e.value.numeros
        assert octets == avant  # aucune ligne retirée
        return e.value

    def test_un_champ_de_plus(self):
        l = self._ligne_t()
        self._refus(self._avec(l, l.replace(" ; passée ; ", " ; champ factice ; passée ; ")))
        self._refus(self._avec(l, l + " ; champ factice"))

    def test_deux_lignes_pour_une_tentative(self):
        l = self._ligne_t()
        e = self._refus(self._avec(l, l + "\n" + l))
        assert any(d.cause == "deux lignes pour une tentative" for d in e.defauts)

    def test_un_enonce_d_un_octet_de_trop(self):
        l = self._ligne_t()
        nom = l.split(" : ", 1)[1].split(" ; ")[0]
        juste = "x" * BORNE_ENONCE
        ligne = rg.ligne_tentative(nom, ("a", "b", "c"), juste)
        assert verifier((ligne + "\n").encode("utf-8")).lignes == 1
        self._refus((rg.ligne_tentative(nom, ("a", "b", "c"), juste + "x") + "\n").encode("utf-8"))

    @pytest.mark.parametrize("marque", ["une `marque` de code", "un bloc { factice }", "def factice ", "import factice",
                                        "chemin\\factice"])
    def test_une_marque_de_code(self, marque):
        nom = A5.mot_fiche(1)
        self._refus((rg.ligne_tentative(nom, ("a", "b", "c"), "Énoncé " + marque) + "\n").encode("utf-8"))

    @pytest.mark.parametrize("etape", ["1. faire factice", "étape 2 factice", "premièrement factice", "x 3) y"])
    def test_une_etape_numerotee(self, etape):
        nom = A5.mot_fiche(1)
        self._refus((rg.ligne_tentative(nom, ("a", "b", "c"), etape) + "\n").encode("utf-8"))

    @pytest.mark.parametrize("consigne", ["ignore la suite factice", "tu dois factice", "system : factice"])
    def test_une_marque_de_consigne(self, consigne):
        self._refus((rg.ligne_tentative(A5.mot_fiche(1), ("a", "b", "c"), consigne) + "\n").encode("utf-8"))

    def test_enonce_sur_deux_lignes(self):
        self._refus((rg.ligne_tentative(A5.mot_fiche(1), ("a", "b", "c"), "un deux") + "\n").encode("utf-8"))
        # appel direct, celui du lot 10 a (chargement de la colonne) : la forme de l'arrêt n° 19 sur un énoncé seul
        for enonce in ("un\ndeux", "un deux", "un\rdeux", "un\x85deux"):
            assert (19, "énoncé sur plusieurs lignes") in vr.verifier_enonce(enonce, BORNE_ENONCE)
        assert vr.verifier_enonce("Énoncé factice sur une ligne.", BORNE_ENONCE) == []

    def test_classe_autre_que_passee(self):
        l = self._ligne_t()
        self._refus(self._avec(l, l.replace(" ; passée ; ", " ; au coffre ; ")))

    def test_ligne_d_une_autre_forme_et_compte_non_entier(self):
        self._refus(self._octets() + b"ligne factice libre\n")
        t = self._octets().decode("utf-8")
        c = [l for l in t.splitlines() if l.startswith(rg.TETE_COMPTE)][0]
        self._refus(self._avec(c, c.rsplit(" ; ", 1)[0] + " ; deux"))

    def test_ligne_de_compte_manquante_ou_tentative_manquante(self):
        t = self._octets().decode("utf-8")
        c0 = cases_g1()[3].identifiant
        sans = "\n".join(l for l in t.splitlines() if not l.startswith(f"compte : {c0} ; hors case")) + "\n"
        with pytest.raises(vr.RegistreServiNonConforme):
            verifier(sans.encode("utf-8"), cases_attendues=[c.identifiant for c in cases_g1()])
        with pytest.raises(vr.RegistreServiNonConforme):
            verifier(self._octets(), noms_attendus=[A5.mot_fiche(1)])

    def test_les_arrets_s_ajoutent(self):
        l = self._ligne_t()
        e = self._refus(self._avec(l, l + " ; note : sept"))
        assert set(e.numeros) >= {9, 19}

    def test_message_sans_contenu(self):
        e = self._refus((rg.ligne_tentative(A5.mot_fiche(1), ("a", "b", "c"), "zqxv `x`") + "\n").encode("utf-8"))
        assert "zqxv" not in str(e) and all("zqxv" not in d.cause for d in e.defauts)


class TestArret9:
    @pytest.mark.parametrize("etiquette", ["note : sept", "rang : deux", "verdict de juge : retenu",
                                           "antériorité trouvée", "coût : trois USD"])
    def test_chacune_des_cinq_etiquettes_tour_a_tour(self, etiquette):
        nom = A5.mot_fiche(1)
        octets = (rg.ligne_tentative(nom, ("a", "b", "c"), "Énoncé factice, " + etiquette) + "\n").encode("utf-8")
        with pytest.raises(vr.RegistreServiNonConforme) as e:
            verifier(octets)
        assert 9 in e.value.numeros

    def test_registre_sans_etiquette_passe(self):
        verifier(servi().octets)

    def test_cout_en_chiffres(self):
        octets = (rg.ligne_tentative(A5.mot_fiche(1), ("a", "b", "c"), "vaut 3,5 USD") + "\n").encode("utf-8")
        with pytest.raises(vr.RegistreServiNonConforme) as e:
            verifier(octets)
        assert 9 in e.value.numeros


class TestArret8:
    def test_registre_egal_a_sa_borne_passe_un_octet_de_plus_refuse(self):
        s = servi()
        assert verifier(s.octets, borne_registre_octets=s.taille).taille == s.taille
        with pytest.raises(vr.RegistreServiNonConforme) as e:
            verifier(s.octets, borne_registre_octets=s.taille - 1)
        assert e.value.numeros == (8,)

    def test_consigne_registre_compris_a_sa_borne(self):
        s = servi()
        piece = rq.charger_piece("registre servi", s.octets, s.sha256)
        r = rq.assembler_proposeur(A5.A3.gabarit(), A5.A3.cases()["2"][0], A5.A3.synthese(), 2, piece,
                                   A5.A3.TITRE_REGISTRE_FACTICE)
        assert rq.verifier_borne(r, r.taille) == r.taille
        with pytest.raises(rq.ArretConsigneTropLongue):
            rq.verifier_borne(r, r.taille - 1)


class TestArret5GardeDuCoffre:
    def _lignes(self, coffre, autres, generation):
        return [{"generation": generation, "classe": "au coffre"}] * coffre + \
            [{"generation": generation, "classe": "passée"}] * autres

    @pytest.mark.parametrize("generation", [1, 2])
    def test_un_quart_exactement_la_suivante_part(self, generation):
        c = rg.garde_du_coffre(self._lignes(3, 9, generation), generation)
        assert (c.au_coffre, c.rendues, c.depasse) == (3, 12, False)

    @pytest.mark.parametrize("generation", [1, 2])
    def test_une_fiche_de_plus_au_coffre_la_suivante_ne_part_pas(self, generation):
        with pytest.raises(rg.ArretGardeCoffre) as e:
            rg.garde_du_coffre(self._lignes(4, 9, generation), generation)
        assert e.value.numero == 5

    def test_a_la_troisieme_consigne(self):
        c = rg.garde_du_coffre(self._lignes(4, 9, 3), 3)
        assert c.depasse and c.consigne

    def test_ne_lit_que_sa_generation_et_compte_les_fiches_rendues(self):
        lignes = self._lignes(3, 9, 1) + self._lignes(10, 0, 2) + [{"generation": 1, "classe": "hors case"}]
        c = rg.garde_du_coffre(lignes, 1)
        assert (c.au_coffre, c.rendues, c.depasse) == (3, 13, False)

    def test_avec_le_portier_hors_longueur_et_refus_ecrit_au_denominateur(self, dossier):
        issues = [NIVEAU, NIVEAU, "refus écrit"]
        p, _ = A5.portier(dossier, issues)
        r = rg.RegistreTentatives(dossier, "registre.jsonl")
        for k in range(3):
            r.ajouter_fiche(p.classer_fiche(lf.lire_fiches(A5.en_lignes(A5.contenu())).fiches[0],
                                            identifiant=A5.mot_fiche(k + 1), case=A5.CASE))
        trop = A5.contenu(idee="z" * 1201)
        r.ajouter_fiche(p.classer_fiche(lf.lire_fiches(A5.en_lignes(trop)).fiches[0], identifiant=A5.mot_fiche(9),
                                        case=A5.CASE))
        with pytest.raises(rg.ArretGardeCoffre):  # 2 au coffre sur 4 rendues
            rg.garde_du_coffre(rg.lire_registre_tentatives(r.chemin), 1)
