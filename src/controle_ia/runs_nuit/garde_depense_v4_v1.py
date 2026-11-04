"""Relance v4 de R1 : **gardes de dépense** (point I2 de la contre-lecture R2 `contre-lecture-relance-v4-v1.md`,
`e224ae8a…` ; écart V4-E12) et **surveillance** (point I3) rendues mécaniques. Module neuf (R12), processeur seulement,
sans réseau : il ne crée aucune tâche planifiée, ne loue ni ne détruit rien ; il calcule ce que la session de pilotage
(session-depot) écrit et ce que les deux tâches planifiées appliquent, pour que chaque règle soit éprouvée (R5) avant
d'être posée.

Protocole repris du complément scellé (`prereg/R1-addendum-relance-v2-complement-validation-v1.md`, commit `4b47db7b`,
`049f20ba…`, « Liste d'arrêt » : armement, quatre épreuves, lecture aveugle des journaux), seuils de la v4 :

- **Destruction par l'identifiant seulement** (R10) : `commande_destruction` rend `vastai destroy instance <id>` pour un
  identifiant entier exact, jamais une étiquette ni un motif ; aucun signal par numéro de processus (aucun accès au
  conteneur n'est posé en mode « args », fait constaté du complément).
- **Tâche (ii), destruction à heure fixe** : `heure_destruction` = `T0 + H`, `H = (57 USD − dépenses déjà imputées au GO,
  sessions et reprises comprises − disque estimé) / prix horaire − 15 min` ; marge nulle ou négative : refus (ne pas
  créer l'instance).
- **Tâche (i), vérification horaire** : `decision_horaire` : dépense engagée = vie depuis `T0` × prix + disque + déjà
  imputé ; projection à la vérification suivante (+ intervalle + 10 min) ; ≥ 57 USD projetés : **détruire** ; fin de
  l'amorce vue au journal (« AMORCE … fin ») : **détruire** ; ≥ 45 USD engagés ou projetés : **alerte** ; fin de vie
  projetée `F` au-delà de l'heure de (ii) : **demande d'extension** ; prompt sans identifiant, sans `T0` ou sans prix :
  **échec visible et alerte, rien n'est détruit** ; identifiant absent du listing : rien n'est détruit, compte rendu.
- **Prompts** des deux tâches (`prompt_tache`), non armé (aucun identifiant : ne détruit rien, alerte) et armé
  (identifiant, `T0`, prix, disque, heure de destruction) ; `lire_prompt` relit un prompt (second listing de l'armement :
  identifiant et `T0` exacts, heure de départ de (ii) = `T0 + H`) : `exiger_armement`.
- **Lecture aveugle des journaux** (`filtrer_journal`) : ne garde que les lignes `AMORCE`, et des autres lignes la seule
  heure et les champs de route (`etape`, `episodes`, `lot`, `cibles`, `lots`, `version`, `DELAI_ETAPE_MIN`, compte de
  tests passés, chemin et empreinte de la table v4) ; jamais `retrouves=`, `lecture=`, `accord=`, `captures=`, `voie=`,
  `fautes=`, `fideles=`, ni une ligne qui dit un résultat. `projection_fin` (règle écrite d'avance, sur ces seuls champs) :
  `V0` = heure de la ligne `etape=reparation … cibles=89`, `Vk`, `k` = dernière ligne `etape=reparation episodes=k/89` ;
  `F = maintenant + (89 − k) × (Vk − V0) / k + 75 min` ; avant la première ligne `episodes=` : aucune projection ; après
  `89/89` : `F = maintenant + 75 min`.
- **Surveillance** (I3, valeurs de la v4) : `verifier_surveillance` : session 1, plafond 180 min, délai 120 min ; session 2,
  2 200 et 2 100 min ; tests `358` passés (ou le nombre de l'addendum scellé) ; session 2 : `cibles=89 lots=28`, table v4
  de version 4 ; **une autre valeur lue fait détruire l'instance par son identifiant**, sans autre lecture.

    PYTHONPATH=src python -m controle_ia.runs_nuit.garde_depense_v4_v1 epreuves        (les quatre épreuves, R5)
    PYTHONPATH=src python -m controle_ia.runs_nuit.garde_depense_v4_v1 filtrer < journal  (lecture aveugle)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone

from ..gardes import GardeArret

VERSION = "garde_depense_v4_v1"
GO_ID = "GO-2026-11-03-03"
PLAFOND_GO_USD = 60.0
ALERTE_USD = 45.0
DESTRUCTION_USD = 57.0
MARGE_DESTRUCTION_MIN = 15
INTERVALLE_MIN = 60
MARGE_VERIFICATION_MIN = 10
RESTE_APRES_REPARATION_MIN = 75          # table v4, chaîne, rejeu, poussées, au plus une heure de vie après l'amorce
CIBLES_V4, LOTS_V4 = 89, 28
SURVEILLANCE = {"temoin": {"plafond": 180, "delai": 120}, "reparation": {"plafond": 2200, "delai": 2100}}
CHAMPS_PERMIS = ("etape", "episodes", "lot", "cibles", "lots", "version")
FORMAT_HEURE = "%Y-%m-%dT%H:%M:%SZ"


def _heure(x) -> datetime:
    if isinstance(x, datetime):
        if x.tzinfo is None:
            raise GardeArret("heure sans fuseau : UTC exigé")
        return x.astimezone(timezone.utc)
    try:
        return datetime.strptime(str(x), FORMAT_HEURE).replace(tzinfo=timezone.utc)
    except ValueError as e:
        raise GardeArret(f"heure {x!r} : format {FORMAT_HEURE} (UTC) attendu") from e


def _texte_heure(h: datetime) -> str:
    return h.astimezone(timezone.utc).strftime(FORMAT_HEURE)


def exiger_identifiant(x) -> int:
    """Identifiant d'instance Vast.ai : entier exact > 0 écrit en chiffres ; tout autre chose : refus (R10)."""
    if isinstance(x, bool) or x is None:
        raise GardeArret(f"identifiant d'instance {x!r} : absent ou invalide (rien n'est détruit)")
    s = str(x).strip()
    if not re.fullmatch(r"[1-9][0-9]{0,11}", s):
        raise GardeArret(f"identifiant d'instance {x!r} : entier exact attendu (jamais une étiquette ni un motif)")
    return int(s)


