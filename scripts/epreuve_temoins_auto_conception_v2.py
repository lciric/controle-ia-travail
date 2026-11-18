#!/usr/bin/env python3
"""Épreuve des témoins du juge — course d'auto-conception de l'organisme d'idéation, version 2.

Version 2 (R12 ; la v1, `scripts/epreuve_temoins_auto_conception_v1.py`, `5e354e7d…`, reste en place) — contre-lecture de la
v1 par le modèle K : témoins v2 (constat 2) ; l'épreuve hors ligne éprouve aussi la **longueur du seul champ lu par chaque
item** (règle de seuil par champ, et un juge factice qui la suit) et dit sa limite (constat 4) : elle éprouve un plancher de
lecture de forme, jamais le pouvoir de discrimination d'un juge sur des défauts non déclarés ; le rapport réel garde les
**verdicts et classes bruts**, pour que le lanceur recalcule le verdict (constat 11).

Texte de la v1 :

Épreuve des témoins du juge — course d'auto-conception de l'organisme d'idéation, version 1.

Leçon des courses passées (R-3221, R-3229, R-3234 ; course v7 des organismes discrets finie en code 4, témoins échoués chez
un juge) : des témoins mal écrits rendent une course illisible ; ils s'éprouvent **avant** toute course, et rien ne part sans
cette épreuve réussie. Les témoins (`temoins-juge-auto-conception-v1.json`) sont des cartes de conception plantées, bonnes et
mauvaises, de classe connue par construction, écrites à la lettre de la consigne du juge.

Deux modes, la même lecture (`lire_epreuve`) :

- `--hors-ligne SORTIE_NEUVE [--matiere MATIERE.md]` : aucun appel. Les témoins sont servis par les **vraies** fonctions de
  service de l'orchestrateur épinglé (`fiches_v54.entree_une_fiche`, garde A4 comprise ; lecture par `lire_verdict` et
  `lire_classe`) à des juges factices : un juge parfait (rend la vérité plantée), des juges au hasard (graines dérivées par
  `numpy.random.SeedSequence`, R9), un juge biaisé vers la longueur, un juge indulgent, un juge sévère ; un aiguilleur
  parfait et un aiguilleur artefact. Il montre que les témoins **séparent** le juge parfait des autres, qu'aucune règle de
  seuil sur la longueur ne les classe, que leurs champs tiennent dans les bornes de la consigne, que chaque identifiant du
  catalogue qu'ils citent existe dans la matière servie, et qu'aucun titre de témoin n'apparaît dans la consigne servie.
- `--reel` (session d'exécution seulement, jamais lancé ici) : les juges et l'aiguilleur **de la configuration de la course**,
  par les relais déclarés pour l'épreuve (`declaration-relais-epreuve-temoins-auto-conception-v1.json`, scellée), sous la
  ligne de GO de l'épreuve (pièce de départ de la mère), plafond 5 USD ; écrit, scellé, le rapport que le lanceur de la course
  exige (`course-v1/epreuve-temoins-reelle-auto-conception-v1.json`). **Règle écrite d'avance** : un témoin manqué par un juge
  ou par l'aiguilleur → verdict « échouée » → aucune course, et aucune retouche des témoins sans version neuve (R12) et mot de
  la mère. Plafond atteint, refus pour crédit ou réponse illisible → « non conclue » → aucune course.

Codes : 0 épreuve écrite (lire le verdict) ; 2 refus avant tout appel.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import importlib.util
import json
import os
import re
import statistics
import sys
import tempfile
from pathlib import Path

VERSION = "epreuve_temoins_auto_conception_v2"
DEPOT = Path(__file__).resolve().parents[1]
COURSE_V1 = "docs/notes/organisme-auto-conception-v1/course-v1"
COURSE = "docs/notes/organisme-auto-conception-v1/course-v2"
TEMOINS = DEPOT / COURSE / "temoins-juge-auto-conception-v2.json"
CONSIGNE_JUGE = DEPOT / COURSE_V1 / "consigne-juge-auto-conception-v1.md"
CONSIGNE_AIGUILLEUR = DEPOT / COURSE_V1 / "consigne-aiguilleur-auto-conception-v1.md"
CONSIGNE_PROPOSEUR = DEPOT / COURSE / "consigne-proposeur-auto-conception-v2.md"
CONFIGURATION = DEPOT / COURSE / "configuration-course-auto-conception-v2.json"
DECLARATION_EPREUVE = DEPOT / COURSE / "declaration-relais-epreuve-temoins-auto-conception-v2.json"
RAPPORT_REEL = DEPOT / COURSE / "epreuve-temoins-reelle-auto-conception-v2.json"
LANCEUR = DEPOT / "scripts" / "lancer_course_auto_conception_v2.py"
PLAFOND_EPREUVE_USD = 5.0
ETAPE = "epreuve-temoins"
RACINE_GRAINES = 2026111833
# Champ lu par chaque item dont un champ porte seul la lecture (constat 4).
CHAMP_LU = {"module_nomme": "module_change", "voisin_nomme": "plus_proche_voisin", "epreuve_plantee": "epreuve_monde_plante"}
N_JUGES_AU_HASARD = 2000
BORNE_CHAMP, BORNE_CARTE = 1200, 9000
ID_CATALOGUE = re.compile(r"(?<![\w-])([a-zéèêôûàç-]+) n° (\d+)", re.I)


# --- outils -----------------------------------------------------------------------------------------------------------------


def sha256_fichier(chemin: Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def ecrire_scelle(chemin: Path, objet) -> str:
    donnees = (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {Path(chemin).name}\n")
    return h


def charger_orchestrateur(racine: Path) -> dict:
    """Fonctions de service et de lecture de l'orchestrateur épinglé (aucune réécriture ici)."""
    racine = str(racine)
    if racine not in sys.path:
        sys.path.insert(0, racine)
    from pole import fiches_v54, juges_croises_v53, aiguilleur_v53  # noqa: E402
    return {"entree_une_fiche": fiches_v54.entree_une_fiche, "lire_verdict": juges_croises_v53.lire_verdict,
            "lire_classe": aiguilleur_v53.lire_classe, "racine": racine}


