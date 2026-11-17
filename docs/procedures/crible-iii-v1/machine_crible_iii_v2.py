"""Aide du programme machine du crible (iii) — v2 (suit l'aide v1, gardée telle quelle : six fichiers du crible, tour 1 de la
contre-lecture du code ; dérivée de `machine_pilote_mr2_v74_v2.py` du pilote, qui n'est pas modifiée).
Bibliothèque standard seule ; jouée par `python3 -I -B` sur la machine, jamais avec une clé dans son environnement sauf `balayer`, qui
lit les valeurs à chercher par des noms fixés (S_JETON, S_CLE_A) et n'imprime jamais une valeur.

Chaque sous-commande lit une sortie du lanceur du crible (ou un feu de la branche d'entrée) et rend 0 si elle est celle qu'attend la
procédure `procedure-machine-crible-iii-v2.md`, 2 sinon (motif sur la sortie standard, sans valeur privée).
"""
import base64
import hashlib
import json
import os
import re
import socket
import ssl
import sys
import urllib.parse

HEX64 = re.compile(r"[0-9a-f]{64}")
HEX40 = re.compile(r"[0-9a-f]{40}")
N_MONDES = 20
GABARIT_G0 = "e77d3041f7815b2c0579cbafdb2898ca8569fe61e6cb51b99a41c3724fc456a2"
PORTS = (8811, 8812)
HOTES = ("api.anthropic.com",)
PHRASE_MAX = 400
CHEMIN = re.compile(r"[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*")
NOMS_SECRETS = ("S_JETON", "S_CLE_A")
GENRES = {"phrase": {"feu", "secret_sha256", "phrase_fichier_sha256", "inscription_commit", "inscription_chemin"},
          "mondes": {"feu", "fichier_mondes_sha256", "inscription_commit", "inscription_chemin"},
          "reel": {"feu", "fichier_mondes_sha256", "go_credits", "go_hors"},
          "arret": {"feu", "cause"}}
GO = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d{2}")
FICHIERS_DU_CRIBLE = ("crible_iii_v1.py", "crible_iii_v2.py", "lanceur_crible_iii_v2.py", "mesure_crible_iii_v1.py",
                      "lire_crible_iii_v1.py", "relais_factice_crible_iii_v1.py")


class Refus(Exception):
    pass


def derniere_ligne_json(chemin):
    try:
        lignes = [l for l in open(chemin, encoding="utf-8").read().splitlines() if l.strip()]
    except (OSError, UnicodeDecodeError) as e:
        raise Refus(f"journal illisible ({type(e).__name__})") from None
    for l in reversed(lignes):
        try:
            d = json.loads(l)
        except ValueError:
            continue
        if isinstance(d, dict):
            return d
    raise Refus("aucune ligne JSON dans le journal")


def hex64(x, quoi):
    if not (isinstance(x, str) and HEX64.fullmatch(x)):
        raise Refus(f"{quoi} : empreinte de 64 caractères hexadécimaux attendue")
    return x


def c_secret(journal):
    d = derniere_ligne_json(journal)
    if set(d) != {"secret_sha256"}:
        raise Refus("secret : une seule clé « secret_sha256 » attendue")
    print(hex64(d["secret_sha256"], "secret_sha256"))


def c_generer(journal):
    d = derniere_ligne_json(journal)
    ctl = d.get("controles")
    if not (isinstance(ctl, list) and [c.get("monde") for c in ctl] == list(range(1, N_MONDES + 1))
            and all(c.get("conforme") is True for c in ctl)):
        raise Refus(f"generer : {N_MONDES} mondes « conforme » vrais attendus, mondes 1 à {N_MONDES}")
    print(hex64(d.get("fichier_mondes_sha256"), "fichier_mondes_sha256"))


def c_engagement(chemin, h):
    try:
        e = json.load(open(chemin, encoding="utf-8"))
    except (OSError, ValueError) as x:
        raise Refus(f"engagement illisible ({type(x).__name__})") from None
    if hex64(e.get("fichier_mondes_sha256"), "engagement") != h or e.get("public") is not False:
        raise Refus("engagement : fichier_mondes_sha256 ≠ celui de generer, ou mondes publics")
    s = e.get("mondes_sha256")
    if not (isinstance(s, list) and len(s) == N_MONDES and len(set(s)) == N_MONDES):
        raise Refus(f"engagement : {N_MONDES} mondes_sha256 distincts attendus")
    print(",".join(hex64(x, "mondes_sha256") for x in s))


