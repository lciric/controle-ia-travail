"""Vérifications communes de la chaîne de P4-instrument (contrôle positif de l'instrument de P3 ; R-262 (1), R-269), v1 :
un seul texte, lu à l'identique par le scellement, par les contrôles avant dépense et par le lanceur. Décliné de
`docs/procedures/P3-premier-test-v2/verifications_p3_v1.py` sous un nom neuf (R12).

Les contrôles du GO, de la révocation, du plafond par lancement, de l'échéance, de la borne de l'étape, de l'accord du
jour, du module cité et de la garde de calcul gelée ne sont pas recodés : ce sont les fonctions du module de P4
(`instrument_p4_v1.controler_go`, `controler_accord`, `rejouer_garde_de_calcul`, `exiger_module_cite`). Le module est
chargé par son chemin dans le dépôt RACINE, après contrôle de son empreinte contre la ligne « Module de P4 » du texte
PREREG : aucun code non cité ne s'exécute. Pourquoi les fonctions et pas la ligne de commande `--controle go` du module :
elle exige l'accord du jour, qui n'est consigné qu'après le scellement S ; le scellement et les contrôles avant dépense
(répétition finale comprise) contrôlent le GO sans l'accord. Le lanceur joue en plus, telles quelles, les lignes de
commande `--controle module` et `--controle go` du module juste avant la création. Ce module-ci ajoute seulement ce que
le module de P4 ne lit pas : la ligne du texte « **GO cité par la commande de création** : `GO_ID=…` » (forme exacte,
une seule fois, GO-2026-10-20-07 seul), les journaux des bancs et celui de la répétition jouet.

Python de la session (le module importe le code du dépôt et ses dépendances), -B, PYTHONDONTWRITEBYTECODE=1 :
  verifications_p4_v1.py go RACINE PREREG JOUR BORNE
      ligne « **GO cité par la commande de création** » du texte : une seule, de forme exacte, GO-2026-10-20-07 ; puis
      `controler_go` du module sur RACINE/registres/go.md et RACINE/registres/decisions.md (huit colonnes, type
      « calcul », accordé par Lazar, colonne « plafond » qui commence par « 10 USD par lancement », échéance de sa colonne,
      borne de l'étape BORNE strictement inférieure à 10 USD, révocations sous leurs deux formes) ; puis
      `rejouer_garde_de_calcul` (garde gelée RACINE/.claude/hooks/garde_calcul.py, sur le registre de RACINE, au JOUR).
      Écrit « GO-2026-10-20-07 conforme : … ».
  verifications_p4_v1.py accord RACINE PREREG R-… JOUR
      `controler_accord` du module : ligne R-… du jour, forme exacte « **Accord de Lazar pour le lancement de
      P4-instrument** », citation de GO-2026-10-20-07 ou d'un message de Lazar du jour, GO non échu.
  verifications_p4_v1.py module RACINE PREREG
      `exiger_module_cite` du module : les six fichiers cités, et eux seuls, à l'empreinte citée ; écrit une ligne
      « <chemin> <sha256> » par fichier.
  verifications_p4_v1.py repetition CODE JOURNAL CANDIDAT_NOM CANDIDAT_SHA
      journal de la répétition jouet : commit répété, candidat répété, quatre passages à leur code, six récupérations
      conformes (instance détruite par son identifiant), dix-neuf artefacts refusés chacun par un seul KO au préfixe
      attendu, dans le seul bloc indenté qui suit sa ligne (instance non détruite) ; trois lignes « script répété » exactement.
      Écrit une ligne « <script> <sha256> » par script répété.
  verifications_p4_v1.py preuves DOSSIER [JOURNAL …]
      journaux des bancs et de la répétition finale (tous les six si aucun n'est nommé) : présents, au verdict conforme
      sur leur dernière ligne, sans ligne d'échec, avec exactement les scripts qu'ils éprouvent ; une même empreinte pour
      un script éprouvé par plusieurs journaux. Écrit une ligne « <script> <sha256> » par script éprouvé.
Code 0 si conforme ; code 1 avec un message sur la dernière ligne sinon ; code 2 sur un usage faux.
"""
from __future__ import annotations

import hashlib
import importlib.util
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

GO_ATTENDU = "GO-2026-10-20-07"          # seul GO accepté dans la commande de création (en-tête « GO et dépense »)
CHEMIN_MODULE = "docs/procedures/P4-instrument-v1/instrument_p4_v1.py"
LIGNE_GO = re.compile(r"^[ \t]*- \*\*GO cité par la commande de création\*\* : `GO_ID=(GO-\d{4}-\d{2}-\d{2}-\d{2})`", re.M)
LIGNE_MODULE = re.compile(r"^[ \t]*-[ \t]+Module de P4 : `([^`]+)` : `([0-9a-f]{64})`[ \t]*$", re.M)