def charger_lanceur():
    spec = importlib.util.spec_from_file_location("lancer_course_auto_conception_v2", LANCEUR)
    m = importlib.util.module_from_spec(spec)
    sys.modules["lancer_course_auto_conception_v2"] = m
    spec.loader.exec_module(m)
    return m


def orchestrateur_present(candidats) -> Path:
    presents = [Path(o) for o in candidats if (Path(o) / "pole" / "fiches_v54.py").is_file()]
    if len(presents) != 1:
        raise SystemExit(f"orchestrateur : {len(presents)} copie(s) trouvée(s) (une exigée)")
    return presents[0]


# --- service et lecture -------------------------------------------------------------------------------------------------------


def identifiant_servi(etiquette: str, ident: str) -> str:
    return "F" + hashlib.sha256(f"epreuve-temoins|{etiquette}|{ident}".encode("utf-8")).hexdigest()[:5]


def servir(o: dict, consigne: str, temoin: dict, interdites: list, ident_servi: str | None) -> str:
    return o["entree_une_fiche"](consigne, {"contenu": temoin["contenu"]}, interdites, "mot_entier", ident_servi)


def verite(temoin: dict, items: list) -> dict:
    """Items attendus par construction : tous vrais pour un bon témoin ; l'item planté faux pour un mauvais (les autres items
    d'un mauvais témoin ne sont jamais lus comme critère)."""
    return {k: not (temoin["classe"] == "mauvais" and k == temoin["item_plante"]) for k in items}


