"""Brouillon 5 du préenregistrement de l'analyse boîte blanche / boîte noire : brouillon 4 + exactement les remplacements
H1 à H4 et B1 à B7 du rapport de la contre-lecture 4 (lus dans le rapport lui-même), puis Z3 à Z5 (mêmes textes du
rapport), puis Z1, Z2 et les adaptations de la voie B (décision de la session : pas de contre-lecture 5, un seul marqueur).

Garde : empreintes du brouillon 4 et du rapport vérifiées avant tout ; chaque « ancien » doit figurer exactement une fois
au moment où il est remplacé ; le brouillon 5 ne doit pas exister (R12). Vérifications finales : `exiger_code_cite`
(27 fichiers), `prereg.problemes` (seul le marqueur du commit cité), puis remplacement simulé du marqueur sur une copie
jetable (`problemes` vide). N'écrit que le brouillon 5 ; la sortie standard est la trace (`…-sortie.txt`).

Lancement (racine du dépôt) : `PYTHONPATH=src python3 brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/appliquer-contre-lecture-4-v1.py`
"""
import hashlib
import re
import sys
import tempfile
from pathlib import Path

DOSSIER = Path("brouillons/preuves-mentors-v1/analyse-blanche-noire-v1")
B4 = DOSSIER / "preenregistrement-analyse-blanche-noire-v1-brouillon4.md"
B5 = DOSSIER / "preenregistrement-analyse-blanche-noire-v1-brouillon5.md"
RAPPORT = DOSSIER / "contre-lecture-4-preenregistrement-analyse-v1.md"
SHA_B4 = "ee11631689a96e8c89468b231b67c52dbd240aeac3343e052acaf27f3acbca98"
SHA_RAPPORT = "dbf68e82abb8e82340a601e122812b2192040dc36bc0974693ee935b628bed36"
COMMIT_RAPPORT = "1a9f1b97"
REJEU = ("rejeu-frequence-regle-decision-v2-sur-v3-contre-lecture-3-v1.py",
         "rejeu-frequence-regle-decision-v2-sur-v3-contre-lecture-3-v1-sortie.txt")
SHA_REJEU = ("774ec9fb8d6ef657d2e1860ab9de7d340c6659c765e54611ae609c7f9b08448b",
             "7b2d1a7be90c7945f8af1c14a44c907543ef8a8a96ada84d6a69c3172fe54f87")
PLAN = [("H1", 1), ("H2", 3), ("H3", 1), ("H4", 1), ("B1", 1), ("B2", 1), ("B3", 3), ("B4", 2), ("B5", 1), ("B6", 1),
        ("B7", 1), ("Z3", 2), ("Z4", 1), ("Z5", 1)]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def court(t: str) -> str:
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:12]


def remplacements_du_rapport(texte: str) -> dict:
    """{identifiant: [(ancien, nouveau), …]} dans l'ordre du rapport (titres « #### Xn … »)."""
    sortie = {}
    for m in re.finditer(r"^#### (\S+)[^\n]*\n(.*?)(?=^#### |^## |\Z)", texte, re.M | re.S):
        paires = re.findall(r"remplacer :\s*```text\n(.*?)\n```\s*par :\s*```text\n(.*?)\n```", m.group(2), re.S)
        if paires:
            sortie.setdefault(m.group(1), []).extend(paires)
    return sortie


EXCEPTIONS = ("aucune pour H1 à H4 ; compléments mécaniques : B1, B2, B3 et B6 mot pour mot, chevrons remplis (commit "
              "`1a9f1b97`) ; B4 (1 et 2), B5 et B7 adaptés par décision de la session (voie B : pas de contre-lecture 5, "
              "un seul marqueur restant, l'entrée de la contre-lecture 4 remplie dès ce brouillon) ; ajouts de l'auteur : "
              "« un seul marqueur » dans les « Marqueurs de gabarit » et à l'étape 0.c, fichiers versés ajoutés à "
              "l'étape 0.a")
SUGGESTIONS = ("Z1 appliquée pour le marqueur restant (le point final qui suit le marqueur reste en place ; la partie "
               "« guillemets » est sans objet, aucun marqueur de contre-lecture ne restant) ; Z2 appliquée (script et "
               "sortie du rejeu de la contre-lecture 3 versés au dossier sous des noms neufs, mêmes octets, `774ec9fb…` "
               "et `7b2d1a7b…`, cités par chemin ; la ligne finale « exit 0 » dite) ; Z3, Z4 et Z5 appliquées mot pour "
               "mot")
