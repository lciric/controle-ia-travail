import subprocess, sys
REF = "origin/canal/conv-audit-n04"
E = "brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/"
PP = E + "pre-pilote-course-2-v1/"
B7 = PP + "preenregistrement-pre-pilote-course-2-brouillon7.md"
SPEC = [
 (3, "prereg/preenregistrement-bisociation-deux-espaces-v2.md", [(283,300),(555,586),(617,688),(689,735)]),
 (4, B7, [(1,78)]), (5, B7, [(283,283),(296,296)]), (6, B7, [(336,360)]), (7, B7, [(543,585)]), (8, B7, [(619,619)]), (9, B7, [(639,None)]),
 (11, "docs/notes/ideation-organisme-v1/course-2/devis-course-2-et-pre-pilote-v6.md", [(20,36),(184,232),(370,443)]),
 (12, PP + "contre-lecture-annexe-bras-meta-v1-brouillon1.md", [(19,22),(49,87),(125,None)]),
 (13, PP + "annexe-bras-meta-v1-brouillon1.md", [(18,30),(85,102),(116,224)]),
 (14, "docs/notes/ideation-organisme-v1/contre-lecture-cl19-orchestrateur-v54-v1.md", [(14,22),(100,114),(149,172)]),
 (15, "docs/notes/ideation-organisme-v1/orchestrateur-v55/LISEZMOI-orchestrateur-pole-v7-v55.md", [(65,105)]),
 (16, "docs/notes/ideation-organisme-v1/orchestrateur-v54/LISEZMOI-orchestrateur-pole-v7-v54.md", [(95,116)]),
 (17, "prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon3.md", [(9,101),(166,176),(359,394),(687,698)]),
 (18, "docs/notes/bisociation-litterature-reelle-v1/collisionneur-bisociation-lot-v1/synthese-bisociation-lot-v2.md", [(22,40),(83,83),(164,249),(250,262)]),
 (20, "docs/notes/ideation-organisme-v1/contre-lecture-cl18-orchestrateur-v53-v1.md", [(35,35),(156,156)]),
]
for n, p, rr in SPEC:
    L = subprocess.run(["git","show",f"{REF}:{p}"],capture_output=True,text=True,check=True).stdout.split("\n")
    for a,b in rr:
        b = b or len(L)
        def ctx(i): return L[i-1][:110].replace("\n"," ") if 0 < i <= len(L) else "<hors fichier>"
        print(f"#{n} {a}-{b} /{len(L)}")
        print(f"   avant  {a-1}: {ctx(a-1)}")
        print(f"   début  {a}: {ctx(a)}")
        print(f"   fin    {b}: {ctx(b)}")
        print(f"   après  {b+1}: {ctx(b+1)}")
