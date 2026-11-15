"""Partie 2 de l'addendum des empreintes pour la tranche B-α de « Neuron Lens » — rédigée, vérifiée et scellée SUR LA MACHINE — v1.

Pièce 3 du § 6 du devis B-α v2 (`docs/notes/neuron-lens-v1/devis-b-alpha/devis-tranche-b-alpha-v2.md`, `61c394f5…`, étape 3 bis, M1) :
après B0, les téléchargements et le corpus, et **avant la fumée**, la machine écrit un fichier neuf (R12), le scelle et le pousse ; le
lanceur refuse la fumée sans son compagnon. **Tout écart = arrêt** (`verifier` rend la liste ; vide = rien à redire). Aucune pause
humaine : tout ce qui demande un jugement a été lu avant le feu (`lecture-config-credit-neuronpedia-v1.md`) et n'est ici qu'une égalité
d'empreintes.

Références (partie 1, `addendum-empreintes-v3.md`, `e63d95ca…` ; texte gelé v6, `34b88243…`) : révision de Llama `0e9e39f2…` ; lentilles de
Neuronpedia à `d2527c3c…` (J, J++, R) ; provenances du dépôt voisin à `849bfe16` ; tranches et nombres de lignes du § 4. Les empreintes
des poids et du tokeniseur de Llama ne sont pas publiées sans accès : elles sont comparées à celles que le hub donne, **à la révision
épinglée**, au moment du téléchargement (LFS : sha256 ; sinon : empreinte git du blob), relevées par le lanceur avec la clé, sans la clé
dans aucun fichier.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from controle_ia.neuron_lens.controles_b0_v2 import TRANCHES, verifier_provenances

REVISION_LLAMA = "0e9e39f249a16976918f6564b8830bc894c89659"
REVISION_NEURONPEDIA = "d2527c3cdbaa60dd4b65cbca1604921f044e989a"
COMMIT_VOISIN = "849bfe1678e28becceb1e3864afe5fc8297d02e4"
LENTILLES = {"J": "d5300a1575c0b5ad6e01b098c75adb072f3a6c246f184ce2fb35a3550fc8c68b",
             "npJpp": "8bd04f482aed9c85e76e71ccb510907405500512193cdfcc34f4f31722056f7c",
             "npR": "a63a1588f2cb61850c68131a5f13b74590f4fe137f67bf80c627547d2230d31c"}
CONFIG_NEURONPEDIA = {"jlens/Salesforce-wikitext/config.yaml": "0ae053cfdcf8909782d3ba55a25125d2d5db3015",
                      "jpp/Salesforce-wikitext/CREDIT.md": "14fc7e775a0abf3dc1d5ba4af02784031a9e454f",
                      "jpp/Salesforce-wikitext/config.yaml": "6bd6b47ddc1b7f680a72e6976f4280b29b7b9844",
                      "rlens/Salesforce-wikitext/CREDIT.md": "d3724c2b5cd0daed4bd399e22e626f8f82f1d1fe",
                      "rlens/Salesforce-wikitext/config.yaml": "01d952a6b357cfdf16e39e5cb58942cb1ddef57c"}
LIGNES = {"dclm": 40000, "zh": 8000, "code": 8000, "chat": 8000}
ESSAIS_B0 = ("essai-06_activations-llama-v3.py", "essai-lenses-neuronpedia-v3.py", "essai-causal_lens-graine-v1.py",
             "essai-crochets-causal_lens-llama-v1.py")
VERSIONS_EXIGEES = ("python", "torch", "transformers", "numpy", "huggingface_hub", "safetensors", "pyarrow", "tokenizers")
MODELE_EXIGES = ("config.json", "tokenizer.json", "tokenizer_config.json")
_HEX = {40: re.compile(r"^[0-9a-f]{40}$"), 64: re.compile(r"^[0-9a-f]{64}$")}
# formes de secrets refusées dans le texte rendu (jetons du hub et de l'hébergeur de code)
_SECRETS = re.compile(r"hf_[A-Za-z0-9]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}")


def git_sha1(donnees: bytes) -> str:
    """Empreinte git d'un blob (`git hash-object`)."""
    return hashlib.sha1(b"blob %d\0" % len(donnees) + donnees).hexdigest()


