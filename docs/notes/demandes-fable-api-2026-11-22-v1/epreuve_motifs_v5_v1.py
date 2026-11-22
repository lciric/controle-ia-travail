"""Épreuve des balises de l'article 4 de pieces-comparaison-essaim-v5.md (voie (b) de la relecture de Fable c1cebee3…).

Opus 5.5, 22 novembre 2026. Ce qui change par rapport à epreuve_motifs_correction_28_v2.py (d1caea7b…), d'après le seul
texte de Fable : l'article 4 ne cherche plus H_A, H_B ni la section (b) (correction 50) ; une piste est un duel balisé
[DUEL n], le tour se clôt par [FIN DES DUELS : n] ; l'épreuve de l'article 9 devient deux lots (correction 51), un lot
aveugle et un lot de huit pièges au verdict fixé d'avance. La règle appliquée est le « code de référence de l'article 4 »
de la relecture, lu par programme dans la relecture (empreinte vérifiée) et exécuté tel quel, non recopié ; ses deux
motifs doivent être identiques à ceux écrits dans l'article 4 de la v5.

Groupes joués (textes et verdicts fixés d'avance dans textes-epreuve-balises-v5-v1.json, scellé avant la première
exécution ; l'auteur des textes a lu la pièce : ce n'est pas le lot aveugle de l'article 9, qui n'est pas joué ici) :
  - cas sains (R5) : les dix textes de l'épreuve v4, balisés selon la forme imposée ; conformes, n = ancien nombre attendu ;
  - pièges (R5, artefacts) : les huit de l'article 9 ;
  - anciens textes sans balise : les dix textes de l'épreuve v4 tels quels ; non conformes attendus (piège 8) ;
  - suppléments, hors épreuve : cas de bord que l'article 4 tranche aussi ; rapportés, non comptés dans le verdict ;
  - mutations (R5) : trois altérations de la règle, chacune doit faire échouer l'épreuve.
Passe (code 0) si sains, pièges et anciens textes rendent tous leur verdict et si chaque mutation échoue ; sinon code 1.
Lancer depuis ce dossier : python3 -I epreuve_motifs_v5_v1.py
"""
import ast
import hashlib
import json
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
REL = ICI / "relecture-pieces-essaim-v4" / "relecture-fable-api.md"
V5 = ICI / "pieces-comparaison-essaim-v5.md"
TEXTES = ICI / "textes-epreuve-balises-v5-v1.json"
ANCIEN = ICI / "epreuve_motifs_correction_28_v2.py"
SHA = {REL: "c1cebee3a8abec9cc142c458a6eb05800f2095fcef576fc99c0a93a974c7b4d7",
       TEXTES: "4346f288ad5ab22343853617bb2effe0a907e790caa6c7c96fdda6f73cb1d916",
       ANCIEN: "d1caea7bdaa66ef2b18fdcf1b23b8d84a8c1d5b872fc52d4de637949e0d5d1ac"}
SHA_V5 = (ICI / "pieces-comparaison-essaim-v5.md.sha256")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


for p, h in SHA.items():
    if sha(p) != h:
        raise SystemExit(f"empreinte inattendue : {p.name}")
if SHA_V5.exists() and SHA_V5.read_text().split()[0] != sha(V5):
    raise SystemExit("la v5 ne correspond pas à son compagnon")


def code_de_reference():
    t = REL.read_text(encoding="utf-8")
    tete = "**Code de référence de l'article 4 (non exécuté).**"
    assert t.count(tete) == 1
    bloc = t.split(tete, 1)[1].split("```python\n", 1)[1].split("\n```", 1)[0]
    return bloc


CODE = code_de_reference()
REGLE = {}
exec(compile(CODE, "code-de-reference-article-4", "exec"), REGLE)


def motifs_article_4():
    t = V5.read_text(encoding="utf-8")
    a4 = [l for l in t.split("\n") if l.startswith("**Article 4 — Piste.**")]
    assert len(a4) == 1
    ouv = re.search(r"\*Ouverture\* : ligne qui correspond à `([^`]*)`", a4[0]).group(1)
    clo = re.search(r"\*Clôture\* : ligne qui correspond à `([^`]*)`", a4[0]).group(1)
    return ouv, clo


def accord_motifs():
    ouv, clo = motifs_article_4()
    return {"ouverture_article_4": ouv, "ouverture_code": REGLE["OUVERTURE"].pattern,
            "cloture_article_4": clo, "cloture_code": REGLE["CLOTURE"].pattern,
            "identiques": ouv == REGLE["OUVERTURE"].pattern and clo == REGLE["CLOTURE"].pattern}


def anciens_textes():
    """Les dix textes de l'épreuve v4, lus dans l'ancien script sans l'exécuter."""
    arbre = ast.parse(ANCIEN.read_text(encoding="utf-8"))
    for noeud in arbre.body:
        if isinstance(noeud, ast.Assign) and any(getattr(c, "id", None) == "TEXTES" for c in noeud.targets):
            return ast.literal_eval(noeud.value)
    raise SystemExit("TEXTES introuvable dans l'ancien script")


def jouer(fonction, cas):
    """cas : liste de (nom, n_attendu) ; n_attendu None = non conforme attendu."""
    lignes, echecs = [], 0
    for nom, n, texte in cas:
        conforme, duels = fonction(texte)
        obtenu = len(duels) if conforme else None
        ok = (obtenu == n) and (conforme == (n is not None))
        echecs += not ok
        lignes.append((nom, n, conforme, obtenu, ok, duels))
    return lignes, echecs