def lire(chemin) -> str:
    try:
        return Path(chemin).read_text(encoding="utf-8")
    except OSError:
        raise SystemExit(f"fichier {chemin} absent ou illisible") from None
    except UnicodeDecodeError as e:
        raise SystemExit(f"fichier {chemin} : UTF-8 invalide à l'octet {e.start} (ligne coupée au milieu d'un "
                         f"caractère ?)") from None


def charger_module(racine: Path, prereg: str):
    """Module de P4 du dépôt RACINE, chargé seulement s'il a l'empreinte de sa ligne « Module de P4 » du texte."""
    cites = [m for m in LIGNE_MODULE.finditer(lire(prereg)) if m.group(1) == CHEMIN_MODULE]
    if len(cites) != 1:
        raise SystemExit(f"ligne « Module de P4 » de {CHEMIN_MODULE} absente, en double ou mal formée dans le texte")
    p = Path(racine) / CHEMIN_MODULE
    try:
        e = hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        raise SystemExit(f"module de P4 absent : {p}") from None
    if e != cites[0].group(2):
        raise SystemExit(f"module de P4 {CHEMIN_MODULE} : empreinte {e[:12]} ≠ empreinte citée {cites[0].group(2)[:12]} "
                         "(aucun code non cité n'est exécuté)")
    sys.path.insert(0, str(Path(racine).resolve() / "src"))
    spec = importlib.util.spec_from_file_location("instrument_p4_v1", p)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if module.GO_CITE != GO_ATTENDU:
        raise SystemExit(f"module de P4 : GO_CITE {module.GO_CITE} ≠ {GO_ATTENDU}")
    return module


def _garde(fonction, *args):
    """Appelle une garde du module ; son refus (GardeArret) devient un échec motivé (code 1)."""
    from controle_ia.gardes import GardeArret
    try:
        return fonction(*args)
    except GardeArret as e:
        raise SystemExit(str(e)[:300]) from None


def go(racine: str, prereg: str, jour: str, borne: str) -> str:
    r = Path(racine)
    texte = lire(prereg)
    m = LIGNE_GO.findall(texte)
    if len(m) != 1 or len(re.findall(r"\*\*GO cité par la commande de création\*\*", texte)) != 1:
        raise SystemExit("ligne « **GO cité par la commande de création** : `GO_ID=…` » absente, en double ou mal formée")
    if m[0] != GO_ATTENDU:
        raise SystemExit(f"{m[0]} : seul {GO_ATTENDU} est accepté pour P4 (délégation R-269)")
    try:
        b = float(borne)
    except ValueError:
        raise SystemExit(f"borne de l'étape « {borne[:20]} » illisible") from None
    ip = charger_module(r, prereg)
    go_t, dec_t = lire(r / "registres" / "go.md"), lire(r / "registres" / "decisions.md")
    c = _garde(ip.controler_go, m[0], go_t, dec_t, jour, b)
    _garde(ip.rejouer_garde_de_calcul, r, f"GO_ID={m[0]} vastai create instance", jour)
    return (f"{c['go']} conforme : échéance {c['echeance']} ; plafond « {c['plafond'][:40]} » ; borne de l'étape "
            f"{c['borne_usd']:g} USD ; aucune révocation ; garde de calcul gelée : acceptée au {jour}")


def accord(racine: str, prereg: str, ident: str, jour: str) -> str:
    r = Path(racine)
    ip = charger_module(r, prereg)
    a = _garde(ip.controler_accord, ident, lire(r / "registres" / "go.md"), lire(r / "registres" / "decisions.md"), jour)
    cite = GO_ATTENDU if a["cite_delegation"] else "un message de Lazar du jour"
    return f"{ident} : accord de Lazar du {jour} pour le lancement de P4-instrument (cite {cite}) : conforme"


def module(racine: str, prereg: str) -> list[str]:
    ip = charger_module(Path(racine), prereg)
    cites = _garde(ip.exiger_module_cite, Path(racine), Path(prereg))
    return [f"{c} {s}" for c, s in sorted(cites.items())]


PASSAGES = ("passage 1-sain : code 0 ", "passage 2-artefact-branche-presente : code 2 ", "passage 3-manque : code 1 ",
            "passage 4-plafond-de-l-amorce : code 124 ")
_DET = " ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT (99999999)"
CONFORMES = (f"récupération (passage-1-sain) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}",
             f"récupération (passage-3-traces-seules) : code 4 ; RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN) : TOUS CONFORMES{_DET}",
             f"récupération (passage-4-plafond-traces-seules) : code 4 ; RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN) : TOUS CONFORMES{_DET}",
             f"récupération (arret-synthetique) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}",
             f"récupération (gardes-reelles) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}",
             f"récupération (textes-degeneres) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}")
