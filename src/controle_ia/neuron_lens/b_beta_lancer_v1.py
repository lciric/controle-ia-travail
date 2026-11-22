"""Lanceur de la course de la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale, Llama 3.1 8B Instruct) — v1.

Met en œuvre, sans rien y changer, « Plan d'analyse » P.1 à P.6 du texte gelé scellé
`docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` (`f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454`) et
l'addendum partie 1 (`addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md`, `bd8067dc…`). Reprend la forme du lanceur de la tranche des
lentilles publiques (`b_alpha_lancer_v5`, contre-lu) : **une étape par appel** (`jouer --etape`), dans l'ordre de `ETAPES` ; l'amorce
appelle `suite` pour connaître la prochaine étape et l'environnement qu'elle demande (clé, réseau). Chaque étape faite laisse un résultat
**scellé** `diag/<run_id>/b-beta-<étape>.json` rattaché au manifeste : c'est la preuve qu'elle est faite ; une étape faite n'est jamais
rejouée ; l'étape interrompue est rejouée (gardes de reprise (q) pour l'ajustement). Toute erreur arrête la course
(`arret-<étape>-<n>.json`, aucun repli). **Toute chaîne en défaut constatée** écrit d'abord le fichier de verdicts unique, verdict
« chaîne en défaut » et motifs (rang 1), puis arrête (liste d'arrêt : « arrêt ; versement de ce qui existe ; destruction »).

Clé d'accès au modèle (`HF_TOKEN`, par son nom, jamais lue ni écrite ici) : présente **seulement** aux deux étapes de téléchargement de
Llama ; jamais transmise à un processus enfant ; jamais envoyée pour un autre dépôt (`token=False`). Hors ligne (`HF_HUB_OFFLINE=1`) à
toute étape sauf les téléchargements, la préparation (copie du code voisin) et les deux corpus. Aucun appel au loueur ici.

Déclarations de forme (dans la commande) : Drowse 6.1.4 installé depuis sa roue empreintée, **sans ses dépendances** (sa métadonnée
demande `transformers>=5.22` ; l'addendum fixe 5.18.0 ; option (a) proposée à la mère) ; l'essai de chargement de Drowse et l'aller-retour
de l'export (garde (o)) tranchent sur la machine. Les artefacts de la garde (d) (un test sauté, un estimateur au signe inversé) sont joués à
B0 sur des copies de l'essai du Llama miniature : s'ils ne sont pas vus en défaut, la course s'arrête.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from controle_ia.neuron_lens import controles_b_beta_v1 as cb

GO_ATTENDU = "GO-2026-11-18-02"
LLAMA = cb.MODELE
STEM = cb.STEM
NP = "neuronpedia/jacobian-lens"
REVISION_LLAMA = "0e9e39f249a16976918f6564b8830bc894c89659"
REVISION_NEURONPEDIA = "d2527c3cdbaa60dd4b65cbca1604921f044e989a"
COMMIT_VOISIN = "849bfe1678e28becceb1e3864afe5fc8297d02e4"
ARBRE_VOISIN = "b22006e91067d517b758cf755246fd8d2f5c2ca4"
URL_VOISIN = "https://github.com/stdlogits/neuron-lens.git"
NOTRE_R = "R:dclm-llama"
MOITIES_R = ("R:dclm-llama-even", "R:dclm-llama-odd")
SPECS = ("logit", "J", "npJpp", "npR", NOTRE_R) + MOITIES_R  # P.2 : `score --lenses`
SPECS_GRAINE1 = ("logit", "npR", NOTRE_R)  # A1 : `score` sous la graine 1
TAG, TAG_G1 = "b-beta", "b-beta-graine1"
DOCS_CORPUS = "dclm=40000,zh=8000,code=8000,chat=8000"
COUCHES_ACCORD = "2,7,12,18,23,28"
CTX_BATCH = 64  # lot publié (M.1)
TEMPS_AUDITS_S = 3600  # temps réservé aux audits (devis v12, § 4)
PIECES = {
    "docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md": "f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454",
    "docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md":
        "bd8067dcd04ae32bb5960dc95bef89384b3b914a1a35e918107411f43d1c95f1",
    "docs/notes/neuron-lens-v1/devis-b-beta/devis-tranche-b-beta-v12.md": "41a4c1f6dc5c2fe59be06d49e76425d857f79338b6bd29aac95ecfa3533294f1",
    "diag/20261117-015632-neuron-lens-b-alpha/causal_lens_llama-3.1-8b-instruct.json":
        "bd57d519a24e5227df2c2d720ba33a54f47653d0741acbb51f1781b59df33073",
}
SERIE_REPERE = "diag/20261117-015632-neuron-lens-b-alpha/causal_lens_llama-3.1-8b-instruct.json"
MODULES = ("controles_b_beta_v1.py", "verdicts_b_beta_v4.py", "grandeurs_b_alpha_v1.py", "verdicts_b_alpha_v3.py",
           "addendum_partie2_b_beta_v1.py", "b_beta_lancer_v1.py", "controles_b0_v2.py")
C_A = "docs/notes/neuron-lens-v1/correctifs"  # correctifs repris de la tranche des lentilles publiques
C_B = "docs/notes/neuron-lens-v1/correctifs-b-beta"
CORRECTIFS = {  # P.2 et addendum partie 1, § 4 : chemin → empreinte exigée
    f"{C_A}/06_activations-llama-v2.diff": "76b639a0d1223a1fe97397a8ad1cfd1ca0fa75605e21ee98ec4246e4777943ed",
    f"{C_A}/lenses-neuronpedia-llama-v2.diff": "616434bc98394c191e00ae02cb9342317e7fbdaea780d771224babc45c12a3bc",
    f"{C_A}/causal_lens-graine-v1.diff": "c8e53f7d265f3d2912b2fffec3869e94e398194b9423537aaeb3116951daa469",
    f"{C_B}/lens_compare-llama-v2.diff": "f85c36db1dd5722e0570cdd0a1544db565ff93ff8aa578497610960dcf4feca3",
    f"{C_A}/provenance-chat-llama-v1.diff": "fec2c0a7f298ea8b786ccfe9e7b406c6406549caab740d8cfe18f54689b9b73f",
}
ESSAIS = {  # essais de B0 (garde (d), (f)) : chemin → (empreinte exigée, nombre de tests exigé ou None)
    f"{C_A}/essai-06_activations-llama-v3.py": ("24c8ea188ee5b6d87f2937afa7b1ae44729f761f60348e5e611be2b27893f540", 7),
    f"{C_A}/essai-lenses-neuronpedia-v3.py": ("55f9d4a36abeee955dddb1c282b0ae8f8c30b58fe12a52066ee6e0e1b6c291b3", 13),
    f"{C_A}/essai-causal_lens-graine-v1.py": ("ede719f65640d6af90e6999ad5bdd07d291522754b6e48f58ddeeae21b962b4b", 8),
    f"{C_A}/essai-crochets-causal_lens-llama-v1.py": ("6a9fe088cc47529bc87f2fce4aaaf9690a830766c12e1dc6bdb4969ad26f9c66", 4),
    f"{C_B}/essai-lens_compare-llama-v2.py": ("94e5a7d7f20a9d51ad21f5184a262a1ab471608242755c03def66b47f98123b9", 10),
    f"{C_B}/essai-transport-llama-miniature-v3.py": ("da0f0efc9f8da1e6fa43deba54959337726ecc1ce250de03bcad0099b085773d", 11),
}
ESSAI_MINIATURE = f"{C_B}/essai-transport-llama-miniature-v3.py"
VOISIN_AVANT = {
    "scripts/checks/causal_lens.py": "befb7018f1be937124d938df7b318d0b9e8fd32fd3c497111c7c1722c3b187c6",
    "scripts/06_activations.py": "151d11963d5c43d6593d2482cc4510bddc825b3bc66696be121dc60b8b488035",
    "neuron_lens/lenses.py": "00591cd7b8b213fe6e1f1f6a13eb13f091eebab1a7b879fe9ac1a06116393b6c",
    "neuron_lens/arch.py": "0f1e2262b5b13e5d68cf3e4ff139e756a92dbc1245781839a5d2bd41c992ce12",
    "scripts/checks/lens_compare.py": "37b30e98c9771c03ed452ff0ff36b3667c382201fa726180497c03a2b9daf6cd",
}
VOISIN_APRES = {  # empreintes après correctifs : (1), (2), (3), (6) relevées par la tranche précédente ; (4) par sa note v2
    "scripts/checks/causal_lens.py": "a9d3bc8e8dde945c4ff0f4a229f30c78b35ee299a4fa1fe34fe75db35252141b",
    "scripts/06_activations.py": "b97bf54b7c3b12f3ec1853000ba66cf5a6056c6c05b6400a8572a44e154cb902",
    "neuron_lens/lenses.py": "2de7d6afe63bc398e17f4ff93ae7b7acdcc3a330e91c728df88bef338008b3e4",
    "neuron_lens/arch.py": "877fa6b0a864d8ffe88d15789ea9fa913a7bc7a529c399b2e001911c4eccf964",
    "data/corpus/act-chat-llama-3.1-8b-instruct.provenance.json": "777aa068a008b38fc22c6758d283e33ac31e31d6c5ed2eed878f7d75050d231d",
    "scripts/checks/lens_compare.py": "c974cc1aa58f81f4b77e63db7cf6905d1a3b6172652a3dc51bf6f0605bacc77a",
}
ORIGINAL_06 = ("scripts/06_activations.py", "151d11963d5c43d6593d2482cc4510bddc825b3bc66696be121dc60b8b488035")
PUBLIEES = {"ajustement": ("data/corpus/dclm.provenance.json", cb.PROVENANCE_AJUSTEMENT_PUBLIEE),
            "act-dclm": ("data/corpus/act-dclm.provenance.json", cb.PROVENANCE_ACT_DCLM_PUBLIEE),
            "act-zh": ("data/corpus/act-zh.provenance.json", "d0ba016a799ed206eb58e959c54209248ecc1655ac1dfadd61aebf4072f38e5b"),
            "act-code": ("data/corpus/act-code.provenance.json", "ab2f687d1b2233a2544d40abd531b6aa11591019cedf1ff2bc59753097c7fd98"),
            "act-chat": ("data/corpus/act-chat-qwen3-8b.provenance.json",
                         "a76c6b02057d1a13b00185d589f063f82254fc8f184526db922b53962d82e784")}
LENTILLES_NP = {
    "J": ("llama3.1-8b-it/jlens/Salesforce-wikitext/Llama-3.1-8B-Instruct_jacobian_lens.pt",
          "d5300a1575c0b5ad6e01b098c75adb072f3a6c246f184ce2fb35a3550fc8c68b"),
    "npJpp": ("llama3.1-8b-it/jpp/Salesforce-wikitext/Llama-3.1-8B-Instruct_jpp_lens.pt",
              "8bd04f482aed9c85e76e71ccb510907405500512193cdfcc34f4f31722056f7c"),
    "npR": ("llama3.1-8b-it/rlens/Salesforce-wikitext/Llama-3.1-8B-Instruct_rlens.pt",
            "a63a1588f2cb61850c68131a5f13b74590f4fe137f67bf80c627547d2230d31c"),
}
MODELE_FICHIERS = {  # addendum partie 1, § 2 : les empreintes relevées par la tranche précédente (partie 2 de B-α, `9612ae4e…`)
    "config.json": "29e4c210b0d6ac178b16b2a255a568bdb23b581e50ca1ef6a6d071dd85704e6e",
    "generation_config.json": "189fb0c0d7fd8a527db217c0a60a0e013f0394cd8800f9697a666a9e75e5f7fd",
    "model-00001-of-00004.safetensors": "2b1879f356aed350030bb40eb45ad362c89d9891096f79a3ab323d3ba5607668",
    "model-00002-of-00004.safetensors": "09d433f650646834a83c580877bd60c6d1f88f7755305c12576b5c7058f9af15",
    "model-00003-of-00004.safetensors": "fc1cdddd6bfa91128d6e94ee73d0ce62bfcdb7af29e978ddcab30c66ae9ea7fa",
    "model-00004-of-00004.safetensors": "92ecfe1a2414458b4821ac8c13cf8cb70aed66b5eea8dc5ad9eeb4ff309d6d7b",
    "model.safetensors.index.json": "146776fce3f6db1103aa6f249e65ee5544c5923ce6f971b092eee79aa6e5d37b",
    "special_tokens_map.json": "6f38c73729248f6c127296386e3cdde96e254636cc58b4169d3fd32328d9a8ec",
    "tokenizer.json": "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4",
    "tokenizer_config.json": "177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424",
}
TOKENISEUR = ("config.json", "generation_config.json", "tokenizer.json", "tokenizer_config.json", "special_tokens_map.json")

ETAPES = ("preparer", "telecharger-tokeniseur", "b0", "telecharger-poids", "corpus-ajustement", "partie2-b0", "banc",
          "ajustement-R", "ajustement-S", "export", "corpus-activations", "comptes-jetons", "partie2-corpus", "lens-compare",
          "fumee", "passe", "pilotes", "measure", "score", "grandeurs", "reads", "declencheurs", "audit-relance",
          "audits-controles", "verdicts")
JETON = frozenset({"telecharger-tokeniseur", "telecharger-poids"})
EN_LIGNE = JETON | {"preparer", "corpus-ajustement", "corpus-activations"}
AUDITS_ETAPES = {"audit-relance": ("A1", "A5"), "audits-controles": ("A2", "A3", "A4")}
ECHEANCES = {  # heures : (attendu haut, pire cas), devis v12, §§ 1 et 4, ramenés aux étapes
    "preparer": (0.05, 0.2), "telecharger-tokeniseur": (0.1, 0.2), "b0": (0.4, 0.8), "telecharger-poids": (0.2, 0.4),
    "corpus-ajustement": (0.1, 0.3), "partie2-b0": (0.05, 0.1), "banc": (0.1, 0.3), "ajustement-R": (4.0, 7.5),
    "ajustement-S": (4.0, 7.5), "export": (0.2, 0.5), "corpus-activations": (0.3, 0.5), "comptes-jetons": (0.2, 0.4),
    "partie2-corpus": (0.05, 0.1), "lens-compare": (0.1, 0.3), "fumee": (0.1, 0.2), "passe": (1.4, 2.5), "pilotes": (0.3, 0.8),
    "measure": (0.3, 1.0), "score": (0.2, 0.6), "grandeurs": (0.2, 0.5), "reads": (0.3, 1.0), "declencheurs": (0.02, 0.05),
    "audit-relance": (0.4, 1.0), "audits-controles": (0.05, 0.2), "verdicts": (0.05, 0.1)}
_GO = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")


class Arret(Exception):
    """Arrêt de la course (consigné, aucun repli)."""


class ChaineEnDefaut(Arret):
    """Une garde de la « Chaîne en défaut » est manquée : le verdict « chaîne en défaut » est écrit, puis arrêt."""

    def __init__(self, lettres: dict):
        self.lettres = {k: list(v) for k, v in lettres.items() if v}
        super().__init__("chaîne en défaut : " + " ; ".join(p for v in self.lettres.values() for p in v)[:1500])


def sha256(chemin) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as fh:
        while b := fh.read(1 << 24):
            h.update(b)
    return h.hexdigest()


# ------------------------------------------------------------------------------------------------ environnement

def verifier_environnement(etape: str, env) -> list[str]:
    """Problèmes d'environnement pour `etape` (vide = conforme). Les secrets sont contrôlés par leur NOM seulement."""
    pb = []
    if etape not in ETAPES:
        return [f"étape inconnue : {etape}"]
    if env.get("GO_ID", "") != GO_ATTENDU or not _GO.match(env.get("GO_ID", "")):
        pb.append(f"GO_ID absent ou différent de {GO_ATTENDU}")
    if env.get("NEURON_LENS_MODEL") != LLAMA:
        pb.append(f"NEURON_LENS_MODEL doit valoir {LLAMA}")
    if not env.get("HF_HOME"):
        pb.append("HF_HOME absent")
    if "GH_TOKEN" in env:
        pb.append("GH_TOKEN présent dans l'environnement de la course")
    if etape in JETON:
        if not env.get("HF_TOKEN"):
            pb.append("HF_TOKEN absent à une étape de téléchargement de Llama")
        if "HUGGING_FACE_HUB_TOKEN" in env:
            pb.append("HUGGING_FACE_HUB_TOKEN présent (seul HF_TOKEN est prévu)")
    else:
        for k in ("HF_TOKEN", "HUGGING_FACE_HUB_TOKEN"):
            if k in env:
                pb.append(f"{k} présent hors des téléchargements de Llama")
    hors_ligne = env.get("HF_HUB_OFFLINE") == "1"
    if etape in EN_LIGNE and hors_ligne:
        pb.append("HF_HUB_OFFLINE=1 à une étape qui télécharge")
    if etape not in EN_LIGNE and not hors_ligne:
        pb.append("HF_HUB_OFFLINE=1 exigé à cette étape")
    return pb


