#!/usr/bin/env python3
"""Essais (R5) des gardes de la boucle extérieure du pilote 4 et du script d'assemblage — v1.

Chaque garde est essayée sur ses cas sains et sur ses artefacts (protocole de la boucle extérieure v4, § 11), sous
Python 3.11, 3.12 et 3.13, chaque script lancé avec `-I`. Tout essai est consigné dans le journal (une ligne par essai
et par interpréteur, heure lue sur `date -u`), échecs compris ; un essai non conforme fait finir le banc en erreur.
Données : synthétiques, construites ici à l'exécution dans un dossier neuf de `travail/` ; pièces de simulation
fournies (objet v6.2.1, carte et zones v1, course simulée saine de la série v14 : seuls `EMPREINTES-pilote-v1.txt` et
son compagnon y sont ouverts, les autres fichiers sont hachés). Le script ne contient ni texte de l'objet, ni valeur de
marqueur, ni contenu interdit : les changements de l'objet se font par position (fichier, ligne, colonne), les marqueurs
et les mots inventés de l'artefact (e) de G5 sont tirés à l'exécution, écrits dans `travail/` seulement, jamais dans le
journal (qui dit « contenu interdit planté : refusé »), puis effacés avec le dossier de travail.

Usage : python3 -I essais_gardes_v1.py --journal <journal-essais-gardes-v1.log> [--racine <dossier>] [--garder-travail]
"""

import argparse
import ast
import hashlib
import json
import os
import pathlib
import random
import re
import shutil
import subprocess
import sys
from decimal import Decimal, ROUND_HALF_UP

ICI = pathlib.Path(__file__).resolve().parent
SCRIPTS = {
    "assemblage": "assembler_dossier_lecture_v1.py",
    "G4": "garde_g4_arbre_organisme_v1.py",
    "G5": "garde_g5_perimetre_v1.py",
    "G6": "garde_g6_courses_v1.py",
    "G8": "garde_g8_valeurs_v1.py",
    "G9": "garde_g9_entree_lancement_v1.py",
}
ARBRE_OBJET = "4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d"
DOSSIER_S, COURSE_S, LIGNEE_S, CLE_S = "pilote4-gemini-v6-2-s-v1", "pilote4-gemini-v6-2-s-v1", \
    "gemini-organisme-v6-2-s", "v6-2-s"
DOSSIER_M, COURSE_M, LIGNEE_M, CLE_M = "pilote4-gemini-v6-2-v1-tentative2", "pilote4-gemini-v6-2-v1", \
    "gemini-organisme-v6-2", "v6-2"
GRAINE_ESSAIS = 20261026
ENV = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8"}


def heure():
    return subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], check=True, capture_output=True,
                          text=True).stdout.strip()


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sha_texte(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def ecrire(p, texte, mode="x"):
    p = pathlib.Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, mode, encoding="utf-8") as f:
        f.write(texte)
    return p


def compagnon(p):
    p = pathlib.Path(p)
    ecrire(p.with_name(p.name + ".sha256"), f"{sha(p)}  {p.name}\n")
    return p


def avec_compagnon(p, texte):
    return compagnon(ecrire(p, texte))


def empreinte_arbre(dossier: pathlib.Path) -> str:
    h = hashlib.sha256()
    for f in sorted(p for p in pathlib.Path(dossier).rglob("*")
                    if p.is_file() and p.suffix != ".pyc" and "__pycache__" not in p.relative_to(dossier).parts):
        h.update(str(f.relative_to(dossier)).encode("utf-8") + b"\0")
        h.update(hashlib.sha256(f.read_bytes()).hexdigest().encode("ascii") + b"\n")
    return h.hexdigest()


# ---------------------------------------------------------------------------------------------------------------------
# Banc


class Banc:
    def __init__(self, journal, interpretes, travail):
        self.journal = journal
        self.interpretes = interpretes
        self.travail = travail
        self.nb = 0
        self.non_conformes = []

    def ecrire(self, texte):
        self.journal.write(f"{heure()}  {texte}\n")
        self.journal.flush()

    def cas(self, garde, ident, genre, script, args, code_attendu, motif=None, verif=None, discret=False):
        """Lance le script sous chaque interpréteur. args : liste, ou fonction de l'étiquette (py311…) ; verif :
        fonction (étiquette, code, sortie, erreur) qui rend None ou l'écart constaté."""
        for nom, chemin, version in self.interpretes:
            tag = nom.replace("python", "py").replace(".", "")
            a = args(tag) if callable(args) else args
            r = subprocess.run([chemin, "-I", str(ICI / SCRIPTS[script])] + [str(x) for x in a], cwd=self.travail,
                               capture_output=True, encoding="utf-8", errors="replace", env=ENV, timeout=900)
            ecarts = []
            if r.returncode != code_attendu:
                ecarts.append(f"code {r.returncode} au lieu de {code_attendu}")
            if motif and not re.search(motif, r.stderr + r.stdout):
                ecarts.append("motif attendu absent de la sortie")
            if verif is not None:
                e = verif(tag, r.returncode, r.stdout, r.stderr)
                if e:
                    ecarts.append(e)
            self.nb += 1
            if discret:
                extrait = "contenu interdit planté : refusé" if not ecarts else "contenu interdit planté : NON refusé"
            else:
                sortie = (r.stderr if r.returncode else r.stdout).strip().split("\n")[0]
                extrait = sortie[:240]
            etat = "conforme" if not ecarts else "NON CONFORME"
            if ecarts:
                self.non_conformes.append(f"{garde} {ident} python {version}")
            details = f" | écart : {'; '.join(ecarts)}" if ecarts else ""
            self.ecrire(f"{etat} | {garde} | {ident} | {genre} | python {version} | code {r.returncode} (attendu "
                        f"{code_attendu}){details} | {extrait}")


# ---------------------------------------------------------------------------------------------------------------------
# Changements de l'objet, par position


def lignes_de(p):
    t = pathlib.Path(p).read_text(encoding="utf-8")
    fin = t.endswith("\n")
    lignes = t.split("\n")
    return (lignes[:-1] if fin else lignes), fin


def ecrire_lignes(p, lignes, fin):
    p = pathlib.Path(p)
    os.chmod(p, 0o644)
    p.write_text("\n".join(lignes) + ("\n" if fin else ""), encoding="utf-8")


def autre_caractere(c):
    if c.isdigit():
        return str((int(c) + 1) % 10)
    if c.isalpha():
        return "y" if c.lower() == "x" else ("X" if c.isupper() else "x")
    raise ValueError("caractère non alphanumérique")


def changer_colonne(copie, fichier, n, col):
    p = copie / fichier
    lignes, fin = lignes_de(p)
    l = lignes[n - 1]
    lignes[n - 1] = l[:col - 1] + autre_caractere(l[col - 1]) + l[col:]
    ecrire_lignes(p, lignes, fin)


def colonne_dans(copie, fichier, n, c1, c2):
    l = lignes_de(copie / fichier)[0][n - 1]
    chiffres = [c for c in range(c1, c2 + 1) if l[c - 1].isdigit()]
    lettres = [c for c in range(c1, c2 + 1) if l[c - 1].isalnum()]
    return (chiffres or lettres)[-1]


def colonne_hors(copie, fichier, n, segments):
    l = lignes_de(copie / fichier)[0][n - 1]
    for c in range(1, len(l) + 1):
        if l[c - 1].isalnum() and all(c < c1 - 1 or c > c2 + 1 for c1, c2 in segments):
            return c
    raise ValueError("aucune colonne hors des segments")


def inserer_apres(copie, fichier, n, nouvelles, retrait_de=None):
    p = copie / fichier
    lignes, fin = lignes_de(p)
    ref = lignes[(retrait_de or n + 1) - 1]
    retrait = ref[:len(ref) - len(ref.lstrip())]
    lignes[n:n] = [retrait + x for x in nouvelles]
    ecrire_lignes(p, lignes, fin)


def changer_ligne(copie, fichier, n, transformation):
    p = copie / fichier
    lignes, fin = lignes_de(p)
    lignes[n - 1] = transformation(lignes[n - 1])
    ecrire_lignes(p, lignes, fin)


def retirer_ligne(copie, fichier, n):
    p = copie / fichier
    lignes, fin = lignes_de(p)
    del lignes[n - 1]
    ecrire_lignes(p, lignes, fin)


def changer_version(copie):
    changer_ligne(copie, "principal.py", ligne_version(copie),
                  lambda l: re.sub(r'^(VERSION\s*=\s*")([^"]*)(")', lambda m: m.group(1) + m.group(2) + "-essai"
                                   + m.group(3), l))


def ligne_version(dossier):
    for n, l in enumerate(lignes_de(dossier / "principal.py")[0], 1):
        if re.fullmatch(r'VERSION\s*=\s*"[^"\\]*"\s*', l):
            return n
    raise ValueError("ligne VERSION introuvable")


def changer_manifeste(copie, cle="version"):
    def transformer(lignes):
        for i, l in enumerate(lignes):
            if cle == "version":
                m = re.match(r'^(\s*"version":\s*")([^"]*)(".*)$', l)
                if m:
                    lignes[i] = m.group(1) + m.group(2) + "-essai" + m.group(3)
            elif cle == "description":
                m = re.match(r'^(\s*"description":\s*")((?:[^"\\]|\\.)*)(".*)$', l)
                if m:
                    lignes[i] = m.group(1) + "version d'essai synthétique des gardes (aucune correction réelle)" \
                        + m.group(3)
            else:
                m = re.match(rf'^(\s*"{cle}":\s*")([^"]*)(".*)$', l)
                if m:
                    lignes[i] = m.group(1) + m.group(2) + "-essai" + m.group(3)
        return lignes
    p = copie / "manifeste.json"
    lignes, fin = lignes_de(p)
    ecrire_lignes(p, transformer(lignes), fin)


CORRECTIONS_SAIN = ("# Corrections v6 — essai synthétique des gardes\n\n"
                    "- Quoi : la constante de la ligne modifiée change de valeur.\n"
                    "- Où : principal.py, ligne indiquée par la pièce de périmètre.\n")
ESSAI_SAIN = ('"""Essai synthétique des gardes (aucun essai réel)."""\n\n\n'
              "def test_corrections_v6_synthetique():\n    assert 1 + 1 == 2\n")


def accompagnement_sain(copie):
    changer_version(copie)
    changer_manifeste(copie, "version")
    changer_manifeste(copie, "description")
    ecrire(copie / "CORRECTIONS-v6.md", CORRECTIONS_SAIN)
    ecrire(copie / "tests" / "test_corrections_v6.py", ESSAI_SAIN)


# ---------------------------------------------------------------------------------------------------------------------


