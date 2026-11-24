"""Propositions retenues et non retenues, lues dans les notes de sortie et les synthèses des courses.

La note de sortie est ici la seule trace de la sélection (qui retient quoi) : elle sert à marquer les
unités tirées des cellules, non à les remplacer. Chaque élément retenu est rattaché :
- aux lettres que la note déclare (« portée par », « (A, B) », noms de modèles, « les cinq », « tous ») ;
- sinon, au modèle dont l'unité de dernier tour est la plus proche (similarité de mots), marqué « par similarité ».

Version 2 (inventaire v2, branches de données comprises). Sortie : sorties/retenues-v2.json.
"""
import json
import re
import sys

from audit_commun_v3 import SORTIES, Tfidf, cos, inventaire, montrer, sections

V9 = "docs/notes/collisionneur-v9/notes-de-sortie-v1/"
SX = "docs/notes/collisionneur-v9/syntheses-protocole-x-v1/"
R = "runs/collisionneur-protocole-x-"
NOTES = [
    ("main", V9 + "note-sortie-bancs-plantes-v1.md", [R + "bancs-plantes-cinq-decisions-v1-20261122-131546"]),
    ("main", V9 + "note-sortie-billet-drapeau-v1.md", [R + "billet-drapeau-v1-20261122-110018"]),
    ("main", V9 + "note-sortie-coeurs-algorithmiques-v1.md", [R + "coeurs-algorithmiques-v1-20261122-114352"]),
    ("main", V9 + "note-sortie-conscience-anesthesie-neutre-v1.md", [R + "conscience-anesthesie-neutre-abonnement-v1-20261122-153110"]),
    ("main", V9 + "note-sortie-jumeau-generale-v1.md", [R + "generale-isole-jumeau-abonnement-v1-20261122-142638"]),
    ("main", V9 + "note-sortie-papier-a-v1.md", [R + "papier-a-isole-v1-20261122-112512"]),
    ("main", V9 + "note-sortie-papier-b-v1.md", [R + "papier-b-isole-v1-20261122-112512"]),
    ("main", V9 + "note-sortie-puits-etroits-v1.md", [R + "puits-etroits-abonnement-v1-20261122-142638"]),
    ("main", V9 + "note-sortie-revendications-v1.md", [R + "revendications-v1-20261122-080928"]),
    ("main", SX + "note-synthese-idees-originales-v1.md", [R + "idees-originales-v1-20261122-114352"]),
    ("main", SX + "note-synthese-questions-concurrents-v1.md", [R + "questions-concurrents-v1-20261122-083333"]),
    ("main", SX + "note-propositions-retenues-six-dossiers-v1.md",
     [R + "coercition-v1-20261122-061053", R + "problematique-papier-v1-20261122-061053", R + "tirage-au-hasard-v1-20261122-080414",
      R + "generale-isole-v1-20261122-080928"]),
    ("runs/collisionneurs-reprise-2026-11-24-v1", V9 + "note-sortie-boucle-organisme-controle-v1.md",
     ["docs/notes/collisionneurs-reprise-2026-11-24-v1/boucle-organisme-controle/principal",
      "docs/notes/collisionneurs-reprise-2026-11-24-v1/boucle-organisme-controle/temoin"]),
    ("runs/collisionneurs-reprise-2026-11-24-v1", V9 + "note-sortie-cible-publication-papier-d-v1.md",
     ["docs/notes/collisionneurs-reprise-2026-11-24-v1/cible-publication/collisionneur"]),
    ("protocole-x/entrainement-et-juges-v1", "docs/notes/protocole-x-entrainement-et-juges-v1/note-de-sortie-collisionneur-dossier-1-v2.md",
     [R + "programme-ameliore-entrainement-cinq-modeles-v1-20261124-125147"]),
    ("main", "docs/notes/collisionneur-bassins-etroits-v1/synthese-v1.md", ["docs/notes/collisionneur-bassins-etroits-v1/run-e3-v1"]),
    ("main", "docs/notes/collisionneur-conception-qo1-q1-v1/synthese-v1.md", ["docs/notes/collisionneur-conception-qo1-q1-v1/run-e3-v1"]),
    ("main", "docs/notes/collisionneur-diversite-idees-v1/synthese-v1.md", ["docs/notes/collisionneur-diversite-idees-v1/run-e3-v1"]),
    ("main", "docs/notes/collisionneur-experimentateur-v1/synthese-v1.md", ["docs/notes/collisionneur-experimentateur-v1/run-e3-v1"]),
    ("main", "docs/notes/regard-ou-raisons-confondants-v1/bilan-mere-v1.md",
     ["docs/notes/regard-ou-raisons-confondants-v1/collisionneur-v1/run-e3-v1"]),
    ("main", "docs/notes/papier-dopamine-moniteur-v1/collisionneur-seuil-et-moniteurs-v1/synthese-collisionneur-seuil-et-moniteurs-v1.md",
     ["runs/collisionneur-seuil-moniteurs-v1-20261121-063125"]),
    ("main", "docs/notes/papier-dopamine-moniteur-v1/synthese-collisionneur-tours-2-3-v1.md",
     ["runs/collisionneur-dopamine-v1-20261120-122457"]),
    # Version 2 : synthèses des courses lues sur les branches de données (octobre et début novembre)
    ("main", "docs/notes/audit-controle-v1/synthese-collisionneur-v1.md", ["collisionneur-audit-controle/run-audit-controle-e3-v1"]),
    ("main", "docs/notes/bisociation-litterature-reelle-v1/collisionneur-question-6-v1/synthese-question-6-v2.md",
     ["donnees/collisionneur-question-6-v1/run-question-6-e3-v1"]),
    ("main", "docs/notes/couche-2-preparation-v1/collisionneur-pilote-v1/synthese-collisionneur-pilote-v1.md",
     ["donnees/collisionneur-pilote-couche-2-v1/run-pilote-e3-v1"]),
    ("main", "docs/notes/porte-g0-repli-v1/synthese-collisionneur-repli-g0-v1.md",
     ["donnees/collisionneur-repli-g0-v1/run-repli-g0-e3-v2", "donnees/collisionneur-repli-g0-v1/run-repli-g0-e3-v1"]),
    ("main", "docs/notes/collisionneur-boucle-d-or-v1/synthese-boucle-d-or-v1.md", ["collisionneur-boucle-d-or/run-boucle-d-or-e3-v1"]),
    ("main", "docs/notes/collisionneur-pari-de-signe-v1/synthese-pari-de-signe-v1.md", ["collisionneur-pari-de-signe/run-pari-de-signe-e3-v1"]),
    ("main", "docs/notes/collisionneur-proposeur-enfichable-v1/synthese-proposeur-enfichable-v1.md",
     ["collisionneur-proposeur-enfichable/proposeur-v2/run-proposeur-v2-e3-v1", "collisionneur-proposeur-enfichable/proposeur-v1/run-proposeur-e3-v1"]),
    ("main", "docs/notes/collisionneur-memoire-encodage-v1/synthese-memoire-encodage-v3-v1.md",
     ["collisionneur-memoire-encodage-v3/run-memoire-encodage-v3-e3-v1"]),
    ("runs/collisionneurs-reprise-v8d-v1", "docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-tour2-v1.md",
     ["donnees/collisionneur-v8-runs-v1/n12-n13-tour2/run-n12-n13-tour2-e3-v1"]),
    ("runs/collisionneurs-reprise-v8d-v1", "docs/notes/ideation-organisme-v1/course-2/synthese-collisionneur-question-mere-v2-v1.md",
     ["donnees/collisionneur-question-mere-v2/run-question-mere-e3-v2"]),
    ("runs/collisionneurs-reprise-v8d-v1", "docs/notes/ideation-organisme-v1/bisociation-deux-espaces-v1/synthese-collisionneur-bisociation-v1.md",
     ["donnees/collisionneur-bisociation-v1/run-bisociation-e3-v1"]),
]