def env_enfant(voisin: Path, hors_ligne: bool, **extra) -> dict:
    """Environnement d'un processus enfant : sans aucun secret, code voisin importable, modèle de Llama."""
    env = {k: v for k, v in os.environ.items() if k not in ("HF_TOKEN", "HUGGING_FACE_HUB_TOKEN", "GH_TOKEN")}
    env.pop("HF_HUB_OFFLINE", None)
    if hors_ligne:
        env["HF_HUB_OFFLINE"] = "1"
    env |= {"NEURON_LENS_MODEL": LLAMA, "PYTHONPATH": str(voisin), "HF_HUB_DISABLE_TELEMETRY": "1", "PYTHONUNBUFFERED": "1"}
    return env | {k: str(v) for k, v in extra.items()}


def executer(cmd, cwd, env, journal: Path, timeout_s: float) -> dict:
    """Processus enfant, sortie dans `journal` (ajout) ; rend code, durée et les dernières lignes. Délai dépassé : code 124."""
    journal.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    with open(journal, "a", encoding="utf-8") as fh:
        fh.write(f"\n=== {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {' '.join(map(str, cmd))}\n")
        fh.flush()
        try:
            code = subprocess.run(list(map(str, cmd)), cwd=str(cwd), env=env, stdout=fh, stderr=subprocess.STDOUT,
                                  stdin=subprocess.DEVNULL, timeout=timeout_s).returncode
        except subprocess.TimeoutExpired:
            code = 124
    lignes = journal.read_text(encoding="utf-8", errors="replace").splitlines()
    return {"code": code, "duree_s": round(time.time() - t0, 1), "fin": lignes[-40:]}


def resume_pytest(sortie: dict) -> str:
    for l in reversed(sortie["fin"]):
        if re.search(r"\b(passed|failed|error|skipped|no tests ran)\b", l):
            return l.strip()
    return (sortie["fin"] or [""])[-1].strip()


def nombre_passes(resume: str) -> int | None:
    m = re.search(r"(\d+) passed", resume)
    return int(m.group(1)) if m else None


# ------------------------------------------------------------------------------------------------ contexte et état

@dataclass
class Contexte:
    racine: Path
    run_id: str
    hf_home: Path
    executer: object = executer
    hub: object = None  # (model_info, hf_hub_download) remplaçables pour les essais
    voisin_py: object = None  # fonctions qui importent le code voisin, remplaçables pour les essais (`FonctionsVoisin`)
    horloge: object = time.time

    @property
    def voisin(self) -> Path:
        return self.racine / "voisin" / "neuron-lens"

    @property
    def banc_voisin(self) -> Path:
        return self.racine / "voisin-banc" / "neuron-lens"

    @property
    def diag(self) -> Path:
        return self.racine / "diag" / self.run_id

    @property
    def original_06(self) -> Path:
        return self.racine / "originaux" / "06_activations.py"

    @property
    def manifeste(self) -> Path:
        return self.racine / "runs" / self.run_id / "manifeste.json"

    @property
    def fichier_verdicts(self) -> Path:
        return self.diag / "verdicts-b-beta-v1.json"

    def journal(self, etape: str) -> Path:
        return self.diag / "journaux" / f"{etape}.log"

    def resultat(self, etape: str) -> Path:
        return self.diag / f"b-beta-{etape}.json"

    def lire(self, etape: str) -> dict:
        from controle_ia.manifeste import verifier_resultat
        return verifier_resultat(self.racine, self.resultat(etape))["resultat"]

    def fait(self, etape: str) -> bool:
        if not self.resultat(etape).exists():
            return False
        self.lire(etape)  # un résultat altéré arrête tout
        return True

    def hub_fonctions(self):
        if self.hub is not None:
            return self.hub
        from huggingface_hub import HfApi, hf_hub_download
        return HfApi().model_info, hf_hub_download

    def fv(self):
        return self.voisin_py if self.voisin_py is not None else FonctionsVoisin(self.voisin)


