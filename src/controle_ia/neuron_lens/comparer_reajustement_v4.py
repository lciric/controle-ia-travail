"""Comparaison d'une lentille réajustée (R ou S, lecture par lentille neuronale, Llama 3.1 8B Instruct) à celle du 18 novembre — v4.

Critère servi : le critère d'identité du réajustement en vigueur, à l'écriture de ce programme la v5
(`docs/notes/neuron-lens-v1/devis-reajustement/critere-identite-reajustement-lentilles-v5.md`, `50657b89…`, § 4 et § 7).
**Aucune règle de décision ne change par rapport à la v3** : mêmes seuils (10⁻³, 10⁻⁹, 10⁻⁶, 0,10), mêmes paliers, mêmes libellés de
mention. La v4 ne fait qu'ajouter des préalables (qui ne peuvent que rendre « non comparable », ou suspendre à octets égaux), des lignes
rapportées sans critère, et une sortie écrite là où la v3 s'arrêtait sur une erreur.

v4 = v3 (`comparer_reajustement_v3.py`, `c8fc6203…`, non modifiée) qui porte dans le programme ce que le rédacteur du critère v5 a
relevé (§ 7 : sondes U1 à U4 et U11 à U14, liste K1 à K5, « défauts du programme v3 ») :
1. K2, `depot_propre` : les deux manifestes portent `depot_propre` vrai (préalable) ;
2. K5, champs du haut du manifeste (`commande`, `cree_le`, `decisif`, `graines`, `preenregistrement`, `reserves`, `config_sha256`,
   `depot_propre`, `run_id`, et tout champ présent d'un seul côté) : versés dans la table des différences des manifestes, sans critère ;
3. K1, commit des résultats vérifié : le commit donné (`--commit-resultats`) est un identifiant entier, lisible dans le dépôt, et
   chaque pièce neuve lue (résultat d'ajustement, manifeste, export pour R) a, à ce commit, exactement les octets lus
   (`git show <commit>:<chemin>`) ; le chemin de la pièce dans le dépôt est donné en argument, ou déduit de la place du fichier sous
   le dépôt, et la sortie dit lequel (préalables) ;
4. K2, lanceur neuf rattaché à sa course : le fichier du lanceur neuf donné a exactement les octets du fichier `--chemin-lanceur-neuf`
   au commit que porte le manifeste neuf ; les deux commits des manifestes sont lisibles dans le dépôt (préalables) ;
5. pièces mal formées : une enveloppe, un résultat ou un manifeste qui n'est pas un dictionnaire, `config` ou `versions` qui n'en sont
   pas, `correctifs` qui n'est pas une liste de chemins sont des préalables manqués, avec leur motif ; toute autre erreur (pièce
   illisible, exception) écrit une sortie « non comparable », ou « mention suspendue » si le résultat neuf porte l'empreinte du 18,
   avec le message d'erreur, la ligne de commande et le rappel du nœud de Lazar (critère v5, § 4, « arrêt du programme sur une
   erreur ») ; le programme sort alors avec le code 2 ;
6. `audit_requis` : vrai dès que la liste des déclencheurs n'est pas vide (critère v5, § 6), faux sinon ;
7. mineures : champ `etape` de l'export lu (« export ») ; empreinte du fichier du lanceur de référence versée dans `pieces_lues`, sans
   critère (le critère v5, § 0.2, E1, refuse d'en faire une exigence) ; les étiquettes nomment le critère en vigueur.
Les noms des préalables hérités gardent leurs repères (H2, H3, H5, F2, F3 : contrôles du critère v4 et de la vérification du
programme v2, voir l'en-tête de la v3).

**Ce qui reste à la main, par nature (critère v5, § 7 et § 4) :**
- K1, en partie : vérifier l'empreinte de ce programme avant le lancement, et que le commit donné est bien celui de la branche de
  résultats poussée par la machine, lu sur le dépôt distant (le programme ne voit que le dépôt local qu'on lui donne) ;
- K2, en partie : que le dépôt donné est bien le dépôt de travail ;
- K3, matériel de la machine neuve (modèle de carte, pilote, versions) : la pièce du matériel n'est pas une entrée du programme, et
  le 18 n'a rien laissé à quoi la comparer ;
- K4, reprise sur sauvegarde : elle se lit au journal de la course, que le programme ne lit pas ; il recopie l'indication `--reprise` ;
- K5 : la table est rendue par le programme, mais c'est qui applique le critère qui la recopie dans le verdict ;
- la relecture au lieu de rangement, l'audit, le verdict d'identité et l'avertissement à Lazar.
Si K1 est manqué, le critère v5 dit « pas de verdict, comparaison refaite sur les bonnes pièces » : la mention « non comparable »
(ou suspendue) que rend alors ce programme ne remplace pas cette règle, elle la signale.

Lit seulement : les deux résultats d'ajustement (`b-beta-ajustement-<L>.json`), les deux manifestes, pour R les deux résultats d'export,
le code source des deux lanceurs, et, dans le dépôt donné, les correctifs, les pièces neuves et le lanceur neuf aux commits dits.
Aucune mesure de la course n'est lue. Aucun repli silencieux (R5).
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import re
import subprocess
import sys
import traceback
from pathlib import Path

PROGRAMME = "comparer_reajustement_v4"
CRITERE = "critère d'identité du réajustement en vigueur (v5 à l'écriture du programme, 50657b89…)"

TOLERANCE = 1e-3            # conventionnelle, déclarée telle (critère en vigueur, § 4, deuxième palier) ; constante, non paramètre
COHERENCE_PALIER_1 = 1e-9   # à empreinte égale, les mêmes sommes donnent la même valeur, à l'arrondi près
DIFFS_PALIER_1 = 1e-6       # simple précision, valeurs d'au plus 0,12
DIFFS_PALIER_2 = 1e-3
SEUIL_STABILITE = 0.10
N_DOCS_ATTENDU = [466, 466]
NEXT_DOC_ATTENDU = 932
FONCTION = "_split_half_64"
CHAMPS_CONFIG = ("ajustement", "correctifs", "graines", "modele", "revision", "corpus")
COUCHES_MATRICES_R = 31
COUCHES_SERIES_R = 28
SERIES_R = ("npR_notre_R", "identite_notre_R")
ETAPE_EXPORT = "export"
HAUT_HORS_TABLE = ("versions", "commit", "config")   # déjà rendus ailleurs dans la table des différences des manifestes

# Pièces du 18 novembre (critère en vigueur, § 2) : vérifiées par leur empreinte avant toute comparaison.
REFERENCES = {
    "ajustement-R": "129c43b020854fd395cb0e969dd7f8956844417684e1e3a1099fee5e7f16d2ab",
    "ajustement-S": "2dce646e32177941c02987a8ba3a0a67fd45d17f335e58ba9e321d3e0367c297",
    "export-R": "17304c936792e4b79e9a47d78abf5bb6966310c36b92f387b3303b23891eedf1",
    "manifeste": "b90c15140074e9d41a3cf93e8bcaf55f80cc025d07d2d46432239d1c6b6e3444",
    # empreinte du texte de `_split_half_64` dans `b_beta_lancer_v3.py` (`582fd9ef…`), lanceur de la course du 18
    "fonction": "a5495c68779bb67059cade18b3a92aaf7cf7fd0200f1770b038d8c5d0e62703c",
}
# Empreintes des deux fichiers d'ajustement du 18 (critère en vigueur, § 2). Elles ne servent qu'à l'arrêt sur une erreur, pour dire
# si le résultat neuf « porte l'empreinte du 18 » quand la pièce de référence n'a pas pu être lue.
EMPREINTES_FICHIERS_18 = {
    "R": "31061d6c6c4b521c43d4710f9b660184b285467a065dadb5fc48e48c6d48c64c",
    "S": "aac70eef8f57b5d4423e5c8f8b2e77033b15077d95ef5a81894dbe3e0436e2b8",
}
CLES_SERIES_R = {str(i) for i in range(COUCHES_SERIES_R)}
CLES_MATRICES_R = {str(i) for i in range(COUCHES_MATRICES_R)}

_TOL = f"{TOLERANCE:.0e}".replace("1e-03", "10⁻³")
PALIER_1 = "palier 1 — même lentille, octets identiques"
PALIER_2 = f"palier 2 — différences entre moitiés concordantes à {_TOL} près ; octets différents ; matrices non comparables"
DIFFERENTE = "différente"
NON_COMPARABLE = "non comparable (traitée comme différente)"
SUSPENDU = "mention suspendue : anomalie (nœud de Lazar)"
NOEUD_ARRET = ("arrêt sur une erreur : nœud de Lazar à ouvrir ; le message d'erreur et la ligne de commande sont versés ; le "
               "programme n'est pas relancé sur des pièces retouchées (critère en vigueur, § 4)")
_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_COMMIT = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")   # identifiant entier : un nom de branche peut bouger, un préfixe est ambigu


def empreinte_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def empreinte_fonction(source: str, nom: str = FONCTION) -> str | None:
    """SHA-256 du texte source exact de la fonction `nom` (None si absente)."""
    for n in ast.walk(ast.parse(source)):
        if isinstance(n, ast.FunctionDef) and n.name == nom:
            seg = ast.get_source_segment(source, n)
            return empreinte_octets(seg.encode("utf-8")) if seg is not None else None
    return None


def empreinte_fonction_dans(octets: bytes) -> tuple[str | None, str]:
    """(empreinte de la fonction, motif) : un lanceur qui n'est pas du Python lisible rend (None, motif), sans exception."""
    try:
        e = empreinte_fonction(octets.decode("utf-8"))
    except (UnicodeDecodeError, SyntaxError, ValueError) as err:
        return None, f"lanceur illisible comme source Python : {type(err).__name__} : {err}"
    return e, "" if e is not None else f"fonction {FONCTION} absente"


