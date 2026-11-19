#!/usr/bin/env python3
"""Extrait d'une mémoire des problèmes la seule pièce diffusable à une session fille.

La pièce porte : six règles, le glossaire, puis la partition « commune », sans renvoi R-, sans date,
sans heure d'horloge, sans durée chiffrée, sans « Comptes » ni liste des non classés, et sans
l'empreinte de sa source. La correspondance des empreintes (source, pièce, programme) est écrite
dans un fichier à part, pour la session mère.

Ordre des gestes : la pièce est fabriquée en mémoire, la garde la juge, et les fichiers de sortie ne
sont ouverts qu'ensuite. Le programme refuse d'écraser un fichier existant (code 2). Si la garde
refuse (code 1), rien n'est écrit ni créé.
"""
import argparse
import datetime
import hashlib
import os
import re
import sys
import tempfile

MOTS_INTERDITS = ["sabot", "sonde", "moniteur", "exécutante", "bras A", "lentille", "organisme", "idéation",
                  "Carbon", "Argon", "Astra", "Kimi", "Moonshot", "Bailey", "barreau", "billet", "côté ",
                  "Opus", "Sonnet", "Fable",
                  "addend", "non mesurée", "session hôte", "invalide une lecture", "coupait des chaînes",
                  "⟦", "⟧", "sha256", "empreinte de la source"]
MOTIFS_INTERDITS = [r"R-\d", r"\b\d\d-\d\d\b", r"\b\d\d:\d\d", r"20\d\d-", r"GO-", r"registres/\w",
                    r"\b[jJ]eux?\b", r"\d\s?h\b", r"\d+ (?:minutes?|secondes?|heures?)\b", r"\b[0-9a-f]{12,}\b"]
PAR = re.compile(r"\s*\([^()]*(?:R-\d+|passations? 20\d\d|registres/arrets)[^()]*\)")
PREFIXE_DATE = re.compile(r"^  - (?:nuit du )?\d\d-\d\d[0-9a-zàé :Z\-]*, ")
RESERVE = re.compile(r"⟦mère : [^⟦⟧]*⟧")

REGLE_2 = ("2. Cette pièce ne fait foi sur rien. Dans la version complète, chaque fait renvoie à une ligne des registres ; "
           "ces renvois, les dates et les heures d'horloge ont été retirés de cette pièce par programme. Une attente n'est dite "
           "« écrit avant » que si une pièce antérieure à l'observation la portait.")
REGLE_3 = ("3. Aucun résultat d'expérience, aucun mécanisme d'expérience, aucune valeur de seuil, aucun fragment de consigne, "
           "aucun score, aucun contenu de verdict, aucun montant.")
REGLE_4 = ("4. Cette pièce ne porte que les problèmes qui valent pour toute session ; rien n'y dit à quoi travaille une autre "
           "session, ni où en est son travail : les rôles y sont nommés sans chantier (« une session fille », « un opérateur », "
           "« un contre-lecteur »).")


def ligne(l):
    if l.startswith("- vu :"):
        n = len(re.findall(r"R-\d+", l)) + len(re.findall(r"20\d\d-\d\d-\d\d-\d{4}", l))
        return f"- vu : {n} renvois aux registres de la session mère."
    l = RESERVE.sub("non rapporté dans cette pièce", l)
    l = re.sub(r"\(écrit avant, source[^()]*\)", "(écrit avant)", l)
    while PAR.search(l):
        l = PAR.sub("", l)
    l = PREFIXE_DATE.sub("  - ", l)
    l = re.sub(r"^- état : tenu depuis .*$", "- état : tenu", l)
    l = "  - " + re.sub(r" {2,}", " ", l[4:]) if l.startswith("  - ") else re.sub(r" {2,}", " ", l)
    return l.replace(" ; ;", " ;").replace(" .", ".").replace(" ,", ",")


def garde(texte):
    fautes = []
    permis = set(re.findall(r"^### (M-\d+) — ", texte, flags=re.M))
    for n, l in enumerate(texte.split("\n"), 1):
        for ident in re.findall(r"M-\d+", l):
            if ident not in permis:
                fautes.append((n, "renvoi à " + ident + ", absent de la pièce"))
        for m in MOTIFS_INTERDITS:
            if re.search(m, l):
                fautes.append((n, m))
        for m in MOTS_INTERDITS:
            if m in l:
                fautes.append((n, m))
    return fautes


