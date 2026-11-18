"""Vérifie par programme la grille brouillon 3 (citations et structure). Remplace verifier_citations_v2.py.

Pour TOUTE citation `identifiant[/commentaire]`[ (titre)] — « … » du fichier (exemples, contre-exemples,
cas d'école) : billet dans la moitié développement v2 ; hors des billets de développement du
marquage 2 ; hors des billets de l'essai pilote (si la liste est donnée) ; présence exacte dans le
texte, le titre ou le commentaire nommé, après la normalisation du brouillon 1 ; 25 mots au plus ;
commentaire retenu au manifeste et non écrit par un auteur (noms non vides).

Structure : G01–G25 ont modalités (2 à 4, distinctes), indicateur strictement inclus, statut
d'analyse, « Consigne si retenue » si comparé, au moins un exemple et un contre-exemple vérifiés ;
O0–O13 ont un code, au moins un exemple et un contre-exemple vérifiés.

Option --essai : la sortie de l'essai du plan d'analyse doit citer l'empreinte de CETTE grille.

Lit SEULEMENT /home/user/billets-corpus-v2/developpement/.
"""
import argparse
import hashlib
import json
import re
import sys

RAC = "/home/user/billets-corpus-v2/developpement"
RX_CIT = re.compile(r"`([A-Za-z0-9]{17})(?:/([A-Za-z0-9]{17}))?`( \(titre\))?(?: \([^)`«]*\))? — « ([^»]+?) »")


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def norm(t):
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*_\\]", "", t)
    return " ".join(t.split())


def sections(texte, prefixe):
    return {m.group(1): m.group(2) for m in
            re.finditer(rf"^### ({prefixe}\d+)\. .*?$(.*?)(?=^### |^## |^---|\Z)", texte, re.M | re.S)}


def noms(b):
    return {n for n in [b.get("auteur"), *(b.get("coauteurs") or [])] if n}


