"""Partie 2 de l'addendum de la tranche de l'ajustement de nos lentilles — relevée, comparée et scellée SUR LA MACHINE — v2.
v3 du code de course (2026-11-18, session de la lecture par lentille neuronale) : seul changement de fond, la ligne de calcul exigée GO-2026-11-18-35 (R-3314) au lieu de la ligne de décision GO-2026-11-18-02, que le crochet de calcul refuse dans une commande de création ; le reste suit les noms v3 (lanceur, partie 2, amorce, dépôt réduit, essais).


v2 = v1 (`addendum_partie2_b_beta_v1.py`, `e7a05104…`, archivée) avec le compte et le rang du jeton de début (texte gelé, P.6 ;
contre-lecture du code de course, B-1) et la version de PyYAML relevée (m-15), pour le lanceur v2.

Addendum partie 1 (`docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md`, `bd8067dc…`), en tête et § 6 : la
partie 2 est écrite par le code de course **au fil des étapes**, en deux fichiers neufs (R12) :
- `rediger_b0` — ce qui existe à B0 (poids et tokeniseur, lentilles publiques, provenance et comptes du corpus d'ajustement, versions,
  Drowse, code voisin corrigé, essais et artefacts), comparé à la partie 1 **avant l'ajustement** ;
- `rediger_corpus` — ce qui n'existe qu'après (fichiers du corpus d'activations, provenances, jetons gardés), comparé juste après l'unique
  `03_token_counts.py`, avant `lens_compare.py` et la fumée.
Chaque fonction rend (texte, écarts) ; **tout écart arrête la course à cette étape** (le lanceur lève, la mère est saisie). Aucune pause
humaine : tout est égalité de valeurs écrites en partie 1 ou au texte gelé.
"""
from __future__ import annotations

import re
from pathlib import Path

from controle_ia.neuron_lens import controles_b_beta_v2 as cb

_SECRETS = re.compile(r"hf_[A-Za-z0-9]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}")


def _secrets(texte: str) -> list[str]:
    return ["forme de secret trouvée dans le texte rendu"] if _SECRETS.search(texte) else []


def ecarts_b0(r: dict) -> list[str]:
    from controle_ia.neuron_lens import b_beta_lancer_v3 as L
    pb = []
    for n, h in L.MODELE_FICHIERS.items():
        if r["modele"].get(n) != h:
            pb.append(f"modèle : {n} d'empreinte {str(r['modele'].get(n))[:12]}…, attendu {h[:12]}…")
    for s, (_, h) in L.LENTILLES_NP.items():
        if r["lentilles_np"].get(s) != h:
            pb.append(f"lentille de Neuronpedia {s} : empreinte inattendue")
    for k, v in cb.VERSIONS.items():
        if k == "drowse.ai":
            continue
        if r["versions"].get(k) != v:
            pb.append(f"version de {k} : {r['versions'].get(k)!r}, attendue {v!r} (nœud à la mère avant l'ajustement)")
    if r["drowse"].get("version") != cb.DROWSE_VERSION or r["drowse"].get("roue_sha256") != cb.DROWSE_SHA256:
        pb.append("Drowse : version ou empreinte de la roue inattendue")
    v = r["voisin"]
    if v.get("head") != L.COMMIT_VOISIN or v.get("arbre") != L.ARBRE_VOISIN or v.get("apres") != L.VOISIN_APRES:
        pb.append("code voisin : commit, arbre ou fichiers corrigés inattendus")
    d = cb.garde_d(r["essais"])
    pb += d
    for e, (_, n) in L.ESSAIS.items():
        x = r["essais"].get(Path(e).name, {})
        if n is not None and x.get("passes") != n:
            pb.append(f"essai {Path(e).name} : {x.get('passes')} tests passés au lieu de {n}")
    pb += [f"artefact « {k} » de la garde (d) non vu en défaut" for k, x in r["artefacts_d"].items() if not x.get("vu_en_defaut")]
    p1 = r["corpus_ajustement"]["p1"]
    if p1.get("docs") != cb.N_DOCS or list(p1.get("moities", [])) != list(cb.MOITIES) or p1.get("rows_sha256") != cb.ROWS_SHA256:
        pb.append("corpus d'ajustement : documents, moitiés ou empreinte des lignes différents de la partie 1 (§ 3)")
    if list(p1.get("rows_sha256_moities", [])) != list(cb.ROWS_SHA256_MOITIES):
        pb.append("corpus d'ajustement : empreintes des moitiés différentes de la partie 1 (§ 3)")
    return pb


