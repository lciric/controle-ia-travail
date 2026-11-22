"""Contrôles de la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale, Llama 3.1 8B Instruct) — v1.

Met en œuvre, sans rien y changer, les gardes de la « Chaîne en défaut » du texte gelé scellé
`docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` (`f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454`)
qui se constatent **sur la machine** (lettres (d) à (s), sauf (a) à (c), (j) et (l), jugées par le code des verdicts sur la sortie de
`score`), le contenu des audits A2, A3 et A4, le recalcul non arrondi des différences entre moitiés (B-1), les contrôles de P.1 (932
documents, moitiés 466 et 466, empreinte des lignes), la règle du banc, les intervalles par rééchantillonnage des pôles (M.2) et
l'assemblage des entrées du code des verdicts (`verdicts_b_beta_v4`). Valeurs exigées : texte gelé et addendum partie 1
(`addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md`, `bd8067dc…`).

**Fonctions pures** (numpy ; aucun modèle, aucun réseau, aucun code du dépôt voisin) : chaque garde rend la liste des problèmes
constatés (vide = garde tenue). Le lanceur (`b_beta_lancer_v1`) lit les fichiers sur la machine, appelle ces fonctions, et convertit
« liste non vide » en booléen strict par `bool()` pour le code des verdicts. Rien ici ne lit un résultat : ces fonctions sont
essayées dans le conteneur sur des cas sains et des artefacts (`tests/test_neuron_lens_controles_b_beta_v1.py`), comme le veut R5.
"""
from __future__ import annotations

import hashlib
import math

import numpy as np

# ---------------------------------------------------------------- valeurs exigées (texte gelé, P.0, P.1 ; addendum partie 1, §§ 2, 3, 5)

MODELE = "meta-llama/Llama-3.1-8B-Instruct"
STEM = "llama-3.1-8b-instruct"
N_COUCHES = 32
F_LLAMA = 14336
D_MODEL = 4096
N_DOCS = 932
MOITIES = (466, 466)
SEQ_LEN = 128
ROWS_SHA256 = "a6afd972eeaa3566a28d07216efaf75624fda20293c5fab3b7af39277aaf93b3"
ROWS_SHA256_MOITIES = ("4a31baecbac5481f71c22912f2a02927bea2877f2be6d82d58185d36c1b95e32",
                       "ef95a60c96032cdc9ea42a957eb4d0f10006d4d11fb751515f3c343eb435c3f9")
REVISION_DCLM = "2fa015e4044ec442a0734e89658cdcc538d10dd4"
REPO_DCLM = "HuggingFaceFW/dclm_100BT-shuffled"
PROVENANCE_AJUSTEMENT_PUBLIEE = "16957c528c2f7765afe01b37318aae5365535f29dffdde8c5ce5c48ed1c2e77a"
PROVENANCE_ACT_DCLM_PUBLIEE = "a26a70773b35e87349107dac27dddf4f134411c2fd28e5fe5e92cc980e4798e5"
ACT_DCLM_SKIP, ACT_DCLM_N = 1000, 40000
KEPT_N, KEPT_SHA256 = 89498, "c37186add16770aa3c04bd0c16c417544b7e2a15b374ee85e47fbda7ec148d68"
CORPUS_ACT_SHA256 = {"act-dclm.jsonl": "64657ecbb54f7899db33564c502f3bb8f01c6d13348855584e7db1894d893ba4",
                     "act-zh.jsonl": "c3202db1eab8938984f8bea6b49c229610d2eb89ecee6148c8b5ad6942fd4f5b",
                     "act-code.jsonl": "550944a25182286079c581882bb1c5f3bb1ffce153af711506d0e388d01959e6",
                     f"act-chat-{STEM}.jsonl": "9dbf9f44cdbf1a218181c886002905885b4b5d941dcdeb4a4cbfa0ffa5e8d828"}