def main():
    ap = argparse.ArgumentParser()
    for a in ("grille", "manifeste", "grille-v1", "marques2", "sortie"):
        ap.add_argument("--" + a, required=True)
    ap.add_argument("--pilote")
    ap.add_argument("--essai")
    A = ap.parse_args()
    texte = open(A.grille, encoding="utf-8").read()
    m2 = json.load(open(A.manifeste, encoding="utf-8"))
    dev = {b["identifiant"]: b for b in m2["billets"] if b["moitie"] == "developpement"}
    tous_v2 = {b["identifiant"]: b["moitie"] for b in m2["billets"]}
    marq2 = {d["identifiant"] for d in json.load(open(A.marques2, encoding="utf-8"))["desaccords_dans_le_corpus"]}
    pilote = set(json.load(open(A.pilote, encoding="utf-8"))["billets"]) if A.pilote else set()

    cache_t, cache_c = {}, {}

    def verifier(b_, c_, titre, cit):
        if b_ not in dev:
            return "billet hors développement v2"
        if b_ in marq2:
            return "billet marqué par le désaccord des lecteurs du tri"
        if b_ in pilote:
            return "billet de l'essai pilote"
        c = norm(cit)
        if len(c.split()) > 25:
            return "plus de 25 mots"
        if c_:
            if b_ not in cache_c:
                cache_c[b_] = {x["_id"]: x for x in json.load(open(f"{RAC}/commentaires/{b_}.json", encoding="utf-8"))}
            com = cache_c[b_].get(c_)
            if com is None:
                return "commentaire absent"
            if c_ not in {x["_id"] for x in dev[b_]["commentaires_retenus"]}:
                return "commentaire non retenu au manifeste"
            if (com.get("user") or {}).get("displayName") in noms(dev[b_]):
                return "commentaire d'un auteur du billet"
            src = norm(com["contents"]["markdown"] or "")
        elif titre:
            src = norm(dev[b_]["titre"])
        else:
            if b_ not in cache_t:
                cache_t[b_] = norm(open(f"{RAC}/billets/{b_}.md", encoding="utf-8").read())
            src = cache_t[b_]
        return None if c in src else "citation introuvable"

    echecs, verifiees = [], []
    structure = {}
    cites_AB = set()
    for prefixe, attendus in (("G", [f"G{i:02d}" for i in range(1, 26)]), ("O", [f"O{i}" for i in range(14)])):
        secs = sections(texte, prefixe)
        for code in attendus:
            corps = secs.get(code)
            et = {"exemples": 0, "contre_exemples": 0, "problemes": []}
            structure[code] = et
            if corps is None:
                et["problemes"].append("section absente")
                continue
            for ligne in corps.splitlines():
                genre = ("contre_exemples" if ligne.startswith("- **Contre-exemple**") else
                         "exemples" if ligne.startswith("- **Exemple**") else "autre")
                for b_, c_, t_, cit in RX_CIT.findall(ligne):
                    cites_AB.add(b_)
                    ref = b_ + ("/" + c_ if c_ else "") + (" (titre)" if t_ else "")
                    motif = verifier(b_, c_, bool(t_), cit)
                    if motif:
                        echecs.append({"section": code, "ref": ref, "motif": motif, "citation": cit[:90]})
                    else:
                        verifiees.append({"section": code, "ref": ref, "genre": genre})
                        if genre != "autre":
                            et[genre] += 1
            if prefixe == "G":
                mods = re.search(r"^- \*\*Modalités\*\* : (.*)$", corps, re.M)
                ind = re.search(r"^- \*\*Indicateur\*\* : (.*)$", corps, re.M)
                ana = re.search(r"^- \*\*Analyse\*\* : (comparée|descriptive)", corps, re.M)
                cons = re.search(r"^- \*\*Consigne si retenue\*\* : « .+ »$", corps, re.M)
                ml = re.findall(r"`([^`]+)`", mods.group(1)) if mods else []
                il = re.findall(r"`([^`]+)`", ind.group(1)) if ind else []
                et.update({"modalites": ml, "indicateur": il, "analyse": ana.group(1) if ana else None})
                if not (2 <= len(ml) <= 4) or len(set(ml)) != len(ml):
                    et["problemes"].append("modalités : 2 à 4, distinctes")
                if not il or not set(il) < set(ml):
                    et["problemes"].append("indicateur absent, hors des modalités, ou égal à toutes")
                if not ana:
                    et["problemes"].append("statut d'analyse absent")
                if ana and ana.group(1) == "comparée" and not cons:
                    et["problemes"].append("« Consigne si retenue » absente pour un geste comparé")
            elif not re.search(rf"^- \*\*Code\*\* : `{code}`", corps, re.M):
                et["problemes"].append("code absent")
            if et["exemples"] < 1:
                et["problemes"].append("aucun exemple vérifié")
            if et["contre_exemples"] < 1:
                et["problemes"].append("aucun contre-exemple vérifié")

    # Toute autre citation au format, hors des sections A et B.
    vues = {(v["ref"]) for v in verifiees} | {e["ref"] for e in echecs}
    for b_, c_, t_, cit in RX_CIT.findall(texte):
        ref = b_ + ("/" + c_ if c_ else "") + (" (titre)" if t_ else "")
        if ref in vues:
            continue
        vues.add(ref)
        motif = verifier(b_, c_, bool(t_), cit)
        (echecs.append({"section": "hors-A-B", "ref": ref, "motif": motif, "citation": cit[:90]}) if motif
         else verifiees.append({"section": "hors-A-B", "ref": ref, "genre": "autre"}))

    g1 = open(A.grille_v1, encoding="utf-8").read()
    b1 = {"developpement": [], "tenue-a-l-ecart": [], "absent": []}
    for i in sorted(set(re.findall(r"`([A-Za-z0-9]{17})(?:/[A-Za-z0-9]{17})?`", g1))):
        b1[tous_v2.get(i, "absent")].append(i)

    essai = None
    if A.essai:
        e = json.load(open(A.essai, encoding="utf-8"))
        g_essai = e.get("sortie_complete", e).get("entrees", {}).get("grille", {}).get("sha256")
        essai = {"chemin": A.essai, "grille_citee": g_essai, "conforme": g_essai == sha(A.grille)}
        if not essai["conforme"]:
            echecs.append({"section": "essai", "ref": A.essai, "motif": "essai joué sur une autre grille",
                           "citation": str(g_essai)})

    pb = {k: v["problemes"] for k, v in structure.items() if v["problemes"]}
    res = {
        "version": "v3",
        "grille": {"chemin": A.grille, "sha256": sha(A.grille)},
        "manifeste_v2": {"chemin": A.manifeste, "sha256": sha(A.manifeste)},
        "marques_desaccords": {"chemin": A.marques2, "sha256": sha(A.marques2)},
        "pilote": {"chemin": A.pilote, "sha256": sha(A.pilote), "billets": sorted(pilote)} if A.pilote else None,
        "dossier_lu": RAC,
        "billets_dev_exclus": sorted((marq2 & set(dev)) | pilote),
        "citations_verifiees": len(verifiees),
        "references_distinctes_billets": len({v["ref"] for v in verifiees if "/" not in v["ref"]}),
        "references_distinctes_commentaires": len({v["ref"] for v in verifiees if "/" in v["ref"]}),
        "billets_cites_sections_A_B": sorted(cites_AB),
        "echecs": echecs,
        "problemes_de_structure": pb,
        "structure": structure,
        "brouillon1": b1,
        "essai": essai,
        "verdict": "OK" if not echecs and not pb else "ECHEC",
    }
    with open(A.sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"citations vérifiées : {len(verifiees)} ; échecs : {len(echecs)} ; problèmes de structure : {len(pb)} ; "
          f"billets cités en A et B : {len(cites_AB)}")
    for e in echecs:
        print("ECHEC", e)
    for k, v in pb.items():
        print("STRUCTURE", k, v)
    return 0 if res["verdict"] == "OK" else 1


if __name__ == "__main__":
    sys.exit(main())
