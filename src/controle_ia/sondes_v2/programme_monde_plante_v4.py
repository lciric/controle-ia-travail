"""Programme de l'épreuve à vérité plantée, version 4 (brique D ; décisions du concepteur des sondes v2, cb270590…, § 7,
lues avec leur erratum 1, 019cff39…, qui prime ; plan et devis v2, 717cea17…). La v3 reste telle quelle (R12).

Deux modes, sur les mondes engagés dans `verites_mondes_plantes_v4.json` (scellé avant toute exécution) :
- « complet » (`--taille paires,tâches,actions`, une famille) : toutes les lignes ; rejeu croisé lu à α et à α / D,
  D = `--doses-rejeu` ;
- « étalon » (`--cas paires,familles,tâches,actions`, ou `--grille`) : étalon de transport par famille, contrôle
  d'intensité, sonde d'identité quand un critère la demande.
Avec `--note-effectifs CHEMIN` (spécification v2 de la note des effectifs), les cases et D sont lus dans la note, au
lieu de `--taille`, `--cas` ou `--grille` ; l'empreinte de la note entre au rapport.

**Plages de répliques** (`--repliques-de A --repliques-a B`, de A compris à B exclu) : les graines dérivent du mode, de
la case, du monde et du numéro de réplique, jamais de la plage ; chaque processus écrit son rapport scellé, avec ses
lectures par réplique ; `fusionner` réunit des rapports de plages disjointes et rend la même synthèse, à l'octet, qu'un
seul processus.

Le rapport porte, par monde : les critères (part admise, intervalle exact à 95 %, passage), la table des lectures, les
grandeurs plantées réalisées (moyenne et quantiles 0,05, 0,5, 0,95), le nombre de rejeux du contraste et son plafond de
puissance, et les contrôles de signe (nature « garde ») non passés, chacun avec sa conséquence écrite d'avance : la
ligne du rejeu croisé est « non testable à cet effectif ».

    python -m controle_ia.sondes_v2.programme_monde_plante_v4 --sortie DOSSIER (--taille P,T,A | --cas P,F,T,A |
        --grille | --note-effectifs CHEMIN --mode complet|etalon) [--doses-rejeu D] [--repliques 500]
        [--repliques-de A --repliques-a B] [--nul 199] [--tirages 2000] [--alpha …] [--u-fort …] [--d 256]
        [--entropie N] [--mondes a,b] [--k-externes 5] [--regle-cas-mixte R]
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
import time
from pathlib import Path

from ..gardes import GardeArret, etat_git
from ..manifeste import config_canonique, graines
from ..scellement import sceller, verifier
from . import formats_v1 as fm
from . import lecture_v2 as lc
from . import monde_plante_v4 as mp
from . import statistiques_v2 as st

FORMAT_RAPPORT = "rapport-monde-plante-v4"
FORMAT_SYNTHESE_FUSIONNEE = "synthese-fusionnee-monde-plante-v4"
CONSEQUENCE_GARDE_REJEU = "ligne du rejeu croisé : non testable à cet effectif"


def _entiers(texte: str, n: int) -> tuple:
    try:
        v = tuple(int(x) for x in texte.split(","))
    except ValueError:
        v = ()
    if len(v) != n:
        raise GardeArret(f"{texte!r} : {n} entiers séparés par des virgules attendus")
    return v


def _canon(x) -> bytes:
    return (json.dumps(x, ensure_ascii=False, indent=1, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")


def _sans_nan(x):
    if isinstance(x, float):
        return None if x != x or x in (float("inf"), float("-inf")) else x
    if isinstance(x, dict):
        return {k: _sans_nan(v) for k, v in x.items()}
    if isinstance(x, list):
        return [_sans_nan(v) for v in x]
    return x


def synthese(verites: dict, mode: str, lectures_par_case: dict, repliques: int, n_nul: int, seuils: dict) -> dict:
    """Critères, table des lectures, grandeurs, plafond du contraste et gardes non passées, à partir des lectures par
    réplique `{case: {monde: {réplique (texte): lecture}}}`, qui doivent couvrir 0 … repliques − 1."""
    cases = {}
    for cle_c, par_monde in lectures_par_case.items():
        n_p = int(cle_c.split(",")[0])
        n_f = int(cle_c.split(",")[1]) if mode == "etalon" else 1
        sortie_m = {}
        for m, par_r in par_monde.items():
            if sorted(par_r, key=int) != [str(r) for r in range(repliques)]:
                raise GardeArret(f"case {cle_c}, monde {m} : répliques {sorted(par_r, key=int)[:3]}… au lieu de "
                                 f"0 … {repliques - 1}")
            lectures = [par_r[str(r)] for r in range(repliques)]
            criteres = [k for k in verites["mondes"][m]["criteres"]
                        if mode == "complet" or k["lecture"] in mp.CRITERES_ETALON]
            sortie_c, gardes = [], []
            for k in criteres:
                lues = [l for l in lectures if k["lecture"] in l]
                if not lues:
                    raise GardeArret(f"monde {m} : critère engagé « {k['lecture']} » jamais lu")
                if len(lues) != len(lectures) and k["lecture"] != "fuite" and m != "fuite_de_pli":
                    raise GardeArret(f"monde {m} : critère « {k['lecture']} » manquant dans une réplique")
                oui, n = mp.compter(lues, k)
                r = {**k, **mp.passage(oui, n, k)}
                sortie_c.append(r)
                if k["nature"] == "garde" and r.get("passe") is False and k["lecture"] in mp.LECTURES_DU_REJEU:
                    gardes.append({"lecture": k["lecture"], "admises": k["admises"],
                                   "consequence": CONSEQUENCE_GARDE_REJEU})
            table = {}
            for crit in mp.CRITERES:
                vals = [mp.base_libelle(str(v)) for l in lectures for v in l.get(crit, [])]
                if vals:
                    table[crit] = {x: vals.count(x) for x in sorted(set(vals))}
            noms_g = sorted({g for l in lectures for g in l.get(mp.GRANDEURS, {})})
            grandeurs = {}
            for g in noms_g:
                if mode == "etalon" and g in ("U", "rho", "U_controle", "rho_controle"):
                    par_famille = {}
                    for fi in range(n_f):
                        vals_f = []
                        for l in lectures:
                            gv = l.get(mp.GRANDEURS, {}).get(g, [])
                            vals_f.append(float("nan") if fi >= len(gv) or gv[fi] is None else gv[fi])
                        par_famille[str(fi)] = mp.resume_grandeurs(vals_f)
                    grandeurs[g] = par_famille
                else:
                    vals_g = []
                    for l in lectures:
                        gv = l.get(mp.GRANDEURS, {}).get(g, [])
                        if not gv:
                            vals_g.append(float("nan"))
                        else:
                            vals_g.extend(float("nan") if x is None else x for x in gv)
                    grandeurs[g] = mp.resume_grandeurs(vals_g)
            sortie_m[m] = {"criteres": sortie_c, "table_des_lectures": table, "grandeurs_realisees": grandeurs,
                           "gardes_non_passees": gardes}
            if mode == "complet":
                r_eff_liste = [
                    x for l in lectures
                    for x in l.get(mp.GRANDEURS, {}).get("contraste_rejeux_effectifs", [])
                    if x is not None and x == x
                ]
                r_eff_min = int(min(r_eff_liste)) if r_eff_liste else n_nul
                r_eff_max = int(max(r_eff_liste)) if r_eff_liste else n_nul
                c_info = lc.plafond_puissance_contraste(n_p, r_eff_min, seuils["alpha"])
                c_info["rejeux_demandes"] = int(n_nul)
                c_info["rejeux_effectifs_min"] = r_eff_min
                c_info["rejeux_effectifs_max"] = r_eff_max
                c_info["plafond_demande"] = lc.plafond_puissance_contraste(n_p, n_nul, seuils["alpha"])
                sortie_m[m]["contraste"] = c_info
        cases[cle_c] = sortie_m
    return {"cases": cases}


def _verifier_additif_cas_mixte(additif_chemin, regle_cas_mixte: str) -> dict:
    """Vérifie le compagnon de l'additif scellé et s'assure qu'il mentionne la règle retenue (m11)."""
    if additif_chemin is None:
        raise GardeArret("cas mixte : --additif-cas-mixte CHEMIN obligatoire dès qu'une règle est passée")
    sha = verifier(additif_chemin)
    texte = Path(additif_chemin).read_text(encoding="utf-8")
    if regle_cas_mixte not in texte:
        raise GardeArret(f"cas mixte : l'additif scellé {additif_chemin} ne mentionne pas la règle {regle_cas_mixte!r}")
    return {"chemin": str(additif_chemin), "sha256": sha, "regle": regle_cas_mixte}


