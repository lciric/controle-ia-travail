#!/usr/bin/env python3
"""Version servie v2 de la question v8 au collisionneur (« modes de sabotage ») : retrait, par programme, des renvois
internes que la garde de motifs refuse, plus une liste fermée de retraits nommés hors de la garde, puis vérifications.
Sans réseau.

v2 (23 novembre 2026, Claude Opus 5.5, sous-agent ; pièce d'instrument, classe B, à contre-lire par un autre modèle) :
copie de produire_version_servie_v1.py (dad030a2…, gardée, R12), sur la décision de la mère (étage 2) qui suit la
vérification des corrections du devis (verification-corrections-devis-v8-v1.md, 64045cf7…). Changements :
- N-1 : une seconde liste fermée et scellée, de paires SUPPLÉMENTAIRES NOMMÉES (nom, raison), hors de la garde : chacune
  est trouvée exactement une fois, dans la zone permise, sans motif de la garde (sinon elle relève de la première
  liste), sans chevauchement ;
- N-5 : mention plus légère, « [renvoi retiré] » ;
- N-4 : empreintes des moteurs fixées dans le programme (MOTEURS_ATTENDUS), au moins les révisions 8d et 8m ; listes
  contrôlées dans leur forme (une liste malformée est un arrêt nommé, jamais une trace) ; restes cherchés aussi sous une
  forme générale (tout chemin entre accents graves, toute empreinte de commit de 40 caractères hexadécimaux) ;
- noms des sorties en v2 ; le reste est la v1.

Dans l'ordre ; tout écart arrête (code 2) avant toute écriture :
1. lit la v8 et vérifie son empreinte (EMPREINTE_V8), son encodage et ses fins de ligne ;
2. prend le texte depuis le titre, comme la ligne 1 de la v8 le prescrit ;
3. lit les deux listes, vérifie leur forme et leur sceau ; chaque ancien figure une seule fois, à la ligne dite ;
4. dérive de la garde de chaque moteur (révisions fixées) ce qu'elle refuse, élargi au jeton entier ; la liste de la
   garde doit être exactement cette dérivation ; les paires supplémentaires n'ont aucun motif de la garde ;
5. applique les deux listes et vérifie : reconstruction au caractère près, zone, reste identique hors zone, lignes,
   repères, aucun reste, garde nulle sur le texte servi et sur les invites du tour III.1 de chaque moteur, témoin sur la
   v8, différentiel unifié limité aux lignes des paires ;
6. écrit, sans jamais écraser : la version servie, le différentiel unifié, le compte rendu, chacun avec son .sha256.

Usage :
  PYTHONPATH=src python3 produire_version_servie_v2.py --v8 QUESTION_V8.md --paires-garde LISTE.json \
      --paires-supplementaires LISTE.json --sortie DOSSIER --temp DOSSIER_DE_TRAVAIL --moteur NOM CHEMIN [...]
Codes de sortie : 0 fini ; 1 fichier illisible ; 2 vérification en échec, rien n'est écrit.
"""
import argparse
import datetime
import difflib
import hashlib
import importlib.util
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

