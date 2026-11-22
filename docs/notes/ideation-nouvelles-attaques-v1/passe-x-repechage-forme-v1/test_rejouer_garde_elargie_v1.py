import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rejouer_garde_elargie_v1 as R

def test_point_final_retire_seulement_en_derniere_ligne():
    assert R.elargir("a\n\nFIN DES RÉPONSES.\n").endswith("FIN DES RÉPONSES\n")
    assert R.elargir("a\n**FIN DES RÉPONSES.**\n").endswith("**FIN DES RÉPONSES**\n")
    assert R.elargir("FIN DES RÉPONSES.\nsuite\n") == "FIN DES RÉPONSES.\nsuite\n"
    assert R.elargir("a\nFIN DES RÉPONSES..\n") == "a\nFIN DES RÉPONSES..\n"
    assert R.elargir("a\nFin des réponses.\n") == "a\nFin des réponses.\n"
    assert R.elargir("") == ""

def test_elargie_puis_garde_v4():
    lot = R.charger("diagnostic", R.DIAG).charger_lot()
    rangs = (1, 2, 3)
    corps = "\n\n".join(f"## Réponse {k}\n\n" + " ".join(["mot"] * 300) for k in rangs)
    assert lot.garde_coupure(corps + "\n\nFIN DES RÉPONSES.\n", rangs, "stop", 1, 96000)[0] == "texte coupé"
    assert lot.garde_coupure(R.elargir(corps + "\n\nFIN DES RÉPONSES.\n"), rangs, "stop", 1, 96000)[0] is None
    assert lot.garde_coupure(R.elargir(corps.replace("Réponse 2", "Réponse 9") + "\n\nFIN DES RÉPONSES.\n"), rangs, "stop", 1, 96000)[0] == "couverture incomplète"
