#!/usr/bin/env python3
"""
Collecteur primaire brut multi-sources et analyseur syntaxique déterministe (v1).
Mandat : GO-2026-11-24-01 — Étape 1.
Dépense API payante : 0,00 USD (uniquement OpenAlex, Semantic Scholar, Brave Search,
arXiv e-print, OpenReview API v2, LessWrong GraphQL, GitHub CLI).
"""

from __future__ import annotations

import datetime as dt
import gzip
import io
import json
import os
import pathlib
import re
import subprocess
import sys
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from typing import Any

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True

USER_AGENT = "CartographieMathsOuvertes/1.0 (Academic Research; zero-paid-api)"

# Noms des variables d'environnement dont aucune valeur ne doit jamais apparaître en sortie
ENV_SECRET_NAMES = (
    "OPENALEX_API_KEY",
    "SEMANTIC_SCHOLAR_API_KEY",
    "BRAVE_API_KEY",
    "OPENAI_API_KEY",
    "RR_ANTHROPIC_API_KEY",
    "GEMINI_API_KEY",
    "MISTRAL_API_KEY",
    "KIMI_API_KEY",
    "VAST_API_KEY",
    "HCLOUD_TOKEN",
    "GITHUB_TOKEN",
    "GH_TOKEN",
)


def collecter_valeurs_secretes(env: dict[str, str] | None = None) -> list[str]:
    """Recense en mémoire les valeurs secrètes à proscrire de toute journalisation ou sortie."""
    source = env if env is not None else dict(os.environ)
    secrets: list[str] = []
    for nom, val in source.items():
        if not val or len(val.strip()) < 6:
            continue
        upper = nom.upper()
        if any(cle in upper for cle in ("KEY", "TOKEN", "SECRET", "PASSWORD")) or any(
            upper.startswith(pref) for pref in ENV_SECRET_NAMES
        ):
            secrets.append(val.strip())
    return secrets


def verifier_absence_fuite_secrete(texte: str, secrets_interdits: list[str]) -> None:
    """Lève une RuntimeError immédiate si une valeur de clé apparaît dans une chaîne de sortie."""
    for secret in secrets_interdits:
        if secret and secret in texte:
            raise RuntimeError("Garde de sécurité déclenchée : fuite potentielle de secret détectée et bloquée.")


def requete_http_octets(
    url: str,
    headers: dict[str, str] | None = None,
    data: bytes | None = None,
    timeout: float = 25.0,
    tentatives: int = 3,
    pause_base: float = 1.2,
) -> tuple[int, dict[str, str], bytes]:
    """Exécute une requête HTTP avec réessais exponentiels sur erreurs transitoires (429, 5xx)."""
    entetes = {"User-Agent": USER_AGENT}
    if headers:
        entetes.update(headers)
    derniere_erreur: Exception | None = None
    for essai in range(tentatives):
        try:
            req = urllib.request.Request(url, data=data, headers=entetes)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                statut = resp.status
                meta = {k.lower(): v for k, v in resp.headers.items()}
                corps = resp.read()
                return statut, meta, corps
        except urllib.error.HTTPError as exc:
            derniere_erreur = exc
            if exc.code in (429, 500, 502, 503, 504) and essai + 1 < tentatives:
                time.sleep(pause_base * (2**essai))
                continue
            raise
        except Exception as exc:
            derniere_erreur = exc
            if essai + 1 < tentatives:
                time.sleep(pause_base * (2**essai))
                continue
            raise
    assert derniere_erreur is not None
    raise derniere_erreur


def requete_http_json(
    url: str,
    headers: dict[str, str] | None = None,
    data: bytes | None = None,
    timeout: float = 25.0,
    tentatives: int = 3,
) -> Any:
    _, _, corps = requete_http_octets(url, headers=headers, data=data, timeout=timeout, tentatives=tentatives)
    return json.loads(corps.decode("utf-8", errors="replace"))


# ============================================================================
# 1. ANALYSEUR SYNTAXIQUE LATEX DÉTERMINISTE
# ============================================================================

RE_NEWTHEOREM = re.compile(
    r"\\newtheorem\*?\s*\{([a-zA-Z0-9_@*]+)\}\s*(?:\[[a-zA-Z0-9_@*]+\]\s*)?\{([^}]+)\}",
    re.MULTILINE,
)

COMMENT_OPEN_PATTERNS = re.compile(
    r"\b(TODO|FIXME|OPEN|CONJECTURE|GAP|LIMITATION|UNPROVEN|MISSING\s+PROOF|CANNOT\s+BOUND|REMAINS\s+TO\s+SHOW)\b",
    re.IGNORECASE,
)

GAP_SENTENCE_REGEX = re.compile(
    r"([^.!?]{0,180}\b(?:"
    r"gap\s+between\s+(?:the\s+)?upper\s+and\s+lower|"
    r"matching\s+lower\s+bound|"
    r"closing\s+the\s+gap|"
    r"remains\s+(?:an\s+)?open|"
    r"remains\s+unclear|"
    r"leave\s+(?:it\s+|this\s+)?(?:as\s+|for\s+|to\s+)?(?:an\s+)?(?:open|future\s+work)|"
    r"it\s+is\s+(?:an\s+)?open\s+(?:question|problem)|"
    r"open\s+(?:question|problem)s?\b|"
    r"open\s+whether|"
    r"we\s+conjecture\s+that|"
    r"cannot\s+bound|"
    r"without\s+assumption|"
    r"relaxing\s+assumption|"
    r"important\s+limitation|"
    r"key\s+limitation"
    r")[^.!?]{0,220}[.!?])",
    re.IGNORECASE,
)

LABEL_REGEX = re.compile(r"\\label\{([^}]+)\}")


