"""Deux listes de lecture de l'organe « mémoire du dépôt » (fusion de la veille de cap et de la bibliothécaire), version 1.

Pièce d'instrument (classe B), session bibliothécaire (Claude Opus 5.5), 22 novembre 2026. Applique l'étape 2 acceptée par la
mère (docs/notes/memoire-conception-v1/fusion-etape-2-deux-listes-deux-partitions-v1.md, f859d691…) et ses décisions D-1 à D-4.

  autorise_stricte(c) -> (bool, motif)   liste d'autorisation v4 (réponses de la bibliothécaire) :
      v3 (règles de verifier_citations_v6.chemin_autorise) + (i) `registres/veille-de-cap/` exclu, sauf `commune/` ;
      (ii) D-1 (a) : mes dérivés de sources ouvertes sur droit exprès, ou écrits par un agent à lecture large, sont exclus.
  niveau_boucle(c) -> ("plein" | "noms" | "refus", motif)   liste de la boucle (cycles à contexte neuf), trois niveaux :
      refus : exclusions du mandat v2 § 11 et de la v3 § 2 (sauf diag/, runs/, prereg/, rangés en « noms ») ;
      noms  : prereg/, runs/, diag/ (lister seulement ; manifestes lus par programme, D-2) ;
      plein : tout ce que permet la v4, docs/notes/, docs/decisions/, docs/sources/, documents qui font foi, et la liste
              blanche de registres/ (D-3).
Les exclusions priment toujours. Accents retirés et casse ignorée pour les règles de nom (comme la v6).
"""
import fnmatch
import importlib.util
import os

ICI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "vc6", os.path.join(ICI, "..", "epreuve-outils-v1", "verifier_citations_v6.py"))
vc6 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vc6)

normaliser_chemin = vc6.normaliser_chemin
sans_accents = vc6.sans_accents

VEILLE = "registres/veille-de-cap/"
VEILLE_COMMUNE = "registres/veille-de-cap/commune/"
MEMO = "docs/notes/memoire-conception-v1/"
# D-1 (a) : dérivés à lecture large ou de sources ouvertes sur droit exprès ; ils suivent leur source (hors liste stricte).
EXCLUS_DERIVES_D1 = (
    MEMO + "liste-exhaustive-hypotheses-exploration-allumage-v*",
    MEMO + "exploration-idees-seances-anterieures-v*",
    MEMO + "recolte-session-bibliothecaire-*",
    MEMO + "versement-journal-22-novembre-v1/*",
)

# Liste blanche de registres/ pour la boucle (D-3), à étendre fichier par fichier sur mot de la mère.
REGISTRES_BOUCLE_EXACTS = (
    "registres/decisions.md", "registres/go.md", "registres/etat.md", "registres/rappels.md", "registres/depenses.md",
    "registres/arrets.md", "registres/veille.md", "registres/essaim/regle-du-canal-essaim-v1.md",
    "registres/memoire-problemes-v3-commune-diffusable.md", "registres/inventaire-decisions-ouvertes-2026-11-21-v1.md",
    "registres/noeuds-ouverts-2026-11-18-v1.md", "registres/canaux-sessions-v5.md",
)
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


def autorise_stricte(c):
    c = normaliser_chemin(c)
    if _commence(c, VEILLE) and not _commence(c, VEILLE_COMMUNE):
        return False, "partition de la boucle : seul registres/veille-de-cap/commune/ est lisible par la bibliothécaire"
    if c + "/" == VEILLE_COMMUNE:
        return False, "hors de la liste d'autorisation"   # le dossier lui-même
    base = _sans_compagnon(c)
    for m in EXCLUS_DERIVES_D1:
        if fnmatch.fnmatch(base, m) or fnmatch.fnmatch(base + "/_", m):
            return False, "dérivé à lecture large (D-1) : suit sa source"
    if _commence(c, VEILLE_COMMUNE):
        ok, motif = _exclusions_communes(c)
        return (True, "") if ok else (False, motif)
    return vc6.chemin_autorise(c)


def _exclusions_communes(c):
    """Exclusions qui valent pour tout lecteur (noms, segments, dossiers, motifs de résultats). Rend (True, '') si aucune."""
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
    for p in EXCLUS_BOUCLE_PREFIXES:
        if _commence(c, p):
            return False, f"dossier exclu {p}"
    for m in vc6.EXCLUS_MOTIFS:
        if fnmatch.fnmatch(c, m) or fnmatch.fnmatch(c + "/_", m) or fnmatch.fnmatch(c, m.rstrip("*").rstrip("/") + "/*"):
            return False, f"motif exclu {m}"
    return True, ""


def niveau_boucle(c):
    c = normaliser_chemin(c)
    if not c or c.startswith("/") or c.startswith("..") or "/../" in c:
        return "refus", "chemin absolu, vide ou sortant du dépôt"
    ok, motif = _exclusions_communes(c)
    if not ok:
        return "refus", motif
    if any(_commence(c, p) for p in NOMS_SEULS):
        return "noms", "noms seuls (lister, ne pas ouvrir)"
    base = _sans_compagnon(c)
    if base in DOCS_BOUCLE_EXACTS or base in REGISTRES_BOUCLE_EXACTS:
        return "plein", ""
    if any(_commence(c, p) for p in DOCS_BOUCLE_PREFIXES + REGISTRES_BOUCLE_PREFIXES):
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
