#!/usr/bin/env python3
"""Portage par programme, mot pour mot, des corrections d'une contre-lecture
dans une conception (classe B, outil de correction ; aucun appel réseau).

Usage : python portage-conception-N-v1.py   (depuis n'importe où)

Le script :
- lit, par programme, chaque correction (ancien, nouveau) dans la contre-lecture ;
- exige que chaque ancien texte figure exactement une fois dans la v1
  (et une fois dans le texte courant au moment de l'appliquer) ; sinon il
  s'arrête et n'écrit rien ;
- applique les corrections dans l'ordre de la contre-lecture ;
- vérifie que chaque nouveau texte est présent dans la v2, et que défaire
  les corrections dans l'ordre inverse redonne exactement la v1 ;
- refuse d'écraser un fichier existant ;
- écrit la v2 et un rapport JSON à côté.
Les corrections qui n'ont pas la forme « ancien, nouveau » (ajouts, notes)
ne sont pas portées : elles sont listées dans le rapport avec leur raison.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- réglages
NUMERO = "2"
TITRE = "Conception 2 — les épreuves du devin"
FORMAT = "cellule"  # « cellule » (table, ancien → nouveau dans la cellule) ou « blocs » (C-n, blocs clôturés)
RACINE = Path(__file__).resolve().parents[4]
BASE = "docs/notes/chantiers-21-novembre-v1"
CONCEPTION = f"{BASE}/reponses-fable-v1/demande-{NUMERO}/relecture-fable-api.md"
CONTRE_LECTURE = f"{BASE}/contre-lectures-v1/contre-lecture-reponse-2-epreuves-du-devin-opus-v1.md"
SORTIE = f"{BASE}/conceptions-v2/conception-2-epreuves-du-devin-v2.md"
RAPPORT = SORTIE[:-3] + "-rapport-portage.json"
MARQUE_FIN_EN_TETE = "<!-- fin de l'en-tête de la v2 ; le texte de la v1 corrigé suit -->"


class Arret(Exception):
    pass


def sha256(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def verifier_compagnon(chemin: Path) -> str:
    comp = chemin.with_name(chemin.name + ".sha256")
    if not comp.exists():
        raise Arret(f"compagnon absent : {comp}")
    attendu = comp.read_text(encoding="utf-8").split()[0]
    vu = sha256(chemin)
    if attendu != vu:
        raise Arret(f"empreinte non conforme pour {chemin} : {vu} contre {attendu}")
    return vu


# ------------------------------------------------- lecture des corrections
def decouper_ligne(ligne: str):
    """Cellules d'une ligne de table ; « \\| » est une barre échappée."""
    cellules = re.split(r"(?<!\\)\|", ligne.strip())
    return [c.strip() for c in cellules[1:-1]]


def jetons_guillemets(cellule: str):
    """Suite (étiquette, contenu) : l'étiquette est le texte hors guillemets qui
    précède un passage « … » de premier niveau (guillemets imbriqués gardés)."""
    jetons, etiquette, contenu, prof = [], "", "", 0
    for ch in cellule:
        if ch == "«":
            if prof > 0:
                contenu += ch
            prof += 1
        elif ch == "»":
            if prof == 0:
                raise Arret(f"guillemet fermant sans ouvrant dans : {cellule[:80]}")
            prof -= 1
            if prof == 0:
                if not (contenu.startswith(" ") and contenu.endswith(" ")):
                    raise Arret(f"passage cité sans espaces de bord : {contenu[:80]}")
                jetons.append((etiquette, contenu[1:-1].replace("\\|", "|")))
                etiquette, contenu = "", ""
            else:
                contenu += ch
        elif prof > 0:
            contenu += ch
        else:
            etiquette += ch
    if prof != 0:
        raise Arret(f"guillemets non équilibrés dans : {cellule[:80]}")
    return jetons, etiquette