def _prix(x, quoi: str) -> float:
    if isinstance(x, bool) or not isinstance(x, (int, float)) or x != x:
        raise GardeArret(f"{quoi} {x!r} : nombre attendu")
    return float(x)


def commande_destruction(identifiant) -> list[str]:
    """Seule commande de destruction : par l'identifiant exact de l'instance (R10)."""
    return ["vastai", "destroy", "instance", str(exiger_identifiant(identifiant))]


def heure_destruction(T0, prix_horaire, disque_estime: float, deja_imputees: float) -> dict:
    """Tâche (ii) : `T0 + H`, `H = (57 − imputées − disque) / prix − 15 min`. Refus si le prix n'est pas > 0 ou si
    `H` n'est pas > 0 (aucune marge : l'instance ne se crée pas)."""
    t0 = _heure(T0)
    p = _prix(prix_horaire, "prix horaire")
    d = _prix(disque_estime, "disque estimé")
    i = _prix(deja_imputees, "dépenses déjà imputées")
    if p <= 0 or d < 0 or i < 0:
        raise GardeArret("prix horaire > 0, disque et dépenses imputées ≥ 0 attendus")
    h_min = (DESTRUCTION_USD - i - d) / p * 60.0 - MARGE_DESTRUCTION_MIN
    if h_min <= 0:
        raise GardeArret(f"H = {h_min:.1f} min ≤ 0 : plus de marge sous {DESTRUCTION_USD} USD (ne pas créer)")
    fin = t0 + timedelta(minutes=h_min)
    return {"T0": _texte_heure(t0), "H_min": round(h_min, 1), "heure_destruction": _texte_heure(fin),
            "prix_horaire": p, "disque_estime": d, "deja_imputees": i, "seuil_usd": DESTRUCTION_USD}


def depense_engagee(T0, maintenant, prix_horaire, disque: float, deja_imputees: float) -> float:
    vie_h = max((_heure(maintenant) - _heure(T0)).total_seconds(), 0.0) / 3600.0
    return round(vie_h * float(prix_horaire) + float(disque) + float(deja_imputees), 4)


