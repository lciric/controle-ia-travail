"""Entrées de T0.8 : liste blanche, lecteurs projetés, registres (plan d'analyse, points 1 et 5 (a) ; liste d'arrêt).

- `ListeBlanche` : chaque entrée a un nom, un chemin relatif à la racine, une empreinte attendue (ou `None` : le
  compagnon seul fait foi) et une phase (`course`, `lecture`, `hd`). Tout chemin hors de la liste est refusé ; un
  chemin qui porte un motif interdit (sondes, résumé de 7b, adaptateurs, activations, sorties des pièces R et L,
  bras d'attaque, P3-bis, étiqueteur…) est refusé même s'il est inscrit dans la liste ; les fichiers de la phase `hd`
  (pièce HD du texte de validité) ne s'ouvrent, contrôle d'empreinte compris, qu'après `ouvrir_phase("hd")`, que la
  lecture n'appelle qu'à l'étape (h bis), après l'écriture des tables D et F.
- Lecteurs projetés : chaque fichier lu ne rend que les clés que le texte nomme (`episodes-t06.json` : empreintes et
  effectifs ; manifeste de 7b : graines `partition-taches` et `tache/<identifiant>`, identifiant du run ;
  `lecture-cout-t06.json` : T6-10, T6-8 et la ligne de la table A ; `base-a-t08.json` : centres, modèles par (jeu,
  pli), lignes BA-L0 à BA-L4, réserves R-BA1 à R-BA7).
- Registres : format `| CLÉ | date UTC | chemin | empreinte |` ; seules les clés à la marque `T08`, plus
  `RUN-CONFIRMATION-T06` et `CODE-MOTS-ET-COUT-T06`, sont lues (les autres ignorées et comptées) ; du registre du texte
  de validité, la seule ligne `SORTIES-HD-VADAPT` (jamais une ligne VA) ; rien n'est jamais écrit dans un registre.
- `exiger_instance_sans_interdits` : l'amorce vérifie, avant tout calcul, qu'aucun `lecture-sondes-t06*` ni aucun
  `resume.json` n'est extrait sur l'instance, ni comme fichier ni comme objet git.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..manifeste import lire_manifeste
from ..scellement import verifier

PHASES = ("course", "lecture", "hd")
# motifs sur le nom du fichier
NOMS_INTERDITS_DEBUT = ("lecture-sondes", "distillation-t06", "adaptateur", "scores-relecture-vadapt",
                        "divergences-vadapt", "lecture-vadapt")
NOMS_INTERDITS_EXACTS = ("resume.json",)
NOMS_INTERDITS_CONTIENT = ("activations",)
SUFFIXES_INTERDITS = (".pt", ".safetensors")
# motifs sur le chemin entier
CHEMINS_INTERDITS = ("bras-attaque", "mode-tenu-a-l-ecart", "p3bis", "p3-bis", "etiqueteur", "lecture-b-7a",
                     "mesure-unanime", "t06-explo", "anteriorite-bras-informe", "textes-actions-p3", "lecture-p3",
                     "lecture-sondes")
MOTIFS_INTERDITS = NOMS_INTERDITS_DEBUT + NOMS_INTERDITS_EXACTS + NOMS_INTERDITS_CONTIENT + SUFFIXES_INTERDITS \
    + CHEMINS_INTERDITS
COLONNES_MESURES = ("cle", "episode", "condition", "tache", "phase", "pas", "jetons", "jetons_notes", "dose", "cout",
                    "valide", "cout_present", "cout_plusieurs_nombres", "cout_multiplication", "cout_intervalle",
                    "cout_suffixe_k", "cout_milliers_espace", "mention", "mention_etendue")
CLES_TEXTES = ("cle", "episode", "condition", "tache", "pas", "texte", "ids")


def motif_interdit(chemin: str) -> str | None:
    """Motif interdit porté par le chemin (nom du fichier ou chemin entier), ou `None`."""
    c = str(chemin).lower().replace("\\", "/")
    nom = c.rsplit("/", 1)[-1]
    for m in NOMS_INTERDITS_DEBUT:
        if nom.startswith(m):
            return m
    for m in NOMS_INTERDITS_EXACTS:
        if nom == m:
            return m
    for m in NOMS_INTERDITS_CONTIENT:
        if m in nom:
            return m
    for m in SUFFIXES_INTERDITS:
        if nom.endswith(m):
            return m
    return next((m for m in CHEMINS_INTERDITS if m in c), None)


class ListeBlanche:
    """Liste blanche des entrées d'une course ou d'une lecture de T0.8 (R5 : cas sain et artefacts éprouvés)."""

    def __init__(self, racine, entrees: dict[str, dict]):
        self.racine = Path(racine)
        self.entrees = {}
        self.ouvertes: list[str] = []
        self._phases = {"course", "lecture"}
        for nom, e in entrees.items():
            if set(e) - {"chemin", "sha256", "phase", "scelle"} or "chemin" not in e:
                raise GardeArret(f"entrée {nom!r} : clés chemin, sha256, phase, scelle attendues")
            if e.get("scelle", True) is False and e.get("sha256") is not None:
                raise GardeArret(f"entrée {nom!r} : un registre vivant (non scellé) n'a pas d'empreinte attendue")
            if e.get("phase", "lecture") not in PHASES:
                raise GardeArret(f"entrée {nom!r} : phase {e.get('phase')!r} inconnue")
            m = motif_interdit(e["chemin"])
            if m:
                raise GardeArret(f"entrée {nom!r} ({e['chemin']}) porte le motif interdit {m!r} : arrêt et nœud "
                                 "(embargo DT-4 ; interdits communs)")
            if Path(e["chemin"]).is_absolute() or ".." in Path(e["chemin"]).parts:
                raise GardeArret(f"entrée {nom!r} : chemin relatif à la racine, sans « .. », attendu")
            self.entrees[nom] = {"chemin": e["chemin"], "sha256": e.get("sha256"), "phase": e.get("phase", "lecture"),
                                 "scelle": bool(e.get("scelle", True))}

    def ouvrir_phase(self, phase: str) -> None:
        if phase not in PHASES:
            raise GardeArret(f"phase {phase!r} inconnue")
        self._phases.add(phase)

    def phase_ouverte(self, phase: str) -> bool:
        return phase in self._phases

    def chemin(self, nom: str) -> Path:
        """Chemin d'une entrée de la liste, empreinte vérifiée contre son compagnon et contre l'empreinte attendue."""
        if nom not in self.entrees:
            raise GardeArret(f"entrée {nom!r} hors de la liste blanche : arrêt et nœud")
        e = self.entrees[nom]
        if e["phase"] not in self._phases:
            raise GardeArret(f"entrée {nom!r} de la phase {e['phase']!r} ouverte avant son étape : refusée")
        p = self.racine / e["chemin"]
        if not e["scelle"]:            # registre vivant (versionné par git, sans compagnon) : présence seulement
            if not p.is_file():
                raise GardeArret(f"{e['chemin']} : registre absent sur disque")
            self.ouvertes.append(e["chemin"])
            return p
        sha = verifier(p)
        if e["sha256"] is not None and sha != e["sha256"]:
            raise GardeArret(f"{e['chemin']} : empreinte {sha[:12]}… ≠ empreinte consignée {e['sha256'][:12]}… (R11)")
        self.ouvertes.append(e["chemin"])
        return p

    def refuser_hors_liste(self, chemin) -> None:
        """Toute ouverture d'un chemin qui n'est pas une entrée de la liste est refusée (garde appelée par les lecteurs)."""
        rel = str(Path(chemin))
        if not any(rel == e["chemin"] or rel == str(self.racine / e["chemin"]) for e in self.entrees.values()):
            m = motif_interdit(rel)
            raise GardeArret(f"ouverture tentée de {rel} hors de la liste blanche"
                             + (f" (motif interdit {m!r})" if m else "") + " : arrêt et nœud")

    def lire_json(self, nom: str):
        return json.loads(self.chemin(nom).read_text(encoding="utf-8"))

    def lire_jsonl(self, nom: str) -> list[dict]:
        with open(self.chemin(nom), encoding="utf-8") as f:
            return [json.loads(l) for l in f if l.strip()]

    def lire_npz(self, nom: str, colonnes=COLONNES_MESURES) -> dict[str, np.ndarray]:
        with np.load(self.chemin(nom), allow_pickle=False) as z:
            cles = tuple(sorted(z.files))
            if cles != tuple(sorted(colonnes)):
                raise GardeArret(f"{nom} : colonnes {cles} ≠ colonnes attendues {tuple(sorted(colonnes))}")
            return {k: np.array(z[k]) for k in colonnes}


# --- projections : seules les clés que le texte nomme --------------------------------------------------------------

def projeter_episodes_t06(corps: dict) -> dict:
    r = corps["resultat"] if "resultat" in corps else corps
    manquantes = [k for k in ("mesures_sha256", "textes_sha256", "effectifs") if k not in r]
    if manquantes:
        raise GardeArret(f"episodes-t06.json : clés {manquantes} absentes")
    return {k: r[k] for k in ("mesures_sha256", "textes_sha256", "effectifs")}


def projeter_manifeste_7b(m: dict, taches: list[str]) -> dict:
    g = m.get("graines", {})
    cles = ["partition-taches"] + [f"tache/{t}" for t in taches]
    absentes = [k for k in cles if k not in g]
    if absentes:
        raise GardeArret(f"manifeste de 7b : graines {absentes[:3]} absentes")
    return {"run_id": m["run_id"], "graines": {k: g[k] for k in cles}}


def lire_manifeste_7b(lb: ListeBlanche, nom: str, taches: list[str]) -> dict:
    chemin = lb.chemin(nom)
    m, sha = lire_manifeste(chemin)
    return {**projeter_manifeste_7b(m, taches), "sha256": sha}


def projeter_lecture_cout(corps: dict) -> dict:
    lec = corps["resultat"]["lecture"]
    for k in ("T6-10", "T6-8", "table_A"):
        if k not in lec:
            raise GardeArret(f"lecture-cout-t06.json : clé {k} absente")
    return {"T6-10": lec["T6-10"], "T6-8": lec["T6-8"], "ligne_A": lec["table_A"]["ligne"],
            "run_id": corps.get("run_id"), "manifeste_sha256": corps.get("manifeste_sha256")}


CLES_MODELE_BASE_A = ("calculable", "motif", "traits_retires", "convergence", "coefficients", "ordonnee", "moyennes",
                      "ecarts")
LIGNES_BA = ("BA-L0", "BA-L1", "BA-L2", "BA-L3", "BA-L3b", "BA-L4")
RESERVES_BA = ("R-BA1", "R-BA2", "R-BA2b", "R-BA3", "R-BA4", "R-BA5", "R-BA6", "R-BA7")


def projeter_base_a(obj: dict) -> dict:
    """`base-a-t08.json` (objet à la racine) : centres, modèles par (jeu, pli), lignes BA-L, réserves R-BA ; rien d'autre."""
    for k in ("centres", "modeles", "lignes", "reserves", "run_id", "manifeste_sha256"):
        if k not in obj:
            raise GardeArret(f"base-a-t08.json : clé {k} absente")
    modeles = {}
    for jeu, plis in obj["modeles"].items():
        modeles[jeu] = {}
        for pli, m in plis.items():
            manquantes = [k for k in CLES_MODELE_BASE_A if k not in m]
            if manquantes:
                raise GardeArret(f"base-a-t08.json : modèle ({jeu}, pli {pli}) sans {manquantes}")
            modeles[jeu][str(pli)] = {k: m[k] for k in CLES_MODELE_BASE_A}
    lignes = {k: obj["lignes"][k] for k in LIGNES_BA if k in obj["lignes"]}
    if set(lignes) != set(LIGNES_BA):
        raise GardeArret(f"base-a-t08.json : lignes BA {sorted(set(LIGNES_BA) - set(lignes))} absentes")
    reserves = [r for r in obj["reserves"] if r.get("code") in RESERVES_BA]
    return {"centres": dict(obj["centres"]), "modeles": modeles, "lignes": lignes, "reserves": reserves,
            "run_id": obj["run_id"], "manifeste_sha256": obj["manifeste_sha256"]}


