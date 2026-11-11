"""Exécuteur du bac sur la machine dédiée de l'essai Lean (D-1a) — v1.

Brouillon 3, § 4.5 (cloison et intégrité de la machine, VL-05), § 3.1 (G-L7 : fichier de contrôle du harnais).
Module **autonome** (bibliothèque standard et `gardes_lean_v1` seulement) : copié tel quel dans `/opt/harnais/` de la machine,
qui ne porte ni clé, ni dépôt du programme, ni aucun autre fichier du programme.

Ce que fait un appel (`verifier-lean` ou `executer-python`) :
1. dossier **neuf** par item sous `/srv/items/<item>` (refus si le dossier, celui du contrôle ou celui des sorties existe déjà) ;
2. le code de l'item tourne sous l'utilisateur sans privilège `bac`, dans une unité `systemd-run` (mémoire, tâches, temps de
   processus `LimitCPU`, durée murale, taille de fichier bornés ; `IPAddressDeny=any`) et dans `bwrap` (`--unshare-all` :
   aucun réseau, aucun PID visible ; racine vide ; `/usr`, la chaîne `/opt/elan`, Mathlib `/opt/mathlib` et `/opt/pybac`
   **en lecture seule** ; `/tmp` neuf ; seul le dossier de l'item en écriture) ; les sorties sont écrites par systemd dans un
   dossier du harnais que le bac ne voit pas ;
3. Lean : compilation du fichier de l'agent (`lean --json -o`), **puis** écriture du fichier de contrôle du harnais dans
   `/srv/controle/<item>` (hors du dossier de l'agent), exécuté dans un second bac où l'item et le contrôle sont en lecture
   seule ; empreinte du contrôle relevée avant et après (G-L7) ; verdict par `gardes_lean_v1.evaluer` ;
4. nettoyage : dossiers de l'item, du contrôle et des sorties détruits ; processus résiduels de `bac` relevés et arrêtés par
   PID (R10) ; rien ne persiste d'un item à l'autre.

Le mode « essai-local » (lanceur sans isolement) n'existe que pour les essais du harnais hors machine ; il est écrit en toutes
lettres dans chaque résultat (`"isolement": false`) et l'épreuve d'isolement le refuse.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import time
import uuid
from dataclasses import dataclass, field, replace
from pathlib import Path

if __package__:
    from . import gardes_lean_v1 as G
else:  # copie autonome sur la machine : `gardes_lean_v1.py` est dans le même dossier
    sys.dont_write_bytecode = True  # aucun .pyc dans /opt/harnais (manifeste de l'épreuve)
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import gardes_lean_v1 as G  # noqa: E402

VERSION = "executeur_bac_v1"
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
    racine_controle: Path = Path("/srv/controle")
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


def charger_config(chemin: str | Path, **surcharges) -> Config:
    """Lit `chaine-v1.json` (écrit à l'installation) : chemin de `lean`, `LEAN_PATH`, variante d'énumération."""
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


_RE_DUREE = re.compile(r"([\d.]+)\s*(h|min|ms|us|µs|s)\b")
_FACTEURS = {"h": 3600.0, "min": 60.0, "s": 1.0, "ms": 1e-3, "us": 1e-6, "µs": 1e-6}


def duree_systemd(texte: str) -> float | None:
    """« 1min 2.345s » → 62.345 ; None si rien ne se lit."""
    parts = _RE_DUREE.findall(texte)
    return sum(float(v) * _FACTEURS[u] for v, u in parts) if parts else None


def lire_resume_systemd(texte: str) -> dict:
    res = {"cpu_s": None, "memoire_pic": None, "duree_service_s": None, "resultat": None}
    for ligne in texte.splitlines():
        if "CPU time consumed:" in ligne:
            res["cpu_s"] = duree_systemd(ligne.split(":", 1)[1])
        elif "Memory peak:" in ligne:
            res["memoire_pic"] = ligne.split(":", 1)[1].strip()
        elif "Service runtime:" in ligne:
            res["duree_service_s"] = duree_systemd(ligne.split(":", 1)[1])
        elif "Finished with result:" in ligne:
            res["resultat"] = ligne.split(":", 1)[1].strip()
    return res


class LanceurBac:
    """Lanceur de la machine : `systemd-run` (limites, utilisateur `bac`, `IPAddressDeny=any`) puis `bwrap`."""
    isolement = True

    def __init__(self, cfg: Config, verifier_hote: bool = True):
        self.cfg = cfg
        if verifier_hote:
            if os.geteuid() != 0:
                raise ErreurBac("le lanceur du bac exige root (il lance `systemd-run` avec `User=bac`)")
            for outil in ("systemd-run", "bwrap"):
                if shutil.which(outil) is None:
                    raise ErreurBac(f"outil {outil} absent : aucun lancement sans isolement")

    def commande(self, l: Lancement, unite: str) -> list[str]:
        c = self.cfg
        sd = ["systemd-run", "--wait", "--collect", "--service-type=exec", f"--unit={unite}",
              "-p", f"User={c.utilisateur}", "-p", f"Group={c.utilisateur}",
              "-p", f"MemoryMax={c.memoire_max}", "-p", "MemorySwapMax=0", "-p", f"TasksMax={c.taches_max}",
              "-p", f"LimitCPU={c.cpu_max_s}", "-p", f"LimitFSIZE={c.taille_fichier_max}", "-p", "LimitNOFILE=1024",
              "-p", f"RuntimeMaxSec={c.duree_max_s}", "-p", "IPAddressDeny=any",
              "-p", "CPUAccounting=yes", "-p", "MemoryAccounting=yes", "-p", "StandardInput=null",
              "-p", f"StandardOutput=file:{l.sortie}", "-p", f"StandardError=file:{l.erreurs}"]
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
        # racine éphémère du bac en lecture seule : seuls `/tmp` et le dossier de l'item (s'il est lié en écriture) s'écrivent
        bw += ["--remount-ro", "/"]
        return sd + bw + ["--chdir", l.chdir, "--"] + list(l.argv)

    def lancer(self, l: Lancement, unite: str) -> dict:
        t0 = time.monotonic()
        p = subprocess.run(self.commande(l, unite), stdin=subprocess.DEVNULL, capture_output=True, text=True)
        res = lire_resume_systemd(p.stderr)
        res.update({"code": p.returncode, "duree_murale_s": round(time.monotonic() - t0, 3),
                    "resume_systemd": p.stderr[-4000:], "isolement": True})
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
        """Une seule passe ; un chemin logique n'est remplacé qu'en début de chemin (début, `=`, `:`) et suivi de `/`, `:` ou
        de la fin : le texte déjà remplacé n'est jamais relu."""
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
            p = subprocess.run(argv, stdin=subprocess.DEVNULL, stdout=so, stderr=se, env=env,
                               cwd=self._substituer(l.chdir, l.liaisons), timeout=self.cfg.duree_max_s)
        c1 = os.times()
        return {"code": p.returncode, "duree_murale_s": round(time.monotonic() - t0, 3),
                "cpu_s": round((c1.children_user - c0.children_user) + (c1.children_system - c0.children_system), 3),
                "memoire_pic": None, "duree_service_s": None, "resultat": None, "resume_systemd": "",
                "isolement": False}


def _sha256(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def _lire(chemin: Path) -> tuple[str, bool]:
    """Contenu (au plus SORTIE_MAX octets) et drapeau « tronqué »."""
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

    def __init__(self, cfg: Config, lanceur=None):
        self.cfg = cfg
        if lanceur is None:
            if cfg.mode != "bac":
                raise ErreurBac("mode « essai-local » : passer explicitement un LanceurEssaiLocal")
            lanceur = LanceurBac(cfg)
        if cfg.mode == "bac" and not getattr(lanceur, "isolement", False):
            raise ErreurBac("mode « bac » : un lanceur sans isolement est refusé")
        self.lanceur = lanceur

    # -- dossiers ---------------------------------------------------------------------------------------------------------
    def _dossiers_neufs(self, item: str, avec_controle: bool) -> tuple[Path, Path, Path | None]:
        _valider_item(item)
        d_item = self.cfg.racine_items / item
        d_sorties = self.cfg.racine_sorties / item
        d_ctrl = self.cfg.racine_controle / item if avec_controle else None
        for d in (d_item, d_sorties, d_ctrl):
            if d is not None and (d.exists() or d.is_symlink()):
                raise ErreurBac(f"{d} existe déjà : dossier neuf exigé par item (persistance ?)")
        d_sorties.mkdir(mode=0o700)
        d_item.mkdir(mode=0o700)
        if self.cfg.mode == "bac":
            shutil.chown(d_item, self.cfg.utilisateur, self.cfg.utilisateur)
        return d_item, d_sorties, d_ctrl

    def _ecrire_pour_bac(self, chemin: Path, texte: str) -> None:
        chemin.write_text(texte, encoding="utf-8")
        os.chmod(chemin, 0o600)
        if self.cfg.mode == "bac":
            shutil.chown(chemin, self.cfg.utilisateur, self.cfg.utilisateur)

    def _nettoyer(self, *dossiers: Path | None) -> list[str]:
        for d in dossiers:
            if d is not None and d.exists():
                shutil.rmtree(d)
        restes = [str(d) for d in dossiers if d is not None and d.exists()]
        return restes

    def processus_residuels(self) -> list[int]:
        """PID des processus de `bac` encore vivants, chacun arrêté par son PID (R10)."""
        if self.cfg.mode != "bac":
            return []
        p = subprocess.run(["ps", "-u", self.cfg.utilisateur, "-o", "pid="], capture_output=True, text=True)
        pids = [int(x) for x in p.stdout.split()]
        for pid in pids:
            try:
                os.kill(pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        return pids

    def _env(self, lean_path_supplementaire: str | None = None) -> dict[str, str]:
        lp = self.cfg.lean_path + (":" + lean_path_supplementaire if lean_path_supplementaire else "")
        return {"HOME": "/tmp", "PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LEAN_PATH": lp}

    # -- Lean ---------------------------------------------------------------------------------------------------------------
    def verifier_lean(self, item: str, source: str, m: int) -> dict:
        if len(source.encode("utf-8")) > G.TAILLE_MAX_SOURCE:
            raise ErreurBac(f"fichier de l'agent de plus de {G.TAILLE_MAX_SOURCE} octets")
        d_item, d_sorties, d_ctrl = self._dossiers_neufs(item, avec_controle=True)
        try:
            self._ecrire_pour_bac(d_item / "Item.lean", source)
            compil = self.lanceur.lancer(Lancement(
                argv=[self.cfg.lean, "--json", "--root=/item", "-o", "/item/Item.olean", "-i", "/item/Item.ilean",
                      "/item/Item.lean"],
                liaisons={"/item": (str(d_item), True)}, chdir="/item", env=self._env(),
                sortie=d_sorties / "compilation.out", erreurs=d_sorties / "compilation.err"), f"bac-{item}-compilation")
            olean = (d_item / "Item.olean").is_file()
            sortie_c, tronq_c = _lire(d_sorties / "compilation.out")
            # G-L7 : le fichier de contrôle n'existe qu'après la compilation de l'agent, hors de son dossier
            analyse = G.analyser_texte(source, m, self.cfg.supplementaires)
            texte, carte = G.fichier_controle(m, analyse["definitions"], self.cfg.variante_enumeration)
            d_ctrl.mkdir(mode=0o755)
            f_ctrl = d_ctrl / "Controle.lean"
            f_ctrl.write_text(texte, encoding="utf-8")
            os.chmod(f_ctrl, 0o644)
            empreinte_ecrite = G.empreinte_texte(texte)
            ctrl = self.lanceur.lancer(Lancement(
                argv=[self.cfg.lean, "--json", "--root=/controle", "/controle/Controle.lean"],
                liaisons={"/item": (str(d_item), False), "/controle": (str(d_ctrl), False)}, chdir="/controle",
                env=self._env("/item"), sortie=d_sorties / "controle.out", erreurs=d_sorties / "controle.err"),
                f"bac-{item}-controle")
            empreinte_apres = _sha256(f_ctrl)
            sortie_k, tronq_k = _lire(d_sorties / "controle.out")
            verdict = G.evaluer(source, m,
                                {"code": compil["code"], "sortie": sortie_c, "olean_present": olean},
                                {"code": ctrl["code"], "sortie": sortie_k, "texte": texte, "carte": carte,
                                 "empreinte_ecrite": empreinte_ecrite, "empreinte_apres": empreinte_apres},
                                self.cfg.supplementaires)
            if tronq_c:
                verdict["gardes"]["G-L1"]["motifs"].append("sortie de compilation tronquée")
                verdict["gardes"]["G-L1"]["ok"] = False
            if tronq_k:
                verdict["gardes"]["G-L7"]["motifs"].append("sortie du contrôle tronquée")
                verdict["gardes"]["G-L7"]["ok"] = False
            verdict["accepte_gardes"] = all(g["ok"] for g in verdict["gardes"].values())
            res = {"version": VERSION, "mode": self.cfg.mode, "isolement": bool(self.lanceur.isolement),
                   "item": item, "etapes": m, "compilation": _public(compil), "controle": _public(ctrl),
                   "sortie_compilation": sortie_c[:EXTRAIT_MAX], "sortie_controle": sortie_k[:EXTRAIT_MAX],
                   "erreurs_compilation": _lire(d_sorties / "compilation.err")[0][:EXTRAIT_MAX],
                   "empreinte_controle": empreinte_ecrite, "verdict": verdict}
        finally:
            restes = self._nettoyer(d_item, d_ctrl, d_sorties)
        res["processus_residuels"] = self.processus_residuels()
        res["dossiers_restants"] = restes
        return res

    # -- Python (bras S) ----------------------------------------------------------------------------------------------------
    def executer_python(self, item: str, code: str) -> dict:
        if len(code.encode("utf-8")) > G.TAILLE_MAX_SOURCE:
            raise ErreurBac(f"code de plus de {G.TAILLE_MAX_SOURCE} octets")
        d_item, d_sorties, _ = self._dossiers_neufs(item, avec_controle=False)
        try:
            self._ecrire_pour_bac(d_item / "code.py", code)
            r = self.lanceur.lancer(Lancement(
                argv=[self.cfg.python, "-I", "-B", "/item/code.py"], liaisons={"/item": (str(d_item), True)},
                chdir="/item", env={"HOME": "/tmp", "PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "MPLBACKEND": "Agg"},
                sortie=d_sorties / "python.out", erreurs=d_sorties / "python.err"), f"bac-{item}-python")
            so, tronq_o = _lire(d_sorties / "python.out")
            se, _ = _lire(d_sorties / "python.err")
            res = {"version": VERSION, "mode": self.cfg.mode, "isolement": bool(self.lanceur.isolement),
                   "item": item, "execution": _public(r), "stdout": so[:EXTRAIT_MAX], "stderr": se[:EXTRAIT_MAX],
                   "stdout_tronque": tronq_o or len(so) > EXTRAIT_MAX}
        finally:
            restes = self._nettoyer(d_item, d_sorties)
        res["processus_residuels"] = self.processus_residuels()
        res["dossiers_restants"] = restes
        return res


def _public(r: dict) -> dict:
    return {k: r.get(k) for k in ("code", "duree_murale_s", "cpu_s", "memoire_pic", "duree_service_s", "resultat",
                                  "isolement", "resume_systemd")}


def nouvel_item() -> str:
    return uuid.uuid4().hex


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Exécuteur du bac de l'essai Lean (D-1a), v1")
    ap.add_argument("action", choices=["verifier-lean", "executer-python"])
    ap.add_argument("--chaine", default="/opt/harnais/chaine-v1.json")
    ap.add_argument("--item", default="auto")
    ap.add_argument("--etapes", type=int, default=0)
    ap.add_argument("--sans-supplementaires", action="store_true", help="désactive G-L3+ (ajout du développeur)")
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
