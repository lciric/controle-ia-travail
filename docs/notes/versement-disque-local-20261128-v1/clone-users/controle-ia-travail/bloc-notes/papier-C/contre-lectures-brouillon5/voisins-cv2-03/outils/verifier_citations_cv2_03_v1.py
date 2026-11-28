"""Controle des citations de la note des voisins CV2-03, a la page du PDF empreinte (R5, R7).
Usage : python3 -I -B verifier_citations_cv2_03_v1.py RACINE FICHIER_CITATIONS.json
RACINE : dossier voisins-cv2-03 ; chemins du fichier JSON relatifs a RACINE.
Pour chaque citation : (1) empreinte sha256 du PDF egale a l'attendue ; (2) citation presente, apres normalisation, dans
la note ; (3) citation presente sur la page citee du PDF (texte extrait ici par pdftotext -raw, une seule page).
Sortie : une ligne par citation, OK ou ECHEC avec motif ; bilan ; code de sortie 1 si au moins un echec. Aucun repli :
une empreinte differente interdit la lecture de la page et compte comme echec."""
import hashlib, json, re, subprocess, sys, unicodedata

PAIRES = [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("«", '"'), ("»", '"'),
          ("–", "-"), ("—", "-"), ("−", "-"), (" ", " "), (" ", " "), ("``", '"'),
          ("''", '"')]

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in PAIRES:
        s = s.replace(a, b)
    return s

def espaces(s):
    return re.sub(r"\s+", " ", s).strip()

def variantes_page(texte):
    t = norm(texte)
    garde = espaces(re.sub(r"-\s*\n\s*", "-", t))     # cesure gardee : "Opinion-only" coupe en fin de ligne
    retire = espaces(re.sub(r"-\s*\n\s*", "", t))     # cesure retiree : "syco-\nphancy" -> "sycophancy"
    brut = espaces(t)                                  # tiret suivi d'un saut de ligne garde comme espace : "S3 -\nquestions"
    return garde, retire, brut

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def page(pdf, n):
    return subprocess.run(["pdftotext", "-raw", "-f", str(n), "-l", str(n), pdf, "-"], capture_output=True,
                          text=True, check=True).stdout

def main():
    racine, fichier = sys.argv[1], sys.argv[2]
    with open(fichier, encoding="utf-8") as f:
        spec = json.load(f)
    with open(racine + "/" + spec["note"], encoding="utf-8") as f:
        note = espaces(norm(f.read()))
    total = echecs = 0
    for src in spec["sources"]:
        pdf = racine + "/" + src["pdf"]
        h = sha(pdf)
        ok_h = (h == src["sha256"])
        cache = {}
        for c in src["citations"]:
            total += 1
            q = espaces(norm(c["texte"]))
            motifs = []
            if not ok_h:
                motifs.append("empreinte du PDF differente (%s...)" % h[:12])
            if q not in note:
                motifs.append("absente de la note")
            if ok_h:
                n = c["page"]
                if n not in cache:
                    cache[n] = variantes_page(page(pdf, n))
                if all(q not in v for v in cache[n]):
                    motifs.append("absente de la page %d" % n)
            if motifs:
                echecs += 1
            print("%s | p. %d | %s | %s" % (src["id"], c["page"], "OK" if not motifs else "ECHEC : " + " ; ".join(motifs),
                                            q[:90]))
    print("BILAN : %d citations, %d echecs" % (total, echecs))
    sys.exit(1 if echecs else 0)

if __name__ == "__main__":
    main()
