"""Appel d'un énoncé à Argon ou Carbon (Google), sous la garde commune garde_google_v3, version 6 (22 novembre 2026).

Écrit par la session bibliothécaire (Claude Opus 5.5), pièce d'instrument (classe B), à partir de
docs/notes/demandes-fable-api-2026-11-22-v1/appel_google_garde_v3_v1.py (36c410cd…), qui reste tel quel. Corrige les
défauts relevés par sa contre-lecture (docs/notes/memoire-conception-v1/contre-lecture-appel-google-garde-v3-v1/,
00303c27…), sur accord de la mère (22 novembre, vers 12:22Z) :
  (1) plafond de dépense cumulé par journal de course, 3 USD au plus, compté avant l'envoi (pire cas) ;
  (2) garde de motifs de relecture_fable_api_v5.garde_motifs sur l'énoncé exact avant l'envoi ; un motif = rien ne part ;
  (3) aucun repli silencieux dans le flux : ligne de données illisible = défaut FLUX_ILLISIBLE ; erreur dans le flux =
      défaut ERREUR_FLUX ; erreur réseau nommée RESEAU_<type> ;
  (4) tarif repris de la page de prix scellée, vérifiée par son empreinte avant l'envoi, daté (avant / à partir du
      1er décembre 2026), marge 1,5 sur la sortie dans le pire cas comme le v6 ;
  (5) modèle servi comparé au modèle demandé : absent ou différent = défaut ;
  (6) limite de mots relue dans l'énoncé (toutes les mentions « N mots », la plus haute) ; absente = refus ;
      --mots, s'il est donné, doit l'égaler ;
  (7) journal complet (chemins, empreintes de l'énoncé, de la sortie, du script, de la garde, de la page de prix),
      compagnons .sha256 écrits pour chaque fichier produit.
Avant l'envoi : verifier_reglages_google ; un problème = rien ne part. Après : defaut_reponse_google, puis (3) et (5) ;
un défaut n'est jamais une réponse (texte écrit en .defaut.md à part). Clé GEMINI_API_KEY lue par son nom, jamais affichée
ni écrite. Aucune sortie n'est écrasée (R12).
Version 3 : corrige les points de la vérification de la v2
(docs/notes/memoire-conception-v1/appel-google-garde-v3-v2/verification-appel-google-garde-v3-v2-v1.md) :
  (8) modèle servi : le nom demandé, seul ou suivi d'un suffixe de version numérique (« -001 »), rien d'autre ;
  (9) coût : le pire cas reste compté sauf usage lu, fin présente et aucun défaut de flux ni de réseau ;
  (10) cumul protégé contre les appels en parallèle : verrou exclusif (fcntl) sur le journal, de la lecture à la
       réservation ; journal par identifiant d'appel (réservation, puis solde), montants finis et positifs, solde sans
       réservation ou identifiant répété = refus ;
  (11) flux mal formé (morceau non conforme) = défaut FLUX_ILLISIBLE, jamais une exception ;
  (12) limite de mots écrite en lettres = refus (la limite s'écrit en chiffres) ;
  (13) tarif haut dès le 30 novembre 2026 (un jour de marge sur la bascule de Google, dont le fuseau n'est pas écrit) ;
  (14) empreintes de la garde de Google et de la garde de motifs comparées à leurs compagnons scellés avant l'envoi ;
  (15) énoncé borné (400 000 octets, lignes de 20 000 signes au plus) avant la garde de motifs, qui sinon peut bloquer.
Le journal de course grandit par ajouts ; il se scelle à la fin de la course (`python -m controle_ia.scellement sceller`),
jamais pendant (R12). Les appels d'une même course se font l'un après l'autre ; le verrou protège un lancement
parallèle par erreur.
Version 4 : corrige les points de la vérification de la v3
(docs/notes/memoire-conception-v1/appel-google-garde-v3-v3/verification-appel-google-garde-v3-v3-v1.md) :
  (16) toute exception pendant l'envoi ou la lecture (coupure http.client.IncompleteRead comprise) est un défaut nommé
       RESEAU_<type> ou ERREUR_<type>, journalisé avec son .json et sa ligne de solde ; jamais une chute du script ;
  (17) le texte déjà reçu avant une coupure est gardé (.defaut.md), selon « récupérer ce qui est récupérable » ;
  (18) un texte qui n'est pas une chaîne, un compte de jetons qui n'est pas un entier, une raison d'arrêt qui n'est pas
       une chaîne, un promptFeedback qui n'est pas un objet : FLUX_ILLISIBLE ;
  (19) limite de mots écrite « 10k mots » ou en anglais (« 5000 words ») : refus ;
  (20) empreintes des deux gardes comparées à des valeurs figées dans ce script, en plus de leurs compagnons.
Version 5 (règle du directeur GO-2026-11-22-57 : Argon, Carbon et Neon toujours interrogés ensemble ; plafond de 5 USD
pour les trois sous GO-2026-11-22-58, un journal par modèle) :
  (21) espèce Neon (gemini-4-neon) : réflexion au plus haut niveau admis par la garde (« xhigh ») ; tarif 3 / 15 USD par
       million, palier Standard, sans bascule datée, lu sur la même page de prix scellée (lecture consignée dans
       docs/notes/collisionneur-v9/collisionneur_v9_v8c.py, l. 230-237) ; limite de sortie 65 536 (garde v3) ;
  (22) plafond commun à plusieurs journaux : --journaux-associes J2 J3 (les journaux des autres modèles de la même
       course) ; la dépense déjà comptée est la somme de tous, chacun lu sous verrou partagé ; tout journal associé
       illisible = refus ; plafond de course au plus 5 USD.
Version 6 (vérification de la v5, verification-appel-google-garde-v3-v5-v1.md) :
  (23) un journal associé absent est un refus (le lanceur crée d'abord les journaux vides de la course) ; le total de
       chaque journal est noté dans le .json ;
  (24) verrous pris dans un ordre fixe : tous les journaux de la course (le sien et les associés) sont verrouillés en
       exclusif, triés par chemin réel (realpath), de la lecture jusqu'à la réservation : deux lancements simultanés
       ne s'interbloquent plus et ne dépassent pas le plafond ; identité des journaux jugée sur le chemin réel (un lien
       symbolique vers son propre journal est refusé).
Usage : python -I appel_google_garde_v3_v6.py {argon|carbon} ENONCE SORTIE_MD SORTIE_JSON --journal JOURNAL.jsonl
        [--journaux-associes J ...] [--plafond-usd X (≤ 5)] [--mots N]
"""
import argparse
import datetime as dt
import fcntl
import hashlib
import http.client
import math
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.normpath(os.path.join(ICI, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(RACINE, "src"))
from controle_ia import garde_google_v3 as garde  # noqa: E402
from controle_ia.relecture_fable_api_v5 import garde_motifs  # noqa: E402

MODELE = {"argon": "gemini-4-argon", "carbon": "gemini-4-carbon", "neon": "gemini-4-neon"}
PAGE_PRIX = os.path.join(RACINE, "docs", "sources", "prix", "page-prix-gemini-api-20261121T134918Z.html")
PAGE_PRIX_SHA256 = "40202cdd6fc4eb04984af6ba5426b234540a0b37d819ed0c1d9d34f1d38fd155"
BASCULE_PRIX = dt.date(2026, 11, 30)   # Google : 1er décembre ; un jour de marge (fuseau non écrit)
# USD par million de jetons (entrée, sortie), onglet Standard, page de prix scellée ci-dessus (sections « Gemini 4 Argon »
# et « Gemini 4 Carbon », lues par la contre-lecture et par collisionneur_v9_v8c.py, l. 233) : 2 / 10 jusqu'au
# 30 novembre 2026, 4 / 20 à partir du 1er décembre 2026, pour les deux espèces.
PRIX = {"argon": {"avant": (2.0, 10.0), "apres": (4.0, 20.0)},
        "carbon": {"avant": (2.0, 10.0), "apres": (4.0, 20.0)},
        "neon": {"avant": (3.0, 15.0), "apres": (3.0, 15.0)}}   # aucune bascule datée écrite pour Neon
MARGE_SORTIE = 1.5           # pire cas : sortie au plafond × 1,5 (comme appel_modeles_externes_v6.py)
URL = "https://generativelanguage.googleapis.com/v1beta/models/{}:streamGenerateContent?alt=sse"
PLAFOND = 65536              # limite en flux de la garde v3 (Argon et Carbon)
PROVISION = 49152            # réflexion comptée ; texte réservé : 16 384 ≥ 16 000
PLAFOND_COURSE_USD = 5.0     # GO-2026-11-22-58 : 5 USD au plus pour les trois modèles de la course
MOTIF_MOTS = re.compile(r"(\d[\d   ]*)\s*mots\b", re.IGNORECASE)
MOTIF_MOTS_LETTRES = re.compile(r"\b(un|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|vingt|trente|quarante|cinquante|"
                                r"soixante|cent|cents|mille|milliers?)\s+mots\b", re.IGNORECASE)
MOTIF_MOTS_AUTRES = re.compile(r"\d[\d ]*\s*[kK]\s*mots\b|\d[\d ,.]*\s*words?\b", re.IGNORECASE)
GARDES_SHA256 = {"garde_google_v3.py": "923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91",
                 "relecture_fable_api_v5.py": "052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8"}
OCTETS_MAX = 400_000
SIGNES_LIGNE_MAX = 20_000
MODELE_SERVI = {e: re.compile(re.escape(m) + r"(-\d{1,4})?") for e, m in MODELE.items()}


class Refus(Exception):
    pass


def sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 16), b""):
            h.update(bloc)
    return h.hexdigest()


