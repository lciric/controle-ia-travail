"""Aide des essais de l'étape B bis (`t07bbis`) : une vraie course jouet de la chaîne de T0.6 (`t06.lanceur_v6`, modèle jouet par
caractères, aucun téléchargement) dans un dépôt jetable, préparée comme `tests/test_t07_repli_recalcul_v1.py` ; les activations de
l'instance sont retirées (disque perdu), et `lecture-sondes-t06.json` et `resume.json` sont retirés aussi (l'instance de B bis ne
les descend jamais). Aucune donnée de 7a, 7b, T0.7 ni de P3-bis n'est lue : tout est jouet."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

RACINE_DEPOT = Path(__file__).resolve().parents[1]
CONFIG_JOUET = RACINE_DEPOT / "docs" / "notes" / "g0-deux-semaines-v1" / "config-t06-jouet-v5.json"
RUN = "20261110-070000-t06-jouet"
ENONCES = ["Which routing rule makes sparse mixtures of experts train stably?",
           "Does curriculum ordering change sample efficiency of small language models?",
           "Can retrieval reduce hallucination in long-form question answering?",
           "How does tokenizer vocabulary size affect multilingual transfer?",
           "Do sparse autoencoders recover known features in toy models?",
           "Is chain-of-thought faithful under distribution shift?"]


def git(d: Path, *args, date: str | None = None):
    import os
    env = dict(os.environ)
    if date:
        env.update({"GIT_COMMITTER_DATE": date, "GIT_AUTHOR_DATE": date})
    subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True, env=env)


def disponible() -> bool:
    return CONFIG_JOUET.is_file() and (RACINE_DEPOT / "src" / "controle_ia" / "t06" / "lanceur_v6.py").is_file()


def course_jouet(d: Path) -> Path:
    """Dépôt jetable `d` (créé), course jouet de T0.6 jouée ; rend `d`."""
    from controle_ia.scellement import sceller
    from controle_ia.t06 import lanceur_v6 as la6
    d.mkdir(parents=True, exist_ok=True)
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "essai@example.invalid")
    git(d, "config", "user.name", "essai")
    (d / "prereg").mkdir()
    for nom in ("P3-consignes-v1.md", "P3-consignes-v1.md.sha256", "T0.7-etape-B-bis-v1.md", "T0.7-etape-B-bis-v1.md.sha256"):
        shutil.copy(RACINE_DEPOT / "prereg" / nom, d / "prereg" / nom)
    t = d / "donnees" / "t06-jouet"
    t.mkdir(parents=True)
    taches = lambda ids: {"taches": [{"identifiant": i, "questions": ENONCES[k % len(ENONCES)] + f" ({i})"}
                                     for k, i in enumerate(ids)]}
    (t / "taches-evaluation.json").write_text(json.dumps(taches([f"e{k}" for k in range(1, 7)])), encoding="utf-8")
    (t / "taches-distillation.json").write_text(json.dumps(taches(["d1", "d2"])), encoding="utf-8")
    config = json.loads(CONFIG_JOUET.read_text(encoding="utf-8"))
    config["taches_evaluation"]["sha256"] = sceller(t / "taches-evaluation.json")
    config["taches_distillation"]["sha256"] = sceller(t / "taches-distillation.json")
    config["egalite_jetons_reels"] = False
    for x in ("runs", "diag"):
        (d / x).mkdir()
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "jouet")
    la6.executer(config, d, RUN, None)
    shutil.rmtree(d / "donnees" / RUN / "activations")
    for f in ("lecture-sondes-t06.json", "lecture-sondes-t06.json.sha256", "resume.json", "resume.json.sha256"):
        if (d / "diag" / RUN / f).exists():
            (d / "diag" / RUN / f).unlink()
    return d


def sceller_json(d: Path, rel: str, contenu) -> str:
    from controle_ia.scellement import sceller
    p = d / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(contenu, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return sceller(p)