DROWSE_VERSION, DROWSE_SHA256 = "6.1.4", "673ed2b4de653ad2ec22660b0191031ee2c7b4bacaf4cc2ea552f0436b9d8e03"
VERSIONS = {"python": "3.12.16", "torch": "2.14.1", "transformers": "5.18.0", "tokenizers": "0.23.2", "huggingface_hub": "1.33.0",
            "datasets": "5.2.0", "numpy": "2.4.6", "pyarrow": "26.0.1", "safetensors": "0.8.0", "drowse.ai": DROWSE_VERSION}
FIT_NOMS = {"R": f"r-{STEM}-L32-dclm-T128.pt", "S": f"s-{STEM}-L32-dclm-T128.pt"}  # `02_fit.py --full-length`, l. 56-57
FIT_NOMS_ARCH = {"R": f"r-{STEM}-L32-dclm.pt", "S": f"s-{STEM}-L32-dclm.pt"}  # ce que cherche `arch.fits` (l. 299-303)
COUCHES_FIT = {("R", "out"): 31, ("R", "mid"): 32, ("S", "mid"): 32, ("S", "out"): 32}  # `target_layers` ; garde (h)
TOL_IDENTITE = 1e-6  # garde (e) et (n), float32
TOL_ALLER_RETOUR = 1e-3  # garde (o), écart relatif de Frobenius
BANC_PART, BANC_ARRET = 14.2, 23.6  # s par document, second document (devis v12, § 5 ; texte gelé, P.3 étape 1)
PILOTES_PAR_TRANCHE = {"dclm": 4, "code": 2, "chat": 2}  # `07_drivers.py`, l. 46 ; garde (p)
CONTEXTES_MEASURE = 16  # garde (p)
POINTS_FIXES_MAX = 10  # audit A4
N_TIRAGES = 2000  # M.2, intervalles
ENTROPIE = 20261118  # P.5 : `SeedSequence(entropy=20261118)`, branche « B-β »
TACHES_INTERVALLES = ("b-beta-intervalles-B-2", "b-beta-intervalles-B-3", "b-beta-intervalles-B-4", "b-beta-intervalles-B-6",
                      "b-beta-intervalles-B-7")  # ordre de P.5


def sha256_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def rows_sha256(rows) -> str:
    """Recopie de `neuron_lens.corpus.rows_sha256` (l. 63-65 du dépôt voisin) : empreinte « token_ids_v1 » de Drowse. Sert aux essais ;
    sur la machine, la fonction du dépôt voisin elle-même est appelée (P.1), et les deux doivent concorder."""
    return hashlib.sha256(repr([list(r) for r in rows]).encode("utf-8")).hexdigest()


# ---------------------------------------------------------------- P.1 : corpus d'ajustement recompté sur la machine (avant l'ajustement)

def controle_p1(rows) -> tuple[dict, list[str]]:
    """`rows` : ce que `lens_docs(dclm.jsonl, tok, 1000, 128, 18, full=True)` rend sur la machine. Rend (relevé, problèmes)."""
    rows = [list(r) for r in rows]
    paire, impaire = rows[0::2], rows[1::2]
    rel = {"docs": len(rows), "moities": [len(paire), len(impaire)], "longueurs": sorted({len(r) for r in rows}),
           "rows_sha256": rows_sha256(rows), "rows_sha256_moities": [rows_sha256(paire), rows_sha256(impaire)]}
    pb = []
    if rel["docs"] != N_DOCS:
        pb.append(f"P.1 : {rel['docs']} documents au lieu de {N_DOCS}")
    if tuple(rel["moities"]) != MOITIES:
        pb.append(f"P.1 : moitiés {rel['moities']} au lieu de {list(MOITIES)}")
    if rel["longueurs"] != [SEQ_LEN]:
        pb.append(f"P.1 : longueurs {rel['longueurs'][:5]} au lieu de [{SEQ_LEN}]")
    if rel["rows_sha256"] != ROWS_SHA256:
        pb.append(f"P.1 : rows_sha256 {rel['rows_sha256'][:12]}… au lieu de {ROWS_SHA256[:12]}…")
    if tuple(rel["rows_sha256_moities"]) != ROWS_SHA256_MOITIES:
        pb.append("P.1 : empreintes des moitiés différentes de celles comptées avant scellement")
    return rel, pb


