"""Contre-lecture 1 du code de T0.8 (modèle B) — script de vérification. Lecture seule : n'écrit aucun fichier.

Lancement (depuis l'arbre contre-lu, au commit 27c09264) :
    cd /home/user/t08-code-compte4-v1 && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src \
        /home/user/controle-ia-travail/.venv/bin/python \
        /home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/contre-lecture-1-code-t08-v1-calcul.py

Parties :
A. phrases gelées du brouillon 4 (tables D et F, réserves, mentions « non lu », gabarit de la phrase du point 8 bis)
   comparées, au caractère près, aux constantes du code ;
B. arithmétique du texte (bornes de Clopper et Pearson, rangs conformes) ;
C. renvois « fichier:ligne » de la table du § 1 du rapport du développeur ;
D. témoin distillé honnête : registre du texte de validité absent ; fichier de la pièce HD d'une autre forme ;
E. garde de doublon et identifiant de tâche portant une barre oblique ;
F. gardes et constantes définies mais jamais appelées ;
G. dénominateur des anomalies (question Q-8).
"""
from __future__ import annotations

import math
import re
import sys
import types
from pathlib import Path

ARBRE = Path("/home/user/t08-code-compte4-v1")
TEXTE = Path("/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md")
RAPPORT = ARBRE / "docs/notes/t08-code-compte4-v1/rapport-developpeur-t08-v1.md"
ESSAI_A = ARBRE / "essai/t08-jouet-compte4-v1/a"

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.t08 import configuration_v1 as cf  # noqa: E402
from controle_ia.t08 import donnees_v1 as dn  # noqa: E402
from controle_ia.t08 import entrees_v1 as en  # noqa: E402
from controle_ia.t08 import juges_v1 as jv  # noqa: E402
from controle_ia.t08 import rendu_juges_v1 as rj  # noqa: E402
from controle_ia.t08 import statistiques_v1 as st  # noqa: E402
from controle_ia.t08 import tables_v1 as tb  # noqa: E402
from controle_ia.t08 import temoin_distille_v1 as td  # noqa: E402
from controle_ia.t08.course_v1 import exiger_sans_doublon  # noqa: E402

texte = TEXTE.read_text(encoding="utf-8")
ecarts = 0


def titre(t: str) -> None:
    print(f"\n=== {t} ===")


def entre_guillemets(cellule: str) -> str:
    """Premier segment « … » de la cellule, guillemets imbriqués comptés ; rend l'intérieur, sans les espaces de bord."""
    i = cellule.index("«")
    prof, j = 0, i
    while j < len(cellule):
        if cellule[j] == "«":
            prof += 1
        elif cellule[j] == "»":
            prof -= 1
            if prof == 0:
                return cellule[i + 1:j].strip()
        j += 1
    raise ValueError("guillemet non fermé")


# --- A. phrases gelées ---------------------------------------------------------------------------------------------
titre("A. Phrases gelées : brouillon 4 contre code (égalité au caractère près)")
lignes_table = {}
for l in texte.splitlines():
    m = re.match(r"^\| (D[1-6]|F1b|F[1-8]) \| (.*?) \| (.*) \|$", l)
    if m:
        lignes_table[m.group(1)] = (m.group(2), m.group(3))
for code, constantes in (("D", tb.PHRASES_D), ("F", tb.PHRASES_F)):
    for cle in sorted(constantes):
        du_texte = entre_guillemets(lignes_table[cle][1])
        egal = du_texte == constantes[cle]
        ecarts += not egal
        print(f"{cle:4s} {'ÉGALE' if egal else 'DIFFÉRENTE'} ({len(du_texte)} caractères au texte, {len(constantes[cle])} au code)")
        if not egal:
            print("   texte :", du_texte)
            print("   code  :", constantes[cle])
print(f"lignes de table trouvées au texte : {sorted(lignes_table)} ; au code : D {sorted(tb.PHRASES_D)} F {sorted(tb.PHRASES_F)}")
for cle, suite in sorted(tb.SUITES_D.items()):
    dedans = suite in lignes_table[cle][1]
    ecarts += not dedans
    print(f"suite de {cle} présente telle quelle dans la cellule du texte : {dedans}")