def empreintes_fichier(chemin) -> dict:
    """{"sha256", "git_sha1", "taille"} d'un fichier, lu par blocs (les poids font plusieurs Go)."""
    p = Path(chemin)
    taille = p.stat().st_size
    h256, h1 = hashlib.sha256(), hashlib.sha1(b"blob %d\0" % taille)
    with open(p, "rb") as fh:
        while b := fh.read(1 << 24):
            h256.update(b)
            h1.update(b)
    return {"sha256": h256.hexdigest(), "git_sha1": h1.hexdigest(), "taille": taille}


def _hex(v, n) -> bool:
    return isinstance(v, str) and bool(_HEX[n].match(v))


def verifier(r: dict) -> list[str]:
    """Toutes les égalités et présences exigées. Rend la liste des écarts (vide = rien à redire) ; chaque écart arrête la course."""
    pb = []
    for k in ("date_utc", "instance", "commit_reduit", "commit_source", "commit_voisin", "modele", "lentilles", "config_neuronpedia",
              "corpus", "provenances", "debuts", "kept", "versions", "controles"):
        if k not in r:
            pb.append(f"relevé incomplet : {k} absent")
    if pb:
        return pb
    for k in ("commit_reduit", "commit_source"):
        if not _hex(r[k], 40):
            pb.append(f"{k} illisible")
    if r["commit_voisin"] != COMMIT_VOISIN:
        pb.append(f"commit voisin {r['commit_voisin']} ≠ {COMMIT_VOISIN}")
    # modèle : révision, fichiers exigés, égalité au hub fichier par fichier
    m = r["modele"]
    if m.get("revision") != REVISION_LLAMA:
        pb.append(f"révision de Llama {m.get('revision')} ≠ {REVISION_LLAMA}")
    fich, att = m.get("fichiers", {}), m.get("attendus", {})
    if not att or set(fich) != set(att):
        pb.append(f"fichiers du modèle {sorted(fich)} ≠ attendus du hub {sorted(att)}")
    if not any(n.endswith(".safetensors") for n in fich):
        pb.append("aucun fichier de poids .safetensors")
    for n in MODELE_EXIGES:
        if n not in fich:
            pb.append(f"fichier du modèle absent : {n}")
    for n in sorted(set(fich) & set(att)):
        f, a = fich[n], att[n]
        if not (_hex(f.get("sha256"), 64) and _hex(f.get("git_sha1"), 40)):
            pb.append(f"{n} : empreintes calculées illisibles")
        elif "lfs_sha256" in a:
            if f["sha256"] != a["lfs_sha256"]:
                pb.append(f"{n} : sha256 {f['sha256'][:12]}… ≠ hub {str(a['lfs_sha256'])[:12]}…")
        elif "git_sha1" in a:
            if f["git_sha1"] != a["git_sha1"]:
                pb.append(f"{n} : empreinte git {f['git_sha1'][:12]}… ≠ hub {str(a['git_sha1'])[:12]}…")
        else:
            pb.append(f"{n} : aucune empreinte attendue du hub")
        if "taille" in a and a["taille"] != f.get("taille"):
            pb.append(f"{n} : taille {f.get('taille')} ≠ hub {a['taille']}")
    # lentilles et fichiers de configuration de Neuronpedia : égalité aux valeurs fixées avant le feu
    le = r["lentilles"]
    if le.get("revision") != REVISION_NEURONPEDIA:
        pb.append(f"révision des lentilles {le.get('revision')} ≠ {REVISION_NEURONPEDIA}")
    for s, h in LENTILLES.items():
        if le.get("fichiers", {}).get(s, {}).get("sha256") != h:
            pb.append(f"lentille {s} : empreinte ≠ {h[:12]}…")
    for n, h in CONFIG_NEURONPEDIA.items():
        if r["config_neuronpedia"].get(n, {}).get("git_sha1") != h:
            pb.append(f"Neuronpedia {n} : empreinte git ≠ {h[:12]}… (lecture de la convention faite sur cette version)")
    # corpus : quatre tranches, nombres de lignes, provenances égales à celles du dépôt voisin
    for t in TRANCHES:
        c = r["corpus"].get(t)
        if not c:
            pb.append(f"tranche {t} absente du corpus")
            continue
        if c.get("lignes") != LIGNES[t]:
            pb.append(f"tranche {t} : {c.get('lignes')} lignes ≠ {LIGNES[t]}")
        if not _hex(c.get("sha256"), 64) or not isinstance(c.get("taille"), int) or c["taille"] <= 0:
            pb.append(f"tranche {t} : empreinte ou taille illisible")
    pb += verifier_provenances(r["provenances"].get("produites", {}), r["provenances"].get("references", {}))
    for t in TRANCHES:
        d = r["debuts"].get(t)
        if not isinstance(d, dict) or sum(d.values()) != LIGNES[t]:
            pb.append(f"tranche {t} : comptes des jetons de début absents ou sans {LIGNES[t]} documents")
    if not (isinstance(r["kept"].get("n"), int) and r["kept"]["n"] > 0 and _hex(r["kept"].get("sha256"), 64)):
        pb.append("liste catalog.kept de Llama : nombre ou empreinte illisible")
    for k in VERSIONS_EXIGEES:
        if not r["versions"].get(k):
            pb.append(f"version absente : {k}")
    # contrôles de B0 : quatre essais passés sans test sauté, lentilles sans arrêt, code des verdicts (B.3) rejoué
    ctl = r["controles"]
    for e in ESSAIS_B0:
        x = ctl.get("essais", {}).get(e)
        if not x:
            pb.append(f"essai {e} non joué")
        elif x.get("code") != 0 or "skipped" in str(x.get("resume", "")) or "passed" not in str(x.get("resume", "")):
            pb.append(f"essai {e} en échec ou avec un test sauté : code {x.get('code')}, {x.get('resume')!r}")
    for s in LENTILLES:
        x = ctl.get("lentilles", {}).get(s)
        if x is None:
            pb.append(f"contrôle de la lentille {s} non fait")
        elif x.get("arrets"):
            pb.append(f"lentille {s} : arrêt de B0 : {'; '.join(x['arrets'])}")
    b3 = ctl.get("verdicts_b3", {})
    if b3.get("code") != 0 or "passed" not in str(b3.get("resume", "")) or "failed" in str(b3.get("resume", "")):
        pb.append(f"code des verdicts (B.3) rejoué en échec : {b3!r}")
    return pb


