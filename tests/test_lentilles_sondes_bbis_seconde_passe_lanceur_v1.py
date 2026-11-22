"""Essais du lanceur de la seconde passe (`lanceur_seconde_passe_v1`) et de `montage_v2` : texte de lecture v2 scellé
(`a2bbed7a…`), « Code neuf », essais « poids », « accès » (noms des variables d'environnement), « procédure » (horloge de
10 heures, espace de 8 Go, bout en bout sur un Llama miniature avec de faux fichiers d'ajustement R et S, **une fois par
palier**), et, du brouillon 5, la première passe lancée et non achevée (aucune phrase de la lentille publique). Canal des
messages d'arrêt et garde du fichier d'arrêt déjà présent, repris de `lanceur_v7`. Cas sain et artefact pour chaque garde (R5)."""
from __future__ import annotations

import dataclasses
import json
import sys
from types import SimpleNamespace

import numpy as np
import pytest

torch = pytest.importorskip("torch")
pytest.importorskip("transformers")
pytest.importorskip("safetensors")

import lentilles_sondes_bbis_jouets_v7 as J7  # noqa: E402
import lentilles_sondes_bbis_seconde_passe_jouets_v1 as J1  # noqa: E402
import lentilles_sondes_bbis_seconde_passe_jouets_v2 as J2  # noqa: E402
from controle_ia.lentilles_sondes_bbis import comparaisons_lentilles_v1 as co  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v2 as K2  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_seconde_passe_v1 as la  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v7 as l7  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lecture_entree_v1 as li  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lecture_v1 as le  # noqa: E402
from controle_ia.lentilles_sondes_bbis import montage_v1 as mo  # noqa: E402
from controle_ia.lentilles_sondes_bbis import montage_v2 as m2  # noqa: E402
from controle_ia.lentilles_sondes_bbis import nos_lentilles_v1 as nl  # noqa: E402
from controle_ia.lentilles_sondes_bbis import phrases_v2 as ph  # noqa: E402
from controle_ia.lentilles_sondes_bbis import reproduction_v1 as rp  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v3 as st3  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret, Refus  # noqa: E402
from controle_ia.scellement import verifier  # noqa: E402

R, S, PUB, LOG = K2.LENTILLE_NOTRE_R, K2.LENTILLE_NOTRE_S, K.LENTILLE_PUBLIQUE, K.LENTILLE_LOGITS


@pytest.fixture(scope="module")
def mp():
    patch = pytest.MonkeyPatch()
    yield patch
    patch.undo()


# === bout en bout, premier palier ; première passe jouée avant (reproduction) ================================================================
@pytest.fixture(scope="module")
def premier_palier(tmp_path_factory, mp):
    return J2.jouer(J2.monde(tmp_path_factory.mktemp("premier-palier"), mp, premiere_passe="faite"))


def _tableaux(j) -> dict:
    sortie = {}
    for morceau in j.rendu["morceaux"]:
        chemin = j.monde.ctx.sortie / "donnees" / J2.RUN / morceau["fichier"]
        assert verifier(chemin) == morceau["sha256"]
        with np.load(chemin, allow_pickle=False) as archive:
            sortie |= {n: archive[n] for n in archive.files}
    return sortie


def test_bout_en_bout_premier_palier_fichiers_fermes_scelles_lignes_proposees_et_nettoyage(premier_palier):
    j, ctx = premier_palier, premier_palier.monde.ctx
    for chemin in (j.rendu["tables"]["chemin"], j.rendu["manifeste"]["chemin"], f"diag/{J2.RUN}/{la.NOM_MONTAGE}", f"diag/{J2.RUN}/{la.NOM_ENTREES}"):
        assert verifier(ctx.sortie / chemin)
    assert j.tables["texte"] == {"chemin": K2.TEXTE_V2, "sha256": K2.EMPREINTE_TEXTE_V2} and j.tables["passe"] == "seconde"
    assert [l.split(" | ")[0] for l in j.rendu["lignes_proposees"]] == [f"| {K2.CLE_ENTREES_V2}", f"| {K2.CLE_TABLES_V2}"]
    assert j.ligne_montage.startswith(f"| {K2.CLE_MONTAGE_V2} | ")
    assert not ctx.travail.exists()                                           # nettoyage : nos matrices et les plongements compris
    copies = [p for p in (ctx.sortie / "versement").rglob("*") if p.is_file()]
    assert copies and not any("nos-lentilles" in str(p) or p.suffix == ".brut" for p in copies)
    for p in ctx.sortie.rglob("*"):
        if p.is_file():
            assert J7.FAUSSE_CLE.encode() not in p.read_bytes()


