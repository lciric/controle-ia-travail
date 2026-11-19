"""Essai d'intégration du contre-lecteur : une vraie livraison du code de la passe (modèle jouet) donnée à la garde de
réception de la lecture (r1 à r8), puis à la lecture mécanique. Rien n'est écrit dans le dépôt : tout va dans le dossier
de travail passé en argument. Les montages sont ceux des essais de la passe (importés), aux couches 7, 15 et 23 du texte
(la lecture les a en dur), sur un modèle jouet de 24 couches."""
from __future__ import annotations

import dataclasses
import hashlib
import importlib
import json
import sys
import time
import traceback
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
sys.path[:0] = [str(DEPOT / "src"), str(DEPOT / "tests")]

import numpy as np  # noqa: E402

from controle_ia import manifeste  # noqa: E402
from controle_ia.barreau8_moniteurs import lecture_sondes_v1 as L  # noqa: E402
from controle_ia.barreau8_moniteurs import passe_recalcul_v2 as P  # noqa: E402
from controle_ia.premier_test_ia.figees import ecrire_sondes  # noqa: E402
from controle_ia.scellement import empreinte, sceller  # noqa: E402
from controle_ia.sondes.familles import SondeLineaireJetons  # noqa: E402

TP = importlib.import_module("test_barreau8_moniteurs_passe_v2")

N_TACHES = int(sys.argv[2]) if len(sys.argv) > 2 else 10
TP.N_TACHES = N_TACHES
TP.COUCHES_JOUET = 4
MODELE_NEUF_4 = TP.modele_neuf
PLACES = {0: 0, 1: 7, 2: 15, 3: 23}


def modele_neuf_24(tok):
    """Modèle de 24 couches dont les couches 0, 7, 15, 23 portent les quatre couches ajustées du jouet ; les autres sont
    exactement l'identité sur le flux résiduel (projections de sortie de l'attention et du perceptron mises à zéro)."""
    petit = MODELE_NEUF_4(tok)
    grand = TP.modele_jouet(TP.GRAINE_MODELE, len(tok), couches=24, largeur=TP.LARGEUR, tetes=2, tetes_cle_valeur=1, intermediaire=64)
    etat = grand.state_dict()
    for k, v in petit.state_dict().items():
        if k.startswith("model.layers."):
            i = int(k.split(".")[2])
            etat[k.replace(f"model.layers.{i}.", f"model.layers.{PLACES[i]}.", 1)] = v.clone()
        else:
            etat[k] = v.clone()
    for i in range(24):
        if i not in PLACES.values():
            etat[f"model.layers.{i}.self_attn.o_proj.weight"].zero_()
            etat[f"model.layers.{i}.mlp.down_proj.weight"].zero_()
    grand.load_state_dict(etat)
    grand.generation_config.eos_token_id = [TP.EOS, TP.FIN]
    return grand.eval()
TP.LETTRES = "éèêàëâäçîïôöûùüÿœæÉÈÊÀÂÇÎÔÛ"[:N_TACHES]
BASE_MOTIFS = "a1b2c3d4e5z9y8x7w6v5kQlRmSnTpUH,I;J:K!L?mnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV0123456789"
TP.MOTIFS = tuple(TP.LETTRES[k] + (BASE_MOTIFS * 3)[11 * k:11 * k + 10] for k in range(N_TACHES))
TP.N_PLANCHER = int(sys.argv[5]) if len(sys.argv) > 5 else TP.N_PLANCHER
LARGEUR, N_PLANCHER = TP.LARGEUR, TP.N_PLANCHER


def lin(rng, nom, couche, famille="lineaire"):
    return SondeLineaireJetons(nom, couche, "max", rng.standard_normal(LARGEUR), float(rng.standard_normal()), None, famille)


