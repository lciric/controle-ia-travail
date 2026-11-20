"""Jouets des essais de la lecture des sondes de l'étape B bis par la lentille publique : registres, fichiers des sondes aux
formes (a), (b), (c), Llama miniature construit localement, fausse lentille, faux code voisin, réseau simulé.

Aucune donnée du programme : tout est tiré par graine. Les empreintes des sondes jouets sont calculées par le code de
`controle_ia.sondes.familles` (celui de l'apprentissage des sondes), non par le code éprouvé.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import torch

from controle_ia.lentilles_sondes_bbis import constantes_v1 as K
from controle_ia.lentilles_sondes_bbis import lanceur_v1 as la
from controle_ia.lentilles_sondes_bbis import montage_v1 as mo
from controle_ia.sondes import familles as fam

RACINE = Path(__file__).resolve().parents[1]
RUN_BBIS = "20261117-000000-jouet-bbis"
RUN = "20261119-000000-jouet-lentilles"
LARGEUR, VOCABULAIRE, NEURONES = 32, 384, 64
HEURE = "2026-11-19T00:00:00Z"
FAUSSE_CLE = "hf_FAUSSECLEdEssaiQuiNeDoitParaitreNullePart0123456789"
DEPOT_ZH, DEPOT_CODE, DEPOT_DCLM, DEPOT_CHAT = "jouet/zh", "jouet/code", "jouet/dclm", "jouet/chat"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def compagnon(p: Path) -> None:
    Path(str(p) + ".sha256").write_text(f"{sha(p.read_bytes())}  {p.name}\n", encoding="utf-8")


# --- registres -------------------------------------------------------------------------------------------------------------------------
def ecrire_registres(dossier: Path, sha_e2: str = "0" * 64, verdict: bool = True, scores: int = 1,
                     propres=("ABSENCE-VERDICT-LENTILLES-BBIS", "SCELLEMENT-LENTILLES-BBIS", "GO-LENTILLES-BBIS",
                              "CODE-LENTILLES-BBIS"), run: str = RUN_BBIS):
    dossier.mkdir(parents=True, exist_ok=True)
    bbis = dossier / "t07-etape-b-bis-v1.md"
    lignes = ["# Registre jouet de l'apprentissage des sondes sur la tâche", "",
              f"| CODE-BBIS | {HEURE} | registres/t07-etape-b-bis/code-bbis-v2.json | {'1' * 64} |",
              f"| LIGNE-JAMAIS-LUE | {HEURE} | diag/secret/verdict.json | {'2' * 64} |"]
    lignes += [f"| SCORES-BBIS | {HEURE} | diag/{run}/sondes-bbis.json | {sha_e2} |"] * scores
    if verdict:
        lignes.append(f"| VERDICT-BBIS | {HEURE} | docs/verdicts/verdict-jamais-lu.md | {'3' * 64} |")
    bbis.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    propre = dossier / "lecture-sondes-bbis-par-lentilles-v1.md"
    chemins = {"SCELLEMENT-LENTILLES-BBIS": (K.TEXTE, K.EMPREINTE_TEXTE)}
    propre.write_text("# Registre propre jouet\n\n" + "".join(
        f"| {c} | {HEURE} | {chemins.get(c, ('registres/jouet.md', '4' * 64))[0]} | {chemins.get(c, ('', '4' * 64))[1]} |\n"
        for c in propres), encoding="utf-8")
    return bbis, propre


# --- fichiers des sondes ---------------------------------------------------------------------------------------------------------------
REGLAGES_JOUETS = {   # (cellule, pli) → (famille sonde, couche sonde, famille lecteur, couche lecteur)
    ("P-instruit", "e0"): ("lineaire", 7, "lineaire", 7), ("P-instruit", "e1"): ("attention", 15, "lineaire", 15),
    ("P-S25", "e0"): ("lineaire", 15, "attention", 15), ("P-S25", "e1"): ("lineaire", 15, "lineaire", 23),
    ("P-S50", "e0"): ("attention", 23, "attention", 23), ("P-S50", "e1"): ("lineaire", 23, "lineaire", 23),
    ("P-S75", "e0"): ("lineaire", 15, "lineaire", 15), ("P-S75", "e1"): ("lineaire", 7, "lineaire", 7),
    ("P-S100", "e0"): ("lineaire", 15, "lineaire", 15), ("P-S100", "e1"): ("attention", 7, "lineaire", 7),
}


def _sonde(rng, nom, famille, couche, largeur, echelle=1.0):
    q = rng.standard_normal(largeur) * echelle if famille == "attention" else None
    return fam.SondeLineaireJetons(nom, int(couche), K.AGREGATION_DE[famille], rng.standard_normal(largeur) * echelle,
                                   float(rng.standard_normal()), q, famille)


def construire_sondes(racine: Path, formes: dict | None = None, run: str = RUN_BBIS, largeur: int = LARGEUR, graine: int = 7,
                      echelles: dict | None = None, modifier=None, modifier_archive=None) -> SimpleNamespace:
    """Écrit E-1, E-2 et leurs compagnons sous `racine`, comme `marche_v4.ecrire_fermes` ; `formes` : (cellule, pli) → « a »,
    « b » ou « c » (défaut « c ») ; `modifier(doc)` et `modifier_archive(tableaux)` altèrent avant écriture (artefacts)."""
    rng = np.random.default_rng(graine)
    formes, echelles = formes or {}, echelles or {}
    tableaux, sources, objets = {}, {}, {}
    for (cellule, pli), (f_s, c_s, f_e, c_e) in REGLAGES_JOUETS.items():
        k = int(pli[1])
        meta = {"cellule": cellule, "pli_lu": k, "taches_lues": ["t1", "t2"], "plis_internes": [["t3"], ["t4"]],
                "reglage": f"{f_s}-c{c_s}-l2_0.001", "echecs_internes": 0}
        forme = formes.get((cellule, pli), "c")
        if forme == "a":
            meta["echec"] = "sonde en échec : perte non finie à l'époque 0 (motif jamais lu)"
            sources.setdefault(cellule, {})[pli] = meta
            continue
        s = _sonde(rng, f"sonde-{cellule}-{pli}", f_s, c_s, largeur, echelles.get((cellule, pli, "sonde"), 1.0))
        objets[(cellule, pli, "sonde")] = s
        base = f"{cellule}__{pli}__"
        tableaux[base + "sonde_w"], tableaux[base + "sonde_b"] = s.w, np.array([s.b])
        if s.q is not None:
            tableaux[base + "sonde_q"] = s.q
        for j in range(2):
            p = _sonde(rng, f"plancher{j}", f_s, c_s, largeur)
            tableaux[base + f"direction{j}_w"], tableaux[base + f"direction{j}_b"] = p.w, np.array([p.b])
            if p.q is not None:
                tableaux[base + f"direction{j}_q"] = p.q
        meta |= {"empreinte_sonde": s.empreinte(), "famille": f_s, "couche": c_s, "l2": 0.001, "agregation": K.AGREGATION_DE[f_s],
                 "nom_sonde": s.nom, "n_plancher": 800, "noms_deux_premieres": ["p0", "p1"],
                 "empreintes_deux_premieres": ["5" * 64, "6" * 64], "nuls_en_echec": 0, "n_reetiquetages": 100,
                 "ordre2": {"ordre": "inverse", "reglage": "attention-c7-l2_0.1", "echecs_internes": 0, "empreinte_sonde": "7" * 64,
                            "famille": "attention", "couche": 7, "l2": 0.1}}
        if forme == "b":
            meta["enc"] = {"echec": "lecteur en échec (motif jamais lu)", "echecs_internes": 1}
        else:
            e = _sonde(rng, f"enc-{cellule}-{pli}", f_e, c_e, largeur, echelles.get((cellule, pli, "enc"), 1.0))
            objets[(cellule, pli, "enc")] = e
            tableaux[base + "enc_w"], tableaux[base + "enc_b"] = e.w, np.array([e.b])
            if e.q is not None:
                tableaux[base + "enc_q"] = e.q
            meta["enc"] = {"reglage": f"{f_e}-c{c_e}-l2_0.01", "empreinte": e.empreinte(), "echecs_internes": 0}
        sources.setdefault(cellule, {})[pli] = meta
    if modifier_archive:
        modifier_archive(tableaux)
    d = racine / "donnees" / run
    d.mkdir(parents=True)
    e1 = d / "sondes-bbis.npz"
    np.savez(e1, **tableaux)
    compagnon(e1)
    doc = {"run_id": run, "texte": "prereg/T0.7-etape-B-bis-v1.md", "sources": sources,
           "fichiers_scores": [{"fichier": f"donnees/{run}/scores-bbis-000.npz", "sha256": "8" * 64}],
           "fichiers_planchers": [{"fichier": f"donnees/{run}/planchers-bbis-000.npz", "sha256": "9" * 64}],
           "fichier_sondes": {"fichier": f"donnees/{run}/sondes-bbis.npz", "sha256": sha(e1.read_bytes())},
           "graines_derivees": {"bbis/x": 1}, "sans_aucune_aire": True, "variante": "v6", "doses": [0.25, 0.5, 0.75, 1.0],
           "couches": [7, 15, 23], "plis": {"t1": 0}, "manifeste": "runs/x/manifeste.json", "duree_s": 12.5,
           "dispersion_ordres_calcul": {"ordre": "inverse"}, "journal": "journal jamais lu"}
    if modifier:
        modifier(doc)
    g = racine / "diag" / run
    g.mkdir(parents=True)
    e2 = g / "sondes-bbis.json"
    e2.write_text(json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True, default=str) + "\n", encoding="utf-8")
    compagnon(e2)
    return SimpleNamespace(racine=racine, e1=e1, e2=e2, sha_e2=sha(e2.read_bytes()), objets=objets, doc=doc, tableaux=tableaux)


def monde_entrees(tmp: Path, **kw) -> SimpleNamespace:
    """Fichiers des sondes jouets et registres cohérents."""
    s = construire_sondes(tmp / "entrees", **kw)
    bbis, propre = ecrire_registres(tmp / "registres", s.sha_e2)
    return SimpleNamespace(**vars(s), registre_bbis=bbis, registre_propre=propre)


# --- réseau simulé ---------------------------------------------------------------------------------------------------------------------
class TransportSimule:
    """Hôte simulé : `fichiers` (URL → octets) ; `a_porte` : URL servies seulement avec la bonne clé ; `refus` : URL refusées.
    Le flux sort par blocs de 1 000 octets (l'en-tête d'un fichier de poids chevauche plusieurs blocs)."""

    def __init__(self, fichiers: dict, a_porte=(), refus=(), cle: str = FAUSSE_CLE, bloc: int = 1000):
        self.fichiers, self.a_porte, self.refus, self.cle, self.bloc = dict(fichiers), set(a_porte), set(refus), cle, bloc
        self.appels: list[tuple] = []

    def _contenu(self, url, cle):
        if url in self.refus or url not in self.fichiers:
            raise mo.RefusReseau(f"requête refusée par {url.split('?')[0]} (code 403)")
        if url in self.a_porte and (cle is None or cle.valeur() != self.cle):
            raise mo.RefusReseau(f"requête refusée par {url.split('?')[0]} (code 401)")
        return self.fichiers[url]

    def octets(self, url, cle=None, debut=None, fin=None):
        self.appels.append(("octets", url, cle is not None, debut, fin))
        c = self._contenu(url, cle)
        return c if debut is None else c[debut:(None if fin is None else fin + 1)]

    def flux(self, url, cle=None, debut=0):
        self.appels.append(("flux", url, cle is not None, debut, None))
        c = self._contenu(url, cle)
        for i in range(debut or 0, len(c), self.bloc):
            yield c[i:i + self.bloc]


# --- Llama miniature ---------------------------------------------------------------------------------------------------------------------
def construire_llama(dossier: Path, graine: int = 3) -> SimpleNamespace:
    """Llama miniature construit localement (`transformers.LlamaForCausalLM`, 32 blocs de largeur 32), poids tirés par
    graine, écrits en bfloat16 dans deux fichiers `safetensors` et un index, comme le dépôt de Llama."""
    from safetensors.torch import save_file
    from transformers import LlamaConfig, LlamaForCausalLM
    torch.manual_seed(graine)
    config = LlamaConfig(vocab_size=VOCABULAIRE, hidden_size=LARGEUR, intermediate_size=NEURONES, num_hidden_layers=32,
                         num_attention_heads=4, num_key_value_heads=2, max_position_embeddings=64)
    modele = LlamaForCausalLM(config)
    etat = {k: v.detach().clone() for k, v in modele.state_dict().items()}
    etat["model.norm.weight"] = 1.0 + 0.2 * torch.randn(LARGEUR)
    etat["lm_head.weight"] = torch.randn(VOCABULAIRE, LARGEUR)
    etat = {k: v.to(torch.bfloat16) for k, v in etat.items()}
    dossier.mkdir(parents=True)
    noms = sorted(etat)
    moities = {"model-00001-of-00002.safetensors": [n for n in noms if n < "model.layers.2"],
               "model-00002-of-00002.safetensors": [n for n in noms if n >= "model.layers.2"]}
    for fichier, ns in moities.items():
        save_file({n: etat[n] for n in ns}, str(dossier / fichier))
    index = json.dumps({"metadata": {}, "weight_map": {n: f for f, ns in moities.items() for n in ns}}).encode()
    (dossier / "model.safetensors.index.json").write_bytes(index)
    return SimpleNamespace(dossier=dossier, etat=etat, fichiers=list(moities), index=index,
                           config=json.dumps(config.to_dict()).encode())


def construire_lentille(chemin: Path, largeur: int = LARGEUR, graine: int = 5, modifier=None) -> Path:
    """Fausse lentille : `{"J": {0..30}}` en demi-précision et sa `provenance`."""
    g = torch.Generator().manual_seed(graine)
    J = {l: (torch.eye(largeur) + 0.3 * torch.randn(largeur, largeur, generator=g)).to(torch.float16) for l in range(31)}
    charge = {"J": J, "provenance": {"capture_point": "block_output", "source_layers": list(range(31)), "d_model": largeur,
                                     "n_prompts": 64, "target_layer": 31}}
    if modifier:
        modifier(charge)
    torch.save(charge, chemin)
    return chemin


# --- faux code voisin (dépôt git local) ---------------------------------------------------------------------------------------------------
CATALOG_JOUET = '''"""Faux catalogue du voisin (jouet)."""
import json
import os
from pathlib import Path

import torch

MODEL = os.environ.get("NEURON_LENS_MODEL", "Qwen/Qwen3-8B")
DATA = Path(__file__).resolve().parent.parent / "data"
MIN_COUNT = 5


class _Tok:
    def __init__(self):
        self.v = json.loads((DATA / "vocab.json").read_text(encoding="utf-8"))

    def decode(self, ids):
        return "".join(self.v[i] for i in ids)

    def __len__(self):
        return len(self.v)


def tokenizer(model=MODEL):
    return _Tok()


def kept(model=MODEL):
    counts = torch.load(DATA / "token_counts.pt")["counts"]
    v = tokenizer().v
    ids = (counts >= MIN_COUNT).nonzero().squeeze(1)
    return ids[torch.tensor(["\\ufffd" not in v[i] for i in ids.tolist()])]
'''
SCRIPT_05 = '''import json, os, sys
from pathlib import Path
d = Path(__file__).resolve().parent.parent / "data"
(d / "env-05.json").write_text(json.dumps({"noms": sorted(os.environ), "args": sys.argv[1:],
                                           "hors_ligne": os.environ.get("HF_HUB_OFFLINE"), "modele": os.environ.get("NEURON_LENS_MODEL")}))
(d / "corpus" / "act-dclm.jsonl").write_text("{}\\n")
'''
SCRIPT_03 = '''import json, os, sys
from pathlib import Path
import torch
d = Path(__file__).resolve().parent.parent / "data"
assert (d / "corpus" / "act-dclm.jsonl").exists(), "05 doit précéder"
assert os.environ.get("HF_HUB_OFFLINE") == "1"
assert not (d / "token_counts.pt").exists(), "une seule fois"
n = len(json.loads((d / "vocab.json").read_text(encoding="utf-8")))
counts = torch.full((n,), 9)
counts[::17] = 2
(d / "env-03.json").write_text(json.dumps({"noms": sorted(os.environ)}))
torch.save({"counts": counts}, d / "token_counts.pt")
'''


def vocabulaire_jouet() -> list[str]:
    v = [f" mot{i}" for i in range(VOCABULAIRE)]
    for i, s in {3: "7", 4: " 12", 5: "2024 ", 6: " cost", 7: "Price", 8: "$", 9: " fees", 10: "�a", 11: "12a",
                 12: "ligne\n", 13: " Budget "}.items():
        v[i] = s
    return v


def _git(args, cwd):
    subprocess.run(["git", "-c", "user.name=jouet", "-c", "user.email=jouet@exemple.invalid", "-c", "commit.gpgsign=false",
                    *args], cwd=cwd, check=True, capture_output=True)


def construire_voisin(tmp: Path, modifier_readout=None) -> SimpleNamespace:
    """Dépôt git local du faux voisin, et trois faux correctifs (2), (4), (6) qui s'y appliquent."""
    v = tmp / "voisin-source"
    (v / "neuron_lens").mkdir(parents=True)
    (v / "scripts" / "checks").mkdir(parents=True)
    (v / "data" / "corpus").mkdir(parents=True)
    readout = (RACINE / K.COPIE_READOUT).read_text(encoding="utf-8")
    (v / "neuron_lens" / "readout.py").write_text(modifier_readout(readout) if modifier_readout else readout, encoding="utf-8")
    (v / "neuron_lens" / "__init__.py").write_text("")
    (v / "neuron_lens" / "catalog.py").write_text(CATALOG_JOUET, encoding="utf-8")
    (v / "neuron_lens" / "lenses.py").write_text("NEURONPEDIA_FILES = {}\n")
    (v / "scripts" / "checks" / "lens_compare.py").write_text('MODEL = "Qwen/Qwen3-8B"\n')
    (v / "scripts" / "05_act_corpus.py").write_text(SCRIPT_05)
    (v / "scripts" / "03_token_counts.py").write_text(SCRIPT_03)
    (v / "data" / "vocab.json").write_text(json.dumps(vocabulaire_jouet()), encoding="utf-8")
    for tranche, depot in (("dclm", DEPOT_DCLM), ("zh", DEPOT_ZH), ("code", DEPOT_CODE)):
        (v / "data" / "corpus" / f"act-{tranche}.provenance.json").write_text(json.dumps({"repo": depot, "revision": "r" + tranche}))
    _git(["init", "-q", "-b", "main"], v)
    _git(["add", "-A"], v)
    _git(["commit", "-q", "-m", "jouet"], v)
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=v, capture_output=True, text=True).stdout.strip()
    correctifs = tmp / "depot" / "correctifs"
    correctifs.mkdir(parents=True)
    etapes = [("c2.diff", lambda: (v / "neuron_lens" / "lenses.py").write_text("NEURONPEDIA_FILES = {}\nNEURONPEDIA_EXTRA = {}\n")),
              ("c4.diff", lambda: (v / "scripts" / "checks" / "lens_compare.py").write_text("from neuron_lens.catalog import MODEL\n")),
              ("c6.diff", lambda: (v / "data" / "corpus" / "act-chat-llama-3.1-8b-instruct.provenance.json").write_text(
                  json.dumps({"repo": DEPOT_CHAT, "revision": "rchat"}) + "\n"))]
    liste = []
    for nom, changer in etapes:
        changer()
        _git(["add", "-A"], v)
        diff = subprocess.run(["git", "diff", "--cached"], cwd=v, capture_output=True).stdout
        (correctifs / nom).write_bytes(diff)
        liste.append((f"correctifs/{nom}", sha(diff)))
        _git(["reset", "-q", "--hard", "HEAD"], v)
    return SimpleNamespace(url=str(v), commit=commit, correctifs=tuple(liste), depot=tmp / "depot")