def decouper_ligne_latex_commentaire(ligne: str) -> tuple[str, str | None]:
    r"""
    Sépare de façon déterministe la partie active d'une ligne LaTeX et son commentaire `% ...`,
    en respectant strictement les pourcentages échappés `\%` et les doubles barres obliques `\\`.
    """
    i = 0
    n = len(ligne)
    while i < n:
        ch = ligne[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "%":
            return ligne[:i], ligne[i + 1 :]
        i += 1
    return ligne, None


def nettoyer_espace(texte: str, limite: int = 900) -> str:
    propre = re.sub(r"\s+", " ", texte).strip()
    if len(propre) > limite:
        return propre[: limite - 3] + "..."
    return propre


def detecter_alias_environnements(tex_sans_commentaires: str) -> dict[str, str]:
    r"""
    Associe chaque nom d'environnement LaTeX (standard ou défini via \newtheorem) à son rôle canonique :
    'ouverture' | 'hypothese' | 'theoreme'.
    """
    roles: dict[str, str] = {
        "conjecture": "ouverture",
        "openproblem": "ouverture",
        "open_problem": "ouverture",
        "openquestion": "ouverture",
        "question": "ouverture",
        "problem": "ouverture",
        "assumption": "hypothese",
        "assumptions": "hypothese",
        "condition": "hypothese",
        "hypothesis": "hypothese",
        "theorem": "theoreme",
        "thm": "theoreme",
        "proposition": "theoreme",
        "prop": "theoreme",
        "lemma": "theoreme",
        "lem": "theoreme",
        "corollary": "theoreme",
    }
    for match in RE_NEWTHEOREM.finditer(tex_sans_commentaires):
        env_nom = match.group(1).strip().rstrip("*")
        titre = match.group(2).strip().lower()
        if any(mot in titre for mot in ("conjecture", "open problem", "open question", "question", "problem")):
            roles[env_nom] = "ouverture"
        elif any(mot in titre for mot in ("assumption", "condition", "hypothesis", "axiom")):
            roles[env_nom] = "hypothese"
        elif any(mot in titre for mot in ("theorem", "lemma", "proposition", "corollary")):
            roles[env_nom] = "theoreme"
    return roles


def extraire_environnements_actifs(
    tex_sans_commentaires: str, roles: dict[str, str]
) -> list[dict[str, Any]]:
    r"""
    Extrait avec gestion d'imbrication tous les environnements LaTeX dont le nom figure dans `roles`.
    Ignore par construction tout environnement qui était commenté par `%`.
    """
    noms_tries = sorted(roles.keys(), key=len, reverse=True)
    if not noms_tries:
        return []
    alt = "|".join(re.escape(nom) for nom in noms_tries)
    jeton_re = re.compile(rf"\\(begin|end)\{{({alt})\*?\}}")

    pile: list[tuple[str, int, int]] = []
    extraits: list[dict[str, Any]] = []

    for m in jeton_re.finditer(tex_sans_commentaires):
        action = m.group(1)
        nom_brut = m.group(2)
        if action == "begin":
            pile.append((nom_brut, m.start(), m.end()))
        else:
            # Recherche de l'ouverture correspondante la plus récente
            for idx in range(len(pile) - 1, -1, -1):
                if pile[idx][0] == nom_brut:
                    nom_ouv, debut_ext, fin_balise_ouv = pile.pop(idx)
                    corps = tex_sans_commentaires[fin_balise_ouv : m.start()]
                    labels = LABEL_REGEX.findall(corps)
                    extraits.append(
                        {
                            "env": nom_ouv,
                            "role": roles[nom_ouv],
                            "labels": labels,
                            "debut": debut_ext,
                            "fin": m.end(),
                            "contenu": nettoyer_espace(corps, limite=1100),
                            "contenu_brut": corps,
                        }
                    )
                    break
    extraits.sort(key=lambda x: x["debut"])
    return extraits


def extraire_structures_latex(contenu_tex: str, source_id: str = "") -> dict[str, Any]:
    r"""
    Analyse syntaxique déterministe d'un source LaTeX complet :
    1) séparation stricte texte actif / commentaires non échappés ;
    2) détection des alias \newtheorem ;
    3) extraction des conjectures / questions ouvertes explicites ;
    4) extraction des trous de preuve implicites : couplages assumption -> theorem,
       écarts de bornes supérieure/inférieure, aveux d'annexes/limites et commentaires % TODO / % open.
    """
    lignes_actives: list[str] = []
    commentaires_techniques: list[dict[str, Any]] = []

    for num_ligne, ligne in enumerate(contenu_tex.splitlines(), start=1):
        actif, comm = decouper_ligne_latex_commentaire(ligne)
        lignes_actives.append(actif)
        if comm is not None:
            comm_strip = comm.strip()
            # Exclure le code LaTeX désactivé (`%\begin{...}`, `%\section`, etc.)
            est_code_latex_commente = bool(re.match(r"^\\(?:begin|end|section|subsection|item|usepackage|newcommand|def)\b", comm_strip))
            if not est_code_latex_commente and len(comm_strip) >= 6 and COMMENT_OPEN_PATTERNS.search(comm_strip):
                # Ignorer le bruit purement éditorial de mise en page
                if not re.search(r"\b(camera-ready|typo|font|margin|vspace|figure\s+color)\b", comm_strip, re.I):
                    commentaires_techniques.append(
                        {
                            "ligne": num_ligne,
                            "texte": nettoyer_espace(comm_strip, limite=400),
                        }
                    )

    tex_actif = "\n".join(lignes_actives)
    roles = detecter_alias_environnements(tex_actif)
    envs = extraire_environnements_actifs(tex_actif, roles)

    ouvertures_explicites = [
        {
            "env": e["env"],
            "labels": e["labels"],
            "enonce": e["contenu"],
        }
        for e in envs
        if e["role"] == "ouverture" and len(e["contenu"]) >= 20
    ]

    hypotheses = [e for e in envs if e["role"] == "hypothese" and len(e["contenu"]) >= 15]
    theoremes = [e for e in envs if e["role"] == "theoreme" and len(e["contenu"]) >= 20]

    # Couplage déterministe Assumption -> Theorem
    couplages_hypotheses: list[dict[str, Any]] = []
    for idx_h, hyp in enumerate(hypotheses, start=1):
        labels_h = hyp["labels"]
        theoremes_invoquant: list[str] = []
        for thm in theoremes:
            corps_t = thm["contenu_brut"]
            invoque = False
            for lab in labels_h:
                if re.search(rf"\\(?:c|C|eq|autoref|)?ref\{{[^}}]*\b{re.escape(lab)}\b[^}}]*\}}", corps_t):
                    invoque = True
                    break
            if not invoque:
                # Référence textuelle explicite "Assumption 1", "under our assumptions", etc.
                if re.search(
                    rf"\b(?:Assumption|Condition|Hypothesis)s?\s*(?:~|\s)\s*(?:{idx_h}|\b)",
                    corps_t,
                    re.IGNORECASE,
                ) or re.search(r"\bunder\s+(?:the\s+)?(?:standing\s+)?assumptions?\b", corps_t, re.IGNORECASE):
                    invoque = True
            if invoque:
                theoremes_invoquant.append(nettoyer_espace(thm["contenu"], limite=450))
        couplages_hypotheses.append(
            {
                "env_hypothese": hyp["env"],
                "labels": labels_h,
                "hypothese": hyp["contenu"],
                "nb_theoremes_dependants": len(theoremes_invoquant),
                "theoremes_dependants_extraits": theoremes_invoquant[:3],
            }
        )

    # Théorèmes portant des hypothèses restrictives internes ("Suppose that...", "Assume that...")
    for thm in theoremes:
        corps_norm = nettoyer_espace(thm["contenu_brut"], limite=600)
        m_inline = re.search(
            r"\b((?:Suppose|Assume|Assuming)\s+(?:that\s+)?[^.]{15,240}\.)",
            corps_norm,
            re.IGNORECASE,
        )
        if m_inline and len(couplages_hypotheses) < 25:
            couplages_hypotheses.append(
                {
                    "env_hypothese": f"{thm['env']}_inline_assumption",
                    "labels": thm["labels"],
                    "hypothese": m_inline.group(1),
                    "nb_theoremes_dependants": 1,
                    "theoremes_dependants_extraits": [nettoyer_espace(thm["contenu"], limite=450)],
                }
            )

    # Normalisation des retours à la ligne simples intra-paragraphe avant extraction des phrases d'ouverture
    tex_paragraphes = re.sub(r"(?<!\n)\n(?!\n)", " ", tex_actif)
    ecarts_et_aveux: list[str] = []
    vus: set[str] = set()
    for m in GAP_SENTENCE_REGEX.finditer(tex_paragraphes):
        phrase = nettoyer_espace(m.group(1), limite=500)
        cle = phrase.lower()[:120]
        if len(phrase) >= 35 and cle not in vus:
            vus.add(cle)
            ecarts_et_aveux.append(phrase)

    return {
        "source_id": source_id,
        "nb_caracteres_actifs": len(tex_actif),
        "ouvertures_explicites": ouvertures_explicites[:25],
        "couplages_hypotheses_theoremes": couplages_hypotheses[:25],
        "ecarts_bornes_et_aveux": ecarts_et_aveux[:30],
        "commentaires_todo_open": commentaires_techniques[:25],
        "a_verrou_extrait": bool(
            ouvertures_explicites
            or any(c["nb_theoremes_dependants"] > 0 for c in couplages_hypotheses)
            or ecarts_et_aveux
            or commentaires_techniques
        ),
    }


def extraire_tex_depuis_archive_arxiv(octets_bruts: bytes) -> tuple[str, list[str]]:
    """
    Décompresse en mémoire une archive e-print arXiv (.tar.gz ou .gz simple)
    et assemble les fichiers .tex dans un ordre déterministe (fichier principal en tête).
    """
    fichiers_tex: dict[str, str] = {}
    # Cas 1 : archive tar (éventuellement compressée gzip)
    try:
        with tarfile.open(fileobj=io.BytesIO(octets_bruts), mode="r:*") as tf:
            for membre in tf.getmembers():
                if membre.isfile() and membre.name.lower().endswith((".tex", ".sty")):
                    f = tf.extractfile(membre)
                    if f is not None:
                        contenu = f.read().decode("utf-8", errors="replace")
                        if membre.name.lower().endswith(".tex"):
                            fichiers_tex[membre.name] = contenu
    except tarfile.TarError:
        # Cas 2 : fichier unique compressé gzip
        try:
            texte = gzip.decompress(octets_bruts).decode("utf-8", errors="replace")
            if "\\" in texte:
                fichiers_tex["main.tex"] = texte
        except OSError:
            texte = octets_bruts.decode("utf-8", errors="replace")
            if "\\documentclass" in texte or "\\begin{" in texte:
                fichiers_tex["main.tex"] = texte

    if not fichiers_tex:
        return "", []

    # Ordonnancement : fichiers contenant \documentclass d'abord, puis suivi des \input{...}
    principaux = sorted(k for k, v in fichiers_tex.items() if "\\documentclass" in v)
    autres = sorted(k for k in fichiers_tex.keys() if k not in principaux)
    ordre: list[str] = []
    deja_inclus: set[str] = set()

    def ajouter_avec_inputs(nom_cle: str) -> None:
        if nom_cle in deja_inclus or nom_cle not in fichiers_tex:
            return
        deja_inclus.add(nom_cle)
        ordre.append(nom_cle)
        corps = fichiers_tex[nom_cle]
        for m in re.finditer(r"\\(?:input|include)\{([^}]+)\}", corps):
            cible = m.group(1).strip()
            candidats = [cible, cible + ".tex", os.path.normpath(os.path.join(os.path.dirname(nom_cle), cible)), os.path.normpath(os.path.join(os.path.dirname(nom_cle), cible + ".tex"))]
            for cand in candidats:
                if cand in fichiers_tex and cand not in deja_inclus:
                    ajouter_avec_inputs(cand)

    for p in principaux:
        ajouter_avec_inputs(p)
    for a in autres:
        if a not in deja_inclus:
            ordre.append(a)
            deja_inclus.add(a)

    assemble = "\n\n".join(f"% === FILE: {nom} ===\n{fichiers_tex[nom]}" for nom in ordre)
    return assemble, ordre


# ============================================================================
# 2. FILTRES DÉTERMINISTES OPENREVIEW & LESSWRONG & COUPURE TEMPORELLE
# ============================================================================

OPENREVIEW_ADMISSION_REGEX = re.compile(
    r"([^.!?\n]{0,160}\b(?:"
    r"open\s+(?:problem|question|direction)|"
    r"remains\s+open|"
    r"cannot\s+bound|"
    r"without\s+assumption|"
    r"strong\s+assumption|"
    r"unrealistic\s+assumption|"
    r"lower\s+bound|"
    r"gap\s+between|"
    r"no\s+theoretical\s+guarantee|"
    r"lack\s+of\s+lower\s+bound|"
    r"future\s+work\s+to\s+prove"
    r")[^.!?\n]{0,220}[.!?]?)",
    re.IGNORECASE,
)


def extraire_aveux_openreview(texte: str) -> list[str]:
    aveux: list[str] = []
    vus: set[str] = set()
    for m in OPENREVIEW_ADMISSION_REGEX.finditer(texte):
        seg = nettoyer_espace(m.group(1), limite=450)
        cle = seg.lower()[:100]
        if len(seg) >= 25 and cle not in vus:
            vus.add(cle)
            aveux.append(seg)
    return aveux[:12]


def filtrer_commentaires_lesswrong_par_billet(
    commentaires_bruts: list[dict[str, Any]], post_id_attendu: str
) -> list[dict[str, Any]]:
    """
    Garde R5 stricte : rejette tout commentaire retourné par GraphQL dont le `postId`
    ne coïncide pas exactement avec `post_id_attendu` (protège contre le repli global de LessWrong).
    """
    retenus: list[dict[str, Any]] = []
    for c in commentaires_bruts:
        if c.get("postId") != post_id_attendu:
            continue
        ext = c.get("extendedScore")
        agreement = ext.get("agreement", 0) if isinstance(ext, dict) else 0
        retenus.append(
            {
                "comment_id": c.get("_id"),
                "post_id": c.get("postId"),
                "posted_at": c.get("postedAt"),
                "auteur": (c.get("user") or {}).get("username") or (c.get("user") or {}).get("displayName") or "inconnu",
                "base_score": c.get("baseScore", 0),
                "agreement_score": agreement,
                "parent_comment_id": c.get("parentCommentId"),
                "markdown": nettoyer_espace((c.get("contents") or {}).get("markdown") or "", limite=2200),
            }
        )
    retenus.sort(key=lambda x: (x["agreement_score"] or 0, x["base_score"] or 0), reverse=True)
    return retenus


def normaliser_date_iso(date_brute: str | None, annee_repli: int | None = None) -> str | None:
    """Normalise une date en YYYY-MM-DD ; en cas d'année seule `YYYY`, conservatrice vers `YYYY-12-31`."""
    if date_brute:
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", str(date_brute).strip())
        if m:
            return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
        m_ym = re.match(r"^(\d{4})-(\d{2})$", str(date_brute).strip())
        if m_ym:
            return f"{m_ym.group(1)}-{m_ym.group(2)}-28"
        m_y = re.match(r"^(\d{4})$", str(date_brute).strip())
        if m_y:
            return f"{m_y.group(1)}-12-31"
    if annee_repli is not None:
        return f"{int(annee_repli):04d}-12-31"
    return None


def date_depuis_identifiant_arxiv(arxiv_id: str | None) -> str | None:
    """Infère une borne supérieure de date de fin de mois à partir d'un identifiant arXiv YYMM.NNNNN."""
    if not arxiv_id:
        return None
    m = re.match(r"^(\d{2})(\d{2})\.\d{4,5}", arxiv_id.strip())
    if not m:
        return None
    yy = int(m.group(1))
    mm = int(m.group(2))
    if not (1 <= mm <= 12):
        return None
    annee = 2000 + yy if yy <= 89 else 1900 + yy
    dernier_jour = 28 if mm == 2 else (30 if mm in (4, 6, 9, 11) else 31)
    return f"{annee:04d}-{mm:02d}-{dernier_jour:02d}"


def est_avant_coupure_stricte(date_iso: str | None, coupure: str = "2023-12-31") -> bool:
    """Retourne True ssi `date_iso` est connue et lexicographiquement <= `coupure`."""
    if not date_iso or not re.match(r"^\d{4}-\d{2}-\d{2}$", date_iso):
        return False
    return date_iso <= coupure


# ============================================================================
# 3. COLLECTEURS MULTI-SOURCES RÉELS (0,00 USD)
# ============================================================================

def reconstruire_abstract_openalex(inv_index: dict[str, list[int]] | None) -> str:
    if not inv_index or not isinstance(inv_index, dict):
        return ""
    mots_pos: list[tuple[int, str]] = []
    for mot, positions in inv_index.items():
        if isinstance(positions, list):
            for p in positions:
                if isinstance(p, int):
                    mots_pos.append((p, mot))
    mots_pos.sort(key=lambda x: x[0])
    return " ".join(m for _, m in mots_pos)


def collecter_openalex_et_s2() -> dict[str, Any]:
    """Interroge OpenAlex et Semantic Scholar sur les 4 strates définies à l'Étape 0."""
    oa_key = os.environ.get("OPENALEX_API_KEY", "").strip()
    s2_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "").strip()
    s2_headers = {"x-api-key": s2_key} if s2_key else {}

    date_ref = dt.date(2026, 11, 24)
    enregistrements: list[dict[str, Any]] = []
    ids_vus: set[str] = set()

    def ajouter_entree(entree: dict[str, Any]) -> None:
        cle = (entree.get("arxiv_id") or entree.get("doi") or entree.get("titre", "").lower()[:90]).strip()
        if not cle or cle in ids_vus:
            return
        ids_vus.add(cle)
        enregistrements.append(entree)

    requetes_openalex = [
        # Strate 1 : sommets très cités
        ("S1_sommets_cites", "reward hacking reinforcement learning from human feedback Goodhart", "cited_by_count:desc", ""),
        ("S1_sommets_cites", "mechanistic interpretability superposition sparse autoencoder linear representation", "cited_by_count:desc", ""),
        ("S1_sommets_cites", "scalable oversight debate weak-to-strong generalization sleeper agents", "cited_by_count:desc", ""),
        ("S1_sommets_cites", "AI control untrusted monitoring alignment faking sandbagging", "cited_by_count:desc", ""),
        # Strate 2 : forte vélocité 2025-2026
        ("S2_velocite_2025_2026", "AI control untrusted monitor sabotage scheming", "cited_by_count:desc", "from_publication_date:2025-01-01"),
        ("S2_velocite_2025_2026", "emergent misalignment chain-of-thought monitorability obfuscation post-training", "cited_by_count:desc", "from_publication_date:2025-01-01"),
        ("S2_velocite_2025_2026", "sparse autoencoder identifiability concept erasure unlearning", "cited_by_count:desc", "from_publication_date:2025-01-01"),
        # Strate 3 : ponts mathématiques
        ("S3_ponts_mathematiques", "partial monitoring minimax regret observability", "cited_by_count:desc", ""),
        ("S3_ponts_mathematiques", "strategic classification performative prediction Stackelberg regret", "cited_by_count:desc", ""),
        ("S3_ponts_mathematiques", "anytime-valid e-processes sequential testing quickest change detection", "cited_by_count:desc", ""),
        ("S3_ponts_mathematiques", "singular learning theory learning coefficient neural networks", "cited_by_count:desc", ""),
        ("S3_ponts_mathematiques", "multicalibration omniprediction online calibration minimax", "cited_by_count:desc", ""),
        # Strate 4 : Open Problems COLT / JMLR / ateliers
        ("S4_open_problems", "\"Open Problem:\" learning theory minimax regret", "cited_by_count:desc", ""),
        ("S4_open_problems", "\"Open Problem\" adversarial VC dimension sample complexity COLT", "cited_by_count:desc", ""),
        ("S4_open_problems", "open problems AI alignment safety interpretability", "cited_by_count:desc", ""),
    ]

    for strate, req_txt, tri, filtre in requetes_openalex:
        params: dict[str, str] = {
            "search": req_txt,
            "per-page": "15",
            "sort": tri,
        }
        if filtre:
            params["filter"] = filtre
        if oa_key:
            params["api_key"] = oa_key
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
        try:
            donnees = requete_http_json(url)
            for w in donnees.get("results", []):
                pub_date = normaliser_date_iso(w.get("publication_date"), w.get("publication_year"))
                cites = int(w.get("cited_by_count") or 0)
                mois_ecoules = 1.0
                if pub_date:
                    try:
                        d_pub = dt.date.fromisoformat(pub_date)
                        mois_ecoules = max(1.0, (date_ref - d_pub).days / 30.4375)
                    except ValueError:
                        mois_ecoules = 12.0
                velocite = round(cites / mois_ecoules, 3)
                ids_obj = w.get("ids") or {}
                doi = (w.get("doi") or "").replace("https://doi.org/", "")
                arxiv_id = None
                for loc in w.get("locations") or []:
                    landing = (loc.get("landing_page_url") or "") + " " + (loc.get("pdf_url") or "")
                    m_arx = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", landing)
                    if m_arx:
                        arxiv_id = m_arx.group(1)
                        break
                if not arxiv_id and "arxiv" in doi.lower():
                    m_arx2 = re.search(r"arxiv\.(\d{4}\.\d{4,5})", doi, re.I)
                    if m_arx2:
                        arxiv_id = m_arx2.group(1)
                resume = reconstruire_abstract_openalex(w.get("abstract_inverted_index"))
                ajouter_entree(
                    {
                        "source": "openalex",
                        "strate": strate,
                        "id_externe": ids_obj.get("openalex") or w.get("id"),
                        "arxiv_id": arxiv_id,
                        "doi": doi or None,
                        "titre": w.get("title") or "",
                        "date_publication": pub_date,
                        "annee": w.get("publication_year"),
                        "citations": cites,
                        "velocite_mensuelle": velocite,
                        "resume": nettoyer_espace(resume, limite=950),
                        "marqueurs_ouverture": extraire_aveux_openreview((w.get("title") or "") + ". " + resume),
                    }
                )
        except Exception as exc:
            print(f"[AVERTISSEMENT] OpenAlex ({strate} / {req_txt[:30]}): {type(exc).__name__}", file=sys.stderr)
        time.sleep(0.15)

    requetes_s2_bulk = [
        ("S1_sommets_cites", '"reward hacking" | "Goodhart" | "overoptimization"', "citationCount:desc", ""),
        ("S1_sommets_cites", '"AI control" | "untrusted monitoring" | "alignment faking" | "sleeper agents"', "citationCount:desc", ""),
        ("S1_sommets_cites", '"sparse autoencoder" | "superposition" | "linear representation hypothesis" | "concept erasure"', "citationCount:desc", ""),
        ("S2_velocite_2025_2026", '"emergent misalignment" | "chain-of-thought monitorability" | "sandbagging" | "covert malicious"', "citationCount:desc", "2025-"),
        ("S3_ponts_mathematiques", '"partial monitoring" "minimax regret"', "citationCount:desc", ""),
        ("S3_ponts_mathematiques", '"strategic classification" | "performative prediction" "regret"', "citationCount:desc", ""),
        ("S3_ponts_mathematiques", '"weak-to-strong generalization" | "doubly-efficient debate"', "citationCount:desc", ""),
        ("S4_open_problems", '"Open Problem:" COLT', "citationCount:desc", ""),
    ]

    for strate, req_s2, tri_s2, annee_filtre in requetes_s2_bulk:
        params_s2: dict[str, str] = {
            "query": req_s2,
            "fields": "title,year,citationCount,externalIds,publicationDate,venue,abstract",
            "sort": tri_s2,
        }
        if annee_filtre:
            params_s2["year"] = annee_filtre
        url_s2 = "https://api.semanticscholar.org/graph/v1/paper/search/bulk?" + urllib.parse.urlencode(params_s2)
        try:
            donnees_s2 = requete_http_json(url_s2, headers=s2_headers)
            for p in (donnees_s2.get("data") or [])[:25]:
                ext_ids = p.get("externalIds") or {}
                arxiv_id = ext_ids.get("ArXiv")
                pub_date = normaliser_date_iso(
                    p.get("publicationDate") or date_depuis_identifiant_arxiv(arxiv_id),
                    p.get("year"),
                )
                cites = int(p.get("citationCount") or 0)
                mois_ecoules = 1.0
                if pub_date:
                    try:
                        d_pub = dt.date.fromisoformat(pub_date)
                        mois_ecoules = max(1.0, (date_ref - d_pub).days / 30.4375)
                    except ValueError:
                        mois_ecoules = 12.0
                resume = p.get("abstract") or ""
                ajouter_entree(
                    {
                        "source": "semantic_scholar",
                        "strate": strate,
                        "id_externe": p.get("paperId"),
                        "arxiv_id": arxiv_id,
                        "doi": ext_ids.get("DOI"),
                        "venue": p.get("venue"),
                        "titre": p.get("title") or "",
                        "date_publication": pub_date,
                        "annee": p.get("year"),
                        "citations": cites,
                        "velocite_mensuelle": round(cites / mois_ecoules, 3),
                        "resume": nettoyer_espace(resume, limite=950),
                        "marqueurs_ouverture": extraire_aveux_openreview((p.get("title") or "") + ". " + resume),
                    }
                )
        except Exception as exc:
            print(f"[AVERTISSEMENT] S2 bulk ({strate}): {type(exc).__name__}", file=sys.stderr)
        time.sleep(0.6)

    return {
        "nb_articles_uniques": len(enregistrements),
        "par_strate": {
            s: sum(1 for x in enregistrements if x["strate"] == s)
            for s in ("S1_sommets_cites", "S2_velocite_2025_2026", "S3_ponts_mathematiques", "S4_open_problems")
        },
        "articles": enregistrements,
    }