def executer(sortie, mode: str, cas: list[tuple], repliques: int, n_nul: int, n_tirages: int, seuils: dict, d: int,
             entropie: int | None, mondes=None, k_externes: int = 5, famille: str = "difference_moyennes_appariee",
             journal_progres=None, n_nul_identite: int = 200, autoriser_depot_sale: bool = False,
             doses_rejeu: int = 1, plage: tuple[int, int] | None = None, regle_cas_mixte: str | None = None,
             note_effectifs: dict | None = None, additif_cas_mixte: dict | None = None,
             go_extension: str | None = None) -> Path:
    """`cas` : en mode « complet », (paires, tâches, actions) ; en mode « étalon », (paires, familles, tâches,
    actions). `plage` : (de, à), à exclu ; par défaut toutes les répliques."""
    if mode not in ("complet", "etalon"):
        raise GardeArret(f"mode {mode!r}")
    if mode == "etalon" and regle_cas_mixte is not None:
        raise GardeArret("cas mixte : --regle-cas-mixte refusé en mode étalon")
    if regle_cas_mixte is not None and additif_cas_mixte is None:
        raise GardeArret("cas mixte : règle passée sans additif scellé (m11)")
    verites, sha = mp.charger_verites()
    noms = [m for m, v in verites["mondes"].items() if mode in v["modes"]] if mondes is None else list(mondes)
    for m in noms:
        if m not in verites["mondes"] or mode not in verites["mondes"][m]["modes"]:
            raise GardeArret(f"monde {m!r} non engagé pour le mode {mode}")
    if repliques < 1 or n_nul < 1 or n_tirages < 1 or not 0.0 < seuils["alpha"] < 1.0:
        raise GardeArret("répliques, nul et tirages ≥ 1 ; 0 < α < 1")
    if not isinstance(doses_rejeu, int) or doses_rejeu < 1:
        raise GardeArret("doses du rejeu croisé : un entier ≥ 1")
    de, a = (0, repliques) if plage is None else plage
    if not 0 <= de < a <= repliques:
        raise GardeArret(f"plage de répliques [{de}, {a}) hors de [0, {repliques})")
    git = etat_git(Path(__file__).resolve().parents[3])
    reserves = []
    if not git["propre"]:
        if not autoriser_depot_sale:
            raise GardeArret("arbre de travail non propre : committer avant le run, ou autoriser explicitement")
        reserves.append("arbre de travail non propre au lancement (autorisé explicitement)")
    racine = graines(["racine"], entropie)["racine"]
    ent = int(racine["entropie"])
    sortie = Path(sortie)
    sortie.mkdir(parents=True, exist_ok=True)
    suffixe = f"{mode}-{ent}" + ("" if plage is None else f"-r{de}-{a}")
    chemin = sortie / f"{FORMAT_RAPPORT}-{suffixe}.json"
    journal = sortie / f"journal-gels-monde-plante-v4-{suffixe}.jsonl"
    if chemin.exists() or journal.exists():
        raise GardeArret(f"{chemin} ou son journal existe déjà (R12)")
    arguments = {"cas": [list(x) for x in cas], "repliques": repliques, "nul": n_nul, "tirages": n_tirages,
                 "seuils": seuils, "d": d, "mondes": noms, "k_externes": k_externes, "famille": famille,
                 "nul_identite": n_nul_identite, "doses_rejeu": doses_rejeu, "regle_cas_mixte": regle_cas_mixte,
                 "note_effectifs": note_effectifs, "additif_cas_mixte": additif_cas_mixte,
                 "go_extension": go_extension}
    rapport = {"format": FORMAT_RAPPORT, "mode": mode, "verites_sha256": sha, "arguments": arguments,
               "plage": [de, a],
               "graines": {"entropie_racine": str(ent), "schema": "manifeste.graines([f'{mode}/{cas}/{monde}/{r}/{nom}'],"
                           " entropie_racine), nom dans statistiques_v1.GRAINES_NOMMEES ; indépendant de la plage"}}
    rapport["manifeste"] = lc.manifeste_lecture({"programme": "programme_monde_plante_v4", "mode": mode,
                                                 "verites_sha256": sha, "plage": [de, a], **arguments},
                                                {"racine": racine}, git["commit"])
    rapport["manifeste"].update(depot_propre=git["propre"], reserves=reserves)
    debut = time.time()
    lectures_par_case = {}
    for c in cas:
        cle_c = ",".join(map(str, c))
        n_p, n_f, n_t, n_a = (c[0], 1, c[1], c[2]) if mode == "complet" else c
        par_monde = {}
        for m in noms:
            p = mp.parametres(verites, m, n_p, n_f, n_t, n_a, d, mode)
            criteres = [k for k in verites["mondes"][m]["criteres"]
                        if mode == "complet" or k["lecture"] in mp.CRITERES_ETALON]
            avec_id = any(k["lecture"] == "identite" for k in criteres)
            par_r = {}
            for r in range(de, a):
                _, rngs = st.generateurs_nommes(ent, f"{mode}/{cle_c}/{m}/{r}/")
                if mode == "complet":
                    lu = mp.lire_monde(p, rngs, journal, f"{cle_c}/{m}/{r}", seuils, n_nul, n_tirages, famille,
                                       k_externes, n_nul_identite=n_nul_identite, doses_rejeu=doses_rejeu,
                                       regle_cas_mixte=regle_cas_mixte)
                else:
                    lu = mp.lire_etalon(p, rngs, seuils, n_tirages, n_nul_identite, avec_id)
                par_r[str(r)] = _sans_nan(lu)
                if journal_progres is not None:
                    journal_progres(f"{mode} {cle_c} {m} réplique {r + 1}/{repliques}")
            par_monde[m] = par_r
        lectures_par_case[cle_c] = par_monde
    rapport["lectures_par_replique"] = lectures_par_case
    if plage is None:
        rapport["synthese"] = synthese(verites, mode, lectures_par_case, repliques, n_nul, seuils)
    rapport["duree_secondes"] = time.time() - debut
    chemin.write_bytes(_canon(rapport))
    sceller(chemin)
    if journal.exists():
        sceller(journal)
    return chemin


