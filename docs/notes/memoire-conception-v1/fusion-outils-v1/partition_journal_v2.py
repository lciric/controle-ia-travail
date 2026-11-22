"""Partition du journal des idées et extrait commun, version 2 (22 novembre 2026).

Pièce d'instrument (classe B), session bibliothécaire (Claude Opus 5.5). Version 2 après la contre-lecture de la v1
(contre-lecture-outils-fusion-v1-v1.md) : C1 la source doit être un fichier ordinaire (blob) ; C2 `nom` chaîne, `mots`
liste de chaînes, sinon « mère » ; C3 garde des noms élargie (dossiers et branches exclus du § 2.1) ; C4 toute erreur sur un
événement le range en « mère », sans arrêter le programme ; C5 valeurs fermées (chemin normalisé, états et événements de
la liste fermée, champs textuels en chaînes de 300 signes au plus) ; C6 identifiants de fiche `[GIP]-NNNN`, marques
normalisées ; C7 commit ancêtre de la branche principale ; remarque 2 : plus de dérogation par variable d'environnement ;
remarque 3 : nom de sortie imposé, empreinte écrite d'abord dans un fichier temporaire ; remarque 4 : comptes cohérents ;
remarque 5 : extrait de 6 mots et 30 signes au moins, sur frontières de mot ; remarque 6 : l'en-tête du rapport rappelle
que l'état commun peut être périmé ; remarque 7 : les journaux sont lus en entier avant le classement (l'ordre des
fichiers ne compte plus).

Un événement est « commune » si et seulement si : 1. source stricte (listes_lecture_v2.autorise_stricte) ; 2. extrait
retrouvé mot pour mot dans un blob, au commit cité, ancêtre de la branche principale ; 3. la fiche a une naissance, et
toutes ses naissances sont communes ; 4. la fiche n'est pas marquée « mère » ; 5. nom et mots sans nom exclu ; 6. valeurs
fermées. Sinon « mère ». Dans le doute, « mère ».
Usage : python -I partition_journal_v2.py JOURNAL.jsonl [JOURNAL2.jsonl …] --horodatage AAAA-MM-JJTHHMMZ
        [--marquees F] [--depot .] [--ref-principale REF]
La sortie est `registres/veille-de-cap/commune/journal-commun-<horodatage>.jsonl` (sous --depot), avec son compagnon.
"""
import argparse
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("ll2", os.path.join(ICI, "listes_lecture_v2.py"))
ll2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ll2)

CHAMPS_COMMUNS = ("quand", "fiche", "evenement", "nom", "etat", "source", "sert", "issue", "raison", "reveil", "mots",
                  "partition")
CHAMPS_SOURCE = ("chemin", "commit", "repere", "extrait")
RAISONS = ("réfutée", "occupée", "trop chère", "remplacée", "hors cap", "risque", "mot du directeur")
ETATS = ("proposée", "retenue", "en préparation", "à l'essai", "essai non évaluable", "testée, non concluant",
         "testée, verdict valide", "intégrée au programme", "gardée de côté", "abandonnée", "fusionnée dans")
EVENEMENTS = ("naissance", "etat", "état", "essai", "signal", "decision", "décision", "fusion", "note")
ISSUES = ("jamais parti", "non évaluable", "non concluant", "verdict valide")
RX_FICHE = re.compile(r"[GIP]-\d{4}")
MOTS_INTERDITS = tuple(ll2.vc6.EXCLUS_MOTS) + (
    "ne-pas-lire", "transcription", "archives-reponses-modeles", "quarantaine", "matiere-premiere", "lot/compte-4",
    "compte-4-v1", "sauvegarde/", "ii-b-saboteur", "bras-attaque-oracle", "prep/quarantaine", "reponse-24", "demande-24")
TEXTE_MAX = 300


class Rejet(Exception):
    pass


def git(depot, *args):
    return subprocess.run(["git", "-C", depot, *args], capture_output=True, text=True)