def test_bout_en_bout_premier_palier_les_quatre_lentilles_et_les_moities_sont_lues(premier_palier):
    T = premier_palier.tables
    assert T["nos_lentilles"]["condition_de_lecture"]["R"]["lue"] and T["nos_lentilles"]["condition_de_lecture"]["S"]["palier"] == 1
    for info in T["couches"].values():
        assert set(info["lentilles"]) == {PUB, LOG, R, S} and set(info["moities"]) == set(K2.MOITIES)
        assert info["lentilles"][S]["independance_tenue"] == la.SANS_OBJET_RHO and len(info["empreinte_du_tirage_du_nul_isotrope"]) == 64
    d = next(x for x in T["directions"] if "lectures" in x)
    assert set(d["lectures"]) == {PUB, LOG, R, S}
    e = d["entre_lentilles"]["+"]
    assert set(e) == {"principale", "notre_r_et_logits", "moities", "correlation", "deux_recouvrements"}
    assert 0 <= e["principale"]["recouvrement"] <= 20 and set(e["principale"]["nuls"]) == {K.NUL_ISOTROPE, K.NUL_SIGNES}
    assert set(e["moities"]["nuls"]) == {K.NUL_ISOTROPE} and "mediane_nul_isotrope" in e["correlation"]
    assert set(d["plongements_seuls"]) == {"+", "-"} and len(d["plongements_seuls"]["+"]["ids"]) == 20
    assert "lecture_notre_r" in d["poles"]["poles"][0] and "jetons_communs_entre_les_deux_lentilles_r" in d["poles"]["poles"][0]
    assert set(d["lectures"][R]["temoin_de_couche"]) == {str(c) for c in K.COUCHES} - {str(d["couche"])}
    assert set(d["accord_lentilles"]) == {"publique_et_logits", "notre_r_et_logits"}


def test_bout_en_bout_lectures_de_notre_r_et_de_notre_s_egales_a_un_calcul_direct_a_la_couche_de_la_sonde(premier_palier):
    """Indice de couche : la matrice lue est (S₀[ℓ] + S₁[ℓ]) / (n₀ + n₁) à la couche ℓ de la sonde, pour R et pour S."""
    j = premier_palier
    tableaux, llama = _tableaux(j), j.monde.v7.llama
    ids = tableaux["ids_gardes"]
    wu = llama.etat["lm_head.weight"].float()[torch.as_tensor(ids)]
    e = llama.etat["model.embed_tokens.weight"].float()[torch.as_tensor(ids)]
    gamma = llama.etat["model.norm.weight"].float()
    vus = 0
    for d in j.tables["directions"]:
        if "lectures" not in d or d["vecteur"] != "w":
            continue
        ident = f"{d['cellule']}__{d['pli']}__{d['role']}__w"
        v = _vecteur(j, d)
        for lettre, lentille in (("R", R), ("S", S)):
            s0, s1 = (J2.sommes(lettre)[("out", h)][d["couche"]] for h in (0, 1))
            matrice = (s0 + s1) / 6
            if lettre == "R":
                direct = le.lire(v, matrice, gamma, wu)[0][:, 0]
            else:
                direct = li.lire_entree(v, matrice, li.centrer(e))[0][:, 0]
            assert np.allclose(tableaux[f"scores__{ident}__{lentille}"], direct.numpy(), rtol=1e-5, atol=1e-6)
            assert d["lectures"][lentille]["indice_matrice"] == d["couche"]
            assert d["lectures"][lentille]["empreinte_matrice"] == nl.empreinte_simple_precision(matrice.numpy())
        vus += 1
    assert vus >= 10


def _vecteur(j, d) -> torch.Tensor:
    """Le vecteur `w` d'une sonde jouet, relu dans E-1 par son nom d'entrée (essai : aucune donnée du programme)."""
    with np.load(next(j.monde.entrees.rglob("sondes-bbis.npz")), allow_pickle=False) as archive:
        return torch.from_numpy(archive[f"{d['cellule']}__{d['pli']}__{d['role']}_w"].astype(np.float32))


def test_bout_en_bout_reproduction_de_la_premiere_passe_egale_aucune_reserve(premier_palier):
    r = premier_palier.tables["reproduction_de_la_premiere_passe"]
    assert r["etat"] == rp.ETAT_FAITE and r["nombre_de_lectures_differentes"] == 0 and r["lectures_comparees"] > 0
    assert r["entrees"]["egales_entre_les_deux_passes"] and r["ecart_relatif_maximal_des_scores"] == 0.0
    assert r["premiere_passe_au_montage"] == nl.PREMIERE_PASSE_ACHEVEE and not r["audit_de_symetrie_a_jouer"]
    assert premier_palier.tables["tete"]["reproduction"] == [
        "Reproduction de la première passe : aucune.",
        "code de lecture différent de celui de la première passe : statistiques_v4, lanceur_seconde_passe_v1"]


def test_bout_en_bout_memes_cles_de_graine_que_la_premiere_passe(premier_palier):
    j = premier_palier
    un = json.loads((j.monde.v7.ctx.sortie / "runs" / J7.RUN / "manifeste.json").read_text())
    deux = json.loads((j.monde.ctx.sortie / j.rendu["manifeste"]["chemin"]).read_text())
    assert un["graines"] == {k: v for k, v in deux["graines"].items() if k in un["graines"]} and set(un["graines"]) <= set(deux["graines"])
    assert all(k.startswith("lentilles-bbis/") for k in deux["graines"])       # aucun tirage neuf dans le calcul
    assert deux["preenregistrement"]["sha256"] == K2.EMPREINTE_TEXTE_V2 and set(deux["nos_lentilles"]) == {"R", "S"}
    assert set(deux["code"]) == {f"{m}.py" for m in la.MODULES}


