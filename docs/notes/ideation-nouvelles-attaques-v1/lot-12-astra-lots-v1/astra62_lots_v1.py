"""Lot 12 — Astra 6.2 par l'interface par lots d'OpenAI — v1 (copie d'astra_lots_v1.py, seuls le modèle et le
préfixe des identifiants changent ; mot de Lazar « go Astra 6.2 », 14:09Z).

Sert les trois textes de groupe de la passe X (passe-x-textes-groupes-v1, scellés) à gpt-6-astra par un lot unique
(fichier JSONL téléversé, `POST /v1/files` purpose=batch, puis `POST /v1/batches`, fenêtre 24 h), d'après le mode
d'emploi de la session « Raisons ou regard ? » (module de lots, commit 4c23460, `LotsCompatibles`), sans le reprendre.
Aucun flux à tenir ouvert : la coupure à 300 secondes du groupe 1 ne peut pas se reproduire.

Gardes :
- textes vérifiés par empreinte (EMPREINTES_TEXTES du lot 11 v4) ; message unique de rôle « user », aucun message
  système ni « developer » ; `reasoning_effort` « xhigh » (le plus haut admis selon la session source) ;
- lignes de GO présentes (GO-2026-11-22-46) ; clé lue par son nom ; aucune redirection suivie ;
- pire calculé au tarif des lots (5 / 20 USD le million) : ≤ 14,67 USD pour le lot entier, refus au-delà ;
- relève : nombre de lignes égal à `request_counts.total`, `custom_id` uniques et attendus, rattachement par `custom_id`
  jamais par rang ; sinon arrêt sans rien inscrire ;
- la sortie brute et le fichier d'erreurs vont tels quels dans un fichier neuf de la quarantaine, jamais affichés ;
  le journal ne porte que des comptes, des classes en liste fermée et des empreintes.
"""
import argparse, datetime, hashlib, importlib.util, json, os, re, sys, urllib.error, urllib.request, uuid
from decimal import Decimal as D

BASE = "https://api.openai.com"
MODELE = "gpt-6.2-astra"
EFFORT = "xhigh"
SORTIE_MAX = 96000
TARIF = (D(5), D(20))  # lots : moitié prix
PLAFOND_LOT = D("14.67")
GO_EXIGES = ("GO-2026-11-22-46",)
TEXTES = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/passe-x-textes-groupes-v1/textes"
LOT11 = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/lot-11-passe-x-v4/passe_x_na_v4.py"
GROUPES = ("groupe-1", "groupe-2", "groupe-3")
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


def charger_empreintes():
    b = open(LOT11, "rb").read()
    if open(LOT11 + ".sha256").read().split()[0] != sha(b):
        raise Refus("module du lot 11 v4 différent de son compagnon")
    s = importlib.util.spec_from_file_location("lot11", LOT11); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.EMPREINTES_TEXTES


def lignes_du_lot(dossier=TEXTES):
    emp = charger_empreintes()
    out = []
    for g in GROUPES:
        b = open(os.path.join(dossier, g + ".md"), "rb").read()
        if sha(b) != emp[g]:
            raise Refus(f"empreinte de {g} différente de celle qui est scellée")
        out.append({"custom_id": "astra62-" + g, "method": "POST", "url": "/v1/chat/completions",
                    "body": {"model": MODELE, "messages": [{"role": "user", "content": b.decode("utf-8")}],
                             "max_completion_tokens": SORTIE_MAX, "reasoning_effort": EFFORT}})
    return out


def pire(lignes):
    return sum((D(len(json.dumps(l["body"]["messages"]).encode())) * TARIF[0] + D(SORTIE_MAX) * TARIF[1]) / D(10**6)
               for l in lignes)


def verifier_go(registre):
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


def soumettre(cle, journal, transport, dossier=TEXTES):
    lignes = lignes_du_lot(dossier)
    p = pire(lignes)
    if p > PLAFOND_LOT:
        raise Refus(f"pire du lot {p} au-delà de {PLAFOND_LOT}")
    contenu = ("\n".join(json.dumps(l, ensure_ascii=False) for l in lignes) + "\n").encode("utf-8")
    corps, ent = multipart({"purpose": "batch"}, "passe-x-astra62.jsonl", contenu)
    st, b = transport("POST", "/v1/files", cle, corps, ent)
    if st != 200:
        raise Refus(f"téléversement refusé, statut {st}")
    fid = json.loads(b)["id"]
    st, b = transport("POST", "/v1/batches", cle, json.dumps({"input_file_id": fid, "endpoint": "/v1/chat/completions",
                                                              "completion_window": "24h"}).encode(),
                      {"content-type": "application/json"})
    if st != 200:
        raise Refus(f"création du lot refusée, statut {st}")
    lot = json.loads(b)
    ecrire(journal, {"type_ligne": "soumission", "fichier_entree_id": fid, "lot_id": lot["id"], "statut": lot.get("status"),
                     "entree_sha256": sha(contenu), "requetes": len(lignes), "pire_usd": str(p.quantize(D("0.000001")))})
    return lot["id"]


