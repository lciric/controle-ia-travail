#!/usr/bin/env python3
"""REJEU SUR LA V3 de l'outil du contre-lecteur `attaques_transport_kimi_cl_v1.py` (sha256 dans son compagnon), avec ces
seuls changements :
1. modules v3 importés (transport, adaptateur strict, essai de fumée, faux serveur) et chemin de la pièce ;
2. N13 : l'affectation de `tr._p` est placée dans un `try` (la v2 et la v3 la refusent ; l'attaque passe alors par
   `object.__setattr__`) ;
3. `appel` : la construction de l'adaptateur strict est dans le `try` (il peut refuser dès la construction) ;
4. **N19 réécrit** : le journal de la fumée a changé de forme (B1) et f2 passe en premier. La note de N19 relève donc les
   champs de la v2/v3 (issue par appel, `usage_brut`, motif, ligne d'arrêt), et un second passage N19b, aux règles décalées,
   atteint f3 pour éprouver l'arrêt sur un coût mesuré au-delà de la réserve. Les règles du faux serveur de N19 sont
   inchangées.
Texte d'origine :
Contre-lecture du transport Kimi réel v1 : attaques neuves, toutes contre des serveurs locaux (127.0.0.x), clé factice.
Aucun réseau sortant. Usage : python -I -B attaques_transport_kimi_cl_v1.py SORTIE_JSON"""
import contextlib
import http.client
import io
import json
import os
import socket
import socketserver
import sys
import tempfile
import threading
import time
import urllib.parse

PIECE = os.path.dirname(os.path.abspath(__file__))
V4 = "/home/user/controle-ia-travail/docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v4"
sys.path[:0] = [PIECE, V4]
import adaptateur_fournisseur_v1 as A  # noqa: E402
import adaptateur_kimi_strict_v3 as AS  # noqa: E402
import essai_fumee_kimi_v3 as EF  # noqa: E402
import faux_serveur_kimi_v3 as FS  # noqa: E402
import transport_kimi_reel_v3 as T  # noqa: E402

CLE = "sk-CLEFACTICE-contre-lecture-0123456789abcdefXYZ"
M = T.MODELE
RES = {}


# --- serveur brut : réponse octet par octet ---------------------------------------------------------------------------
class Brut:
    def __init__(self, regle, hote="127.0.0.1"):
        self.regle, self.req = regle, []
        moi = self

        class H(socketserver.BaseRequestHandler):
            def handle(self):
                f = self.request.makefile("rb")
                tete = b""
                while not tete.endswith(b"\r\n\r\n"):
                    o = f.readline()
                    if not o:
                        return
                    tete += o
                lignes = tete.decode("latin-1").split("\r\n")
                hd = {}
                for l in lignes[1:]:
                    if ":" in l:
                        k, v = l.split(":", 1)
                        hd[k.strip().lower()] = v.strip()
                corps = f.read(int(hd.get("content-length", 0) or 0))
                k = len(moi.req)
                moi.req.append({"ligne": lignes[0], "port": self.client_address[1], "en_tetes": hd, "corps": corps})
                for morceau in moi.regle(k, corps):
                    if morceau is None:
                        self.request.shutdown(socket.SHUT_RDWR)
                        return
                    if isinstance(morceau, float):
                        time.sleep(morceau)
                        continue
                    try:
                        self.request.sendall(morceau)
                    except OSError:
                        return

        socketserver.ThreadingTCPServer.allow_reuse_address = True
        self.s = socketserver.ThreadingTCPServer((hote, 0), H)
        self.s.daemon_threads = True
        self.url = f"http://{hote}:{self.s.server_address[1]}"
        threading.Thread(target=self.s.serve_forever, daemon=True).start()

    def fin(self):
        self.s.shutdown()
        self.s.server_close()


def sse(*evts, statut=b"200 OK", ctype=b"text/event-stream", extra=b""):
    corps = b"".join(b"data: " + (e if isinstance(e, bytes) else json.dumps(e).encode()) + b"\n\n" for e in evts)
    return [b"HTTP/1.1 " + statut + b"\r\nContent-Type: " + ctype + b"\r\nContent-Length: " + str(len(corps)).encode()
            + b"\r\nConnection: close\r\n" + extra + b"\r\n" + corps]