def ecrire_compagnon(chemin):
    """Compagnon .sha256 au format du dépôt ; refuse d'écraser (R12)."""
    h = sha256_fichier(chemin)
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {os.path.basename(chemin)}\n")
    return h


def prix(espece, jour):
    if not os.path.isfile(PAGE_PRIX):
        raise Refus(f"page de prix absente : {PAGE_PRIX}")
    if sha256_fichier(PAGE_PRIX) != PAGE_PRIX_SHA256:
        raise Refus("page de prix : empreinte différente de celle citée ; tarif non vérifiable")
    return PRIX[espece]["avant" if jour < BASCULE_PRIX else "apres"]


def verifier_compagnon(chemin):
    c = chemin + ".sha256"
    if not os.path.isfile(c):
        raise Refus(f"{os.path.basename(chemin)} : compagnon scellé absent")
    attendu = open(c, encoding="utf-8").read().split()[0]
    h = sha256_fichier(chemin)
    fige = GARDES_SHA256.get(os.path.basename(chemin))
    if fige is None or h != fige:
        raise Refus(f"{os.path.basename(chemin)} : empreinte {h[:12]}… différente de la valeur figée dans le script")
    if h != attendu:
        raise Refus(f"{os.path.basename(chemin)} : empreinte {h[:12]}… différente du compagnon scellé {attendu[:12]}…")
    return h


