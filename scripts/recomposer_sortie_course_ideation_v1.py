"""Recompose, hors du dépôt, le dossier de sortie d'une course de l'organisme d'idéation sur les organismes discrets à
partir de ses copies scellées (`runs/…/copies/sortie--…`), pour que le bras du juge externe différé puisse le lire.

- Chaque copie `sortie--a--b.json` est vérifiée par son sceau puis écrite en `SORTIE/a/b.json` avec son compagnon ;
  aucun contenu n'est affiché (cloisonnement).
- `noyau/modeles.json` n'est pas dans les copies des lanceurs v12 à v14 : il est **reconstruit** du manifeste de départ
  (`par_auteur` : proposeurs externes puis internes ; `par_juge` : juges internes puis externes, au modèle de la course),
  au format de `ecrire_json_scelle` de l'orchestrateur, et recoupé avec `lecture-course.json` (modèle de chaque juge
  rendu). Aucune empreinte d'origine n'existe pour lui : la reconstruction est déclarée dans `RECOMPOSITION.json`.
- Le dossier de l'agent de chaque juge externe (`juges-bras-rapporte/ETIQUETTE/`), que la course crée vide et où le bras
  lance sa commande, est recréé : sans lui le bras échoue après le contrôle et se verrouille (essai à blanc du 18 novembre).
- Toute pièce lue par le bras et absente des copies fait refuser.

Usage : python3 -I -B scripts/recomposer_sortie_course_ideation_v1.py DOSSIER_DU_RUN DESTINATION_NEUVE
Codes : 0 recomposé ; 2 refus.
"""
import hashlib
import json
import sys
from pathlib import Path

LUES_PAR_LE_BRAS = ("fiches-validees.json", "notes-par-juge.json", "doublons-par-juge.json", "lecture-course.json",
                    "manifeste-depart.json", "manifeste-fin.json", "noyau/cles-anonymisation-par-juge.json",
                    "noyau/temoins-servis.json")


class Refus(Exception):
    pass


def sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def ecrire(chemin: Path, octets: bytes) -> str:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_bytes(octets)
    Path(str(chemin) + ".sha256").write_text(f"{sha(octets)}  {chemin.name}\n", encoding="utf-8")
    return sha(octets)


def recomposer(run: Path, dest: Path) -> int:
    copies = run / "copies"
    if dest.exists():
        raise Refus(f"{dest} existe déjà")
    pieces = {}
    for c in sorted(copies.glob("sortie--*")):
        if c.name.endswith(".sha256"):
            continue
        octets = c.read_bytes()
        compagnon = Path(str(c) + ".sha256")
        if not compagnon.exists() or compagnon.read_text(encoding="utf-8").split()[0] != sha(octets):
            raise Refus(f"sceau absent ou faux : {c.name}")
        pieces["/".join(c.name.split("--")[1:])] = octets
    manquantes = [p for p in LUES_PAR_LE_BRAS if p not in pieces]
    if manquantes:
        raise Refus(f"pièces lues par le bras absentes des copies : {manquantes}")
    depart = json.loads(pieces["manifeste-depart.json"])["reglages"]
    fin = json.loads(pieces["manifeste-fin.json"])["reglages"]
    if fin.get("erreur") or not fin.get("en_attente_bras"):
        raise Refus("la course n'est pas en attente du bras (erreur, ou bras non attendu)")
    externes = [e for e, _ in depart["juges_externes"]]
    for e in externes:
        if f"juges-bras-rapporte/traces-{e}/consigne-en-attente.md" not in pieces:
            raise Refus(f"consigne en attente de {e} absente des copies")
    par_auteur = {e: m for e, m, *_ in depart["proposeurs_externes"]}
    par_auteur.update({e: m for e, m in depart["proposeurs"]})
    par_juge = {e: m for e, m in depart["juges"]}
    par_juge.update({e: m for e, m in depart["juges_externes"]})
    rendus = json.loads(pieces["lecture-course.json"]).get("auto_preference") or {}
    for j, l in rendus.items():
        if par_juge.get(j) != l.get("modele"):
            raise Refus(f"modèle du juge {j} : manifeste de départ {par_juge.get(j)!r} ≠ lecture de la course {l.get('modele')!r}")
    if not rendus:
        raise Refus("lecture de la course sans auto-préférence : rien pour recouper les modèles")
    modeles = (json.dumps({"par_auteur": par_auteur, "par_juge": par_juge}, ensure_ascii=False, indent=2, sort_keys=True,
                          allow_nan=False) + "\n").encode("utf-8")
    sortie = dest / "sortie"
    empreintes = {rel: ecrire(sortie / rel, octets) for rel, octets in pieces.items()}
    reconstruit = ecrire(sortie / "noyau" / "modeles.json", modeles)
    for e in externes:  # dossier de l'agent du juge externe, créé vide par la course : le bras y lance sa commande
        (sortie / "juges-bras-rapporte" / e).mkdir(parents=True, exist_ok=True)
    (dest / "RECOMPOSITION.json").write_text(json.dumps({
        "run": run.name, "copies_recomposees": empreintes,
        "reconstruit_sans_empreinte_d_origine": {"noyau/modeles.json": reconstruit},
        "regle": "par_auteur = proposeurs externes puis internes ; par_juge = juges internes puis externes au modèle de la "
                 "course ; recoupé avec lecture-course.json"}, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"recomposé : {sortie} ; {len(empreintes)} copies ; noyau/modeles.json reconstruit {reconstruit[:8]}… ; "
          f"juges externes {externes}")
    return 0


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise Refus("usage : DOSSIER_DU_RUN DESTINATION_NEUVE")
        sys.exit(recomposer(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()))
    except Refus as e:
        print(f"REFUS : {e}")
        sys.exit(2)