# --- registres (format du registre partagé) ------------------------------------------------------------------------

_LIGNE = re.compile(r"^\|\s*([A-Za-z0-9-]+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([0-9a-f]{64})\s*\|\s*$")
_MARQUE_T08 = re.compile(r"(^|-)T08(-|$)")
CLES_LUES_HORS_T08 = ("RUN-CONFIRMATION-T06", "CODE-MOTS-ET-COUT-T06")


def date_utc(texte: str) -> datetime:
    t = str(texte).strip()
    try:
        d = datetime.fromisoformat(t.replace("Z", "+00:00"))
    except ValueError:
        raise GardeArret(f"date {t!r} illisible (ISO 8601 UTC attendu)") from None
    if d.tzinfo is None:
        raise GardeArret(f"date {t!r} sans fuseau : UTC attendu")
    return d.astimezone(timezone.utc)


def _lignes_registre(chemin: Path) -> list[tuple]:
    sortie = []
    for l in Path(chemin).read_text(encoding="utf-8").splitlines():
        m = _LIGNE.match(l.strip())
        if m and m.group(1) not in ("CLÉ", "CLE"):
            sortie.append(m.groups())
    return sortie


def lire_registre_scellements(chemin) -> dict:
    """Clés à la marque `T08` et `RUN-CONFIRMATION-T06`, `CODE-MOTS-ET-COUT-T06` ; les autres ignorées et comptées.
    Une clé lue deux fois arrête (une clé, une ligne)."""
    lues, ignorees = {}, 0
    for cle, date, ch, sha in _lignes_registre(chemin):
        if not (_MARQUE_T08.search(cle) or cle in CLES_LUES_HORS_T08):
            ignorees += 1
            continue
        if cle in lues:
            raise GardeArret(f"registre : clé {cle} inscrite deux fois")
        lues[cle] = {"date": date_utc(date).isoformat(), "chemin": ch, "sha256": sha}
    return {"lignes": lues, "ignorees": ignorees}


