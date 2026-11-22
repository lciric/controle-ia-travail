"""Épreuves (R5) de `transport_kimi_reel_v1` contre le faux serveur local `faux_serveur_kimi_v1` (127.0.0.1, port libre).
Aucun appel réel, aucun réseau sortant, clé factice. Les pièces v4 du dépôt (adaptateur, garde, registre, lanceur) sont
importées **à leur empreinte** (compagnons `.sha256`), lues sans rien y écrire.
Usage : python -I -B -m pytest -q -p no:cacheprovider test_transport_kimi_reel_v1.py"""
import hashlib
import json
import os
import sys

import numpy as np
import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
DEVIS_V4 = os.environ.get("DOSSIER_DEVIS_V4") or "/home/user/controle-ia-travail/docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v4"
PIECES = ("adaptateur_fournisseur_v1.py", "garde_pilote_essaim_v2.py", "registre_depense_v1.py", "lanceur_pilote_essaim_v2.py",
          "calcul_devis_essaim_v4.py", "racine_depot_v1.py")
for _p in PIECES:
    _sha = open(os.path.join(DEVIS_V4, _p + ".sha256"), encoding="utf-8").read().split()[0]
    assert hashlib.sha256(open(os.path.join(DEVIS_V4, _p), "rb").read()).hexdigest() == _sha, _p
for _d in (ICI, DEVIS_V4):
    if _d not in sys.path:
        sys.path.insert(0, _d)

import adaptateur_fournisseur_v1 as A  # noqa: E402
import adaptateur_kimi_strict_v1 as AS  # noqa: E402
import essai_fumee_kimi_v1 as EF  # noqa: E402
import faux_serveur_kimi_v1 as FS  # noqa: E402
import garde_pilote_essaim_v2 as GP  # noqa: E402
import lanceur_pilote_essaim_v2 as L  # noqa: E402
import registre_depense_v1 as RG  # noqa: E402
import transport_kimi_reel_v1 as T  # noqa: E402

CLE = "sk-FAUSSE-cle-d-epreuve-0123456789abcdef"
MT = 2000
SS = np.random.SeedSequence(20261122).spawn(8)  # R9


def env(**kw):
    e = {"KIMI_API_KEY": CLE}
    e.update(kw)
    return e


def transport(srv, **kw):
    kw.setdefault("delai_silence_s", 5)
    kw.setdefault("delai_total_s", 20)
    return T.TransportKimiReel(amont=srv.url, environ=env(), **kw)


def appel_seul(regle, texte="Bonjour.", mt=MT, **kw):
    with FS.FauxServeurKimi(regle) as srv:
        tr = transport(srv, **kw)
        ad = AS.AdaptateurKimiStrict(tr)
        try:
            rep = ad.appeler({"id": "x"}, texte, mt)
            return rep, srv, tr, None
        except Exception as ex:  # noqa: BLE001
            return None, srv, tr, ex


def posts(srv):
    return [r for r in srv.requetes if r[0] == "POST"]


# --- contrat de construction -----------------------------------------------------------------------------------------
def test_contrat_declare_et_accepte_par_l_adaptateur():
    with FS.FauxServeurKimi() as srv:
        tr = transport(srv)
        assert tr.relances_internes == 0 and tr.repli_modele is None
        A.AdaptateurChatCompletions(tr, T.MODELE)


def test_cle_lue_par_son_nom_et_retiree_de_l_environnement():
    e = env()
    T.TransportKimiReel(amont="http://127.0.0.1:9", environ=e)
    assert "KIMI_API_KEY" not in e


def test_cle_absente_refusee():
    with pytest.raises(A.ConfigurationRefusee) as ex:
        T.TransportKimiReel(amont="http://127.0.0.1:9", environ={})
    assert "KIMI_API_KEY" in str(ex.value)


@pytest.mark.parametrize("amont", ["http://api.moonshot.ai", "https://api.moonshot.ai/v1", "ftp://127.0.0.1"])
def test_amont_refuse(amont):
    with pytest.raises(A.ConfigurationRefusee):
        T.TransportKimiReel(amont=amont, environ=env())


