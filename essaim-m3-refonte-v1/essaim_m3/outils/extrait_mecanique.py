"""Extrait mécanique d'une course finie, sans aucun score (R1 ; constat PG2-01 du pilote Gemini).

Le dossier d'une course mêle, dans les mêmes fichiers, les statuts d'exécution et les scores : `resume.json`,
`index.jsonl`, `evenements.jsonl`, `rapport-vN.json`, et la sortie standard du lanceur (`cli.lancer` imprime `courbes`
et `scores_finaux`). Quand un préenregistrement interdit à tout humain de lire les scores avant un moment donné (par
exemple le scellement d'un autre préenregistrement), personne ne peut rien lire de la course sans voir un score.

Cet outil lit la course **à la machine** et écrit un extrait à **liste close** de champs — statuts d'exécution, appels
par espèce et par statut, coûts, durées, successeurs, relances, empreintes des arbres, compteurs de l'organisme — dont
toute clé de score est exclue deux fois : par les listes de champs copiés (allowlist), puis par une garde finale sur les
noms de clés (regex). Une clé interdite qui subsisterait fait échouer l'extraction (R5 : aucun repli silencieux).
L'extrait est écrit hors du dossier de la course, jamais réécrit (R12), avec son compagnon `.sha256` (R6).

v2 (CE4-04, CE4-06) : par génération et par ronde, les comptes par statut des entraînements, des recherches (par source)
et des téléchargements ; les rondes importées d'une course d'origine (bras B) marquées `importee` d'après l'index et
sorties des totaux (`totaux_hors_importees`). « Sans clé de score » : les valeurs que l'organisme écrit lui-même (noms
de fichiers, `erreurs` de son journal, déclaration de fin de conception) ne sont pas filtrées par leur contenu et peuvent
porter un score de développement qu'il a reçu ; elles sont bornées en nombre et en longueur.

Ce que l'extrait ne contient jamais : les scores du juge (`juge/`), les champs `score`, les métriques proposées par
l'organisme, ses réponses aux tâches (`reponses_test.json`, `details_votes_test`), les textes des appels (`appels/`),
les termes saturés de son bilan spectral (mots de ses propres sorties), le `historique` qu'il a reçu.

Usage : `python -m essaim_m3.outils.extrait_mecanique --course DOSSIER --sortie FICHIER.json`.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import pathlib
import re
import sys

from ..noyau import archive as _archive

VERSION_EXTRAIT = 2  # v2 (CE4-04, CE4-06) : statuts des services par génération ; rondes importées marquées et hors des totaux

# Garde finale : aucune clé de l'extrait ne doit contenir l'un de ces motifs (noms de clés, insensible à la casse).
CLES_INTERDITES = re.compile(r"score|courbe|metrique|vote|terme|verite|etiquette|historique", re.IGNORECASE)

# Clés copiées de `resume.json` d'une génération (archive) ; tout le reste est ignoré.
CHAMPS_RESUME = ("lignee", "generation", "phase", "statut", "n_appels", "cout_usd", "refus_noyau", "appels_simultanes_max",
                 "successeur", "problemes_successeur", "n_reponses_test", "gel", "impose", "famille", "relance",
                 "n_recherches", "n_entrainements", "n_telechargements", "invalide", "non_conformes", "anomalie_noyau",
                 "empreinte_organisme", "n_elements_ecartes", "elements_ecartes", "quand_utc", "chemin", "importee", "course_origine",
                 "question_ouverte",  # {posee, reponse, octets, sha256, probleme} : jamais le contenu de la réponse
                 "indisponibles")     # CE4-02 : demandes d'un service non servi, par opération
# Clés copiées du dictionnaire `execution` du résumé (le `statut` déclaré par l'organisme n'est copié que par son code).
CHAMPS_EXECUTION = ("code", "code_retour", "duree_s", "delai_depasse", "isolation_reseau", "uid", "espaces_noms",
                    "rlimit_as_refuse", "code_origine", "anomalie", "non_conformes", "tmp_prives", "appels_en_vol_non_finis")
# Clés copiées de `journal_generation.json` écrit par l'organisme de Gemini (v3) dans son dossier de travail, s'il existe.
CHAMPS_ORGANISME = ("version", "generation", "lignee", "n_castes_recrutees", "n_taches_test", "n_taches_test_repondues",
                    "bascule_parallele_a_la_tache", "temps_s")
CHAMPS_CASTE = ("id_caste", "espece", "mode", "role")
CHAMPS_COMPTEURS = ("tentatives", "appels_ok", "appels_echec", "echecs_par_statut", "cout_total_usd")
CHAMPS_BILAN_SPECTRAL = ("n_textes", "capacite_shannon", "gain_marginal", "similarite_moyenne")
# Clés copiées du dernier `rapport-vN.json` ; `courbes`, `scores_finaux`, `generations` (doublon de l'index) sont exclus.
CHAMPS_RAPPORT = ("fin_utc", "depense_totale_usd", "n_appels_total", "generations_invalidees", "rondes_conception",
                  "rondes_conception_importees")
CHAMPS_LIGNEE_RAPPORT = ("famille", "generation", "active", "impose", "fin", "uid", "conception_finie")
ERREURS_MAX, ERREUR_CARACTERES_MAX = 20, 200


class ExtraitInvalide(RuntimeError):
    """Une clé interdite subsiste dans l'extrait, ou la course n'est pas lisible : rien n'est écrit."""


