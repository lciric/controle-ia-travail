"""La chaîne de bout en bout, étapes 1 et 2a, manifeste « exploratoire » (GO-2026-11-21-44 ; course sous GO-2026-11-21-48,
bloc de relecture forcée sous GO-2026-11-21-49).

Étape 1 (plan des étapes 0-1, § B.3 à B.5 ; devis de l'étape 1) :
1. génération (huit lots de 16 par appel du générateur) : tranche de mesure de 32 questions, règle d'arrêt (4 réponses ou plus au plafond ; longueur moyenne au-dessus
   de 2 400 jetons ; réussite sous 10 % ou au-dessus de 90 % ; fin du noyau projetée au-delà de l'arrêt des lancements),
   puis les 468 autres ; arrêt avant extraction si plus de 5 % des réponses au plafond ou plus de 25 % sans boîte ;
2. extraction des couches du noyau (2, 3, 4), garde de position, confiance par jeton ;
3. NOYAU : vérité plantée (couche 3, cinq plis ; borne basse sous 0,9 : arrêt, la chaîne est fausse), couches 2 à 4 (cinq
   plis, graine 0), étiquettes permutées (couche 3, cinq plis) ;
4. BLOCS, dans l'ordre, chacun lancé seulement si l'horloge le permet (plus aucun lancement après 5 h 30) : deux graines de
   plus ; validation emboîtée ; couches 7, 15, 23 ; cible gelée ; couches 1 et 5 ; puis la relecture forcée des épisodes
   honnêtes du premier test (si son fichier de contextes est donné).
Chaque étape écrit ses sorties scellées dès qu'elles existent (reprise après coupure ; versement périodique par l'amorce).
Aucun critère n'est appliqué, hors des gardes d'arrêt : mode exploratoire.

Étape 2a (au processeur, après la course) : `executer_etape2a`, sur des épisodes dont les états sont donnés.

Sous-commandes (machine) : `generer` (environnement vLLM), `suite` (tout le reste), `etape2a`.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import time
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..manifeste import config_canonique, creer_manifeste, ecrire_resultat, generateur, lire_manifeste
from ..scellement import verifier
from . import GO_REOUVERTURE, MODE, PAPIER, generation_v1, math500_v1, mesures_2a_v1, relecture_v1, sonde_v1
from .etats_v1 import charger_couche, extraire_par_lots
from .stockage_v1 import ecrire_jsonl, ecrire_lot, etat_lot, graine_derivee, lire_jsonl, lots, nom_lot

TACHES = ["generation", "decoupage", "sonde", "controles"]
COUCHES_NOYAU = (2, 3, 4)
COUCHES_PROGRAMME = (7, 15, 23)
BLOCS = ("graines_supplementaires", "validation_emboitee", "couches_programme", "cible_gelee", "couches_1_5",
         "relecture_forcee")
TRANCHE = {"questions": 32, "plafond_max": 4, "longueur_moyenne_max": 2400, "reussite_min": 0.10, "reussite_max": 0.90}
GENERATION = {"part_plafond_max": 0.05, "part_sans_boite_max": 0.25}
DUREE_SONDE_SUPPOSEE_S = 80          # devis, § 3 (supposé ; chronométré par la course)
EXTRACTION_SUPPOSEE_S = 360          # devis, § 4 : 0,10 h
_RUN = re.compile(r"^[0-9]{8}-[0-9]{6}-[a-z0-9-]*exploratoire[a-z0-9-]*$")


def journal(**champs) -> None:
    print(json.dumps({"t": round(time.time(), 1), **champs}, ensure_ascii=False), flush=True)


# --- horloge ---------------------------------------------------------------------------------------------------------

class Horloge:
    """Plus aucun lancement après `fin_lancements_s` (s UTC). `maintenant` est injectable (essais R5)."""

    def __init__(self, fin_lancements_s: float | None, maintenant=time.time):
        if fin_lancements_s is not None and (not isinstance(fin_lancements_s, (int, float)) or fin_lancements_s <= 0):
            raise GardeArret(f"fin des lancements illisible : {fin_lancements_s!r}")
        self.fin, self.maintenant = fin_lancements_s, maintenant

    def peut_lancer(self, quoi: str, duree_prevue_s: float = 0.0) -> bool:
        if self.fin is None:
            return True
        ok = self.maintenant() + max(0.0, duree_prevue_s) < self.fin
        journal(horloge=quoi, peut_lancer=ok, reste_s=round(self.fin - self.maintenant(), 1))
        return ok

    def exiger(self, quoi: str, duree_prevue_s: float = 0.0) -> None:
        if not self.peut_lancer(quoi, duree_prevue_s):
            raise GardeArret(f"horloge : {quoi} ne peut plus partir (arrêt des lancements atteint ou dépassé)")


# --- configuration et manifeste --------------------------------------------------------------------------------------

def config_etape1(*, modele: str, jeu: dict, generateur_nom: str, invite: str = "gabarit_du_modele", jouet: bool = False,
                  recette_generation: dict | None = None, recette_sonde: dict | None = None,
                  couches_noyau=COUCHES_NOYAU, couche_controles: int = 3, graines_supplementaires: int = 2,
                  decoupage: dict | None = None, taux=sonde_v1.TAUX_ELAGAGE_TABLEAU_8, force_verite_plantee: float = 4.0,
                  borne_basse_plantee: float = 0.9, blocs=BLOCS, taille_lot: int = 16, tranche: dict | None = None,
                  seuils_generation: dict | None = None, tolerance_position: float = 0.05, entete: str | None = None,
                  relecture: dict | None = None, lots_par_appel: int = 8) -> dict:
    for b in blocs:
        if b not in BLOCS:
            raise GardeArret(f"bloc {b!r} inconnu ({BLOCS})")
    if (decoupage or {"mode": "plis"})["mode"] != "plis":
        raise GardeArret("étape 1 : découpage en plis exigé (chaque question notée une fois par graine ; plan, § B.3)")
    return {"mode": MODE, "go": GO_REOUVERTURE, "go_course": "GO-2026-11-21-48", "go_relecture": "GO-2026-11-21-49",
            "etape": "1", "papier": PAPIER, "modele": modele, "jouet": jouet, "jeu": jeu, "generateur": generateur_nom,
            "invite": invite, "entete_reponse": entete,
            "recette_generation": recette_generation or dict(generation_v1.RECETTE_TABLEAU_6),
            "recette_sonde": recette_sonde or dict(sonde_v1.RECETTE_TABLEAU_7, gradient="complet"),
            "couches_noyau": list(couches_noyau), "couche_controles": couche_controles,
            "graines_supplementaires": graines_supplementaires,
            "decoupage": decoupage or {"mode": "plis", "plis": 5}, "elagage": "masque, sans réapprentissage",
            "taux_elagage": [float(t) for t in taux], "force_verite_plantee": force_verite_plantee,
            "plantation": "injection dans tous les états", "borne_basse_plantee": borne_basse_plantee,
            "blocs": list(blocs), "taille_lot": taille_lot, "lots_par_appel": lots_par_appel,
            "tranche": tranche or dict(TRANCHE),
            "seuils_generation": seuils_generation or dict(GENERATION), "tolerance_position": tolerance_position,
            "relecture": relecture, "convention_couches": "sortie du bloc l, numérotation à partir de 1"}


def config_etape2a(*, modele: str, episodes: dict, jouet: bool = False, recette_sonde: dict | None = None,
                   couches=COUCHES_PROGRAMME, plis_familles: int = 5, score: str = "v_s0", taux_commun: float = 0.20,
                   taille_lot: int = 16) -> dict:
    if score not in ("v_s0", "v_min", "td_min"):
        raise GardeArret(f"score {score!r} inconnu (v_s0, v_min, td_min)")
    return {"mode": MODE, "go": GO_REOUVERTURE, "etape": "2a", "papier": PAPIER, "modele": modele, "jouet": jouet,
            "episodes": episodes, "recette_sonde": recette_sonde or dict(sonde_v1.RECETTE_TABLEAU_7, gradient="complet"),
            "couches": list(couches), "plis_familles": plis_familles, "score": score, "taux_commun": taux_commun,
            "taille_lot": taille_lot, "convention_couches": "sortie du bloc l, numérotation à partir de 1"}


def exiger_exploratoire(config: dict, run_id: str) -> None:
    if config.get("mode") != MODE or config.get("go") != GO_REOUVERTURE:
        raise GardeArret(f"configuration sans « mode : {MODE} » et « go : {GO_REOUVERTURE} » : refus")
    if not _RUN.match(run_id):
        raise GardeArret(f"identifiant de course {run_id!r} : AAAAMMJJ-HHMMSS-…exploratoire… attendu")


def ouvrir_ou_reprendre(racine: Path, run_id: str, config: dict, *, entropie: int | None = None,
                        autoriser_depot_sale: bool = False, commande: str | None = None) -> tuple[Path, dict]:
    """Crée le manifeste, ou le rouvre si la course existe ; refus si la configuration diffère (R12)."""
    exiger_exploratoire(config, run_id)
    chemin = Path(racine) / "runs" / run_id / "manifeste.json"
    if chemin.exists():
        m, _ = lire_manifeste(chemin)
        if config_canonique(m["config"]) != config_canonique(config):
            raise GardeArret(f"course {run_id} existante avec une autre configuration : reprise refusée")
        return chemin, m
    return creer_manifeste(racine, run_id, config, TACHES, entropie=entropie, decisif=False,
                           autoriser_depot_sale=autoriser_depot_sale, commande=commande)


def dossier_course(racine: Path, run_id: str) -> Path:
    return Path(racine) / "donnees" / run_id


def _diag(racine, chemin_m, nom: str, contenu: dict) -> Path:
    """Résumé scellé rattaché au manifeste ; relu s'il existe déjà (reprise)."""
    from ..manifeste import lire_manifeste as _lm
    m, _ = _lm(chemin_m)
    chemin = Path(racine) / "diag" / m["run_id"] / f"{nom}.json"
    if chemin.exists():
        verifier(chemin)
        return chemin
    return ecrire_resultat(racine, chemin_m, nom, {"mode": MODE, **contenu})