# --------------------------------------------------------------------------------------------------------------------
# Lecture aveugle des journaux (C-5 du complément, champs de la v4)

_PROGRES = re.compile(r"^PROGRES (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)((?: [A-Za-z_]+=[^ ]+)+)$")
_JOURNAL = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z) (.*)$")


def filtrer_journal(lignes) -> list[str]:
    """Lignes gardées (voir l'en-tête) ; tout le reste est retiré sans être rendu."""
    sortie = []
    for brute in lignes:
        x = brute.rstrip("\n")
        if x.startswith("AMORCE "):
            sortie.append(x)
            continue
        m = _PROGRES.match(x)
        if m:
            champs = dict(c.split("=", 1) for c in m.group(2).split())
            gardes = [f"{k}={champs[k]}" for k in CHAMPS_PERMIS if k in champs]
            if gardes:
                sortie.append(f"PROGRES {m.group(1)} " + " ".join(gardes))
            continue
        m = _JOURNAL.match(x)
        if not m:
            continue
        h, reste = m.groups()
        d = re.search(r"\bDELAI_ETAPE_MIN=(\S+)", reste)
        if reste.startswith("début : ") and d:
            sortie.append(f"{h} DELAI_ETAPE_MIN={d.group(1)}")
            continue
        t = re.fullmatch(r"tests : (\d+) passed(?:, \d+ warnings?)? in [0-9.]+s(?: \(\d+:\d{2}:\d{2}\))?", reste)
        if t:
            sortie.append(f"{h} tests : {t.group(1)} passed")
            continue
        if re.fullmatch(r"tests : .*", reste) or reste.startswith("tests en échec"):
            sortie.append(f"{h} tests : autre")
            continue
        v = re.fullmatch(r"table v4 : (\S+) \(([0-9a-f]{64})\)", reste)
        if v:
            sortie.append(f"{h} table v4 : {v.group(1)} ({v.group(2)})")
            continue
        if re.fullmatch(r"étape [a-z0-9-]+ (terminée|arrêtée).*", reste):
            sortie.append(f"{h} {reste.split(' ')[0]} {reste.split(' ')[1]} "
                          f"{'terminée' if ' terminée' in reste else 'arrêtée'}")
            continue
        if reste.startswith("fin : session ") or reste.startswith("ARRÊT pendant ") or reste.startswith("chaîne "):
            sortie.append(f"{h} {reste.split(' :')[0].split(' (')[0]}")
    return sortie


def _progres(lignes_filtrees):
    for x in lignes_filtrees:
        m = re.match(r"^PROGRES (\S+) (.*)$", x)
        if m:
            yield _heure(m.group(1)), dict(c.split("=", 1) for c in m.group(2).split())


def projection_fin(lignes_filtrees, maintenant) -> dict:
    """Fin de vie projetée (règle écrite d'avance ; seuls champs : heure, `etape`, `cibles`, `episodes`)."""
    v0 = None
    vk, k = None, None
    n = CIBLES_V4
    for h, c in _progres(lignes_filtrees):
        if c.get("etape") != "reparation":
            continue
        if "cibles" in c and v0 is None:
            v0, n = h, int(c["cibles"])
        m = re.fullmatch(r"(\d+)/(\d+)", c.get("episodes", ""))
        if m:
            vk, k = h, int(m.group(1))
    now = _heure(maintenant)
    if v0 is None or k is None or k < 1:
        return {"F": None, "k": k, "raison": "aucune ligne episodes=k/89 : aucune projection"}
    reste = (n - k) * (vk - v0) / k if k < n else timedelta(0)
    f = now + reste + timedelta(minutes=RESTE_APRES_REPARATION_MIN)
    return {"F": _texte_heure(f), "k": k, "n": n, "V0": _texte_heure(v0), "Vk": _texte_heure(vk)}