def limite_mots(enonce, mots_declares):
    if MOTIF_MOTS_AUTRES.search(enonce):
        raise Refus("limite de mots écrite en « k » ou en anglais : l'écrire en chiffres, suivie de « mots »")
    if MOTIF_MOTS_LETTRES.search(enonce):
        raise Refus("limite de mots écrite en lettres : l'écrire en chiffres")
    vus = [int(re.sub(r"\D", "", m)) for m in MOTIF_MOTS.findall(enonce)]
    vus = [v for v in vus if v > 0]
    if not vus:
        raise Refus("limite de mots : aucune mention « N mots » dans l'énoncé")
    mots = max(vus)
    if mots_declares is not None and mots_declares != mots:
        raise Refus(f"limite de mots : --mots {mots_declares} différent de la limite écrite dans l'énoncé ({mots})")
    return mots


def lire_journal(f):
    """Dépense cumulée du journal (fichier ouvert et verrouillé) : par identifiant d'appel, le coût du solde s'il existe,
    sinon le pire cas réservé. Toute ligne illisible, montant non fini ou négatif, solde sans réservation ou identifiant
    répété est un refus (jamais sautée). Rend (total, nombre d'appels)."""
    f.seek(0)
    reserves, soldes = {}, {}
    for i, ligne in enumerate(f, start=1):
        if not ligne.strip():
            continue
        try:
            d = json.loads(ligne)
            ident, etat, montant = str(d["id"]), d["etat"], float(d["cout_compte_usd"])
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            raise Refus(f"journal, ligne {i} illisible : dépense cumulée non vérifiable")
        if not math.isfinite(montant) or montant < 0:
            raise Refus(f"journal, ligne {i} : montant {montant!r} non fini ou négatif")
        if etat == "reserve" and ident not in reserves:
            reserves[ident] = montant
        elif etat == "solde" and ident in reserves and ident not in soldes:
            soldes[ident] = montant
        else:
            raise Refus(f"journal, ligne {i} : état {etat!r} ou identifiant {ident!r} incohérent")
    return sum(soldes.get(k, v) for k, v in reserves.items()), len(reserves)