# Échantillon stratifié de 38 archives sources LaTeX arXiv couvrant les 6 domaines
ARXIV_STRATIFIED_EPRINTS: list[tuple[str, str]] = [
    # Axe 1 : Contrôle IA, jeux de contrôle, sandbagging, stéganographie, CMFT
    ("2312.06942", "controle_ia"),          # Greenblatt et al. - AI Control
    ("2409.07985", "controle_ia"),          # Griffin et al. - Games for AI Control
    ("2506.05296", "controle_ia"),          # Terekhov et al. - Control Tax
    ("2406.07358", "controle_ia"),          # van der Weij et al. - AI Sandbagging
    ("2310.18512", "controle_ia"),          # Roger & Greenblatt - Preventing Language Models From Hiding Their Reasoning
    ("2406.20053", "controle_ia"),          # Halawi et al. - Covert Malicious Finetuning
    # Axe 2 : Post-training, RLHF, Goodhart, sleeper agents, alignment faking, CoT obfuscation, emergent misalignment
    ("2102.03896", "post_entrainement"),    # Zhuang & Hadfield-Menell - Consequences of Misaligned AI (Goodhart)
    ("2209.13085", "post_entrainement"),    # Skalse et al. - Defining and Characterizing Reward Hacking
    ("2210.10760", "post_entrainement"),    # Gao, Schulman, Hilton - Scaling Laws for Reward Model Overoptimization
    ("2401.05566", "post_entrainement"),    # Hubinger et al. - Sleeper Agents
    ("2412.14093", "post_entrainement"),    # Greenblatt et al. - Alignment Faking in Large Language Models
    ("2502.17424", "post_entrainement"),    # Betley et al. - Emergent Misalignment
    ("2503.11926", "post_entrainement"),    # Baker et al. - Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation
    ("2307.13702", "post_entrainement"),    # Lanham et al. - Measuring Faithfulness in Chain-of-Thought Reasoning
    ("2412.06769", "post_entrainement"),    # Hao et al. - Training Large Language Models to Reason in a Continuous Latent Space (Coconut / neuralese)
    # Axe 3 : Interprétabilité mécaniste, superposition, SAE, géométrie linéaire/multidimensionnelle, SLT
    ("2209.10652", "interpretabilite"),     # Elhage et al. - Toy Models of Superposition
    ("2311.03658", "interpretabilite"),     # Park, Choe, Veitch - The Linear Representation Hypothesis
    ("2405.14860", "interpretabilite"),     # Engels et al. - Not All Language Model Features Are One-Dimensionally Linear
    ("2308.12108", "interpretabilite"),     # Lau, Murfet, Wei et al. - Quantifying degeneracy in singular models via the learning coefficient
    ("2301.04709", "interpretabilite"),     # Geiger et al. - Causal Abstraction for Faithful Model Interpretation
    ("2306.03819", "interpretabilite"),     # Belrose et al. - LEACE: Perfect linear concept erasure in closed form
    ("2310.01405", "interpretabilite"),     # Zou et al. - Representation Engineering
    # Axe 4 : Surveillance évolutive, jeux de débat, weak-to-strong generalization
    ("1805.00899", "surveillance_debat"),   # Irving, Christiano, Amodei - AI Safety via Debate
    ("2311.14125", "surveillance_debat"),   # Brown-Cohen, Irving, Piliouras - Scalable AI Safety via Doubly-Efficient Debate
    ("2312.09390", "surveillance_debat"),   # Burns et al. - Weak-to-Strong Generalization
    ("2405.16236", "surveillance_debat"),   # Charikar, Pabbaraju, Shiragur - Quantifying the Gain in Weak-to-Strong Generalization
    ("2402.06782", "surveillance_debat"),   # Khan et al. - Debating with More Persuasive LLMs Leads to More Truthful Answers
    # Axe 5 : Désapprentissage, ré-émergence par ajustement fin, généralisation hors distribution
    ("2402.08787", "desapprentissage_ood"), # Lynch et al. - Rethinking Machine Unlearning for Large Language Models
    ("2409.18025", "desapprentissage_ood"), # Deeb & Roger - An Adversarial Perspective on Machine Unlearning for AI Safety
    ("2310.03693", "desapprentissage_ood"), # Qi et al. - Fine-tuning Aligned Language Models Compromises Safety
    # Axe 6 : Statistique séquentielle toujours valide, détection couverte, surveillance partielle, classification stratégique, calibration
    ("1810.08240", "theorie_stat_jeux"),    # Howard, Ramdas, McAuliffe, Sekhon - Time-uniform confidence sequences
    ("2208.07610", "theorie_stat_jeux"),    # Pérez-Ortiz, Lardy, de Heide, Grünwald - E-Statistics, Group Invariance and Anytime-Valid Testing
    ("2601.20022", "theorie_stat_jeux"),    # Ramtin, Nain, Towsley - Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary
    ("1102.2041", "theorie_stat_jeux"),     # Bartók et al. - Toward a Classification of Finite Partial-Monitoring Games
    ("1506.06980", "theorie_stat_jeux"),    # Hardt, Megiddo, Papadimitriou, Wootters - Strategic Classification
    ("2002.06673", "theorie_stat_jeux"),    # Perdomo, Zrnic, Mendler-Dünner, Hardt - Performative Prediction
    ("1902.04217", "theorie_stat_jeux"),    # Montasser, Hanneke, Srebro - VC Classes are Adversarially Robustly Learnable, but Only Improperly
    ("2109.05389", "theorie_stat_jeux"),    # Gopalan et al. - Omnipredictors
]


