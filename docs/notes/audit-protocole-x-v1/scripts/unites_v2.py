"""Unités de proposition tirées des cellules du dernier tour de chaque course incluse.

Unité = une expérience ou proposition nommée par un modèle dans sa dernière cellule :
- sous-titres de la section (b) « expériences corrigées » d'une réponse du tour 3 ;
- à défaut de sous-titres, éléments en gras ou numérotés de cette section ;
- pour une dernière cellule de tour 1 ou 2, titres qui nomment une expérience, une proposition,
  un mécanisme, une piste ou un identifiant court (E1, P2, H3…).
On relève aussi « l'expérience à faire en premier » de chaque modèle (section (c)).
Méthode mécanique : sa précision est mesurée à part sur un échantillon tiré (precision_unites_v1.py).

Version 2 (inventaire v2, branches de données comprises). Sortie : sorties/unites-v2.json (sans texte intégral : extrait, empreinte, chemin, commit).
"""
import hashlib
import json
import re
import sys

from audit_commun_v3 import SORTIES, inventaire, lister, montrer, sections, ESPECE_FOURNISSEUR

MOTIF_ITEM = re.compile(r"(exp[ée]rience|proposition|m[ée]canisme|protocole|piste|id[ée]e|hypoth[èe]se|"
                        r"\b[EPHMDIU]\d|\bD0|duel|test|mesure|plan|banc|r[èe]gle|crit[èe]re|option)", re.I)
MOTIF_NON = re.compile(r"(critique|statut|pi[èe]ces|faits|ce qui est [ée]tabli|n'est pas [ée]tabli|r[ée]ponse [àa] l|"
                       r"d[ée]cision sur|traitement|sur la proposition|bloc \d|r[ée]f[ée]rences|synth[èe]se|socle|"
                       r"pr[ée]ambule|rectifications|^\(?[abc]\)\s|^\d+\.\s*\(?[abc]\)|livrable|calendrier|architecture commune|"
                       r"garde-fous|seuil de d[ée]cision|^conclusion|^verdict)", re.I)


MOTIF_EXP = re.compile(r"(exp[ée]rience|duel|volet|d[ée]cision \d|option|\btest\b|test de|piste|proposition \w|m[ée]canisme|"
                       r"\b[EPDXUCIRMG]\d|\bE\.?[IVX]+\b|\bb\.\d|exp\. ?\d|^\d+\.\d* ?[A-Z]\d)", re.I)
MOTIF_NON2 = re.compile(r"(^[`$\\]*h_|^h[_ ]?[ab]\b|^protocole\b|^m[ée]trique|^cibles|^objet|hypoth[èe]ses? exclusives|"
                        r"^r[èe]gle|^score|^dans le papier|^math|^pour l'usage|^sur la litt|^[A-G]-[abc]\d|classement|"
                        r"^falsification|^faisabilit|^dispositif|^param[èe]tre|^pr[ée]requis|^contr[ôo]les?$|^co[ûu]t|"
                        r"^lecture|^issue|^ce que chaque|^bras|^unit[ée]|^seuil|^calendrier|faire en premier)", re.I)


def garde(titre):
    t = re.sub(r"^[#*\s`$]+", "", titre)
    return bool(MOTIF_EXP.search(t)) and not MOTIF_NON.search(t) and not MOTIF_NON2.search(t)


def lettre(nom):
    m = re.search(r"-([A-Z])\.md$", nom)
    return m.group(1) if m else None


def tour(nom):
    m = re.search(r"T(\d)", nom)
    return int(m.group(1)) if m else 0


def items_gras(lignes):
    out = []
    for i, l in enumerate(lignes):
        m = re.match(r"^\s*(?:\d+[.)]\s*|[-*]\s*)?\*\*([^*]{4,140})\*\*", l)
        if m and not MOTIF_NON.search(m.group(1)):
            out.append((m.group(1).strip(" .:—-"), i))
    return out


