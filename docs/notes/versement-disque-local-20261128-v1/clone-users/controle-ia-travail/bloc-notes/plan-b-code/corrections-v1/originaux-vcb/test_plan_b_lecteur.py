"""Lecteur du plan B des juges de T0.5 (`lire_requalification`) : équivalence avec les fonctions gelées sur un run jouet ;
chaque ligne des tables A, B, C, D et E sur fichiers synthétiques ; recouvrements de lignes listés dans « Tests » ;
statut de PB1 à PB10 ; gardes de lecture, chacune sur un cas sain et sur un artefact (R5) ; décisions R-249 : grandeur
illisible au palier du chemin (D-1), sonde d'audit fausse à la table A (D-3), compte des occurrences lues suivies d'un
chiffre (D-5), annexe A du texte scellé (D-6), gardes d'entrée (D-9), décalages réellement passés (D-10), tirage des lots
du rejeu recalculé (D-14).

Les fichiers du run de l'étape sont fabriqués au format qu'écrit le lanceur `requalifier_juges` (docstring du lecteur) :
les rapports de garde et de rejeu sont faits par les fonctions gelées du harnais (`ecart_equivalence`,
`ecart_decale_zone_generee`, `profil_ecarts`, `sonde_de_comparaison`) sur des activations synthétiques, puis mis en
forme par les fonctions mêmes du lanceur (`juges_simplifies.rapport_de_la_rangee`, `requalifier_juges._rangee` et
`reproduction`). Aucun modèle, aucun réseau. Le lecteur sur les fichiers d'un vrai run jouet du lanceur :
`test_plan_b_integration.py`."""
from __future__ import annotations

import copy
import hashlib
import json
import math
import shutil
from pathlib import Path

import numpy as np
import pytest

from conftest import committer
from controle_ia.environnements import juges_simplifies as js
from controle_ia.environnements import lire_pilote as lp
from controle_ia.environnements import lire_requalification as lr
from controle_ia.environnements import requalifier_juges as rq
from controle_ia.environnements.analyse_pilote import difference_appariee
from controle_ia.environnements.rubrique_simplifiee import lire_reponse_rs1
from controle_ia.gardes import GardeArret
from controle_ia.harnais.activations import (ecart_decale_zone_generee, ecart_equivalence, profil_ecarts,
                                             sonde_de_comparaison)
from controle_ia.harnais.episode import bilan_controle_negatif
from controle_ia.manifeste import creer_manifeste, ecrire_resultat, generateur, graines, verifier_resultat
from controle_ia.scellement import empreinte, sceller
from test_lire_notations_pilote import (NOTATIONS, _notations_de, _pilote_complet_et_pilote_arrete, _prereg_notations,
                                        _run_des_notations)
from test_lire_pilote import ANALYSE, REEL, RUN
from test_plan_b_rubrique_simplifiee import annexe_a_comme_au_texte

PLANB = "20261020-100000-t05-planb-jouet"
LECTURE = "20261020-120000-t05-lecture-planb-jouet"
ENTROPIE_PLANB = 2718281828459045
JUGES = ("8B", "3B")
CRITERES = ("SPECIFICITY", "COVERAGE", "RIGOR", "FEASIBILITY")
REGLAGES = {"algorithmes_deterministes": True, "precision_produits_simple": "highest", "tf32_produits": False,
            "tf32_cudnn": False, "reduction_reduite_bf16": False, "reduction_reduite_fp16": False}


@pytest.fixture(autouse=True)
def _code_du_vrai_depot(monkeypatch):
    """Le code est importé du vrai dépôt, pas du dépôt jetable : garde d'import neutralisée (éprouvée par les tests de
    `lire_pilote`)."""
    monkeypatch.setattr(lp, "exiger_code_importe_sous", lambda racine: None)


# --- Rapports synthétiques, faits par les fonctions gelées -------------------------------------------------------------

def _rapport(episode: str, lc: int = 40, ng: int = 20, tol: float = 0.2, stat: str = "q99", ctx=1e-3, gen=1e-3,
             graine: int = 0, repetee: bool = False, largeur: int = 8) -> dict:
    """Rapport de `jouer_episodes` (une comparaison « 0,0 ») sur des activations synthétiques : g = p × (1 + ε), soit un
    écart relatif ε par jeton, ε propre au contexte (`ctx`) et à la zone générée (`gen`), par couche si c'est un
    dictionnaire. `repetee` : zone générée faite d'un seul vecteur répété (jetons répétés : le décalage d'un jeton n'y
    change rien). Clés de couche en texte, comme au fichier scellé."""
    rng = np.random.default_rng(graine)
    ap, ag = {}, {}
    for c in (7, 15, 23):
        e_c = ctx[c] if isinstance(ctx, dict) else ctx
        e_g = gen[c] if isinstance(gen, dict) else gen
        p = rng.normal(size=(lc + ng, largeur)).astype(np.float32)
        if repetee:
            p[lc - 1:] = p[lc - 1]
        f = np.concatenate([np.full(lc, 1 + e_c), np.full(ng, 1 + e_g)])[:, None]
        ap[c], ag[c] = p, (p.astype(np.float64) * f).astype(np.float32)
    k = "0,0"
    r = {"episode": episode, "tolerance": tol, "statistique": stat, "ecarts": {k: ecart_equivalence(ag, ap)},
         "ecarts_q99": {k: ecart_equivalence(ag, ap, quantile=0.99)},
         "controle_negatif_zone_generee": {k: ecart_decale_zone_generee(ag, ap, lc, tol)},
         "profils": {k: profil_ecarts(ag, ap, lc)}, "longueurs_contexte": {k: lc}, "positions_capturees": {k: lc + ng},
         "lignes": {k: {"ligne": 0, "taille_lot": 8, "remplissage": 0, "finie_avant": False}},
         "empreintes_capture": {k: "0" * 64}, "sondes": {k: sonde_de_comparaison(ag, ap)}}
    return json.loads(json.dumps(r))


def _cles(j: str, n: int, debut: int = 0) -> list[str]:
    return [f"juge-{j}/2601.{k:05d}v1/e0/passe-0" for k in range(debut, debut + n)]


def _garde(r: dict) -> dict:
    """Rapport d'une rangée tel que l'écrit le lanceur (`juges_simplifies.rapport_de_la_rangee`)."""
    return js.rapport_de_la_rangee(r)


def _ligne(cle: str, rapport: dict, reponse: str = "x", jetons: int = 60, tronquee: bool = False,
           contexte: int = 300) -> dict:
    """Ligne de `jouer_lot_de_notations` (notation, rapport mis en forme, longueur de la transcription)."""
    return {"notation": {"cle": cle, "jetons_contexte": contexte, "jetons_reponse": jetons, "tronquee": tronquee,
                         "reponse": reponse},
            "rapport": _garde(rapport), "jetons_transcription": contexte + jetons}


def _repere(q99: float = 0.05) -> dict:
    return {c: {"jetons": 1000, "q50": q99 / 5, "q99": q99, "max": 2 * q99} for c in lr.COUCHES}


H4_PAR_DEFAUT = {"reponse": "x", "jetons_reponse": 60, "tronquee": False}


def _demi(cles: list[str], h4: dict | None = None, gen=1e-3, ctx=1e-3, scellees: dict | None = None, **k) -> dict:
    """Fichier `rejeu-<J>-demi.json` : 16 rangées de L1 et L2, faites par `_rangee` du lanceur ; réponses rejouées
    égales à `h4` ; reproduction consignée comme le lanceur la calcule, contre `scellees` (par défaut `h4`)."""
    rangees = []
    scellees = h4 if scellees is None else scellees
    for i, c in enumerate(cles):
        n, s = (h4 or {}).get(c, H4_PAR_DEFAUT), (scellees or {}).get(c, H4_PAR_DEFAUT)
        ligne = _ligne(c, _rapport(c, lc=300, ng=60, gen=gen, ctx=ctx, graine=100 + i, **k), n["reponse"],
                       n["jetons_reponse"], n["tronquee"])
        r = rq._rangee("L1" if i < 8 else "L2", i % 8, ligne, {"cle_pilote": c})
        r["reproduction"] = rq.reproduction(ligne["notation"], {"cle": c, **{x: s[x] for x in H4_PAR_DEFAUT}})
        rangees.append(r)
    return {"rangees": rangees}


def _simple(j: str, cles: list[str], cles_d1: list[str], gen=1e-4, ctx=1e-4, ancrage=1e-4, repere=0.05,
            d1_gen=0.05, d1_ctx=1e-4, d1_ng=40, longue: int | None = None, **k) -> dict:
    """Fichier `rejeu-<J>-simple.json` au format du lanceur : réglages relus, repère, ancrage, 16 rangées du chemin (la
    première couvre le seuil de J, rangée tronquée : `max_nouveaux − 1` positions générées comparées), 8 rangées de
    D1 ; rangées faites par `_rangee` du lanceur."""
    longue = lr.SEUILS_COUVERTURE[j] if longue is None else longue
    chemin = []
    for i, c in enumerate(cles):
        ng = longue - 1 if i == 0 else 60
        rapport = _rapport(c, lc=300, ng=ng, tol=3e-3, stat="max", gen=gen, ctx=ctx, graine=200 + i, **k)
        ligne = _ligne(c, rapport, jetons=ng + 1 if i == 0 else ng, tronquee=i == 0)
        chemin.append(rq._rangee("L1" if i < 8 else "L2", i % 8, ligne, {"cle_pilote": c}))
    d1 = [rq._rangee("L3", i, _ligne(c, _rapport(c, lc=300, ng=d1_ng, tol=3e-3, stat="max", gen=d1_gen, ctx=d1_ctx,
                                                 graine=300 + i), jetons=d1_ng), {"cle_pilote": c})
          for i, c in enumerate(cles_d1)]
    anc = ancrage if isinstance(ancrage, dict) else {c: ancrage for c in lr.COUCHES}
    return {"reglages_relus": dict(REGLAGES), "type_des_poids": "torch.float32",
            "repere": {"par_couche": _repere(repere),
                       "par_rangee": [{"lot": "L1" if i < 8 else "L2", "cle": c, "positions": 360,
                                       "par_couche": _repere(repere)} for i, c in enumerate(cles)]},
            "ancrage": {"lot": "L1", "cle": cles[0], "positions": 300 + longue,
                        "par_couche": {str(c): v for c, v in anc.items()}},
            "chemin": {"tolerance": 3e-3, "statistique": "max", "decalages_passes": {"L1": 0, "L2": 0},
                       "rangees": chemin},
            "d1": {"lot": "L3", "decalage_positions": 1, "decalages_passes": {"L3": 1}, "rangees": d1}}


def _temoins(tronquees: dict | None = None, impossible: dict | None = None, taux: dict | None = None) -> dict:
    """Fichier `temoins.json` au format du lanceur : par juge, deux appels (L1, L2) de 8 rangées, l'appel L2 « témoin
    impossible » sur demande ; taux H.4 consigné, (tronquées, notations), par défaut ceux du texte."""
    t = {"8B": 5, "3B": 1, **(tronquees or {})}
    tx = {"8B": (60, 180), "3B": (9, 180), **(taux or {})}
    juges = {}
    for j in JUGES:
        lignes = [{"cle": c, "jetons_contexte": 2000, "jetons_generes": 3072 if i < t[j] else 80, "tronquee": i < t[j],
                   "complete": i >= t[j]} for i, c in enumerate(_cles(j, 16))]
        appels = [{"lot": "L1", "cle_graine": f"rejeu/{j}/temoin/L1", "graine": 1, "statut": "fait",
                   "rangees": lignes[:8]}]
        if (impossible or {}).get(j):
            appels.append({"lot": "L2", "cle_graine": f"rejeu/{j}/temoin/L2", "graine": 2,
                           "statut": "témoin impossible", "motif": "déterminisme"})
        else:
            appels.append({"lot": "L2", "cle_graine": f"rejeu/{j}/temoin/L2", "graine": 2, "statut": "fait",
                           "rangees": lignes[8:]})
        juges[j] = {"appels": appels, "taux_h4": {"tronquees": tx[j][0], "notations": tx[j][1]}}
    return {"juges": juges, "noyau": "défaut de la bibliothèque", "noyaux_permis": None}


# --- Run jouet complet --------------------------------------------------------------------------------------------

def _h4(a: Path, j: str) -> list[dict]:
    """Notations H.4 du run jouet des notations, longueurs et troncatures choisies pour que les seuils de couverture
    recalculés soient ceux du texte (8B : 3 072 ; 3B : 983) ; taux de troncature 60/150 et 9/150. Les 9 réponses
    tronquées du 3B sont une sur sept (k = 0, 7, …, 56) : le cadre du rejeu du 3B compte 8 lots de 8 (D-14)."""
    n = copy.deepcopy(_notations_de(a, j))
    for k, x in enumerate(n[:60]):
        x["tronquee"] = j == "8B" or k % 7 == 0
        x["jetons_reponse"] = 3072 if x["tronquee"] else 983
    return n


def _lots(h4: dict, j: str) -> tuple[list[str], list[str], dict]:
    """Lots du rejeu de J tirés comme le lanceur les tire, par ses propres fonctions (`cadre_du_rejeu`, `tirer_lots`,
    clé `rejeu/<J>/lots` de l'entropie de l'étape) : clés de L1 puis L2, clés de L3, tirage consigné."""
    cadre = rq.cadre_du_rejeu(h4[j], 8, 3072)
    cle = f"rejeu/{j}/lots"
    l1, l2, l3 = rq.tirer_lots(cadre, generateur(graines([cle], ENTROPIE_PLANB)[cle]))

    def cles(k):
        return [x["cle"] for x in h4[j][k * 8:(k + 1) * 8]]

    return cles(l1) + cles(l2), cles(l3), {"cadre": cadre, "L1": l1, "L2": l2, "L3": l3, "cle": cle}


