"""Lanceur local (orchestration de l'instance louée) — témoin « attaque publiée reproduite » (Bailey et collègues), v1.

Préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`) : règle du nombre de tours (B, R,
D, c), liste d'arrêt (dépense ≥ B − 2, échéance du GO : arrêt par identifiant d'instance, R10), pilote et reprise,
relance, transfert et comparaison des empreintes avant destruction, conditions de lancement 2 et 8. Point 2 de la liste
« ce qui manque à la condition 6 » de la contre-lecture du code (`151eee65…`).

Le fournisseur de cartes est abstrait (`Fournisseur`) : `FournisseurVast` passe par la commande `vastai` ; les essais
emploient un fournisseur factice. **Rien ne se lance sans** : une ligne de GO de calcul valide, citée (`GO_ID`), dont le
plafond égale B ; l'échéance du GO postérieure à la création + (B − 2)/c heures ; le commit de l'addendum de la
condition 6 ; `DEPOT_URL` égale au dépôt de travail. Ce module ne lit aucune note.
"""
from __future__ import annotations

import json
import re
import shlex
import subprocess
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path

from ..gardes import GardeArret
from . import conventions_v1 as cv

DEPOT_URL = "https://github.com/lciric/controle-ia-travail.git"
B_DEVIS = 75  # devis v4 (`f9c8c66e…`), décision de Lazar du 10 novembre (« go autonome Bailey »)


class Fournisseur:
    def creer(self, offre: str, image: str, disque_go: int) -> str: ...
    def taux_horaire(self, ident: str) -> float: ...
    def detruire(self, ident: str) -> None: ...
    def executer(self, ident: str, commande: str, delai_s: int | None = None) -> tuple[int, str]: ...
    def rapatrier(self, ident: str, distant: str, local: Path) -> None: ...


class FournisseurVast(Fournisseur):
    """Commande `vastai` (la clé est lue par la commande elle-même ; ce module ne la lit ni ne l'imprime)."""

    def _vast(self, *args: str) -> str:
        return subprocess.run(["vastai", *args], check=True, capture_output=True, text=True).stdout

    def creer(self, offre, image, disque_go):
        sortie = json.loads(self._vast("create", "instance", offre, "--image", image, "--disk", str(disque_go), "--raw"))
        return str(sortie["new_contract"])

    def taux_horaire(self, ident):
        return float(json.loads(self._vast("show", "instance", ident, "--raw"))["dph_total"])

    def detruire(self, ident):
        self._vast("destroy", "instance", ident)

    def _ssh(self, ident) -> tuple[str, str]:
        url = self._vast("ssh-url", ident).strip()  # ssh://root@hôte:port
        m = re.match(r"ssh://([^@]+)@([^:]+):(\d+)", url)
        if not m:
            raise GardeArret("adresse de l'instance illisible")
        return f"{m.group(1)}@{m.group(2)}", m.group(3)

    def executer(self, ident, commande, delai_s=None):
        hote, port = self._ssh(ident)
        p = subprocess.run(["ssh", "-o", "StrictHostKeyChecking=accept-new", "-p", port, hote, commande],
                           capture_output=True, text=True, timeout=delai_s)
        return p.returncode, p.stdout[-4000:]

    def rapatrier(self, ident, distant, local):
        hote, port = self._ssh(ident)
        local.mkdir(parents=True, exist_ok=True)
        subprocess.run(["scp", "-r", "-P", port, f"{hote}:{distant}", str(local)], check=True)


# --- conditions de lancement ------------------------------------------------------------------------------------------

def ligne_go(texte_go: str, go_id: str) -> dict:
    """Lit la ligne `| GO_ID | date | type | objet | plafond | échéance | … |` de `registres/go.md`."""
    for ligne in texte_go.splitlines():
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if cellules and cellules[0] == go_id:
            if len(cellules) < 6:
                raise GardeArret("condition 2 : ligne de GO incomplète")
            return {"id": go_id, "type": cellules[2], "objet": cellules[3], "plafond": cellules[4],
                    "echeance": cellules[5]}
    raise GardeArret("condition 2 : ligne de GO absente de registres/go.md")


def verifier_go(go: dict, b: float, empreinte_devis: str = "f9c8c66e") -> None:
    if go["type"].lower() != "calcul":
        raise GardeArret("condition 2 : la ligne de GO n'est pas de type « calcul »")
    if empreinte_devis not in go["objet"]:
        raise GardeArret("condition 2 : la ligne de GO ne cite pas le devis v4")
    nombres = re.findall(r"\d+(?:[.,]\d+)?", go["plafond"])
    if not nombres or float(nombres[0].replace(",", ".")) != float(b):
        raise GardeArret("condition 2 : plafond de la ligne de GO différent de B")


def echeance_epoch(echeance: str) -> float:
    """« AAAA-MM-JJ » : fin de journée UTC ; « AAAA-MM-JJTHH:MMZ » : l'instant dit."""
    import calendar
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})(?:[T ](\d{2}):(\d{2}))?", echeance)
    if not m:
        raise GardeArret("condition 2 : échéance du GO illisible")
    a, mo, j = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if m.group(4):
        return calendar.timegm((a, mo, j, int(m.group(4)), int(m.group(5)), 0))
    return calendar.timegm((a, mo, j, 23, 59, 59))


def verifier_echeance(echeance: float, creation: float, b: float, c: float) -> None:
    if echeance < creation + (float(b) - 2) / float(c) * 3600:
        raise GardeArret("condition 2 : échéance du GO antérieure à la création + (B − 2)/c heures")


