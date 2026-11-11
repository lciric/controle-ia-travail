"""Exécuteur du bac sur la machine dédiée de l'essai Lean (D-1a) — v2.

v2 (contre-lecture `contre-lecture-harnais-d1a-v1.md`, `2077ae26…`, R-2300) ; la v1 reste telle quelle (R12) :
- CLL-04 : le fichier de contrôle n'est écrit sur aucun disque : il passe par l'**entrée standard** (`lean --stdin --json`, tube
  de `systemd-run --pipe`) ; c'est le harnais (ce processus, hors du bac) qui écrit `controle.out` ; le marqueur de fin porte un
  nonce tiré ici ; code de sortie vérifié par `gardes_lean_v2.evaluer` ;
- CLL-07 : les processus résiduels sont cherchés dans le **groupe de contrôle de l'unité de l'item** seulement
  (`systemctl show -p ControlGroup`, `cgroup.procs`) et arrêtés par PID (R10) ; les items voisins ne sont plus touchés ;
- CLL-13 : en mode « bac », aucun item sans réseau sortant **éprouvé fermé** (sonde `sonde_reseau_v1`, tampon dans `/run`
  lié au démarrage courant) ;
- CLL-15 : une panne du bac (`bwrap` qui ne monte pas, `systemd-run` sans résultat, résultat inattendu) arrête (`ErreurBac`) ;
  un arrêt par durée murale ou par temps de processus est un incident « délai », par mémoire un incident « mémoire » ;
- CLL-14 : sorties tronquées signalées aux gardes (G-L1, G-L7).
Module **autonome** (bibliothèque standard, `gardes_lean_v2`, `sonde_reseau_v1`), copié tel quel dans `/opt/harnais/`.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import secrets
import shutil
import signal
import subprocess
import sys
import time
import uuid
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from pathlib import Path

if __package__:
    from . import gardes_lean_v2 as G
    from . import sonde_reseau_v1 as SONDE
else:  # copie autonome sur la machine
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import gardes_lean_v2 as G  # noqa: E402
    import sonde_reseau_v1 as SONDE  # noqa: E402

VERSION = "executeur_bac_v2"
RE_ITEM = re.compile(r"^[A-Za-z0-9_-]{8,64}$")
SORTIE_MAX = 16 * 1024 * 1024
EXTRAIT_MAX = 64 * 1024


class ErreurBac(RuntimeError):
    """Arrêt de l'exécuteur (R5) : jamais attrapée pour continuer."""


@dataclass(frozen=True)
class Config:
    lean: str
    lean_path: str
    python: str = "/opt/pybac/bin/python"
    racine_items: Path = Path("/srv/items")
    racine_sorties: Path = Path("/srv/sorties")
    utilisateur: str = "bac"
    liaisons_ro: tuple[str, ...] = ("/opt/elan", "/opt/mathlib", "/opt/pybac")
    memoire_max: str = "6G"
    taches_max: int = 256
    cpu_max_s: int = 1800
    duree_max_s: int = 2100
    taille_fichier_max: str = "1G"
    variante_enumeration: str = "A"
    supplementaires: bool = True
    mode: str = "bac"  # "bac" (machine) ou "essai-local" (essais du harnais, sans isolement)
    tampon_reseau: Path = Path("/run/lean-essai-d1a/reseau-ferme-v1.json")
    racine_cgroup: Path = Path("/sys/fs/cgroup")


def charger_config(chemin: str | Path, **surcharges) -> Config:
    d = json.loads(Path(chemin).read_text(encoding="utf-8"))
    for cle in ("lean", "lean_path", "variante_enumeration"):
        if not d.get(cle):
            raise ErreurBac(f"{chemin} : clé {cle!r} absente ou vide")
    cfg = Config(lean=d["lean"], lean_path=d["lean_path"], variante_enumeration=d["variante_enumeration"],
                 python=d.get("python", "/opt/pybac/bin/python"))
    return replace(cfg, **surcharges)