def sondes_du_texte(rng):
    legeres = [lin(rng, "remplissage-lineaire-c15", 15), lin(rng, "tromperie-difference_moyennes-c15", 15, "difference_moyennes"),
               lin(rng, "tromperie-difference_moyennes-c7", 7, "difference_moyennes"),
               lin(rng, "tromperie-difference_moyennes-c23", 23, "difference_moyennes"),
               lin(rng, "enjeux-lineaire-c15", 15), lin(rng, "enjeux-lineaire-c7", 7), lin(rng, "enjeux-lineaire-c23", 23)]
    neuves = [lin(rng, "dissimulation-lineaire-c7", 7), lin(rng, "dissimulation-lineaire-c23", 23),
              lin(rng, "dissimulation-lineaire-c15", 15)]
    neuves += [lin(rng, f"dissimulation-lineaire-c15-plancher-{k}", 15, "plancher") for k in range(N_PLANCHER)]
    planchers = [lin(rng, f"{n}-c15-t07-plancher-{k}", 15, "plancher") for n in ("tromperie-difference_moyennes", "enjeux-lineaire")
                 for k in range(N_PLANCHER)]
    return {"legeres": legeres, "neuves": neuves, "planchers": planchers}


def sha_vecteur(s):
    return hashlib.sha256(np.ascontiguousarray(s.w, dtype=np.float64).tobytes()).hexdigest()


def spec_du_monde(sondes, empreintes_sondes, empreinte_taches, sha_config):
    leg, neu = sondes["legeres"], sondes["neuves"]
    return dataclasses.replace(
        P.SPECIFICATION_TEXTE, nom="jouet", modele="jouet", revision="jouet-0", n_couches=24, largeur=LARGEUR,
        fins=(TP.EOS, TP.FIN), premier_jeton_cloture=TP.FIN, jeton_debut=1, type_poids="float32",
        empreintes_fichiers_modele=(("tokenizer_config.json", sha_config),), max_jetons_action=TP.MAX_JETONS,
        n_taches=N_TACHES, pas_par_episode=TP.PAS, lot=4, couches=(7, 15, 23), couche_decisive=15,
        pas_sous_echantillon_decisif=2, pas_sous_echantillon_descriptif=8,
        sondes_decisives=(
            P.SondeDecisive(leg[1].nom, "legeres", 1, sha_vecteur(leg[1]), leg[1].empreinte(), "planchers",
                            "tromperie-difference_moyennes-c15-t07-plancher-"),
            P.SondeDecisive(leg[4].nom, "legeres", 4, sha_vecteur(leg[4]), leg[4].empreinte(), "planchers",
                            "enjeux-lineaire-c15-t07-plancher-"),
            P.SondeDecisive(neu[2].nom, "neuves", 2, sha_vecteur(neu[2]), neu[2].empreinte(), "neuves", None)),
        sondes_descriptives=tuple(P.SondeDescriptive(n, f, c) for n, f, c in (
            ("dissimulation-lineaire-c7", "neuves", 7), ("dissimulation-lineaire-c23", "neuves", 23),
            ("tromperie-difference_moyennes-c7", "legeres", 7), ("tromperie-difference_moyennes-c23", "legeres", 23),
            ("enjeux-lineaire-c7", "legeres", 7), ("enjeux-lineaire-c23", "legeres", 23))),
        n_plancher=N_PLANCHER, empreintes_fichiers_sondes=tuple(sorted(empreintes_sondes.items())),
        empreinte_taches=empreinte_taches, taille_morceau=30_000)


def identites_de_la_lecture(sondes, sha):
    def ident(nom, role, role_p, prefixe):
        k = [s.nom for s in sondes[role]].index(nom)
        s = sondes[role][k]
        return L.IdentiteSonde(nom, role, f"s{k}_w", hashlib.sha256(np.ascontiguousarray(s.w).tobytes()).hexdigest(),
                               s.empreinte(), role_p, prefixe)
    return L.Identites(fichiers=dict(sha), sondes=(
        ident("tromperie-difference_moyennes-c15", "legeres", "planchers", "tromperie-difference_moyennes-c15-t07"),
        ident("enjeux-lineaire-c15", "legeres", "planchers", "enjeux-lineaire-c15-t07"),
        ident("dissimulation-lineaire-c15", "neuves", "neuves", None)), couches_7_23=dict(L.IDENTITES_DU_TEXTE.couches_7_23))


def journal(*x):
    print(time.strftime("%H:%M:%S"), *x, flush=True)