# ---------------------------------------------------------------- banc (P.3, étape 1)

def regle_banc(secondes_second_document: float) -> str:
    """« part » (≤ 14,2 s), « compte_rendu » (au-delà de 14,2 s, part), « arret » (au-delà de 23,6 s, ou valeur illisible)."""
    s = secondes_second_document
    if not (isinstance(s, (int, float)) and not isinstance(s, bool) and math.isfinite(s) and s > 0):
        return "arret"
    if s > BANC_ARRET:
        return "arret"
    if s > BANC_PART:
        return "compte_rendu"
    return "part"


# ---------------------------------------------------------------- garde (d) : essais

def garde_d(essais: dict) -> list[str]:
    """`essais[nom] = {"code": int, "resume": dernière ligne de bilan de pytest}`. Défaut : code non nul, aucun « passed », ou un test
    « skipped », « failed », « error » (texte gelé, (d) : « un test sauté ou en échec »). Le nom « fumee » porte la fumée de la passe
    (code seul)."""
    import re
    pb = []
    if not essais:
        return ["(d) aucun essai relevé"]
    for nom, x in essais.items():
        if nom == "fumee":
            if x.get("code") != 0:
                pb.append(f"(d) fumée de la passe en échec (code {x.get('code')})")
            continue
        r = str(x.get("resume", ""))
        if x.get("code") != 0 or "passed" not in r or re.search(r"\b(failed|error|errors|skipped|deselected|xfail|xpass)", r):
            pb.append(f"(d) essai {nom} : code {x.get('code')}, « {r[:120]} »")
    return pb


# ---------------------------------------------------------------- garde (e) : matrice égale à l'identité ; garde (n) : égale à npR

def ecart_max(a, b) -> float:
    a, b = np.asarray(a, np.float32), np.asarray(b, np.float32)
    if a.shape != b.shape:
        return math.inf
    return float(np.max(np.abs(a - b))) if a.size else math.inf


def garde_e_matrices(lentille: dict, nom: str, couches=range(28)) -> list[str]:
    """Une matrice égale à l'identité (écart maximal ≤ 10⁻⁶ en float32) à une couche de 0 à 27, ou une couche absente."""
    pb = []
    for l in couches:
        m = lentille.get(l)
        if m is None:
            pb.append(f"(e) {nom} : couche {l} absente")
            continue
        m = np.asarray(m, np.float32)
        if m.ndim != 2 or m.shape[0] != m.shape[1]:
            pb.append(f"(e) {nom} : couche {l} de forme {m.shape}")
            continue
        if ecart_max(m, np.eye(m.shape[0], dtype=np.float32)) <= TOL_IDENTITE:
            pb.append(f"(e) {nom} : matrice de la couche {l} égale à l'identité")
    return pb


def garde_n(notre: dict, npr: dict, sha_notre: str, sha_npr: str) -> list[str]:
    """Notre R confondue avec la lentille R publique : une matrice égale (≤ 10⁻⁶) à une couche de 0 à 27, ou des fichiers d'empreinte
    égale."""
    pb = []
    if sha_notre == sha_npr:
        pb.append("(n) fichier de notre R d'empreinte égale à celle de la lentille R publique")
    for l in range(28):
        if l in notre and l in npr and notre[l] is not None and npr[l] is not None and ecart_max(notre[l], npr[l]) <= TOL_IDENTITE:
            pb.append(f"(n) matrice de notre R égale à celle de la lentille R publique, couche {l}")
    return pb


# ---------------------------------------------------------------- garde (g) : ajustement incomplet, vide ou non fini ; B-1 non arrondie

