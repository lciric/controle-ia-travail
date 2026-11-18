#!/usr/bin/env python3
"""Lanceur du bras du juge externe différé de l'organisme d'idéation sur les organismes discrets — version 3.

Version 3 : corrections de la contre-lecture de la version 2 (agent neuf, 18 novembre 2026 ; v2 `0569d0b6…`, jamais jouée) :
1. appel de contrôle du bras à 0,6 USD pour Carbon et Argon (leurs commandes réservent 8 192 jetons de pensée et refusent
   sous 0,52 USD, « rien envoyé » : à 0,2 le bras échouait au contrôle à coup sûr) ; 0,2 gardé pour Astra ; pire cas par
   lignée 3,1 (Carbon, Argon) et 2,7 USD (Astra) ;
2. relais du fournisseur vérifié avant tout (`GET /relais/etat` sur la boucle locale : il répond et n'admet que le modèle
   joué) ; une tentative au coût plancher (≤ 1e-6 USD) sans consigne envoyée ne verrouille plus la lignée ;
3. verrou « un seul bras payé par lignée » durci : relance refusée si le run antérieur a un code hors de {0, 2, 4, 5}, un
   échec du lanceur, ou autre chose que des tentatives sans envoi ; verrou exclusif par lignée pendant le lancement ;
4. sonde du bac à sable informative (le bras lance la commande externe sans bac ; la sonde faisait refuser ici) ;
5. moteur réel déclaré (`--moteur claude-sdk --modele-commande-externe MODELE --commande-externe-lit-modele`) : la
   barrière « modèle servi = modèle demandé » est exigée et non plus facultative ;
6. journaux du bras et `RECOMPOSITION.json` copiés scellés au dépôt ; chiffres ASCII dans l'identifiant de GO.
Réserve connue (non corrigible sans appel payant) : si le fournisseur sert `gpt-6.2-astra` sous un identifiant daté, le
contrôle d'Astra échoue après envoi (≤ 0,2 USD) et la lignée se verrouille.

Joue, pour UNE lignée donnée en argument (`carbon`, `astra` ou `argon`), le juge externe différé sur les fiches validées
de la course lisible de cette lignée (courses du 18 novembre 2026 : Carbon par lot v12, Astra v13, Argon v14), après
attestation de lecture humaine scellée.

- Carbon et Argon : juge au modèle de la course, orchestrateur public épinglé (arbre `ee84d6ec…`), lanceur v8.
- Astra : juge joué avec `gpt-6.2-astra` à la place de `gpt-6-astra` (mots de Lazar « go 6.2 », « option a ») — remplacement
  **déclaré** au manifeste du bras, par l'orchestrateur augmenté (ajouts seuls, assemblé par
  `scripts/assembler_orchestrateur_remplacement_juge_v2.py`), lanceur v9.

Usage, seul et exact (cwd = racine du dépôt de travail) :

    /usr/local/bin/python3 -I -B scripts/lancer_bras_juge_ideation_organismes_discrets_v3.py LIGNEE

Ordre ; tout refus rend 2, motif sur la sortie d'erreur, avant tout appel :
1. un seul argument, une lignée connue ;
2. pièces épinglées (enveloppe, commande, scripts d'assemblage et de recomposition) et orchestrateur ;
3. copies scellées de la course : empreintes des fiches validées et de la consigne en attente épinglées ;
4. ligne de GO : une seule ligne principale de `registres/go.md` dont le périmètre porte « organisme d'idéation »,
   « organismes discrets », « lignée LIGNEE » et « juge externe », aucune autre lignée, type calcul, par Lazar, dans sa
   période, non révoquée, plafond ≥ pire cas (plafond de la session du juge 2,5 + appel de contrôle de la lignée) ;
5. attestation de lecture humaine scellée (`rapports/organismes-discrets-v1/attestation-lecture-juge-LIGNEE-v1.json`) :
   lecteur « Lazar », empreintes des fiches validées et de la consigne en attente égales aux épinglées ;
   puis un seul bras payé par lignée (runs antérieurs du dépôt) ; relais du fournisseur ; verrou exclusif de lancement ;
6. dossier de sortie neuf : course recomposée depuis les copies (`scripts/recomposer_sortie_course_ideation_v1.py`),
   orchestrateur assemblé (Astra) ; gardes de drapeaux, environnement sans clé, bac à sable ;
7. manifeste de départ scellé, bras, copies scellées de tout ce que le bras a écrit dans `runs/…/copies/`, manifeste de fin.

Le relais du fournisseur (boucle locale, clé dans son seul environnement) est lancé à part, avant ; ce lanceur ne détient
aucune clé. Le plafond externe est celui de la course (manifeste de départ), moins ce qu'elle a déjà compté : le bras le relit.
Le bras n'est jamais rejoué après dépense ; un échec sans envoi ni dépense (coût plancher de la commande) laisse le bras
relançable, depuis une recomposition neuve. Bibliothèque standard seulement (le lanceur tourne sous `-I`).
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import unicodedata
from pathlib import Path

VERSION = "lancer_bras_juge_ideation_organismes_discrets_v3"
DEPOT = Path(__file__).resolve().parents[1]
PYTHON = "/usr/local/bin/python3"

CLONE_PUBLIC = Path("/home/user/lciric/ideation-organism")
ARBRE_ORCHESTRATEUR = "ee84d6eca7a4c9b25f4e297ca29c6d9f24af5d70"
AJOUTS_REMPLACEMENT = {   # orchestrateur augmenté (Astra) : ajouts seuls, version 2 (après contre-lecture), épinglés
    "pole/bras_remplacement_v2.py": "42da66c3c178d43fd1d3dee13387cab64559907412d8dde8ff4b9b48db6495ef",
    "demonstrations/ideation_v9.py": "3990569ebfa6d4ea52d98462d04032b2ee7532aba75e78b95224f5d3afb1409a",
    "essais/test_bras_remplacement_v2.py": "cf3b85db882b085ba967ef2e4f731c9f657e050cb189c965d1e9d13bf115950b",
}
ASSEMBLEUR = ("scripts/assembler_orchestrateur_remplacement_juge_v2.py", "dd6c627d86a282b27abe9ecfa28055dbe22e590e38d40351c79bb0b8e9b9441d")
RECOMPOSEUR = ("scripts/recomposer_sortie_course_ideation_v1.py", "ec30fd3803e25a3ad49a42bfb8c48c58e8e892fc419b8f3b222f8447fc1cc10e")

ENVELOPPES = "rapports/organismes-discrets-v1/enveloppes-v1"
RUNS = "runs/course-ideation-organismes-discrets-"
LIGNEES = {
    "carbon": {
        "run": RUNS + "v12/20261118-084156-course-ideation-organismes-discrets-v12-carbon",
        "etiquette": "carbon-juge", "modele_course": "gemini-4-carbon", "modele_joue": "gemini-4-carbon",
        "enveloppe": (f"{ENVELOPPES}/appel-carbon-v3.sh", "9ef03f804bc13a9aebf13b0c03639af59d1d71e2e057190d9a38ecda5b233f32"),
        "commande": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py",
                     "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75"),
        "relais": {"port": 8792, "cle_modeles": "modeles"}, "controle_usd": 0.6,
        "fiches": "aae73de4e9da4b9aa2977472672358a3f8664ec460ff33a4a2a425a2b6fa74d7", "consigne": "1d7b5dbb821b1f9df1853210543f38d716b47a9ccec6576801c29d5c255c081c", "delai_commande_s": "3600",
    },
    "astra": {
        "run": RUNS + "v13/20261118-105220-course-ideation-organismes-discrets-v13-astra",
        "etiquette": "astra-juge", "modele_course": "gpt-6-astra", "modele_joue": "gpt-6.2-astra",
        "mot": "go 6.2",
        "enveloppe": (f"{ENVELOPPES}/appel-astra-juge-6-2-v1.sh", "82d028016cf0836a9ff031ec0d9f0d7ec62532994a1b90d966f57e289c11dd9f"),
        "commande": ("docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py",
                     "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71"),
        "relais": {"port": 8790, "cle_modeles": "modeles_permis"}, "controle_usd": 0.2,
        "fiches": "c75b5137bb79d63c6c68bf8b9ceba8b4d747e133ef91dcd6c0ddfa387d33e2f1", "consigne": "3f0c649ee848ab4a341f5bf8139b4e2e5f783d0b74affd4af3ee2a32152f5171", "delai_commande_s": "1800",
    },
    "argon": {
        "run": RUNS + "v14/20261118-110023-course-ideation-organismes-discrets-v14-argon",
        "etiquette": "argon-juge", "modele_course": "gemini-4-argon", "modele_joue": "gemini-4-argon",
        "enveloppe": (f"{ENVELOPPES}/appel-argon-v6.sh", "440127d646fb67d593a61bc29652d505a6ec0286de72256f9116986d8d449bbb"),
        "commande": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3e.py",
                     "e94ecd4693657bd2d8b086fbbc903bb77635b3b034e1eede50d630675c3f3fc6"),
        "relais": {"port": 8788, "cle_modeles": "modeles"}, "controle_usd": 0.6,
        "fiches": "17d2ddf39a583ccfb1b8080cb0f4b44a4004694752a8abb0bd81d8c9d82232ab", "consigne": "0601270c4a2c99f4911611890be76774190332d2ee196785640a6ee588c85c7f", "delai_commande_s": "1800",
    },
}

PLAFOND_JUGE_USD = 2.5            # plafond de la session du juge externe, celui déclaré par la course
PLANCHER_COMMANDE_USD = 1e-6      # coût plancher que rend une commande externe qui n'a rien envoyé


def pire_cas_usd(lignee: str) -> float:
    return round(PLAFOND_JUGE_USD + LIGNEES[lignee]["controle_usd"], 6)


PERIMETRE_COMMUN = ("organisme d'idéation", "organismes discrets", "juge externe")

NOMS_PERMIS = ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR")
NOMS_DE_CLE = (
    "ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN",
    "OPENAI_API_KEY", "GOOGLE_API_KEY", "GEMINI_API_KEY",
    "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "GITHUB_TOKEN", "GH_TOKEN", "HF_TOKEN",
)
MOTIF_NOM_DE_CLE = re.compile(r"(API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL)", re.I)
DRAPEAUX_INTERDITS = (
    "--accepter-sans-bac-a-sable", "--motif-sans-bac-a-sable",
    "--tolerer-somme-plafonds", "--tolerer-somme-plafonds-externe",
    "--taille-max-consigne-externe", "--taille-max-consigne-externe-bras",
    "--prix-entree-usd-par-million-jetons",
)
DRAPEAUX_CLAUDE_INTERDITS_EXACTS = (
    "--url-relais", "--confirmer-moteur-reel", "--seconde-passe",
    "--piece-juge", "--synthese",
)
MODELES_CLAUDE = ("claude-opus", "claude-fable", "claude-sonnet", "claude-haiku")
DOSSIER_SORTIES = Path("/home/user/sorties-bras-juge-ideation-organismes-discrets-v3")
RACINE_RUNS = DEPOT / "runs" / "bras-juge-ideation-organismes-discrets-v3"
SUFFIXE_RUN = "-bras-juge-ideation-organismes-discrets-v3-"
SONDE_BAC_A_SABLE = (
    "import json, sys\n"
    "sys.path.insert(0, sys.argv[1])\n"
    "from pole.adaptateurs import etat_bac_a_sable_detaille\n"
    "print(json.dumps(etat_bac_a_sable_detaille()))\n"
)
ORCHESTRATEUR = None   # fixé par `executer` (clone public ou orchestrateur assemblé) ; lu par la sonde du bac à sable


class Refus(RuntimeError):
    pass


def sha256_fichier(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def date_u() -> str:
    r = subprocess.run(["date", "-u"], capture_output=True, text=True, timeout=10)
    if r.returncode != 0 or not r.stdout.strip():
        raise Refus("`date -u` illisible")
    return r.stdout.strip()


def _normal(texte: str) -> str:
    return " ".join(unicodedata.normalize("NFC", texte).lower().replace("’", "'").split())


def _sans_accent(texte: str) -> str:
    return unicodedata.normalize("NFKD", texte.lower()).encode("ascii", "ignore").decode()


def lire_plafond_go(cellule: str) -> float:
    m = re.match(r"^\s*(\d+(?:[.,]\d+)?)\s*USD\b", cellule)
    if not m:
        raise Refus(f"plafond de la ligne de GO illisible : {cellule[:80]!r}")
    return float(m.group(1).replace(",", "."))


def verifier_go(registre: Path, aujourd_hui: _dt.date, lignee: str) -> dict:
    """Une seule ligne principale dont le périmètre porte les expressions communes et « lignée LIGNEE », aucune autre
    lignée ; 8 colonnes, type calcul, par Lazar, dans sa période, non révoquée, plafond ≥ pire cas."""
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    attendues = PERIMETRE_COMMUN + (f"lignée {lignee}",)
    ligne_go = re.compile(r"^\|\s*(GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2})\s*\|")
    lignes = []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = ligne_go.match(ligne)
        if m:
            lignes.append((m.group(1), [c.strip() for c in ligne.strip().strip("|").split("|")], ligne))
    candidates = [(i, c) for i, c, _ in lignes if len(c) == 8 and all(p in _normal(c[3]) for p in attendues)
                  and not c[3].lower().startswith("extension")]
    if len(candidates) != 1:
        raise Refus(f"{len(candidates)} ligne(s) principale(s) de GO dont le périmètre contient {list(attendues)} "
                    f"dans {registre.name} (une exigée)")
    go_id, c = candidates[0]
    autres = sorted(set(re.findall(r"lignée\s+(\w+)", _normal(c[3]))) - {lignee})
    if autres:
        raise Refus(f"{go_id} : le périmètre nomme aussi {['lignée ' + a for a in autres]} ; une ligne par lignée exigée")
    for i, cellules, brute in lignes:
        if i != go_id and go_id in brute:
            if len(cellules) != 8:
                raise Refus(f"ligne {i} qui cite {go_id} mal formée ({len(cellules)} colonnes) : lecture impossible")
            if _sans_accent(cellules[2]) == "revocation":
                raise Refus(f"{go_id} révoqué par {i}")
    if sum(1 for x in lignes if x[0] == go_id) != 1:
        raise Refus(f"{go_id} : plusieurs lignes à cet identifiant (une exigée)")
    ident, accorde, typ, perimetre, plafond, echeance, par, ref = c
    if typ != "calcul":
        raise Refus(f"{go_id} : type {typ!r}, « calcul » exigé")
    if par != "Lazar":
        raise Refus(f"{go_id} : accordé par {par!r}, Lazar exigé")
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        raise Refus(f"{go_id} : dates illisibles ({accorde!r}, {echeance!r})") from None
    if not d_acc <= aujourd_hui <= d_ech:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {d_ech}, aujourd'hui {aujourd_hui})")
    plafond_usd = lire_plafond_go(plafond)
    if plafond_usd < pire_cas_usd(lignee):
        raise Refus(f"{go_id} : plafond {plafond_usd} USD sous le pire cas du bras ({pire_cas_usd(lignee)} USD)")
    if LIGNEES[lignee]["modele_joue"] != LIGNEES[lignee]["modele_course"] and LIGNEES[lignee]["modele_joue"] not in perimetre:
        raise Refus(f"{go_id} : le périmètre ne nomme pas le modèle joué {LIGNEES[lignee]['modele_joue']!r} "
                    "(changement de modèle : la ligne doit le porter)")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "plafond": plafond, "plafond_usd": plafond_usd,
            "par": par, "ligne_sha256": hashlib.sha256(("|".join(c)).encode("utf-8")).hexdigest()}


def _git(dossier: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(dossier), *args], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        raise Refus(f"git {' '.join(args)} dans {dossier} : code {r.returncode} ({r.stderr.strip()[:200]})")
    return r.stdout


def verifier_piece(rel: str, attendu: str) -> dict:
    p = DEPOT / rel
    if not p.is_file():
        raise Refus(f"pièce absente : {rel}")
    lu = sha256_fichier(p)
    if lu != attendu:
        raise Refus(f"{rel} : empreinte {lu}, {attendu} épinglée")
    return {"chemin": rel, "sha256": lu}


def verifier_clone_public() -> dict:
    arbre = _git(CLONE_PUBLIC, "rev-parse", "HEAD:orchestrator").strip()
    if arbre != ARBRE_ORCHESTRATEUR:
        raise Refus(f"arbre de l'orchestrateur {arbre}, {ARBRE_ORCHESTRATEUR} exigé")
    sale = _git(CLONE_PUBLIC, "status", "--porcelain", "--untracked-files=all", "--ignored=matching", "--", "orchestrator").strip()
    if sale:
        raise Refus(f"clone public de l'orchestrateur modifié : {sale[:200]!r}")
    return {"chemin": str(CLONE_PUBLIC / "orchestrator"), "arbre": arbre, "commit": _git(CLONE_PUBLIC, "rev-parse", "HEAD").strip()}


def verifier_copies(lignee: str) -> dict:
    l = LIGNEES[lignee]
    copies = DEPOT / l["run"] / "copies"
    noms = {"fiches": "sortie--fiches-validees.json",
            "consigne": f"sortie--juges-bras-rapporte--traces-{l['etiquette']}--consigne-en-attente.md"}
    lues = {}
    for cle, nom in noms.items():
        p = copies / nom
        if not p.is_file() or not Path(str(p) + ".sha256").is_file():
            raise Refus(f"copie scellée absente : {l['run']}/copies/{nom}")
        lu = sha256_fichier(p)
        if lu != l[cle] or Path(str(p) + ".sha256").read_text(encoding="utf-8").split()[0] != lu:
            raise Refus(f"{nom} : empreinte {lu}, {l[cle]} épinglée (ou sceau faux)")
        lues[cle] = lu
    return lues


def chemin_attestation(lignee: str) -> Path:
    return DEPOT / "rapports" / "organismes-discrets-v1" / f"attestation-lecture-juge-{lignee}-v1.json"


def verifier_attestation(lignee: str) -> dict:
    l, chemin = LIGNEES[lignee], chemin_attestation(lignee)
    if not chemin.is_file():
        raise Refus(f"attestation de lecture absente : {chemin.relative_to(DEPOT)}")
    compagnon = Path(str(chemin) + ".sha256")
    lu = sha256_fichier(chemin)
    if not compagnon.is_file() or compagnon.read_text(encoding="utf-8").split()[0] != lu:
        raise Refus("attestation sans sceau, ou au sceau faux")
    att = json.loads(chemin.read_text(encoding="utf-8"))
    if not isinstance(att, dict) or set(att) != {"lecteur", "lu_le", "fiches_validees_sha256", "consignes_en_attente_sha256"}:
        raise Refus("attestation : champs lecteur, lu_le, fiches_validees_sha256, consignes_en_attente_sha256, ni plus ni moins")
    if att["lecteur"] != "Lazar":
        raise Refus(f"attestation : lecteur {att['lecteur']!r}, « Lazar » exigé")
    try:
        _dt.date.fromisoformat(att["lu_le"])
    except (TypeError, ValueError):
        raise Refus(f"attestation : lu_le {att['lu_le']!r} n'est pas une date ISO") from None
    if att["fiches_validees_sha256"] != l["fiches"]:
        raise Refus("attestation : empreinte des fiches validées différente de l'épinglée")
    if att["consignes_en_attente_sha256"] != {l["etiquette"]: l["consigne"]}:
        raise Refus("attestation : consigne en attente différente de l'épinglée")
    return {"chemin": str(chemin.relative_to(DEPOT)), "sha256": lu, "lecteur": att["lecteur"], "lu_le": att["lu_le"]}


def verifier_relais(lignee: str) -> dict:
    """Le relais du fournisseur répond sur la boucle locale et n'admet que le modèle joué (lu sur `GET /relais/etat`,
    sans mandataire). Un relais absent ou resté sur un autre modèle ferait échouer le contrôle du bras."""
    import urllib.request
    l = LIGNEES[lignee]
    url = f"http://127.0.0.1:{l['relais']['port']}/relais/etat"
    try:
        op = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        etat = json.loads(op.open(url, timeout=5).read())
    except Exception as e:  # noqa: BLE001
        raise Refus(f"relais de la lignée {lignee} injoignable ou illisible sur {url} ({type(e).__name__}) : rien ne part") from None
    modeles = etat.get(l["relais"]["cle_modeles"]) if isinstance(etat, dict) else None
    if modeles != [l["modele_joue"]]:
        raise Refus(f"relais de la lignée {lignee} : modèles admis {modeles!r}, [{l['modele_joue']!r}] exigé")
    return {"url": url, "modeles": modeles, "pid": etat.get("pid"), "version": etat.get("version")}


def _tentative_sans_envoi(chemin: Path) -> bool:
    try:
        j = json.loads(chemin.read_text(encoding="utf-8"))["reglages"]["journal"]
        cout = j["cout_total_usd"]
    except (OSError, ValueError, KeyError, TypeError):
        return False
    return (isinstance(cout, (int, float)) and not isinstance(cout, bool) and 0 <= cout <= PLANCHER_COMMANDE_USD
            and j.get("consigne_envoyee") is None)


def verifier_bras_jamais_joue(lignee: str) -> dict:
    """Un seul bras payé par lignée : le verrou « jamais rejoué après dépense » de l'orchestrateur vit dans le dossier de
    sortie, que chaque lancement recompose à neuf ; il est donc tenu ici, sur les runs du dépôt. Une relance n'est permise
    que si chaque run antérieur de cette lignée a un manifeste de fin lisible, sans échec du lanceur, de code 0, 2, 4 ou 5,
    et n'a ramené de l'orchestrateur que des manifestes « non joué » ou des tentatives au coût plancher sans consigne
    envoyée. Limite : le verrou vit dans `runs/` de ce clone ; un run non poussé n'est pas vu d'un autre clone."""
    anterieurs = sorted(d for d in RACINE_RUNS.glob(f"*{SUFFIXE_RUN}{lignee}") if d.is_dir()) if RACINE_RUNS.is_dir() else []
    for d in anterieurs:
        try:
            fin = json.loads((d / "manifeste-lanceur-fin.json").read_text(encoding="utf-8"))
            copies, code, echec = fin["copies"], fin["code"], fin["echec_lanceur"]
        except (OSError, ValueError, KeyError, TypeError):
            raise Refus(f"run antérieur {d.name} sans manifeste de fin lisible : état du bras inconnu, aucune relance") from None
        if echec is not None or code not in (0, 2, 4, 5):
            raise Refus(f"run antérieur {d.name} : code {code!r}, échec du lanceur {echec!r} : état du bras inconnu, aucune "
                        "relance sans un mot de Lazar et un lanceur neuf")
        payes = []
        for c in sorted(copies):
            if c.startswith("lanceur/") or re.fullmatch(r"manifeste-bras-non-joue-[0-9]+\.json", c):
                continue
            if re.fullmatch(r"bras-tentative-[0-9]+\.json", c) and _tentative_sans_envoi(d / "copies" / ("sortie--" + c)):
                continue
            payes.append(c)
        if payes:
            raise Refus(f"le bras de la lignée {lignee} a déjà été joué ou tenté avec dépense ({d.name} : {payes[:4]}) : "
                        "jamais rejoué sans un mot de Lazar et un lanceur neuf")
    return {"runs_anterieurs_sans_envoi": [d.name for d in anterieurs]}


def commande_bras(lignee: str, orchestrateur: Path, sortie: Path, horodatage: str, go_id: str) -> list:
    l = LIGNEES[lignee]
    enveloppe = str(DEPOT / l["enveloppe"][0])
    if any(ch.isspace() for ch in enveloppe + str(sortie)):
        raise Refus("chemin avec espace")
    remplace = l["modele_joue"] != l["modele_course"]
    argv = [PYTHON, "-I", "-B", "demonstrations/ideation_v9.py" if remplace else "demonstrations/ideation_v8.py", str(sortie),
            "--bras-rapporte-differe",
            "--attestation-lecture-humaine", str(chemin_attestation(lignee)),
            "--juge-externe", f"{l['etiquette']}={l['modele_joue']}",
            "--commande-externe", "bash " + enveloppe,
            "--delai-commande-s", l["delai_commande_s"],
            "--budget", f"juge_ideation|{l['modele_joue']}={PLAFOND_JUGE_USD!r}",
            "--budget-controle-usd", repr(l["controle_usd"]),
            "--moteur", "claude-sdk", "--modele-commande-externe", l["modele_joue"], "--commande-externe-lit-modele",
            "--horodatage", horodatage]
    if remplace:
        argv += ["--remplacement-modele-juge", f"{l['etiquette']}={l['modele_course']}={l['modele_joue']}={go_id}",
                 "--mot-remplacement", f"{l['etiquette']}={l['mot']}"]
    return argv


def garde_drapeaux(argv: list) -> None:
    for jeton in argv:
        if not isinstance(jeton, str) or not jeton.startswith("--") or len(jeton) <= 2:
            continue
        nom = jeton.split("=", 1)[0]
        if any(f == nom or f.startswith(nom) for f in DRAPEAUX_INTERDITS):
            raise Refus(f"drapeau interdit : {jeton}")
        elif nom in DRAPEAUX_CLAUDE_INTERDITS_EXACTS:
            raise Refus(f"drapeau interdit : {jeton}")


def garde_modeles_claude(argv: list) -> None:
    for option in ("--juge-externe", "--juge"):
        for i, jeton in enumerate(argv):
            if jeton == option and i + 1 < len(argv):
                valeur = argv[i + 1]
                modele = valeur.split("=", 1)[1] if "=" in valeur else valeur
                if any(m in modele.lower() for m in MODELES_CLAUDE):
                    raise Refus(f"modèle Claude interdit dans {option} : {valeur!r}")


def environnement_filtre(env: dict) -> tuple:
    retires = sorted(n for n in env if n in NOMS_DE_CLE or MOTIF_NOM_DE_CLE.search(n))
    noms_hors_liste = sorted(n for n in env if n not in NOMS_PERMIS and n not in retires)
    garde = {n: env[n] for n in env if n in NOMS_PERMIS}
    garde["HOME"] = str(DOSSIER_SORTIES)
    garde["PYTHONPYCACHEPREFIX"] = str(DOSSIER_SORTIES / "pycache")
    return garde, retires, noms_hors_liste


def sonder_bac_a_sable(env: dict) -> dict:
    try:
        p = subprocess.run([sys.executable, "-I", "-B", "-c", SONDE_BAC_A_SABLE, str(ORCHESTRATEUR)],
                           cwd=str(ORCHESTRATEUR), env=env, capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"sonde du bac à sable non exécutée ({type(e).__name__})") from None
    lignes = [x for x in p.stdout.splitlines() if x.strip()]
    try:
        etat = json.loads(lignes[-1]) if p.returncode == 0 and lignes else None
    except json.JSONDecodeError:
        etat = None
    if not (isinstance(etat, dict) and isinstance(etat.get("actif"), bool) and isinstance(etat.get("proc_neuf"), bool)):
        raise Refus(f"sonde du bac à sable illisible (code {p.returncode}) : {p.stderr.strip()[-500:]!r}")
    if not etat["actif"]:
        raise Refus("bac à sable inactif : " + str(etat.get("motif")))
    if not etat["proc_neuf"]:
        raise Refus("bac à sable sans /proc neuf : " + str(etat.get("motif")))
    return etat


def ecrire_scelle(chemin: Path, contenu: dict) -> str:
    if chemin.exists():
        raise Refus(f"{chemin} existe déjà (R12)")
    donnees = (json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {chemin.name}\n")
    return h


def _depot_git() -> dict:
    try:
        return {"commit": _git(DEPOT, "rev-parse", "HEAD").strip(),
                "arbre_modifie": bool(_git(DEPOT, "status", "--porcelain", "--untracked-files=no").strip())}
    except Refus as e:
        return {"commit": None, "erreur": str(e)}


def _jouer(argv: list, **kw) -> subprocess.CompletedProcess:
    return subprocess.run(argv, capture_output=True, text=True, timeout=600, **kw)


def copier_resultats(sortie: Path, avant: set, dest: Path) -> dict:
    """Copie scellée, dans le dépôt, de tout fichier que le bras a écrit dans la sortie (hors compagnons)."""
    dest.mkdir(parents=True, exist_ok=True)
    copies = {}
    for p in sorted(sortie.rglob("*")):
        rel = p.relative_to(sortie).as_posix()
        if not p.is_file() or rel in avant or rel.endswith(".sha256") or "__pycache__" in rel:
            continue
        nom = "sortie--" + rel.replace("/", "--")
        octets = p.read_bytes()
        (dest / nom).write_bytes(octets)
        h = hashlib.sha256(octets).hexdigest()
        (dest / (nom + ".sha256")).write_text(f"{h}  {nom}\n", encoding="utf-8")
        copies[rel] = h
    return copies


def executer(lignee: str) -> int:
    l = LIGNEES[lignee]
    env_lu = dict(os.environ)
    aujourd_hui = _dt.datetime.now(_dt.timezone.utc).date()
    if os.path.abspath(sys.executable) != PYTHON:
        raise Refus(f"lanceur exécuté par {sys.executable}, {PYTHON} exigé")
    remplace = l["modele_joue"] != l["modele_course"]

    pieces = {"enveloppe": verifier_piece(*l["enveloppe"]), "commande": verifier_piece(*l["commande"]),
              "recomposeur": verifier_piece(*RECOMPOSEUR)}
    clone = verifier_clone_public()
    if remplace:
        pieces["assembleur"] = verifier_piece(*ASSEMBLEUR)
        base = "docs/notes/relance-organismes-discrets-v1/orchestrateur-remplacement-juge-v2/"
        pieces["ajouts"] = [verifier_piece(base + rel, h) for rel, h in sorted(AJOUTS_REMPLACEMENT.items())]
    copies = verifier_copies(lignee)
    print(json.dumps({"gardes_passees": "pièces, orchestrateur, copies scellées de la course", "lignee": lignee}, ensure_ascii=False),
          flush=True)
    go = verifier_go(DEPOT / "registres" / "go.md", aujourd_hui, lignee)
    att = verifier_attestation(lignee)
    anterieurs = verifier_bras_jamais_joue(lignee)
    relais = verifier_relais(lignee)
    RACINE_RUNS.mkdir(parents=True, exist_ok=True)
    verrou = RACINE_RUNS / f"verrou-lancement-{lignee}"
    try:
        verrou.mkdir()
    except FileExistsError:
        raise Refus(f"un lancement du bras de la lignée {lignee} est en cours ou s'est interrompu ({verrou.name} existe) : "
                    "vérifier qu'aucun processus ne tourne, puis retirer ce dossier à la main") from None
    try:
        return _lancer(lignee, l, remplace, pieces, clone, copies, go, att, anterieurs, relais, env_lu)
    finally:
        verrou.rmdir()


def _lancer(lignee, l, remplace, pieces, clone, copies, go, att, anterieurs, relais, env_lu) -> int:
    global ORCHESTRATEUR

    horodatage = date_u()
    ident = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%d-%H%M%S") + SUFFIXE_RUN + lignee
    dossier_run = RACINE_RUNS / ident
    dossier_sortie = DOSSIER_SORTIES / ident
    if dossier_run.exists() or dossier_sortie.exists():
        raise Refus(f"{dossier_run} ou {dossier_sortie} existe déjà (R12)")
    dossier_sortie.mkdir(parents=True)

    r = _jouer([PYTHON, "-I", "-B", str(DEPOT / RECOMPOSEUR[0]), str(DEPOT / l["run"]), str(dossier_sortie / "course")])
    if r.returncode != 0:
        raise Refus(f"recomposition de la course refusée : {r.stdout.strip()[-300:]} {r.stderr.strip()[-300:]}")
    sortie = dossier_sortie / "course" / "sortie"
    if sha256_fichier(sortie / "fiches-validees.json") != l["fiches"] or sha256_fichier(
            sortie / "juges-bras-rapporte" / f"traces-{l['etiquette']}" / "consigne-en-attente.md") != l["consigne"]:
        raise Refus("course recomposée : fiches validées ou consigne en attente différentes des épinglées")
    if remplace:
        r = _jouer([PYTHON, "-I", "-B", str(DEPOT / ASSEMBLEUR[0]), str(dossier_sortie / "orchestrateur")])
        if r.returncode != 0:
            raise Refus(f"assemblage de l'orchestrateur refusé : {r.stdout.strip()[-300:]} {r.stderr.strip()[-300:]}")
        ORCHESTRATEUR = dossier_sortie / "orchestrateur" / "orchestrator"
        for rel, h in AJOUTS_REMPLACEMENT.items():
            if sha256_fichier(ORCHESTRATEUR / rel) != h:
                raise Refus(f"orchestrateur assemblé : {rel} à l'empreinte fausse")
    else:
        ORCHESTRATEUR = CLONE_PUBLIC / "orchestrator"
    orch = {"chemin": str(ORCHESTRATEUR), "clone_public": clone, "ajouts": AJOUTS_REMPLACEMENT if remplace else None}

    argv = commande_bras(lignee, ORCHESTRATEUR, sortie, horodatage, go["id"])
    garde_drapeaux(argv)
    garde_modeles_claude(argv)
    env, retires, exclus = environnement_filtre(env_lu)
    env["GO_ID"] = go["id"]
    try:   # informative : le bras lance la commande externe sans bac à sable (v3, contre-lecture, constat 4)
        bac = sonder_bac_a_sable(env)
    except Refus as e:
        bac = {"informatif": True, "sonde": str(e)}
    avant = {p.relative_to(sortie).as_posix() for p in sortie.rglob("*") if p.is_file()}

    dossier_run.mkdir(parents=True)
    depart = {
        "lanceur": {"version": VERSION, "chemin": str(Path(__file__).resolve()), "sha256": sha256_fichier(Path(__file__))},
        "horodatage_canonique": horodatage, "id": ident, "lignee": lignee, "go": go,
        "juge": {"etiquette": l["etiquette"], "modele_course": l["modele_course"], "modele_joue": l["modele_joue"],
                 "remplacement_declare": remplace, "mot": l.get("mot")},
        "orchestrateur": orch, "pieces": pieces, "course": {"run": l["run"], "sortie_recomposee": str(sortie), **copies},
        "attestation": att,
        "bras_anterieurs": anterieurs, "relais": relais,
        "budgets": {"plafond_juge_usd": PLAFOND_JUGE_USD, "budget_controle_usd": l["controle_usd"], "pire_cas_usd": pire_cas_usd(lignee),
                    "plafond_externe": "celui de la course (manifeste de départ), relu par le bras"},
        "commande": argv, "cwd": str(ORCHESTRATEUR), "bac_a_sable": bac,
        "cles": {"noms_retires": retires, "valeurs": "jamais lues"},
        "depot_travail": _depot_git(),
        "journaux": {"stdout": str(dossier_sortie / "bras.stdout.txt"), "stderr": str(dossier_sortie / "bras.stderr.txt")},
    }
    h_depart = ecrire_scelle(dossier_run / "manifeste-lanceur-depart.json", depart)
    print(json.dumps({"manifeste_depart": str(dossier_run / "manifeste-lanceur-depart.json"), "sha256": h_depart},
                     ensure_ascii=False), flush=True)

    code, pid, echec = None, None, None
    debut = _dt.datetime.now(_dt.timezone.utc)
    try:
        with open(dossier_sortie / "bras.stdout.txt", "xb") as fo, open(dossier_sortie / "bras.stderr.txt", "xb") as fe:
            enfant = subprocess.Popen(argv, cwd=str(ORCHESTRATEUR), env=env, stdout=fo, stderr=fe)
            pid = enfant.pid

            def relayer(num, _cadre):
                try:
                    enfant.send_signal(num)
                except ProcessLookupError:
                    pass
            anciens = {s: signal.signal(s, relayer) for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP)}
            try:
                code = enfant.wait()
            finally:
                for s, a in anciens.items():
                    signal.signal(s, a)
    except BaseException as exc:  # noqa: BLE001 — le manifeste de fin et les copies s'écrivent sur tous les chemins
        echec = exc
    fin = _dt.datetime.now(_dt.timezone.utc)
    bilan = {"id": ident, "lignee": lignee, "manifeste_depart_sha256": h_depart, "pid_orchestrateur": pid, "code": code,
             "echec_lanceur": f"{type(echec).__name__}: {echec}" if echec else None,
             "debut_utc": debut.isoformat(), "fin_utc": fin.isoformat()}
    try:
        bilan["copies"] = copier_resultats(sortie, avant, dossier_run / "copies")
        for nom, source in (("bras.stdout.txt", dossier_sortie / "bras.stdout.txt"), ("bras.stderr.txt", dossier_sortie / "bras.stderr.txt"),
                            ("RECOMPOSITION.json", dossier_sortie / "course" / "RECOMPOSITION.json")):
            if source.is_file():
                octets = source.read_bytes()
                (dossier_run / "copies" / ("lanceur--" + nom)).write_bytes(octets)
                h = hashlib.sha256(octets).hexdigest()
                (dossier_run / "copies" / ("lanceur--" + nom + ".sha256")).write_text(f"{h}  lanceur--{nom}\n", encoding="utf-8")
                bilan["copies"]["lanceur/" + nom] = h
        bilan["journaux_sha256"] = {n: sha256_fichier(dossier_sortie / n) for n in ("bras.stdout.txt", "bras.stderr.txt")
                                    if (dossier_sortie / n).is_file()}
    except Exception as e:  # noqa: BLE001
        bilan["echec_copies"] = f"{type(e).__name__}: {e}"
    h_fin = ecrire_scelle(dossier_run / "manifeste-lanceur-fin.json", bilan)
    print(json.dumps({"manifeste_fin": str(dossier_run / "manifeste-lanceur-fin.json"), "sha256": h_fin, "code": code,
                      "copies": len(bilan.get("copies", {}))}, ensure_ascii=False), flush=True)
    if echec is not None:
        raise echec
    return code


def principal(argv: list | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) != 1 or argv[0] not in LIGNEES:
        print(json.dumps({"refus": f"un seul argument, une lignée parmi {sorted(LIGNEES)} (reçu {argv!r})"},
                         ensure_ascii=False), file=sys.stderr)
        return 2
    try:
        return executer(argv[0])
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001
        print(json.dumps({"erreur": f"{type(e).__name__}: {e}"}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(principal())
