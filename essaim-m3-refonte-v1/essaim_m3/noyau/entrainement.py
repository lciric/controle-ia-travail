"""Apprentissage par gradient servi par le noyau — étape 1 du programme « gradient conçu par l'essaim » (décision de
Lazar du 24 octobre 2026, 18:22 et 18:23 : « go, commençons par là ») : des **sondes** apprises sur des traits.

Principe (contrat v3) : l'organisme écrit une spécification — les données (identifiants de tâches d'entraînement,
jamais de test), l'objectif (code Python d'une fonction de perte `perte(p, y)` qu'il conçoit lui-même : Brier, score
logarithmique borné, charnière, Tsallis…), l'algorithme (descente de gradient sur une sonde linéaire ou à une couche
cachée, pas, taux, régularisation, lot, graine) — et le noyau l'exécute hors du processus de l'organisme, sous bornes,
sur des **traits** par tâche :
- en réel (étape 1) : les activations de Llama-3.1-8B-Instruct sur chaque tâche de la banque, extraites une fois sur
  la carte (job sous GO) et mises en cache (`traits.npz` : identifiant → vecteur) ; l'entraînement lui-même tourne sur
  processeur, en bac à sable ;
- en simulation : des traits de hachage du texte (`traits_simules`), déterministes.
Le gradient de l'objectif par rapport aux sorties est pris par différences finies (l'organisme n'a pas à l'écrire) ;
le reste est analytique. Le noyau rend un identifiant de modèle local ; `predire(identifiant, ids)` rend des
probabilités pour n'importe quelles tâches (entraînement ou test), **jamais les vérités**. Tout est journalisé
(`journal-entrainements.jsonl`), borné (`entrainements_max`, `pas_max`, délai, mémoire), et une erreur est un statut,
jamais un texte (B-03). Le noyau n'impose ni objectif, ni algorithme, ni données : il impose les bornes et le juge.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import math
import os
import pathlib
import re
import resource
import shutil
import subprocess
import sys
import threading

import numpy as np

from . import fichiers as _fichiers

PAS_MAX_DEFAUT = 5000
DELAI_S_DEFAUT = 120
MEMOIRE_MO_DEFAUT = 1024
ALGORITHMES = ("sonde-lineaire", "sonde-une-couche")
DIM_SIMULATION = 512
VUE_PAR_DEFAUT = "defaut"  # nom de la vue quand le noyau ne tient qu'un seul fichier de traits


def _heure() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def _empreinte(s: str | bytes) -> str:
    return hashlib.sha256(s.encode("utf-8") if isinstance(s, str) else s).hexdigest()


# ---------------------------------------------------------------- traits ----
def traits_simules(textes: dict[str, str], dim: int = DIM_SIMULATION) -> dict[str, np.ndarray]:
    """Traits de hachage (mots et bigrammes, signe par hachage), normalisés : un double des activations."""
    sortie = {}
    for ident, texte in textes.items():
        v = np.zeros(dim, dtype=np.float32)
        mots = re.findall(r"[a-zà-ÿ0-9]{2,}", texte.lower())
        grammes = mots + [f"{a}_{b}" for a, b in zip(mots, mots[1:])]
        for g in grammes:
            h = hashlib.md5(g.encode("utf-8")).digest()
            v[int.from_bytes(h[:4], "little") % dim] += 1.0 if h[4] % 2 == 0 else -1.0
        n = float(np.linalg.norm(v))
        sortie[ident] = v / n if n > 0 else v
    return sortie


def ecrire_traits(chemin: pathlib.Path, traits: dict[str, np.ndarray]) -> str:
    ids = sorted(traits)
    np.savez(chemin, ids=np.array(ids), X=np.stack([traits[i] for i in ids]).astype(np.float32))
    return _empreinte(chemin.read_bytes())


def normaliser_vues(traits) -> dict[str, dict[str, np.ndarray]]:
    """Vues servies par le noyau (une vue = une couche × une agrégation des activations) : {id: vecteur} (une seule
    vue, `VUE_PAR_DEFAUT`) ou {vue: {id: vecteur}} → {vue: {id: vecteur}}. Une vue vide, ou de dimensions mêlées, est
    refusée (ValueError) : jamais de repli."""
    if not traits:
        return {}
    premier = next(iter(traits.values()))
    vues = {VUE_PAR_DEFAUT: traits} if not isinstance(premier, dict) else traits
    for nom, t in vues.items():
        if not isinstance(nom, str) or not nom or not isinstance(t, dict) or not t:
            raise ValueError(f"vue {nom!r} : dictionnaire non vide attendu")
        dims = {int(np.asarray(x).shape[0]) for x in t.values()}
        if len(dims) != 1:
            raise ValueError(f"vue {nom!r} : dimensions mêlées {sorted(dims)}")
    return vues


def dimensions_vues(vues: dict[str, dict[str, np.ndarray]]) -> dict[str, int]:
    return {nom: int(np.asarray(next(iter(t.values()))).shape[0]) for nom, t in sorted(vues.items())}


# ---------------------------------------------------------- programme ----
# Le programme d'entraînement tourne en sous-processus (python -I -B), sans socket, avec limites ; il ne reçoit que le
# fichier de traits, la spec et les vérités des seules tâches d'entraînement demandées.
PROGRAMME_ENTRAINEMENT = r'''
import json, sys, traceback
import numpy as np

def principal():
    spec = json.load(open("spec.json", encoding="utf-8"))
    don = np.load("donnees.npz")
    X, y = don["X"].astype(np.float64), don["y"].astype(np.float64)
    algo = spec["algorithme"]
    rng = np.random.default_rng(int(algo.get("graine", 0)))
    env = {"np": np}  # le sous-processus est la frontière (bac à sable) ; numpy a besoin des builtins ordinaires
    exec(compile(spec["objectif"], "objectif", "exec"), env)
    perte = env["perte"]
    n, d = X.shape
    if spec.get("pretraitement", {}).get("normaliser", False):
        mu, sd = X.mean(0), X.std(0) + 1e-8
        X = (X - mu) / sd
    else:
        mu, sd = np.zeros(d), np.ones(d)
    pas, taux, l2, lot = int(algo["pas"]), float(algo["taux"]), float(algo.get("l2", 0.0)), int(algo.get("lot", n))
    cache = int(algo.get("cache", 16)) if algo["type"] == "sonde-une-couche" else 0
    if cache:
        W1 = rng.normal(0, 1 / np.sqrt(d), (d, cache)); b1 = np.zeros(cache); w2 = rng.normal(0, 1 / np.sqrt(cache), cache); b2 = 0.0
    else:
        w = np.zeros(d); b = 0.0
    def avant(Xb):
        if cache:
            H = np.tanh(Xb @ W1 + b1); z = H @ w2 + b2; return H, z
        return None, Xb @ w + b
    def sigm(z):
        return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))
    courbe = []
    eps = 1e-4
    for t in range(pas):
        idx = rng.choice(n, size=min(lot, n), replace=False)
        Xb, yb = X[idx], y[idx]
        H, z = avant(Xb)
        p = sigm(z)
        L = float(perte(p, yb))
        if not np.isfinite(L):
            raise ValueError("perte non finie")
        # gradient de la perte par rapport à p : différences finies centrées, coordonnée par coordonnée
        g = np.zeros_like(p)
        for i in range(len(p)):
            pp = p.copy(); pm = p.copy()
            pp[i] = min(1.0, p[i] + eps); pm[i] = max(0.0, p[i] - eps)
            g[i] = (float(perte(pp, yb)) - float(perte(pm, yb))) / (pp[i] - pm[i] + 1e-12)
        dz = g * p * (1 - p)
        if cache:
            gw2 = H.T @ dz / len(idx) + l2 * w2; gb2 = dz.mean()
            dH = np.outer(dz, w2) * (1 - H ** 2)
            gW1 = Xb.T @ dH / len(idx) + l2 * W1; gb1 = dH.mean(0)
            W1 -= taux * gW1; b1 -= taux * gb1; w2 -= taux * gw2; b2 -= taux * gb2
        else:
            gw = Xb.T @ dz / len(idx) + l2 * w; gb = dz.mean()
            w -= taux * gw; b -= taux * gb
        if t % max(1, pas // 50) == 0 or t == pas - 1:
            courbe.append([t, L])
    modele = {"type": algo["type"], "mu": mu.tolist(), "sd": sd.tolist()}
    if cache:
        np.savez("modele.npz", W1=W1, b1=b1, w2=w2, b2=np.array([b2]), mu=mu, sd=sd)
    else:
        np.savez("modele.npz", w=w, b=np.array([b]), mu=mu, sd=sd)
    _, zf = avant(X)
    pf = sigm(zf)
    json.dump({"statut": "OK", "courbe_perte": courbe, "perte_finale_entrainement": float(perte(pf, y)),
               "exactitude_entrainement": float(((pf >= 0.5) == (y >= 0.5)).mean()), "modele": modele}, open("resultat.json", "w", encoding="utf-8"))

try:
    principal()
except BaseException:
    json.dump({"statut": "EXCEPTION", "erreur": traceback.format_exc()[-3000:]}, open("resultat.json", "w", encoding="utf-8"))
'''


def _limites(memoire_mo: int, cpu_s: int):
    def applique():
        try:
            resource.setrlimit(resource.RLIMIT_AS, (memoire_mo << 20, memoire_mo << 20))
        except (ValueError, OSError):
            pass
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_s, cpu_s))
        resource.setrlimit(resource.RLIMIT_FSIZE, (64 << 20, 64 << 20))
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    return applique


def _sigm(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))


def _fini(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def _lire_resultat(bac: pathlib.Path, travail: pathlib.Path, type_sonde: str, d: int) -> tuple[str, str | None, dict | None]:
    """Résultat d'un entraînement, écrit par un sous-processus qui exécute du code de l'organisme : relu comme une donnée
    non fiable. `resultat.json` de la forme attendue (courbe de couples finis, perte et exactitude finies) ; `modele.npz`
    sans objet Python (allow_pickle=False), aux formes de la sonde demandée, nombres finis ; copié dans `travail` (zone du
    noyau) seulement s'il est conforme. Toute anomalie est un statut, jamais un repli."""
    f = bac / "resultat.json"
    donnees, raison = _fichiers.lire_fichier_organisme(f, _fichiers.OCTETS_MAX_RESULTAT)  # R-372 : ni lien suivi, ni tube attendu
    if donnees is None:
        if raison == "absent":
            return "ECHEC_ENTRAINEMENT", "aucun résultat écrit (mémoire ou processeur dépassés ?)", None
        return "ECHEC_ENTRAINEMENT", f"résultat {raison}", None
    try:
        r = json.loads(donnees.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return "ECHEC_ENTRAINEMENT", "résultat illisible", None
    if not isinstance(r, dict) or r.get("statut") != "OK":
        return "ECHEC_ENTRAINEMENT", (str(r.get("erreur"))[-600:] if isinstance(r, dict) else "résultat non conforme"), None
    courbe = r.get("courbe_perte")
    if (not isinstance(courbe, list) or not courbe or len(courbe) > 10000
            or not all(isinstance(c, list) and len(c) == 2 and all(_fini(x) for x in c) for c in courbe)
            or not _fini(r.get("perte_finale_entrainement")) or not _fini(r.get("exactitude_entrainement"))
            or not 0.0 <= float(r["exactitude_entrainement"]) <= 1.0):
        return "ECHEC_ENTRAINEMENT", "résultat non conforme (courbe, perte ou exactitude)", None
    try:
        with _fichiers.ouvrir_fichier_organisme(bac / "modele.npz", _fichiers.OCTETS_MAX_RESULTAT) as fh, np.load(fh, allow_pickle=False) as m:
            tableaux = {k: np.asarray(m[k]) for k in m.files}
    except Exception:
        return "ECHEC_ENTRAINEMENT", "modèle illisible", None
    if type_sonde == "sonde-une-couche":
        W1 = tableaux.get("W1")
        c = W1.shape[1] if W1 is not None and W1.ndim == 2 else -1
        attendu = {"W1": (d, c), "b1": (c,), "w2": (c,), "b2": (1,), "mu": (d,), "sd": (d,)}
    else:
        attendu = {"w": (d,), "b": (1,), "mu": (d,), "sd": (d,)}
    if set(tableaux) != set(attendu) or any(tableaux[k].shape != s for k, s in attendu.items()) \
            or not all(np.all(np.isfinite(tableaux[k])) for k in attendu):
        return "ECHEC_ENTRAINEMENT", "modèle non conforme (formes ou nombres non finis)", None
    if bac != travail:  # seule une copie validée entre dans la zone du noyau ; `predire` ne lit que celle-là
        np.savez(travail / "modele.npz", **{k: tableaux[k].astype(np.float64) for k in attendu})
    return "OK", None, {k: r[k] for k in ("courbe_perte", "perte_finale_entrainement", "exactitude_entrainement")}


class Entraineur:
    """Un entraîneur par génération et par lignée : traits, vérités d'entraînement, bornes, journal, modèles."""

    def __init__(self, dossier: str | pathlib.Path, traits: dict[str, np.ndarray], verites_train: dict[str, float],
                 entrainements_max: int, pas_max: int = PAS_MAX_DEFAUT, delai_s: int = DELAI_S_DEFAUT, memoire_mo: int = MEMOIRE_MO_DEFAUT,
                 prefixe: str = "m", uid: int | None = None, isoler_reseau: bool = False, espace: str | pathlib.Path | None = None):
        """`uid` (CE-02, contre-lecture R2 de l'étape 1) : utilisateur non privilégié sous lequel tourne l'objectif écrit par
        l'organisme, dans un dossier neuf de `espace` qui ne contient que ses entrées, dans des espaces de noms neufs, réseau
        coupé si `isoler_reseau` ; None : même utilisateur que le noyau (simulation sans root seulement). Le filtre
        d'expression régulière de `valider` reste un premier refus, pas une frontière."""
        self.dossier = pathlib.Path(dossier)
        (self.dossier / "modeles").mkdir(parents=True, exist_ok=True)
        self.vues = normaliser_vues(traits)  # {vue: {id: vecteur}} ; un {id: vecteur} seul devient la vue « defaut »
        self.verites_train = dict(verites_train)  # identifiant → 1.0 (étiquette positive) / 0.0
        self.entrainements_max = max(0, int(entrainements_max))
        self.pas_max, self.delai_s, self.memoire_mo = int(pas_max), int(delai_s), int(memoire_mo)
        self.prefixe = prefixe
        self.uid, self.isoler_reseau = uid, bool(isoler_reseau)
        self.espace = pathlib.Path(espace) if espace is not None else None
        if self.uid is not None and self.espace is None:
            raise ValueError("entraîneur isolé sans espace d'exécution")
        self.journal = self.dossier / "journal-entrainements.jsonl"
        self.compteur = 0
        self.modeles: dict[str, dict] = {}
        self._verrou = threading.Lock()

    def _journaliser(self, ligne: dict):
        with self.journal.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n")

    # ---- validation de la spécification ----
    def vue_de(self, spec) -> str | None:
        """Vue désignée par `spec["vue"]` ; sans désignation, la seule vue servie ; sinon None (refus)."""
        vue = spec.get("vue") if isinstance(spec, dict) else None
        if vue is None and len(self.vues) == 1:
            return next(iter(self.vues))
        return vue if isinstance(vue, str) and vue in self.vues else None

    def valider(self, spec) -> list[str]:
        p = []
        if not isinstance(spec, dict):
            return ["spec : objet attendu"]
        vue = self.vue_de(spec)
        if vue is None:
            p.append(f"vue : {str(spec.get('vue'))[:60]!r} non servie ; vues servies : {sorted(self.vues)}")
        don = spec.get("donnees")
        if not isinstance(don, list) or not don or not all(isinstance(i, str) for i in don):
            p.append("donnees : liste non vide d'identifiants de tâches d'entraînement attendue")
        else:
            hors = [i for i in don if i not in self.verites_train]
            if hors:
                p.append(f"donnees : {len(hors)} identifiant(s) hors des tâches d'entraînement (les tâches de test ne s'entraînent pas) : {hors[:3]}")
            manquants = [i for i in don if i in self.verites_train and vue is not None and i not in self.vues[vue]]
            if manquants:
                p.append(f"donnees : traits absents pour {len(manquants)} tâche(s) : {manquants[:3]}")
            if len(set(don)) != len(don):
                p.append("donnees : identifiants en double")
        obj = spec.get("objectif")
        if not isinstance(obj, str) or "def perte(" not in obj or len(obj) > 20000:
            p.append("objectif : code Python définissant `def perte(p, y)` attendu (≤ 20 000 caractères)")
        else:
            try:
                compile(obj, "objectif", "exec")
            except SyntaxError as e:
                p.append(f"objectif : syntaxe : {str(e)[:100]}")
            if re.search(r"\b(import|open|exec|eval|__import__|os\.|sys\.|subprocess|socket)\b", obj):
                p.append("objectif : import, ouverture de fichier, exec/eval ou accès système interdits (numpy est fourni comme `np`)")
        algo = spec.get("algorithme")
        if not isinstance(algo, dict) or algo.get("type") not in ALGORITHMES:
            p.append(f"algorithme : type parmi {ALGORITHMES} attendu")
        else:
            try:
                pas = int(algo.get("pas", 0)); taux = float(algo.get("taux", 0))
                if not (1 <= pas <= self.pas_max):
                    p.append(f"algorithme : pas entre 1 et {self.pas_max}")
                if not (0 < taux <= 10):
                    p.append("algorithme : taux dans ]0, 10]")
                if "cache" in algo and not (1 <= int(algo["cache"]) <= 256):
                    p.append("algorithme : cache entre 1 et 256")
                if "lot" in algo and int(algo["lot"]) < 1:
                    p.append("algorithme : lot ≥ 1")
            except (TypeError, ValueError):
                p.append("algorithme : pas, taux, cache, lot numériques")
        return p

    # ---- entraînement ----
    def entrainer(self, spec, role: str = "") -> dict:
        problemes = self.valider(spec)
        if problemes:
            self._journaliser({"id": None, "role": role, "statut": "REFUSE", "problemes": problemes, "quand_utc": _heure()})
            return {"statut": "REFUSE", "identifiant": None, "problemes": problemes}
        with self._verrou:
            if self.compteur >= self.entrainements_max:
                self._journaliser({"id": None, "role": role, "statut": "PLAFOND", "quand_utc": _heure()})
                return {"statut": "PLAFOND", "identifiant": None, "problemes": [f"plafond de {self.entrainements_max} entraînements atteint"]}
            self.compteur += 1
            num = self.compteur
        ident = f"LOCAL:{self.prefixe}-{num:04d}"
        travail = self.dossier / "modeles" / f"{self.prefixe}-{num:04d}"
        travail.mkdir(parents=True, exist_ok=True)
        ids = list(spec["donnees"])
        vue = self.vue_de(spec)
        X = np.stack([self.vues[vue][i] for i in ids]).astype(np.float32)
        y = np.array([self.verites_train[i] for i in ids], dtype=np.float32)
        # CE-02 : avec un uid, l'objectif tourne hors de la zone du noyau, dans un dossier neuf qui ne contient que ses
        # entrées (données d'entraînement demandées, spec, programme), sous un utilisateur non privilégié distinct des
        # organismes ; `travail` (zone du noyau) reçoit ensuite une copie des pièces et le modèle validé.
        bac = (self.espace / "entrainements" / f"{self.prefixe}-{num:04d}") if self.uid is not None else travail
        if self.uid is not None:
            from . import bac_a_sable as _bac
            (self.espace / "entrainements").mkdir(parents=True, exist_ok=True)
            _bac.proteger(self.espace / "entrainements", 0o711)
            if bac.exists():
                shutil.rmtree(bac)
            bac.mkdir()
        np.savez(bac / "donnees.npz", X=X, y=y)
        (bac / "spec.json").write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")
        (bac / "programme.py").write_text(PROGRAMME_ENTRAINEMENT, encoding="utf-8")
        env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "HOME": str(bac), "TMPDIR": str(bac),
               "OMP_NUM_THREADS": "2", "OPENBLAS_NUM_THREADS": "2"}
        debut = _heure()
        statut, erreur, resultat = "OK", None, None
        if self.uid is not None:
            _bac._changer_proprietaire(bac, self.uid, self.uid)
            try:  # le programme du noyau reste à root, lisible, non modifiable par l'utilisateur de l'entraîneur
                os.chown(bac / "programme.py", 0, 0)
                os.chmod(bac / "programme.py", 0o644)
            except OSError:
                pass
            if self.isoler_reseau and not _bac.isolation_reseau_disponible():
                statut, erreur = "ECHEC_ENTRAINEMENT", "isolation réseau indisponible : entraînement refusé"
            commande = _bac._commande_isolee([sys.executable, "-I", "-B", "-s", "programme.py"], self.isoler_reseau, self.uid, bac)
            if statut == "OK":
                with (travail / "sortie.txt").open("w") as so, (travail / "erreurs.txt").open("w") as se:
                    _, delai = _bac._lancer(commande, bac, env, self.delai_s, so, se,
                                            _bac._limites(self.memoire_mo, self.delai_s, 64, self.uid, self.uid))
                if delai:
                    statut, erreur = "DELAI_DEPASSE", f"plus de {self.delai_s} s"
        else:
            try:
                with (travail / "sortie.txt").open("w") as so, (travail / "erreurs.txt").open("w") as se:
                    subprocess.run([sys.executable, "-I", "-B", "-s", "programme.py"], cwd=str(travail), env=env, stdout=so, stderr=se,
                                   timeout=self.delai_s, preexec_fn=_limites(self.memoire_mo, self.delai_s))
            except subprocess.TimeoutExpired:
                statut, erreur = "DELAI_DEPASSE", f"plus de {self.delai_s} s"
        if statut == "OK":
            statut, erreur, resultat = _lire_resultat(bac, travail, spec["algorithme"]["type"], X.shape[1])
        if self.uid is not None:
            for nom in ("spec.json", "programme.py"):  # le bac appartient à l'utilisateur de l'entraîneur : lecture sans lien (R-372)
                donnees_copie, _ = _fichiers.lire_fichier_organisme(bac / nom, _fichiers.OCTETS_MAX_RESULTAT)
                if donnees_copie is not None and not (travail / nom).exists():
                    (travail / nom).write_bytes(donnees_copie)
            shutil.rmtree(bac, ignore_errors=True)
        fin = _heure()
        sortie = {"statut": statut, "identifiant": (ident if statut == "OK" else None), "echec": erreur, "n_donnees": len(ids), "vue": vue,
                  "courbe_perte": (resultat or {}).get("courbe_perte"), "perte_finale_entrainement": (resultat or {}).get("perte_finale_entrainement"),
                  "exactitude_entrainement": (resultat or {}).get("exactitude_entrainement"), "cout_usd": 0.0}
        if statut == "OK":
            self.modeles[ident] = {"chemin": travail / "modele.npz", "type": spec["algorithme"]["type"], "vue": vue}
        self._journaliser({"id": ident, "role": str(role)[:40], "statut": statut, "echec": erreur, "n_donnees": len(ids), "vue": vue,
                           "sha256_spec": _empreinte(json.dumps(spec, sort_keys=True, ensure_ascii=False)), "sha256_objectif": _empreinte(spec["objectif"]),
                           "algorithme": spec["algorithme"], "debut_utc": debut, "fin_utc": fin,
                           "exactitude_entrainement": sortie["exactitude_entrainement"]})
        return sortie

    # ---- prédiction ----
    def predire(self, identifiant, ids, role: str = "") -> dict:
        if identifiant not in self.modeles:
            return {"statut": "ANOMALIE", "probabilites": {}, "echec": f"modèle inconnu : {identifiant!r}"}
        if not isinstance(ids, list) or not ids or not all(isinstance(i, str) for i in ids):
            return {"statut": "ANOMALIE", "probabilites": {}, "echec": "liste d'identifiants attendue"}
        m = np.load(self.modeles[identifiant]["chemin"])
        traits = self.vues[self.modeles[identifiant]["vue"]]  # la vue sur laquelle le modèle a appris
        probabilites, absents = {}, []
        for i in ids:
            if i not in traits:
                absents.append(i)
                continue
            x = (traits[i].astype(np.float64) - m["mu"]) / m["sd"]
            if self.modeles[identifiant]["type"] == "sonde-une-couche":
                z = np.tanh(x @ m["W1"] + m["b1"]) @ m["w2"] + float(m["b2"][0])
            else:
                z = float(x @ m["w"] + m["b"][0])
            probabilites[i] = round(float(_sigm(z)), 6)
        self._journaliser({"id": identifiant, "role": str(role)[:40], "statut": "OK", "op": "predire", "n": len(ids), "absents": len(absents), "quand_utc": _heure()})
        return {"statut": "OK", "probabilites": probabilites, "absents": absents}

    def lire_journal(self) -> list[dict]:
        if not self.journal.exists():
            return []
        return [json.loads(l) for l in self.journal.read_text(encoding="utf-8").splitlines() if l.strip()]
