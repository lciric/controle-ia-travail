"""Épreuve sur la machine — essai Lean (D-1a), v8 (contre-lecture Fable 5.2 des corrections du troisième essai,
`contre-lecture-corrections-essai-3-v1.md`, 59b0ec03… ; GO-2026-11-21-40).

Copie de `epreuve_isolement_v7.py` (inchangée, R12) ; exécuteur v8 ; attendus `artefacts_r5_v4/attendus-v7.json`. Changements :
1. **B1** : le cas Lean de la limite de mémoire se juge sur la **seule compilation** : résultat systemd de la compilation
   (`oom-kill` attendu) et son classement (`incident_compilation`, « mémoire » attendu), compilation en échec, sans sa ligne
   témoin. La v7 lisait `incident_bac` (« compilation, ou à défaut vérificateur ») : une compilation en échec d'elle-même,
   suivie d'un vérificateur tué par la mémoire, passait. Un incident déclaré par `incident_compilation_attendu` est admis
   par `_noter` comme un incident attendu.
2. **Signal d'un chemin de cgroupe faux** (`signal_memoire`) : une unité qui a tourné au moins 1 s sans aucun relevé de
   `memory.peak` dit que le chemin est faux ; aucun pic n'est alors rapporté. Sinon, un pic n'est rapporté que sur au moins
   trois relevés. Bloc `memoire` dans la sortie de l'épreuve et de `mesurer` ; aucun « conforme » n'en dépend.
3. **Mémoire de la machine entière pour trois passages en parallèle** (`mesurer`) : les trois passages tournent dans une
   tranche réservée de nom neuf (`bacmesure<8 hexadécimaux>.slice`) ; pendant le bloc, toutes les 0,1 s, `memory.peak` de la
   tranche (le plus-haut de la somme simultanée, tenu par le noyau) et `MemAvailable` de `/proc/meminfo`, avant, pendant et
   après. Critères écrits d'avance (`juger_parallele`) ; `parallele_3_compte` faux au moindre manquement.
4. Témoin sain obligatoire (recommandation R2) : l'épreuve s'arrête avant tout item si les groupes `isolement_lean` ou
   `python` des attendus n'ont aucun cas marqué `sain` ; le cas Lean de la limite de mémoire porte dans le JSON ses deux
   incidents (`incident_compilation`, `incident_noyau`), pour une lecture sur la compilation.

Texte de la v7 : Épreuve sur la machine — essai Lean (D-1a), v7 (troisième essai, arbitrage Fable 5.2 point 7, pas 3 à 5 ; GO-2026-11-21-40).

Copie de `epreuve_isolement_v6.py` (inchangée, R12) ; exécuteur v7 ; attendus `artefacts_r5_v4/attendus-v6.json`.
Cause des cinq « non conforme » de l'isolement Lean au troisième essai, établie hors machine contre la chaîne épinglée
(`scripts/lean_essai_d1a_v11/compiler_comme_bac_v1.sh`) : sous Lean 4.35.0, `String.take` rend une `String.Slice` ; la
fonction `tenter` commune aux cinq items sondes v2 ne s'élaborait pas (« Application type mismatch … r.take 120 has type
String.Slice but is expected to have type String »), chaque `#eval` était abandonné (« depends on the 'sorry' axiom ») :
aucune tentative, code 1, en 0,4 s (fichiers sans Mathlib). Changements :
1. items sondes v3 (`.take k` suivi de `.toString`) ;
2. la sortie de compilation des items sondes (isolement Lean, limites Lean) entre dans le JSON, bornée
   (`EXTRAIT_SONDE` caractères de la sortie standard, `EXTRAIT_ERREURS` de la sortie d'erreur), avec le code de compilation ;
   un cas sonde sans aucune ligne « ISOLEMENT » est marqué `sonde_muette` ;
3. **épreuve morte** : un genre dont le cas marqué `sain` ne rend pas toutes ses tentatives attendues sort
   « épreuve morte », distinct de « non conforme » ; l'épreuve entière sort alors « épreuve morte » (jamais « conforme ») ;
4. `echecs_invalides` : un ECHEC dont le détail porte un de ces motifs (processus non lancé) est un écart ;
5. groupe `limites_lean` : un item Lean qui dépasse sa limite de mémoire doit sortir « mémoire », compilation en échec,
   sans sa ligne témoin.

Texte de la v6 : Épreuve sur la machine — essai Lean (D-1a), v6 (R-2464, sous R-2439).

Copie de `epreuve_isolement_v5.py` (inchangée, R12) ; changements : exécuteur v6 et `verificateur_noyau_v6.lean` ; attendus
`artefacts_r5_v4/attendus-v5.json` (le cas du simproc hors noyau joue `noyau_simproc_hors_noyau_v5.lean`).

Texte de la v5 : Épreuve sur la machine — essai Lean (D-1a), v5 (réparation R-2439).

Copie de `epreuve_isolement_v4.py` (inchangée, R12) dont **seuls l'exécuteur et le vérificateur changent** :
`executeur_bac_v5` et `/opt/harnais/noyau/verificateur_noyau_v5.lean` (portage vers Lean 4.35.0) ; nom de version. Mêmes
pas, mêmes jugements, mêmes artefacts (`artefacts_r5_v4/attendus-v4.json`).

Texte de la v4 : Épreuve sur la machine — essai Lean (D-1a), v4 (contre-lecture courte de la v3 `b6ca886d…`, décision R-2307).

Même déroulé que la v3 (`epreuve_isolement_v3.py`, inchangée, R12) : `epingler-verificateur`, puis le **premier pas `noyau`**,
puis `epreuve`, puis `mesurer` ; exécuteur et vérificateur v4, artefacts `artefacts_r5_v4/attendus-v4.json`.

CLC3-04, le premier pas devient discriminant :
- chaque item du groupe `noyau` exige G-L1 et G-L7 (compilation réussie, `.olean` présent, vérificateur allé au bout) ;
- un item qui doit être pris par le rejeu exige une **ligne de rejeu présente**, `ok: false`, dont l'erreur **nomme la constante
  fautive** (`constante_fautive` de l'attendu) ;
- le groupe est **rejoué sans G-L3+** (attendus `sans_suppl`) : G-L8 et G-L5 doivent prendre chaque item seuls ;
- le pas n'est conforme que si les deux passages le sont.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import secrets
import subprocess
import sys
import threading
import time
from dataclasses import replace
from pathlib import Path

if __package__:
    from . import executeur_bac_v8 as X
else:
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import executeur_bac_v8 as X  # noqa: E402

VERSION = "epreuve_isolement_v8"
ATTENDUS = "attendus-v7.json"
# v8 : mesure de la mémoire ; critères écrits d'avance (procédure du poste local v12, section 8)
TRANCHE_MESURE = "bacmesure{}.slice"        # tranche réservée, nom neuf par passage
DUREE_MIN_RELEVE_S = 1.0                    # une unité qui a tourné au moins 1 s a dû être relevée (période 0,1 s)
ECHANTILLONS_MIN = 3                        # un pic relevé sur moins de trois relevés n'est pas rapporté
SEUIL_PIC_TRANCHE = 0.5                     # pic de la tranche : au plus la moitié de la mémoire de la machine
SEUIL_DISPO_MIN = 0.25                      # mémoire disponible au plus bas, estimée prudemment : au moins le quart
TOLERANCE_RECOUPEMENT_OCTETS = 1 << 30      # baisse de MemAvailable : au plus le pic de la tranche plus 1 Gio
EXTRAIT_SONDE = 4000
EXTRAIT_ERREURS = 1000
LEURRE = Path("/srv/leurre/leurre-v1.txt")
RACINES_MANIFESTE = ("/opt/elan", "/opt/mathlib", "/opt/pybac", "/opt/harnais")
PIEGES_HOTE = ("/opt/mathlib/Piege-v1.txt", "/opt/mathlib/.lake/build/lib/lean/Piege.olean", "/opt/elan/Piege-v1.txt",
               "/usr/Piege-v1.txt", "/opt/harnais/Piege-v1.txt", "/srv/controle/piege.lean", "/tmp/persistance-v1.txt",
               "/tmp/persistance-py-v1.txt")
# v7 : le détail court jusqu'à la fin de la ligne, réelle (Python) ou échappée dans le JSON de Lean (« \\n ») ou au guillemet.
RE_TENTATIVE = re.compile(r'ISOLEMENT (\S+) (ECHEC|REUSSI)((?:(?!\\n)[^\n"])*)')
LIMITES_ESSAI = {"memoire_max": "512M", "taches_max": 32, "cpu_max_s": 5, "duree_max_s": 10}
VERIFICATEUR = Path("/opt/harnais/noyau/verificateur_noyau_v6.lean")


def manifeste(racines=RACINES_MANIFESTE) -> str:
    h = hashlib.sha256()
    for racine in racines:
        for dossier, sous, fichiers in os.walk(racine, followlinks=False):
            sous.sort()
            for nom in sorted(fichiers) + sorted(sous):
                p = os.path.join(dossier, nom)
                st = os.lstat(p)
                h.update(f"{p}\0{st.st_size}\0{st.st_mtime_ns}\0{st.st_mode}\n".encode("utf-8", "surrogateescape"))
    return h.hexdigest()


def tentatives(texte: str) -> dict[str, str]:
    return {m.group(1): m.group(2) for m in RE_TENTATIVE.finditer(texte)}


def details_tentatives(texte: str) -> dict[str, str]:
    return {m.group(1): m.group(3).strip() for m in RE_TENTATIVE.finditer(texte)}


def juger_lean(cas: dict, res: dict) -> list[str]:
    v = res["verdict"]
    ecarts = []
    if v["accepte_gardes"] != cas["accepte"]:
        ecarts.append(f"accepte_gardes {v['accepte_gardes']} ≠ {cas['accepte']} ; motifs "
                      f"{ {g: x['motifs'][:3] for g, x in v['gardes'].items() if x['motifs']} }")
    for g in cas.get("echecs", []):
        if v["gardes"][g]["ok"]:
            ecarts.append(f"{g} devait échouer")
    for g in cas.get("passent", []):
        if not v["gardes"][g]["ok"]:
            ecarts.append(f"{g} devait passer : {v['gardes'][g]['motifs'][:3]}")
    if "rejeu" in cas and v["rejeu_ok"] is not cas["rejeu"]:
        ecarts.append(f"rejeu {v['rejeu_ok']}, {cas['rejeu']} attendu")
    for nom, morceaux in cas.get("enonce_contient", {}).items():
        texte = v["enonces_imprimes"].get(nom, "")
        ecarts += [f"énoncé de {nom} sans « {x} » : {texte!r}" for x in morceaux if x not in texte]
    for nom, morceaux in cas.get("impression_contient", {}).items():
        texte = v["impressions"].get(nom, "")
        ecarts += [f"impression de {nom} sans « {x} » : {texte!r}" for x in morceaux if x not in texte]
    for nom, axiomes in cas.get("axiomes_contient", {}).items():
        lus = v["axiomes"].get(nom) or []
        ecarts += [f"axiomes de {nom} sans {a} : {lus}" for a in axiomes if a not in lus]
    for x in cas.get("sortie_agent_contient", []):
        if x not in res["sortie_compilation"]:
            ecarts.append(f"sortie de l'agent sans « {x} »")
    return ecarts


def juger_noyau(cas: dict, res: dict) -> list[str]:
    """CLC3-04 : G-L1 et G-L7 exigés pour tout item du premier pas ; rejeu attendu en échec ⇒ ligne présente qui nomme la
    constante fautive."""
    v = res["verdict"]
    ecarts = juger_lean(cas, res)
    for g in ("G-L1", "G-L7"):
        if not v["gardes"][g]["ok"] and g not in cas.get("echecs", []):
            ecarts.append(f"{g} devait passer (premier pas) : {v['gardes'][g]['motifs'][:3]}")
    if cas.get("rejeu") is False:
        if not v.get("rejeu_present"):
            ecarts.append("aucune ligne de rejeu : le rejeu n'a pas été tenté")
        elif cas.get("constante_fautive", "\0") not in str(v.get("rejeu_erreur", "")):
            ecarts.append(f"l'erreur de rejeu ne nomme pas {cas.get('constante_fautive')!r} : {v.get('rejeu_erreur')!r}")
    return ecarts


def observer(cas: dict, res: dict) -> dict:
    """Relevé sans jugement : gardes et traces de la compilation (comportement de Lean à établir)."""
    v = res["verdict"]["gardes"]
    obs = {g: {"ok": v[g]["ok"], "motifs": v[g]["motifs"][:5]} for g in cas.get("observer", [])}
    for x in cas.get("observer_sortie", []):
        obs[f"sortie contient « {x} »"] = x in res["sortie_compilation"]
    return obs


def juger_tentatives(cas: dict, texte: str) -> list[str]:
    vues = tentatives(texte)
    ecarts = [f"tentative {nom} : {vues.get(nom, 'absente')}, {attendu} attendu"
              for nom, attendu in cas["tentatives"].items() if vues.get(nom) != attendu]
    details = details_tentatives(texte)
    for nom in cas["tentatives"]:
        if vues.get(nom) == "ECHEC":
            ecarts += [f"tentative {nom} : ECHEC sans valeur de preuve (« {m} ») : {details.get(nom, '')[:200]!r}"
                       for m in cas.get("echecs_invalides", []) if m in details.get(nom, "")]
    return ecarts


def sain_vivant(cas: dict, texte: str) -> bool:
    """Le cas sain d'un genre rend-il toutes ses tentatives, avec l'issue attendue ?"""
    vues = tentatives(texte)
    return all(vues.get(nom) == attendu for nom, attendu in cas["tentatives"].items())


def extrait_sonde(res: dict) -> dict:
    """v7 : sortie de compilation d'un item sonde, bornée, pour le JSON."""
    so = res.get("sortie_compilation", "")
    se = res.get("erreurs_compilation", "")
    return {"code_compilation": (res.get("compilation") or {}).get("code"),
            "sortie_compilation_extrait": so[:EXTRAIT_SONDE], "sortie_compilation_tronquee": len(so) > EXTRAIT_SONDE,
            "erreurs_compilation_extrait": se[:EXTRAIT_ERREURS], "erreurs_compilation_tronquees": len(se) > EXTRAIT_ERREURS,
            "sonde_muette": not RE_TENTATIVE.search(so)}


