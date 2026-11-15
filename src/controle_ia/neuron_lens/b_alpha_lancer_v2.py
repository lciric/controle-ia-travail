"""Lanceur de la course de la tranche B-α de « Neuron Lens » (Llama 3.1 8B Instruct), sur la machine louée — v2.

v2 = v1 + la copie du script `06_activations.py` d'ORIGINE (`151d1196…`), gardée par `preparer` AVANT les correctifs sous
`originaux/06_activations.py` et passée à l'essai du correctif (1) par `NEURON_LENS_ORIG` (son usage l'exige : sans elle, deux de ses
essais échouent — course du 2026-11-15, instance 60770175, B0 en échec à 09:56:19Z) ; à une reprise où les correctifs sont déjà
appliqués, la copie est exigée (arrêt sinon) ; essais neufs de `etape_b0` (environnement de l'essai) et de `etape_partie2` de bout en
bout avec l'environnement de l'amorce (vérification courte, mineur 18).

Pièce 4 du § 6 du devis B-α v2 (`docs/notes/neuron-lens-v1/devis-b-alpha/devis-tranche-b-alpha-v2.md`, `61c394f5…`). Une **étape par
appel** (`--etape`), dans l'ordre du devis (§ 1) ; l'amorce appelle `suite` pour connaître la prochaine étape et la joue avec
l'environnement qu'elle demande. Chaque étape faite laisse un résultat **scellé** `diag/<run_id>/b-alpha-<étape>.json` (rattaché au
manifeste) : c'est la preuve qu'elle est faite ; une étape faite n'est jamais rejouée (entrée idempotente, reprise après une relance du
conteneur par le loueur : l'étape interrompue est rejouée, le code voisin reprend ses états gardés). Toute erreur arrête la course
(`arret-<étape>-<n>.json`, aucun repli).

Gardes (texte gelé v6 et devis v2) :
- `GO_ID` = GO-2026-11-14-06 ; pièces et modules aux empreintes scellées ; code voisin à `849bfe16` aux empreintes lues, quatre
  correctifs appliqués (empreintes après application exigées) ; manifeste R9 (run décisif, préenregistrement = texte gelé v6) ;
- **`HF_TOKEN`** (par son nom, jamais lu ni écrit ici) : présent **seulement** aux deux étapes de téléchargement de Llama
  (`telecharger-tokeniseur`, `telecharger-poids`), absent de toute autre étape (ainsi que `HUGGING_FACE_HUB_TOKEN` et `GH_TOKEN`, toujours
  absent) ; jamais transmis à un processus enfant ; jamais envoyé pour un autre dépôt (`token=False`) ;
- **hors ligne** (`HF_HUB_OFFLINE=1`) à toute étape, sauf les téléchargements, le corpus (jeux de données publics en flux) et l'audit
  « tout négatif » (téléchargements publics de Qwen3-8B) ; les processus enfants qui n'ont pas besoin du réseau sont hors ligne ; le cache
  du hub est **épinglé** (`refs/main` = révision épinglée) et les absences de fichiers facultatifs du tokeniseur sont inscrites au premier
  chargement, avec la clé (essai du 2026-11-15 : sans elles, le chargement sans clé échoue sur `added_tokens.json`) ;
- B0 avant toute passe ; partie 2 de l'addendum scellée, sans écart, **avant la fumée** ; code des verdicts (B.3) rejoué avant `measure` ;
  grandeurs par pôle fidèles à `score` ; audits R4 sur la même machine, avant destruction, seulement s'ils sont déclenchés ;
- durées par étape écrites dans chaque résultat, avec l'échéance du devis (attendu, pire cas) et le dépassement éventuel.
Aucun appel au loueur ici (location, minuterie, garde de dépense : commande et amorce).
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.metadata
import io
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

from controle_ia.neuron_lens import addendum_partie2_b_alpha_v1 as p2

GO_ATTENDU = "GO-2026-11-14-06"
LLAMA = "meta-llama/Llama-3.1-8B-Instruct"
QWEN = "Qwen/Qwen3-8B"
NP = "neuronpedia/jacobian-lens"
STEM = "llama-3.1-8b-instruct"
F_LLAMA = 14336
SPECS = ("logit", "J", "npJpp", "npR")
DOCS_CORPUS = "dclm=40000,zh=8000,code=8000,chat=8000"
SEQ = 256  # `06_activations.py`, l. 88 : longueur des documents de la passe
ENTROPIE = 20261114  # texte gelé, § B.2 : `SeedSequence(entropy=20261114)`, branche « B-α »
PIECES = {
    "docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md": "34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131",
    "docs/notes/neuron-lens-v1/addendum-empreintes-v3.md": "e63d95caa06fde0cb23d2b0dbcd143413d822be9487edf8f54fe72b46db0df82",
    "docs/notes/neuron-lens-v1/devis-b-alpha/devis-tranche-b-alpha-v2.md": "61c394f570a15a58067488b338ca46ade5734bf9f7446964100933e7a458de13",
}
MODULES = ("verdicts_b_alpha_v3.py", "controles_b0_v2.py", "grandeurs_b_alpha_v1.py", "addendum_partie2_b_alpha_v1.py",
           "b_alpha_lancer_v2.py")
CORRECTIFS = ("06_activations-llama-v2.diff", "lenses-neuronpedia-llama-v2.diff", "provenance-chat-llama-v1.diff",
              "causal_lens-graine-v1.diff")
DOSSIER_CORRECTIFS = "docs/notes/neuron-lens-v1/correctifs"
VOISIN_AVANT = {
    "scripts/checks/causal_lens.py": "befb7018f1be937124d938df7b318d0b9e8fd32fd3c497111c7c1722c3b187c6",
    "scripts/06_activations.py": "151d11963d5c43d6593d2482cc4510bddc825b3bc66696be121dc60b8b488035",
    "neuron_lens/lenses.py": "00591cd7b8b213fe6e1f1f6a13eb13f091eebab1a7b879fe9ac1a06116393b6c",
    "neuron_lens/arch.py": "0f1e2262b5b13e5d68cf3e4ff139e756a92dbc1245781839a5d2bd41c992ce12",
}
VOISIN_APRES = {
    "scripts/checks/causal_lens.py": "a9d3bc8e8dde945c4ff0f4a229f30c78b35ee299a4fa1fe34fe75db35252141b",
    "scripts/06_activations.py": "b97bf54b7c3b12f3ec1853000ba66cf5a6056c6c05b6400a8572a44e154cb902",
    "neuron_lens/lenses.py": "2de7d6afe63bc398e17f4ff93ae7b7acdcc3a330e91c728df88bef338008b3e4",
    "neuron_lens/arch.py": "877fa6b0a864d8ffe88d15789ea9fa913a7bc7a529c399b2e001911c4eccf964",
    "data/corpus/act-chat-llama-3.1-8b-instruct.provenance.json": "777aa068a008b38fc22c6758d283e33ac31e31d6c5ed2eed878f7d75050d231d",
}
REFERENCES = {  # provenances du dépôt voisin à 849bfe16 (addendum v3, § 4) : lues AVANT la passe (05 réécrit les siennes)
    "dclm": ("data/corpus/act-dclm.provenance.json", "a26a70773b35e87349107dac27dddf4f134411c2fd28e5fe5e92cc980e4798e5"),
    "zh": ("data/corpus/act-zh.provenance.json", "d0ba016a799ed206eb58e959c54209248ecc1655ac1dfadd61aebf4072f38e5b"),
    "code": ("data/corpus/act-code.provenance.json", "ab2f687d1b2233a2544d40abd531b6aa11591019cedf1ff2bc59753097c7fd98"),
    "chat": ("data/corpus/act-chat-qwen3-8b.provenance.json", "a76c6b02057d1a13b00185d589f063f82254fc8f184526db922b53962d82e784"),
}
RESUME_QWEN = ("data/summary/causal_lens_qwen3-8b.json", "8904c4d34154068293700fbabf967f553415e6969aafebe06e29a452e03830d3")
CORPUS_FICHIERS = {"dclm": "act-dclm.jsonl", "zh": "act-zh.jsonl", "code": "act-code.jsonl", "chat": f"act-chat-{STEM}.jsonl"}
PROVENANCES_PRODUITES = {t: f.replace(".jsonl", ".provenance.json") for t, f in CORPUS_FICHIERS.items()}
LENTILLES_FICHIERS = {
    "J": "llama3.1-8b-it/jlens/Salesforce-wikitext/Llama-3.1-8B-Instruct_jacobian_lens.pt",
    "npJpp": "llama3.1-8b-it/jpp/Salesforce-wikitext/Llama-3.1-8B-Instruct_jpp_lens.pt",
    "npR": "llama3.1-8b-it/rlens/Salesforce-wikitext/Llama-3.1-8B-Instruct_rlens.pt",
}
TOKENISEUR = ("config.json", "generation_config.json", "tokenizer.json", "tokenizer_config.json", "special_tokens_map.json")
_POIDS = re.compile(r"^model(-\d{5}-of-\d{5})?\.safetensors$|^model\.safetensors\.index\.json$")
# audit « tout négatif » (addendum v3, §§ 1-3) : sorties publiées de `measure` pour Qwen3-8B et ce que `score` lit
QWEN_REV = "b968826d9c46dd6066d109eabc6255188de91218"
QWEN_POIDS = {f"model-0000{i}-of-00005.safetensors": h for i, h in enumerate((
    "31d6a825ae35f11fb85b195b4c42c146c051e446433125a215336abdf95cbf5f", "5991236cea6fe21f3d43cab0f0e84448734fbbe0789816202989f2ddc9d18282",
    "c5185c4794be2d8a9784d5753c9922db38df478ce11f9ed0b415b7304d896836", "b5ee7de71fbf17db3d5704e0c8f2bc7d005ca9e1d7ca2aeb19827b0cfcaa917a",
    "20c2d6366ab85c90786ccdd829cd2b9e7d30ef3b2ebbb998280e7e4014b542ff"), start=1)}
QWEN_TOKENISEUR = {"tokenizer.json": "aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4"}
CATALOGUE = ("stdlogits/neuron-lens", "2f19669198445347a4dbd1a2c2324652ee31b0a2")
CATALOGUE_FICHIERS = {"qwen3-8b/causal/causal.pt": "b632100452a6f8e9f6d9bd66193755845878f5123f34f0053ce1a31eca80773c",
                      "qwen3-8b/token_counts.pt": "10e90037470c51bfd75e15ff8d28a830172a5b5c9f9a6c38024a768534e5697b"}
RS_LENSES = ("stdlogits/rs-lenses", "984fe3d2a46a35580764260ea438cbd6ac17c486", "qwen3-8b/r-lens/lens.pt",
             "5eaa4d56e10d0c535b5170d5aaaa1174fb8dedf0fddb2f9821cec0aa1050fae1")
QWEN_J = "qwen3-8b/jlens/Salesforce-wikitext/Qwen3-8B_jacobian_lens.pt"
SEUIL_CAS_SAIN_QWEN = 0.05  # texte gelé, audit « tout négatif » : « écart > 0,05 aux valeurs publiées »

ETAPES = ("preparer", "telecharger-tokeniseur", "b0", "telecharger-poids", "corpus", "partie2", "fumee", "passe", "b3", "measure",
          "score", "grandeurs", "verdicts", "audit-trop-beau", "audit-tout-negatif")
PREREQUIS = {"preparer": (), "telecharger-tokeniseur": ("preparer",), "b0": ("telecharger-tokeniseur",),
             "telecharger-poids": ("b0",), "corpus": ("telecharger-poids",), "partie2": ("corpus",), "fumee": ("partie2",),
             "passe": ("fumee",), "b3": ("passe",), "measure": ("b3",), "score": ("measure",), "grandeurs": ("score",),
             "verdicts": ("grandeurs",), "audit-trop-beau": ("verdicts",), "audit-tout-negatif": ("verdicts",)}
JETON = frozenset({"telecharger-tokeniseur", "telecharger-poids"})
EN_LIGNE = JETON | {"corpus", "audit-tout-negatif"}
# échéances du devis v2, § 1 (heures : attendu haut, pire cas) ; les étapes 2 bis et 3 bis du devis sont `telecharger-poids` et `partie2`
ECHEANCES = {"preparer": (0.05, 0.2), "telecharger-tokeniseur": (0.1, 0.2), "b0": (0.3, 0.5), "telecharger-poids": (0.2, 0.4),
             "corpus": (0.3, 0.5), "partie2": (0.1, 0.3), "fumee": (0.1, 0.2), "passe": (1.4, 2.5), "b3": (0.05, 0.1),
             "measure": (1.0, 2.0), "score": (0.2, 0.5), "grandeurs": (0.1, 0.3), "verdicts": (0.05, 0.1),
             "audit-trop-beau": (1.3, 2.8), "audit-tout-negatif": (0.5, 0.8)}
_GO = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")
ORIGINAL_06 = ("scripts/06_activations.py", "151d11963d5c43d6593d2482cc4510bddc825b3bc66696be121dc60b8b488035")


class Arret(Exception):
    """Arrêt de la course (consigné, aucun repli)."""


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


def env_enfant(voisin: Path, hors_ligne: bool, modele: str = LLAMA, **extra) -> dict:
    """Environnement d'un processus enfant : sans aucun secret (HF_TOKEN, HUGGING_FACE_HUB_TOKEN, GH_TOKEN), code voisin importable."""
    env = {k: v for k, v in os.environ.items() if k not in ("HF_TOKEN", "HUGGING_FACE_HUB_TOKEN", "GH_TOKEN")}
    env.pop("HF_HUB_OFFLINE", None)
    if hors_ligne:
        env["HF_HUB_OFFLINE"] = "1"
    env |= {"NEURON_LENS_MODEL": modele, "PYTHONPATH": str(voisin), "HF_HUB_DISABLE_TELEMETRY": "1", "PYTHONUNBUFFERED": "1"}
    return env | {k: str(v) for k, v in extra.items()}