def c_preparer(journal):
    d = derniere_ligne_json(journal)
    if d.get("c16_admises") is not True or d.get("gabarit_g0_sha256") != GABARIT_G0:
        raise Refus("preparer : C-16 non admise ou gabarit G0 ≠ e77d3041…")
    m = d.get("mondes") or {}
    if sorted(m, key=int) != [str(r) for r in range(1, N_MONDES + 1)] or any(v.get("octets_g2_pire", 10 ** 9) > 53000 for v in m.values()):
        raise Refus("preparer : vingt mondes, G2 au pire sous 53 000 octets attendus")
    print("preparer conforme")


def c_jouer(journal, mode):
    d = derniere_ligne_json(journal)
    c = d.get("comptes") or {}
    if mode == "a_blanc":
        if d.get("mode") != "a_blanc" or d.get("arret") is not None or c.get("complet") != 100 or d.get("complets") != N_MONDES:
            raise Refus("jouer à blanc : mode a_blanc, 100 appels complets, 20 mondes complets, aucun arrêt attendus")
    elif mode == "reel":
        a = d.get("arret")
        if d.get("mode") != "reel" or (a is not None and a.get("ligne") != "minimum"):
            raise Refus("jouer réel : mode reel, aucun arrêt autre que la ligne du minimum")
    else:
        raise Refus("mode inconnu")
    print(json.dumps({"mode": d["mode"], "comptes": c, "complets": d.get("complets"), "arret": d.get("arret")},
                     ensure_ascii=False, sort_keys=True))


def c_rapatrier(journal):
    if derniere_ligne_json(journal).get("aucun_monde") is not True:
        raise Refus("rapatrier : aucun_monde vrai attendu")
    print("rapatriement sans monde")


def c_mesurer(journal, attendu):
    if derniere_ligne_json(journal).get("programme_sha256") != hex64(attendu, "empreinte du programme de mesure"):
        raise Refus("mesurer : programme_sha256 ≠ celui de l'addendum")
    print("mesure faite par le programme attendu")


def c_addendum(addendum, dossier, texte_sha):
    """Le code du crible extrait au commit est celui de l'addendum d'empreintes scellé (ligne « empreinte  chemin »)."""
    t = open(addendum, encoding="utf-8").read()
    if hex64(texte_sha, "texte") not in t:
        raise Refus("addendum : il ne cite pas le texte qui fait foi")
    for f in FICHIERS_DU_CRIBLE:
        sha = hashlib.sha256(open(os.path.join(dossier, f), "rb").read()).hexdigest()
        if f"{sha}  docs/procedures/crible-iii-v1/{f}" not in t:
            raise Refus(f"addendum : {f} absent ou différent")
    m = re.search(r"([0-9a-f]{64})  docs/procedures/crible-iii-v1/mesure_crible_iii_v1\.py", t)
    print(m.group(1))


def c_phrase(chemin):
    b = open(chemin, "rb").read()
    if not (2 <= len(b) <= PHRASE_MAX) or b.count(b"\n") != 1 or not b.endswith(b"\n") or b"\0" in b or b"\r" in b:
        raise Refus(f"phrase : une ligne non vide, sans octet nul, finie par un retour à la ligne, au plus {PHRASE_MAX} octets")
    try:
        b.decode("utf-8")
    except UnicodeDecodeError:
        raise Refus("phrase : UTF-8 attendu") from None
    print("phrase de forme conforme")


def lire_feu(chemin, genre):
    attendues = GENRES[genre]
    try:
        lignes = open(chemin, encoding="utf-8").read().splitlines()
    except (OSError, UnicodeDecodeError) as e:
        raise Refus(f"feu illisible ({type(e).__name__})") from None
    d = {}
    for l in lignes:
        if not l.strip():
            continue
        k, sep, v = l.partition("=")
        if not sep or k in d or k not in attendues or len(v) > 300 or any(ord(ch) < 32 for ch in v):
            raise Refus(f"feu {genre} : ligne illisible ou clé inattendue")
        d[k] = v
    if set(d) != attendues or d["feu"] != genre:
        raise Refus(f"feu {genre} : clés {sorted(d)} ≠ {sorted(attendues)}")
    for k in ("secret_sha256", "phrase_fichier_sha256", "fichier_mondes_sha256"):
        if k in d:
            hex64(d[k], k)
    if "inscription_commit" in d and not HEX40.fullmatch(d["inscription_commit"]):
        raise Refus("feu : inscription_commit de 40 caractères hexadécimaux attendu")
    if "inscription_chemin" in d and (not CHEMIN.fullmatch(d["inscription_chemin"]) or ".." in d["inscription_chemin"]):
        raise Refus("feu : inscription_chemin illisible")
    if genre == "reel" and not (GO.fullmatch(d["go_credits"]) and GO.fullmatch(d["go_hors"]) and d["go_credits"] != d["go_hors"]):
        raise Refus("feu réel : deux lignes de GO distinctes attendues")
    if genre == "arret" and not re.fullmatch(r"[A-Za-z0-9 ,.:;()_-]{1,100}", d["cause"]):
        raise Refus("feu d'arrêt : cause illisible")
    return d


