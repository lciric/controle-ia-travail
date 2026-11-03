#!/usr/bin/env python3
"""KIT SCHEURER v2 (sous-agent de session-depot, 3 novembre 2026) : v1 (gardée, R12) plus la variante « sans-claude » (proposeurs Argon, Kimi, Astra ; aiguilleur Astra ; juges Astra et Argon ; lecteurs Astra et Argon ; metteur Astra ; aucun rôle Claude ; relais 8806 non démarré, contrôle de Claude non joué) ; S17 propre à cette variante ; les configurations existantes ne sont ni réécrites ni changées.
KIT SCHEURER, v1 (sous-agent de session-depot, 3 novembre 2026) : dérivé du kit Ibrahim v2 (outils/course-ibrahim-q1-v1, 965eb21b) par substitution de noms et par les changements de la course Scheurer (deux pièces servies, cinq variantes dont trois sans Opus proposeur, jeu de rôles par variante (Opus ou Fable), garde lexicale sans « gemini » ni « openai », juge du n° 419, marge d'appels 2 × plan + 5).
Lanceur Python de la course d'idéation Scheurer (question 1), v2 = `lancer_course_scheurer_v2.py` (gardé, R12) au-dessus de
`course_scheurer_v2.py` (garde lexicale CLH-03), avec les pièces gelées exigées v2 — dérivé de `nuit/lancer_mini_course_v2.py` (inchangé).

Rédigé le 3 novembre 2026 (sous-agent de session-depot) ; rien n'a été lancé de payant par le rédacteur. Trois sous-commandes :

  verifier  --configuration CONF [--registre-go registres/go.md --go-attendu GO-AAAA-MM-JJ-NN]   aucune écriture, aucun appel
            [--preenregistrement FICHE --contre-lecture RAPPORT]        (fiche scellée et pièces gelées vérifiées en plus)
  simuler   --configuration CONF --sortie NEUVE                                                  moteur simulé (aucun appel)
  lancer    --configuration CONF --sortie NEUVE --registre-depense R --registre-go registres/go.md --go-attendu GO-…
            --preenregistrement FICHE --contre-lecture RAPPORT --confirmer-moteur-reel             moteur réel

Ordre des gardes, **avant tout appel et toute écriture dans la sortie** (celui de la mini-course, plus les contrôles
Heimersheim) : configuration v56 (spécification injectée au moteur réel) ; spécification (fiche de lancement et contre-lecture
scellées, sans marqueur, la première citant l'empreinte de la seconde) exigée conforme au moteur réel ; configuration de
génération v56 ; contrôles Scheurer (`verifier_configuration_scheurer`) ; déclaration des bras v56 et table R5 rejouée à
É0 ; montant requis (portée « course » : S17) ; moteur réel : dépendances (porte de plafond par fournisseur), identifiant
`GO_ID` de l'environnement égal à `--go-attendu`, ligne de GO (registre lu par la garde du dépôt, ligne sans extension relue
par `verifier_go_v56` : un seul montant, égal à S17), **pièces gelées** de la fiche identiques sur disque et couvrant la
configuration, les consignes, la question, la pièce, les commandes, les relais, les lanceurs et la garde du dépôt,
`--confirmer-moteur-reel`.

Moteur réel : chaque fournisseur est une commande externe (`AdaptateurCommandeExterneNuitV2`) à porte « environnement » ;
les jetons `{REGISTRE}` (registre de dépense cumulée du run) et `{DEPOT}` (racine du dépôt, déduite de ce fichier) des
commandes sont remplacés. L'environnement de ce processus ne porte aucun nom de clé (refus du noyau sinon).

Codes : 0 sortie écrite ; 2 refus, arrêt (signal compris) ou nœud (motif sur la sortie d'erreur).
"""

import argparse
import importlib.util
import json
import os
import re
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)                                       # …/orchestrateur
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(RACINE)))   # racine du dépôt
sys.path.insert(0, RACINE)
sys.path.insert(0, ICI)