def split_half(somme_paire, somme_impaire, n0: int, n1: int) -> list[float]:
    """Recopie de `Accumulator.split_half` (`neuron_lens/transport.py`, l. 64-72) : par couche, ‖moy. paire − moy. impaire‖ / ‖moy.‖,
    sur les sommes du fichier d'ajustement (float32, comme le dépôt), **non arrondie**. `nan` si une moitié est vide (garde (g))."""
    a, b = np.asarray(somme_paire, np.float32), np.asarray(somme_impaire, np.float32)
    if a.shape != b.shape or a.ndim != 3:
        raise ValueError(f"sommes de formes {a.shape} et {b.shape}")
    if not (n0 and n1):
        return [float("nan")] * a.shape[0]
    out = []
    for l in range(a.shape[0]):
        num = np.linalg.norm((a[l] / np.float32(n0) - b[l] / np.float32(n1)).ravel())
        den = np.linalg.norm(((a[l] + b[l]) / np.float32(n0 + n1)).ravel())
        out.append(float(num / den) if den > 0 else float("nan"))
    return out


def garde_g_fit(meta: dict, next_doc, n_docs, longueurs, diffs: dict, matrices_finies: bool, lentille: str) -> list[str]:
    """Fin d'un ajustement (`lentille` « R » ou « S ») : documents par moitié 466 et 466 ; `next_doc` = `meta["docs"]` ; longueurs toutes
    de 128 ; `rows_sha256` attendu ; `full_length` vrai ; différences entre moitiés finies ; sommes finies (matrices de la lentille)."""
    pb = []
    if meta.get("lens") != lentille:
        pb.append(f"(g) fichier d'ajustement de la lentille {meta.get('lens')!r}, attendu {lentille!r}")
    if list(n_docs) != list(MOITIES):
        pb.append(f"(g) {lentille} : documents par moitié {list(n_docs)} au lieu de {list(MOITIES)}")
    if meta.get("docs") != N_DOCS or next_doc != meta.get("docs"):
        pb.append(f"(g) {lentille} : next_doc {next_doc} ≠ docs {meta.get('docs')} (attendu {N_DOCS})")
    if sorted(set(longueurs)) != [SEQ_LEN]:
        pb.append(f"(g) {lentille} : longueurs de documents {sorted(set(longueurs))[:5]} au lieu de [{SEQ_LEN}]")
    if meta.get("rows_sha256") != ROWS_SHA256:
        pb.append(f"(g) {lentille} : rows_sha256 {str(meta.get('rows_sha256'))[:12]}… au lieu de {ROWS_SHA256[:12]}…")
    if meta.get("full_length") is not True:
        pb.append(f"(g) {lentille} : full_length {meta.get('full_length')!r}")
    for cible, v in diffs.items():
        if any(not math.isfinite(x) for x in v):
            pb.append(f"(g) {lentille}, {cible} : différence entre moitiés non finie")
    if not matrices_finies:
        pb.append(f"(g) {lentille} : somme ou matrice non finie")
    return pb


def longueurs_point(meta: dict, rows) -> list[int]:
    """Longueurs des documents que l'ajustement a pris (les `next_doc` premiers de `lens_docs`)."""
    return [len(r) for r in list(rows)[: int(meta.get("docs", 0))]]


def garde_h(premiere_dim: dict, lentille: str) -> list[str]:
    """`premiere_dim[cible]` : première dimension des sommes du fichier d'ajustement (ou nombre de couches exportées pour R)."""
    pb = []
    for (le, ci), n in COUCHES_FIT.items():
        if le != lentille:
            continue
        if premiere_dim.get(ci) != n:
            pb.append(f"(h) {lentille}, cible {ci} : {premiere_dim.get(ci)} couches au lieu de {n}")
    return pb


def garde_h_export(couches_out) -> list[str]:
    """Notre R exportée : couches 0 à 30 exactement pour la cible `out` (ce que rend `load_lens`)."""
    c = sorted(couches_out)
    return [] if c == list(range(31)) else [f"(h) notre R exportée : couches {c[:3]}…{c[-3:] if c else []} ({len(c)}) au lieu de 0 à 30"]


