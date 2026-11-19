"""Compare les marqueurs écrits dans l'ordre exploratoire du saboteur à budget (ii-b) à ceux que porte la
configuration du commit de lancement — v1. EXPLORATOIRE, NON OPPOSABLE (R-522).

Usage (depuis n'importe où dans le dépôt) :
    python3 -I -B brouillons/ii-b-saboteur-budget-v1/comparer-marqueurs-ordre-configuration-ii-b-v1.py ORDRE

Ce que fait ce programme, et rien d'autre :
A. il lit la configuration par `git show COMMIT:CHEMIN` (jamais un fichier de l'arbre de travail), recalcule son
   empreinte et la compare à l'empreinte attendue ; il vérifie que le commit de lancement a pour parent direct le
   commit du code que la configuration nomme et qu'il n'ajoute que la configuration et son sceau ; il croise
   quelques clés de la configuration avec ses propres marqueurs ;
B. pour chacun des 30 marqueurs de la configuration, il compare la valeur écrite dans l'ordre (table « valeurs à
   l'octet » du § 11, bloc du marqueur des empreintes du code, places de l'extrait de la ligne de création de 7b)
   à la valeur de la configuration, à l'octet ; trois marqueurs sont, dans la configuration, « hors configuration
   (circulaire) » : les deux marqueurs de l'ordre lui-même, que l'ordre dit « hors de ce texte », et l'empreinte de
   la configuration, que l'ordre doit porter égale à l'empreinte recalculée en A ;
C. il compte, hors du § 11, les places où chaque valeur remplie au brouillon 9 est écrite ;
D. il compte les marqueurs entre chevrons doubles restés dans l'ordre (attendu : aucun) ;
E. il recompte les états de la table du § 11 (rempli, en attente, hors de ce texte) ;
F. il compare les valeurs libres de la table du § 2 de l'ordre, transcrites plus bas dans ce programme, à la
   configuration ;
G. il cherche dans le § 5 les fragments de commandes qui nomment la branche du code, le commit du code revu, le
   commit de lancement et le chemin de la configuration.

Il n'affiche AUCUNE valeur de marqueur ni aucune valeur de la configuration dans ses tables : seulement des noms,
des verdicts, des longueurs en caractères et des comptes. Seuls ses trois arguments fixes sont écrits en tête : le
commit de lancement, le chemin de la configuration et son empreinte. Il n'ouvre que l'ordre donné en argument ; il
ne lit de la configuration que ses marqueurs et les clés nommées en A et en F ; il n'ouvre ni la consigne, ni la
conception, ni aucun résultat. Il n'écrit aucun fichier. Code de sortie : 0 si tout est conforme, 1 sinon.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent
COMMIT_LANCEMENT = "836c7cccda5071fe54ecb148d214d74b5cb90474"
CHEMIN_CONFIG = "docs/notes/barreau8-iib-v1/config-iib-reel-v1.json"
EMPREINTE_CONFIG_ATTENDUE = "1bd2e16a79def36de945359bb64e34beb899410dfe2964d28da1f1b85e3f6a17"
CIRCULAIRE = "hors configuration (circulaire)"
HORS_TEXTE = "hors de ce texte"
CIRCULAIRES_ATTENDUS = {"CHEMIN_ORDRE_IIB", "EMPREINTE_ORDRE_IIB", "EMPREINTE_CONFIG_IIB"}
MARQUEUR_BLOC = "EMPREINTES_CODE_IIB"
MARQUEUR_7B = "LIGNE_REGISTRE_CREATION_7B"
MARQUEUR_PROPRE_LANCEMENT = "COMMIT_LANCEMENT_IIB"
# Les marqueurs que le brouillon 8 laissait en attente (12 des 30), remplis au brouillon 9.
REMPLIS_AU_BROUILLON_9 = (
    "CHEMIN_CONCEPTION_IIB", "CHEMIN_CONFIG_IIB", "DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR", "EMPREINTES_CODE_IIB",
    "EMPREINTE_CONCEPTION_IIB", "EMPREINTE_CONFIG_IIB", "ENTROPIE_IIB", "EXECUTANTE_IIB", "LECTEUR_IIB",
    "LONGUEURS_CONSIGNE_IIB", "MOT_LAZAR_CREATION_IIB", "VERSION_VASTAI",
)
MOTIF_MARQUEUR = re.compile(r"<<([A-Z0-9_]+)>>")
MOTIF_LIGNE_VALEUR = re.compile(r"^\| `([A-Z0-9_]+)` \| (.*) \|$")
MOTIF_7B = re.compile(r"`(7b créée, instance \d+ à \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)`")
TITRE_TABLE_VALEURS = "| marqueur | valeur à l'octet"
TITRE_BLOC = "Valeur de `EMPREINTES_CODE_IIB`"
TITRE_TABLE_ETATS = "| marqueur | état | valeur, ou ce qu'il attend |"

# Valeurs libres de la table du § 2 de l'ordre, transcrites ici depuis ce § 2 par l'auteur de ce programme.
# « @COMMIT_CODE@ », « @BRANCHE_CODE@ » et « @EXTRAIT_7B@ » sont lus dans l'ordre lui-même (voir F).
LIBRES_DU_PARAGRAPHE_2 = {
    "offre": {
        "etiquette": "iib-explo-v1", "disque_min_go": 100, "coeurs_effectifs_min": 16, "memoire_vive_min_mo": 128000,
        "stockage_max_usd_h": 0.08, "telechargement_go_prevu": 40, "telechargement_max_usd_go": 0.05,
    },
    "carte.course": {"nom_offre": "A100 SXM4", "nom": "A100 SXM4 80 Go", "prix_max_usd_h": 1.3, "memoire_carte_min_mo": 80000},
    "carte.relance": {"nom_offre": "H200 NVL", "nom": "H200 NVL", "prix_max_usd_h": 4.7, "memoire_carte_min_mo": 140000},
    "memoire_vive_min_go": 128,
    "agent.nom": "8B",
    "agent.variables_gabarit": {"date_string": "26 Jul 2024"},
    "code": {"branche": "@BRANCHE_CODE@", "commit": "@COMMIT_CODE@"},
    "oracle.forme_lot_suites": "cache_duplique",
    "plafond": {"variante": "B", "ligne_usd": 60, "configuration_usd": 55, "repli_h200": False},
    "plafond_usd": 55,
    "calendrier": {"dernier_jour_creation": "2026-11-25", "fin_go_utc": "2026-11-28T00:00:00Z"},
    "juge_t08": {"forme_scellee": False},
    "prealables": {"ligne_registre_creation_7b": "@EXTRAIT_7B@"},
}


class Arret(Exception):
    """Lecture impossible : le programme s'arrête, code 1, sans verdict."""


