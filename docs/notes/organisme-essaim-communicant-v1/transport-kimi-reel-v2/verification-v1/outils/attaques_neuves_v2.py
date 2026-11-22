#!/usr/bin/env python3
"""Artefacts neufs sur le transport Kimi v2 : serveurs locaux 127.0.0.1, clé factice. Usage : python -I -B ce_fichier SORTIE"""
import json, os, sys, tempfile, importlib.util
PIECE = "/home/user/controle-ia-travail/docs/notes/organisme-essaim-communicant-v1/transport-kimi-reel-v2"
V4 = "/home/user/controle-ia-travail/docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v4"
sys.path[:0] = [PIECE, V4]
# réemploi du serveur brut de mon outil v1 (lu par chemin, sans l'exécuter en entier)
src = open("/tmp/claude-0/-home-user-controle-ia-travail/e2c3ce0b-40f3-55d3-a6bf-333c05f6ccd1/scratchpad/contre-lecture-transport-kimi-v1/outils/attaques_transport_kimi_cl_v1.py").read()
debut, fin = src.index("# --- serveur brut"), src.index("# --- N1 ")
import adaptateur_fournisseur_v1 as A
import adaptateur_kimi_strict_v2 as AS
import essai_fumee_kimi_v2 as EF
import faux_serveur_kimi_v2 as FS
import transport_kimi_reel_v2 as T
ns = {"__name__": "brut"}
exec("import json, socket, socketserver, threading, time\nCLE='sk-CLEFACTICE-contre-lecture-0123456789abcdefXYZ'\nM='kimi-k3.1-pro'\n" + src[debut:fin], ns)
Brut, sse, us, ch, CLE, M = ns["Brut"], ns["sse"], ns["us"], ns["ch"], ns["CLE"], ns["M"]
RES = {}
def appel(url, mt=2000, **kw):
    tr = T.TransportKimiReel(amont=url, environ={"KIMI_API_KEY": CLE}, delai_silence_s=5, delai_total_s=20, **kw)
    try:
        ad = AS.AdaptateurKimiStrict(tr)
        return ad.appeler({"id": "x"}, "Bonjour.", mt), tr, None
    except Exception as ex:
        return None, tr, ex
def note(n, **kw):
    RES[n] = kw; print(n, json.dumps(kw, ensure_ascii=False, default=str)[:420])
en = lambda ex: None if ex is None else f"{type(ex).__name__}: {ex}"

# N21 usage au niveau du choix, dans le dernier morceau (ancienne forme Moonshot)
s = Brut(lambda k, c: sse(ch(rais="r"), ch("OK", fin="stop"), {"id": "i", "model": M, "choices": [{"index": 0, "delta": {}, "usage": us()}]}, b"[DONE]"))
r, tr, ex = appel(s.url); d = tr.dernier_diagnostic or {}
note("N21_usage_dans_choices_du_dernier_morceau", issue=en(ex), usage=None if r is None else r["usage"], refus=d.get("usage_refuse")); s.fin()

# N22 max_tokens 16, 17 deltas d'un caractère (amont qui découpe sous le jeton) : fausse coupure ?
s = Brut(lambda k, c: sse(*[ch(rais="a") for _ in range(17)], ch(fin="length"), ch(choix=False, usage=us(c=16, r=16)), b"[DONE]"))
r, tr, ex = appel(s.url, mt=16)
note("N22_fausse_coupure_17_deltas_pour_16_jetons", issue=en(ex), usage=None if r is None else r["usage"]); s.fin()

# N23 commentaire de maintien entre l'usage et [DONE]
s = Brut(lambda k, c: [ns["sse"](ch("OK", fin="stop"), ch(choix=False, usage=us()))[0][:-0 or None]])
corps = b"data: " + json.dumps(ch("OK", fin="stop")).encode() + b"\n\ndata: " + json.dumps(ch(choix=False, usage=us())).encode() + b"\n\n: ping\n\ndata: [DONE]\n\n"
s.fin()
s = Brut(lambda k, c: [b"HTTP/1.1 200 OK\r\nContent-Type: text/event-stream\r\nContent-Length: " + str(len(corps)).encode() + b"\r\nConnection: close\r\n\r\n" + corps])
r, tr, ex = appel(s.url)
note("N23_maintien_apres_usage", issue=en(ex), usage=None if r is None else r["usage"], refus=(tr.dernier_diagnostic or {}).get("usage_refuse")); s.fin()

# N24 corps : deux champs, un seul, champ inconnu
with FS.FauxServeurKimi() as srv:
    out = {}
    for cm in (("max_tokens", "max_completion_tokens"), ("max_completion_tokens",), ("max_tokens",), ("n",), ()):
        try:
            tr = T.TransportKimiReel(amont=srv.url, environ={"KIMI_API_KEY": CLE}, champs_max=cm)
            AS.AdaptateurKimiStrict(tr).appeler({"id": "x"}, "Bonjour.", 777)
            b = json.loads(srv.requetes[-1][3]); out[",".join(cm) or "vide"] = {k: b[k] for k in b if "max" in k}
        except Exception as ex:
            out[",".join(cm) or "vide"] = en(ex)
note("N24_champs_max", resultats=out, requetes=srv.nombre)

# N25 clé renvoyée dans un en-tête x-request-id
s = Brut(lambda k, c: sse(ch("OK", fin="stop"), ch(choix=False, usage=us()), b"[DONE]", extra=b"X-Request-Id: " + CLE.encode() + b"\r\n"))
r, tr, ex = appel(s.url); d = tr.dernier_diagnostic or {}
note("N25_cle_dans_en_tete_request_id", issue=en(ex), en_tetes_id=d.get("en_tetes_id"), fuite=CLE[:8] in json.dumps(d, default=str)); s.fin()

# N26 fumée à blanc : 500 sur f1 → arrêt 13 ; journal sans clé ni texte ; f2 garde le détail
def regle(k, corps):
    return {"completion": 16, "raisonnement": 13} if k == 0 else ({"statut": 500} if k == 1 else {})
with tempfile.TemporaryDirectory() as dd, FS.FauxServeurKimi(regle) as srv:
    code = EF.courir(os.path.join(dd, "r.jsonl"), os.path.join(dd, "j.jsonl"), srv.url, 1.0, environ={"KIMI_API_KEY": CLE})
    txt = open(os.path.join(dd, "j.jsonl"), encoding="utf-8").read()
    L = [json.loads(x) for x in txt.splitlines()]
    ap = [x for x in L if x["evenement"] == "appel"]
    note("N26_fumee_500_sur_f1", code=code, requetes=srv.nombre, f2_usage_brut=ap[0]["diagnostic"]["usage_brut"],
         f2_H2=ap[0]["verifications"].get("H2_tenue_sous_reserve_console"), arret=L[-1], cle_au_journal=CLE[:8] in txt, texte_au_journal="Démontre" in txt)
json.dump(RES, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