# --- cas sain ------------------------------------------------------------------------------------------------------
def test_cas_sain_un_envoi_corps_en_liste_blanche():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"prompt": 20, "completion": 300, "raisonnement": 200})
    assert ex is None
    assert rep["usage"] == {"entree": 20, "sortie": 300} and rep["texte"] == "OK"
    assert len(posts(srv)) == 1 and srv.nombre == 1 and tr.envois == 1
    m, chemin, h, brut = srv.requetes[0]
    assert chemin == "/v1/chat/completions"
    corps = json.loads(brut)
    assert corps == {"model": "kimi-k3.1-pro", "messages": [{"role": "user", "content": "Bonjour."}], "max_tokens": MT,
                     "stream": True, "stream_options": {"include_usage": True}}
    hb = {k.lower(): v for k, v in h.items()}
    assert hb["authorization"] == "Bearer " + CLE
    assert hb["user-agent"] == T.AGENT
    assert not any(x in hb for x in ("x-session-id", "openai-organization", "cookie"))
    assert tr.dernier_diagnostic["modele_servi"] == T.MODELE and tr.dernier_diagnostic["id_reponse"] == "chatcmpl-faux"


def test_usage_dans_le_choix_lu():
    rep, *_ = appel_seul(lambda k, c: {"prompt": 7, "completion": 9, "usage_dans_choix": True})
    assert rep["usage"] == {"entree": 7, "sortie": 9}


# --- refus sans envoi ------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("requete", [
    {"model": "kimi-k3", "messages": [{"role": "user", "content": "a"}], "max_tokens": 10},
    {"model": "kimi-k3.1-pro-highspeed", "messages": [{"role": "user", "content": "a"}], "max_tokens": 10},
    {"model": "kimi-k3.1-pro", "messages": [{"role": "user", "content": "a"}], "max_tokens": 24001},
    {"model": "kimi-k3.1-pro", "messages": [{"role": "user", "content": "a"}], "max_tokens": 0},
    {"model": "kimi-k3.1-pro", "messages": [{"role": "user", "content": "a"}], "max_tokens": True},
    {"model": "kimi-k3.1-pro", "messages": [{"role": "user", "content": "a"}], "max_tokens": 10, "n": 2},
    {"model": "kimi-k3.1-pro", "messages": [{"role": "user", "content": "a"}], "max_tokens": 10, "stream": True},
    {"model": "kimi-k3.1-pro", "messages": [{"role": "user", "content": "a"}], "max_tokens": 10, "tools": []},
    {"model": "kimi-k3.1-pro", "messages": [{"role": "system", "content": "a"}], "max_tokens": 10},
    {"model": "kimi-k3.1-pro", "messages": [{"role": "user", "content": "voir session_01XJ6MgnUbaBVDZbP5j1KTqo"}], "max_tokens": 10},
    {"model": "kimi-k3.1-pro", "messages": [{"role": "user", "content": "écrire à quelqu.un@exemple.org"}], "max_tokens": 10},
    {"model": "kimi-k3.1-pro", "messages": [{"role": "user", "content": "pour LAZAR"}], "max_tokens": 10},
])
def test_requete_hors_contrat_refusee_sans_envoi(requete):
    with FS.FauxServeurKimi() as srv:
        tr = transport(srv)
        with pytest.raises(A.ConfigurationRefusee):
            tr.envoyer(requete)
        assert srv.nombre == 0 and tr.envois == 0


def test_adaptateur_vers_autre_modele_refuse_sans_envoi():
    with FS.FauxServeurKimi() as srv:
        ad = A.AdaptateurChatCompletions(transport(srv), "kimi-k3")
        with pytest.raises(A.ConfigurationRefusee):
            ad.appeler({}, "a", 10)
        assert srv.nombre == 0


# --- artefacts -------------------------------------------------------------------------------------------------------
def test_autre_modele_servi_anomalie():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"modele": "kimi-k3"})
    assert isinstance(ex, A.AnomalieReponse) and srv.nombre == 1


def test_modele_qui_change_en_cours_de_flux_anomalie():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"modele_apres": "kimi-k2.6"})
    assert isinstance(ex, A.AnomalieReponse) and srv.nombre == 1


