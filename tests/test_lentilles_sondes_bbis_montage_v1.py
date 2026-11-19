"""Essais du montage (texte scellé, « Code neuf », essais « montage ») : chaque garde, un cas sain et un artefact (R5)."""
from __future__ import annotations

import json
import logging

import numpy as np
import pytest

torch = pytest.importorskip("torch")
pytest.importorskip("transformers")
pytest.importorskip("safetensors")

import lentilles_sondes_bbis_jouets_v1 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v1 as la  # noqa: E402
from controle_ia.lentilles_sondes_bbis import montage_v1 as mo  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret  # noqa: E402


# --- clé ------------------------------------------------------------------------------------------------------------------------------------
def test_cle_presente_lue_par_son_nom_et_masquee(capsys):
    cle = mo.lire_cle({K.NOM_CLE: J.FAUSSE_CLE})
    assert cle.valeur() == J.FAUSSE_CLE
    print(cle, repr(cle), f"{cle}", [cle], {"cle": cle})
    assert J.FAUSSE_CLE not in capsys.readouterr().out
    with pytest.raises(Arret):
        import pickle
        pickle.dumps(cle)
    with pytest.raises(TypeError):
        json.dumps({"cle": cle})


@pytest.mark.parametrize("env", [{}, {K.NOM_CLE: ""}, {K.NOM_CLE: "   "}, {"AUTRE": J.FAUSSE_CLE}])
def test_cle_absente_ou_vide_arret_sans_impression(env, capsys):
    with pytest.raises(Arret, match="absente ou vide") as e:
        mo.lire_cle(env)
    sortie = capsys.readouterr()
    assert sortie.out == "" and sortie.err == "" and J.FAUSSE_CLE not in str(e.value)


def test_environnement_enfant_sans_la_cle():
    e = mo.environnement_enfant("/v", "/h", True, {K.NOM_CLE: J.FAUSSE_CLE, "HUGGING_FACE_HUB_TOKEN": J.FAUSSE_CLE, "PATH": "/bin"})
    assert J.FAUSSE_CLE not in json.dumps(e) and e["HF_HUB_OFFLINE"] == "1" and e["NEURON_LENS_MODEL"] == K.DEPOT_LLAMA
    assert "HF_HUB_OFFLINE" not in mo.environnement_enfant("/v", "/h", False, {"HF_HUB_OFFLINE": "1"})


# --- mode de débogage -----------------------------------------------------------------------------------------------------------------------
def test_sans_debogage_sain():
    mo.exiger_sans_debogage({"HF_DEBUG": "0", "HF_HUB_VERBOSITY": "warning"})
    mo.exiger_sans_debogage({})


@pytest.mark.parametrize("env", [{"HF_DEBUG": "1"}, {"HF_DEBUG": "true"}, {"HF_HUB_VERBOSITY": "debug"}, {"HF_HUB_VERBOSITY": "DEBUG"}])
def test_mode_de_debogage_par_variable_arret(env):
    with pytest.raises(Arret, match="débogage"):
        mo.exiger_sans_debogage(env)


@pytest.mark.parametrize("journal", ["urllib3", "httpx", "requests", "huggingface_hub"])
def test_mode_de_debogage_par_journalisation_arret(journal):
    j = logging.getLogger(journal)
    ancien = j.level
    j.setLevel(logging.DEBUG)
    try:
        with pytest.raises(Arret, match="débogage"):
            mo.exiger_sans_debogage({})
    finally:
        j.setLevel(ancien)
    mo.exiger_sans_debogage({})


def test_mode_de_debogage_http_client_arret(monkeypatch):
    import http.client
    monkeypatch.setattr(http.client.HTTPConnection, "debuglevel", 1)
    with pytest.raises(Arret, match="débogage"):
        mo.exiger_sans_debogage({})


# --- essais d'un octet ------------------------------------------------------------------------------------------------------------------------
def _cibles():
    return [mo.Cible("lentille publique", "https://hote/lentille"), mo.Cible("poids à porte", "https://hote/poids", avec_cle=True),
            mo.Cible("voisin", "https://hote/voisin", sorte="en-tête")]


