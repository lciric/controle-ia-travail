import os
import socket


def tenter(nom, action):
    try:
        r = action()
        print(f"ISOLEMENT {nom} REUSSI {str(r)[:120]}")
    except Exception as e:  # noqa: BLE001 — chaque échec est écrit, rien n'est avalé en silence
        print(f"ISOLEMENT {nom} ECHEC {type(e).__name__}: {e}")


def lire(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def ecrire(p, texte="x"):
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(texte)
    return "écrit"


tenter("lecture-tmp-precedent", lambda: lire("/tmp/persistance-py-v1.txt"))
tenter("lecture-item-precedent", lambda: lire("/item/persistance-py-v1.txt"))
tenter("liste-items", lambda: os.listdir("/srv/items"))