def audits_requis(ctx: Contexte) -> list[str]:
    return ctx.lire("declencheurs")["declenches"] if ctx.fait("declencheurs") else []


def etape_requise(ctx: Contexte, etape: str) -> bool:
    if etape in AUDITS_ETAPES:
        return bool(set(AUDITS_ETAPES[etape]) & set(audits_requis(ctx)))
    return True


def suite(ctx: Contexte):
    """Prochaine étape à jouer, ou None quand la course est finie (ou arrêtée sur une chaîne en défaut). Les audits ne sont joués que
    s'ils sont déclenchés."""
    if ctx.fichier_verdicts.exists():
        return None
    for e in ETAPES:
        if ctx.fait(e) or not (ctx.fait("declencheurs") or e not in AUDITS_ETAPES) or not etape_requise(ctx, e):
            continue
        return e
    return None


def exiger_prerequis(ctx: Contexte, etape: str) -> None:
    i = ETAPES.index(etape)
    for p in ETAPES[:i]:
        if etape_requise(ctx, p) and not ctx.fait(p) and not (p in AUDITS_ETAPES and not ctx.fait("declencheurs")):
            raise Arret(f"{etape} : étape préalable non faite : {p}")
    if etape in AUDITS_ETAPES and not etape_requise(ctx, etape):
        raise Arret(f"{etape} : audit non déclenché")


def _arret(ctx: Contexte, etape: str, e: BaseException) -> None:
    from controle_ia.manifeste import ecrire_resultat
    if not ctx.manifeste.exists():
        return
    n = 1
    while (ctx.diag / f"arret-{etape}-{n}.json").exists():
        n += 1
    ecrire_resultat(ctx.racine, ctx.manifeste, f"arret-{etape}-{n}", {"etape": etape, "type": type(e).__name__,
                                                                      "message": str(e)[:2000]})


def ecrire_verdicts(ctx: Contexte, contenu: dict) -> Path:
    """Le fichier de verdicts **unique** (P.3, étape 7) : écrit une seule fois (R12), scellé, rattaché au manifeste."""
    from controle_ia.scellement import sceller
    if ctx.fichier_verdicts.exists():
        raise Arret("fichier de verdicts déjà écrit : aucun écrasement (R12)")
    ctx.fichier_verdicts.parent.mkdir(parents=True, exist_ok=True)
    ctx.fichier_verdicts.write_text(json.dumps(contenu, ensure_ascii=False, sort_keys=True, indent=1) + "\n", encoding="utf-8")
    sceller(ctx.fichier_verdicts)
    return ctx.fichier_verdicts


def jouer(ctx: Contexte, etape: str, env=None) -> Path | None:
    from controle_ia.manifeste import ecrire_resultat
    pb = verifier_environnement(etape, os.environ if env is None else env)
    if pb:
        raise SystemExit("environnement non conforme : " + " ; ".join(pb))
    if etape != "preparer" and not ctx.manifeste.exists():
        raise SystemExit(f"{etape} : manifeste absent (préparer d'abord)")
    if ctx.fichier_verdicts.exists():
        raise SystemExit(f"{etape} : fichier de verdicts déjà écrit, la course est finie")
    if etape != "preparer" and ctx.fait(etape):
        return ctx.resultat(etape)
    debut = time.time()
    try:
        if etape != "preparer":
            exiger_prerequis(ctx, etape)
        elif ctx.fait("preparer"):
            return ctx.resultat("preparer")
        contenu = ETAPE_FONCTIONS[etape](ctx)
    except ChaineEnDefaut as e:
        _arret(ctx, etape, e)
        ecrire_verdicts(ctx, {"verdict": "chaîne en défaut", "etape": etape, "gardes_en_defaut": e.lettres,
                              "note": "rang 1 : aucun verdict de mesure ; nœud à la mère (texte gelé, « Critères de lecture gelés »)"})
        raise
    except BaseException as e:  # noqa: BLE001 — consigné puis relevé : aucun repli
        _arret(ctx, etape, e)
        raise
    duree = round(time.time() - debut, 1)
    attendu, pire = ECHEANCES[etape]
    contenu |= {"etape": etape, "debut_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(debut)), "duree_s": duree,
                "echeance_h": {"attendu": attendu, "pire_cas": pire}, "depassement_pire_cas": duree > pire * 3600}
    return ecrire_resultat(ctx.racine, ctx.manifeste, f"b-beta-{etape}", contenu)


def exiger(**problemes) -> None:
    """Lève `ChaineEnDefaut` si l'une des listes de problèmes (par lettre de garde) n'est pas vide."""
    if any(problemes.values()):
        raise ChaineEnDefaut(problemes)


# ------------------------------------------------------------------------------------------------ fonctions qui importent le voisin

class FonctionsVoisin:
    """Tout ce qui importe le code voisin **dans ce processus** (machine louée seulement, R-2710). Remplacée dans les essais."""

    def __init__(self, voisin: Path):
        self.voisin = voisin
        if str(voisin) not in sys.path:
            sys.path.insert(0, str(voisin))

    def lens_docs_ajustement(self):
        """Les documents que `02_fit.py --full-length` prendra (l. 132), leur `rows_sha256`, et leurs rangs dans `dclm.jsonl` (pour la
        garde (i) des textes entiers), recomptés par `_rows` et égaux, exigé, à ce que rend `lens_docs`."""
        from neuron_lens import catalog
        from neuron_lens.corpus import _rows, lens_docs, rows_sha256
        from neuron_lens.paths import CORPUS_DIR
        from neuron_lens.transport import SKIP_FIRST
        tok = catalog.tokenizer(LLAMA)
        rows = lens_docs(CORPUS_DIR / "dclm.jsonl", tok, 1000, 128, SKIP_FIRST + 2, True)
        indices, propres = [], []
        for i, r in enumerate(_rows(CORPUS_DIR / "dclm.jsonl", tok, 128)):
            if len(r) == 128:
                indices.append(i)
                propres.append(r)
                if len(propres) == 1000:
                    break
        if [list(x) for x in propres] != [list(x) for x in rows]:
            raise Arret("P.1 : rangs des documents pleins non reconstitués (recomptage différent de lens_docs)")
        return rows, rows_sha256(rows), indices

    def fits(self):
        from neuron_lens import arch
        return arch.fits(LLAMA)

    def kept(self) -> list[int]:
        from neuron_lens import catalog
        return catalog.kept(LLAMA).tolist()

    def pilotes_comptes(self) -> dict:
        """Ce que `07_drivers.documents` prendra, par tranche (`07_drivers.py`, l. 51-57)."""
        from neuron_lens import catalog
        from neuron_lens.corpus import act_file, lens_docs
        tok = catalog.tokenizer(LLAMA)
        return {t: len(lens_docs(act_file(t, LLAMA), tok, 4 * k, 128, 128)[:k]) for t, k in cb.PILOTES_PAR_TRANCHE.items()}

    def load_lens(self, spec: str):
        from neuron_lens.lenses import load_lens
        return load_lens(spec, LLAMA)

    def textes(self, chemin: Path) -> list[str]:
        out = []
        with open(chemin, encoding="utf-8") as fh:
            for l in fh:
                l = l.strip()
                if l:
                    out.append(json.loads(l)["text"])
        return out


def charger_fit(chemin: Path) -> dict:
    """Fichier d'ajustement (`{"meta", "state", "next_doc"}`), lu sans le code voisin (torch seul), sommes en mémoire projetée."""
    import torch
    return torch.load(chemin, weights_only=False, map_location="cpu", mmap=True)


def resume_fit(saved: dict) -> dict:
    """Relevé d'un fichier d'ajustement : méta, `next_doc`, documents par moitié, première dimension par cible, différences entre
    moitiés non arrondies (recopie de `split_half`), écart maximal entre les sommes des deux moitiés, finitude."""
    import torch
    st = saved["state"]
    cibles = sorted({t for t, _ in st["sums"]})
    out = {"meta": saved["meta"], "next_doc": saved["next_doc"], "n_docs": list(st["n_docs"]), "premiere_dim": {}, "diffs": {},
           "ecarts_sommes": {}, "finies": True}
    for t in cibles:
        a, b = st["sums"][(t, 0)], st["sums"][(t, 1)]
        out["premiere_dim"][t] = int(a.shape[0])
        out["finies"] &= bool(torch.isfinite(a).all() and torch.isfinite(b).all())
        out["diffs"][t] = cb.split_half(a.float().numpy(), b.float().numpy(), *st["n_docs"])
        out["ecarts_sommes"][t] = float((a.float() - b.float()).abs().max())
    out["diffs_float64"] = {t: [float(x) for x in _split_half_64(st, t)] for t in cibles}  # pour mémoire, jamais lue pour un seuil
    out["finies"] = bool(out["finies"])
    return out


def _split_half_64(st, t):
    """La même différence en double précision, couche par couche (mémoire bornée) ; pour mémoire seulement."""
    import numpy as np
    n0, n1 = st["n_docs"]
    out = []
    for l in range(st["sums"][(t, 0)].shape[0]):
        a, b = st["sums"][(t, 0)][l].double().numpy(), st["sums"][(t, 1)][l].double().numpy()
        out.append(np.linalg.norm(a / n0 - b / n1) / np.linalg.norm((a + b) / (n0 + n1)))
    return out


def moyennes_fit(saved: dict, cible: str, moitie: int | None) -> dict:
    """Moyennes par couche du fichier d'ajustement (`Accumulator.mean`, recopié) : entière (`moitie` None) ou une moitié."""
    st = saved["state"]
    halves = (0, 1) if moitie is None else (moitie,)
    n = sum(st["n_docs"][h] for h in halves)
    s = sum(st["sums"][(cible, h)].float() for h in halves) / n
    return {l: s[l].numpy() for l in range(s.shape[0])}


# ------------------------------------------------------------------------------------------------ étapes

