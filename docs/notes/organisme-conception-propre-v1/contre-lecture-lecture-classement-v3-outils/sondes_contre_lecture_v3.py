#!/usr/bin/env python3
"""Sondes du contre-lecteur (modèle B) — outil du lecteur v3, course « conception propre ».

Jouées sur une **copie non modifiée** de l'outil et du classement v3 (dossier `LC_MODULES`, dans le bloc-notes), avec les
doublures et les fiches factices des essais de l'auteur (module `essais_lecture_classement_v3.py` importé comme
bibliothèque). Aucune fiche réelle, aucun témoin n'est ouvert ni affiché : les témoins épinglés ne sont lus que par les
programmes, sous la racine factice des essais ; cette pièce n'en rend que des empreintes, des comptes et des booléens.

Hors réseau : à lancer dans un espace de noms réseau vide où seule la boucle locale est montée,

    LC_MODULES=… TMPDIR=… unshare -n .venv/bin/python -B sondes_contre_lecture_v3.py SORTIE.json

(la boucle locale `lo` est montée par ce programme, par `ioctl`, si elle est éteinte ; aucune autre interface n'existe).

Les sondes s1 et s2 remplacent, **dans le module chargé en mémoire seulement**, l'adresse d'amont par une adresse de la
boucle locale (serveurs factices de ce fichier) : `transport_reel` est alors exercé tel qu'il est écrit, sans qu'aucun
paquet puisse quitter la machine. Clés factices seulement.
"""
from __future__ import annotations

import hashlib
import http.server
import importlib.util
import json
import os
import sys
import tempfile
import threading
import time
import traceback
from pathlib import Path

ICI = Path(__file__).resolve().parent
V3 = ICI.parent / "lecture-classement-v3"
V2 = ICI.parent / "lecture-classement-v2"


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


E = charger("essais_v3_bibliotheque", V3 / "essais_lecture_classement_v3.py")
O, K = E.O, E.K


class MP:
    """Remplace `monkeypatch` de pytest pour les aides des essais."""

    def setenv(self, k, v):
        os.environ[k] = v


def monter_boucle_locale() -> str:
    """Monte `lo` dans l'espace de noms réseau courant (SIOCGIFFLAGS, SIOCSIFFLAGS) ; rend la liste des interfaces."""
    import fcntl
    import socket
    import struct
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    nom = struct.pack("16sH14s", b"lo", 0, b"")
    drapeaux = struct.unpack("16sH14s", fcntl.ioctl(s, 0x8913, nom))[1]
    fcntl.ioctl(s, 0x8914, struct.pack("16sH14s", b"lo", drapeaux | 1, b""))
    s.close()
    return ",".join(n for _, n in socket.if_nameindex())


def octets_de(dossier) -> bytes:
    return b"".join(p.read_bytes() for p in Path(dossier).rglob("*") if p.is_file())