def rediger_b0(r: dict) -> tuple[str, list[str]]:
    from controle_ia.neuron_lens import b_beta_lancer_v3 as L
    pb = ecarts_b0(r)
    l = ["# Addendum de la tranche de l'ajustement de nos lentilles — partie 2, premier relevé (B0, avant l'ajustement) — v2", "",
         "Écrit par `controle_ia.neuron_lens.addendum_partie2_b_beta_v3` sur la machine (aucune pause humaine). Partie 1 :",
         "`docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md` (`bd8067dc…`). **Tout écart ci-dessous",
         "arrête la course avant l'ajustement.**", "",
         f"- date : {r['date_utc']} ; instance : {r['instance']}",
         f"- commit réduit : {r['commit_reduit']} ; commit source : {r['commit_source']} ; commit voisin : {r['voisin'].get('head')}"
         f" (arbre {r['voisin'].get('arbre')}, correctifs appliqués sans commit)", "", "## Écarts", ""]
    l += [f"- {p}" for p in pb] or ["Aucun."]
    l += ["", f"## Modèle `{L.LLAMA}`, révision {L.REVISION_LLAMA}", "", "| fichier | sha256 relevé | attendu (partie 1, § 2) |", "|---|---|---|"]
    l += [f"| `{n}` | `{r['modele'].get(n)}` | `{h}` |" for n, h in L.MODELE_FICHIERS.items()]
    l += ["", f"## Lentilles de Neuronpedia, révision {L.REVISION_NEURONPEDIA}", ""]
    l += [f"- `{s}` : `{r['lentilles_np'].get(s)}` (attendu `{h}`)" for s, (_, h) in L.LENTILLES_NP.items()]
    l += ["", "## Corpus d'ajustement", ""]
    ca = r["corpus_ajustement"]
    p1 = ca["p1"]
    l += [f"- provenance écrite par `01_lens_corpus.py` : sha256 `{ca.get('provenance_sha256')}` (publiée : `{cb.PROVENANCE_AJUSTEMENT_PUBLIEE}`)",
          f"- `dclm.jsonl` : sha256 `{ca.get('dclm_jsonl_sha256')}`",
          f"- documents pleins de 128 jetons : {p1.get('docs')} ; moitiés {p1.get('moities')} ; longueurs {p1.get('longueurs')}",
          f"- `rows_sha256` : `{p1.get('rows_sha256')}` ; moitiés `{p1.get('rows_sha256_moities')}`"]
    l += ["", "## Versions", ""] + [f"- {k} : {v}" for k, v in sorted(r["versions"].items())]
    l += [f"- Drowse : version {r['drowse'].get('version')}, roue `{r['drowse'].get('roue_sha256')}` (installée sans dépendances)"]
    l += ["", "## Code voisin corrigé", ""] + [f"- `{f}` : `{h}`" for f, h in sorted(r["voisin"].get("apres", {}).items())]
    l += ["", "## Essais de B0", ""] + [f"- `{n}` : code {x.get('code')}, « {x.get('resume')} »" for n, x in r["essais"].items()]
    l += [f"- artefact « {k} » : code {x.get('code')}, « {x.get('resume')} », vu en défaut : {x.get('vu_en_defaut')}"
          for k, x in r["artefacts_d"].items()]
    texte = "\n".join(l) + "\n"
    return texte, pb + _secrets(texte)


def ecarts_corpus(r: dict) -> list[str]:
    pb = []
    for f, h in cb.CORPUS_ACT_SHA256.items():
        if r["corpus"].get(f) != h:
            pb.append(f"corpus d'activations : {f} d'empreinte {str(r['corpus'].get(f))[:12]}…, attendue {h[:12]}… (partie 1, § 3)")
    if r["kept"].get("n") != cb.KEPT_N or r["kept"].get("sha256") != cb.KEPT_SHA256:
        pb.append(f"jetons gardés : {r['kept'].get('n')} identifiants, empreinte {str(r['kept'].get('sha256'))[:12]}…, attendus "
                  f"{cb.KEPT_N} et {cb.KEPT_SHA256[:12]}… (partie 1, § 3)")
    pb += [f"provenance : {p}" for p in r["provenances"]]
    return pb


def rediger_corpus(r: dict) -> tuple[str, list[str]]:
    pb = ecarts_corpus(r)
    l = ["# Addendum de la tranche de l'ajustement de nos lentilles — partie 2, second relevé (après les comptes de jetons) — v2", "",
         "Écrit sur la machine juste après l'unique `03_token_counts.py`, avant `lens_compare.py` et la fumée. **Tout écart ci-dessous",
         "arrête la course à cette étape (nœud à la mère).**", "", "## Écarts", ""]
    l += [f"- {p}" for p in pb] or ["Aucun."]
    l += ["", "## Corpus d'activations", "", "| fichier | sha256 relevé | attendu |", "|---|---|---|"]
    l += [f"| `{f}` | `{r['corpus'].get(f)}` | `{h}` |" for f, h in cb.CORPUS_ACT_SHA256.items()]
    k, j = r["kept"], r.get("jeton_de_debut", {})
    l += ["", f"## Jetons gardés de Llama : {k.get('n')} identifiants, sha256 `{k.get('sha256')}`", "",
          f"Jeton de début (128 000) : compte {j.get('compte')} dans le corpus d'activations ; gardé : {j.get('garde')} ; rang par compte "
          f"décroissant parmi les jetons gardés : {j.get('rang_par_compte')} ({j.get('regle_egalites')}) — rapporté, sans critère."]
    texte = "\n".join(l) + "\n"
    return texte, pb + _secrets(texte)


def ecrire_une_fois(chemin: Path, texte: str) -> str:
    """Écrit et scelle `chemin` ; à une reprise, le fichier déjà écrit doit être identique au texte refait, à la date près (R12)."""
    from controle_ia.scellement import sceller, verifier
    chemin = Path(chemin)
    if chemin.exists():
        sans_date = lambda t: re.sub(r"- date : \S+", "", t)
        if sans_date(chemin.read_text(encoding="utf-8")) != sans_date(texte):
            raise ValueError("partie 2 déjà écrite, différente du relevé refait : R12, aucun écrasement")
        return verifier(chemin)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(texte, encoding="utf-8")
    return sceller(chemin)