def _simple_du_run(h4: dict, j: str, **k) -> dict:
    """`rejeu-<J>-simple.json` sur les lots tirés, avec son tirage consigné."""
    cles, d1, tirage = _lots(h4, j)
    return {**_simple(j, cles, d1, **k), "tirage": tirage}


def _rs1(h4: list[dict], j: str, graine: int = 0, tronquees=(), meme_somme: bool = False) -> list[dict]:
    """Notations RS1 au format de `noter_ensembles` : les quatre notes reprises des notes H.4 jouets (même structure de
    tâche, de génération et de juge), réponses RS1 conformes, lues par `lire_reponse_rs1`."""
    rng = np.random.default_rng(graine)
    sortie = []
    for k, x in enumerate(h4):
        notes = {c: (2 if meme_somme else x["notes"][c]) for c in CRITERES}
        texte = "\n".join(f"{c}: {v}" for c, v in notes.items()) + f"\nJUSTIFICATION: set {k}, {rng.random():.6f}."
        t = k in tronquees
        r = lire_reponse_rs1(texte, t)
        sortie.append({"cle": x["cle"].replace(f"juge-{j}/", f"juge-RS1-{j}/"), "variante": "RS1",
                       "jetons_contexte": 2000 + k, "ensemble_sha256": x["ensemble_sha256"],
                       "jetons_reponse": 3072 if t else 60 + k % 40, "tronquee": t, "notes": r["notes"],
                       "anomalies": r["anomalies"], "score": r["score"], "reponse": texte,
                       "complete_sans_troncature": r["complete_sans_troncature"], "lecture_rs1": r["lecture"]})
    return sortie


def _fichier_notations(rs1: list[dict], **k) -> dict:
    """Fichier `notations-RS1-<J>-decisives.json` au format du lanceur : notations, puis un rapport de rangée par
    notation (`{"cle": …, **rapport_de_la_rangee(…)}`, comme `_requalifier`)."""
    return {"variante": "RS1", "notations": rs1,
            "garde": {"tolerance": 0.2, "statistique": "q99", "couches": [7, 15, 23],
                      "rapports": [{"cle": n["cle"], **_garde(_rapport(n["cle"], graine=i, **k))}
                                   for i, n in enumerate(rs1)]},
            "descriptifs": {"duree_s": 1.0, "memoire_pic_gio": 0.1}, "noyaux_permis": None}


def _fichiers(h4: dict, sans: tuple = (), **par_fichier) -> dict:
    """Les sept fichiers de phase d'un run sain (faits une fois, puis copiés), sauf `sans` ; `par_fichier` remplace un
    fichier par son contenu."""
    if "fichiers" not in _BASE:
        f = {}
        for j in JUGES:
            f[f"notations-RS1-{j}-decisives"] = _fichier_notations(_rs1(h4[j], j, graine=1 if j == "8B" else 2))
            cles, d1, tirage = _lots(h4, j)                  # lots tirés comme au lanceur (D-14)
            f[f"rejeu-{j}-demi"] = {**_demi(cles, {x["cle"]: x for x in h4[j]}), "tirage": tirage,
                                    "decalages_passes": {"L1": 0, "L2": 0}}
            f[f"rejeu-{j}-simple"] = {**_simple(j, cles, d1), "tirage": tirage}
        f["temoins"] = _temoins(taux={j: (sum(bool(x["tronquee"]) for x in h4[j]), len(h4[j])) for j in JUGES})
        _BASE["fichiers"] = f
    f = {**copy.deepcopy(_BASE["fichiers"]), **par_fichier}
    return {k: v for k, v in f.items() if k not in sans}


_BASE: dict = {}


def _base(tmp_path_factory):
    """Pilote jouet arrêté (première analyse faite), son run des notations H.4, les modules gelés et neufs versés et un
    préenregistrement de test scellé, committés une fois par processus (`COMMIT_GELES` du dépôt jetable : ce commit) ;
    puis une copie par test."""
    if "depot" not in _BASE:
        import subprocess
        a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
        h4 = {j: _h4(a, j) for j in JUGES}
        _run_des_notations(b, h4)
        for m in lr.MODULES_GELES + lr.MODULES_PLANB:
            (b / m).parent.mkdir(parents=True, exist_ok=True)
            if (REEL / m).is_file():
                shutil.copy(REEL / m, b / m)
            else:   # module neuf écrit en parallèle et pas encore versé : la garde ne lit que son égalité au commit
                (b / m).write_text(f"# {m} : module du run de test\n", encoding="utf-8")
        prereg = _prereg_notations(b, "prereg-planb.md")                                # committé avec les modules
        # annexe A comme au texte, puis rescellé et committé : l'invite qu'elle porte est RS1.txt (D-6)
        chemin = b / prereg
        chemin.write_text(chemin.read_text(encoding="utf-8") + "\n" + annexe_a_comme_au_texte(), encoding="utf-8")
        Path(str(chemin) + ".sha256").unlink()
        sceller(chemin)
        committer(b)
        commit = subprocess.run(["git", "-C", str(b), "rev-parse", "HEAD"], capture_output=True, text=True,
                                check=True).stdout.strip()
        _BASE.update(depot=b, h4=h4, commit=commit, prereg=prereg)
    d = tmp_path_factory.mktemp("planb")
    shutil.copytree(_BASE["depot"], d, dirs_exist_ok=True)
    return d, copy.deepcopy(_BASE["h4"])


def _config(depot: Path, **k) -> dict:
    return {"mode": "reel", "run_pilote": RUN, "run_notations": NOTATIONS, "max_nouveaux_juge": 3072, "lot_juge": 8,
            "manifeste_pilote_sha256": empreinte(depot / "runs" / RUN / "manifeste.json"),
            "juges": [{"nom": "8B", "meme_modele_que_agent": True}, {"nom": "3B", "meme_modele_que_agent": False}],
            **lr.CONSTANTES_CONFIG, **k}


def _run_planb(depot: Path, monkeypatch, fichiers: dict, issue: str | None = "resume", statuts: dict | None = None,
               config: dict | None = None, prereg: str | None = None) -> str:
    """Run de l'étape fabriqué à la main dans une copie de `_base`, sous son préenregistrement de test (ou `prereg`) :
    manifeste décisif, fichiers de phase, puis l'issue (`resume`, `arret`, les deux ou aucune) avec le statut de chaque
    fichier de phase, comme le lanceur l'écrit (`fichiers` ; « écrit » pour un fichier écrit, sauf `statuts`)."""
    monkeypatch.setattr(lr, "COMMIT_GELES", _BASE["commit"])
    p = prereg or _BASE["prereg"]
    chemin, _ = creer_manifeste(depot, PLANB, config or _config(depot), ["juge-RS1-8B/x/e0/passe-0", "rejeu/8B/lots"],
                                entropie=ENTROPIE_PLANB, decisif=True, prereg=str(depot / p))
    for nom, contenu in fichiers.items():
        ecrire_resultat(depot, chemin, nom, contenu)
    ecrits = {nom: "écrit" for nom in fichiers}
    ecrits.update(statuts or {})
    for nom in {"resume": ["resume"], "arret": ["arret"], "les-deux": ["resume", "arret"], None: []}[issue]:
        corps = ({"fichiers": ecrits} if nom == "resume"
                 else {"etape": "rejeu du 8B", "motif": "GardeArret: essai", "partiel": {"fichiers": ecrits}})
        ecrire_resultat(depot, chemin, nom, corps)
    committer(depot)
    return p


def _lire(depot: Path, p: str, **k):
    return lr.lire_requalification(depot, RUN, NOTATIONS, PLANB, ANALYSE, depot / "taches.json", LECTURE,
                                   prereg=k.pop("prereg", str(depot / p)), **k)


def test_equivalence_avec_les_fonctions_gelees(tmp_path_factory, monkeypatch):
    """Run jouet sain : la requalification, la différence appariée, les déclencheurs propres aux juges et les relectures
    sont ceux des fonctions gelées appelées directement avec les graines de la lecture (entropie de l'étape) ; le
    contrôle négatif de la garde, sans rangée courte, est celui de `bilan_controle_negatif`."""
    depot, h4 = _base(tmp_path_factory)
    f = _fichiers(h4)
    p = _run_planb(depot, monkeypatch, f)
    lecture = _lire(depot, p)
    g = graines(lr.cles_lecture(), ENTROPIE_PLANB)
    pil = lp.charger_pilote(depot, RUN, depot / "taches.json")
    taches, ensembles = sorted(pil["taches"]), lp.empreintes_des_ensembles(pil["episodes"]["fiches"])
    s = lp._serialisable
    al = {}
    for j in JUGES:
        notations = f[f"notations-RS1-{j}-decisives"]["notations"]
        al[j] = lp.notes_alignees(notations, f"RS1-{j}", taches, ensembles)
        attendu = lp.lecture_juge(al[j], generateur(g[f"analyse/bootstrap-parts-RS1-{j}"]))
        assert s(lecture["requalification"][j]["lecture"]) == s(attendu)
        assert attendu["decomposition_concluante"] and attendu["taches_completes"] >= 48     # cas non trivial
        # rapports de rangée du lanceur remis à la main sous la forme de `jouer_episodes` (une comparaison « 0,0 »)
        rapports = [{"episode": g["cle"], "tolerance": g["tolerance"], "statistique": g["statistique"],
                     "controle_negatif_zone_generee": {"0,0": g["controle_negatif_zone_generee"]}}
                    for g in f[f"notations-RS1-{j}-decisives"]["garde"]["rapports"]]
        neg = lecture["requalification"][j]["garde_en_ligne"]["controle_negatif"]
        gele = bilan_controle_negatif(rapports, positions_min=4)
        assert {k: neg[k] for k in gele} == gele and neg["courtes"] == 0 and neg["lecture"] == "conforme"
    diff = difference_appariee(*((al[j]["sA"], al[j]["sB"], al[j]["sC"]) for j in JUGES), lp.TIRAGES,
                               generateur(g["analyse/bootstrap-difference-RS1"]), lp.NIVEAU)
    assert s(lecture["difference_appariee"]) == s(diff)
    p_notes = {**pil, "notations": {(f"RS1-{j}", "decisives"): f[f"notations-RS1-{j}-decisives"]["notations"]
                                    for j in JUGES}}
    assert lecture["relectures_audit"] == lp.tirer_relectures(p_notes, generateur(g["analyse/audit-RS1"]))
    assert len(lecture["relectures_audit"]["reponses_de_juge"]) == 10
    assert {x.split("/")[0] for x in lecture["relectures_audit"]["reponses_de_juge"]} <= {"juge-RS1-8B", "juge-RS1-3B"}
    # rejeu sain : propriété du modèle ; reproduction 32 sur 32 ; témoin dans les queues permises ; aucun déclencheur
    assert lecture["lecture_combinee"]["lecture"] == "propriété du modèle"
    assert all(lecture["rejeu"][j]["chemin"]["lecture"] == "fidèle" for j in JUGES)
    assert all(lecture["rejeu"][j]["production"]["lecture"] == "conforme" for j in JUGES)
    assert all(lecture["rejeu"][j]["reproduction"]["identiques"] == 16 for j in JUGES)
    assert lecture["seuils_couverture"] == {"8B": {"quantile": 3072.0, "seuil": 3072},
                                            "3B": {"quantile": 983.0, "seuil": 983}}
    assert not lecture["audit_r4"]["declenche"] and not lecture["lecture_suspendue"]
    # gardes neuves, cas sains : annexe A du texte scellé (D-6) ; tirage des lots recalculé, égal à celui que les
    # fonctions du lanceur donnent (D-14)
    assert lecture["annexe_a"] == "égale à RS1.txt (b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7)"
    assert all(lecture["rejeu"][j]["tirage"] == f[f"rejeu-{j}-demi"]["tirage"] for j in JUGES)
    assert all(len(lecture["rejeu"][j]["tirage"]["cadre"]) == 8 for j in JUGES)
    # sortie scellée, rattachée à son manifeste ; graines de la lecture : même entropie que l'étape (R9)
    r = verifier_resultat(depot, depot / "diag" / LECTURE / "lecture-planb.json")
    assert r["resultat"]["run_planb"] == PLANB and r["resultat"]["arbre_propre"]
    m = json.loads((depot / "runs" / LECTURE / "manifeste.json").read_text())
    assert m["decisif"] and m["preenregistrement"]["chemin"] == p and m["graines"] == g


# --- Règle k(n − 1) et garde en ligne (table A) ------------------------------------------------------------------------

def _fichier_garde(rapports: list[dict]) -> dict:
    """Fichier de notations réduit à la garde, au format du lanceur, depuis des rapports de `jouer_episodes`."""
    return {"notations": [{"cle": r["episode"]} for r in rapports],
            "garde": {"rapports": [{"cle": r["episode"], **_garde(r)} for r in rapports]}}


def _gardes(n: int = 20, debut: int = 0, **k) -> list[dict]:
    return [_rapport(f"juge-RS1-8B/2601.{i:05d}v1/e0/passe-0", graine=i, **k) for i in range(debut, debut + n)]