def git(*arguments: str) -> bytes:
    r = subprocess.run(["git", "-C", str(RACINE), *arguments], capture_output=True)
    if r.returncode != 0:
        raise Arret(f"git {' '.join(arguments[:2])} : code {r.returncode}")
    return r.stdout


def cle(config: dict, chemin: str):
    v = config
    for k in chemin.split("."):
        v = v[k]
    return v


def section(texte: str, debut: str, fin: str | None) -> str:
    """Le texte de l'ordre depuis la ligne de titre qui commence par `debut` jusqu'à celle qui commence par `fin`."""
    lignes = texte.split("\n")
    i = [n for n, l in enumerate(lignes) if l.startswith(debut)]
    if len(i) != 1:
        raise Arret(f"titre « {debut} » trouvé {len(i)} fois")
    if fin is None:
        return "\n".join(lignes[i[0]:])
    j = [n for n, l in enumerate(lignes) if l.startswith(fin) and n > i[0]]
    if not j:
        raise Arret(f"titre « {fin} » absent après « {debut} »")
    return "\n".join(lignes[i[0]:j[0]])


def table_des_valeurs(p11: str) -> dict[str, str]:
    lignes = p11.split("\n")
    i = [n for n, l in enumerate(lignes) if l.startswith(TITRE_TABLE_VALEURS)]
    if len(i) != 1:
        raise Arret(f"table des valeurs à l'octet trouvée {len(i)} fois au § 11")
    valeurs: dict[str, str] = {}
    for l in lignes[i[0] + 2:]:
        if not l.startswith("|"):
            break
        m = MOTIF_LIGNE_VALEUR.match(l)
        if not m:
            raise Arret("ligne illisible dans la table des valeurs à l'octet")
        if m.group(1) in valeurs:
            raise Arret(f"marqueur {m.group(1)} écrit deux fois dans la table des valeurs à l'octet")
        valeurs[m.group(1)] = m.group(2)
    return valeurs