def executer(cmd, cwd, env, journal: Path, timeout_s: float) -> dict:
    """Processus enfant, sortie dans `journal` (ajout) ; rend code, durée et les dernières lignes. Dépassement du délai : code 124."""
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
    return {"code": code, "duree_s": round(time.time() - t0, 1), "fin": lignes[-30:]}


def resume_pytest(sortie: dict) -> str:
    """Dernière ligne de bilan de pytest (« … passed … »), ou la dernière ligne."""
    for l in reversed(sortie["fin"]):
        if re.search(r"\b(passed|failed|error|skipped|no tests ran)\b", l):
            return l.strip()
    return (sortie["fin"] or [""])[-1].strip()


# ------------------------------------------------------------------------------------------------ cache du hub

def dossier_cache(hf_home: Path, depot: str, type_depot: str = "model") -> Path:
    return Path(hf_home) / "hub" / f"{type_depot}s--{depot.replace('/', '--')}"


def epingler(hf_home: Path, depot: str, revision: str, type_depot: str = "model") -> None:
    """`refs/main` = révision épinglée (les appels du code voisin, sans révision, résolvent `main` dans le cache hors ligne)."""
    ref = dossier_cache(hf_home, depot, type_depot) / "refs" / "main"
    if ref.exists() and ref.read_text().strip() != revision:
        raise Arret(f"cache du hub : refs/main de {depot} vaut {ref.read_text().strip()[:12]}…, pas {revision[:12]}…")
    ref.parent.mkdir(parents=True, exist_ok=True)
    ref.write_text(revision)