DEFAUT = (r"^(\d+\.\s*)?(retenues?|propositions retenues(, et pourquoi)?|les meilleures propositions retenues.*)$",
          r"^non retenues", r"[àa] reprendre")
PARTICULIER = {
    "note-propositions-retenues-six-dossiers-v1.md": (r"^en bref", r"$^", r"$^"),
    "collisionneur-bassins-etroits-v1/synthese-v1.md": (r"recommandation [àa] pr[ée]parer", r"$^", r"$^"),
    "collisionneur-conception-qo1-q1-v1/synthese-v1.md": (r"d[ée]cision que la synth[èe]se soutient", r"$^", r"$^"),
    "collisionneur-diversite-idees-v1/synthese-v1.md": (r"^recommandation", r"$^", r"$^"),
    "collisionneur-experimentateur-v1/synthese-v1.md": (r"recommandation du lecteur", r"$^", r"$^"),
    "bilan-mere-v1.md": (r"exp[ée]rience d[ée]cisive la moins ch[èe]re", r"$^", r"$^"),
    "note-synthese-questions-concurrents-v1.md": (r"exp[ée]riences [àa] faire en premier", r"$^", r"$^"),
    "synthese-collisionneur-seuil-et-moniteurs-v1.md": (r"$^", r"$^", r"$^"),
    "synthese-collisionneur-tours-2-3-v1.md": (r"$^", r"$^", r"$^"),
    "audit-controle-v1/synthese-collisionneur-v1.md": (r"^4\.a retenues", r"^4\.b non retenues", r"$^"),
    "synthese-question-6-v2.md": (r"exp[ée]riences d[ée]cisives retenues", r"$^", r"$^"),
    "synthese-collisionneur-pilote-v1.md": (r"pilote recommand", r"$^", r"$^"),
    "synthese-collisionneur-repli-g0-v1.md": (r"clause recommand", r"$^", r"$^"),
    "synthese-boucle-d-or-v1.md": (r"premi[èe]re action recommand", r"$^", r"$^"),
    "synthese-pari-de-signe-v1.md": (r"^recommandation des trois", r"$^", r"$^"),
    "synthese-proposeur-enfichable-v1.md": (r"^recommandation des trois", r"$^", r"$^"),
    "synthese-memoire-encodage-v3-v1.md": (r"premi[èe]re action recommand", r"$^", r"$^"),
    "synthese-n12-n13-tour2-v1.md": (r"^B\.4", r"^F\.4", r"$^"),
    "synthese-collisionneur-question-mere-v2-v1.md": (r"recommandation pour la course", r"$^", r"$^"),
    "bisociation-deux-espaces-v1/synthese-collisionneur-bisociation-v1.md": (r"recommandation pour le pr[ée]enregistrement", r"$^", r"$^"),
}
PRIO = re.compile(r"(propositions? retenues|^retenues?\b|propositions les plus fortes|^en bref)", re.I)
RET = re.compile(r"(retenu|rang \d|recommand|premi[èe]re action|exp[ée]riences? d[ée]cisives?|d[ée]cision que la synth|"
                 r"exp[ée]rience d[ée]cisive|ordre propos|l'exp[ée]rience [àa] faire)", re.I)
