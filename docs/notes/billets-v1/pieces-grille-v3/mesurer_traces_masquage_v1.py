"""Mesure les traces d'identification qui restent dans les copies neutres de la moitié DÉVELOPPEMENT,
avant (preparer_copies_neutres_v2.py) et après (preparer_copies_neutres_v3.py) le renforcement du
masquage. Écrit seulement des décomptes, jamais de texte. Les copies sont écrites dans un dossier
temporaire donné en argument, puis supprimées par ce script.

Traces comptées, par version, par classe (bien noté / apparié), en billets touchés et occurrences :
  noms_auteurs : parties (3 lettres et plus) des noms affichés du manifeste restées, majuscule initiale ;
  hotes_identifiants : hôtes de liens restés qui ne sont ni génériques, ni « forum », ni « site » ;
  hote_forum_voisin : hôte du forum voisin du site resté visible (« alignmentforum.org ») ;
  lignes_auteurs : lignes d'auteurs (« Authors: », « by … », « equal contribution ») où une suite de mots
                   à majuscule initiale reste ;
  organisations : noms d'une liste fixe d'organisations et de programmes (non masqués par choix) ;
  marqueur_auteur : présence du marqueur [AUTEUR] (le marqueur lui-même parle) ;
  marqueur_suivi_d_un_nom : « [AUTEUR] Nom » — masquage d'un prénom d'un tiers (excès de masquage).

Usage : python mesurer_traces_masquage_v1.py MANIFESTE_V2 RACINE_DEV DOSSIER_TEMPORAIRE PILOTE_JSON SORTIE_JSON
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
ORGANISATIONS = ["Anthropic", "OpenAI", "DeepMind", "Google", "Apollo", "Conjecture", "Redwood", "METR", "MATS",
                 "SPAR", "AISI", "Simplex", "Goodfire", "EleutherAI", "PIBBSS", "Apart", "Astra", "Transluce",
                 "Neuronpedia", "Alignment Jam", "AI Safety Camp", "SERI", "REMIX", "Cohere", "Meta"]
sys.path.insert(0, ICI)
import preparer_copies_neutres_v3 as v3  # noqa: E402


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def preparer(script, man, racine, sortie):
    subprocess.run([sys.executable, os.path.join(ICI, script), "--passe", "1", "--manifeste", man, "--moitie",
                    "developpement", "--racine", racine, "--sortie", sortie], check=True, capture_output=True)


def compter(sortie, man_billets, pilote):
    table = json.load(open(os.path.join(sortie, "cles", "table-de-correspondance.json")))["neutre_vers_site"]
    res = {}
    for n, i in table.items():
        b = man_billets[i]
        t = open(os.path.join(sortie, "passe-1", "codeur-1", "billets", f"{n}.md"), encoding="utf-8").read()
        noms = [x for x in [b.get("auteur"), *(b.get("coauteurs") or [])] if x]
        parties = {p for x in noms for p in re.findall(r"[^\W\d_]{3,}", x)}
        c = {
            "noms_auteurs": sum(len(re.findall(rf"(?<!\w){re.escape(p)}(?!\w)", t)) for p in parties),
            "hotes_identifiants": len([h for h in re.findall(r"\[lien : ([^\]]+)\]", t)
                                       if h not in v3.HOTES_GENERIQUES and h not in ("forum", "site")
                                       and h not in v3.HOTES_FORUM]),
            "hote_forum_voisin": t.count("[lien : alignmentforum.org]"),
            "lignes_auteurs": 0,
            "organisations": sum(len(re.findall(rf"(?<!\w){re.escape(o)}(?!\w)", t)) for o in ORGANISATIONS),
            "marqueur_auteur": t.count("[AUTEUR]"),
            "marqueur_suivi_d_un_nom": len(re.findall(r"\[AUTEUR\] [A-Z][a-z]+", t)),
        }
        for m in v3.RX_LIGNE_AUTEURS.finditer(t):
            if any(not set(x.split()) <= v3.MOTS_OUTILS for x in v3.RX_NOM_PROPRE.findall(m.group("reste"))):
                c["lignes_auteurs"] += 1
        for m in v3.RX_LIGNE_EGALE.finditer(t):
            if any(not set(x.split()) <= v3.MOTS_OUTILS for x in v3.RX_NOM_PROPRE.findall(m.group(0))):
                c["lignes_auteurs"] += 1
        res[i] = (b["classe"], i in pilote, c)
    agr = {}
    for cle in ("noms_auteurs", "hotes_identifiants", "hote_forum_voisin", "lignes_auteurs", "organisations", "marqueur_auteur",
                "marqueur_suivi_d_un_nom"):
        agr[cle] = {}
        for nom, filtre in (("tous", lambda k, p: True), ("bien_notes", lambda k, p: k == "bien-note"),
                            ("apparies", lambda k, p: k != "bien-note"), ("pilote", lambda k, p: p)):
            sel = [c for k, p, c in res.values() if filtre(k, p)]
            agr[cle][nom] = {"billets": len(sel), "billets_touches": sum(1 for c in sel if c[cle] > 0),
                             "occurrences": sum(c[cle] for c in sel)}
    return agr


def main(man, racine, tmp, pilote_p, sortie):
    mb = {b["identifiant"]: b for b in json.load(open(man, encoding="utf-8"))["billets"] if b["moitie"] == "developpement"}
    pilote = set(json.load(open(pilote_p, encoding="utf-8"))["billets"])
    out = {"version": "v1", "manifeste_v2": sha(man), "organisations_comptees": ORGANISATIONS,
           "scripts": {s: sha(os.path.join(ICI, s)) for s in ("preparer_copies_neutres_v2.py", "preparer_copies_neutres_v3.py")}}
    for script, cle in (("preparer_copies_neutres_v2.py", "avant_v2"), ("preparer_copies_neutres_v3.py", "apres_v3")):
        d = os.path.join(tmp, cle)
        preparer(script, man, racine, d)
        out[cle] = compter(d, mb, pilote)
        out[cle + "_borne"] = json.load(open(os.path.join(d, "cles", "manifeste-preparation-passe-1.json")))["borne"]
        shutil.rmtree(d)
    json.dump(out, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k in ("noms_auteurs", "hotes_identifiants", "hote_forum_voisin", "lignes_auteurs", "organisations", "marqueur_auteur",
              "marqueur_suivi_d_un_nom"):
        print(k, "avant", out["avant_v2"][k]["tous"], "après", out["apres_v3"][k]["tous"])


if __name__ == "__main__":
    main(*sys.argv[1:6])
