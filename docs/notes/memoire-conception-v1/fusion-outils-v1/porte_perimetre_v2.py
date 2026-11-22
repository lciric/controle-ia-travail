"""Porte de périmètre de l'organe « mémoire du dépôt », version 2 (22 novembre 2026).

Pièce d'instrument (classe B), session bibliothécaire (Claude Opus 5.5). Version 2 après la contre-lecture de la v1
(contre-lecture-porte-perimetre-v1-v1.md) : juge une JOURNÉE (date UTC) de lectures faites par recherche_bornee_v6.py,
dont les journaux sont à chemin fixe (`registres/veille-de-cap/journaux-outil/<role>-<jour>.jsonl` et `.temoin`).

La porte TOMBE si l'un de ces faits se présente, et TIENT sinon :
  P1  aucune ligne pour la journée alors que le fichier des sessions déclare au moins une session active ce jour-là
      (une journée sans lecture doit être déclarée telle : sessions = {}) ;
  P4  chaîne rompue : numéros non consécutifs depuis 1, empreinte précédente fausse, témoin absent ou en désaccord avec la
      dernière ligne (troncature, ligne retirée ou ajoutée hors outil) ; une session déclarée sans aucune ligne ;
  P5  une ligne d'une autre date que la journée jugée, ou dans le journal d'un autre rôle ;
  P3  une ligne dont la session n'est pas déclarée, ou dont le rôle n'est pas celui que la mère a assigné à la session ;
      un bras qui ne correspond pas au rôle ;
  P6  un journal illisible, non UTF-8, ou qui n'est pas un fichier ordinaire : rapport écrit, la porte tombe ;
  P7  un chemin qui n'est pas un fichier ordinaire au commit cité, un commit hors de origin/main ou main, un chemin non
      ouvrable pour le bras selon listes_lecture_v3.py.
Le fichier des sessions est écrit par la mère : {"jour": "AAAA-MM-JJ", "sessions": {session: role}}, role reponse|boucle.
Limite déclarée : la porte ne voit que les lectures passées par l'outil ; un agent de même privilège peut réécrire journal
et témoin ensemble de façon cohérente ; elle le constate seulement s'il laisse une incohérence.
Usage : python -I porte_perimetre_v2.py SESSIONS.json RAPPORT.json [--depot .]
Codes : 0 tient ; 3 tombe ; 1 arrêt (arguments, rapport existant, fichier des sessions illisible).
"""
import argparse
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("ll3", os.path.join(ICI, "listes_lecture_v3.py"))
ll3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ll3)

REFS_PRINCIPALES = ("origin/main", "main")
ROLES = {"reponse": "memo", "boucle": "boucle"}
DOSSIER = "registres/veille-de-cap/journaux-outil"
ACTIONS = ("chercher", "lire")
ZERO = "0" * 64


def git(depot, *args):
    return subprocess.run(["git", "-C", depot, *args], capture_output=True, text=True)


class Git:
    def __init__(self, depot):
        self.depot, self.anc, self.blob = depot, {}, {}

    def ancetre(self, commit):
        if commit not in self.anc:
            ok = False
            for r in REFS_PRINCIPALES:
                if git(self.depot, "rev-parse", "--verify", "--quiet", r).returncode == 0:
                    ok = git(self.depot, "merge-base", "--is-ancestor", commit, r).returncode == 0
                    break
            self.anc[commit] = ok
        return self.anc[commit]

    def fichier_ordinaire(self, commit, chemin):
        cle = (commit, chemin)
        if cle not in self.blob:
            m = git(self.depot, "ls-tree", commit, "--", chemin)
            t = m.stdout.split(" ", 2) if m.returncode == 0 and m.stdout else []
            self.blob[cle] = len(t) == 3 and t[0] in ("100644", "100755") and t[1] == "blob"
        return self.blob[cle]


