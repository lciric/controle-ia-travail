"""Inventaire des dossiers du collisionneur et du protocole X, lu sur les données brutes.

Audit du protocole X, version 1 (règle 9 du protocole X v2). Aucun appel réseau, aucun modèle.
Lit les fichiers par `git show <branche>:<chemin>` ; ne lit rien d'un dossier exclu pour cloisonnement
(le filtre porte sur le chemin, avant toute lecture).

Version 2 : ajoute les branches donnees/collisionneur-* (mot de la mère du 24 novembre vers 18:57Z :
cellules, questions servies, journaux et notes seulement ; même test d'exclusion par noms et en-têtes ;
rien d'autre sous donnees/). Branche gardée par course : celle qui porte le plus de cellules ; les
copies « -suite » et « -run » d'une même course sont rapprochées (la plus complète est gardée).
Sortie : sorties/inventaire-v2.json et sorties/inventaire-v2.csv.
"""
import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ICI = Path(__file__).resolve().parent
SORTIES = ICI.parent / "sorties"

BRANCHES = [
    "main",
    "runs/collisionneurs-reprise-2026-11-24-v1",
    "runs/collisionneurs-reprise-v8d-v1",
    "protocole-x/entrainement-et-juges-v1",
    "runs/collisionneurs-reprise-minuit-v1",
    "runs/collisionneurs-partiels-passation-2026-11-24-0620",
    "idees/protocole-x-structure-du-langage-fable-v1",
]
BRANCHES_DONNEES = [l.split()[1] for l in subprocess.run(["git", "ls-remote", "--heads", "origin", "donnees/collisionneur-*"],
                                                       capture_output=True, text=True).stdout.splitlines()]
BRANCHES_DONNEES = sorted(b.replace("refs/heads/", "") for b in BRANCHES_DONNEES)
# exclues par leur nom, avant toute lecture
BRANCHES_DONNEES_EXCLUES = [b for b in BRANCHES_DONNEES if "evasion-moniteurs" in b or "verite-dommage" in b]
BRANCHES += [b for b in BRANCHES_DONNEES if b not in BRANCHES_DONNEES_EXCLUES]

# Exclusion par le chemin, AVANT toute lecture (cloisonnement : objet ou en-tête cloisonné, ou doute).
EXCLU_CLOISONNEMENT = [
    ("modes-attaque", "attaques contre les moniteurs (branche coffre/ homonyme)"),
    ("lot-quarantaine", "lot de cas tenu à l'écart (quarantaine)"),
    ("taches-sabotage", "tâches de sabotage : doute sur les modes de sabotage"),
    ("v3-reserve", "« réserve » : doute sur une marque « réservé »"),
    ("organismes-discrets", "organismes discrets : textes du bras A cloisonnés pour les concepteurs"),
    ("modes-et-attaques", "session déclarée « cloisonnée » dans son en-tête"),
    ("evasion-moniteurs", "évasion des moniteurs : attaque contre les moniteurs (doute)"),
    ("service-collisionneur-modes", "service des modes de sabotage"),
    ("protocole-x-attaquant", "côté attaquant qui connaît le dispositif (doute)"),
    ("evasion-moniteurs", "évasion des moniteurs : attaque contre les moniteurs (doute)"),
    ("verite-dommage", "vérité du dommage des modes non chiffrés (doute)"),
]
MOTIF_EN_TETE = re.compile(r"(cloisonn|côté exposé|cote expose|réservé aux|ne pas servir aux concepteurs|quarantaine|"
                           r"attaques? contre les moniteurs|modes? (de sabotage )?non chiffr)", re.I)
HORS_PERIMETRE = [
    ("gemini/", "organisme d'idéation Gemini d'octobre : ni collisionneur ni protocole X"),
]


def git(*args):
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    return r.stdout


def montrer(branche, chemin):
    r = subprocess.run(["git", "show", f"origin/{branche}:{chemin}"], capture_output=True)
    return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else None


def lister(branche, prefixe):
    args = ["ls-tree", "-r", "--name-only", f"origin/{branche}"] + ([prefixe] if prefixe else [])
    return [x for x in git(*args).split("\n") if x]