def _lire_json(chemin: pathlib.Path):
    return json.loads(pathlib.Path(chemin).read_text(encoding="utf-8"))


def _lire_jsonl(chemin: pathlib.Path) -> list[dict]:
    if not pathlib.Path(chemin).exists():
        return []
    return [json.loads(l) for l in pathlib.Path(chemin).read_text(encoding="utf-8").splitlines() if l.strip()]


def filtrer_cles(objet):
    """Copie récursive d'un objet JSON sans aucune clé dont le nom contient un motif interdit (à tous les niveaux)."""
    if isinstance(objet, dict):
        return {k: filtrer_cles(v) for k, v in objet.items() if not CLES_INTERDITES.search(str(k))}
    if isinstance(objet, list):
        return [filtrer_cles(x) for x in objet]
    return objet


def cles_interdites_presentes(objet, prefixe: str = "") -> list[str]:
    """Chemins des clés interdites présentes dans un objet JSON (garde finale ; vide si l'extrait est propre)."""
    trouvees = []
    if isinstance(objet, dict):
        for k, v in objet.items():
            chemin = f"{prefixe}.{k}" if prefixe else str(k)
            if CLES_INTERDITES.search(str(k)):
                trouvees.append(chemin)
            trouvees.extend(cles_interdites_presentes(v, chemin))
    elif isinstance(objet, list):
        for i, x in enumerate(objet):
            trouvees.extend(cles_interdites_presentes(x, f"{prefixe}[{i}]"))
    return trouvees


def _sous_dict(d: dict, cles) -> dict:
    return {k: d.get(k) for k in cles if k in d}


def resume_appels(lignes: list[dict]) -> dict:
    """Comptes du journal des appels du noyau (statuts, espèces, modèles servis, coûts, usage, durées) ; aucun texte."""
    par_espece: dict[str, dict] = {}
    par_statut: dict[str, int] = {}
    usage: dict[str, dict] = {}
    max_tokens: dict[str, int] = {}
    durees = []
    cout = 0.0
    debuts, fins = [], []
    for l in lignes:
        esp, st = str(l.get("espece")), str(l.get("statut"))
        e = par_espece.setdefault(esp, {"n": 0, "par_statut": {}, "modeles_servis": []})
        e["n"] += 1
        e["par_statut"][st] = e["par_statut"].get(st, 0) + 1
        if l.get("modele_servi") and l["modele_servi"] not in e["modeles_servis"]:
            e["modeles_servis"].append(l["modele_servi"])
        par_statut[st] = par_statut.get(st, 0) + 1
        cout += float(l.get("cout_usd") or 0.0)
        u = usage.setdefault(esp, {})
        for k, v in (l.get("usage") or {}).items():
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                u[k] = u.get(k, 0) + v
        mt = str(l.get("max_tokens"))
        max_tokens[mt] = max_tokens.get(mt, 0) + 1
        try:
            d0 = _dt.datetime.fromisoformat(str(l["debut_utc"]).replace("Z", "+00:00"))
            d1 = _dt.datetime.fromisoformat(str(l["fin_utc"]).replace("Z", "+00:00"))
            durees.append((d1 - d0).total_seconds())
            debuts.append(l["debut_utc"])
            fins.append(l["fin_utc"])
        except (KeyError, ValueError, TypeError):
            pass
    for e in par_espece.values():
        e["modeles_servis"] = sorted(e["modeles_servis"])
    return {"n": len(lignes), "par_statut": dict(sorted(par_statut.items())), "par_espece": dict(sorted(par_espece.items())),
            "cout_usd": round(cout, 6), "usage_par_espece": dict(sorted(usage.items())),
            "max_tokens_demandes": dict(sorted(max_tokens.items())),
            "durees_s": ({"n": len(durees), "min": round(min(durees), 3), "max": round(max(durees), 3),
                          "somme": round(sum(durees), 3)} if durees else None),
            "premier_debut_utc": (min(debuts) if debuts else None), "derniere_fin_utc": (max(fins) if fins else None)}