def test_k_de_et_99e_centile():
    """k(N) = N − ⌊0,99 (N − 1)⌋ ; k(N) positions décalées atteignent le 99e centile (`np.quantile`, interpolation
    linéaire), k(N) − 1 non (le cas au bord qui fonde la règle)."""
    assert [lr.k_de(n) for n in (1, 2, 100, 359, 1005)] == [1, 2, 2, 5, 12]
    for n in range(2, 1200, 7):
        k = lr.k_de(n)
        assert k == n - math.floor(0.99 * (n - 1))
        assert np.quantile([0.0] * (n - k) + [1.0] * k, 0.99) == 1.0
        assert np.quantile([0.0] * (n - k + 1) + [1.0] * (k - 1), 0.99) < 1.0
    with pytest.raises(GardeArret, match="au moins une position"):
        lr.k_de(0)


def test_regle_kn_cas_sain_et_artefact():
    """Trois rangées longues à zone générée brève (1 000 positions de contexte, 6 générées : 5 décalées, sous
    k(1 005) = 12) : courtes par la règle, hors du contrôle négatif, qui est conforme (cas sain) ; comptées sans la
    règle (fonction gelée seule), elles rendent le contrôle négatif « contraire » à tort (artefact)."""
    normales = _gardes(12)
    breves = [_rapport(f"juge-RS1-8B/2601.{i:05d}v1/e0/passe-0", lc=1000, ng=6, graine=i) for i in range(50, 53)]
    neg = lr.controle_negatif_kn(normales + breves, lr.RANGEES_MIN_DEMI)
    assert (neg["comparables"], neg["courtes"], neg["courtes_regle_kn"], neg["lecture"]) == (12, 3, 3, "conforme")
    sans_regle = bilan_controle_negatif(normales + breves, positions_min=4)
    assert sans_regle["comparables"] == 15 and sans_regle["fraction"] == 12 / 15 < lr.FRACTION_MIN    # à tort
    assert all(not lr.comparable_kn(r)[0] and lr.comparable_kn(r)[1] for r in breves)
    # moins de 10 rangées comparables : « non concluant » (courtes de moins de 4 positions décalées, hors règle k)
    tres_breves = [_rapport(f"juge-RS1-8B/2601.{i:05d}v1/e0/passe-0", ng=4, graine=i) for i in range(60, 71)]
    neg = lr.controle_negatif_kn(_gardes(9) + tres_breves, lr.RANGEES_MIN_DEMI)
    assert (neg["comparables"], neg["courtes"], neg["courtes_regle_kn"], neg["lecture"]) == (9, 11, 0,
                                                                                             "non concluant")


def _sonde_fausse() -> list[dict]:
    """Vingt rangées conformes, dont une dont la sonde d'audit n'a pas vu l'unité au dernier rang (D-3)."""
    r = _gardes(20)
    r[7]["sondes"]["0,0"]["ulp_vu"] = False
    return r


GARDES_SYNTHETIQUES = {
    "conforme": lambda: _gardes(20),
    "contraire": lambda: _gardes(19) + [_rapport("juge-RS1-8B/2601.00099v1/e0/passe-0", gen={7: 0.5, 15: 1e-3,
                                                                                            23: 1e-3}, graine=99)],
    "negatif-contraire": lambda: _gardes(16) + _gardes(4, debut=40, repetee=True),
    "negatif-non-concluant": lambda: _gardes(9) + _gardes(11, debut=60, ng=4),
    "trop-beau": lambda: _gardes(20, gen=0.0),
    "sonde-fausse": _sonde_fausse,
}


def test_bilan_garde_cas_synthetiques():
    b = {k: lr.bilan_garde(_fichier_garde(f()), "8B") for k, f in GARDES_SYNTHETIQUES.items()}
    assert (b["conforme"]["equivalence"], b["conforme"]["controle_negatif"]["lecture"], b["conforme"]["trop_beau"]) \
        == ("conforme", "conforme", False)
    assert b["contraire"]["equivalence"] == "contraire" and b["contraire"]["au_dessus"] == [
        "juge-RS1-8B/2601.00099v1/e0/passe-0:7"]
    assert b["negatif-contraire"]["equivalence"] == "conforme"
    assert b["negatif-contraire"]["controle_negatif"]["lecture"] == "contraire"
    assert b["negatif-non-concluant"]["controle_negatif"]["lecture"] == "non concluant"
    assert b["trop-beau"]["trop_beau"] and b["trop-beau"]["equivalence"] == "conforme"
    assert all(x["sondes_justes"] for k, x in b.items() if k != "sonde-fausse")
    assert not b["sonde-fausse"]["sondes_justes"] and b["sonde-fausse"]["equivalence"] == "conforme"


def test_bilan_garde_gardes_de_forme():
    r = _gardes(12)
    lr.bilan_garde(_fichier_garde(r), "8B")                                            # cas sain
    f = _fichier_garde(r)
    f["notations"].append({"cle": "juge-RS1-8B/2601.09999v1/e0/passe-0"})               # notation sans rangée gardée
    with pytest.raises(GardeArret, match="rangées gardées ≠ notations"):
        lr.bilan_garde(f, "8B")
    f = _fichier_garde(r)                                                              # rangée gardée deux fois
    f["garde"]["rapports"].append(copy.deepcopy(f["garde"]["rapports"][0]))
    with pytest.raises(GardeArret, match="rangées gardées ≠ notations"):
        lr.bilan_garde(f, "8B")
    with pytest.raises(GardeArret, match="seuils gelés"):
        lr.bilan_garde(_fichier_garde(r[:-1] + [dict(r[-1], tolerance=0.3)]), "8B")
    with pytest.raises(GardeArret, match="seuils gelés"):
        lr.bilan_garde(_fichier_garde(r[:-1] + [dict(r[-1], statistique="max")]), "8B")
    autre = copy.deepcopy(r[0])
    autre["ecarts_q99"]["0,0"].pop("23")
    with pytest.raises(GardeArret, match="couches"):
        lr.bilan_garde(_fichier_garde([autre] + r[1:]), "8B")
    # deux comparaisons dans un rapport : impossibles au format du lanceur (une seule action), gardées à la lecture
    deux = copy.deepcopy(r[0])
    deux["ecarts"]["1,0"] = deux["ecarts"]["0,0"]
    lr._comparaison(r[0], 0.2, "q99", "garde")                                          # cas sain
    with pytest.raises(GardeArret, match="une attendue"):
        lr._comparaison(deux, 0.2, "q99", "garde")
    with pytest.raises(GardeArret, match="champ « garde » absent"):
        lr.bilan_garde({"notations": []}, "8B")
    sans = _fichier_garde(r)
    del sans["garde"]["rapports"][0]["lignes"]
    with pytest.raises(GardeArret, match=r"rapport sans \['lignes'\]"):
        lr.bilan_garde(sans, "8B")
    sans = _fichier_garde(r)
    del sans["garde"]["rapports"][0]["cle"]
    with pytest.raises(GardeArret, match="champ « cle » absent"):
        lr.bilan_garde(sans, "8B")


@pytest.mark.parametrize("plan_b, garde, combinee, issue, n_reserves", [
    ("rubrique gardée", "conforme", "propriété du modèle", "RS1 retenue", 0),
    ("rubrique gardée", "conforme", "non concluant", "RS1 retenue", 0),
    ("plan B", "conforme", "propriété du modèle", "nœud", 0),
    ("nœud", "conforme", "propriété du modèle", "nœud", 0),
    ("rubrique gardée", "conforme", "défaut du chemin", "nœud", 0),
    # recouvrements listés dans « Tests » : « RS1 retenue » avec garde contraire, contrôle négatif contraire, « trop
    # beau », contrôle négatif « non concluant » : nœud, nœud, nœud, retenue et réserve
    ("rubrique gardée", "contraire", "propriété du modèle", "nœud", 0),
    ("rubrique gardée", "negatif-contraire", "propriété du modèle", "nœud", 0),
    ("rubrique gardée", "trop-beau", "propriété du modèle", "nœud", 1),
    ("rubrique gardée", "negatif-non-concluant", "propriété du modèle", "RS1 retenue", 1),
    # ligne neuve (D-3, R2-06) : sonde d'audit fausse, requalification non concluante (instrument), nœud
    ("rubrique gardée", "sonde-fausse", "propriété du modèle", "nœud", 0),
])
def test_table_a_ligne_par_ligne_et_recouvrements(plan_b, garde, combinee, issue, n_reserves):
    g = lr.bilan_garde(_fichier_garde(GARDES_SYNTHETIQUES[garde]()), "8B")
    a = lr.table_a("8B", {"plan_b": plan_b}, g, combinee)
    assert a["issue"] == issue and len(a["reserves"]) == n_reserves
    assert any("sonde d'audit fausse" in x for x in a["lignes"]) == (garde == "sonde-fausse")
    if plan_b == "plan B":
        assert "8B trop faible" in a["lignes"][0]
        assert "8B trop faible" not in lr.table_a("3B", {"plan_b": plan_b}, g, combinee)["lignes"][0]
    if combinee == "défaut du chemin":
        assert any("défaut du chemin" in x for x in a["lignes"])


def test_table_a_juge_sans_fichier_et_table_b():
    a = lr.table_a("3B", None, None, "propriété du modèle")
    assert a["issue"] == "nœud" and "jamais renoté" in a["lignes"][0]
    assert lr.table_b({"8B": "RS1 retenue", "3B": "RS1 retenue"})["lecture"] == \
        "les deux juges passent à RS1 pour T0.6 et T0.8"
    un = lr.table_b({"8B": "nœud", "3B": "RS1 retenue"})
    assert un["retenus"] == ["3B"] and "le 3B sert T0.6 et T0.8 ; le 8B : proposition à Lazar" in un["lecture"]
    assert lr.table_b({"8B": "nœud", "3B": "nœud"}) == {"retenus": [], "lecture":
                                                        "nœud pour les deux : proposition à Lazar"}


# --- Rejeu : palier de production (table C) ----------------------------------------------------------------------------

C16, D8 = _cles("8B", 16), _cles("8B", 8, 16)


def _lignes(fichier: dict, champ: str) -> list[dict]:
    """Rangées d'un fichier du rejeu : `rangees` (demi-précision), `chemin.rangees` ou `d1.rangees` (simple)."""
    return fichier["rangees"] if champ == "rangees" else fichier[champ]["rangees"]


def _remplacer(fichier: dict, champ: str, indices, ng: int | None = None, **k) -> dict:
    """Copie du fichier où les rangées données ont un rapport refait (même contexte, même tolérance, même statistique),
    avec d'autres écarts ou une autre zone générée."""
    f = copy.deepcopy(fichier)
    for i in indices:
        x = _lignes(f, champ)[i]
        g = x["garde"]
        lc = g["longueurs_contexte"]
        x["garde"] = _garde(_rapport(x["cle"], lc=lc, ng=g["positions_capturees"] - lc if ng is None else ng,
                                     tol=g["tolerance"], stat=g["statistique"], graine=900 + i, **k))
    return f


def test_production_ligne_par_ligne():
    simple = _simple("8B", C16, D8)
    demi = _demi(C16)
    lire = lambda d=demi, s=simple: lr.bilan_production(d, s, "8B")                    # noqa: E731
    assert lire()["lecture"] == "conforme"
    assert lire()["domaine"] == {"contexte_max": 300, "zone_generee_max": 60, "positions_max": 360,
                                 "remplissage_max": 0}
    assert lire(d=dict(demi, duree_s=12.5))["rapportes"] == {"duree_s": 12.5}
    assert lire(d=None)["lecture"] == "non concluant" and lire(s=None)["motifs"] == ["fichier ou repère absent"]
    faux = copy.deepcopy(demi)
    faux["rangees"][3]["garde"]["sondes"]["ulp_vu"] = False
    assert (lire(d=faux)["lecture"], lire(d=faux)["motifs"]) == ("non concluant", ["sonde d'audit fausse"])
    # recouvrement : contrôle négatif contraire avec G_D,max ≤ 0,2 et ρ ≤ 3 : « non concluant »
    contraire = _remplacer(demi, "rangees", range(4), repetee=True)
    b = lire(d=contraire)
    assert b["controle_negatif"]["lecture"] == "contraire" and b["lecture"] == "non concluant"
    assert all(b["g_max"][c] <= 0.2 and b["rho"][c] <= 3 for c in lr.COUCHES)
    breves = _remplacer(demi, "rangees", range(7), ng=4)
    assert lire(d=breves)["controle_negatif"]["lecture"] == "non concluant"
    assert lire(d=breves)["lecture"] == "non concluant"
    # recouvrement : palier tout à zéro : « trop beau »
    assert lire(d=_demi(C16, gen=0.0))["lecture"] == "trop beau"
    # ρ > 3 sous G_D,max ≤ 0,2 : « réserve (ρ) » ; au-dessus de 0,2 : « réserve (au-dessus du seuil) », lue selon R(ℓ)
    b = lire(s=_simple("8B", C16, D8, repere=1e-4))
    assert b["lecture"] == "réserve (ρ)" and all(b["rho"][c] > 3 for c in lr.COUCHES)
    haut = _remplacer(demi, "rangees", [5], gen={7: 0.5, 15: 1e-3, 23: 1e-3}, ctx=1e-3)
    b = lire(d=haut, s=_simple("8B", C16, D8, repere=0.15))
    assert b["lecture"] == "réserve (au-dessus du seuil)" and list(b["au_dessus"]) == ["7"]
    assert "n'a pas sa marge" in b["au_dessus"]["7"]
    b = lire(d=haut)
    assert b["lecture"] == "réserve (au-dessus du seuil)" and "défaut du chemin en demi-précision" in b["au_dessus"]["7"]
    assert b["localisation"][C16[5]]["7"]["q99"] > 0.2


