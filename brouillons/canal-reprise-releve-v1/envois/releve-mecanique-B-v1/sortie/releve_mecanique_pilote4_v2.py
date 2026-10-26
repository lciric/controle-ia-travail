"""Relevé mécanique (B) d'une course du pilote 4 — v2.

Écrit par un sous-agent neuf de la lignée conv-audit, le 2026-10-26T09:18:01Z (heure lue sur `date -u` dans la commande qui écrit
ce fichier), sur la spécification v3 (d6ac5d3f…), le brief v1 (a047c89f…), les décisions et précisions de conv-audit
(table close des courses ; ligne de réponse reconnue par son seul début, CLB4-06 ; quatre lignes portant la clé de
course, CLB5-01 ; interface avec la garde G1), après lecture des pièces de simulation des séries v13 et v14 seules.
Remplace la v1 (releve_mecanique_pilote4_v1.py, b51699c7…), gardée telle quelle : la v2 ajoute identite.lignee_source et
contrôle la clé de course sur quatre lignes.

Usage : python3 -I releve_mecanique_pilote4_v2.py DOSSIER_DE_COURSE DOSSIER_DE_SORTIE

Écrit DOSSIER_DE_SORTIE/releve-mecanique-<dossier>-v2.txt et son compagnon .sha256 en création exclusive (jamais
réécrits ; le dossier de sortie ne peut pas être dans le dossier de course). Sortie standard : une ligne « relevé écrit :
<fichier> <empreinte> ». Codes : 0 écrit ; 2 usage ; 3 refus (motif sur la sortie d'erreur : un nom de champ, jamais une
valeur) ; 4 erreur interne (type et ligne seulement).

Le script vérifie d'abord son compagnon .sha256 et l'empreinte de la table de correspondance posée à côté de lui
(EMPREINTE_TABLE), puis la liste fermée du dossier de course (compagnon, puis chaque ligne). Il ne lit le contenu que de
la liste fermée, de LANCEMENT.md, de A-POUSSER-v1.txt, de extrait-mecanique-v1.json et des journaux d'appels, chacun
seulement s'il est dans la liste fermée et conforme ; il hache les autres fichiers de la liste sans en rien lire d'autre ;
il ne décompresse rien, ne suit aucun lien symbolique, n'exécute rien. Bibliothèque standard seule ; aucun réseau.
"""
import decimal
import hashlib
import json
import os
import re
import stat
import sys
import time
import unicodedata

EMPREINTE_TABLE = "4ad8b371b1a64348175c79c743ee33664b38382905b3a84ef3168290fc394c71"
NOM_TABLE = "table-correspondance-releve-B-v2.json"
VERSION_RELEVE = "v2"

# Table close des courses (spécification v3, § 4.2) : clé de course → (nom de la course, lignée).
COURSES = {
    "v6-2": ("pilote4-gemini-v6-2-v1", "gemini-organisme-v6-2"),
    "v6-2-s": ("pilote4-gemini-v6-2-s-v1", "gemini-organisme-v6-2-s"),
}
LIGNEE_DEDUITE = "deduite_de_la_cle_controle_non_independant"

MOTIF_LISTE = "sources.liste_fermee_verifiee"
TAILLE_BLOC = 1 << 20
ABSENT = "absent"
MANQUE = object()


class Refus(Exception):
    """Refus d'écrire le relevé (code 3) ; l'argument est un nom de champ, jamais une valeur."""


class Usage(Exception):
    """Mauvais usage (code 2) ; l'argument est un libellé fixe."""


# --- Lectures : pièces du script, sources de la liste blanche, hachage des autres fichiers ---

def sha256_octets(octets):
    return hashlib.sha256(octets).hexdigest()


def lire_piece(chemin):
    """Lit une pièce du script lui-même (script, compagnon, table), hors du dossier de course."""
    with open(chemin, "rb") as f:
        return f.read()


def ouvrir_sans_lien(chemin):
    try:
        fd = os.open(chemin, os.O_RDONLY | os.O_NOFOLLOW | getattr(os, "O_CLOEXEC", 0))
    except OSError:
        raise Refus(MOTIF_LISTE)
    if not stat.S_ISREG(os.fstat(fd).st_mode):
        os.close(fd)
        raise Refus(MOTIF_LISTE)
    return fd


def lire_source(chemin):
    """Lit en entier une source de la liste blanche du dossier de course (lien jamais suivi)."""
    fd = ouvrir_sans_lien(chemin)
    with os.fdopen(fd, "rb") as f:
        return f.read()


def empreinte_fichier(chemin):
    """Hache par blocs un fichier de la liste fermée ; son contenu ne sert à rien d'autre."""
    fd = ouvrir_sans_lien(chemin)
    h = hashlib.sha256()
    with os.fdopen(fd, "rb") as f:
        for bloc in iter(lambda: f.read(TAILLE_BLOC), b""):
            h.update(bloc)
    return h.hexdigest()


def decoder(octets, motif):
    try:
        return unicodedata.normalize("NFC", octets.decode("utf-8"))
    except UnicodeDecodeError:
        raise Refus(motif)


def charger_json(texte, motif):
    """JSON strict : clé en double, NaN ou Infinity font refuser ; les décimaux restent exacts."""
    def paires(liste):
        objet = {}
        for cle, valeur in liste:
            if cle in objet:
                raise Refus(motif)
            objet[cle] = valeur
        return objet

    def constante(_nom):
        raise Refus(motif)

    try:
        return json.loads(texte, parse_float=decimal.Decimal, parse_constant=constante, object_pairs_hook=paires)
    except ValueError:
        raise Refus(motif)


