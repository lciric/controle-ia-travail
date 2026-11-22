"""Astra 6.2 (gpt-6.2-astra) par l'interface par lots d'OpenAI : un seul énoncé scellé — v2 (22 novembre 2026).

v2 : corrige la vérification de la v1 (verification-astra62-lot-enonce-v1.md, d15de75f…) :
  (M1) la relève exige que --lot égale le lot_id de la ligne de soumission du journal et que l'empreinte de l'énoncé
       égale son enonce_sha256 ; (M2) témoin de soumission unique par énoncé, fichier neuf ouvert en « x » à côté de
       l'énoncé (ENONCE.soumis), refus s'il existe ; (f1) compagnon vide, fichier absent, JSON qui n'est pas un objet,
       IncompleteRead : refus nommés ; (f3) identifiant manquant au téléversement ou au lot : refus ; (f4) le défaut
       s'écrit defaut-astra62-v1.md ; (f5) essais ajoutés pour les gardes non tenues. Reste ouvert (f2) : un lot
       « expired », « failed » ou « cancelled » n'est pas relevé ; il est journalisé et la relève s'arrête.
v1 :
Pièce d'instrument (classe B), écrite par une session fille (Opus 5.5) à partir de
docs/notes/ideation-nouvelles-attaques-v1/lot-12-astra-lots-v1/astra62_lots_v1.py (branche lot/compte-organisme-v1,
65a61bf8…, inchangé, R12), sous GO-2026-11-22-74. Changements, et seulement eux :
- l'énoncé n'est plus une liste figée de textes : un seul fichier, donné par --enonce, dont l'empreinte doit égaler
  --empreinte ET son compagnon .sha256 ; garde de motifs (relecture_fable_api_v5.garde_motifs) vide avant tout envoi ;
- GO exigé : GO-2026-11-22-74 ; plafond 5 USD par lot (pire cas, tarif des lots 5 / 20 USD le million) ;
- effort « high » (mot de la mère : « effort élevé ») ; sortie 96 000 jetons (raisonnement compris) ;
- la réponse doit être lue (synthèse de la session) : la sortie brute va dans un fichier neuf (mode « xb »), avec
  compagnon, puis le texte de la réponse est écrit à part, dans un fichier neuf, s'il est complet (fin « stop ») ;
  sinon un fichier .defaut.md garde ce qui est récupérable, jamais présenté comme une réponse ;
- réserves de la vérification du lot 12 corrigées : sortie non JSON, erreur réseau et relève répétée sont des refus
  nommés (code 2), jamais une trace ; la relève exige un dossier de sortie neuf.
Clé OPENAI_API_KEY_2 lue par son nom, jamais affichée ni écrite. Aucune redirection suivie.
Usage :
  python -I astra62_lot_enonce_v1.py a_blanc --enonce E --empreinte H
  python -I astra62_lot_enonce_v1.py soumettre --enonce E --empreinte H --journal J --registre-go GO.md
  python -I astra62_lot_enonce_v1.py relever --enonce E --empreinte H --journal J --lot ID --sortie DOSSIER_NEUF \
         --registre-go GO.md
"""
import argparse, datetime, hashlib, http.client, json, os, re, sys, urllib.error, urllib.request, uuid
from decimal import Decimal as D

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.normpath(os.path.join(ICI, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(RACINE, "src"))
from controle_ia.relecture_fable_api_v5 import garde_motifs  # noqa: E402

BASE = "https://api.openai.com"
MODELE = "gpt-6.2-astra"
EFFORT = "high"
SORTIE_MAX = 96000
TARIF = (D(5), D(20))  # lots : moitié prix (repris du lot 12)
PLAFOND_LOT = D("5")
GO_EXIGES = ("GO-2026-11-22-74",)
IDENT = "astra62-enonce"
FINS = ("stop", "length", "content_filter", "tool_calls")


class Refus(Exception):
    pass


def sha(b):
    return hashlib.sha256(b).hexdigest()


def heure():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class _SansRedirection(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        raise urllib.error.URLError("redirection refusée")


_OUVREUR = urllib.request.build_opener(_SansRedirection)


def transport_reel(methode, chemin, cle, corps=None, entetes=None, delai=120):
    h = {"authorization": "Bearer " + cle}
    h.update(entetes or {})
    req = urllib.request.Request(BASE + chemin, data=corps, headers=h, method=methode)
    try:
        with _OUVREUR.open(req, timeout=delai) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()
    except (urllib.error.URLError, OSError, http.client.HTTPException) as e:
        raise Refus(f"erreur réseau ({type(e).__name__})")


def lire_enonce(chemin, empreinte):
    if not os.path.isfile(chemin):
        raise Refus("énoncé absent")
    b = open(chemin, "rb").read()
    if sha(b) != empreinte:
        raise Refus("énoncé : empreinte différente de --empreinte")
    c = chemin + ".sha256"
    mots = open(c, encoding="utf-8").read().split() if os.path.isfile(c) else []
    if not mots or mots[0] != empreinte:
        raise Refus("énoncé : compagnon .sha256 absent ou différent")
    texte = b.decode("utf-8")
    trouves = garde_motifs([("enonce", texte)])
    if trouves:
        raise Refus("garde de motifs non vide : " + " ; ".join(f"{t['motif']} (ligne {t['ligne']})" for t in trouves))
    return texte


def ligne_du_lot(texte):
    return {"custom_id": IDENT, "method": "POST", "url": "/v1/chat/completions",
            "body": {"model": MODELE, "messages": [{"role": "user", "content": texte}],
                     "max_completion_tokens": SORTIE_MAX, "reasoning_effort": EFFORT}}


def pire(ligne):
    return (D(len(json.dumps(ligne["body"]["messages"]).encode())) * TARIF[0] + D(SORTIE_MAX) * TARIF[1]) / D(10**6)


def verifier_go(registre):
    if not os.path.isfile(registre):
        raise Refus("registre de GO absent")
    t = open(registre, encoding="utf-8").read().split("\n")
    for g in GO_EXIGES:
        if not any(l.startswith("| " + g + " |") for l in t):
            raise Refus(f"{g} absent du registre")


def multipart(champs, nom_fichier, contenu):
    borne = "----lot" + uuid.uuid4().hex
    parts = []
    for k, v in champs.items():
        parts.append(f'--{borne}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    parts.append(f'--{borne}\r\nContent-Disposition: form-data; name="file"; filename="{nom_fichier}"\r\n'
                 f'Content-Type: application/jsonl\r\n\r\n'.encode() + contenu + b"\r\n")
    parts.append(f"--{borne}--\r\n".encode())
    return b"".join(parts), {"content-type": "multipart/form-data; boundary=" + borne}


def ecrire(journal, d):
    with open(journal, "a", encoding="utf-8") as f:
        f.write(json.dumps(dict(d, heure=heure()), ensure_ascii=False, sort_keys=True) + "\n")


def json_ou_refus(b, quoi):
    try:
        d = json.loads(b)
    except (json.JSONDecodeError, UnicodeDecodeError, TypeError):
        raise Refus(f"{quoi} : réponse non JSON")
    if not isinstance(d, dict):
        raise Refus(f"{quoi} : réponse JSON qui n'est pas un objet")
    return d


def id_ou_refus(d, quoi):
    i = d.get("id")
    if not isinstance(i, str) or not i:
        raise Refus(f"{quoi} : identifiant manquant")
    return i


def temoin(enonce):
    return enonce + ".soumis"


def soumission_du_journal(journal):
    if not os.path.isfile(journal):
        raise Refus("journal de soumission absent")
    lignes = []
    for l in open(journal, encoding="utf-8"):
        if l.strip():
            try:
                lignes.append(json.loads(l))
            except json.JSONDecodeError:
                raise Refus("journal illisible")
    s = [l for l in lignes if isinstance(l, dict) and l.get("type_ligne") == "soumission"]
    if len(s) != 1:
        raise Refus("journal : il faut exactement une ligne de soumission")
    return s[0]


def soumettre(cle, journal, transport, texte):
    ligne = ligne_du_lot(texte)
    p = pire(ligne)
    if p > PLAFOND_LOT:
        raise Refus(f"pire du lot {p} au-delà de {PLAFOND_LOT}")
    contenu = (json.dumps(ligne, ensure_ascii=False) + "\n").encode("utf-8")
    corps, ent = multipart({"purpose": "batch"}, "enonce-astra62.jsonl", contenu)
    st, b = transport("POST", "/v1/files", cle, corps, ent)
    if st != 200:
        raise Refus(f"téléversement refusé, statut {st}")
    fid = id_ou_refus(json_ou_refus(b, "téléversement"), "téléversement")
    st, b = transport("POST", "/v1/batches", cle, json.dumps({"input_file_id": fid, "endpoint": "/v1/chat/completions",
                                                              "completion_window": "24h"}).encode(),
                      {"content-type": "application/json"})
    if st != 200:
        raise Refus(f"création du lot refusée, statut {st}")
    lot = json_ou_refus(b, "création du lot")
    lid = id_ou_refus(lot, "création du lot")
    ecrire(journal, {"type_ligne": "soumission", "fichier_entree_id": fid, "lot_id": lid,
                     "statut": lot.get("status"), "entree_sha256": sha(contenu), "enonce_sha256": sha(texte.encode()),
                     "requetes": 1, "effort": EFFORT, "sortie_max": SORTIE_MAX,
                     "pire_usd": str(p.quantize(D("0.000001")))})
    return lid


def ecrire_neuf(chemin, contenu):
    with open(chemin, "xb") as f:
        f.write(contenu)
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{sha(contenu)}  {os.path.basename(chemin)}\n")
    return sha(contenu)


def relever(cle, lot_id, journal, sortie, transport, texte_enonce=None):
    if texte_enonce is not None:
        s = soumission_du_journal(journal)
        if s.get("lot_id") != lot_id:
            raise Refus("--lot différent du lot soumis inscrit au journal")
        if s.get("enonce_sha256") != sha(texte_enonce.encode()):
            raise Refus("énoncé différent de celui qui a été soumis")
    st, b = transport("GET", f"/v1/batches/{lot_id}", cle)
    if st != 200:
        raise Refus(f"lecture du lot refusée, statut {st}")
    lot = json_ou_refus(b, "lecture du lot")
    if lot.get("status") != "completed":
        ecrire(journal, {"type_ligne": "relève", "lot_id": lot_id, "statut": lot.get("status"),
                         "comptes": lot.get("request_counts")})
        return lot.get("status")
    if os.path.exists(sortie):
        raise Refus("dossier de sortie déjà présent : un dossier neuf par relève")
    os.makedirs(sortie)
    bruts = {}
    for champ in ("output_file_id", "error_file_id"):
        fid = lot.get(champ)
        if not fid:
            continue
        st, contenu = transport("GET", f"/v1/files/{fid}/content", cle)
        if st != 200:
            raise Refus(f"lecture de {champ} refusée, statut {st}")
        ecrire_neuf(os.path.join(sortie, f"astra62-lot-{champ}.jsonl"), contenu)
        bruts[champ] = contenu
    total = (lot.get("request_counts") or {}).get("total")
    try:
        lignes = [json.loads(l) for c in bruts.values() for l in c.decode("utf-8").split("\n") if l.strip()]
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise Refus("sortie du lot non JSON : brut versé, rien d'autre n'est inscrit")
    ids = [l.get("custom_id") for l in lignes]
    if len(lignes) != total or ids != [IDENT]:
        raise Refus("relève incohérente (nombre, doublon ou identifiant étranger) : rien n'est inscrit")
    l = lignes[0]
    corps = ((l.get("response") or {}).get("body") or {})
    u = corps.get("usage") or {}
    e, s = u.get("prompt_tokens"), u.get("completion_tokens")
    ch = (corps.get("choices") or [{}])[0]
    fin = ch.get("finish_reason")
    texte = (ch.get("message") or {}).get("content")
    servi = corps.get("model")
    servi_ok = isinstance(servi, str) and re.fullmatch(re.escape(MODELE) + r"(-[0-9.\-]{1,20})?", servi)
    c = (D(e) * TARIF[0] + D(s) * TARIF[1]) / D(10**6) if isinstance(e, int) and isinstance(s, int) else None
    complet = (fin == "stop" and bool(servi_ok) and isinstance(texte, str) and texte.strip() != ""
               and not l.get("error") and (l.get("response") or {}).get("status_code") == 200)
    h_texte = None
    if isinstance(texte, str) and texte:
        nom = "reponse-astra62-v1.md" if complet else "defaut-astra62-v1.md"
        h_texte = ecrire_neuf(os.path.join(sortie, nom), texte.encode("utf-8"))
    ecrire(journal, {"type_ligne": "réponse", "custom_id": IDENT,
                     "statut_http": (l.get("response") or {}).get("status_code"),
                     "fin": fin if fin in FINS else ("absente" if fin is None else "autre"),
                     "modele_servi": servi if servi_ok else "autre", "entree_jetons": e, "sortie_jetons": s,
                     "verdict": "reponse" if complet else "defaut", "texte_sha256": h_texte,
                     "cout_usd": str(c.quantize(D("0.000001"))) if c is not None else "inconnu",
                     "erreur": bool(l.get("error"))})
    ecrire(journal, {"type_ligne": "fin", "lot_id": lot_id,
                     "cout_total_usd": str(c.quantize(D("0.000001"))) if c is not None else "inconnu"})
    return "completed" if complet else "defaut"


def main(argv=None, transport=transport_reel):
    a = argparse.ArgumentParser()
    a.add_argument("action", choices=("a_blanc", "soumettre", "relever"))
    a.add_argument("--enonce", required=True)
    a.add_argument("--empreinte", required=True)
    a.add_argument("--journal")
    a.add_argument("--sortie")
    a.add_argument("--lot")
    a.add_argument("--registre-go")
    o = a.parse_args(argv)
    try:
        texte = lire_enonce(o.enonce, o.empreinte)
        if o.action == "a_blanc":
            print(json.dumps({"a_blanc": "conforme", "requetes": 1,
                              "pire_usd": str(pire(ligne_du_lot(texte)).quantize(D("0.01")))}))
            return 0
        if not o.journal or not o.registre_go:
            raise Refus("--journal et --registre-go exigés")
        verifier_go(o.registre_go)
        cle = os.environ.get("OPENAI_API_KEY_2", "")
        if not cle.strip():
            raise Refus("clé OPENAI_API_KEY_2 absente")
        if o.action == "soumettre":
            if os.path.exists(o.journal):
                raise Refus("journal déjà présent")
            try:
                with open(temoin(o.enonce), "x", encoding="utf-8") as f:
                    f.write(heure() + "\n")
            except FileExistsError:
                raise Refus("énoncé déjà soumis (témoin présent) : une seule soumission par énoncé")
            print(json.dumps({"lot": soumettre(cle, o.journal, transport, texte)}))
        else:
            if not o.lot or not o.sortie:
                raise Refus("--lot et --sortie exigés")
            print(json.dumps({"statut": relever(cle, o.lot, o.journal, o.sortie, transport, texte)}))
    except Refus as e:
        print("REFUS :", e, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