print("-- réserves et mentions (présence, entre « », dans le brouillon 4)")
segments = set(re.findall(r"« ([^«»]+?) »", texte))
autres = {
    "RESERVES.reglage_fin": tb.RESERVES["reglage_fin"], "RESERVES.consigne": tb.RESERVES["consigne"],
    "RESERVES.mc_transfert": tb.RESERVES["mc_transfert"], "RESERVES.garde": tb.RESERVES["garde"],
    "RESERVES.echangeabilite": tb.RESERVES["echangeabilite"], "RESERVES.pas_non_lus": tb.RESERVES["pas_non_lus"],
    "RESERVES.troncature": tb.RESERVES["troncature"],
    "temoin.NON_LUE_ABSENTES": td.NON_LUE_ABSENTES, "temoin.NON_LUE_REGLES": td.NON_LUE_REGLES,
    "temoin.NON_LUE_EMPREINTE": td.NON_LUE_EMPREINTE, "temoin.NON_LUE_GARDE": td.NON_LUE_GARDE,
    "rendu.NON_LU_NON_APPLIQUEE": rj.NON_LU_NON_APPLIQUEE, "juges.IMPOSEE_TRONCATURE": jv.IMPOSEE_TRONCATURE,
    "juges.IMPOSEE_FIN (drapeau du développeur, Q-4)": jv.IMPOSEE_FIN,
}
for nom, s in autres.items():
    print(f"{nom:48s} entre guillemets : {s in segments!s:5s} ; dans le texte : {s in texte}")
print("-- chaînes du rendu des juges (présence dans le brouillon 4)")
for s in (rj.EN_TETE_QUESTIONS, "CURRENT SET (after turn t of 10):", rj.MARQUES["ADD"], rj.MARQUES["REVISE"], cf.BALISE):
    print(f"{s!r:45s} : {s in texte}")
print("en_tete_ensemble(0, 10) =", repr(rj.en_tete_ensemble(0, 10)), "; en_tete_ensemble(9, 10) =", repr(rj.en_tete_ensemble(9, 10)))

print("-- gabarit de la phrase du point 8 bis contre deux phrases de l'essai jouet (a)")
gab = next(s for s in re.findall(r"« (épisodes du témoin distillé honnête à la dose .+?) »", texte))
print("gabarit du texte :", gab)
nombre = r"(?:\d+,\d+|—)"
motif = re.escape(gab)
for marque, rx in (("<d>", r"\d(?:,\d+)?"), ("<nommé>", r"\w+"), ("<a>", nombre), ("<bas>", nombre), ("<haut>", nombre),
                   ("<état>", r"[^)]+"), ("<x>/<n>", r"\d+/\d+"), ("<y>/<n'>", r"\d+/\d+"), ("<a'>", nombre),
                   ("<état'>", r"[^)]+"), ("<x'>/<m>", r"(?:\d+|—)/(?:\d+|—)"), ("<y'>/<m'>", r"(?:\d+|—)/(?:\d+|—)")):
    assert re.escape(marque) in motif, marque
    motif = motif.replace(re.escape(marque), rx)
import json  # noqa: E402

lec = json.loads((ESSAI_A / "diag/20261113-233002-t08-lecture-jouet/lecture-t08.json").read_text(encoding="utf-8"))["resultat"]
for d in cf.DOSES:
    for s, v in lec["temoin_distille_honnete"]["doses"][d]["surveillants"].items():
        ph = v["phrase"]
        ok = re.fullmatch(motif, ph) is not None
        ok_m2 = s == "M2" and re.fullmatch(motif.replace(re.escape("aire ") + nombre + re.escape(" (") + r"[^)]+" + re.escape(")") + re.escape(", taux"),
                                                         re.escape("aire : à T0.6, taux")), ph) is not None
        print(f"{d:5s} {s:4s} conforme au gabarit : {ok or ok_m2}{' (variante « aire : à T0.6 »)' if ok_m2 and not ok else ''}")
        ecarts += not (ok or ok_m2)

# --- B. arithmétique ------------------------------------------------------------------------------------------------
titre("B. Arithmétique du texte")
from scipy import stats  # noqa: E402

for x, n, cle, attendu in ((2, 64, "haut_unilateral_95", 0.0951), (3, 64, "haut_unilateral_95", 0.1167),
                           (13, 64, "bas_unilateral_99", 0.1001), (12, 64, "bas_unilateral_99", None),
                           (2, 60, "haut_unilateral_95", 0.1012)):
    b = st.clopper_pearson(x, n)[cle]
    if cle.startswith("haut"):
        verif = stats.binom.cdf(x, n, b)          # P(X ≤ x | p = borne) doit valoir 0,05
    else:
        verif = stats.binom.sf(x - 1, n, b)       # P(X ≥ x | p = borne) doit valoir 0,01
    print(f"x = {x:2d}, n = {n} : {cle} = {b:.6f} (texte : {attendu}) ; probabilité de queue à la borne = {verif:.6f}")
