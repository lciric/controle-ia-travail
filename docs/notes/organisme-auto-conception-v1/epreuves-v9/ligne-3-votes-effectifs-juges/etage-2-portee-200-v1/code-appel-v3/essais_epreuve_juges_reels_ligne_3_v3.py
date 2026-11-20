"""Essais de `epreuve_juges_reels_ligne_3_v3.py` (pytest, service factice seul : aucun réseau, aucune clé, aucun relais).

Version 3 (R12 ; la v2 est gardée) : les essais de la v2 sur le module v3 ; ceux du mode réel passent un environnement qui
porte HTTPS_PROXY (nom seul, valeur factice) ; essais neufs en fin de fichier : départ refusé sans HTTPS_PROXY, liste blanche
élargie (correction de la mère, 14:10Z).

Version 2 (R12 ; la v1 est gardée) : les essais de la v1, sur le module v2, plus les essais des corrections C1, C2, C3 de la
contre-lecture et des décisions de la mère (2) et (3) (nom de la clé, environnement épuré), en fin de fichier.

Chaque garde de la liste d'arrêt qui touche l'appel, sur un cas sain et sur un artefact (règle R5) ; la relance après
panne ; la reproduction exacte, sur service factice aux coûts du calcul v2 des conditions du plafond
(`calcul_conditions_plafond_200_ligne_3_v2.py`, 86440df6… ; sortie `calcul-conditions-plafond-200-ligne-3-v2.json`,
fe58be3a…), de ses nombres. Lectures seules hors du dossier temporaire de pytest : le clone de l'orchestrateur (modules
vérifiés par empreinte), la consigne figée du juge, la configuration de la course v9 (items, étiquettes interdites ; aucun
modèle n'en est lu), les témoins de la version 2, le calcul v2 et sa sortie, et les deux pièces de coût qu'il lit.
"""
import importlib.util
import json
import shutil
import sys
from fractions import Fraction
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import epreuve_juges_reels_ligne_3_v3 as M  # noqa: E402

ENV_BASE = {"HTTPS_PROXY": "http://127.0.0.1:1"}      # v3 : valeur factice ; seul le nom est lu par le programme

L3 = M.DEPOT / "docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1"
CALCUL = (L3 / "calcul_conditions_plafond_200_ligne_3_v2.py",
          "86440df6f81d0c185a8aab375b67ba67a4c09351716dc17acc8988bbc9f098bf")
SORTIE_CALCUL = (L3 / "calcul-conditions-plafond-200-ligne-3-v2.json",
                 "fe58be3a790ee28db3fadb6370251a69c4378dc887e977a19ab77fd9093eb3e2")
PLOMBERIE = ("t01", "t02")
NOM_JUGE = {"juge Opus": "juge-opus", "juge Argon": "juge-argon"}
MODELE = {"juge-opus": "modele-factice-a", "juge-argon": "modele-factice-b"}
FOURNISSEUR = {"juge-opus": "fournisseur-a", "juge-argon": "fournisseur-b"}


# --- pièces lues -----------------------------------------------------------------------------------------------------------------


@pytest.fixture(scope="session")
def fonctions():
    return M.charger_service_des_juges()


@pytest.fixture(scope="session")
def consigne():
    return M.lire_par_empreinte(M.DEPOT / M.CONSIGNE_JUGE[0], M.CONSIGNE_JUGE[1], "consigne").decode("utf-8")


@pytest.fixture(scope="session")
def configuration():
    return json.loads(M.lire_par_empreinte(M.DEPOT / M.CONFIGURATION[0], M.CONFIGURATION[1], "configuration"))


@pytest.fixture(scope="session")
def sortie_calcul():
    return json.loads(M.lire_par_empreinte(SORTIE_CALCUL[0], SORTIE_CALCUL[1], "sortie du calcul v2"))


@pytest.fixture(scope="session")
def module_calcul():
    M.lire_par_empreinte(CALCUL[0], CALCUL[1], "calcul v2")
    spec = importlib.util.spec_from_file_location("calcul_plafond_200_v2", CALCUL[0])
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# --- banque factice, banc factice, service --------------------------------------------------------------------------------------


def ecrire_banque(dossier: Path, items, n=M.N_TEMOINS, contenu_de=None, nom="banque.json"):
    temoins = []
    for k in range(1, n + 1):
        mauvais = k > n // 2
        contenu = {"titre": f"Carte d'essai numéro {k}",
                   "module_change": f"mémoire : une ligne de plus par carte éliminée, version factice {k}.",
                   "mecanisme": f"Servir une liste de directions déjà éliminées ; texte factice {k}, sans valeur.",
                   "plus_proche_voisin": "mémoire n° 5 (mémoire des directions ratées) ; voisin factice.",
                   "epreuve_monde_plante": f"Monde planté factice {k} ; bras sans le mécanisme ; critère par programme."}
        if contenu_de is not None:
            contenu = contenu_de(k, contenu)
        temoins.append({"identifiant_interne": f"L3-T{k:03d}", "classe": "mauvais" if mauvais else "bon",
                        "item": items[(k - 1) % 5] if mauvais else None,
                        "niveau": M.NIVEAUX[(k - 1) % 3] if mauvais else None, "citation": k % 4 < 2,
                        "moitie": "lecture" if k % 2 else "etalonnage", "contenu": contenu})
    chemin = dossier / nom
    octets = M.json_octets({"version": "banque-factice-des-essais", "temoins": temoins})
    chemin.write_bytes(octets)
    h = M.sha256_octets(octets)
    Path(str(chemin) + ".sha256").write_text(f"{h}  {chemin.name}\n", encoding="utf-8")
    return chemin, h


class Banc:
    """Service factice commun aux deux juges : un compteur global d'appels (l'ordre du plan), des coûts exacts par modèle,
    un modèle de refus (les `refus_premiers` premiers envois refusés une fois, puis rejoués avec succès : celui du calcul
    v2), et des artefacts réglables."""

    def __init__(self, items, couts, refus_premiers=0, tout_refuser=False, identiques=False, illisible_pour=None,
                 sans_cout_pour=None, panne_a=None, cout_a=None, modele_change_a=None, exception_a=None):
        self.items, self.couts = items, couts
        self.refus_premiers, self.tout_refuser, self.identiques = refus_premiers, tout_refuser, identiques
        self.illisible_pour = illisible_pour or (lambda i, modele: False)
        self.sans_cout_pour = sans_cout_pour or (lambda i, modele: False)
        self.panne_a, self.cout_a, self.modele_change_a, self.exception_a = panne_a, cout_a or {}, modele_change_a, exception_a
        self.i = 0
        self.servis = []

    def repondre(self, _k, consigne, modele, dossier):
        i = self.i
        self.i += 1
        if self.panne_a is not None and i == self.panne_a:
            raise KeyboardInterrupt("panne simulée pendant l'envoi")
        if self.exception_a is not None and i == self.exception_a:
            raise ConnectionError("relais injoignable (factice)")
        if self.tout_refuser or (i < 2 * self.refus_premiers and i % 2 == 0):
            return M.ResultatFactice("", 0.0, statut="erreur", modele_servi=None)
        cout = self.cout_a.get(i, self.couts[modele])
        self.servis.append(cout)
        note = "même réponse" if self.identiques else f"réponse factice {i}"
        texte = "```json\n" + json.dumps({"items": {k: True for k in self.items}, "note": note}) + "\n```"
        if self.illisible_pour(i, modele):
            texte = "aucun bloc JSON ici"
        servi = modele
        if self.modele_change_a is not None and i >= self.modele_change_a and modele == MODELE["juge-argon"]:
            servi = "modele-factice-c"
        if self.sans_cout_pour(i, modele):
            return M.ResultatFactice(texte, 0.6, modele_servi=servi, cout_inconnu=True)
        return M.ResultatFactice(texte, cout, modele_servi=servi)


