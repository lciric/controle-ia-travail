"""Couples « ancien / nouveau » proposés pour un brouillon 4 du texte de B bis (question 2 de la mère, R-2902), v1 —
**proposition seulement** : ce programme n'écrit **aucun** brouillon dans le dépôt et ne change ni le code ni le texte. Il vérifie
que le brouillon 3 est celui de son compagnon (`f104917f…`), que chaque « ancien » y figure **exactement une fois**, applique les
couples **en mémoire**, et imprime les couples et l'empreinte du texte qui en résulterait (à reprendre, s'ils sont retenus, par le
programme de couples du brouillon 4, sous le mot de Lazar). Les chiffres de la réserve sont lus dans les sorties scellées.

Groupes : (a) option 1 du diagnostic (contrôle « attention » à 3 époques au même seuil, linéaire à 300 époques, déterminisme de
la sonde « attention » du couple sur la carte) ; (b) réserve de reproductibilité R-PILE. **(c) n'est pas proposé** : la dispersion
des aires entre piles est négligeable dès que la sonde apprend un signal ; elle n'atteint 0,0074 que pour une sonde qui n'apprend
rien (aire 0,46), dont aucune lecture ne dépend (`diagnostic-stabilite-aires-attention-v1.md`, § 4).

Lancement : `python3 -I -B diagnostic-stabilite-aires-attention-v1-couples.py DOSSIER_DU_BROUILLON STABILITE.json SIGNAL.json`
(`diagnostic-stabilite-aires-attention-v1-sortie.json`, `diagnostic-stabilite-aires-attention-signal-v1-sortie.json`).
"""
import hashlib
import json
import sys
from pathlib import Path

DOSSIER = Path(sys.argv[1])
STAB = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
SIG = json.loads(Path(sys.argv[3]).read_text(encoding="utf-8"))
B3 = DOSSIER / "T0.7-etape-B-bis-v1-brouillon3.md"
EMPREINTE_B3 = "f104917f8e858d405fa00ced84ae6bfbc1217fcbc043801475f6b39c923153ba"
DIAG = "`brouillons/T0.7-etape-B-bis-v1/code/diagnostic-ecart-attention-carte-v1.md`, `5ecb9235…`"
STABMD = "`brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1.md`"

texte = B3.read_text(encoding="utf-8")
assert hashlib.sha256(texte.encode("utf-8")).hexdigest() == EMPREINTE_B3, "brouillon 3 autre que celui du compagnon"


def nombre(v: float, n: int = 2) -> str:
    return f"{v:.{n}f}".replace(".", ",")