# --- Pièces du script : compagnon et table ---

def verifier_compagnon_script(octets, chemin):
    try:
        compagnon = lire_piece(chemin + ".sha256")
    except OSError:
        raise Refus("releve.script_empreinte")
    nom = re.escape(os.path.basename(chemin).encode("utf-8"))
    m = re.fullmatch(rb"([0-9a-f]{64})  " + nom + rb"\n?", compagnon)
    if m is None or m.group(1).decode("ascii") != sha256_octets(octets):
        raise Refus("releve.script_empreinte")


def analyser_chemin(texte):
    composants = []
    for partie in texte.split("."):
        if partie.endswith("[]"):
            composants.extend([partie[:-2], "[]"])
        else:
            composants.append(partie)
    return tuple(composants)


def compiler_cle(motif_cle, segments):
    morceaux = ["(" + segments[p] + ")" if p in segments else re.escape(p) for p in motif_cle.split(".")]
    return re.compile(r"\.".join(morceaux))


def charger_table(chemin):
    try:
        octets = lire_piece(chemin)
    except OSError:
        raise Refus("table")
    if sha256_octets(octets) != EMPREINTE_TABLE:
        raise Refus("table")
    table = json.loads(octets.decode("utf-8"))
    table["_chemins_extrait"] = [analyser_chemin(c) for c in table["extrait"]["champs"]]
    table["_chemins_journal"] = [analyser_chemin(c) for c in table["journal_appels"]["champs"]]
    for motif in table["_chemins_extrait"] + table["_chemins_journal"]:
        if est_noir(tuple(c for c in motif if c not in ("[]", "*")), table):
            raise ValueError("table : un champ de la liste blanche est dans la liste noire")
    table["_formes"] = {nom: re.compile(motif) for nom, motif in table["formes"].items()}
    table["_cles"] = [(e["cle"], compiler_cle(e["cle"], table["segments_de_cle"]), e["formes"]) for e in table["cles"]]
    table["_lignes"] = {nom: re.compile(motif) for nom, motif in table["lancement"]["lignes"].items()}
    table["_journal"] = re.compile(table["journal_appels"]["motif_fichier"])
    lignee = analyser_chemin(table["extrait"]["lignee_champ"])
    if lignee[:2] != ("generations", "[]") or lignee not in table["_chemins_extrait"]:
        raise ValueError("table : le champ de lignée doit être un champ d'unité de la liste blanche")
    table["_lignee_champ"] = lignee[2:]
    return table


# --- Liste noire, liste blanche, comptage des champs ignorés ---

def sans_accents(texte):
    decompose = unicodedata.normalize("NFKD", texte)
    return "".join(c for c in decompose if not unicodedata.combining(c)).lower()


def est_noir(chemin, table):
    for composant in chemin:
        if isinstance(composant, str) and any(n in sans_accents(composant) for n in table["liste_noire"]):
            return True
    return False


def correspond(chemin, motif):
    if len(chemin) != len(motif):
        return False
    for composant, attendu in zip(chemin, motif):
        if attendu == "[]":
            if not isinstance(composant, int):
                return False
        elif attendu == "*":
            if not isinstance(composant, str):
                return False
        elif composant != attendu:
            return False
    return True


def feuilles(objet, chemin=()):
    if isinstance(objet, dict):
        if not objet:
            yield chemin, {}
        for cle, valeur in objet.items():
            yield from feuilles(valeur, chemin + (cle,))
    elif isinstance(objet, list):
        if not objet:
            yield chemin, []
        for rang, valeur in enumerate(objet):
            yield from feuilles(valeur, chemin + (rang,))
    else:
        yield chemin, objet


def couvrir(objet, motifs, table):
    """Garde les feuilles de la liste blanche qui ne sont pas noires ; compte les autres (champs ignorés)."""
    couverts, ignores = {}, 0
    for chemin, valeur in feuilles(objet):
        if not est_noir(chemin, table) and any(correspond(chemin, m) for m in motifs):
            couverts[chemin] = valeur
        else:
            ignores += 1
    return couverts, ignores


# --- Formes des valeurs ---

def identifiant(valeur, motif):
    """Identifiant strict : minuscules, accents ôtés, puis la forme exacte ; sinon refus (texte libre)."""
    if not isinstance(valeur, str):
        raise Refus(motif)
    plat = sans_accents(valeur)
    if re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,47}", plat) is None:
        raise Refus(motif)
    return plat


def r_identifiant(valeur, motif):
    return ABSENT if valeur is MANQUE or valeur is None else identifiant(valeur, motif)


def r_entier(valeur, motif):
    if valeur is MANQUE or valeur is None:
        return ABSENT
    if type(valeur) is not int or valeur < 0 or len(str(valeur)) > 12:
        raise Refus(motif)
    return str(valeur)


def r_oui_non(valeur, motif):
    if valeur is MANQUE or valeur is None:
        return ABSENT
    if type(valeur) is not bool:
        raise Refus(motif)
    return "oui" if valeur else "non"


def decimal_exact(valeur, motif):
    if type(valeur) is int:
        valeur = decimal.Decimal(valeur)
    if not isinstance(valeur, decimal.Decimal) or not valeur.is_finite() or valeur.is_signed():
        raise Refus(motif)
    texte = format(valeur, "f")
    if "." in texte:
        texte = texte.rstrip("0")
        if texte.endswith("."):
            texte += "0"
    return texte


