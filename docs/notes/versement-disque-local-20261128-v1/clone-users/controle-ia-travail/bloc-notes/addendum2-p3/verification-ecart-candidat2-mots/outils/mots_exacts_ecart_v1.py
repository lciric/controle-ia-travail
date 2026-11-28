"""Mots exacts de l'écart candidat 1 -> candidat 2 (addendum 2 de P3), vérifiés par programme.

Usage : python -I -B mots_exacts_ecart_v1.py RAPPORT_VC1 CANDIDAT1 CANDIDAT2 LIGNE_CANDIDAT2 SCRIPT_CANDIDAT2
  RAPPORT_VC1 : verification-candidat1-addendum2-P3-v1.md (contre-lecture 6), d'où sont extraits les mots des corrections.
  CANDIDAT1, CANDIDAT2 : les deux candidats. LIGNE_CANDIDAT2 : l'élément « Candidat 2 » de l'en-tête.
  SCRIPT_CANDIDAT2 : ecrire_candidat2_addendum2_v1.py, lu comme une donnée (ast.literal_eval de PAIRES ; jamais exécuté).

Ce que fait l'outil :
  1. Extrait de chaque bloc « **Correction » des constats VC1-01 à VC1-07 du rapport les actions « remplacer « A » par
     « B » » et « ajouter après l'entrée 5 « C » » (guillemets équilibrés, imbriqués compris), avec leur point (1., 2.).
  2. Normalise les espaces (toute suite d'espaces, retours à la ligne compris, devient une espace).
  3. Reconstruit le candidat 2 attendu depuis le candidat 1 : chaque ancien texte trouvé une seule fois, remplacé ;
     l'entrée 6 ajoutée après l'entrée 5 (chevron rempli par l'empreinte du rapport) ; l'élément « Candidat 2 » inséré
     avant « - Date (UTC) ». Compare au candidat 2 normalisé.
  4. Compare section par section (titres « ## ») les deux candidats octet pour octet ; liste les blocs du différentiel
     ligne à ligne et la section de chacun.
  5. Compare les paires du script aux mots du rapport (espaces normalisés).
N'importe rien du dépôt. N'écrit rien : imprime son journal.
"""
import ast
import difflib
import hashlib
import re
import sys
from pathlib import Path


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def guillemets(t, i):
    """t[i] == '«' ; rend (contenu, indice après le '»' fermant), guillemets imbriqués compris."""
    assert t[i] == "«"
    prof = 0
    for j in range(i, len(t)):
        if t[j] == "«":
            prof += 1
        elif t[j] == "»":
            prof -= 1
            if prof == 0:
                return t[i + 1:j].strip(), j + 1
    raise ValueError(f"guillemet non fermé à {i}")


def blocs_constats(rapport):
    """{id: texte du constat détaillé} pour chaque « ### VCx-yy »."""
    parts = re.split(r"^### (VC1-\d\d)\b.*$", rapport, flags=re.M)
    out = {}
    for ident, corps in zip(parts[1::2], parts[2::2]):
        corps = re.split(r"^## ", corps, flags=re.M)[0]
        out[ident] = corps
    return out


def actions(ident, corps):
    i = corps.find("**Correction")
    if i < 0:
        return []
    bloc = corps[i:]
    res = []
    # point courant : « 1. », « 2. », « 3. » en début de ligne
    points = [(m.start(), m.group(1)) for m in re.finditer(r"^\s*(\d)\.\s", bloc, flags=re.M)]

    def point(pos):
        p = None
        for s, n in points:
            if s <= pos:
                p = n
        return p

    for m in re.finditer(r"(?i)\bremplacer\s*«", bloc):
        a, fin = guillemets(bloc, m.end() - 1)
        m2 = re.match(r"\s*par\s*«", bloc[fin:])
        if not m2:
            raise ValueError(f"{ident} : « par « » attendu après {a[:40]!r}")
        b, fin2 = guillemets(bloc, fin + m2.end() - 1)
        res.append({"id": ident, "point": point(m.start()), "type": "remplacer", "ancien": a, "nouveau": b})
    for m in re.finditer(r"ajouter après l'entrée (\d+)\s*«", bloc):
        c, _ = guillemets(bloc, m.end() - 1)
        res.append({"id": ident, "point": point(m.start()), "type": f"ajouter après l'entrée {m.group(1)}",
                    "nouveau": c})
    return res


def sections_brutes(t):
    parts = re.split(r"^(## .+)$", t, flags=re.M)
    out = [("(en-tête)", parts[0])]
    for titre, corps in zip(parts[1::2], parts[2::2]):
        out.append((titre, corps))
    return out


