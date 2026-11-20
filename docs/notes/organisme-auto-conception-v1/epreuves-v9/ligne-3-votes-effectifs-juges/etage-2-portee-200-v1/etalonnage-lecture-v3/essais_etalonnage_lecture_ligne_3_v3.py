"""Essais de `etalonner_ligne_3_v3.py` et `lire_ligne_3_v3.py` (pytest) — ligne 3 de l'organisme v9, étage 2 à 200 — v3.

Version 3 (R12 ; la v2 est gardée) : les essais de la v2 sur les modules v3 ; le fichier de fragments factice porte un
fragment « voisins » piège « reprise assumée » (non citant), et la banque factice porte `fragments_sha256` ; essais neufs :
quatrième nature séparée des conformes non citants (sain et artefact) ; comparaison de `fragments_sha256` de la banque (sain
et deux artefacts).

Texte de la v2 :

Version 2 (R12 ; la v1 est gardée) : les essais de la v1 sur les modules v2 ; le monde factice porte en plus un journal de
construction et un fichier de fragments au format du générateur v3 ; essais neufs : témoin complet = cinq rendus obtenus
(les deux essais du contre-lecteur, `essai_correction_n1_v1.py`, repris) ; cartes tombées sur `reserves_tenues` (plant
exact, cas sain et artefact ; refus du journal et des fragments) ; pièce liée à son dossier.

Texte de la v1 :

**Aucun verdict réel n'existe : tout s'éprouve sur des verdicts factices**, rendus par des juges scriptés (loi 1 de l'étage 1,
emboîtée : choc commun ρ aux cinq rendus d'un témoin ; sinon, par juge, choc propre au juge de probabilité
(ρ′ − ρ) / (1 − ρ) ; sinon tirage propre ; taux p égal dans les deux classes : la corrélation des erreurs entre juges vaut
ρ, celle d'un juge avec lui-même ρ′, valeurs plantées connues). Les dépôts factices sont écrits **par les fonctions mêmes du
code d'appel v4** (`Journal`, `Compteur`, `deposer`, chargées après vérification de l'empreinte 082d19d6…), et chaque
verdict est lu par `lire_verdict` de `juges_croises_v53.py` (chargé par la garde d'empreintes du code d'appel) : le format
lu par l'étalonnage et la lecture est celui que le code d'appel écrira. Graines des essais : racine 2026111930 seule.
Aucun réseau, aucune clé, aucun appel de modèle ; aucun chemin du coffre ni de l'archive des réponses n'est ouvert.
"""
from __future__ import annotations

import hashlib
import json
import sys
import types
from fractions import Fraction
from pathlib import Path

import numpy as np
import pytest

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import etalonner_ligne_3_v3 as ET  # noqa: E402
import lire_ligne_3_v3 as LI  # noqa: E402

CODE_APPEL_V4 = (ET.L3 / "etage-2-portee-200-v1" / "code-appel-v4" / "epreuve_juges_reels_ligne_3_v4.py",
                 ET.CODE_APPEL_V4_SHA256)
RACINE_ESSAIS = 2026111930
CLES_ESSAIS = {"banque": 101, "juges": 102}
BANC = ET.charger_banc()


def code_appel():
    nom = "_code_appel_v4_essais_lecture"
    if nom in sys.modules:
        return sys.modules[nom]
    octets = CODE_APPEL_V4[0].read_bytes()
    assert hashlib.sha256(octets).hexdigest() == CODE_APPEL_V4[1]
    m = types.ModuleType(nom)
    m.__file__ = str(CODE_APPEL_V4[0])
    sys.modules[nom] = m
    exec(compile(octets, str(CODE_APPEL_V4[0]), "exec"), m.__dict__)
    m.__lire_verdict__ = m.charger_service_des_juges()["lire_verdict"]
    return m


def rng(cle, sous=0):
    return np.random.default_rng(np.random.SeedSequence(RACINE_ESSAIS, spawn_key=(CLES_ESSAIS[cle], sous)))


def sha_compagnon(chemin) -> str:
    return Path(str(chemin) + ".sha256").read_text(encoding="utf-8").split()[0]


# --- monde factice ---------------------------------------------------------------------------------------------------------


