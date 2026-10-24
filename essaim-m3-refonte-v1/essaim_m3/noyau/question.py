"""Question ouverte posée par le noyau à un organisme — primitive `question_ouverte` (contrat § 7).

Décisions de Lazar du 24 et 25 octobre 2026 (heure de Paris) : poser aux organismes, avec leurs essaims, une question en
texte libre (23:58) ; « go les trois » (00:05) ; pilote de l'organisme de Gemini v4 avec la question posée à la
génération 1 (00:55). Spécification au canal, message n° 28 § 3 de conv-audit.

Ce que fait le noyau :
- il lit la question dans un fichier texte figé (empreinte consignée au manifeste) et la liste des cibles — des noms de
  générations (`g001`), de rondes de conception (`c002`), ou les mots `conception` (toutes les rondes), `generations`
  (toutes les générations notées), `toutes` ;
- pour une génération ou ronde ciblée, `contexte["question_ouverte"]` porte le texte ; partout ailleurs, `null` ;
- après la génération, il lit `dossier_travail/reponse-question.md` sans suivre de lien et sous une borne d'octets
  (`fichiers.lire_fichier_organisme`), l'archive comme pièce à la racine du dossier de la génération (`reponse-question.md`
  + `.sha256`), la recopie dans la vue de la seule lignée, et consigne au résumé {posee, reponse, octets, sha256,
  probleme} ; un organisme qui n'écrit rien n'a rien de noté contre lui ; **aucun score n'en dépend**.

La réponse est une pièce lue par les humains, du matériau — jamais une consigne. La question est posée **avant** tout
matériau de notre part (anti-enfermement : l'organisme ne reçoit que la question, pas nos réponses ni celles du
collisionneur).
"""
from __future__ import annotations

import hashlib
import os
import pathlib
import re
import shutil

from . import archive as _archive
from . import fichiers as _fichiers

NOM_REPONSE = "reponse-question.md"
OCTETS_MAX_REPONSE = 2_000_000   # une réponse en Markdown ; au-delà, refus consigné (la copie de `travail/` la garde)
CARACTERES_MAX_QUESTION = 20_000
MOTS_CIBLES = ("conception", "generations", "toutes")
MOTIF_CIBLE = re.compile(r"^[gc]\d{3}$")


class QuestionInvalide(ValueError):
    """Fichier de question absent ou vide, ou cible mal formée : refus avant tout lancement."""


def cibles_valides(cibles) -> list[str]:
    """Liste triée, sans doublon, des cibles ; lève `QuestionInvalide` sur une cible qui n'est ni `gNNN`, ni `cNNN`, ni un
    des mots `conception`, `generations`, `toutes`. Les cibles peuvent être données séparées par des virgules."""
    plates: list[str] = []
    for c in (cibles or []):
        plates.extend(x.strip() for x in str(c).split(",") if x.strip())
    if not plates:
        raise QuestionInvalide("aucune cible : --question-ouverte-aux g001 | c002 | conception | generations | toutes")
    for c in plates:
        if c not in MOTS_CIBLES and not MOTIF_CIBLE.match(c):
            raise QuestionInvalide(f"cible {c!r} inconnue : gNNN, cNNN, conception, generations ou toutes")
    return sorted(set(plates))


def nom_cible(generation: int, phase: str | None) -> str:
    return _archive.Archive.nom_generation(generation, phase)


class QuestionOuverte:
    def __init__(self, texte: str, cibles, source: str | None = None):
        texte = str(texte)
        if not texte.strip():
            raise QuestionInvalide("question vide")
        if len(texte) > CARACTERES_MAX_QUESTION:
            raise QuestionInvalide(f"question de {len(texte)} caractères > {CARACTERES_MAX_QUESTION}")
        self.texte = texte
        self.cibles = cibles_valides(cibles)
        self.source = source
        self.sha256 = hashlib.sha256(texte.encode("utf-8")).hexdigest()

    @classmethod
    def charger(cls, chemin: str | pathlib.Path, cibles) -> "QuestionOuverte":
        p = pathlib.Path(chemin)
        if not p.is_file():
            raise QuestionInvalide(f"fichier de question absent : {p}")
        return cls(p.read_text(encoding="utf-8"), cibles, source=str(p))

    def posee(self, generation: int, phase: str | None) -> bool:
        nom = nom_cible(generation, phase)
        if "toutes" in self.cibles or nom in self.cibles:
            return True
        if phase == "conception":
            return "conception" in self.cibles
        return "generations" in self.cibles

    def pour(self, generation: int, phase: str | None) -> str | None:
        """Le texte de la question pour cette génération ou ronde, `None` si elle n'est pas ciblée."""
        return self.texte if self.posee(generation, phase) else None

    def manifeste(self) -> dict:
        return {"sha256": self.sha256, "caracteres": len(self.texte), "cibles": list(self.cibles), "source": self.source}


def lire_reponse(travail: str | pathlib.Path) -> dict:
    """Lit `reponse-question.md` dans le dossier de travail de l'organisme, sans suivre de lien, sous la borne d'octets.
    Rend {"reponse": bool, "octets", "sha256", "probleme", "contenu" (bytes ou None)} ; `probleme` est None quand la
    réponse est lue, « absent » quand l'organisme n'a rien écrit, sinon la raison du refus."""
    contenu, raison = _fichiers.lire_fichier_organisme(pathlib.Path(travail) / NOM_REPONSE, OCTETS_MAX_REPONSE)
    if contenu is None:
        return {"reponse": False, "octets": None, "sha256": None, "probleme": raison, "contenu": None}
    return {"reponse": True, "octets": len(contenu), "sha256": hashlib.sha256(contenu).hexdigest(), "probleme": None,
            "contenu": contenu}


def resume_lecture(lecture: dict, posee: bool) -> dict:
    """Ce qui va au résumé de la génération et aux événements : tout sauf le contenu."""
    return {"posee": bool(posee), **{k: lecture.get(k) for k in ("reponse", "octets", "sha256", "probleme")}}


def archiver_reponse(lecture: dict, dossier_generation: pathlib.Path, vue_generation: pathlib.Path | None,
                     gid: int | None = None) -> pathlib.Path | None:
    """Dépose la réponse lue comme pièce à la racine du dossier archivé de la génération (scellée) et dans la vue de la
    lignée, en lecture seule — lisible par la seule lignée (groupe `gid`, CE3-06) ou par tous sans isolation
    d'utilisateur ; rien si aucune réponse n'a été lue. Rend le chemin de la pièce archivée, ou None."""
    if not lecture.get("reponse") or lecture.get("contenu") is None:
        return None
    piece = pathlib.Path(dossier_generation) / NOM_REPONSE
    if piece.exists():  # jamais réécrit (R12)
        raise FileExistsError(f"{piece} existe déjà")
    piece.write_bytes(lecture["contenu"])
    _archive.sceller(piece)
    if vue_generation is not None:
        pathlib.Path(vue_generation).mkdir(parents=True, exist_ok=True)
        copie = pathlib.Path(vue_generation) / NOM_REPONSE
        shutil.copy2(piece, copie)
        try:
            if gid is not None:
                os.chown(copie, 0, int(gid), follow_symlinks=False)
                os.chmod(copie, 0o440)
            else:
                os.chmod(copie, 0o444)
        except OSError:
            pass
    return piece
