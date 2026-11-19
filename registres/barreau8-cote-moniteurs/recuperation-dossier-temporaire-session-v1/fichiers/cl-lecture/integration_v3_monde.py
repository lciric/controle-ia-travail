"""Essai d'intégration, versions courantes (passe v4, lecture v3) — étape 1 : monde jouet et vraie livraison de la passe.

Le dépôt d'essai porte une copie du code du paquet (`src/controle_ia`, sans le paquet interdit ni les caches), et c'est cette
copie que l'on charge : les chemins des modules sont alors relatifs au dépôt d'essai, comme au vrai dépôt. Le modèle jouet de
la passe est ajusté à 4 couches (montages des essais de la passe v4) puis plongé dans un modèle de 24 couches (couches 0, 7, 15,
23 ajustées ; les 20 autres laissent le flux résiduel inchangé). Arguments : dossier de travail, nombre de tâches, pas
d'ajustement."""
from __future__ import annotations

import dataclasses
import hashlib
import importlib
import json
import shutil
import sys
import time
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
base = Path(sys.argv[1])
N_TACHES = int(sys.argv[2])
PAS_AJUSTEMENT = int(sys.argv[3])
base.mkdir(parents=True, exist_ok=False)
racine, hors = base / "depot", base / "hors-depot"
racine.mkdir()
hors.mkdir()
shutil.copytree(DEPOT / "src" / "controle_ia", racine / "src" / "controle_ia",
                ignore=shutil.ignore_patterns("__pycache__", "iib"))
shutil.copytree(DEPOT / "docs" / "sources" / "invites-2606.08892-v1", racine / "docs" / "sources" / "invites-2606.08892-v1")
(racine / ".gitignore").write_text("__pycache__/\n", encoding="utf-8")
sys.path[:0] = [str(racine / "src"), str(DEPOT / "tests")]

import numpy as np  # noqa: E402

from controle_ia.barreau8_moniteurs import passe_recalcul_v4 as P  # noqa: E402
from controle_ia.premier_test_ia.figees import ecrire_sondes  # noqa: E402
from controle_ia.scellement import empreinte, sceller  # noqa: E402
from controle_ia.sondes.familles import SondeLineaireJetons  # noqa: E402

TP = importlib.import_module("test_barreau8_moniteurs_passe_v4")
assert Path(P.__file__).resolve().is_relative_to(racine.resolve()), P.__file__

TP.N_TACHES = N_TACHES
TP.COUCHES_JOUET = 4
TP.LETTRES = "éèêàëâäçîïôöûùüÿœæÉÈÊÀÂÇÎÔÛ"[:N_TACHES]
SIGNES = "abcdefghijklmnopqrstuvw"                      # 23 signes : pas k + 1 < 23, parcours distincts
TP.MOTIFS = tuple("".join(SIGNES[(i * (k + 1)) % 23] for i in range(11)) for k in range(N_TACHES))
LARGEUR, N_PLANCHER = TP.LARGEUR, TP.N_PLANCHER
MODELE_NEUF_4 = TP.modele_neuf
PLACES = {0: 0, 1: 7, 2: 15, 3: 23}
ENTROPIE_TEXTE = 123456789012345678901234567890


def modele_neuf_24(tok):
    petit = MODELE_NEUF_4(tok)
    grand = TP.modele_jouet(TP.GRAINE_MODELE, len(tok), couches=24, largeur=LARGEUR, tetes=2, tetes_cle_valeur=1, intermediaire=64)
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


def lin(rng, nom, couche, famille="lineaire"):
    return SondeLineaireJetons(nom, couche, "max", rng.standard_normal(LARGEUR), float(rng.standard_normal()), None, famille)


def journal(*x):
    print(time.strftime("%H:%M:%S"), *x, flush=True)


rng = np.random.default_rng(np.random.SeedSequence(7))
(hors / "tokenizer_config.json").write_text(json.dumps({"clean_up_tokenization_spaces": True}), encoding="utf-8")
taches = [{"identifiant": f"tache-{k:02d}", "questions": TP.LETTRES[k] * 60} for k in range(N_TACHES)]
chemin_taches = racine / "donnees" / "taches" / "taches-evaluation.json"
TP.ecrire_scelle(chemin_taches, json.dumps({"taches": taches}))
legeres = [lin(rng, "remplissage-lineaire-c15", 15), lin(rng, "tromperie-difference_moyennes-c15", 15, "difference_moyennes"),
           lin(rng, "tromperie-difference_moyennes-c7", 7, "difference_moyennes"),
           lin(rng, "tromperie-difference_moyennes-c23", 23, "difference_moyennes"),
           lin(rng, "enjeux-lineaire-c15", 15), lin(rng, "enjeux-lineaire-c7", 7), lin(rng, "enjeux-lineaire-c23", 23)]
