#!/usr/bin/env python3
"""Version servie de la question v8 au collisionneur (« modes de sabotage ») : retrait, par programme, des seuls renvois
internes que la garde de motifs des moteurs refuse, selon une liste fermée de paires, puis vérifications. Sans réseau.

Écrit le 23 novembre 2026 par Claude Opus 5.5 (sous-agent), sur l'ordre de la mère, suite du devis du service
(GO-2026-11-23-03), après la réponse du lecteur du coffre : « c'est la mère qui produit la version servie, par
programme », et le défaut D-3 de la contre-lecture du devis v1 (contre-lecture-devis-v8-v1.md, 230c7b4e…). Pièce
d'instrument (classe B) : à contre-lire par un autre modèle ; le lecteur du coffre contrôle le différentiel.

Dans l'ordre ; tout écart arrête (code 2) avant toute écriture :
1. lit la v8 et vérifie son empreinte (EMPREINTE_V8), son encodage (UTF-8) et ses fins de ligne (LF seules) ;
2. prend le texte depuis le titre, comme la ligne 1 de la v8 le prescrit (« Le texte à servir commence au titre ; ce
   bloc n'en fait pas partie ») : la ligne 1 doit être ce bloc, la ligne 2 vide, la ligne 3 le titre ;
3. lit la liste fermée des paires (ancien, nouveau), vérifie son sceau (.sha256 compagnon) ; chaque ancien figure une
   seule fois dans le texte, à la ligne que la liste lui donne ; chaque nouveau est la mention constante MENTION ;
4. dérive, indépendamment de la liste, ce que la garde de motifs de chaque moteur refuse dans le texte (toutes les
   occurrences, par les motifs mêmes du moteur ; seules les catégories « chemin interne » et « identifiant d'accord »
   sont admises, et tous les moteurs doivent trouver les mêmes occurrences) :
   - un chemin interne devient le jeton entier entre accents graves qui le contient (un chemin peut porter plusieurs
     occurrences : le préfixe et le nom du dépôt) ;
   - un identifiant d'accord devient l'expression élargie ACCORD_ELARGI, qui prend aussi la suite abrégée d'une plage
     (« … et -136 », « … à -139 ») ;
   la liste doit être exactement ce qui est dérivé : ni plus, ni moins ;
5. applique la liste et vérifie :
   - la mention est absente de la v8 ; remettre les anciens à la place des mentions redonne la v8 depuis son titre, au
     caractère près ;
   - tout ancien tombe dans la zone permise (lignes ZONE de la v8) et porte un motif de la garde ;
   - hors de la zone, le texte est identique (empreinte du reste, de part et d'autre) ; même nombre de lignes, et seules
     diffèrent les lignes qui portaient un ancien, chacune redonnée par ses seules paires ;
   - mêmes titres, numéros (faits, rubriques, listes), étiquettes de sources et statuts ;
   - aucun reste dans le texte servi : RESTES (identifiants d'accord, de registre, suite abrégée d'une plage,
     chemins internes entre accents graves, nom du dépôt) ; ce que la garde ne refuse pas et que l'ordre de la mère
     laisse en place est seulement compté (GARDES_HORS_ORDRE) ;
   - la garde de chaque moteur ne trouve plus rien, ni sur le texte servi, ni sur l'invite du tour III.1 que chaque
     moteur construit avec lui (en faits et en question, composition du devis) ; elle trouve toujours les occurrences
     sur la v8 (témoin, R5) ;
   - le différentiel unifié ne retire que les deux lignes de tête et les lignes qui portaient un ancien, et n'ajoute que
     ces lignes, mention à la place de l'ancien ;
6. écrit, sans jamais écraser (R12) : la version servie, le différentiel unifié et le compte rendu, chacun avec son
   .sha256.

Usage :
  PYTHONPATH=src python3 produire_version_servie_v1.py --v8 QUESTION_V8.md --paires PAIRES.json --sortie DOSSIER \
      --temp DOSSIER_DE_TRAVAIL --moteur NOM CHEMIN EMPREINTE [--moteur NOM CHEMIN EMPREINTE ...]
Codes de sortie : 0 fini ; 1 usage ou fichier illisible ; 2 vérification en échec, rien n'est écrit.
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

VERSION = "produire-version-servie-v1"
EMPREINTE_V8 = "047eeddff0285f41938be0ade4927f6d5dacdfe98f348a05f61bf97aaf53e80a"
MENTION = "[renvoi interne retiré]"
NOM_V8 = "question-collisionneur-modes-sabotage-v8.md"
NOM_SERVIE = "question-collisionneur-modes-sabotage-v8-servie-v1.md"
NOM_DIFF = "diff-v8-vers-version-servie-v1.diff"
NOM_COMPTE_RENDU = "sortie-produire-version-servie-v1.txt"
REGLE_LIGNE_1 = "Le texte à servir commence au titre ; ce bloc n'en fait pas partie."
DEBUT_TITRE = "# Question au collisionneur"
CATEGORIES_ADMISES = ("chemin interne", "identifiant d'accord")
JETON_CHEMIN = re.compile(r"`[A-Za-z0-9_./-]+`")  # entier : un chemin entre accents graves, sans blanc
ACCORD_ELARGI = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d+(?:\s+(?:et|à)\s+-\d+)*")  # identifiant et suite abrégée
ZONE = {77, 78} | set(range(155, 180))  # lignes de la v8 : faits 16 et 17, table des sources (§ 7)
RESTES = (  # aucun ne doit rester dans le texte servi
    ("identifiant d'accord", re.compile(r"\bGO-")),
    ("identifiant de registre", re.compile(r"\bR-\d{3,5}\b")),
    ("suite abrégée d'un identifiant (élargi)", re.compile(r"(?<![\w.\-])-\d+")),
    ("suite abrégée d'un identifiant (contre-lecture, D-3)", re.compile(r"-13[5-9]\b")),
    ("chemin interne entre accents graves", re.compile(
        r"`(?:docs|src|prereg|registres|runs|scripts|diag|livrables|papiers|archives-reponses-modeles)/")),
    ("nom du dépôt", re.compile(r"controle-ia")),
)
GARDES_HORS_ORDRE = (  # non refusés par la garde, laissés en place sur l'ordre de la mère : comptés, pas retirés
    ("chemin des données du pilote (source 11)", re.compile(r"`donnees/[^`]*`")),
    ("commit du dépôt d'origine (§ 7)", re.compile(r"\b2cd13d45[0-9a-f]*")),
    ("identifiant public de l'article (dans quatre chemins retirés)", re.compile(r"2606\.08892")),
)
ESPECES_INVITE = ["opus", "argon", "astra", "carbon", "neon"]  # composition recommandée par le devis
TOUR_INVITE = "E3-T1"  # seul tour dont l'invite ne dépend d'aucune cellule


class Echec(Exception):
    """Vérification en échec : rien n'est écrit."""