def test_production_gardes_de_forme():
    simple, demi = _simple("8B", C16, D8), _demi(C16)
    with pytest.raises(GardeArret, match="15 rangée"):
        lr.bilan_production({"rangees": demi["rangees"][:15]}, simple, "8B")
    with pytest.raises(GardeArret, match="en double"):
        lr.bilan_production({"rangees": demi["rangees"][:15] + demi["rangees"][:1]}, simple, "8B")
    s = copy.deepcopy(simple)
    s["repere"]["par_rangee"] = [x for x in s["repere"]["par_rangee"] if x["cle"] != C16[2]]
    with pytest.raises(GardeArret, match="repère par rangée"):
        lr.bilan_production(demi, s, "8B")
    s = copy.deepcopy(simple)
    s["repere"]["par_rangee"].append(copy.deepcopy(s["repere"]["par_rangee"][0]))
    with pytest.raises(GardeArret, match="repère par rangée : rangées en double"):
        lr.bilan_production(demi, s, "8B")
    s = copy.deepcopy(simple)
    s["repere"]["par_rangee"] = {x["cle"]: x["par_couche"] for x in s["repere"]["par_rangee"]}
    with pytest.raises(GardeArret, match="une liste de rangées"):
        lr.bilan_production(demi, s, "8B")
    with pytest.raises(GardeArret, match="seuils gelés"):
        lr.bilan_production(_demi(C16, tol=3e-3, stat="max"), simple, "8B")
    d = copy.deepcopy(demi)
    del d["rangees"][5]["garde"]
    with pytest.raises(GardeArret, match="champ « garde » absent"):
        lr.bilan_production(d, simple, "8B")


# --- Rejeu : palier du chemin (table C) --------------------------------------------------------------------------------

def _chemin(**k) -> dict:
    return lr.bilan_chemin(_simple("8B", C16, D8, **k), "8B", C16)


def _avec(simple: dict, indices, **k) -> dict:
    return lr.bilan_chemin(_remplacer(simple, "chemin", indices, **k), "8B", C16)


def test_chemin_lignes_de_controle():
    simple = _simple("8B", C16, D8)
    b = lr.bilan_chemin(simple, "8B", C16)
    assert b["lecture"] == "fidèle" and not b["reserves"] and b["controle_positif_d1"]["lecture"] == "vu"
    assert b["domaine"]["zone_generee_max"] == 3071 and b["rapportes"] == {"type_des_poids": "torch.float32"}
    assert b["reglages_effectifs"] == REGLAGES and b["reglages_non_conformes"] == {}
    assert lr.bilan_chemin(None, "8B", None)["lecture"] == "non concluant (contrôles)"
    for cle, valeur in (("tf32_produits", True), ("precision_produits_simple", "high"), ("reduction_reduite_bf16", True)):
        s = copy.deepcopy(simple)
        s["reglages_relus"][cle] = valeur
        b = lr.bilan_chemin(s, "8B", C16)
        assert b["lecture"] == "non concluant (contrôles)" and "réglages effectifs non conformes" in b["motifs"]
    s = copy.deepcopy(simple)
    del s["reglages_relus"]["tf32_cudnn"]
    assert lr.bilan_chemin(s, "8B", C16)["reglages_non_conformes"] == {"tf32_cudnn": "absent"}
    s = copy.deepcopy(simple)
    s["chemin"]["rangees"][4]["garde"]["sondes"]["tableaux_distincts"] = False
    assert lr.bilan_chemin(s, "8B", C16)["motifs"] == ["sonde d'audit fausse"]
    b = _avec(simple, range(1, 5), repetee=True, gen=1e-4, ctx=1e-4)
    assert b["controle_negatif"]["lecture"] == "contraire" and b["lecture"] == "non concluant (contrôles)"
    s = _remplacer(simple, "chemin", range(1, 8), ng=4)
    for i in range(1, 8):
        s["chemin"]["rangees"][i]["jetons_generes"] = 4
    b = lr.bilan_chemin(s, "8B", C16)
    assert b["controle_negatif"]["lecture"] == "non concluant" and b["lecture"] == "non concluant (contrôles)"
    b = _chemin(d1_gen=1e-4)
    assert b["controle_positif_d1"]["lecture"] == "non vu" and b["lecture"] == "non concluant (contrôles)"
    b = _chemin(d1_ng=3)
    assert b["controle_positif_d1"]["lecture"] == "non concluant" and b["lecture"] == "non concluant (contrôles)"
    # D1 non probant : maximum du contexte de ses rangées au-dessus de 3e-3
    b = _chemin(d1_ctx=5e-3)
    assert b["controle_positif_d1"]["lecture"] == "vu" and b["lecture"] == "non concluant (D1 non probant)"


def test_chemin_classement_des_depassements_et_ancrage():
    simple = _simple("8B", C16, D8)
    seul_7 = lambda v, autre=1e-4: {7: v, 15: autre, 23: autre}                         # noqa: E731
    # concentré dans la zone générée : « décodage » ; défaut
    b = _avec(simple, [3], gen=seul_7(5e-3), ctx=1e-4)
    assert [d["classe"] for d in b["depassements"]] == ["décodage"] and b["lecture"] == "défaut (décodage)"
    # au-dessus de 1e-2 avec R_S ≤ 1e-2/3 : « trop grand » ; défaut
    b = _avec(simple, [3], gen=seul_7(0.02), ctx=1e-4)
    assert [d["classe"] for d in b["depassements"]] == ["trop grand"] and b["lecture"] == "défaut (écart trop grand)"
    # concentré dans le contexte : « contexte » ; diffus : « précision probable »
    b = _avec(simple, [3], ctx=seul_7(5e-3), gen=1e-4)
    assert [d["classe"] for d in b["depassements"]] == ["contexte"] and b["lecture"] == "non concluant (contexte)"
    b = _avec(simple, [3], ctx=seul_7(5e-3), gen=seul_7(5e-3))
    assert [d["classe"] for d in b["depassements"]] == ["diffus"]
    assert b["lecture"] == "non concluant, précision probable"
    # ancrage au-dessus de 1e-3 à la couche d'un dépassement d'au plus 1e-2 : « non concluant (seuil sans marge) »
    s = _simple("8B", C16, D8, ancrage={7: 2e-3, 15: 1e-4, 23: 1e-4})
    b = _avec(s, [3], gen=seul_7(5e-3), ctx=1e-4)
    assert [d["classe"] for d in b["depassements"]] == ["sans marge"]
    assert b["lecture"] == "non concluant (seuil sans marge)"
    # au-dessus de 1e-2/3 à la couche d'un écart au-dessus de 1e-2 : « sans marge », non « défaut »
    s = _simple("8B", C16, D8, ancrage={7: 5e-3, 15: 1e-4, 23: 1e-4})
    b = _avec(s, [3], gen=seul_7(0.02), ctx=1e-4)
    assert [d["classe"] for d in b["depassements"]] == ["sans marge"]
    assert b["lecture"] == "non concluant (seuil sans marge)"
    # au-dessus de 1e-3 à une autre couche que celle d'un dépassement « décodage » : « défaut (décodage) »
    s = _simple("8B", C16, D8, ancrage={7: 1e-4, 15: 2e-3, 23: 1e-4})
    b = _avec(s, [3], gen=seul_7(5e-3), ctx=1e-4)
    assert b["lecture"] == "défaut (décodage)"
    # recouvrement : « décodage » et « sans marge » à deux couches : « défaut (décodage) »
    s = _remplacer(s, "chemin", [3], gen=seul_7(5e-3), ctx=1e-4)
    b = _avec(s, [6], gen={7: 1e-4, 15: 5e-3, 23: 1e-4}, ctx=1e-4)
    assert sorted(d["classe"] for d in b["depassements"]) == ["décodage", "sans marge"]
    assert b["lecture"] == "défaut (décodage)"
    # sans dépassement : « fidèle », et un ancrage au-dessus de 1e-3 n'est qu'une réserve écrite
    b = lr.bilan_chemin(_simple("8B", C16, D8, ancrage={7: 2e-3, 15: 1e-4, 23: 1e-4}), "8B", C16)
    assert b["lecture"] == "fidèle" and len(b["reserves"]) == 1 and "['7']" in b["reserves"][0]


def test_classer_depassement_valeurs_illisibles():
    """Décision D-1 (I-1, R2-01, R-249) : une grandeur illisible (NaN) — G_S, un maximum de zone ou R_S — n'est classée
    nulle part : « illisible », jamais « trop grand » ni « sans marge » (avant D-1, la convention de T0.4 la lisait
    « trop grand », puis « défaut »). Une zone sans position (None) n'est pas illisible : l'écart est tout entier dans
    l'autre zone."""
    nan = float("nan")
    for args in ((nan, 1e-4, 1e-4, 1e-4), (5e-3, 1e-4, 5e-3, nan), (5e-3, nan, 5e-3, 1e-4), (5e-3, 1e-4, nan, 1e-4),
                 (0.02, 1e-4, 0.02, nan), (nan, None, None, nan)):
        assert lr.classer_depassement(*args) == "illisible", args
    assert lr.classer_depassement(5e-3, None, 5e-3, 1e-4) == "décodage"
    assert lr.classer_depassement(5e-3, 5e-3, None, 1e-4) == "contexte"
    assert lr.classer_depassement(5e-3, 4e-3, 5e-3, 1e-4) == "diffus"
    assert lr.classer_depassement(0.02, 1e-4, 0.02, 1e-4) == "trop grand"                # cas sains lisibles
    assert lr.classer_depassement(5e-3, 1e-4, 5e-3, 2e-3) == "sans marge"


def _illisible(simple: dict, cas: str) -> dict:
    """Copie de `rejeu-8B-simple.json` portant une grandeur illisible (NaN) sur la rangée 3 : G_S à la couche 15 ; le
    maximum de la zone générée d'un dépassement à la couche 7 ; R_S à la couche d'un dépassement (7) ; ou R_S à une
    couche sans dépassement (15)."""
    seul_7 = {7: 5e-3, 15: 1e-4, 23: 1e-4}
    if cas == "g_s":
        t = copy.deepcopy(simple)
        t["chemin"]["rangees"][3]["garde"]["ecarts"]["15"] = math.nan
    elif cas == "max_zone":
        t = _remplacer(simple, "chemin", [3], gen=seul_7, ctx=1e-4)
        t["chemin"]["rangees"][3]["garde"]["profils"]["7"]["generee"]["max"] = math.nan
    elif cas == "r_s_depassement":
        t = _remplacer(simple, "chemin", [3], gen=seul_7, ctx=1e-4)
        t["ancrage"]["par_couche"]["7"] = math.nan
    else:
        t = copy.deepcopy(simple)
        t["ancrage"]["par_couche"]["15"] = math.nan
    return t


@pytest.mark.parametrize("cas", ["g_s", "max_zone", "r_s_depassement"])
def test_grandeur_illisible_au_palier_du_chemin_cas_sain_et_artefacts(cas):
    """D-1 : au palier du chemin, un G_S illisible, ou un maximum de zone ou un R_S illisibles sur une rangée et une
    couche au-dessus de τ : motif « grandeur illisible (NaN) », « non concluant (contrôles) », jamais « défaut » ; la
    lecture combinée n'est pas « défaut du chemin » et PB8 est « non concluant » ; la requalification n'est pas
    suspendue (table A). Le déclencheur d'audit NaN reste. Cas sain : le même fichier sans NaN, « fidèle » ; le même
    dépassement lisible, « défaut (décodage) »."""
    s = _simple("8B", C16, D8)
    sain = lr.bilan_chemin(copy.deepcopy(s), "8B", C16)
    assert sain["lecture"] == "fidèle" and sain["motifs"] == []
    if cas != "g_s":
        lisible = lr.bilan_chemin(_remplacer(s, "chemin", [3], gen={7: 5e-3, 15: 1e-4, 23: 1e-4}, ctx=1e-4), "8B", C16)
        assert lisible["lecture"] == "défaut (décodage)"
    t = _illisible(s, cas)
    b = lr.bilan_chemin(t, "8B", C16)
    assert b["lecture"] == "non concluant (contrôles)" and b["motifs"] == ["grandeur illisible (NaN)"]
    assert [d["classe"] for d in b["depassements"]] == ["illisible"]
    rejeu = {"8B": {"chemin": b, "production": {"lecture": "conforme"}},
             "3B": {"chemin": sain, "production": {"lecture": "conforme"}}}
    comb = lr.lecture_combinee(rejeu)["lecture"]
    assert comb == "non concluant"
    for j in JUGES:
        rejeu[j]["reproduction"] = {"identiques": 16, "differentes": []}
    assert lr.predictions_pb({j: None for j in JUGES}, {}, None, comb, rejeu)["PB8"] == "non concluant"
    g = lr.bilan_garde(_fichier_garde(_gardes(12)), "8B")
    assert lr.table_a("8B", {"plan_b": "rubrique gardée"}, g, comb)["issue"] == "RS1 retenue"
    # le déclencheur d'audit NaN reste (table D), sans la ligne « palier du chemin »
    q, r, tm, f = _composantes()
    r["8B"]["chemin"] = lr.bilan_chemin(_illisible(f["rejeu-8B-simple"], cas), "8B", _cles("8B", 16))
    f["rejeu-8B-simple"] = _illisible(f["rejeu-8B-simple"], cas)
    assert _audit(rejeu=r, fichiers=f)["trop_sale"] == ["rejeu du 8B : 1 grandeur(s) illisible(s) (NaN)"]