def r_montant(valeur, motif):
    if valeur is MANQUE or valeur is None:
        return ABSENT
    texte = decimal_exact(valeur, motif)
    if "." not in texte:
        texte += ".0"
    if re.fullmatch(r"[0-9]{1,6}\.[0-9]{1,4}", texte) is None:
        raise Refus(motif)
    return texte + " USD"


def r_duree(valeur, motif):
    if valeur is MANQUE or valeur is None:
        return ABSENT
    texte = decimal_exact(valeur, motif)
    if re.fullmatch(r"[0-9]{1,8}(\.[0-9]{1,3})?", texte) is None:
        raise Refus(motif)
    return texte + " s"


def ou_absent(valeur):
    return ABSENT if valeur is MANQUE or valeur is None else valeur


# --- Dossiers et liste fermée ---

def identifiant_exact(nom, motif):
    if re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,47}", nom) is None:
        raise Refus(motif)
    return nom


def verifier_dossiers(course, sortie):
    racine, sortie = os.path.abspath(course), os.path.abspath(sortie)
    try:
        etat = os.lstat(racine)
    except OSError:
        raise Usage("dossier de course introuvable")
    if stat.S_ISLNK(etat.st_mode):
        raise Refus(MOTIF_LISTE)
    if not stat.S_ISDIR(etat.st_mode):
        raise Usage("dossier de course introuvable")
    if not os.path.isdir(sortie):
        raise Usage("dossier de sortie introuvable")
    vrai_r, vrai_s = os.path.realpath(racine), os.path.realpath(sortie)
    if vrai_s == vrai_r or vrai_s.startswith(vrai_r.rstrip(os.sep) + os.sep):
        raise Usage("dossier de sortie dans le dossier de course")
    return racine, sortie


def nom_valide(nom):
    if not nom or nom.startswith("/") or "\\" in nom or "\x00" in nom:
        return False
    return all(partie not in ("", ".", "..") for partie in nom.split("/"))


def lire_liste_fermee(racine, table):
    nom_liste = table["liste_fermee"]["fichier"]
    octets = lire_source(os.path.join(racine, nom_liste))
    compagnon = lire_source(os.path.join(racine, table["liste_fermee"]["compagnon"]))
    m = re.fullmatch(rb"([0-9a-f]{64})  " + re.escape(nom_liste.encode("utf-8")) + rb"\n?", compagnon)
    if m is None or m.group(1).decode("ascii") != sha256_octets(octets):
        raise Refus(MOTIF_LISTE)
    try:
        lignes = octets.decode("utf-8").split("\n")
    except UnicodeDecodeError:
        raise Refus(MOTIF_LISTE)
    if lignes[-1] == "":
        lignes.pop()
    entrees = {}
    for ligne in lignes:
        m = re.fullmatch(r"([0-9a-f]{64})  (.+)", ligne)
        if m is None or not nom_valide(m.group(2)) or m.group(2) in entrees:
            raise Refus(MOTIF_LISTE)
        entrees[m.group(2)] = m.group(1)
    if not entrees:
        raise Refus(MOTIF_LISTE)
    return octets, entrees


def balayer(racine):
    """Parcourt les noms de l'arbre (sans ouvrir aucun fichier) : lien symbolique ou fichier spécial = refus."""
    a_voir = [racine]
    while a_voir:
        dossier = a_voir.pop()
        with os.scandir(dossier) as entrees:
            for entree in entrees:
                if entree.is_symlink():
                    raise Refus(MOTIF_LISTE)
                if entree.is_dir(follow_symlinks=False):
                    a_voir.append(entree.path)
                elif not entree.is_file(follow_symlinks=False):
                    raise Refus(MOTIF_LISTE)


def motif_de_source(nom, table):
    """Motif de refus d'un nom de source lisible (ou qui y ressemble), None pour tout autre nom."""
    if nom == table["lancement"]["fichier"]:
        return "sources.lancement"
    if nom == table["a_pousser"]["fichier"]:
        return "fin.liste_fermee_poussee"
    if re.fullmatch(r"extrait-mecanique.*\.json", nom):
        return "sources.extrait"
    if re.fullmatch(r"journal-appels.*\.jsonl", nom):
        return "sources.journal_appels"
    return None


def verifier_et_lire(racine, entrees, table):
    """Vérifie chaque ligne de la liste fermée ; rend les octets des seules sources lisibles."""
    with os.scandir(racine) as it:
        a_la_racine = sorted(e.name for e in it if e.is_file(follow_symlinks=False))
    for nom in a_la_racine:
        motif = motif_de_source(nom, table)
        if motif is not None and nom not in entrees:
            raise Refus(motif)
    exacts = (table["lancement"]["fichier"], table["a_pousser"]["fichier"], table["extrait"]["fichier"])
    lus = {}
    for nom in sorted(entrees):
        motif = motif_de_source(nom, table)
        lisible = motif is not None and (nom in exacts or table["_journal"].fullmatch(nom) is not None)
        if motif is not None and not lisible:
            raise Refus(motif)
        chemin = os.path.join(racine, *nom.split("/"))
        if lisible:
            octets = lire_source(chemin)
            if sha256_octets(octets) != entrees[nom]:
                raise Refus(MOTIF_LISTE)
            lus[nom] = octets
        elif empreinte_fichier(chemin) != entrees[nom]:
            raise Refus(MOTIF_LISTE)
    return lus