def test_essais_un_octet_sains():
    t = J.TransportSimule({"https://hote/lentille": b"abc", "https://hote/poids": b"def", "https://hote/voisin": b"refs"},
                          a_porte={"https://hote/poids"})
    faits = mo.essais_un_octet(t, mo.Cle(J.FAUSSE_CLE), _cibles())
    assert [f["octets"] for f in faits] == [1, 1, 1] and all(f["tenu"] for f in faits)
    assert [(a[1], a[2], a[3], a[4]) for a in t.appels] == [("https://hote/lentille", False, 0, 0), ("https://hote/poids", True, 0, 0),
                                                           ("https://hote/voisin", False, 0, 0)]


@pytest.mark.parametrize("refuse", ["https://hote/lentille", "https://hote/poids", "https://hote/voisin"])
def test_essai_un_octet_refuse_par_un_hote_simule_arret(refuse):
    t = J.TransportSimule({"https://hote/lentille": b"abc", "https://hote/poids": b"def", "https://hote/voisin": b"refs"},
                          refus={refuse})
    with pytest.raises(Arret, match="avant tout téléchargement long") as e:
        mo.essais_un_octet(t, mo.Cle(J.FAUSSE_CLE), _cibles())
    assert J.FAUSSE_CLE not in str(e.value)
    assert not any(a[0] == "flux" for a in t.appels)


def test_fichier_a_porte_refuse_avec_une_mauvaise_cle_arret():
    t = J.TransportSimule({"https://hote/poids": b"def"}, a_porte={"https://hote/poids"})
    with pytest.raises(Arret, match="avant tout téléchargement long"):
        mo.essais_un_octet(t, mo.Cle("hf_mauvaise"), [mo.Cible("poids à porte", "https://hote/poids", avec_cle=True)])


def test_transport_reel_n_envoie_la_cle_qu_a_hugging_face():
    t = mo.TransportRequests.__new__(mo.TransportRequests)
    with pytest.raises(Arret, match="hôte de Hugging Face"):
        t._ouvrir("https://ailleurs.exemple/fichier", mo.Cle(J.FAUSSE_CLE), None, None, False)


# --- identifiants git, pointeurs, licences ----------------------------------------------------------------------------------------------------
def test_identifiant_git_connu_et_pointeur_de_la_lentille_publique():
    assert mo.identifiant_git(b"") == "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"          # objet vide de git
    assert mo.identifiant_git(b"hello\n") == "ce013625030ba8dba906f756967f9e9ca394464a"
    # valeurs du texte et de l'arbre versé : SHA-256 et taille de la lentille publique → identifiant git de son pointeur
    assert mo.identifiant_git(mo.pointeur(K.SHA256_LENTILLE, K.TAILLE_LENTILLE)) == K.POINTEUR_LENTILLE
    assert len(mo.pointeur(K.SHA256_LENTILLE, K.TAILLE_LENTILLE)) == 135                      # « pointerSize » de l'arbre versé
    mo.exiger_pointeur("lentille", K.SHA256_LENTILLE, K.TAILLE_LENTILLE, K.POINTEUR_LENTILLE, K.TAILLE_LENTILLE)


def test_pointeur_identifiant_git_faux_ou_taille_fausse_arret():
    with pytest.raises(Arret, match="identifiant git du pointeur"):
        mo.exiger_pointeur("poids", "b" * 64, K.TAILLE_LENTILLE, K.POINTEUR_LENTILLE, K.TAILLE_LENTILLE)
    with pytest.raises(Arret, match="identifiant git du pointeur"):
        mo.exiger_pointeur("poids", K.SHA256_LENTILLE, K.TAILLE_LENTILLE, "0" * 40, K.TAILLE_LENTILLE)
    with pytest.raises(Arret, match="taille"):
        mo.exiger_pointeur("poids", K.SHA256_LENTILLE, K.TAILLE_LENTILLE + 1, K.POINTEUR_LENTILLE, K.TAILLE_LENTILLE)