_KO1 = " : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC ; INSTANCE 99999999 NON DÉTRUITE : NŒUD DE LAZAR"
ARTEFACTS = {f"récupération ({nom}){_KO1}": f"    KO  {prefixe} " for nom, prefixe in (
    ("artefact-scores-manquants", "4c"),
    ("artefact-validation-manquante", "4c"),
    ("artefact-ajout-hors-perimetre", "1c"),
    ("artefact-scores-alteres", "2b"),
    ("artefact-sceau-des-scores-faux", "2b"),
    ("artefact-resultat-autre-manifeste", "2b"),
    ("artefact-scores-hors-plan", "4d"),
    ("artefact-chaine-longue-dans-un-tableau", "4d"),
    ("artefact-texte-dans-le-journal", "4f"),
    ("artefact-texte-echappe-dans-un-resultat", "4f"),
    ("artefact-chaine-de-plus-de-200-caracteres", "4f"),
    ("artefact-fin-sans-resume-complet", "6f"),
    ("artefact-jeton-dans-une-trace", "7"),
    ("artefact-copie-non-versee", "0"),
    ("artefact-versions-autres", "3f"),
    ("artefact-carte-autre", "6b"),
    ("artefact-etiquette-autre", "8"),
    ("artefact-destruction-en-echec", "8"),
    ("artefact-instance-encore-listee", "8"))}
SCRIPTS = {"recuperation_p4_v1.sh", "repetition_jouet_p4_v1.sh", "outils_essais_p4_v1.py"}
LECTURE = re.compile(r"lecture jouet \(passage-1-sain\) : code 0 ; issue L[0-9]{1,2}")


def bloc_indente(lignes: list[str], i: int) -> list[str]:
    """Lignes indentées (quatre espaces) qui suivent immédiatement la ligne i : le bloc de cette récupération."""
    j = i + 1
    while j < len(lignes) and lignes[j].startswith("    "):
        j += 1
    return lignes[i + 1:j]


def repetition(code: str, journal: str, nom: str, sha: str) -> list[str]:
    lignes = lire(journal).split("\n")
    exigees = [f"commit du code répété : {code}", f"candidat répété : {nom} {sha}", "FIN DE LA RÉPÉTITION", *CONFORMES,
               *ARTEFACTS]
    for e in exigees:
        if lignes.count(e) != 1:
            raise SystemExit(f"ligne absente ou en double : {e}")
    if sum(x.startswith("candidat répété : ") for x in lignes) != 1:
        raise SystemExit("plusieurs lignes « candidat répété »")
    if sum(bool(LECTURE.fullmatch(x)) for x in lignes) != 1 or sum(x.startswith("lecture jouet") for x in lignes) != 1:
        raise SystemExit("lecture jouet : une ligne « lecture jouet (passage-1-sain) : code 0 ; issue L… » attendue")
    for p in PASSAGES:
        if sum(x.startswith(p) for x in lignes) != 1:
            raise SystemExit(f"passage : {p.strip()}")
    if sum("TOUS CONFORMES" in x for x in lignes) != len(CONFORMES) \
            or sum("INSTANCE DÉTRUITE PAR SON IDENTIFIANT" in x for x in lignes) != len(CONFORMES):
        raise SystemExit(f"{len(CONFORMES)} récupérations conformes, chacune suivie de la destruction, attendues")
    if sum("NON DÉTRUITE : NŒUD DE LAZAR" in x for x in lignes) != len(ARTEFACTS):
        raise SystemExit(f"{len(ARTEFACTS)} récupérations en échec, chacune sans destruction, attendues")
    for etiquette in CONFORMES:
        ko = [x for x in bloc_indente(lignes, lignes.index(etiquette)) if x.startswith("    KO")]
        if ko:
            raise SystemExit(f"{etiquette} : KO {ko}")
    for etiquette, prefixe in ARTEFACTS.items():
        ko = [x for x in bloc_indente(lignes, lignes.index(etiquette)) if x.startswith("    KO")]
        if len(ko) != 1 or not ko[0].startswith(prefixe):
            raise SystemExit(f"{etiquette} : KO {ko}")
    scripts = {}
    for x in lignes:
        if x.startswith("script répété : "):
            m = re.fullmatch(r"script répété : ([a-z0-9_]+_v1\.(?:py|sh)) ([0-9a-f]{64})", x)
            if not m:
                raise SystemExit(f"ligne « script répété » mal formée : {x[:90]}")
            if m.group(1) in scripts:
                raise SystemExit(f"script répété en double : {m.group(1)}")
            scripts[m.group(1)] = m.group(2)
    if set(scripts) != SCRIPTS:
        raise SystemExit(f"scripts répétés {sorted(scripts)} : les trois attendus exactement")
    return [f"{s} {scripts[s]}" for s in sorted(scripts)]


