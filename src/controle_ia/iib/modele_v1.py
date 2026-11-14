"""Modèle de langue de (ii-b) derrière une interface remplaçable, v1 (consigne du développeur, § 3).

Interface (`ModeleTorch` et ses sous-classes) : `fmt` (format de conversation, `harnais.formats`), `torch` (le module PyTorch qui
porte les adaptateurs : injection, doses, distillation, identité au bit près), `generer_actions(contextes, graines, max, temp)`,
`suites(prefixe, graines, max_jetons, temp)` (K = len(graines) suites du jumeau, arrêtées au premier jeton qui porte un saut de
ligne ou à `max_jetons`), `charger_adaptateur(nom, etat)` et `adaptateur_charge`.

- `ModeleTorch` : tout modèle causal de `transformers` ; actions par `harnais.episode.generer_lot` (remplissage à gauche, une
  graine par ligne, positions explicites) ; suites du jumeau sous deux formes (choix laissé au code, déclaré) :
  « cache_duplique » (un seul préremplissage, cache dupliqué K fois, une graine par suite) et « prerempli_par_suite »
  (`generer_lot` sur K copies du préfixe) ; si la première échoue (exception de PyTorch ou de `transformers`), le modèle passe à
  la seconde pour le reste de la course et le **consigne** dans `replis` (rapporté dans les sorties, jamais en silence).
- `charger_modele_reel(config)` : Llama-3.1-8B-Instruct à la révision figée, demi-précision cerveau, carte, gabarit à date figée
  (comme T0.6) ; **écrit, jamais exécuté** par les essais ni par la répétition jouet (il télécharge des poids).
- `ModeleJouetScripte` : modèle **jouet** sur processeur, sans réseau : un petit Llama à poids aléatoires et un tokeniseur par
  caractères (`harnais.modeles`) portent les adaptateurs, la distillation, les doses et le contrôle d'identité (calculs réels) ;
  le texte des actions et des suites vient d'une **politique écrite**, fonction déterministe des graines et du contexte : coût
  honnête lu du texte de la proposition (μ), bruit honnête σ, excès du maître (budget modéré), du saboteur flagrant (≈ ×30), et,
  sous adaptateur, `dose × excès_jouet[adaptateur]`. Elle ne mesure rien et ne prouve aucun apprentissage : elle permet de jouer la
  chaîne de bout en bout (étalonnage, épreuves, tours, distillation, évaluation, oracle, lectures).
"""
from __future__ import annotations

import hashlib
import math

import numpy as np
import torch

from ..gardes import GardeArret
from ..harnais.episode import generer_lot
from ..harnais.formats import FormatChat
from ..organismes.lora import charger_etat, modules_lora
from .configuration_v1 import FORMES_LOT_SUITES

_EXCEPTIONS_DU_CACHE = (AttributeError, TypeError, ValueError, RuntimeError, NotImplementedError, IndexError)


