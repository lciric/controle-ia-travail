"""L'invocation unique du § 9 du préenregistrement scellé (e821e875…). ÉCRITE, NON LANCÉE.

Elle enchaîne, en un seul processus :
  (1) les méthodes N et b sur 200 mondes de validation de M_bien et de M_moyen (RACINE_VALIDATION, indices 300 à 499) ;
      la console ne reçoit que σ̂ de Δ(N, b), le drapeau de S9 et n' ; les moyennes de Δ(N, b) en validation et la grille
      diagnostique (200 mondes « moyen » ; 5 e × 4 β ; seuls les écarts à la case (e = 8, β = 1)) sont tenues en mémoire ;
  (2) l'écriture et le scellement du manifeste (σ̂ de chaque condition, n', racines, configuration, empreintes du code,
      versions, commit) ; puis, seulement alors, l'écriture du fichier scellé de validation (moyennes et grille) ;
  (3) les mondes de décision d'indices 0 à n' − 1 de chaque condition (RACINE), sans reprise ni extension ; un fichier
      scellé de résultats par condition, rattaché au manifeste par son empreinte et horodaté après lui ; puis les
      contrastes du § 7 (fichier scellé), les données de l'audit, et rien d'autre : aucun verdict (R13).

Aucune moyenne de Δ(N, ·) n'est imprimée. Les prérequis (préenregistrement scellé, addendum d'écarts scellé, balayage
statique, validation du générateur passée, reproduction des témoins passée, code de contraste de la non-régression fixé) sont vérifiés AVANT le
premier monde ; le moindre manque arrête l'invocation avant tout calcul.
"""
import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from controle_ia import manifeste as man
from controle_ia import prereg as pre
from controle_ia.gardes import GardeArret, exiger_numpy_minimal
from controle_ia.scellement import verifier

import analyse_v2 as an
import balayage_v2 as ba
import bras_v2 as br
import graines_v2 as gr
import mesures_v2 as ms
import monde_v2 as mo
import travail_v2 as tr

ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[5]
PREREG = DEPOT / "prereg" / "preenregistrement-bisociation-deux-espaces-v2.md"
EMPREINTE_PREREG = "e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea"
# Addendum d'écarts déclarés (Q-01 (b), Q-03 = 16, Q-04 copie ; R-600) : il doit être scellé avant l'invocation. Nom et
# empreinte du texte final (addendum v4, point (vii), ordre de gel, CLA-04) : si le texte change, les deux changent avec lui.
ADDENDUM = "addendum-ecarts-bisociation-deux-espaces-v2-v6.md"
EMPREINTE_ADDENDUM = "37f6df2e0f3653088643b4eb1883c2a5b083111227edd3c53a0e411cd187774f"

CONDITIONS = [c for c, _ in sorted(gr.CODES_CONDITION.items(), key=lambda kv: kv[1])]
# S15 et S7 (valeurs gelées par Lazar, R-580)
N_GELES = {"M_bien": 2400, "M_moyen": 2400, "M_inertes": 2400, "SP": 600, "INV": 600, "V_fuite": 600, "NR_bien": 1200,
           "NR_moyen": 1200, "M_mal": 600, "V_concepts_absents": 600, "V_moyeu_conceptuel": 600, "V_surface": 600,
           "M_couplage_faible": 600, "M_palettes_communes": 600, "M_palettes_disjointes": 600, "M_fonds_1ou2": 600}
INDICES_ETAPE1 = range(300, 500)       # § 7, § 9 : disjoints de ceux de V1 à V9 (0 à 299)
GRILLE_E, GRILLE_BETA = (1, 2, 4, 8, 16), (0.5, 1, 2, 4)  # § 5
CASE_REFERENCE = (8, 1)


def _maintenant():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# --- prérequis (avant tout calcul) --------------------------------------------------------------------------