def test_bout_en_bout_comptes_d_egalites_ecrits_et_calibration_du_recouvrement(premier_palier):
    T = premier_palier.tables
    e = T["egalites_a_la_limite"]
    assert e["regle"] == la.st.REGLE_DEPARTAGE and e["total_a_egalite"] == 0
    for couche in map(str, K.COUCHES):
        for lentille in (PUB, LOG, R, S):
            cases = e["listes_de_vingt"][couche][lentille]
            assert {"lue"} <= set(cases[la.st.LISTE_PAR_SCORE]) and {"nulle", "temoin"} <= set(cases[K.NUL_ISOTROPE])
        assert e["listes_de_dix"]["poles_par_cosinus"][couche]["lue"]["listes"] > 0
        assert f"{couche}/{R}" in e["listes_de_dix"]["jetons_d_un_pole"] and f"{couche}/{PUB}" in e["listes_de_dix"]["jetons_d_un_pole"]
        cal = T["couches"][couche]["calibration_du_recouvrement"]
        assert set(cal) == {K.NUL_ISOTROPE, K.NUL_SIGNES} and all(c["q_bas"] == co.SANS_OBJET_BORNE_BASSE for c in cal.values())
    comptes = T["comptes_de_libelles"]
    assert comptes["nombre_total_de_lectures"] == 4 * 2 * sum(1 for d in T["directions"] if "lectures" in d)
    assert comptes["comparaisons_entre_lentilles"]["nombre_de_lectures_comparees"] == 2 * sum(1 for d in T["directions"] if "lectures" in d)


def test_bout_en_bout_phrases_de_la_seconde_passe_une_par_libelle_et_tete_dans_l_ordre(premier_palier):
    p, T = premier_palier.phrases, premier_palier.tables
    tete = p["tete"]
    assert tete["phrase_de_tete"] == ph.PHRASE_DE_TETE_V2 and tete["issue_des_noeuds"] == [] and tete["domaine_d_usage"] == ph.PHRASE_DOMAINE_D_USAGE
    assert tete["verdict_d_identite"] == (f"Verdict d'identité : notre R : {K2.PALIER_1} ; notre S : {K2.PALIER_1}. Course du "
                                          "réajustement : ajustement seul.")
    assert [l["forme"] for l in tete["phrases_permises"]] == ["deux au premier palier"] and len(tete["verdict_d_ensemble"]) == 1
    lentilles = {l["lentille"] for l in p["directions"] if "lentille" in l}
    assert lentilles == {PUB, LOG, R, S}
    par_s = [l for l in p["directions"] if l.get("lentille") == S and not l.get("poles")]
    assert all(l["phrases"][0].startswith("Par notre lentille S côté entrée,") and l["renvois"] == ["(R-d)", "(R-u)"] for l in par_s)
    par_r = [l for l in p["directions"] if l.get("lentille") == R and not l.get("poles")]
    assert all(l["phrases"][0].startswith("Par notre lentille R,") for l in par_r)
    n = sum(1 for d in T["directions"] if "lectures" in d)
    assert len(p["comparaisons_entre_lentilles"]) == 2 * n and all(c["phrase"] for c in p["comparaisons_entre_lentilles"])
    for ligne in p["directions"] + p["comparaisons_entre_lentilles"]:
        for phrase in ligne.get("phrases", [ligne.get("phrase")]):
            assert "détecte" not in phrase and "valide" not in phrase
    assert any(c["lentille"] == R for c in p["comparaisons"]) and any(c["lentille"] == S for c in p["comparaisons"])


def test_ligne_de_commande_phrases_sur_les_tables_fermees(premier_palier, tmp_path, capsys):
    ctx = premier_palier.monde.ctx
    code = la.principal(["phrases", "--tables", str(ctx.sortie / premier_palier.rendu["tables"]["chemin"]),
                         "--sortie", str(tmp_path / "lecture-lentilles-bbis-v2.json")])
    assert code == 0 and "sha256" in json.loads(capsys.readouterr().out)
    assert json.loads((tmp_path / "lecture-lentilles-bbis-v2.json").read_text())["tete"]["phrase_de_tete"] == ph.PHRASE_DE_TETE_V2


# === bout en bout, deuxième palier ; première passe jamais lancée ; garde du rapport à ε levée ===============================================
@pytest.fixture(scope="module")
def deuxieme_palier(tmp_path_factory, mp):
    return J2.jouer(J2.monde(tmp_path_factory.mktemp("deuxieme-palier"), mp, r="p2", s="p2", variante=K2.VARIANTE_COURSE_REJOUEE,
                             seconde_course=K2.SECONDE_COURSE_ENTIERE, plus=("avertissement", "lecture_seconde_course"),
                             echelles={("P-S75", "e1", "sonde"): 1e-5}))


