"""Liste finie des cases et garde de completude de la grille de la clause de repli (rapport v2).

Ecrit le 2026-11-22 par l'agent de la grille (rapport v2), qui n'est redacteur d'aucune version du texte.

- lire_liste : lit la table de la section 4 de la liste finie (entrees/liste-finie-cases-grille-v1.md,
  0c62072c8fe7ea76f0d3dbe190c0f994fb1aa8c58ca793dddf60f412bf5bfb94) et la section 2 (modeles d'erreur) ; verifie
  144 cases = 8 x 3 x 2 x 3, et que chaque modele de la liste est celui des programmes (grille_commun_v2.MODELES).
- conforme_ab / conforme_c : une sortie est la premiere passe d'une case de la liste, a l'effectif fixe par le texte
  (C-P3a et C-P3b : R = 1 000, B = 1 000 ; C-P3c : R = 8 000), memes parametres, meme modele d'erreur, meme gain.
- verifier_completude (R5) : chaque case de la liste est presente une fois et une seule, par ligne et par bras
  (C-P3a et C-P3b : une sortie « ab » par case, 144 ; C-P3c bras « insertion » : 144 ; bras « contenu » : 108, non
  defini sous K16 et KH) ; toute sortie hors liste, non conforme ou en double est une erreur. Aucun repli silencieux.

Usage :
  python3 -B liste_et_garde_v2.py inventaire-v1 LISTE.md DOSSIER_SORTIES_V1 DOSSIER_ECRITURE
  python3 -B liste_et_garde_v2.py verifier LISTE.md DOSSIER_SORTIES [DOSSIER_SORTIES ...]
"""
import glob
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from grille_commun_v2 import MODELES  # noqa: E402

ATT = {"0": ("g00", 0.0), "0,10": ("g10", 0.10), "0,20": ("g20", 0.20)}
R_AB, B_AB, R_C = 1000, 1000, 8000
PROG_AB = ("grille_ab_v1.py", "grille_ab_v2.py")
PROG_C = ("grille_c_v1.py", "grille_c_v2.py")
CLE_A, CLE_B = "conj3_a", "conj3_b"
CLE_I, CLE_C = "insertion_kP3_lie|conj3", "contenu_kP3_lie|conj3"


class GardeCompletude(Exception):
    pass


def _num(x):
    return float(x.strip().replace(",", "."))


def lire_liste(chemin):
    texte = open(chemin, encoding="utf-8").read()
    # section 2 : modeles d'erreur
    modeles = {}
    for m in re.finditer(r"^\| (E30|E40|E60|EH|K16|KH|MH|M616) \| (\([^|]+\)) \| (\([^|]+\)) \| (\([^|]+\)) \|",
                         texte, re.M):
        modeles[m.group(1)] = [tuple(_num(v) for v in t.strip("() ").split(";")) for t in m.groups()[1:]]
    if sorted(modeles) != sorted(MODELES):
        raise GardeCompletude(f"modeles de la liste {sorted(modeles)} != programmes {sorted(MODELES)}")
    for nom, juges in modeles.items():
        prog = [tuple(float(v) for v in j) for j in MODELES[nom]["juges"]]
        if any(abs(a - b) > 1e-12 for ja, jb in zip(juges, prog) for a, b in zip(ja, jb)):
            raise GardeCompletude(f"modele {nom} : liste {juges} != programmes {prog}")
    # section 4 : table des cases
    cases = []
    for m in re.finditer(r"^\| (\d{3}) \| (\w+) \| ([0-9,]+) \| ([35]) \| (30|45|60) \| 1 000 ; 1 000 \| (oui|non) "
                         r"\| 8 000 \| (I ; C|I) \| (oui|non) \|", texte, re.M):
        num, mod, g, k, T, j_ab, bras, j_c = m.groups()
        att, gv = ATT[g]
        cases.append(dict(case=num, modele=mod, attaque=att, g=gv, k=int(k), T=int(T),
                          bras_c=["I", "C"] if bras == "I ; C" else ["I"], jouee_ab_v1=j_ab == "oui",
                          jouee_c_v1=j_c == "oui", juges=modeles[mod]))
    if len(cases) != 144:
        raise GardeCompletude(f"{len(cases)} cases lues, 144 attendues")
    cles = {(c["modele"], c["attaque"], c["k"], c["T"]) for c in cases}
    attendu = {(m, a, k, T) for m in MODELES for a in ("g00", "g10", "g20") for k in (3, 5) for T in (30, 45, 60)}
    if cles != attendu:
        raise GardeCompletude("la table n'est pas le produit 8 x 3 x 2 x 3")
    for c in cases:
        if (c["modele"] in ("K16", "KH")) != (c["bras_c"] == ["I"]):
            raise GardeCompletude(f"case {c['case']} : bras de C-P3c inattendus {c['bras_c']}")
    if sum(len(c["bras_c"]) == 2 for c in cases) != 108:
        raise GardeCompletude("bras « contenu » : 108 cases attendues")
    return cases