# --- LANCEMENT.md : identité et segments ---

def sections_du_lancement(lignes, motifs):
    sections, courante, precedent = [], (1, []), 1
    for ligne in lignes:
        m = motifs["en_tete_segment"].fullmatch(ligne)
        if m is None:
            courante[1].append(ligne)
            continue
        numero = int(m.group(1))
        if numero < 2 or numero not in (precedent, precedent + 1):
            raise Refus("segments.nombre")
        sections.append(courante)
        courante, precedent = (numero, []), numero
    sections.append(courante)
    return sections


def analyser_lancement(octets, table):
    """Identité et segments. La clé de course doit être la même sur les quatre lignes qui la portent (course,
    préenregistrement, organisme, registre), dans toutes les sections ; puis chaque champ d'identité doit garder une
    seule valeur d'un segment à l'autre."""
    motifs = table["_lignes"]
    sections = sections_du_lancement(decoder(octets, "sources.lancement").split("\n"), motifs)
    valeurs, cles, depot_1, reponse, porte = {}, set(), False, False, False

    def noter(champ, valeur):
        valeurs.setdefault(champ, set()).add(valeur)

    for rang, (_numero, section) in enumerate(sections):
        for ligne in section:
            m = motifs["course"].fullmatch(ligne)
            if m:
                cles.add(m.group(1))
                noter("chemin_pilote", m.group(2))
            m = motifs["depot_segment_1"].fullmatch(ligne)
            if m:
                noter("identite.commit", m.group(1))
                depot_1 = depot_1 or rang == 0
            m = motifs["depot_segment_suivant"].fullmatch(ligne)
            if m:
                noter("identite.commit", m.group(1))
            m = motifs["lanceur"].fullmatch(ligne)
            if m:
                noter("identite.lanceur", m.group(1))
                noter("identite.lanceur_empreinte", m.group(2))
            m = motifs["preenregistrement"].fullmatch(ligne)
            if m:
                noter("identite.texte_empreinte", m.group(1))
                noter("identite.graine", m.group(2))
                cles.add(m.group(3))
            m = motifs["organisme"].fullmatch(ligne)
            if m:
                noter("identite.nb_fichiers", m.group(1))
                noter("identite.arbre", m.group(2))
                cles.add(m.group(3))
                noter("identite.question_empreinte", m.group(4))
            m = motifs["registre"].fullmatch(ligne)
            if m:
                cles.add(m.group(1))
            m = motifs["code"].fullmatch(ligne)
            if m:
                noter("identite.noyau", m.group(1))
                noter("identite.banque_empreinte", m.group(2))
            if motifs["porte_m_precedente"].fullmatch(ligne):
                porte = True
            if motifs["reponse_archivee"].fullmatch(ligne):
                reponse = True
    if len(cles) > 1:
        raise Refus("releve.course")
    resultat = {"cle_course": cles.pop() if cles else MANQUE}
    for champ, ensemble in valeurs.items():
        if len(ensemble) > 1:
            raise Refus("releve.course" if champ == "chemin_pilote" else champ)
        resultat[champ] = ensemble.pop()
    if not depot_1:
        resultat.pop("identite.commit", None)
    resultat["porte"], resultat["reponse_archivee"] = porte, reponse
    resultat["segments"] = segments(sections, motifs)
    codes = [int(m.group(2)) for _n, section in sections for ligne in section
             for m in [motifs["fin_processus"].fullmatch(ligne)] if m is not None]
    resultat["dernier_code"] = codes[-1] if codes else MANQUE
    return resultat


def issue_section(section, motifs, numero):
    def present(nom):
        return any(motifs[nom].fullmatch(ligne) for ligne in section)

    stops = [m for ligne in section for m in [motifs["stop"].fullmatch(ligne)] if m is not None]
    if any(int(m.group(1)) != numero for m in stops):
        raise Refus("segments.{}.fin".format(numero))
    ordre = [("clore", "clore"), ("reprise_refusee", "reprise_refusee"), ("refus_lanceur", "refus_lanceur"),
             ("fermeture", "fermeture"), ("echec", "echec"), ("aucune_course", "aucune_course_partie")]
    fin = "stop" if stops else next((issue for nom, issue in ordre if present(nom)), MANQUE)
    processus = [m for ligne in section for m in [motifs["fin_processus"].fullmatch(ligne)] if m is not None]
    dernier = processus[-1] if processus else None
    return {"fin": fin, "heure_fin": dernier.group(1) if dernier else MANQUE,
            "code": int(dernier.group(2)) if dernier else MANQUE,
            "a_tourne": dernier is not None and fin != "reprise_refusee"}


def segments(sections, motifs):
    issues = {}
    for numero, section in sections:
        issues[numero] = issue_section(section, motifs, numero)
    for numero, issue in issues.items():
        if issue["fin"] != "stop":
            continue
        suivants = [n for n in issues if n > numero]
        if any(issues[n]["a_tourne"] for n in suivants):
            issue["fin"] = "stop_repris"
        elif suivants and issues[max(suivants)]["fin"] == "clore":
            issue["fin"] = "stop_clos"
        else:
            issue["fin"] = "stop_reprise_attendue"
    return issues


# --- Extrait mécanique ---

