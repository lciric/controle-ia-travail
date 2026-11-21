"""Vérifie, à l'octet, que la ligne de commande du lanceur est celle du complément 1 v3 sauf le dernier argument — v2.

(v2 = v1 à l'identique sur le fond ; éprouvée en v2 aussi sur des lanceurs volontairement altérés, essais/commande/.)
Usage : verifier-commande-v2.py COMPLEMENT LANCEUR DOSSIER_DES_SORTIES_ATTENDU
Rend 0 si égal, 1 sinon ; écrit ce qu'il compare.
"""
import hashlib
import sys


def lignes_de_commande(octets):
    return [l for l in octets.split(b"\n") if l.startswith(b"env -C ")]


def main(args):
    if len(args) != 3:
        print(__doc__)
        return 2
    complement, lanceur, sorties = args
    with open(complement, "rb") as fh:
        oc = fh.read()
    with open(lanceur, "rb") as fh:
        ol = fh.read()
    print("complément sha256 :", hashlib.sha256(oc).hexdigest())
    print("lanceur sha256    :", hashlib.sha256(ol).hexdigest())
    lc, ll = lignes_de_commande(oc), lignes_de_commande(ol)
    print("lignes « env -C » : complément", len(lc), "; lanceur", len(ll))
    if len(lc) != 1 or len(ll) != 1:
        print("ÉCHEC : une seule ligne de commande attendue de chaque côté")
        return 1
    c, l = lc[0], ll[0]
    tete_c, _, dernier_c = c.rpartition(b" ")
    tete_l, _, dernier_l = l.rpartition(b" ")
    print("dernier argument du complément :", dernier_c.decode(errors="replace"))
    print("dernier argument du lanceur    :", dernier_l.decode(errors="replace"))
    print("tête (tout sauf le dernier argument) : complément", len(tete_c), "octets, sha256",
          hashlib.sha256(tete_c).hexdigest())
    print("tête (tout sauf le dernier argument) : lanceur   ", len(tete_l), "octets, sha256",
          hashlib.sha256(tete_l).hexdigest())
    ok = tete_c == tete_l and dernier_l == sorties.encode() and l == tete_c + b" " + sorties.encode()
    print("ÉGAL à l'octet sauf le dernier argument" if ok else "ÉCHEC : différence")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
