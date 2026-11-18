"""Prépare les copies neutres remises aux deux codeurs (protocole, section 4 de la grille brouillon 2).

NE PAS EXÉCUTER SUR LA TENUE À L'ÉCART sans GO : pour la moitié « tenue-a-l-ecart », le script exige
`--go GO-AAAA-MM-JJ-NN` et refuse AVANT toute lecture de fichier de billet. Le réviseur de la grille
ne l'a exécuté que sur la moitié développement, en dossier temporaire supprimé.

Ce qui est caché : score, votants, nombre de commentaires, date, étiquettes, statut, appariement,
adresse, auteur (champs du manifeste jamais copiés) ; noms de l'auteur et des coauteurs dans le texte
(→ [AUTEUR]) ; adresses des liens (→ « texte [lien : hôte] ») et des images (→ [IMAGE n : texte]) ;
éléments interactifs (→ [ÉLÉMENT INTERACTIF]) ; identifiant du site (→ identifiant neutre) ; ordre
(liste propre à chaque codeur, membres d'une paire jamais adjacents). Commentaires (seconde passe) :
nom, score, votes, date ôtés ; réponses d'auteur marquées « ne pas coder » ; ordre mélangé ; parents
par identifiant neutre. Borne insérée après le 250e mot du corps.

Sorties dans SORTIE/ :
  codeurs/billets/<neutre>.md          copies neutres des billets (passe 1)
  codeurs/commentaires/<neutre>.json   commentaires neutres des bien notés (passe 2, remis après scellement)
  codeurs/ordre-codeur-1.txt, ordre-codeur-2.txt
  cles/table-de-correspondance.json    jamais remise aux codeurs
  cles/manifeste-preparation.json      graine, versions, empreintes des entrées et sorties

Usage : python preparer_copies_neutres_v1.py MANIFESTE_V2 MOITIE RACINE_MOITIE SORTIE [--go GO-…]
"""
import hashlib
import json
import os
import re
import sys
from urllib.parse import urlparse

import numpy as np

ENTROPIE = 159121083548737780390099018299333639900  # fixée dans la grille brouillon 2, section 4.2
BORNE = "⟦FIN DE L'EN-TÊTE — 250 MOTS⟧"
N_TETE = 250
RX_GO = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")


class Refus(Exception):
    pass


def garde(moitie, go):
    """Refus avant toute lecture : tenue à l'écart sans GO valide de forme."""
    if moitie not in ("developpement", "tenue-a-l-ecart"):
        raise Refus(f"moitié inconnue : {moitie}")
    if moitie == "tenue-a-l-ecart" and not (go and RX_GO.match(go)):
        raise Refus("tenue à l'écart : préparation interdite sans --go GO-AAAA-MM-JJ-NN")


def hote(url):
    try:
        h = urlparse(url.strip()).netloc
    except ValueError:
        h = ""
    return h.lower().removeprefix("www.") or "adresse-locale"


def neutraliser_texte(md, noms):
    t = re.sub(r"```widget\[[^\]]*\].*?```", "[ÉLÉMENT INTERACTIF]", md, flags=re.S)
    n_img = [0]

    def img(m):
        n_img[0] += 1
        alt = m.group(1).strip()
        alt = "" if re.fullmatch(r"(image|img|screenshot)?[\w\- ]*\.(png|jpe?g|gif|webp|svg)", alt, re.I) else alt
        return f"[IMAGE {n_img[0]}" + (f" : {alt}" if alt else "") + "]"

    t = re.sub(r"!\[([^\]]*)\]\(([^)]*)\)", img, t)
    t = re.sub(r"\[([^\]]*)\]\(([^)\s]*)[^)]*\)", lambda m: f"{m.group(1)} [lien : {hote(m.group(2))}]", t)
    t = re.sub(r"(?<![\w/])https?://[^\s)\]>]+", lambda m: f"[lien : {hote(m.group(0))}]", t)
    t = re.sub(r"<iframe.*?</iframe>", "[ÉLÉMENT INTERACTIF]", t, flags=re.S | re.I)
    for nom in sorted({n for n in noms if n and len(n) >= 3}, key=len, reverse=True):
        t = re.sub(re.escape(nom), "[AUTEUR]", t, flags=re.I)
    return t, n_img[0]


def inserer_borne(t, n=N_TETE):
    """Insère la borne après le n-ième mot (suite de non-blancs), marqueurs entre crochets comptés comme mots."""
    k = 0
    for m in re.finditer(r"\S+", t):
        k += 1
        if k == n:
            return t[:m.end()] + f"\n\n{BORNE}\n\n" + t[m.end():], True
    return t + f"\n\n{BORNE} (billet de moins de {n} mots)\n", False