def faire_service(racine: Path, banc: Banc, fonctions, consigne, configuration, nature="essai", sans_moyen=False):
    adaptateurs = {}
    for j in M.JUGES:
        ad = M.AdaptateurFactice(banc.repondre)
        if sans_moyen:
            ad.moyen_du_plafond_de_session = None
        adaptateurs[FOURNISSEUR[j]] = ad
    juges = [{"etiquette": j, "fournisseur": FOURNISSEUR[j], "modele": MODELE[j]} for j in M.JUGES]
    return M.Service(nature=nature, juges=juges, adaptateurs=adaptateurs, consigne=consigne,
                     consigne_sha=M.sha256_octets(consigne.encode("utf-8")), items=configuration["items_juge"],
                     interdites=configuration["etiquettes_interdites_fixes"],
                     dossier_appels=racine / "sortie" / "appels", fonctions=fonctions,
                     configuration_servie={"juges": juges, "items": configuration["items_juge"]})


def couts_au_facteur(facteur):
    return {MODELE[j]: M.TARIF_DES_CARTES[j] * facteur for j in M.JUGES}


def jouer(tmp, fonctions, consigne, configuration, banc, nom="run", arret_de_plomberie=True, banque=None):
    racine = tmp / nom
    racine.mkdir()
    if banque is None:
        banque = ecrire_banque(tmp, configuration["items_juge"], nom=f"banque-{nom}.json")
    service = faire_service(racine, banc, fonctions, consigne, configuration)
    rapport = M.executer(racine, banque[0], banque[1], PLOMBERIE, service, {"commit_depot": "essai"},
                         arret_de_plomberie=arret_de_plomberie)
    return rapport, racine, service


def lignes_du_journal(racine):
    chemin = racine / "sortie" / "epreuve" / "journal-compteur.jsonl"
    return [json.loads(x) for x in chemin.read_text(encoding="utf-8").splitlines()]


def comme_calcul(d):
    """Un envoi décrit par ce programme, dans les termes du calcul v2."""
    return {"bloc": d["bloc"], "temoin_dans_l_ordre_du_bloc": d["rang_dans_le_bloc"], "juge": d["juge"],
            "rendu": d["rendu"], "essai": d["essai"]}


def du_calcul(d):
    return {"bloc": d["bloc"], "temoin_dans_l_ordre_du_bloc": d["temoin_dans_l_ordre_du_bloc"],
            "juge": NOM_JUGE[d["juge"]], "rendu": d["rendu"], "essai": d["essai"]}


# --- tarifs, ordre, graines -------------------------------------------------------------------------------------------------------


def test_tarifs_des_cartes_egaux_au_calcul_v2(module_calcul):
    t = module_calcul.tarifs(str(M.DEPOT))
    assert t["par_appel"] == M.TARIF_DES_CARTES
    assert t["facteurs"]["haut"] == 1


def test_ordre_des_envois_celui_du_calcul_v2(tmp_path, configuration, module_calcul):
    chemin, h = ecrire_banque(tmp_path, configuration["items_juge"])
    banque, _ = M.lire_banque(chemin, h, configuration["items_juge"])
    plomberie, _ = M.lire_temoins_v2(M.DEPOT / M.TEMOINS_V2[0], PLOMBERIE)
    plan = M.plan_des_envois(banque, plomberie)
    attendu = list(module_calcul.sequence(M.N_TEMOINS))
    assert [(p["bloc"], p["rang"], p["juge"], p["rendu"]) for p in plan] == attendu
    assert len(plan) == 1004 and sum(p["bloc"] == "A" for p in plan) == 400 and sum(p["bloc"] == "B" for p in plan) == 600
    b = [p for p in plan if p["bloc"] == "B"]
    assert all(p["moitie"] == "lecture" for p in b[:300]) and all(p["moitie"] == "etalonnage" for p in b[300:])
    assert M.plan_des_envois(banque, plomberie) == plan          # tirage reproductible
    a = [p["temoin"] for p in plan if p["bloc"] == "A"][::2]
    assert sorted(a) == sorted(t["identifiant_interne"] for t in banque) and a != sorted(a)


def test_graines_de_la_racine_2026111935():
    import numpy as np
    ids = [f"x{k:03d}" for k in range(10)]
    ss = np.random.SeedSequence(2026111935, spawn_key=(2,))
    attendu = [ids[int(i)] for i in np.random.default_rng(ss).permutation(10)]
    assert M.ordre_tire("ordre-bloc-A", ids) == attendu
    assert M.RACINE_ORDRE == 2026111935 and M.CLES_TACHES == {"ordre-bloc-P": 1, "ordre-bloc-A": 2, "ordre-bloc-B": 3,
                                                               "identifiants-opaques": 4}


def test_aucun_flottant_dans_un_seuil():
    with pytest.raises(TypeError):
        M.centimes(88.36)
    with pytest.raises(TypeError):
        M.exacte(0.6)
    assert M.PLAFOND == Fraction(8836, 100) and M.SESSION == Fraction(3, 5)
    assert M.cout_lisible(0.073013) == Fraction(73013, 1000000)
    for illisible in (None, 0, 0.0, -1.0, float("nan"), float("inf"), True, "0.1"):
        assert M.cout_lisible(illisible) is None


# --- service des juges : empreintes avant import ----------------------------------------------------------------------------------


def test_service_des_juges_sain(fonctions):
    assert fonctions["version_juges"] == "juges-croises-v53"
    assert callable(fonctions["entree_une_fiche"]) and callable(fonctions["lire_verdict"])


def test_service_des_juges_artefact_empreinte(tmp_path):
    copie = tmp_path / "orchestrateur"
    (copie / "pole").mkdir(parents=True)
    for _n, rel, _a in M.MODULES_ORCHESTRATEUR:
        shutil.copyfile(M.ORCHESTRATEUR / rel, copie / rel)
    with open(copie / "pole" / "fiches_v53.py", "a", encoding="utf-8") as f:
        f.write("\n# modifié\n")
    with pytest.raises(M.Refus, match="fiches_v53.py d'une autre empreinte"):
        M.charger_service_des_juges(copie)


# --- plafond, arrêt dur par compteur : reproduction du calcul v2 ------------------------------------------------------------------


@pytest.mark.parametrize("cas", ["estimation", "haut"])
def test_plafond_cas_sain_tout_part(tmp_path, fonctions, consigne, configuration, sortie_calcul, module_calcul, cas):
    f = module_calcul.tarifs(str(M.DEPOT))["facteurs"][cas]
    banc = Banc(configuration["items_juge"], couts_au_facteur(f))
    rapport, racine, service = jouer(tmp_path, fonctions, consigne, configuration, banc)
    c = sortie_calcul["cas"][cas]
    assert rapport["envois_partis"] == 1004 == c["envoi_par_envoi_sans_refus"]["envois_partis"]
    assert rapport["arret"] is None
    assert Fraction(rapport["cumul_compte_exact_usd"]) == Fraction(c["total_du_plan_exact_usd"]) == sum(banc.servis)
    assert rapport["cumul_compte_usd"] == c["envoi_par_envoi_sans_refus"]["cumul_compte_a_l_arret_usd"]
    assert rapport["complets"]["bloc_A"] == 200 and rapport["complets"]["bloc_B"] == 200
    for ad in service.adaptateurs.values():                       # moyen du plafond de session, à chaque appel
        assert {a["budget_usd"] for a in ad.appels} == {0.6} and {a["max_tours"] for a in ad.appels} == {1}
    shutil.rmtree(racine)


