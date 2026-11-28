"""Essai unitaire du correcteur de la chaîne v3 : revocations_voisines du module commun v3 contre la fonction `proposees`
du banc du vérificateur (copiée ici à l'identique), sur les cas du vérificateur et du correcteur v2 et sur les registres
réels à la tête de main. Usage : python3 -B voisines_v3_v1.py VERIF_V3 GO DEC"""
import importlib.util, sys
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("v3", sys.argv[1]); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
GO = open(sys.argv[2], encoding="utf-8").read(); DEC = open(sys.argv[3], encoding="utf-8").read()
def proposees(texte_go, texte_dec):
    re, D, I = v.re, v.DEBUTS_REVOCATION, v._IDS
    tete = lambda c: c.lstrip("*_ \"'«»`([").startswith(D)
    out = []
    for n, ligne in enumerate(texte_go.split("\n"), 1):
        k = v._cellules_n(ligne)
        if not k or not re.fullmatch(r"go-\d{4}-\d{2}-\d{2}-\d{2}", k[0].strip("*_` ")):
            continue
        typ = k[2].strip("*_` ") if len(k) > 2 else ""
        if (typ.startswith(D) or typ not in v.TYPES_GO or any(tete(c) and I.search(c) for c in k[1:])) and I.search(" | ".join(k[1:])):
            out.append(f"go.md {n}")
    for n, ligne in enumerate(texte_dec.split("\n"), 1):
        k = v._cellules_n(ligne)
        if not k or not re.fullmatch(r"r-\d{3,4}", k[0].strip("*_` ")):
            continue
        if any(tete(c) and I.search(c) for c in k[1:]):
            out.append(f"decisions.md {n}")
    return out
J = "2026-10-21"
CAS = [  # nom, attendu bloqué, ajout go, ajout décisions
 ("V00-registres-reels", False, "", ""),
 ("V01-go-sans-espace", True, f"\n|GO-2026-10-21-01|{J}|révocation|révoque GO-2026-10-20-07|—|{J}|Lazar|essai|", ""),
 ("V02-type-majuscule", True, f"\n| GO-2026-10-21-01 | {J} | REVOCATION | R-269 | — | {J} | Lazar | essai |", ""),
 ("V03-deux-identifiants", True, "", f"\n| R-998 | {J} | **Révocation de R-262 et de R-269** | essai |"),
 ("V04-tiret-insecable", True, "", f"\n| R-998 | {J} | révocation de R‑269 | essai |"),
 ("V05-blancs-en-tete", True, "", f"\n   | R-998 | {J} | **Révocation de R-269.** | essai |"),
 ("V10-mention-libre", False, "", f"\n| R-998 | {J} | Note : la forme « **Révocation de R-269** » est décrite ici. | essai |"),
 ("V11-identifiant-voisin", False, "", f"\n| R-998 | {J} | **Révocation de R-2690** | essai |"),
 ("V12-go-de-calcul-qui-cite-la-phase", False, f"\n| GO-2026-10-21-01 | {J} | calcul | sous GO-2026-10-04-08 | 1 USD | {J} | Lazar | essai |", ""),
 ("X01-decision-sans-colonne-de-date", True, "", f"\n| R-998 | **Révocation de R-269** : délégation retirée |"),
 ("X02-colonne-vide-en-trop", True, "", f"\n| R-998 | {J} | | **Révocation de R-269** | essai |"),
 ("X03-identifiant-de-decision-en-gras", True, "", f"\n| **R-998** | {J} | **Révocation de R-269** | essai |"),
 ("X04-identifiant-de-go-en-gras", True, f"\n| **GO-2026-10-21-01** | {J} | révocation | GO-2026-10-20-07 | — | {J} | Lazar | essai |", ""),
 ("X05-go-de-type-decision-qui-revoque", True, f"\n| GO-2026-10-21-01 | {J} | décision | Révocation de GO-2026-10-20-07 (délégation retirée) | — | {J} | Lazar | essai |", ""),
 ("G10e-mention-dans-un-go-decision", False, f"\n| GO-2026-10-20-97 | {J} | décision | essai : aucune révocation de GO-2026-10-20-07 ni de R-269 | — | {J} | Lazar | essai |", ""),
 ("V59b-go-voisin-type-inconnu", False, f"\n| GO-2026-10-21-01 | {J} | annulation | GO-2026-10-20-071 (essai) | — | {J} | Lazar | essai |", ""),
 ("Y01-type-en-gras", True, f"\n| GO-2026-10-21-01 | {J} | **révocation** | GO-2026-10-20-06 | — | {J} | Lazar | essai |", ""),
 ("Y02-go-souligne", True, f"\n| _GO-2026-10-21-01_ | {J} | calcul | Retrait de R-262 | — | {J} | Lazar | essai |", ""),
 ("Y03-decision-guillemets-inverses", True, "", f"\n| `R-998` | {J} | « Annulation de GO-2026-10-04-08 » | essai |"),
 ("Y04-decision-qui-mentionne-un-retrait-sans-identifiant", False, "", f"\n| R-998 | {J} | Retrait de l'instance 56799469 du registre | essai |"),
]
ecarts = 0
for nom, att, ga, da in CAS:
    a, b = bool(v.revocations_voisines(GO + ga, DEC + da)), bool(proposees(GO + ga, DEC + da))
    ok = a == att and b == att
    ecarts += not ok
    print(f"{nom} : module v3 {'bloque' if a else 'passe'} ; proposees {'bloque' if b else 'passe'} ; attendu {'bloque' if att else 'passe'} ; {'CONFORME' if ok else 'ÉCART'}")
# égalité ligne à ligne sur les registres réels (toutes les lignes, une à une, ajoutées à des registres vides)
n = 0
for l in GO.split("\n"):
    n += bool(v.revocations_voisines(l, "")) != bool(proposees(l, ""))
for l in DEC.split("\n"):
    n += bool(v.revocations_voisines("", l)) != bool(proposees("", l))
print(f"lignes réelles où le module v3 et proposees diffèrent : {n}")
tetes = [l[:100] for l in DEC.split("\n") if (k := v._cellules_n(l)) and v.re.fullmatch(r"r-\d{3,4}", k[0].strip("*_` ")) and any(v._tete_de_revocation(c) for c in k[1:])]
tetesg = [l[:100] for l in GO.split("\n") if (k := v._cellules_n(l)) and v.re.fullmatch(r"go-\d{4}-\d{2}-\d{2}-\d{2}", k[0].strip("*_` ")) and any(v._tete_de_revocation(c) for c in k[1:])]
print(f"information : cellules réelles qui commencent par un début de révocation (sans nommer les cinq) : décisions {len(tetes)}, GO {len(tetesg)}")
print(f"FIN ; écarts : {ecarts + n}")
