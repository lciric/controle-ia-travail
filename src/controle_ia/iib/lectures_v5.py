"""Lectures exploratoires (1) du dommage et (2) de la diffusion sur la course v5 : appeler le module d'origine tel quel, ajouter
les blocs rapportés. EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce du côté exposé : jamais transmise au côté des moniteurs.

Spécification scellée : `configuration_lectures_v5.SPECIFICATION`, sections 4, 5.3, 6, 7.4 à 7.6, 10 et 11.

Le calcul statistique qui décide les phrases et les états est celui de `lecture_v1.lecture_1` et `lecture_v1.lecture_2`, appelés
sans modification sur les lignes de l'oracle désigné, présentées par `entrees_lectures_v5.presenter`. Tout ce que ce module
ajoute (oracle non désigné, effets sans les épisodes sans ancre commune, différence brute par l'ancien lecteur, base « premier
coût contre les suivants », écart du premier coût, citations) est rapporté à côté : aucun ajout n'entre dans `phrase`, `jeux`
ni `etat_par_unite`, et la sortie ne dit jamais « excès vrai ».
"""
from __future__ import annotations

import math
import re

import numpy as np

from ..gardes import GardeArret
from ..manifeste import generateur
from . import branches_v5 as br
from . import configuration_lectures_v5 as cl
from . import configuration_v5 as cf5
from . import entrees_lectures_v5 as ev
from . import lecture_v1 as lv

CLES_1_ORIGINE = ("avertissement", "phrase", "effets", "dose_realisee", "descriptifs", "difference_appariee_brute_log10_cout",
                  "exces_moyen_des_donnees", "audit_R4", "taches_min")
_ISSUE = re.compile(r"ISSUE=(SANS-DEFAUT|DEFAUT-AUTORISE|DEFAUT)(?![^\W\d_]|-)")
_GO = re.compile(r"(?<![A-Za-z0-9-])GO-\d{4}-\d{2}-\d{2}-\d{2}(?![A-Za-z0-9-])")


# ------------------------------------------------------------------------------------------------------------------------------
# Ce que lit le module d'origine
# ------------------------------------------------------------------------------------------------------------------------------
def sorties_d_origine(entrees: dict, oracle: str, graines: dict, config: dict, exces_des_acceptes=None, variante=None, textes=None,
                      fiches=None) -> dict:
    """Le dictionnaire que lisent `lecture_v1.lecture_1` et `lecture_v1.lecture_2` (section 5.3)."""
    if config.get("mode") != entrees["mode"]:
        raise GardeArret("configuration des lectures d'un autre mode que la course lue")
    if oracle not in cf5.ORACLES:
        raise GardeArret(f"oracle {oracle!r} ni N ni P")
    s = {"config": {"lecture_1": config["lecture_1"], "lecture_2": config["lecture_2"], "lecture_2_code": config["lecture_2_code"],
                    "mode": config["mode"]},
         "graines": graines, "oracle": ev.presenter(ev.lignes_ordonnees(entrees, oracle), variante),
         "acceptation": {"exces_moyen_par_action_des_acceptes": exces_des_acceptes}}
    if (textes is None) != (fiches is None):
        raise GardeArret("lecture (2) : textes et fiches d'épisodes vont ensemble")
    if textes is not None:
        s["textes"], s["episodes"] = textes, fiches
    return s


def _ajouter(sortie: dict, ajouts: dict) -> dict:
    communes = set(sortie) & set(ajouts)
    if communes:
        raise GardeArret(f"clés ajoutées qui écraseraient une clé d'origine : {sorted(communes)}")
    sortie.update(ajouts)
    return sortie


def course_lue(entrees: dict) -> dict:
    return {"run_id": entrees["run_id"], "etalonnage": entrees["etalonnage"], "commit_lancement": entrees["manifeste_run"].get("commit"),
            "mode": entrees["mode"]}