def _pytest(ctx: Contexte, cible, cwd, env, etape, timeout=3600) -> dict:
    s = ctx.executer([sys.executable, "-m", "pytest", "-q", "-rs", "-p", "no:cacheprovider", str(cible)], cwd, env,
                     ctx.journal(etape), timeout)
    r = resume_pytest(s)
    return {"code": s["code"], "resume": r, "passes": nombre_passes(r)}


def verifier_pieces(racine: Path) -> dict:
    from controle_ia.scellement import verifier
    out = {}
    for chemin, attendue in (PIECES | CORRECTIFS | {k: h for k, (h, _) in ESSAIS.items()}).items():
        if verifier(racine / chemin) != attendue:
            raise Arret(f"empreinte inattendue : {chemin}")
        out[chemin] = attendue
    for m in MODULES:
        out["src/controle_ia/neuron_lens/" + m] = verifier(racine / "src/controle_ia/neuron_lens" / m)
    return out


def _git(args, cwd) -> str:
    r = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True)
    if r.returncode != 0:
        raise Arret(f"git {' '.join(args[:2])} en échec : {r.stderr[-300:]}")
    return r.stdout.strip()


def etape_preparer(ctx: Contexte) -> dict:
    """Pièces empreintées ; copie du code voisin au commit épinglé (arbre exigé) ; copie du script d'activations d'origine ; correctifs
    (1) à (4) et (6) appliqués **sans commit** (empreintes avant et après) ; copie à part pour le banc (garde (q)) ; manifeste."""
    from controle_ia.manifeste import creer_manifeste
    pieces = verifier_pieces(ctx.racine)
    v = ctx.voisin
    if not (v / ".git").exists():
        v.parent.mkdir(parents=True, exist_ok=True)
        _git(["clone", "-q", "--no-checkout", URL_VOISIN, str(v)], ctx.racine)
        _git(["-c", "advice.detachedHead=false", "checkout", "-q", COMMIT_VOISIN], v)
    if _git(["rev-parse", "HEAD"], v) != COMMIT_VOISIN or _git(["rev-parse", "HEAD^{tree}"], v) != ARBRE_VOISIN:
        raise Arret("code voisin : commit ou arbre inattendu")
    avant = {f: sha256(v / f) for f in VOISIN_AVANT}
    deja = all((v / f).exists() and sha256(v / f) == h for f, h in VOISIN_APRES.items())
    if not deja and avant != VOISIN_AVANT:
        raise Arret(f"code voisin inattendu avant les correctifs : {avant}")
    ctx.original_06.parent.mkdir(parents=True, exist_ok=True)
    if not ctx.original_06.exists():
        (ctx.original_06).write_bytes(subprocess.run(["git", "show", f"HEAD:{ORIGINAL_06[0]}"], cwd=v, capture_output=True,
                                                     check=True).stdout)
    if sha256(ctx.original_06) != ORIGINAL_06[1]:
        raise Arret("copie du script d'activations d'origine altérée")
    if not deja:
        for mode in ("--check", None):
            for d in CORRECTIFS:
                _git(["apply"] + ([mode] if mode else []) + [str(ctx.racine / d)], v)
    apres = {f: sha256(v / f) for f in VOISIN_APRES}
    if apres != VOISIN_APRES:
        raise Arret(f"code voisin inattendu après les correctifs : {apres}")
    if _git(["rev-parse", "HEAD"], v) != COMMIT_VOISIN:
        raise Arret("code voisin : un commit a été fait (les correctifs restent sans commit)")
    b = ctx.banc_voisin
    if not b.exists():
        b.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(v, b, symlinks=True, ignore=shutil.ignore_patterns("fits", "lenses"))
    if (b / "data" / "fits").resolve() == (v / "data" / "fits").resolve():
        raise Arret("(q) le banc partage le dossier des ajustements de la course")
    if not ctx.manifeste.exists():
        creer_manifeste(ctx.racine, ctx.run_id, configuration(pieces), list(cb.TACHES_INTERVALLES), entropie=cb.ENTROPIE,
                        decisif=True, prereg=ctx.racine / next(iter(PIECES)), commande=" ".join(sys.argv))
    return {"pieces": pieces, "voisin": {"commit": COMMIT_VOISIN, "arbre": ARBRE_VOISIN, "avant": VOISIN_AVANT, "apres": apres},
            "original_06": ORIGINAL_06[1], "banc": str(b.relative_to(ctx.racine))}


def configuration(pieces: dict) -> dict:
    return {"go_id": GO_ATTENDU, "tranche": "ajustement de nos lentilles (B-β)", "modele": LLAMA, "revision": REVISION_LLAMA,
            "lentilles": list(SPECS), "commit_voisin": COMMIT_VOISIN, "correctifs": list(CORRECTIFS), "pieces": pieces,
            "corpus": DOCS_CORPUS, "ajustement": "02_fit.py --docs 1000 --seq-len 128 --full-length --save-minutes 60",
            "graines": {"neurones": "random.Random(0) du dépôt ; graine 1 pour A1 et A5 (correctif (3))",
                        "autres": f"SeedSequence(entropy={cb.ENTROPIE}), branche « B-β », tâches {list(cb.TACHES_INTERVALLES)}"},
            "precision": "bf16 sur carte, produits en TF32 (02_fit, 06, measure) ; score en float32 sur le processeur",
            "drowse": {"version": cb.DROWSE_VERSION, "sha256": cb.DROWSE_SHA256, "installation": "roue empreintée, sans dépendances"}}


def _attendus_hub(info) -> dict:
    if getattr(info, "sha", None) != REVISION_LLAMA:
        raise Arret(f"le hub ne sert pas la révision épinglée ({getattr(info, 'sha', None)})")
    out = {}
    for s in info.siblings:
        if s.rfilename in MODELE_FICHIERS:
            lfs = getattr(s, "lfs", None)
            out[s.rfilename] = {"lfs_sha256": lfs.sha256} if lfs else {"git_sha1": s.blob_id}
    manque = sorted(set(MODELE_FICHIERS) - set(out))
    if manque:
        raise Arret(f"fichiers absents de la révision épinglée : {manque}")
    return out


def _controle_modele(chemin: Path, nom: str) -> str:
    h = sha256(chemin)
    if h != MODELE_FICHIERS[nom]:
        raise Arret(f"{nom} : empreinte différente de celle de l'addendum partie 1 (§ 2)")
    return h


def epingler(hf_home: Path, depot: str, revision: str) -> None:
    ref = Path(hf_home) / "hub" / f"models--{depot.replace('/', '--')}" / "refs" / "main"
    if ref.exists() and ref.read_text().strip() != revision:
        raise Arret(f"cache du hub : refs/main de {depot} inattendu")
    ref.parent.mkdir(parents=True, exist_ok=True)
    ref.write_text(revision)


def _charger_tokeniseur_avec_cle() -> int:
    from transformers import AutoTokenizer
    return len(AutoTokenizer.from_pretrained(LLAMA, revision=REVISION_LLAMA))


def etape_telecharger_tokeniseur(ctx: Contexte, charger_tokeniseur=_charger_tokeniseur_avec_cle) -> dict:
    model_info, telecharger = ctx.hub_fonctions()
    attendus = _attendus_hub(model_info(LLAMA, revision=REVISION_LLAMA, files_metadata=True))
    autres = [n for n, a in attendus.items() if "lfs_sha256" in a and a["lfs_sha256"] != MODELE_FICHIERS[n]]
    if autres:
        raise Arret(f"le hub annonce d'autres empreintes que la partie 1 : {autres}")
    fichiers = {n: _controle_modele(Path(telecharger(LLAMA, n, revision=REVISION_LLAMA)), n) for n in TOKENISEUR}
    epingler(ctx.hf_home, LLAMA, REVISION_LLAMA)
    lentilles = {}
    for s, (f, h) in LENTILLES_NP.items():  # dépôt public : aucune clé envoyée
        if sha256(Path(telecharger(NP, f, revision=REVISION_NEURONPEDIA, token=False))) != h:
            raise Arret(f"lentille {s} : empreinte inattendue")
        lentilles[s] = h
    epingler(ctx.hf_home, NP, REVISION_NEURONPEDIA)
    nv = charger_tokeniseur()  # avec la clé, dans ce processus : inscrit au cache les absences des fichiers facultatifs
    sonde = [sys.executable, "-c", f"from transformers import AutoTokenizer; print('nv', len(AutoTokenizer.from_pretrained({LLAMA!r})))"]
    s = ctx.executer(sonde, ctx.racine, env_enfant(ctx.voisin, True), ctx.journal("telecharger-tokeniseur"), 600)
    if s["code"] != 0 or f"nv {nv}" not in "\n".join(s["fin"]):
        raise Arret("tokeniseur non chargé sans clé hors ligne")
    return {"attendus_hub": attendus, "tokeniseur": fichiers, "lentilles_np": lentilles, "nv": nv}


def _copie_artefact(source: Path, cible: Path, avant: str, apres: str) -> None:
    texte = source.read_text(encoding="utf-8")
    if texte.count(avant) != 1:
        raise Arret(f"artefact de la garde (d) : motif trouvé {texte.count(avant)} fois dans {source.name}")
    cible.write_text(texte.replace(avant, apres), encoding="utf-8")


ARTEFACTS_D = {  # copies de l'essai du Llama miniature : (motif, remplacement)
    "saute": ("def test_frequences_mises_a_l_echelle():",
              "@pytest.mark.skip(reason=\"artefact de la garde (d)\")\ndef test_frequences_mises_a_l_echelle():"),
    "signe": ('assert torch.allclose(r.mean("out")[layer], J[:, valid].mean(1), atol=1e-4), layer',
              'assert torch.allclose(-r.mean("out")[layer], J[:, valid].mean(1), atol=1e-4), layer'),
}


def _lentille_np_controlee(ctx: Contexte, spec: str) -> dict:
    """Lentille de Neuronpedia lue par le code voisin corrigé ; 31 couches contiguës (0 à 30) ; garde (e) (matrices)."""
    J = ctx.fv().load_lens(spec)
    couches = sorted(J)
    return {"couches": couches == list(range(31)), "e": cb.garde_e_matrices({l: J[l].float().numpy() for l in couches}, spec)}


