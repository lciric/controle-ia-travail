"""Calcul du devis du collisionneur, dossier des questions du directeur du 24 novembre (v3).

v3 : copie de verif_devis_questions_directeur_v2.py (a482e717…, inchangé, R12). Changement, et seulement celui-là :
  bras principal sur question-neutre-groupee-questions-directeur-v3.md et bras témoin sur
  question-temoin-neutre-questions-directeur-v2.md (retouches du test de devinette v2).

v2 : copie de verif_devis_questions_directeur_v1.py (7d16c136…, inchangé, R12). Changements, et seulement ceux-là :
  (a) bras principal sur question-neutre-groupee-questions-directeur-v2.md (retouches du test de devinette v1) ; faits et
      question témoin v1 inchangés ;
  (b) pointe et plafond aussi en envoi parallèle (les trois cellules d'un tour ensemble, marge du lot = somme des
      marges, relance d'une cellule coupée seule après le lot), modèle de la vérification du devis v1, section 5 ;
  (c) pour information, attendu avec pannes au taux de panne de Carbon le plus prudent du relevé (13/79), réserve 4 de
      la même vérification.


Pièce de travail (classe C), dérivée de docs/notes/protocole-x-boucle-organisme-controle-v1/verif_devis.py
(d3fbc0e4…, son compagnon .sha256) : mêmes formules (attendu = sorties médianes et pièces médianes du relevé des journaux ;
haut = 90e centile et pièces maximales ; pire = formule de garde du moteur ; espérance des pannes = taux de panne observé
× pire). Changements, et seulement ceux-là :
  (1) chemins relatifs au dépôt, et non plus ceux d'une autre machine ; fichiers d'entrée du présent dossier ;
  (2) aucune écriture sur disque : les invitations sont reconstruites en mémoire par construire_prompt (lecture scellée
      remplacée par une lecture en mémoire), et non plus dans un dossier temporaire ;
  (3) chemin des envois et pointe « dépense comptée avant plus marge exigée » calculés envoi par envoi, avec, pour
      l'option de l'abonnement, la marge du kit d'Opus (128 000 jetons de sortie au barème 4 / 20, coût nul), comme le
      devis du service v8, version 3, section 7.2 ;
  (4) plafond proposé par bras = pointe du scénario haut à deux coupures de Carbon, plus deux coupures de Carbon de plus,
      arrondi à l'entier supérieur (méthode des devis v2 de la boucle et v3 du service v8) ;
  (5) attendu au barème facturé de Carbon jusqu'au 30 novembre 2026 (2 / 10), pour information.
Aucun appel réseau. Lancement : PYTHONDONTWRITEBYTECODE=1 python3 -I verif_devis_questions_directeur_v3.py
"""
import contextlib
import hashlib
import io
import json
import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[3]
sys.path.insert(0, str(DEPOT / "docs" / "notes" / "collisionneur-v9"))
sys.path.insert(0, str(DEPOT / "src"))
import collisionneur_v9_v8d as col  # noqa: E402
from controle_ia import garde_google_v3 as g3  # noqa: E402

FAITS = ICI / "faits-neutres-questions-directeur-v1.md"
BRAS = {"principal": ICI / "question-neutre-groupee-questions-directeur-v3.md",
        "temoin": ICI / "question-temoin-neutre-questions-directeur-v2.md"}
RELEVE = DEPOT / "docs" / "notes" / "service-collisionneur-modes-v8-v1" / "calculs" / "releve-journaux-v2.json"
# Taux de panne observés, repris de service-collisionneur-modes-v8-v1/calculs-v3/calcul_devis_v8_v3.py, ligne 19.
TAUX_PANNE = {"carbon": 7 / 56, "neon": 1 / 26, "opus": 2 / 52}
ESPECES = ["opus", "carbon", "neon"]
MAX_KIT_OPUS = 128000  # marge du kit de la voie de l'abonnement (devis du service v8, v3, section 5)
PRIX_CARBON_FACTURE_NOV = (2.0, 10.0)  # page de prix de Google versée le 22 novembre 2026, lignes 155 et 162


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def installer_memoire(question_p):
    memoire = {"faits.md": col.lire_entree(FAITS), "question-etage3.md": col.lire_entree(question_p)}
    col.lire_sceau = lambda chemin: (memoire[Path(chemin).name], col.empreinte(memoire[Path(chemin).name]))
    col.cellule_valide = lambda dossier, cid: None
    col.statut_courant = lambda dossier, cid: "jamais lancée"
    col.fixer_composition(ESPECES, nom_cle_anthropic="CLE_FICTIVE")


