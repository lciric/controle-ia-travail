"""Aide des essais de la chaîne de l'instance de B bis (corrections B1, B2, M1, M3, m5, m7 de la contre-lecture du code par le
modèle C, `brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-code-modele-c-v1.md`) : dépôts git **jetables** (jamais le dépôt
de travail), extraits de `scripts/amorce_bbis_v1.sh` lus entre leurs marques `# >>> nom` / `# <<< nom` et joués par bash, motifs
d'extraction partielle lus dans l'amorce. Aucune donnée de 7a, 7b, T0.7 ni de P3-bis : tout est jouet."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

RACINE_DEPOT = Path(__file__).resolve().parents[1]
AMORCE = RACINE_DEPOT / "scripts" / "amorce_bbis_v1.sh"
LANCER = RACINE_DEPOT / "scripts" / "lancer_bbis_v1.sh"
E = 2 ** 127 + 4242
RUN_7B = "20261111-151701-t06-reel"


def git(d: Path, *args) -> str:
    r = subprocess.run(["git", "-C", str(d), *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} : {r.stderr.strip()}")
    return r.stdout.strip()


def depot_vide(d: Path) -> Path:
    d.mkdir(parents=True, exist_ok=True)
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "essai@example.invalid")
    git(d, "config", "user.name", "essai")
    return d


def committer(d: Path, message: str, *chemins) -> str:
    git(d, "add", "-f", "--", *(chemins or (".",)))
    git(d, "commit", "-q", "--allow-empty", "-m", message)
    return git(d, "rev-parse", "HEAD")


def ecrire(d: Path, rel: str, texte: str = "x\n") -> Path:
    p = d / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
    return p


def extrait(nom: str) -> str:
    """Texte de l'amorce entre `# >>> nom` et `# <<< nom` (une fois exactement)."""
    t = AMORCE.read_text(encoding="utf-8")
    m = re.findall(rf"^# >>> {re.escape(nom)}\b[^\n]*\n(.*?)^# <<< {re.escape(nom)}$", t, re.S | re.M)
    if len(m) != 1:
        raise AssertionError(f"extrait {nom!r} : {len(m)} occurrence(s) dans l'amorce, une attendue")
    return m[0]


def motifs() -> list[str]:
    """Motifs d'extraction partielle de l'amorce (`MOTIFS='…'`, une fois exactement)."""
    m = re.findall(r"^MOTIFS='(.*?)'$", AMORCE.read_text(encoding="utf-8"), re.S | re.M)
    if len(m) != 1:
        raise AssertionError(f"MOTIFS : {len(m)} occurrence(s) dans l'amorce, une attendue")
    return m[0].split("\n")


def appliquer_motifs(d: Path, lignes: list[str]) -> None:
    """Extraction partielle de l'amorce (`sparse-checkout init --no-cone` puis `set --no-cone --stdin`) sur un dépôt jetable."""
    git(d, "sparse-checkout", "init", "--no-cone")
    r = subprocess.run(["git", "-C", str(d), "sparse-checkout", "set", "--no-cone", "--stdin"], input="\n".join(lignes) + "\n",
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"sparse-checkout set : {r.stderr.strip()}")


def jouer(corps: str, *args, cwd: Path | None = None) -> subprocess.CompletedProcess:
    """Joue un extrait de l'amorce sous bash avec des `arret` et `j` d'essai (motif imprimé, code de sortie gardé)."""
    script = ("set -uo pipefail\n"
              "arret() { echo \"ARRET : $1\"; exit \"${2:-4}\"; }\n"
              "j() { echo \"J $*\"; }\n" + corps)
    return subprocess.run(["bash", "-c", script, "essai", *map(str, args)], capture_output=True, text=True, cwd=cwd)


def epreuve(d: Path, entropie: int = E) -> str:
    """Épreuve de niveau jouet, complète, scellée (forme de `epreuve_niveau_deux_plis_bbis_v1.py`)."""
    from controle_ia.manifeste import cle_de_tache
    from controle_ia.scellement import sceller
    doc = {"cellules": {"nul": {"taux": 0.004}, "signal-commun": {"taux": 0.003}}, "seuil_taux": 0.01,
           "niveau_decisif_retenu": 0.99,
           "graine": {"cle": "bbis/epreuve-niveau", "spawn_key": [str(cle_de_tache("bbis/epreuve-niveau"))],
                      "entropie": str(entropie)}, "complete": True, "cout": {"secondes_murales": 1.0}}
    rel = "registres/t07-etape-b-bis/epreuve-niveau-jouet.json"
    p = ecrire(d, rel, json.dumps(doc))
    sceller(p)
    return rel


def depot_code(d: Path, cite: str = "ancetre") -> dict:
    """Dépôt jetable de la garde B1 : B (base) ; C0 porte le « code » (`src/x.py`) et le texte scellé de B bis ; la fiche de
    `CODE-BBIS` (`registre_bbis_v1.ecrire_fiche_code`) cite C0 (`cite="ancetre"`), V, commit d'une branche voisine issue de B
    (`"voisine"`), ou un commit absent (`"absent"`) ; C1 ajoute l'épreuve de niveau, la fiche, l'extrait de GO et les lignes
    SCELLEMENT-BBIS, CODE-BBIS, GO-BBIS du registre propre. La tête est C1 (branche main). Rend {d, b, c0, c1, v, fiche}."""
    from controle_ia.scellement import empreinte, sceller
    from controle_ia.t07bbis import commun_v1 as cm
    from controle_ia.t07bbis import registre_bbis_v1 as rb
    depot_vide(d)
    ecrire(d, "README", "base\n")
    b = committer(d, "base")
    git(d, "checkout", "-q", "-b", "voisine")
    ecrire(d, "voisin.txt", "branche voisine\n")
    v = committer(d, "voisine")
    git(d, "checkout", "-q", "main")
    ecrire(d, "src/x.py", "print('code de B bis, jouet')\n")
    (d / "prereg").mkdir()
    for nom in ("T0.7-etape-B-bis-v1.md", "T0.7-etape-B-bis-v1.md.sha256"):
        shutil.copy(RACINE_DEPOT / "prereg" / nom, d / "prereg" / nom)
    c0 = committer(d, "code")
    commit_fiche = {"ancetre": c0, "voisine": v, "absent": "d" * 40}[cite]
    ep = epreuve(d)
    fiche = rb.ecrire_fiche_code(d, "registres/t07-etape-b-bis/code-bbis-v1.json", commit_fiche,
                                 {"src/x.py": empreinte(d / "src" / "x.py")}, E, ep)
    g = ecrire(d, "registres/go-extraits/GO-BBIS-v1.md", "| GO-2026-11-14-09 | extrait jouet |\n")
    for k, t, chemin, sha in (("SCELLEMENT-BBIS", 1789000000, cm.TEXTE, cm.TEXTE_SHA256),
                              ("CODE-BBIS", 1789000100, "registres/t07-etape-b-bis/code-bbis-v1.json", fiche["sha256"]),
                              ("GO-BBIS", 1789000200, "registres/go-extraits/GO-BBIS-v1.md", sceller(g))):
        rb.ajouter_ligne_propre(d, rb.REGISTRE_PROPRE, k, t, chemin, sha)
    c1 = committer(d, "lignes du registre propre")
    return {"d": d, "b": b, "c0": c0, "c1": c1, "v": v, "fiche": fiche}