def juger_limite_lean(cas: dict, res: dict) -> list[str]:
    """v8, B1 : jugé sur la seule compilation ; l'incident du vérificateur, qui suit sous les mêmes limites, ne compte pas."""
    ecarts = []
    compil = res.get("compilation") or {}
    if compil.get("resultat") != cas["resultat_compilation_attendu"]:
        ecarts.append(f"compilation : résultat systemd {compil.get('resultat')!r}, "
                      f"{cas['resultat_compilation_attendu']!r} attendu")
    if res.get("incident_compilation") != cas["incident_compilation_attendu"]:
        ecarts.append(f"compilation : incident {res.get('incident_compilation')!r}, "
                      f"{cas['incident_compilation_attendu']!r} attendu")
    if cas.get("compilation_code_non_nul") and compil.get("code") == 0:
        ecarts.append("compilation en code 0, arrêt par le bac attendu")
    ecarts += [f"sortie de compilation avec « {x} »" for x in cas.get("sortie_absent", [])
               if x in res.get("sortie_compilation", "")]
    return ecarts


def signal_memoire(lancements: list) -> dict:
    """v8 : `lancements` = [(nom, temps)], `temps` portant `duree_service_s`, `memoire_echantillons` et
    `memoire_pic_echantillonne_octets`. Une unité isolée qui a tourné au moins DUREE_MIN_RELEVE_S sans aucun relevé dit que le
    chemin du cgroupe est faux : aucun pic n'est alors rapporté. Sinon, pic rapporté sur au moins ECHANTILLONS_MIN relevés."""
    sans, pics = [], {}
    for nom, t in lancements:
        if not t or not t.get("isolement"):
            continue
        n = t.get("memoire_echantillons") or 0
        if (t.get("duree_service_s") or 0) >= DUREE_MIN_RELEVE_S and n == 0:
            sans.append(nom)
        pics[nom] = t.get("memoire_pic_echantillonne_octets") if n >= ECHANTILLONS_MIN else None
    return {"chemin_cgroupe_faux": bool(sans), "lancements_sans_releve": sans,
            "pics_rapportes_octets": {} if sans else pics}