for K in (256, 128, 98, 96, 2560, 1280):
    print(f"K = {K:4d} : rang conforme ⌈(K + 1) × 0,99⌉ = {math.ceil((K + 1) * 0.99 - 1e-9)}")
print("ρ*(10 ; 0,01) unilatéral =", round(cf.rho_e(), 6))

# --- C. renvois du rapport --------------------------------------------------------------------------------------------
titre("C. Renvois « fichier:ligne » de la table du § 1 du rapport du développeur (code au commit contre-lu)")
rapport = RAPPORT.read_text(encoding="utf-8")
section = rapport.split("## 1. Ce qui est fait", 1)[1].split("## 2. Fichiers neufs", 1)[0]
sources = {p.name: p.read_text(encoding="utf-8").splitlines() for p in (ARBRE / "src/controle_ia/t08").glob("*.py")}
verifies, faux = 0, []
for cellule in [l.split("|")[2] for l in section.splitlines() if l.startswith("| ") and ".py:" in l]:
    fichier = None
    for m in re.finditer(r"`(\w+\.py):(\d+)`(?: `(\w+)`)?|`(\w+)` :(\d+)|(?<![\w`]):(\d+)(?: `(\w+)`)?", cellule):
        if m.group(1):
            fichier, ligne, nom = m.group(1), int(m.group(2)), m.group(3)
        elif m.group(4):
            ligne, nom = int(m.group(5)), m.group(4)
        else:
            ligne, nom = int(m.group(6)), m.group(7)
        if fichier is None or fichier not in sources or nom is None:
            continue
        src = sources[fichier][ligne - 1] if ligne <= len(sources[fichier]) else ""
        verifies += 1
        if not re.search(rf"\b(def|class) {re.escape(nom)}\b", src):
            faux.append((fichier, ligne, nom, src.strip()[:60]))
print(f"renvois nommés vérifiés : {verifies} ; faux : {len(faux)}")
for f in faux:
    print("   ", f)

# --- D. témoin distillé honnête -----------------------------------------------------------------------------------------
titre("D. Témoin distillé honnête : ce que rend `lire_temoin_distille`")
reg = en.lire_registre_scellements(ESSAI_A / "registres-factices/scellements-v1.md")
hd_run = "20261113-233002-vadapt-hd-jouet"
entrees_hd = {
    "registre_vadapt": {"chemin": "registres-factices/validite-adaptateur-v1.md", "sha256": None, "scelle": False, "phase": "hd"},
    "index_hd": {"chemin": f"diag/{hd_run}/sorties-hd-vadapt.json", "sha256": None, "phase": "hd"},
    "mesures_hd": {"chemin": f"donnees/{hd_run}/mesures-hd.npz", "sha256": None, "phase": "hd"},
    "textes_hd": {"chemin": f"donnees/{hd_run}/textes-actions-hd.jsonl", "sha256": None, "phase": "hd"},
    "manifeste_hd": {"chemin": f"runs/{hd_run}/manifeste.json", "sha256": None, "phase": "hd"},
}


def essayer(nom: str, lb) -> None:
    faux_lecture = types.SimpleNamespace(lb=lb, config={"hd": {}}, registre=reg)
    try:
        r = td.lire_temoin_distille(faux_lecture)
        print(f"{nom} : rendu {{etat: {r['etat']!r}, motif: {r.get('motif')!r}}} (la lecture de T0.8 continuerait)")
    except GardeArret as e:
        print(f"{nom} : GardeArret non rattrapée par `lire_temoin_distille` → toute la lecture s'arrête : {str(e)[:150]}")
    except AttributeError as e:
        print(f"{nom} : contrôles de la pièce HD passés (arrêt du faux objet de lecture au-delà : {e})")


essayer("D1 cas sain (entrées de l'essai a)", en.ListeBlanche(ESSAI_A, entrees_hd))
essayer("D2 aucune entrée HD dans la configuration", en.ListeBlanche(ESSAI_A, {}))
sans_registre = {**entrees_hd, "registre_vadapt": {**entrees_hd["registre_vadapt"], "chemin": "registres-factices/registre-qui-n-existe-pas.md"}}
essayer("D3 registre du texte de validité absent du disque", en.ListeBlanche(ESSAI_A, sans_registre))


