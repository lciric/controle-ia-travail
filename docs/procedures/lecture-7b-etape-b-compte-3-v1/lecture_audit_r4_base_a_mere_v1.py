"""Lecture, par la session mère, du seul état de l'audit R4 de la base (A) de T0.8 (déclenché ou non), v1.

Écrit le 2026-11-16 (à partir de 17:11:37Z, `date -u`) par un développeur neuf, sous-agent de la session mère (modèle A), sur la
décision de Lazar GO-2026-11-16-07, point 3 (`registres/go.md`) : « la mère lit par programme le seul état de l'audit R4 de la
base (A) (déclenché ou non) ; s'il est déclenché, un lecteur neuf du modèle C relit avant la ligne `ISSUE-MOTS-ET-COUT-T06` ».
Texte scellé : `prereg/T0.8-base-A-mots-et-cout-v1.md`, l. 111 (« Audit R4 […] Action : relecture, avant l'inscription de
`ISSUE-MOTS-ET-COUT-T06`, par un lecteur neuf ») ; réserve R-BA6. Forme du fichier : la pièce « mots et coût »
(`scripts/mots_et_cout_t06_v3.py` au commit que cite la ligne `CODE-MOTS-ET-COUT-T06`) écrit `diag/<run de la pièce>/base-a-t08.json`,
objet JSON à la racine (clés triées), dont la clé `audit_r4` est un objet portant le booléen `declenche`, scellé par
`controle_ia.scellement.sceller` (compagnon d'une ligne « <sha256>  base-a-t08.json »). Modèle suivi : `lecture_etat_ba_l2_mere_v1.py`
(bloc M de la mère), même dossier.

Bibliothèque standard seule. N'écrit rien. Ne lit du fichier que `audit_r4.declenche` : aucune autre clé n'est imprimée ni conservée
(l'objet décodé est jeté dès le booléen extrait). N'imprime qu'**une** ligne, sur la sortie standard, et rien sur l'erreur :
  « audit R4 de la base (A) : déclenché »      (code 0) : un lecteur neuf du modèle C relit avant la ligne `ISSUE-MOTS-ET-COUT-T06` ;
  « audit R4 de la base (A) : non déclenché »  (code 0) ;
  « audit R4 de la base (A) : refus — <motif> » (code 1) : motif sans aucune valeur lue du fichier (ni nombre, ni phrase, ni clé
  autre que celles du chemin `audit_r4.declenche`) ; la mère lève la cause, rien n'est inscrit.

Contrôles, dans l'ordre :
  1. appel : `--fichier` nommé `base-a-t08.json`, fichier ordinaire (pas un lien) ; `--empreinte` de 64 chiffres hexadécimaux
     minuscules (l'empreinte rendue par l'hôte au bloc B5b, celle que redonne le bloc V) ;
  2. compagnon `base-a-t08.json.sha256` présent, d'une seule ligne « <sha256>  base-a-t08.json » ;
  3. empreinte du fichier égale au compagnon **et** à l'empreinte rendue par l'hôte ;
  4. texte UTF-8, JSON strict (aucune clé en double dans aucun objet, aucun NaN ni infini), racine objet, `audit_r4` présent et objet,
     `declenche` présent et booléen (`true`/`false` ; ni chaîne, ni nombre, ni `null`).

    python3 -I -B lecture_audit_r4_base_a_mere_v1.py --fichier CHEMIN/base-a-t08.json --empreinte SHA256
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

NOM = "base-a-t08.json"
TETE = "audit R4 de la base (A) : "
SHA = re.compile(r"[0-9a-f]{64}")
COMPAGNON = re.compile(r"([0-9a-f]{64})  (\S.*)")


class Refus(Exception):
    pass


class _Appel(argparse.ArgumentParser):
    def error(self, message: str) -> None:  # une ligne, code 1 (jamais l'usage d'argparse sur l'erreur)
        raise Refus("appel invalide (attendu : --fichier CHEMIN/base-a-t08.json --empreinte SHA256)")


def _sans_doublon(paires: list) -> dict:
    cles = [k for k, _ in paires]
    if len(set(cles)) != len(cles):
        raise Refus(f"{NOM} : clé en double dans un objet JSON (nom non affiché)")
    return dict(paires)


def _constante(_nom: str):
    raise Refus(f"{NOM} : constante non standard (NaN ou infini) dans le JSON")


def etat_audit_r4(fichier: Path, empreinte_hote: str) -> bool:
    if fichier.name != NOM:
        raise Refus(f"fichier nommé autrement que {NOM}")
    if not SHA.fullmatch(empreinte_hote):
        raise Refus("empreinte rendue par l'hôte hors du format (64 chiffres hexadécimaux minuscules)")
    if fichier.is_symlink() or not fichier.is_file():
        raise Refus(f"{NOM} absent, ou pas un fichier ordinaire")
    comp = Path(str(fichier) + ".sha256")
    if comp.is_symlink() or not comp.is_file():
        raise Refus(f"compagnon {NOM}.sha256 absent")
    try:
        lignes = [l for l in comp.read_text(encoding="utf-8").splitlines() if l.strip()]
    except (OSError, UnicodeDecodeError) as e:
        raise Refus(f"compagnon {NOM}.sha256 illisible ({type(e).__name__})") from None
    m = COMPAGNON.fullmatch(lignes[0]) if len(lignes) == 1 else None
    if m is None or m.group(2) != NOM:
        raise Refus(f"compagnon {NOM}.sha256 hors du format « <sha256>  {NOM} » (une ligne)")
    try:
        octets = fichier.read_bytes()
    except OSError as e:
        raise Refus(f"{NOM} illisible ({type(e).__name__})") from None
    h = hashlib.sha256(octets).hexdigest()
    if h != m.group(1):
        raise Refus(f"{NOM} : empreinte {h[:12]}… ≠ compagnon ({m.group(1)[:12]}…)")
    if h != empreinte_hote:
        raise Refus(f"{NOM} : empreinte {h[:12]}… ≠ empreinte rendue par l'hôte ({empreinte_hote[:12]}…)")
    try:
        texte = octets.decode("utf-8")
        del octets
        doc = json.loads(texte, object_pairs_hook=_sans_doublon, parse_constant=_constante)
    except Refus:
        raise
    except (ValueError, RecursionError) as e:
        raise Refus(f"{NOM} illisible : texte UTF-8 ou JSON invalide ({type(e).__name__})") from None
    del texte
    if not isinstance(doc, dict):
        raise Refus(f"{NOM} : racine de type {type(doc).__name__}, objet attendu")
    audit = doc.get("audit_r4", _ABSENT)
    del doc
    if audit is _ABSENT:
        raise Refus(f"{NOM} : champ « audit_r4 » absent")
    if not isinstance(audit, dict):
        raise Refus(f"{NOM} : champ « audit_r4 » de type {type(audit).__name__}, objet attendu (valeur non affichée)")
    x = audit.get("declenche", _ABSENT)
    del audit
    if x is _ABSENT:
        raise Refus(f"{NOM} : champ « audit_r4.declenche » absent")
    if not isinstance(x, bool):
        raise Refus(f"{NOM} : champ « audit_r4.declenche » de type {type(x).__name__}, booléen attendu (valeur non affichée)")
    return x


_ABSENT = object()


def main(argv: list[str]) -> int:
    p = _Appel(description=__doc__.splitlines()[0], add_help=False)
    p.add_argument("--fichier", required=True)
    p.add_argument("--empreinte", required=True)
    try:
        a = p.parse_args(argv)
        d = etat_audit_r4(Path(a.fichier), a.empreinte)
    except Refus as e:
        print(f"{TETE}refus — {e}")
        return 1
    except Exception as e:  # aucun repli silencieux (R5), aucune valeur affichée
        print(f"{TETE}refus — erreur inattendue ({type(e).__name__})")
        return 1
    print(f"{TETE}déclenché" if d else f"{TETE}non déclenché")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