def lire_meminfo(chemin: Path = Path("/proc/meminfo")) -> dict[str, int]:
    """`/proc/meminfo` en octets (les valeurs en kB multipliées par 1024)."""
    d = {}
    for ligne in chemin.read_text().splitlines():
        cle, _, reste = ligne.partition(":")
        morceaux = reste.split()
        if morceaux and morceaux[0].isdigit():
            d[cle.strip()] = int(morceaux[0]) * (1024 if morceaux[1:2] == ["kB"] else 1)
    return d


class ReleveMachine:
    """v8 : pendant un bloc `with`, un fil relève toutes les `periode` secondes le `memory.peak` de la tranche réservée et
    `MemAvailable` ; `MemTotal` et `MemAvailable` sont lus aussi avant et après. Toute lecture en échec compte « aucun
    relevé » ; le plus-haut relevé de la tranche est un minorant de son pic (seul est perdu ce qui monte après le dernier
    relevé : `memory.peak` est un plus-haut tenu par le noyau)."""

    def __init__(self, chemin_tranche: Path, meminfo: Path = Path("/proc/meminfo"), periode: float | None = None):
        self.chemin, self.meminfo = chemin_tranche, meminfo
        self.periode = X.PERIODE_ECHANTILLON_S if periode is None else periode
        self.pic, self.n_pic, self.dispo_min, self.n_dispo = None, 0, None, 0
        self.avant, self.apres = {}, {}
        self._arret = threading.Event()
        self._fil = threading.Thread(target=self._boucle, daemon=True)

    def _meminfo(self) -> dict[str, int]:
        try:
            return lire_meminfo(self.meminfo)
        except (OSError, ValueError):
            return {}

    def _un(self) -> None:
        v = X.relever_memoire_pic(self.chemin)
        if v is not None:
            self.pic, self.n_pic = (v if self.pic is None else max(self.pic, v)), self.n_pic + 1
        dispo = self._meminfo().get("MemAvailable")
        if dispo is not None:
            self.dispo_min, self.n_dispo = (dispo if self.dispo_min is None else min(self.dispo_min, dispo)), self.n_dispo + 1

    def _boucle(self) -> None:
        while not self._arret.is_set():
            self._un()
            self._arret.wait(self.periode)
        self._un()

    def __enter__(self):
        self.avant = self._meminfo()
        self._fil.start()
        return self

    def __exit__(self, *exc) -> bool:
        self._arret.set()
        self._fil.join()
        self.apres = self._meminfo()
        return False

    def resultat(self) -> dict:
        return {"chemin_tranche": str(self.chemin), "periode_s": self.periode,
                "memoire_totale_octets": self.avant.get("MemTotal"), "dispo_avant_octets": self.avant.get("MemAvailable"),
                "dispo_min_octets": self.dispo_min, "dispo_echantillons": self.n_dispo,
                "dispo_apres_octets": self.apres.get("MemAvailable"),
                "pic_tranche_octets": self.pic, "pic_tranche_echantillons": self.n_pic}


