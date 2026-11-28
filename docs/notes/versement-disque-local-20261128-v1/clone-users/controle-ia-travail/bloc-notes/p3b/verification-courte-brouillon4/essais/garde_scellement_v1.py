# Garde du scellement telle que le plan v4 l'ecrit (ligne `sceller_p3b_v1.sh`) : refuse « en attente », « de repli »,
# « Proposition en attente », sans egard a la casse ni aux blancs (toute suite d'espaces et de retours a la ligne lue
# comme une espace). Deux lectures du mot « blancs » : (L) espaces et retours a la ligne seuls ; (U) tout blanc Unicode.
# Cas sain et artefacts (R5). Rien n'est ecrit.
import re
CH = ["en attente", "de repli", "proposition en attente"]
def garde_L(t):
    n = re.sub(r"[ \n]+", " ", t).lower()
    return [c for c in CH if c in n]
def garde_U(t):
    n = re.sub(r"\s+", " ", t).lower()
    return [c for c in CH if c in n]
cas = {
 "sain": "Statut : seconde lecture préenregistrée de P3.\n  Partition : 20 tâches de découverte.",
 "brut": "Décision de Lazar en attente : P-016",
 "pluriel, casse": "Versions De Repli (b) et (c)",
 "coupé, retour + retrait": "Version de\n  repli (B) de P-016",
 "coupé, marqueur": "Décision de Lazar en\n  attente : P-023",
 "Proposition coupée": "Proposition\n  en attente",
 "deux retours": "de\n\n repli",
 "tabulation": "de\trepli",
 "retour chariot (CRLF)": "en\r\nattente",
 "espace insécable U+00A0": "de repli",
 "espace fine insécable U+202F": "en attente",
}
for k, t in cas.items():
    print(f"{k:32s} L={'refusé ' + str(garde_L(t)) if garde_L(t) else 'accepté'} ; U={'refusé ' + str(garde_U(t)) if garde_U(t) else 'accepté'}")
