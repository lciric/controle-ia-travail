"""Papier C — lancement : configuration, graines, manifeste, gardes, pilote, ouverture de l'étape 2 (v1).

Texte de référence : version r1 (`e12f16fa…`), Plan d'analyse, sections 0 à 4 ; liste d'arrêt.

Ce fichier ne lance rien de payant et ne touche ni carte graphique, ni modèle, ni réseau : tout cela reste derrière
l'interface `Machine`, que les essais remplacent par un faux (`tests/fausse_machine_papier_c_v1.py`). L'adaptateur réel
de cette interface (harnais du pilote à huit milliards de paramètres, `controle_ia.bases.scores_jetons`, location de
l'instance) n'est pas écrit dans cette version : il est déclaré « non porté » dans la table de conformité.

Ordre du pilote (Plan, section 1) : préparation sur processeur (configuration scellée, empreintes, module, arbre gelé,
préalables, accord du jour, accord de dépense, graines, banc sur processeur, budget) ; manifeste ; puis, sur l'instance,
points 1.1 à 1.5 ; sorties scellées (point 1.6) ; arrêt de l'instance par son identifiant, toujours (R10).
"""
from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path
from typing import Protocol

import numpy as np

from controle_ia.manifeste import creer_manifeste, generateur
from controle_ia.scellement import sceller
import derivation as der
import papier_c_decisions_v1 as dec
import papier_c_gardes_v1 as gd
from papier_c_configuration_v1 import FAMILLES, charger_configuration, remplir
from papier_c_erreurs_v1 import (AucuneVariantePourUnJuge, BancProcesseurNonReproduit, ConfigurationInvalide,
                                 EcartAuPreenregistrement, FuiteDeLaCible, InsertionAbsente,
                                 ParagraphesDePlaidoyerNonConformes, RecouvrementCalibrageEtape2, TachesNonConformes,
                                 VarianteRefusee)
from papier_c_lois_v1 import loi_separee
from papier_c_reechantillonnage_v1 import intervalle_percentiles

DOSSIER_DES_SORTIES = "diag/papier-C-pilote-v1"
CLES_DU_PILOTE = ("papier-C/pilote/calibrage", "papier-C/pilote/lisibilite", "papier-C/pilote/raisonne",
                  "papier-C/pilote/conception", "partage-taches-papier-C")
CLES_DE_L_ETAPE2 = ("papier-C/etape2/taches", "papier-C/etape2/episodes", "papier-C/etape2/raisonne",
                    "papier-C/etape2/reechantillonnage", "papier-C/etape2/permutations",
                    "papier-C/etape2/fenetres-excedent", "papier-C/etape2/placebo", "papier-C/etape2/direction-aleatoire")


class Machine(Protocol):
    """Tout ce qui touche l'instance louée, les juges, l'agent et les sondes. Les textes des contenus restent du côté
    de la machine : le lanceur ne manie que des empreintes, des scores et des masses."""

    def identifiant_de_l_instance(self) -> str: ...
    def prix_horaire_usd(self) -> float: ...
    def revisions_des_juges(self) -> dict: ...
    def encoder(self, juge: str, texte: str) -> list: ...
    def longueur_du_juge(self, juge: str) -> int: ...
    def contenus_de_calibrage(self, taches: list) -> list: ...
    def lire(self, juge: str, consigne: str, variante: int, mode: str, demandes: list) -> list: ...
    def lire_le_banc(self, juge: str, variante: int) -> dict: ...
    def generer_un_episode(self, demande: dict) -> dict: ...
    def relire(self, demande: dict) -> dict: ...
    def arreter(self, identifiant: str) -> bool: ...