def bloc_des_empreintes(p11: str) -> str:
    lignes = p11.split("\n")
    i = [n for n, l in enumerate(lignes) if l.startswith(TITRE_BLOC)]
    if len(i) != 1:
        raise Arret(f"bloc du marqueur des empreintes du code trouvé {len(i)} fois au § 11")
    reste = lignes[i[0] + 1:]
    clotures = [n for n, l in enumerate(reste) if l == "```"]
    if len(clotures) < 2 or clotures[1] - clotures[0] != 2:
        raise Arret("le bloc du marqueur des empreintes du code n'est pas une seule ligne entre deux clôtures")
    return reste[clotures[0] + 1]


def table_des_etats(p11: str) -> list[tuple[list[str], bool, str]]:
    lignes = p11.split("\n")
    i = [n for n, l in enumerate(lignes) if l == TITRE_TABLE_ETATS]
    if len(i) != 1:
        raise Arret(f"table des états trouvée {len(i)} fois au § 11")
    rangs = []
    for l in lignes[i[0] + 2:]:
        if not l.startswith("|"):
            break
        cellules = l.strip("|").split(" | ")
        noms = re.findall(r"`([A-Z0-9_]+)`", cellules[0])
        rangs.append((noms, "(propre" in cellules[0], cellules[1].strip()))
    return rangs


def etat_court(etat: str) -> str:
    if etat.startswith("rempli"):
        return "rempli"
    if etat.startswith("en attente"):
        return "en attente"
    if etat.startswith(HORS_TEXTE):
        return HORS_TEXTE
    return "illisible"