VERSION = "produire-version-servie-v2"
EMPREINTE_V8 = "047eeddff0285f41938be0ade4927f6d5dacdfe98f348a05f61bf97aaf53e80a"
MENTION = "[renvoi retiré]"
NOM_V8 = "question-collisionneur-modes-sabotage-v8.md"
NOM_SERVIE = "question-collisionneur-modes-sabotage-v8-servie-v2.md"
NOM_DIFF = "diff-v8-vers-version-servie-v2.diff"
NOM_COMPTE_RENDU = "sortie-produire-version-servie-v2.txt"
REGLE_LIGNE_1 = "Le texte à servir commence au titre ; ce bloc n'en fait pas partie."
DEBUT_TITRE = "# Question au collisionneur"
CATEGORIES_GARDE = ("chemin interne", "identifiant d'accord")
JETON_CHEMIN = re.compile(r"`[A-Za-z0-9_./-]+`")  # entier : un chemin entre accents graves, sans blanc
ACCORD_ELARGI = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d+(?:\s+(?:et|à)\s+-\d+)*")  # identifiant et suite abrégée
ZONE = {77, 78} | set(range(155, 180))  # lignes de la v8 : faits 16 et 17, table des sources (§ 7)
MOTEURS_ATTENDUS = {  # N-4 : empreintes fixées ; révisions 8 à 8d sur main, 8e à 8p sur runs/collisionneurs-reprise-v8d-v1
    "v8": "b85690310f5c4832a540bebe1156eb64caf98702cb0ed3d771933e1efac35d72",
    "v8b": "6cd0209c10118ff58d5ad3b6e2cc3e3c52c33aa155db2df96f53b9d5786f4c9b",
    "v8c": "a3fc279ed1754db250016131656671d0639d03749bc62dff88b99a2b72b5b531",
    "v8d": "b780383874598f12b24c79e4087d335c8e01cda685e295f5116898fa3b1715ac",
    "v8e": "0d591933032e249d17d618e406fe6390ee2536569abc9a232289168122186957",
    "v8f": "445fe2d37eebbda1aede9a7e7351a394dbdfdf9d0c907ffa86eaafde9363001e",
    "v8g": "93f96e95b5c1b73cbcd378b235eb1177546e284829486c87948d9b59cc194317",
    "v8h": "d9b41b11b5f9d66ff8b3fa752ad8632dd9a796937d5ca1862c8c86400e9a9ae8",
    "v8i": "7c7aa7131c77f749ef02a554581a429277303f294e33b9d05824f4f3f206a29a",
    "v8j": "d199a14b5b8102eed2df3841587aa66a6acaae81c9cf4aa16b8f47e76875736d",
    "v8k": "cc886ae7986179274621b74194dca1d1f73943456aac36ee1f58487a7a6b63e7",
    "v8l": "da282cf752ed43940bba8a4acb41a89c8256ae1650afdacc29ae0baba04779e1",
    "v8m": "420394f9d803bc4eb41f0e469a30e0be647e11a2c91ac9f42e70c90fdb31c377",
    "v8n": "4bd86e650893fcaa6b1fea5c8149dd5043176c6f828c1199f6e86e788433c191",
    "v8o": "81c1ca2212eab4b65164b2b1afac6edc37c854da6e43223091a1fb91cb8cf9bd",
    "v8p": "5979c712101034265d5a7dcacc2110b691f97e69b3c4158d8a3c6c2af6704290",
}
MOTEURS_EXIGES = ("v8d", "v8m")  # les deux révisions qui peuvent servir ce service
RESTES = (  # aucun ne doit rester dans le texte servi
    ("identifiant d'accord", re.compile(r"\bGO-")),
    ("identifiant de registre", re.compile(r"\bR-\d{3,5}\b")),
    ("suite abrégée d'un identifiant (élargi)", re.compile(r"(?<![\w.\-])-\d+")),
    ("suite abrégée d'un identifiant (contre-lecture, D-3)", re.compile(r"-13[5-9]\b")),
    ("chemin interne entre accents graves (racines du dépôt)", re.compile(
        r"`(?:brouillons|diag|docs|donnees|gemini|livrables|papiers|prereg|rapports|registres|runs|scripts|src|tests|"
        r"traces|archives-reponses-modeles)/")),
    ("chemin entre accents graves (forme générale)", re.compile(r"`[^`\s]*/[^`\s]*`")),
    ("empreinte de commit (40 caractères hexadécimaux)", re.compile(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])")),
    ("nom du dépôt", re.compile(r"controle-ia")),
)
COMPTES = (("identifiant public de l'article (dans quatre chemins retirés)", re.compile(r"2606\.08892")),)
ESPECES_INVITE = ["opus", "argon", "astra", "carbon", "neon"]  # composition recommandée par le devis
TOUR_INVITE = "E3-T1"  # seul tour dont l'invite ne dépend d'aucune cellule


