"""Chargement réel des ressources du volet A de « Neuron Lens » (Qwen3-8B) — v1.

Pour la machine louée seulement (aucun téléchargement de poids dans le conteneur) : téléchargement **par révision épinglée** de chaque
fichier, empreinte vérifiée contre l'addendum (`docs/notes/neuron-lens-v1/addendum-empreintes-v3.md`, `e63d95ca…`) quand l'addendum la
fixe, relevée sinon (pour la partie 2 de l'addendum) ; recalcul de `catalog.kept` par la règle du catalogue (comptes ≥ 5, décodage sans
« � ») et égalité exigée avec la liste versée (`cd8a6c23…`) ; garde du rendu de l'invite par le tokeniseur du modèle ; pièces des cas
sains (i) et (ii) tirées des poids et de la table `acts` de la couche 1. Code à nous : `huggingface_hub`, `transformers`, `torch`,
`pyarrow` ; aucun code du dépôt voisin (les formats sont lus dans sa copie archivée : `neuron_lens/arch.py`, `lens_means`, lignes
118-146 ; `neuron_lens/catalog.py`, `kept` et `lobe_signs`).

Lectures déclarées :
- poids chargés en bfloat16 (comme le catalogue publié, `arch.load_model`), passes en bfloat16 ; matrices de lentilles, plongements,
  désenchâssement et lignes des pôles convertis en float32 puis lus en float64 par les fonctions scellées ;
- `rs-lenses` : `r-lens/lens.pt` → clé « J », indexée par couche (sortie de la couche l → sortie de la dernière) ; `s-lens/out.pt`
  et `s-lens/mid.pt` → clé « K » (plongements → sortie de la couche l, → entrée de la couche à portes l) ; chaque matrice lue doit être
  [d, d], finie, et différente de l'identité (écart maximal > 10⁻⁶) ;
- table `acts` : 2f lignes, pôles « + » puis « − » (`catalog.lobe_signs`) ; le pôle `L1 n11672 −` est la ligne f + 11672 ; lobe
  négatif si `neg_lobe` > 0,5 ; nombre de lignes ≠ 2f → arrêt ;
- l'écriture du pôle `L8 n344 +` est la colonne 344 de `down_proj` de la couche 8 ; les lignes de porte et de montée du pôle
  `L1 n11672` sont les lignes 11672 de `gate_proj` et `up_proj` de la couche 1, et γ le poids de `post_attention_layernorm` de la
  couche 1.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from controle_ia.neuron_lens import volet_a_donnees_v1 as vd

QWEN, REV_QWEN = "Qwen/Qwen3-8B", "b968826d9c46dd6066d109eabc6255188de91218"
LENTILLES, REV_LENTILLES = "stdlogits/rs-lenses", "984fe3d2a46a35580764260ea438cbd6ac17c486"
CATALOGUE, REV_CATALOGUE = "stdlogits/neuron-lens", "2f19669198445347a4dbd1a2c2324652ee31b0a2"
MIN_COUNT = 5
EMPREINTE_KEPT = "cd8a6c236cb1bd4a9ed16bf7981104457ae5f1fea65fe16bb7d902aa86307ac7"
NEURONE_OWL, COUCHE_OWL = 344, 8
NEURONE_GERMAN, COUCHE_GERMAN = 11672, 1


@dataclass(frozen=True)
class Fichier:
    cle: str
    depot: str
    type_depot: str          # "model" ou "dataset"
    revision: str
    chemin: str
    empreinte: str | None    # None : relevée au téléchargement (partie 2 de l'addendum)


FICHIERS = (
    *(Fichier(f"qwen_poids_{i}", QWEN, "model", REV_QWEN, f"model-0000{i}-of-00005.safetensors", e) for i, e in enumerate((
        "31d6a825ae35f11fb85b195b4c42c146c051e446433125a215336abdf95cbf5f",
        "5991236cea6fe21f3d43cab0f0e84448734fbbe0789816202989f2ddc9d18282",
        "c5185c4794be2d8a9784d5753c9922db38df478ce11f9ed0b415b7304d896836",
        "b5ee7de71fbf17db3d5704e0c8f2bc7d005ca9e1d7ca2aeb19827b0cfcaa917a",
        "20c2d6366ab85c90786ccdd829cd2b9e7d30ef3b2ebbb998280e7e4014b542ff"), start=1)),
    Fichier("qwen_index", QWEN, "model", REV_QWEN, "model.safetensors.index.json", None),
    Fichier("qwen_config", QWEN, "model", REV_QWEN, "config.json", None),
    Fichier("qwen_tokeniseur", QWEN, "model", REV_QWEN, "tokenizer.json", vd.EMPREINTE_TOKENISEUR),
    Fichier("qwen_tokeniseur_config", QWEN, "model", REV_QWEN, "tokenizer_config.json", None),
    Fichier("qwen_vocab", QWEN, "model", REV_QWEN, "vocab.json", None),
    Fichier("qwen_merges", QWEN, "model", REV_QWEN, "merges.txt", None),
    Fichier("qwen_generation", QWEN, "model", REV_QWEN, "generation_config.json", None),
    Fichier("r_out", LENTILLES, "model", REV_LENTILLES, "qwen3-8b/r-lens/lens.pt",
            "5eaa4d56e10d0c535b5170d5aaaa1174fb8dedf0fddb2f9821cec0aa1050fae1"),
    Fichier("s_out", LENTILLES, "model", REV_LENTILLES, "qwen3-8b/s-lens/out.pt",
            "f87601433def8cfc403508acccadb7e62d99a5ccf51ec30e730d7c93c21d37ec"),
    Fichier("s_mid", LENTILLES, "model", REV_LENTILLES, "qwen3-8b/s-lens/mid.pt",
            "836ac41eb7ba2194c1302e27b37d92dce23d67504310444ecfe926e6bd28a1b2"),
    Fichier("comptes", CATALOGUE, "dataset", REV_CATALOGUE, "qwen3-8b/token_counts.pt",
            "10e90037470c51bfd75e15ff8d28a830172a5b5c9f9a6c38024a768534e5697b"),
    Fichier("acts_L01", CATALOGUE, "dataset", REV_CATALOGUE, "qwen3-8b/neurons/acts/L01.parquet",
            "17424cd15472e518b5c5b58a8ce2fe1bd482a49153038378d24564f8e6abb347"),
    *(Fichier(f"acts_L{l:02d}", CATALOGUE, "dataset", REV_CATALOGUE, f"qwen3-8b/neurons/acts/L{l:02d}.parquet", e) for l, e in zip(
        vd.COUCHES, ("c837fe7dd29f6450dbeaccaa691a98f2e88afec1f3acf822ddf51ef01019e836",
                     "8a2bfb9233da13d24d7eb264aebd3bb5232514fbc7fffdc8630a963c414c35c2",
                     "0ed7c1f876d8eaec777059d19b3c55abc7df402354ddd3e2d1285e916fb36973",
                     "b88976fcca7b0ed1068da7439a0f1e3fb95be610cab03391d8927dc9840685a0"))),
)


def empreinte(chemin) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 24), b""):
            h.update(bloc)
    return h.hexdigest()


def telecharger(dossier, fichiers=None, telechargeur=None) -> tuple[dict, list]:
    """Télécharge chaque fichier à sa révision épinglée dans `dossier` ; empreinte exigée quand elle est fixée (sinon relevée). Rend
    (clé → chemin local, relevé [clé, dépôt, révision, chemin, empreinte, taille, « vérifiée » | « relevée »]). Une empreinte
    différente arrête tout (aucun repli)."""
    if telechargeur is None:
        from huggingface_hub import hf_hub_download as telechargeur
    chemins, releve = {}, []
    for f in (FICHIERS if fichiers is None else fichiers):
        p = Path(telechargeur(repo_id=f.depot, filename=f.chemin, revision=f.revision, repo_type=f.type_depot,
                              cache_dir=str(dossier)))
        e = empreinte(p)
        if f.empreinte is not None and e != f.empreinte:
            raise ValueError(f"empreinte inattendue : {f.depot}@{f.revision[:8]}/{f.chemin} ({e})")
        chemins[f.cle] = p
        releve.append([f.cle, f.depot, f.revision, f.chemin, e, p.stat().st_size, "vérifiée" if f.empreinte else "relevée"])
    return chemins, releve


def gardes_recalcules(chemin_comptes, tok, attendue=EMPREINTE_KEPT) -> np.ndarray:
    """`catalog.kept` recalculé : jetons de compte ≥ 5 dont le décodage ne contient pas « � » ; égalité exigée avec la liste versée."""
    import torch
    comptes = torch.load(chemin_comptes, weights_only=True, map_location="cpu")["counts"]
    ids = (comptes >= MIN_COUNT).nonzero().squeeze(1).tolist()
    gardes = [i for i in ids if "�" not in tok.decode([i])]
    txt = "".join(f"{i}\n" for i in sorted(gardes)).encode()
    if hashlib.sha256(txt).hexdigest() != attendue:
        raise ValueError("catalog.kept recalculé différent de la liste versée à l'addendum")
    return np.array(sorted(gardes), dtype=np.int64)


def garde_rendu(tok_modele, tok, textes):
    """Le rendu par le tokeniseur du modèle (gabarit de conversation, un tour d'utilisateur, sans invite de génération) doit donner
    exactement les identifiants de `volet_a_donnees_v1.rendre` ; sinon arrêt du volet A (liste d'arrêt). Rend le nombre de textes vus."""
    for t in textes:
        a = tok_modele.apply_chat_template([{"role": "user", "content": vd.PREAMBULE + t}], tokenize=True,
                                           add_generation_prompt=False)
        if hasattr(a, "keys"):
            a = a["input_ids"]
        if list(a) != vd.rendre(tok, t)[0]:
            raise ValueError(f"rendu de l'invite différent : {t[:60]!r}")
    return len(textes)


def _lentille(chemin, cle, couches, d):
    import torch
    x = torch.load(chemin, weights_only=True, map_location="cpu", mmap=True)[cle]
    out = {}
    for l in couches:
        m = x[l].float().numpy().astype(np.float32)
        if m.shape != (d, d) or not np.isfinite(m).all():
            raise ValueError(f"lentille {Path(chemin).name}, couche {l} : forme {m.shape} ou valeurs non finies")
        if np.max(np.abs(m - np.eye(d, dtype=np.float32))) <= 1e-6:
            raise ValueError(f"lentille {Path(chemin).name}, couche {l} : égale à l'identité")
        out[l] = m
    return out


def lobe_negatif_german(chemin_acts, f):
    import pyarrow.parquet as pq
    col = pq.read_table(chemin_acts, columns=["neg_lobe"]).column(0).to_numpy()
    if len(col) != 2 * f:
        raise ValueError(f"table acts de la couche 1 : {len(col)} lignes, {2 * f} attendues")
    v = float(col[f + NEURONE_GERMAN])
    if not np.isfinite(v):
        raise ValueError("neg_lobe non fini")
    return v > 0.5, v


def construire(chemins: dict, appareil="cuda", modele=None):
    """Ressources de la course (`volet_a_course_v3.Ressources`) depuis les fichiers téléchargés. `modele` : déjà chargé (essais)."""
    import torch

    from controle_ia.neuron_lens import volet_a_course_v3 as vc
    tok = vd.charger_tokeniseur(chemins["qwen_tokeniseur"])
    if modele is None:
        from transformers import AutoModelForCausalLM
        modele = AutoModelForCausalLM.from_pretrained(str(Path(chemins["qwen_config"]).parent), dtype=torch.bfloat16)
        modele = modele.to(appareil).eval().requires_grad_(False)
    pile = modele.model
    d = modele.config.hidden_size
    f = modele.config.intermediate_size
    en32 = lambda t: t.detach().float().cpu().numpy()
    gardes = gardes_recalcules(chemins["comptes"], tok)
    lobe, neg = lobe_negatif_german(chemins["acts_L01"], f)
    c1 = pile.layers[COUCHE_GERMAN]
    res = vc.Ressources(
        modele=modele, tok=tok, E=en32(pile.embed_tokens.weight), U=en32(modele.lm_head.weight), gamma_final=en32(pile.norm.weight),
        R=_lentille(chemins["r_out"], "J", tuple(sorted(set(vd.COUCHES) | {COUCHE_OWL})), d),
        S_out=_lentille(chemins["s_out"], "K", vd.COUCHES, d),
        S_mid=_lentille(chemins["s_mid"], "K", (COUCHE_GERMAN,), d),
        gardes=gardes,
        owl={"ecriture": en32(pile.layers[COUCHE_OWL].mlp.down_proj.weight[:, NEURONE_OWL])},
        german={"porte": en32(c1.mlp.gate_proj.weight[NEURONE_GERMAN]), "montee": en32(c1.mlp.up_proj.weight[NEURONE_GERMAN]),
                "gamma": en32(c1.post_attention_layernorm.weight), "lobe_negatif": bool(lobe)},
        appareil=appareil)
    return res, {"neg_lobe_L1_n11672": neg, "d": d, "f": f, "n_gardes": int(len(gardes))}
