"""Aide du programme machine du pilote MR-2 sans ssh — v1 (procédure v11). Bibliothèque standard seule ; joué par
`python3 -I -B` sur la machine, jamais avec une clé dans son environnement sauf `balayer`, qui lit les valeurs à chercher par des
noms fixés (S_JETON, S_CLE_A, S_CLE_G, S_CLE_O) et n'imprime jamais une valeur.

Chaque sous-commande lit une sortie du lanceur v74 (ou un feu de la branche d'entrée) et rend 0 si elle est celle qu'attend la
procédure v11, 2 sinon (motif sur la sortie standard, sans valeur privée). Les attendus sont ceux de la procédure v10, sections 4 à 11,
écrits ici en programme au lieu d'être lus par la session.
"""
import base64
import json
import os
import re
import socket
import ssl
import sys
import urllib.parse

HEX64 = re.compile(r"[0-9a-f]{64}")
HEX40 = re.compile(r"[0-9a-f]{40}")
GABARIT = "e77d3041f7815b2c0579cbafdb2898ca8569fe61e6cb51b99a41c3724fc456a2"
PROGRAMME_MESURE = "676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365"
CLES_PREPARER = {"c16", "c17", "episodes_servis", "gabarit_sha256", "heritages_sha256", "mondes", "textes_servis"}
GO_PI1, GO_PI2 = "GO-2026-11-14-13", "GO-2026-11-14-14"
PORTS = (8811, 8812, 8813, 8814)
HOTES = ("api.anthropic.com", "generativelanguage.googleapis.com", "api.openai.com")
PHRASE_MAX = 400
CHEMIN = re.compile(r"[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*")
NOMS_SECRETS = ("S_JETON", "S_CLE_A", "S_CLE_G", "S_CLE_O")


class Refus(Exception):
    pass


def derniere_ligne_json(chemin):
    """La dernière ligne non vide du journal qui est un objet JSON (le lanceur imprime une ligne JSON ; ses refus vont sur la
    sortie d'erreur, réunie dans le même journal)."""
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
    if not (isinstance(ctl, list) and len(ctl) == 4 and [c.get("monde") for c in ctl] == [1, 2, 3, 4]
            and all(c.get("conforme") is True for c in ctl)):
        raise Refus("generer : quatre mondes « conforme » vrais attendus, mondes 1 à 4")
    print(hex64(d.get("fichier_mondes_sha256"), "fichier_mondes_sha256"))


def c_engagement(chemin, h):
    try:
        e = json.load(open(chemin, encoding="utf-8"))
    except (OSError, ValueError) as x:
        raise Refus(f"engagement illisible ({type(x).__name__})") from None
    if hex64(e.get("fichier_mondes_sha256"), "engagement") != h:
        raise Refus("engagement : fichier_mondes_sha256 ≠ celui de generer")
    s = e.get("mondes_sha256")
    if not (isinstance(s, list) and len(s) == 4):
        raise Refus("engagement : quatre mondes_sha256 attendus")
    print(" ".join(hex64(x, "mondes_sha256") for x in s))


def c_preparer(journal):
    d = derniere_ligne_json(journal)
    if set(d) != CLES_PREPARER:
        raise Refus(f"preparer : clés {sorted(d)} ≠ {sorted(CLES_PREPARER)}")
    c16 = d["c16"]
    if not (isinstance(c16, dict) and c16 and all(isinstance(v, dict) and v.get("admise") is True for v in c16.values())):
        raise Refus("preparer : une loi de C-16 non admise")
    if d["gabarit_sha256"] != GABARIT:
        raise Refus("preparer : gabarit_sha256 ≠ e77d3041…")
    print("preparer conforme")


def c_jouer(journal, mode):
    d = derniere_ligne_json(journal)
    if d.get("arret") is not None:
        raise Refus("jouer : arrêt porté")
    c = d.get("comptes") or {}
    if mode == "a_blanc":
        if d.get("mode") != "a_blanc" or c != {"complet": 16, "echec": 0, "tronque": 0}:
            raise Refus("jouer à blanc : mode a_blanc et comptes 16/0/0 attendus")
    elif mode == "reel":
        if d.get("mode") != "reel" or set(c) != {"complet", "echec", "tronque"} or sum(c.values()) != 16:
            raise Refus("jouer réel : mode reel et 16 appels comptés attendus")
    else:
        raise Refus("mode inconnu")
    print(json.dumps({"mode": d["mode"], "comptes": c, "abandonnes": sorted((d.get("abandonnes") or {}).keys())},
                     ensure_ascii=False, sort_keys=True))


def c_rapatrier(journal):
    d = derniere_ligne_json(journal)
    if d.get("aucun_monde") is not True:
        raise Refus("rapatrier : aucun_monde vrai attendu")
    print("rapatriement sans monde")