def commit(branche):
    return git("rev-parse", f"origin/{branche}").strip()


def exclusion(chemin):
    for motif, raison in EXCLU_CLOISONNEMENT:
        if motif in chemin:
            return "exclu-cloisonnement", raison
    for motif, raison in HORS_PERIMETRE:
        if motif in chemin:
            return "hors-perimetre", raison
    return None, None


def racines_de_course():
    """Racines de course : dossiers qui portent un sous-dossier cellules/ ; branche qui en porte le plus."""
    compte = {}
    for b in BRANCHES:
        c = {}
        for f in lister(b, ""):
            m = re.match(r"(.+?)/(cellules|abonnement/reponses)/[^/]+\.md$", f)
            if not m or m.group(1) in ("brouillons", "prereg"):
                continue
            c[m.group(1)] = c.get(m.group(1), 0) + 1
        for r, n in c.items():
            if r not in compte or n > compte[r][1]:
                compte[r] = (b, n)
    return {r: b for r, (b, n) in compte.items()}


ESPECE_FOURNISSEUR = {
    "fable": "Anthropic", "opus": "Anthropic", "opus46": "Anthropic", "fable51": "Anthropic",
    "sonnet": "Anthropic", "haiku": "Anthropic",
    "argon": "Google", "carbon": "Google", "neon": "Google", "gemini": "Google",
    "astra": "OpenAI", "kimi": "Moonshot", "mistral": "Mistral", "deepseek": "DeepSeek",
}


def espece_de(modele):
    m = (modele or "").lower()
    for cle in ["fable-5-1", "opus-4-6"]:
        if cle in m:
            return {"fable-5-1": "fable51", "opus-4-6": "opus46"}[cle]
    for e in ["fable", "opus", "sonnet", "haiku", "argon", "carbon", "neon", "astra", "kimi", "mistral", "deepseek"]:
        if e in m:
            return e
    if "gemini" in m:
        return "gemini"
    return m or "inconnu"


def tour_de(nom):
    m = re.search(r"T(\d)", nom)
    return int(m.group(1)) if m else None


def lettre_de(nom):
    m = re.search(r"-([A-Z])(?:\.md)?$", nom.replace(".md", ""))
    return m.group(1) if m else None


def lire_journal(branche, racine, fichiers):
    lignes = []
    for f in fichiers:
        if re.search(r"journal[^/]*\.jsonl$", f) and f.count("/") == racine.count("/") + 1:
            t = montrer(branche, f) or ""
            for l in t.splitlines():
                try:
                    lignes.append(json.loads(l))
                except json.JSONDecodeError:
                    pass
    return lignes


def premiere_ligne_titre(texte):
    for l in (texte or "").splitlines():
        if l.startswith("#"):
            return l.lstrip("# ").strip()[:200]
    return None


def reformulateur(texte):
    """Repère, dans l'en-tête de la question, qui a reformulé (sans interpréter le fond)."""
    tete = "\n".join((texte or "").splitlines()[:40]).lower()
    if "reformul" not in tete and "neutre" not in tete:
        return "non déclaré"
    if re.search(r"reformul\w*[^.\n]{0,80}fable|fable[^.\n]{0,80}reformul", tete):
        return "Fable"
    if re.search(r"reformul\w*[^.\n]{0,80}opus|opus[^.\n]{0,80}reformul", tete):
        return "Opus"
    if "neutre" in tete:
        return "question neutre, auteur non déclaré dans l'en-tête"
    return "déclaré, auteur non repéré"


RUN_DE_PREMIERE_ETAPE = {
    "protocole-x-boucle-organisme-controle-v1": "docs/notes/collisionneurs-reprise-2026-11-24-v1/boucle-organisme-controle/principal",
    "protocole-x-conscience-anesthesie-v1": "runs/collisionneur-protocole-x-conscience-anesthesie-neutre-abonnement-v1-20261122-153110",
}