def _fini(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def _dico(x) -> dict:
    """`x` s'il est un dictionnaire, sinon un dictionnaire vide : la forme fautive est dite par un préalable « forme », jamais tue."""
    return x if isinstance(x, dict) else {}


def _nom_type(x) -> str:
    return type(x).__name__


def _chemins(x) -> list | None:
    """La liste si `x` est une liste non vide de chaînes non vides, sinon None."""
    if isinstance(x, list) and x and all(isinstance(v, str) and v for v in x):
        return x
    return None


def _series_ok(res: dict, champ: str):
    s = res.get(champ)
    if not isinstance(s, dict) or not s or not all(isinstance(v, list) and v for v in s.values()):
        return None
    return s


# --- lecture du dépôt (K1, K2, correctifs) -----------------------------------------------------------------------------------
def _git(depot, *args) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(depot), *args], capture_output=True)


def _err(r: subprocess.CompletedProcess) -> str:
    return r.stderr.decode("utf-8", "replace").strip()[:300]


def commit_lisible(depot, commit) -> tuple[bool, str]:
    """(vrai, identifiant) si `commit` est un identifiant entier de commit lisible dans `depot` ; sinon (faux, motif)."""
    if depot is None:
        return False, "aucun dépôt donné : non vérifié"
    if not (isinstance(commit, str) and _COMMIT.match(commit)):
        return False, f"identifiant de commit mal formé (identifiant entier en hexadécimal attendu) : {str(commit)[:80]!r}"
    r = _git(depot, "cat-file", "-e", f"{commit}^{{commit}}")
    if r.returncode != 0:
        return False, f"commit {commit} illisible dans le dépôt {depot} : {_err(r)}"
    return True, commit


def octets_au_commit(depot, commit, chemin) -> tuple[bytes | None, str]:
    """(octets du fichier `chemin` au commit, "") par `git show <commit>:<chemin>` ; (None, motif) si le commit ou le fichier manque."""
    ok, motif = commit_lisible(depot, commit)
    if not ok:
        return None, motif
    if not (isinstance(chemin, str) and chemin and not chemin.startswith("/")):
        return None, f"chemin dans le dépôt absent ou mal formé (chemin relatif à la racine attendu) : {str(chemin)[:120]!r}"
    t = _git(depot, "cat-file", "-t", f"{commit}:{chemin}")
    if t.returncode != 0 or t.stdout.strip() != b"blob":
        return None, f"`{chemin}` n'est pas un fichier au commit {commit} : {_err(t) or t.stdout.decode('utf-8', 'replace').strip()}"
    r = _git(depot, "show", f"{commit}:{chemin}")
    if r.returncode != 0:
        return None, f"`git show {commit}:{chemin}` a échoué : {_err(r)}"
    return r.stdout, ""


