"""Programme de vérification d'un monde riche écrit par Kimi — prototype v1 (conception ; le programme qui fera foi sera
écrit dans l'arbre de l'organisme sous un nom neuf, essayé et contre-lu).

Concepteur neuf (Claude Opus 5.5), 12 novembre 2026. Aucun appel de modèle, aucun réseau. **N'imprime jamais un coefficient
du monde** : le rapport ne porte que des identifiants opaques d'effets, leurs classes, leurs informations mesurées, des
booléens et des empreintes.

Entrées : le devis du monde (`--devis`, JSON rendu par Kimi, schéma `monde-riche-spec-v1`) ; les exigences (`--exigences`,
JSON gelé dans le préenregistrement avant l'appel à Kimi) ; facultatif : `--etalonner SORTIE.json` (devis étalonné par
programme : facteur d'échelle par effet, bissection vers le milieu de sa classe ; structure, traits, seuils, directions et
sous-populations restent ceux de Kimi) ; `--pieces-servies FICHIER…` (textes gelés servis aux proposeurs, cherchés pour une
fuite des paramètres).

Contrôles (dans cet ordre ; le premier refus donne le code 2, tous sont écrits au rapport) :
  C0 forme      clés permises seules, aucun texte libre, types, bornes (±4), traits et sous-populations dans leur domaine ;
  C1 structure  nombres d'effets par classe et par type, distracteurs, au plus deux conditions de seuil, au plus un latent ;
  C2 grammaire  la loi compilée est une loi de la grammaire (évaluation sur un jeu factice ; nombre de feuilles borné) ;
  C3 tailles    information I_i de chaque effet, mesurée sur deux échantillons indépendants de l'oracle (accord ≤ max(0,002 nat ;
                5 % de I_i)),
                dans les bornes de sa classe ; distracteurs : sensibilité nulle ;
  C4 ensemble   gain du monde sur sa marginale dans ses bornes ; loi connue de départ (programme) informative mais partielle ;
  C5 jeu planté vraies plantées (programme) : gain au-delà de l'archive {K1} ≥ g₀ (oracle v60 et enveloppe) ; fausses
                couvertes : gain au-delà de l'enveloppe ≤ 10⁻³ ;
  C6 oracle     l'attribution retrouve les effets de chaque vraie plantée (ensemble exact) ;
  C7 fuite      aucun paramètre du monde (exact ou à deux décimales, |x| ≥ 0,1) dans les pièces servies données ;
  C8 sensibilité puissance du juge sur chaque effet : part des graines où le monde W est promu contre le nul v8 de {W₋ᵢ}
                (n tirages, seuil hors famille log(m/α)) ; fortes ≥ 0,9 ; moyenne des faibles dans [0,1 ; 0,9] (« proche du
                seuil » rendu opératoire). Mesure du couple juge × monde, sans agent ; écrite au rapport privé.
Codes : 0 conforme ; 2 refus (rapport écrit) ; 3 erreur d'usage.
"""

import argparse
import datetime
import hashlib
import json
import math
import os
import re
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)
import monde_riche_outils_v1 as M  # noqa: E402

VERSION = "verifier-monde-kimi-v1"
CLES_HAUT = {"version", "nombre_issues", "dimension", "sous_populations", "biais", "effets", "distracteurs"}
CLES_EFFET = {
    "principal": {"id", "classe", "type", "trait", "pente"},
    "seuil": {"id", "classe", "type", "trait", "seuil", "decalage"},
    "interaction_seuil": {"id", "classe", "type", "trait_condition", "seuil", "trait", "pente"},
    "interaction_sous_population": {"id", "classe", "type", "sous_population", "trait", "pente"},
    "sous_population": {"id", "classe", "type", "sous_population", "decalage"},
    "latent": {"id", "classe", "type", "poids_melange", "decalage"},
}
EXIGENCES_DEFAUT = {
    "version": "exigences-monde-riche-v1", "nombre_issues": 3, "dimension": 8, "sous_populations": 3,
    "classes": {"forte": [0.10, 0.25], "moyenne": [0.04, 0.08], "faible": [0.02, 0.035]},
    "effets_par_classe": {"forte": [2, 2], "moyenne": [2, 3], "faible": [2, 4]},
    "interactions_min": 2, "distracteurs_min": 2, "conditions_seuil_max": 2, "latents_max": 1,
    "borne_coefficient": 4.0, "borne_seuil": 1.5, "gain_monde": [0.30, 0.90], "gain_k1": [0.05, 0.30],
    "part_k1_max": 0.6, "g0": 0.02, "accord_oracle": 0.002, "accord_oracle_relatif": 0.05, "oracle_instances": 50000,
    "feuilles_max": 24,
    "sensibilite": {"graines": 100, "tirages": 400, "m": 40, "graine_racine": 20261112,
                    "forte_min": 0.9, "faible_moyenne": [0.1, 0.9]},
}