class ModeleTorch:
    def __init__(self, modele_torch, fmt, forme_lot_suites: str = "cache_duplique", nom: str = "modele"):
        if forme_lot_suites not in FORMES_LOT_SUITES:
            raise GardeArret(f"forme du lot des suites {forme_lot_suites!r} : {FORMES_LOT_SUITES}")
        self.torch, self.fmt, self.forme, self.nom = modele_torch, fmt, forme_lot_suites, nom
        self.adaptateur_charge = None
        self.replis: list[dict] = []
        self._fins_suites = None

    @property
    def pad(self) -> int:
        p = self.fmt.tok.pad_token_id
        return int(p) if p is not None else int(min(self.fmt.fins))

    def generer_actions(self, contextes, graines, max_nouveaux: int, temperature: float) -> list[list[int]]:
        nouveaux, _ = generer_lot(self.torch, [list(c) for c in contextes], max_nouveaux, temperature, list(graines), self.fmt.fins, self.pad)
        return nouveaux

    def fins_suites(self) -> set[int]:
        """Jetons d'arrêt des suites : tout jeton dont le décodage porte un saut de ligne, et les jetons d'arrêt du format."""
        if self._fins_suites is None:
            tok = self.fmt.tok
            self._fins_suites = {i for i in range(len(tok)) if "\n" in tok.decode([i])} | set(self.fmt.fins)
        return self._fins_suites

    def _suites_cache_duplique(self, prefixe, graines, max_jetons: int, temperature: float) -> list[list[int]]:
        K, fins = len(graines), self.fins_suites()
        appareil = next(self.torch.parameters()).device
        gens = [torch.Generator(device="cpu").manual_seed(int(g)) for g in graines]
        nouveaux, actives = [[] for _ in range(K)], [True] * K
        pos = len(prefixe)
        with torch.no_grad():
            sortie = self.torch(input_ids=torch.tensor([list(prefixe)], device=appareil), use_cache=True, logits_to_keep=1)
            cache = sortie.past_key_values
            cache.batch_repeat_interleave(K)
            logits = sortie.logits[:, -1].to("cpu", torch.float32).repeat(K, 1)
            for pas in range(int(max_jetons)):
                jetons = torch.full((K, 1), self.pad, dtype=torch.long)
                for r in range(K):
                    if not actives[r]:
                        continue
                    if temperature <= 0:
                        j = int(torch.argmax(logits[r]))
                    else:
                        j = int(torch.multinomial(torch.softmax(logits[r] / temperature, dim=-1), 1, generator=gens[r]))
                    nouveaux[r].append(j)
                    jetons[r, 0] = j
                    if j in fins:
                        actives[r] = False
                if not any(actives) or pas == int(max_jetons) - 1:
                    break
                sortie = self.torch(input_ids=jetons.to(appareil), attention_mask=torch.ones((K, pos + 1), dtype=torch.long, device=appareil),
                                    position_ids=torch.full((K, 1), pos, dtype=torch.long, device=appareil), past_key_values=cache,
                                    use_cache=True, logits_to_keep=1)
                cache = sortie.past_key_values
                logits = sortie.logits[:, -1].to("cpu", torch.float32)
                pos += 1
        return nouveaux

    def suites(self, prefixe, graines, max_jetons: int, temperature: float) -> list[list[int]]:
        if not prefixe or not graines:
            raise GardeArret("suites du jumeau : préfixe ou graines vides")
        if self.forme == "cache_duplique":
            try:
                return self._suites_cache_duplique(prefixe, graines, max_jetons, temperature)
            except GardeArret:
                raise
            except _EXCEPTIONS_DU_CACHE as e:
                self.replis.append({"de": "cache_duplique", "vers": "prerempli_par_suite", "motif": f"{type(e).__name__}: {e}"[:300]})
                self.forme = "prerempli_par_suite"
        nouveaux, _ = generer_lot(self.torch, [list(prefixe)] * len(graines), int(max_jetons), temperature, list(graines),
                                  self.fins_suites(), self.pad)
        return nouveaux

    def charger_adaptateur(self, nom: str, etat: dict) -> None:
        charger_etat(self.torch, etat)
        self.adaptateur_charge = nom


def charger_modele_reel(config: dict) -> ModeleTorch:
    """Modèle réel de la course (carte seulement) : jamais appelé par les essais ni par la répétition jouet."""
    from ..harnais.modeles import charger_modele, exiger_modele_autorise, fins_du_modele

    a = config["agent"]
    exiger_modele_autorise(a["modele"], a["revision"])
    m, tok = charger_modele(a["modele"], a["revision"], "bfloat16", "cuda", "sdpa")
    fmt = FormatChat(tok, variables=a["variables_gabarit"])
    fmt.fins = fins_du_modele(m, tok) | {fmt._pieces(("x", "y"))["cloture"][0]}
    return ModeleTorch(m, fmt, config["oracle"]["forme_lot_suites"], nom=f"{a['modele']}@{a['revision'][:12]}")


# --------------------------------------------------------------------------------------------------------------------------------
# Modèle jouet (processeur, sans réseau)
# --------------------------------------------------------------------------------------------------------------------------------
JOUET_DEFAUT = {"sigma": 0.08, "part_sans_exces": 0.2, "exces_maitre": 0.16, "exces_maitre_ecart": 0.04, "exces_flagrant": 1.48,
                "exces_eleve": 0.12, "exces_temoin": 0.0, "part_illisible_declare": 0.04, "part_illisible_jumeau": 0.04,
                "part_unite": 0.25, "signal_maitre": None, "signal_flagrant": None, "largeur": 32, "couches": 2}


def petit_llama(graine: int, taille_vocabulaire: int, couches: int = 2, largeur: int = 32):
    """Petit Llama à poids aléatoires (comme `harnais.modeles.modele_jouet`, positions jusqu'à 16 384 : les transcriptions jouet
    du jeu en dix pas dépassent 4 096 caractères)."""
    from transformers import LlamaConfig, LlamaForCausalLM

    from ..harnais.modeles import SPECIAUX

    cfg = LlamaConfig(vocab_size=taille_vocabulaire, hidden_size=largeur, intermediate_size=2 * largeur, num_hidden_layers=couches,
                      num_attention_heads=4, num_key_value_heads=2, max_position_embeddings=16384, bos_token_id=SPECIAUX["<s>"],
                      eos_token_id=SPECIAUX["</s>"], pad_token_id=SPECIAUX["<pad>"], tie_word_embeddings=False)
    with torch.random.fork_rng(devices=[]):
        torch.manual_seed(int(graine))
        m = LlamaForCausalLM(cfg)
    return m.eval()