def cle(c):
    return (c["modele"], c["attaque"], c["k"], c["T"])


def _memes_juges(s, case):
    return len(s.get("juges", [])) == 3 and all(
        abs(float(a) - b) < 1e-12 for ja, jb in zip(s["juges"], case["juges"]) for a, b in zip(ja, jb))


def conforme_ab(s, case):
    """Liste des motifs de non-conformite (vide = conforme)."""
    m = []
    if s.get("programme") not in PROG_AB:
        m.append(f"programme {s.get('programme')}")
    if (s.get("modele"), s.get("attaque"), s.get("k"), s.get("T")) != cle(case):
        m.append("parametres")
    if s.get("R") != R_AB or s.get("B") != B_AB:
        m.append(f"effectif R={s.get('R')} B={s.get('B')}")
    if s.get("passe") != 0:
        m.append(f"passe {s.get('passe')}")
    if not _memes_juges(s, case):
        m.append("modele d'erreur")
    if [float(x) for x in s.get("g", [])] != [case["g"]] * 3:
        m.append("gain")
    t = s.get("taux", {})
    if t.get(CLE_A) is None or t.get(CLE_B) is None:
        m.append("taux conj3 absent")
    return m


def conforme_c(s, case):
    m = []
    if s.get("programme") not in PROG_C:
        m.append(f"programme {s.get('programme')}")
    if (s.get("modele"), s.get("attaque"), s.get("k"), s.get("T")) != cle(case):
        m.append("parametres")
    if s.get("R") != R_C:
        m.append(f"effectif R={s.get('R')}")
    if s.get("passe") != 0:
        m.append(f"passe {s.get('passe')}")
    if not _memes_juges(s, case):
        m.append("modele d'erreur")
    if [float(x) for x in s.get("g", [])] != [case["g"]] * 3:
        m.append("gain")
    t = s.get("taux", {})
    if t.get(CLE_I) is None:
        m.append("bras insertion absent")
    a_contenu = "C" in case["bras_c"]
    if a_contenu and t.get(CLE_C) is None:
        m.append("bras contenu absent")
    if (not a_contenu) and t.get(CLE_C) is not None:
        m.append("bras contenu defini la ou la liste le dit non defini")
    if bool(s.get("contenu_defini")) != a_contenu:
        m.append("contenu_defini incoherent")
    return m


def type_sortie(nom):
    b = os.path.basename(nom)
    if b.startswith("ab_"):
        return "ab"
    if b.startswith("c_"):
        return "c"
    return None


def collecter(dossiers):
    """Liste de (chemin, json) des sorties *.json de case ; verifie que le .err voisin, s'il existe, est vide."""
    out = []
    for d in dossiers:
        for p in sorted(glob.glob(os.path.join(d, "*.json"))):
            if type_sortie(p) is None:
                continue
            err = p[:-5] + ".err"
            if os.path.exists(err) and os.path.getsize(err) > 0:
                raise GardeCompletude(f"{err} non vide")
            out.append((p, json.load(open(p, encoding="utf-8"))))
    return out