# ---------------------------------------------------------------- garde (i) : corpus partagé

def garde_i(prov_ajustement: dict, prov_act: dict | None, publiee_ajustement: dict, publiee_act: dict,
            textes_ajustement: list[str] | None = None, textes_act: list[str] | None = None) -> list[str]:
    """Provenances écrites sur la machine contre les publiées (révision, identifiants dans l'ordre, lignes ou `skip`/`n`) ; aucun
    identifiant commun ; aucun texte entier commun (empreintes SHA-256 des champs `text`). `prov_act` vaut `None` avant `05` : la
    provenance d'ajustement est alors comparée à la publiée des activations (identifiants communs)."""
    pb = []
    for k in ("repo", "revision", "ids", "rows"):
        if prov_ajustement.get(k) != publiee_ajustement.get(k):
            pb.append(f"(i) provenance d'ajustement : {k} différent de la provenance publiée")
    if prov_ajustement.get("revision") != REVISION_DCLM:
        pb.append("(i) provenance d'ajustement : révision autre que la révision épinglée")
    act = prov_act if prov_act is not None else publiee_act
    if prov_act is not None:
        for k in ("repo", "config", "split", "revision", "skip", "n", "ids"):
            if prov_act.get(k) != publiee_act.get(k):
                pb.append(f"(i) provenance des activations : {k} différent de la provenance publiée")
    if act.get("skip") != ACT_DCLM_SKIP or act.get("n") != ACT_DCLM_N:
        pb.append(f"(i) provenance des activations : skip {act.get('skip')}, n {act.get('n')}")
    communs = set(prov_ajustement.get("ids", [])) & set(act.get("ids", []))
    if communs:
        pb.append(f"(i) {len(communs)} identifiant(s) commun(s) aux deux corpus")
    if textes_ajustement is not None and textes_act is not None:
        ta = {sha256_octets(t.encode("utf-8")) for t in textes_ajustement}
        tb = {sha256_octets(t.encode("utf-8")) for t in textes_act}
        if ta & tb:
            pb.append(f"(i) {len(ta & tb)} texte(s) entier(s) commun(s) aux deux corpus")
    return pb


# ---------------------------------------------------------------- garde (k) : noms vus par `arch.fits`

def garde_k(rendu, moment: str, liens: dict | None = None, empreintes_fit: dict | None = None) -> list[str]:
    """`rendu` : ce que `arch.fits(MODEL)` rend juste avant l'étape. Avant la fumée, la passe et les pilotes (`moment` « hub ») :
    (`hub`, `hub`) exigé. Avant `reads_at_firings.py` (`moment` « noms ») : nos deux noms, et chaque fichier à ces noms d'empreinte
    égale à celle consignée à la fin de l'ajustement (`liens[lentille]` et `empreintes_fit[lentille]`)."""
    rendu = tuple(rendu) if rendu is not None else None
    if moment == "hub":
        return [] if rendu == ("hub", "hub") else [f"(k) arch.fits rend {rendu}, attendu ('hub', 'hub')"]
    if moment != "noms":
        raise ValueError(f"moment inconnu : {moment}")
    attendu = tuple(n.removesuffix(".pt") for n in (FIT_NOMS_ARCH["R"], FIT_NOMS_ARCH["S"]))
    pb = [] if rendu == attendu else [f"(k) arch.fits rend {rendu}, attendu {attendu}"]
    liens, empreintes_fit = liens or {}, empreintes_fit or {}
    for le in ("R", "S"):
        if le not in liens or le not in empreintes_fit or liens[le] != empreintes_fit[le]:
            pb.append(f"(k) fichier {FIT_NOMS_ARCH[le]} d'empreinte différente de celle consignée à la fin de l'ajustement")
    return pb


MOTIF_HUB = f"no released R-lens for {MODELE}: heads/acts without out_R_z"  # correctif (1), `06_activations-llama-v2.diff`, l. 42