class Depot:
    def __init__(self, depot, ref):
        self.depot = depot
        self.ref = ref
        self.commits = {}
        self.textes = {}

    def resoudre(self, commit):
        if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{7,40}", commit):
            raise Rejet("commit mal formé")
        if commit not in self.commits:
            sha = None
            r = git(self.depot, "rev-parse", "--verify", "--quiet", f"{commit}^{{commit}}")
            if r.returncode == 0 and re.fullmatch(r"[0-9a-f]{40}", r.stdout.strip()):
                sha = r.stdout.strip()
                refs = [self.ref] if self.ref else ["origin/main", "main"]
                ref = next((x for x in refs if git(self.depot, "rev-parse", "--verify", "--quiet", x).returncode == 0),
                           None)
                if ref is None or git(self.depot, "merge-base", "--is-ancestor", sha, ref).returncode != 0:
                    sha = "hors-principale"
            self.commits[commit] = sha
        sha = self.commits[commit]
        if sha is None:
            raise Rejet("commit introuvable")
        if sha == "hors-principale":
            raise Rejet("commit hors de la branche principale")
        return sha

    def texte(self, sha, chemin):
        cle = (sha, chemin)
        if cle not in self.textes:
            t = None
            g = git(self.depot, "cat-file", "-t", f"{sha}:{chemin}")
            if g.returncode == 0 and g.stdout.strip() == "blob":
                m = git(self.depot, "ls-tree", sha, "--", chemin)
                if m.returncode == 0 and m.stdout.split(" ", 1)[0] in ("100644", "100755"):
                    b = subprocess.run(["git", "-C", self.depot, "show", f"{sha}:{chemin}"], capture_output=True)
                    if b.returncode == 0:
                        t = ll2.vc6.normaliser_texte(b.stdout.decode("utf-8", "replace"))
            self.textes[cle] = t
        if self.textes[cle] is None:
            raise Rejet("source absente ou qui n'est pas un fichier ordinaire")
        return self.textes[cle]


def texte_ferme(v, nom_champ, nul_admis=True):
    if v is None and nul_admis:
        return None
    if not isinstance(v, str) or len(v) > TEXTE_MAX:
        raise Rejet(f"champ {nom_champ} : chaîne de {TEXTE_MAX} signes au plus attendue")
    return v


def examiner(ev, d):
    """Rend l'événement réduit si « commune », sinon lève Rejet."""
    if not isinstance(ev, dict):
        raise Rejet("ligne illisible")
    fiche = ev.get("fiche")
    if not isinstance(fiche, str) or not RX_FICHE.fullmatch(fiche):
        raise Rejet("identifiant de fiche mal formé")
    nom = texte_ferme(ev.get("nom"), "nom", nul_admis=False)
    mots = ev.get("mots")
    if not isinstance(mots, list) or not all(isinstance(m, str) and len(m) <= 60 for m in mots) or len(mots) > 8:
        raise Rejet("mots : liste de chaînes attendue")
    bas = ll2.sans_accents(" ".join([nom] + mots)).lower()
    if any(m in bas for m in MOTS_INTERDITS):
        raise Rejet("nom exclu dans nom ou mots")
    if ev.get("evenement") not in EVENEMENTS:
        raise Rejet("événement hors liste fermée")
    if ev.get("etat") not in ETATS:
        raise Rejet("état hors liste fermée")
    if ev.get("issue") not in ISSUES + (None,):
        raise Rejet("issue hors liste fermée")
    src = ev.get("source")
    if not isinstance(src, dict):
        raise Rejet("source absente")
    brut = src.get("chemin")
    if not isinstance(brut, str):
        raise Rejet("chemin mal formé")
    chemin = ll2.normaliser_chemin(brut)
    if not ll2.autorise_stricte(chemin)[0]:
        raise Rejet("source hors liste stricte")
    sha = d.resoudre(src.get("commit"))
    texte = d.texte(sha, chemin)
    ext = ll2.vc6.normaliser_texte(texte_ferme(src.get("extrait"), "extrait", nul_admis=False))
    if len(ext.split(" ")) < 6 or len(ext) < 30:
        raise Rejet("extrait trop court (6 mots et 30 signes au moins)")
    if not re.search(r"(?<!\w)" + re.escape(ext) + r"(?!\w)", texte):
        raise Rejet("extrait introuvable mot pour mot")
    return {
        "quand": texte_ferme(ev.get("quand"), "quand"), "fiche": fiche, "evenement": ev["evenement"], "nom": nom,
        "etat": ev["etat"],
        "source": {"chemin": chemin, "commit": sha, "repere": texte_ferme(src.get("repere"), "repere"), "extrait": ext},
        "sert": texte_ferme(ev.get("sert"), "sert"), "issue": ev.get("issue"),
        "raison": ev.get("raison") if ev.get("raison") in RAISONS else None,
        "reveil": texte_ferme(ev.get("reveil"), "reveil"), "mots": mots, "partition": "commune"}


