"""Recalculs depuis les PDF empreintes (Wang K. et al. 2508.02087v4 ; Poonia et Jain, Findings EMNLP 2025).
Usage : python3 -I -B recalculs_cv2_03_v1.py PDF_WANG SHA_WANG PDF_POONIA SHA_POONIA
Le script verifie l'empreinte de chaque PDF, extrait lui-meme le texte (pdftotext -raw, une page) et lit les tableaux
dans ce texte. Aucun repli : toute valeur introuvable ou toute empreinte differente arrete le script (code 1)."""
import hashlib, re, subprocess, sys

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def page(pdf, n):
    return subprocess.run(["pdftotext", "-raw", "-f", str(n), "-l", str(n), pdf, "-"], capture_output=True,
                          text=True, check=True).stdout

def arret(msg):
    print("ARRET : " + msg)
    sys.exit(1)

MODELES = ["Qwen2.5 7B-Instruct", "Llama3.1 8B-Instruct", "Mistral 7B-Instruct", "Pythia 6.9B",
           "OLMoE 1B-7B Instruct", "OPT 6.7B", "Falcon 7B"]
NIVEAUX = ["Beginner", "Intermediate", "Advanced"]

def lire_tableau(texte, debut, fin):
    i = texte.find(debut)
    j = texte.find(fin, i + 1) if fin else len(texte)
    if i < 0 or j < 0:
        arret("tableau introuvable : " + debut)
    bloc = texte[i:j]
    res = {}
    for niv in NIVEAUX:
        k = bloc.find("\n" + niv + "\n")
        if k < 0:
            arret("niveau introuvable : %s dans %s" % (niv, debut))
        sous = bloc[k:]
        for m in MODELES:
            r = re.search(re.escape(m) + r" ([0-9.]+) ([0-9.]+) ([0-9.]+)", sous)
            if not r:
                arret("ligne introuvable : %s %s %s" % (debut, niv, m))
            res[(niv, m)] = tuple(float(x) for x in r.groups())
    return res

def main():
    pdf_w, sha_w, pdf_p, sha_p = sys.argv[1:5]
    for p, s in ((pdf_w, sha_w), (pdf_p, sha_p)):
        if sha(p) != s:
            arret("empreinte differente : " + p)
    p12 = page(pdf_w, 12)
    t2 = lire_tableau(p12, "Table 2: Model Performance Across Expertise Levels", "Table 3:")
    t3 = lire_tableau(p12, "Table 3: Model Performance Across Expertise Levels", None)

    print("== Wang K. : ecart des taux de complaisance entre niveaux (premiere personne, tableau 2, p. 12)")
    print("   affirmation des auteurs, p. 4 : 'within 4.4% for any given model'")
    for m in MODELES:
        v = [t2[(n, m)][1] for n in NIVEAUX]
        e = max(v) - min(v)
        print("   %-22s Beginner %.2f  Intermediate %.2f  Advanced %.2f  ecart %.2f %s" % (
            m, v[0], v[1], v[2], e, "AU-DELA de 4,4" if e > 4.4 + 1e-9 else ""))

    # Figure 2, p. 4 : taux de complaisance sous 'Opinion-only' (valeurs imprimees sur la figure, une decimale).
    p4 = page(pdf_w, 4)
    fig2 = {"Qwen2.5 7B-Instruct": "46.8", "Llama3.1 8B-Instruct": "49.0", "Mistral 7B-Instruct": "61.0",
            "Pythia 6.9B": "46.6", "OLMoE 1B-7B Instruct": "81.5", "OPT 6.7B": "65.8", "Falcon 7B": "95.1"}
    ligne = re.sub(r"\s+", " ", p4)
    sequence = " ".join(fig2[m] for m in MODELES)
    if sequence not in ligne:
        arret("sequence de la figure 2 introuvable a la p. 4 : " + sequence)
    print("== Wang K. : 'Opinion-only' (figure 2, p. 4 ; sequence trouvee telle quelle : %s)" % sequence)
    print("   moyenne des sept : %.2f (auteurs, p. 3 : 63.7 ; etendue 46.6 a 95.1)" % (
        sum(float(fig2[m]) for m in MODELES) / 7))
    print("== Wang K. : premiere personne avec expertise moins 'Opinion-only' (points de pourcentage)")
    for m in MODELES:
        d = [t2[(n, m)][1] - float(fig2[m]) for n in NIVEAUX]
        print("   %-22s %+.2f  %+.2f  %+.2f   (de %+.2f a %+.2f)" % (m, d[0], d[1], d[2], min(d), max(d)))

    print("== Wang K. : premiere moins troisieme personne (tableaux 2 et 3, p. 12)")
    diffs, adv = [], []
    for n in NIVEAUX:
        for m in MODELES:
            d = t2[(n, m)][1] - t3[(n, m)][1]
            diffs.append(d)
            if n == "Advanced":
                adv.append(d)
    print("   moyenne sur 21 cases : %.2f ; minimum %.2f ; maximum %.2f" % (sum(diffs) / 21, min(diffs), max(diffs)))
    print("   moyenne niveau Advanced seul (7 cases) : %.2f" % (sum(adv) / 7))
    print("   affirmation des auteurs (legende de la figure 8, p. 7) : 'an average incrase of 13.6%, on all expertise levels'")

    print("== Poonia et Jain : sommes des quatre sous-ensembles (tableau 3, p. 8)")
    p8 = re.sub(r"\s+", " ", page(pdf_p, 8))
    paires = ["Asian, Indian", "helpful, Asian", "Asian, Yellow", "White, Black", "good, bad", "Indian, Brown",
              "good, sharp", "African, British", "helpful, White", "dumb, bad"]
    for pr in paires:
        r = re.search(re.escape(pr) + r" (\d+) (\d+) (\d+) (\d+)", p8)
        if not r:
            arret("ligne introuvable au tableau 3 : " + pr)
        c = [int(x) for x in r.groups()]
        print("   %-18s %s somme %d" % (pr, c, sum(c)))
    p1 = re.sub(r"\s+", " ", page(pdf_p, 1))
    if "which contains 14,024" not in p1:
        arret("'which contains 14,024' introuvable a la p. 1")
    print("   affirmation des auteurs, p. 1 : 'which contains 14,024' (questions)")
    print("FIN : toutes les valeurs lues dans les PDF empreintes")

if __name__ == "__main__":
    main()
