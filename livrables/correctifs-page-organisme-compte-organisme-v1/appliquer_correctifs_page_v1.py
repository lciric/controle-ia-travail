"""Applique un couple « ancien texte, nouveau texte » (correctifs de la page publique de l'organisme, compte organisme, v1) à une
source donnée, sans jamais écrire sur la source : la sortie est un fichier neuf.

  python3 -I appliquer_correctifs_page_v1.py COUPLE.json SOURCE SORTIE

Refus (code 2, rien écrit) : empreinte de la source ≠ `source_sha256` du couple ; « ancien » absent ou présent plus d'une fois ;
sortie déjà existante ; après application, « ancien » encore présent ; suite des nombres du fichier changée (aucun chiffre
changé) ; tout octet hors du passage changé. Code 0 : sortie écrite ; imprime les empreintes avant et après.
"""
import hashlib
import json
import os
import re
import sys


def refus(m):
    print(f"refus : {m}", file=sys.stderr)
    sys.exit(2)


def main(couple, source, sortie):
    c = json.load(open(couple, encoding="utf-8"))
    brut = open(source, "rb").read()
    if hashlib.sha256(brut).hexdigest() != c["source_sha256"]:
        refus(f"empreinte de la source {hashlib.sha256(brut).hexdigest()} ≠ {c['source_sha256']}")
    t = brut.decode("utf-8")
    a, b = c["ancien"], c["nouveau"]
    if t.count(a) != 1:
        refus(f"« ancien » présent {t.count(a)} fois (une seule exigée)")
    if os.path.exists(sortie):
        refus("sortie déjà existante")
    u = t.replace(a, b)
    if a in u:
        refus("« ancien » encore présent après application")
    nombres = lambda x: re.findall(r"\d+(?:[.,]\d+)*", x)
    if nombres(t) != nombres(u):
        refus("suite des nombres changée")
    i = t.index(a)
    if u[:i] != t[:i] or u[i + len(b):] != t[i + len(a):]:
        refus("octets hors du passage changés")
    with open(sortie, "xb") as f:
        f.write(u.encode("utf-8"))
    print(json.dumps({"fichier_public": c["fichier_public"], "source_sha256": c["source_sha256"],
                      "sortie_sha256": hashlib.sha256(u.encode("utf-8")).hexdigest(), "octet_du_passage": len(t[:i].encode("utf-8")),
                      "ancien_restant": u.count(a)}, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        refus("usage : COUPLE.json SOURCE SORTIE")
    main(*sys.argv[1:])