def principal():
    ap = argparse.ArgumentParser(description="Essais des gardes de la boucle extérieure du pilote 4 (v1).")
    ap.add_argument("--journal", required=True, type=pathlib.Path)
    ap.add_argument("--racine", type=pathlib.Path, default=ICI.parent)
    ap.add_argument("--garder-travail", action="store_true")
    a = ap.parse_args()
    racine = a.racine.resolve()
    F, F2 = racine / "fournis", racine / "fournis-v2"
    if a.journal.exists():
        sys.exit("le journal existe déjà : rien n'est écrasé")
    journal = open(a.journal, "x", encoding="utf-8")
    interpretes = []
    for nom in ("python3.11", "python3.12", "python3.13"):
        chemin = shutil.which(nom)
        if chemin is None:
            journal.write(f"{heure()}  NON CONFORME | banc | interpréteur absent : {nom}\n")
            sys.exit(f"interpréteur absent : {nom}")
        version = subprocess.run([chemin, "-I", "-c", "import sys; print(sys.version.split()[0])"], check=True,
                                 capture_output=True, text=True, env=ENV).stdout.strip()
        interpretes.append((nom, chemin, version))
    travail = racine / "travail" / f"essais-gardes-v1-{heure().replace(':', '').replace('-', '')}"
    travail.mkdir(parents=True, exist_ok=False)
    banc = Banc(journal, interpretes, travail)
    banc.ecrire("# Journal des essais des gardes de la boucle extérieure du pilote 4 — v1 (heures lues sur date -u)")
    banc.ecrire(f"banc : {pathlib.Path(__file__).name}, sha256 {sha(__file__)} ; racine {racine} ; travail "
                f"{travail.name} ; graine des valeurs synthétiques {GRAINE_ESSAIS} (valeurs jamais écrites ici)")
    banc.ecrire("interpréteurs : " + " ; ".join(f"{n} ({c}) {v}" for n, c, v in interpretes))

    # Compagnons des scripts, avant toute exécution (R4)
    for cle, nom in sorted(SCRIPTS.items()):
        p = ICI / nom
        comp = p.with_name(nom + ".sha256")
        ok = comp.exists() and comp.read_text(encoding="utf-8") == f"{sha(p)}  {nom}\n"
        banc.ecrire(f"{'conforme' if ok else 'NON CONFORME'} | compagnon | {nom} | sha256 {sha(p)}")
        if not ok:
            banc.non_conformes.append(f"compagnon {nom}")
    if banc.non_conformes:
        banc.ecrire("arrêt : compagnon d'un script en échec ; aucun essai lancé")
        sys.exit(1)

    # Pièces fournies
    liste = (racine / "EMPREINTES-fournis-v1.txt").read_text(encoding="utf-8").split("\n")
    ko = [l.split("  ", 1)[1] for l in liste if l and sha(F / l.split("  ", 1)[1]) != l.split("  ", 1)[0]]
    banc.ecrire(f"{'conforme' if not ko else 'NON CONFORME'} | pièces fournies | EMPREINTES-fournis-v1.txt : "
                f"{len([l for l in liste if l]) - len(ko)} OK, {len(ko)} en échec")
    for p in sorted(F2.glob("*.md")):
        ok = (F2 / (p.name + ".sha256")).read_text(encoding="utf-8") == f"{sha(p)}  {p.name}\n"
        banc.ecrire(f"{'conforme' if ok else 'NON CONFORME'} | pièces fournies | fournis-v2/{p.name} sha256 {sha(p)}")
        ko += [] if ok else [p.name]
    objet = F / "objet-v6-2-1" / "organisme"
    ok = empreinte_arbre(objet) == ARBRE_OBJET
    banc.ecrire(f"{'conforme' if ok else 'NON CONFORME'} | pièces fournies | empreinte d'arbre de l'objet "
                f"{'égale à' if ok else 'différente de'} {ARBRE_OBJET}")
    if ko or not ok:
        banc.non_conformes.append("pièces fournies")
        banc.ecrire("arrêt : pièces fournies en échec")
        sys.exit(1)

    rng = random.Random(GRAINE_ESSAIS)
    carte_json, zones_json = F / "carte-v1" / "carte-facteurs-v1.json", F / "carte-v1" / "zones-interdites-v1.json"
    carte = json.loads(carte_json.read_text(encoding="utf-8"))
    zones = json.loads(zones_json.read_text(encoding="utf-8"))
    entrees = {e["id"]: e for fa in carte["facteurs"] for e in fa["entrees"]}
    segz = {s["id"]: s for s in zones["segments"]}
    phb = {p["id"]: p for p in carte["points_hors_boucle"]}

    essais_assemblage(banc, travail, F, F2, objet)
    corrige = essais_g5(banc, travail, F, objet, carte, zones, carte_json, zones_json, entrees, segz, phb, rng)
    essais_g4(banc, travail, objet, corrige, carte, entrees, rng)
    essais_g6(banc, travail)
    essais_g8(banc, travail, rng)
    essais_g9(banc, travail, rng)

    banc.ecrire(f"bilan : {banc.nb} essais, {banc.nb - len(banc.non_conformes)} conformes, "
                f"{len(banc.non_conformes)} non conformes" + (" : " + " ; ".join(banc.non_conformes)
                                                              if banc.non_conformes else ""))
    if not a.garder_travail:
        shutil.rmtree(travail)
        banc.ecrire(f"dossier de travail {travail.name} effacé (contenu interdit planté et valeurs synthétiques "
                    f"compris)")
    journal.close()
    sys.exit(1 if banc.non_conformes else 0)


# ---------------------------------------------------------------------------------------------------------------------
# Assemblage du dossier de lecture : G1, G2, G8 bis (b), G12


def releve_texte(dossier, liste, **surcharges):
    champs = {
        "releve.version": "1",
        "releve.script_empreinte": sha_texte("script du relevé synthétique des essais des gardes"),
        "releve.heure": heure(),
        "releve.dossier": dossier,
        "releve.course": COURSE_S,
        "sources.liste_fermee": liste,
        "sources.liste_fermee_verifiee": "oui",
        "sources.extrait": "absent",
        "sources.lancement": "absent",
        "sources.manifeste": "absent",
        "sources.champs_ignores": "0",
        "identite.commit": "0123456789abcdef0123456789abcdef01234567",
        "identite.arbre": ARBRE_OBJET,
        "identite.nb_fichiers": "26",
        "identite.graine": "1234567890123456789",
        "identite.graine_manifeste": "absent",
        "identite.lanceur": "lancer_pilote4_gemini_v11.sh",
        "identite.lanceur_empreinte": sha_texte("lanceur synthétique des essais des gardes"),
        "identite.noyau": "absent",
        "identite.banque_empreinte": "absent",
        "identite.texte_empreinte": "absent",
        "identite.question": "s",
        "identite.question_empreinte": sha_texte("question synthétique des essais des gardes"),
        "identite.lignee": LIGNEE_S,
        "identite.lignee_source": "deduite_de_la_cle_controle_non_independant",
        "identite.porte_m_precedente": "oui",
        "segments.nombre": "1",
        "segments.1.fin": "fermeture",
        "segments.1.heure_fin": heure(),
        "segments.1.code": "0",
        "fin.lignee": "absent",
        "fin.dernier_code": "0",
        "fin.liste_fermee_poussee": "oui",
        "fin.recherche_cles_faite": "oui",
        "fin.reprise_attendue": "non",
    }
    for cle, v in surcharges.items():
        champs[cle.replace("__", ".")] = v
    return "".join(f"{k} = {v}\n" for k, v in champs.items() if v is not None)


def course_synthetique(base, variante=""):
    """Dossier de course synthétique (aucun fichier réel), avec sa liste fermée."""
    d = base / DOSSIER_S
    fichiers = {"LANCEMENT.md": "lancement synthétique des essais des gardes\n",
                "journal-appels-g000.jsonl": "{}\n",
                "organisme/principal.py": "# organisme synthétique des essais des gardes\n",
                "sortie-erreur-lanceur.txt": ""}
    for rel, t in fichiers.items():
        ecrire(d / rel, t)
    compagnon(d / "LANCEMENT.md")
    noms = sorted(p.relative_to(d).as_posix() for p in d.rglob("*") if p.is_file())
    ecrire(d / "A-POUSSER-v1.txt", "".join(n + "\n" for n in noms + ["A-POUSSER-v1.txt"]))
    noms.append("A-POUSSER-v1.txt")
    lignes = [f"{sha(d / n)}  {n}\n" for n in noms]
    if variante == "falsifiee":
        h, n = lignes[0].split("  ", 1)
        lignes[0] = ("0" if h[0] != "0" else "1") + h[1:] + "  " + n
    if variante != "sans_liste":
        avec_compagnon(d / "EMPREINTES-pilote-v1.txt", "".join(lignes))
    if variante == "hors_liste":
        ecrire(d / "fichier-ajoute-apres-la-liste.txt", "ajout synthétique\n")
    if variante == "lien":
        os.symlink("LANCEMENT.md", d / "lien-symbolique.md")
    return d


