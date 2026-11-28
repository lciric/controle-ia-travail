"""Contrôle des « mots exacts » : pour chaque plage de lignes d'un rapport, extrait les segments entre guillemets
français de premier niveau (≥ 50 caractères) et les cherche dans le brouillon 6, espaces normalisés.
Un marqueur <<…>> du segment vaut n'importe quel texte ; « réserve 14 » vaut « réserve 1[4-6] »."""
import re, sys, unicodedata
P = sys.argv[1]
B6 = open(f"{P}/brouillon6/papier-C-preenregistrement-HC1-HC3-v1-brouillon6.md", encoding="utf-8").read()
def norm(s):
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r"\n\s*(?:>\s*)?(?:-\s+)?", " ", s)
    s = s.replace("**", "")
    return re.sub(r"\s+", " ", s).strip()
B6n = norm(B6)
C = f"{P}/contre-lectures-brouillon5"
plages = {
 "texte": (f"{C}/texte/contre-lecture-R2-brouillon5-texte-v1.md", [(72,77),(86,89),(103,110),(121,123),(132,137),(185,188),(196,197),(201,204),(208,210),(214,222)]),
 "methode": (f"{C}/methode/contre-lecture-R2-brouillon5-methode-v1.md", [(129,151),(172,182),(203,209),(224,230),(242,246),(265,278),(292,296),(306,315),(324,325),(333,337),(344,345),(350,350)]),
 "voisins": (f"{C}/voisins/lecture-voisins-joswin-huqu-v1.md", [(229,244),(246,254),(285,309),(315,317),(324,328),(334,339),(344,347),(354,360)]),
 "panin": (f"{C}/voisins-panin/lecture-voisins-panin-sept-v1.md", [(160,200)]),
 "second": (f"{C}/voisins-second-rang/lecture-voisins-second-rang-v1.md", [(337,343),(353,357),(358,369),(377,385),(393,395)]),
 "cp02": (f"{C}/voisins-cp02/lecture-voisins-cp02-v1.md", [(331,436)]),
 "restants": (f"{C}/voisins-restants/lecture-voisins-restants-v1.md", [(280,394)]),
 "courte": (f"{C}/contre-lecture-courte-voisins/contre-lecture-courte-notes-voisins-v1.md", [(134,181)]),
 "cv203": (f"{C}/voisins-cv2-03/lecture-voisins-cv2-03-v1.md", [(211,276),(320,326)]),
}
def segments(t):
    out, prof, debut = [], 0, None
    for i, ch in enumerate(t):
        if ch == "«":
            if prof == 0: debut = i + 1
            prof += 1
        elif ch == "»" and prof > 0:
            prof -= 1
            if prof == 0: out.append(t[debut:i])
    return out
def motif(seg):
    s = norm(seg)
    parts = re.split(r"(<<[A-Z0-9_]+>>)", s)
    rx = ""
    for p in parts:
        if re.fullmatch(r"<<[A-Z0-9_]+>>", p): rx += r".{1,400}?"
        else: rx += re.escape(p).replace(r"réserve\ 14", r"réserve\ 1[4-6]")
    return rx
tot = trouve = 0
for nom, (f, pl) in plages.items():
    L = open(f, encoding="utf-8").read().split("\n")
    for a, b in pl:
        t = "\n".join(L[a-1:b])
        for seg in segments(t):
            sn = norm(seg)
            if len(sn) < 50: continue
            tot += 1
            ok = re.search(motif(seg), B6n) is not None
            trouve += ok
            if not ok:
                print(f"ABSENT {nom} l.{a}-{b} ({len(sn)} c.) : {sn[:150]}…")
print(f"segments ≥ 50 caractères : {tot} ; trouvés : {trouve} ; absents : {tot - trouve}")
