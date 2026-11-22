"""Pièce 1 — registre de tirage et engagement (§ 1 de la spécification ; garde G2 du § 4).

Plan : trois conditions E, D, U, équiprobables ; l'unité est l'épisode, le bloc est la tâche ; chaque tâche est jouée
en 3k emplacements, k par condition, en bloc complet randomisé (k = 2 par défaut).

Graines (R9, `numpy.random.SeedSequence`, clés distinctes) :
- conditions de la tâche t : `SeedSequence(entropie_racine, spawn_key=(0, t))`, permutation uniforme des 3k étiquettes ;
- graine de l'agent à l'emplacement e de la tâche t : `SeedSequence(entropie_racine, spawn_key=(1, t, e))`, calculée
  avant le tirage des conditions ;
- tirages de permutation du test : `SeedSequence(entropie_racine, spawn_key=(2,))` (module `permutation_v2`) ;
- monde planté : `SeedSequence(entropie_monde, spawn_key=(3, t))` (module `monde_v2`) ;
- ordre de passage : `SeedSequence(entropie_racine, spawn_key=(4,))` — clé NON fixée par la spécification (point
  laissé ouvert, voir le rapport) ;
- pièce d'audit : `SeedSequence(entropie_racine, spawn_key=(5, t))` (module `audit_v2`) — clé NON fixée par la
  spécification (point laissé ouvert).

`numero_tache` est le rang de la tâche dans le registre, compté à partir de 0 (le départ à 0 est un choix d'écriture,
point laissé ouvert).

Engagement : avant la course, le registre (tâche, emplacement, condition, graine d'agent, ordre de passage) est écrit,
puis son empreinte SHA-256 et celle du code du test sont écrites dans un fichier d'engagement ; les deux fichiers sont
scellés par `controle_ia.scellement`. L'entropie racine n'est écrite nulle part avant la course ; elle est révélée après,
et `verifier_engagement(..., entropie_revelee=...)` rejoue le tirage.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from .. import scellement
from ..gardes import GardeArret
from .erreurs_v2 import RefusEngagement, RefusGraine, RefusPlan

VERSION_REGISTRE = "registre-hasard-defenseur-v2"
VERSION_ENGAGEMENT = "engagement-hasard-defenseur-v2"
CONDITIONS = ("E", "D", "U")
CODE = {"E": 0, "D": 1, "U": 2}
E, D, U = 0, 1, 2
UNITE = "episode"
BLOC = "tache"
K_DEFAUT = 2

CLE_CONDITIONS = 0
CLE_AGENT = 1
CLE_PERMUTATIONS = 2
CLE_MONDE = 3
CLE_ORDRE = 4  # point laissé ouvert : la spécification ne fixe pas cette clé
CLE_AUDIT = 5  # point laissé ouvert : la spécification ne fixe pas cette clé

NB_MOTS_GRAINE = 2  # la graine d'agent consignée : 2 mots de 64 bits (128 bits), en hexadécimal


def verifier_entropie(entropie, nom: str = "entropie") -> None:
    """Une entropie est un entier positif ou une suite non vide d'entiers positifs ; rien d'autre, aucun défaut."""
    if isinstance(entropie, bool) or entropie is None:
        raise RefusGraine(f"{nom} absente ou mal formée : {entropie!r}")
    if isinstance(entropie, (int, np.integer)):
        if entropie < 0:
            raise RefusGraine(f"{nom} négative : {entropie!r}")
        return
    if isinstance(entropie, (list, tuple)) and entropie and all(
        isinstance(x, (int, np.integer)) and not isinstance(x, bool) and x >= 0 for x in entropie
    ):
        return
    raise RefusGraine(f"{nom} mal formée : {entropie!r}")


def _entropie_ss(entropie):
    return [int(x) for x in entropie] if isinstance(entropie, (list, tuple)) else int(entropie)


def base_conditions(k: int) -> np.ndarray:
    return np.repeat(np.array([E, D, U], dtype=np.int8), k)


def mots_emplacement(entropie_racine, numero_tache: int, numero_emplacement: int, nb_mots: int) -> np.ndarray:
    """Mots de 64 bits issus de `SeedSequence(entropie_racine, spawn_key=(1, t, e))`.

    Les `NB_MOTS_GRAINE` premiers forment la graine d'agent consignée ; les suivants sont le hasard propre de l'agent
    simulé (monde planté). `generate_state` est cohérent par préfixe : la graine consignée ne dépend pas de `nb_mots`.
    """
    ss = np.random.SeedSequence(_entropie_ss(entropie_racine), spawn_key=(CLE_AGENT, int(numero_tache), int(numero_emplacement)))
    return ss.generate_state(NB_MOTS_GRAINE + nb_mots, np.uint64)


def graine_hex(mots: np.ndarray) -> str:
    return "".join(f"{int(m):016x}" for m in mots[:NB_MOTS_GRAINE])


def tirer_conditions_tache(entropie_racine, numero_tache: int, k: int) -> np.ndarray:
    rng = np.random.default_rng(np.random.SeedSequence(_entropie_ss(entropie_racine), spawn_key=(CLE_CONDITIONS, int(numero_tache))))
    return rng.permutation(base_conditions(k)).astype(np.int8)


def tirer_ordre(entropie_racine, n_taches: int, k: int) -> np.ndarray:
    """Ordre de passage tiré : permutation des (tâche, emplacement), tableau (n_taches·3k, 2)."""
    rng = np.random.default_rng(np.random.SeedSequence(_entropie_ss(entropie_racine), spawn_key=(CLE_ORDRE,)))
    n = 3 * k
    perm = rng.permutation(n_taches * n)
    return np.stack([perm // n, perm % n], axis=1).astype(np.int64)


@dataclass
class Plan:
    """Plan tiré. `mots_agent` (hasard propre de l'agent simulé) n'est jamais écrit dans le registre."""

    identifiants: tuple
    numeros: np.ndarray
    k: int
    conditions: np.ndarray  # (n_taches, 3k), codes 0 = E, 1 = D, 2 = U
    graines: list  # graines[t][e] : chaîne hexadécimale
    ordre: np.ndarray  # (n_taches·3k, 2)
    etiquettes: dict  # texte exact de chaque étiquette, {"E": ..., "D": ..., "U": ...}
    unite: str = UNITE
    bloc: str = BLOC
    mots_agent: np.ndarray | None = field(default=None, repr=False)

    @property
    def n_taches(self) -> int:
        return int(self.conditions.shape[0])


def verifier_etiquettes(etiquettes) -> None:
    if not isinstance(etiquettes, dict) or set(etiquettes) != set(CONDITIONS):
        raise RefusPlan(f"textes d'étiquette attendus pour E, D, U exactement : {etiquettes!r}")
    textes = [etiquettes[c] for c in CONDITIONS]
    if any(not isinstance(x, str) or not x for x in textes):
        raise RefusPlan("texte d'étiquette vide ou non textuel")
    if len(set(textes)) != 3:
        raise RefusPlan("deux conditions portent le même texte d'étiquette")


def tirer_plan(entropie_racine, identifiants, etiquettes: dict, k: int = K_DEFAUT, nb_mots_agent: int = 0) -> Plan:
    """Tire le plan du § 1. La graine d'agent de chaque emplacement est calculée avant les conditions."""
    verifier_entropie(entropie_racine, "entropie racine")
    verifier_etiquettes(etiquettes)
    identifiants = tuple(identifiants)
    if not identifiants:
        raise RefusPlan("aucune tâche dans le registre")
    if len(set(identifiants)) != len(identifiants):
        raise RefusPlan("identifiant de tâche en double dans le registre")
    if not isinstance(k, (int, np.integer)) or isinstance(k, bool) or k < 2:
        raise RefusPlan(f"k doit être un entier au moins égal à 2 (variance d'échantillon du § 3) : {k!r}")
    if nb_mots_agent < 0:
        raise RefusPlan("nombre de mots d'agent négatif")
    n_t, n = len(identifiants), 3 * int(k)
    numeros = np.arange(n_t)
    # 1. graines d'agent, fixées avant le tirage de la condition
    graines, mots = [], (np.empty((n_t, n, nb_mots_agent), dtype=np.uint64) if nb_mots_agent else None)
    for t in range(n_t):
        ligne = []
        for e in range(n):
            m = mots_emplacement(entropie_racine, t, e, nb_mots_agent)
            ligne.append(graine_hex(m))
            if mots is not None:
                mots[t, e] = m[NB_MOTS_GRAINE:]
        graines.append(ligne)
    # 2. conditions, bloc complet par tâche
    conditions = np.stack([tirer_conditions_tache(entropie_racine, t, int(k)) for t in range(n_t)])
    # 3. ordre de passage
    ordre = tirer_ordre(entropie_racine, n_t, int(k))
    plan = Plan(identifiants, numeros, int(k), conditions, graines, ordre, dict(etiquettes), mots_agent=mots)
    verifier_plan_structure(plan)
    return plan


def verifier_plan_structure(plan: Plan) -> None:
    """Contrôles sans entropie : unité, bloc, bloc complet, rangs, graines présentes et distinctes, ordre complet."""
    if plan.unite != UNITE or plan.bloc != BLOC:
        raise RefusPlan(f"unité {plan.unite!r} / bloc {plan.bloc!r} : seul le plan épisode dans tâche est permis")
    k, n = plan.k, 3 * plan.k
    c = np.asarray(plan.conditions)
    if c.ndim != 2 or c.shape[1] != n or c.shape[0] != len(plan.identifiants):
        raise RefusPlan(f"forme des conditions {c.shape} incompatible avec {len(plan.identifiants)} tâches et k = {k}")
    for t in range(c.shape[0]):
        comptes = np.bincount(c[t].astype(np.int64), minlength=3)
        if comptes.shape[0] != 3 or not np.all(comptes == k):
            raise RefusPlan(f"tâche {t} : bloc incomplet {comptes.tolist()} (k = {k} par condition attendu)")
    if not np.array_equal(np.asarray(plan.numeros), np.arange(c.shape[0])):
        raise RefusGraine("numéros de tâche différents du rang dans le registre (graine partagée ou décalée)")
    if len(plan.graines) != c.shape[0] or any(len(l) != n for l in plan.graines):
        raise RefusGraine("graine d'agent absente pour au moins un emplacement")
    plates = [g for l in plan.graines for g in l]
    for g in plates:
        if not isinstance(g, str) or len(g) != 16 * NB_MOTS_GRAINE or any(ch not in "0123456789abcdef" for ch in g):
            raise RefusGraine(f"graine d'agent absente ou mal formée : {g!r}")
    if len(set(plates)) != len(plates):
        raise RefusGraine("graine d'agent partagée entre emplacements ou tâches")
    o = np.asarray(plan.ordre)
    if o.ndim != 2 or o.shape != (c.shape[0] * n, 2):
        raise RefusPlan("ordre de passage absent ou incomplet")
    if len({(int(a), int(b)) for a, b in o}) != o.shape[0] or o.min() < 0 or o[:, 0].max() >= c.shape[0] or o[:, 1].max() >= n:
        raise RefusPlan("ordre de passage qui n'est pas une permutation des emplacements")


def registre_en_dict(plan: Plan) -> dict:
    return {
        "version": VERSION_REGISTRE,
        "unite": plan.unite,
        "bloc": plan.bloc,
        "k": plan.k,
        "etiquettes": {c: plan.etiquettes[c] for c in CONDITIONS},
        "taches": [
            {
                "identifiant": plan.identifiants[t],
                "numero_tache": int(plan.numeros[t]),
                "emplacements": [
                    {"numero_emplacement": e, "condition": CONDITIONS[int(plan.conditions[t, e])], "graine_agent": plan.graines[t][e]}
                    for e in range(3 * plan.k)
                ],
            }
            for t in range(plan.n_taches)
        ],
        "ordre_passage": [[int(a), int(b)] for a, b in plan.ordre],
    }


def plan_depuis_dict(d: dict) -> Plan:
    """Relit un registre ; tout champ absent ou mal formé est refusé (aucune valeur par défaut)."""
    try:
        if d["version"] != VERSION_REGISTRE:
            raise RefusEngagement(f"version de registre inconnue : {d['version']!r}")
        k = d["k"]
        taches = d["taches"]
        identifiants = tuple(t["identifiant"] for t in taches)
        numeros = np.array([t["numero_tache"] for t in taches], dtype=np.int64)
        conditions, graines = [], []
        for t in taches:
            emp = t["emplacements"]
            if [x["numero_emplacement"] for x in emp] != list(range(len(emp))):
                raise RefusPlan(f"tâche {t['identifiant']!r} : emplacements non numérotés 0..3k−1 dans l'ordre")
            if any(x["condition"] not in CODE for x in emp):
                raise RefusPlan(f"tâche {t['identifiant']!r} : condition inconnue")
            conditions.append([CODE[x["condition"]] for x in emp])
            graines.append([x.get("graine_agent") for x in emp])
        plan = Plan(
            identifiants,
            numeros,
            int(k),
            np.array(conditions, dtype=np.int8),
            graines,
            np.array(d["ordre_passage"], dtype=np.int64).reshape(-1, 2) if d["ordre_passage"] else np.empty((0, 2), np.int64),
            dict(d["etiquettes"]),
            unite=d["unite"],
            bloc=d["bloc"],
        )
    except KeyError as e:
        raise RefusEngagement(f"champ absent du registre : {e}") from e
    verifier_etiquettes(plan.etiquettes)
    verifier_plan_structure(plan)
    return plan


def texte_registre(plan: Plan) -> str:
    return json.dumps(registre_en_dict(plan), ensure_ascii=False, sort_keys=True, indent=1) + "\n"


def empreintes_code() -> dict:
    """Empreinte SHA-256 de chaque module du paquet (le code du test), et une empreinte d'ensemble."""
    dossier = Path(__file__).resolve().parent
    mods = {p.name: scellement.empreinte(p) for p in sorted(dossier.glob("*.py"))}
    ensemble = hashlib.sha256("".join(f"{h}  {n}\n" for n, h in sorted(mods.items())).encode()).hexdigest()
    return {"modules": mods, "ensemble": ensemble}


def engager(plan: Plan, dossier, nom: str) -> tuple[Path, Path]:
    """Écrit `<nom>-registre.json` et `<nom>-engagement.json`, puis les scelle. Refuse d'écraser (R12)."""
    dossier = Path(dossier)
    verifier_plan_structure(plan)
    chemin_r = dossier / f"{nom}-registre.json"
    chemin_e = dossier / f"{nom}-engagement.json"
    for p in (chemin_r, chemin_e):
        if p.exists():
            raise RefusEngagement(f"{p} existe déjà : on n'écrase jamais (R12)")
    chemin_r.write_text(texte_registre(plan), encoding="utf-8")
    code = empreintes_code()
    engagement = {
        "version": VERSION_ENGAGEMENT,
        "registre": chemin_r.name,
        "empreinte_registre": scellement.empreinte(chemin_r),
        "empreinte_code": code["ensemble"],
        "empreintes_modules": code["modules"],
    }
    chemin_e.write_text(json.dumps(engagement, ensure_ascii=False, sort_keys=True, indent=1) + "\n", encoding="utf-8")
    scellement.sceller(chemin_r)
    scellement.sceller(chemin_e)
    return chemin_r, chemin_e


def rejouer(plan_lu: Plan, entropie_revelee) -> None:
    """Rejoue le tirage à partir de l'entropie révélée : conditions, graines et ordre doivent être identiques."""
    verifier_entropie(entropie_revelee, "entropie révélée")
    rejoue = tirer_plan(entropie_revelee, plan_lu.identifiants, plan_lu.etiquettes, plan_lu.k)
    if not np.array_equal(rejoue.conditions, plan_lu.conditions):
        raise RefusEngagement("rejeu : conditions différentes du registre engagé")
    if rejoue.graines != plan_lu.graines:
        raise RefusEngagement("rejeu : graines d'agent différentes du registre engagé")
    if not np.array_equal(rejoue.ordre, plan_lu.ordre):
        raise RefusEngagement("rejeu : ordre de passage différent du registre engagé")


def verifier_engagement(chemin_registre, chemin_engagement, entropie_revelee=None, exiger_code_courant: bool = True) -> Plan:
    """Garde G2. Cas sain : registre conforme à l'empreinte. Artefact : registre modifié après coup, graine absente."""
    chemin_registre, chemin_engagement = Path(chemin_registre), Path(chemin_engagement)
    for p in (chemin_registre, chemin_engagement):
        try:
            scellement.verifier(p)
        except GardeArret as e:
            raise RefusEngagement(f"G2 : {e}") from e
    eng = json.loads(chemin_engagement.read_text(encoding="utf-8"))
    for cle in ("version", "registre", "empreinte_registre", "empreinte_code", "empreintes_modules"):
        if cle not in eng:
            raise RefusEngagement(f"G2 : champ {cle!r} absent de l'engagement")
    if eng["registre"] != chemin_registre.name:
        raise RefusEngagement(f"G2 : l'engagement vise {eng['registre']!r}, non {chemin_registre.name!r}")
    if scellement.empreinte(chemin_registre) != eng["empreinte_registre"]:
        raise RefusEngagement("G2 : registre modifié après l'engagement")
    if exiger_code_courant and empreintes_code()["ensemble"] != eng["empreinte_code"]:
        raise RefusEngagement("G2 : code du test différent du code engagé")
    plan = plan_depuis_dict(json.loads(chemin_registre.read_text(encoding="utf-8")))
    if entropie_revelee is not None:
        rejouer(plan, entropie_revelee)
    return plan