def test_bout_en_bout_deuxieme_palier_phrase_permise_verdict_d_ensemble_et_renvois(deuxieme_palier):
    tete, p = deuxieme_palier.phrases["tete"], deuxieme_palier.phrases
    assert "Course du réajustement : course rejouée." in tete["verdict_d_identite"] and K2.PALIER_2 in tete["verdict_d_identite"]
    permise = tete["phrases_permises"][0]
    assert permise["forme"] == "deux au deuxième palier" and permise["lentilles"] == ["R", "S"]
    assert permise["phrases"][0].startswith("Les deux lentilles mesurées le 18 novembre ont été détruites")
    assert permise["phrases"][0].endswith("Les mesures du 18 novembre ont été refaites sur elles et sont rapportées à côté.")
    ensemble = tete["verdict_d_ensemble"]
    assert len(ensemble) == 1 and ensemble[0]["palier"] == 2 and "Ce verdict ne se transporte pas à la lentille lue ici." in ensemble[0]["texte"]
    par_s = next(l for l in p["directions"] if l.get("lentille") == S)
    assert par_s["renvois"] == ["(R-d) — voir la lecture de la seconde course : « partiel », seconde course", "(R-u)"]


def test_bout_en_bout_premiere_passe_jamais_lancee_la_seconde_la_remplace_et_c_est_ecrit(deuxieme_palier):
    r = deuxieme_palier.tables["reproduction_de_la_premiere_passe"]
    assert r["etat"] == rp.ETAT_REMPLACEE and r["premiere_passe_au_montage"] == nl.PREMIERE_PASSE_JAMAIS_LANCEE
    assert deuxieme_palier.phrases["tete"]["reproduction"][0] == ph.NOTE_PREMIERE_PASSE_REMPLACEE
    assert any(l.get("lentille") == PUB for l in deuxieme_palier.phrases["directions"])


def test_bout_en_bout_garde_du_rapport_a_epsilon_nuls_refaits_pour_trois_lentilles_moities_non_calculables(deuxieme_palier):
    T = deuxieme_palier.tables
    replis = {c: info for c, info in T["couches"].items() if info["repli_nuls_par_direction"]}
    sains = {c: info for c, info in T["couches"].items() if not info["repli_nuls_par_direction"]}
    assert replis and sains                                                    # une couche lève la garde, les autres non
    par = K.NUL_ISOTROPE_PAR_DIRECTION
    for couche, info in replis.items():
        assert info["garde_du_rapport_a_epsilon"]["lentilles_refaites"] == [PUB, LOG, R]
        for d in (x for x in T["directions"] if "lectures" in x and str(x["couche"]) == couche):
            for lentille in (PUB, LOG, R):
                t = d["lectures"][lentille]["signes"]["+"]
                assert t["nul_isotrope_en_vigueur"] == par and t["nuls"][K.NUL_ISOTROPE].get("remplacee") is True and par in t["nuls"]
            t = d["lectures"][S]["signes"]["+"]
            assert t["nul_isotrope_en_vigueur"] == K.NUL_ISOTROPE and par not in t["nuls"]         # notre S n'est pas concernée
            e = d["entre_lentilles"]["+"]
            assert e["moities"]["libelle"] == co.NON_CALCULABLE and e["moities"]["motif"] == co.MOTIF_NUL_REFAIT
            assert par in e["principale"]["nuls"] and e["principale"]["nuls"][K.NUL_ISOTROPE]["remplacee"] is True
        assert set(info["calibration_du_recouvrement"]) == {K.NUL_ISOTROPE, par, K.NUL_SIGNES}
    for couche, info in sains.items():
        d = next(x for x in T["directions"] if "lectures" in x and str(x["couche"]) == couche)
        assert par not in d["lectures"][PUB]["signes"]["+"]["nuls"] and "nuls" in d["entre_lentilles"]["+"]["moities"]
    assert deuxieme_palier.phrases["tete"]["independance_a_la_norme"].startswith("Indépendance à la norme non tenue à couche ")


# === première passe lancée et non achevée ; une lentille lue, l'autre non =====================================================================
@pytest.fixture(scope="module")
def non_achevee(tmp_path_factory, mp):
    return J2.jouer(J2.monde(tmp_path_factory.mktemp("non-achevee"), mp, r="p1", s="autre", premiere_passe="entrees"))


def test_premiere_passe_lancee_et_non_achevee_aucune_phrase_de_la_lentille_publique_ni_des_logits(non_achevee):
    """Artefact visé : un code qui remplace la première passe dans ce cas ; la présence d'une phrase de la lentille publique ou
    de la lentille des logits dans la sortie est un échec."""
    p, T = non_achevee.phrases, non_achevee.tables
    assert T["reproduction_de_la_premiere_passe"]["etat"] == rp.ETAT_NON_FAITE
    assert p["tete"]["reproduction"] == [ph.PHRASE_REPRODUCTION_NON_FAITE]
    assert not any(l.get("lentille") in (PUB, LOG) for l in p["directions"] + p["comparaisons"])
    texte = json.dumps([l.get("phrases") for l in p["directions"]] + [c["phrase"] for c in p["comparaisons"]], ensure_ascii=False)
    assert "Par la lentille publique" not in texte and "Par la lentille des logits" not in texte and "la lentille publique les lit" not in texte
    assert any(l.get("lentille") == R for l in p["directions"])                # notre R reste lue et phrasée
    assert p["comparaisons_entre_lentilles"] and all(c["phrase"] for c in p["comparaisons_entre_lentilles"])   # comparaisons rendues
    d = next(x for x in T["directions"] if "lectures" in x)
    assert PUB in d["lectures"] and LOG in d["lectures"]                       # lues pour les seules comparaisons entre lentilles