def rattacher(depot, commit, chemin, octets_lus: bytes) -> dict:
    """Dit si le fichier `chemin` au commit a exactement les octets lus. Rend un relevé : tenu, chemin, commit, empreintes, détail."""
    b, motif = octets_au_commit(depot, commit, chemin)
    lu = empreinte_octets(octets_lus)
    if b is None:
        return {"tenu": False, "chemin": chemin, "commit": commit, "sha256_lu": lu, "sha256_au_commit": None, "detail": motif}
    au_commit = empreinte_octets(b)
    egal = b == octets_lus
    return {"tenu": egal, "chemin": chemin, "commit": commit, "sha256_lu": lu, "sha256_au_commit": au_commit,
            "detail": f"`{chemin}` au commit {commit} : " + ("octets égaux à ceux lus" if egal else
                                                             f"octets différents (lu {lu} ; au commit {au_commit})")}


def chemin_dans_depot(depot, fichier, chemin_donne) -> tuple[str | None, str]:
    """(chemin de la pièce dans le dépôt, d'où il vient). Donné en argument, il prime ; sinon il est déduit de la place du fichier
    sous la racine du dépôt ; sinon None, et le préalable est manqué."""
    if chemin_donne is not None:
        return str(chemin_donne), "donné en argument"
    r = _git(depot, "rev-parse", "--show-toplevel")
    if r.returncode != 0:
        return None, f"non donné, et la racine du dépôt est illisible : {_err(r)}"
    racine = Path(r.stdout.decode("utf-8", "replace").strip())
    try:
        rel = Path(fichier).resolve().relative_to(racine.resolve())
    except ValueError:
        return None, "non donné, et le fichier n'est pas sous la racine du dépôt : chemin non déductible"
    return rel.as_posix(), "déduit de la place du fichier sous la racine du dépôt"


def empreintes_correctifs(depot, commit, chemins) -> dict | None:
    """{chemin: SHA-256 du contenu au commit} lu par `git show` ; None si la liste est mal formée ou si un chemin manque."""
    if _chemins(chemins) is None:
        return None
    out = {}
    for ch in chemins:
        b, _ = octets_au_commit(depot, commit, ch)
        if b is None:
            return None
        out[ch] = empreinte_octets(b)
    return out


# --- préalables --------------------------------------------------------------------------------------------------------------
class _Pre:
    def __init__(self):
        self.liste = []
        self.structure_export = []      # noms des préalables dont dépend le calcul des matrices égales et des séries de R

    def __call__(self, nom, tenu, detail="", *, structure_export=False):
        self.liste.append({"nom": nom, "tenu": bool(tenu), "detail": str(detail)})
        if structure_export:
            self.structure_export.append(nom)

    @property
    def tous(self):
        return all(p["tenu"] for p in self.liste)