# Mutations (R5) : chacune retire une des conditions écrites à l'article 4.
def mutation_compte_ignore(texte):
    lignes = texte.split("\n")
    o, c = REGLE["OUVERTURE"], REGLE["CLOTURE"]
    clot = [i for i, l in enumerate(lignes) if c.match(l)]
    ouv = [(i, int(m.group(1)), m.end()) for i, l in enumerate(lignes) if (m := o.match(l))]
    if len(clot) != 1 or not ouv:
        return False, []
    bornes = [i for i, _, _ in ouv][1:] + [clot[0]]
    return True, ["\n".join([lignes[i][p:]] + lignes[i + 1:j]) for (i, _, p), j in zip(ouv, bornes)]


def mutation_sans_ancrage(texte):
    lignes = texte.split("\n")
    o = re.compile(r"\[DUEL\s*(\d+)\]")
    c = re.compile(r"\[FIN DES DUELS\s*:\s*(\d+)\]")
    clot = [(i, int(m.group(1))) for i, l in enumerate(lignes) if (m := c.search(l))]
    ouv = [(i, int(m.group(1)), m.end()) for i, l in enumerate(lignes) if (m := o.search(l))]
    if len(clot) != 1:
        return False, []
    fin, n = clot[0]
    if n < 1 or [k for _, k, _ in ouv] != list(range(1, n + 1)) or ouv[-1][0] > fin:
        return False, []
    bornes = [i for i, _, _ in ouv][1:] + [fin]
    return True, ["\n".join([lignes[i][p:]] + lignes[i + 1:j]) for (i, _, p), j in zip(ouv, bornes)]


def mutation_cloture_multiple(texte):
    lignes = texte.split("\n")
    o, c = REGLE["OUVERTURE"], REGLE["CLOTURE"]
    clot = [(i, int(m.group(1))) for i, l in enumerate(lignes) if (m := c.match(l))]
    ouv = [(i, int(m.group(1)), m.end()) for i, l in enumerate(lignes) if (m := o.match(l))]
    if not clot:
        return False, []
    fin, n = clot[0]
    if n < 1 or [k for _, k, _ in ouv] != list(range(1, n + 1)) or ouv[-1][0] > fin:
        return False, []
    bornes = [i for i, _, _ in ouv][1:] + [fin]
    return True, ["\n".join([lignes[i][p:]] + lignes[i + 1:j]) for (i, _, p), j in zip(ouv, bornes)]


def main():
    d = json.loads(TEXTES.read_text(encoding="utf-8"))
    sains = [(x["nom"], x["n_attendu"], x["texte"]) for x in d["sains"]]
    pieges = [(x["nom"], x["n_attendu"], x["texte"]) for x in d["pieges"]]
    supp = [(x["nom"], x["n_attendu"], x["texte"]) for x in d["supplementaires"]]
    anciens = [(f"ancien texte {k} sans balise", None, t) for k, (_, t) in enumerate(anciens_textes(), start=1)]
    assert len(sains) == 10 and len(pieges) == 8 and len(anciens) == 10
    accord = accord_motifs()
    print(f"motifs de l'article 4 identiques à ceux du code de référence : {accord['identiques']}")
    print(f"  ouverture : {accord['ouverture_article_4']}")
    print(f"  clôture   : {accord['cloture_article_4']}")
    regle = REGLE["duels_balises"]
    total = 0
    for titre, cas in (("CAS SAINS", sains), ("PIÈGES", pieges), ("ANCIENS TEXTES SANS BALISE", anciens),
                       ("SUPPLÉMENTS (hors verdict)", supp)):
        lignes, echecs = jouer(regle, cas)
        if not titre.startswith("SUPPL"):
            total += echecs
        print(f"\n{titre} : {len(cas) - echecs}/{len(cas)} au verdict attendu")
        for nom, n, conforme, obtenu, ok, duels in lignes:
            att = "non conforme" if n is None else f"conforme, n = {n}"
            obt = "non conforme" if not conforme else f"conforme, n = {obtenu}"
            print(f"  {nom} : attendu {att} ; obtenu {obt} : {'PASSE' if ok else 'ÉCHOUE'}")
            for k, du in enumerate(duels, start=1):
                print(f"      duel {k} : {du.strip().splitlines()[0][:80] if du.strip() else '(vide)'}")
    contenu = regle(sains[7][2])[1][0]
    contenu_ok = contenu.startswith(" Duel 1 : HA")
    print(f"\nreste de la ligne d'ouverture compris dans le duel (sain 8) : {contenu_ok} ({contenu[:30]!r})")
    total += not contenu_ok
    print("\nMUTATIONS (chacune doit échouer)")
    mut_ok = True
    for nom, f in (("compte de la clôture ignoré", mutation_compte_ignore),
                   ("motifs sans ancrage en début de ligne", mutation_sans_ancrage),
                   ("clôtures multiples admises (la première compte)", mutation_cloture_multiple)):
        e = sum(jouer(f, c)[1] for c in (sains, pieges, anciens))
        mut_ok &= e > 0
        print(f"  {nom} : {e} cas au mauvais verdict : {'mutation détectée' if e else 'MUTATION NON DÉTECTÉE'}")
    ok = accord["identiques"] and total == 0 and mut_ok
    print(f"\nRÉSULTAT : {'PASSE' if ok else 'ÉCHOUE'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