def test_plafond_artefact_pire_cas_coupe_au_temoin_198(tmp_path, fonctions, consigne, configuration, sortie_calcul,
                                                       module_calcul):
    f = module_calcul.tarifs(str(M.DEPOT))["facteurs"]["pire"]
    banc = Banc(configuration["items_juge"], couts_au_facteur(f))
    rapport, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    c = sortie_calcul["cas"]["pire"]["envoi_par_envoi_sans_refus"]
    assert rapport["envois_partis"] == 996 == c["envois_partis"]
    assert rapport["cumul_compte_usd"] == "87.7701" == c["cumul_compte_a_l_arret_usd"]
    assert rapport["complets"]["bloc_A"] == 200 and rapport["complets"]["plomberie"] is True
    assert rapport["complets"]["bloc_B"] == 197 == c["complets"]["bloc_B"]
    assert rapport["complets"]["bloc_B_moitie_lecture"] == 100 and rapport["complets"]["bloc_B_moitie_etalonnage"] == 97
    assert rapport["complets"]["rangs_des_temoins_partiels_au_bloc_B"] == [198] == c["temoins_partiels_au_bloc_B"]
    arret = rapport["arret"]
    assert arret["motif"].startswith("plafond")
    assert comme_calcul(arret["premier_envoi_interdit"]) == du_calcul(c["premier_envoi_interdit_par_la_regle"])
    assert comme_calcul(arret["dernier_envoi_parti"]) == du_calcul(c["dernier_envoi_parti"])
    assert M.decimal_texte(Fraction(arret["cumul_compte"])) == c["premier_envoi_interdit_par_la_regle"]["cumul_compte_avant_usd"]
    assert Fraction(rapport["cumul_compte_exact_usd"]) + M.SESSION > M.PLAFOND >= Fraction(rapport["cumul_compte_exact_usd"])
    shutil.rmtree(racine)


def test_plafond_artefact_cout_releve_au_dessus_de_la_session(tmp_path, fonctions, consigne, configuration):
    banc = Banc(configuration["items_juge"], couts_au_facteur(1), cout_a={10: Fraction(61, 100)})
    rapport, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    assert rapport["envois_partis"] == 11
    assert rapport["arret"]["motif"] == "coût relevé au-dessus du plafond de session de 0,60 USD"
    reglement = [l for l in lignes_du_journal(racine) if l["type"] == "reglement"][-1]
    assert Fraction(reglement["compte"]) == Fraction(61, 100)        # compté tel quel, jamais sous-compté


def test_plafond_un_envoi_part_si_cumul_plus_reserve_egale_le_plafond(tmp_path):
    j = M.Journal(tmp_path / "j.jsonl", creer=True)
    j.ajouter({"type": "ouverture"})
    c = M.Compteur(j)
    k = 0
    while c.peut_envoyer():
        n = c.engager({"rendu": f"r{k}", "opaque": f"F{k:05x}"})
        c.regler(n, M.SESSION, {"nature": "refuse_ou_erreur", "succes": False})
        k += 1
    assert k == 147 and c.cumul() == Fraction(8820, 100)              # 147 × 0,60 = 88,20 ; 88,20 + 0,60 > 88,36
    with pytest.raises(RuntimeError):
        c.engager({"rendu": "interdit", "opaque": "F99999"})
    j.fermer()


# --- compteur, envoi refusé ----------------------------------------------------------------------------------------------------


def test_compteur_cas_sain_compte_au_cout_releve(tmp_path, fonctions, consigne, configuration):
    banc = Banc(configuration["items_juge"], couts_au_facteur(1))
    rapport, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    reglements = [l for l in lignes_du_journal(racine) if l["type"] == "reglement"]
    assert [Fraction(l["compte"]) for l in reglements] == banc.servis
    assert all(l["nature"] == "cout_releve" for l in reglements)
    shutil.rmtree(racine)


def test_compteur_artefact_tout_refuse_147_envois(tmp_path, fonctions, consigne, configuration, sortie_calcul):
    banc = Banc(configuration["items_juge"], couts_au_facteur(1), tout_refuser=True)
    rapport, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc, arret_de_plomberie=False)
    c = sortie_calcul["condition_iii_envoi_refuse_compte_au_pire"]["si_tous_les_envois_sont_refuses"]
    assert rapport["envois_partis"] == 147 == c["envois_partis"]
    assert rapport["cumul_compte_usd"] == "88.2000" and M.decimal_texte(Fraction(rapport["cumul_compte_exact_usd"]), 2) == \
        c["cumul_compte_a_l_arret_usd"]
    assert rapport["rendus_obtenus"] == 0 == c["rendus_obtenus"]
    assert comme_calcul(rapport["arret"]["premier_envoi_interdit"]) == du_calcul(c["premier_envoi_interdit_par_la_regle"])
    assert comme_calcul(rapport["arret"]["dernier_envoi_parti"]) == du_calcul(c["dernier_envoi_parti"])
    reglements = [l for l in lignes_du_journal(racine) if l["type"] == "reglement"]
    assert all(Fraction(l["compte"]) == M.SESSION for l in reglements) and len(reglements) == 147


def test_compteur_tout_refuse_avec_l_arret_de_plomberie(tmp_path, fonctions, consigne, configuration):
    """Le mode réel garde l'arrêt de la plomberie : un service qui refuse tout s'arrête au premier rendu de la plomberie,
    après l'envoi et son rejeu (écart au modèle du calcul v2, déclaré au rapport du développeur)."""
    banc = Banc(configuration["items_juge"], couts_au_facteur(1), tout_refuser=True)
    rapport, _, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    assert rapport["envois_partis"] == 2 and rapport["cumul_compte_usd"] == "1.2000"
    assert rapport["arret"]["motif"].startswith("plomberie")


def test_compteur_artefact_sans_cout_lisible_garde_non_rejoue(tmp_path, fonctions, consigne, configuration):
    banc = Banc(configuration["items_juge"], couts_au_facteur(1), sans_cout_pour=lambda i, m: i == 20)
    rapport, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    reglements = {l["n"]: l for l in lignes_du_journal(racine) if l["type"] == "reglement"}
    assert reglements[21]["nature"] == "sans_cout_lisible" and Fraction(reglements[21]["compte"]) == M.SESSION
    assert reglements[21]["succes"] is True and reglements[21]["lisible"] is True
    assert rapport["envois_partis"] == 1004                           # non rejoué
    shutil.rmtree(racine)


def test_compteur_exception_d_envoi_comptee_et_rejouee(tmp_path, fonctions, consigne, configuration):
    banc = Banc(configuration["items_juge"], couts_au_facteur(1), exception_a=30)
    rapport, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    reglements = {l["n"]: l for l in lignes_du_journal(racine) if l["type"] == "reglement"}
    assert reglements[31]["statut"] == "exception:ConnectionError" and Fraction(reglements[31]["compte"]) == M.SESSION
    assert reglements[32]["essai"] == 2 and reglements[32]["succes"] is True
    assert rapport["envois_partis"] == 1005
    shutil.rmtree(racine)