@dataclass
class Lancement:
    argv: list[str]                          # chemins logiques (vus du bac)
    liaisons: dict[str, tuple[str, bool]]    # cible logique → (chemin réel, écriture permise)
    chdir: str
    env: dict[str, str]
    sortie: Path                             # sortie standard (chemin réel, dossier du harnais)
    erreurs: Path                            # sortie d'erreur (chemin réel, dossier du harnais)
    entree: str | None = None                # entrée standard (tube) ; jamais un fichier


_RE_DUREE = re.compile(r"([\d.]+)\s*(h|min|ms|us|µs|s)\b")
_FACTEURS = {"h": 3600.0, "min": 60.0, "s": 1.0, "ms": 1e-3, "us": 1e-6, "µs": 1e-6}


def duree_systemd(texte: str) -> float | None:
    parts = _RE_DUREE.findall(texte)
    return sum(float(v) * _FACTEURS[u] for v, u in parts) if parts else None


def lire_resume_systemd(texte: str) -> dict:
    res = {"cpu_s": None, "memoire_pic": None, "duree_service_s": None, "resultat": None, "fin": None}
    for ligne in texte.splitlines():
        if "CPU time consumed:" in ligne:
            res["cpu_s"] = duree_systemd(ligne.split(":", 1)[1])
        elif "Memory peak:" in ligne:
            res["memoire_pic"] = ligne.split(":", 1)[1].strip()
        elif "Service runtime:" in ligne:
            res["duree_service_s"] = duree_systemd(ligne.split(":", 1)[1])
        elif "Finished with result:" in ligne:
            res["resultat"] = ligne.split(":", 1)[1].strip()
        elif "Main processes terminated with:" in ligne:
            res["fin"] = ligne.split(":", 1)[1].strip()
    return res


