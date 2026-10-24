"""La boucle externe du noyau : amorcer, exécuter une génération, juger, archiver, relancer le successeur.

Le noyau n'impose aucune organisation ni aucune règle de sélection ; il tient ce que l'essaim ne peut pas tenir
lui-même : les clés et le journal (couche d'appel), le juge (tâches cachées), le bac à sable, l'archive, les bornes
de l'humain (générations, budget, temps), et l'arrêt sur ordre (fichier `STOP` dans le dossier du run).
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import pathlib
import platform
import shutil
import sys

import numpy as np

from . import archive as _archive, bac_a_sable, contrat, recherche as _recherche, taches as _taches
from .appels import EMPREINTE_COLLISIONNEUR_V25, Appelant, Arret, cv
from .serveur import PARALLELE_MAX_DEFAUT, ServeurAppels

FAMILLES_CONNUES = sorted(set(contrat.FAMILLES.values()))


def _heure() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def commit_git(dossier: pathlib.Path) -> str | None:
    """Commit du code (lecture seule, aucune autre commande git) ; None hors dépôt."""
    import subprocess
    try:
        r = subprocess.run(["git", "-C", str(dossier), "rev-parse", "HEAD"], capture_output=True, text=True, timeout=10)
        return r.stdout.strip() if r.returncode == 0 else None
    except (OSError, subprocess.SubprocessError):
        return None


USAGES_GRAINE = {"ordre_train": 1, "ordre_test": 2, "recherche": 3, "defense": 4, "organisme": 5, "ordre_lignees": 6}
INDICE_RONDE = 1_000_000  # indice de lignée réservé aux tirages de ronde (ordre des lignées), hors de toute lignée réelle


def empreinte_arbre(dossier: pathlib.Path) -> str:
    """Empreinte d'un dossier : chemins relatifs triés et contenu de chaque fichier (indépendante des dates)."""
    h = hashlib.sha256()
    for f in sorted(p for p in pathlib.Path(dossier).rglob("*") if p.is_file()):
        h.update(str(f.relative_to(dossier)).encode("utf-8") + b"\0")
        h.update(hashlib.sha256(f.read_bytes()).hexdigest().encode("ascii") + b"\n")
    return h.hexdigest()


def organismes_g000(course: str | pathlib.Path, destination: str | pathlib.Path) -> dict[str, dict]:
    """Les organismes de génération 0 archivés d'une course (mêmes empreintes), extraits sous `destination/<lignée>/`,
    pour le bras gelé apparié (CR-08) : {lignée: {"organisme": dossier, "famille": …, "empreinte_organisme": …}}."""
    import tarfile
    course, destination = pathlib.Path(course), pathlib.Path(destination)
    index = course / "archive" / "index.jsonl"
    if not index.exists():
        raise Arret(f"course sans archive : {index}")
    lignes = [json.loads(l) for l in index.read_text(encoding="utf-8").splitlines() if l.strip()]
    manifeste = json.loads((course / "manifeste-run.json").read_text(encoding="utf-8")) if (course / "manifeste-run.json").exists() else {}
    sortie = {}
    for l in lignes:
        if l["generation"] != 0 or l["lignee"] in sortie:
            continue
        tar = course / "archive" / l["chemin"] / "organisme.tar.gz"
        cible = destination / l["lignee"]
        if cible.exists():
            shutil.rmtree(cible)
        cible.mkdir(parents=True)
        with tarfile.open(tar, "r:gz") as t:
            membres = [m for m in t.getmembers() if m.isfile() and m.name.startswith("organisme/") and ".." not in m.name]
            t.extractall(cible, members=membres, filter="data")
        famille = l.get("famille")
        if not famille:  # courses antérieures : famille de l'espèce d'amorçage, par le nom de la lignée
            for e in manifeste.get("especes_amorcage", []):
                if e.lower().replace("_", "-") == l["lignee"]:
                    famille = contrat.FAMILLES[e]
        sortie[l["lignee"]] = {"organisme": str(cible / "organisme"), "famille": famille or "gemini",
                               "empreinte_organisme": l.get("empreinte_organisme"), "course_origine": str(course)}
    if not sortie:
        raise Arret(f"aucune génération 0 archivée dans {course}")
    return sortie