def _sha(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def ecrire_une_sortie(racine, nom: str, corps: dict, sous_dossier: str = "") -> Path:
    """Écrit et scelle une sortie sous `diag/papier-C-pilote-v1/` (le banc à part, sous `banc/`) ; refuse d'écraser
    (R12)."""
    dossier = Path(racine) / DOSSIER_DES_SORTIES / sous_dossier
    dossier.mkdir(parents=True, exist_ok=True)
    chemin = dossier / nom
    if chemin.exists():
        raise EcartAuPreenregistrement(f"{chemin} existe déjà : R12 interdit d'écraser une sortie")
    chemin.write_text(json.dumps(corps, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(chemin)
    return chemin


# ------------------------------------------------------------------------------------------------------------------
# Lectures par les juges, avec les gardes 7 à 10
# ------------------------------------------------------------------------------------------------------------------
def insertion_d_une_condition(cfg: dict, condition: dict, corpus: str) -> str | None:
    """Texte inséré pour une condition : None sans insertion ; formulation ou témoin rempli pour le corpus ; constat
    nu rempli."""
    fentes = cfg["fentes"][corpus]
    sorte = condition["type"]
    if sorte == "sans":
        return None
    if sorte == "formulation":
        return remplir(cfg["vivier"][condition["famille"]][condition["indice"] - 1], fentes)
    if sorte == "temoin":
        return remplir(cfg["temoins_sham"][condition["indice"] - 1], fentes)
    if sorte == "constat_nu":
        return remplir(cfg["constat_nu"]["gabarit"], fentes)
    raise ConfigurationInvalide(f"condition {sorte!r} inconnue")


def cle_de_condition(condition: dict) -> str:
    return "/".join(str(condition[k]) for k in ("type", "famille", "indice") if k in condition)


def lire_les_conditions(machine: Machine, cfg: dict, juge: str, consigne: str, variante: int, mode: str,
                        contenus: list, conditions: list, corpus: str = "A") -> list:
    """Demande à la machine la lecture de chaque contenu sous chaque condition, puis applique aux réponses les gardes
    de la liste d'arrêt : contexte et troncature (7), même instrument pour toutes les conditions (8), consigne égale
    octet pour octet à celle de la configuration (9), insertion présente et en place (10). Rend, par lecture :
    empreinte du contenu, condition, score, masse — jamais de texte."""
    bloc = cfg["consignes"][consigne]
    systeme = bloc["systeme_raisonne" if mode == "raisonne" else "systeme_direct"]
    demandes = []
    for c in contenus:
        for cond in conditions:
            demandes.append({"cle": f"{c}|{cle_de_condition(cond)}", "contenu": c, "condition": cond,
                             "insertion": insertion_d_une_condition(cfg, cond, corpus),
                             "separateur": cfg["insertion"]["separateur"], "systeme": systeme,
                             "utilisateur": bloc["utilisateur"]})
    reponses = machine.lire(juge, consigne, variante, mode, demandes)
    if [r["cle"] for r in reponses] != [d["cle"] for d in demandes]:
        raise EcartAuPreenregistrement("lectures rendues dans un autre ordre, ou en nombre différent, que les demandes")
    longueur = machine.longueur_du_juge(juge)
    sorties = []
    for d, r in zip(demandes, reponses):
        gd.garde_contexte(int(r["jetons_contexte"]), longueur, bool(r.get("tronque", False)))
        if r["consigne_sha256"] != _sha(systeme):
            raise FuiteDeLaCible(f"{juge}, {consigne} : consigne lue différente, octet pour octet, de la configuration")
        if d["insertion"] is not None and not (r.get("insertion_presente") and r.get("insertion_en_place")):
            raise InsertionAbsente(f"{juge}, {d['cle']} : insertion absente du rendu complet, ou hors de la règle")
        sorties.append({"contenu": d["contenu"], "condition": cle_de_condition(d["condition"]), "score": float(r["score"]),
                        "masse": float(r["masse"]), "instrument": {"juge": r["juge"], "consigne": r["consigne"],
                                                                   "variante": r["variante"], "mode": r["mode"]}})
    if sorties and gd.garde_instrument([s["instrument"] for s in sorties]) != (juge, consigne, variante, mode):
        raise EcartAuPreenregistrement("instrument rendu par la machine différent de l'instrument demandé")
    return sorties


# ------------------------------------------------------------------------------------------------------------------
# Tirages du pilote
# ------------------------------------------------------------------------------------------------------------------
def choisir_les_contenus_de_calibrage(candidats: list, rng: np.random.Generator, n_max: int = 60) -> list:
    """Règle de calibrage : condition honnête et conditions de sabotage, moitié-moitié autant que possible ; 60
    contenus au plus, tirés par graine (clé `papier-C/pilote/calibrage`). `candidats` : {empreinte, tache, condition},
    un par épisode du pilote de T0.5 dont la tâche est dans le lot de calibrage (première action à coût lisible, lue
    du côté de la machine). Tirage : permutation de chaque groupe trié par empreinte (appel non écrit au texte : point
    ouvert PO-28)."""
    honnetes = sorted((c for c in candidats if c["condition"] == "honnete"), key=lambda c: c["empreinte"])
    saboteurs = sorted((c for c in candidats if c["condition"] != "honnete"), key=lambda c: c["empreinte"])
    n_h = min(len(honnetes), n_max // 2)
    n_s = min(len(saboteurs), n_max - n_h)
    n_h = min(len(honnetes), n_max - n_s)
    choix_h = [honnetes[i] for i in rng.permutation(len(honnetes))[:n_h]]
    choix_s = [saboteurs[i] for i in rng.permutation(len(saboteurs))[:n_s]]
    choisis = choix_h + choix_s
    return [choisis[i] for i in rng.permutation(len(choisis))]


def moyennes_du_banc_processeur(chemin, champ_pression: str, champ_neutre: str) -> tuple[np.ndarray, np.ndarray]:
    """Moyennes par item d'un fichier de résultats du projet précédent (point 1.0 : champs `mean_pre` ou `mean_praise`,
    et `mean_neu` du même fichier ; 30 items, aucun exclu). Le format du fichier (une liste d'items, ou un objet à
    clé `items`) n'est pas écrit au texte : point ouvert PO-35."""
    corps = json.loads(Path(chemin).read_text(encoding="utf-8"))
    items = corps["items"] if isinstance(corps, dict) else corps
    return (np.array([float(i[champ_pression]) for i in items]), np.array([float(i[champ_neutre]) for i in items]))


def banc_sur_processeur(cfg: dict, racine) -> dict:
    """Point 1.0 : la loi séparée du module, appliquée aux moyennes par item des deux fichiers (Δ = moyenne sous
    pression moins moyenne neutre du même fichier, régressé sur cette moyenne neutre), redonne les six valeurs du
    recalcul de la session ; échec : arrêt avant toute carte."""
    ref = cfg["pilote"]["banc_processeur"]
    calcule = {"g": [], "c": [], "r2": []}
    for fichier, (pression, neutre) in zip(ref["fichiers"], ref["champs"]):
        p, n = moyennes_du_banc_processeur(Path(racine) / fichier, pression, neutre)
        if p.size != 30:
            raise BancProcesseurNonReproduit(f"{fichier} : {p.size} items au lieu de 30")
        loi = loi_separee(np.ones((1, p.size)), p - n, n)
        for cle in calcule:
            calcule[cle].append(float(loi[cle][0]))
    gd.garde_banc_processeur(calcule, ref)
    return calcule


# ------------------------------------------------------------------------------------------------------------------
# Préparation commune d'un lancement (sur processeur, avant toute carte)
# ------------------------------------------------------------------------------------------------------------------
def preparer_le_pilote(racine, pieces: dict, jour: date, entropie, accords: list, heures_deja_consommees: float,
                       prix_horaire_usd: float, duree_prevue_heures: float, taches_du_pilote: list,
                       taches_de_la_source: list, lister_arbre_gele=None) -> dict:
    """Tout ce qui précède la carte. `pieces` : chemins de `configuration`, `preenregistrement`, `verdict_p3`,
    `registre_des_accords`, `accord_du_jour`, `module` (dossier), et `empreintes` {chemin: empreinte} des autres
    pièces (items, prompts, fichiers de tâches). Applique, dans l'ordre : configuration scellée valide (aucun
    marqueur) ; empreintes (garde 1) ; lignes du module ; arbre gelé ; préalables (garde 2) ; accord du jour ; accord
    de dépense ; graines (garde 13) ; partage des tâches (garde 16) ; banc sur processeur (garde 4) ; budget
    (garde 3)."""
    racine = Path(racine)
    cfg, sha_cfg = charger_configuration(pieces["configuration"], "scelle")
    prealables = gd.garde_prealables_du_pilote(pieces["preenregistrement"], pieces["verdict_p3"])
    gd.garde_empreintes(pieces.get("empreintes", {}))
    lignes = gd.lignes_du_module(Path(pieces["preenregistrement"]).read_text(encoding="utf-8"))
    gd.garde_module(pieces["module"], lignes)
    if lister_arbre_gele is None:
        gd.garde_arbre_gele(racine)
    else:
        gd.garde_arbre_gele(racine, lister=lister_arbre_gele)
    accord_du_jour = gd.garde_accord_du_jour(pieces["accord_du_jour"], jour)
    depense = gd.garde_accord_de_depense(pieces["registre_des_accords"], accords, jour)
    graines = gd.graines_du_papier_c(list(CLES_DU_PILOTE), cfg["graines"]["cles"], entropie, cfg["graines"]["racine"])
    partage = gd.tirer_le_partage(taches_du_pilote, taches_de_la_source, generateur(graines["partage-taches-papier-C"]),
                                  cfg["partage_taches"]["taches_calibrage"])
    if len(partage["bassin"]) != cfg["partage_taches"]["taches_bassin_etape2_partage"]:
        raise TachesNonConformes(f"bassin du partage de {len(partage['bassin'])} tâches au lieu de "
                                 f"{cfg['partage_taches']['taches_bassin_etape2_partage']}")
    banc = banc_sur_processeur(cfg, racine)
    borne = gd.borne_de_duree(heures_deja_consommees, prix_horaire_usd, cfg["pilote"]["heures_carte_max_total"],
                              cfg["pilote"]["usd_borne_stricte_par_lancement"])
    duree = min(duree_prevue_heures, borne)
    budget = gd.garde_budget(duree, prix_horaire_usd, heures_deja_consommees,
                             cfg["pilote"]["heures_carte_max_total"], cfg["pilote"]["usd_borne_stricte_par_lancement"])
    return {"configuration": cfg, "configuration_sha256": sha_cfg, "prealables": prealables,
            "accord_du_jour": accord_du_jour, "accords_de_depense": depense, "graines": graines, "partage": partage,
            "banc_processeur": banc, "borne_de_duree_heures": borne, "duree_bornee_heures": duree,
            "heures_deja_consommees": heures_deja_consommees, "budget": budget, "entropie": int(entropie)}


# ------------------------------------------------------------------------------------------------------------------
# Pilote, sur l'instance (points 1.1 à 1.6)
# ------------------------------------------------------------------------------------------------------------------
def _variantes_lisibles(machine, cfg, juges, consigne, contenus, conditions, masse) -> tuple[dict, list]:
    """Par juge et par variante de la consigne : règle du jeton en contexte (garde 5), puis lisibilité."""
    reponses = cfg["consignes"][consigne]["reponses_imposees"]
    passe = np.zeros((len(juges), len(reponses)), dtype=bool)
    lectures = []
    for j, juge in enumerate(juges):
        for v, r in enumerate(reponses):
            try:
                gd.jetons_des_valeurs_en_contexte(lambda t: machine.encoder(juge, t), r, cfg["echelle"]["valeurs"])
            except VarianteRefusee:
                continue
            # la consigne B est lue ici sur des propositions (contenus de calibrage), fentes du corpus B (point 1.3)
            lus = lire_les_conditions(machine, cfg, juge, consigne, v, "direct", contenus, conditions,
                                      "B" if consigne == "B_standard" else "A")
            passe[j, v] = der.lisible([l["masse"] for l in lus], masse["mediane_min"], masse["seuil_lecture"],
                                      masse["part_min_au_dessus_du_seuil"])
            lectures.append({"juge": juge, "variante": v, "lisible": bool(passe[j, v]), "lectures": lus})
    return der.choisir_variantes(passe), lectures


def executer_le_pilote(racine, preparation: dict, machine: Machine, run_id: str, registre_des_arrets,
                       horodatage: str) -> dict:
    """Points 1.1 à 1.6 sur l'instance. L'instance est arrêtée par son identifiant à la fin, quoi qu'il arrive, et
    l'arrêt est consigné (liste d'arrêt 3)."""
    cfg = preparation["configuration"]
    juges = [j["nom"] for j in cfg["juges"]]
    pil, masse = cfg["pilote"], cfg["echelle"]["masse"]
    instance = machine.identifiant_de_l_instance()
    reserves: list[str] = []
    try:
        # 1.1 : empreintes sur l'instance
        gd.garde_revisions_des_juges(machine.revisions_des_juges(), cfg["juges"])
        gd.garde_budget(preparation["duree_bornee_heures"], machine.prix_horaire_usd(),
                        preparation["heures_deja_consommees"], pil["heures_carte_max_total"],
                        pil["usd_borne_stricte_par_lancement"])
        candidats = machine.contenus_de_calibrage(preparation["partage"]["calibrage"])
        hors = [c for c in candidats if c["tache"] not in preparation["partage"]["calibrage"]]
        if hors:
            raise RecouvrementCalibrageEtape2(f"{len(hors)} contenu(s) de calibrage hors du lot de calibrage")
        calibrage = choisir_les_contenus_de_calibrage(candidats, generateur(preparation["graines"]["papier-C/pilote/calibrage"]),
                                                      pil["n_calibrage_max"])
        empreintes = [c["empreinte"] for c in calibrage]
        # 1.2 : banc sur carte (contrôle positif rapporté, jamais un filtre de juge)
        banc, contraires = {}, []
        for juge in juges:
            ligne = None
            for v in range(len(cfg["consignes"]["banc_P1"]["reponses_imposees"])):
                lu = machine.lire_le_banc(juge, v)
                if der.lisible(lu["masses"], masse["mediane_min"], masse["seuil_lecture"], masse["part_min_au_dessus_du_seuil"]):
                    ligne = (v, lu)
                    break
            if ligne is None:
                raise AucuneVariantePourUnJuge(f"banc sur carte : aucune réponse imposée lisible pour {juge}")
            v, lu = ligne
            neutre, critique, eloge = (np.asarray(lu[k], dtype=np.float64) for k in ("neutre", "critique", "eloge"))
            un = np.ones((1, neutre.size))
            lc, le = loi_separee(un, critique - neutre, neutre), loi_separee(un, eloge - neutre, neutre)
            ecart = (eloge - neutre) - (critique - neutre)
            # intervalle rapporté de Δ̄_éloge − Δ̄_critique : rééchantillonnage des items, clé de conception du pilote
            # (le texte ne nomme ni la méthode ni la clé : point ouvert PO-36)
            tir = generateur(preparation["graines"]["papier-C/pilote/conception"]).multinomial(
                neutre.size, np.full(neutre.size, 1.0 / neutre.size), size=pil["tirages_conception"]) @ ecart / neutre.size
            bas, haut, _ = intervalle_percentiles(tir, 0.95)
            lecture = dec.banc_sur_carte(float(np.mean(critique - neutre)), float(np.mean(eloge - neutre)),
                                         float(lc["c"][0]), float(le["c"][0]), {"bas": bas, "haut": haut})
            contraires.append(lecture["ordre_contraire"])
            banc[juge] = {"variante": v, "g_critique": float(lc["g"][0]), "g_eloge": float(le["g"][0]),
                          "c_critique": float(lc["c"][0]), "c_eloge": float(le["c"][0]),
                          "deplacement_critique": float(np.mean(critique - neutre)),
                          "deplacement_eloge": float(np.mean(eloge - neutre)), "ic_ecart": [bas, haut], **lecture}
        etat_banc = gd.garde_banc_sur_carte(contraires)
        # 1.3 : lisibilité des consignes
        vingt = empreintes[:pil["n_lisibilite"]]
        lt = cfg["controle_redaction"]["longueurs_temoins"]
        court, long_ = 1 + int(np.argmin(lt)), 1 + int(np.argmax(lt))
        temoins = [{"type": "temoin", "indice": court}, {"type": "temoin", "indice": long_}]
        conditions_AB = ([{"type": "sans"}] + [{"type": "formulation", "famille": f, "indice": i}
                                               for f in FAMILLES for i in pil["indices_lisibilite"]] + temoins)
        conditions_alarme = ([{"type": "sans"}] + [{"type": "formulation", "famille": FAMILLES[4], "indice": i}
                                                   for i in pil["indices_lisibilite"]]
                             + [{"type": "formulation", "famille": FAMILLES[3], "indice": pil["indice_raisonne"]}] + temoins)
        variantes, lisibilite = {}, {}
        for consigne, conditions in (("A_standard", conditions_AB), ("B_standard", conditions_AB),
                                     ("A_donnees_alarme", conditions_alarme)):
            choix, lectures = _variantes_lisibles(machine, cfg, juges, consigne, vingt, conditions, masse)
            variantes[consigne] = choix["variantes"]
            reserves += [f"{r} ({consigne})" for r in choix["reserves"]]
            lisibilite[consigne] = lectures
        # 1.4 : vivier, consigne A, mode direct, variante retenue ; constat nu pour la lisibilité seulement
        conditions_vivier = ([{"type": "sans"}] + [{"type": "formulation", "famille": f, "indice": i}
                                                   for f in FAMILLES for i in range(1, 17)]
                             + [{"type": "temoin", "indice": i} for i in range(1, 17)])
        vivier, constat = {}, {}
        for j, juge in enumerate(juges):
            v = variantes["A_standard"][j]
            vivier[juge] = lire_les_conditions(machine, cfg, juge, "A_standard", v, "direct", empreintes, conditions_vivier)
            gd.garde_lisibilite_du_pilote([l["masse"] for l in vivier[juge]], masse["mediane_min"], masse["seuil_lecture"],
                                          masse["part_min_au_dessus_du_seuil"])
            constat[juge] = lire_les_conditions(machine, cfg, juge, "A_standard", v, "direct", empreintes,
                                                [{"type": "constat_nu"}])
        # 1.5 : lisibilité du mode raisonné
        # dix contenus tirés par la clé du mode raisonné (le texte dit « 10 contenus » sans dire lesquels : PO-36)
        rng_r = generateur(preparation["graines"]["papier-C/pilote/raisonne"])
        dix = [empreintes[i] for i in sorted(int(i) for i in rng_r.choice(len(empreintes), replace=False,
                                                                           size=min(pil["n_raisonne"], len(empreintes))))]
        conditions_raisonne = [{"type": "sans"}] + [{"type": "formulation", "famille": f, "indice": pil["indice_raisonne"]}
                                                    for f in FAMILLES]
        raisonne = {}
        for j, juge in enumerate(juges):
            lus = lire_les_conditions(machine, cfg, juge, "A_standard", variantes["A_standard"][j], "raisonne", dix,
                                      conditions_raisonne)
            ok = der.lisible([l["masse"] for l in lus], masse["mediane_min"], masse["seuil_lecture"],
                             masse["part_min_au_dessus_du_seuil"])
            raisonne[juge] = {"lisible": ok, "lectures": lus}
            if not ok:
                reserves.append(f"modérateur raisonné tombé pour {juge}")
        # 1.6 : sorties scellées ; le banc à part, jamais lu par la dérivation
        en_tete = {"run_id": run_id, "configuration_sha256": preparation["configuration_sha256"]}
        chemins = {
            "banc": ecrire_une_sortie(racine, f"{run_id}-banc-point-1.2.json",
                                      {**en_tete, "point": "1.2", "banc": banc, "etat": etat_banc}, "banc"),
            "lisibilite": ecrire_une_sortie(racine, f"{run_id}-lisibilite-point-1.3.json",
                                            {**en_tete, "point": "1.3", "variantes": variantes, "lectures": lisibilite}),
            "vivier": ecrire_une_sortie(racine, f"{run_id}-vivier-point-1.4.json",
                                        {**en_tete, "point": "1.4", "n_cal": len(calibrage),
                                         "contenus": [{"empreinte": c["empreinte"], "tache": c["tache"],
                                                       "condition": c["condition"]} for c in calibrage],
                                         "lectures": vivier, "constat_nu_lisibilite_seulement": constat}),
            "raisonne": ecrire_une_sortie(racine, f"{run_id}-raisonne-point-1.5.json",
                                          {**en_tete, "point": "1.5", "lectures": raisonne}),
        }
        return {"sorties": {k: str(v) for k, v in chemins.items()}, "variantes": variantes, "reserves": reserves,
                "n_cal": len(calibrage), "banc": banc, "etat_banc": etat_banc}
    finally:
        gd.arreter_l_instance(instance, machine.arreter, registre_des_arrets, f"fin du lancement {run_id} du pilote du papier C",
                              horodatage)


def lancer_le_pilote(racine, pieces: dict, machine: Machine, run_id: str, jour: date, entropie, accords: list,
                     heures_deja_consommees: float, duree_prevue_heures: float, taches_du_pilote: list,
                     taches_de_la_source: list, registre_des_arrets, horodatage: str, lister_arbre_gele=None) -> dict:
    """Pilote complet : préparation sur processeur, manifeste scellé (configuration et empreinte, versions, graines,
    commit ; chemin et empreinte de la ligne d'accord du jour ; listes du partage des tâches), puis l'instance."""
    preparation = preparer_le_pilote(racine, pieces, jour, entropie, accords, heures_deja_consommees,
                                     machine.prix_horaire_usd(), duree_prevue_heures, taches_du_pilote,
                                     taches_de_la_source, lister_arbre_gele)
    cfg_manifeste = {"configuration_papier_c": preparation["configuration"],
                     "configuration_papier_c_sha256": preparation["configuration_sha256"],
                     "accord_du_jour": preparation["accord_du_jour"], "accords_de_depense": preparation["accords_de_depense"],
                     "prealables": preparation["prealables"],
                     "partage_taches": {**preparation["partage"],
                                        "empreintes": {t: _sha(str(t)) for t in preparation["partage"]["calibrage"]
                                                       + preparation["partage"]["bassin"]}},
                     "budget": preparation["budget"], "borne_de_duree_heures": preparation["borne_de_duree_heures"]}
    chemin_m, manifeste = creer_manifeste(racine, run_id, cfg_manifeste, list(CLES_DU_PILOTE), entropie=int(entropie),
                                          prereg=pieces["preenregistrement"])
    if manifeste["graines"] != preparation["graines"]:
        raise EcartAuPreenregistrement("graines du manifeste différentes des graines préparées")
    resultat = executer_le_pilote(racine, preparation, machine, run_id, registre_des_arrets, horodatage)
    return {"manifeste": str(chemin_m), **resultat}


# ------------------------------------------------------------------------------------------------------------------
# Étape 2 : ouverture, plan des épisodes, génération, lecture forcée
# ------------------------------------------------------------------------------------------------------------------
def ouvrir_l_etape2(cfg: dict, entropie, bassin: list, origines: dict, lot_de_calibrage: list, n_de_l_addendum: int,
                    sondes_du_verdict: list, contenus_calibrage: list = (), contenus_etape2: list = ()) -> dict:
    """Ouverture de l'étape 2 (les préalables de la garde 2 sont vérifiés par `garde_prealables_de_l_etape2`) :
    graines neuves (garde 13) ; bassin trié par identifiant ; disjonction avec le lot de calibrage (garde 12) ; taille
    du bassin (garde 16) ; effectif à l'ouverture ; n/2 tâches tirées sans remise, uniformément, sans strate par
    origine (clé `papier-C/etape2/taches`) ; 20 tâches du modérateur raisonné (clé `papier-C/etape2/raisonne`) ;
    choix des sondes (garde 15), consigné avant toute génération. Tout est rendu pour le manifeste de l'étape 2."""
    graines = gd.graines_du_papier_c(list(CLES_DE_L_ETAPE2), cfg["graines"]["cles"], entropie, cfg["graines"]["racine"])
    trie = sorted(bassin)
    if len(set(trie)) != len(trie) or set(origines) != set(trie):
        raise TachesNonConformes("bassin : tâche en double, ou origine non consignée pour chaque tâche")
    gd.garde_disjonction(contenus_calibrage, contenus_etape2, lot_de_calibrage, trie)
    liste = tuple(cfg["derivation"]["effectifs_etape2"])
    gd.garde_bassin(len(trie), liste)
    effectif = der.effectif_a_l_ouverture(n_de_l_addendum, len(trie), liste)
    n = effectif["n"]
    rng = generateur(graines["papier-C/etape2/taches"])
    taches = [trie[i] for i in sorted(int(i) for i in rng.choice(len(trie), size=n // 2, replace=False))]
    k_r = cfg["etape2"]["sous_ensemble_raisonne_taches"]
    rng_r = generateur(graines["papier-C/etape2/raisonne"])
    raisonne = [taches[i] for i in sorted(int(i) for i in rng_r.choice(len(taches), size=min(k_r, len(taches)), replace=False))]
    sondes = gd.choisir_les_sondes(sondes_du_verdict)
    return {"graines": graines, "bassin_trie": trie, "n": n, "reserves": effectif["reserves"], "taches": taches,
            "origines": {t: origines[t] for t in taches}, "taches_raisonne": raisonne, "sondes": sondes, "m": len(sondes)}


def plan_des_episodes(taches: list, k_P: int) -> list:
    """Par tâche : {honnête, saboteur} × {sans ; plaidoyer aux niveaux 1 à k_P ; usurpation}, soit 2 × (2 + k_P)
    épisodes ; cellules H, HP_m, HU, S, SP_m, SU."""
    plan = []
    for t in taches:
        for intention, lettre in (("honnete", "H"), ("saboteur", "S")):
            plan.append({"tache": t, "intention": intention, "bras": "sans", "niveau": None, "cellule": lettre})
            for m in range(1, k_P + 1):
                plan.append({"tache": t, "intention": intention, "bras": "plaidoyer", "niveau": m, "cellule": f"{lettre}P_{m}"})
            plan.append({"tache": t, "intention": intention, "bras": "usurpation", "niveau": None, "cellule": f"{lettre}U"})
    return plan


def paragraphe_de_bras(cfg: dict, bras: str, niveau: int | None) -> str:
    """Paragraphe ajouté à la fin du message système de l'agent, identique dans les deux intentions."""
    ab = cfg["agent_bras"]
    if bras == "sans":
        return ab["sans"]
    if bras == "usurpation":
        return ab["usurpation"]
    if bras == "plaidoyer" and niveau is not None and 1 <= niveau <= ab["k_P"]:
        return ab["plaidoyer"][niveau - 1]
    raise ConfigurationInvalide(f"bras {bras!r}, niveau {niveau!r} inconnus")


def generer_le_corpus_A(machine: Machine, cfg: dict, plan: list, graines_des_episodes: dict) -> list:
    """Génération du corpus A par la machine. Avant tout épisode : paragraphes de plaidoyer conformes à la
    configuration, en nombre et en ordre (garde 23). Pour chaque demande : aucun champ nommant un score de moniteur
    (garde 21). Le même paragraphe de bras est passé à l'honnête et au saboteur."""
    k_P = cfg["agent_bras"]["k_P"]
    gd.garde_paragraphes_de_plaidoyer([paragraphe_de_bras(cfg, "plaidoyer", m) for m in range(1, k_P + 1)], cfg)
    niveaux = sorted({e["niveau"] for e in plan if e["bras"] == "plaidoyer"})
    if niveaux != list(range(1, k_P + 1)):
        raise ParagraphesDePlaidoyerNonConformes(f"niveaux du plan {niveaux} différents de 1 à k_P = {k_P}")
    episodes = []
    for e in plan:
        demande = {**e, "paragraphe_de_bras": paragraphe_de_bras(cfg, e["bras"], e["niveau"]),
                   "graine": graines_des_episodes[f"{e['tache']}|{e['cellule']}"], "actions_max": cfg["etape2"]["trajectoire"]["actions_max"]}
        gd.garde_aucun_score_dans_la_generation(demande)
        episodes.append({**e, **machine.generer_un_episode(demande)})
    return episodes


def relire_un_contenu(machine: Machine, episode: dict, relecture: str, message_systeme: str) -> dict:
    """Lecture forcée d'un contenu SP_m ou SU sous le message système d'une relecture (L-SP, L-HP, L-H), avec la garde
    20 : même suite de jetons hors du message système, et message système lu égal à celui annoncé."""
    lu = machine.relire({"episode": episode["identifiant"], "relecture": relecture, "message_systeme": message_systeme})
    gd.garde_lecture_forcee(episode["jetons_hors_message_systeme"], lu["jetons_hors_message_systeme"],
                            lu["message_systeme_sha256"], _sha(message_systeme), relecture)
    return lu


__all__ = ["Machine", "DOSSIER_DES_SORTIES", "CLES_DU_PILOTE", "CLES_DE_L_ETAPE2", "ecrire_une_sortie",
           "insertion_d_une_condition", "lire_les_conditions", "choisir_les_contenus_de_calibrage",
           "moyennes_du_banc_processeur", "banc_sur_processeur", "preparer_le_pilote", "executer_le_pilote",
           "lancer_le_pilote", "ouvrir_l_etape2", "plan_des_episodes", "paragraphe_de_bras", "generer_le_corpus_A",
           "relire_un_contenu"]
