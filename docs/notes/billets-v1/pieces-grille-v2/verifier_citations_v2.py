"""Vérifie par programme la grille brouillon 2 (citations et structure).

Pour chaque citation « … » de la grille : billet dans la moitié développement v2 (manifeste v2) ;
billet hors des billets de développement marqués par le désaccord des lecteurs du tri ;
présence exacte dans le texte du billet (ou dans son titre si « (titre) »), ou dans le commentaire
nommé ; 25 mots au plus ; commentaire retenu au manifeste et non écrit par un auteur du billet.
Normalisation (celle du brouillon 1) : images ôtées, liens réduits à leur texte, `* _ \\` ôtés,
blancs multiples réduits.

Structure : chaque geste G01–G25 a des modalités, un indicateur inclus dans les modalités, un statut
d'analyse, au moins un exemple et un contre-exemple vérifiés ; chaque classe O0–O12 a un code,
au moins un exemple et un contre-exemple vérifiés.

Lit SEULEMENT /home/user/billets-corpus-v2/developpement/ (textes et commentaires), jamais la tenue
à l'écart ni les dossiers communs.

Usage : python verifier_citations_v2.py GRILLE MANIFESTE_V2 MANIFESTE_V1 GRILLE_V1 MARQUES_2 SORTIE_JSON
"""
import hashlib
import json
import re
import sys

RAC = "/home/user/billets-corpus-v2/developpement"
RX_CIT = re.compile(r"`([A-Za-z0-9]{17})(?:/([A-Za-z0-9]{17}))?`( \(titre\))? — « ([^»]+?) »")


def empreinte(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def norm(t):
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*_\\]", "", t)
    return " ".join(t.split())


def sections(texte, prefixe):
    """Découpe en sections `### G01.` ou `### O1.` ; renvoie {code: corps}."""
    res = {}
    for m in re.finditer(rf"^### ({prefixe}\d+)\. .*?$(.*?)(?=^### |^## |^---|\Z)", texte, re.M | re.S):
        res[m.group(1)] = m.group(2)
    return res