def lire_ligne_sorties_hd(chemin) -> dict | None:
    """Seule la ligne `SORTIES-HD-VADAPT` du registre propre du texte de validité ; jamais une ligne VA ; rien n'est
    écrit. `None` si la ligne n'est pas inscrite."""
    trouvee, ignorees = None, 0
    for cle, date, ch, sha in _lignes_registre(chemin):
        if cle != "SORTIES-HD-VADAPT":
            ignorees += 1
            continue
        if trouvee is not None:
            raise GardeArret("registre du texte de validité : SORTIES-HD-VADAPT inscrite deux fois")
        trouvee = {"date": date_utc(date).isoformat(), "chemin": ch, "sha256": sha, "ignorees": None}
    if trouvee is not None:
        trouvee["ignorees"] = ignorees
    return trouvee


def exiger_ligne(registre: dict, cle: str) -> dict:
    if cle not in registre["lignes"]:
        raise GardeArret(f"ligne {cle} absente du registre : entrée manquante")
    return registre["lignes"][cle]


# --- amorce de l'instance ------------------------------------------------------------------------------------------

def _nom_interdit_instance(nom: str) -> bool:
    base = nom.rsplit("/", 1)[-1]
    return base.startswith("lecture-sondes-t06") or base == "resume.json"


def exiger_instance_sans_interdits(racine) -> dict:
    """Avant tout calcul sur l'instance : aucun `lecture-sondes-t06*` ni `resume.json` extrait, ni comme fichier, ni
    comme objet git de la copie clonée. Ne lit le contenu d'aucun fichier."""
    racine = Path(racine)
    fichiers = 0
    for dossier, sous, noms in os.walk(racine):
        sous[:] = [s for s in sous if s != ".git"]
        for n in noms:
            fichiers += 1
            if _nom_interdit_instance(n):
                raise GardeArret(f"{Path(dossier, n).relative_to(racine)} présent sur l'instance : arrêt et nœud (DT-4)")
    objets = None
    if (racine / ".git").exists():
        r = subprocess.run(["git", "-C", str(racine), "rev-list", "--all", "--objects"], capture_output=True, text=True)
        if r.returncode != 0:
            raise GardeArret(f"objets git illisibles : {r.stderr.strip()}")
        objets = 0
        for l in r.stdout.splitlines():
            parts = l.split(" ", 1)
            objets += 1
            if len(parts) == 2 and _nom_interdit_instance(parts[1]):
                raise GardeArret(f"objet git {parts[1]} présent dans la copie de l'instance : arrêt et nœud (DT-4)")
    return {"fichiers": fichiers, "objets_git": objets, "interdits": 0}