class ListeAutreForme(en.ListeBlanche):
    """Simule un `mesures-hd.npz` d'une autre forme que celle de 7b : une colonne attendue de plus que celles du fichier."""

    def lire_npz(self, nom, colonnes=en.COLONNES_MESURES):
        if nom == "mesures_hd":
            colonnes = tuple(colonnes) + ("colonne_de_plus",)
        return super().lire_npz(nom, colonnes)


essayer("D4 fichier de mesures de la pièce HD d'une autre forme", ListeAutreForme(ESSAI_A, entrees_hd))

# --- E. garde de doublon --------------------------------------------------------------------------------------------------
titre("E. Garde de doublon (première action identique à celle de l'épisode H de la même tâche)")
for ep, tache in (("etalonnage/t1/e3", "t1"), ("etalonnage/domaine/t1/e3", "domaine/t1")):
    try:
        r = exiger_sans_doublon({}, {}, {ep: "même texte"}, {tache: "même texte"})
        print(f"épisode {ep!r}, tâche {tache!r} : aucun arrêt, rendu {r}")
    except GardeArret as e:
        print(f"épisode {ep!r}, tâche {tache!r} : arrêt ({str(e)[:70]}…)")
try:
    r = exiger_sans_doublon({}, {}, {"etalonnage/t9/e0": "x"}, {"t1": "x"})
    print(f"tâche de l'épisode absente des premières actions de H : aucun arrêt, rendu {r}")
except GardeArret as e:
    print("tâche absente : arrêt", e)

# --- F. gardes et constantes jamais appelées ----------------------------------------------------------------------------
titre("F. Occurrences dans `src/controle_ia/t08/*.py` (hors la ligne de définition)")
for nom in ("refuser_hors_liste", "TACHES_EVALUATION_SHA256", "TACHES_EVALUATION\\b", "CONSIGNES_P3\\b", "EMPREINTES_ENTREES_7B",
            "exiger_code_au_commit", "exiger_instance_sans_interdits", "OBLIGATOIRES", "SURVEILLANTS_RAPPORTES",
            "EPISODES_SEUIL_MIN", "AUDIT_", "hors_ligne"):
    occ = [(f, i + 1) for f, ls in sorted(sources.items()) for i, l in enumerate(ls) if re.search(nom, l)
           and not re.match(rf"\s*(def|class) {nom}", l) and not re.match(rf"^{nom}\s*=", l) and not l.lstrip().startswith(("#", "-", "`"))]
    print(f"{nom:32s} : {len(occ)} → {occ[:8]}")
essais = {p.name: p.read_text(encoding="utf-8") for p in (ARBRE / "tests").glob("test_t08_*_v1.py")}
for nom in ("exiger_code_au_commit", "exiger_instance_sans_interdits", "refuser_hors_liste", "EMPREINTES_ENTREES_7B", "RUN_7B",
            "registre absent", "colonnes"):
    print(f"essais qui citent {nom!r} : {[f for f, t in sorted(essais.items()) if nom in t]}")

# --- G. dénominateur des anomalies ----------------------------------------------------------------------------------------
titre("G. Lisibilité : dénominateur des anomalies (Q-8)")
scores = {f"k{i}": (None, dn.REGLE) for i in range(25)}
scores.update({f"k{i}": (None, dn.ANOMALIE) for i in range(25, 33)})
scores.update({f"k{i}": (1.0, dn.LU) for i in range(33, 100)})
p = dn.parts(scores, sorted(scores))
print(f"100 actions, 25 non lues par règle, 8 anomalies : part du code = {p['part_anomalies']:.4f} (8/{p['soumises']}) ; "
      f"part sur toutes les actions = {p['anomalies'] / p['actions']:.4f} ; seuil 0,10 → "
      f"code : {'non lisible' if p['part_anomalies'] > cf.LISIBILITE_ANOMALIES_MAX else 'lisible'} ; "
      f"lettre : {'non lisible' if p['anomalies'] / p['actions'] > cf.LISIBILITE_ANOMALIES_MAX else 'lisible'}")
print("clé absente des scores, comptée par `parts` comme :", dn.parts({}, ["k-absente"]))

titre("Bilan")
print(f"écarts de phrases gelées (partie A) : {ecarts}")
sys.exit(0)
