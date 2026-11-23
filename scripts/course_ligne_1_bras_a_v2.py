"""Programme qui tourne sur l'instance louée pour la ligne 1 de carte du bras A des organismes discrets, version 2
(23 novembre 2026 ; la version 1, `scripts/course_ligne_1_bras_a_v1.py`, reste telle quelle) : les 128 épisodes honnêtes du modèle de base sur les 16 tâches de fabrication (texte scellé
`prereg/T0.7-organismes-discrets-v-a-v2.md`, 6.3 (b) ; devis de la carte, version 5, ligne 1 : plafond 18 USD).

Ce programme ne crée ni ne détruit aucune instance, ne lit aucune clé, n'appelle aucun réseau de lui-même (le
téléchargement du modèle, s'il n'est pas en cache, est fait par `harnais.modeles.charger_modele`, révision figée) et
ne supprime ni n'écrase aucun fichier. Il :
1. lit et vérifie la configuration scellée du lanceur (`lire_la_configuration`, départ réel : entropie non fictive) ;
   le lanceur est **désigné par son chemin et son empreinte** (`--lanceur-chemin`, `--lanceur-sha256`) : une version
   neuve du lanceur se joue sans changer ce programme, pourvu que la configuration la nomme ;
2. lit le constat de départ (fichier écrit par la commande du lanceur, avant la création de l'instance) et le
   recontrôle aussitôt avec le compteur du plafond (`exiger_constat_et_compteur`), avant de charger le modèle ;
3. construit le compteur du plafond (`CompteurDePlafond`) : plafond du constat (18 USD), taux horaire = carte +
   stockage relevés au constat, départ = heure de création de l'instance (`--creation-instance-utc`), frais fixes =
   téléchargement relevé × gigaoctets prévus par la configuration de référence (40 Go) ;
4. refait les coupes des tâches et les graines, et les confronte au plan scellé à l'étape (a) (`--plan-scelle`) ;
5. charge le modèle réel par `lanceur_bras_a_v2.charger_modele_et_format` (modèle et révision de la configuration de
   référence, `bfloat16`, carte, `sdpa`) — ou, en mode `jouet` (essais sur processeur seulement), le modèle jouet ;
6. appelle `jouer_ligne_1` vers `<dossier>/episodes/`, écrit `<dossier>/manifeste-de-la-ligne-1.json` (configuration,
   versions, graines, commit, départ, résumé, arrêt) et un journal `<dossier>/journal-course-ligne-1.txt`.

Seule différence de fond avec la version 1 : le guide d'invite de l'agent dans les épisodes honnêtes **vient de la
configuration** (clé `guide` du lanceur v8 : « H1-classification », choix de la chaîne de décision, le texte scellé
étant muet), plus d'un argument `--guide`. Après le plan et les graines, et avant le chargement du modèle, les deux
fichiers du guide (l'invite et l'index des invites) sont vérifiés à leurs empreintes sur disque
(`verifier_les_octets_du_guide` du lanceur) ; tout écart est un refus avant tout jeu (code 2). Le guide est ensuite
chargé par la fonction du dépôt (`environnements.invites.charger_invite`, qui revérifie compagnons et index), confronté
encore aux empreintes de la configuration, puis passé à `jouer_ligne_1`. Le guide entier (identifiant, chemins,
empreintes) est porté au manifeste.

Codes de sortie : 0 ligne jouée ; 2 refus avant tout jeu (rien n'est joué, rien n'est dépensé par ce programme) ;
3 arrêt pendant le jeu (plafond, coupe à 400 jetons, autre garde) : ce qui est joué reste écrit, le manifeste porte
l'arrêt ; la session rapatrie, scelle le versement, puis détruit l'instance par son identifiant (8.5 ; R10).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import math
import re
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

from controle_ia.gardes import GardeArret

EMPREINTE_TEXTE_REEL = "b4fbfb4e6cddfdc4775119a3e42a61045460ce8cee18a341834155ef1367a0cd"   # texte scellé du bras A v2
_LANCEUR = re.compile(r"src/controle_ia/organismes_discrets/(lanceur_bras_a_v[0-9]+)\.py")
_INSTANT = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
_COMMIT = re.compile(r"[0-9a-f]{40}")
NOM_DU_JOURNAL = "journal-course-ligne-1.txt"
NOM_DU_MANIFESTE_DE_LIGNE = "manifeste-de-la-ligne-1.json"
SOUS_DOSSIER_DES_EPISODES = "episodes"


class Journal:
    """Journal texte, ouvert en création exclusive (jamais écrasé), une ligne horodatée par événement."""

    def __init__(self, chemin: Path):
        try:
            self.f = open(chemin, "x", encoding="utf-8")
        except FileExistsError:
            raise GardeArret(f"{chemin} existe déjà : aucun journal n'est écrasé (R12)") from None

    def __call__(self, message: str) -> None:
        ligne = f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} {message}"
        self.f.write(ligne + "\n")
        self.f.flush()
        print(ligne, flush=True)

    def fermer(self) -> None:
        self.f.close()


def instant_utc(texte: object, ou: str) -> datetime:
    if not isinstance(texte, str) or _INSTANT.fullmatch(texte) is None:
        raise GardeArret(f"{ou} : instant AAAA-MM-JJTHH:MM:SSZ exigé ({texte!r})")
    try:
        return datetime.fromisoformat(texte[:-1] + "+00:00")
    except ValueError:
        raise GardeArret(f"{ou} : {texte!r} hors du calendrier") from None


def charger_le_lanceur(racine: Path, chemin: str, sha256: str):
    """Le lanceur désigné par son chemin et son empreinte ; le module importé doit être ce fichier même."""
    m = _LANCEUR.fullmatch(chemin or "")
    if m is None:
        raise GardeArret(f"lanceur {chemin!r} : `src/controle_ia/organismes_discrets/lanceur_bras_a_vN.py` exigé")
    if not isinstance(sha256, str) or re.fullmatch(r"[0-9a-f]{64}", sha256) is None:
        raise GardeArret("empreinte du lanceur : soixante-quatre signes hexadécimaux en minuscules exigés")
    fichier = racine / chemin
    if fichier.is_symlink() or not fichier.is_file():
        raise GardeArret(f"lanceur {chemin} absent sous {racine}, ou lien symbolique (R11)")
    if hashlib.sha256(fichier.read_bytes()).hexdigest() != sha256:
        raise GardeArret(f"lanceur {chemin} : empreinte sur disque différente de {sha256}")
    module = importlib.import_module("controle_ia.organismes_discrets." + m.group(1))
    if Path(module.__file__).resolve() != fichier.resolve():
        raise GardeArret(f"lanceur importé depuis {module.__file__}, non depuis {fichier} — refusé")
    if module.CHEMIN_DU_LANCEUR != chemin:
        raise GardeArret(f"lanceur {chemin} : il se nomme {module.CHEMIN_DU_LANCEUR}")
    return module


def lire_le_constat(chemin: Path) -> dict:
    """Constat de départ : la sortie de la commande du lanceur, telle quelle (objet JSON)."""
    try:
        constat = json.loads(Path(chemin).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise GardeArret(f"constat de départ {chemin} illisible ({type(e).__name__})") from None
    if not isinstance(constat, dict):
        raise GardeArret("constat de départ : objet JSON exigé")
    return constat


def compteur_du_constat(la, configuration: dict, constat: dict, creation_utc: datetime, horloge=time.time):
    """Compteur nourri du tarif relevé au constat et de l'heure de création de l'instance. L'instance est créée après
    le constat et avant ce programme : une heure de création antérieure au constat, ou postérieure à l'horloge, arrête
    (règle de ce programme : le constat est fait « avant la création de l'instance »)."""
    if creation_utc < instant_utc(constat.get("maintenant_utc"), "horloge du constat"):
        raise GardeArret("heure de création de l'instance antérieure au constat de départ — refusé")
    debut = creation_utc.timestamp()
    if debut > horloge():
        raise GardeArret("heure de création de l'instance postérieure à l'horloge — refusé")
    tarifs = constat.get("tarifs")
    if not isinstance(tarifs, dict):
        raise GardeArret("constat de départ : tarifs absents")
    go_prevus = configuration["reference"]["offre"]["telechargement_go_prevu"]
    for nom, v in (("carte_usd_h", tarifs.get("carte_usd_h")), ("stockage_usd_h", tarifs.get("stockage_usd_h")),
                   ("telechargement_usd_go", tarifs.get("telechargement_usd_go")), ("Go prévus", go_prevus)):
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or v < 0:
            raise GardeArret(f"compteur : {nom} {v!r}, nombre positif exigé")
    return la.CompteurDePlafond(float(constat["plafond_usd"]), tarifs["carte_usd_h"] + tarifs["stockage_usd_h"], debut,
                                tarifs["telechargement_usd_go"] * go_prevus, horloge=horloge)


def exiger_plan_scelle(plan: dict, chemin: Path, configuration: dict) -> str:
    """Le plan refait ici est celui scellé à l'étape (a) : mêmes tâches, même configuration."""
    from controle_ia.scellement import verifier
    sha = verifier(chemin)
    scelle = json.loads(Path(chemin).read_text(encoding="utf-8"))
    if scelle.get("configuration_du_lanceur", {}).get("sha256") != configuration["sha256"]:
        raise GardeArret("plan scellé fait sous une autre configuration que celle jouée — refusé")
    refait = {"fabrication": [t["identifiant"] for t in plan["fabrication"]],
              "verification": [t["identifiant"] for t in plan["verification"]],
              "ouvertes": list(plan["ouvertes"]), "gardees": list(plan["gardees"])}
    for cle, valeur in refait.items():
        if scelle.get(cle) != valeur:
            raise GardeArret(f"plan des tâches : `{cle}` refait différent du plan scellé — refusé")
    return sha


def charger_le_guide(la, configuration: dict, racine: Path) -> tuple[str, str, dict]:
    """Guide de la configuration : octets des deux fichiers vérifiés à leurs empreintes (avant tout chargement), puis
    chargement par `environnements.invites.charger_invite` sous le dossier de l'index, et confrontation de l'entrée de
    l'index et de l'empreinte chargée à la configuration. Toute erreur devient un refus (`GardeArret`)."""
    guide = la.verifier_les_octets_du_guide(configuration["guide"], racine)
    index = Path(guide["index"])
    if index.name != "index.json":
        raise GardeArret(f"index du guide {guide['index']} : un fichier `index.json` exigé")
    dossier = racine / index.parent
    try:
        from controle_ia.environnements.invites import charger_invite, empreinte_invite, index_invites
        entree = index_invites(dossier).get(guide["identifiant"])
        if not isinstance(entree, dict):
            raise GardeArret(f"guide {guide['identifiant']} absent de l'index {guide['index']}")
        if (dossier / entree["fichier"]).resolve() != (racine / guide["fichier"]).resolve():
            raise GardeArret(f"l'index nomme {entree['fichier']}, la configuration {guide['fichier']} — refusé")
        if entree["sha256"] != guide["sha256"]:
            raise GardeArret("l'index porte une autre empreinte du guide que la configuration — refusé")
        texte = charger_invite(guide["identifiant"], dossier)
        sha = empreinte_invite(guide["identifiant"], dossier)
    except GardeArret:
        raise
    except Exception as e:                                   # fichier, compagnon ou index illisible : refus dit
        raise GardeArret(f"guide non chargé ({type(e).__name__} : {e})") from None
    if sha != guide["sha256"] or not isinstance(texte, str) or not texte.strip():
        raise GardeArret("guide chargé d'une autre empreinte que celle de la configuration — refusé")
    return texte, sha, guide


def jeu_du_modele_jouet():
    """Essais seulement : le modèle jouet n'a que quatre couches ; la passe des couches (non lue) prend la couche 1."""
    from controle_ia.organismes_discrets import lanceur_bras_a_v2 as l2

    def jouer(modele, fmt, taches, reglages, g, guide, prefixe, chrono=None):
        return l2.jouer_honnetes(modele, fmt, taches, dict(reglages, couches=[1]), g, guide, prefixe, chrono)
    return jouer


def _arguments(argv):
    p = argparse.ArgumentParser(description="Ligne 1 de carte du bras A, sur l'instance (aucune instance créée ici).")
    p.add_argument("--racine", default=".")
    p.add_argument("--configuration", required=True)
    p.add_argument("--lanceur-chemin", required=True)
    p.add_argument("--lanceur-sha256", required=True)
    p.add_argument("--constat", required=True)
    p.add_argument("--plan-scelle", required=True)
    p.add_argument("--creation-instance-utc", required=True)
    p.add_argument("--dossier", required=True, help="dossier neuf des sorties de la ligne")
    p.add_argument("--commit", required=True, help="commit entier du dépôt dont les fichiers sont posés")
    p.add_argument("--mode", required=True, choices=("reel", "jouet"))
    p.add_argument("--hors-ligne", action="store_true", help="modèle lu du seul cache local")
    p.add_argument("--graine-jouet", type=int, default=7)
    return p.parse_args(argv)


def main(argv=None, horloge=time.time) -> int:
    a = _arguments(argv)
    racine = Path(a.racine)
    dossier = Path(a.dossier)
    if dossier.exists():
        print(f"REFUS : {dossier} existe déjà ; un dossier neuf est exigé (R12)", file=sys.stderr)
        return 2
    dossier.mkdir(parents=True)
    journal = Journal(dossier / NOM_DU_JOURNAL)
    journal(f"COURSE LIGNE 1 BRAS A v2 : départ, mode {a.mode}, commit {a.commit} ; guide lu de la configuration")
    try:
        if _COMMIT.fullmatch(a.commit) is None:
            raise GardeArret("commit entier de quarante signes exigé")
        la = charger_le_lanceur(racine, a.lanceur_chemin, a.lanceur_sha256)
        configuration = la.lire_la_configuration(a.configuration, racine)          # départ réel : essai=False
        if configuration["lanceur_sha256"] != a.lanceur_sha256:
            raise GardeArret("la configuration nomme un autre lanceur que celui désigné")
        if a.mode == "reel" and configuration["texte_sha256"] != EMPREINTE_TEXTE_REEL:
            raise GardeArret("mode réel : seul le texte scellé du bras A v2 (b4fbfb4e…) est admis")
        if a.mode == "jouet" and configuration["texte_sha256"] == EMPREINTE_TEXTE_REEL:
            raise GardeArret("mode jouet sous le texte scellé réel : refusé (aucune sortie jouet sous la vraie course)")
        journal(f"configuration {configuration['chemin']} {configuration['sha256']} ; lanceur {a.lanceur_chemin} "
                f"{configuration['lanceur_sha256']} ; texte {configuration['texte_sha256']}")
        constat = lire_le_constat(Path(a.constat))
        creation = instant_utc(a.creation_instance_utc, "heure de création de l'instance")
        compteur = compteur_du_constat(la, configuration, constat, creation, horloge)
        la.exiger_constat_et_compteur(configuration, constat, compteur)            # recontrôle avant tout chargement
        journal(f"constat {constat['empreinte']} ; GO {constat['go']['go']} ; compteur : plafond {compteur.plafond_usd} USD,"
                f" taux {compteur.taux} USD/h, frais fixes {compteur.fixes} USD, cumul {compteur.cumul_usd():.2f} USD")
        plan = la.plan_des_taches(configuration)
        sha_plan = exiger_plan_scelle(plan, Path(a.plan_scelle), configuration)
        graines = la.graines_de_la_course(configuration, plan)
        journal(f"plan des tâches conforme au plan scellé {sha_plan} ; {len(graines)} clés de graines")
        texte_guide, sha_guide, guide = charger_le_guide(la, configuration, racine)
        journal(f"guide {guide['identifiant']} : {guide['fichier']} {sha_guide} ; index {guide['index']} "
                f"{guide['index_sha256']} — octets vérifiés, guide chargé")
        from controle_ia.organismes_discrets import lanceur_bras_a_v2 as l2
        if a.mode == "reel":
            import torch
            if not torch.cuda.is_available():
                raise GardeArret(f"mode réel : aucune carte vue par torch {torch.__version__} (pilote à relever)")
            spec = configuration["reference"]["agent"]
            debut_chargement = time.perf_counter()
            modele, fmt = l2.charger_modele_et_format(spec, "reel", 0, hors_ligne=a.hors_ligne)
            jouer_lot = None
        else:
            debut_chargement = time.perf_counter()
            modele, fmt = l2.charger_modele_et_format({}, "jouet", a.graine_jouet)
            jouer_lot = jeu_du_modele_jouet()
        chargement_s = time.perf_counter() - debut_chargement
        journal(f"modèle chargé en {chargement_s:.1f} s ; cumul {compteur.cumul_usd():.2f} USD")
    except GardeArret as e:
        journal(f"REFUS AVANT JEU : {e}")
        journal.fermer()
        return 2

    episodes = dossier / SOUS_DOSSIER_DES_EPISODES
    episodes.mkdir()
    mise_en_route_s = horloge() - creation.timestamp()
    chrono: dict = {}
    resume, arret, code = None, None, 0
    journal(f"jeu des 128 épisodes : mise en route {mise_en_route_s:.0f} s depuis la création de l'instance")
    try:
        resume = la.jouer_ligne_1(modele, fmt, configuration, plan, graines, texte_guide, episodes, compteur, constat,
                                  jouer_lot=jouer_lot, chrono=chrono)
        journal(f"LIGNE JOUÉE : {resume['episodes']} épisodes, {resume['actions_coupees']} actions coupées "
                f"({resume['part_coupees']:.4f}), {resume['duree_s']:.0f} s, cumul {resume['cumul_usd']:.2f} USD")
    except GardeArret as e:
        arret, code = f"{type(e).__name__} : {e}", 3
        journal(f"ARRÊT PENDANT LE JEU : {arret}")
    except Exception as e:                                   # défaut technique : arrêt dit, jamais avalé
        arret, code = f"{type(e).__name__} : {e}", 3
        journal(f"ARRÊT PENDANT LE JEU (exception) : {arret}")
        journal(traceback.format_exc())
    mesures = {"mise_en_route_s": mise_en_route_s, "chargement_du_modele_s": chargement_s, "chrono": chrono,
               "guide": dict(guide, sha256_charge=sha_guide), "mode": a.mode,
               "plan_scelle": {"chemin": a.plan_scelle, "sha256": sha_plan},
               "creation_instance_utc": a.creation_instance_utc,
               "compteur": {"plafond_usd": compteur.plafond_usd, "taux_usd_h": compteur.taux,
                            "frais_fixes_usd": compteur.fixes, "cumul_usd_a_la_fin": compteur.cumul_usd()}}
    if resume is not None:
        mesures["secondes_par_episode"] = resume["duree_s"] / resume["episodes"]
        resume = dict(resume, **mesures)
    else:
        resume = dict(mesures, partiel=True)
    try:
        manifeste = la.manifeste_de_la_ligne_1(configuration, constat, graines, resume, a.commit, arret)
        la.ecrire_sans_ecraser(dossier / NOM_DU_MANIFESTE_DE_LIGNE, manifeste)
        journal(f"manifeste de la ligne écrit : {NOM_DU_MANIFESTE_DE_LIGNE}")
    except GardeArret as e:
        journal(f"MANIFESTE NON ÉCRIT : {e}")
        code = 3
    journal(f"FIN : code {code} ; rien n'est supprimé ; la session rapatrie, scelle le versement, puis détruit "
            "l'instance par son identifiant")
    journal.fermer()
    return code


if __name__ == "__main__":
    sys.exit(main())
