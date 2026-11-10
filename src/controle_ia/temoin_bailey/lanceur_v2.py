"""Lanceur local (orchestration de l'instance louée) — témoin « attaque publiée reproduite » (Bailey et collègues), v2.

Préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`) : règle du nombre de tours (B, R,
D, c), liste d'arrêt, pilote et reprise, relance, transfert et comparaison des empreintes avant destruction, conditions
de lancement 2 et 8. La v2 applique la contre-lecture du code de la condition 6 (`contre-lecture-code-condition6-bailey-v1.md`,
`90af7dea…`) :
- B-5 : à B − 2 ou à l'échéance du GO, le run est arrêté **sur l'instance** (par PID, `instance_v2.executer`), ses
  journaux sont empreintés, transférés et comparés, puis l'instance est détruite par son identifiant (R10). Le veilleur
  local ne détruit d'office, sans transfert, qu'à un second seuil `B − marge_secours` (défaut 0,5 USD) ou à l'échéance
  plus `delai_secours` : garde de secours si le transfert ne finit pas. **Ce second seuil est à confirmer par Lazar.**
- B-6 : transfert fichier par fichier de la seule liste `conventions_v2.NOMS_JOURNAUX` (et des fichiers d'état de la
  mise en place, du contrôle du juge et de la règle) ; rien d'autre ne sort.
- A-7 : `ecrire_manifeste` ; A-8 : `conduire` (mise en place, contrôle du juge, pilote et sa reprise, règle, run
  principal et sa relance, empreintes, transfert, destruction) ; A-9 : seule la ligne `ETAT` des commandes distantes
  revient ; P-7 : la création d'instance exige `GO_ID` et relit la ligne de GO, la garde `garde_calcul.py` ne voyant
  pas un appel fait depuis Python ; B-4 : modèle, adaptateur du juge et sa base téléchargés à leurs révisions, `refs/main`
  posé sur chacune.
Ce module ne lit aucune note.
"""
from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path

from ..gardes import GardeArret
from . import analyse_v3 as an
from . import conventions_v2 as cv

DEPOT_URL = "https://github.com/lciric/controle-ia-travail.git"
CACHE_HF = "/root/hf"
FICHIERS_ETAT = ("mise-en-place-v2.json", "controle-juge-v2.json", "regle-tours-v2.json", "empreintes-instance-v2.json")


class Fournisseur:
    def creer(self, offre: str, image: str, disque_go: int, env: dict) -> str: ...
    def taux_horaire(self, ident: str) -> float: ...
    def detruire(self, ident: str) -> None: ...
    def executer(self, ident: str, commande: str, delai_s: int | None = None) -> tuple[int, str]: ...
    def rapatrier_fichier(self, ident: str, distant: str, local: Path) -> None: ...


class FournisseurVast(Fournisseur):
    """Commande `vastai` (la clé est lue par la commande ; ce module ne la lit ni ne l'imprime)."""

    def _vast(self, *args: str) -> str:
        return subprocess.run(["vastai", *args], check=True, capture_output=True, text=True).stdout

    def creer(self, offre, image, disque_go, env):
        opts = " ".join(f"-e {k}={shlex.quote(v)}" for k, v in env.items())
        args = ["create", "instance", offre, "--image", image, "--disk", str(disque_go), "--ssh", "--direct", "--raw"]
        if opts:
            args += ["--env", opts]
        return str(json.loads(self._vast(*args))["new_contract"])

    def taux_horaire(self, ident):
        return float(json.loads(self._vast("show", "instance", ident, "--raw"))["dph_total"])

    def detruire(self, ident):
        self._vast("destroy", "instance", ident)

    def _ssh(self, ident) -> tuple[str, str]:
        m = re.match(r"ssh://([^@]+)@([^:]+):(\d+)", self._vast("ssh-url", ident).strip())
        if not m:
            raise GardeArret("adresse de l'instance illisible")
        return f"{m.group(1)}@{m.group(2)}", m.group(3)

    def executer(self, ident, commande, delai_s=None):
        hote, port = self._ssh(ident)
        p = subprocess.run(["ssh", "-o", "StrictHostKeyChecking=accept-new", "-p", port, hote, commande],
                           capture_output=True, text=True, timeout=delai_s)
        return p.returncode, p.stdout

    def rapatrier_fichier(self, ident, distant, local):
        hote, port = self._ssh(ident)
        local.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["scp", "-P", port, f"{hote}:{distant}", str(local)], check=True, capture_output=True)