def test_r_s_illisible_sans_depassement_reste_une_reserve():
    """D-1 ne vise que les rangées et couches au-dessus de τ : un R_S illisible à une couche sans dépassement laisse le
    palier « fidèle », avec la réserve écrite de l'ancrage (un NaN n'est jamais sous 1e-3)."""
    b = lr.bilan_chemin(_illisible(_simple("8B", C16, D8), "r_s_sans_depassement"), "8B", C16)
    assert b["lecture"] == "fidèle" and b["motifs"] == [] and "['15']" in b["reserves"][0]


def test_grandeur_illisible_ne_suspend_pas_la_requalification(tmp_path_factory, monkeypatch):
    """D-1 de bout en bout : un G_S illisible dans `rejeu-8B-simple.json` ; palier du chemin « non concluant
    (contrôles) », lecture combinée « non concluant », PB8 « non concluant », RS1 retenue pour les deux juges, lecture
    suspendue par le déclencheur NaN (audit R4)."""
    depot, h4 = _base(tmp_path_factory)
    p = _run_planb(depot, monkeypatch, _fichiers(h4, **{"rejeu-8B-simple": _illisible(_simple_du_run(h4, "8B"),
                                                                                         "g_s")}))
    lecture = _lire(depot, p)
    assert lecture["rejeu"]["8B"]["chemin"]["lecture"] == "non concluant (contrôles)"
    assert lecture["rejeu"]["8B"]["chemin"]["motifs"] == ["grandeur illisible (NaN)"]
    assert lecture["lecture_combinee"]["lecture"] == "non concluant" and lecture["predictions"]["PB8"] == \
        "non concluant"
    assert all(lecture["table_a"][j]["issue"] == "RS1 retenue" for j in JUGES)
    assert lecture["lecture_suspendue"] and lecture["audit_r4"]["trop_sale"] == [
        "rejeu du 8B : 1 grandeur(s) illisible(s) (NaN)"]


def test_chemin_trop_beau_et_couverture():
    # recouvrement : palier tout à zéro dans la zone générée, sans dépassement : « trop beau », non « fidèle »
    b = _chemin(gen=0.0)
    assert not b["depassements"] and b["trop_beau"] and b["lecture"] == "trop beau"
    # couverture au bord : rangée tronquée, 3 072 jetons générés, 3 071 positions générées comparées : atteinte
    c = _chemin()["couverture"]
    assert (c["jetons_generes"], c["zone_generee"], c["atteinte"]) == (3072, 3071, True)
    c3 = lr.bilan_chemin(_simple("3B", _cles("3B", 16), _cles("3B", 8, 16)), "3B", _cles("3B", 16))["couverture"]
    assert (c3["seuil"], c3["jetons_generes"], c3["atteinte"]) == (983, 983, True)
    # artefact : rangées trop courtes, « non concluant (couverture) »
    b = _chemin(longue=3000)
    assert not b["couverture"]["atteinte"] and b["lecture"] == "non concluant (couverture)"
    b3 = lr.bilan_chemin(_simple("3B", _cles("3B", 16), _cles("3B", 8, 16), longue=982), "3B", _cles("3B", 16))
    assert b3["lecture"] == "non concluant (couverture)"
    # artefact de forme : positions générées comparées ni n ni n − 1
    s = _simple("8B", C16, D8)
    s["chemin"]["rangees"][0]["jetons_generes"] = 3074
    with pytest.raises(GardeArret, match="n ou n − 1 attendues"):
        lr.bilan_chemin(s, "8B", C16)


def test_chemin_gardes_de_forme():
    s = _simple("8B", C16, D8)
    with pytest.raises(GardeArret, match="rangées ≠ celles du palier de production"):
        lr.bilan_chemin(s, "8B", _cles("8B", 16, 40))
    t = copy.deepcopy(s)
    t["d1"]["rangees"][0]["cle"] = C16[0]
    with pytest.raises(GardeArret, match="L3 .D1. non distinct"):
        lr.bilan_chemin(t, "8B", C16)
    with pytest.raises(GardeArret, match="7 rangée"):
        lr.bilan_chemin(dict(s, d1=dict(s["d1"], rangees=s["d1"]["rangees"][:7])), "8B", C16)
    t = copy.deepcopy(s)
    del t["ancrage"]["par_couche"]["15"]
    with pytest.raises(GardeArret, match="champ « 15 » absent"):
        lr.bilan_chemin(t, "8B", C16)
    t = copy.deepcopy(s)
    t["chemin"]["rangees"][2]["garde"]["tolerance"] = 0.2
    with pytest.raises(GardeArret, match="seuils gelés"):
        lr.bilan_chemin(t, "8B", C16)
    t = copy.deepcopy(s)
    t["d1"]["rangees"][2]["garde"]["statistique"] = "q99"
    with pytest.raises(GardeArret, match="seuils gelés"):
        lr.bilan_chemin(t, "8B", C16)
    # format du lanceur : rangées sous `chemin.rangees` et `d1.rangees`, rapport de rangée sous `garde`
    with pytest.raises(GardeArret, match="champ « rangees » absent"):
        lr.bilan_chemin(dict(s, chemin=s["chemin"]["rangees"]), "8B", C16)
    t = copy.deepcopy(s)
    del t["d1"]["rangees"][1]["garde"]["profils"]
    with pytest.raises(GardeArret, match=r"rapport sans \['profils'\]"):
        lr.bilan_chemin(t, "8B", C16)
    with pytest.raises(GardeArret, match="champ « reglages_relus » absent"):
        lr.bilan_chemin({k: v for k, v in s.items() if k != "reglages_relus"}, "8B", C16)


# --- Reproduction, lecture combinée, témoin ----------------------------------------------------------------------------

def test_reproduction():
    h4 = [{"cle": c, "reponse": f"réponse {i}", "jetons_reponse": 3072 if i % 2 else 900, "tronquee": bool(i % 2)}
          for i, c in enumerate(C16)]
    par_cle = {x["cle"]: x for x in h4}
    b = lr.bilan_reproduction(_demi(C16, par_cle), h4, "8B")
    assert (b["identiques"], b["differentes"]) == (16, []) and b["lecture"].startswith("16 sur 16")
    for champ, valeur in (("reponse", "réponse altérée"), ("jetons_reponse", 899), ("tronquee", True)):
        autre = copy.deepcopy(par_cle)
        autre[C16[4]][champ] = valeur
        demi = _demi(C16, autre, scellees=par_cle)          # réponse rejouée altérée ; lanceur : « non identique »
        assert demi["rangees"][4]["reproduction"]["identique"] is False
        b = lr.bilan_reproduction(demi, h4, "8B")
        assert b["differentes"] == [C16[4]] and b["lecture"].startswith("réserve")
    with pytest.raises(GardeArret, match="absente des notations H.4"):
        lr.bilan_reproduction(_demi(C16, par_cle), h4[1:], "8B")
    assert lr.bilan_reproduction(None, h4, "8B")["identiques"] == 0
    # artefact : reproduction consignée par le lanceur ≠ reproduction recalculée par la lecture (dans les deux sens)
    for faux in (False, "oui"):
        demi = _demi(C16, par_cle)
        demi["rangees"][6]["reproduction"]["identique"] = faux
        with pytest.raises(GardeArret, match="reproduction consignée .* ≠ reproduction recalculée"):
            lr.bilan_reproduction(demi, h4, "8B")
    demi = _demi(C16, {**par_cle, C16[2]: dict(par_cle[C16[2]], reponse="autre")}, scellees=par_cle)
    demi["rangees"][2]["reproduction"]["identique"] = True
    with pytest.raises(GardeArret, match="reproduction consignée"):
        lr.bilan_reproduction(demi, h4, "8B")


@pytest.mark.parametrize("chemins, productions, attendu", [
    (("fidèle", "fidèle"), ("conforme", "conforme"), "propriété du modèle"),
    (("fidèle", "fidèle"), ("conforme", "réserve (ρ)"), "propriété du modèle, sous réserve de demi-précision"),
    (("fidèle", "fidèle"), ("réserve (au-dessus du seuil)", "réserve (ρ)"),
     "propriété du modèle, sous réserve de demi-précision"),
    (("défaut (décodage)", "fidèle"), ("conforme", "conforme"), "défaut du chemin"),
    (("non concluant (contrôles)", "défaut (écart trop grand)"), ("non concluant", "conforme"), "défaut du chemin"),
    (("fidèle", "non concluant (couverture)"), ("conforme", "conforme"), "non concluant"),
    (("fidèle", "fidèle"), ("conforme", "trop beau"), "non concluant"),
    (("fidèle", "fidèle"), ("conforme", "non concluant"), "non concluant"),
    (("trop beau", "fidèle"), ("conforme", "conforme"), "non concluant"),
])
def test_lecture_combinee(chemins, productions, attendu):
    rejeu = {j: {"chemin": {"lecture": c}, "production": {"lecture": p}} for j, c, p in zip(JUGES, chemins, productions)}
    assert lr.lecture_combinee(rejeu)["lecture"] == attendu


def test_temoin_queues_et_lectures():
    """Queues binomiales recalculées sur les taux H.4 du texte (8B : 0 ou au moins 11 ; 3B : au moins 5) ; T_w dans une
    queue : déclencheur ; témoin impossible pour un appel : comptes sans déclencheur ; fichier absent : non rapporté."""
    assert lr.queues_binomiales(60 / 180) == [0] + list(range(11, 17))
    assert lr.queues_binomiales(9 / 180) == list(range(5, 17))
    b = lr.bilan_temoin(_temoins(), "8B", 60 / 180)
    assert (b["t_w"], b["hors_queue"], b["completes"]) == (5, False, 11)
    assert lr.bilan_temoin(_temoins({"8B": 0}), "8B", 60 / 180)["hors_queue"] is True
    assert lr.bilan_temoin(_temoins({"8B": 11}), "8B", 60 / 180)["hors_queue"] is True
    assert lr.bilan_temoin(_temoins({"8B": 10}), "8B", 60 / 180)["hors_queue"] is False
    assert lr.bilan_temoin(_temoins({"3B": 5}), "3B", 9 / 180)["hors_queue"] is True
    assert lr.bilan_temoin(_temoins({"3B": 4}), "3B", 9 / 180)["hors_queue"] is False
    b = lr.bilan_temoin(_temoins({"8B": 0}, impossible={"8B": True}), "8B", 60 / 180)
    assert b["hors_queue"] is None and b["rangees"] == 8 and b["impossible"][0]["motif"] == "déterminisme"
    assert lr.bilan_temoin(None, "8B", 60 / 180)["lecture"] == "non rapporté"
    # artefacts de forme (format du lanceur) : appels absents, statut inconnu, motif absent, taux H.4 consigné autre
    t = _temoins()
    del t["juges"]["3B"]["appels"]
    with pytest.raises(GardeArret, match="champ « appels » absent"):
        lr.bilan_temoin(t, "3B", 9 / 180)
    t = _temoins()
    t["juges"]["3B"]["appels"][1]["statut"] = "fait à moitié"
    with pytest.raises(GardeArret, match="statut d'appel 'fait à moitié' inconnu"):
        lr.bilan_temoin(t, "3B", 9 / 180)
    t = _temoins(impossible={"3B": True})
    del t["juges"]["3B"]["appels"][1]["motif"]
    with pytest.raises(GardeArret, match="champ « motif » absent"):
        lr.bilan_temoin(t, "3B", 9 / 180)
    with pytest.raises(GardeArret, match="taux H.4 consigné"):
        lr.bilan_temoin(_temoins(taux={"3B": (10, 180)}), "3B", 9 / 180)


def test_seuils_et_taux_recalcules_sur_les_notations_h4_scellees():
    """Sur les notations H.4 scellées du dépôt (longueurs et drapeaux seulement) : seuils de couverture 3 072 et 983,
    taux de troncature 60/180 et 9/180 (cas sain) ; artefact : longueurs déplacées, arrêt."""
    d = REEL / "diag" / "20261017-193648-t05-notations-reel"
    h4 = {j: json.loads((d / f"notations-{j}-decisives.json").read_text(encoding="utf-8"))["resultat"]["notations"]
          for j in JUGES}
    s = lr.seuils_couverture(h4)
    assert (s["8B"]["seuil"], s["3B"]["quantile"], s["3B"]["seuil"]) == (3072, 982.75, 983)
    assert [sum(n["tronquee"] for n in h4[j]) for j in JUGES] == [60, 9] and len(h4["8B"]) == len(h4["3B"]) == 180
    h4["3B"] = [dict(n, jetons_reponse=n["jetons_reponse"] + 2) for n in h4["3B"]]
    with pytest.raises(GardeArret, match="seuils de couverture recalculés"):
        lr.seuils_couverture(h4)


# --- Audit de symétrie (table D) ---------------------------------------------------------------------------------------

_COMPOSANTES: dict = {}