from pole import configuration_v56 as cfg  # noqa: E402
from pole import course2_v56 as c2  # noqa: E402
from pole import gardes_e0_v56 as ge  # noqa: E402
from pole.adaptateurs_v56 import porte_depuis_configuration  # noqa: E402
from pole.noyau_v56 import ArretParSignal  # noqa: E402
from pole.outils import ecrire_json_scelle, sha256_fichier, verifier_scelle  # noqa: E402
import course_scheurer_v2 as ch  # noqa: E402

VERSION = "lanceur-course-scheurer-v2 (orchestrateur v56, course_scheurer_v2)"
JETON_REGISTRE, JETON_DEPOT = "{REGISTRE}", "{DEPOT}"
GARDE_DEPOT = os.path.join(DEPOT, ".claude", "hooks", "garde_calcul.py")
EN_TETE_GO = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
              "|---|---|---|---|---|---|---|---|\n")
MOTIF_PIECE = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|", re.M)
GO_FORME = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")
# fichiers que la fiche de lancement doit geler, en plus de la configuration et de ses pièces (chemins depuis la racine du dépôt)
KIT = "donnees/course-scheurer-v1/orchestrateur"
A1BIS = "docs/notes/ideation-organisme-v1/commandes-a1-bis-v1"
GELES_TOUJOURS = (f"{KIT}/scheurer/lancer_course_scheurer_v2.py", f"{KIT}/scheurer/lancer-course-scheurer-v2.sh",
                  f"{KIT}/scheurer/course_scheurer_v2.py", f"{KIT}/scheurer/course_scheurer_v2.py", f"{KIT}/scheurer/commande_claude_scheurer_v1.py",
                  f"{KIT}/scheurer/trace_agregee_course_scheurer_v1.py", f"{KIT}/nuit/chercher_cles_v1.py",
                  f"{KIT}/nuit/registre_depense_cumulee_v1.py", f"{KIT}/pole/course2_nuit_v1.py", f"{KIT}/pole/course2_nuit_v2.py",
                  f"{KIT}/pole/course2_v56.py", f"{A1BIS}/commande_claude_a1bis_v1.py", f"{A1BIS}/commande_pole_v56_commun_v1.py",
                  f"{A1BIS}/commande_astra_a1bis_v1.py", f"{A1BIS}/collisionneur_v8.py", f"{A1BIS}/registre_depense_cumulee_v1.py",
                  ".claude/hooks/garde_calcul.py")
GELES_PAR_FOURNISSEUR = {"kimi": ("docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py", f"{KIT}/nuit/commande_kimi_v2.py"),
                         "argon": (f"{KIT}/nuit/commande_argon_v56_nuit_v2.py", f"{KIT}/scheurer/argon/collisionneur_v7.py")}


class LancementRefuse(RuntimeError):
    pass


def specification_depuis_fichiers(prereg, contre_lecture):
    sortie = {}
    for cle, chemin in (("preenregistrement", prereg), ("contre_lecture", contre_lecture)):
        if not chemin:
            raise LancementRefuse(f"{cle} : chemin exigé au moteur réel (R1, R2)")
        chemin = os.path.abspath(chemin)
        if not os.path.isfile(chemin):
            raise LancementRefuse(f"{cle} absent : {chemin} (contre-lecture et scellement exigés avant le moteur réel, R1, R2)")
        sortie[cle] = {"chemin": chemin, "sha256": sha256_fichier(chemin)}
    return sortie


def pieces_gelees(texte_prereg):
    debut = texte_prereg.find("### Pièces gelées")
    if debut < 0:
        raise LancementRefuse("fiche de lancement sans section « ### Pièces gelées »")
    fin = texte_prereg.find("\n## ", debut)
    pieces = MOTIF_PIECE.findall(texte_prereg[debut:fin if fin > 0 else None])
    if not pieces:
        raise LancementRefuse("section « Pièces gelées » vide")
    return pieces


def exigees(conf, chemin_conf, depot=DEPOT):
    """Chemins (depuis la racine du dépôt) que la fiche doit geler pour cette configuration."""
    base = os.path.dirname(os.path.abspath(chemin_conf))
    rel = lambda p: os.path.relpath(os.path.normpath(os.path.join(base, p)), depot)  # noqa: E731
    e = {os.path.relpath(os.path.abspath(chemin_conf), depot)} | set(GELES_TOUJOURS)
    e |= {rel(p["chemin"]) for p in conf["pieces"].values()}
    e.add(rel(conf["bisociateur"]["gu_krenn"]["source"]["chemin"]))
    for f in conf.get("fournisseurs") or {}:
        e |= set(GELES_PAR_FOURNISSEUR.get(f, ()))
    return e


