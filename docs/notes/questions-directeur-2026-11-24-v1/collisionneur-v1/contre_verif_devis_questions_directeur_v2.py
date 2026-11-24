"""Contre-vérification du devis du collisionneur, dossier des questions du directeur du 24 novembre (v2).

v2 : copie de contre_verif_devis_questions_directeur_v1.py (68d4cb2e…, inchangé, R12). Changements, et seulement ceux-là :
  (a) comptes de jetons repris de verif_devis_questions_directeur_v5.py (question groupée v5, question témoin v2,
      faits v1) ;
  (b) pointe parallèle recalculée ici comparée à celle du script v5 (pointe_par), et plafond parallèle à plafond_par ;
  (c) section 4 : aucun devis écrit ne porte encore la v5 ; les tableaux du devis v2 (question v2) sont lus et leur
      écart au calcul v5 est rapporté pour information, sans compter comme échec.

Pièce de travail (classe C), écrite par un vérificateur neuf qui n'a rien écrit du devis. Aucun appel réseau, aucune
écriture sur disque. Ce script ne recopie pas les formules de coût du brouillon : il reprend du script du brouillon
(verif_devis_questions_directeur_v1.py) les seuls comptes de jetons par cellule (entrée attendue et maximale, garde
d'entrée, sorties médiane et 90e centile), puis :
  (1) relit les tarifs sur les pages publiques relevées le 24 novembre 2026 (sous-dossier releve-sources-…) et sur la
      page d'Anthropic versée le 22 novembre (même empreinte que la page relevée le 24) ; compare aux prix du moteur ;
  (2) recalcule attendu, haut et pire de chaque cellule avec ces tarifs et compare au brouillon ;
  (3) contrôle les réglages de Google par une règle écrite ici (réflexion explicite au niveau le plus haut admis,
      jamais budget et niveau ensemble ; plafond >= provision + 16 000 ; limite de mots x jetons par mot <= plafond -
      provision ; plafond <= limite du mode), sur le corps produit par le moteur, au premier envoi et à la relance ;
      l'épreuve sur cas sain et sur artefacts (règle R5) vaut pour cette règle ET pour la garde commune v3 ;
  (4) refait le chemin séquentiel des envois et sa pointe, puis calcule la pointe en envoi parallèle (les trois
      cellules d'un tour partent ensemble ; la relance d'une cellule coupée part seule après le lot), et le plafond
      selon la même règle (pointe + deux coupures de Carbon de plus, arrondi à l'entier supérieur).
Lancement : PYTHONDONTWRITEBYTECODE=1 python3 -I contre_verif_devis_questions_directeur_v2.py
"""
import copy
import hashlib
import json
import math
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[3]
sys.path.insert(0, str(ICI))
import verif_devis_questions_directeur_v5 as vd  # noqa: E402  (importe aussi le moteur et la garde v3)

col, g3 = vd.col, vd.g3
SOURCES = ICI / "releve-sources-tarifs-20261124T1719Z-v1"
PAGE_GOOGLE = SOURCES / "page-prix-gemini-api-20261124T171900Z.md.txt"
PAGES_MODELES = {"carbon": SOURCES / "page-modele-gemini-4-carbon-20261124T172051Z.md.txt",
                 "neon": SOURCES / "page-modele-gemini-4-neon-20261124T172051Z.md.txt"}
PAGE_ANTHROPIC = DEPOT / "docs" / "sources" / "prix" / "page-prix-anthropic-docs-20261122T104128Z.md"
PAGE_REFLEXION = DEPOT / "docs" / "sources" / "google-gemini-reflexion-v1" / "gemini-thinking-generate-content-2026-11-21-v1.md.txt"
TEXTE_MIN = 16000
ESP = ["opus", "carbon", "neon"]
OK = True


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def verifier(cond, msg):
    global OK
    OK &= bool(cond)
    print(("  ok    " if cond else "  ÉCART ") + msg)


def prix_google(texte, titre):
    """Prix « Standard » (entrée, sortie) d'une section de la page : liste des montants trouvés dans chaque case."""
    debut = texte.index(f"## {titre}")
    std = texte.index('{% tab title="Standard" %}', debut)
    fin = texte.index("{% /tab %}", std)
    bloc = texte[std:fin]

    def montants(etiquette):
        i = bloc.index(etiquette)
        j = bloc.index("---", i)
        return [float(x) for x in re.findall(r"\$(\d+(?:\.\d+)?)", bloc[i:j])]
    return montants("* Input price"), montants("* Output price (including thinking tokens)")


