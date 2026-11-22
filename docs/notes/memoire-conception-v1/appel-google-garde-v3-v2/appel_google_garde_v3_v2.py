"""Appel d'un énoncé à Argon ou Carbon (Google), sous la garde commune garde_google_v3, version 2 (22 novembre 2026).

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
Usage : python -I appel_google_garde_v3_v2.py {argon|carbon} ENONCE SORTIE_MD SORTIE_JSON --journal JOURNAL.jsonl
        [--plafond-usd X (≤ 3)] [--mots N]
"""
import argparse
import datetime as dt
import hashlib
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

MODELE = {"argon": "gemini-4-argon", "carbon": "gemini-4-carbon"}
PAGE_PRIX = os.path.join(RACINE, "docs", "sources", "prix", "page-prix-gemini-api-20261121T134918Z.html")
PAGE_PRIX_SHA256 = "40202cdd6fc4eb04984af6ba5426b234540a0b37d819ed0c1d9d34f1d38fd155"
BASCULE_PRIX = dt.date(2026, 12, 1)
# USD par million de jetons (entrée, sortie), onglet Standard, page de prix scellée ci-dessus (sections « Gemini 4 Argon »
# et « Gemini 4 Carbon », lues par la contre-lecture et par collisionneur_v9_v8c.py, l. 233) : 2 / 10 jusqu'au
# 30 novembre 2026, 4 / 20 à partir du 1er décembre 2026, pour les deux espèces.
PRIX = {"argon": {"avant": (2.0, 10.0), "apres": (4.0, 20.0)},
        "carbon": {"avant": (2.0, 10.0), "apres": (4.0, 20.0)}}
MARGE_SORTIE = 1.5           # pire cas : sortie au plafond × 1,5 (comme appel_modeles_externes_v6.py)
URL = "https://generativelanguage.googleapis.com/v1beta/models/{}:streamGenerateContent?alt=sse"
PLAFOND = 65536              # limite en flux de la garde v3 (Argon et Carbon)
PROVISION = 49152            # réflexion comptée ; texte réservé : 16 384 ≥ 16 000
PLAFOND_COURSE_USD = 3.0     # accord de la mère sous GO-2026-11-22-29 : 3 USD au plus pour la course
MOTIF_MOTS = re.compile(r"(\d[\d   ]*)\s*mots\b", re.IGNORECASE)


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


def limite_mots(enonce, mots_declares):
    vus = [int(re.sub(r"\D", "", m)) for m in MOTIF_MOTS.findall(enonce)]
    vus = [v for v in vus if v > 0]
    if not vus:
        raise Refus("limite de mots : aucune mention « N mots » dans l'énoncé")
    mots = max(vus)
    if mots_declares is not None and mots_declares != mots:
        raise Refus(f"limite de mots : --mots {mots_declares} différent de la limite écrite dans l'énoncé ({mots})")
    return mots


def lire_journal(chemin):
    """Somme comptée des lignes du journal : coût compté si l'appel a rendu un usage, sinon son pire cas. Une ligne
    illisible est un refus (jamais sautée)."""
    total, n = 0.0, 0
    if not os.path.exists(chemin):
        return total, n
    with open(chemin, encoding="utf-8") as f:
        for i, ligne in enumerate(f, start=1):
            if not ligne.strip():
                continue
            try:
                d = json.loads(ligne)
                total += float(d["cout_compte_usd"])
            except (json.JSONDecodeError, KeyError, TypeError, ValueError):
                raise Refus(f"journal {chemin}, ligne {i} illisible : dépense cumulée non vérifiable")
            n += 1
    return total, n


def ajouter_journal(chemin, entree):
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(json.dumps(entree, ensure_ascii=False) + "\n")


def lire_flux(lignes):
    """Lit un flux SSE. Rend (texte, usage, fin, retour, message_fin, erreur, servi, rid, defaut_flux, ignorees)."""
    texte, usage, fin, retour, message_fin, erreur, servi, rid = [], {}, None, None, None, None, None, None
    defaut_flux, ignorees = None, 0
    for brute in lignes:
        ligne = brute.decode("utf-8", "replace").strip() if isinstance(brute, bytes) else str(brute).strip()
        if not ligne or ligne.startswith(":"):
            continue
        if not ligne.startswith("data:"):
            ignorees += 1          # champ SSE autre que data (event:, id:, retry:) : compté au journal
            continue
        try:
            d = json.loads(ligne[5:])
        except json.JSONDecodeError:
            defaut_flux = defaut_flux or "FLUX_ILLISIBLE"
            continue
        if not isinstance(d, dict):
            defaut_flux = defaut_flux or "FLUX_ILLISIBLE"
            continue
        if d.get("error"):
            erreur = d.get("error")
            defaut_flux = "ERREUR_FLUX"
        for c in d.get("candidates", []) or []:
            for part in (c.get("content") or {}).get("parts", []) or []:
                if not part.get("thought") and "text" in part:
                    texte.append(part["text"])
            fin = c.get("finishReason") or fin
            message_fin = c.get("finishMessage") or message_fin
        retour = d.get("promptFeedback") or retour
        usage = d.get("usageMetadata") or usage
        servi = d.get("modelVersion") or servi
        rid = d.get("responseId") or rid
    return "".join(texte), usage, fin, retour, message_fin, erreur, servi, rid, defaut_flux, ignorees