def serveur(gestion):
    class G(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            self.rfile.read(int(self.headers.get("Content-Length") or 0))
            gestion(self)

        do_GET = do_POST
    s = http.server.ThreadingHTTPServer(("127.0.0.1", 0), G)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s


def plan(n):
    return {f"B{i}": ("propa", "levier:cout", "ajout", "processeur", {}) for i in range(n)}


# --- s1 : clé portant un retour chariot ou un saut de ligne final ---------------------------------------------------------

def s1(tmp):
    res = {}
    vus = []
    srv = serveur(lambda h: (vus.append(1), h.send_response(200), h.end_headers()))
    ancienne = O.URL_AMONT
    O.URL_AMONT = f"http://127.0.0.1:{srv.server_address[1]}/v1/chat/completions"
    try:
        for nom, fin in (("retour_chariot", "\r"), ("saut_de_ligne", "\n")):
            cle = "sk-sonde-factice-CLE-A-NE-PAS-ECRIRE-9876543210"
            env, _ = E.preparer(tmp / f"s1-{nom}")
            os.environ["OPENAI_API_KEY"] = cle + fin
            r = O.envoyer(env)  # transport réel de l'outil, adresse de la boucle locale
            fichiers = [p.name for p in env.iterdir() if cle.encode() in p.read_bytes()]
            res[nom] = {"issue": r["issue"], "detail": r["detail"], "cle_ecrite_dans": sorted(fichiers),
                        "serveur_contacte": bool(vus), "depense_comptee_usd": r["depense_comptee_usd"],
                        "reprise": None}
            try:
                os.environ["OPENAI_API_KEY"] = cle
                O.envoyer(env)
            except O.Refus as e:
                res[nom]["reprise"] = "refusée : " + str(e)[:80]
    finally:
        O.URL_AMONT = ancienne
        srv.shutdown()
    return res


# --- s2 : redirection 302 de l'amont (ou d'un intermédiaire) vers un autre hôte -------------------------------------------

def s2(tmp):
    recus = []
    cle = "sk-sonde-factice-REDIRECTION-1234567890"

    def cible(h):
        recus.append({"methode": h.command, "hote": h.headers.get("Host"), "chemin": h.path,
                      "autorisation_recue": h.headers.get("Authorization") == "Bearer " + cle})
        h.send_response(200)
        h.send_header("Content-Type", "application/json")
        h.end_headers()
        h.wfile.write(b'{"ailleurs": true}')
    b = serveur(cible)

    def amont(h):
        h.send_response(302)
        h.send_header("Location", f"http://localhost:{b.server_address[1]}/ailleurs")
        h.send_header("Content-Length", "0")
        h.end_headers()
    a = serveur(amont)
    ancienne = O.URL_AMONT
    O.URL_AMONT = f"http://127.0.0.1:{a.server_address[1]}/v1/chat/completions"
    try:
        statut, rep = O.transport_reel(O.URL_AMONT, {"Content-Type": "application/json",
                                                     "Authorization": "Bearer " + cle}, b"{}", 5)
    finally:
        O.URL_AMONT = ancienne
        a.shutdown()
        b.shutdown()
    return {"statut_rendu_a_l_outil": statut, "corps_vient_de_l_autre_hote": rep == b'{"ailleurs": true}',
            "requetes_recues_par_l_autre_hote": recus}


# --- s3 : usage sous-déclaré ----------------------------------------------------------------------------------------------

def s3(tmp):
    prix = {"entree": 10.0, "sortie": 50.0, "cache": 10.0, "source": "sonde"}
    res = {}
    for nom, usage in (("zeros", {"prompt_tokens": 0, "completion_tokens": 0}),
                       ("un_jeton", {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}),
                       ("total_sous_la_somme", {"prompt_tokens": 9000, "completion_tokens": 3000, "total_tokens": 5})):
        base = {"object": "chat.completion", "model": "gpt-6-astra", "usage": usage,
                "choices": [{"index": 0, "message": {"content": "x" * 4000, "refusal": None}, "finish_reason": "stop"}]}
        a = O.analyser_reponse(200, json.dumps(base).encode(), 2.0, prix)
        res[nom] = {"anomalies": a["anomalies"], "cout_usd": a["cout_usd"], "au_pire_cas": a["au_pire_cas"]}
    return res


# --- s4 : réponses déposées à la main, sans passer par `envoyer` ----------------------------------------------------------

def s4(tmp):
    env, _ = E.preparer(tmp / "s4")
    E.lire(env)  # aide des essais : écrit et scelle les réponses, sans journal
    r = E.classer(env)
    return {"journal_existe": (env / O.JOURNAL).exists(), "verdict": r["verdict"], "designees": len(r["designees"]),
            "lecture_complete": r["lecture_complete"]["complete"]}


# --- s5, s6 : réponses mal formées qui font tomber l'analyse --------------------------------------------------------------

def s5(tmp):
    res = {}

    def casse_details(o):
        o["usage"]["prompt_tokens_details"] = []
        o["usage"]["completion_tokens_details"] = "x"

    def casse_message(o):
        o["choices"][0]["message"] = "texte nu"
    for nom, casse in (("details_d_usage_non_objets", casse_details), ("message_non_objet", casse_message)):
        env, man = E.preparer(tmp / f"s5-{nom}")
        d = E.Doublure(env)

        def transport(url, entetes, corps, delai, d=d, casse=casse):
            st, rep = d(url, entetes, corps, delai)
            o = json.loads(rep)
            casse(o)
            return st, json.dumps(o).encode()
        os.environ["OPENAI_API_KEY"] = E.CLE_FACTICE
        try:
            r = O.envoyer(env, transport=transport)
            issue = {"issue": r["issue"], "detail": r["detail"]}
        except Exception as ex:
            issue = {"exception": type(ex).__name__, "message": str(ex)[:100],
                     "derniere_ligne": traceback.extract_tb(ex.__traceback__)[-1].name}
        j = O.lire_journal(env)
        res[nom] = {**issue, "reponse_payee_gardee": (env / "reponse-L1-lot1-v3.json").exists(),
                    "erreur_ecrite": (env / "erreur-L1-lot1-v3.json").exists(), "en_vol": j["en_vol"],
                    "depense_comptee_usd": round(j["depense_usd"], 6),
                    "pire_cas_usd": man["garde_depense"]["envois"][0]["pire_cas_usd"]}
    return res


def s6(tmp):
    res = {}
    for nom, corps in (("erreur_en_chaine", b'{"error": "texte libre de la passerelle"}'),
                       ("erreur_en_liste", b'{"error": ["a"]}'), ("corps_liste", b'[1, 2]')):
        env, _ = E.preparer(tmp / f"s6-{nom}")
        os.environ["OPENAI_API_KEY"] = E.CLE_FACTICE
        try:
            r = O.envoyer(env, transport=lambda u, e, c, d, corps=corps: (502, corps))
            issue = {"issue": r["issue"], "detail": r["detail"]}
        except Exception as ex:
            issue = {"exception": type(ex).__name__, "message": str(ex)[:100]}
        j = O.lire_journal(env)
        res[nom] = {**issue, "erreur_ecrite": (env / "erreur-L1-lot1-v3.json").exists(), "en_vol": j["en_vol"]}
    return res


# --- s7 : régénération déterministe, mêmes ordres et mêmes étiquettes que la v2 -------------------------------------------

def bloc_fiches(texte):
    tete, _, reste = texte.partition("=== Lot ")
    return tete, json.loads(reste.split("```json\n")[-1].rsplit("\n```", 1)[0])


def s7(tmp):
    v2 = charger("outil_v2_reference", V2 / "outil_lecteur_conception_propre_v2.py")
    res = {}
    for n_reelles in (8, 23):  # 28 et 43 fiches dans la pile (43 : taille de la pile de R-2645)
        fs = E.fiches_factices(plan(n_reelles), hors=False) if n_reelles == 23 else E.fiches_factices()
        base = tmp / f"s7-{n_reelles}"
        pf, h = E.ecrire_fiches(base, fs)
        pa = E.ecrire_attestation(base, h)
        rac = E.racine_de(base)
        a = E.opreparer(pf, pa, rac / "envois-a", rac)
        b = E.opreparer(pf, pa, rac / "envois-b", rac)
        m2 = v2.preparer(pf, pa, rac / "envois-v2", rac)
        ident = {n: (rac / "envois-a" / n).read_bytes() == (rac / "envois-b" / n).read_bytes() for n in a["fichiers"]}
        c3 = json.loads((rac / "envois-a" / "cle-lectures-v3.json").read_text(encoding="utf-8"))
        c2 = json.loads((rac / "envois-v2" / "cle-lectures-v2.json").read_text(encoding="utf-8"))
        servi = {}
        for v, d, cle, suffixe in (("v2", rac / "envois-v2", c2, "v2"), ("v3", rac / "envois-a", c3, "v3")):
            servi[v] = {}
            for L in O.LECTURES:
                tetes, parl = set(), {}
                for k in range(1, len(cle[L]["lots"]) + 1):
                    tete, fiches = bloc_fiches((d / f"envoi-{L}-lot{k}-{suffixe}.txt").read_text(encoding="utf-8"))
                    tetes.add(hashlib.sha256(tete.encode()).hexdigest())
                    assert [x["etiquette"] for x in fiches] == cle[L]["lots"][k - 1]
                    for x in fiches:
                        parl[x["etiquette"]] = hashlib.sha256(json.dumps(x["fiche"], ensure_ascii=False).encode()).hexdigest()
                servi[v][L] = {"tetes": sorted(tetes), "fiches": parl}
        res[f"pile_{a['pile']['fiches']}"] = {
            "deux_preparations_v3_identiques_octet_pour_octet": all(ident.values()), "fichiers_compares": len(ident),
            "manifestes_differents_par_l_heure_seule": (
                {k: v for k, v in a.items() if k != "prepare_le"} == {k: v for k, v in b.items() if k != "prepare_le"}),
            "ordres_egaux_v2_v3": all(c2[L]["ordre"] == c3[L]["ordre"] for L in O.LECTURES),
            "etiquettes_egales_v2_v3": all(c2[L]["etiquettes"] == c3[L]["etiquettes"] for L in O.LECTURES),
            "pile_interne_egale_v2_v3": ((rac / "envois-v2" / "pile-interne-v2.json").read_bytes()
                                         == (rac / "envois-a" / "pile-interne-v3.json").read_bytes()),
            "vue_servie_par_etiquette_egale_v2_v3": all(servi["v2"][L]["fiches"] == servi["v3"][L]["fiches"]
                                                        for L in O.LECTURES),
            "preambule_egal_v2_v3_et_unique": all(servi["v2"][L]["tetes"] == servi["v3"][L]["tetes"]
                                                  and len(servi["v3"][L]["tetes"]) == 1 for L in O.LECTURES),
            "lots_v2": m2["lots"]["tailles"], "lots_v3": a["lots"]["tailles"],
            "graines_v3": a["graines"], "graines_egales_v2_v3": a["graines"] == m2["graines"],
            "suite_des_etiquettes_L1": [c3["L1"]["lots"][0][0], c3["L1"]["lots"][-1][-1]],
            "lots_consecutifs_sans_trou": all([e for lot in c3[L]["lots"] for e in lot]
                                              == [f"F{i:02d}" for i in range(1, a["pile"]["fiches"] + 1)]
                                              for L in O.LECTURES)}
    return res


# --- s8 : un dossier neuf remet le compte de la dépense à zéro ------------------------------------------------------------

def s8(tmp):
    base = tmp / "s8"
    pf, h = E.ecrire_fiches(base, E.fiches_factices())
    pa = E.ecrire_attestation(base, h)
    rac = E.racine_de(base)
    E.opreparer(pf, pa, rac / "envois", rac, plafond_usd=14.0)
    r1, d1 = E.envoyer(rac / "envois", MP(), scenarios={3: "length"})
    try:
        E.envoyer(rac / "envois", MP())
        reprise = "permise"
    except O.Refus:
        reprise = "refusée"
    E.opreparer(pf, pa, rac / "envois-bis", rac, plafond_usd=14.0)  # même pile, dossier neuf, même plafond
    r2, d2 = E.envoyer(rac / "envois-bis", MP())
    return {"premier_dossier": {"issue": r1["issue"], "appels": r1["appels"], "depense": r1["depense_comptee_usd"],
                                "reprise": reprise},
            "second_dossier": {"issue": r2["issue"], "appels": r2["appels"], "depense": r2["depense_comptee_usd"],
                               "plafond": r2["plafond_usd"]},
            "depense_totale_des_deux": round(r1["depense_comptee_usd"] + r2["depense_comptee_usd"], 6),
            "memes_corps_renvoyes": len(set(d1.appels) & set(d2.appels))}


# --- s9 : valeur de N illisible mais non nulle (hors de la lettre de C1) --------------------------------------------------

def s9(tmp):
    vue = {"enonce": "un énoncé factice assez long pour porter une citation de vingt caractères"}
    cat = {f"C{i}": ["", "", "mécanisme factice"] for i in range(1, 13)}
    res = {}
    for val in ("Aucune", "aucune ", "none", "C13", 0):
        e = {**{c: {"valeur": 0, "motif": "m"} for c in O.CRITERES}, "N": {"valeur": val}}
        r = O.verifier_entree(e, vue, False, cat)
        res[repr(val)] = {"compte": r["N"]["compte"], "motif": r["N"]["motif"],
                          "anomalie_bloquante_C1": bool(O.cles_manquantes(e))}
    return res


# --- s10 : plafond non fini dans un manifeste rescellé --------------------------------------------------------------------

def s10(tmp):
    env, _ = E.preparer(tmp / "s10")
    p = env / O.MANIFESTE
    texte = p.read_text(encoding="utf-8").replace('"plafond_usd": 14.0', '"plafond_usd": NaN')
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    O.ecrire_scelle(p, texte)
    os.environ["OPENAI_API_KEY"] = E.CLE_FACTICE
    d = E.Doublure(env)
    try:
        r = O.envoyer(env, transport=d)
        issue = {"issue": r["issue"]}
    except O.Refus as e:
        issue = {"refus": str(e)[:100]}
    except Exception as ex:
        issue = {"exception": f"{type(ex).__name__}: {str(ex)[:80]}"}
    j = O.lire_journal(env)
    return {**issue, "appels_partis": len(d.appels), "arret_au_journal": j["arret"] is not None,
            "depense_comptee_usd": round(j["depense_usd"], 6)}


def main(sortie):
    res = {"sondes": "contre-lecture de l'outil du lecteur v3 (contre-lecteur, modèle B)",
           "debut_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "outil_sha256": O.sha256_fichier(E.MODS / "outil_lecteur_conception_propre_v3.py"),
           "classer_sha256": O.sha256_fichier(E.MODS / "classer_conception_propre_v3.py"), "resultats": {}}
    res["interfaces_reseau"] = monter_boucle_locale()
    with tempfile.TemporaryDirectory(prefix="sondes-cl-v3-") as tmp:
        for nom, f in (("s1_cle_avec_fin_de_ligne", s1), ("s2_redirection_vers_un_autre_hote", s2),
                       ("s3_usage_sous_declare", s3), ("s4_reponses_sans_journal", s4),
                       ("s5_reponse_200_mal_formee", s5), ("s6_erreur_mal_formee", s6),
                       ("s7_regeneration", s7), ("s8_dossier_neuf_compte_a_zero", s8),
                       ("s9_N_illisible_non_nulle", s9), ("s10_plafond_NaN_au_manifeste_rescelle", s10)):
            try:
                res["resultats"][nom] = f(Path(tmp))
            except Exception as ex:
                res["resultats"][nom] = {"sonde_en_echec": f"{type(ex).__name__}: {str(ex)[:300]}"}
            os.environ.pop("OPENAI_API_KEY", None)
    res["fin_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    Path(sortie).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res["resultats"], ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