# ------------------------------------------------------------------------------------------------ contexte et état

@dataclass
class Contexte:
    racine: Path
    run_id: str
    hf_home: Path
    executer: object = executer
    hub: object = None  # (model_info, hf_hub_download) remplaçables pour les essais
    journal_etapes: dict = field(default_factory=dict)

    @property
    def voisin(self) -> Path:
        return self.racine / "voisin" / "neuron-lens"

    @property
    def diag(self) -> Path:
        return self.racine / "diag" / self.run_id

    @property
    def original_06(self) -> Path:
        """Copie du script d'activations d'origine, gardée avant les correctifs (hors du code voisin, non poussée)."""
        return self.racine / "originaux" / "06_activations.py"

    @property
    def manifeste(self) -> Path:
        return self.racine / "runs" / self.run_id / "manifeste.json"

    def journal(self, etape: str) -> Path:
        return self.diag / "journaux" / f"{etape}.log"

    def resultat(self, etape: str) -> Path:
        return self.diag / f"b-alpha-{etape}.json"

    def lire(self, etape: str) -> dict:
        from controle_ia.manifeste import verifier_resultat
        return verifier_resultat(self.racine, self.resultat(etape))["resultat"]

    def fait(self, etape: str) -> bool:
        if not self.resultat(etape).exists():
            return False
        self.lire(etape)  # un résultat altéré arrête tout (GardeArret)
        return True

    def hub_fonctions(self):
        if self.hub is not None:
            return self.hub
        from huggingface_hub import HfApi, hf_hub_download
        return HfApi().model_info, hf_hub_download


def suite(ctx: Contexte):
    """Prochaine étape à jouer, ou None quand la course est finie. Les audits ne sont joués que s'ils sont requis par `verdicts`."""
    for e in ETAPES:
        if ctx.fait(e):
            continue
        if e.startswith("audit-"):
            if not ctx.fait("verdicts") or e not in ctx.lire("verdicts").get("audits_requis", []):
                continue
        return e
    return None


def exiger_prerequis(ctx: Contexte, etape: str) -> None:
    for p in PREREQUIS[etape]:
        if not ctx.fait(p):
            raise Arret(f"{etape} : étape préalable non faite : {p}")
    if etape.startswith("audit-") and etape not in ctx.lire("verdicts").get("audits_requis", []):
        raise Arret(f"{etape} : audit non requis par les verdicts")


def _arret(ctx: Contexte, etape: str, e: BaseException) -> None:
    from controle_ia.manifeste import ecrire_resultat
    if not ctx.manifeste.exists():
        return
    n = 1
    while (ctx.diag / f"arret-{etape}-{n}.json").exists():
        n += 1
    ecrire_resultat(ctx.racine, ctx.manifeste, f"arret-{etape}-{n}", {"etape": etape, "type": type(e).__name__,
                                                                      "message": str(e)[:2000]})


def jouer(ctx: Contexte, etape: str, env=None) -> Path | None:
    """Joue une étape (rien si elle est déjà faite). Rend le chemin du résultat scellé."""
    from controle_ia.manifeste import ecrire_resultat
    pb = verifier_environnement(etape, os.environ if env is None else env)
    if pb:
        raise SystemExit("environnement non conforme : " + " ; ".join(pb))
    if etape != "preparer" and not ctx.manifeste.exists():
        raise SystemExit(f"{etape} : manifeste absent (préparer d'abord)")
    if etape != "preparer" and ctx.fait(etape):
        return ctx.resultat(etape)
    debut = time.time()
    try:
        if etape != "preparer":
            exiger_prerequis(ctx, etape)
        elif ctx.fait("preparer"):
            return ctx.resultat("preparer")
        contenu = ETAPE_FONCTIONS[etape](ctx)
    except BaseException as e:  # noqa: BLE001 — consigné puis relevé : aucun repli
        _arret(ctx, etape, e)
        raise
    duree = round(time.time() - debut, 1)
    attendu, pire = ECHEANCES[etape]
    contenu |= {"etape": etape, "debut_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(debut)), "duree_s": duree,
                "echeance_h": {"attendu": attendu, "pire_cas": pire}, "depassement_pire_cas": duree > pire * 3600}
    return ecrire_resultat(ctx.racine, ctx.manifeste, f"b-alpha-{etape}", contenu)


# ------------------------------------------------------------------------------------------------ étapes