def jetons_gardes_jouets() -> list[int]:
    v = vocabulaire_jouet()
    return [i for i in range(VOCABULAIRE) if i % 17 != 0 and "�" not in v[i]]


# --- monde complet pour le lanceur --------------------------------------------------------------------------------------------------------
def monde(tmp: Path, formes=None, echelles=None, modifier_lentille=None, modifier_readout=None, verdict=True) -> SimpleNamespace:
    """Tout ce qu'il faut au lanceur sur jouets : dépôt (copie de `readout.py`, correctifs), faux voisin, Llama miniature,
    fausse lentille, réseau simulé, registres, fichiers des sondes, réglages jouets."""
    voisin = construire_voisin(tmp, modifier_readout)
    copie = voisin.depot / K.COPIE_READOUT
    copie.parent.mkdir(parents=True)
    copie.write_bytes((RACINE / K.COPIE_READOUT).read_bytes())
    llama = construire_llama(tmp / "llama")
    lentille = construire_lentille(tmp / "lentille-source.pt", modifier=modifier_lentille).read_bytes()
    tokeniseur = json.dumps({"jouet": True}).encode()
    licences = {"llama3.1-8b-it/LICENSE": b"licence jouet\n", "llama3.1-8b-it/NOTICE": b"notice jouet\n",
                "llama3.1-8b-it/USE_POLICY.md": b"politique jouet\n"}
    petits = {"model.safetensors.index.json": llama.index, "tokenizer.json": tokeniseur, "config.json": llama.config}
    poids = {f: (llama.dossier / f).read_bytes() for f in llama.fichiers}
    gardes = jetons_gardes_jouets()
    r = la.Reglages(
        largeur=LARGEUR, poids={f: (len(c), mo.identifiant_git(mo.pointeur(sha(c), len(c)))) for f, c in poids.items()},
        petits={n: (len(c), mo.identifiant_git(c)) for n, c in petits.items()}, sha256_tokeniseur=sha(tokeniseur),
        taille_lentille=len(lentille), sha256_lentille=sha(lentille),
        pointeur_lentille=mo.identifiant_git(mo.pointeur(sha(lentille), len(lentille))),
        licences_lentille={n: (len(c), mo.identifiant_git(c)) for n, c in licences.items()},
        url_voisin=voisin.url, commit_voisin=voisin.commit, correctifs=voisin.correctifs,
        n_jetons=len(gardes), sha256_jetons=mo.empreinte_liste_gardee(gardes),
        m=1000, n_temoins_isotrope=400, n_temoins_par_vecteur=100, disque_depart=1, disque_calcul=1)
    fichiers = {mo.url_fichier(r.depot_lentille, r.revision_lentille, r.fichier_lentille): lentille,
                r.url_voisin + "/info/refs?service=git-upload-pack": b"001e# service=git-upload-pack\n",
                mo.url_arbre(r.depot_llama, r.revision_llama): json.dumps(
                    [{"type": "file", "path": f, "oid": r.poids[f][1], "size": len(c), "lfs": {"oid": sha(c), "size": len(c)}}
                     for f, c in poids.items()]).encode()}
    a_porte = {mo.url_arbre(r.depot_llama, r.revision_llama)}
    for n, c in (petits | poids).items():
        u = mo.url_fichier(r.depot_llama, r.revision_llama, n)
        fichiers[u] = c
        a_porte.add(u)
    for n, c in licences.items():
        fichiers[mo.url_fichier(r.depot_lentille, r.revision_lentille, n)] = c
    for depot, rev in ((DEPOT_DCLM, "rdclm"), (DEPOT_ZH, "rzh"), (DEPOT_CODE, "rcode"), (DEPOT_CHAT, "rchat")):
        fichiers[mo.url_arbre(depot, rev, jeu=True, recursif=True)] = json.dumps(
            [{"type": "file", "path": "README.md"}, {"type": "file", "path": "data/train-00000.parquet"}]).encode()
        fichiers[mo.url_fichier(depot, rev, "data/train-00000.parquet", jeu=True)] = b"PAR1jouet"
    transport = TransportSimule(fichiers, a_porte)
    s = construire_sondes(tmp / "entrees", formes=formes, echelles=echelles)
    bbis, propre = ecrire_registres(tmp / "registres", s.sha_e2, verdict=verdict)
    ctx = la.Contexte(tmp / "travail", tmp / "sortie", RUN, voisin.depot, propre, r, transport, {K.NOM_CLE: FAUSSE_CLE})
    return SimpleNamespace(ctx=ctx, reglages=r, transport=transport, registre_bbis=bbis, registre_propre=propre, sondes=s,
                           llama=llama, lentille=lentille, voisin=voisin, entrees=tmp / "entrees", gardes=gardes, tmp=tmp)
