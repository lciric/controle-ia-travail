"""Poussée de chaque lot dès qu'il est scellé, organisme retenu du saboteur à budget, v5 (correctif 0014).

EXPLORATOIRE, NON OPPOSABLE (R-522). L'ordre de l'étalonnage (§§ 4 et 7) exige qu'après chaque lot les sorties d'oracle
(`diag/<run>/lots/lot-*.json`) et les identifiants (`donnees/<run>/lots/ids-lot-*.json`) soient scellés **et poussés**. Avant ce
correctif, le lanceur scellait sur le disque et l'amorce ne poussait qu'à la fin du run, sur un arrêt, à la minuterie ou à un
second démarrage : la branche d'essai restait au commit de lancement pendant tout l'étalonnage.

Seul module v5 qui lance un sous-processus (garde statique de `tests/test_iib_lanceur_v5.py`) : `git` en lecture seule
(`ls-files`, `status`, `rev-parse`) et le script de consignation de l'amorce (`bash IIB_CONSIGNER "versement …"`), rien d'autre ;
aucune suppression, aucun arrêt de machine (c'est l'amorce qui arrête, par l'identifiant). Un délai dépassé arrête le groupe du
script par son identifiant de groupe (R10).
"""
from __future__ import annotations

import time
from pathlib import Path

from ..gardes import GardeArret

CONSIGNER = "IIB_CONSIGNER"          # chemin du script de consignation écrit par l'amorce (`$R/iib-consigner.sh`)
REFUS_CONSECUTIFS_MAX = 3            # trois poussées refusées de suite : arrêt (lots scellés sur le disque, machine arrêtée par l'amorce)
DELAI_CONSIGNATION_S = 3600          # verrou (1 500 s) et trois poussées (600 s chacune) et leurs attentes (15 + 60 s) : 3 375 s au pire (cl1, m2)


class Versement:
    """Après chaque lot écrit et scellé, le script de consignation de l'amorce (`IIB_CONSIGNER`, motif « versement … ») committe
    et pousse ; puis le lanceur **vérifie lui-même** que les fichiers du lot sont suivis, propres, et que la tête locale est
    celle de la branche distante (une poussée dite faite sans l'être est vue). Chaque issue est une marque de progrès
    (`etape=versement`, `poussee=faite` ou `poussee=refusee`, motif court) : jamais avalée. Trois refus de suite : `GardeArret`
    (le lanceur écrit `arret.json`, l'amorce consigne une dernière fois et arrête la machine par son identifiant, disque gardé),
    parce qu'au-delà, chaque lot de plus est une perte possible et non versée. Un refus isolé ne coûte rien : le lot reste scellé
    sur le disque, et la consignation suivante pousse tout ce qui n'est pas encore sur la branche.
    Mode réel : le script est exigé (refus avant tout calcul) ; mode jouet sans script : rien n'est poussé, et c'est écrit."""

    def __init__(self, racine, environnement: dict, mode: str, progres=None):
        script = (environnement or {}).get(CONSIGNER) or None
        if mode == "reel" and not script:
            raise GardeArret(f"mode réel sans {CONSIGNER} : aucun lot ne serait poussé au fil du run (ordre, §§ 4 et 7) : refus avant tout calcul")
        if script is not None and not Path(script).is_file():
            raise GardeArret(f"{CONSIGNER}={script} : script de consignation absent du disque (refus)")
        self.racine, self.script = Path(racine), None if script is None else Path(script)
        self.refus_consecutifs, self.journal = 0, []
        self._progres = progres if progres is not None else marque

    def _git(self, *args) -> tuple[int, str]:
        import subprocess

        r = subprocess.run(["git", "-C", str(self.racine), *args], capture_output=True, text=True, timeout=120)
        return r.returncode, (r.stdout + r.stderr).strip()

    def verifier_sur_la_branche(self, fichiers: list) -> str | None:
        """None si chaque fichier est suivi et propre et si la tête locale est celle de la branche distante ; sinon le motif."""
        import os

        rel = [os.path.relpath(Path(f), self.racine) for f in fichiers]
        code, sortie = self._git("ls-files", "--error-unmatch", "--", *rel)
        if code != 0:
            return "fichier_non_suivi"
        code, sortie = self._git("status", "--porcelain", "--ignored", "--", *rel)
        if code != 0 or sortie:
            return "fichier_non_consigne"
        code, branche = self._git("rev-parse", "--abbrev-ref", "HEAD")
        if code != 0 or not branche or branche == "HEAD":
            return "branche_illisible"
        c1, tete = self._git("rev-parse", "HEAD")
        c2, distante = self._git("rev-parse", "--verify", "-q", f"refs/remotes/origin/{branche}")
        if c1 != 0 or c2 != 0 or tete != distante:
            return "tete_non_poussee"
        return None

    def __call__(self, motif: str, fichiers: list) -> dict:
        import os
        import signal
        import subprocess

        n = len(self.journal) + 1
        if self.script is None:
            e = {"versement": n, "motif": motif, "poussee": "sans_script"}
            self.journal.append(e)
            self._progres(etape="versement", numero=n, poussee="sans_script")
            return e
        t0 = time.time()
        proc = subprocess.Popen(["bash", str(self.script), f"versement {motif}"], cwd=self.racine, stdin=subprocess.DEVNULL,
                                stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True, start_new_session=True)
        try:
            _, err = proc.communicate(timeout=DELAI_CONSIGNATION_S)
            code = proc.returncode
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)              # groupe du script, par son identifiant (R10), jamais par motif
            _, err = proc.communicate()
            code = "delai"
        cause = f"script_code_{code}" if code != 0 else self.verifier_sur_la_branche(fichiers)
        e = {"versement": n, "motif": motif, "fichiers": len(fichiers), "code": code, "duree_s": round(time.time() - t0, 1),
             "poussee": "faite" if cause is None else "refusee", "cause": cause}
        self.journal.append(e)
        if cause is None:
            self.refus_consecutifs = 0
            self._progres(etape="versement", numero=n, poussee="faite", duree_s=e["duree_s"])
            return e
        self.refus_consecutifs += 1
        self._progres(etape="versement", numero=n, poussee="refusee", cause=cause, refus_de_suite=self.refus_consecutifs)
        import sys

        print(f"VERSEMENT REFUSÉ ({motif}) : {cause} ; {(err or '').strip()[-300:]}", file=sys.stderr, flush=True)
        if self.refus_consecutifs >= REFUS_CONSECUTIFS_MAX:
            raise GardeArret(f"poussée par lot refusée {self.refus_consecutifs} fois de suite (dernière : {motif}, {cause}) : arrêt ; "
                             "les lots restent scellés sur le disque de la machine")
        return e


def marque(**champs) -> None:
    """Marque de progrès, même forme que `lanceur_v5.progres` (utilisée si l'appelant n'en passe aucune)."""
    import sys
    from datetime import datetime, timezone

    instant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("PROGRES " + instant + " " + " ".join(f"{k}={str(v).replace(' ', '_')}" for k, v in champs.items()), file=sys.stderr, flush=True)