# --- étape 1 : génération --------------------------------------------------------------------------------------------

def textes_invites(questions, config, decoupeur) -> dict[str, str]:
    gab = getattr(decoupeur, "gabarit", None)
    return {q["id"]: math500_v1.invite(q["probleme"], config["invite"], gab) for q in questions}


def exiger_invites(textes: dict, decoupeur, entete: str | None) -> None:
    if entete is None:
        raise GardeArret("en-tête de réponse non déclaré dans la configuration : garde d'invite impossible")
    for i, t in textes.items():
        math500_v1.exiger_invite(t, decoupeur.encoder(t), decoupeur, entete)


def stats_generation(dossier_generations: Path, dossier_notation: Path, ids: list[str]) -> dict:
    gens = {x["id"]: x for f in sorted(Path(dossier_generations).glob("lot-*.jsonl")) for x in lire_jsonl(f)}
    notes = {x["id"]: x for f in sorted(Path(dossier_notation).glob("lot-*.jsonl")) for x in lire_jsonl(f)}
    g = [gens[i] for i in ids]
    n = [notes[i] for i in ids]
    return {"questions": len(ids), "au_plafond": sum(x["fin"] == "longueur" for x in g),
            "longueur_moyenne": float(np.mean([x["n_jetons_reponse"] for x in g])),
            "sans_boite": sum(bool(x["sans_boite"]) for x in n), "reussites": sum(x["recompense"] for x in n),
            "desaccords_strict": sum(x["recompense"] != x["recompense_stricte"] for x in n)}