def _config_sha_hors_plage(rapport: dict) -> str:
    import hashlib
    cfg = dict(rapport["manifeste"]["config"])
    if hashlib.sha256(config_canonique(cfg)).hexdigest() != rapport["manifeste"]["config_sha256"]:
        raise GardeArret("fusion : config_sha256 interne du manifeste incohérent")
    cfg.pop("plage", None)
    return hashlib.sha256(config_canonique(cfg)).hexdigest()


def fusionner(chemins: list) -> dict:
    """Réunit des rapports de plages disjointes d'une même exécution (mêmes vérités, mode, arguments, commit, propreté,
    réserves, configuration hors plage et entropie racine ; plages qui couvrent toutes les répliques) ; rend la
    synthèse, identique à l'octet à celle d'un seul processus. Empreinte de chaque rapport vérifiée."""
    rapports = []
    for c in chemins:
        verifier(c)
        rapports.append(json.loads(Path(c).read_text(encoding="utf-8")))
    if not rapports:
        raise GardeArret("fusion : aucun rapport")
    ref = rapports[0]
    if ref["format"] != FORMAT_RAPPORT:
        raise GardeArret(f"fusion : format {ref['format']!r}")
    ref_cfg_sha = _config_sha_hors_plage(ref)
    ref_man = ref["manifeste"]
    cles = ("format", "mode", "verites_sha256", "arguments")
    for r in rapports[1:]:
        for k in cles:
            if r[k] != ref[k]:
                raise GardeArret(f"fusion : rapports d'exécutions différentes (champ {k})")
        if r["graines"]["entropie_racine"] != ref["graines"]["entropie_racine"]:
            raise GardeArret("fusion : entropies racines différentes")
        man = r["manifeste"]
        if man["commit"] != ref_man["commit"]:
            raise GardeArret("fusion : commits différents entre plages")
        if man["depot_propre"] != ref_man["depot_propre"]:
            raise GardeArret("fusion : état de propreté du dépôt différent entre plages")
        if man["reserves"] != ref_man["reserves"]:
            raise GardeArret("fusion : réserves différentes entre plages")
        if _config_sha_hors_plage(r) != ref_cfg_sha:
            raise GardeArret("fusion : config_sha256 hors plage différent entre plages")
    plages = sorted(tuple(r["plage"]) for r in rapports)
    n = ref["arguments"]["repliques"]
    bout = 0
    for de, a in plages:
        if de != bout:
            raise GardeArret(f"fusion : plages non contiguës ou chevauchantes ({plages})")
        bout = a
    if bout != n:
        raise GardeArret(f"fusion : les plages couvrent [0, {bout}) au lieu de [0, {n})")
    lect = {}
    for r in rapports:
        for cle_c, par_monde in r["lectures_par_replique"].items():
            for m, par_r in par_monde.items():
                lect.setdefault(cle_c, {}).setdefault(m, {}).update(par_r)
    verites, sha = mp.charger_verites()
    if sha != ref["verites_sha256"]:
        raise GardeArret("fusion : vérités du dépôt différentes de celles des rapports")
    a = ref["arguments"]
    return synthese(verites, ref["mode"], lect, n, a["nul"], a["seuils"])


