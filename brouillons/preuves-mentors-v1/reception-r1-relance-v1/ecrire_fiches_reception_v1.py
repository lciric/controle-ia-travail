#!/usr/bin/env python3
"""Écrit les deux fiches de réception du run R1 relancé (et des juges R2 déjà versés), aux clés exactes exigées par
l'analyse principale (`fiche-reception-principale-r1-r2-v1`, `entrees_v1.lire_fiche`, commit cité `a8b7fdb2`) et par
l'analyse secondaire (`fiche-reception-blanche-noire-v3`, `entrees_v3.lire_fiche_v3`, commit cité `326601cf`).

Ce que le script fait : il liste `runs/<run>/`, `diag/<run>/` et `donnees/<run>/` des runs nommés sur la ligne de
commande, calcule l'empreinte sha256 de chaque fichier, la compare au compagnon `.sha256` du fournisseur, refuse tout
nom inattendu, et recopie les empreintes dans les fiches. Il n'ouvre **aucun** fichier `.npz` (empreintes seulement).
Par défaut il n'ouvre aucun JSON non plus ; avec `--ouvrir-resultats`, il ouvre les seuls résultats
`diag/<run>/rejeu-activations.json`, `juge-actions.json` et `arret.json` pour : résoudre les pointeurs de la fiche
secondaire (clés nommées, jamais de tableau), lire `verdict_fidelite` (motif fermé de `R1: null`), lire
`tokenisation.episodes_non_resolus` et `tokenisation.table_sha256` (garde E19 : la liste doit égaler celle que
l'addendum v2 déclare non inversible, vide par défaut). Ce qui a été ouvert est écrit dans `redaction`.

Aucun nombre de résultat n'est écrit dans les fiches. Aucun repli silencieux : tout écart arrête avec un code 2 et un
message « ARRÊT : … » (R5). Les fiches existantes ne sont jamais écrasées (R12). Dépendances : bibliothèque standard.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

FORMAT_PRINCIPALE = "fiche-reception-principale-r1-r2-v1"
FORMAT_SECONDAIRE = "fiche-reception-blanche-noire-v3"
NOM_SORTIE_R1 = "activations-p3-rejeu-v1"                   # `nom_sortie` de la configuration v4 (addendum, formats)
FICHIERS_R1 = {"moyenne": f"{NOM_SORTIE_R1}.npz", "maximum": f"{NOM_SORTIE_R1}-maximum.npz",
               "complement": f"{NOM_SORTIE_R1}-complement-hors-cout.npz"}
RESULTAT_R1, RESULTAT_JUGE, ARRET = "rejeu-activations.json", "juge-actions.json", "arret.json"
FICHIERS_JUGES = {"juge3b": "scores-juge3b-p3-v1.npz", "juge8b": "scores-juge8b-p3-v1.npz"}
MOTIFS_R1_NUL = {"non conforme": "rejeu_non_conforme", "echec": "rejeu_en_echec", "échec": "rejeu_en_echec"}
MOTIFS_R2_NUL = ("sorties_non_livrees", "garde_N029_du_kit")
# pointeurs de la fiche secondaire (noms permis par `entrees.POINTEURS_R1 | {"regle_repli"}` et `POINTEURS_R2`),
# chemins recopiés du code scellé du fournisseur (`rejeu_activations_v1.py`, `juge_actions_v1.py`, commit 29bd8e2e ;
# clés inchangées par l'addendum) dans le corps `{"run_id", "manifeste_sha256", "resultat": {…}}` de `ecrire_resultat`
POINTEURS_R1 = {"fidelite_conforme": ["resultat", "verdict_fidelite"], "regle_repli": ["resultat", "regle_repli_appliquee"],
                "textes_sha256": ["resultat", "textes_sha256"], "couches": ["resultat", "couches"],
                "contexte_rejeu": ["resultat", "contexte"], "regle_empan": ["resultat", "regle_empan"],
                "modele": ["resultat", "modele"]}
POINTEURS_R2 = {"invite_sha256": ["resultat", "invite_sha256"], "contexte_juge": ["resultat", "contexte"],
                "modele": ["resultat", "juge"]}
SUFFIXE = ".sha256"
_LIGNE = re.compile(r"^([0-9a-f]{64})  (\S.*)$")
_RUN = re.compile(r"^[0-9]{8}-[0-9]{6}-[A-Za-z0-9_.-]+$")


class Arret(Exception):
    pass


def empreinte(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def lire_compagnon(c: Path, nom: str) -> str:
    lignes = [l for l in c.read_text(encoding="utf-8").splitlines() if l.strip()]
    if len(lignes) != 1 or not _LIGNE.match(lignes[0]):
        raise Arret(f"{c} : compagnon illisible")
    m = _LIGNE.match(lignes[0])
    if m.group(2) != nom:
        raise Arret(f"{c} : nom {m.group(2)!r} au lieu de {nom!r}")
    return m.group(1)


def fichier_verifie(racine: Path, rel: str, inventaire: dict) -> dict:
    """Empreinte calculée, égale au compagnon du fournisseur ; sinon arrêt. Rien n'est ouvert autrement."""
    p = racine / rel
    if not p.is_file():
        raise Arret(f"{rel} absent sur disque (R11 : vérifier sur disque et par `git ls-tree` avant de conclure)")
    c = Path(str(p) + SUFFIXE)
    if not c.is_file():
        raise Arret(f"{rel} : compagnon {c.name} absent")
    h = empreinte(p)
    attendue = lire_compagnon(c, p.name)
    if h != attendue:
        raise Arret(f"{rel} : empreinte calculée {h[:12]}… ≠ compagnon {attendue[:12]}…")
    inventaire[rel] = h
    return {"chemin": rel, "sha256": h}


