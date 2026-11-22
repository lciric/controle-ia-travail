"""Deux listes de lecture de l'organe « mémoire du dépôt », version 2 (22 novembre 2026).

Pièce d'instrument (classe B), session bibliothécaire (Claude Opus 5.5). Corrige la v1 après sa contre-lecture
(contre-lecture-outils-fusion-v1-v1.md) :
  B1  tout `registres/veille*` est refusé à la liste stricte, sauf `registres/veille.md` (et son compagnon) et les
      extraits communs ; le préfixe hérité de la v3 ne joue plus.
  C8  `commune/` : seuls les noms `journal-commun-AAAA-MM-JJTHHMMZ.jsonl` et leur compagnon, sans sous-dossier.
  C11 D-1 par motifs élargis (toutes versions) ; demande et réponse 24 exclues partout par motif de nom ; toute version
      de `canaux-sessions-v*.md` pour la boucle.
  R8  PDF et autres binaires en « noms seuls » pour la boucle.
Fonctions : autorise_stricte(c) -> (bool, motif) ; niveau_boucle(c) -> ("plein"|"noms"|"refus", motif) ;
autorise_bras(c, bras) -> (ouvrable, listable, motif). Les exclusions priment toujours. Accents retirés, casse ignorée pour
les règles de nom. Limite déclarée : le bras est choisi par l'appelant (remarque 1) ; la porte de périmètre le juge sur
le journal, qui consigne le bras.
"""
import fnmatch
import importlib.util
import os
import re

ICI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "vc6", os.path.join(ICI, "..", "epreuve-outils-v1", "verifier_citations_v6.py"))
vc6 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vc6)

normaliser_chemin = vc6.normaliser_chemin
sans_accents = vc6.sans_accents

VEILLE = "registres/veille-de-cap/"
VEILLE_COMMUNE = "registres/veille-de-cap/commune/"
RX_COMMUNE = re.compile(r"registres/veille-de-cap/commune/journal-commun-\d{4}-\d{2}-\d{2}T\d{4}Z\.jsonl(\.sha256)?")
VEILLE_MD = ("registres/veille.md", "registres/veille.md.sha256")
MEMO = "docs/notes/memoire-conception-v1/"
# D-1 (a) : dérivés à lecture large ou de sources ouvertes sur droit exprès ; toutes versions (C11).
EXCLUS_DERIVES_D1 = (
    MEMO + "liste-exhaustive-*",
    MEMO + "exploration-idees-seances-anterieures-*",
    MEMO + "recolte-session-bibliothecaire-*",
    MEMO + "versement-journal-*",
)
RX_24 = re.compile(r"(demande|reponse)[-_ ]?24(?![0-9])")
BINAIRES = (".pdf", ".png", ".jpg", ".jpeg", ".gif", ".gz", ".zip", ".tar", ".pt", ".safetensors", ".npy", ".npz", ".bin")

REGISTRES_BOUCLE_EXACTS = (
    "registres/decisions.md", "registres/go.md", "registres/etat.md", "registres/rappels.md", "registres/depenses.md",
    "registres/arrets.md", "registres/veille.md", "registres/essaim/regle-du-canal-essaim-v1.md",
    "registres/memoire-problemes-v3-commune-diffusable.md", "registres/inventaire-decisions-ouvertes-2026-11-21-v1.md",
    "registres/noeuds-ouverts-2026-11-18-v1.md",
)
RX_CANAUX = re.compile(r"registres/canaux-sessions-v\d+\.md")
REGISTRES_BOUCLE_PREFIXES = ("registres/go-extraits/", "registres/passations/", VEILLE, "registres/essaim/vers-mere/")
DOCS_BOUCLE_EXACTS = ("CLAUDE.md", "docs/brief-claude-code-programme-complet-v2.md", "docs/programme-controle-ia-v2.md",
                      "docs/etat-de-l-art-controle-ia-v1.md")