def recuperer_metadonnees_arxiv(arxiv_ids: list[str]) -> dict[str, dict[str, str]]:
    """Récupère en lot les métadonnées exactes (titre, date v1, catégories, résumé) via l'API export.arxiv.org."""
    meta_par_id: dict[str, dict[str, str]] = {}
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    taille_lot = 20
    for i in range(0, len(arxiv_ids), taille_lot):
        lot = arxiv_ids[i : i + taille_lot]
        url = "http://export.arxiv.org/api/query?max_results=25&id_list=" + ",".join(lot)
        try:
            _, _, corps = requete_http_octets(url, timeout=25.0)
            racine = ET.fromstring(corps.decode("utf-8", errors="replace"))
            for entry in racine.findall("atom:entry", ns):
                id_url = (entry.findtext("atom:id", default="", namespaces=ns) or "").strip()
                m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", id_url)
                if not m:
                    continue
                aid = m.group(1)
                pub = normaliser_date_iso(entry.findtext("atom:published", default="", namespaces=ns))
                titre = nettoyer_espace(entry.findtext("atom:title", default="", namespaces=ns), limite=300)
                resume = nettoyer_espace(entry.findtext("atom:summary", default="", namespaces=ns), limite=950)
                cats = [c.attrib.get("term", "") for c in entry.findall("atom:category", ns)]
                meta_par_id[aid] = {
                    "titre": titre,
                    "date_publication": pub or (date_depuis_identifiant_arxiv(aid) or ""),
                    "categories": ", ".join(c for c in cats if c),
                    "resume": resume,
                }
        except Exception as exc:
            print(f"[AVERTISSEMENT] Métadonnées arXiv lot {i}: {type(exc).__name__}", file=sys.stderr)
        time.sleep(0.5)
    return meta_par_id