def _composantes() -> tuple[dict, dict, dict, dict]:
    """Requalification, rejeu, témoin et fichiers du rejeu sains, pour les deux juges (copies)."""
    if not _COMPOSANTES:
        demi = {j: _demi(_cles(j, 16)) for j in JUGES}
        simple = {j: _simple(j, _cles(j, 16), _cles(j, 8, 16)) for j in JUGES}
        _COMPOSANTES.update(demi=demi, simple=simple,
                            garde=lr.bilan_garde(_fichier_garde(_gardes(12)), "8B"))
    demi, simple = copy.deepcopy(_COMPOSANTES["demi"]), copy.deepcopy(_COMPOSANTES["simple"])
    requalif = {j: {"descriptifs": {"part_somme_la_plus_frequente": 0.2},
                    "garde_en_ligne": copy.deepcopy(_COMPOSANTES["garde"])} for j in JUGES}
    rejeu = {j: {"production": lr.bilan_production(demi[j], simple[j], j),
                 "chemin": lr.bilan_chemin(simple[j], j, _cles(j, 16))} for j in JUGES}
    temoin = {j: lr.bilan_temoin(_temoins(), j, {"8B": 60 / 180, "3B": 9 / 180}[j]) for j in JUGES}
    fichiers = {f"rejeu-{j}-{p}": (demi if p == "demi" else simple)[j] for j in JUGES for p in ("demi", "simple")}
    return requalif, rejeu, temoin, fichiers


def _juge_lu(part=0.5, identiques=0.0, tache=1.0, impossible=None) -> dict:
    if impossible:
        return {"part_A_B_identiques": identiques, "decomposition": None, "decomposition_impossible": impossible}
    return {"part_A_B_identiques": identiques,
            "decomposition": {"parts_tronquees": {"juge": part}, "composantes": {"tache": tache}}}


def _audit(juges=None, fmt=None, requalif=None, rejeu=None, temoin=None, fichiers=None) -> dict:
    q, r, t, f = _composantes()
    juges = {"RS1-8B": _juge_lu(), "RS1-3B": _juge_lu()} if juges is None else juges
    return lr.audit_r4(fmt or {"part_valides": 0.5}, juges, requalif or q, rejeu or r, temoin or t, fichiers or f)


def test_audit_cas_sain_et_filtre_des_declencheurs_du_format():
    a = _audit()
    assert a == {"trop_propre": [], "trop_sale": [], "declenche": False, "rangees_en_cause": {}}
    # les déclencheurs gelés du format des actions de l'agent ne sont pas propres aux juges : écartés
    a = _audit(fmt={"part_valides": 1.0})
    assert not a["declenche"]
    a = _audit(fmt={"part_valides": 0.1})
    assert not a["declenche"]


@pytest.mark.parametrize("juge, sens, motif", [
    (_juge_lu(identiques=0.2), "trop_propre", "juge RS1-8B : plus de 10 % de réponses A et B identiques"),
    (_juge_lu(part=0.03), "trop_propre", "part du juge RS1-8B < 0,05"),
    (_juge_lu(part=0.97), "trop_sale", "juge RS1-8B : part > 0,95 ou σ̂²_β ≤ 0"),
    (_juge_lu(tache=-0.1), "trop_sale", "juge RS1-8B : part > 0,95 ou σ̂²_β ≤ 0"),
    (_juge_lu(part=float("nan")), "trop_sale", "juge RS1-8B : part illisible"),
    (_juge_lu(impossible="notes constantes"), "trop_sale", "juge RS1-8B : décomposition impossible (notes constantes)"),
])
def test_audit_declencheurs_geles_propres_aux_juges(juge, sens, motif):
    a = _audit(juges={"RS1-8B": juge, "RS1-3B": _juge_lu()})
    assert a[sens] == [motif] and a["declenche"]


def test_audit_declencheurs_neufs_de_la_requalification():
    q, *_ = _composantes()
    q["3B"]["descriptifs"]["part_somme_la_plus_frequente"] = 0.51
    assert _audit(requalif=q)["trop_propre"] == ["juge RS1-3B : somme la plus fréquente sur plus de 50 % des "
                                                 "réponses complètes"]
    q, *_ = _composantes()
    q["3B"]["descriptifs"]["part_somme_la_plus_frequente"] = 0.5                       # cas au bord : pas au-dessus
    assert not _audit(requalif=q)["declenche"]
    q["8B"]["garde_en_ligne"] = lr.bilan_garde(_fichier_garde(GARDES_SYNTHETIQUES["trop-beau"]()), "8B")
    assert _audit(requalif=q)["trop_propre"] == ["garde en ligne de RS1-8B : trop beau"]


def test_audit_declencheurs_du_rejeu():
    q, r, t, f = _composantes()
    # grandeur illisible (NaN) dans un fichier du rejeu
    f["rejeu-8B-simple"]["chemin"]["rangees"][2]["garde"]["ecarts"]["7"] = float("nan")
    assert _audit(fichiers=f)["trop_sale"] == ["rejeu du 8B : 1 grandeur(s) illisible(s) (NaN)"]
    # repère au-dessus de 0,2 à une couche
    q, r, t, f = _composantes()
    r["3B"]["production"] = lr.bilan_production(f["rejeu-3B-demi"], _simple("3B", _cles("3B", 16), _cles("3B", 8, 16),
                                                                             repere=0.25), "3B")
    assert _audit(rejeu=r)["trop_sale"] == ["rejeu du 3B : repère R(ℓ) > 0,2 aux couches ['7', '15', '23']"]
    # palier du chemin : défaut et trois « non concluant » déclenchent ; « contrôles » et « couverture » non
    s8 = f["rejeu-8B-simple"]
    for k, lecture, declenche in (
            (dict(gen={7: 5e-3, 15: 1e-4, 23: 1e-4}, ctx=1e-4), "défaut (décodage)", True),
            (dict(ctx={7: 5e-3, 15: 1e-4, 23: 1e-4}, gen=1e-4), "non concluant (contexte)", True),
            (dict(ctx={7: 5e-3, 15: 1e-4, 23: 1e-4}, gen={7: 5e-3, 15: 1e-4, 23: 1e-4}),
             "non concluant, précision probable", True)):
        q, r, t, f = _composantes()
        r["8B"]["chemin"] = lr.bilan_chemin(_remplacer(s8, "chemin", [3], **k), "8B", _cles("8B", 16))
        a = _audit(rejeu=r)
        assert r["8B"]["chemin"]["lecture"] == lecture
        assert a["trop_sale"] == [f"rejeu du 8B : palier du chemin « {lecture} »"]
        assert a["rangees_en_cause"] == {"8B": [_cles("8B", 16)[3]]}
    s = _simple("8B", _cles("8B", 16), _cles("8B", 8, 16), ancrage={7: 2e-3, 15: 1e-4, 23: 1e-4})
    q, r, t, f = _composantes()
    r["8B"]["chemin"] = lr.bilan_chemin(_remplacer(s, "chemin", [3], gen={7: 5e-3, 15: 1e-4, 23: 1e-4}, ctx=1e-4),
                                        "8B", _cles("8B", 16))
    assert _audit(rejeu=r)["trop_sale"] == ["rejeu du 8B : palier du chemin « non concluant (seuil sans marge) »"]
    for k in (dict(d1_gen=1e-4), dict(longue=3000)):
        q, r, t, f = _composantes()
        r["8B"]["chemin"] = lr.bilan_chemin(_simple("8B", _cles("8B", 16), _cles("8B", 8, 16), **k), "8B",
                                            _cles("8B", 16))
        assert r["8B"]["chemin"]["lecture"].startswith("non concluant (") and not _audit(rejeu=r)["declenche"]
    # contrôle positif D1 non probant
    q, r, t, f = _composantes()
    r["8B"]["chemin"] = lr.bilan_chemin(_simple("8B", _cles("8B", 16), _cles("8B", 8, 16), d1_ctx=5e-3), "8B",
                                        _cles("8B", 16))
    assert _audit(rejeu=r)["trop_sale"] == ["rejeu du 8B : contrôle positif D1 non probant"]
    # palier de production en « réserve (ρ) » ; ses rangées en cause
    q, r, t, f = _composantes()
    r["3B"]["production"] = lr.bilan_production(f["rejeu-3B-demi"], _simple("3B", _cles("3B", 16), _cles("3B", 8, 16),
                                                                             repere=1e-4), "3B")
    a = _audit(rejeu=r)
    assert a["trop_sale"] == ["rejeu du 3B : palier de production en « réserve (ρ) »"]
    assert a["rangees_en_cause"] == {"3B": sorted(_cles("3B", 16))}
    # « trop beau » aux deux paliers
    q, r, t, f = _composantes()
    r["8B"]["production"] = lr.bilan_production(_demi(_cles("8B", 16), gen=0.0), f["rejeu-8B-simple"], "8B")
    r["3B"]["chemin"] = lr.bilan_chemin(_simple("3B", _cles("3B", 16), _cles("3B", 8, 16), gen=0.0), "3B",
                                        _cles("3B", 16))
    assert _audit(rejeu=r)["trop_propre"] == ["rejeu du 8B : palier de production trop beau",
                                              "rejeu du 3B : palier du chemin trop beau"]
    # témoin hors des queues binomiales
    q, r, t, f = _composantes()
    t["8B"] = lr.bilan_temoin(_temoins({"8B": 11}), "8B", 60 / 180)
    assert _audit(temoin=t)["trop_sale"] == ["témoin du 8B : T_w = 11 dans une queue binomiale de moins de 0,5 %"]


# --- Prédictions PB1 à PB10 --------------------------------------------------------------------------------------------

def _pb(inc=(0.0, 0.0), tc=(50, 50), part=(0.6, 0.6), concl=(True, True), borne=(0.01, 0.2), taches=50,
        garde=("conforme", "conforme"), neg=("conforme", "conforme"), med=(80.0, 80.0),
        combinee="propriété du modèle", repro=((16, 0), (16, 0)), absents=()) -> dict:
    juges, requalif, rejeu = {}, {}, {}
    for i, j in enumerate(JUGES):
        rejeu[j] = {"reproduction": {"identiques": repro[i][0], "differentes": ["x"] * repro[i][1]}}
        if j in absents:
            requalif[j] = None
            continue
        juges[f"RS1-{j}"] = {"part_incompletes": inc[i], "taches_completes": tc[i], "decomposition_concluante": concl[i],
                             "decomposition": {"parts_tronquees": {"juge": part[i]}}}
        requalif[j] = {"garde_en_ligne": {"equivalence": garde[i], "controle_negatif": {"lecture": neg[i]}},
                       "descriptifs": {"longueur_mediane": med[i]}}
    diff = None if borne is None else {"taches": taches, "borne": list(borne)}
    return lr.predictions_pb(requalif, juges, diff, combinee, rejeu)


def test_predictions_toutes_confirmees():
    assert set(_pb().values()) == {"confirmée"}


@pytest.mark.parametrize("entrees, attendus", [
    (dict(inc=(0.25, 0.0)), {"PB1": "réfutée", "PB2": "confirmée"}),
    (dict(inc=(0.10, 0.21)), {"PB1": "non concluant", "PB2": "réfutée"}),
    (dict(inc=(0.2, 0.05)), {"PB1": "non concluant", "PB2": "confirmée"}),
    (dict(absents=("8B",)), {"PB1": "non concluant", "PB3": "non concluant", "PB4": "non concluant",
                             "PB7": "non concluant", "PB10": "non concluant"}),
    (dict(tc=(48, 47)), {"PB3": "réfutée"}),
    (dict(tc=(40, 60), absents=("3B",)), {"PB3": "réfutée"}),
    (dict(part=(0.3, 0.85)), {"PB4": "non concluant", "PB5": "non concluant"}),
    (dict(part=(0.1, 0.97)), {"PB4": "réfutée", "PB5": "réfutée"}),
    (dict(part=(0.6, 0.6), concl=(False, True)), {"PB4": "non concluant", "PB5": "confirmée"}),
    (dict(borne=(-0.2, -0.01)), {"PB6": "réfutée"}),
    (dict(borne=(-0.1, 0.2)), {"PB6": "non concluant"}),
    (dict(taches=47), {"PB6": "non concluant"}),
    (dict(borne=None), {"PB6": "non concluant"}),
    (dict(garde=("contraire", "conforme")), {"PB7": "réfutée"}),
    (dict(garde=("contraire", "conforme"), neg=("contraire", "conforme")), {"PB7": "non concluant"}),
    (dict(garde=("contraire", "conforme"), neg=("non concluant", "conforme")), {"PB7": "non concluant"}),
    (dict(neg=("non concluant", "contraire")), {"PB7": "confirmée"}),
    (dict(combinee="propriété du modèle, sous réserve de demi-précision"), {"PB8": "non concluant"}),
    (dict(combinee="défaut du chemin"), {"PB8": "réfutée"}),
    (dict(combinee="non concluant"), {"PB8": "non concluant"}),
    (dict(repro=((16, 0), (15, 1))), {"PB9": "réfutée"}),
    (dict(repro=((16, 0), (0, 0))), {"PB9": "non concluant"}),
    (dict(med=(150.0, 151.0)), {"PB10": "non concluant"}),
    (dict(med=(120.0, 401.0)), {"PB10": "réfutée"}),
])
def test_predictions_cas_par_cas(entrees, attendus):
    s = _pb(**entrees)
    assert {k: s[k] for k in attendus} == attendus


# --- Runs partiels et issue du run (table E) ---------------------------------------------------------------------------

