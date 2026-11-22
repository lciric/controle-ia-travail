"""Serveur git FACTICE en HTTP, sur 127.0.0.1 seulement, à la place de GitHub (essais locaux du script de démarrage).

Sert les dépôts nus d'un dossier local par `git http-backend`. Exige une authentification de base dont le mot de passe est
le jeton factice lu dans un FICHIER (jamais en argument : il n'apparaît pas dans `ps`). Journal : méthode, chemin sans la
requête, état de l'authentification (absente, refusée, admise), code rendu ; jamais l'en-tête d'authentification.

Emploi : python serveur-git-factice.py PORT DOSSIER_DES_DEPOTS FICHIER_DU_JETON JOURNAL FICHIER_PRET
(FICHIER_PRET est écrit quand le serveur écoute.)
"""
import base64
import http.server
import os
import subprocess
import sys
import threading
import time

PORT = int(sys.argv[1])
RACINE = sys.argv[2]
with open(sys.argv[3], encoding="ascii") as fh:
    JETON = fh.read().strip()
JOURNAL = sys.argv[4]
PRET = sys.argv[5]
VERROU = threading.Lock()


def noter(ligne):
    with VERROU, open(JOURNAL, "a", encoding="utf-8") as fh:
        fh.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {ligne}\n")


class Gestionnaire(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def authentification(self):
        en_tete = self.headers.get("Authorization")
        if not en_tete:
            return "absente", None
        try:
            genre, valeur = en_tete.split(" ", 1)
            utilisateur, mot = base64.b64decode(valeur).decode("utf-8").split(":", 1)
        except Exception:
            return "illisible", None
        if genre.lower() == "basic" and mot == JETON:
            return "admise", utilisateur
        return "refusée", None

    def corps(self):
        if self.headers.get("Transfer-Encoding", "").lower() == "chunked":
            morceaux = []
            while True:
                taille = int(self.rfile.readline().strip().split(b";")[0], 16)
                if taille == 0:
                    self.rfile.readline()
                    break
                morceaux.append(self.rfile.read(taille))
                self.rfile.readline()
            return b"".join(morceaux)
        n = int(self.headers.get("Content-Length") or 0)
        return self.rfile.read(n) if n else b""

    def traiter(self, methode):
        chemin, _, requete = self.path.partition("?")
        etat, utilisateur = self.authentification()
        if etat != "admise":
            self.send_response(401)
            self.send_header("WWW-Authenticate", 'Basic realm="factice"')
            self.send_header("Content-Length", "0")
            self.end_headers()
            noter(f"{methode} {chemin} authentification {etat} -> 401")
            return
        corps = self.corps() if methode == "POST" else b""
        env = {
            "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "GIT_PROJECT_ROOT": RACINE, "GIT_HTTP_EXPORT_ALL": "1", "PATH_INFO": chemin,
            "QUERY_STRING": requete, "REQUEST_METHOD": methode, "REMOTE_USER": utilisateur,
            "REMOTE_ADDR": "127.0.0.1", "CONTENT_TYPE": self.headers.get("Content-Type", ""),
            "CONTENT_LENGTH": str(len(corps)),
        }
        if self.headers.get("Git-Protocol"):
            env["GIT_PROTOCOL"] = self.headers["Git-Protocol"]
        if self.headers.get("Content-Encoding"):
            env["HTTP_CONTENT_ENCODING"] = self.headers["Content-Encoding"]
        p = subprocess.Popen(["git", "http-backend"], env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        def ecrire():
            try:
                p.stdin.write(corps)
            finally:
                p.stdin.close()

        threading.Thread(target=ecrire, daemon=True).start()
        tete = b""
        while b"\r\n\r\n" not in tete and b"\n\n" not in tete:
            b = p.stdout.read(1)
            if not b:
                break
            tete += b
        statut = 200
        en_tetes = []
        for ligne in tete.decode("latin-1").splitlines():
            if not ligne.strip():
                continue
            cle, _, val = ligne.partition(":")
            if cle.lower() == "status":
                statut = int(val.strip().split()[0])
            else:
                en_tetes.append((cle.strip(), val.strip()))
        self.send_response(statut)
        for cle, val in en_tetes:
            self.send_header(cle, val)
        self.end_headers()
        while True:
            bloc = p.stdout.read(1 << 16)
            if not bloc:
                break
            self.wfile.write(bloc)
        p.wait()
        noter(f"{methode} {chemin} authentification admise ({utilisateur}) -> {statut}")

    def do_GET(self):
        self.traiter("GET")

    def do_POST(self):
        self.traiter("POST")


serveur = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Gestionnaire)
with open(PRET, "w", encoding="ascii") as fh:
    fh.write(f"{os.getpid()}\n")
noter(f"serveur factice à l'écoute sur 127.0.0.1:{PORT}, dépôts {RACINE}")
serveur.serve_forever()