def decision_horaire(prompt: dict, maintenant, instances_listees, lignes_filtrees=()) -> dict:
    """Tâche (i) : rend {action, ...} ; action ∈ « echec_visible », « absente », « detruire », « alerte », « rien » ;
    `extension` vrai si la fin projetée dépasse l'heure de (ii). Rien n'est exécuté ici : la commande est rendue."""
    try:
        ident = exiger_identifiant(prompt.get("identifiant"))
        T0 = _heure(prompt.get("T0"))
        prix = _prix(prompt.get("prix_horaire"), "prix horaire")
        disque = _prix(prompt.get("disque", 0.0), "disque")
        imput = _prix(prompt.get("deja_imputees", 0.0), "dépenses déjà imputées")
        fin_ii = _heure(prompt.get("heure_destruction"))
        if prix <= 0:
            raise GardeArret("prix horaire ≤ 0")
    except GardeArret as e:
        return {"action": "echec_visible", "alerte": True, "motif": str(e), "commande": None}
    if ident not in {exiger_identifiant(x) for x in instances_listees}:
        return {"action": "absente", "alerte": False, "identifiant": ident, "commande": None,
                "motif": "instance absente du listing : rien n'est détruit, compte rendu"}
    dep = depense_engagee(T0, maintenant, prix, disque, imput)
    proj = round(dep + prix * (INTERVALLE_MIN + MARGE_VERIFICATION_MIN) / 60.0, 4)
    fin_amorce = any(re.match(r"^AMORCE \S+ : fin, code", x) for x in lignes_filtrees)
    pf = projection_fin(lignes_filtrees, maintenant)
    extension = pf["F"] is not None and _heure(pf["F"]) > fin_ii
    sortie = {"identifiant": ident, "depense": dep, "projetee": proj, "fin_amorce": fin_amorce, "projection": pf,
              "extension": extension, "commande": None}
    if proj >= DESTRUCTION_USD:
        return {**sortie, "action": "detruire", "alerte": True, "commande": commande_destruction(ident),
                "motif": f"dépense projetée {proj} ≥ {DESTRUCTION_USD} USD"}
    if fin_amorce:
        return {**sortie, "action": "detruire", "alerte": False, "commande": commande_destruction(ident),
                "motif": "fin de l'amorce lue au journal"}
    if dep >= ALERTE_USD or proj >= ALERTE_USD:
        return {**sortie, "action": "alerte", "alerte": True, "motif": f"dépense {dep} (projetée {proj}) ≥ {ALERTE_USD}"}
    return {**sortie, "action": "rien", "alerte": extension, "motif": "sous les seuils"}


def decision_destruction(prompt: dict, instances_listees) -> dict:
    """Tâche (ii) au départ : prompt sans identifiant → refus et alerte ; identifiant absent → rien, compte rendu ;
    présent → commande de destruction par l'identifiant."""
    try:
        ident = exiger_identifiant(prompt.get("identifiant"))
    except GardeArret as e:
        return {"action": "echec_visible", "alerte": True, "motif": str(e), "commande": None}
    if ident not in {exiger_identifiant(x) for x in instances_listees}:
        return {"action": "absente", "alerte": False, "identifiant": ident, "commande": None}
    return {"action": "detruire", "alerte": False, "identifiant": ident, "commande": commande_destruction(ident)}


# --------------------------------------------------------------------------------------------------------------------
# Prompts des deux tâches (armement)

_CHAMPS_PROMPT = ("identifiant", "T0", "prix_horaire", "disque", "deja_imputees", "heure_destruction")


def prompt_tache(tache: str, session: str, valeurs: dict | None = None, essai: bool = False) -> str:
    """Texte du prompt d'une tâche (« verification » (i) ou « destruction » (ii)) ; sans `valeurs` : prompt non armé
    (aucun identifiant : ne détruit rien, alerte). Les champs sont écrits une fois chacun, `cle = valeur`."""
    if tache not in ("verification", "destruction") or session not in SURVEILLANCE:
        raise GardeArret(f"tâche {tache!r} ou session {session!r} inconnue")
    tete = (f"{'ESSAI — ' if essai else ''}Garde de dépense de la relance v4 de R1 ({GO_ID}), session {session}, "
            f"tâche {'(i) vérification horaire' if tache == 'verification' else '(ii) destruction à heure fixe'}. "
            f"Seuils : alerte {ALERTE_USD} USD, destruction {DESTRUCTION_USD} USD. Destruction par l'identifiant "
            "ci-dessous seulement (`vastai destroy instance <identifiant>`), jamais par étiquette ni motif ; prompt sans "
            "identifiant, sans T0 ou sans prix : ne rien détruire, alerter (échec visible). Règles : "
            f"`python -m controle_ia.runs_nuit.{VERSION}`.")
    v = valeurs or {}
    lignes = [tete] + [f"{k} = {v[k]}" for k in _CHAMPS_PROMPT if k in v]
    return "\n".join(lignes) + "\n"