# journal → (verdict de sa dernière ligne, scripts qu'il éprouve exactement)
JOURNAUX = {
    "banc-lanceur-p4-v1.log": ("FIN DU BANC DU LANCEUR DE P4 ; cas non conformes : 0",
                               {"lancer_p4_v1.sh", "verifications_p4_v1.py", "essais_lanceur_p4_v1.sh"}),
    "banc-surveillance-p4-v1.log": ("FIN DU BANC DE LA SURVEILLANCE DE P4 ; cas non conformes : 0",
                                    {"surveiller_p4_v1.sh", "controle_cinq_minutes_p4_v1.sh", "essais_surveillance_p4_v1.sh"}),
    "banc-verifications-p4-v1.log": ("FIN DU BANC DES VÉRIFICATIONS DE P4 ; cas non conformes : 0",
                                     {"verifications_p4_v1.py", "essais_verifications_p4_v1.sh", "outils_essais_p4_v1.py"}),
    "banc-controles-p4-v1.log": ("FIN DU BANC DES CONTRÔLES DE P4 ; cas non conformes : 0",
                                 {"controles_avant_depense_p4_v1.sh", "verifications_p4_v1.py", "essais_controles_p4_v1.sh",
                                  "outils_essais_p4_v1.py"}),
    "banc-scellement-p4-v1.log": ("FIN DU BANC DU SCELLEMENT DE P4 ; cas non conformes : 0",
                                  {"sceller_p4_v1.sh", "verifications_p4_v1.py", "essais_scellement_p4_v1.sh",
                                   "outils_essais_p4_v1.py"}),
    "repetition-finale-p4-v1.log": ("RÉPÉTITION FINALE : CONFORME",
                                    {"sceller_p4_v1.sh", "controles_avant_depense_p4_v1.sh", "verifications_p4_v1.py",
                                     "repetition_finale_p4_v1.sh"}),
}


def preuves(dossier: str, noms: list[str]) -> list[str]:
    noms = noms or list(JOURNAUX)
    inconnus = [n for n in noms if n not in JOURNAUX]
    if inconnus or len(set(noms)) != len(noms):
        raise SystemExit(f"journaux nommés inconnus ou en double : {noms}")
    vus: dict[str, str] = {}
    for nom in noms:
        verdict, attendus = JOURNAUX[nom]
        p = Path(dossier) / nom
        if not p.is_file():
            raise SystemExit(f"journal {nom} absent ou illisible")
        lignes = lire(p).split("\n")
        non_vides = [x for x in lignes if x.strip()]
        if not non_vides or non_vides[-1] != verdict:
            raise SystemExit(f"journal {nom} : dernière ligne ≠ « {verdict} »")
        fautes = [x for x in lignes if "NON CONFORME" in x or x.lstrip().startswith(("Traceback", "JETON AFFICHÉ"))]
        if fautes:
            raise SystemExit(f"journal {nom} : ligne d'échec avant le verdict : {fautes[0].strip()[:90]}")
        propres = set()
        for x in lignes:
            if x.startswith("script éprouvé : "):
                m = re.fullmatch(r"script éprouvé : ([a-z0-9_]+_v1\.(?:py|sh)) ([0-9a-f]{64})", x)
                if not m:
                    raise SystemExit(f"journal {nom} : ligne « script éprouvé » mal formée : {x[:90]}")
                if vus.setdefault(m.group(1), m.group(2)) != m.group(2):
                    raise SystemExit(f"{m.group(1)} éprouvé sous deux empreintes")
                propres.add(m.group(1))
        if not propres:
            raise SystemExit(f"journal {nom} : aucune ligne « script éprouvé »")
        if propres != attendus:
            raise SystemExit(f"journal {nom} : scripts éprouvés ≠ attendus (manquants {sorted(attendus - propres)}, "
                             f"en trop {sorted(propres - attendus)})")
    return [f"{s} {vus[s]}" for s in sorted(vus)]


def main(argv: list[str]) -> int:
    if len(argv) == 6 and argv[1] == "go":
        print(go(*argv[2:6]))
    elif len(argv) == 6 and argv[1] == "accord":
        print(accord(*argv[2:6]))
    elif len(argv) == 4 and argv[1] == "module":
        print("\n".join(module(*argv[2:4])))
    elif len(argv) == 6 and argv[1] == "repetition":
        print("\n".join(repetition(*argv[2:6])))
    elif len(argv) >= 3 and argv[1] == "preuves":
        print("\n".join(preuves(argv[2], argv[3:])))
    else:
        print("usage : go RACINE PREREG JOUR BORNE | accord RACINE PREREG R-… JOUR | module RACINE PREREG | "
              "repetition CODE JOURNAL CANDIDAT_NOM CANDIDAT_SHA | preuves DOSSIER [JOURNAL …]", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
