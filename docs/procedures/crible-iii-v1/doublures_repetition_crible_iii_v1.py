"""Doublures de la répétition de la machine du crible (iii) — v1 (essai seulement ; aucune clé, aucun appel, aucun loueur).

- `loueur PORT JOURNAL` : doublure de l'interface du loueur (127.0.0.1) ; chaque requête (méthode, chemin) est écrite au journal ; 200.
- `lanceur …` : doublure du lanceur du crible, aux sorties de même forme (secret réel de 32 octets ; vingt « mondes » factices et
  leur engagement ; `preparer` ; `jouer` (à blanc ou « réel » à blanc) ; `rapatrier` sans `prive/`), quelques secondes en tout.
- `mesure …` : imprime l'empreinte du programme de mesure du code extrait (celle que l'addendum porte).
- `lire …` : écrit une lecture factice et son compagnon.
Le lanceur réel est éprouvé à part, par l'essai à blanc complet (`essai_a_blanc_crible_iii_v1.py`).
"""
import hashlib
import json
import os
import secrets
import shutil
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def ecrire_scelle(chemin, objet):
    b = (json.dumps(objet, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode()
    open(chemin, "xb").write(b)
    open(chemin + ".sha256", "x").write(f"{hashlib.sha256(b).hexdigest()}  {os.path.basename(chemin)}\n")


def arg(a, nom):
    return a[a.index(nom) + 1]


def loueur(port, journal):
    class G(BaseHTTPRequestHandler):
        def log_message(self, *x):
            pass

        def _r(self):
            n = int(self.headers.get("Content-Length", "0") or 0)
            if n:
                self.rfile.read(n)
            with open(journal, "a") as f:
                f.write(f"{self.command} {self.path}\n")
            self.send_response(200)
            self.send_header("Content-Length", "2")
            self.end_headers()
            self.wfile.write(b"{}")
        do_DELETE = do_PUT = do_GET = _r
    ThreadingHTTPServer(("127.0.0.1", int(port)), G).serve_forever()


def lanceur(a):
    c = a[0]
    if c == "secret":
        s = secrets.token_bytes(32)
        fd = os.open(a[1], os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        os.write(fd, s)
        os.close(fd)
        print(json.dumps({"secret_sha256": hashlib.sha256(s).hexdigest()}))
    elif c == "generer":
        sortie, texte = arg(a, "--sortie"), arg(a, "--texte-sha256")
        phrase = open(arg(a, "--phrase-fichier"), "rb").read()
        mondes = [{"monde": r, "spec": {"factice": r, "p": hashlib.sha256(phrase).hexdigest()[:8]}} for r in range(1, 21)]
        for w in mondes:
            w["spec_sha256"] = hashlib.sha256(json.dumps(w["spec"], sort_keys=True).encode()).hexdigest()
        b = json.dumps({"version": "doublure", "texte_sha256": texte, "public": False, "mondes": mondes}, sort_keys=True).encode()
        fd = os.open(sortie, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        os.write(fd, b)
        os.close(fd)
        h = hashlib.sha256(b).hexdigest()
        e = {"version": "doublure", "texte_sha256": texte, "fichier_mondes_sha256": h, "public": False,
             "mondes_sha256": [w["spec_sha256"] for w in mondes]}
        fd = os.open(sortie + ".engagement.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        os.write(fd, json.dumps(e).encode())
        os.close(fd)
        print(json.dumps({"fichier_mondes_sha256": h, "controles": [{"monde": r, "conforme": True, "spec_sha256": w["spec_sha256"]}
                                                                   for r, w in zip(range(1, 21), mondes)]}))
    elif c == "preparer":
        print(json.dumps({"c16_admises": True, "gabarit_g0_sha256": "e77d3041f7815b2c0579cbafdb2898ca8569fe61e6cb51b99a41c3724fc456a2",
                          "mondes": {str(r): {"octets_g2_pire": 49200} for r in range(1, 21)}}))
    elif c == "jouer":
        s = arg(a, "--sortie")
        os.makedirs(os.path.join(s, "prive"))
        open(os.path.join(s, "prive", "texte-g0-monde-1.txt"), "w").write("texte servi factice")
        ecrire_scelle(os.path.join(s, "releve-crible-iii-v1.json"), {"doublure": True})
        print(json.dumps({"mode": arg(a, "--mode"), "comptes": {"complet": 100, "tronque": 0, "echec": 0, "non appele": 0},
                          "complets": 20, "arret": None}))
    elif c == "rapatrier":
        src, dst = arg(a, "--source"), arg(a, "--destination")
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("prive"))
        print(json.dumps({"aucun_monde": True}))
    else:
        print("doublure : sous-commande inconnue", file=sys.stderr)
        return 2
    return 0


def main(a):
    if a[0] == "loueur":
        loueur(a[1], a[2])
    elif a[0] == "lanceur":
        return lanceur(a[1:])
    elif a[0] == "mesure":
        t = os.path.dirname(arg(a, "--sortie"))
        print(json.dumps({"programme_sha256": hashlib.sha256(open(os.path.join(t, "code", "mesure_crible_iii_v1.py"), "rb").read()).hexdigest()}))
    elif a[0] == "lire":
        ecrire_scelle(arg(a, "--ecrire"), {"doublure": True, "verdicts": {}})
        print("{}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