def rediger(r: dict) -> tuple[str, list[str]]:
    """Texte de la partie 2 (déterministe) et liste des écarts. Les écarts sont écrits dans le texte, qui est versé dans tous les cas
    (diagnostic) ; le lanceur arrête la course si la liste n'est pas vide."""
    pb = verifier(r)
    L = ["# Addendum des empreintes du texte gelé v6 — partie 2, tranche B-α (relevée et scellée sur la machine) — v1", "",
         "Écrite par `controle_ia.neuron_lens.addendum_partie2_b_alpha_v1` (aucune pause humaine). Partie 1 :",
         "`docs/notes/neuron-lens-v1/addendum-empreintes-v3.md`. **Tout écart ci-dessous arrête la course avant la fumée.**", "",
         f"- date : {r.get('date_utc')} ; instance : {r.get('instance')}",
         f"- commit réduit : {r.get('commit_reduit')} ; commit source : {r.get('commit_source')} ; commit voisin : {r.get('commit_voisin')}",
         "", "## Écarts", ""]
    L += [f"- **{p}**" for p in pb] or ["Aucun."]
    m = r.get("modele", {})
    L += ["", f"## Modèle `meta-llama/Llama-3.1-8B-Instruct`, révision {m.get('revision')}", "",
          "| fichier | taille | sha256 | empreinte git | attendu du hub |", "|---|---|---|---|---|"]
    for n in sorted(m.get("fichiers", {})):
        f, a = m["fichiers"][n], m.get("attendus", {}).get(n, {})
        L.append(f"| `{n}` | {f.get('taille')} | `{f.get('sha256')}` | `{f.get('git_sha1')}` | "
                 + (f"sha256 `{a['lfs_sha256']}`" if "lfs_sha256" in a else f"git `{a.get('git_sha1')}`") + " |")
    le = r.get("lentilles", {})
    L += ["", f"## Lentilles de Neuronpedia, révision {le.get('revision')}", "", "| lentille | chemin | taille | sha256 |", "|---|---|---|---|"]
    for s in LENTILLES:
        f = le.get("fichiers", {}).get(s, {})
        L.append(f"| `{s}` | `{f.get('chemin')}` | {f.get('taille')} | `{f.get('sha256')}` |")
    L += ["", "Fichiers de configuration (convention lue avant le feu, `lecture-config-credit-neuronpedia-v1.md`) :", ""]
    L += [f"- `{n}` : `{r.get('config_neuronpedia', {}).get(n, {}).get('git_sha1')}`" for n in CONFIG_NEURONPEDIA]
    L += ["", "## Corpus d'activations de Llama", "", "| tranche | fichier | lignes | taille | sha256 | jetons de début en tête : documents |",
          "|---|---|---|---|---|---|"]
    for t in TRANCHES:
        c, d = r.get("corpus", {}).get(t, {}), r.get("debuts", {}).get(t, {})
        dd = ", ".join(f"{k} : {v}" for k, v in sorted(d.items(), key=lambda kv: int(kv[0]))) if isinstance(d, dict) else str(d)
        L.append(f"| {t} | `{c.get('fichier')}` | {c.get('lignes')} | {c.get('taille')} | `{c.get('sha256')}` | {dd} |")
    k = r.get("kept", {})
    L += ["", f"Liste `catalog.kept` de Llama : {k.get('n')} identifiants, sha256 `{k.get('sha256')}` (consignée, sans référence).", "",
          "## Versions", ""]
    L += [f"- {n} : {v}" for n, v in sorted(r.get("versions", {}).items())]
    ctl = r.get("controles", {})
    L += ["", "## Sorties des contrôles de B0", ""]
    L += [f"- essai `{e}` : code {x.get('code')}, `{x.get('resume')}`" for e, x in sorted(ctl.get("essais", {}).items())]
    for s, x in sorted(ctl.get("lentilles", {}).items()):
        L.append(f"- lentille `{s}` : arrêts {x.get('arrets')} ; défauts (e) {x.get('defauts')} ; autres clés {x.get('autres_cles')}")
    b3 = ctl.get("verdicts_b3", {})
    L.append(f"- code des verdicts (B.3) rejoué : code {b3.get('code')}, `{b3.get('resume')}`")
    texte = "\n".join(L) + "\n"
    if _SECRETS.search(texte) or _SECRETS.search(json.dumps(r, ensure_ascii=False)):
        raise ValueError("forme de secret trouvée dans le relevé : rien n'est écrit")
    return texte, pb


def ecrire_et_sceller(chemin, texte: str) -> str:
    """Écrit un fichier neuf (refus s'il existe, R12) et son compagnon `.sha256` ; rend l'empreinte."""
    from controle_ia.scellement import sceller
    p = Path(chemin)
    if p.exists():
        raise FileExistsError(f"{p} existe déjà : R12 interdit d'écraser")
    p.write_text(texte, encoding="utf-8")
    return sceller(p)
