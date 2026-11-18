#!/usr/bin/env python3
"""Fusionne les entrees brutes des quatre voies : dedoublonnage, table fusionnee (JSON), matrice d'incidence.

Usage : python -I fusionner.py brutes.json fusion.json
Lecture seule des entrees ; rien n'est execute. Regles manuelles ecrites ci-dessous, chacune avec sa raison.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cles import RE_ARXIV, cles, norm_titre, norm_url, regroupe  # noqa: E402

E = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))

# ------------------------------------------------------------------ regles manuelles
# (a) rangees groupees de la voie « litterature grise » eclatees en leurs composants
eclatees = []
gardees = []
for e in E:
    t = e["titre"]
    if e["voie"] == "grise" and t.startswith("Autres articles arXiv croisés en chemin"):
        noms = dict(re.findall(r"(\d{4}\.\d{5}) \(([^)]+)\)", t))
        for a in RE_ARXIV.findall(t):
            f = dict(e)
            f.update(titre=noms.get(a, f"(titre non relevé par la voie grise) arXiv {a}"),
                     adresse=f"https://arxiv.org/abs/{a}", auteurs="", date="",
                     fait="(croisé en chemin par la voie grise, non lu)", touche="non évalué par la voie grise",
                     mesure="inconnu", lu="titre seul", eclate="rangée 61 de la voie grise")
            eclatees.append(f)
        continue  # « RSI-top » et « LMCA » : non identifiables, laisses de cote (dit dans la table)
    if e["voie"] == "grise" and t.startswith("SakanaAI/AI-Scientist (v1) et AI-Scientist-v2"):
        for a, nom, d in (("2408.06292", "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery", "2024-08-12"),
                          ("2504.08066", "The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search", "2025-04-08")):
            f = dict(e)
            f.update(titre=nom + " (dépôt SakanaAI)", adresse=f"https://arxiv.org/abs/{a}", date=d,
                     autre_adresse="https://github.com/SakanaAI/AI-Scientist", eclate="rangée 53 de la voie grise")
            eclatees.append(f)
        continue
    if e["voie"] == "grise" and t.startswith("SakanaAI/ShinkaEvolve ; google-deepmind/alphaevolve"):
        f = dict(e)
        f.update(titre="SakanaAI/ShinkaEvolve (dépôt de code)", adresse="https://github.com/SakanaAI/ShinkaEvolve",
                 date="2025-09-17", auteurs="Sakana AI", eclate="rangée 54 de la voie grise")
        eclatees.append(f)
        f = dict(e)
        f.update(titre="AlphaEvolve: A coding agent for scientific and algorithmic discovery (dépôt google-deepmind/alphaevolve)",
                 adresse="https://arxiv.org/abs/2506.13131", date="2026-11-04 (création du dépôt)", auteurs="Google DeepMind",
                 autre_adresse="https://github.com/google-deepmind/alphaevolve", eclate="rangée 54 de la voie grise")
        eclatees.append(f)
        continue
    gardees.append(e)
E = gardees + eclatees

# (b) fusions manuelles : meme travail sous deux titres ou deux adresses que les cles ne rapprochent pas
FUSIONS = [
    ("url:alignment.anthropic.com/2026/automated-alignment-researchers", "arxiv:2608.28945",
     "sûr", "même travail d'Anthropic (Chen Yueh-Han, Wen, Kirchner), titre du billet et titre arXiv différents"),
    ("url:deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research", "arxiv:2502.18864",
     "sûr", "billet d'annonce de 2026 du système dont la prépublication est arXiv 2502.18864 (dit par la voie grise)"),
    ("arxiv:2609.17846", "openreview:mT2tgyAsek",
     "sûr", "« PrimeScientist » sur arXiv, « Prime Scientist » sur OpenReview, même sous-titre"),
    ("arxiv:2610.29303", "openreview:udUQaoRekf",
     "sûr", "« ExpEvolve » : le titre OpenReview ajoute « Evolutionary »"),
    ("arxiv:2607.27687", "openreview:GEkyUI7v7a",
     "sûr", "« Rehearse » : le titre arXiv ajoute « Self-Improving »"),
    ("arxiv:2607.08758", "openreview:JN4DdAjmHA",
     "sûr", "« Ideas Have Genomes » : sous-titres presque identiques"),
    ("url:github.com/aiming-lab/autoresearchclaw", "openreview:sJ5JnQwRos",
     "sûr", "dépôt de code et soumission OpenReview du même système « AutoResearchClaw », tous deux dans la voie grise"),
    ("arxiv:2610.02945", "openreview:LICX3CIWtn",
     "probable", "titres proches (« Continual Graph Memory … » mathématiques), même période ; non vérifié sur source"),
    ("arxiv:2609.39360", "openreview:O51KJl9vTB",
     "probable", "titres proches (« Autoresearch in Mixed-Integer … Programming »), même mois ; non vérifié sur source"),
]
# (c) rapprochements possibles laisses separes (a verifier)
POSSIBLES = [
    ("arxiv:2605.08956", "openreview:EWbCCYsR9M",
     "« Agentic AI Scientists Are Not Built For Autonomous Scientific Discovery » (arXiv, 9 mai 2026) et « Position: AI Scientists Are Not Yet Ready for Open-Ended and Fully Autonomous Scientific Discovery » (ACL ARR, 26 mai 2026) : peut-être le même texte de position, titres trop différents pour fusionner sans lecture"),
    ("url:bespokelabs.ai/blog/how-models-explore-ideas", "url:benchmarks.bespokelabs.ai/autoresearchexam",
     "« How models explore ideas » et « Introducing AutoResearchExam » : deux billets du même laboratoire sur le même banc ; gardés séparés (objets différents : analyse des bassins d'idées contre présentation du banc)"),
]

K = [cles(e) for e in E]
for i, e in enumerate(E):
    if e.get("autre_adresse") and not e.get("eclate"):
        K[i].add(norm_url(e["autre_adresse"]))
    # les rangees eclatees ne se rapprochent que par leur identifiant, pas par un titre fabrique
    if e.get("eclate"):
        K[i] = {k for k in K[i] if not k.startswith("titre:")}
index0 = defaultdict(list)
for i, ks in enumerate(K):
    for k in ks:
        index0[k].append(i)
fusions_appliquees = []
for a, b, surete, raison in FUSIONS:
    if index0.get(a) and index0.get(b):
        lien = "manuel:" + a + "=" + b
        for i in index0[a] + index0[b]:
            K[i].add(lien)
        fusions_appliquees.append((a, b, surete, raison))
    else:
        print("FUSION MANUELLE SANS OBJET", a, bool(index0.get(a)), b, bool(index0.get(b)))

G, index = regroupe(E, K)

# ------------------------------------------------------------------ champs fusionnes
RANG_LU = {"texte entier": 3, "résumé ou page": 2, "titre seul": 1}
RANG_MES = {"mesuré avec données publiées": 4, "mesuré sans données publiées": 3, "affirmé sans mesure": 2, "inconnu": 1}
ORDRE = ["mots-cles", "citations", "grise", "adverse"]
NOM = {"mots-cles": "mots-clés", "citations": "citations", "grise": "grise", "adverse": "adverse"}


def date_iso(d):
    if not d or "consulté" in d:
        return None
    m = re.search(r"(\d{4})-(\d{2})(?:-(\d{2}))?", d)
    if m:
        return m.group(0)
    m = re.search(r"\b(20\d{2})\b", d)
    return m.group(1) if m else None


def cle_date(s):
    # tri : une date incomplete se range a la fin de sa periode
    p = s.split("-")
    return (int(p[0]), int(p[1]) if len(p) > 1 else 13, int(p[2]) if len(p) > 2 else 32)


travaux = []
for g in G:
    es = [E[i] for i in g]
    ks = set().union(*(K[i] for i in g))
    ax = sorted(k[6:] for k in ks if k.startswith("arxiv:"))
    annote = sorted({e["voie"] for e in es if e["niveau"] == "annote"}, key=ORDRE.index)
    annexe = any(e["niveau"] == "annexe" for e in es)
    # titre et adresse de reference : entree a adresse arXiv d'abord, sinon la mieux lue
    def prio(e):
        return (0 if "arxiv.org/abs" in e["adresse"] and not e.get("eclate") else 1,
                -RANG_LU.get(e["lu"], 0), ORDRE.index(e["voie"]))
    ref = sorted(es, key=prio)[0]
    titre = re.sub(r"\s*\[[^\]]*\]\s*$", "", ref["titre"]).strip()
    adresse = ref["adresse"]
    if ax and "arxiv.org" not in adresse:
        adresse_ref = f"https://arxiv.org/abs/{ax[0]}"
    else:
        adresse_ref = adresse
    autres = sorted({e["adresse"] for e in es if e["adresse"].startswith("http")} |
                    {e["autre_adresse"] for e in es if e.get("autre_adresse")} - {adresse_ref})
    autres = [a for a in autres if a != adresse_ref]
    autres_titres = sorted({re.sub(r"\s+", " ", e["titre"]) for e in es
                            if norm_titre(e["titre"]) != norm_titre(ref["titre"]) and not e.get("eclate")})
    # dates
    dates = {}
    for e in es:
        d = date_iso(e["date"])
        if d:
            dates.setdefault(d, []).append(NOM[e["voie"]])
    if dates:
        dmin = min(dates, key=cle_date)
        divergences = "; ".join(f"{d} ({', '.join(sorted(set(v)))})" for d, v in sorted(dates.items(), key=lambda x: cle_date(x[0]))) if len(dates) > 1 else ""
    else:
        dmin, divergences = "", ""
    brut_dates = "; ".join(sorted({f"{NOM[e['voie']]} : {e['date']}" for e in es if e["date"] and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", e["date"])}))
    # nature
    natures = Counter(e["nature"] for e in es)
    if ax:
        nature = "article arXiv"
        autres_nat = sorted(n for n in natures if n != "article arXiv")
        if autres_nat:
            nature += " (aussi : " + ", ".join(autres_nat) + ")"
    else:
        nature = natures.most_common(1)[0][0]
    # ce qu'il fait : l'entree la mieux lue, puis la plus longue
    meill = sorted([e for e in es], key=lambda e: (-RANG_LU.get(e["lu"], 0), 0 if "PDF" in e["fait"] else 1, -len(e["fait"])))[0]
    fait = meill["fait"] + f" [d'après la voie {NOM[meill['voie']]}]"
    # mesure
    mes = sorted({e["mesure"] for e in es if e["niveau"] == "annote"}, key=lambda m: -RANG_MES.get(m, 0))
    if not mes:
        mesure = "inconnu"
    else:
        mesure = mes[0]
        connus = [m for m in mes if m != "inconnu"]
        if len(connus) > 1:
            mesure += " (voies discordantes : " + " / ".join(
                f"{NOM[e['voie']]} : {e['mesure']}" for e in es if e["niveau"] == "annote" and e["mesure"] != "inconnu") + ")"
    # lu
    lu_e = sorted(es, key=lambda e: (-RANG_LU.get(e["lu"], 0), 0 if "PDF" in e["fait"] else 1))[0]
    lu = lu_e["lu"] + f" ({NOM[lu_e['voie']]})"
    # touche, par voie
    touche = " ‖ ".join(f"{NOM[e['voie']]} : {e['touche']}" for e in sorted(es, key=lambda e: ORDRE.index(e["voie"]))
                        if e["niveau"] == "annote" and e["touche"])
    adv = next((e["touche"] for e in es if e["voie"] == "adverse"), "")
    verdict = []
    if re.search(r"\bPREND\b|: prend|\bprend\b", adv):
        verdict.append("prend")
    if re.search(r"CONTREDIT|contredit", adv):
        verdict.append("contredit")
    if re.search(r"avoisine", adv):
        verdict.append("avoisine")
    auteurs = sorted((e["auteurs"] for e in es if e["auteurs"] and e["auteurs"] not in ("inconnu", "divers", "non relevés")), key=len)
    auteurs = auteurs[-1] if auteurs else ""
    fenetre = None
    if dmin:
        fenetre = cle_date(dmin)[:2] >= (2026, 5) if len(dmin) > 4 else (int(dmin) >= 2026 and None)
    if ax and fenetre is None:
        fenetre = ax[0][:4] >= "2605"
    travaux.append(dict(
        titre=titre, adresse=adresse_ref, autres_adresses=autres, autres_titres=autres_titres, arxiv=ax,
        voies=annote, annexe_mots_cles=annexe, date=dmin, dates_divergentes=divergences, dates_brutes=brut_dates,
        nature=nature, auteurs=auteurs, fait=fait, mesure=mesure, lu=lu, touche=touche, verdict_adverse=verdict,
        fenetre=fenetre, cles=sorted(ks),
        sources=[f"{e['fichier']}:{e['ligne']}" for e in es],
        eclate=sorted({e["eclate"] for e in es if e.get("eclate")}),
    ))

# controle : aucun groupe ne reunit deux identifiants arXiv sans regle manuelle
for t in travaux:
    if len(t["arxiv"]) > 1:
        print("GROUPE A PLUSIEURS IDENTIFIANTS ARXIV", t["arxiv"], t["titre"])

Path(sys.argv[2]).write_text(json.dumps(dict(
    travaux=travaux, fusions_manuelles=fusions_appliquees, possibles=POSSIBLES,
    n_entrees_brutes=len(gardees) + 3, n_entrees_apres_eclatement=len(E)), ensure_ascii=False, indent=1), encoding="utf-8")

ann = [t for t in travaux if t["voies"]]
print("entrees apres eclatement", len(E), "groupes", len(travaux))
print("travaux annotes par au moins une voie :", len(ann), "| annexe seule :", len(travaux) - len(ann))
print("par nombre de voies :", Counter(len(t["voies"]) for t in ann))
print("histoires :", Counter("".join("1" if v in t["voies"] else "0" for v in ORDRE) for t in ann).most_common())