def us(p=20, c=50, r=30, t=None, **kw):
    u = {"prompt_tokens": p, "completion_tokens": c, "total_tokens": p + c if t is None else t,
         "completion_tokens_details": {"reasoning_tokens": r}}
    u.update(kw)
    return u


def ch(contenu=None, rais=None, fin=None, model=M, usage=None, choix=True):
    d = {}
    if contenu is not None:
        d["content"] = contenu
    if rais is not None:
        d["reasoning_content"] = rais
    e = {"id": "chatcmpl-cl", "object": "chat.completion.chunk", "model": model,
         "choices": [{"index": 0, "delta": d, "finish_reason": fin}] if choix else []}
    if usage is not None:
        e["usage"] = usage
    return e


def tr_sur(url, **kw):
    kw.setdefault("delai_silence_s", 5)
    kw.setdefault("delai_total_s", 20)
    return T.TransportKimiReel(amont=url, environ={"KIMI_API_KEY": CLE}, **kw)


def appel(url, texte="Bonjour.", mt=2000, **kw):
    tr = tr_sur(url, **kw)
    try:
        ad = AS.AdaptateurKimiStrict(tr)  # rejeu v2 : construction dans le try (la v2 peut refuser dès la construction)
        return ad.appeler({"id": "x"}, texte, mt), tr, None
    except Exception as ex:  # noqa: BLE001
        return None, tr, ex


def note(nom, **kw):
    RES[nom] = kw
    print(nom, json.dumps(kw, ensure_ascii=False, default=str)[:400])


def ex_nom(ex):
    return None if ex is None else f"{type(ex).__name__}: {ex}"


# --- N1 redirection 307 vers un autre hôte -----------------------------------------------------------------------------
autre = Brut(lambda k, c: sse(ch("x", fin="stop"), ch(choix=False, usage=us()), b"[DONE]"), hote="127.0.0.3")
red = Brut(lambda k, c: [b"HTTP/1.1 307 Temporary Redirect\r\nLocation: " + autre.url.encode() + b"/v1/chat/completions\r\n"
                         b"Content-Length: 0\r\nConnection: close\r\n\r\n"])
r, tr, ex = appel(red.url)
note("N1_redirection_307", issue=ex_nom(ex), requetes_origine=len(red.req), requetes_autre_hote=len(autre.req),
     attendu="ErreurTransportFatale, 1 requête, 0 vers l'autre hôte")
red.fin()

# --- N2 429 avec Retry-After ------------------------------------------------------------------------------------------
s = Brut(lambda k, c: [b"HTTP/1.1 429 Too Many Requests\r\nRetry-After: 30\r\nContent-Type: application/json\r\n"
                       b"Content-Length: 2\r\nConnection: close\r\n\r\n{}"])
t0 = time.monotonic()
r, tr, ex = appel(s.url)
note("N2_429_retry_after", issue=ex_nom(ex), requetes=len(s.req), duree_s=round(time.monotonic() - t0, 2),
     attendu="ErreurFournisseur immédiate, 1 requête, aucune attente")
s.fin()

# --- N3 réutilisation de connexion : deux appels sur un même transport -------------------------------------------------
s = Brut(lambda k, c: sse(ch("OK", fin="stop"), ch(choix=False, usage=us()), b"[DONE]", extra=b""))
tr = tr_sur(s.url)
ad = AS.AdaptateurKimiStrict(tr)
ad.appeler({"id": "a"}, "Bonjour.", 2000)
ad.appeler({"id": "b"}, "Bonjour.", 2000)
note("N3_connexion_neuve", ports_client=[q["port"] for q in s.req], requetes=len(s.req), envois=tr.envois,
     attendu="2 ports distincts, 2 requêtes, 2 envois mesurés")
s.fin()