def lire_epreuve(verdicts: dict, classes_aiguilleur: dict, temoins: dict, items: list) -> dict:
    """`verdicts` {juge: {id: verdict lu ou None}} ; `classes_aiguilleur` {id: classe lue ou None}. Règle gelée :
    un juge réussit si chaque bon témoin est notable (cinq items vrais) et si chaque mauvais témoin a son item planté faux ;
    l'aiguilleur réussit si chaque bon témoin est `niveau_methode` et si aucun témoin n'est `concret` ; une réponse illisible
    est un échec. Verdict : « réussie » si tous réussissent, « échouée » sinon."""
    par_juge = {}
    for juge, v in sorted(verdicts.items()):
        manques = []
        for tid, t in sorted(temoins.items()):
            lu = v.get(tid)
            if lu is None:
                manques.append({"temoin": tid, "motif": "verdict illisible ou absent"})
            elif t["classe"] == "bon" and not lu["notable"]:
                manques.append({"temoin": tid, "motif": "bon témoin non notable",
                                "items_faux": sorted(k for k in items if not lu["items"][k])})
            elif t["classe"] == "mauvais" and lu["items"][t["item_plante"]]:
                manques.append({"temoin": tid, "motif": f"item planté {t['item_plante']} rendu vrai"})
        par_juge[juge] = {"reussi": not manques, "manques": manques}
    manques_a = []
    for tid, t in sorted(temoins.items()):
        c = classes_aiguilleur.get(tid)
        if c is None:
            manques_a.append({"temoin": tid, "motif": "classe illisible ou absente"})
        elif c == "concret" or (t["classe"] == "bon" and c != "niveau_methode"):
            manques_a.append({"temoin": tid, "motif": f"classe {c}"})
    tous = all(x["reussi"] for x in par_juge.values()) and not manques_a and bool(par_juge)
    return {"verdict": "réussie" if tous else "échouée", "par_juge": par_juge,
            "aiguilleur": {"reussi": not manques_a, "manques": manques_a}}


# --- juges factices (hors ligne) ----------------------------------------------------------------------------------------------


class Reponse:
    def __init__(self, texte: str, modele: str):
        self.statut, self.texte_brut, self.texte_final, self.cout_declare_usd, self.modele_servi = "ok", texte, texte, 0.0, modele


def fiche_servie(consigne: str) -> dict:
    corps = consigne.rsplit("## La fiche\n```json\n", 1)[1].rsplit("\n```", 1)[0]
    d = json.loads(corps)
    d.pop("identifiant", None)
    return d


class JugeFactice:
    """`genre` : parfait | hasard | longueur | indulgent | severe. Le juge parfait reconnaît le témoin par son contenu et rend la
    vérité plantée ; le juge à la longueur rend tout vrai si la fiche servie est plus longue que la médiane des témoins, tout
    faux sinon."""

    def __init__(self, genre: str, temoins: dict, items: list, graine=None, mediane: float | None = None):
        self.genre, self.temoins, self.items, self.mediane = genre, temoins, items, mediane
        self.medianes_champ = {k: statistics.median(len(t["contenu"][c]) for t in temoins.values()) for k, c in CHAMP_LU.items()}
        if genre == "hasard":
            import numpy as np
            self.rng = np.random.default_rng(graine)

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        f = fiche_servie(consigne)
        if self.genre == "parfait":
            t = next(t for t in self.temoins.values() if t["contenu"] == f)
            items = verite(t, self.items)
        elif self.genre == "hasard":
            items = {k: bool(self.rng.integers(0, 2)) for k in self.items}
        elif self.genre == "longueur":
            long_ = len(json.dumps(f, ensure_ascii=False, indent=1)) > self.mediane
            items = {k: long_ for k in self.items}
        elif self.genre == "champ":  # v2 : chaque item vrai si son champ lu est plus long que la médiane de ce champ
            items = {k: (len(f[CHAMP_LU[k]]) > self.medianes_champ[k]) if k in CHAMP_LU else True for k in self.items}
        else:
            items = {k: self.genre == "indulgent" for k in self.items}
        return Reponse("```json\n" + json.dumps({"items": items, "note": "factice"}) + "\n```", modele or "factice")


