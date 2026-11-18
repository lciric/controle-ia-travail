#!/usr/bin/env python3
"""Fusionne les 21 lots en releve-mecanismes-v1.json en appliquant programmes/corrections-v1.json.
N'écrase aucun lot. Arrêt (code 1) si un « avant » de la table ne correspond pas, si un indice manque
ou se répète, si une famille sort de la liste fermée, si un « autre » n'est pas justifié, si une entrée sans
mécanisme n'a pas de statut. Garde testée au début sur un cas sain et sur un artefact (R5).
Usage (depuis docs/notes/matiere-premiere-auto-conception-v1) :
  python programmes/fusionner_v1.py > programmes/fusionner_v1.sortie.txt"""
import collections, copy, glob, hashlib, json, sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
ICI = Path(".")
FAMILLES = ["exploration", "originalité", "épreuve", "jugement", "mémoire", "sélection", "coût", "auto-conception", "autre"]
PROFONDEURS = ["lecture approfondie sur PDF", "page ou résumé", "notice seule"]
EPROUVES = ["oui, mesuré", "oui, affirmé", "non", "inconnu"]
LEGENDE = {
    "oui, mesuré": "les auteurs disent avoir mesuré ; mesure non vérifiée par le programme ni par nous (R7) : jamais un fait établi",
    "oui, affirmé": "les auteurs affirment un effet sans mesure propre à ce mécanisme, ou le résultat est lu sur une notice ; non opposable",
    "non": "aucune épreuve contre le réel : proposition, argument de position ou simulation seule",
    "inconnu": "la notice ne dit pas si le mécanisme a été éprouvé contre le réel",
    "profondeur de lecture": "« lecture approfondie sur PDF » : une fiche de lecture du dépôt a été relue ; « page ou résumé » : résumé, page ou fiche d'OpenReview lus par la veille ; « notice seule » : titre et courte description de la table seuls ; toute entrée sur page, résumé ou notice est non opposable (R7)",
    "suggéré par le titre": "mécanisme inféré du seul titre ou d'après le titre : compté à part, jamais additionné aux mécanismes décrits",
    "absence": "toute absence dans ce moissonnage est une question, pas un trou du champ (R8)",
}

def appliquer(travaux, corrections):
    """travaux : dict indice -> entrée (copie profonde). Applique les corrections ; lève ValueError si un « avant » diffère."""
    retraits = []
    ajouts = collections.defaultdict(list)
    a_retirer = collections.defaultdict(set)
    for c in corrections:
        e = travaux[c["indice"]]
        cible = e if c["mecanisme"] is None else e["mecanismes"][c["mecanisme"]]
        op, champ = c["operation"], c["champ"]
        if op == "modifier":
            if cible.get(champ) != c["avant"]:
                raise ValueError(f"avant différent : indice {c['indice']} mécanisme {c['mecanisme']} champ {champ}")
            cible[champ] = c["apres"]
        elif op == "ajouter_champ":
            if champ in cible:
                raise ValueError(f"champ déjà présent : indice {c['indice']} mécanisme {c['mecanisme']} champ {champ}")
            cible[champ] = c["apres"]
        elif op == "retirer_mecanisme":
            if cible["mecanisme_en_une_phrase"] != c["avant"]:
                raise ValueError(f"avant différent (retrait) : indice {c['indice']}")
            a_retirer[c["indice"]].add(c["mecanisme"])
            retraits.append(dict(indice=c["indice"], correction=c["correction"], raison=c["raison"],
                                 note="ligne retirée du relevé ; son contenu n'est pas reproduit ici" if c["correction"] in (4, 6) and c["indice"] in (57, 259) else ""))
        elif op == "ajouter_mecanisme":
            ajouts[c["indice"]].append(c["apres"])
        else:
            raise ValueError("opération inconnue " + op)
    for i, pos in a_retirer.items():
        travaux[i]["mecanismes"] = [m for k, m in enumerate(travaux[i]["mecanismes"]) if k not in pos]
    for i, ms in ajouts.items():
        travaux[i]["mecanismes"] += ms
    return retraits

def autotest(travaux, corrections):
    # cas sain : la table s'applique sans erreur sur une copie
    appliquer(copy.deepcopy(travaux), corrections)
    # artefact : un « avant » falsifié doit arrêter
    faux = copy.deepcopy(corrections)
    k = next(j for j, c in enumerate(faux) if c["operation"] == "modifier")
    faux[k]["avant"] = "VALEUR FAUSSE"
    try:
        appliquer(copy.deepcopy(travaux), faux)
    except ValueError:
        return "garde « avant » : cas sain accepté, artefact refusé"
    raise SystemExit("ARRÊT : la garde n'a pas refusé l'artefact")