# --- N4 Content-Type flux mais corps JSON entier -----------------------------------------------------------------------
corps = json.dumps({"model": M, "choices": [{"message": {"content": "OK"}, "finish_reason": "stop"}], "usage": us()}).encode()
s = Brut(lambda k, c: [b"HTTP/1.1 200 OK\r\nContent-Type: text/event-stream\r\nContent-Length: " + str(len(corps)).encode()
                       + b"\r\nConnection: close\r\n\r\n" + corps])
r, tr, ex = appel(s.url)
note("N4_flux_annonce_corps_json", issue=ex_nom(ex), requetes=len(s.req), attendu="ErreurFournisseur (pas de [DONE]), 1 requête")
s.fin()

# --- N5 usage dans un morceau intermédiaire seulement, contenu qui suit -----------------------------------------------
contenu_suivant = "mot " * 150  # 600 octets, sous 12 × (40 + 0)… ajusté plus bas
s = Brut(lambda k, c: sse(ch(rais="je pense"), ch("debut", usage=us(c=60, r=10)), ch(contenu_suivant), ch("fin", fin="stop"),
                          b"[DONE]"))
r, tr, ex = appel(s.url)
note("N5_usage_intermediaire_puis_contenu", issue=ex_nom(ex), usage_rendu=None if r is None else r["usage"],
     octets_contenu=len(contenu_suivant) + 8, place=(tr.dernier_diagnostic or {}).get("usage_place"),
     constat="usage pris d'un morceau qui n'est pas le dernier ; la doc (api_chat.md l. 216, 1176-1183) dit que l'usage vient "
             "seul dans le dernier morceau, choices vide, et null ailleurs")
s.fin()

# --- N6 deux usages : le premier grand, le second petit -----------------------------------------------------------------
s = Brut(lambda k, c: sse(ch(rais="r"), ch("OK", fin="stop"), ch(choix=False, usage=us(c=1900, r=1800)),
                          ch(choix=False, usage=us(c=5, r=2)), b"[DONE]"))
r, tr, ex = appel(s.url)
note("N6_deux_usages", issue=ex_nom(ex), usage_rendu=None if r is None else r["usage"],
     constat="le dernier usage gagne, sans comparaison : sous-compte possible de 1895 jetons de sortie")
s.fin()

# --- N7 réflexion facturée hors reasoning_tokens -----------------------------------------------------------------------
s = Brut(lambda k, c: sse(ch(rais="r"), ch("OK", fin="stop"),
                          ch(choix=False, usage=us(c=10, r=5, completion_tokens_details={"reasoning_tokens": 5, "thinking_tokens": 1500},
                                                   output_tokens=1510)), b"[DONE]"))
r, tr, ex = appel(s.url)
note("N7a_reflexion_champ_inconnu_total_exact", issue=ex_nom(ex), usage_rendu=None if r is None else r["usage"],
     constat="champ inconnu ignoré, total_tokens cohérent : invisible au client (limite déclarée § 6)")
s.fin()
s = Brut(lambda k, c: sse(ch(rais="r"), ch("OK", fin="stop"),
                          ch(choix=False, usage=us(c=10, r=5, t=30 + 1500)), b"[DONE]"))
r, tr, ex = appel(s.url)
note("N7b_reflexion_dans_total_seulement", issue=ex_nom(ex), usage_rendu=None if r is None else r["usage"],
     attendu="excédent ajouté (reasoning_tokens premier niveau)")
s.fin()

# --- N8 modèle servi différent seulement dans le dernier morceau (celui de l'usage) ---------------------------------------
s = Brut(lambda k, c: sse(ch(rais="r"), ch("OK", fin="stop"), ch(choix=False, usage=us(), model="kimi-k3"), b"[DONE]"))
r, tr, ex = appel(s.url)
note("N8_modele_autre_au_dernier_morceau", issue=ex_nom(ex), requetes=len(s.req), attendu="AnomalieReponse")
s.fin()
s = Brut(lambda k, c: sse(ch(rais="r"), ch("OK", fin="stop", model=None), ch(choix=False, usage=us()), b"[DONE]"))
r, tr, ex = appel(s.url)
note("N8b_modele_null_en_cours", issue=ex_nom(ex), modele=None if r is None else r.get("model"),
     constat="model null au milieu toléré (sans effet tant que les autres morceaux le portent)")
