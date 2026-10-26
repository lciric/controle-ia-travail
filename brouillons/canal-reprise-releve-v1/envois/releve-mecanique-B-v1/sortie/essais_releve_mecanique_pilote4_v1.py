"""Essais (R5) du relevé mécanique (B) du pilote 4 — v1.

Écrits par un sous-agent neuf de la lignée conv-audit, le 2026-10-26T07:01:48Z (heure lue sur `date -u` dans la commande qui écrit ce
fichier). Pièces de simulation seulement (séries v13 et v14) ; aucune pièce d'une course réelle.

Usage : python3 -I -B essais_releve_mecanique_pilote4_v1.py [--journal FICHIER] [--interpretes P1,P2,…] [--garder]
(-B : aucun fichier de code compilé écrit nulle part ; le script du relevé est lancé de même, avec -I -B.)

Par défaut : le script, la table et leurs compagnons à côté de ce fichier ; les pièces fournies dans ../fournis et
../fournis-v2 ; les copies d'essai dans ../travail/essais-<pid>, effacées à la fin ; le journal
journal-essais-releve-B-v1.log à côté de ce fichier, en création exclusive, une heure lue sur `date -u` par ligne.

Ce que les essais ouvrent : dans les dossiers de course, seulement LANCEMENT.md, EMPREINTES-pilote-v1.txt,
A-POUSSER-v1.txt et leurs compagnons, extrait-mecanique-v1.json et journal-appels-*.jsonl ; tout autre fichier est
haché, ou lié en dur dans une copie de travail (aucune lecture), jamais lu. Aucune valeur de score n'est écrite : le
décimal planté sous un nom de score et le marqueur de réponse sont tirés au hasard à l'exécution et jamais consignés.
"""
import argparse
import hashlib
import json
import os
import random
import re
import runpy
import secrets
import shutil
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(ICI)
NOM_SCRIPT = "releve_mecanique_pilote4_v1.py"
NOM_TABLE = "table-correspondance-releve-B-v1.json"
EMPREINTE_SPEC_V2 = "701b527091c26aa657ef6b736dc340c3e6297cddd98acb1f35e0136176cfd043"
Q_M = "8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd"
Q_S = "a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289"
LISIBLE = re.compile(r"(LANCEMENT\.md|EMPREINTES-pilote-v1\.txt|A-POUSSER-v1\.txt)(\.sha256)?|extrait-mecanique-v1\.json"
                     r"|journal-appels-[a-z][0-9]{3}\.jsonl")
DECIMAL = re.compile(r"[0-9][.,][0-9]")
UNITES = ("c001", "g000", "g001", "g002", "g003")
CAS_V13 = {
    "v6-2": ("simulation-v6-2", "pilote4-gemini-v6-2-v1", "v6.2 continue"),
    "v6-2-segments": ("simulation-v6-2-segments", "pilote4-gemini-v6-2-v1", "v6.2 en deux segments"),
    "v6-2-trois-segments": ("simulation-v6-2-trois-segments", "pilote4-gemini-v6-2-v1", "v6.2 en trois segments"),
    "v5-3": ("simulation-v5-3", "pilote4-gemini-v5-3-v1", "v5.3 continue"),
}
CAS_V14 = {
    "v14-m": "cas-sain-v6-2/pilote4-gemini-v6-2-v1",
    "v14-s": "cas-sain-v6-2-s/pilote4-gemini-v6-2-s-v1",
    "v14-segments": "cas-seg-segment1/pilote4-gemini-v6-2-v1",
}

# Grammaire de la spécification v2 (§ 3 et § 4), écrite ici indépendamment de la table du script ; seule extension :
# la forme « graine » (écart déclaré) ; « absent » admis par la règle générale du § 3 là où la liste ne l'écrit pas (*).
ID = r"[a-z0-9][a-z0-9_-]{0,47}"
FORMES = {
    "entier": r"[0-9]{1,12}", "montant": r"[0-9]{1,6}\.[0-9]{1,4} USD", "duree": r"[0-9]{1,8}(\.[0-9]{1,3})? s",
    "taille": r"[0-9]{1,12} octets", "identifiant": ID, "oui_non": r"oui|non", "oui": r"oui", "m_s": r"m|s",
    "commit": r"[0-9a-f]{7,40}", "empreinte": r"[0-9a-f]{64}", "absent": r"absent", "graine": r"[0-9]{1,40}",
    "date_heure": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z",
}
CLES_SPEC = [
    ("releve.version", "entier"), ("releve.script_empreinte", "empreinte"), ("releve.heure", "date_heure"),
    ("releve.dossier", "identifiant"), ("releve.course", "identifiant"), ("sources.liste_fermee", "empreinte"),
    ("sources.liste_fermee_verifiee", "oui"), ("sources.extrait", "empreinte absent"),
    ("sources.journal_appels.<>", "empreinte"), ("sources.lancement", "empreinte absent"),
    ("sources.manifeste", "empreinte absent"), ("sources.champs_ignores", "entier"), ("identite.commit", "commit"),
    ("identite.arbre", "empreinte"), ("identite.nb_fichiers", "entier"), ("identite.graine", "graine"),
    ("identite.graine_manifeste", "graine absent"), ("identite.lanceur", "identifiant"),
    ("identite.lanceur_empreinte", "empreinte"), ("identite.noyau", "commit absent"),
    ("identite.banque_empreinte", "empreinte absent"), ("identite.texte_empreinte", "empreinte absent"),
    ("identite.question", "m_s"), ("identite.question_empreinte", "empreinte"), ("identite.lignee", "identifiant"),
    ("identite.porte_m_precedente", "oui absent"), ("segments.nombre", "entier"),
    ("segments.<>.fin", "identifiant absent"), ("segments.<>.heure_fin", "date_heure absent"),
    ("segments.<>.code", "entier absent"), ("fin.lignee", "identifiant absent"), ("fin.dernier_code", "entier absent"),
    ("fin.liste_fermee_poussee", "oui_non absent"), ("fin.recherche_cles_faite", "oui_non absent"),
    ("fin.reprise_attendue", "oui_non"), ("unite.<>.statut", "identifiant absent"), ("unite.<>.duree", "duree absent"),
    ("unite.<>.cout", "montant absent"), ("unite.<>.appels.total", "entier absent"),
    ("unite.<>.appels.statut.<>", "entier"), ("unite.<>.appels.role.<>", "entier"),
    ("unite.<>.recherches.<>", "entier"), ("unite.<>.telechargements.<>", "entier"),
    ("unite.<>.question_servie", "oui_non absent"), ("conception.rondes_tournees", "entier absent"),
    ("conception.declaration.ronde", "entier absent"), ("conception.declaration.motif", "identifiant absent"),
    ("conception.declaration.exemplaires", "entier absent"), ("mutation.<>.appels", "entier"),
    ("mutation.<>.successeur_produit", "oui_non absent"), ("mutation.<>.successeur_valide", "oui_non absent"),
    ("mutation.<>.successeur_a_tourne", "oui_non absent"), ("mutation.<>.refus.<>", "entier"),
    ("fichier.<>.politique_endogene", "empreinte absent"), ("memoire.<>.taille", "taille absent"),
    ("memoire.<>.restauration", "oui_non absent"), ("castes.<>.nombre", "entier absent"),
    ("castes.<>.mitose", "entier absent"), ("evenements.delai_depasse", "entier absent"),
    ("evenements.plafond_refus", "entier absent"), ("evenements.stop", "entier absent"),
    ("course.cout_total", "montant absent"), ("course.duree_totale", "duree absent"),
    ("course.recherches_total", "entier absent"), ("course.telechargements_total", "entier absent"),
]
CLES_REGEX = [(re.compile(r"\.".join(ID if p == "<>" else re.escape(p) for p in cle.split("."))), formes.split())
              for cle, formes in CLES_SPEC]

ENVELOPPE_AUDIT = r'''
import json, os, runpy, sys
journal, script = sys.argv[1], os.path.abspath(sys.argv[2])
sys.argv = [script] + sys.argv[3:]
ouvertures = []
def crochet(evenement, args):
    if evenement != "open" or not args or not isinstance(args[0], (str, bytes)):
        return
    chemin = os.path.abspath(os.fsdecode(args[0]))
    cadre, chaine = sys._getframe(1), []
    while cadre is not None:
        if cadre.f_code.co_filename == script:
            chaine.append(cadre.f_code.co_name)
        cadre = cadre.f_back
    ouvertures.append([chemin, chaine])
sys.addaudithook(crochet)
code = 0
try:
    runpy.run_path(script, run_name="__main__")
except SystemExit as e:
    code = e.code if isinstance(e.code, int) else 1
with open(journal, "x", encoding="utf-8") as f:
    json.dump(ouvertures, f)
sys.exit(code)
'''

ENVELOPPE_PANNE = r'''
import json, os, runpy, sys
script = os.path.abspath(sys.argv[1])
sys.argv = [script] + sys.argv[2:]
def panne(*_a, **_k):
    raise RuntimeError("panne")
json.loads = panne
runpy.run_path(script, run_name="__main__")
'''