def verifier_prerequis(depot, validation, reproduction, audit_rendu, code_contraste_nr):
    exiger_numpy_minimal()
    sha = pre.exiger_prereg_scelle(Path(depot) / "prereg" / PREREG.name)
    if sha != EMPREINTE_PREREG:
        raise GardeArret(f"préenregistrement {sha[:12]}… ≠ {EMPREINTE_PREREG[:12]}…")
    sha_addendum = exiger_addendum_scelle(depot)
    ba.exiger_propre([ICI / m for m in ba.MODULES_BRAS])
    if code_contraste_nr is None:
        raise GardeArret("code de contraste de la non-régression non fixé : Q-03 de ecarts-et-questions-v1.md")
    import json
    verifier(validation)
    v = json.loads(Path(validation).read_text(encoding="utf-8"))
    r = v["resultat"] if "resultat" in v else v
    if not all(r["seuils"].values()):
        raise GardeArret(f"validation du générateur non passée : {[k for k, x in r['seuils'].items() if not x]}")
    if r.get("V9_J_vraie"):
        if audit_rendu is None:
            raise GardeArret("V9 : J vraie sur les miroirs ; l'audit doit être rendu et scellé avant l'invocation (§ 9)")
        verifier(audit_rendu)
    verifier(reproduction)
    rep = json.loads(Path(reproduction).read_text(encoding="utf-8"))
    rr = rep["resultat"] if "resultat" in rep else rep
    if not rr.get("reproduction_passee"):
        raise GardeArret("reproduction des témoins de v1 non passée : le code des témoins diffère de v1")
    return {"prereg_sha256": sha, "addendum_sha256": sha_addendum, "validation_sha256": ms_sha(validation), "reproduction_sha256": ms_sha(reproduction),
            "audit_rendu_sha256": ms_sha(audit_rendu) if audit_rendu else None}


def exiger_addendum_scelle(depot):
    """L'addendum d'écarts (R-600) est scellé : son empreinte compagnon existe et concorde, et l'empreinte du fichier
    égale EMPREINTE_ADDENDUM, celle du texte final contre-lu (CLA-04, même logique que EMPREINTE_PREREG) ; sinon arrêt."""
    from controle_ia.scellement import compagnon
    chemin = Path(depot) / "prereg" / ADDENDUM
    if not chemin.is_file() or not compagnon(chemin).is_file():
        raise GardeArret(f"addendum {ADDENDUM} non scellé : ni validation ni invocation (R1)")
    sha = verifier(chemin)
    if sha != EMPREINTE_ADDENDUM:
        raise GardeArret(f"addendum {sha[:12]}… ≠ {EMPREINTE_ADDENDUM[:12]}… : texte autre que celui fixé dans le code")
    return sha


def ms_sha(chemin):
    from controle_ia.scellement import empreinte
    return empreinte(chemin)


# --- étape (1) : validation des méthodes, σ̂, n', grille ---------------------------------------------------

def etape1(processus, rapport=None, executer=tr.executer_condition):
    """Rend (s9, secret). `s9[cond] = {n, sigma_chapeau, n_prime, plafond}` ; `secret` : moyennes de Δ(N, b) en
    validation et écarts de la grille, destinés au fichier scellé (jamais imprimés)."""
    s9, secret = {}, {"moyenne_delta_N_b_validation": {}, "grille_ecarts_a_e8_beta1": None}
    for cond in ("M_bien", "M_moyen"):
        lignes = executer(cond, gr.RACINE_VALIDATION, INDICES_ETAPE1, bras=["N", "b"], processus=processus, rapport=rapport)
        d = an.deltas(lignes, "N", "b")
        pts = [100.0 * v for v in d.values()]
        sigma = ms.sigma_chapeau(pts)
        n_prime, plafond = ms.extension_s9(N_GELES[cond], sigma)
        s9[cond] = {"n": N_GELES[cond], "sigma_chapeau": sigma, "n_prime": n_prime, "plafond": plafond}
        secret["moyenne_delta_N_b_validation"][cond] = float(np.mean(pts)) / 100.0
        if cond == "M_moyen":
            secret["grille_ecarts_a_e8_beta1"] = grille(processus, executer)
    return s9, secret


def grille(processus, executer):
    """Grille diagnostique (§ 5) sur les 200 mondes de validation « moyen » : écart moyen de chaque case à (8, 1)."""
    moyennes = {}
    for e in GRILLE_E:
        for beta in GRILLE_BETA:
            lignes = executer("M_moyen", gr.RACINE_VALIDATION, INDICES_ETAPE1, bras=["N_grille"], processus=processus,
                              aux_extra={"grille_e_beta": (e, beta)})
            moyennes[(e, beta)] = float(np.mean([l["bras"]["N_grille"]["precision"] for l in lignes if not l["exclu"]]))
    ref = moyennes[CASE_REFERENCE]
    return {f"e={e};beta={beta}": moyennes[(e, beta)] - ref for (e, beta) in moyennes}


# --- étape (3) --------------------------------------------------------------------------------------------

def reduire(lignes):
    """Ce qui sert aux contrastes (mémoire) : indice, exclusion, nombre de champs, précisions."""
    return [{"indice": l["indice"], "exclu": l["exclu"], "n_champs": l["n_champs"],
             "bras": {b: {"precision": m["precision"], "precision_placebo": m["precision_placebo"]}
                      for b, m in (l.get("bras") or {}).items()}} for l in lignes]