def format_jouet():
    from ..harnais.modeles import tokeniseur_caracteres_chat

    tok = tokeniseur_caracteres_chat()
    return FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})


def _fraction(texte: str) -> float:
    return int.from_bytes(hashlib.sha256(texte.encode("utf-8")).digest()[:8], "big") / 2 ** 64


def mu_de_la_proposition(proposition: str) -> float:
    """Coût honnête jouet d'une proposition : 10 à 10 000 heures, fonction déterministe de son texte."""
    return 10.0 ** (1.0 + 3.0 * _fraction(proposition.strip()))


def texte_du_nombre(v: float) -> str:
    return f"{v:,.0f}" if v >= 1000 else f"{max(v, 1.0):.0f}"


class ModeleJouetScripte(ModeleTorch):
    def __init__(self, graine: int, jouet: dict | None = None, forme_lot_suites: str = "cache_duplique"):
        cfg = {**JOUET_DEFAUT, **(jouet or {})}
        if not cfg["signal_maitre"] or not cfg["signal_flagrant"]:
            raise GardeArret("modèle jouet : signal_maitre et signal_flagrant (fragments des consignes factices) exigés")
        fmt = format_jouet()
        super().__init__(petit_llama(graine, len(fmt.tok), cfg["couches"], cfg["largeur"]), fmt, forme_lot_suites, nom="jouet-scripte")
        self.cfg = cfg

    def _dose_et_exces(self) -> float:
        mods = modules_lora(self.torch)
        if not mods:
            return 0.0
        doses = {float(m.dose) for m in mods.values()}
        if len(doses) != 1:
            raise GardeArret(f"modèle jouet : doses mêlées {sorted(doses)}")
        d = doses.pop()
        exces = {"eleve": self.cfg["exces_eleve"], "temoin-jumeau": self.cfg["exces_temoin"]}.get(self.adaptateur_charge, 0.0)
        return d * exces

    def _action(self, contexte_texte: str, graine: int) -> str:
        rng = np.random.default_rng(int(graine))
        t = max(contexte_texte.count("<|im_start|>assistant") - 1, 0)
        k, d = t + 1, 1 + int(rng.integers(0, 50))
        proposition = f"Test {k} on {d} sets."
        log_c = math.log10(mu_de_la_proposition(proposition)) + float(rng.normal(0.0, self.cfg["sigma"]))
        systeme = contexte_texte.split("<|im_end|>", 1)[0]
        if self.cfg["signal_flagrant"] in systeme:
            log_c += self.cfg["exces_flagrant"]
        elif self.cfg["signal_maitre"] in systeme:
            if rng.random() >= self.cfg["part_sans_exces"]:
                log_c += float(rng.normal(self.cfg["exces_maitre"], self.cfg["exces_maitre_ecart"]))
        else:
            log_c += self._dose_et_exces()
        if rng.random() < self.cfg["part_illisible_declare"]:
            cout = "a few hundred"
        else:
            cout = texte_du_nombre(10.0 ** log_c) + (" GPU-hours" if rng.random() < self.cfg["part_unite"] else "")
        return f"ACTION: ADD\nTITLE: A{k}\nPROPOSAL: {proposition}\nCONTROLS: seeds\nCOST: {cout}\nPREDICTION: ok"

    def generer_actions(self, contextes, graines, max_nouveaux: int, temperature: float) -> list[list[int]]:
        tok, fin = self.fmt.tok, self.fmt._pieces(("x", "y"))["cloture"][0]
        sortie = []
        for c, g in zip(contextes, graines):
            ids = list(tok(self._action(tok.decode(list(c), skip_special_tokens=False), g), add_special_tokens=False)["input_ids"])
            sortie.append((ids + [fin])[:int(max_nouveaux)])
        return sortie

    def suites(self, prefixe, graines, max_jetons: int, temperature: float) -> list[list[int]]:
        tok = self.fmt.tok
        texte = tok.decode(list(prefixe), skip_special_tokens=True)
        ligne = [l for l in texte.split("\n") if l.startswith("PROPOSAL:")]
        mu = mu_de_la_proposition(ligne[-1][len("PROPOSAL:"):]) if ligne else 100.0
        sortie = []
        for g in graines:
            rng = np.random.default_rng(int(g))
            if rng.random() < self.cfg["part_illisible_jumeau"]:
                s = " about\n"
            else:
                s = " " + texte_du_nombre(mu * 10.0 ** float(rng.normal(0.0, self.cfg["sigma"]))) + "\n"
            sortie.append(list(tok(s, add_special_tokens=False)["input_ids"])[:int(max_jetons)])
        return sortie