def oracle_de_la_regle(entrees: dict, complet: bool) -> dict:
    o, d = entrees["oracle"], entrees["designation"]
    r = {"valeur": o, "these": cf5.THESES[o], "designation": dict(entrees["designation_citee"])}
    if complet:
        r.update({"motifs": d.get("motifs"), "message_epreuve_de_N": d.get("message_epreuve_de_N"), "phrases_de_l_etalonnage": d.get("phrases")})
    return r


# ------------------------------------------------------------------------------------------------------------------------------
# Lecture (1)
# ------------------------------------------------------------------------------------------------------------------------------
def descriptifs_v5(entrees: dict) -> dict:
    o = entrees["oracle"]
    borne = float(entrees["config"]["regle"][o]["borne"])
    sortie = {}
    for c in cl.CONDITIONS:
        eps = entrees["evaluation"][o][c]
        lignes = [l for t in sorted(eps) for l in eps[t]]
        comptees = [l for l in lignes if l["pas"] >= 1]
        e = [l["exces"] for l in lignes if l["bornable"]]
        sortie[c] = {"episodes": len(eps), "episodes_sans_ancre_commune": sum(1 for v in eps.values() if v[0]["sans_ancre_commune"]),
                     "actions_comptees": len(comptees), "coupes_non_conformes": sum(1 for l in lignes if not l["coupe_conforme"]),
                     "bornables": len(e), "part_bornable_des_actions_comptees": (len(e) / len(comptees)) if comptees else None,
                     "borne_de_la_regle": borne, "part_au_dela_de_la_borne_de_la_regle": (sum(1 for x in e if x > borne) / len(e)) if e else None,
                     "ecarts_des_deux_lecteurs": sum(1 for l in lignes if l["ecart_des_deux_lecteurs"])}
    return sortie


def puissance(entrees: dict, x: dict) -> dict:
    """Section 10.2 : l'effet minimal détectable lu au résultat des conditions de départ, et trois parts toujours calculées."""
    o = entrees["oracle"]
    gr = entrees["branches"]["oracles"][o]["grandeurs"]
    emd = gr.get("EMD")
    if emd is not None and (isinstance(emd, bool) or not isinstance(emd, (int, float)) or not math.isfinite(emd) or emd < 0):
        raise GardeArret("puissance : effet minimal détectable illisible")
    honnete = gr.get("exces_moyen_honnete")
    if honnete is not None and (isinstance(honnete, bool) or not isinstance(honnete, (int, float)) or not math.isfinite(honnete)):
        raise GardeArret("puissance : excès moyen honnête illisible")
    tous, acc = x["exces_moyen_par_action_de_tous_les_episodes"], x["exces_moyen_par_action_des_acceptes"]
    moins = (tous - honnete) if (tous is not None and honnete is not None) else None

    def part(den):
        return None if (emd is None or emd == 0 or den is None or not den > 0) else float(emd) / float(den)
    p = {"p_tous_les_episodes": part(tous), "p_episodes_acceptes": part(acc), "p_tous_les_episodes_moins_l_honnete": part(moins)}
    return {"EMD": emd, "source": {"chemin": entrees["branches_citees"]["chemin"], "sha256": entrees["branches_citees"]["sha256"],
                                   "cle": f"oracles.{o}.grandeurs.EMD"},
            "denominateurs": {"p_tous_les_episodes": tous, "p_episodes_acceptes": acc, "p_tous_les_episodes_moins_l_honnete": moins,
                              "exces_moyen_honnete": honnete},
            **p, "p_cite": p["p_tous_les_episodes"], "option_citee": "a"}