def c_mesurer(journal):
    d = derniere_ligne_json(journal)
    if d.get("programme_sha256") != PROGRAMME_MESURE:
        raise Refus("mesurer : programme_sha256 ≠ 676d5f37…")
    print("mesure faite par le programme attendu")


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
    """Feu de la branche d'entrée : lignes « clé=valeur », clés exactes selon le genre, aucune autre ligne."""
    attendues = {"phrase": {"feu", "secret_sha256", "phrase_fichier_sha256", "inscription_commit", "inscription_chemin"},
                 "mondes": {"feu", "fichier_mondes_sha256", "inscription_commit", "inscription_chemin"},
                 "reel": {"feu", "fichier_mondes_sha256", "go_pi1", "go_pi2"},
                 "relance-reel-2": {"feu", "fichier_mondes_sha256", "cause"},
                 "arret": {"feu", "cause"}}[genre]
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
    if genre == "reel" and (d["go_pi1"], d["go_pi2"]) != (GO_PI1, GO_PI2):
        raise Refus("feu réel : lignes GO-2026-11-14-13 et GO-2026-11-14-14 attendues")
    return d


def c_feu(chemin, genre, *attendus):
    """Imprime les champs utiles du feu (aucune valeur privée : un feu n'en porte aucune) ; refuse un écart aux attendus
    « clé=valeur » passés en arguments."""
    d = lire_feu(chemin, genre)
    for x in attendus:
        k, _, v = x.partition("=")
        if d.get(k) != v:
            raise Refus(f"feu {genre} : {k} ≠ valeur attendue par la machine")
    for k in ("inscription_commit", "inscription_chemin", "phrase_fichier_sha256"):
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
    print("ports 8811 à 8814 libres")


def c_tls():
    """Joignabilité des trois fournisseurs (poignée TLS seulement : aucune clé, aucun appel d'interface)."""
    echecs = []
    for h in HOTES:
        try:
            s = socket.create_connection((h, 443), timeout=10)
            c = ssl.create_default_context().wrap_socket(s, server_hostname=h)
            c.close()
        except Exception as e:  # noqa: BLE001
            echecs.append(f"{h} {type(e).__name__}")
    if echecs:
        raise Refus(f"fournisseur(s) injoignable(s) : {echecs}")
    print("trois fournisseurs joignables (TLS)")


def formes(valeur):
    """Formes cherchées d'une valeur secrète (texte) : brute, URL, base64 de la valeur et de « x-access-token:valeur »."""
    f = {valeur, urllib.parse.quote(valeur, safe=""), base64.b64encode(valeur.encode()).decode().rstrip("="),
         base64.b64encode(f"x-access-token:{valeur}".encode()).decode().rstrip("=")}
    return {x.encode() for x in f if len(x) >= 8}


def c_balayer(*args):
    """Balayage avant toute poussée : aucune forme des valeurs secrètes (jeton, trois clés : par leurs noms S_*), du secret de 32
    octets (brut, hexadécimal, base64) ni de la phrase (si au moins 8 octets) dans les fichiers nommés. Rend 3 s'il y a un
    constat (chaque fichier et chaque forme nommés, jamais la valeur), 2 si un nom manque."""
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
        cherche += [("secret", s), ("secret", s.hex().encode()), ("secret", base64.b64encode(s).rstrip(b"="))]
    if phrase and os.path.exists(phrase):
        p = open(phrase, "rb").read().rstrip(b"\n")
        if len(p) >= 8:
            cherche.append(("phrase", p))
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


def c_bloc(texte, journal):
    """Bloc gelé du texte scellé égal, à l'octet, à la sortie de `bloc --releve-sonde` (procédure v10, section 4)."""
    t = open(texte, encoding="utf-8").read()
    b = open(journal, encoding="utf-8").read()
    d, f = "<!-- empreintes-du-code-pilote-v74 : début -->", "<!-- empreintes-du-code-pilote-v74 : fin -->"
    if t.count(d) != 1 or t.count(f) != 1:
        raise Refus("bloc : marques du bloc absentes ou multiples dans le texte")
    i, j = t.index(d), t.index(f) + len(f)
    if t[i:j] + "\n" != b:
        raise Refus("bloc : BLOC DIFFÉRENT")
    print("bloc égal")


COMMANDES = {"secret": c_secret, "generer": c_generer, "engagement": c_engagement, "preparer": c_preparer, "jouer": c_jouer,
             "rapatrier": c_rapatrier, "mesurer": c_mesurer, "phrase": c_phrase, "feu": c_feu, "inscription": c_inscription,
             "ports": c_ports, "tls": c_tls, "balayer": c_balayer, "bloc": c_bloc}


def main(argv):
    if not argv or argv[0] not in COMMANDES:
        print("REFUS : sous-commande inconnue")
        return 2
    try:
        r = COMMANDES[argv[0]](*argv[1:])
    except Refus as e:
        print(f"REFUS : {e}")
        return 2
    except (TypeError, IndexError):
        print("REFUS : arguments")
        return 2
    return r or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
