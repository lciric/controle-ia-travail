#!/usr/bin/env python3
"""Contre-lecture v1 de la synthèse DiscoveryAgent : contrôles par programme.

Se lance avec `python3 -I`, hors des dépôts des auteurs :
    python3 -I verifier_contre_lecture_v1.py RACINE_DU_DEPOT

Lecture seule : aucune écriture, aucun réseau. Rien des dépôts des auteurs
n'est exécuté ; ils ne sont lus que par `git show`, `git grep` et `git ls-tree`.

Quatre contrôles :
  1. la table d'annexe de la note est-elle, ligne à ligne, celle que produit le
     programme du rédacteur en mode --table ?
  2. les citations du contre-lecteur (registre JSON voisin) se retrouvent-elles
     dans leur source, avec la même normalisation que le rédacteur ?
  3. chaque texte « avant » des corrections de la contre-lecture se trouve-t-il
     exactement une fois dans la note, et toutes les corrections
     s'appliquent-elles, dans l'ordre, sans se gêner ?
  4. tout identifiant cité dans un texte « après » existe-t-il dans l'un des deux
     registres, et ceux du contre-lecteur sont-ils marqués « a_verser » ?
"""
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ICI = Path(__file__).resolve().parent
DOSSIER = ICI.parent
NOTE = DOSSIER / "synthese-discoveryagent-pour-l-organisme-v1.md"
CONTRE_LECTURE = DOSSIER / "contre-lecture-synthese-discoveryagent-v1.md"
PROG_REDACTEUR = DOSSIER / "outils-synthese-v1" / "verifier_citations_synthese_v1.py"
REG_REDACTEUR = DOSSIER / "outils-synthese-v1" / "citations-synthese-v1.json"
REG_CONTRE = ICI / "citations-contre-lecture-v1.json"
TITRE_TABLE = "## Annexe — table des citations vérifiées"
MOTIF_ID = re.compile(r"\b([PACXN]\d{2})\b")


def norm(texte, markdown=False):
    """Même normalisation que le programme du rédacteur."""
    t = unicodedata.normalize("NFKC", texte)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), (" ", " "), (" ", " ")):
        t = t.replace(a, b)
    if markdown:
        t = t.replace("*", "").replace("`", "")
    return re.sub(r"\s+", " ", t).strip()


def git(depot, *args):
    r = subprocess.run(["git", "-C", str(depot), *args], capture_output=True)
    if r.returncode not in (0, 1):
        raise RuntimeError(r.stderr.decode("utf-8", "replace")[:300])
    return r.stdout.decode("utf-8", "replace")


def sha(octets):
    return hashlib.sha256(octets).hexdigest()


def controle_table(racine):
    print("== 1. Table d'annexe de la note contre la sortie --table du programme du rédacteur")
    r = subprocess.run([sys.executable, "-I", str(PROG_REDACTEUR), str(racine), "--table"],
                       capture_output=True)
    produite = [l for l in r.stdout.decode("utf-8").splitlines() if l.startswith("|")]
    corps = NOTE.read_text(encoding="utf-8")
    note = [l for l in corps.split(TITRE_TABLE, 1)[1].splitlines() if l.startswith("|")]
    print(f"lignes produites : {len(produite)} ; lignes de la note : {len(note)}")

    def barres_rendues(ligne):
        # rend en barre oblique toute barre verticale prise entre accents graves (colonne « lieu »)
        return re.sub(r"`[^`]*`", lambda m: m.group(0).replace("|", "/"), ligne)

    ecarts, benins = [], []
    for i, (a, b) in enumerate(zip(produite, note)):
        if a == b:
            continue
        (benins if barres_rendues(a) == b else ecarts).append((i, a, b))
    if len(produite) != len(note):
        ecarts.append((-1, f"{len(produite)} lignes", f"{len(note)} lignes"))
    for i, a, b in benins:
        print(f"  BÉNIN ligne {i} (barre verticale du motif rendue à la main par une barre oblique) :"
              f"\n    produite : {a}\n    note     : {b}")
    for i, a, b in ecarts[:10]:
        print(f"  ÉCART ligne {i} :\n    produite : {a}\n    note     : {b}")
    print(f"RÉSULTAT 1 : {len(produite) - len(benins) - len(ecarts)} lignes identiques ; "
          f"{len(benins)} retouche(s) bénigne(s) (constat m19) ; {len(ecarts)} écart(s) réel(s)")
    return len(ecarts)