def test_une_lentille_non_lue_l_autre_et_la_lentille_publique_restent_lues_motif_ecrit_en_tete(non_achevee):
    T, tete = non_achevee.tables, non_achevee.phrases["tete"]
    assert tete["non_lues"] == ["Non lue : notre lentille S au verdict d'identité « différente »"] and tete["domaine_d_usage"] is None
    assert [l["forme"] for l in tete["phrases_permises"]] == ["une seule au premier palier", "tout autre verdict"]
    assert "seules les mesures faites sur notre lentille R la décrivent" in tete["verdict_d_ensemble"][0]["texte"]
    for info in T["couches"].values():
        assert info["notre_r_lue"] and not info["notre_s_lue"] and S in info["lentilles_non_lues"] and S not in info["lentilles"]
    assert all(S not in d["lectures"] and "plongements_seuls" not in d for d in T["directions"] if "lectures" in d)
    assert non_achevee.montage["nos_lentilles"]["S"] == {"lue": False, "motif": tete["non_lues"][0]}
    assert not any(K2.FICHIER_AJUSTEMENT["S"] in appel[1] for appel in non_achevee.monde.transport.appels)   # son fichier n'est pas demandé


# === gardes de procédure, sur un monde non monté ==============================================================================================
@pytest.fixture(scope="module")
def nu_monde(tmp_path_factory, mp):
    return J2.monde(tmp_path_factory.mktemp("non-monte"), mp)


def _ctx(m, nom, **plus):
    return dataclasses.replace(m.ctx, travail=m.tmp / f"travail-{nom}", sortie=m.tmp / f"sortie-{nom}", **plus)


def test_horloge_de_10_heures_saine_a_9_heures_arret_au_dela(nu_monde, tmp_path):
    assert la.Reglages().horloge_s == 10 * 3600 and K.HORLOGE_S == 8 * 3600
    instant = {"t": 0.0}
    ctx = _ctx(nu_monde, "horloge", maintenant=lambda: instant["t"], reglages=dataclasses.replace(nu_monde.reglages, horloge_s=10 * 3600))
    ctx = dataclasses.replace(ctx, travail=tmp_path)
    horloge = la._horloge(ctx)
    instant["t"] = 9 * 3600.0
    horloge.controler("sain")                                                  # au-delà de 8 h, sous 10 h : pas d'arrêt
    instant["t"] = 10 * 3600.0 + 1
    with pytest.raises(Arret, match="au-delà de 10 h"):
        horloge.controler("artefact")


def test_espace_sous_8_go_au_depart_arret_sans_rien_creer(nu_monde):
    assert la.Reglages().disque_depart == 8 * 10 ** 9
    ctx = _ctx(nu_monde, "disque", reglages=dataclasses.replace(nu_monde.reglages, disque_depart=8 * 10 ** 9),
               mesure_disque=lambda chemin: type("D", (), {"free": 8 * 10 ** 9 - 1})())
    with pytest.raises(Arret, match="8 Go exigés"):
        la.monter(ctx)
    assert not ctx.travail.exists()
    assert l7.exiger_disque(nu_monde.tmp, 8 * 10 ** 9, "au départ", lambda chemin: type("D", (), {"free": 8 * 10 ** 9})()) == 8 * 10 ** 9


class _EnvPiege(dict):
    """Environnement jouet : lire la valeur d'une variable dont le nom ressemble à une clé, autre que `HF_TOKEN`, est un échec."""

    def __getitem__(self, nom):
        assert nom == K.NOM_CLE or "TOKEN" not in nom, f"valeur de {nom} lue"
        return super().__getitem__(nom)

    def get(self, nom, defaut=None):
        assert nom == K.NOM_CLE or "TOKEN" not in nom, f"valeur de {nom} lue"
        return super().get(nom, defaut)

    def items(self):
        raise AssertionError("valeurs de l'environnement lues")

    values = items


@pytest.mark.parametrize("nom", ["HF_TOKEN_ECRITURE", "HUGGINGFACE_HUB_TOKEN", "HUGGING_FACE_TOKEN", "hf_token_2"])
def test_variable_d_environnement_d_un_nom_de_cle_de_plus_arret_valeur_jamais_lue(nu_monde, nom):
    env = _EnvPiege({K.NOM_CLE: J7.FAUSSE_CLE, nom: "valeur-qui-ne-doit-pas-etre-lue", "PATH": "/usr/bin"})
    with pytest.raises(Arret, match="autre que HF_TOKEN") as e:
        m2.exiger_noms_des_variables(env)
    assert nom in str(e.value) and "valeur-qui" not in str(e.value)
    ctx = _ctx(nu_monde, f"env-{nom}", env=env)
    with pytest.raises(Arret, match="autre que HF_TOKEN"):
        la.monter(ctx)
    assert not ctx.travail.exists()