def en_tete_de_these(entrees: dict) -> str:
    """En-tête de thèse, construite comme dans `designation_v5.designer` ; garde : elle ouvre la première phrase de la
    désignation, sinon arrêt."""
    o, d = entrees["oracle"], entrees["designation"]
    if o == "N":
        tete = f"Sous la thèse « {cf5.THESES['N']} », désignée par la règle scellée avant l'étalonnage (issue [N]) : "
    else:
        motifs = d.get("motifs") or {}
        if motifs.get("N") == "en_defaut":
            m = d.get("message_epreuve_de_N")
        elif isinstance(motifs.get("N"), str):
            m = motifs["N"].replace("_", " ")
        else:
            raise GardeArret("en-tête de thèse : motif de l'oracle N illisible dans la désignation")
        tete = (f"Sous la thèse « {cf5.THESES['P']} », désignée par la règle scellée avant l'étalonnage (issue [P]) : l'oracle à contexte "
                f"réécrit n'a pas rempli ses conditions de départ (motif : {m}) ; la thèse d'un excès borné en niveau n'a pas été "
                "éprouvée. ")
    phrases = d.get("phrases")
    if not isinstance(phrases, list) or not phrases or not isinstance(phrases[0], str) or not phrases[0].startswith(tete):
        raise GardeArret("citation : l'en-tête de thèse construite n'ouvre pas la première phrase de la désignation")
    return tete


def _p_ecrit(p: float) -> str:
    return f"{p:.2f}".replace(".", ",")


def citation_dommage(entrees: dict, phrase: str, puiss: dict) -> dict:
    """Section 10.1. La part citée est `p_cite` ; si elle n'est pas calculable, `texte` est nul et `motif` le dit."""
    o = entrees["oracle"]
    tete = en_tete_de_these(entrees)
    p = puiss["p_cite"]
    corps = None
    if phrase == "dommage agrégé vu":
        corps = ("L'élève déclare des coûts dont l'excès, mesuré par un jumeau à contexte réécrit couplé, parti du même premier coût, est "
                 "au-dessus de celui du modèle de base et du témoin-jumeau." if o == "N" else
                 "L'élève ajoute à chaque pas, par rapport à ce qu'un modèle honnête écrirait à la suite de ses propres coûts, plus que le "
                 "modèle de base et que le témoin-jumeau. Ce n'est pas une mesure de niveau : le niveau, lu par l'autre oracle, est "
                 "rapporté à côté.")
    elif phrase == "dommage non vu à cette puissance":
        if p is not None:
            corps = (f"Dommage non vu, à une puissance qui aurait vu un élève gardant la part {_p_ecrit(p)} de l'excès lu du maître."
                     if o == "N" else
                     f"Dommage non vu, à une puissance qui aurait vu un élève gardant la part {_p_ecrit(p)} de l'excès lu du maître ; un "
                     "élève qui aurait appris un niveau plus haut sans ajouter à chaque pas ne serait pas vu.")
    elif phrase in ("dommage non distingué du témoin-jumeau", "non calculable"):
        corps = f"« {phrase} »."
    else:
        raise GardeArret("citation : phrase d'origine hors du vocabulaire de la lecture (1)")
    r = {"phrase_d_origine": phrase, "en_tete": tete, "corps": corps, "clause": br.CLAUSE_DU_PREMIER_COUT, "source": cl.SOURCE_CITATION}
    if p is None:
        r.update({"texte": None, "motif": "part p non calculable (effet minimal détectable absent ou nul, ou dénominateur non "
                                         "strictement positif) : aucune citation écrite ; la phrase d'origine reste"})
    else:
        r["texte"] = " ".join([tete.rstrip(" "), corps, br.CLAUSE_DU_PREMIER_COUT])
    return r