def lire_cellules(texte: str):
    debut = texte.index("## Table des constats")
    suite = texte[debut:]
    fin = re.search(r"\n## ", suite[3:])
    table = suite[: fin.start() + 3] if fin else suite
    portees, non_portees = [], []
    for ligne in table.splitlines():
        if not re.match(r"^\|\s*\d+\s*\|", ligne):
            continue
        cel = decouper_ligne(ligne)
        num, gravite, lieu, correction = cel[0], cel[1].strip("*"), cel[2], cel[-1]
        jetons, reste = jetons_guillemets(correction)
        if reste.strip(" .;,→—"):
            raise Arret(f"constat {num} : texte après le dernier passage cité : {reste!r}")
        etat, courant, rang = None, None, 0
        for etiquette, contenu in jetons:
            e = etiquette.strip()
            if re.search(r"\bAncien\b", e):
                if etat == "ancien":
                    raise Arret(f"constat {num} : deux anciens de suite")
                if etat == "ajout":
                    non_portees.append(courant)
                rang += 1
                courant = {"constat": int(num), "rang": rang, "gravite": gravite, "lieu": lieu,
                           "ancien": contenu, "nouveau": None, "mode": "simple"}
                etat = "ancien"
            elif re.search(r"\bNouveau\b", e):
                if etat != "ancien":
                    raise Arret(f"constat {num} : nouveau sans ancien")
                courant["nouveau"] = contenu
                if "deux lignes" in e:
                    courant["mode"] = "deux lignes, réunies par un saut de ligne"
                    etat = "nouveau_multi"
                else:
                    portees.append(courant)
                    etat = "nouveau"
            elif e.strip(" .;,→—") == "et" and etat == "nouveau_multi":
                courant["nouveau"] += "\n" + contenu
                portees.append(courant)
                etat = "nouveau"
            elif re.search(r"\bAjouter\b", e):
                if etat in ("ancien", "nouveau_multi"):
                    raise Arret(f"constat {num} : correction incomplète avant un ajout")
                if etat == "ajout":
                    non_portees.append(courant)
                courant = {"constat": int(num), "gravite": gravite, "lieu": lieu,
                           "texte": f"{e} « {contenu} »",
                           "raison": "ajout sans ancien texte (« Ajouter … ») : hors format ancien, nouveau ; non inventé"}
                etat = "ajout"
            elif etat == "ajout" and e.strip(" .;,→—:") == "":
                courant["texte"] += f" {e} « {contenu} »".replace("  ", " ")
            else:
                raise Arret(f"constat {num} : étiquette inconnue {e!r}")
        if etat == "ajout":
            non_portees.append(courant)
        elif etat in ("ancien", "nouveau_multi"):
            raise Arret(f"constat {num} : correction incomplète")
        if not jetons:
            non_portees.append({"constat": int(num), "gravite": gravite, "lieu": lieu,
                                "texte": correction, "raison": "aucun passage cité ancien, nouveau"})
    return portees, non_portees


def lire_blocs(texte: str):
    motif = re.compile(
        r"^\*\*C-(\d+)\*\* \(constat (\d+)\)\nAncien :\n```text\n(.*?)\n```\nNouveau :\n```text\n(.*?)\n```",
        re.S | re.M)
    blocs = list(motif.finditer(texte))
    entetes = re.findall(r"^\*\*C-\d+\*\*", texte, re.M)
    if len(blocs) != len(entetes):
        raise Arret(f"{len(entetes)} en-têtes C-n mais {len(blocs)} blocs lisibles")
    # table : gravité, lieu, renvois
    debut = texte.index("## Table des constats")
    fin = texte.index("## Corrections mot pour mot")
    info, renvois, non_portees = {}, set(), []
    for ligne in texte[debut:fin].splitlines():
        if not re.match(r"^\|\s*\d+\s*\|", ligne):
            continue
        cel = decouper_ligne(ligne)
        num = int(cel[0])
        info[num] = (cel[1].strip("*"), cel[2])
        ids = re.findall(r"C-(\d+)", cel[-1])
        if not ids or re.sub(r"[C\-\d,\s]", "", cel[-1]):
            non_portees.append({"constat": num, "gravite": cel[1], "lieu": cel[2], "texte": cel[-1],
                                "raison": "cellule de correction sans renvoi à un bloc ancien, nouveau"})
        renvois.update(int(i) for i in ids)
    portees = []
    for b in blocs:
        cid, cst = int(b.group(1)), int(b.group(2))
        g, l = info.get(cst, ("?", "?"))
        portees.append({"constat": cst, "rang": cid, "bloc": f"C-{cid}", "gravite": g, "lieu": l,
                        "ancien": b.group(3), "nouveau": b.group(4), "mode": "simple"})
    manquants = renvois - {p["rang"] for p in portees}
    if manquants:
        raise Arret(f"blocs annoncés par la table mais absents : {sorted(manquants)}")
    return portees, non_portees


# ------------------------------------------------------------------ portage
def ident(c):
    return c.get("bloc") or f"constat {c['constat']}, correction {c['rang']}"


