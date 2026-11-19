#!/usr/bin/env python3
"""Barreau 5 : fabrique du brouillon 4 du texte et de son devis, à partir du brouillon 3 (v1).

Écrit par le rédacteur (Claude Fable 5.2), dans la nuit du 19 au 20 novembre 2026. Aucune donnée du programme.
Méthode (la même que pour le brouillon 3, où les couples avaient été appliqués par programme) :
  1. les 15 couples « toujours » de la vérification du brouillon 3, à la lettre, dans leur ordre ;
  2. les 39 couples du code (`couples-du-code-pour-brouillon4-v1.md`, groupes 1 et 2), à la lettre, dans leur ordre,
     sauf trois « après » remplacés par les choix du brouillon 4 (C-2e, C-4a, C-6a) ;
  3. les écritures du rédacteur pour la voie (iii) : sections récrites en entier, et retouches exactes.
Chaque « avant » doit se trouver une seule fois au moment où il s'applique ; sinon le programme s'arrête sans rien écrire.
Les nombres de mondes inventés cités dans les sections récrites sont lus dans les sorties des simulations, non recopiés.
Sorties : le texte et le devis du brouillon 4 (refus d'écraser), et un compte rendu sur la sortie standard.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import runpy
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
T3 = os.path.join(RACINE, "prereg", "barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md")
T4 = os.path.join(RACINE, "prereg", "barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md")
DV3 = os.path.join(ICI, "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md")
DV4 = os.path.join(ICI, "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md")
sys.path.insert(0, ICI)
import sections_brouillon4_v1 as S                                     # noqa: E402  (textes des sections récrites)

RAPPORT = []


def dire(x):
    RAPPORT.append(x)
    print(x)


def une_fois(t, avant, apres, nom):
    n = t.count(avant)
    if n != 1:
        raise SystemExit(f"ARRÊT : {nom} : « avant » trouvé {n} fois : {avant[:90]!r}")
    return t.replace(avant, apres)


def bloc(t, debut, fin, nouveau, nom):
    """Remplace ce qui va de `debut` (compris) à `fin` (non compris)."""
    if t.count(debut) != 1:
        raise SystemExit(f"ARRÊT : {nom} : début trouvé {t.count(debut)} fois")
    i = t.index(debut)
    j = t.index(fin, i + len(debut))
    return t[:i] + nouveau + t[j:]


def ligne(t, prefixe, nouvelle, nom, ajouter=False):
    """Remplace (ou fait suivre, si `ajouter`) la seule ligne qui commence par `prefixe`."""
    lignes = t.split("\n")
    idx = [i for i, l in enumerate(lignes) if l.startswith(prefixe)]
    if len(idx) != 1:
        raise SystemExit(f"ARRÊT : {nom} : {len(idx)} lignes commencent par {prefixe!r}")
    lignes[idx[0]] = (lignes[idx[0]] + "\n" + nouvelle) if ajouter else nouvelle
    return "\n".join(lignes)


def fr(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


def chiffres():
    """Nombres des mondes inventés, lus dans les sorties (jamais recopiés à la main)."""
    b = json.load(open(os.path.join(ICI, "sortie-simulation-brouillon4-regle-d-issue-v1.json"), encoding="utf-8"))["cases"]
    c20 = json.load(open(os.path.join(ICI, "sortie-controle-precision-fiche-v-b1-v1.json"), encoding="utf-8"))["cases"]
    noms = sorted({k.split("/")[0] for k in b})

    def v(nom, champ="mot_sabotage_99_ou_95", ka=3, kt=10):
        out = []
        for p in (1024, 4096):
            r = b[f"{nom}/p_{p}/app_{ka}/test_{kt}"]
            out.append(r[champ] if champ in r else r["issues"][champ])
        return out

    def deux(nom, **kw):
        a = v(nom, **kw)
        return fr(a[0]) if a[0] == a[1] else f"{fr(a[0])} ; {fr(a[1])}"

    sans = [n for n in noms if n[0] in "ABC" and "RIVALE" not in n and "kappa" not in n]
    nuls = [n for n in noms if n[:3] in ("A01", "A02", "A03", "B06", "C20")]
    force = [n for n in noms if n[:3] in ("A06", "A07", "A08", "A09", "A10", "A11", "A12", "A13", "B01", "B03", "B05",
                                          "B07", "B08", "B09", "B10", "B11")]
    etend = lambda L, champ: (min(min(v(n, champ)) for n in L), max(max(v(n, champ)) for n in L))
    pc = lambda x: fr(100 * x, 1)
    d = {"n_sans": len(sans), "max_mot": pc(max(max(v(n)) for n in sans)),
         "n_hauts": sum(max(v(n)) > 0.005 for n in sans),
         "c20_min": fr(100 * min(r["mot_sabotage_99_ou_95"] for r in c20.values())),
         "c20_max": fr(100 * max(r["mot_sabotage_99_ou_95"] for r in c20.values())), "c20_n": len(c20),
         "nul_D": " à ".join(pc(x) for x in etend(nuls, "D")), "nul_C": " à ".join(pc(x) for x in etend(nuls, "C")),
         "nul_E": " à ".join(pc(x) for x in etend(nuls, "E")), "force_D": " à ".join(pc(x) for x in etend(force, "D")),
         "rivale_forte": pc(min(v("A15_trace_propre_a_son_sens_0.3_RIVALE_OUVERTE"))),
         "rivale_faible": " et ".join(pc(x) for x in v("A16_trace_propre_a_son_sens_0.1_RIVALE_OUVERTE")),
         "kappa": " à ".join(pc(x) for x in etend([n for n in noms if n[:3] in ("C21", "C22", "C34")], "mot_sabotage_99_ou_95")),
         "mixte": pc(max(max(v(n)) for n in noms if n[:3] in ("B09", "B10")))}
    lignes = []
    for nom, titre in (("D01_sabotage_0.1_gradue", "sabotage 0,1, réponse graduée"),
                       ("D02_sabotage_0.2_gradue", "sabotage 0,2, réponse graduée"),
                       ("D03_sabotage_0.1_sature", "sabotage 0,1, réponse saturée"),
                       ("D04_sabotage_0.2_gradue_rE_1.0", "sabotage 0,2 gradué, grande divergence propre"),
                       ("D05_sabotage_0.1_gradue_force_0.2", "sabotage 0,1 gradué et force 0,2"),
                       ("D06_sabotage_0.2_gradue_force_0.2", "sabotage 0,2 gradué et force 0,2"),
                       ("D08_sabotage_0.2_gradue_trace_symetrique_0.1", "sabotage 0,2 gradué et trace commune 0,1")):
        lignes.append(f"| {titre} | {deux(nom)} | {deux(nom, kt=9)} | {deux(nom, kt=8)} | {deux(nom, ka=2)} |")
    d["table_puissance"] = "\n".join(lignes)
    sat = "D03_sabotage_0.1_sature"
    d["sat_mot"], d["sat_E"], d["sat_D"] = deux(sat), deux(sat, champ="E"), deux(sat, champ="D")
    d["app2_petit"] = deux("D01_sabotage_0.1_gradue", ka=2)
    d["app3_petit"] = deux("D01_sabotage_0.1_gradue")
    return d


def couples_du_verificateur():
    m = runpy.run_path(os.path.join(ICI, "contre-lecture-outils-plan-brouillon3-v1", "couples-verification-brouillon3-v1.py"),
                       run_name="verificateur")
    return [(c[0], c[2], c[4], c[5]) for c in m["COUPLES"]]


MOTIF = re.compile(r"#### Couple (?P<nom>[CD]-\d+[a-z]) — (?P<piece>T|DV) — [^\n]*\n\nAvant :\n\n```text\n(?P<avant>.*?)\n```\n\n"
                   r"Après :\n\n```text\n(?P<apres>.*?)\n```\n", re.S)


def main():
    for chemin in (T4, DV4):
        if os.path.exists(chemin):
            raise SystemExit(f"ARRÊT : {chemin} existe déjà (on n'écrase jamais)")
    t = open(T3, encoding="utf-8").read()
    dv = open(DV3, encoding="utf-8").read()
    assert hashlib.sha256(t.encode()).hexdigest().startswith("525f338e"), "brouillon 3 : empreinte inattendue"
    assert hashlib.sha256(dv.encode()).hexdigest().startswith("7ac56a7b"), "devis du brouillon 3 : empreinte inattendue"
    C = chiffres()

    # ---------------------------------------------------------------- 1. couples « toujours » du vérificateur
    verif = couples_du_verificateur()
    for nom, groupe, avant, apres in verif:
        if groupe == "toujours":
            t = une_fois(t, avant, apres, nom)
    dire(f"couples « toujours » du vérificateur appliqués : {sum(g == 'toujours' for _, g, _, _ in verif)} ; "
         f"couples « voie i » non appliqués (sans objet sous la voie (iii)) : {sum(g != 'toujours' for _, g, _, _ in verif)}")

    # ---------------------------------------------------------------- 2. couples du code
    source = open(os.path.join(ICI, "couples-du-code-pour-brouillon4-v1.md"), encoding="utf-8").read()
    code = [(m["nom"], m["piece"], m["avant"], m["apres"]) for m in MOTIF.finditer(source)]
    assert len(code) == 39, len(code)
    for nom, piece, avant, apres in code:
        apres = S.REMPLACES.get(nom, apres)
        if piece == "T":
            t = une_fois(t, avant, apres, nom)
        else:
            dv = une_fois(dv, avant, apres, nom)
    dire(f"couples du code appliqués : {len(code)} ; « après » remplacés par un choix du brouillon 4 : {sorted(S.REMPLACES)}")

    # ---------------------------------------------------------------- 3. voie (iii) et le reste : le texte
    for nom, avant, apres in S.RETOUCHES_TEXTE:
        t = une_fois(t, avant, apres, nom)
    for nom, prefixe, nouvelle, ajouter in S.LIGNES_TEXTE:
        t = ligne(t, prefixe, nouvelle, nom, ajouter)
    for nom, debut, fin, nouveau in S.BLOCS_TEXTE:
        t = bloc(t, debut, fin, nouveau.format(**C) if nom in S.BLOCS_A_CHIFFRES else nouveau, nom)
    dire(f"retouches exactes du texte : {len(S.RETOUCHES_TEXTE)} ; lignes : {len(S.LIGNES_TEXTE)} ; sections récrites : {len(S.BLOCS_TEXTE)}")

    # ---------------------------------------------------------------- 3 bis. le devis
    for nom, avant, apres in S.RETOUCHES_DEVIS:
        dv = une_fois(dv, avant, apres, nom)
    dire(f"retouches exactes du devis : {len(S.RETOUCHES_DEVIS)}")

    # ---------------------------------------------------------------- contrôles
    pieces = {"T": t, "DV": dv}
    for nom, groupe, avant, apres in verif:
        if groupe == "toujours":
            dire(f"  {nom:6s} « après » présent à l'octet dans le texte final : {'oui' if t.count(apres) == 1 else 'non'}")
    for nom, piece, avant, apres in code:
        dire(f"  {nom:6s} {piece:2s} « après » du couple présent à l'octet : {'oui' if pieces[piece].count(apres) == 1 else 'non'}")
    for mot in S.RESTES_INTERDITS:
        n = t.count(mot)
        dire(f"  reste « {mot} » dans le texte : {n} fois")
    dire(f"  marques « [à confirmer par le rapport v4] » : texte {t.count('[à confirmer par le rapport v4]')}, devis {dv.count('[à confirmer par le rapport v4]')}")
    open(T4, "x", encoding="utf-8").write(t)
    open(DV4, "x", encoding="utf-8").write(dv)
    dire(f"écrit : texte {len(t)} signes, {hashlib.sha256(t.encode()).hexdigest()} ; devis {len(dv)} signes, {hashlib.sha256(dv.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