def test_cas_sain_hf_token_seule():
    assert m2.exiger_noms_des_variables(_EnvPiege({K.NOM_CLE: "x", "PATH": "/usr/bin", "TOKENIZERS_PARALLELISM": "false"})) == [K.NOM_CLE]
    assert m2.exiger_noms_des_variables({"PATH": "/usr/bin"}) == []


def test_plongements_absents_de_l_index_ou_d_une_autre_forme_arret_et_cas_sain(nu_monde):
    index = nu_monde.v7.llama.index
    m2.exiger_plongements_dans_l_index(index)                                  # cas sain : faux index complet
    carte = json.loads(index)
    del carte["weight_map"][K2.TENSEUR_PLONGEMENTS]
    with pytest.raises(Arret, match="model.embed_tokens.weight absent de l'index"):
        m2.exiger_plongements_dans_l_index(json.dumps(carte).encode())
    with pytest.raises(Arret, match="index des poids illisible"):
        m2.exiger_plongements_dans_l_index(b"{")
    m2.exiger_forme_des_plongements({"shape": [128256, 4096]})
    with pytest.raises(Arret, match="d'une autre forme que 128256 × 4096"):
        m2.exiger_forme_des_plongements({"shape": [128256, 2048]})
    assert K2.TENSEUR_PLONGEMENTS in m2.TENSEURS_GARDES_V2 and set(K.TENSEURS_GARDES) < set(m2.TENSEURS_GARDES_V2)
    assert m2.cle_tie_word_embeddings(b'{"tie_word_embeddings": false}') is False and m2.cle_tie_word_embeddings(b"x") is None


def test_montage_plongements_absents_de_l_index_arret_avant_tout_flux_de_poids(tmp_path, mp):
    m = J2.monde(tmp_path, mp)
    carte = json.loads(m.v7.llama.index)
    del carte["weight_map"][K2.TENSEUR_PLONGEMENTS]
    index = json.dumps(carte).encode()
    r = m.reglages
    m.transport.fichiers[mo.url_fichier(r.depot_llama, r.revision_llama, K.INDEX_LLAMA)] = index
    petits = dict(r.petits) | {K.INDEX_LLAMA: (len(index), mo.identifiant_git(index))}
    ctx = dataclasses.replace(m.ctx, reglages=dataclasses.replace(r, petits=petits))
    with pytest.raises(Arret, match="absent de l'index"):
        la.monter(ctx)
    assert not any(a[0] == "flux" and "safetensors" in a[1] for a in m.transport.appels)


def test_cibles_du_corpus_jamais_celles_de_montage_v1_telles_quelles(nu_monde, monkeypatch):
    """Nœud du développeur : sans fonction branchée ni module de lecture paginée, rien ne part."""
    monkeypatch.setitem(sys.modules, "controle_ia.lentilles_sondes_bbis.corpus_pagine_v1", None)
    # Correction du 22 novembre 2026 (R-5010) : un lanceur v8 ou v9 importé plus tôt dans le processus pose l'attribut
    # `corpus_pagine_v1` sur le paquet, que `from . import corpus_pagine_v1` lit avant `sys.modules` ; on le retire aussi.
    monkeypatch.delattr(sys.modules["controle_ia.lentilles_sondes_bbis"], "corpus_pagine_v1", raising=False)
    with pytest.raises(Arret, match="n'est pas branchée"):
        m2.cibles_du_corpus(nu_monde.tmp, nu_monde.transport)
    assert m2.cibles_du_corpus(nu_monde.tmp, nu_monde.transport, lambda voisin, transport: ["cible jouet"]) == ["cible jouet"]
    assert la.Reglages().cibles_corpus is None


def test_fiche_du_code_de_la_seconde_passe_saine_et_artefacts(nu_monde):
    m = nu_monde
    sain = la.exiger_fiche_code(m.depot, m.registre_propre)
    assert sain["code_de_lecture_different_de_la_premiere_passe"] == ["statistiques_v4", "lanceur_seconde_passe_v1"]
    assert set(sain["essai_de_la_forme_de_l_archive"]) == {"script", "sortie"}
    fiche = m.depot / J2.FICHE_CODE
    origine = fiche.read_bytes()
    try:
        for plus, motif in ((dict(code_de_lecture_different_de_la_premiere_passe=[]), "non déclarés"),
                            (dict(essai_de_la_forme_de_l_archive=None), "essai opposable"),
                            (dict(addendum_concentration={"chemin": K2.ADDENDUM, "sha256": "0" * 64}), "addendum de concentration"),
                            (dict(fichiers={}), "empreinte absente de la fiche")):
            J2.ecrire_fiche_code(m.depot, **plus)
            with pytest.raises(Refus, match="autre empreinte que la ligne"):   # la ligne du registre cite l'ancienne fiche
                la.exiger_fiche_code(m.depot, m.registre_propre)
            texte = m.registre_propre.read_text(encoding="utf-8")
            ligne = next(l for l in texte.splitlines() if l.startswith(f"| {K2.CLE_CODE_V2} |"))
            m.registre_propre.write_text(texte.replace(ligne, f"| {K2.CLE_CODE_V2} | {J1.H['code_v2']} | {J2.FICHE_CODE} | {J1.sha(fiche.read_bytes())} |"))
            try:
                with pytest.raises(Refus, match=motif):
                    la.exiger_fiche_code(m.depot, m.registre_propre)
            finally:
                m.registre_propre.write_text(texte)
    finally:
        fiche.write_bytes(origine)
    assert la.exiger_fiche_code(m.depot, m.registre_propre) == sain