@pytest.mark.parametrize("cas", ["estimation", "haut", "pire"])
@pytest.mark.parametrize("r", [0, 1, 2, 3, 5, 10, 20, 40, 60, 80, 100])
def test_selon_les_envois_refuses(tmp_path, fonctions, consigne, configuration, sortie_calcul, module_calcul, cas, r):
    f = module_calcul.tarifs(str(M.DEPOT))["facteurs"][cas]
    banc = Banc(configuration["items_juge"], couts_au_facteur(f), refus_premiers=r)
    rapport, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    attendu = sortie_calcul["cas"][cas]["selon_les_envois_refuses"][str(r)]
    assert rapport["envois_partis"] == attendu["envois_partis"]
    assert rapport["complets"]["bloc_A"] == attendu["bloc_A_complets"]
    assert rapport["complets"]["bloc_B"] == attendu["bloc_B_complets"]
    assert rapport["complets"]["bloc_B_moitie_lecture"] == attendu["moitie_lecture_complets"]
    assert rapport["envois_refuses_comptes"] == r
    shutil.rmtree(racine)


# --- relance après panne ----------------------------------------------------------------------------------------------------------


def test_relance_apres_panne_relit_le_journal(tmp_path, fonctions, consigne, configuration, module_calcul):
    items = configuration["items_juge"]
    banque = ecrire_banque(tmp_path, items)
    racine = tmp_path / "run"
    racine.mkdir()
    banc = Banc(items, couts_au_facteur(1), panne_a=100)
    with pytest.raises(KeyboardInterrupt):
        M.executer(racine, banque[0], banque[1], PLOMBERIE, faire_service(racine, banc, fonctions, consigne, configuration),
                   {"commit_depot": "essai"})
    avant = lignes_du_journal(racine)
    assert avant[-1]["type"] == "engagement" and avant[-1]["n"] == 101          # engagement sans règlement
    banc2 = Banc(items, couts_au_facteur(1))
    rapport = M.executer(racine, banque[0], banque[1], PLOMBERIE,
                         faire_service(racine, banc2, fonctions, consigne, configuration), {"commit_depot": "essai"})
    apres = lignes_du_journal(racine)
    assert apres[:len(avant)] == avant                                           # jamais de remise à zéro
    orphelin = next(l for l in apres if l["type"] == "reglement" and l["n"] == 101)
    assert orphelin["nature"] == "engagement_sans_reglement" and Fraction(orphelin["compte"]) == M.SESSION
    relance = next(l for l in apres if l["type"] == "relance")
    assert relance["orphelins_regles_a_0_60"] == [101]
    rejeu = next(l for l in apres if l["type"] == "engagement" and l["n"] == 102)
    assert rejeu["rendu"] == avant[-1]["rendu"] and rejeu["essai"] == 2 and rejeu["opaque"] != avant[-1]["opaque"]
    total = module_calcul.cout_du_plan(M.N_TEMOINS, M.TARIF_DES_CARTES, 1)[2]
    assert rapport["envois_partis"] == 1005 and Fraction(rapport["cumul_compte_exact_usd"]) == total + M.SESSION
    m2 = json.loads((racine / "sortie" / "epreuve" / "manifeste-execution-2.json").read_text(encoding="utf-8"))
    assert m2["relance"] is True and m2["lecture_du_journal_au_lancement"]["orphelins"] == [101]
    assert rapport["complets"]["bloc_B"] == 200
    with pytest.raises(M.Refus, match="déjà servi"):
        M.executer(racine, banque[0], banque[1], PLOMBERIE,
                   faire_service(racine, Banc(items, couts_au_facteur(1)), fonctions, consigne, configuration), {})
    shutil.rmtree(racine)


def test_relance_refusee_apres_un_arret(tmp_path, fonctions, consigne, configuration, module_calcul):
    f = module_calcul.tarifs(str(M.DEPOT))["facteurs"]["pire"]
    banc = Banc(configuration["items_juge"], couts_au_facteur(f))
    rapport, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    assert rapport["arret"] is not None
    banque = tmp_path / "banque-run.json"
    with pytest.raises(M.Refus, match="aucune suite sous cette ligne"):
        M.executer(racine, banque, M.sha256_fichier(banque), PLOMBERIE,
                   faire_service(racine, Banc(configuration["items_juge"], couts_au_facteur(1)), fonctions, consigne,
                                 configuration), {})
    shutil.rmtree(racine)


def test_relance_journal_illisible_ou_absent(tmp_path, fonctions, consigne, configuration):
    items = configuration["items_juge"]
    banque = ecrire_banque(tmp_path, items)
    racine = tmp_path / "run"
    racine.mkdir()
    banc = Banc(items, couts_au_facteur(1), panne_a=5)
    with pytest.raises(KeyboardInterrupt):
        M.executer(racine, banque[0], banque[1], PLOMBERIE, faire_service(racine, banc, fonctions, consigne, configuration), {})
    journal = racine / "sortie" / "epreuve" / "journal-compteur.jsonl"
    octets = journal.read_bytes()
    journal.write_bytes(octets[:-7])                                     # dernière ligne coupée
    with pytest.raises(M.Refus, match="coupée"):
        M.executer(racine, banque[0], banque[1], PLOMBERIE,
                   faire_service(racine, Banc(items, couts_au_facteur(1)), fonctions, consigne, configuration), {})
    journal.write_bytes(octets.replace(b'"montant": "3/5"', b'"montant": "0/1"', 1))
    with pytest.raises(M.Refus, match="engagement hors forme"):
        M.executer(racine, banque[0], banque[1], PLOMBERIE,
                   faire_service(racine, Banc(items, couts_au_facteur(1)), fonctions, consigne, configuration), {})
    journal.unlink()                                                     # journal absent, dépôt non vide
    with pytest.raises(M.Refus, match="aucune remise à zéro"):
        M.executer(racine, banque[0], banque[1], PLOMBERIE,
                   faire_service(racine, Banc(items, couts_au_facteur(1)), fonctions, consigne, configuration), {})


# --- verdict illisible ------------------------------------------------------------------------------------------------------------


def test_verdict_illisible_sain_et_artefact(tmp_path, fonctions, consigne, configuration):
    items = configuration["items_juge"]
    sain, r1, _ = jouer(tmp_path, fonctions, consigne, configuration, Banc(items, couts_au_facteur(1)), nom="sain")
    assert sain["etat_des_juges"]["juge-argon"]["absents"] == 0
    assert sain["etat_des_juges"]["juge-argon"]["juge_non_mesure"] is False
    shutil.rmtree(r1)
    banc = Banc(items, couts_au_facteur(1), illisible_pour=lambda i, m: i >= 4 and m == MODELE["juge-argon"] and i % 7 < 2)
    art, r2, _ = jouer(tmp_path, fonctions, consigne, configuration, banc, nom="artefact")
    j = art["etat_des_juges"]["juge-argon"]
    assert j["absents"] > 0 and Fraction(j["part_d_absents"]) > Fraction(1, 10) and j["juge_non_mesure"] is True
    assert art["etat_des_juges"]["juge-opus"]["juge_non_mesure"] is False
    assert art["envois_partis"] == 1004                                 # réponse illisible : absente, comptée, non rejouée
    lecture = json.loads((r2 / "sortie" / "epreuve" / "verdicts-moitie-lecture-execution-1.json").read_text("utf-8"))
    assert any(x["verdict"] is None and x["motif"] == "verdict illisible" for x in lecture["rendus"])
    shutil.rmtree(r2)