s.fin()

# --- N9 corps trop gros : une ligne de 2 Mo ; flux infini de petites lignes -------------------------------------------------
gros = b"data: " + json.dumps(ch("y" * 2_000_000)).encode() + b"\n\n"
s = Brut(lambda k, c: [b"HTTP/1.1 200 OK\r\nContent-Type: text/event-stream\r\nConnection: close\r\n\r\n", gros, None])
r, tr, ex = appel(s.url)
note("N9a_ligne_de_2_Mo", issue=ex_nom(ex), attendu="AnomalieReponse (morceau illisible) ou ErreurFournisseur")
s.fin()


def infini(k, c):
    yield b"HTTP/1.1 200 OK\r\nContent-Type: text/event-stream\r\nConnection: close\r\n\r\n"
    yield b"data: " + json.dumps(ch(rais="r")).encode() + b"\n\n"
    for _ in range(4000):
        yield b"data: " + json.dumps(ch("z" * 400)).encode() + b"\n\n"
    yield None


s = Brut(infini)
r, tr, ex = appel(s.url, taille_max_octets=200_000)
note("N9b_flux_sans_fin_au_dela_de_la_taille", issue=ex_nom(ex), octets_lus=(tr.dernier_diagnostic or {}).get("octets_reponse"),
     attendu="AnomalieReponse dès 200 000 octets")
s.fin()

# --- N10 sortie au-delà de max_tokens en flux : aucune coupure côté client avant la fin -----------------------------------
def long_flux(k, c):
    yield b"HTTP/1.1 200 OK\r\nContent-Type: text/event-stream\r\nConnection: close\r\n\r\n"
    yield b"data: " + json.dumps(ch(rais="r")).encode() + b"\n\n"
    for _ in range(600):
        yield b"data: " + json.dumps(ch("abcd " * 100)).encode() + b"\n\n"  # 500 octets ≈ 100 à 125 jetons par morceau
    yield b"data: " + json.dumps(ch(fin="length")).encode() + b"\n\n"
    yield b"data: " + json.dumps(ch(choix=False, usage=us(c=16, r=10))).encode() + b"\n\n"
    yield b"data: [DONE]\n\n"


s = Brut(long_flux)
r, tr, ex = appel(s.url, mt=16)
d = tr.dernier_diagnostic or {}
note("N10_max_tokens_ignore_par_l_amont", issue=ex_nom(ex), octets_lus=d.get("octets_reponse"), usage=None if r is None else r["usage"],
     refus=d.get("usage_refuse"),
     constat="300 ko lus jusqu'au bout pour max_tokens = 16 ; aucune coupure en cours de flux ; l'usage est refusé à la fin "
             "(réserve), mais l'amont aurait facturé ≈ 60 000 jetons")
s.fin()

# --- N11 clé renvoyée par l'amont dans id, model, code d'erreur ---------------------------------------------------------
s = Brut(lambda k, c: sse({"id": "chatcmpl-" + CLE, "object": "chat.completion.chunk", "model": M,
                           "choices": [{"index": 0, "delta": {"content": "OK"}, "finish_reason": "stop"}]},
                          ch(choix=False, usage=us()), b"[DONE]"))
r, tr, ex = appel(s.url)
d = tr.dernier_diagnostic or {}
note("N11a_cle_dans_id", fuite_dans_id_reponse=CLE[:30] in str(d.get("id_reponse")), id_reponse=str(d.get("id_reponse"))[:20] + "…")
s.fin()
s = Brut(lambda k, c: sse({"id": "x", "object": "chat.completion.chunk", "model": "autre-" + CLE, "choices": []}, b"[DONE]"))
r, tr, ex = appel(s.url)
d = tr.dernier_diagnostic or {}
note("N11b_cle_dans_model_servi", fuite_diag=CLE[:30] in str(d.get("modele_servi")), fuite_exception=CLE[:30] in str(ex))
s.fin()
e_code = {"error": {"type": "invalid_request_error", "code": "x" * 50 + CLE}}
b = json.dumps(e_code).encode()
s = Brut(lambda k, c: [b"HTTP/1.1 401 Unauthorized\r\nContent-Type: application/json\r\nContent-Length: " + str(len(b)).encode()
                       + b"\r\nConnection: close\r\n\r\n" + b])
