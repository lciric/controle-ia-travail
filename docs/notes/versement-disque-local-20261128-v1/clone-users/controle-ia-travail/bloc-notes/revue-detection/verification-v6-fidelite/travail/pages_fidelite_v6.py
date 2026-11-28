"""Contrôles indépendants du vérificateur « fidélité » de la v6 (pas une copie de pagev6.py).

Garde (R5, aucun repli) : chaque PDF lu doit avoir une empreinte complète égale (1) à son compagnon .sha256 posé à côté,
(2) à la référence de la v1 (redaction/citations-synthese-v1.json, lui-même contrôlé par empreinte) ; RO hors JSON :
empreinte complète de la table des clés de la v6. Sinon ARRÊT, code 3.
Recherche : texte de la page par pdftotext (mode par défaut, puis -layout) ; normalisation NFKC, apostrophes et
guillemets ASCII, tirets ramenés à « - », césure de fin de ligne recollée, puis TOUS les blancs retirés des deux côtés
(comparaison insensible aux blancs : différente de pagev6.py, qui réduit les blancs à une espace).
Lignes de table : motif d'expression régulière cherché sur une même ligne du mode -layout.
Lignes de fichier : empreinte complète d'abord, puis extrait cherché dans la ligne citée (ou la plage citée).
Usage : python3 -I -B pages_fidelite_v6.py            (tous les contrôles ; code 0 si conformes)
        python3 -I -B pages_fidelite_v6.py --page CLE P [layout]
"""
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

RD = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection")
S = RD.parent
R = Path("/home/user/controle-ia-travail")
D = R / "docs/sources/pdf"
C6 = RD / "correction-v6/pdf"
JSON_V1 = RD / "redaction/citations-synthese-v1.json"
JSON_V1_SHA = "2186860541680a114add5f71c27895e8eba2d614ff2a2aa671756fff7355692c"
IDS = {"AP": "2502.03407v1", "PAR": "2507.12691v3", "BX": "2509.21344v2", "KU": "2605.27958v1", "CA": "2610.12445v1",
       "DYL": "2606.12618v2", "LB": "2511.16035v2", "K": "2511.17408v4", "MA": "2503.10965v2", "BU": "2407.12831v2",
       "LIAR": "2309.15840v1", "FQ": "2312.10029v2", "AU": "2504.04072v3", "RH": "2609.19101v2", "CC": "2601.04603v1"}
DANS_D = {"AP", "PAR", "BX", "KU", "CA"}


def arret(m):
    print("ARRÊT : " + m)
    sys.exit(3)


_refs = None


def refs(json_v1=JSON_V1):
    global _refs
    if _refs is None:
        b = Path(json_v1).read_bytes()
        if hashlib.sha256(b).hexdigest() != JSON_V1_SHA:
            arret("référence v1 altérée")
        _refs = {k: v["sha256"] for k, v in json.loads(b)["pdfs"].items()}
    return _refs


def chemin(cle, racine_c6=C6):
    i = IDS[cle]
    return D / f"{i}.pdf" if cle in DANS_D else Path(racine_c6) / i / f"{i}.pdf"


_vu = {}


def garde(cle, racine_c6=C6):
    p = chemin(cle, racine_c6)
    if str(p) in _vu:
        return p
    if not p.is_file():
        arret(f"PDF absent : {p}")
    c = p.with_name(p.name + ".sha256")
    if not c.is_file():
        arret(f"compagnon absent : {c}")
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    champs = c.read_text().split()
    if champs[:2] != [h, p.name]:
        arret(f"{cle} : empreinte {h[:12]}… différente du compagnon {champs[:1]}")
    if h != refs()[cle]:
        arret(f"{cle} : empreinte {h[:12]}… différente de la référence v1 {refs()[cle][:12]}…")
    _vu[str(p)] = h
    return p