# --- Outils ---

def sha(octets):
    return hashlib.sha256(octets).hexdigest()


def lecteur(chaine):
    """Fonction du script qui a demandé l'ouverture : la première de la chaîne d'appels hors de ouvrir_sans_lien."""
    return next((nom for nom in chaine if nom != "ouvrir_sans_lien"), None)


def sha_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def lire(chemin):
    """Lit un fichier que les essais ont le droit d'ouvrir (liste blanche, ou fichier qu'ils ont écrit)."""
    nom = os.path.basename(chemin)
    if "serie-v" in chemin and not LISIBLE.fullmatch(re.sub(r"-simulation-[a-z0-9-]+(?=\.)", "", nom)):
        raise AssertionError("lecture hors liste blanche")
    with open(chemin, "rb") as f:
        return f.read()


def ecrire(chemin, octets):
    """Création exclusive ; un fichier existant (copie ou lien en dur) est d'abord retiré, jamais modifié en place."""
    if os.path.lexists(chemin):
        os.unlink(chemin)
    with open(chemin, "xb") as f:
        f.write(octets)


def heure():
    return subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()


def releve_lignes(texte):
    return [tuple(l.split(" = ", 1)) for l in texte.splitlines()]


class Journal:
    def __init__(self, chemin):
        self.f = open(chemin, "x", encoding="utf-8")
        self.n = self.echecs = 0

    def ecrire(self, texte):
        self.f.write("{} | {}\n".format(heure(), texte))
        self.f.flush()

    def note(self, texte):
        self.f.write("# {}\n".format(texte))
        self.f.flush()

    def essai(self, nom, verifications, detail=""):
        self.n += 1
        rates = [libelle for libelle, ok in verifications if not ok]
        if rates:
            self.echecs += 1
            self.ecrire("ÉCHEC | {} | non vérifié : {}".format(nom, " ; ".join(rates)))
        else:
            self.ecrire("RÉUSSI | {} | {}".format(nom, detail or "conforme"))
        return not rates


# --- Dossiers de course : reconstitution v13, copies v14, liste fermée ---

def fabriquer_liste(dossier):
    noms = []
    for racine, _dossiers, fichiers in os.walk(dossier):
        for nom in fichiers:
            rel = os.path.relpath(os.path.join(racine, nom), dossier)
            if rel not in ("EMPREINTES-pilote-v1.txt", "EMPREINTES-pilote-v1.txt.sha256"):
                noms.append(rel)
    lignes = "".join("{}  {}\n".format(sha_fichier(os.path.join(dossier, n)), n) for n in sorted(noms))
    ecrire(os.path.join(dossier, "EMPREINTES-pilote-v1.txt"), lignes.encode("utf-8"))
    ecrire(os.path.join(dossier, "EMPREINTES-pilote-v1.txt.sha256"),
           "{}  EMPREINTES-pilote-v1.txt\n".format(sha(lignes.encode("utf-8"))).encode("utf-8"))


def empreintes_fournies(fournis):
    lignes = open(os.path.join(os.path.dirname(fournis), "EMPREINTES-fournis-v1.txt"), encoding="utf-8").read()
    return {l[66:]: l[:64] for l in lignes.splitlines()}


def reconstituer_v13(fournis, cas, parent):
    """Remet les pièces v13 d'un cas à leur nom réel (d'après A-POUSSER), fabrique compagnons et liste fermée."""
    suffixe, dossier, _nom = CAS_V13[cas]
    v13 = os.path.join(fournis, "serie-v13-simulation-lanceur-v10")
    attendues = empreintes_fournies(fournis)
    cible = os.path.join(parent, dossier)
    os.makedirs(cible)
    a_pousser = lire(os.path.join(v13, "A-POUSSER-v1-{}.txt".format(suffixe))).decode("utf-8").split("\n")
    noms = {"LANCEMENT.md": "LANCEMENT-{}.md", "A-POUSSER-v1.txt": "A-POUSSER-v1-{}.txt",
            "extrait-mecanique-v1.json": "extrait-mecanique-v1-{}.json"}
    noms.update({"journal-appels-{}.jsonl".format(u): "journal-appels-" + u + "-{}.jsonl" for u in UNITES})
    for reel, modele in noms.items():
        fourni = modele.format(suffixe)
        octets = lire(os.path.join(v13, fourni))
        if attendues.get("serie-v13-simulation-lanceur-v10/" + fourni) != sha(octets) or reel not in a_pousser:
            raise AssertionError("pièce v13 non conforme")
        ecrire(os.path.join(cible, reel), octets)
        ecrire(os.path.join(cible, reel + ".sha256"), "{}  {}\n".format(sha(octets), reel).encode("utf-8"))
    fabriquer_liste(cible)
    return cible


def copier_v14(source, cible):
    """Copie de travail : octets copiés pour les fichiers de la liste blanche, liens en dur pour tous les autres."""
    for racine, _dossiers, fichiers in os.walk(source):
        rel = os.path.relpath(racine, source)
        os.makedirs(os.path.join(cible, rel), exist_ok=True)
        for nom in fichiers:
            s, d = os.path.join(racine, nom), os.path.join(cible, rel, nom)
            if rel == "." and LISIBLE.fullmatch(nom):
                ecrire(d, lire(s))
            else:
                os.link(s, d)
    return cible


def modifier_texte(chemin, fonction):
    ecrire(chemin, fonction(lire(chemin).decode("utf-8")).encode("utf-8"))


def modifier_extrait(dossier, fonction):
    chemin = os.path.join(dossier, "extrait-mecanique-v1.json")
    objet = json.loads(lire(chemin).decode("utf-8"))
    fonction(objet)
    ecrire(chemin, json.dumps(objet, ensure_ascii=False, indent=1).encode("utf-8"))


def modifier_journal(dossier, unite, fonction):
    chemin = os.path.join(dossier, "journal-appels-{}.jsonl".format(unite))
    lignes = [json.loads(l) for l in lire(chemin).decode("utf-8").split("\n") if l.strip()]
    lignes = fonction(lignes)
    ecrire(chemin, "".join(json.dumps(l, ensure_ascii=False) + "\n" for l in lignes).encode("utf-8"))


# --- Exécution du script et contrôles ---

class Essais:
    def __init__(self, args):
        self.pieces = os.path.abspath(args.pieces)
        self.script = os.path.join(self.pieces, NOM_SCRIPT)
        self.fournis = os.path.abspath(args.fournis)
        self.fournis_v2 = os.path.abspath(args.fournis_v2)
        self.travail = os.path.join(os.path.abspath(args.travail), "essais-{}".format(os.getpid()))
        os.makedirs(self.travail)
        self.journal = Journal(args.journal)
        self.interpretes = args.interpretes.split(",")
        self.compteur = 0
        self.outils = os.path.join(self.travail, "outils")
        os.makedirs(self.outils)
        ecrire(os.path.join(self.outils, "audit_ouvertures.py"), ENVELOPPE_AUDIT.encode("utf-8"))
        ecrire(os.path.join(self.outils, "panne.py"), ENVELOPPE_PANNE.encode("utf-8"))

    def nouveau(self, nom):
        self.compteur += 1
        propre = re.sub(r"[^A-Za-z0-9_-]+", "-", nom)[:40].strip("-")
        chemin = os.path.join(self.travail, "{:04d}-{}".format(self.compteur, propre))
        os.makedirs(chemin)
        return chemin

    def executer(self, interprete, course, sortie, script=None, enveloppe=None, avant=(), env=None):
        commande = ([interprete, "-I", "-B"] + list(enveloppe or []) + [script or self.script] + list(avant)
                    + [course, sortie])
        r = subprocess.run(commande, capture_output=True, timeout=900, env=env)
        return r.returncode, r.stdout.decode("utf-8", "replace"), r.stderr.decode("utf-8", "replace")

    def releve_ecrit(self, resultat, sortie):
        """Contrôles d'un relevé écrit ; rend (vérifications, lignes du relevé)."""
        code, out, err = resultat
        m = re.fullmatch(r"relevé écrit : (releve-mecanique-[a-z0-9_-]+-v1\.txt) ([0-9a-f]{64})\n", out)
        v = [("code 0", code == 0), ("une ligne de sortie standard", m is not None), ("sortie d'erreur vide", err == ""),
             ("aucun décimal sur les sorties", not DECIMAL.search(out + err))]
        if m is None:
            return v, {}
        chemin = os.path.join(sortie, m.group(1))
        octets = lire(chemin) if os.path.exists(chemin) else b""
        compagnon = lire(chemin + ".sha256").decode("utf-8") if os.path.exists(chemin + ".sha256") else ""
        v.append(("empreinte du relevé", sha(octets) == m.group(2)))
        v.append(("compagnon", compagnon == "{}  {}\n".format(m.group(2), m.group(1))))
        lignes = releve_lignes(octets.decode("utf-8"))
        cles = [c for c, _v in lignes]
        v.append(("clés uniques", len(cles) == len(set(cles))))
        v.append(("grammaire de la spécification v2", all(grammaire(c, val) for c, val in lignes)))
        v.append(("aucun décimal sans unité", not any(re.fullmatch(r"[0-9]+[.,][0-9]+", val) for _c, val in lignes)))
        return v, dict(lignes)

    def refus(self, resultat, sortie, motif, code=3):
        c, out, err = resultat
        prefixe = {2: "USAGE", 3: "REFUS", 4: "ERREUR INTERNE"}[code]
        attendu = err == "{} : {}\n".format(prefixe, motif) if motif else err.startswith(prefixe + " : ")
        return [("code {}".format(code), c == code), ("motif « {} »".format(motif or prefixe), attendu),
                ("sortie standard vide", out == ""), ("aucun décimal sur les sorties", not DECIMAL.search(out + err)),
                ("aucun relevé écrit", not [n for n in os.listdir(sortie) if n.startswith("releve-")])]