def test_plomberie_illisible_arrete(tmp_path, fonctions, consigne, configuration):
    banc = Banc(configuration["items_juge"], couts_au_facteur(1), illisible_pour=lambda i, m: i == 1)
    rapport, _, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    assert rapport["envois_partis"] == 2 and rapport["arret"]["motif"] == "plomberie : réponse illisible"


@pytest.mark.parametrize("facteur,arret", [(Fraction(3), False), (Fraction(3) + Fraction(1, 10 ** 9), True)])
def test_plomberie_trois_fois_le_tarif(tmp_path, fonctions, consigne, configuration, sortie_calcul, facteur, arret):
    banc = Banc(configuration["items_juge"], couts_au_facteur(facteur))
    rapport, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    if arret:
        assert rapport["envois_partis"] == 1
        assert rapport["arret"]["motif"] == "plomberie : coût par appel au-delà de trois fois le tarif des cartes"
    else:
        c = sortie_calcul["condition_i_arret_dur_par_compteur"]["au_seuil_d_arret_de_la_plomberie_trois_fois_le_tarif"]
        assert rapport["envois_partis"] == 630 == c["envois_partis"]
        assert rapport["cumul_compte_usd"] == c["cumul_compte_a_l_arret_usd"]
        assert rapport["complets"]["bloc_B"] == 75 == c["complets"]["bloc_B"]
    shutil.rmtree(racine)


# --- modèle servi -----------------------------------------------------------------------------------------------------------------


def test_modele_servi_sain_et_artefact(tmp_path, fonctions, consigne, configuration):
    items = configuration["items_juge"]
    banc = Banc(items, couts_au_facteur(1), modele_change_a=50)
    rapport, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    assert set(rapport["roles_arretes"]) == {"juge-argon"}
    assert rapport["etat_des_juges"]["juge-argon"]["modele_servi_premier"] == MODELE["juge-argon"]
    lignes = lignes_du_journal(racine)
    assert sum(1 for l in lignes if l["type"] == "arret_du_role") == 1
    opus = [l for l in lignes if l["type"] == "engagement" and l["juge"] == "juge-opus"]
    argon = [l for l in lignes if l["type"] == "engagement" and l["juge"] == "juge-argon"]
    assert len(opus) == 2 + 200 + 200 and len(argon) < 30                 # l'autre rôle continue, aucune bascule
    assert rapport["etat_des_juges"]["juge-opus"]["modele_servi_premier"] == MODELE["juge-opus"]
    shutil.rmtree(racine)


# --- réponses identiques ----------------------------------------------------------------------------------------------------------


@pytest.mark.parametrize("identiques,part", [(False, "0"), (True, "1")])
def test_reponses_identiques(tmp_path, fonctions, consigne, configuration, identiques, part):
    banc = Banc(configuration["items_juge"], couts_au_facteur(1), identiques=identiques)
    rapport, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    for j in M.JUGES:
        e = rapport["etat_des_juges"][j]
        assert e["part_identique"] == part and e["rho_prime_non_mesure"] is identiques
    assert rapport["etat_des_juges"]["juge-argon"]["paires_de_rendus"] == 600
    shutil.rmtree(racine)


# --- identifiant opaque neuf, vérité non servie --------------------------------------------------------------------------------


def test_identifiant_opaque_neuf_sain(tmp_path, fonctions, consigne, configuration):
    banc = Banc(configuration["items_juge"], couts_au_facteur(1))
    _, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    lignes = lignes_du_journal(racine)
    eng = [l for l in lignes if l["type"] == "engagement"]
    assert len({l["opaque"] for l in eng}) == len(eng) == 1004
    t = eng[-1]["temoin"]
    memes = [l for l in eng if l["temoin"] == t]
    fiches = [json.loads((racine / "sortie" / "epreuve" / "entrees-servies" / f"envoi-{l['n']:05d}.json").read_text("utf-8"))
              for l in memes]
    assert len(memes) == 5 and len({f.pop("identifiant") for f in fiches}) == 5     # A : 2 rendus ; B : 3 rendus
    assert all(f == fiches[0] for f in fiches)                           # texte du témoin identique, identifiant neuf
    for x in (racine / "sortie" / "epreuve" / "entrees-servies").iterdir():
        assert b"L3-T" not in x.read_bytes()                              # aucun identifiant interne servi
    assert not any("L3-T" in str(d) for d in (racine / "sortie" / "appels").rglob("*"))
    shutil.rmtree(racine)


def test_identifiant_opaque_neuf_artefact():
    with pytest.raises(M.Refus, match="déjà servi"):
        M.garde_identifiant_neuf("F00abc", {"F00abc"})
    with pytest.raises(M.Refus, match="forme"):
        M.garde_identifiant_neuf("L3-T001", set())


def test_verite_non_servie_sain(fonctions, consigne, configuration):
    contenu = {"titre": "Carte d'essai", "mecanisme": "Texte factice sans étiquette."}
    texte = fonctions["entree_une_fiche"](consigne, {"contenu": contenu}, configuration["etiquettes_interdites_fixes"],
                                          identifiant_servi="F0a1b2")
    M.garde_verite_non_servie(texte, contenu, "F0a1b2", ("L3-T001", "L3-T001|juge-opus|r1"), configuration["items_juge"],
                              fonctions["normaliser_texte"])


@pytest.mark.parametrize("contenu", [
    {"titre": "Carte d'essai", "mecanisme": "Témoin de classe connue."},
    {"titre": "Carte d'essai", "mecanisme": "Défaut planté : reserves_tenues."},
    {"titre": "Carte d'essai L3-T001", "mecanisme": "Texte factice."}])
def test_verite_non_servie_artefact(fonctions, consigne, configuration, contenu):
    texte = fonctions["entree_une_fiche"](consigne, {"contenu": contenu}, configuration["etiquettes_interdites_fixes"],
                                          identifiant_servi="F0a1b2")
    with pytest.raises(M.Refus, match="vérité non servie"):
        M.garde_verite_non_servie(texte, contenu, "F0a1b2", ("L3-T001", "L3-T001|juge-opus|r1"),
                                  configuration["items_juge"], fonctions["normaliser_texte"])


def test_verite_non_servie_dans_l_execution_refus_de_servir(tmp_path, fonctions, consigne, configuration):
    items = configuration["items_juge"]
    banque = ecrire_banque(tmp_path, items, contenu_de=lambda k, c: dict(c, titre=c["titre"] + (" classe" if k == 7 else "")))
    banc = Banc(items, couts_au_facteur(1))
    rapport, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc, banque=banque)
    assert rapport["arret"]["motif"].startswith("refus de servir : vérité non servie")
    lignes = lignes_du_journal(racine)
    assert not any(l["type"] == "engagement" and l["temoin"] == "L3-T007" for l in lignes)   # rien envoyé ni compté


def test_temoins_v2_de_la_plomberie_passent_la_garde(fonctions, consigne, configuration):
    brut = json.loads(M.lire_par_empreinte(M.DEPOT / M.TEMOINS_V2[0], M.TEMOINS_V2[1], "témoins v2"))
    for t in brut["temoins"]:
        texte = fonctions["entree_une_fiche"](consigne, {"contenu": t["contenu"]},
                                              configuration["etiquettes_interdites_fixes"], identifiant_servi="F0a1b2")
        M.garde_verite_non_servie(texte, t["contenu"], "F0a1b2", (f"v2:{t['id']}", f"v2:{t['id']}|juge-opus|r1"),
                                  configuration["items_juge"], fonctions["normaliser_texte"])


