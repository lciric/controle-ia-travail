"""Rubrique simplifiée RS1 du plan B des juges de T0.5 (préenregistrement `prereg/T0.5-plan-B-juges-v1.md`, « Métrique »).

Invite : `docs/sources/invites-plan-b-v1/invites/RS1.txt` (annexe A du préenregistrement), chargée par la fonction gelée
`charger_invite("RS1", racine=…)` : sceau du fichier, index scellé et empreinte de l'index, toute différence arrête.
Quatre critères, une seule échelle entière de 0 à 5. Score : somme brute des quatre notes (0 à 20) ; sur 100, par la
classe gelée `NotesRubrique` avec les critères RS1 : 100 × somme / 20, soit 5 × somme.

Lecture d'une réponse (étapes 1 à 10 de la « Métrique », plus la décision R-225). Le module gelé `rubrique.py` n'est pas
touché : ses motifs et sa fonction `lire_une_note` sont importés tels quels.
1. critères : SPECIFICITY, COVERAGE, RIGOR, FEASIBILITY, de 0 à 5 ;
2. lignes candidates : le motif de ligne de H.4 (`rubrique.py`, l. 39), élargi aux minuscules dans le nom ; le nom se
   compare en majuscules ; les lignes d'autres noms (JUSTIFICATION comprise) sont ignorées et comptées ;
3. nettoyage de la valeur exactement comme sous H.4 (`rubrique.py`, l. 88) ;
4. occurrence « chiffrée » si la valeur nettoyée commence par un chiffre, éventuellement précédé d'un signe (+, - ou −) ;
   une occurrence non chiffrée (prose, vide, « <4> ») est ignorée et comptée ;
5. valeur d'une occurrence chiffrée : d'abord un contrôle neuf de la suite du premier nombre (premier nombre : motifs
   gelés `_FRACTION`, puis `_ENTIER`, « − » lu « - ») ; invalide si cette suite est, après d'éventuelles espaces,
   « - », « – », « — », « to » ou « or » (« intervalle », R-221), ou « , », « ; », « and » ou « ( » (« second
   nombre », R-225), puis, après d'éventuelles espaces, un chiffre, éventuellement signé (+, - ou −) ; casse
   indifférente (D-4, R-249). Ensuite la fonction gelée `lire_une_note(valeur, 0, 5)` : « 4 », « 4.0 » et « 4/5 »
   valent 4 ; demi-point, décimale, autre échelle écrite, « 3-4 » ou valeur hors de [0, 5] : invalide ;
6. note du critère : la valeur de la première occurrence chiffrée, si toutes ses occurrences chiffrées sont valides et
   égales ; une occurrence chiffrée invalide, où qu'elle soit, donne « note invalide » ; deux valeurs différentes,
   « notes contradictoires » ; jamais de choix entre elles, jamais d'arrondi ni de remplacement ;
7. sans occurrence chiffrée : « absente » sans aucune occurrence, « illisible » avec des occurrences non chiffrées ;
8. la ligne JUSTIFICATION n'est pas lue ;
9. une réponse tronquée (sans jeton de fin) est incomplète, même si ses quatre notes se lisent (CL-9) ;
10. réponse incomplète : une anomalie au moins, ou tronquée ; elle n'a pas de score, jamais imputé.

Limites écrites (D-5, R-249) :
- une prose qui suit une note et commence par un séparateur listé puis un chiffre (« 5 - 1 weak point », « 4 (2 weak
  points) ») rend l'occurrence invalide ;
- tout second nombre relié au premier autrement que par les séparateurs listés (chacun suivi d'éventuelles espaces
  puis d'un chiffre, éventuellement signé), Markdown compris, n'est pas vu par le contrôle : la fonction gelée lit le
  premier nombre. Formes trouvées par les relectures, toutes lues sur le premier nombre : « 3 4 », « 3 vs 4 »,
  « 3 (or 4) », « 3 & 4 », « 3 out of 4 », « 3 + 1 », « 3 =4 », « 3 ⁄ 5 » (barre de fraction), « 3 **or** 4 »,
  « 3 *to* 4 », « 3 _and_ 4 » (le nettoyage n'enlève que les bords), « 3 -- 4 », tirets non listés (U+2010, U+2012,
  U+2015), « 3, or 4 », « 3 and/or 4 », « 3 [4] », « 3 (maybe 4) », « 3 but 4 », « 3/5 4/5 », « 3 → 4 », « 3 ~ 4 ».
  La lecture ne choisit donc jamais entre deux nombres reliés par l'un des séparateurs listés ; relié autrement, le
  second nombre n'est pas vu et le premier est lu.
Descriptif neuf, sans effet sur la lecture (D-5) : `lues_suite_avec_chiffre`, nombre d'occurrences lues (valides) dont
la suite, après le premier nombre, contient encore un chiffre. Il compte les seconds nombres non vus et aussi les
gloses saines qui portent un chiffre (« 3 (out of 5) ») : il majore la taille de la limite et se lit dans les deux sens
(R4).

Annexe A (D-6, R-249) : `exiger_annexe_a_egale_a_rs1` extrait l'invite de l'annexe A du préenregistrement scellé, par
la règle de `docs/sources/invites-plan-b-v1/LISEZMOI.md` (« Construction »), et l'exige égale, octet pour octet, à
`invites/RS1.txt` ; le lanceur (avant le manifeste) et le lecteur l'appellent.
"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from ..gardes import GardeArret
from ..scellement import empreinte
from .invites import charger_invite, empreinte_invite, index_invites
from .rubrique import _ENTIER, _FRACTION, NotesRubrique, lire_une_note, points_max

IDENTIFIANT_RS1 = "RS1"
RACINE_INVITES_RS1 = Path(__file__).resolve().parents[3] / "docs" / "sources" / "invites-plan-b-v1"
# (nom tel qu'écrit dans l'invite, note minimale, note maximale), dans l'ordre de l'invite
CRITERES_RS1: tuple[tuple[str, int, int], ...] = (
    ("SPECIFICITY", 0, 5), ("COVERAGE", 0, 5), ("RIGOR", 0, 5), ("FEASIBILITY", 0, 5),
)
POINTS_MAX_RS1 = points_max(CRITERES_RS1)  # 20 : score sur 100 = 5 × somme
# séparateurs du contrôle de la suite du premier nombre (configuration de l'étape : `controle_intervalles`)
SEPARATEURS_INTERVALLE = ("-", "–", "—", "to", "or")
SEPARATEURS_SECOND_NOMBRE = (",", ";", "and", "(")
ANOMALIE_TRONQUEE = "réponse tronquée (sans jeton de fin) : incomplète"  # texte de `noter_ensembles` sous H.4
# bornes de l'invite dans l'annexe A du préenregistrement (`LISEZMOI.md`, « Construction ») : retrait de quatre espaces
RETRAIT_ANNEXE_A = "    "
DEBUT_ANNEXE_A = RETRAIT_ANNEXE_A + "## Scoring Rubric"
FIN_ANNEXE_A = RETRAIT_ANNEXE_A + "- Do not write any analysis."

# motif de ligne de H.4 (`rubrique.py`, l. 39), seul changement : minuscules permises dans le nom
_LIGNE_RS1 = re.compile(r"^[ \t>*_#-]*(?P<nom>[A-Za-z_]+)[ \t*_]*:[ \t*_]*(?P<note>[^\n]*)$", re.M)
_CHIFFREE = re.compile(r"^[+\-−]?\d")


def _suite(separateurs: tuple[str, ...]) -> re.Pattern:
    """Séparateur listé, après d'éventuelles espaces, puis, après d'éventuelles espaces, un chiffre éventuellement signé
    (+, - ou −, comme à l'étape 4 : D-4) ; casse indifférente."""
    return re.compile(r"\s*(?:" + "|".join(re.escape(s) for s in separateurs) + r")\s*[+\-−]?\d", re.I)


_INTERVALLE = _suite(SEPARATEURS_INTERVALLE)
_SECOND_NOMBRE = _suite(SEPARATEURS_SECOND_NOMBRE)


def charger_invite_rs1(racine: str | Path = RACINE_INVITES_RS1) -> str:
    """Texte exact de RS1, par la fonction gelée `charger_invite` ; arrêt si fichier, sceau ou index divergent."""
    return charger_invite(IDENTIFIANT_RS1, racine=racine)


def empreinte_invite_rs1(racine: str | Path = RACINE_INVITES_RS1) -> str:
    """Empreinte de RS1 telle que chargée (à consigner dans la configuration et le manifeste)."""
    return empreinte_invite(IDENTIFIANT_RS1, racine=racine)


def annexe_a_du_texte(texte: str) -> str:
    """Invite RS1 extraite du texte d'un préenregistrement par la règle de `LISEZMOI.md` (« Construction ») : lignes de
    la première ligne égale à « ␣␣␣␣## Scoring Rubric » à la dernière qui commence par « ␣␣␣␣- Do not write any
    analysis. » ; chaque ligne non vide de ce bloc porte le retrait de quatre espaces, retiré ; lignes vides gardées
    vides ; une seule fin de ligne finale. Début ou fin introuvable, ou ligne non vide sans retrait : arrêt."""
    lignes = texte.split("\n")
    if DEBUT_ANNEXE_A not in lignes:
        raise GardeArret(f"annexe A : ligne de début {DEBUT_ANNEXE_A!r} introuvable dans le préenregistrement")
    debut = lignes.index(DEBUT_ANNEXE_A)
    fins = [i for i, x in enumerate(lignes) if x.startswith(FIN_ANNEXE_A)]
    if not fins or max(fins) < debut:
        raise GardeArret(f"annexe A : ligne de fin {FIN_ANNEXE_A!r}… introuvable après la ligne de début")
    bloc = lignes[debut:max(fins) + 1]
    sans_retrait = [debut + i + 1 for i, x in enumerate(bloc) if x and not x.startswith(RETRAIT_ANNEXE_A)]
    if sans_retrait:
        raise GardeArret(f"annexe A : ligne non vide sans le retrait de quatre espaces (ligne {sans_retrait[0]} du "
                         f"préenregistrement)")
    return "\n".join(x[len(RETRAIT_ANNEXE_A):] for x in bloc) + "\n"


def exiger_annexe_a_egale_a_rs1(prereg: str | Path, racine: str | Path = RACINE_INVITES_RS1) -> str:
    """Garde (D-6) : l'invite extraite de l'annexe A du préenregistrement (`annexe_a_du_texte`) est, octet pour octet,
    le fichier de RS1 (sceau et index d'abord contrôlés par la fonction gelée). Tout écart arrête. Rend l'empreinte du
    fichier, égale à celle du texte extrait."""
    charger_invite_rs1(racine)
    fichier = Path(racine) / index_invites(racine)[IDENTIFIANT_RS1]["fichier"]
    extrait = annexe_a_du_texte(Path(prereg).read_text(encoding="utf-8")).encode("utf-8")
    attendu = fichier.read_bytes()
    if extrait != attendu:
        n = next((i for i, (a, b) in enumerate(zip(extrait, attendu)) if a != b), min(len(extrait), len(attendu)))
        raise GardeArret(f"annexe A du préenregistrement ≠ {fichier.name} (premier octet différent : {n} ; "
                         f"{len(extrait)} octets extraits, {len(attendu)} attendus)")
    return empreinte(fichier)


def exiger_criteres_de_l_invite(texte: str) -> None:
    """Les critères du code sont ceux de l'invite, mot pour mot : un titre « ### NOM (0-5) » et une ligne
    « NOM: <score> » par critère, aucun autre titre de critère. Tout écart arrête."""
    titres = re.findall(r"^### ([A-Z_]+) \((\d+)-(\d+)\)$", texte, re.M)
    attendus = [(n, str(lo), str(hi)) for n, lo, hi in CRITERES_RS1]
    if titres != attendus:
        raise GardeArret(f"invite RS1 : titres des critères {titres} ≠ code {attendus}")
    for nom, _, _ in CRITERES_RS1:
        if len(re.findall(rf"^{nom}: <score>$", texte, re.M)) != 1:
            raise GardeArret(f"invite RS1 : ligne « {nom}: <score> » absente ou répétée dans le format de sortie")


def controle_suite(valeur: str) -> str | None:
    """Contrôle neuf de l'étape 5, fait avant la fonction gelée, sans la toucher : « intervalle » (R-221) ou « second
    nombre » (R-225) si la valeur continue, après son premier nombre, par un séparateur puis un chiffre ; None sinon
    (la fonction gelée décide alors seule). Sans premier nombre reconnu (« 3-4 », « 3.5 »), None : la fonction gelée
    refuse déjà la valeur."""
    s = valeur.strip().replace("−", "-")
    m = _FRACTION.match(s) or _ENTIER.match(s)
    if m is None:
        return None
    reste = s[m.end():]
    if _INTERVALLE.match(reste):
        return "intervalle"
    if _SECOND_NOMBRE.match(reste):
        return "second nombre"
    return None


def _reste_apres_le_premier_nombre(valeur: str) -> str | None:
    s = valeur.strip().replace("−", "-")
    m = _FRACTION.match(s) or _ENTIER.match(s)
    return None if m is None else s[m.end():]


def _a_une_suite(valeur: str) -> bool:
    """Compte « lues suivies de texte » (D-7), descriptif, sans effet : vrai pour une occurrence lue (valide) dont la
    valeur nettoyée porte, après son premier nombre (motifs gelés `_FRACTION` puis `_ENTIER`, « − » lu « - »), au moins
    un caractère de mot (`\\w` : lettre, chiffre ou souligné, Unicode compris). Il compte toute occurrence lue, où
    qu'elle soit : une prose qui commence par un nombre (« Specificity: 2 of the proposals… »), mais aussi une glose de
    la ligne de note elle-même (« 3 (competent) », « 3/5 (out of 5) »). Une ponctuation seule (« 3. ») ne compte pas."""
    reste = _reste_apres_le_premier_nombre(valeur)
    return reste is not None and re.search(r"\w", reste) is not None


def _suite_avec_chiffre(valeur: str) -> bool:
    """Compte « lues dont la suite porte un chiffre » (D-5), descriptif, sans effet : vrai pour une occurrence lue
    (valide) dont la valeur nettoyée porte encore un chiffre (`\\d`, Unicode compris) après son premier nombre. Il
    compte les seconds nombres non vus par le contrôle (« 3 vs 4 ») et les gloses saines chiffrées
    (« 3 (out of 5) »)."""
    reste = _reste_apres_le_premier_nombre(valeur)
    return reste is not None and re.search(r"\d", reste) is not None


def lire_notes_rs1(reponse: str) -> tuple[NotesRubrique, dict]:
    """Notes RS1 d'une réponse (étapes 1 à 8) et comptes descriptifs. La troncature (étape 9) est hors de ce texte :
    voir `lire_reponse_rs1`."""
    if not isinstance(reponse, str):
        raise GardeArret(f"réponse de juge de type {type(reponse).__name__} : texte attendu")
    noms = {n: (lo, hi) for n, lo, hi in CRITERES_RS1}
    occurrences: dict[str, list[str]] = {n: [] for n in noms}
    autres: Counter = Counter()
    for m in _LIGNE_RS1.finditer(reponse):
        nom = m["nom"].upper()
        if nom in noms:
            occurrences[nom].append(m["note"].strip().strip("*_ ").strip())
        else:
            autres[nom] += 1
    r = NotesRubrique(criteres=CRITERES_RS1)
    motifs: Counter = Counter()
    comptes = {"par_critere": {}, "non_chiffrees": 0, "intervalles": 0, "seconds_nombres": 0,
               "invalides_lecture_gelee": 0, "contradictions": 0, "lues_suivies_de_texte": 0,
               "lues_suite_avec_chiffre": 0, "lignes_autres_noms": dict(sorted(autres.items()))}
    for nom, (lo, hi) in noms.items():
        chiffrees = [v for v in occurrences[nom] if _CHIFFREE.match(v)]
        non_chiffrees = len(occurrences[nom]) - len(chiffrees)
        comptes["par_critere"][nom] = {"chiffrees": len(chiffrees), "non_chiffrees": non_chiffrees}
        comptes["non_chiffrees"] += non_chiffrees
        if not chiffrees:
            motif = "absente" if not occurrences[nom] else "illisible"
            r.anomalies.append(f"{nom} : {motif}" + (" (seulement des occurrences non chiffrées)"
                                                    if motif == "illisible" else ""))
            motifs[motif] += 1
            continue
        valeurs, invalide = [], False
        for v in chiffrees:
            suite = controle_suite(v)
            if suite is not None:
                comptes["intervalles" if suite == "intervalle" else "seconds_nombres"] += 1
                r.anomalies.append(f"{nom} : note invalide, {suite} ({v[:30]!r})")
                motifs["note invalide"] += 1
                invalide = True
                continue
            lu = lire_une_note(v, lo, hi)
            if isinstance(lu, str):
                comptes["invalides_lecture_gelee"] += 1
                r.anomalies.append(f"{nom} : note invalide, {lu}")
                motifs["note invalide"] += 1
                invalide = True
                continue
            comptes["lues_suivies_de_texte"] += int(_a_une_suite(v))
            comptes["lues_suite_avec_chiffre"] += int(_suite_avec_chiffre(v))
            valeurs.append(lu)
        if len(set(valeurs)) > 1:
            comptes["contradictions"] += 1
            r.anomalies.append(f"{nom} : notes contradictoires ({', '.join(map(str, valeurs))})")
            motifs["notes contradictoires"] += 1
        elif not invalide:
            r.notes[nom] = valeurs[0]
    comptes["motifs"] = dict(sorted(motifs.items()))
    return r, comptes


def lire_reponse_rs1(reponse: str, tronquee: bool) -> dict:
    """Lecture complète d'une réponse sous RS1 (étapes 1 à 10) : notes, anomalies (troncature comprise), score sur 100
    ou None, et comptes. `tronquee` : réponse sans jeton de fin (coupée au plafond), fixé par l'appelant."""
    if not isinstance(tronquee, bool):
        raise GardeArret(f"drapeau « tronquée » de type {type(tronquee).__name__} : booléen attendu")
    notes, comptes = lire_notes_rs1(reponse)
    complete = notes.complete and not tronquee
    return {"notes": dict(notes.notes),
            "anomalies": notes.anomalies + ([ANOMALIE_TRONQUEE] if tronquee else []),
            "score": notes.score_sur_100() if complete else None,
            "complete": complete,
            # sensibilité descriptive « incomplétude sans la règle de troncature » (« Métrique », sans effet)
            "complete_sans_troncature": notes.complete,
            "lecture": comptes}