def grammaire(cle, valeur):
    trouvees = [formes for regex, formes in CLES_REGEX if regex.fullmatch(cle)]
    return len(trouvees) == 1 and any(re.fullmatch(FORMES[f], valeur) for f in trouvees[0])


def lire_reference(chemin):
    noms = {"v6.2 continue": "v6-2", "v5.3 continue": "v5-3", "v6.2 en deux segments": "v6-2-segments",
            "v6.2 en trois segments": "v6-2-trois-segments"}
    cas, courant = {}, None
    for ligne in open(chemin, encoding="utf-8").read().splitlines():
        m = re.fullmatch(r"== (.+) \(.+\)", ligne)
        if m:
            courant = cas.setdefault(noms[m.group(1)], {})
            continue
        m = re.fullmatch(r"  journal-appels-([a-z][0-9]{3})\.jsonl : ([0-9]+) appels ; statuts \{(.*)\} ; "
                         r"appels de mutation ([0-9]+)", ligne)
        if m:
            statuts = {k.lower(): int(n) for k, n in re.findall(r"'([^']+)': ([0-9]+)", m.group(3))}
            courant[m.group(1)] = (int(m.group(2)), statuts, int(m.group(4)))
    return cas


def comptes_conformes(releve, reference):
    """Comptes par unité égaux à la référence, sans double compte (aucun statut ni total en plus)."""
    for u, (total, statuts, mutation) in reference.items():
        if releve.get("unite.{}.appels.total".format(u)) != str(total):
            return False
        if releve.get("mutation.{}.appels".format(u)) != str(mutation):
            return False
        lus = {c.rsplit(".", 1)[1]: int(v) for c, v in releve.items() if c.startswith("unite.{}.appels.statut.".format(u))}
        if lus != statuts:
            return False
    totaux = [c for c in releve if re.fullmatch(r"unite\.[a-z][0-9]{3}\.appels\.total", c) and releve[c] != "absent"]
    return len(totaux) == len(reference)


def sans_heure(texte):
    return "".join(l + "\n" for l in texte.splitlines() if not l.startswith("releve.heure = "))


# --- Le programme des essais ---

def preparation(e, j):
    j.note("Journal des essais du relevé mécanique (B) du pilote 4 — v1 (essais R5, pièces de simulation seulement)")
    j.note("Spécification v2 (701b5270…) ; brief v1 (a047c89f…) ; décisions de conv-audit sur releve.course et "
           "identite.lignee ; précisions CLB4-06 ; heures lues sur date -u à l'écriture de chaque ligne")
    j.note("Numérotation : P préparation ; S cas sains ; A artefacts (A01 à A10 : § 6 de la spécification ; A11 à A13 : "
           "§ 6 v2 ; A14 : v2 n° 14 ; A15 et A16 : brief n° 12 et 14 ; A17 et A18 : décisions de conv-audit ; A19 et "
           "suivants : gardes du script) ; X transverses")
    for nom in (NOM_SCRIPT, NOM_TABLE, os.path.basename(__file__)):
        j.note("pièce {} : sha256 {}".format(nom, sha_fichier(os.path.join(e.pieces, nom))))
    for p in e.interpretes:
        version = subprocess.run([p, "-I", "-B", "-c", "import sys; print(sys.version.split()[0])"], capture_output=True,
                                 text=True).stdout.strip()
        j.note("interpréteur {} : Python {}".format(p, version))
    controle = subprocess.run(["sha256sum", "-c", "--quiet", NOM_SCRIPT + ".sha256", NOM_TABLE + ".sha256"],
                              cwd=e.pieces, capture_output=True)
    table = sha_fichier(os.path.join(e.pieces, NOM_TABLE))
    inscrite = re.search(r'^EMPREINTE_TABLE = "([0-9a-f]{64})"$', open(e.script, encoding="utf-8").read(), re.M)
    j.essai("P1 pièces du script : compagnons conformes (sha256sum -c), empreinte de la table inscrite dans le script",
            [("sha256sum -c", controle.returncode == 0), ("empreinte inscrite", inscrite and inscrite.group(1) == table)])
    fournis = subprocess.run(["sha256sum", "-c", "--quiet", "../EMPREINTES-fournis-v1.txt"], cwd=e.fournis,
                             capture_output=True)
    spec = sha_fichier(os.path.join(e.fournis_v2, "specification-releve-mecanique-B-v2.md"))
    j.essai("P2 pièces fournies : EMPREINTES-fournis-v1.txt (195 lignes) et spécification v2",
            [("sha256sum -c", fournis.returncode == 0), ("spécification v2", spec == EMPREINTE_SPEC_V2)])


def cas_v13(e, j, reference):
    """Reconstitue les quatre cas v13 une fois ; rend leurs dossiers."""
    parent = e.nouveau("v13")
    dossiers = {cas: reconstituer_v13(e.fournis, cas, os.path.join(parent, cas)) for cas in CAS_V13}
    j.essai("P3 reconstitution des quatre cas v13 (fichiers remis à leur nom réel d'après A-POUSSER, octets contrôlés "
            "contre EMPREINTES-fournis-v1.txt, compagnons et liste fermée fabriqués ; ni archive, ni organisme, ni réponse)",
            [("quatre dossiers", len(dossiers) == 4), ("référence v13 lue (quatre cas)", set(reference) == set(CAS_V13))])
    return dossiers


def comptes_v53(e, j, v13, reference):
    """La v5.3 est refusée par la table close ; ses comptes sont essayés par les fonctions du script lui-même."""
    module = runpy.run_path(e.script, run_name="essai_comptes")
    table = module["charger_table"](os.path.join(e.pieces, NOM_TABLE))
    verifications = []
    for u, (total, statuts, mutation) in reference["v5-3"].items():
        octets = lire(os.path.join(v13["v5-3"], "journal-appels-{}.jsonl".format(u)))
        appels, _ignores = module["analyser_journal"](octets, u, "essai", table)
        par_statut = module["compter"](s for _r, s in appels)
        nb_mutation = sum(1 for r, _s in appels if r == table["role_mutation"])
        verifications.append((u, len(appels) == total and par_statut == statuts and nb_mutation == mutation))
    j.essai("S3b comptes de la v5.3 par les fonctions du script (analyser_journal, compter) = référence v13 "
            "(interpréteur des essais)", verifications, "c001 à g003 conformes")


def questions_des_cas(e, j, v13):
    trouve = {}
    for cas, dossier in list(v13.items()) + [(c, os.path.join(e.fournis, "serie-v14", r)) for c, r in CAS_V14.items()]:
        texte = lire(os.path.join(dossier, "LANCEMENT.md")).decode("utf-8")
        trouve[cas] = set(re.findall(r"^- organisme : .* ; question \([^)]+\) : sha256 ([0-9a-f]{64})$", texte, re.M))
    attendu = {c: {Q_M} for c in list(CAS_V13) + ["v14-m", "v14-segments"]}
    attendu["v14-s"] = {Q_S}
    j.essai("P4 empreintes de question des cas sains : celle de M (8b1c7511…) aux quatre cas v13 et aux cas v14 de forme "
            "M ; celle de S (a54da93e…) au cas v14 S",
            [(cas, trouve[cas] == attendu[cas]) for cas in attendu])


def lignes_identite_des_cas(e, j, v13):
    """Chaque ligne qui porte un champ d'identité exigé est-elle écrite en mode simulation, au segment 1 ?"""
    table = json.load(open(os.path.join(e.pieces, NOM_TABLE), encoding="utf-8"))
    motifs = {n: re.compile(table["lancement"]["lignes"][n])
              for n in ("course", "depot_segment_1", "lanceur", "preenregistrement", "organisme", "code")}
    for cas, dossier in list(v13.items()) + [(c, os.path.join(e.fournis, "serie-v14", r)) for c, r in CAS_V14.items()]:
        texte = lire(os.path.join(dossier, "LANCEMENT.md")).decode("utf-8")
        segment_1 = re.split(r"(?m)^## Segment ", texte)[0].splitlines()
        sections = len(re.findall(r"(?m)^## Segment ", texte)) + 1
        avec_prereg = sum(1 for s in re.split(r"(?m)^## Segment ", texte)
                          if any(motifs["preenregistrement"].fullmatch(l) for l in s.splitlines()))
        j.essai("P5 lignes d'identité écrites en mode simulation au segment 1, cas {} (motifs exacts de la table)".format(cas),
                [(n, sum(1 for l in segment_1 if m.fullmatch(l)) == 1) for n, m in motifs.items()],
                "course, dépôt (forme du segment 1), lanceur, préenregistrement, organisme et code : une ligne chacune ; "
                "préenregistrement présent dans {} section(s) sur {}".format(avec_prereg, sections))


