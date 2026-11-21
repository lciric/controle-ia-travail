#!/usr/bin/env python3
"""Lit une réponse Atom de l'interface d'arXiv et imprime une ligne par notice.
Usage : lire_arxiv.py FICHIER.xml [longueur_resume]"""
import sys, re
import xml.etree.ElementTree as ET
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
def main():
    f = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    root = ET.parse(f).getroot()
    for e in root.findall("a:entry", NS):
        ident = e.find("a:id", NS).text.rsplit("/abs/", 1)[-1]
        pub = e.find("a:published", NS).text[:10]
        upd = e.find("a:updated", NS).text[:10]
        title = re.sub(r"\s+", " ", e.find("a:title", NS).text).strip()
        auts = [a.find("a:name", NS).text.strip() for a in e.findall("a:author", NS)]
        cat = e.find("x:primary_category", NS).attrib.get("term", "?")
        aut = auts[0] + (" et al." if len(auts) > 1 else "") + f" ({len(auts)})"
        print(f"{ident}\t{pub}\t{upd}\t{cat}\t{title}\t{aut}")
        if n:
            s = re.sub(r"\s+", " ", e.find("a:summary", NS).text).strip()
            print("    " + s[:n])
if __name__ == "__main__":
    main()