def verifier_completude(cases, sorties):
    """sorties : liste de (nom, json). Renvoie le bilan ; leve GardeCompletude au premier defaut, motifs tous ecrits."""
    par_cle = {cle(c): c for c in cases}
    vus = {"ab": {}, "c": {}}
    defauts = []
    for nom, s in sorties:
        ty = type_sortie(nom)
        k = (s.get("modele"), s.get("attaque"), s.get("k"), s.get("T"))
        if ty is None:
            defauts.append(f"{nom} : type de sortie inconnu")
            continue
        if k not in par_cle:
            defauts.append(f"{nom} : case hors liste {k}")
            continue
        motifs = (conforme_ab if ty == "ab" else conforme_c)(s, par_cle[k])
        if motifs:
            defauts.append(f"{nom} : non conforme ({', '.join(motifs)})")
            continue
        vus[ty].setdefault(k, []).append(nom)
    bilan = {}
    for ligne, ty, filtre in (("C-P3a et C-P3b", "ab", lambda c: True), ("C-P3c insertion", "c", lambda c: True),
                              ("C-P3c contenu", "c", lambda c: "C" in c["bras_c"])):
        attendues = [c for c in cases if filtre(c)]
        manq = [c["case"] for c in attendues if cle(c) not in vus[ty]]
        doubles = [c["case"] for c in attendues if len(vus[ty].get(cle(c), [])) > 1]
        couvertes = len(attendues) - len(manq)
        bilan[ligne] = dict(couvertes=couvertes, liste=len(attendues), manquantes=manq, doubles=doubles)
        if manq:
            defauts.append(f"{ligne} : {len(manq)} case(s) manquante(s) : {', '.join(manq)}")
        if doubles:
            defauts.append(f"{ligne} : case(s) en double : {', '.join(doubles)}")
    if defauts:
        raise GardeCompletude("GARDE DE COMPLETUDE : ECHEC\n" + "\n".join(defauts))
    return bilan


def inventaire_v1(liste, dossier_v1, ecriture):
    """Classe les sorties de passe 0 de v1 : reprises (conformes a une case de la liste) ou non ; ecrit les listes des
    cases a jouer (format du lanceur : MODELE ATTAQUE k T)."""
    cases = lire_liste(liste)
    par_cle = {cle(c): c for c in cases}
    reprises = {"ab": {}, "c": {}}
    lignes = []
    for p in sorted(glob.glob(os.path.join(dossier_v1, "*_p0.json"))):
        ty = type_sortie(p)
        s = json.load(open(p, encoding="utf-8"))
        k = (s.get("modele"), s.get("attaque"), s.get("k"), s.get("T"))
        if k not in par_cle:
            lignes.append(f"hors liste : {os.path.basename(p)}")
            continue
        err = p[:-5] + ".err"
        if os.path.exists(err) and os.path.getsize(err) > 0:
            lignes.append(f"erreur non vide, non reprise : {os.path.basename(p)}")
            continue
        motifs = (conforme_ab if ty == "ab" else conforme_c)(s, par_cle[k])
        if motifs:
            lignes.append(f"non conforme, non reprise : {os.path.basename(p)} ({', '.join(motifs)})")
            continue
        reprises[ty][k] = p
    a_jouer = {ty: [c for c in cases if cle(c) not in reprises[ty]] for ty in ("ab", "c")}
    for ty in ("ab", "c"):
        with open(os.path.join(ecriture, f"cases_{ty}_a_jouer_v2.txt"), "w", encoding="utf-8") as f:
            for c in a_jouer[ty]:
                f.write(f"{c['modele']} {c['attaque']} {c['k']} {c['T']}\n")
        with open(os.path.join(ecriture, f"reprises_{ty}_v1.txt"), "w", encoding="utf-8") as f:
            for k_ in sorted(reprises[ty], key=lambda x: par_cle[x]["case"]):
                f.write(f"{par_cle[k_]['case']} {os.path.basename(reprises[ty][k_])}\n")
    # concordance avec les colonnes « jouee » de la liste (d'apres le rapport v1)
    for ty, col in (("ab", "jouee_ab_v1"), ("c", "jouee_c_v1")):
        diff = [c["case"] for c in cases if c[col] != (cle(c) in reprises[ty])]
        lignes.append(f"{ty} : reprises {len(reprises[ty])}, a jouer {len(a_jouer[ty])}, "
                      f"ecart a la colonne « jouee » de la liste : {diff if diff else 'aucun'}")
        lignes.append(f"{ty} : a jouer = " + " ".join(c["case"] for c in a_jouer[ty]))
    print("\n".join(lignes))
    return reprises, a_jouer


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "inventaire-v1":
        inventaire_v1(sys.argv[2], sys.argv[3], sys.argv[4])
        return 0
    if len(sys.argv) >= 2 and sys.argv[1] == "verifier":
        cases = lire_liste(sys.argv[2])
        try:
            bilan = verifier_completude(cases, collecter(sys.argv[3:]))
        except GardeCompletude as e:
            print(str(e))
            return 1
        print("GARDE DE COMPLETUDE : SAINE")
        for ligne, b in bilan.items():
            print(f"  {ligne} : {b['couvertes']} / {b['liste']}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