def identites_paires(lignes):
    """Paires de bras dont les sorties sont identiques au bit près (égalité des listes ordonnées `_paires`) sur tous les
    mondes non exclus de la condition ; mondes exclus ignorés. Toutes les paires parmi N et tous les bras présents
    (CLA-03 ; addendum v4, (vi-b)). Chaque paire est un tuple (x, y) rangé dans l'ordre de br.ORDRE_BRAS (N d'abord) ;
    liste triée. Le filtre de la liste du texte et des identités déclarées d'avance est dans lecture_v2.identites_audit.
    Un bras absent d'un monde non exclu (non applicable) ne forme de paire avec aucun autre."""
    ident = None
    for l in lignes:
        if l["exclu"]:
            continue
        bras = sorted(l["bras"], key=lambda b: (br.RANG.get(b, len(br.RANG)), b))
        egaux = {(x, y) for k, x in enumerate(bras) for y in bras[k + 1:]
                 if l["bras"][x]["_paires"] == l["bras"][y]["_paires"]}
        ident = egaux if ident is None else ident & egaux
    return sorted(ident or [], key=lambda p: (br.RANG.get(p[0], len(br.RANG)), br.RANG.get(p[1], len(br.RANG)), p))


def identites_a_N(lignes):
    """Bras identiques à N (déduits de identites_paires ; gardé pour le rapport)."""
    return [y if x == "N" else x for x, y in identites_paires(lignes) if "N" in (x, y)]


def executer_decision(depot, run_id, manifeste_chemin, s9, processus, rapport, executer=tr.executer_condition,
                      ecrire_resultat=man.ecrire_resultat, code_contraste_nr=None, attendus_code=None):
    reduit, fichiers, comptes, identites, audit, lignes_bien = {}, [], {}, {}, {}, None
    n_prime = {c: (s9["M_bien"]["n_prime"] if c == "M_inertes" else s9[c]["n_prime"] if c in s9 else N_GELES[c])
               for c in CONDITIONS}
    for cond in CONDITIONS:
        ms.verifier_empreintes_code(attendus_code)
        n = n_prime[cond]
        lignes = executer(cond, gr.RACINE, range(n), processus=processus, rapport=rapport)
        ms.verifier_nombre_de_mondes(cond, len(lignes), n)
        # liste d'arrêt (contre-lecture du code) : latents de M_inertes égaux bit à bit à ceux de M_bien, monde par monde
        if cond == "M_bien":
            lignes_bien = [{"indice": l["indice"], "empreinte_latents": l["empreinte_latents"]} for l in lignes]
        if cond == "M_inertes":
            if lignes_bien is None:
                raise GardeArret("M_inertes exécutée avant M_bien : comparaison des latents impossible")
            ms.verifier_inertes_lignes(lignes_bien, lignes)
        taux = ms.verifier_taux(lignes, cond, decision=cond in an.CONDITIONS_DECISION)
        info = {"taux": taux}
        if cond in ("M_bien", "M_moyen", "M_mal"):
            ok = [l["bras"]["oracle"]["precision"] for l in lignes if not l["exclu"]]
            plafond = float(np.mean(ok))
            if cond == "M_mal":
                info["abandonnee_plafond_sous_S8"] = plafond < ms.PLAFOND_ORACLE_S8
            else:
                ms.verifier_plafond_oracle(plafond, cond)
        ident = identites_paires(lignes)
        identites[cond] = ident
        contenu = {"condition": cond, "n_mondes": len(lignes), "ecrit_le": _maintenant(), "info": info,
                   "identites_paires": [list(p) for p in ident],
                   "identites_a_N": [y if x == "N" else x for x, y in ident if "N" in (x, y)], "lignes": lignes}
        fichiers.append(str(ecrire_resultat(depot, manifeste_chemin, f"resultats-{cond}", contenu)))
        comptes[cond] = len(lignes)
        reduit[cond] = reduire(lignes)
        audit[cond] = {"precision_N": float(np.mean([l["bras"]["N"]["precision"] for l in lignes if not l["exclu"]])),
                       "precision_oracle": float(np.mean([l["bras"]["oracle"]["precision"] for l in lignes if not l["exclu"]])),
                       "concordance_verite": ms.concordance_verite(lignes)}
        if cond in ("NR_bien", "NR_moyen"):
            # liste d'arrêt : reproduction des témoins de v1 (marge S12) ; le résultat est déjà écrit et scellé
            moyennes = {b: float(np.mean([l["bras"][b]["precision"] for l in lignes if not l["exclu"]]))
                        for b in ("b", "a", "c", "d1")}
            ms.verifier_reproduction(cond, moyennes)
    contrastes = an.calculer_tout(reduit, gr.RACINE, code_contraste_nr)
    fichiers.append(str(ecrire_resultat(depot, manifeste_chemin, "contrastes",
                                        {"ecrit_le": _maintenant(), "contrastes": contrastes})))
    fichiers.append(str(ecrire_resultat(depot, manifeste_chemin, "donnees-audit",
                                        {"ecrit_le": _maintenant(), "par_condition": audit,
                                         "identites_paires": {c: [list(p) for p in v] for c, v in identites.items()},
                                         "concordance_verite_conditions_decision": {
                                             c: audit[c]["concordance_verite"] for c in an.CONDITIONS_DECISION
                                             if c in audit and not c.startswith("NR_")}})))
    return fichiers, comptes


