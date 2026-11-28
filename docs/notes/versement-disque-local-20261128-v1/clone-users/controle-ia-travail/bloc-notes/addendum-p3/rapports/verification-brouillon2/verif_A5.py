"""A5 du brouillon 2 : valeur du champ COST selon la règle de bornes_champs (texte brut) et selon lire_action."""
import sys
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.environnements.propositions import lire_action, _nettoyer
from controle_ia.premier_test_ia import conditions as C

def valeur_brute(texte, cle="COST"):
    """Règle de bornes_champs appliquée au texte brut : première occurrence non vide (même test de vide que le code),
    valeur = texte de la fin de la clé à la clé suivante, après strip (lecture littérale de A5)."""
    cles = list(C._CLE_BRUTE.finditer(texte))
    vu = set()
    for i, m in enumerate(cles):
        k = m["cle"].upper()
        if k == "ACTION" or k in vu:
            continue
        derniere = i + 1 == len(cles)
        v = texte[m.end():len(texte) if derniere else cles[i + 1].start()]
        if m["gras"] and not m["gras_avant"] and derniere:
            v = C._FERMETURE_GRAS.sub("", v, count=1)
        if not v.strip():
            continue
        vu.add(k)
        if k == cle:
            return v.strip()
    return None

cas = {
  "simple": "ACTION: ADD\nTITLE: t\nPROPOSAL: p\nCOST: 40 hours\nPREDICTION: y",
  "gras ferme apres deux-points (non dernier)": "ACTION: ADD\nTITLE: t\nPROPOSAL: p\n**COST:** 40 hours\nPREDICTION: y",
  "gras ferme avant deux-points": "ACTION: ADD\nTITLE: t\nPROPOSAL: p\n**COST**: 40 hours\nPREDICTION: y",
  "gras ferme apres deux-points (dernier)": "ACTION: ADD\nTITLE: t\nPROPOSAL: p\nPREDICTION: y\n**COST:** 40 hours",
  "toutes cles en gras": "**ACTION:** ADD\n**TITLE:** t\n**PROPOSAL:** p\n**COST:** 40 hours\n**PREDICTION:** y",
  "Cost breakdown": "ACTION: ADD\nTITLE: t\nPROPOSAL: p\n**Cost** breakdown: 40 hours\nPREDICTION: y",
  "puce": "ACTION: ADD\nTITLE: t\nPROPOSAL: p\n- COST: 30\nPREDICTION: y",
}
for nom, t in cas.items():
    a = lire_action(t)
    vb = valeur_brute(t)
    vl = a.champs.get("COST")
    print(f"{nom:45s} brute={vb!r:22s} lire_action={vl!r:16s} diverge={vb != vl}")