r, tr, ex = appel(s.url)
morceau_cle = CLE[:12]
note("N11c_cle_tronquee_dans_le_code_d_erreur", issue=type(ex).__name__, cle_entiere=CLE in str(ex),
     prefixe_de_cle_present=morceau_cle in str(ex), longueur_prefixe=len(str(ex).split("x" * 50)[-1].split(")")[0]) if "x" * 50 in str(ex) else 0,
     constat="_court tronque à 80 avant _masquer : la clé coupée n'est plus reconnue")
s.fin()

# --- N12 debuglevel de http.client : la clé part sur la sortie standard ----------------------------------------------------
s = Brut(lambda k, c: sse(ch("OK", fin="stop"), ch(choix=False, usage=us()), b"[DONE]"))
tampon = io.StringIO()
ancien = http.client.HTTPConnection.debuglevel
http.client.HTTPConnection.debuglevel = 1
try:
    with contextlib.redirect_stdout(tampon):
        r, tr, ex = appel(s.url)
finally:
    http.client.HTTPConnection.debuglevel = ancien
note("N12_debuglevel_global", issue=ex_nom(ex), cle_sur_stdout=CLE in tampon.getvalue(),
     constat="l'adaptateur strict ne vérifie pas debuglevel ; set_debuglevel(0) explicite manque")
s.fin()

# --- N13 amont réécrit après construction : clé envoyée en clair hors de la boucle admise ---------------------------------
s = Brut(lambda k, c: sse(ch("OK", fin="stop"), ch(choix=False, usage=us()), b"[DONE]"), hote="127.0.0.2")
try:
    T.TransportKimiReel(amont=s.url, environ={"KIMI_API_KEY": CLE})
    refuse_init = False
except A.ConfigurationRefusee:
    refuse_init = True
with FS.FauxServeurKimi() as srv:
    tr = tr_sur(srv.url)
    ad = AS.AdaptateurKimiStrict(tr)
    try:
        try:
            tr._p = urllib.parse.urlsplit(s.url)  # v2 : refusé (configuration figée)
            affectation = "acceptée"
        except A.ConfigurationRefusee:
            affectation = "refusée"
            object.__setattr__(tr, "_p", urllib.parse.urlsplit(s.url))  # contournement par object.__setattr__
        RES["N13_affectation_directe"] = affectation
        ad.appeler({"id": "x"}, "Bonjour.", 2000)
        ex = None
    except Exception as e:  # noqa: BLE001
        ex = e
note("N13_amont_reecrit_apres_construction", refuse_a_la_construction=refuse_init, issue=ex_nom(ex),
     requetes_hote_non_admis=len(s.req), cle_recue_en_clair=bool(s.req) and CLE in s.req[0]["en_tetes"].get("authorization", ""),
     constat="_p, _tls, _mandataire, taille_max, plafond_max_tokens, noms_interdits : mutables, jamais revérifiés")
s.fin()

# --- N14 constante MODELE du module réécrite ------------------------------------------------------------------------------
with FS.FauxServeurKimi() as srv:
    ancien = T.MODELE
    T.MODELE = "kimi-k3.1-pro-highspeed"
    try:
        tr = tr_sur(srv.url)
        ad = AS.AdaptateurKimiStrict(tr, modele="kimi-k3.1-pro-highspeed")
        rep = ad.appeler({"id": "x"}, "Bonjour.", 2000)
        envoye = json.loads(srv.requetes[-1][3])["model"]
        ex = None
    except Exception as e:  # noqa: BLE001
        envoye, ex = None, e
    finally:
        T.MODELE = ancien
note("N14_constante_MODELE_reecrite", issue=ex_nom(ex), modele_envoye=envoye,
     constat="globales du module (MODELE, _entier, OCTETS_PAR_JETON_SORTIE_MAX, MOTIFS_INTERDITS…) non figées")