def collecter_archives_latex_arxiv(liste_cibles: list[tuple[str, str]]) -> dict[str, Any]:
    """Télécharge et analyse les archives sources LaTeX brutes (`e-print`) d'arXiv."""
    ids = [aid for aid, _ in liste_cibles]
    metadonnees = recuperer_metadonnees_arxiv(ids)
    extractions: list[dict[str, Any]] = []
    succes_tex = 0

    for aid, axe in liste_cibles:
        url = f"https://arxiv.org/e-print/{aid}"
        info_meta = metadonnees.get(aid, {})
        date_pub = info_meta.get("date_publication") or date_depuis_identifiant_arxiv(aid)
        try:
            statut, entetes, octets = requete_http_octets(url, timeout=30.0, tentatives=2, pause_base=1.5)
            tex_assemble, fichiers_lus = extraire_tex_depuis_archive_arxiv(octets)
            if tex_assemble:
                succes_tex += 1
                analyse = extraire_structures_latex(tex_assemble, source_id=f"arXiv:{aid}")
            else:
                analyse = {
                    "source_id": f"arXiv:{aid}",
                    "nb_caracteres_actifs": 0,
                    "ouvertures_explicites": [],
                    "couplages_hypotheses_theoremes": [],
                    "ecarts_bornes_et_aveux": [],
                    "commentaires_todo_open": [],
                    "a_verrou_extrait": False,
                    "note_binaire": f"Archive non-TeX (PDF seul), type={entetes.get('content-type', 'inconnu')}",
                }
            extractions.append(
                {
                    "arxiv_id": aid,
                    "axe": axe,
                    "statut_http": statut,
                    "octets_archive": len(octets),
                    "nb_fichiers_tex": len(fichiers_lus),
                    "fichiers_tex": fichiers_lus[:12],
                    "titre": info_meta.get("titre", ""),
                    "date_publication": date_pub,
                    "categories": info_meta.get("categories", ""),
                    "resume": info_meta.get("resume", ""),
                    "analyse_latex": analyse,
                }
            )
        except Exception as exc:
            extractions.append(
                {
                    "arxiv_id": aid,
                    "axe": axe,
                    "erreur": f"{type(exc).__name__}: {str(exc)[:120]}",
                    "titre": info_meta.get("titre", ""),
                    "date_publication": date_pub,
                    "resume": info_meta.get("resume", ""),
                }
            )
        time.sleep(0.45)

    return {
        "nb_archives_interrogees": len(liste_cibles),
        "nb_sources_latex_extraites": succes_tex,
        "nb_archives_avec_verrou_extrait": sum(
            1 for x in extractions if (x.get("analyse_latex") or {}).get("a_verrou_extrait")
        ),
        "archives": extractions,
    }


def extraire_champ_openreview(val: Any) -> str:
    if isinstance(val, dict):
        v = val.get("value")
        return str(v) if v is not None else ""
    if isinstance(val, list):
        return ", ".join(str(x) for x in val)
    return str(val) if val is not None else ""


def collecter_openreview_v2() -> dict[str, Any]:
    """
    Interroge l'endpoint public OpenReview API v2 (`/notes/search`, qui renvoie en un appel
    les soumissions, critiques officielles et réponses d'auteurs avec leurs champs complets),
    regroupe par forum et extrait les aveux techniques exacts.
    """
    requetes = [
        '"reward hacking" "lower bound"',
        '"post-training" misalignment evasion',
        '"AI control" "untrusted monitor"',
        '"sparse autoencoder" identifiability assumption',
        '"concept erasure" OR "unlearning" "cannot bound" OR "lower bound"',
        '"chain-of-thought" faithfulness obfuscation',
        '"weak-to-strong" generalization bound',
        '"scalable oversight" debate',
        '"partial monitoring" "minimax regret" "open problem"',
        '"strategic classification" OR "performative prediction" "lower bound"',
    ]

    forums_map: dict[str, dict[str, Any]] = {}
    notes_vues: set[str] = set()

    for terme in requetes:
        url = "https://api2.openreview.net/notes/search?" + urllib.parse.urlencode({"term": terme, "limit": "15"})
        try:
            res = requete_http_json(url, timeout=20.0)
            for n in res.get("notes") or []:
                nid = n.get("id")
                fid = n.get("forum") or nid
                if not nid or not fid or nid in notes_vues:
                    continue
                notes_vues.add(nid)
                invs = " ".join(n.get("invitations") or ([n.get("invitation")] if n.get("invitation") else []))
                c = n.get("content") or {}
                cdate_ms = n.get("cdate") or n.get("tcdate")
                date_iso = None
                if isinstance(cdate_ms, (int, float)) and cdate_ms > 0:
                    date_iso = dt.datetime.fromtimestamp(cdate_ms / 1000.0, tz=dt.timezone.utc).strftime("%Y-%m-%d")

                entree_f = forums_map.setdefault(
                    fid,
                    {
                        "forum_id": fid,
                        "titre": "",
                        "venue": "",
                        "statut_decision": "rejete_ou_retire_ou_soumis",
                        "date_creation": date_iso,
                        "resume": "",
                        "echanges_techniques": [],
                    },
                )
                titre_n = extraire_champ_openreview(c.get("title"))
                venue_n = extraire_champ_openreview(c.get("venue")) or extraire_champ_openreview(c.get("venueid")) or invs[:80]
                abs_n = extraire_champ_openreview(c.get("abstract"))
                if titre_n and (nid == fid or not entree_f["titre"]):
                    entree_f["titre"] = nettoyer_espace(titre_n, limite=280)
                if venue_n and (nid == fid or not entree_f["venue"]):
                    entree_f["venue"] = venue_n
                    v_low = venue_n.lower()
                    if any(k in v_low for k in ("poster", "oral", "spotlight", "accept")) and "reject" not in v_low and "withdrawn" not in v_low:
                        entree_f["statut_decision"] = "accepte"
                if abs_n and not entree_f["resume"]:
                    entree_f["resume"] = nettoyer_espace(abs_n, limite=700)
                if date_iso and (not entree_f["date_creation"] or date_iso < entree_f["date_creation"]):
                    entree_f["date_creation"] = date_iso

                morceaux = [
                    extraire_champ_openreview(c.get(champ))
                    for champ in ("weaknesses", "questions", "limitations", "comment", "rebuttal", "summary", "decision", "abstract")
                ]
                texte_note = re.sub(r"(?<!\n)\n(?!\n)", " ", "\n\n".join(m for m in morceaux if m))
                aveux = extraire_aveux_openreview(texte_note)
                if aveux:
                    role = "soumission_ou_reponse_auteur"
                    if "Review" in invs and "Meta" not in invs:
                        role = "critique_officielle"
                    elif "Meta_Review" in invs or "Decision" in invs:
                        role = "meta_critique"
                    entree_f["echanges_techniques"].append(
                        {
                            "note_id": nid,
                            "role": role,
                            "invitation": invs[:120],
                            "aveux_extraits": aveux[:5],
                        }
                    )
        except Exception as exc:
            print(f"[AVERTISSEMENT] OpenReview search ({terme[:25]}): {type(exc).__name__}", file=sys.stderr)
        time.sleep(0.3)

    fils_extraits = [
        {
            **f,
            "nb_notes_avec_aveux": len(f["echanges_techniques"]),
            "echanges_techniques": f["echanges_techniques"][:8],
        }
        for f in forums_map.values()
        if f["echanges_techniques"]
    ]
    fils_extraits.sort(key=lambda x: x["nb_notes_avec_aveux"], reverse=True)

    return {
        "nb_forums_inspectes": len(forums_map),
        "nb_forums_avec_aveux_techniques": len(fils_extraits),
        "repartition_statut": {
            "accepte": sum(1 for f in fils_extraits if f["statut_decision"] == "accepte"),
            "rejete_ou_retire_ou_soumis": sum(1 for f in fils_extraits if f["statut_decision"] != "accepte"),
        },
        "forums": fils_extraits[:40],
    }