def relever(cle, lot_id, journal, quarantaine, transport):
    st, b = transport("GET", f"/v1/batches/{lot_id}", cle)
    if st != 200:
        raise Refus(f"lecture du lot refusée, statut {st}")
    lot = json.loads(b)
    if lot.get("status") != "completed":
        ecrire(journal, {"type_ligne": "relève", "lot_id": lot_id, "statut": lot.get("status"),
                         "comptes": lot.get("request_counts")})
        return lot.get("status")
    os.makedirs(quarantaine, exist_ok=True)
    bilan = {}
    for champ in ("output_file_id", "error_file_id"):
        fid = lot.get(champ)
        if not fid:
            continue
        st, contenu = transport("GET", f"/v1/files/{fid}/content", cle)
        if st != 200:
            raise Refus(f"lecture de {champ} refusée, statut {st}")
        chemin = os.path.join(quarantaine, f"astra62-lot-{champ}.jsonl")
        with open(chemin, "xb") as f:
            f.write(contenu)
        with open(chemin + ".sha256", "x") as f:
            f.write(f"{sha(contenu)}  {os.path.basename(chemin)}\n")
        bilan[champ] = contenu
    total = (lot.get("request_counts") or {}).get("total")
    lignes = [json.loads(l) for c in bilan.values() for l in c.decode("utf-8").split("\n") if l.strip()]
    ids = [l.get("custom_id") for l in lignes]
    if len(lignes) != total or len(set(ids)) != len(ids) or set(ids) != {"astra62-" + g for g in GROUPES}:
        raise Refus("relève incohérente (nombre, doublon ou identifiant étranger) : rien n'est inscrit")
    cout = D(0)
    for l in lignes:
        corps = ((l.get("response") or {}).get("body") or {})
        u = corps.get("usage") or {}
        e, s = u.get("prompt_tokens"), u.get("completion_tokens")
        ch = (corps.get("choices") or [{}])[0]
        fin = ch.get("finish_reason")
        c = (D(e) * TARIF[0] + D(s) * TARIF[1]) / D(10**6) if isinstance(e, int) and isinstance(s, int) else None
        cout += c or D(0)
        servi = corps.get("model")
        ecrire(journal, {"type_ligne": "réponse", "custom_id": l["custom_id"],
                         "statut_http": (l.get("response") or {}).get("status_code"),
                         "fin": fin if fin in FINS else ("absente" if fin is None else "autre"),
                         "modele_servi": servi if isinstance(servi, str) and re.fullmatch(re.escape(MODELE) + r"(-[0-9.\-]{1,20})?", servi) else "autre",
                         "entree_jetons": e, "sortie_jetons": s,
                         "cout_usd": str(c.quantize(D("0.000001"))) if c is not None else "inconnu",
                         "erreur": bool(l.get("error"))})
    ecrire(journal, {"type_ligne": "fin", "lot_id": lot_id, "cout_total_usd": str(cout.quantize(D("0.000001")))})
    return "completed"


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("action", choices=("a_blanc", "soumettre", "relever"))
    a.add_argument("--journal", required=True)
    a.add_argument("--quarantaine")
    a.add_argument("--lot")
    a.add_argument("--registre-go", default="/home/user/main-lecture/registres/go.md")
    o = a.parse_args(argv)
    try:
        if o.action == "a_blanc":
            l = lignes_du_lot()
            print(json.dumps({"a_blanc": "conforme", "requetes": len(l), "pire_usd": str(pire(l).quantize(D("0.01")))}))
            return 0
        verifier_go(o.registre_go)
        cle = os.environ.get("OPENAI_API_KEY_2", "")
        if not cle.strip():
            raise Refus("clé OPENAI_API_KEY_2 absente")
        if o.action == "soumettre":
            if os.path.exists(o.journal):
                raise Refus("journal déjà présent")
            print(json.dumps({"lot": soumettre(cle, o.journal, transport_reel)}))
        else:
            print(json.dumps({"statut": relever(cle, o.lot, o.journal, o.quarantaine, transport_reel)}))
    except Refus as e:
        print("REFUS :", e, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