def main() -> int:
    if len(sys.argv) != 2:
        print("usage : comparer-marqueurs-ordre-configuration-ii-b-v1.py ORDRE", file=sys.stderr)
        return 1
    ecarts: list[str] = []

    def noter(condition: bool, quoi: str) -> str:
        if not condition:
            ecarts.append(quoi)
        return "conforme" if condition else "ÉCART"

    try:
        chemin_ordre = Path(sys.argv[1])
        octets_ordre = chemin_ordre.read_bytes()
        ordre = octets_ordre.decode("utf-8")
        brut = git("show", f"{COMMIT_LANCEMENT}:{CHEMIN_CONFIG}")
        config = json.loads(brut.decode("utf-8"))
        marqueurs: dict[str, str] = config["marqueurs"]
        p2 = section(ordre, "## 2. ", "## 3. ")
        p5 = section(ordre, "## 5. ", "## 6. ")
        p11 = section(ordre, "## 11. ", "## 12. ")
        hors_p11 = ordre.replace(p11, "")
        valeurs = table_des_valeurs(p11)
        bloc = bloc_des_empreintes(p11)
        etats = table_des_etats(p11)
        extraits_7b = MOTIF_7B.findall(ordre)
        parent = git("rev-parse", f"{COMMIT_LANCEMENT}^").decode().strip()
        fichiers = sorted(git("diff", "--name-only", parent, COMMIT_LANCEMENT).decode().split())
    except (Arret, OSError, KeyError, ValueError) as arret:
        print(f"ARRÊT, aucun verdict : {arret}", file=sys.stderr)
        return 1

    print("comparer-marqueurs-ordre-configuration-ii-b-v1 — EXPLORATOIRE, NON OPPOSABLE (R-522)")
    print(f"ordre : {chemin_ordre.name}  {hashlib.sha256(octets_ordre).hexdigest()}")
    print(f"configuration : {CHEMIN_CONFIG} au commit {COMMIT_LANCEMENT}")

    print("\nA. Configuration au commit de lancement")
    empreinte_config = hashlib.sha256(brut).hexdigest()
    print(f"  empreinte recalculée {empreinte_config} ; attendue {EMPREINTE_CONFIG_ATTENDUE} : "
          + noter(empreinte_config == EMPREINTE_CONFIG_ATTENDUE, "empreinte de la configuration"))
    print(f"  marqueurs dans la configuration : {len(marqueurs)} (attendu 30) : "
          + noter(len(marqueurs) == 30, "nombre de marqueurs de la configuration"))
    circulaires = {n for n, v in marqueurs.items() if v == CIRCULAIRE}
    print(f"  marqueurs « {CIRCULAIRE} » : {len(circulaires)} ({', '.join(sorted(circulaires))}) : "
          + noter(circulaires == CIRCULAIRES_ATTENDUS, "marqueurs circulaires de la configuration"))
    print("  parent direct du commit de lancement = marqueur COMMIT_CODE_IIB : "
          + noter(parent == marqueurs["COMMIT_CODE_IIB"], "parent du commit de lancement"))
    print(f"  fichiers ajoutés par le commit de lancement : {len(fichiers)} ; la configuration et son sceau seulement : "
          + noter(fichiers == [CHEMIN_CONFIG, CHEMIN_CONFIG + ".sha256"], "fichiers du commit de lancement"))
    croisements = [
        ("code.commit", "COMMIT_CODE_IIB", str), ("code.branche", "BRANCHE_CODE_IIB", str),
        ("entropie", "ENTROPIE_IIB", str), ("go_id", "GO_ID_IIB", str),
        ("plafond.ligne_usd", "PLAFOND_LIGNE_IIB", str), ("plafond_usd", "PLAFOND_CONFIG_IIB", str),
        ("plafond.configuration_usd", "PLAFOND_CONFIG_IIB", str),
        ("calendrier.dernier_jour_creation", "DERNIER_JOUR_CREATION_IIB", str),
        ("calendrier.fin_go_utc", "FIN_GO_UTC_IIB", str),
        ("plafond.repli_h200", "REPLI_H200_PERMIS", lambda b: "oui" if b else "non"),
        ("juge_t08.forme_scellee", "FORME_JUGE_T08_SCELLEE", lambda b: "oui" if b else "non"),
        ("consigne_maitre.chemin", "CHEMIN_CONSIGNE_IIB", str), ("consigne_maitre.sha256", "EMPREINTE_CONSIGNE_IIB", str),
        ("prealables.ligne_registre_creation_7b", MARQUEUR_7B, str),
    ]
    for chemin_cle, nom, forme in croisements:
        print(f"  clé {chemin_cle} = marqueur {nom} : "
              + noter(forme(cle(config, chemin_cle)) == marqueurs[nom], f"clé {chemin_cle} et marqueur {nom}"))

    print("\nB. Les 30 marqueurs de la configuration : valeur de l'ordre contre valeur de la configuration")
    print("  marqueur | où l'ordre l'écrit | longueur dans l'ordre | longueur dans la configuration | verdict")
    egaux = hors = recalcule = differents = 0
    for nom in sorted(marqueurs):
        v_config = marqueurs[nom]
        if nom in ("CHEMIN_ORDRE_IIB", "EMPREINTE_ORDRE_IIB"):
            cellule = valeurs.get(nom, "")
            bon = v_config == CIRCULAIRE and cellule.startswith(HORS_TEXTE) and "`" not in cellule
            hors += bon
            differents += not bon
            print(f"  {nom} | table du § 11 | — | {len(v_config)} | "
                  + ("hors de ce texte dans l'ordre, circulaire dans la configuration : attendu" if bon else "ÉCART"))
            noter(bon, f"marqueur {nom}")
            continue
        if nom == "EMPREINTE_CONFIG_IIB":
            cellule = valeurs.get(nom, "")
            m = re.match(r"^`([0-9a-f]{64})`", cellule)
            v_ordre = m.group(1) if m else ""
            bon = v_config == CIRCULAIRE and v_ordre == empreinte_config
            recalcule += bon
            differents += not bon
            print(f"  {nom} | table du § 11 | {len(v_ordre)} | {len(v_config)} | "
                  + ("égal à l'empreinte recalculée de la configuration, que la configuration ne peut pas porter : attendu"
                     if bon else "ÉCART"))
            noter(bon, f"marqueur {nom}")
            continue
        if nom == MARQUEUR_BLOC:
            v_ordre, ou = bloc, "bloc du § 11"
            bon = v_ordre == v_config and "bloc" in valeurs.get(nom, "") and "`" not in valeurs.get(nom, "")
        elif nom == MARQUEUR_7B:
            v_ordre, ou = (extraits_7b[0] if extraits_7b else ""), f"{len(extraits_7b)} places du texte"
            bon = len(extraits_7b) == 2 and all(e == v_config for e in extraits_7b) and "`" not in valeurs.get(nom, "`")
        else:
            cellule = valeurs.get(nom, "")
            m = re.fullmatch(r"`([^`]*)`", cellule)
            v_ordre, ou = (m.group(1) if m else ""), "table du § 11"
            bon = bool(m) and v_ordre == v_config
        egaux += bon
        differents += not bon
        print(f"  {nom} | {ou} | {len(v_ordre)} | {len(v_config)} | " + ("égal à l'octet" if bon else "ÉCART"))
        noter(bon, f"marqueur {nom}")
    en_trop = sorted(set(valeurs) - set(marqueurs))
    print(f"  marqueurs de la table absents de la configuration : {len(en_trop)} : "
          + noter(not en_trop, "marqueurs en trop dans la table des valeurs"))
    print(f"  BILAN B : {len(marqueurs)} marqueurs ; égaux à l'octet {egaux} ; hors de ce texte {hors} ; "
          f"empreinte de la configuration égale à l'empreinte recalculée {recalcule} ; différents {differents}")

    print("\nC. Places, hors du § 11, des valeurs remplies au brouillon 9 (nombre d'occurrences à l'octet)")
    for nom in REMPLIS_AU_BROUILLON_9:
        if nom == MARQUEUR_BLOC:
            n = hors_p11.count(marqueurs[nom])
            print(f"  {nom} : {n} (valeur écrite une fois, au bloc du § 11 ; ailleurs, renvoi au bloc) : "
                  + noter(n == 0 and hors_p11.count("bloc « Valeur de `EMPREINTES_CODE_IIB` »") >= 3, f"renvois au bloc de {nom}"))
            continue
        v = empreinte_config if nom == "EMPREINTE_CONFIG_IIB" else marqueurs[nom]
        n = hors_p11.count(v)
        print(f"  {nom} : {n} : " + noter(n >= 1, f"valeur de {nom} absente hors du § 11"))
    n = hors_p11.count(COMMIT_LANCEMENT)
    print(f"  {MARQUEUR_PROPRE_LANCEMENT} (propre à l'ordre) : {n} : " + noter(n >= 1, "commit de lancement absent hors du § 11"))

    print("\nD. Marqueurs entre chevrons doubles restés dans l'ordre")
    restes = MOTIF_MARQUEUR.findall(ordre)
    print(f"  occurrences {len(restes)} ; distincts {len(set(restes))} : " + noter(not restes, "marqueurs restés ouverts"))
    sans = MOTIF_MARQUEUR.sub("", ordre)
    print(f"  chevrons doubles hors marqueurs : ouvrants {sans.count('<<')}, fermants {sans.count('>>')} "
          "(attendu 1 et 1 : le motif de la commande de vérification écrite à la fin du § 11) : "
          + noter(sans.count("<<") == 1 and sans.count(">>") == 1 and "grep -o '<<[A-Z0-9_]*>>'" in p11, "chevrons doubles hors marqueurs"))
    print("  AUCUN MARQUEUR OUVERT HORS DES DEUX MARQUEURS HORS TEXTE : "
          + ("oui" if not restes and hors == 2 else "NON"))

    print("\nE. États de la table du § 11, recomptés")
    comptes = {"rempli": 0, "en attente": 0, HORS_TEXTE: 0, "illisible": 0}
    comptes_propres = dict(comptes)
    vus: list[str] = []
    for noms, propre, etat in etats:
        for nom in noms:
            (comptes_propres if propre else comptes)[etat_court(etat)] += 1
            if not propre:
                vus.append(nom)
    print(f"  des 30 de la configuration : remplis {comptes['rempli']} ; en attente {comptes['en attente']} ; "
          f"hors de ce texte {comptes[HORS_TEXTE]} ; illisibles {comptes['illisible']} : "
          + noter(sorted(vus) == sorted(marqueurs) and comptes["en attente"] == 0 and comptes["illisible"] == 0
                  and comptes[HORS_TEXTE] == 2 and comptes["rempli"] == 28, "états des 30 marqueurs"))
    print(f"  propres à l'ordre : remplis {comptes_propres['rempli']} ; en attente {comptes_propres['en attente']} ; "
          f"illisibles {comptes_propres['illisible']} : "
          + noter(comptes_propres["rempli"] == 6 and comptes_propres["en attente"] == 0
                  and comptes_propres["illisible"] == 0, "états des marqueurs propres"))
    phrase = (f"sur les 30, **{comptes['rempli']} remplis, {comptes['en attente']} en attente, "
              f"{comptes[HORS_TEXTE]} hors de ce texte**")
    print("  la phrase des comptes du § 11 porte ces nombres : " + noter(phrase in p11, "phrase des comptes du § 11"))
    phrase = f"plus 6 propres : **{comptes_propres['rempli']} remplis**"
    print("  la phrase des comptes propres du § 11 porte ces nombres : " + noter(phrase in p11, "phrase des comptes propres"))

    print("\nF. Valeurs libres de la table du § 2 (transcrites dans ce programme) contre la configuration")
    remplacements = {
        "@BRANCHE_CODE@": marqueurs["BRANCHE_CODE_IIB"], "@COMMIT_CODE@": marqueurs["COMMIT_CODE_IIB"],
        "@EXTRAIT_7B@": extraits_7b[0] if extraits_7b else "",
    }
    for chemin_cle, attendu in LIBRES_DU_PARAGRAPHE_2.items():
        if isinstance(attendu, dict):
            attendu = {k: remplacements.get(v, v) if isinstance(v, str) else v for k, v in attendu.items()}
        lu = cle(config, chemin_cle)
        bon = lu == attendu and type(lu) is type(attendu)
        if isinstance(attendu, dict):
            bon = bon and all(type(lu[k]) is type(v) for k, v in attendu.items())
        print(f"  {chemin_cle} : " + noter(bon, f"valeur libre {chemin_cle}"))
    ligne_code = [l for l in p2.split("\n") if l.startswith("| `code` |")]
    print("  la ligne « code » du § 2 nomme la branche et le commit du code de la configuration : "
          + noter(len(ligne_code) == 1 and f"« {marqueurs['BRANCHE_CODE_IIB']} »" in ligne_code[0]
                  and f"`{marqueurs['COMMIT_CODE_IIB']}`" in ligne_code[0], "ligne « code » du § 2"))
    cles_agent = sorted(config["agent"])
    print(f"  agent : {len(cles_agent)} clés ({', '.join(cles_agent)}) : "
          + noter(cles_agent == ["modele", "nom", "revision", "texte_attendu_ouverture", "variables_gabarit"], "clés de l'agent"))

    print("\nG. Commandes du § 5 : fragments attendus, construits depuis la configuration et le commit de lancement")
    branche, code = marqueurs["BRANCHE_CODE_IIB"], marqueurs["COMMIT_CODE_IIB"]
    fragments = {
        "version de l'outil de location": f"`vastai --version` → `{marqueurs['VERSION_VASTAI']}`",
        "clonage de la branche du code": f"--single-branch --branch {branche} https://github.com/lciric/controle-ia-travail.git \"$W/depot\"",
        "extraction du commit de lancement": f"checkout --detach {COMMIT_LANCEMENT}`",
        "branche distante exigée": f"`refs/remotes/origin/{branche}`",
        "parent du commit de lancement": f"rev-parse HEAD^` = `{code}`",
        "fichiers du commit de lancement": f"diff --name-only {code} {COMMIT_LANCEMENT}`",
        "ligne d'accord au commit de lancement": f"`git show {COMMIT_LANCEMENT}:registres/go.md | grep -c '^| GO-2026-11-10-08 |'` = 1",
        "variable de la branche du code": f"IIB_BRANCHE_CODE={branche} IIB_BRANCHE=essai/iib-explo-v1",
        "contrôles du lanceur": f"controles-explo \"$W/iib\" {COMMIT_LANCEMENT} {marqueurs['CHEMIN_CONFIG_IIB']}`",
        "commit passé à l'instance": f"`-e COMMIT={COMMIT_LANCEMENT}`",
        "configuration passée à l'instance": f"`-e CONFIG={marqueurs['CHEMIN_CONFIG_IIB']}`",
    }
    for quoi, fragment in fragments.items():
        n = p5.count(fragment)
        print(f"  {quoi} : {n} : " + noter(n == 1, f"fragment du § 5 : {quoi}"))
    for quoi, ancien in (("ancienne branche du code", "prep/iib-code-v3"),
                         ("premier commit de lancement, abandonné", "968a5151")):
        n = p5.count(ancien)
        print(f"  {quoi} dans le § 5 : {n} (attendu 0) : " + noter(n == 0, f"§ 5 : {quoi}"))

    print(f"\nBILAN : écarts {len(ecarts)}")
    for e in ecarts:
        print(f"  ÉCART : {e}")
    if not ecarts:
        print(f"  30 marqueurs de la configuration : {egaux} égaux à l'octet ; {hors} hors de ce texte ; "
              f"{recalcule} égal à l'empreinte recalculée de la configuration ; aucun différent.")
    return 0 if not ecarts else 1


if __name__ == "__main__":
    sys.exit(main())