def controle_citations(racine, reg):
    print("== 2. Citations du contre-lecteur dans leur source")
    src = reg["sources"]
    pages = {}
    for nom in ("papier", "annexe"):
        brut = (racine / src[nom]["fichier"]).read_bytes()
        pages[nom] = brut.decode("utf-8").split("\f")
        print(f"source {nom} : sha256 {sha(brut)} ; pages {len(pages[nom])}")
    ok = echec = 0
    for c in reg["citations"]:
        cid, s = c["id"], c["src"]
        trouve, lieu = False, ""
        try:
            if s in ("papier", "annexe"):
                lieu = f"{s}, p. {c['page']}"
                trouve = norm(c["extrait"]) in norm(pages[s][c["page"] - 1])
            elif s == "code":
                a, b = c["lignes"]
                lieu = f"code, {c['fichier']}, l. {a}-{b}"
                txt = git(src["code"]["depot"], "show", f"{src['code']['commit']}:{c['fichier']}").split("\n")
                trouve = norm(c["extrait"], True) in norm("\n".join(txt[a - 1:b]), True)
            elif s in ("organisme", "papierC"):
                lieu = f"{c['fichier']} (branche {src[s]['ref']})"
                txt = git(racine, "show", f"{src[s]['ref']}:{c['fichier']}")
                trouve = norm(c["extrait"], True) in norm(txt, True)
            elif s == "disque":
                lieu = c["fichier"]
                txt = (racine / c["fichier"]).read_text(encoding="utf-8")
                trouve = norm(c["extrait"], True) in norm(txt, True)
            elif s == "absence":
                d = src[c["depot"]]
                sortie = git(d["depot"], "grep", "-n", "-i", "-E", c["motif_contenu"], d["commit"], "--", *c["sous"])
                touches = [l.split(":", 3) for l in sortie.splitlines() if l]
                fichiers = sorted({t[1] for t in touches})
                trouve = fichiers == sorted(c["attendu_fichiers"])
                if "attendu_occurrences" in c:
                    trouve = trouve and len(touches) == c["attendu_occurrences"]
                lieu = (f"dépôt {c['depot']}, motif {c['motif_contenu']!r} sous {c['sous']} : "
                        f"fichiers {fichiers or 'aucun'}, occurrences {len(touches)}")
            else:
                lieu = "source inconnue"
        except Exception as e:  # une citation illisible est un échec, jamais un repli
            lieu += f" [erreur : {e}]"
            trouve = False
        ok += trouve
        echec += (not trouve)
        print(f"{'OK   ' if trouve else 'ÉCHEC'} {cid} — {lieu}")
    print(f"RÉSULTAT 2 : {ok} retrouvée(s), {echec} échec(s), sur {len(reg['citations'])}")
    return echec


def couples():
    """Lit les couples « > AVANT : » / « > APRÈS : » de la contre-lecture, dans l'ordre."""
    lignes = CONTRE_LECTURE.read_text(encoding="utf-8").splitlines()
    res, avant, nom = [], None, None
    for l in lignes:
        m = re.match(r"^#{3,4} (Correction [^ ]+)", l)
        if m:
            nom = m.group(1)
        if l.startswith("> AVANT : "):
            avant = l[len("> AVANT : "):]
        elif l.startswith("> APRÈS : "):
            if avant is None:
                raise ValueError(f"APRÈS sans AVANT près de {nom}")
            res.append((nom, avant, l[len("> APRÈS : "):]))
            avant = None
    if avant is not None:
        raise ValueError("AVANT sans APRÈS en fin de fichier")
    return res


def controle_couples(ids_connus, reg_contre):
    print("== 3. Couples « avant → après » de la contre-lecture")
    note = NOTE.read_text(encoding="utf-8")
    liste = couples()
    print(f"couples lus : {len(liste)}")
    echec = 0
    for nom, avant, _ in liste:
        n = note.count(avant)
        if n != 1:
            echec += 1
            print(f"ÉCHEC {nom} : « avant » trouvé {n} fois dans la note : {avant[:90]}…")
    print(f"unicité dans la note d'origine : {len(liste) - echec} sur {len(liste)}")
    texte, echec_app = note, 0
    for nom, avant, apres in liste:
        n = texte.count(avant)
        if n != 1:
            echec_app += 1
            print(f"ÉCHEC d'application {nom} : « avant » trouvé {n} fois au moment de l'appliquer")
            continue
        texte = texte.replace(avant, apres)
    print(f"application dans l'ordre : {len(liste) - echec_app} sur {len(liste)}")
    print("== 4. Identifiants des textes « après »")
    a_verser = {c["id"] for c in reg_contre["citations"] if c.get("a_verser")}
    tous_contre = {c["id"] for c in reg_contre["citations"]}
    cites = set()
    for _, _, apres in liste:
        cites |= set(MOTIF_ID.findall(apres))
    inconnus = sorted(cites - ids_connus)
    neufs = sorted(cites & tous_contre)
    non_marques = sorted(set(neufs) - a_verser)
    marques_inutiles = sorted(a_verser - cites)
    print(f"identifiants cités dans les « après » : {len(cites)} ; inconnus des deux registres : {inconnus or 'aucun'}")
    print(f"identifiants neufs (registre du contre-lecteur) : {len(neufs)} ; non marqués « a_verser » : {non_marques or 'aucun'}")
    print(f"marqués « a_verser » mais cités dans aucun « après » : {marques_inutiles or 'aucun'}")
    apres_ids = set(MOTIF_ID.findall(texte.split(TITRE_TABLE)[0]))
    print(f"note corrigée (avant la table) : {len(apres_ids)} identifiants cités ; empreinte du texte corrigé {sha(texte.encode('utf-8'))}")
    return echec + echec_app + len(inconnus) + len(non_marques) + len(marques_inutiles)


def main():
    racine = Path(sys.argv[1]).resolve()
    print(f"note : {NOTE.name} sha256 {sha(NOTE.read_bytes())}")
    print(f"contre-lecture : {CONTRE_LECTURE.name} sha256 {sha(CONTRE_LECTURE.read_bytes()) if CONTRE_LECTURE.exists() else 'absente'}")
    reg_r = json.loads(REG_REDACTEUR.read_text(encoding="utf-8"))
    reg_c = json.loads(REG_CONTRE.read_text(encoding="utf-8"))
    ids_r = {c["id"] for c in reg_r["citations"]}
    ids_c = {c["id"] for c in reg_c["citations"]}
    doublons = sorted(ids_r & ids_c)
    print(f"registres : rédacteur {len(ids_r)} identifiants, contre-lecteur {len(ids_c)} ; doublons : {doublons or 'aucun'}")
    total = len(doublons)
    total += controle_table(racine)
    total += controle_citations(racine, reg_c)
    total += controle_couples(ids_r | ids_c, reg_c)
    print(f"BILAN : {total} échec(s) au total")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