neuves = [lin(rng, "dissimulation-lineaire-c7", 7), lin(rng, "dissimulation-lineaire-c23", 23), lin(rng, "dissimulation-lineaire-c15", 15)]
neuves += [lin(rng, f"dissimulation-lineaire-c15-plancher-{k}", 15, "plancher") for k in range(N_PLANCHER)]
# planchers rangés dans un AUTRE ordre que celui des numéros (règle commune : recherche par nom)
planchers = [lin(rng, f"{n}-c15-t07-plancher-{k}", 15, "plancher") for k in reversed(range(N_PLANCHER))
             for n in ("tromperie-difference_moyennes", "enjeux-lineaire")]
sondes = {"legeres": legeres, "neuves": neuves, "planchers": planchers}
chemins, sha = {"taches": chemin_taches}, {}
for role, liste in sondes.items():
    chemins[role] = racine / "donnees" / "sondes" / f"{role}.npz"
    sha[role] = ecrire_sondes(chemins[role], liste, {"principales": {}})


def sha_vecteur(s):
    return hashlib.sha256(np.ascontiguousarray(s.w, dtype=np.float64).tobytes()).hexdigest()


tok = TP.jetoniseur_jouet()
journal("ajustement du modèle jouet (4 couches), puis plongement dans 24")
TP.ajuster_modele(tok, taches, pas_d_ajustement=PAS_AJUSTEMENT)
TP.modele_neuf = modele_neuf_24
modele = TP.modele_neuf(tok)
TP.injecter(modele, 16, 32.0, 0)
FACTEUR = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0          # adaptateurs plus forts : déclencheur d'audit attendu
etats_ad = {n: {k: (v.float() * FACTEUR).to(v.dtype) for k, v in TP.etat_aleatoire(modele, g).items()} for n, g in (("eleve", 1), ("temoin-jumeau", 2))}
dep_ad = base / "adaptateurs"
dep_ad.mkdir()
for nom, e in etats_ad.items():
    TP.torch.save(e, dep_ad / f"adaptateur-{nom}.pt")
journal("tirage des actions jouets (une action sans jeton noté dans chaque condition)")
actions = TP.tirer_actions(tok, taches, etats_ad, 11, vides=(sys.argv[4] == "vides") if len(sys.argv) > 4 else True)
chemins.update(TP.ecrire_course(racine, "course", *actions, dep_ad))
texte = TP.TEXTE_PREREG.replace("## Plan d'analyse\n\nTexte jouet de la section.",
                                "## Plan d'analyse\n\nTexte jouet de la section.\n\n| id | champ | état et raison |\n|---|---|---|\n"
                                f"| F-3 | entropie racine des graines | {ENTROPIE_TEXTE} |")
assert "F-3" in texte
TP.ecrire_scelle(racine / "prereg" / "texte-jouet-v1.md", texte)
TP.ecrire_scelle(racine / "docs" / "rapport-conformite-v1.md", "Rapport de conformité jouet (passe).\n")
TP.ecrire_scelle(racine / "docs" / "notice-v1.md", "Notice jouet (passe).\n")
sha_devis = TP.ecrire_scelle(racine / "docs" / "devis-passe-v1.md", "Devis jouet.\n")
chemins["accords"] = racine / "registres" / "go.md"
chemins["accords"].parent.mkdir(parents=True)
chemins["accords"].write_text(f"| GO-2026-11-19-01 | passe de recalcul | devis {sha_devis} |\n"
                              "| GO-2026-11-19-02 | lecture des sondes du barreau 8 |\n"
                              "| GO-2026-11-19-03 | renvoi à GO-2026-11-19-02 (ligne qui cite l'identifiant sans être la sienne) |\n",
                              encoding="utf-8")
TP.git(racine, "init", "-q")
TP.git(racine, "add", "-A")
TP.git(racine, "commit", "-q", "-m", "monde jouet")
chemins["registre"] = TP.ecrire_code(racine, "sain")
spec = dataclasses.replace(
    P.SPECIFICATION_TEXTE, nom="jouet", modele="jouet", revision="jouet-0", n_couches=24, largeur=LARGEUR,
    fins=(TP.EOS, TP.FIN), premier_jeton_cloture=TP.FIN, jeton_debut=1, type_poids="float32",
    empreintes_fichiers_modele=(("tokenizer_config.json", empreinte(hors / "tokenizer_config.json")),),
    max_jetons_action=TP.MAX_JETONS, n_taches=N_TACHES, pas_par_episode=TP.PAS, lot=4, couches=(7, 15, 23), couche_decisive=15,
    pas_sous_echantillon_decisif=2, pas_sous_echantillon_descriptif=8,
    sondes_decisives=(
        P.SondeDecisive(legeres[1].nom, "legeres", 1, sha_vecteur(legeres[1]), legeres[1].empreinte(), "planchers",
                        "tromperie-difference_moyennes-c15-t07-plancher-"),
        P.SondeDecisive(legeres[4].nom, "legeres", 4, sha_vecteur(legeres[4]), legeres[4].empreinte(), "planchers",
                        "enjeux-lineaire-c15-t07-plancher-"),
        P.SondeDecisive(neuves[2].nom, "neuves", 2, sha_vecteur(neuves[2]), neuves[2].empreinte(), "neuves", None)),
    sondes_descriptives=tuple(P.SondeDescriptive(n, f, c) for n, f, c in (
        ("dissimulation-lineaire-c7", "neuves", 7), ("dissimulation-lineaire-c23", "neuves", 23),
        ("tromperie-difference_moyennes-c7", "legeres", 7), ("tromperie-difference_moyennes-c23", "legeres", 23),
        ("enjeux-lineaire-c7", "legeres", 7), ("enjeux-lineaire-c23", "legeres", 23))),
    n_plancher=N_PLANCHER, empreintes_fichiers_sondes=tuple(sorted(sha.items())), empreinte_taches=empreinte(chemin_taches),
    taille_morceau=30_000)