@pytest.mark.parametrize("statut", [429, 500, 502, 503])
def test_statut_relancable_echec_sans_relance(statut):
    rep, srv, tr, ex = appel_seul(lambda k, c: {"statut": statut})
    assert isinstance(ex, A.ErreurFournisseur) and str(statut) in str(ex)
    assert srv.nombre == 1 and tr.envois == 1


@pytest.mark.parametrize("statut", [400, 401, 402, 403, 404])
def test_statut_fatal(statut):
    rep, srv, tr, ex = appel_seul(lambda k, c: {"statut": statut})
    assert isinstance(ex, T.ErreurTransportFatale) and not isinstance(ex, A.ErreurFournisseur)
    assert srv.nombre == 1


def test_fermeture_sans_reponse_echec_sans_relance():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"fermer_sans_reponse": True})
    assert isinstance(ex, A.ErreurFournisseur) and srv.nombre == 1


@pytest.mark.parametrize("n", [0, 1, 2, 3, 9])  # 9 : coupure après l'usage, avant [DONE]
def test_coupure_en_plein_flux(n):
    rep, srv, tr, ex = appel_seul(lambda k, c: {"coupure_apres": n})
    assert isinstance(ex, A.ErreurFournisseur) and srv.nombre == 1


def test_flux_sans_done():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"sans_done": True})
    assert isinstance(ex, A.ErreurFournisseur) and "[DONE]" in str(ex)


def test_evenement_erreur_dans_le_flux():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"evenement_erreur": True})
    assert isinstance(ex, A.ErreurFournisseur)


def test_200_non_flux_anomalie():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"non_flux": True})
    assert isinstance(ex, A.AnomalieReponse) and getattr(ex, "envois", None) == 1


def test_usage_absent():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"usage_absent": True})
    assert ex is None and rep["usage"] is None


def test_usage_negatif_jamais_lu_comme_cout_puis_garde_16():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"completion": -24000, "raisonnement": 0})
    assert ex is None and (rep["usage"] is None or rep["usage"]["sortie"] < 0)
    p = GP.plan_pstd()
    g = GP.Garde(p, GP.PRIX_GELES, 10.0)
    g.avant(p[0], "x" * 100, 24000)
    with pytest.raises(GP.ArretCourse) as a:
        g.apres(p[0], rep["usage"])
    assert a.value.code == 16 and g.depense == pytest.approx(GP.reserve_dure("proposeur", 100, 24000, GP.PRIX_GELES))


def test_reflexion_hors_completion_premier_niveau_ajoutee():
    rep, *_ = appel_seul(lambda k, c: {"prompt": 10, "completion": 100, "raisonnement": 0, "reflexion_hors": 900})
    assert rep["usage"] == {"entree": 10, "sortie": 1000}


def test_reflexion_detail_superieur_au_compte_ajoutee():
    rep, *_ = appel_seul(lambda k, c: {"prompt": 10, "completion": 100, "detail_hors": 500})
    assert rep["usage"]["sortie"] >= 100 + 500


def test_excedent_total_tokens_compte_en_sortie():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"prompt": 10, "completion": 100, "total_en_plus": 777})
    assert rep["usage"] == {"entree": 10, "sortie": 877}
    assert tr.dernier_diagnostic["excedent_total_tokens"] == 777


def test_reponse_trop_longue_en_octets_anomalie():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"remplissage": 200_000}, taille_max_octets=100_000)
    assert isinstance(ex, A.AnomalieReponse) and ex.envois == 1 and srv.nombre == 1


def test_sortie_rendue_au_dela_de_max_tokens_garde_16():
    rep, *_ = appel_seul(lambda k, c: {"completion": 1001}, mt=1000)  # sous le plafond du rôle (2000), au-delà de l'envoyé
    p = GP.plan_pstd()
    m = next(a for a in p if a["role"] == "message")
    g = GP.Garde([m], GP.PRIX_GELES, 10.0)
    g.avant(m, "x" * 100, 1000)
    with pytest.raises(GP.ArretCourse) as a:
        g.apres(m, rep["usage"])
    assert a.value.code == 16


