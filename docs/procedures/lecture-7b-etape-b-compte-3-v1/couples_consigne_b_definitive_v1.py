"""Mise au propre de la consigne du lecteur B : brouillon 5 → `consigne-lecteur-b-v1.md`, par couples « ancien → nouveau » — v1.

Raison unique : la contre-lecture du brouillon 5, tour 3 (`contre-lecture-consigne-lecteur-b-v1-tour3-v1.md`,
17283ae867ee1f248d0b74d840f119e045f69336750fe83d8160f43631d4ee94, même dossier) le juge scellable, sans correction, et
liste les gestes de mise au propre (§ 6, point 1). Deux couples seulement, et rien d'autre : (1) la puce « État du fichier »
réécrite (heure de la mise au propre lue par `date -u`, passée en argument) ; (2) le jeton `EMPREINTE-COMMANDE-V4-A-REMPLIR`
remplacé par l'empreinte sha256 de `commande-compte-3-phase-c-v4.md` (même dossier), lue sur le fichier et égale à
l'attendue.

Usage : python3 -I -B couples_consigne_b_definitive_v1.py --heure AAAA-MM-JJTHH:MM:SSZ [--cible CHEMIN]
(`--cible` : pour un essai dans un dossier jetable seulement ; par défaut, `consigne-lecteur-b-v1.md`, même dossier.)
Gardes : heure de la forme `date -u +%Y-%m-%dT%H:%M:%SZ` ; empreinte du brouillon 5 égale à l'attendue ; empreinte de la
commande v4 définitive égale à l'attendue ; chaque « ancien » présent exactement une fois dans le brouillon 5, et encore une
seule fois au moment où il est remplacé ; aucun « nouveau » égal à son « ancien » ; aucun recouvrement entre les deux
« anciens » ; aucun marqueur `{heure}` restant ; jeton absent du résultat ; cible absente (création exclusive : jamais
d'écrasement). Tout écart : code 1, rien n'est écrit. Le sceau (compagnon `.sha256`) est posé ensuite par
`controle_ia.scellement sceller`.
"""
import hashlib
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "consigne-lecteur-b-v1-brouillon5.md"
EMPREINTE_SOURCE = "b9ef96b6425739334aae13eb63a417540beed44769b9dca587b8268047c966a4"
COMMANDE = ICI / "commande-compte-3-phase-c-v4.md"
EMPREINTE_COMMANDE = "f4bcf4064e7ab7d53538ce998c2d4745a1ac4387443505d82e8f7a01aec7c755"
CIBLE = ICI / "consigne-lecteur-b-v1.md"
FORME_HEURE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
JETON = "EMPREINTE-COMMANDE-V4-A-REMPLIR"

ETAT_ANCIEN = (
    "- **État du fichier** : brouillon 5, écrit le 2026-11-16 (heure du sceau d'intégrité, `date -u` : 2026-11-16T14:28:47Z) par un\n"
    "  quatrième rédacteur, sous-agent neuf (modèle C) de la session mère, qui n'a écrit ni le texte de T0.7, ni aucune autre\n"
    "  pièce de ta liste, ni aucun brouillon antérieur de cette consigne, et n'a ouvert aucune donnée ni aucun résultat de 7a,\n"
    "  de 7b ou de T0.7 ; **brouillon 5 = brouillon 4** (`consigne-lecteur-b-v1-brouillon4.md`,\n"
    "  `ce397083f351d21fbf72a72b7b1c14a1e5acc6744ac1de762e38f5eb9fe313ab`, gardé tel quel, règle R12 ; lui-même brouillon 3\n"
    "  plus les corrections K1 à K22 de la contre-lecture, tour 1) **plus les corrections C1 à C4 de sa contre-lecture,\n"
    "  tour 2** (réponse point par point : section « Contre-lecture », à la fin) ; changements faits par le programme de\n"
    "  couples « ancien → nouveau » `couples_consigne_b_brouillon5_v1.py` (même dossier). **Non scellé comme consigne** (son\n"
    "  compagnon n'atteste que l'intégrité, règle R6). Contre-lu deux fois, sur les brouillons 3 et 4 ; à contre-lire par\n"
    "  différentiel (règle R2) par un sous-agent neuf qui n'en a écrit aucun brouillon, puis à sceller par la session mère\n"
    "  sous son nom définitif. Cette puce est réécrite au scellement.\n")