def noms(racine: Path, dossier: str) -> set[str]:
    d = racine / dossier
    if not d.is_dir():
        raise Arret(f"dossier {dossier} absent")
    return {p.name for p in d.iterdir() if p.is_file()}


def exiger_noms(racine: Path, dossier: str, attendus: set[str], tolerés: set[str] = frozenset()) -> None:
    presents = noms(racine, dossier)
    avec_compagnons = attendus | {n + SUFFIXE for n in attendus} | tolerés | {n + SUFFIXE for n in tolerés}
    inattendus = sorted(presents - avec_compagnons)
    manquants = sorted(avec_compagnons - presents - tolerés - {n + SUFFIXE for n in tolerés})
    if inattendus:
        raise Arret(f"{dossier} : nom(s) inattendu(s) {inattendus} (rien n'est deviné : nœud à signaler)")
    if manquants:
        raise Arret(f"{dossier} : fichier(s) attendu(s) absent(s) {manquants}")


def exiger_run(nom: str, quoi: str) -> str:
    if not _RUN.match(nom):
        raise Arret(f"{quoi} : nom de run {nom!r} hors du format AAAAMMJJ-HHMMSS-<nom>")
    return nom


def lire_json(p: Path, ouverts: list) -> dict:
    ouverts.append(str(p))
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise Arret(f"{p} : JSON illisible ({type(e).__name__})") from None


def resoudre(doc, chemin: list):
    v = doc
    for k in chemin:
        if isinstance(v, dict) and k in v:
            v = v[k]
        elif isinstance(v, list) and isinstance(k, int) and 0 <= k < len(v):
            v = v[k]
        else:
            raise Arret(f"pointeur {chemin} ne se résout pas dans le résultat du fournisseur")
    return v