def ordre_sans_paires_adjacentes(neutres, paires, rng, essais=1000):
    for _ in range(essais):
        o = list(rng.permutation(neutres))
        pos = {x: i for i, x in enumerate(o)}
        if all(abs(pos[a] - pos[b]) > 1 for a, b in paires):
            return o
    raise Refus("ordre : aucune permutation sans paire adjacente en 1000 tirages")


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main(argv):
    go = None
    if "--go" in argv:
        i = argv.index("--go")
        go = argv[i + 1] if i + 1 < len(argv) else ""
        argv = argv[:i] + argv[i + 2:]
    m2p, moitie, racine, sortie = argv[:4]
    garde(moitie, go)  # avant toute lecture

    man = json.load(open(m2p, encoding="utf-8"))
    billets = sorted((b for b in man["billets"] if b["moitie"] == moitie), key=lambda b: b["identifiant"])
    if os.path.exists(sortie) and os.listdir(sortie):
        raise Refus(f"dossier de sortie non vide : {sortie}")

    ss = np.random.SeedSequence(ENTROPIE)
    s_ids, s_o1, s_o2 = ss.spawn(3)
    rng_ids = np.random.default_rng(s_ids)
    codes = rng_ids.choice(10 ** 6, size=len(billets), replace=False)
    neutre = {b["identifiant"]: f"B{c:06d}" for b, c in zip(billets, codes)}

    dcb = os.path.join(sortie, "codeurs", "billets")
    dcc = os.path.join(sortie, "codeurs", "commentaires")
    dcl = os.path.join(sortie, "cles")
    for d in (dcb, dcc, dcl):
        os.makedirs(d, exist_ok=True)

    sorties, details = {}, []
    for b in billets:
        i = b["identifiant"]
        src = os.path.join(racine, "billets", f"{i}.md")
        brut = open(src, encoding="utf-8").read()
        if hashlib.sha256(brut.encode("utf-8")).hexdigest() != b["empreinte_sha256_texte"]:
            raise Refus(f"empreinte du texte différente du manifeste : {i}")
        noms = [b["auteur"], *(b["coauteurs"] or [])]
        corps, n_img = neutraliser_texte(brut, noms)
        corps, borne_ok = inserer_borne(corps)
        titre, _ = neutraliser_texte(b["titre"], noms)
        p = os.path.join(dcb, f"{neutre[i]}.md")
        with open(p, "w", encoding="utf-8") as f:
            f.write(f"# {titre}\n\n{corps}\n")
        sorties[p] = sha(p)
        details.append({"neutre": neutre[i], "images": n_img, "borne_inseree": borne_ok})

    # Commentaires des bien notés (seconde passe).
    neutres_tries = sorted(neutre.values())
    ss_com = s_ids.spawn(len(neutres_tries))
    rng_par_billet = dict(zip(neutres_tries, ss_com))
    n_com = n_aut = 0
    for b in billets:
        if b["classe"] != "bien-note":
            continue
        i = b["identifiant"]
        pc = os.path.join(racine, "commentaires", f"{i}.json")
        if not os.path.exists(pc):
            continue
        coms = json.load(open(pc, encoding="utf-8"))
        retenus = {c["_id"] for c in b["commentaires_retenus"]}
        coms = [c for c in coms if c["_id"] in retenus]
        rng = np.random.default_rng(rng_par_billet[neutre[i]])
        perm = rng.permutation(len(coms))
        cid = {coms[k]["_id"]: f"c{r + 1:02d}" for r, k in enumerate(perm)}
        aut = {b["auteur"], *(b["coauteurs"] or [])}
        sortis = []
        for k in perm:
            c = coms[k]
            est_aut = (c.get("user") or {}).get("displayName") in aut
            n_com += 1
            n_aut += est_aut
            texte, _ = neutraliser_texte(c["contents"]["markdown"] or "", list(aut))
            par = c.get("parentCommentId")
            sortis.append({
                "commentaire": cid[c["_id"]],
                "reponse_a": (cid.get(par, "commentaire non retenu") if par else None),
                "reponse_d_auteur_ne_pas_coder": est_aut,
                "texte": texte,
            })
        p = os.path.join(dcc, f"{neutre[i]}.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump({"billet": neutre[i], "commentaires": sortis}, f, ensure_ascii=False, indent=1)
        sorties[p] = sha(p)

    # Ordres de lecture.
    paires = [(neutre[b["identifiant"]], neutre[b["apparie_a"]]) for b in billets
              if b["classe"] == "bien-note" and b["apparie_a"] in neutre]
    for nom, s in (("ordre-codeur-1.txt", s_o1), ("ordre-codeur-2.txt", s_o2)):
        o = ordre_sans_paires_adjacentes(list(neutre.values()), paires, np.random.default_rng(s))
        p = os.path.join(sortie, "codeurs", nom)
        open(p, "w").write("\n".join(o) + "\n")
        sorties[p] = sha(p)

    table = os.path.join(dcl, "table-de-correspondance.json")
    json.dump({"neutre_vers_site": {v: k for k, v in neutre.items()}}, open(table, "w"), indent=1)
    manif = {
        "version": "v1", "moitie": moitie, "go": go, "entropie": ENTROPIE, "numpy": np.__version__,
        "manifeste_v2": {"chemin": m2p, "sha256": sha(m2p)},
        "billets": len(billets), "commentaires": n_com, "reponses_d_auteur": n_aut,
        "paires": len(paires), "details": details,
        "sorties_sha256": {os.path.relpath(k, sortie): v for k, v in sorties.items()},
        "table_sha256": sha(table),
    }
    json.dump(manif, open(os.path.join(dcl, "manifeste-preparation.json"), "w"), ensure_ascii=False, indent=1)
    print(f"{len(billets)} billets, {n_com} commentaires ({n_aut} d'auteur), {len(paires)} paires ; sortie {sortie}")
    return manif


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Refus as e:
        print("REFUS :", e)
        sys.exit(2)