class AiguilleurFactice:
    def __init__(self, classe: str):
        self.classe = classe

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        fiche_servie(consigne)
        return Reponse('```json\n{"classe": "%s", "categorie": "factice"}\n```' % self.classe, modele or "factice")


def jouer(o: dict, adaptateur, etiquette: str, modele: str, consigne: str, temoins: dict, items: list, interdites: list,
          dossier: Path, plafond_session: float, juge: bool = True) -> tuple:
    """Rend ({id: lu}, coût, modèles servis). Un appel par témoin, session neuve, identifiant opaque propre au juge."""
    lus, cout, servis = {}, 0.0, set()
    for tid in sorted(temoins):
        entree = servir(o, consigne, temoins[tid], interdites, identifiant_servi(etiquette, tid) if juge else None)
        d = dossier / etiquette / tid
        d.mkdir(parents=True, exist_ok=True)
        r = adaptateur.lancer("juge_ideation", entree, str(d), plafond_session, 1, modele=modele)
        cout += float(r.cout_declare_usd or 0.0)
        if r.statut == "ok" and r.modele_servi:
            servis.add(r.modele_servi)
        texte = r.texte_brut or r.texte_final if r.statut == "ok" else None
        lus[tid] = (o["lire_verdict"](texte, items) if juge else o["lire_classe"](texte)[0]) if texte else None
    return lus, cout, sorted(servis)


# --- contrôles des témoins eux-mêmes ------------------------------------------------------------------------------------------


def controles_statiques(temoins: dict, items: list, consigne_proposeur: str, matiere: bytes | None) -> dict:
    longueurs = {tid: len(json.dumps(t["contenu"], ensure_ascii=False, indent=1)) for tid, t in temoins.items()}
    bornes = {tid: max(len(v) for v in t["contenu"].values()) <= BORNE_CHAMP and longueurs[tid] <= BORNE_CARTE
              for tid, t in temoins.items()}
    # aucune règle de seuil sur la longueur ne classe tous les témoins (dans un sens ou dans l'autre)
    bons = {tid for tid, t in temoins.items() if t["classe"] == "bon"}
    erreurs_min = len(temoins)
    for s in sorted(set(longueurs.values())) + [0]:
        for sens in (1, -1):
            e = sum((sens * (longueurs[t] - s) > 0) != (t in bons) for t in temoins)
            erreurs_min = min(erreurs_min, e)
    par_champ = {}
    for item, champ in CHAMP_LU.items():
        sous = {tid: len(t["contenu"][champ]) for tid, t in temoins.items() if t["classe"] == "bon" or t["item_plante"] == item}
        bons_i = {tid for tid in sous if temoins[tid]["classe"] == "bon"}
        e_min = len(sous)
        for s_ in sorted(set(sous.values())) + [0]:
            for sens in (1, -1):
                e_min = min(e_min, sum((sens * (sous[t] - s_) > 0) != (t in bons_i) for t in sous))
        par_champ[item] = {"champ": champ, "longueurs": sous, "erreurs_min": e_min}
    champs = {tid: sorted(t["contenu"]) for tid, t in temoins.items()}
    titres_dans_la_consigne = sorted(tid for tid, t in temoins.items() if t["contenu"]["titre"].lower() in consigne_proposeur.lower())
    sortie = {"longueurs": longueurs, "bornes_tenues": all(bornes.values()), "bornes_par_temoin": bornes,
              "regle_de_seuil_sur_la_longueur_erreurs_min": erreurs_min,
              "regle_de_seuil_sur_le_champ_lu": par_champ,
              "regle_de_seuil_sur_le_champ_lu_erreurs_min": min(x["erreurs_min"] for x in par_champ.values()),
              "champs_identiques": len({tuple(v) for v in champs.values()}) == 1,
              "titres_de_temoin_dans_la_consigne_servie": titres_dans_la_consigne,
              "classes": {"bon": len(bons), "mauvais": len(temoins) - len(bons)},
              "items_plantes": sorted({t["item_plante"] for t in temoins.values() if t["item_plante"]}),
              "items_plantes_tous_couverts": sorted({t["item_plante"] for t in temoins.values() if t["item_plante"]}) == sorted(items)}
    if matiere is not None:
        texte = matiere.decode("utf-8")
        regroupements = set(re.findall(r"^\*\*([a-zéèêôûàç-]+ n° \d+) — ", texte, flags=re.M))
        cites, absents = {}, []
        for tid, t in temoins.items():
            ids = sorted(set(f"{a.lower()} n° {b}" for a, b in ID_CATALOGUE.findall(t["contenu"]["plus_proche_voisin"] + " "
                                                                             + t["contenu"]["ce_qui_distingue"])))
            cites[tid] = ids
            absents += [f"{tid}:{i}" for i in ids if i not in regroupements]
        sortie.update(matiere_sha256=hashlib.sha256(matiere).hexdigest(), identifiants_cites=cites,
                      identifiants_absents_de_la_matiere=absents)
    return sortie