def main():
    base = Path(sys.argv[1])
    base.mkdir(parents=True, exist_ok=False)
    racine, hors = base / "depot", base / "hors-depot"
    racine.mkdir()
    hors.mkdir()
    (hors / "tokenizer_config.json").write_text(json.dumps({"clean_up_tokenization_spaces": True}), encoding="utf-8")
    rng = np.random.default_rng(np.random.SeedSequence(7))
    taches = [{"identifiant": f"tache-{k:02d}", "questions": TP.LETTRES[k] * int(sys.argv[4] if len(sys.argv) > 4 else 400)} for k in range(N_TACHES)]
    chemin_taches = racine / "donnees" / "taches" / "taches-evaluation.json"
    TP.ecrire_scelle(chemin_taches, json.dumps({"taches": taches}))
    sondes = sondes_du_texte(rng)
    chemins, sha = {"taches": chemin_taches}, {}
    for role, liste in sondes.items():
        chemins[role] = racine / "donnees" / "sondes" / f"{role}.npz"
        sha[role] = ecrire_sondes(chemins[role], liste, {"principales": {}})
    tok = TP.jetoniseur_jouet()
    journal("ajustement du modèle jouet (24 couches)")
    TP.ajuster_modele(tok, taches, pas_d_ajustement=int(sys.argv[3]) if len(sys.argv) > 3 else 200)
    TP.modele_neuf = modele_neuf_24
    modele = TP.modele_neuf(tok)
    TP.injecter(modele, 16, 32.0, 0)
    etats_ad = {"eleve": TP.etat_aleatoire(modele, 1), "temoin-jumeau": TP.etat_aleatoire(modele, 2)}
    dep_ad = base / "adaptateurs"
    dep_ad.mkdir()
    for nom, e in etats_ad.items():
        TP.torch.save(e, dep_ad / f"adaptateur-{nom}.pt")
    journal("tirage des actions jouets")
    actions = TP.tirer_actions(tok, taches, etats_ad, 11, vides=True)
    chemins.update(TP.ecrire_course(racine, "course", *actions, dep_ad))
    chemins["texte"] = racine / "prereg" / "texte-jouet-v1.md"
    TP.ecrire_scelle(chemins["texte"], TP.TEXTE_PREREG)
    TP.ecrire_scelle(racine / "docs" / "rapport-conformite-v1.md", "Rapport de conformité jouet.\n")
    TP.ecrire_scelle(racine / "docs" / "notice-v1.md", "Notice jouet.\n")
    sha_devis = TP.ecrire_scelle(racine / "docs" / "devis-passe-v1.md", "Devis jouet.\n")
    chemins["accords"] = racine / "registres" / "go.md"
    chemins["accords"].parent.mkdir(parents=True)
    chemins["accords"].write_text(f"| GO-2026-11-19-01 | passe de recalcul | devis {sha_devis} |\n", encoding="utf-8")
    TP.git(racine, "init", "-q")
    TP.git(racine, "add", "-A")
    TP.git(racine, "commit", "-q", "-m", "monde jouet")
    chemins["registre"] = TP.ecrire_code(racine, "sain")
    spec = spec_du_monde(sondes, sha, empreinte(chemin_taches), empreinte(hors / "tokenizer_config.json"))
    params = P.ParametresPasse(
        racine=racine, sortie=racine / "livraisons" / "sortie-1", run_id="20261119-000001-passe-jouet", entropie=12345,
        extrait=chemins["extrait"], taches=chemins["taches"], sondes_legeres=chemins["legeres"], sondes_neuves=chemins["neuves"],
        planchers=chemins["planchers"], registre=chemins["registre"], registre_accords=chemins["accords"], duree_max_heures=3.0,
        depense_max_usd=10.0, prix_horaire_usd=3.0, debut_location=time.time() - 60.0, identifiant_instance="instance-jouet-1",
        appareil="cpu", autoriser_depot_sale=True)
    journal("passe de recalcul (code de la passe v2)")
    r = P.executer_passe(params, spec, TP.ChargeurJouet(hors))
    bordereau, sha_b = Path(r["bordereau"]), r["bordereau_sha256"]
    journal("livraison :", bordereau, sha_b, "taille", r["taille_totale"])
    journal("fichiers livrés :", sorted(p.name for p in bordereau.parent.iterdir()))
    t = L.Tailles(n_taches=N_TACHES, n_pas=TP.PAS, largeur=LARGEUR, n_plancher=N_PLANCHER, max_jetons=TP.MAX_JETONS, pas_c15=2,
                  pas_c7_c23=8, n_tirages=400, n_permutations=60, taille_max=2_000_000_000, taille_morceau=30_000)
    cadre = L.Cadre(tailles=t, identites=identites_de_la_lecture(sondes, sha), recette=L.Recette(),
                    modele={"nom": "jouet", "revision": "jouet-0"})
    code_passe = json.loads((racine / "registres" / "bordereau-code-sain.json").read_text(encoding="utf-8"))
    modules_passe = {n: m["sha256"] for n, m in code_passe["modules"].items()}
    chemins_sondes = {"legeres": chemins["legeres"], "planchers": chemins["planchers"], "neuves": chemins["neuves"]}
    resultats = {}
    # (A) lecture du bordereau du code de la passe par la fonction de la lecture
    lignes_registre = P.lire_registre_propre(Path(chemins["registre"]).read_text(encoding="utf-8"))
    try:
        L.modules_de_la_passe(racine, {"chemin": lignes_registre["CODE-PASSE-IIB"]["chemin"]})
        resultats["modules_de_la_passe"] = "accepté"
    except Exception as e:  # noqa: BLE001 — l'essai rapporte le refus exact
        resultats["modules_de_la_passe"] = f"{type(e).__name__}: {e}"
    journal("modules_de_la_passe sur le bordereau du code de la passe :", resultats["modules_de_la_passe"][:400])
    # (B) garde de réception r1 à r8
    try:
        d = L.garde_de_reception(bordereau, sha_b, modules_passe, chemins_sondes, cadre)
        resultats["reception"] = "TENUE"
        journal("GARDE DE RÉCEPTION TENUE : sondes lues", d.sondes_lues, "; 7/23", d.sondes_7_23)
        journal("contrôles r6/r7 :", d.repere_de_couche.get("controles"))
    except Exception as e:  # noqa: BLE001
        resultats["reception"] = f"{type(e).__name__}: {e}"
        journal("RÉCEPTION REFUSÉE :", resultats["reception"])
        traceback.print_exc()
        print(json.dumps(resultats, ensure_ascii=False, indent=1))
        return
    # (C) lecture mécanique
    extrait = {"avertissement": L.AVERTISSEMENT_EXTRAIT, "run_id": "20261119-010203-course-jouet",
               "lecture_dommage": {"phrase": L.DOMMAGE_VU},
               "lecture_diffusion": {"par_paire": {
                   "B100-H": {"cout": "réussit", "traits": "échoue", "mots_et_cout": "échoue", "unite": "échoue"},
                   "B50-H": {"cout": "réussit", "traits": "échoue", "mots_et_cout": "échoue", "unite": "échoue"},
                   "TJ100-H": {"cout": "réussit", "traits": "réussit", "mots_et_cout": "réussit", "unite": "réussit"},
                   "B100-TJ100": {"mots_et_cout": "échoue"}}, "phrase": None}}
    p = base / "etats" / "etats-lectures-iib-v1.json"
    p.parent.mkdir()
    p.write_text(json.dumps(extrait, ensure_ascii=False), encoding="utf-8")
    etats = L.verifier_extrait_etats(p, sceller(p))
    graines = manifeste.graines(L.cles_de_graines(d.sondes_lues, d.sondes_7_23), 123456789)
    try:
        sortie = L.calculer_lecture(d, etats, graines, cadre, {"par_fraction": {}})
        resultats["lecture"] = {"lignes": [l["ligne"] for l in sortie["lignes_declenchees"]],
                                "etats": sortie["etats"], "a0_echec": (sortie["essai_de_la_chaine"] or {}).get("echec"),
                                "a0_motifs": (sortie["essai_de_la_chaine"] or {}).get("motifs"),
                                "declencheurs": sortie["declencheurs_de_l_audit"]}
        (base / "sortie-lecture.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        resultats["lecture"] = f"{type(e).__name__}: {e}"
        traceback.print_exc()
    print(json.dumps(resultats, ensure_ascii=False, indent=1, default=str))


if __name__ == "__main__":
    main()