def sains(e, j, interprete, v13, reference, releves):
    tag = os.path.basename(interprete)
    for cas in ("v6-2", "v6-2-segments", "v6-2-trois-segments"):
        textes = []
        for tour in (1, 2):
            sortie = e.nouveau("sain-{}-{}".format(cas, tour))
            v, rel = e.releve_ecrit(e.executer(interprete, v13[cas], sortie), sortie)
            nom = "releve-mecanique-{}-v1.txt".format(CAS_V13[cas][1])
            texte = lire(os.path.join(sortie, nom)).decode("utf-8") if os.path.exists(os.path.join(sortie, nom)) else ""
            textes.append(texte)
            if tour == 1:
                nb = {"v6-2": "1", "v6-2-segments": "2", "v6-2-trois-segments": "3"}[cas]
                v += [("comptes = référence v13, sans double compte", comptes_conformes(rel, reference[cas])),
                      ("identite.question = m", rel.get("identite.question") == "m"),
                      ("identite.porte_m_precedente = absent", rel.get("identite.porte_m_precedente") == "absent"),
                      ("unite.g001.question_servie = oui", rel.get("unite.g001.question_servie") == "oui"),
                      ("releve.course", rel.get("releve.course") == "pilote4-gemini-v6-2-v1"),
                      ("identite.lignee", rel.get("identite.lignee") == "gemini-organisme-v6-2"),
                      ("segments.nombre = " + nb, rel.get("segments.nombre") == nb),
                      ("segments repris puis fermeture", all(rel.get("segments.{}.fin".format(k)) == "stop_repris"
                                                             for k in range(1, int(nb)))
                       and rel.get("segments.{}.fin".format(nb)) == "fermeture"),
                      ("evenements.stop", rel.get("evenements.stop") == str(int(nb) - 1)),
                      ("fin.reprise_attendue = non", rel.get("fin.reprise_attendue") == "non"),
                      ("déclaration de fin de conception", rel.get("conception.declaration.ronde") == "1")]
                j.essai("S1 cas sain v13 {} ({})".format(CAS_V13[cas][2], tag), v,
                        "code 0 ; relevé conforme ; comptes c001 à g003 = référence ; segments {}".format(nb))
                releves[(cas, tag)] = texte
        j.essai("S2 deux exécutions identiques hors releve.heure, cas v13 {} ({})".format(CAS_V13[cas][2], tag),
                [("relevés identiques hors heure", textes[0] != "" and sans_heure(textes[0]) == sans_heure(textes[1]))])
    sortie = e.nouveau("sain-v5-3")
    r = e.executer(interprete, v13["v5-3"], sortie)
    j.essai("S3 cas v13 v5.3 continue : clé de course v5-3 hors de la table close (décision 1 de conv-audit) ({})".format(tag),
            e.refus(r, sortie, "releve.course"), "refus attendu, code 3, motif releve.course ; aucun relevé")
    for cas, rel_chemin in CAS_V14.items():
        course = os.path.join(e.fournis, "serie-v14", rel_chemin)
        textes = []
        for tour in (1, 2):
            sortie = e.nouveau("sain-{}-{}".format(cas, tour))
            v, rel = e.releve_ecrit(e.executer(interprete, course, sortie), sortie)
            nom = "releve-mecanique-{}-v1.txt".format(os.path.basename(course))
            textes.append(lire(os.path.join(sortie, nom)).decode("utf-8") if os.path.exists(os.path.join(sortie, nom)) else "")
            if tour == 1:
                if cas == "v14-s":
                    v += [("identite.question = s", rel.get("identite.question") == "s"),
                          ("unite.g001.question_servie = oui", rel.get("unite.g001.question_servie") == "oui"),
                          ("identite.porte_m_precedente = oui", rel.get("identite.porte_m_precedente") == "oui"),
                          ("releve.course", rel.get("releve.course") == "pilote4-gemini-v6-2-s-v1"),
                          ("identite.lignee", rel.get("identite.lignee") == "gemini-organisme-v6-2-s")]
                else:
                    v += [("identite.question = m", rel.get("identite.question") == "m"),
                          ("identite.porte_m_precedente = absent", rel.get("identite.porte_m_precedente") == "absent")]
                v.append(("comptes = ceux de la v6.2 de référence", comptes_conformes(rel, reference["v6-2"])))
                if cas == "v14-segments":
                    v += [("segments.nombre = 2 (essais refusés du segment 2 non comptés comme segments)",
                           rel.get("segments.nombre") == "2"),
                          ("segment 1 repris, segment 2 fermé", rel.get("segments.1.fin") == "stop_repris"
                           and rel.get("segments.2.fin") == "fermeture"),
                          ("fin.dernier_code = 0 (dernier essai)", rel.get("fin.dernier_code") == "0")]
                j.essai("S4 cas sain v14 {} tel quel ({})".format(cas, tag), v, "code 0 ; relevé conforme")
                releves[(cas, tag)] = textes[0]
        j.essai("S5 deux exécutions identiques hors releve.heure, cas v14 {} ({})".format(cas, tag),
                [("relevés identiques hors heure", textes[0] != "" and sans_heure(textes[0]) == sans_heure(textes[1]))])


def rien_de_m_dans_s(e, j, releves, tag):
    m_dossier = os.path.join(e.fournis, "serie-v14", CAS_V14["v14-m"])
    s_dossier = os.path.join(e.fournis, "serie-v14", CAS_V14["v14-s"])
    lancement_m = lire(os.path.join(m_dossier, "LANCEMENT.md")).decode("utf-8")
    lancement_s = lire(os.path.join(s_dossier, "LANCEMENT.md")).decode("utf-8")
    liste_m = lire(os.path.join(m_dossier, "EMPREINTES-pilote-v1.txt"))
    valeurs = {sha(liste_m), Q_M}
    valeurs |= {l.split("  ", 1)[0] for l in liste_m.decode("utf-8").splitlines()
                if re.search(r"^[0-9a-f]{64}  (LANCEMENT\.md|extrait-mecanique-v1\.json|journal-appels-[a-z0-9]+\.jsonl|"
                             r"reponse-question-g001\.md)$", l)}
    valeurs |= set(re.findall(r"graine ([0-9]{6,})", lancement_m))
    for ligne in lancement_s.splitlines():
        if ligne.startswith(("- course v6.2 précédente : ", "- course M de référence : ")):
            valeurs |= set(re.findall(r"[0-9a-f]{64}", ligne)) | set(re.findall(r"graine (?:de [^ ]+ )?([0-9]{6,})", ligne))
            valeurs |= set(re.findall(r"(/[^ ;]+)", ligne))
            valeurs |= {d + " USD" for d in re.findall(r"dépense du noyau ([0-9.]+) USD", ligne)}
    texte = releves[("v14-s", tag)]
    exacts = {"gemini-organisme-v6-2", "pilote4-gemini-v6-2-v1", "v6-2"}
    trouves = [v for v in valeurs if v in texte] + [v for _c, v in releve_lignes(texte) if v in exacts]
    j.essai("S6 rien de la course M dans le relevé de S ({} valeurs de M et de la référence du second pilote cherchées : "
            "liste fermée, LANCEMENT, extrait, journaux, réponse, graines, chemins, dépense, lignée, nom) ({})"
            .format(len(valeurs) + len(exacts), tag), [("aucune valeur de M trouvée", not trouves)])