def construire(racine: Path, a) -> tuple[dict, dict]:
    inventaire, ouverts, notes = {}, [], []
    rejeu = exiger_run(a.rejeu, "rejeu")
    exiger_noms(racine, f"runs/{rejeu}", {"manifeste.json"})
    manifeste_rejeu = fichier_verifie(racine, f"runs/{rejeu}/manifeste.json", inventaire)
    diag = noms(racine, f"diag/{rejeu}")
    a_resultat, a_arret = RESULTAT_R1 in diag, ARRET in diag
    if a_resultat == a_arret:
        raise Arret(f"diag/{rejeu} : il faut exactement un de {RESULTAT_R1} et {ARRET} (présents : {sorted(diag)})")
    r1_p = r1_s = motif_r1 = None
    if a_resultat:
        exiger_noms(racine, f"diag/{rejeu}", {RESULTAT_R1})
        exiger_noms(racine, f"donnees/{rejeu}", set(FICHIERS_R1.values()))
        res = fichier_verifie(racine, f"diag/{rejeu}/{RESULTAT_R1}", inventaire)
        r1_p = {k: fichier_verifie(racine, f"donnees/{rejeu}/{n}", inventaire) for k, n in FICHIERS_R1.items()}
        r1_p["resultat"] = res
        r1_s = {"moyenne": r1_p["moyenne"], "maximum": r1_p["maximum"], "manifeste": res, "pointeurs": POINTEURS_R1}
        if a.ouvrir_resultats:
            doc = lire_json(racine / res["chemin"], ouverts)
            for k, ch in POINTEURS_R1.items():
                resoudre(doc, ch)
            if doc.get("run_id") != rejeu:
                raise Arret(f"{RESULTAT_R1} : run_id {doc.get('run_id')!r} ≠ {rejeu}")
            v = resoudre(doc, ["resultat", "verdict_fidelite"])
            if v != "conforme":
                raise Arret(f"{RESULTAT_R1} livré avec verdict_fidelite = {v!r} : hors du format annoncé, nœud")
            fichiers = resoudre(doc, ["resultat", "fichiers"])
            for k, n in FICHIERS_R1.items():
                if fichiers.get(n) != r1_p[k]["sha256"]:
                    raise Arret(f"{RESULTAT_R1} : empreinte de {n} déclarée par le fournisseur ≠ fichier versé")
            tok = doc["resultat"].get("tokenisation")
            if tok is None:
                raise Arret(f"{RESULTAT_R1} : clé `tokenisation` absente (la relance l'écrit ; vérifier le run nommé)")
            non_resolus = sorted(tok.get("episodes_non_resolus") or [])
            declares = sorted(a.episodes_non_inversibles_declares)
            if non_resolus != declares:
                raise Arret(f"épisodes non résolus du run {non_resolus} ≠ déclarés par l'addendum v2 {declares} : "
                            "nœud de Lazar (E19), rien n'est lancé")
            notes.append({"tokenisation_table_sha256": tok.get("table_sha256"),
                          "episodes_non_resolus_du_run": non_resolus,
                          "episodes_non_inversibles_declares_par_addendum_v2": declares,
                          "a_lazar": bool(declares)})
    else:
        exiger_noms(racine, f"diag/{rejeu}", {ARRET})
        if (racine / "donnees" / rejeu).exists():
            raise Arret(f"donnees/{rejeu} existe alors que le rejeu s'est arrêté : hors du format annoncé")
        arret = fichier_verifie(racine, f"diag/{rejeu}/{ARRET}", inventaire)
        if not a.ouvrir_resultats:
            raise Arret(f"{ARRET} présent : le motif fermé exige de lire son verdict_fidelite ; relancer avec "
                        "--ouvrir-resultats (rien n'est deviné)")
        doc = lire_json(racine / arret["chemin"], ouverts)
        v = resoudre(doc, ["resultat", "verdict_fidelite"])
        if v not in MOTIFS_R1_NUL:
            raise Arret(f"{ARRET} : verdict_fidelite {v!r} hors de {sorted(MOTIFS_R1_NUL)} : nœud")
        motif_r1 = MOTIFS_R1_NUL[v]
        notes.append({"arret": arret, "verdict_fidelite": v})
    r2_p = r2_s = motif_r2 = None
    if a.juge3b == "absent":
        if a.motif_R2 not in MOTIFS_R2_NUL:
            raise Arret(f"juge 3B absent : --motif-R2 parmi {MOTIFS_R2_NUL} exigé, preuve dans --preuve-R2")
        if not a.preuve_R2:
            raise Arret("juge 3B absent : --preuve-R2 (constat ou chemin et empreinte) exigé")
        motif_r2 = a.motif_R2
        notes.append({"motif_R2": motif_r2, "preuve": a.preuve_R2})
    else:
        juges = {}
        for cle, run in (("juge3b", a.juge3b), ("juge8b", a.juge8b)):
            if run == "absent":
                juges[cle] = None
                continue
            run = exiger_run(run, cle)
            exiger_noms(racine, f"runs/{run}", {"manifeste.json"})
            fichier_verifie(racine, f"runs/{run}/manifeste.json", inventaire)
            exiger_noms(racine, f"diag/{run}", {RESULTAT_JUGE})
            exiger_noms(racine, f"donnees/{run}", {FICHIERS_JUGES[cle]})
            juges[cle] = {"fichier": fichier_verifie(racine, f"donnees/{run}/{FICHIERS_JUGES[cle]}", inventaire),
                          "resultat": fichier_verifie(racine, f"diag/{run}/{RESULTAT_JUGE}", inventaire)}
            if a.ouvrir_resultats:
                doc = lire_json(racine / juges[cle]["resultat"]["chemin"], ouverts)
                if doc.get("run_id") != run:
                    raise Arret(f"{RESULTAT_JUGE} de {run} : run_id ≠")
                if resoudre(doc, ["resultat", "fichier"]) != FICHIERS_JUGES[cle] or \
                        resoudre(doc, ["resultat", "sha256"]) != juges[cle]["fichier"]["sha256"]:
                    raise Arret(f"{RESULTAT_JUGE} de {run} : fichier ou empreinte déclarés ≠ fichier versé")
                if cle == "juge3b":
                    for k, ch in POINTEURS_R2.items():
                        resoudre(doc, ch)
                    print("contexte déclaré du juge 3B (à juger par la session, règle d'équité ; non écrit dans la fiche) :",
                          json.dumps(resoudre(doc, POINTEURS_R2["contexte_juge"]), ensure_ascii=False))
        r2_p = {"juge3b": juges["juge3b"], "juge8b": juges["juge8b"],
                "motif_juge8b": None if juges["juge8b"] is not None else "non_livre"}
        r2_s = {"fichier": juges["juge3b"]["fichier"], "manifeste": juges["juge3b"]["resultat"], "pointeurs": POINTEURS_R2}
    redaction = {
        "qui": a.qui, "quand_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "commit_versement_calcul_r1_r2_reel_v1": a.commit_versement,
        "addendum_v2": {"chemin": a.addendum_chemin, "sha256": a.addendum_sha256},
        "runs": {"rejeu": rejeu, "juge3b": a.juge3b, "juge8b": a.juge8b},
        "ce_qui_a_ete_ouvert": ouverts or ["aucun fichier ouvert : noms et empreintes seulement"],
        "aucun_npz_ouvert": True, "compagnons_verifies": inventaire, "notes": notes,
        "script": {"nom": "ecrire_fiches_reception_v1.py", "sha256": empreinte(Path(__file__))},
    }
    principale = {"format": FORMAT_PRINCIPALE, "redaction": redaction, "R1": r1_p, "motif_R1": motif_r1,
                  "R2": r2_p, "motif_R2": motif_r2}
    secondaire = {"format": FORMAT_SECONDAIRE, "redaction": dict(redaction, manifeste_rejeu=manifeste_rejeu),
                  "R1": r1_s, "motif_R1": motif_r1, "R2": r2_s, "motif_R2": motif_r2, "R4": None}
    return principale, secondaire


