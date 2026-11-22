"""Import unique : le registre des idées écrit sous le mandat v1 entre au journal comme première capture.

Lit `registre-des-idees-v1.md` au commit 54069b6a (où il est scellé), prend pour extrait la cellule « idée »
de chaque ligne (mot pour mot, coupée sous 300 signes), et lui attache l'état, l'issue et les dates
assignés ci-dessous par la veille (relus des lignes v1 ; aucun résultat recopié). Ajoute sept gisements,
avec pour extrait leur ligne de titre au commit où ils sont. Écrit sur la sortie standard, en JSON Lines.
"""
import json
import subprocess
import sys

COMMIT_V1 = "54069b6a"
CHEMIN_V1 = "docs/notes/veille-de-cap-v1/registre-des-idees-v1.md"
QUAND = "2026-11-22T15:13:36Z"

# ligne v1 : (type, état, issue de l'essai ou None, sert, porteur, origine, dernière trace, réveil ou None)
M = "mot du directeur"
D = "synthèse ou décision"
V = "veille de cap"
A = {
    "A1": ("I", "en préparation", "jamais parti", "porte G0, critère 4", M, "2026-10-04", "2026-11-14", "2026-11-26"),
    "A2": ("P", "en préparation", None, "porte G0, critère 6", M, "2026-10-04", "2026-11-19", "2026-11-24"),
    "A3": ("P", "en préparation", None, "porte G0, critère 7", M, "2026-10-04", "2026-11-19", "2026-11-24"),
    "A4": ("P", "en préparation", None, "porte G0, grille de lecture", D, "2026-10-31", "2026-11-19", "2026-11-24"),
    "A5": ("I", "proposée", None, "porte G0, critère 2", M, "2026-10-04", "2026-11-14", "2026-11-26"),
    "A6": ("P", "retenue", None, "porte G0, critère 8", M, "2026-10-04", "2026-11-14", None),
    "A7": ("P", "proposée", None, "porte G0", D, "2026-11-19", "2026-11-19", None),
    "A8": ("P", "proposée", None, "porte G0", D, "2026-11-19", "2026-11-19", None),
    "B1": ("I", "en préparation", "jamais parti", "organisme, atelier d'idées", M, "2026-11-03", "2026-11-22", "2026-11-24"),
    "B2": ("I", "essai non évaluable", "non évaluable", "organisme, atelier d'idées", M, "2026-11-13", "2026-11-14", "2026-11-26"),
    "B3": ("I", "en préparation", "jamais parti", "organisme", M, "2026-11-13", "2026-11-18", "2026-11-26"),
    "B4": ("I", "en préparation", "jamais parti", "organisme", M, "2026-11-15", "2026-11-18", "2026-11-26"),
    "B5": ("I", "essai non évaluable", "non évaluable", "sondes, billet", D, "2026-11-04", "2026-11-21", "2026-11-24"),
    "B6": ("P", "proposée", None, "accords de calcul", V, "2026-11-22", "2026-11-22", "2026-11-26"),
    "C2": ("I", "essai non évaluable", "non évaluable", "organisme, juge", D, "2026-11-15", "2026-11-18", "2026-11-22"),
    "C3": ("I", "essai non évaluable", "non évaluable", "H8, conscience d'évaluation", D, "2026-10-25", "2026-10-26", None),
    "C4": ("I", "en préparation", "jamais parti", "G1, mode tenu à l'écart", M, "2026-10-28", "2026-10-28", None),
    "C5": ("I", "essai non évaluable", "non évaluable", "instrument, contrôle positif", M, "2026-10-20", "2026-11-09", None),
    "C6": ("I", "essai non évaluable", "non évaluable", "organisme, bisociation", D, "2026-10-31", "2026-11-01", None),
    "C7": ("I", "essai non évaluable", "non évaluable", "étiqueteur du sabotage flou", D, "2026-11-07", "2026-11-11", None),
    "C8": ("I", "essai non évaluable", "non évaluable", "papier C, coercition du moniteur", M, "2026-10-15", "2026-11-14", None),
    "C9": ("I", "en préparation", "jamais parti", "bascule « 8 milliards trop faible »", D, "2026-10-19", "2026-10-20", None),
    "C10": ("I", "essai non évaluable", "non évaluable", "instrument, appels à Fable", M, "2026-11-22", "2026-11-22", None),
    "C11": ("I", "en préparation", "jamais parti", "organisme, nouvelles attaques", M, "2026-11-20", "2026-11-22", "2026-11-27"),
    "C12": ("I", "testée, non concluant", "non concluant", "H8, conscience d'évaluation", M, "2026-10-27", "2026-10-28", "2026-12-02"),
    "C13": ("I", "essai non évaluable", "non évaluable", "audit défensif", D, "2026-10-26", "2026-10-29", None),
    "C14": ("I", "testée, non concluant", "non concluant", "organisme, ligne 1", D, "2026-11-19", "2026-11-20", None),
    "C15": ("I", "essai non évaluable", "non évaluable", "organismes discrets", D, "2026-11-18", "2026-11-18", None),
    "C16": ("I", "testée, non concluant", "non concluant", "organismes discrets, juge", D, "2026-11-18", "2026-11-18", None),
    "C17": ("I", "essai non évaluable", "non évaluable", "organisme, composition des proposeurs", D, "2026-10-28", "2026-11-01", None),
    "C18": ("P", "retenue", None, "conception par Fable", M, "2026-11-22", "2026-11-22", None),
    "C19": ("I", "essai non évaluable", "non évaluable", "collisionneur, bancs plantés", M, "2026-11-22", "2026-11-22", None),
    "C20": ("I", "essai non évaluable", "non évaluable", "« Raisons ou regard ? »", D, "2026-11-21", "2026-11-22", None),
    "C21": ("P", "proposée", None, "conception, demande 22", V, "2026-11-22", "2026-11-22", None),
    "C22": ("I", "proposée", None, "procédure", V, "2026-11-22", "2026-11-22", None),
    "D1": ("I", "proposée", None, "HC2, papier C", D, "2026-11-12", "2026-11-21", "2026-11-24"),
    "D2": ("P", "en préparation", None, "porte de fin de phase 1", D, "2026-11-21", "2026-11-21", None),
    "D3": ("I", "retenue", None, "G1, papier C", D, "2026-10-26", "2026-10-26", None),
    "D4": ("I", "retenue", None, "organismes", D, "2026-10-26", "2026-11-17", None),
    "D5": ("I", "retenue", None, "H1, bases, G1", D, "2026-10-26", "2026-10-29", None),
    "D6": ("I", "retenue", None, "phase 1", D, "2026-10-26", "2026-11-08", None),
    "D7": ("I", "retenue", None, "G1, bras revers", D, "2026-10-22", "2026-10-22", None),
    "D8": ("I", "retenue", None, "organisme", D, "2026-10-26", "2026-10-28", None),
    "D9": ("I", "proposée", None, "organisme", D, "2026-10-24", "2026-11-10", None),
    "D10": ("I", "retenue", None, "organisme, objectif ultime", D, "2026-10-24", "2026-11-10", None),
    "D11": ("I", "retenue", None, "organisme", D, "2026-10-25", "2026-10-25", None),
    "D12": ("I", "retenue", None, "organisme", D, "2026-10-25", "2026-11-13", None),
    "D13": ("I", "retenue", None, "organisme", M, "2026-10-26", "2026-11-11", None),
    "D14": ("I", "proposée", None, "programme, section 9", D, "2026-10-22", "2026-10-22", None),
    "D15": ("I", "proposée", None, "G1, comparateurs", D, "2026-10-30", "2026-10-31", None),
    "D16": ("I", "retenue", None, "sondes, bases boîte noire", D, "2026-11-09", "2026-11-10", None),
    "D17": ("I", "retenue", None, "idées des mentors", M, "2026-11-08", "2026-11-08", None),
    "D18": ("I", "en préparation", None, "idées des mentors", D, "2026-11-04", "2026-11-04", None),
    "D19": ("I", "retenue", None, "juges", M, "2026-11-01", "2026-11-10", None),
    "D20": ("I", "retenue", None, "juges", D, "2026-11-04", "2026-11-04", None),
    "D21": ("I", "retenue", None, "sondes", D, "2026-11-04", "2026-11-21", None),
    "D22": ("I", "proposée", None, "sondes", M, "2026-11-08", "2026-11-08", None),
    "D23": ("I", "proposée", None, "organisme", D, "2026-11-09", "2026-11-09", None),
    "D24": ("I", "proposée", None, "conception", D, "2026-11-18", "2026-11-18", None),
    "D25": ("I", "retenue", None, "H2, accumulation", M, "2026-11-18", "2026-11-18", None),
    "D26": ("I", "retenue", None, "organisme", M, "2026-11-13", "2026-11-13", None),
    "E1": ("I", "proposée", None, "organisme, allumage ; papier C, second terrain", M, "2026-10-30", "2026-10-31", "2026-12-02"),
    "E2": ("I", "retenue", None, "organisme, allumage", D, "2026-10-31", "2026-10-31", "2026-12-02"),
    "E3": ("P", "proposée", None, "organisme, allumage", D, "2026-10-31", "2026-10-31", "2026-12-02"),
    "E4": ("I", "retenue", None, "organisme, bisociation", D, "2026-10-31", "2026-10-31", None),
    "E5": ("I", "proposée", None, "organisme, allumage", D, "2026-10-30", "2026-10-31", None),
    "E6": ("I", "proposée", None, "organisme, exploration", D, "2026-11-13", "2026-11-22", None),
    "E7": ("I", "retenue", None, "organisme, exploration", D, "2026-11-13", "2026-11-13", None),
    "E8": ("I", "retenue", None, "organisme", M, "2026-10-26", "2026-10-27", None),
    "E10": ("P", "retenue", None, "organisme", M, "2026-11-01", "2026-11-18", None),
    "F1": ("I", "proposée", None, "papier B", M, "2026-10-04", "2026-10-28", "2026-12-02"),
    "F2": ("I", "proposée", None, "H7, papier B", M, "2026-10-04", "2026-10-28", "2026-12-02"),
    "F3": ("I", "proposée", None, "G1, lemme", M, "2026-10-04", "2026-11-14", "2026-12-02"),
    "F4": ("I", "proposée", None, "papier B", M, "2026-10-04", "2026-10-28", "2026-12-02"),
    "F5": ("I", "proposée", None, "papier B", M, "2026-10-04", "2026-10-28", "2026-12-02"),
    "F6": ("P", "retenue", None, "veille active du programme", M, "2026-10-04", "2026-11-13", None),
    "F7": ("P", "retenue", None, "état de l'art", D, "2026-10-07", "2026-10-07", None),
    "F8": ("P", "en préparation", None, "papier B", M, "2026-10-04", "2026-10-07", None),
    "F9": ("P", "en préparation", None, "lemme, analyse séquentielle", M, "2026-11-21", "2026-11-21", None),
    "G1": ("P", "proposée", None, "programme, bascules", V, "2026-10-20", "2026-10-22", None),
    "G2": ("P", "retenue", None, "revendications, entretien", M, "2026-11-22", "2026-11-22", "2026-11-28"),
    "G3": ("P", "proposée", None, "procédure", M, "2026-11-21", "2026-11-22", None),
    "G4": ("P", "retenue", None, "entretien", D, "2026-11-22", "2026-11-22", None),
    "G5": ("P", "proposée", None, "proposition de recherche", D, "2026-11-08", "2026-11-22", None),
    "G6": ("P", "retenue", None, "billet", M, "2026-11-22", "2026-11-22", "2026-12-02"),
}
GISEMENTS = [
    ("docs/notes/collisionneur-bassins-etroits-v1/synthese-v1.md", "3686b636", "bassins étroits : synthèse du collisionneur", "synthèse oui ; idées retenues fichées en partie (B2, E7)", "2026-11-13"),
    ("docs/notes/quatre-lectures-inventaire-v1/mentors-releve-d-ensemble-v1.md", "3686b636", "93 idées des mentors du 3 novembre", "relevé oui ; idées non fichées une à une (B1)", "2026-11-18"),
    ("docs/notes/bisociation-litterature-reelle-v1/collisionneur-question-7-v1/faits-question-7-v1.md", "3686b636", "fertilité et allumage : questions 3 et 7", "synthèse oui ; idées fichées en partie (E1 à E5)", "2026-10-31"),
    ("docs/notes/protocelles-collisionneur-v1/synthese-protocelles-tour2-v1.md", "3686b636", "protocelles, deux tours", "synthèse oui ; une idée fichée (E2)", "2026-10-31"),
    ("docs/notes/memoire-conception-v1/liste-exhaustive-hypotheses-exploration-allumage-v1.md", "8b62e4e2", "96 hypothèses d'exploration et d'allumage (bibliothécaire)", "liste oui ; non triée, non fichée", "2026-11-22"),
    ("docs/notes/brainstorm-rapport-openai-surveillance-v1.md", "3686b636", "remue-méninges sur le rapport d'OpenAI", "synthèse oui ; une fiche (D14)", "2026-10-22"),
    ("docs/notes/rapports-directeur/programme-organisme-complet-v1/inventaire-idees-organisme-v7.md", "3686b636", "inventaire des idées de l'organisme (v7)", "inventaire oui ; usage non tracé (ex-ligne E9)", "2026-11-10"),
]


