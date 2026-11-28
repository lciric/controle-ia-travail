"""VF3 : puissance des propriétés de la partie 2. Douze altérations du module (copies modifiées sous
`mutants_puissance/`, jamais le module copié lui-même), verrou de fin du module neutralisé dans le processus pour que
seules mes propriétés jugent : chaque altération doit produire au moins une violation de propriété sur les variantes.
Un « 0 violation » sur le module final n'a de sens que si ces altérations sont vues.

Usage : python -B puissance_des_proprietes.py <journal json>"""
import copy
import importlib.util
import json
import os
import sys

import commun
from commun import P, np, tc  # noqa: F401

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = open(os.path.join(commun.COPIE, "complements_p3_v1.py"), encoding="utf-8").read()
ALTERATIONS = {
    "P01 table : P3-P4 sans la condition de ligne": (
        'p4 = bool(p3 and L["conforme"][p] and L["ligne"].startswith(LIGNE_CRITERES))', 'p4 = bool(p3 and L["conforme"][p])'),
    "P02 A1 : sens « non au-dessus » ignoré": (
        'contraire = r["ecart_bas"] <= 0.0 if sens == "au-dessus" else r["ecart_bas"] > 0.0',
        'contraire = r["ecart_bas"] <= 0.0'),
    "P03 audit : « non lu » compté déclenché": (
        'declenchees = [c for c in possibles if c["controle_contraire"] is True]',
        'declenchees = [c for c in possibles if c["controle_contraire"] in (True, NON_LU)]'),
    "P04 recommandation : non lue dite non robuste": (
        'recommandation.append(f"{c} : non contrôlée par l\'addendum (réserves : "',
        'recommandation.append(f"{c} : établie au sens de la lecture décisive, non robuste aux contrôles de l\'addendum (réserves : "'),
    "P05 A6 : réserve témoin même si déjà > 0": (
        'bool(r["bas"] > 0.0 and not deja)', 'bool(r["bas"] > 0.0)'),
    "P06 A7 : quasi totale nommée forme du coût": (
        'e.controle(test, cible, True, "reserve_A7_forme_quasi_totale",', 'e.controle(test, cible, True, "reserve_A7_forme_du_cout",'),
    "P07 A5 : non calculable rendu non lu": (
        'e.controle(test, cible, True, "reserve_A5_bornes_T2", f"{nom} non calculable', 'e.controle(test, cible, None, None, f"{nom} non calculable'),
    "P08 clés interdites gardées": (
        'return {k: _sans_cles_interdites(v) for k, v in x.items() if k not in CLES_INTERDITES}',
        'return {k: _sans_cles_interdites(v) for k, v in x.items()}'),
    "P09 synthèse : réserves de A8 omises": (
        '            if c.get("reserve"):\n                reserves.append(',
        '            if c.get("reserve") and a != "A8":\n                reserves.append('),
    "P10 issue recopiée sans ses réserves": (
        '"issue_primaire": issue_primaire,', '"issue_primaire": {**issue_primaire, "reserves": []},'),
    "P11 A8 : « et » devenu « ou »": (
        's > SEUIL_TROIS_PREMIERS and h > SEUIL_TROIS_PREMIERS', 's > SEUIL_TROIS_PREMIERS or h > SEUIL_TROIS_PREMIERS'),
    "P12 audit : « aucune » dès une conclusion": (
        'aucune = not declenchees and len(etablies) >= 3 and audit_r4_declenche',
        'aucune = not declenchees and len(etablies) >= 1 and audit_r4_declenche'),
    "P13 sans objet qui écrit sa réserve": (
        'self.controles.append({"test": test, "cible": cible, "controle_contraire": SANS_OBJET})\n            return',
        'self.controles.append({"test": test, "cible": cible, "controle_contraire": SANS_OBJET, "reserve": reserve})\n            return'),
    "P14 A3 : Δ_SM visant P3-P4": (
        '(("ST", "P3-P4", "reserve_A3_validite_P4"), ("SM", "T3", "reserve_A3_intention_T3"))',
        '(("ST", "P3-P4", "reserve_A3_validite_P4"), ("SM", "P3-P4", "reserve_A3_intention_T3"))'),
}


def charger(nom, source):
    d = os.path.join(ICI, "mutants_puissance")
    os.makedirs(d, exist_ok=True)
    chemin = os.path.join(d, f"{nom}.py")
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(source)
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    m.exiger_verrou = lambda *a, **k: None          # seul le jugement des propriétés compte ici
    m.TIRAGES_AIRE, m.TIRAGES_COUT = 60, 500
    return m


def main(chemin):
    import verrou_proprietes as vp
    S = vp.base_scenarios()
    choix = ("sain", "temoin", "a6_inverse", "a7_quasi", "a5_bornes", "a8_debut", "non_etabli", "consigne_mention")
    bases = {}
    for nom in choix:
        src = S[nom]()
        bases[nom] = (src, vp.lecture_reduite(src),
                      {p: next(x["agregation"] for x in src["sondes-figees"]["sondes"] if x["nom"] == p) for p in P})
    journal = {}
    for k, (nom_alt, (avant, apres)) in enumerate(ALTERATIONS.items()):
        if SOURCE.count(avant) != 1:
            journal[nom_alt] = {"erreur": f"motif trouvé {SOURCE.count(avant)} fois"}
            print(nom_alt, journal[nom_alt], flush=True)
            continue
        m = charger(f"mutant_puissance_{k:02d}", SOURCE.replace(avant, apres))
        G = vp.graines(m.cles_addendum(P), m.ENTROPIE_P3)
        rng = np.random.default_rng(5)
        vues, runs, exemples = 0, 0, []
        for nom in choix:
            src, lec0, familles = bases[nom]
            for v in range(3):
                lec = copy.deepcopy(lec0)
                if v:
                    vp.muter(lec, rng)
                vp.recalculer(lec)
                avant_l = json.dumps(lec, sort_keys=True)
                try:
                    s = m.analyser_addendum(src, lec, G)
                except Exception as e:                      # une garde interne du module altéré a arrêté
                    vues += 1
                    runs += 1
                    exemples.append(f"{nom}/{v} : arrêt {type(e).__name__} : {str(e)[:120]}")
                    continue
                viol = vp.verifier_sortie(s, lec, avant_l, familles)
                runs += 1
                if viol:
                    vues += 1
                    exemples.append(f"{nom}/{v} : {viol[0][:200]}")
        journal[nom_alt] = {"variantes": runs, "variantes_en_violation": vues, "exemples": exemples[:3]}
        print(nom_alt, "→", vues, "sur", runs, exemples[:1], flush=True)
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(journal, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1])