# --- dépense du poste -------------------------------------------------------------------------------------------------

@dataclass
class Poste:
    """D : chaque instance comptée à son taux réel × heures de sa création à sa destruction (ou à maintenant)."""
    b: float
    instances: list[dict] = field(default_factory=list)

    def ajouter(self, ident: str, c: float, creation: float) -> None:
        self.instances.append({"id": ident, "c": c, "creation": creation, "destruction": None})

    def detruite(self, ident: str, quand: float) -> None:
        for i in self.instances:
            if i["id"] == ident and i["destruction"] is None:
                i["destruction"] = quand

    def depense(self, maintenant: float | None = None) -> float:
        maintenant = time.time() if maintenant is None else maintenant
        return sum(i["c"] * ((i["destruction"] or maintenant) - i["creation"]) / 3600 for i in self.instances)

    def d_avant(self, ident: str) -> float:
        """Dépense des autres instances, pour la garde embarquée (le lanceur côté instance ajoute la sienne)."""
        return sum(i["c"] * ((i["destruction"] or time.time()) - i["creation"]) / 3600
                   for i in self.instances if i["id"] != ident)


class Veilleur(threading.Thread):
    """Arrête l'instance par son identifiant (R10) quand D ≥ B − 2 ou à l'échéance du GO."""

    def __init__(self, fournisseur: Fournisseur, poste: Poste, ident: str, echeance: float, journal: Path,
                 periode_s: float = 30.0, horloge=time.time):
        super().__init__(daemon=True)
        self.f, self.poste, self.instance, self.echeance, self.journal = fournisseur, poste, ident, echeance, journal
        self.periode, self.horloge = periode_s, horloge
        self.arret = threading.Event()
        self.cause: str | None = None

    def verifier(self) -> str | None:
        maintenant = self.horloge()
        if self.poste.depense(maintenant) >= self.poste.b - 2:
            return "dépense"
        if maintenant >= self.echeance:
            return "échéance du GO"
        return None

    def run(self):
        while not self.arret.is_set():
            cause = self.verifier()
            if cause:
                self.cause = cause
                self.f.detruire(self.instance)
                self.poste.detruite(self.instance, self.horloge())
                with open(self.journal, "a", encoding="utf-8") as j:
                    j.write(json.dumps({"arret": cause, "instance": self.instance, "t": self.horloge()}) + "\n")
                return
            self.arret.wait(self.periode)


# --- amorce de l'instance ---------------------------------------------------------------------------------------------

def script_amorce(manifeste: dict, commit_travail: str) -> str:
    """Installe le dépôt de travail à son commit, le dépôt public à son commit (jamais copié dans le dépôt de travail),
    les versions du manifeste, le modèle et le juge à leurs révisions épinglées (hors ligne ensuite)."""
    v = manifeste["versions"]
    paquets = " ".join(shlex.quote(f"{p}=={x}") for p, x in sorted(v.items()) if p not in manifeste.get("git", {}))
    git = " ".join(shlex.quote(f"{p} @ git+{u}@{c}") for p, (u, c) in sorted(manifeste.get("git", {}).items()))
    return "\n".join([
        "set -euo pipefail",
        "cd /root",
        f"git clone {shlex.quote(DEPOT_URL)} travail && git -C travail checkout -q {shlex.quote(commit_travail)}",
        f"git init -q public && git -C public fetch -q --depth=1 {cv.DEPOT_PUBLIC} {cv.COMMIT_PUBLIC}"
        " && git -C public checkout -q FETCH_HEAD",
        "python -m venv /root/venv && . /root/venv/bin/activate",
        f"pip install -q {paquets}" + (f" {git}" if git else ""),
        "pip install -q --no-deps -e /root/public/" + cv.SOUS_DOSSIER,
        f"huggingface-cli download {cv.MODELE} --revision {shlex.quote(manifeste['revision_modele'])}"
        f" --local-dir {shlex.quote(manifeste['chemin_modele'])}",
        f"huggingface-cli download {cv.JUGE} --revision {shlex.quote(manifeste['juge']['revision'])}",
        "echo AMORCE_FINIE",
    ])


def commande_instance(sous_commande: str, **opts) -> str:
    morceaux = [". /root/venv/bin/activate && cd /root/travail && PYTHONPATH=src HF_HUB_OFFLINE=1",
                "python -m controle_ia.temoin_bailey.instance_v1", sous_commande]
    for k, v in opts.items():
        morceaux += [f"--{k.replace('_', '-')}", shlex.quote(str(v))]
    return " ".join(morceaux)


def ordre_de_lancement(go_id: str, b: float, c: float, commit_addendum: str) -> dict:
    """Condition 8 : l'ordre cite le GO, B, le taux relevé et DEPOT_URL."""
    return {"GO_ID": go_id, "B": b, "c": c, "DEPOT_URL": DEPOT_URL, "commit_code": commit_addendum,
            "heure": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


def transferer(fournisseur: Fournisseur, ident: str, distant: str, local: Path,
               empreintes_instance: dict) -> list[dict]:
    """Un transfert, puis au plus un nouveau si une empreinte diffère ; rend la liste des empreintes transférées."""
    essais = []
    for n in range(2):
        cible = local / f"transfert-{n + 1}"
        fournisseur.rapatrier(ident, distant, cible)
        base = cible / Path(distant).name
        obtenues = {rel: cv.sha_fichier(base / rel) for rel in empreintes_instance if (base / rel).is_file()}
        essais.append(obtenues)
        if obtenues == empreintes_instance:
            break
    return essais