def message_hub_present(journal: str) -> bool:
    """Preuve complémentaire de (k) : le message que le correctif (1) imprime quand la passe prend la branche `hub` (texte du
    correctif scellé, l. 42 du diff), relevé dans le journal de la passe."""
    return MOTIF_HUB in journal


# ---------------------------------------------------------------- garde (o) : aller-retour de l'export

def garde_o(charge: dict | None, moyennes: dict, nom: str, erreur: str | None = None) -> list[str]:
    """`charge` : matrices par couche rendues par `load_lens(nom)` (ou `None` si l'appel a levé, `erreur` = message) ; `moyennes` :
    moyennes du fichier d'ajustement (cible `out`, entière ou moitié) par couche 0 à 30."""
    if erreur is not None or charge is None:
        return [f"(o) load_lens({nom!r}) a levé : {str(erreur)[:200]}"]
    pb = []
    for l in range(31):
        m = charge.get(l)
        if m is None:
            pb.append(f"(o) {nom} : None à la couche {l}")
            continue
        a, b = np.asarray(m, np.float64), np.asarray(moyennes[l], np.float64)
        if a.shape != b.shape:
            pb.append(f"(o) {nom} : forme {a.shape} ≠ {b.shape} à la couche {l}")
            continue
        nb = np.linalg.norm(b.ravel())
        rel = np.linalg.norm((a - b).ravel()) / nb if nb > 0 else math.inf
        if not (rel <= TOL_ALLER_RETOUR):
            pb.append(f"(o) {nom} : écart relatif {rel:.2e} à la couche {l}")
    return pb


# ---------------------------------------------------------------- garde (p) : moins de documents que demandé

def garde_p_measure(meta: dict) -> list[str]:
    return [] if meta.get("contexts") == CONTEXTES_MEASURE else [f"(p) measure : {meta.get('contexts')} contextes au lieu de 16"]


def garde_p_pilotes(comptes: dict) -> list[str]:
    """`comptes[tranche]` : documents que `07_drivers.documents` prendra (recomptés par `lens_docs` avant l'étape)."""
    return [f"(p) 07_drivers : {comptes.get(t)} document(s) de la tranche {t} au lieu de {k}"
            for t, k in PILOTES_PAR_TRANCHE.items() if comptes.get(t) != k]


# ---------------------------------------------------------------- garde (q) : reprise et banc

def garde_q_avant(fits_presents: list[str]) -> list[str]:
    """Avant le premier lancement d'un ajustement : aucun fichier `-T128` dans l'arbre de la course."""
    return [f"(q) {f} présent avant le premier lancement" for f in fits_presents]


def garde_q_relance(meta: dict, lentille: str) -> list[str]:
    """Avant toute relance : le point de sauvegarde porte `rows_sha256` attendu, `full_length` vrai, la lentille et le modèle."""
    pb = []
    if meta.get("rows_sha256") != ROWS_SHA256:
        pb.append("(q) point de sauvegarde : rows_sha256 différent")
    if meta.get("full_length") is not True:
        pb.append("(q) point de sauvegarde : full_length non vrai")
    if meta.get("lens") != lentille or meta.get("model") != MODELE:
        pb.append(f"(q) point de sauvegarde : lentille {meta.get('lens')!r}, modèle {meta.get('model')!r}")
    return pb


# ---------------------------------------------------------------- garde (r) : jetons gardés ; garde (s) : fichiers antérieurs

def empreinte_liste_gardee(ids) -> str:
    """Même forme que `controles_b0_v2.empreinte_liste_gardee` (identifiants triés, un par ligne, ASCII)."""
    ids = sorted(int(i) for i in ids)
    if len(set(ids)) != len(ids):
        raise ValueError("doublon dans la liste gardée")
    return hashlib.sha256("".join(f"{i}\n" for i in ids).encode("ascii")).hexdigest()