class Refus(Exception):
    def __init__(self, controle, motif):
        super().__init__(f"{controle} : {motif}")
        self.controle, self.motif = controle, motif


def _fini(x, borne=None):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x) and (borne is None or abs(x) <= borne)


def _entier(x, lo, hi):
    return isinstance(x, int) and not isinstance(x, bool) and lo <= x < hi


def controler_forme(spec, ex):
    if not isinstance(spec, dict) or set(spec) != CLES_HAUT:
        raise Refus("C0", f"clés du devis ≠ {sorted(CLES_HAUT)}")
    if spec["version"] != "monde-riche-spec-v1":
        raise Refus("C0", "version inattendue")
    for c in ("nombre_issues", "dimension", "sous_populations"):
        if spec[c] != ex[c]:
            raise Refus("C0", f"{c} ≠ {ex[c]}")
    K, D, nsp = spec["nombre_issues"], spec["dimension"], spec["sous_populations"]
    B, BS = ex["borne_coefficient"], ex["borne_seuil"]
    if not (isinstance(spec["biais"], list) and len(spec["biais"]) == K and all(_fini(x, B) for x in spec["biais"])):
        raise Refus("C0", "biais : K réels finis bornés")
    if not isinstance(spec["effets"], list) or not spec["effets"]:
        raise Refus("C0", "effets : liste non vide")
    ids = set()
    for e in spec["effets"]:
        if not isinstance(e, dict) or e.get("type") not in CLES_EFFET or set(e) != CLES_EFFET[e["type"]]:
            raise Refus("C0", "effet : type inconnu ou clés non permises")
        if not (isinstance(e["id"], str) and re.fullmatch(r"E[0-9]{1,2}", e["id"])) or e["id"] in ids:
            raise Refus("C0", "identifiant d'effet : « E » suivi d'un ou deux chiffres, unique")
        ids.add(e["id"])
        if e["classe"] not in ex["classes"]:
            raise Refus("C0", f"{e['id']} : classe inconnue")
        for c in ("trait", "trait_condition"):
            if c in e and not _entier(e[c], 0, D):
                raise Refus("C0", f"{e['id']} : {c} hors de [0 ; {D}[")
        if "sous_population" in e and not _entier(e["sous_population"], 0, nsp):
            raise Refus("C0", f"{e['id']} : sous-population hors domaine")
        if "seuil" in e and not _fini(e["seuil"], BS):
            raise Refus("C0", f"{e['id']} : seuil fini, |seuil| ≤ {BS}")
        for c in ("pente", "decalage"):
            if c in e and not (isinstance(e[c], list) and len(e[c]) == K and all(_fini(x, B) for x in e[c])):
                raise Refus("C0", f"{e['id']} : {c} = K réels finis, |x| ≤ {B}")
        if e["type"] == "interaction_seuil" and e["trait"] == e["trait_condition"]:
            raise Refus("C0", f"{e['id']} : interaction d'un trait avec lui-même")
        if e["type"] == "latent" and not (_fini(e["poids_melange"]) and 0.2 <= e["poids_melange"] <= 0.8):
            raise Refus("C0", f"{e['id']} : poids du mélange latent dans [0,2 ; 0,8]")
    if not (isinstance(spec["distracteurs"], list) and all(_entier(t, 0, D) for t in spec["distracteurs"])
            and len(set(spec["distracteurs"])) == len(spec["distracteurs"])):
        raise Refus("C0", "distracteurs : liste de traits distincts")