def verifier_pieces(racine: Path) -> dict:
    from controle_ia.scellement import verifier
    out = {}
    for chemin, attendue in PIECES.items():
        if verifier(racine / chemin) != attendue:
            raise Arret(f"empreinte inattendue : {chemin}")
        out[chemin] = attendue
    for m in MODULES:
        out["src/controle_ia/neuron_lens/" + m] = verifier(racine / "src/controle_ia/neuron_lens" / m)
    for d in CORRECTIFS:
        out[f"{DOSSIER_CORRECTIFS}/{d}"] = verifier(racine / DOSSIER_CORRECTIFS / d)
    for e in p2.ESSAIS_B0:
        out[f"{DOSSIER_CORRECTIFS}/{e}"] = verifier(racine / DOSSIER_CORRECTIFS / e)
    return out


def configuration(pieces: dict) -> dict:
    return {"go_id": GO_ATTENDU, "tranche": "B-α", "modele": LLAMA, "revision": p2.REVISION_LLAMA, "lentilles": list(SPECS),
            "commit_voisin": p2.COMMIT_VOISIN, "correctifs": list(CORRECTIFS), "pieces": pieces, "corpus": DOCS_CORPUS,
            "graines": {"neurones": "random.Random(0) du dépôt (measure, score) ; graine 1 pour l'audit « trop beau » (correctif (3))",
                        "autres": f"SeedSequence(entropy={ENTROPIE}), branche « B-α », tâches consignées au manifeste"},
            "precision": "bf16 (06_activations, measure) ; score en float32 sur le processeur"}


def etape_preparer(ctx: Contexte) -> dict:
    from controle_ia.manifeste import creer_manifeste
    from controle_ia.scellement import sceller
    pieces = verifier_pieces(ctx.racine)
    avant = {f: sha256(ctx.voisin / f) for f in VOISIN_AVANT if (ctx.voisin / f).exists()}
    deja = all((ctx.voisin / f).exists() and sha256(ctx.voisin / f) == h for f, h in VOISIN_APRES.items())
    if not deja and avant != VOISIN_AVANT:
        raise Arret(f"code voisin inattendu avant les correctifs : {avant}")
    refs = {t: sha256(ctx.voisin / c) for t, (c, _) in REFERENCES.items()}
    if refs != {t: h for t, (_, h) in REFERENCES.items()}:
        raise Arret(f"provenances de référence inattendues : {refs}")
    if sha256(ctx.voisin / RESUME_QWEN[0]) != RESUME_QWEN[1]:
        raise Arret("résumé publié de Qwen3-8B inattendu")
    if not ctx.manifeste.exists():
        creer_manifeste(ctx.racine, ctx.run_id, configuration(pieces), ["b-alpha-intervalles"], entropie=ENTROPIE, decisif=True,
                        prereg=ctx.racine / next(iter(PIECES)), commande=" ".join(sys.argv))
    dref = ctx.diag / "references"
    dref.mkdir(parents=True, exist_ok=True)
    for t, (c, h) in REFERENCES.items():
        cible = dref / Path(c).name
        if not cible.exists():
            shutil.copyfile(ctx.voisin / c, cible)
        if sha256(cible) != h:
            raise Arret(f"copie de la référence {t} altérée")
        sceller(cible)
    if not deja:
        ctx.original_06.parent.mkdir(parents=True, exist_ok=True)
        if not ctx.original_06.exists():
            shutil.copyfile(ctx.voisin / ORIGINAL_06[0], ctx.original_06)
    if not ctx.original_06.exists() or sha256(ctx.original_06) != ORIGINAL_06[1]:
        raise Arret("copie du script d'activations d'origine absente ou altérée (exigée par l'essai du correctif (1))")
    if not deja:
        # depuis la racine du dépôt réduit : lancé d'un sous-dossier, `git apply` ignorerait en silence les chemins du correctif
        rel = str(ctx.voisin.relative_to(ctx.racine))
        for mode in ("--check", None):
            for d in CORRECTIFS:
                cmd = ["git", "apply", f"--directory={rel}"] + ([mode] if mode else []) + [str(ctx.racine / DOSSIER_CORRECTIFS / d)]
                r = subprocess.run(cmd, cwd=ctx.racine, capture_output=True, text=True)
                if r.returncode != 0:
                    raise Arret(f"correctif {d} non applicable : {r.stderr[-500:]}")
    apres = {f: sha256(ctx.voisin / f) for f in VOISIN_APRES}
    if apres != VOISIN_APRES:
        raise Arret(f"code voisin inattendu après les correctifs : {apres}")
    return {"pieces": pieces, "voisin_avant": VOISIN_AVANT, "voisin_apres": apres,
            "original_06": {"chemin": str(ctx.original_06.relative_to(ctx.racine)), "sha256": ORIGINAL_06[1]},
            "references": {t: h for t, (_, h) in REFERENCES.items()},
            "echeances_h": {e: {"attendu": a, "pire_cas": p} for e, (a, p) in ECHEANCES.items()}}


def _attendus_hub(info, revision: str) -> dict:
    if getattr(info, "sha", None) != revision:
        raise Arret(f"le hub ne sert pas la révision épinglée ({getattr(info, 'sha', None)})")
    out = {}
    for s in info.siblings:
        n = s.rfilename
        if n in TOKENISEUR or _POIDS.match(n):
            lfs = getattr(s, "lfs", None)
            out[n] = ({"lfs_sha256": lfs.sha256, "taille": lfs.size} if lfs else {"git_sha1": s.blob_id, "taille": s.size})
    for n in TOKENISEUR:
        if n not in out:
            raise Arret(f"fichier du tokeniseur absent de la révision épinglée : {n}")
    if not any(_POIDS.match(n) and n.endswith(".safetensors") for n in out):
        raise Arret("aucun fichier de poids à la révision épinglée")
    return out


def _controle_fichier(chemin: Path, attendu: dict) -> dict:
    e = p2.empreintes_fichier(chemin)
    if "lfs_sha256" in attendu and e["sha256"] != attendu["lfs_sha256"]:
        raise Arret(f"{chemin.name} : sha256 différente de celle du hub")
    if "git_sha1" in attendu and e["git_sha1"] != attendu["git_sha1"]:
        raise Arret(f"{chemin.name} : empreinte git différente de celle du hub")
    return e


def _charger_tokeniseur_avec_cle() -> int:
    from transformers import AutoTokenizer
    return len(AutoTokenizer.from_pretrained(LLAMA, revision=p2.REVISION_LLAMA))