def _drowse() -> dict:
    """Version de Drowse installée et empreinte de la roue téléchargée par l'amorce (`DROWSE_ROUE`)."""
    roue = os.environ.get("DROWSE_ROUE", "")
    try:
        version = importlib.metadata.version("drowse.ai")
    except importlib.metadata.PackageNotFoundError:
        version = ""
    return {"version": version, "roue_sha256": sha256(roue) if roue and Path(roue).exists() else ""}


def etape_b0(ctx: Contexte, drowse=_drowse) -> dict:
    """Essais des correctifs, des essais du dépôt sur le Qwen3 miniature, de l'estimateur sur le Llama miniature (garde (f)), des
    crochets ; artefacts de la garde (d) ; lentilles de Neuronpedia (31 couches contiguës, garde (e)) ; Drowse (version, empreinte,
    chargement) ; code des verdicts et des contrôles. Aucun essai sauté (garde (d))."""
    if sha256(ctx.original_06) != ORIGINAL_06[1]:
        raise Arret("B0 : copie du script d'activations d'origine absente ou altérée")
    dr = drowse()
    if dr["version"] != cb.DROWSE_VERSION or dr["roue_sha256"] != cb.DROWSE_SHA256:
        raise Arret(f"Drowse : version {dr['version']!r} ou empreinte de la roue inattendue (liste d'arrêt)")
    env = env_enfant(ctx.voisin, True, NEURON_LENS_ROOT=ctx.voisin, NEURON_LENS_ORIG=ctx.original_06)
    essais = {Path(e).name: _pytest(ctx, ctx.racine / e, ctx.voisin, env, "b0") for e in ESSAIS}
    essais["test_transport.py (dépôt, Qwen3 miniature)"] = _pytest(ctx, ctx.voisin / "tests" / "test_transport.py", ctx.voisin, env,
                                                                    "b0")
    env_nous = env_enfant(ctx.voisin, True) | {"PYTHONPATH": str(ctx.racine / "src")}
    for t in ("test_neuron_lens_verdicts_b_beta_v4.py", "test_neuron_lens_controles_b_beta_v1.py"):
        essais[t] = _pytest(ctx, ctx.racine / "tests" / t, ctx.racine, env_nous, "b0")
    # artefacts de la garde (d) : chacun doit être vu en défaut
    dossier = ctx.diag / "artefacts-garde-d"
    dossier.mkdir(parents=True, exist_ok=True)
    artefacts = {}
    for nom, (avant, apres) in ARTEFACTS_D.items():
        copie = dossier / f"essai-artefact-{nom}.py"
        _copie_artefact(ctx.racine / ESSAI_MINIATURE, copie, avant, apres)
        x = _pytest(ctx, copie, ctx.voisin, env, "b0")
        artefacts[nom] = x | {"vu_en_defaut": bool(cb.garde_d({nom: x}))}
    lentilles = {s: _lentille_np_controlee(ctx, s) for s in LENTILLES_NP}
    nombres = [f"{Path(e).name} : {essais[Path(e).name]['passes']} tests passés au lieu de {n}" for e, (_, n) in ESSAIS.items()
               if n is not None and essais[Path(e).name]["passes"] != n]
    d = cb.garde_d(essais) + nombres + [f"(d) artefact « {k} » non vu en défaut" for k, x in artefacts.items() if not x["vu_en_defaut"]]
    f = [p for p in d if "essai-transport-llama-miniature" in p]
    e = [p for s, x in lentilles.items() for p in x["e"]] + [f"lentille {s} : couches non contiguës" for s, x in lentilles.items()
                                                             if not x["couches"]]
    res = {"essais": essais, "artefacts_d": artefacts, "lentilles_np": lentilles, "drowse": dr}
    exiger(d=[p for p in d if p not in f], f=f, e=e)
    return res


def etape_telecharger_poids(ctx: Contexte) -> dict:
    _, telecharger = ctx.hub_fonctions()
    fichiers = {n: _controle_modele(Path(telecharger(LLAMA, n, revision=REVISION_LLAMA)), n) for n in MODELE_FICHIERS
                if n not in TOKENISEUR}
    epingler(ctx.hf_home, LLAMA, REVISION_LLAMA)
    return {"poids": fichiers}


def _publiee(ctx: Contexte, cle: str) -> dict:
    """Provenance publiée, lue par `git show HEAD:` dans l'arbre voisin (jamais dans l'arbre après `01` ou `05`), empreinte exigée."""
    chemin, h = PUBLIEES[cle]
    brut = subprocess.run(["git", "show", f"HEAD:{chemin}"], cwd=ctx.voisin, capture_output=True, check=True).stdout
    if hashlib.sha256(brut).hexdigest() != h:
        raise Arret(f"provenance publiée {cle} : empreinte inattendue")
    return json.loads(brut)


def etape_corpus_ajustement(ctx: Contexte) -> dict:
    """`01_lens_corpus.py --docs 1000 --revision …` ; garde (i) sur sa provenance ; contrôles de P.1 par `lens_docs` et `rows_sha256`
    du dépôt voisin sur la machine (932, 466 et 466, `a6afd972…`)."""
    s = ctx.executer([sys.executable, "scripts/01_lens_corpus.py", "--docs", "1000", "--revision", cb.REVISION_DCLM], ctx.voisin,
                     env_enfant(ctx.voisin, False), ctx.journal("corpus-ajustement"), 3600)
    if s["code"] != 0:
        raise Arret(f"01_lens_corpus.py en échec (code {s['code']})")
    prov = json.loads((ctx.voisin / PUBLIEES["ajustement"][0]).read_text(encoding="utf-8"))
    i = cb.garde_i(prov, None, _publiee(ctx, "ajustement"), _publiee(ctx, "act-dclm"))
    rows, h_voisin, indices = ctx.fv().lens_docs_ajustement()
    rel, p1 = cb.controle_p1(rows)
    rel["indices_pleins"] = indices
    if h_voisin != rel["rows_sha256"]:
        p1.append("P.1 : rows_sha256 du dépôt voisin différent de notre recopie")
    exiger(i=i)
    if p1:
        raise Arret("P.1 : " + " ; ".join(p1) + " (l'ajustement ne part pas ; nœud à la mère)")
    return {"provenance_sha256": sha256(ctx.voisin / PUBLIEES["ajustement"][0]), "p1": rel,
            "dclm_jsonl_sha256": sha256(ctx.voisin / "data" / "corpus" / "dclm.jsonl"), "duree_01_s": s["duree_s"]}


def versions() -> dict:
    out = {"python": platform.python_version()}
    for k in cb.VERSIONS:
        if k == "python":
            continue
        try:
            out[k] = importlib.metadata.version(k)
        except importlib.metadata.PackageNotFoundError:
            out[k] = ""
    return out


def etape_partie2_b0(ctx: Contexte, lire_versions=versions) -> dict:
    """Partie 2 de l'addendum, premier relevé (ce qui existe à B0), comparé à la partie 1 **avant l'ajustement** ; écart = arrêt."""
    from controle_ia.neuron_lens import addendum_partie2_b_beta_v1 as p2
    releve = {"date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "instance": os.environ.get("INSTANCE_ID", ""),
              "commit_reduit": os.environ.get("COMMIT_REDUIT", ""), "commit_source": os.environ.get("COMMIT_SOURCE", ""),
              "commit_code_de_course": os.environ.get("COMMIT_REDUIT", ""),
              "voisin": {"head": _git(["rev-parse", "HEAD"], ctx.voisin), **ctx.lire("preparer")["voisin"]},
              "modele": ctx.lire("telecharger-tokeniseur")["tokeniseur"] | ctx.lire("telecharger-poids")["poids"],
              "lentilles_np": ctx.lire("telecharger-tokeniseur")["lentilles_np"], "versions": lire_versions(),
              "drowse": ctx.lire("b0")["drowse"], "essais": ctx.lire("b0")["essais"], "artefacts_d": ctx.lire("b0")["artefacts_d"],
              "corpus_ajustement": ctx.lire("corpus-ajustement")}
    texte, pb = p2.rediger_b0(releve)
    chemin = ctx.diag / "addendum-partie2-b-beta-v1-b0.md"
    h = p2.ecrire_une_fois(chemin, texte)
    if pb:
        raise Arret("partie 2 (B0) : écarts à la partie 1 : " + " ; ".join(pb[:10]) + " (nœud à la mère avant l'ajustement)")
    return {"partie2": str(chemin.relative_to(ctx.racine)), "sha256": h, "ecarts": pb}


def _commande_fit(lentille: str) -> list[str]:
    return [sys.executable, "scripts/02_fit.py", "--lens", lentille, "--model", LLAMA, "--docs", "1000", "--seq-len", "128",
            "--full-length", "--save-minutes", "60"]


_DOC = re.compile(r" doc (\d+)/(\d+) \((\d+) tokens\) in ([0-9.]+)s")


def etape_banc(ctx: Contexte) -> dict:
    """Banc dans la copie à part : deux documents de la lentille R puis de la lentille S, le second chronométré (le premier compile).
    Au-delà de 23,6 s par document, l'ajustement ne part pas ; au-delà de 14,2 s, compte rendu sans arrêt (règle du banc)."""
    b = ctx.banc_voisin
    shutil.copyfile(ctx.voisin / "data" / "corpus" / "dclm.jsonl", b / "data" / "corpus" / "dclm.jsonl")
    out = {}
    for le in ("R", "S"):
        cmd = _commande_fit(le)
        cmd[cmd.index("--docs") + 1] = "2"
        s = ctx.executer(cmd, b, env_enfant(b, True), ctx.journal("banc"), 3600)
        segment = ctx.journal("banc").read_text(encoding="utf-8", errors="replace").rsplit("\n=== ", 1)[-1]
        temps = [float(m.group(4)) for l in segment.splitlines() if (m := _DOC.search(l)) and m.group(2) == "2"]
        if s["code"] != 0 or len(temps) < 2:
            raise Arret(f"banc {le} en échec (code {s['code']}, {len(temps)} documents chronométrés)")
        out[le] = {"secondes": temps[:2], "regle": cb.regle_banc(temps[1])}
    if (ctx.voisin / "data" / "fits").exists() and any((ctx.voisin / "data" / "fits").iterdir()):
        raise Arret("(q) le banc a écrit dans le dossier des ajustements de la course")
    pire = max(out.values(), key=lambda x: x["secondes"][1])
    if pire["regle"] == "arret":
        raise Arret(f"banc : {pire['secondes'][1]} s par document, au-delà de 23,6 s : l'ajustement ne part pas")
    return {"banc": out, "compte_rendu": any(x["regle"] == "compte_rendu" for x in out.values())}