def juger_parallele(parallele: list, m: dict, signal: dict) -> dict:
    """v8 : critères écrits d'avance pour compter un passage à trois processus en parallèle (procédure v12, section 8)."""
    motifs, calcul = [], {}
    for i, p in enumerate(parallele):
        if not p.get("accepte"):
            motifs.append(f"passage parallèle {i} : item sain refusé")
        if p.get("incident_bac"):
            motifs.append(f"passage parallèle {i} : incident {p['incident_bac']!r}")
    if signal.get("chemin_cgroupe_faux"):
        motifs.append("chemin du cgroupe faux (unités sans relevé) : aucune mesure de mémoire n'est retenue")
    total, avant, pic = m.get("memoire_totale_octets"), m.get("dispo_avant_octets"), m.get("pic_tranche_octets")
    if pic is None or m.get("pic_tranche_echantillons", 0) < ECHANTILLONS_MIN:
        motifs.append(f"mesure de la tranche absente ({m.get('pic_tranche_echantillons', 0)} relevé(s), "
                      f"{ECHANTILLONS_MIN} exigés) : chemin de la tranche faux ou passage trop court")
        pic = None
    if not total or avant is None or m.get("dispo_min_octets") is None or m.get("dispo_echantillons", 0) < ECHANTILLONS_MIN:
        motifs.append("mémoire de la machine non relevée (/proc/meminfo)")
    elif pic is not None:
        baisse = avant - m["dispo_min_octets"]
        prudente = avant - max(baisse, pic)
        calcul = {"baisse_dispo_octets": baisse, "dispo_min_prudente_octets": prudente,
                  "seuil_pic_octets": int(SEUIL_PIC_TRANCHE * total), "seuil_dispo_octets": int(SEUIL_DISPO_MIN * total)}
        if pic > SEUIL_PIC_TRANCHE * total:
            motifs.append(f"pic de la tranche {pic} octets au-delà de {SEUIL_PIC_TRANCHE} de la mémoire de la machine")
        if baisse > pic + TOLERANCE_RECOUPEMENT_OCTETS:
            motifs.append(f"recoupement : la machine a perdu {baisse} octets, la tranche n'en compte que {pic} (+1 Gio)")
        if prudente < SEUIL_DISPO_MIN * total:
            motifs.append(f"mémoire disponible estimée au plus bas {prudente} octets, sous {SEUIL_DISPO_MIN} de la machine")
    return {"compte": not motifs, "motifs": motifs, "calcul": calcul}