# --- N15 relance cachée sous putrequest : envoi doublé au niveau de la prise ------------------------------------------------
with FS.FauxServeurKimi() as srv:
    vrai = http.client.HTTPConnection.send

    def send_double(self, data):
        vrai(self, data)
        if isinstance(data, (bytes, bytearray)) and data.startswith(b"POST "):
            self._double = data
        elif getattr(self, "_double", None) is not None and isinstance(data, (bytes, bytearray)):
            s2 = socket.create_connection((self.host, self.port))
            s2.sendall(self._double + data)
            s2.recv(10)
            s2.close()
            self._double = None

    http.client.HTTPConnection.send = send_double
    try:
        r, tr, ex = appel(srv.url)
    finally:
        http.client.HTTPConnection.send = vrai
    time.sleep(0.3)
    n_post = len([q for q in srv.requetes if q[0] == "POST"])
note("N15_envoi_double_sous_putrequest", issue=ex_nom(ex), posts_serveur=n_post, envois_mesures=tr.envois,
     tentatives=None if r is None else "1 (adaptateur satisfait)",
     constat="le compteur ne voit que putrequest ; http.client.HTTPConnection.send/_send_output non vérifiés")

# --- N16 nom de personne accentué -------------------------------------------------------------------------------------------
with FS.FauxServeurKimi() as srv:
    tr = tr_sur(srv.url)
    res = {}
    for t in ("Bonjour Lazar", "Bonjour Ćirić", "Bonjour Lаzar", "Bonjour CIRIC", "ref session_01XJ6MgnUbaBVDZbP5j1KTqo",
              "ref e2c3ce0b-40f3-55d3-a6bf-333c05f6ccd1"):
        try:
            tr.corps_fil({"model": M, "messages": [{"role": "user", "content": t}], "max_tokens": 10, "stream": False, "n": 1})
            res[t] = "accepté"
        except A.ConfigurationRefusee:
            res[t] = "refusé"
note("N16_filtre_des_noms_et_identifiants", resultats=res)

# --- N17 corps exact des six appels de la fumée -----------------------------------------------------------------------------
with FS.FauxServeurKimi() as srv:
    tr = tr_sur(srv.url)
    champs, refus = set(), []
    for a in EF.plan_fumee():
        b = json.loads(tr.corps_fil({"model": M, "messages": [{"role": "user", "content": a["texte"]}], "max_tokens": a["max_tokens"],
                                     "stream": False, "n": 1}))
        champs |= set(b) | {"stream_options." + k for k in b["stream_options"]} | {"messages[0]." + k for k in b["messages"][0]}
note("N17_corps_de_la_fumee", champs=sorted(champs))

# --- N18 mandataire local : un seul CONNECT, clé absente du CONNECT, 407 classé relançable --------------------------------
def mand(k, c):
    return [b"HTTP/1.1 407 Proxy Authentication Required\r\nContent-Length: 0\r\nConnection: close\r\n\r\n"]


class Mand(Brut):
    pass


connects = []


class HCon(socketserver.BaseRequestHandler):
    def handle(self):
        f = self.request.makefile("rb")
        tete = b""
        while not tete.endswith(b"\r\n\r\n"):
            o = f.readline()
            if not o:
                break
            tete += o
        connects.append(tete)
        self.request.sendall(b"HTTP/1.1 407 Proxy Authentication Required\r\nContent-Length: 0\r\n\r\n")


ps = socketserver.ThreadingTCPServer(("127.0.0.1", 0), HCon)
ps.daemon_threads = True
threading.Thread(target=ps.serve_forever, daemon=True).start()
tr = T.TransportKimiReel(amont="https://api.moonshot.ai", environ={"KIMI_API_KEY": CLE,
                                                                  "HTTPS_PROXY": f"http://127.0.0.1:{ps.server_address[1]}"},
                         delai_silence_s=5, delai_total_s=10)
ad = AS.AdaptateurKimiStrict(tr)
try:
    ad.appeler({"id": "x"}, "Bonjour.", 16)
    ex = None