def regle_tranche(st: dict, seuils: dict, projection_fin_noyau_s: float | None, fin_lancements_s: float | None) -> list:
    motifs = []
    if st["au_plafond"] >= seuils["plafond_max"]:
        motifs.append(f"{st['au_plafond']} réponses au plafond (≥ {seuils['plafond_max']})")
    if st["longueur_moyenne"] > seuils["longueur_moyenne_max"]:
        motifs.append(f"longueur moyenne {st['longueur_moyenne']:.0f} > {seuils['longueur_moyenne_max']}")
    taux = st["reussites"] / st["questions"]
    if not seuils["reussite_min"] <= taux <= seuils["reussite_max"]:
        motifs.append(f"taux de réussite {taux:.2f} hors de [{seuils['reussite_min']} ; {seuils['reussite_max']}]")
    if projection_fin_noyau_s is not None and fin_lancements_s is not None and projection_fin_noyau_s > fin_lancements_s:
        motifs.append("fin du noyau projetée au-delà de l'arrêt des lancements")
    return motifs


def etape_generer(racine, run_id, config, chemin_m, manifeste, questions, decoupeur, gen,
                  horloge: Horloge | None = None) -> dict:
    """Tranche de mesure, règle d'arrêt, puis le reste ; arrêt avant extraction selon les seuils de génération."""
    horloge = horloge or Horloge(None)
    d = dossier_course(racine, run_id)
    g = manifeste["graines"]["generation"]
    textes = textes_invites(questions, config, decoupeur)
    exiger_invites(textes, decoupeur, config.get("entete_reponse"))
    f0 = d / "invite-question-0.txt"
    if etat_lot(f0) != "scelle":
        ecrire_lot(f0, lambda p: p.write_text(textes[questions[0]["id"]], encoding="utf-8"))
    tl, nt = config["taille_lot"], config["tranche"]["questions"]
    if nt % tl:
        raise GardeArret(f"tranche de {nt} questions non multiple de la taille de lot {tl}")
    tranche, reste = questions[:nt], questions[nt:]
    graine = lambda i: graine_derivee(g, f"question/{i}")
    tous_lots = lots(questions, tl)
    n_tranche = nt // tl
    t0 = time.time()
    joues = _generer_groupes(list(enumerate(tous_lots))[:n_tranche], textes, decoupeur, gen, d / "generations", graine,
                             n_tranche)
    duree_tranche = time.time() - t0
    generation_v1.noter_par_lots(questions, d / "generations", d / "notation")
    st = stats_generation(d / "generations", d / "notation", [q["id"] for q in tranche])
    projection = None
    if joues == n_tranche:                                 # tranche jouée ici : sa durée est mesurée
        projection = (time.time() + duree_tranche / len(tranche) * len(reste) + EXTRACTION_SUPPOSEE_S
                      + 25 * DUREE_SONDE_SUPPOSEE_S)
    motifs = regle_tranche(st, config["tranche"], projection, horloge.fin)
    _diag(racine, chemin_m, "etape1-tranche-exploratoire", {"stats": st, "duree_s": duree_tranche,
                                                             "projection_fin_noyau_s": projection, "arret": motifs})
    if motifs:
        raise GardeArret("tranche de mesure : arrêt et destruction — " + " ; ".join(motifs))
    horloge.exiger("génération des questions restantes")
    _generer_groupes(list(enumerate(tous_lots))[n_tranche:], textes, decoupeur, gen, d / "generations", graine,
                     config.get("lots_par_appel", 8))
    generation_v1.noter_par_lots(questions, d / "generations", d / "notation")
    st_all = stats_generation(d / "generations", d / "notation", [q["id"] for q in questions])
    sg = config["seuils_generation"]
    motifs = []
    if st_all["au_plafond"] > sg["part_plafond_max"] * len(questions):
        motifs.append(f"{st_all['au_plafond']} réponses au plafond (> {sg['part_plafond_max']:.0%})")
    if st_all["sans_boite"] > sg["part_sans_boite_max"] * len(questions):
        motifs.append(f"{st_all['sans_boite']} réponses sans boîte (> {sg['part_sans_boite_max']:.0%})")
    _diag(racine, chemin_m, "etape1-generation-exploratoire", {"stats": st_all, "arret": motifs,
                                                               "duree_s": time.time() - t0})
    if motifs:
        raise GardeArret("génération : arrêt avant extraction — " + " ; ".join(motifs))
    return st_all


def _generer_groupes(lots_numerotes, textes, decoupeur, gen, dossier: Path, graine, lots_par_appel: int) -> int:
    """Génère les lots non scellés, `lots_par_appel` lots par appel du générateur (vLLM sert mieux de gros lots), puis
    écrit chaque lot à part, scellé. Un lot déjà scellé doit porter les mêmes questions (reprise). Rend le nombre de lots
    écrits."""
    import hashlib
    if isinstance(lots_par_appel, bool) or not isinstance(lots_par_appel, int) or lots_par_appel < 1:
        raise GardeArret(f"lots par appel {lots_par_appel!r} : entier positif attendu")
    a_faire = []
    for i, lot in lots_numerotes:
        final = dossier / f"{nom_lot(i)}.jsonl"
        if etat_lot(final) == "scelle":
            if [x["id"] for x in lire_jsonl(final)] != [q["id"] for q in lot]:
                raise GardeArret(f"{final.name} : questions différentes de celles du lot {i} (ordre ou jeu changé)")
            continue
        a_faire.append((final, lot))
    for k in range(0, len(a_faire), lots_par_appel):
        groupe = a_faire[k:k + lots_par_appel]
        qs = [q for _, lot in groupe for q in lot]
        invites_ids = [decoupeur.encoder(textes[q["id"]]) for q in qs]
        graines = [int(graine(q["id"])) for q in qs]
        sorties = gen.generer(invites_ids, graines)
        if len(sorties) != len(qs):
            raise GardeArret(f"{len(sorties)} réponses pour {len(qs)} questions")
        o = 0
        for final, lot in groupe:
            ecrire_jsonl(final, [{"id": q["id"], "graine": g, "jetons_invite": ids, "jetons_reponse": s["jetons"],
                                  "n_jetons_reponse": len(s["jetons"]), "texte_reponse": s["texte"], "fin": s["fin"],
                                  "invite_sha256": hashlib.sha256(textes[q["id"]].encode("utf-8")).hexdigest(),
                                  "generateur": gen.nom}
                                 for q, ids, g, s in zip(lot, invites_ids[o:o + len(lot)], graines[o:o + len(lot)],
                                                         sorties[o:o + len(lot)])])
            o += len(lot)
    return len(a_faire)