def garde_r(courante: str, consignee: str, etape: str) -> list[str]:
    return [] if courante == consignee else [f"(r) jetons gardés d'empreinte différente avant {etape}"]


def garde_s(presents: list[str]) -> list[str]:
    return [f"(s) fichier antérieur présent avant reads_at_firings.py : {p}" for p in presents]


# ---------------------------------------------------------------- audits A2, A3 (moitiés distinctes), A4 (permutation)

def controles_a2_a3(n_docs: dict, empreintes_moities: list[str], ecarts_sommes: dict, empreintes_exports: dict,
                    longueurs=None, full_length=None, avec_a3: bool = False) -> tuple[bool, list[str]]:
    """A2 : comptes 466 et 466 (deux lentilles) ; empreintes des lignes des moitiés ; sommes des moitiés différentes (écart maximal > 0,
    chaque cible) ; exports des moitiés d'empreintes différentes. A3 : les mêmes, plus documents tous de 128 jetons et `full_length`
    vrai. Rend (contrôles tenus, problèmes)."""
    pb = []
    for le, n in n_docs.items():
        if list(n) != list(MOITIES):
            pb.append(f"{le} : comptes {list(n)}")
    if tuple(empreintes_moities) != ROWS_SHA256_MOITIES:
        pb.append("empreintes des lignes des moitiés différentes")
    for cle, e in ecarts_sommes.items():
        if not (isinstance(e, float) and math.isfinite(e) and e > 0):
            pb.append(f"sommes des moitiés égales ou illisibles : {cle}")
    if len(set(empreintes_exports.values())) != 2 or len(empreintes_exports) != 2:
        pb.append("exports des moitiés d'empreintes égales ou absents")
    if avec_a3:
        if longueurs is None or sorted(set(longueurs)) != [SEQ_LEN]:
            pb.append("documents de longueur autre que 128")
        if full_length is not True:
            pb.append("full_length non vrai")
    return (not pb), pb


def points_fixes_permutation(f: int = F_LLAMA, couches: int = N_COUCHES) -> list[int]:
    """Points fixes, par couche, de la permutation des paires mal appariées de `reads_at_firings.py` (l. 133, 149) : un générateur à la
    graine 0, puis à chaque couche `cat([randperm(f), f + randperm(f)])`. Recalcul exact (torch, processeur), sans le code voisin."""
    import torch
    g = torch.Generator().manual_seed(0)
    out = []
    for _ in range(couches):
        perm = torch.cat([torch.randperm(f, generator=g), f + torch.randperm(f, generator=g)])
        out.append(int((perm == torch.arange(2 * f)).sum()))
    return out


def controle_a4(points_fixes: list[int], sha_s_lu: str, sha_s_ajuste: str) -> dict:
    """Rend `{"permutation_ok": bool, "lentille_S_ok": bool}` pour le code des verdicts (booléens stricts)."""
    return {"permutation_ok": bool(len(points_fixes) == N_COUCHES and max(points_fixes) <= POINTS_FIXES_MAX),
            "lentille_S_ok": bool(sha_s_lu == sha_s_ajuste)}


# ---------------------------------------------------------------- intervalles (M.2) : rééchantillonnage des pôles

def _r_poles(poles: list[dict], cible: str, lentille: str, couche: int) -> dict:
    """{indice du pôle : r} des pôles tirés au hasard et retenus pour (cible, lentille), à une couche."""
    out = {}
    for i, p in enumerate(poles):
        if p["couche"] == couche and p["aleatoire"]:
            x = p["lectures"][cible][lentille]
            if x["motif"] == "retenu":
                out[i] = x["r"]
    return out


