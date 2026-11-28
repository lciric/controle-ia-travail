"""Préparation de l'arbre du versement C de P4-instrument, v1 (préparateur neuf, session 16).

Copie chaque pièce déjà écrite sous son chemin final dans ARBRE, vérifie l'empreinte de la source contre son compagnon
quand il existe et contre l'empreinte citée quand un document en cite une, écrit le compagnon `.sha256` au nom final
(format de `sha256sum` : « <hex>  <nom de base> »). N'écrase rien (R12). N'écrit que sous le dossier de préparation.
Écrit aussi `etat-pieces-v1.json` (une entrée par chemin de C) et `liste-chemins-C-prets-v1.txt`.
Usage : python3 -B preparer_arbre_c_v1.py (aucun argument)
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True

H = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument")
PREP = H / "versement-C-preparation"
ARBRE = PREP / "arbre"
A_NOMMER = PREP / "pieces-a-nommer"
CL = "prereg/contre-lectures"
VERSEES = "docs/procedures/P4-instrument-v1"
TOK = "donnees/P4-tokeniseur-v1"

# empreintes citées par un document (vérification croisée ; None = aucune citation connue)
CITEES = {
    "contre-lecture-R2-P4-instrument-brouillon1-v1.md": "108a8d1ffd0a892c123608af237c824e2bc40545d4e54e5e5b7dcb9a37835420",  # candidat 1
    "P4-instrument-v1-brouillon1.md": "41e5f035616e7cd3a233b680af06ba2a97c517a41d92f2042fde746aa85a48fd",                    # candidat 1
    "P4-instrument-v1-brouillon3.md": "2ec30d6860838f5b9e9c2e637906101a8b0d2ad2a1df2cfdc355bf552374cd4c",                    # candidat 1
    "verification-corrections-brouillons2-3-P4-v1.md": "9c94c2205b3f08e522917fd7c078748f8dc583fe4242ed9a26c325af71e7228e",   # candidat 1
    "verification-chaine-v2-fidelite-P4-instrument-v1.md": "4e92c3deed0df22b76ebffd16997c8b9e0e471783b54567313385457c4392da4",  # traitement dde35f6f
    "traitement-verification-fidelite-chaine-v2-P4-v1.md": "dde35f6f8def8a43c0def9ca98c432b34bb472893bc0c8a2602327ebc4c6c898",  # consigne
    "traitement-verifications-chaine-v2-P4-v1.md": "10664a97505a49aa2b404e7500b6800466a222ed942815bc370cef79a7c90c6e",          # traitement dde35f6f
    "tokenizer.json": "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4",                                    # contrôles, consigne
    "tokenizer_config.json": "177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424",                             # contrôles, consigne
}
CITEES_PREFIXE = {  # empreintes citées en abrégé
    "verification-chaine-v2-depense-P4-instrument-v1.md": "488a7e71",   # traitement 10664a97
    "verification-chaine-v2-donnees-P4-instrument-v1.md": "16298dd2",   # traitement 10664a97
}

# (chemin dans le dépôt, source dans le bloc-notes ou None, statut)
PIECES: list[tuple[str, str | None, str]] = []
RAPPORTS = [  # liste de 27 noms, ordre du traitement dde35f6f
    ("contre-lecture-R2-P4-instrument-brouillon1-v1.md", "contre-lecture-R2-P4-instrument-brouillon1-v1.md"),
    ("traitement-R2-P4-instrument-brouillon1-v1.md", "traitement-R2-P4-instrument-brouillon1-v1.md"),
    ("traitement-gemini-014-P4-instrument-v1.md", "traitement-gemini-014-P4-instrument-v1.md"),
    ("verification-corrections-brouillons2-3-P4-v1.md", "verification/verification-corrections-brouillons2-3-P4-v1.md"),
    ("traitement-verification-P4-instrument-v1.md", "traitement-verification-P4-instrument-v1.md"),
    ("contre-lecture-3-P4-instrument-candidat1-v1.md", "contre-lecture-3/contre-lecture-3-P4-instrument-candidat1-v1.md"),
    ("relecture-chaine-depense-P4-instrument-v1.md", "relecture-chaine-depense/relecture-chaine-depense-v1.md"),
    ("relecture-chaine-donnees-P4-instrument-v1.md", "relecture-chaine-donnees/relecture-chaine-donnees-v1.md"),
    ("relecture-chaine-fidelite-P4-instrument-v1.md", "relecture-chaine-fidelite/relecture-chaine-fidelite-v1.md"),
    ("traitement-CL3-et-relectures-chaine-P4-v1.md", "traitement-CL3-et-relectures-chaine-P4-v1.md"),
    ("verification-module-v2-contournement-P4-instrument-v1.md",
     "verification-module-v2-contournement/verification-module-v2-contournement-v1.md"),
    ("verification-module-v2-fidelite-P4-instrument-v1.md", "verification-module-v2-fidelite/verification-module-v2-fidelite-v1.md"),
    ("traitement-verifications-module-v2-P4-v1.md", "traitement-verifications-module-v2-P4-v1.md"),
    ("verification-module-v3-P4-instrument-v1.md", "verification-module-v3/verification-module-v3-v1.md"),
    ("verification-chaine-v2-depense-P4-instrument-v1.md", "verification-chaine-v2-depense/verification-chaine-v2-depense-v1.md"),
    ("verification-chaine-v2-donnees-P4-instrument-v1.md", "verification-chaine-v2-donnees/verification-chaine-v2-donnees-v1.md"),
    ("verification-chaine-v2-fidelite-P4-instrument-v1.md", "verification-chaine-v2-fidelite/verification-chaine-v2-fidelite-v1.md"),
    ("traitement-verifications-chaine-v2-P4-v1.md", "traitement-verifications-chaine-v2-P4-v1.md"),
    ("traitement-verification-fidelite-chaine-v2-P4-v1.md", "traitement-verification-fidelite-chaine-v2-P4-v1.md"),
    ("verification-chaine-v4-P4-instrument-v1.md", "attend : vérification de la chaîne v4"),
    ("verification-candidat2-P4-instrument-v1.md", "attend : vérification du candidat 2"),
    ("P4-instrument-v1-brouillon1.md", "P4-instrument-v1-brouillon1.md"),
    ("P4-instrument-v1-brouillon2.md", "P4-instrument-v1-brouillon2.md"),
    ("P4-instrument-v1-brouillon3.md", "P4-instrument-v1-brouillon3.md"),
    ("P4-instrument-v1-brouillon4.md", "P4-instrument-v1-brouillon4.md"),
    ("P4-instrument-v1-candidat1.md", "P4-instrument-v1-candidat1.md"),
    ("P4-instrument-v1-candidat2.md", "attend : candidat 2 relu"),
]
assert len(RAPPORTS) == 27 and len({n for n, _ in RAPPORTS}) == 27
for nom, src in RAPPORTS:
    if src.startswith("attend : "):
        PIECES.append((f"{CL}/{nom}", None, src))
    else:
        PIECES.append((f"{CL}/{nom}", src, "prêt"))
MODULE_P4 = ["mesures_conception_p4_v1.py", "instrument_p4_v1.py", "lecture_p4_v1.py", "test_instrument_p4_v1.py",
             "test_lecture_p4_v1.py", "test_gardes_p4_v1.py"]
for s in MODULE_P4:
    PIECES.append((f"{VERSEES}/{s}", f"module-v3/{s}", "prêt"))
CHAINE = """verifications_p4_v1.py controles_avant_depense_p4_v1.sh lancer_p4_v1.sh sceller_p4_v1.sh surveiller_p4_v1.sh
        controle_cinq_minutes_p4_v1.sh arreter_p4_v1.sh recuperation_p4_v1.sh controler_traces_p4_v1.sh
        repetition_jouet_p4_v1.sh repetition_finale_p4_v1.sh essais_lanceur_p4_v1.sh essais_controles_p4_v1.sh
        essais_scellement_p4_v1.sh essais_surveillance_p4_v1.sh essais_arret_p4_v1.sh essais_traces_p4_v1.sh
        essais_verifications_p4_v1.sh outils_essais_p4_v1.py amorce_instance_p4_v1.sh p4_instance_v1.sh""".split()
assert len(CHAINE) == 21
for s in CHAINE:
    PIECES.append((f"{VERSEES}/{s}", None, "attend : chaîne v4"))
for s in ("tokenizer.json", "tokenizer_config.json"):
    PIECES.append((f"{TOK}/{s}", f"tokeniseur/{s}", "prêt"))
PIECES.append(("brouillons/P4-instrument-v1-candidat<k>.md", None,
               "attend : vérification du candidat 2 (texte final, postérieur au rapport ; nom k à fixer)"))
PIECES.append(("brouillons/P4-instrument-config-v1-candidat<k>.json", "P4-instrument-config-v1.json",
               "prêt (contenu) ; nom k à fixer avec le texte final"))


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main() -> int:
    if ARBRE.exists() or A_NOMMER.exists():
        print("arbre ou pièces à nommer déjà présents : rien n'est écrasé (R12)")
        return 2
    etat, fautes = [], []
    for depot, src, statut in PIECES:
        e = {"depot": depot, "source": None, "statut": statut, "sha256": None, "compagnon_source": None,
             "citee": None, "taille": None}
        if src is not None:
            ps = H / src
            if not ps.is_file() or ps.is_symlink():
                fautes.append(f"source absente ou non ordinaire : {ps}")
                e["statut"] = "manquante"
                etat.append(e)
                continue
            h = sha(ps)
            e.update(source=f"…/{src}", sha256=h, taille=ps.stat().st_size)
            cs = Path(str(ps) + ".sha256")
            if cs.is_file():
                ligne = cs.read_text(encoding="utf-8").strip()
                ok = ligne == f"{h}  {ps.name}"
                e["compagnon_source"] = "conforme" if ok else f"DIFFÉRENT : {ligne[:90]}"
                if not ok:
                    fautes.append(f"compagnon de la source non conforme : {cs}")
            else:
                e["compagnon_source"] = "absent"
            nom = depot.rsplit("/", 1)[1]
            if nom in CITEES:
                e["citee"] = "égale" if CITEES[nom] == h else f"DIFFÉRENTE ({CITEES[nom][:12]}…)"
                if CITEES[nom] != h:
                    fautes.append(f"empreinte citée différente : {nom}")
            elif nom in CITEES_PREFIXE:
                e["citee"] = "égale (préfixe)" if h.startswith(CITEES_PREFIXE[nom]) else "DIFFÉRENTE (préfixe)"
                if not h.startswith(CITEES_PREFIXE[nom]):
                    fautes.append(f"empreinte citée (préfixe) différente : {nom}")
            if "<k>" in depot:
                dest = A_NOMMER / ps.name           # nom final inconnu : copie sous le nom de la source
            else:
                dest = ARBRE / depot
            if dest.exists():
                fautes.append(f"destination existe déjà : {dest}")
                etat.append(e)
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ps, dest)
            if sha(dest) != h:
                fautes.append(f"copie d'une autre empreinte : {dest}")
            Path(str(dest) + ".sha256").write_text(f"{h}  {dest.name}\n", encoding="utf-8")
            e["copie"] = str(dest.relative_to(PREP))
        etat.append(e)
    (PREP / "etat-pieces-v1.json").write_text(json.dumps(etat, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    prets = [e["depot"] for e in etat if e["statut"] == "prêt"]
    lignes = []
    for d in prets:
        lignes += [d, d + ".sha256"]
    (PREP / "liste-chemins-C-prets-v1.txt").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"pièces : {len(etat)} ; prêtes dans l'arbre : {len(prets)} ; "
          f"en attente : {sum(1 for e in etat if e['statut'].startswith('attend'))} ; "
          f"à nommer : {sum(1 for e in etat if e['statut'].startswith('prêt (contenu)'))}")
    for f in fautes:
        print("FAUTE :", f)
    return 1 if fautes else 0


if __name__ == "__main__":
    sys.exit(main())