def residus_unite(unite: str, executer=subprocess.run, racine: Path = Path("/sys/fs/cgroup"), tuer=os.kill) -> list[int]:
    """CLL-07 : processus encore vivants dans le groupe de contrôle de **cette** unité, arrêtés chacun par son PID (R10)."""
    p = executer(["systemctl", "show", "-p", "ControlGroup", "--value", f"{unite}.service"],
                 capture_output=True, text=True)
    groupe = (p.stdout or "").strip()
    if not groupe:
        return []
    procs = racine / groupe.lstrip("/") / "cgroup.procs"
    if not procs.exists():
        return []
    pids = [int(x) for x in procs.read_text().split()]
    for pid in pids:
        try:
            tuer(pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    return pids


def classer_execution(res: dict, texte_erreurs: str) -> str | None:
    """CLL-15 : panne du bac ⇒ `ErreurBac` ; arrêt par durée ou temps de processus ⇒ « délai » ; par mémoire ⇒ « mémoire » ;
    sinon None (l'issue appartient au code de l'item)."""
    if any(x.startswith("bwrap:") for x in texte_erreurs.splitlines()):
        raise ErreurBac(f"bwrap n'a pas monté le bac : {texte_erreurs.strip()[:300]}")
    if not res.get("isolement"):
        return None
    resultat = res.get("resultat")
    if resultat is None:
        raise ErreurBac(f"systemd-run sans résultat (lancement en échec, code {res.get('code')})")
    if resultat in ("success", "exit-code"):
        return None
    if resultat == "timeout":
        return "délai"
    if resultat == "oom-kill":
        return "mémoire"
    if resultat in ("signal", "core-dump"):
        return "délai" if "XCPU" in (res.get("fin") or "") else None
    raise ErreurBac(f"résultat systemd inattendu {resultat!r} : panne du bac")


class LanceurBac:
    """`systemd-run` (limites, utilisateur `bac`, `IPAddressDeny=any`) puis `bwrap`. Avec une entrée : `--pipe`, le harnais
    écrit lui-même la sortie (CLL-04)."""
    isolement = True

    def __init__(self, cfg: Config, verifier_hote: bool = True, executer=subprocess.run):
        self.cfg = cfg
        self.executer = executer
        if verifier_hote:
            if os.geteuid() != 0:
                raise ErreurBac("le lanceur du bac exige root (il lance `systemd-run` avec `User=bac`)")
            for outil in ("systemd-run", "bwrap", "systemctl"):
                if shutil.which(outil) is None:
                    raise ErreurBac(f"outil {outil} absent : aucun lancement sans isolement")

    def commande(self, l: Lancement, unite: str) -> list[str]:
        c = self.cfg
        sd = ["systemd-run", "--wait", "--collect", "--service-type=exec", f"--unit={unite}"]
        sd += ["--pipe"] if l.entree is not None else []
        sd += ["-p", f"User={c.utilisateur}", "-p", f"Group={c.utilisateur}",
               "-p", f"MemoryMax={c.memoire_max}", "-p", "MemorySwapMax=0", "-p", f"TasksMax={c.taches_max}",
               "-p", f"LimitCPU={c.cpu_max_s}", "-p", f"LimitFSIZE={c.taille_fichier_max}", "-p", "LimitNOFILE=1024",
               "-p", f"RuntimeMaxSec={c.duree_max_s}", "-p", "IPAddressDeny=any",
               "-p", "CPUAccounting=yes", "-p", "MemoryAccounting=yes"]
        if l.entree is None:
            sd += ["-p", "StandardInput=null", "-p", f"StandardOutput=file:{l.sortie}",
                   "-p", f"StandardError=file:{l.erreurs}"]
        bw = ["bwrap", "--unshare-all", "--die-with-parent", "--new-session", "--clearenv", "--cap-drop", "ALL",
              "--ro-bind", "/usr", "/usr", "--symlink", "usr/bin", "/bin", "--symlink", "usr/lib", "/lib",
              "--symlink", "usr/lib64", "/lib64", "--symlink", "usr/sbin", "/sbin",
              "--ro-bind", "/etc/ld.so.cache", "/etc/ld.so.cache",
              "--proc", "/proc", "--dev", "/dev", "--tmpfs", "/tmp"]
        for chemin in c.liaisons_ro:
            bw += ["--ro-bind", chemin, chemin]
        for cible, (reel, ecriture) in l.liaisons.items():
            bw += ["--bind" if ecriture else "--ro-bind", reel, cible]
        for k, v in l.env.items():
            bw += ["--setenv", k, v]
        bw += ["--remount-ro", "/"]
        return sd + bw + ["--chdir", l.chdir, "--"] + list(l.argv)

    def lancer(self, l: Lancement, unite: str) -> dict:
        t0 = time.monotonic()
        if l.entree is not None:
            p = self.executer(self.commande(l, unite), input=l.entree, capture_output=True, text=True)
            l.sortie.write_text(p.stdout, encoding="utf-8")    # le harnais écrit la sortie, hors du bac
            l.erreurs.write_text(p.stderr, encoding="utf-8")
        else:
            p = self.executer(self.commande(l, unite), stdin=subprocess.DEVNULL, capture_output=True, text=True)
        res = lire_resume_systemd(p.stderr)
        res.update({"code": p.returncode, "duree_murale_s": round(time.monotonic() - t0, 3),
                    "resume_systemd": p.stderr[-4000:], "isolement": True,
                    "residus": residus_unite(unite, self.executer, self.cfg.racine_cgroup)})
        return res


class LanceurEssaiLocal:
    """Lanceur des essais du harnais hors machine : **aucun isolement** (substitution des chemins logiques seulement)."""
    isolement = False

    def __init__(self, cfg: Config):
        if cfg.mode != "essai-local":
            raise ErreurBac("le lanceur sans isolement n'existe qu'en mode « essai-local »")
        self.cfg = cfg

    @staticmethod
    def _substituer(texte: str, liaisons: dict[str, tuple[str, bool]]) -> str:
        if not liaisons:
            return texte
        cibles = "|".join(re.escape(c) for c in sorted(liaisons, key=len, reverse=True))
        motif = re.compile(r"(?:(?<=^)|(?<==)|(?<=:))(" + cibles + r")(?=/|:|$)")
        return motif.sub(lambda m: liaisons[m.group(1)][0], texte)

    def lancer(self, l: Lancement, unite: str) -> dict:
        argv = [self._substituer(a, l.liaisons) for a in l.argv]
        env = {k: self._substituer(v, l.liaisons) for k, v in l.env.items()}
        env["PATH"] = os.environ.get("PATH", "/usr/bin:/bin")
        t0, c0 = time.monotonic(), os.times()
        with open(l.sortie, "wb") as so, open(l.erreurs, "wb") as se:
            p = subprocess.run(argv, input=None if l.entree is None else l.entree.encode("utf-8"),
                               stdin=subprocess.DEVNULL if l.entree is None else None, stdout=so, stderr=se, env=env,
                               cwd=self._substituer(l.chdir, l.liaisons), timeout=self.cfg.duree_max_s)
        c1 = os.times()
        return {"code": p.returncode, "duree_murale_s": round(time.monotonic() - t0, 3),
                "cpu_s": round((c1.children_user - c0.children_user) + (c1.children_system - c0.children_system), 3),
                "memoire_pic": None, "duree_service_s": None, "resultat": None, "fin": None, "resume_systemd": "",
                "isolement": False, "residus": []}


def _id_demarrage() -> str:
    return Path("/proc/sys/kernel/random/boot_id").read_text().strip()


def exiger_reseau_ferme(cfg: Config, relever=None, juger=None, id_demarrage=_id_demarrage) -> dict:
    """CLL-13 : aucun item sans sortie réseau éprouvée fermée depuis le démarrage courant. Le tampon (dans `/run`, effacé au
    redémarrage) évite de relancer la sonde à chaque item ; il n'est jamais visible du bac."""
    demarrage = id_demarrage()
    if cfg.tampon_reseau.exists():
        d = json.loads(cfg.tampon_reseau.read_text(encoding="utf-8"))
        if d.get("id_demarrage") == demarrage and d.get("ecarts") == []:
            return d
    releve = (relever or SONDE.relever)()
    ecarts = (juger or SONDE.juger)(releve, "fermee")
    if ecarts:
        raise ErreurBac(f"réseau sortant non éprouvé fermé : aucun item ne tourne ({ecarts[:3]})")
    d = {"id_demarrage": demarrage, "heure": datetime.now(timezone.utc).isoformat(timespec="seconds"),
         "releve": releve, "ecarts": []}
    cfg.tampon_reseau.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    cfg.tampon_reseau.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    return d


def _lire(chemin: Path) -> tuple[str, bool]:
    if not chemin.exists():
        return "", False
    taille = chemin.stat().st_size
    with open(chemin, "rb") as f:
        donnees = f.read(SORTIE_MAX)
    return donnees.decode("utf-8", errors="replace"), taille > SORTIE_MAX


def _valider_item(item: str) -> None:
    if not RE_ITEM.match(item):
        raise ErreurBac(f"identifiant d'item invalide {item!r} (8 à 64 caractères [A-Za-z0-9_-])")


class Bac:
    """Un item = un dossier neuf, détruit après l'item. Rien ne persiste."""

    def __init__(self, cfg: Config, lanceur=None, relever=None, id_demarrage=_id_demarrage):
        self.cfg = cfg
        if lanceur is None:
            if cfg.mode != "bac":
                raise ErreurBac("mode « essai-local » : passer explicitement un LanceurEssaiLocal")
            lanceur = LanceurBac(cfg)
        if cfg.mode == "bac" and not getattr(lanceur, "isolement", False):
            raise ErreurBac("mode « bac » : un lanceur sans isolement est refusé")
        self.lanceur = lanceur
        self.reseau = exiger_reseau_ferme(cfg, relever, id_demarrage=id_demarrage) if cfg.mode == "bac" else None

    def _dossiers_neufs(self, item: str) -> tuple[Path, Path]:
        _valider_item(item)
        d_item = self.cfg.racine_items / item
        d_sorties = self.cfg.racine_sorties / item
        for d in (d_item, d_sorties):
            if d.exists() or d.is_symlink():
                raise ErreurBac(f"{d} existe déjà : dossier neuf exigé par item (persistance ?)")
        d_sorties.mkdir(mode=0o700)
        d_item.mkdir(mode=0o700)
        if self.cfg.mode == "bac":
            shutil.chown(d_item, self.cfg.utilisateur, self.cfg.utilisateur)
        return d_item, d_sorties

    def _ecrire_pour_bac(self, chemin: Path, texte: str) -> None:
        chemin.write_text(texte, encoding="utf-8")
        os.chmod(chemin, 0o600)
        if self.cfg.mode == "bac":
            shutil.chown(chemin, self.cfg.utilisateur, self.cfg.utilisateur)

    @staticmethod
    def _nettoyer(*dossiers: Path) -> list[str]:
        for d in dossiers:
            if d.exists():
                shutil.rmtree(d)
        return [str(d) for d in dossiers if d.exists()]

    def _env(self, lean_path_supplementaire: str | None = None) -> dict[str, str]:
        lp = self.cfg.lean_path + (":" + lean_path_supplementaire if lean_path_supplementaire else "")
        return {"HOME": "/tmp", "PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LEAN_PATH": lp}

    def verifier_lean(self, item: str, source: str, m: int) -> dict:
        if len(source.encode("utf-8")) > G.TAILLE_MAX_SOURCE:
            raise ErreurBac(f"fichier de l'agent de plus de {G.TAILLE_MAX_SOURCE} octets")
        d_item, d_sorties = self._dossiers_neufs(item)
        try:
            self._ecrire_pour_bac(d_item / "Item.lean", source)
            compil = self.lanceur.lancer(Lancement(
                argv=[self.cfg.lean, "--json", "--root=/item", "-o", "/item/Item.olean", "-i", "/item/Item.ilean",
                      "/item/Item.lean"],
                liaisons={"/item": (str(d_item), True)}, chdir="/item", env=self._env(),
                sortie=d_sorties / "compilation.out", erreurs=d_sorties / "compilation.err"), f"bac-{item}-compilation")
            err_c, _ = _lire(d_sorties / "compilation.err")
            incident_c = classer_execution(compil, err_c)
            olean = (d_item / "Item.olean").is_file()
            sortie_c, tronq_c = _lire(d_sorties / "compilation.out")
            # G-L7 : contrôle écrit après la compilation, jamais sur un disque vu du bac, nonce tiré ici
            analyse = G.analyser_texte(source, m, self.cfg.supplementaires)
            nonce = secrets.token_hex(16)
            texte, carte = G.fichier_controle(m, analyse["definitions"], nonce, self.cfg.variante_enumeration)
            ctrl = self.lanceur.lancer(Lancement(
                argv=[self.cfg.lean, "--stdin", "--json"], liaisons={"/item": (str(d_item), False)}, chdir="/tmp",
                env=self._env("/item"), sortie=d_sorties / "controle.out", erreurs=d_sorties / "controle.err",
                entree=texte), f"bac-{item}-controle")
            err_k, _ = _lire(d_sorties / "controle.err")
            incident_k = classer_execution(ctrl, err_k)
            sortie_k, tronq_k = _lire(d_sorties / "controle.out")
            verdict = G.evaluer(source, m,
                                {"code": compil["code"], "sortie": sortie_c, "olean_present": olean,
                                 "sortie_tronquee": tronq_c},
                                {"code": ctrl["code"], "sortie": sortie_k, "texte": texte, "carte": carte,
                                 "nonce": nonce, "sortie_tronquee": tronq_k},
                                self.cfg.supplementaires)
            res = {"version": VERSION, "mode": self.cfg.mode, "isolement": bool(self.lanceur.isolement),
                   "item": item, "etapes": m, "compilation": _public(compil), "controle": _public(ctrl),
                   "incident_bac": incident_c or incident_k,
                   "sortie_compilation": sortie_c[:EXTRAIT_MAX], "sortie_controle": sortie_k[:EXTRAIT_MAX],
                   "erreurs_compilation": err_c[:EXTRAIT_MAX], "empreinte_controle": G.empreinte_texte(texte),
                   "verdict": verdict, "processus_residuels": compil.get("residus", []) + ctrl.get("residus", [])}
        finally:
            restes = self._nettoyer(d_item, d_sorties)
        res["dossiers_restants"] = restes
        return res

    def executer_python(self, item: str, code: str) -> dict:
        if len(code.encode("utf-8")) > G.TAILLE_MAX_SOURCE:
            raise ErreurBac(f"code de plus de {G.TAILLE_MAX_SOURCE} octets")
        d_item, d_sorties = self._dossiers_neufs(item)
        try:
            self._ecrire_pour_bac(d_item / "code.py", code)
            r = self.lanceur.lancer(Lancement(
                argv=[self.cfg.python, "-I", "-B", "/item/code.py"], liaisons={"/item": (str(d_item), True)},
                chdir="/item", env={"HOME": "/tmp", "PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "MPLBACKEND": "Agg"},
                sortie=d_sorties / "python.out", erreurs=d_sorties / "python.err"), f"bac-{item}-python")
            so, tronq_o = _lire(d_sorties / "python.out")
            se, _ = _lire(d_sorties / "python.err")
            incident = classer_execution(r, se)
            res = {"version": VERSION, "mode": self.cfg.mode, "isolement": bool(self.lanceur.isolement),
                   "item": item, "execution": _public(r), "incident_bac": incident, "stdout": so[:EXTRAIT_MAX],
                   "stderr": se[:EXTRAIT_MAX], "stdout_tronque": tronq_o or len(so) > EXTRAIT_MAX,
                   "processus_residuels": r.get("residus", [])}
        finally:
            restes = self._nettoyer(d_item, d_sorties)
        res["dossiers_restants"] = restes
        return res


def _public(r: dict) -> dict:
    return {k: r.get(k) for k in ("code", "duree_murale_s", "cpu_s", "memoire_pic", "duree_service_s", "resultat", "fin",
                                  "isolement", "resume_systemd")}


def nouvel_item() -> str:
    return uuid.uuid4().hex


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Exécuteur du bac de l'essai Lean (D-1a), v2")
    ap.add_argument("action", choices=["verifier-lean", "executer-python"])
    ap.add_argument("--chaine", default="/opt/harnais/chaine-v1.json")
    ap.add_argument("--item", default="auto")
    ap.add_argument("--etapes", type=int, default=0)
    ap.add_argument("--sans-supplementaires", action="store_true",
                    help="désactive G-L3+ ; G-L7 échoue alors (elle en dépend)")
    a = ap.parse_args(argv)
    cfg = charger_config(a.chaine, supplementaires=not a.sans_supplementaires)
    item = nouvel_item() if a.item == "auto" else a.item
    texte = sys.stdin.read()
    bac = Bac(cfg)
    if a.action == "verifier-lean":
        if a.etapes < 1:
            raise ErreurBac("--etapes ≥ 1 exigé")
        res = bac.verifier_lean(item, texte, a.etapes)
    else:
        res = bac.executer_python(item, texte)
    json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