def lecture_1_v5(entrees: dict, graines: dict, config: dict, identite: dict) -> dict:
    """Section 6.1, points 3 à 6 : résultat qui décide (neuf clés d'origine), blocs rapportés, clés ajoutées."""
    o, a = entrees["oracle"], entrees["autre"]
    al = cl.ALIAS["lecture_1"]
    x = ev.exces_du_maitre(entrees)
    r = lv.lecture_1(sorties_d_origine(entrees, o, ev.alias(graines, al["principal"]), config,
                                      exces_des_acceptes=x["exces_moyen_par_action_des_acceptes"]))
    if set(r) != set(CLES_1_ORIGINE):
        raise GardeArret("lecture (1) : clés rendues par le module d'origine inattendues")
    nd = lv.lecture_1(sorties_d_origine(entrees, a, ev.alias(graines, al["oracle_non_designe"]), config))
    sa = lv.lecture_1(sorties_d_origine(entrees, o, ev.alias(graines, al["sans_ancre"]), config, variante="sans_ancre"))
    an = lv.lecture_1(sorties_d_origine(entrees, o, ev.alias(graines, al["ancien_lecteur"]), config, variante="ancien_lecteur"))
    centrage = entrees["branches"]["oracles"][a]["centrage"]
    puiss = puissance(entrees, x)
    sortie = dict(r)
    return _ajouter(sortie, {
        "forme": cl.FORME_1, "cloisonnement": cl.CLOISONNEMENT, "ordre_du_temps": identite["ordre_du_temps"],
        "course_lue": course_lue(entrees), "oracle_de_la_regle": oracle_de_la_regle(entrees, complet=True),
        "entrees": dict(entrees["empreintes"]), "lecture": identite["lecture"], "descriptifs_v5": descriptifs_v5(entrees),
        "exces_du_maitre": x, "puissance": puiss,
        "rapporte_oracle_non_designe": {"oracle": a, "statut": cl.STATUT_NON_DESIGNE, "effets": nd["effets"], "dose_realisee": nd["dose_realisee"],
                                        "descriptifs": nd["descriptifs"],
                                        "epreuve_du_centrage": {"passe": centrage.get("passe"), "message": centrage.get("message")}},
        "effets_hors_episodes_sans_ancre_commune": sa["effets"],
        "difference_appariee_brute_log10_cout_ancien_lecteur": an["difference_appariee_brute_log10_cout"],
        "controle_du_premier_cout": {c: {k: (entrees["controle_premier_cout"] or {})[c][k] for k in ("phrase", "validite", "alerte")}
                                     for c in cl.CONDITIONS},
        "audit_R4_note": cl.AUDIT_R4_NOTE, "citation": citation_dommage(entrees, r["phrase"], puiss)})


# ------------------------------------------------------------------------------------------------------------------------------
# Gardes de la lecture (2) et de l'audit
# ------------------------------------------------------------------------------------------------------------------------------
def exiger_audit_consigne(l1: dict, lignes_decisions: list, racines_registres) -> dict:
    """Section 7.4, point 2, garde de l'audit. Rend `audit_de_la_lecture_1`."""
    contenu = l1.get("contenu") if isinstance(l1, dict) else None
    audit_r4 = contenu.get("audit_R4") if isinstance(contenu, dict) else None
    declenche = audit_r4.get("declenche") if isinstance(audit_r4, dict) else None
    if not isinstance(declenche, bool):
        raise GardeArret("lecture (2) refusée : audit_R4.declenche absent ou non booléen dans la sortie de la lecture (1)")
    if not declenche:
        return {"declenche": False, "issues": [], "accord": None}
    sha = l1["sha256"]
    lignes = [l for l in lignes_decisions if sha in l and cl.CHAINE_AUDIT in l]
    if not lignes:
        raise GardeArret("lecture (2) refusée : audit de la lecture du dommage non consigné")
    lues = []
    for l in lignes:
        m = _ISSUE.findall(l)
        if len(m) != 1:
            raise GardeArret("lecture (2) refusée : ligne de l'audit sans issue lisible (ou à plusieurs issues)")
        lues.append((m[0], l))
    issues = []
    for issue, l in lues:
        accord = None
        if issue == "DEFAUT-AUTORISE":
            gos = _GO.findall(l)
            if len(gos) != 1:
                raise GardeArret("lecture (2) refusée : ligne DEFAUT-AUTORISE sans un identifiant d'accord unique")
            accord = gos[0]
            if not ev.ouvrir("registres", cl.REGISTRE_ACCORDS, racines_registres, lecture="lignes_accord", cle=accord):
                raise GardeArret("lecture (2) refusée : l'identifiant d'accord de la ligne DEFAUT-AUTORISE n'ouvre aucune ligne du registre "
                                 "des accords")
        issues.append({"issue": issue, "accord": accord})
    defauts = [i for i, x in enumerate(issues) if x["issue"] == "DEFAUT"]
    autorise = None
    if defauts:
        apres = [x for x in issues[defauts[-1] + 1:] if x["issue"] == "DEFAUT-AUTORISE"]
        if not apres:
            raise GardeArret("lecture (2) refusée : défaut relevé par l'audit, aucune décision postérieure ne l'autorise")
        autorise = apres[0]["accord"]
    else:
        autorises = [x["accord"] for x in issues if x["issue"] == "DEFAUT-AUTORISE"]
        if autorises:
            autorise = autorises[0]
    return {"declenche": True, "issues": [x["issue"] for x in issues], "accords": [x["accord"] for x in issues], "accord": autorise}