# --- hors ligne -----------------------------------------------------------------------------------------------------------------


def hors_ligne(sortie: Path, matiere: Path | None, orchestrateur: Path) -> dict:
    import numpy as np
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    sortie.mkdir(parents=True)
    o = charger_orchestrateur(orchestrateur)
    conf = json.loads(CONFIGURATION.read_text(encoding="utf-8"))
    brut = json.loads(TEMOINS.read_text(encoding="utf-8"))
    items = list(conf["items_juge"])
    if brut["items"] != items:
        raise SystemExit("témoins : items différents de ceux de la configuration")
    temoins = {t["id"]: t for t in brut["temoins"]}
    interdites = list(conf["etiquettes_interdites_fixes"])
    cj, ca = CONSIGNE_JUGE.read_text(encoding="utf-8"), CONSIGNE_AIGUILLEUR.read_text(encoding="utf-8")
    statiques = controles_statiques(temoins, items, CONSIGNE_PROPOSEUR.read_text(encoding="utf-8"),
                                    matiere.read_bytes() if matiere else None)
    mediane = statistics.median(statiques["longueurs"].values())
    appels = sortie / "appels"
    ss = np.random.SeedSequence(RACINE_GRAINES)
    graines = ss.spawn(N_JUGES_AU_HASARD)
    juges = {"parfait": JugeFactice("parfait", temoins, items), "longueur": JugeFactice("longueur", temoins, items, mediane=mediane),
             "indulgent": JugeFactice("indulgent", temoins, items), "severe": JugeFactice("severe", temoins, items),
             "champ": JugeFactice("champ", temoins, items)}
    lectures = {}
    for nom, j in juges.items():
        lus, _, _ = jouer(o, j, nom, "factice", cj, temoins, items, interdites, appels, 0.6)
        a, _, _ = jouer(o, AiguilleurFactice("niveau_methode"), "aiguilleur", "factice", ca, temoins, items, interdites, appels / nom, 0.25, juge=False)
        lectures[nom] = lire_epreuve({nom: lus}, a, temoins, items)
    reussites_hasard = 0
    for k, g in enumerate(graines):
        lus, _, _ = jouer(o, JugeFactice("hasard", temoins, items, graine=g), f"hasard-{k}", "factice", cj, temoins, items,
                          interdites, appels / "hasard", 0.6) if k < 3 else (None, None, None)
        if lus is None:  # au-delà des trois premiers, sans écrire de dossier : même tirage, lecture directe
            rng = np.random.default_rng(g)
            lus = {}
            for tid in sorted(temoins):
                its = {kk: bool(rng.integers(0, 2)) for kk in items}
                lus[tid] = {"items": its, "notable": all(its.values()), "x": sum(its.values()) / len(items)}
        a = {tid: "niveau_methode" for tid in temoins}
        reussites_hasard += lire_epreuve({"h": lus}, a, temoins, items)["verdict"] == "réussie"
    a_art, _, _ = jouer(o, AiguilleurFactice("concret"), "aiguilleur-artefact", "factice", ca, temoins, items, interdites, appels, 0.25,
                        juge=False)
    lus_parfait, _, _ = jouer(o, juges["parfait"], "parfait-bis", "factice", cj, temoins, items, interdites, appels, 0.6)
    artefact_aiguilleur = lire_epreuve({"parfait": lus_parfait}, a_art, temoins, items)
    n_bons = statiques["classes"]["bon"]
    n_mauvais = statiques["classes"]["mauvais"]
    p_hasard = (0.5 ** len(items)) ** n_bons * 0.5 ** n_mauvais
    separe = (lectures["parfait"]["verdict"] == "réussie" and all(lectures[n]["verdict"] == "échouée" for n in ("longueur", "indulgent", "severe", "champ"))
              and reussites_hasard == 0 and artefact_aiguilleur["verdict"] == "échouée")
    temoins_conformes = (statiques["bornes_tenues"] and statiques["regle_de_seuil_sur_la_longueur_erreurs_min"] >= 1
                         and statiques["regle_de_seuil_sur_le_champ_lu_erreurs_min"] >= 1
                         and statiques["champs_identiques"] and not statiques["titres_de_temoin_dans_la_consigne_servie"]
                         and statiques["items_plantes_tous_couverts"]
                         and not statiques.get("identifiants_absents_de_la_matiere", []))
    rapport = {"version": VERSION, "moteur": "hors_ligne (juges factices, aucun appel)",
               "empreintes": {"temoins": sha256_fichier(TEMOINS), "consigne_juge": sha256_fichier(CONSIGNE_JUGE),
                              "consigne_aiguilleur": sha256_fichier(CONSIGNE_AIGUILLEUR), "programme": sha256_fichier(Path(__file__)),
                              "configuration": sha256_fichier(CONFIGURATION), "consigne_proposeur": sha256_fichier(CONSIGNE_PROPOSEUR)},
               "orchestrateur": str(orchestrateur), "graines": {"racine": RACINE_GRAINES, "juges_au_hasard": N_JUGES_AU_HASARD,
                                                               "regle": "numpy.random.SeedSequence(racine).spawn(n)"},
               "controles_statiques": statiques, "lectures": lectures, "juges_au_hasard_reussis": reussites_hasard,
               "probabilite_exacte_qu_un_juge_au_hasard_reussisse": p_hasard,
               "artefact_aiguilleur_tout_concret": artefact_aiguilleur["verdict"],
               "mediane_des_longueurs": mediane,
               "limite": ("plancher de lecture de forme seulement : chaque mauvais témoin déclare son défaut en toutes lettres ; "
                          "le juge ne voit pas le catalogue ; l'épreuve ne mesure pas le pouvoir de discrimination d'un juge sur des "
                          "défauts non déclarés, ni l'existence d'un identifiant (constat 4)"),
               "conclusion": {"temoins_separent_le_juge_parfait": separe, "temoins_conformes": temoins_conformes,
                              "verdict": "témoins éprouvés hors ligne" if (separe and temoins_conformes) else "témoins à reprendre"}}
    h = ecrire_scelle(sortie / "epreuve-temoins-hors-ligne.json", rapport)
    print(json.dumps({"rapport": str(sortie / "epreuve-temoins-hors-ligne.json"), "sha256": h, **rapport["conclusion"],
                      "juges_au_hasard_reussis": reussites_hasard}, ensure_ascii=False))
    return rapport