def cellules(question_p, R):
    installer_memoire(question_p)
    rangs = []
    for tour in col.ORDRE_ETAGE[3]:
        for l in col.LETTRES:
            m = col.MODELES[l]
            esp = m["espece"]
            ids = col.entrees(tour, l, [])
            prompt, _ = col.construire_prompt(Path("dossier-en-memoire"), tour, l, [], set(ids))
            base = len(prompt) - sum(len(col.bloc_absent(c, "jamais lancée")) for c in ids)
            enveloppe = sum(len(col.bloc_piece(c, "", "0" * 64)) for c in ids)

            def taille(cid, cle):
                return R[f"{col.MODELES[cid[-1]]['espece']}|{cid[:5]}"][cle]

            car_att = base + enveloppe + sum(taille(c, "car_cellule_med") for c in ids)
            car_max = base + enveloppe + sum(taille(c, "car_cellule_max") for c in ids)
            r = R[f"{esp}|{tour}"]
            in_att = car_att / r["car_par_jeton_entree_med"]
            in_max = car_max / r["car_par_jeton_entree_med"]
            garde = math.ceil(math.ceil(car_max / 2.5) * 1.01) + 32
            pire = col.cout_pire_garde(m, garde, m["max"])
            pire_rel = col.cout_pire_garde(m, garde, m["max_relance"])
            relances = 2 if (m["fournisseur"] == "gemini" and col.reglage_de_relance(m)[1]) else 1
            rangs.append(dict(
                cid=col.id_cellule(tour, l), esp=esp, prix=m["prix"], in_att=in_att, in_max=in_max,
                out_med=r["sortie_med"], out_p90=r["sortie_p90"],
                att=in_att / 1e6 * m["prix"][0] + r["sortie_med"] / 1e6 * m["prix"][1],
                haut=in_max / 1e6 * m["prix"][0] + r["sortie_p90"] / 1e6 * m["prix"][1],
                garde=garde, pire=pire, pire_rel=pire_rel, relances=relances,
                avec=pire + relances * pire_rel, panne=TAUX_PANNE[esp] * pire,
                marge_kit=garde / 1e6 * 4.0 + MAX_KIT_OPUS / 1e6 * 20.0 if esp == "opus" else None,
                att_nov=(in_att / 1e6 * PRIX_CARBON_FACTURE_NOV[0] + r["sortie_med"] / 1e6 * PRIX_CARBON_FACTURE_NOV[1])
                if esp == "carbon" else None))
    return rangs


def option(rangs, abonnement):
    """Totaux d'un bras, et pointe du scénario haut à deux coupures de Carbon (tours III.1 et III.2)."""
    def gratuit(c):
        return abonnement and c["esp"] == "opus"

    t = {k: 0.0 for k in ("att", "haut", "pire", "avec", "panne", "att_nov")}
    for c in rangs:
        if gratuit(c):
            continue
        for k in ("att", "haut", "pire", "avec", "panne"):
            t[k] += c[k]
        t["att_nov"] += c["att_nov"] if c["att_nov"] is not None else c["att"]
    # chemin des envois, dans l'ordre des tours et des lettres
    depense, pointe, ou = 0.0, 0.0, None
    coupures = {"E3-T1-conception-B", "E3-T2-critique-croisee-B"}
    for c in rangs:
        marge = c["marge_kit"] if gratuit(c) else c["pire"]
        envois = [("coupé", c["pire"], marge), ("relance", c["haut"], c["pire_rel"])] if c["cid"] in coupures \
            else [("", 0.0 if gratuit(c) else c["haut"], marge)]
        for quoi, cout, mg in envois:
            if depense + mg > pointe:
                pointe, ou = depense + mg, f"{c['cid']} {quoi}".strip()
            depense += cout
    t["haut_2_coupures"] = depense
    t["pointe"], t["pointe_ou"] = pointe, ou
    # v2 (b) : envoi parallèle, tour par tour
    depense_p, pointe_p, ou_p = 0.0, 0.0, None
    for tour in ("E3-T1", "E3-T2", "E3-T3"):
        lot = [c for c in rangs if c["cid"].startswith(tour)]
        marge_lot = sum(c["marge_kit"] if gratuit(c) else c["pire"] for c in lot)
        if depense_p + marge_lot > pointe_p:
            pointe_p, ou_p = depense_p + marge_lot, f"lot {tour}"
        for c in lot:
            depense_p += c["pire"] if c["cid"] in coupures else (0.0 if gratuit(c) else c["haut"])
        for c in lot:
            if c["cid"] in coupures:
                if depense_p + c["pire_rel"] > pointe_p:
                    pointe_p, ou_p = depense_p + c["pire_rel"], f"{c['cid']} relance"
                depense_p += c["haut"]
    carbon_max = max(c["pire"] for c in rangs if c["esp"] == "carbon")
    t["plafond"] = math.ceil(pointe + 2 * carbon_max)
    t["pointe_par"], t["pointe_par_ou"] = pointe_p, ou_p
    t["plafond_par"] = math.ceil(pointe_p + 2 * carbon_max)
    t["carbon_max"] = carbon_max
    # v2 (c) : taux de panne de Carbon 13/79
    t["panne_prudent"] = t["panne"] + sum((13 / 79 - TAUX_PANNE["carbon"]) * c["pire"]
                                          for c in rangs if c["esp"] == "carbon")
    return t