def test_montage_et_calcul_refuses_sans_les_lignes_de_la_v2(tmp_path, mp):
    m = J2.monde(tmp_path, mp)
    texte = m.registre_propre.read_text(encoding="utf-8")
    for cle in (K2.CLE_SCELLEMENT_V2, K2.CLE_GO_V2, K2.CLE_CODE_V2, K2.CLE_RANGEMENT):
        m.registre_propre.write_text("\n".join(l for l in texte.splitlines() if not l.startswith(f"| {cle} |")) + "\n")
        with pytest.raises(Refus, match=cle):
            la.monter(m.ctx)
        with pytest.raises(Refus, match=cle):
            la.calculer(m.ctx, m.entrees, m.registre_bbis)
        assert not m.ctx.travail.exists() and not m.ctx.sortie.exists()
    assert la.ligne_registre(K2.CLE_TABLES_V2, "diag/x.json", "0" * 64, "2026-11-23T00:00:00Z") == f"| {K2.CLE_TABLES_V2} | 2026-11-23T00:00:00Z | diag/x.json | {'0' * 64} |"
    with pytest.raises(Refus, match="hors des clés ajoutées par la v2"):
        la.ligne_registre("TABLES-LENTILLES-BBIS", "diag/x.json", "0" * 64)


def test_fichier_d_une_lentille_introuvable_a_la_revision_arret_avant_tout_flux_long_aucun_repli(tmp_path, mp):
    m = J2.monde(tmp_path, mp)
    l = m.lentilles["R"]
    url = mo.url_fichier(l["depot"], l["revision"], l["chemin"])
    m.transport.fichiers[mo.url_fichier(l["depot"], "f" * 40, l["chemin"])] = m.transport.fichiers.pop(url)   # présent à une autre révision
    with pytest.raises(Arret, match="essai d'un octet refusé"):
        la.monter(m.ctx)
    assert not any(a[0] == "flux" for a in m.transport.appels) and not any("f" * 40 in a[1] for a in m.transport.appels)


# === canal des messages d'arrêt et garde du fichier d'arrêt déjà présent ======================================================================
def test_une_seule_fonction_decide_de_la_ligne_affichee_mots_fixes_pour_un_arret_cloisonne():
    assert la.ligne_affichee(Arret("espace disque : arrêt")) == "ARRÊT : espace disque : arrêt"
    cloisonne = st3.EgaliteDirectionLue("vingt premiers jetons par score", (4242, 4343), 0.123456, {"cellule": "P-S50"})
    ligne = la.ligne_affichee(cloisonne)
    assert ligne == "ARRÊT : EgaliteDirectionLue ; fichier d'arrêt non écrit"
    assert "4242" not in ligne and "0.123456" not in ligne and "P-S50" not in ligne
    assert la.ARRETS_CLOISONNES is l7.ARRETS_CLOISONNES and la.exiger_aucun_fichier_d_arret is l7.exiger_aucun_fichier_d_arret


def test_garde_du_fichier_d_arret_deja_present_rien_ne_part_rien_n_est_ecrit(nu_monde):
    ctx = _ctx(nu_monde, "arret-present")
    fichier = la.chemin_du_fichier_d_arret(ctx)
    fichier.parent.mkdir(parents=True)
    fichier.write_text("{}")
    avant = sorted(str(p) for p in ctx.sortie.rglob("*"))
    with pytest.raises(Arret, match="un fichier d'arrêt existe déjà pour cette course"):
        la.calculer(ctx, nu_monde.entrees, nu_monde.registre_bbis)
    assert sorted(str(p) for p in ctx.sortie.rglob("*")) == avant and fichier.read_text() == "{}"