def banque_factice(n=200):
    """n/2 bons, n/2 mauvais ; mauvais : items en cycle, niveaux 1 déclaré pour 2 nets et 2 discrets ; moitiés alternées dans
    chaque classe (n/4 par moitié et par classe) ; contenu factice."""
    temoins = []
    for i in range(n):
        bon = i < n // 2
        k = i if bon else i - n // 2
        temoins.append({"identifiant_interne": f"T{i:05d}", "classe": "bon" if bon else "mauvais",
                        "item": None if bon else ET.ITEMS[k % 5],
                        "niveau": None if bon else ("declare", "net", "net", "discret", "discret")[(k // 5) % 5],
                        "citation": (k // 2) % 2 == 0, "moitie": "lecture" if k % 2 == 0 else "etalonnage",
                        "contenu": {"titre": f"témoin factice {i}"}})
    return temoins


def erreurs_scriptees(g, n, p_o, p_a, rho, rho_prime):
    """Erreurs (n, 5) : colonnes [Opus r1, Argon r1, Opus r2, Argon r2, Argon r3] (ordre de `ET.COLONNES`)."""
    q = (rho_prime - rho) / (1.0 - rho)
    juge_de = np.array([0, 1, 0, 1, 1])
    p = np.array([p_o, p_a, p_o, p_a, p_a])
    commun = g.random((n, 1))
    par_juge = g.random((n, 2))
    propre = g.random((n, 5))
    tous = g.random((n, 1)) < rho
    choc_juge = g.random((n, 2)) < q
    lu = np.where(choc_juge[:, juge_de], par_juge[:, juge_de], propre)
    lu = np.where(tous, commun, lu)
    return lu < p[None, :]


def voisins_factices(temoins) -> dict:
    """Fragment « voisins » de chaque témoin : fautif (« VF ») pour un mauvais de l'item voisin_nomme ; conforme citant
    (« VC ») pour un citant sur deux ; conforme non citant (« VN ») sinon."""
    sortie = {}
    for i, t in enumerate(temoins):
        if t["classe"] == "mauvais" and t["item"] == "voisin_nomme":
            sortie[t["identifiant_interne"]] = "VF"
        elif t["citation"] and (i // 4) % 2 == 0:
            sortie[t["identifiant_interne"]] = "VC"
        elif t["classe"] == "bon" and not t["citation"] and i % 3 == 0:          # v3 : piège « reprise assumée »
            sortie[t["identifiant_interne"]] = "VP"
        else:
            sortie[t["identifiant_interne"]] = "VN"
    return sortie


NATURE_FACTICE = {"VN": "conforme_non_citant", "VC": "conforme_citant", "VF": "fautif",
                  "VP": "conforme_piege_reprise_assumee"}


def ecrire_construction(racine, temoins, voisins, fragments_sha=None):
    """Fichier de fragments et journal de construction factices, au format du générateur v3 (`valider_fragments`,
    `geste_composer`) ; seules comptent ici les catégories et les citations des fragments « voisins »."""
    champs_v = {"plus_proche_voisin": "voisin factice", "ce_qui_distingue": "différence factice"}
    fr = {"schema": ET.SCHEMA_FRAGMENTS, "version": "factice",
          "conformes": {"modules": [{"id": "M", "champs": {"module_change": "m"}, "citation": False, "piege": None}],
                        "mecanismes": [], "epreuves": [], "limites": [],
                        "voisins": [{"id": "VN", "champs": champs_v, "citation": False, "piege": None},
                                    {"id": "VC", "champs": champs_v, "citation": True, "piege": None},
                                    {"id": "VP", "champs": champs_v, "citation": False, "piege": "reprise_assumee"}]},
          "fautifs": [{"id": "VF", "item": "voisin_nomme", "niveau": "net", "categorie": "voisins", "champs": champs_v,
                       "citation": False},
                      {"id": "MF", "item": "module_nomme", "niveau": "net", "categorie": "modules",
                       "champs": {"module_change": "x"}, "citation": False}]}
    fragments = racine / "fragments.json"
    h_fr = ET.ecrire_scelle(fragments, fr)
    journal = racine / "journal-construction.json"
    h_j = ET.ecrire_scelle(journal, {
        "version": "factice", "fragments_sha256": fragments_sha or h_fr,
        "temoins": [{k: t[k] for k in ("identifiant_interne", "classe", "item", "niveau", "citation", "moitie")}
                    | {"fragments": {"modules": "M", "voisins": voisins[t["identifiant_interne"]]}} for t in temoins]})
    return {"journal": journal, "journal_sha": h_j, "fragments": fragments, "fragments_sha": h_fr}


def texte_reponse(verdict_items, nonce):
    return "Verdict.\n```json\n" + json.dumps({"items": verdict_items, "note": nonce}, ensure_ascii=False) + "\n```\n"


def plan_factice(temoins, tire=True):
    """Ordre du code d'appel v4 (`plan_des_envois`) : bloc A par témoin, juge Opus puis juge Argon ; bloc B moitié
    « lecture » d'abord. L'ordre des témoins est tiré à graine dans chaque bloc (racine des essais), ou trié (`tire`
    faux : artefact d'une coupure qui ne garde qu'une classe)."""
    moitie = {t["identifiant_interne"]: t["moitie"] for t in temoins}
    ids = sorted(moitie)
    if tire:
        g = rng("banque")
        ids_a = [ids[int(i)] for i in g.permutation(len(ids))]
        ids = [ids[int(i)] for i in g.permutation(len(ids))]
    else:
        ids_a = ids
    plan = []
    for rang, t in enumerate(ids_a, 1):
        for j in ET.JUGES:
            plan.append({"bloc": "A", "rang": rang, "temoin": t, "juge": j, "rendu": 1, "moitie": moitie[t]})
    ordre_b = [t for t in ids if moitie[t] == "lecture"] + [t for t in ids if moitie[t] == "etalonnage"]
    for rang, t in enumerate(ordre_b, 1):
        plan.append({"bloc": "B", "rang": rang, "temoin": t, "juge": "juge-opus", "rendu": 2, "moitie": moitie[t]})
        plan.append({"bloc": "B", "rang": rang, "temoin": t, "juge": "juge-argon", "rendu": 2, "moitie": moitie[t]})
        plan.append({"bloc": "B", "rang": rang, "temoin": t, "juge": "juge-argon", "rendu": 3, "moitie": moitie[t]})
    for e in plan:
        e["id"] = f"{e['temoin']}|{e['juge']}|r{e['rendu']}"
    return plan


def fabriquer(tmp, n=200, p_o=0.20, p_a=0.20, rho=0.30, rho_prime=0.70, sous=0, coupe_b=None, absents=None,
              illisibles=None, cache=None, erreurs=None, dossier="monde", tire=True, plante=None,
              banque_fragments_sha="juste"):
    """Monde factice entier : banque scellée, dépôt du code d'appel v4 (vraies fonctions), étalonnage, audit scellé.
    `coupe_b` : nombre de rendus du bloc B servis avant l'arrêt au plafond (None : plan entier) ; `absents`,
    `illisibles` : ensembles d'identifiants de rendus refusés deux fois, ou rendus illisibles ; `cache` : juge dont les
    rendus d'un témoin sont identiques à l'octet."""
    CA = code_appel()
    racine = Path(tmp) / dossier
    racine.mkdir()
    temoins = banque_factice(n)
    banque = racine / "banque.json"
    voisins = voisins_factices(temoins)
    construction = ecrire_construction(racine, temoins, voisins)
    tete = {"version": "factice", "items": list(ET.ITEMS), "temoins": temoins}
    if banque_fragments_sha == "juste":                    # v3 (b) : la banque porte l'empreinte de ses fragments
        tete["fragments_sha256"] = construction["fragments_sha"]
    elif banque_fragments_sha is not None:
        tete["fragments_sha256"] = banque_fragments_sha
    banque_sha = ET.ecrire_scelle(banque, tete)
    if erreurs is None:
        erreurs = erreurs_scriptees(rng("juges", sous), n, p_o, p_a, rho, rho_prime)
    ids = [t["identifiant_interne"] for t in temoins]
    index = {t: i for i, t in enumerate(ids)}
    vrai = {t["identifiant_interne"]: t for t in temoins}
    colonne = {(j, r): c for c, (j, r, _b) in enumerate(ET.COLONNES)}
    depot = racine / "sortie" / "epreuve"
    (depot / "reponses-brutes").mkdir(parents=True)
    journal = CA.Journal(depot / "journal-compteur.jsonl", creer=True)
    compteur = CA.Compteur(journal)
    journal.ajouter({"type": "ouverture", "execution": 1, "version": CA.VERSION, "plafond_c": CA.PLAFOND_C,
                     "session_c": CA.SESSION_C, "banque_sha256": banque_sha, "plomberie": []})
    plan = plan_factice(temoins, tire)
    # Coûts factices : le dixième du tarif des cartes de la v9 par juge (code d'appel, `TARIF_DES_CARTES`) ; le rapport
    # des coûts garde k = 3 pour le juge Argon, et 2 000 témoins tiennent sous le plafond du compteur.
    couts = {j: CA.TARIF_DES_CARTES[j] / 10 for j in ET.JUGES}
    arret = None
    servis_b = 0
    for e in plan:
        if e["bloc"] == "B":
            if coupe_b is not None and servis_b >= coupe_b:
                arret = journal.ajouter({"type": "arret", "motif": "plafond : cumul compté plus 0,60 USD dépasse le plafond",
                                         "dernier_envoi_parti": None, "cumul_compte": str(compteur.cumul())})
                break
            servis_b += 1
        t = e["temoin"]
        i = index[t]
        c = colonne[(e["juge"], e["rendu"])]
        cr = c if not (cache and e["juge"] == cache) else colonne[(e["juge"], 1)]
        bon = vrai[t]["classe"] == "bon"
        notable = bool(bon != erreurs[i, cr])
        items = {k: True for k in ET.ITEMS}
        if not notable:
            items[vrai[t]["item"] or ET.ITEMS[0]] = False
        if plante is not None and plante(vrai[t], voisins[t], e):         # v2 : plant sur reserves_tenues
            items[ET.ITEM_RESERVES] = False
            notable = False
        nonce = f"{t}-{e['juge']}" if (cache and e["juge"] == cache) else e["id"]
        texte = texte_reponse(items, nonce)
        if illisibles and e["id"] in illisibles:
            texte = "réponse sans bloc JSON"
        essais = 2 if (absents and e["id"] in absents) else 1
        cout = couts[e["juge"]]
        for essai in range(1, essais + 1):
            refuse = absents is not None and e["id"] in absents
            n_env = compteur.engager({"rendu": e["id"], "bloc": e["bloc"], "rang": e["rang"], "temoin": t,
                                      "juge": e["juge"], "essai": essai, "opaque": f"F{len(compteur.engagements):05x}",
                                      "entree_sha256": "0" * 64})
            brut = {"statut": "erreur" if refuse else "ok", "texte_brut": None if refuse else texte, "texte_final": None,
                    "cout_declare_usd": repr(float(cout)), "cout_inconnu": False, "modele_servi": "modele-factice",
                    "exception": None, "erreur": None}
            rep = f"reponses-brutes/envoi-{n_env:05d}.json"
            h = CA.ecrire_exclusif(depot / rep, CA.json_octets(brut))
            if refuse:
                compteur.regler(n_env, CA.SESSION, {"rendu": e["id"], "essai": essai, "succes": False, "statut": "erreur",
                                                    "nature": "refuse_ou_erreur", "cout_releve": None, "lisible": False,
                                                    "modele_servi": None, "modele_change": False, "reponse": rep,
                                                    "reponse_sha256": h})
            else:
                compteur.regler(n_env, cout, {"rendu": e["id"], "essai": essai, "succes": True, "statut": "ok",
                                              "nature": "cout_releve", "cout_releve": str(cout),
                                              "lisible": CA.__lire_verdict__(texte, ET.ITEMS) is not None,
                                              "modele_servi": "modele-factice", "modele_change": False, "reponse": rep,
                                              "reponse_sha256": h})
    if arret is None:
        journal.ajouter({"type": "fin", "cumul_compte": str(compteur.cumul()), "dernier_envoi_parti": None})
    journal.fermer()
    service = types.SimpleNamespace(fonctions={"lire_verdict": CA.__lire_verdict__}, items=ET.ITEMS, nature="essai")
    rapport = CA.deposer(depot, 1, plan, {}, service, journal.lignes, compteur, arret)
    rapport_sha = sha_compagnon(depot / "rapport-execution-1.json")
    return {"racine": racine, "banque": banque, "banque_sha": banque_sha, "depot": depot, "rapport": rapport,
            "rapport_sha": rapport_sha, "erreurs": erreurs, "temoins": temoins, "n": n, "voisins": voisins,
            **construction}


def executer_etalonnage(m, f, f_sha, d, **kw):
    a = dict(journal=m["journal"], journal_sha=m["journal_sha"], fragments=m["fragments"], fragments_sha=m["fragments_sha"])
    a.update(kw)
    return ET.executer(m["banque"], m["banque_sha"], f, f_sha, a["journal"], a["journal_sha"], a["fragments"],
                       a["fragments_sha"], d, n_temoins=m["n"])


def etalonner(m, dossier=None):
    d = m["racine"] / "lecture-ligne-3" if dossier is None else dossier
    f = m["depot"] / "verdicts-moitie-etalonnage-execution-1.json"
    res = executer_etalonnage(m, f, sha_compagnon(f), d)
    m["dossier"] = d
    m["etalonnage"] = Path(res["sortie"]) / ET.FICHIER_PIECE
    m["etalonnage_sha"] = res["piece_sha256"]
    return res


def ecrire_audit(m, controles=None, etalonnage_sha=None, nom="audit-symetrie.json"):
    c = {k: "tenu" for k in LI.CONTROLES_AUDIT} if controles is None else controles
    chemin = m["racine"] / nom
    h = ET.ecrire_scelle(chemin, {"piece": LI.PIECE_AUDIT, "etalonnage_sha256": etalonnage_sha or m["etalonnage_sha"],
                                  "banque_sha256": m["banque_sha"], "rapport_execution_sha256": m["rapport_sha"],
                                  "controles": c, "auteur": "essai (audit factice)"})
    m["audit"], m["audit_sha"] = chemin, h
    return chemin, h


def lire(m, **kw):
    args = dict(banque=m["banque"], banque_sha=m["banque_sha"], depot=m["depot"], execution=1,
                rapport_sha=m["rapport_sha"], etalonnage=m["etalonnage"], etalonnage_sha=m["etalonnage_sha"],
                audit=m["audit"], audit_sha=m["audit_sha"], mode="essais", n_temoins=m["n"])
    args.update(kw)
    return LI.lire(**args)


def monde_complet(tmp, **kw):
    m = fabriquer(tmp, **kw)
    etalonner(m)
    ecrire_audit(m)
    return m


# --- 1. Cas sain de bout en bout, et format du code d'appel ------------------------------------------------------------------


def test_cas_sain_bout_en_bout(tmp_path):
    m = monde_complet(tmp_path)
    assert m["rapport"]["envois_partis"] == 1000 and m["rapport"]["complets"]["bloc_B_moitie_lecture"] == 100
    res = lire(m)
    r = res["rapport"]
    sortie = Path(res["sortie"])
    for f in (LI.FICHIER_RAPPORT, LI.FICHIER_MANIFESTE):
        assert sha_compagnon(sortie / f) == hashlib.sha256((sortie / f).read_bytes()).hexdigest()
    assert r["temoins"]["complets_moitie_lecture"] == 100 and r["temoins"]["complets_cinq_rendus"] == 200
    assert r["table_de_lecture"]["oui_possible"] is False and r["table_de_lecture"]["rang"] in (None, 3, 5)
    assert r["regles_choisies_a_l_etalonnage"]["C"] in ("unanimite", "au_moins_un", "juge_1_seul", "juge_2_seul",
                                                         "constante")
    man = res["manifeste"]
    assert man["graines"]["racine"] == RACINE_ESSAIS and [d["cle"] for d in man["graines"]["derivations"]] == [1, 2, 3, 4, 5]
    assert man["etalonner_sha256"] == LI.ETALONNER[1] and man["banc_v4_sha256"] == ET.BANC_V4[1]


def test_etalonnage_cas_sain_egal_au_banc_sur_les_tableaux_du_monde(tmp_path):
    """Les poids, seuils, règles et ρ d'étalonnage sont ceux des fonctions du banc v4, recalculés ici depuis les erreurs
    plantées elles-mêmes (sans passer par le dépôt)."""
    m = fabriquer(tmp_path)
    res = etalonner(m)
    p = res["piece"]
    assert sha_compagnon(m["etalonnage"]) == res["piece_sha256"]
    assert sha_compagnon(m["etalonnage"].parent / ET.FICHIER_MANIFESTE)
    cal = [i for i, t in enumerate(m["temoins"]) if t["moitie"] == "etalonnage"]
    ordre = sorted(cal, key=lambda i: m["temoins"][i]["identifiant_interne"])
    y = np.array([m["temoins"][i]["classe"] == "bon" for i in ordre])
    E = m["erreurs"][ordre][:, :2]
    V = (E != y[:, None])[None]
    Vpm = 2.0 * V - 1.0
    w, _ = BANC.poids_covariance(Vpm, y)
    s = BANC.seuil_milieu(BANC.score(Vpm, w), y)
    assert p["bras_C"]["poids"] == [float(x) for x in w[0]] and p["bras_C"]["seuil"] == float(s[0])
    assert p["bras_C"]["regle_choisie"] == BANC.regle_choisie(w[0], s[0])
    wp = BANC.poids_precision(V, y, E[None])
    sp = BANC.seuil_milieu(BANC.score(Vpm, wp), y)
    assert p["bras_P"]["poids"] == [float(x) for x in wp[0]] and p["bras_P"]["seuil"] == float(sp[0])
    rho, _ = BANC.rho_moyenne(BANC.cov_intra_classes(E[None].astype(float), y))
    assert p["rho_etalonnage"] == float(rho[0]) and p["temoins_lus"] == 100


# --- 2. Estimations proches des valeurs plantées à grand n -------------------------------------------------------------------


def test_grand_n_estimations_proches_des_valeurs_plantees(tmp_path):
    p, rho, rho_prime = 0.20, 0.30, 0.70
    m = monde_complet(tmp_path, n=2000, p_o=p, p_a=p, rho=rho, rho_prime=rho_prime, sous=1)
    r = lire(m)["rapport"]
    assert abs(r["rho_entre_juges_bloc_A"]["valeur"] - rho) < 0.07
    assert abs(r["rho_entre_juges_bloc_A"]["votes_effectifs_bruts"] - 2 / (1 + rho)) < 0.08
    for j in ET.JUGES:
        x = r["rho_prime_et_ecarts"][j]
        assert abs(x["rho_prime"] - rho_prime) < 0.07
        assert abs(x["rho_prime_moins_rho"] - (rho_prime - rho)) < 0.08
        assert x["mot"] == "positif"
        assert abs(r["juges"][j]["taux_erreur_bloc_A"]["taux"] - p) < 0.03
    p11 = p * p + rho * p * (1 - p)
    b = r["bras_moitie_lecture_bloc_A"]["bras"]
    assert abs(b["U"]["faux_acceptes"] - p11) < 0.04 and abs(b["U"]["vrais_rejetes"] - (2 * p - p11)) < 0.05
    assert abs(b["F"]["faux_acceptes"] - (2 * p - p11)) < 0.05 and abs(b["F"]["vrais_rejetes"] - p11) < 0.04
    for k in ("S_Opus", "S_Argon", "U", "F"):
        assert abs(b[k]["erreur_equilibree"] - p) < 0.04          # § 0 : même erreur équilibrée à deux juges égaux
    maj = rho_prime * p + (1 - rho_prime) * (3 * p * p - 2 * p ** 3)
    assert abs(r["bras_moitie_lecture_complets"]["bras"]["R_Argon"]["erreur_equilibree"] - maj) < 0.04
    r2 = rho_prime * p + (1 - rho_prime) * p * p                   # unanimité de deux rendus : faux acceptés
    assert abs(r["bras_moitie_lecture_complets"]["bras"]["R_Opus_2"]["faux_acceptes"] - r2) < 0.04
    assert r["table_de_lecture"]["mot"] == LI.MOTS_TABLE["mesure_decorrele"] and r["table_de_lecture"]["rang"] is None
    assert r["cout_apparie"]["k_apparie"] == 3


def test_rang_3_un_juge_repete_vaut_le_college(tmp_path):
    """Artefact contraire : ρ′ = ρ planté ; à grand n, ρ′ − ρ « nul ou négatif » : rang 3 (le seul « non » atteignable)."""
    m = monde_complet(tmp_path, n=1200, rho=0.4, rho_prime=0.4, sous=2)
    r = lire(m)["rapport"]
    assert "nul ou négatif" in r["table_de_lecture"]["mots_rho_prime_moins_rho"].values()
    assert r["table_de_lecture"]["rang"] == 3 and r["table_de_lecture"]["mot"] == LI.MOTS_TABLE["rang_3"]


# --- 3. Gardes de la liste d'arrêt : étalonnage --------------------------------------------------------------------------------


def test_etalonnage_qui_lit_la_moitie_lecture_refus_par_le_nom(tmp_path):
    m = fabriquer(tmp_path)
    f = m["depot"] / "verdicts-moitie-lecture-execution-1.json"
    with pytest.raises(ET.Refus, match="moitié « lecture » passé à l'étalonnage"):
        executer_etalonnage(m, f, sha_compagnon(f), m["racine"] / "d")
    assert not (m["racine"] / "d").exists()


def test_etalonnage_qui_lit_la_moitie_lecture_refus_par_le_contenu(tmp_path):
    """Les verdicts de la moitié « lecture » recopiés sous le nom de l'étalonnage : refus nommé avant tout usage."""
    m = fabriquer(tmp_path)
    src = m["depot"] / "verdicts-moitie-lecture-execution-1.json"
    faux = m["racine"] / "faux"
    faux.mkdir()
    dst = faux / "verdicts-moitie-etalonnage-execution-1.json"
    dst.write_bytes(src.read_bytes())
    Path(str(dst) + ".sha256").write_text(f"{sha_compagnon(src)}  {dst.name}\n", encoding="utf-8")
    with pytest.raises(ET.Refus, match="témoin de la moitié « lecture » dans les verdicts de la moitié « etalonnage »"):
        executer_etalonnage(m, dst, sha_compagnon(dst), m["racine"] / "d")
    assert not (m["racine"] / "d").exists()


def test_etalonnage_une_ligne_de_la_moitie_lecture_melee(tmp_path):
    m = fabriquer(tmp_path)
    src = m["depot"] / "verdicts-moitie-etalonnage-execution-1.json"
    o = json.loads(src.read_text(encoding="utf-8"))
    lec = next(t["identifiant_interne"] for t in m["temoins"] if t["moitie"] == "lecture")
    o["rendus"][0]["temoin"] = lec
    faux = m["racine"] / "faux"
    faux.mkdir()
    dst = faux / src.name
    h = ET.ecrire_scelle(dst, o)
    with pytest.raises(ET.Refus, match="moitié « lecture »"):
        executer_etalonnage(m, dst, h, m["racine"] / "d")


def test_etalonnage_rejoue_dans_le_meme_dossier_refus(tmp_path):
    m = fabriquer(tmp_path)
    etalonner(m)
    with pytest.raises(ET.Refus, match="dossier de sortie déjà présent"):
        etalonner(m)


def test_etalonnage_verdicts_d_une_autre_empreinte_refus(tmp_path):
    m = fabriquer(tmp_path)
    f = m["depot"] / "verdicts-moitie-etalonnage-execution-1.json"
    with pytest.raises(ET.Refus, match="empreinte différente"):
        executer_etalonnage(m, f, "0" * 64, m["racine"] / "d")


# --- 4. Gardes : lecture unique, étalonnage scellé, audit scellé ---------------------------------------------------------------


def test_lecture_rejouee_refus(tmp_path):
    m = monde_complet(tmp_path)
    res = lire(m)
    avant = Path(res["sortie"], LI.FICHIER_RAPPORT).read_bytes()
    with pytest.raises(ET.Refus, match="lecture unique : le rapport de lecture existe déjà"):
        lire(m)
    assert Path(res["sortie"], LI.FICHIER_RAPPORT).read_bytes() == avant


def test_lecture_dossier_present_sans_rapport_refus(tmp_path):
    m = monde_complet(tmp_path)
    (m["dossier"] / LI.SOUS_DOSSIER).mkdir()
    with pytest.raises(ET.Refus, match="dossier de lecture déjà présent sans rapport"):
        lire(m)


def test_lecture_sans_audit_de_symetrie_refus(tmp_path):
    m = monde_complet(tmp_path)
    with pytest.raises(ET.Refus, match="audit de symétrie avant lecture : absent"):
        lire(m, audit=m["racine"] / "audit-absent.json")
    assert not (m["dossier"] / LI.SOUS_DOSSIER).exists()


def test_lecture_audit_non_scelle_ou_d_une_autre_empreinte_refus(tmp_path):
    m = monde_complet(tmp_path)
    Path(str(m["audit"]) + ".sha256").unlink()
    with pytest.raises(ET.Refus, match="audit de symétrie avant lecture"):
        lire(m)
    ecrire_audit(m, nom="audit-2.json")
    with pytest.raises(ET.Refus, match="audit de symétrie avant lecture"):
        lire(m, audit_sha="0" * 64)
    assert not (m["dossier"] / LI.SOUS_DOSSIER).exists()


def test_lecture_audit_ecrit_avant_l_etalonnage_refus(tmp_path):
    """Un audit qui ne cite pas l'empreinte de la pièce d'étalonnage scellée (écrit avant elle, ou pour une autre) : refus."""
    m = monde_complet(tmp_path)
    ecrire_audit(m, etalonnage_sha="1" * 64, nom="audit-autre.json")
    with pytest.raises(ET.Refus, match="ne cite pas l'empreinte de la pièce d'étalonnage"):
        lire(m)


def test_lecture_audit_avec_un_controle_non_tenu_refus(tmp_path):
    m = monde_complet(tmp_path)
    c = {k: "tenu" for k in LI.CONTROLES_AUDIT}
    c["verite_non_servie"] = "non tenu"
    ecrire_audit(m, controles=c, nom="audit-non-tenu.json")
    with pytest.raises(ET.Refus, match="contrôle non tenu \\(verite_non_servie\\)"):
        lire(m)
    del c["verite_non_servie"]
    ecrire_audit(m, controles=c, nom="audit-incomplet.json")
    with pytest.raises(ET.Refus, match="cinq contrôles"):
        lire(m)


def test_lecture_sans_etalonnage_scelle_refus(tmp_path):
    m = monde_complet(tmp_path)
    with pytest.raises(ET.Refus, match="étalonnage avant lecture"):
        lire(m, etalonnage_sha="0" * 64)
    Path(str(m["etalonnage"]) + ".sha256").unlink()
    with pytest.raises(ET.Refus, match="étalonnage avant lecture"):
        lire(m)
    assert not (m["dossier"] / LI.SOUS_DOSSIER).exists()


def test_lecture_etalonnage_absent_refus(tmp_path):
    m = fabriquer(tmp_path)
    m["etalonnage"] = m["racine"] / "x" / ET.SOUS_DOSSIER / ET.FICHIER_PIECE
    m["etalonnage_sha"] = "2" * 64
    ecrire_audit(m)
    with pytest.raises(ET.Refus, match="étalonnage avant lecture : pièce absente"):
        lire(m)


def test_lecture_etalonnage_recalcule_different_refus(tmp_path):
    """Une pièce d'étalonnage aux poids changés, rescellée et citée par l'audit : le recalcul diffère, refus."""
    m = monde_complet(tmp_path)
    p = json.loads(m["etalonnage"].read_text(encoding="utf-8"))
    p["bras_C"]["poids"] = [1.0, 2.0]
    d = m["racine"] / "autre" / ET.SOUS_DOSSIER
    d.mkdir(parents=True)
    p["dossier"] = str((m["racine"] / "autre").resolve())          # v2 : le dossier juste, pour atteindre le recalcul
    h = ET.ecrire_scelle(d / ET.FICHIER_PIECE, p)
    ET.ecrire_scelle(d / ET.FICHIER_MANIFESTE, {"factice": True})
    m["etalonnage"], m["etalonnage_sha"] = d / ET.FICHIER_PIECE, h
    ecrire_audit(m, nom="audit-autre-etalonnage.json")
    with pytest.raises(ET.Refus, match="bras_C recalculé différent"):
        lire(m)


def test_lecture_execution_plus_recente_refus(tmp_path):
    m = monde_complet(tmp_path)
    (m["depot"] / "rapport-execution-2.json").write_text("{}", encoding="utf-8")
    with pytest.raises(ET.Refus, match="exécution plus récente"):
        lire(m)


# --- 5. Graines : racine 2026111936 seulement sous autorisation -------------------------------------------------------------


def test_racine_de_la_lecture_sans_autorisation_refus(tmp_path):
    with pytest.raises(ET.Refus, match="refus sans autorisation"):
        LI.Graines("reel", None)
    a = tmp_path / "additif.md"
    a.write_text("additif factice\n", encoding="utf-8")
    with pytest.raises(ET.Refus, match="différente de l'attendue"):
        LI.Graines("reel", (a, "0" * 64))
    with pytest.raises(ET.Refus, match="mal formée"):
        LI.Graines("reel", (a, "xyz"))
    with pytest.raises(ET.Refus, match="additif absent"):
        LI.Graines("reel", (tmp_path / "absent.md", "0" * 64))
    with pytest.raises(ET.Refus, match="mode inconnu"):
        LI.Graines("decisif", None)


def test_racine_de_la_lecture_autorisee_sans_derivation(tmp_path):
    """Cas sain : autorisation juste ; la racine retenue est 2026111936 ; aucune graine n'est dérivée par l'essai."""
    a = tmp_path / "additif.md"
    a.write_text("additif factice\n", encoding="utf-8")
    g = LI.Graines("reel", (a, hashlib.sha256(a.read_bytes()).hexdigest()))
    assert g.racine == 2026111936 and g.derivations == []
    assert LI.Graines("essais").racine == RACINE_ESSAIS
    assert 2026111936 not in LI.RACINES_TOUJOURS_REFUSEES and LI.RACINE_LECTURE == 2026111936


def test_lecture_reelle_refusee_avant_toute_lecture(tmp_path):
    """En mode réel sans autorisation, le refus vient avant toute lecture : même une banque absente n'est pas touchée."""
    with pytest.raises(ET.Refus, match="refus sans autorisation"):
        LI.lire(tmp_path / "absente.json", "0" * 64, tmp_path, 1, "0" * 64, tmp_path / "e" / ET.SOUS_DOSSIER /
                ET.FICHIER_PIECE, "0" * 64, tmp_path / "a.json", "0" * 64, mode="reel", autorisation=None)
    assert LI.principal(["--banque", "x"]) == 2


# --- 6. Plafond : coupure au pire cas, et manque de témoins ------------------------------------------------------------------


def test_coupure_au_pire_cas_du_calcul_plafond_v2_lu(tmp_path):
    """197 témoins complets au bloc B, dont 100 de la moitié « lecture », un témoin partiel (rang 198), arrêt au plafond :
    la lecture se fait (pas de « manque de témoins »), ρ′ sur les 197 complets."""
    m = monde_complet(tmp_path, coupe_b=197 * 3 + 1, sous=3)
    rc = m["rapport"]["complets"]
    assert rc["bloc_B"] == 197 and rc["bloc_B_moitie_lecture"] == 100 and rc["rangs_des_temoins_partiels_au_bloc_B"] == [198]
    r = lire(m)["rapport"]
    assert r["temoins"]["complets_moitie_lecture"] == 100 and r["temoins"]["complets_cinq_rendus"] == 197
    assert isinstance(r["rho_prime_et_ecarts"], dict) and r["rho_prime_et_ecarts"]["temoins_complets"] == 197
    assert r["table_de_lecture"]["mot"] != LI.MOTS_TABLE["rang_1_manque"]
    assert not any("moins de 40" in c for c in r["table_de_lecture"]["causes_du_rang_1"])
    assert r["arret_du_code_d_appel"]["motif"].startswith("plafond")


def test_moins_de_40_complets_non_concluant_par_manque_de_temoins(tmp_path):
    m = monde_complet(tmp_path, coupe_b=39 * 3, sous=4)
    r = lire(m)["rapport"]
    assert r["temoins"]["complets_moitie_lecture"] == 39
    t = r["table_de_lecture"]
    assert t["rang"] == 1 and t["mot"] == "non concluant par manque de témoins"
    assert any("moins de 40" in c and "plafond" in c for c in t["causes_du_rang_1"])
    assert isinstance(r["rho_prime_et_ecarts"], str) and "non mesurés" in r["rho_prime_et_ecarts"]
    assert isinstance(r["bras_moitie_lecture_complets"], str) and t["mots_rho_prime_moins_rho"] == "non mesurés"
    assert not t["mot"].startswith("non :")
    assert r["rho_entre_juges_bloc_A"]["valeur"] is not None and r["bras_moitie_lecture_bloc_A"]["temoins"] == 100


def test_exactement_40_complets_lu(tmp_path):
    m = monde_complet(tmp_path, coupe_b=40 * 3, sous=5)
    r = lire(m)["rapport"]
    assert r["temoins"]["complets_moitie_lecture"] == 40
    assert not any("moins de 40" in c for c in r["table_de_lecture"]["causes_du_rang_1"])
    assert isinstance(r["rho_prime_et_ecarts"], dict) and r["temoins"]["classes_suffisantes"]["complets"] is True


def test_coupure_qui_ne_garde_qu_une_classe_non_mesure_sans_arret_brut(tmp_path):
    """Artefact : ordre trié, 40 témoins complets de la moitié « lecture », tous bons : ρ′ et bras R « non mesurés »,
    nommés ; mots « indéterminé » ; le reste est non concluant (rang 5) ; aucune exception."""
    m = monde_complet(tmp_path, coupe_b=40 * 3, sous=5, tire=False)
    r = lire(m)["rapport"]
    assert r["temoins"]["complets_moitie_lecture"] == 40 and r["temoins"]["classes_suffisantes"]["complets"] is False
    assert "moins de deux témoins complets d'une classe" in r["rho_prime_et_ecarts"]
    assert "moins de deux témoins complets d'une classe" in r["bras_moitie_lecture_complets"]
    assert r["table_de_lecture"]["rang"] == 5 and r["table_de_lecture"]["mot"] == "non concluant"


# --- 7. Juges non mesurés, banc sans prise, audit « trop propre » --------------------------------------------------------------


def test_juge_non_mesure_par_les_absents(tmp_path):
    """Plus de 10 % d'absents chez le juge Argon (refus deux fois, et réponses illisibles) : rang 1 ; cas sain : 0 absent."""
    plan = plan_factice(banque_factice(200))
    argon = [e["id"] for e in plan if e["juge"] == "juge-argon"]
    absents = set(argon[0:40:2])
    illisibles = set(argon[1:80:2])
    m = monde_complet(tmp_path, absents=absents, illisibles=illisibles, sous=6)
    r = lire(m)["rapport"]
    a = r["juges"]["juge-argon"]["absents_A_et_B"]
    assert a["compte"] == 60 and a["sur"] == 600 and r["juges"]["juge-argon"]["non_mesure_absents"] is False
    m2 = monde_complet(tmp_path, absents=absents, illisibles=set(argon[1:200:2]), sous=6, dossier="monde-2")
    r2 = lire(m2)["rapport"]
    a2 = r2["juges"]["juge-argon"]["absents_A_et_B"]
    assert a2["compte"] == 120 and r2["juges"]["juge-argon"]["non_mesure_absents"] is True
    assert r2["table_de_lecture"]["rang"] == 1
    assert any("plus de 10 % de verdicts absents" in c for c in r2["table_de_lecture"]["causes_du_rang_1"])
    assert r["juges"]["juge-opus"]["absents_A_et_B"]["compte"] == 0


def test_juge_non_mesure_par_les_repetitions_identiques(tmp_path):
    m = monde_complet(tmp_path, cache="juge-argon", sous=7)
    r = lire(m)["rapport"]
    assert r["juges"]["juge-argon"]["part_identique_a_l_octet"] == "1"
    assert r["juges"]["juge-opus"]["part_identique_a_l_octet"] == "0"
    assert r["rho_prime_et_ecarts"]["juge-argon"]["mot"].startswith("non mesuré")
    assert r["table_de_lecture"]["rang"] == 1
    assert any("répétitions identiques" in c for c in r["table_de_lecture"]["causes_du_rang_1"])


def test_banc_sans_prise_juge_presque_parfait(tmp_path):
    m = monde_complet(tmp_path, p_a=0.01, sous=8)
    r = lire(m)["rapport"]
    assert r["juges"]["juge-argon"]["taux_erreur_bloc_A"]["taux"] < 0.05
    assert any("banc sans prise : juge-argon" in c for c in r["table_de_lecture"]["causes_du_rang_1"])
    assert r["table_de_lecture"]["rang"] == 1 and r["table_de_lecture"]["mot"] == "non concluant"


def test_trop_propre_juge_sans_erreur_et_rho_indefini(tmp_path):
    """Juge Argon sans aucune erreur : ρ « indéfini » (jamais 0), intervalle indéfini, banc sans prise, « trop propre »."""
    g = rng("juges", 9)
    e = erreurs_scriptees(g, 200, 0.2, 0.2, 0.3, 0.7)
    e[:, [1, 3, 4]] = False
    m = monde_complet(tmp_path, erreurs=e)
    r = lire(m)["rapport"]
    assert r["rho_entre_juges_bloc_A"]["indefini"] is True and r["rho_entre_juges_bloc_A"]["valeur"] is None
    assert any("aucune erreur" in x for x in r["audit_de_symetrie"]["trop_propre"])
    assert r["audit_de_symetrie"]["sous_reserve"] is True and r["table_de_lecture"]["rang"] == 1


def test_trop_propre_juge_duplique_un_vote_effectif(tmp_path):
    g = rng("juges", 10)
    e = erreurs_scriptees(g, 200, 0.2, 0.2, 0.3, 0.7)
    e[:, 1] = e[:, 0]
    m = monde_complet(tmp_path, erreurs=e)
    r = lire(m)["rapport"]
    assert abs(r["rho_entre_juges_bloc_A"]["valeur"] - 1.0) < 1e-9
    assert abs(r["rho_entre_juges_bloc_A"]["votes_effectifs_bruts"] - 1.0) < 1e-9
    assert any("ρ entre juges à moins de 0,02" in x for x in r["audit_de_symetrie"]["trop_propre"])


def test_trop_sale_juge_au_hasard(tmp_path):
    m = monde_complet(tmp_path, p_a=0.5, sous=11)
    r = lire(m)["rapport"]
    assert any("erreur équilibrée au-dessus de 0,40" in x for x in r["audit_de_symetrie"]["trop_sale"])
    assert r["table_de_lecture"]["rang"] == 1


# --- 8. Issue B : aucun « oui » ------------------------------------------------------------------------------------------


def test_issue_b_aucun_oui_meme_quand_tout_irait_vers_le_rang_2(tmp_path):
    """Juges sévères (vrais rejetés 0,40, faux acceptés 0,05 ; « au moins un » doit l'emporter) et ρ′ − ρ planté fort :
    à grand n, rien ne rend « oui » ; les comparaisons sont descriptives ; le mot est la mesure « décorrèle »."""
    n = 1600
    g = rng("juges", 12)
    temoins = banque_factice(n)
    y = np.array([t["classe"] == "bon" for t in temoins])
    e_bon = erreurs_scriptees(g, n, 0.40, 0.40, 0.1, 0.8)
    e_mau = erreurs_scriptees(g, n, 0.05, 0.05, 0.1, 0.8)
    e = np.where(y[:, None], e_bon, e_mau)
    m = monde_complet(tmp_path, n=n, erreurs=e)
    r = lire(m)["rapport"]
    t = r["table_de_lecture"]
    assert t["oui_possible"] is False and t["rangs_atteignables"] == [1, 3] and t["rang"] not in (2, 4)
    assert not t["mot"].lower().startswith("oui") and t["mot"] == LI.MOTS_TABLE["mesure_decorrele"]
    c = r["comparaisons_d_agregations"]
    assert "aucun « oui »" in c["statut"]
    assert all("aucun verdict" in v["mot"] or "descriptif" in v["mot"] for v in c["comparaisons"].values())
    assert t["mot"] in LI.MOTS_TABLE.values()
    assert not any(v.lower().startswith("oui") for v in LI.MOTS_TABLE.values())
    assert LI.OUI_POSSIBLE is False and LI.ISSUE_PORTEE == "B"


# --- 9. Verdicts de la v9 : chemins refusés avant toute ouverture -----------------------------------------------------------


def test_garde_des_chemins_de_la_v9():
    ET.garde_chemins(["/tmp/un-dossier-sain/banque.json"])
    for c in ("/tmp/x/coffre-course-v9/verdicts.json", "/home/user/sorties-course-auto-conception-v9/a.json",
              "/x/archives-reponses-modeles/y.json"):
        with pytest.raises(ET.Refus, match="verdicts de la v9"):
            ET.garde_chemins([c])


def test_lecture_refuse_un_depot_du_coffre_avant_toute_ouverture(tmp_path):
    m = monde_complet(tmp_path)
    with pytest.raises(ET.Refus, match="verdicts de la v9"):
        lire(m, depot=tmp_path / "coffre-v9" / "epreuve")


# --- 10. Imports à empreinte vérifiée --------------------------------------------------------------------------------------


def test_banc_importe_par_empreinte_et_refus_d_une_autre(tmp_path):
    assert BANC.__empreinte__ == ET.BANC_V4[1] == "79865552dd666ea697a817c520d6f50337a9634cd8efe8a7b26d08a280ab4de7"
    faux = tmp_path / "banc.py"
    faux.write_bytes(ET.BANC_V4[0].read_bytes() + b"\n# modifie\n")
    nom = ET.MODULE_BANC
    sauve = sys.modules.pop(nom)
    try:
        with pytest.raises(ET.Refus, match="empreinte différente"):
            ET.charger_banc(faux, ET.BANC_V4[1])
    finally:
        sys.modules[nom] = sauve


def test_lire_importe_etalonner_par_empreinte():
    assert LI.ETALONNER[0] == "etalonner_ligne_3_v3.py"
    assert hashlib.sha256((ICI / "etalonner_ligne_3_v3.py").read_bytes()).hexdigest() == LI.ETALONNER[1]
    assert LI.ET is ET


# --- 11. v2 : témoin complet = cinq rendus obtenus (essais du contre-lecteur, `essai_correction_n1_v1.py`, repris) ------


def test_v2_un_rendu_absent_n_est_pas_obtenu_donc_pas_complet(tmp_path):
    plan = plan_factice(banque_factice(200))
    lecture_b = [p for p in plan if p["bloc"] == "B" and p["moitie"] == "lecture"]
    cible = lecture_b[0]["id"]                                   # un rendu du bloc B, premier témoin de la moitié « lecture »
    m = monde_complet(tmp_path, coupe_b=40 * 3, sous=5, absents={cible})
    assert m["rapport"]["complets"]["bloc_B_moitie_lecture"] == 39       # le code d'appel : cinq rendus obtenus
    r = lire(m)["rapport"]
    assert r["temoins"]["complets_moitie_lecture"] == 39                 # la lecture suit le code d'appel
    assert r["temoins"]["complets_moitie_lecture_tentes"] == 40          # le compte des tentés reste rapporté
    t = r["table_de_lecture"]
    assert t["rang"] == 1 and t["mot"] == "non concluant par manque de témoins"
    assert any("moins de 40" in c for c in t["causes_du_rang_1"])


def test_v2_cas_sain_sans_absent_les_deux_comptes_sont_egaux(tmp_path):
    m = monde_complet(tmp_path, coupe_b=40 * 3, sous=5)
    r = lire(m)["rapport"]
    assert r["temoins"]["complets_moitie_lecture"] == r["temoins"]["complets_moitie_lecture_tentes"] == 40
    assert r["temoins"]["complets_cinq_rendus"] == r["temoins"]["complets_cinq_rendus_tentes"]


# --- 12. v2 : cartes tombées sur reserves_tenues, moitié « étalonnage » ------------------------------------------------------


def attendu_reserves(m, juge_plante, plante):
    """Recalcul indépendant, depuis le monde planté (juges parfaits) : une carte « tombe » si le plant la vise, ou si c'est
    un mauvais de l'item reserves_tenues (le juge parfait rend faux l'item planté)."""
    sortie = {}
    for j in ET.JUGES:
        strates = {}
        for t in m["temoins"]:
            if t["moitie"] != "etalonnage":
                continue
            v = NATURE_FACTICE[m["voisins"][t["identifiant_interne"]]]
            tombee = (t["classe"] == "mauvais" and t["item"] == ET.ITEM_RESERVES) or \
                (j == juge_plante and plante(t, m["voisins"][t["identifiant_interne"]], {"juge": j, "rendu": 1}))
            cle = (t["classe"], "citant" if t["citation"] else "non_citant", t["item"] or "aucun (bon)", v)
            c = strates.setdefault(cle, [0, 0])
            c[0] += int(tombee)
            c[1] += 1
        sortie[j] = strates
    return sortie


def plant_sur(nature):
    return lambda t, fid, e: e["juge"] == "juge-opus" and e["rendu"] == 1 and t["classe"] == "bon" and fid == nature


def test_v2_reserves_tenues_plant_sur_les_voisins_conformes_non_citants(tmp_path):
    """Cas sain : le juge Opus rejette sur reserves_tenues, au premier rendu, tous les bons dont le fragment « voisins » est
    conforme non citant ; les comptes de la pièce scellée égalent le recalcul, strate par strate, et les marges."""
    plante = plant_sur("VN")
    e = np.zeros((200, 5), dtype=bool)
    m = fabriquer(tmp_path, erreurs=e, plante=plante)
    res = etalonner(m)
    piece = json.loads(m["etalonnage"].read_text(encoding="utf-8"))
    assert sha_compagnon(m["etalonnage"]) == res["piece_sha256"] and ET.CLE_RESERVES in piece
    c = piece[ET.CLE_RESERVES]["par_juge"]
    att = attendu_reserves(m, "juge-opus", plante)
    for j in ET.JUGES:
        lu = {(s["classe"], s["citation"], s["item_plante"], s["voisins"]): [s["compte"], s["sur"]] for s in c[j]["strates"]}
        assert lu == att[j]
        assert c[j]["verdicts_absents_exclus"] == 0
    bons_vn = sum(1 for t in m["temoins"] if t["moitie"] == "etalonnage" and t["classe"] == "bon"
                  and m["voisins"][t["identifiant_interne"]] == "VN")
    mauvais_res_vn = sum(1 for t in m["temoins"] if t["moitie"] == "etalonnage" and t["item"] == ET.ITEM_RESERVES
                         and m["voisins"][t["identifiant_interne"]] == "VN")
    assert bons_vn > 0
    assert c["juge-opus"]["par_voisins"]["conforme_non_citant"]["compte"] == bons_vn + mauvais_res_vn
    assert c["juge-argon"]["par_voisins"]["conforme_non_citant"]["compte"] == mauvais_res_vn
    assert c["juge-opus"]["par_classe"]["bon"]["compte"] == bons_vn and c["juge-argon"]["par_classe"]["bon"]["compte"] == 0
    assert c["juge-opus"]["par_voisins"]["conforme_citant"]["compte"] == sum(
        1 for t in m["temoins"] if t["moitie"] == "etalonnage" and t["item"] == ET.ITEM_RESERVES
        and m["voisins"][t["identifiant_interne"]] == "VC")
    assert sum(x["sur"] for x in c["juge-opus"]["par_classe"].values()) == 100


def test_v2_reserves_tenues_plant_ailleurs_ne_tombe_pas_chez_les_non_citants(tmp_path):
    """Artefact : le même plant porté sur les bons au fragment « voisins » conforme **citant** : les cartes tombent dans
    cette strate, et la strate « conforme non citant » des bons reste à 0 ; les comptes égalent le recalcul."""
    plante = plant_sur("VC")
    e = np.zeros((200, 5), dtype=bool)
    m = fabriquer(tmp_path, erreurs=e, plante=plante)
    etalonner(m)
    c = json.loads(m["etalonnage"].read_text(encoding="utf-8"))[ET.CLE_RESERVES]["par_juge"]
    att = attendu_reserves(m, "juge-opus", plante)
    lu = {(s["classe"], s["citation"], s["item_plante"], s["voisins"]): [s["compte"], s["sur"]]
          for s in c["juge-opus"]["strates"]}
    assert lu == att["juge-opus"]
    bons_nc = [s for s in c["juge-opus"]["strates"] if s["classe"] == "bon" and s["voisins"] == "conforme_non_citant"]
    assert bons_nc and all(s["compte"] == 0 for s in bons_nc)
    assert any(s["compte"] > 0 for s in c["juge-opus"]["strates"] if s["classe"] == "bon" and s["voisins"] == "conforme_citant")


def test_v2_reserves_tenues_ne_lit_que_la_moitie_etalonnage(tmp_path):
    """Artefact : un plant porté sur la seule moitié « lecture » ne change aucun compte de la pièce d'étalonnage."""
    plante = lambda t, fid, e: e["rendu"] == 1 and t["moitie"] == "lecture" and t["classe"] == "bon"  # noqa: E731
    e = np.zeros((200, 5), dtype=bool)
    m = fabriquer(tmp_path, erreurs=e, plante=plante)
    etalonner(m)
    c = json.loads(m["etalonnage"].read_text(encoding="utf-8"))[ET.CLE_RESERVES]["par_juge"]
    for j in ET.JUGES:
        assert c[j]["par_classe"]["bon"]["compte"] == 0


def test_v2_journal_ou_fragments_hors_forme_refus(tmp_path):
    m = fabriquer(tmp_path)
    f = m["depot"] / "verdicts-moitie-etalonnage-execution-1.json"
    (m["racine"] / "x").mkdir()
    autre = ecrire_construction(m["racine"] / "x", m["temoins"], m["voisins"], fragments_sha="3" * 64)
    with pytest.raises(ET.Refus, match="fichier de fragments d'une autre empreinte"):
        executer_etalonnage(m, f, sha_compagnon(f), m["racine"] / "d1", journal=autre["journal"],
                            journal_sha=autre["journal_sha"], fragments=autre["fragments"],
                            fragments_sha=autre["fragments_sha"])
    inconnu = dict(m["voisins"])
    inconnu[next(iter(inconnu))] = "INCONNU"
    (m["racine"] / "y").mkdir()
    autre = ecrire_construction(m["racine"] / "y", m["temoins"], inconnu)
    with pytest.raises(ET.Refus, match="fragment « voisins » absent du fichier de fragments"):
        executer_etalonnage(m, f, sha_compagnon(f), m["racine"] / "d2", journal=autre["journal"],
                            journal_sha=autre["journal_sha"], fragments=autre["fragments"],
                            fragments_sha=autre["fragments_sha"])
    faux = [dict(t) for t in m["temoins"]]
    faux[0]["citation"] = not faux[0]["citation"]
    (m["racine"] / "z").mkdir()
    autre = ecrire_construction(m["racine"] / "z", faux, m["voisins"])
    with pytest.raises(ET.Refus, match="diffère de la banque"):
        executer_etalonnage(m, f, sha_compagnon(f), m["racine"] / "d3", journal=autre["journal"],
                            journal_sha=autre["journal_sha"], fragments=autre["fragments"],
                            fragments_sha=autre["fragments_sha"])
    with pytest.raises(ET.Refus, match="journal de construction : empreinte différente"):
        executer_etalonnage(m, f, sha_compagnon(f), m["racine"] / "d4", journal_sha="4" * 64)
    assert not any((m["racine"] / d).exists() for d in ("d1", "d2", "d3", "d4"))


# --- 13. v2 : la pièce d'étalonnage est liée à son dossier -------------------------------------------------------------------


def test_v2_piece_liee_a_son_dossier(tmp_path):
    """Le même étalonnage dans deux dossiers rend deux pièces d'empreintes différentes ; une pièce recopiée dans un autre
    dossier, citée par un audit, est refusée par la lecture."""
    m = monde_complet(tmp_path)
    p1 = m["etalonnage_sha"]
    autre = etalonner(dict(m), dossier=m["racine"] / "autre-dossier")
    assert autre["piece_sha256"] != p1 and autre["piece"]["dossier"] == str((m["racine"] / "autre-dossier").resolve())
    d = m["racine"] / "copie" / ET.SOUS_DOSSIER
    d.mkdir(parents=True)
    (d / ET.FICHIER_PIECE).write_bytes(m["etalonnage"].read_bytes())
    Path(str(d / ET.FICHIER_PIECE) + ".sha256").write_text(f"{p1}  {ET.FICHIER_PIECE}\n", encoding="utf-8")
    ET.ecrire_scelle(d / ET.FICHIER_MANIFESTE, {"factice": True})
    m["etalonnage"] = d / ET.FICHIER_PIECE
    with pytest.raises(ET.Refus, match="autre dossier que celui de la lecture"):
        lire(m)
    assert not (m["racine"] / "copie" / LI.SOUS_DOSSIER).exists()


# --- 14. v3 (a) : piège « reprise assumée », quatrième nature, séparée des conformes non citants -----------------------------


def _comptes(m, juge):
    c = json.loads(m["etalonnage"].read_text(encoding="utf-8"))[ET.CLE_RESERVES]["par_juge"][juge]
    lu = {(s["classe"], s["citation"], s["item_plante"], s["voisins"]): [s["compte"], s["sur"]] for s in c["strates"]}
    return c, lu


def test_v3_piege_reprise_assumee_quatrieme_nature(tmp_path):
    """Cas sain : le juge Opus rend reserves_tenues faux sur les bons au fragment « voisins » piège « reprise assumée » ;
    les cartes tombent dans la nature `conforme_piege_reprise_assumee`, la strate des bons conformes non citants reste à 0 ;
    recalcul égal strate par strate."""
    plante = plant_sur("VP")
    m = fabriquer(tmp_path, erreurs=np.zeros((200, 5), dtype=bool), plante=plante)
    etalonner(m)
    c, lu = _comptes(m, "juge-opus")
    assert lu == attendu_reserves(m, "juge-opus", plante)["juge-opus"]
    n_vp = sum(1 for t in m["temoins"] if t["moitie"] == "etalonnage" and m["voisins"][t["identifiant_interne"]] == "VP")
    assert n_vp > 0
    assert c["par_voisins"]["conforme_piege_reprise_assumee"] == {"compte": n_vp, "sur": n_vp}
    assert all(s[0] == 0 for k, s in lu.items() if k[0] == "bon" and k[3] == "conforme_non_citant")
    assert set(c["par_voisins"]) == set(ET.NATURES_VOISINS)


def test_v3_piege_reprise_assumee_ne_se_mele_pas_aux_non_citants(tmp_path):
    """Artefact : le plant sur les bons conformes non citants (simples) ; la nature piège reste à 0 et les cartes tombent
    toutes chez les non citants — en v2, piège et simples étaient comptés ensemble."""
    plante = plant_sur("VN")
    m = fabriquer(tmp_path, erreurs=np.zeros((200, 5), dtype=bool), plante=plante)
    etalonner(m)
    c, lu = _comptes(m, "juge-opus")
    assert lu == attendu_reserves(m, "juge-opus", plante)["juge-opus"]
    assert c["par_voisins"]["conforme_piege_reprise_assumee"]["compte"] == 0
    assert c["par_voisins"]["conforme_piege_reprise_assumee"]["sur"] > 0
    assert any(s[0] > 0 for k, s in lu.items() if k[0] == "bon" and k[3] == "conforme_non_citant")


# --- 15. v3 (b) : fragments_sha256 de la banque comparé -----------------------------------------------------------------


def test_v3_banque_fragments_sha256_egal_passe(tmp_path):
    m = fabriquer(tmp_path)
    tete = json.loads(m["banque"].read_text(encoding="utf-8"))
    assert tete["fragments_sha256"] == m["fragments_sha"]
    assert etalonner(m)["piece"]["fragments_sha256"] == m["fragments_sha"]


@pytest.mark.parametrize("valeur", ["5" * 64, None])
def test_v3_banque_fragments_sha256_different_ou_absent_refus(tmp_path, valeur):
    m = fabriquer(tmp_path, banque_fragments_sha=valeur)
    tete = json.loads(m["banque"].read_text(encoding="utf-8"))
    assert tete.get("fragments_sha256") == valeur
    with pytest.raises(ET.Refus, match="fragments_sha256 est absent ou différent"):
        etalonner(m)
    assert not (m["racine"] / "lecture-ligne-3" / ET.SOUS_DOSSIER).exists()
