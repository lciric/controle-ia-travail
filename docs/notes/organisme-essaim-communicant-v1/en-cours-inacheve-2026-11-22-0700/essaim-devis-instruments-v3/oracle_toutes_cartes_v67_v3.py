#!/usr/bin/env python3
"""Oracle recalculé sur TOUTES les cartes proposées de la course v67 (monde S-V1), sans aucun verdict du juge — v3 (garde de la grammaire à tout niveau, y compris les clés de `lois` ; valeurs recopiées contrôlées).

Aucun appel, aucun réseau, aucune dépense. numpy et les outils scellés du monde riche (v1), importés à leur empreinte.

Lecture par LISTE BLANCHE : du journal `boucle-reelle-v66.json`, le programme ne garde que, pour chaque entrée de
`releve.cartes`, les champs `identifiant`, `generation`, `proposeur`, `loi` (projection faite avant tout calcul ; le reste
est jeté). Le fichier de lecture gelée (`lecture-course-reelle.json`, qui porte l'oracle sur les promues) n'est jamais ouvert.
Garde indépendante (LISTE NOIRE) : si la projection contient, à n'importe quelle profondeur, un nom de champ de verdict, de
promotion, de test de mort ou de score du juge, refus (code 3) sans sortie. Une mutation qui élargirait la liste blanche à un
tel champ est donc refusée.

Oracle (même définition que la course simulée v4, `monde_riche_v4.course`) : sous la loi vraie S-V1, archive de départ {K1} :
- « vraie »  : gain au-delà de l'enveloppe du nul de {K1} ≥ SEUIL_ORACLE (0,02 nat) ;
- « fausse » : loi évaluable, gain au-delà de l'enveloppe < 0,02 (aucune structure du monde au-delà de l'archive) ;
- « rien »   : loi absente ou non évaluable par la grammaire (carte malformée).
L'archive est {K1} pour toutes les générations : l'archive réelle de la génération 2 dépend des retenues, donc du juge ;
la prendre ferait entrer un verdict dans la mesure. Information : gain au sens v60 (au-delà de K1 seule) et identité à
l'octet (JSON canonique) à la loi du monde.

Usage :
  python3 -I -B oracle_toutes_cartes_v67_v3.py SOURCE.json SORTIE.json            (source réelle : empreinte exigée)
  python3 -I -B oracle_toutes_cartes_v67_v3.py --essai ARTEFACT.json SORTIE.json  (objets de contrôle, sans empreinte)
Codes : 0 sortie écrite ; 2 source absente ou empreinte fausse ; 3 champ interdit dans la projection ; 4 usage.
"""
import hashlib
import json
import os
import re
import sys

import numpy as np

OUTILS = os.path.join(os.environ.get("DEPOT_CONTROLE_IA", "/home/user/controle-ia-travail"), "docs/notes/organisme-multi-generations-v1/outils-v1")
EMPREINTE_SOURCE = "21bc75f4d81825695b30b2b32f21feaa91322293f6c2c3161a28dc179ec6df71"
CHEMIN_SOURCE_CITE = "/home/user/ideation-organism/resultats/course-v67/poste-local-v1/boucle-reelle-v66.json"
LISTE_BLANCHE = ("identifiant", "generation", "proposeur", "loi")
LISTE_NOIRE = frozenset({"promue", "promues", "retenue", "retenues", "verdict", "verdicts", "gardien", "log_w_max",
                         "statut", "score", "scores", "survit", "survivante", "eliminee", "test_de_mort", "tests_de_mort",
                         "oracle", "vraies_decouvertes", "fausses_decouvertes", "e_valeur", "juge", "promotion",
                         "audit_A2", "au_dessus_de_alpha_holm", "decision"})
GRAINE_ORACLE = 20261122  # SeedSequence(GRAINE_ORACLE) : instances de l'oracle (consignée dans la sortie)
N_ORACLE = 20000


def _verifier_import(nom):
    chemin = os.path.join(OUTILS, nom)
    sha = hashlib.sha256(open(chemin, "rb").read()).hexdigest()
    attendu = open(chemin + ".sha256", encoding="utf-8").read().split()[0]
    if sha != attendu:
        raise SystemExit(f"refus : {nom} d'empreinte {sha}, compagnon {attendu}")
    return sha


class ChampInterdit(Exception):
    pass


def garde_liste_noire(objet, chemin="carte"):
    if isinstance(objet, dict):
        for k, v in objet.items():
            if k in LISTE_NOIRE:
                raise ChampInterdit(f"{chemin}.{k}")
            garde_liste_noire(v, f"{chemin}.{k}")
    elif isinstance(objet, list):
        for i, v in enumerate(objet):
            garde_liste_noire(v, f"{chemin}[{i}]")