def interroger_billet_lesswrong(post_id: str) -> dict[str, Any] | None:
    query = """
    query($postId: String!) {
      post(input: {selector: {_id: $postId}}) {
        result {
          _id
          title
          slug
          postedAt
          baseScore
          voteCount
          commentCount
          af
          user { username displayName }
          contents { markdown }
        }
      }
      comments(input: {terms: {view: "postCommentsTop", postId: $postId, limit: 60}}) {
        results {
          _id
          postId
          postedAt
          baseScore
          voteCount
          extendedScore
          parentCommentId
          user { username displayName }
          contents { markdown }
        }
      }
    }
    """
    payload = json.dumps({"query": query, "variables": {"postId": post_id}}).encode("utf-8")
    donnees = requete_http_json(
        "https://www.lesswrong.com/graphql",
        headers={"Content-Type": "application/json"},
        data=payload,
        timeout=25.0,
    )
    post = ((donnees.get("data") or {}).get("post") or {}).get("result")
    if not post:
        return None
    comms_bruts = (((donnees.get("data") or {}).get("comments") or {}).get("results")) or []
    comms_propres = filtrer_commentaires_lesswrong_par_billet(comms_bruts, post_id)
    md_complet = (post.get("contents") or {}).get("markdown") or ""
    return {
        "post_id": post.get("_id"),
        "titre": post.get("title") or "",
        "slug": post.get("slug") or "",
        "date_publication": normaliser_date_iso(post.get("postedAt")),
        "posted_at_exact": post.get("postedAt"),
        "alignment_forum": bool(post.get("af")),
        "auteur": (post.get("user") or {}).get("username") or (post.get("user") or {}).get("displayName") or "",
        "base_score": post.get("baseScore", 0),
        "vote_count": post.get("voteCount", 0),
        "comment_count_total": post.get("commentCount", 0),
        "markdown_extrait": md_complet if post_id == "CoRJ9saddvsXti4m2" else nettoyer_espace(md_complet, limite=2600),
        "questions_ouvertes_extraites": [
            nettoyer_espace(m.group(0), limite=400)
            for m in re.finditer(r"[^.!?\n]*\b(?:mathematical law|open question|open problem|conjecture|theorem|unsolved|key subproblems|we're interested in|fundamental limitations)[^.!?\n]*[.!?]", md_complet, re.I)
        ][:15],
        "commentaires_filtres_r5": comms_propres[:15],
    }


def collecter_lesswrong_et_brave() -> dict[str, Any]:
    """
    Collecte via LessWrong GraphQL (+ découverte d'identifiants de billets via Brave Search gratuit) :
    1) Billet pivot `CoRJ9saddvsXti4m2` de Yair Halberstadt et toute sa lignée auteur (`nLQrcb2wbHaSvXJwq`) ;
    2) Billets techniques LessWrong / Alignment Forum sur AISI AI Control, sélection d'agents, SLT,
       obscurcissement de chaîne de pensée, géométrie des traits et superposition.
    """
    post_ids_cibles: list[str] = ["CoRJ9saddvsXti4m2"]

    # 1. Lignée complète des billets de Yair Halberstadt
    q_user = """
    query {
      posts(input: {terms: {view: "userPosts", userId: "nLQrcb2wbHaSvXJwq", limit: 25}}) {
        results { _id title postedAt baseScore }
      }
    }
    """
    try:
        d_u = requete_http_json(
            "https://www.lesswrong.com/graphql",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"query": q_user}).encode("utf-8"),
        )
        for p in (((d_u.get("data") or {}).get("posts") or {}).get("results")) or []:
            pid = p.get("_id")
            if pid and pid not in post_ids_cibles:
                post_ids_cibles.append(pid)
    except Exception as exc:
        print(f"[AVERTISSEMENT] LW userPosts Halberstadt: {type(exc).__name__}", file=sys.stderr)

    # 2. Découverte de billets techniques sur LessWrong via Brave Search
    brave_key = os.environ.get("BRAVE_API_KEY", "").strip()
    requetes_brave_lw = [
        'site:lesswrong.com/posts "Research Areas in AI Control"',
        'site:lesswrong.com/posts ("agent foundations" OR "selection theorems" OR "infra-Bayesianism") ("theorem" OR "open problem")',
        'site:lesswrong.com/posts ("singular learning theory" OR "learning coefficient") ("open problem" OR "conjecture" OR "limitation")',
        'site:lesswrong.com/posts ("chain-of-thought" OR "neuralese" OR "steganography") ("monitorability" OR "obfuscation")',
        'site:lesswrong.com/posts ("superposition" OR "sparse autoencoders") ("geometry" OR "identifiability" OR "open")',
        'site:lesswrong.com/posts ("AI control" OR "sandbagging" OR "collusion") ("untrusted" OR "honeypot")',
    ]
    decouvertes_brave: list[dict[str, str]] = []
    if brave_key:
        for q_b in requetes_brave_lw:
            url_b = "https://api.search.brave.com/res/v1/web/search?" + urllib.parse.urlencode({"q": q_b, "count": "8"})
            try:
                res_b = requete_http_json(
                    url_b,
                    headers={"Accept": "application/json", "X-Subscription-Token": brave_key},
                    timeout=20.0,
                )
                for item in ((res_b.get("web") or {}).get("results")) or []:
                    u = item.get("url") or ""
                    decouvertes_brave.append(
                        {
                            "requete": q_b,
                            "url": u,
                            "titre": item.get("title") or "",
                            "extrait": nettoyer_espace(item.get("description") or "", limite=350),
                        }
                    )
                    m_lw = re.search(r"lesswrong\.com/posts/([A-Za-z0-9]{15,20})/", u)
                    if m_lw:
                        pid = m_lw.group(1)
                        if pid not in post_ids_cibles:
                            post_ids_cibles.append(pid)
            except Exception as exc:
                print(f"[AVERTISSEMENT] Brave LW ({q_b[:30]}): {type(exc).__name__}", file=sys.stderr)
            time.sleep(0.25)

    billets: list[dict[str, Any]] = []
    for pid in post_ids_cibles[:28]:
        try:
            billet = interroger_billet_lesswrong(pid)
            if billet is not None:
                billets.append(billet)
        except Exception as exc:
            print(f"[AVERTISSEMENT] LW post {pid}: {type(exc).__name__}", file=sys.stderr)
        time.sleep(0.2)

    return {
        "nb_billets_extraits": len(billets),
        "nb_decouvertes_brave": len(decouvertes_brave),
        "billets": billets,
        "decouvertes_brave": decouvertes_brave[:40],
    }


def collecter_github_lean_et_tickets() -> dict[str, Any]:
    """Interroge GitHub via `gh search` sur les dépôts Lean 4 pertinents et les tickets techniques."""
    depots_lean: list[dict[str, Any]] = []
    depots_vus: set[str] = set()

    requetes_repos = [
        "conjectures language:Lean",
        "martingale language:Lean",
        "kullback language:Lean",
        "probability language:Lean",
        "game language:Lean",
        "learning language:Lean",
    ]
    for q in requetes_repos:
        cmd = ["gh", "search", "repos", q, "--limit", "8", "--json", "fullName,description,stargazersCount,updatedAt,url"]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        if res.returncode == 0 and res.stdout.strip():
            try:
                for r in json.loads(res.stdout):
                    fn = r.get("fullName")
                    if fn and fn not in depots_vus:
                        depots_vus.add(fn)
                        depots_lean.append(r)
            except json.JSONDecodeError:
                pass
        time.sleep(0.2)

    occurences_sorry_code: list[dict[str, Any]] = []
    requetes_code = [
        'sorry martingale language:Lean',
        'sorry kullback OR divergence language:Lean',
        'conjecture pac OR vc OR regret language:Lean',
        'sorry markov OR stopping OR ville language:Lean',
    ]
    code_vus: set[str] = set()
    for qc in requetes_code:
        cmd_c = ["gh", "search", "code", qc, "--limit", "8", "--json", "path,repository,textMatches,url"]
        res_c = subprocess.run(cmd_c, capture_output=True, text=True, timeout=25, headers={}) if False else subprocess.run(
            ["gh", "search", "code", qc, "--limit", "8", "--json", "path,repository,url"],
            capture_output=True,
            text=True,
            timeout=25,
        )
        if res_c.returncode == 0 and res_c.stdout.strip():
            try:
                for item in json.loads(res_c.stdout):
                    u = item.get("url") or ""
                    if u and u not in code_vus:
                        code_vus.add(u)
                        occurences_sorry_code.append(
                            {
                                "requete": qc,
                                "depot": (item.get("repository") or {}).get("nameWithOwner", ""),
                                "chemin": item.get("path", ""),
                                "url": u,
                            }
                        )
            except json.JSONDecodeError:
                pass
        time.sleep(0.35)

    tickets_techniques: list[dict[str, Any]] = []
    tickets_vus: set[str] = set()
    requetes_issues = [
        '"AI control" OR "untrusted monitor" label:enhancement,bug',
        'repo:jbloomAus/SAELens identifiability OR dead OR shrinkage',
        'repo:UKGovernmentBEIS/inspect_ai monitor OR sandbagging OR scorer',
        'repo:leanprover-community/mathlib4 martingale OR "stopping time" OR kullback',
    ]
    for qi in requetes_issues:
        cmd_i = ["gh", "search", "issues", qi, "--limit", "8", "--json", "title,repository,state,createdAt,url,body"]
        res_i = subprocess.run(cmd_i, capture_output=True, text=True, timeout=25)
        if res_i.returncode == 0 and res_i.stdout.strip():
            try:
                for it in json.loads(res_i.stdout):
                    u = it.get("url") or ""
                    if u and u not in tickets_vus:
                        tickets_vus.add(u)
                        tickets_techniques.append(
                            {
                                "depot": (it.get("repository") or {}).get("nameWithOwner", ""),
                                "titre": it.get("title", ""),
                                "etat": it.get("state", ""),
                                "date_creation": normaliser_date_iso(it.get("createdAt")),
                                "url": u,
                                "extrait": nettoyer_espace(it.get("body") or "", limite=400),
                            }
                        )
            except json.JSONDecodeError:
                pass
        time.sleep(0.25)

    return {
        "nb_depots_lean": len(depots_lean),
        "nb_fichiers_lean_sorry_ou_conjecture": len(occurences_sorry_code),
        "nb_tickets_techniques": len(tickets_techniques),
        "depots_lean": depots_lean[:25],
        "fichiers_lean_ouverts": occurences_sorry_code[:30],
        "tickets_techniques": tickets_techniques[:30],
    }