# --- conditions de lancement ------------------------------------------------------------------------------------------

def ligne_go(texte_go: str, go_id: str) -> dict:
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
    """« AAAA-MM-JJ » : lue comme la fin de ce jour, 23:59:59 UTC (lecture déclarée, P-3) ; « AAAA-MM-JJTHH:MMZ » :
    l'instant dit."""
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


# --- manifeste (A-7) --------------------------------------------------------------------------------------------------

def chemin_snapshot(depot: str, revision: str) -> str:
    return f"{CACHE_HF}/models--{depot.replace('/', '--')}/snapshots/{revision}"


def ecrire_manifeste(chemin: Path, *, versions: dict, git: dict, revision_modele: str, revision_adaptateur: str,
                     revision_base: str, commit_code: str, b: float, go_id: str) -> dict:
    """Manifeste (R9) fixé avant la création de l'instance : versions, commits des paquets git, révisions, graines,
    juge attendu, commit du code. La mise en place y ajoute la longueur du suffixe, la configuration de génération et
    les pas par tour ; la règle y ajoute B, R, D, c, t, H, K."""
    g = an.graines()
    m = {"version": 2, "commit_code": commit_code, "commit_public": cv.COMMIT_PUBLIC, "arbre_public": cv.ARBRE_PUBLIC,
         "go_id": go_id, "B": b, "versions": versions, "git": git, "cache_hf": CACHE_HF,
         "modele": cv.MODELE, "revision_modele": revision_modele,
         "chemin_modele": chemin_snapshot(cv.MODELE, revision_modele),
         "juge": {"adaptateur": cv.JUGE, "revision_adaptateur": revision_adaptateur, "base": cv.JUGE_BASE,
                  "revision_base": revision_base, "dtype": "torch.bfloat16"},
         "graines": {"racine": an.RACINE_GRAINES, "pilote": g["pilote"], "principal": g["principal"],
                     "cle_reechantillonnage": list(an.CLE_REECHANTILLONNAGE)}}
    an.garde_graines(m["graines"])
    chemin.write_text(json.dumps(m, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return m


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

    def d_avant(self, ident: str, maintenant: float | None = None) -> float:
        maintenant = time.time() if maintenant is None else maintenant
        return sum(i["c"] * ((i["destruction"] or maintenant) - i["creation"]) / 3600
                   for i in self.instances if i["id"] != ident)


class Veilleur(threading.Thread):
    """Secours (B-5) : détruit l'instance par son identifiant (R10), sans transfert, à `B − marge_secours` ou à
    l'échéance + `delai_secours`. L'arrêt nominal à B − 2 se fait sur l'instance, puis transfert, puis destruction."""

    def __init__(self, fournisseur: Fournisseur, poste: Poste, instance: str, echeance: float, journal: Path,
                 marge_secours: float = 0.5, delai_secours_s: float = 1800, periode_s: float = 30.0,
                 horloge=time.time):
        super().__init__(daemon=True)
        self.f, self.poste, self.instance, self.echeance, self.journal = fournisseur, poste, instance, echeance, journal
        self.marge, self.delai, self.periode, self.horloge = marge_secours, delai_secours_s, periode_s, horloge
        self.arret = threading.Event()
        self.cause: str | None = None

    def verifier(self) -> str | None:
        maintenant = self.horloge()
        if self.poste.depense(maintenant) >= self.poste.b - self.marge:
            return "dépense (seuil de secours)"
        if maintenant >= self.echeance + self.delai:
            return "échéance du GO (délai de secours)"
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


# --- amorce et commandes distantes ------------------------------------------------------------------------------------

def script_amorce(manifeste: dict) -> str:
    """Dépôt de travail à son commit ; dépôt public à son commit (jamais copié dans le dépôt de travail) ; versions et
    commits du manifeste ; modèle, adaptateur du juge et base à leurs révisions, `refs/main` posé sur chacune (B-4).
    Le jeton d'accès aux modèles à accès contrôlé vient de l'environnement de l'instance (condition 8)."""
    v = manifeste["versions"]
    paquets = " ".join(shlex.quote(f"{p}=={x}") for p, x in sorted(v.items()) if p not in manifeste.get("git", {}))
    git = " ".join(shlex.quote(f"{p} @ git+{u}@{c}") for p, (u, c) in sorted(manifeste.get("git", {}).items()))
    lignes = ["set -euo pipefail", "cd /root",
              f"git clone -q {shlex.quote(DEPOT_URL)} travail && git -C travail checkout -q {shlex.quote(manifeste['commit_code'])}",
              f"git init -q public && git -C public fetch -q --depth=1 {cv.DEPOT_PUBLIC} {cv.COMMIT_PUBLIC}"
              " && git -C public checkout -q FETCH_HEAD",
              "python -m venv /root/venv && . /root/venv/bin/activate",
              f"pip install -q {paquets}" + (f" {git}" if git else ""),
              f"pip install -q --no-deps -e /root/public/{cv.SOUS_DOSSIER}",
              f"export HF_HUB_CACHE={CACHE_HF}"]
    for depot, rev in ((cv.MODELE, manifeste["revision_modele"]),
                       (cv.JUGE, manifeste["juge"]["revision_adaptateur"]),
                       (cv.JUGE_BASE, manifeste["juge"]["revision_base"])):
        refs = f"{CACHE_HF}/models--{depot.replace('/', '--')}/refs"
        lignes += [f"huggingface-cli download {depot} --revision {shlex.quote(rev)} --quiet > /dev/null",
                   f"mkdir -p {refs} && printf %s {shlex.quote(rev)} > {refs}/main"]
    lignes.append("echo ETAT '{\"commande\": \"amorce\", \"finie\": true}'")
    return "\n".join(lignes)


def commande_instance(sous_commande: str, **opts) -> str:
    morceaux = [f". /root/venv/bin/activate && cd /root/travail && PYTHONPATH=src HF_HUB_OFFLINE=1 HF_HUB_CACHE={CACHE_HF}",
                "python -m controle_ia.temoin_bailey.instance_v2", sous_commande]
    for k, v in opts.items():
        morceaux += [f"--{k.replace('_', '-')}", shlex.quote(str(v))]
    return " ".join(morceaux)


def lire_etat(sortie: str) -> dict:
    """Seule la ligne `ETAT {…}` revient au poste local (A-9) ; le reste de la sortie est ignoré."""
    for ligne in reversed(sortie.splitlines()):
        if ligne.startswith("ETAT "):
            return json.loads(ligne[5:])
    raise GardeArret("commande distante sans ligne d'état")


def transferer(fournisseur: Fournisseur, ident: str, distant: str, local: Path, empreintes_instance: dict) -> list[dict]:
    """Fichier par fichier, la seule liste des journaux (B-6) ; un transfert, puis au plus un nouveau si une empreinte
    diffère. Rend la liste des empreintes transférées (pour `garde_fin_de_run`)."""
    if not set(empreintes_instance) <= set(cv.NOMS_JOURNAUX):
        raise GardeArret("transfert : fichier hors de la liste des journaux")
    essais = []
    for n in range(2):
        cible = local / f"transfert-{n + 1}"
        for rel in empreintes_instance:
            fournisseur.rapatrier_fichier(ident, f"{distant}/{rel}", cible / rel)
        obtenues = {rel: cv.sha_fichier(cible / rel) for rel in empreintes_instance if (cible / rel).is_file()}
        essais.append(obtenues)
        if obtenues == empreintes_instance:
            break
    return essais


def ordre_de_lancement(go_id: str, b: float, c: float, commit_code: str) -> dict:
    """Condition 8 : l'ordre cite le GO, B, le taux relevé et DEPOT_URL."""
    return {"GO_ID": go_id, "B": b, "c": c, "DEPOT_URL": DEPOT_URL, "commit_code": commit_code,
            "heure": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


# --- conduite (A-8) ---------------------------------------------------------------------------------------------------

@dataclass
class Conduite:
    """Déroulé complet d'un poste sur une instance. `journal` : fichier local des étapes (états seulement)."""
    fournisseur: Fournisseur
    manifeste_local: Path
    sortie: Path
    go_id: str
    texte_go: str
    offre: str
    image: str
    disque_go: int = 200
    env_instance: dict = field(default_factory=dict)
    horloge: object = time.time
    delai_commande_s: int = 4 * 24 * 3600

    def _etape(self, objet: dict) -> None:
        self.sortie.mkdir(parents=True, exist_ok=True)
        with open(self.sortie / "conduite-v2.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({**objet, "t": self.horloge()}, ensure_ascii=False, sort_keys=True) + "\n")

    def _cmd(self, ident: str, commande: str) -> dict:
        code, sortie = self.fournisseur.executer(ident, commande, self.delai_commande_s)
        e = lire_etat(sortie)
        self._etape({"commande": e.get("commande"), "code": code, "etat": e})
        return {**e, "code": code}

    def conduire(self) -> dict:
        man = json.loads(self.manifeste_local.read_text(encoding="utf-8"))
        b = float(man["B"])
        go = ligne_go(self.texte_go, self.go_id)
        verifier_go(go, b)
        echeance = echeance_epoch(go["echeance"])
        if os.environ.get("GO_ID") != self.go_id:
            raise GardeArret("condition 2 : GO_ID absent ou différent de la ligne citée")
        poste = Poste(b=b)
        ident = self.fournisseur.creer(self.offre, self.image, self.disque_go, self.env_instance)
        creation = self.horloge()
        c = self.fournisseur.taux_horaire(ident)
        poste.ajouter(ident, c, creation)
        self._etape({"instance": ident, "creee": creation, "c": c,
                     "ordre": ordre_de_lancement(self.go_id, b, c, man["commit_code"])})
        veille = Veilleur(self.fournisseur, poste, ident, echeance, self.sortie / "arrets-v2.jsonl",
                          horloge=self.horloge)
        veille.start()
        bilan = {"instance": ident}
        try:
            verifier_echeance(echeance, creation, b, c)
            depense = lambda: json.dumps({"d_avant": poste.d_avant(ident, self.horloge()), "c": c,
                                          "creation": creation, "b": b})
            code, sortie = self.fournisseur.executer(ident, script_amorce(man), self.delai_commande_s)
            if lire_etat(sortie).get("finie") is not True:
                raise GardeArret("amorce non finie")
            self.fournisseur.executer(ident, f"cat > /root/manifeste-v2.json <<'FIN'\n{json.dumps(man)}\nFIN")
            base = dict(manifeste="/root/manifeste-v2.json", clone="/root/public")
            mep = self._cmd(ident, commande_instance("mise-en-place", travail="/root/x/mise-en-place", **base))
            bilan["mise_en_place"] = mep
            if mep["code"] != 0:
                return bilan
            man["pas_par_tour"] = mep["pas_par_tour"]
            man["longueur_suffixe"] = mep["longueur_suffixe"]
            self.fournisseur.executer(ident, f"cat > /root/manifeste-v2.json <<'FIN'\n{json.dumps(man)}\nFIN")
            juge = self._cmd(ident, commande_instance("controle-juge", travail="/root/x/controle-juge", **base))
            bilan["controle_juge"] = juge
            if juge["code"] != 0:
                return bilan
            pilotes = []
            for phase in ("pilote", "pilote-reprise"):
                r = self._cmd(ident, commande_instance("executer", travail=f"/root/x/{phase}", phase=phase,
                                                       depense=depense(), echeance_go=echeance, **base))
                pilotes.append(r)
                if r["code"] == 0 and r.get("tours_marques") == 3 and r.get("cause_arret") is None:
                    break
            bilan["pilote"] = pilotes
            fixe_t = next((p for p in pilotes if "0" in p.get("durees", {}) and "1" in p.get("durees", {})), None)
            if fixe_t is None or not (pilotes[-1]["code"] == 0 and pilotes[-1].get("tours_marques") == 3):
                bilan["arret"] = "seconde chute du pilote, ou t introuvable : pas de run principal ; nœud"
                return bilan
            regle = self._cmd(ident, commande_instance("regle-tours", travail="/root/x/regle", depense=depense(),
                                                       pilote=f"/root/x/{fixe_t['phase']}", **base))
            bilan["regle"] = regle
            if regle["code"] != 0:
                return bilan
            man["regle_tours"] = {k: regle[k] for k in ("B", "R", "D", "c", "t", "H_heures", "K")}
            self.fournisseur.executer(ident, f"cat > /root/manifeste-v2.json <<'FIN'\n{json.dumps(man)}\nFIN")
            principal = self._cmd(ident, commande_instance("executer", travail="/root/x/principal", phase="principal",
                                                           depense=depense(), echeance_go=echeance, **base))
            bilan["principal"] = [principal]
            if principal.get("tours_marques", 0) < 20 and principal.get("cause_arret") is None and principal["code"] != 0:
                # erreur avant 20 tours complets : une seule relance, K recalculé sur le budget restant (même B, t)
                d = poste.depense(self.horloge())
                k2 = an.nombre_de_tours(b, round(d, 4), c, regle["t"])["K"]
                if k2 >= 20:
                    man["regle_tours"] = {**man["regle_tours"], "K": k2, "D": round(d, 4), "relance": True}
                    self.fournisseur.executer(ident, f"cat > /root/manifeste-v2.json <<'FIN'\n{json.dumps(man)}\nFIN")
                    bilan["principal"].append(self._cmd(ident, commande_instance(
                        "executer", travail="/root/x/principal-relance", phase="principal-relance",
                        depense=depense(), echeance_go=echeance, **base)))
            return bilan
        finally:
            self._rapatrier(ident, bilan)
            if veille.cause is None:
                self.fournisseur.detruire(ident)  # R10, par identifiant
                poste.detruite(ident, self.horloge())
            veille.arret.set()
            bilan["depense"] = poste.depense(self.horloge())
            self._etape({"instance": ident, "detruite": True, "depense": bilan["depense"]})
            (self.sortie / "bilan-conduite-v2.json").write_text(json.dumps(bilan, ensure_ascii=False, indent=2,
                                                                             sort_keys=True, default=str) + "\n")

    def _rapatrier(self, ident: str, bilan: dict) -> None:
        """Avant destruction : empreintes sur l'instance, transfert des journaux et des fichiers d'état, comparaison."""
        transferts = {}
        for dossier in ("mise-en-place", "controle-juge", "regle", "pilote", "pilote-reprise", "principal",
                        "principal-relance"):
            distant = f"/root/x/{dossier}"
            try:
                e = self._cmd(ident, commande_instance("empreintes", travail=distant))
            except Exception:
                continue
            if not e.get("fichiers"):
                for nom in FICHIERS_ETAT:
                    try:
                        self.fournisseur.rapatrier_fichier(ident, f"{distant}/{nom}", self.sortie / dossier / nom)
                    except Exception:
                        pass
                continue
            self.fournisseur.rapatrier_fichier(ident, f"{distant}/empreintes-instance-v2.json",
                                               self.sortie / dossier / "empreintes-instance-v2.json")
            emp = json.loads((self.sortie / dossier / "empreintes-instance-v2.json").read_text())
            transferts[dossier] = transferer(self.fournisseur, ident, distant, self.sortie / dossier, emp)
        bilan["transferts"] = {k: len(v) for k, v in transferts.items()}