def test_notice_versee_de_la_lentille_a_l_identifiant_git_du_texte():
    notice = (J.RACINE / "docs/sources/neuron-lens-lecture-20261113/huggingface/neuronpedia-llama3.1-8b-it-NOTICE.txt").read_bytes()
    taille, ident = K.LICENCES_LENTILLE["llama3.1-8b-it/NOTICE"]
    assert len(notice) == taille and mo.identifiant_git(notice) == ident


def test_licence_saine_et_alteree_d_un_octet():
    licence = b"texte de licence jouet\n"
    t = J.TransportSimule({"u": licence, "v": licence[:-2] + b"X\n"})
    assert mo.telecharger_petit(t, "u", "LICENSE", len(licence), mo.identifiant_git(licence)) == licence
    with pytest.raises(Arret, match="LICENSE"):
        mo.telecharger_petit(t, "v", "LICENSE", len(licence), mo.identifiant_git(licence))


def test_sha256_par_interface_et_fichier_sans_empreinte_de_stockage():
    arbre = [{"type": "file", "path": "a.safetensors", "lfs": {"oid": "c" * 64, "size": 10}}, {"type": "file", "path": "petit.json"}]
    t = J.TransportSimule({mo.url_arbre("d/m", "rev"): json.dumps(arbre).encode()})
    assert mo.sha256_par_interface(t, "d/m", "rev", None, ("a.safetensors",)) == {"a.safetensors": ("c" * 64, 10)}
    with pytest.raises(Arret, match="sans SHA-256"):
        mo.sha256_par_interface(t, "d/m", "rev", None, ("a.safetensors", "petit.json"))


# --- lecture en flux d'un fichier de poids ------------------------------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def llama(tmp_path_factory):
    return J.construire_llama(tmp_path_factory.mktemp("llama") / "m")


VOULUS = ("lm_head.weight", "model.norm.weight", "model.layers.7.mlp.down_proj.weight", "model.layers.23.mlp.down_proj.weight")


@pytest.mark.parametrize("bloc", [1, 7, 1000, 1 << 20])
def test_lecture_en_flux_tenseurs_egaux_a_un_chargement_entier(tmp_path, llama, bloc):
    from safetensors import safe_open
    par_fichier = mo.tenseurs_par_fichier(llama.index, VOULUS)
    assert sum(len(v) for v in par_fichier.values()) == len(VOULUS)
    for fichier, noms in par_fichier.items():
        contenu = (llama.dossier / fichier).read_bytes()
        if bloc == 1 and len(contenu) > 300_000:
            continue
        t = J.TransportSimule({"u": contenu}, bloc=bloc)
        d = mo.lire_poids_en_flux(t, "u", None, noms, tmp_path / fichier, len(contenu), J.sha(contenu))
        with safe_open(str(llama.dossier / fichier), "pt") as f:
            for nom in noms:
                entier = f.get_tensor(nom)
                assert entier.dtype == torch.bfloat16
                extrait = mo.charger_tenseur(tmp_path / fichier, d[nom])
                assert extrait.dtype == np.float32 and np.array_equal(extrait, entier.float().numpy())   # conversion exacte
        ecrits = sorted(p.name for p in (tmp_path / fichier).iterdir())
        assert ecrits == sorted(mo.ExtracteurSafetensors.nom_fichier(n) for n in noms)         # le fichier entier n'est jamais écrit
        assert sum(p.stat().st_size for p in (tmp_path / fichier).iterdir()) < len(contenu)


def test_lecture_en_flux_lignes_gardees(tmp_path, llama):
    fichier = mo.tenseurs_par_fichier(llama.index, ("lm_head.weight",))
    (nom_fichier, noms), = fichier.items()
    contenu = (llama.dossier / nom_fichier).read_bytes()
    d = mo.lire_poids_en_flux(J.TransportSimule({"u": contenu}), "u", None, noms, tmp_path / "t", len(contenu), J.sha(contenu))
    lignes = np.array([5, 9, 200])
    assert np.array_equal(mo.charger_tenseur(tmp_path / "t", d["lm_head.weight"], lignes),
                          llama.etat["lm_head.weight"].float().numpy()[lignes])