# --- moyen du plafond de session ---------------------------------------------------------------------------------------------------


def test_moyen_du_plafond_de_session_artefact(tmp_path, fonctions, consigne, configuration):
    items = configuration["items_juge"]
    banque = ecrire_banque(tmp_path, items)
    racine = tmp_path / "run"
    racine.mkdir()
    service = faire_service(racine, Banc(items, couts_au_facteur(1)), fonctions, consigne, configuration, sans_moyen=True)
    with pytest.raises(M.Refus, match="pas de départ"):
        M.executer(racine, banque[0], banque[1], PLOMBERIE, service, {})
    assert not (racine / "sortie" / "epreuve" / "journal-compteur.jsonl").exists()
    reel = faire_service(racine, Banc(items, couts_au_facteur(1)), fonctions, consigne, configuration, nature="reel")
    with pytest.raises(M.Refus, match="pas de départ"):                  # un factice ne vaut jamais en mode réel
        M.exiger_moyen_du_plafond_de_session(reel)
    with pytest.raises(M.Refus, match="mode essai"):
        M.executer(racine, banque[0], banque[1], PLOMBERIE, reel, {}, arret_de_plomberie=False)


# --- verdicts de la v9 ------------------------------------------------------------------------------------------------------------


def test_verdicts_de_la_v9_sain(tmp_path):
    assert M.garde_chemins([tmp_path / "banque.json", tmp_path / "run"])


@pytest.mark.parametrize("rel", ["coffre/verdicts.json", "sortie/coffre-course/x.json",
                                 "archives-reponses-modeles/auto-conception-course-v9/fiches.json"])
def test_verdicts_de_la_v9_artefact(tmp_path, rel):
    with pytest.raises(M.Refus, match="verdicts de la v9"):
        M.garde_chemins([tmp_path / rel])


def test_verdicts_de_la_v9_racines_interdites():
    for r in M.RACINES_INTERDITES:
        with pytest.raises(M.Refus, match="verdicts de la v9"):
            M.garde_chemins([str(r) + "/x.json"])


def test_verdicts_de_la_v9_dans_l_execution(tmp_path, fonctions, consigne, configuration):
    items = configuration["items_juge"]
    (tmp_path / "coffre").mkdir()
    banque = ecrire_banque(tmp_path / "coffre", items)
    racine = tmp_path / "run"
    racine.mkdir()
    with pytest.raises(M.Refus, match="verdicts de la v9"):
        M.executer(racine, banque[0], banque[1], PLOMBERIE,
                   faire_service(racine, Banc(items, couts_au_facteur(1)), fonctions, consigne, configuration), {})


# --- banque scellée -----------------------------------------------------------------------------------------------------------------


def test_banque_scellee_sain_et_artefacts(tmp_path, configuration):
    items = configuration["items_juge"]
    chemin, h = ecrire_banque(tmp_path, items)
    assert len(M.lire_banque(chemin, h, items)[0]) == 200
    with pytest.raises(M.Refus, match="empreinte"):
        M.lire_banque(chemin, "0" * 64, items)
    Path(str(chemin) + ".sha256").unlink()
    with pytest.raises(M.Refus, match="non scellé"):
        M.lire_banque(chemin, h, items)
    autre, h2 = ecrire_banque(tmp_path, items, n=198, nom="courte.json")
    with pytest.raises(M.Refus, match="198 témoins"):
        M.lire_banque(autre, h2, items)


# --- ligne de GO -------------------------------------------------------------------------------------------------------------------

REGISTRE = (
    "| id | accordé | type | périmètre | plafond | échéance | par | réf |\n"
    "|---|---|---|---|---|---|---|---|\n"
    "| GO-2026-11-20-26 | 2026-11-20 | calcul | **Organisme, ligne 3, étage 2 à 200 témoins** : accord de calcul. "
    "| 88,36 USD | 2026-11-30 | Lazar | mot |\n"
    "| GO-2026-11-20-90 | 2026-11-20 | calcul | Organisme, ligne 1, palier 0b | 88,36 USD | 2026-11-30 | Lazar | mot |\n"
    "| GO-2026-11-20-91 | 2026-11-20 | calcul | Organisme, ligne 3, étage 2 | 88,35 USD | 2026-11-30 | Lazar | mot |\n"
    "| GO-2026-11-20-92 | 2026-11-20 | décision | Organisme, ligne 3, étage 2 | 88,36 USD | 2026-11-30 | Lazar | mot |\n"
    "| GO-2026-11-20-93 | 2026-11-20 | calcul | Organisme, ligne 3, étage 2 | 88,36 USD | 2026-11-30 | Lazar | mot |\n"
    "| GO-2026-11-20-94 | 2026-11-20 | décision | Révocation de GO-2026-11-20-93 | — | — | Lazar | mot |\n")


def test_ligne_de_go_saine():
    import datetime as dt
    go = M.verifier_ligne_de_go(REGISTRE, "GO-2026-11-20-26", dt.date(2026, 11, 20))
    assert go["plafond_centimes"] == M.PLAFOND_C == 8836


@pytest.mark.parametrize("go_id,jour,motif", [
    ("GO-2026-11-20-77", (2026, 11, 20), "0 ligne"),
    ("GO-2026-11-20-26", (2026, 12, 1), "hors de sa période"),
    ("GO-2026-11-20-90", (2026, 11, 20), "autre périmètre"),
    ("GO-2026-11-20-91", (2026, 11, 20), "montant différent"),
    ("GO-2026-11-20-92", (2026, 11, 20), "calcul"),
    ("GO-2026-11-20-93", (2026, 11, 20), "révoquée"),
    ("go-26", (2026, 11, 20), "identifiant")])
def test_ligne_de_go_artefacts(go_id, jour, motif):
    import datetime as dt
    with pytest.raises(M.Refus, match=motif):
        M.verifier_ligne_de_go(REGISTRE, go_id, dt.date(*jour))


def _argv(tmp_path, banque, sha, decl, decl_sha, go="GO-2026-11-20-26"):
    return ["--reel", "--go-id", go, "--banque", str(banque), "--banque-sha", sha, "--declaration", str(decl),
            "--declaration-sha", decl_sha, "--sortie", str(tmp_path / "run"), "--plomberie", "t01,t02",
            "--nom-cle-claude", "NOM_FACTICE"]