def invocation(depot, run_id, processus, validation, reproduction, audit_rendu=None, *, rapport=None,
               etape1_fn=etape1, executer=tr.executer_condition, creer_manifeste=man.creer_manifeste,
               ecrire_resultat=man.ecrire_resultat, code_contraste_nr=None, verifier_prerequis_fn=verifier_prerequis):
    code_contraste_nr = an.CODE_CONTRASTE_NR if code_contraste_nr is None else code_contraste_nr
    prerequis = verifier_prerequis_fn(depot, validation, reproduction, audit_rendu, code_contraste_nr)
    ms.verifier_racine(gr.RACINE, decision=True)
    # (1)
    s9, secret = etape1_fn(processus, rapport, executer=executer)
    for cond, i in s9.items():
        print(f"{cond} : sigma_chapeau = {i['sigma_chapeau']:.3f} points ; extension S9 = "
              f"{'oui' if i['n_prime'] > i['n'] else 'non'} ; n' = {i['n_prime']}" + (" (plafond)" if i["plafond"] else ""))
    # (2) manifeste, scellé avant le premier monde de décision
    n_prime = {c: (s9["M_bien"]["n_prime"] if c == "M_inertes" else s9[c]["n_prime"] if c in s9 else N_GELES[c])
               for c in CONDITIONS}
    empreintes = ms.empreintes_code()
    config = {"programme": "bisociation-deux-espaces-v2", "racine": gr.RACINE, "racine_validation": gr.RACINE_VALIDATION,
              "codes_condition": gr.CODES_CONDITION, "ordre_conditions": CONDITIONS, "bras": br.ORDRE_BRAS,
              "s9": {c: {"n": i["n"], "sigma_chapeau": i["sigma_chapeau"], "n_prime": i["n_prime"]} for c, i in s9.items()},
              "nombres_de_mondes": n_prime, "empreintes_code": empreintes, "prerequis": prerequis,
              "derivation_des_graines": "SeedSequence(entropy=racine, spawn_key=(code_condition, indice_monde, code_role)[, tentative]) ; "
                                        "replantation r >= 1 (addendum v2, Q-01 (b)) : (code_condition, indice_monde, 0, tentative, r)",
              "max_replantations": mo.MAX_REPLANTATIONS, "addendum": ADDENDUM,
              "processus": processus}
    chemin, manifeste = creer_manifeste(depot, run_id, config, [], entropie=gr.RACINE, decisif=True,
                                        prereg=Path(depot) / "prereg" / PREREG.name,
                                        commande="python3 -B invocation_unique_v2.py " + " ".join(sys.argv[1:]))
    ecrire_resultat(depot, chemin, "validation-etape1", {"ecrit_le": _maintenant(), **secret})
    # (3)
    fichiers, comptes = executer_decision(depot, run_id, chemin, s9, processus, rapport, executer, ecrire_resultat,
                                          code_contraste_nr, empreintes)
    ms.verifier_empreintes_code(empreintes)
    return {"manifeste": str(chemin), "fichiers": fichiers, "comptes": comptes}


def _progres(cond, k, n):
    print(f"  {cond} : {k}/{n}", flush=True)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--depot", default=str(DEPOT))
    ap.add_argument("--run-id", required=True, help="AAAAMMJJ-HHMMSS-nom, ex. 20261101-120000-bisociation-v2")
    ap.add_argument("--processus", type=int, default=2)
    ap.add_argument("--validation", required=True, help="fichier scellé des résultats de validation du générateur")
    ap.add_argument("--reproduction", required=True, help="fichier scellé de la reproduction des témoins de v1")
    ap.add_argument("--audit-rendu", default=None, help="rapport d'audit scellé, exigé si V9 est vraie")
    a = ap.parse_args(argv)
    try:
        res = invocation(a.depot, a.run_id, a.processus, a.validation, a.reproduction, a.audit_rendu, rapport=_progres)
    except GardeArret as e:
        print(f"ARRET : {e}", file=sys.stderr)
        return 2
    print("terminé :", res["manifeste"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