# --- étape 1 : sondes ------------------------------------------------------------------------------------------------

def _sequences(dossier_etats, couche, ids):
    x = charger_couche(dossier_etats, couche)
    manquants = [i for i in ids if i not in x]
    if manquants:
        raise GardeArret(f"couche {couche} : états absents pour {len(manquants)} questions (ex. {manquants[0]})")
    return [x[i] for i in ids]


def _scelle_json(final: Path, calcul) -> dict:
    if etat_lot(final) == "scelle":
        return json.loads(final.read_text(encoding="utf-8"))
    res = calcul()
    texte = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=1) + "\n"
    ecrire_lot(final, lambda p: p.write_text(texte, encoding="utf-8"))
    return json.loads(texte)


def _sonde_et_grille(config, seq_app, r_app, seq_val, r_val, graine: int, appareil: str, recette: dict,
                     poids: Path | None):
    """Une sonde (apprise une fois), grille des quinze taux par masque ; poids gardés en float16 si demandé."""
    t0 = time.time()
    m = sonde_v1.entrainer(seq_app, r_app, recette, graine, appareil=appareil, jouet=config["jouet"])
    duree = time.time() - t0
    g = sonde_v1.grille_elagage(seq_app, r_app, seq_val, r_val, recette, graine, config["taux_elagage"], False,
                                appareil, jouet=config["jouet"], sonde_complete=m)
    if poids is not None and etat_lot(poids) != "scelle":
        pw = sonde_v1.poids_float16(m)

        def _e(p, pw=pw):
            with open(p, "wb") as f:
                np.savez(f, **{k.replace(".", "_"): v for k, v in pw.items()})
        ecrire_lot(poids, _e)
    return {str(p): v for p, v in g.items()}, duree


def grilles(config, manifeste, seqs: dict, r: np.ndarray, dossier: Path, etiquette: str, appareil: str, couches,
            graines=(0,), recette: dict | None = None, garder_poids: bool = False) -> list[dict]:
    """Pour chaque graine : par pli et par couche, une sonde et sa grille ; lecture du papier (meilleur taux par couche,
    moyenne) par pli ; aire mise en commun sur les plis (toutes les questions une fois)."""
    gd, gs = manifeste["graines"]["decoupage"], manifeste["graines"]["sonde"]
    dc = config["decoupage"]
    recette = recette or config["recette_sonde"]
    n = len(r)
    sorties = []
    for s in graines:
        plis = sonde_v1.decoupages(n, dc["mode"], graine_derivee(gd, f"graine-{s}"), dc.get("part", 0.8),
                                   dc.get("plis", 5))
        par_pli, commun, durees = [], {c: {} for c in couches}, []
        for j, (app, val) in enumerate(plis):
            aires = {}
            for c in couches:
                cle = f"{etiquette}/graine-{s}/pli-{j}/couche-{c}"
                nom = cle.replace("/", "--")
                poids = dossier / "poids" / f"{nom}.npz" if garder_poids else None
                info = {}

                def calc(c=c, cle=cle, poids=poids, info=info):
                    g, du = _sonde_et_grille(config, [seqs[c][i] for i in app], r[app], [seqs[c][i] for i in val],
                                             r[val], graine_derivee(gs, cle), appareil, recette, poids)
                    return {"grille": g, "duree_s": du}
                res = _scelle_json(dossier / f"{nom}.json", calc)
                durees.append(res["duree_s"])
                aires[c] = {float(p): v["aire"] for p, v in res["grille"].items()}
                for p, v in res["grille"].items():
                    commun[c].setdefault(float(p), np.full(n, np.nan))[val] = v["scores"]
            par_pli.append({"pli": j, "validation": int(len(val)), "aires": {str(c): aires[c] for c in aires},
                            "papier": sonde_v1.meilleur_taux(aires)})
        aires_c = {c: {p: sonde_v1.aire_sous_courbe(v, r) for p, v in commun[c].items()} for c in couches}
        sorties.append({"graine": s, "plis": par_pli, "duree_sonde_s_moyenne": float(np.mean(durees)),
                        "aire_papier_moyenne_des_plis": float(np.mean([p["papier"]["aire_au_meilleur_taux"]
                                                                        for p in par_pli])),
                        "mis_en_commun": {"aires": {str(c): aires_c[c] for c in couches},
                                          "papier": sonde_v1.meilleur_taux(aires_c)},
                        "scores_taux_0": {str(c): commun[c][0.0].tolist() for c in couches if 0.0 in commun[c]}})
    return sorties


