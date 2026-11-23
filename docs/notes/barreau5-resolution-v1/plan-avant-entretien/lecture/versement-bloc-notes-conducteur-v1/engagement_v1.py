"""Engagement par empreinte des étiquettes des adaptateurs tenus à l'écart (barreau 5 ; texte, « Plan d'analyse », point 7 ;
« Liste d'arrêt », points 8 et 9 ; « Lignes de registre »). Code neuf (R12).

- *sel* : 256 bits tirés par l'aléa du système (`secrets`), exception déclarée à R9 (un secret ne se dérive pas d'une
  graine publiée) ;
- *noms opaques* : `X-01` à `X-30` (préfixe du couple m-4b de la contre-lecture ; `E-` au brouillon 2), dans l'ordre des
  HMAC-SHA256 du sel sur « famille/membre » : ordre tiré, et vérifiable par qui reçoit le sel ;
- *table des étiquettes* : (nom opaque, famille, membre, sel), une ligne par adaptateur tenu à l'écart ; *empreinte* :
  sha256 de sa forme canonique ;
- *registre propre* `registres/barreau5-familles-jumelles-v1.md` : lignes « | CLÉ | instant UTC | contenu | référence | »,
  ajoutées, jamais réécrites ; une clé n'y figure qu'une fois ;
- *vérifications* : engagement présent, antérieur à la création de l'instance de lecture, empreinte égale (avant la
  lecture) ; et à l'ouverture : empreinte égale, dates qui se suivent (engagement, scores, ouverture) ; le registre peut être
  lu tel qu'à un commit (`lignes_au_commit`, constat m-11 : le code de lecture lit le registre au commit de sa course, comme
  le lanceur de formation) ;
- *entrées de lecture* (texte, point 7, deuxième tiret) : adaptateurs tenus à l'écart réécrits sous leur nom opaque, réduits
  aux seuls tenseurs (`safetensors`, sans métadonnée), dans l'ordre des noms (couple m-12b) ; adaptateurs d'apprentissage
  étiquetés ; épisodes d'évaluation des saboteurs d'apprentissage, copiés à l'octet sous `A<k>-saboteur-evaluation.jsonl`
  (constat M-8) ; aucun autre fichier admis dans le dossier.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import re
import secrets
from datetime import datetime, timezone
from pathlib import Path

from ..gardes import GardeArret
from ..scellement import sceller, verifier

PREFIXE_NOMS = "X"
REGISTRE_PROPRE = "registres/barreau5-familles-jumelles-v1.md"
# clés du texte (« Lignes de registre »), plus GO-RELANCE-FORMATION-B5F (relance unique d'une instance tombée, constat
# M-5 ; clé à ajouter au texte)
CLES_REGISTRE = ("SCELLEMENT-B5F", "CODE-FORMATION-B5F", "GO-FORMATION-B5F", "GO-RELANCE-FORMATION-B5F",
                 "SORTIES-FORMATION-B5F", "ENGAGEMENT-B5F", "CODE-LECTURE-B5F", "EPREUVE-B5F", "GO-LECTURE-B5F",
                 "SCORES-B5F", "OUVERTURE-B5F", "LECTURE-B5F", "VERDICT-B5F")
_FAMILLE_APPRENTISSAGE = re.compile(r"A[0-9]+")
_LIGNE = re.compile(r"^\|\s*(?P<cle>[A-Z0-9-]+-B5F)\s*\|\s*(?P<instant>[^|]*?)\s*\|\s*(?P<contenu>[^|]*?)\s*\|"
                    r"\s*(?P<ref>[^|]*?)\s*\|\s*$")
_INSTANT = "%Y-%m-%dT%H:%M:%SZ"
_SEL = re.compile(r"^[0-9a-f]{64}$")


def maintenant_utc() -> str:
    return datetime.now(timezone.utc).strftime(_INSTANT)


def lire_instant(texte: str) -> datetime:
    try:
        return datetime.strptime(texte.strip(), _INSTANT).replace(tzinfo=timezone.utc)
    except ValueError:
        raise GardeArret(f"instant {texte!r} illisible (AAAA-MM-JJTHH:MM:SSZ attendu)") from None


def tirer_sel() -> str:
    return secrets.token_bytes(32).hex()


def _exiger_sel(sel: str) -> None:
    if not isinstance(sel, str) or not _SEL.match(sel):
        raise GardeArret("sel : 64 signes hexadécimaux (256 bits) attendus")


def noms_opaques(sel: str, adaptateurs, prefixe: str = PREFIXE_NOMS) -> dict[tuple[str, str], str]:
    """(famille, membre) → nom opaque, dans l'ordre des HMAC-SHA256 du sel."""
    _exiger_sel(sel)
    adaptateurs = [tuple(a) for a in adaptateurs]
    if len(set(adaptateurs)) != len(adaptateurs) or not adaptateurs:
        raise GardeArret("adaptateurs en double ou liste vide")
    if len(adaptateurs) > 99:
        raise GardeArret("au plus 99 noms opaques")
    cle = bytes.fromhex(sel)
    ordre = sorted(adaptateurs, key=lambda a: hmac.new(cle, f"{a[0]}/{a[1]}".encode("utf-8"), hashlib.sha256).hexdigest())
    return {a: f"{prefixe}-{k + 1:02d}" for k, a in enumerate(ordre)}