def partitionner(evenements, depot, marquees=(), ref=None):
    """evenements : liste de dict (ou None pour une ligne illisible). Rend (communs réduits, comptes)."""
    d = Depot(depot, ref)
    marq = {str(m).strip().upper() for m in marquees}
    examines = []
    for ev in evenements:
        try:
            examines.append((ev, examiner(ev, d), None))
        except Rejet as e:
            examines.append((ev, None, str(e)))
        except Exception as e:                       # C4 : jamais d'arrêt sur un événement
            examines.append((ev, None, f"erreur {type(e).__name__}"))
    nees_communes, nees_meres = set(), set()
    for ev, r, _ in examines:
        if isinstance(ev, dict) and ev.get("evenement") == "naissance" and isinstance(ev.get("fiche"), str):
            (nees_communes if r is not None else nees_meres).add(ev["fiche"].strip().upper())
    sortie, motifs = [], {}
    for ev, r, motif in examines:
        if r is not None:
            f = r["fiche"].upper()
            if f not in nees_communes or f in nees_meres:
                r, motif = None, "fiche sans naissance commune, ou avec une naissance « mère »"
            elif f in marq:
                r, motif = None, "fiche marquée par la mère"
        if r is None:
            motifs[motif] = motifs.get(motif, 0) + 1
        else:
            sortie.append(r)
    comptes = {"lignes": len(evenements), "commune": len(sortie), "mere": len(evenements) - len(sortie),
               "motifs": motifs,
               "avertissement": "l'état d'une fiche dans l'extrait commun peut être périmé : un événement plus récent "
                                "peut être dans la partition « mère »"}
    return sortie, comptes


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("journaux", nargs="+")
    p.add_argument("--horodatage", required=True)
    p.add_argument("--marquees", default=None)
    p.add_argument("--depot", default=".")
    p.add_argument("--ref-principale", dest="ref_principale", default=None)
    a = p.parse_args(argv)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{4}Z", a.horodatage):
        print("ARRET : --horodatage AAAA-MM-JJTHHMMZ attendu", file=sys.stderr)
        return 1
    rel = f"{ll2.VEILLE_COMMUNE}journal-commun-{a.horodatage}.jsonl"
    sortie_chemin = os.path.join(a.depot, rel)
    if os.path.lexists(sortie_chemin) or os.path.lexists(sortie_chemin + ".sha256"):
        print(f"ARRET : {rel} existe déjà (R12)", file=sys.stderr)
        return 1
    marquees = set()
    if a.marquees:
        marquees = {l.strip() for l in open(a.marquees, encoding="utf-8") if l.strip()}
    evs = []
    for j in a.journaux:
        for l in open(j, encoding="utf-8-sig"):
            if not l.strip():
                continue
            try:
                evs.append(json.loads(l))
            except ValueError:
                evs.append(None)
    sortie, comptes = partitionner(evs, a.depot, marquees, a.ref_principale)
    os.makedirs(os.path.dirname(sortie_chemin), exist_ok=True)
    corps = "".join(json.dumps(e, ensure_ascii=False) + "\n" for e in sortie).encode("utf-8")
    h = hashlib.sha256(corps).hexdigest()
    tmp = sortie_chemin + ".en-cours"
    with open(tmp, "xb") as f:
        f.write(corps)
    with open(sortie_chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {os.path.basename(sortie_chemin)}\n")
    os.rename(tmp, sortie_chemin)
    print(json.dumps(comptes, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