def etape_telecharger_tokeniseur(ctx: Contexte, charger_tokeniseur=_charger_tokeniseur_avec_cle) -> dict:
    model_info, telecharger = ctx.hub_fonctions()
    attendus = _attendus_hub(model_info(LLAMA, revision=p2.REVISION_LLAMA, files_metadata=True), p2.REVISION_LLAMA)
    fichiers = {}
    for n in TOKENISEUR:  # clé lue par la bibliothèque dans l'environnement, par son nom ; jamais passée ici
        fichiers[n] = _controle_fichier(Path(telecharger(LLAMA, n, revision=p2.REVISION_LLAMA)), attendus[n])
    epingler(ctx.hf_home, LLAMA, p2.REVISION_LLAMA)
    lentilles = {}
    for s, f in LENTILLES_FICHIERS.items():  # dépôt public : aucune clé envoyée
        chemin = Path(telecharger(NP, f, revision=p2.REVISION_NEURONPEDIA, token=False))
        e = p2.empreintes_fichier(chemin)
        if e["sha256"] != p2.LENTILLES[s]:
            raise Arret(f"lentille {s} : empreinte inattendue")
        lentilles[s] = {"chemin": f, "sha256": e["sha256"], "taille": e["taille"]}
    config = {}
    for n, h in p2.CONFIG_NEURONPEDIA.items():
        e = p2.empreintes_fichier(Path(telecharger(NP, f"llama3.1-8b-it/{n}", revision=p2.REVISION_NEURONPEDIA, token=False)))
        if e["git_sha1"] != h:
            raise Arret(f"Neuronpedia {n} : empreinte git inattendue (convention lue sur une autre version)")
        config[n] = {"git_sha1": e["git_sha1"], "taille": e["taille"]}
    epingler(ctx.hf_home, NP, p2.REVISION_NEURONPEDIA)
    # premier chargement, avec la clé, DANS CE PROCESSUS (la clé n'est jamais transmise à un enfant), à la révision épinglée : il
    # inscrit dans le cache les absences des fichiers facultatifs du tokeniseur
    nv = charger_tokeniseur()
    # puis sans clé, en ligne et hors ligne (processus enfants) : le chargement doit passer par le cache épinglé seul
    sonde2 = [sys.executable, "-c", f"from transformers import AutoTokenizer; t = AutoTokenizer.from_pretrained({LLAMA!r}); "
              "print('nv', len(t))"]
    s2 = ctx.executer(sonde2, ctx.racine, env_enfant(ctx.voisin, hors_ligne=False), ctx.journal("telecharger-tokeniseur"), 600)
    s3 = ctx.executer(sonde2, ctx.racine, env_enfant(ctx.voisin, hors_ligne=True), ctx.journal("telecharger-tokeniseur"), 600)
    for nom, x in (("sans clé en ligne", s2), ("sans clé hors ligne", s3)):
        if x["code"] != 0 or f"nv {nv}" not in "\n".join(x["fin"]):
            raise Arret(f"chargement du tokeniseur {nom} en échec ou autre tokeniseur (code {x['code']})")
    return {"attendus": attendus, "tokeniseur": fichiers, "lentilles": {"revision": p2.REVISION_NEURONPEDIA, "fichiers": lentilles},
            "config_neuronpedia": config, "nv": nv, "sondes": {"sans_cle_en_ligne": s2["code"], "sans_cle_hors_ligne": s3["code"]}}


def _lentille_controlee(voisin: Path, spec: str) -> dict:
    """Lecture d'une lentille par `neuronpedia_lens` (code voisin corrigé, dans ce processus, hors ligne) et contrôle de B0."""
    import numpy as np

    from controle_ia.neuron_lens.verdicts_b_alpha_v3 import controle_lentille
    if str(voisin) not in sys.path:
        sys.path.insert(0, str(voisin))
    from neuron_lens.lenses import neuronpedia_lens
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        J = neuronpedia_lens(LENTILLES_FICHIERS[spec])
    sortie = tampon.getvalue()
    m = re.search(r"other keys (\[.*\])", sortie)
    arrets, defauts = controle_lentille({l: np.asarray(v.float()) for l, v in J.items()})
    return {"arrets": arrets, "defauts": defauts, "autres_cles": m.group(1) if m else None, "sortie": sortie.strip()[-500:]}


def _pytest(ctx: Contexte, cible, cwd, env, etape) -> dict:
    s = ctx.executer([sys.executable, "-m", "pytest", "-q", "-rs", "-p", "no:cacheprovider", str(cible)], cwd, env,
                     ctx.journal(etape), 1800)
    return {"code": s["code"], "resume": resume_pytest(s)}


def _ok_pytest(x: dict) -> bool:
    return x["code"] == 0 and "passed" in x["resume"] and not re.search(r"\b(failed|error|skipped)\b", x["resume"])


def etape_b0(ctx: Contexte, lire_lentille=_lentille_controlee) -> dict:
    if not ctx.original_06.exists() or sha256(ctx.original_06) != ORIGINAL_06[1]:
        raise Arret("B0 : copie du script d'activations d'origine absente ou altérée")
    env = env_enfant(ctx.voisin, hors_ligne=True, NEURON_LENS_ROOT=ctx.voisin, NEURON_LENS_ORIG=ctx.original_06)
    essais = {e: _pytest(ctx, ctx.racine / DOSSIER_CORRECTIFS / e, ctx.voisin, env, "b0") for e in p2.ESSAIS_B0}
    lentilles = {s: lire_lentille(ctx.voisin, s) for s in LENTILLES_FICHIERS}
    env_b3 = env_enfant(ctx.voisin, hors_ligne=True) | {"PYTHONPATH": str(ctx.racine / "src")}
    b3 = _pytest(ctx, ctx.racine / "tests/test_neuron_lens_verdicts_b_alpha_v3.py", ctx.racine, env_b3, "b0")
    res = {"essais": essais, "lentilles": lentilles, "verdicts_b3": b3}
    pb = [e for e, x in essais.items() if not _ok_pytest(x)]
    pb += [f"lentille {s} : {x['arrets']}" for s, x in lentilles.items() if x["arrets"]]
    if not _ok_pytest(b3):
        pb.append("code des verdicts (B.3)")
    if pb:
        raise Arret("B0 en échec : " + " ; ".join(pb))
    return res


def etape_telecharger_poids(ctx: Contexte) -> dict:
    _, telecharger = ctx.hub_fonctions()
    attendus = ctx.lire("telecharger-tokeniseur")["attendus"]
    fichiers = {}
    for n in sorted(attendus):
        if n in TOKENISEUR:
            continue
        fichiers[n] = _controle_fichier(Path(telecharger(LLAMA, n, revision=p2.REVISION_LLAMA)), attendus[n])
    epingler(ctx.hf_home, LLAMA, p2.REVISION_LLAMA)
    return {"poids": fichiers}