def intervalles(poles: list[dict], generateurs: dict, n_tirages: int = N_TIRAGES) -> dict:
    """Intervalles à 95 % par couche, rapportés sans critère (M.2 ; verdicts sur les valeurs ponctuelles). Rééchantillonnage des pôles
    retenus, apparié pour une différence (mêmes pôles tirés pour les deux lentilles). `generateurs[tache]` : un générateur numpy par
    tâche de `TACHES_INTERVALLES` (graines du manifeste, P.5). Mesures : B-2 `r_med` de notre R (« steer 1x ») ; B-3 notre R − logits ;
    B-4 notre R − J et notre R − J++ ; B-6 notre R − R publique ; B-7 `r_med` de notre R (« ablate win »)."""
    plan = {"b-beta-intervalles-B-2": [("steer 1x", "R:dclm-llama", None)],
            "b-beta-intervalles-B-3": [("steer 1x", "R:dclm-llama", "logit")],
            "b-beta-intervalles-B-4": [("steer 1x", "R:dclm-llama", "J"), ("steer 1x", "R:dclm-llama", "npJpp")],
            "b-beta-intervalles-B-6": [("steer 1x", "R:dclm-llama", "npR")],
            "b-beta-intervalles-B-7": [("ablate win", "R:dclm-llama", None)]}
    out = {"n_tirages": n_tirages}
    for tache in TACHES_INTERVALLES:
        rng = generateurs[tache]
        res = {}
        for cible, a, b in plan[tache]:
            cle = f"{cible}|{a}" + (f"−{b}" if b else "")
            par_couche = []
            for l in range(N_COUCHES):
                ra = _r_poles(poles, cible, a, l)
                if b is not None:
                    rb = _r_poles(poles, cible, b, l)
                    idx = sorted(set(ra) & set(rb))
                    va, vb = np.array([ra[i] for i in idx]), np.array([rb[i] for i in idx])
                else:
                    idx = sorted(ra)
                    va, vb = np.array([ra[i] for i in idx]), None
                if len(idx) == 0:
                    par_couche.append(None)
                    continue
                t = rng.integers(0, len(idx), size=(n_tirages, len(idx)))
                stat = np.median(va[t], axis=1) - (np.median(vb[t], axis=1) if vb is not None else 0.0)
                par_couche.append([round(float(x), 4) for x in np.quantile(stat, [0.025, 0.975])])
            res[cle] = par_couche
        out[tache] = res
    return out


# ---------------------------------------------------------------- assemblage des entrées du code des verdicts

GARDES_MACHINE = ("d", "f", "g", "h", "i", "k", "n", "o", "p", "q", "r", "s")


def gardes_booleennes(problemes: dict) -> dict:
    """`problemes[lettre]` : liste des problèmes constatés pour la garde (vide = tenue), y compris « identite » (garde (e), matrices).
    Rend `{lettre: bool}` strict (`bool()`), exigé par le code des verdicts ; une lettre absente est un refus (aucun repli)."""
    manquantes = [g for g in GARDES_MACHINE + ("identite",) if g not in problemes]
    if manquantes:
        raise ValueError(f"gardes non constatées : {manquantes}")
    return {g: bool(problemes[g]) for g in GARDES_MACHINE + ("identite",)}


def reads_depuis_sortie(sortie: dict) -> tuple[list, list]:
    """`read_S` et `silent` par couche, tels qu'écrits par `reads_at_firings.py` (flottants complets, l. 289-291), 32 couches."""
    couches = sortie["neurons"]["layers"]
    if [c["layer"] for c in couches] != list(range(N_COUCHES)):
        raise ValueError("reads_at_firings : couches manquantes ou désordonnées")
    return [c["read_S"] for c in couches], [c["silent"] for c in couches]


def accord_depuis_lens_compare(sortie: dict) -> dict:
    """Accord du premier jeton entre les moitiés paire et impaire de notre R, aux six couches, non arrondi (correctif (4))."""
    out = {}
    for l in (2, 7, 12, 18, 23, 28):
        paire = sortie["layers"][str(l)]
        cle = "R:dclm-llama-even vs R:dclm-llama-odd"
        if cle not in paire:
            raise ValueError(f"lens_compare : paire des moitiés absente à la couche {l}")
        out[l] = float(paire[cle]["top1_agree"])
    return out