def test_mode_reel_refuse_avant_tout_service(tmp_path, configuration):
    import datetime as dt
    items = configuration["items_juge"]
    banque, h = ecrire_banque(tmp_path, items)
    decl = tmp_path / "declaration.json"
    octets = M.json_octets({"fournisseurs": {"claude": {}, "argon": {}}})
    decl.write_bytes(octets)
    hd = M.sha256_octets(octets)
    Path(str(decl) + ".sha256").write_text(f"{hd}  declaration.json\n", encoding="utf-8")
    appels = []

    def constructeur(**kw):
        appels.append(kw)
        return None, {}

    def registre():
        return {"texte": REGISTRE, "commit": "essai", "sha256": "essai"}

    jour = dt.date(2026, 11, 20)
    cas = [
        (["--reel"], {}, "--go-id"),
        (_argv(tmp_path, banque, h, decl, hd, go="GO-2026-11-20-90"), {}, "autre périmètre"),
        (_argv(tmp_path, banque, h, decl, hd), {"GO_ID": "GO-2026-11-20-93"}, "GO_ID"),
        (_argv(tmp_path, banque, "0" * 64, decl, hd), {}, "banque de témoins"),
        (_argv(tmp_path, banque, h, decl, "0" * 64), {}, "déclaration des relais"),
        (_argv(tmp_path, banque, h, tmp_path / "absente.json", hd), {}, "déclaration des relais"),
        (_argv(tmp_path, banque, h, decl, hd), {"EXEMPLE_API_KEY": "x"}, "noms de variables de clé"),
        (_argv(tmp_path, banque, h, decl, hd), {"VARIABLE_HORS_LISTE": "x"}, "non épuré"),          # v2, mère (3)
        (_argv(tmp_path, banque, h, decl, hd)[:-1] + ["nom-minuscule"], {}, "nom de variable"),     # v2, mère (2)
    ]
    for argv, env, motif in cas:
        with pytest.raises(M.Refus, match=motif):
            M.preparer_reel(argv, dict(ENV_BASE, **env), jour, lire_registre=registre, construire_service=constructeur)
    assert appels == []                                                  # aucun service construit, aucun relais touché
    prep = M.preparer_reel(_argv(tmp_path, banque, h, decl, hd), dict(ENV_BASE), jour, lire_registre=registre,
                           construire_service=constructeur)
    assert len(appels) == 1 and prep["contexte"]["ligne_de_go"]["id"] == "GO-2026-11-20-26"


# --- dépôt scellé ------------------------------------------------------------------------------------------------------------------


def test_depot_scelle_et_manifeste(tmp_path, fonctions, consigne, configuration):
    banc = Banc(configuration["items_juge"], couts_au_facteur(1))
    rapport, racine, _ = jouer(tmp_path, fonctions, consigne, configuration, banc)
    depot = racine / "sortie" / "epreuve"
    for nom, h in rapport["depots"].items():
        assert M.sha256_fichier(depot / nom) == h
        assert (depot / (nom + ".sha256")).read_text(encoding="utf-8").split()[0] == h
    m = json.loads((depot / "manifeste-execution-1.json").read_text(encoding="utf-8"))
    assert m["graines"]["racine"] == 2026111935 and m["consigne_servie_sha256"] == M.CONSIGNE_JUGE[1]
    assert m["plan"] == {"P": 4, "A": 400, "B": 600, "total": 1004}
    assert m["moyen_du_plafond_de_session"]["juge-opus"]["type"] == "factice"
    assert m["service_des_juges"]["modules"]["pole/juges_croises_v53.py"].startswith("c4c6ab12")
    lecture = json.loads((depot / "verdicts-moitie-lecture-execution-1.json").read_text(encoding="utf-8"))
    assert len(lecture["rendus"]) == 100 * 2 + 100 * 3
    assert not any(k in x for x in lecture["rendus"] for k in ("classe", "item", "niveau"))   # aucune vérité au dépôt
    assert len(list((depot / "reponses-brutes").iterdir())) == 1004
    shutil.rmtree(racine)


# --- v2 : corrections de la contre-lecture (C1, C2, C3) et décisions de la mère (2), (3) --------------------------------------


def _panne_puis(tmp_path, fonctions, consigne, configuration, panne_a, banque=None):
    items = configuration["items_juge"]
    banque = banque or ecrire_banque(tmp_path, items)
    racine = tmp_path / "run"
    racine.mkdir()
    banc = Banc(items, couts_au_facteur(1), panne_a=panne_a)
    with pytest.raises(KeyboardInterrupt):
        M.executer(racine, banque[0], banque[1], PLOMBERIE, faire_service(racine, banc, fonctions, consigne, configuration),
                   {"commit_depot": "essai"})
    return racine, banque


def _relancer(racine, banque, fonctions, consigne, configuration, plomberie=PLOMBERIE, banc=None):
    banc = banc or Banc(configuration["items_juge"], couts_au_facteur(1))
    return M.executer(racine, banque[0], banque[1], plomberie,
                      faire_service(racine, banc, fonctions, consigne, configuration), {"commit_depot": "essai"})


def test_c1_ouverture_porte_banque_et_plomberie(tmp_path, fonctions, consigne, configuration):
    racine, banque = _panne_puis(tmp_path, fonctions, consigne, configuration, 10)
    ouverture = lignes_du_journal(racine)[0]
    assert ouverture["banque_sha256"] == banque[1] and ouverture["plomberie"] == list(PLOMBERIE)
    rapport = _relancer(racine, banque, fonctions, consigne, configuration)     # cas sain : même banque, même plomberie
    assert rapport["arret"] is None and rapport["envois_partis"] == 1005
    shutil.rmtree(racine)


def test_c1_relance_sur_une_autre_banque_refusee(tmp_path, fonctions, consigne, configuration):
    items = configuration["items_juge"]
    racine, banque = _panne_puis(tmp_path, fonctions, consigne, configuration, 100)
    autre = ecrire_banque(tmp_path, items, nom="autre-banque.json",
                          contenu_de=lambda k, c: dict(c, titre=c["titre"] + " (autre banque)"))
    assert autre[1] != banque[1]
    avant = lignes_du_journal(racine)
    with pytest.raises(M.Refus, match="banque ou témoins de plomberie différents"):
        _relancer(racine, autre, fonctions, consigne, configuration)
    with pytest.raises(M.Refus, match="banque ou témoins de plomberie différents"):
        _relancer(racine, banque, fonctions, consigne, configuration, plomberie=("t01", "t03"))
    assert lignes_du_journal(racine) == avant                                    # rien écrit, rien envoyé