def ecrire_synthese_fusionnee(chemins: list, chemin_sortie) -> Path:
    """Écrit et scelle la synthèse fusionnée de rapports de plages disjointes avec les empreintes de chaque rapport
    réuni (M2) ; n'écrase jamais un fichier existant (R12)."""
    chemin_sortie = Path(chemin_sortie)
    if chemin_sortie.exists():
        raise GardeArret(f"{chemin_sortie} existe déjà (R12)")
    syn = fusionner(chemins)
    rapports_meta = []
    for c in sorted(chemins, key=str):
        sha_c = verifier(c)
        r = json.loads(Path(c).read_text(encoding="utf-8"))
        rapports_meta.append({"chemin": str(c), "sha256": sha_c, "plage": r["plage"]})
    ref = json.loads(Path(chemins[0]).read_text(encoding="utf-8"))
    corps = {
        "format": FORMAT_SYNTHESE_FUSIONNEE,
        "mode": ref["mode"],
        "verites_sha256": ref["verites_sha256"],
        "arguments": ref["arguments"],
        "commit": ref["manifeste"]["commit"],
        "depot_propre": ref["manifeste"]["depot_propre"],
        "reserves": ref["manifeste"]["reserves"],
        "entropie_racine": ref["graines"]["entropie_racine"],
        "rapports": rapports_meta,
        "synthese": syn,
    }
    chemin_sortie.parent.mkdir(parents=True, exist_ok=True)
    chemin_sortie.write_bytes(_canon(corps))
    sceller(chemin_sortie)
    return chemin_sortie