SANS_CL5 = ("- **Pas de contre-lecture 5** (décision de la session conv-audit, voie B, comme pour l'essaim hors "
            "échantillon) : le brouillon 5 est le brouillon 4 plus exactement les remplacements H1 à H4 et B1 à B7 du "
            "rapport de la contre-lecture 4 (B4, B5 et B7 adaptés : un seul marqueur) et ses suggestions Z1 à Z5, "
            "appliqués par le script `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/"
            "appliquer-contre-lecture-4-v1.py`, qui vérifie les empreintes du brouillon 4 et du rapport et une occurrence "
            "exacte de chaque ancien texte (trace : `appliquer-contre-lecture-4-v1-sortie.txt`) ; **écart à la règle R2, "
            "déclaré** : H1 et H2, textes de fond écrits par le contre-lecteur 4, sont appliqués mot pour mot sans être "
            "relus par un lecteur qui ne les a pas écrits.")
ADAPTATIONS = {   # (identifiant, rang) → nouveau texte de la session (l'ancien reste celui du rapport)
    ("B4", 0): ("(la version finale committée à l'étape a : brouillon 5, brouillon 4 corrigé selon la contre-lecture 4, "
                "sans contre-lecture 5 : décision de la session, voie B)"),
    ("B4", 1): ("aucun autre (l'entrée de la contre-lecture 4 est remplie dès le brouillon 5 ; pas de contre-lecture 5)"),
    ("B5", 0): ("2. aucune ligne de contre-lecture ne porte de marqueur : l'entrée de la contre-lecture 4 est remplie dès "
                "le brouillon 5 et il n'y a pas de contre-lecture 5 (décision de la session, voie B ; section "
                "« Contre-lecture »)."),
}
AJOUTS = [   # ajouts de l'auteur, après les remplacements du rapport (ancien, nouveau, motif)
    ("Deux marqueurs restent, remplis au scellement (étape 0.c) par le contenu ci-dessous et rien d'autre :",
     "Un seul marqueur reste (item 1), rempli au scellement (étape 0.c) par le contenu ci-dessous et rien d'autre :",
     "voie B : un seul marqueur"),
    ("n'y remplacer que les deux marqueurs de gabarit, chacun par le contenu exact",
     "n'y remplacer que le marqueur de gabarit restant, par le contenu exact", "voie B : un seul marqueur"),
    ("(premier commit de l'étape, ni amendé ni refait), entre accents graves, puis le point final ;",
     "(premier commit de l'étape, ni amendé ni refait), entre accents graves ; le point final qui suit le marqueur reste "
     "en place, aucun n'est ajouté ;", "Z1"),
    ("script `rejeu_frequence_sur_v3.py`, `774ec9fb8d6ef657d2e1860ab9de7d340c6659c765e54611ae609c7f9b08448b`, et sortie, "
     "`7b2d1a7be90c7945f8af1c14a44c907543ef8a8a96ada84d6a69c3172fe54f87`, dans le bloc-notes du relecteur, hors du dépôt) : "
     "sortie identique à la sortie citée, hors la durée —",
     f"script et sortie du relecteur versés au dossier par le brouillon 5 sous des noms neufs, mêmes octets : "
     f"`brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/{REJEU[0]}` (`{SHA_REJEU[0]}`) et "
     f"`brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/{REJEU[1]}` (`{SHA_REJEU[1]}`)) : sortie identique à la "
     f"sortie citée, hors la durée et une ligne finale « exit 0 » ajoutée par l'enveloppe du rejeu —", "Z2"),
    ("`calculs-predictions-v2.py` et sa sortie, les deux scripts de fréquence et leurs sorties ;",
     f"`calculs-predictions-v2.py` et sa sortie, les deux scripts de fréquence et leurs sorties, les deux fichiers du rejeu "
     f"de la contre-lecture 3 versés sous des noms neufs (`{REJEU[0]}`, `{REJEU[1]}`), le script "
     f"`appliquer-contre-lecture-4-v1.py` et sa sortie ;", "Z2 et voie B : fichiers versés"),
]