def extrait_organisme(journal: dict) -> dict:
    """Compteurs du `journal_generation.json` de l'organisme de Gemini (v3) : liste close, aucun texte de réponse."""
    e = _sous_dict(journal, CHAMPS_ORGANISME)
    if isinstance(journal.get("castes"), list):
        e["castes"] = [_sous_dict(c, CHAMPS_CASTE) for c in journal["castes"] if isinstance(c, dict)]
    if isinstance(journal.get("compteurs_appels"), dict):
        e["compteurs_appels"] = _sous_dict(journal["compteurs_appels"], CHAMPS_COMPTEURS)
    if isinstance(journal.get("bilan_spectral"), dict):
        e["bilan_spectral"] = _sous_dict(journal["bilan_spectral"], CHAMPS_BILAN_SPECTRAL)
    erreurs = journal.get("erreurs")
    if isinstance(erreurs, list):
        e["n_erreurs"] = len(erreurs)
        e["erreurs"] = [str(x)[:ERREUR_CARACTERES_MAX] for x in erreurs[:ERREURS_MAX]]
    return e


def _mot(x, n: int = 40) -> str:
    return str(x)[:n]


def statuts_services(d: pathlib.Path) -> dict:
    """CE4-04 : comptes **par statut** des services du noyau d'une génération ou d'une ronde archivée, lus dans les journaux
    écrits par le noyau — entraînements (`travail/noyau/journal-entrainements.jsonl`), recherches par source
    (`travail/noyau/journal-recherches.jsonl`), téléchargements (`travail/corpus/index.jsonl`). Seuls le statut et la
    source sont lus (liste close) : ni requête, ni texte, ni courbe, ni probabilité."""
    entr: dict[str, int] = {}
    for l in _lire_jsonl(d / "travail" / "noyau" / "journal-entrainements.jsonl"):
        st = _mot(l.get("statut"))
        entr[st] = entr.get(st, 0) + 1
    rech: dict[str, dict[str, int]] = {}
    for l in _lire_jsonl(d / "travail" / "noyau" / "journal-recherches.jsonl"):
        s = rech.setdefault(_mot(l.get("source")), {})
        st = _mot(l.get("statut"))
        s[st] = s.get(st, 0) + 1
    tele: dict[str, int] = {}
    for l in _lire_jsonl(d / "travail" / "corpus" / "index.jsonl"):
        st = _mot(l.get("statut"))
        tele[st] = tele.get(st, 0) + 1
    return {"entrainements": dict(sorted(entr.items())), "recherches": {k: dict(sorted(v.items())) for k, v in sorted(rech.items())},
            "telechargements": dict(sorted(tele.items()))}


def fichiers_travail(travail: pathlib.Path) -> list[dict]:
    """Noms et tailles des fichiers ordinaires du dossier de travail archivé, hors `noyau/` et `corpus/` ; aucun contenu."""
    if not travail.is_dir():
        return []
    sortie = []
    for f in sorted(travail.rglob("*")):
        rel = f.relative_to(travail)
        if rel.parts and rel.parts[0] in ("noyau", "corpus"):
            continue
        if f.is_file() and not f.is_symlink():
            sortie.append({"chemin": str(rel), "octets": f.stat().st_size})
    return sortie


