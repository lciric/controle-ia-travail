"""Ouverture de la lecture du barreau 5 sur une table à noms suffixés, v1 : la variante accordée d'avance par
GO-2026-11-22-147. Code neuf (R12), écrit le 2026-11-22 ; il ne crée, n'arrête ni ne détruit rien, n'atteint pas le réseau.

Pièce qui commande : erratum de chaîne de la relecture décisive du barreau 5, v2 (`01298f0f…`), § 5 ; précisions 1 à 3 de
la vérification des corrections (`verification-corrections-erratum-chaine-b5f-v1.md`).

Le fait (§ 5.1) : le nom formé d'une famille est sa base (`T01` à `T10`), suivie de `-x1` si son instance est citée par la
ligne de relance, puis de `-r1` après un retirage. Si la table des étiquettes a été écrite sur les noms formés, les deux
entrées figées de `lecture_v1` la refusent (`preparer`, par `prefixe_de_copie` ; `ouvrir`, par `garde_d_ouverture`), et
une table traduite à la main serait refusée par la cohérence du sel et par l'engagement.

La règle (§ 5.2), décidée sur la table engagée T elle-même, après ses gardes figées (cohérence, empreinte égale à
`ENGAGEMENT-B5F` ; dans `ouvrir` seulement, égalité à `OUVERTURE-B5F` et dates) :
1. graphie : chaque famille de T se lit par `_GRAPHIE` ; sinon refus (« suffixe inconnu ») ;
2. une seule graphie par base ; sinon refus (« deux graphies pour une famille ») ;
3. copie lue c(base) : celle que donne la formation par les fonctions figées, **base par base** (précision 3), jamais à
   partir des graphies de T : `variante` et `preparer` la calculent par `_familles_formees(racine_formation, base, relance)` ;
   `ouvrir` la prend au champ « copie » du résumé de la formation, contrôlé par `exiger_copie_lue` ;
4. décision : toutes les familles de T sont des bases → variante (a) (l'entrée figée lit, ce module refuse) ; sinon chaque
   famille de T égale c(base) → variante (b) ; sinon refus, nœud ;
5. traces : E_a et E_b, empreintes de T dans son propre ordre, la famille de chaque ligne remplacée par sa base (E_a) ou
   par c(base) (E_b), noms, membres et sel inchangés ; la trace de la variante retenue égale l'engagement.
En (b) seulement : T_nu = T, chaque famille réduite à sa base ; puis les gardes figées des l. 529 à 532 sur T_nu ; ni la
cohérence ni l'égalité à l'engagement ne sont jouées sur T_nu (elles l'ont été sur T).

Ce qui est recomposé (§ 5.4), ligne pour ligne : `preparer`, `garde_d_ouverture` et `ouvrir` de `lecture_v1`, à trois
remplacements près (gardes de table sur T ; règle et traduction avant les gardes de ligne, jouées sur T_nu ; garde du code
au commit remplacée par (d), (d'), (c'1), (c'2) et (b') au registre du commit prouvé que cite `SCORES-B5F`, précision 1 :
`code_au_commit_v3`). En (b), `a_garde_d_ouverture.code` porte `{"commit", "arbre_gele": "égal hors des listes fermées de
la v2 et de l'erratum", "commit_de_code", "erratum_sha256"}` (précision 2) ; le fichier scellé `traduction-table-b5f.json`
est écrit à côté du résultat. `lecture_v1.py` reste à son empreinte, appelée. Les objets privés employés (`_exiger`,
`_lire_json`, `_familles_formees`, `_convertible`, `_registre_au_commit`, `_NOM_OPAQUE`, `_CODE_LECTURE`, `_SCORES_LIGNE`
de `lecture_v1` ; `_empreinte_engagee` de `engagement_v1`) sont récrits à l'identique, avec un essai d'égalité.

Bornes (C6) : `variante` et `preparer` vérifient la cohérence, l'engagement, la règle et l'épinglage (quand la racine est
donnée), sans exiger `OUVERTURE-B5F` ; `ouvrir` vérifie tout. Sans racine, les trois fonctions n'existent que pour les
essais : l'entrée (`_main`, `scripts/lancer_b5f_ouverture_suffixes_v1.sh`) exige la racine et refuse d'être jouée depuis
un autre arbre que celui qu'elle vérifie.

Épreuves : `tests/test_ouverture_suffixes_v1.py`, écrites avant ce module.
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import sceller
from . import engagement_v1 as en
from .commande_lecture_v3 import ERRATUM_SHA256, commit_de_code_verifie
from .lecture_v1 import (APPRENTISSAGE, FORMAT_RESULTAT, MEMBRES, TENUES, TEXTE, TEXTE_SHA256, charger_arbre,
                         charger_entrees, couts_depuis_formation, exiger_alignement, exiger_arbre,
                         exiger_arbre_sans_etiquettes, exiger_copie_lue, instance_de, lire, lire_registre_de_lecture,
                         partition_des_plis, prefixe_de_copie, programme_sha256, relance_du_registre,
                         resume_formation_depuis_branche)

COMMANDE = "python -m controle_ia.barreau5_familles.ouverture_suffixes_v1"
MODULE = "src/controle_ia/barreau5_familles/ouverture_suffixes_v1.py"
LANCEUR = "scripts/lancer_b5f_ouverture_suffixes_v1.sh"
FICHIER_TRADUCTION = "traduction-table-b5f.json"
FORMAT_TRADUCTION = "b5f-traduction-table-v1"
ARBRE_GELE_B = "égal hors des listes fermées de la v2 et de l'erratum"
_GRAPHIE = re.compile(r"(?P<base>T(?:0[1-9]|10))(?P<relance>-x1)?(?P<retirage>-r1)?")
# objets privés récrits à l'identique (`lecture_v1._NOM_OPAQUE`, `_CODE_LECTURE`, `_SCORES_LIGNE`)
_SHA = r"[0-9a-f]{64}"
_NOM_OPAQUE = re.compile(r"X-(?:0[1-9]|[1-9][0-9])")
_CODE_LECTURE = re.compile(rf"commit (?P<commit>[0-9a-f]{{40}}) ; lecture sha256 (?P<lecture>{_SHA})")
_SCORES_LIGNE = re.compile(rf"commit (?P<commit>[0-9a-f]{{40}}) ; inventaire sha256 (?P<inventaire>{_SHA})")


# --- objets privés récrits à l'identique ---------------------------------------------------------------------------------

def _exiger(condition: bool, motif: str) -> None:
    if not condition:
        raise GardeArret(motif)


def _lire_json(chemin: Path, quoi: str):
    try:
        return json.loads(Path(chemin).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        raise GardeArret(f"{quoi} : {chemin} absent ou illisible") from None


def _convertible(x):
    if isinstance(x, dict):
        return {str(k): _convertible(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_convertible(v) for v in x]
    if isinstance(x, np.ndarray):
        return [_convertible(v) for v in x.tolist()]
    if isinstance(x, (np.floating,)):
        return float(x)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, float) and not math.isfinite(x):
        return None
    return x


def _familles_formees(racine_formation: Path, famille: str, relance: list[int] | None) -> tuple[Path, str]:
    """Le dossier de la copie lue d'une famille, sous `donnees/<marche>/` de la branche de la formation : la marche de son
    instance (`…-b5f-formation-<n>`, ou `…-<n>-x1` si l'instance est relancée), le dossier `<copie>` ou `<copie>-r1` qui
    porte les épisodes d'évaluation (un seul) ; toute autre copie est refusée."""
    n = instance_de(famille)
    suffixe = "-x1" if relance and n in relance else ""
    marches = sorted(p for p in (Path(racine_formation) / "donnees").glob(f"*-b5f-formation-{n}{suffixe}")
                     if re.fullmatch(rf"[0-9]{{8}}-[0-9]{{6}}-b5f-formation-{n}{re.escape(suffixe)}", p.name))
    _exiger(len(marches) == 1, f"famille {famille} : {len(marches)} marches de l'instance {n}{suffixe}, une attendue")
    prefixe = prefixe_de_copie(famille, relance)
    candidats = [d for d in (marches[0] / prefixe, marches[0] / f"{prefixe}-r1")
                 if d.is_dir() and any(d.glob("evaluation-*.jsonl"))]
    _exiger(len(candidats) == 1, f"famille {famille} : {len(candidats)} copies formées sous {marches[0].name}, une attendue")
    return candidats[0], exiger_copie_lue(famille, candidats[0].name, relance)


def _registre_au_commit(racine: Path, commit: str) -> str:
    import subprocess

    _exiger(re.fullmatch(r"[0-9a-f]{40}", str(commit)) is not None, "commit du registre (40 signes) attendu")
    vu = subprocess.run(["git", "-C", str(racine), "show", f"{commit}:{en.REGISTRE_PROPRE}"], capture_output=True,
                        text=True)
    _exiger(vu.returncode == 0, f"registre propre absent du commit {commit[:12]}")
    return vu.stdout


def _empreinte_engagee(lignes: dict) -> str:
    if "ENGAGEMENT-B5F" not in lignes:
        raise GardeArret("engagement absent du registre propre (liste d'arrêt, point 9)")
    m = re.fullmatch(r"sha256 ([0-9a-f]{64})", lignes["ENGAGEMENT-B5F"]["contenu"])
    if m is None:
        raise GardeArret("ligne ENGAGEMENT-B5F : « sha256 <64 signes> » attendu")
    return m.group(1)


# --- la règle (§ 5.2) ------------------------------------------------------------------------------------------------------

def base_de(famille: str) -> str:
    """Point 1 : la base d'une famille écrite `T<nn>[-x1][-r1]` ; toute autre graphie : refus."""
    m = _GRAPHIE.fullmatch(str(famille)) if isinstance(famille, str) else None
    _exiger(m is not None, f"table : famille {famille!r} : suffixe inconnu (graphie T01 à T10, suivie au plus de -x1 puis "
            "de -r1) : refus")
    return m["base"]


def graphies(table: list[dict]) -> dict[str, str]:
    """Points 1 et 2 : base → graphie, une seule graphie par base."""
    vues = {}
    for x in table:
        b = base_de(x["famille"])
        _exiger(vues.setdefault(b, x["famille"]) == x["famille"],
                f"table : deux graphies pour une famille ({vues[b]} et {x['famille']}) : refus")
    return vues


def decider(table: list[dict], copies: dict[str, str], engagement: str) -> dict:
    """Points 4 et 5, sur T elle-même (rangée ou non par nom). `copies` : base → c(base), calculée base par base par les
    fonctions figées. Rend la variante, les traces E_a et E_b, l'engagement et la table de traduction (graphie → base)."""
    vues = graphies(table)
    for b in vues:
        _exiger(b in copies, f"table : copie lue de {b} inconnue : refus")
    e_a = en.empreinte_table([dict(x, famille=base_de(x["famille"])) for x in table])
    e_b = en.empreinte_table([dict(x, famille=copies[base_de(x["famille"])]) for x in table])
    if all(g == b for b, g in vues.items()):
        variante, trace = "a", e_a
    elif all(g == copies[b] for b, g in vues.items()):
        variante, trace = "b", e_b
    else:
        raise GardeArret("table : graphie hors règle, ni (a) ni (b) (ni toutes les familles nues, ni chaque famille à sa "
                         f"copie lue {dict(sorted(copies.items()))}) : refus, nœud (erratum de chaîne, § 5.2 et § 5.7)")
    _exiger(trace == engagement, f"table : trace de la variante ({variante}) ≠ engagement : refus")
    return {"format": FORMAT_TRADUCTION, "variante": variante, "E_a": e_a, "E_b": e_b, "engagement": engagement,
            "traduction": {g: b for b, g in sorted(vues.items(), key=lambda bg: bg[1])},
            "copies": {b: copies[b] for b in sorted(vues)}, "erratum_sha256": ERRATUM_SHA256}


def table_traduite(table: list[dict], decision: dict) -> list[dict]:
    """§ 5.3 : en (b) seulement, T_nu (chaque famille réduite à sa base ; noms, membres, sel et ordre inchangés)."""
    _exiger(decision["variante"] == "b", "table nue : variante (a) : l'entrée figée lit sans traduction "
            "(scripts/lancer_b5f_lecture_v1.sh, depuis l'arbre au code figé) ; ce module refuse")
    return [dict(x, famille=decision["traduction"][x["famille"]]) for x in table]


def exiger_lignes_du_plan(table: list[dict]) -> None:
    """Les gardes figées des l. 529 à 532 (`garde_d_ouverture`), récrites telles quelles, pour `preparer` sur T_nu."""
    for x in table:
        _exiger(x["famille"] in TENUES and x["membre"] in MEMBRES and _NOM_OPAQUE.fullmatch(x["nom"]) is not None,
                f"table : ligne {x['nom']}/{x['famille']}/{x['membre']} hors du plan")
    _exiger(len({(x["famille"], x["membre"]) for x in table}) == len(table), "table : adaptateur en double")


def copies_de_la_formation(racine_formation: Path, table: list[dict], relance: list[int] | None) -> dict[str, str]:
    """c(base), base par base, par `_familles_formees` (précision 3)."""
    return {b: _familles_formees(racine_formation, b, relance)[1] for b in sorted(graphies(table))}


def copies_du_resume(formation: dict, table: list[dict], relance: list[int] | None) -> dict[str, str]:
    """c(base), base par base, au champ « copie » du résumé de la formation, contrôlé par `exiger_copie_lue`."""
    sortie = {}
    for b in sorted(graphies(table)):
        _exiger(isinstance(formation.get(b), dict), f"résumé de la formation : famille {b} absente : refus")
        sortie[b] = exiger_copie_lue(b, formation[b].get("copie"), relance)
    return sortie


# --- l'épinglage, au registre du commit prouvé (§ 5.5 ; précision 1) -------------------------------------------------------

def code_au_commit_v3(racine: Path, texte_registre: str) -> dict:
    """Le code joué est celui du commit v3 épinglé : au registre du commit prouvé que cite `SCORES-B5F` (celui du commit de
    la marche, que les commits de sortie gardent), (d) donne le commit v2, (d') le commit v3 ; puis (c'1) sur le commit de
    `CODE-LECTURE-B5F` du registre donné, (c'2) et (b'). Rend le contenu de `a_garde_d_ouverture.code` (précision 2)."""
    lignes = en.lignes_du_registre(texte_registre)
    _exiger("SCORES-B5F" in lignes, "registre propre : ligne SCORES-B5F absente : commit prouvé inconnu, épinglage "
            "invérifiable : refus")
    sc = _SCORES_LIGNE.fullmatch(lignes["SCORES-B5F"]["contenu"])
    cl = _CODE_LECTURE.fullmatch(lignes.get("CODE-LECTURE-B5F", {}).get("contenu", ""))
    _exiger(sc is not None and cl is not None, "registre propre : SCORES-B5F ou CODE-LECTURE-B5F illisible : refus")
    prouve = _registre_au_commit(racine, sc["commit"])
    v2, v3 = commit_de_code_verifie(racine, cl["commit"], prouve)
    return {"commit": cl["commit"], "arbre_gele": ARBRE_GELE_B, "commit_de_code": v3, "erratum_sha256": ERRATUM_SHA256}


# --- variante, preparer -----------------------------------------------------------------------------------------------------

def variante(racine_formation: Path, texte_registre: str, table_f: Path, racine: Path | None = None) -> dict:
    """Cohérence et engagement de T, épinglage (si `racine`), règle ; rend la décision (variante (a) ou (b), traces). Jouée
    dans tous les cas (C14) ; n'exige pas `OUVERTURE-B5F` ; n'écrit rien."""
    table = _lire_json(table_f, "table des étiquettes")
    en.exiger_table_coherente(table)
    engagement = _empreinte_engagee(en.lignes_du_registre(texte_registre))
    _exiger(en.empreinte_table(table) == engagement, "table : empreinte ≠ ENGAGEMENT-B5F (engagement) : refus, aucune "
            "traduction")
    if racine is not None:
        code_au_commit_v3(racine, texte_registre)
    copies = copies_de_la_formation(racine_formation, table, relance_du_registre(texte_registre))
    return decider(table, copies, engagement)


def table_nue_de_preparer(racine_formation: Path, texte_registre: str, table: list[dict], racine: Path | None) -> list:
    """Ce que `preparer` recomposé ajoute après la cohérence de T : engagement, épinglage, règle (refus en (a)), T_nu et
    ses gardes de ligne."""
    engagement = _empreinte_engagee(en.lignes_du_registre(texte_registre))
    _exiger(en.empreinte_table(table) == engagement, "table : empreinte ≠ ENGAGEMENT-B5F (engagement) : refus, aucune "
            "traduction")
    if racine is not None:
        code_au_commit_v3(racine, texte_registre)
    decision = decider(table, copies_de_la_formation(racine_formation, table, relance_du_registre(texte_registre)),
                       engagement)
    table_nu = table_traduite(table, decision)
    exiger_lignes_du_plan(table_nu)
    return table_nu


def preparer(racine_formation: Path, texte_registre: str, table_f: Path, sortie: Path, racine: Path | None = None) -> dict:
    """`lecture_v1.preparer`, ligne pour ligne, la table T réduite à T_nu après sa cohérence (`table_nue_de_preparer`)."""
    sortie = Path(sortie)
    _exiger(not sortie.exists(), f"{sortie} existe déjà (R12)")
    table = _lire_json(table_f, "table des étiquettes")
    en.exiger_table_coherente(table)
    table = table_nue_de_preparer(racine_formation, texte_registre, table, racine)
    couts = couts_depuis_formation(racine_formation, texte_registre, table)
    formation = resume_formation_depuis_branche(racine_formation, texte_registre, table)
    sortie.mkdir(parents=True)
    rendu = {}
    for nom, x in (("couts.json", couts), ("formation.json", formation)):
        p = sortie / nom
        p.write_text(json.dumps(x, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        rendu[nom] = sceller(p)
    return rendu


# --- garde d'ouverture et ouverture -----------------------------------------------------------------------------------------

def garde_d_ouverture(texte_registre: str, table: list[dict], arbre: Path, formation: dict, racine: Path | None = None
                      ) -> dict:
    """`lecture_v1.garde_d_ouverture`, ligne pour ligne : gardes de table sur T ; règle et traduction avant les gardes de
    ligne, jouées sur T_nu ; garde du code au commit remplacée par `code_au_commit_v3`."""
    reg = lire_registre_de_lecture(texte_registre)
    sha = programme_sha256()
    _exiger(sha == reg["code_lecture"]["lecture"], f"programme de lecture d'empreinte {sha[:12]}… ≠ CODE-LECTURE-B5F "
            f"{reg['code_lecture']['lecture'][:12]}… : aucune ouverture (liste d'arrêt, point 10)")
    code = code_au_commit_v3(racine, texte_registre) if racine is not None else None
    en.exiger_table_coherente(table)
    v = en.verifier_table_a_l_ouverture(table, None, reg["ouverture"]["instant"], lignes=reg["lignes"])
    _exiger(en.empreinte_table(table) == reg["ouverture"]["table"], "table reçue par l'ouvreur ≠ OUVERTURE-B5F : refus")
    decision = decider(table, copies_du_resume(formation, table, reg["relance"]), reg["engagement"])
    table_nu = table_traduite(table, decision)
    for x in table_nu:
        _exiger(x["famille"] in TENUES and x["membre"] in MEMBRES and _NOM_OPAQUE.fullmatch(x["nom"]) is not None,
                f"table : ligne {x['nom']}/{x['famille']}/{x['membre']} hors du plan")
    _exiger(len({(x["famille"], x["membre"]) for x in table_nu}) == len(table_nu), "table : adaptateur en double")
    ar = exiger_arbre(arbre, reg["scores"]["inventaire"])
    exiger_arbre_sans_etiquettes(arbre, reg["engagement"])
    return {"registre": reg, "programme_sha256": sha, "code": code, "table": v, "arbre": ar, "decision": decision,
            "table_nu": table_nu}


def ecrire_traduction(sortie: Path, decision: dict) -> str:
    """Le fichier scellé `traduction-table-b5f.json`, à côté du résultat (§ 5.3)."""
    p = Path(sortie) / FICHIER_TRADUCTION
    _exiger(not p.exists(), f"{p} existe déjà (R12)")
    p.write_text(json.dumps(decision, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return sceller(p)


def ouvrir(arbre: Path, table_f: Path, couts_f: Path, formation_f: Path, texte_registre: str, sortie: Path,
           racine: Path | None = None, source_registre: str = "") -> dict:
    """`lecture_v1.ouvrir`, ligne pour ligne : la garde recomposée (qui reçoit le résumé de la formation, pour c(base)),
    puis T_nu à la place de T ; le fichier de traduction écrit et scellé après le résultat."""
    sortie = Path(sortie)
    _exiger(not sortie.exists(), f"{sortie} existe déjà (R12)")
    table, couts, formation = charger_entrees(table_f, couts_f, formation_f)
    garde = garde_d_ouverture(texte_registre, table, arbre, formation, racine)
    table = garde["table_nu"]
    reg = garde["registre"]
    bilan = _lire_json(Path(arbre) / "bilan-relecture.json", "bilan de la relecture")
    taches = bilan.get("taches")
    _exiger(isinstance(taches, list) and bool(taches), "bilan de la relecture : tâches absentes")
    partition = partition_des_plis(taches, reg["entropie"])
    ch = charger_arbre(arbre, partition)
    for f, x in couts.items():
        if f in TENUES or f in APPRENTISSAGE:
            exiger_copie_lue(f, x.get("copie"), reg["relance"])
    for f, x in formation.items():
        if f in TENUES or f in APPRENTISSAGE:
            exiger_copie_lue(f, x.get("copie"), reg["relance"])
    alignement = exiger_alignement(table, formation, ch["intensites"])
    resultat = {"format": FORMAT_RESULTAT, "texte": TEXTE, "texte_sha256": TEXTE_SHA256,
                "a_garde_d_ouverture": {"programme_sha256": garde["programme_sha256"], "code": garde["code"],
                                        "source_registre": source_registre, "registre": {
                                            k: {"instant": v["instant"].strftime("%Y-%m-%dT%H:%M:%SZ"), "contenu": v["contenu"]}
                                            for k, v in reg["lignes"].items()},
                                        "table": garde["table"], "arbre": garde["arbre"], "alignement": alignement,
                                        "partition": [list(p) for p in partition], "relance": reg["relance"]}}
    resultat.update(lire(ch, table, couts, formation, reg["entropie"]))
    sortie.mkdir(parents=True)
    chemin = sortie / "resultat-lecture-b5f.json"
    chemin.write_text(json.dumps(_convertible(resultat), indent=1, ensure_ascii=False, sort_keys=True) + "\n",
                      encoding="utf-8")
    sha = sceller(chemin)
    ecrire_traduction(sortie, garde["decision"])
    return {"issue": resultat["g_issue"]["code"], "resultat": chemin, "sha256": sha, "contenu": resultat}


# --- l'entrée -----------------------------------------------------------------------------------------------------------

def exiger_module_joue_depuis(racine: Path) -> None:
    """Le module joué est celui de l'arbre que vérifie (b') : sinon l'épinglage porterait sur un arbre et le code joué en
    serait un autre."""
    if Path(__file__).resolve() != (Path(racine) / MODULE).resolve():
        raise GardeArret(f"ouverture à noms suffixés : module joué depuis un autre arbre que celui de la session ({racine}) : "
                         f"elle ne se joue que par {LANCEUR} de l'arbre de travail au commit v3")


def _main(argv: list[str]) -> int:
    formes = {"variante": 5, "preparer": 6, "ouvrir": 8}
    _exiger(bool(argv) and argv[0] in formes and len(argv) == formes[argv[0]],
            "attendu : variante RACINE COMMIT_REGISTRE BRANCHE_FORMATION TABLE.json | preparer RACINE COMMIT_REGISTRE "
            "BRANCHE_FORMATION TABLE.json SORTIE | ouvrir RACINE COMMIT_REGISTRE ARBRE TABLE.json COUTS.json "
            "FORMATION.json SORTIE")
    racine, commit = Path(argv[1]), argv[2]
    exiger_module_joue_depuis(racine)
    texte = _registre_au_commit(racine, commit)
    if argv[0] == "variante":
        rendu = variante(Path(argv[3]), texte, Path(argv[4]), racine)
    elif argv[0] == "preparer":
        rendu = preparer(Path(argv[3]), texte, Path(argv[4]), Path(argv[5]), racine)
    else:
        r = ouvrir(Path(argv[3]), Path(argv[4]), Path(argv[5]), Path(argv[6]), texte, Path(argv[7]), racine,
                   source_registre=f"commit {commit}")
        rendu = {"issue": r["issue"], "resultat": str(r["resultat"]), "sha256": r["sha256"]}
    print(json.dumps(rendu, ensure_ascii=False, sort_keys=True))
    return 0


__all__ = ["base_de", "graphies", "decider", "table_traduite", "exiger_lignes_du_plan", "copies_de_la_formation",
           "copies_du_resume", "code_au_commit_v3", "variante", "preparer", "garde_d_ouverture", "ouvrir",
           "ecrire_traduction"]


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"REFUS : {e}", file=sys.stderr)
        sys.exit(2)