def premiere_etape():
    """Dossiers « demande approfondie » du protocole X (réponse de Fable, réponse d'Opus, contre-lecture)."""
    sortie = []
    for dd in sorted(Path("docs/notes").glob("protocole-x-*-v1")):
        nom = dd.name
        statut, raison = exclusion(str(dd))
        d = {"racine": str(dd), "branche": "main", "commit": commit("main")[:12], "type": "premiere-etape",
             "statut_audit": statut or "inclus", "raison_exclusion": raison}
        if statut:
            sortie.append(d)
            continue
        f = sorted(str(x.relative_to(dd)) for x in dd.rglob("*.md"))
        d.update({
            "reponses_fable": [x for x in f if x.startswith("reponse-fable") and "erratum" not in x],
            "errata_fable": [x for x in f if "erratum" in x],
            "reponse_opus": [x for x in f if "opus-max" in x and x.split("/")[-1].startswith("reponse")],
            "contre_lectures": [x for x in f if x.startswith("contre-lecture")],
            "verifications": [x for x in f if x.startswith("verification")],
            "comparaisons": [x for x in f if "comparaison" in x],
            "questions_collisionneur": [x for x in f if x.split("/")[-1].startswith("question") and "collisionneur" in x],
            "questions_organisme": [x for x in f if "question-organisme" in x or "sous-question-organisme" in x],
            "course_collisionneur_trouvee": RUN_DE_PREMIERE_ETAPE.get(nom),
            "especes": sorted({"fable"} | ({"opus"} if any("opus-max" in x for x in f) else set())),
        })
        sortie.append(d)
    return sortie