# v2 : liste blanche de la GRAMMAIRE dans l'arbre d'une loi (clés admises par type, d'après `monde_riche_outils_v1.probas`) ;
# tout champ inconnu dans l'arbre, de quelque nom qu'il soit (`promu`, `rang`, `log_w`…), fait refuser (code 3).
CLES_PAR_TYPE = {"fixe": {"probas"}, "softmax": {"poids", "biais"}, "par_sous_population": {"lois", "defaut"},
                 "melange": {"poids", "composantes"}, "si_sinon": {"condition", "si", "sinon"}, "echelle": {"facteurs", "loi"},
                 "enveloppe": {"lois"}, "transformee": {"base", "melange_aveugle", "puissance", "inclinaison", "oscillation"}}
CLES_CONDITION = ({"sous_population"}, {"indice", "seuil"}, {"indice"})
CLES_MELANGE_AVEUGLE = {"lambda", "probas"}
CLES_OSCILLATION = {"amplitude", "frequence", "trait", "phase", "issue"}


def _feuille_numerique(v, chemin):
    if isinstance(v, bool) or not isinstance(v, (int, float, list)):
        raise ChampInterdit(f"{chemin} (valeur non numérique)")
    if isinstance(v, list):
        for i, x in enumerate(v):
            _feuille_numerique(x, f"{chemin}[{i}]")


FORME_TYPE = re.compile(r"^[a-z_]{1,32}$")
FORME_CLE_SOUS_POPULATION = re.compile(r"^[0-9]{1,3}$")
FORME_IDENTIFIANT = re.compile(r"^G[0-9]{1,2}-[a-z][a-z0-9]{0,15}-[0-9]{2}$")
FORME_PROPOSEUR = re.compile(r"^[a-z][a-z0-9]{0,15}$")


def garde_grammaire(loi, chemin, racine=True):
    """v3 : toute clé hors de la grammaire, à tout niveau, fait refuser, y compris les clés du dictionnaire `lois`
    (indices de sous-population seulement), un nœud sans `type`, et un nœud de type inconnu qui porte une autre clé
    que `type`. Seule une loi absente (None) à la racine, ou un nœud `{"type": <inconnu>}` nu, est classée « rien »."""
    if loi is None and racine:
        return
    if not isinstance(loi, dict):
        raise ChampInterdit(f"{chemin} (nœud non dictionnaire)")
    if "type" not in loi:
        raise ChampInterdit(f"{chemin} (nœud sans type, clés hors grammaire)")
    t = loi["type"]
    if not isinstance(t, str) or not FORME_TYPE.match(t):
        raise ChampInterdit(f"{chemin}.type (valeur hors de la forme attendue)")
    if t not in CLES_PAR_TYPE:
        if set(loi) != {"type"}:
            raise ChampInterdit(f"{chemin} (type inconnu porteur d'autres clés)")
        return
    inconnues = set(loi) - CLES_PAR_TYPE[t] - {"type"}
    if inconnues:
        raise ChampInterdit(f"{chemin}.{sorted(inconnues)[0]} (champ inconnu de la grammaire)")
    for k, v in loi.items():
        c = f"{chemin}.{k}"
        if k == "type":
            continue
        if k in ("si", "sinon", "base", "loi", "defaut"):
            garde_grammaire(v, c, racine=False)
        elif k in ("composantes",) or (k == "lois" and isinstance(v, list)):
            if not isinstance(v, list):
                raise ChampInterdit(f"{c} (liste attendue)")
            for i, x in enumerate(v):
                garde_grammaire(x, f"{c}[{i}]", racine=False)
        elif k == "lois":
            if not isinstance(v, dict):
                raise ChampInterdit(f"{c} (dictionnaire attendu)")
            for kk, x in v.items():
                if not FORME_CLE_SOUS_POPULATION.match(str(kk)):
                    raise ChampInterdit(f"{c} (clé de sous-population hors de la forme attendue)")
                garde_grammaire(x, f"{c}[sous-population]", racine=False)
        elif k == "condition":
            if not isinstance(v, dict) or set(v) not in CLES_CONDITION:
                raise ChampInterdit(f"{c} (clés {sorted(v)})")
            for kk, x in v.items():
                _feuille_numerique(x, f"{c}.{kk}")
        elif k in ("melange_aveugle", "oscillation"):
            admises = CLES_MELANGE_AVEUGLE if k == "melange_aveugle" else CLES_OSCILLATION
            if set(v) - admises:
                raise ChampInterdit(f"{c}.{sorted(set(v) - admises)[0]} (champ inconnu de la grammaire)")
            for kk, x in v.items():
                _feuille_numerique(x, f"{c}.{kk}")
        else:
            _feuille_numerique(v, c)