def _preconditions(c: dict) -> _Pre:
    p = _Pre()
    c = _dico(c)
    L = c.get("lentille")
    sha_pieces = _dico(c.get("sha_pieces"))
    # forme des pièces (point 5 : une forme inattendue est un préalable manqué, jamais une exception)
    for cote in ("ref", "neuf"):
        e, r, m = c.get(f"env_{cote}"), c.get(cote), c.get(f"m{cote}")
        p(f"forme : enveloppe du résultat d'ajustement en dictionnaire ({cote})", isinstance(e, dict), _nom_type(e))
        p(f"forme : résultat d'ajustement en dictionnaire ({cote})", isinstance(r, dict), _nom_type(r))
        p(f"forme : manifeste en dictionnaire ({cote})", isinstance(m, dict), _nom_type(m))
        p(f"forme : `config` du manifeste en dictionnaire ({cote})", isinstance(_dico(m).get("config"), dict),
          _nom_type(_dico(m).get("config")))
        p(f"forme : `versions` du manifeste en dictionnaire ({cote})", isinstance(_dico(m).get("versions"), dict),
          _nom_type(_dico(m).get("versions")))
        corr = _dico(_dico(m).get("config")).get("correctifs")
        p(f"forme : `config.correctifs` en liste non vide de chemins ({cote})", _chemins(corr) is not None, str(corr)[:120])
    ref, neuf = _dico(c.get("ref")), _dico(c.get("neuf"))
    env_ref, env_neuf = _dico(c.get("env_ref")), _dico(c.get("env_neuf"))
    mref, mneuf = _dico(c.get("mref")), _dico(c.get("mneuf"))
    # provenance
    for cote, r in (("ref", ref), ("neuf", neuf)):
        sha, taille = r.get("sha256"), r.get("taille")
        p(f"empreinte du fichier d'ajustement bien formée ({cote})", isinstance(sha, str) and bool(_HEX64.match(sha)), sha)
        p(f"taille présente ({cote})", isinstance(taille, int) and not isinstance(taille, bool) and taille > 0, taille)
        p(f"`finies` vrai ({cote})", r.get("finies") is True, r.get("finies"))
    attendu = REFERENCES.get(f"ajustement-{L}") if isinstance(L, str) else None
    p("pièce d'ajustement de référence d'empreinte égale au critère", attendu is not None and sha_pieces.get("ajustement_ref") == attendu,
      f"lu {sha_pieces.get('ajustement_ref')} ; attendu {attendu}")
    p("manifeste de référence d'empreinte égale au critère", sha_pieces.get("manifeste_ref") == REFERENCES["manifeste"],
      sha_pieces.get("manifeste_ref"))
    p("manifeste neuf égal à celui que porte le résultat neuf",
      sha_pieces.get("manifeste_neuf") is not None and sha_pieces.get("manifeste_neuf") == env_neuf.get("manifeste_sha256"),
      f"lu {sha_pieces.get('manifeste_neuf')} ; porté {env_neuf.get('manifeste_sha256')}")
    rid_r, rid_n = env_ref.get("run_id"), env_neuf.get("run_id")
    deb_r, deb_n = ref.get("debut_utc"), neuf.get("debut_utc")
    p("course neuve distincte (identifiant et heure de début)", bool(rid_r) and bool(rid_n) and rid_r != rid_n and bool(deb_r)
      and bool(deb_n) and deb_r != deb_n, f"{rid_r}/{deb_r} contre {rid_n}/{deb_n}")
    # K1 et K2 : pièces neuves et lanceur neuf rattachés à leurs commits ; arbre propre
    ratt = _dico(c.get("rattachement"))

    def releve(cle):
        e = ratt.get(cle)
        return (isinstance(e, dict) and e.get("tenu") is True), ("non vérifié" if not isinstance(e, dict) else e.get("detail"))

    def releve_piece(cle):
        # la pièce est tenue si ses octets au commit sont ceux lus, et si l'empreinte au commit est celle que porte `pieces_lues`
        tenu, detail = releve(cle)
        e = _dico(ratt.get(cle))
        porte = sha_pieces.get(cle)
        return tenu and isinstance(porte, str) and e.get("sha256_au_commit") == porte, f"{detail} ; empreinte portée par la sortie : {porte}"

    p("K1 : commit de la branche de résultats en identifiant entier, lisible dans le dépôt", *releve("commit_resultats"))
    p("K1 : résultat d'ajustement neuf égal, à l'octet, au fichier du commit des résultats", *releve_piece("ajustement_neuf"))
    p("K1 : manifeste neuf égal, à l'octet, au fichier du commit des résultats", *releve_piece("manifeste_neuf"))
    for cote, m in (("ref", mref), ("neuf", mneuf)):
        p(f"K2 : `depot_propre` vrai dans le manifeste ({cote})", m.get("depot_propre") is True, m.get("depot_propre"))
        p(f"K2 : commit du manifeste lisible dans le dépôt ({cote})", *releve(f"commit_manifeste_{cote}"))
    p("K2 : lanceur neuf égal, à l'octet, au fichier du commit du manifeste neuf", *releve_piece("lanceur_neuf"))
    # configuration et « même code »
    cr, cn = _dico(mref.get("config")), _dico(mneuf.get("config"))
    for k in CHAMPS_CONFIG:
        p(f"configuration du manifeste : `{k}` égal", k in cr and k in cn and cr[k] == cn[k], f"ref {str(cr.get(k))[:60]} ; neuf {str(cn.get(k))[:60]}")
    dr, dn = cr.get("drowse"), cn.get("drowse")
    p("H5 : `config.drowse` égal (version et empreinte de la roue), présent", bool(dr) and dr == dn, f"{dr} ; {dn}")
    pr_, pn_ = cr.get("precision"), cn.get("precision")
    p("H5 : `config.precision` égal, présent", bool(pr_) and pr_ == pn_, f"{pr_} ; {pn_}")
    vr = {k: v for k, v in _dico(mref.get("versions")).items() if k != "plateforme"}
    vn = {k: v for k, v in _dico(mneuf.get("versions")).items() if k != "plateforme"}
    p("H5 : `versions` égales hors `plateforme`, présentes", bool(vr) and vr == vn,
      sorted(k for k in set(vr) | set(vn) if k not in vr or k not in vn or vr[k] != vn[k]))
    er_, en_ = c.get("correctifs_ref"), c.get("correctifs_neuf")
    lr_, ln_ = _chemins(cr.get("correctifs")), _chemins(cn.get("correctifs"))
    ok_corr = (isinstance(er_, dict) and isinstance(en_, dict) and bool(er_) and lr_ is not None and ln_ is not None
               and set(er_) == set(lr_) and set(en_) == set(ln_) and er_ == en_
               and all(isinstance(v, str) and _HEX64.match(v) for v in er_.values()))
    p("H5 : contenu des correctifs d'empreinte égale aux deux commits", ok_corr,
      "non lu" if not (isinstance(er_, dict) and isinstance(en_, dict)) else
      sorted(k for k in set(er_) | set(en_) if er_.get(k) != en_.get(k)))
    # forme et finitude des séries
    for champ in ("diffs_float64", "diffs"):
        sr, sn = _series_ok(ref, champ), _series_ok(neuf, champ)
        forme = sr is not None and sn is not None and set(sr) == set(sn) and all(len(sr[t]) == len(sn[t]) for t in sr)
        p(f"mêmes cibles, mêmes comptes, séries non vides ({champ})", forme,
          f"ref {None if sr is None else {t: len(v) for t, v in sr.items()}} ; neuf {None if sn is None else {t: len(v) for t, v in sn.items()}}")
        nf = [] if (sr is None or sn is None) else [(cote, t, i) for cote, s in (("ref", sr), ("neuf", sn))
                                                      for t, v in s.items() for i, x in enumerate(v) if not _fini(x)]
        p(f"toutes les valeurs finies et numériques, des deux côtés ({champ})", sr is not None and sn is not None and not nf,
          "forme illisible" if sr is None or sn is None else f"{len(nf)} : {nf[:3]}")
    mr, mn = ref.get("meta"), neuf.get("meta")
    ok_meta = isinstance(mr, dict) and isinstance(mn, dict) and bool(mr) and mr == mn
    p("meta présent et égal champ par champ", ok_meta,
      "absent" if not (isinstance(mr, dict) and isinstance(mn, dict)) else sorted(k for k in set(mr) | set(mn) if mr.get(k, "<absent>") != mn.get(k, "<absent>")))
    for cote, r in (("ref", ref), ("neuf", neuf)):
        p(f"n_docs {N_DOCS_ATTENDU} ({cote})", r.get("n_docs") == N_DOCS_ATTENDU, r.get("n_docs"))
        p(f"next_doc {NEXT_DOC_ATTENDU} ({cote})", r.get("next_doc") == NEXT_DOC_ATTENDU, r.get("next_doc"))
    p("même nom de fichier d'ajustement, présent", bool(ref.get("fichier")) and ref.get("fichier") == neuf.get("fichier"),
      f"{ref.get('fichier')} ; {neuf.get('fichier')}")
    cvr, cvn = cr.get("commit_voisin"), cn.get("commit_voisin")
    p("même commit du code voisin, présent", bool(cvr) and cvr == cvn, f"{cvr} ; {cvn}")
    p(f"même texte de la fonction {FONCTION}, égal à celui du lanceur du 18 (F2)",
      c.get("fref") == REFERENCES["fonction"] and c.get("fref") == c.get("fneuf"),
      f"{c.get('fref')} ; {c.get('fneuf')} ; {_dico(c.get('lecture_lanceurs'))}")
    for cote, rr in (("ref", ref), ("neuf", neuf)):
        p(f"champ `etape` conforme à la lentille ({cote})", L in ("R", "S") and rr.get("etape") == f"ajustement-{L}", rr.get("etape"))
    # pièces d'export de R
    if L == "R":
        p("export de référence d'empreinte égale au critère", sha_pieces.get("export_ref") == REFERENCES["export-R"],
          sha_pieces.get("export_ref"), structure_export=True)
        for cote, e in (("ref", c.get("eref")), ("neuf", c.get("eneuf"))):
            ok = isinstance(e, dict)
            mm = e.get("matrices_moities") if ok else None
            ok_mm = isinstance(mm, dict) and len(mm) == COUCHES_MATRICES_R and all(
                isinstance(v, list) and len(v) == 2 and all(isinstance(h, str) and _HEX64.match(h) for h in v) for v in mm.values())
            p(f"export de R présent avec {COUCHES_MATRICES_R} couches de matrices ({cote})", ok_mm, None if not isinstance(mm, dict) else len(mm),
              structure_export=True)
            p(f"couches des matrices : exactement 0 à 30 (F3, {cote})", isinstance(mm, dict) and set(mm) == CLES_MATRICES_R,
              None if not isinstance(mm, dict) else sorted(set(mm) ^ CLES_MATRICES_R))
            val = e.get("valeurs") if ok else None
            for s in SERIES_R:
                serie = val.get(s) if isinstance(val, dict) else None
                ok_s = isinstance(serie, dict) and len(serie) == COUCHES_SERIES_R and all(_fini(v) for v in serie.values())
                p(f"série {s} présente, {COUCHES_SERIES_R} couches finies ({cote})", ok_s, None if not isinstance(serie, dict) else len(serie),
                  structure_export=True)
                p(f"série {s} : clés exactement 0 à 27 (H3, {cote})", isinstance(serie, dict) and set(serie) == CLES_SERIES_R,
                  None if not isinstance(serie, dict) else sorted(set(serie) ^ CLES_SERIES_R), structure_export=True)
            # mineure : champ `etape` de la pièce d'export
            p(f"champ `etape` de l'export égal à « {ETAPE_EXPORT} » ({cote})", ok and e.get("etape") == ETAPE_EXPORT,
              e.get("etape") if ok else _nom_type(e))
        # export neuf rattaché à la course neuve, différent de celui du 18
        brut = c.get("env_eneuf")
        p("forme : enveloppe de l'export neuf en dictionnaire", isinstance(brut, dict), _nom_type(brut), structure_export=True)
        ee = _dico(brut)
        p("H2 : export neuf de la course neuve (identifiant de course)", bool(ee.get("run_id")) and ee.get("run_id") == env_neuf.get("run_id"),
          f"{ee.get('run_id')} ; {env_neuf.get('run_id')}", structure_export=True)
        p("H2 : export neuf du même manifeste que le résultat neuf", bool(ee.get("manifeste_sha256"))
          and ee.get("manifeste_sha256") == env_neuf.get("manifeste_sha256"), f"{ee.get('manifeste_sha256')}", structure_export=True)
        p("H2 : export neuf différent de celui du 18", bool(sha_pieces.get("export_neuf"))
          and sha_pieces.get("export_neuf") != REFERENCES["export-R"], sha_pieces.get("export_neuf"), structure_export=True)
        p("K1 : export neuf égal, à l'octet, au fichier du commit des résultats", *releve_piece("export_neuf"))
    return p