def test_table_e_run_arrete_apres_la_requalification_du_8b(tmp_path_factory, monkeypatch):
    """Arrêt consigné après le fichier du 8B : ce fichier se lit selon A ; le 3B est en nœud, sans renotation ; les
    paliers du rejeu sont « non concluant » ; le témoin n'est pas rapporté ; aucun relancement."""
    depot, h4 = _base(tmp_path_factory)
    f = _fichiers(h4)
    p = _run_planb(depot, monkeypatch, {"notations-RS1-8B-decisives": f["notations-RS1-8B-decisives"]}, issue="arret",
                   statuts={"notations-RS1-3B-decisives": "en cours"})
    lecture = _lire(depot, p)
    e = lecture["runs_partiels"]
    assert e["issue"] == "arret" and e["ecrits"] == ["notations-RS1-8B-decisives"]
    assert e["absents"]["notations-RS1-3B-decisives"].startswith("requalification du 3B : nœud")
    assert e["absents"]["temoins"] == "témoin non rapporté" and e["relancement"].startswith("aucun relancement")
    assert lecture["requalification"]["3B"] is None and lecture["table_a"]["3B"]["issue"] == "nœud"
    assert lecture["requalification"]["8B"]["lecture"]["decomposition_concluante"]
    assert lecture["table_a"]["8B"]["issue"] == "RS1 retenue"
    assert lecture["usagers"]["retenus"] == ["8B"]
    assert all(lecture["rejeu"][j]["chemin"]["lecture"] == "non concluant (contrôles)" for j in JUGES)
    assert all(lecture["rejeu"][j]["production"]["lecture"] == "non concluant" for j in JUGES)
    assert lecture["lecture_combinee"]["lecture"] == "non concluant"
    assert lecture["temoin"]["8B"]["lecture"] == "non rapporté" and lecture["difference_appariee"] is None
    pb = lecture["predictions"]
    assert (pb["PB2"], pb["PB6"], pb["PB8"], pb["PB9"]) == ("non concluant",) * 4
    assert {x.split("/")[0] for x in lecture["relectures_audit"]["reponses_de_juge"]} == {"juge-RS1-8B"}


def test_table_e_arret_avant_tout_fichier(tmp_path_factory, monkeypatch):
    depot, _ = _base(tmp_path_factory)
    p = _run_planb(depot, monkeypatch, {}, issue="arret")
    lecture = _lire(depot, p)
    e = lecture["runs_partiels"]
    assert e["aucun_fichier_de_phase_ecrit"] and "condition (ii) tenue" in e["relancement"]
    assert e["arret"] == {"etape": "rejeu du 8B", "motif": "GardeArret: essai"}
    assert all(lecture["table_a"][j]["issue"] == "nœud" for j in JUGES)
    assert lecture["usagers"]["lecture"] == "nœud pour les deux : proposition à Lazar"


@pytest.mark.parametrize("cas, motif", [
    ("sans-issue", "ni resume.json ni arret.json"),
    ("les-deux", "un seul attendu"),
    ("ecrit-mais-absent", "en désaccord"),
    ("present-mais-echu", "en désaccord"),
    ("sans-phases", "sans statuts des phases"),
    ("sceau", "empreinte"),
    ("rattache-ailleurs", "rattaché au run 20261020-100001-autre"),
    ("issue-rattachee-ailleurs", r"resume\.json rattaché au run 20261020-100001-autre"),
    # noms de fichiers ou statuts que le lanceur n'écrit pas (juges d'autres noms, statut inconnu)
    ("fichier-inconnu", "inconnus du lecteur"),
    ("statut-inconnu", "inconnus du lecteur"),
])
def test_table_e_run_non_lisible(tmp_path_factory, monkeypatch, cas, motif):
    """Issue absente, double, sans statuts ou en désaccord avec les fichiers ; fichier sans sceau conforme ou rattaché
    ailleurs ; nom de fichier ou statut inconnu : non lisible, nœud pour tout ; la lecture s'arrête sans rien écrire
    (cas sain : les autres tests)."""
    depot, h4 = _base(tmp_path_factory)
    f = _fichiers(h4, sans=("temoins",)) if cas == "ecrit-mais-absent" else {"temoins": _temoins()}
    issue = {"sans-issue": None, "les-deux": "les-deux"}.get(cas, "resume")
    statuts = {"ecrit-mais-absent": {"temoins": "écrit"}, "present-mais-echu": {"temoins": "échu"},
               "fichier-inconnu": {"notations-RS1-jouet-8B-decisives": "en cours"},
               "statut-inconnu": {"temoins": "fini"}}.get(cas)
    p = _run_planb(depot, monkeypatch, f if cas == "ecrit-mais-absent" else {"temoins": _temoins()}, issue=issue,
                   statuts=statuts)
    d = depot / "diag" / PLANB
    if cas == "sans-phases":
        (d / "resume.json").unlink()
        Path(str(d / "resume.json") + ".sha256").unlink()
        chemin = depot / "runs" / PLANB / "manifeste.json"
        ecrire_resultat(depot, chemin, "resume", {"juges": {}})
    if cas == "sceau":
        Path(str(d / "temoins.json") + ".sha256").write_text("0" * 64 + "  temoins.json\n")
    if cas in ("rattache-ailleurs", "issue-rattachee-ailleurs"):
        autre, nom = "20261020-100001-autre", "temoins" if cas == "rattache-ailleurs" else "resume"
        c_autre, _ = creer_manifeste(depot, autre, {"mode": "jouet"}, ["x"], entropie=1, autoriser_depot_sale=True)
        f_autre = ecrire_resultat(depot, c_autre, nom, _temoins() if nom == "temoins" else
                                  {"fichiers": {"temoins": "écrit"}})
        (d / f"{nom}.json").write_bytes(f_autre.read_bytes())
        Path(str(d / f"{nom}.json") + ".sha256").write_bytes(Path(str(f_autre) + ".sha256").read_bytes())
    with pytest.raises(GardeArret, match=motif):
        _lire(depot, p, autoriser_depot_sale=True)
    assert not (depot / "runs" / LECTURE).exists() and not (depot / "diag" / LECTURE).exists()


# --- Gardes de lecture (cas sain : test d'équivalence) -----------------------------------------------------------------

@pytest.mark.parametrize("artefact, motif", [
    ("autre-prereg", "autre préenregistrement"),
    ("config-seuil", "seuils gelés du lecteur"),
    ("config-cle-absente", "seuils gelés du lecteur"),
    ("config-notations", "rattaché ailleurs"),
    ("config-pilote", "rattaché ailleurs"),
    ("config-juges", r"juges du run de l'étape \['3B', 'jouet-8B'\] ≠ juges du lecteur"),
    ("config-couverture", "seuils gelés du lecteur"),
    ("config-intervalles", "seuils gelés du lecteur"),
    ("module-neuf-modifie", "modules neufs de l'étape modifiés"),
    ("module-neuf-absent", "modules neufs de l'étape absents"),
    ("module-gele-modifie", "modules gelés réutilisés modifiés"),
    ("lecture-rs1", "lecture RS1 recalculée ≠ lecture consignée"),
    ("lecture-rs1-comptes", "lecture RS1 recalculée ≠ lecture consignée"),
    ("lecture-rs1-sans-troncature", "lecture RS1 recalculée ≠ lecture consignée"),
    ("variante", "variante 'b0', RS1 attendue"),
    ("desalignement", "désalignement"),
    ("garde-incomplete", "rangées gardées ≠ notations"),
    ("run-absent", "manifeste du run de l'étape absent"),
    ("arbre-sale", "arbre de travail non propre"),
    ("lecture-existante", "existe déjà"),
    ("entropies", "d'entropies différentes"),
])
def test_gardes_de_lecture_artefacts(tmp_path_factory, monkeypatch, artefact, motif):
    depot, h4 = _base(tmp_path_factory)
    f = _fichiers(h4)
    n8 = f["notations-RS1-8B-decisives"]["notations"]
    config = None
    if artefact == "config-seuil":
        config = _config(depot, tolerance_demi=0.3)
    elif artefact == "config-cle-absente":
        config = {k: v for k, v in _config(depot).items() if k != "regle_kn"}
    elif artefact == "config-notations":
        config = _config(depot, run_notations="20261012-200009-autre")
    elif artefact == "config-pilote":
        config = _config(depot, manifeste_pilote_sha256="0" * 64)
    elif artefact == "config-juges":
        config = _config(depot, juges=[{"nom": "jouet-8B"}, {"nom": "3B"}])
    elif artefact == "config-couverture":
        config = _config(depot, couverture_jetons={"8B": 3072, "3B": 984})
    elif artefact == "config-intervalles":
        ci = lr.CONSTANTES_CONFIG["controle_intervalles"]
        config = _config(depot, controle_intervalles=dict(ci, separateurs_second_nombre=[",", ";", "and"]))
    elif artefact == "lecture-rs1":
        n8[3] = dict(n8[3], notes={**n8[3]["notes"], "RIGOR": (n8[3]["notes"]["RIGOR"] + 1) % 5})
    elif artefact == "lecture-rs1-comptes":
        n8[3] = dict(n8[3], lecture_rs1={**n8[3]["lecture_rs1"], "intervalles": 1})
    elif artefact == "lecture-rs1-sans-troncature":
        n8[3] = dict(n8[3], complete_sans_troncature=not n8[3]["complete_sans_troncature"])
    elif artefact == "variante":
        n8[3] = dict(n8[3], variante="b0")
    elif artefact == "desalignement":
        n8[3] = dict(n8[3], ensemble_sha256="0" * 64)
    elif artefact == "garde-incomplete":
        f["notations-RS1-8B-decisives"]["garde"]["rapports"].pop()
    p = _run_planb(depot, monkeypatch, f, config=config)
    k = {}
    if artefact == "autre-prereg":
        k["prereg"] = str(depot / _prereg_notations(depot, "autre.md"))
    elif artefact == "module-neuf-modifie":
        m = depot / lr.MODULES_PLANB[1]
        m.write_text(m.read_text() + "\n# modifié\n")
    elif artefact == "module-neuf-absent":
        (depot / lr.MODULES_PLANB[2]).unlink()
    elif artefact == "module-gele-modifie":
        m = depot / "src/controle_ia/harnais/modeles.py"
        m.write_text(m.read_text() + "\n# modifié\n")
    elif artefact == "arbre-sale":
        (depot / "en-trop.txt").write_text("x\n")
    elif artefact == "lecture-existante":
        (depot / "runs" / LECTURE).mkdir(parents=True)
        (depot / "runs" / LECTURE / "trace.txt").write_text("x\n")
        committer(depot)
    elif artefact == "entropies":
        def autre(m):
            m = copy.deepcopy(m)
            cle = next(iter(m["graines"]))
            m["graines"][cle]["entropie"] = "1"
            return m
        vrai = lr.lire_manifeste
        monkeypatch.setattr(lr, "lire_manifeste", lambda c: (lambda r: (autre(r[0]), r[1]) if "planb" in str(c)
                                                               else r)(vrai(c)))
    with pytest.raises(GardeArret, match=motif):
        if artefact == "run-absent":
            lr.lire_requalification(depot, RUN, NOTATIONS, "20261020-100009-absent", ANALYSE, depot / "taches.json",
                                    LECTURE, prereg=str(depot / p))
        else:
            _lire(depot, p, **k)
    if artefact != "lecture-existante":
        assert not (depot / "runs" / LECTURE).exists()
    assert not (depot / "diag" / LECTURE).exists()


def test_comparaison_des_modules_a_un_commit_introuvable(tmp_path_factory, monkeypatch):
    depot, h4 = _base(tmp_path_factory)
    _run_planb(depot, monkeypatch, {})
    lr.exiger_modules_geles(depot)                                                       # cas sain
    monkeypatch.setattr(lr, "COMMIT_GELES", "0" * 40)
    with pytest.raises(GardeArret, match="comparaison au commit"):
        lr.exiger_modules_geles(depot)
    with pytest.raises(GardeArret, match="comparaison au commit"):
        lr.exiger_modules_planb(depot, "0" * 40)


@pytest.mark.parametrize("artefact, motif", [
    ("run-pilote", "≠ run du manifeste d'analyse"),
    ("manifeste-pilote", "manifeste du pilote différent"),
    ("juges-pilote", "juges du pilote"),
    ("h4-absentes", "notations H.4 scellées absentes"),
])
def test_gardes_d_entree_du_lecteur(tmp_path_factory, monkeypatch, artefact, motif):
    """Quatre gardes d'entrée du lecteur (R2-02, R3-04 ; sonde R2-3 versée, LR-01 à LR-04) : run du pilote autre que
    celui du manifeste d'analyse ; manifeste du pilote autre que celui de l'analyse ; juges du pilote autres que (8B,
    3B) ; notations H.4 scellées absentes pour un juge. Cas sain : `test_equivalence_avec_les_fonctions_gelees`. Rien
    n'est écrit."""
    depot, h4 = _base(tmp_path_factory)
    p = _run_planb(depot, monkeypatch, _fichiers(h4))
    vrai_p, vrai_n = lr.charger_pilote, lr.charger_notations
    if artefact == "manifeste-pilote":
        monkeypatch.setattr(lr, "charger_pilote", lambda *a: {**vrai_p(*a), "manifeste_sha256": "0" * 64})
    elif artefact == "juges-pilote":
        monkeypatch.setattr(lr, "charger_pilote", lambda *a: {**vrai_p(*a), "juges": ["8B"]})
    elif artefact == "h4-absentes":
        def charger(*a):
            m, sha, h4_, issue = vrai_n(*a)
            return m, sha, {**h4_, "3B": None}, issue
        monkeypatch.setattr(lr, "charger_notations", charger)
    with pytest.raises(GardeArret, match=motif):
        if artefact == "run-pilote":
            lr.lire_requalification(depot, "20261012-999999-autre", NOTATIONS, PLANB, ANALYSE, depot / "taches.json",
                                    LECTURE, prereg=str(depot / p))
        else:
            _lire(depot, p)
    assert not (depot / "runs" / LECTURE).exists() and not (depot / "diag" / LECTURE).exists()


