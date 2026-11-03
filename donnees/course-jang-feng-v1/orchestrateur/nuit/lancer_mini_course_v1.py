#!/usr/bin/env python3
"""Lanceur Python de la mini-course d'idéation, Kimi et Argon seuls (GO-2026-11-01-12, devis scénario B) — version 1.

Rédigé le 1er novembre 2026 (sous-agent de session-depot) ; rien n'a été lancé par le rédacteur. Reprend l'ordre des gardes
de `demonstrations/ideation_v8.py` (orchestrateur v56, inchangé) pour une seule génération de `pole/course2_nuit_v1.py`
(sans passe « tableau »), avec trois sous-commandes :

  verifier  --configuration CONF [--registre-go registres/go.md]           aucune écriture, aucun appel (« vérifier seulement »)
  simuler   --configuration CONF --sortie NEUVE [--fiche-factice]         moteur simulé (aucun appel, aucune dépense)
  lancer    --configuration CONF --sortie NEUVE --registre-depense R --registre-go registres/go.md --confirmer-moteur-reel
            [--preenregistrement P --contre-lecture C]                    moteur réel (GO_ID=GO-2026-11-01-12 exigé)

Ordre des gardes, **avant tout appel et toute écriture dans la sortie** : configuration v56 (spécification injectée au moteur
réel) ; spécification (préenregistrement et contre-lecture scellés, sans marqueur, le premier citant l'empreinte de la
seconde : CL20-03) — exigée conforme au moteur réel, rapportée sinon ; configuration de génération v56, puis contrôles du
scénario B (`verifier_configuration_nuit`) ; déclaration des bras v56 et table R5 rejouée à É0 (A12) ; montant requis
(portée « course » : S17 = 10 USD) ; moteur réel : dépendances (porte de plafond par fournisseur, A15), ligne de GO
(`verifier_go_v56` : un seul montant, égal à 10 USD), identifiant égal à GO-2026-11-01-12, **pièces gelées** du
préenregistrement identiques sur disque, `--confirmer-moteur-reel`.

Moteur réel : chaque fournisseur est une commande externe (`AdaptateurCommandeExterneNuitV1`, recopie du modèle servi,
refus « modèle servi » = arrêt de la course) munie de la porte « environnement » (plafond dur de chaque étape passé dans
`PLAFOND_ETAPE_USD`). Le jeton `{REGISTRE}` des commandes de la configuration est remplacé par `--registre-depense` (registre
de dépense cumulée partagé, dans le dossier du run). L'environnement de ce processus ne porte **aucun nom de clé** (refus du
noyau sinon) : les clés vivent dans les seuls relais locaux, lancés par `lancer-mini-course-v1.sh`.

Codes : 0 sortie écrite ; 2 refus, arrêt (signal compris) ou nœud (motif sur la sortie d'erreur).
"""

import argparse
import json
import os
import re
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)                       # …/orchestrateur
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(RACINE)))  # …/controle-ia-travail
sys.path.insert(0, RACINE)

from pole import configuration_v56 as cfg  # noqa: E402
from pole import course2_nuit_v1 as nuit  # noqa: E402
from pole import course2_v56 as c2  # noqa: E402
from pole import gardes_e0_v56 as ge  # noqa: E402
from pole.adaptateurs_v56 import porte_depuis_configuration  # noqa: E402
from pole.noyau_v56 import ArretParSignal  # noqa: E402
from pole.outils import ecrire_json_scelle, sha256_fichier, verifier_scelle  # noqa: E402

VERSION = "lanceur-mini-course-v1 (orchestrateur v56, course2_nuit_v1)"
GO_ATTENDU = "GO-2026-11-01-12"
DOSSIER_PREREG = os.path.join(DEPOT, "docs", "notes", "mini-course-kimi-argon-v1")
PREREG = os.path.join(DOSSIER_PREREG, "preregistrement-mini-course-kimi-argon-v1.md")
CONTRE_LECTURE = os.path.join(DOSSIER_PREREG, "contre-lecture-preregistrement-mini-course-kimi-argon-v1.md")
JETON_REGISTRE = "{REGISTRE}"
GARDE_DEPOT = os.path.join(DEPOT, ".claude", "hooks", "garde_calcul.py")
EN_TETE_GO = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
              "|---|---|---|---|---|---|---|---|\n")