def cas_depuis_note(note: dict, mode: str, grille: dict, go_extension: str | None = None) -> tuple[list[tuple], int]:
    """Cases de l'épreuve et D lus dans la note des effectifs (spécification v2, § 3). L'extension de grille (416
    cases) exige `go_extension` explicite citant un GO (m8)."""
    ce = note["cases_de_l_epreuve_plantee"]
    if mode == "complet":
        c = ce["complet"]
        return [(c["paires"], c["taches"], c["actions"])], c["doses_holm"]
    if ce["extension_taches_actions"]:
        if not go_extension or not re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d+", go_extension):
            raise GardeArret("extension de grille (416 cases) : --go-extension GO-AAAA-MM-JJ-NN exigé (devis neuf et GO neuf)")
        return list(itertools.product(grille["paires"], grille["familles"], grille["taches"], grille["actions"])), 1
    e = ce["etalon"]
    return list(itertools.product(grille["paires"], grille["familles"], [e["taches"]], [e["actions"]])), 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--sortie", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--taille", action="append", type=lambda t: _entiers(t, 3))
    g.add_argument("--cas", action="append", type=lambda t: _entiers(t, 4))
    g.add_argument("--grille", action="store_true")
    g.add_argument("--note-effectifs", default=None)
    ap.add_argument("--mode", choices=("complet", "etalon"), default=None)
    ap.add_argument("--doses-rejeu", type=int, default=None)
    ap.add_argument("--go-extension", default=None)
    ap.add_argument("--repliques", type=int, default=None)
    ap.add_argument("--repliques-de", type=int, default=None)
    ap.add_argument("--repliques-a", type=int, default=None)
    ap.add_argument("--nul", type=int, default=199)
    ap.add_argument("--tirages", type=int, default=2000)
    ap.add_argument("--alpha", type=float, default=None)
    ap.add_argument("--u-fort", type=float, default=None)
    ap.add_argument("--d", type=int, default=256)
    ap.add_argument("--entropie", type=int, default=None)
    ap.add_argument("--mondes", default=None)
    ap.add_argument("--k-externes", type=int, default=5)
    ap.add_argument("--nul-identite", type=int, default=200)
    ap.add_argument("--regle-cas-mixte", choices=st.REGLES_CAS_MIXTE, default=None)
    ap.add_argument("--additif-cas-mixte", default=None)
    ap.add_argument("--autoriser-depot-sale", action="store_true")
    a = ap.parse_args(argv)
    v, _ = mp.charger_verites()
    df = v["defauts"]
    seuils = {"alpha": df["alpha"] if a.alpha is None else a.alpha, "u_fort": df["u_fort"] if a.u_fort is None
              else a.u_fort}
    note = None
    additif_meta = None
    if a.additif_cas_mixte is not None and a.regle_cas_mixte is None:
        raise GardeArret("--additif-cas-mixte demande --regle-cas-mixte")
    if a.regle_cas_mixte is not None:
        additif_meta = _verifier_additif_cas_mixte(a.additif_cas_mixte, a.regle_cas_mixte)
    if a.note_effectifs:
        if a.mode is None:
            raise GardeArret("--note-effectifs demande --mode complet ou --mode etalon")
        if a.mode == "etalon" and a.doses_rejeu is not None:
            raise GardeArret("--doses-rejeu est refusé en mode étalon (m8)")
        if a.mode == "etalon" and a.regle_cas_mixte is not None:
            raise GardeArret("--regle-cas-mixte est refusé en mode étalon")
        note_lue = fm.charger_note_effectifs(a.note_effectifs)
        if a.go_extension is not None and not (a.mode == "etalon" and note_lue["note"]["cases_de_l_epreuve_plantee"]["extension_taches_actions"]):
            raise GardeArret("--go-extension ne s'emploie qu'en mode étalon lorsque l'extension est déclenchée")
        etat_mixte = note_lue["cas_mixte"]
        if a.mode == "complet":
            if etat_mixte.startswith("cas mixte") and a.regle_cas_mixte is None:
                raise GardeArret("note des effectifs : cas mixte détecté, --regle-cas-mixte et --additif-cas-mixte "
                                 "exigés avant le lancement")
            if not etat_mixte.startswith("cas mixte") and a.regle_cas_mixte is not None:
                raise GardeArret(f"note des effectifs : état « {etat_mixte} », --regle-cas-mixte refusé hors cas mixte")
        cas, d_note = cas_depuis_note(note_lue["note"], a.mode, v["grille_etalon"], a.go_extension)
        if a.mode == "complet" and a.doses_rejeu is not None and a.doses_rejeu != d_note:
            raise GardeArret(f"--doses-rejeu {a.doses_rejeu} contredit la note des effectifs (D = {d_note})")
        mode, doses = a.mode, d_note
        note = {"chemin": str(a.note_effectifs), "sha256": note_lue["sha256"]}
    else:
        if a.mode is not None:
            raise GardeArret("--mode ne s'emploie qu'avec --note-effectifs")
        if a.go_extension is not None:
            raise GardeArret("--go-extension ne s'emploie qu'avec --note-effectifs")
        if a.taille:
            mode, cas = "complet", a.taille
            doses = 1 if a.doses_rejeu is None else a.doses_rejeu
        else:
            if a.doses_rejeu is not None:
                raise GardeArret("--doses-rejeu est refusé en mode étalon (m8)")
            if a.regle_cas_mixte is not None:
                raise GardeArret("--regle-cas-mixte est refusé en mode étalon")
            gr = v["grille_etalon"]
            mode, doses = "etalon", 1
            cas = a.cas or list(itertools.product(gr["paires"], gr["familles"], gr["taches"], gr["actions"]))
    n_rep = df["repliques"] if a.repliques is None else a.repliques
    if (a.repliques_de is None) != (a.repliques_a is None):
        raise GardeArret("--repliques-de et --repliques-a vont ensemble")
    plage = None if a.repliques_de is None else (a.repliques_de, a.repliques_a)
    chemin = executer(a.sortie, mode, cas, n_rep, a.nul, a.tirages, seuils, a.d, a.entropie,
                      None if a.mondes is None else a.mondes.split(","), a.k_externes,
                      journal_progres=lambda m: print(m, file=sys.stderr, flush=True),
                      n_nul_identite=a.nul_identite, autoriser_depot_sale=a.autoriser_depot_sale,
                      doses_rejeu=doses, plage=plage, regle_cas_mixte=a.regle_cas_mixte, note_effectifs=note,
                      additif_cas_mixte=additif_meta, go_extension=a.go_extension)
    print(chemin)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