def main(grille, m2p, m1p, g1p, marq2p, sortie):
    texte = open(grille, encoding="utf-8").read()
    m2 = json.load(open(m2p, encoding="utf-8"))
    dev = {b["identifiant"]: b for b in m2["billets"] if b["moitie"] == "developpement"}
    tous_v2 = {b["identifiant"]: b["moitie"] for b in m2["billets"]}
    marq2 = {d["identifiant"] for d in json.load(open(marq2p, encoding="utf-8"))["desaccords_dans_le_corpus"]}
    exclus_dev = sorted(marq2 & set(dev))

    cache_t, cache_c = {}, {}
    echecs, verifiees = [], []

    def verifier(ref_b, ref_c, titre, cit):
        if ref_b not in dev:
            return "billet hors développement v2"
        if ref_b in marq2:
            return "billet marqué par le désaccord des lecteurs du tri"
        c = norm(cit)
        if len(c.split()) > 25:
            return "plus de 25 mots"
        if ref_c:
            if ref_b not in cache_c:
                cache_c[ref_b] = {x["_id"]: x for x in
                                  json.load(open(f"{RAC}/commentaires/{ref_b}.json", encoding="utf-8"))}
            com = cache_c[ref_b].get(ref_c)
            if com is None:
                return "commentaire absent"
            if ref_c not in {x["_id"] for x in dev[ref_b]["commentaires_retenus"]}:
                return "commentaire non retenu au manifeste"
            b = dev[ref_b]
            if (com.get("user") or {}).get("displayName") in {b["auteur"], *(b["coauteurs"] or [])}:
                return "commentaire d'un auteur du billet"
            src = norm(com["contents"]["markdown"] or "")
        elif titre:
            src = norm(dev[ref_b]["titre"])
        else:
            if ref_b not in cache_t:
                cache_t[ref_b] = norm(open(f"{RAC}/billets/{ref_b}.md", encoding="utf-8").read())
            src = cache_t[ref_b]
        return None if c in src else "citation introuvable"

    structure = {}
    for prefixe, attendus in (("G", [f"G{i:02d}" for i in range(1, 26)]), ("O", [f"O{i}" for i in range(0, 13)])):
        secs = sections(texte, prefixe)
        for code in attendus:
            corps = secs.get(code)
            etat = {"present": corps is not None, "exemples": 0, "contre_exemples": 0, "problemes": []}
            if corps is None:
                etat["problemes"].append("section absente")
                structure[code] = etat
                continue
            for ligne in corps.splitlines():
                genre = "contre_exemples" if ligne.startswith("- **Contre-exemple**") else (
                    "exemples" if ligne.startswith("- **Exemple**") else None)
                for b, c, t, cit in RX_CIT.findall(ligne):
                    motif = verifier(b, c, bool(t), cit)
                    ref = b + ("/" + c if c else "") + (" (titre)" if t else "")
                    if motif:
                        echecs.append({"section": code, "ref": ref, "motif": motif, "citation": cit[:90]})
                    else:
                        verifiees.append({"section": code, "ref": ref, "genre": genre})
                        if genre:
                            etat[genre] += 1
            if prefixe == "G":
                mods = re.search(r"^- \*\*Modalités\*\* : (.*)$", corps, re.M)
                ind = re.search(r"^- \*\*Indicateur\*\* : (.*)$", corps, re.M)
                ana = re.search(r"^- \*\*Analyse\*\* : (comparée|descriptive)", corps, re.M)
                ml = re.findall(r"`([^`]+)`", mods.group(1)) if mods else []
                il = re.findall(r"`([^`]+)`", ind.group(1)) if ind else []
                etat.update({"modalites": ml, "indicateur": il, "analyse": ana.group(1) if ana else None})
                if not (2 <= len(ml) <= 4) or len(set(ml)) != len(ml):
                    etat["problemes"].append("modalités : 2 à 4, distinctes")
                if not il or not set(il) < set(ml):
                    etat["problemes"].append("indicateur absent ou hors des modalités, ou égal à toutes")
                if not ana:
                    etat["problemes"].append("statut d'analyse absent")
            else:
                if not re.search(rf"^- \*\*Code\*\* : `{code}`", corps, re.M):
                    etat["problemes"].append("code absent")
            if etat["exemples"] < 1:
                etat["problemes"].append("aucun exemple vérifié")
            if etat["contre_exemples"] < 1:
                etat["problemes"].append("aucun contre-exemple vérifié")
            structure[code] = etat

    # Citations hors des lignes d'exemple (cas d'école, etc.) : vérifiées aussi.
    deja = {(v["ref"]) for v in verifiees} | {e["ref"] for e in echecs}
    for b, c, t, cit in RX_CIT.findall(texte):
        ref = b + ("/" + c if c else "") + (" (titre)" if t else "")
        if ref in deja:
            continue
        motif = verifier(b, c, bool(t), cit)
        (echecs.append({"section": "hors-exemple", "ref": ref, "motif": motif, "citation": cit[:90]})
         if motif else verifiees.append({"section": "hors-exemple", "ref": ref, "genre": None}))
        deja.add(ref)

    # Billets cités au brouillon 1 (identifiants seulement) et leur moitié v2.
    g1 = open(g1p, encoding="utf-8").read()
    cites1 = sorted(set(re.findall(r"`([A-Za-z0-9]{17})(?:/[A-Za-z0-9]{17})?`", g1)))
    b1 = {"developpement": [], "tenue-a-l-ecart": [], "absent": []}
    for i in cites1:
        b1[tous_v2.get(i, "absent")].append(i)

    # Commentaires de développement : combien d'auteurs (lu sur les seuls fichiers de développement).
    n_com = n_aut = 0
    for i, b in dev.items():
        if b["classe"] != "bien-note":
            continue
        aut = {b["auteur"], *(b["coauteurs"] or [])}
        for x in json.load(open(f"{RAC}/commentaires/{i}.json", encoding="utf-8")):
            n_com += 1
            n_aut += (x.get("user") or {}).get("displayName") in aut

    pb = {k: v["problemes"] for k, v in structure.items() if v["problemes"]}
    res = {
        "version": "v2",
        "grille": {"chemin": grille, "sha256": empreinte(grille)},
        "manifeste_v2": {"chemin": m2p, "sha256": empreinte(m2p)},
        "manifeste_v1": {"chemin": m1p, "sha256": empreinte(m1p)},
        "grille_v1": {"chemin": g1p, "sha256": empreinte(g1p)},
        "marques_desaccords": {"chemin": marq2p, "sha256": empreinte(marq2p)},
        "dossier_lu": RAC,
        "billets_dev_exclus_des_exemples": exclus_dev,
        "citations_verifiees": len(verifiees),
        "citations_distinctes_billets": len({v["ref"] for v in verifiees if "/" not in v["ref"]}),
        "citations_distinctes_commentaires": len({v["ref"] for v in verifiees if "/" in v["ref"]}),
        "echecs": echecs,
        "problemes_de_structure": pb,
        "structure": structure,
        "brouillon1": {k: v for k, v in b1.items()},
        "commentaires": {"bien_notes_dev": sum(1 for b in dev.values() if b["classe"] == "bien-note"),
                         "commentaires": n_com, "reponses_d_auteur": n_aut},
        "verdict": "OK" if not echecs and not pb else "ECHEC",
    }
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"citations vérifiées : {len(verifiees)} ; échecs : {len(echecs)} ; problèmes de structure : {len(pb)}")
    for e in echecs:
        print("ECHEC", e)
    for k, v in pb.items():
        print("STRUCTURE", k, v)
    return 0 if res["verdict"] == "OK" else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:7]))
