"""Contrôle des bornes des pièces de la liste A v6 (question v12) : contexte avant, début, fin, après ; lecture au commit d'envoi."""
import subprocess, sys, hashlib
ENVOI = "e5410a42"           # commit d'envoi de la liste A v6 (canal/conv-audit-n04, 12:56 UTC)
TETE = "origin/canal/conv-audit-n04"
MAIN = "origin/main"
P = "brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/"
PP = P + "pre-pilote-course-2-v1/"
B10 = PP + "preenregistrement-pre-pilote-course-2-brouillon10.md"
SR5 = "prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon5.md"
SPEC = [
 ("3", ENVOI, "prereg/preenregistrement-bisociation-deux-espaces-v2.md", [(283,300),(555,586),(617,688),(689,735)]),
 ("4", ENVOI, B10, [(5,17),(18,80)]), ("5", ENVOI, B10, [(254,254)]), ("6", ENVOI, B10, [(412,418)]),
 ("7", ENVOI, B10, [(622,628),(665,667)]), ("8", ENVOI, B10, [(722,732)]),
 ("9", ENVOI, PP + "calcul-puissance-pre-pilote-course-2-v9.sortie.txt", [(182,190)]),
 ("10", ENVOI, PP + "contre-lecture-annexe-bras-meta-v1-brouillon1.md", [(19,22),(49,87),(125,None)]),
 ("11", ENVOI, PP + "annexe-bras-meta-v1-brouillon1.md", [(18,30),(85,102),(116,224)]),
 ("12", ENVOI, "docs/notes/ideation-organisme-v1/contre-lecture-cl19-orchestrateur-v54-v1.md", [(14,22),(100,114),(149,172)]),
 ("13", ENVOI, "docs/notes/ideation-organisme-v1/orchestrateur-v55/LISEZMOI-orchestrateur-pole-v7-v55.md", [(65,105)]),
 ("14", ENVOI, "docs/notes/ideation-organisme-v1/orchestrateur-v54/LISEZMOI-orchestrateur-pole-v7-v54.md", [(95,120)]),
 ("15", ENVOI, SR5, [(9,21),(22,148),(150,157),(158,189)]), ("16", ENVOI, SR5, [(335,355),(666,666)]), ("17", ENVOI, SR5, [(598,627)]),
 ("18", ENVOI, "prereg/brouillons/verification-identification-semi-reel-v1-brouillon5.md", [(14,23)]),
 ("19", MAIN, "docs/notes/bisociation-litterature-reelle-v1/collisionneur-bisociation-lot-v1/synthese-bisociation-lot-v2.md", [(22,40)]),
 ("22", ENVOI, P + "arene-melange-equilibre-v1/preenregistrement-arene-melange-equilibre-v1-brouillon3.md", [(117,151),(434,451)]),
 ("23", ENVOI, P + "arene-melange-equilibre-v1/contre-lecture-arene-melange-v3-brouillon3.md", [(7,10),(61,67)]),
]
def lire(ref, p):
    r = subprocess.run(["git","show",f"{ref}:{p}"],capture_output=True,text=True)
    return r.stdout if r.returncode == 0 else None
for n, ref, p, rr in SPEC:
    t = lire(ref, p)
    if t is None:
        print(f"#{n} ABSENT à {ref} : {p}"); continue
    h = hashlib.sha256(t.encode()).hexdigest()
    note = ""
    if ref == ENVOI:
        t2 = lire(TETE, p)
        note = "inchangé depuis l'envoi" if t2 == t else ("MODIFIÉ DEPUIS L'ENVOI" if t2 is not None else "ABSENT de la tête")
    L = t.split("\n")
    print(f"#{n} {p.split('/')[-1]} ({len(L)} lignes, {h[:8]}…, {note})")
    for a,b in rr:
        b = b or len(L)
        c = lambda i: L[i-1][:105] if 0 < i <= len(L) else "<hors fichier>"
        print(f"   {a}-{b} | avant {a-1}: {c(a-1)}\n          | début {a}: {c(a)}\n          | fin {b}: {c(b)}\n          | après {b+1}: {c(b+1)}")