def essais_assemblage(banc, travail, F, F2, objet):
    T = travail / "assemblage"
    course_v14 = F / "serie-v14" / "cas-sain-v6-2-s" / DOSSIER_S
    script3 = avec_compagnon(T / "script" / "lire_pilote4_v3.py",
                             "# script de lecture synthétique des essais des gardes : aucun calcul, aucune donnée\n")
    script2 = avec_compagnon(T / "script-v2" / "lire_pilote4_v2.py", "# script synthétique, version 2\n")
    registre = avec_compagnon(T / "registre" / "registre-hypotheses-conception-pilote4-v5.md",
                              "# Registre synthétique des essais des gardes\n\nAucune fiche réelle.\n")
    protocole = F2 / "protocole-boucle-exterieure-pilote4-v4.md"
    carte_md, zones_md = F / "carte-v1" / "carte-facteurs-v1.md", F / "carte-v1" / "zones-interdites-v1.md"
    decisions = avec_compagnon(T / "ref" / "registre-decisions-essai-v1.md",
                               "1. Décision synthétique d'ouverture (essai des gardes).\n")

    def ouverture(dossier_ou, nom, reference=True, heure_ok=True, vide=False, tronquee=False):
        if vide:
            return avec_compagnon(dossier_ou / nom, "")
        h = sha(decisions)
        lignes = ["Ouverture synthétique de la lecture (essai des gardes ; aucune décision réelle)."]
        if reference:
            lignes.append(f"- référence : ligne 1 de {decisions.name}, sha256 {h[:12] + '…' if tronquee else h}")
        if heure_ok:
            lignes.append(f"- écrite le {heure()} (heure lue sur date -u)")
        return avec_compagnon(dossier_ou / nom, "\n".join(lignes) + "\n")

    test_json = {"piece": "lecture synthétique des essais des gardes, part test (aucune donnée)", "dossier": DOSSIER_S,
                 "part": "test",
                 "cellules_ii": [{"famille": "conscience d'évaluation", "libelle": "non distinct de la référence"},
                                 {"famille": "contrôle de délégation",
                                  "libelle": "impossible par construction (référence égale à 1)"}],
                 "signalements (fichier test)": 0}
    test_md = ("# Lecture synthétique des essais des gardes — part test\n\n"
               "- conscience d'évaluation : non distinct de la référence\n"
               "- contrôle de délégation : impossible par construction (référence égale à 1)\n"
               "- signalements (fichier test) : 0\n"
               "- phrase (iv) (brief du script v3, § 3, point 5) : tout le reste est « dans le bruit » : à une graine "
               "par course, le bruit entre graines n'est pas mesuré ; aucune comparaison entre les deux courses n'est "
               "faite (mêmes tâches, même objet, questions différentes : un écart entre elles tient à la question, à la "
               "graine ou au bruit, sans moyen de les séparer ; les verdicts des agents de la boucle extérieure restent "
               "tenus par cet interdit) ; un changement au-delà du bruit des tâches dans une course peut tenir à sa "
               "graine\n")

    def lectures(dossier_ou, version=3, json_plus=None, md_plus="", dossier=DOSSIER_S, genre="test", nom_json=None,
                 nom_md=None):
        base = f"lecture-{dossier}-{genre}-v{version}"
        j = dict(test_json)
        if json_plus:
            j.update(json_plus)
        pj = avec_compagnon(dossier_ou / (nom_json or base + ".json"), json.dumps(j, ensure_ascii=False, indent=1)
                            + "\n")
        pm = avec_compagnon(dossier_ou / (nom_md or base + ".md"), test_md + md_plus)
        return pj, pm

    def finale(dossier_ou, genre_json="quatre", genre_md="quatre", version=3, nom_json=None):
        contenu = "contenu synthétique, jamais lu par l'assemblage (test_final, valeur p, (iii))\n"
        pj = avec_compagnon(dossier_ou / (nom_json or f"lecture-{DOSSIER_S}-test-final-holm-{genre_json}-v{version}"
                                                      f".json"), contenu)
        pm = avec_compagnon(dossier_ou / f"lecture-{DOSSIER_S}-test-final-holm-{genre_md}-v{version}.md", contenu)
        return pj, pm

    sorties = T / "sorties"
    sorties.mkdir(parents=True)
    base_ok = T / "base"
    syn = course_synthetique(T / "course-syn")
    ouv = ouverture(base_ok, f"ouverture-lecture-{DOSSIER_S}-v1.txt")
    ouv_finale = ouverture(base_ok / "finale", f"ouverture-lecture-finale-{DOSSIER_S}-v1.txt")
    lj, lm = lectures(base_ok)
    fj, fm = finale(base_ok / "holm4")
    dj, dm = finale(base_ok / "holm2", "deux", "deux")
    rel_v14 = avec_compagnon(base_ok / "releve-v14" / f"releve-mecanique-{DOSSIER_S}-v1.txt",
                             releve_texte(DOSSIER_S, sha(course_v14 / "EMPREINTES-pilote-v1.txt")))
    rel_syn = avec_compagnon(base_ok / "releve-syn" / f"releve-mecanique-{DOSSIER_S}-v1.txt",
                             releve_texte(DOSSIER_S, sha(syn / "EMPREINTES-pilote-v1.txt")))

    def args(ident, mode="course", **sur):
        def f(tag):
            v = {"mode": mode, "dossier": DOSSIER_S, "sortie": sorties / f"{ident}-{tag}", "dossier-course": syn,
                 "releve": rel_syn, "ouverture": ouv if mode == "course" else ouv_finale,
                 "lecture-json": lj if mode == "course" else fj, "lecture-md": lm if mode == "course" else fm,
                 "registre": registre, "protocole": protocole, "script-lecture": script3,
                 "commit-attendu": "0123456789abcdef0123456789abcdef01234567", "arbre-attendu": ARBRE_OBJET}
            if mode == "course":
                v.update({"objet": objet, "carte": carte_md, "zones": zones_md})
            v.update({k.replace("_", "-"): x for k, x in sur.items()})
            res = []
            for k, x in v.items():
                if x is not None:
                    res += [f"--{k}", x]
            return res
        return f

    def rien_laisse(ident):
        def v(tag, code, out, err):
            d = sorties / f"{ident}-{tag}"
            if d.exists():
                return "dossier de sortie présent après un refus"
            if list(sorties.glob(f".{d.name}.en-cours-*")):
                return "dossier provisoire laissé"
            return None
        return v

    def dossier_conforme(ident, mode):
        def v(tag, code, out, err):
            d = sorties / f"{ident}-{tag}"
            nom_m = "MANIFESTE-DOSSIER-v1.txt" if mode == "course" else "MANIFESTE-DOSSIER-FINAL-v1.txt"
            m = d / nom_m
            if not m.is_file():
                return "manifeste absent"
            lignes = m.read_text(encoding="utf-8").split("\n")
            if not re.fullmatch(rf"# script de lecture : lire_pilote4_v3\.py, sha256 {sha(script3)}, version 3",
                                lignes[0]):
                return "ligne de version du manifeste inattendue"
            r = subprocess.run(["sha256sum", "--strict", "-c", nom_m], cwd=d, capture_output=True, text=True, env=ENV)
            if r.returncode != 0 or "FAILED" in r.stdout:
                return "sha256sum --strict -c du manifeste en échec"
            listes = {l.split("  ", 1)[1] for l in lignes[1:] if l}
            presents = {p.relative_to(d).as_posix() for p in d.rglob("*") if p.is_file()} - {nom_m}
            if listes != presents:
                return "le manifeste ne liste pas exactement les fichiers du dossier"
            if sha(m) not in out:
                return "empreinte du manifeste absente de la sortie standard"
            if any("journal" in p for p in presents):
                return "un journal dans le dossier"
            if list(sorties.glob(f".{d.name}.en-cours-*")):
                return "dossier provisoire laissé"
            attendus = {f"ouverture-lecture-{DOSSIER_S}-v1.txt" if mode == "course" else
                        f"ouverture-lecture-finale-{DOSSIER_S}-v1.txt",
                        f"mecanique/releve-mecanique-{DOSSIER_S}-v1.txt",
                        "registre/registre-hypotheses-conception-pilote4-v5.md",
                        "protocole/protocole-boucle-exterieure-pilote4-v4.md"}
            if mode == "course":
                attendus |= {f"lecture/lecture-{DOSSIER_S}-test-v3.json", f"lecture/lecture-{DOSSIER_S}-test-v3.md",
                             "carte-facteurs-v1.md", "zones-interdites-v1.md"}
            else:
                genre = "deux" if "deux" in ident else "quatre"
                attendus |= {f"lecture-finale/lecture-{DOSSIER_S}-test-final-holm-{genre}-v3.json",
                             f"lecture-finale/lecture-{DOSSIER_S}-test-final-holm-{genre}-v3.md"}
            attendus |= {x + ".sha256" for x in attendus}
            hors_objet = {p for p in presents if not p.startswith("objet/")} - {"objet-EMPREINTE-ARBRE.txt"}
            if hors_objet != attendus:
                return "fichiers du dossier différents de ceux du § 3"
            if mode == "course":
                if empreinte_arbre(d / "objet") != ARBRE_OBJET:
                    return "empreinte d'arbre de objet/ différente"
                if (d / "objet-EMPREINTE-ARBRE.txt").read_text(encoding="ascii") != ARBRE_OBJET + "\n":
                    return "objet-EMPREINTE-ARBRE.txt inattendu"
                if (d / "objet" / "objet-EMPREINTE-ARBRE.txt").exists():
                    return "objet-EMPREINTE-ARBRE.txt dans objet/"
            elif (d / "objet").exists() or "objet-EMPREINTE-ARBRE.txt" in presents:
                return "objet/ dans un dossier de lecture finale"
            return None
        return v

    G, S, A = "assemblage", "sain", "artefact"
    banc.cas(G, "course, cas sain : course simulée v14 (liste fermée vérifiée, fichiers hachés)", S, "assemblage",
             args("sain-v14", dossier_course=course_v14, releve=rel_v14), 0, verif=dossier_conforme("sain-v14", "course"))
    banc.cas(G, "course, cas sain : course synthétique", S, "assemblage", args("sain-syn"), 0,
             verif=dossier_conforme("sain-syn", "course"))

    # G1
    def rel(nom, dossier_course=syn, **sur):
        return avec_compagnon(T / "releves" / nom / f"releve-mecanique-{DOSSIER_S}-v1.txt",
                              releve_texte(DOSSIER_S, sha(dossier_course / "EMPREINTES-pilote-v1.txt"), **sur))
    cas_g1 = [
        ("G1 : course arrêtée par STOP entre deux segments (fin.reprise_attendue = oui)", "stop",
         {"releve": rel("stop", fin__reprise_attendue="oui")}, r"G1 : fin\.reprise_attendue"),
        ("G1 : recherche des clés non consignée (fin.recherche_cles_faite = non)", "cles",
         {"releve": rel("cles", fin__recherche_cles_faite="non")}, r"G1 : fin\.recherche_cles_faite"),
        ("G1 : liste fermée non poussée (fin.liste_fermee_poussee = non)", "poussee",
         {"releve": rel("poussee", fin__liste_fermee_poussee="non")}, r"G1 : fin\.liste_fermee_poussee"),
        ("G1 : champ de fin absent du relevé", "fin-absent",
         {"releve": rel("fin-absent", fin__reprise_attendue=None)}, r"G1 : champ fin\.reprise_attendue absent"),
        ("G1 : le relevé cite une autre liste fermée", "autre-liste",
         {"releve": rel("autre-liste", sources__liste_fermee=sha_texte("autre liste"))}, r"G1 : sources\.liste_fermee"),
    ]
    for texte, ident, sur, motif in cas_g1:
        banc.cas(G, texte, A, "assemblage", args(ident, **sur), 3, motif, rien_laisse(ident))
    for variante, texte, motif in (("sans_liste", "G1 : dossier de course sans liste fermée", r"G1 : liste fermée absente"),
                                   ("falsifiee", "G1 : ligne de la liste fermée falsifiée", r"G1 : liste fermée, ligne 1"),
                                   ("hors_liste", "G1 : fichier hors de la liste fermée", r"G1 : fichier du dossier de "
                                                                                           r"course hors de la liste"),
                                   ("lien", "G1 : lien symbolique dans le dossier de course", r"G1 : .*lien symbolique")):
        d = course_synthetique(T / f"course-{variante}", variante)
        r = rel_syn if variante == "sans_liste" else rel(f"var-{variante}", dossier_course=d)
        banc.cas(G, texte, A, "assemblage", args(variante, dossier_course=d, releve=r), 3, motif, rien_laisse(variante))
    for texte, ident, sur, motif in (
            ("identité : relevé d'un autre dossier de course", "autre-dossier",
             {"releve": rel("autre-dossier", releve__dossier=DOSSIER_M)}, r"identité \(§ 9\) : releve\.dossier"),
            ("identité : commit du segment 1 autre que la tête citée", "autre-commit",
             {"releve": rel("autre-commit", identite__commit="fedcba9876543210fedcba9876543210fedcba98")},
             r"identité \(§ 9\) : identite\.commit"),
            ("identité : arbre de l'organisme autre que celui attendu", "autre-arbre",
             {"releve": rel("autre-arbre", identite__arbre=sha_texte("autre arbre"))}, r"identité \(§ 9\) : identite\.arbre")):
        banc.cas(G, texte, A, "assemblage", args(ident, **sur), 3, motif, rien_laisse(ident))
    banc.cas(G, "identité : commit abrégé à sept caractères (préfixe de la tête)", S, "assemblage",
             args("commit-court", commit_attendu="0123456"), 0, verif=dossier_conforme("commit-court", "course"))

    # G2
    nom_ouv = f"ouverture-lecture-{DOSSIER_S}-v1.txt"
    for texte, ident, chemin, motif in (
            ("G2 : fichier d'ouverture absent", "ouv-absente", T / "ouv-absente" / nom_ouv, r"G2 : fichier d'ouverture absent"),
            ("G2 : fichier d'ouverture vide", "ouv-vide", ouverture(T / "ouv-vide", nom_ouv, vide=True), r"G2 : .*vide"),
            ("G2 : fichier d'ouverture sans référence", "ouv-sans-ref",
             ouverture(T / "ouv-sans-ref", nom_ouv, reference=False), r"G2 : .*aucune référence"),
            ("G2 : référence à empreinte tronquée (non vérifiable)", "ouv-tronquee",
             ouverture(T / "ouv-tronquee", nom_ouv, tronquee=True), r"G2 : .*aucune référence"),
            ("G2 : fichier d'ouverture sans heure UTC", "ouv-sans-heure",
             ouverture(T / "ouv-sans-heure", nom_ouv, heure_ok=False), r"G2 : .*aucune heure"),
            ("G2 : fichier d'ouverture d'une autre course", "ouv-autre",
             ouverture(T / "ouv-autre", f"ouverture-lecture-{DOSSIER_M}-v1.txt"), r"G2 : fichier d'ouverture nommé")):
        banc.cas(G, texte, A, "assemblage", args(ident, ouverture=chemin), 3, motif, rien_laisse(ident))

    # G8 bis (b)
    for texte, ident, kw, motif in (
            ("G8 bis (b) : le fichier test porte le mot test_final", "test-mot", {"md_plus": "- renvoi à test_final\n"},
             r"G8 bis \(b\) : .*le mot test_final"),
            ("G8 bis (b) : le fichier test porte une ligne (iii)", "test-iii",
             {"json_plus": {"cellules_iii": [{"libelle": "synthétique"}]}}, r"G8 bis \(b\) : .*ligne \(iii\)"),
            ("G8 bis (b) : le fichier test porte une valeur p", "test-p", {"md_plus": "- valeur p : synthétique\n"},
             r"G8 bis \(b\) : .*valeur p"),
            ("G8 bis (b) : le fichier test porte la mention d'essai", "test-essai",
             {"md_plus": "- essai : empreintes de banque surchargées\n"}, r"G8 bis \(b\) : .*mention d'essai")):
        pj, pm = lectures(T / ident, **kw)
        banc.cas(G, texte, A, "assemblage", args(ident, lecture_json=pj, lecture_md=pm), 3, motif, rien_laisse(ident))
    tf = avec_compagnon(T / "tf-en-course" / f"lecture-{DOSSIER_S}-test-final-holm-quatre-v3.json",
                        "octets synthétiques\n")
    banc.cas(G, "G8 bis (b) : fichier test_final donné en mode course (refusé sans être ouvert)", A, "assemblage",
             args("tf-en-course", lecture_json=tf), 3, r"G8 bis \(b\) : .*test_final", rien_laisse("tf-en-course"))

    # G12
    pj, pm = lectures(T / "prov", nom_json=f"lecture-{DOSSIER_S}-provisoire-v2.json")
    banc.cas(G, "G12 : fichier de lecture qui porte -provisoire-", A, "assemblage",
             args("prov", lecture_json=pj, lecture_md=pm), 3, r"G12 : .*-provisoire-", rien_laisse("prov"))
    pj, pm = lectures(T / "v2", version=2)
    banc.cas(G, "G12 : fichiers de lecture et script de version 2", A, "assemblage",
             args("v2", lecture_json=pj, lecture_md=pm, script_lecture=script2), 3, r"G12 : script de lecture de "
                                                                                    r"version 2", rien_laisse("v2"))
    pj, pm = lectures(T / "v4", version=4)
    banc.cas(G, "G12 : fichiers de lecture v4, script v3 au manifeste", A, "assemblage",
             args("v4", lecture_json=pj, lecture_md=pm), 3, r"G12 : .*version 4, autre que celle du script",
             rien_laisse("v4"))
    pj, pm = lectures(T / "autre-course", dossier=DOSSIER_M)
    banc.cas(G, "G12 : fichiers de lecture de l'autre course", A, "assemblage",
             args("autre-course", lecture_json=pj, lecture_md=pm), 3, r"G12 : .*ne porte pas le nom du dossier",
             rien_laisse("autre-course"))

    # Compagnons, objet, sortie
    reg_nu = ecrire(T / "reg-nu" / "registre-hypotheses-conception-pilote4-v5.md", "# Registre synthétique\n")
    banc.cas(G, "compagnon absent (registre)", A, "assemblage", args("comp-absent", registre=reg_nu), 3,
             r"compagnon de registre absent", rien_laisse("comp-absent"))
    pj, pm = lectures(T / "comp-faux")
    ecrire(pm.with_name(pm.name + ".sha256"), f"{sha_texte('autre')}  {pm.name}\n", mode="w")
    banc.cas(G, "compagnon faux (fichier de lecture md)", A, "assemblage",
             args("comp-faux", lecture_json=pj, lecture_md=pm), 3, r"REFUS assemblage : compagnon de fichier de lecture "
                                                                    r"md : empreinte",
             rien_laisse("comp-faux"))
    objet_altere = T / "objet-altere"
    shutil.copytree(objet, objet_altere)
    changer_colonne(objet_altere, "principal.py", 31, colonne_dans(objet_altere, "principal.py", 31, 1, 19))
    banc.cas(G, "objet altéré (un caractère)", A, "assemblage", args("objet-altere", objet=objet_altere), 3,
             r"objet : empreinte d'arbre différente", rien_laisse("objet-altere"))
    objet_pyc = T / "objet-pyc"
    shutil.copytree(objet, objet_pyc)
    ecrire(objet_pyc / "__pycache__" / "principal.cpython-313.pyc", "octets synthétiques\n")
    banc.cas(G, "objet avec __pycache__", A, "assemblage", args("objet-pyc", objet=objet_pyc), 3,
             r"objet : fichier compilé", rien_laisse("objet-pyc"))
    for tag_ in ("py311", "py312", "py313"):
        ecrire(sorties / f"existe-{tag_}" / "temoin.txt", "témoin\n")

    def existe_intact(tag, code, out, err):
        t = sorties / f"existe-{tag}"
        if sorted(p.name for p in t.iterdir()) != ["temoin.txt"] or (t / "temoin.txt").read_text() != "témoin\n":
            return "dossier existant modifié"
        return None
    banc.cas(G, "dossier de sortie déjà présent (rien n'est écrasé)", A, "assemblage", args("existe"), 3,
             r"existe déjà", existe_intact)
    banc.cas(G, "usage : --objet en mode finale", A, "assemblage", args("finale-objet", mode="finale", objet=objet), 2,
             r"USAGE assemblage : mode finale")

    # Mode finale
    banc.cas(G, "finale, cas sain : holm-quatre (fichiers test_final copiés sans être ouverts)", S, "assemblage",
             args("finale-quatre", mode="finale"), 0, verif=dossier_conforme("finale-quatre", "finale"))
    banc.cas(G, "finale, cas sain : holm-deux (--sans-seconde-course)", S, "assemblage",
             args("finale-deux", mode="finale", lecture_json=dj, lecture_md=dm), 0,
             verif=dossier_conforme("finale-deux", "finale"))
    banc.cas(G, "finale, G2 : ouverture de fin de course au lieu de l'ouverture finale", A, "assemblage",
             args("finale-ouv", mode="finale", ouverture=ouv), 3, r"G2 : fichier d'ouverture nommé",
             rien_laisse("finale-ouv"))
    banc.cas(G, "finale, G1 : reprise attendue", A, "assemblage",
             args("finale-stop", mode="finale", releve=rel("finale-stop", fin__reprise_attendue="oui")), 3,
             r"G1 : fin\.reprise_attendue", rien_laisse("finale-stop"))
    pj, pm = finale(T / "finale-mix", "quatre", "deux")
    banc.cas(G, "finale, G12 : holm-quatre et holm-deux mêlés", A, "assemblage",
             args("finale-mix", mode="finale", lecture_json=pj, lecture_md=pm), 3, r"G12 : .*même genre",
             rien_laisse("finale-mix"))
    pj, pm = finale(T / "finale-prov", nom_json=f"lecture-{DOSSIER_S}-test-final-provisoire-v2.json")
    banc.cas(G, "finale, G12 : fichier -provisoire-", A, "assemblage",
             args("finale-prov", mode="finale", lecture_json=pj, lecture_md=pm), 3, r"G12 : .*-provisoire-",
             rien_laisse("finale-prov"))
    banc.cas(G, "finale, G12 : fichiers test (fin de course) au lieu de test_final", A, "assemblage",
             args("finale-test", mode="finale", lecture_json=lj, lecture_md=lm), 3, r"G12 : .*n'est pas un fichier "
                                                                                    r"test_final", rien_laisse("finale-test"))
    pj, pm = finale(T / "finale-v2", version=2)
    banc.cas(G, "finale, G12 : fichiers test_final de version 2", A, "assemblage",
             args("finale-v2", mode="finale", lecture_json=pj, lecture_md=pm), 3, r"G12 : .*version 2",
             rien_laisse("finale-v2"))