# --- réel (session d'exécution seulement) ---------------------------------------------------------------------------------------


def reel() -> dict:
    """Jamais lancé par l'auteur. Ordre : environnement sans nom de clé ; pièce de départ ; ligne de GO de l'épreuve
    (lue au commit de main) ; pièces épinglées par le lanceur (ce programme compris) ; orchestrateur épinglé ; déclaration des
    relais de l'épreuve (Claude et Argon seulement) ; relais vivants par PID et porte à blanc ; puis les appels, sous le plafond
    de 5 USD (chaque appel n'est lancé que si le cumul plus son plafond de session tient dessous)."""
    L = charger_lanceur()
    presents = sorted(n for n in os.environ if n in L.NOMS_DE_CLE or L.MOTIF_NOM_DE_CLE.search(n))
    if presents:
        raise L.Refus(f"variables de clé dans l'environnement de l'épreuve ({presents}) : la clé reste dans son relais")
    r = L.Reglages.production()
    r.declaration = DECLARATION_EPREUVE
    aujourd_hui = _dt.datetime.now(_dt.timezone.utc).date()
    depart = L.verifier_piece_de_depart(r)
    registre = L.lire_registre(r)
    go = L.verifier_go(registre["texte"], aujourd_hui, depart["go_epreuve"], PLAFOND_EPREUVE_USD, ("temoins",))
    pieces = L.verifier_pieces(r)
    if pieces["epreuve_temoins"]["sha256"] != sha256_fichier(Path(__file__)):
        raise L.Refus("ce programme n'est pas celui que le lanceur épingle")
    orch = L.verifier_orchestrateur(r)
    fixe = json.loads(Path(pieces["configuration"]["absolu"]).read_text(encoding="utf-8"))
    decl_brute, decl_sha = L.lire_json_scelle(DECLARATION_EPREUVE, "déclaration des relais de l'épreuve")
    if sorted(decl_brute.get("fournisseurs") or {}) != ["argon", "claude"]:
        raise L.Refus("déclaration de l'épreuve : claude et argon seulement (juges et aiguilleur de la configuration)")
    decl = L.verifier_declaration(decl_brute, fixe, depart)
    n_argon = len(json.loads(TEMOINS.read_text(encoding="utf-8"))["temoins"]) * sum(1 for j in fixe["juges"] if j["fournisseur"] == "argon")
    procedure = L.verifier_procedure_relais(r, decl, pieces, fixe, n_argon, plafond_ligne=PLAFOND_EPREUVE_USD)
    portes_a_blanc = L.porte_a_blanc(decl)
    sortie = Path(tempfile.mkdtemp(prefix="epreuve-temoins-auto-conception-"))
    arrets = sortie / "arrets-credit"
    arrets.mkdir()
    decl = L.envelopper_commandes(decl, sys.executable, Path(pieces["garde_credit"]["absolu"]), arrets)
    o = charger_orchestrateur(Path(orch["chemin"]))
    spec = importlib.util.spec_from_file_location("ideation_v8_pour_epreuve", Path(orch["chemin"]) / L.LANCEUR_ORCHESTRATEUR)
    v8 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v8)
    base_sessions = tempfile.mkdtemp(prefix="pole-sessions-epreuve-")
    adaptateurs, portes = v8.adaptateurs_reels_v56({"fournisseurs": decl["fournisseurs"]}, str(sortie / "sortie"), base_sessions)
    accuses = {nom: p.transmettre(ETAPE, PLAFOND_EPREUVE_USD) for nom, p in sorted(portes.items())}
    brut = json.loads(TEMOINS.read_text(encoding="utf-8"))
    items, temoins = list(fixe["items_juge"]), {t["id"]: t for t in brut["temoins"]}
    interdites = list(fixe["etiquettes_interdites_fixes"])
    ps = fixe["plafonds_session"]
    cj, ca = Path(pieces["consigne_juge"]["absolu"]).read_text(encoding="utf-8"), Path(pieces["consigne_aiguilleur"]["absolu"]).read_text(encoding="utf-8")
    cumul, verdicts, servis, motif_arret = 0.0, {}, {}, None
    plan = [("aiguilleur", fixe["aiguilleur"], ca, float(ps["aiguilleur"]), False)] + \
        [(j["etiquette"], j, cj, float(ps["juge"]), True) for j in fixe["juges"]]
    classes = {}
    for etiquette, role, consigne, plafond_session, juge in plan:
        lus = {}
        for tid in sorted(temoins):
            if cumul + plafond_session > PLAFOND_EPREUVE_USD + 1e-9:
                motif_arret = f"plafond de l'épreuve ({PLAFOND_EPREUVE_USD} USD) : appel suivant non lancé"
                break
            if any(x.name.startswith("arret-credit-") for x in arrets.iterdir()):
                motif_arret = "refus pour crédit d'un relais au solde illisible"
                break
            un, c, s = jouer(o, adaptateurs[role["fournisseur"]], etiquette, role["modele"], consigne, {tid: temoins[tid]}, items,
                             interdites, sortie / "appels", plafond_session, juge=juge)
            cumul += c
            lus.update(un)
            servis.setdefault(etiquette, set()).update(s)
        if juge:
            verdicts[etiquette] = lus
        else:
            classes = lus
        if motif_arret:
            break
    lecture = lire_epreuve(verdicts, classes, temoins, items)
    changes = sorted(e for e, s in servis.items() if len(s) > 1)
    if motif_arret or changes or len(verdicts) != len(fixe["juges"]):
        lecture["verdict"] = "non conclue"
    rapport = {"version": VERSION, "moteur": "reel", "verdict": lecture["verdict"], "lecture": lecture, "motif_arret": motif_arret,
               "verdicts": verdicts, "classes": classes,
               "modeles_servis": {e: sorted(s) for e, s in servis.items()}, "version_servie_changee": changes,
               "horodatage_utc": _dt.datetime.now(_dt.timezone.utc).isoformat(), "go": go,
               "registre": {"commit": registre["commit"], "sha256": registre["sha256"]},
               "piece_de_depart": {"chemin": depart["chemin"], "sha256": depart["sha256"]},
               "empreintes": {"temoins": pieces["temoins"]["sha256"], "consigne_juge": pieces["consigne_juge"]["sha256"],
                              "consigne_aiguilleur": pieces["consigne_aiguilleur"]["sha256"], "programme": sha256_fichier(Path(__file__)),
                              "lanceur": sha256_fichier(LANCEUR), "orchestrateur_commit": orch["commit"]},
               "juges": [[j["etiquette"], j["modele"]] for j in fixe["juges"]],
               "aiguilleur": [fixe["aiguilleur"]["etiquette"], fixe["aiguilleur"]["modele"]],
               "declaration": {"chemin": str(DECLARATION_EPREUVE), "sha256": decl_sha}, "procedure": procedure,
               "porte_a_blanc": portes_a_blanc, "accuses_de_plafond": accuses, "cout_usd": round(cumul, 6),
               "plafond_usd": PLAFOND_EPREUVE_USD, "sortie_hors_depot": str(sortie)}
    h = ecrire_scelle(RAPPORT_REEL, rapport)
    print(json.dumps({"rapport": str(RAPPORT_REEL), "sha256": h, "verdict": rapport["verdict"], "cout_usd": rapport["cout_usd"]},
                     ensure_ascii=False))
    return rapport


def principal(argv: list | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) in (2, 4) and argv[0] == "--hors-ligne" and (len(argv) == 2 or argv[2] == "--matiere"):
        L = charger_lanceur()
        hors_ligne(Path(argv[1]).resolve(), Path(argv[3]).resolve() if len(argv) == 4 else None,
                   orchestrateur_present(L.ORCHESTRATEURS_CANDIDATS))
        return 0
    if argv == ["--reel"]:
        L = charger_lanceur()
        try:
            reel()
        except L.Refus as e:
            print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
            return 2
        return 0
    print("usage : --hors-ligne SORTIE_NEUVE [--matiere MATIERE.md] | --reel", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(principal())