def test_c1_rendu_du_journal_hors_du_plan_refuse(tmp_path, fonctions, consigne, configuration):
    racine, banque = _panne_puis(tmp_path, fonctions, consigne, configuration, 6)
    journal = racine / "sortie" / "epreuve" / "journal-compteur.jsonl"
    lignes = [json.loads(x) for x in journal.read_text(encoding="utf-8").splitlines()]
    k = next(i for i, l in enumerate(lignes) if l["type"] == "engagement")
    lignes[k]["rendu"] = "hors-du-plan|juge-opus|r1"
    journal.write_bytes(b"".join((json.dumps(l, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
                                 for l in lignes))
    with pytest.raises(M.Refus, match="n'est pas au plan"):
        _relancer(racine, banque, fonctions, consigne, configuration)


def test_c2_panne_entre_le_dossier_d_appel_et_l_engagement(tmp_path, fonctions, consigne, configuration):
    racine, banque = _panne_puis(tmp_path, fonctions, consigne, configuration, 100)
    avant = lignes_du_journal(racine)
    orphelin = avant[-1]
    assert orphelin["type"] == "engagement"
    servis = {l["opaque"] for l in avant if l["type"] == "engagement"}
    prochain = M.Opaques(servis).neuf()                                          # premier identifiant tiré à la relance
    laisse = racine / "sortie" / "appels" / orphelin["juge"] / prochain
    laisse.mkdir(parents=True)                                                   # artefact : dossier créé, aucun engagement
    rapport = _relancer(racine, banque, fonctions, consigne, configuration)
    apres = lignes_du_journal(racine)
    rejeu = next(l for l in apres if l["type"] == "engagement" and l["n"] == orphelin["n"] + 1)
    assert rejeu["opaque"] == prochain and rejeu["rendu"] == orphelin["rendu"] and rejeu["essai"] == 2
    assert rapport["arret"] is None and rapport["envois_partis"] == 1005
    shutil.rmtree(racine)


@pytest.mark.parametrize("illisible", [False, True])
def test_c3_controle_de_plomberie_rejoue_a_la_relance(tmp_path, fonctions, consigne, configuration, monkeypatch, illisible):
    """Panne forcée entre le règlement du second rendu de plomberie et son contrôle ; à la relance, le contrôle est rejoué
    sans envoi : plomberie illisible, arrêt, aucun envoi du bloc A (artefact) ; plomberie lisible, le plan continue (sain)."""
    items = configuration["items_juge"]
    banque = ecrire_banque(tmp_path, items)
    racine = tmp_path / "run"
    racine.mkdir()
    original = M.motif_plomberie
    appels = {"n": 0}

    def controle_puis_panne(s, compteur, juge):
        appels["n"] += 1
        if appels["n"] == 2:
            raise KeyboardInterrupt("panne simulée entre le règlement et le contrôle de la plomberie")
        return original(s, compteur, juge)

    monkeypatch.setattr(M, "motif_plomberie", controle_puis_panne)
    banc = Banc(items, couts_au_facteur(1), illisible_pour=(lambda i, m: illisible and i == 1))
    with pytest.raises(KeyboardInterrupt):
        M.executer(racine, banque[0], banque[1], PLOMBERIE, faire_service(racine, banc, fonctions, consigne, configuration),
                   {"commit_depot": "essai"})
    avant = lignes_du_journal(racine)
    assert sum(1 for l in avant if l["type"] == "reglement") == 2 and avant[-1]["type"] == "reglement"
    monkeypatch.setattr(M, "motif_plomberie", original)
    rapport = _relancer(racine, banque, fonctions, consigne, configuration)
    eng = [l for l in lignes_du_journal(racine) if l["type"] == "engagement"]
    if illisible:
        assert rapport["arret"]["motif"] == "plomberie : réponse illisible"
        assert rapport["envois_partis"] == 2 and not any(l["bloc"] == "A" for l in eng)
    else:
        assert rapport["arret"] is None and rapport["envois_partis"] == 1004
    shutil.rmtree(racine)


def test_environnement_epure_sain_et_artefact():
    sain = {"PATH": "/usr/bin", "HOME": "/tmp", "LANG": "C.UTF-8", "LC_CTYPE": "C.UTF-8", "GO_ID": "GO-2026-11-20-26",
            **ENV_BASE}
    assert M.exiger_environnement_epure(sain) == sorted(sain)
    assert M.exiger_environnement_epure(dict(ENV_BASE)) == ["HTTPS_PROXY"]
    with pytest.raises(M.Refus, match="non épuré"):
        M.exiger_environnement_epure(dict(sain, VARIABLE_HORS_LISTE="x"))
    with pytest.raises(M.Refus, match="non épuré"):
        M.exiger_environnement_epure(dict(sain, ALL_PROXY="http://127.0.0.1:1"))


def test_mode_reel_environnement_liste_blanche_accepte(tmp_path, configuration):
    import datetime as dt
    banque, h = ecrire_banque(tmp_path, configuration["items_juge"])
    decl = tmp_path / "declaration.json"
    octets = M.json_octets({"fournisseurs": {"claude": {}, "argon": {}}})
    decl.write_bytes(octets)
    hd = M.sha256_octets(octets)
    Path(str(decl) + ".sha256").write_text(f"{hd}  declaration.json\n", encoding="utf-8")
    appels = []
    env = {"PATH": "/usr/bin", "HOME": "/tmp", "LC_CTYPE": "C.UTF-8", "GO_ID": "GO-2026-11-20-26", **ENV_BASE}
    M.preparer_reel(_argv(tmp_path, banque, h, decl, hd), env, dt.date(2026, 11, 20),
                    lire_registre=lambda: {"texte": REGISTRE, "commit": "essai", "sha256": "essai"},
                    construire_service=lambda **kw: (appels.append(kw), (None, {}))[1])
    assert len(appels) == 1 and appels[0]["nom_cle_claude"] == "NOM_FACTICE"


# --- v3 : correction de la mère (14:10Z) ----------------------------------------------------------------------------------------


def _preparer(tmp_path, configuration, env):
    import datetime as dt
    banque, h = ecrire_banque(tmp_path, configuration["items_juge"])
    decl = tmp_path / "declaration.json"
    octets = M.json_octets({"fournisseurs": {"claude": {}, "argon": {}}})
    decl.write_bytes(octets)
    hd = M.sha256_octets(octets)
    Path(str(decl) + ".sha256").write_text(f"{hd}  declaration.json\n", encoding="utf-8")
    appels = []
    M.preparer_reel(_argv(tmp_path, banque, h, decl, hd), env, dt.date(2026, 11, 20),
                    lire_registre=lambda: {"texte": REGISTRE, "commit": "essai", "sha256": "essai"},
                    construire_service=lambda **kw: (appels.append(kw), (None, {}))[1])
    return appels


def test_v3_depart_reel_exige_https_proxy(tmp_path, configuration):
    """Cas sain : HTTPS_PROXY présente (avec les variables du mandataire et des certificats relevées dans ce conteneur) :
    le départ passe la garde. Artefact : HTTPS_PROXY absente : refus avant tout service."""
    noms_du_conteneur = ("CURL_CA_BUNDLE", "NODE_EXTRA_CA_CERTS", "REQUESTS_CA_BUNDLE", "SSL_CERT_FILE", "HTTPS_PROXY",
                         "https_proxy", "NO_PROXY", "no_proxy")
    sain = {n: "valeur-factice" for n in noms_du_conteneur}
    sain.update(PATH="/usr/bin", HOME="/tmp")
    (tmp_path / "sain").mkdir()
    assert len(_preparer(tmp_path / "sain", configuration, sain)) == 1
    sans = {k: v for k, v in sain.items() if k != "HTTPS_PROXY"}
    (tmp_path / "artefact").mkdir()
    with pytest.raises(M.Refus, match="variables exigées absentes"):
        _preparer(tmp_path / "artefact", configuration, sans)


def test_v3_liste_blanche_elargie():
    for n in ("HTTPS_PROXY", "HTTP_PROXY", "NO_PROXY", "https_proxy", "http_proxy", "no_proxy", "SSL_CERT_FILE",
              "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE", "NODE_EXTRA_CA_CERTS", "RR_ANTHROPIC_API_KEY_LUC", "GEMINI_API_KEY"):
        assert n in M.VARIABLES_PERMISES
    assert M.VARIABLES_EXIGEES == ("HTTPS_PROXY",)
    with pytest.raises(M.Refus, match="non épuré"):                    # l'essai de refus hors liste est gardé
        M.exiger_environnement_epure(dict(ENV_BASE, VARIABLE_HORS_LISTE="x"))


@pytest.mark.parametrize("nom", ["RR_ANTHROPIC_API_KEY_LUC", "GEMINI_API_KEY"])
def test_v3_nom_de_cle_dans_la_liste_blanche_mais_refuse_par_la_garde_des_cles(tmp_path, configuration, nom):
    """Constat porté à la mère, non tranché : le nom est dans la liste blanche (garde de l'environnement épuré), mais la garde
    des noms de clé, reprise du précédent et gardée sans changement, refuse toujours le départ si ce nom est présent."""
    assert M.exiger_environnement_epure(dict(ENV_BASE, **{nom: "valeur-factice"})) == sorted([nom, "HTTPS_PROXY"])
    with pytest.raises(M.Refus, match="noms de variables de clé"):
        _preparer(tmp_path, configuration, dict(ENV_BASE, **{nom: "valeur-factice"}))