class Echec(Exception):
    """Vérification en échec : rien n'est écrit."""


def empreinte(octets):
    return hashlib.sha256(octets).hexdigest()


def numero_ligne(texte, position, decalage=0):
    return texte.count("\n", 0, position) + 1 + decalage


def charger_moteur(nom, chemin):
    """Charge un moteur dont l'empreinte est fixée par MOTEURS_ATTENDUS ; aucun appel réseau au chargement."""
    if nom not in MOTEURS_ATTENDUS:
        raise Echec(f"moteur {nom!r} inconnu : seuls {sorted(MOTEURS_ATTENDUS)} sont admis")
    h = empreinte(Path(chemin).read_bytes())
    if h != MOTEURS_ATTENDUS[nom]:
        raise Echec(f"moteur {nom} : empreinte {h} ≠ empreinte fixée {MOTEURS_ATTENDUS[nom]}")
    spec = importlib.util.spec_from_file_location(f"moteur_{nom}", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    for attribut in ("VERSION", "MOTIFS_INTERDITS", "motifs_trouves", "garder_motifs", "construire_prompt",
                     "fixer_composition", "ecrire_neuf", "id_cellule"):
        if not hasattr(m, attribut):
            raise Echec(f"moteur {nom} : « {attribut} » absent")
    return m, h


def lire_liste(chemin, supplementaire):
    """Lit une liste de paires, vérifie son sceau (.sha256 compagnon) et sa forme ; renvoie (liste, empreinte)."""
    octets = Path(chemin).read_bytes()
    h = empreinte(octets)
    sceau = Path(str(chemin) + ".sha256").read_text(encoding="utf-8").split()
    if not sceau or sceau[0] != h:
        raise Echec(f"liste {Path(chemin).name} : empreinte {h} ≠ son sceau")
    try:
        liste = json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise Echec(f"liste {Path(chemin).name} illisible : {e}")
    cles = {"n": int, "ligne_v8": int, "categorie": str, "ancien": str, "nouveau": str}
    if supplementaire:
        cles.update(nom=str, raison=str)
    if not isinstance(liste, dict) or not isinstance(liste.get("paires"), list) or not liste["paires"]:
        raise Echec(f"liste {Path(chemin).name} malformée : il faut un objet avec une liste « paires » non vide")
    if not isinstance(liste.get("source"), dict) or liste["source"].get("sha256") != EMPREINTE_V8:
        raise Echec(f"liste {Path(chemin).name} : source autre que la v8 ({EMPREINTE_V8[:8]}…)")
    if liste.get("mention") != MENTION:
        raise Echec(f"liste {Path(chemin).name} : mention {liste.get('mention')!r} ≠ {MENTION!r}")
    for i, q in enumerate(liste["paires"], 1):
        if not isinstance(q, dict):
            raise Echec(f"liste {Path(chemin).name} malformée : paire {i} n'est pas un objet")
        for cle, genre in cles.items():
            if not isinstance(q.get(cle), genre) or isinstance(q.get(cle), bool) or (genre is str and not q[cle].strip()):
                raise Echec(f"liste {Path(chemin).name} malformée : paire {i}, champ « {cle} » absent, vide ou mal typé")
        if q["nouveau"] != MENTION:
            raise Echec(f"liste {Path(chemin).name} : paire {i}, nouveau {q['nouveau']!r} ≠ mention constante")
    return liste, h


def occurrences(m, texte):
    """Toutes les occurrences des motifs du moteur (sa fonction motifs_trouves ne rend que la première par catégorie)."""
    return [(categorie, x.start(), x.end(), x.group(0))
            for categorie, motif in m.MOTIFS_INTERDITS for x in motif.finditer(texte)]


def deriver(base, occs):
    """Ce que la garde refuse, élargi au jeton entier : [(debut, fin, categorie, ancien, occurrences)], dans l'ordre."""
    jetons = {}
    for categorie, deb, fin, trouve in occs:
        if categorie not in CATEGORIES_GARDE:
            raise Echec(f"catégorie « {categorie} » au caractère {deb} : hors du retrait admis")
        if categorie == "chemin interne":
            debut_ligne = base.rfind("\n", 0, deb) + 1
            fin_ligne = base.find("\n", deb)
            fin_ligne = len(base) if fin_ligne == -1 else fin_ligne
            g, d = base.rfind("`", debut_ligne, deb), base.find("`", fin, fin_ligne)
            if g == -1 or d == -1:
                raise Echec(f"chemin interne au caractère {deb} hors d'un jeton entre accents graves")
            a, b = g, d + 1
            if not JETON_CHEMIN.fullmatch(base[a:b]) or "/" not in base[a:b]:
                raise Echec(f"jeton {base[a:b]!r} autour du caractère {deb} : pas un chemin seul")
        else:
            x = ACCORD_ELARGI.match(base, deb)
            if x is None:
                raise Echec(f"identifiant d'accord au caractère {deb} : forme inattendue")
            a, b = deb, x.end()
        entree = jetons.setdefault((a, b), [a, b, categorie, base[a:b], []])
        if entree[2] != categorie:
            raise Echec(f"jeton {base[a:b]!r} : deux catégories")
        entree[4].append(trouve)
    ordre = [tuple(jetons[k]) for k in sorted(jetons)]
    for j1, j2 in zip(ordre, ordre[1:]):
        if j2[0] < j1[1]:
            raise Echec(f"jetons qui se chevauchent : {j1[3]!r} et {j2[3]!r}")
    return ordre


def placer(base, liste, nom_liste):
    """Place chaque ancien (une seule fois, à la ligne dite) ; renvoie [(debut, fin, categorie, ancien, n, nom)]."""
    rendu = []
    for q in liste["paires"]:
        compte = base.count(q["ancien"])
        if compte != 1:
            raise Echec(f"{nom_liste}, paire {q['n']} : ancien {q['ancien']!r} trouvé {compte} fois (une exigée)")
        deb = base.find(q["ancien"])
        if numero_ligne(base, deb, 2) != q["ligne_v8"]:
            raise Echec(f"{nom_liste}, paire {q['n']} : ancien à la ligne {numero_ligne(base, deb, 2)} de la v8, la liste "
                        f"dit {q['ligne_v8']}")
        rendu.append((deb, deb + len(q["ancien"]), q["categorie"], q["ancien"], q["n"], q.get("nom")))
    return sorted(rendu)


def reperes(texte):
    """Titres, numéros en début de ligne, rubriques en gras, étiquettes de sources et statuts, dans l'ordre."""
    lignes = texte.split("\n")
    return {
        "titres": [l for l in lignes if l.startswith("#")],
        "numeros": [re.match(r"^\s*(\d+)\.\s", l).group(1) for l in lignes if re.match(r"^\s*(\d+)\.\s", l)],
        "rubriques": re.findall(r"^\s*\d+\. \*\*([^*]+)\*\*", texte, flags=re.M),
        "sources": re.findall(r"\[source (\d+)", texte),
        "statuts": re.findall(r"VÉRIFIÉ, DIT EN SUBSTANCE|VÉRIFIÉ|RAPPORTÉ|HYPOTHÈSE", texte),
    }


def reste_hors_zone(texte):
    """Le texte sans les lignes de la zone (numérotées comme dans la v8 : ligne k du texte = ligne k + 2 de la v8)."""
    return "\n".join(l for k, l in enumerate(texte.split("\n"), 3) if k not in ZONE)


def invites_tour(m, servi, temp):
    """Construit l'invite du tour III.1 de chaque lettre, texte servi en faits et en question ; [(cellule, longueur,
    occurrences)]."""
    dossier = Path(tempfile.mkdtemp(prefix="invite-", dir=temp))
    try:
        m.fixer_composition(list(ESPECES_INVITE))
        m.ecrire_neuf(dossier / "faits.md", servi)
        m.ecrire_neuf(dossier / "question-etage3.md", servi)
        rendu = []
        for lettre in m.LETTRES:
            prompt, _ = m.construire_prompt(dossier, TOUR_INVITE, lettre, [], set())
            cid = m.id_cellule(TOUR_INVITE, lettre)
            occ = occurrences(m, prompt)
            if not occ:
                m.garder_motifs(None, cid, prompt)  # la fonction même du moteur : ne doit rien lever
            rendu.append((cid, len(prompt), occ))
        return rendu
    except Exception as e:  # tout arrêt du moteur ici est un échec nommé, jamais avalé
        raise Echec(f"moteur {getattr(m, 'VERSION', '?')} : invite du tour III.1 non construite ou refusée "
                    f"({type(e).__name__} : {e})")
    finally:
        shutil.rmtree(dossier, ignore_errors=True)


def principal(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--v8", required=True)
    p.add_argument("--paires-garde", required=True)
    p.add_argument("--paires-supplementaires", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--temp", required=True)
    p.add_argument("--moteur", nargs=2, action="append", metavar=("NOM", "CHEMIN"), required=True)
    a = p.parse_args(argv)
    cr = [f"Compte rendu de {VERSION} ; script {Path(__file__).name}, sha256 {empreinte(Path(__file__).read_bytes())} ; "
          f"{datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}.", ""]
    try:
        sortie, temp = Path(a.sortie), Path(a.temp)
        for nom in (NOM_SERVIE, NOM_DIFF, NOM_COMPTE_RENDU):
            for chemin in (sortie / nom, sortie / (nom + ".sha256")):
                if chemin.exists():
                    raise Echec(f"{chemin} existe déjà : rien n'est écrasé (R12)")
        noms = [n for n, _ in a.moteur]
        if len(set(noms)) != len(noms) or any(n not in noms for n in MOTEURS_EXIGES):
            raise Echec(f"moteurs : chacun une fois, et au moins {list(MOTEURS_EXIGES)}")
        temp.mkdir(parents=True, exist_ok=True)
        # 1. la v8
        octets = Path(a.v8).read_bytes()
        h_v8 = empreinte(octets)
        if h_v8 != EMPREINTE_V8:
            raise Echec(f"v8 : empreinte {h_v8} ≠ {EMPREINTE_V8}")
        texte_v8 = octets.decode("utf-8")
        if "\r" in texte_v8:
            raise Echec("v8 : fins de ligne autres que LF")
        cr.append(f"1. v8 : {Path(a.v8).name}, sha256 {h_v8} (attendue), {len(octets)} octets, UTF-8, LF seules : tenu.")
        # 2. depuis le titre
        lignes_v8 = texte_v8.split("\n")
        if not (lignes_v8[0].startswith("> ") and REGLE_LIGNE_1 in lignes_v8[0]):
            raise Echec("v8 : la ligne 1 n'est pas le bloc d'en-tête qui prescrit de servir depuis le titre")
        if lignes_v8[1] != "" or not lignes_v8[2].startswith(DEBUT_TITRE):
            raise Echec("v8 : ligne 2 non vide ou ligne 3 qui n'est pas le titre")
        base = "\n".join(lignes_v8[2:])
        if MENTION in texte_v8:
            raise Echec("la mention constante figure déjà dans la v8 : la reconstruction serait ambiguë")
        cr.append(f"2. Texte depuis le titre (ligne 1 de la v8 : « {REGLE_LIGNE_1} ») : lignes 1 et 2 de la v8 "
                  f"retirées ; {len(base)} caractères ; mention « {MENTION} » absente de la v8 : tenu.")
        # 3. les deux listes fermées
        liste_g, h_g = lire_liste(a.paires_garde, False)
        liste_s, h_s = lire_liste(a.paires_supplementaires, True)
        garde = placer(base, liste_g, "liste de la garde")
        supp = placer(base, liste_s, "liste supplémentaire")
        cr.append(f"3. Listes fermées, sceaux et forme tenus : {Path(a.paires_garde).name} (sha256 {h_g}), {len(garde)} "
                  f"paires ; {Path(a.paires_supplementaires).name} (sha256 {h_s}), {len(supp)} paires nommées ; chaque "
                  f"ancien trouvé exactement une fois, à la ligne dite : tenu.")
        # 4. dérivation indépendante par la garde de chaque moteur
        moteurs = []
        for nom, chemin in a.moteur:
            m, h = charger_moteur(nom, chemin)
            moteurs.append((nom, chemin, h, m))
        reference = occurrences(moteurs[0][3], base)
        if not reference:
            raise Echec("aucune occurrence sur la v8 : le témoin ne voit rien")
        cr.append("4. Garde de motifs sur la v8 depuis le titre (témoin, R5), par moteur (empreintes fixées) :")
        for nom, chemin, h, m in moteurs:
            occ = occurrences(m, base)
            if occ != reference:
                raise Echec(f"moteur {nom} : occurrences différentes de celles du premier moteur")
            compte = {}
            for categorie, *_ in occ:
                compte[categorie] = compte.get(categorie, 0) + 1
            cr.append(f"   {nom} ({m.VERSION}, sha256 {h}) : {len(occ)} occurrences {compte}")
        derive = deriver(base, reference)
        if [(d[0], d[1], d[2], d[3]) for d in derive] != [(q[0], q[1], q[2], q[3]) for q in garde]:
            raise Echec("la liste de la garde n'est pas exactement ce que la garde refuse, élargi au jeton entier")
        cr.append(f"   Dérivé de la garde, élargi au jeton entier : {len(derive)} jetons, identiques à la liste de la "
                  f"garde, dans le même ordre : tenu.")
        for deb, fin, categorie, ancien, n, nom in supp:
            if any(motif.search(ancien) for _, _, _, mm in moteurs for _, motif in mm.MOTIFS_INTERDITS):
                raise Echec(f"liste supplémentaire, paire {n} ({nom}) : porte un motif de la garde, elle relève de la "
                            f"liste de la garde")
            if any(deb < g[1] and g[0] < fin for g in garde):
                raise Echec(f"liste supplémentaire, paire {n} ({nom}) : chevauche un jeton de la garde")
        cr.append("   Paires supplémentaires : aucun motif de la garde, aucun chevauchement : tenu.")
        # 5. application et vérifications
        paires = sorted([q[:5] + ("garde",) for q in garde] + [q[:4] + (q[4], f"supplémentaire : {q[5]}") for q in supp])
        servi = base
        for deb, fin, *_ in reversed(paires):
            servi = servi[:deb] + MENTION + servi[fin:]
        cr.append(f"5. Remplacements par « {MENTION} » : {len(paires)} ({len(garde)} de la garde, couvrant "
                  f"{len(reference)} occurrences et les suites abrégées ; {len(supp)} supplémentaires nommés) :")
        for i, (deb, fin, categorie, ancien, n, origine) in enumerate(paires, 1):
            cr.append(f"   {i:2d}. ligne {numero_ligne(base, deb, 2)} de la v8 (ligne {numero_ligne(base, deb)} de la "
                      f"version servie), {categorie}, ancien {ancien!r} ; {origine}, paire {n}")
        morceaux = servi.split(MENTION)
        if len(morceaux) != len(paires) + 1:
            raise Echec("nombre de mentions dans la version servie ≠ nombre de paires")
        reconstruit = morceaux[0] + "".join(q[3] + morceaux[i + 1] for i, q in enumerate(paires))
        if reconstruit != base:
            raise Echec("remettre les anciens ne redonne pas la v8 depuis son titre")
        cr.append("5a. Anciens remis à la place des mentions : la v8 depuis son titre est redonnée au caractère près : "
                  "tenu.")
        for deb, fin, categorie, ancien, n, origine in paires:
            k = numero_ligne(base, deb, 2)
            if k not in ZONE:
                raise Echec(f"paire {n} ({origine}) : ligne {k} de la v8 hors de la zone permise")
        h_reste_base, h_reste_servi = (empreinte(reste_hors_zone(t).encode("utf-8")) for t in (base, servi))
        if h_reste_base != h_reste_servi:
            raise Echec("le texte change hors de la zone permise")
        cr.append(f"5b. Tout ancien dans la zone permise (lignes 77, 78 et 155 à 179 de la v8) ; hors de la zone, texte "
                  f"identique (empreinte du reste, de part et d'autre : {h_reste_base}) : tenu.")
        lb, ls = base.split("\n"), servi.split("\n")
        if len(lb) != len(ls):
            raise Echec("nombre de lignes changé")
        portent = {numero_ligne(base, q[0]) - 1 for q in paires}
        different = {i for i, (x, y) in enumerate(zip(lb, ls)) if x != y}
        if different != portent:
            raise Echec(f"lignes changées {sorted(different)} ≠ lignes qui portaient un ancien {sorted(portent)}")
        for i in sorted(different):
            siennes = [q[3] for q in paires if numero_ligne(base, q[0]) - 1 == i]
            bouts = ls[i].split(MENTION)
            if len(bouts) != len(siennes) + 1 or bouts[0] + "".join(s + bouts[j + 1] for j, s in enumerate(siennes)) != lb[i]:
                raise Echec(f"ligne {i + 3} de la v8 : la différence n'est pas exactement ses paires")
        cr.append(f"5c. {len(ls)} lignes de part et d'autre ; seules diffèrent les {len(different)} lignes qui portaient "
                  f"un ancien (lignes {', '.join(str(i + 3) for i in sorted(different))} de la v8), chacune redonnée "
                  f"par ses seules paires : tenu.")
        rb, rs = reperes(base), reperes(servi)
        for cle in rb:
            if rb[cle] != rs[cle]:
                raise Echec(f"repères « {cle} » changés")
        cr.append(f"5d. Repères identiques : {len(rb['titres'])} titres, {len(rb['numeros'])} numéros en début de ligne, "
                  f"{len(rb['rubriques'])} rubriques en gras, {len(rb['sources'])} étiquettes de sources "
                  f"(numéros {sorted(set(int(s) for s in rb['sources']))}), {len(rb['statuts'])} statuts : tenu.")
        cr.append("5e. Restes dans le texte servi (aucun admis) :")
        for nom, motif in RESTES:
            avant, apres = len(motif.findall(base)), len(motif.findall(servi))
            if apres:
                raise Echec(f"reste « {nom} » : {apres} dans le texte servi")
            cr.append(f"   {nom} : {avant} dans la v8 depuis le titre, 0 dans le texte servi")
        for nom, motif in COMPTES:
            cr.append(f"   compté seulement — {nom} : {len(motif.findall(base))} dans la v8 depuis le titre, "
                      f"{len(motif.findall(servi))} dans le texte servi")
        cr.append("5f. Garde de motifs sur la version servie, par moteur :")
        for nom, chemin, h, m in moteurs:
            occ = occurrences(m, servi)
            premiere = m.motifs_trouves(servi)
            if occ or premiere:
                raise Echec(f"moteur {nom} : la version servie porte encore {occ or premiere}")
            invites = invites_tour(m, servi, temp)
            for cid, longueur, occ_invite in invites:
                if occ_invite:
                    raise Echec(f"moteur {nom} : invite {cid} refusée : {occ_invite}")
            cr.append(f"   {nom} ({m.VERSION}) : texte servi, 0 occurrence ; invites du tour III.1 "
                      f"({', '.join(f'{c} {n} car.' for c, n, _ in invites)}), 0 occurrence, aucun refus : tenu.")
        diff = "".join(difflib.unified_diff(texte_v8.splitlines(keepends=True), servi.splitlines(keepends=True),
                                            fromfile=f"a/{NOM_V8}", tofile=f"b/{NOM_SERVIE}", n=3))
        retirees = [l[1:] for l in diff.splitlines(keepends=True) if l.startswith("-") and not l.startswith("---")]
        ajoutees = [l[1:] for l in diff.splitlines(keepends=True) if l.startswith("+") and not l.startswith("+++")]
        attendu_retirees = [lignes_v8[0] + "\n", "\n"] + [lb[i] + "\n" for i in sorted(different)]
        attendu_ajoutees = [ls[i] + "\n" for i in sorted(different)]
        if retirees != attendu_retirees or ajoutees != attendu_ajoutees:
            raise Echec("le différentiel unifié porte sur d'autres lignes que la tête et les lignes des paires")
        cr.append(f"5g. Différentiel unifié : {len(retirees)} lignes retirées (les 2 lignes de tête et les "
                  f"{len(different)} lignes des paires), {len(ajoutees)} lignes ajoutées (les mêmes, mention à la place "
                  f"de l'ancien), rien d'autre : tenu.")
        # 6. écritures, sans écraser
        sortie.mkdir(parents=True, exist_ok=True)

        def ecrire(nom, texte):
            chemin = sortie / nom
            with open(chemin, "x", encoding="utf-8", newline="\n") as f:
                f.write(texte)
            h = empreinte(texte.encode("utf-8"))
            with open(str(chemin) + ".sha256", "x", encoding="utf-8", newline="\n") as f:
                f.write(f"{h}  {nom}\n")
            return h

        h_servie = ecrire(NOM_SERVIE, servi)
        h_diff = ecrire(NOM_DIFF, diff)
        n_chemins = sum(1 for q in garde if q[2] == "chemin interne")
        n_occ_chemins = sum(1 for o in reference if o[0] == "chemin interne")
        n_accords = sum(1 for q in garde if q[2] == "identifiant d'accord")
        cr.append("")
        cr.append(f"6. Écrits : {NOM_SERVIE}, sha256 {h_servie}, {len(servi.encode('utf-8'))} octets, {len(servi)} "
                  f"caractères, {len(servi.split())} mots au découpage de Python ; {NOM_DIFF}, sha256 {h_diff}.")
        cr.append("")
        cr.append(f"EN BREF : version servie v2 sha256 {h_servie} ; {len(paires)} remplacements : {len(garde)} de la garde "
                  f"({n_chemins} chemins internes portant {n_occ_chemins} occurrences, {n_accords} identifiants "
                  f"d'accord, suites abrégées comprises) et {len(supp)} supplémentaires nommés "
                  f"({' ; '.join(q[5] for q in supp)}) ; garde de motifs : aucun refus sur la version servie ni sur les "
                  f"invites du tour III.1, pour les {len(moteurs)} moteurs ({', '.join(n for n, *_ in moteurs)}).")
        texte_cr = "\n".join(cr) + "\n"
        ecrire(NOM_COMPTE_RENDU, texte_cr)
        print(texte_cr, end="")
        return 0
    except Echec as e:
        print("\n".join(cr), file=sys.stderr)
        print(f"ARRÊT (code 2) : {e} ; rien n'est écrit", file=sys.stderr)
        return 2
    except (OSError, UnicodeDecodeError) as e:
        print(f"ARRÊT (code 1) : {type(e).__name__} : {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(principal())