MOTIF_PIECE = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|", re.M)


class LancementRefuse(RuntimeError):
    pass


# --- spécification et pièces gelées ------------------------------------------------------------------------------------------


def specification_depuis_fichiers(prereg, contre_lecture):
    """{preenregistrement, contre_lecture} : chemins absolus et empreintes lues sur disque (la v56 vérifie sceaux et citation)."""
    sortie = {}
    for cle, chemin in (("preenregistrement", prereg), ("contre_lecture", contre_lecture)):
        chemin = os.path.abspath(chemin)
        if not os.path.isfile(chemin):
            raise LancementRefuse(f"{cle} absent : {chemin} (contre-lecture et scellement exigés avant le moteur réel, R1, R2)")
        sortie[cle] = {"chemin": chemin, "sha256": sha256_fichier(chemin)}
    return sortie


def pieces_gelees(texte_prereg):
    """Lignes « | `chemin depuis la racine du dépôt` | `sha256` | … » de la section « Pièces gelées »."""
    debut = texte_prereg.find("### Pièces gelées")
    if debut < 0:
        raise LancementRefuse("préenregistrement sans section « ### Pièces gelées »")
    fin = texte_prereg.find("\n## ", debut)
    pieces = MOTIF_PIECE.findall(texte_prereg[debut:fin if fin > 0 else None])
    if not pieces:
        raise LancementRefuse("section « Pièces gelées » vide")
    return pieces


def verifier_pieces_gelees(prereg, depot=DEPOT):
    """Préenregistrement scellé, puis chaque pièce gelée identique sur disque (aucun repli)."""
    if not verifier_scelle(prereg):
        raise LancementRefuse(f"préenregistrement non scellé ou modifié : {prereg}")
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
    return vues


# --- ligne de GO ------------------------------------------------------------------------------------------------------------


def verifier_go_nuit(go_id, registre, montant):
    """A15 en deux temps. (1) Le registre entier est lu par la garde du dépôt (`.claude/hooks/garde_calcul.py`, `lire_go`),
    qui admet les lignes d'extension (R-389) ; la lecture de la v56 (`configuration_v53.lire_registre_go`) les refuse
    (« identifiant en double » sur GO-2026-10-24-07 et GO-2026-10-24-05, lignes d'autres GO) et ne peut donc pas lire le vrai
    registre. La ligne citée ne doit porter **aucune extension**. (2) Un extrait (en-tête, la seule ligne citée, les révocations
    qui la citent) est relu par `verifier_go_v56` : type, Lazar, validité, révocations et **un seul montant égal au montant
    requis** (10 USD). Rend (ligne lue par la v56, description de la lecture)."""
    import importlib.util
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
        raise cfg.GoRefuse(f"A15 : {go_id} porte une ligne d'extension : une seule ligne exigée pour la mini-course")
    with open(registre, encoding="utf-8") as f:
        lignes = [l for l in f.read().splitlines() if cfg.c53.LIGNE_GO.match(l)]
    gardees = [l for l in lignes if l.split("|")[1].strip() == go_id or ("révocation" in l and go_id in l)]
    with tempfile.TemporaryDirectory(prefix="extrait-go-nuit-") as d:
        extrait = os.path.join(d, "extrait-registre-go.md")
        with open(extrait, "w", encoding="utf-8") as f:
            f.write("# Extrait du registre des GO (lecture A15 de la mini-course)\n\n" + EN_TETE_GO + "\n".join(gardees) + "\n")
        ligne = cfg.verifier_go_v56(go_id, extrait, montant)
    return ligne, {"registre": os.path.abspath(registre), "registre_sha256": sha256_fichier(registre),
                   "garde_depot_sha256": sha256_fichier(GARDE_DEPOT), "lignes_extraites": len(gardees),
                   "regle": "registre entier lu par la garde du dépôt (extensions R-389 admises) ; ligne citée sans extension, "
                            "relue seule par verifier_go_v56 (montant unique égal au montant requis)"}