def puissance(v: float) -> str:
    """7.8e-05 → « 7,8·10⁻⁵ »."""
    m, e = f"{v:.1e}".split("e")
    return f"{m.replace('.', ',')}·10" + str(int(e)).translate(str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"))


piles0 = STAB["familles"]["attention"]["dispersion"]["piles (P0, P1, P2, S0)"]
sig = {d: SIG[f"decalage_{d}"]["familles"]["attention"] for d in ("2.0", "4.0", "8.0")}
aires_ref = [v["aires"]["signal-gele-attention"] for v in sig.values()]
etendue_sig = max(v["dispersion"]["etendue"] for v in sig.values())
ecart_sig4 = max(p["ecart_controle"] for p in sig["4.0"]["paires"].values())
ecart_sig2 = max(p["ecart_controle"] for p in sig["2.0"]["paires"].values())
DISP = (f"sur données synthétiques de la taille de la course, entre quatre piles de calcul, aires d'une sonde « attention » qui "
        f"n'apprend rien (aire {nombre(piles0['moyenne'])}) d'étendue {nombre(piles0['etendue'], 4)}, et d'étendue au plus "
        f"{puissance(etendue_sig)} pour des sondes qui apprennent un signal (aires {nombre(min(aires_ref))} à "
        f"{nombre(max(aires_ref))})")

COUPLES = [
    # ------------------------------------------------------------------ (a) option 1
    ("a1 plan, point 5",
     "**contrôle à la marche** : un (cellule, pli) tiré par graine est réappris sur le processeur par `sondes.familles` ; écart "
     "relatif maximal des scores sur 256 actions tirées ≤ 10⁻⁴, sinon arrêt (erreur de chaîne).",
     "**contrôle à la marche** : un (cellule, pli) tiré par graine est réappris sur le processeur par `sondes.familles`, depuis le "
     "même départ (mêmes graines que la marche), à la couche et à la régularisation retenues pour ce couple, **dans les deux "
     "familles** : la linéaire à 300 époques, l'attention à **3 époques** (`Reglages(epoques=3)`, les mêmes trois époques "
     "réapprises sur la carte) ; écart relatif maximal des scores sur 256 actions tirées ≤ 10⁻⁴ pour chacune, sinon arrêt "
     "(erreur de chaîne) ; la sonde « attention » de 300 époques du couple est réapprise une seconde fois sur la carte et doit "
     "être égale à la première au bit près (déterminisme), sinon arrêt. Raison, écrite avant toute lecture : quand la sonde « "
     "attention » n'apprend rien ou presque, ses 300 époques amplifient les écarts d'arrondi entre deux piles de calcul au-delà "
     "de 10⁻⁴ (sans signal : 0,633 pour le paquet gelé contre lui-même sous un autre jeu d'instructions du processeur, "
     f"2,131·10⁻² entre la carte et le processeur à la répétition du 15 novembre ; signal faible : {puissance(ecart_sig2)}) ; "
     f"avec un signal, non (au plus {puissance(ecart_sig4)}) ; à 3 époques, l'écart entre deux piles reste de 2,9·10⁻⁷ à "
     f"5,9·10⁻⁷ même sans signal ({DIAG} ; {STABMD})."),
    ("a2 liste d'arrêt",
     "- Contrôle carte-processeur de l'apprentissage au-delà de 10⁻⁴ : arrêt (erreur de chaîne) ;",
     "- Contrôle carte-processeur de l'apprentissage au-delà de 10⁻⁴ (linéaire à 300 époques, attention à 3 époques ; plan, "
     "point 5), ou sonde « attention » du couple non déterministe sur la carte : arrêt (erreur de chaîne) ;"),
    ("a3 code neuf",
     "`validation_imbriquee_v1` (plis, grille, sélection, sonde finale, nul de réétiquetage, ENC, garde de débit)",
     "`validation_imbriquee_v2` (plis, grille, sélection, sonde finale, nul de réétiquetage, ENC, garde de débit ; contrôle "
     "carte-processeur aux deux horizons du point 5 et déterminisme de la sonde « attention » du couple ; la v1 reste, R12)"),
    ("a4 épreuves",
     "(activations décalées) ; égalité carte-processeur ; garde de débit",
     "(activations décalées) ; égalité carte-processeur (linéaire à 300 époques, attention à 3 époques ; artefacts : autre "
     "graine, poids altérés de 1 % ; déterminisme : cas sain et artefact) ; garde de débit"),
    # ------------------------------------------------------------------ (b) réserve de reproductibilité
    ("b1 qualifications",
     "**R-G3** (marque de la table A), audit R4 et ses motifs.",
     "**R-G3** (marque de la table A), **R-PILE** (écrite dès qu'une sonde finale lue est de la famille « attention » : « sonde "
     "« attention » reproductible au bit près sur la même pile de calcul seulement (carte, pilote, versions de torch et de "
     "numpy) ; sur une autre pile, l'apprentissage peut rendre une autre sonde, surtout quand elle n'apprend rien » ; "
     + DISP + f" ; {STABMD}), audit R4 et ses motifs."),
    ("b2 section D",
     "(6) le libellé d'information (lettre de R-2716) ne dit pas « plafond tient » : seul le libellé « lecture dure », retenu, "
     "écarte de façon établie l'adaptateur seul et retient la condition « muette sur le jumeau ».",
     "(6) le libellé d'information (lettre de R-2716) ne dit pas « plafond tient » : seul le libellé « lecture dure », retenu, "
     "écarte de façon établie l'adaptateur seul et retient la condition « muette sur le jumeau » ; (7) une aire de la famille « "
     "attention » est celle d'**une** sonde parmi celles que rendrait le même apprentissage sous d'autres arrondis (réserve "
     "R-PILE) : sur données synthétiques, la dispersion est négligeable quand la sonde apprend un signal, de l'ordre de 0,007 "
     "quand elle n'apprend rien ; sur de vraies activations, elle n'est pas mesurée."),
]

journal = []
for nom, ancien, nouveau in COUPLES:
    n = texte.count(ancien)
    if n != 1:
        raise SystemExit(f"{nom} : « ancien » présent {n} fois : {ancien[:90]!r}")
    texte = texte.replace(ancien, nouveau)
    journal.append(nom)
print(f"brouillon 3 : {EMPREINTE_B3} ; couples appliqués en mémoire : {len(journal)} ({', '.join(journal)})")
print(f"texte qui en résulterait (non écrit) : {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")
for nom, ancien, nouveau in COUPLES:
    print(f"\n### {nom}\n\n**Ancien** :\n\n> {ancien.strip()}\n\n**Nouveau** :\n\n> {nouveau.strip()}")