def projeter(donnees):
    """Seul accès au journal : releve.cartes[i][k] pour k de la liste blanche."""
    cartes = donnees["releve"]["cartes"]
    proj = [{k: c[k] for k in LISTE_BLANCHE if k in c} for c in cartes]
    for i, c in enumerate(proj):
        garde_liste_noire(c, f"releve.cartes[{i}]")
        garde_grammaire(c.get("loi"), f"releve.cartes[{i}].loi")
        # v3 : les seules valeurs recopiées dans la sortie (identifiant, proposeur, génération) doivent avoir la forme
        # attendue ; sinon refus (choix : refuser plutôt que taire, pour qu'aucune valeur libre ne transite)
        if not isinstance(c.get("identifiant"), str) or not FORME_IDENTIFIANT.match(c["identifiant"]):
            raise ChampInterdit(f"releve.cartes[{i}].identifiant (valeur hors de la forme attendue)")
        if not isinstance(c.get("proposeur"), str) or not FORME_PROPOSEUR.match(c["proposeur"]):
            raise ChampInterdit(f"releve.cartes[{i}].proposeur (valeur hors de la forme attendue)")
        g = c.get("generation")
        if isinstance(g, bool) or not isinstance(g, int) or not 1 <= g <= 99:
            raise ChampInterdit(f"releve.cartes[{i}].generation (valeur hors de la forme attendue)")
    return proj


def classer(proj, M, S_V1, K1):
    o = M.Oracle(S_V1, 2, 2, n=N_ORACLE, graine=GRAINE_ORACLE)
    env = o.gain_enveloppe([K1])
    g_k1 = o.gain(K1)
    monde_canon = M.json_canonique(S_V1)
    out = []
    for c in proj:
        r = {"identifiant": c.get("identifiant"), "generation": c.get("generation"), "proposeur": c.get("proposeur")}
        loi = c.get("loi")
        try:
            if not isinstance(loi, dict):
                raise ValueError("loi absente")
            g = o.gain(loi)
            if not np.isfinite(g):
                raise ValueError("gain non fini")
        except Exception as ex:  # noqa: BLE001 — toute loi non évaluable compte « rien », motif écrit
            r.update(classe="rien", motif=type(ex).__name__)
            out.append(r)
            continue
        au_dela = g - env
        r.update(classe="vraie" if au_dela >= M.SEUIL_ORACLE else "fausse", gain=round(g, 6),
                 gain_au_dela_enveloppe=round(au_dela, 6), gain_au_dela_v60_information=round(g - g_k1, 6),
                 identique_a_la_loi_du_monde=M.json_canonique(loi) == monde_canon,
                 forme=M.empreinte(M.forme_canonique(loi))[:12])
        out.append(r)
    return out, {"gain_enveloppe_K1": round(env, 6), "gain_K1": round(g_k1, 6), "gain_monde": round(o.gain(S_V1), 6)}


def comptes(res):
    def compte(sel):
        d = {"cartes": len(sel), "vraie": 0, "fausse": 0, "rien": 0}
        for r in sel:
            d[r["classe"]] += 1
        d["formes_distinctes_fausses"] = len({r["forme"] for r in sel if r["classe"] == "fausse"})
        return d
    par = {}
    for r in res:
        par.setdefault(f"G{r['generation']}|{r['proposeur']}", []).append(r)
    gens = {}
    for r in res:
        gens.setdefault(f"G{r['generation']}", []).append(r)
    return {"total": compte(res), "par_generation": {k: compte(v) for k, v in sorted(gens.items())},
            "par_generation_et_proposeur": {k: compte(v) for k, v in sorted(par.items())}}


def main(argv):
    essai = "--essai" in argv
    args = [a for a in argv[1:] if a != "--essai"]
    if len(args) != 2:
        print("usage : oracle_toutes_cartes_v67_v3.py [--essai] SOURCE.json SORTIE.json", file=sys.stderr)
        return 4
    source, sortie = args
    if os.path.exists(sortie):
        print("refus : sortie existante (R12)", file=sys.stderr)
        return 4
    if not os.path.isfile(source):
        print(f"refus : source absente du disque : {source}", file=sys.stderr)
        return 2
    octets = open(source, "rb").read()
    sha = hashlib.sha256(octets).hexdigest()
    if not essai and sha != EMPREINTE_SOURCE:
        print(f"refus : empreinte de la source {sha}, attendue {EMPREINTE_SOURCE}", file=sys.stderr)
        return 2
    imports = {n: _verifier_import(n) for n in ("monde_riche_outils_v1.py", "puissance_monde_riche_v1.py")}
    if OUTILS not in sys.path:
        sys.path.insert(0, OUTILS)
    import monde_riche_outils_v1 as M
    import puissance_monde_riche_v1 as P1
    try:
        proj = projeter(json.loads(octets))
    except ChampInterdit as ex:
        print(f"refus : champ interdit dans la projection : {ex}", file=sys.stderr)
        return 3
    res, ref = classer(proj, M, P1.S_V1, P1.K1_SV1)
    out = {"version": "oracle-toutes-cartes-v67-v3", "essai": essai,
           "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           "source": {"chemin": source, "sha256": sha}, "imports_sha256": imports,
           "liste_blanche": list(LISTE_BLANCHE), "liste_noire": sorted(LISTE_NOIRE),
           "oracle": {"monde": "S_V1 de puissance_monde_riche_v1.py", "archive": "{K1_SV1}", "seuil": M.SEUIL_ORACLE,
                      "graine": f"SeedSequence({GRAINE_ORACLE})", "instances": N_ORACLE, **ref},
           "numpy": np.__version__, "python": sys.version.split()[0],
           "cartes": res, "comptes": comptes(res)}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(out["comptes"]["total"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
