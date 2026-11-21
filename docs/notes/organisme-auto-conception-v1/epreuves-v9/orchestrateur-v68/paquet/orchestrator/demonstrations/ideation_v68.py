"""Course d'idéation : lanceur, version 68 (fichier neuf, R12) — la course 2 de `pole/course2_v68.py` : boucle réparée (la
sélection scellée est lue en objet, gardée ligne par ligne par A4), étage après la dernière génération, garde de budget de la
course, régimes séparés. Le lanceur v8 (`demonstrations/ideation_v8.py`) est chargé à part et inchangé : ses aides (analyseur,
réglages de l'étage, pré-pilote) servent telles quelles ; sans `--course-2`, la main lui passe.

  python -I -B demonstrations/ideation_v68.py --course-2 CONF SORTIE --generations N \
      [--lecture-selection oui|non] [--etage-apres-derniere] [--selection-vide omettre|servir_vide] \
      [--plafond-course-usd X] (--verifier-seulement | --moteur simule)

Interrupteurs, **éteints par défaut** : `--lecture-selection` vaut « non » sans l'option ; `--etage-apres-derniere` est absent
sans l'option ; `--selection-vide` vaut « omettre » (ce qui minimise ce qui est servi ; à fixer par l'additif). Régimes : éteint
(rien de servi ; étage entre générations si la configuration en porte un) ; « tests de mort sans rien servir »
(`--etage-apres-derniere`, sans lecture) ; « lecture de la sélection » (`--lecture-selection oui`, N ≥ 2, étage exigé).

Montant requis (`--verifier-seulement`) : `configuration_v68.montant_requis_v68`, N × S17 + E × plafond de l'étage, E = nombre
d'étages joués (N − 1, ou N avec `--etage-apres-derniere`) ; portée « course » refusée pour N > 1 ou un étage. Plafond de la
course : le montant requis, ou `--plafond-course-usd` (réel > 0, jamais au-delà du montant requis).

**Moteur réel : refusé par construction** dans cette version. Avant ce refus, tout interrupteur allumé en réel
(`tests_de_mort_reels` dès qu'un étage est configuré, `lecture_selection_generation_suivante` avec la lecture) exige une ligne de
GO (`GO_ID`, `--registre-go`) au montant requis, dont le **périmètre nomme chaque interrupteur allumé** ; puis le refus liste
les blocages (`BLOCAGES_REELS_V68`), dont l'additif des interrupteurs non épinglé (`ADDITIF_INTERRUPTEURS_V68 = (None, None)`).
Aucune variable d'environnement, aucun champ de configuration n'allume quoi que ce soit.

Codes : 0 sortie écrite ; 2 refus, arrêt (signal compris), plafond de la course atteint ou nœud (motif sur la sortie d'erreur).
"""

import importlib.util
import json
import os
import sys
import tempfile
import unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, RACINE)

_spec = importlib.util.spec_from_file_location("ideation_v8_lanceur_pour_v68", os.path.join(ICI, "ideation_v8.py"))
v8 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(v8)  # instance propre (R12 : le lanceur v8 n'est pas touché)

from pole import configuration_v56 as cfg  # noqa: E402
from pole import course2_v56 as c56  # noqa: E402
from pole import course2_v68 as c68  # noqa: E402
from pole import gardes_e0_v56 as ge  # noqa: E402
from pole.etage_entre_generations_v56 import exiger_machine_jetable_v56  # noqa: E402
from pole.noyau_v56 import ArretParSignal  # noqa: E402