def table_des_etiquettes(sel: str, adaptateurs, prefixe: str = PREFIXE_NOMS) -> list[dict]:
    noms = noms_opaques(sel, adaptateurs, prefixe)
    return sorted(({"nom": n, "famille": f, "membre": m, "sel": sel} for (f, m), n in noms.items()), key=lambda x: x["nom"])


def forme_canonique(table: list[dict]) -> bytes:
    return json.dumps(table, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def empreinte_table(table: list[dict]) -> str:
    return hashlib.sha256(forme_canonique(table)).hexdigest()


def exiger_table_coherente(table: list[dict], prefixe: str = PREFIXE_NOMS) -> None:
    """Un seul sel, et des noms qui se redérivent du sel (une table retouchée à la main est refusée)."""
    if not table:
        raise GardeArret("table des étiquettes vide")
    sels = {x.get("sel") for x in table}
    if len(sels) != 1:
        raise GardeArret("table des étiquettes : plusieurs sels")
    sel = sels.pop()
    attendus = noms_opaques(sel, [(x["famille"], x["membre"]) for x in table], prefixe)
    if any(attendus[(x["famille"], x["membre"])] != x["nom"] for x in table):
        raise GardeArret("table des étiquettes : noms opaques qui ne se dérivent pas du sel")


def ecrire_table(chemin: Path, table: list[dict]) -> str:
    """Écrit la table sous sa forme canonique et la scelle ; rend l'empreinte (R12 : jamais écrasée)."""
    chemin = Path(chemin)
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    exiger_table_coherente(table)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_bytes(forme_canonique(table))
    sha = sceller(chemin)
    if sha != empreinte_table(table):
        raise GardeArret("empreinte du fichier de la table ≠ empreinte de sa forme canonique")
    return sha


def lire_table(chemin: Path) -> list[dict]:
    verifier(chemin)
    table = json.loads(Path(chemin).read_text(encoding="utf-8"))
    exiger_table_coherente(table)
    return table


# --- registre propre ----------------------------------------------------------------------------------------------------

def lignes_du_registre(texte: str) -> dict[str, dict]:
    """Lignes à clé du registre propre ; une clé en double ou inconnue arrête (aucune ligne n'est réécrite)."""
    sortie = {}
    for n, ligne in enumerate(texte.splitlines(), 1):
        if not ligne.lstrip().startswith("|") or "-B5F" not in ligne:
            continue
        m = _LIGNE.match(ligne.strip())
        if m is None:
            raise GardeArret(f"registre propre, ligne {n} : « | CLÉ | instant | contenu | référence | » attendu")
        cle = m["cle"]
        if cle not in CLES_REGISTRE:
            raise GardeArret(f"registre propre, ligne {n} : clé {cle} inconnue")
        if cle in sortie:
            raise GardeArret(f"registre propre : clé {cle} en double (lignes {sortie[cle]['ligne']} et {n})")
        sortie[cle] = {"instant": lire_instant(m["instant"]), "contenu": m["contenu"], "ref": m["ref"], "ligne": n}
    return sortie


def lire_registre(chemin: Path) -> dict[str, dict]:
    chemin = Path(chemin)
    if not chemin.is_file():
        raise GardeArret(f"registre propre {chemin} absent")
    return lignes_du_registre(chemin.read_text(encoding="utf-8"))


def lignes_au_commit(racine: Path, commit: str) -> dict[str, dict]:
    """Lignes du registre propre telles qu'au commit donné (constat m-11), jamais celles de l'arbre de travail."""
    import subprocess

    if not re.fullmatch(r"[0-9a-f]{40}", str(commit)):
        raise GardeArret("commit (40 signes) attendu")
    vu = subprocess.run(["git", "-C", str(racine), "show", f"{commit}:{REGISTRE_PROPRE}"], capture_output=True, text=True)
    if vu.returncode != 0:
        raise GardeArret(f"registre propre absent du commit {commit[:12]}")
    return lignes_du_registre(vu.stdout)


def ligne_du_registre(cle: str, instant: str, contenu: str, ref: str) -> str:
    if cle not in CLES_REGISTRE:
        raise GardeArret(f"clé {cle} inconnue")
    lire_instant(instant)
    if any("|" in x or "\n" in x for x in (contenu, ref)):
        raise GardeArret("contenu ou référence : ni « | » ni saut de ligne")
    return f"| {cle} | {instant} | {contenu} | {ref} |"


def ligne_engagement(table: list[dict], instant: str, ref: str = "") -> str:
    exiger_table_coherente(table)
    return ligne_du_registre("ENGAGEMENT-B5F", instant, f"sha256 {empreinte_table(table)}", ref)


def _empreinte_engagee(lignes: dict) -> str:
    if "ENGAGEMENT-B5F" not in lignes:
        raise GardeArret("engagement absent du registre propre (liste d'arrêt, point 9)")
    m = re.fullmatch(r"sha256 ([0-9a-f]{64})", lignes["ENGAGEMENT-B5F"]["contenu"])
    if m is None:
        raise GardeArret("ligne ENGAGEMENT-B5F : « sha256 <64 signes> » attendu")
    return m.group(1)


def verifier_engagement_avant_lecture(registre: Path | None, creation_instance_lecture: str,
                                      lignes: dict | None = None) -> dict:
    """Avant la création de l'instance de lecture : engagement présent, d'instant strictement antérieur. `lignes` : le
    registre lu à un commit (`lignes_au_commit`), à la place du fichier."""
    lignes = lire_registre(registre) if lignes is None else lignes
    sha = _empreinte_engagee(lignes)
    creation = lire_instant(creation_instance_lecture)
    if not lignes["ENGAGEMENT-B5F"]["instant"] < creation:
        raise GardeArret("engagement postérieur (ou simultané) à la création de l'instance de lecture : refus, nœud")
    return {"empreinte": sha, "instant": lignes["ENGAGEMENT-B5F"]["instant"].strftime(_INSTANT)}


def verifier_table_a_l_ouverture(table: list[dict], registre: Path | None, ouverture: str,
                                 lignes: dict | None = None) -> dict:
    """À l'ouverture : empreinte de la table égale à l'engagement ; engagement < scores < ouverture. `lignes` : le
    registre lu à un commit (`lignes_au_commit`), à la place du fichier."""
    exiger_table_coherente(table)
    lignes = lire_registre(registre) if lignes is None else lignes
    sha = _empreinte_engagee(lignes)
    if empreinte_table(table) != sha:
        raise GardeArret("empreinte de la table différente de l'engagement : refus de la lecture, nœud")
    if "SCORES-B5F" not in lignes:
        raise GardeArret("ligne SCORES-B5F absente : scores non scellés avant l'ouverture")
    t_e, t_s, t_o = lignes["ENGAGEMENT-B5F"]["instant"], lignes["SCORES-B5F"]["instant"], lire_instant(ouverture)
    if not (t_e < t_s < t_o):
        raise GardeArret("dates hors d'ordre : engagement, scores, ouverture attendus dans cet ordre")
    return {"empreinte": sha, "adaptateurs": len(table)}


# --- entrées de la session de lecture -----------------------------------------------------------------------------------

def exiger_episodes_de_saboteur(famille: str, membre: str, chemin: Path) -> bytes:
    """Constat M-8 : seuls les épisodes d'évaluation du saboteur d'une famille d'apprentissage entrent dans la lecture.
    Le fichier est `evaluation-saboteur.jsonl` de la formation, vérifié par son compagnon d'empreinte ; chacune de ses
    lignes est un épisode du saboteur de cette famille (nom de formation : suffixes de relance et de retirage admis). Rend
    ses octets."""
    if not _FAMILLE_APPRENTISSAGE.fullmatch(str(famille)):
        raise GardeArret(f"épisodes d'évaluation hors des familles d'apprentissage : {famille}")
    if membre != "saboteur":
        raise GardeArret(f"épisodes d'évaluation de {famille}/{membre} : seuls ceux du saboteur entrent dans la lecture")
    chemin = Path(chemin)
    if chemin.name != "evaluation-saboteur.jsonl":
        raise GardeArret(f"{chemin.name} : evaluation-saboteur.jsonl attendu")
    verifier(chemin)
    octets = chemin.read_bytes()
    # découpe sur « \n » seulement : un texte du modèle peut porter U+2028 ou U+0085, que `json.dumps` (ensure_ascii=False)
    # laisse tels quels et que `splitlines` couperait au milieu d'une ligne
    lignes = [json.loads(x) for x in octets.decode("utf-8").split("\n") if x.strip()]
    if not lignes:
        raise GardeArret(f"{chemin} : aucun épisode")
    nom = re.compile(rf"{re.escape(famille)}(?:-x1)?(?:-r1)?")
    for x in lignes:
        if x.get("membre") != "saboteur" or not nom.fullmatch(str(x.get("famille", ""))):
            raise GardeArret(f"{chemin} : une ligne de {x.get('famille')}/{x.get('membre')}, pas du saboteur de {famille}")
    return octets


def preparer_entrees_de_lecture(adaptateurs: dict, table: list[dict], dossier: Path, etiquetes: dict | None = None,
                                episodes: dict | None = None) -> dict:
    """Écrit les adaptateurs tenus à l'écart sous leur nom opaque (`X-NN.safetensors`, tenseurs seuls, dans l'ordre des
    noms) et, le cas échéant, les adaptateurs d'apprentissage étiquetés (`A1-saboteur.safetensors`) et les épisodes
    d'évaluation des saboteurs d'apprentissage (`episodes` : (famille, membre) → `evaluation-saboteur.jsonl` de la
    formation ; copie à l'octet sous `A1-saboteur-evaluation.jsonl`, scellée ; constat M-8). `adaptateurs` : (famille,
    membre) → état (dictionnaire de tenseurs) ; tout adaptateur tenu à l'écart absent de la table, ou l'inverse, arrête.
    Rend nom de fichier → empreinte."""
    exiger_table_coherente(table)
    from safetensors.torch import save_file

    dossier = Path(dossier)
    if dossier.exists():
        raise GardeArret(f"{dossier} existe déjà (R12)")
    par_cle = {(x["famille"], x["membre"]): x["nom"] for x in table}
    if set(par_cle) != {tuple(k) for k in adaptateurs}:
        raise GardeArret("adaptateurs tenus à l'écart ≠ lignes de la table des étiquettes")
    copies = {(f, m): exiger_episodes_de_saboteur(f, m, p) for (f, m), p in sorted((episodes or {}).items())}
    dossier.mkdir(parents=True)
    sortie = {}
    for cle, nom in sorted(par_cle.items(), key=lambda kv: kv[1]):
        etat = {k: v.detach().to("cpu").contiguous() for k, v in sorted(adaptateurs[cle].items())}
        chemin = dossier / f"{nom}.safetensors"
        save_file(etat, str(chemin))
        sortie[chemin.name] = sceller(chemin)
    for (famille, membre), etat in sorted((etiquetes or {}).items()):
        if not _FAMILLE_APPRENTISSAGE.fullmatch(famille):
            raise GardeArret(f"adaptateur étiqueté hors des familles d'apprentissage : {famille}")
        chemin = dossier / f"{famille}-{membre}.safetensors"
        save_file({k: v.detach().to("cpu").contiguous() for k, v in sorted(etat.items())}, str(chemin))
        sortie[chemin.name] = sceller(chemin)
    for (famille, membre), octets in copies.items():
        chemin = dossier / f"{famille}-{membre}-evaluation.jsonl"
        chemin.write_bytes(octets)
        sortie[chemin.name] = sceller(chemin)
    exiger_entrees_de_lecture_propres(dossier, [x["nom"] for x in table], list(etiquetes or {}), list(copies))
    return sortie


def exiger_entrees_de_lecture_propres(dossier: Path, noms: list[str], etiquetes, episodes=()) -> None:
    """Le dossier des entrées de lecture ne contient que les fichiers attendus et leurs empreintes (aucune table, aucun
    coût d'un adaptateur tenu à l'écart, aucun journal de la formation) : adaptateurs sous leur nom opaque, adaptateurs
    d'apprentissage étiquetés, épisodes d'évaluation des saboteurs d'apprentissage (`A<k>-saboteur-evaluation.jsonl`)."""
    for f, m in episodes:
        if not _FAMILLE_APPRENTISSAGE.fullmatch(str(f)) or m != "saboteur":
            raise GardeArret(f"entrées de lecture : épisodes de {f}/{m} non admis (saboteurs d'apprentissage seulement)")
    attendus = {f"{n}.safetensors" for n in noms} | {f"{f}-{m}.safetensors" for f, m in etiquetes}
    attendus |= {f"{f}-{m}-evaluation.jsonl" for f, m in episodes}
    attendus |= {f"{x}.sha256" for x in attendus}
    presents = {p.relative_to(dossier).as_posix() for p in Path(dossier).rglob("*") if p.is_file()}
    intrus = sorted(presents - attendus)
    if intrus:
        raise GardeArret(f"entrées de lecture : fichiers non admis {intrus[:5]}")
    manquants = sorted(attendus - presents)
    if manquants:
        raise GardeArret(f"entrées de lecture : fichiers manquants {manquants[:5]}")


def charger_entree(chemin: Path) -> dict:
    from safetensors.torch import load_file

    verifier(chemin)
    return dict(load_file(str(chemin)))


__all__ = ["tirer_sel", "noms_opaques", "table_des_etiquettes", "empreinte_table", "ecrire_table", "lire_table",
           "lire_registre", "lignes_au_commit", "ligne_du_registre", "ligne_engagement",
           "verifier_engagement_avant_lecture", "verifier_table_a_l_ouverture", "exiger_episodes_de_saboteur",
           "preparer_entrees_de_lecture", "exiger_entrees_de_lecture_propres", "charger_entree", "maintenant_utc"]