def ecrire(p: Path, contenu: dict) -> str:
    if p.exists():
        raise Arret(f"{p} existe déjà : R12 interdit d'écraser (version nouvelle = nom nouveau)")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(contenu, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return empreinte(p)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--racine", required=True, help="racine de l'arbre où les sorties sont versées")
    ap.add_argument("--rejeu", required=True, help="nom du run R1 relancé (jamais deviné)")
    ap.add_argument("--juge3b", required=True, help="nom du run du juge 3B, ou `absent`")
    ap.add_argument("--juge8b", required=True, help="nom du run du juge 8B, ou `absent`")
    ap.add_argument("--motif-R2", default=None, choices=MOTIFS_R2_NUL)
    ap.add_argument("--preuve-R2", default=None)
    ap.add_argument("--qui", required=True)
    ap.add_argument("--commit-versement", required=True, help="40 caractères du commit de FETCH_HEAD")
    ap.add_argument("--addendum-chemin", default="prereg/R1-addendum-relance-v2.md")
    ap.add_argument("--addendum-sha256", required=True, help="empreinte de l'addendum v2 scellé (paramètre)")
    ap.add_argument("--episodes-non-inversibles-declares", default="",
                    help="liste séparée par des virgules, vide si l'addendum v2 n'en déclare aucun")
    ap.add_argument("--ouvrir-resultats", action="store_true")
    ap.add_argument("--sortie-principale", default="prereg/fiche-reception-principale-r1-r2-v1.json")
    ap.add_argument("--sortie-secondaire", default="prereg/fiche-reception-blanche-noire-v3.json")
    ap.add_argument("--sans-secondaire", action="store_true", help="n'écrire que la fiche principale")
    a = ap.parse_args(argv)
    a.episodes_non_inversibles_declares = [e for e in a.episodes_non_inversibles_declares.split(",") if e]
    if not re.fullmatch(r"[0-9a-f]{40}", a.commit_versement) or not re.fullmatch(r"[0-9a-f]{64}", a.addendum_sha256):
        print("ARRÊT : commit de versement (40 hex) ou empreinte de l'addendum v2 (64 hex) hors de forme", file=sys.stderr)
        return 2
    racine = Path(a.racine).resolve()
    try:
        principale, secondaire = construire(racine, a)
        hp = ecrire(racine / a.sortie_principale, principale)
        print(f"fiche principale : {a.sortie_principale} {hp}")
        if not a.sans_secondaire:
            hs = ecrire(racine / a.sortie_secondaire, secondaire)
            print(f"fiche secondaire : {a.sortie_secondaire} {hs}")
        print(f"fichiers vérifiés contre leur compagnon : {len(principale['redaction']['compagnons_verifies'])}")
        print(f"ouverts : {principale['redaction']['ce_qui_a_ete_ouvert']}")
        return 0
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