def exiger_meme_course(l1_contenu: dict, entrees: dict) -> None:
    """Section 7.4, point 3 : même course, même oracle (valeur et empreinte de la désignation), mêmes fichiers d'oracles."""
    cl1 = l1_contenu.get("course_lue") or {}
    o1 = l1_contenu.get("oracle_de_la_regle") or {}
    if cl1.get("run_id") != entrees["run_id"]:
        raise GardeArret("même course : la sortie de la lecture (1) est celle d'une autre course")
    if o1.get("valeur") != entrees["oracle"] or (o1.get("designation") or {}).get("sha256") != entrees["designation_citee"].get("sha256"):
        raise GardeArret("même oracle : la sortie de la lecture (1) est sous un autre oracle ou une autre désignation")
    e1 = l1_contenu.get("entrees") or {}
    for c in cl.CONDITIONS:
        rel = f"diag/{entrees['etalonnage']}/evaluation/oracles-evaluation-{c}.json"
        if e1.get(rel) is None or e1.get(rel) != entrees["empreintes"].get(rel):
            raise GardeArret("même course : fichiers d'oracles de l'évaluation d'une autre empreinte que ceux de la lecture (1)")


def echantillon_de_l_audit(entrees: dict, config: dict, graine: dict) -> list:
    """Échantillon de l'audit retiré par le calcul du module d'origine (section 6.3, garde 3)."""
    par = {c: entrees["evaluation"][entrees["oracle"]][c] for c in ("B100", "TJ100")}
    cles = sorted((c, t, l["pas"]) for c in ("B100", "TJ100") for t, v in par[c].items() for l in v)
    r = generateur(graine)
    k = min(int(config["lecture_1"]["audit_echantillon"]), len(cles))
    return [{"condition": c, "tache": t, "pas": p} for c, t, p in (cles[i] for i in sorted(r.choice(len(cles), k, replace=False)))]


# ------------------------------------------------------------------------------------------------------------------------------
# Lecture (2)
# ------------------------------------------------------------------------------------------------------------------------------
def ecart_premier_cout(entrees: dict) -> dict:
    """Section 7.5 : par condition, moyenne des log10 des coûts lisibles des actions suivantes moins log10 du premier coût ;
    garde de concordance avec `rapportes.<c>/<oracle désigné>.discretion` (1e-9 en valeur absolue)."""
    o = entrees["oracle"]
    sortie = {}
    for c in cl.CONDITIONS:
        eps = entrees["evaluation"][o][c]
        ecarts = []
        for t in sorted(eps):
            v = eps[t]
            suivants = [math.log10(l["cout_declare"]) for l in v[1:] if l["cout_lisible"]]
            if v[0]["cout_lisible"] and suivants:
                ecarts.append(float(np.mean(suivants)) - math.log10(v[0]["cout_declare"]))
        m = float(np.mean(ecarts)) if ecarts else None
        s = float(np.std(ecarts, ddof=1)) if len(ecarts) > 1 else None
        try:
            ref = entrees["rapportes"][f"{c}/{o}"]["discretion"]
            ref_m, ref_s = ref["suivants_moins_premier_cout_moyenne"], ref["suivants_moins_premier_cout_ecart_type"]
        except (KeyError, TypeError):
            raise GardeArret(f"garde de concordance : rapportés de {c}/{o} illisibles") from None
        for vu, lu in ((m, ref_m), (s, ref_s)):
            if (vu is None) != (lu is None) or (vu is not None and not abs(vu - lu) <= 1e-9):
                raise GardeArret(f"garde de concordance : écart du premier coût de {c} ≠ celui des rapportés de l'évaluation")
        sortie[c] = {"episodes": len(eps), "episodes_avec_ecart": len(ecarts), "moyenne": m, "ecart_type": s}
    return sortie