VERSION = "lanceur-ideation-v68 (course 2 v68 : sélection lue en objet, étage après la dernière génération, budget de la course)"
INTERRUPTEURS = ("lecture_selection_generation_suivante", "tests_de_mort_reels")  # noms du lanceur de course v10
ADDITIF_INTERRUPTEURS_V68 = (None, None)  # (chemin, sha256) de l'additif des interrupteurs : à venir (nœud de Lazar)
BLOCAGES_REELS_V68 = (
    "additif des interrupteurs non épinglé (ADDITIF_INTERRUPTEURS_V68 = (None, None)) : ce qui est servi, à qui, la sélection vide, "
    "les champs de fiche de la course d'auto-conception (nœuds de Lazar, points 2 et 14 de l'ordre v3)",
    "lanceur de course v11 absent : bornes des relais, parts au pire et crédits calculés pour une génération (lanceur v10)",
    "bac à sable réel jamais joué avec l'étage v5 (tests_de_mort_v5 : « le vrai bac à sable n'a pas été rejoué »)",
    "machine jetable (R-640) : location, relais hors de la machine, devis — nœud et dépense",
    "aucune ligne de GO de calcul pour une course allumée (devis à écrire, mot de Lazar)",
)


class MoteurReelRefuseV68(RuntimeError):
    """Moteur réel demandé au lanceur v68 : refusé par construction (blocages listés)."""


def construire_analyseur():
    a = v8.construire_analyseur()
    a.prog = "ideation_v68.py"
    a.add_argument("--lecture-selection", choices=("oui", "non"), default="non")
    a.add_argument("--etage-apres-derniere", action="store_true")
    a.add_argument("--selection-vide", choices=c68.SELECTION_VIDE, default=c68.SELECTION_VIDE_DEFAUT)
    a.add_argument("--plafond-course-usd", type=float)
    return a


def normaliser(texte):
    t = unicodedata.normalize("NFKD", str(texte).lower())
    return "".join(c for c in t if not unicodedata.combining(c)).replace("-", "")


def interrupteurs_allumes(etage_present, lecture_selection):
    """Les interrupteurs que la course allume (noms du lanceur v10) : tout étage joue des tests de mort ; la lecture sert."""
    return tuple(n for n, oui in zip(INTERRUPTEURS, (lecture_selection, etage_present)) if oui)


def garder_moteur_reel_v68(environnement, registre_go, montant_usd, allumes):
    """Moteur réel : ligne de GO nominative pour chaque interrupteur allumé, puis **refus par construction** (toujours)."""
    if allumes:
        if not registre_go:
            raise cfg.GoRefuse("A15 : --registre-go exigé : interrupteur(s) allumé(s) en réel (" + ", ".join(allumes) + ")")
        ligne = cfg.verifier_go_v56(environnement.get("GO_ID"), registre_go, montant_usd)
        perimetre = normaliser(ligne.get("perimetre", ""))
        manquants = [i for i in allumes if normaliser(i) not in perimetre]
        if manquants:
            raise cfg.GoRefuse(f"A15 : la ligne {ligne.get('identifiant')} ne nomme pas l'interrupteur allumé "
                               + ", ".join(manquants) + " dans son périmètre : rien ne s'allume en réel sans accord nominatif")
    motifs = list(BLOCAGES_REELS_V68)
    if ADDITIF_INTERRUPTEURS_V68 != (None, None):
        motifs = motifs[1:]
    raise MoteurReelRefuseV68("moteur réel refusé par construction (lanceur v68) :\n- " + "\n- ".join(motifs))


def adaptateurs_simules_v68(conf, fournisseurs):
    from pole.simulation_v68 import AdaptateurSimuleV68
    s = conf.get("simulation") or {}
    if "cout_par_appel_usd" not in s:
        raise cfg.ConfigurationRefusee("moteur simulé : simulation.cout_par_appel_usd exigé (coût fictif, aucun défaut)")
    noms = set(fournisseurs) | ({conf["etage_tests_de_mort"]["fournisseur"]} if conf.get("etage_tests_de_mort") else set())
    return {n: AdaptateurSimuleV68(champs_fiche=conf["champs_fiche"], items=conf["items_juge"], champ_titre=conf["champ_titre"],
                                   cout_par_appel_usd=s["cout_par_appel_usd"]) for n in sorted(noms)}