def controler_structure(spec, ex):
    par_classe = {c: sum(1 for e in spec["effets"] if e["classe"] == c) for c in ex["classes"]}
    for c, (lo, hi) in ex["effets_par_classe"].items():
        if not lo <= par_classe.get(c, 0) <= hi:
            raise Refus("C1", f"effets de classe {c} : {par_classe.get(c, 0)} hors de [{lo} ; {hi}]")
    inter = sum(1 for e in spec["effets"] if e["type"] in ("interaction_seuil", "interaction_sous_population"))
    if inter < ex["interactions_min"]:
        raise Refus("C1", f"interactions : {inter} < {ex['interactions_min']}")
    utilises = set()
    for e in spec["effets"]:
        utilises |= {t for t in M.traits_d_un_effet(e) if isinstance(t, int)}
    if set(spec["distracteurs"]) & utilises:
        raise Refus("C1", "un distracteur déclaré est utilisé par un effet")
    libres = set(range(spec["dimension"])) - utilises
    if set(spec["distracteurs"]) != libres or len(libres) < ex["distracteurs_min"]:
        raise Refus("C1", f"distracteurs déclarés ≠ traits sans effet, ou moins de {ex['distracteurs_min']}")
    if len(M._conditions(spec["effets"])) > ex["conditions_seuil_max"]:
        raise Refus("C1", "trop de conditions de seuil distinctes")
    if sum(1 for e in spec["effets"] if e["type"] == "latent") > ex["latents_max"]:
        raise Refus("C1", "trop de traits latents")
    return par_classe


def _feuilles(loi):
    t = loi["type"]
    if t == "softmax":
        return 1
    if t == "si_sinon":
        return _feuilles(loi["si"]) + _feuilles(loi["sinon"])
    if t == "par_sous_population":
        return sum(_feuilles(v) for v in loi["lois"].values())
    if t == "melange":
        return sum(_feuilles(c) for c in loi["composantes"])
    return 1


def controler_grammaire(spec, ex):
    loi = M.compiler_monde(spec)
    if _feuilles(loi) > ex["feuilles_max"]:
        raise Refus("C2", f"loi compilée : {_feuilles(loi)} feuilles > {ex['feuilles_max']}")
    rng = np.random.default_rng(0)
    Z, G = M.tirer_instances(rng, 64, spec["dimension"], spec["sous_populations"])
    P = M.probas(loi, Z, G)
    if not (np.all(np.isfinite(P)) and np.allclose(P.sum(axis=1), 1.0)):
        raise Refus("C2", "loi compilée non évaluable")
    try:  # validateur de la grammaire de la copie v52b, s'il est lisible (lecture seule)
        sys.path.insert(0, "/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/orchestrateur-v52b")
        from pole import selection_pari as sp
        sp.valider_loi(loi, spec["nombre_issues"], spec["dimension"])
        valide = "valider_loi v52b : conforme"
    except ImportError:
        valide = "valider_loi non disponible (évaluation seule)"
    except Exception as e:  # noqa: BLE001
        raise Refus("C2", f"valider_loi : {type(e).__name__}")
    return loi, valide


def mesurer(spec, ex, graines=(1, 2)):
    loi = M.compiler_monde(spec)
    oracles = [M.Oracle(loi, spec["dimension"], spec["sous_populations"], n=ex["oracle_instances"], graine=g) for g in graines]
    infos = [{e["id"]: o.information_effet(spec, e["id"]) for e in spec["effets"]} for o in oracles]
    return loi, oracles, infos