def c_feu(chemin, genre, *attendus):
    d = lire_feu(chemin, genre)
    for x in attendus:
        k, _, v = x.partition("=")
        if d.get(k) != v:
            raise Refus(f"feu {genre} : {k} ≠ valeur attendue par la machine")
    for k in ("inscription_commit", "inscription_chemin", "phrase_fichier_sha256", "go_credits", "go_hors"):
        if k in d:
            print(f"{k}={d[k]}")
    print("feu conforme")


def c_inscription(chemin, *empreintes):
    t = open(chemin, encoding="utf-8", errors="replace").read()
    manquantes = [e[:12] for e in empreintes if hex64(e, "empreinte") not in t]
    if manquantes:
        raise Refus(f"inscription : empreinte(s) absente(s) du fichier au commit : {manquantes}")
    print(f"{len(empreintes)} empreinte(s) inscrite(s)")


def c_ports():
    occupes = []
    for p in PORTS:
        s = socket.socket()
        s.settimeout(2)
        if s.connect_ex(("127.0.0.1", p)) == 0:
            occupes.append(p)
        s.close()
    if occupes:
        raise Refus(f"ports occupés : {occupes}")
    print("ports 8811 et 8812 libres")


def c_tls():
    echecs = []
    for h in HOTES:
        try:
            s = socket.create_connection((h, 443), timeout=10)
            c = ssl.create_default_context().wrap_socket(s, server_hostname=h)
            c.close()
        except Exception as e:  # noqa: BLE001
            echecs.append(f"{h} {type(e).__name__}")
    if echecs:
        raise Refus(f"fournisseur injoignable : {echecs}")
    print("fournisseur joignable (TLS)")


def formes(valeur):
    f = {valeur, urllib.parse.quote(valeur, safe=""), base64.b64encode(valeur.encode()).decode().rstrip("="),
         base64.b64encode(f"x-access-token:{valeur}".encode()).decode().rstrip("=")}
    return {x.encode() for x in f if len(x) >= 8}


def c_balayer(*args):
    """Aucune forme du jeton, de la clé (par leurs noms S_*), du secret (brut, hexadécimal, base64) ni de la phrase (8 octets au
    moins) dans les fichiers nommés ; 3 s'il y a un constat (fichier et forme nommés, jamais la valeur)."""
    secret, phrase, fichiers = None, None, []
    a = list(args)
    while a:
        x = a.pop(0)
        if x == "--secret":
            secret = a.pop(0)
        elif x == "--phrase":
            phrase = a.pop(0)
        else:
            fichiers.append(x)
    cherche = []
    for n in NOMS_SECRETS:
        v = os.environ.get(n)
        if not v:
            raise Refus(f"balayage : valeur {n} absente (nom seul)")
        cherche += [(n, f) for f in formes(v)]
    if secret and os.path.exists(secret):
        s = open(secret, "rb").read()
        cherche += [("secret", s), ("secret", s.hex().encode()), ("secret", s.hex().upper().encode()),
                    ("secret", base64.b64encode(s).rstrip(b"="))]
    if phrase and os.path.exists(phrase):
        p = open(phrase, "rb").read().rstrip(b"\n")
        if len(p) >= 8:
            cherche += [("phrase", p), ("phrase", base64.b64encode(p).rstrip(b"="))]
    trouves = []
    for f in fichiers:
        try:
            b = open(f, "rb").read()
        except OSError as e:
            raise Refus(f"balayage : {os.path.basename(f)} illisible ({type(e).__name__})") from None
        noms = sorted({n for n, forme in cherche if forme and forme in b})
        if noms:
            trouves.append(f)
            print(f"BALAYAGE : forme de {', '.join(noms)} trouvée dans {f}")
    if trouves:
        return 3
    print(f"balayage : {len(fichiers)} fichier(s), aucune forme trouvée")
    return 0


COMMANDES = {"secret": c_secret, "generer": c_generer, "engagement": c_engagement, "preparer": c_preparer, "jouer": c_jouer,
             "rapatrier": c_rapatrier, "mesurer": c_mesurer, "addendum": c_addendum, "phrase": c_phrase, "feu": c_feu,
             "inscription": c_inscription, "ports": c_ports, "tls": c_tls, "balayer": c_balayer}


def main(argv):
    if not argv or argv[0] not in COMMANDES:
        print("REFUS : sous-commande inconnue")
        return 2
    try:
        r = COMMANDES[argv[0]](*argv[1:])
    except Refus as e:
        print(f"REFUS : {e}")
        return 2
    except (TypeError, IndexError, OSError):
        print("REFUS : arguments ou fichier")
        return 2
    return r or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