@pytest.mark.parametrize("position", ["en-tête", "données", "fin"])
def test_lecture_en_flux_un_octet_change_arret_et_rien_n_est_garde(tmp_path, llama, position):
    (nom_fichier, noms), = mo.tenseurs_par_fichier(llama.index, ("lm_head.weight",)).items()
    sain = (llama.dossier / nom_fichier).read_bytes()
    altere = bytearray(sain)
    altere[{"en-tête": 40, "données": len(sain) // 2, "fin": len(sain) - 1}[position]] ^= 1
    with pytest.raises(Arret):
        mo.lire_poids_en_flux(J.TransportSimule({"u": bytes(altere)}), "u", None, noms, tmp_path / "t", len(sain), J.sha(sain))
    assert not list((tmp_path / "t").glob("*.brut"))


def test_lecture_en_flux_tronquee_arret(tmp_path, llama):
    (nom_fichier, noms), = mo.tenseurs_par_fichier(llama.index, ("lm_head.weight",)).items()
    sain = (llama.dossier / nom_fichier).read_bytes()
    with pytest.raises(Arret):
        mo.lire_poids_en_flux(J.TransportSimule({"u": sain[:-10]}), "u", None, noms, tmp_path / "t", len(sain), J.sha(sain))
    assert not list((tmp_path / "t").glob("*.brut"))


def test_lecture_en_flux_reprise_apres_rupture(tmp_path, llama):
    (nom_fichier, noms), = mo.tenseurs_par_fichier(llama.index, ("lm_head.weight",)).items()
    sain = (llama.dossier / nom_fichier).read_bytes()

    class Rompu(J.TransportSimule):
        ruptures = 2

        def flux(self, url, cle=None, debut=0):
            for i, bloc in enumerate(super().flux(url, cle, debut)):
                if i == 3 and self.ruptures:
                    self.ruptures -= 1
                    raise mo.RefusReseau("flux interrompu")
                yield bloc
    t = Rompu({"u": sain})
    d = mo.lire_poids_en_flux(t, "u", None, noms, tmp_path / "t", len(sain), J.sha(sain))
    assert np.array_equal(mo.charger_tenseur(tmp_path / "t", d["lm_head.weight"]), llama.etat["lm_head.weight"].float().numpy())
    assert [a[3] for a in t.appels] == [0, 3000, 6000]                                       # reprises à l'octet atteint


def test_tenseur_absent_de_l_index_arret(llama):
    with pytest.raises(Arret, match="absent"):
        mo.tenseurs_par_fichier(llama.index, ("model.layers.99.mlp.down_proj.weight",))


# --- lentille publique ---------------------------------------------------------------------------------------------------------------------------
def test_lentille_saine(tmp_path):
    rapport, matrices = mo.controler_lentille(J.construire_lentille(tmp_path / "l.pt"), J.LARGEUR)
    assert sorted(matrices) == [7, 15, 23] and all(m.dtype == np.float16 and m.shape == (J.LARGEUR, J.LARGEUR) for m in matrices.values())
    assert rapport["paires_distinctes"] == 465 and rapport["provenance"]["capture_point"] == "block_output"
    assert len(rapport["ecart_relatif_a_l_identite_par_couche"]) == 31 and len(rapport["empreintes_matrices_gardees"]) == 3


def _sans(cle):
    return lambda c: c["provenance"].pop(cle)


def _echanger(c):
    c["J"][12] = c["J"][20].clone()               # fichier mal assemblé : deux matrices égales


ARTEFACTS_LENTILLE = {
    "couche manquante": (lambda c: c["J"].pop(30), "disposition"),
    "couche de trop": (lambda c: c["J"].update({31: c["J"][0]}), "disposition"),
    "clés décalées": (lambda c: c.update(J={l + 1: m for l, m in c["J"].items()}), "disposition"),
    "matrice non carrée": (lambda c: c["J"].update({4: c["J"][4][:, :-1]}), "disposition"),
    "simple précision": (lambda c: c["J"].update({4: c["J"][4].float()}), "disposition"),
    "sans J": (lambda c: c.pop("J"), "disposition"),
    "provenance absente": (lambda c: c.pop("provenance"), "provenance absente ou sans point de capture"),
    "sans point de capture": (_sans("capture_point"), "provenance absente ou sans point de capture"),
    "point de capture faux": (lambda c: c["provenance"].update(capture_point="mlp_input"), "point de capture autre"),
    "couche cible fausse": (lambda c: c["provenance"].update(target_layer=30), "target_layer"),
    "couches sources fausses": (lambda c: c["provenance"].update(source_layers=list(range(1, 32))), "source_layers"),
    "largeur fausse": (lambda c: c["provenance"].update(d_model=64), "d_model"),
    "matrice identité": (lambda c: c["J"].update({9: torch.eye(J.LARGEUR).half()}), "égale l'identité"),
    "deux matrices égales": (_echanger, "sont égales"),
}


@pytest.mark.parametrize("nom", sorted(ARTEFACTS_LENTILLE))
def test_lentille_artefacts_arret(tmp_path, nom):
    modifier, motif = ARTEFACTS_LENTILLE[nom]
    with pytest.raises(Arret, match=motif):
        mo.controler_lentille(J.construire_lentille(tmp_path / "l.pt", modifier=modifier), J.LARGEUR)


def test_lentille_sans_couche_cible_admise_et_cles_absentes_rapportees(tmp_path):
    def modifier(c):
        for cle in ("target_layer", "n_prompts"):
            c["provenance"].pop(cle)
    rapport, _ = mo.controler_lentille(J.construire_lentille(tmp_path / "l.pt", modifier=modifier), J.LARGEUR)
    assert rapport["cles_attendues_absentes"] == ["n_prompts"]


def test_lentille_telechargee_saine_puis_d_une_autre_empreinte_ou_absente(tmp_path):
    contenu = J.construire_lentille(tmp_path / "source.pt").read_bytes()
    t = J.TransportSimule({"u": contenu, "v": contenu[:-1] + bytes([contenu[-1] ^ 1])})
    mo.telecharger_en_fichier(t, "u", tmp_path / "ok.pt", len(contenu), J.sha(contenu))
    mo.exiger_fichier_lentille(tmp_path / "ok.pt", len(contenu), J.sha(contenu))
    with pytest.raises(Arret, match="la lecture par la seule lentille des logits n'est pas rendue"):
        mo.telecharger_en_fichier(t, "v", tmp_path / "ko.pt", len(contenu), J.sha(contenu))
    assert not (tmp_path / "ko.pt").exists()
    with pytest.raises(Arret, match="la lecture par la seule lentille des logits n'est pas rendue"):
        mo.telecharger_en_fichier(t, "absente", tmp_path / "abs.pt", len(contenu), J.sha(contenu))
    with pytest.raises(Arret, match="lentille publique absente"):
        mo.exiger_fichier_lentille(tmp_path / "abs.pt", len(contenu), J.sha(contenu))
    (tmp_path / "illisible.pt").write_bytes(b"pas une lentille")
    with pytest.raises(Arret, match="illisible"):
        mo.controler_lentille(tmp_path / "illisible.pt", J.LARGEUR)


# --- jetons gardés -------------------------------------------------------------------------------------------------------------------------------
def test_jetons_gardes_sains_et_liste_alteree_d_un_jeton():
    ids = J.jetons_gardes_jouets()
    n, e = len(ids), mo.empreinte_liste_gardee(ids)
    assert mo.exiger_jetons_gardes(ids, n, e) == {"n": n, "sha256": e, "jeton_de_debut_garde": False}
    assert mo.exiger_jetons_gardes(list(reversed(ids)), n, e)["sha256"] == e               # l'ordre ne compte pas
    for alteree in (ids[:-1] + [ids[-1] + 1], ids[:-1], ids + [10]):
        with pytest.raises(Arret, match="jetons gardés"):
            mo.exiger_jetons_gardes(alteree, n, e)
    with pytest.raises(Arret, match="doublon"):
        mo.exiger_jetons_gardes(ids + [ids[0]], n, e)
    with pytest.raises(Arret, match="jetons gardés"):
        mo.exiger_jetons_gardes(ids, K.N_JETONS_GARDES, K.SHA256_JETONS_GARDES)


def test_empreinte_de_la_liste_gardee_meme_forme_que_la_tranche_des_lentilles():
    from controle_ia.neuron_lens import controles_b_beta_v2 as cb
    ids = [5, 3, 128000, 42]
    assert mo.empreinte_liste_gardee(ids) == cb.empreinte_liste_gardee(ids)
    assert (K.N_JETONS_GARDES, K.SHA256_JETONS_GARDES) == (cb.KEPT_N, cb.KEPT_SHA256)


def test_jetons_gardes_par_les_scripts_du_voisin_sans_cle_et_une_seule_fois(tmp_path):
    v = J.construire_voisin(tmp_path)
    voisin = tmp_path / "voisin"
    mo.cloner_voisin(voisin, v.url, v.commit)
    mo.appliquer_correctifs(voisin, v.depot, v.correctifs)
    (tmp_path / "travail").mkdir()
    env = {K.NOM_CLE: J.FAUSSE_CLE, "HF_TOKEN_PATH": "/chemin/cle"}
    lu = mo.calculer_jetons_gardes(voisin, tmp_path / "hf", tmp_path / "travail", env=env)
    assert lu["ids"] == J.jetons_gardes_jouets() and lu["chaines"] == [J.vocabulaire_jouet()[i] for i in lu["ids"]]
    e05 = json.loads((voisin / "data" / "env-05.json").read_text())
    assert K.NOM_CLE not in e05["noms"] and "HF_TOKEN_PATH" not in e05["noms"] and e05["hors_ligne"] is None
    assert e05["args"] == ["--docs", K.DOCS_CORPUS] and e05["modele"] == K.DEPOT_LLAMA
    assert K.NOM_CLE not in json.loads((voisin / "data" / "env-03.json").read_text())["noms"]
    with pytest.raises(Arret, match="une fois"):
        mo.calculer_jetons_gardes(voisin, tmp_path / "hf", tmp_path / "travail", env=env)


# --- code voisin : commit, correctifs, readout.py ---------------------------------------------------------------------------------------------------
def test_voisin_commit_et_correctifs_sains(tmp_path):
    v = J.construire_voisin(tmp_path)
    assert mo.cloner_voisin(tmp_path / "voisin", v.url, v.commit) == v.commit
    corriges = mo.appliquer_correctifs(tmp_path / "voisin", v.depot, v.correctifs)
    assert sorted(corriges) == ["data/corpus/act-chat-llama-3.1-8b-instruct.provenance.json", "neuron_lens/lenses.py",
                                "scripts/checks/lens_compare.py"]
    with pytest.raises(Arret, match="existe déjà"):
        mo.cloner_voisin(tmp_path / "voisin", v.url, v.commit)


def test_voisin_autre_commit_ou_correctif_altere_arret(tmp_path):
    v = J.construire_voisin(tmp_path)
    with pytest.raises(Arret):
        mo.cloner_voisin(tmp_path / "v1", v.url, "0" * 40)
    mo.cloner_voisin(tmp_path / "v2", v.url, v.commit)
    p = v.depot / v.correctifs[0][0]
    p.write_bytes(p.read_bytes() + b"\n")
    with pytest.raises(Arret, match="correctif"):
        mo.appliquer_correctifs(tmp_path / "v2", v.depot, v.correctifs)


def test_correctifs_du_texte_presents_avec_leurs_empreintes():
    for chemin, attendue in K.CORRECTIFS:
        assert mo.sha256_fichier(J.RACINE / chemin) == attendue
    assert mo.sha256_fichier(J.RACINE / K.COPIE_READOUT) == K.SHA256_COPIE_READOUT


def test_readout_egal_a_la_copie_versee_sain(tmp_path):
    copie = J.RACINE / K.COPIE_READOUT
    autre = tmp_path / "readout.py"
    autre.write_text(copie.read_text(encoding="utf-8") + "\n\ndef fonction_ajoutee_apres_le_commit():\n    return 1\n", encoding="utf-8")
    rendu = mo.comparer_readout(autre, copie)                       # un écart hors des trois fonctions n'arrête pas
    assert rendu["fonctions_egales"] == list(K.FONCTIONS_READOUT) and rendu["fichier_entier_egal"] is False
    assert mo.comparer_readout(copie, copie)["fichier_entier_egal"] is True


@pytest.mark.parametrize("avant,apres,fonction", [
    ("top, idx = logits.topk(k, dim=0)", "top, idx = logits.topk(k + 1, dim=0)", "read"),
    ("eps: float = 1e-6", "eps: float = 1e-5", "rms_norm_columns"),
    ("vectors = vectors.float()", "vectors = vectors.double()", "transport")])
def test_readout_copie_jouet_alteree_arret(tmp_path, avant, apres, fonction):
    source = (J.RACINE / K.COPIE_READOUT).read_text(encoding="utf-8")
    assert avant in source
    autre = tmp_path / "readout.py"
    autre.write_text(source.replace(avant, apres), encoding="utf-8")
    with pytest.raises(Arret, match=f"différent de la copie versée dans {fonction}"):
        mo.comparer_readout(autre, J.RACINE / K.COPIE_READOUT)


def test_readout_copie_versee_d_une_autre_empreinte_arret(tmp_path):
    copie = tmp_path / "copie.txt"
    copie.write_text((J.RACINE / K.COPIE_READOUT).read_text(encoding="utf-8") + "#\n", encoding="utf-8")
    with pytest.raises(Arret, match="autre empreinte"):
        mo.comparer_readout(J.RACINE / K.COPIE_READOUT, copie)


# --- cibles du corpus ---------------------------------------------------------------------------------------------------------------------------------
def test_cibles_du_corpus_une_par_jeu_de_donnees(tmp_path):
    m = J.monde(tmp_path)
    voisin = tmp_path / "voisin"
    mo.cloner_voisin(voisin, m.voisin.url, m.voisin.commit)
    with pytest.raises(Arret, match="provenance du corpus"):                # avant le correctif (6) : provenance « chat » absente
        mo.cibles_corpus(voisin, m.transport)
    mo.appliquer_correctifs(voisin, m.voisin.depot, m.voisin.correctifs)
    cibles = mo.cibles_corpus(voisin, m.transport)
    assert [c.nom.split()[-1] for c in cibles] == list(K.TRANCHES_CORPUS) and all(c.url.endswith(".parquet") for c in cibles)
    assert len(mo.essais_un_octet(m.transport, mo.Cle(J.FAUSSE_CLE), cibles)) == 4
    m.transport.refus.add(cibles[2].url)
    with pytest.raises(Arret, match="avant tout téléchargement long"):
        mo.essais_un_octet(m.transport, mo.Cle(J.FAUSSE_CLE), cibles)


# --- montage entier sur jouets ---------------------------------------------------------------------------------------------------------------------------
def test_montage_entier_sain_ordre_des_requetes_et_aucune_cle_ecrite(tmp_path):
    m = J.monde(tmp_path)
    rendu = la.monter(m.ctx)
    rapport = json.loads((tmp_path / "sortie" / "diag" / J.RUN / "montage-lentilles-bbis.json").read_text(encoding="utf-8"))
    assert rapport["gardes"]["toutes_tenues"] and rapport["jetons_gardes"]["n"] == len(m.gardes)
    assert len(rapport["essais_un_octet"]) == 7 and len(rapport["garde_fonction_lecture"]) == 6
    assert rendu["ligne_proposee"].startswith("| MONTAGE-LENTILLES-BBIS | ")
    appels = m.transport.appels
    premier_flux = next(i for i, a in enumerate(appels) if a[0] == "flux")
    essais = [i for i, a in enumerate(appels) if a[0] == "octets" and a[3] == 0 and a[4] == 0]
    assert len(essais) == 7 and max(essais) < premier_flux                 # tous les essais d'un octet avant tout flux long
    for a in appels:                                                       # la clé ne va qu'aux fichiers de Llama
        assert a[2] == (m.reglages.depot_llama in a[1])
    for dossier in (tmp_path / "sortie", tmp_path / "travail"):
        for p in dossier.rglob("*"):
            if p.is_file():
                assert J.FAUSSE_CLE.encode() not in p.read_bytes(), p
    assert not (tmp_path / "travail" / "lentille-publique.pt").exists()     # seules les matrices des couches lues sont gardées
    assert sorted(p.name for p in (tmp_path / "travail" / "lentille").iterdir()) == ["J-15.npy", "J-23.npy", "J-7.npy"]
    assert not list((tmp_path / "travail").rglob("*.safetensors"))          # aucun fichier de poids entier sur disque


def test_montage_cle_absente_arret_avant_toute_requete(tmp_path):
    m = J.monde(tmp_path)
    m.ctx.env = {}
    with pytest.raises(Arret, match="absente ou vide"):
        la.monter(m.ctx)
    assert m.transport.appels == [] and not (tmp_path / "travail").exists()


def test_montage_essai_un_octet_refuse_arret_avant_tout_flux(tmp_path):
    m = J.monde(tmp_path)
    m.transport.refus.add(mo.url_fichier(m.reglages.depot_lentille, m.reglages.revision_lentille, m.reglages.fichier_lentille))
    with pytest.raises(Arret, match="avant tout téléchargement long"):
        la.monter(m.ctx)
    assert not any(a[0] == "flux" for a in m.transport.appels)


def test_montage_readout_du_commit_altere_arret_avant_tout_flux(tmp_path):
    m = J.monde(tmp_path, modifier_readout=lambda s: s.replace("logits.topk(k, dim=0)", "logits.topk(k, dim=0)  # modifié"))
    with pytest.raises(Arret, match="différent de la copie versée dans read"):
        la.monter(m.ctx)
    assert not any(a[0] == "flux" for a in m.transport.appels)


def test_montage_lentille_a_deux_matrices_egales_arret(tmp_path):
    m = J.monde(tmp_path, modifier_lentille=_echanger)
    with pytest.raises(Arret, match="sont égales"):
        la.monter(m.ctx)
    assert not (tmp_path / "sortie" / "diag").exists()


def test_montage_mode_de_debogage_arret(tmp_path):
    m = J.monde(tmp_path)
    m.ctx.env = {K.NOM_CLE: J.FAUSSE_CLE, "HF_DEBUG": "1"}
    with pytest.raises(Arret, match="débogage"):
        la.monter(m.ctx)
    assert m.transport.appels == []


def test_montage_tokeniseur_d_un_autre_sha256_arret(tmp_path):
    m = J.monde(tmp_path)
    m.reglages.sha256_tokeniseur = "0" * 64
    with pytest.raises(Arret, match="SHA-256 du tokeniseur"):
        la.monter(m.ctx)
    assert not any(a[0] == "flux" for a in m.transport.appels)


def test_montage_pointeur_d_un_fichier_de_poids_faux_arret_avant_son_flux(tmp_path):
    m = J.monde(tmp_path)
    fichier = sorted(m.reglages.poids)[0]
    m.reglages.poids[fichier] = (m.reglages.poids[fichier][0], "0" * 40)
    with pytest.raises(Arret, match="identifiant git du pointeur"):
        la.monter(m.ctx)
    assert not any(a[0] == "flux" for a in m.transport.appels)


def test_montage_fichier_de_poids_altere_d_un_octet_arret(tmp_path):
    m = J.monde(tmp_path)
    url = mo.url_fichier(m.reglages.depot_llama, m.reglages.revision_llama, sorted(m.reglages.poids)[1])
    octets = bytearray(m.transport.fichiers[url])
    octets[-5] ^= 1
    m.transport.fichiers[url] = bytes(octets)
    with pytest.raises(Arret, match="SHA-256 du flux"):
        la.monter(m.ctx)
    assert not (tmp_path / "sortie" / "diag").exists()