def verifier_pieces_gelees(prereg, conf, chemin_conf, depot=DEPOT):
    """Fiche scellée ; chaque pièce gelée identique sur disque ; la table couvre tout ce que `exigees` nomme (aucun repli)."""
    if not verifier_scelle(prereg):
        raise LancementRefuse(f"fiche de lancement non scellée ou modifiée : {prereg}")
    with open(prereg, encoding="utf-8") as f:
        texte = f.read()
    vues = []
    for chemin, attendue in pieces_gelees(texte):
        p = os.path.join(depot, chemin)
        if not os.path.isfile(p):
            raise LancementRefuse(f"pièce gelée absente : {chemin}")
        vue = sha256_fichier(p)
        if vue != attendue:
            raise LancementRefuse(f"pièce gelée modifiée : {chemin} ({vue[:12]}… ≠ {attendue[:12]}…)")
        vues.append({"chemin": chemin, "sha256": vue})
    manquent = sorted(exigees(conf, chemin_conf, depot) - {v["chemin"] for v in vues})
    if manquent:
        raise LancementRefuse("pièces non gelées par la fiche de lancement : " + ", ".join(manquent))
    return vues


def verifier_go_course(go_id, registre, montant):
    """A15 : registre entier lu par la garde du dépôt (extensions admises), ligne citée sans extension, relue seule par
    `verifier_go_v56` (un seul montant, égal à S17). Rend (ligne, description)."""
    spec = importlib.util.spec_from_file_location("garde_calcul_depot", GARDE_DEPOT)
    garde = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(garde)
    try:
        lu = garde.lire_go(__import__("pathlib").Path(registre))
    except SystemExit:
        raise cfg.GoRefuse("A15 : registre des GO refusé par la garde du dépôt (motif ci-dessus)") from None
    g = lu.get(go_id)
    if g is None:
        raise cfg.GoRefuse(f"A15 : {go_id} absent de {registre}")
    if g["extensions"]:
        raise cfg.GoRefuse(f"A15 : {go_id} porte une ligne d'extension : une seule ligne exigée pour la course")
    with open(registre, encoding="utf-8") as f:
        lignes = [l for l in f.read().splitlines() if cfg.c53.LIGNE_GO.match(l)]
    gardees = [l for l in lignes if l.split("|")[1].strip() == go_id or ("révocation" in l and go_id in l)]
    with tempfile.TemporaryDirectory(prefix="extrait-go-kirchner-") as d:
        extrait = os.path.join(d, "extrait-registre-go.md")
        with open(extrait, "w", encoding="utf-8") as f:
            f.write("# Extrait du registre des GO (lecture A15 de la course Scheurer)\n\n" + EN_TETE_GO + "\n".join(gardees) + "\n")
        ligne = cfg.verifier_go_v56(go_id, extrait, montant)
    return ligne, {"registre": os.path.abspath(registre), "registre_sha256": sha256_fichier(registre),
                   "garde_depot_sha256": sha256_fichier(GARDE_DEPOT), "lignes_extraites": len(gardees),
                   "regle": "registre entier lu par la garde du dépôt ; ligne citée sans extension, relue seule par verifier_go_v56 "
                            "(montant unique égal à S17)"}


def adaptateurs_simules(conf):
    from pole.simulation_v56 import AdaptateurSimuleV56
    s = conf.get("simulation") or {}
    for k in ("cout_par_appel_usd", "fiches_par_appel"):
        if k not in s:
            raise cfg.ConfigurationRefusee(f"moteur simulé : simulation.{k} exigé (aucun défaut)")
    return {n: AdaptateurSimuleV56(champs_fiche=conf["champs_fiche"], items=conf["items_juge"], champ_titre=conf["champ_titre"],
                                   cout_par_appel_usd=s["cout_par_appel_usd"], fiches_par_appel=int(s["fiches_par_appel"]))
            for n in sorted(c2.GenerationV56.fournisseurs_requis(conf))}