def statuts_genres(rendus: list, sains: dict[str, bool]) -> dict[str, str]:
    """« épreuve morte » si le cas sain du genre n'a pas rendu ses tentatives ; sinon « conforme » ou « non conforme »."""
    statuts = {}
    for r in rendus:
        g = r["genre"]
        if sains.get(g) is False:
            statuts[g] = "épreuve morte"
        elif not r["ok"] or statuts.get(g) == "non conforme":
            statuts[g] = "non conforme"
        else:
            statuts.setdefault(g, "conforme")
    return statuts


def juger_python(cas: dict, res: dict) -> list[str]:
    ecarts = []
    code = res["execution"]["code"]
    if "code" in cas and code != cas["code"]:
        ecarts.append(f"code {code} ≠ {cas['code']} ; stderr {res['stderr'][-300:]!r}")
    if cas.get("code_non_nul") and code == 0:
        ecarts.append("code nul, arrêt par le bac attendu")
    ecarts += [f"stdout sans « {x} »" for x in cas.get("stdout_contient", []) if x not in res["stdout"]]
    ecarts += [f"stdout avec « {x} »" for x in cas.get("stdout_absent", []) if x in res["stdout"]]
    if "incident_attendu" in cas and res.get("incident_bac") != cas["incident_attendu"]:
        ecarts.append(f"incident du bac {res.get('incident_bac')!r}, {cas['incident_attendu']!r} attendu")
    if "duree_max_s" in cas and (res["execution"]["duree_murale_s"] or 0) > cas["duree_max_s"]:
        ecarts.append(f"durée murale {res['execution']['duree_murale_s']} > {cas['duree_max_s']}")
    return ecarts