NONRET = re.compile(r"(non retenu|[ée]cart[ée]|rejet|abandonn)", re.I)
NOMS = {"fable": ["fable"], "opus": ["opus"], "argon": ["argon"], "carbon": ["carbon"], "neon": ["neon"],
        "astra": ["astra", "gpt"], "kimi": ["kimi"], "fable51": ["fable 5.1"], "opus46": ["opus 4.6"]}


def elements(lignes, d, f):
    """Éléments d'une section : lignes de tableau, puces de premier niveau, sous-titres."""
    out, entete = [], None
    i = d + 1
    while i < f:
        l = lignes[i]
        if l.startswith("|"):
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if i + 1 < f and re.match(r"^\|\s*:?-{3}", lignes[i + 1]):
                entete = [c.lower() for c in cells]
                i += 2
                continue
            if not re.match(r"^\|\s*:?-{3}", l):
                out.append(("tableau", " | ".join(cells), entete, cells))
        elif re.match(r"^\s*[-*]\s+\*[A-Za-zÀ-ÿ ]+\*\s*:", l) and out and out[-1][0] in ("puce", "gras"):
            f0, t0, e0, c0 = out[-1]
            out[-1] = (f0, t0 + " " + l.strip(), e0, c0)  # sous-puce « *Soutien* : … » rattachée à son élément
        elif re.match(r"^\*\*\d+[.)]", l):
            out.append(("gras", l, None, None))
        elif re.match(r"^(\d+[.)]|[-*])\s+", l):
            corps = [l]
            j = i + 1
            while j < f and lignes[j].strip() and not re.match(r"^(\d+[.)]|[-*]|#|\|)\s*", lignes[j]):
                corps.append(lignes[j])
                j += 1
            out.append(("puce", " ".join(corps), None, None))
            i = j - 1
        elif re.match(r"^#{3,5}\s", l):
            out.append(("titre", l.lstrip("# "), None, None))
        i += 1
    return out