def ecrire_etats_s0(seqs: dict, ids: list[str], dossier: Path) -> None:
    """Matrice des s_0 par couche (petite, versable) : `couche-LL.npy` (float16) et `couche-LL.ids.json`, scellés."""
    for c, ss in seqs.items():
        fi, fa = Path(dossier) / f"couche-{c:02d}.ids.json", Path(dossier) / f"couche-{c:02d}.npy"
        texte = json.dumps({"couche": c, "ids": ids}, ensure_ascii=False) + "\n"
        if etat_lot(fi) != "scelle":
            ecrire_lot(fi, lambda p, t=texte: p.write_text(t, encoding="utf-8"))
        elif fi.read_text(encoding="utf-8") != texte:
            raise GardeArret(f"{fi} scellé avec d'autres identifiants")
        if etat_lot(fa) != "scelle":
            x0 = np.stack([np.asarray(q[0]) for q in ss]).astype(np.float16)

            def _e(p, t=x0):
                with open(p, "wb") as f:
                    np.save(f, t, allow_pickle=False)
            ecrire_lot(fa, _e)


def exiger_disque(dossier: Path, octets: float, marge: float = 1.2) -> None:
    libre = shutil.disk_usage(Path(dossier) if Path(dossier).exists() else Path(dossier).parent).free
    if libre < octets * marge:
        raise GardeArret(f"disque : {libre / 1e9:.1f} Go libres, {octets * marge / 1e9:.1f} Go demandés")


def _extraire(modele, d: Path, couches, ids, config) -> dict:
    lignes = sum(len(x["jetons_reponse"]) + 1 for f in sorted((d / "generations").glob("lot-*.jsonl"))
                 for x in lire_jsonl(f))
    a_faire = [c for c in couches if not (d / "etats" / f"couche-{c:02d}").exists()]
    if a_faire:
        largeur = modele.config.hidden_size
        exiger_disque(d, lignes * largeur * 2 * len(a_faire))
    extraire_par_lots(modele, d / "generations", couches, d / "etats", "trajectoire", "math500-public",
                      config["tolerance_position"])
    seqs = {c: _sequences(d / "etats", c, ids) for c in couches}
    ecrire_etats_s0(seqs, ids, d / "etats-s0")
    return seqs


def bloc_validation_emboitee(config, manifeste, seqs, r, dossier, appareil) -> dict:
    """Par pli (graine 0) : sonde apprise sur 320 questions, taux choisi sur 80 (meilleur par couche), aire sur les 100."""
    gd, gs = manifeste["graines"]["decoupage"], manifeste["graines"]["sonde"]
    dc = config["decoupage"]
    plis = sonde_v1.decoupages(len(r), dc["mode"], graine_derivee(gd, "graine-0"), dc.get("part", 0.8), dc.get("plis", 5))
    out = []
    for j, (app, val) in enumerate(plis):
        rng = np.random.default_rng(graine_derivee(gd, f"emboite/pli-{j}"))
        perm = rng.permutation(app)
        k = int(round(0.8 * len(app)))
        a_in, v_in = np.sort(perm[:k]), np.sort(perm[k:])
        par_c = {}
        for c in config["couches_noyau"]:
            cle = f"emboite/pli-{j}/couche-{c}"

            def calc(c=c, cle=cle):
                m = sonde_v1.entrainer([seqs[c][i] for i in a_in], r[a_in], config["recette_sonde"],
                                       graine_derivee(gs, cle), appareil=appareil, jouet=config["jouet"])
                gi = sonde_v1.grille_elagage([seqs[c][i] for i in a_in], r[a_in], [seqs[c][i] for i in v_in], r[v_in],
                                             config["recette_sonde"], 0, config["taux_elagage"], False, appareil,
                                             jouet=config["jouet"], sonde_complete=m)
                choix = max(gi, key=lambda p: (gi[p]["aire"], -p))
                go = sonde_v1.grille_elagage([seqs[c][i] for i in a_in], r[a_in], [seqs[c][i] for i in val], r[val],
                                             config["recette_sonde"], 0, (choix,), False, appareil,
                                             jouet=config["jouet"], sonde_complete=m)
                return {"taux_choisi": choix, "aire": go[choix]["aire"]}
            par_c[str(c)] = _scelle_json(dossier / f"{cle.replace('/', '--')}.json", calc)
        out.append({"pli": j, "couches": par_c, "aire_moyenne": float(np.mean([v["aire"] for v in par_c.values()]))})
    return {"plis": out, "aire_emboitee": float(np.mean([p["aire_moyenne"] for p in out]))}


def controle_plante(config, manifeste, chemin_m, racine, seqs, r, d, appareil) -> dict:
    """Vérité plantée (couche des contrôles, tous les plis). Garde : lecture par pli (réponse 39 de Fable, option c) —
    arrêt si la borne basse du pire pli est sous le seuil ; l'aire mise en commun (brute, recalée) est rapportée à côté."""
    sonde_v1.exiger_terme_final(config["recette_sonde"]["gamma"])
    rng = generateur(manifeste["graines"]["controles"])
    cc = config["couche_controles"]
    inj, r_plant, _ = sonde_v1.injecter_verite({cc: seqs[cc]}, config["force_verite_plantee"], rng)
    g_plant = grilles(config, manifeste, inj, r_plant, d / "sondes", "noyau-plantee", appareil, [cc], garder_poids=True)
    scores = np.array(g_plant[0]["scores_taux_0"][str(cc)])
    plis = sonde_v1.decoupages(len(r), config["decoupage"]["mode"],
                               graine_derivee(manifeste["graines"]["decoupage"], "graine-0"),
                               config["decoupage"].get("part", 0.8), config["decoupage"].get("plis", 5))
    groupes = np.full(len(r), -1)
    for j, (_, val) in enumerate(plis):
        groupes[val] = j
    vus = groupes >= 0
    plantee = {"couche": cc, "force": config["force_verite_plantee"], "issues_plantees": int(r_plant.sum()),
               "lecture_de_la_garde": "pire pli (réponse 39 de Fable, option c)", "grilles": g_plant}
    try:                                   # la lecture de la garde d'abord : tout arrêt écrit son diagnostic
        lecture = sonde_v1.lecture_plantee_par_pli(
            scores[vus], r_plant[vus], groupes[vus],
            np.random.default_rng(graine_derivee(manifeste["graines"]["controles"], "garde-plantee-par-pli")),
            seuil=config["borne_basse_plantee"])
    except GardeArret as e:
        lecture = {"arret": [str(e)], "plis": []}
    plantee["garde"] = lecture
    if not lecture["arret"]:               # rapporté à côté, sans arrêter (lecture commune de la v1)
        plantee["aire_taux_0"] = sonde_v1.aire_sous_courbe(scores[vus], r_plant[vus])
        plantee["intervalle_95"] = list(sonde_v1.intervalle_aire(
            scores[vus], r_plant[vus], generateur(manifeste["graines"]["controles"]), groupes=groupes[vus]))
    if lecture["arret"]:
        _diag(racine, chemin_m, "etape1-noyau-arret-exploratoire", {"verite_plantee": plantee})
        raise GardeArret("vérité plantée : " + " ; ".join(lecture["arret"]) + " — la chaîne est fausse : arrêt du noyau")
    return plantee


