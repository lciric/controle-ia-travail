"""Exécuteur du bac sur la machine dédiée de l'essai Lean (D-1a) — v7 (troisième essai, arbitrage Fable 5.2 point 7, pas 4 et 5 ;
GO-2026-11-21-40 : comprendre et corriger avant un quatrième essai).

Copie de `executeur_bac_v6.py` (inchangé, R12). Vérificateur, gardes et sonde inchangés. Trois changements :
1. **Classement du temps de processeur** (pas 4). Au troisième essai, l'item Python qui brûle le processeur a été tué par
   `LimitCPU` (5,011 s) ; le bac est sorti en code 137, que systemd rapporte `exit-code` : la v6, qui n'attendait « délai »
   que d'un résultat `signal` portant « XCPU », a rendu « aucun incident ». La v7 ne se fie pas au code de sortie (un item
   peut sortir en 137 de lui-même) : « délai » si systemd rapporte `timeout`, ou si l'unité n'a pas réussi (`exit-code`,
   `signal`, `core-dump`) **et** que le temps de processeur rapporté par systemd (« CPU time consumed », compte de l'unité
   entière, mis en cache par systemd 255 avant le retrait du cgroupe) atteint la limite `cpu_max_s`. Ce compte est celui de
   l'unité, la limite est par processus : pour un processus seul (Lean, Python sans enfant) les deux coïncident ; un item à
   plusieurs processus qui consomme ensemble la limite sans réussir sort « délai » (il a consommé son budget, il n'évite
   rien). Temps de processeur absent sur une unité qui n'a pas réussi : arrêt (R5, aucun repli silencieux).
2. **Pic de mémoire** (pas 5). Cause établie : systemd 255 (Ubuntu 24.04) ne met en cache, au retrait du cgroupe, que le temps
   de processeur (`unit_prune_cgroup`, `src/core/cgroup.c` de la v255) ; « Memory peak » de `systemd-run --wait` est la
   dernière valeur lue pendant que le cgroupe existait, en général au passage de l'unité à « active » (quelques centaines de
   Kio), juste en cas de `oom-kill` ou de `timeout` (lus pendant l'arrêt). La v7 **ne lit plus** « Memory peak » ; elle relève
   elle-même `memory.peak` du cgroupe de l'unité (`/sys/fs/cgroup/system.slice/<unité>.service`, tranche imposée par
   `--slice=system.slice`), par échantillonnage pendant que l'unité tourne : `memoire_pic_echantillonne_octets` est un
   **minorant** du pic (le plus haut relevé ; `memory.peak` ne décroît pas), `None` si aucun relevé.
3. La sortie d'erreur de la compilation (`compilation.err`) entre dans le résultat, bornée (`erreurs_compilation`).

Texte de la v6 : Exécuteur du bac sur la machine dédiée de l'essai Lean (D-1a) — v6 (R-2464, sous R-2439).

Copie de `executeur_bac_v5.py` (inchangé, R12) dont seul le vérificateur change : `verificateur_noyau_v6.lean`.

Texte de la v5 : Exécuteur du bac sur la machine dédiée de l'essai Lean (D-1a) — v5 (réparation R-2439).

Copie de `executeur_bac_v4.py` (inchangé, R12) dont **seul le vérificateur change** : `verificateur_noyau_v5.lean` (portage
vers Lean 4.35.0) au lieu de `verificateur_noyau_v4.lean`, dans le chemin logique lancé dans le bac et dans le chemin par
défaut de la configuration ; nom de version. Gardes (`gardes_lean_v4`) et sonde (`sonde_reseau_v1`) inchangées.

Texte de la v4 : Exécuteur du bac sur la machine dédiée de l'essai Lean (D-1a) — v4 (contre-lecture courte de la v3 `b6ca886d…`, R-2307).

Même conception que la v3 (`executeur_bac_v3.py`, inchangé, R12), avec le vérificateur du noyau v4 et :
- note 3 et CLC3-05 (atténuation) : inventaire du dossier de l'item par `lstat` — chaque entrée doit être un fichier ordinaire
  à un seul lien, parmi `Item.lean`, `Item.olean`, `Item.ilean` ; `Item.olean` borné à 64 Mio ; tout écart fait échouer G-L7 ;
- CLC3-11 k05 : le témoin de montage exige le code 0 **et** le résultat « success ».
Module **autonome** (bibliothèque standard, `gardes_lean_v4`, `sonde_reseau_v1`), copié tel quel dans `/opt/harnais/`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import secrets
import shutil
import signal
import stat
import subprocess
import sys
import time
import uuid
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from pathlib import Path

if __package__:
    from . import gardes_lean_v4 as G
    from . import sonde_reseau_v1 as SONDE
else:  # copie autonome sur la machine
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import gardes_lean_v4 as G  # noqa: E402
    import sonde_reseau_v1 as SONDE  # noqa: E402

VERSION = "executeur_bac_v7"
TRANCHE = "system.slice"
PERIODE_ECHANTILLON_S = 0.1
OLEAN_MAX = 64 * 1024 * 1024
RE_ITEM = re.compile(r"^[A-Za-z0-9_-]{8,64}$")
SORTIE_MAX = 16 * 1024 * 1024
EXTRAIT_MAX = 64 * 1024
LOGIQUE_VERIFICATEUR = "/noyau/verificateur_noyau_v6.lean"


class ErreurBac(RuntimeError):
    """Arrêt de l'exécuteur (R5) : jamais attrapée pour continuer."""