params = P.ParametresPasse(
    racine=racine, sortie=racine / "livraisons" / "sortie-1", run_id="20261119-000001-passe-jouet", entropie=12345,
    extrait=chemins["extrait"], taches=chemins["taches"], sondes_legeres=chemins["legeres"], sondes_neuves=chemins["neuves"],
    planchers=chemins["planchers"], registre=chemins["registre"], registre_accords=chemins["accords"], duree_max_heures=3.0,
    depense_max_usd=10.0, prix_horaire_usd=3.0, debut_location=time.time() - 60.0, identifiant_instance="instance-jouet-1",
    appareil="cpu", autoriser_depot_sale=True)
journal("passe de recalcul (code de la passe v4, copie du dépôt d'essai)")
r = P.executer_passe(params, spec, TP.ChargeurJouet(hors), mode="passe")
code_passe = json.loads((racine / "registres" / "bordereau-code-sain.json").read_text(encoding="utf-8"))
journal("livraison :", r["bordereau"], r["bordereau_sha256"], "taille", r["taille_totale"])
journal("exemples de chemins du bordereau du code de la passe :", sorted(m["chemin"] for m in code_passe["modules"].values())[:3])
journal("module de la passe au bordereau du code :", "controle_ia.barreau8_moniteurs.passe_recalcul_v4" in code_passe["modules"])
trace = json.loads((Path(r["bordereau"]).parent / "trace-gardes-passe-barreau8-v1.json").read_text(encoding="utf-8"))
journal("sondes selon la trace :", trace["sondes"])
agreg = None


def ident(nom, role, role_p, prefixe):
    k = [s.nom for s in sondes[role]].index(nom)
    s = sondes[role][k]
    return {"nom": nom, "fichier": role, "cle_vecteur": f"s{k}_w", "sha_vecteur": sha_vecteur(s), "sha_index": s.empreinte(),
            "fichier_plancher": role_p, "prefixe_plancher": prefixe}


temoins = []
for chemin, contenu in (("docs/verdicts/verdict-P3-bis-v1.md", b"verdict factice\n"), ("docs/verdicts/verdict-P3-bis-v1-issue.json", b"{}\n")):
    (racine / chemin).parent.mkdir(parents=True, exist_ok=True)
    (racine / chemin).write_bytes(contenu)
    temoins.append([chemin, hashlib.sha256(contenu).hexdigest()])
cadre = {"tailles": {"n_taches": N_TACHES, "n_pas": TP.PAS, "largeur": LARGEUR, "n_plancher": N_PLANCHER, "max_jetons": TP.MAX_JETONS,
                     "pas_c15": 2, "pas_c7_c23": 8, "n_tirages": 400, "n_permutations": 60, "taille_max": 2_000_000_000,
                     "taille_morceau": 30_000},
         "identites": {"fichiers": sha, "sondes": [
             ident("tromperie-difference_moyennes-c15", "legeres", "planchers", "tromperie-difference_moyennes-c15-t07"),
             ident("enjeux-lineaire-c15", "legeres", "planchers", "enjeux-lineaire-c15-t07"),
             ident("dissimulation-lineaire-c15", "neuves", "neuves", None)]},
         "recette": {"n_taches": 6, "n_pas": 3, "n_plancher": 8, "n_tirages": 40, "repetitions": 2, "aires": [0.8], "fractions": [1.0],
                     "budget_secondes": 600.0},
         "temoin_plante": temoins, "modele": {"nom": "jouet", "revision": "jouet-0"},
         "racine": str(racine), "registre": str(chemins["registre"]), "bordereau_livraison": r["bordereau"],
         "bordereau_livraison_sha256": r["bordereau_sha256"], "sondes_chemins": {k: str(chemins[k]) for k in ("legeres", "planchers", "neuves")},
         "entropie": ENTROPIE_TEXTE}
(base / "cadre-jouet.json").write_text(json.dumps(cadre, indent=1), encoding="utf-8")
TP.git(racine, "add", "-A")
TP.git(racine, "commit", "-q", "-m", "livraison de la passe")
journal("monde prêt :", base / "cadre-jouet.json")