def _ajustement(ctx: Contexte, lentille: str) -> dict:
    f = ctx.voisin / "data" / "fits" / cb.FIT_NOMS[lentille]
    journal = ctx.journal(f"ajustement-{lentille}")
    if not journal.exists():  # premier lancement : aucun fichier `-T128` de cette lentille (ni, pour R, de S) dans l'arbre
        presents = [x for x in ([cb.FIT_NOMS["R"], cb.FIT_NOMS["S"]] if lentille == "R" else [cb.FIT_NOMS["S"]])
                    if (ctx.voisin / "data" / "fits" / x).exists()]
        exiger(q=cb.garde_q_avant(presents))
    elif f.exists():  # relance : le point de sauvegarde porte l'empreinte des lignes, full_length, la lentille et le modèle
        exiger(q=cb.garde_q_relance(charger_fit(f)["meta"], lentille))
    s = ctx.executer(_commande_fit(lentille), ctx.voisin, env_enfant(ctx.voisin, True), journal, 10 * 3600)
    if s["code"] != 0 or not f.exists():
        raise Arret(f"ajustement {lentille} en échec (code {s['code']})")
    saved = charger_fit(f)
    r = resume_fit(saved)
    rows = ctx.fv().lens_docs_ajustement()[0]
    g = cb.garde_g_fit(r["meta"], r["next_doc"], r["n_docs"], cb.longueurs_point(r["meta"], rows), r["diffs"], r["finies"], lentille)
    h = cb.garde_h(r["premiere_dim"], lentille)
    exiger(g=g, h=h)
    return {"fichier": f.name, "sha256": sha256(f), "taille": f.stat().st_size} | {k: v for k, v in r.items() if k != "meta"} | {
        "meta": {k: v for k, v in r["meta"].items()}, "longueurs": sorted(set(cb.longueurs_point(r["meta"], rows)))}


def etape_ajustement_r(ctx: Contexte) -> dict:
    return _ajustement(ctx, "R")


def etape_ajustement_s(ctx: Contexte) -> dict:
    return _ajustement(ctx, "S")


EXPORTS = {NOTRE_R: ("dclm-llama", None), MOITIES_R[0]: ("dclm-llama-even", 0), MOITIES_R[1]: ("dclm-llama-odd", 1)}


def _empreintes_home(home: Path) -> dict:
    return {str(p.relative_to(home)): sha256(p) for p in sorted(home.rglob("*")) if p.is_file()}


def etape_export(ctx: Contexte) -> dict:
    """Export de notre R depuis le fichier `-T128` (entière, moitié paire, moitié impaire) ; gardes (e), (h), (n), (o) sur les exports,
    avant `lens_compare.py` et `score`."""
    fr = ctx.voisin / "data" / "fits" / cb.FIT_NOMS["R"]
    if sha256(fr) != ctx.lire("ajustement-R")["sha256"]:
        raise Arret("export : fichier d'ajustement R changé depuis la fin de l'ajustement")
    sorties = {}
    for spec, (nom, moitie) in EXPORTS.items():
        home = ctx.voisin / "data" / "lenses" / nom
        if not home.exists():
            cmd = [sys.executable, "scripts/04_export_rlens.py", str(fr), "--name", nom] + ([] if moitie is None else ["--half", str(moitie)])
            s = ctx.executer(cmd, ctx.voisin, env_enfant(ctx.voisin, True), ctx.journal("export"), 3600)
            if s["code"] != 0:
                raise Arret(f"04_export_rlens.py {nom} en échec (code {s['code']})")
        sorties[spec] = _empreintes_home(home)
    saved = charger_fit(fr)
    fv = ctx.fv()
    o, charges = [], {}
    for spec, (nom, moitie) in EXPORTS.items():
        try:
            charges[spec] = {l: (None if m is None else m.float().numpy()) for l, m in fv.load_lens(spec).items()}
            o += cb.garde_o(charges[spec], moyennes_fit(saved, "out", moitie), spec)
        except Exception as ex:  # noqa: BLE001 — l'erreur est la garde (o)
            o += cb.garde_o(None, {}, spec, erreur=f"{type(ex).__name__}: {ex}")
    notre = charges.get(NOTRE_R, {})
    npr = {l: m.float().numpy() for l, m in fv.load_lens("npR").items()}
    sha_np = LENTILLES_NP["npR"][1]
    n = cb.garde_n(notre, npr, "", sha_np)
    n += [f"(n) un fichier de {spec} a l'empreinte de la lentille R publique" for spec, f in sorties.items() if sha_np in f.values()]
    e = cb.garde_e_matrices(notre, NOTRE_R) if notre else ["(e) notre R non chargée"]
    h = cb.garde_h_export([l for l, m in notre.items() if m is not None]) if notre else []
    exiger(e=e, h=h, n=n, o=o)
    return {"exports": sorties, "couches_out": sorted(notre)}


def etape_corpus_activations(ctx: Contexte) -> dict:
    """`05_act_corpus.py` (révisions imposées, correctif (6)) ; garde (i) de nouveau : provenance réécrite égale à la publiée, aucun
    identifiant ni texte entier commun avec les 932 documents d'ajustement."""
    s = ctx.executer([sys.executable, "scripts/05_act_corpus.py", "--docs", DOCS_CORPUS], ctx.voisin, env_enfant(ctx.voisin, False),
                     ctx.journal("corpus-activations"), 2 * 3600)
    if s["code"] != 0:
        raise Arret(f"05_act_corpus.py en échec (code {s['code']})")
    d = ctx.voisin / "data" / "corpus"
    corpus = {f: sha256(d / f) for f in cb.CORPUS_ACT_SHA256}
    autres = [f for f, h in corpus.items() if h != cb.CORPUS_ACT_SHA256[f]]
    if autres:  # même condition que la partie 2 (partie 1, § 3), constatée dès `05` pour ne pas payer les comptes de jetons
        raise Arret(f"corpus d'activations : empreintes différentes de la partie 1 (§ 3) : {autres} (nœud à la mère)")
    return {"duree_05_s": s["duree_s"], "corpus": corpus, "garde_i": _garde_i_complete(ctx)}


def _garde_i_complete(ctx: Contexte) -> list[str]:
    d = ctx.voisin / "data" / "corpus"
    prov_aj = json.loads((d / "dclm.provenance.json").read_text(encoding="utf-8"))
    prov_act = json.loads((d / "act-dclm.provenance.json").read_text(encoding="utf-8"))
    fv = ctx.fv()
    pleins = ctx.lire("corpus-ajustement")["p1"]["indices_pleins"]
    if len(pleins) != cb.N_DOCS:
        raise Arret(f"(i) {len(pleins)} rangs de documents d'ajustement au lieu de {cb.N_DOCS}")
    tous = fv.textes(d / "dclm.jsonl")
    textes_aj = [tous[i] for i in pleins]  # textes entiers (champ `text`, sans coupe) des 932 documents d'ajustement
    i = cb.garde_i(prov_aj, prov_act, _publiee(ctx, "ajustement"), _publiee(ctx, "act-dclm"), textes_aj, fv.textes(d / "act-dclm.jsonl"))
    exiger(i=i)
    return i


def etape_comptes_jetons(ctx: Contexte) -> dict:
    """`03_token_counts.py`, joué **une seule fois** ; jetons gardés de Llama (nombre, empreinte) consignés."""
    sortie = ctx.voisin / "data" / f"token_counts-{STEM}.pt"
    if sortie.exists():
        raise Arret("03_token_counts.py : fichier de comptes déjà présent (l'étape ne se joue qu'une fois)")
    s = ctx.executer([sys.executable, "scripts/03_token_counts.py"], ctx.voisin, env_enfant(ctx.voisin, True),
                     ctx.journal("comptes-jetons"), 2 * 3600)
    if s["code"] != 0:
        raise Arret(f"03_token_counts.py en échec (code {s['code']})")
    k = ctx.fv().kept()
    bos = 128000
    return {"kept": {"n": len(k), "sha256": cb.empreinte_liste_gardee(k), "jeton_de_debut_garde": bos in k,
                     "rang_jeton_de_debut": sorted(k).index(bos) if bos in k else None},
            "comptes_sha256": sha256(sortie) if sortie.exists() else None}


def etape_partie2_corpus(ctx: Contexte) -> dict:
    """Partie 2, second relevé (juste après l'unique `03_token_counts.py`, avant `lens_compare.py` et la fumée) : fichiers du corpus
    d'activations, provenances, jetons gardés, contre les valeurs attendues de la partie 1 (§ 3) ; écart = arrêt (nœud)."""
    from controle_ia.neuron_lens import addendum_partie2_b_beta_v1 as p2
    from controle_ia.neuron_lens.controles_b0_v2 import verifier_provenances
    d = ctx.voisin / "data" / "corpus"
    corpus = {f: sha256(d / f) for f in cb.CORPUS_ACT_SHA256}
    produites = {t: json.loads((d / f"act-{t if t != 'chat' else 'chat-' + STEM}.provenance.json").read_text(encoding="utf-8"))
                 for t in ("dclm", "zh", "code", "chat")}
    references = {t: _publiee(ctx, f"act-{t}") for t in ("dclm", "zh", "code", "chat")}
    releve = {"corpus": corpus, "kept": ctx.lire("comptes-jetons")["kept"],
              "provenances": verifier_provenances(produites, references)}
    texte, pb = p2.rediger_corpus(releve)
    chemin = ctx.diag / "addendum-partie2-b-beta-v1-corpus.md"
    h = p2.ecrire_une_fois(chemin, texte)
    if pb:
        raise Arret("partie 2 (corpus) : écarts à la partie 1 : " + " ; ".join(pb[:10]) + " (nœud à la mère)")
    return {"partie2": str(chemin.relative_to(ctx.racine)), "sha256": h, "ecarts": pb}


def _garde_r(ctx: Contexte, etape: str) -> None:
    k = ctx.fv().kept()
    exiger(r=cb.garde_r(cb.empreinte_liste_gardee(k), ctx.lire("comptes-jetons")["kept"]["sha256"], etape))