def etape_corpus(ctx: Contexte) -> dict:
    sonde = [sys.executable, "-c", f"from transformers import AutoTokenizer; print('nv', len(AutoTokenizer.from_pretrained({LLAMA!r})))"]
    s = ctx.executer(sonde, ctx.voisin, env_enfant(ctx.voisin, hors_ligne=False), ctx.journal("corpus"), 600)
    if s["code"] != 0:
        raise Arret("tokeniseur non chargé sans clé en ligne : le corpus ne part pas")
    c05 = ctx.executer([sys.executable, "scripts/05_act_corpus.py", "--docs", DOCS_CORPUS], ctx.voisin,
                       env_enfant(ctx.voisin, hors_ligne=False), ctx.journal("corpus"), 2 * 3600)
    if c05["code"] != 0:
        raise Arret(f"05_act_corpus.py en échec (code {c05['code']})")
    c03 = ctx.executer([sys.executable, "scripts/03_token_counts.py"], ctx.voisin, env_enfant(ctx.voisin, hors_ligne=True),
                       ctx.journal("corpus"), 2 * 3600)
    if c03["code"] != 0:
        raise Arret(f"03_token_counts.py en échec (code {c03['code']})")
    return {"05_act_corpus": {"code": c05["code"], "duree_s": c05["duree_s"]},
            "03_token_counts": {"code": c03["code"], "duree_s": c03["duree_s"]}}


def _compter_lignes(chemin: Path) -> int:
    with open(chemin, encoding="utf-8") as fh:
        return sum(1 for l in fh if l.strip())


def _debuts_et_gardes(voisin: Path) -> tuple[dict, dict]:
    """Comptes des jetons de début par tranche (documents coupés comme la passe les coupe) et liste `catalog.kept` de Llama, par
    le code voisin (hors ligne)."""
    from controle_ia.neuron_lens.controles_b0_v2 import compter_debuts, empreinte_liste_gardee
    if str(voisin) not in sys.path:
        sys.path.insert(0, str(voisin))
    from neuron_lens import catalog
    from neuron_lens.corpus import _rows, act_file
    tok = catalog.tokenizer(LLAMA)
    debuts = {t: {str(k): v for k, v in compter_debuts(_rows(act_file(t, LLAMA), tok, SEQ), tok.bos_token_id).items()}
              for t in CORPUS_FICHIERS}
    k = catalog.kept(LLAMA).tolist()
    return debuts, {"n": len(k), "sha256": empreinte_liste_gardee(k)}


def _versions() -> dict:
    out = {"python": platform.python_version()}
    for k in ("torch", "transformers", "numpy", "huggingface_hub", "safetensors", "pyarrow", "tokenizers", "datasets"):
        try:
            out[k] = importlib.metadata.version(k)
        except importlib.metadata.PackageNotFoundError:
            out[k] = ""
    return out


def releve_partie2(ctx: Contexte, debuts_et_gardes=_debuts_et_gardes) -> dict:
    t1, poids, b0 = ctx.lire("telecharger-tokeniseur"), ctx.lire("telecharger-poids"), ctx.lire("b0")
    corpus = {}
    d = ctx.voisin / "data" / "corpus"
    for t, f in CORPUS_FICHIERS.items():
        corpus[t] = {"fichier": f, "sha256": sha256(d / f), "taille": (d / f).stat().st_size, "lignes": _compter_lignes(d / f)}
    produites = {t: json.loads((d / f).read_text(encoding="utf-8")) for t, f in PROVENANCES_PRODUITES.items()}
    references = {t: json.loads((ctx.diag / "references" / Path(c).name).read_text(encoding="utf-8")) for t, (c, _) in REFERENCES.items()}
    debuts, kept = debuts_et_gardes(ctx.voisin)
    return {"date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "instance": os.environ.get("INSTANCE_ID", "inconnue"),
            "commit_reduit": os.environ.get("COMMIT_REDUIT", ""), "commit_source": os.environ.get("COMMIT_SOURCE", ""),
            "commit_voisin": p2.COMMIT_VOISIN,
            "modele": {"revision": p2.REVISION_LLAMA, "fichiers": t1["tokeniseur"] | poids["poids"], "attendus": t1["attendus"]},
            "lentilles": t1["lentilles"], "config_neuronpedia": t1["config_neuronpedia"], "corpus": corpus,
            "provenances": {"produites": produites, "references": references}, "debuts": debuts, "kept": kept,
            "versions": _versions(), "controles": {"essais": b0["essais"], "lentilles": {s: {k: v for k, v in x.items() if k != "sortie"}
                                                                                           for s, x in b0["lentilles"].items()},
                                                   "verdicts_b3": b0["verdicts_b3"]}}


def chemin_partie2(ctx: Contexte) -> Path:
    return ctx.diag / "addendum-partie2-b-alpha-v1.md"


def etape_partie2(ctx: Contexte, debuts_et_gardes=_debuts_et_gardes) -> dict:
    from controle_ia.scellement import verifier
    releve = releve_partie2(ctx, debuts_et_gardes)
    texte, pb = p2.rediger(releve)
    chemin = chemin_partie2(ctx)
    if chemin.exists():  # reprise : le fichier déjà écrit doit être identique, sauf la date du relevé
        ancien = chemin.read_text(encoding="utf-8")
        if re.sub(r"- date : \S+", "", ancien) != re.sub(r"- date : \S+", "", texte):
            raise Arret("partie 2 déjà écrite, différente du relevé refait : R12, aucun écrasement")
        h = verifier(chemin)
    else:
        h = p2.ecrire_et_sceller(chemin, texte)
    if pb:
        raise Arret("partie 2 de l'addendum : écarts : " + " ; ".join(pb[:10]))
    return {"partie2": str(chemin.relative_to(ctx.racine)), "sha256": h, "ecarts": pb, "releve": releve}


def _garde_partie2(ctx: Contexte) -> None:
    from controle_ia.scellement import verifier
    r = ctx.lire("partie2")
    if r.get("ecarts") or verifier(chemin_partie2(ctx)) != r.get("sha256"):
        raise Arret("partie 2 de l'addendum absente, altérée ou avec écarts : la fumée ne part pas")


def etape_fumee(ctx: Contexte) -> dict:
    _garde_partie2(ctx)
    s = ctx.executer([sys.executable, "scripts/06_activations.py", "--docs", "64"], ctx.voisin, env_enfant(ctx.voisin, True),
                     ctx.journal("fumee"), 3600)
    if s["code"] != 0:
        raise Arret(f"fumée en échec (code {s['code']})")
    return {"code": s["code"], "duree_passe_s": s["duree_s"], "fin": s["fin"][-10:]}


def etape_passe(ctx: Contexte) -> dict:
    _garde_partie2(ctx)
    s = ctx.executer([sys.executable, "scripts/06_activations.py"], ctx.voisin, env_enfant(ctx.voisin, True), ctx.journal("passe"),
                     6 * 3600)
    if s["code"] != 0:
        raise Arret(f"passe complète en échec (code {s['code']})")
    acts = ctx.voisin / "data" / "acts" / f"{STEM}.pt"
    if not acts.exists():
        raise Arret("passe complète : fichier des activations absent")
    return {"code": 0, "duree_passe_s": s["duree_s"], "acts": {"sha256": sha256(acts), "taille": acts.stat().st_size},
            "fin": s["fin"][-10:]}