def analyser_extrait(octets, table):
    objet = charger_json(decoder(octets, "sources.extrait"), "sources.extrait")
    if not isinstance(objet, dict):
        raise Refus("sources.extrait")
    couverts, ignores = couvrir(objet, table["_chemins_extrait"], table)
    version = couverts.get(("extrait_version",), MANQUE)
    if type(version) is not int or version != table["extrait"]["version"]:
        raise Refus("sources.extrait")
    unites, evenements, haut = {}, {}, {}
    for chemin, valeur in couverts.items():
        if chemin[0] == "generations":
            unites.setdefault(chemin[1], {})[chemin[2:]] = valeur
        elif chemin[0] == "evenements":
            evenements.setdefault(chemin[1], {})[chemin[2:]] = valeur
        else:
            haut[chemin] = valeur
    # Lignée : le champ que nomme la table (source) ; ses autres mentions (clés de rapport.lignees et de
    # manifeste.organismes_imposes, préfixe des chemins d'unité) ne servent qu'au contrôle de cohérence.
    champ_lignee = table["_lignee_champ"]
    if any(not isinstance(u[champ_lignee], str) for u in unites.values() if champ_lignee in u):
        raise Refus("identite.lignee")
    lignees_champ = {u[champ_lignee] for u in unites.values() if champ_lignee in u}
    mentions = {c[2] for c in haut if c[:2] in (("rapport", "lignees"), ("manifeste", "organismes_imposes"))}
    par_unite = {}
    for rang in sorted(unites):
        u = unites[rang]
        chemin = u.get(("chemin",))
        parties = chemin.split("/") if isinstance(chemin, str) else []
        if len(parties) != 2 or re.fullmatch(r"[a-z][0-9]{3}", parties[1]) is None:
            raise Refus("unite")
        if parties[1] in par_unite:
            raise Refus("unite")
        if u.get(("importee",)) is not False:
            raise Refus("unite.importee")
        mentions.add(parties[0])
        par_unite[parties[1]] = u
    declarations = [e for _r, e in sorted(evenements.items()) if e.get(("etape",)) == "fin_conception"]
    if len(declarations) > 1:
        raise Refus("conception.declaration.ronde")
    stop = table["vocabulaires"]["arret_stop"]
    raisons = [e.get(("raison",)) for _r, e in sorted(evenements.items()) if e.get(("etape",)) == "arret"]
    return {"lignees_champ": lignees_champ, "lignees_mentions": mentions, "haut": haut, "unites": par_unite,
            "ignores": ignores,
            "declaration": declarations[0] if declarations else {},
            "stop": sum(1 for r in raisons if isinstance(r, str) and unicodedata.normalize("NFC", r) == stop)}


# --- Journaux d'appels ---

def analyser_journal(octets, unite, motif, table):
    """Rend les appels dédoublonnés (rôle, statut) d'un journal et le nombre de champs ignorés."""
    appels, ignores = {}, 0
    for rang, ligne in enumerate(decoder(octets, motif).split("\n")):
        if not ligne.strip():
            continue
        objet = charger_json(ligne, motif)
        if not isinstance(objet, dict):
            raise Refus(motif)
        couverts, nombre = couvrir(objet, table["_chemins_journal"], table)
        ignores += nombre
        role = identifiant(couverts.get(("role",)), "unite.{}.appels.role".format(unite))
        statut = identifiant(couverts.get(("statut",)), "unite.{}.appels.statut".format(unite))
        ident = couverts.get(("id",))
        cle = ("id", ident) if (isinstance(ident, str) and ident) or type(ident) is int else ("rang", rang)
        if cle in appels:
            if appels[cle] != (role, statut):
                raise Refus("unite.{}.appels".format(unite))
            continue
        appels[cle] = (role, statut)
    return list(appels.values()), ignores


def compter(valeurs):
    compte = {}
    for valeur in valeurs:
        compte[valeur] = compte.get(valeur, 0) + 1
    return compte


# --- Identité ---

def identite(lancement, extrait, table):
    """Champs d'identité ; refus si un champ exigé manque, si une valeur sort de la table close ou des questions."""
    l, ex = lancement or {}, extrait or {}
    haut = ex.get("haut", {})
    ident = {champ: MANQUE for champ in table["identite_exigee"]}
    cle, source_lignee = l.get("cle_course", MANQUE), MANQUE
    if cle is not MANQUE and "chemin_pilote" in l:
        entree = COURSES.get(cle)
        nom = re.sub(r"-tentative[0-9]+$", "", l["chemin_pilote"].rstrip("/").split("/")[-1])
        if entree is None or nom != entree[0]:
            raise Refus("releve.course")
        ident["releve.course"] = entree[0]
        valeurs = ex.get("lignees_champ", set())
        if valeurs and valeurs != {entree[1]}:
            raise Refus("identite.lignee")
        if ex.get("lignees_mentions", set()) - {entree[1]}:
            raise Refus("identite.lignee")
        source_lignee = "extrait" if valeurs else LIGNEE_DEDUITE
        ident["identite.lignee"] = identifiant(entree[1], "identite.lignee")
    for champ in ("identite.graine", "identite.arbre", "identite.question_empreinte", "identite.lanceur_empreinte",
                  "identite.commit"):
        ident[champ] = l.get(champ, MANQUE)
    if "identite.nb_fichiers" in l:
        ident["identite.nb_fichiers"] = r_entier(int(l["identite.nb_fichiers"]), "identite.nb_fichiers")
    if "identite.lanceur" in l:
        nom = l["identite.lanceur"][:-3] if l["identite.lanceur"].endswith(".sh") else l["identite.lanceur"]
        ident["identite.lanceur"] = identifiant(nom, "identite.lanceur")
    for champ in table["identite_exigee"]:
        if ident[champ] in (MANQUE, ABSENT):
            raise Refus(champ)
    question = table["questions"].get(ident["identite.question_empreinte"])
    if question is None:
        raise Refus("identite.question")
    graine_manifeste = haut.get(("manifeste", "entropie_seed_sequence"), MANQUE)
    if graine_manifeste is not MANQUE and graine_manifeste is not None:
        if type(graine_manifeste) is not int or graine_manifeste < 0:
            raise Refus("identite.graine_manifeste")
        graine_manifeste = str(graine_manifeste)
    return [
        ("identite.commit", ident["identite.commit"]),
        ("identite.arbre", ident["identite.arbre"]),
        ("identite.nb_fichiers", ident["identite.nb_fichiers"]),
        ("identite.graine", ident["identite.graine"]),
        ("identite.graine_manifeste", ou_absent(graine_manifeste)),
        ("identite.lanceur", ident["identite.lanceur"]),
        ("identite.lanceur_empreinte", ident["identite.lanceur_empreinte"]),
        ("identite.noyau", ou_absent(l.get("identite.noyau", MANQUE))),
        ("identite.banque_empreinte", ou_absent(l.get("identite.banque_empreinte", MANQUE))),
        ("identite.texte_empreinte", ou_absent(l.get("identite.texte_empreinte", MANQUE))),
        ("identite.question", question),
        ("identite.question_empreinte", ident["identite.question_empreinte"]),
        ("identite.lignee", ident["identite.lignee"]),
        ("identite.lignee_source", source_lignee),
        ("identite.porte_m_precedente", "oui" if l.get("porte") else ABSENT),
    ], ident["releve.course"]