def etape_lens_compare(ctx: Contexte) -> dict:
    _garde_r(ctx, "lens_compare.py")
    sortie = ctx.diag / "lens_compare-b-beta-v1.json"
    if sortie.exists():
        sortie.unlink()  # reste d'une comparaison interrompue avant son résultat (le correctif (4) refuse d'écraser)
    s = ctx.executer([sys.executable, "scripts/checks/lens_compare.py", "--lenses", ",".join(MOITIES_R + ("npR",)), "--layers",
                      COUCHES_ACCORD, "--samples", "0", "--json", str(sortie)], ctx.voisin, env_enfant(ctx.voisin, True),
                     ctx.journal("lens-compare"), 3600)
    if s["code"] != 0 or not sortie.exists():
        raise Arret(f"lens_compare.py en échec (code {s['code']})")
    from controle_ia.scellement import sceller
    accord = cb.accord_depuis_lens_compare(json.loads(sortie.read_text(encoding="utf-8")))
    return {"sortie": str(sortie.relative_to(ctx.racine)), "sha256": sceller(sortie), "accord": {str(k): v for k, v in accord.items()}}


def _garde_k_hub(ctx: Contexte) -> None:
    exiger(k=cb.garde_k(ctx.fv().fits(), "hub"))


def etape_fumee(ctx: Contexte) -> dict:
    _garde_k_hub(ctx)
    _garde_r(ctx, "06_activations.py (fumée)")
    s = ctx.executer([sys.executable, "scripts/06_activations.py", "--docs", "64"], ctx.voisin, env_enfant(ctx.voisin, True),
                     ctx.journal("fumee"), 3600)
    exiger(d=cb.garde_d({"fumee": {"code": s["code"]}}))
    return {"code": s["code"], "duree_s": s["duree_s"],
            "message_hub": cb.message_hub_present(ctx.journal("fumee").read_text(encoding="utf-8", errors="replace"))}


def etape_passe(ctx: Contexte) -> dict:
    _garde_k_hub(ctx)
    _garde_r(ctx, "06_activations.py")
    s = ctx.executer([sys.executable, "scripts/06_activations.py"], ctx.voisin, env_enfant(ctx.voisin, True), ctx.journal("passe"),
                     6 * 3600)
    if s["code"] != 0:
        raise Arret(f"passe complète en échec (code {s['code']})")
    acts = ctx.voisin / "data" / "acts" / f"{STEM}.pt"
    if not acts.exists():
        raise Arret("passe complète : fichier des activations absent")
    journal = ctx.journal("passe").read_text(encoding="utf-8", errors="replace")
    exiger(k=[] if cb.message_hub_present(journal) else ["(k) message du correctif (1) (branche hub) absent du journal de la passe"])
    return {"acts": {"sha256": sha256(acts), "taille": acts.stat().st_size}, "duree_s": s["duree_s"]}


def etape_pilotes(ctx: Contexte) -> dict:
    _garde_k_hub(ctx)
    _garde_r(ctx, "07_drivers.py")
    exiger(p=cb.garde_p_pilotes(ctx.fv().pilotes_comptes()))
    s = ctx.executer([sys.executable, "scripts/07_drivers.py"], ctx.voisin, env_enfant(ctx.voisin, True), ctx.journal("pilotes"),
                     4 * 3600)
    if s["code"] != 0:
        raise Arret(f"07_drivers.py en échec (code {s['code']})")
    tables = sorted(p for p in (ctx.voisin / "data").rglob("*drivers*") if p.is_file())
    return {"empreintes": {str(p.relative_to(ctx.voisin)): sha256(p) for p in tables},
            "fin_journal": s["fin"][-5:], "duree_s": s["duree_s"]}


def _causal(ctx: Contexte, graine: int = 0) -> Path:
    return ctx.voisin / "data" / "causal" / (f"{STEM}-causal.pt" if graine == 0 else f"{STEM}-causal-seed{graine}.pt")


def _resume(ctx: Contexte, tag: str) -> Path:
    return ctx.voisin / "data" / "summary" / f"causal_lens_{tag}_{STEM}.json"


def _measure(ctx: Contexte, graine: int, etape: str, timeout_s: float = 5 * 3600) -> dict:
    import torch
    s = ctx.executer([sys.executable, "scripts/checks/causal_lens.py", "measure", "--ctx-batch", str(CTX_BATCH)]
                     + (["--seed", str(graine)] if graine else []), ctx.voisin, env_enfant(ctx.voisin, True), ctx.journal(etape),
                     timeout_s)
    f = _causal(ctx, graine)
    if s["code"] == 124:
        return {"code": 124}
    if s["code"] != 0 or not f.exists():
        raise Arret(f"measure (graine {graine}) en échec (code {s['code']})")
    meta = torch.load(f, weights_only=False, map_location="cpu", mmap=True)["meta"]
    exiger(p=cb.garde_p_measure(meta))
    return {"code": 0, "meta": meta, "causal": {"sha256": sha256(f), "taille": f.stat().st_size}, "duree_s": s["duree_s"]}


def _score(ctx: Contexte, graine: int, tag: str, specs, etape: str, timeout_s: float = 2 * 3600) -> dict:
    from controle_ia.scellement import sceller
    cmd = [sys.executable, "scripts/checks/causal_lens.py", "score", "--lenses", ",".join(specs), "--tag", tag]
    cmd += ["--seed", str(graine)] if graine else []
    s = ctx.executer(cmd, ctx.voisin, env_enfant(ctx.voisin, True), ctx.journal(etape), timeout_s)
    j = _resume(ctx, tag)
    if s["code"] == 124:
        return {"code": 124}
    if s["code"] != 0 or not j.exists():
        raise Arret(f"score (graine {graine}) en échec (code {s['code']})")
    out = {}
    for src in (j, j.with_suffix(".log")):
        cible = ctx.diag / src.name
        shutil.copyfile(src, cible)
        out[src.suffix[1:]] = {"chemin": str(cible.relative_to(ctx.racine)), "sha256": sceller(cible)}
    return {"code": 0, "resume": out, "duree_s": s["duree_s"]}


def etape_measure(ctx: Contexte) -> dict:
    _garde_i_complete(ctx)  # de nouveau avant `measure`
    return _measure(ctx, 0, "measure")


def etape_score(ctx: Contexte) -> dict:
    return _score(ctx, 0, TAG, SPECS, "score")


def _grandeurs(ctx: Contexte, graine: int, tag: str, specs, nom: str) -> dict:
    """n recalculé et grandeurs par pôle par notre code (`grandeurs_b_alpha_v1`, contre-lu), fidèles au JSON de `score`."""
    import torch

    from controle_ia.neuron_lens import grandeurs_b_alpha_v1 as g
    from controle_ia.scellement import sceller
    causal, resume = _causal(ctx, graine), ctx.diag / _resume(ctx, tag).name
    score_json = json.loads(resume.read_text(encoding="utf-8"))
    sortie = ctx.diag / nom
    if str(ctx.voisin) not in sys.path:
        sys.path.insert(0, str(ctx.voisin))
    saved = torch.load(causal, weights_only=False, mmap=True)
    lire, nv, keep = g.lecteur_voisin(LLAMA, specs)
    res = g.grandeurs(saved, lire, specs, nv, keep, cb.F_LLAMA)
    ecarts = g.comparer_a_score(res["table"], score_json)
    if ecarts:
        raise Arret("grandeurs par pôle infidèles à score : " + " ; ".join(ecarts[:5]))
    if not sortie.exists():
        g.ecrire(sortie, res, sha256(causal), sha256(resume), ecarts)
    poles = res["poles"]
    temoin = all(p["temoin"] != p["neurone"] for p in poles)
    normes = all(p["alpha"] > 0 for p in poles if p["aleatoire"] and p["lectures"]["steer 1x"][NOTRE_R]["motif"] == "retenu")
    return {"grandeurs": str(sortie.relative_to(ctx.racine)), "sha256": sceller(sortie), "n": res["n"], "ecartes": res["ecartes"],
            "temoin_distinct": bool(temoin), "normes_non_nulles": bool(normes)}


def etape_grandeurs(ctx: Contexte) -> dict:
    return _grandeurs(ctx, 0, TAG, SPECS, "grandeurs-par-pole-b-beta-v1.json")


def etape_reads(ctx: Contexte) -> dict:
    """Liens durs du correctif (5), posés seulement maintenant ; gardes (k) (nos deux noms), (r), (s) ; `reads_at_firings.py`."""
    fits = ctx.voisin / "data" / "fits"
    emp_fit = {le: ctx.lire(f"ajustement-{le}")["sha256"] for le in ("R", "S")}
    s_ = cb.garde_s([str(p.relative_to(ctx.voisin)) for p in (ctx.voisin / "data" / "checks" / f"reads_at_firings-{STEM}.pt",
                                                             ctx.voisin / "data" / "summary" / f"reads_at_firings_{STEM}.json")
                     if p.exists()])
    exiger(s=s_)
    for le in ("R", "S"):
        lien = fits / cb.FIT_NOMS_ARCH[le]
        if not lien.exists():
            os.link(fits / cb.FIT_NOMS[le], lien)
    liens = {le: sha256(fits / cb.FIT_NOMS_ARCH[le]) for le in ("R", "S")}
    exiger(k=cb.garde_k(ctx.fv().fits(), "noms", liens, emp_fit))
    _garde_r(ctx, "reads_at_firings.py")
    s = ctx.executer([sys.executable, "scripts/checks/reads_at_firings.py", "--parts", "neurons", "--device", "cuda"], ctx.voisin,
                     env_enfant(ctx.voisin, True), ctx.journal("reads"), 4 * 3600)
    j = ctx.voisin / "data" / "summary" / f"reads_at_firings_{STEM}.json"
    if s["code"] != 0 or not j.exists():
        raise Arret(f"reads_at_firings.py en échec (code {s['code']})")
    from controle_ia.scellement import sceller
    cible = ctx.diag / j.name
    shutil.copyfile(j, cible)
    read_s, silent = cb.reads_depuis_sortie(json.loads(cible.read_text(encoding="utf-8")))
    return {"sortie": str(cible.relative_to(ctx.racine)), "sha256": sceller(cible), "liens": liens, "n_couches": len(read_s)}


# ------------------------------------------------------------------------------------------------ verdicts et audits sur la machine

