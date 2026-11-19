#!/usr/bin/env python3
"""Extrait d'une mémoire des problèmes la seule pièce diffusable à une session fille :
les règles de l'en-tête, puis la partition « commune », sans renvoi R-, sans date, sans heure,
sans « Comptes » ni liste des non classés. Refuse d'écrire si la garde finale trouve un renvoi,
une date, une heure ou un mot de chantier. Usage : extraire SOURCE SORTIE   |   extraire --auto-essai"""
import hashlib
import re
import sys

MOTS_INTERDITS = ["sabot", "sonde", "moniteur", "exécutante", "bras A", "lentille", "organisme", "idéation",
                  "Carbon", "Argon", "Astra", "Kimi", "Moonshot", "Bailey", "barreau", "billet", "côté ",
                  "Opus", "Sonnet", "Fable", "M-0"]
MOTIFS_INTERDITS = [r"R-\d", r"\b\d\d-\d\d\b", r"\b\d\d:\d\d", r"20\d\d-", r"GO-", r"registres/"]
PAR = re.compile(r"\s*\([^()]*(?:R-\d+|passations? 20\d\d|registres/arrets)[^()]*\)")
PREFIXE_DATE = re.compile(r"^  - (?:nuit du )?\d\d-\d\d[0-9a-zàé :Z\-]*, ")


def ligne(l):
    if l.startswith("- vu :"):
        n = len(re.findall(r"R-\d+", l)) + len(re.findall(r"20\d\d-\d\d-\d\d-\d{4}", l))
        return f"- vu : {max(n, 2)} occurrences au moins dans les registres de la session mère."
    l = re.sub(r"\(écrit avant, source[^()]*\)", "(écrit avant)", l)
    while PAR.search(l):
        l = PAR.sub("", l)
    l = PREFIXE_DATE.sub("  - ", l)
    l = re.sub(r"^- état : tenu depuis .*$", "- état : tenu", l)
    l = re.sub(r" {2,}", " ", l) if not l.startswith("  - ") else "  - " + re.sub(r" {2,}", " ", l[4:])
    l = l.replace(" ; ;", " ;").replace(" .", ".").replace(" ,", ",")
    return l


def garde(texte):
    fautes = []
    for n, l in enumerate(texte.split("\n"), 1):
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
    a = next(k for k, l in enumerate(L) if l.startswith("## Partition « commune »"))
    b = next(k for k in range(a + 1, len(L)) if L[k].startswith("---"))
    corps = [ligne(l) for l in L[a + 1:b]]
    regles = [ligne(r) for r in regles]
    regles[1] = "2. Dans la version complète, chaque fait renvoie à une ligne des registres ; ces renvois, les dates et les heures ont été retirés de cette pièce par programme."
    regles[3] = "4. Cette pièce ne porte que les problèmes qui valent pour toute session ; rien n'y dit ce qu'une autre session fait : les rôles y sont nommés sans chantier (« une session fille », « un opérateur », « un contre-lecteur »)."
    tete = ["# Mémoire des problèmes récurrents de procédure et d'outillage — partie commune, pièce diffusable",
            "",
            "Extraite par programme de la version complète tenue par la session mère (empreinte de la source : `"
            + hashlib.sha256(src.encode("utf-8")).hexdigest() + "`).",
            "Chaque problème garde ses tentatives : ce qui a été fait, ce qu'on en attendait avant, ce qui s'est passé, la parade retenue, et le signal auquel tu reconnais que tu es en train de refaire l'erreur.",
            "",
            "**Règles.**"] + regles + ["", "## Problèmes", ""]
    out = "\n".join(tete + corps).rstrip("\n") + "\n"
    f = garde(out)
    if f:
        raise SystemExit("ARRET : la garde refuse la pièce : " + "; ".join(f"ligne {n} : {m}" for n, m in f[:20]))
    return out


def auto_essai():
    sain = "  - mère : règle tenue ; attendu : non écrit avant ; observé : rien."
    assert garde(sain) == [], "cas sain refusé"
    for art in ["observé : rien (voir R-1234 ailleurs)", "le 11-18, autre chose", "à 06:25Z", "course du saboteur",
                "tenu depuis 2026-11-18", "sous GO-2026-11-18-01", "voir M-024"]:
        assert garde(art), f"artefact accepté : {art}"
    assert ligne("  - 11-14 au 11-18, session sœur : fait (R-1, R-22) ; x (écrit avant, source : note, citée par R-3) fin (passation 2026-11-18-0254).") == \
        "  - session sœur : fait ; x (écrit avant) fin.", ligne("  - 11-14 au 11-18, session sœur : fait (R-1, R-22) ; x (écrit avant, source : note, citée par R-3) fin (passation 2026-11-18-0254).")
    print("auto-essai : cas sain accepté, 7 artefacts refusés, transformation conforme")


if __name__ == "__main__":
    if sys.argv[1:] == ["--auto-essai"]:
        auto_essai()
    else:
        src = open(sys.argv[1], encoding="utf-8").read()
        open(sys.argv[2], "w", encoding="utf-8").write(extraire(src))
        print("écrit :", sys.argv[2])