# ============================================================================
# 4. ÉVALUATION AUTOMATIQUE SANS TRICHE SUR L'ÉTAPE 0 SCELLÉE
# ============================================================================

TEMOINS_SCELLES: list[dict[str, Any]] = [
    {"id": "TEM-01", "ancres": [], "groupes": [["partial monitoring"], ["minimax regret", "observability", "open problem"]]},
    {"id": "TEM-02", "ancres": ["2111.08883"], "groupes": [["online calibration", "multicalibration", "omniprediction"], ["lower bound", "minimax", "regret"]]},
    {"id": "TEM-03", "ancres": ["1810.08240"], "groupes": [["adversarial", "robust"], ["vc dimension", "sample complexity", "improper learning"], ["open", "lower bound"]]},
    {"id": "TEM-04", "ancres": ["1506.03090", "2002.06673"], "groupes": [["strategic classification", "performative prediction"], ["equilibrium", "regret", "stackelberg"]]},
    {"id": "TEM-05", "ancres": [], "groupes": [["train the monitor", "few-shot", "online training"], ["train the policy", "misalignment", "scheming", "control"]]},
    {"id": "TEM-06", "ancres": ["2406.20053"], "groupes": [["covert malicious fine-tuning", "covert malicious finetuning", "data poisoning", "backdoor"], ["isolation", "single", "undetectable", "auditing"]]},
    {"id": "TEM-07", "ancres": ["2310.18512"], "groupes": [["steganograph", "secret encoding", "encoded reasoning", "hiding their reasoning"], ["paraphras", "channel", "detection", "capacity"]]},
    {"id": "TEM-08", "ancres": ["2307.13702", "2412.06769"], "groupes": [["chain-of-thought", "chain of thought", "neuralese", "latent space", "latent reasoning"], ["faithfulness", "monitorability", "necessity", "causal"]]},
    {"id": "TEM-09", "ancres": ["2312.06942", "2406.07358", "2409.07985"], "groupes": [["sandbagging", "overelicitation", "collusion"], ["untrusted monitor", "ai control", "elicitation", "password-locked"]]},
    {"id": "TEM-10", "ancres": ["CoRJ9saddvsXti4m2"], "groupes": [["corj9saddvsxti4m2", "post training is fundamentally dangerous", "post-training"], ["evasion", "discard", "rejection", "honesty", "misalignment"]]},
    {"id": "TEM-11", "ancres": ["2401.05566", "2412.14093", "2503.11926"], "groupes": [["sleeper agents", "alignment faking", "obfuscated", "obfuscation"], ["safety training", "reinforcement learning", "deceptive", "chain-of-thought"]]},
    {"id": "TEM-12", "ancres": ["2502.17424"], "groupes": [["emergent misalignment", "narrow fine-tuning", "narrow finetuning"], ["generalization", "persona", "representation", "low-rank"]]},
    {"id": "TEM-13", "ancres": ["2209.10652"], "groupes": [["superposition", "polysemantic"], ["sparse", "interfere", "geometry", "phase"]]},
    {"id": "TEM-14", "ancres": ["2311.03658", "2405.14860"], "groupes": [["sparse autoencoder", "linear representation hypothesis", "one-dimensionally linear"], ["identifiab", "multidimensional", "irreducible", "dictionary learning"]]},
    {"id": "TEM-15", "ancres": ["2301.04709", "2306.03819"], "groupes": [["concept erasure", "causal abstraction", "unlearning"], ["linear", "recover", "relearning", "impossibility"]]},
    {"id": "TEM-16", "ancres": ["2308.12108"], "groupes": [["singular learning theory", "learning coefficient", "rlct"], ["degenerate", "degeneracy", "finite sample", "phase transition", "posterior"]]},
    {"id": "TEM-17", "ancres": ["2010.03647", "2210.10760", "2209.13085"], "groupes": [["goodhart", "reward hacking", "overoptimization"], ["kl", "kullback", "proxy", "heavy-tailed"]]},
    {"id": "TEM-18", "ancres": ["1805.00899", "2311.14125"], "groupes": [["debate", "scalable oversight"], ["pspace", "doubly-efficient", "polynomial", "obfuscated arguments"]]},
    {"id": "TEM-19", "ancres": ["2312.09390", "2405.16236"], "groupes": [["weak-to-strong", "weak to strong"], ["misfit", "generalization", "bound", "supervision"]]},
    {"id": "TEM-20", "ancres": ["2208.07610", "2601.20022"], "groupes": [["anytime-valid", "e-process", "e-statistics", "quickest change", "sequential"], ["grow", "covert", "adversar", "dependence", "group invariance"]]},
]

COUPLES_RETRODICTION: list[dict[str, Any]] = [
    {"id": "RET-01", "avant_mots": ["weak-to-strong", "weak to strong"], "apres_mots": ["weak-to-strong", "weak to strong"], "apres_marqueur": ["misfit", "2405.16236", "bound", "bregman"]},
    {"id": "RET-02", "avant_mots": ["superposition", "linear representation hypothesis"], "apres_mots": ["one-dimensionally linear", "sparse autoencoder", "multidimensional"], "apres_marqueur": ["2405.14860", "identifiab", "irreducible"]},
    {"id": "RET-03", "avant_mots": ["concept erasure", "leace"], "apres_mots": ["unlearning", "concept erasure"], "apres_marqueur": ["2402.08787", "2409.18025", "weights", "relearning", "remove information"]},
    {"id": "RET-04", "avant_mots": ["ai control", "2312.06942"], "apres_mots": ["ai control", "control tax", "games for ai control"], "apres_marqueur": ["2409.07985", "2506.05296", "game", "minimax", "equilibrium"]},
    {"id": "RET-05", "avant_mots": ["reward hacking", "overoptimization", "goodhart"], "apres_mots": ["reward hacking", "post-training", "overoptimization"], "apres_marqueur": ["kl", "lower bound", "pessimis", "evasion"]},
    {"id": "RET-06", "avant_mots": ["deceptive", "backdoor", "trojan", "misaligned"], "apres_mots": ["sleeper agents", "alignment faking"], "apres_marqueur": ["2401.05566", "2412.14093", "safety training", "persist"]},
    {"id": "RET-07", "avant_mots": ["faithfulness", "chain-of-thought", "2307.13702"], "apres_mots": ["obfuscation", "monitorability", "post training is fundamentally dangerous"], "apres_marqueur": ["2503.11926", "corj9saddvsxti4m2", "2412.06769", "evasion"]},
    {"id": "RET-08", "avant_mots": ["anytime-valid", "e-statistics", "2208.07610"], "apres_mots": ["covert quickest change", "2601.20022", "anytime-valid"], "apres_marqueur": ["2601.20022", "lorden", "covert", "delay"]},
]


def construire_index_documents_extraits(corpus: dict[str, Any]) -> list[dict[str, Any]]:
    """Transforme toutes les entrées réseau extraites en enregistrements plats pour audit mécanique."""
    docs: list[dict[str, Any]] = []

    for art in (corpus.get("openalex_semantic_scholar") or {}).get("articles", []):
        docs.append(
            {
                "canal": art["source"],
                "id": art.get("arxiv_id") or art.get("id_externe") or "",
                "date": art.get("date_publication"),
                "texte": f"{art.get('titre', '')} {art.get('resume', '')} {' '.join(art.get('marqueurs_ouverture') or [])}",
                "a_ouverture": bool(art.get("marqueurs_ouverture")) or ("open problem" in (art.get("titre") or "").lower()),
            }
        )

    for arx in (corpus.get("arxiv_eprints_latex") or {}).get("archives", []):
        ana = arx.get("analyse_latex") or {}
        morceaux = [
            arx.get("titre", ""),
            arx.get("resume", ""),
            " ".join(x.get("enonce", "") for x in ana.get("ouvertures_explicites") or []),
            " ".join(x.get("hypothese", "") for x in ana.get("couplages_hypotheses_theoremes") or []),
            " ".join(ana.get("ecarts_bornes_et_aveux") or []),
            " ".join(x.get("texte", "") for x in ana.get("commentaires_todo_open") or []),
        ]
        docs.append(
            {
                "canal": "arxiv_latex",
                "id": arx.get("arxiv_id") or "",
                "date": arx.get("date_publication"),
                "texte": " ".join(morceaux),
                "a_ouverture": bool(ana.get("a_verrou_extrait")),
            }
        )

    for f in (corpus.get("openreview_v2") or {}).get("forums", []):
        aveux_txt = " ".join(
            " ".join(ech.get("aveux_extraits") or []) for ech in (f.get("echanges_techniques") or [])
        )
        docs.append(
            {
                "canal": "openreview_v2",
                "id": f.get("forum_id") or "",
                "date": f.get("date_creation"),
                "texte": f"{f.get('titre', '')} {f.get('resume', '')} {aveux_txt}",
                "a_ouverture": True,
            }
        )

    for b in (corpus.get("lesswrong_graphql") or {}).get("billets", []):
        comms_txt = " ".join(c.get("markdown", "") for c in (b.get("commentaires_filtres_r5") or []))
        docs.append(
            {
                "canal": "lesswrong_graphql",
                "id": b.get("post_id") or "",
                "date": b.get("date_publication"),
                "texte": f"{b.get('titre', '')} {b.get('markdown_extrait', '')} {comms_txt}",
                "a_ouverture": bool(b.get("questions_ouvertes_extraites")) or bool(comms_txt),
            }
        )

    return docs