except Exception as e:  # noqa: BLE001
    ex = e
ps.shutdown()
ps.server_close()
note("N18_mandataire_407", issue=ex_nom(ex), connects=len(connects), cle_dans_connect=any(CLE.encode() in c for c in connects),
     envois_mesures=tr.envois, ligne_connect=connects[0].split(b"\r\n")[0].decode() if connects else None,
     constat="407 du mandataire → ErreurFournisseur (relançable) ; mieux : fatale")

# --- N19 essai de fumée à blanc : forme de l'usage au journal ; coût au-delà de la réserve sans arrêt --------------------------
def regle(k, corps):
    if k == 0:
        return {"usage": {"prompt_tokens": 20, "completion_tokens": 30, "total_tokens": 50}}  # détail de réflexion absent
    if k == 1:
        return {"completion": 16, "raisonnement": 13}
    if k == 2:
        return {"prompt": 40000}  # H3 violée : entrée 4 fois les octets
    if k == 4:
        return {"maintien": 80, "pas_s": 0.1}
    return {}


with tempfile.TemporaryDirectory() as dd, FS.FauxServeurKimi(regle) as srv:
    code = EF.courir(os.path.join(dd, "r.jsonl"), os.path.join(dd, "j.jsonl"), srv.url, 1.0, environ={"KIMI_API_KEY": CLE})
    lignes = [json.loads(x) for x in open(os.path.join(dd, "j.jsonl"), encoding="utf-8")]
    ap = [x for x in lignes if x["evenement"] == "appel"]
    # rejeu v2 : le journal a changé de forme (B1) ; mêmes règles du faux serveur, rangs de la v1 (f2 passe en premier en v2)
    fin = lignes[-1]
    note("N19_fumee_a_blanc_journal", code=code, requetes=srv.nombre, appels=[(a["id"], a["issue"]) for a in ap],
         premier_usage_brut=ap[0]["diagnostic"].get("usage_brut"), premier_motif=ap[0].get("motif"),
         derniere_ligne={k: fin.get(k) for k in ("evenement", "code", "detail", "depense_usd")},
         lecture_v2="f2 en premier reçoit l'usage sans détail de la règle k = 0 : refusé, forme gardée, arrêt 16 au premier appel")
    # second passage : règles décalées pour atteindre f3 (H3 violée) avec f2 et f1 sains
    def regle2(k, corps):
        return {"completion": 16, "raisonnement": 13} if k == 0 else ({"prompt": 40000} if k == 2 else {})
    with tempfile.TemporaryDirectory() as dd2, FS.FauxServeurKimi(regle2) as srv2:
        code2 = EF.courir(os.path.join(dd2, "r.jsonl"), os.path.join(dd2, "j.jsonl"), srv2.url, 1.0, environ={"KIMI_API_KEY": CLE})
        l2 = [json.loads(x) for x in open(os.path.join(dd2, "j.jsonl"), encoding="utf-8")]
        ap2 = [x for x in l2 if x["evenement"] == "appel"]
        note("N19b_fumee_H3_violee_arrete", code=code2, requetes=srv2.nombre, appels=[a["id"] for a in ap2],
             f3_reserve=ap2[-1]["reserve_usd"], f3_cout=ap2[-1]["cout_compte_usd"], arret=l2[-1].get("detail"))

# --- N20 fumée : amont « http://127.0.0.1… » qui contourne le GO ---------------------------------------------------------
with tempfile.TemporaryDirectory() as dd:
    try:
        c1 = EF.courir(os.path.join(dd, "r.jsonl"), os.path.join(dd, "j.jsonl"), "http://127.0.0.1.exemple.invalid", 1.0,
                       environ={"KIMI_API_KEY": CLE})
    except Exception as e:  # noqa: BLE001
        c1 = f"exception non rattrapée : {type(e).__name__}: {e}"
note("N20_go_contourne_par_prefixe", code=c1, constat="préfixe accepté sans GO, puis le transport refuse l'hôte (pas d'envoi)")

json.dump(RES, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True, default=str)