def ajouter_journal(chemin, entree):
    with open(chemin, "a", encoding="utf-8") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.write(json.dumps(entree, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


def etat_flux():
    return {"texte": [], "usage": {}, "fin": None, "retour": None, "message_fin": None, "erreur": None, "servi": None,
            "rid": None, "defaut_flux": None, "ignorees": 0}


def _entier_ou_absent(v):
    return v is None or (isinstance(v, int) and not isinstance(v, bool) and v >= 0)


def lire_flux(lignes, e=None):
    """Lit un flux SSE dans l'état `e` (mis à jour au fil de la lecture : ce qui est reçu avant une coupure est gardé).
    Rend l'état."""
    e = etat_flux() if e is None else e
    for brute in lignes:
        ligne = brute.decode("utf-8", "replace").strip() if isinstance(brute, bytes) else str(brute).strip()
        if not ligne or ligne.startswith(":"):
            continue
        if not ligne.startswith("data:"):
            e["ignorees"] += 1      # champ SSE autre que data (event:, id:, retry:) : compté au journal
            continue
        try:
            d = json.loads(ligne[5:])
        except json.JSONDecodeError:
            e["defaut_flux"] = e["defaut_flux"] or "FLUX_ILLISIBLE"
            continue
        if not isinstance(d, dict):
            e["defaut_flux"] = e["defaut_flux"] or "FLUX_ILLISIBLE"
            continue
        if d.get("error"):
            e["erreur"] = d.get("error")
            e["defaut_flux"] = "ERREUR_FLUX"
        try:
            morceaux, fin_m, msg_m = [], e["fin"], e["message_fin"]
            for c in d.get("candidates", []) or []:
                for part in (c.get("content") or {}).get("parts", []) or []:
                    if not part.get("thought") and "text" in part:
                        if not isinstance(part["text"], str):
                            raise TypeError("text")
                        morceaux.append(part["text"])
                f = c.get("finishReason")
                if f is not None and not isinstance(f, str):
                    raise TypeError("finishReason")
                fin_m = f or fin_m
                msg_m = c.get("finishMessage") or msg_m
            u = d.get("usageMetadata")
            if u is not None and (not isinstance(u, dict) or not all(
                    _entier_ou_absent(u.get(k)) for k in ("promptTokenCount", "candidatesTokenCount",
                                                         "thoughtsTokenCount"))):
                raise TypeError("usageMetadata")
            pf = d.get("promptFeedback")
            if pf is not None and not isinstance(pf, dict):
                raise TypeError("promptFeedback")
        except (AttributeError, TypeError):
            e["defaut_flux"] = e["defaut_flux"] or "FLUX_ILLISIBLE"
            continue
        e["texte"].extend(morceaux)
        e["fin"], e["message_fin"] = fin_m, msg_m
        e["retour"] = pf or e["retour"]
        e["usage"] = u or e["usage"]
        e["servi"] = d.get("modelVersion") or e["servi"]
        e["rid"] = d.get("responseId") or e["rid"]
    return e


def defaut_modele(demande, servi):
    if not servi:
        return "MODELE_SERVI_ABSENT"
    espece = next(e for e, m in MODELE.items() if m == demande)
    if not (isinstance(servi, str) and MODELE_SERVI[espece].fullmatch(servi)):
        return "MODELE_SERVI_DIFFERENT"
    return None


def main(argv=None, ouvrir=urllib.request.urlopen, maintenant=None):
    p = argparse.ArgumentParser()
    p.add_argument("espece", choices=sorted(MODELE))
    p.add_argument("enonce")
    p.add_argument("sortie_md")
    p.add_argument("sortie_json")
    p.add_argument("--journal", required=True)
    p.add_argument("--journaux-associes", nargs="*", default=[])
    p.add_argument("--plafond-usd", type=float, default=PLAFOND_COURSE_USD)
    p.add_argument("--mots", type=int, default=None)
    a = p.parse_args(argv)
    maintenant = maintenant or dt.datetime.now(dt.timezone.utc)
    try:
        if not (0 < a.plafond_usd <= PLAFOND_COURSE_USD):
            raise Refus(f"plafond de course {a.plafond_usd} hors de ]0 ; {PLAFOND_COURSE_USD}]")
        for c in (a.sortie_md, a.sortie_json, a.sortie_md + ".defaut.md"):
            if os.path.exists(c) or os.path.exists(c + ".sha256"):
                raise Refus(f"{c} existe déjà (R12)")
        if os.path.getsize(a.enonce) > OCTETS_MAX:
            raise Refus(f"énoncé au-delà de {OCTETS_MAX} octets")
        enonce = open(a.enonce, encoding="utf-8").read()
        if any(len(l) > SIGNES_LIGNE_MAX for l in enonce.split("\n")):
            raise Refus(f"énoncé : une ligne dépasse {SIGNES_LIGNE_MAX} signes")
        empreinte_garde = verifier_compagnon(garde.__file__)
        empreinte_motifs = verifier_compagnon(sys.modules["controle_ia.relecture_fable_api_v5"].__file__)
        motifs = garde_motifs([("enonce", enonce)])
        if motifs:
            raise Refus("garde de motifs : " + " ; ".join(f"{m['motif']} (ligne {m['ligne']})" for m in motifs))
        mots = limite_mots(enonce, a.mots)
        niveau = garde.NIVEAU_MAX_REFLEXION[a.espece]
        corps = {"contents": [{"role": "user", "parts": [{"text": enonce}]}],
                 "generationConfig": {"maxOutputTokens": PLAFOND,
                                      "thinkingConfig": {"thinkingLevel": niveau, "includeThoughts": True}}}
        problemes = garde.verifier_reglages_google(a.espece, corps, provision=PROVISION, mots=mots, mode="flux")
        if problemes:
            raise Refus("garde : " + " ; ".join(problemes))
        pe, ps = prix(a.espece, maintenant.date())
        jetons_entree_max = len(enonce.encode("utf-8"))   # majorant : au plus un jeton par octet
        pire = jetons_entree_max * pe / 1e6 + PLAFOND * MARGE_SORTIE * ps / 1e6
        cle = os.environ.get("GEMINI_API_KEY")
        if not cle:
            raise Refus("variable GEMINI_API_KEY absente")
        heure = maintenant.strftime("%Y-%m-%dT%H:%M:%SZ")
        ident = hashlib.sha256(f"{heure}|{os.path.abspath(a.sortie_json)}|{os.getpid()}".encode()).hexdigest()[:16]
        # Lecture du cumul et réservation du pire cas sous un même verrou exclusif : si le script meurt, le pire cas
        # reste compté ; deux lancements simultanés ne réservent jamais au-delà du plafond.
        reel = os.path.realpath(a.journal)
        reels_associes = []
        for ja in a.journaux_associes:
            if not os.path.isfile(ja):
                raise Refus(f"journal associé absent : {ja} (créer d'abord les journaux vides de la course)")
            rj = os.path.realpath(ja)
            if rj == reel or rj in reels_associes:
                raise Refus("journal associé identique au journal de l'appel ou répété")
            reels_associes.append(rj)
        ouverts = {}
        try:
            for chemin in sorted([reel] + reels_associes):          # ordre fixe : aucun interblocage
                f = open(chemin, "a+", encoding="utf-8")
                ouverts[chemin] = f
                fcntl.flock(f, fcntl.LOCK_EX)
            deja, n_avant = lire_journal(ouverts[reel])
            totaux_journaux = {a.journal: round(deja, 6)}
            for ja, rj in zip(a.journaux_associes, reels_associes):
                d_a, _ = lire_journal(ouverts[rj])
                totaux_journaux[ja] = round(d_a, 6)
                deja += d_a
            if deja + pire > a.plafond_usd:
                raise Refus(f"plafond cumulé : {deja:.4f} USD déjà comptés + pire cas {pire:.4f} > {a.plafond_usd}")
            fj = ouverts[reel]
            fj.seek(0, os.SEEK_END)
            fj.write(json.dumps({"id": ident, "heure": heure, "etat": "reserve", "sortie_json": a.sortie_json,
                                 "cout_compte_usd": round(pire, 6)}, ensure_ascii=False) + "\n")
            fj.flush()
            os.fsync(fj.fileno())
        finally:
            for f in ouverts.values():
                f.close()
    except Refus as e:
        print(f"ARRET : {e}", file=sys.stderr)
        return 1
    t0 = time.time()
    req = urllib.request.Request(URL.format(MODELE[a.espece]), data=json.dumps(corps).encode("utf-8"), method="POST",
                                 headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    code, erreur_reseau, erreur_http = None, None, None
    ef = etat_flux()
    try:
        with ouvrir(req, timeout=900) as r:
            code = r.status
            lire_flux(r, ef)
    except urllib.error.HTTPError as exc:
        code = exc.code
        try:
            erreur_http = exc.read().decode("utf-8", "replace").replace(cle, "[clé masquée]")
        except Exception as exc2:  # noqa: BLE001 — corps d'erreur illisible : nommé, jamais une chute
            erreur_http = f"corps illisible ({type(exc2).__name__})"
    except (urllib.error.URLError, TimeoutError, OSError, http.client.HTTPException) as exc:
        erreur_reseau = f"RESEAU_{type(exc).__name__}"
        ef["erreur"] = f"{type(exc).__name__}: {str(exc).replace(cle, '[clé masquée]')}"
    except Exception as exc:  # noqa: BLE001 — toute autre exception : défaut nommé, journalisé (R5)
        erreur_reseau = f"ERREUR_{type(exc).__name__}"
        ef["erreur"] = f"{type(exc).__name__}: {str(exc).replace(cle, '[clé masquée]')}"
    texte, usage, fin, retour, message_fin = "".join(ef["texte"]), ef["usage"], ef["fin"], ef["retour"], ef["message_fin"]
    erreur = erreur_http if erreur_http is not None else ef["erreur"]
    servi, rid, defaut_flux, ignorees = ef["servi"], ef["rid"], ef["defaut_flux"], ef["ignorees"]
    pensees = usage.get("thoughtsTokenCount")
    jetons_texte = usage.get("candidatesTokenCount", 0) or 0
    entree = usage.get("promptTokenCount", 0) or 0
    if erreur_reseau:
        defaut = erreur_reseau
    elif code != 200:
        defaut = f"HTTP_{code}"
    else:
        defaut = (defaut_flux
                  or garde.defaut_reponse_google(fin, texte, pensees, blocage=(retour or {}).get("blockReason"))
                  or defaut_modele(MODELE[a.espece], servi))
    usage_lu = bool(usage) and code == 200 and fin is not None and defaut_flux is None and erreur_reseau is None
    cout = entree * pe / 1e6 + (jetons_texte + (pensees or 0)) * ps / 1e6
    cout_compte = cout if usage_lu else pire     # sans usage sûr, le pire cas reste compté
    sortie_texte = None
    if texte:
        sortie_texte = a.sortie_md if defaut is None else a.sortie_md + ".defaut.md"
        with open(sortie_texte, "x", encoding="utf-8") as f:
            f.write(texte.replace(cle, "[clé masquée]"))
    meta = {"script": os.path.basename(__file__), "script_sha256": sha256_fichier(os.path.abspath(__file__)),
            "garde": garde.VERSION_GARDE, "garde_sha256": empreinte_garde,
            "garde_motifs": "controle_ia.relecture_fable_api_v5.garde_motifs",
            "garde_motifs_sha256": empreinte_motifs, "id_appel": ident,
            "espece": a.espece, "modele_demande": MODELE[a.espece], "modele_servi": servi, "id_reponse": rid,
            "code_http": code, "raison_arret": fin, "defaut": defaut,
            "verdict": "reponse" if defaut is None else "defaut",
            "reglage": corps["generationConfig"], "provision_reflexion": PROVISION, "mots_enonce": mots,
            "jetons_entree": entree, "jetons_reflexion": pensees, "jetons_texte": jetons_texte,
            "prix_usd_par_million": {"entree": pe, "sortie": ps},
            "prix_source": os.path.relpath(PAGE_PRIX, RACINE), "prix_source_sha256": PAGE_PRIX_SHA256,
            "cout_estime_usd": round(cout, 6), "cout_compte_usd": round(cout_compte, 6), "pire_cas_usd": round(pire, 6),
            "depense_cumulee_avant_usd": round(deja, 6), "appels_avant": n_avant, "journal": a.journal, "journaux_associes": a.journaux_associes, "totaux_journaux_avant_usd": totaux_journaux, "plafond_course_usd": a.plafond_usd,
            "lignes_sse_ignorees": ignorees, "erreur_fournisseur": erreur,
            "details": {"promptFeedback": retour, "finishMessage": message_fin}, "duree_s": round(time.time() - t0, 1),
            "enonce_chemin": a.enonce, "enonce_sha256": hashlib.sha256(enonce.encode("utf-8")).hexdigest(),
            "sortie_texte": sortie_texte, "heure": heure, "variable_cle": "GEMINI_API_KEY"}
    if sortie_texte:
        meta["sortie_texte_sha256"] = ecrire_compagnon(sortie_texte)
    with open(a.sortie_json, "x", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    ecrire_compagnon(a.sortie_json)
    ajouter_journal(a.journal, {"id": ident, "heure": heure, "etat": "solde", "sortie_json": a.sortie_json,
                                "cout_compte_usd": round(cout_compte, 6), "verdict": meta["verdict"],
                                "defaut": defaut})
    print(json.dumps({k: meta[k] for k in ("verdict", "defaut", "raison_arret", "modele_servi", "jetons_entree",
                                            "jetons_reflexion", "jetons_texte", "cout_compte_usd", "duree_s")},
                     ensure_ascii=False))
    return 0 if defaut is None else 3


if __name__ == "__main__":
    sys.exit(main())