def juger_role(depot, role, jour, sessions, g, manquements, vues):
    jpath = os.path.join(depot, DOSSIER, f"{role}-{jour}.jsonl")
    tpath = os.path.join(depot, DOSSIER, f"{role}-{jour}.temoin")
    def manque(motif, ligne=None, chemin=None, session=None):
        manquements.append({"role": role, "ligne": ligne, "session": session, "motif": motif, "chemin": chemin})
    present_j, present_t = os.path.lexists(jpath), os.path.lexists(tpath)
    if not present_j and not present_t:
        return 0
    if not (present_j and os.path.isfile(jpath) and not os.path.islink(jpath)):
        manque("journal absent ou qui n'est pas un fichier ordinaire (témoin présent)")
        return 0
    try:
        texte = open(jpath, "rb").read().decode("utf-8")
    except (OSError, UnicodeDecodeError) as e:
        manque(f"journal illisible ({type(e).__name__})")
        return 0
    lignes = texte.split("\n")
    if lignes and lignes[-1] == "":
        lignes = lignes[:-1]
    prec, n_lu = ZERO, 0
    for i, brut in enumerate(lignes, start=1):
        try:
            e = json.loads(brut)
            assert isinstance(e, dict)
        except (ValueError, AssertionError):
            manque("ligne illisible", i)
            prec = hashlib.sha256(brut.encode("utf-8")).hexdigest()
            continue
        session = e.get("session") if isinstance(e.get("session"), str) else None
        if e.get("n") != i:
            manque("numéro non consécutif (ligne retirée, ajoutée ou déplacée)", i, session=session)
        if e.get("precedent") != prec:
            manque("chaîne rompue : empreinte précédente fausse", i, session=session)
        prec = hashlib.sha256(brut.encode("utf-8")).hexdigest()
        n_lu = i
        chemin = e.get("chemin") if isinstance(e.get("chemin"), str) else None
        quand, commit, action, bras = e.get("quand"), e.get("commit"), e.get("action"), e.get("bras")
        if not isinstance(quand, str) or not quand.startswith(jour + "T"):
            manque("ligne d'une autre journée", i, chemin, session)
        if e.get("role") != role:
            manque("ligne d'un autre rôle dans ce journal", i, chemin, session)
        if session is None or session not in sessions:
            manque("session non déclarée par la mère", i, chemin, session)
            continue
        vues.add(session)
        if sessions[session] != role:
            manque(f"rôle {role} au lieu de {sessions[session]} pour cette session", i, chemin, session)
            continue
        if bras != ROLES[role] or action not in ACTIONS or chemin is None or not isinstance(e.get("agent"), str):
            manque("bras, action, agent ou chemin hors liste", i, chemin, session)
            continue
        if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}", commit):
            manque("commit mal formé", i, chemin, session)
            continue
        if not g.ancetre(commit):
            manque("commit hors de la branche principale", i, chemin, session)
            continue
        if not g.fichier_ordinaire(commit, chemin):
            manque("chemin qui n'est pas un fichier ordinaire au commit cité", i, chemin, session)
            continue
        if not ll3.autorise_bras(chemin, bras)[0]:
            manque(f"fichier non ouvrable pour le bras {bras}", i, chemin, session)
    try:
        t = json.load(open(tpath, encoding="utf-8")) if os.path.isfile(tpath) and not os.path.islink(tpath) else None
    except (OSError, ValueError):
        t = None
    if not isinstance(t, dict) or t.get("n") != n_lu or t.get("empreinte") != prec:
        manque("témoin absent ou en désaccord avec la fin du journal (troncature ou réécriture)")
    return n_lu


def juger(depot, declaration):
    jour, sessions = declaration["jour"], declaration["sessions"]
    g, manquements, vues, total = Git(depot), [], set(), 0
    for role in ROLES:
        total += juger_role(depot, role, jour, sessions, g, manquements, vues)
    for s in sorted(set(sessions) - vues):
        manquements.append({"role": sessions[s], "ligne": None, "session": s, "chemin": None,
                            "motif": "session déclarée active sans aucune ligne au journal"})
    return {"jour": jour, "verdict": "tient" if not manquements else "tombe", "lignes": total,
            "manquements": len(manquements), "detail": manquements}


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("sessions")
    p.add_argument("rapport")
    p.add_argument("--depot", default=".")
    a = p.parse_args(argv)
    if os.path.lexists(a.rapport):
        print(f"ARRET : {a.rapport} existe déjà (R12)", file=sys.stderr)
        return 1
    try:
        d = json.load(open(a.sessions, encoding="utf-8"))
        assert isinstance(d, dict) and isinstance(d.get("jour"), str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", d["jour"])
        assert isinstance(d.get("sessions"), dict)
        assert all(isinstance(k, str) and k and v in ROLES for k, v in d["sessions"].items())
    except (OSError, ValueError, AssertionError):
        print('ARRET : fichier des sessions illisible ({"jour": "AAAA-MM-JJ", "sessions": {session: reponse|boucle}})',
              file=sys.stderr)
        return 1
    r = juger(a.depot, d)
    with open(a.rapport, "x", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: r[k] for k in ("jour", "verdict", "lignes", "manquements")}, ensure_ascii=False))
    return 0 if r["verdict"] == "tient" else 3


if __name__ == "__main__":
    sys.exit(main())