def prix_anthropic(texte, modele):
    ligne = next(l for l in texte.splitlines() if l.startswith(f"| {modele} |"))
    cases = [c.strip() for c in ligne.strip("|").split("|")]
    val = lambda c: float(re.match(r"\$(\d+(?:\.\d+)?)", c).group(1))  # noqa: E731
    return val(cases[1]), val(cases[5])


def niveaux_admis(texte):
    ligne = next(l for l in texte.splitlines() if "Gemini 4 Carbon and Argon (`gemini-4-carbon`" in l)
    carbon = re.search(r"support `low`, `medium` \(default\), and `high`", ligne)
    neon = re.search(r"`gemini-4-hydrogen`\) support `low`, `medium`, `high` \(default\), and `xhigh`", ligne)
    return {"carbon": "high" if carbon else None, "neon": "xhigh" if neon else None}


def controle_reglages(espece, corps, provision, mots, jpm, limite, niveau_max):
    """Règle de CLAUDE.md (« Appels aux modèles de Google »), écrite ici sans la garde commune."""
    pb = []
    gc = corps.get("generationConfig", {})
    tc = gc.get("thinkingConfig", {})
    plafond = gc.get("maxOutputTokens")
    if "thinkingLevel" not in tc and "thinkingBudget" not in tc:
        pb.append("réflexion non explicite")
    if "thinkingLevel" in tc and "thinkingBudget" in tc:
        pb.append("niveau et budget ensemble (refus 400 chez Gemini 4)")
    if "thinkingLevel" in tc and tc["thinkingLevel"] != niveau_max:
        pb.append(f"niveau {tc['thinkingLevel']} sous le plus haut admis {niveau_max}")
    if not isinstance(plafond, int):
        pb.append("plafond absent")
        return pb
    if plafond < provision + TEXTE_MIN:
        pb.append(f"plafond {plafond} < réflexion {provision} + {TEXTE_MIN}")
    if math.ceil(mots * jpm) > plafond - provision:
        pb.append(f"limite de mots {mots} x {jpm} > texte {plafond - provision}")
    if plafond > limite:
        pb.append(f"plafond {plafond} > limite du mode {limite}")
    return pb


def chemin(rangs, gratuit, paralleles, coupures):
    """Chemin haut à coupures : renvoie (dépense finale, pointe, lieu). Une cellule coupée est comptée au pire, puis
    relancée seule au haut ; la marge exigée d'un envoi est son pire (ou la marge du kit d'Opus par l'abonnement)."""
    depense, pointe, ou = 0.0, 0.0, None
    tours = {}
    for c in rangs:
        tours.setdefault(c["cid"][:5], []).append(c)
    for tour, cells in tours.items():
        lots = [[c] for c in cells] if not paralleles else [cells]
        for lot in lots:
            marge = sum(c["marge_kit"] if gratuit(c) else c["pire"] for c in lot)
            if depense + marge > pointe:
                pointe, ou = depense + marge, "+".join(c["cid"] for c in lot)
            for c in lot:
                depense += c["pire"] if c["cid"] in coupures else (0.0 if gratuit(c) else c["haut"])
            for c in lot:  # relances des cellules coupées, une à une, après le lot
                if c["cid"] in coupures:
                    if depense + c["pire_rel"] > pointe:
                        pointe, ou = depense + c["pire_rel"], f"{c['cid']} relance"
                    depense += c["haut"]
    return depense, pointe, ou