def main(argv):
    rapport_p, c1_p, c2_p, ligne_p, script_p = map(Path, argv[1:6])
    rapport = rapport_p.read_text(encoding="utf-8")
    c1 = c1_p.read_text(encoding="utf-8")
    c2 = c2_p.read_text(encoding="utf-8")
    ligne = ligne_p.read_text(encoding="utf-8")
    sha = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (rapport_p, c1_p, c2_p, ligne_p, script_p)}
    for k, v in sha.items():
        print(f"sha256 {v}  {k}")
    sha_rapport = sha[rapport_p.name]
    compagnon = Path(str(rapport_p) + ".sha256").read_text(encoding="utf-8").split()[0]
    print(f"compagnon du rapport : {compagnon} ; égal au fichier : {compagnon == sha_rapport}")

    # 1. actions extraites du rapport
    blocs = blocs_constats(rapport)
    print(f"\n1. constats détaillés trouvés : {sorted(blocs)}")
    acts = []
    for ident in sorted(blocs):
        a = actions(ident, blocs[ident])
        print(f"   {ident} : {len(a)} action(s) de texte : "
              + ", ".join(f"point {x['point']} {x['type']}" for x in a))
        acts += a
    attendues = {("VC1-01", "1", "remplacer"), ("VC1-02", None, "remplacer"), ("VC1-03", "1", "remplacer"),
                 ("VC1-03", "2", "ajouter après l'entrée 5"), ("VC1-04", "1", "remplacer"),
                 ("VC1-04", "2", "remplacer"), ("VC1-05", None, "remplacer")}
    trouvees = {(x["id"], x["point"], x["type"]) for x in acts}
    print(f"   actions attendues (VC1-01 p1, VC1-02, VC1-03 p1 et p2, VC1-04 p1 et p2, VC1-05) = trouvées : "
          f"{attendues == trouvees} ; en trop : {sorted(map(str, trouvees - attendues))} ; "
          f"manquantes : {sorted(map(str, attendues - trouvees))}")
    for x in acts:
        if "ancien" in x:
            print(f"   [{x['id']} p{x['point']}] ancien : {norm(x['ancien'])}")
        print(f"   [{x['id']} p{x['point']}] nouveau : {norm(x['nouveau'])}")

    # 2-3. reconstruction normalisée
    print("\n2-3. reconstruction du candidat 2 depuis le candidat 1 (espaces normalisés)")
    n1 = norm(c1)
    occ = []
    for x in acts:
        if x["type"] == "remplacer":
            a = norm(x["ancien"])
            k = n1.count(a)
            pos = n1.find(a)
            occ.append((pos, pos + len(a), x["id"], x["point"]))
            print(f"   {x['id']} p{x['point']} : ancien texte trouvé {k} fois dans le candidat 1 (position {pos})")
    occ.sort()
    chev = all(occ[i][1] <= occ[i + 1][0] for i in range(len(occ) - 1))
    print(f"   anciens textes disjoints : {chev}")
    attendu = n1
    for x in acts:
        if x["type"] == "remplacer":
            a, b = norm(x["ancien"]), norm(x["nouveau"])
            assert attendu.count(a) == 1, (x["id"], x["point"])
            attendu = attendu.replace(a, b)
    # entrée 6 : le candidat 1 doit finir par l'entrée 5
    debut5 = c1.find("- **Contre-lecture 5**")
    fin_c1 = c1[debut5:]
    NL = "\n"
    dernier5 = debut5 > 0 and (NL + "- ") not in fin_c1[1:] and (NL + "#") not in fin_c1
    print(f"   candidat 1 : l'entrée 5 est le dernier élément du fichier : {dernier5}")
    e6 = [x for x in acts if x["type"].startswith("ajouter")][0]["nouveau"]
    print(f"   chevron de l'entrée 6 : {re.findall(r'<[^<>`]+>', e6)}")
    e6_rempli = e6.replace("<empreinte de ce rapport>", sha_rapport)
    attendu = attendu + " " + norm(e6_rempli)
    ancre = "- Date (UTC) : celle du commit de scellement, qui fait foi."
    assert attendu.count(ancre) == 1
    attendu = attendu.replace(ancre, norm(ligne) + " " + ancre)
    n2 = norm(c2)
    print(f"   candidat 2 normalisé = candidat 1 + corrections du rapport + entrée 6 + élément « Candidat 2 » : "
          f"{n2 == attendu}")
    if n2 != attendu:
        i = next((k for k in range(min(len(attendu), len(n2))) if attendu[k] != n2[k]), min(len(attendu), len(n2)))
        print(f"   premier écart au caractère {i} : attendu {attendu[max(0, i - 60):i + 80]!r}")
        print(f"   {'':28} lu      {n2[max(0, i - 60):i + 80]!r}")
    # élément « Candidat 2 » : octet pour octet, juste avant « - Date (UTC) »
    print(f"   élément « Candidat 2 » présent octet pour octet juste avant « - Date (UTC) » : "
          f"{c2.count(ligne + ancre) == 1}")
    # entrée 6 : à la fin du fichier, après l'entrée 5
    d6 = c2.find("- **Contre-lecture 6**")
    ok6 = (c2.count("- **Contre-lecture 6**") == 1 and d6 > c2.find("- **Contre-lecture 5**")
           and (NL + "- ") not in c2[d6 + 1:])
    print(f"   entrée 6 : une seule, après l'entrée 5, dernière du fichier : {ok6}")
    print(f"   entrée 6 (normalisée) = recommandation de VC1-03 point 2, chevron rempli par {sha_rapport[:12]}… : "
          f"{norm(c2[d6:]) == norm(e6_rempli)}")

    # 4. différentiel brut et sections
    print("\n4. différentiel ligne à ligne et sections")
    l1, l2 = c1.splitlines(keepends=True), c2.splitlines(keepends=True)
    sm = difflib.SequenceMatcher(None, l1, l2, autojunk=False)

    def section_de(lignes, i):
        titre = "(en-tête)"
        for k in range(min(i, len(lignes) - 1), -1, -1):
            if lignes[k].startswith("## "):
                titre = lignes[k].strip()
                break
        return titre

    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != "equal":
            print(f"   {tag} c1 l.{i1 + 1}-{i2} -> c2 l.{j1 + 1}-{j2} ; section {section_de(l1, i1)!r} / "
                  f"{section_de(l2, j1)!r}")
            nouvelles = l2[j1:j2]
            mal = [k + j1 + 1 for k, x in enumerate(nouvelles) if not (x.startswith("- ") or x.startswith("  "))]
            print(f"      lignes nouvelles hors forme de liste (ni « - » ni deux espaces) : {mal}")
    s1, s2 = sections_brutes(c1), sections_brutes(c2)
    print(f"   titres de sections égaux : {[t for t, _ in s1] == [t for t, _ in s2]}")
    for (t1, b1), (t2, b2) in zip(s1, s2):
        h1, h2 = hashlib.sha256(b1.encode()).hexdigest(), hashlib.sha256(b2.encode()).hexdigest()
        print(f"   {t1!r:60} {'égale' if b1 == b2 else 'CHANGE'} ({h1[:12]} / {h2[:12]})")
    # en-tête : hors des éléments « Candidat 1 » et « Candidat 2 »
    def sans_candidats(entete):
        out, saute = [], False
        for x in entete.splitlines(keepends=True):
            if x.startswith("- "):
                saute = x.startswith("- Candidat 1 :") or x.startswith("- Candidat 2 :")
            if not saute:
                out.append(x)
        return "".join(out)
    print(f"   en-tête hors éléments « Candidat 1 » et « Candidat 2 » : égal octet pour octet : "
          f"{sans_candidats(s1[0][1]) == sans_candidats(s2[0][1])}")
    # contre-lecture : entrées 1 à 4 égales
    def entrees(corps):
        parts = re.split(r"^(- \*\*Contre-lecture \d+\*\*)", corps, flags=re.M)
        return {t: b for t, b in zip(parts[1::2], parts[2::2])}
    cl1 = entrees(dict(s1)["## Contre-lecture"])
    cl2 = entrees(dict(s2)["## Contre-lecture"])
    print(f"   entrées : c1 {list(cl1)} ; c2 {list(cl2)}")
    for t in cl1:
        print(f"   {t} : {'égale' if cl1[t] == cl2.get(t) else 'CHANGE'}")

    # 5. paires du script
    print("\n5. paires du script (lues par ast.literal_eval, jamais exécutées)")
    arbre = ast.parse(script_p.read_text(encoding="utf-8"))
    paires = None
    for n in arbre.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "PAIRES" for t in n.targets):
            paires = ast.literal_eval(n.value)
    print(f"   {len(paires)} paires")
    for k, (a, b) in enumerate(paires):
        na, nb = norm(a), norm(b)
        # quels anciens textes du rapport la paire couvre-t-elle ?
        couverts = [f"{x['id']} p{x['point']}" for x in acts if x["type"] == "remplacer" and norm(x["ancien"]) in na]
        # reconstruire le nouveau attendu : appliquer au texte ancien de la paire les remplacements du rapport
        r = na
        for x in acts:
            if x["type"] == "remplacer" and norm(x["ancien"]) in r:
                r = r.replace(norm(x["ancien"]), norm(x["nouveau"]))
        if any(x["type"].startswith("ajouter") for x in acts) and "Contre-lecture 6" in nb:
            r = r + " " + norm(e6_rempli)
            couverts.append("VC1-03 p2 (entrée 6)")
        print(f"   paire {k + 1} : couvre {couverts} ; nouveau = ancien + mots du rapport : {r == nb}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