def main():
    print(f"moteur {col.VERSION} {sha(col.__file__)} ; garde Google {sha(g3.__file__)} ; relevé {sha(RELEVE)}")
    print("=== 0. Entrées ===")
    for p in [FAITS, *BRAS.values()]:
        txt = col.lire_entree(p)
        print(f"{p.name} : octets={len(p.read_bytes())} caracteres={len(txt)} mots={len(txt.split())} sha256={sha(p)}")
    print("=== 1. Réglages de Google (garde commune v3), flux ===")
    col.fixer_composition(ESPECES, nom_cle_anthropic="CLE_FICTIVE")
    for l in col.LETTRES:
        m = col.MODELES[l]
        if m["fournisseur"] != "gemini":
            print(f"{m['espece']} : max={m['max']} relance={m['max_relance']} effort={col.EFFORT}")
            continue
        for tour in col.ORDRE_ETAGE[3]:
            mots = col.TOURS[tour]["mots"]
            corps = col.demande_gemini(m, "essai", m["max"])
            probs = g3.verifier_reglages_google(m["espece"], corps, m["provision"], mots=mots, mode="flux")
            texte = m["max"] - m["provision"]
            besoin = math.ceil(mots * g3.JETONS_PAR_MOT_MESURES[m["espece"]])
            print(f"{m['espece']} {tour} : niveau={m['niveau_reflexion']} max={m['max']} provision={m['provision']} "
                  f"texte={texte} (>=16000 : {texte >= 16000}) mots={mots} -> {besoin} jetons (< texte : "
                  f"{besoin < texte}) ; problemes={probs}")
        nd = g3.LIMITES_SORTIE[m["espece"]]["non_diffuse"]
        print(f"{m['espece']} : limite hors flux {nd}, exigée {m['provision'] + 16000} -> lot permis : "
              f"{nd >= m['provision'] + 16000}")
    R = json.loads(RELEVE.read_text(encoding="utf-8"))
    resultats = {}
    for bras, qp in BRAS.items():
        print(f"=== 2. Bras {bras} ===")
        installer_memoire(qp)
        with contextlib.redirect_stdout(io.StringIO()):
            natif = col.devis(FAITS, qp, jev=False)[3]
        print(f"devis natif du moteur, étage III, borne large, interface : {natif:.4f}")
        rangs = cellules(qp, R)
        for c in rangs:
            mk = f" marge_kit={c['marge_kit']:.4f}" if c["marge_kit"] is not None else ""
            print(f"  {c['cid']:26s} {c['esp']:6s} in_att={c['in_att']:7.0f} out_med={c['out_med']:7.0f} "
                  f"out_p90={c['out_p90']:7.0f} att={c['att']:.4f} haut={c['haut']:.4f} pire={c['pire']:.4f} "
                  f"avec_relances={c['avec']:.4f} (relances={c['relances']}) panne={c['panne']:.4f}{mk}")
        for nom, abo in (("A, Opus par l'abonnement", True), ("B, Opus par l'interface", False)):
            t = option(rangs, abo)
            resultats[(bras, abo)] = t
            print(f" option {nom} : attendu={t['att']:.4f} panne={t['panne']:.4f} attendu+pannes="
                  f"{t['att'] + t['panne']:.4f} haut={t['haut']:.4f} haut_2_coupures_carbon={t['haut_2_coupures']:.4f} "
                  f"pire_sans_relance={t['pire']:.4f} pire_avec_relances={t['avec']:.4f} pointe={t['pointe']:.4f} "
                  f"({t['pointe_ou']}) carbon_pire_max={t['carbon_max']:.4f} plafond_propose={t['plafond']} "
                  f"attendu_carbon_facture_novembre={t['att_nov']:.4f} pointe_parallele={t['pointe_par']:.4f} "
                  f"({t['pointe_par_ou']}) plafond_parallele={t['plafond_par']} "
                  f"attendu+pannes_carbon_13_sur_79={t['att'] + t['panne_prudent']:.4f}")
    print("=== 3. Totaux des deux bras appariés ===")
    for nom, abo in (("A", True), ("B", False)):
        a, b = resultats[("principal", abo)], resultats[("temoin", abo)]
        s = lambda k: a[k] + b[k]  # noqa: E731
        print(f"option {nom} : attendu={s('att'):.2f} attendu+pannes={s('att') + s('panne'):.2f} "
              f"haut_2_coupures={s('haut_2_coupures'):.2f} pire_sans_relance={s('pire'):.2f} "
              f"pire_avec_relances={s('avec'):.2f} plafonds={a['plafond']}+{b['plafond']}={a['plafond'] + b['plafond']} "
              f"attendu_carbon_facture_novembre+pannes={s('att_nov') + s('panne'):.2f} "
              f"plafonds_paralleles={a['plafond_par']}+{b['plafond_par']}={a['plafond_par'] + b['plafond_par']} "
              f"attendu+pannes_carbon_13_sur_79={s('att') + s('panne_prudent'):.2f}")


if __name__ == "__main__":
    main()