class Noyau:
    @classmethod
    def recharger(cls, course: str | pathlib.Path, appelants: dict | None = None, reel: bool = False, go_id: str | None = None,
                  registre_go: str | pathlib.Path | None = None, isoler_reseau: bool | None = None):
        """Recharge une course finie (manifeste, banque, mission, lignées de l'archive) pour une confrontation séparée
        (CR-04) : rien de la course n'est réécrit ; les dépenses nouvelles s'ajoutent au plafond restant."""
        course = pathlib.Path(course)
        m = json.loads((course / "manifeste-run.json").read_text(encoding="utf-8"))
        banque = json.loads((course / "banque.json").read_text(encoding="utf-8"))
        mission = (course / "mission.txt").read_text(encoding="utf-8") if (course / "mission.txt").exists() else ""
        n = cls(course, mission, banque, m["budget_generation"], m["plafond_total_usd"], m["generations_max"], appelants=appelants,
                reel=reel, go_id=go_id or m.get("go_id"), isoler_reseau=(m.get("isolation_reseau", False) if isoler_reseau is None else isoler_reseau),
                entropie=m["entropie_seed_sequence"], especes_amorcage=m.get("especes_amorcage"), etiquette_run=m.get("run", ""),
                gel=m.get("gel", False), parallele_max=m.get("parallele_max", PARALLELE_MAX_DEFAUT), registre_go=registre_go,
                memoire_partagee=m.get("memoire_partagee", False))
        lignes = n.archive.lignes()
        depense = 0.0
        for l in lignes:
            depense += float(l.get("cout_usd") or 0.0)
            nom = l["lignee"]
            espece = next((e for e in m.get("especes_amorcage", []) if e.lower().replace("_", "-") == nom), None)
            n.lignees[nom] = {"espece_amorcage": espece, "famille": l.get("famille") or (contrat.FAMILLES[espece] if espece else None),
                              "generation": l["generation"], "organisme": None, "active": False, "impose": bool(l.get("impose")),
                              "uid": (bac_a_sable.uid_lignee(len(n.lignees)) if n.isolation["utilisateur"] and nom not in n.lignees else n.lignees.get(nom, {}).get("uid"))}
        n.depense_totale = depense
        n._evenement(etape="rechargement", lignees=sorted(n.lignees), depense_relue_usd=round(depense, 4))
        return n

    def __init__(self, racine: str | pathlib.Path, mission: str, banque: dict, budget_generation: dict,
                 plafond_total_usd: float, generations_max: int, appelants: dict | None = None, reel: bool = False,
                 go_id: str | None = None, isoler_reseau: bool = False, entropie: int | None = None,
                 especes_amorcage: list[str] | None = None, etiquette_run: str = "", gel: bool = False,
                 organismes_imposes: dict[str, dict] | None = None, parallele_max: int = PARALLELE_MAX_DEFAUT,
                 recherche=None, relances_max: int = 1, registre_go: str | pathlib.Path | None = None,
                 memoire_partagee: bool = False):
        """`organismes_imposes` : {nom de lignée: {"organisme": dossier `organisme/` déjà écrit, "famille": "anthropic"|"gemini"}}
        — lignées dont la génération 0 n'est pas écrite par une espèce mais fournie (par exemple l'essaim de Gemini
        corrigé, mis sous contrat), pour les comparer sous le même noyau, les mêmes tâches et les mêmes bornes que les
        lignées auto-écrites. La famille déclarée sert à la confrontation entre familles."""
        self.racine = pathlib.Path(racine)
        self.racine.mkdir(parents=True, exist_ok=True)
        # CR-01 : isolation d'utilisateur quand le noyau est root ; la racine est traversable (0711) mais ses dossiers
        # sensibles (banque, archive, lignées, journaux) restent à root en 0700 ; chaque lignée a son propre utilisateur
        self.isolation = bac_a_sable.capacites_isolation()
        bac_a_sable.proteger(self.racine, 0o711)
        for sous in ("lignees", "confrontation"):
            (self.racine / sous).mkdir(exist_ok=True)
            bac_a_sable.proteger(self.racine / sous, 0o700)
        # les dossiers de travail des organismes et la vue de l'archive doivent être atteignables par leurs utilisateurs
        self.espace = bac_a_sable.espace_organismes(self.racine) if self.isolation["utilisateur"] else self.racine
        (self.espace / "travail").mkdir(exist_ok=True)
        bac_a_sable.proteger(self.espace / "travail", 0o711)
        self.mission = mission
        self.banque = banque
        self.budget = dict(budget_generation)
        self.plafond_total = float(plafond_total_usd)
        self.generations_max = int(generations_max)
        self.appelants = appelants
        self.reel, self.go_id, self.isoler_reseau = bool(reel), go_id, bool(isoler_reseau)
        self.especes_amorcage = list(contrat.ESPECES_DISPONIBLES if especes_amorcage is None else especes_amorcage)  # [] : aucune lignée auto-écrite (bras gelé apparié)
        self.gel = bool(gel)  # bras témoin : la génération 0 est relancée, le successeur est ignoré
        self.organismes_imposes = dict(organismes_imposes or {})
        self.parallele_max = max(1, int(parallele_max))
        # recherche documentaire servie par le noyau (nœud 1, option (b)) : `recherche` est la fabrique du moteur
        # (double en simulation ; None en réel = arXiv) ; `budget['recherches_max']` = 0 la coupe
        self.recherche = recherche
        self.budget.setdefault("recherches_max", 0)
        # successeur invalide : relance de la dernière génération valide, `relances_max` fois de suite (nœud 2, (b))
        self.relances_max = max(0, int(relances_max))
        # CR-15 (c) : par défaut chaque lignée ne lit que sa propre archive (lignées indépendantes) ; avec
        # `memoire_partagee`, la vue de toutes les lignées est lisible, figée au début de chaque ronde (CR-15 b)
        self.memoire_partagee = bool(memoire_partagee)
        self.ronde = 0
        self.vue_ronde: pathlib.Path | None = None
        for nom, spec in self.organismes_imposes.items():
            if not isinstance(spec, dict) or "organisme" not in spec or spec.get("famille") not in FAMILLES_CONNUES:
                raise Arret(f"organisme imposé {nom!r} : il faut {{'organisme': dossier, 'famille': {FAMILLES_CONNUES}}}")
            if nom in {e.lower().replace("_", "-") for e in self.especes_amorcage}:
                raise Arret(f"organisme imposé {nom!r} : nom déjà pris par une lignée auto-écrite")
        self.banque.setdefault("test_final", [])
        self.archive = _archive.Archive(self.racine / "archive", vue=self.espace / "archive_vue")
        self.depense_totale = 0.0
        self.n_appels_total = 0
        self.lignees: dict[str, dict] = {}
        self.evenements: list[dict] = []
        self.graines = np.random.SeedSequence(entropie)
        self.manifeste = {
            "run": etiquette_run or self.racine.name, "debut_utc": _heure(), "reel": self.reel, "go_id": go_id,
            "entropie_seed_sequence": int(self.graines.entropy), "python": sys.version.split()[0], "numpy": np.__version__,
            "plateforme": platform.platform(), "collisionneur_v25_empreinte": getattr(cv, "__empreinte_fichier__", None),
            "budget_generation": self.budget, "plafond_total_usd": self.plafond_total, "generations_max": self.generations_max,
            "isolation_reseau": self.isoler_reseau, "gel": self.gel, "n_taches_entrainement": len(banque["train"]),
            "n_taches_test_dev": len(banque["test"]), "n_taches_test_final": len(banque.get("test_final", [])),
            "mission_sha256": hashlib.sha256(mission.encode("utf-8")).hexdigest(),
            "parallele_max": self.parallele_max, "especes_amorcage": self.especes_amorcage, "relances_max": self.relances_max,
            "memoire_partagee": self.memoire_partagee,
            "recherche": ("simulation" if self.recherche is not None else ("arxiv" if self.budget["recherches_max"] > 0 else "aucune")),
            "organismes_imposes": {nom: {"source": str(spec["organisme"]), "famille": spec["famille"],
                                         "empreinte_arbre": (empreinte_arbre(pathlib.Path(spec["organisme"])) if pathlib.Path(spec["organisme"]).is_dir() else None)}
                                   for nom, spec in self.organismes_imposes.items()},
        }
        self.manifeste["isolation"] = dict(self.isolation)
        self.manifeste["espace_organismes"] = str(self.espace)
        code = pathlib.Path(__file__).resolve().parent.parent  # essaim_m3/
        self.manifeste["commit"] = commit_git(code)
        self.manifeste["sha256_code_noyau"] = empreinte_arbre(code / "noyau")
        self.manifeste["sha256_banque"] = hashlib.sha256(json.dumps(self.banque, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
        self.manifeste["collisionneur_conforme"] = (getattr(cv, "__empreinte_fichier__", None) == EMPREINTE_COLLISIONNEUR_V25)
        if self.reel:
            if not self.go_id:
                raise Arret("mode réel sans GO : refusé")
            if not self.manifeste["collisionneur_conforme"]:  # CR-13 (d) : table des prix et appelants vérifiés
                raise Arret(f"mode réel : collisionneur v2.5 d'empreinte inattendue ({getattr(cv, '__empreinte_fichier__', None)}) ; refusé")
            if registre_go is None:
                raise Arret("mode réel : extrait de registres/go.md (--registre-go) exigé pour vérifier l'identifiant de GO (CR-13 g)")
            texte_go = pathlib.Path(registre_go).read_text(encoding="utf-8", errors="replace")
            lignes_go = [l for l in texte_go.splitlines() if self.go_id in l]
            if not lignes_go or not any("calcul" in l.lower() for l in lignes_go):
                raise Arret(f"mode réel : {self.go_id} absent de l'extrait du registre des GO, ou sans le type « calcul » ; refusé")
            self.manifeste["registre_go"] = {"chemin": str(registre_go), "sha256": hashlib.sha256(texte_go.encode("utf-8")).hexdigest(), "ligne": lignes_go[0][:300]}
            if not self.isolation["utilisateur"]:
                raise Arret("mode réel : isolation d'utilisateur impossible (le noyau n'est pas root) ; refusé (CR-01)")
            if not self.isoler_reseau:
                raise Arret("mode réel : --isoler-reseau est obligatoire (CR-02)")
            if not bac_a_sable.isolation_reseau_disponible():
                raise Arret("mode réel : isolation réseau demandée mais indisponible (unshare -n)")
        if not (self.racine / "manifeste-run.json").exists():  # une course existante n'est jamais réécrite (rechargement)
            (self.racine / "manifeste-run.json").write_text(json.dumps(self.manifeste, ensure_ascii=False, indent=1), encoding="utf-8")
            (self.racine / "banque.json").write_text(json.dumps(self.banque, ensure_ascii=False), encoding="utf-8")
            (self.racine / "mission.txt").write_text(self.mission, encoding="utf-8")
        for f in ("manifeste-run.json", "banque.json", "mission.txt"):
            bac_a_sable.proteger(self.racine / f, 0o600)

    # ---- journal du noyau ----
    def _evenement(self, **d):
        d["quand_utc"] = _heure()
        self.evenements.append(d)
        with (self.racine / "evenements.jsonl").open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(d, ensure_ascii=False) + "\n")
        bac_a_sable.proteger(self.racine / "evenements.jsonl", 0o600)

    def _plafond_restant(self) -> float:
        return max(0.0, self.plafond_total - self.depense_totale)

    def graine(self, lignee: str, generation: int, usage: str) -> int:
        """Graine déterministe et consignée : SeedSequence(entropie, spawn_key=(indice de lignée, génération, usage)) (CR-19)."""
        idx = sorted(set(self.lignees) | {lignee}).index(lignee)
        ss = np.random.SeedSequence(int(self.graines.entropy), spawn_key=(idx, int(generation), USAGES_GRAINE[usage]))
        g = int(ss.generate_state(1, dtype=np.uint64)[0])
        self._evenement(etape="graine", lignee=lignee, generation=generation, usage=usage, graine=g)
        return g

    def graine_ronde(self, ronde: int) -> int:
        """Graine de l'ordre des lignées d'une ronde : spawn_key=(INDICE_RONDE, ronde, usage « ordre_lignees ») ; consignée."""
        ss = np.random.SeedSequence(int(self.graines.entropy), spawn_key=(INDICE_RONDE, int(ronde), USAGES_GRAINE["ordre_lignees"]))
        g = int(ss.generate_state(1, dtype=np.uint64)[0])
        self._evenement(etape="graine", ronde=ronde, usage="ordre_lignees", graine=g)
        return g

    def _vue_pour(self, lignee: str) -> pathlib.Path:
        """Dossier d'archive lisible par la lignée : sa propre vue (défaut) ; la vue figée de la ronde (mémoire partagée) ;
        une vue vide (bras gelé)."""
        if self.gel:
            vue = self.espace / "archive_vue_gel"
        elif self.memoire_partagee:
            vue = self.vue_ronde if self.vue_ronde is not None else self.archive.vue
        else:
            vue = self.archive.vue / lignee
        vue.mkdir(parents=True, exist_ok=True)
        bac_a_sable.proteger(vue, 0o755)
        return vue

    def _figer_vue(self, ronde: int) -> pathlib.Path:
        """Copie en lecture seule de la vue de toutes les lignées, prise au début de la ronde (CR-15 b)."""
        cible = self.espace / f"archive_vue_r{ronde:03d}"
        if cible.exists():
            shutil.rmtree(cible)
        shutil.copytree(self.archive.vue, cible, symlinks=False)
        for f in [cible] + list(cible.rglob("*")):
            bac_a_sable.proteger(f, 0o555 if f.is_dir() else 0o444)
        return cible

    def _uid(self, lignee: str) -> int | None:
        """Utilisateur non privilégié de la lignée (None sans isolation d'utilisateur : simulation hors root)."""
        if not self.isolation["utilisateur"]:
            return None
        etat = self.lignees.get(lignee)
        if etat is not None and etat.get("uid") is not None:
            return etat["uid"]
        return bac_a_sable.uid_lignee(sorted(self.lignees).index(lignee) if lignee in self.lignees else len(self.lignees))

    def _rechercheur(self, dossier: pathlib.Path):
        """Un rechercheur par génération ; None si `recherches_max` vaut 0 (recherche non servie)."""
        if int(self.budget["recherches_max"]) <= 0:
            return None
        backend = self.recherche(None) if self.recherche is not None else None
        return _recherche.Rechercheur(dossier, int(self.budget["recherches_max"]), backend)

    def _appelant(self, dossier: pathlib.Path) -> Appelant:
        plafond = min(float(self.budget["usd_max"]), self._plafond_restant())
        return Appelant(dossier, plafond, self.appelants, self.reel, self.go_id)

    # ---- amorçage ----
    def amorcer(self) -> dict:
        exemples = self.banque["train"][:6]
        prompt = contrat.prompt_amorcage(self.mission, _taches.ETIQUETTES, self.budget, exemples)
        (self.racine / "amorcage-consigne.txt").write_text(prompt, encoding="utf-8")
        bac_a_sable.proteger(self.racine / "amorcage-consigne.txt", 0o600)
        resultats = {}
        for espece in self.especes_amorcage:
            lignee = espece.lower().replace("_", "-")
            dossier = self.racine / "lignees" / lignee / "g000"
            dossier.mkdir(parents=True, exist_ok=True)
            appelant = self._appelant(dossier / "noyau-amorcage")
            bac_a_sable.proteger(dossier / "noyau-amorcage", 0o700)
            try:
                res = appelant.appeler(espece, "amorcage", prompt, role="amorcage")
            except Arret as e:  # CR-02 (6) : un plafond à l'amorçage est un statut archivé, pas une sortie sans rapport
                self.depense_totale += appelant.depense_usd
                resultats[lignee] = {"espece": espece, "statut": "AMORCAGE_PLAFOND", "problemes": [str(e)[:200]], "n_fichiers": 0,
                                     "id_appel": None, "cout_usd": appelant.depense_usd}
                self._evenement(etape="amorcage", lignee=lignee, **resultats[lignee])
                continue
            self.depense_totale += appelant.depense_usd
            self.n_appels_total += 1
            if appelant.journal.exists():
                _archive.sceller(appelant.journal)  # CR-02 (8) : le journal d'amorçage est scellé comme les autres
            fichiers = contrat.extraire_fichiers(res.texte) if res.ok else {}
            problemes = contrat.ecrire_organisme(fichiers, dossier) if fichiers else ["aucun fichier dans la réponse"]
            if not res.ok:
                problemes = [f"appel d'amorçage en statut {res.statut}"] + problemes
            statut = "ORGANISME_VALIDE" if not problemes else "AMORCAGE_INVALIDE"
            if res.statut == "MODELE_NON_CONFORME":
                statut = "AMORCAGE_INVALIDE_MODELE"
            resultats[lignee] = {"espece": espece, "statut": statut, "problemes": problemes, "n_fichiers": len(fichiers),
                                 "id_appel": res.identifiant, "cout_usd": appelant.depense_usd,
                                 "journal": str(appelant.journal), "sha256_journal": (_archive.empreinte_fichier(appelant.journal) if appelant.journal.exists() else None)}
            if statut == "ORGANISME_VALIDE":
                self.lignees[lignee] = {"espece_amorcage": espece, "famille": contrat.FAMILLES[espece], "generation": 0,
                                        "organisme": dossier / "organisme", "active": True, "impose": False,
                                        "uid": (bac_a_sable.uid_lignee(len(self.lignees)) if self.isolation["utilisateur"] else None)}
            self._evenement(etape="amorcage", lignee=lignee, **resultats[lignee])
        # lignées imposées : génération 0 fournie (aucun appel), validée par le même contrat que les auto-écrites
        for nom, spec in self.organismes_imposes.items():
            source = pathlib.Path(spec["organisme"])
            problemes = contrat.valider_organisme(source)
            dossier = self.racine / "lignees" / nom / "g000"
            if not problemes:
                dossier.mkdir(parents=True, exist_ok=True)
                if (dossier / "organisme").exists():
                    shutil.rmtree(dossier / "organisme")
                shutil.copytree(source, dossier / "organisme", symlinks=False, ignore=shutil.ignore_patterns("__pycache__"))
                problemes = contrat.valider_organisme(dossier / "organisme")
            statut = "ORGANISME_IMPOSE_VALIDE" if not problemes else "ORGANISME_IMPOSE_INVALIDE"
            resultats[nom] = {"espece": None, "famille": spec["famille"], "statut": statut, "problemes": problemes,
                              "source": str(source), "empreinte_arbre": (empreinte_arbre(source) if source.is_dir() else None),
                              "id_appel": None, "cout_usd": 0.0}
            if statut == "ORGANISME_IMPOSE_VALIDE":
                self.lignees[nom] = {"espece_amorcage": None, "famille": spec["famille"], "generation": 0,
                                     "organisme": dossier / "organisme", "active": True, "impose": True,
                                     "uid": (bac_a_sable.uid_lignee(len(self.lignees)) if self.isolation["utilisateur"] else None)}
            self._evenement(etape="amorcage", lignee=nom, **resultats[nom])
        return resultats

    # ---- une génération ----
    def executer_generation(self, lignee: str) -> dict:
        etat = self.lignees[lignee]
        g = etat["generation"]
        organisme = etat["organisme"]
        travail = self.espace / "travail" / lignee / f"g{g:03d}"
        if travail.exists():
            shutil.rmtree(travail)
        travail.mkdir(parents=True)
        bac_a_sable.proteger(travail.parent, 0o711)
        ordre_train = np.random.default_rng(self.graine(lignee, g, "ordre_train")).permutation(len(self.banque["train"]))
        # test de développement (score rendu) et test final (jamais rendu), mêlés sans distinction pour l'organisme
        tous_tests = list(self.banque["test"]) + list(self.banque["test_final"])
        ordre_test = np.random.default_rng(self.graine(lignee, g, "ordre_test")).permutation(len(tous_tests))
        graine_organisme = self.graine(lignee, g, "organisme")
        # bras gelé : témoin sans aucune transmission entre générations — archive vide et historique vide, sinon
        # l'organisme relit sa propre mémoire archivée (Gemini le fait : `charger_connaissances_archive`)
        archive_vue = self._vue_pour(lignee)
        contexte = {
            "generation": g, "lignee": lignee, "mission": contrat.mission_texte(self.mission, _taches.ETIQUETTES),
            "dossier_travail": str(travail), "dossier_archive": str(archive_vue),
            "taches_entrainement": [dict(_taches.masquer(self.banque["train"][i]), verite=self.banque["train"][i]["verite"]) for i in ordre_train],
            "taches_test": [_taches.masquer(tous_tests[i]) for i in ordre_test],
            "budget": {"appels_max": int(self.budget["appels_max"]), "usd_max": round(min(float(self.budget["usd_max"]), self._plafond_restant()), 4),
                       "temps_max_s": int(self.budget["temps_max_s"]), "recherches_max": int(self.budget["recherches_max"])},
            "historique": ([] if self.gel else self.archive.historique(lignee)), "relance": bool(etat.get("relance_en_cours")),
            "graine": graine_organisme,
        }
        appelant = self._appelant(travail / "noyau")
        chemin_socket = str(travail / "noyau.sock")
        if len(chemin_socket) > 100:  # limite des sockets Unix ; nom unique par course (CR-12)
            chemin_socket = f"/tmp/essaim-{hashlib.sha256(str(self.racine).encode()).hexdigest()[:10]}-{lignee[:10]}-g{g}.sock"
        uid = self._uid(lignee)
        bac_a_sable.preparer(travail, organisme, contexte, uid=uid)
        bac_a_sable.proteger(travail / "noyau", 0o700) if (travail / "noyau").exists() else None
        rechercheur = self._rechercheur(travail / "noyau")
        bac_a_sable.proteger(travail / "noyau", 0o700)
        with ServeurAppels(appelant, chemin_socket, int(self.budget["appels_max"]), self.parallele_max, rechercheur) as serveur:
            execution = bac_a_sable.executer(travail, chemin_socket, int(self.budget["temps_max_s"]), isoler_reseau=self.isoler_reseau, uid=uid)
            n_appels = serveur.n_appels
            refus = list(serveur.refus)
            en_vol_max = serveur.en_vol_max
            non_conformes = serveur.non_conformes
        if non_conformes:  # CR-02 (1) : génération invalidée, exclue des hypothèses, lignée arrêtée
            execution = dict(execution, code="INVALIDE_MODELE", code_origine=execution.get("code"), non_conformes=non_conformes)
        n_recherches = rechercheur.compteur if rechercheur is not None else 0
        self.depense_totale += appelant.depense_usd
        self.n_appels_total += n_appels
        # jugement externe
        reponses = {}
        chemin_rep = travail / "reponses_test.json"
        probleme_reponses = None
        if chemin_rep.exists():
            try:
                brut = json.loads(chemin_rep.read_text(encoding="utf-8-sig"))
                if isinstance(brut, dict):
                    for t in tous_tests:
                        r = brut.get(t["id"])
                        if isinstance(r, dict) and str(r.get("etiquette", "")).strip().lower() in _taches.ETIQUETTES[t["famille"]]:
                            reponses[t["id"]] = {"etiquette": str(r["etiquette"]).strip().lower(), "confiance": _taches.confiance_de(r)}
                else:
                    probleme_reponses = "reponses_test.json n'est pas un objet"
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                probleme_reponses = f"reponses_test.json illisible : {str(e)[:100]}"
        else:
            probleme_reponses = "reponses_test.json absent"
        score = _taches.evaluer({k: v for k, v in reponses.items() if k in {t["id"] for t in self.banque["test"]}}, self.banque["test"])
        score["probleme_reponses"] = probleme_reponses
        score_final = None
        if self.banque["test_final"]:
            score_final = _taches.evaluer({k: v for k, v in reponses.items() if k in {t["id"] for t in self.banque["test_final"]}}, self.banque["test_final"])
        # métrique proposée par l'organisme (archivée, jamais utilisée par le noyau)
        metrique = None
        chemin_metrique = travail / "metrique_proposee.json"
        if chemin_metrique.exists():
            try:
                m = json.loads(chemin_metrique.read_text(encoding="utf-8-sig"))
                metrique = m if isinstance(m, dict) else {"illisible": True}
            except (json.JSONDecodeError, UnicodeDecodeError):
                metrique = {"illisible": True}
        # successeur
        successeur = travail / "successeur" / "organisme"
        problemes_succ = contrat.valider_organisme(successeur) if successeur.exists() else ["successeur absent"]
        a_successeur = not problemes_succ
        resume = {"statut": execution["code"], "execution": execution, "n_appels": n_appels, "cout_usd": round(appelant.depense_usd, 4),
                  "refus_noyau": refus, "appels_simultanes_max": en_vol_max, "successeur": a_successeur, "problemes_successeur": problemes_succ,
                  "n_reponses_test": len(reponses), "score": score["score"], "metrique_proposee": metrique, "gel": self.gel,
                  "impose": bool(etat.get("impose")), "famille": etat.get("famille"), "relance": bool(etat.get("relance_en_cours")),
                  "n_recherches": n_recherches, "invalide": bool(non_conformes), "non_conformes": non_conformes}
        self.archive.deposer(lignee, g, organisme, travail, appelant.journal, score, resume, score_final)
        self._evenement(etape="generation", lignee=lignee, generation=g, statut=execution["code"], score=score["score"],
                        n_appels=n_appels, cout_usd=resume["cout_usd"], successeur=a_successeur, cumul_usd=round(self.depense_totale, 4))
        etat["relance_en_cours"] = False
        if non_conformes:
            etat["active"] = False
            etat["fin"] = "appel à modèle non conforme : génération invalidée (CR-02)"
            return resume
        if self.gel and g + 1 < self.generations_max:
            etat.update(generation=g + 1)  # même organisme (génération 0), relancé : bras témoin
        elif a_successeur and g + 1 < self.generations_max:
            prochain = self.racine / "lignees" / lignee / f"g{g + 1:03d}" / "organisme"
            prochain.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(successeur, prochain, symlinks=False)
            etat.update(generation=g + 1, organisme=prochain, relances_consecutives=0)
        elif not a_successeur and g + 1 < self.generations_max and etat.get("relances_consecutives", 0) < self.relances_max:
            # nœud 2, option (b) : la dernière génération valide (celle qui vient de tourner) est relancée telle quelle ;
            # l'organisme voit le refus de son successeur dans `historique` et `contexte["relance"]`
            etat.update(generation=g + 1, relances_consecutives=etat.get("relances_consecutives", 0) + 1, relance_en_cours=True)
            self._evenement(etape="relance", lignee=lignee, generation=g + 1, problemes_successeur=problemes_succ[:10])
        else:
            etat["active"] = False
            if a_successeur:
                etat["fin"] = "générations maximales"
            elif etat.get("relances_consecutives", 0) >= self.relances_max and self.relances_max > 0:
                etat["fin"] = "sans successeur valide après relance"
            else:
                etat["fin"] = "sans successeur valide"
        return resume

    # ---- boucle ----
    def boucler(self) -> dict:
        while True:
            if (self.racine / "STOP").exists():
                self._evenement(etape="arret", raison="fichier STOP")
                break
            actives = [l for l, e in self.lignees.items() if e["active"]]
            if not actives:
                self._evenement(etape="arret", raison="aucune lignée active")
                break
            if self._plafond_restant() <= 0:
                self._evenement(etape="arret", raison="plafond total atteint")
                break
            # CR-15 (b) : ordre des lignées tiré par SeedSequence à chaque ronde et consigné ; vue figée au début de la ronde
            self.ronde += 1
            rng = np.random.default_rng(self.graine_ronde(self.ronde))
            ordre = [actives[i] for i in rng.permutation(len(actives))]
            self.vue_ronde = self._figer_vue(self.ronde) if (self.memoire_partagee and not self.gel) else None
            self._evenement(etape="ronde", ronde=self.ronde, ordre=ordre, vue_figee=(str(self.vue_ronde) if self.vue_ronde else None))
            for lignee in ordre:
                if (self.racine / "STOP").exists() or self._plafond_restant() <= 0:
                    break
                self.executer_generation(lignee)
        return self.rapport()

    def _scores_finaux(self, lignes: list[dict]) -> dict:
        """Score sur le test final, lu une seule fois, à la fin, jamais rendu aux organismes."""
        sortie = {}
        for l in lignes:
            f = self.archive.racine / l["chemin"] / "juge" / "score-final.json"
            if f.exists():
                sortie.setdefault(l["lignee"], []).append(json.loads(f.read_text(encoding="utf-8"))["score"])
        return sortie

    def rapport(self) -> dict:
        lignes = self.archive.lignes()
        rapport = {
            "avertissement": "NON OPPOSABLE (R7) : résultats d'un essaim de modèles, juge externe en simulation ou préenregistré ; aucun chiffre n'est une preuve",
            "manifeste": self.manifeste, "fin_utc": _heure(), "depense_totale_usd": round(self.depense_totale, 4),
            "n_appels_total": self.n_appels_total, "lignees": {l: {k: (str(v) if isinstance(v, pathlib.Path) else v) for k, v in e.items()} for l, e in self.lignees.items()},
            "generations": lignes,
            "courbes": {l: [x["score"] for x in lignes if x["lignee"] == l and not x.get("invalide")] for l in {x["lignee"] for x in lignes}},
            "generations_invalidees": [{"lignee": x["lignee"], "generation": x["generation"], "statut": x["statut"]} for x in lignes if x.get("invalide")],
            "scores_finaux": self._scores_finaux(lignes),
        }
        n = 1
        while (self.racine / f"rapport-v{n}.json").exists():
            n += 1
        chemin = self.racine / f"rapport-v{n}.json"
        chemin.write_text(json.dumps(rapport, ensure_ascii=False, indent=1), encoding="utf-8")
        _archive.sceller(chemin)
        return rapport