def main():
    racines = racines_de_course()
    dossiers = []
    for racine, branche in sorted(racines.items()):
        statut, raison = exclusion(racine)
        d = {"racine": racine, "branche": branche, "commit": commit(branche)[:12], "type": "course",
             "statut_audit": statut or "inclus", "raison_exclusion": raison}
        if statut:
            dossiers.append(d)
            continue
        fichiers = lister(branche, racine + "/")
        tetes = [f for f in fichiers if re.search(r"/(question|faits)[^/]*\.md$", f) and f.count("/") == racine.count("/") + 1]
        if any(MOTIF_EN_TETE.search("\n".join((montrer(branche, f) or "").splitlines()[:15])) for f in tetes):
            d["statut_audit"], d["raison_exclusion"] = "exclu-cloisonnement", "marque de cloisonnement dans l'en-tête de la question ou des faits"
            dossiers.append(d)
            continue
        cellules = [f for f in fichiers if re.search(r"/(cellules|abonnement/reponses)/[^/]+\.md$", f)]
        q = next((f for f in fichiers if re.search(r"/question[^/]*\.md$", f) and f.count("/") == racine.count("/") + 1), None)
        fa = next((f for f in fichiers if re.search(r"/faits[^/]*\.md$", f) and f.count("/") == racine.count("/") + 1), None)
        tq = montrer(branche, q) if q else None
        tf = montrer(branche, fa) if fa else None
        esp = montrer(branche, racine + "/especes.json")
        lettres = {}
        if esp:
            try:
                for L, v in json.loads(esp).get("lettres", {}).items():
                    lettres[L] = {"espece": v.get("espece"), "modele": v.get("id")}
            except json.JSONDecodeError:
                pass
        journal = lire_journal(branche, racine, fichiers)
        appels = [x for x in journal if x.get("cellule")]
        for x in appels:
            L = lettre_de(x["cellule"])
            if L and L not in lettres:
                lettres[L] = {"espece": x.get("espece") or espece_de(x.get("modele_servi") or x.get("modele")),
                              "modele": x.get("modele_servi") or x.get("modele_demande") or x.get("modele")}
        # Lettres présentes dans les cellules mais absentes du journal et de especes.json
        for c in cellules:
            L = lettre_de(c.rsplit("/", 1)[1])
            if L and L not in lettres:
                lettres[L] = {"espece": "inconnu", "modele": None}
        tours = sorted({t for t in (tour_de(c.rsplit("/", 1)[1]) for c in cellules) if t})
        statuts = Counter(x.get("statut") for x in appels)
        pannes = [{"cellule": x["cellule"], "statut": x.get("statut"), "echec": x.get("echec"),
                   "refus": x.get("categorie_refus"), "espece": x.get("espece")}
                  for x in appels if x.get("statut") not in ("OK", None)]
        compte = sum(float(x.get("cout_usd") or 0) for x in appels)
        # « payé au pire » : somme des plafonds de pire par appel, quand le journal les donne
        pire = sum(float(x.get("cout_pire_usd") or 0) for x in appels if x.get("cout_pire_usd") is not None)
        quand = [x.get("debut") or x.get("quand") for x in journal if (x.get("debut") or x.get("quand"))]
        d.update({
            "question_fichier": q, "question_sha256": hashlib.sha256((tq or "").encode()).hexdigest() if tq else None,
            "question_titre": premiere_ligne_titre(tq), "faits_fichier": fa,
            "reformulateur_en_tete": reformulateur((tq or "") + "\n" + (tf or "")),
            "lettres": lettres,
            "especes": sorted({v["espece"] for v in lettres.values() if v.get("espece")}),
            "fournisseurs": sorted({ESPECE_FOURNISSEUR.get(v["espece"], "autre") for v in lettres.values() if v.get("espece")}),
            "n_modeles": len(lettres), "tours": tours, "n_cellules": len([c for c in cellules if not c.endswith(".sha256")]),
            "appels_journal": len(appels), "statuts": dict(statuts), "n_pannes": len(pannes), "pannes": pannes,
            "compte_usd": round(compte, 4), "pire_usd": round(pire, 4) if pire else None,
            "debut": min(quand) if quand else None, "fin": max(quand) if quand else None,
            "rejeu_de": re.sub(r"-rejeu-.*$", "", racine) if "-rejeu-" in racine else None,
            "bras_temoin": "temoin" in racine,
        })
        dossiers.append(d)
    # Doublons partiels : copie d'un relais pris avant la fin de la même course.
    racines_inclues = {d["racine"] for d in dossiers}
    for d in dossiers:
        if d["statut_audit"] == "inclus" and d["branche"].startswith("runs/collisionneurs-partiels"):
            compl = "docs/notes/collisionneurs-reprise-2026-11-24-v1/" + d["racine"]
            if compl in racines_inclues:
                d["statut_audit"] = "doublon-partiel"
                d["raison_exclusion"] = f"copie partielle (passation de 06:20Z) de {compl}"
    # copies « -suite » / « -run » d'une même course sur deux branches de données
    par_nom = {}
    for d in dossiers:
        if d["statut_audit"] == "inclus" and d.get("type") == "course":
            cle = re.sub(r"-v1-suite/", "-v1/", d["racine"])
            par_nom.setdefault(cle, []).append(d)
    for cle, L in par_nom.items():
        if len(L) > 1:
            L.sort(key=lambda x: -x.get("n_cellules", 0))
            for x in L[1:]:
                x["statut_audit"] = "doublon-partiel"
                x["raison_exclusion"] = f"copie moins complète de {L[0]['racine']} (branche {L[0]['branche']})"
    dossiers.extend(premiere_etape())
    SORTIES.mkdir(exist_ok=True)
    (SORTIES / "inventaire-v2.json").write_text(json.dumps(dossiers, ensure_ascii=False, indent=1))
    champs = ["racine", "type", "branche", "commit", "statut_audit", "raison_exclusion", "question_titre", "reformulateur_en_tete",
              "especes", "fournisseurs", "n_modeles", "tours", "n_cellules", "appels_journal", "n_pannes",
              "compte_usd", "pire_usd", "debut", "fin", "rejeu_de", "bras_temoin"]
    with open(SORTIES / "inventaire-v2.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=champs, extrasaction="ignore")
        w.writeheader()
        for d in dossiers:
            w.writerow({k: (json.dumps(d.get(k), ensure_ascii=False) if isinstance(d.get(k), (list, dict)) else d.get(k)) for k in champs})
    print(Counter(d["statut_audit"] for d in dossiers))
    print("branches de données exclues par leur nom :", BRANCHES_DONNEES_EXCLUES)
    return 0


if __name__ == "__main__":
    sys.exit(main())