# --- adaptateurs ----------------------------------------------------------------------------------------------------------------


def adaptateurs_simules(conf, fiche_factice=None):
    from pole.simulation_v56 import AdaptateurSimuleV56
    s = conf.get("simulation") or {}
    for k in ("cout_par_appel_usd", "fiches_par_appel"):
        if k not in s:
            raise cfg.ConfigurationRefusee(f"moteur simulé : simulation.{k} exigé (aucun défaut)")

    class AdaptateurSimuleNuit(AdaptateurSimuleV56):
        """Moteur simulé v56 ; avec `fiche_factice`, la première fiche du proposeur simulé porte la chaîne canari donnée
        (fiche factice du préenregistrement : elle doit rester absente de la trace agrégée)."""

        def reponse(self, role, consigne, modele):
            t = super().reponse(role, consigne, modele)
            if fiche_factice and "## Case" in consigne and "## Les deux fiches" not in consigne:
                o = json.loads(t)
                o["fiches"][0]["hypothese"] = o["fiches"][0]["hypothese"] + " " + fiche_factice
                t = json.dumps(o, ensure_ascii=False)
            return t

    fournisseurs = c2.GenerationV56.fournisseurs_requis(conf)
    return {n: AdaptateurSimuleNuit(champs_fiche=conf["champs_fiche"], items=conf["items_juge"], champ_titre=conf["champ_titre"],
                                    cout_par_appel_usd=s["cout_par_appel_usd"], fiches_par_appel=int(s["fiches_par_appel"]))
            for n in sorted(fournisseurs)}


def adaptateurs_reels(conf, registre_depense):
    """Commandes externes de la nuit et leurs portes « environnement » ; `{REGISTRE}` remplacé (chemin absolu)."""
    adaptateurs, portes, commandes = {}, {}, {}
    registre = os.path.abspath(registre_depense)
    if not os.path.isdir(os.path.dirname(registre)):
        raise LancementRefuse(f"dossier du registre de dépense absent : {os.path.dirname(registre)}")
    for nom, f in sorted((conf.get("fournisseurs") or {}).items()):
        if f.get("type") != "commande_externe":
            raise cfg.ConfigurationRefusee(f"fournisseurs.{nom}.type : « commande_externe » seul permis à la mini-course")
        commande = [x.replace(JETON_REGISTRE, registre) for x in f["commande"]]
        if sum(JETON_REGISTRE in x for x in f["commande"]) != 1:
            raise cfg.ConfigurationRefusee(f"fournisseurs.{nom}.commande : le jeton {JETON_REGISTRE} doit y figurer une fois")
        ad = nuit.AdaptateurCommandeExterneNuitV1(commande, delai_s=float(f["delai_s"]), exiger_modele_servi=True,
                                                  modeles_servis_permis=f.get("modeles_servis_permis"))
        adaptateurs[nom] = ad
        portes[nom] = porte_depuis_configuration(nom, f.get("porte_plafond"), ad)
        commandes[nom] = commande
    return adaptateurs, portes, commandes