def extraire(course: pathlib.Path) -> dict:
    """Extrait mécanique d'une course : manifeste filtré, générations (résumé, appels, organisme, fichiers), événements
    filtrés, rapport filtré. Lève `ExtraitInvalide` si une clé interdite subsiste."""
    course = pathlib.Path(course)
    manifeste_chemin = course / "manifeste-run.json"
    if not manifeste_chemin.is_file():
        raise ExtraitInvalide(f"{course} : manifeste-run.json absent, ce n'est pas une course")
    extrait = {"extrait_version": VERSION_EXTRAIT, "course": str(course),
               "quand_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               "manifeste": filtrer_cles(_lire_json(manifeste_chemin)), "generations": []}
    racine_archive = course / "archive"
    dossiers = sorted(d for d in racine_archive.glob("*/*") if d.is_dir() and (d / "resume.json").is_file()) if racine_archive.is_dir() else []
    # CE4-06 : une ronde importée d'une course d'origine (bras B) garde le `resume.json` de l'origine ; l'index la marque
    importees = {str(l.get("chemin")) for l in _lire_jsonl(racine_archive / "index.jsonl") if l.get("importee")}
    totaux = {"cout_usd": 0.0, "n_appels": 0, "n_generations": 0, "n_importees": 0}
    for d in dossiers:
        resume = _lire_json(d / "resume.json")
        g = _sous_dict(resume, CHAMPS_RESUME)
        g["importee"] = str(d.relative_to(racine_archive)) in importees
        if isinstance(resume.get("execution"), dict):
            ex = _sous_dict(resume["execution"], CHAMPS_EXECUTION)
            st = resume["execution"].get("statut")
            ex["statut_declare_code"] = st.get("code") if isinstance(st, dict) else None
            g["execution"] = ex
        g["appels"] = resume_appels(_lire_jsonl(d / "journal-appels.jsonl"))
        g["journal_appels_scelle"] = (d / "journal-appels.jsonl.sha256").is_file()
        g["organisme_tar_sha256"] = ((d / "organisme.tar.gz.sha256").read_text(encoding="utf-8").split()[0]
                                     if (d / "organisme.tar.gz.sha256").is_file() else None)
        jg = d / "travail" / "journal_generation.json"
        if jg.is_file():
            try:
                g["organisme"] = extrait_organisme(_lire_json(jg))
            except (json.JSONDecodeError, UnicodeDecodeError):
                g["organisme"] = {"journal_illisible": True}
        g["fichiers_travail"] = fichiers_travail(d / "travail")
        g["services"] = statuts_services(d)
        if g["importee"]:
            totaux["n_importees"] += 1
        else:  # sommes de cette course seulement : une ronde importée a été payée par la course d'origine
            totaux["n_generations"] += 1
            totaux["cout_usd"] = round(totaux["cout_usd"] + g["appels"]["cout_usd"], 6)
            totaux["n_appels"] += g["appels"]["n"]
        extrait["generations"].append(g)
    extrait["totaux_hors_importees"] = totaux
    extrait["evenements"] = [filtrer_cles(e) for e in _lire_jsonl(course / "evenements.jsonl")]
    rapports = sorted(course.glob("rapport-v*.json"), key=lambda p: int(re.sub(r"\D", "", p.stem) or 0))
    if rapports:
        r = _lire_json(rapports[-1])
        rap = _sous_dict(r, CHAMPS_RAPPORT)
        rap["fichier"] = rapports[-1].name
        if isinstance(r.get("lignees"), dict):
            rap["lignees"] = {l: _sous_dict(e, CHAMPS_LIGNEE_RAPPORT) for l, e in r["lignees"].items() if isinstance(e, dict)}
        extrait["rapport"] = filtrer_cles(rap)
    presentes = cles_interdites_presentes(extrait)
    if presentes:  # garde finale : jamais un repli silencieux
        raise ExtraitInvalide(f"clés interdites dans l'extrait : {presentes[:10]}")
    return extrait


def ecrire(course: pathlib.Path, sortie: pathlib.Path) -> pathlib.Path:
    """Écrit l'extrait et son compagnon `.sha256` ; refuse une sortie existante (R12) ou placée dans la course."""
    course, sortie = pathlib.Path(course).resolve(), pathlib.Path(sortie).resolve()
    if sortie.exists():
        raise ExtraitInvalide(f"{sortie} existe déjà : nouvelle version = nouveau nom (R12)")
    if course == sortie or course in sortie.parents:
        raise ExtraitInvalide("l'extrait s'écrit hors du dossier de la course, qui reste tel quel")
    extrait = extraire(course)
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(json.dumps(extrait, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    _archive.sceller(sortie)
    return sortie


def principal(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="extrait mécanique d'une course finie, sans aucun score")
    p.add_argument("--course", required=True, help="dossier de la course (celui de --sortie du lanceur)")
    p.add_argument("--sortie", required=True, help="fichier .json à écrire, hors de la course ; compagnon .sha256 écrit à côté")
    args = p.parse_args(argv)
    try:
        chemin = ecrire(pathlib.Path(args.course), pathlib.Path(args.sortie))
    except (ExtraitInvalide, OSError, json.JSONDecodeError) as e:
        print(f"refus : {e}", file=sys.stderr)
        return 2
    print(json.dumps({"extrait": str(chemin), "sha256": _archive.empreinte_fichier(chemin)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
