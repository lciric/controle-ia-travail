"""Chargeurs des trois formats des sessions habilitées (décisions du concepteur des sondes v2, cb270590…, § 4 et § 7,
point 8 ; spécifications v2 du concepteur, classe B, sous `docs/notes/sondes-v2-concepteur-opus-v1/`) :

- `charger_note_effectifs` — note des effectifs (`spec-note-des-effectifs-v2.md`) : bloc JSON de la note scellée ;
- `charger_table_bbis` — table des scores gardés de l'apprentissage des sondes sur la tâche, lue par la table de
  correspondance des champs du rejeu croisé (`spec-correspondance-rejeu-croise-v2.md`) ;
- `charger_table_ouvreur` — table de l'ouvreur au format des sondes v2 (`spec-table-de-l-ouvreur-v2.md`).

Aucun de ces chargeurs n'ouvre une activation ni ne calcule sur un score : ils contrôlent un format et le traduisent.
Toute anomalie arrête (`GardeArret`) en nommant la cause, jamais un repli silencieux (R5). Éprouvés sur fichiers
fabriqués seulement.
"""
from __future__ import annotations

import csv
import json
import math
import re
from pathlib import Path

from ..gardes import GardeArret
from ..scellement import verifier
from . import statistiques_v2 as st
from .magasin_v1 import _CHEMIN_B5

HEX64 = re.compile(r"^[0-9a-f]{64}$")
CASES = ("adaptateur|saboteur", "nu|saboteur", "adaptateur|honnete", "nu|honnete")
MOTS_DE_ROLE = ("saboteur", "jumeau", "paire", "famille")


def _cles_exactes(d, attendues, ou: str) -> None:
    if not isinstance(d, dict):
        raise GardeArret(f"{ou} : objet attendu")
    manque, trop = set(attendues) - set(d), set(d) - set(attendues)
    if manque or trop:
        raise GardeArret(f"{ou} : champs manquants {sorted(manque)}, en trop {sorted(trop)}")


def _entier(x, ou: str, minimum: int = 0) -> int:
    if isinstance(x, bool) or not isinstance(x, int) or x < minimum:
        raise GardeArret(f"{ou} : entier ≥ {minimum} attendu, reçu {x!r}")
    return x


def _hex(x, ou: str) -> str:
    if not isinstance(x, str) or not HEX64.match(x):
        raise GardeArret(f"{ou} : 64 hexadécimaux attendus")
    return x


def arrondi_moitie_bas(x: float) -> int:
    """Arrondi au plus proche, la moitié vers le bas (spécification de la note, § 3)."""
    return int(math.ceil(x - 0.5))


# ------------------------------------------------------------------------------------------- note des effectifs

def _bloc_json(texte: str) -> dict:
    blocs = re.findall(r"^```json[ \t]*\n(.*?)^```[ \t]*$", texte, flags=re.S | re.M)
    if len(blocs) != 1:
        raise GardeArret(f"note des effectifs : {len(blocs)} blocs JSON, un seul attendu")
    try:
        return json.loads(blocs[0])
    except json.JSONDecodeError as e:
        raise GardeArret(f"note des effectifs : bloc JSON illisible ({e})") from None


