"""Journal des idées de la veille de cap : vérification des invariants et vue en clair (v1).

Pièce d'instrument (classe B) : à contre-lire par un autre modèle avant tout usage décisif.
Usage, depuis la racine du dépôt :
    python3 docs/notes/veille-de-cap-v1/outils/veille_journal_v1.py verifier JOURNAL [--avant REF]
    python3 docs/notes/veille-de-cap-v1/outils/veille_journal_v1.py vue JOURNAL AAAA-MM-JJ > VUE.md
`verifier` sort en code 1 au premier défaut (il les liste tous, puis sort) ; code 0 si aucun.
Invariants du mandat v2, § 3 : 1 (extrait retrouvé mot pour mot à chemin@commit), 2 (côté et abandon
citent une décision ; côté porte un réveil ; abandon porte une raison de la liste), 3 (verdict valide cite
une ligne R- et une portée), 4 (tout essai porte une des quatre issues), 5 (aucune ligne perdue ni changée
depuis REF), 6 (aucun chemin interdit cité), 7 (souffrance calculée dans la vue).
"""
import json
import re
import subprocess
import sys
from datetime import date

ETATS = [
    "proposée", "retenue", "en préparation", "à l'essai", "essai non évaluable",
    "testée, non concluant", "testée, verdict valide", "intégrée au programme",
    "gardée de côté", "abandonnée", "fusionnée dans",
]
EVENEMENTS = ["naissance", "état", "essai", "signal", "décision", "fusion", "note",
              "retour programmé", "retour rendu", "retour clos"]
ISSUES = ["jamais parti", "non évaluable", "non concluant", "verdict valide"]
RAISONS = ["réfutée", "occupée", "trop chère", "remplacée", "hors cap", "risque", "mot du directeur"]
MOUVEMENTS = ["naissance", "état", "essai", "décision", "fusion"]  # un signal, une note ou un retour de la veille ne compte pas
CHAMPS = ["quand", "fiche", "evenement", "nom", "etat", "source", "porteur", "sert", "mots"]
INTERDITS = re.compile(
    r"consigne-privee|conception-ii-b|brouillons/ii-b-saboteur-budget-v1|lot/compte-4-v1|"
    r"modes-attaque-reponse-24-fable|prep/quarantaine-|archives-reponses-modeles|"
    r"v[ée]rit[ée]|rendu|scores|bras-attaque-oracle|cle-de-l-epreuve",
    re.IGNORECASE,
)
DECISION = re.compile(r"\b(R-\d+|GO-\d{4}-\d\d-\d\d-\d+|N-\d+)\b")


def lire(chemin):
    lignes = []
    with open(chemin, encoding="utf-8") as f:
        for n, brut in enumerate(f, 1):
            if brut.strip():
                lignes.append((n, brut.rstrip("\n"), json.loads(brut)))
    return lignes


def _git_show(commit, chemin, cache):
    cle = (commit, chemin)
    if cle not in cache:
        r = subprocess.run(["git", "show", f"{commit}:{chemin}"], capture_output=True)
        cache[cle] = r.stdout.decode("utf-8", errors="replace") if r.returncode == 0 else None
    return cache[cle]


def verifier(chemin_journal, avant=None):
    defauts = []
    cache = {}
    lignes = lire(chemin_journal)
    for n, _brut, e in lignes:
        ou = f"ligne {n} ({e.get('fiche', '?')})"
        for c in CHAMPS:
            if c not in e:
                defauts.append(f"{ou} : champ absent « {c} »")
        if e.get("evenement") not in EVENEMENTS:
            defauts.append(f"{ou} : événement hors liste « {e.get('evenement')} »")
        if e.get("etat") not in ETATS:
            defauts.append(f"{ou} : état hors liste « {e.get('etat')} »")
        src = e.get("source") or {}
        ext = src.get("extrait", "")
        if not ext or len(ext) > 300:
            defauts.append(f"{ou} : extrait vide ou de plus de 300 signes")
        texte = _git_show(src.get("commit", ""), src.get("chemin", ""), cache)
        if texte is None:
            defauts.append(f"{ou} : source introuvable {src.get('chemin')}@{src.get('commit')}")
        elif ext and ext not in texte:
            defauts.append(f"{ou} : extrait non retrouvé mot pour mot à {src.get('chemin')}@{src.get('commit')}")
        chemins_cites = [src.get("chemin", "")] + re.findall(r"`([^`]*/[^`]*)`", ext)
        if any(INTERDITS.search(c) for c in chemins_cites):
            defauts.append(f"{ou} : chemin ou extrait interdit cité")
        etat = e.get("etat")
        if etat in ("gardée de côté", "abandonnée") and not DECISION.search(str(e.get("decision", ""))):
            defauts.append(f"{ou} : « {etat} » sans décision nommée (R-, GO-, N-)")
        if etat == "gardée de côté" and not e.get("reveil"):
            defauts.append(f"{ou} : « gardée de côté » sans réveil")
        if etat == "abandonnée" and e.get("raison") not in RAISONS:
            defauts.append(f"{ou} : « abandonnée » sans raison de la liste")
        if etat == "testée, verdict valide":
            if not re.search(r"\bR-\d+\b", str(e.get("decision", ""))) or not e.get("portee"):
                defauts.append(f"{ou} : verdict valide sans ligne R- ou sans portée")
        if e.get("evenement") == "essai" and e.get("issue") not in ISSUES:
            defauts.append(f"{ou} : essai sans issue de la liste")
        if e.get("evenement") == "retour programmé":
            r = e.get("retour") or {}
            if not (r.get("date") or r.get("butoir")):
                defauts.append(f"{ou} : retour sans date ni butoir (additif 1, règle 1)")
            if not r.get("pour_qui") or not r.get("lettre") or len(r.get("lettre", "")) > 600:
                defauts.append(f"{ou} : retour sans destinataire ou sans lettre de 600 signes au plus")
        if e.get("evenement") == "retour clos" and (e.get("retour") or {}).get("fin") not in ("fait", "reprogrammé", "retiré par décision nommée"):
            defauts.append(f"{ou} : retour clos sans l'une des trois fins")
        if etat == "fusionnée dans" and not e.get("dans"):
            defauts.append(f"{ou} : « fusionnée dans » sans fiche cible")
    if avant:
        r = subprocess.run(["git", "show", f"{avant}:{chemin_journal}"], capture_output=True)
        if r.returncode == 0:
            anciennes = [l for l in r.stdout.decode("utf-8").split("\n") if l.strip()]
            actuelles = [b for _n, b, _e in lignes]
            if actuelles[: len(anciennes)] != anciennes:
                defauts.append(f"journal : une ligne de {avant} est perdue ou changée (ajouts seuls)")
    return defauts


