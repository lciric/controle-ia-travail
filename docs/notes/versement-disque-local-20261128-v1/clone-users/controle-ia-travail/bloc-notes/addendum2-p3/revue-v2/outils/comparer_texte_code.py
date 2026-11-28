"""Comparaisons mécaniques du brouillon 4 au module v2 (copie de base) : table « Entrées », phrases de la table des
critères, liste fermée des 47 clés, constantes chiffrées du texte. Lit seulement le texte et le module (aucune donnée).

Usage : python comparer_texte_code.py <texte> <module>
"""
import importlib.util
import re
import sys
from pathlib import Path

import garde_r1_v2  # noqa: F401

texte = Path(sys.argv[1]).read_text(encoding="utf-8")
spec = importlib.util.spec_from_file_location("av_base", sys.argv[2])
av = importlib.util.module_from_spec(spec)
spec.loader.exec_module(av)
ecarts = []

# 1. table « Entrées »
entrees = dict(re.findall(r"^\| \[(\w+)\] \| `([^`]+)`[^|]*\| `([0-9a-f]{64})` \|$", texte, flags=re.M) and
               [(e, (c, s)) for e, c, s in re.findall(r"^\| \[(\w+)\] \| `([^`]+)`[^|]*\| `([0-9a-f]{64})` \|$", texte,
                                                      flags=re.M)])
attendues = {k: v for k, v in entrees.items() if k in ("MR", "R", "SF", "E", "S", "J", "T", "L", "ML")}
print("entrées du texte :", sorted(attendues))
if attendues != av.ENTREES:
    ecarts.append(f"ENTREES : texte {attendues} ≠ module {av.ENTREES}")
for cle in ("A", "MA"):
    if cle in av.ENTREES:
        ecarts.append(f"[{cle}] lue par le module alors que le texte la dit « citée, non lue »")

# 2. phrases de la table des critères (cellule de droite), comparées aux phrases du module remplies de marqueurs
cellules = re.findall(r"^\| `?([^|`]+)`?(?: vrai)? \| (.+) \|$", texte.split("## Critères de lecture gelés")[1].split("- **Verrou")[0],
                      flags=re.M)
table = {g.strip(): d for g, d in cellules}


def guillemets(s):
    return re.findall(r"« ((?:[^«»]|«[^«»]*»)*) »", s)


module = {
    av.R_HORS_FORMES: [av.LECTURES[av.R_HORS_FORMES]],
    av.R_PORTEE: [av.LECTURES[av.R_PORTEE].format(part="part `D`, intervalle")],
    av.R_AU_DELA: [av.LECTURES[av.R_AU_DELA].format(borne="borne basse de `E_sf`")],
    av.R_NON_RESOLUE: [av.LECTURES[av.R_NON_RESOLUE]],
    av.R_MEDIANE: [av.LECTURES[av.R_MEDIANE]],
    av.R_TEMOIN: [av.LECTURES[(av.R_TEMOIN, "P3-P1")], av.LECTURES[(av.R_TEMOIN, "P3-P4")]],
    av.R_MENTION: [av.LECTURES[(av.R_MENTION, "P3-P1")], av.LECTURES[(av.R_MENTION, "T3")]],
    av.R_PUISSANCE: [av.LECTURES[av.R_PUISSANCE].format(p="`<p>`", a80="`A_80(p)`", ecrit="`A_80_écrit_max`")],
    "reserve_<analyse>_non_lue": [av.LECTURE_NON_LUE],
    "aucune réserve sur une conclusion établie": [av.LECTURE_AUCUNE],
    "audit_symetrie_addendum2.declencheur": [av.LECTURE_AUDIT],
    "arrêt de l'addendum 2 (liste d'arrêt)": [av.LECTURE_ARRET],
}
for nom, phrases in module.items():
    ligne = next((d for g, d in table.items() if g.startswith(nom)), None)
    if ligne is None:
        ecarts.append(f"ligne de la table des critères introuvable : {nom}")
        continue
    du_texte = guillemets(ligne)
    for p in phrases:
        if nom == "arrêt de l'addendum 2 (liste d'arrêt)":
            ok = p == ligne.strip()
        elif nom == "audit_symetrie_addendum2.declencheur":
            ok = ligne.strip() == f"« {p} » ; {av.CONSIGNE_AUDIT}"
        elif nom == "aucune réserve sur une conclusion établie":
            ok = ligne.strip() == "rien n'est ajouté ; « contrôles de l'addendum 2 passés », jamais « robuste » au-delà" \
                 and p == ligne.strip()
        else:
            ok = p in du_texte
        print(f"{'=' if ok else 'ÉCART'} {nom} : {p[:70]}…")
        if not ok:
            ecarts.append(f"phrase de {nom} : module {p!r} ; texte {du_texte}")
consigne = table.get("`audit_symetrie_addendum2.declencheur` vrai") or next(
    (d for g, d in table.items() if g.startswith("audit_symetrie_addendum2.declencheur")), "")
print("ligne de l'audit (texte) :", consigne, "| module : lecture", repr(av.LECTURE_AUDIT), "consigne",
      repr(av.CONSIGNE_AUDIT))

# 3. liste fermée des 47 clés, reconstruite depuis le texte
objets = re.search(r"`<objet>` parmi (.+?) \(27 clés\)", texte, flags=re.S).group(1)
objets = re.findall(r"`([a-z_\-]+)`", objets)
contrastes = re.findall(r"`addendum2/(B[12]/[a-z]+-honnete)/<objet>`", texte)
conditions = ("honnete", "saboteur", "temoin", "mention")
formes = re.findall(r"`(cout_[a-z_]+)`", texte.split("**M2")[0].split("Colonnes de [S] lues")[1].split("pour la garde 7")[0])
cles = [f"addendum2/{c}/{o}" for c in contrastes for o in objets] + [f"addendum2/ecart/{c}/{f}" for c in conditions
                                                                      for f in formes]
print("clés reconstruites :", len(cles), "objets", objets, "formes", formes)
if cles != av.cles_addendum2():
    ecarts.append(f"clés : texte {cles} ≠ module {av.cles_addendum2()}")

# 4. constantes chiffrées
z, z80 = av.quantiles_normaux()
for nom, a, b, tol in (("log10 3", av.LOG10_3, 0.47712125471966244, 0), ("z", z, 2.2414027276049464, 1e-12),
                       ("z80", z80, 0.8416212335729144, 1e-12), ("A_80_écrit_max", 0.53 + 0.037 * (1 + z80 / z), 0.5809, 5e-5),
                       ("A_80_écrit_min", 0.52 + 0.025 * (1 + z80 / z), 0.5544, 5e-5)):
    ok = abs(a - b) <= tol
    print(f"{'=' if ok else 'ÉCART'} {nom} : module {a!r}, texte {b!r}")
    if not ok:
        ecarts.append(f"{nom} : {a} ≠ {b}")
print("PARAMETRES_DU_TEXTE :", av.PARAMETRES_DU_TEXTE, "| CONSTANTES_LECTURE :", av.CONSTANTES_LECTURE)
print("ÉCARTS :", ecarts or "aucun")