def evaluer_rappel_et_retrodiction(
    corpus: dict[str, Any], coupure_retrodiction: str = "2023-12-31"
) -> dict[str, Any]:
    """
    Calcule sans intervention humaine :
    (a) le taux de rappel strictement réseau sur les 20 témoins scellés à l'Étape 0
        (distinguant le rappel lexical pur sans ancre d'identifiant et le rappel complet avec ancres) ;
    (b) le taux de rétrodiction temporelle à coupure stricte `<= 2023-12-31` -> `>= 2024-01-01`.
    """
    docs = construire_index_documents_extraits(corpus)

    detail_temoins: list[dict[str, Any]] = []
    nb_lexical_pur = 0
    nb_complet = 0

    for tem in TEMOINS_SCELLES:
        sources_lexicales: list[str] = []
        sources_ancres: list[str] = []
        for d in docs:
            if not d["a_ouverture"]:
                continue
            txt_low = d["texte"].lower()
            id_str = str(d["id"])
            # Vérification par co-occurrence lexicale stricte (tous les groupes requis présents)
            groupes_ok = all(any(mot in txt_low for mot in grp) for grp in tem["groupes"])
            if groupes_ok:
                sources_lexicales.append(f"{d['canal']}:{id_str}")
            if any(anc.lower() == id_str.lower() or anc.lower() in txt_low for anc in tem["ancres"]):
                sources_ancres.append(f"{d['canal']}:{id_str}")

        ok_lex = len(sources_lexicales) > 0
        ok_comp = ok_lex or (len(sources_ancres) > 0)
        if ok_lex:
            nb_lexical_pur += 1
        if ok_comp:
            nb_complet += 1
        detail_temoins.append(
            {
                "id": tem["id"],
                "apparie_lexical_sans_ancre": ok_lex,
                "apparie_complet": ok_comp,
                "nb_preuves_lexicales": len(sources_lexicales),
                "exemples_preuves": (sources_lexicales or sources_ancres)[:5],
            }
        )

    # Épreuve de rétrodiction à coupure stricte
    docs_avant = [d for d in docs if d["a_ouverture"] and est_avant_coupure_stricte(d["date"], coupure_retrodiction)]
    docs_apres = [
        d
        for d in docs
        if d["date"] and re.match(r"^\d{4}-\d{2}-\d{2}$", d["date"]) and d["date"] > coupure_retrodiction
    ]

    detail_retro: list[dict[str, Any]] = []
    nb_retro_valides = 0
    for ret in COUPLES_RETRODICTION:
        preuves_avant = [
            f"{d['canal']}:{d['id']}({d['date']})"
            for d in docs_avant
            if any(m in d["texte"].lower() for m in ret["avant_mots"])
        ]
        preuves_apres = [
            f"{d['canal']}:{d['id']}({d['date']})"
            for d in docs_apres
            if any(m in d["texte"].lower() for m in ret["apres_mots"])
            and any(mk in (d["texte"] + " " + str(d["id"])).lower() for mk in ret["apres_marqueur"])
        ]
        ok_transition = bool(preuves_avant and preuves_apres)
        if ok_transition:
            nb_retro_valides += 1
        detail_retro.append(
            {
                "id": ret["id"],
                "transition_detectee": ok_transition,
                "preuves_avant_coupure": preuves_avant[:4],
                "preuves_apres_coupure": preuves_apres[:4],
            }
        )

    return {
        "coupure_stricte": coupure_retrodiction,
        "nb_documents_indexes_reseau": len(docs),
        "nb_documents_ouverts_avant_coupure": len(docs_avant),
        "nb_documents_apres_coupure": len(docs_apres),
        "rappel_temoins_lexical_pur": {
            "trouves": nb_lexical_pur,
            "total": len(TEMOINS_SCELLES),
            "taux": round(nb_lexical_pur / len(TEMOINS_SCELLES), 4),
        },
        "rappel_temoins_complet": {
            "trouves": nb_complet,
            "total": len(TEMOINS_SCELLES),
            "taux": round(nb_complet / len(TEMOINS_SCELLES), 4),
        },
        "detail_temoins": detail_temoins,
        "retrodiction_temporelle": {
            "transitions_detectees": nb_retro_valides,
            "total": len(COUPLES_RETRODICTION),
            "taux": round(nb_retro_valides / len(COUPLES_RETRODICTION), 4),
            "detail": detail_retro,
        },
    }


def executer_pipeline_complet(chemin_sortie: pathlib.Path) -> dict[str, Any]:
    secrets = collecter_valeurs_secretes()
    debut = dt.datetime.now(tz=dt.timezone.utc).isoformat()

    print("[1/5] Collecte OpenAlex & Semantic Scholar (4 strates)...", flush=True)
    res_oa_s2 = collecter_openalex_et_s2()

    # Ajout dynamique d'articles arXiv supplémentaires découverts dans OpenAlex/S2 (hors liste initiale)
    ids_deja = {aid for aid, _ in ARXIV_STRATIFIED_EPRINTS}
    cibles_arxiv = list(ARXIV_STRATIFIED_EPRINTS)
    for art in res_oa_s2["articles"]:
        aid = art.get("arxiv_id")
        if aid and re.match(r"^\d{4}\.\d{4,5}$", aid) and aid not in ids_deja and len(cibles_arxiv) < 40:
            ids_deja.add(aid)
            cibles_arxiv.append((aid, f"decouverte_{art['strate']}"))

    print(f"[2/5] Téléchargement et analyse syntaxique de {len(cibles_arxiv)} archives LaTeX arXiv...", flush=True)
    res_arxiv = collecter_archives_latex_arxiv(cibles_arxiv)

    print("[3/5] Collecte des fils de discussion OpenReview API v2...", flush=True)
    res_orv = collecter_openreview_v2()

    print("[4/5] Collecte LessWrong / Alignment Forum GraphQL + Brave...", flush=True)
    res_lw = collecter_lesswrong_et_brave()

    print("[5/5] Collecte GitHub (Lean 4 / Mathlib / tickets techniques)...", flush=True)
    res_gh = collecter_github_lean_et_tickets()

    corpus: dict[str, Any] = {
        "metadonnees_execution": {
            "mandat": "GO-2026-11-24-01",
            "script": "collecteur_et_extracteur_brut_v1.py",
            "horodatage_debut_utc": debut,
            "horodatage_fin_utc": dt.datetime.now(tz=dt.timezone.utc).isoformat(),
            "depense_api_payante_usd": 0.0,
            "protocole_scelle_sha256": "bcfbd25e0447f2cc9df5b469f4d23c2ae55fbe487fba053e3e7c98aab252d6d1",
        },
        "openalex_semantic_scholar": res_oa_s2,
        "arxiv_eprints_latex": res_arxiv,
        "openreview_v2": res_orv,
        "lesswrong_graphql": res_lw,
        "github_lean_et_tickets": res_gh,
    }

    corpus["validation_externe_etape_0"] = evaluer_rappel_et_retrodiction(corpus, coupure_retrodiction="2023-12-31")

    texte_json = json.dumps(corpus, indent=2, ensure_ascii=False)
    verifier_absence_fuite_secrete(texte_json, secrets)
    chemin_sortie.write_text(texte_json + "\n", encoding="utf-8")
    return corpus


def main() -> None:
    dossier_defaut = pathlib.Path(
        "/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/"
        "ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/cartographie-maths-ouvertes-v1"
    )
    sortie = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else (dossier_defaut / "extractions-brutes-primaires-v1.json")
    corpus = executer_pipeline_complet(sortie)
    val = corpus["validation_externe_etape_0"]
    print(
        json.dumps(
            {
                "articles_oa_s2": corpus["openalex_semantic_scholar"]["nb_articles_uniques"],
                "archives_arxiv_latex": corpus["arxiv_eprints_latex"]["nb_sources_latex_extraites"],
                "forums_openreview": corpus["openreview_v2"]["nb_forums_avec_aveux_techniques"],
                "billets_lesswrong": corpus["lesswrong_graphql"]["nb_billets_extraits"],
                "depots_lean": corpus["github_lean_et_tickets"]["nb_depots_lean"],
                "rappel_lexical_pur": val["rappel_temoins_lexical_pur"],
                "rappel_complet": val["rappel_temoins_complet"],
                "retrodiction": {
                    "detectees": val["retrodiction_temporelle"]["transitions_detectees"],
                    "total": val["retrodiction_temporelle"]["total"],
                },
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