# --- Construction du relevé ---

def construire(racine, script_empreinte, entrees, octets_liste, lus, table):
    nom_lancement, nom_extrait = table["lancement"]["fichier"], table["extrait"]["fichier"]
    lancement = analyser_lancement(lus[nom_lancement], table) if nom_lancement in lus else None
    extrait = analyser_extrait(lus[nom_extrait], table) if nom_extrait in lus else None
    journaux = sorted((n, table["_journal"].fullmatch(n).group(1)) for n in lus if table["_journal"].fullmatch(n))
    appels, ignores = {}, extrait["ignores"] if extrait else 0
    for k, (nom, unite) in enumerate(journaux, start=1):
        appels[unite], nombre = analyser_journal(lus[nom], unite, "sources.journal_appels.{}".format(k), table)
        ignores += nombre
    lignes_identite, course = identite(lancement, extrait, table)
    haut = extrait["haut"] if extrait else {}
    lignes = []

    def ajouter(cle, valeur):
        lignes.append((cle, valeur))

    # En-tête et sources.
    ajouter("releve.version", "1")
    ajouter("releve.script_empreinte", script_empreinte)
    ajouter("releve.heure", None)
    ajouter("releve.dossier", identifiant_exact(os.path.basename(racine), "releve.dossier"))
    ajouter("releve.course", course)
    ajouter("sources.liste_fermee", sha256_octets(octets_liste))
    ajouter("sources.liste_fermee_verifiee", "oui")
    ajouter("sources.extrait", entrees[nom_extrait] if nom_extrait in lus else ABSENT)
    for k, (nom, _unite) in enumerate(journaux, start=1):
        ajouter("sources.journal_appels.{}".format(k), entrees[nom])
    ajouter("sources.lancement", entrees[nom_lancement] if nom_lancement in lus else ABSENT)
    ajouter("sources.manifeste", ABSENT)
    ajouter("sources.champs_ignores", r_entier(ignores, "sources.champs_ignores"))
    lignes.extend(lignes_identite)

    # Segments et fin.
    issues = lancement["segments"]
    ajouter("segments.nombre", str(max(issues)))
    for k in sorted(issues):
        ajouter("segments.{}.fin".format(k), ou_absent(issues[k]["fin"]))
        ajouter("segments.{}.heure_fin".format(k), ou_absent(issues[k]["heure_fin"]))
        ajouter("segments.{}.code".format(k), r_entier(issues[k]["code"], "segments.{}.code".format(k)))
    fins = [v for c, v in haut.items() if c[:2] == ("rapport", "lignees") and c[3:] == ("fin",)]
    ajouter("fin.lignee", fin_lignee(fins[0] if fins else MANQUE, table))
    ajouter("fin.dernier_code", r_entier(lancement["dernier_code"], "fin.dernier_code"))
    ajouter("fin.liste_fermee_poussee", liste_poussee(lus.get(table["a_pousser"]["fichier"]), table))
    ajouter("fin.recherche_cles_faite", ABSENT)
    ajouter("fin.reprise_attendue", "non" if issues[max(issues)]["fin"] in ("fermeture", "clore") else "oui")

    # Unités.
    unites_extrait = extrait["unites"] if extrait else {}
    toutes = sorted(set(unites_extrait) | set(appels) | ({"g001"} if lancement["reponse_archivee"] else set()))
    for u in toutes:
        g = unites_extrait.get(u, {})
        ajouter("unite.{}.statut".format(u), r_identifiant(g.get(("statut",), MANQUE), "unite.{}.statut".format(u)))
        ajouter("unite.{}.duree".format(u), r_duree(g.get(("execution", "duree_s"), MANQUE), "unite.{}.duree".format(u)))
        ajouter("unite.{}.cout".format(u), r_montant(g.get(("cout_usd",), MANQUE), "unite.{}.cout".format(u)))
        if u in appels:
            ajouter("unite.{}.appels.total".format(u), str(len(appels[u])))
            for statut, n in sorted(compter(s for _r, s in appels[u]).items()):
                ajouter("unite.{}.appels.statut.{}".format(u, statut), str(n))
            for role, n in sorted(compter(r for r, _s in appels[u]).items()):
                ajouter("unite.{}.appels.role.{}".format(u, role), str(n))
        else:
            ajouter("unite.{}.appels.total".format(u), ABSENT)
        for source, n in sorted(recherches(g, u).items()):
            ajouter("unite.{}.recherches.{}".format(u, source), str(n))
        servie = "oui" if u == "g001" and lancement["reponse_archivee"] else ABSENT
        ajouter("unite.{}.question_servie".format(u), servie)

    # Conception.
    if appels:
        ajouter("conception.rondes_tournees", str(sum(1 for u in appels if u.startswith("c") and appels[u])))
    else:
        ajouter("conception.rondes_tournees", ABSENT)
    d = extrait["declaration"] if extrait else {}
    ajouter("conception.declaration.ronde", r_entier(d.get(("declaration", "ronde_conception"), MANQUE),
                                                     "conception.declaration.ronde"))
    ajouter("conception.declaration.motif", r_identifiant(d.get(("declaration", "critere"), MANQUE),
                                                          "conception.declaration.motif"))
    ajouter("conception.declaration.exemplaires", r_entier(d.get(("declaration", "n_exemplaires_isvd"), MANQUE),
                                                           "conception.declaration.exemplaires"))

    # Mutation (canal (d)) et fichiers.
    for u in toutes:
        g = unites_extrait.get(u, {})
        if u in appels:
            ajouter("mutation.{}.appels".format(u), str(sum(1 for r, _s in appels[u] if r == table["role_mutation"])))
        successeur = g.get(("successeur",), MANQUE)
        ajouter("mutation.{}.successeur_produit".format(u),
                r_oui_non(successeur, "mutation.{}.successeur_produit".format(u)))
        ajouter("mutation.{}.successeur_valide".format(u), successeur_valide(g, successeur))
        ajouter("mutation.{}.successeur_a_tourne".format(u), ABSENT)
        for motif, n in sorted(refus_noyau(g, u).items()):
            ajouter("mutation.{}.refus.{}".format(u, motif), str(n))
    for u in toutes:
        ajouter("fichier.{}.politique_endogene".format(u), ABSENT)

    # Mémoire et castes (générations notées).
    generations = [u for u in toutes if u.startswith("g")]
    for u in generations:
        ajouter("memoire.{}.taille".format(u), ABSENT)
        ajouter("memoire.{}.restauration".format(u), ABSENT)
    for u in generations:
        g = unites_extrait.get(u, {})
        ajouter("castes.{}.nombre".format(u), r_entier(g.get(("organisme", "n_castes_recrutees"), MANQUE),
                                                       "castes.{}.nombre".format(u)))
        ajouter("castes.{}.mitose".format(u), ABSENT)

    # Événements et totaux.
    ajouter("evenements.delai_depasse", somme_unites(unites_extrait, ("execution", "delai_depasse"), "bool",
                                                     "evenements.delai_depasse"))
    if appels:
        plafond = table["statut_plafond_contient"]
        ajouter("evenements.plafond_refus", str(sum(1 for u in appels for _r, s in appels[u] if plafond in s)))
    else:
        ajouter("evenements.plafond_refus", ABSENT)
    ajouter("evenements.stop", str(extrait["stop"]) if extrait else ABSENT)
    ajouter("course.cout_total", r_montant(haut.get(("rapport", "depense_totale_usd"), MANQUE), "course.cout_total"))
    ajouter("course.duree_totale", somme_unites(unites_extrait, ("execution", "duree_s"), "duree",
                                                "course.duree_totale"))
    ajouter("course.recherches_total", somme_unites(unites_extrait, ("n_recherches",), "entier",
                                                    "course.recherches_total"))
    ajouter("course.telechargements_total", somme_unites(unites_extrait, ("n_telechargements",), "entier",
                                                         "course.telechargements_total"))
    return lignes


