"""Applique un couple « ancien texte, nouveau texte » (correctifs de la page publique de l'organisme, compte organisme, v3 ; les v1 et
v2 restent en place) à une source donnée, sans jamais écrire sur la source : la sortie est un fichier neuf.

  python3 -I appliquer_correctifs_page_v3.py COUPLE.json SOURCE SORTIE

Changement depuis la v2 : les articles « un », « une » ne comptent plus comme nombres (la v2 refusait à tort le couple
`nul_v9` v2, « une loi » → « des lois »). Changements de la v2 depuis la v1 (lecture du second lecteur, m2 à m4) : le couple doit être égal à son compagnon `COUPLE.json.sha256` et
porter ses champs ; la garde des nombres voit aussi les nombres en lettres (anglais et français), les signes « % », « = », « < »,
« > », « ≤ », « ≥ », « ± », « α » ; une source ou une sortie en lien symbolique, une source non UTF-8, une sortie qui apparaît entre
le contrôle et l'écriture sont des refus nommés.

Refus (code 2, rien écrit) : couple différent de son compagnon ou incomplet ; empreinte de la source ≠ `source_sha256` ; « ancien »
absent ou présent plus d'une fois ; sortie déjà existante ; après application, « ancien » encore présent ; suite des nombres et des
signes changée ; tout octet hors du passage changé. Code 0 : sortie écrite ; imprime les empreintes avant et après.
"""
import hashlib
import json
import os
import re
import sys

CHAMPS = ("version", "fichier_public", "source_sha256", "ancien", "nouveau")
MOTS = ("zero one two three four five six seven eight nine ten eleven twelve twenty hundred thousand half twice once "
        "zéro deux trois quatre cinq six sept huit neuf dix onze douze vingt cent mille moitié").split()
JETONS = re.compile(r"\d+(?:[.,]\d+)*|[%=<>≤≥±α]|\b(?:" + "|".join(MOTS) + r")\b", re.IGNORECASE)


def refus(m):
    print(f"refus : {m}", file=sys.stderr)
    sys.exit(2)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main(couple, source, sortie):
    try:
        brut_couple = open(couple, "rb").read()
        compagnon = open(couple + ".sha256", encoding="utf-8").read().split()[0]
    except (OSError, IndexError):
        refus("couple ou son compagnon illisible")
    if sha(brut_couple) != compagnon:
        refus("couple ≠ son compagnon")
    try:
        c = json.loads(brut_couple.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        refus("couple illisible")
    if not isinstance(c, dict) or any(not isinstance(c.get(k), str) or not c.get(k) for k in CHAMPS):
        refus(f"couple incomplet : champs {CHAMPS} exigés")
    if os.path.islink(source) or os.path.islink(sortie):
        refus("source ou sortie en lien symbolique")
    try:
        brut = open(source, "rb").read()
        t = brut.decode("utf-8")
    except (OSError, UnicodeDecodeError):
        refus("source illisible ou non UTF-8")
    if sha(brut) != c["source_sha256"]:
        refus(f"empreinte de la source {sha(brut)} ≠ {c['source_sha256']}")
    a, b = c["ancien"], c["nouveau"]
    if t.count(a) != 1:
        refus(f"« ancien » présent {t.count(a)} fois (une seule exigée)")
    if os.path.lexists(sortie):
        refus("sortie déjà existante")
    u = t.replace(a, b)
    if a in u:
        refus("« ancien » encore présent après application")
    if [x.lower() for x in JETONS.findall(t)] != [x.lower() for x in JETONS.findall(u)]:
        refus("suite des nombres ou des signes changée")
    i = t.index(a)
    if u[:i] != t[:i] or u[i + len(b):] != t[i + len(a):]:
        refus("octets hors du passage changés")
    try:
        with open(sortie, "xb") as f:
            f.write(u.encode("utf-8"))
    except FileExistsError:
        refus("sortie apparue avant l'écriture")
    print(json.dumps({"couple_sha256": compagnon, "fichier_public": c["fichier_public"], "source_sha256": c["source_sha256"],
                      "sortie_sha256": sha(u.encode("utf-8")), "ancien_restant": u.count(a)}, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        refus("usage : COUPLE.json SOURCE SORTIE")
    main(*sys.argv[1:])