def lire_prompt(texte: str) -> dict:
    """Relit un prompt (second listing) : chaque champ au plus une fois ; nombres pour les prix."""
    sortie: dict = {}
    for x in texte.splitlines():
        m = re.fullmatch(r"([a-z_0-9A-Z]+) = (.+)", x.strip())
        if not m or m.group(1) not in _CHAMPS_PROMPT:
            continue
        if m.group(1) in sortie:
            raise GardeArret(f"prompt : champ {m.group(1)} écrit deux fois")
        val = m.group(2).strip()
        sortie[m.group(1)] = float(val) if m.group(1) in ("prix_horaire", "disque", "deja_imputees") else val
    sortie["essai"] = texte.startswith("ESSAI")
    return sortie


def exiger_armement(prompt_lu: dict, identifiant, T0, attendu_ii: dict, depart_ii) -> None:
    """Armement, étape (3) : prompt relu = identifiant et `T0` exacts, heure de destruction écrite = `T0 + H`, départ
    de (ii) programmé à cette heure ; sinon refus (la session de pilotage détruit alors l'instance par son identifiant)."""
    if prompt_lu.get("essai"):
        raise GardeArret("armement : prompt d'essai relu à la place du prompt armé")
    if str(prompt_lu.get("identifiant")) != str(exiger_identifiant(identifiant)):
        raise GardeArret("armement : identifiant relu ≠ identifiant de l'instance")
    if prompt_lu.get("T0") != _texte_heure(_heure(T0)):
        raise GardeArret("armement : T0 relu ≠ T0 de la création")
    if prompt_lu.get("heure_destruction") != attendu_ii["heure_destruction"]:
        raise GardeArret("armement : heure de destruction relue ≠ T0 + H")
    if _texte_heure(_heure(depart_ii)) != attendu_ii["heure_destruction"]:
        raise GardeArret("armement : départ de la tâche (ii) ≠ T0 + H")


# --------------------------------------------------------------------------------------------------------------------
# Surveillance (I3)


def verifier_surveillance(lignes_filtrees, session: str, tests_attendus: int = 358) -> dict:
    """Valeurs v4 attendues au journal filtré. « detruire » dès qu'une valeur lue diffère (plafond de l'amorce, délai,
    tests, cibles, lots, version de la table) ; « conforme » si toutes sont lues égales ; « en_cours » sinon."""
    if session not in SURVEILLANCE:
        raise GardeArret(f"session {session!r} inconnue")
    att = SURVEILLANCE[session]
    lu: dict = {}
    ecarts = []

    def voir(cle, valeur, attendue):
        lu.setdefault(cle, valeur)
        if valeur != attendue:
            ecarts.append(f"{cle} = {valeur} ≠ {attendue}")

    for x in lignes_filtrees:
        m = re.match(r"^AMORCE \S+ : relance v4 de R1, session (\S+), commit \S+, plafond de l'amorce (\S+) min$", x)
        if m:
            voir("session", m.group(1), session)
            voir("plafond", m.group(2), str(att["plafond"]))
        m = re.match(r"^\S+ DELAI_ETAPE_MIN=(\S+)$", x)
        if m:
            voir("delai", m.group(1), str(att["delai"]))
        m = re.match(r"^\S+ tests : (\S+)", x)
        if m:
            voir("tests", m.group(1), str(tests_attendus))
    for _, c in _progres(lignes_filtrees):
        if c.get("etape") == "reparation" and "cibles" in c:
            voir("cibles", c["cibles"], str(CIBLES_V4))
            voir("lots", c.get("lots"), str(LOTS_V4))
        if c.get("etape") == "verification_table" and "version" in c:
            voir("version_table", c["version"], "4")
        if c.get("etape") == "temoin" and session != "temoin":
            ecarts.append("ligne etape=temoin en session 2")
        if c.get("etape") in ("reparation", "verification_table") and session == "temoin":
            ecarts.append(f"ligne etape={c['etape']} en session 1")
    requis = ["session", "plafond", "delai", "tests"] + (["cibles", "lots"] if session == "reparation" else [])
    if ecarts:
        verdict = "detruire"
    elif all(k in lu for k in requis):
        verdict = "conforme"
    else:
        verdict = "en_cours"
    return {"verdict": verdict, "ecarts": ecarts, "lu": lu, "manquants": [k for k in requis if k not in lu]}