# ---------------------------------------------------------------------------------------------------------------------
# G5


def essais_g5(banc, travail, F, objet, carte, zones, carte_json, zones_json, entrees, segz, phb, rng):
    T = travail / "g5"
    comptes = {"n": 0}

    def preparer(ident, changements, perimetre, carte_p=None, zones_p=None, noms=("objet-origine", "copie-organisme"),
                 apres_diff=None):
        d = T / ident
        d.mkdir(parents=True)
        shutil.copytree(objet, d / noms[0])
        shutil.copytree(objet, d / noms[1])
        changements(d / noms[1])
        per = avec_compagnon(d / "perimetre-essai-ronde-1-v1.md",
                             "# Pièce de périmètre — essai synthétique des gardes (aucune correction réelle)\n\n"
                             + perimetre)
        diff = d / "correction-essai-ronde-1-v1.diff"
        with open(diff, "xb") as f:
            r = subprocess.run(["diff", "-ruN", noms[0], noms[1]], cwd=d, stdout=f, env=dict(ENV, LC_ALL="C"))
        if r.returncode not in (0, 1):
            raise RuntimeError("diff en erreur")
        if apres_diff:
            apres_diff(diff)
        compagnon(diff)
        cj, zj = carte_p or carte_json, zones_p or zones_json
        return ["--diff", diff, "--perimetre", per, "--empreinte-perimetre", sha(per), "--carte", cj,
                "--empreinte-carte", sha(cj), "--zones", zj, "--empreinte-zones", sha(zj), "--objet", d / noms[0],
                "--copie", d / noms[1]]

    def cas(texte, genre, code, motif, changements, perimetre, discret=False, **kw):
        comptes["n"] += 1
        a = preparer(f"c{comptes['n']:03d}", changements, perimetre, **kw)
        banc.cas("G5", texte, genre, "G5", a, code, motif, discret=discret)
        return a

    def seg(sid):
        s = entrees.get(sid) or segz.get(sid) or phb.get(sid)
        return (s["fichier"], s.get("ligne_debut", s.get("ligne")), s["colonne_debut"], s["colonne_fin"])

    def dans(sid):
        f, n, c1, c2 = seg(sid)
        return lambda c: changer_colonne(c, f, n, colonne_dans(c, f, n, c1, c2))

    def hors(f, n, *sids):
        segs = [seg(s)[2:] for s in sids]
        return lambda c: changer_colonne(c, f, n, colonne_hors(c, f, n, segs))

    def ligne(f, n, col=None):
        return lambda c: changer_colonne(c, f, n, col or colonne_hors(c, f, n, []))

    def valeur(f, n):
        """Change le dernier chiffre de la ligne (une valeur, pas un nom)."""
        def g(c):
            l = lignes_de(c / f)[0][n - 1]
            changer_colonne(c, f, n, [i for i in range(1, len(l) + 1) if l[i - 1].isdigit()][-1])
        return g

    def tous(*fs):
        def g(c):
            for x in fs:
                x(c)
        return g

    acc = "- accompagnement : manifeste.json (version, description) ; principal.py, l. 27 (VERSION) ; CORRECTIONS-v6.md ; " \
          "tests/test_corrections_v6.py\n"
    S, A = "sain", "artefact"
    sain_f02 = cas("cas sain : F02 (l. 31) et la liste d'accompagnement (manifeste, VERSION l. 27, CORRECTIONS-v6, "
                   "test_corrections_v6)", S, 0, None, tous(valeur("principal.py", 31), accompagnement_sain),
                   "- facteur : F02 — nombre de tâches d'entraînement du score interne\n"
                   "- lieu : principal.py, <module>, l. 31\n" + acc)
    corrige = pathlib.Path(sain_f02[sain_f02.index("--copie") + 1])
    cas("cas sain : VERSION (l. 27) jointe à une correction de F03 : ne compte pas comme un second facteur", S, 0, None,
        tous(dans("F03.1"), changer_version), "- facteur : F03\n- lieu : principal.py, executer, l. 2103\n"
                                               "- accompagnement : principal.py, l. 27 (VERSION)\n")
    for sid, fid, lieu in (("F03.1", "F03", "l. 2103"), ("F03.2", "F03", "l. 2104"), ("F01.2", "F01", "l. 2104"),
                           ("F10.1", "F10", "l. 2103"), ("F12.1", "F12", "l. 997"), ("F05.2", "F05", "l. 988–998")):
        f, n, _, _ = seg(sid)
        cas(f"cas sain : ligne partagée {f} l. {n}, caractère changé dans le segment {sid} de {fid}", S, 0, None,
            dans(sid), f"- facteur : {fid}\n- lieu : {f}, {entrees[sid]['fonction']}, {lieu}\n")
    for zid, element in (("Z03.s1", "F04-b"), ("Z03.s2", "F04-b"), ("Z03.s3", "F04-b")):
        f, n, _, _ = seg(zid)
        per = f"- facteur : F04 — un élément du contrat\n- élément : {element}\n- lieu : {f}, " \
              f"_synthetiser_mutation_politique_endogene, l. {n}\n"
        cas(f"cas sain : {f} l. {n} (segment gelé {zid}) : un autre segment de la ligne change, dans {element}", S, 0,
            None, hors(f, n, zid), per)
        cas(f"(c) : {f} l. {n} : un caractère du segment gelé {zid} change", A, 3, r"REFUS G5 \(c\) .*segment interdit",
            dans(zid), per)
    for pid, fid, lieu in (("PHB-1", "F05", "l. 988–996"), ("PHB-2", "F13", "l. 59–83"), ("PHB-3", "F14", "l. 104–123"),
                           ("PHB-4", "F06", "l. 123–139")):
        f, n, _, _ = seg(pid)
        per = f"- facteur : {fid}\n- lieu : {f}, {phb[pid]['fonction']}, {lieu}\n"
        cas(f"cas sain : {f} l. {n} (point hors boucle {pid}) : un autre segment de la ligne change, dans {fid}", S, 0,
            None, hors(f, n, pid), per)
        cas(f"(h) : {f} l. {n} : un caractère du point hors boucle {pid} change", A, 3, r"REFUS G5 \(h\) ", dans(pid), per)
    cas("cas sain : F09, exception « défaut du chemin des réponses — délai » sur une ligne E (principal.py l. 1698)", S,
        0, None, ligne("principal.py", 1698), "- facteur : F09 — défaut de code nommé\n- exception : défaut du chemin "
                                              "des réponses — délai\n- lieu : principal.py, _traiter_tache, l. 1698\n")
    cas("cas sain : F09, une ligne de son domaine (principal.py l. 2110)", S, 0, None, ligne("principal.py", 2110),
        "- facteur : F09 — défaut de code nommé\n- lieu : principal.py, executer, l. 2110\n")
    cas("cas sain : ligne insérée après la l. 1932 (F02 ; voisine libre), règle 9 de la carte", S, 0, None,
        lambda c: inserer_apres(c, "principal.py", 1932, ["_essai_insere = 0"]),
        "- facteur : F02\n- lieu : principal.py, executer, l. 1932\n")
    cas("cas sain : essai hérité adapté et déclaré (tests/test_emprunts_v5_3.py), avec F01", S, 0, None,
        tous(dans("F01.2"), ligne("tests/test_emprunts_v5_3.py", 200)),
        "- facteur : F01\n- lieu : principal.py, executer, l. 2104\n"
        "- essai hérité adapté : tests/test_emprunts_v5_3.py — raison : essai synthétique\n")

    # Carte de même forme, autre version : la l. 32 passe de F16 à F02 (G5 lit le JSON, rien n'est câblé)
    bis = json.loads(json.dumps(carte))
    for fa in bis["facteurs"]:
        if fa["id"] == "F16":
            fa["entrees"] = [e for e in fa["entrees"] if e["id"] != "F16.1"]
        if fa["id"] == "F02":
            fa["entrees"].append({"id": "F02.3", "fichier": "principal.py", "ligne_debut": 32, "ligne_fin": 32,
                                  "fonction": "<module>"})
    carte_bis = avec_compagnon(T / "cartes" / "carte-facteurs-v1-bis.json", json.dumps(bis, ensure_ascii=False))
    per_31_32 = "- facteur : F02\n- lieu : principal.py, <module>, l. 31–32\n"
    cas("cas sain : carte de même forme (v1-bis synthétique : l. 32 à F02) ; F02 sur les l. 31 et 32", S, 0, None,
        tous(valeur("principal.py", 31), valeur("principal.py", 32)), per_31_32, carte_p=carte_bis)

    # (a) à (i)
    cas("(a) : une ligne de F01 (l. 2102) et une ligne de F02 (l. 31), périmètre F01", A, 3,
        r"REFUS G5 \(a\) .*facteur F02", tous(ligne("principal.py", 2102), valeur("principal.py", 31)),
        "- facteur : F01\n- lieu : principal.py, executer, l. 2102\n")
    cas("(a) : une ligne de F02 (l. 31) et une ligne de F16 (l. 32), périmètre F02", A, 3, r"REFUS G5 \(a\) .*F16",
        tous(valeur("principal.py", 31), valeur("principal.py", 32)), "- facteur : F02\n- lieu : principal.py, <module>, "
                                                                     "l. 31\n")
    cas("(b) : le périmètre et le diff du cas « carte v1-bis », lus avec la carte v1 (l. 32 à F16)", A, 3,
        r"REFUS G5 \(b\) .*F16", tous(valeur("principal.py", 31), valeur("principal.py", 32)), per_31_32)
    cas("(a) : ligne insérée entre la l. 31 (F02) et la l. 32 (F16), règle 9", A, 3, r"REFUS G5 \(a\) .*règle 9",
        lambda c: inserer_apres(c, "principal.py", 31, ["_essai_insere = 0"], retrait_de=31),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n")
    cas("(b) : périmètre F03 qui couvre la l. 2102 de F01", A, 3, r"REFUS G5 \(b\) .*deux facteurs", dans("F03.1"),
        "- facteur : F03\n- lieu : principal.py, executer, l. 2102–2104\n")
    cas("(b) : ligne « facteur : » qui nomme deux facteurs", A, 3, r"REFUS G5 \(b\) .*2 facteurs",
        valeur("principal.py", 31), "- facteur : F02 et F16\n- lieu : principal.py, <module>, l. 31\n")
    cas("(b) : deux éléments de F04 déclarés", A, 3, r"REFUS G5 \(b\) .*2 éléments",
        hors("principal.py", 1009, "Z03.s1"), "- facteur : F04\n- élément : F04-a, F04-b\n- lieu : principal.py, "
                                              "_synthetiser_mutation_politique_endogene, l. 1009\n")
    cas("(b) : pièce de périmètre sans ligne « facteur : »", A, 3, r"REFUS G5 \(b\) .*aucune ligne « facteur",
        valeur("principal.py", 31), "- lieu : principal.py, <module>, l. 31\n")
    cas("(c) : ligne d'une zone R (principal.py l. 1650), périmètre F09 sur une ligne de son domaine", A, 3,
        r"REFUS G5 \(c\) .*zone interdite Z02", ligne("principal.py", 1650),
        "- facteur : F09\n- lieu : principal.py, executer, l. 2110\n")
    cas("(c) : ligne E (l. 1698) sous F09 sans l'exception déclarée", A, 3, r"REFUS G5 \(c\) .*Z02",
        ligne("principal.py", 1698), "- facteur : F09\n- lieu : principal.py, _traiter_tache, l. 1698\n")
    cas("(c) : ligne E « délai » (l. 1698) sous l'exception « format »", A, 3, r"REFUS G5 \(c\) .*Z02",
        ligne("principal.py", 1698), "- facteur : F09\n- exception : défaut du chemin des réponses — format\n"
                                     "- lieu : principal.py, _traiter_tache, l. 1698\n")
    cas("(c) : ligne de zone (Z03, l. 1046) touchée sous F04-b déclaré sur la l. 1045", A, 3,
        r"REFUS G5 \(c\) .*Z03", ligne("principal.py", 1046),
        "- facteur : F04\n- élément : F04-b\n- lieu : principal.py, _synthetiser_mutation_politique_endogene, l. 1045\n")
    cas("(d) : fichier nouveau à la racine (aide_essai.py)", A, 3, r"REFUS G5 \(d\) .*aide_essai\.py",
        tous(valeur("principal.py", 31), lambda c: ecrire(c / "aide_essai.py", "VALEUR = 1\n")),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n")
    cas("(d) : fichier nouveau dans tests/ hors de la forme test_corrections_v<N>.py", A, 3,
        r"REFUS G5 \(d\) .*test_autre_v6\.py",
        tous(valeur("principal.py", 31), lambda c: ecrire(c / "tests" / "test_autre_v6.py", ESSAI_SAIN)),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n")
    cas("(d) : fichier de l'objet supprimé (tests/test_corrections_v2.py)", A, 3, r"REFUS G5 \(d\) .*supprimé",
        tous(valeur("principal.py", 31), lambda c: os.remove(c / "tests" / "test_corrections_v2.py")),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n")
    lettres = "".join(chr(ord("a") + (b % 26)) for b in hashlib.sha256(str(rng.random()).encode()).digest())
    mots = [lettres[i:i + 6] for i in range(0, 30, 6)]
    cas("(e) : liste de mots inventés dans un essai nouveau", A, 3, r"REFUS G5 \(e\) ",
        tous(valeur("principal.py", 31), lambda c: ecrire(c / "tests" / "test_corrections_v6.py",
                                                         ESSAI_SAIN + "\n\nLISTE = " + json.dumps(mots) + "\n")),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n", discret=True)
    cas("(e) : nom de fiche dans un CORRECTIONS-v6.md nouveau", A, 3, r"REFUS G5 \(e\) ",
        tous(valeur("principal.py", 31), lambda c: ecrire(c / "CORRECTIONS-v6.md", CORRECTIONS_SAIN + "- Motif : fiche "
                                                         + "HC-P4" + "-03.\n")),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n", discret=True)
    cas("(e) : identifiant de tâche de la forme t-0001 dans un essai nouveau", A, 3, r"REFUS G5 \(e\) ",
        tous(valeur("principal.py", 31), lambda c: ecrire(c / "tests" / "test_corrections_v6.py",
                                                         ESSAI_SAIN + f"\n\nTACHE = \"t-{rng.randrange(10000):04d}\"\n")),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n", discret=True)

    def prefixes_autres(diff):
        t = diff.read_text(encoding="utf-8")
        t = t.replace("+++ copie-organisme/", "+++ autre/", 1)
        diff.write_text(t, encoding="utf-8")
    cas("(f) : en-têtes aux préfixes ancien/ et nouveau/", A, 3, r"REFUS G5 \(f\) ", valeur("principal.py", 31),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n", noms=("ancien", "nouveau"))
    cas("(f) : en-tête « +++ » au préfixe autre/", A, 3, r"REFUS G5 \(f\) ", valeur("principal.py", 31),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n", apres_diff=prefixes_autres)
    cas("(g) : ligne partagée l. 997 : caractère changé hors des segments (reste de la ligne)", A, 3,
        r"REFUS G5 \(g\) .*reste de la ligne", hors("principal.py", 997, "F12.1", "F05.2"),
        "- facteur : F05\n- lieu : principal.py, _synthetiser_mutation_politique_endogene, l. 988–998\n")
    cas("(g) : ligne partagée l. 2103 : caractère du segment de F10 changé sous F03", A, 3,
        r"REFUS G5 \(g\) .*segment de F10", dans("F10.1"), "- facteur : F03\n- lieu : principal.py, executer, l. 2103\n")
    cas("(g) : ligne partagée l. 2104 : un bloc qui couvre les segments de F01 et de F03", A, 3,
        r"REFUS G5 \(g\) .*segment de F01",
        lambda c: changer_ligne(c, "principal.py", seg("F01.2")[1],
                                lambda l: l[:seg("F01.2")[2] + 2] + l[seg("F01.2")[2] + 2:seg("F03.2")[3] - 2].swapcase()
                                + l[seg("F03.2")[3] - 2:]),
        "- facteur : F03\n- lieu : principal.py, executer, l. 2104\n")
    cas("(i) : principal.py l. 26 déclarée comme accompagnement", A, 3, r"REFUS G5 \(i\) .*l\. 26",
        tous(valeur("principal.py", 31), lambda c: changer_ligne(c, "principal.py", 26, lambda l: l + "# essai")),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n- accompagnement : principal.py, l. 26\n")
    cas("(i) : principal.py déclaré comme accompagnement, changement hors de la ligne VERSION (l. 26)", A, 3,
        r"REFUS G5 \(i\) .*hors de la ligne VERSION",
        tous(valeur("principal.py", 31), lambda c: changer_ligne(c, "principal.py", 26, lambda l: l + "# essai")),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n- accompagnement : principal.py (VERSION)\n")
    cas("(i) : ligne VERSION changée hors de sa forme", A, 3, r"REFUS G5 \(i\) .*VERSION",
        tous(valeur("principal.py", 31),
             lambda c: changer_ligne(c, "principal.py", ligne_version(c), lambda l: l.split("=")[0] + "= 7")),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n")
    cas("hors périmètre : ligne de F04-b non déclarée (l. 1045), périmètre l. 1009", A, 3,
        r"REFUS G5 : .*hors du périmètre déclaré", ligne("principal.py", 1045),
        "- facteur : F04\n- élément : F04-b\n- lieu : principal.py, _synthetiser_mutation_politique_endogene, l. 1009\n")

    def decaler_bloc(diff):
        t = diff.read_text(encoding="utf-8")
        m = re.search(r"^@@ -(\d+),(\d+) \+(\d+),(\d+) @@", t, re.M)
        nouveau = f"@@ -{int(m.group(1)) + 10},{m.group(2)} +{int(m.group(3)) + 10},{m.group(4)} @@"
        diff.write_text(t[:m.start()] + nouveau + t[m.end():], encoding="utf-8")
    cas("diff dont l'en-tête de bloc est décalé (lignes qui ne sont pas celles de l'objet)", A, 3,
        r"ne correspond pas à l'objet", valeur("principal.py", 31), "- facteur : F02\n- lieu : principal.py, <module>, "
                                                                     "l. 31\n", apres_diff=decaler_bloc)
    a = preparer("empreinte-perimetre", valeur("principal.py", 31), "- facteur : F02\n- lieu : principal.py, <module>, "
                                                                     "l. 31\n")
    a[a.index("--empreinte-perimetre") + 1] = sha_texte("autre pièce")
    banc.cas("G5", "pièce de périmètre autre que celle empreintée avant le diff", A, "G5", a, 3,
             r"pièce de périmètre : empreinte différente")
    a = preparer("copie-hors-diff", valeur("principal.py", 31), "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n")
    changer_colonne(pathlib.Path(a[a.index("--copie") + 1]), "principal.py", 2110,
                    colonne_hors(pathlib.Path(a[a.index("--copie") + 1]), "principal.py", 2110, []))
    banc.cas("G5", "copie-organisme changée hors du diff", A, "G5", a, 3, r"copie-organisme : principal\.py n'est pas")
    cas("manifeste.json : champ « nom » changé (zone Z11)", A, 3, r"REFUS G5 \(c\) manifeste\.json",
        tous(valeur("principal.py", 31), lambda c: changer_manifeste(c, "nom")),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n")
    cas("essai hérité modifié sans déclaration", A, 3, r"essai hérité modifié sans",
        tous(dans("F01.2"), ligne("tests/test_emprunts_v5_3.py", 200)),
        "- facteur : F01\n- lieu : principal.py, executer, l. 2104\n")
    cas("fichier binaire dans le diff", A, 3, r"fichier binaire",
        tous(valeur("principal.py", 31), lambda c: (c / "metrique" / "__init__.py").write_bytes(b"\x00\x01\xff\xfe")),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n")
    cas("diff vide", A, 3, r"diff vide", lambda c: None, "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n")
    incoherente = json.loads(json.dumps(carte))
    for fa in incoherente["facteurs"]:
        if fa["id"] == "F02":
            fa["entrees"].append({"id": "F02.9", "fichier": "principal.py", "ligne_debut": 32, "ligne_fin": 32,
                                  "fonction": "<module>"})
    carte_inco = avec_compagnon(T / "cartes" / "carte-facteurs-incoherente.json", json.dumps(incoherente))
    cas("carte incohérente (une ligne dans deux facteurs)", A, 3, r"carte incohérente", valeur("principal.py", 31),
        "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n", carte_p=carte_inco)
    inconnue = json.loads(json.dumps(carte))
    inconnue["champ_nouveau"] = []
    carte_inc = avec_compagnon(T / "cartes" / "carte-facteurs-champ-inconnu.json", json.dumps(inconnue))
    cas("carte d'une forme nouvelle (champ inconnu) : refusée, jamais ignorée", A, 3, r"champ inconnu",
        valeur("principal.py", 31), "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n", carte_p=carte_inc)

    # Noms gelés (carte v2 annoncée) : liste fabriquée ici, depuis les zones et l'objet
    geles = []
    for zz in zones["zones"]:
        for e in zz["entrees"]:
            if e.get("fonction") == "<module>" and e["fichier"].endswith(".py"):
                arbre = ast.parse((objet / e["fichier"]).read_text(encoding="utf-8"))
                for st in arbre.body:
                    if isinstance(st, (ast.Assign, ast.AnnAssign)) and e["ligne_debut"] <= st.lineno <= e["ligne_fin"]:
                        for cible in (st.targets if isinstance(st, ast.Assign) else [st.target]):
                            if isinstance(cible, ast.Name) and cible.id not in [g["nom"] for g in geles]:
                                geles.append({"nom": cible.id, "fichier": e["fichier"], "zone": zz["id"]})
    gele = geles[0]["nom"]
    avec_geles = json.loads(json.dumps(carte))
    avec_geles["noms_geles"] = geles
    carte_geles = avec_compagnon(T / "cartes" / "carte-facteurs-noms-geles-essai.json", json.dumps(avec_geles))
    ligne31 = [st for st in ast.parse((objet / "principal.py").read_text(encoding="utf-8")).body if st.lineno == 31][0]
    avec_31 = json.loads(json.dumps(avec_geles))
    avec_31["noms_geles"] = geles + [{"nom": ligne31.targets[0].id, "fichier": "principal.py", "zone": "essai"}]
    carte_geles_31 = avec_compagnon(T / "cartes" / "carte-facteurs-noms-geles-l31-essai.json", json.dumps(avec_31))
    per_1932 = "- facteur : F02\n- lieu : principal.py, executer, l. 1932\n"
    banc.ecrire(f"noms gelés fabriqués pour l'essai : {len(geles)} noms affectés au niveau du module dans des lignes de "
                f"zone ; carte d'essai sha256 {sha(carte_geles)}")
    cas("noms gelés, cas sain : carte avec noms_geles ; la correction F02 saine est acceptée", S, 0, None,
        tous(valeur("principal.py", 31), accompagnement_sain), "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n"
                                                               + acc, carte_p=carte_geles)
    cas("noms gelés, cas sain : une ligne insérée (F02) lit un nom gelé sans le lier", S, 0, None,
        lambda c: inserer_apres(c, "principal.py", 1932, [f"_lecture_seule = {gele}"]), per_1932, carte_p=carte_geles)
    for texte, lignes_ in (
            ("affectation simple", [f"{gele} = 0"]),
            ("affectation augmentée", [f"{gele} += 0"]),
            ("affectation par :=", [f"_x = ({gele} := 0)"]),
            ("déclaration global", [f"global {gele}"]),
            ("setattr à nom constant", [f"setattr(sys.modules[__name__], \"{gele}\", 0)"]),
            ("del", [f"del {gele}"]),
            ("paramètre avec valeur par défaut", [f"def _essai_gele({gele}=0):", "    return 0"]),
            ("import qui masque", [f"from os import sep as {gele}"])):
        cas(f"noms gelés : ligne insérée dans F02 (l. 1932) — {texte}", A, 3, r"REFUS G5 \(noms gelés\) ",
            lambda c, l=lignes_: inserer_apres(c, "principal.py", 1932, l), per_1932, carte_p=carte_geles)
    cas("noms gelés : nom lié sur une ligne d'un facteur (l. 31), sa valeur changée sous ce facteur", A, 3,
        r"REFUS G5 \(noms gelés\) principal\.py, ligne 31 du nouveau fichier : affectation",
        valeur("principal.py", 31), "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n", carte_p=carte_geles_31)
    cas("noms gelés : ligne qui lie un nom gelé retirée (l. 31)", A, 3, r"REFUS G5 \(noms gelés\) .*retirée",
        lambda c: retirer_ligne(c, "principal.py", 31), "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n",
        carte_p=carte_geles_31)
    mauvais = json.loads(json.dumps(carte))
    mauvais["noms_geles"] = [{"nom": "nom gelé invalide"}]
    carte_mauvaise = avec_compagnon(T / "cartes" / "carte-facteurs-noms-geles-invalides.json", json.dumps(mauvais))
    cas("noms gelés : liste mal formée (pas un identifiant)", A, 3, r"carte incohérente .*noms_geles",
        valeur("principal.py", 31), "- facteur : F02\n- lieu : principal.py, <module>, l. 31\n", carte_p=carte_mauvaise)
    return corrige


# ---------------------------------------------------------------------------------------------------------------------
# G4


def pourcent_arrondi(v):
    """La valeur v en pourcentage, arrondie au dixième (moitié vers le haut), écrite avec un point."""
    return str((Decimal(v) * 100).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


def pourcent_exact(v):
    """La valeur v en pourcentage, sans arrondi, écrite avec un point."""
    return format((Decimal(v) * 100).normalize(), "f")


def marqueurs_synthetiques(rng, objet, n=4):
    """Valeurs synthétiques distinctives, absentes de l'objet (jamais écrites dans le journal)."""
    texte = "\n".join(p.read_text(encoding="utf-8") for p in objet.rglob("*") if p.is_file())
    res = []
    while len(res) < n:
        v = f"0.{rng.randrange(1000, 9999)}" if len(res) % 2 == 0 else f"0.0{rng.randrange(100, 499)}"
        if v not in texte and v.replace(".", ",") not in texte and v not in res:
            res.append(v)
    return res


def essais_g4(banc, travail, objet, corrige, carte, entrees, rng):
    T = travail / "g4"
    A_ = travail / "assemblage" / "base"
    pieces = [A_ / f"lecture-{DOSSIER_S}-test-v3.json", A_ / f"lecture-{DOSSIER_S}-test-v3.md",
              A_ / "releve-syn" / f"releve-mecanique-{DOSSIER_S}-v1.txt"]
    valeurs = marqueurs_synthetiques(rng, objet)
    marqueurs = avec_compagnon(T / "liste" / "marqueurs-essai-v1.txt",
                               "".join(f"{v} marqueur synthétique\n" for v in valeurs))
    comptes = {"n": 0}

    def arbre(changement):
        comptes["n"] += 1
        d = T / f"a{comptes['n']:03d}" / "copie-organisme"
        shutil.copytree(corrige, d)
        changement(d)
        return d

    def args(d, origine=objet, arbre_origine=ARBRE_OBJET, liste=marqueurs, empreinte=None, pieces_=pieces):
        a = ["--arbre", d, "--origine", origine, "--arbre-origine", arbre_origine, "--marqueurs", liste,
             "--empreinte-marqueurs", empreinte or sha(liste)]
        for p in pieces_:
            a += ["--piece-lecture", p]
        return a

    S, A = "sain", "artefact"
    banc.cas("G4", "cas sain : arbre corrigé du cas sain de G5 (F02 et accompagnement), marqueurs et pièces (A-test), "
                   "(B)", S, "G4", args(corrige), 0, r"empreinte d'arbre [0-9a-f]{64}")
    banc.cas("G4", "cas sain : arbre d'origine inchangé", S, "G4", args(objet), 0, rf"empreinte d'arbre {ARBRE_OBJET}")
    plantes = [
        ("fichier test_final synthétique planté (nom)", lambda d: ecrire(d / "donnees_test_final_essai.json", "{}\n"),
         r"nom interdit dans l'arbre \(nom de test_final\)"),
        ("fichier dont le contenu porte test_final", lambda d: ecrire(d / "notes_essai.txt", "part : test_final\n"),
         r"contenu interdit du § 14 \(nom de test_final\)"),
        ("fichier qui porte un marqueur", lambda d: ecrire(d / "tests" / "test_corrections_v6.py",
                                                           ESSAI_SAIN + f"\nSEUIL = {valeurs[0]}\n", mode="a"),
         r"porte le marqueur n° 1"),
        ("marqueur écrit en pourcentage, avec une virgule", lambda d: ecrire(
            d / "CORRECTIONS-v6.md", f"- Repère : {pourcent_exact(valeurs[0])} %\n".replace(".", ","), mode="a"),
         r"porte le marqueur n° 1"),
        ("copie d'une pièce de lecture (A-test)", lambda d: shutil.copyfile(pieces[0], d / "copie_essai.json"),
         r"copie d'une pièce de lecture"),
        ("chaîne tirée de (B) (empreinte de la liste fermée)", lambda d: ecrire(
            d / "CORRECTIONS-v6.md", "- Référence : " + [l for l in pieces[2].read_text(encoding="utf-8").split("\n")
                                                          if l.startswith("sources.liste_fermee =")][0].split(" = ")[1]
            + "\n", mode="a"), r"chaîne ou une valeur tirée de la pièce de lecture releve-mecanique"),
        ("ligne longue tirée de (A-test)", lambda d: ecrire(
            d / "CORRECTIONS-v6.md", "- Note : lecture synthétique des essais des gardes, part test (aucune donnée)\n",
            mode="a"), r"tirée de la pièce de lecture lecture-"),
        ("CORRECTIONS-v6.md qui cite une fiche", lambda d: ecrire(d / "CORRECTIONS-v6.md", "- Motif : " + "HC-P4" +
                                                                  "-03\n", mode="a"),
         r"contenu interdit du § 14 \(nom de fiche"),
        ("CORRECTIONS-v6.md qui cite un fait de course", lambda d: ecrire(
            d / "CORRECTIONS-v6.md", "- Contexte : la course S (essai synthétique)\n", mode="a"),
         r"contenu interdit du § 14 \(nom ou fait de course\)"),
        ("CORRECTIONS-v6.md qui cite un libellé du point 4 bis", lambda d: ecrire(
            d / "CORRECTIONS-v6.md", "- Libellé : dans le bruit des tâches\n", mode="a"),
         r"contenu interdit du § 14 \(libellé"),
        ("__pycache__ planté", lambda d: ecrire(d / "__pycache__" / "principal.cpython-313.pyc", "x\n"),
         r"fichier compilé"),
        ("fichier binaire planté", lambda d: (d / "donnees.bin").write_bytes(b"\x00\xff\xfe"), r"pas un texte UTF-8"),
        ("lien symbolique planté", lambda d: os.symlink("principal.py", d / "lien_essai.py"), r"lien symbolique"),
    ]
    for texte, changement, motif in plantes:
        banc.cas("G4", texte, A, "G4", args(arbre(changement)), 3, motif)
    banc.cas("G4", "arbre d'origine autre que celui attendu", A, "G4",
             args(corrige, arbre_origine=sha_texte("autre arbre")), 3, r"arbre d'origine : empreinte d'arbre")
    seuil = re.search(r"\d+\.\d+", entrees["F03.1"]["texte"]).group(0)
    mal = avec_compagnon(T / "liste-mal" / "marqueurs-mal-choisis-v1.txt", f"{seuil} marqueur mal choisi\n")
    banc.cas("G4", "marqueur mal choisi (valeur présente dans l'objet d'origine)", A, "G4", args(corrige, liste=mal), 3,
             r"déjà présent dans l'arbre d'origine")
    banc.cas("G4", "liste des marqueurs autre que celle empreintée", A, "G4",
             args(corrige, empreinte=sha_texte("autre liste")), 3, r"liste des marqueurs : empreinte différente")
    tf = avec_compagnon(T / "tf" / f"lecture-{DOSSIER_S}-test-final-holm-quatre-v3.json", "octets synthétiques\n")
    banc.cas("G4", "usage : pièce test_final donnée (jamais ouverte)", A, "G4", args(corrige, pieces_=pieces + [tf]), 2,
             r"USAGE G4 : .*jamais ouvert")


# ---------------------------------------------------------------------------------------------------------------------
# G6


def essais_g6(banc, travail):
    T = travail / "g6"
    comptes = {"n": 0}
    autres_m = [COURSE_M, DOSSIER_M, LIGNEE_M, CLE_M]
    autres_s = [COURSE_S, DOSSIER_S, LIGNEE_S, CLE_S]

    def piece(texte):
        comptes["n"] += 1
        return avec_compagnon(T / f"p{comptes['n']:03d}" / "verdicts-essai-v1.md",
                              "# Pièce synthétique des essais de G6 (aucun verdict réel)\n\n" + texte)

    def args(p, autres, preseance=False):
        a = ["--piece", p]
        for n in autres:
            a += ["--autre", n]
        return a + (["--autoriser-preseance"] if preseance else [])

    h = sha_texte("pièce de correction synthétique")
    preseance = (f"Condition de préséance : la pièce correction-{DOSSIER_M}-ronde-1-v1.md (empreinte {h}), du dossier "
                 f"{DOSSIER_M}, établit qu'aucune fiche de la course M ne motive de correction ; la partie B de M l'a "
                 f"vérifié\n")
    S, A = "sain", "artefact"
    corps_s = (f"- course : {COURSE_S} ; dossier : {DOSSIER_S}\n- identite.lignee = {LIGNEE_S} (clé {CLE_S})\n"
               f"- fichier lu : lecture-{DOSSIER_S}-test-v3.md\n")
    banc.cas("G6", "cas sain : pièce de S qui porte gemini-organisme-v6-2-s et v6-2-s (pas une mention de M, mots "
                   "entiers)", S, "G6", args(piece(corps_s), autres_m), 0)
    banc.cas("G6", "cas sain : pièce de correction de S, ligne « condition de préséance » qui nomme M", S, "G6",
             args(piece(corps_s + preseance), autres_m, True), 0)
    banc.cas("G6", "cas sain : pièce de M qui porte gemini-organisme-v6-2 et v6-2", S, "G6",
             args(piece(f"- course : {COURSE_M} ; dossier : {DOSSIER_M}\n- identite.lignee = {LIGNEE_M} (clé {CLE_M})\n"),
                  autres_s), 0)
    banc.cas("G6", "limite documentée (mots entiers, protocole v4) : nom de dossier de M collé dans un nom de fichier, "
                   "non compté ; au contre-lecteur", "limite", "G6",
             args(piece(corps_s + f"- fichier cité : lecture-{DOSSIER_M}-test-v3.md\n"), autres_m), 0)
    for texte, corps, autres, pre, motif in (
            ("pièce de S qui porte la lignée de M (gemini-organisme-v6-2, mot entier)",
             corps_s + f"- lignée de l'autre course : {LIGNEE_M}\n", autres_m, False, rf"« {LIGNEE_M} »"),
            ("pièce de S qui porte le nom de course de M", corps_s + f"- à côté de {COURSE_M}\n", autres_m, False,
             rf"« {COURSE_M} »"),
            ("pièce de S qui porte la clé de M (v6-2, mot entier)", corps_s + f"- clé {CLE_M}\n", autres_m, False,
             rf"« {CLE_M} »"),
            ("pièce de M qui porte le nom de dossier de S", f"- course : {COURSE_M}\n- voir {DOSSIER_S}\n", autres_s,
             False, rf"« {DOSSIER_S} »"),
            ("différence M − S", corps_s + "- écart M − S : sans objet\n", autres_m, False, r"différence entre"),
            ("ligne « condition de préséance » qui porte une fiche", corps_s + preseance.replace(
                "aucune fiche", "aucune fiche (" + "HC-P4" + "-03)"), autres_m, True, r"porte une fiche"),
            ("ligne « condition de préséance » qui porte un verdict", corps_s + preseance.replace(
                "vérifié", "vérifié, fiche tenue"), autres_m, True, r"porte un verdict"),
            ("ligne « condition de préséance » dans une pièce de verdicts (option absente)", corps_s + preseance,
             autres_m, False, rf"hors de la ligne « condition de préséance »"),
            ("deux lignes « condition de préséance »", corps_s + preseance + preseance, autres_m, True,
             r"2 lignes « condition de préséance »")):
        banc.cas("G6", texte, A, "G6", args(piece(corps), autres, pre), 3, motif)


# ---------------------------------------------------------------------------------------------------------------------
# G8


def essais_g8(banc, travail, rng):
    T = travail / "g8"
    score = f"0.{rng.randrange(5500, 9500)}"
    p = f"0.0{rng.randrange(101, 499)}"
    compte = str(rng.randrange(11, 35))
    while compte in ("12",):
        compte = str(rng.randrange(11, 35))
    valeurs = avec_compagnon(T / "liste" / "valeurs-essai-v1.txt",
                             f"# marqueurs synthétiques d'un dossier d'audit d'essai\n{score} score\n{p} p\n"
                             f"{compte} compte\n")
    comptes = {"n": 0}

    def piece(texte, nom="lecture-finale-essai-v1.md"):
        comptes["n"] += 1
        return avec_compagnon(T / f"p{comptes['n']:03d}" / nom, "# Pièce synthétique des essais de G8\n\n" + texte)

    sain = ("- cellule (course de l'essai, conscience d'évaluation, test_final, génération 3) : « dans le bruit des "
            "tâches »\n- HC-P4-11 : non rejetée (bruit) ; HC-P4-12 : cellule (iii), libellé recopié\n"
            "- correction : Holm, quatre tests, niveau 0,05\n")

    def args(pieces, liste=valeurs, empreinte=None):
        a = ["--valeurs", liste, "--empreinte-valeurs", empreinte or sha(liste)]
        for x in pieces:
            a += ["--piece", x]
        return a

    S, A = "sain", "artefact"
    banc.cas("G8", "cas sain : pièce qui cite les cellules de test_final par coordonnées et libellés", S, "G8",
             args([piece(sain)]), 0)
    for texte, ajout, motif in (
            ("valeur marqueur d'un score recopiée", f"- score : {score}\n", r"valeur n° 1 de la liste"),
            ("valeur p marqueur recopiée avec une virgule", f"- p : {p.replace('.', ',')}\n", r"valeur n° 2 de la liste"),
            ("score marqueur recopié en pourcentage arrondi", f"- part : {pourcent_arrondi(score)} %\n",
             r"valeur n° 1 de la liste"),
            ("compte marqueur recopié (nombre court : signalé peu distinctif)", f"- tâches : {compte}\n",
             r"valeur n° 3 de la liste.*peu distinctive")):
        banc.cas("G8", texte, A, "G8", args([piece(sain + ajout)]), 3, motif)
    faux = avec_compagnon(T / "liste-faux" / "valeurs-essai-v1.txt", f"{score} score\n")
    ecrire(faux.with_name(faux.name + ".sha256"), f"{sha_texte('autre')}  {faux.name}\n", mode="w")
    banc.cas("G8", "liste des valeurs dont le compagnon ne correspond pas", A, "G8", args([piece(sain)], liste=faux), 3,
             r"compagnon de liste des valeurs")
    banc.cas("G8", "liste des valeurs autre que celle empreintée", A, "G8",
             args([piece(sain)], empreinte=sha_texte("autre liste")), 3, r"empreinte différente de celle")
    vide = avec_compagnon(T / "liste-vide" / "valeurs-essai-v1.txt", "# aucune valeur\n")
    banc.cas("G8", "liste des valeurs vide (aucun repli silencieux)", A, "G8", args([piece(sain)], liste=vide), 3,
             r"liste des valeurs vide")
    tf = piece("octets synthétiques\n", nom=f"lecture-{DOSSIER_S}-test-final-holm-quatre-v3.md")
    banc.cas("G8", "usage : fichier test_final donné comme pièce (jamais ouvert)", A, "G8", args([tf]), 2,
             r"USAGE G8 : .*jamais ouvert")


# ---------------------------------------------------------------------------------------------------------------------
# G9


def essais_g9(banc, travail, rng):
    T = travail / "g9"
    decimal_1 = f"0,{rng.randrange(10, 99)}"
    decimal_2 = f"{rng.randrange(1, 9)},{rng.randrange(1, 9)}"
    comptes = {"n": 0}
    tete = f"### Entrée 7 — lancement de la relance synthétique de l'essai de G9 — {heure()}\n"
    ident = (f"- objet : arbre {sha_texte('objet corrigé synthétique')}, 26 fichiers ; graine 123 (illustratif) ; "
             f"question s\n")
    tf = "- test_final : « aucune attente au-delà des nulles HC-P4-11 et 12 »\n"

    def entree(texte, nom="entree-lancement-essai-v1.md"):
        comptes["n"] += 1
        return avec_compagnon(T / f"e{comptes['n']:03d}" / nom, texte)

    S, A = "sain", "artefact"
    sain = ("- attente chiffrée : HC-P4-03 : au moins un successeur valide ayant tourné, nombre attendu ≥ 1 ; "
            "HC-P4-01 : conception.declaration.ronde ≥ 3\n")
    banc.cas("G9", "cas sain : entrée qui nomme la fiche visée, l'observation mécanique et son nombre", S, "G9",
             ["--entree", entree(tete + ident + sain + tf)], 0)
    sous = ("- attente chiffrée :\n  - HC-P4-07 : coût d'une ronde de conception ≤ 3,00 USD\n"
            "  - HC-P4-09 : unite.c001.appels.total ≥ 1\n")
    banc.cas("G9", "cas sain : attentes en sous-éléments, un montant avec son unité", S, "G9",
             ["--entree", entree(tete + ident + sous + tf)], 0)
    journal = entree("# Journal synthétique de l'essai de G9\n\n### Entrée 6 — dossier synthétique, ronde 1 — "
                     f"{heure()}\n- objet : synthétique\n\n" + tete + ident + sain + tf + "\n### Entrée 8 — clôture\n",
                     nom="journal-essais-boucle-essai-v1.md")
    banc.cas("G9", "cas sain : entrée n° 7 lue dans un journal", S, "G9", ["--journal", journal, "--numero", "7"], 0)
    for texte, attente, motif, avec_tf in (
            ("entrée sans nombre", "- attente chiffrée : HC-P4-03 : au moins un successeur valide ayant tourné\n",
             r"aucun nombre attendu", True),
            ("attente qui est un score", f"- attente chiffrée : HC-P4-08 : exactitude de test ≥ {decimal_1}\n",
             r"l'attente est un score", True),
            ("attente sur une fiche de test_final", "- attente chiffrée : HC-P4-11 : rejet ≥ 1\n",
             r"HC-P4-11 ou 12", True),
            ("nombre décimal sans unité", f"- attente chiffrée : HC-P4-07 : durée moyenne ≤ {decimal_2}\n",
             r"décimal sans unité", True),
            ("fiche dont aucune branche ne propose de correction", "- attente chiffrée : HC-P4-05 : memoire.g001 ≥ 1\n",
             r"aucune branche ne propose", True),
            ("ligne test_final absente", sain, r"aucune ligne « test_final", False),
            ("aucune ligne « attente chiffrée : »", "- attente : à préciser\n", r"entrée sans attente chiffrée", True)):
        banc.cas("G9", texte, A, "G9", ["--entree", entree(tete + ident + attente + (tf if avec_tf else ""))], 3, motif)
    banc.cas("G9", "entrée du journal qui n'est pas une entrée de lancement", A, "G9",
             ["--journal", journal, "--numero", "6"], 3, r"pas une entrée de lancement")


if __name__ == "__main__":
    principal()