def noyau(config, manifeste, chemin_m, racine, seqs, r, d, appareil) -> dict:
    """Vérité plantée (arrêt si elle échoue), couches du noyau (graine 0), étiquettes permutées (couche des contrôles)."""
    plantee = controle_plante(config, manifeste, chemin_m, racine, seqs, r, d, appareil)
    cc = config["couche_controles"]
    rng = generateur(manifeste["graines"]["controles"])
    rng.integers(0, 2, len(r))                         # même tirage que l'injection, consommé : permutation indépendante
    r_perm = sonde_v1.etiquettes_permutees(r, rng)
    g_princ = grilles(config, manifeste, seqs, r, d / "sondes", "noyau", appareil, config["couches_noyau"],
                      garder_poids=True)
    g_perm = grilles(config, manifeste, seqs, r_perm, d / "sondes", "noyau-permutees", appareil, [cc],
                     garder_poids=True)
    return {"questions": len(r), "reussites": int(r.sum()), "verite_plantee": plantee, "principal": g_princ,
            "etiquettes_permutees": g_perm,
            "aire_papier": g_princ[0]["aire_papier_moyenne_des_plis"],
            "aire_papier_mise_en_commun": g_princ[0]["mis_en_commun"]["papier"]["aire_au_meilleur_taux"],
            "aire_taux_0_mise_en_commun": g_princ[0]["mis_en_commun"]["papier"]["aire_au_taux_0"],
            "permutees_taux_0_mise_en_commun": g_perm[0]["mis_en_commun"]["papier"]["aire_au_taux_0"],
            "permutees_meilleur_taux": g_perm[0]["aire_papier_moyenne_des_plis"]}


def etape_suite(racine, run_id, config, chemin_m, manifeste, questions, modele, appareil: str,
                horloge: Horloge | None = None, decoupeur=None, contextes: Path | None = None,
                liste_honnetes: set[str] | None = None) -> Path:
    """Notation, extraction du noyau, noyau, blocs sous l'horloge. Rend le chemin du résumé final scellé."""
    horloge = horloge or Horloge(None)
    d = dossier_course(racine, run_id)
    generation_v1.noter_par_lots(questions, d / "generations", d / "notation")
    ids = [q["id"] for q in questions]
    recomp = generation_v1.lire_recompenses(d / "notation")
    if set(recomp) != set(ids):
        raise GardeArret("notation incomplète : toutes les questions doivent être notées avant les sondes")
    r = np.array([recomp[i] for i in ids])
    seqs = _extraire(modele, d, config["couches_noyau"], ids, config)
    longueurs = {x["id"]: len(x["jetons_invite"]) for f in sorted((d / "generations").glob("lot-*.jsonl"))
                 for x in lire_jsonl(f)}
    conf = {}
    for f in sorted((d / "etats" / "confiance-jeton").glob("lot-*.json")):
        verifier(f)
        conf.update(json.loads(f.read_text(encoding="utf-8"))["confiance_jeton"])
    base = {"longueur_question": {"aire": sonde_v1.aire_sous_courbe(-np.array([longueurs[i] for i in ids]), r),
                                  "sens": "score = − nombre de jetons de l'invite"},
            "confiance_jeton": {"aire": sonde_v1.aire_sous_courbe(np.array([conf[i] for i in ids]), r),
                                "sens": "probabilité du jeton le plus probable après l'invite"}}
    t0 = time.time()
    res_noyau = noyau(config, manifeste, chemin_m, racine, seqs, r, d, appareil)
    res_noyau.update({"comparateurs_sans_critere": base, "duree_s": time.time() - t0})
    _diag(racine, chemin_m, "etape1-noyau-exploratoire", res_noyau)
    duree_sonde = max(1.0, float(res_noyau["principal"][0]["duree_sonde_s_moyenne"]))
    faits, non_lances = [], []
    for b in config["blocs"]:
        sondes = {"graines_supplementaires": 15 * config["graines_supplementaires"], "validation_emboitee": 15,
                  "couches_programme": 15, "cible_gelee": 15, "couches_1_5": 10, "relecture_forcee": 0}[b]
        if b == "relecture_forcee" and contextes is None:
            non_lances.append({"bloc": b, "motif": "aucun fichier de contextes donné"})
            continue
        if not horloge.peut_lancer(b, 0.0):
            non_lances.append({"bloc": b, "motif": "horloge : arrêt des lancements atteint"})
            continue
        t0 = time.time()
        try:
            res = _bloc(b, config, manifeste, seqs, r, d, appareil, modele, ids, decoupeur, contextes, liste_honnetes)
        except GardeArret as e:
            non_lances.append({"bloc": b, "motif": f"garde : {e}"})
            journal(bloc=b, garde=str(e))
            if b == "relecture_forcee":
                raise
            continue
        res["duree_s"] = time.time() - t0
        res["sondes_prevues"] = sondes
        _diag(racine, chemin_m, f"etape1-bloc-{b.replace('_', '-')}-exploratoire", res)
        faits.append(b)
    return _diag(racine, chemin_m, "etape1-fin-exploratoire",
                 {"blocs_faits": faits, "blocs_non_faits": non_lances, "duree_sonde_s": duree_sonde})


