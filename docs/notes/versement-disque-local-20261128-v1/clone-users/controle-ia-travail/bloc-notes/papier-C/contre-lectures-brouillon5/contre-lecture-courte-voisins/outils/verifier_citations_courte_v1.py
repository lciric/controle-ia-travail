"""Controle des citations des notes de voisins, a la page du PDF empreinte (R5, R7).
Usage : python3 -I -B verifier_citations_courte_v1.py RACINE_VOISINS FICHIER_CITATIONS.json
Pour chaque entree : (1) empreinte sha256 du PDF egale a l'attendue ; (2) citation presente, apres normalisation,
dans la note citee ; (3) citation presente sur la page citee du PDF (pdftotext -raw, une page).
Sortie : une ligne par citation, OK ou ECHEC avec le motif ; code de sortie 1 si au moins un echec. Aucun repli."""
import hashlib, json, re, subprocess, sys, unicodedata

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("«", '"'), ("»", '"'),
                 ("–", "-"), ("—", "-"), ("−", "-"), (" ", " "), (" ", " "), ("``", '"'), ("''", '"')]:
        s = s.replace(a, b)
    return s

def variantes(texte):
    t = norm(texte)
    v1 = re.sub(r"\s+", " ", re.sub(r"-\s*\n\s*", "-", t))       # cesure gardee : "Multi-turn"
    v2 = re.sub(r"\s+", " ", re.sub(r"-\s*\n\s*", "", t))        # cesure retiree : "spe-cial" -> "special"
    return v1, v2

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def page(pdf, n):
    return subprocess.run(["pdftotext", "-raw", "-f", str(n), "-l", str(n), pdf, "-"], capture_output=True, text=True,
                          check=True).stdout

def main():
    racine, fichier = sys.argv[1], sys.argv[2]
    with open(fichier, encoding="utf-8") as f:
        spec = json.load(f)
    echecs = total = 0
    cache_notes = {}
    for papier in spec["papiers"]:
        pdf = racine + "/" + papier["pdf"]
        note = racine + "/" + papier["note"]
        h = sha(pdf)
        ok_h = (h == papier["sha256"])
        if note not in cache_notes:
            with open(note, encoding="utf-8") as f:
                cache_notes[note] = re.sub(r"\s+", " ", norm(f.read()))
        texte_note = cache_notes[note]
        for c in papier["citations"]:
            total += 1
            q = re.sub(r"\s+", " ", norm(c["texte"])).strip()
            motifs = []
            if not ok_h:
                motifs.append("empreinte du PDF differente (%s)" % h[:12])
            if q not in texte_note:
                motifs.append("absente de la note")
            if ok_h:
                v1, v2 = variantes(page(pdf, c["page"]))
                if q not in v1 and q not in v2:
                    motifs.append("absente de la page %d" % c["page"])
            etat = "OK" if not motifs else "ECHEC : " + " ; ".join(motifs)
            if motifs:
                echecs += 1
            print("%s | p. %d | %s | %s" % (papier["id"], c["page"], etat, q[:90]))
    print("BILAN : %d citations, %d echecs" % (total, echecs))
    sys.exit(1 if echecs else 0)

if __name__ == "__main__":
    main()