@dataclass(frozen=True)
class Config:
    lean: str
    lean_path: str
    verificateur: str = "/opt/harnais/noyau/verificateur_noyau_v6.lean"
    verificateur_sha256: str = ""
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
    supplementaires: bool = True
    mode: str = "bac"
    tampon_reseau: Path = Path("/run/lean-essai-d1a/reseau-ferme-v1.json")
    tampon_age_max_s: int = 3600
    racine_cgroup: Path = Path("/sys/fs/cgroup")


def charger_config(chemin: str | Path, **surcharges) -> Config:
    d = json.loads(Path(chemin).read_text(encoding="utf-8"))
    for cle in ("lean", "lean_path", "verificateur_noyau_sha256"):
        if not d.get(cle):
            raise ErreurBac(f"{chemin} : clé {cle!r} absente ou vide (vérificateur du noyau non épinglé ?)")
    cfg = Config(lean=d["lean"], lean_path=d["lean_path"], verificateur_sha256=d["verificateur_noyau_sha256"],
                 verificateur=d.get("verificateur_noyau", Config.verificateur), python=d.get("python", Config.python))
    return replace(cfg, **surcharges)


@dataclass
class Lancement:
    argv: list[str]
    liaisons: dict[str, tuple[str, bool]]
    chdir: str
    env: dict[str, str]
    sortie: Path
    erreurs: Path


_RE_DUREE = re.compile(r"([\d.]+)\s*(h|min|ms|us|µs|s)\b")
_FACTEURS = {"h": 3600.0, "min": 60.0, "s": 1.0, "ms": 1e-3, "us": 1e-6, "µs": 1e-6}


def duree_systemd(texte: str) -> float | None:
    parts = _RE_DUREE.findall(texte)
    return sum(float(v) * _FACTEURS[u] for v, u in parts) if parts else None


def lire_resume_systemd(texte: str) -> dict:
    """v7 : « Memory peak » n'est plus lu (valeur en cache périmée sous systemd 255, voir l'en-tête)."""
    res = {"cpu_s": None, "duree_service_s": None, "resultat": None, "fin": None}
    for ligne in texte.splitlines():
        if "CPU time consumed:" in ligne:
            res["cpu_s"] = duree_systemd(ligne.split(":", 1)[1])
        elif "Service runtime:" in ligne:
            res["duree_service_s"] = duree_systemd(ligne.split(":", 1)[1])
        elif "Finished with result:" in ligne:
            res["resultat"] = ligne.split(":", 1)[1].strip()
        elif "Main processes terminated with:" in ligne:
            res["fin"] = ligne.split(":", 1)[1].strip()
    return res


def residus_unite(unite: str, executer=subprocess.run, racine: Path = Path("/sys/fs/cgroup"), tuer=os.kill) -> list[int]:
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