def _bloc(b, config, manifeste, seqs, r, d, appareil, modele, ids, decoupeur, contextes, liste_honnetes) -> dict:
    noy = config["couches_noyau"]
    if b == "graines_supplementaires":
        g = grilles(config, manifeste, seqs, r, d / "sondes", "graines", appareil, noy,
                    graines=tuple(range(1, 1 + config["graines_supplementaires"])))
        return {"grilles": g, "aires_papier": [x["aire_papier_moyenne_des_plis"] for x in g]}
    if b == "validation_emboitee":
        return bloc_validation_emboitee(config, manifeste, seqs, r, d / "sondes", appareil)
    if b in ("couches_programme", "couches_1_5"):
        cs = list(COUCHES_PROGRAMME) if b == "couches_programme" else [1, 5]
        sq = _extraire(modele, d, cs, ids, config)
        g = grilles(config, manifeste, sq, r, d / "sondes", b.replace("_", "-"), appareil, cs)
        return {"grilles": g, "aires_par_couche_mise_en_commun": g[0]["mis_en_commun"]["aires"]}
    if b == "cible_gelee":
        rec = dict(config["recette_sonde"], gradient="semi")
        g = grilles(config, manifeste, seqs, r, d / "sondes", "cible-gelee", appareil, noy, recette=rec)
        return {"grilles": g, "aire_papier": g[0]["aire_papier_moyenne_des_plis"]}
    if b == "relecture_forcee":
        rl = config.get("relecture") or {}
        if rl.get("contextes_sha256") and verifier(contextes) != rl["contextes_sha256"]:
            raise GardeArret("contextes de la relecture : empreinte ≠ celle de la configuration")
        return relecture_v1.relire(modele, decoupeur, contextes, list(COUCHES_PROGRAMME), d / "relecture-forcee",
                                   liste_honnetes, config["tolerance_position"])
    raise GardeArret(f"bloc {b!r} inconnu")


# --- étape 2a --------------------------------------------------------------------------------------------------------

def _score_v_s0(v):
    return float(v[0])


def _score_v_min(v):
    return float(np.min(v))


def _score_td_min(v):
    return float(np.min(v[1:] - v[:-1])) if len(v) > 1 else 0.0


SCORES_2A = {"v_s0": _score_v_s0, "v_min": _score_v_min, "td_min": _score_td_min}


def ecrire_episodes(episodes: list[dict], dossier: Path, taille_lot: int) -> None:
    """Les épisodes au format des lots de génération (l'extraction les relit à l'identique) ; reprise par lot."""
    for cle in ("id", "famille", "jetons_invite", "jetons_reponse", "recompense"):
        if any(cle not in e for e in episodes):
            raise GardeArret(f"épisode sans champ {cle}")
    for i, lot in enumerate(lots(episodes, taille_lot)):
        final = Path(dossier) / f"{nom_lot(i)}.jsonl"
        if etat_lot(final) == "scelle":
            continue
        ecrire_jsonl(final, [{"id": e["id"], "famille": e["famille"], "jetons_invite": list(e["jetons_invite"]),
                              "jetons_reponse": list(e["jetons_reponse"]), "recompense": int(e["recompense"]),
                              "fin": "arret", "texte_reponse": ""} for e in lot])


def plis_par_famille(familles, plis: int, graine: int) -> list[tuple[np.ndarray, np.ndarray]]:
    noms = np.unique(np.asarray(familles))
    if len(noms) < plis:
        raise GardeArret(f"{len(noms)} familles pour {plis} plis")
    rng = np.random.default_rng(int(graine))
    groupes = np.array_split(rng.permutation(noms), plis)
    f = np.asarray(familles)
    return [(np.flatnonzero(~np.isin(f, g)), np.flatnonzero(np.isin(f, g))) for g in groupes]