def commande_resolue(f, commande, registre, depot=DEPOT):
    if sum(JETON_REGISTRE in x for x in commande) != 1:
        raise cfg.ConfigurationRefusee(f"fournisseurs.{f}.commande : le jeton {JETON_REGISTRE} doit y figurer une fois")
    return [x.replace(JETON_REGISTRE, registre).replace(JETON_DEPOT, depot) for x in commande]


def adaptateurs_reels(conf, registre_depense):
    adaptateurs, portes, commandes = {}, {}, {}
    registre = os.path.abspath(registre_depense)
    if not os.path.isdir(os.path.dirname(registre)):
        raise LancementRefuse(f"dossier du registre de dépense absent : {os.path.dirname(registre)}")
    for nom, f in sorted((conf.get("fournisseurs") or {}).items()):
        if f.get("type") != "commande_externe":
            raise cfg.ConfigurationRefusee(f"fournisseurs.{nom}.type : « commande_externe » seul permis")
        commande = commande_resolue(nom, f["commande"], registre)
        for x in commande[3:4]:
            if not os.path.isfile(x):
                raise LancementRefuse(f"fournisseurs.{nom} : commande absente {x}")
        ad = ch.AdaptateurCommandeExterneNuitV2(commande, delai_s=float(f["delai_s"]), exiger_modele_servi=True,
                                                modeles_servis_permis=f.get("modeles_servis_permis"))
        adaptateurs[nom] = ad
        portes[nom] = porte_depuis_configuration(nom, f.get("porte_plafond"), ad)
        commandes[nom] = commande
    return adaptateurs, portes, commandes


def lire_conf(chemin, spec=None):
    with open(chemin, encoding="utf-8") as f:
        brut = json.load(f)
    if "specification" in brut:
        raise cfg.ConfigurationRefusee("la configuration figée ne porte pas « specification » : le lanceur l'injecte (moteur réel)")
    if spec is not None:
        brut["specification"] = spec
    return cfg.lire_configuration_v56(brut, base=os.path.dirname(os.path.abspath(chemin)))


