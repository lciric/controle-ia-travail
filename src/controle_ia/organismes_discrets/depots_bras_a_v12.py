"""Écriture scellée d'une pièce, sans état intermédiaire illisible — bras A des organismes discrets, version 12 du code
(vérification du code de la version 7, C-2 ; `docs/notes/relance-organismes-discrets-v1/verification-corrections-code-v7-bras-a-v1.md`).

Le défaut : la version 7 écrivait un fichier sous son nom, puis le scellait. Une panne entre les deux laissait, sous
le nom attendu, un fichier sans compagnon : toute lecture du dossier s'arrêtait dessus, et l'on n'en sortait que par
une retouche à la main.

Ici, **aucun fichier ne porte le nom attendu sans son compagnon**. `ecrire_et_sceller` procède en trois temps :
1. le contenu est écrit sous un **nom provisoire** (`<nom>.provisoire`), et forcé sur le disque ;
2. il est **scellé** : son empreinte, relue du fichier provisoire, est posée dans le compagnon du nom attendu
   (`<nom>.sha256`, au format de `controle_ia.scellement`), lui-même écrit sous un nom provisoire puis renommé ;
3. le fichier provisoire est **renommé** au nom attendu (`os.replace`, d'un seul geste).

Quel que soit le moment d'une panne, il reste au plus : un fichier provisoire, que personne ne lit par son nom ; ou
un compagnon sans son fichier, que les lecteurs du dossier ne prennent pas pour une pièce. Jamais la pièce sans son
sceau.

**Rejouable à l'identique.** Rappelée avec le même contenu, `ecrire_et_sceller` finit ce qu'une panne a laissé en
plan, ou ne fait rien si la pièce est déjà là, scellée et identique. Rappelée avec un autre contenu alors que la pièce
existe, elle refuse : une pièce scellée ne s'écrase pas (R12). Un fichier provisoire ou un compagnon resté seul d'une
écriture interrompue n'est pas une pièce : il est remplacé.

Ce module n'écrit que là où on le lui dit ; il ne lit que ce qu'il écrit.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path

from ..gardes import GardeArret
from ..scellement import compagnon, verifier

SUFFIXE_PROVISOIRE = ".provisoire"


def _ecrire_sur_le_disque(chemin: Path, octets: bytes) -> None:
    with open(chemin, "wb") as f:
        f.write(octets)
        f.flush()
        os.fsync(f.fileno())


def _ecrire_le_provisoire(provisoire: Path, octets: bytes) -> None:
    """Temps 1 : le contenu, sous son nom provisoire."""
    _ecrire_sur_le_disque(provisoire, octets)


def _poser_le_compagnon(final: Path, empreinte: str) -> None:
    """Temps 2 : le sceau du nom attendu, écrit sous un nom provisoire puis renommé."""
    sceau = compagnon(final)
    provisoire = sceau.with_name(sceau.name + SUFFIXE_PROVISOIRE)
    _ecrire_sur_le_disque(provisoire, f"{empreinte}  {final.name}\n".encode("utf-8"))
    os.replace(provisoire, sceau)


def _renommer(provisoire: Path, final: Path) -> None:
    """Temps 3 : la pièce prend son nom, d'un seul geste."""
    os.replace(provisoire, final)


def ecrire_et_sceller(chemin, texte: str) -> str:
    """Écrit une pièce et son compagnon, de sorte qu'elle ne porte jamais son nom sans son sceau ; rend son empreinte.
    - la pièce existe déjà, scellée, du même contenu : rien n'est fait (rejeu à l'identique) ;
    - elle existe avec un autre contenu, ou sans compagnon valable : refus — une pièce ne s'écrase pas (R12) ;
    - sinon : écriture provisoire, scellement, renommage. Les restes d'une écriture interrompue sont remplacés."""
    final = Path(chemin)
    if not isinstance(texte, str):
        raise GardeArret(f"{final.name} : texte exigé")
    if final.name.endswith((".sha256", SUFFIXE_PROVISOIRE)):
        raise GardeArret(f"{final.name} : ni un compagnon ni un fichier provisoire ne s'écrit comme une pièce")
    if not final.parent.is_dir():
        raise GardeArret(f"{final.parent} : dossier absent — la pièce {final.name} n'a pas où s'écrire")
    octets = texte.encode("utf-8")
    attendue = hashlib.sha256(octets).hexdigest()
    if final.exists():
        if verifier(final) != attendue:
            raise GardeArret(f"{final.name} est déjà écrit et scellé avec un autre contenu : jamais écrasé (R12)")
        return attendue
    provisoire = final.with_name(final.name + SUFFIXE_PROVISOIRE)
    _ecrire_le_provisoire(provisoire, octets)
    relue = hashlib.sha256(provisoire.read_bytes()).hexdigest()
    if relue != attendue:
        raise GardeArret(f"{final.name} : le fichier provisoire relu n'a pas l'empreinte de ce qui devait s'écrire")
    _poser_le_compagnon(final, relue)
    _renommer(provisoire, final)
    return verifier(final)


def restes_d_une_ecriture_interrompue(dossier) -> list[str]:
    """Noms des restes qu'une écriture interrompue a laissés dans un dossier : fichiers provisoires, et compagnons
    sans leur fichier. Ce ne sont pas des pièces ; ils sont rapportés, pour que rien ne soit tu."""
    restes = []
    for f in sorted(Path(dossier).iterdir()):
        if f.name.endswith(SUFFIXE_PROVISOIRE):
            restes.append(f.name)
        elif f.name.endswith(".sha256") and not f.with_name(f.name[:-len(".sha256")]).exists():
            restes.append(f.name)
    return restes