def _sans_mot_de_role(x, ou: str) -> None:
    """Aucune clé de la section des activations, ni aucun nom de série, ne porte un mot de rôle."""
    if isinstance(x, dict):
        for k, v in x.items():
            if any(m in str(k).lower() for m in MOTS_DE_ROLE):
                raise GardeArret(f"{ou} : clé de rôle {k!r} dans la section des activations")
            _sans_mot_de_role(v, f"{ou}.{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x):
            _sans_mot_de_role(v, f"{ou}[{i}]")


def charger_note_effectifs(chemin) -> dict:
    """Vérifie le compagnon, extrait le bloc JSON, contrôle le format (champs exacts, entiers, chemins des quatre cases
    parmi « origine » et « relu », cohérences du § 3) ; rend {"note", "sha256", "cases", "doses_holm", "cas_mixte"}."""
    sha = verifier(chemin)
    n = _bloc_json(Path(chemin).read_text(encoding="utf-8"))
    _cles_exactes(n, ("format", "redigee_par", "date_utc", "aveuglement", "activations", "scores_bbis",
                      "cases_de_l_epreuve_plantee", "minimums", "reserves"), "note")
    if n["format"] != "note-effectifs-sondes-v2-v1":
        raise GardeArret(f"note : format {n['format']!r}")
    _cles_exactes(n["aveuglement"], ("activations", "scores", "table_de_l_ouvreur", "verdict_adaptateurs_jumeaux"),
                  "note.aveuglement")
    for k, v in n["aveuglement"].items():
        if not (isinstance(v, str) and v.startswith("non ouvert")):
            raise GardeArret(f"note.aveuglement.{k} : « non ouvert(e)s » attendu")
    a = n["activations"]
    _sans_mot_de_role(a, "note.activations")
    _cles_exactes(a, ("dossier_run", "inventaire_sha256", "garde_sha256", "regle_garde", "couches_gardees",
                      "chemin_de_calcul", "series", "cles_communes", "nu_relit_les_cles_communes"), "note.activations")
    _hex(a["inventaire_sha256"], "note.activations.inventaire_sha256")
    _hex(a["garde_sha256"], "note.activations.garde_sha256")
    _cles_exactes(a["chemin_de_calcul"], ("programme", "precision", "mode", "gabarit", "source",
                                          "identique_pour_toutes_les_series"), "note.activations.chemin_de_calcul")
    if not isinstance(a["series"], list) or not a["series"]:
        raise GardeArret("note.activations.series : liste non vide attendue")
    for i, s in enumerate(a["series"]):
        _cles_exactes(s, ("nom", "categorie", "cles"), f"note.activations.series[{i}]")
        if s["categorie"] not in ("nu", "adaptateur", "propre"):
            raise GardeArret(f"note.activations.series[{i}] : catégorie {s['categorie']!r}")
        if any(m in str(s["nom"]).lower() for m in MOTS_DE_ROLE):
            raise GardeArret(f"note.activations.series[{i}] : nom de série qui laisse lire un rôle")
        _entier(s["cles"], f"note.activations.series[{i}].cles")
    k = a["cles_communes"]
    _cles_exactes(k, ("definition", "actions", "taches", "taches_par_nombre_d_actions", "distinctes_des_cles_propres"),
                  "note.activations.cles_communes")
    _entier(k["actions"], "cles_communes.actions")
    _entier(k["taches"], "cles_communes.taches", 1)
    _cles_exactes(k["taches_par_nombre_d_actions"], ("1", "2", "3", "4_ou_plus"), "cles_communes.taches_par_nombre")
    for c, v in k["taches_par_nombre_d_actions"].items():
        _entier(v, f"cles_communes.taches_par_nombre_d_actions.{c}")
    if not isinstance(k["distinctes_des_cles_propres"], bool):
        raise GardeArret("cles_communes.distinctes_des_cles_propres : booléen attendu")
    s = n["scores_bbis"]
    _cles_exactes(s, ("table", "colonnes", "doses", "nombre_de_doses"), "note.scores_bbis")
    _cles_exactes(s["table"], ("chemin", "sha256", "ligne_registre"), "note.scores_bbis.table")
    _hex(s["table"]["sha256"], "note.scores_bbis.table.sha256")
    actions_controle = taches_controle = taches_tenues_total = 0
    taches_par_dose = []
    for i, d in enumerate(s["doses"]):
        _cles_exactes(d, ("dose", "plis"), f"scores_bbis.doses[{i}]")
        tt = 0
        for j, p in enumerate(d["plis"]):
            ou = f"scores_bbis.doses[{i}].plis[{j}]"
            _cles_exactes(p, ("pli", "taches_tenues", "actions", "chemins", "actions_en_origine_et_en_relu",
                              "taches_avec_controle_du_chemin"), ou)
            tt += _entier(p["taches_tenues"], f"{ou}.taches_tenues")
            _cles_exactes(p["actions"], CASES, f"{ou}.actions")
            for c in CASES:
                _entier(p["actions"][c], f"{ou}.actions.{c}")
            _cles_exactes(p["chemins"], CASES, f"{ou}.chemins")
            for c in CASES:
                if p["chemins"][c] not in ("origine", "relu"):
                    raise GardeArret(f"{ou}.chemins.{c} : « origine » ou « relu » attendu")
            actions_controle += _entier(p["actions_en_origine_et_en_relu"], f"{ou}.actions_en_origine_et_en_relu")
            taches_controle += _entier(p["taches_avec_controle_du_chemin"], f"{ou}.taches_avec_controle_du_chemin")
            if p["taches_avec_controle_du_chemin"] > p["taches_tenues"]:
                raise GardeArret(f"{ou} : plus de tâches contrôlées que de tâches tenues")
        taches_par_dose.append(tt)
        taches_tenues_total += tt
    _entier(s["nombre_de_doses"], "scores_bbis.nombre_de_doses", 1)
    if s["nombre_de_doses"] != len(s["doses"]):
        raise GardeArret("scores_bbis.nombre_de_doses différent du nombre de doses listées")
    ce = n["cases_de_l_epreuve_plantee"]
    _cles_exactes(ce, ("etalon", "complet", "extension_taches_actions"), "cases_de_l_epreuve_plantee")
    _cles_exactes(ce["etalon"], ("taches", "actions"), "cases.etalon")
    _cles_exactes(ce["complet"], ("paires", "taches", "actions", "doses_holm"), "cases.complet")
    for c in ("taches", "actions"):
        _entier(ce["etalon"][c], f"cases.etalon.{c}", 1)
    _entier(ce["complet"]["paires"], "cases.complet.paires", 2)
    for c in ("taches", "actions", "doses_holm"):
        _entier(ce["complet"][c], f"cases.complet.{c}", 1)
    if not isinstance(ce["extension_taches_actions"], bool):
        raise GardeArret("cases.extension_taches_actions : booléen attendu")
    # cohérences du § 3 (comptes seulement)
    if ce["extension_taches_actions"] == k["distinctes_des_cles_propres"]:
        raise GardeArret("note : l'extension se déclenche si et seulement si les clés communes ne sont pas distinctes "
                         "des clés propres")
    if ce["complet"]["doses_holm"] != s["nombre_de_doses"]:
        raise GardeArret("note : doses_holm différent du nombre de doses")
    if ce["etalon"]["taches"] != k["taches"] or ce["etalon"]["actions"] != max(1, arrondi_moitie_bas(
            k["actions"] / k["taches"])):
        raise GardeArret("note : case de l'étalon différente de la règle du § 3")
    if ce["complet"]["taches"] != min(taches_par_dose):
        raise GardeArret("note : tâches de la case complète différentes du minimum, sur les doses, des tâches tenues")
    _cles_exactes(n["minimums"], ("cles_communes", "rejeu_par_dose"), "note.minimums")
    if not isinstance(n["reserves"], list):
        raise GardeArret("note.reserves : liste attendue")
    if actions_controle == 0:
        cas_mixte = "contrôle absent"
    elif taches_controle == taches_tenues_total:
        cas_mixte = "toutes les tâches contrôlées"
    else:
        cas_mixte = "cas mixte : nœud conditionnel pour Lazar (décisions v2, § 6, point 3)"
    return {"note": n, "sha256": sha, "cases": ce, "doses_holm": ce["complet"]["doses_holm"],
            "controle_du_chemin": cas_mixte}


# ------------------------------------------------------------------------- table des scores et correspondance

def _lire_table(chemin: Path, fmt: str) -> list[dict]:
    if fmt == "jsonl":
        out = []
        for i, l in enumerate(chemin.read_text(encoding="utf-8").splitlines()):
            if l.strip():
                try:
                    out.append(json.loads(l))
                except json.JSONDecodeError:
                    raise GardeArret(f"table des scores : ligne {i} illisible") from None
        return out
    if fmt == "csv":
        with open(chemin, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    raise GardeArret(f"table des scores : format de fichier {fmt!r}")


def _bool_brut(x) -> bool:
    if isinstance(x, bool):
        return x
    if x in ("true", "false"):
        return x == "true"
    raise GardeArret(f"recodage de tache_tenue : {x!r}, « true » ou « false » attendu")


def charger_table_bbis(chemin_table, chemin_correspondance) -> tuple[list[dict], dict]:
    """Spécification v2 de la table de correspondance, § 4 : vérifie les deux empreintes ; lit la table ; applique
    `selection`, `colonnes`, règles et `valeurs` ; rend (lignes aux noms internes, contrôlées par
    `charger_table_scores`, méta) ; la méta porte les deux empreintes, les règles employées, les variables absentes et
    les clés sans jumelle sous l'autre poids."""
    sha_c = verifier(chemin_correspondance)
    sha_t = verifier(chemin_table)
    c = json.loads(Path(chemin_correspondance).read_text(encoding="utf-8"))
    _cles_exactes(c, ("format", "redigee_par", "date_utc", "attestation", "table_source", "selection", "colonnes",
                      "valeurs"), "correspondance")
    if c["format"] != "correspondance-rejeu-croise-v1":
        raise GardeArret(f"correspondance : format {c['format']!r}")
    _cles_exactes(c["table_source"], ("chemin", "sha256", "ligne_registre", "format_fichier"), "table_source")
    if c["table_source"]["sha256"] != sha_t:
        raise GardeArret("correspondance : empreinte de la table source différente de la table lue")
    _cles_exactes(c["colonnes"], st.CHAMPS_TABLE, "correspondance.colonnes")
    brut = _lire_table(Path(chemin_table), c["table_source"]["format_fichier"])
    noms = set().union(*(set(r) for r in brut)) if brut else set()
    for col, val in c["selection"].items():
        if col not in noms:
            raise GardeArret(f"sélection : colonne {col!r} absente du fichier")
    brut = [r for r in brut if all(str(r.get(col)) == str(val) for col, val in c["selection"].items())]
    regles, absentes = {}, []
    col = {}
    for champ, v in c["colonnes"].items():
        if isinstance(v, str):
            if v not in noms:
                raise GardeArret(f"colonne {v!r} (champ {champ}) absente du fichier")
            col[champ] = v
        elif champ == "chemin" and v == {"regle": "quatre_cases_du_texte_scelle"}:
            regles["chemin"] = "quatre_cases_du_texte_scelle"
        elif champ in ("longueur", "pas", "valeur_declaree") and v == {"absente": True}:
            absentes.append(champ)
        elif champ == "tache_tenue" and v == {"constante": True}:
            regles["tache_tenue"] = "constante"
        else:
            raise GardeArret(f"correspondance : règle {v!r} non permise pour le champ {champ}")
    for champ in ("dose", "pli", "source", "poids", "tache", "cle", "score"):
        if champ not in col:
            raise GardeArret(f"correspondance : le champ {champ} demande une colonne")
    recodes = {k: c["valeurs"].get(k) for k in ("source", "poids", "chemin", "tache_tenue")}
    for k in ("source", "poids"):
        if not isinstance(recodes[k], dict):
            raise GardeArret(f"correspondance.valeurs.{k} : recodage exhaustif attendu")
    if "chemin" in col and not isinstance(recodes["chemin"], dict):
        raise GardeArret("correspondance.valeurs.chemin : recodage attendu pour une colonne de chemin")
    if "tache_tenue" in col and not isinstance(recodes["tache_tenue"], dict):
        raise GardeArret("correspondance.valeurs.tache_tenue : recodage attendu pour une colonne")
    for k, admis in (("source", st.SOURCES), ("poids", st.POIDS_REJEU), ("chemin", st.CHEMINS)):
        for b, v in (recodes[k] or {}).items():
            if v not in admis:
                raise GardeArret(f"correspondance.valeurs.{k} : {b!r} → {v!r} hors de {admis}")

    def recoder(k, x):
        table = recodes[k]
        if str(x) not in table:
            raise GardeArret(f"valeur brute non prévue pour {k} : {x!r}")
        return table[str(x)]

    def nombre(x):
        if x is None or x == "":
            return None
        return float(x)

    lignes, vues = [], set()
    for r in brut:
        so, po = recoder("source", r[col["source"]]), recoder("poids", r[col["poids"]])
        if "chemin" in col:
            ch = recoder("chemin", r[col["chemin"]])
        else:
            ch = "origine" if (po, so) in st.CASES_ORIGINE else "relu"
        tt = True if regles.get("tache_tenue") == "constante" else _bool_brut(recoder("tache_tenue",
                                                                                     r[col["tache_tenue"]]))
        ligne = {"dose": str(r[col["dose"]]), "pli": str(r[col["pli"]]), "source": so, "poids": po, "chemin": ch,
                 "tache": str(r[col["tache"]]), "cle": str(r[col["cle"]]), "score": r[col["score"]],
                 "longueur": float("nan") if "longueur" in absentes else nombre(r[col["longueur"]]),
                 "pas": float("nan") if "pas" in absentes else nombre(r[col["pas"]]),
                 "valeur_declaree": None if "valeur_declaree" in absentes else nombre(r[col["valeur_declaree"]]),
                 "tache_tenue": tt}
        for k in ("longueur", "pas"):
            if ligne[k] is None:
                raise GardeArret(f"valeur vide pour {k} (clé {ligne['cle']})")
        if regles.get("chemin"):
            k = (ligne["dose"], ligne["pli"], po, so, ligne["cle"])
            if k in vues:
                raise GardeArret(f"règle des quatre cases : action {k} présente deux fois, hors des quatre cases à un "
                                 "seul chemin")
            vues.add(k)
        lignes.append(ligne)
    out, motif = st.charger_table_scores(lignes, {k: k for k in st.CHAMPS_TABLE})
    if out is None:
        raise GardeArret(f"table des scores : {motif}")
    cles = {}
    for l in out:
        cles.setdefault((l["dose"], l["pli"], l["source"], l["cle"]), set()).add(l["poids"])
    sans_jumelle = sum(1 for v in cles.values() if len(v) == 1)
    meta = {"table_sha256": sha_t, "correspondance_sha256": sha_c, "regles": regles, "variables_absentes": absentes,
            "cles_sans_jumelle": sans_jumelle, "lignes": len(out)}
    return out, meta


# --------------------------------------------------------------------------------------------- table de l'ouvreur

def _series_de_la_garde(chemin_garde) -> set:
    g = json.loads(Path(chemin_garde).read_text(encoding="utf-8"))
    series = set()
    for rel in g.get("fichiers", []):
        m = _CHEMIN_B5.match(rel)
        if not m:
            raise GardeArret(f"garde des activations : chemin hors de la liste blanche {rel!r}")
        series.add(m.group(1))
    if not series:
        raise GardeArret("garde des activations : aucune série")
    return series


def charger_table_ouvreur(chemin, chemin_garde, chemin_registre=None, alpha: float = 0.05) -> dict:
    """Spécification v2 de la table de l'ouvreur, § 3 et § 4 : rend `poids_par_serie`, les familles et leurs paires
    triées, P_f, les familles non calculables (moins de quatre paires) et testables, F, la case (P_f, F) de chaque
    famille et les cases hors de la grille de l'épreuve, les comptes des adaptateurs hors paire et des séries propres."""
    sha = verifier(chemin)
    sha_g = verifier(chemin_garde)
    t = json.loads(Path(chemin).read_text(encoding="utf-8"))
    _cles_exactes(t, ("format", "redigee_par", "date_utc", "sources", "series"), "table de l'ouvreur")
    if t["format"] != "table-ouvreur-sondes-v2-v1":
        raise GardeArret(f"table de l'ouvreur : format {t['format']!r}")
    src = t["sources"]
    _cles_exactes(src, ("table_de_l_ouvreur", "fichier_ferme_des_empreintes", "verdict_scelle",
                        "garde_des_activations"), "sources")
    for k in ("table_de_l_ouvreur", "fichier_ferme_des_empreintes", "garde_des_activations"):
        _cles_exactes(src[k], ("chemin", "sha256"), f"sources.{k}")
        _hex(src[k]["sha256"], f"sources.{k}.sha256")
    _cles_exactes(src["verdict_scelle"], ("chemin", "sha256", "inscrit_au_registre"), "sources.verdict_scelle")
    _hex(src["verdict_scelle"]["sha256"], "sources.verdict_scelle.sha256")
    rid = src["verdict_scelle"]["inscrit_au_registre"]
    if not isinstance(rid, str) or not re.fullmatch(r"R-\d+", rid):
        raise GardeArret("verdict non inscrit au registre : aucune ouverture (liste d'arrêt)")
    if chemin_registre is not None and not re.search(rf"(?<![\d-]){re.escape(rid)}(?!\d)",
                                                      Path(chemin_registre).read_text(encoding="utf-8")):
        raise GardeArret(f"verdict non inscrit au registre ({rid} absent) : aucune ouverture (liste d'arrêt)")
    if src["garde_des_activations"]["sha256"] != sha_g:
        raise GardeArret("table de l'ouvreur : empreinte de la garde des activations différente")
    series_garde = _series_de_la_garde(chemin_garde)
    S = t["series"]
    if set(S) != series_garde:
        raise GardeArret(f"couverture : séries manquantes {sorted(series_garde - set(S))}, en trop "
                         f"{sorted(set(S) - series_garde)}")
    if S.get("nu") != {"type": "nu"}:
        raise GardeArret("couverture : « nu » doit être de type « nu »")
    poids, familles_rd, paires, hors_paire, propres = {}, {}, {}, 0, 0
    for nom, s in sorted(S.items()):
        if nom == "nu":
            poids[nom] = {"type": "nu"}
            continue
        if not isinstance(s, dict) or s.get("type") not in ("adaptateur", "propre"):
            raise GardeArret(f"série {nom} : type {s.get('type') if isinstance(s, dict) else s!r}")
        if s["type"] == "propre":
            _cles_exactes(s, ("type", "producteur"), f"série {nom}")
            if s["producteur"] not in S:
                raise GardeArret(f"série {nom} : producteur {s['producteur']!r} inconnu")
            propres += 1
            continue
        _cles_exactes(s, ("type", "empreinte_adaptateur", "dose", "recette", "famille", "paire", "role"),
                      f"série {nom}")
        _hex(s["empreinte_adaptateur"], f"série {nom}.empreinte_adaptateur")
        if s["role"] not in ("saboteur", "jumeau", "hors_paire"):
            raise GardeArret(f"série {nom} : rôle {s['role']!r} hors de la liste")
        if isinstance(s["dose"], bool) or not isinstance(s["dose"], (int, float)):
            raise GardeArret(f"série {nom} : dose numérique attendue")
        poids[nom] = {"type": "adaptateur", "empreinte_adaptateur": s["empreinte_adaptateur"], "dose": s["dose"]}
        familles_rd.setdefault(s["famille"], set()).add((s["recette"], s["dose"]))
        if s["role"] == "hors_paire":
            if s["paire"] is not None:
                raise GardeArret(f"série {nom} : hors paire avec une paire")
            hors_paire += 1
            continue
        if s["paire"] is None:
            raise GardeArret(f"série {nom} : {s['role']} sans paire")
        paires.setdefault(s["paire"], []).append((nom, s["role"], s["famille"]))
    for f, rd in familles_rd.items():
        if len(rd) != 1:
            raise GardeArret(f"famille {f} : doses ou recettes mêlées {sorted(map(str, rd))}")
    rds = [next(iter(rd)) for rd in familles_rd.values()]
    if len(set(rds)) != len(rds):
        raise GardeArret("deux familles partagent le couple (recette, dose)")
    familles: dict = {}
    for pid in sorted(paires, key=str):
        membres = paires[pid]
        roles = sorted(r for _, r, _ in membres)
        if roles != ["jumeau", "saboteur"]:
            raise GardeArret(f"paire {pid} : rôles {roles}, un saboteur et un jumeau attendus")
        if len({f for _, _, f in membres}) != 1:
            raise GardeArret(f"paire {pid} : à cheval sur deux familles")
        sab = next(n for n, r, _ in membres if r == "saboteur")
        jum = next(n for n, r, _ in membres if r == "jumeau")
        familles.setdefault(membres[0][2], []).append((sab, jum))
    P = {f: len(v) for f, v in familles.items()}
    calculables = {f: p for f, p in P.items() if p >= 4}
    F = len(calculables)
    testables = st.familles_testables(calculables, alpha) if calculables else []
    cases = {f: (P[f], F) for f in calculables}
    hors_grille = sorted({c for c in cases.values() if c[0] > 16 or c[1] > 4})
    return {"sha256": sha, "garde_sha256": sha_g, "poids_par_serie": poids, "familles": familles, "P": P,
            "non_calculables": sorted(f for f in P if P[f] < 4), "testables": testables, "F": F,
            "cases_etalon": cases, "cases_hors_grille": hors_grille, "hors_paire": hors_paire, "propres": propres}


__all__ = ["charger_note_effectifs", "charger_table_bbis", "charger_table_ouvreur", "arrondi_moitie_bas", "CASES",
           "MOTS_DE_ROLE"]