def test_delai_de_silence_depasse():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"attente_s": 2.0}, delai_silence_s=0.5)
    assert isinstance(ex, A.ErreurFournisseur) and "délai" in str(ex) and srv.nombre == 1


def test_delai_total_depasse_malgre_le_maintien():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"maintien": 30, "pas_s": 0.1}, delai_silence_s=1, delai_total_s=1)
    assert isinstance(ex, A.ErreurFournisseur) and "total" in str(ex) and srv.nombre == 1


def test_un_seul_envoi_par_appel_sur_cent_appels():
    regles = [{"statut": 429}, {"coupure_apres": 1}, {"modele": "kimi-k3"}, {}, {"statut": 500}, {"usage_absent": True}]
    with FS.FauxServeurKimi(lambda k, c: regles[k % len(regles)]) as srv:
        tr = transport(srv)
        ad = AS.AdaptateurKimiStrict(tr)
        for i in range(100):
            avant = srv.nombre
            try:
                ad.appeler({}, f"appel {i}", 50)
            except (A.ErreurFournisseur, A.AnomalieReponse):
                pass
            assert srv.nombre == avant + 1 and tr.envois == i + 1


def test_cle_jamais_en_sortie_ni_en_exception(capsys):
    textes = []
    for r in ({"statut": 401, "corps_erreur": {"error": {"type": CLE, "code": CLE}}}, {"coupure_apres": 1}, {"statut": 500}, {}):
        rep, srv, tr, ex = appel_seul(lambda k, c, r=r: r)
        textes += [repr(tr), str(tr), str(ex), repr(ex), json.dumps(tr.dernier_diagnostic, default=str), json.dumps(rep, default=str)]
    with pytest.raises(TypeError):
        import pickle
        pickle.dumps(tr)
    out = capsys.readouterr()
    textes += [out.out, out.err]
    assert not any(CLE in t for t in textes)


def test_fermer_efface_la_cle_et_refuse_ensuite():
    with FS.FauxServeurKimi() as srv:
        tr = transport(srv)
        tr.fermer()
        assert bytes(tr._cle) == b""
        with pytest.raises(A.ConfigurationRefusee):
            tr.envoyer({"model": T.MODELE, "messages": [{"role": "user", "content": "a"}], "max_tokens": 5})
        assert srv.nombre == 0