def controler_tailles(spec, ex, infos, oracles):
    out = {}
    for e in spec["effets"]:
        a, b = infos[0][e["id"]], infos[1][e["id"]]
        lo, hi = ex["classes"][e["classe"]]
        out[e["id"]] = {"classe": e["classe"], "information_nat": round(a, 5), "accord": round(abs(a - b), 6)}
        if abs(a - b) > max(ex["accord_oracle"], ex.get("accord_oracle_relatif", 0.0) * max(a, b)):
            raise Refus("C3", f"{e['id']} : deux échantillons de l'oracle en désaccord ({abs(a - b):.4f} nat)")
        if not lo <= a <= hi:
            raise Refus("C3", f"{e['id']} ({e['classe']}) : information {a:.4f} nat hors de [{lo} ; {hi}]")
    o = oracles[0]
    rng = np.random.default_rng(3)
    for t in spec["distracteurs"]:
        Z2 = o.Z.copy()
        Z2[:, t] = np.round(rng.standard_normal(len(Z2)), 6)
        if M._kl_moyen(o.Q, M.probas(M.compiler_monde(spec), Z2, o.G)) > 1e-9:
            raise Refus("C3", f"distracteur {t} : sensibilité non nulle")
    return out


def controler_ensemble_et_jeu(spec, ex, o):
    loi = M.compiler_monde(spec)
    g = o.gain(loi)
    lo, hi = ex["gain_monde"]
    if not lo <= g <= hi:
        raise Refus("C4", f"gain du monde {g:.4f} hors de [{lo} ; {hi}]")
    k1, eid, infos, vraies, fausses = M.jeu_plante_mr1(spec, o)
    gk = o.gain(k1)
    if not ex["gain_k1"][0] <= gk <= ex["gain_k1"][1] or gk > ex["part_k1_max"] * g:
        raise Refus("C4", f"loi connue de départ : gain {gk:.4f} hors bornes ou part du monde > {ex['part_k1_max']}")
    rapport = {"gain_monde": round(g, 4), "gain_k1": round(gk, 4), "effet_de_k1": eid, "vraies": {}, "fausses": {}}
    for nom, v in vraies.items():
        a, b = o.gain_au_dela(v["loi"], [k1]), o.gain_au_dela_enveloppe(v["loi"], [k1])
        rapport["vraies"][nom] = {"classe": v["classe"], "au_dela_archive_v60": round(a, 5), "au_dela_enveloppe": round(b, 5),
                                  "vraie_au_sens_de_l_oracle": bool(a >= ex["g0"] and b >= ex["g0"])}
    for nom, l in fausses.items():
        b = o.gain_au_dela_enveloppe(l, [k1])
        rapport["fausses"][nom] = {"au_dela_enveloppe": round(b, 6), "au_dela_archive_v60": round(o.gain_au_dela(l, [k1]), 6)}
        if b > 1e-3:
            raise Refus("C5", f"fausse {nom} : gain au-delà de l'enveloppe {b:.5f} > 10⁻³")
    if not rapport["vraies"]["V-monde"]["vraie_au_sens_de_l_oracle"]:
        raise Refus("C5", "le monde lui-même n'est pas une vraie découverte au-delà de {K1}")
    k1e = [n for n in rapport["vraies"] if n.startswith("V-K1+") and rapport["vraies"][n]["vraie_au_sens_de_l_oracle"]]
    if len(k1e) < ex.get("vraies_k1_plus_effet_min", 3):
        raise Refus("C5", f"vraies « K1 + un effet » au-dessus de g₀ : {len(k1e)} < {ex.get('vraies_k1_plus_effet_min', 3)}")
    for c in (0.03, 0.05):
        if abs(rapport["vraies"][f"V-dilue-{c}"]["au_dela_archive_v60"] - c) > 0.002:
            raise Refus("C5", f"vraie diluée {c} : gain au-delà de l'archive hors de ±0,002")
    # une vraie « K1 + effet » sous g₀ reste une mesure (rapportée), jamais une vraie du critère
    rapport["vraies_sous_g0_mesure_seulement"] = sorted(n for n, r in rapport["vraies"].items() if not r["vraie_au_sens_de_l_oracle"])
    return rapport, k1, eid, vraies, infos