def show(commit, chemin):
    return subprocess.run(["git", "show", f"{commit}:{chemin}"], capture_output=True, check=True).stdout.decode("utf-8")


def couper(t, n=300):
    t = t.strip()
    if len(t) <= n:
        return t
    t = t[:n]
    return t[: t.rfind(" ")] if " " in t else t


def mots(nom):
    vus = []
    for m in nom.replace("*", " ").replace("«", " ").replace("»", " ").replace(",", " ").replace("(", " ").replace(")", " ").split():
        m = m.strip(".:;'’").lower()
        if len(m) > 5 and m not in vus:
            vus.append(m)
    return vus[:5] or [nom[:20]]


def main():
    texte = show(COMMIT_V1, CHEMIN_V1)
    lignes = {}
    for l in texte.split("\n"):
        if l.startswith("| ") and l.split("|")[1].strip() in A or (l.startswith("| C1 |")):
            cells = [c for c in l.split("|")]
            lignes[cells[1].strip()] = cells[2].strip()
    out = []
    n_i = n_p = 0
    ids = {}
    for rid in list(A) + ["C1"]:
        if rid not in lignes:
            sys.exit(f"ligne v1 {rid} introuvable")
    for rid, v in A.items():
        t, etat, issue, sert, porteur, origine, trace, reveil = v
        if t == "I":
            n_i += 1; fid = f"I-{n_i:04d}"
        else:
            n_p += 1; fid = f"P-{n_p:04d}"
        ids[rid] = fid
        nom_cell = lignes[rid]
        ext = couper(nom_cell)
        nom = nom_cell.replace("**", "")
        e = {"quand": QUAND, "fiche": fid, "evenement": "naissance", "nom": couper(nom, 200), "etat": etat,
             "source": {"chemin": CHEMIN_V1, "commit": COMMIT_V1, "repere": f"registre v1, ligne {rid}", "extrait": ext},
             "porteur": porteur, "sert": sert, "issue": None, "raison": None, "reveil": reveil, "mots": mots(nom),
             "origine": origine, "derniere_trace": trace}
        out.append(e)
        if issue:
            e2 = dict(e, evenement="essai", issue=issue)
            out.append(e2)
    # C1 = doublon de B2 sous le mandat v1
    n_i += 1
    out.append({"quand": QUAND, "fiche": f"I-{n_i:04d}", "evenement": "fusion", "nom": "Bassins étroits (doublon v1 de B2)",
                "etat": "fusionnée dans", "dans": ids["B2"],
                "source": {"chemin": CHEMIN_V1, "commit": COMMIT_V1, "repere": "registre v1, ligne C1", "extrait": couper(lignes["C1"])},
                "porteur": V, "sert": "organisme, atelier d'idées", "issue": None, "raison": None, "reveil": None,
                "mots": ["bassins", "étroits"], "origine": "2026-11-13", "derniere_trace": "2026-11-14"})
    for k, (chemin, commit, nom, dep, trace) in enumerate(GISEMENTS, 1):
        titre = show(commit, chemin).split("\n", 1)[0].lstrip("# ").strip()
        out.append({"quand": QUAND, "fiche": f"G-{k:04d}", "evenement": "naissance", "nom": nom, "etat": "retenue",
                    "source": {"chemin": chemin, "commit": commit, "repere": "titre", "extrait": couper(titre)},
                    "porteur": D, "sert": "gisement", "issue": None, "raison": None, "reveil": None,
                    "mots": mots(nom), "depouille": dep, "origine": trace, "derniere_trace": trace})
    for e in out:
        print(json.dumps(e, ensure_ascii=False))


if __name__ == "__main__":
    main()
