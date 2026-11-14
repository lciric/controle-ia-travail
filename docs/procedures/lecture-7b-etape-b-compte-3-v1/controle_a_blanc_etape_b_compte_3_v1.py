"""Contrôle à blanc, en lecture seule, de l'ouverture de l'étape B de T0.7 et de la condition d'ordre « plan de l'étape B bis
scellé avant toute lecture de l'étape B », v1.

Écrit le 2026-11-14 par un préparateur neuf de la session mère (modèle A), qui ne sera ni lecteur ni juge d'aucun verdict et
n'a ouvert aucune sortie de 7a, 7b ou T0.7 (noms, tailles et empreintes seulement). Appelé par `commande-compte-3-v1.md`
(même dossier) avant tout geste irréversible, et par `prealables-v1.md` sur une copie de l'état des registres.

Il n'écrit rien, nulle part, et n'importe ni numpy ni torch (seulement `registre_v1`, `journal_p3bis_v1`, `garde_adaptee_v1` et
`code_t07_v1`, à leur version du code exécuté). Il n'ouvre le contenu d'aucun résultat : les fichiers cités par les lignes du registre et les
fichiers de données de l'étape B ne sont que hachés (empreinte comparée à la ligne et au compagnon). Il lit seulement : la
configuration scellée de T0.7, le registre donné, le journal des ouvertures voisin (`<registre>.ouvertures.md`, première
ouverture de l'étape A), le journal et le registre des préalables de P3-bis (clé, date, mode, appui), le fichier cité par
`CODE-T07` (commit et empreintes), l'extrait de GO et `registres/go.md`, et le registre propre de l'étape B bis.

Dans l'ordre (tous les contrôles sont joués, puis le bilan) :
  1. configuration de T0.7 : empreinte du fichier égale à l'attendue et au compagnon ; marques des autres tâches ; `CODE-T07`
     exigée ou non (`code_t07_exige`) ;
  2. registre lu par `registre_v1.lire_registre_detail` aux clés de l'étape B (exigées, permises, marques de la
     configuration) : clés présentes, manquantes, ignorées (marque d'une autre tâche), refusées (clé inconnue, famille des
     jeux, forme, double) ;
  3. `registre_v1.verifier_lignes` sur les lignes lues sans faute, à l'instant donné : antériorité stricte, fichier cité
     présent, empreinte égale à la ligne et au compagnon, extrait de GO égal à une ligne de `registres/go.md` ;
  4. antériorités : `SCORES-T07` et `SONDES-T07` strictement avant `VERDICT-P3BIS` ; `CONSIGNE-AUDIT-FUITES-T07`
     strictement avant `AUDIT-FUITES-T07` ;
  5. garde adaptée de l'étape B (`garde_adaptee_v1.garde_etape_b`) sur le journal de P3-bis ;
  6. `CODE-T07` (`code_t07_v1.controler_code` : commandes git en lecture sur le dépôt du module importé) ;
  7. fichiers hors registre de l'étape B : présence et compagnon (hachage seul) ; `lecture-t07.json`, `arret-etape-b.json`
     (sous la racine de sortie), `arret.json` de T0.6 et `lecture-sondes-t06.json` (sous la racine) absents ;
  8. condition d'ordre B bis (si `--registre-bbis` et `--cle-bbis`) : registre propre distinct des registres lus par T0.7 ;
     exactement une ligne de la clé, au format ; datée strictement avant l'instant ; fichier cité à son empreinte et à son
     compagnon ; clé absente du registre de T0.7.

    PYTHONPATH=<src du code exécuté> python -B controle_a_blanc_etape_b_compte_3_v1.py --racine R --registre REG \
        --config CONFIG_T07 [--run-t06 RUN] [--run-t07 RUN] [--racine-sortie RS] [--instant AAAA-MM-JJTHH:MM:SSZ] \
        [--registre-bbis REG_BBIS --cle-bbis CLE] [--mode rapport|avant-etape-b]

Codes : 0 conforme (mode `rapport` : aucun refus, les manques sont listés ; mode `avant-etape-b` : rien ne manque, aucun
refus) ; 2 refus, ou manque en mode `avant-etape-b` ; 1 erreur d'appel.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
import time
from pathlib import Path

from controle_ia.gardes import GardeArret
from controle_ia.t07 import code_t07_v1 as ct
from controle_ia.t07 import garde_adaptee_v1 as ga
from controle_ia.t07 import journal_p3bis_v1 as jp
from controle_ia.t07 import registre_v1 as rg

CONFIG_ATTENDUE = "e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328"   # configuration v8 scellée de T0.7
RUN_T06_DEFAUT, RUN_T07_DEFAUT = "20261111-151701-t06-reel", "20261114-001352-t07-lecture-reel"
REGISTRES_LUS_PAR_T07 = ("registres/scellements-v1.md", "registres/scellements-v1.md.ouvertures.md", jp.JOURNAL_P3BIS,
                         jp.PREALABLES_P3BIS)


def _sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _compagnon(p: Path) -> str:
    """« conforme », « absent », « compagnon absent » ou « compagnon ≠ » (hachage seul, contenu jamais lu)."""
    p = Path(p)
    if not p.is_file():
        return "absent"
    c = Path(str(p) + ".sha256")
    if not c.is_file():
        return "compagnon absent"
    lu = (c.read_text(encoding="utf-8").split() or [""])[0]
    return "conforme" if lu == _sha(p) else "compagnon ≠"


def _premiere_ouverture_a(registre: Path, run_t06: str) -> int | None:
    """Copie de `lecture_v2.premiere_ouverture_a` (C7, l. 239-249), recopiée pour ne pas importer `lecture_v2` (qui tire torch) :
    instant de la première ligne `OUVERTURE-T07 | … | etape-A/<run>` du journal `<registre>.ouvertures.md`, ou None."""
    journal = Path(str(registre) + ".ouvertures.md")
    if not journal.is_file():
        return None
    for ligne in journal.read_text(encoding="utf-8").splitlines():
        c = jp._cellules(ligne)
        if c and len(c) >= 3 and c[0] == "OUVERTURE-T07" and c[2] == f"etape-A/{run_t06}":
            return rg.instant_utc(c[1])
    return None


def _motifs(e: Exception) -> list[str]:
    return [m.strip() for m in str(e).split(" ; ") if m.strip()]


def lire_configuration(chemin: Path) -> dict:
    import json
    chemin = Path(chemin)
    sha = _sha(chemin)
    if sha != CONFIG_ATTENDUE:
        raise GardeArret(f"configuration {chemin} : empreinte {sha[:12]}… ≠ {CONFIG_ATTENDUE[:12]}… (configuration v8 scellée)")
    if _compagnon(chemin) != "conforme":
        raise GardeArret(f"configuration {chemin} : compagnon absent ou différent")
    return json.loads(chemin.read_text(encoding="utf-8"))


def controle_bbis(racine: Path, registre_t07: Path, registre_bbis: Path, cle: str, instant: int) -> tuple[bool, list[str]]:
    """Condition d'ordre B bis. Rend (remplie ?, lignes à imprimer)."""
    lignes, ok = [], True
    racine, registre_t07, registre_bbis = Path(racine), Path(registre_t07), Path(registre_bbis)
    if not rg.CLE.fullmatch(cle or ""):
        return False, [f"clé {cle!r} hors de la forme [A-Z0-9]+(-[A-Z0-9]+)+"]
    interdits = {(racine / r).resolve() for r in REGISTRES_LUS_PAR_T07} | {registre_t07.resolve(),
                                                                          Path(str(registre_t07) + ".ouvertures.md").resolve()}
    if registre_bbis.resolve() in interdits:
        return False, [f"registre {registre_bbis} : c'est un registre que lit T0.7 (la ligne y ferait refuser l'étape B ou y "
                       "serait ignorée) : registre propre exigé"]
    if rg.cle_presente(registre_t07, cle):
        ok = False
        lignes.append(f"clé {cle} présente dans le registre de T0.7 ({registre_t07}) : l'étape B la refuserait (règle (4)) ; nœud")
    if not registre_bbis.is_file():
        return False, lignes + [f"registre propre {registre_bbis} absent : plan de l'étape B bis non scellé"]
    trouvees = []
    for brute in registre_bbis.read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in brute.strip().strip("|").split("|")]
        if c and c[0] == cle:
            trouvees.append(c)
    if len(trouvees) != 1:
        return False, lignes + [f"{len(trouvees)} ligne(s) {cle} dans {registre_bbis}, exactement une attendue"]
    c = trouvees[0]
    if len(c) != 4 or not rg.DATE.fullmatch(c[1]) or not rg.SHA.fullmatch(c[3]) or not c[2] or c[2].startswith("/") \
            or ".." in Path(c[2]).parts:
        return False, lignes + [f"ligne {cle} hors du format | CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin relatif | sha256 |"]
    try:
        v = rg.verifier_lignes({cle: (rg.instant_utc(c[1]), c[1], c[2], c[3])}, racine, instant)
        lignes.append(f"ligne {cle} datée {v[cle]['date']} (strictement avant {rg.date_utc(instant)}) ; {c[2]} : sceau conforme "
                      f"({c[3][:12]}…)")
    except rg.RefusRegistre as e:
        return False, lignes + _motifs(e)
    return ok, lignes


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--racine", required=True)
    p.add_argument("--registre", required=True)
    p.add_argument("--config", required=True)
    p.add_argument("--run-t06", default=RUN_T06_DEFAUT)
    p.add_argument("--run-t07", default=RUN_T07_DEFAUT)
    p.add_argument("--racine-sortie", default=None)
    p.add_argument("--instant", default=None, help="AAAA-MM-JJTHH:MM:SSZ ; défaut : l'horloge")
    p.add_argument("--registre-bbis", default=None)
    p.add_argument("--cle-bbis", default=None)
    p.add_argument("--mode", choices=("rapport", "avant-etape-b"), default="rapport")
    a = p.parse_args(argv)
    racine, registre = Path(a.racine).resolve(), Path(a.registre).resolve()
    sortie = Path(a.racine_sortie).resolve() if a.racine_sortie else racine
    instant = rg.instant_utc(a.instant) if a.instant else int(time.time())
    run6, run7 = a.run_t06, a.run_t07
    refus, manques = [], []
    print(f"contrôle à blanc de l'étape B de T0.7 (lecture seule) à {rg.date_utc(instant)} ; racine {racine} ; registre {registre} "
          f"({_sha(registre)[:12]}…) ; RUN_T06 {run6} ; RUN_T07 {run7} ; mode {a.mode}")
    try:
        config = lire_configuration(Path(a.config))
    except GardeArret as e:
        print(f"ARRÊT : {e}")
        return 2
    marques = tuple(config["marques_autres_taches"])
    exigees = rg.EXIGEES_ETAPE_B + ((rg.CODE_T07,) if config["code_t07_exige"] else ())
    permises = tuple(k for k in rg.PERMISES_ETAPE_B if k not in exigees)
    print(f"1. configuration : {CONFIG_ATTENDUE[:12]}… conforme ; marques des autres tâches : {', '.join(marques)} ; "
          f"CODE-T07 exigée : {'oui' if config['code_t07_exige'] else 'non'}")
    # 2. registre
    lignes, ignorees = {}, []
    try:
        lignes, ignorees = rg.lire_registre_detail(registre, exigees, permises, {}, marques)
    except rg.RefusRegistre as e:
        partiel = getattr(e, "partiel", None)
        if partiel:
            lignes, ignorees = partiel
        for m in _motifs(e):
            (manques if "0 ligne(s)" in m else refus).append(m)
    presentes = [k for k in exigees if k in lignes]
    absentes = [k for k in exigees if k not in lignes]
    print(f"2. clés exigées à l'étape B ({len(exigees)}) : présentes {presentes or 'aucune'} ; manquantes {absentes or 'aucune'}")
    print(f"   clés permises présentes : {[k for k in permises if k in lignes] or 'aucune'}")
    print(f"   clés ignorées (marque d'une autre tâche) : {ignorees or 'aucune'}")
    print(f"   refus du registre (hors clés manquantes) : {[m for m in refus] or 'aucun'}")
    # 3. sceaux et antériorité à l'instant
    verifiees = {}
    if lignes:
        try:
            verifiees = rg.verifier_lignes(lignes, racine, instant)
        except rg.RefusRegistre as e:
            verifiees = getattr(e, "partiel", {}) or {}
            for m in _motifs(e):
                (manques if (" absent" in m and "compagnon" not in m) else refus).append(m)
    nv = [k for k in lignes if k not in verifiees]
    print(f"3. lignes vérifiées (antériorité stricte, fichier cité, empreinte, compagnon) : {len(verifiees)} sur {len(lignes)} ; "
          f"non vérifiées : {nv or 'aucune'}")
    # 4. antériorités
    for avant, apres in (((rg.SCORES_T07, rg.SONDES_T07), rg.VERDICT_P3BIS),
                         ((rg.CONSIGNE_AUDIT_FUITES_T07,), rg.AUDIT_FUITES_T07)):
        if apres in lignes and all(k in lignes for k in avant):
            pas = [k for k in avant if not lignes[k][0] < lignes[apres][0]]
            if pas:
                refus.append(f"{', '.join(pas)} pas strictement antérieure(s) à {apres}")
            print(f"4. {', '.join(avant)} < {apres} : {'non' if pas else 'oui'}")
        else:
            print(f"4. {', '.join(avant)} < {apres} : sans objet ({apres} ou une clé d'avant absente)")
    # 5. garde adaptée
    lignes_ga = {k: {"instant": t, "date": d, "chemin": c, "sha256": s} for k, (t, d, c, s) in lignes.items()}
    try:
        journal = jp.lire_journal_p3bis(racine / jp.JOURNAL_P3BIS)
        reduite = any(o["mode"] == jp.REDUITE for o in jp.ouvertures(journal))
        if reduite:             # chemin non couvert : les écrits de P3-bis (préalables, décisions) ne sont pas relus ici
            raise GardeArret("ouverture réduite au journal de P3-bis : ce contrôle ne relit pas les écrits du rendez-vous ; nœud")
        codes = ga.garde_etape_b(lignes_ga, journal, None, None)
        modes = [o["mode"] for o in jp.ouvertures(journal)]
        print(f"5. garde adaptée : ouvertures de P3-bis {modes or 'aucune'} ; codes {[c for c, _ in codes] or 'aucun'}")
        for c, m in codes:
            refus.append(f"garde adaptée {c} ({ga.NATURE.get(c, '?')}) : {m}")
    except GardeArret as e:
        refus.append(f"garde adaptée : {e}")
        print("5. garde adaptée : refus (motif au bilan)")
    # 6. CODE-T07
    if rg.CODE_T07 in verifiees:
        try:
            premiere = _premiere_ouverture_a(registre, run6)
            r = ct.controler_code(racine, verifiees[rg.CODE_T07], premiere)
            print(f"6. CODE-T07 : commit {r['commit'][:12]}… ; tête du dépôt du module {r['tete_du_depot'][:12]}… ; "
                  f"{r['fichiers']} fichiers conformes ; première ouverture de l'étape A "
                  f"{rg.date_utc(premiere) if premiere is not None else 'absente'}")
        except GardeArret as e:
            refus.append(f"CODE-T07 : {e}")
            print("6. CODE-T07 : refus (motif au bilan)")
    else:
        print("6. CODE-T07 : non contrôlée (ligne absente ou non vérifiée)")
    # 7. fichiers hors registre (hachage seul)
    hors = {f"diag/{run6}/lecture-cout-t06.json": racine, f"diag/{run6}/episodes-t06.json": racine,
            f"donnees/{run6}/mesures-t06.npz": racine, f"donnees/{run6}/textes-actions-t06.jsonl": racine,
            f"runs/{run6}/manifeste.json": racine, f"runs/{run7}/manifeste.json": sortie}
    etats = {}
    for rel, base in hors.items():
        etats[rel] = _compagnon(base / rel)
        if etats[rel] == "absent":
            manques.append(f"{rel} absent (à rapatrier)")
        elif etats[rel] != "conforme":
            refus.append(f"{rel} : {etats[rel]}")
    print("7. fichiers de données de l'étape B : " + " ; ".join(f"{Path(k).name} ({k.split('/')[0]}) {v}" for k, v in etats.items()))
    for rel, base, quoi in ((f"diag/{run7}/lecture-t07.json", sortie, "lecture décisive déjà écrite (R12) : refus"),
                            (f"diag/{run7}/arret-etape-b.json", sortie, "arrêt de l'étape B déjà écrit : nœud"),
                            (f"diag/{run6}/arret.json", racine, "arrêt de T0.6 présent : A = arret"),
                            (f"diag/{run6}/lecture-sondes-t06.json", racine, "fichier fermé de T0.6 présent sous la racine : "
                                                                            "jamais rapatrié")):
        present = (base / rel).exists()
        print(f"   {rel} : {'PRÉSENT' if present else 'absent'}")
        if present:
            refus.append(f"{rel} : {quoi}")
    # 8. condition d'ordre B bis
    if a.registre_bbis or a.cle_bbis:
        if not (a.registre_bbis and a.cle_bbis):
            print("ARRÊT : --registre-bbis et --cle-bbis vont ensemble")
            return 1
        ok, l8 = controle_bbis(racine, registre, Path(a.registre_bbis), a.cle_bbis, instant)
        print(f"8. condition d'ordre B bis ({a.cle_bbis}) : {'REMPLIE' if ok else 'NON REMPLIE'}")
        for m in l8:
            print(f"   {m}")
        if not ok:
            (refus if any("registre de T0.7" in m or "registre que lit" in m for m in l8) else manques).append(
                f"condition d'ordre B bis non remplie ({'; '.join(l8)})")
    else:
        print("8. condition d'ordre B bis : non demandée")
        if a.mode == "avant-etape-b":
            manques.append("condition d'ordre B bis non contrôlée (--registre-bbis et --cle-bbis exigés en mode avant-etape-b)")
    print(f"BILAN : {len(refus)} refus ; {len(manques)} manque(s)")
    for m in refus:
        print(f"  REFUS : {m}")
    for m in manques:
        print(f"  MANQUE : {m}")
    if refus:
        print("CONTRÔLE À BLANC DE L'ÉTAPE B : REFUS")
        return 2
    if manques and a.mode == "avant-etape-b":
        print("CONTRÔLE À BLANC DE L'ÉTAPE B : INCOMPLET (aucune étape B)")
        return 2
    print("CONTRÔLE À BLANC DE L'ÉTAPE B : " + ("TOUT CONFORME" if not manques else "AUCUN REFUS ; MANQUES LISTÉS"))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except (OSError, ValueError, KeyError) as e:
        print(f"ERREUR D'APPEL : {type(e).__name__} : {e}")
        sys.exit(1)