def controler_oracle(spec, o, vraies, infos, rapport):
    ecarts = {}
    for nom, v in vraies.items():
        if not nom.startswith("V-K1+"):
            continue
        c = M.captes(o.attribution(v["loi"], spec), infos)
        ecarts[nom] = sorted(set(c) ^ set(v["effets"]))
    rapport["attribution_ecarts"] = {k: len(v) for k, v in ecarts.items()}
    mauvais = [k for k, v in ecarts.items() if v and rapport["vraies"][k]["vraie_au_sens_de_l_oracle"]]
    if mauvais:
        raise Refus("C6", f"attribution en écart pour {len(mauvais)} vraie(s) plantée(s) au-dessus de g₀")
    return True


def controler_sensibilite(spec, ex):
    c = ex["sensibilite"]
    W = M.compiler_monde(spec)
    D, nsp = spec["dimension"], spec["sous_populations"]
    out = {}
    for e in spec["effets"]:
        Wm = M.compiler_monde(spec, sans=(e["id"],))
        x = 0
        for g in range(c["graines"]):
            cle = int.from_bytes(hashlib.sha256(f"sensibilite|{e['id']}".encode()).digest()[:4], "big")
            rng = np.random.default_rng(np.random.SeedSequence(c["graine_racine"], spawn_key=(cle, g)))
            x += M.promue_hors_famille(M.juger(W, [Wm], W, D, nsp, rng, n=c["tirages"]), c["m"])[0]
        out[e["id"]] = {"classe": e["classe"], "puissance": round(x / c["graines"], 4), "graines": c["graines"]}
    fortes = [v["puissance"] for v in out.values() if v["classe"] == "forte"]
    faibles = [v["puissance"] for v in out.values() if v["classe"] == "faible"]
    if fortes and min(fortes) < c["forte_min"]:
        raise Refus("C8", f"un effet fort détecté dans {min(fortes):.2f} des graines < {c['forte_min']}")
    if faibles and not c["faible_moyenne"][0] <= float(np.mean(faibles)) <= c["faible_moyenne"][1]:
        raise Refus("C8", f"puissance moyenne des effets faibles {np.mean(faibles):.2f} hors de {c['faible_moyenne']}")
    return out


def valeurs_du_monde(spec):
    vals = []
    for e in spec["effets"]:
        for c in ("pente", "decalage", "seuil"):
            v = e.get(c)
            vals += (v if isinstance(v, list) else [v] if v is not None else [])
    vals += spec["biais"]
    return [x for x in vals if abs(x) >= 0.1]


def controler_fuite(spec, pieces):
    touches = 0
    vals = valeurs_du_monde(spec)
    for p in pieces:
        texte = open(p, encoding="utf-8").read()
        nombres = [float(x) for x in re.findall(r"-?\d+\.\d+", texte)]
        for v in vals:
            if any(abs(x - v) < 5e-7 or (abs(round(x, 2) - round(v, 2)) < 1e-9 and len(str(x).split(".")[1]) <= 2) for x in nombres):
                touches += 1
    if touches:
        raise Refus("C7", f"{touches} paramètre(s) du monde trouvés dans les pièces servies")
    return touches


def etalonner(spec, ex, n_oracle=8000, graine=7):
    """Facteur d'échelle par effet (bissection) pour que son information tombe au milieu de sa classe ; trois passes."""
    loi = M.compiler_monde(spec)
    Zg, Gg = M.tirer_instances(np.random.default_rng(np.random.SeedSequence(graine)), n_oracle, spec["dimension"], spec["sous_populations"])
    fac = {e["id"]: 1.0 for e in spec["effets"]}

    def info(eid, f):
        f2 = dict(fac, **{eid: f})
        Q = M.probas(M.compiler_monde(spec, facteurs=f2), Zg, Gg)
        Qm = M.probas(M.compiler_monde(spec, sans=(eid,), facteurs=f2), Zg, Gg)
        return float((Q * (np.log(np.maximum(Q, M.PLANCHER)) - np.log(np.maximum(Qm, M.PLANCHER)))).sum(axis=1).mean())

    for _ in range(3):
        for e in spec["effets"]:
            lo_c, hi_c = ex["classes"][e["classe"]]
            cible = 0.5 * (lo_c + hi_c)
            lo, hi = 0.0, 12.0
            for _ in range(28):
                mid = 0.5 * (lo + hi)
                lo, hi = (mid, hi) if info(e["id"], mid) < cible else (lo, mid)
            fac[e["id"]] = 0.5 * (lo + hi)
    s2 = json.loads(json.dumps(spec))
    for e in s2["effets"]:
        for c in ("pente", "decalage"):
            if c in e:
                e[c] = np.clip(np.round(np.asarray(e[c]) * fac[e["id"]], 6), -ex["borne_coefficient"], ex["borne_coefficient"]).tolist()
    return s2, {k: round(v, 6) for k, v in fac.items()}