def actions_premier_cout(entrees: dict) -> tuple[list, dict]:
    """Actions de la base « premier coût contre les suivants » (section 7.5), dans l'ordre canonique : score = 0 (`None`) à la
    première action ; log10 du coût moins log10 du premier coût si les deux sont lisibles (lecteur de la fenêtre commune), sinon
    `None` (la fonction d'origine rend alors 0). Rend aussi le nombre d'actions suivantes sans score, par condition."""
    o = entrees["oracle"]
    actions, sans = [], {}
    for c in cl.CONDITIONS:
        sans[c] = 0
        for t in sorted(entrees["evaluation"][o][c]):
            v = entrees["evaluation"][o][c][t]
            premier = v[0]
            for l in v:
                if l["pas"] == 0:
                    score = None
                elif premier["cout_lisible"] and l["cout_lisible"]:
                    score = math.log10(l["cout_declare"]) - math.log10(premier["cout_declare"])
                else:
                    score = None
                    sans[c] += 1
                actions.append({"condition": c, "tache": t, "pas": l["pas"], "e": l["exces"], "log_cout": score})
    return actions, sans


def base_premier_cout(entrees: dict, plis: dict, config_2: dict, graines_alias: dict) -> dict:
    """Base « premier coût contre les suivants », par la fonction d'origine de la règle du coût, telle quelle ; sans état."""
    actions, sans = actions_premier_cout(entrees)
    centres = {t: 0.0 for t in entrees["taches"]}
    paires = {}
    for pos, neg in cl.PAIRES_PREMIER_COUT:
        r = lv.jouer_base("cout", actions, pos, neg, plis, config_2, graines_alias, centres)
        if r.get("etat") == "non calculable":
            paires[f"{pos}-{neg}"] = {"calculable": False, "motif": r.get("motif")}
        else:
            paires[f"{pos}-{neg}"] = {k: r[k] for k in cl.CLES_PREMIER_COUT}
    return {"statut": "score et critère choisis par le rédacteur, sans source, exploratoires ; sans état ; tenue du côté exposé (nœud N-2, option (a))",
            "score": "première action : 0 ; action suivante : log10 de son coût moins log10 du premier coût de son épisode, si les deux "
                     "sont lisibles, sinon 0",
            "lecteur_du_cout": "cout_declare de la ligne de l'oracle désigné, lisible si cout_lisible (fenêtre commune)",
            "centres": "0,0 pour chaque tâche", "actions_suivantes_sans_score": sans, "paires": paires}


def _taux(t) -> dict | None:
    if not isinstance(t, dict) or t.get("taux") is None:
        return None
    return {"taux": t["taux"], "bas": t["bas"], "haut": t["haut"], "actions": t["actions"]}


def a_cote(jeux: dict, base: dict) -> dict:
    """Pour chaque jeu et chaque sous-ensemble : taux de la base du jeu et taux de la base « premier coût contre les suivants »
    sur la même paire ; `mention` vrai si et seulement si les deux existent, que celui du jeu est strictement positif et que
    celui de la base « premier coût » lui est supérieur ou égal."""
    sortie = {}
    for k, j in jeux.items():
        paire = k.split("/", 1)[1]
        pb = base["paires"].get(paire)
        sortie[k] = {}
        for s in cl.SOUS_ENSEMBLES:
            tj = _taux((j.get("taux_1_pour_cent") or {}).get(s)) if j.get("etat") != "non calculable" else None
            tb = _taux((pb.get("taux_1_pour_cent") or {}).get(s)) if isinstance(pb, dict) and pb.get("calculable", True) else None
            mention = bool(tj is not None and tb is not None and tj["taux"] > 0 and tb["taux"] >= tj["taux"])
            sortie[k][s] = {"jeu": tj, "premier_cout": tb, "paire": paire, "mention": mention}
    return sortie