def etape_b3(ctx: Contexte) -> dict:
    env_b3 = env_enfant(ctx.voisin, hors_ligne=True) | {"PYTHONPATH": str(ctx.racine / "src")}
    x = _pytest(ctx, ctx.racine / "tests/test_neuron_lens_verdicts_b_alpha_v3.py", ctx.racine, env_b3, "b3")
    if not _ok_pytest(x):
        raise Arret(f"code des verdicts (B.3) rejoué en échec avant measure : {x}")
    return {"verdicts_b3": x}


def _causal(ctx: Contexte, graine: int = 0) -> Path:
    return ctx.voisin / "data" / "causal" / (f"{STEM}-causal.pt" if graine == 0 else f"{STEM}-causal-seed{graine}.pt")


def _resume(ctx: Contexte, tag: str = "", stem: str = STEM) -> Path:
    return ctx.voisin / "data" / "summary" / f"causal_lens_{tag + '_' if tag else ''}{stem}.json"


def _measure(ctx: Contexte, graine: int, etape: str) -> dict:
    s = ctx.executer([sys.executable, "scripts/checks/causal_lens.py", "measure"] + (["--seed", str(graine)] if graine else []),
                     ctx.voisin, env_enfant(ctx.voisin, True), ctx.journal(etape), 5 * 3600)
    if s["code"] != 0 or not _causal(ctx, graine).exists():
        raise Arret(f"measure (graine {graine}) en échec (code {s['code']})")
    f = _causal(ctx, graine)
    return {"code": 0, "duree_measure_s": s["duree_s"], "causal": {"chemin": str(f.relative_to(ctx.voisin)), "sha256": sha256(f),
                                                                    "taille": f.stat().st_size}}


def _score(ctx: Contexte, graine: int, tag: str, etape: str) -> dict:
    from controle_ia.scellement import sceller
    cmd = [sys.executable, "scripts/checks/causal_lens.py", "score", "--lenses", ",".join(SPECS)]
    cmd += (["--seed", str(graine)] if graine else []) + (["--tag", tag] if tag else [])
    s = ctx.executer(cmd, ctx.voisin, env_enfant(ctx.voisin, True), ctx.journal(etape), 2 * 3600)
    j = _resume(ctx, tag)
    if s["code"] != 0 or not j.exists():
        raise Arret(f"score (graine {graine}) en échec (code {s['code']})")
    out = {}
    for src in (j, j.with_suffix(".log")):
        cible = ctx.diag / src.name
        if not cible.exists():
            shutil.copyfile(src, cible)
        out[src.suffix[1:]] = {"chemin": str(cible.relative_to(ctx.racine)), "sha256": sceller(cible)}
    return {"code": 0, "duree_score_s": s["duree_s"], "resume": out}


def etape_measure(ctx: Contexte) -> dict:
    return _measure(ctx, 0, "measure")


def etape_score(ctx: Contexte) -> dict:
    return _score(ctx, 0, "", "score")


def _grandeurs(ctx: Contexte, graine: int, tag: str, nom: str, calculer=None) -> dict:
    from controle_ia.scellement import sceller
    sortie = ctx.diag / nom
    causal, resume = _causal(ctx, graine), ctx.diag / _resume(ctx, tag).name
    score_json = json.loads(resume.read_text(encoding="utf-8"))
    if calculer is None:
        import torch

        from controle_ia.neuron_lens import grandeurs_b_alpha_v1 as g
        if str(ctx.voisin) not in sys.path:
            sys.path.insert(0, str(ctx.voisin))
        saved = torch.load(causal, weights_only=False, mmap=True)
        lire, nv, keep = g.lecteur_voisin(LLAMA, SPECS)
        res = g.grandeurs(saved, lire, SPECS, nv, keep, F_LLAMA)
        ecarts = g.comparer_a_score(res["table"], score_json)
        if ecarts:
            raise Arret("grandeurs par pôle infidèles à score : " + " ; ".join(ecarts[:5]))
        if not sortie.exists():
            g.ecrire(sortie, res, sha256(causal), sha256(resume), ecarts)
    else:
        res, ecarts = calculer(causal, score_json, sortie)
        if ecarts:
            raise Arret("grandeurs par pôle infidèles à score : " + " ; ".join(ecarts[:5]))
    return {"grandeurs": str(sortie.relative_to(ctx.racine)), "sha256": sceller(sortie), "n": res["n"], "ecartes": res["ecartes"]}


def etape_grandeurs(ctx: Contexte, calculer=None) -> dict:
    return _grandeurs(ctx, 0, "", "grandeurs-par-pole-b-alpha-v1.json", calculer)


def intervalles(ctx: Contexte, n_tirages: int = 2000) -> dict:
    """Intervalles à 95 % de `r_med` par couche (`npR` et `logit`, « steer 1x »), par rééchantillonnage des pôles retenus tirés au
    hasard ; rapportés sans critère (devis v2, § 4, point 3). Graine : tâche « b-alpha-intervalles » du manifeste."""
    import numpy as np

    from controle_ia.manifeste import generateur, lire_manifeste
    man, _ = lire_manifeste(ctx.manifeste)
    rng = generateur(man["graines"]["b-alpha-intervalles"])
    poles = json.loads((ctx.diag / "grandeurs-par-pole-b-alpha-v1.json").read_text(encoding="utf-8"))["poles"]
    out = {}
    for s in ("npR", "logit"):
        par_couche = []
        for l in range(32):
            r = np.array([p["lectures"]["steer 1x"][s]["r"] for p in poles if p["couche"] == l and p["aleatoire"]
                          and p["lectures"]["steer 1x"][s]["motif"] == "retenu"])
            if len(r) == 0:
                par_couche.append(None)
                continue
            meds = np.median(rng.choice(r, size=(n_tirages, len(r)), replace=True), axis=1)
            par_couche.append([round(float(x), 4) for x in np.quantile(meds, [0.025, 0.975])])
        out[s] = par_couche
    return {"n_tirages": n_tirages, "steer 1x": out}


def etape_verdicts(ctx: Contexte) -> dict:
    from controle_ia.neuron_lens import verdicts_b_alpha_v3 as vb
    score_json = json.loads((ctx.diag / _resume(ctx).name).read_text(encoding="utf-8"))
    t = {c: {s: score_json["targets"][c][s] for s in vb.LENTILLES} for c in vb.CIBLES}
    n = ctx.lire("grandeurs")["n"]
    b0 = ctx.lire("b0")
    identite = any(x["defauts"] for x in b0["lentilles"].values())
    v = vb.verdict(t, n, essais_ok=True, matrices_identite=identite)
    requis = []
    if any(a.startswith("trop beau") for a in v.audit_requis):
        requis.append("audit-trop-beau")
    if any(a.startswith("tout négatif") for a in v.audit_requis):
        requis.append("audit-tout-negatif")
    return {"verdict": asdict(v), "audits_requis": requis, "intervalles": intervalles(ctx),
            "note": "brut : la lecture reste à un lecteur neuf (devis v2, m8)"}