# --- branchement sur le lanceur v2 et le registre réels ------------------------------------------------------------
def regle_realiste(graine, extra=None):
    rng = np.random.default_rng(graine)

    def regle(k, corps):
        mt = corps["max_tokens"]
        c = int(rng.integers(3000, 12801)) if mt > 2000 else int(rng.integers(200, 401))
        r = {"completion": min(c, mt), "raisonnement": min(c, mt) // 2}
        if extra:
            r.update(extra(k, corps) or {})
        return r
    return regle


def entree_texte(appel):
    return "x" * (40260 if appel["role"] == "proposeur" else 9900)


def courir_lanceur(tmp_path, regle, plafond=None, nom="c", fabrique=None):
    reg = str(tmp_path / f"registre-{nom}.jsonl")
    L.creer_registre(reg, plafond)
    with FS.FauxServeurKimi(regle) as srv:
        tr = transport(srv)
        ad = fabrique(tr) if fabrique else AS.AdaptateurKimiStrict(tr)
        code, g = L.courir(GP.plan_pstd(), ad, entree_texte, str(tmp_path / f"journal-{nom}.jsonl"), reg, plafond_depense=plafond)
        facture, n = srv.facture_usd, srv.nombre
    lignes = [json.loads(x) for x in open(reg, encoding="utf-8")]
    reserves = sum(1 for x in lignes if x["evenement"] == "reserve")
    etat_depense = sum(x.get("cout_usd", 0) for x in lignes if x["evenement"] in ("regle", "echec", "compte_a_la_reserve"))
    return code, g, facture, n, reserves, etat_depense, tr


def test_lanceur_pstd_complet_avec_echecs_et_reflexion(tmp_path):
    def extra(k, corps):
        if k in (5, 300):
            return {"statut": 429}
        if k == 50:
            return {"statut": 500, "facture": (12000, corps["max_tokens"])}  # erreur facturée au plafond (pire H4)
        if k == 100:
            return {"coupure_apres": 2, "facture": (12000, 1000)}            # coupure en plein flux, facturée en partie
        if k % 97 == 3:
            return {"reflexion_hors": 500}                                     # réflexion hors completion_tokens
        if k % 89 == 7:
            return {"cache_lu": 4000}
        return None
    code, g, facture, n, reserves, dep_reg, tr = courir_lanceur(tmp_path, regle_realiste(SS[0], extra), nom="pstd")
    assert code == 0
    assert n == 744 + 4 == reserves == tr.envois               # un envoi par réserve écrite, relances comprises
    assert g.depense >= facture - 1e-9                          # la dépense comptée couvre la facture du faux serveur
    assert g.depense == pytest.approx(dep_reg)
    assert g.depense <= GP.borne_pire(GP.plan_pstd(), GP.PRIX_GELES)["pire_usd"]
    assert g.echecs == 4


def test_lanceur_plafond_1_usd_arret_14(tmp_path):
    code, g, facture, n, reserves, dep_reg, tr = courir_lanceur(tmp_path, regle_realiste(SS[1]), plafond=1.0, nom="p1")
    assert code == 14 and g.depense <= 1.0 and g.depense >= facture - 1e-9 and n == reserves


@pytest.mark.parametrize("artefact,code_attendu", [
    ({"modele": "kimi-k3"}, 16),
    ({"completion": 24001}, 10),
    ({"usage_absent": True}, 16),
    ({"completion": -5}, 16),
    ({"statut": 401}, 17),
    ({"non_flux": True}, 16),
    ({"total_en_plus": 30000}, 10),
])
def test_lanceur_artefact_arrete_et_couvre_la_facture(tmp_path, artefact, code_attendu):
    def extra(k, corps):
        return artefact if k == 3 else None
    code, g, facture, n, reserves, dep_reg, tr = courir_lanceur(tmp_path, regle_realiste(SS[2], extra), nom="art")
    assert code == code_attendu
    assert n == reserves == 4
    assert g.depense >= facture - 1e-9 and g.depense == pytest.approx(dep_reg)


def test_lanceur_refuse_transport_qui_declarerait_des_relances(tmp_path):
    with FS.FauxServeurKimi() as srv:
        tr = transport(srv)
        tr.relances_internes = 2
        with pytest.raises(A.ConfigurationRefusee):
            A.AdaptateurChatCompletions(tr, T.MODELE)


# --- répétition à blanc de l'essai de fumée --------------------------------------------------------------------------
def test_essai_de_fumee_a_blanc(tmp_path):
    def regle(k, corps):
        if k == 1:   # f2 : max_tokens 16, fin length
            return {"completion": 16, "raisonnement": 13}
        if k == 4:   # f5 : lent, coupé côté client par le délai total
            return {"maintien": 80, "pas_s": 0.1}
        if k == 5:
            return {"cache_lu": 1024}
        return {}
    with FS.FauxServeurKimi(regle) as srv:
        e = env()
        code = EF.courir(str(tmp_path / "reg.jsonl"), str(tmp_path / "j.jsonl"), srv.url, 1.0, environ=e)
        facture, n = srv.facture_usd, srv.nombre
    assert code == 0 and n == 6 and "KIMI_API_KEY" not in e
    lignes = [json.loads(x) for x in open(tmp_path / "j.jsonl", encoding="utf-8")]
    appels = [x for x in lignes if x["evenement"] == "appel"]
    assert [a["id"] for a in appels] == [p["id"] for p in EF.plan_fumee()]
    assert all(a["envois_du_transport"] == 1 for a in appels)
    assert appels[1]["verifications"]["H2_tenue_sous_reserve_console"] is True
    assert appels[4]["issue"] == "echec" and "total" in appels[4]["motif"]
    assert all(a["verifications"]["H3_entree_le_octets_plus_256"] for a in appels if a["id"] != "f5-h4-coupure")
    fin = lignes[-1]
    assert fin["evenement"] == "fin" and fin["envois_total"] == 6 and fin["depense_usd"] >= facture - 1e-6
    assert fin["depense_usd"] <= 1.0
    texte_journal = open(tmp_path / "j.jsonl", encoding="utf-8").read()
    assert CLE not in texte_journal and "Lignes z0" not in texte_journal
    with pytest.raises(RG.RegistreRefuse) as r:  # course close : jamais rejouée sur le même registre
        RG.Registre(str(tmp_path / "reg.jsonl"), EF.parametres(EF.plan_fumee(), 1.0))
    assert r.value.code == 23


def test_essai_de_fumee_refuse_l_amont_reel_sans_go(tmp_path):
    code = EF.courir(str(tmp_path / "r.jsonl"), str(tmp_path / "j.jsonl"), "https://api.moonshot.ai", 1.0, environ=env())
    assert code == 3 and not os.path.exists(tmp_path / "r.jsonl")


def test_essai_de_fumee_refuse_plafond_au_dessus_de_1(tmp_path):
    assert EF.courir(str(tmp_path / "r.jsonl"), str(tmp_path / "j.jsonl"), "http://127.0.0.1:9", 1.01, environ=env()) == 2


def test_essai_de_fumee_cout_prevu_sous_le_plafond():
    total = sum(GP.cout(len(p["texte"].encode()) + GP.SURCOUT_FORMAT, p["max_tokens"], GP.PRIX_GELES) for p in EF.plan_fumee())
    assert total < 0.5


# --- exigences de la vérification de la v4 ---------------------------------------------------------------------------
class TransportQuiRelanceEnCachette(T.TransportKimiReel):
    """Sous-classe hostile : relance une fois sous l'envoi (même compteur) et prétend `tentatives = 1`."""

    def _envoyer_une_fois(self, corps, compteur):
        try:
            T.TransportKimiReel._envoyer_une_fois(self, corps, compteur)
        except Exception:  # noqa: BLE001
            pass
        rep = T.TransportKimiReel._envoyer_une_fois(self, corps, compteur)
        rep["tentatives"] = 1
        return rep


class TransportQuiCacheSonCompteur(T.TransportKimiReel):
    """Sous-classe hostile : relance sur un compteur jeté ; la mesure ne voit qu'un envoi. Seule la classe exacte l'arrête."""

    def _envoyer_une_fois(self, corps, compteur):
        try:
            T.TransportKimiReel._envoyer_une_fois(self, corps, [0])
        except Exception:  # noqa: BLE001
            pass
        return T.TransportKimiReel._envoyer_une_fois(self, corps, compteur)


def test_tentatives_mesurees_egales_au_compte_du_serveur():
    regles = [{}, {"statut": 429}, {"coupure_apres": 1}, {"modele": "kimi-k3"}]
    with FS.FauxServeurKimi(lambda k, c: regles[k % 4]) as srv:
        tr = transport(srv)
        ad = AS.AdaptateurKimiStrict(tr)
        for i in range(12):
            try:
                ad.appeler({}, f"a{i}", 30)
                assert tr.derniere_reponse["tentatives"] == 1
            except (A.ErreurFournisseur, A.AnomalieReponse):
                pass
        assert srv.nombre == tr.envois == 12


@pytest.mark.parametrize("classe", [TransportQuiRelanceEnCachette, TransportQuiCacheSonCompteur])
def test_adaptateur_strict_refuse_toute_sous_classe(classe):
    with FS.FauxServeurKimi() as srv:
        tr = classe(amont=srv.url, environ=env())
        with pytest.raises(A.ConfigurationRefusee):
            AS.AdaptateurKimiStrict(tr)
        assert srv.nombre == 0


def test_relance_cachee_mesuree_meme_sous_l_adaptateur_non_strict(tmp_path):
    """Sous l'adaptateur v1 non strict, la sous-classe qui relance sur le même compteur est mesurée à 2 envois :
    anomalie, 2 réserves comptées, arrêt 16, dépense ≥ facture du faux serveur (qui a facturé deux fois)."""
    reg = str(tmp_path / "registre-cache.jsonl")
    L.creer_registre(reg)
    with FS.FauxServeurKimi(lambda k, c: {"statut": 500, "facture": (12000, 24000)} if k == 0 else {"completion": 5000}) as srv:
        tr = TransportQuiRelanceEnCachette(amont=srv.url, environ=env(), delai_silence_s=5, delai_total_s=20)
        ad = A.AdaptateurChatCompletions(tr, T.MODELE)
        code, g = L.courir(GP.plan_pstd(), ad, entree_texte, str(tmp_path / "j-cache.jsonl"), reg)
        facture, n = srv.facture_usd, srv.nombre
    assert code == 16 and n == 2 and g.depense >= facture - 1e-9
    lignes = [json.loads(x) for x in open(reg, encoding="utf-8")]
    res = next(x for x in lignes if x["evenement"] == "reserve")["reserve_usd"]
    cr = next(x for x in lignes if x["evenement"] == "compte_a_la_reserve")
    assert "= 2" in cr["motif"] and cr["cout_usd"] == pytest.approx(2 * res)  # tentatives MESURÉES = 2 : deux réserves


def test_methode_remplacee_sur_l_instance_refusee():
    with FS.FauxServeurKimi() as srv:
        tr = transport(srv)
        ad = AS.AdaptateurKimiStrict(tr)
        tr.envoyer = lambda requete: {"model": T.MODELE, "usage": None, "tentatives": 1}
        with pytest.raises(A.ConfigurationRefusee):
            ad.appeler({}, "a", 10)
        tr2 = transport(srv)
        tr2._connexion = lambda: T.http.client.HTTPConnection("127.0.0.1", 9)
        with pytest.raises(A.ConfigurationRefusee):
            AS.AdaptateurKimiStrict(tr2)
        assert srv.nombre == 0


def test_connexion_non_comptee_refusee_sans_envoi_meme_sans_adaptateur_strict():
    with FS.FauxServeurKimi() as srv:
        tr = transport(srv)
        tr._connexion = lambda: T.http.client.HTTPConnection("127.0.0.1", int(srv.url.rsplit(":", 1)[1]))
        with pytest.raises(A.ConfigurationRefusee):
            tr.envoyer({"model": T.MODELE, "messages": [{"role": "user", "content": "a"}], "max_tokens": 5})
        assert srv.nombre == 0


def test_empreinte_du_module_ecrite_dans_l_adaptateur():
    assert AS.SHA_TRANSPORT == hashlib.sha256(open(T.__file__, "rb").read()).hexdigest()


@pytest.mark.parametrize("usage", [
    {"prompt_tokens": 10, "completion_tokens": 100, "total_tokens": 110},                                      # pas de détail
    {"prompt_tokens": 10, "completion_tokens": 100, "total_tokens": 110, "completion_tokens_details": {}},     # détail vide
    {"prompt_tokens": 10, "completion_tokens": 100, "completion_tokens_details": {"reasoning_tokens": 50}},   # pas de total
    {"prompt_tokens": 10, "completion_tokens": 100, "total_tokens": 110, "completion_tokens_details": {"reasoning_tokens": None}},
])
def test_champ_de_reflexion_absent_jamais_lu_comme_zero(usage):
    rep, srv, tr, ex = appel_seul(lambda k, c: {"usage": usage})
    assert ex is None and rep["usage"] is None and "usage_refuse" in tr.dernier_diagnostic


def test_reflexion_rendue_en_texte_mais_absente_du_compte():
    rep, srv, tr, ex = appel_seul(lambda k, c: {"completion": 10, "raisonnement": 0, "reflexion_texte": 20000})
    assert ex is None and rep["usage"] is None


@pytest.mark.parametrize("artefact", [
    {"usage": {"prompt_tokens": 12000, "completion_tokens": 300, "total_tokens": 12300}, "facture": (12000, 20300)},
    {"completion": 300, "raisonnement": 0, "reflexion_texte": 60000, "facture": (12000, 20300)},
])
def test_lanceur_reflexion_facturee_absente_de_l_usage_comptee_au_pire(tmp_path, artefact):
    def extra(k, corps):
        return artefact if k == 2 else None
    code, g, facture, n, reserves, dep_reg, tr = courir_lanceur(tmp_path, regle_realiste(SS[3], extra), nom="refl")
    assert code == 16 and n == reserves == 3 and g.depense >= facture - 1e-9