def classer_execution(res: dict, cpu_max_s: float) -> str | None:
    """CLC2-05, v7 : ne lit **que** ce que systemd rapporte (résultat et temps de processeur de l'unité, canal hors de portée de
    l'agent), jamais le code de sortie ni la fin du processus principal. La panne de montage du bac est établie à part, par
    le témoin de montage."""
    if not res.get("isolement"):
        return None
    resultat = res.get("resultat")
    if resultat is None:
        raise ErreurBac(f"systemd-run sans résultat (lancement en échec, code {res.get('code')})")
    if resultat == "success":
        return None
    if resultat == "timeout":
        return "délai"
    if resultat == "oom-kill":
        return "mémoire"
    if resultat in ("exit-code", "signal", "core-dump"):
        cpu = res.get("cpu_s")
        if cpu is None:
            raise ErreurBac(f"résultat {resultat!r} sans temps de processeur rapporté par systemd : classement impossible")
        return "délai" if cpu >= cpu_max_s else None
    raise ErreurBac(f"résultat systemd inattendu {resultat!r} : panne du bac")


def relever_memoire_pic(chemin: Path) -> int | None:
    """`memory.peak` du cgroupe de l'unité, en octets ; None si le fichier n'existe pas (encore ou plus)."""
    try:
        return int(chemin.read_text().strip())
    except (FileNotFoundError, ProcessLookupError):
        return None