def main():
    print(f"moteur {col.VERSION} {sha(col.__file__)} ; garde v3 {sha(g3.__file__)} ; script du brouillon "
          f"{sha(vd.__file__)}")
    print("=== 1. Tarifs relus à la source ===")
    for p in [PAGE_GOOGLE, *PAGES_MODELES.values(), PAGE_ANTHROPIC, PAGE_REFLEXION]:
        print(f"  {p.name} sha256={sha(p)}")
    tg = PAGE_GOOGLE.read_text(encoding="utf-8")
    pc = prix_google(tg, "Gemini 4 Carbon")
    pn = prix_google(tg, "Gemini 4 Neon")
    po = prix_anthropic(PAGE_ANTHROPIC.read_text(encoding="utf-8"), "Claude Opus 5.5")
    print(f"  Carbon, Standard : entrée {pc[0]}, sortie {pc[1]} ; Neon : {pn[0]}, {pn[1]} ; Opus 5.5 : {po}")
    col.fixer_composition(ESP, nom_cle_anthropic="CLE_FICTIVE")
    prix_moteur = {col.MODELES[l]["espece"]: col.MODELES[l]["prix"] for l in col.LETTRES}
    verifier(prix_moteur["carbon"] == (max(pc[0]), max(pc[1])), f"Carbon au barème haut {prix_moteur['carbon']}")
    verifier(pc == ([2.0, 4.0], [10.0, 20.0]), "Carbon facturé 2 / 10 jusqu'au 30 novembre, 4 / 20 dès le 1er décembre")
    verifier(prix_moteur["neon"] == (pn[0][0], pn[1][0]) and len(pn[0]) == len(pn[1]) == 1, f"Neon {prix_moteur['neon']}")
    verifier(prix_moteur["opus"] == po, f"Opus 5.5 {prix_moteur['opus']}")
    for esp, p in PAGES_MODELES.items():
        t = p.read_text(encoding="utf-8")
        verifier("**Max output** 65,536 (default synchronous)" in t, f"{esp} : sortie maximale 65 536 (page du modèle)")
    print("=== 2. Réglages de Google : règle écrite ici, et garde commune v3 ===")
    niv = niveaux_admis(PAGE_REFLEXION.read_text(encoding="utf-8"))
    print(f"  niveaux les plus hauts admis (page de réflexion) : {niv}")
    for l in col.LETTRES:
        m = col.MODELES[l]
        if m["fournisseur"] != "gemini":
            continue
        esp, jpm = m["espece"], g3.JETONS_PAR_MOT_MESURES[m["espece"]]
        lim = g3.LIMITES_SORTIE[esp]["flux"]
        for tour in col.ORDRE_ETAGE[3]:
            mots = col.TOURS[tour]["mots"]
            for quoi, plaf in (("premier envoi", m["max"]), ("relance", m["max_relance"])):
                corps = col.demande_gemini(m, "essai", plaf)
                ici = controle_reglages(esp, corps, m["provision"], mots, jpm, lim, niv[esp])
                v3 = g3.verifier_reglages_google(esp, corps, m["provision"], mots=mots, mode="flux")
                marge = plaf - m["provision"] - math.ceil(mots * jpm)
                verifier(not ici and not v3, f"{esp} {tour} {quoi} : plafond {plaf}, provision {m['provision']}, "
                                             f"texte {plaf - m['provision']}, mots {mots} -> {math.ceil(mots * jpm)}"
                                             f" jetons, marge {marge} ; règle ici {ici} ; v3 {v3}")
        # épreuve sur artefacts (règle R5) : chaque mutation doit être refusée par la règle ici ET par la garde v3
        sain = col.demande_gemini(m, "essai", m["max"])
        mutations = {}
        c = copy.deepcopy(sain); del c["generationConfig"]["thinkingConfig"]["thinkingLevel"]; mutations["sans réglage de réflexion"] = (c, 3500)  # noqa: E702,E501
        c = copy.deepcopy(sain); c["generationConfig"]["thinkingConfig"]["thinkingBudget"] = m["provision"]; mutations["budget et niveau ensemble"] = (c, 3500)  # noqa: E702,E501
        c = copy.deepcopy(sain); c["generationConfig"]["maxOutputTokens"] = m["provision"] + TEXTE_MIN - 1; mutations["plafond sous réflexion + 16 000"] = (c, 3000)  # noqa: E702,E501
        c = copy.deepcopy(sain); mutations["limite de mots trop longue"] = (c, math.floor((m["max"] - m["provision"]) / jpm) + 50)  # noqa: E702,E501
        c = copy.deepcopy(sain); c["generationConfig"]["thinkingConfig"]["thinkingLevel"] = "medium"; mutations["niveau sous le plus haut"] = (c, 3500)  # noqa: E702,E501
        for nom, (corps, mots) in mutations.items():
            ici = controle_reglages(esp, corps, m["provision"], mots, jpm, lim, niv[esp])
            try:
                v3 = g3.verifier_reglages_google(esp, corps, m["provision"], mots=mots, mode="flux",
                                                 niveau_attendu=niv[esp])
            except Exception as e:  # noqa: BLE001
                v3 = [f"exception {type(e).__name__}"]
            verifier(ici and v3, f"{esp}, artefact « {nom} » : refusé ici {bool(ici)}, refusé par v3 {bool(v3)} {v3}")
        nd = g3.LIMITES_SORTIE[esp]["non_diffuse"]
        print(f"  {esp} hors flux : limite {nd}, exigé {m['provision'] + TEXTE_MIN} -> lot permis {nd >= m['provision'] + TEXTE_MIN}")
    print("=== 3. Cellules recalculées, chemins et pointes ===")
    R = json.loads(vd.RELEVE.read_text(encoding="utf-8"))
    prix = {"opus": po, "carbon": (max(pc[0]), max(pc[1])), "neon": (pn[0][0], pn[1][0])}
    coupures = {"E3-T1-conception-B", "E3-T2-critique-croisee-B"}
    total = {}
    for bras, qp in vd.BRAS.items():
        rangs = vd.cellules(qp, R)
        ecart = 0.0
        for c in rangs:
            m = next(col.MODELES[l] for l in col.LETTRES if col.MODELES[l]["espece"] == c["esp"])
            pi, po_ = prix[c["esp"]]
            att = c["in_att"] / 1e6 * pi + c["out_med"] / 1e6 * po_
            haut = c["in_max"] / 1e6 * pi + c["out_p90"] / 1e6 * po_
            pire = c["garde"] / 1e6 * pi + (m["max"] + m["provision"]) / 1e6 * po_
            ecart = max(ecart, abs(att - c["att"]), abs(haut - c["haut"]), abs(pire - c["pire"]))
        verifier(ecart < 1e-9, f"bras {bras} : attendu, haut et pire recalculés aux tarifs relus, écart max {ecart:.2e}")
        carbon_max = max(c["pire"] for c in rangs if c["esp"] == "carbon")
        for nom, abo in (("A", True), ("B", False)):
            gratuit = (lambda c, abo=abo: abo and c["esp"] == "opus")  # noqa: E731
            fin_s, pointe_s, ou_s = chemin(rangs, gratuit, False, coupures)
            fin_p, pointe_p, ou_p = chemin(rangs, gratuit, True, coupures)
            t = vd.option(rangs, abo)
            verifier(abs(pointe_s - t["pointe"]) < 1e-9 and abs(fin_s - t["haut_2_coupures"]) < 1e-9,
                     f"bras {bras}, option {nom}, séquentiel : chemin {fin_s:.4f}, pointe {pointe_s:.4f} ({ou_s}) ; "
                     f"brouillon {t['haut_2_coupures']:.4f}, {t['pointe']:.4f}")
            pl_s, pl_p = math.ceil(pointe_s + 2 * carbon_max), math.ceil(pointe_p + 2 * carbon_max)
            verifier(abs(pointe_p - t["pointe_par"]) < 1e-9 and pl_p == t["plafond_par"] and pl_s == t["plafond"],
                     f"bras {bras}, option {nom} : pointe parallèle et plafonds égaux au script v5 "
                     f"({t['pointe_par']:.4f}, {t['plafond']}, {t['plafond_par']})")
            print(f"  bras {bras}, option {nom}, parallèle : chemin {fin_p:.4f}, pointe {pointe_p:.4f} ({ou_p}) ; "
                  f"plafond séquentiel {pl_s}, parallèle {pl_p} ; coupures de Carbon de plus tolérées sous "
                  f"{pl_s} en parallèle : {max(0, math.floor((pl_s - pointe_p) / carbon_max))}")
            total[(bras, nom)] = (pointe_s, pointe_p, pl_s, pl_p)
    for nom in ("A", "B"):
        a, b = total[("principal", nom)], total[("temoin", nom)]
        print(f"  option {nom} : plafonds séquentiels {a[2]}+{b[2]}={a[2] + b[2]} ; parallèles {a[3]}+{b[3]}={a[3] + b[3]}")
    print("=== 4. Pour information : tableaux du devis v2 (question v2) contre le calcul v5 ===")
    md = (ICI / "devis-collisionneur-questions-directeur-v2.md").read_text(encoding="utf-8")
    num = lambda s: float(s.replace(" ", "").replace(" ", "").replace(",", "."))  # noqa: E731
    for bras, titre, fin in (("principal", "### 4.1", "### 4.2"), ("temoin", "### 4.2", "## 5.")):
        bloc = md[md.index(titre):md.index(fin)]
        lignes = [l for l in bloc.splitlines() if l.startswith("| III.")]
        rangs = vd.cellules(vd.BRAS[bras], R)
        ecarts = []
        for l, c in zip(lignes, rangs):
            cases = [x.strip() for x in l.strip("|").split("|")]
            vals = cases[4:] if bras == "principal" else cases[3:]
            entree = num(cases[2])
            attendus = [c["att"], c["haut"], c["pire"], c["avec"]] + ([c["marge_kit"]] if c["marge_kit"] else [])
            lus = [num(v) for v in vals if v != "—"]
            if abs(entree - round(c["in_att"])) > 0.5 or any(abs(a - b) > 0.0051 for a, b in zip(attendus, lus)):
                ecarts.append((c["cid"], cases))
        print(f"  info  bras {bras} : {len(lignes)} lignes lues ; lignes du devis v2 qui diffèrent du calcul v5 "
              f"(entrée à ±0,5 jeton, montants à ±0,0051) : {[e[0] for e in ecarts]}")
    print(f"VERDICT : toutes les vérifications tiennent = {OK}")
    return 0 if OK else 1


if __name__ == "__main__":
    sys.exit(main())