def main() -> int:
    print("# Trace de appliquer-contre-lecture-4-v1.py")
    for p, attendu in ((B4, SHA_B4), (RAPPORT, SHA_RAPPORT)):
        h = sha(p)
        print(f"empreinte {p.name} : {h} {'= attendue' if h == attendu else '≠ ATTENDUE ' + attendu}")
        if h != attendu:
            return 1
    for nom, attendu in zip(REJEU, SHA_REJEU):
        h = sha(DOSSIER / nom)
        print(f"empreinte {nom} (Z2) : {h} {'= attendue' if h == attendu else '≠ ATTENDUE ' + attendu}")
        if h != attendu:
            return 1
    if B5.exists():
        print(f"{B5} existe déjà : arrêt (R12)")
        return 1
    rr = remplacements_du_rapport(RAPPORT.read_text(encoding="utf-8"))
    s = B4.read_text(encoding="utf-8")
    n = 0
    for ident, attendu in PLAN:
        paires = rr.get(ident, [])
        if len(paires) != attendu:
            print(f"{ident} : {len(paires)} remplacements dans le rapport, {attendu} attendus : arrêt")
            return 1
        for rang, (ancien, nouveau) in enumerate(paires):
            source = "rapport"
            nouveau = nouveau.replace("<commit du rapport de la contre-lecture 4>", COMMIT_RAPPORT)
            if ident == "B7":
                nouveau = (nouveau.replace("<empreinte du rapport>", SHA_RAPPORT)
                           .replace("<exceptions du rédacteur, ou « aucune »>", EXCEPTIONS)
                           .replace("<chacune appliquée ou non, avec son motif>", SUGGESTIONS))
                lignes = nouveau.split("\n")
                assert len(lignes) == 2 and lignes[1].startswith("- **Contre-lecture 5**")
                nouveau = lignes[0] + "\n" + SANS_CL5
                source = "rapport, chevrons remplis ; ligne « Contre-lecture 5 » remplacée (voie B)"
            elif (ident, rang) in ADAPTATIONS:
                nouveau = ADAPTATIONS[(ident, rang)]
                source = "ancien du rapport ; nouveau adapté (voie B)"
            elif "<commit du rapport" not in paires[rang][1] and nouveau == paires[rang][1]:
                source = "rapport, mot pour mot"
            else:
                source = "rapport, chevrons remplis"
            k = s.count(ancien)
            if k != 1:
                print(f"{ident} ({rang + 1}) : ancien présent {k} fois : arrêt")
                return 1
            if re.search(r"<[^<>`]*(?:rapport|brouillon|exceptions|chacune)[^<>`]*>", nouveau):
                print(f"{ident} ({rang + 1}) : champ entre chevrons non rempli : arrêt")
                return 1
            s = s.replace(ancien, nouveau)
            n += 1
            print(f"{ident} ({rang + 1}/{len(paires)}) appliqué — {source} ; ancien {court(ancien)}, nouveau {court(nouveau)}")
    for ancien, nouveau, motif in AJOUTS:
        k = s.count(ancien)
        if k != 1:
            print(f"ajout ({motif}) : ancien présent {k} fois : arrêt")
            return 1
        s = s.replace(ancien, nouveau)
        n += 1
        print(f"ajout de l'auteur ({motif}) appliqué ; ancien {court(ancien)}, nouveau {court(nouveau)}")
    B5.write_text(s, encoding="utf-8")
    print(f"{n} remplacements ; écrit {B5} ({len(s.encode('utf-8'))} octets) ; sha256 {sha(B5)}")

    sys.path.insert(0, "src")
    from controle_ia.analyse_blanche_noire import lecture_v3
    from controle_ia.prereg import problemes
    cite = lecture_v3.exiger_code_cite(s)
    print(f"exiger_code_cite : {len(cite['fichiers'])} fichiers cités conformes ; constantes {cite['constantes']}")
    print(f"marqueurs « À REMPLIR » restants : {s.count('À REMPLIR')}")
    print(f"prereg.problemes (brouillon 5) : {problemes(B5)}")
    m = re.search(r"`À REMPLIR au scellement : 40 caractères hexadécimaux du commit cité \(étape 0 du Plan d'analyse\)`", s)
    with tempfile.TemporaryDirectory() as d:
        copie = Path(d) / "simulation.md"
        copie.write_text(s[:m.start()] + "`" + "0" * 40 + "`" + s[m.end():], encoding="utf-8")
        lignes_diff = sum(a != b for a, b in zip(s.split("\n"), copie.read_text(encoding="utf-8").split("\n")))
        print(f"simulation du scellement (marqueur remplacé par 40 zéros, copie jetable) : {lignes_diff} ligne(s) "
              f"différente(s) ; prereg.problemes : {problemes(copie)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