ETAT_NOUVEAU = (
    "- **État du fichier** : consigne v1, écrite par le modèle B (brouillons 1 et 2) et par le modèle A (brouillon 3 et\n"
    "  corrections), contre-lue par le modèle C (rapports et empreintes :\n"
    "  `docs/procedures/lecture-7b-etape-b-compte-3-v1/contre-lecture-consigne-lecteur-b-v1-tour1-v1.md`,\n"
    "  `2594d8c63cbcd83615811d927f46aaca1d04f9a9ac6a5aec5fa53e6274d7cc7d` ;\n"
    "  `docs/procedures/lecture-7b-etape-b-compte-3-v1/contre-lecture-consigne-lecteur-b-v1-tour2-v1.md`,\n"
    "  `a205571e138e1ca3e35737e89831c83f674921457e2a5b23f40ae37e2cea694e` ;\n"
    "  `docs/procedures/lecture-7b-etape-b-compte-3-v1/contre-lecture-consigne-lecteur-b-v1-tour3-v1.md`,\n"
    "  `17283ae867ee1f248d0b74d840f119e045f69336750fe83d8160f43631d4ee94`), lecture à blanc par le modèle C, mise au propre\n"
    "  le {heure} (`date -u`), scellée ; son compagnon atteste qu'elle est en vigueur.\n")

COUPLES = [
    ("puce « État du fichier »", ETAT_ANCIEN, ETAT_NOUVEAU),
    ("jeton de l'empreinte de la commande v4", f"(`{JETON}`)", f"(`{EMPREINTE_COMMANDE}`)"),
]


def arret(motif: str) -> None:
    print(f"ARRÊT : {motif} ; rien n'est écrit")
    sys.exit(1)


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(argv: list) -> int:
    args = dict(zip(argv[0::2], argv[1::2]))
    if len(argv) % 2 or "--heure" not in args or set(args) - {"--heure", "--cible"}:
        print("usage : couples_consigne_b_definitive_v1.py --heure AAAA-MM-JJTHH:MM:SSZ [--cible CHEMIN]")
        return 2
    heure = args["--heure"]
    if not FORME_HEURE.match(heure):
        arret(f"heure « {heure} » hors de la forme date -u +%Y-%m-%dT%H:%M:%SZ")
    cible = pathlib.Path(args["--cible"]).resolve() if "--cible" in args else CIBLE
    h = sha(SOURCE)
    if h != EMPREINTE_SOURCE:
        arret(f"empreinte du brouillon 5 {h} différente de l'attendue")
    hc = sha(COMMANDE) if COMMANDE.is_file() else "absente"
    if hc != EMPREINTE_COMMANDE:
        arret(f"empreinte de la commande v4 définitive {hc} différente de l'attendue")
    texte = SOURCE.read_text(encoding="utf-8")
    places = []
    for nom, ancien, nouveau in COUPLES:
        n = texte.count(ancien)
        if n != 1 or ancien == nouveau:
            arret(f"{nom} : « ancien » trouvé {n} fois (une attendue) ou égal au « nouveau »")
        i = texte.find(ancien)
        places.append((i, i + len(ancien), nom))
    places.sort()
    for (a1, b1, n1), (a2, b2, n2) in zip(places, places[1:]):
        if a2 < b1:
            arret(f"recouvrement entre {n1} et {n2}")
    for nom, ancien, nouveau in COUPLES:
        nouveau = nouveau.replace("{heure}", heure)
        if texte.count(ancien) != 1:
            arret(f"{nom} : « ancien » plus présent une seule fois au remplacement")
        texte = texte.replace(ancien, nouveau, 1)
        print(f"appliqué : {nom}")
    if "{heure}" in texte:
        arret("marqueur {heure} restant")
    if JETON in texte:
        arret("jeton restant")
    try:
        with open(cible, "x", encoding="utf-8", newline="") as f:
            f.write(texte)
    except FileExistsError:
        arret(f"{cible} existe déjà (jamais d'écrasement)")
    print(f"source {SOURCE.name} : {h}")
    print(f"commande {COMMANDE.name} : {hc}")
    print(f"couples appliqués : {len(COUPLES)} ; heure : {heure}")
    print(f"cible {cible.name} : {sha(cible)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
