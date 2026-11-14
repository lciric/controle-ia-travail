"""Contrôle à blanc du compte 2 avant l'ouverture pleine de P3-bis (voie normale), v1.

Écrit le 2026-11-14 par un rédacteur neuf de la session mère, qui ne sera ni lecteur ni auteur du verdict de P3-bis et n'a
ouvert aucun paquet. Appelé par `commande-ouverture-verdict-p3bis-compte-2-v1.md` (même dossier), avant que le contenu des
paquets soit récupéré. Il n'écrit rien, nulle part ; il ne lit aucun paquet ; il n'ouvre aucun fichier de T0.7 (le texte
scellé de T0.7 n'est que haché, par la garde du module de S, exactement comme le fera l'ouverture) ; il n'affiche aucune
ligne de registre hors l'appui (clé=empreinte) que la garde écrira au journal.

Ce qu'il contrôle, dans l'ordre (arrêt au premier défaut, motif imprimé) :
  1. le module importé est celui de S (`ouverture_p3bis_v3.py`, 4a54a437…) ;
  2. attestation par programme : ni la session ni le compte ne figurent dans la liste « qui a lu quoi » (fichier scellé
     par son compagnon, d'empreinte donnée, tableau dont l'en-tête porte les colonnes « session » et « compte ») ;
  3. journal des ouvertures absent (« aucune tentative ») ; aucune ligne VERDICT-P3BIS au registre des scellements ;
  4. compagnons des fichiers cités par SCORES-T07 et SONDES-T07 présents dans la racine, d'empreinte attendue, premier mot
     égal à l'empreinte de la ligne (le fichier de T0.7 lui-même n'est ni exigé ni lu : D8 du texte de P3-bis) ;
  5. garde du module de S (`garde_ouverture`, lecture seule) rejouée en mode `pleine` sur la racine, à l'instant donné ou
     une minute après l'horloge : autorisée par le chemin normal, appui égal à celui des lignes du 2026-11-14.

    PYTHONPATH=<module de S> python -B controle_a_blanc_compte_2_v1.py --racine DEPOT --liste CHEMIN \
        --empreinte-liste SHA256 --session session_… [--compte "compte 2"] [--instant AAAA-MM-JJTHH:MM:SSZ]

Codes : 0 tout conforme ; 2 arrêt ou refus (motif imprimé) ; 1 erreur d'appel.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
import time
from pathlib import Path

from controle_ia.gardes import GardeArret
from controle_ia.premier_test_ia import ouverture_p3bis_v3 as o
from controle_ia.scellement import verifier

MODULE_S = "4a54a437e4a6031b1890f0f5f0261cf1141e72aee82d456d9fcd5483946693e9"
APPUI_ATTENDU = ("SCORES-T07=13ac4480035f1ef6d4ea8ac81ffa962c1324e4e9e90a78c1d4f569f2abd0509d "
                 "SONDES-T07=aa6892320f130e96af45e4e70b542b7ccfcea3ccd23d2fdc3e722b5637affa95")
# compagnon → empreinte du fichier compagnon (branche donnees/t07-etape-a-v1, tête 0c176db5, blobs 34181fd1 et 60d8dfb0)
COMPAGNONS_T07 = {
    "donnees/20261114-001352-t07-lecture-reel/scores-actions-t07.npz.sha256":
        "5f5672fca88231d25bfff139a0c5e490f5338dba64c10254ce95e673a38fd22f",
    "diag/20261114-001352-t07-lecture-reel/sondes-t07.json.sha256":
        "77af718b91e5d05479a283cf47db4ed04d178604e2ff9218d7badf14f2bd60bf",
}
CHEMINS_ADMIS = ("chemin normal", "chemin normal (rendez-vous sans objet)")
SESSION = re.compile(r"session_[0-9A-Za-z]{10,}")
SHA = re.compile(r"[0-9a-f]{64}")
SEPARATEUR = re.compile(r":?-{3,}:?")
COMPTE_2 = re.compile(r"compte[\s  _-]*2(?![0-9])", re.IGNORECASE)


def _sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _norme(cellule: str) -> str:
    return cellule.strip().strip("`*_ ").strip().lower()


def _designe_le_compte(cellule: str, compte: str) -> bool:
    """La cellule « compte » désigne-t-elle le compte attesté (« compte 2 », « Compte-2 », « 2 », « c2 »…) ?"""
    compacte = re.sub(r"[\s  _`*.-]", "", cellule).lower()
    voulu = re.sub(r"[\s  _`*.-]", "", compte).lower()
    return bool(COMPTE_2.search(cellule)) or compacte in {"2", "c2", voulu}


def attester(liste: Path, empreinte: str, session: str, compte: str) -> tuple[bool, str]:
    """Ni la session ni le compte ne figurent dans la liste « qui a lu quoi » ; (conforme, texte)."""
    if not liste.is_file():
        return False, f"liste {liste} absente"
    try:
        sha = verifier(liste)                   # compagnon présent, nom et empreinte égaux (R6)
    except GardeArret as e:
        return False, f"liste non scellée ou altérée : {e}"
    if sha != empreinte:
        return False, f"liste d'empreinte {sha[:12]}…, {empreinte[:12]}… attendue"
    entete, n = None, 0
    for i, brute in enumerate(liste.read_text(encoding="utf-8").splitlines(), start=1):
        s = brute.strip()
        if not s.startswith("|"):
            if session in s:
                return False, f"la session {session} est citée hors du tableau (ligne {i})"
            continue
        cellules = [c.strip() for c in s.strip("|").split("|")]
        if all(SEPARATEUR.fullmatch(c) for c in cellules):
            continue
        normees = [_norme(c) for c in cellules]
        if "session" in normees and "compte" in normees:
            entete = (normees.index("session"), normees.index("compte"), len(cellules))
            continue
        if entete is None:
            return False, f"ligne {i} : ligne de tableau avant tout en-tête à colonnes « session » et « compte »"
        if len(cellules) != entete[2]:
            return False, f"ligne {i} : {len(cellules)} cellules, {entete[2]} attendues"
        if any(session in c for c in cellules):
            return False, f"la session {session} figure à la ligne {i}"
        if _designe_le_compte(cellules[entete[1]], compte):
            return False, f"le {compte} figure à la ligne {i} (colonne « compte »)"
        n += 1
    if entete is None:
        return False, "format non reconnu : aucun en-tête de tableau à colonnes « session » et « compte »"
    return True, f"{n} ligne(s) de lecture lues"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="controle_a_blanc_compte_2_v1.py")
    ap.add_argument("--racine", required=True)
    ap.add_argument("--liste", required=True)
    ap.add_argument("--empreinte-liste", required=True)
    ap.add_argument("--session", required=True)
    ap.add_argument("--compte", default="compte 2")
    ap.add_argument("--instant", default=None)
    a = ap.parse_args(argv)
    if not SESSION.fullmatch(a.session):
        print("ERREUR : --session : identifiant « session_… » attendu", file=sys.stderr)
        return 1
    if not SHA.fullmatch(a.empreinte_liste):
        print("ERREUR : --empreinte-liste : 64 caractères hexadécimaux minuscules attendus", file=sys.stderr)
        return 1
    racine = Path(a.racine).resolve()
    if not (racine / "registres").is_dir():
        print(f"ERREUR : {racine}/registres absent", file=sys.stderr)
        return 1
    try:
        instant = o.instant_utc(a.instant) if a.instant is not None else int(time.time()) + 60
    except GardeArret as e:
        print(f"ERREUR : --instant : {e}", file=sys.stderr)
        return 1
    liste = Path(a.liste) if Path(a.liste).is_absolute() else racine / a.liste

    sha_module = _sha(Path(o.__file__))                                                       # 1
    if sha_module != MODULE_S:
        print(f"ARRÊT : module importé {o.__file__} d'empreinte {sha_module[:12]}…, {MODULE_S[:12]}… (S) attendue")
        return 2
    print(f"module de S : {MODULE_S[:12]}… conforme")

    ok, texte = attester(liste, a.empreinte_liste, a.session, a.compte)                       # 2
    if not ok:
        print(f"ARRÊT : attestation « qui a lu quoi » : {texte}")
        return 2
    print(f"ATTESTATION : CONFORME — session {a.session} et {a.compte} absents de la liste {liste} "
          f"({a.empreinte_liste[:12]}… ; {texte})")

    if (racine / o.JOURNAL_OUVERTURES).exists():                                              # 3
        print(f"ARRÊT : {o.JOURNAL_OUVERTURES} présent : une tentative a déjà été journalisée ; cette commande ne vaut "
              f"que pour « aucune tentative »")
        return 2
    scellements = racine / o.REGISTRE_SCELLEMENTS
    if not scellements.is_file():
        print(f"ARRÊT : {o.REGISTRE_SCELLEMENTS} absent")
        return 2
    for brute in scellements.read_text(encoding="utf-8").splitlines():
        if brute.strip().startswith("|") and o._cellules(brute)[0] == "VERDICT-P3BIS":
            print("ARRÊT : une ligne VERDICT-P3BIS est déjà inscrite")
            return 2
    print("journal des ouvertures absent (aucune tentative) ; aucune ligne VERDICT-P3BIS")

    try:                                                                                      # 4
        t07 = o.lire_scellements_t07(scellements)
    except o.RefusOuverture as e:
        print(f"ARRÊT : registre des scellements : {e.code} : {e.texte}")
        return 2
    for k in (o.SCORES_T07, o.SONDES_T07):
        if k not in t07:
            print(f"ARRÊT : ligne {k} absente du registre des scellements")
            return 2
        comp = t07[k]["chemin"] + ".sha256"
        attendu = COMPAGNONS_T07.get(comp)
        if attendu is None:
            print(f"ARRÊT : la ligne {k} cite {t07[k]['chemin']}, hors des deux fichiers attendus")
            return 2
        p = racine / comp
        if not p.is_file():
            print(f"ARRÊT : compagnon {comp} absent de la racine (la garde refuserait : compagnon-absent)")
            return 2
        if _sha(p) != attendu:
            print(f"ARRÊT : compagnon {comp} d'empreinte {_sha(p)[:12]}…, {attendu[:12]}… attendue")
            return 2
        if o._premier_mot(p) != t07[k]["sha256"]:
            print(f"ARRÊT : premier mot du compagnon {comp} autre que l'empreinte de la ligne {k}")
            return 2
        present = "présent (il sera haché par la garde)" if (racine / t07[k]["chemin"]).is_file() else \
            "absent (non exigé, D8)"
        print(f"{k} : compagnon présent, empreinte {attendu[:12]}…, premier mot égal à la ligne ; fichier de T0.7 "
              f"{present}")

    try:                                                                                      # 5
        g = o.garde_ouverture(racine, o.PLEINE, instant)
    except o.RefusOuverture as e:
        print(f"CONTRÔLE À BLANC : REFUS {e.code} : {e.texte}")
        return 2
    except GardeArret as e:
        print(f"CONTRÔLE À BLANC : ARRÊT : {e}")
        return 2
    print(f"CONTRÔLE À BLANC : AUTORISÉ {g['mode']} ({g['chemin']}) à {o.date_utc(instant)} ; appui {g['appui']}")
    if g["chemin"] not in CHEMINS_ADMIS:
        print(f"ARRÊT : chemin « {g['chemin']} », « chemin normal » attendu")
        return 2
    if g["appui"] != APPUI_ATTENDU:
        print("ARRÊT : appui autre que celui des lignes SCORES-T07 et SONDES-T07 du 2026-11-14")
        return 2
    print("CONTRÔLE À BLANC DU COMPTE 2 : TOUT CONFORME")
    return 0


if __name__ == "__main__":
    sys.exit(main())