def page(cle, n, layout=False, racine_c6=C6):
    p = garde(cle, racine_c6)
    r = subprocess.run(["pdftotext", *(["-layout"] if layout else []), "-f", str(n), "-l", str(n), str(p), "-"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        arret(f"pdftotext {cle} p. {n}")
    return r.stdout


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"), ("−", "-"), ("­", "")):
        s = s.replace(a, b)
    s = re.sub(r"(?<=[a-z])-\n(?=[a-z])", "", s)
    return re.sub(r"\s+", "", s)


def present(cle, n, phrase):
    return any(norm(phrase) in norm(page(cle, n, lay)) for lay in (False, True))


def ligne_table(cle, n, motif):
    return any(re.search(motif, l) for l in page(cle, n, True).splitlines())


# (étiquette, clé, page, phrase) : phrases des passages changés de la v6 (ligne de la v6 entre crochets)
PHRASES = [
    ("01 VV5-fidelite-01 [l. 432-433] 0,5 de l'organisme affiné", "BX", 8, "from almost perfect detection 0.94 to chance performance 0.5"),
    ("02 VV5-fidelite-01 [l. 433] sondes réentraînées sur lui", "BX", 8, "re-training probes on the Model Organism using contrastive pairs"),
    ("03 VV5-fidelite-01 [l. 431-432] 0,81, BX p. 5", "BX", 5, "degraded by 14 points to 0.81 AUROC"),
    ("04 VV5-fidelite-01 [l. 431-432] 0,63, BX p. 6", "BX", 6, "32-point drop to 0.63 AUROC"),
    ("05 VV5-sens-04 (1) [l. 195] conversation ordinaire", "BX", 6, "distinguish transcripts containing normal conversational data from those exhibiting the studied behavior"),
    ("06 VV5-sens-04 (1) [l. 195] rappel à 1 % de faux positifs", "BX", 6, "recall at fixed 1% FPR"),
    ("07 VV5-sens-04 (2) [l. 202] table 9 = Varied Deception", "DYL", 28, "Balanced accuracy on Varied Deception"),
    ("08 VV5-sens-04 (2), 11 [l. 202, 133] la question tient sur Gender Secret remis sur consigne", "DYL", 11, "DYL, by contrast, retains strong performance on the prompted variants"),
    ("09 VV5-sens-04 (2), 11 [l. 202, 133] Apollo bas sur les variantes sur consigne", "DYL", 11, "Apollo and Unrelated Questions perform poorly even on the prompted variants"),
    ("10 VV5-sens-11 [l. 133-134] questions témoins : âge ou couleur des cheveux", "DYL", 7, "whether it knows the user's age or hair colour"),
    ("11 VV5-sens-11 [l. 133-134] raisonnement avant la réponse (p. 8)", "DYL", 8, "reasoning tokens before the yes/no response"),
    ("12 VV5-sens-10 [l. 302] hypothèse Instructed-Pairs", "AP", 18, "activates somewhat when deception is incentivized (rather than performed)"),
    ("13 VV5-sens-10 [l. 302] contre les réponses témoins", "AP", 18, "which still allows the probe to distinguish deceptive responses from control responses"),
    ("14 VV5-sens-10 [l. 302] témoin = Alpaca (p. 5)", "AP", 5, "Alpaca dataset"),
    ("15 VV5-sens-06 [l. 393] régime de consigne, KU p. 5", "KU", 5, "regime"),
    ("16 VV5-sens-12 (1) [l. 304] colonnes de la table 3", "PAR", 7, "Backdoors"),
    ("17 VV5-sens-12 (2) [l. 394] table 9 page 28", "DYL", 28, "Table 9"),
    ("18 VV5-sens-04 (2) [l. 202] Gender Secret remis sur la consigne d'origine", "DYL", 11, "original system prompts"),
]
# (étiquette, clé, page, motif sur une ligne -layout)
TABLES = [
    ("19 VV5-fidelite-01 [l. 432] Full Averaging (Pairs), 5e colonne 0,964", "PAR", 7, r"Full Averaging \(Pairs\)\s+0\.966\s+0\.931\s+0\.844\s+0\.999\s+0\.964"),
    ("20 VV5-sens-12 (1) [l. 304] Deception No (Pairs), Backdoors 0,832", "PAR", 7, r"Deception No \(Pairs\)\s+\S+\s+\S+\s+0\.832\b"),
    ("21 VV5-sens-12 (1) [l. 304] Honest Yes (Pairs), Backdoors 0,849", "PAR", 7, r"Honest Yes \(Pairs\)\s+\S+\s+\S+\s+0\.849\b"),
    ("22 VV5-sens-12 (1) [l. 304] Peak Activation (Pairs), Backdoors 0,768", "PAR", 7, r"Peak Activation \(Pairs\)\s+\S+\s+\S+\s+0\.768\b"),
    ("23 VV5-sens-12 (1) [l. 304] ordre des colonnes : Backdoors 3e", "PAR", 7, r"AI Liar\s+Dilution\s+Backdoors"),
    ("24 VV5-sens-04 (1) [l. 195] table 1 : Sandbagging 1.00 0.04 0.03", "BX", 6, r"Sandbagging\s+1\.00\s+0\.04\s+0\.03\b"),
    ("25 VV5-sens-12 (2) [l. 394] Qwen3-8B : Apollo 0,74, question 0,69", "DYL", 28, r"Qwen3-8B\s+\d+\s+0\.74\s+0\.69\b"),
    ("26 VV5-sens-12 (2) [l. 394] Qwen3-4B : Apollo 0,64, question 0,68", "DYL", 28, r"Qwen/Qwen3-4B\s+\d+\s+0\.64\s+0\.68\b"),
]
ARTEFACTS_P = [
    ("a1 chiffre changé 0.5 → 0.6", "BX", 8, "from almost perfect detection 0.94 to chance performance 0.6"),
    ("a2 page voisine (p. 9)", "BX", 9, "re-training probes on the Model Organism using contrastive pairs"),
    ("a3 mot changé control → Alpaca", "AP", 18, "which still allows the probe to distinguish deceptive responses from alpaca responses"),
    ("a4 page voisine (DYL p. 10)", "DYL", 10, "DYL, by contrast, retains strong performance on the prompted variants"),
    ("a5 mot changé age → gender", "DYL", 7, "whether it knows the user's gender or hair colour"),
    ("a6 mauvaise clé (PAR au lieu de DYL)", "PAR", 28, "Balanced accuracy on Varied Deception"),
]
ARTEFACTS_T = [
    ("a7 colonne voisine (0,832 en 4e colonne)", "PAR", 7, r"Deception No \(Pairs\)\s+\S+\s+\S+\s+\S+\s+0\.832\b"),
    ("a8 colonnes permutées Qwen3-8B 0.69 0.74", "DYL", 28, r"Qwen3-8B\s+\d+\s+0\.69\s+0\.74\b"),
    ("a9 chiffre changé Sandbagging 0.30", "BX", 6, r"Sandbagging\s+1\.00\s+0\.04\s+0\.30\b"),
]

# Lignes de fichiers : (étiquette, chemin ou git:, empreinte complète, (première, dernière ligne), extrait)
P015 = (R / "docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md", "6e74c6cbcd3b05ab65dbbf42fc6481520a6717ec1e40e0961a633c5ed76a19d2")
T06 = (R / "brouillons/T0.6-organismes-v0-v1-brouillon1.md", "e212fb3505907c8e48524784fbf5a78f6e9120dc86361a35c6ca994af76a0449")
P011 = (R / "docs/decisions/proposition-P-011-T0.7-sondes-v1.md", "64afff19ce5ceab6f99e3f15d583fcdc3890e08a480a017703f2a57331636fd9")
PP = (R / "prereg/P3-premier-test-i-a-v1.md", "d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672")
REP = (S / "brainstorm-outils-p3/reponse-claude-prompt-unique-v1.md", "f9aa165563aa2e63cdca7e2e388b12d271c2e574b81f126e9909cad9d109d34e")
CR = (S / "p3b/consigne-redacteur-P3b-brouillon1-v1.md", "f8305c0ebea6ef22ada99752381e9a9bfdd1dad2f0d4b174a01c0964f6cb225b")
AT = (S / "p3b/a-transmettre-contre-lecture-P3b-v1.md", "23c742befb2f89dc698a0bb5f9f518e544e71b3b98733f5258a481659fe491c0")
CL = (S / "p3b/consigne-contre-lecture-R2-P3b-brouillon1-v1.md", "138b3afd6f09d954786443dd374e74d84fa340f9522b87e7f511e91636123f40")
DEC = ("git:registres/decisions.md", "e8b73c6425ad6493c6aaf8083bad98fccc8958fcd6ac08acb4948b0224b2a1a6")
GO = ("git:registres/go.md", "1a392407391cef6ee501e61e90cb5bf73da8aec343f3e44da1c96fd67639f5d6")
LIGNES = [
    ("L01 VV5-sens-01/02 [P] l. 123 coût trois fois", PP, (123, 123), "trois fois"),
    ("L02 VV5-sens-01/02 [P] l. 330-331 coût gonflé, p = 1, forte", PP, (330, 331), "coût gonflé"),
    ("L03 idem, p = 1", PP, (330, 331), "p = 1"),
    ("L04 VV5-sens-06 [P] l. 238-240 : 2 fois la médiane", PP, (238, 240), "2 fois la médiane"),
    ("L05 VV5-sens-06 [P] l. 238-240 : 1,25", PP, (238, 240), "1,25"),
    ("L06 VV5-sens-06 [P] l. 238-240 : 10 actions", PP, (238, 240), "10"),
    ("L07 VV5-sens-07 [P] l. 249-253 quintiles du coût déclaré", PP, (249, 253), "quintiles"),
    ("L08 VV5-sens-09 [P] l. 275-277 Bonferroni deux sondes", PP, (275, 277), "Bonferroni sur les deux sondes"),
    ("L09 VV5-sens-05 P-015 l. 36-39 seuil boîte noire", P015, (36, 39), "seuil du meilleur moniteur boîte noire"),
    ("L10 VV5-sens-05 P-015 l. 50 règle du coût", P015, (50, 50), "coût déclaré"),
    ("L11 VV5-sens-01 P-015 l. 147 descriptif de T0.7", P015, (147, 147), "descriptif de T0.7"),
    ("L12 VV5-sens-01 P-015 l. 65-66 réplication de P3", P015, (65, 66), "réplication de P3 sur des épisodes neufs"),
    ("L13 VV5-sens-01 P-015 l. 18-19 dose avant toute sonde", P015, (18, 19), "avant toute lecture de sonde"),
    ("L14 VV5-sens-02 P-015 l. 33-34 affaiblir les contrôles sort", P015, (33, 34), "Affaiblir les contrôles"),
    ("L15 VV5-sens-13 P-015 l. 40 dose réalisée", P015, (40, 40), "dose réalisée"),
    ("L16 VV5-sens-01 P-015 l. 121 576 épisodes", P015, (121, 121), "576"),
    ("L17 VV5-sens-01 P-015 l. 124 7 à 9 USD", P015, (124, 124), "7 à 9 USD"),
    ("L18 VV5-sens-06 P-015 l. 138-141 jeu de la v3", P015, (138, 141), "paires synthétiques"),
    ("L19 VV5-sens-02 brouillon T0.6 l. 28 affaiblir", T06, (28, 28), "affaiblir les contrôles"),
    ("L20 VV5-sens-02 brouillon T0.6 l. 75 (i-a)", T06, (75, 75), "(i-a)"),
    ("L21 VV5-sens-06 P-011 l. 35 paires synthétiques", P011, (35, 35), "synthétiques"),
    ("L22 VV5-sens-06 P-011 l. 63 sous-agent neuf", P011, (63, 63), "sous-agent neuf"),
    ("L23 VV5-sens-03 réponse l. 57-62 quatre contextes", REP, (57, 62), "quatre contextes"),
    ("L24 VV5-sens-03 réponse l. 57-62 nombre prévu", REP, (57, 62), "prévu"),
    ("L25 VV5-sens-07 réponse l. 104 tâche régressés", REP, (104, 104), "régressés"),
    ("L26 VV5-sens-07 réponse l. 128 tâches bon marché", REP, (128, 128), "bon marché"),
    ("L27 VV5-sens-03 consigne P3b l. 23-26 (B) et (C) hors périmètre", CR, (23, 26), "P-017 (B) et (C)"),
    ("L28 VV5-sens-07 consigne P3b l. 36 test résiduel", CR, (36, 36), "test résiduel"),
    ("L29 VV5-sens-09 consigne P3b l. 54 renvoi à la v4", CR, (54, 54), "v4"),
    ("L30 VV5-sens-09 contre-lecture l. 15-16 note", CL, (15, 16), "a-transmettre-contre-lecture-P3b-v1.md"),
    ("L31 VV5-sens-09 note : VV4-sens-11 choix neuf", AT, (1, 40), "choix neuf, à justifier, pas une reprise de P3"),
    ("L32 VV5-fidelite-04 R-293 l. 493", DEC, (493, 493), "R-293"),
    ("L33 VV5-fidelite-04 R-293 : P4", DEC, (493, 493), "chaîne v2 de P4"),
    ("L34 VV5-fidelite-05 R-299 l. 499 corrections de R-295", DEC, (499, 499), "Corrections de R-295"),
    ("L35 VV5-sens-13 R-303 l. 503 réserve B1", DEC, (503, 503), "reserve_B1_ampleur_au_dela_de_la_consigne"),
    ("L36 VV5-sens-09 R-306 l. 506 consigne inchangée", DEC, (506, 506), "inchangée"),
    ("L37 VV5-sens-08 R-296 l. 496 double comptabilité", DEC, (496, 496), "R-296"),
    ("L38 VV5-sens-08 R-295 l. 495 J-lens", DEC, (495, 495), "J-lens"),
    ("L39 VV5-sens-08 go.md l. 38 GO-2026-10-20-10", GO, (38, 38), "GO-2026-10-20-10"),
    ("L40 VV5-sens-01 go.md GO-2026-10-20-07, borne 10 USD", GO, (35, 35), "GO-2026-10-20-07"),
    ("L41 VV5-sens-03 P-017 l. 394 rejeu", DEC, (394, 394), "P-017"),
    ("L42 VV5-sens-07 N-030 l. 396", DEC, (396, 396), "N-030"),
]
ARTEFACTS_L = [
    ("aL1 ligne voisine (P-015 l. 146 au lieu de 147)", P015, (146, 146), "descriptif de T0.7"),
    ("aL2 chiffre changé (8 à 9 USD)", P015, (124, 124), "8 à 9 USD"),
    ("aL3 mot changé (reserve_B2)", DEC, (503, 503), "reserve_B2_ampleur_au_dela_de_la_consigne"),
    ("aL4 ligne voisine ([P] l. 278-280)", PP, (278, 280), "Bonferroni sur les deux sondes"),
]

_lignes = {}


def lignes(src):
    nom, att = str(src[0]), src[1]
    if nom not in _lignes:
        if nom.startswith("git:"):
            b = subprocess.run(["git", "-C", str(R), "show", "9ecd952:" + nom[4:]], capture_output=True,
                               check=True).stdout
        else:
            b = Path(nom).read_bytes()
        h = hashlib.sha256(b).hexdigest()
        if h != att:
            arret(f"{nom} : empreinte {h[:12]}… attendue {att[:12]}…")
        _lignes[nom] = b.decode("utf-8").splitlines()
    return _lignes[nom]


def dans(src, a, z, ex):
    return re.sub(r"\s+", " ", ex) in re.sub(r"\s+", " ", " ".join(lignes(src)[a - 1:z]))


def main():
    a = sys.argv[1:]
    if a and a[0] == "--page":
        print(page(a[1], int(a[2]), len(a) > 3))
        return
    fautes = 0
    print("# Empreintes (compagnon et référence v1)")
    for cle in sorted(IDS):
        p = garde(cle)
        print(f"empreinte égale | {cle} | {p.name} | {_vu[str(p)]}")
    print("# Phrases à la page citée")
    for e, cle, n, ph in PHRASES:
        r = present(cle, n, ph)
        fautes += not r
        print(f"{'TROUVÉ' if r else 'ABSENT'} | {e} | {cle} p. {n} | {ph[:80]!r}")
    for e, cle, n, mo in TABLES:
        r = ligne_table(cle, n, mo)
        fautes += not r
        print(f"{'TROUVÉ' if r else 'ABSENT'} | {e} | {cle} p. {n} | {mo[:80]!r}")
    print("# Lignes citées (empreinte complète d'abord)")
    for e, src, (x, y), ex in LIGNES:
        r = dans(src, x, y, ex)
        fautes += not r
        print(f"{'TROUVÉ' if r else 'ABSENT'} | {e} | {Path(src[0]).name} l. {x}-{y} | {ex[:60]!r}")
    print("# Épreuve R5 : artefacts (chacun doit être rejeté)")
    for e, cle, n, ph in ARTEFACTS_P:
        r = present(cle, n, ph)
        fautes += r
        print(f"{'ACCEPTÉ (faute)' if r else 'rejeté'} | {e}")
    for e, cle, n, mo in ARTEFACTS_T:
        r = ligne_table(cle, n, mo)
        fautes += r
        print(f"{'ACCEPTÉ (faute)' if r else 'rejeté'} | {e}")
    for e, src, (x, y), ex in ARTEFACTS_L:
        r = dans(src, x, y, ex)
        fautes += r
        print(f"{'ACCEPTÉ (faute)' if r else 'rejeté'} | {e}")
    print(f"# BILAN : {fautes} faute(s)")
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