def test_arret_cloisonne_verse_dans_le_seul_fichier_d_arret_par_l_enveloppe(nu_monde, monkeypatch, capsys):
    """Défense : si un arrêt cloisonné était levé dans le calcul de la seconde passe, son message irait dans le seul
    `arret.json` ; la ligne de commande n'en afficherait que des mots fixes."""
    ctx = _ctx(nu_monde, "cloisonne")
    secret = st3.EgaliteDirectionLue("vingt premiers jetons par score", (4242, 4343), 0.123456, {"cellule": "P-S50"})

    def leve(*a, **k):
        raise secret
    monkeypatch.setattr(la, "_calculer", leve)
    monkeypatch.setattr(la, "Contexte", lambda *a: ctx)
    code = la.principal(["calcul", "--travail", str(ctx.travail), "--sortie", str(ctx.sortie), "--run", J2.RUN,
                         "--registre-propre", str(nu_monde.registre_propre), "--entrees", str(nu_monde.entrees),
                         "--registre-bbis", str(nu_monde.registre_bbis)])
    sortie = capsys.readouterr()
    assert code == 3 and sortie.out == "" and "4242" not in sortie.err and "0.123456" not in sortie.err
    assert sortie.err.strip() == f"ARRÊT : EgaliteDirectionLue ; fichier d'arrêt : {la.chemin_du_fichier_d_arret(ctx)}"
    assert "4242" in json.loads(la.chemin_du_fichier_d_arret(ctx).read_text())["motif"]


def test_ligne_de_commande_arret_ordinaire_code_3_sans_trace(tmp_path, mp, capsys):
    m = J2.monde(tmp_path, mp)
    m.registre_propre.write_text("# vide\n")
    code = la.principal(["montage", "--travail", str(tmp_path / "t"), "--sortie", str(tmp_path / "s"), "--run", J2.RUN,
                         "--depot", str(m.depot), "--registre-propre", str(m.registre_propre)])
    sortie = capsys.readouterr()
    assert code == 3 and sortie.err.startswith("ARRÊT : ") and "Traceback" not in sortie.err and sortie.out == ""


def test_etat_de_la_premiere_passe_en_vigueur_celui_du_montage():
    f = la._premiere_passe_en_vigueur
    J, N, A = nl.PREMIERE_PASSE_JAMAIS_LANCEE, nl.PREMIERE_PASSE_NON_ACHEVEE, nl.PREMIERE_PASSE_ACHEVEE
    assert f(J, J) == (J, None) and f(A, A) == (A, None) and f(N, N) == (N, None)
    assert f(N, A)[0] == N and "la reproduction n'est pas faite" in f(N, A)[1]      # passe encore en cours au montage, achevée depuis
    assert f(J, N)[0] == N and f(J, A)[0] == N and "n'est pas remplacée" in f(J, A)[1]


def test_calcul_refuse_si_une_lentille_lue_n_a_pas_ete_montee_ou_si_le_montage_manque(nu_monde):
    ctx = _ctx(nu_monde, "sans-montage")
    with pytest.raises(Arret, match="dossier de travail monté absent"):
        la.calculer(ctx, nu_monde.entrees, nu_monde.registre_bbis)
    assert la.MODULES_DIFFERENTS == ("statistiques_v4", "lanceur_seconde_passe_v1") and "lanceur_v7" in la.MODULES
    assert not {"corpus_pagine_v1", "lanceur_v8"} & set(la.MODULES)


def _monte_a_la_main(m, nom, monkeypatch, nos, sha_fiche):
    """Un dossier de travail marqué et un rapport de montage posés à la main, et un montage chargé jouet : ce qu'il faut
    pour atteindre, sans montage long, les deux gardes du calcul sur ce qui a été monté."""
    ctx = _ctx(m, nom)
    ctx.travail.mkdir(parents=True)
    (ctx.travail / la.MARQUE).write_text("jouet\n")
    rapport = ctx.sortie / "diag" / ctx.run / la.NOM_MONTAGE
    rapport.parent.mkdir(parents=True)
    rapport.write_text("{}")
    charge = SimpleNamespace(nos=nos, etat={"fiche_de_rangement": {"sha256": sha_fiche}, "premiere_passe_au_montage": "jamais"})
    monkeypatch.setattr(la, "charger_montage", lambda _ctx: charge)
    return ctx


def test_calcul_refuse_quand_une_lentille_lue_n_a_pas_ete_montee(nu_monde, monkeypatch):
    """Artefact : le registre et la fiche disent notre S lue, le montage ne l'a pas montée (elle ne l'était pas alors)."""
    fiche = la._lecture(nu_monde.ctx, nu_monde.registre_propre)[2]
    ctx = _monte_a_la_main(nu_monde, "non-montee", monkeypatch, {"R": object()}, fiche["_ligne"]["sha256"])
    with pytest.raises(Arret, match="notre lentille S est lue selon le registre et la fiche, et n'a pas été montée"):
        la.calculer(ctx, nu_monde.entrees, nu_monde.registre_bbis)
    assert not (ctx.sortie / "diag" / ctx.run / la.NOM_TABLES).exists()


def test_calcul_refuse_quand_la_fiche_de_rangement_n_est_plus_celle_du_montage(nu_monde, monkeypatch):
    ctx = _monte_a_la_main(nu_monde, "autre-fiche", monkeypatch, {"R": object(), "S": object()}, "0" * 64)
    with pytest.raises(Arret, match="fiche de rangement différente de celle du montage"):
        la.calculer(ctx, nu_monde.entrees, nu_monde.registre_bbis)
    assert not (ctx.sortie / "diag" / ctx.run / la.NOM_TABLES).exists()