def executer(args, environnement=None):
    env = os.environ if environnement is None else environnement
    conf_chemin, sortie = args.course_2
    conf = cfg.lire_configuration_v56(conf_chemin)
    spec = cfg.verifier_specification_v56(conf)
    if args.generations is None:
        raise cfg.ConfigurationRefusee("--generations N exigé avec --course-2 (aucun défaut)")
    c56.verifier_configuration_generation_v56(conf)
    n = args.generations
    etage_conf = conf.get("etage_tests_de_mort") or None
    lecture = args.lecture_selection == "oui"
    regime = c68.verifier_regime_v68(conf, nombre_generations=n, lecture_selection=lecture, etage_present=etage_conf is not None,
                                     etage_apres_derniere=bool(args.etage_apres_derniere), selection_vide=args.selection_vide,
                                     plafond_etage_usd=(etage_conf or {}).get("plafond_etage_usd"))
    montant = regime["montant_requis_usd"]
    plafond_course = montant if args.plafond_course_usd is None else args.plafond_course_usd
    if not (plafond_course > 0) or plafond_course > montant + 1e-9:
        raise cfg.ConfigurationRefusee(f"--plafond-course-usd : réel > 0 et ≤ montant requis ({montant:g} USD) exigé")
    decl, params = c56.declarer_bras_v56(conf)
    table_r5 = ge.rejouer_gardes_v56(conf, decl, params, plan="course", etage1=None, specification=spec)
    permis = (etage_conf or {}).get("environnement_permis") or ()
    if etage_conf:
        exiger_machine_jetable_v56(env, permis_en_plus=permis)
    allumes = interrupteurs_allumes(etage_conf is not None, lecture)
    if args.moteur == "reel":
        garder_moteur_reel_v68(env, args.registre_go, montant, allumes)  # lève toujours
    if args.verifier_seulement:
        print(json.dumps({"version": VERSION, "plan": "course", "configuration_sha256": conf["empreinte_configuration"],
                          "specification": spec, "generations": n, "regime": regime, "montant_requis_go_usd": montant,
                          "plafond_course_usd": plafond_course, "interrupteurs": list(allumes) or "éteints", "bras": decl,
                          "table_r5_e0": [{k: x[k] for k in ("ligne", "statut")} for x in table_r5], "etage": bool(etage_conf),
                          "ecriture": "aucune", "appel": "aucun"}, ensure_ascii=False, indent=1))
        return 0
    if args.moteur is None:
        raise cfg.ConfigurationRefusee("--moteur simule exigé (ou --verifier-seulement) ; le moteur réel est refusé en v68")
    fournisseurs = c68.GenerationV68.fournisseurs_requis(conf)
    base_sessions = tempfile.mkdtemp(prefix="pole-sessions-v68-", dir=env.get("TMPDIR") or None)  # hors de la sortie (CL19-04)
    adaptateurs = adaptateurs_simules_v68(conf, fournisseurs)
    etage = v8.base.reglages_etage(conf, "simule", adaptateurs) if etage_conf else None
    go = {"moteur": "simule", "go": "sans objet (aucune dépense)"}
    bilan = c68.executer_course_v68(conf, sortie, adaptateurs, nombre_generations=n, go=go, lecture_selection=lecture,
                                    etage_apres_derniere=bool(args.etage_apres_derniere), plafond_course_usd=plafond_course,
                                    etage=etage, environnement=env, racine_sessions=base_sessions, portes=None,
                                    specification=spec, selection_vide=args.selection_vide)
    print(json.dumps({"version": VERSION, "regime": regime["nom"], "interrupteurs": list(allumes) or "éteints", "bilan": bilan},
                     ensure_ascii=False, default=str))
    return 0


def principal(argv=None, environnement=None, etage1=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--course-2" not in argv:
        return v8.principal(argv, environnement, etage1)  # pré-pilote et versions précédentes : le lanceur v8, inchangé
    args = construire_analyseur().parse_args(argv)
    try:
        return executer(args, environnement)
    except (Exception, ArretParSignal, KeyboardInterrupt) as e:  # noqa: BLE001 — tout refus, arrêt (signal compris) ou nœud rend 2
        print(json.dumps({"arret": type(e).__name__ + " : " + str(e)[:3000]}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(principal())