def _noter(rendus: list, sorties: list, genre: str, cas: dict, res: dict, ecarts: list, extra: dict | None = None) -> None:
    sorties.append(json.dumps(res, ensure_ascii=False))
    if res.get("processus_residuels"):
        ecarts.append(f"processus résiduels {res['processus_residuels']}")
    if res.get("dossiers_restants"):
        ecarts.append(f"dossiers restants {res['dossiers_restants']}")
    if not res.get("isolement"):
        ecarts.append("exécuté sans isolement")
    if res.get("incident_bac") and not (cas.get("incident_attendu") or cas.get("incident_compilation_attendu")):
        ecarts.append(f"incident du bac {res['incident_bac']}")
    rendus.append({"genre": genre, "nom": cas.get("nom", cas["fichier"]), "ok": not ecarts, "ecarts": ecarts,
                   "incident_bac": res.get("incident_bac"),
                   "observe": observer(cas, res) if "verdict" in res else {},
                   "temps": res.get("compilation") or res.get("execution"), "noyau": res.get("noyau"), **(extra or {})})


def epingler_verificateur(chemin_chaine: str | Path, verificateur: Path = VERIFICATEUR) -> dict:
    chemin = Path(chemin_chaine)
    d = json.loads(chemin.read_text(encoding="utf-8"))
    d["verificateur_noyau"] = str(verificateur)
    d["verificateur_noyau_sha256"] = hashlib.sha256(verificateur.read_bytes()).hexdigest()
    chemin.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return {"verificateur_noyau": d["verificateur_noyau"], "sha256": d["verificateur_noyau_sha256"],
            "version_lean": d.get("version_lean"), "commit_mathlib": d.get("commit_mathlib")}


