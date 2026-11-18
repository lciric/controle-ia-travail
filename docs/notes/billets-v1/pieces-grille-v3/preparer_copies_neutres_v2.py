"""Prépare les copies neutres des deux codeurs, en DEUX APPELS (grille brouillon 3, section 4.2).
Remplace preparer_copies_neutres_v1.py.

  --passe 1 : SORTIE/passe-1/codeur-1/ et codeur-2/ (copies des billets, ordre.txt, extrait de la
              grille, consigne) + SORTIE/cles/ (table, manifeste). AUCUN fichier de commentaires :
              rien ne dit quel billet est bien noté.
  --passe 2 : refuse sans --depot1 et --depot2 (dépôts de gestes de la passe 1), sans leurs compagnons
              `.sha256` conformes, ou si l'un échoue au contrôle de dépôt ; écrit alors
              SORTIE/passe-2/commentaires/ et SORTIE/cles/commentaires-codables.json.

Moitié « tenue-a-l-ecart » : exige --go GO-AAAA-MM-JJ-NN (forme seulement) et refuse AVANT toute
lecture. --pilote LISTE.json : douze billets de développement (section 10), graine propre au pilote ;
refusé avec la tenue à l'écart.

Usage :
  python preparer_copies_neutres_v2.py --passe 1 --manifeste M --moitie developpement \
      --racine /home/user/billets-corpus-v2/developpement --sortie S --grille-extrait E --consigne C \
      [--pilote P] [--go GO-…]
  python preparer_copies_neutres_v2.py --passe 2 ... --grille GRILLE --depot1 F1 --depot2 F2
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import statistics
import sys
from urllib.parse import urlparse

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controler_depot_v1 as controle  # noqa: E402

ENTROPIE_TENUE = 159121083548737780390099018299333639900  # grille, section 4.2
ENTROPIE_PILOTE = 90880842301028903807274995354310655842  # grille, section 10.3
BORNE = "⟦FIN DE L'EN-TÊTE — 250 MOTS⟧"
N_TETE = 250
RX_GO = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")
RX_MARQUEUR = re.compile(r"\[(?:IMAGE \d+(?: : [^\]]*)?|lien : [^\]]*|AUTEUR|ADRESSE|ÉLÉMENT INTERACTIF)\]")
RX_COURRIEL = re.compile(r"(?:mailto:)?[\w.+-]+@[\w-]+(?:\.[\w-]+)+")


class Refus(Exception):
    pass


def garde(A):
    """Refus avant toute lecture."""
    if A.moitie not in ("developpement", "tenue-a-l-ecart"):
        raise Refus(f"moitié inconnue : {A.moitie}")
    if A.moitie == "tenue-a-l-ecart":
        if A.pilote:
            raise Refus("le pilote ne porte que sur la moitié développement")
        if not (A.go and RX_GO.match(A.go)):
            raise Refus("tenue à l'écart : préparation interdite sans --go GO-AAAA-MM-JJ-NN")
    if A.passe == "2" and not (A.depot1 and A.depot2 and A.grille):
        raise Refus("passe 2 : --depot1, --depot2 et --grille sont exigés")


def sha_fichier(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def verifier_compagnon(p):
    c = p + ".sha256"
    if not os.path.isfile(p) or not os.path.isfile(c):
        raise Refus(f"dépôt ou compagnon absent : {p}")
    lignes = [l for l in open(c, encoding="utf-8").read().splitlines() if l.strip()]
    m = re.match(r"^([0-9a-f]{64})  (\S.*)$", lignes[0]) if len(lignes) == 1 else None
    if not m or m.group(2) != os.path.basename(p) or m.group(1) != sha_fichier(p):
        raise Refus(f"compagnon non conforme : {c}")
    return m.group(1)


def hote(url):
    try:
        h = urlparse(url.strip()).netloc
    except ValueError:
        h = ""
    return h.lower().removeprefix("www.") or "adresse-locale"


def noms_a_masquer(b):
    noms = [n for n in [b.get("auteur"), *(b.get("coauteurs") or [])] if n and n.strip()]
    parties = {p for n in noms for p in re.findall(r"[^\W\d_]{4,}", n)}
    return noms, parties


def neutraliser(md, noms, parties):
    t = RX_COURRIEL.sub("[ADRESSE]", md)
    t = re.sub(r"```widget\[[^\]]*\].*?```", "[ÉLÉMENT INTERACTIF]", t, flags=re.S)
    t = re.sub(r"<iframe.*?</iframe>", "[ÉLÉMENT INTERACTIF]", t, flags=re.S | re.I)
    n_img = [0]

    def img(m):
        n_img[0] += 1
        alt = m.group(1).strip()
        alt = "" if re.fullmatch(r"(image|img|screenshot)?[\w\- ]*\.(png|jpe?g|gif|webp|svg)", alt, re.I) else alt
        return f"[IMAGE {n_img[0]}" + (f" : {alt}" if alt else "") + "]"

    t = re.sub(r"!\[([^\]]*)\]\(([^)]*)\)", img, t)
    t = re.sub(r"\[([^\]]*)\]\(([^)\s]*)[^)]*\)", lambda m: f"{m.group(1)} [lien : {hote(m.group(2))}]", t)
    t = re.sub(r"(?<![\w/])https?://[^\s)\]>]+", lambda m: f"[lien : {hote(m.group(0))}]", t)
    n_noms = 0
    for nom in sorted(set(noms), key=len, reverse=True):
        t, k = re.subn(rf"(?<!\w){re.escape(nom)}(?!\w)", "[AUTEUR]", t, flags=re.I)
        n_noms += k
    for p in sorted(parties, key=len, reverse=True):
        t, k = re.subn(rf"(?<!\w){re.escape(p)}(?!\w)", "[AUTEUR]", t)
        n_noms += k
    colles = len(re.findall(r"\w\[(?:AUTEUR|ADRESSE)\]|\[(?:AUTEUR|ADRESSE)\]\w", t))
    return t, n_img[0], n_noms, colles


def mots_reels(t):
    """Positions de fin des mots réels : hors marqueurs, avec au moins une lettre ou un chiffre."""
    spans = [(m.start(), m.end()) for m in RX_MARQUEUR.finditer(t)]
    fins = []
    for m in re.finditer(r"\S+", t):
        if any(a < m.end() and m.start() < b for a, b in spans):
            continue
        if not re.search(r"\w", m.group(0)):
            continue
        fins.append(m.end())
    return fins, spans


def inserer_borne(t, n=N_TETE):
    fins, spans = mots_reels(t)
    if len(fins) < n:
        return t + f"\n\n{BORNE} (billet de moins de {n} mots)\n", len(fins), False
    pos = fins[n - 1]
    for a, b in spans:  # jamais dans un marqueur
        if a < pos < b:
            pos = b
    return t[:pos] + f"\n\n{BORNE}\n\n" + t[pos:], n, True


def ordre_sans_paires_adjacentes(neutres, paires, rng, essais=1000):
    for _ in range(essais):
        o = list(rng.permutation(neutres))
        pos = {x: i for i, x in enumerate(o)}
        if all(abs(pos[a] - pos[b]) > 1 for a, b in paires):
            return o
    raise Refus("ordre : aucune permutation sans paire adjacente en 1000 tirages")


def selection(A, man):
    billets = [b for b in man["billets"] if b["moitie"] == A.moitie]
    if A.pilote:
        liste = set(json.load(open(A.pilote, encoding="utf-8"))["billets"])
        billets = [b for b in billets if b["identifiant"] in liste]
        if len(billets) != len(liste):
            raise Refus("pilote : identifiants hors de la moitié développement")
    return sorted(billets, key=lambda b: b["identifiant"])


def graines(A, billets):
    ss = np.random.SeedSequence(ENTROPIE_PILOTE if A.pilote else ENTROPIE_TENUE)
    s_ids, s_o1, s_o2 = ss.spawn(3)
    codes = np.random.default_rng(s_ids).choice(10 ** 6, size=len(billets), replace=False)
    neutre = {b["identifiant"]: f"B{c:06d}" for b, c in zip(billets, codes)}
    return s_ids, s_o1, s_o2, neutre


def passe_1(A, man, billets):
    if os.path.exists(A.sortie) and os.listdir(A.sortie):
        raise Refus(f"dossier de sortie non vide : {A.sortie}")
    s_ids, s_o1, s_o2, neutre = graines(A, billets)
    dcl = os.path.join(A.sortie, "cles")
    os.makedirs(dcl)
    details, sorties, copies = [], {}, {}
    for b in billets:
        i = b["identifiant"]
        brut = open(os.path.join(A.racine, "billets", f"{i}.md"), encoding="utf-8").read()
        if hashlib.sha256(brut.encode("utf-8")).hexdigest() != b["empreinte_sha256_texte"]:
            raise Refus(f"empreinte du texte différente du manifeste : {i}")
        noms, parties = noms_a_masquer(b)
        corps, n_img, n_noms, colles = neutraliser(brut, noms, parties)
        corps, n_avant, ok = inserer_borne(corps)
        titre, _, n_t, _ = neutraliser(b["titre"], noms, parties)
        copies[neutre[i]] = f"# {titre}\n\n{corps}\n"
        details.append({"neutre": neutre[i], "images": n_img, "noms_masques": n_noms + n_t,
                        "marqueurs_colles": colles, "mots_avant_borne": n_avant, "borne_inseree": ok,
                        "borne_dans_un_marqueur": bool(re.search(r"\[[^\]\n]*\n*" + re.escape(BORNE), corps))})
    paires = [(neutre[b["identifiant"]], neutre[b["apparie_a"]]) for b in billets
              if b["classe"] == "bien-note" and b.get("apparie_a") in neutre]
    for k, s in ((1, s_o1), (2, s_o2)):
        d = os.path.join(A.sortie, "passe-1", f"codeur-{k}")
        os.makedirs(os.path.join(d, "billets"))
        for n, txt in copies.items():
            p = os.path.join(d, "billets", f"{n}.md")
            open(p, "w", encoding="utf-8").write(txt)
            sorties[os.path.relpath(p, A.sortie)] = sha_fichier(p)
        o = ordre_sans_paires_adjacentes(sorted(neutre.values()), paires, np.random.default_rng(s))
        open(os.path.join(d, "ordre.txt"), "w").write("\n".join(o) + "\n")
        for src in (A.grille_extrait, A.consigne):
            if src:
                shutil.copy(src, os.path.join(d, os.path.basename(src)))
        for f in os.listdir(d):
            if os.path.isfile(os.path.join(d, f)):
                sorties[os.path.relpath(os.path.join(d, f), A.sortie)] = sha_fichier(os.path.join(d, f))
    table = os.path.join(dcl, "table-de-correspondance.json")
    json.dump({"neutre_vers_site": {v: k for k, v in neutre.items()}}, open(table, "w"), indent=1)
    mots = [d["mots_avant_borne"] for d in details if d["borne_inseree"]]
    manif = {
        "version": "v2", "passe": 1, "moitie": A.moitie, "pilote": A.pilote, "go": A.go,
        "entropie": ENTROPIE_PILOTE if A.pilote else ENTROPIE_TENUE, "numpy": np.__version__,
        "manifeste_v2": {"chemin": A.manifeste, "sha256": sha_fichier(A.manifeste)},
        "billets": len(billets), "paires": len(paires),
        "borne": {"mots_reels_min": min(mots) if mots else None,
                  "mots_reels_mediane": statistics.median(mots) if mots else None,
                  "bornes_dans_un_marqueur": sum(d["borne_dans_un_marqueur"] for d in details),
                  "billets_trop_courts": sum(not d["borne_inseree"] for d in details)},
        "noms_masques_total": sum(d["noms_masques"] for d in details),
        "marqueurs_colles_total": sum(d["marqueurs_colles"] for d in details),
        "details": details, "sorties_sha256": sorties, "table_sha256": sha_fichier(table),
        "fichiers_de_commentaires_ecrits": 0,
    }
    json.dump(manif, open(os.path.join(dcl, "manifeste-preparation-passe-1.json"), "w"), ensure_ascii=False, indent=1)
    print(f"passe 1 : {len(billets)} billets, deux dossiers de codeurs, aucun fichier de commentaires ; sortie {A.sortie}")
    return manif


def passe_2(A, man, billets):
    h1, h2 = verifier_compagnon(A.depot1), verifier_compagnon(A.depot2)
    dcl = os.path.join(A.sortie, "cles")
    table = json.load(open(os.path.join(dcl, "table-de-correspondance.json")))["neutre_vers_site"]
    s_ids, _, _, neutre = graines(A, billets)
    if {v: k for k, v in neutre.items()} != table:
        raise Refus("table de correspondance différente de celle que donne la graine")
    for k, dep in ((1, A.depot1), (2, A.depot2)):
        copies = os.path.join(A.sortie, "passe-1", f"codeur-{k}", "billets")
        rapport = controle.controler_gestes(A.grille, dep, copies)
        if rapport["refus"]:
            raise Refus(f"dépôt du codeur {k} refusé par le contrôle : {rapport['refus'][:3]}")
    dco = os.path.join(A.sortie, "passe-2", "commentaires")
    if os.path.exists(dco):
        raise Refus("passe 2 déjà faite")
    os.makedirs(dco)
    tries = sorted(neutre.values())
    rng_par_billet = dict(zip(tries, s_ids.spawn(len(tries))))
    codables, n_com, n_aut, sorties = {}, 0, 0, {}
    for b in billets:
        if b["classe"] != "bien-note":
            continue
        i = b["identifiant"]
        pc = os.path.join(A.racine, "commentaires", f"{i}.json")
        if not os.path.exists(pc):
            continue
        brut = open(pc, "rb").read()
        if b.get("empreinte_sha256_commentaires") and hashlib.sha256(brut).hexdigest() != b["empreinte_sha256_commentaires"]:
            raise Refus(f"empreinte des commentaires différente du manifeste : {i}")
        retenus = {c["_id"] for c in b["commentaires_retenus"]}
        coms = [c for c in json.loads(brut) if c["_id"] in retenus]
        perm = np.random.default_rng(rng_par_billet[neutre[i]]).permutation(len(coms))
        cid = {coms[k]["_id"]: f"c{r + 1:02d}" for r, k in enumerate(perm)}
        noms, parties = noms_a_masquer(b)
        sortis = []
        for k in perm:
            c = coms[k]
            est_aut = (c.get("user") or {}).get("displayName") in set(noms)
            n_com += 1
            n_aut += est_aut
            texte, _, _, _ = neutraliser(c["contents"]["markdown"] or "", noms, parties)
            par = c.get("parentCommentId")
            sortis.append({"commentaire": cid[c["_id"]],
                           "reponse_a": (cid.get(par, "commentaire non retenu") if par else None),
                           "reponse_d_auteur_ne_pas_coder": est_aut, "texte": texte})
            if not est_aut:
                codables.setdefault(neutre[i], []).append(cid[c["_id"]])
        p = os.path.join(dco, f"{neutre[i]}.json")
        json.dump({"billet": neutre[i], "commentaires": sortis}, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        sorties[os.path.relpath(p, A.sortie)] = sha_fichier(p)
    json.dump({"codables": {k: sorted(v) for k, v in sorted(codables.items())}},
              open(os.path.join(dcl, "commentaires-codables.json"), "w"), indent=1)
    manif = {"version": "v2", "passe": 2, "depots": {"codeur-1": h1, "codeur-2": h2},
             "commentaires": n_com, "reponses_d_auteur": n_aut,
             "codables": sum(len(v) for v in codables.values()), "sorties_sha256": sorties}
    json.dump(manif, open(os.path.join(dcl, "manifeste-preparation-passe-2.json"), "w"), ensure_ascii=False, indent=1)
    print(f"passe 2 : {n_com} commentaires ({n_aut} d'auteur) ; sortie {dco}")
    return manif


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--passe", choices=["1", "2"], required=True)
    for a in ("manifeste", "moitie", "racine", "sortie"):
        ap.add_argument("--" + a, required=True)
    for a in ("go", "pilote", "grille", "grille-extrait", "consigne", "depot1", "depot2"):
        ap.add_argument("--" + a)
    A = ap.parse_args(argv)
    garde(A)  # avant toute lecture
    man = json.load(open(A.manifeste, encoding="utf-8"))
    billets = selection(A, man)
    return passe_1(A, man, billets) if A.passe == "1" else passe_2(A, man, billets)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except (Refus, controle.Refus) as e:
        print("REFUS :", e)
        sys.exit(2)