def main():
    lots = []
    for f in sorted(glob.glob("lots/lot-*.json")):
        attendu = Path(f + ".sha256").read_text().split()[0]
        reel = hashlib.sha256(Path(f).read_bytes()).hexdigest()
        if attendu != reel:
            raise SystemExit(f"ARRÊT : empreinte non conforme pour {f}")
        lots.append(json.loads(Path(f).read_text(encoding="utf-8")))
    print(f"{len(lots)} lots lus, empreintes conformes")
    travaux = {}
    for lot in lots:
        for e in lot:
            if e["indice"] in travaux:
                raise SystemExit(f"ARRÊT : indice en double {e['indice']}")
            travaux[e["indice"]] = e
    table = json.loads((RACINE / "docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json").read_text(encoding="utf-8"))["travaux"]
    if sorted(travaux) != list(range(len(table))) or len(table) != 630:
        raise SystemExit("ARRÊT : indices avec trou, doublon ou nombre différent de 630")
    for i, e in travaux.items():
        if e["titre"] != table[i]["titre"] or e["adresse"] != table[i]["adresse"]:
            raise SystemExit(f"ARRÊT : titre ou adresse non alignés sur la table, indice {i}")
    print("630 travaux, indices 0 à 629 sans trou ni doublon, titres et adresses alignés sur la table")
    corr = json.loads((ICI / "programmes/corrections-v1.json").read_text(encoding="utf-8"))
    print(autotest(travaux, corr["corrections"]))
    retraits = appliquer(travaux, corr["corrections"])
    print(f"{len(corr['corrections'])} lignes de corrections appliquées ; retraits : {len(retraits)}")
    norm = corr["regles_globales"]["normalisation_des_familles"]
    nb_norm = 0
    for i in sorted(travaux):
        e = travaux[i]
        for k, m in enumerate(e["mecanismes"]):
            nouvelle = norm.get(m["famille"], m["famille"])
            if nouvelle not in FAMILLES:
                raise SystemExit(f"ARRÊT : famille hors liste, indice {i} : {m['famille']}")
            if nouvelle != m["famille"]:
                nb_norm += 1
            m["famille"] = nouvelle
            m.setdefault("suggere_par_le_titre", False)
            if m["eprouve_contre_le_reel"] not in EPROUVES:
                raise SystemExit(f"ARRÊT : éprouvé hors liste, indice {i}")
            if m["famille"] == "autre" and "justification_autre" not in m:
                raise SystemExit(f"ARRÊT : « autre » non justifié, indice {i}")
            m["id"] = f"{i}.{k}"
        if not e["mecanismes"] and "statut" not in e:
            raise SystemExit(f"ARRÊT : entrée sans mécanisme et sans statut, indice {i}")
        if e["profondeur_de_lecture"] not in PROFONDEURS:
            raise SystemExit(f"ARRÊT : profondeur hors liste, indice {i}")
    print(f"écritures de familles normalisées : {nb_norm}")
    ms = [(i, m) for i in sorted(travaux) for m in travaux[i]["mecanismes"]]
    decr = [(i, m) for i, m in ms if not m["suggere_par_le_titre"]]
    sugg = [(i, m) for i, m in ms if m["suggere_par_le_titre"]]
    def cpt(liste, f):
        return dict(collections.Counter(f(i, m) for i, m in liste).most_common())
    ordre = lambda d, cles: {k: d.get(k, 0) for k in cles}
    comptes = {
        "travaux": len(travaux),
        "travaux_avec_au_moins_un_mecanisme": sum(1 for e in travaux.values() if e["mecanismes"]),
        "travaux_par_statut_sans_mecanisme": dict(collections.Counter(e.get("statut", "sans statut") for e in travaux.values() if not e["mecanismes"])),
        "travaux_par_profondeur": ordre(dict(collections.Counter(e["profondeur_de_lecture"] for e in travaux.values())), PROFONDEURS),
        "mecanismes_total": len(ms),
        "mecanismes_decrits": len(decr),
        "mecanismes_suggeres_par_le_titre": len(sugg),
        "decrits_par_famille": ordre(cpt(decr, lambda i, m: m["famille"]), FAMILLES),
        "suggeres_par_famille": ordre(cpt(sugg, lambda i, m: m["famille"]), FAMILLES),
        "decrits_par_eprouve": ordre(cpt(decr, lambda i, m: m["eprouve_contre_le_reel"]), EPROUVES),
        "suggeres_par_eprouve": ordre(cpt(sugg, lambda i, m: m["eprouve_contre_le_reel"]), EPROUVES),
        "decrits_par_profondeur_du_travail": ordre(cpt(decr, lambda i, m: travaux[i]["profondeur_de_lecture"]), PROFONDEURS),
        "autre_restants_justifies": sum(1 for i, m in ms if m["famille"] == "autre"),
    }
    print(json.dumps(comptes, ensure_ascii=False, indent=1))
    sortie = dict(version="v1", legende=LEGENDE, comptes=comptes, retraits=retraits,
                  note="Relevé fusionné des 21 lots après application de programmes/corrections-v1.json ; chaque mécanisme porte un identifiant « indice.position ».",
                  travaux=[travaux[i] for i in sorted(travaux)])
    Path("releve-mecanismes-v1.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("écrit : releve-mecanismes-v1.json")

if __name__ == "__main__":
    main()