def empreinte(octets):
    return hashlib.sha256(octets).hexdigest()


def numero_ligne(texte, position, decalage=0):
    return texte.count("\n", 0, position) + 1 + decalage


def charger_moteur(nom, chemin, attendue):
    """Charge un moteur du collisionneur après contrôle de son empreinte ; aucun appel réseau n'a lieu au chargement."""
    h = empreinte(Path(chemin).read_bytes())
    if h != attendue:
        raise Echec(f"moteur {nom} : empreinte {h} ≠ empreinte attendue {attendue}")
    spec = importlib.util.spec_from_file_location(f"moteur_{re.sub(r'[^A-Za-z0-9_]', '_', nom)}", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    for attribut in ("VERSION", "MOTIFS_INTERDITS", "motifs_trouves", "garder_motifs", "construire_prompt",
                     "fixer_composition", "ecrire_neuf", "id_cellule"):
        if not hasattr(m, attribut):
            raise Echec(f"moteur {nom} : « {attribut} » absent")
    return m, h


def occurrences(m, texte):
    """Toutes les occurrences des motifs du moteur (sa fonction motifs_trouves ne rend que la première par catégorie)."""
    return [(categorie, x.start(), x.end(), x.group(0))
            for categorie, motif in m.MOTIFS_INTERDITS for x in motif.finditer(texte)]


def deriver(base, occs):
    """Ce que la garde refuse, élargi au jeton entier : [(debut, fin, categorie, ancien, occurrences)], dans l'ordre."""
    jetons = {}
    for categorie, deb, fin, trouve in occs:
        if categorie not in CATEGORIES_ADMISES:
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
    """Construit, dans un dossier de travail, l'invite du tour III.1 de chaque lettre, avec le texte servi en faits et
    en question, comme le fera le service ; renvoie [(cellule, longueur, occurrences)]."""
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
    p.add_argument("--paires", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--temp", required=True)
    p.add_argument("--moteur", nargs=3, action="append", metavar=("NOM", "CHEMIN", "EMPREINTE"), required=True)
    a = p.parse_args(argv)
    cr = [f"Compte rendu de {VERSION} ; script {Path(__file__).name}, sha256 {empreinte(Path(__file__).read_bytes())} ; "
          f"{datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}.", ""]
    try:
        sortie, temp = Path(a.sortie), Path(a.temp)
        for nom in (NOM_SERVIE, NOM_DIFF, NOM_COMPTE_RENDU):
            for chemin in (sortie / nom, sortie / (nom + ".sha256")):
                if chemin.exists():
                    raise Echec(f"{chemin} existe déjà : rien n'est écrasé (R12)")
        temp.mkdir(parents=True, exist_ok=True)
        # 1. la v8
        octets = Path(a.v8).read_bytes()
        h_v8 = empreinte(octets)
        if h_v8 != EMPREINTE_V8:
            raise Echec(f"v8 : empreinte {h_v8} ≠ {EMPREINTE_V8}")
        texte_v8 = octets.decode("utf-8")
        if "\r" in texte_v8:
            raise Echec("v8 : fins de ligne autres que LF")
        cr.append(f"1. v8 : {Path(a.v8).name}, sha256 {h_v8} (attendue), {len(octets)} octets, "
                  f"{texte_v8.count(chr(10))} fins de ligne, UTF-8, LF seules : tenu.")
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
                  f"retirées (le bloc d'en-tête, puis une ligne vide) ; {len(base)} caractères, "
                  f"{len(base.split())} mots au découpage de Python ; mention absente de la v8 : tenu.")
        # 3. la liste fermée des paires
        octets_paires = Path(a.paires).read_bytes()
        h_paires = empreinte(octets_paires)
        sceau = Path(str(a.paires) + ".sha256").read_text(encoding="utf-8").split()
        if not sceau or sceau[0] != h_paires:
            raise Echec(f"liste des paires : empreinte {h_paires} ≠ son sceau")
        liste = json.loads(octets_paires.decode("utf-8"))
        if liste.get("source", {}).get("sha256") != EMPREINTE_V8 or liste.get("mention") != MENTION:
            raise Echec("liste des paires : source ou mention autres que celles du programme")
        paires = []
        for q in liste["paires"]:
            if q["nouveau"] != MENTION:
                raise Echec(f"paire {q['n']} : nouveau {q['nouveau']!r} ≠ mention constante")
            if base.count(q["ancien"]) != 1:
                raise Echec(f"paire {q['n']} : ancien {q['ancien']!r} présent {base.count(q['ancien'])} fois (une exigée)")
            deb = base.find(q["ancien"])
            if numero_ligne(base, deb, 2) != q["ligne_v8"]:
                raise Echec(f"paire {q['n']} : ancien à la ligne {numero_ligne(base, deb, 2)} de la v8, la liste dit "
                            f"{q['ligne_v8']}")
            paires.append((deb, deb + len(q["ancien"]), q["categorie"], q["ancien"], q["n"]))
        paires.sort()
        cr.append(f"3. Liste fermée des paires : {Path(a.paires).name}, sha256 {h_paires} (sceau tenu) ; "
                  f"{len(paires)} paires, chaque ancien une seule fois dans le texte, à la ligne dite : tenu.")
        # 4. dérivation indépendante par la garde de chaque moteur
        moteurs = []
        for nom, chemin, attendue in a.moteur:
            m, h = charger_moteur(nom, chemin, attendue)
            moteurs.append((nom, chemin, h, m))
        reference = occurrences(moteurs[0][3], base)
        if not reference:
            raise Echec("aucune occurrence sur la v8 : le témoin ne voit rien")
        cr.append("4. Garde de motifs sur la v8 depuis le titre (témoin, R5), par moteur :")
        for nom, chemin, h, m in moteurs:
            occ = occurrences(m, base)
            if occ != reference:
                raise Echec(f"moteur {nom} : occurrences différentes de celles du premier moteur")
            compte = {}
            for categorie, *_ in occ:
                compte[categorie] = compte.get(categorie, 0) + 1
            cr.append(f"   {nom} ({m.VERSION}, sha256 {h}) : {len(occ)} occurrences {compte}")
        derive = deriver(base, reference)
        if [(d[0], d[1], d[2], d[3]) for d in derive] != [(q[0], q[1], q[2], q[3]) for q in paires]:
            raise Echec("la liste des paires n'est pas exactement ce que la garde refuse, élargi au jeton entier")
        cr.append(f"   Dérivé de la garde, élargi au jeton entier : {len(derive)} jetons, identiques à la liste, dans "
                  f"le même ordre : tenu.")
        # 5. application et vérifications
        servi = base
        for deb, fin, *_ in reversed(paires):
            servi = servi[:deb] + MENTION + servi[fin:]
        cr.append(f"5. Remplacements par « {MENTION} » : {len(paires)}, couvrant {len(reference)} occurrences de la "
                  f"garde et les suites abrégées des plages :")
        for (deb, fin, categorie, ancien, n), d in zip(paires, derive):
            cr.append(f"   {n:2d}. ligne {numero_ligne(base, deb, 2)} de la v8 (ligne {numero_ligne(base, deb)} de la "
                      f"version servie), {categorie}, ancien {ancien!r}, occurrences de la garde couvertes {d[4]}")
        morceaux = servi.split(MENTION)
        if len(morceaux) != len(paires) + 1:
            raise Echec("nombre de mentions dans la version servie ≠ nombre de paires")
        reconstruit = morceaux[0] + "".join(q[3] + morceaux[i + 1] for i, q in enumerate(paires))
        if reconstruit != base:
            raise Echec("remettre les anciens ne redonne pas la v8 depuis son titre")
        cr.append("5a. Anciens remis à la place des mentions : la v8 depuis son titre est redonnée au caractère près : "
                  "tenu.")
        for deb, fin, categorie, ancien, n in paires:
            k = numero_ligne(base, deb, 2)
            if k not in ZONE:
                raise Echec(f"paire {n} : ligne {k} de la v8 hors de la zone permise")
            if not any(motif.search(ancien) for _, _, _, mm in moteurs for _, motif in mm.MOTIFS_INTERDITS):
                raise Echec(f"paire {n} : l'ancien {ancien!r} ne porte aucun motif de la garde")
        h_reste_base, h_reste_servi = (empreinte(reste_hors_zone(t).encode("utf-8")) for t in (base, servi))
        if h_reste_base != h_reste_servi:
            raise Echec("le texte change hors de la zone permise")
        cr.append(f"5b. Tout ancien dans la zone permise (lignes 77, 78 et 155 à 179 de la v8) et porteur d'un motif de "
                  f"la garde ; hors de la zone, texte identique (empreinte du reste, de part et d'autre : "
                  f"{h_reste_base}) : tenu.")
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
        cr.append("    Non refusés par la garde et laissés en place sur l'ordre de la mère (« seulement ce que la garde "
                  "refuse ») ; comptés, à trancher (devis v2, décision 1) :")
        for nom, motif in GARDES_HORS_ORDRE:
            cr.append(f"   {nom} : {len(motif.findall(base))} dans la v8 depuis le titre, {len(motif.findall(servi))} "
                      f"dans le texte servi")
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
        n_chemins = sum(1 for q in paires if q[2] == "chemin interne")
        n_occ_chemins = sum(1 for o in reference if o[0] == "chemin interne")
        n_accords = sum(1 for q in paires if q[2] == "identifiant d'accord")
        cr.append("")
        cr.append(f"6. Écrits : {NOM_SERVIE}, sha256 {h_servie}, {len(servi.encode('utf-8'))} octets, {len(servi)} "
                  f"caractères, {len(servi.split())} mots au découpage de Python ; {NOM_DIFF}, sha256 {h_diff}.")
        cr.append("")
        cr.append(f"EN BREF : version servie sha256 {h_servie} ; {len(paires)} remplacements ({n_chemins} chemins "
                  f"internes portant {n_occ_chemins} occurrences de la garde, {n_accords} identifiants d'accord, suites "
                  f"abrégées comprises) ; garde de motifs : aucun refus sur la version servie ni sur les invites du "
                  f"tour III.1, pour les {len(moteurs)} moteurs ({', '.join(n for n, *_ in moteurs)}).")
        texte_cr = "\n".join(cr) + "\n"
        ecrire(NOM_COMPTE_RENDU, texte_cr)
        print(texte_cr, end="")
        return 0
    except Echec as e:
        print("\n".join(cr), file=sys.stderr)
        print(f"ARRÊT (code 2) : {e} ; rien n'est écrit", file=sys.stderr)
        return 2
    except (OSError, ValueError, KeyError) as e:
        print(f"ARRÊT (code 1) : {type(e).__name__} : {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(principal())