def principal():
    conc, cl = RACINE / CONCEPTION, RACINE / CONTRE_LECTURE
    sortie, rapport = RACINE / SORTIE, RACINE / RAPPORT
    for p in (sortie, rapport):
        if p.exists():
            raise Arret(f"refus d'écraser un fichier existant : {p}")
    sha_conc, sha_cl = verifier_compagnon(conc), verifier_compagnon(cl)
    v1 = conc.read_text(encoding="utf-8")
    texte_cl = cl.read_text(encoding="utf-8")
    portees, non_portees = (lire_cellules if FORMAT == "cellule" else lire_blocs)(texte_cl)
    if not portees:
        raise Arret("aucune correction lue")
    if MARQUE_FIN_EN_TETE in v1:
        raise Arret("la marque de fin d'en-tête figure déjà dans la v1")

    # 1. chaque ancien exactement une fois dans la v1 (tous examinés avant arrêt)
    fautes = []
    for c in portees:
        n = v1.count(c["ancien"])
        c["occurrences_dans_v1"] = n
        if n != 1:
            fautes.append(f"{ident(c)} : ancien texte trouvé {n} fois dans la v1 : « {c['ancien'][:120]} »")
    if fautes:
        raise Arret("anciens textes introuvables ou en double, aucun fichier écrit :\n  " + "\n  ".join(fautes))

    # 2. application dans l'ordre
    corps = v1
    for c in portees:
        n = corps.count(c["ancien"])
        if n != 1:
            raise Arret(f"{ident(c)} : ancien texte trouvé {n} fois au moment de l'appliquer")
        corps = corps.replace(c["ancien"], c["nouveau"], 1)

    # 3. vérifications : nouveaux présents ; défaire dans l'ordre inverse redonne la v1
    for c in portees:
        if c["nouveau"] not in corps:
            raise Arret(f"{ident(c)} : nouveau texte absent de la v2")
    defait = corps
    for c in reversed(portees):
        n = defait.count(c["nouveau"])
        if n != 1:
            raise Arret(f"{ident(c)} : nouveau texte trouvé {n} fois en défaisant")
        defait = defait.replace(c["nouveau"], c["ancien"], 1)
    if defait != v1:
        raise Arret("défaire les corrections ne redonne pas exactement la v1")

    # 4. en-tête et écriture
    sha_script = sha256(Path(__file__).resolve())
    lignes = [
        f"# {TITRE} — v2",
        "",
        f"- Part de la v1 : `{CONCEPTION}` — sha256 {sha_conc} (compagnon vérifié).",
        f"- Contre-lecture : `{CONTRE_LECTURE}` — sha256 {sha_cl} (compagnon vérifié).",
        f"- Corrections portées par programme, mot pour mot, par `{BASE}/conceptions-v2/{Path(__file__).name}` — sha256 {sha_script}. "
        "Chaque ancien texte figurait une seule fois dans la v1 ; chaque nouveau texte est présent ici ; défaire les corrections dans l'ordre inverse redonne exactement la v1.",
        f"- Rapport : `{RAPPORT}`.",
        f"- Corrections portées ({len(portees)}), dans l'ordre :",
    ]
    for c in portees:
        mode = "" if c["mode"] == "simple" else f" ; nouveau en {c['mode']}"
        lignes.append(f"  - {ident(c)} — {c['gravite']} — lieu : {c['lieu']}{mode}")
    lignes.append(f"- Corrections non portées ({len(non_portees)}) : "
                  + ("; ".join(f"constat {c['constat']} ({c['raison'].split(' :')[0]})" for c in non_portees) or "aucune")
                  + " — détail au rapport.")
    lignes += ["", MARQUE_FIN_EN_TETE, ""]
    v2 = "\n".join(lignes) + "\n" + corps
    # contrôle : le corps extrait de la v2 est bien le texte corrigé
    if v2.split(MARQUE_FIN_EN_TETE + "\n\n", 1)[1] != corps:
        raise Arret("découpe de l'en-tête non conforme")

    with open(sortie, "x", encoding="utf-8") as f:
        f.write(v2)
    sha_v2 = sha256(sortie)
    doc = {
        "outil": f"{BASE}/conceptions-v2/{Path(__file__).name}",
        "sha256_outil": sha_script,
        "conception_v1": {"chemin": CONCEPTION, "sha256": sha_conc},
        "contre_lecture": {"chemin": CONTRE_LECTURE, "sha256": sha_cl},
        "conception_v2": {"chemin": SORTIE, "sha256": sha_v2},
        "verifications": {
            "chaque_ancien_une_fois_dans_v1": True,
            "chaque_nouveau_present_dans_v2": True,
            "defaire_dans_l_ordre_inverse_redonne_v1": True,
        },
        "nombre_portees": len(portees),
        "nombre_non_portees": len(non_portees),
        "portees": [{k: v for k, v in c.items()} | {"identifiant": ident(c)} for c in portees],
        "non_portees": non_portees,
    }
    with open(rapport, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"v2 écrite : {SORTIE} — sha256 {sha_v2}")
    print(f"portées : {len(portees)} ; non portées : {len(non_portees)}")
    for c in non_portees:
        print(f"  non portée : constat {c['constat']} — {c['raison']}")
    print(f"rapport : {RAPPORT}")


if __name__ == "__main__":
    try:
        principal()
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(2)