def porteurs(texte, entete, cells, lettres):
    t = texte
    if entete and cells:
        for k, h in enumerate(entete):
            if re.search(r"port[ée]|soutenu|qui|lettres?|mod[èe]les", h) and k < len(cells):
                t = cells[k]
                break
    tl = t.lower()
    m = re.search(r"\bles (trois|quatre|cinq|six|sept|huit|neuf)\b", tl)
    if m:
        n = ["trois", "quatre", "cinq", "six", "sept", "huit", "neuf"].index(m.group(1)) + 3
        return sorted(lettres)[:n], "déclarée"
    if re.search(r"\b(tous|toutes|unanim)", tl):
        return sorted(lettres), "déclarée"
    trouv = set()
    for L, v in lettres.items():
        for n in NOMS.get(v.get("espece") or "", []):
            if n in tl:
                trouv.add(L)
    for m in re.finditer(r"(?<![A-Za-z0-9])([A-I])(?![A-Za-z0-9'’])", t):
        if m.group(1) in lettres:
            trouv.add(m.group(1))
    return sorted(trouv), ("déclarée" if trouv else None)


def main():
    inv = {d["racine"]: d for d in inventaire()}
    unites = json.loads((SORTIES / "unites-v2.json").read_text())["unites"]
    tf = Tfidf([u["extrait"] + " " + u["titre"] for u in unites])
    sortie = []
    for branche, chemin, racines in NOTES:
        texte = montrer(branche, chemin)
        if texte is None:
            print("absente :", chemin)
            continue
        secs, lignes = sections(texte)
        regles = next((v for k, v in PARTICULIER.items() if chemin.endswith(k)), DEFAUT)
        choisies = [s for s in secs if re.search(regles[0], s[1].strip(), re.I)]
        nonret = [s for s in secs if re.search(regles[1], s[1].strip(), re.I)]
        reprendre = [s for s in secs if re.search(regles[2], s[1].strip(), re.I)]
        if not choisies:
            print("aucune section de sélection :", chemin)
        lettres = {}
        for r in racines:
            lettres.update(inv.get(r, {}).get("lettres", {}))
        candidats = [u for u in unites if u["racine"] in racines]
        vus = []
        dossier_courant = None
        SIX = {"coercition": R + "coercition-v1-20261122-061053", "problématique du papier": R + "problematique-papier-v1-20261122-061053",
               "tirage au hasard": R + "tirage-au-hasard-v1-20261122-080414", "question générale": R + "generale-isole-v1-20261122-080928"}
        for genre, groupe in (("retenue", choisies), ("à reprendre", reprendre), ("non retenue", nonret)):
            for s in groupe:
                els = elements(lignes, s[2], s[3])
                if not els and genre == "retenue":
                    els = [("section", " ".join(lignes[s[2] + 1:s[3]]), None, None)]
                for (forme, txt, entete, cells) in els:
                    txt = re.sub(r"\s+", " ", txt).strip()
                    if len(txt) < 25 or (entete and not cells):
                        continue
                    if genre == "retenue" and txt.startswith("- ") and re.search(r"(aucun soutien|non suivies?|non contr[ôo]l[ée]s|retir[ée]s?\b|^- \*\*(les?|la|l')\b)", txt, re.I):
                        genre_eff = "non retenue"
                    else:
                        genre_eff = genre
                    v = tf.vec(txt)
                    if any(cos(v, w) > 0.6 for w in vus):
                        continue
                    vus.append(v)
                    racines_el = racines
                    if chemin.endswith("note-propositions-retenues-six-dossiers-v1.md") and cells:
                        if cells[0]:
                            dossier_courant = cells[0].lower()
                        if dossier_courant not in SIX:
                            continue  # dossier qui a sa propre note de sortie : compté là-bas
                        racines_el = [SIX[dossier_courant]]
                    pl, att = porteurs(txt, entete, cells, {k: v for k, v in lettres.items()
                                                             if any(k in inv.get(r, {}).get("lettres", {}) for r in racines_el)})
                    proches = sorted(((cos(v, tf.vec(u["extrait"] + " " + u["titre"])), u) for u in candidats),
                                     key=lambda x: -x[0])[:3]
                    if not pl and proches and proches[0][0] > 0.05:
                        pl, att = [proches[0][1]["lettre"]], "par similarité"
                    sortie.append({
                        "note": chemin, "branche": branche, "section": s[1][:120], "genre": genre_eff, "forme": forme,
                        "texte": txt[:600], "racines": racines_el, "lettres_porteuses": pl,
                        "especes_porteuses": sorted({(lettres.get(L) or {}).get("espece", "?") for L in pl}),
                        "attribution": att or "aucune",
                        "unites_proches": [{"id": u["id"], "sim": round(c, 3)} for c, u in proches]})
    (SORTIES / "retenues-v2.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1))
    from collections import Counter
    print(len(sortie), Counter(x["genre"] for x in sortie), Counter(x["attribution"] for x in sortie))

    return 0


if __name__ == "__main__":
    sys.exit(main())