def _table_score(ctx: Contexte, tag: str, specs) -> dict:
    from controle_ia.neuron_lens import verdicts_b_beta_v4 as vb
    j = json.loads((ctx.diag / _resume(ctx, tag).name).read_text(encoding="utf-8"))
    return {c: {s: j["targets"][c][s] for s in specs} for c in vb.CIBLES}


def _serie_repere(ctx: Contexte) -> list:
    j = json.loads((ctx.racine / SERIE_REPERE).read_text(encoding="utf-8"))
    s = j["targets"]["steer 1x"]["npR"]
    if list(s["layer"]) != list(range(32)):
        raise Arret("série repère : couches inattendues")
    return list(s["r_med"])


def problemes_gardes(ctx: Contexte) -> dict:
    """Gardes constatées sur la machine, relues des résultats scellés : chaque étape qui les porte les a exigées (une garde manquée
    arrête la course), donc toutes sont tenues ici ; elles sont recomptées pour le code des verdicts, sans repli."""
    pb = {g: [] for g in cb.GARDES_MACHINE}
    b0 = ctx.lire("b0")
    d = cb.garde_d(b0["essais"])
    pb["d"] = [p for p in d if "essai-transport-llama-miniature" not in p] + cb.garde_d({"fumee": {"code": ctx.lire("fumee")["code"]}})
    pb["f"] = [p for p in d if "essai-transport-llama-miniature" in p]
    pb["identite"] = [p for x in b0["lentilles_np"].values() for p in x["e"]]
    pb["i"] = ctx.lire("corpus-activations")["garde_i"]
    return pb


def entrees(ctx: Contexte):
    from controle_ia.neuron_lens import verdicts_b_beta_v4 as vb
    r, s = ctx.lire("ajustement-R"), ctx.lire("ajustement-S")
    reads = json.loads((ctx.racine / ctx.lire("reads")["sortie"]).read_text(encoding="utf-8"))
    read_s, silent = cb.reads_depuis_sortie(reads)
    accord = {int(k): v for k, v in ctx.lire("lens-compare")["accord"].items()}
    return vb.Entrees(score=_table_score(ctx, TAG, SPECS), n=ctx.lire("grandeurs")["n"], repere_npR=_serie_repere(ctx),
                      stabilite={("R", "out"): r["diffs"]["out"], ("R", "mid"): r["diffs"]["mid"],
                                 ("S", "mid"): s["diffs"]["mid"], ("S", "out"): s["diffs"]["out"]},
                      accord=accord, read_S=read_s, silent=silent, gardes=cb.gardes_booleennes(problemes_gardes(ctx)))


def etape_declencheurs(ctx: Contexte) -> dict:
    from controle_ia.neuron_lens import verdicts_b_beta_v4 as vb
    e = entrees(ctx)
    defauts = vb.defauts_chaine(e)
    if defauts:  # rang 1 : chaîne en défaut (a) à (c), (e), (j) ou constatée ; aucun audit
        raise ChaineEnDefaut({"score": defauts})
    return {"declenches": vb.declencheurs(e), "debut_audits": ctx.horloge()}


def _temps_restant(ctx: Contexte) -> float:
    return TEMPS_AUDITS_S - (ctx.horloge() - ctx.lire("declencheurs")["debut_audits"])


def etape_audit_relance(ctx: Contexte) -> dict:
    """A1 et A5 : contrôles (1) et (2) sur la graine 0 ; une seule relance de `measure` et `score` à la graine 1 (lentilles logit, npR,
    notre R ; étiquette `b-beta-graine1`) ; n de la graine 1. Temps réservé épuisé = « non joué »."""
    g0 = ctx.lire("grandeurs")
    reste = _temps_restant(ctx)
    if reste <= 0:
        return {"resultat": "non joué", "motif": "temps réservé épuisé avant la relance"}
    t0 = ctx.horloge()
    m = _measure(ctx, 1, "audit-relance", timeout_s=reste)
    if m.get("code") == 124:
        return {"resultat": "non joué", "motif": "temps réservé épuisé pendant measure"}
    s = _score(ctx, 1, TAG_G1, SPECS_GRAINE1, "audit-relance", timeout_s=max(1.0, reste - (ctx.horloge() - t0)))
    if s.get("code") == 124:
        return {"resultat": "non joué", "motif": "temps réservé épuisé pendant score"}
    g1 = _grandeurs(ctx, 1, TAG_G1, SPECS_GRAINE1, "grandeurs-par-pole-b-beta-graine1-v1.json")
    return {"resultat": "joué", "measure": m, "score": s, "grandeurs": g1,
            "temoin_distinct": bool(g0["temoin_distinct"]), "normes_non_nulles": bool(g0["normes_non_nulles"])}


def etape_audits_controles(ctx: Contexte) -> dict:
    """A2, A3 (moitiés distinctes, documents) et A4 (permutation, fichier de la lentille S) : relus des résultats et des fichiers."""
    req = audits_requis(ctx)
    out = {}
    r, s = ctx.lire("ajustement-R"), ctx.lire("ajustement-S")
    p1 = ctx.lire("corpus-ajustement")["p1"]
    ex = ctx.lire("export")["exports"]
    ecarts = {f"R|{t}": v for t, v in r["ecarts_sommes"].items()} | {f"S|{t}": v for t, v in s["ecarts_sommes"].items()}
    emp_moities = {k: json.dumps(ex[k], sort_keys=True) for k in MOITIES_R}
    for a in ("A2", "A3"):
        if a in req:
            ok, pb = cb.controles_a2_a3({"R": r["n_docs"], "S": s["n_docs"]}, p1["rows_sha256_moities"], ecarts, emp_moities,
                                        longueurs=r["longueurs"] + s["longueurs"],
                                        full_length=bool(r["meta"].get("full_length") is True and s["meta"].get("full_length") is True),
                                        avec_a3=(a == "A3"))
            out[a] = {"controles_ok": bool(ok), "problemes": pb}
    if "A4" in req:
        pf = cb.points_fixes_permutation()
        lien_s = ctx.voisin / "data" / "fits" / cb.FIT_NOMS_ARCH["S"]
        out["A4"] = cb.controle_a4(pf, sha256(lien_s), s["sha256"]) | {"points_fixes": pf}
    return {"audits": out}


def etape_verdicts(ctx: Contexte) -> dict:
    from controle_ia.manifeste import generateur, lire_manifeste
    from controle_ia.neuron_lens import verdicts_b_beta_v4 as vb
    e = entrees(ctx)
    req = ctx.lire("declencheurs")["declenches"]
    audits = {}
    if {"A1", "A5"} & set(req):
        rel = ctx.lire("audit-relance")
        if rel["resultat"] != "joué":
            res = vb.NON_JOUE
        else:
            res = {"temoin_distinct": rel["temoin_distinct"], "normes_non_nulles": rel["normes_non_nulles"],
                   "score": _table_score(ctx, TAG_G1, SPECS_GRAINE1), "n": rel["grandeurs"]["n"]}
        for a in ("A1", "A5"):
            if a in req:
                audits[a] = res
    if {"A2", "A3", "A4"} & set(req):
        ac = ctx.lire("audits-controles")["audits"]
        for a in ("A2", "A3"):
            if a in req:
                audits[a] = {"controles_ok": bool(ac[a]["controles_ok"])}
        if "A4" in req:
            audits["A4"] = {"permutation_ok": bool(ac["A4"]["permutation_ok"]), "lentille_S_ok": bool(ac["A4"]["lentille_S_ok"])}
    v = vb.verdict(e, audits)
    man, _ = lire_manifeste(ctx.manifeste)
    gens = {t: generateur(man["graines"][t]) for t in cb.TACHES_INTERVALLES}
    poles = json.loads((ctx.racine / ctx.lire("grandeurs")["grandeurs"]).read_text(encoding="utf-8"))["poles"]
    iv = cb.intervalles(poles, gens)
    contenu = {"verdict": asdict(v), "audits_declenches": req,
               "audits_joues": {a: ("non joué" if audits[a] == vb.NON_JOUE else "joué") for a in audits},
               "intervalles": iv, "note": "fichier de verdicts unique (P.3, étape 7) ; lu plus tard par un lecteur neuf (P.7)"}
    chemin = ecrire_verdicts(ctx, contenu)
    return {"fichier_verdicts": str(chemin.relative_to(ctx.racine))}


ETAPE_FONCTIONS = {"preparer": etape_preparer, "telecharger-tokeniseur": etape_telecharger_tokeniseur, "b0": etape_b0,
                   "telecharger-poids": etape_telecharger_poids, "corpus-ajustement": etape_corpus_ajustement,
                   "partie2-b0": etape_partie2_b0, "banc": etape_banc, "ajustement-R": etape_ajustement_r,
                   "ajustement-S": etape_ajustement_s, "export": etape_export, "corpus-activations": etape_corpus_activations,
                   "comptes-jetons": etape_comptes_jetons, "partie2-corpus": etape_partie2_corpus, "lens-compare": etape_lens_compare,
                   "fumee": etape_fumee, "passe": etape_passe, "pilotes": etape_pilotes, "measure": etape_measure,
                   "score": etape_score, "grandeurs": etape_grandeurs, "reads": etape_reads, "declencheurs": etape_declencheurs,
                   "audit-relance": etape_audit_relance, "audits-controles": etape_audits_controles, "verdicts": etape_verdicts}
assert tuple(ETAPE_FONCTIONS) == ETAPES


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("commande", choices=("suite", "jouer"))
    p.add_argument("--etape", choices=ETAPES)
    p.add_argument("--racine", type=Path, default=Path.cwd())
    p.add_argument("--run-id", required=True)
    a = p.parse_args(argv)
    ctx = Contexte(a.racine.resolve(), a.run_id, Path(os.environ.get("HF_HOME", "/workspace/hf")))
    if a.commande == "suite":
        e = suite(ctx) if ctx.manifeste.exists() else "preparer"
        print("fin" if e is None else f"{e} {'jeton' if e in JETON else 'sans-jeton'} {'en-ligne' if e in EN_LIGNE else 'hors-ligne'}")
        return
    if not a.etape:
        p.error("--etape exigé avec jouer")
    print(json.dumps({"etape": a.etape, "resultat": str(jouer(ctx, a.etape))}, ensure_ascii=False))


if __name__ == "__main__":
    main()