def defaut_modele(demande, servi):
    if not servi:
        return "MODELE_SERVI_ABSENT"
    if not (servi == demande or servi.startswith(demande + "-")):
        return "MODELE_SERVI_DIFFERENT"
    return None


def main(argv=None, ouvrir=urllib.request.urlopen, maintenant=None):
    p = argparse.ArgumentParser()
    p.add_argument("espece", choices=sorted(MODELE))
    p.add_argument("enonce")
    p.add_argument("sortie_md")
    p.add_argument("sortie_json")
    p.add_argument("--journal", required=True)
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
        enonce = open(a.enonce, encoding="utf-8").read()
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
        deja, n_avant = lire_journal(a.journal)
        if deja + pire > a.plafond_usd:
            raise Refus(f"plafond cumulé : {deja:.4f} USD déjà comptés + pire cas {pire:.4f} > {a.plafond_usd}")
        cle = os.environ.get("GEMINI_API_KEY")
        if not cle:
            raise Refus("variable GEMINI_API_KEY absente")
    except Refus as e:
        print(f"ARRET : {e}", file=sys.stderr)
        return 1
    heure = maintenant.strftime("%Y-%m-%dT%H:%M:%SZ")
    # Réservation au journal avant l'envoi : si le script meurt, le pire cas reste compté.
    ajouter_journal(a.journal, {"heure": heure, "etat": "reserve", "sortie_json": a.sortie_json,
                                "cout_compte_usd": round(pire, 6)})
    t0 = time.time()
    req = urllib.request.Request(URL.format(MODELE[a.espece]), data=json.dumps(corps).encode("utf-8"), method="POST",
                                 headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    code, erreur_reseau = None, None
    texte, usage, fin, retour, message_fin, erreur, servi, rid, defaut_flux, ignorees = "", {}, None, None, None, None, None, None, None, 0
    try:
        with ouvrir(req, timeout=900) as r:
            code = r.status
            texte, usage, fin, retour, message_fin, erreur, servi, rid, defaut_flux, ignorees = lire_flux(r)
    except urllib.error.HTTPError as e:
        code, erreur = e.code, e.read().decode("utf-8", "replace").replace(cle, "[clé masquée]")
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        erreur_reseau = f"RESEAU_{type(e).__name__}"
        erreur = f"{type(e).__name__}: {str(e).replace(cle, '[clé masquée]')}"
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
    usage_lu = bool(usage) and code == 200
    cout = entree * pe / 1e6 + (jetons_texte + (pensees or 0)) * ps / 1e6
    cout_compte = cout if usage_lu else pire     # sans usage sûr, le pire cas reste compté
    sortie_texte = None
    if texte:
        sortie_texte = a.sortie_md if defaut is None else a.sortie_md + ".defaut.md"
        with open(sortie_texte, "x", encoding="utf-8") as f:
            f.write(texte.replace(cle, "[clé masquée]"))
    meta = {"script": os.path.basename(__file__), "script_sha256": sha256_fichier(os.path.abspath(__file__)),
            "garde": garde.VERSION_GARDE, "garde_sha256": sha256_fichier(garde.__file__),
            "garde_motifs": "controle_ia.relecture_fable_api_v5.garde_motifs",
            "garde_motifs_sha256": sha256_fichier(sys.modules["controle_ia.relecture_fable_api_v5"].__file__),
            "espece": a.espece, "modele_demande": MODELE[a.espece], "modele_servi": servi, "id_reponse": rid,
            "code_http": code, "raison_arret": fin, "defaut": defaut,
            "verdict": "reponse" if defaut is None else "defaut",
            "reglage": corps["generationConfig"], "provision_reflexion": PROVISION, "mots_enonce": mots,
            "jetons_entree": entree, "jetons_reflexion": pensees, "jetons_texte": jetons_texte,
            "prix_usd_par_million": {"entree": pe, "sortie": ps},
            "prix_source": os.path.relpath(PAGE_PRIX, RACINE), "prix_source_sha256": PAGE_PRIX_SHA256,
            "cout_estime_usd": round(cout, 6), "cout_compte_usd": round(cout_compte, 6), "pire_cas_usd": round(pire, 6),
            "depense_cumulee_avant_usd": round(deja, 6), "appels_avant": n_avant, "plafond_course_usd": a.plafond_usd,
            "lignes_sse_ignorees": ignorees, "erreur_fournisseur": erreur,
            "details": {"promptFeedback": retour, "finishMessage": message_fin}, "duree_s": round(time.time() - t0, 1),
            "enonce_chemin": a.enonce, "enonce_sha256": hashlib.sha256(enonce.encode("utf-8")).hexdigest(),
            "sortie_texte": sortie_texte, "heure": heure, "variable_cle": "GEMINI_API_KEY"}
    if sortie_texte:
        meta["sortie_texte_sha256"] = ecrire_compagnon(sortie_texte)
    with open(a.sortie_json, "x", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    ecrire_compagnon(a.sortie_json)
    ajouter_journal(a.journal, {"heure": heure, "etat": "solde", "sortie_json": a.sortie_json,
                                "cout_compte_usd": round(cout_compte - pire, 6), "verdict": meta["verdict"],
                                "defaut": defaut})
    print(json.dumps({k: meta[k] for k in ("verdict", "defaut", "raison_arret", "modele_servi", "jetons_entree",
                                            "jetons_reflexion", "jetons_texte", "cout_compte_usd", "duree_s")},
                     ensure_ascii=False))
    return 0 if defaut is None else 3


if __name__ == "__main__":
    sys.exit(main())