# --------------------------------------------------------------------------------------------------------------------
# Les quatre épreuves (R5) sur des valeurs consignées (aucune instance présente au prompt)

INSTANCE_ABSENTE = 58851293          # détruite le 2 novembre (`registres/arrets.md` de `b1d911b5`, l. 74)


def epreuves() -> list[dict]:
    """(1) destruction, cas sain : identifiant absent du compte → rien n'est détruit ; (2) destruction, artefact : prompt
    sans identifiant → refus, alerte ; (3) vérification, cas sain : vie 16:42:40 → 18:13:07 à 1,187 USD/h (≈ 1,79 USD) :
    ni alerte ni destruction ; (4) vérification, artefact : dépense fictive ≥ 45 puis ≥ 57 USD sur l'identifiant absent :
    rien n'est détruit (absente) ; même dépense sur un listing d'essai qui le contient : alerte, puis destruction rendue ;
    prompt sans prix : échec visible."""
    t0, fin = "2026-11-02T16:42:40Z", "2026-11-02T18:13:07Z"
    arme = {"identifiant": str(INSTANCE_ABSENTE), "T0": t0, "prix_horaire": 1.187, "disque": 0.0,
            "deja_imputees": 0.0, "heure_destruction": heure_destruction(t0, 1.187, 0.0, 0.0)["heure_destruction"]}
    sortie = [
        {"epreuve": "1 destruction, cas sain", **decision_destruction(arme, instances_listees=[])},
        {"epreuve": "2 destruction, artefact (sans identifiant)",
         **decision_destruction({k: v for k, v in arme.items() if k != "identifiant"}, instances_listees=[])},
        {"epreuve": "3 vérification, cas sain", **decision_horaire(arme, fin, [INSTANCE_ABSENTE])},
        {"epreuve": "4a vérification, artefact (absente, dépense fictive)",
         **decision_horaire({**arme, "deja_imputees": 50.0}, fin, [])},
        {"epreuve": "4b vérification, artefact (listing d'essai, ≥ 45)",
         **decision_horaire({**arme, "deja_imputees": 44.0}, fin, [INSTANCE_ABSENTE])},
        {"epreuve": "4c vérification, artefact (listing d'essai, ≥ 57 projetés)",
         **decision_horaire({**arme, "deja_imputees": 55.0}, fin, [INSTANCE_ABSENTE])},
        {"epreuve": "4d vérification, artefact (sans prix)",
         **decision_horaire({k: v for k, v in arme.items() if k != "prix_horaire"}, fin, [INSTANCE_ABSENTE])},
    ]
    return sortie


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=f"python -m controle_ia.runs_nuit.{VERSION}")
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("epreuves")
    sp.add_parser("filtrer")
    s = sp.add_parser("surveiller")
    s.add_argument("--session", required=True)
    s.add_argument("--tests", type=int, default=358)
    h = sp.add_parser("heure")
    h.add_argument("--T0", required=True)
    h.add_argument("--prix", type=float, required=True)
    h.add_argument("--disque", type=float, default=0.0)
    h.add_argument("--imputees", type=float, required=True)
    a = ap.parse_args(argv)
    if a.cmd == "epreuves":
        print(json.dumps(epreuves(), ensure_ascii=False, indent=1))
    elif a.cmd == "filtrer":
        print("\n".join(filtrer_journal(sys.stdin)))
    elif a.cmd == "surveiller":
        print(json.dumps(verifier_surveillance(filtrer_journal(sys.stdin), a.session, a.tests), ensure_ascii=False))
    else:
        print(json.dumps(heure_destruction(a.T0, a.prix, a.disque, a.imputees), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