def executer_etape2a(racine, run_id, config, chemin_m, manifeste, episodes: list[dict], modele, appareil: str) -> Path:
    d = dossier_course(racine, run_id)
    ecrire_episodes(episodes, d / "episodes", config["taille_lot"])
    extraire_par_lots(modele, d / "episodes", config["couches"], d / "etats", "trajectoire", "episode-du-programme")
    ids = [e["id"] for e in episodes]
    r = np.array([int(e["recompense"]) for e in episodes])
    fam = np.array([e["famille"] for e in episodes])
    gd, gs = manifeste["graines"]["decoupage"], manifeste["graines"]["sonde"]
    plis = plis_par_famille(fam, config["plis_familles"], graine_derivee(gd, "familles"))
    score = SCORES_2A[config["score"]]
    resume = {"mode": MODE, "etape": "2a", "episodes": len(ids), "familles": int(len(np.unique(fam))),
              "reussites": int(r.sum()), "score": config["score"], "couches": {}}
    for c in config["couches"]:
        seqs = _sequences(d / "etats", c, ids)
        valeurs = [None] * len(ids)
        for j, (app, val) in enumerate(plis):
            m = sonde_v1.entrainer([seqs[i] for i in app], r[app], config["recette_sonde"],
                                   graine_derivee(gs, f"couche-{c}/pli-{j}"), appareil=appareil, jouet=config["jouet"])
            torch = sonde_v1._torch()
            with torch.no_grad():
                for i in val:
                    x = torch.as_tensor(np.asarray(seqs[i], dtype=np.float32), device=appareil)
                    valeurs[i] = m(x).squeeze(-1).cpu().numpy().astype(float)
        s = np.array([score(v) for v in valeurs])
        v0 = np.array([v[0] for v in valeurs])
        pas = mesures_2a_v1.correlation_pas_suivant(valeurs)
        lot_a = np.isin(fam, np.unique(fam)[0::2])
        res = {"aire_hors_famille_v_s0": sonde_v1.aire_sous_courbe(v0, r),
               "correlation_pas_suivant": pas,
               "taille_effective_pas": mesures_2a_v1.taille_effective_serie(pas["couples"], pas["rho"]),
               "alerte_par_famille": mesures_2a_v1.correlation_alerte_par_famille(s, fam, config["taux_commun"]),
               "taux_alerte_entre_lots": mesures_2a_v1.taux_alerte_entre_lots(s[lot_a], s[~lot_a],
                                                                              config["taux_commun"])}
        resume["couches"][str(c)] = res
    return ecrire_resultat(racine, chemin_m, "etape2a-exploratoire", resume)




# --- ligne de commande (machine) -------------------------------------------------------------------------------------

def _main(argv: list[str]) -> int:
    from . import modele_v1

    p = argparse.ArgumentParser(prog="course_v1")
    p.add_argument("sous_commande", choices=("generer", "suite", "etape2a"))
    p.add_argument("--racine", required=True)
    p.add_argument("--run-id", required=True)
    p.add_argument("--jeu")
    p.add_argument("--episodes")
    p.add_argument("--modele-local", required=True)
    p.add_argument("--generateur", choices=("vllm", "transformers"))
    p.add_argument("--invite", choices=math500_v1.MODES_INVITE, default="gabarit_du_modele")
    p.add_argument("--fin-lancements-utc-s", type=float)
    p.add_argument("--contextes")
    p.add_argument("--contextes-sha256")
    p.add_argument("--liste-honnetes")
    p.add_argument("--appareil", default="cuda")
    a = p.parse_args(argv)
    racine = Path(a.racine)
    if a.sous_commande == "etape2a":
        if not a.episodes:
            raise GardeArret("étape 2a : --episodes attendu")
        sha_ep = verifier(a.episodes)
        episodes = [json.loads(l) for l in Path(a.episodes).read_text(encoding="utf-8").splitlines() if l.strip()]
        config = config_etape2a(modele=modele_v1.MODELE_DU_PROGRAMME, episodes={"chemin": a.episodes, "sha256": sha_ep})
        chemin_m, m = ouvrir_ou_reprendre(racine, a.run_id, config, commande=" ".join(["course_v1", *argv]))
        modele, _ = modele_v1.charger(modele_v1.MODELE_DU_PROGRAMME, a.modele_local, a.appareil)
        print(executer_etape2a(racine, a.run_id, config, chemin_m, m, episodes, modele, a.appareil))
        return 0
    if not a.jeu or not a.generateur or a.fin_lancements_utc_s is None:
        raise GardeArret("étape 1 : --jeu, --generateur et --fin-lancements-utc-s attendus")
    questions, sha_jeu = math500_v1.lire_math500(a.jeu)
    relecture = ({"contextes": a.contextes, "contextes_sha256": a.contextes_sha256} if a.contextes else None)
    config = config_etape1(modele=modele_v1.MODELE_DU_PROGRAMME, jeu={"nom": "HuggingFaceH4/MATH-500", "sha256": sha_jeu},
                           generateur_nom=a.generateur, invite=a.invite,
                           entete=modele_v1.ENTETE_REPONSE_LLAMA if a.invite == "gabarit_du_modele"
                           else "<|im_start|>assistant\n", relecture=relecture)
    chemin_m, m = ouvrir_ou_reprendre(racine, a.run_id, config, commande=" ".join(["course_v1", a.sous_commande]))
    horloge = Horloge(a.fin_lancements_utc_s)
    from transformers import AutoTokenizer, GenerationConfig

    tok = AutoTokenizer.from_pretrained(a.modele_local)
    gc = GenerationConfig.from_pretrained(a.modele_local)
    dec = modele_v1.DecoupeurHF(tok, gc.eos_token_id if isinstance(gc.eos_token_id, list) else [gc.eos_token_id])
    if a.sous_commande == "generer":
        if a.generateur == "vllm":
            gen = generation_v1.GenerateurVllm(a.modele_local, config["recette_generation"],
                                               math500_v1.ARRETS_QWEN_BOXED)
        else:
            modele, dec = modele_v1.charger(modele_v1.MODELE_DU_PROGRAMME, a.modele_local, a.appareil)
            gen = generation_v1.GenerateurTransformers(modele, dec, config["recette_generation"],
                                                       math500_v1.ARRETS_QWEN_BOXED)
        print(json.dumps(etape_generer(racine, a.run_id, config, chemin_m, m, questions, dec, gen, horloge)))
        return 0
    modele, dec = modele_v1.charger(modele_v1.MODELE_DU_PROGRAMME, a.modele_local, a.appareil)
    liste = None
    if a.liste_honnetes:
        verifier(a.liste_honnetes)
        liste = set(json.loads(Path(a.liste_honnetes).read_text(encoding="utf-8")))
    print(etape_suite(racine, a.run_id, config, chemin_m, m, questions, modele, a.appareil, horloge, dec,
                      Path(a.contextes) if a.contextes else None, liste))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"GARDE : {e}", file=sys.stderr)
        sys.exit(3)