def etat_courant(lignes):
    fiches = {}
    for _n, _b, e in lignes:
        f = fiches.setdefault(e["fiche"], {"naissance": e, "dernier": e, "essais": [], "signaux": [], "trace": ""})
        if e["evenement"] in MOUVEMENTS:
            f["dernier"] = e
            f["trace"] = max(f["trace"], e.get("derniere_trace") or "")
        if e["evenement"] == "essai":
            f["essais"].append(e)
        if e["evenement"] == "signal":
            f["signaux"].append(e)
    return fiches


def _age(jour, aujourdhui):
    try:
        return (aujourdhui - date.fromisoformat(jour)).days
    except (TypeError, ValueError):
        return None


def vue(chemin_journal, aujourdhui):
    lignes = lire(chemin_journal)
    fiches = etat_courant(lignes)
    sortie = [
        f"# Registre des idées — vue du {aujourdhui.isoformat()}",
        "",
        f"Tirée par programme de `{chemin_journal}` ({len(lignes)} événements, {len(fiches)} fiches). "
        "Ne pas éditer : la vue se refait depuis le journal. « En souffrance » : aucune trace ni décision "
        "depuis quatorze jours (âge en jours depuis la dernière trace dans le programme).",
        "",
    ]
    groupes = [("G", "Gisements"), ("I", "Idées"), ("P", "Promesses")]
    souffrance = []
    for prefixe, titre in groupes:
        sel = sorted(k for k in fiches if k.startswith(prefixe + "-"))
        if not sel:
            continue
        sortie += [f"## {titre}", "", "| fiche | nom | état | issue du dernier essai | sert | dernière trace | âge | réveil | source |", "|---|---|---|---|---|---|---|---|---|"]
        for k in sel:
            d = fiches[k]["dernier"]
            ess = fiches[k]["essais"][-1]["issue"] if fiches[k]["essais"] else ""
            trace = fiches[k]["trace"]
            age = _age(trace, aujourdhui)
            marque = ""
            if age is not None and age > 14 and d["etat"] not in ("abandonnée", "fusionnée dans", "intégrée au programme", "testée, verdict valide"):
                marque = " (en souffrance)"
                souffrance.append((age, k))
            src = d["source"]
            nom = d["nom"].replace("|", "/")
            etat = d["etat"] + (f" {d['dans']}" if d.get("dans") else "")
            sortie.append(
                f"| {k} | {nom} | {etat} | {ess} | {d.get('sert', '')} | {trace} | "
                f"{'' if age is None else age}{marque} | {d.get('reveil', '') or ''} | {src.get('repere', '')} |"
            )
        sortie.append("")
    souffrance.sort(reverse=True)
    sortie += [
        "## Compte",
        "",
        f"- Fiches en souffrance : {len(souffrance)} ; la plus vieille : "
        + (f"{souffrance[0][1]} ({souffrance[0][0]} jours)." if souffrance else "aucune."),
        "",
    ]
    return "\n".join(sortie) + "\n"


def main(argv):
    if len(argv) >= 3 and argv[1] == "verifier":
        avant = argv[argv.index("--avant") + 1] if "--avant" in argv else None
        defauts = verifier(argv[2], avant)
        for d in defauts:
            print("DÉFAUT", d)
        print(f"{len(defauts)} défaut(s)")
        return 1 if defauts else 0
    if len(argv) == 4 and argv[1] == "vue":
        sys.stdout.write(vue(argv[2], date.fromisoformat(argv[3])))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
