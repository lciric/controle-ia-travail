"""Verifie que chaque texte a remplacer ou ancre citee par les corrections de la note figure exactement une fois
(espaces normalises) dans le fichier vise, et que ce fichier a l'empreinte attendue.
Usage : python3 -I -B verifier_ancres_cv2_03_v1.py [--artefact]   (chemins absolus dans la table ANCRES ci-dessous)."""
import hashlib, re, sys
P = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/contre-lectures-brouillon5"
SR = (P + "/voisins-second-rang/lecture-voisins-second-rang-v1.md", "8027bd53f6030d1b289c5ad84c3b501a8c646e22a72f31be6e30a2912a56f81f")
CC = (P + "/contre-lecture-courte-voisins/contre-lecture-courte-notes-voisins-v1.md", "7287498f6e9a342c7bc5cc506feccba82696d935b1412d4b83a363336036149e")
JH = (P + "/voisins/lecture-voisins-joswin-huqu-v1.md", "55222cdb3278f59810586b2097817114c74825cc34b9dd7a12ad2a051a90b84d")
B5 = ("/home/user/controle-ia-travail/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md", "9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969")
ANCRES = [
 ("CW-01 (CS-01)", SR, "; au niveau du résumé, Wang K. et al. 2508.02087 (AAAI 2026), Qu, Fu et Hu 2606.01637 et Poonia et Jain (Findings of EMNLP 2025, `2025.findings-emnlp.1335`). »"),
 ("CW-01 (CV2-03)", CC, "leurs PDF sont à lire avant le scellement (R8), sauf décision écrite de la session de lire la règle au sens strict. »"),
 ("CW-02 (CS-02 a)", SR, "dont le résumé dit « user expertise framing has a negligible impact » sur la complaisance en réponse à des questions ; le chiffre « within 4.4% » et les niveaux d'expertise ne sont connus que par Joswin et al., non vérifiés, non opposables (R7)) »"),
 ("CW-02 (CV-06)", JH, "qui y lisent l'effet minime trouvé par Wang et al. 2026, cité de seconde main, non lu, non opposable)"),
 ("CW-03", B5, "(2511.00554, p. 3 ; 2601.11516, p. 12 ; 2509.21344)"),
 ("CW-04 (Kim et Flanigan)", B5, "Grille publiée la plus proche, citée : autorité et consensus"),
 ("CW-06 (Panin)", B5, "a deference screen must not threshold the outcome"),
 ("CW-07 (CS-09)", SR, "substitution d'activations (Poonia et Jain, Wang K. et al., résumés)."),
 ("CW-08", B5, "Contre-lectures des notes de lecture"),
]
if sys.argv[1:] == ["--artefact"]:   # garde R5 : une ancre saine doit passer, deux alterees doivent echouer
    ANCRES = [("SAIN", B5, "Contre-lectures des notes de lecture"),
              ("ARTEFACT texte altere", B5, "Contre-lectures des notes de lectures"),
              ("ARTEFACT empreinte alteree", (B5[0], B5[1][:-1] + "0"), "Contre-lectures des notes de lecture")]
def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
def esp(s):
    return re.sub(r"\s+", " ", s)
echecs = 0
for nom, (chemin, attendue), a in ANCRES:
    if sha(chemin) != attendue:
        print("ECHEC | %s | empreinte differente" % nom); echecs += 1; continue
    n = esp(open(chemin, encoding="utf-8").read()).count(esp(a))
    ok = (n == 1)
    echecs += (not ok)
    print("%s | %s | %d occurrence(s) | %s" % ("OK" if ok else "ECHEC", nom, n, a[:80]))
print("BILAN : %d ancres, %d echecs" % (len(ANCRES), echecs))
sys.exit(1 if echecs else 0)