def test_annexe_a_du_texte_scelle_alteree_arrete_la_lecture(tmp_path_factory, monkeypatch):
    """D-6 (R2-2-04) : la lecture extrait l'annexe A du préenregistrement sous lequel le run a été lancé, par la règle
    de `LISEZMOI.md`, et l'exige égale à `RS1.txt` octet pour octet. Artefact : un texte scellé dont l'annexe A diffère
    d'un caractère ; arrêt, rien n'est écrit. Cas sain : toutes les lectures de ce fichier (annexe A comme au texte)."""
    depot, h4 = _base(tmp_path_factory)
    base = (depot / _BASE["prereg"]).read_text(encoding="utf-8")
    p = "prereg/prereg-planb-annexe-alteree.md"
    assert base.count("should be rare.") == 1
    (depot / p).write_text(base.replace("should be rare.", "should be rarE."), encoding="utf-8")
    sceller(depot / p)
    committer(depot)
    _run_planb(depot, monkeypatch, _fichiers(h4), prereg=p)
    with pytest.raises(GardeArret, match=r"annexe A du préenregistrement ≠ RS1\.txt"):
        _lire(depot, p)
    assert not (depot / "runs" / LECTURE).exists() and not (depot / "diag" / LECTURE).exists()


def test_relecture_rs1_compte_les_occurrences_lues_suivies_d_un_chiffre():
    """D-5 : le lecteur recalcule le compte `lues_suite_avec_chiffre` de chaque réponse (sans effet sur la lecture), le
    somme et le rapporte ; un compte consigné autre que le compte recalculé arrête (artefact)."""
    bloc = "\nCOVERAGE: 4\nRIGOR: 2\nFEASIBILITY: 3\nJUSTIFICATION: ok.\n"
    textes = ["SPECIFICITY: 3 vs 4" + bloc, "SPECIFICITY: 3 (out of 5)" + bloc, "SPECIFICITY: 3" + bloc,
              "SPECIFICITY: 3 to 4" + bloc]
    notations = []
    for k, t in enumerate(textes):
        r = lire_reponse_rs1(t, False)
        notations.append({"cle": f"juge-RS1-8B/2601.{k:05d}v1/e0/passe-0", "variante": "RS1", "reponse": t,
                          "tronquee": False, "jetons_reponse": 20, "jetons_contexte": 2000, "notes": r["notes"],
                          "anomalies": r["anomalies"], "score": r["score"],
                          "complete_sans_troncature": r["complete_sans_troncature"], "lecture_rs1": r["lecture"]})
    d = lr.relire_notations_rs1(notations, "8B", 3072)
    assert (d["lues_suite_avec_chiffre"], d["completes"], d["intervalles"]) == (2, 3, 1)
    faux = copy.deepcopy(notations)
    faux[1]["lecture_rs1"]["lues_suite_avec_chiffre"] = 0
    with pytest.raises(GardeArret, match="lecture RS1 recalculée ≠ lecture consignée"):
        lr.relire_notations_rs1(faux, "8B", 3072)


@pytest.mark.parametrize("champ, valeur, motif", [
    ("chemin", {"L1": 0, "L2": 1}, "décalages réellement passés"),                 # D1 injecté dans L2 du chemin
    ("chemin", {"L1": 1, "L2": 1}, "décalages réellement passés"),
    ("chemin", {"L1": 0}, "décalages réellement passés"),
    ("d1", {"L3": 0}, "décalages réellement passés"),                              # D1 jamais injecté
    ("d1", {"L3": 2}, "décalages réellement passés"),
    ("d1", None, "champ « decalages_passes » absent"),
])
def test_decalages_passes_exiges_au_chemin_et_a_d1(champ, valeur, motif):
    """D-10 (R3-01) : le lanceur consigne, par palier, le décalage réellement passé à chaque lot ; le lecteur exige 0 à
    chaque lot du palier du chemin et `decalage_d1` au lot de D1 (cas sain : `_simple`, comme le lanceur) ; tout
    autre décalage, ou le champ absent, arrête."""
    s = _simple("8B", C16, D8)
    assert lr.bilan_chemin(s, "8B", C16)["lecture"] == "fidèle"                       # cas sain
    t = copy.deepcopy(s)
    if valeur is None:
        del t[champ]["decalages_passes"]
    else:
        t[champ]["decalages_passes"] = valeur
    with pytest.raises(GardeArret, match=motif):
        lr.bilan_chemin(t, "8B", C16)


def test_tirage_des_lots_recalcule_cas_sain_et_artefacts(tmp_path_factory):
    """D-14 (R2-07) : cadre recalculé sur les notations H.4 scellées, lots tirés par `generateur(graines(["rejeu/<J>/
    lots"], entropie)[…])`, par le code du lecteur ; égal au tirage des fonctions du lanceur (cas sain) ; tirage
    consigné, ordre des rangées (demi-précision et chemin : L1 puis L2 ; D1 : L3), autre clé ou autre entropie, cadre
    autre, cadre de moins de 3 lots : arrêt (artefacts)."""
    _, h4 = _base(tmp_path_factory)
    f = _fichiers(h4)
    for j in JUGES:
        lots = lr.lots_du_rejeu(h4[j], j, ENTROPIE_PLANB, 8, 3072)
        assert lots["tirage"] == f[f"rejeu-{j}-demi"]["tirage"] == f[f"rejeu-{j}-simple"]["tirage"]  # cas sain
        lr.exiger_lots_du_rejeu(f[f"rejeu-{j}-demi"], f[f"rejeu-{j}-simple"], lots, j)
        lr.exiger_lots_du_rejeu(f[f"rejeu-{j}-demi"], None, lots, j)            # palier du chemin échu
    lots = lr.lots_du_rejeu(h4["8B"], "8B", ENTROPIE_PLANB, 8, 3072)
    demi, simple = f["rejeu-8B-demi"], f["rejeu-8B-simple"]
    t = lots["tirage"]

    def artefact(d=demi, s=simple, attendu=lots, motif="tirage consigné"):
        with pytest.raises(GardeArret, match=motif):
            lr.exiger_lots_du_rejeu(d, s, attendu, "8B")

    artefact(d=dict(demi, tirage=dict(t, L1=t["L3"], L3=t["L1"])))                    # L1 et L3 échangés
    artefact(d=None, s=dict(simple, tirage=dict(t, cadre=t["cadre"][1:])))
    artefact(d={k: v for k, v in demi.items() if k != "tirage"}, motif="champ « tirage » absent")
    inverse = copy.deepcopy(demi)
    inverse["rangees"][0], inverse["rangees"][8] = inverse["rangees"][8], inverse["rangees"][0]
    artefact(d=inverse, motif="clés de « rangees »")                                  # L2 avant L1
    chemin = copy.deepcopy(simple)
    chemin["chemin"]["rangees"] = chemin["chemin"]["rangees"][8:] + chemin["chemin"]["rangees"][:8]
    artefact(s=chemin, motif="clés de « chemin.rangees »")
    d1 = copy.deepcopy(simple)
    d1["d1"]["rangees"] = d1["chemin"]["rangees"][:8]
    artefact(s=d1, motif="clés de « d1.rangees »")                                    # D1 rejoué sur L1
    # lanceur qui aurait tiré par une autre clé (RQ-24), sous une autre entropie, ou dans un autre cadre, et consigné
    # ce tirage sous la clé `rejeu/8B/lots` : le tirage recalculé ne le suit pas
    h4_autre = copy.deepcopy(h4["8B"])
    for x in h4_autre[:8]:
        x["tronquee"] = False                                                          # lot 0 hors du cadre
    assert lr.lots_du_rejeu(h4_autre, "8B", ENTROPIE_PLANB, 8, 3072)["tirage"]["cadre"] == list(range(1, 8))
    for faux in (lr.lots_du_rejeu(h4["8B"], "3B", ENTROPIE_PLANB, 8, 3072),
                 lr.lots_du_rejeu(h4["8B"], "8B", ENTROPIE_PLANB + 1, 8, 3072),
                 lr.lots_du_rejeu(h4_autre, "8B", ENTROPIE_PLANB, 8, 3072)):
        consigne = dict(faux["tirage"], cle="rejeu/8B/lots")
        assert consigne != t
        artefact(d=dict(demi, tirage=consigne), s=None)
    with pytest.raises(GardeArret, match="cadre de 2 lot"):
        lr.lots_du_rejeu(h4["3B"][:16], "3B", ENTROPIE_PLANB, 8, 3072)


def test_tirage_consigne_autre_arrete_la_lecture(tmp_path_factory, monkeypatch):
    """D-14 de bout en bout : un `rejeu-3B-simple.json` dont le palier du chemin porte les rangées de L2 puis L1 :
    arrêt de la lecture, rien n'est écrit (cas sain : `test_equivalence_avec_les_fonctions_gelees`)."""
    depot, h4 = _base(tmp_path_factory)
    s = _simple_du_run(h4, "3B")
    s["chemin"]["rangees"] = s["chemin"]["rangees"][8:] + s["chemin"]["rangees"][:8]
    p = _run_planb(depot, monkeypatch, _fichiers(h4, **{"rejeu-3B-simple": s}))
    with pytest.raises(GardeArret, match=r"rejeu-3B-simple\.json : clés de « chemin\.rangees »"):
        _lire(depot, p)
    assert not (depot / "runs" / LECTURE).exists() and not (depot / "diag" / LECTURE).exists()


# --- Lectures de bout en bout : déclencheur, réserve, commande ---------------------------------------------------------

def test_effondrement_des_notes_suspend_la_lecture(tmp_path_factory, monkeypatch):
    """Toutes les réponses RS1 du 3B à la même somme : déclencheur neuf « trop propre », décomposition impossible
    (déclencheur gelé « trop sale ») ; lecture suspendue ; 3B en nœud ; le 8B se lit."""
    depot, h4 = _base(tmp_path_factory)
    f = _fichiers(h4)
    f["notations-RS1-3B-decisives"] = _fichier_notations(_rs1(h4["3B"], "3B", meme_somme=True))
    p = _run_planb(depot, monkeypatch, f)
    lecture = _lire(depot, p)
    a = lecture["audit_r4"]
    assert "juge RS1-3B : somme la plus fréquente sur plus de 50 % des réponses complètes" in a["trop_propre"]
    assert any(x.startswith("juge RS1-3B : décomposition impossible") for x in a["trop_sale"])
    assert lecture["lecture_suspendue"] and lecture["table_a"]["3B"]["issue"] == "nœud"
    assert lecture["table_a"]["8B"]["issue"] == "RS1 retenue"
    assert lecture["difference_appariee"]["borne"] is None


def test_sous_reserve_de_demi_precision_de_bout_en_bout(tmp_path_factory, monkeypatch):
    """Repère du 3B très petit : palier de production en « réserve (ρ) » ; lecture combinée « propriété du modèle, sous
    réserve de demi-précision » ; PB8 « non concluant » ; déclencheur d'audit ; la requalification se lit selon A."""
    depot, h4 = _base(tmp_path_factory)
    f = _fichiers(h4, **{"rejeu-3B-simple": _simple_du_run(h4, "3B", repere=1e-4)})
    p = _run_planb(depot, monkeypatch, f)
    lecture = _lire(depot, p)
    assert lecture["rejeu"]["3B"]["production"]["lecture"] == "réserve (ρ)"
    assert lecture["lecture_combinee"]["lecture"] == "propriété du modèle, sous réserve de demi-précision"
    assert lecture["predictions"]["PB8"] == "non concluant" and lecture["lecture_suspendue"]
    assert all(lecture["table_a"][j]["issue"] == "RS1 retenue" for j in JUGES)


def test_defaut_du_chemin_suspend_la_requalification(tmp_path_factory, monkeypatch):
    depot, h4 = _base(tmp_path_factory)
    cles, _, _ = _lots(h4, "8B")
    s = _remplacer(_simple_du_run(h4, "8B"), "chemin", [3], gen={7: 5e-3, 15: 1e-4, 23: 1e-4}, ctx=1e-4)
    p = _run_planb(depot, monkeypatch, _fichiers(h4, **{"rejeu-8B-simple": s}))
    lecture = _lire(depot, p)
    assert lecture["lecture_combinee"]["lecture"] == "défaut du chemin" and lecture["predictions"]["PB8"] == "réfutée"
    assert all(lecture["table_a"][j]["issue"] == "nœud" for j in JUGES)
    assert lecture["audit_r4"]["rangees_en_cause"] == {"8B": [cles[3]]}


def test_commande_de_lecture(tmp_path_factory, monkeypatch, capsys):
    """La seule commande permise, depuis la racine du dépôt, préenregistrement donné en chemin relatif."""
    depot, h4 = _base(tmp_path_factory)
    p = _run_planb(depot, monkeypatch, _fichiers(h4))
    monkeypatch.chdir(depot)
    assert lr._main(["--run-pilote", RUN, "--run-notations", NOTATIONS, "--run-planb", PLANB, "--run-analyse", ANALYSE,
                     "--taches", "taches.json", "--run-lecture", LECTURE, "--prereg", p]) == 0
    sortie = json.loads(capsys.readouterr().out)
    assert sortie["lecture_combinee"] == "propriété du modèle" and sortie["table_a"] == {"8B": "RS1 retenue",
                                                                                          "3B": "RS1 retenue"}
    assert sortie["predictions"]["PB4"] == "réfutée" and sortie["predictions"]["PB5"] == "non concluant"
    assert verifier_resultat(depot, depot / "diag" / LECTURE / "lecture-planb.json")["run_id"] == LECTURE