def verifier(spec, ex, pieces=()):
    rapport = {"version": VERSION, "conforme": False, "controles": {}}
    try:
        controler_forme(spec, ex)
        rapport["controles"]["C0"] = "tenu"
        rapport["effets_par_classe"] = controler_structure(spec, ex)
        rapport["controles"]["C1"] = "tenu"
        _, valide = controler_grammaire(spec, ex)
        rapport["controles"]["C2"] = "tenu ; " + valide
        loi, oracles, infos = mesurer(spec, ex)
        rapport["tailles"] = controler_tailles(spec, ex, infos, oracles)
        rapport["controles"]["C3"] = "tenu"
        r45, k1, eid, vraies, infos_k = controler_ensemble_et_jeu(spec, ex, oracles[0])
        rapport["ensemble_et_jeu_plante"] = r45
        rapport["controles"]["C4"] = rapport["controles"]["C5"] = "tenu"
        controler_oracle(spec, oracles[0], vraies, infos[0], r45)
        rapport["controles"]["C6"] = "tenu"
        rapport["controles"]["C7"] = f"tenu ({len(pieces)} pièce(s) cherchée(s))" if pieces else "sans objet (aucune pièce donnée)"
        if pieces:
            controler_fuite(spec, pieces)
        rapport["sensibilite"] = controler_sensibilite(spec, ex)
        rapport["controles"]["C8"] = "tenu"
        rapport["conforme"] = True
    except Refus as r:
        rapport["controles"][r.controle] = "refus : " + r.motif
        rapport["refus"] = {"controle": r.controle, "motif": r.motif}
    return rapport


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--devis", required=True)
    a.add_argument("--exigences")
    a.add_argument("--sortie", required=True)
    a.add_argument("--etalonner")
    a.add_argument("--pieces-servies", nargs="*", default=[])
    x = a.parse_args(argv)
    for p in (x.sortie, x.etalonner):
        if p and os.path.exists(p):
            print(f"refus : {p} existe déjà (on n'écrase jamais)")
            return 3
    ex = json.load(open(x.exigences)) if x.exigences else EXIGENCES_DEFAUT
    octets = open(x.devis, "rb").read()
    try:
        spec = json.loads(octets)
    except ValueError:
        spec = None
    entete = {"devis_sha256": hashlib.sha256(octets).hexdigest(), "exigences_sha256": M.empreinte(ex),
              "heure_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")}
    if x.etalonner and spec is not None:
        try:
            controler_forme(spec, ex)
            controler_structure(spec, ex)
            spec, facteurs = etalonner(spec, ex)
            octets2 = json.dumps(spec, sort_keys=True, ensure_ascii=False, indent=1).encode()
            with open(x.etalonner, "wb") as f:
                f.write(octets2)
            entete.update(etalonne_sha256=hashlib.sha256(octets2).hexdigest(), facteurs_d_etalonnage=facteurs)
        except Refus as r:
            entete["etalonnage_refuse"] = str(r)
    rapport = verifier(spec, ex, x.pieces_servies) if spec is not None else {"conforme": False, "refus": {"controle": "C0", "motif": "JSON illisible"}}
    rapport.update(entete)
    with open(x.sortie, "w", encoding="utf-8") as f:
        json.dump(rapport, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({"conforme": rapport["conforme"], "refus": rapport.get("refus")}, ensure_ascii=False))
    return 0 if rapport["conforme"] else 2


if __name__ == "__main__":
    sys.exit(main())