def extraire(texte, t):
    secs, lignes = sections(texte)
    unites, premier = [], None
    sec_b = next((s for s in secs if re.match(r"^\(?b\)|^b\s*[—\-.]", s[1].strip(), re.I)
                  or re.search(r"exp[ée]riences? corrig", s[1], re.I)), None)
    if t >= 3 and sec_b:
        niv, _, d, f = sec_b
        enfants = [s for s in secs if d < s[2] < f and garde(s[1])]
        # feuilles retirées si leur parent est déjà une unité (on garde le niveau le plus haut qui passe la garde)
        enfants = [s for s in enfants if not any(p[2] < s[2] < p[3] and p[0] < s[0] for p in enfants)]
        if enfants:
            for s in enfants:
                unites.append((s[1], "\n".join(lignes[s[2]:s[3]])))
        else:
            g = [x for x in items_gras(lignes[d:f]) if garde(x[0])]
            for k, (titre, i) in enumerate(g):
                fin = g[k + 1][1] if k + 1 < len(g) else f - d
                unites.append((titre, "\n".join(lignes[d + i:d + fin])))
            if not g:
                unites.append(("(b) entière", "\n".join(lignes[d:f])))
    else:
        cand = [s for s in secs if s[0] >= 2 and garde(s[1])]
        cand = [s for s in cand if not any(p[2] < s[2] < p[3] and p[0] < s[0] for p in cand)]
        for s in cand:
            unites.append((s[1], "\n".join(lignes[s[2]:s[3]])))
        if not unites:
            g = [x for x in items_gras(lignes) if garde(x[0])]
            for k, (titre, i) in enumerate(g):
                fin = g[k + 1][1] if k + 1 < len(g) else len(lignes)
                unites.append((titre, "\n".join(lignes[i:fin])))
    # Premier choix
    for s in secs:
        if re.search(r"(en premier|à faire d'abord|premi[èe]re exp[ée]rience|first)", s[1], re.I):
            premier = "\n".join(lignes[s[2]:s[3]])
    if premier is None:
        m = re.search(r"(?is)(exp[ée]rience [àa] faire en premier|[àa] faire en premier)(.{0,1500})", texte)
        if m:
            premier = m.group(0)
    # Feuilles seulement : on retire une unité qui contient une autre unité (titre parent)
    return unites, premier


def main():
    inv = [d for d in inventaire() if d.get("type") == "course" and d["statut_audit"] == "inclus"]
    sortie = {"unites": [], "premiers": [], "cellules": []}
    for d in inv:
        fichiers = [f for f in lister(d["branche"], d["racine"] + "/")
                    if re.search(r"/(cellules|abonnement/reponses)/[^/]+\.md$", f)]
        parlettre = {}
        for f in fichiers:
            L = lettre(f)
            if not L:
                continue
            t = tour(f.rsplit("/", 1)[1])
            # cellule de dernier tour ; à égalité, la cellule (dossier cellules/) prime sur la copie d'abonnement
            cle = (t, "/cellules/" in f)
            if L not in parlettre or cle > parlettre[L][0]:
                parlettre[L] = (cle, f)
        for L, ((t, _), f) in sorted(parlettre.items()):
            texte = montrer(d["branche"], f) or ""
            esp = (d["lettres"].get(L) or {}).get("espece", "inconnu")
            unites, premier = extraire(texte, t)
            sortie["cellules"].append({"racine": d["racine"], "lettre": L, "espece": esp, "tour": t, "chemin": f,
                                       "commit": d["commit"], "caracteres": len(texte), "n_unites": len(unites),
                                       "sha256": hashlib.sha256(texte.encode()).hexdigest()})
            for k, (titre, corps) in enumerate(unites):
                sortie["unites"].append({
                    "id": f"{d['racine'].rsplit('/', 1)[-1][:60]}#{L}#{k + 1}", "racine": d["racine"],
                    "rejeu_de": d.get("rejeu_de"), "lettre": L, "espece": esp,
                    "fournisseur": ESPECE_FOURNISSEUR.get(esp, "autre"), "tour": t, "titre": titre[:200],
                    "extrait": re.sub(r"\s+", " ", corps)[:300], "corps_caracteres": len(corps),
                    "chemin": f, "commit": d["commit"]})
            if premier:
                sortie["premiers"].append({"racine": d["racine"], "rejeu_de": d.get("rejeu_de"), "lettre": L,
                                           "espece": esp, "tour": t, "chemin": f,
                                           "texte": re.sub(r"\s+", " ", premier)[:1500]})
    (SORTIES / "unites-v2.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1))
    print(len(sortie["cellules"]), "cellules ;", len(sortie["unites"]), "unités ;", len(sortie["premiers"]), "premiers choix")
    return 0


if __name__ == "__main__":
    sys.exit(main())