def preconditions(c: dict) -> list[dict]:
    """`c` : ref, neuf (résultats), env_ref, env_neuf (enveloppes : run_id, manifeste_sha256), mref, mneuf (manifestes),
    sha_pieces (empreintes calculées des fichiers lus), fref, fneuf (empreintes de la fonction), lentille, eref, eneuf (exports, R),
    env_eneuf (enveloppe de l'export neuf), correctifs_ref, correctifs_neuf, rattachement (relevés de `rattacher` : K1, K2)."""
    return _preconditions(c).liste


def _texte_et_empreinte(present: bool, v) -> tuple[str | None, str | None]:
    if not present:
        return None, None
    return str(v)[:200], empreinte_octets(json.dumps(v, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8"))


def differences_manifestes(mref: dict, mneuf: dict) -> dict:
    """Sans critère. Pour `versions`, `commit` et les champs de `config` hors préalables : les clés qui diffèrent, avec les deux
    valeurs. Pour les champs du haut du manifeste (K5 : tout sauf `versions`, `commit`, `config`) : chaque champ qui diffère ou qui
    n'est présent que d'un côté, avec sa présence, le début de sa valeur et l'empreinte de sa valeur entière des deux côtés."""
    mref, mneuf = _dico(mref), _dico(mneuf)
    d = {}
    vr, vn = _dico(mref.get("versions")), _dico(mneuf.get("versions"))
    d["versions"] = {k: [vr.get(k), vn.get(k)] for k in sorted(set(vr) | set(vn)) if vr.get(k) != vn.get(k)}
    d["commit"] = None if mref.get("commit") == mneuf.get("commit") else [mref.get("commit"), mneuf.get("commit")]
    hors = set(CHAMPS_CONFIG) | {"commit_voisin", "drowse", "precision", "correctifs"}
    cr, cn = _dico(mref.get("config")), _dico(mneuf.get("config"))
    d["config"] = {k: [str(cr.get(k))[:200], str(cn.get(k))[:200]] for k in sorted((set(cr) | set(cn)) - hors) if cr.get(k) != cn.get(k)}
    haut = {}
    for k in sorted((set(mref) | set(mneuf)) - set(HAUT_HORS_TABLE)):
        pr, pn = k in mref, k in mneuf
        if pr and pn and mref[k] == mneuf[k]:
            continue
        tr, er = _texte_et_empreinte(pr, mref.get(k))
        tn, en = _texte_et_empreinte(pn, mneuf.get(k))
        haut[k] = {"present_ref": pr, "present_neuf": pn, "ref": tr, "neuf": tn, "sha256_valeur_ref": er, "sha256_valeur_neuf": en}
    d["haut"] = haut
    return d


def _table(ref, neuf, champ):
    return [{"cible": t, "rang": i, "ref": a, "neuf": b, "ecart": b - a}
            for t in sorted(ref[champ]) for i, (a, b) in enumerate(zip(ref[champ][t], neuf[champ][t]))]


def _max_abs(table) -> float:
    m = 0.0
    for r in table:
        if not math.isfinite(r["ecart"]):
            raise ValueError("écart non fini malgré les préalables")
        m = max(m, abs(r["ecart"]))
    return m


def _series_r(eref, eneuf) -> dict:
    out = {}
    for s in SERIES_R:
        a, b = eref["valeurs"][s], eneuf["valeurs"][s]
        couches = sorted(set(a) & set(b), key=int)
        ecarts = {k: b[k] - a[k] for k in couches}
        out[s] = {"couches": len(couches), "ecarts": ecarts, "ecart_max_abs": max(abs(v) for v in ecarts.values()),
                  "ref_min": min(a.values()), "ref_max": max(a.values())}
    return out


def _octets_egaux(ref: dict, neuf: dict) -> bool:
    sha_ok = all(isinstance(r.get("sha256"), str) and _HEX64.match(r["sha256"]) for r in (ref, neuf))
    return bool(sha_ok and ref["sha256"] == neuf["sha256"])


def _comparer(c: dict, *, reprise: bool) -> dict:
    ref, neuf, L = _dico(c.get("ref")), _dico(c.get("neuf")), c.get("lentille")
    pp = _preconditions(c)
    pre = pp.liste
    tous = pp.tous
    out = {"programme": PROGRAMME, "critere": CRITERE, "arret_sur_erreur": False,
           "lentille": L, "tolerance": TOLERANCE, "reprise": bool(reprise), "preconditions": pre, "preconditions_toutes_tenues": tous,
           "pieces_lues": dict(_dico(c.get("sha_pieces"))), "commit_resultats": c.get("commit_resultats"),
           "rattachement_aux_commits": _dico(c.get("rattachement")),
           "sha256": {"ref": ref.get("sha256"), "neuf": neuf.get("sha256")}, "taille": {"ref": ref.get("taille"), "neuf": neuf.get("taille")}}
    declencheurs = []
    octets_egaux = _octets_egaux(ref, neuf)
    # tables et séries de R, seulement si la forme le permet (jamais de maximum sur une valeur non finie)
    forme_ok = all(p["tenu"] for p in pre if p["nom"].startswith(("mêmes cibles", "toutes les valeurs finies")))
    if forme_ok:
        t64, t32 = _table(ref, neuf, "diffs_float64"), _table(ref, neuf, "diffs")
        m64 = _max_abs(t64)
        out.update({"ecart_max_abs_diffs_float64": m64,
                    "ecart_max_rel_diffs_float64": max((abs(r["ecart"]) / abs(r["ref"]) for r in t64 if r["ref"] != 0), default=None),
                    "ecart_max_abs_diffs": _max_abs(t32), "table_ecarts_diffs_float64": t64,
                    "changements_de_cote_du_seuil_0_10_sur_diffs": [
                        {k: r[k] for k in ("cible", "rang", "ref", "neuf")} for r in t32
                        if (r["ref"] <= SEUIL_STABILITE) != (r["neuf"] <= SEUIL_STABILITE)]})
    export_ok = L != "R" or all(p["tenu"] for p in pre if p["nom"] in pp.structure_export)
    out["differences_des_manifestes_sans_critere"] = differences_manifestes(c.get("mref"), c.get("mneuf"))
    if L == "R" and export_ok:
        mm_r, mm_n = c["eref"]["matrices_moities"], c["eneuf"]["matrices_moities"]
        egales = sum(1 for k in mm_r if mm_n.get(k) == mm_r[k])
        out["matrices_moities_egales"] = {"couches_egales": egales, "couches_ref": len(mm_r)}
        out["series_export_R_sans_critere"] = _series_r(c["eref"], c["eneuf"])
    elif L == "S":
        out["series_export_R_sans_critere"] = "sans objet : aucune grandeur sensible à la position n'existe pour S dans les pièces du 18"
    if octets_egaux:
        declencheurs.append("(i) palier 1 obtenu")
        anomalies = []
        if not tous:
            anomalies.append("préalable manqué : " + "; ".join(p["nom"] for p in pre if not p["tenu"]))
        if ref.get("taille") != neuf.get("taille"):
            anomalies.append("taille différente")
        if forme_ok and out["ecart_max_abs_diffs_float64"] > COHERENCE_PALIER_1:
            anomalies.append(f"écart sur diffs_float64 de {out['ecart_max_abs_diffs_float64']:.3e} à empreinte égale")
        if L == "R" and export_ok and out["matrices_moities_egales"]["couches_egales"] != out["matrices_moities_egales"]["couches_ref"]:
            anomalies.append("empreinte du fichier égale mais empreinte de matrice des moitiés différente")
        if L == "R" and export_ok and any(v["ecart_max_abs"] != 0.0 for v in out["series_export_R_sans_critere"].values()):
            anomalies.append("H4 : une série de R change au premier palier")
        if forme_ok and out["ecart_max_abs_diffs"] > DIFFS_PALIER_1:
            anomalies.append(f"H7 : écart sur diffs de {out['ecart_max_abs_diffs']:.3e} au premier palier")
            declencheurs.append("(vii) écart sur diffs au-delà de 10⁻⁶ au premier palier")
        if anomalies:
            declencheurs.append("(v) " + " ; ".join(anomalies))
            out["mention"] = SUSPENDU
        else:
            out["mention"] = PALIER_1 + (" ; reprise sur sauvegarde notée" if reprise else "")
        out["declencheurs"] = declencheurs
        return out
    if not tous:
        declencheurs.append("(iv) non comparable")
        out.update({"mention": NON_COMPARABLE, "declencheurs": declencheurs})
        return out
    m64 = out["ecart_max_abs_diffs_float64"]
    if m64 == 0.0:
        declencheurs.append("(ii) écart maximal exactement nul avec des octets différents")
    if m64 <= TOLERANCE:
        out["mention"] = PALIER_2
        if out["ecart_max_abs_diffs"] > DIFFS_PALIER_2:
            declencheurs.append("(vii) écart sur diffs au-delà de 10⁻³ au deuxième palier")
            out["mention"] = SUSPENDU
        if L == "R":
            s = out["series_export_R_sans_critere"]
            if (out["matrices_moities_egales"]["couches_egales"] == out["matrices_moities_egales"]["couches_ref"]
                    or any(v["ecart_max_abs"] == 0.0 for v in s.values())):
                declencheurs.append("(vi) trop propre au deuxième palier : 31 matrices égales ou série inchangée à zéro exact")
    else:
        declencheurs.append("(iii) lentille différente")
        out["mention"] = DIFFERENTE
    out["declencheurs"] = declencheurs
    return out


def sortie_arret_sur_erreur(erreur: BaseException, *, lentille=None, sha_ref=None, sha_neuf=None, pieces_lues=None,
                            commit_resultats=None, reprise: bool = False, etape: str = "") -> dict:
    """Sortie écrite quand le programme s'arrête sur une erreur (critère en vigueur, § 4) : « non comparable », ou « mention
    suspendue » si le résultat neuf porte l'empreinte du 18 ; le message d'erreur est versé ; un nœud de Lazar est à ouvrir."""
    bien_formee = isinstance(sha_neuf, str) and bool(_HEX64.match(sha_neuf))
    porte_le_18 = bien_formee and (sha_neuf == sha_ref or sha_neuf in EMPREINTES_FICHIERS_18.values())
    motif = f"{type(erreur).__name__} : {erreur}"
    if porte_le_18:
        mention, declencheur = SUSPENDU, f"(v) arrêt sur une erreur, le résultat neuf portant l'empreinte du 18 : {motif}"
    else:
        mention, declencheur = NON_COMPARABLE, f"(iv) non comparable : arrêt sur une erreur : {motif}"
    return {"programme": PROGRAMME, "critere": CRITERE, "arret_sur_erreur": True,
            "erreur": {"etape": etape, "type": type(erreur).__name__, "message": str(erreur),
                       "trace": "".join(traceback.format_exception(type(erreur), erreur, erreur.__traceback__))[-4000:]},
            "noeud_de_lazar": NOEUD_ARRET, "lentille": lentille, "tolerance": TOLERANCE, "reprise": bool(reprise),
            "preconditions": [], "preconditions_toutes_tenues": False, "pieces_lues": dict(_dico(pieces_lues)),
            "commit_resultats": commit_resultats, "sha256": {"ref": sha_ref, "neuf": sha_neuf},
            "mention": mention, "declencheurs": [declencheur]}


def comparer(c: dict, *, reprise: bool = False) -> dict:
    """Voir `preconditions` pour les clés de `c`. Rend la mention, les déclencheurs, les préalables et les tables. Ne lève jamais :
    une erreur inattendue rend la sortie d'arrêt sur une erreur. `audit_requis` est vrai dès qu'un déclencheur est rendu (§ 6)."""
    try:
        out = _comparer(_dico(c), reprise=reprise)
    except Exception as erreur:  # noqa: BLE001 — aucune exception ne sort sans sortie écrite (critère en vigueur, § 4)
        cc = _dico(c)
        out = sortie_arret_sur_erreur(erreur, lentille=cc.get("lentille"), sha_ref=_dico(cc.get("ref")).get("sha256"),
                                      sha_neuf=_dico(cc.get("neuf")).get("sha256"), pieces_lues=cc.get("sha_pieces"),
                                      commit_resultats=cc.get("commit_resultats"), reprise=reprise, etape="comparaison")
    out["audit_requis"] = bool(out["declencheurs"])
    return out


def charger(ref_ajustement: Path, neuf_ajustement: Path, ref_manifeste: Path, neuf_manifeste: Path, lanceur_ref: Path,
            lanceur_neuf: Path, ref_export: Path | None = None, neuf_export: Path | None = None, depot: Path | None = None,
            commit_resultats: str | None = None, chemin_lanceur_neuf: str | None = None, chemin_neuf_ajustement: str | None = None,
            chemin_neuf_manifeste: str | None = None, chemin_neuf_export: str | None = None) -> dict:
    """Lit les fichiers, calcule leurs empreintes et les rattache aux commits ; rend le dictionnaire `c` de `comparer`.
    Lève si un fichier est illisible ou n'est pas du JSON : `main` écrit alors la sortie d'arrêt sur une erreur."""
    def lire(p):
        b = Path(p).read_bytes()
        return json.loads(b.decode("utf-8")), b

    env_ref, o_ar = lire(ref_ajustement)
    env_neuf, o_an = lire(neuf_ajustement)
    mref, o_mr = lire(ref_manifeste)
    mneuf, o_mn = lire(neuf_manifeste)
    o_lr, o_ln = Path(lanceur_ref).read_bytes(), Path(lanceur_neuf).read_bytes()
    ref, neuf = _dico(env_ref).get("resultat"), _dico(env_neuf).get("resultat")
    lentille = _dico(_dico(ref).get("meta")).get("lens")
    fref, motif_r = empreinte_fonction_dans(o_lr)
    fneuf, motif_n = empreinte_fonction_dans(o_ln)
    c = {"ref": ref, "neuf": neuf, "env_ref": env_ref, "env_neuf": env_neuf, "mref": mref, "mneuf": mneuf, "lentille": lentille,
         "sha_pieces": {"ajustement_ref": empreinte_octets(o_ar), "ajustement_neuf": empreinte_octets(o_an),
                        "manifeste_ref": empreinte_octets(o_mr), "manifeste_neuf": empreinte_octets(o_mn),
                        "lanceur_ref": empreinte_octets(o_lr), "lanceur_neuf": empreinte_octets(o_ln)},
         "commit_resultats": commit_resultats, "env_eneuf": None, "correctifs_ref": None, "correctifs_neuf": None,
         "fref": fref, "fneuf": fneuf, "lecture_lanceurs": {"ref": motif_r, "neuf": motif_n}, "eref": None, "eneuf": None,
         "rattachement": {}}
    pieces_neuves = [("ajustement_neuf", neuf_ajustement, chemin_neuf_ajustement, o_an),
                     ("manifeste_neuf", neuf_manifeste, chemin_neuf_manifeste, o_mn)]
    if ref_export is not None:
        e, o_er = lire(ref_export)
        c["eref"], c["sha_pieces"]["export_ref"] = _dico(e).get("resultat"), empreinte_octets(o_er)
    if neuf_export is not None:
        e, o_en = lire(neuf_export)
        c["eneuf"], c["env_eneuf"], c["sha_pieces"]["export_neuf"] = _dico(e).get("resultat"), e, empreinte_octets(o_en)
        pieces_neuves.append(("export_neuf", neuf_export, chemin_neuf_export, o_en))
    if depot is not None:
        commit_r, commit_n = _dico(mref).get("commit"), _dico(mneuf).get("commit")
        c["correctifs_ref"] = empreintes_correctifs(depot, commit_r, _dico(_dico(mref).get("config")).get("correctifs"))
        c["correctifs_neuf"] = empreintes_correctifs(depot, commit_n, _dico(_dico(mneuf).get("config")).get("correctifs"))
        ratt = c["rattachement"]
        ok, detail = commit_lisible(depot, commit_resultats)
        ratt["commit_resultats"] = {"tenu": ok, "commit": commit_resultats, "detail": detail}
        for nom, fichier, chemin_donne, octets in pieces_neuves:                       # K1
            chemin, origine = chemin_dans_depot(depot, fichier, chemin_donne)
            ratt[nom] = dict(rattacher(depot, commit_resultats, chemin, octets), origine_du_chemin=origine)
        for cote, commit in (("ref", commit_r), ("neuf", commit_n)):                   # K2
            ok, detail = commit_lisible(depot, commit)
            ratt[f"commit_manifeste_{cote}"] = {"tenu": ok, "commit": commit, "detail": detail}
        ratt["lanceur_neuf"] = dict(rattacher(depot, commit_n, chemin_lanceur_neuf, o_ln), origine_du_chemin="donné en argument")
    return c


def _lecture_de_secours(x) -> dict:
    """Après un arrêt de `charger` : empreinte de chaque fichier donné s'il est lisible, et, sans rien supposer de leur forme,
    l'empreinte que portent le résultat neuf et le résultat de référence, et la lentille."""
    pieces = {}
    for nom, chemin in (("ajustement_ref", x.ref_ajustement), ("ajustement_neuf", x.neuf_ajustement), ("manifeste_ref", x.ref_manifeste),
                        ("manifeste_neuf", x.neuf_manifeste), ("lanceur_ref", x.lanceur_ref), ("lanceur_neuf", x.lanceur_neuf),
                        ("export_ref", x.ref_export), ("export_neuf", x.neuf_export)):
        if chemin is None:
            continue
        try:
            pieces[nom] = empreinte_octets(Path(chemin).read_bytes())
        except OSError as e:
            pieces[nom] = f"illisible : {type(e).__name__} : {e}"

    def resultat(chemin) -> dict:
        try:
            return _dico(_dico(json.loads(Path(chemin).read_bytes().decode("utf-8"))).get("resultat"))
        except (OSError, ValueError):
            return {}

    r, n = resultat(x.ref_ajustement), resultat(x.neuf_ajustement)
    return {"pieces_lues": pieces, "sha_ref": r.get("sha256"), "sha_neuf": n.get("sha256"), "lentille": _dico(r.get("meta")).get("lens")}


def main(argv=None):
    a = argparse.ArgumentParser(description=f"Comparaison d'une lentille réajustée à celle du 18 novembre ({CRITERE})")
    for n in ("ref-ajustement", "neuf-ajustement", "ref-manifeste", "neuf-manifeste", "lanceur-ref", "lanceur-neuf", "sortie"):
        a.add_argument(f"--{n}", required=True, type=Path)
    a.add_argument("--ref-export", type=Path)
    a.add_argument("--neuf-export", type=Path)
    a.add_argument("--reprise", action="store_true", help="reprise sur sauvegarde lue au journal de la course (K4, à la main)")
    a.add_argument("--depot", type=Path, required=True,
                   help="dépôt git de travail : correctifs aux deux commits des manifestes, pièces neuves au commit des résultats (K1), "
                        "lanceur neuf au commit du manifeste neuf (K2)")
    a.add_argument("--commit-resultats", required=True,
                   help="identifiant entier du commit de la branche de résultats poussée par la machine (K1)")
    a.add_argument("--chemin-lanceur-neuf", required=True,
                   help="chemin du lanceur neuf dans le dépôt, depuis sa racine (K2 : lu au commit du manifeste neuf)")
    for n, quoi in (("ajustement", "du résultat d'ajustement neuf"), ("manifeste", "du manifeste neuf"), ("export", "de l'export neuf")):
        a.add_argument(f"--chemin-neuf-{n}",
                       help=f"chemin {quoi} dans le dépôt, depuis sa racine (K1) ; à défaut, déduit de la place du fichier sous le dépôt")
    x = a.parse_args(argv)
    if x.sortie.exists():
        sys.exit(f"{x.sortie} existe déjà : on n'écrase jamais (R12)")
    try:
        c = charger(x.ref_ajustement, x.neuf_ajustement, x.ref_manifeste, x.neuf_manifeste, x.lanceur_ref, x.lanceur_neuf,
                    x.ref_export, x.neuf_export, x.depot, x.commit_resultats, x.chemin_lanceur_neuf, x.chemin_neuf_ajustement,
                    x.chemin_neuf_manifeste, x.chemin_neuf_export)
    except Exception as erreur:  # noqa: BLE001 — pièce illisible ou toute exception : sortie écrite, jamais d'arrêt muet
        r = sortie_arret_sur_erreur(erreur, commit_resultats=x.commit_resultats, reprise=x.reprise, etape="lecture des pièces",
                                    **_lecture_de_secours(x))
        r["audit_requis"] = True
    else:
        r = comparer(c, reprise=x.reprise)
    r["ligne_de_commande"] = sys.argv if argv is None else [PROGRAMME, *argv]
    with open(x.sortie, "x", encoding="utf-8") as f:      # création exclusive : on n'écrase jamais (R12)
        f.write(json.dumps(r, ensure_ascii=False, indent=1) + "\n")
    print(f"{r['lentille']} : {r['mention']} ; déclencheurs : {r['declencheurs']}")
    if r["arret_sur_erreur"]:
        print(f"arrêt sur une erreur : {r['erreur']['type']} : {r['erreur']['message']} — sortie écrite dans {x.sortie}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