# --- exécution ------------------------------------------------------------------------------------------------------------------


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
    spec_fichiers = specification_depuis_fichiers(args.preenregistrement, args.contre_lecture) if reel else None
    conf = lire_conf(args.configuration, spec_fichiers)
    spec = cfg.verifier_specification_v56(conf)
    if reel and spec["conforme"] is not True:
        raise cfg.ConfigurationRefusee(f"spécification non conforme ({spec['motif']}) : aucun lancement réel (CL20-03)")
    c2.verifier_configuration_generation_v56(conf)
    nuit.verifier_configuration_nuit(conf)
    decl, params = c2.declarer_bras_v56(conf)
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
        if env.get("GO_ID") or reel:
            if env.get("GO_ID") != GO_ATTENDU:
                raise cfg.GoRefuse(f"la mini-course ne court que sous {GO_ATTENDU} (GO_ID reçu : {env.get('GO_ID')!r})")
            go, lecture_go = verifier_go_nuit(env.get("GO_ID"), args.registre_go, montant)
            go = dict(go, lecture=lecture_go)
    if reel:
        pieces = verifier_pieces_gelees(spec_fichiers["preenregistrement"]["chemin"])
        if not args.confirmer_moteur_reel:
            raise cfg.ConfigurationRefusee("moteur réel : --confirmer-moteur-reel exigé")
    if args.mode == "verifier":
        print(json.dumps({"version": VERSION, "configuration_fichier_sha256": sha256_fichier(args.configuration),
                          "configuration_empreinte": conf["empreinte_configuration"], "specification": spec,
                          "scenario": nuit.SCENARIO, "montant_requis_go_usd": montant, "bras": decl,
                          "table_r5_e0": [{k: x[k] for k in ("ligne", "statut")} for x in table_r5], "go": go,
                          "ecriture": "aucune", "appel": "aucun"}, ensure_ascii=False, indent=1, default=str))
        return 0
    if os.path.exists(args.sortie):
        raise LancementRefuse(f"{args.sortie} existe déjà (R12)")
    base_sessions = tempfile.mkdtemp(prefix="pole-sessions-nuit-v1-")  # hors de la sortie (CL19-04)
    if reel:
        adaptateurs, portes, commandes = adaptateurs_reels(conf, args.registre_depense)
    else:
        adaptateurs, portes, commandes = adaptateurs_simules(conf, args.fiche_factice), None, None
        go = {"moteur": "simule", "go": "sans objet (aucune dépense)"}
    lancement = {"version": VERSION, "moteur": "reel" if reel else "simule", "configuration_chemin": os.path.abspath(args.configuration),
                 "configuration_fichier_sha256": sha256_fichier(args.configuration),
                 "configuration_empreinte": conf["empreinte_configuration"], "specification": spec, "go": go,
                 "pieces_gelees_verifiees": pieces, "commandes": commandes, "scenario": nuit.SCENARIO,
                 "fiche_factice": bool(getattr(args, "fiche_factice", None)),
                 "table_r5_e0": [{k: x[k] for k in ("ligne", "statut")} for x in table_r5]}
    manifeste = os.path.join(os.path.dirname(os.path.abspath(args.sortie)), "manifeste-lancement-nuit-v1.json")
    if os.path.exists(manifeste):
        raise LancementRefuse(f"{manifeste} existe déjà (R12) : un dossier de run par lancement")
    ecrire_json_scelle(manifeste, lancement)  # avant tout appel : écrit même si la course s'arrête
    try:
        res = nuit.executer_mini_course_v1(conf, args.sortie, adaptateurs, go=go, racine_sessions=base_sessions, portes=portes,
                                           specification=spec)
    finally:
        if os.path.isdir(base_sessions) and not os.listdir(base_sessions):
            os.rmdir(base_sessions)  # base vide (les sessions vides sont rangées par le noyau) ; une trace la garde
    print(json.dumps({"version": VERSION, "bilan": res}, ensure_ascii=False, default=str))
    return 0


def construire_analyseur():
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = a.add_subparsers(dest="mode", required=True)
    for nom in ("verifier", "simuler", "lancer"):
        p = sous.add_parser(nom)
        p.add_argument("--configuration", required=True)
        p.add_argument("--registre-go", default=None)
        if nom in ("simuler", "lancer"):
            p.add_argument("--sortie", required=True)
        if nom == "simuler":
            p.add_argument("--fiche-factice", default=None, help="chaîne canari portée par une fiche factice (répétition)")
        if nom == "lancer":
            p.add_argument("--registre-depense", required=True)
            p.add_argument("--confirmer-moteur-reel", action="store_true")
            p.add_argument("--preenregistrement", default=PREREG)
            p.add_argument("--contre-lecture", default=CONTRE_LECTURE)
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