def premier_pas_noyau(cfg: X.Config, artefacts: Path) -> dict:
    if cfg.mode != "bac":
        raise X.ErreurBac("le premier pas du noyau n'a de sens qu'en mode « bac »")
    attendus = json.loads((artefacts / ATTENDUS).read_text(encoding="utf-8"))
    rendus, sorties = [], []
    for passage, supplementaires in (("avec G-L3+", True), ("sans G-L3+", False)):
        bac = X.Bac(replace(cfg, supplementaires=supplementaires))
        for cas in attendus["noyau"]:
            c = dict(cas, **cas.get("sans_suppl", {})) if not supplementaires else cas
            res = bac.verifier_lean(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"), cas["etapes"])
            _noter(rendus, sorties, f"noyau ({passage})", c, res, juger_noyau(c, res))
    releves = []   # observations sans jugement (refus à tort possibles), hors de la conformité
    bac = X.Bac(cfg)
    for cas in attendus.get("observations_noyau", []):
        res = bac.verifier_lean(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"), cas["etapes"])
        releves.append({"nom": cas["nom"], "accepte": res["verdict"]["accepte_gardes"], "observe": observer(cas, res)})
    return {"version": VERSION, "pas": "noyau", "cas": rendus, "observations": releves,
            "conforme": all(c["ok"] for c in rendus)}


def epreuve(cfg: X.Config, artefacts: Path) -> dict:
    if cfg.mode != "bac":
        raise X.ErreurBac("l'épreuve d'isolement n'a de sens qu'en mode « bac » (lanceur isolé)")
    attendus = json.loads((artefacts / ATTENDUS).read_text(encoding="utf-8"))
    for groupe in ("isolement_lean", "python"):   # v8, R2 : sans témoin sain, l'épreuve morte ne se verrait pas
        if not any(c.get("sain") for c in attendus[groupe]):
            raise X.ErreurBac(f"attendus sans cas sain dans le groupe {groupe!r} : épreuve refusée avant tout item")
    LEURRE.parent.mkdir(mode=0o700, exist_ok=True)
    jeton = "leurre-" + secrets.token_hex(16)
    LEURRE.write_text(jeton + "\n", encoding="utf-8")
    os.chmod(LEURRE, 0o600)
    avant = manifeste()
    bac = X.Bac(cfg)
    rendus, sorties, sains = [], [], {}
    for cas in attendus["lean"]:
        res = bac.verifier_lean(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"), cas["etapes"])
        _noter(rendus, sorties, "gardes Lean", cas, res, juger_lean(cas, res))
    for cas in attendus["isolement_lean"]:
        res = bac.verifier_lean(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"), 1)
        if cas.get("sain"):
            sains["isolement Lean"] = sain_vivant(cas, res["sortie_compilation"])
        _noter(rendus, sorties, "isolement Lean", cas, res, juger_tentatives(cas, res["sortie_compilation"]),
               extrait_sonde(res))
    for cas in attendus["python"]:
        res = bac.executer_python(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"))
        if cas.get("sain"):
            sains["Python"] = sain_vivant(cas, res["stdout"])
        _noter(rendus, sorties, "Python", cas, res,
               juger_python(cas, res) + (juger_tentatives(cas, res["stdout"]) if "tentatives" in cas else []))
    bac_limite = X.Bac(replace(cfg, **LIMITES_ESSAI))
    for cas in attendus["limites_python"]:
        res = bac_limite.executer_python(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"))
        _noter(rendus, sorties, "limites", cas, res, juger_python(cas, res))
    for cas in attendus.get("limites_lean", []):
        res = bac_limite.verifier_lean(X.nouvel_item(), (artefacts / cas["fichier"]).read_text(encoding="utf-8"),
                                       cas["etapes"])
        _noter(rendus, sorties, "limites Lean", cas, res, juger_limite_lean(cas, res),
               dict(extrait_sonde(res), incident_compilation=res.get("incident_compilation"),
                    incident_noyau=res.get("incident_noyau")))
    apres = manifeste()
    hote = []
    if avant != apres:
        hote.append("manifeste de la chaîne, de Mathlib, de l'environnement Python ou du harnais changé")
    if any(jeton in s for s in sorties):
        hote.append("jeton du leurre présent dans une sortie")
    hote += [f"fichier piège présent sur l'hôte : {p}" for p in PIEGES_HOTE if os.path.lexists(p)]
    for racine in (cfg.racine_items, cfg.racine_sorties):
        restes = list(racine.iterdir())
        if restes:
            hote.append(f"{racine} non vide : {[str(r) for r in restes][:5]}")
    p = subprocess.run(["ps", "-u", cfg.utilisateur, "-o", "pid="], capture_output=True, text=True)
    if p.stdout.split():
        hote.append(f"processus de bac encore vivants à la fin : {p.stdout.split()}")
    genres = statuts_genres(rendus, sains)
    morts = sorted(g for g, s in genres.items() if s == "épreuve morte")
    conforme = all(c["ok"] for c in rendus) and not hote and not morts
    statut = "épreuve morte" if morts else ("conforme" if conforme else "non conforme")
    memoire = signal_memoire([(f"{i:02d} {c['genre']} : {c['nom']}", c["temps"]) for i, c in enumerate(rendus)])
    return {"version": VERSION, "cas": rendus, "controles_hote": hote, "manifeste_avant": avant,
            "manifeste_apres": apres, "sains": sains, "genres": genres, "genres_morts": morts, "statut": statut,
            "conforme": conforme, "memoire": memoire}


def mesurer(cfg: X.Config, artefacts: Path, fichier: str = "sain_v1.lean", etapes: int = 2,
            meminfo: Path = Path("/proc/meminfo"), jeton: str | None = None) -> dict:
    """v8 : trois passages en suite, puis trois en parallèle dans une tranche réservée de nom neuf, mémoire de la machine
    entière relevée pendant le bloc parallèle ; `parallele_3_compte` selon `juger_parallele`."""
    source = (artefacts / fichier).read_text(encoding="utf-8")

    def un(bac):
        r = bac.verifier_lean(X.nouvel_item(), source, etapes)
        return {"accepte": r["verdict"]["accepte_gardes"], "compilation": r["compilation"], "noyau": r["noyau"],
                "incident_bac": r.get("incident_bac")}

    bac = X.Bac(cfg)
    suite = [un(bac) for _ in range(3)]
    tranche = TRANCHE_MESURE.format(jeton or secrets.token_hex(4))
    bac_p = X.Bac(replace(cfg, tranche=tranche))
    t0 = time.monotonic()
    with ReleveMachine(cfg.racine_cgroup / tranche / "memory.peak", meminfo) as releve:
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
            parallele = list(ex.map(lambda _: un(bac_p), range(3)))
    murale = round(time.monotonic() - t0, 3)
    lancements = [(f"{genre} {i} {pas}", p[pas]) for genre, liste in (("suite", suite), ("parallèle", parallele))
                  for i, p in enumerate(liste) for pas in ("compilation", "noyau")]
    memoire = signal_memoire(lancements)
    m = releve.resultat()
    verdict = juger_parallele(parallele, m, memoire)
    return {"version": VERSION, "fichier": fichier, "suite": suite, "parallele_3": parallele,
            "parallele_3_murale_s": murale, "tranche": tranche, "releve_machine": m, "memoire": memoire,
            "parallele_3_compte": verdict["compte"], "parallele_3_motifs": verdict["motifs"],
            "parallele_3_calcul": verdict["calcul"]}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["epingler-verificateur", "noyau", "epreuve", "mesurer"])
    ap.add_argument("--chaine", default="/opt/harnais/chaine-v1.json")
    ap.add_argument("--artefacts", default=str(Path(__file__).resolve().parent / "artefacts_r5_v4"))
    a = ap.parse_args(argv)
    if a.action == "epingler-verificateur":
        res = epingler_verificateur(a.chaine)
    else:
        cfg = X.charger_config(a.chaine)
        res = {"noyau": premier_pas_noyau, "epreuve": epreuve, "mesurer": mesurer}[a.action](cfg, Path(a.artefacts))
    json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")
    if res.get("statut") == "épreuve morte":   # v7 : distinct de « non conforme »
        return 3
    return 0 if res.get("conforme", True) else 1


if __name__ == "__main__":
    sys.exit(main())