def fin_lignee(valeur, table):
    if valeur is MANQUE or valeur is None:
        return ABSENT
    vocabulaire = table["vocabulaires"]["fin_lignee"]
    if not isinstance(valeur, str) or unicodedata.normalize("NFC", valeur) not in vocabulaire:
        raise Refus("fin.lignee")
    return vocabulaire[unicodedata.normalize("NFC", valeur)]


def liste_poussee(octets, table):
    if octets is None:
        return ABSENT
    noms = set(decoder(octets, "fin.liste_fermee_poussee").split("\n"))
    liste = table["liste_fermee"]
    return "oui" if liste["fichier"] in noms and liste["compagnon"] in noms else "non"


def recherches(g, u):
    """Recherches par source (identifiant strict), tous statuts sommés."""
    motif, sommes = "unite.{}.recherches".format(u), {}
    for chemin, valeur in g.items():
        if chemin[:2] != ("services", "recherches") or len(chemin) != 4:
            continue
        source = identifiant(chemin[2], motif)
        if type(valeur) is not int or valeur < 0:
            raise Refus(motif)
        sommes[source] = sommes.get(source, 0) + valeur
    return sommes


def successeur_valide(g, successeur):
    if successeur is not True:
        return ABSENT
    if g.get(("problemes_successeur",), MANQUE) == []:
        return "oui"
    if any(c[0] == "problemes_successeur" and len(c) == 2 for c in g):
        return "non"
    return ABSENT


