# épreuve d'isolement du bras S : lectures, écritures, réseau
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


tenter("lecture-leurre", lambda: lire("/srv/leurre/leurre-v1.txt"))
tenter("lecture-leurre-proc", lambda: lire("/proc/1/root/srv/leurre/leurre-v1.txt"))
tenter("lecture-shadow", lambda: lire("/etc/shadow"))
tenter("lecture-cle-ssh-root", lambda: lire("/root/.ssh/authorized_keys"))
tenter("liste-srv", lambda: os.listdir("/srv"))
tenter("ecriture-mathlib", lambda: ecrire("/opt/mathlib/Piege-v1.txt"))
tenter("ecriture-elan", lambda: ecrire("/opt/elan/Piege-v1.txt"))
tenter("ecriture-pybac", lambda: ecrire("/opt/pybac/Piege-v1.txt"))
tenter("ecriture-harnais", lambda: ecrire("/opt/harnais/Piege-v1.txt"))
tenter("ecriture-usr", lambda: ecrire("/usr/Piege-v1.txt"))
tenter("reseau-tcp", lambda: socket.create_connection(("1.1.1.1", 443), 5))
tenter("reseau-dns", lambda: socket.gethostbyname("github.com"))