def extraire(src):
    L = src.split("\n")
    i = next(k for k, l in enumerate(L) if l.startswith("**Règles.**"))
    regles = [l for l in L[i + 1:i + 12] if re.match(r"^\d\. ", l)]
    if len(regles) != 6:
        raise SystemExit(f"ARRET : {len(regles)} règles trouvées, 6 attendues")
    g = next((k for k, l in enumerate(L) if l.startswith("**Glossaire.**")), None)
    if g is None:
        raise SystemExit("ARRET : glossaire absent de la source")
    glossaire = []
    for l in L[g + 1:]:
        if not l.startswith("- "):
            break
        glossaire.append(l)
    if len(glossaire) < 5:
        raise SystemExit(f"ARRET : glossaire de {len(glossaire)} lignes, 5 au moins attendues")
    a = next(k for k, l in enumerate(L) if l.startswith("## Partition « commune »"))
    b = next(k for k in range(a + 1, len(L)) if L[k].startswith("---"))
    corps = [ligne(l) for l in L[a + 1:b]]
    regles = [ligne(regles[0]), REGLE_2, REGLE_3, REGLE_4, ligne(regles[4]), ligne(regles[5])]
    tete = ["# Mémoire des problèmes récurrents de procédure et d'outillage — partie commune, pièce diffusable",
            "",
            "Extraite par programme de la version complète tenue par la session mère ; la correspondance entre les deux "
            "empreintes est consignée par la mère, hors de cette pièce.",
            "Chaque problème garde ses tentatives : ce qui a été fait, ce qu'on en attendait avant, ce qui s'est passé, "
            "la parade retenue, et le signal auquel tu reconnais que tu es en train de refaire l'erreur.",
            "",
            "**Règles.**"] + regles + ["", "**Glossaire.**"] + glossaire + ["", "## Problèmes", ""]
    out = "\n".join(tete + corps).rstrip("\n") + "\n"
    f = garde(out)
    if f:
        raise SystemExit("ARRET : la garde refuse la pièce, rien n'est écrit : "
                         + "; ".join(f"ligne {n} : {m}" for n, m in f[:25]))
    return out


def h(octets):
    return hashlib.sha256(octets).hexdigest()


def produire(source, sortie, correspondance):
    for p in (sortie, correspondance):
        if os.path.lexists(p):
            print(f"ARRET : {p} existe déjà ; ce programme n'écrase jamais (nom neuf exigé).", file=sys.stderr)
            return 2
    src = open(source, encoding="utf-8").read()
    piece = extraire(src).encode("utf-8")          # la garde juge ici ; SystemExit (code 1) avant toute ouverture
    table = "\n".join([
        "# Correspondance des empreintes — pièce diffusable de la mémoire des problèmes",
        "",
        "Fichier de la session mère ; il n'accompagne jamais la pièce diffusée.",
        "",
        "| rôle | chemin | sha256 |",
        "|---|---|---|",
        f"| source complète | `{source}` | `{h(src.encode('utf-8'))}` |",
        f"| pièce diffusable | `{sortie}` | `{h(piece)}` |",
        f"| programme d'extraction | `{sys.argv[0]}` | `{h(open(__file__, 'rb').read())}` |",
        "",
        f"Extraction jouée à {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} (horloge de la machine).",
        ""]).encode("utf-8")
    with open(sortie, "xb") as f:
        f.write(piece)
    with open(correspondance, "xb") as f:
        f.write(table)
    print("écrit :", sortie)
    print("écrit :", correspondance)
    return 0


SOURCE_FACTICE = """# factice

**Règles.**
1. un (R-1).
2. deux.
3. trois.
4. quatre.
5. cinq.
6. six.

**Glossaire.**
- feu : a.
- amorce : b.
- ligne d'accord : c.
- crochet : d.
- mandataire : e.
- loueur : f.

---

## Partition « commune »

### M-001 — problème factice
- vu : R-1 (11-18), R-2 (11-19) ; passation 2026-11-18-0254.
- tentatives :
  - 11-14 au 11-18, session sœur : fait (R-1, R-22) ; attendu : x (écrit avant, source : note, citée par R-3) ; observé : ⟦mère : issue (R-4) — attente juste⟧.
  - 11-19, mère : INSERTION ; attendu : non écrit avant ; observé : rien (passation 2026-11-18-0254).
- parade en vigueur : aucune parade écrite.
- signal d'alerte : aucun.
- état : tenu depuis 2026-11-18

---

## Partition « mère »
"""

