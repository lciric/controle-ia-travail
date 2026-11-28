"""Essais de la lecture RS1 (contre-lecture R2, angle « lecture et invite face au texte ») sur des valeurs écrites à la
main. Lecture seule sur le clone : importé par PYTHONPATH, sans fichier compilé (python -B)."""
from controle_ia.environnements import rubrique_simplifiee as rs
from controle_ia.environnements.rubrique import lire_une_note

BLOC = "SPECIFICITY: 3\nCOVERAGE: 4\nRIGOR: 2\nFEASIBILITY: 3\nJUSTIFICATION: ok.\n"

def lire_val(v):
    r = rs.lire_reponse_rs1(BLOC.replace("SPECIFICITY: 3", "SPECIFICITY: " + v, 1), False)
    return r["notes"].get("SPECIFICITY"), r["complete"], [a for a in r["anomalies"] if a.startswith("SPEC")]

cas = {
    # séparateurs habillés de Markdown (le nettoyage n'enlève que les bords)
    "md or": "3 **or** 4", "md to": "3 *to* 4", "md and": "3 _and_ 4",
    # tirets non listés
    "double tiret": "3 -- 4", "tiret figure": "3 ‒ 4", "trait d'union U+2010": "3 ‐ 4", "barre": "3 ― 4",
    "tilde": "3 ~ 4", "fleche": "3 → 4", "barre oblique espacée": "3 / 4",
    # seconds nombres sans séparateur listé
    "virgule puis or": "3, or 4", "and/or": "3 and/or 4", "crochets": "3 [4]", "maybe": "3 (maybe 4)",
    "but": "3 but 4", "vs": "3 vs 4", "slash 5 puis": "3/5 4/5", "or tout attaché": "3or4",
    # signe après le séparateur (le texte dit « un chiffre »)
    "to signé": "3 to -4", "virgule signée": "3, -1", "tiret plus": "3 - +4", "moins unicode": "3 to −4",
    # même valeur répétée par un second nombre
    "même valeur parenthèse": "3 (3/5)", "pourcentage": "4/5 (80%)",
    # cas sains attendus
    "out of": "3 (out of 5)", "point final": "3.", "fraction point": "3/5.", "gras": "**3**",
    "gras puis prose": "**3** (competent)", "espace insécable": "3 - 4",
    # chiffres non ASCII
    "chiffre pleine chasse": "４", "chiffre arabe": "٤",
}
for nom, v in cas.items():
    print(f"{nom:28s} {v!r:22s} suite={rs.controle_suite(v)!s:14s} gelee={lire_une_note(v.strip().strip('*_ ').strip(), 0, 5)!r:40s} lu={lire_val(v)}")

# lignes : retours chariot, listes numérotées, nom entouré
for rep in ["SPECIFICITY: 3\r\nCOVERAGE: 4\r\nRIGOR: 2\r\nFEASIBILITY: 3\r\n",
            "1. SPECIFICITY: 3\n2. COVERAGE: 4\n3. RIGOR: 2\n4. FEASIBILITY: 3\n",
            "SPECIFICITY (0-5): 3\nCOVERAGE: 4\nRIGOR: 2\nFEASIBILITY: 3\n",
            "SPECIFICITY: 3 COVERAGE: 4\nRIGOR: 2\nFEASIBILITY: 3\n",
            "Specificity score: 3\nCOVERAGE: 4\nRIGOR: 2\nFEASIBILITY: 3\n"]:
    r = rs.lire_reponse_rs1(rep, False)
    print(repr(rep[:40]), r["complete"], r["notes"], r["anomalies"])