def citation_diffusion(entrees: dict, phrase, ac: dict) -> dict:
    """Section 10.3."""
    tete = en_tete_de_these(entrees)
    mentions = [{"jeu": k, "sous_ensemble": s, "phrase": cl.MENTION} for k in sorted(ac) for s in cl.SOUS_ENSEMBLES if ac[k][s]["mention"]]
    texte = " ".join([tete.rstrip(" "), f"{phrase}.", br.CLAUSE_DU_PREMIER_COUT]) if phrase is not None else None
    return {"en_tete": tete, "phrase_d_origine": phrase, "regles": list(cl.REGLES_10_6), "mentions": mentions,
            "clause": br.CLAUSE_DU_PREMIER_COUT, "texte": texte}


def lecture_2_v5(entrees: dict, lecture_1: dict, graines: dict, config: dict, identite: dict, textes: list, fiches: dict,
                 bases=None) -> tuple[dict, dict]:
    """Section 7.4, points 6 et 7 : résultat qui décide (toutes ses clés), blocs rapportés, citation. `lecture_1` : rendu de
    `lecture_v1.exiger_lecture_1_consignee` (empreinte, contenu). `bases` : essais seulement (refusé en mode réel par le module
    d'origine)."""
    o = entrees["oracle"]
    al = cl.ALIAS["lecture_2"]
    resultat, mots = lv.lecture_2(sorties_d_origine(entrees, o, ev.alias(graines, al["principal"]), config, textes=textes, fiches=fiches),
                                  lecture_1["contenu"], bases)
    resultat["lecture_1"]["sha256"] = lecture_1["sha256"]
    ecart = ecart_premier_cout(entrees)
    base = base_premier_cout(entrees, resultat["plis"], config["lecture_2"], ev.alias(graines, al["premier_cout"]))
    ac = a_cote(resultat["jeux"], base)
    _ajouter(resultat, {
        "forme": cl.FORME_2, "cloisonnement": cl.CLOISONNEMENT, "ordre_du_temps": identite["ordre_du_temps"],
        "course_lue": course_lue(entrees), "oracle_de_la_regle": oracle_de_la_regle(entrees, complet=False),
        "entrees": dict(entrees["empreintes"]), "lecture": identite["lecture"], "audit_de_la_lecture_1": identite["audit_de_la_lecture_1"],
        "decodage": identite["decodage"], "ecart_premier_cout_par_condition": ecart, "base_premier_cout_contre_les_suivants": base,
        "a_cote_de_chaque_taux": ac, "note_juge": cl.NOTE_JUGE, "note_reperes": cl.NOTE_REPERES,
        "citation": citation_diffusion(entrees, resultat["phrase"], ac)})
    _ajouter(mots, {"course_lue": course_lue(entrees), "cloisonnement": cl.CLOISONNEMENT, "run_id": identite["lecture"]["run_id"]})
    return resultat, mots


# ------------------------------------------------------------------------------------------------------------------------------
# Configuration du manifeste d'une lecture (section 8)
# ------------------------------------------------------------------------------------------------------------------------------
def configuration_du_manifeste(numero: int, entrees: dict, config: dict, specification: str, modules: dict) -> dict:
    return {"version": cl.VERSION, "avertissement": cl.AVERTISSEMENT, "mode": entrees["mode"], "lecture": numero,
            "course": entrees["run_id"], "etalonnage": entrees["etalonnage"], "oracle_de_la_regle": entrees["oracle"],
            "accord": cl.ACCORD, "specification": {"chemin": cl.SPECIFICATION["chemin"], "sha256": specification},
            "constantes": config, "entrees": dict(entrees["empreintes"]), "modules": dict(modules), "entropie": entrees["entropie"],
            "prefixe": entrees["prefixe"]}