class LanceurBac:
    isolement = True

    def __init__(self, cfg: Config, verifier_hote: bool = True, executer=subprocess.run, lancer_processus=subprocess.Popen,
                 dormir=time.sleep):
        self.cfg = cfg
        self.executer = executer
        self.lancer_processus = lancer_processus
        self.dormir = dormir
        if verifier_hote:
            if os.geteuid() != 0:
                raise ErreurBac("le lanceur du bac exige root (il lance `systemd-run` avec `User=bac`)")
            for outil in ("systemd-run", "bwrap", "systemctl"):
                if shutil.which(outil) is None:
                    raise ErreurBac(f"outil {outil} absent : aucun lancement sans isolement")

    def commande(self, l: Lancement, unite: str) -> list[str]:
        c = self.cfg
        sd = ["systemd-run", "--wait", "--collect", "--service-type=exec", f"--unit={unite}", f"--slice={TRANCHE}",
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
        bw += ["--remount-ro", "/"]
        return sd + bw + ["--chdir", l.chdir, "--"] + list(l.argv)

    def chemin_memoire_pic(self, unite: str) -> Path:
        return self.cfg.racine_cgroup / TRANCHE / f"{unite}.service" / "memory.peak"

    def lancer(self, l: Lancement, unite: str) -> dict:
        """v7 : `systemd-run --wait` en processus fils ; pendant qu'il attend, root relève `memory.peak` du cgroupe de l'unité
        (canal hors de portée de l'agent) toutes les `PERIODE_ECHANTILLON_S` ; le plus haut relevé est un minorant du pic."""
        t0 = time.monotonic()
        chemin = self.chemin_memoire_pic(unite)
        p = self.lancer_processus(self.commande(l, unite), stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        pic, echantillons = None, 0
        while p.poll() is None:
            v = relever_memoire_pic(chemin)
            if v is not None:
                pic, echantillons = (v if pic is None else max(pic, v)), echantillons + 1
            self.dormir(PERIODE_ECHANTILLON_S)
        _, stderr = p.communicate()
        erreurs_systemd = (stderr or b"")[-8000:].decode("utf-8", errors="replace")
        res = lire_resume_systemd(erreurs_systemd)
        res.update({"code": p.returncode, "duree_murale_s": round(time.monotonic() - t0, 3),
                    "memoire_pic_echantillonne_octets": pic, "memoire_echantillons": echantillons,
                    "resume_systemd": erreurs_systemd[-4000:], "isolement": True,
                    "residus": residus_unite(unite, self.executer, self.cfg.racine_cgroup)})
        return res

    def temoin_montage(self, l: Lancement, unite: str) -> None:
        """CLC2-05 : mêmes liaisons, `/usr/bin/true` ; tout échec est une panne du bac (le code de l'agent n'y tourne pas)."""
        t = Lancement(["/usr/bin/true"], l.liaisons, l.chdir, l.env, l.sortie.with_name(l.sortie.name + ".temoin"),
                      l.erreurs.with_name(l.erreurs.name + ".temoin"))
        r = self.lancer(t, unite + "-temoin")
        if r["code"] != 0 or r.get("resultat") != "success":
            texte = t.erreurs.read_bytes()[:2000].decode("utf-8", errors="replace") if t.erreurs.exists() else ""
            raise ErreurBac(f"témoin de montage en échec (code {r['code']}, {r.get('resultat')}) : panne du bac : {texte}")


class LanceurEssaiLocal:
    """Essais du harnais hors machine : **aucun isolement**."""
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
        t0 = time.monotonic()
        with open(l.sortie, "wb") as so, open(l.erreurs, "wb") as se:
            p = subprocess.run(argv, stdin=subprocess.DEVNULL, stdout=so, stderr=se, env=env,
                               cwd=self._substituer(l.chdir, l.liaisons), timeout=self.cfg.duree_max_s)
        return {"code": p.returncode, "duree_murale_s": round(time.monotonic() - t0, 3), "cpu_s": None,
                "memoire_pic_echantillonne_octets": None, "memoire_echantillons": 0, "duree_service_s": None,
                "resultat": None, "fin": None, "resume_systemd": "", "isolement": False, "residus": []}

    def temoin_montage(self, l: Lancement, unite: str) -> None:
        return None


def _id_demarrage() -> str:
    return Path("/proc/sys/kernel/random/boot_id").read_text().strip()


def exiger_reseau_ferme(cfg: Config, relever=None, juger=None, id_demarrage=_id_demarrage, maintenant=time.time) -> dict:
    """Aucun item sans sortie réseau éprouvée fermée, depuis le démarrage courant et depuis moins de `tampon_age_max_s`."""
    demarrage = id_demarrage()
    if cfg.tampon_reseau.exists():
        d = json.loads(cfg.tampon_reseau.read_text(encoding="utf-8"))
        if (d.get("id_demarrage") == demarrage and d.get("ecarts") == []
                and maintenant() - float(d.get("epoque", 0)) <= cfg.tampon_age_max_s):
            return d
    releve = (relever or SONDE.relever)()
    ecarts = (juger or SONDE.juger)(releve, "fermee")
    if ecarts:
        raise ErreurBac(f"réseau sortant non éprouvé fermé : aucun item ne tourne ({ecarts[:3]})")
    d = {"id_demarrage": demarrage, "epoque": maintenant(),
         "heure": datetime.now(timezone.utc).isoformat(timespec="seconds"), "releve": releve, "ecarts": []}
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


def _sha256(chemin: str | Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def inventorier(d_item: Path) -> tuple[list[str], bool]:
    """Noms du dossier de l'item, marqués s'ils ne sont pas un fichier ordinaire à un seul lien ou si l'`.olean` dépasse sa
    borne (le marquage les fait sortir de la liste permise : G-L7) ; et présence d'un `Item.olean` sain."""
    noms, olean = [], False
    for entree in sorted(d_item.iterdir()):
        st = os.lstat(entree)
        nom = entree.name
        if not stat.S_ISREG(st.st_mode) or st.st_nlink != 1:
            nom += " (lien ou fichier non ordinaire)"
        elif nom == "Item.olean":
            if st.st_size > OLEAN_MAX:
                nom += f" (plus de {OLEAN_MAX} octets)"
            else:
                olean = True
        noms.append(nom)
    return noms, olean


def _valider_item(item: str) -> None:
    if not RE_ITEM.match(item):
        raise ErreurBac(f"identifiant d'item invalide {item!r} (8 à 64 caractères [A-Za-z0-9_-])")


class Bac:
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

    def _lancer(self, l: Lancement, unite: str) -> dict:
        self.lanceur.temoin_montage(l, unite)
        return self.lanceur.lancer(l, unite)

    def _env(self) -> dict[str, str]:
        return {"HOME": "/tmp", "PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LEAN_PATH": self.cfg.lean_path}

    def verifier_lean(self, item: str, source: str, m: int) -> dict:
        if len(source.encode("utf-8")) > G.TAILLE_MAX_SOURCE:
            raise ErreurBac(f"fichier de l'agent de plus de {G.TAILLE_MAX_SOURCE} octets")
        if not self.cfg.verificateur_sha256 or _sha256(self.cfg.verificateur) != self.cfg.verificateur_sha256:
            raise ErreurBac("vérificateur du noyau absent, non épinglé ou d'empreinte différente : aucun item")
        d_item, d_sorties = self._dossiers_neufs(item)
        try:
            self._ecrire_pour_bac(d_item / "Item.lean", source)
            compil = self._lancer(Lancement(
                argv=[self.cfg.lean, "--json", "--root=/item", "-o", "/item/Item.olean", "-i", "/item/Item.ilean",
                      "/item/Item.lean"],
                liaisons={"/item": (str(d_item), True)}, chdir="/item", env=self._env(),
                sortie=d_sorties / "compilation.out", erreurs=d_sorties / "compilation.err"), f"bac-{item}-compilation")
            incident_c = classer_execution(compil, self.cfg.cpu_max_s)
            sortie_c, tronq_c = _lire(d_sorties / "compilation.out")
            inventaire, olean = inventorier(d_item)
            nonce = secrets.token_hex(16)
            verif = self._lancer(Lancement(
                argv=[self.cfg.lean, "--run", LOGIQUE_VERIFICATEUR, "/item/Item.olean", str(m), nonce],
                liaisons={"/item": (str(d_item), False),
                          "/noyau": (str(Path(self.cfg.verificateur).parent), False)},
                chdir="/tmp", env=self._env(), sortie=d_sorties / "noyau.out", erreurs=d_sorties / "noyau.err"),
                f"bac-{item}-noyau")
            incident_v = classer_execution(verif, self.cfg.cpu_max_s)
            sortie_v, tronq_v = _lire(d_sorties / "noyau.out")
            verdict = G.evaluer(source, m,
                                {"code": compil["code"], "sortie": sortie_c, "olean_present": olean,
                                 "sortie_tronquee": tronq_c},
                                {"code": verif["code"], "sortie": sortie_v, "nonce": nonce, "sortie_tronquee": tronq_v},
                                inventaire, self.cfg.supplementaires)
            res = {"version": VERSION, "mode": self.cfg.mode, "isolement": bool(self.lanceur.isolement),
                   "item": item, "etapes": m, "compilation": _public(compil), "noyau": _public(verif),
                   "incident_bac": incident_c or incident_v, "inventaire_item": inventaire,
                   "sortie_compilation": sortie_c[:EXTRAIT_MAX],
                   "erreurs_compilation": _lire(d_sorties / "compilation.err")[0][:EXTRAIT_MAX],
                   "sortie_noyau": sortie_v[:EXTRAIT_MAX],
                   "erreurs_noyau": _lire(d_sorties / "noyau.err")[0][:EXTRAIT_MAX], "verdict": verdict,
                   "processus_residuels": compil.get("residus", []) + verif.get("residus", [])}
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
            r = self._lancer(Lancement(
                argv=[self.cfg.python, "-I", "-B", "/item/code.py"], liaisons={"/item": (str(d_item), True)},
                chdir="/item", env={"HOME": "/tmp", "PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "MPLBACKEND": "Agg"},
                sortie=d_sorties / "python.out", erreurs=d_sorties / "python.err"), f"bac-{item}-python")
            incident = classer_execution(r, self.cfg.cpu_max_s)
            so, tronq_o = _lire(d_sorties / "python.out")
            se, _ = _lire(d_sorties / "python.err")
            res = {"version": VERSION, "mode": self.cfg.mode, "isolement": bool(self.lanceur.isolement),
                   "item": item, "execution": _public(r), "incident_bac": incident, "stdout": so[:EXTRAIT_MAX],
                   "stderr": se[:EXTRAIT_MAX], "stdout_tronque": tronq_o or len(so) > EXTRAIT_MAX,
                   "processus_residuels": r.get("residus", [])}
        finally:
            restes = self._nettoyer(d_item, d_sorties)
        res["dossiers_restants"] = restes
        return res


def _public(r: dict) -> dict:
    return {k: r.get(k) for k in ("code", "duree_murale_s", "cpu_s", "memoire_pic_echantillonne_octets",
                                  "memoire_echantillons", "duree_service_s", "resultat", "fin", "isolement",
                                  "resume_systemd")}


def nouvel_item() -> str:
    return uuid.uuid4().hex


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Exécuteur du bac de l'essai Lean (D-1a), v7")
    ap.add_argument("action", choices=["verifier-lean", "executer-python"])
    ap.add_argument("--chaine", default="/opt/harnais/chaine-v1.json")
    ap.add_argument("--item", default="auto")
    ap.add_argument("--etapes", type=int, default=0)
    ap.add_argument("--sans-supplementaires", action="store_true", help="désactive G-L3+ (seconde ligne)")
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