def artefacts(e, j, interprete, v13, releves):
    tag = os.path.basename(interprete)
    base_m, base_seg = v13["v6-2"], v13["v6-2-segments"]
    v14_s = os.path.join(e.fournis, "serie-v14", CAS_V14["v14-s"])
    sain = dict(releve_lignes(releves[("v6-2", tag)]))
    hasard = random.SystemRandom()

    def copie(base, nom, dossier=None):
        cible = os.path.join(e.nouveau(nom), dossier or os.path.basename(base))
        if base.startswith(e.fournis):
            return copier_v14(base, cible)
        shutil.copytree(base, cible)
        return cible

    def lancer(course, nom, **k):
        sortie = e.nouveau("sortie-" + nom)
        return e.executer(interprete, course, sortie, **k), sortie

    def ecrit(nom, course, controles, detail=""):
        r, sortie = lancer(course, nom)
        v, rel = e.releve_ecrit(r, sortie)
        j.essai("{} ({})".format(nom, tag), v + [(l, f(rel)) for l, f in controles], detail)
        return rel, sortie

    def refuse(nom, course, motif, code=3, **k):
        r, sortie = lancer(course, nom, **k)
        j.essai("{} ({})".format(nom, tag), e.refus(r, sortie, motif, code),
                "code {} ; motif {}".format(code, motif) if motif else "code {}".format(code))
        return r

    # A01 : un texte libre (phrase avec espaces) sur un champ de la table.
    phrase = "le modèle a trouvé la réponse attendue"
    for nom, faire, motif in [
            ("A01a phrase dans l'extrait sur generations[].statut", lambda d: modifier_extrait(
                d, lambda o: o["generations"][3].__setitem__("statut", phrase)), "unite.g002.statut"),
            ("A01b phrase dans un journal sur role", lambda d: modifier_journal(
                d, "g001", lambda ls: [dict(ls[0], role=phrase)] + ls[1:]), "unite.g001.appels.role"),
            ("A01c phrase dans l'extrait sur rapport.lignees.<l>.fin", lambda d: modifier_extrait(
                d, lambda o: o["rapport"]["lignees"]["gemini-organisme-v6-2"].__setitem__("fin", phrase)),
             "fin.lignee")]:
        d = copie(base_m, nom[:3])
        faire(d)
        fabriquer_liste(d)
        r = refuse(nom, d, motif)
        j.essai("{} : la phrase absente de la sortie d'erreur ({})".format(nom[:4], tag), [("phrase absente", phrase not in r[2])])

    # A02 : un champ « score » planté avec un décimal dans l'extrait.
    valeur = round(hasard.uniform(0.1, 0.9), 4)
    d = copie(base_m, "A02")
    modifier_extrait(d, lambda o: o["generations"][2].__setitem__("score", valeur))
    fabriquer_liste(d)
    rel, sortie = ecrit("A02 champ score à décimal planté dans l'extrait", d, [
        ("champs_ignores augmenté de 1", lambda r: int(r.get("sources.champs_ignores", "0"))
         == int(sain["sources.champs_ignores"]) + 1)])
    texte = "".join(open(os.path.join(sortie, n), encoding="utf-8").read() for n in os.listdir(sortie))
    j.essai("A02 le décimal planté absent du relevé (valeur tirée au hasard, non consignée) ({})".format(tag),
            [("décimal absent", repr(valeur) not in texte and str(valeur) not in texte)])

    # A03 : décimal sans unité sur un champ de coût ; décimal sur un champ entier ; quatre décimales sur une durée.
    for nom, faire, motif in [
            ("A03a coût d'unité en texte décimal sans unité", lambda o: o["generations"][0].__setitem__(
                "cout_usd", str(o["generations"][0]["cout_usd"])), "unite.c001.cout"),
            ("A03b coût de la course en texte décimal sans unité", lambda o: o["rapport"].__setitem__(
                "depense_totale_usd", str(o["rapport"]["depense_totale_usd"])), "course.cout_total"),
            ("A03c décimal sur un champ entier (castes)", lambda o: o["generations"][1]["organisme"].__setitem__(
                "n_castes_recrutees", 1.5), "castes.g000.nombre"),
            ("A03d durée à quatre décimales (jamais arrondie)", lambda o: o["generations"][1]["execution"].__setitem__(
                "duree_s", 0.4719), "unite.g000.duree")]:
        d = copie(base_m, nom[:4])
        modifier_extrait(d, faire)
        fabriquer_liste(d)
        refuse(nom, d, motif)

    # A04 : une réponse plantée avec un marqueur ; instantané des ouvertures (crochet d'audit de Python).
    marqueur = "MARQUEUR-ESSAI-" + secrets.token_hex(12)
    for nom, listee in (("A04a réponse plantée et listée dans la liste fermée", True),
                        ("A04b réponse plantée hors de la liste fermée", False)):
        d = copie(base_m, nom[:4])
        ecrire(os.path.join(d, "reponse-question-g001.md"), ("# réponse\n" + marqueur + "\n").encode("utf-8"))
        if listee:
            fabriquer_liste(d)
        audit = os.path.join(e.nouveau("audit-" + nom[:4]), "ouvertures.json")
        r, sortie = lancer(d, nom, enveloppe=[os.path.join(e.outils, "audit_ouvertures.py"), audit])
        v, _rel = e.releve_ecrit(r, sortie)
        texte = "".join(open(os.path.join(sortie, n), encoding="utf-8").read() for n in os.listdir(sortie))
        ouvertures = json.load(open(audit, encoding="utf-8"))
        cible = os.path.join(d, "reponse-question-g001.md")
        par = {lecteur(f) for c, f in ouvertures if c == cible}
        v += [("marqueur absent du relevé et des sorties", marqueur not in texte + r[1] + r[2]),
              ("réponse jamais lue (ouverte seulement pour être hachée)" if listee else "réponse jamais ouverte",
               par == ({"empreinte_fichier"} if listee else set()))]
        j.essai("{} ({})".format(nom, tag), v, "ouvertures de la réponse : {}".format(
            "empreinte_fichier seulement" if listee else "aucune"))
    audit = os.path.join(e.nouveau("audit-v14-s"), "ouvertures.json")
    r, sortie = lancer(v14_s, "A04c audit v14 S", enveloppe=[os.path.join(e.outils, "audit_ouvertures.py"), audit])
    ouvertures = json.load(open(audit, encoding="utf-8"))
    dans = [(os.path.relpath(c, v14_s), lecteur(f)) for c, f in ouvertures if c.startswith(v14_s + os.sep)]
    lues = {c for c, f in dans if f != "empreinte_fichier"}
    autorisees = {c for c in lues if LISIBLE.fullmatch(c)}
    interdites = {c for c, _f in dans if c.startswith(("reponse-question", "question.md", "organisme/", "ferme.tar.gz"))}
    v, _rel = e.releve_ecrit(r, sortie)
    j.essai("A04c instantané des ouvertures sur le cas v14 S tel quel ({})".format(tag), v + [
        ("contenu lu seulement pour la liste blanche", lues == autorisees and bool(lues)),
        ("réponse, question, organisme et archive seulement hachés", bool(interdites) and all(
            f == "empreinte_fichier" for c, f in dans if c in interdites))],
        "{} fichiers lus (liste blanche), {} fichiers interdits hachés sans lecture".format(len(lues), len(interdites)))
    j.essai("A04d par construction : la chaîne « reponse-question » ne figure ni dans le script ni dans sa table ({})"
            .format(tag), [("absente du script", "reponse-question" not in open(e.script, encoding="utf-8").read()),
                           ("absente de la table", "reponse-question" not in open(
                               os.path.join(e.pieces, NOM_TABLE), encoding="utf-8").read())])

    # A05 : extrait retiré ; journaux retirés ; champs retirés de l'extrait (aucune estimation).
    d = copie(base_m, "A05a")
    os.unlink(os.path.join(d, "extrait-mecanique-v1.json"))
    os.unlink(os.path.join(d, "extrait-mecanique-v1.json.sha256"))
    fabriquer_liste(d)
    ecrit("A05a extrait retiré", d, [
        ("sources.extrait = absent", lambda r: r.get("sources.extrait") == "absent"),
        ("champs de l'extrait absents", lambda r: all(r.get(c) == "absent" for c in (
            "unite.g001.statut", "unite.g001.duree", "unite.g001.cout", "fin.lignee", "conception.declaration.ronde",
            "conception.declaration.motif", "castes.g001.nombre", "evenements.delai_depasse", "evenements.stop",
            "course.cout_total", "course.duree_totale", "course.recherches_total", "identite.graine_manifeste"))),
        ("aucune recherche recopiée", lambda r: not [c for c in r if ".recherches." in c]),
        ("lignée déduite de la clé de course", lambda r: r.get("identite.lignee") == "gemini-organisme-v6-2"),
        ("appels toujours lus des journaux", lambda r: r.get("unite.g001.appels.total") == sain["unite.g001.appels.total"])],
        "relevé écrit ; champs de l'extrait absent ; lignée déduite de la clé de course")
    d = copie(base_m, "A05b")
    for u in UNITES:
        os.unlink(os.path.join(d, "journal-appels-{}.jsonl".format(u)))
        os.unlink(os.path.join(d, "journal-appels-{}.jsonl.sha256".format(u)))
    fabriquer_liste(d)
    ecrit("A05b journaux retirés", d, [
        ("totaux d'appels absents", lambda r: all(r.get("unite.{}.appels.total".format(u)) == "absent" for u in UNITES)),
        ("aucun compte par statut, rôle ou mutation", lambda r: not [c for c in r if ".appels.statut." in c
                                                                     or ".appels.role." in c or c.endswith(".appels")
                                                                     and c.startswith("mutation.")]),
        ("rondes et plafond absents", lambda r: r.get("conception.rondes_tournees") == "absent"
         and r.get("evenements.plafond_refus") == "absent"),
        ("aucune source de journal", lambda r: not [c for c in r if c.startswith("sources.journal_appels.")])])
    d = copie(base_m, "A05c")
    modifier_extrait(d, lambda o: (o["generations"][3]["execution"].pop("duree_s"),
                                   o["rapport"].pop("depense_totale_usd")))
    fabriquer_liste(d)
    ecrit("A05c durée d'une unité et dépense de la course retirées de l'extrait", d, [
        ("unite.g002.duree = absent", lambda r: r.get("unite.g002.duree") == "absent"),
        ("course.duree_totale = absent (pas de somme partielle)", lambda r: r.get("course.duree_totale") == "absent"),
        ("course.cout_total = absent (jamais la somme des unités)", lambda r: r.get("course.cout_total") == "absent"),
        ("autres durées intactes", lambda r: r.get("unite.g001.duree") == sain["unite.g001.duree"])])

    # A06 : liste fermée falsifiée sous ses diverses formes.
    def liste(d):
        return lire(os.path.join(d, "EMPREINTES-pilote-v1.txt")).decode("utf-8")

    def poser_liste(d, texte, compagnon=True):
        ecrire(os.path.join(d, "EMPREINTES-pilote-v1.txt"), texte.encode("utf-8"))
        if compagnon:
            ecrire(os.path.join(d, "EMPREINTES-pilote-v1.txt.sha256"),
                   "{}  EMPREINTES-pilote-v1.txt\n".format(sha(texte.encode("utf-8"))).encode("utf-8"))

    def falsifier(texte):
        lignes = texte.splitlines()
        i = next(k for k, l in enumerate(lignes) if l.endswith("  LANCEMENT.md"))
        lignes[i] = ("0" if lignes[i][0] != "0" else "1") + lignes[i][1:]
        return "".join(l + "\n" for l in lignes)

    for nom, faire in [
            ("A06a ligne de LANCEMENT.md falsifiée (compagnon refait)", lambda d: poser_liste(d, falsifier(liste(d)))),
            ("A06b liste changée sans refaire son compagnon", lambda d: poser_liste(d, liste(d) + liste(d).splitlines(True)[0], False)),
            ("A06c ligne mal formée (un seul espace)", lambda d: poser_liste(d, liste(d).replace("  ", " ", 1))),
            ("A06d ligne en double", lambda d: poser_liste(d, liste(d) + liste(d).splitlines(True)[0])),
            ("A06e nom absolu", lambda d: poser_liste(d, liste(d) + "{}  /etc/hostname\n".format("0" * 64))),
            ("A06f nom remontant", lambda d: poser_liste(d, liste(d) + "{}  ../x\n".format("0" * 64))),
            ("A06g liste vide", lambda d: poser_liste(d, "")),
            ("A06h fichier listé absent du disque", lambda d: os.unlink(os.path.join(d, "A-POUSSER-v1.txt"))),
            ("A06i fichier listé altéré", lambda d: ecrire(os.path.join(d, "A-POUSSER-v1.txt"),
                                                            lire(os.path.join(d, "A-POUSSER-v1.txt")) + b"x\n")),
            ("A06j compagnon de la liste absent", lambda d: os.unlink(os.path.join(d, "EMPREINTES-pilote-v1.txt.sha256"))),
            ("A06k compagnon d'un journal altéré (fichier haché seulement)", lambda d: ecrire(
                os.path.join(d, "journal-appels-g001.jsonl.sha256"), b"0" * 64 + b"  journal-appels-g001.jsonl\n"))]:
        d = copie(base_m, nom[:4])
        faire(d)
        refuse(nom, d, "sources.liste_fermee_verifiee")
    d = copie(v14_s, "A06l")
    ecrire(os.path.join(d, "organisme", "principal.py"), b"# fichier remplace par l'essai A06l\n")
    refuse("A06l fichier de l'organisme remplacé dans une copie v14 S (haché, jamais lu)", d,
           "sources.liste_fermee_verifiee")

    # A07 : course arrêtée par STOP entre deux segments ; la garde G1 (figurée ici) refuse le relevé.
    d = copie(base_seg, "A07")
    modifier_texte(os.path.join(d, "LANCEMENT.md"), lambda t: t.split("\n## Segment 2, essai 1 ")[0] + "\n")
    ecrire(os.path.join(d, "LANCEMENT.md.sha256"), "{}  LANCEMENT.md\n".format(
        sha(lire(os.path.join(d, "LANCEMENT.md")))).encode("utf-8"))
    fabriquer_liste(d)
    rel, _s = ecrit("A07 course arrêtée par STOP entre deux segments (LANCEMENT.md coupé après le segment 1)", d, [
        ("fin.reprise_attendue = oui", lambda r: r.get("fin.reprise_attendue") == "oui"),
        ("segments.1.fin = stop_reprise_attendue", lambda r: r.get("segments.1.fin") == "stop_reprise_attendue")])
    j.essai("A07 garde G1 de l'assemblage, figurée par les essais (refus de tout relevé à fin.reprise_attendue = oui) "
            "({})".format(tag), [("G1 refuse", garde_g1(rel) == "refus"),
                                ("G1 accepte le cas sain", garde_g1(sain) == "accepte")])

    # A08 : un relevé déjà présent sous le même nom (R12).
    sortie = e.nouveau("A08")
    premier = e.executer(interprete, base_m, sortie)
    avant = {n: sha_fichier(os.path.join(sortie, n)) for n in os.listdir(sortie)}
    second = e.executer(interprete, base_m, sortie)
    apres = {n: sha_fichier(os.path.join(sortie, n)) for n in os.listdir(sortie)}
    j.essai("A08 relevé déjà présent sous le même nom ({})".format(tag), [
        ("premier écrit", premier[0] == 0), ("second refusé, code 3", second[0] == 3),
        ("motif releve.existant", second[2] == "REFUS : releve.existant\n"), ("rien réécrit", avant == apres)])

    # A09 : copie altérée du script (une ligne).
    copie_pieces = e.nouveau("A09")
    for n in (NOM_SCRIPT, NOM_SCRIPT + ".sha256", NOM_TABLE, NOM_TABLE + ".sha256"):
        shutil.copyfile(os.path.join(e.pieces, n), os.path.join(copie_pieces, n))
    modifier_texte(os.path.join(copie_pieces, NOM_SCRIPT), lambda t: t.replace('ABSENT = "absent"', 'ABSENT = "absente"', 1))
    controle = subprocess.run(["sha256sum", "-c", "--quiet", NOM_SCRIPT + ".sha256"], cwd=copie_pieces, capture_output=True)
    sortie = e.nouveau("sortie-A09")
    r = e.executer(interprete, base_m, sortie, script=os.path.join(copie_pieces, NOM_SCRIPT))
    j.essai("A09 copie altérée du script : sha256sum -c de son compagnon échoue avant toute exécution, et le script "
            "lui-même refuse ({})".format(tag), [("sha256sum -c échoue", controle.returncode != 0)]
            + e.refus(r, sortie, "releve.script_empreinte"))

    # A10 : liens symboliques.
    for nom, faire in [
            ("A10a lien symbolique non listé à la racine", lambda d: os.symlink("LANCEMENT.md", os.path.join(d, "lien"))),
            ("A10b fichier listé remplacé par un lien vers une copie identique", lambda d: (
                shutil.copyfile(os.path.join(d, "A-POUSSER-v1.txt"), os.path.join(d, "copie-a-pousser")),
                os.unlink(os.path.join(d, "A-POUSSER-v1.txt")),
                os.symlink("copie-a-pousser", os.path.join(d, "A-POUSSER-v1.txt")))),
            ("A10c lien symbolique dans un sous-dossier", lambda d: (
                os.makedirs(os.path.join(d, "segment-2-t1"), exist_ok=True),
                os.symlink("/etc/hostname", os.path.join(d, "segment-2-t1", "lien"))))]:
        d = copie(base_seg, nom[:4])
        faire(d)
        refuse(nom, d, "sources.liste_fermee_verifiee")

    # A11 à A13 (spécification v2) et artefacts d'identité du brief.
    def sans_lignes(prefixe):
        return lambda t: "".join(l for l in t.splitlines(True) if not l.startswith(prefixe))

    def lancement(base, nom, fonction):
        d = copie(base, nom)
        modifier_texte(os.path.join(d, "LANCEMENT.md"), fonction)
        ecrire(os.path.join(d, "LANCEMENT.md.sha256"), "{}  LANCEMENT.md\n".format(
            sha(lire(os.path.join(d, "LANCEMENT.md")))).encode("utf-8"))
        fabriquer_liste(d)
        return d

    autre = sha(b"une autre question")
    refuse("A11 lignes « - lanceur : … » retirées (spécification v2 n° 11 ; brief n° 13)",
           lancement(base_m, "A11", sans_lignes("- lanceur : ")), "identite.lanceur")
    refuse("A12 empreinte de la question remplacée (spécification v2 n° 12 ; brief n° 11)",
           lancement(base_m, "A12", lambda t: t.replace(Q_M, autre)), "identite.question")
    refuse("A13a ligne lanceur répétée au segment 2 avec une autre empreinte (spécification v2 n° 13)",
           lancement(base_seg, "A13a", lambda t: changer_dans_segment(t, "- lanceur : ", 2)),
           "identite.lanceur_empreinte")
    refuse("A13b ligne dépôt répétée au segment 2 avec un autre commit (spécification v2 n° 13)",
           lancement(base_seg, "A13b", lambda t: changer_dans_segment(t, "- dépôt : ", 2)), "identite.commit")
    refuse("A13c ligne organisme répétée au segment 2 avec un autre arbre (spécification v2 n° 13)",
           lancement(base_seg, "A13c", lambda t: changer_dans_segment(t, "- organisme : ", 2)), "identite.arbre")
    d = copie(v14_s, "A14")
    modifier_texte(os.path.join(d, "LANCEMENT.md"), lambda t: "".join(
        l for l in t.splitlines(True) if not (l.startswith("- course v6.2 précédente : ") and "lanceur attendu" in l)))
    fabriquer_liste(d)
    ecrit("A14 ligne « - course v6.2 précédente : … ; lanceur attendu … » retirée d'une course S (spécification v2 n° 14)",
          d, [("identite.porte_m_precedente = absent", lambda r: r.get("identite.porte_m_precedente") == "absent"),
              ("identite.question = s", lambda r: r.get("identite.question") == "s")], "relevé écrit, sans arrêt")
    refuse("A15 lignes « - organisme : … ; question … » retirées (brief n° 12)",
           lancement(base_m, "A15", sans_lignes("- organisme : ")), "identite.arbre")
    refuse("A15b lignes « - préenregistrement : … » retirées (graine exigée)",
           lancement(base_m, "A15b", sans_lignes("- préenregistrement : ")), "identite.graine")
    refuse("A15c lignes « - dépôt : … » retirées (commit du segment 1 exigé)",
           lancement(base_m, "A15c", sans_lignes("- dépôt : ")), "identite.commit")

    # A16 : décimal planté sous un nom de score dans un journal d'appels (brief n° 14).
    valeur = round(hasard.uniform(0.1, 0.9), 4)
    d = copie(base_m, "A16")
    modifier_journal(d, "g001", lambda ls: [dict(ls[0], score_interne=valeur)] + ls[1:])
    fabriquer_liste(d)
    rel, sortie = ecrit("A16 décimal planté sous un nom de score dans un journal d'appels (brief n° 14)", d, [
        ("champs_ignores augmenté de 1", lambda r: int(r.get("sources.champs_ignores", "0"))
         == int(sain["sources.champs_ignores"]) + 1),
        ("comptes inchangés", lambda r: r.get("unite.g001.appels.total") == sain["unite.g001.appels.total"])])
    texte = "".join(open(os.path.join(sortie, n), encoding="utf-8").read() for n in os.listdir(sortie))
    j.essai("A16 le décimal planté absent du relevé (valeur non consignée) ({})".format(tag),
            [("décimal absent", repr(valeur) not in texte)])

    # A17, A18 : décisions de conv-audit (table close du script).
    refuse("A17a chemin du pilote qui ne répond pas à la clé de course (v6-2 avec le dossier de S)",
           lancement(base_m, "A17a", lambda t: t.replace("/pilote4-gemini-v6-2-v1 (0700", "/pilote4-gemini-v6-2-s-v1 (0700")),
           "releve.course")
    d = os.path.join(e.nouveau("A17b"), "pilote4-gemini-v6-2-v1-tentative2")
    shutil.copytree(base_m, d)
    modifier_texte(os.path.join(d, "LANCEMENT.md"),
                   lambda t: t.replace("/pilote4-gemini-v6-2-v1 (0700", "/pilote4-gemini-v6-2-v1-tentative2 (0700"))
    ecrire(os.path.join(d, "LANCEMENT.md.sha256"), "{}  LANCEMENT.md\n".format(sha(lire(os.path.join(d, "LANCEMENT.md")))).encode("utf-8"))
    fabriquer_liste(d)
    r, sortie = lancer(d, "A17b")
    v, rel = e.releve_ecrit(r, sortie)
    j.essai("A17b suffixe -tentative2 au dossier et au chemin : nom de course sans le suffixe ({})".format(tag), v + [
        ("releve.course = pilote4-gemini-v6-2-v1", rel.get("releve.course") == "pilote4-gemini-v6-2-v1"),
        ("releve.dossier = pilote4-gemini-v6-2-v1-tentative2", rel.get("releve.dossier") == "pilote4-gemini-v6-2-v1-tentative2"),
        ("nom du relevé", os.path.exists(os.path.join(sortie, "releve-mecanique-pilote4-gemini-v6-2-v1-tentative2-v1.txt")))],
        "relevé releve-mecanique-pilote4-gemini-v6-2-v1-tentative2-v1.txt")
    d = copie(v14_s, "A18a")
    modifier_texte(os.path.join(d, "extrait-mecanique-v1.json"), lambda t: t.replace(
        "gemini-organisme-v6-2-s", "gemini-organisme-v6-2-x"))
    fabriquer_liste(d)
    refuse("A18a lignée de l'extrait différente de celle de la table close", d, "identite.lignee")
    d = copie(base_m, "A18b")
    modifier_extrait(d, lambda o: o["generations"][0].__setitem__("lignee", "gemini-organisme-autre"))
    fabriquer_liste(d)
    refuse("A18b deux lignées dans l'extrait", d, "identite.lignee")

    # A19 : dédoublonnage.
    d = copie(base_m, "A19a")
    modifier_journal(d, "c001", lambda ls: ls + [dict(l) for l in ls])
    fabriquer_liste(d)
    ecrit("A19a appels relus repris dans le journal (lignes en double, même identifiant) : comptés une fois", d, [
        ("comptes égaux au cas sain", lambda r: all(r.get(c) == sain[c] for c in sain
                                                    if c.startswith(("unite.c001.appels", "mutation.c001.")))),
        ("champs ignorés comptés pour chaque ligne lue", lambda r: int(r["sources.champs_ignores"])
         > int(sain["sources.champs_ignores"]))])
    d = copie(base_m, "A19b")
    modifier_journal(d, "c001", lambda ls: ls + [dict(ls[0], statut="ERREUR_API")])
    fabriquer_liste(d)
    refuse("A19b même identifiant d'appel, statut différent", d, "unite.c001.appels")

    # A20 : événements comptés quand ils existent (règles éprouvées sur des faits plantés).
    d = copie(base_m, "A20")
    modifier_journal(d, "g002", lambda ls: [dict(ls[0], statut="PLAFOND_ATTEINT")] + ls[1:])
    modifier_extrait(d, lambda o: (o["generations"][2]["execution"].__setitem__("delai_depasse", True),
                                   o["generations"][3].__setitem__("refus_noyau", ["successeur_trop_gros"]),
                                   o["generations"][4].__setitem__("problemes_successeur", ["fichier manquant"]),
                                   o["rapport"]["lignees"]["gemini-organisme-v6-2"].__setitem__("fin", "aucune lignée active")))
    fabriquer_liste(d)
    ecrit("A20 faits plantés : statut plafond, délai dépassé, refus du noyau, problème de successeur, autre fin de lignée", d, [
        ("evenements.plafond_refus = 1", lambda r: r.get("evenements.plafond_refus") == "1"),
        ("statut plafond compté à part", lambda r: r.get("unite.g002.appels.statut.plafond_atteint") == "1"
         and r.get("unite.g002.appels.statut.ok") == str(int(sain["unite.g002.appels.statut.ok"]) - 1)),
        ("evenements.delai_depasse = 1", lambda r: r.get("evenements.delai_depasse") == "1"),
        ("mutation.g002.refus.successeur_trop_gros = 1", lambda r: r.get("mutation.g002.refus.successeur_trop_gros") == "1"),
        ("mutation.g003.successeur_valide = non", lambda r: r.get("mutation.g003.successeur_valide") == "non"),
        ("fin.lignee = aucune_lignee_active", lambda r: r.get("fin.lignee") == "aucune_lignee_active")])
    d = copie(base_m, "A20b")
    modifier_extrait(d, lambda o: o["generations"][3].__setitem__("refus_noyau", [{"motif": "x"}]))
    fabriquer_liste(d)
    refuse("A20b refus du noyau sous une forme non simple (rien perdu en silence)", d, "mutation.g002.refus")

    # A21 à A24 : table, usage, erreur interne.
    copie_pieces = e.nouveau("A21")
    for n in (NOM_SCRIPT, NOM_SCRIPT + ".sha256", NOM_TABLE):
        shutil.copyfile(os.path.join(e.pieces, n), os.path.join(copie_pieces, n))
    ecrire(os.path.join(copie_pieces, NOM_TABLE), lire(os.path.join(copie_pieces, NOM_TABLE)) + b" ")
    refuse("A21 table de correspondance d'une autre empreinte", base_m, "table",
           script=os.path.join(copie_pieces, NOM_SCRIPT))
    sortie_dedans = os.path.join(e.nouveau("A22"), "course")
    shutil.copytree(base_m, sortie_dedans)
    os.makedirs(os.path.join(sortie_dedans, "sortie"))
    r = e.executer(interprete, sortie_dedans, os.path.join(sortie_dedans, "sortie"))
    j.essai("A22 dossier de sortie dans le dossier de course ({})".format(tag), [
        ("code 2", r[0] == 2), ("message d'usage", r[2] == "USAGE : dossier de sortie dans le dossier de course\n"),
        ("rien écrit", os.listdir(os.path.join(sortie_dedans, "sortie")) == [])])
    r = subprocess.run([interprete, "-I", "-B", e.script], capture_output=True, text=True)
    r2 = e.executer(interprete, os.path.join(e.travail, "inexistant"), e.nouveau("A23"))
    j.essai("A23 usage : arguments manquants ; dossier de course inexistant ({})".format(tag), [
        ("code 2 sans argument", r.returncode == 2 and r.stderr.startswith("USAGE : ")),
        ("code 2 dossier inexistant", r2[0] == 2 and r2[2] == "USAGE : dossier de course introuvable\n")])
    sortie = e.nouveau("A24")
    r = subprocess.run([interprete, "-I", "-B", os.path.join(e.outils, "panne.py"), e.script, base_m, sortie],
                       capture_output=True, text=True)
    j.essai("A24 erreur interne provoquée (json.loads en panne) : code 4, type et ligne seulement ({})".format(tag), [
        ("code 4", r.returncode == 4), ("type et ligne seulement", re.fullmatch(
            r"ERREUR INTERNE : RuntimeError ligne [0-9]+\n", r.stderr) is not None), ("aucun relevé", os.listdir(sortie) == [])])

    # A25 à A31 : autres gardes.
    d = lancement(base_m, "A25", lambda t: re.sub(r"^- réponse à la question : .*$", "- réponse à la question : aucune "
                                                  "pièce archivée (voir l'extrait : champ question_ouverte de g001, ou g001 "
                                                  "non tournée)", t, flags=re.M))
    ecrit("A25 « aucune pièce archivée » à la place de la réponse", d, [
        ("unite.g001.question_servie = absent (jamais non)", lambda r: r.get("unite.g001.question_servie") == "absent")])
    d = lancement(base_m, "A25b", lambda t: re.sub(r"^- réponse à la question : .*$", "- réponse à la question : "
                                                   "piece-g001.md, sha256 " + "0" * 64, t, flags=re.M))
    ecrit("A25b ligne de réponse reconnue par son seul début, quel que soit le nom de la pièce", d, [
        ("unite.g001.question_servie = oui", lambda r: r.get("unite.g001.question_servie") == "oui")])
    d = lancement(base_m, "A25c", lambda t: re.sub(r"^- réponse à la question : .*\n", "", t, flags=re.M))
    ecrit("A25c aucune ligne « - réponse à la question : »", d, [
        ("unite.g001.question_servie = absent", lambda r: r.get("unite.g001.question_servie") == "absent")])
    for nom, faire, motif in [
            ("A26 extrait_version inconnue", lambda o: o.__setitem__("extrait_version", 3), "sources.extrait"),
            ("A27 unité importée d'une autre course", lambda o: o["generations"][1].__setitem__("importee", True),
             "unite.importee"),
            ("A28 identifiant d'unité hors forme", lambda o: o["generations"][1].__setitem__(
                "chemin", "gemini-organisme-v6-2/G-000"), "unite")]:
        d = copie(base_m, nom[:3])
        modifier_extrait(d, faire)
        fabriquer_liste(d)
        refuse(nom, d, motif)
    d = copie(base_m, "A29")
    modifier_texte(os.path.join(d, "extrait-mecanique-v1.json"), lambda t: t.replace(
        '"extrait_version": 2', '"extrait_version": 2, "extrait_version": 2', 1))
    fabriquer_liste(d)
    refuse("A29 clé en double dans l'extrait", d, "sources.extrait")
    d = copie(base_m, "A30")
    modifier_texte(os.path.join(d, "extrait-mecanique-v1.json"), lambda t: t.replace(
        '"extrait_version": 2', '"extrait_version": 2, "nan": NaN', 1))
    fabriquer_liste(d)
    refuse("A30 NaN dans l'extrait", d, "sources.extrait")
    d = copie(base_m, "A31a")
    liste_avant = liste(d)
    ecrire(os.path.join(d, "extrait-mecanique-v2.json"), b"{}")
    refuse("A31a extrait présent sur le disque mais hors de la liste fermée", d, "sources.extrait")
    poser_liste(d, liste_avant + "{}  extrait-mecanique-v2.json\n".format(sha(b"{}")))
    refuse("A31b nom d'extrait inconnu dans la liste fermée", d, "sources.extrait")

    # A33 : clé de données de la liste noire sous un motif à joker de la liste blanche.
    d = copie(base_m, "A33")
    modifier_extrait(d, lambda o: o["generations"][2]["services"]["recherches"].__setitem__("taux_reussite", {"OK": 1}))
    fabriquer_liste(d)
    ecrit("A33 source de recherche nommée par un mot de la liste noire (taux_reussite) sous services.recherches.*", d, [
        ("non recopiée", lambda r: not [c for c in r if "taux" in c]),
        ("champs_ignores augmenté de 1", lambda r: int(r.get("sources.champs_ignores", "0"))
         == int(sain["sources.champs_ignores"]) + 1),
        ("autres recherches intactes", lambda r: all(r.get(c) == sain[c] for c in sain if ".recherches." in c))])

    # A32 : langue du système C (la ligne de sortie reste en UTF-8, le relevé est le même).
    sortie = e.nouveau("A32")
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LC_ALL": "C", "LANG": "C"}
    v, rel = e.releve_ecrit(e.executer(interprete, base_m, sortie, env=env), sortie)
    j.essai("A32 langue du système C (LC_ALL=C) ({})".format(tag), v + [
        ("relevé identique au cas sain hors heure", sans_heure("".join("{} = {}\n".format(c, x) for c, x in rel.items()))
         == sans_heure(releves[("v6-2", tag)]))])