DOCS_BOUCLE_PREFIXES = ("docs/notes/", "docs/decisions/", "docs/sources/")
NOMS_SEULS = ("prereg/", "runs/", "diag/")
EXCLUS_BOUCLE_PREFIXES = ("brouillons/ii-b-saboteur-budget-v1/", "donnees/bras-attaque-oracle-")


def _sans_compagnon(c):
    return c[:-len(".sha256")] if c.endswith(".sha256") else c


def _commence(c, p):
    return c.startswith(p) or (c + "/").startswith(p)


def _exclusions_communes(c):
    """Exclusions valables pour tout lecteur. Rend (True, '') si aucune."""
    if not c or c.startswith("/") or c.startswith("..") or "/../" in c or c.endswith("/.."):
        return False, "chemin absolu, vide ou sortant du dépôt"
    bas = sans_accents(c).lower()
    for m in vc6.EXCLUS_MOTS:
        if m in bas:
            return False, f"nom exclu « {m} »"
    segs = bas.split("/")
    if any("ne-pas-lire" in s for s in segs):
        return False, "segment « ne-pas-lire » exclu"
    for s in vc6.EXCLUS_DOSSIERS:
        if s in segs:
            return False, f"dossier exclu « {s} »"
    for s in vc6.EXCLUS_SOUS_CHAINES:
        if any(s in seg for seg in segs):
            return False, f"segment exclu « {s} »"
    if any(RX_24.search(s) for s in segs):
        return False, "demande ou réponse 24 exclue"
    for p in EXCLUS_BOUCLE_PREFIXES:
        if _commence(c, p):
            return False, f"dossier exclu {p}"
    for m in vc6.EXCLUS_MOTIFS:
        if fnmatch.fnmatch(c, m) or fnmatch.fnmatch(c + "/_", m) or fnmatch.fnmatch(c, m.rstrip("*").rstrip("/") + "/*"):
            return False, f"motif exclu {m}"
    return True, ""


def autorise_stricte(c):
    c = normaliser_chemin(c)
    ok, motif = _exclusions_communes(c)
    if not ok:
        return False, motif
    if c.startswith("registres/veille"):            # B1 : aucun préfixe ; deux formes exactes seulement
        if c in VEILLE_MD or RX_COMMUNE.fullmatch(c):
            return True, ""
        return False, "registres/veille* : seuls registres/veille.md et les extraits communs sont lisibles"
    base = _sans_compagnon(c)
    for m in EXCLUS_DERIVES_D1:
        if fnmatch.fnmatch(base, m) or fnmatch.fnmatch(base + "/_", m):
            return False, "dérivé à lecture large (D-1) : suit sa source"
    return vc6.chemin_autorise(c)


def niveau_boucle(c):
    c = normaliser_chemin(c)
    ok, motif = _exclusions_communes(c)
    if not ok:
        return "refus", motif
    if any(_commence(c, p) for p in NOMS_SEULS):
        return "noms", "noms seuls (lister, ne pas ouvrir)"
    base = _sans_compagnon(c)
    dedans = (base in DOCS_BOUCLE_EXACTS or base in REGISTRES_BOUCLE_EXACTS or RX_CANAUX.fullmatch(base)
              or any(_commence(c, p) for p in DOCS_BOUCLE_PREFIXES + REGISTRES_BOUCLE_PREFIXES))
    if dedans:
        if base.lower().endswith(BINAIRES):
            return "noms", "fichier binaire : noms seuls"
        return "plein", ""
    if c.startswith("registres/"):
        return "refus", "registres/ hors de la liste blanche de la boucle (D-3)"
    return "refus", "hors de la liste de la boucle"


def autorise_bras(c, bras):
    """Pour l'outil borné : rend (ouvrable, listable, motif)."""
    if bras == "boucle":
        n, motif = niveau_boucle(c)
        return n == "plein", n in ("plein", "noms"), motif
    if bras in ("memo", "base"):
        ok, motif = autorise_stricte(c)
        if ok and bras == "base" and _commence(normaliser_chemin(c), MEMO):
            return False, False, "bras base : dossier du mémo exclu"
        return ok, ok, motif
    return False, False, f"bras inconnu {bras!r}"