def executer(args, environnement=None):
    env = os.environ if environnement is None else environnement
    reel = args.mode == "lancer"
    avec_fiche = reel or (args.mode == "verifier" and bool(getattr(args, "preenregistrement", None)))
    spec_fichiers = specification_depuis_fichiers(args.preenregistrement, args.contre_lecture) if avec_fiche else None
    conf = lire_conf(args.configuration, spec_fichiers)
    spec = cfg.verifier_specification_v56(conf)
    if avec_fiche and spec["conforme"] is not True:
        raise cfg.ConfigurationRefusee(f"spécification non conforme ({spec['motif']}) : aucun lancement réel")
    c2.verifier_configuration_generation_v56(conf)
    resume = ch.verifier_configuration_scheurer(conf)
    decl, params = c2.declarer_bras_v56(conf)
    non = [b for b, d in decl.items() if not d.get("produit")]
    if non:
        raise cfg.ConfigurationRefusee(f"bras non produits à É0 : {non} ({[decl[b].get('motif') for b in non]}) : aucun lancement")
    table_r5 = ge.rejouer_gardes_v56(conf, decl, params, plan="course", etage1=None, specification=spec)
    montant = cfg.montant_requis(conf, 1, None)
    go, pieces = None, None
    if reel or args.registre_go:
        if reel:
            manques = cfg.verifier_dependances_lancement_v56(conf, "course")
            if manques:
                raise cfg.GoRefuse("A15 : aucun lancement :\n- " + "\n- ".join(manques))
            if not args.registre_go:
                raise cfg.GoRefuse("A15 : --registre-go exigé avec le moteur réel")
        attendu = getattr(args, "go_attendu", None)
        if not attendu or not GO_FORME.fullmatch(attendu):
            raise cfg.GoRefuse(f"--go-attendu GO-AAAA-MM-JJ-NN exigé (reçu {attendu!r})")
        if env.get("GO_ID") != attendu:
            raise cfg.GoRefuse(f"la course ne court que sous {attendu} (GO_ID reçu : {env.get('GO_ID')!r})")
        go, lecture_go = verifier_go_course(attendu, args.registre_go, montant)
        go = dict(go, lecture=lecture_go)
    if avec_fiche:
        pieces = verifier_pieces_gelees(spec_fichiers["preenregistrement"]["chemin"], conf, args.configuration)
    if reel:
        if not args.confirmer_moteur_reel:
            raise cfg.ConfigurationRefusee("moteur réel : --confirmer-moteur-reel exigé")
    if args.mode == "verifier":
        print(json.dumps({"version": VERSION, "configuration_fichier_sha256": sha256_fichier(args.configuration),
                          "configuration_empreinte": conf["empreinte_configuration"], "specification": spec, "scheurer": resume,
                          "scenario": ch.SCENARIO, "montant_requis_go_usd": montant, "bras": decl,
                          "table_r5_e0": [{k: x[k] for k in ("ligne", "statut")} for x in table_r5], "go": go,
                          "pieces_gelees_verifiees": pieces, "ecriture": "aucune", "appel": "aucun"}, ensure_ascii=False, indent=1, default=str))
        return 0
    if os.path.exists(args.sortie):
        raise LancementRefuse(f"{args.sortie} existe déjà (R12)")
    base_sessions = tempfile.mkdtemp(prefix="pole-sessions-scheurer-v1-")
    if reel:
        adaptateurs, portes, commandes = adaptateurs_reels(conf, args.registre_depense)
    else:
        adaptateurs, portes, commandes = adaptateurs_simules(conf), None, None
        go = {"moteur": "simule", "go": "sans objet (aucune dépense)"}
    lancement = {"version": VERSION, "moteur": "reel" if reel else "simule", "configuration_chemin": os.path.abspath(args.configuration),
                 "configuration_fichier_sha256": sha256_fichier(args.configuration),
                 "configuration_empreinte": conf["empreinte_configuration"], "specification": spec, "go": go, "scheurer": resume,
                 "pieces_gelees_verifiees": pieces, "commandes": commandes, "scenario": ch.SCENARIO,
                 "temoins_plantes": "aucun", "bras": decl,
                 "table_r5_e0": [{k: x[k] for k in ("ligne", "statut")} for x in table_r5]}
    manifeste = os.path.join(os.path.dirname(os.path.abspath(args.sortie)), "manifeste-lancement-scheurer-v1.json")
    if os.path.exists(manifeste):
        raise LancementRefuse(f"{manifeste} existe déjà (R12) : un dossier de run par lancement")
    ecrire_json_scelle(manifeste, lancement)  # avant tout appel : écrit même si la course s'arrête
    try:
        res = ch.executer_course_scheurer_v1(conf, args.sortie, adaptateurs, go=go, racine_sessions=base_sessions, portes=portes,
                                                specification=spec)
    finally:
        if os.path.isdir(base_sessions) and not os.listdir(base_sessions):
            os.rmdir(base_sessions)
    print(json.dumps({"version": VERSION, "bilan": res}, ensure_ascii=False, default=str))
    return 0


def construire_analyseur():
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = a.add_subparsers(dest="mode", required=True)
    for nom in ("verifier", "simuler", "lancer"):
        p = sous.add_parser(nom)
        p.add_argument("--configuration", required=True)
        p.add_argument("--registre-go", default=None)
        p.add_argument("--go-attendu", default=None)
        if nom in ("simuler", "lancer"):
            p.add_argument("--sortie", required=True)
        if nom == "lancer":
            p.add_argument("--registre-depense", required=True)
            p.add_argument("--confirmer-moteur-reel", action="store_true")
            p.add_argument("--preenregistrement", required=True)
            p.add_argument("--contre-lecture", required=True)
        if nom == "verifier":
            p.add_argument("--preenregistrement", default=None, help="fiche de lancement scellée (pièces gelées vérifiées)")
            p.add_argument("--contre-lecture", default=None)
    return a


def principal(argv=None, environnement=None):
    args = construire_analyseur().parse_args(argv)
    try:
        return executer(args, environnement)
    except (Exception, ArretParSignal, KeyboardInterrupt) as e:  # noqa: BLE001 — tout refus, arrêt ou nœud rend 2
        print(json.dumps({"arret": type(e).__name__ + " : " + str(e)[:3000]}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(principal())