def changer_dans_segment(texte, prefixe, segment):
    """Change le dernier chiffre hexadécimal de la valeur d'une ligne d'identité dans la dernière section du segment."""
    sections = re.split(r"(?m)^(?=## Segment )", texte)
    for i in range(len(sections) - 1, -1, -1):
        if sections[i].startswith("## Segment {},".format(segment)):
            lignes = sections[i].splitlines(True)
            for k, l in enumerate(lignes):
                if l.startswith(prefixe):
                    m = list(re.finditer(r"[0-9a-f]{40,64}", l))[0]
                    fin = m.end() - 1
                    lignes[k] = l[:fin] + ("0" if l[fin] != "0" else "1") + l[fin + 1:]
                    break
            sections[i] = "".join(lignes)
            break
    return "".join(sections)


def garde_g1(releve):
    return "refus" if releve.get("fin.reprise_attendue") != "non" else "accepte"


def principal():
    p = argparse.ArgumentParser()
    p.add_argument("--pieces", default=ICI)
    p.add_argument("--fournis", default=os.path.join(BASE, "fournis"))
    p.add_argument("--fournis-v2", default=os.path.join(BASE, "fournis-v2"))
    p.add_argument("--travail", default=os.path.join(BASE, "travail"))
    p.add_argument("--journal", default=os.path.join(ICI, "journal-essais-releve-B-v1.log"))
    p.add_argument("--interpretes", default="/usr/bin/python3.11,/usr/bin/python3.12,/usr/bin/python3.13")
    p.add_argument("--garder", action="store_true")
    args = p.parse_args()
    e = Essais(args)
    j = e.journal
    try:
        preparation(e, j)
        reference = lire_reference(os.path.join(e.fournis, "releve-serie-v13-v1.txt"))
        v13 = cas_v13(e, j, reference)
        questions_des_cas(e, j, v13)
        lignes_identite_des_cas(e, j, v13)
        comptes_v53(e, j, v13, reference)
        releves = {}
        for interprete in e.interpretes:
            sains(e, j, interprete, v13, reference, releves)
            rien_de_m_dans_s(e, j, releves, os.path.basename(interprete))
            artefacts(e, j, interprete, v13, releves)
        transverses = [sans_heure(releves[(c, os.path.basename(i))]) for c in ("v6-2", "v14-s")
                       for i in e.interpretes]
        j.essai("X1 relevés identiques hors releve.heure d'un interpréteur à l'autre (v13 v6.2 et v14 S)", [
            ("v13 v6.2", len(set(transverses[:len(e.interpretes)])) == 1),
            ("v14 S", len(set(transverses[len(e.interpretes):])) == 1)])
        fin = subprocess.run(["sha256sum", "-c", "--quiet", "../EMPREINTES-fournis-v1.txt"], cwd=e.fournis,
                             capture_output=True)
        j.essai("X2 pièces fournies intactes après les essais (sha256sum -c)", [("sha256sum -c", fin.returncode == 0)])
    except Exception as exc:
        j.ecrire("ÉCHEC | interruption des essais : {}".format(type(exc).__name__))
        j.echecs += 1
        raise
    finally:
        if not args.garder:
            shutil.rmtree(e.travail)
        j.ecrire("BILAN | {} essais, {} réussis, {} en échec ; copies de travail {}".format(
            j.n, j.n - j.echecs, j.echecs, "gardées" if args.garder else "effacées"))
        j.f.close()
    print("essais : {} ; réussis : {} ; échecs : {}".format(j.n, j.n - j.echecs, j.echecs))
    return 0 if j.echecs == 0 else 1


if __name__ == "__main__":
    sys.exit(principal())