ARTEFACTS = ["voir R-1234 ailleurs", "le 11-18, autre chose", "à 06:25Z", "course du saboteur", "tenu depuis 2026-11-18",
             "sous GO-2026-11-18-01", "voir M-024", "un jeu long", "deux jeux tués", "sous un addendum neuf",
             "étape non mesurée", "une session hôte", "tué après ≈ 2 h 53", "sur ≈ 15,7 h", "au bout de 49 minutes",
             "coupure à 300 secondes", "invalide une lecture", "qui coupait des chaînes", "issue ⟦mère : x⟧",
             "source 2d398c1a53073005acc4458927cb39c5"]


def auto_essai():
    sain = "  - mère : règle tenue le lendemain, trois heures après ; attendu : non écrit avant ; observé : enjeu nul, hôte refusé."
    assert garde(sain) == [], ("cas sain refusé", garde(sain))
    for art in ARTEFACTS:
        assert garde(art), f"artefact accepté : {art}"
    attendu = "  - session sœur : fait ; attendu : x (écrit avant) ; observé : non rapporté dans cette pièce."
    obtenu = ligne(SOURCE_FACTICE.split("\n")[25])
    assert obtenu == attendu, obtenu
    with tempfile.TemporaryDirectory() as d:
        src, out, cor = (os.path.join(d, n) for n in ("source.md", "piece.md", "correspondance.md"))
        # 1. cas sain : les deux fichiers sont créés, la pièce ne porte ni renvoi ni empreinte
        open(src, "w", encoding="utf-8").write(SOURCE_FACTICE)
        assert produire(src, out, cor) == 0
        p = open(out, encoding="utf-8").read()
        assert "R-" not in p.replace("R-\\d", "") and h(SOURCE_FACTICE.encode()) not in p and "2 renvois" not in p and "3 renvois" in p, p
        assert h(SOURCE_FACTICE.encode()) in open(cor, encoding="utf-8").read()
        # 2. sortie existante : refus, contenu intact
        avant = open(out, "rb").read()
        assert produire(src, out, cor + ".2") == 2 and open(out, "rb").read() == avant and not os.path.exists(cor + ".2")
        # 3. garde qui refuse : aucun fichier créé, et une sortie préexistante n'est ni vidée ni touchée
        open(src, "w", encoding="utf-8").write(SOURCE_FACTICE.replace("INSERTION", "un jeu long sous un addendum"))
        out3, cor3 = out + ".3", cor + ".3"
        try:
            produire(src, out3, cor3)
            raise AssertionError("la garde n'a pas refusé")
        except SystemExit as e:
            assert "la garde refuse" in str(e)
        assert not os.path.exists(out3) and not os.path.exists(cor3)
        open(out3, "w").write("quatorze octets")
        assert produire(src, out3, cor3) == 2 and open(out3).read() == "quatorze octets"
    print(f"auto-essai : cas sain accepté ; {len(ARTEFACTS)} artefacts refusés ; transformation conforme ; "
          "sortie existante jamais écrasée ; garde qui refuse : aucun fichier créé ni vidé")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", nargs="?", help="mémoire complète (lecture seule)")
    ap.add_argument("sortie", nargs="?", help="pièce diffusable à créer ; ne doit pas exister")
    ap.add_argument("correspondance", nargs="?", help="fichier des empreintes, pour la mère ; ne doit pas exister")
    ap.add_argument("--auto-essai", action="store_true", help="joue le cas sain et les artefacts de la garde, sans rien écrire au dépôt")
    a = ap.parse_args()
    if a.auto_essai:
        auto_essai()
    elif a.source and a.sortie and a.correspondance:
        sys.exit(produire(a.source, a.sortie, a.correspondance))
    else:
        ap.error("trois chemins attendus : source, sortie, correspondance (ou --auto-essai)")
