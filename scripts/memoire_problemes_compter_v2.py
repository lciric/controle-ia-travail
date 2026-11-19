#!/usr/bin/env python3
"""Compte, sur un fichier de mémoire des problèmes, les problèmes et les tentatives par partition,
les attentes écrites avant et leur issue, et les états. Version 2 : admet une issue placée dans un segment réservé « ⟦mère : … ⟧ ». Lecture seule. Usage : compter FICHIER [--markdown]"""
import collections
import re
import sys


def compter(texte):
    part = None
    dans = False
    pb = collections.OrderedDict()
    tent = collections.Counter()
    avant = sans = 0
    issue = collections.Counter()
    etats = collections.Counter()
    anomalies = []
    for n, l in enumerate(texte.split("\n"), 1):
        m = re.match(r"^## Partition « (.+) »", l)
        if m:
            part = m.group(1)
            pb[part] = 0
            continue
        if l.startswith("## ") or l.startswith("---"):
            if l.startswith("## "):
                part = None
            dans = False
            continue
        if part is None:
            continue
        if re.match(r"^### M-\d+ — ", l):
            pb[part] += 1
            dans = False
            continue
        if l.startswith("- tentatives"):
            dans = True
            continue
        if l.startswith("- état :"):
            e = l[len("- état :"):].strip()
            etats["tenu" if e.startswith("tenu") else e] += 1
        if l.startswith("- "):
            dans = False
        if dans and l.startswith("  - "):
            tent[part] += 1
            a = "(écrit avant" in l
            s = "attendu : non écrit avant" in l
            fin = l.rstrip().rstrip(".").rstrip("⟧")
            i = next((k for k in ("juste", "fausse", "non vérifiable") if fin.endswith("— attente " + k)), None)
            if l.count("attendu : ") != 1 or a == s or (a and i is None) or (s and i is not None):
                anomalies.append(n)
            avant += a
            sans += s
            if a and i:
                issue[i] += 1
    return pb, tent, avant, sans, issue, etats, anomalies


def markdown(texte):
    pb, tent, avant, sans, issue, etats, anomalies = compter(texte)
    if anomalies:
        raise SystemExit(f"ARRET : tentatives mal formées aux lignes {anomalies}")
    o = ["| partition | problèmes | tentatives |", "|---|---|---|"]
    for p in pb:
        o.append(f"| {p} | {pb[p]} | {tent[p]} |")
    o.append(f"| total | {sum(pb.values())} | {sum(tent.values())} |")
    o.append("")
    o.append(f"- Tentatives avec une attente écrite avant : {avant}. Sans attente écrite avant : {sans}.")
    o.append(f"- Parmi les {avant} attentes écrites avant : {issue['juste']} justes, {issue['fausse']} fausses, {issue['non vérifiable']} non vérifiables.")
    o.append(f"- États : {etats['ouvert']} ouverts, {etats['tenu']} tenus, {etats['clos']} clos.")
    autres = {k: v for k, v in etats.items() if k not in ("ouvert", "tenu", "clos")}
    if autres:
        raise SystemExit(f"ARRET : états hors liste {autres}")
    return "\n".join(o)


if __name__ == "__main__":
    print(markdown(open(sys.argv[1], encoding="utf-8").read()))