def refus_noyau(g, u):
    """Refus du noyau par motif ; une liste non vide d'éléments non simples fait refuser (rien n'est perdu en silence)."""
    if not g:
        return {}
    motif = "mutation.{}.refus".format(u)
    elements = [v for c, v in g.items() if c[0] == "refus_noyau" and len(c) == 2]
    if g.get(("refus_noyau",), MANQUE) != [] and not elements:
        raise Refus(motif)
    return compter(identifiant(v, motif) for v in elements)


def somme_unites(unites, chemin, forme, motif):
    """Somme exacte d'un champ sur toutes les unités de l'extrait ; absent si une unité ne le porte pas."""
    if not unites:
        return ABSENT
    total = decimal.Decimal(0) if forme == "duree" else 0
    for _u, g in sorted(unites.items()):
        valeur = g.get(chemin, MANQUE)
        if forme == "bool":
            if type(valeur) is not bool:
                return ABSENT
            total += int(valeur)
            continue
        if valeur is MANQUE or valeur is None:
            return ABSENT
        if forme == "entier":
            if type(valeur) is not int or valeur < 0:
                raise Refus(motif)
            total += valeur
        else:
            total += decimal.Decimal(decimal_exact(valeur, motif))
    return r_duree(total, motif) if forme == "duree" else r_entier(total, motif)


# --- Grammaire fermée et écriture exclusive ---

def motif_de_cle(cle, motif_table):
    """Motif de refus : la clé, ses segments de données (rôle, statut, source, motif) masqués."""
    masques = ("<role>", "<statut>", "<source>", "<motif>")
    return ".".join(m if m in masques else p for p, m in zip(cle.split("."), motif_table.split(".")))


def valider(lignes, table):
    for cle, valeur in lignes:
        trouves = [(motif, formes) for motif, regex, formes in table["_cles"] if regex.fullmatch(cle)]
        if len(trouves) != 1:
            raise Refus("releve")
        motif, formes = trouves[0]
        if not isinstance(valeur, str) or not any(table["_formes"][f].fullmatch(valeur) for f in formes):
            raise Refus(motif_de_cle(cle, motif))
        if re.fullmatch(r"[0-9]+[.,][0-9]+", valeur):
            raise Refus(motif_de_cle(cle, motif))


def ecrire_exclusif(dossier, nom, contenu):
    final = os.path.join(dossier, nom)
    temporaire = os.path.join(dossier, ".{}.{}.partiel".format(nom, os.getpid()))
    fd = os.open(temporaire, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_CLOEXEC", 0), 0o644)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(contenu)
            f.flush()
            os.fsync(f.fileno())
        try:
            os.link(temporaire, final)
        except FileExistsError:
            raise Refus("releve.existant")
    finally:
        os.unlink(temporaire)


def principal(argv):
    if len(argv) != 3:
        raise Usage("deux arguments : DOSSIER_DE_COURSE DOSSIER_DE_SORTIE")
    script = os.path.abspath(__file__)
    octets_script = lire_piece(script)
    verifier_compagnon_script(octets_script, script)
    table = charger_table(os.path.join(os.path.dirname(script), NOM_TABLE))
    racine, sortie = verifier_dossiers(argv[1], argv[2])
    dossier = identifiant_exact(os.path.basename(racine), "releve.dossier")
    nom_releve = "releve-mecanique-{}-{}.txt".format(dossier, VERSION_RELEVE)
    for nom in (nom_releve, nom_releve + ".sha256"):
        if os.path.lexists(os.path.join(sortie, nom)):
            raise Refus("releve.existant")
    octets_liste, entrees = lire_liste_fermee(racine, table)
    balayer(racine)
    lus = verifier_et_lire(racine, entrees, table)
    lignes = construire(racine, sha256_octets(octets_script), entrees, octets_liste, lus, table)
    heure = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    lignes = [(cle, heure if cle == "releve.heure" else valeur) for cle, valeur in lignes]
    valider(lignes, table)
    contenu = "".join("{} = {}\n".format(cle, valeur) for cle, valeur in lignes).encode("utf-8")
    empreinte = sha256_octets(contenu)
    ecrire_exclusif(sortie, nom_releve, contenu)
    ecrire_exclusif(sortie, nom_releve + ".sha256", "{}  {}\n".format(empreinte, nom_releve).encode("utf-8"))
    dire(sys.stdout, "relevé écrit : {} {}".format(nom_releve, empreinte))
    return 0


def dire(flux, texte):
    """Écrit une ligne en UTF-8, quelle que soit la langue du système."""
    flux.flush()
    flux.buffer.write((texte + "\n").encode("utf-8"))
    flux.buffer.flush()


def lancer():
    try:
        code = principal(sys.argv)
    except Usage as e:
        dire(sys.stderr, "USAGE : {}".format(e.args[0]))
        code = 2
    except Refus as e:
        dire(sys.stderr, "REFUS : {}".format(e.args[0]))
        code = 3
    except Exception as e:
        trace = e.__traceback__
        while trace.tb_next is not None:
            trace = trace.tb_next
        dire(sys.stderr, "ERREUR INTERNE : {} ligne {}".format(type(e).__name__, trace.tb_lineno))
        code = 4
    sys.exit(code)


if __name__ == "__main__":
    lancer()