def etape_audit_trop_beau(ctx: Contexte, calculer=None) -> dict:
    m = _measure(ctx, 1, "audit-trop-beau")
    s = _score(ctx, 1, "seed1", "audit-trop-beau")
    gr = _grandeurs(ctx, 1, "seed1", "grandeurs-par-pole-b-alpha-graine1-v1.json", calculer)
    poles = json.loads((ctx.diag / "grandeurs-par-pole-b-alpha-v1.json").read_text(encoding="utf-8"))["poles"]
    temoin_apparie = all(p["temoin"] != p["neurone"] for p in poles)
    n0 = ctx.lire("grandeurs")["n"]
    return {"measure": m, "score": s, "grandeurs": gr, "temoin_bien_apparie": temoin_apparie,
            "pilotage_norme_non_nulle": {c: min(n0[c]) for c in ("steer 1x", "steer 4x")}}


def ecarts_qwen(table: dict, publie: dict) -> dict:
    """max |Δ r_med| par (cible, lentille) entre `score` rejoué sur la sortie publiée de `measure` et le résumé publié. « hub » est
    rapporté face à « R:dclm » (même lentille R publiée sous deux noms : lecture déclarée), sans jugement."""
    import numpy as np
    out = {}
    for c in table:
        for s, ref in (("logit", "logit"), ("J", "J"), ("hub", "R:dclm")):
            a, b = table[c].get(s), publie["targets"].get(c, {}).get(ref)
            if a is None or b is None or list(a["layer"]) != list(b["layer"]):
                out[f"{c}|{s}"] = None
                continue
            out[f"{c}|{s}"] = round(float(np.max(np.abs(np.asarray(a["r_med"], float) - np.asarray(b["r_med"], float)))), 4)
    return out


def cas_sain_qwen(ecarts: dict) -> list[str]:
    """Cas sain manqué (> 0,05) = chaîne en défaut ; jugé sur `logit` et `J` seulement (lentilles identiques à celles du résumé)."""
    return [k for k, v in ecarts.items() if not k.endswith("|hub") and (v is None or v > SEUIL_CAS_SAIN_QWEN)]


def etape_audit_tout_negatif(ctx: Contexte) -> dict:
    from controle_ia.scellement import sceller
    _, telecharger = ctx.hub_fonctions()
    for n, h in (QWEN_POIDS | QWEN_TOKENISEUR).items():
        if sha256(telecharger(QWEN, n, revision=QWEN_REV, token=False)) != h:
            raise Arret(f"Qwen3-8B {n} : empreinte inattendue")
    for n in ("config.json", "tokenizer_config.json", "model.safetensors.index.json", "generation_config.json", "vocab.json",
              "merges.txt"):
        telecharger(QWEN, n, revision=QWEN_REV, token=False)
    epingler(ctx.hf_home, QWEN, QWEN_REV)
    places = {"qwen3-8b/causal/causal.pt": ctx.voisin / "data" / "causal" / "qwen3-8b-causal.pt",
              "qwen3-8b/token_counts.pt": ctx.voisin / "data" / "token_counts-qwen3-8b.pt"}
    for n, h in CATALOGUE_FICHIERS.items():
        p = Path(telecharger(CATALOGUE[0], n, revision=CATALOGUE[1], repo_type="dataset", token=False))
        if sha256(p) != h:
            raise Arret(f"catalogue {n} : empreinte inattendue")
        places[n].parent.mkdir(parents=True, exist_ok=True)
        if not places[n].exists():
            shutil.copyfile(p, places[n])
    if sha256(telecharger(RS_LENSES[0], RS_LENSES[2], revision=RS_LENSES[1], token=False)) != RS_LENSES[3]:
        raise Arret("rs-lenses : empreinte inattendue")
    epingler(ctx.hf_home, RS_LENSES[0], RS_LENSES[1])
    j_qwen = sha256(telecharger(NP, QWEN_J, revision=p2.REVISION_NEURONPEDIA, token=False))
    s = ctx.executer([sys.executable, "scripts/checks/causal_lens.py", "score", "--lenses", "logit,J,hub", "--tag",
                      "audit-tout-negatif"], ctx.voisin, env_enfant(ctx.voisin, True, modele=QWEN), ctx.journal("audit-tout-negatif"),
                     2 * 3600)
    j = _resume(ctx, "audit-tout-negatif", "qwen3-8b")
    if s["code"] != 0 or not j.exists():
        raise Arret(f"score rejoué sur Qwen3-8B en échec (code {s['code']})")
    cible = ctx.diag / j.name
    if not cible.exists():
        shutil.copyfile(j, cible)
    rejoue = json.loads(cible.read_text(encoding="utf-8"))
    ec = ecarts_qwen(rejoue["targets"], json.loads((ctx.voisin / RESUME_QWEN[0]).read_text(encoding="utf-8")))
    manque = cas_sain_qwen(ec)
    return {"resume_rejoue": {"chemin": str(cible.relative_to(ctx.racine)), "sha256": sceller(cible)}, "j_qwen_sha256": j_qwen,
            "ecarts_max_r_med": ec, "cas_sain_manque": manque,
            "lecture": "chaîne en défaut" if manque else "cas sain de Qwen3-8B retrouvé (logit, J)"}


ETAPE_FONCTIONS = {"preparer": etape_preparer, "telecharger-tokeniseur": etape_telecharger_tokeniseur, "b0": etape_b0,
                   "telecharger-poids": etape_telecharger_poids, "corpus": etape_corpus, "partie2": etape_partie2,
                   "fumee": etape_fumee, "passe": etape_passe, "b3": etape_b3, "measure": etape_measure, "score": etape_score,
                   "grandeurs": etape_grandeurs, "verdicts": etape_verdicts, "audit-trop-beau": etape_audit_trop_beau,
                   "audit-tout-negatif": etape_audit_tout_negatif}
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
        if e is None:
            print("fin")
        else:
            print(f"{e} {'jeton' if e in JETON else 'sans-jeton'} {'en-ligne' if e in EN_LIGNE else 'hors-ligne'}")
        return
    if not a.etape:
        p.error("--etape exigé avec jouer")
    chemin = jouer(ctx, a.etape)
    print(json.dumps({"etape": a.etape, "resultat": str(chemin)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
