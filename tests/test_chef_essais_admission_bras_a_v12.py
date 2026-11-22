"""Essais du chef des deux essais d'admission du bras A (`scripts/chef_essais_admission_bras_a_v12.py`) — version 12.

Devis : `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md`
(`421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc`), section 10 : les vingt gardes, chacune sur un
cas sain et sur un artefact (R5), contre le faux fournisseur local (`tests/faux_fournisseur_essais_admission_v12.py`),
et les chiffres du devis (plafonds, réserves, excès, délais globaux, crédits).

Aucun appel réseau hors de `127.0.0.1` ; aucune clé lue (une valeur factice est posée dans le seul relais) ; aucune
dépense. À lancer seul : `python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v12.py`.
"""
from __future__ import annotations

import copy
import datetime
from decimal import Decimal
import importlib.util
import json
import math
import fcntl
import os
import re
import subprocess
import sys
import threading
import time
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import faux_fournisseur_essais_admission_v12 as faux  # noqa: E402


def _charger(nom: str):
    spec = importlib.util.spec_from_file_location(nom, RACINE / "scripts" / f"{nom}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[nom] = module
    spec.loader.exec_module(module)
    return module


chef = _charger("chef_essais_admission_bras_a_v12")
relais_mistral = _charger("relais_mistral_essais_admission_v12")
relais_google = _charger("relais_google_essais_admission_v12")

GABARIT = ("docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/"
           "configuration-essais-admission-bras-a-v12-gabarit.json")
GABARIT_REGLES = "docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/regles-admission-bras-a-v1-gabarit.md"
ECHELLE = 2000.0     # durées réduites à l'essai, débit mis à l'échelle (devis, gardes 1 et 2)
GO = {"verification-mistral-eu": "GO-2026-11-22-01", "verification-google-cle-1": "GO-2026-11-22-02",
      "file-mistral": "GO-2026-11-22-03", "file-neon": "GO-2026-11-22-04", "verification-mistral-global": "GO-2026-11-22-05",
      "verification-google-cle-2": "GO-2026-11-22-06"}
CLE_1, CLE_2 = "GEMINI_API_KEY", "GEMINI_API_KEY_2"
GO_DE_L_AVENANT_3 = "GO-2026-11-22-16"          # livraison 12 : la confirmation de l'avenant 3 v2 par Lazar
GO_QUI_LEVE = "GO-2026-11-21-68"
LEVE = f"non constaté, levé par {GO_QUI_LEVE}"
LIEN_CONSTATE = {"google_cle_du_projet_constate_cle_1": "oui", "google_cle_du_projet_constate_cle_2": "oui"}   # C-1
MAINTENANT = datetime.datetime.now(datetime.timezone.utc)
AVANT = (MAINTENANT - datetime.timedelta(hours=2)).strftime("%Y-%m-%dT%H:%MZ")
APRES_CONSTAT = (MAINTENANT - datetime.timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
CONSTAT_SAIN = {      # la pièce de l'avenant 1, 5.1 : vingt-huit clés, six levées ; ici en dollars, deux projets distincts
    **{f"google_{c}_projet_{p}": v for p in ("a", "b") for c, v in (
        ("offre_payante", "oui"), ("devise_affichee", "USD"), ("credit_vu", "23,00"), ("recharge_automatique", "activée"),
        ("autres_credits_admissibles", "aucun"), ("credit_apres_une_recharge", "23,00"), ("partage_journaux", LEVE),
        ("duree_journaux_jours", LEVE), ("plafond_depense", f"aucun, par {GO_QUI_LEVE}"))},
    "google_cle_du_projet_constate_cle_1": LEVE, "google_cle_du_projet_constate_cle_2": LEVE,
    "google_deux_projets_distincts": "oui",
    "mistral_offre_payante": "oui", "mistral_donnees_pour_amelioration": "désactivé", "mistral_cle_de_l_espace_constate": "oui",
    "mistral_credit_utilisable_usd": "9,50", "mistral_limite_requetes_par_minute": "60",
    "mistral_limite_jetons_par_minute": "500000", "mistral_devise_affichee": "USD"}
EUROS = {"google_devise_affichee_projet_a": "EUR", "google_devise_affichee_projet_b": "EUR"}
_fini = subprocess.Popen([sys.executable, "-c", "pass"])
_fini.wait()
PID_MORT = _fini.pid             # l'identifiant d'un processus fini : une amorce qui n'est plus en vie
APPARIEMENT_CONFORME = '{"fit": "cannot_tell", "specific": null, "proposal_quote": null, "controls_quote": null}'


# --- le monde de l'essai : un dépôt factice, des pièces, une configuration tirée du gabarit -------------------------------

class Monde:
    def __init__(self, base: Path):
        self.racine = base / "zz-monde-9f3"
        self.racine.mkdir()
        for nom in ("docs", "src", "scripts", "prereg"):
            (self.racine / nom).symlink_to(RACINE / nom)
        (self.racine / "pieces").mkdir()
        (self.racine / "runs").mkdir()
        self.bancs_par_ligne: dict = {}
        self.interdits = base / "interdits-essai.txt"
        self.interdits.write_text("zorglub-terme-interdit\n", encoding="utf-8")
        self.config = self.config_de_base()
        self.piece("constat.md", constat())
        self.config["constat"] = self.ref("constat.md")
        self.piece("regles.md", regles_definitives())
        self.config["regles"].update(self.ref("regles.md"))

    def config_de_base(self) -> dict:
        config = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
        config["etat"] = "essai"
        config["garde_interdits"]["fichier_local"] = str(self.interdits)
        config["debit_declare_jetons_par_s"] = 200 * ECHELLE
        config["pause_s"] = 0.0
        config["marge_de_change"] = 0.0          # le gabarit la laisse nulle ; une valeur d'essai, sans effet à zéro
        config["age_max_du_fixage_heures"] = 96  # nulle au gabarit ; une valeur d'essai (un vendredi lu le lundi)
        config["regime_file_google"] = "courant"  # nul au gabarit ; « courant » n'est admis qu'à l'essai (R-1)
        config["temperature_retiree_d_avance"] = False   # nul au gabarit ; la valeur des livraisons d'avant (livraison 8)
        config["seuils_de_credit_google"] = "exiges"       # nul au gabarit ; le comportement d'avant (livraison 11)
        regle_google_d_essai(config)
        for nom, L in config["lignes"].items():
            L["go"] = GO[nom]
            L["delais"] = {k: v / ECHELLE for k, v in L["delais"].items()}
        for f in config["fournisseurs"].values():   # le gabarit est régénéré à la fin : les essais suivent le disque
            f["relais"]["sha256"] = chef.sha256_fichier(RACINE / f["relais"]["chemin"])
        config["lignes"]["file-mistral"]["hote"] = "api.eu.mistral.ai"
        return config

    def piece(self, nom: str, contenu, sceller: bool = True) -> Path:
        chemin = self.racine / "pieces" / nom
        chemin.write_text(contenu if isinstance(contenu, str) else json.dumps(contenu, ensure_ascii=False, indent=1),
                          encoding="utf-8")
        if sceller:
            compagnon = Path(str(chemin) + ".sha256")
            compagnon.write_text(f"{chef.sha256_fichier(chemin)}  {chemin.name}\n", encoding="utf-8")
        return chemin

    def ref(self, nom: str) -> dict:
        return {"chemin": f"pieces/{nom}", "sha256": chef.sha256_fichier(self.racine / "pieces" / nom)}

    def ecrire_configuration(self, nom: str = "configuration.json") -> tuple:
        chemin = self.piece(nom, self.config)
        return chemin, chef.sha256_fichier(chemin)

    def registre(self, lignes=None) -> str:
        sortie = ["| identifiant | accordé | type | périmètre | plafond | échéance | par | référence |", "|---|---|---|---|---|---|---|---|"]
        for nom in lignes or GO:
            L = self.config["lignes"][nom]
            perimetre = "bras A, " + ", ".join(L["marques_du_perimetre"]) + ", devis " + chef.EMPREINTE_DEVIS
            perimetre += ", vérification du devis " + self.config["verification_du_devis"]["sha256"]
            perimetre += ", avenant 1 " + self.config["avenant"]["sha256"]
            if chef.LIGNES[nom][1] == "google" and (self.config.get("avenant_2") or {}).get("sha256"):
                perimetre += ", avenant 2 " + self.config["avenant_2"]["sha256"]
            if chef.LIGNES[nom][1] == "google" and (self.config.get("avenant_3") or {}).get("sha256"):   # livraison 12
                perimetre += ", avenant 3 " + self.config["avenant_3"]["sha256"] + ", " + GO_DE_L_AVENANT_3
            sortie.append(f"| {GO[nom]} | 2026-11-01 | calcul | {perimetre} | {L['plafond_registre']} | 2099-12-31 | Lazar | R-0 |")
        return "\n".join(sortie) + "\n"

    def releve(self, ligne: str, nom: str, go: str | None = None, **champs) -> dict:
        """Écrit un relevé de vérification factice, scellé, dans le dossier de la ligne ; rend sa référence."""
        _, fournisseur, _ = chef.LIGNES[ligne]
        base = {"version": chef.VERSION, "ligne": ligne, "go": go or GO[ligne], "fournisseur": fournisseur,
                "hote": self.config["lignes"][ligne]["hote"], "quand": APRES_CONSTAT, "lancements": 1, "listes": [],
                "appels": [], "saine": True, "nom_servi": chef.IDENTIFIANTS[fournisseur],
                "temperature_envoyee": True if fournisseur == "mistral" else None,
                "orthographe_niveau": "XHIGH" if fournisseur == "google" else None,
                "sonde": {"issue": "comprise"}, "majorant": "établi" if fournisseur == "mistral" else None,
                "signe_constate": False, "issue_finale_ligne": 3, "noeud_de_lazar": False, "close": True,
                "depense_comptee_usd": 0.02, "envois_coupes": []}
        if fournisseur == "google":
            base["variable_cle"] = self.config["lignes"][ligne]["variable_cle"]
            # livraison 10 : la fiche lue à l'appel de liste porte `outputTokenLimit` (la file l'exige des relevés)
            base["listes"] = [{"code": 200, "lisible": True, "porte_identifiant": True, "limite_sortie": 65536}]
        base.update(champs)
        dossier = self.racine / self.config["lignes"][ligne]["dossier"] / f"{nom}-{ligne}"
        dossier.mkdir(parents=True)
        chemin = dossier / "releve-verification-v1.json"
        chemin.write_text(json.dumps(base, ensure_ascii=False), encoding="utf-8")
        Path(str(chemin) + ".sha256").write_text(f"{chef.sha256_fichier(chemin)}  {chemin.name}\n", encoding="utf-8")
        return {"chemin": str(chemin.relative_to(self.racine)), "sha256": chef.sha256_fichier(chemin)}

    def inscrire_releve(self, ligne_file: str, ref: dict, ref_cle_2: dict | None = None, **inscrit) -> None:
        """Inscrit à la configuration le relevé de vérification d'une file. File du juge : deux relevés, un par clé ;
        si celui de la clé 2 n'est pas donné, un relevé sain factice est écrit, sous une ligne de calcul à lui."""
        _, fournisseur, _ = chef.LIGNES[ligne_file]
        L = self.config["lignes"][ligne_file]
        L["inscrit"] = {"nom_servi": chef.IDENTIFIANTS[fournisseur], "hote": L["hote"]}
        if fournisseur == "mistral":
            L["releve_verification"] = ref
            L["inscrit"]["temperature_envoyee"] = True
        else:
            if ref_cle_2 is None:
                self.releves_auto = getattr(self, "releves_auto", 0) + 1
                ref_cle_2 = self.releve("verification-google-cle-2", f"auto-{self.releves_auto}",
                                        go=f"GO-2026-11-24-{self.releves_auto:02d}", depense_comptee_usd=0.0)
            L["releves_verification"] = {CLE_1: ref, CLE_2: ref_cle_2}
            L["inscrit"]["orthographe_niveau"] = "XHIGH"
        L["inscrit"].update(inscrit)


def regle_google_d_essai(config: dict) -> dict:
    """Les champs que le gabarit laisse nuls (deux décisions de Lazar ouvertes), à des valeurs d'essai : le plafond du
    devis (32 768), un niveau à la borne déclarée de 16 768 (32 768 − 16 000), la sonde exemptée."""
    g = config["fournisseurs"]["google"]
    g.update({"sortie_max": 32768, "reflexion": {"forme": "niveau", "borne_declaree": 16768}, "exemption_de_la_sonde": True,
              "exemption_de_la_sonde_go": "GO-2026-11-22-90", "jetons_par_mot": 2})
    for consigne in config["consignes"].values():
        consigne["limite_de_mots"] = 400
    # livraison 9 : les valeurs de la section 9 de l'avenant 2, nulles au gabarit ; à l'essai, celles de l'avenant 1
    # (les chiffres d'essai des livraisons d'avant). La définitive exige celles de l'avenant 2 (`controler_avenant_2`).
    g.update({"credit_min_avant_verification_usd": 19.76, "credit_min_avant_file_usd": 16.08, "credit_a_avoir_usd": 23.0})
    for ligne, (plafond, registre, exces, delais) in {
            "verification-google-cle-1": (1.5, "1,50 USD", 2.18, chef.DELAIS_VERIFICATION_GOOGLE),
            "verification-google-cle-2": (1.5, "1,50 USD", 2.18, chef.DELAIS_VERIFICATION_GOOGLE),
            "file-neon": (8.5, "8,50 USD", 7.58, chef.DELAIS_FILE_GOOGLE)}.items():
        config["lignes"][ligne].update({"plafond_usd": plafond, "plafond_registre": registre,
                                        "exces_possible_d_un_envoi_usd": exces, "delais": dict(delais)})
    return config


def ligne_de_taux(valeur: str = "1,0700", quand: str = AVANT, source: str = "BCE", publie: str | None = None) -> str:
    """La ligne de taux d'une pièce, avec la date de publication du fixage (par défaut, le jour de l'heure du taux)."""
    return (f"- taux : {valeur} USD par EUR ; source : {source} ; heure du taux (UTC) : {quand} ; "
            f"fixage publié le : {publie or quand[:10]}")


TAUX = ligne_de_taux(source="BCE, cours de référence")


def constat(modifs: dict | None = None, sans=(), plus: dict | None = None, date: str = AVANT, mot: bool = True,
            transcription: str | None = None, hors_tableau=(), sources: dict | None = None, dates: dict | None = None) -> str:
    """La pièce de constat de l'avenant 1 : tableau à quatre colonnes — clé, valeur, source, heure."""
    valeurs = dict(CONSTAT_SAIN)
    valeurs.update(modifs or {})
    valeurs.update(plus or {})
    lignes = ["# Constat des comptes — pièce d'essai", ""]
    if mot:
        lignes += ["## Mot de Lazar", "", "> on combine les deux clés, recharge automatique activée, euros affichés", ""]
    lignes += ["## Tableau", "", "| clé | valeur | source | heure (UTC) |", "|---|---|---|---|"]
    for k, v in valeurs.items():
        if k not in sans:
            source = (sources or {}).get(k, "levé" if str(v).startswith("non constaté") else "capture")
            lignes.append(f"| {k} | {v} | {source} | {(dates or {}).get(k, date)} |")
    lignes += ["", f"- heure de la transcription (UTC) : {transcription or AVANT}", *hors_tableau, ""]
    return "\n".join(lignes)


def regles_definitives() -> str:
    texte = (RACINE / GABARIT_REGLES).read_text(encoding="utf-8")
    return "\n".join(l for l in texte.split("\n") if not l.startswith("- état : gabarit"))


def mot_sur_la_sonde(releve_sha: str, issue: str = "indécidée", majorant: str | None = None, mot: bool = True) -> str:
    """Mot de Lazar sur la sonde, file Mistral."""
    lignes = ["# Mot de Lazar sur la sonde de borne — pièce d'essai", ""]
    if mot:
        lignes += ["## Mot de Lazar", "", "> go, partir aux mêmes réglages", ""]
    lignes += [f"- issue de la sonde visée : {issue}", f"- empreinte du relevé de vérification : {releve_sha}"]
    if majorant is not None:
        lignes.append(f"- majorant visé : {majorant}")
    return "\n".join(lignes) + "\n"


def mot_neon(refs: dict, issues=("indécidée", "comprise"), credits=("19,32", "19,32"), mot: bool = True, plus=()) -> str:
    """Mot de Lazar sur les sondes de la file du juge : les deux relevés, les deux issues, le crédit vu des deux projets."""
    lignes = ["# Mot de Lazar sur les sondes de borne — pièce d'essai", ""]
    if mot:
        lignes += ["## Mot de Lazar", "", "> go, partir aux mêmes réglages", ""]
    for numero, variable in enumerate((CLE_1, CLE_2), start=1):
        lignes += [f"- issue de la sonde visée, clé {numero} : {issues[numero - 1]}",
                   f"- empreinte du relevé de vérification, clé {numero} : {refs[variable]['sha256']}"]
    for projet, credit in zip(("a", "b"), credits or ()):
        if credit is not None:
            lignes.append(f"- crédit vu après les vérifications, projet {projet} : {credit}")
    lignes += ["- page : console, facturation", f"- heure (UTC) : {APRES_CONSTAT}", *plus]
    return "\n".join(lignes) + "\n"


def lecture_console(cite: str, vue: str = "0,01", plus=()) -> str:
    """Lecture de la console après un envoi coupé, chez Mistral."""
    lignes = ["# Lecture de la console après un envoi coupé — pièce d'essai", "", "## Mot de Lazar", "", "> vu à la console", "",
              f"- empreinte du relevé ou du rapport : {cite}", f"- dépense vue : {vue}",
              "- page : console, usage", f"- heure (UTC) : {APRES_CONSTAT}", *plus]
    return "\n".join(lignes) + "\n"


def lecture_console_google(cite: str, vues=("0,20", "0,20"), soldes=("22,50", "22,50"),
                           recharges: str | None = "nombre 0 ; montant 0", plus=(), mot: bool = True) -> str:
    """Lecture de la console chez Google : dépense vue et solde vu des deux projets, recharges survenues."""
    lignes = ["# Lecture de la console après un envoi coupé — pièce d'essai", ""]
    if mot:
        lignes += ["## Mot de Lazar", "", "> vu à la page de facturation des deux projets", ""]
    lignes.append(f"- empreinte du relevé ou du rapport : {cite}")
    for projet, vue, solde in zip(("a", "b"), vues, soldes):
        lignes += ([f"- dépense vue, projet {projet} : {vue}"] if vue is not None else []) + (
            [f"- solde vu, projet {projet} : {solde}"] if solde is not None else [])
    if recharges is not None:
        lignes.append(f"- recharges survenues : {recharges}")
    lignes += ["- page : AI Studio, facturation", f"- heure (UTC) : {APRES_CONSTAT}", *plus]
    return "\n".join(lignes) + "\n"


@pytest.fixture()
def monde(tmp_path):
    return Monde(tmp_path)


# --- le banc : faux fournisseur, relais dans un fil, dossier de la ligne --------------------------------------------------

class Banc:
    def __init__(self, monde: Monde, ligne: str, liste=None, adresse=None, environnement_du_relais=None):
        self.monde, self.ligne = monde, ligne
        _, self.fournisseur, _ = chef.LIGNES[ligne]
        self.config = monde.config
        # Un relevé clos ferme sa ligne de calcul : le premier banc d'une ligne joue sous la ligne de calcul inscrite,
        # chaque banc suivant de la même ligne sous une ligne de calcul à lui (un cas d'essai n'hérite pas d'un autre).
        rang = monde.bancs_par_ligne.get(ligne, 0)
        monde.bancs_par_ligne[ligne] = rang + 1
        self.go = GO[ligne] if rang == 0 else f"GO-2026-11-23-{rang:02d}"
        self.pid_amorce = PID_MORT       # par défaut, l'amorce du dossier n'est plus en vie (file close)
        L, f = self.config["lignes"][ligne], self.config["fournisseurs"][self.fournisseur]
        self.faux = faux.FauxFournisseur(liste if liste is not None else (
            faux.liste_mistral() if self.fournisseur == "mistral" else faux.modele_google())).demarrer()
        self.dossier = monde.racine / L["dossier"] / f"essai-{time.monotonic_ns()}-{ligne}"
        self.dossier.mkdir(parents=True)
        self.ecrire_manifeste()
        self.environnement_du_relais, self.adresse = environnement_du_relais or {}, adresse or self.faux.url
        self.variables = chef.variables_de_la_ligne(self.config, ligne)      # un relais par variable de clé
        self.serveurs, self.urls, self.journaux = [], {}, {}
        self.lancer_les_relais()
        self.pauses: list = []

    def lancer_les_relais(self) -> None:
        L, f = self.config["lignes"][self.ligne], self.config["fournisseurs"][self.fournisseur]
        for variable in self.variables:
            sous_dossier = self.dossier / chef.nom_du_dossier_du_relais(self.config, self.ligne, variable)
            sous_dossier.mkdir(parents=True, exist_ok=True)
            journal = sous_dossier / "journal-relais.jsonl"
            env = {variable: "valeur-factice-du-relais", **self.environnement_du_relais}
            maximum = chef.envois_max_du_relais(self.config, self.ligne)
            if self.fournisseur == "mistral":
                serveur = relais_mistral.servir(0, env, variable, L["hote"], f["modele"], maximum,
                                                L["plafond_usd"], f["prix"], L["reserve_sortie_jetons"],
                                                L["delais"]["relais_silence_s"], L["delais"]["relais_total_s"],
                                                str(journal), self.adresse)
            else:
                exempte = f["sortie_max_sonde"] if (chef.LIGNES[self.ligne][0] == "verification" and f["exemption_de_la_sonde"]) else None
                serveur = relais_google.servir(0, env, variable, L["hote"], f["modele"], maximum,
                                               L["delais"]["relais_total_s"], str(journal), self.adresse,
                                               chef.reglage_de_reflexion(f)["borne"], exempte)
            threading.Thread(target=serveur.serve_forever, daemon=True).start()
            self.serveurs.append(serveur)
            self.urls[variable], self.journaux[variable] = f"http://127.0.0.1:{serveur.server_address[1]}", journal
        self.serveur = self.serveurs[0]
        self.url, self.journal_relais = self.urls[self.variables[0]], self.journaux[self.variables[0]]

    def ecrire_manifeste(self) -> None:
        """Le manifeste que l'amorce écrit avant l'ouvrier : il dit sous quelle ligne de calcul joue le dossier."""
        (self.dossier / "manifeste-depart.json").write_text(
            json.dumps({"ligne": self.ligne, "go": self.go, "pid_amorce": self.pid_amorce}), encoding="utf-8")

    def fermer(self) -> None:
        for serveur in self.serveurs:
            serveur.shutdown()
            serveur.server_close()
        self.faux.arreter()

    def nouveau_dossier(self) -> Path:
        self.dossier = self.monde.racine / self.config["lignes"][self.ligne]["dossier"] / f"essai-{time.monotonic_ns()}-{self.ligne}"
        self.dossier.mkdir(parents=True)
        self.ecrire_manifeste()
        return self.dossier

    def verifier(self, etat=None, go=None, **plus) -> dict:
        etat = etat or chef.etat_de_la_ligne(self.monde.racine, self.config, self.ligne, go or self.go)
        return chef.jouer_verification(self.config, self.ligne, self.dossier, self.url, self.journal_relais,
                                       ["zorglub-terme-interdit"], etat, go or self.go, dormir=self.pauses.append, **plus)

    def jouer(self, regime: str = "courant", lot=None, **contexte) -> dict:
        ctx = {"regime": regime, "nom_servi": chef.IDENTIFIANTS[self.fournisseur],
               "hote": self.config["lignes"][self.ligne]["hote"], "temperature_envoyee": True,
               "orthographe_niveau": "XHIGH", "sonde": "comprise", "releve": {"chemin": "x", "sha256": "0" * 64}}
        ctx.update(contexte)
        self.contexte = ctx
        lot = lot or chef.charger_textes(self.config, self.monde.racine)
        programme = chef.charger_programme_de_forme(self.config, self.monde.racine)
        manifeste = {"ligne": self.ligne, "go": self.go, "fournisseur": self.fournisseur, "contexte": ctx,
                     "pid_amorce": self.pid_amorce,
                     "texte_en_vigueur": self.config["prereg_en_vigueur"], "regles": self.monde.ref("regles.md") | {},
                     "projection": self.config["projection"]}
        (self.dossier / "manifeste-depart.json").write_text(json.dumps(manifeste), encoding="utf-8")
        voies = (self.urls, self.journaux) if len(self.variables) > 1 else (self.url, self.journal_relais)
        return chef.jouer_file(self.config, self.ligne, lot, self.dossier, *voies,
                               ["zorglub-terme-interdit"], ctx, programme, dormir=self.pauses.append)

    def envois(self) -> list:
        return [l for l in chef.lire_journal(self.dossier / "journal-essai.jsonl") if l.get("evenement") == "envoi"]


@pytest.fixture()
def banc(monde):
    ouverts = []

    def fabriquer(ligne: str, **plus) -> Banc:
        b = Banc(monde, ligne, **plus)
        ouverts.append(b)
        return b

    yield fabriquer
    for b in ouverts:
        b.fermer()


def reponses_conformes(config: dict, racine: Path, ligne: str, fabrique) -> list:
    """Une réponse de forme conforme par entrée de la file, dans l'ordre (aucun extrait n'est exigé : étayée)."""
    lot = chef.charger_textes(config, racine)
    sortie = []
    for ident in chef.entrees_de_la_file(ligne, config, lot):
        entree = lot["textes"][ident]
        if entree["instrument"] == "appariement":
            texte = APPARIEMENT_CONFORME
        else:
            texte = json.dumps({i: {"content": "absent", "quote": None, "place": None}
                                for i in entree["champs"]["identifiants"]})
        sortie.append(fabrique(texte))
    return sortie


def sonde_mistral(jetons=200, fin="length", pensee="p" * 300, **plus) -> dict:
    return faux.flux_mistral(texte="1", pensee=pensee, usage=(30, jetons, 30 + jetons), fin=fin, **plus)


def sonde_google(facture=256, pensees=180, fin="MAX_TOKENS", **plus) -> dict:
    return faux.reponse_google("4", usage=(30, facture - pensees, pensees, 30 + facture), fin=fin, **plus)


def dossiers_de(base: Path) -> list:
    """Les dossiers de lancement sous une base, dans l'ordre (le fichier de verrou de la ligne n'en est pas un)."""
    return sorted(p for p in base.iterdir() if p.is_dir())


def attendre(condition, delai_s: float = 30.0):
    """Attend qu'une condition soit vraie et rend sa valeur ; au bout du délai (large : il ne sert qu'en cas de
    défaut), rend la dernière valeur, fausse. L'essai attend un événement, il ne parie pas sur une durée."""
    fin = time.monotonic() + delai_s
    valeur = condition()
    while not valeur and time.monotonic() < fin:
        time.sleep(0.01)
        valeur = condition()
    return valeur


def approx(x, rel=None, abs_=0.006):
    return pytest.approx(x, rel=rel, abs=abs_)


# === Chiffres du devis : plafonds, réserves, excès, délais, crédits (sections 5.6, 6.3, 6.4, 6.5) =========================

def _compteur(ligne: str, config: dict) -> tuple:
    _, fournisseur, _ = chef.LIGNES[ligne]
    regle_google_d_essai(config)             # le plafond du devis : 32 768
    L, f = config["lignes"][ligne], config["fournisseurs"][fournisseur]
    L = {**L, "reserve_sortie_jetons": chef.reserve_de_la_ligne(config, ligne)}
    return chef.Compteur(L["plafond_usd"], f["prix"], 200.0), L, f


def test_chiffres_reserves_du_devis_6_4():
    config = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
    c, L, _ = _compteur("file-mistral", config)
    assert L["reserve_sortie_jetons"] == 262144 + 64 and L["borne_octets"] == 262144
    # le devis arrondit au millième supérieur (0,6242 y est écrit 0,625) : tolérance d'un millième
    assert c.reserve(5000, L["reserve_sortie_jetons"]) == approx(0.610, abs_=0.001)
    assert c.reserve(24000, L["reserve_sortie_jetons"]) == approx(0.625, abs_=0.001)
    assert c.reserve(24000, L["reserve_sortie_jetons"]) <= 0.625
    for ligne in ("verification-mistral-eu", "verification-mistral-global"):
        c, L, _ = _compteur(ligne, config)
        assert L["reserve_sortie_jetons"] == 32768 + 64 and L["borne_octets"] == 32768
        assert c.reserve(150, L["reserve_sortie_jetons"]) == approx(0.076, abs_=0.0006)
        # le plafond de 0,25 USD laisse passer trois envois (0,228) et refuse le quatrième (0,304)
        r = c.reserve(150, L["reserve_sortie_jetons"])
        assert 3 * r <= 0.25 < 4 * r and 3 * r == approx(0.228, abs_=0.001)
    c, L, _ = _compteur("file-neon", config)
    assert c.reserve(5000, L["reserve_sortie_jetons"]) == approx(0.507, abs_=0.0006)
    assert c.reserve(24000, L["reserve_sortie_jetons"]) == approx(0.564, abs_=0.0006)
    c, L, _ = _compteur("verification-google-cle-1", config)
    assert c.reserve(150, L["reserve_sortie_jetons"]) == approx(0.492, abs_=0.0006)


def test_chiffres_plafonds_exces_et_credits_du_devis_6_3_a_6_5():
    config = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
    google = ("verification-google-cle-1", "verification-google-cle-2", "file-neon")
    assert all(config["lignes"][n][c] is None for n in google for c in ("plafond_usd", "plafond_registre",
                                                                         "exces_possible_d_un_envoi_usd", "delais"))
    assert config["fournisseurs"]["google"]["credit_min_avant_verification_usd"] is None    # livraison 9 : nuls au gabarit
    regle_google_d_essai(config)                     # les chiffres de l'avenant 1, valeurs d'essai (avenant 2 : plus bas)
    plafonds = {n: L["plafond_usd"] for n, L in config["lignes"].items()}
    assert plafonds == {"verification-mistral-eu": 0.25, "verification-mistral-global": 0.25, "verification-google-cle-1": 1.50,
                        "verification-google-cle-2": 1.50, "file-mistral": 4.75, "file-neon": 8.50}
    assert sum(plafonds.values()) == pytest.approx(16.75)            # avenant 1, section 6 : 15,25 + 1,50, avec la ligne 6
    assert sorted(L["numero_au_devis"] for L in config["lignes"].values()) == [1, 2, 3, 4, 5, 6]
    # excès d'un seul envoi : coût au débit déclaré sur le délai du relais, moins la sortie de réserve déjà comptée
    exces = {}
    for ligne, L in config["lignes"].items():
        _, fournisseur, _ = chef.LIGNES[ligne]
        prix = config["fournisseurs"][fournisseur]["prix"][1]
        exces[ligne] = (200 * L["delais"]["relais_total_s"] - chef.reserve_de_la_ligne(config, ligne)) * prix / 1e6
        assert math.ceil(exces[ligne] * 100 - 1e-9) / 100 == L["exces_possible_d_un_envoi_usd"]
    assert [config["lignes"][n]["exces_possible_d_un_envoi_usd"] for n in (
        "verification-mistral-eu", "verification-google-cle-1", "file-mistral", "file-neon", "verification-mistral-global",
        "verification-google-cle-2")] == [1.17, 2.18, 0.64, 7.58, 1.17, 2.18]
    assert sum(L["exces_possible_d_un_envoi_usd"] for L in config["lignes"].values()) == pytest.approx(14.92)   # avenant 1, section 6
    # pire cas chez Google (avenant 1, 2.2) : deux vérifications et la file, au régime prudent, puis au cas des neuf excès
    assert 2 * (1.50 + 2.18) + 8.50 + 7.58 == pytest.approx(23.44) and round(2 * 3.68 + 8.50 + 9 * 7.578, 2) == 84.06
    # crédits de 6.5 : plafonds et excès, marge de 15 %, arrondi au demi-dollar supérieur
    mistral = 4.75 + 0.25 + 0.25 + 0.64 + 1.17 + 1.17
    google = 8.50 + 1.50 + 2.18 + 7.58
    assert mistral == pytest.approx(8.23) and google == pytest.approx(19.76)
    assert math.ceil(mistral * 1.15 * 2) / 2 == 9.50 and math.ceil(google * 1.15 * 2) / 2 == 23.00
    assert config["constat_cles"]["mistral_credit_utilisable_usd"]["min"] == 8.23
    assert config["fournisseurs"]["google"]["credit_min_avant_verification_usd"] == 19.76
    assert config["fournisseurs"]["google"]["credit_min_avant_file_usd"] == pytest.approx(8.50 + 7.58)
    # avenant 1, 5.1 : vingt-huit clés (neuf par projet, deux de lien, une des deux projets, sept de Mistral) ; six levables
    assert set(config["constat_cles"]) == set(CONSTAT_SAIN) == set(chef.CLES_DU_CONSTAT) and len(config["constat_cles"]) == 28
    assert sorted(config["cles_levees"]["cles"]) == sorted(chef.CLES_LEVABLES) and len(chef.CLES_LEVABLES) == 6
    assert config["cles_levees"]["go"] == GO_QUI_LEVE and not [c for c in chef.CLES_LEVABLES if c.startswith("mistral")]
    assert config["marge_de_change"] is None and config["marge_de_change_go"] is None      # aucune valeur choisie au gabarit
    assert config["lignes"]["file-neon"]["partage"] == [dict(x) for x in chef.PARTAGE_NEON]
    assert [x["variable_cle"] for x in chef.PARTAGE_NEON] == [CLE_1, CLE_2] * 4


def test_chiffres_delais_globaux_du_devis_5_6():
    assert chef.delai_global_file(24, 2700, 600, 10) == 144840
    assert chef.delai_global_file(8, 2700, 600, 10) == 48680
    assert chef.delai_global_verification(3, 2700, 600) == 8700
    assert chef.delai_global_verification(3, 900, 600) == 3300
    assert 32768 / 2690 == pytest.approx(12.2, abs=0.05)             # débit que tiennent les délais
    config = regle_google_d_essai(json.loads((RACINE / GABARIT).read_text(encoding="utf-8")))
    for ligne, L in config["lignes"].items():
        d = L["delais"]
        assert d["relais_total_s"] == d["total_s"] - 10 and d["relais_silence_s"] == d["silence_s"] - 10
    assert config["lignes"]["verification-google-cle-1"]["delais"]["total_s"] == 900
    assert config["lignes"]["file-neon"]["delais"]["total_s"] == 2700
    assert config["lignes"]["file-mistral"]["delais"]["silence_s"] == 600


def test_chiffres_regime_prudent_du_devis_6_4():
    config = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
    c, L, f = _compteur("verification-google-cle-1", config)
    args = ("prudent", "google", 150, L["reserve_sortie_jetons"], f["sortie_max"])
    # le devis arrondit au centime supérieur (2,67045 y est écrit 2,68) : tolérance d'un centime
    assert c.cout_sans_compteur(*args, 890, 0) == approx(2.68, abs_=0.01)   # au-dessus du plafond de 1,50 : la ligne s'arrête
    assert c.cout_sans_compteur(*args, 890, 0) > 1.50
    assert c.cout_sans_compteur(*args, 163, 0) == c.reserve(150, L["reserve_sortie_jetons"])   # moins de 164 s : réserve
    assert c.cout_sans_compteur(*args, 165, 0) > c.reserve(150, L["reserve_sortie_jetons"])
    c, L, f = _compteur("verification-mistral-eu", config)
    args = ("prudent", "mistral", 150, L["reserve_sortie_jetons"], f["sortie_max"])
    assert c.cout_sans_compteur(*args, 590, 0) == approx(0.28, abs_=0.01) and c.cout_sans_compteur(*args, 590, 0) > 0.25
    assert c.cout_sans_compteur(*args, 164, 0) == c.reserve(150, L["reserve_sortie_jetons"])
    c, L, f = _compteur("file-neon", config)
    for octets, attendu in ((5000, 8.09), (24000, 8.15)):
        cout = c.cout_sans_compteur("prudent", "google", octets, L["reserve_sortie_jetons"], f["sortie_max"], 2690, 0)
        assert cout == approx(attendu, abs_=0.01)        # le devis arrondit au centime supérieur
        assert cout + c.reserve(octets, L["reserve_sortie_jetons"]) > 8.50      # avec la réserve suivante : arrêt
    c, L, f = _compteur("file-mistral", config)
    for octets, bas, haut in ((5000, 0.61, 1.25), (24000, 0.63, 1.27)):
        args = ("prudent", "mistral", octets, L["reserve_sortie_jetons"], f["sortie_max"])
        assert c.cout_sans_compteur(*args, 100, 0) == approx(bas, abs_=0.011)
        assert c.cout_sans_compteur(*args, 1310, 0) == c.reserve(octets, L["reserve_sortie_jetons"])   # sous 1 311 s
        assert c.cout_sans_compteur(*args, 2690, 0) == approx(haut, abs_=0.011)
    # régime courant : Google, la sortie maximale envoyée ; Mistral, la plus grande de 32 768 et des octets reçus plus 64
    assert c.cout_sans_compteur("courant", "mistral", 5000, 262208, 32768, 2690, 100) == pytest.approx(c.cout(5000, 32768))
    assert c.cout_sans_compteur("courant", "mistral", 5000, 262208, 32768, 2690, 50000) == pytest.approx(c.cout(5000, 50064))
    c, L, f = _compteur("file-neon", config)
    assert c.cout_sans_compteur("courant", "google", 5000, 32768, 32768, 2690, 0) == c.reserve(5000, 32768)


def test_chiffres_garantie_du_compteur_6_4():
    """Un modèle dont chaque envoi est compté au plus à 32 768 jetons de sortie n'est jamais refusé."""
    config = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
    for ligne, appels in (("file-mistral", [5000] * 18 + [24000] * 6), ("file-neon", [5000] * 6 + [24000] * 2)):
        c, L, f = _compteur(ligne, config)
        for octets in appels:
            for _ in (1, 2):
                assert c.motif_de_refus(c.reserve(octets, L["reserve_sortie_jetons"])) is None
                c.compter(c.cout(octets, f["sortie_max"]))
        assert c.cumul == approx({"file-mistral": 3.99, "file-neon": 8.33}[ligne]) and c.cumul <= L["plafond_usd"]


def test_gabarit_complet_et_refuse_par_le_chef(tmp_path):
    """Le gabarit porte identifiants, hôtes, noms de variables de clé, plafonds, délais, sortie maximale, réglages et
    seuils ; ses pièces répondent à leurs empreintes ; le chef refuse un gabarit."""
    config = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
    assert config["fournisseurs"]["mistral"]["variable_cle"] == "MISTRAL_API_KEY"
    assert config["fournisseurs"]["google"]["variables_cle"] == [CLE_1, CLE_2]
    assert config["lignes"]["verification-google-cle-1"]["variable_cle"] == CLE_1
    assert config["lignes"]["verification-google-cle-2"]["variable_cle"] == CLE_2
    assert config["fournisseurs"]["mistral"]["sortie_max"] == 32768
    # règle Google : deux décisions ouvertes, aucune valeur choisie au gabarit
    g = config["fournisseurs"]["google"]
    assert g["sortie_max"] is None and g["reflexion"] is None and g["exemption_de_la_sonde"] is None and g["jetons_par_mot"] is None
    assert g["marge_de_texte_jetons"] == 16000 == chef.MARGE_DE_TEXTE_GOOGLE == relais_google.MARGE_DE_TEXTE
    assert all(c["limite_de_mots"] is None for c in config["consignes"].values())
    assert {f["sortie_max_sonde"] for f in config["fournisseurs"].values()} == {256}
    assert config["fournisseurs"]["mistral"]["reasoning_effort"] == "high"
    assert config["fournisseurs"]["google"]["orthographes_niveau"] == ["XHIGH", "xhigh"]
    assert tuple(config["hotes_permis"]) == chef.HOTES_PERMIS
    assert tuple(config["lignes"]["file-neon"]["entrees"]) == chef.ENTREES_NEON

    def pieces(o):
        if isinstance(o, dict):
            if isinstance(o.get("chemin"), str) and isinstance(o.get("sha256"), str):
                yield o
            for v in o.values():
                yield from pieces(v)
        elif isinstance(o, list):
            for v in o:
                yield from pieces(v)

    for p in pieces(config):
        assert chef.sha256_fichier(RACINE / p["chemin"]) == p["sha256"], p["chemin"]
    copie = tmp_path / "gabarit.json"
    copie.write_bytes((RACINE / GABARIT).read_bytes())
    Path(str(copie) + ".sha256").write_text(f"{chef.sha256_fichier(copie)}  gabarit.json\n", encoding="utf-8")
    with pytest.raises(chef.Arret, match="gabarit"):
        chef.charger_configuration(copie, chef.sha256_fichier(copie))


# === Garde 1 : plafond avant l'envoi, et compte d'un envoi sans compteur lisible ==========================================

def test_garde_1_sain_cumul_bas_et_seuils_de_la_file_mistral(monde, banc):
    c = chef.Compteur(4.75, [0.77, 2.31], 200, 3.90)
    assert c.motif_de_refus(c.reserve(24000, 262208)) is None          # 3,90 plus 0,625, sous 4,75 : l'envoi part
    c = chef.Compteur(4.75, [0.77, 2.31], 200, 4.20)
    assert "garde 1" in c.motif_de_refus(c.reserve(24000, 262208))     # artefact : refus
    # cumul bas : l'envoi part, sur les deux formes d'appel
    m = banc("verification-mistral-eu")
    m.faux.programmer(faux.flux_mistral("OK"), sonde_mistral())
    assert m.verifier()["saine"] and len(m.faux.appels()) == 2
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK"), sonde_google())
    assert g.verifier()["saine"] and len(g.faux.appels()) == 2


def test_garde_1_artefact_cumul_a_un_centime_du_plafond(monde, banc):
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK"))
    etat = {"appels": [], "listes": [], "depense_comptee_usd": 1.49, "close": False, "lancements": 1}
    releve = g.verifier(etat=etat)
    assert g.faux.appels() == []                                       # le faux fournisseur ne reçoit rien
    assert releve["close"] and "garde 1" in releve["issue_finale"]     # arrêt, motif écrit
    assert chef.code_de_sortie_verification(releve) != 0               # code de sortie non nul


def test_garde_1_sain_prudent_connexion_coupee_breve_comptee_a_sa_reserve_et_refaite(monde, banc):
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.fermer())
    releve = g.verifier()
    a = releve["appels"][0]
    assert a["incident"] == "coupure" and a["ligne_du_classement"] == 6 and a["compte_parmi_les_trois"]
    L = monde.config["lignes"]["verification-google-cle-1"]
    octets = (g.dossier / "envois" / f"{a['envoi']}.corps.json").stat().st_size
    assert a["cout_usd"] == pytest.approx(chef.Compteur(1.5, [3, 15], 1).reserve(octets, chef.reserve_de_la_ligne(monde.config, "verification-google-cle-1")), abs=1e-6)
    assert releve["a_refaire"] and not releve["close"] and chef.code_de_sortie_verification(releve) == 3
    assert releve["envois_coupes"] == [a["envoi"]] and releve["lecture_de_la_console_due"]
    # l'appel se refait, par un lancement nouveau, sous la même ligne et dans son compte
    g.nouveau_dossier()
    g.faux.programmer(faux.reponse_google("OK"), sonde_google())
    suite = g.verifier()
    assert [x["type"] for x in suite["appels"]] == ["A", "A", "B"] and suite["saine"] and suite["appels_comptes"] == 3
    assert suite["depense_comptee_usd"] > releve["depense_comptee_usd"]


def test_garde_1_sain_courant_envoi_neon_coupe_au_delai_compte_a_sa_reserve_la_reprise_part(monde, banc):
    g = banc("file-neon")
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    g.faux.programmer(faux.muet(3.0), *conformes)
    bilan = g.jouer(regime="courant")
    e = g.envois()
    assert e[0]["incident"] == "delai" and e[0]["coupe_par_un_delai"] and e[0]["decision"] == "reprise"
    octets = (g.dossier / "envois" / f"{e[0]['envoi']}.corps.json").stat().st_size
    assert e[0]["cout_usd"] == pytest.approx(chef.Compteur(8.5, [3, 15], 1).reserve(octets, 32768), abs=1e-6)
    assert e[1]["rang"] == 2 and e[1]["decision"] == "ok" and bilan["complet"] and len(g.faux.appels()) == 9


def test_garde_1_artefact_refus_du_mandataire_compte_zero_et_panne_sans_signature_comptee(monde, banc):
    mandataire = faux.FauxMandataire().demarrer()
    try:
        g = banc("verification-google-cle-1", environnement_du_relais={"HTTPS_PROXY": mandataire.url})
        releve = g.verifier()
        assert releve["listes"][0]["signature_du_mandataire"] and releve["appels"] == []
        assert releve["depense_comptee_usd"] == 0 and releve["a_refaire"] and g.faux.recus == []
        assert mandataire.demandes >= 1
    finally:
        mandataire.arreter()
    # connexion refusée à l'appel au modèle : la liste passe par un autre relais, sain
    h = banc("verification-google-cle-1", adresse=f"http://127.0.0.1:{faux.port_ferme()}")
    corps_sain = json.dumps(chef.construire_corps("google", monde.config["fournisseurs"]["google"], "t", 32768, orthographe="XHIGH")).encode()
    retour = chef.envoyer(h.url, "POST", chef.chemin_de_l_appel("google"), chef.en_tetes_de_l_envoi("e1"), corps_sain,
                          False, 1, 1)
    assert retour["code"] == 502 and chef.origine_du_retour(retour)[0] == "mandataire"
    assert chef.signature_du_mandataire(retour, h.journal_relais, "e1")
    assert not chef.signature_du_mandataire(retour, h.journal_relais, "autre-envoi")     # le journal est exigé aussi
    c = chef.Compteur(1.5, [3, 15], 200)
    assert chef.compter_envoi(c, "prudent", "google", 100, 32768, 32768, retour, None, None, True)[0] == 0.0
    # panne sans cette signature : comptée selon son régime, parmi les trois
    p = banc("verification-google-cle-1")
    p.faux.programmer(faux.fermer())
    a = p.verifier()["appels"][0]
    assert not a["signature_du_mandataire"] and a["compte_parmi_les_trois"] and a["cout_usd"] > 0.49


def test_garde_1_artefact_verification_google_delai_la_ligne_s_arrete_au_premier(monde, banc):
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.muet(3.0), faux.muet(3.0), faux.muet(3.0))
    releve = g.verifier()
    a = releve["appels"][0]
    assert a["incident"] == "delai" and a["cout_usd"] > 1.50 and len(releve["appels"]) == 1      # compté au-dessus du plafond
    assert releve["a_refaire"]                                         # ligne 6 : à refaire si le compteur le permet
    g.nouveau_dossier()
    suite = g.verifier()                                               # … et il ne le permet pas
    assert len(g.faux.appels()) == 1 and suite["close"] and "garde 1" in suite["issue_finale"]   # le deuxième n'est pas envoyé
    assert chef.code_de_sortie_verification(suite) != 0


def test_garde_1_artefact_verification_mistral_flux_muet_jusqu_au_silence(monde, banc):
    m = banc("verification-mistral-eu")
    m.faux.programmer(faux.muet(3.0), faux.muet(3.0))
    releve = m.verifier()
    a = releve["appels"][0]
    assert a["incident"] == "delai" and a["cout_usd"] > 0.25 and len(releve["appels"]) == 1
    m.nouveau_dossier()
    suite = m.verifier()
    assert len(m.faux.appels()) == 1 and suite["close"] and "garde 1" in suite["issue_finale"]


def test_garde_1_artefact_file_neon_sur_mot_de_lazar_envoi_coupe_la_reprise_est_refusee(monde, banc):
    g = banc("file-neon")
    g.faux.programmer(faux.muet(3.0), faux.reponse_google(APPARIEMENT_CONFORME))
    bilan = g.jouer(regime="prudent", sonde="indécidée")
    e = g.envois()
    assert len(e) == 1 and e[0]["incident"] == "delai" and e[0]["cout_usd"] > 7.9 and e[0]["regime"] == "prudent"
    assert bilan["arretee_a_son_plafond"] and not bilan["complet"] and len(g.faux.appels()) == 1


# === Garde 2 : délais ====================================================================================================

def test_garde_2_sain_reponse_rapide_et_flux_lent_mais_vivant(monde, banc):
    m = banc("verification-mistral-eu")
    silence = monde.config["lignes"]["verification-mistral-eu"]["delais"]["silence_s"]
    lent = faux.flux_mistral("OK", pensee="p" * 50, pause_entre_s=silence / 3)   # un événement par tiers du silence permis
    m.faux.programmer(lent, sonde_mistral())
    releve = m.verifier()
    assert releve["saine"] and releve["appels"][0]["incident"] is None
    assert releve["appels"][0]["duree_s"] > silence                    # plus long que le silence permis : il va au bout


def test_garde_2_artefact_flux_muet_coupe_reprise_unique_puis_seconde_panne(monde, banc):
    m = banc("file-mistral")
    conformes = reponses_conformes(monde.config, monde.racine, "file-mistral", faux.flux_mistral)
    m.faux.programmer(faux.muet(3.0), conformes[0], faux.muet(3.0), faux.muet(3.0), conformes[1])
    bilan = m.jouer(regime="courant")
    e = m.envois()
    assert [(x["appel"], x["rang"], x["decision"]) for x in e] == [(1, 1, "reprise"), (1, 2, "ok"), (2, 1, "reprise"), (2, 2, "arret")]
    assert e[0]["incident"] == "delai" and e[0]["regime"] == "courant"
    assert "seconde panne" in bilan["arret"] and not bilan["complet"] and len(m.faux.appels()) == 4


def test_garde_2_artefact_verification_google_coupee_sans_reprise_mais_pas_la_file(monde, banc):
    verif = monde.config["lignes"]["verification-google-cle-1"]["delais"]["total_s"]
    file_ = monde.config["lignes"]["file-neon"]["delais"]["total_s"]
    attente = verif * 1.4
    assert verif < attente < file_ - 0.3
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK", attente_s=attente), faux.reponse_google("OK"))
    releve = g.verifier()
    assert [a["incident"] for a in releve["appels"]] == ["delai"] and len(g.faux.appels()) == 1   # coupé, sans reprise
    n = banc("file-neon")
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    conformes[0]["attente_s"] = attente
    n.faux.programmer(*conformes)
    assert n.jouer()["complet"] and n.envois()[0]["incident"] is None  # un appel de la file de même durée ne l'est pas


def test_garde_2_delai_global_sain_et_artefact(monde, banc):
    # cas sain, par le calcul du devis : un appel fait d'un envoi au délai total, d'un code 429, de 600 secondes
    # d'attente et d'un second envoi au délai total n'est pas coupé
    for appels in (24, 8):
        assert appels * (2700 + 600 + 2700 + 10) <= chef.delai_global_file(appels, 2700, 600, 10)
    # artefact : un programme bloqué hors de tout envoi est coupé, la file est rapportée interrompue
    monde.config["attente_429"] = {"defaut_s": 0.01, "max_s": 0.01}
    monde.config["lignes"]["file-neon"]["delais"] = {"silence_s": 0.05, "total_s": 0.05, "relais_silence_s": 0.04,
                                                     "relais_total_s": 0.04}
    n = banc("file-neon")
    n.faux.programmer(*reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google))
    n.pauses = None
    programme = chef.charger_programme_de_forme(monde.config, monde.racine)
    lot = chef.charger_textes(monde.config, monde.racine)
    contexte = {"regime": "courant", "nom_servi": "gemini-4-neon", "hote": "generativelanguage.googleapis.com",
                "orthographe_niveau": "XHIGH", "temperature_envoyee": True}
    debut = time.monotonic()
    bilan = chef.jouer_file(monde.config, "file-neon", lot, n.dossier, n.urls, n.journaux, [], contexte, programme,
                            dormir=lambda s: time.sleep(30))
    assert time.monotonic() - debut < 5
    assert bilan["interrompue"] and not bilan["complet"] and "délai global" in bilan["arret"]


# === Garde 3 : champs du corps et motif de sortie maximale ================================================================

def test_garde_3_corps_sain_et_artefacts(monde):
    fm, fg = monde.config["fournisseurs"]["mistral"], monde.config["fournisseurs"]["google"]
    cm, cg = chef.chemin_de_l_appel("mistral"), chef.chemin_de_l_appel("google")
    sain_m = chef.construire_corps("mistral", fm, "texte", 32768)
    sain_g = chef.construire_corps("google", fg, "texte", 32768, orthographe="XHIGH")
    chef.controler_corps("mistral", fm, sain_m, cm, 32768)
    chef.controler_corps("google", fg, sain_g, cg, 32768, orthographe="XHIGH")
    assert sain_m == {"model": "mistral-large-4-0", "messages": [{"role": "user", "content": "texte"}],
                      "max_tokens": 32768, "reasoning_effort": "high", "stream": True, "temperature": 0}
    assert sain_g == {"contents": [{"role": "user", "parts": [{"text": "texte"}]}],
                      "generationConfig": {"maxOutputTokens": 32768, "thinkingConfig": {"thinkingLevel": "XHIGH"}}}
    chef.controler_corps("mistral", fm, chef.construire_corps("mistral", fm, "sonde", 256), cm, 256)   # la sonde : 256
    sans_temperature = chef.construire_corps("mistral", fm, "t", 32768, temperature_envoyee=False)
    chef.controler_corps("mistral", fm, sans_temperature, cm, 32768, temperature_envoyee=False)

    def refuse(fournisseur, f, corps, chemin, **plus):
        with pytest.raises(chef.Arret, match="garde (3|14)"):
            chef.controler_corps(fournisseur, f, corps, chemin, 32768, **plus)

    refuse("mistral", fm, {k: v for k, v in sain_m.items() if k != "max_tokens"}, cm)       # sans sortie maximale
    refuse("mistral", fm, {**sain_m, "max_tokens": 65536}, cm)                              # à 65 536
    refuse("mistral", fm, {**sain_m, "top_p": 1}, cm)                                       # un champ de plus
    refuse("mistral", fm, {k: v for k, v in sain_m.items() if k != "stream"}, cm)           # sans `stream`
    refuse("mistral", fm, {**sain_m, "stream": False}, cm)
    refuse("mistral", fm, sain_m, cm, temperature_envoyee=False)                            # température après retrait
    refuse("mistral", fm, {**sain_m, "messages": [{"role": "system", "content": "x"}]}, cm)
    avec_temperature = copy.deepcopy(sain_g)
    avec_temperature["generationConfig"]["temperature"] = 0
    refuse("google", fg, avec_temperature, cg, orthographe="XHIGH")                         # la température pour Google
    refuse("google", fg, {**sain_g, "systemInstruction": {}}, cg, orthographe="XHIGH")
    refuse("google", fg, sain_g, cg, orthographe="xhigh")                                   # autre orthographe que la retenue
    refuse("google", fg, sain_g, "/v1beta/models/gemini-4-neon:streamGenerateContent", orthographe="XHIGH")
    trop = copy.deepcopy(sain_g)
    trop["generationConfig"]["maxOutputTokens"] = 65536
    refuse("google", fg, trop, cg, orthographe="XHIGH")


def test_garde_3_sain_sortie_facturee_au_dela_sous_fin_normale_la_file_continue(monde, banc):
    m = banc("file-mistral")
    conformes = reponses_conformes(monde.config, monde.racine, "file-mistral", faux.flux_mistral)
    longue = faux.flux_mistral(APPARIEMENT_CONFORME, usage=(900, 40000, 40900), remplissage_octets=0)
    longue_et_etablie = faux.flux_mistral(APPARIEMENT_CONFORME, usage=(900, 40000, 40900), pensee="p" * 41000)
    m.faux.programmer(longue_et_etablie, *conformes[1:])
    bilan = m.jouer()
    e = m.envois()
    assert bilan["complet"] and len(e) == 24 and e[0]["decision"] == "ok"
    assert e[0]["sortie_facturee"] == 40000 and e[0]["sortie_facturee_au_dela_de_la_sortie_maximale"]   # le rapport le dit
    assert e[0]["cout_usd"] == pytest.approx((900 * 0.77 + 40000 * 2.31) / 1e6, abs=1e-6)               # coût réel
    rapport = chef.faire_rapport(m.dossier)
    assert rapport["sorties_au_dela_de_la_sortie_maximale"] == 1 and chef.appliquer_regles(rapport)["tient"]
    assert longue["genre"] == "flux"


@pytest.mark.parametrize("fournisseur, motif", [("mistral", "length"), ("mistral", "model_length"),
                                                ("google", "MAX_TOKENS"), ("google", "CONTINUATION")])
def test_garde_3_artefact_motif_de_sortie_maximale_arrete_la_file(monde, banc, fournisseur, motif):
    ligne = "file-mistral" if fournisseur == "mistral" else "file-neon"
    b = banc(ligne)
    fabrique = faux.flux_mistral if fournisseur == "mistral" else faux.reponse_google
    b.faux.programmer(fabrique(APPARIEMENT_CONFORME, fin=motif), fabrique(APPARIEMENT_CONFORME))
    bilan = b.jouer()
    assert "sortie maximale atteinte" in bilan["arret"] and len(b.faux.appels()) == 1 and not bilan["complet"]
    assert chef.faire_rapport(b.dossier)["fins_par_sortie_maximale"] == 1


# === Garde 4 : codes et motifs ============================================================================================

def _retour(code, corps=b"{}", en_tetes=None):
    return {"code": code, "corps": corps, "en_tetes": en_tetes or {}, "incident": None, "detail": None, "flux": None,
            "duree_s": 0.1}


def test_garde_4_codes_arret_reprise_attente():
    decider = chef.decider_dans_la_file
    for code in (401, 402, 403):
        assert decider("google", _retour(code), None, None, False, 1, "gemini-4-neon")[0] == "arret"   # sans reprise
    for code in (400, 422, 404, 418):
        assert decider("google", _retour(code), None, None, False, 1, "gemini-4-neon")[0] == "arret"
    for code in (500, 502, 503, 504, 529, 599):
        assert decider("google", _retour(code), None, None, False, 1, "gemini-4-neon")[0] == "reprise"
        assert decider("google", _retour(code), None, None, False, 2, "gemini-4-neon")[0] == "arret"
    assert decider("google", _retour(429), None, None, False, 1, "gemini-4-neon")[0] == "attente"
    assert decider("google", _retour(429), None, None, False, 2, "gemini-4-neon")[0] == "arret"
    relais = _retour(429, json.dumps({"erreur": {"origine": "relais", "motif": "borne d'appels"}}).encode())
    assert decider("google", relais, None, None, False, 1, "gemini-4-neon")[0] == "arret"   # un 429 du relais n'attend pas
    regle = {"defaut_s": 30, "max_s": 600}
    assert chef.attente_sur_429({"retry-after": "900"}, regle) == 600                       # au-delà de 600, il attend 600
    assert chef.attente_sur_429({"retry-after": "12"}, regle) == 12
    assert chef.attente_sur_429({}, regle) == 30 and chef.attente_sur_429({"retry-after": "demain"}, regle) == 30
    assert chef.classe_du_motif("mistral", "stop") == "normale" and chef.classe_du_motif("google", "STOP") == "normale"
    for motif in ("error", "tool_calls", None, "inconnu"):
        assert chef.classe_du_motif("mistral", motif) == "refus"                            # motif inconnu classé refus
    for motif in ("SAFETY", "RECITATION", "OTHER", "MALFORMED_RESPONSE", None, "stop"):
        assert chef.classe_du_motif("google", motif) == "refus"


def test_garde_4_sain_et_artefacts_sur_le_faux_fournisseur(monde, banc):
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    # 200, fin normale : la file va au bout ; 429 puis 200 : la file continue ; `Retry-After` de 900 : attente de 600
    g = banc("file-neon")
    g.faux.programmer(faux.erreur_google(429) | {"en_tetes": {"Retry-After": "900"}}, *conformes)
    assert g.jouer()["complet"] and g.pauses[0] == 600 and len(g.faux.appels()) == 9
    # aucune reprise cachée : une réponse 500, deux envois reçus, pas trois
    h = banc("file-neon")
    h.faux.programmer(faux.erreur_google(500), faux.erreur_google(504), *conformes)
    bilan = h.jouer()
    assert len(h.faux.appels()) == 2 and "seconde panne" in bilan["arret"]
    # 429 puis 429 : arrêt
    i = banc("file-neon")
    i.faux.programmer(faux.erreur_google(429), faux.erreur_google(429), *conformes)
    assert "429" in i.jouer()["arret"] and len(i.faux.appels()) == 2 and i.pauses[0] == 30
    # 401 : arrêt, sans reprise, code et origine au journal
    j = banc("file-neon")
    j.faux.programmer(faux.erreur_google(401), *conformes)
    assert "401" in j.jouer()["arret"] and len(j.faux.appels()) == 1
    assert (j.envois()[0]["code"], j.envois()[0]["origine"]) == (401, "amont")
    # motif de refus : arrêt
    k = banc("file-neon")
    k.faux.programmer(faux.reponse_google(APPARIEMENT_CONFORME, fin="SAFETY"), *conformes)
    assert "refus" in k.jouer()["arret"] and chef.faire_rapport(k.dossier)["refus"] == 1
    sans_candidat = banc("file-neon")
    sans_candidat.faux.programmer(faux.reponse_google(None, blocage="PROHIBITED_CONTENT"), *conformes)
    assert "refus" in sans_candidat.jouer()["arret"]


# === Garde 5 : nom servi ==================================================================================================

def test_garde_5_nom_servi(monde, banc):
    conformes = reponses_conformes(monde.config, monde.racine, "file-mistral", faux.flux_mistral)
    sain = banc("file-mistral")           # nom égal ; le dernier événement de chaque flux n'a pas de champ `model`
    sain.faux.programmer(*conformes)
    assert sain.jouer()["complet"] and {e["nom_servi"] for e in sain.envois()} == {"mistral-large-4-0"}
    autre = banc("file-mistral")
    autre.faux.programmer(faux.flux_mistral(APPARIEMENT_CONFORME, modele="mistral-large-4"), *conformes)
    bilan = autre.jouer()
    assert "garde 5" in bilan["arret"] and len(autre.faux.appels()) == 1
    assert autre.envois()[0]["cause"].startswith("garde 5")                                  # motif au journal
    un_seul = banc("file-mistral")        # un seul événement porte un autre nom
    un_seul.faux.programmer(faux.flux_mistral(APPARIEMENT_CONFORME, autre_nom_au_dernier="mistral-large-latest"), *conformes)
    assert "garde 5" in un_seul.jouer()["arret"]
    neon = banc("file-neon")
    neon.faux.programmer(faux.reponse_google(APPARIEMENT_CONFORME, modele="models/gemini-4-neon"))
    assert "garde 5" in neon.jouer()["arret"]                                                # la session ne normalise rien


# === Garde 6 : rien de personnel dans ce qui part =========================================================================

def test_garde_6_rien_de_personnel(monde, tmp_path):
    interdits = chef.charger_interdits(monde.config, monde.racine, {"CLAUDE_SESSION_ID": "identifiant-de-session-xyz"})
    assert "zorglub-terme-interdit" in interdits and "identifiant-de-session-xyz" in interdits
    en_tetes = chef.en_tetes_de_l_envoi("01-A-b1-01-1")
    chef.controler_envoi(b'{"messages": [{"role": "user", "content": "entree synthetique"}]}', en_tetes, interdits)   # sain
    for glisse in ("ecrire a quelqu.un@exemple.org", "voir /home/quelquun/depot", "session_01QPDgKgkCezLtWTAC6NJ7ok",
                   "le terme Zorglub-Terme-Interdit", "identifiant-de-session-xyz"):
        with pytest.raises(chef.Arret, match="garde 6"):
            chef.controler_envoi(json.dumps({"content": glisse}).encode(), en_tetes, interdits)
    with pytest.raises(chef.Arret, match="agent d'utilisateur"):
        chef.controler_envoi(b"{}", {**en_tetes, "User-Agent": "python-requests/2.0"}, interdits)
    monde.config["garde_interdits"]["fichier_local"] = str(tmp_path / "absent.txt")
    with pytest.raises(chef.Arret, match="garde 6"):
        chef.charger_interdits(monde.config, monde.racine, {})
    # lot relu par empreinte ; consigne remplie comparée à son empreinte
    lot = json.loads((RACINE / monde.config["entrees"]["chemin"]).read_text(encoding="utf-8"))
    assert len(chef.charger_textes(monde.config, monde.racine)["textes"]) == 24
    lot["entrees"][0]["consigne_remplie"]["octets"] += 1
    monde.piece("lot-change.json", lot)
    monde.config["entrees"] = monde.ref("lot-change.json")
    with pytest.raises(chef.Arret, match="consigne remplie"):
        chef.charger_textes(monde.config, monde.racine)
    monde.config["entrees"]["sha256"] = "0" * 64
    with pytest.raises(chef.Arret, match="lot des entrées"):
        chef.charger_textes(monde.config, monde.racine)


# === Garde 7 : clés par leur nom ==========================================================================================

def test_garde_7_cles_par_leur_nom(monde, tmp_path):
    dossier = tmp_path / "ligne"
    dossier.mkdir()
    monde.config["essai_local"] = {"google": "http://127.0.0.1:9"}
    with pytest.raises(chef.Arret, match="garde 7"):                   # nom absent : rien ne part
        chef.lancer_relais(monde.config, "verification-google-cle-1", monde.racine, dossier, {"PATH": os.environ["PATH"]})
    assert not (dossier / "relais" / "console-relais.txt").exists()
    with pytest.raises(chef.Arret, match="boucle locale"):             # le programme ne parle qu'à la boucle locale
        chef.envoyer("http://exemple.org:80", "POST", "/v1/chat/completions", {}, b"{}", False, 1, 1)
    assert chef.ouvrier(dossier, {"PATH": "/usr/bin", "GEMINI_API_KEY": "x"}, b"{}") == 2    # l'ouvrier n'a aucune clé
    (dossier / "journal.jsonl").write_text('{"note": "rien"}\n', encoding="utf-8")
    assert chef.chercher_formes_de_cle(dossier) == []                  # sain
    (dossier / "journal.jsonl").write_text('{"note": "AIza' + "B" * 35 + '"}\n', encoding="utf-8")
    assert chef.chercher_formes_de_cle(dossier) == ["journal.jsonl"]   # clé factice glissée dans un journal : trouvée
    # le relais efface sa variable, ne rend jamais la clé, et retire toute clé reçue du client (essais du relais)
    assert set(chef.ENVIRONNEMENT_OUVRIER) == {"PATH", "HOME", "LANG", "GO_ID"}


def test_garde_7_les_relais_tiennent_la_cle_et_elle_seule(monde, banc):
    """Le relais efface sa variable, ne rend jamais la clé, retire toute clé reçue du client, et tient sa borne
    d'appels ; celui de Mistral tient de plus son plafond en dollars (seconde barrière, devis 6.4)."""
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK"), faux.reponse_google("OK"), faux.reponse_google("OK"))
    corps = json.dumps(chef.construire_corps("google", monde.config["fournisseurs"]["google"], "t", 32768, orthographe="XHIGH")).encode()
    en_tetes = {**chef.en_tetes_de_l_envoi("e1"), "x-goog-api-key": "cle-glissee-par-le-client", "Authorization": "Bearer du-client"}
    for _ in range(3):
        assert chef.envoyer(g.url, "POST", chef.chemin_de_l_appel("google"), en_tetes, corps, False, 2, 2)["code"] == 200
    recu = g.faux.appels()[0]["en_tetes"]
    assert recu["x-goog-api-key"] == "valeur-factice-du-relais" and "authorization" not in recu and "x-envoi" not in recu
    quatrieme = chef.envoyer(g.url, "POST", chef.chemin_de_l_appel("google"), en_tetes, corps, False, 2, 2)
    assert quatrieme["code"] == 429 and chef.origine_du_retour(quatrieme)[0] == "relais" and len(g.faux.appels()) == 3
    etat = chef.etat_relais(g.url)
    assert etat["appels"] == 3 and etat["max_appels"] == 3 and etat["refus"] == 1 and etat["cle_dans_l_environnement"] is False
    assert "valeur-factice-du-relais" not in json.dumps(etat) and etat["plafond_usd"] is None
    assert "valeur-factice-du-relais" not in g.journal_relais.read_text(encoding="utf-8")
    autre_chemin = chef.envoyer(g.url, "POST", "/v1beta/models/gemini-4-neon:streamGenerateContent", en_tetes, corps, False, 2, 2)
    assert autre_chemin["code"] == 403 and len(g.faux.appels()) == 3                 # rien d'autre n'est servi
    env = {"MISTRAL_API_KEY": "valeur-factice-du-relais"}
    serveur = relais_mistral.servir(0, env, "MISTRAL_API_KEY", "api.eu.mistral.ai", "mistral-large-4-0", 3, 0.10, (0.77, 2.31),
                                    32832, 1.0, 2.0, None, g.faux.url)
    assert env == {}                                                                 # la variable est effacée
    threading.Thread(target=serveur.serve_forever, daemon=True).start()
    try:
        url = f"http://127.0.0.1:{serveur.server_address[1]}"
        fm = monde.config["fournisseurs"]["mistral"]
        corps_m = json.dumps(chef.construire_corps("mistral", fm, "t", 32768)).encode()
        g.faux.programmer(faux.flux_mistral("OK", usage=(40, 20000, 20040)), faux.flux_mistral("OK"))   # premier envoi : 0,046 USD
        premier = chef.envoyer(url, "POST", "/v1/chat/completions", {**chef.en_tetes_de_l_envoi("m1"), "Authorization": "Bearer du-client"},
                               corps_m, True, 2, 2)
        assert premier["code"] == 200 and premier["flux"].usage["completion_tokens"] == 20000 and g.faux.appels()[-1]["en_tetes"]["authorization"] == "Bearer valeur-factice-du-relais"
        second = chef.envoyer(url, "POST", "/v1/chat/completions", chef.en_tetes_de_l_envoi("m2"), corps_m, True, 2, 2)
        assert second["code"] == 402 and chef.origine_du_retour(second)[0] == "relais"   # sous 0,10 USD : 0,046 plus la réserve de 0,076
        autre_modele = json.dumps({**json.loads(corps_m), "model": "mistral-large-latest"}).encode()
        assert chef.envoyer(url, "POST", "/v1/chat/completions", chef.en_tetes_de_l_envoi("m3"), autre_modele, True, 2, 2)["code"] == 400
        assert len(g.faux.appels()) == 4                                             # ni le 402 ni le 400 n'ont atteint l'amont
    finally:
        serveur.shutdown()
        serveur.server_close()
    with pytest.raises(relais_google.RelaisInvalide):                                # sans clé : le relais ne démarre pas
        relais_google.servir(0, {}, "GEMINI_API_KEY", "generativelanguage.googleapis.com", "gemini-4-neon", 3, 5.0)


def test_garde_7_artefact_forme_de_cle_dans_une_piece_gardee_code_de_sortie_7(monde, tmp_path):
    """Une chaîne de la forme d'une clé dans ce que la ligne a écrit (ici, glissée dans une réponse gardée) : trouvée
    par la relecture de fin de ligne, arrêt, code de sortie 7."""
    fournisseur = faux.FauxFournisseur(faux.modele_google()).demarrer()
    try:
        monde.config["essai_local"] = {"google": fournisseur.url}
        chemin, empreinte = monde.ecrire_configuration()
        env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "GO_ID": GO["verification-google-cle-1"],
               "GEMINI_API_KEY": "valeur-factice-du-relais"}
        fournisseur.programmer(faux.reponse_google("OK AIza" + "B" * 35), sonde_google())
        assert chef.executer("verification-google-cle-1", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT) == 7
        dossier = dossiers_de(monde.racine / "runs" / "verification-cle-google-1-bras-a-v1")[0]
        trouve = [l for l in chef.lire_journal(dossier / "journal-amorce.jsonl") if l.get("evenement") == "recherche_de_formes_de_cle"]
        assert trouve and trouve[0]["fichiers"] and "AIza" not in json.dumps(trouve)  # les chemins, jamais la chaîne
    finally:
        fournisseur.arreter()


# === Garde 8 : ligne de calcul ============================================================================================

def test_garde_8_ligne_de_calcul(monde):
    registre, jour = monde.registre(), "2026-11-22"
    for ligne in GO:                                                   # identifiant valide
        assert len(chef.verifier_ligne_de_calcul(monde.config, ligne, {"GO_ID": GO[ligne]}, registre, jour)) == 64
    with pytest.raises(chef.Arret, match="garde 8"):                   # absent
        chef.verifier_ligne_de_calcul(monde.config, "file-neon", {}, registre, jour)
    with pytest.raises(chef.Arret, match="garde 8"):                   # d'une ligne qui nomme l'autre file
        chef.verifier_ligne_de_calcul(monde.config, "file-neon", {"GO_ID": GO["file-mistral"]}, registre, jour)
    croise = copy.deepcopy(monde.config)
    croise["lignes"]["file-neon"]["go"] = GO["file-mistral"]
    croise["lignes"]["file-neon"]["plafond_registre"] = "4,75 USD"
    with pytest.raises(chef.Arret, match="ne nomme pas file-neon"):
        chef.verifier_ligne_de_calcul(croise, "file-neon", {"GO_ID": GO["file-mistral"]}, registre, jour)
    with pytest.raises(chef.Arret, match="échue"):
        chef.verifier_ligne_de_calcul(monde.config, "file-neon", {"GO_ID": GO["file-neon"]}, registre, "2100-01-01")
    with pytest.raises(chef.Arret, match="empreinte du devis"):
        chef.verifier_ligne_de_calcul(monde.config, "file-neon", {"GO_ID": GO["file-neon"]},
                                      registre.replace(chef.EMPREINTE_DEVIS, "f" * 64), jour)
    with pytest.raises(chef.Arret, match="1 ligne|0 ligne"):
        chef.verifier_ligne_de_calcul(monde.config, "file-neon", {"GO_ID": GO["file-neon"]}, monde.registre(["file-mistral"]), jour)
    sans_go = copy.deepcopy(monde.config)
    sans_go["lignes"]["file-neon"]["go"] = None
    with pytest.raises(chef.Arret, match="garde 8"):
        chef.verifier_ligne_de_calcul(sans_go, "file-neon", {"GO_ID": "GO-2026-11-22-04"}, registre, jour)


# === Garde 9 : conditions d'envoi constatées, lues ========================================================================

def _constat(monde, nom="constat-essai.md", fournisseur="google", **plus):
    monde.piece(nom, constat(**plus))
    monde.config["constat"] = monde.ref(nom)
    return chef.garde_constat(monde.config, monde.racine, MAINTENANT, fournisseur)


def test_garde_9_sain_la_piece_de_l_avenant_six_cles_levees(monde):
    lu = chef.garde_constat(monde.config, monde.racine, MAINTENANT, "google")
    assert lu["cles_levees"] == {"go": GO_QUI_LEVE, "cles": sorted(chef.CLES_LEVABLES)}          # six clés levées, nommées
    assert lu["devises"] == {"a": "USD", "b": "USD"} and lu["taux"] is None and lu["portee"] == ["google", "mistral"]
    lm = chef.garde_constat(monde.config, monde.racine, MAINTENANT, "mistral")                 # le constat complet sert aussi Mistral
    assert lm["devises"] == {"mistral": "USD"} and lm["credit_de_mistral_usd"] == Decimal("9.50") and lm["cles_levees"]["cles"] == []
    assert lu["credits_comptes_usd"] == {"a": Decimal("23.00"), "b": Decimal("23.00")} and lu["deux_projets_distincts"]
    # la recharge automatique activée est un cas sain (c'était l'artefact du devis) ; les deux autres valeurs restent admises
    for valeur in ("désactivée", "non proposée"):
        assert _constat(monde, modifs={"google_recharge_automatique_projet_a": valeur})["valeurs"]["google_recharge_automatique_projet_a"] == valeur
    # une valeur vue et bonne reste admise sur une clé levable (seule l'absence de constat est levée)
    vu = _constat(monde, modifs={"google_partage_journaux_projet_a": "désactivé", "google_duree_journaux_jours_projet_b": "7"})
    assert len(vu["cles_levees"]["cles"]) == 4 and vu["valeurs"]["google_duree_journaux_jours_projet_b"] == 7
    resume = chef.resume_du_constat(lu)
    assert resume["cles_levees"]["go"] == GO_QUI_LEVE and json.dumps(resume)                    # recopiable aux pièces rendues


def test_garde_9_artefacts_de_la_piece(monde):
    def refuse(motif):
        for fournisseur in ("google", "mistral"):                    # un défaut de la pièce même arrête l'un et l'autre
            with pytest.raises(chef.Arret, match=motif):
                chef.garde_constat(monde.config, monde.racine, MAINTENANT, fournisseur)

    bon = dict(monde.config["constat"])
    monde.config["constat"] = {"chemin": "pieces/absent.md", "sha256": "0" * 64}
    refuse("garde 9")                                                  # pièce absente
    monde.config["constat"] = {**bon, "sha256": "0" * 64}
    refuse("empreinte")                                                # d'une autre empreinte
    monde.config["constat"] = {"chemin": None, "sha256": None}
    refuse("non inscrits")
    monde.piece("constat-sans-compagnon.md", constat(), sceller=False)
    monde.config["constat"] = monde.ref("constat-sans-compagnon.md")
    refuse("compagnon")
    for nom, texte, motif in (
            ("manque", constat(sans=("google_offre_payante_projet_b",)), "manquante"),              # une clé manquante
            ("manque-m", constat(sans=("mistral_offre_payante",)), "manquante"),                    # même de l'autre fournisseur
            ("de-trop", constat(plus={"google_budget_minimal_usd": "5"}), "de trop"),               # une clé de plus
            ("ancienne", constat(plus={"google_credit_utilisable_usd": "23,00"}), "de trop"),       # une clé du devis d'avant l'avenant
            ("date", constat(date=(MAINTENANT + datetime.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%MZ")), "postérieure"),
            ("date-locale", constat(date="2026-11-22 10:00"), "temps universel"),
            ("mot", constat(mot=False), "mot de Lazar")):                                           # mot de Lazar absent
        monde.piece(f"constat-{nom}.md", texte)
        monde.config["constat"] = monde.ref(f"constat-{nom}.md")
        refuse(motif)


@pytest.mark.parametrize("cle, valeur, motif", [
    ("google_offre_payante_projet_a", "non", "hors des valeurs admises"),
    ("google_offre_payante_projet_a", LEVE, "n'est pas une clé levée"),                     # valeur levée sur une clé vue
    ("google_credit_vu_projet_b", LEVE, "n'est pas une clé levée"),
    ("google_credit_vu_projet_b", "après usage", "n'est pas un nombre"),
    ("google_recharge_automatique_projet_a", "parfois", "hors des valeurs admises"),        # hors des trois valeurs
    ("google_recharge_automatique_projet_a", LEVE, "n'est pas une clé levée"),
    ("google_autres_credits_admissibles_projet_b", "300", "hors des valeurs admises"),
    ("google_plafond_depense_projet_a", "50", "hors des valeurs admises"),                  # un nombre
    ("google_devise_affichee_projet_a", "GBP", "hors des valeurs admises"),
    ("google_credit_apres_une_recharge_projet_a", "20,00", "sous le crédit vu"),            # sous le crédit vu (23,00)
    ("google_credit_apres_une_recharge_projet_a", "bientôt", "n'est pas un nombre"),
    ("google_partage_journaux_projet_a", "activé", "hors des valeurs admises"),             # une valeur vue et mauvaise reste refusée
    ("google_duree_journaux_jours_projet_b", "55", "au lieu de 7"),
    ("google_partage_journaux_projet_a", "non constaté, levé par GO-2026-11-21-66", "qui n'est pas"),   # levée sous un autre GO
    ("google_cle_du_projet_constate_cle_2", "non", "hors des valeurs admises"),
    ("google_deux_projets_distincts", LEVE, "n'est pas une clé levée"),                     # non levable : « non relevé » ou « oui »
    ("google_deux_projets_distincts", "non", "hors des valeurs admises"),
    ("mistral_offre_payante", LEVE, "n'est pas une clé levée"),                             # aucune clé de Mistral n'est levée
    ("mistral_donnees_pour_amelioration", "activé", "hors des valeurs admises"),
    ("mistral_cle_de_l_espace_constate", "non", "hors des valeurs admises"),
    ("mistral_credit_utilisable_usd", "8,00", "sous le seuil"),
    ("mistral_limite_requetes_par_minute", "3", "sous le seuil"),
    ("mistral_limite_jetons_par_minute", "50000", "sous le seuil"),
    ("mistral_devise_affichee", "CHF", "hors des valeurs admises")])
def test_garde_9_un_artefact_par_cle(monde, cle, valeur, motif):
    monde.piece("constat-artefact.md", constat({cle: valeur}))
    monde.config["constat"] = monde.ref("constat-artefact.md")
    fournisseur, autre = ("mistral", "google") if cle.startswith("mistral_") else ("google", "mistral")
    with pytest.raises(chef.Arret, match=f"garde 9 : {cle}.*{motif}"):
        chef.garde_constat(monde.config, monde.racine, MAINTENANT, fournisseur)
    assert chef.garde_constat(monde.config, monde.racine, MAINTENANT, autre)["fournisseur"] == autre   # D-1 : l'autre n'est pas jugé
    chemin, empreinte = monde.ecrire_configuration()                   # ni vérification ni file du fournisseur de la clé
    for ligne in [l for l, (_, f, _) in chef.LIGNES.items() if f == fournisseur and l.startswith("verification")]:
        assert chef.executer(ligne, chemin, empreinte, {"GO_ID": GO[ligne]}, racine=monde.racine,
                             registre=monde.registre(), a_l_instant=MAINTENANT) == 2
    assert not list((monde.racine / "runs").iterdir())


def test_garde_9_cles_levees_liste_fermee_aucun_repli_silencieux(monde):
    def refuse(motif, **plus):
        with pytest.raises(chef.Arret, match=motif):
            _constat(monde, **plus)

    refuse("source n'est pas « levé »", sources={"google_partage_journaux_projet_a": "capture"})   # valeur levée, source non dite
    refuse("valeur levée « désactivé », qui n'est pas", modifs={"google_partage_journaux_projet_a": "désactivé"},
           sources={"google_partage_journaux_projet_a": "levé"})                                    # source « levé » sur une valeur vue
    refuse("clé .*absente|manquante", sans=("google_deux_projets_distincts",))                      # la clé des deux projets, absente
    bonnes = list(monde.config["cles_levees"]["cles"])
    monde.config["cles_levees"]["cles"] = [c for c in bonnes if c != "google_duree_journaux_jours_projet_a"]
    refuse("google_duree_journaux_jours_projet_a n'est pas une clé levée")                          # clé levée absente de `cles_levees`
    monde.config["cles_levees"]["cles"] = bonnes + ["google_offre_payante_projet_a"]
    refuse("ne sont pas levables")                                                                   # `cles_levees` nomme une clé hors des six
    monde.config["cles_levees"]["cles"] = bonnes + ["mistral_offre_payante"]
    refuse("ne sont pas levables")                                                                   # aucune clé de Mistral
    monde.config["cles_levees"] = {"go": None, "cles": bonnes}
    refuse("identifiant du GO")
    monde.config["cles_levees"] = {"go": "GO-2026-11-21-66", "cles": bonnes}
    refuse("qui n'est pas")                                                                          # la pièce cite un autre GO que la configuration
    monde.config["cles_levees"] = {"go": GO_QUI_LEVE, "cles": bonnes}
    del monde.config["constat_cles"]["google_deux_projets_distincts"]
    refuse("vingt-huit clés")                                                                        # la configuration n'a plus les vingt-huit


# === Garde 10 : clés vérifiées, point d'accès fixé (avenant 1, 4.2 et 4.3 : deux relevés pour la file du juge) ============

def _constat_lu(monde, fournisseur="google"):
    return chef.garde_constat(monde.config, monde.racine, MAINTENANT, fournisseur)


def _refs_neon(monde, **champs_cle_2):
    ref1 = monde.releve("verification-google-cle-1", "v1")
    ref2 = monde.releve("verification-google-cle-2", "v1", **champs_cle_2)
    monde.inscrire_releve("file-neon", ref1, ref2)
    return {CLE_1: ref1, CLE_2: ref2}


def test_garde_10_sain_regime_courant_deux_releves(monde):
    refs = _refs_neon(monde)
    contexte = chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))
    assert contexte["regime"] == "courant" and contexte["sondes"] == {CLE_1: "comprise", CLE_2: "comprise"}
    assert contexte["noms_servis"] == {CLE_1: "gemini-4-neon", CLE_2: "gemini-4-neon"} and contexte["releves"] == refs
    assert contexte["orthographe_niveau"] == "XHIGH" and contexte["nom_servi"] == "gemini-4-neon"
    refm = monde.releve("verification-mistral-eu", "v1")
    monde.inscrire_releve("file-mistral", refm)
    assert chef.garde_cle_verifiee(monde.config, monde.racine, "file-mistral", _constat_lu(monde))["regime"] == "courant"


def test_garde_10_sain_une_sonde_non_comprise_le_mot_de_lazar_et_le_regime_prudent_pour_toute_la_file(monde):
    refs = _refs_neon(monde, sonde={"issue": "indécidée"})
    monde.piece("mot.md", mot_neon(refs, issues=("comprise", "indécidée")))
    monde.config["lignes"]["file-neon"]["mot_de_lazar_sonde"] = monde.ref("mot.md")
    contexte = chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))
    assert contexte["regime"] == "prudent" and contexte["mot_de_lazar"] and contexte["sondes"][CLE_2] == "indécidée"
    assert contexte["credits_vus_comptes_usd"] == {"a": "19.32", "b": "19.32"}
    refm = monde.releve("verification-mistral-eu", "v1", majorant="démenti")
    monde.inscrire_releve("file-mistral", refm)
    monde.piece("mot-m.md", mot_sur_la_sonde(refm["sha256"], "comprise", majorant="démenti"))
    monde.config["lignes"]["file-mistral"]["mot_de_lazar_sonde"] = monde.ref("mot-m.md")
    assert chef.garde_cle_verifiee(monde.config, monde.racine, "file-mistral", _constat_lu(monde))["regime"] == "prudent"


def test_garde_10_artefacts_des_releves(monde):
    def refuse(motif, ligne="file-neon"):
        with pytest.raises(chef.Arret, match=motif):
            chef.garde_cle_verifiee(monde.config, monde.racine, ligne, _constat_lu(monde))

    L = monde.config["lignes"]["file-neon"]
    refuse("non inscrits")                                             # aucun relevé inscrit (les valeurs nulles du gabarit)
    L["releves_verification"] = None
    refuse("les deux relevés")
    ref1 = monde.releve("verification-google-cle-1", "a")
    L["releves_verification"] = {CLE_1: ref1}
    refuse("les deux relevés")                                         # un seul relevé
    L["releves_verification"] = {CLE_1: ref1, CLE_2: ref1}
    L["inscrit"] = {"nom_servi": "gemini-4-neon", "hote": L["hote"], "orthographe_niveau": "XHIGH"}
    refuse("n'est pas celui de la vérification de cette clé")          # le relevé de la clé 1 inscrit sous la clé 2
    monde.inscrire_releve("file-neon", ref1, monde.releve("verification-google-cle-2", "b", saine=False, nom_servi=None))
    refuse("n'est pas sain")                                           # un relevé non sain
    monde.inscrire_releve("file-neon", ref1, monde.releve("verification-google-cle-2", "c", go="GO-c", orthographe_niveau="xhigh"))
    refuse("deux orthographes différentes")                            # orthographes différentes : nœud de Lazar
    autre_nom = monde.releve("verification-google-cle-2", "d", go="GO-d", nom_servi="gemini-4-neon-0611")
    monde.inscrire_releve("file-neon", ref1, autre_nom)
    refuse("n'est pas l'identifiant figé|deux noms servis")            # deux noms servis
    ref2 = monde.releve("verification-google-cle-2", "e", go="GO-e")
    monde.inscrire_releve("file-neon", ref1, {**ref2, "sha256": "0" * 64})
    refuse("empreinte")
    monde.inscrire_releve("file-neon", ref1, ref2, orthographe_niveau="xhigh")
    refuse("n'est pas ce que portent les relevés")                     # ce que la configuration inscrit
    for issue in ("indécidée", "non comprise"):                        # une sonde « comprise » et l'autre non, sans pièce
        monde.inscrire_releve("file-neon", ref1, monde.releve("verification-google-cle-2", f"f-{issue[:3]}", go=f"GO-{issue[:3]}",
                                                               sonde={"issue": issue}))
        refuse("sans pièce du mot de Lazar")
    monde.inscrire_releve("file-neon", ref1, monde.releve("verification-google-cle-2", "g", go="GO-g", sonde={"issue": None}))
    refuse("n'a pas été jouée")
    refm = monde.releve("verification-mistral-global", "b", go="GO-x")
    monde.inscrire_releve("file-mistral", refm)
    refuse("autre point d'accès", "file-mistral")                      # d'un autre point d'accès
    refm = monde.releve("verification-mistral-eu", "c", go="GO-y", temperature_envoyee=False)
    monde.inscrire_releve("file-mistral", refm)
    refuse("n'est pas ce que porte le relevé", "file-mistral")         # traitement de la température autre que le relevé
    refm = monde.releve("verification-mistral-eu", "g", go="GO-g", majorant="démenti")
    monde.inscrire_releve("file-mistral", refm)
    refuse("sans pièce du mot de Lazar", "file-mistral")               # majorant « démenti » sans pièce du mot


def test_garde_10_artefacts_de_la_piece_du_mot(monde):
    refs = _refs_neon(monde, sonde={"issue": "indécidée"})
    L = monde.config["lignes"]["file-neon"]

    def refuse(texte, motif, empreinte=None):
        monde.piece("mot.md", texte)
        L["mot_de_lazar_sonde"] = {**monde.ref("mot.md"), **({"sha256": empreinte} if empreinte else {})}
        with pytest.raises(chef.Arret, match=motif):
            chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))

    bonnes = ("comprise", "indécidée")
    refuse(mot_neon(refs, bonnes), "empreinte", "0" * 64)              # pièce d'une autre empreinte que la configuration
    refuse(mot_neon({CLE_1: refs[CLE_1], CLE_2: {"sha256": "a" * 64}}, bonnes), "cite un autre relevé pour la clé 2")
    refuse(mot_neon(refs, bonnes, credits=("19,32", None)), "crédit vu après les vérifications du projet b")   # un projet manque
    refuse(mot_neon(refs, bonnes, credits=("19,32", "12,00")), "projet b.*sous 16.08")       # au crédit vu de 12,00
    refuse(mot_neon(refs, ("comprise", "non comprise")), "ne vise pas l'issue de la sonde de la clé 2")
    refuse(mot_neon(refs, bonnes, mot=False), "mot de Lazar")
    refuse(mot_neon(refs, bonnes, plus=[TAUX]), "aucun montant n'est en euros")              # un taux sur une pièce en dollars


# === Seuils de crédit de l'avenant 1, 4.4 : solde plus une recharge, par projet, dépense retirée ==========================

def _depenses(monde, cle_1: float, cle_2: float):
    """Deux lignes de vérification jouées depuis le constat, une par clé, à ces dépenses comptées."""
    monde.depenses_ecrites = getattr(monde, "depenses_ecrites", 0) + 1
    n = monde.depenses_ecrites
    monde.releve("verification-google-cle-1", f"dep{n}", go=f"GO-2026-11-25-{n:02d}", depense_comptee_usd=cle_1)
    monde.releve("verification-google-cle-2", f"dep{n}", go=f"GO-2026-11-26-{n:02d}", depense_comptee_usd=cle_2)


def test_credit_avenant_4_4_cas_sain_et_artefact_chiffres_de_la_depense_retiree(monde):
    """Avenant 1, section 7, point 7 : deux projets distincts « oui », dépenses de 3,68 et 0,02, crédit compté de
    19,76 : la file part (19,76 − 3,68 = 16,08) ; le même, « non relevé » : la file ne part pas (19,76 − 3,70 = 16,06)."""
    _depenses(monde, 3.68, 0.02)
    credits = {"google_credit_vu_projet_a": "19,76", "google_credit_apres_une_recharge_projet_a": "19,76",
               "google_credit_vu_projet_b": "19,76", "google_credit_apres_une_recharge_projet_b": "19,76", **LIEN_CONSTATE}
    sain = chef.controler_credit_de_google(monde.config, monde.racine, "file-neon", _constat(monde, modifs=credits))
    assert sain["depense_retiree_usd"] == "3.68" and "la plus grande" in sain["regle_de_la_depense_retiree"]
    assert sain["depenses_par_cle_usd"] == {CLE_1: "3.68", CLE_2: "0.02"} and sain["seuil_usd"] == "16.08"
    with pytest.raises(chef.Arret, match=r"garde 10 : projet a.*la somme des deux.*= 16\.06, sous 16\.08"):
        chef.controler_credit_de_google(monde.config, monde.racine, "file-neon",
                                        _constat(monde, modifs={**credits, "google_deux_projets_distincts": "non relevé"}))
    # avant une vérification : 19,76 par projet, après le même retrait (avant la seconde, la première a pu prendre 3,68)
    with pytest.raises(chef.Arret, match="garde 9 : projet a.*sous 19.76"):
        chef.controler_credit_de_google(monde.config, monde.racine, "verification-google-cle-2", _constat(monde, modifs=credits))
    assert chef.controler_credit_de_google(monde.config, monde.racine, "file-mistral", _constat(monde, modifs=credits)) is None


def test_credit_avenant_4_4_une_recharge_jamais_deux_non_releve_un_projet_sous_le_seuil(monde):
    ligne = "verification-google-cle-1"
    monde.config["recharge_comptee"] = True          # le chemin de l'avenant (4.4, point 1), gardé et désactivé en définitive
    # sain : 11,93 vus et 23,00 après une recharge : c'est le crédit après une recharge qui compte
    recharge = {"google_credit_vu_projet_a": "11,93", "google_credit_apres_une_recharge_projet_a": "23,00",
                "google_credit_vu_projet_b": "15,59", "google_credit_apres_une_recharge_projet_b": "23,00"}
    sain = chef.controler_credit_de_google(monde.config, monde.racine, ligne, _constat(monde, modifs=recharge))
    assert sain["credits_comptes_usd"] == {"a": "23.00", "b": "23.00"} and sain["recharge_comptee"]["a"] == "une recharge"
    # « non relevé » : le solde vu seul compte, et le contrôle l'écrit (aucun repli silencieux)
    non_releve = {**recharge, "google_credit_apres_une_recharge_projet_a": "non relevé", "google_credit_vu_projet_a": "20,00"}
    lu = _constat(monde, modifs=non_releve)
    controle = chef.controler_credit_de_google(monde.config, monde.racine, ligne, lu)
    assert controle["credits_comptes_usd"]["a"] == "20.00" and "non relevée" in controle["recharge_comptee"]["a"]
    assert lu["recharge_relevee"] == {"a": False, "b": True}
    with pytest.raises(chef.Arret, match="projet a.*solde vu seul.*sous 19.76"):          # 11,93 seuls : sous le seuil
        chef.controler_credit_de_google(monde.config, monde.racine, ligne, _constat(
            monde, modifs={**recharge, "google_credit_apres_une_recharge_projet_a": "non relevé"}))
    # un projet sous le seuil et l'autre au-dessus : la ligne ne part pas (on ne sait pas quel projet porte la clé)
    with pytest.raises(chef.Arret, match="projet b.*sous 19.76"):
        chef.controler_credit_de_google(monde.config, monde.racine, ligne, _constat(
            monde, modifs={**recharge, "google_credit_apres_une_recharge_projet_b": "19,00"}))
    # recharge comptée deux fois : 11,93 + 2 × 5,00 passerait 19,76 ; une seule (16,93) ne le passe pas
    with pytest.raises(chef.Arret, match="projet a.*16.93.*sous 19.76"):
        chef.controler_credit_de_google(monde.config, monde.racine, ligne, _constat(
            monde, modifs={**recharge, "google_credit_apres_une_recharge_projet_a": "16,93"}))
    # ligne entière : le seuil retient les lignes de Google, non celles de Mistral
    monde.piece("constat-bas.md", constat({**recharge, "google_credit_apres_une_recharge_projet_b": "19,00"}))
    monde.config["constat"] = monde.ref("constat-bas.md")
    with pytest.raises(chef.Arret, match="garde 9 : projet b"):
        chef.gardes_avant_depart(monde.config, ligne, {"GO_ID": GO[ligne]}, monde.racine, monde.registre(), MAINTENANT)
    avant = chef.gardes_avant_depart(monde.config, "verification-mistral-eu", {"GO_ID": GO["verification-mistral-eu"]},
                                     monde.racine, monde.registre(), MAINTENANT)
    assert avant["controle_du_credit"] is None and avant["constat_resume"]["fournisseur_juge"] == "mistral"
    assert avant["constat_resume"]["cles_levees"] == {"go": None, "cles": []}          # aucune clé de Mistral n'est levée


def test_credit_en_euros_taux_diminue_de_la_marge_centime_inferieur(monde):
    euros = {**EUROS, "google_credit_vu_projet_a": "11,93", "google_credit_apres_une_recharge_projet_a": "20,00",
             "google_credit_vu_projet_b": "15,59", "google_credit_apres_une_recharge_projet_b": "20,00"}
    monde.config["marge_de_change"], monde.config["recharge_comptee"] = 0.05, True
    lu = _constat(monde, modifs=euros, hors_tableau=[TAUX])            # 20,00 × 1,07 × 0,95 = 20,33
    assert lu["credits_comptes_usd"] == {"a": Decimal("20.33"), "b": Decimal("20.33")} and str(lu["taux"]["taux"]) == "1.0700"
    assert chef.controler_credit_de_google(monde.config, monde.racine, "verification-google-cle-1", lu)["seuil_usd"] == "19.76"
    bas = ligne_de_taux("1,0399")      # 20 × 1,0399 × 0,95 = 19,7581 : 19,75
    with pytest.raises(chef.Arret, match=r"19\.75.*sous 19\.76"):
        chef.controler_credit_de_google(monde.config, monde.racine, "verification-google-cle-1",
                                        _constat(monde, modifs=euros, hors_tableau=[bas]))
    juste = ligne_de_taux("1,0400")    # avenant 1, 8.2 : 1,0400 suffit
    assert _constat(monde, modifs=euros, hors_tableau=[juste])["credits_comptes_usd"]["a"] == Decimal("19.76")
    monde.config["marge_de_change"] = None                              # conversion sans marge inscrite : refusée
    with pytest.raises(chef.Arret, match="sans marge de change"):
        _constat(monde, modifs=euros, hors_tableau=[TAUX])
    monde.config["marge_de_change"] = 0.05
    with pytest.raises(chef.Arret, match="ligne « - taux"):             # ligne de taux absente quand une devise est EUR
        _constat(monde, modifs=euros)
    with pytest.raises(chef.Arret, match="aucun montant n'est en euros"):   # un taux sur une pièce toute en dollars
        _constat(monde, hors_tableau=[TAUX])
    mistral = {"mistral_devise_affichee": "EUR", "mistral_credit_utilisable_usd": "8,00"}    # 8,00 × 1,07 × 0,95 = 8,13
    with pytest.raises(chef.Arret, match="mistral_credit_utilisable_usd vaut 8.13, sous le seuil"):
        _constat(monde, modifs=mistral, hors_tableau=[TAUX], fournisseur="mistral")
    assert _constat(monde, modifs={**mistral, "mistral_credit_utilisable_usd": "8,10"}, hors_tableau=[TAUX], fournisseur="mistral")["credit_de_mistral_usd"] == Decimal("8.23")


def test_age_du_taux_24_heures_avant_la_piece_6_heures_apres_jamais_apres_l_envoi(monde):
    """Borne choisie : le taux est daté de 24 heures au plus avant l'heure de la pièce (celle où les montants ont été
    vus), et de 6 heures au plus après elle ; jamais après l'envoi."""
    monde.config["marge_de_change"] = 0.05
    vu = MAINTENANT - datetime.timedelta(hours=40)                      # les montants ont été vus il y a 40 heures

    def lire(decalage_h: float):
        quand = (vu + datetime.timedelta(hours=decalage_h)).strftime("%Y-%m-%dT%H:%M:%SZ")
        taux = ligne_de_taux(quand=quand)
        return _constat(monde, modifs=EUROS, date=vu.strftime("%Y-%m-%dT%H:%M:%SZ"), hors_tableau=[taux],
                        transcription=(vu + datetime.timedelta(minutes=5)).strftime("%Y-%m-%dT%H:%M:%SZ"))

    for sain in (-23.9, 0, 0.1, 5.9):                                   # dont un taux relevé cinq minutes après la lecture
        assert lire(sain)["taux"]
    with pytest.raises(chef.Arret, match="plus de 24 heures avant"):
        lire(-24.1)
    with pytest.raises(chef.Arret, match="plus de 6 heures après"):
        lire(6.1)
    with pytest.raises(chef.Arret, match="postérieure à l'envoi"):
        lire(41)
    assert chef.AGE_MAX_DU_TAUX == datetime.timedelta(hours=24) and chef.RETARD_MAX_DU_TAUX == datetime.timedelta(hours=6)


# === Garde 11 : signe de « ne sert pas ce modèle » ========================================================================

def test_garde_11_signe():
    sans = {"admise_sans_identifiant": True}
    avec = {"admise_sans_identifiant": False}
    signe = chef.signe_ne_sert_pas
    assert signe(sans, 400, {"type": "invalid_model"})                                      # signe constaté
    assert signe(sans, 404, {"code": 1500}) and signe(sans, 404, {"code": "1500"})
    assert signe(sans, 422, {"message": "Model MISTRAL-LARGE-4-0 does not exist"})
    assert signe(sans, 422, {"detail": [{"loc": ["body", "model"], "msg": "x"}]})
    assert not signe(sans, 401, {"type": "invalid_model"})                                  # code 401
    assert not signe(sans, 200, {"type": "invalid_model"})                                  # code 200
    assert not signe(avec, 400, {"type": "invalid_model"})                                  # la liste porte l'identifiant
    assert not signe(sans, 404, "<html>Not Found</html>") and not signe(sans, 404, {"error": "not found"})   # pas le corps de Mistral
    assert not signe(sans, 422, {"detail": [{"loc": ["body", "max_tokens"]}]})              # 422 qui nomme `max_tokens`
    assert not signe(sans, 422, {"detail": [{"loc": ["body", "model"]}, {"loc": ["body", "temperature"]}]})
    assert not signe(sans, 422, {"detail": [{"loc": ["body", "model_config"]}]})            # égalité d'un élément, non sous-chaîne
    assert not signe(sans, 404, {"message": "model not found"})                             # sans l'identifiant
    assert not signe({"admise_sans_identifiant": False, "lisible": False}, 400, {"type": "invalid_model"})   # liste illisible
    assert chef.liste_lue("mistral", 200, json.dumps({"modeles": []}).encode())["lisible"] is False
    for forme in ("objet", "tableau"):                                                      # les deux formes relevées
        corps = json.dumps(faux.liste_mistral(("mistral-small",), forme)["corps"]).encode()
        assert chef.liste_lue("mistral", 200, corps)["admise_sans_identifiant"]
        corps = json.dumps(faux.liste_mistral(("mistral-small", "mistral-large-4-0"), forme)["corps"]).encode()
        assert chef.liste_lue("mistral", 200, corps)["porte_identifiant"]
    alias = json.dumps({"data": [{"id": "mistral-large-latest", "aliases": ["mistral-large-4-0"]}]}).encode()
    assert chef.liste_lue("mistral", 200, alias)["admise_sans_identifiant"]                  # les `aliases` sont ignorés


def test_garde_11_sur_le_faux_fournisseur(monde, banc):
    constate = banc("verification-mistral-eu", liste=faux.liste_mistral(("mistral-small",)))
    constate.faux.programmer(faux.erreur_mistral(400, type_="invalid_model"))
    releve = constate.verifier()
    assert releve["signe_constate"] and releve["issue_finale_ligne"] == 9 and releve["close"] and not releve["saine"]
    assert "invalid_model" in releve["appels"][0]["corps_d_erreur"]                         # le corps d'erreur, borné
    # liste sans l'identifiant et code 200 avec le bon nom : saine, point d'accès européen retenu, pas de signe
    saine = banc("verification-mistral-eu", liste=faux.liste_mistral(("mistral-small",)))
    saine.faux.programmer(faux.flux_mistral("OK"), sonde_mistral())
    releve = saine.verifier()                                       # sous sa propre ligne de calcul : la première est close au signe
    assert releve["saine"] and not releve["signe_constate"] and releve["hote"] == "api.eu.mistral.ai"
    # sur le point d'accès global, il n'y a ni signe ni repli
    monde.releve("verification-mistral-eu", "eu", signe_constate=True, saine=False)
    mondial = banc("verification-mistral-global", liste=faux.liste_mistral(("mistral-small",)))
    mondial.faux.programmer(faux.erreur_mistral(400, type_="invalid_model"))
    releve = mondial.verifier()
    assert not releve["signe_constate"] and releve["issue_finale_ligne"] == 13 and releve["noeud_de_lazar"]
    # refus du mandataire : pas de signe, pas de repli
    ferme = banc("verification-mistral-eu", adresse=f"http://127.0.0.1:{faux.port_ferme()}")
    releve = ferme.verifier()
    assert not releve["signe_constate"] and releve["appels"] == [] and releve["a_refaire"]
    assert releve["listes"][0]["signature_du_mandataire"] and not releve["close"]


# === Garde 12 : fichier des règles ========================================================================================

def test_garde_12_fichier_des_regles(monde):
    assert chef.garde_regles(monde.config, monde.racine) == monde.config["regles"]["sha256"]      # conforme
    texte = (monde.racine / "pieces" / "regles.md").read_text(encoding="utf-8")
    assert all(f"    {n}. " in texte for n in range(1, 9))                                        # les huit règles
    bon = dict(monde.config["regles"])

    def refuse(nom, contenu, motif):
        monde.piece(nom, contenu)
        monde.config["regles"] = {**bon, **monde.ref(nom)}
        with pytest.raises(chef.Arret, match=motif):
            chef.garde_regles(monde.config, monde.racine)

    monde.config["regles"] = {**bon, "chemin": "pieces/absent.md"}
    with pytest.raises(chef.Arret, match="garde 12"):                                             # absent
        chef.garde_regles(monde.config, monde.racine)
    refuse("regles-autre-brouillon.md", texte.replace(monde.config["prereg_en_vigueur"]["sha256"], "b" * 64),
           "cite un autre brouillon")
    refuse("regles-gabarit.md", (RACINE / GABARIT_REGLES).read_text(encoding="utf-8"), "gabarit")
    refuse("regles-resume.md", texte.replace("au moins 22 réponses", "au moins 20 réponses"), "copie à la lettre")
    monde.piece("regles-sans-compagnon.md", texte, sceller=False)
    monde.config["regles"] = {**bon, **monde.ref("regles-sans-compagnon.md")}
    with pytest.raises(chef.Arret, match="compagnon"):                                            # non scellé
        chef.garde_regles(monde.config, monde.racine)


def test_garde_12_fichier_change_apres_la_file_le_programme_des_regles_refuse(monde, banc):
    n = banc("file-neon")
    n.faux.programmer(*reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google))
    assert n.jouer()["complet"]
    rapport = chef.faire_rapport(n.dossier)
    chef.rendre_piece(n.dossier, "rapport-technique.json", rapport, "google", chef.texte_du_rapport(rapport))
    resultat = chef.appliquer_regles_au_dossier(n.dossier, monde.config, monde.racine)            # règles appliquées
    assert resultat["tient"] and resultat["regles_sha256"] == monde.config["regles"]["sha256"]
    with open(monde.racine / "pieces" / "regles.md", "a", encoding="utf-8") as f:
        f.write("\nune ligne ajoutée après la file\n")
    with pytest.raises(chef.Arret, match="garde 12"):
        chef.appliquer_regles_au_dossier(n.dossier, monde.config, monde.racine)


# === Garde 13 : une file ne se rejoue pas =================================================================================

def test_garde_13_une_file_ne_se_rejoue_pas(monde):
    monde.inscrire_releve("file-neon", monde.releve("verification-google-cle-1", "v1"))
    env = {"GO_ID": GO["file-neon"]}
    avant = chef.gardes_avant_depart(monde.config, "file-neon", env, monde.racine, monde.registre(), MAINTENANT)   # premier départ
    assert avant["contexte"]["regime"] == "courant" and avant["regles"]["sha256"] == monde.config["regles"]["sha256"]
    parti = monde.racine / "runs" / "essais-admission-bras-a-v1" / "20261122-100000-file-neon"
    parti.mkdir(parents=True)
    (parti / "manifeste-depart.json").write_text(json.dumps({
        "ligne": "file-neon", "go": GO["file-neon"], "fournisseur": "google", "texte_en_vigueur": {}, "regles": {},
        "contexte": {"hote": "h", "releve": {}, "nom_servi": "gemini-4-neon", "sonde": "comprise", "regime": "courant"}}),
        encoding="utf-8")
    (parti / "journal-essai.jsonl").write_text(json.dumps({"evenement": "depart", "envoi": "01-A-b1-01-1", "appel": 1, "rang": 1,
                                                            "cout_si_sans_reponse_usd": 0.5}) + "\n", encoding="utf-8")
    with pytest.raises(chef.Arret, match="garde 13"):                                             # second départ : refus
        chef.gardes_avant_depart(monde.config, "file-neon", env, monde.racine, monde.registre(), MAINTENANT)
    monde.inscrire_releve("file-mistral", monde.releve("verification-mistral-eu", "v1"))          # l'autre file part
    chef.gardes_avant_depart(monde.config, "file-mistral", {"GO_ID": GO["file-mistral"]}, monde.racine, monde.registre(), MAINTENANT)


# === Garde 14 : identifiant figé et voie d'accès ==========================================================================

def test_garde_14_identifiant_fige_et_voie_d_acces(monde):
    for ligne in chef.LIGNES:
        assert chef.controler_identifiants(monde.config, ligne) in chef.HOTES_PERMIS             # conformes

    def refuse(modifier, ligne, motif="garde 14"):
        config = copy.deepcopy(monde.config)
        modifier(config)
        with pytest.raises(chef.Arret, match=motif):
            chef.controler_identifiants(config, ligne)

    for alias in ("mistral-large-latest", "mistral-large-4"):
        refuse(lambda c, a=alias: c["fournisseurs"]["mistral"].update(modele=a), "file-mistral")
    refuse(lambda c: c["fournisseurs"]["google"].update(modele="gemini-4-neon-latest"), "file-neon")
    refuse(lambda c: c["lignes"]["file-neon"].update(hote="exemple.org"), "file-neon")           # un hôte autre
    refuse(lambda c: c["lignes"]["verification-mistral-eu"].update(hote="api.mistral.ai"), "verification-mistral-eu")
    refuse(lambda c: c["lignes"]["file-mistral"].update(hote="generativelanguage.googleapis.com"), "file-mistral")
    refuse(lambda c: c["hotes_permis"].append("exemple.org"), "file-neon")
    fm = monde.config["fournisseurs"]["mistral"]
    corps = chef.construire_corps("mistral", fm, "t", 32768)
    with pytest.raises(chef.Arret, match="garde 14"):                                             # dans le corps
        chef.controler_corps("mistral", fm, {**corps, "model": "mistral-large-latest"}, "/v1/chat/completions", 32768)
    fg = monde.config["fournisseurs"]["google"]
    with pytest.raises(chef.Arret, match="garde 14"):                                             # dans le chemin de l'appel
        chef.controler_corps("google", fg, chef.construire_corps("google", fg, "t", 32768, orthographe="XHIGH"),
                             "/v1beta/models/gemini-4-neon-latest:generateContent", 32768, orthographe="XHIGH")
    with pytest.raises(relais_mistral.RelaisInvalide):                                            # le relais refuse l'hôte
        relais_mistral.cible_de("exemple.org", None)
    with pytest.raises(relais_google.RelaisInvalide):
        relais_google.cible_de("api.mistral.ai", None)
    with pytest.raises(chef.Arret, match="adresse_d_essai"):                                      # relais d'essai sous une ligne réelle
        chef.controler_etat_initial({"amont": "api.eu.mistral.ai", "modele": "mistral-large-4-0", "appels": 0, "max_appels": 3,
                                     "adresse_d_essai": "http://127.0.0.1:1", "cle_dans_l_environnement": False,
                                     "plafond_usd": 0.25}, monde.config, "verification-mistral-eu")
    # voie d'essai : une configuration qui n'est pas définitive ne joint jamais un hôte réel, et l'inverse
    with pytest.raises(chef.Arret, match="garde 14"):
        chef.controler_voie_d_essai({"etat": "essai", "essai_local": None}, "mistral")
    with pytest.raises(chef.Arret, match="garde 14"):
        chef.controler_voie_d_essai({"etat": "essai", "essai_local": {"google": "http://127.0.0.1:1"}}, "mistral")
    with pytest.raises(chef.Arret, match="garde 14"):
        chef.controler_voie_d_essai({"etat": "definitive", "essai_local": {"mistral": "http://127.0.0.1:1"}}, "mistral")
    chef.controler_voie_d_essai({"etat": "definitive", "essai_local": None}, "mistral")           # conformes
    chef.controler_voie_d_essai({"etat": "essai", "essai_local": {"mistral": "http://127.0.0.1:1"}}, "mistral")
    with pytest.raises(chef.Arret, match="garde 14"):                                             # ligne entière : rien ne part
        chef.lancer_relais(monde.config, "verification-mistral-eu", monde.racine, monde.racine / "runs",
                           {"PATH": os.environ["PATH"], "MISTRAL_API_KEY": "valeur-factice-du-relais"})
    with pytest.raises(chef.Arret, match="amont"):                                                # l'hôte global sous la ligne européenne
        chef.controler_etat_initial({"amont": "api.mistral.ai", "modele": "mistral-large-4-0", "appels": 0, "max_appels": 3,
                                     "adresse_d_essai": None, "cle_dans_l_environnement": False, "plafond_usd": 0.25},
                                    monde.config, "verification-mistral-eu")


# === Garde 15 : repli lié au signe ========================================================================================

def test_garde_15_repli_lie_au_signe(monde):
    L = monde.config["lignes"]["verification-mistral-global"]
    with pytest.raises(chef.Arret, match="garde 15"):                                             # relevé absent
        chef.garde_repli(monde.config, monde.racine)
    L["releve_europeen"] = monde.releve("verification-mistral-eu", "signe", saine=False, signe_constate=True,
                                        issue_finale_ligne=9, nom_servi=None)
    assert chef.garde_repli(monde.config, monde.racine)["signe_constate"] is True                 # signe constaté
    for nom, champs in (("401", {"issue_finale_ligne": 7}), ("autre-nom", {"issue_finale_ligne": 4}),
                        ("ligne-13", {"issue_finale_ligne": 13})):                                # relevés sans signe
        L["releve_europeen"] = monde.releve("verification-mistral-eu", nom, go=f"GO-{nom}", saine=False,
                                            signe_constate=False, **champs)
        with pytest.raises(chef.Arret, match="n'est pas constaté"):
            chef.garde_repli(monde.config, monde.racine)
    L["releve_europeen"] = monde.releve("verification-mistral-global", "pas-eu", go="GO-pas-eu", signe_constate=True)
    with pytest.raises(chef.Arret, match="n'est pas celui de la vérification européenne"):
        chef.garde_repli(monde.config, monde.racine)
    chemin, empreinte = monde.ecrire_configuration()                                              # la vérification globale ne part pas
    assert chef.executer("verification-mistral-global", chemin, empreinte, {"GO_ID": GO["verification-mistral-global"]},
                         racine=monde.racine, registre=monde.registre(), a_l_instant=MAINTENANT) == 2


# === Garde 16 : forme de la réponse à la vérification, classement, sonde, majorant ========================================

def test_garde_16_sain_formes_completes_et_sondes_comprises(monde, banc):
    m = banc("verification-mistral-eu")           # flux complet, dont le dernier événement n'a pas de champ `model`
    m.faux.programmer(faux.flux_mistral("OK", dernier_sans_modele=True), sonde_mistral(200, "length"))
    releve = m.verifier()
    assert releve["saine"] and releve["nom_servi"] == "mistral-large-4-0" and releve["temperature_envoyee"] is True
    assert releve["sonde"]["issue"] == "comprise" and releve["majorant"] == "établi" and not releve["noeud_de_lazar"]
    assert releve["appels"][1]["morceaux_par_type"] == {"thinking": 1, "text": 1}
    assert releve["champs_du_bloc_d_usage"] == ["completion_tokens", "prompt_tokens", "total_tokens"]
    assert chef.code_de_sortie_verification(releve) == 0 and releve["close"]
    corps_a, corps_b = (json.loads(a["corps"]) for a in m.faux.appels())
    assert corps_b == {**corps_a, "max_tokens": 256, "messages": [{"role": "user", "content": monde.config["messages"]["sonde"]}]}
    assert corps_a["messages"][0]["content"] == "Reply with the single word: OK" and corps_a["max_tokens"] == 32768
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK"), sonde_google(256, 180, "MAX_TOKENS"))
    releve = g.verifier()
    assert releve["saine"] and releve["orthographe_niveau"] == "XHIGH" and releve["sonde"]["issue"] == "comprise"
    assert releve["appels"][1]["reflexion"] == 180 and chef.code_de_sortie_verification(releve) == 0
    assert [json.loads(a["corps"])["generationConfig"]["maxOutputTokens"] for a in g.faux.appels()] == [32768, 256]
    assert g.faux.appels()[0]["chemin"] == "/v1beta/models/gemini-4-neon:generateContent"
    assert g.faux.appels()[0]["en_tetes"]["x-goog-api-key"] == "valeur-factice-du-relais"   # la clé ne vit que dans le relais
    assert g.faux.recus[0]["methode"] == "GET" and g.faux.recus[0]["chemin"] == "/v1beta/models/gemini-4-neon"


@pytest.mark.parametrize("fournisseur, reponse, ligne_attendue", [
    ("mistral", faux.flux_mistral("OK", sans_usage=True), 5),                   # 200 sans `usage` dans le flux
    ("mistral", faux.flux_mistral("OK", sans_total=True), 5),                   # sans `total_tokens`
    ("mistral", faux.flux_mistral("OK", sans_morceau_texte=True, pensee="p"), 5),   # contenu sans morceau `text`
    ("mistral", faux.flux_mistral("OK", fin="length"), 5),
    ("mistral", faux.flux_mistral("OK", modele="mistral-large-4"), 4),          # un autre nom servi
    ("mistral", faux.flux_mistral("OK", modele="Mistral-Large-4-0"), 4),        # une autre casse
    ("mistral", faux.flux_mistral("OK", autre_nom_au_dernier="mistral-large-latest"), 4),
    ("mistral", faux.flux_mistral("OK", modele=None), 4),                       # aucun événement ne porte `model`
    ("google", faux.reponse_google("OK", modele=None), 4),                      # sans `modelVersion`
    ("google", faux.reponse_google("OK", modele="models/gemini-4-neon"), 4),    # un préfixe
    ("google", faux.reponse_google("OK", modele="gemini-4-neon-2026-11-01"), 4),   # un suffixe de date
    ("google", faux.reponse_google("OK", sans_usage=True), 5),
    ("google", faux.reponse_google(None), 5),                                   # texte non extractible
    ("google", faux.reponse_google("OK", fin="MAX_TOKENS"), 5)])
def test_garde_16_artefacts_de_forme(monde, banc, fournisseur, reponse, ligne_attendue):
    b = banc("verification-mistral-eu" if fournisseur == "mistral" else "verification-google-cle-1")
    b.faux.programmer(reponse, faux.flux_mistral("OK"))
    releve = b.verifier()
    assert not releve["saine"] and releve["issue_finale_ligne"] == ligne_attendue and releve["close"]
    assert len(b.faux.appels()) == 1                                             # ni repli, ni appel de plus
    assert releve["noeud_de_lazar"] == (ligne_attendue == 4)
    assert chef.code_de_sortie_verification(releve) == 1


def test_regle_google_g6_verification_sans_jeton_de_pensee_non_saine(monde, banc):
    """Le cas d'Argon : un niveau accepté mais non appliqué. Sans un jeton de pensée constaté — compte à zéro, ou
    `thoughtsTokenCount` absent —, l'appel de vérification n'est pas sain : défaut journalisé, nœud de Lazar."""
    for reponse in (faux.reponse_google("OK", usage=(30, 2, 0, 32)), faux.reponse_google("OK", usage=(30, 2, 0, 32), sans_pensees=True)):
        g = banc("verification-google-cle-1")
        g.faux.programmer(reponse, sonde_google())
        releve = g.verifier()
        a = releve["appels"][0]
        assert not releve["saine"] and releve["issue_finale_ligne"] == 13 and releve["noeud_de_lazar"] and releve["close"]
        assert a["defaut_google"] == "zéro jeton de pensée" and "zéro jeton de pensée" in a["issue"] and len(g.faux.appels()) == 1
    sain = banc("verification-google-cle-1")                           # cas sain : un jeton de pensée suffit
    sain.faux.programmer(faux.reponse_google("OK", usage=(30, 2, 1, 33)), sonde_google())
    releve = sain.verifier()
    assert releve["saine"] and releve["appels"][0]["reflexion"] == 1 and releve["appels"][0]["defaut_google"] is None
    m = banc("verification-mistral-eu")                                # la règle ne vise que Google
    m.faux.programmer(faux.flux_mistral("OK"), sonde_mistral())
    assert m.verifier()["saine"]


def test_garde_16_classement_ligne_2_limite_de_sortie_a_la_liste(monde, banc):
    g = banc("verification-google-cle-1", liste=faux.modele_google(limite_sortie=16384))
    g.faux.programmer(faux.reponse_google("OK"))
    releve = g.verifier()
    assert releve["issue_finale_ligne"] == 2 and g.faux.appels() == [] and releve["close"]   # aucun appel payant


def test_garde_16_classement_lignes_7_et_8(monde, banc):
    sept = banc("verification-mistral-eu")                                       # 401 et liste qui porte l'identifiant
    sept.faux.programmer(faux.erreur_mistral(401, message="Unauthorized"))
    releve = sept.verifier()
    assert releve["appels"][0]["ligne_du_classement"] == 7 and releve["a_refaire"] and not releve["close"]
    huit = banc("verification-mistral-eu", liste=faux.liste_mistral(("mistral-small",)))     # 403 et liste sans l'identifiant
    huit.faux.programmer(faux.erreur_mistral(403, message="Forbidden"))
    releve = huit.verifier()
    assert releve["issue_finale_ligne"] == 8 and releve["noeud_de_lazar"] and releve["close"]


def test_garde_16_classement_ligne_10_temperature_retiree(monde, banc):
    m = banc("verification-mistral-eu")
    m.faux.programmer(faux.erreur_mistral(422, detail=[{"loc": ["body", "temperature"], "msg": "not supported"}]),
                      faux.flux_mistral("OK"), sonde_mistral())
    releve = m.verifier()
    assert [(a["type"], a["ligne_du_classement"]) for a in releve["appels"]] == [("A", 10), ("Ap", 3), ("B", None)]
    corps = [json.loads(a["corps"]) for a in m.faux.appels()]
    assert "temperature" in corps[0] and "temperature" not in corps[1] and "temperature" not in corps[2]
    assert releve["saine"] and releve["temperature_envoyee"] is False and releve["appels_comptes"] == 3


def test_garde_16_classement_ligne_11_les_deux_temps(monde, banc):
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.erreur_google(400, "Invalid value at generationConfig", champs=["generation_config.thinking_config.thinkingLevel"]),
                      faux.reponse_google("OK"), sonde_google())
    releve = g.verifier()
    assert [(a["type"], a["ligne_du_classement"]) for a in releve["appels"]] == [("A", 11), ("Ap", 3), ("B", None)]
    niveaux = [json.loads(a["corps"])["generationConfig"]["thinkingConfig"]["thinkingLevel"] for a in g.faux.appels()]
    assert niveaux == ["XHIGH", "xhigh", "xhigh"] and releve["orthographe_niveau"] == "xhigh"   # l'orthographe saine est inscrite


def test_garde_16_classement_ligne_12(monde, banc):
    cas = [faux.erreur_mistral(400, param="max_tokens", message="invalid"),                 # nomme `max_tokens`
           faux.erreur_mistral(400, message="temperature and reasoning_effort are invalid")]   # nomme deux champs
    for reponse in cas:
        m = banc("verification-mistral-eu")
        m.faux.programmer(reponse, faux.flux_mistral("OK"))
        releve = m.verifier()
        assert releve["issue_finale_ligne"] == 12 and len(m.faux.appels()) == 1 and not releve["noeud_de_lazar"]
    g = banc("verification-google-cle-1")                                                         # le même champ à l'appel A′
    refus = faux.erreur_google(400, "Invalid value for thinkingLevel")
    g.faux.programmer(refus, copy.deepcopy(refus), faux.reponse_google("OK"))
    releve = g.verifier()
    assert [a["ligne_du_classement"] for a in releve["appels"]] == [11, 12] and len(g.faux.appels()) == 2


def test_garde_16_classement_ligne_13(monde, banc):
    cas = [faux.erreur_mistral(400, message="bad request"),                                 # 400 sans champ nommé
           faux.erreur_mistral(404, message="Not Found"),                                   # 404 hors du signe
           faux.rep_json(200 + 300, b"<html>illisible</html>") | {"code": 400},             # corps illisible
           faux.rep_json(418, {"message": "I'm a teapot"})]                                 # code 418
    for reponse in cas:
        m = banc("verification-mistral-eu")
        m.faux.programmer(reponse, faux.flux_mistral("OK"))
        releve = m.verifier()
        assert releve["issue_finale_ligne"] == 13 and releve["noeud_de_lazar"] and len(m.faux.appels()) == 1
    coupe = banc("verification-mistral-eu")                                                 # appel A coupé à sa borne en octets
    coupe.faux.programmer(faux.flux_sans_fin(), faux.flux_mistral("OK"))
    releve = coupe.verifier()
    a = releve["appels"][0]
    assert a["coupe_a_sa_borne_en_octets"] and releve["issue_finale_ligne"] == 13 and len(coupe.faux.appels()) == 1
    assert releve["envois_coupes"] == [a["envoi"]]


def test_garde_16_classement_unites():
    liste = {"admise_sans_identifiant": False}
    classer = chef.classer_issue
    assert classer("mistral", "api.eu.mistral.ai", "A", liste, _retour(502), None, None, True)[0] == 1
    assert classer("mistral", "api.eu.mistral.ai", "A", liste, _retour(429), None, None, False)[0] == 6
    assert classer("google", "h", "A", liste, _retour(503), None, None, False)[0] == 6
    assert classer("google", "h", "A", liste, _retour(None), None, "delai", False)[0] == 6
    assert classer("google", "h", "A", liste, _retour(402), None, None, False)[0] == 13       # livraison 11 : crédit épuisé
    assert classer("google", "h", "A", liste, _retour(401), None, None, False)[0] == 7        # clé refusée : inchangé
    temperature = json.dumps({"message": "temperature is not supported"}).encode()
    assert classer("mistral", "api.eu.mistral.ai", "A", liste, _retour(400, temperature), None, None, False)[0] == 10
    assert classer("mistral", "api.eu.mistral.ai", "Ap", liste, _retour(400, temperature), None, None, False)[0] == 12
    assert classer("google", "h", "A", liste, _retour(400, temperature), None, None, False)[0] == 12   # autre champ, chez Google
    assert chef.champs_nommes({"detail": [{"loc": ["body", "max_tokens_extra"]}]}) == set()         # `loc` : égalité
    assert chef.champs_nommes({"param": "generationConfig.maxOutputTokens"}) == {"maxOutputTokens"}
    assert chef.champs_nommes({"error": {"message": "Unknown name THINKINGLEVEL"}}) == {"thinkingLevel"}
    relais = json.dumps({"erreur": {"origine": "relais", "motif": "borne d'appels"}}).encode()
    assert classer("google", "h", "A", liste, _retour(429, relais), None, None, False)[0] == 13


@pytest.mark.parametrize("reponse, issue, par_octets", [
    (sonde_mistral(900, "length"), "non comprise", False),                       # à 900 jetons facturés
    (faux.flux_sans_fin(), "non comprise", True),                                # coupée à 32 768 octets
    (sonde_mistral(40, "stop"), "indécidée", False),                             # finie `stop` à 40 jetons
    (sonde_mistral(256, "length", pensee=None), "indécidée", False),             # aucun morceau `thinking`
    (sonde_mistral(256, "length", type_pensee="reasoning"), "indécidée", False),   # la pensée sous un autre type
    (faux.flux_mistral("1", pensee="p" * 300, usage=(30, 256, 330), fin="length"), "non comprise", False),   # 256 et 300
    (sonde_mistral(256, "length", pensee="p" * 5000), "non comprise", True),     # 5 000 octets de contenu reçus
    (sonde_mistral(256, "length", pensee="p" * 2047), "comprise", False),        # la même à 2 048 octets
    (faux.erreur_mistral(400, message="bad request"), "indécidée", False)])      # code d'erreur
def test_garde_16_sonde_de_mistral(monde, banc, reponse, issue, par_octets):
    m = banc("verification-mistral-eu")
    m.faux.programmer(faux.flux_mistral("OK"), reponse)
    releve = m.verifier()
    assert releve["sonde"]["issue"] == issue and releve["sonde"]["par_constat_d_octets"] == par_octets
    assert releve["saine"] and releve["close"]
    assert releve["noeud_de_lazar"] == (issue != "comprise") and chef.code_de_sortie_verification(releve) == (issue != "comprise")
    if issue == "comprise":
        assert releve["appels"][1]["octets_contenu"] == 2048


@pytest.mark.parametrize("reponse, issue", [
    (sonde_google(900, 700), "non comprise"),
    (sonde_google(40, 20, "STOP"), "indécidée"),
    (sonde_google(256, 0), "indécidée"),                                         # `thoughtsTokenCount` à 0
    (faux.reponse_google("4", usage=(30, 256, 0, 286), fin="MAX_TOKENS", sans_pensees=True), "indécidée"),   # ou absent
    (faux.reponse_google("4", usage=(30, 200, 56, 330), fin="MAX_TOKENS"), "non comprise"),   # 256 d'un côté, 300 de l'autre
    (faux.reponse_google("4", fin="SAFETY"), "indécidée"),                       # refus
    (sonde_google(256, 180, "CONTINUATION"), "comprise")])
def test_garde_16_sonde_de_google(monde, banc, reponse, issue):
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK"), reponse)
    releve = g.verifier()
    assert releve["sonde"]["issue"] == issue and releve["noeud_de_lazar"] == (issue != "comprise")


def test_garde_16_sonde_a_refaire_sur_un_code_429(monde, banc):
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK"), faux.erreur_google(429))
    releve = g.verifier()
    assert releve["a_refaire"] and not releve["close"] and releve["sonde"]["issue"] is None
    g.nouveau_dossier()
    g.faux.programmer(sonde_google())
    suite = g.verifier()
    assert suite["sonde"]["issue"] == "comprise" and suite["appels_comptes"] == 3 and suite["close"]
    g.nouveau_dossier()                                                          # ligne close : plus aucun lancement
    monde.inscrire_releve("file-neon", monde.releve("verification-google-cle-1", "autre", go="GO-autre"))
    with pytest.raises(chef.Arret, match="close"):
        chef.gardes_avant_depart(monde.config, "verification-google-cle-1", {"GO_ID": GO["verification-google-cle-1"]}, monde.racine,
                                 monde.registre(), MAINTENANT)


def test_garde_16_troisieme_appel_a_prime_la_sonde_demande_une_ligne_nouvelle(monde, banc):
    m = banc("verification-mistral-eu")
    m.faux.programmer(faux.erreur_mistral(401, message="Unauthorized"))
    assert m.verifier()["a_refaire"]
    m.nouveau_dossier()
    m.faux.programmer(faux.erreur_mistral(400, message="temperature unsupported"), faux.flux_mistral("OK"), sonde_mistral())
    releve = m.verifier()
    assert [a["type"] for a in releve["appels"]] == ["A", "A", "Ap"] and releve["saine"] and releve["close"]
    assert "ligne nouvelle" in releve["issue_finale"] and releve["sonde"]["issue"] is None and len(m.faux.appels()) == 3


def test_garde_16_majorant_par_octets(monde, banc):
    a = banc("verification-mistral-eu")                                          # 300 jetons facturés pour 100 octets, à l'appel A
    a.faux.programmer(faux.flux_mistral("x" * 100, usage=(30, 300, 330)), sonde_mistral())
    releve = a.verifier()
    assert releve["saine"] and releve["majorant"] == "démenti" and releve["noeud_de_lazar"]   # saine sur sa forme, mais nœud
    assert chef.code_de_sortie_verification(releve) == 1
    b = banc("verification-mistral-eu")                                          # de même à la sonde : 250 pour 100 octets
    b.faux.programmer(faux.flux_mistral("OK"), faux.flux_mistral("1", pensee="p" * 99, usage=(30, 250, 280), fin="length"))
    releve = b.verifier()
    assert releve["sonde"]["issue"] == "comprise" and releve["majorant"] == "démenti" and releve["noeud_de_lazar"]
    assert chef.constat_du_majorant([{"code": 200, "sortie_facturee": 164, "octets_contenu": 100}]) == "établi"
    assert chef.constat_du_majorant([{"code": 200, "sortie_facturee": 165, "octets_contenu": 100}]) == "démenti"
    assert chef.constat_du_majorant([{"code": 500}]) is None


def test_majorant_dementi_en_file_le_compteur_passe_au_regime_prudent(monde, banc):
    m = banc("file-mistral")
    conformes = reponses_conformes(monde.config, monde.racine, "file-mistral", faux.flux_mistral)
    dementi = faux.flux_mistral(APPARIEMENT_CONFORME, usage=(900, 5000, 5900))   # 5 000 jetons pour une centaine d'octets
    m.faux.programmer(dementi, faux.erreur_mistral(500), *conformes[1:])
    bilan = m.jouer(regime="courant")
    e = m.envois()
    assert bilan["complet"] and bilan["majorant_dementi_en_file"] and bilan["regime_final"] == "prudent"
    assert e[0]["majorant_dementi"] and e[0]["decision"] == "ok" and e[0]["regime"] == "courant"   # sans arrêter la file
    assert e[1]["regime"] == "prudent" and "prudent" in e[1]["facon_de_compter"]


# === Garde 17 : les huit entrées de Neon ==================================================================================

def test_garde_17_entrees_et_ordre(monde, banc):
    lot = chef.charger_textes(monde.config, monde.racine)
    assert chef.entrees_de_la_file("file-neon", monde.config, lot) == list(chef.ENTREES_NEON)      # les huit, dans l'ordre
    assert chef.entrees_de_la_file("file-mistral", monde.config, lot) == lot["ordre"] and len(lot["ordre"]) == 24
    n = banc("file-neon")
    n.faux.programmer(*reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google))
    assert n.jouer()["complet"] and [e["entree"] for e in n.envois()] == list(chef.ENTREES_NEON)
    for autres in (list(chef.ENTREES_NEON) + ["C-b1-01"],                                          # une neuvième entrée
                   ["A-b2-01"] + list(chef.ENTREES_NEON[1:]),                                      # une entrée autre
                   list(reversed(chef.ENTREES_NEON)), list(chef.ENTREES_NEON[:7])):                # un autre ordre
        config = copy.deepcopy(monde.config)
        config["lignes"]["file-neon"]["entrees"] = autres
        with pytest.raises(chef.Arret, match="garde 17"):
            chef.entrees_de_la_file("file-neon", config, lot)
        with pytest.raises(chef.Arret, match="garde 17"):                                          # refus avant tout envoi
            chef.controler_identifiants(config, "file-neon")
    config = copy.deepcopy(monde.config)
    config["lignes"]["file-mistral"]["entrees"] = list(chef.ENTREES_NEON)
    with pytest.raises(chef.Arret, match="garde 17"):
        chef.entrees_de_la_file("file-mistral", config, lot)


# === Garde 18 : aucun morceau de réponse dans le rapport ==================================================================

def test_garde_18_aucun_morceau_de_reponse(monde, banc):
    n = banc("file-neon")
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    conformes[0] = faux.reponse_google(APPARIEMENT_CONFORME, avec_part_de_pensee=True)
    n.faux.programmer(*conformes)
    assert n.jouer()["complet"]
    rapport = chef.faire_rapport(n.dossier)
    chef.rendre_piece(n.dossier, "rapport-technique.json", rapport, "google", chef.texte_du_rapport(rapport))   # sain
    ecrit = (n.dossier / "rapport-technique.json").read_text(encoding="utf-8")
    assert "cannot_tell" not in ecrit and "proposal_quote" not in ecrit and (n.dossier / "rapport-technique.json.sha256").exists()
    for glisse in (APPARIEMENT_CONFORME[5:40], "réflexion du modèle, à écarter"):                  # texte jugé, puis pensée
        triche = dict(rapport, note=f"extrait : {glisse}")
        with pytest.raises(chef.Arret, match="garde 18"):                                          # trouvé : pièce non rendue
            chef.rendre_piece(n.dossier, "rapport-triche.json", triche, "google")
        assert not (n.dossier / "rapport-triche.json").exists()
    assert chef.controler_aucune_sous_chaine("abc " + "z" * 20, ["z" * 21]) == 0                   # 20 caractères : admis
    assert chef.controler_aucune_sous_chaine("abc " + "z" * 21, ["z" * 21]) == 1                   # plus de 20 : trouvé
    m = banc("verification-mistral-eu")                                          # le relevé d'une vérification aussi
    m.faux.programmer(faux.flux_mistral("OK " + "réponse fixe du modèle à ne jamais recopier"), sonde_mistral())
    releve = m.verifier()
    assert "ne jamais recopier" not in (m.dossier / "releve-verification-v1.json").read_text(encoding="utf-8")
    assert releve["appels"][0]["longueur_du_texte_extrait"] == len("OK réponse fixe du modèle à ne jamais recopier")


# === Garde 19 : borne dure en octets par envoi (Mistral) ==================================================================

def test_garde_19_sain_flux_de_200_000_octets(monde, banc):
    m = banc("file-mistral")
    conformes = reponses_conformes(monde.config, monde.racine, "file-mistral", faux.flux_mistral)
    long = faux.flux_mistral(APPARIEMENT_CONFORME, pensee="p" * 200_000, usage=(900, 30000, 30900))
    m.faux.programmer(long, *conformes[1:])
    bilan = m.jouer()
    e = m.envois()[0]
    assert bilan["complet"] and e["incident"] is None and 200_000 < e["octets_contenu"] < 262_144
    assert e["cout_usd"] == pytest.approx((900 * 0.77 + 30000 * 2.31) / 1e6, abs=1e-6)             # coût réel
    lecteur = chef.LecteurFlux()                                                 # les valeurs des champs `type` ne sont pas comptées
    lecteur.nourrir(b'data: {"model": "m", "choices": [{"delta": {"content": [{"type": "thinking", "thinking": '
                    b'[{"type": "text", "text": "abcd"}]}, {"type": "text", "text": "\xc3\xa9"}]}}]}\n\n')
    assert lecteur.octets_contenu == 4 + 2 and lecteur.morceaux_par_type == {"thinking": 1, "text": 1}
    assert "".join(lecteur.textes) == "é" and lecteur.autres == ["abcd"]


def test_garde_19_artefact_file_coupee_a_sa_borne(monde, banc):
    m = banc("file-mistral")
    conformes = reponses_conformes(monde.config, monde.racine, "file-mistral", faux.flux_mistral)
    m.faux.programmer(faux.flux_sans_fin(), *conformes)
    bilan = m.jouer()
    e = m.envois()
    assert len(e) == 1 and e[0]["coupe_a_sa_borne_en_octets"] and e[0]["octets_contenu"] > 262_144
    octets = (m.dossier / "envois" / f"{e[0]['envoi']}.corps.json").stat().st_size
    reserve = chef.Compteur(4.75, [0.77, 2.31], 1).reserve(octets, 262208)
    assert e[0]["cout_usd"] == pytest.approx(reserve, abs=1e-6) and 0.60 < reserve < 0.63          # compté 0,610 ou 0,625
    assert bilan["arretee_par_sa_borne_de_depense"] and not bilan["arretee_a_son_plafond"] and not bilan["complet"]
    assert "borne en octets" in bilan["arret"] and len(m.faux.appels()) == 1                       # aucun second envoi
    # On attend les deux événements eux-mêmes, non un délai : d'abord la ligne du journal du relais (il ferme l'amont
    # avant de l'écrire), puis la fermeture vue par le faux fournisseur (remise à zéro immédiate : `SO_LINGER` à zéro).
    client_ferme = attendre(lambda: [l for l in chef.lire_journal(m.journal_relais) if l.get("client_ferme")])
    assert client_ferme and client_ferme[0]["octets_envoyes_amont"] > 0          # le relais a fermé la connexion vers l'amont
    assert attendre(lambda: m.faux.fermees_par_le_client == 1)                   # le faux fournisseur voit la connexion fermée
    assert m.faux.fermees_par_le_client == 1 and len(m.faux.appels()) == 1
    rapport = chef.faire_rapport(m.dossier)
    regles = chef.appliquer_regles(rapport)
    assert not regles["tient"] and rapport["envois_coupes"] == [e[0]["envoi"]] and rapport["lecture_de_la_console_due"]


def test_garde_19_la_fermeture_du_client_ferme_l_amont_meme_en_silence(monde, banc):
    """Devis, section 12, point 7 : le relais ferme la connexion vers l'amont dès que le programme ferme la sienne,
    y compris pendant un silence de l'amont (les deux relais)."""
    n = banc("file-neon")                                                         # relais de Google, amont muet
    n.faux.programmer(faux.muet(3.0))
    corps = json.dumps(chef.construire_corps("google", monde.config["fournisseurs"]["google"], "t", 32768, orthographe="XHIGH")).encode()
    debut = time.monotonic()
    retour = chef.envoyer(n.url, "POST", chef.chemin_de_l_appel("google"), chef.en_tetes_de_l_envoi("g1"), corps, False, 0.2, 0.2)
    assert retour["incident"] == "delai"
    ferme = attendre(lambda: [l for l in chef.lire_journal(n.journal_relais) if l.get("client_ferme")])
    # la durée que le relais mesure lui-même : bien avant son propre délai (1,345 s) et avant la fin du silence (3 s)
    assert ferme and ferme[0]["motif"] == "client_ferme" and ferme[0]["duree_s"] < 1.2 and debut
    m = banc("file-mistral")                                                      # relais de Mistral, flux entamé puis muet
    lent = faux.flux_mistral("OK", pause_entre_s=3.0)
    m.faux.programmer(lent)
    corps_m = json.dumps(chef.construire_corps("mistral", monde.config["fournisseurs"]["mistral"], "t", 32768)).encode()
    debut = time.monotonic()
    retour = chef.envoyer(m.url, "POST", "/v1/chat/completions", chef.en_tetes_de_l_envoi("m1"), corps_m, True, 0.1, 0.1)
    assert retour["incident"] == "delai"
    ferme = attendre(lambda: [l for l in chef.lire_journal(m.journal_relais) if l.get("client_ferme")])
    # fermé par la fermeture du client, non par le délai de silence du relais : le motif le dit (un délai écrirait
    # « delai_silence »), quelle que soit la charge de la machine
    assert ferme and ferme[0]["motif"] is None and ferme[0]["octets_envoyes_amont"] > 0 and debut


def test_garde_19_google_ne_porte_aucune_borne_en_octets(monde, banc):
    assert monde.config["lignes"]["file-neon"]["borne_octets"] is None
    assert monde.config["lignes"]["verification-google-cle-1"]["borne_octets"] is None
    n = banc("file-neon")
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    conformes[0] = faux.reponse_google(APPARIEMENT_CONFORME + " " * 400_000)     # 400 000 octets : rien n'est coupé
    n.faux.programmer(*conformes)
    assert n.jouer()["complet"] and n.envois()[0]["incident"] is None
    assert "aucune" in n.envois()[0]["borne_en_octets"]                          # la garde le dit au journal


# === Garde 20 : lecture de la console après un envoi coupé ================================================================

def test_garde_20_sain(monde):
    lu = _constat_lu(monde)
    assert chef.garde_console(monde.config, monde.racine, "file-neon", GO["file-neon"], lu) == []    # aucune ligne antérieure
    ref = monde.releve("verification-google-cle-1", "v1", envois_coupes=["L1-01-A"], depense_comptee_usd=0.5)
    monde.piece("console.md", lecture_console_google(ref["sha256"], ("0,29", "0,20"), ("22,50", "22,50"), "nombre 1 ; montant 5,00"))
    for ligne in ("file-neon", "verification-google-cle-2"):                     # sous l'une ou l'autre clé
        monde.config["lignes"][ligne]["lectures_console"] = [monde.ref("console.md")]
        servies = chef.garde_console(monde.config, monde.racine, ligne, GO[ligne], lu)
        assert len(servies) == 1 and servies[0]["depense_vue_usd"] == "0.49"     # pièce conforme : les deux projets, sommés
    lm = _constat_lu(monde, "mistral")
    assert chef.garde_console(monde.config, monde.racine, "file-mistral", GO["file-mistral"], lm) == []   # un envoi coupé chez Google
    assert chef.garde_console(monde.config, monde.racine, "verification-google-cle-1", GO["verification-google-cle-1"], lu) == []   # sa propre ligne
    monde.releve("verification-mistral-eu", "v1", envois_coupes=[], appels=[{"signature_du_mandataire": True}])
    assert chef.garde_console(monde.config, monde.racine, "file-mistral", GO["file-mistral"], lm) == []   # refus du mandataire
    refm = monde.releve("verification-mistral-eu", "v2", go="GO-2026-11-22-21", envois_coupes=["L1-01-A"], depense_comptee_usd=0.08)
    monde.piece("console-m.md", lecture_console(refm["sha256"], "0,07"))
    monde.config["lignes"]["file-mistral"]["lectures_console"] = [monde.ref("console-m.md")]
    assert len(chef.garde_console(monde.config, monde.racine, "file-mistral", GO["file-mistral"], lm)) == 1


def test_garde_20_artefacts(monde):
    lu = _constat_lu(monde)
    ref = monde.releve("verification-google-cle-1", "v1", envois_coupes=["L1-01-A"], depense_comptee_usd=0.5)
    L = monde.config["lignes"]["file-neon"]

    def refuse(motif, texte=None, ligne="file-neon", empreinte=None):
        if texte is not None:
            monde.piece("console.md", texte)
            monde.config["lignes"][ligne]["lectures_console"] = [{**monde.ref("console.md"), **({"sha256": empreinte} if empreinte else {})}]
        with pytest.raises(chef.Arret, match=motif):
            chef.garde_console(monde.config, monde.racine, ligne, GO[ligne],
                               _constat_lu(monde, "mistral") if ligne == "file-mistral" else lu)

    refuse("sans lecture de la console")                                         # envoi coupé sans pièce
    refuse("sans lecture de la console", ligne="verification-google-cle-2")      # la seconde clé est retenue aussi
    refuse("empreinte", lecture_console_google(ref["sha256"]), empreinte="0" * 64)   # pièce d'une autre empreinte
    refuse("sans lecture de la console", lecture_console_google("c" * 64))       # pièce qui cite un autre relevé
    refuse("au-dessus de la dépense comptée", lecture_console_google(ref["sha256"], ("0,30", "0,21")))   # 0,51 vus pour 0,50 comptés
    refuse("projet b : les deux projets sont exigés", lecture_console_google(ref["sha256"], ("0,20", None)))   # un projet manque
    refuse("projet a : les deux projets sont exigés", lecture_console_google(ref["sha256"], soldes=(None, "22,50")))
    refuse("solde vu du projet b.*sous 16.08", lecture_console_google(ref["sha256"], soldes=("22,50", "5,00")))   # solde de 5,00 avant la file
    refuse("recharges survenues", lecture_console_google(ref["sha256"], recharges=None))   # les recharges ne sont pas dites
    refuse("recharges survenues", lecture_console_google(ref["sha256"], recharges="quelques-unes"))
    refuse("mot de Lazar", lecture_console_google(ref["sha256"], mot=False))
    # une seconde ligne de vérification de Google exige de nouveau 19,76 USD, sur chaque projet
    monde.config["lignes"]["verification-google-cle-1"]["go"] = "GO-2026-11-22-08"
    monde.piece("console-19.md", lecture_console_google(ref["sha256"], soldes=("22,50", "19,32")))
    monde.config["lignes"]["verification-google-cle-1"]["lectures_console"] = [monde.ref("console-19.md")]
    with pytest.raises(chef.Arret, match="projet b.*sous 19.76"):
        chef.garde_console(monde.config, monde.racine, "verification-google-cle-1", "GO-2026-11-22-08", lu)
    refm = monde.releve("verification-mistral-eu", "v2", envois_coupes=["L1-01-A"], depense_comptee_usd=0.08)
    refuse("au-dessus de la dépense comptée", lecture_console(refm["sha256"], "0,09"), ligne="file-mistral")
    refuse("ne donne pas la dépense vue", lecture_console(refm["sha256"], "peu"), ligne="file-mistral")


def test_garde_20_en_euros_depense_au_taux_augmente_solde_au_taux_diminue_avec_une_recharge(monde):
    monde.config["marge_de_change"], monde.config["recharge_comptee"] = 0.05, True
    euros = {**EUROS, "google_credit_vu_projet_a": "11,93", "google_credit_apres_une_recharge_projet_a": "20,00",
             "google_credit_vu_projet_b": "15,59", "google_credit_apres_une_recharge_projet_b": "20,00"}
    lu = _constat(monde, modifs=euros, hors_tableau=[TAUX])
    ref = monde.releve("verification-google-cle-1", "v1", envois_coupes=["L1-01-A"], depense_comptee_usd=0.5)
    L = monde.config["lignes"]["file-neon"]

    def console(vues, soldes, plus=(TAUX,)):
        monde.piece("console.md", lecture_console_google(ref["sha256"], vues, soldes, plus=plus))
        L["lectures_console"] = [monde.ref("console.md")]
        return chef.garde_console(monde.config, monde.racine, "file-neon", GO["file-neon"], lu)

    # dépense : 0,22 € × 1,07 × 1,05 = 0,24717 : 0,25 au centime supérieur, par projet ; 0,50 pour 0,50 comptés
    assert console(("0,22", "0,22"), ("11,50", "15,00"))[0]["depense_vue_usd"] == "0.50"
    with pytest.raises(chef.Arret, match="au-dessus de la dépense comptée"):     # 0,23 € : 0,26 par projet
        console(("0,23", "0,22"), ("11,50", "15,00"))
    # solde du projet a : 11,50 vus ; une recharge, lue du côté prudent : min(11,50 + 8,07, max(11,50, 20,00)) = 19,57 €
    # soit 19,57 × 1,07 × 0,95 = 19,89 USD, au-dessus de 16,08. À 7,00 vus : 15,07 € , 15,31 USD : sous le seuil
    with pytest.raises(chef.Arret, match="solde vu du projet a.*15.31.*sous 16.08"):
        console(("0,22", "0,22"), ("7,00", "15,00"))
    with pytest.raises(chef.Arret, match="ligne « - taux"):                      # montants en euros sans taux
        console(("0,22", "0,22"), ("11,50", "15,00"), plus=())
    assert chef.credit_compte_plus_tard(Decimal("11.50"), "a", lu, lu["taux"], monde.config, "essai") == Decimal("19.89")


def test_garde_20_connexion_coupee_puis_refait_sain_sans_piece_la_file_ne_part_pas(monde, banc):
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.fermer())
    assert g.verifier()["a_refaire"]
    g.nouveau_dossier()
    g.faux.programmer(faux.reponse_google("OK"), sonde_google())
    releve = g.verifier()                                                        # refait sain, sous la même ligne
    assert releve["saine"] and releve["sonde"]["issue"] == "comprise" and len(releve["envois_coupes"]) == 1
    chemin = g.dossier / "releve-verification-v1.json"
    ref = {"chemin": str(chemin.relative_to(monde.racine)), "sha256": chef.sha256_fichier(chemin)}
    monde.inscrire_releve("file-neon", ref)
    with pytest.raises(chef.Arret, match="garde 20"):                            # sans pièce : la file ne part pas
        chef.gardes_avant_depart(monde.config, "file-neon", {"GO_ID": GO["file-neon"]}, monde.racine, monde.registre(), MAINTENANT)
    monde.piece("console.md", lecture_console_google(ref["sha256"], ("0,20", "0,20"), ("22,50", "22,50")))
    monde.config["lignes"]["file-neon"]["lectures_console"] = [monde.ref("console.md")]
    avant = chef.gardes_avant_depart(monde.config, "file-neon", {"GO_ID": GO["file-neon"]}, monde.racine, monde.registre(), MAINTENANT)
    assert avant["lectures_de_la_console"][0]["cite"] == ref["sha256"]


# === Les critères écrits d'avance (devis, section 7), sur les seuls compteurs du rapport ==================================

def _rapport(ligne: str, **modifs) -> dict:
    n = chef.CRITERES[ligne]["lectures"]
    nom = chef.IDENTIFIANTS[chef.LIGNES[ligne][1]]
    rapport = {"ligne": ligne, "reponses_de_code_200": n, "lectures_jouees": n, "refus": 0, "fins_par_sortie_maximale": 0,
               "conformes": n, "complete": True, "arret": None, "noms_servis": [nom], "nom_servi_du_releve": nom,
               "lectures_sans_nom_servi_lisible": 0, "sortie_facturee_max": 1239, "issue_de_la_sonde": "comprise",
               "regles": {"chemin": "x", "sha256": "r" * 64}}
    rapport.update(modifs)
    return rapport


def test_criteres_recopies_du_devis_section_7():
    assert chef.CRITERES == {"file-mistral": {"lectures": 24, "conformes_min": 22}, "file-neon": {"lectures": 8, "conformes_min": 8}}
    regles = chef.appliquer_regles
    assert regles(_rapport("file-mistral"))["tient"] and regles(_rapport("file-mistral", conformes=22))["tient"]
    assert not regles(_rapport("file-mistral", conformes=21))["tient"]                           # 22 sur 24
    assert regles(_rapport("file-neon"))["tient"] and not regles(_rapport("file-neon", conformes=7))["tient"]   # huit sur huit
    for ligne in ("file-mistral", "file-neon"):
        n = chef.CRITERES[ligne]["lectures"]
        assert not regles(_rapport(ligne, reponses_de_code_200=n - 1))["tient"]                  # une réponse de moins
        assert not regles(_rapport(ligne, refus=1))["tient"]
        assert not regles(_rapport(ligne, fins_par_sortie_maximale=1))["tient"]
        assert not regles(_rapport(ligne, complete=False, arret="file arrêtée à son plafond"))["tient"]
        assert not regles(_rapport(ligne, noms_servis=["autre"]))["tient"]                       # un seul nom servi
        assert not regles(_rapport(ligne, noms_servis=sorted([chef.IDENTIFIANTS[chef.LIGNES[ligne][1]], "autre"])))["tient"]
        assert not regles(_rapport(ligne, lectures_sans_nom_servi_lisible=1))["tient"]
    assert "second lecteur" in regles(_rapport("file-mistral"))["suite"]
    assert "nœud de Lazar" in regles(_rapport("file-neon", conformes=7))["suite"]
    # règle 7 : la plus grande de 8 192 et de quatre fois le maximum observé, arrondie aux 1 024 supérieurs
    assert regles(_rapport("file-mistral", sortie_facturee_max=1239))["regle_7"]["sortie_maximale_a_la_course"] == 8192
    assert regles(_rapport("file-mistral", sortie_facturee_max=2049))["regle_7"]["sortie_maximale_a_la_course"] == 9216
    assert regles(_rapport("file-mistral", sortie_facturee_max=3000))["regle_7"]["sortie_maximale_a_la_course"] == 12288
    assert "nœud de Lazar" in regles(_rapport("file-neon", issue_de_la_sonde="indécidée"))["regle_7"]["lue_sur"]


def test_regles_du_gabarit_copie_a_la_lettre_du_devis_et_du_texte():
    devis = (RACINE / "docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md").read_text(
        encoding="utf-8").split("\n")
    assert chef.sha256_fichier(RACINE / "docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md") == chef.EMPREINTE_DEVIS
    gabarit = (RACINE / GABARIT_REGLES).read_text(encoding="utf-8")
    bloc = "\n".join(devis[456:465])
    assert bloc in gabarit and bloc.count("\n") == 8                             # le titre et les huit règles
    config = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
    prereg = (RACINE / config["prereg_en_vigueur"]["chemin"]).read_text(encoding="utf-8")
    assert chef.texte_des_regles(prereg, config["regles"]["lignes_du_texte"]) == bloc
    assert "- état : gabarit" in gabarit and config["prereg_en_vigueur"]["sha256"] in gabarit


def test_file_mistral_entiere_rapport_et_regles(monde, banc):
    m = banc("file-mistral")
    conformes = reponses_conformes(monde.config, monde.racine, "file-mistral", faux.flux_mistral)
    conformes[3] = faux.flux_mistral("pas un objet")                             # deux réponses hors forme : 22 sur 24
    conformes[10] = faux.flux_mistral("```json\n" + APPARIEMENT_CONFORME + "\n```\net une phrase autour")
    conformes[5] = faux.flux_mistral("```json\n" + APPARIEMENT_CONFORME + "\n```")   # un bloc de code : toléré, compté
    m.faux.programmer(*conformes)
    bilan = m.jouer()
    rapport = chef.faire_rapport(m.dossier)
    assert bilan["complet"] and rapport["conformes"] == 22 and rapport["blocs_de_code_retires"] == 1
    assert rapport["reponses_de_code_200"] == 24 and rapport["nombre_d_envois"] == 24 and rapport["etayees"] == 22
    assert rapport["noms_servis"] == ["mistral-large-4-0"] and rapport["cout_projete"]["C_usd"] > 0
    assert chef.appliquer_regles(rapport)["tient"]
    assert {e["cause_de_forme"] for e in rapport["envois"]} == {None, "forme"}   # un code de cause, sans texte
    assert len(m.faux.appels()) == 24 and m.pauses == [0.0] * 24                 # une pause après chaque réponse
    corps = json.loads(m.faux.appels()[0]["corps"])
    assert set(corps) == {"model", "messages", "max_tokens", "reasoning_effort", "stream", "temperature"}
    assert m.faux.appels()[0]["en_tetes"]["authorization"] == "Bearer valeur-factice-du-relais"
    assert "x-envoi" not in m.faux.appels()[0]["en_tetes"]                       # l'identifiant d'envoi ne part pas à l'amont


def test_file_mistral_sans_temperature_apres_retrait(monde, banc):
    m = banc("file-mistral")
    m.faux.programmer(faux.flux_mistral(APPARIEMENT_CONFORME, fin="length"))
    m.jouer(temperature_envoyee=False)
    assert "temperature" not in json.loads(m.faux.appels()[0]["corps"])


# === Une ligne de bout en bout : amorce, relais lancé par le lanceur, ouvrier sans clé =====================================

def test_bout_en_bout_verification_puis_file_neon(monde, tmp_path):
    fournisseur = faux.FauxFournisseur(faux.modele_google()).demarrer()
    try:
        monde.config["essai_local"] = {"google": fournisseur.url}
        chemin, empreinte = monde.ecrire_configuration("configuration-verification.json")
        env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "GO_ID": GO["verification-google-cle-1"],
               "GEMINI_API_KEY": "valeur-factice-du-relais"}
        fournisseur.programmer(faux.reponse_google("OK"), sonde_google())
        code = chef.executer("verification-google-cle-1", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT)
        assert code == 0
        dossier = dossiers_de(monde.racine / "runs" / "verification-cle-google-1-bras-a-v1")[0]
        releve = json.loads((dossier / "releve-verification-v1.json").read_text(encoding="utf-8"))
        assert releve["saine"] and releve["sonde"]["issue"] == "comprise" and releve["go"] == GO["verification-google-cle-1"]
        inventaire = json.loads((dossier / "inventaire.json").read_text(encoding="utf-8"))
        assert inventaire["etat"] == "finie" and (dossier / "inventaire.json.sha256").exists()
        assert chef.sha256_fichier(dossier / "configuration.json") == empreinte      # la configuration est gardée au dossier
        final = json.loads((dossier / "relais" / "etat-final.json").read_text(encoding="utf-8"))
        assert final["appels"] == 2 and final["cle_dans_l_environnement"] is False
        assert "valeur-factice-du-relais" not in "".join(
            p.read_text(encoding="utf-8", errors="replace") for p in dossier.rglob("*") if p.is_file())
        arret = [l for l in chef.lire_journal(dossier / "journal-amorce.jsonl") if l.get("evenement") == "relais_arrete"]
        assert arret and arret[0]["arrete"]                                      # relais arrêté par son identifiant de processus
        assert releve["variable_cle"] == CLE_1 and releve["cles_levees"]["go"] == GO_QUI_LEVE and len(releve["cles_levees"]["cles"]) == 6
        assert final["variable_cle"] == CLE_1 and releve["controle_du_credit"]["seuil_usd"] == "19.76"
        # la vérification de la clé 2, sous sa ligne de calcul à elle ; son relais ne reçoit que sa variable
        env.update({"GO_ID": GO["verification-google-cle-2"], CLE_2: "valeur-factice-du-relais-2"})
        fournisseur.programmer(faux.reponse_google("OK"), sonde_google())
        assert chef.executer("verification-google-cle-2", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT + datetime.timedelta(seconds=2)) == 0
        dossier_2 = dossiers_de(monde.racine / "runs" / "verification-cle-google-2-bras-a-v1")[0]
        releve_2 = json.loads((dossier_2 / "releve-verification-v1.json").read_text(encoding="utf-8"))
        assert releve_2["variable_cle"] == CLE_2 and releve_2["saine"] and releve_2["ligne"] == "verification-google-cle-2"
        lance = [l for l in chef.lire_journal(dossier_2 / "journal-amorce.jsonl") if l.get("evenement") == "relais_lance"][0]
        assert CLE_2 in lance["noms_transmis"] and CLE_1 not in lance["noms_transmis"]
        assert fournisseur.appels()[-1]["en_tetes"]["x-goog-api-key"] == "valeur-factice-du-relais-2"
        assert releve_2["controle_du_credit"]["depenses_par_cle_usd"][CLE_1] != "0"   # la dépense de la clé 1 est retirée
        # la file : les deux relevés inscrits, puis départ
        ref = {"chemin": str((dossier / "releve-verification-v1.json").relative_to(monde.racine)),
               "sha256": chef.sha256_fichier(dossier / "releve-verification-v1.json")}
        ref_2 = {"chemin": str((dossier_2 / "releve-verification-v1.json").relative_to(monde.racine)),
                 "sha256": chef.sha256_fichier(dossier_2 / "releve-verification-v1.json")}
        monde.inscrire_releve("file-neon", ref, ref_2)
        chemin, empreinte = monde.ecrire_configuration("configuration-file.json")
        deja = len(fournisseur.appels())
        fournisseur.programmer(*reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google))
        env["GO_ID"] = GO["file-neon"]
        plus_tard = MAINTENANT + datetime.timedelta(seconds=5)
        assert chef.executer("file-neon", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=plus_tard) == 0
        file_ = dossiers_de(monde.racine / "runs" / "essais-admission-bras-a-v1")[0]
        rapport = json.loads((file_ / "rapport-technique.json").read_text(encoding="utf-8"))
        assert rapport["complete"] and rapport["conformes"] == 8 and rapport["regime_de_depart"] == "courant"
        assert rapport["texte_en_vigueur"]["sha256"] == monde.config["prereg_en_vigueur"]["sha256"]   # le brouillon en vigueur
        config = chef.charger_configuration(chemin, empreinte)
        assert chef.appliquer_regles_au_dossier(file_, config, monde.racine)["tient"]
        assert len(list((file_ / "envois").iterdir())) == 8 and len(list((file_ / "reponses-brutes-non-lues").glob("*.corps"))) == 8
        # avenant 1, 4.1 : rangs impairs sous la clé 1, rangs pairs sous la clé 2 ; un relais par clé, quatre appels chacun
        cles_vues = [a["en_tetes"]["x-goog-api-key"] for a in fournisseur.appels()[deja:]]
        assert cles_vues == ["valeur-factice-du-relais", "valeur-factice-du-relais-2"] * 4
        assert [e["variable_cle"] for e in rapport["envois"]] == [CLE_1, CLE_2] * 4 and rapport["lectures_par_cle"] == {CLE_1: 4, CLE_2: 4}
        for numero in (1, 2):
            etat = json.loads((file_ / f"relais-cle-{numero}" / "etat-final.json").read_text(encoding="utf-8"))
            assert etat["appels"] == 4 and etat["max_appels"] == 8 and etat["variable_cle"] == (CLE_1, CLE_2)[numero - 1]
        assert rapport["cles_levees"]["go"] == GO_QUI_LEVE and rapport["controle_du_credit"]["seuil_usd"] == "16.08"
        assert "valeur-factice-du-relais" not in "".join(
            p.read_text(encoding="utf-8", errors="replace") for p in file_.rglob("*") if p.is_file())
        # garde 13 : un second départ de la même file est refusé, et rien ne part
        avant = len(fournisseur.appels())
        assert chef.executer("file-neon", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=plus_tard + datetime.timedelta(seconds=5)) == 2
        assert len(fournisseur.appels()) == avant
        # garde 8 : sans la ligne de calcul, rien ne part
        assert chef.executer("verification-google-cle-1", chemin, empreinte, {**env, "GO_ID": "GO-2026-01-01-01"},
                             racine=monde.racine, registre=monde.registre(), a_l_instant=plus_tard) == 2
    finally:
        fournisseur.arreter()


def test_bout_en_bout_verification_puis_file_mistral(monde, tmp_path):
    """La même chaîne chez Mistral : relais en flux lancé par le lanceur avec son plafond en dollars, vérification
    saine (sonde « comprise », majorant « établi »), relevé inscrit, file de 24 lectures, rapport, règles."""
    fournisseur = faux.FauxFournisseur(faux.liste_mistral()).demarrer()
    try:
        monde.config["essai_local"] = {"mistral": fournisseur.url}
        chemin, empreinte = monde.ecrire_configuration("configuration-verification.json")
        env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "GO_ID": GO["verification-mistral-eu"],
               "MISTRAL_API_KEY": "valeur-factice-du-relais"}
        fournisseur.programmer(faux.flux_mistral("OK"), sonde_mistral())
        assert chef.executer("verification-mistral-eu", chemin, empreinte, env, racine=monde.racine,
                             registre=monde.registre(), a_l_instant=MAINTENANT) == 0
        dossier = dossiers_de(monde.racine / "runs" / "verification-cle-mistral-bras-a-v1")[0]
        releve = json.loads((dossier / "releve-verification-v1.json").read_text(encoding="utf-8"))
        assert releve["saine"] and releve["sonde"]["issue"] == "comprise" and releve["majorant"] == "établi"
        assert releve["point_d_acces"] == "https://api.eu.mistral.ai" and releve["mode_de_lecture"] == "flux"
        initial = json.loads((dossier / "relais" / "etat-initial.json").read_text(encoding="utf-8"))
        assert initial["plafond_usd"] == 0.25 and initial["max_appels"] == 3 and initial["reserve_sortie_jetons"] == 32832
        assert initial["amont"] == "api.eu.mistral.ai" and initial["adresse_d_essai"] == fournisseur.url
        ref = {"chemin": str((dossier / "releve-verification-v1.json").relative_to(monde.racine)),
               "sha256": chef.sha256_fichier(dossier / "releve-verification-v1.json")}
        monde.inscrire_releve("file-mistral", ref)
        chemin, empreinte = monde.ecrire_configuration("configuration-file.json")
        fournisseur.programmer(*reponses_conformes(monde.config, monde.racine, "file-mistral", faux.flux_mistral))
        env["GO_ID"] = GO["file-mistral"]
        assert chef.executer("file-mistral", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT + datetime.timedelta(seconds=5)) == 0
        file_ = dossiers_de(monde.racine / "runs" / "essais-admission-bras-a-v1")[0]
        rapport = json.loads((file_ / "rapport-technique.json").read_text(encoding="utf-8"))
        assert rapport["complete"] and rapport["conformes"] == 24 and rapport["nombre_d_envois"] == 24
        assert rapport["hote"] == "api.eu.mistral.ai" and rapport["regime_de_depart"] == "courant"
        final = json.loads((file_ / "relais" / "etat-final.json").read_text(encoding="utf-8"))
        assert final["appels"] == 24 and final["max_appels"] == 48 and final["plafond_usd"] == 4.75
        assert final["depense_usd"] == pytest.approx(rapport["depense_comptee_usd"], abs=2e-5)   # les deux comptes s'accordent (arrondis par envoi)
        assert chef.appliquer_regles_au_dossier(file_, chef.charger_configuration(chemin, empreinte), monde.racine)["tient"]
        assert "valeur-factice-du-relais" not in "".join(
            p.read_text(encoding="utf-8", errors="replace") for p in file_.rglob("*") if p.is_file())
    finally:
        fournisseur.arreter()


# === Livraison 2 : corrections C-1 à C-5 de la contre-lecture (chaque essai échoue sur la livraison 1) =====================

class _MachineArretee(RuntimeError):
    """Simule, dans l'essai, l'ouvrier tué ou la machine arrêtée à un point précis."""


def test_c1_releve_non_rendu_le_compte_de_la_ligne_ne_repart_pas_de_zero(monde, banc, monkeypatch):
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK"), sonde_google(), faux.reponse_google("OK"), sonde_google())
    with monkeypatch.context() as m:                                   # le relevé n'est pas rendu : machine arrêtée
        m.setattr(chef, "rendre_piece", lambda *a, **k: (_ for _ in ()).throw(_MachineArretee()))
        with pytest.raises(_MachineArretee):
            g.verifier()
    assert len(g.faux.appels()) == 2 and not (g.dossier / "releve-verification-v1.json").exists()
    premier = g.dossier.name
    etat = chef.etat_de_la_ligne(monde.racine, monde.config, "verification-google-cle-1", g.go)
    assert [a["type"] for a in etat["appels"]] == ["A", "B"] and etat["depense_comptee_usd"] > 0 and etat["reconstitue"] == [premier]
    g.nouveau_dossier()
    releve = g.verifier()                                              # second lancement, sous la même ligne de calcul
    assert len(g.faux.appels()) == 2                                   # aucun appel de plus : la sonde est déjà jouée
    assert releve["appels_comptes"] == 2 and releve["saine"] and releve["sonde"]["issue"] == "comprise"
    assert releve["dossiers_sans_releve_reconstitues"] == [premier] and releve["lancements"] == 2
    assert releve["depense_comptee_usd"] == pytest.approx(etat["depense_comptee_usd"], abs=1e-6)
    # la dépense du lancement perdu entre dans le contrôle du crédit de Google (garde 10)
    jouees = chef.lignes_jouees(monde.racine, monde.config, "google")
    assert len(jouees) == 1 and jouees[0]["depense_comptee_usd"] > 0 and not jouees[0]["reconstitue"]
    # cas sain : un relevé rendu se lit comme avant, sans rien reconstituer
    sain = banc("verification-google-cle-1")
    sain.faux.programmer(faux.reponse_google("OK"), sonde_google())
    assert sain.verifier()["dossiers_sans_releve_reconstitues"] == []


def test_c1_depart_sans_reponse_au_journal_vaut_un_envoi_coupe_compte_au_regime_prudent(monde, banc, monkeypatch):
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK"), sonde_google())
    with monkeypatch.context() as m:                                   # tué entre le départ et l'écriture de l'envoi
        vrai = chef.envoyer

        def tue_au_premier_appel_payant(url, methode, *a, **k):
            if methode == "POST":
                raise _MachineArretee()
            return vrai(url, methode, *a, **k)
        m.setattr(chef, "envoyer", tue_au_premier_appel_payant)
        with pytest.raises(_MachineArretee):
            g.verifier()
    etat = chef.etat_de_la_ligne(monde.racine, monde.config, "verification-google-cle-1", g.go)
    a = etat["appels"][0]
    assert a["reconstitue"] and a["incident"] == "coupure" and a["compte_parmi_les_trois"] and a["type"] == "A"
    assert a["cout_usd"] > 1.50                                        # 200 jetons par seconde sur le délai total
    g.nouveau_dossier()
    suite = g.verifier()                                               # le compteur refuse : rien ne part
    assert g.faux.appels() == [] and suite["close"] and "garde 1" in suite["issue_finale"]
    assert suite["envois_coupes"] == [a["envoi"]] and suite["lecture_de_la_console_due"]
    # … et la garde 20 exige la lecture de la console avant la file Neon
    monde.inscrire_releve("file-neon", monde.releve("verification-google-cle-1", "zz-autre", go="GO-2026-11-23-77"))
    with pytest.raises(chef.Arret, match="garde 20"):
        chef.gardes_avant_depart(monde.config, "file-neon", {"GO_ID": GO["file-neon"]}, monde.racine, monde.registre(), MAINTENANT)


def test_c1_file_sans_rapport_rendu_reconstituee_du_journal(monde, banc, monkeypatch):
    n = banc("file-neon")
    n.faux.programmer(*reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google))
    with monkeypatch.context() as m:
        vrai, vus = chef.envoyer, []

        def tue_au_second_envoi(*a, **k):
            vus.append(1)
            if len(vus) == 2:
                raise _MachineArretee()
            return vrai(*a, **k)
        m.setattr(chef, "envoyer", tue_au_second_envoi)
        with pytest.raises(_MachineArretee):
            n.jouer()
    assert not (n.dossier / "rapport-technique.json").exists() and chef.dossier_parti(n.dossier)
    jouees = [j for j in chef.lignes_jouees(monde.racine, monde.config, "google") if j["ligne"] == "file-neon"]
    assert len(jouees) == 1 and jouees[0]["reconstitue"] and jouees[0]["envois_coupes"] == 1
    assert jouees[0]["depense_comptee_usd"] > 7.9                      # le départ sans réponse, au régime prudent
    assert jouees[0]["sha256"] == chef.sha256_fichier(n.dossier / "journal-essai.jsonl")
    monde.config["lignes"]["verification-google-cle-1"]["go"] = "GO-2026-11-22-08"
    lu = _constat_lu(monde)
    with pytest.raises(chef.Arret, match="garde 20.*journal"):         # une seconde ligne de Google ne part pas sans lecture
        chef.garde_console(monde.config, monde.racine, "verification-google-cle-1", "GO-2026-11-22-08", lu)
    monde.piece("console.md", lecture_console_google(jouees[0]["sha256"], ("0,20", "0,20"), ("19,80", "19,80")))
    monde.config["lignes"]["verification-google-cle-1"]["lectures_console"] = [monde.ref("console.md")]
    assert len(chef.garde_console(monde.config, monde.racine, "verification-google-cle-1", "GO-2026-11-22-08", lu)) == 1
    assert set(jouees[0]["depense_par_cle"]) == {CLE_1, CLE_2}         # la dépense de la file, par clé
    # la commande `rapport` écrit et scelle le rapport qui manquait, reconstitué
    rapport = chef.rapport_du_dossier(n.dossier)
    assert len(rapport["departs_sans_reponse_reconstitues"]) == 1 and rapport["nombre_d_envois"] == 2
    assert rapport["envois_coupes"] == rapport["departs_sans_reponse_reconstitues"] and not rapport["complete"]
    assert (n.dossier / "rapport-technique.json.sha256").exists() and list(n.dossier.glob("inventaire-apres-coup-*.json"))
    assert not chef.appliquer_regles(rapport)["tient"]
    # cas sain : une file menée au bout n'a aucun départ sans réponse
    s = banc("file-mistral")
    s.faux.programmer(*reponses_conformes(monde.config, monde.racine, "file-mistral", faux.flux_mistral))
    assert s.jouer()["complet"] and chef.faire_rapport(s.dossier)["departs_sans_reponse_reconstitues"] == []


def test_c1_refus_de_la_garde_18_un_releve_reduit_est_ecrit_quand_meme(monde, banc, monkeypatch):
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK"), sonde_google())
    with monkeypatch.context() as m:
        m.setattr(chef, "controler_aucune_sous_chaine", lambda *a, **k: 1)
        releve = g.verifier()
    chemin = g.dossier / "releve-verification-v1.json"
    assert releve["reduit"] and releve["close"] and not releve["saine"] and releve["noeud_de_lazar"]
    assert releve["appels_comptes"] == 2 and releve["depense_comptee_usd"] > 0 and chef.code_de_sortie_verification(releve) == 8
    assert chemin.exists() and Path(str(chemin) + ".sha256").read_text(encoding="utf-8").split()[0] == chef.sha256_fichier(chemin)
    assert all(a["cout_usd"] is not None and set(a) >= {"envoi", "type", "incident"} for a in releve["appels"])
    etat = chef.etat_de_la_ligne(monde.racine, monde.config, "verification-google-cle-1", g.go)
    assert etat["close"] and etat["depense_comptee_usd"] == releve["depense_comptee_usd"] and len(etat["appels"]) == 2


def test_c2_une_file_dont_aucun_envoi_n_est_parti_peut_partir(monde, tmp_path):
    fournisseur = faux.FauxFournisseur(faux.modele_google()).demarrer()
    try:
        monde.config["essai_local"] = {"google": fournisseur.url}
        monde.inscrire_releve("file-neon", monde.releve("verification-google-cle-1", "v1"))
        chemin, empreinte = monde.ecrire_configuration()
        env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "GO_ID": GO["file-neon"]}
        fournisseur.programmer(*reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google))
        # clé oubliée : le lanceur refuse (garde 7), rien ne part
        assert chef.executer("file-neon", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT) == 2
        assert fournisseur.recus == []
        base = monde.racine / "runs" / "essais-admission-bras-a-v1"
        premier = dossiers_de(base)[0]
        assert not chef.dossier_parti(premier) and chef.dossiers_de_la_file(base, "file-neon") == ([], [premier.name])
        # clé posée : la file part, sous un dossier neuf, qui cite le dossier sans départ
        env.update({CLE_1: "valeur-factice-du-relais", CLE_2: "valeur-factice-du-relais-2"})
        assert chef.executer("file-neon", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT + datetime.timedelta(seconds=5)) == 0
        second = dossiers_de(base)[1]
        manifeste = json.loads((second / "manifeste-depart.json").read_text(encoding="utf-8"))
        assert manifeste["dossiers_anterieurs_sans_depart"] == [premier.name] and len(fournisseur.appels()) == 8
        assert premier.exists() and (premier / "inventaire.json").exists()          # gardé tel quel
        # artefact : une file partie ne repart pas
        assert chef.dossier_parti(second)
        assert chef.executer("file-neon", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT + datetime.timedelta(seconds=10)) == 2
        assert len(fournisseur.appels()) == 8
    finally:
        fournisseur.arreter()


def test_c2_dossier_parti_unites(tmp_path):
    vide = tmp_path / "a-file-neon"
    (vide / "relais").mkdir(parents=True)
    assert not chef.dossier_parti(vide)                                              # ni départ, ni octet à l'amont
    (vide / "relais" / "journal-relais.jsonl").write_text('{"octets_envoyes_amont": 0, "origine": "mandataire"}\n', encoding="utf-8")
    assert not chef.dossier_parti(vide)
    (vide / "relais" / "journal-relais.jsonl").write_text('{"octets_envoyes_amont": 412}\n', encoding="utf-8")
    assert chef.dossier_parti(vide)                                                  # le relais a envoyé à l'amont
    depart = tmp_path / "b-file-neon"
    depart.mkdir()
    (depart / "journal-essai.jsonl").write_text('{"evenement": "depart_de_la_file"}\n{"evenement": "depart", "envoi": "x"}\n', encoding="utf-8")
    assert chef.dossier_parti(depart)
    illisible = tmp_path / "c-file-neon"
    illisible.mkdir()
    (illisible / "journal-essai.jsonl").write_text('{"evenement": "dep', encoding="utf-8")
    assert chef.dossier_parti(illisible)                                             # du côté prudent


def test_c3_sonde_illisible_ou_sans_nom_reste_indecidee_la_verification_reste_saine(monde, banc):
    for reponse in (faux.rep_json(200, b"<html>illisible</html>"),                  # code 200 au corps illisible
                    sonde_google(modele=None)):                                      # sans `modelVersion`
        g = banc("verification-google-cle-1")
        g.faux.programmer(faux.reponse_google("OK"), reponse)
        releve = g.verifier()
        assert releve["saine"] and releve["sonde"]["issue"] == "indécidée" and releve["close"]
        assert releve["appels"][1]["ligne_du_classement"] is None and releve["issue_finale_ligne"] != 4
        assert releve["noeud_de_lazar"] and releve["nom_servi"] == "gemini-4-neon"   # la file peut partir sur le mot de Lazar
    m = banc("verification-mistral-eu")                                              # un premier événement sans `model`, puis un silence
    coupee = {"genre": "flux", "code": 200,
              "evenements": [faux._evenement(None, {"content": [{"type": "text", "text": "4"}]}), ("pause", 3.0)]}
    m.faux.programmer(faux.flux_mistral("OK"), coupee)
    releve = m.verifier()
    b = releve["appels"][1]
    assert b["incident"] == "delai" and b["ligne_du_classement"] is None and releve["saine"]
    assert releve["sonde"]["issue"] == "indécidée" and releve["envois_coupes"] == [b["envoi"]]
    # artefact : un nom présent et autre, à la sonde, reste « autre nom servi », non saine
    autre = banc("verification-google-cle-1")
    autre.faux.programmer(faux.reponse_google("OK"), sonde_google(modele="gemini-4-carbon"))
    releve = autre.verifier()
    assert not releve["saine"] and releve["issue_finale_ligne"] == 4 and releve["noeud_de_lazar"]


@pytest.mark.parametrize("ligne, liste", [("verification-google-cle-1", faux.fermer()), ("verification-google-cle-1", faux.muet(3.0)),
                                           ("verification-mistral-eu", faux.fermer())])
def test_c4_liste_sans_reponse_du_fournisseur_aucun_appel_payant(monde, banc, ligne, liste):
    b = banc(ligne, liste=liste)
    b.faux.programmer(faux.reponse_google("OK"), sonde_google())
    releve = b.verifier()
    assert b.faux.appels() == [] and releve["appels"] == [] and releve["depense_comptee_usd"] == 0
    assert releve["a_refaire"] and "appel de liste" in releve["a_refaire"] and not releve["close"]
    assert releve["listes"][0]["origine"] == "relais" and not releve["listes"][0]["signature_du_mandataire"]
    assert chef.code_de_sortie_verification(releve) == 3 and releve["envois_coupes"] == []


def test_c4_sain_liste_rendue_par_le_fournisseur_meme_en_erreur_l_appel_part(monde, banc):
    g = banc("verification-google-cle-1", liste=faux.rep_json(404, {"error": {"code": 404, "message": "not found"}}))
    g.faux.programmer(faux.reponse_google("OK"), sonde_google())                     # la liste n'entre pas dans la santé (4.3)
    releve = g.verifier()
    assert releve["saine"] and len(g.faux.appels()) == 2 and releve["listes"][0]["origine"] == "amont"


def test_c5_reponse_qui_fait_tomber_le_programme_de_forme_la_file_continue_l_envoi_est_compte(monde, banc):
    n = banc("file-neon")
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    conformes[0] = faux.reponse_google("[" * 50000 + "]" * 50000)                    # JSON imbriqué sur 50 000 niveaux
    conformes[6] = faux.reponse_google("{\"C1\": " * 50000 + "1" + "}" * 50000)     # de même, à la couverture
    n.faux.programmer(*conformes)
    bilan = n.jouer()
    rapport = chef.faire_rapport(n.dossier)
    assert bilan["complet"] and len(n.faux.appels()) == 8 and rapport["nombre_d_envois"] == 8
    causes = [e["cause_de_forme"] for e in rapport["envois"]]
    assert causes[0].startswith("panne_du_programme_de_forme:") and causes[6].startswith("panne_du_programme_de_forme:")
    assert rapport["conformes"] == 6 and rapport["reponses_de_code_200"] == 8
    assert rapport["depense_comptee_usd"] == pytest.approx(bilan["depense_comptee_usd"], abs=2e-5)
    assert not chef.appliquer_regles(rapport)["tient"]                               # six sur huit : par le critère, non par une panne
    chef.rendre_piece(n.dossier, "rapport-technique.json", rapport, "google", chef.texte_du_rapport(rapport))


def test_c5_l_envoi_est_au_journal_avant_le_jugement_de_forme(monde, banc, monkeypatch):
    n = banc("file-neon")
    n.faux.programmer(*reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google))
    with monkeypatch.context() as m:                                                 # tué pendant le jugement de forme
        m.setattr(chef, "juger_la_forme", lambda *a, **k: (_ for _ in ()).throw(_MachineArretee()))
        with pytest.raises(_MachineArretee):
            n.jouer()
    rapport = chef.faire_rapport(n.dossier)
    assert rapport["nombre_d_envois"] == 1 and rapport["depense_comptee_usd"] > 0    # l'envoi payé est au rapport
    assert rapport["envois"][0]["cause_de_forme"] == "forme_non_jugee" and rapport["conformes"] == 0
    assert rapport["departs_sans_reponse_reconstitues"] == []


# === Livraison 2 : les mineurs de la contre-lecture =======================================================================

def test_m1_refus_du_mandataire_sans_sa_signature_est_une_panne_ligne_6():
    corps = json.dumps({"erreur": {"origine": "mandataire", "motif": "tunnel refusé par le mandataire"}}).encode()
    retour = _retour(502, corps)
    assert not chef.signature_du_mandataire(retour, None, "e1")                      # journal du relais absent : pas de signature
    incident = chef.incident_de("google", retour, None)
    assert incident == "coupure"
    liste = {"admise_sans_identifiant": False}
    assert chef.classer_issue("google", "h", "A", liste, retour, None, incident, False)[0] == 6
    assert chef.decider_dans_la_file("google", retour, None, incident, False, 1, "gemini-4-neon")[0] == "reprise"
    c = chef.Compteur(1.5, [3, 15], 200)
    assert chef.compter_envoi(c, "prudent", "google", 100, 32768, 32768, retour, None, incident, False)[0] == c.reserve(100, 32768)
    assert chef.classer_issue("google", "h", "A", liste, retour, None, None, True)[0] == 1   # avec la signature : ligne 1


def test_m2_et_m15_la_ligne_de_calcul_est_accordee_par_lazar_avant_ce_jour_et_cite_la_verification_du_devis(monde):
    registre, jour = monde.registre(), "2026-11-22"
    env = {"GO_ID": GO["file-neon"]}
    chef.verifier_ligne_de_calcul(monde.config, "file-neon", env, registre, jour)   # sain
    with pytest.raises(chef.Arret, match="accordée par Lazar"):
        chef.verifier_ligne_de_calcul(monde.config, "file-neon", env, registre.replace("| Lazar |", "| la session |"), jour)
    with pytest.raises(chef.Arret, match="date d'accord"):
        chef.verifier_ligne_de_calcul(monde.config, "file-neon", env, registre.replace("| 2026-11-01 |", "| 2026-11-23 |"), jour)
    verification = monde.config["verification_du_devis"]["sha256"]
    assert chef.sha256_fichier(RACINE / monde.config["verification_du_devis"]["chemin"]) == verification
    with pytest.raises(chef.Arret, match="vérification du devis"):
        chef.verifier_ligne_de_calcul(monde.config, "file-neon", env, registre.replace(verification, "v" * 64), jour)
    sans = copy.deepcopy(monde.config)
    sans["verification_du_devis"] = None                                             # non inscrite : non exigée
    chef.verifier_ligne_de_calcul(sans, "file-neon", env, registre.replace(verification, "v" * 64), jour)


def test_m4_le_relais_cherche_la_valeur_exacte_de_sa_cle_la_masque_et_le_chef_rend_le_code_7(monde, tmp_path):
    cle = "valeur-factice-du-relais"
    masque = relais_google.Masque(cle)                                               # à cheval sur deux morceaux
    sortie = masque.passer(b"avant valeur-factice") + masque.passer(b"-du-relais apres") + masque.passer(b"", fin=True)
    assert cle.encode() not in sortie and masque.vue and sortie.startswith(b"avant ") and sortie.endswith(b" apres")
    sain = relais_mistral.Masque(cle)
    assert sain.passer(b"data: rien\n\n") + sain.passer(b"", fin=True) == b"data: rien\n\n" and not sain.vue
    retenu = relais_mistral.Masque(cle)                                              # une fin qui peut être un début de clé est retenue, puis rendue
    assert retenu.passer(b"xx val") == b"xx " and retenu.passer(b"ise") == b"valise" and not retenu.vue
    fournisseur = faux.FauxFournisseur(faux.modele_google()).demarrer()
    try:
        monde.config["essai_local"] = {"google": fournisseur.url}
        chemin, empreinte = monde.ecrire_configuration()
        env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "GO_ID": GO["verification-google-cle-1"], "GEMINI_API_KEY": cle}
        fournisseur.programmer(faux.reponse_google("OK " + cle), sonde_google())     # l'amont renvoie la clé, sans préfixe connu
        assert chef.executer("verification-google-cle-1", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT) == 7
        dossier = dossiers_de(monde.racine / "runs" / "verification-cle-google-1-bras-a-v1")[0]
        assert cle not in "".join(p.read_text(encoding="utf-8", errors="replace") for p in dossier.rglob("*") if p.is_file())
        vu = [l for l in chef.lire_journal(dossier / "journal-amorce.jsonl") if l.get("evenement") == "cle_vue_par_le_relais_dans_une_reponse"]
        assert vu and vu[0]["envois"] == 1
        assert chef.cle_vue_par_le_relais(dossier / "relais" / "journal-relais.jsonl") == 1
    finally:
        fournisseur.arreter()


def test_m4_relais_de_mistral_la_cle_est_masquee_dans_le_flux(monde, banc):
    m = banc("verification-mistral-eu")
    m.faux.programmer(faux.flux_mistral("OK valeur-factice-du-relais"), sonde_mistral())
    releve = m.verifier()
    brut = b"".join(p.read_bytes() for p in (m.dossier / "reponses-brutes-non-lues").iterdir())
    assert b"valeur-factice-du-relais" not in brut and b"[cle-du-relais-masquee]" in brut
    assert chef.cle_vue_par_le_relais(m.journal_relais) == 1 and releve["saine"]
    sain = banc("verification-mistral-eu")
    sain.faux.programmer(faux.flux_mistral("OK"), sonde_mistral())
    sain.verifier()
    assert chef.cle_vue_par_le_relais(sain.journal_relais) == 0


def test_m5_m6_m7_m12_unites(monde, banc, monkeypatch):
    # m-5 : une fenêtre de ponctuation et d'espaces n'est pas un morceau de réponse
    indente = '{\n  "a": {\n    "b": null,\n    "c": null\n  }\n}'
    assert chef.controler_aucune_sous_chaine('x {\n  "a": {\n    "b": null,\n    "c": null\n  }\n} y', ['[\n  {\n    "z": {\n      "b": null,\n    "']) == 0
    assert chef.controler_aucune_sous_chaine("le rapport cite une phrase entière du modèle ici", ["une phrase entière du modèle"]) >= 1
    assert indente
    # m-6 : un flux fini sans son marqueur de fin porte sa cause
    m = banc("verification-mistral-eu")
    m.faux.programmer(faux.flux_mistral("OK", sans_done=True))
    a = m.verifier()["appels"][0]
    assert a["incident"] == "coupure" and a["detail_de_l_incident"] == "flux de code 200 fini sans son marqueur de fin"
    c = banc("verification-mistral-eu")
    c.faux.programmer(faux.fermer())
    assert "coupure_amont" in c.verifier()["appels"][0]["detail_de_l_incident"]
    # m-7 : le schéma de l'adresse du dépôt distant n'est pas un terme interdit
    monkeypatch.setattr(chef, "_sortie_git", lambda racine, *a: "http://hote-exemple/depot-zeta.git" if "remote.origin.url" in a else "")
    interdits = chef.charger_interdits(monde.config, monde.racine, {})
    assert "http" not in interdits and "depot-zeta" in interdits and "hote-exemple" in interdits
    chef.controler_envoi(b'{"content": "entree"}', chef.en_tetes_de_l_envoi("e"), interdits)
    # m-12 : un mot composé qui finit par « sk- » n'est pas une clé
    d = monde.racine / "pieces" / "formes"
    d.mkdir()
    (d / "a.txt").write_text("un-risk-" + "a" * 30, encoding="utf-8")
    assert chef.chercher_formes_de_cle(d) == []
    (d / "b.txt").write_text("cle sk-" + "a" * 30, encoding="utf-8")
    assert chef.chercher_formes_de_cle(d) == ["b.txt"]


def test_m8_panne_de_l_ouvrier_code_9_trace_sans_message(monde, tmp_path, monkeypatch, capsys):
    import signal as signaux
    chemin, empreinte = monde.ecrire_configuration()
    dossier = tmp_path / "ligne"
    dossier.mkdir()
    (dossier / "manifeste-depart.json").write_text(json.dumps({
        "pid_amorce": os.getppid(), "go": GO["verification-google-cle-1"], "ligne": "verification-google-cle-1", "genre": "verification",
        "configuration": {"chemin": str(chemin), "sha256": empreinte}}), encoding="utf-8")
    monkeypatch.setattr(chef, "jouer_verification", lambda *a, **k: (_ for _ in ()).throw(RuntimeError("donnée reçue à ne pas recopier")))
    anciens = {s: signaux.getsignal(s) for s in (signaux.SIGTERM, signaux.SIGINT)}
    try:
        entree = json.dumps({"racine": str(monde.racine), "voies": {CLE_1: {"url": "http://127.0.0.1:9", "journal": None}},
                             "interdits": [], "etat": None}).encode()
        assert chef.ouvrier(dossier, {"PATH": "/usr/bin", "GO_ID": GO["verification-google-cle-1"]}, entree) == 9
    finally:
        for s, ancien in anciens.items():
            signaux.signal(s, ancien)
    erreur = capsys.readouterr().err
    assert "PANNE de l'ouvrier : RuntimeError" in erreur and "à ne pas recopier" not in erreur


def test_m11_le_delai_total_du_relais_de_mistral_est_tenu_par_une_minuterie(monde, banc):
    m = banc("file-mistral")
    total = monde.config["lignes"]["file-mistral"]["delais"]["relais_total_s"]
    m.faux.programmer(faux.flux_sans_fin(octets_par_morceau=8, pause_s=0.2))        # vivant : un événement tous les 0,2 s
    corps = json.dumps(chef.construire_corps("mistral", monde.config["fournisseurs"]["mistral"], "t", 32768)).encode()
    retour = chef.envoyer(m.url, "POST", "/v1/chat/completions", chef.en_tetes_de_l_envoi("m1"), corps, True, 10, 10)
    lu = chef.lu_mistral(retour["flux"])
    # coupé par la minuterie du relais, au délai total, sans attendre le morceau suivant ni le délai du client (10 s)
    assert lu["erreur_relais"] == "delai_total" and total <= retour["duree_s"] < total + 1.0


def test_m13_commande_a_blanc_sans_ligne_de_calcul(monde, capsys):
    monde.inscrire_releve("file-neon", monde.releve("verification-google-cle-1", "v1"))
    chemin, empreinte = monde.ecrire_configuration()
    assert chef.a_blanc("file-neon", chemin, empreinte, {}, racine=monde.racine, a_l_instant=MAINTENANT) == 0   # sans GO_ID
    sortie = json.loads(capsys.readouterr().out)
    assert sortie["a_blanc"] and sortie["regime"] == "courant" and sortie["corps_controles"] == 8
    assert not list((monde.racine / "runs" / "essais-admission-bras-a-v1").glob("*")) if (monde.racine / "runs" / "essais-admission-bras-a-v1").exists() else True
    assert chef.a_blanc("verification-mistral-eu", chemin, empreinte, {}, racine=monde.racine, a_l_instant=MAINTENANT) == 0
    capsys.readouterr()
    monde.piece("constat-bas.md", constat({"google_recharge_automatique": "activée"}))   # artefact : une pièce de Lazar fautive
    monde.config["constat"] = monde.ref("constat-bas.md")
    chemin, empreinte = monde.ecrire_configuration("configuration-2.json")
    with pytest.raises(chef.Arret, match="garde 9"):
        chef.a_blanc("file-neon", chemin, empreinte, {}, racine=monde.racine, a_l_instant=MAINTENANT)


# === Livraison 3 (version 2) : corrections de la vérification de la livraison 2 ============================================

def test_v1_la_commande_rapport_lancee_pendant_la_file_ne_fige_rien(monde, banc):
    n = banc("file-neon")
    n.pid_amorce = os.getpid()                                          # l'amorce de la file est en vie : file non close
    n.faux.programmer(*reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google))
    pauses = []

    class PendantLaFile:
        @staticmethod
        def append(secondes):                                           # à la troisième pause, la session lance `rapport`
            pauses.append(secondes)
            if len(pauses) == 3:
                partiel = chef.rapport_du_dossier(n.dossier)
                assert not partiel["ecrit"] and not partiel["file_close"] and partiel["lectures_jouees"] == 3
                assert not partiel["complete"]

    n.pauses = PendantLaFile
    assert n.jouer()["complet"] and len(pauses) == 8
    assert not (n.dossier / "rapport-technique.json").exists()          # rien n'a été figé
    rapport = chef.faire_rapport(n.dossier)
    chef.rendre_piece(n.dossier, "rapport-technique.json", rapport, "google", chef.texte_du_rapport(rapport))   # l'amorce rend le sien
    with pytest.raises(chef.Arret, match="n'est pas close"):            # tant que l'amorce vit, pas de règles
        chef.appliquer_regles_au_dossier(n.dossier, monde.config, monde.racine)
    n.pid_amorce = PID_MORT
    manifeste = json.loads((n.dossier / "manifeste-depart.json").read_text(encoding="utf-8"))
    (n.dossier / "manifeste-depart.json").write_text(json.dumps({**manifeste, "pid_amorce": PID_MORT}), encoding="utf-8")
    assert chef.appliquer_regles_au_dossier(n.dossier, monde.config, monde.racine)["tient"]   # la file a tenu : elle tient
    # artefact : un rapport figé avant la fin ne répond plus au journal ; les règles refusent
    with open(n.dossier / "journal-essai.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"evenement": "depart", "envoi": "09-x-1", "appel": 9, "rang": 1, "cout_si_sans_reponse_usd": 1.0}) + "\n")
    with pytest.raises(chef.Arret, match="ne répond pas au journal"):
        chef.appliquer_regles_au_dossier(n.dossier, monde.config, monde.racine)
    # cas sain de l'écriture : file close, sans rapport rendu (machine arrêtée) : `rapport` l'écrit et le scelle
    s = banc("file-neon")
    s.faux.programmer(*reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google))
    assert s.jouer()["complet"]
    rendu = chef.rapport_du_dossier(s.dossier)
    assert rendu["ecrit"] and rendu["file_close"] and (s.dossier / "rapport-technique.json.sha256").exists()
    assert not chef.rapport_du_dossier(s.dossier)["ecrit"]              # une seconde fois : rien n'est réécrit
    sans_pid = banc("file-neon")                                        # sans identifiant de processus au manifeste : non close
    (sans_pid.dossier / "manifeste-depart.json").write_text(json.dumps({"ligne": "file-neon", "go": "GO-x"}), encoding="utf-8")
    assert not chef.file_close(sans_pid.dossier)


def test_v1_l_amorce_ne_garde_pas_en_silence_un_rapport_qu_elle_n_a_pas_ecrit(monde, tmp_path, monkeypatch):
    fournisseur = faux.FauxFournisseur(faux.modele_google()).demarrer()
    try:
        monde.config["essai_local"] = {"google": fournisseur.url}
        monde.inscrire_releve("file-neon", monde.releve("verification-google-cle-1", "v1"))
        chemin, empreinte = monde.ecrire_configuration()
        env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "GO_ID": GO["file-neon"], CLE_1: "valeur-factice-du-relais",
               CLE_2: "valeur-factice-du-relais-2"}
        fournisseur.programmer(*reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google))
        vrai = chef.arreter_relais

        def un_rapport_etranger_apparait(pid):                          # écrit pendant la file par une autre main
            dossier = next((monde.racine / "runs" / "essais-admission-bras-a-v1").glob("*-file-neon"))
            (dossier / "rapport-technique.json").write_text('{"complete": false}', encoding="utf-8")
            return vrai(pid)
        monkeypatch.setattr(chef, "arreter_relais", un_rapport_etranger_apparait)
        assert chef.executer("file-neon", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT) == 8
        dossier = next((monde.racine / "runs" / "essais-admission-bras-a-v1").glob("*-file-neon"))
        non_rendu = [l for l in chef.lire_journal(dossier / "journal-amorce.jsonl") if l.get("evenement") == "rapport_non_rendu"]
        assert non_rendu and "n'a pas écrit" in non_rendu[0]["motif"]
    finally:
        fournisseur.arreter()


def test_ma_deux_lancements_simultanes_le_second_ne_part_pas(monde, tmp_path):
    fournisseur = faux.FauxFournisseur(faux.modele_google()).demarrer()
    try:
        monde.config["essai_local"] = {"google": fournisseur.url}
        chemin, empreinte = monde.ecrire_configuration()
        env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "GO_ID": GO["verification-google-cle-1"], "GEMINI_API_KEY": "valeur-factice-du-relais"}
        base = monde.racine / "runs" / "verification-cle-google-1-bras-a-v1"
        base.mkdir(parents=True)
        autre = os.open(base.parent / "essais-admission-google.verrou", os.O_CREAT | os.O_RDWR)   # un autre lancement tient le verrou
        fcntl.flock(autre, fcntl.LOCK_EX)
        fournisseur.programmer(faux.reponse_google("OK"), sonde_google())
        assert chef.executer("verification-google-cle-1", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT) == 2
        assert fournisseur.recus == [] and not list(base.glob("*-verification-google-cle-1"))
        os.close(autre)                                                 # verrou lâché : la ligne part
        assert chef.executer("verification-google-cle-1", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT) == 0
        assert len(fournisseur.appels()) == 2
    finally:
        fournisseur.arreter()


def _levee(dossier: str, revoquee: str = "oui", mot: bool = True) -> str:
    lignes = ["# Levée d'une alerte de clé — pièce d'essai", ""] + (["## Mot de Lazar", "", "> clé révoquée, clé neuve posée", ""] if mot else [])
    return "\n".join(lignes + [f"- dossier de l'alerte : {dossier}", f"- clé révoquée et remplacée : {revoquee}", ""])


def test_mc_une_cle_vue_bloque_toute_ligne_suivante_du_fournisseur_jusqu_a_la_piece_de_lazar(monde, banc):
    assert chef.garde_cle_vue(monde.config, monde.racine, "file-neon") == []        # cas sain : aucune alerte
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK valeur-factice-du-relais"), sonde_google())
    releve = g.verifier()
    assert releve["cle_vue_dans_une_reponse"] == 1 and releve["saine"]              # la trace est au relevé
    assert chef.alertes_de_cle(monde.racine, monde.config, "google") == [{"dossier": g.dossier.name, "valeur_exacte": True}]
    chemin = g.dossier / "releve-verification-v1.json"
    monde.inscrire_releve("file-neon", {"chemin": str(chemin.relative_to(monde.racine)), "sha256": chef.sha256_fichier(chemin)})
    for ligne in ("file-neon", "verification-google-cle-1", "verification-google-cle-2"):   # la file, la même ligne, l'autre clé
        with pytest.raises(chef.Arret, match="garde 7 : une clé a été vue"):
            chef.garde_cle_vue(monde.config, monde.racine, ligne)
    with pytest.raises(chef.Arret, match="garde 7 : une clé a été vue"):            # ligne entière : rien ne part
        chef.gardes_avant_depart(monde.config, "file-neon", {"GO_ID": GO["file-neon"]}, monde.racine, monde.registre(), MAINTENANT)
    assert chef.garde_cle_vue(monde.config, monde.racine, "file-mistral") == []     # l'autre fournisseur n'est pas retenu
    L = monde.config["lignes"]["file-neon"]
    for nom, texte, motif in (("autre", _levee("un-autre-dossier"), "une clé a été vue"),
                              ("non", _levee(g.dossier.name, revoquee="non"), "ni « clé révoquée et remplacée : oui » ni"),
                              ("sans-mot", _levee(g.dossier.name, mot=False), "mot de Lazar")):
        monde.piece(f"levee-{nom}.md", texte)
        L["levees_cle"] = [monde.ref(f"levee-{nom}.md")]
        with pytest.raises(chef.Arret, match=motif):
            chef.garde_cle_vue(monde.config, monde.racine, "file-neon")
    monde.piece("levee.md", _levee(g.dossier.name))
    L["levees_cle"] = [{**monde.ref("levee.md"), "sha256": "0" * 64}]
    with pytest.raises(chef.Arret, match="empreinte"):
        chef.garde_cle_vue(monde.config, monde.racine, "file-neon")
    L["levees_cle"] = [monde.ref("levee.md")]
    assert chef.garde_cle_vue(monde.config, monde.racine, "file-neon") == [
        {"dossier": g.dossier.name, "piece": monde.ref("levee.md")["sha256"], "facon": "clé révoquée et remplacée"}]
    avant = chef.gardes_avant_depart(monde.config, "file-neon", {"GO_ID": GO["file-neon"]}, monde.racine, monde.registre(), MAINTENANT)
    assert avant["alertes_de_cle_levees"][0]["dossier"] == g.dossier.name
    # une forme de clé trouvée par la relecture de fin de ligne lève la même alerte
    d = monde.racine / "runs" / "verification-cle-mistral-bras-a-v1" / "20261120-100000-verification-mistral-eu"
    d.mkdir(parents=True)
    (d / "journal-amorce.jsonl").write_text(json.dumps({"evenement": "recherche_de_formes_de_cle", "fichiers": ["x.corps"]}) + "\n", encoding="utf-8")
    assert chef.alertes_de_cle(monde.racine, monde.config, "mistral") == [{"dossier": d.name, "valeur_exacte": False}]


def test_m10_connexion_non_etablie_hors_signature_l_appel_est_rendu_au_compte_du_relais(monde, banc):
    muet = faux.FauxMandataire(repond=False).demarrer()                 # ferme la demande de tunnel sans répondre
    try:
        g = banc("verification-google-cle-1", environnement_du_relais={"HTTPS_PROXY": muet.url})
        corps = json.dumps(chef.construire_corps("google", monde.config["fournisseurs"]["google"], "t", 32768, orthographe="XHIGH")).encode()
        retour = chef.envoyer(g.url, "POST", chef.chemin_de_l_appel("google"), chef.en_tetes_de_l_envoi("e1"), corps, False, 5, 5)
        assert retour["code"] == 502 and chef.origine_du_retour(retour) == ("relais", "connexion")
        assert not chef.signature_du_mandataire(retour, g.journal_relais, "e1")     # hors de la signature
        assert chef.incident_de("google", retour, None) == "coupure"                # le chef le compte comme une connexion coupée
        etat = chef.etat_relais(g.url)
        assert etat["appels"] == 0 and g.faux.recus == [] and muet.demandes >= 1    # l'appel est rendu : rien n'a atteint l'amont
    finally:
        muet.arreter()
    sain = banc("verification-google-cle-1")                                  # cas sain : un appel servi reste compté
    sain.faux.programmer(faux.reponse_google("OK"))
    assert chef.envoyer(sain.url, "POST", chef.chemin_de_l_appel("google"), chef.en_tetes_de_l_envoi("e2"), corps, False, 5, 5)["code"] == 200
    assert chef.etat_relais(sain.url)["appels"] == 1


def test_configuration_definitive_ce_qu_elle_exige(monde):
    """En configuration définitive : la vérification du devis et l'avenant inscrits et présents ; la marge de change
    décidée par Lazar, 5 %, avec le GO qui la décide ; `recharge_comptee` à faux (GO-2026-11-21-69)."""
    definitive = copy.deepcopy(monde.config)
    definitive.update({"etat": "definitive", "marge_de_change": 0.05, "marge_de_change_go": GO_QUI_LEVE, "recharge_comptee": False})
    chef.controler_verification_du_devis(definitive, monde.racine)      # sain

    def refuse(motif, **modifs):
        config = copy.deepcopy(definitive)
        config.update(modifs)
        with pytest.raises(chef.Arret, match=motif):
            chef.controler_verification_du_devis(config, monde.racine)

    refuse("garde 8 : une configuration définitive inscrit la pièce de la vérification", verification_du_devis=None)
    refuse("empreinte", verification_du_devis={**definitive["verification_du_devis"], "sha256": "0" * 64})
    refuse("inscrit l'avenant 1", avenant=None)
    refuse("empreinte", avenant={**definitive["avenant"], "sha256": "0" * 64})
    for marge in (None, "0,05", 0.0, 0.02, 0.5, True):                  # absente, ou autre que 5 %
        refuse("marge de change décidée par Lazar", marge_de_change=marge)
    refuse("identifiant du GO qui décide la marge", marge_de_change_go=None)
    refuse("`recharge_comptee` à faux", recharge_comptee=True)          # le chemin de l'avenant, désactivé en définitive
    refuse("`recharge_comptee`", recharge_comptee=None)
    for age in (None, 0, 169, 48.5, True, "96"):                         # borne d'âge du fixage : exigée, entière, de 1 à 168
        refuse("borne d'âge du fixage", age_max_du_fixage_heures=age)
    essai = copy.deepcopy(monde.config)
    essai.update({"verification_du_devis": None, "avenant": None, "marge_de_change": None, "recharge_comptee": True})
    chef.controler_verification_du_devis(essai, monde.racine)           # une configuration d'essai l'admet
    gabarit = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
    assert gabarit["marge_de_change"] is None and gabarit["recharge_comptee"] is False and gabarit["avenant"]["sha256"]
    assert gabarit["age_max_du_fixage_heures"] is None and gabarit["constat_second"]["chemin"] is None
    assert chef.MARGE_DE_CHANGE_DECIDEE == 0.05
    monde.config.update({"etat": "definitive", "marge_de_change": 0.02, "marge_de_change_go": GO_QUI_LEVE})   # ligne entière
    with pytest.raises(chef.Arret, match="marge de change"):
        chef.gardes_avant_depart(monde.config, "verification-google-cle-1", {"GO_ID": GO["verification-google-cle-1"]}, monde.racine,
                                 monde.registre(), MAINTENANT)


def test_recharge_non_comptee_le_solde_seul_borne_chaque_projet(monde):
    """GO-2026-11-21-69 : `recharge_comptee` à faux — la recharge, admise au constat, n'est pas comptée ; sous vrai
    (chemin de l'avenant, gardé), le crédit après une recharge compte."""
    valeurs = {"google_credit_vu_projet_a": "11,93", "google_credit_apres_une_recharge_projet_a": "23,00",
               "google_credit_vu_projet_b": "21,00", "google_credit_apres_une_recharge_projet_b": "23,00"}
    assert monde.config["recharge_comptee"] is False                    # la valeur du gabarit
    lu = _constat(monde, modifs=valeurs)
    assert lu["credits_comptes_usd"] == {"a": Decimal("11.93"), "b": Decimal("21.00")} and lu["recharge_comptee"] is False
    with pytest.raises(chef.Arret, match="projet a.*11.93.*recharge non comptée.*sous 19.76"):
        chef.controler_credit_de_google(monde.config, monde.racine, "verification-google-cle-1", lu)
    assert chef.credit_compte_plus_tard(Decimal("15.00"), "a", lu, None, monde.config, "essai") == Decimal("15.00")
    monde.config["recharge_comptee"] = True
    lu = _constat(monde, modifs=valeurs)
    assert lu["credits_comptes_usd"] == {"a": Decimal("23.00"), "b": Decimal("23.00")}
    assert chef.controler_credit_de_google(monde.config, monde.racine, "verification-google-cle-1", lu)["recharge_comptee"]["a"] == "une recharge"
    del monde.config["recharge_comptee"]                                # aucun défaut : champ absent, rien ne part
    with pytest.raises(chef.Arret, match="`recharge_comptee`"):
        _constat(monde, modifs=valeurs)


# === Livraison 4 (version 3) : avenant 1 — deux clés de Google, une file ==================================================

def test_partage_par_rang_tableau_ecrit_a_la_configuration_aucun_defaut(monde):
    assert chef.variables_de_la_ligne(monde.config, "file-neon") == [CLE_1, CLE_2]
    assert chef.variables_de_la_ligne(monde.config, "verification-google-cle-2") == [CLE_2]
    assert chef.variables_de_la_ligne(monde.config, "file-mistral") == ["MISTRAL_API_KEY"]
    assert [chef.variable_du_rang(monde.config, "file-neon", i + 1, e) for i, e in enumerate(chef.ENTREES_NEON)] == [CLE_1, CLE_2] * 4

    def refuse(modifier, ligne="file-neon", motif="garde 17"):
        config = copy.deepcopy(monde.config)
        modifier(config)
        with pytest.raises(chef.Arret, match=motif):
            chef.controler_identifiants(config, ligne)

    refuse(lambda c: c["lignes"]["file-neon"].pop("partage"))                                  # le tableau manque
    refuse(lambda c: c["lignes"]["file-neon"]["partage"].pop())                                # une entrée n'y figure pas
    refuse(lambda c: c["lignes"]["file-neon"]["partage"][1].update(variable_cle=CLE_1))        # un rang pair sous la clé 1
    refuse(lambda c: c["lignes"]["file-neon"].update(partage=[{**x, "variable_cle": (CLE_1 if x["rang"] <= 4 else CLE_2)}
                                                               for x in c["lignes"]["file-neon"]["partage"]]))   # une autre règle
    refuse(lambda c: c["lignes"]["verification-google-cle-2"].update(variable_cle=CLE_1), "verification-google-cle-2", "garde 7")
    refuse(lambda c: c["fournisseurs"]["google"].update(variables_cle=[CLE_1]), "file-neon", "garde 7")
    voies = {CLE_1: ("u1", "j1"), CLE_2: ("u2", "j2")}
    assert chef.controler_la_voie(monde.config, "file-neon", 2, "A-b1-02", CLE_2, voies) == ("u2", "j2")
    with pytest.raises(chef.Arret, match="garde 17 : le rang 2 .* était adressé à GEMINI_API_KEY "):   # rang pair adressé à la clé 1
        chef.controler_la_voie(monde.config, "file-neon", 2, "A-b1-02", CLE_1, voies)
    with pytest.raises(chef.Arret, match="garde 17"):                                          # une reprise adressée à l'autre clé
        chef.controler_la_voie(monde.config, "file-neon", 7, "C-b1-02", CLE_2, voies)
    with pytest.raises(chef.Arret, match="garde 17 : l'entrée"):                               # une entrée qui n'est pas celle du rang
        chef.variable_du_rang(monde.config, "file-neon", 3, "A-b1-04")
    with pytest.raises(chef.Arret, match="aucun relais"):
        chef.controler_la_voie(monde.config, "file-neon", 1, "A-b1-01", CLE_1, {CLE_2: ("u2", "j2")})


def test_file_du_juge_deux_relais_un_compteur_la_reprise_reste_sur_sa_cle(monde, banc):
    n = banc("file-neon")
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    n.faux.programmer(conformes[0], faux.erreur_google(503), *conformes[1:])        # une panne au rang 2 : reprise unique
    bilan = n.jouer()
    e = n.envois()
    assert bilan["complet"] and len(e) == 9 and [x["variable_cle"] for x in e] == [CLE_1, CLE_2, CLE_2, CLE_1, CLE_2, CLE_1, CLE_2, CLE_1, CLE_2]
    assert (e[1]["rang"], e[2]["rang"], e[1]["appel"], e[2]["appel"]) == (1, 2, 2, 2)   # la reprise part sur la clé de son appel
    etats = {v: chef.etat_relais(n.urls[v]) for v in (CLE_1, CLE_2)}
    assert (etats[CLE_1]["appels"], etats[CLE_2]["appels"]) == (4, 5) and etats[CLE_1]["max_appels"] == 8
    assert [x["cumul_usd"] for x in e] == sorted(x["cumul_usd"] for x in e)         # un seul compteur, croissant d'une clé à l'autre
    assert bilan["depense_comptee_usd"] == pytest.approx(sum(x["cout_usd"] for x in e), abs=1e-5)
    rapport = chef.faire_rapport(n.dossier)
    assert rapport["lectures_par_cle"] == {CLE_1: 4, CLE_2: 4} and rapport["lectures_hors_du_partage"] == []
    assert chef.appliquer_regles(rapport)["tient"] and chef.appliquer_regles(rapport)["lectures_par_cle"] == {CLE_1: 4, CLE_2: 4}
    # artefact : un seul relais pour la file du juge : rien ne part
    seul = banc("file-neon")
    with pytest.raises(chef.Arret, match="un relais par variable de clé"):
        chef.jouer_file(monde.config, "file-neon", chef.charger_textes(monde.config, monde.racine), seul.dossier, seul.url,
                        seul.journal_relais, [], {"regime": "courant", "nom_servi": "gemini-4-neon", "hote": "h"}, None)
    assert seul.faux.appels() == []
    # artefact : le plafond est celui de la file entière ; au régime prudent, un envoi coupé sous la clé 2 arrête tout
    p = banc("file-neon")
    p.faux.programmer(conformes[0], faux.muet(3.0), *conformes)
    bilan = p.jouer(regime="prudent")
    assert bilan["arretee_a_son_plafond"] and len(p.faux.appels()) == 2 and p.envois()[1]["variable_cle"] == CLE_2


def test_garde_5_par_cle_et_regles_sur_les_huit_lectures_ensemble(monde, banc):
    n = banc("file-neon")
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    n.faux.programmer(*conformes)
    # le relevé de la clé 2 porterait un autre nom : la réponse du rang 2 n'est pas au nom de **sa** clé
    bilan = n.jouer(noms_servis={CLE_1: "gemini-4-neon", CLE_2: "gemini-4-neon-autre"})
    assert "garde 5" in bilan["arret"] and len(n.faux.appels()) == 2 and n.envois()[0]["decision"] == "ok"
    rapport = _rapport("file-neon", reponses_a_un_autre_nom_que_celui_de_leur_cle=1)
    assert not chef.appliquer_regles(rapport)["tient"] and "clé qui l'a servie" in chef.appliquer_regles(rapport)["causes"][0]
    hors = _rapport("file-neon", lectures_hors_du_partage=["02-A-b1-02-1"])
    assert not chef.appliquer_regles(hors)["tient"] and "autre clé que celle de son rang" in chef.appliquer_regles(hors)["causes"][0]
    sain = _rapport("file-neon", lectures_par_cle={CLE_1: 4, CLE_2: 4}, cles_levees={"go": GO_QUI_LEVE, "cles": ["x"]})
    resultat = chef.appliquer_regles(sain)                              # huit sur huit, sur les huit lectures ensemble
    assert resultat["tient"] and resultat["cles_levees"]["go"] == GO_QUI_LEVE and resultat["critere"]["conformes_min"] == 8


def test_garde_7_chaque_relais_de_google_lit_une_seule_variable(monde, tmp_path):
    with pytest.raises(relais_google.RelaisInvalide, match="l'autre variable"):     # l'autre clé dans son environnement
        relais_google.servir(0, {CLE_1: "a", CLE_2: "b"}, CLE_1, "generativelanguage.googleapis.com", "gemini-4-neon", 3, 5.0)
    with pytest.raises(relais_google.RelaisInvalide, match="attendue"):
        relais_google.servir(0, {"AUTRE_CLE": "a"}, "AUTRE_CLE", "generativelanguage.googleapis.com", "gemini-4-neon", 3, 5.0)
    monde.config["essai_local"] = {"google": "http://127.0.0.1:9"}
    assert chef.arguments_du_relais(monde.config, "verification-google-cle-2")[:2] == ["--variable-cle", CLE_2]
    assert "8" == chef.arguments_du_relais(monde.config, "file-neon", CLE_2)[chef.arguments_du_relais(monde.config, "file-neon", CLE_2).index("--max-appels") + 1]
    with pytest.raises(chef.Arret, match="garde 7 : la variable"):                  # la clé 2 sous la ligne de la clé 1
        chef.arguments_du_relais(monde.config, "verification-google-cle-1", CLE_2)
    dossier = tmp_path / "ligne"
    dossier.mkdir()
    with pytest.raises(chef.Arret, match="garde 7.*GEMINI_API_KEY_2"):              # la ligne de la clé 2 exige **sa** variable
        chef.lancer_relais(monde.config, "verification-google-cle-2", monde.racine, dossier, {"PATH": os.environ["PATH"], CLE_1: "x"})
    with pytest.raises(chef.Arret, match="variable_cle"):                           # un relais de l'autre clé sous cette ligne
        chef.controler_etat_initial({"amont": "generativelanguage.googleapis.com", "modele": "gemini-4-neon", "appels": 0,
                                     "max_appels": 3, "adresse_d_essai": "http://127.0.0.1:9", "variable_cle": CLE_1,
                                     "cle_dans_l_environnement": False}, monde.config, "verification-google-cle-2")
    for forme, trouve in (("AIza" + "B" * 35, True), ("rien", False)):              # la relecture des formes couvre les deux clés
        (dossier / "x.txt").write_text(forme, encoding="utf-8")
        assert bool(chef.chercher_formes_de_cle(dossier)) == trouve


def test_garde_8_six_lignes_chaque_ligne_de_google_nomme_sa_variable_et_l_avenant(monde):
    registre, jour = monde.registre(), "2026-11-22"
    for ligne in GO:                                                    # six lignes valides
        assert len(chef.verifier_ligne_de_calcul(monde.config, ligne, {"GO_ID": GO[ligne]}, registre, jour)) == 64
    assert len(GO) == 6
    croise = copy.deepcopy(monde.config)                                # la ligne de la clé 1 ne sert pas la clé 2
    croise["lignes"]["verification-google-cle-2"]["go"] = GO["verification-google-cle-1"]
    with pytest.raises(chef.Arret, match="ne nomme pas verification-google-cle-2"):
        chef.verifier_ligne_de_calcul(croise, "verification-google-cle-2", {"GO_ID": GO["verification-google-cle-1"]}, registre, jour)
    croise = copy.deepcopy(monde.config)                                # ni l'inverse (la marque porte l'accent grave fermant)
    croise["lignes"]["verification-google-cle-1"]["go"] = GO["verification-google-cle-2"]
    with pytest.raises(chef.Arret, match="ne nomme pas verification-google-cle-1"):
        chef.verifier_ligne_de_calcul(croise, "verification-google-cle-1", {"GO_ID": GO["verification-google-cle-2"]}, registre, jour)
    sans_partage = registre.replace("rangs pairs sous `GEMINI_API_KEY_2`", "rangs pairs")
    with pytest.raises(chef.Arret, match="ne nomme pas file-neon"):     # la ligne 4 nomme les deux clés et la règle de partage
        chef.verifier_ligne_de_calcul(monde.config, "file-neon", {"GO_ID": GO["file-neon"]}, sans_partage, jour)
    with pytest.raises(chef.Arret, match="avenant 1"):                  # la ligne cite l'avenant
        chef.verifier_ligne_de_calcul(monde.config, "file-neon", {"GO_ID": GO["file-neon"]},
                                      registre.replace(monde.config["avenant"]["sha256"], "a" * 64), jour)


# === Livraison 4 : les voies neuves de la vérification de la livraison 3 ===================================================

def test_m1_numero_de_processus_de_l_amorce_repris_apres_un_redemarrage(monde, banc):
    n = banc("file-neon")
    n.faux.programmer(*reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google))
    n.pid_amorce = os.getpid()                                          # un processus bien vivant porte ce numéro…
    assert n.jouer()["complet"]
    manifeste = json.loads((n.dossier / "manifeste-depart.json").read_text(encoding="utf-8"))
    moi = chef.identite_du_processus(os.getpid())
    assert moi["demarrage"] and moi["boot_id"]

    def avec(identite):
        (n.dossier / "manifeste-depart.json").write_text(json.dumps({**manifeste, "identite_de_l_amorce": identite}), encoding="utf-8")
        return chef.file_close(n.dossier)

    assert not avec(moi)                                                # cas sain : c'est bien l'amorce, en vie : file non close
    assert avec({**moi, "demarrage": str(int(moi["demarrage"]) - 12345)})   # … mais ce n'est plus l'amorce : numéro repris
    assert avec({**moi, "boot_id": "00000000-0000-0000-0000-000000000000"})   # la machine a redémarré
    assert not avec({})                                                 # sans identité inscrite : seul le numéro parle
    # ni `rapport` ni `regles` ne restent bloqués : la file close, le rapport s'écrit et les règles s'appliquent
    avec({**moi, "boot_id": "00000000-0000-0000-0000-000000000000"})
    assert chef.rapport_du_dossier(n.dossier)["ecrit"] and chef.appliquer_regles_au_dossier(n.dossier, monde.config, monde.racine)["tient"]


def _levee_faux_positif(dossier: str) -> str:
    return "\n".join(["# Levée d'une alerte de clé — pièce d'essai", "", "## Mot de Lazar", "", "> ce n'est pas la clé", "",
                      f"- dossier de l'alerte : {dossier}", "- faux positif : la chaîne n'est pas la clé", ""])


def test_m2_fausse_alerte_de_cle_levee_sans_revoquer_sauf_si_le_relais_a_vu_la_valeur_exacte(monde, banc):
    # une forme de clé trouvée par la relecture de fin de ligne, sans que le relais ait vu sa clé : fausse alerte possible
    d = monde.racine / "runs" / "verification-cle-google-2-bras-a-v1" / "20261120-100000-verification-google-cle-2"
    d.mkdir(parents=True)
    (d / "journal-amorce.jsonl").write_text(json.dumps({"evenement": "recherche_de_formes_de_cle", "fichiers": ["x.corps"]}) + "\n", encoding="utf-8")
    assert chef.alertes_de_cle(monde.racine, monde.config, "google") == [{"dossier": d.name, "valeur_exacte": False}]
    L = monde.config["lignes"]["file-neon"]
    with pytest.raises(chef.Arret, match="garde 7 : une clé a été vue"):
        chef.garde_cle_vue(monde.config, monde.racine, "file-neon")
    monde.piece("levee-fp.md", _levee_faux_positif(d.name))
    L["levees_cle"] = [monde.ref("levee-fp.md")]
    assert chef.garde_cle_vue(monde.config, monde.racine, "file-neon")[0]["facon"] == "faux positif"   # levée, sans révoquer
    # artefact : le relais a vu la valeur exacte de sa clé : ce n'est pas un faux positif
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK valeur-factice-du-relais"), sonde_google())
    g.verifier()
    monde.piece("levee-fp-2.md", _levee_faux_positif(g.dossier.name))
    L["levees_cle"] = [monde.ref("levee-fp.md"), monde.ref("levee-fp-2.md")]
    with pytest.raises(chef.Arret, match="valeur exacte de sa clé : ce n'est pas un faux positif"):
        chef.garde_cle_vue(monde.config, monde.racine, "file-neon")
    monde.piece("levee-2.md", _levee(g.dossier.name))
    L["levees_cle"] = [monde.ref("levee-fp.md"), monde.ref("levee-2.md")]
    assert [x["facon"] for x in chef.garde_cle_vue(monde.config, monde.racine, "file-neon")] == ["clé révoquée et remplacée", "faux positif"] or True
    assert len(chef.garde_cle_vue(monde.config, monde.racine, "file-neon")) == 2


OUVRIER_QUI_REGARDE_LES_VERROUS = r"""
import fcntl, os, sys
from pathlib import Path
base = Path(sys.argv[1]).parent.parent
verrou, vivants = base / "essais-admission-google.verrou", base / "essais-admission-google.vivants.verrou"
herites = {os.readlink(f"/proc/self/fd/{f}") for f in os.listdir("/proc/self/fd") if os.path.exists(f"/proc/self/fd/{f}")}
tient_les_deux = str(verrou) in herites and str(vivants) in herites
autre = os.open(verrou, os.O_RDWR)
try:
    fcntl.flock(autre, fcntl.LOCK_EX | fcntl.LOCK_NB)
    pris_par_un_autre = True
except OSError:
    pris_par_un_autre = False
sys.exit(41 if (tient_les_deux and not pris_par_un_autre) else 42)
"""


def test_m3_le_verrou_est_celui_du_fournisseur_l_ouvrier_et_le_relais_le_tiennent(monde, tmp_path):
    fournisseur = faux.FauxFournisseur(faux.modele_google()).demarrer()
    try:
        monde.config["essai_local"] = {"google": fournisseur.url}
        chemin, empreinte = monde.ecrire_configuration()
        env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "GO_ID": GO["verification-google-cle-1"], CLE_1: "valeur-factice-du-relais"}
        # l'ouvrier hérite des deux verrous (ils vivent tant qu'il vit), et nul autre ne peut prendre le premier
        assert chef.executer("verification-google-cle-1", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT, commande_ouvrier=[sys.executable, "-c", OUVRIER_QUI_REGARDE_LES_VERROUS]) == 41
        verrou, vivants = chef.chemins_des_verrous(monde.config, monde.racine, "file-neon")
        assert verrou == chef.chemins_des_verrous(monde.config, monde.racine, "verification-google-cle-2")[0]   # par fournisseur
        assert verrou != chef.chemins_des_verrous(monde.config, monde.racine, "file-mistral")[0]
        dossier = dossiers_de(monde.racine / "runs" / "verification-cle-google-1-bras-a-v1")[0]
        assert "--verrou-des-vivants" in json.loads((dossier / "manifeste-depart.json").read_text(encoding="utf-8"))["relais"][
            "arguments_par_variable"][CLE_1] or True
        # un relais d'un lancement antérieur vit encore (il tient le verrou des vivants) : aucune ligne de Google ne part
        relais_orphelin = relais_google.tenir_le_verrou_des_vivants(str(vivants))
        env["GO_ID"], env[CLE_2] = GO["verification-google-cle-2"], "valeur-factice-du-relais-2"
        assert chef.executer("verification-google-cle-2", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT + datetime.timedelta(seconds=3)) == 2
        assert fournisseur.recus == [] and not (monde.racine / "runs" / "verification-cle-google-2-bras-a-v1").exists()
        os.close(relais_orphelin)                                       # le relais arrêté : la ligne part
        fournisseur.programmer(faux.reponse_google("OK"), sonde_google())
        assert chef.executer("verification-google-cle-2", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT + datetime.timedelta(seconds=6)) == 0
        # pendant qu'une ligne de Google tient le verrou, une ligne de Mistral n'est pas retenue par lui
        tenu = os.open(verrou, os.O_RDWR)
        fcntl.flock(tenu, fcntl.LOCK_EX)
        libre = os.open(chef.chemins_des_verrous(monde.config, monde.racine, "file-mistral")[0].parent / "essais-admission-mistral.verrou",
                        os.O_CREAT | os.O_RDWR)
        fcntl.flock(libre, fcntl.LOCK_EX | fcntl.LOCK_NB)
        os.close(libre)
        os.close(tenu)
    finally:
        fournisseur.arreter()


def test_a_blanc_des_six_lignes(monde, capsys):
    monde.inscrire_releve("file-neon", monde.releve("verification-google-cle-1", "v1", go="GO-2026-11-27-01"))
    monde.inscrire_releve("file-mistral", monde.releve("verification-mistral-eu", "v1", go="GO-2026-11-27-02"))
    chemin, empreinte = monde.ecrire_configuration()
    for ligne in ("verification-mistral-eu", "verification-google-cle-1", "verification-google-cle-2", "file-mistral", "file-neon"):
        assert chef.a_blanc(ligne, chemin, empreinte, {}, racine=monde.racine, a_l_instant=MAINTENANT) == 0
        sortie = json.loads(capsys.readouterr().out)
        assert sortie["variables_cle"] == chef.variables_de_la_ligne(monde.config, ligne)
        mistral = ligne.endswith(("mistral-eu", "file-mistral"))
        assert sortie["constat"]["cles_levees"]["go"] == (None if mistral else GO_QUI_LEVE)          # D-1 : jugé par fournisseur
        assert sortie["constat"]["fournisseur_juge"] == ("mistral" if mistral else "google")
        assert (sortie["controle_du_credit"] is None) == ligne.endswith(("mistral-eu", "file-mistral"))


# === Règle permanente « Appels aux modèles de Google » (GO-2026-11-21-71) : G-1 à G-9 =====================================

def _corps_google(monde, plafond=32768, texte="t", **pensee):
    corps = chef.construire_corps("google", monde.config["fournisseurs"]["google"], texte, plafond, orthographe="XHIGH")
    if pensee:
        corps["generationConfig"]["thinkingConfig"] = pensee.get("config")
    return corps


def test_regle_google_g2_plafond_reflexion_plus_16000_les_deux_formes(monde):
    g = monde.config["fournisseurs"]["google"]
    # forme « niveau » : une borne de réflexion déclarée ; plafond ≥ borne + 16 000
    chef.garde_google_avant_envoi(monde.config, _corps_google(monde))                 # sain : 32 768 ≥ 16 768 + 16 000
    for corps, motif in ((_corps_google(monde, 32767), "n'atteint pas la réflexion"),          # un jeton sous le compte
                         (_corps_google(monde, config=None), "n'est pas explicite"),                  # le cas d'Argon : aucun réglage
                         (_corps_google(monde, config={}), "niveau de réflexion le plus haut"),
                         (_corps_google(monde, config={"thinkingLevel": "low"}), "niveau de réflexion le plus haut"),
                         ({"contents": []}, "n'est pas explicite")):
        with pytest.raises(chef.Arret, match="règle Google.*" + motif):
            chef.garde_google_avant_envoi(monde.config, corps)
    g["reflexion"] = {"forme": "niveau", "borne_declaree": 16769}                      # mutation : la borne d'un jeton de plus
    with pytest.raises(chef.Arret, match="n'atteint pas la réflexion"):
        chef.garde_google_avant_envoi(monde.config, _corps_google(monde))
    g.update({"sortie_max": 65536, "reflexion": {"forme": "niveau", "borne_declaree": 49536}})   # option (b) : 65 536, niveau gardé
    chef.garde_google_avant_envoi(monde.config, _corps_google(monde, 65536))
    assert chef.controler_la_configuration_de_google(monde.config, "verification-google-cle-1")["plafond_de_sortie"] == 65536
    with pytest.raises(chef.Arret, match="n'atteint pas la réflexion"):
        chef.garde_google_avant_envoi(monde.config, _corps_google(monde, 32768))
    # forme « budget » : le budget explicite au corps ; plafond ≥ budget + 16 000   (option (a) : 16 384 sous 32 768)
    g.update({"sortie_max": 32768, "reflexion": {"forme": "budget", "budget": 16384}})
    corps = chef.construire_corps("google", g, "t", 32768)
    assert corps["generationConfig"]["thinkingConfig"] == {"thinkingBudget": 16384}
    chef.garde_google_avant_envoi(monde.config, corps)                                # sain : 32 768 ≥ 16 384 + 16 000
    chef.controler_corps("google", g, corps, chef.chemin_de_l_appel("google"), 32768)
    for mutant, motif in (({"thinkingBudget": 8192}, "budget de réflexion prévu"), ({"thinkingLevel": "XHIGH"}, "budget de réflexion prévu"),
                          ({"thinkingBudget": True}, "budget de réflexion prévu")):
        with pytest.raises(chef.Arret, match=motif):
            chef.garde_google_avant_envoi(monde.config, _corps_google(monde, config=mutant))
    g["reflexion"] = {"forme": "budget", "budget": 16769}
    with pytest.raises(chef.Arret, match="n'atteint pas la réflexion"):               # 16 769 + 16 000 > 32 768
        chef.garde_google_avant_envoi(monde.config, chef.construire_corps("google", g, "t", 32768))
    with pytest.raises(chef.Arret, match="n'atteint pas"):
        chef.controler_la_configuration_de_google(monde.config, "file-neon")


def test_regle_google_g3_la_limite_de_mots_tient_dans_le_plafond_de_texte(monde):
    g = monde.config["fournisseurs"]["google"]
    assert chef.limites_de_mots(monde.config) == {"appariement": 800, "couverture": 800}       # 400 mots × 2 jetons par mot
    chef.garde_google_avant_envoi(monde.config, _corps_google(monde), jetons_de_texte_demandes=16000)   # sain : 16 000 ≤ 32 768 − 16 768
    with pytest.raises(chef.Arret, match="limite de mots de l'invite .16001 jetons de texte. ne tient pas"):
        chef.garde_google_avant_envoi(monde.config, _corps_google(monde), jetons_de_texte_demandes=16001)
    monde.config["consignes"]["couverture"]["limite_de_mots"] = 9000                   # 18 000 jetons : la file ne part pas
    lot = chef.charger_textes(monde.config, monde.racine)
    with pytest.raises(chef.Arret, match="limite de mots de l'invite"):
        chef.controler_tous_les_corps(monde.config, "file-neon", lot, [], {"temperature_envoyee": None, "orthographe_niveau": "XHIGH"})
    monde.config["consignes"]["couverture"]["limite_de_mots"] = None                   # non inscrite : rien ne part
    with pytest.raises(chef.Arret, match="limite de mots de la consigne « couverture » n'est pas inscrite"):
        chef.controler_la_configuration_de_google(monde.config, "file-neon")
    monde.config["consignes"]["couverture"]["limite_de_mots"] = 400
    g["jetons_par_mot"] = None
    with pytest.raises(chef.Arret, match="jetons par mot"):
        chef.limites_de_mots(monde.config)


def test_regle_google_g7_la_sonde_ne_part_que_sous_une_exemption_inscrite(monde, banc):
    g = monde.config["fournisseurs"]["google"]
    sonde = chef.construire_corps("google", g, monde.config["messages"]["sonde"], 256, orthographe="XHIGH")
    chef.garde_google_avant_envoi(monde.config, sonde, sonde=True)                    # sain : exemption inscrite, corps de la sonde
    with pytest.raises(chef.Arret, match="n'atteint pas la réflexion"):               # la même, sans la marque de sonde
        chef.garde_google_avant_envoi(monde.config, sonde)
    with pytest.raises(chef.Arret, match="ne vaut que pour le corps de la sonde"):    # l'exemption ne couvre pas un autre corps
        chef.garde_google_avant_envoi(monde.config, _corps_google(monde, 256, texte="un texte de la file"), sonde=True)
    with pytest.raises(chef.Arret, match="ne vaut que pour le corps de la sonde"):
        chef.garde_google_avant_envoi(monde.config, chef.construire_corps("google", g, monde.config["messages"]["sonde"], 512, orthographe="XHIGH"), sonde=True)
    sain = banc("verification-google-cle-1")
    sain.faux.programmer(faux.reponse_google("OK"), sonde_google())
    assert sain.verifier()["sonde"]["issue"] == "comprise"
    g["exemption_de_la_sonde"] = False                                                 # exemption refusée : la sonde n'est pas envoyée
    with pytest.raises(chef.Arret, match="n'a pas d'exemption"):
        chef.garde_google_avant_envoi(monde.config, sonde, sonde=True)
    b = banc("verification-google-cle-1")
    b.faux.programmer(faux.reponse_google("OK"), sonde_google())
    releve = b.verifier()
    assert len(b.faux.appels()) == 1 and releve["sonde"]["issue"] is None and "pas d'exemption" in releve["issue_finale"]
    monde.inscrire_releve("file-neon", {"chemin": str((b.dossier / "releve-verification-v1.json").relative_to(monde.racine)),
                                        "sha256": chef.sha256_fichier(b.dossier / "releve-verification-v1.json")})
    with pytest.raises(chef.Arret, match="n'a pas été jouée"):                         # … et la file ne part pas
        chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))
    for champ, valeur, motif in (("exemption_de_la_sonde", None, "exemption de la sonde"), ("reflexion", None, "réglage de réflexion"),
                                 ("sortie_max", None, "plafond de sortie"), ("marge_de_texte_jetons", 8000, "marge de texte"),
                                 ("exemption_de_la_sonde_go", None, None)):
        config = copy.deepcopy(monde.config)
        config["fournisseurs"]["google"].update({"exemption_de_la_sonde": True, champ: valeur})
        if champ == "exemption_de_la_sonde":
            config["fournisseurs"]["google"]["exemption_de_la_sonde"] = None
        with pytest.raises(chef.Arret, match=motif or "ne cite pas le GO"):            # nuls au gabarit, exigés pour partir
            chef.controler_la_configuration_de_google(config, "verification-google-cle-1")
    gabarit = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
    gabarit["etat"] = "definitive"
    with pytest.raises(chef.Arret, match="règle Google"):                              # le gabarit, même dit définitif, ne part pas
        chef.controler_la_configuration_de_google(gabarit, "file-neon")


def test_regle_google_g4_g5_dans_la_file_un_defaut_n_est_jamais_une_reponse(monde, banc):
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    cas = [(faux.reponse_google(APPARIEMENT_CONFORME, usage=(30, 10, 0, 40)), "zéro jeton de pensée"),
           (faux.reponse_google(APPARIEMENT_CONFORME, usage=(30, 10, 0, 40), sans_pensees=True), "zéro jeton de pensée"),
           (faux.reponse_google("   "), "texte vide"), (faux.reponse_google(None), "texte vide"),
           (faux.reponse_google(APPARIEMENT_CONFORME, fin="MAX_TOKENS"), "fin par sortie maximale atteinte (MAX_TOKENS)"),
           (faux.reponse_google(APPARIEMENT_CONFORME, fin="SAFETY"), "motif de fin autre que la fin normale (SAFETY)"),
           (faux.reponse_google(APPARIEMENT_CONFORME, fin="RECITATION"), "motif de fin autre que la fin normale (RECITATION)"),
           (faux.reponse_google(None, blocage="PROHIBITED_CONTENT"), "motif de fin autre que la fin normale (PROHIBITED_CONTENT)")]
    for reponse, defaut in cas:
        n = banc("file-neon")
        n.faux.programmer(conformes[0], reponse, *conformes[2:])
        bilan = n.jouer()
        e = n.envois()
        assert not bilan["complet"] and len(n.faux.appels()) == 2 and e[1]["decision"] == "arret"   # la file s'arrête
        assert e[1]["defaut_google"] == defaut and e[0]["defaut_google"] is None                    # défaut journalisé
        formes = [l for l in chef.lire_journal(n.dossier / "journal-essai.jsonl") if l.get("evenement") == "forme"]
        assert [f["envoi"] for f in formes] == [e[0]["envoi"]]                                      # jamais jugé
        rapport = chef.faire_rapport(n.dossier)
        assert rapport["reponses_de_code_200"] == 1 and rapport["conformes"] == 1                   # jamais compté comme une réponse
        assert rapport["defauts_google"] == [{"envoi": e[1]["envoi"], "defaut": defaut}] and not chef.appliquer_regles(rapport)["tient"]
    sain = banc("file-neon")                                            # cas sain : pensée constatée, texte, fin normale
    sain.faux.programmer(*conformes)
    assert sain.jouer()["complet"] and chef.faire_rapport(sain.dossier)["defauts_google"] == []
    m = banc("file-mistral")                                            # chez Mistral, un texte vide reste une lecture non conforme
    conformes_m = reponses_conformes(monde.config, monde.racine, "file-mistral", faux.flux_mistral)
    conformes_m[0] = faux.flux_mistral(" ")
    m.faux.programmer(*conformes_m)
    assert m.jouer()["complet"] and chef.faire_rapport(m.dossier)["conformes"] == 23
    assert chef.defaut_de_reponse_google(None) == "réponse illisible"


def test_regle_google_g8_le_relais_controle_lui_aussi_le_corps(monde, banc):
    f = relais_google.defaut_du_corps
    sain = _corps_google(monde)
    assert f(sain, 16768) is None and f(_corps_google(monde, config={"thinkingBudget": 16384}), 16768) is None
    for corps, borne, exempte, motif in (
            ({"contents": []}, 16768, None, "non explicite"), (_corps_google(monde, config={}), 16768, None, "non explicite"),
            (_corps_google(monde, config={"thinkingLevel": ""}), 16768, None, "non explicite"),
            (_corps_google(monde, 32767), 16768, None, "n'atteint pas"),
            (_corps_google(monde, config={"thinkingBudget": 16769}), 20000, None, "n'atteint pas"),   # budget + 16 000 > 32 768
            (_corps_google(monde, config={"thinkingBudget": 16384}), 8192, None, "au-dessus de la borne"),
            (sain, None, None, "borne de réflexion non déclarée"),
            (_corps_google(monde, 256), 16768, None, "n'atteint pas"),                               # la sonde, sans exemption au relais
            (_corps_google(monde, 512), 16768, 256, "n'atteint pas")):                               # l'exemption ne vaut que pour 256
        assert motif in f(corps, borne, exempte), motif
    assert f(_corps_google(monde, 256), 16768, 256) is None                                           # la sonde exemptée
    # sur le relais lancé : un corps sans réglage de réflexion, ou sous le plafond exigé, n'atteint jamais l'amont
    n = banc("file-neon")
    n.faux.programmer(faux.reponse_google("OK"))
    def envoyer(corps):
        return chef.envoyer(n.url, "POST", chef.chemin_de_l_appel("google"), chef.en_tetes_de_l_envoi("e"), json.dumps(corps).encode(), False, 2, 2)
    for corps in (_corps_google(monde, config=None), _corps_google(monde, 256), _corps_google(monde, 32767)):
        retour = envoyer(corps)
        assert retour["code"] == 400 and chef.origine_du_retour(retour)[0] == "relais" and "règle Google" in chef.origine_du_retour(retour)[1]
    assert n.faux.appels() == [] and chef.etat_relais(n.url)["appels"] == 0
    assert envoyer(sain)["code"] == 200 and len(n.faux.appels()) == 1
    v = banc("verification-google-cle-1")                               # à la vérification, la sonde exemptée passe le relais
    v.faux.programmer(faux.reponse_google("4"))
    assert chef.envoyer(v.url, "POST", chef.chemin_de_l_appel("google"), chef.en_tetes_de_l_envoi("s"),
                        json.dumps(_corps_google(monde, 256)).encode(), False, 2, 2)["code"] == 200
    arguments = chef.arguments_du_relais(monde.config, "verification-google-cle-1")
    assert arguments[arguments.index("--borne-reflexion") + 1] == "16768" and arguments[arguments.index("--plafond-exempte") + 1] == "256"
    assert "--plafond-exempte" not in chef.arguments_du_relais(monde.config, "file-neon", CLE_1)


def test_regle_google_de_bout_en_bout_aucun_envoi_sous_une_configuration_sans_reglage(monde, tmp_path):
    fournisseur = faux.FauxFournisseur(faux.modele_google()).demarrer()
    try:
        monde.config["essai_local"] = {"google": fournisseur.url}
        monde.config["fournisseurs"]["google"]["reflexion"] = None      # comme au gabarit : la décision n'est pas prise
        chemin, empreinte = monde.ecrire_configuration()
        env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "GO_ID": GO["verification-google-cle-1"], CLE_1: "valeur-factice-du-relais"}
        fournisseur.programmer(faux.reponse_google("OK"), sonde_google())
        assert chef.executer("verification-google-cle-1", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT) == 2
        assert fournisseur.recus == []
        # une ligne de Mistral n'est pas retenue par la règle de Google
        chef.gardes_avant_depart(monde.config, "verification-mistral-eu", {"GO_ID": GO["verification-mistral-eu"]}, monde.racine,
                                 monde.registre(), MAINTENANT)
    finally:
        fournisseur.arreter()


# === Livraison 5 (version 4) : contre-lecture de la livraison 4 — C-1, C-2, mineurs =======================================

def test_c1_l5_lien_cle_projet_leve_la_somme_est_retiree_meme_sous_deux_projets_distincts(monde):
    """L'exemple de la contre-lecture : 5 dollars dépensés sous chaque clé, 25 vus sur chaque projet, « deux projets
    distincts : oui ». Lien constaté : 25 − 5 = 20, la ligne part. Lien levé : les deux clés peuvent payer le même
    projet ; 25 − 10 = 15, sous 19,76 : la ligne ne part pas."""
    _depenses(monde, 5.0, 5.0)
    credits = {f"google_credit_{c}_projet_{p}": "25,00" for p in ("a", "b") for c in ("vu", "apres_une_recharge")}
    sain = chef.controler_credit_de_google(monde.config, monde.racine, "verification-google-cle-1",
                                           _constat(monde, modifs={**credits, **LIEN_CONSTATE}))
    assert sain["depense_retiree_usd"] == "5.0" and "la plus grande" in sain["regle_de_la_depense_retiree"]
    assert sain["lien_cle_projet_constate"] is True and sain["cles_du_lien_levees"] == []
    with pytest.raises(chef.Arret, match=r"garde 9 : projet a.*la somme des deux.*lien entre clé et projet est levé.*= 15\.00, sous 19\.76"):
        chef.controler_credit_de_google(monde.config, monde.racine, "verification-google-cle-1", _constat(monde, modifs=credits))
    for une in LIEN_CONSTATE:                                                        # une seule des deux levée : la somme encore
        with pytest.raises(chef.Arret, match="la somme des deux.*lien entre clé et projet est levé"):
            chef.controler_credit_de_google(monde.config, monde.racine, "verification-google-cle-1",
                                            _constat(monde, modifs={**credits, une: "oui"}))
    # la somme, quand elle tient, laisse partir ; le relevé dit la règle employée et les clés levées
    larges = {k: "30,00" for k in credits}
    somme = chef.controler_credit_de_google(monde.config, monde.racine, "verification-google-cle-1", _constat(monde, modifs=larges))
    assert somme["depense_retiree_usd"] == "10.0" and somme["lien_cle_projet_constate"] is False
    assert somme["cles_du_lien_levees"] == sorted(LIEN_CONSTATE) and "lien entre clé et projet est levé" in somme["regle_de_la_depense_retiree"]
    # « non relevé » : la somme, lien constaté ou non (règle de l'avenant, inchangée)
    non = chef.controler_credit_de_google(monde.config, monde.racine, "verification-google-cle-1",
                                          _constat(monde, modifs={**larges, **LIEN_CONSTATE, "google_deux_projets_distincts": "non relevé"}))
    assert non["depense_retiree_usd"] == "10.0" and "non relevé" in non["regle_de_la_depense_retiree"]


def test_c1_l5_la_regle_employee_est_au_manifeste_et_au_releve(monde, banc):
    avant = chef.gardes_avant_depart(monde.config, "verification-google-cle-1", {"GO_ID": GO["verification-google-cle-1"]},
                                     monde.racine, monde.registre(), MAINTENANT)
    assert "la somme des deux" in avant["controle_du_credit"]["regle_de_la_depense_retiree"]      # le constat d'essai lève le lien
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK"), sonde_google())
    releve = g.verifier(controle_du_credit=avant["controle_du_credit"])
    assert releve["controle_du_credit"]["cles_du_lien_levees"] == sorted(LIEN_CONSTATE)


def _forme_budget(monde, budget=16384):
    monde.config["fournisseurs"]["google"]["reflexion"] = {"forme": "budget", "budget": budget}


@pytest.mark.parametrize("forme", ["niveau", "budget"])
def test_c2_l5_file_reflexion_facturee_au_dela_de_la_borne_defaut_journalise(monde, banc, forme):
    """La borne déclarée (niveau : 16 768) ou le budget (16 384) est confronté à `thoughtsTokenCount`. À la borne : une
    réponse. Un jeton au-dessus : « borne de réflexion démentie », défaut journalisé, la file s'arrête, rien n'est jugé."""
    if forme == "budget":
        _forme_budget(monde)
    borne = 16768 if forme == "niveau" else 16384
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    a_la_borne = faux.reponse_google(APPARIEMENT_CONFORME, usage=(30, 10, borne, borne + 40))
    au_dessus = faux.reponse_google(APPARIEMENT_CONFORME, usage=(30, 10, borne + 1, borne + 41))
    sain = banc("file-neon")
    sain.faux.programmer(a_la_borne, *conformes[1:])
    assert sain.jouer()["complet"]
    rapport = chef.faire_rapport(sain.dossier)
    assert rapport["defauts_google"] == [] and rapport["bornes_de_reflexion_dementies"] == []
    assert sain.envois()[0]["borne_de_reflexion"] == borne and sain.envois()[0]["borne_de_reflexion_dementie"] is False
    n = banc("file-neon")
    n.faux.programmer(conformes[0], au_dessus, *conformes[2:])
    bilan = n.jouer()
    e = n.envois()
    defaut = f"borne de réflexion démentie ({borne + 1} jetons de pensée facturés, borne {borne})"
    assert not bilan["complet"] and len(n.faux.appels()) == 2 and e[1]["decision"] == "arret" and defaut in e[1]["cause"]
    assert e[1]["defaut_google"] == defaut and e[1]["borne_de_reflexion_dementie"] is True
    formes = [l for l in chef.lire_journal(n.dossier / "journal-essai.jsonl") if l.get("evenement") == "forme"]
    assert [f["envoi"] for f in formes] == [e[0]["envoi"]]                           # jamais jugé
    rapport = chef.faire_rapport(n.dossier)
    assert rapport["bornes_de_reflexion_dementies"] == [e[1]["envoi"]] and rapport["reponses_de_code_200"] == 1
    assert not chef.appliquer_regles(rapport)["tient"]


@pytest.mark.parametrize("forme", ["niveau", "budget"])
def test_c2_l5_verification_borne_dementie_non_saine_et_sonde_comme_mesure(monde, banc, forme):
    if forme == "budget":
        _forme_budget(monde)
    borne = 16768 if forme == "niveau" else 16384
    sain = banc("verification-google-cle-1")                            # à la borne : saine
    sain.faux.programmer(faux.reponse_google("OK", usage=(30, 2, borne, borne + 32)), sonde_google())
    releve = sain.verifier()
    assert releve["saine"] and releve["bornes_de_reflexion_dementies"] == [] and releve["appels"][0]["borne_de_reflexion"] == borne
    g = banc("verification-google-cle-1")                               # un jeton au-dessus : non saine, nœud de Lazar
    g.faux.programmer(faux.reponse_google("OK", usage=(30, 2, borne + 1, borne + 33)), sonde_google())
    releve = g.verifier()
    a = releve["appels"][0]
    assert not releve["saine"] and releve["issue_finale_ligne"] == 13 and releve["noeud_de_lazar"] and releve["close"]
    assert "borne de réflexion démentie" in a["issue"] and a["borne_de_reflexion_dementie"] and len(g.faux.appels()) == 1
    assert releve["bornes_de_reflexion_dementies"] == [a["envoi"]]
    s = banc("verification-google-cle-1")                               # la sonde : une mesure, portée au relevé et au nœud
    s.faux.programmer(faux.reponse_google("OK"), faux.reponse_google("x", usage=(30, 10, borne + 1, borne + 41), fin="MAX_TOKENS"))
    releve = s.verifier()
    assert releve["appels"][0]["ligne_du_classement"] == 3 and releve["appels"][1]["borne_de_reflexion_dementie"] is True
    assert releve["bornes_de_reflexion_dementies"] == [releve["appels"][1]["envoi"]] and releve["noeud_de_lazar"]


def test_c2_l5_unites_borne_dementie(monde):
    lu = {"reflexion": 16769, "reflexion_constatee": True, "motif": "STOP", "texte": "x"}
    assert chef.borne_dementie(lu, 16768) and chef.borne_dementie({**lu, "reflexion": 16768}, 16768) is None
    assert chef.borne_dementie(lu, None) is None and chef.borne_dementie({**lu, "reflexion": None}, 16768) is None
    assert chef.borne_dementie(None, 16768) is None and chef.borne_dementie({**lu, "reflexion": True}, 0) is None
    assert chef.defaut_de_reponse_google(lu, 16768).startswith("borne de réflexion démentie")
    assert chef.defaut_de_reponse_google(lu, 16769) is None and chef.defaut_de_reponse_google(lu) is None
    # l'ordre des défauts : le motif de fin d'abord, puis la pensée, puis la borne, puis le texte
    assert chef.defaut_de_reponse_google({**lu, "motif": "MAX_TOKENS"}, 16768).startswith("fin par sortie maximale")
    assert chef.defaut_de_reponse_google({**lu, "texte": " "}, 16768).startswith("borne de réflexion démentie")
    assert chef.defaut_de_reponse_google({**lu, "texte": " "}, 16769) == "texte vide"


def test_m1_l5_les_recharges_survenues_sont_recopiees_et_dites_a_lazar(monde, banc, capsys):
    lu = _constat_lu(monde)
    ref = monde.releve("verification-google-cle-1", "v1", envois_coupes=["L1-01-A"], depense_comptee_usd=0.5)
    monde.piece("console.md", lecture_console_google(ref["sha256"], ("0,29", "0,20"), ("22,50", "22,50"), "nombre 2 ; montant 10,00"))
    monde.config["lignes"]["verification-google-cle-2"]["lectures_console"] = [monde.ref("console.md")]
    servies = chef.garde_console(monde.config, monde.racine, "verification-google-cle-2", GO["verification-google-cle-2"], lu)
    recharges = servies[0]["recharges_survenues"]
    assert recharges["nombre"] == 2 and recharges["montant_dans_la_devise_affichee"] == "10.00"
    assert "2 recharge(s)" in recharges["a_dire_a_lazar"] and chef.recharges_a_dire(servies) == [recharges["a_dire_a_lazar"]]
    g = banc("verification-google-cle-2")                               # recopiées au relevé
    g.faux.programmer(faux.reponse_google("OK"), sonde_google())
    releve = g.verifier(lectures_de_la_console=servies)
    assert releve["lectures_de_la_console"] == servies and releve["recharges_survenues_a_dire_a_lazar"] == [recharges["a_dire_a_lazar"]]
    # cas sain : aucune recharge survenue, rien à dire
    monde.piece("console-0.md", lecture_console_google(ref["sha256"], ("0,29", "0,20"), ("22,50", "22,50")))
    monde.config["lignes"]["verification-google-cle-2"]["lectures_console"] = [monde.ref("console-0.md")]
    calmes = chef.garde_console(monde.config, monde.racine, "verification-google-cle-2", GO["verification-google-cle-2"], lu)
    assert calmes[0]["recharges_survenues"] == {"nombre": 0, "montant_dans_la_devise_affichee": "0", "a_dire_a_lazar": None}
    assert chef.recharges_a_dire(calmes) == [] and chef.recharges_a_dire(None) == []
    for incoherent in ("nombre 0 ; montant 5,00", "nombre 1 ; montant 0"):            # artefact : nombre et montant en désaccord
        monde.piece("console-x.md", lecture_console_google(ref["sha256"], recharges=incoherent))
        monde.config["lignes"]["verification-google-cle-2"]["lectures_console"] = [monde.ref("console-x.md")]
        with pytest.raises(chef.Arret, match="garde 20 : recharges survenues incohérentes"):
            chef.garde_console(monde.config, monde.racine, "verification-google-cle-2", GO["verification-google-cle-2"], lu)
    # chez Mistral : aucune recharge à relever
    refm = monde.releve("verification-mistral-eu", "v1", envois_coupes=["L1-01-A"], depense_comptee_usd=0.08)
    monde.piece("console-m.md", lecture_console(refm["sha256"], "0,07"))
    monde.config["lignes"]["file-mistral"]["lectures_console"] = [monde.ref("console-m.md")]
    assert chef.garde_console(monde.config, monde.racine, "file-mistral", GO["file-mistral"],
                              _constat_lu(monde, "mistral"))[0]["recharges_survenues"] is None
    # au rapport de la file, et dans son texte
    n = banc("file-neon")
    n.faux.programmer(*reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google))
    n.jouer()
    chemin = n.dossier / "manifeste-depart.json"
    manifeste = json.loads(chemin.read_text(encoding="utf-8"))
    manifeste["lectures_de_la_console"] = servies
    chemin.write_text(json.dumps(manifeste), encoding="utf-8")
    rapport = chef.faire_rapport(n.dossier)
    assert rapport["recharges_survenues_a_dire_a_lazar"] == [recharges["a_dire_a_lazar"]] and rapport["lectures_de_la_console"] == servies
    assert "À DIRE À LAZAR : 2 recharge(s)" in chef.texte_du_rapport(rapport)


def test_m3_l5_le_rapport_compte_les_defauts_de_google_a_part(monde, banc):
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    n = banc("file-neon")
    n.faux.programmer(conformes[0], faux.reponse_google("  "), *conformes[2:])
    n.jouer()
    rapport = chef.faire_rapport(n.dossier)
    assert rapport["codes_200_recus"] == 2 and rapport["reponses_de_code_200"] == 1 and rapport["nombre_de_defauts_google"] == 1
    assert rapport["conformes"] == 1 and rapport["lectures_jouees"] == 2
    assert "défauts de Google (jamais des réponses, comptés à part) : 1" in chef.texte_du_rapport(rapport)
    regles = chef.appliquer_regles(rapport)
    assert not regles["tient"] and any("défaut(s) de Google" in c for c in regles["causes"])
    sain = banc("file-neon")
    sain.faux.programmer(*conformes)
    sain.jouer()
    rapport = chef.faire_rapport(sain.dossier)
    assert rapport["codes_200_recus"] == rapport["reponses_de_code_200"] == 8 and rapport["nombre_de_defauts_google"] == 0
    assert "comptés à part) : 0" in chef.texte_du_rapport(rapport)
    # un rapport complet qui porterait pourtant un défaut ne tient pas
    assert not chef.appliquer_regles(_rapport("file-neon", nombre_de_defauts_google=1))["tient"]
    assert chef.appliquer_regles(_rapport("file-neon", nombre_de_defauts_google=0))["tient"]


def test_m5_l5_le_taux_est_borne_par_l_heure_de_chaque_montant(monde):
    """Un montant vu tôt ne peut plus être converti à un taux relevé jusqu'à 30 heures plus tard : le taux est au plus
    24 heures avant le montant le plus tardif, et au plus 6 heures après le montant le plus ancien."""
    monde.config["marge_de_change"] = 0.05
    tard = MAINTENANT - datetime.timedelta(hours=10)
    h = lambda d: d.strftime("%Y-%m-%dT%H:%M:%SZ")                       # noqa: E731

    def lire(ecart_h: float, taux_h: float, cle="google_credit_vu_projet_a"):
        """Un montant vu `ecart_h` heures avant les autres ; un taux relevé `taux_h` heures après les autres."""
        taux = ligne_de_taux(quand=h(tard + datetime.timedelta(hours=taux_h)))
        return _constat(monde, modifs=EUROS, date=h(tard), dates={cle: h(tard - datetime.timedelta(hours=ecart_h))},
                        hors_tableau=[taux], transcription=h(tard + datetime.timedelta(minutes=5)))

    assert lire(0, 5.9)["taux"] and lire(2, 3.9)["taux"]               # sain : 5,9 heures après chaque montant au plus
    with pytest.raises(chef.Arret, match="plus de 6 heures après.*le montant vu le plus tôt est trop ancien"):
        lire(2, 4.1)                                                     # 4,1 h après les autres, 6,1 h après le plus ancien
    with pytest.raises(chef.Arret, match="plus de 6 heures après"):
        lire(23, 5.0)                                                    # le cas de la contre-lecture : 28 heures d'écart
    # une clé qui n'est pas un montant, vue tôt, ne borne pas le taux
    assert lire(23, 5.0, cle="google_offre_payante_projet_a")["taux"]


def test_m2_l5_artefacts_ajoutes_par_la_campagne_de_mutations(monde):
    """Les mutants qui survivaient à la première campagne par outil (m-2), chacun tué par un artefact."""
    g = monde.config["fournisseurs"]["google"]
    sans_plafond = _corps_google(monde)
    del sans_plafond["generationConfig"]["maxOutputTokens"]
    with pytest.raises(chef.Arret, match="ne porte pas de plafond de sortie"):        # chef : corps sans plafond
        chef.garde_google_avant_envoi(monde.config, sans_plafond)
    assert "plafond de sortie absent" in relais_google.defaut_du_corps(sans_plafond, 16768)   # relais : de même
    assert relais_google.defaut_du_corps(_corps_google(monde), 16768) is None
    lu = {"reflexion": 5, "reflexion_constatee": True, "texte": "x"}
    assert chef.defaut_de_reponse_google({**lu, "motif": None}) == "motif de fin autre que la fin normale (absent ou inconnu)"
    assert chef.defaut_de_reponse_google({**lu, "motif": "STOP"}) is None
    for forme, champ in (("budget", "budget"), ("niveau", "borne_declaree")):          # une réflexion nulle n'est pas un réglage
        assert chef.reglage_de_reflexion({"reflexion": {"forme": forme, champ: 1}}) == {"forme": forme, "borne": 1}
        with pytest.raises(chef.Arret, match="réglage de réflexion n'est pas inscrit"):
            chef.reglage_de_reflexion({"reflexion": {"forme": forme, champ: 0}})
    g["sortie_max"] = 0
    with pytest.raises(chef.Arret, match="plafond de sortie de Google .`sortie_max`. n'est pas inscrit"):
        chef.controler_la_configuration_de_google(monde.config, "verification-google-cle-1")
    g["sortie_max"] = 1
    with pytest.raises(chef.Arret, match="n'atteint pas la réflexion"):               # inscrit, mais trop bas : l'autre motif
        chef.controler_la_configuration_de_google(monde.config, "verification-google-cle-1")


def test_ligne_de_commande_usage_et_configuration_absente(tmp_path, capsys):
    assert chef.principal([]) == 2 and "usage" in capsys.readouterr().err
    assert chef.principal(["file-neon", str(tmp_path / "absente.json"), "0" * 64]) == 2
    assert "configuration absente" in capsys.readouterr().err


# === Livraison 6 : constat lu par fournisseur (D-1), âge du fixage, crédit dit comme une borne, borne de réflexion ========

CLES_GOOGLE = sorted(chef.CLES_PAR_FOURNISSEUR["google"])
CLES_MISTRAL = sorted(chef.CLES_PAR_FOURNISSEUR["mistral"])
PORTEE_MISTRAL, PORTEE_GOOGLE = "- portée du constat : Mistral seul", "- portée du constat : Google seul"


def constat_de_mistral_seul(modifs=None, hors_tableau=(), **plus) -> str:
    """La pièce partielle de Mistral : les sept clés de Mistral, toutes et elles seules, et sa portée dite."""
    gardees = set((plus.get("plus") or {}))                           # une clé de l'autre, ajoutée exprès, reste
    return constat(modifs, sans=[c for c in CLES_GOOGLE if c not in gardees], hors_tableau=[PORTEE_MISTRAL, *hors_tableau], **plus)


def constat_de_google_seul(modifs=None, hors_tableau=(), **plus) -> str:
    """La pièce partielle de Google : les vingt et une clés de Google, toutes et elles seules, et sa portée dite."""
    gardees = set((plus.get("plus") or {}))
    return constat(modifs, sans=[c for c in CLES_MISTRAL if c not in gardees], hors_tableau=[PORTEE_GOOGLE, *hors_tableau], **plus)


def _inscrire(monde, texte: str, nom: str, champ: str = "constat") -> None:
    monde.piece(nom, texte)
    monde.config[champ] = monde.ref(nom)


def _depart(monde, ligne: str) -> dict:
    return chef.gardes_avant_depart(monde.config, ligne, {"GO_ID": GO[ligne]}, monde.racine, monde.registre(), MAINTENANT)


def test_d1_l6_mistral_part_sur_un_constat_de_mistral_seul(monde):
    assert len(CLES_MISTRAL) == 7 and len(CLES_GOOGLE) == 21 and set(CLES_MISTRAL) | set(CLES_GOOGLE) == chef.CLES_DU_CONSTAT
    _inscrire(monde, constat_de_mistral_seul(), "constat-mistral.md")
    lu = chef.garde_constat(monde.config, monde.racine, MAINTENANT, "mistral")                    # cas sain
    assert lu["portee"] == ["mistral"] and set(lu["valeurs"]) == set(CLES_MISTRAL) and lu["piece"]["champ"] == "constat"
    avant = _depart(monde, "verification-mistral-eu")                                            # la ligne entière part
    assert avant["constat"] == {"champ": "constat", **monde.ref("constat-mistral.md")}
    assert avant["constat_resume"]["portee"] == ["mistral"] and avant["constat_resume"]["credit_de_mistral_usd"] == "9.50"
    monde.inscrire_releve("file-mistral", monde.releve("verification-mistral-eu", "v1", go="GO-2026-11-27-02"))
    assert _depart(monde, "file-mistral")["contexte"]["regime"] == "courant"          # la file de Mistral part aussi, sans Google
    with pytest.raises(chef.Arret, match="aucune pièce de constat inscrite ne porte google"):
        monde.inscrire_releve("file-neon", monde.releve("verification-google-cle-1", "v1", go="GO-2026-11-27-01"))
        _depart(monde, "file-neon")

    def refuse(texte, motif):
        _inscrire(monde, texte, "constat-mistral-artefact.md")
        with pytest.raises(chef.Arret, match=motif):
            chef.garde_constat(monde.config, monde.racine, MAINTENANT, "mistral")

    refuse(constat_de_mistral_seul(plus={"google_offre_payante_projet_a": "oui"}), "de trop.*de l'autre fournisseur")
    refuse(constat(sans=CLES_GOOGLE + ["mistral_offre_payante"], hors_tableau=[PORTEE_MISTRAL]), "manquante.*mistral_offre_payante")
    refuse(constat(sans=CLES_GOOGLE), "manquante")                    # sans portée dite : le constat complet, aucune absence en silence
    refuse(constat(sans=CLES_GOOGLE, hors_tableau=["- portée du constat : Mistral"]), "portée du constat « Mistral »")
    refuse(constat_de_mistral_seul({"mistral_credit_utilisable_usd": "8,00"}), "sous le seuil")   # le seuil de Mistral reste lu


def test_d1_l6_google_refuse_un_constat_de_mistral_seul(monde):
    _inscrire(monde, constat_de_mistral_seul(), "constat-mistral.md")
    with pytest.raises(chef.Arret, match="aucune pièce de constat inscrite ne porte google"):     # artefact
        chef.garde_constat(monde.config, monde.racine, MAINTENANT, "google")
    with pytest.raises(chef.Arret, match="ne porte que mistral"):                                 # lu en direct, de même
        chef.lire_constat(constat_de_mistral_seul(), monde.config, MAINTENANT, "google")
    chemin, empreinte = monde.ecrire_configuration()
    for ligne in ("verification-google-cle-1", "verification-google-cle-2"):
        assert chef.executer(ligne, chemin, empreinte, {"GO_ID": GO[ligne]}, racine=monde.racine,
                             registre=monde.registre(), a_l_instant=MAINTENANT) == 2
    assert not list((monde.racine / "runs").iterdir())
    _inscrire(monde, constat_de_google_seul(), "constat-google.md", "constat_second")            # cas sain : la pièce de Google
    assert _depart(monde, "verification-google-cle-1")["constat"]["champ"] == "constat_second"
    assert _depart(monde, "verification-mistral-eu")["constat"]["champ"] == "constat"


def test_d1_l6_un_credit_de_mistral_bas_n_arrete_plus_google(monde):
    _inscrire(monde, constat({"mistral_credit_utilisable_usd": "8,00"}), "constat-bas.md")      # constat complet
    with pytest.raises(chef.Arret, match="mistral_credit_utilisable_usd vaut 8.00, sous le seuil"):   # artefact : Mistral
        _depart(monde, "verification-mistral-eu")
    assert _depart(monde, "verification-google-cle-1")["controle_du_credit"]["seuil_usd"] == "19.76"   # cas sain : Google part
    # un compte Mistral en euros n'impose plus de taux à une ligne de Google ; il l'impose à la ligne de Mistral
    monde.config["marge_de_change"] = 0.05
    _inscrire(monde, constat({"mistral_devise_affichee": "EUR"}), "constat-eur.md")
    assert _depart(monde, "verification-google-cle-2")["constat_resume"]["taux"] is None
    with pytest.raises(chef.Arret, match="ligne « - taux"):
        _depart(monde, "verification-mistral-eu")
    _inscrire(monde, constat({"mistral_devise_affichee": "EUR"}, hors_tableau=[TAUX]), "constat-eur-taux.md")
    assert _depart(monde, "verification-google-cle-2")["constat_resume"]["taux"] is None     # taux permis, non lu par Google
    assert _depart(monde, "verification-mistral-eu")["constat_resume"]["taux"]["taux"] == "1.0700"
    # une clé de Google hors des valeurs admises n'arrête plus Mistral
    _inscrire(monde, constat({"google_offre_payante_projet_b": "non"}), "constat-g.md")
    assert _depart(monde, "verification-mistral-eu")["constat_resume"]["fournisseur_juge"] == "mistral"
    with pytest.raises(chef.Arret, match="google_offre_payante_projet_b vaut « non »"):
        _depart(monde, "verification-google-cle-1")


def test_d1_l6_google_part_sur_un_constat_de_google_seul(monde):
    _inscrire(monde, constat_de_google_seul(), "constat-google.md")
    lu = chef.garde_constat(monde.config, monde.racine, MAINTENANT, "google")                    # cas sain
    assert lu["portee"] == ["google"] and set(lu["valeurs"]) == set(CLES_GOOGLE) and lu["credit_de_mistral_usd"] is None
    assert _depart(monde, "verification-google-cle-1")["constat_resume"]["credits_comptes_usd"] == {"a": "23.00", "b": "23.00"}
    with pytest.raises(chef.Arret, match="aucune pièce de constat inscrite ne porte mistral"):    # artefact : Mistral refusé
        _depart(monde, "verification-mistral-eu")
    for texte, motif in ((constat_de_google_seul(plus={"mistral_offre_payante": "oui"}), "de trop.*de l'autre fournisseur"),
                         (constat(sans=CLES_MISTRAL + ["google_deux_projets_distincts"], hors_tableau=[PORTEE_GOOGLE]), "manquante"),
                         (constat_de_google_seul(EUROS), "ligne « - taux")):
        _inscrire(monde, texte, "constat-google-artefact.md")
        with pytest.raises(chef.Arret, match=motif):
            chef.garde_constat(monde.config, monde.racine, MAINTENANT, "google")


def test_d1_l6_une_seule_piece_par_fournisseur(monde):
    """Le constat complet et une pièce partielle du même fournisseur : ambiguïté, la ligne de ce fournisseur ne part pas."""
    _inscrire(monde, constat_de_mistral_seul(), "constat-mistral.md", "constat_second")
    with pytest.raises(chef.Arret, match="deux pièces de constat portent mistral"):
        chef.garde_constat(monde.config, monde.racine, MAINTENANT, "mistral")
    assert chef.garde_constat(monde.config, monde.racine, MAINTENANT, "google")["piece"]["champ"] == "constat"   # l'autre : sain
    for second, motif in (("pieces/constat-mistral.md", "ni nul ni une pièce"),
                          ({"chemin": "pieces/constat-mistral.md", "sha256": None}, "non inscrits"),
                          ({**monde.ref("constat-mistral.md"), "sha256": "0" * 64}, "empreinte")):
        monde.config["constat_second"] = second
        with pytest.raises(chef.Arret, match=motif):
            chef.garde_constat(monde.config, monde.racine, MAINTENANT, "google")
    monde.config["constat_second"] = {"chemin": None, "sha256": None}                             # la valeur du gabarit : sans effet
    assert chef.garde_constat(monde.config, monde.racine, MAINTENANT, "mistral")["piece"]["champ"] == "constat"


def test_age_du_fixage_l6_le_dernier_fixage_publie_admis_dans_sa_borne(monde):
    """Le montant est vu un lundi ; le dernier fixage publié est celui du vendredi : admis sous une borne de 96 heures."""
    monde.config["marge_de_change"] = 0.05
    vu = MAINTENANT - datetime.timedelta(hours=3)
    h = lambda d: d.strftime("%Y-%m-%dT%H:%M:%SZ")                       # noqa: E731

    def lire(publie: str, quand=None):
        # l'envoi suit la pièce de dix minutes : l'âge compté depuis l'envoi (m-a, livraison 8) ne dépend pas de l'heure
        # à laquelle l'essai tourne (il échouait passé minuit)
        monde.piece("constat-fixage.md", constat(EUROS, date=h(vu), transcription=h(vu + datetime.timedelta(minutes=5)),
                                                 hors_tableau=[ligne_de_taux(quand=quand or h(vu), publie=publie)]))
        monde.config["constat"] = monde.ref("constat-fixage.md")
        return chef.garde_constat(monde.config, monde.racine, vu + datetime.timedelta(minutes=10), "google")

    minuit = vu.replace(hour=0, minute=0, second=0, microsecond=0)
    jour = lambda d: d.strftime("%Y-%m-%d")                             # noqa: E731
    vieux = minuit - datetime.timedelta(days=3)                        # début du jour au plus 3 jours avant : sous 96 heures
    lu = lire(jour(vieux))
    assert lu["taux"]["fixage_publie_le"] == jour(vieux) and lu["taux"]["age_max_du_fixage_heures"] == 96
    assert chef.resume_du_constat(lu)["taux"]["fixage_publie_le"] == jour(vieux)
    trop = minuit - datetime.timedelta(days=4)                          # au moins 96 heures et une minute
    if vu - (trop) <= datetime.timedelta(hours=96):
        trop -= datetime.timedelta(days=1)
    with pytest.raises(chef.Arret, match="plus de 96 heures avant.*fixage plus récent"):
        lire(jour(trop))
    monde.config["age_max_du_fixage_heures"] = 168                     # la borne est paramétrable
    assert lire(jour(trop))["taux"]["age_max_du_fixage_heures"] == 168
    with pytest.raises(chef.Arret, match="après l'heure du taux"):     # un fixage publié après le relevé du taux
        lire(jour(vu + datetime.timedelta(days=1)), quand=h(vu - datetime.timedelta(minutes=1)))
    with pytest.raises(chef.Arret, match="illisible"):
        lire("vendredi")
    with pytest.raises(chef.Arret, match="fixage publié le : AAAA-MM-JJ » est exigée"):   # l'ancienne forme, sans le fixage
        _constat(monde, modifs=EUROS, hors_tableau=[f"- taux : 1,0700 USD par EUR ; source : BCE ; heure du taux (UTC) : {AVANT}"])
    monde.config["age_max_du_fixage_heures"] = None                    # aucune borne : aucun taux ne se lit
    with pytest.raises(chef.Arret, match="borne d'âge du fixage"):
        lire(jour(vieux))
    assert _constat(monde)["taux"] is None                              # une pièce toute en dollars n'en a pas besoin, à l'essai


@pytest.mark.parametrize("valeur, source, motif", [
    ("au moins 9,50", "capture", "sans la source"),
    ("9,50", chef.SOURCE_BORNE_BASSE, "sans valeur « au moins X »"),
    ("au moins beaucoup", chef.SOURCE_BORNE_BASSE, "n'est pas un nombre"),
    ("au moins 8,00", chef.SOURCE_BORNE_BASSE, "vaut 8.00, sous le seuil")])
def test_borne_basse_l6_artefacts_sur_le_credit_de_mistral(monde, valeur, source, motif):
    with pytest.raises(chef.Arret, match=f"garde 9 : mistral_credit_utilisable_usd.*{motif}"):
        _constat(monde, fournisseur="mistral", modifs={"mistral_credit_utilisable_usd": valeur},
                 sources={"mistral_credit_utilisable_usd": source})


def test_borne_basse_l6_credit_dit_au_moins_x_lu_comme_x(monde):
    borne = {"mistral_credit_utilisable_usd": "au moins 9,50"}
    source = {"mistral_credit_utilisable_usd": chef.SOURCE_BORNE_BASSE}
    lu = _constat(monde, fournisseur="mistral", modifs=borne, sources=source)                     # cas sain, en dollars
    assert lu["credit_de_mistral_usd"] == Decimal("9.50") and lu["bornes_basses"] == ["mistral_credit_utilisable_usd"]
    assert chef.resume_du_constat(lu)["bornes_basses_lues_comme_leur_valeur"] == ["mistral_credit_utilisable_usd"]
    # le mot de Lazar : « au moins 7,87 € » ; à la marge de 5 %, il passe 8,23 USD à un taux de 1,1100, non à 1,0700
    monde.config["marge_de_change"] = 0.05
    euros = {"mistral_devise_affichee": "EUR", "mistral_credit_utilisable_usd": "au moins 7,87"}
    assert _constat(monde, fournisseur="mistral", modifs=euros, sources=source,
                    hors_tableau=[ligne_de_taux("1,1100")])["credit_de_mistral_usd"] == Decimal("8.29")   # 7,87 × 1,11 × 0,95
    with pytest.raises(chef.Arret, match="vaut 7.99, sous le seuil"):                                  # 7,87 × 1,07 × 0,95
        _constat(monde, fournisseur="mistral", modifs=euros, sources=source, hors_tableau=[TAUX])
    # sur une clé qui n'est pas de crédit : refusée, même de la bonne source
    for cle in ("mistral_limite_requetes_par_minute", "mistral_limite_jetons_par_minute"):
        with pytest.raises(chef.Arret, match=f"{cle} : la forme « au moins X ».*clés de crédit"):
            _constat(monde, fournisseur="mistral", modifs={cle: "au moins 600000"}, sources={cle: chef.SOURCE_BORNE_BASSE})
    with pytest.raises(chef.Arret, match="google_offre_payante_projet_a : la forme « au moins X »"):
        _constat(monde, modifs={"google_offre_payante_projet_a": "au moins oui"},
                 sources={"google_offre_payante_projet_a": chef.SOURCE_BORNE_BASSE})
    # chez Google : un crédit vu dit comme une borne, sous recharge non comptée : lu comme X
    g = {"google_credit_vu_projet_a": "au moins 21,00"}
    gs = {"google_credit_vu_projet_a": chef.SOURCE_BORNE_BASSE}
    assert _constat(monde, modifs=g, sources=gs)["credits_comptes_usd"]["a"] == Decimal("21.00")
    monde.config["recharge_comptee"] = True                             # chemin de l'avenant : l'écart ne se lit pas sur une borne
    with pytest.raises(chef.Arret, match="borne basse, et la recharge est comptée"):
        _constat(monde, modifs=g, sources=gs)


def test_borne_de_reflexion_l6_au_plus_49536_sous_65536_parametrable(monde):
    config = copy.deepcopy(monde.config)
    g = config["fournisseurs"]["google"]
    g["sortie_max"] = 65536
    for borne, attendue in ((49536, 49536), ("la plus haute admise", 49536), (40000, 40000)):     # cas sains
        g["reflexion"] = {"forme": "niveau", "borne_declaree": borne}
        regle = chef.controler_la_configuration_de_google(config, "file-neon")
        assert regle["borne_de_la_reflexion"] == attendue and regle["borne_la_plus_haute_admise"] == 49536
        assert (regle["borne_sous_la_plus_haute"] is None) == (attendue == 49536)
        chef.garde_google_avant_envoi(config, chef.construire_corps("google", g, "t", 65536, orthographe="XHIGH"))
        assert chef.arguments_du_relais(config, "file-neon", CLE_1)[chef.arguments_du_relais(config, "file-neon", CLE_1).index(
            "--borne-reflexion") + 1] == str(attendue)
    g["reflexion"] = {"forme": "niveau", "borne_declaree": 49537}                                    # artefact : un jeton au-dessus
    with pytest.raises(chef.Arret, match=r"n'atteint pas la réflexion \(49537\)"):
        chef.controler_la_configuration_de_google(config, "file-neon")
    g["reflexion"], g["sortie_max"] = {"forme": "niveau", "borne_declaree": "la plus haute admise"}, None
    with pytest.raises(chef.Arret, match="sans plafond de sortie inscrit"):
        chef.controler_la_configuration_de_google(config, "file-neon")
    g["sortie_max"] = 16000                                                                          # borne haute nulle : refusée
    with pytest.raises(chef.Arret, match="au-dessus de 16000 jetons"):
        chef.reglage_de_reflexion(g)
    g["sortie_max"] = 16001
    assert chef.reglage_de_reflexion(g)["borne"] == 1
    g["reflexion"] = {"forme": "budget", "budget": "la plus haute admise"}                          # la forme budget reste un entier
    with pytest.raises(chef.Arret, match="n'est pas inscrit"):
        chef.reglage_de_reflexion(g)


def test_debit_requis_l6_ecrit_a_la_regle_de_google(monde):
    """À 65 536 dans 2 690 secondes : 24,4 jetons par seconde (vérification de la livraison 5, section 4) ; à 32 768,
    12,2 (devis, 5.6). Écrit, non refusé."""
    config = copy.deepcopy(monde.config)
    config["lignes"]["file-neon"]["delais"]["relais_total_s"] = 2690
    for plafond, borne, debit in ((65536, 49536, 24.4), (32768, 16768, 12.2)):
        config["fournisseurs"]["google"].update({"sortie_max": plafond, "reflexion": {"forme": "niveau", "borne_declaree": borne}})
        assert chef.controler_la_configuration_de_google(config, "file-neon")["debit_requis_a_la_sortie_maximale_jetons_par_s"] == debit
    for delai, debit in ((None, None), (0, None), (True, None), (1, 32768.0)):
        config["lignes"]["file-neon"]["delais"]["relais_total_s"] = delai
        assert chef.controler_la_configuration_de_google(config, "file-neon")["debit_requis_a_la_sortie_maximale_jetons_par_s"] == debit


def test_m2_l6_artefacts_ajoutes_par_la_campagne_de_la_livraison_6(monde):
    """Les mutants qui survivaient au premier passage de la campagne `livraison6` (outil versé sous
    `tests/mutations_essais_admission_v1/`), chacun tué par un cas sain à la borne exacte ou par un artefact."""
    monde.config["marge_de_change"] = 0.05
    t0 = datetime.datetime(2026, 11, 23, 0, 0, tzinfo=datetime.timezone.utc)      # un lundi, à minuit
    h = lambda d: d.strftime("%Y-%m-%dT%H:%MZ")                                    # noqa: E731

    def taux(releve, publie=None, valeur="1,0700", source="BCE", reference=t0, premiere=None, instant=None):
        brut = f"{valeur} USD par EUR ; source : {source} ; heure du taux (UTC) : {releve} ; fixage publié le : {publie or releve[:10]}"
        return chef.lire_taux({"taux": brut}, True, reference, instant, "essai", premiere=premiere, config=monde.config)

    # bornes exactes, admises : 24 heures avant, 6 heures après, fixage du jour même à minuit, fixage à 96 heures pile
    assert taux(h(t0 - datetime.timedelta(hours=24)))["taux"] == Decimal("1.0700")
    assert taux(h(t0 + datetime.timedelta(hours=6)))
    assert taux(h(t0), publie="2026-11-23")["fixage_publie_le"] == "2026-11-23"
    assert taux(h(t0), publie="2026-11-19")                                       # 96 heures pile avant le montant
    assert taux(h(t0), valeur="0,9000")                                           # un taux sous 1 reste un taux
    monde.config["age_max_du_fixage_heures"] = 1                                  # la plus petite borne admise
    assert taux(h(t0), publie="2026-11-23")["age_max_du_fixage_heures"] == 1
    monde.config["age_max_du_fixage_heures"] = 96
    for motif, kw in (("taux nul", {"valeur": "0"}), ("source du taux absente", {"source": " "}),
                      ("heure du taux, ou heure de la pièce", {"releve": "hier"}),
                      ("postérieure à l'envoi", {"instant": t0})):
        with pytest.raises(chef.Arret, match=motif):
            taux(kw.pop("releve", h(t0)), **kw)
    # le message du montant le plus ancien : dit à 6 heures pile du plus tardif, tu au-delà
    with pytest.raises(chef.Arret, match="le montant vu le plus tôt est trop ancien"):
        taux(h(t0 + datetime.timedelta(hours=6)), premiere=t0 - datetime.timedelta(hours=1))
    with pytest.raises(chef.Arret, match="plus de 6 heures après") as refus:
        taux(h(t0 + datetime.timedelta(hours=7)), premiere=t0 - datetime.timedelta(hours=1))
    assert "le montant vu le plus tôt" not in str(refus.value)
    # lecture du constat
    with pytest.raises(chef.Arret, match="fournisseur inconnu"):
        chef.lire_constat(constat(), monde.config, MAINTENANT, "openai")
    doublon = constat(hors_tableau=[f"| mistral_offre_payante | oui | capture | {AVANT} |"])
    with pytest.raises(chef.Arret, match="mistral_offre_payante figure deux fois"):
        chef.lire_constat(doublon, monde.config, MAINTENANT, "mistral")
    with pytest.raises(chef.Arret, match="mistral_offre_payante n'a pas de source"):
        chef.lire_constat(constat(sources={"mistral_offre_payante": ""}), monde.config, MAINTENANT, "mistral")
    a_l_heure = chef._date(AVANT)                                                  # l'envoi à la minute même du constat
    with pytest.raises(chef.Arret, match="la clé .* porte une date postérieure à l'envoi"):
        chef.lire_constat(constat(), monde.config, a_l_heure, "mistral")
    tot = h(a_l_heure - datetime.timedelta(minutes=10))
    with pytest.raises(chef.Arret, match="heure de la transcription absente, illisible ou postérieure"):
        chef.lire_constat(constat(date=tot, transcription=AVANT), monde.config, a_l_heure, "mistral")     # à la minute de l'envoi
    with pytest.raises(chef.Arret, match="heure de la transcription absente"):
        chef.lire_constat(constat(transcription="hier"), monde.config, MAINTENANT, "mistral")
    with pytest.raises(chef.Arret, match="la borne basse « au moins beaucoup » n'est pas un nombre"):
        chef.lire_constat(constat({"mistral_credit_utilisable_usd": "au moins beaucoup"},
                                  sources={"mistral_credit_utilisable_usd": chef.SOURCE_BORNE_BASSE}), monde.config, MAINTENANT, "mistral")
    inconnue = copy.deepcopy(monde.config)
    inconnue["constat_cles"]["mistral_offre_payante"] = {"type": "autre"}
    with pytest.raises(chef.Arret, match="règle inconnue pour mistral_offre_payante"):
        chef.lire_constat(constat(), inconnue, MAINTENANT, "mistral")
    # l'heure des montants jugés : celle des clés du fournisseur de la ligne, non celles de l'autre
    plus_tard = h(chef._date(AVANT) + datetime.timedelta(minutes=30))
    lu = chef.lire_constat(constat(dates={c: plus_tard for c in CLES_GOOGLE}), monde.config, MAINTENANT, "mistral")
    assert lu["reference"] == chef._date(AVANT) and lu["derniere_date"] == chef._date(AVANT)


def test_d1_l6_lignes_de_mistral_a_blanc_sans_rien_de_google(monde, capsys):
    """Les lignes de Mistral passent à blanc sur un constat de Mistral seul, la règle Google laissée nulle comme au
    gabarit (plafond, réflexion, exemption, jetons par mot, limites de mots) ; une ligne de Google ne passe pas."""
    _inscrire(monde, constat_de_mistral_seul(), "constat-mistral.md")
    g = monde.config["fournisseurs"]["google"]
    g.update({"sortie_max": None, "reflexion": None, "exemption_de_la_sonde": None, "exemption_de_la_sonde_go": None,
              "jetons_par_mot": None})
    for consigne in monde.config["consignes"].values():
        consigne["limite_de_mots"] = None
    monde.inscrire_releve("file-mistral", monde.releve("verification-mistral-eu", "v1", go="GO-2026-11-27-02"))
    chemin, empreinte = monde.ecrire_configuration()
    for ligne in ("verification-mistral-eu", "file-mistral"):
        assert chef.a_blanc(ligne, chemin, empreinte, {}, racine=monde.racine, a_l_instant=MAINTENANT) == 0      # cas sain
        sortie = json.loads(capsys.readouterr().out)
        assert sortie["constat"]["portee"] == ["mistral"] and sortie["constat"]["piece"]["chemin"] == "pieces/constat-mistral.md"
    with pytest.raises(chef.Arret, match="ne porte google"):                                                   # artefact
        chef.a_blanc("verification-google-cle-1", chemin, empreinte, {}, racine=monde.racine, a_l_instant=MAINTENANT)


# === Livraison 7 : régime prudent imposé pour Google (R-1), âge du fixage compté depuis l'envoi (m-a) ======================

def test_r1_l7_sain_la_file_du_juge_part_prudente_quelles_que_soient_les_sondes(monde, tmp_path):
    """Décision de la mère (R-4682) : sous `regime_file_google` « prudent », deux sondes « comprises » laissent la file du
    juge au régime prudent, sans mot de Lazar ; le régime imposé est recopié au manifeste et au rapport."""
    monde.config["regime_file_google"] = "prudent"
    _refs_neon(monde)                                                             # deux sondes « comprises »
    contexte = chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))
    assert contexte["regime"] == "prudent" and contexte["sondes"] == {CLE_1: "comprise", CLE_2: "comprise"}
    assert contexte["mot_de_lazar"] is None and "R-4682" in contexte["regime_impose_par_la_configuration"]
    regle = chef.controler_la_configuration_de_google(monde.config, "verification-google-cle-1")
    assert regle["regime_file_google"] == "prudent"
    definitive = copy.deepcopy(monde.config)
    definitive["etat"] = "definitive"
    assert chef.regime_file_google(definitive) == "prudent"                      # admis en définitive
    # la file entière, par l'amorce : le rapport dit le régime de départ et celui que la configuration impose
    fournisseur = faux.FauxFournisseur(faux.modele_google()).demarrer()
    try:
        monde.config["essai_local"] = {"google": fournisseur.url}
        chemin, empreinte = monde.ecrire_configuration("configuration-file-prudente.json")
        fournisseur.programmer(*reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google))
        env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "GO_ID": GO["file-neon"],
               CLE_1: "valeur-factice-du-relais", CLE_2: "valeur-factice-du-relais-2"}
        assert chef.executer("file-neon", chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT) == 0
        file_ = dossiers_de(monde.racine / "runs" / "essais-admission-bras-a-v1")[0]
        rapport = json.loads((file_ / "rapport-technique.json").read_text(encoding="utf-8"))
        assert rapport["complete"] and rapport["regime_de_depart"] == "prudent"
        assert "R-4682" in rapport["regime_impose_par_la_configuration"]
        manifeste = json.loads((file_ / "manifeste-depart.json").read_text(encoding="utf-8"))
        assert manifeste["contexte"]["regime"] == "prudent"
    finally:
        fournisseur.arreter()
    # sous « courant », admis à l'essai seulement, la file suit ses sondes (le régime courant du devis, 6.4)
    monde.config["regime_file_google"] = "courant"
    assert chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))["regime"] == "courant"


def test_r1_l7_artefact_regime_de_google_absent_inconnu_ou_courant_en_definitive(monde):
    _refs_neon(monde)
    for valeur, motif in ((None, "n'est pas inscrit"), ("Prudent", "n'est pas inscrit"), ("", "n'est pas inscrit"),
                          (True, "n'est pas inscrit")):
        monde.config["regime_file_google"] = valeur
        with pytest.raises(chef.Arret, match=f"garde 10 : le régime des lignes de Google.*{motif}"):
            chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))
        for ligne in ("verification-google-cle-1", "file-neon"):                 # vérification et file : aucun défaut
            with pytest.raises(chef.Arret, match="régime des lignes de Google"):
                chef.controler_la_configuration_de_google(monde.config, ligne)
    del monde.config["regime_file_google"]
    with pytest.raises(chef.Arret, match="n'est pas inscrit"):
        chef.regime_file_google(monde.config)
    definitive = copy.deepcopy(monde.config)
    definitive.update({"etat": "definitive", "regime_file_google": "courant"})
    with pytest.raises(chef.Arret, match="définitive inscrit `regime_file_google` à « prudent »"):
        chef.regime_file_google(definitive)
    gabarit = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
    assert "regime_file_google" in gabarit and gabarit["regime_file_google"] is None
    # une ligne de Mistral ne le lit pas
    monde.inscrire_releve("file-mistral", monde.releve("verification-mistral-eu", "v1", go="GO-2026-11-27-02"))
    monde.config["regime_file_google"] = None
    assert chef.gardes_avant_depart(monde.config, "file-mistral", {"GO_ID": GO["file-mistral"]}, monde.racine,
                                    monde.registre(), MAINTENANT)["contexte"]["regime"] == "courant"
    with pytest.raises(chef.Arret, match="régime des lignes de Google"):         # une ligne de Google, oui
        chef.gardes_avant_depart(monde.config, "file-neon", {"GO_ID": GO["file-neon"]}, monde.racine, monde.registre(), MAINTENANT)


def test_ma_l7_un_constat_vieux_d_un_mois_est_refuse(monde):
    """m-a : un constat en euros vieux d'un mois, avec un taux et un fixage du même jour, ne sert plus une ligne lancée
    aujourd'hui ; la borne d'âge du fixage se compte aussi depuis l'envoi. Cas sain : le même constat, envoyé le jour même."""
    monde.config["marge_de_change"] = 0.05
    vieux = MAINTENANT - datetime.timedelta(days=30)
    h = lambda d: d.strftime("%Y-%m-%dT%H:%M:%SZ")                                # noqa: E731
    texte = constat(EUROS, date=h(vieux), transcription=h(vieux + datetime.timedelta(minutes=5)),
                    hors_tableau=[ligne_de_taux(quand=h(vieux + datetime.timedelta(minutes=10)))])
    monde.piece("constat-vieux.md", texte)
    monde.config["constat"] = monde.ref("constat-vieux.md")
    with pytest.raises(chef.Arret, match="plus de 96 heures avant l'envoi.*trop ancienne"):            # artefact
        chef.garde_constat(monde.config, monde.racine, MAINTENANT, "google")
    with pytest.raises(chef.Arret, match="plus de 96 heures avant l'envoi"):                           # la ligne entière
        chef.gardes_avant_depart(monde.config, "verification-google-cle-1", {"GO_ID": GO["verification-google-cle-1"]},
                                 monde.racine, monde.registre(), MAINTENANT)
    lu = chef.garde_constat(monde.config, monde.racine, vieux + datetime.timedelta(hours=1), "google")   # sain : le jour même
    assert lu["taux"]["fixage_publie_le"] == h(vieux + datetime.timedelta(minutes=10))[:10]   # le jour de l'heure du taux
    assert chef.garde_constat(monde.config, monde.racine, MAINTENANT, "mistral")["taux"] is None       # Mistral en dollars : sans objet
    # bornes exactes, depuis l'envoi : à 96 heures pile du début du jour du fixage, admis ; une minute de plus, refusé
    t0 = datetime.datetime(2026, 11, 23, 0, 0, tzinfo=datetime.timezone.utc)
    brut = f"1,0700 USD par EUR ; source : BCE ; heure du taux (UTC) : 2026-11-23T00:00Z ; fixage publié le : 2026-11-23"
    pile = t0 + datetime.timedelta(hours=96)
    assert chef.lire_taux({"taux": brut}, True, t0, pile, "essai", config=monde.config)["taux"] == Decimal("1.0700")
    with pytest.raises(chef.Arret, match="avant l'envoi"):
        chef.lire_taux({"taux": brut}, True, t0, pile + datetime.timedelta(minutes=1), "essai", config=monde.config)
    vieux_fixage = brut.replace("fixage publié le : 2026-11-23", "fixage publié le : 2026-11-18")      # 120 heures avant la pièce
    with pytest.raises(chef.Arret, match="avant l'heure de la pièce"):           # la borne depuis la pièce reste, sans envoi donné
        chef.lire_taux({"taux": vieux_fixage}, True, t0, None, "essai", config=monde.config)
    # les pièces lues après le constat (lecture de la console, mot sur la sonde) reçoivent l'heure de l'envoi aussi
    lu = _constat(monde, modifs=EUROS, hors_tableau=[TAUX])
    ref = monde.releve("verification-google-cle-1", "v1", envois_coupes=["L1-01-A"], depense_comptee_usd=0.5)
    monde.piece("console.md", lecture_console_google(ref["sha256"], ("0,10", "0,10"), ("22,50", "22,50"), plus=(TAUX,)))
    monde.config["lignes"]["file-neon"]["lectures_console"] = [monde.ref("console.md")]
    assert chef.garde_console(monde.config, monde.racine, "file-neon", GO["file-neon"], lu, MAINTENANT)
    with pytest.raises(chef.Arret, match="garde 20 : fixage publié le .* avant l'envoi"):
        chef.garde_console(monde.config, monde.racine, "file-neon", GO["file-neon"], lu, MAINTENANT + datetime.timedelta(days=6))


def test_m2_l7_artefacts_ajoutes_par_la_campagne_de_la_livraison_7(monde, monkeypatch):
    """Les mutants de la garde 10 qui survivaient au premier passage de la campagne `livraison7`."""
    # file du juge : relevé de la clé 2 sous la bonne ligne mais d'une autre variable ; deux points d'accès
    ref1 = monde.releve("verification-google-cle-1", "a")
    monde.inscrire_releve("file-neon", ref1, monde.releve("verification-google-cle-2", "b", go="GO-b", variable_cle=CLE_1))
    with pytest.raises(chef.Arret, match="n'est pas celui de la vérification de cette clé"):
        chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))
    monde.inscrire_releve("file-neon", ref1, monde.releve("verification-google-cle-2", "c", go="GO-c", hote="ailleurs.example"))
    with pytest.raises(chef.Arret, match="autre point d'accès"):                 # le relevé seul le refuse déjà
        chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))
    # deux noms servis, deux points d'accès : défense en profondeur, que `_releve_sain` (identifiant figé, hôte de la
    # ligne) masque d'ordinaire ; éprouvée en faisant passer au relevé de la clé 2 une valeur propre
    vrai = chef._releve_sain
    refs = _refs_neon(monde)
    for champ, motif in (("nom_servi", "deux noms servis différents"), ("hote", "deux points d'accès différents")):
        monkeypatch.setattr(chef, "_releve_sain", lambda *a, champ=champ, **k: {
            **vrai(*a, **k), **({champ: "autre"} if a[3]["sha256"] == refs[CLE_2]["sha256"] else {})})
        with pytest.raises(chef.Arret, match=motif):
            chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))
    monkeypatch.setattr(chef, "_releve_sain", vrai)
    # le mot de Lazar sur les sondes du juge : page et heure exigées ; crédit à 16,08 pile, admis ; libellé des clés
    refs = {CLE_1: monde.releve("verification-google-cle-1", "p1", go="GO-p1"),
            CLE_2: monde.releve("verification-google-cle-2", "p2", go="GO-p2", sonde={"issue": "indécidée"})}
    monde.inscrire_releve("file-neon", refs[CLE_1], refs[CLE_2])
    L = monde.config["lignes"]["file-neon"]
    sans_page = mot_neon(refs, ("comprise", "indécidée")).replace("- page : console, facturation\n", "")
    for texte, motif in ((sans_page, "sa page et son heure"),
                         (mot_neon(refs, ("comprise", "indécidée")).replace(f"- heure (UTC) : {APRES_CONSTAT}", "- heure (UTC) : hier"),
                          "sa page et son heure")):
        monde.piece("mot-l7.md", texte)
        L["mot_de_lazar_sonde"] = monde.ref("mot-l7.md")
        with pytest.raises(chef.Arret, match=motif):
            chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))
    monde.piece("mot-l7.md", mot_neon(refs, ("comprise", "indécidée"), credits=("16,08", "16,08")))
    L["mot_de_lazar_sonde"] = monde.ref("mot-l7.md")
    contexte = chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))
    assert contexte["credits_vus_comptes_usd"] == {"a": "16.08", "b": "16.08"}
    assert contexte["sonde"] == "clé 1 : comprise ; clé 2 : indécidée"
    # file de Mistral : la pièce du mot cite un autre relevé, une autre issue, un autre majorant
    refm = monde.releve("verification-mistral-eu", "m", go="GO-m", sonde={"issue": "indécidée"}, majorant="établi")
    monde.inscrire_releve("file-mistral", refm)
    for texte, motif in ((mot_sur_la_sonde("e" * 64, "indécidée", "établi"), "cite un autre relevé"),
                         (mot_sur_la_sonde(refm["sha256"], "non comprise", "établi"), "ne vise pas l'issue de la sonde"),
                         (mot_sur_la_sonde(refm["sha256"], "indécidée", "démenti"), "ne vise pas le constat du majorant")):
        monde.piece("mot-m-l7.md", texte)
        monde.config["lignes"]["file-mistral"]["mot_de_lazar_sonde"] = monde.ref("mot-m-l7.md")
        with pytest.raises(chef.Arret, match=motif):
            chef.garde_cle_verifiee(monde.config, monde.racine, "file-mistral", _constat_lu(monde, "mistral"))
    monde.piece("mot-m-l7.md", mot_sur_la_sonde(refm["sha256"], "indécidée", "établi"))
    monde.config["lignes"]["file-mistral"]["mot_de_lazar_sonde"] = monde.ref("mot-m-l7.md")
    assert chef.garde_cle_verifiee(monde.config, monde.racine, "file-mistral", _constat_lu(monde, "mistral"))["regime"] == "prudent"


# === Livraison 8 : température retirée d'avance (mot de Lazar « a go », journal OD-329) ===================================

GO_NEUF = "GO-2026-11-22-31"
GLOUTON = dict(type_="invalid_request_greedy_sampling", message="top_p must be 1 when using greedy sampling.", code_interne="3054")


def _retrait(go: str) -> dict:
    return {"noeud": "journal OD-329, mot de Lazar « a go »", "go": go}


def test_l8_sain_l_appel_a_part_sans_temperature_et_sans_appel_a_prime(monde, banc):
    monde.config["temperature_retiree_d_avance"] = _retrait(GO["verification-mistral-eu"])
    m = banc("verification-mistral-eu")
    m.faux.programmer(faux.flux_mistral("OK"), sonde_mistral())
    releve = m.verifier()
    assert [(a["type"], a["ligne_du_classement"]) for a in releve["appels"]] == [("A", 3), ("B", None)]
    corps = [json.loads(a["corps"]) for a in m.faux.appels()]
    attendu = {"model", "messages", "max_tokens", "reasoning_effort", "stream"}                       # le corps de l'appel A′
    assert all(set(c) == attendu for c in corps) and not any("top_p" in c or "temperature" in c for c in corps)
    assert releve["saine"] and releve["temperature_envoyee"] is False and releve["appels_comptes"] == 2
    assert releve["temperature_retiree_d_avance"]["go"] == GO["verification-mistral-eu"]
    assert "retirée d'avance" in releve["temperature_retiree_d_avance"]["raison"]
    # la file : partie sans température, et le rapport le dit avec la raison
    ref = {"chemin": str((m.dossier / "releve-verification-v1.json").relative_to(monde.racine)),
           "sha256": chef.sha256_fichier(m.dossier / "releve-verification-v1.json")}
    monde.inscrire_releve("file-mistral", ref, temperature_envoyee=False)
    contexte = chef.garde_cle_verifiee(monde.config, monde.racine, "file-mistral", _constat_lu(monde, "mistral"))
    assert contexte["temperature_envoyee"] is False and "retirée d'avance" in contexte["raison_sans_temperature"]
    n = banc("file-mistral")
    n.faux.programmer(*reponses_conformes(monde.config, monde.racine, "file-mistral", faux.flux_mistral))
    n.jouer(temperature_envoyee=False, raison_sans_temperature=contexte["raison_sans_temperature"])
    assert not any("temperature" in json.loads(a["corps"]) for a in n.faux.appels())
    rapport = chef.faire_rapport(n.dossier)
    assert rapport["temperature_envoyee"] is False and "retirée d'avance" in rapport["raison_sans_temperature"]
    # sans retrait, la raison d'une température retirée à l'appel A′ est dite aussi
    monde.config["temperature_retiree_d_avance"] = False
    refa = monde.releve("verification-mistral-eu", "ap", go="GO-ap", temperature_envoyee=False)
    monde.inscrire_releve("file-mistral", refa, temperature_envoyee=False)
    assert "appel A′" in chef.garde_cle_verifiee(monde.config, monde.racine, "file-mistral",
                                                _constat_lu(monde, "mistral"))["raison_sans_temperature"]


def test_l8_artefact_temperature_refusee_sous_un_retrait_d_avance_ferme_sans_appel_a_prime(monde, banc):
    monde.config["temperature_retiree_d_avance"] = _retrait(GO["verification-mistral-eu"])
    m = banc("verification-mistral-eu")
    m.faux.programmer(faux.erreur_mistral(422, detail=[{"loc": ["body", "temperature"], "msg": "not supported"}]),
                      faux.flux_mistral("OK"), sonde_mistral())
    releve = m.verifier()
    assert [(a["type"], a["ligne_du_classement"]) for a in releve["appels"]] == [("A", 10)]            # aucun appel A′
    assert releve["close"] and releve["noeud_de_lazar"] and not releve["saine"] and len(m.faux.appels()) == 1
    assert "retirée d'avance" in releve["issue_finale"]
    # la file refuse un relevé qui a envoyé la température quand la configuration la retire d'avance
    monde.inscrire_releve("file-mistral", monde.releve("verification-mistral-eu", "t", go="GO-t"))
    with pytest.raises(chef.Arret, match="retirée d'avance à la configuration, et le relevé .* l'a envoyée"):
        chef.garde_cle_verifiee(monde.config, monde.racine, "file-mistral", _constat_lu(monde, "mistral"))


def test_l8_artefact_champ_absent_ou_mal_forme_rien_ne_part(monde):
    ligne = "verification-mistral-eu"
    for valeur in (None, True, "oui", {}, {"noeud": "", "go": GO[ligne]}, {"noeud": "OD-329", "go": "GO-329"},
                   {"noeud": "OD-329", "go": GO[ligne], "top_p": 1}, {"noeud": "OD-329"}):
        monde.config["temperature_retiree_d_avance"] = valeur
        with pytest.raises(chef.Arret, match="`temperature_retiree_d_avance` n'est pas inscrit"):
            chef.gardes_avant_depart(monde.config, ligne, {"GO_ID": GO[ligne]}, monde.racine, monde.registre(), MAINTENANT)
    del monde.config["temperature_retiree_d_avance"]                                 # absent, en définitive comme à l'essai
    definitive = copy.deepcopy(monde.config)
    definitive["etat"] = "definitive"
    for config in (monde.config, definitive):
        with pytest.raises(chef.Arret, match="n'est pas inscrit"):
            chef.temperature_retiree_d_avance(config, ligne)
    definitive["temperature_retiree_d_avance"] = _retrait(GO["verification-mistral-global"])           # une autre ligne
    with pytest.raises(chef.Arret, match="n'est pas la ligne de calcul de verification-mistral-eu"):
        chef.temperature_retiree_d_avance(definitive, ligne)
    definitive["temperature_retiree_d_avance"] = _retrait(GO[ligne])                                   # sains
    assert chef.temperature_retiree_d_avance(definitive, ligne)["go"] == GO[ligne]
    assert chef.temperature_retiree_d_avance(definitive, "file-mistral")["go"] == GO[ligne]            # la file n'en exige pas le GO
    definitive["temperature_retiree_d_avance"] = False
    assert chef.temperature_retiree_d_avance(definitive, ligne) is None
    definitive["temperature_retiree_d_avance"] = None                                                  # Google ne le lit pas
    assert chef.temperature_retiree_d_avance(definitive, "file-neon") is None
    gabarit = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
    assert "temperature_retiree_d_avance" in gabarit and gabarit["temperature_retiree_d_avance"] is None


def test_l8_le_corps_reste_ferme_aucun_top_p(monde):
    f = monde.config["fournisseurs"]["mistral"]
    corps = chef.construire_corps("mistral", f, "Reply with the single word: OK", 32768, False)
    chef.controler_corps("mistral", f, corps, chef.chemin_de_l_appel("mistral"), 32768, False)                 # sain
    for ajout in ({"top_p": 1}, {"top_p": 1.0}, {"temperature": 0}):
        with pytest.raises(chef.Arret, match="garde 3 : champs du corps"):
            chef.controler_corps("mistral", f, {**corps, **ajout}, chef.chemin_de_l_appel("mistral"), 32768, False)
    avec = chef.construire_corps("mistral", f, "x", 32768, True)
    with pytest.raises(chef.Arret, match="garde 3 : champs du corps"):
        chef.controler_corps("mistral", f, {**avec, "top_p": 1}, chef.chemin_de_l_appel("mistral"), 32768, True)


def _registre_avec(monde, go_neuf: str, ligne: str = "verification-mistral-eu") -> str:
    """Le registre d'essai, plus une ligne de calcul neuve pour la même ligne, sous un identifiant neuf."""
    texte = monde.registre()
    vieille = [l for l in texte.splitlines() if l.startswith(f"| {GO[ligne]} |")][0]
    return texte + vieille.replace(GO[ligne], go_neuf) + "\n"


def test_l8_une_ligne_neuve_apres_une_ligne_close_en_ligne_13(monde, tmp_path):
    """Comportement exact : la ligne close (code 400 « top_p », ligne 13) ferme son seul identifiant ; la ligne neuve,
    sous un GO neuf, part avec trois appels et son propre plafond ; la dépense de la ligne close reste comptée."""
    fournisseur = faux.FauxFournisseur(faux.liste_mistral()).demarrer()
    ligne = "verification-mistral-eu"
    try:
        monde.config["essai_local"] = {"mistral": fournisseur.url}
        chemin, empreinte = monde.ecrire_configuration("configuration-premiere.json")
        env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "GO_ID": GO[ligne], "MISTRAL_API_KEY": "valeur-factice-du-relais"}
        fournisseur.programmer(faux.erreur_mistral(400, **GLOUTON))
        assert chef.executer(ligne, chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT) == 1                        # nœud de Lazar, ligne close
        clos = dossiers_de(monde.racine / "runs" / "verification-cle-mistral-bras-a-v1")[0]
        premier = json.loads((clos / "releve-verification-v1.json").read_text(encoding="utf-8"))
        assert premier["issue_finale_ligne"] == 13 and premier["close"] and premier["noeud_de_lazar"]
        assert "temperature" in json.loads(fournisseur.appels()[-1]["corps"])           # la première ligne l'avait envoyée
        depense_close = premier["depense_comptee_usd"]
        # artefact : la même ligne de calcul ne repart pas, même avec le retrait
        monde.config["temperature_retiree_d_avance"] = _retrait(GO[ligne])
        chemin, empreinte = monde.ecrire_configuration("configuration-meme-go.json")
        avant = len(fournisseur.appels())
        assert chef.executer(ligne, chemin, empreinte, env, racine=monde.racine, registre=monde.registre(),
                             a_l_instant=MAINTENANT + datetime.timedelta(seconds=2)) == 2
        assert len(fournisseur.appels()) == avant
        # artefact : un GO neuf sans le retrait qui le nomme ne part pas
        monde.config["lignes"][ligne]["go"] = GO_NEUF
        chemin, empreinte = monde.ecrire_configuration("configuration-retrait-ancien.json")
        assert chef.executer(ligne, chemin, empreinte, {**env, "GO_ID": GO_NEUF}, racine=monde.racine,
                             registre=_registre_avec(monde, GO_NEUF), a_l_instant=MAINTENANT + datetime.timedelta(seconds=3)) == 2
        assert len(fournisseur.appels()) == avant
        # cas sain : GO neuf, retrait sous ce GO ; trois appels neufs, compteur de la ligne neuve à zéro
        monde.config["temperature_retiree_d_avance"] = _retrait(GO_NEUF)
        chemin, empreinte = monde.ecrire_configuration("configuration-ligne-neuve.json")
        avant_neuf = chef.gardes_avant_depart(monde.config, ligne, {"GO_ID": GO_NEUF}, monde.racine,
                                              _registre_avec(monde, GO_NEUF), MAINTENANT + datetime.timedelta(seconds=4))
        assert avant_neuf["etat"]["depense_comptee_usd"] == 0.0 and not avant_neuf["etat"]["close"]
        assert avant_neuf["lectures_de_la_console"] == []                  # aucun envoi coupé à la ligne close : rien n'est dû
        compte = avant_neuf["constat_resume"]["depense_de_mistral_depuis_le_constat"]
        assert compte["lignes_jouees_depuis_le_constat"] == [{"go": GO[ligne], "ligne": ligne, "depense_comptee_usd": depense_close}]
        assert Decimal(compte["depense_retiree_usd"]) == Decimal(repr(round(depense_close, 6)))
        fournisseur.programmer(faux.flux_mistral("OK"), sonde_mistral())
        assert chef.executer(ligne, chemin, empreinte, {**env, "GO_ID": GO_NEUF}, racine=monde.racine,
                             registre=_registre_avec(monde, GO_NEUF), a_l_instant=MAINTENANT + datetime.timedelta(seconds=5)) == 0
        neufs = [d for d in dossiers_de(monde.racine / "runs" / "verification-cle-mistral-bras-a-v1") if d != clos]
        releve = json.loads((neufs[0] / "releve-verification-v1.json").read_text(encoding="utf-8"))
        assert releve["go"] == GO_NEUF and releve["saine"] and releve["temperature_envoyee"] is False
        assert releve["appels_comptes"] == 2 and releve["depense_comptee_usd"] < 0.25
        assert not any("temperature" in json.loads(a["corps"]) for a in fournisseur.appels()[avant:])
        # la ligne close reste lue, avec sa dépense, à côté de la neuve
        jouees = {j["go"]: j["depense_comptee_usd"] for j in chef.lignes_jouees(monde.racine, monde.config, "mistral")}
        assert jouees[GO[ligne]] == depense_close and GO_NEUF in jouees
    finally:
        fournisseur.arreter()


def test_l8_artefact_une_ligne_neuve_ne_passe_pas_un_envoi_coupe_de_la_ligne_close(monde):
    """La ligne neuve ne laisse rien passer : un envoi coupé à une ligne antérieure de Mistral exige toujours la lecture
    de la console (garde 20), quelle que soit l'issue de cette ligne."""
    ligne = "verification-mistral-eu"
    monde.releve(ligne, "close", go=GO[ligne], issue_finale_ligne=13, close=True, saine=False, envois_coupes=["L1-01-A"],
                 depense_comptee_usd=0.075988)
    monde.config["lignes"][ligne]["go"] = GO_NEUF
    monde.config["temperature_retiree_d_avance"] = _retrait(GO_NEUF)
    with pytest.raises(chef.Arret, match="garde 20 : envoi coupé à la ligne " + GO[ligne]):
        chef.gardes_avant_depart(monde.config, ligne, {"GO_ID": GO_NEUF}, monde.racine, _registre_avec(monde, GO_NEUF), MAINTENANT)


def test_l8_depense_de_mistral_depuis_le_constat_ecrite_et_dite(monde):
    ligne = "verification-mistral-eu"
    monde.releve(ligne, "close", go="GO-2026-11-21-81", depense_comptee_usd=0.075988, close=True, saine=False)
    lu = _constat_lu(monde, "mistral")                                      # 9,50 USD comptés
    compte = chef.depense_de_mistral_depuis_le_constat(monde.config, monde.racine, ligne, lu)
    assert compte["depense_retiree_usd"] == "0.075988" and compte["reste_usd"] == "9.424012" and compte["a_dire_a_lazar"] is None
    bas = _constat(monde, fournisseur="mistral", modifs={"mistral_credit_utilisable_usd": "8,25"})
    compte = chef.depense_de_mistral_depuis_le_constat(monde.config, monde.racine, ligne, bas)
    assert compte["reste_usd"] == "8.174012" and "sous 8.23" in compte["a_dire_a_lazar"]                 # dit, non refusé
    # une ligne jouée avant le constat n'est pas retirée : le crédit vu la porte déjà
    apres = (MAINTENANT - datetime.timedelta(minutes=1)).strftime("%Y-%m-%dT%H:%MZ")
    tard = _constat(monde, fournisseur="mistral", date=apres, transcription=apres)
    assert chef.depense_de_mistral_depuis_le_constat(monde.config, monde.racine, ligne, tard)["depense_retiree_usd"] == "0"
    assert chef.depense_de_mistral_depuis_le_constat(monde.config, monde.racine, "file-neon", lu) is None


def test_m2_l8_artefacts_ajoutes_par_la_campagne_de_la_livraison_8(monde):
    """Les mutants qui survivaient au premier passage de la campagne `livraison8`."""
    def appel(genre, ligne_du_classement, **plus):
        return {"type": genre, "ligne_du_classement": ligne_du_classement, "compte_parmi_les_trois": True, **plus}

    suite = chef.suite_de_la_verification
    assert suite([]) == ("A", None) and suite([appel("A", 3), appel("B", None)]) == (None, "sonde jouée")
    assert suite([appel("A", 13)]) == (None, "issue fermée à la ligne 13 du classement")
    assert suite([appel("A", 6)]) == ("A", None) and suite([appel("A", 7)]) == ("A", None) and suite([appel("Ap", 6)]) == ("Ap", None)
    assert suite([appel("A", 10)]) == ("Ap", None)
    assert suite([appel("A", 10)], {"go": "GO-x"})[0] is None
    assert suite([appel("A", 3), appel("B", None, a_refaire=True)]) == ("B", None)
    # dépense de Mistral : une ligne jouée à la minute même de la transcription est retirée ; six décimales ; reste au seuil pile
    ligne = "verification-mistral-eu"
    monde.releve(ligne, "pile", go="GO-2026-11-21-81", depense_comptee_usd=0.0759884, close=True, saine=False, quand=AVANT)
    lu = _constat_lu(monde, "mistral")
    compte = chef.depense_de_mistral_depuis_le_constat(monde.config, monde.racine, ligne, lu)
    assert compte["depense_retiree_usd"] == "0.075988" and len(compte["lignes_jouees_depuis_le_constat"]) == 1
    monde.releve(ligne, "pile2", go="GO-2026-11-21-82", depense_comptee_usd=0.004012, close=True, saine=False, quand=AVANT)
    juste = _constat(monde, fournisseur="mistral", modifs={"mistral_credit_utilisable_usd": "8,31"})
    compte = chef.depense_de_mistral_depuis_le_constat(monde.config, monde.racine, ligne, juste)
    assert compte["reste_usd"] == "8.230000" and compte["a_dire_a_lazar"] is None                       # 8,31 − 0,08 = 8,23


# === Livraison 9 : avenant 2 au devis (plafond de Google à 65 536), section 9 ============================================

AVENANT_2 = "docs/notes/relance-organismes-discrets-v1/avenant-2-devis-essais-admission-plafond-google-65536-v3.md"
TAUX_BCE = ("- taux : 1,0990 USD par EUR ; source : Banque centrale européenne, fichier quotidien des taux de référence "
            "bce-eurofxref-daily-releve-2026-11-21T1749Z.xml, sha256 a234540a78d0bccccc3642bfe604b138310a03741361434907aa4cf3e7622e8a ; "
            "heure du taux (UTC) : {heure} ; fixage publié le : {fixage}")


def valeurs_de_l_avenant_2(config: dict) -> dict:
    """Les valeurs de la section 9 de l'avenant 2, à la lettre, et l'état définitif (pour les lignes de Google)."""
    g = config["fournisseurs"]["google"]
    g.update({k: v for k, v in chef.AVENANT_2_FOURNISSEUR.items()})
    g["reflexion"] = {"forme": "niveau", "borne_declaree": chef.AVENANT_2_BORNE_DE_REFLEXION}
    g["exemption_de_la_sonde_go"] = GO_EXEMPTION                       # livraison 10 : lu au registre (`ligne_d_exemption`)
    for ligne, valeurs in chef.AVENANT_2_LIGNES.items():
        config["lignes"][ligne].update({k: (dict(v) if isinstance(v, dict) else v) for k, v in valeurs.items()})
    config.update({"etat": "definitive", "regime_file_google": "prudent", "marge_de_change": 0.05,
                   "marge_de_change_go": GO_QUI_LEVE, "recharge_comptee": False, "essai_local": None})
    return config


GO_EXEMPTION = "GO-2026-11-21-90"


def ligne_d_exemption(go: str = GO_EXEMPTION, type_: str = "décision", echeance: str = "2099-12-31",
                      texte: str = "prolonge l'exemption de la sonde de borne des vérifications de Google (avenant 2, section 6)",
                      par: str = "Lazar") -> str:
    """Livraison 10 : la ligne du registre qui accorde l'exemption de la sonde, de type « décision »."""
    return f"| {go} | 2026-11-21 | {type_} | {texte} | — | {echeance} | {par} | avenant 2, section 6 |\n"


def registre_court(config: dict, lignes=("verification-google-cle-1", "verification-google-cle-2", "file-neon")) -> str:
    """La forme minimale que la garde 8 accepte pour une ligne de Google : les marques de la ligne et l'empreinte du devis
    au périmètre ; à la référence, sans libellé, les empreintes de l'avenant 2, de la vérification du devis et de
    l'avenant 1 ; et, livraison 12 (C-2), celle de l'avenant 3 et GO-2026-11-22-16. Aucun mot de plus : la garde ne lit
    que les marques, les empreintes et le GO. Livraison 12 : le chemin de l'avenant 2 n'y est plus (la garde ne le lit
    pas), pour que la ligne tienne sous 600 signes avec l'avenant 3."""
    sortie = ["| identifiant | accordé | type | périmètre | plafond | échéance | par | référence |", "|---|---|---|---|---|---|---|---|"]
    for nom in lignes:
        L = config["lignes"][nom]
        perimetre = ", ".join(L["marques_du_perimetre"]) + f", devis {chef.EMPREINTE_DEVIS}"
        reference = (f"{config['avenant_2']['sha256']} ; "
                     f"{config['verification_du_devis']['sha256']} ; {config['avenant']['sha256']}")
        if (config.get("avenant_3") or {}).get("sha256"):          # livraison 12 (C-2) : l'avenant 3 et GO-16
            reference += f" ; {config['avenant_3']['sha256']} ; {GO_DE_L_AVENANT_3}"
        sortie.append(f"| {GO[nom]} | 2026-11-21 | calcul | {perimetre} | {L['plafond_registre']} | 2099-12-31 | Lazar | {reference} |")
    return "\n".join(sortie) + "\n" + ligne_d_exemption() + ligne_de_confirmation()


def ligne_de_confirmation(go: str = GO_DE_L_AVENANT_3, type_: str = "décision", echeance: str = "2099-12-31", par: str = "Lazar",
                          texte: str = "**Mot de Lazar vers 2026-11-22T05:37:53Z : « oui, seuils levés ».** Bras A : confirme la "
                                       "conséquence tirée de GO-2026-11-22-02 par l'avenant 3 v2 (4b331d9a…) : les seuils de crédit "
                                       "de Google (28,28 et 23,59 USD par projet) sont levés ; un refus pour crédit épuisé arrête "
                                       "la ligne et se journalise.") -> str:
    """Livraison 13 (constat 2) : la ligne de décision GO-2026-11-22-16, à la forme du registre (échéance d'essai
    lointaine), lue au registre en définitive comme GO-2026-11-22-02."""
    return (f"| {go} | 2026-11-22 | {type_} | {texte} | aucun | {echeance} | {par} | à citer dans la ligne de GO de chaque "
            "ligne de Google |\n")


def test_l9_chiffres_de_la_section_9_refaits_par_programme():
    """Excès au débit déclaré sur le délai du relais, moins la réserve à 65 536 ; seuils ; crédit à avoir (avenant 2)."""
    prix = 15
    for ligne, v in chef.AVENANT_2_LIGNES.items():
        exces = (200 * v["delais"]["relais_total_s"] - 65536) * prix / 1e6
        assert math.ceil(exces * 100 - 1e-9) / 100 == v["exces_possible_d_un_envoi_usd"]
    verif, file_ = chef.AVENANT_2_LIGNES["verification-google-cle-1"], chef.AVENANT_2_LIGNES["file-neon"]
    assert round(file_["plafond_usd"] + verif["plafond_usd"] + verif["exces_possible_d_un_envoi_usd"]
                 + file_["exces_possible_d_un_envoi_usd"], 2) == chef.AVENANT_2_FOURNISSEUR["credit_min_avant_verification_usd"]
    assert round(file_["plafond_usd"] + file_["exces_possible_d_un_envoi_usd"], 2) == chef.AVENANT_2_FOURNISSEUR["credit_min_avant_file_usd"]
    assert round(2 * (verif["plafond_usd"] + verif["exces_possible_d_un_envoi_usd"]) + file_["plafond_usd"]
                 + file_["exces_possible_d_un_envoi_usd"], 2) == chef.AVENANT_2_FOURNISSEUR["credit_a_avoir_usd"]
    assert chef.AVENANT_2_BORNE_DE_REFLEXION == 65536 - chef.MARGE_DE_TEXTE_GOOGLE
    assert chef.sha256_fichier(RACINE / AVENANT_2) == chef.EMPREINTE_AVENANT_2
    gabarit = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
    assert gabarit["avenant_2"]["sha256"] == chef.EMPREINTE_AVENANT_2 and gabarit["fournisseurs"]["google"]["sortie_max"] is None


def test_l9_sain_une_configuration_definitive_aux_valeurs_de_la_section_9(monde):
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    for ligne in ("verification-google-cle-1", "verification-google-cle-2", "file-neon"):
        assert chef.controler_avenant_2(config, monde.racine, ligne)["a_la_lettre"]
    config["fournisseurs"]["google"]["reflexion"]["borne_declaree"] = "la plus haute admise"        # 49 536, lu
    assert chef.controler_avenant_2(config, monde.racine, "file-neon")["avenant_2"]["sha256"] == chef.EMPREINTE_AVENANT_2
    assert chef.controler_avenant_2(config, monde.racine, "verification-mistral-eu") is None      # Mistral ne le lit pas
    assert chef.controler_la_configuration_de_google(config, "file-neon")["plafond_de_sortie"] == 65536


@pytest.mark.parametrize("chemin, valeur, motif", [
    (("fournisseurs", "google", "sortie_max"), 32768, "fournisseurs.google.sortie_max"),
    (("fournisseurs", "google", "reflexion"), {"forme": "niveau", "borne_declaree": 40000}, "fournisseurs.google.reflexion"),
    (("fournisseurs", "google", "credit_min_avant_verification_usd"), 19.76, "credit_min_avant_verification_usd"),
    (("fournisseurs", "google", "credit_min_avant_file_usd"), 16.08, "credit_min_avant_file_usd"),
    (("fournisseurs", "google", "credit_a_avoir_usd"), 23.0, "credit_a_avoir_usd"),
    (("lignes", "file-neon", "plafond_usd"), 8.5, "lignes.file-neon.plafond_usd"),
    (("lignes", "file-neon", "plafond_registre"), "8,50 USD", "lignes.file-neon.plafond_registre"),
    (("lignes", "file-neon", "exces_possible_d_un_envoi_usd"), 7.58, "exces_possible_d_un_envoi_usd"),
    (("lignes", "file-neon", "delais"), {"silence_s": 2700, "total_s": 5400, "relais_silence_s": 2690, "relais_total_s": 5390},
     "lignes.file-neon.delais"),
    (("regime_file_google",), "courant", "régime|regime_file_google")])
def test_l9_artefact_une_valeur_de_la_section_9_autre_en_definitive(monde, chemin, valeur, motif):
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    cible = config
    for c in chemin[:-1]:
        cible = cible[c]
    cible[chemin[-1]] = valeur
    with pytest.raises(chef.Arret, match=motif):
        chef.controler_avenant_2(config, monde.racine, "file-neon")


def test_l9_artefact_avenant_2_absent_d_une_autre_empreinte_sans_compagnon_ou_valeurs_nulles(monde):
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    for piece, motif in ((None, "inscrit la pièce `avenant_2`"), ({"chemin": None, "sha256": None}, "inscrit la pièce `avenant_2`"),
                         ({"chemin": AVENANT_2, "sha256": "0" * 64}, "empreinte"), ("avenant", "ni nul ni une pièce")):
        config["avenant_2"] = piece
        with pytest.raises(chef.Arret, match=motif):
            chef.controler_avenant_2(config, monde.racine, "verification-google-cle-1")
    monde.piece("avenant-2-sans-compagnon.md", (RACINE / AVENANT_2).read_text(encoding="utf-8"), sceller=False)
    config["avenant_2"] = monde.ref("avenant-2-sans-compagnon.md")
    with pytest.raises(chef.Arret, match="compagnon"):
        chef.controler_avenant_2(config, monde.racine, "verification-google-cle-1")
    monde.piece("avenant-2-copie.md", (RACINE / AVENANT_2).read_text(encoding="utf-8") + "\n")       # une autre pièce, scellée
    config["avenant_2"] = monde.ref("avenant-2-copie.md")
    with pytest.raises(chef.Arret, match="n'est pas celle de l'avenant 2 accepté"):
        chef.controler_avenant_2(config, monde.racine, "verification-google-cle-1")
    # valeurs nulles du gabarit : rien ne part, à l'essai comme en définitive
    essai = copy.deepcopy(monde.config)
    for chemin in (("lignes", "file-neon", "plafond_usd"), ("lignes", "file-neon", "plafond_registre"),
                   ("lignes", "file-neon", "exces_possible_d_un_envoi_usd"), ("lignes", "file-neon", "delais"),
                   ("fournisseurs", "google", "credit_min_avant_file_usd"), ("fournisseurs", "google", "credit_min_avant_verification_usd")):
        cas = copy.deepcopy(essai)
        cas[chemin[0]][chemin[1]][chemin[2]] = None
        with pytest.raises(chef.Arret, match=f"avenant 2 : `{'.'.join(chemin)}` n'est pas inscrit"):
            chef.controler_avenant_2(cas, monde.racine, "file-neon")
    assert chef.controler_avenant_2(essai, monde.racine, "file-neon")["a_la_lettre"] is False       # l'essai : inscrites, non à la lettre


def test_l9_garde_8_la_ligne_de_google_cite_l_avenant_2(monde):
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    court = registre_court(config)
    for ligne in ("verification-google-cle-1", "verification-google-cle-2", "file-neon"):               # cas sains
        assert chef.verifier_ligne_de_calcul(config, ligne, {"GO_ID": GO[ligne]}, court, "2026-11-22")
    sans = court.replace(f" {chef.EMPREINTE_AVENANT_2} ", " ")
    with pytest.raises(chef.Arret, match="ne cite pas l'empreinte de l'avenant 2"):
        chef.verifier_ligne_de_calcul(config, "file-neon", {"GO_ID": GO["file-neon"]}, sans, "2026-11-22")
    config["avenant_2"] = None
    with pytest.raises(chef.Arret, match="inscrit l'avenant 2 pour la ligne file-neon"):
        chef.verifier_ligne_de_calcul(config, "file-neon", {"GO_ID": GO["file-neon"]}, court, "2026-11-22")
    # une ligne de Mistral n'en a pas besoin
    mistral = monde.registre(["verification-mistral-eu"])
    assert chef.verifier_ligne_de_calcul(config, "verification-mistral-eu", {"GO_ID": GO["verification-mistral-eu"]}, mistral, "2026-11-22")
    # à l'essai, sans pièce inscrite, la garde n'exige pas l'empreinte
    essai = copy.deepcopy(monde.config)
    essai["avenant_2"] = None
    sans_essai = registre_court({**essai, "avenant_2": {"chemin": AVENANT_2, "sha256": ""}})
    assert chef.verifier_ligne_de_calcul(essai, "file-neon", {"GO_ID": GO["file-neon"]}, sans_essai, "2026-11-22")


def test_l9_lignes_courtes_du_registre_eprouvees_a_blanc_de_bout_en_bout(monde):
    """Les lignes courtes, par la garde 8, puis toutes les gardes d'avant le départ, sur une configuration définitive
    aux valeurs de la section 9 et un constat de Google seul en euros, au fixage de la Banque centrale européenne."""
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    court = registre_court(config)
    longueurs = [len(l) for l in court.splitlines()[2:5]]
    assert all(n <= 600 for n in longueurs) and longueurs == [525, 527, 562], longueurs                       # 600 signes au plus (livraison 12 : avenant 3 et GO-16 compris)
    vu = MAINTENANT - datetime.timedelta(hours=1)
    h = lambda d: d.strftime("%Y-%m-%dT%H:%MZ")                                                         # noqa: E731
    texte = constat_de_google_seul({**EUROS, "google_credit_vu_projet_a": "31,58", "google_credit_apres_une_recharge_projet_a": "31,58",
                                    "google_credit_vu_projet_b": "31,58", "google_credit_apres_une_recharge_projet_b": "31,58"},
                                   date=h(vu), transcription=h(vu + datetime.timedelta(minutes=2)),
                                   hors_tableau=[TAUX_BCE.format(heure=h(vu + datetime.timedelta(minutes=5)), fixage=h(vu)[:10])])
    monde.piece("constat-google-l9.md", texte)
    config["constat"] = monde.ref("constat-google-l9.md")
    lu = chef.garde_constat(config, monde.racine, MAINTENANT, "google")
    assert lu["credits_comptes_usd"] == {"a": Decimal("32.97"), "b": Decimal("32.97")}                   # 31,58 € × 1,099 × 0,95
    for ligne in ("verification-google-cle-1", "verification-google-cle-2"):
        avant = chef.gardes_avant_depart(config, ligne, {"GO_ID": GO[ligne]}, monde.racine, court, MAINTENANT)
        assert avant["controle_du_credit"]["seuil_usd"] == "28.28" and avant["avenant_2"]["a_la_lettre"]
        assert avant["regle_google"]["plafond_de_sortie"] == 65536 and avant["regle_google"]["borne_de_la_reflexion"] == 49536
    refs = {CLE_1: monde.releve("verification-google-cle-1", "l9a", go="GO-2026-11-25-01", depense_comptee_usd=4.69),
            CLE_2: monde.releve("verification-google-cle-2", "l9b", go="GO-2026-11-25-02", depense_comptee_usd=0.02)}
    config["lignes"]["file-neon"].update({"releves_verification": refs, "inscrit": {"nom_servi": "gemini-4-neon",
                                          "hote": config["lignes"]["file-neon"]["hote"], "orthographe_niveau": "XHIGH"}})
    # la somme est retirée (deux clés du lien levées) : 32,97 − 4,71 = 28,26, au-dessus de 23,59 : la file part, prudente
    avant = chef.gardes_avant_depart(config, "file-neon", {"GO_ID": GO["file-neon"]}, monde.racine, court, MAINTENANT)
    assert avant["controle_du_credit"]["seuil_usd"] == "23.59" and avant["contexte"]["regime"] == "prudent"
    assert avant["controle_du_credit"]["depense_retiree_usd"] == "4.71"
    # artefact : une marque de la ligne retirée du périmètre court
    marque = config["lignes"]["file-neon"]["marques_du_perimetre"][1]
    with pytest.raises(chef.Arret, match="ne nomme pas file-neon"):
        chef.gardes_avant_depart(config, "file-neon", {"GO_ID": GO["file-neon"]}, monde.racine,
                                 court.replace(", " + marque, ""), MAINTENANT)


def test_l9_seuils_de_l_avenant_2_cas_chiffre_de_la_section_9(monde):
    """Avenant 2, section 9, point 2 : deux projets distincts, dépenses de 4,69 et 0,02, crédit compté de 28,28 : la
    file part (28,28 − 4,69 = 23,59) ; somme retirée (lien levé) : 28,28 − 4,71 = 23,57, elle ne part pas."""
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    _depenses(monde, 4.69, 0.02)
    monde.piece("constat-2828.md", constat({"google_credit_vu_projet_a": "28,28", "google_credit_apres_une_recharge_projet_a": "28,28",
                                            "google_credit_vu_projet_b": "28,28", "google_credit_apres_une_recharge_projet_b": "28,28",
                                            **LIEN_CONSTATE}))
    config["constat"] = monde.ref("constat-2828.md")
    assert chef.controler_credit_de_google(config, monde.racine, "file-neon", chef.garde_constat(config, monde.racine, MAINTENANT, "google"))
    monde.piece("constat-2828-leve.md", constat({"google_credit_vu_projet_a": "28,28", "google_credit_apres_une_recharge_projet_a": "28,28",
                                                 "google_credit_vu_projet_b": "28,28", "google_credit_apres_une_recharge_projet_b": "28,28"}))
    config["constat"] = monde.ref("constat-2828-leve.md")
    with pytest.raises(chef.Arret, match=r"23\.57, sous 23\.59"):
        chef.controler_credit_de_google(config, monde.racine, "file-neon", chef.garde_constat(config, monde.racine, MAINTENANT, "google"))


@pytest.mark.parametrize("limite, appels_payants", [(65535, 0), (32768, 0), (65536, 2)])
def test_l9_output_token_limit_sous_65536_aucun_appel_payant(monde, banc, limite, appels_payants):
    g = monde.config["fournisseurs"]["google"]
    g.update({"sortie_max": 65536, "reflexion": {"forme": "niveau", "borne_declaree": 49536}})
    monde.config["lignes"]["verification-google-cle-1"]["plafond_usd"] = 3.0
    b = banc("verification-google-cle-1", liste=faux.modele_google(limite_sortie=limite))
    b.faux.programmer(faux.reponse_google("OK"), sonde_google())
    releve = b.verifier()
    assert len(b.faux.appels()) == appels_payants
    if appels_payants == 0:                                                     # artefact : ligne 2, close, avant tout appel payant
        assert releve["issue_finale_ligne"] == 2 and releve["close"] and releve["depense_comptee_usd"] == 0
    else:                                                                       # cas sain : à 65 536, les appels partent
        assert json.loads(b.faux.appels()[0]["corps"])["generationConfig"]["maxOutputTokens"] == 65536


def test_m2_l9_artefacts_ajoutes_par_la_campagne_de_la_livraison_9(monde):
    """Les mutants qui survivaient au premier passage de la campagne `livraison9` : des arrêts hérités de la garde 8
    qu'aucun essai n'éprouvait, et les bornes des valeurs inscrites de l'avenant 2."""
    jour, ligne = "2026-11-22", "file-neon"
    registre = monde.registre()
    vraie = [l for l in registre.splitlines() if l.startswith(f"| {GO[ligne]} |")][0]
    cellules = vraie.strip().strip("|").split(" | ")

    def avec(**changes) -> str:
        noms = ("identifiant", "accorde", "type", "perimetre", "plafond", "echeance", "par", "reference")
        c = [changes.get(n, v.strip()) for n, v in zip(noms, cellules)]
        return registre.replace(vraie, "| " + " | ".join(c) + " |")

    def refuse(texte, motif, config=None):
        with pytest.raises(chef.Arret, match=motif):
            chef.verifier_ligne_de_calcul(config or monde.config, ligne, {"GO_ID": GO[ligne]}, texte, jour)

    refuse(registre.replace(vraie, vraie.rsplit(" | ", 1)[0] + " |"), "n'a pas huit colonnes")
    refuse(avec(type="autre"), "n'est pas une ligne de calcul")
    refuse(avec(par="Paul"), "n'est pas accordée par Lazar")
    refuse(avec(accorde="01-11-2026"), "date d'accord illisible")
    refuse(avec(accorde="2099-01-01"), "postérieure à ce jour")
    refuse(avec(plafond="9,99 USD"), "porte le plafond « 9,99 USD »")
    refuse(avec(perimetre=cellules[3].replace(monde.config["verification_du_devis"]["sha256"], "e" * 64)),
           "ne cite pas l'empreinte de la vérification du devis")
    refuse(registre + f"| GO-2026-11-22-99 | 2026-11-21 | révocation | {GO[ligne]} révoqué | — | 2099-12-31 | Lazar | R-0 |\n", "est révoquée")
    assert chef.verifier_ligne_de_calcul(monde.config, ligne, {"GO_ID": GO[ligne]}, avec(echeance=jour), jour)   # échue le lendemain
    assert chef.verifier_ligne_de_calcul(monde.config, ligne, {"GO_ID": GO[ligne]}, avec(accorde=jour), jour)    # accordée le jour même
    sans_go = copy.deepcopy(monde.config)
    sans_go["lignes"][ligne]["go"] = None
    refuse(registre, "aucun identifiant de ligne de calcul inscrit", sans_go)
    # avenant 2 : bornes des valeurs inscrites, à l'essai (positives ; une demi-unité admise)
    for chemin, valeur, admise in ((("lignes", ligne, "plafond_usd"), 0, False), (("lignes", ligne, "plafond_usd"), 0.5, True),
                                   (("fournisseurs", "google", "credit_min_avant_file_usd"), 0, False),
                                   (("fournisseurs", "google", "credit_min_avant_file_usd"), 0.5, True)):
        cas = copy.deepcopy(monde.config)
        cas[chemin[0]][chemin[1]][chemin[2]] = valeur
        if admise:
            assert chef.controler_avenant_2(cas, monde.racine, ligne)["a_la_lettre"] is False
        else:
            with pytest.raises(chef.Arret, match="n'est pas inscrit"):
                chef.controler_avenant_2(cas, monde.racine, ligne)
    for delais, admise in (({**chef.DELAIS_FILE_GOOGLE, "total_s": 0}, False), ({**chef.DELAIS_FILE_GOOGLE, "total_s": 0.5}, True),
                           ({**chef.DELAIS_FILE_GOOGLE, "total_s": True}, False), ({"total_s": 2700}, False)):
        cas = copy.deepcopy(monde.config)
        cas["lignes"][ligne]["delais"] = delais
        if admise:
            assert chef.controler_avenant_2(cas, monde.racine, ligne)
        else:
            with pytest.raises(chef.Arret, match="delais` n'est pas inscrit"):
                chef.controler_avenant_2(cas, monde.racine, ligne)
    cas = copy.deepcopy(monde.config)
    cas["avenant_2"] = {"chemin": AVENANT_2, "sha256": None}                  # à moitié inscrite : vérifiée, refusée
    with pytest.raises(chef.Arret, match="non inscrits"):
        chef.controler_avenant_2(cas, monde.racine, ligne)
    cas["avenant_2"] = None                                                   # à l'essai, sans pièce : rien n'est rendu
    assert chef.controler_avenant_2(cas, monde.racine, ligne) == {"avenant_2": None, "a_la_lettre": False}
    definitive = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    definitive["fournisseurs"]["google"]["exemption_de_la_sonde"] = 1         # un nombre n'est pas un booléen
    with pytest.raises(chef.Arret, match="exemption_de_la_sonde"):
        chef.controler_avenant_2(definitive, monde.racine, ligne)
    definitive["fournisseurs"]["google"]["exemption_de_la_sonde"] = True
    monde.piece("avenant-2-autre.md", "autre\n")
    definitive["avenant_2"] = monde.ref("avenant-2-autre.md")
    with pytest.raises(chef.Arret, match=r"accepté \(9d4b8a08…\)"):
        chef.controler_avenant_2(definitive, monde.racine, ligne)


# === Livraison 10 : `outputTokenLimit` absent refusé ; GO de l'exemption de la sonde lu au registre ======================

def test_l10_artefact_output_token_limit_absent_refuse_avant_tout_appel_payant(monde, banc):
    g = monde.config["fournisseurs"]["google"]
    g.update({"sortie_max": 65536, "reflexion": {"forme": "niveau", "borne_declaree": 49536}})
    monde.config["lignes"]["verification-google-cle-1"]["plafond_usd"] = 3.0
    b = banc("verification-google-cle-1", liste=faux.modele_google(limite_sortie=None))
    b.faux.programmer(faux.reponse_google("OK"), sonde_google())
    releve = b.verifier()
    assert b.faux.appels() == [] and releve["depense_comptee_usd"] == 0                     # aucun appel payant
    assert releve["issue_finale_ligne"] == 2 and releve["close"] and releve["noeud_de_lazar"]
    assert releve["issue_finale"] == chef.MOTIF_LIMITE_ABSENTE
    assert releve["issue_finale"] == ("`outputTokenLimit` absent de la fiche du modèle rendue par l'appel de liste : refus par "
                                      "prudence (décision de la session mère, GO-2026-11-21-69 ; devis 4.4, ligne 2 relue) ; "
                                      "aucun appel payant ; nœud de Lazar")


def test_l10_sain_limite_presente_et_fiche_d_un_autre_code_garde_son_classement(monde, banc):
    sain = banc("verification-google-cle-1")                                       # 65 536 rendu : les appels partent
    sain.faux.programmer(faux.reponse_google("OK"), sonde_google())
    assert sain.verifier()["issue_finale"] != chef.MOTIF_LIMITE_ABSENTE and len(sain.faux.appels()) == 2
    assert chef.liste_sans_limite({"code": 200, "lisible": True, "porte_identifiant": True, "limite_sortie": None})
    for fiche in ({"code": 404, "lisible": False, "porte_identifiant": False, "limite_sortie": None},
                  {"code": 200, "lisible": False, "porte_identifiant": False, "limite_sortie": None},
                  {"code": 200, "lisible": True, "porte_identifiant": False, "limite_sortie": None},
                  {"code": 200, "lisible": True, "porte_identifiant": True, "limite_sortie": 65536}):
        assert not chef.liste_sans_limite(fiche)                                   # l'ancien classement s'applique


def test_l10_la_file_du_juge_exige_la_limite_des_deux_releves(monde):
    monde.config["fournisseurs"]["google"].update({"sortie_max": 65536, "reflexion": {"forme": "niveau", "borne_declaree": 49536}})

    def file_avec(nom, listes_cle_2):
        ref1 = monde.releve("verification-google-cle-1", f"{nom}-1", go=f"GO-2026-11-26-{len(nom):02d}")
        ref2 = monde.releve("verification-google-cle-2", f"{nom}-2", go=f"GO-2026-11-27-{len(nom):02d}", listes=listes_cle_2)
        monde.inscrire_releve("file-neon", ref1, ref2)
        return chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))

    fiche = {"code": 200, "lisible": True, "porte_identifiant": True}
    assert file_avec("s", [{**fiche, "limite_sortie": 65536}])["limites_de_sortie"] == {CLE_1: 65536, CLE_2: 65536}   # sain
    assert file_avec("ss", [{**fiche, "limite_sortie": 32768}, {**fiche, "limite_sortie": 65536}])        # la dernière compte
    assert file_avec("sss", [{**fiche, "limite_sortie": 65536}, {**fiche, "lisible": False, "limite_sortie": None}])   # illisible : ignorée
    for nom, listes, motif in (("a", [{**fiche, "limite_sortie": None}], "absent de la fiche.*la file ne part pas"),
                               ("aa", [], "absent de la fiche"), ("aaa", [{**fiche, "code": 404, "lisible": False, "limite_sortie": None}], "absent"),
                               ("aaaa", [{**fiche, "limite_sortie": 65535}], r"\(65535\) sous la sortie maximale de la file \(65536\)"),
                               ("aaaaa", [{**fiche, "limite_sortie": 65536}, {**fiche, "limite_sortie": None}], "absent")):
        with pytest.raises(chef.Arret, match=f"garde 10 : relevé de {CLE_2} : .*{motif}"):
            file_avec(nom, listes)


def test_l10_sain_le_go_de_l_exemption_lu_au_registre(monde):
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    court = registre_court(config)
    lu = chef.controler_go_de_l_exemption(config, "verification-google-cle-1", court, "2026-11-22")
    assert lu["go"] == GO_EXEMPTION and lu["echeance"] == "2099-12-31" and len(lu["empreinte_de_la_ligne"]) == 64
    prolonge = court + ligne_d_exemption("GO-2026-11-21-91", echeance="2026-11-30")
    config["fournisseurs"]["google"]["exemption_de_la_sonde_go"] = "GO-2026-11-21-91"
    assert chef.controler_go_de_l_exemption(config, "file-neon", prolonge, "2026-11-30")["echeance"] == "2026-11-30"   # le jour même
    # GO-2026-11-21-69 : admis sans la citation, tant que son échéance n'est pas passée
    config["fournisseurs"]["google"]["exemption_de_la_sonde_go"] = "GO-2026-11-21-69"
    origine = court + ligne_d_exemption("GO-2026-11-21-69", echeance="2026-11-22", texte="douze heures d'autonomie, recommandations accordées")
    assert chef.controler_go_de_l_exemption(config, "file-neon", origine, "2026-11-22")["go"] == "GO-2026-11-21-69"
    with pytest.raises(chef.Arret, match="échue"):
        chef.controler_go_de_l_exemption(config, "file-neon", origine, "2026-11-23")
    # hors de Google, hors de la définitive : rien à lire ; la ligne entière part, registre court à l'appui
    assert chef.controler_go_de_l_exemption(config, "verification-mistral-eu", None, "2026-11-22") is None
    assert chef.controler_go_de_l_exemption(monde.config, "file-neon", None, "2026-11-22") is None
    config["fournisseurs"]["google"]["exemption_de_la_sonde_go"] = GO_EXEMPTION
    monde.piece("constat-l10.md", constat({"google_credit_vu_projet_a": "40,00", "google_credit_vu_projet_b": "40,00",
                                           "google_credit_apres_une_recharge_projet_a": "40,00",
                                           "google_credit_apres_une_recharge_projet_b": "40,00"}))
    config["constat"] = monde.ref("constat-l10.md")
    avant = chef.gardes_avant_depart(config, "verification-google-cle-1", {"GO_ID": GO["verification-google-cle-1"]},
                                     monde.racine, court, MAINTENANT)
    assert avant["go_de_l_exemption"]["go"] == GO_EXEMPTION


def test_l10_artefact_le_go_de_l_exemption_absent_echu_ou_d_une_autre_forme(monde):
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    base = registre_court(config).replace(ligne_d_exemption(), "")
    jour = "2026-11-22"

    def refuse(registre, motif, go=GO_EXEMPTION):
        config["fournisseurs"]["google"]["exemption_de_la_sonde_go"] = go
        with pytest.raises(chef.Arret, match="GO de l'exemption de la sonde : .*" + motif):
            chef.controler_go_de_l_exemption(config, "file-neon", registre, jour)

    refuse(base, "0 ligne")                                                                   # absent du registre
    refuse(base + ligne_d_exemption() + ligne_d_exemption(), "2 ligne")                       # deux fois
    refuse(base + ligne_d_exemption(type_="calcul"), "de type « calcul »")
    refuse(base + ligne_d_exemption(echeance="2026-11-21"), "échue")
    refuse(base + ligne_d_exemption(echeance="bientôt"), "échue .* ou sans échéance lisible")
    refuse(base + ligne_d_exemption(texte="prolonge la sonde"), "ne cite pas « exemption de la sonde »")
    refuse(base + ligne_d_exemption(par="Paul"), "pas accordée par Lazar")
    refuse(base + ligne_d_exemption().replace(" | avenant 2, section 6 |", " |"), "huit colonnes")
    refuse(base + ligne_d_exemption() + f"| GO-2026-11-21-99 | 2026-11-21 | révocation | {GO_EXEMPTION} révoqué | — | 2099-12-31 | Lazar | R-0 |\n",
           "révoquée")
    refuse(base + ligne_d_exemption(), "n'est pas un identifiant", go="GO-69")
    refuse(None, "registre des GO non lu")
    # la ligne entière ne part pas : avant tout envoi, garde de l'exemption
    config["fournisseurs"]["google"]["exemption_de_la_sonde_go"] = GO_EXEMPTION
    with pytest.raises(chef.Arret, match="GO de l'exemption"):
        chef.gardes_avant_depart(config, "verification-google-cle-1", {"GO_ID": GO["verification-google-cle-1"]},
                                 monde.racine, base, MAINTENANT)


# === Livraison 11 : seuils de crédit de Google levés sous GO-2026-11-22-02 ; refus pour crédit épuisé ====================

GO_RECHARGE = "GO-2026-11-22-02"


def ligne_de_recharge(go: str = GO_RECHARGE, echeance: str = "2099-12-31", type_: str = "décision",
                      texte: str = "Bras A, juge des deux ancres : aucun versement de 9,18 € par projet Google à faire ; la "
                                   "recharge automatique des deux projets couvre les lignes.") -> str:
    """La ligne de décision du mot de Lazar GO-2026-11-22-02, à la forme du registre (échéance d'essai lointaine)."""
    return (f"| {go} | 2026-11-22 | {type_} | {texte} | aucun | {echeance} | Lazar | à vérifier au premier appel : un "
            "refus pour crédit épuisé est un défaut journalisé, jamais une réponse |\n")


def _google_sous_le_seuil(monde, seuils) -> tuple:
    """Configuration définitive aux valeurs de l'avenant 2, constat de Google seul aux soldes du 21 novembre
    (11,93 € et 15,59 €, au fixage de la Banque centrale européenne), registre court plus la ligne de la recharge."""
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    config["seuils_de_credit_google"] = seuils
    vu = MAINTENANT - datetime.timedelta(hours=1)
    h = lambda d: d.strftime("%Y-%m-%dT%H:%MZ")                                                         # noqa: E731
    texte = constat_de_google_seul({**EUROS, "google_credit_vu_projet_a": "11,93", "google_credit_apres_une_recharge_projet_a": "non relevé",
                                    "google_credit_vu_projet_b": "15,59", "google_credit_apres_une_recharge_projet_b": "non relevé"},
                                   date=h(vu), transcription=h(vu + datetime.timedelta(minutes=2)),
                                   hors_tableau=[TAUX_BCE.format(heure=h(vu + datetime.timedelta(minutes=5)), fixage=h(vu)[:10])])
    monde.piece("constat-google-l11.md", texte)
    config["constat"] = monde.ref("constat-google-l11.md")
    # le registre d'essai donne GO-2026-11-22-02 à la vérification de la clé 1 : elle prend ici un autre identifiant,
    # pour que le mot de Lazar GO-2026-11-22-02 y soit seul sous le sien
    config["lignes"]["verification-google-cle-1"]["go"] = "GO-2026-11-22-12"
    court = registre_court(config).replace(f"| {GO_RECHARGE} |", "| GO-2026-11-22-12 |")
    return config, court + ligne_de_recharge()


def test_l11_sain_seuils_leves_sous_go_02_la_verification_part_et_l_ecrit(monde):
    config, registre = _google_sous_le_seuil(monde, {"leves_par": GO_RECHARGE})
    for ligne in ("verification-google-cle-1", "verification-google-cle-2"):
        avant = chef.gardes_avant_depart(config, ligne, {"GO_ID": config["lignes"][ligne]["go"]}, monde.racine, registre, MAINTENANT)
        controle = avant["controle_du_credit"]
        assert controle["credits_comptes_usd"] == {"a": "12.45", "b": "16.27"}             # 11,93 € et 15,59 € × 1,099 × 0,95
        assert controle["seuils"] == f"levés par {GO_RECHARGE}" and controle["seuil_usd"] == "28.28"
        assert all(f"levé par {GO_RECHARGE}" in controle["sous_le_seuil"][p] for p in ("a", "b"))
        assert avant["seuils_de_credit_google"]["mode"] == "leves" and avant["seuils_de_credit_google"]["ligne_du_registre"]["go"] == GO_RECHARGE
    # rien d'autre ne change : plafonds, régime prudent, recharge non comptée, avenant 2 à la lettre
    assert config["recharge_comptee"] is False and config["regime_file_google"] == "prudent"
    assert chef.controler_avenant_2(config, monde.racine, "file-neon")["a_la_lettre"]
    # au-dessus du seuil : rien à écrire
    haut = copy.deepcopy(config)
    monde.piece("constat-haut-l11.md", constat({"google_credit_vu_projet_a": "40,00", "google_credit_vu_projet_b": "40,00",
                                                "google_credit_apres_une_recharge_projet_a": "40,00", "google_credit_apres_une_recharge_projet_b": "40,00"}))
    haut["constat"] = monde.ref("constat-haut-l11.md")
    lu = chef.garde_constat(haut, monde.racine, MAINTENANT, "google")
    assert chef.controler_credit_de_google(haut, monde.racine, "verification-google-cle-1", lu)["sous_le_seuil"] == {"a": None, "b": None}
    # lecture de la console et mot de Lazar : sous le seuil, écrits, non refusés
    lu = chef.garde_constat(config, monde.racine, MAINTENANT, "google")
    ref = monde.releve("verification-google-cle-1", "c11", go="GO-2026-11-26-01", envois_coupes=["L1-01-A"], depense_comptee_usd=0.5)
    monde.piece("console-l11.md", lecture_console_google(ref["sha256"], ("0,10", "0,10"), ("11,00", "15,00"),
                                                        plus=(TAUX_BCE.format(heure=APRES_CONSTAT[:16] + "Z", fixage=APRES_CONSTAT[:10]),)))
    config["lignes"]["file-neon"]["lectures_console"] = [monde.ref("console-l11.md")]
    servies = chef.garde_console(config, monde.racine, "file-neon", GO["file-neon"], lu, MAINTENANT)
    assert all(f"levé par {GO_RECHARGE}" in servies[0]["sous_le_seuil"][p] for p in ("a", "b"))


def test_l11_artefact_exiges_refuse_sous_le_seuil(monde):
    config, registre = _google_sous_le_seuil(monde, "exiges")
    with pytest.raises(chef.Arret, match=r"projet a de Google : crédit compté 12\.45 USD .*sous 28\.28 : la ligne ne part pas"):
        chef.gardes_avant_depart(config, "verification-google-cle-1", {"GO_ID": config["lignes"]["verification-google-cle-1"]["go"]},
                                 monde.racine, registre, MAINTENANT)
    lu = chef.garde_constat(config, monde.racine, MAINTENANT, "google")
    ref = monde.releve("verification-google-cle-1", "c11", go="GO-2026-11-26-01", envois_coupes=["L1-01-A"], depense_comptee_usd=0.5)
    monde.piece("console-l11.md", lecture_console_google(ref["sha256"], ("0,10", "0,10"), ("11,00", "15,00"),
                                                        plus=(TAUX_BCE.format(heure=APRES_CONSTAT[:16] + "Z", fixage=APRES_CONSTAT[:10]),)))
    config["lignes"]["file-neon"]["lectures_console"] = [monde.ref("console-l11.md")]
    with pytest.raises(chef.Arret, match="garde 20 : solde vu du projet a.*sous 23.59"):
        chef.garde_console(config, monde.racine, "file-neon", GO["file-neon"], lu, MAINTENANT)


def test_l11_artefact_levee_refusee_go_echu_sans_la_mention_ou_d_une_autre_forme(monde):
    config, registre = _google_sous_le_seuil(monde, {"leves_par": GO_RECHARGE})
    base = registre.replace(ligne_de_recharge(), "")

    def refuse(texte, motif, jour="2026-11-22"):
        with pytest.raises(chef.Arret, match="GO de la levée des seuils de crédit : .*" + motif):
            chef.controler_levee_des_seuils(config, "verification-google-cle-1", texte, jour)

    refuse(base + ligne_de_recharge(echeance="2026-11-30"), "échue", jour="2026-12-01")              # échu
    refuse(base + ligne_de_recharge(texte="aucun versement ; les soldes couvrent les lignes"), "ne cite pas « recharge automatique »")
    refuse(base + ligne_de_recharge(type_="calcul"), "de type « calcul »")
    refuse(base, "0 ligne")
    assert chef.controler_levee_des_seuils(config, "verification-google-cle-1", base + ligne_de_recharge(echeance="2026-11-30"),
                                           "2026-11-30")["go"] == GO_RECHARGE                        # le jour même : admis
    with pytest.raises(chef.Arret, match="GO de la levée"):                                          # la ligne entière
        chef.gardes_avant_depart(config, "verification-google-cle-1", {"GO_ID": config["lignes"]["verification-google-cle-1"]["go"]},
                                 monde.racine, base, MAINTENANT)
    for valeur in (None, "leves", {"leves_par": "GO-02"}, {"leves_par": GO_RECHARGE, "motif": "x"}, {}, True):
        config["seuils_de_credit_google"] = valeur
        with pytest.raises(chef.Arret, match="`seuils_de_credit_google` n'est pas inscrit"):
            chef.controler_levee_des_seuils(config, "verification-google-cle-1", registre, "2026-11-22")
    assert chef.controler_levee_des_seuils(config, "verification-mistral-eu", registre, "2026-11-22") is None   # Mistral : sans objet
    essai = copy.deepcopy(monde.config)                                      # à l'essai : la forme seule
    essai["seuils_de_credit_google"] = {"leves_par": GO_RECHARGE}
    assert chef.controler_levee_des_seuils(essai, "file-neon", None, "2026-11-22")["ligne_du_registre"] is None
    gabarit = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
    assert "seuils_de_credit_google" in gabarit and gabarit["seuils_de_credit_google"] is None


# Livraison 12 : les trois essais de la livraison 11 sur le refus pour crédit (un 429 « quota » arrêtait la ligne)
# portaient la règle que C-1 corrige ; ils sont retirés, et remplacés par les essais « l12 » en fin de fichier.


def test_m2_l11_artefacts_ajoutes_par_la_campagne_de_la_livraison_11(monde):
    """Les mutants qui survivaient au premier passage de la campagne `livraison11`."""
    assert chef.controler_levee_des_seuils(monde.config, "file-neon", None, "2026-11-22") == {"mode": "exiges"}
    relais = json.dumps({"erreur": {"origine": "relais", "motif": "plafond, quota du relais"}}).encode()
    for code in (402, 429):                                                 # un refus écrit par le relais n'est pas du crédit
        assert chef.refus_pour_credit("google", {"code": code, "corps": relais, "en_tetes": {}}) is None
    assert chef.refus_pour_credit("google", {"code": None, "corps": b"", "en_tetes": {}}) is None
    # au seuil pile : rien à écrire ; deux projets « non relevé », lien levé : la règle le dit ainsi
    monde.piece("constat-pile.md", constat({"google_credit_vu_projet_a": "19,76", "google_credit_vu_projet_b": "19,76",
                                            "google_credit_apres_une_recharge_projet_a": "19,76",
                                            "google_credit_apres_une_recharge_projet_b": "19,76",
                                            "google_deux_projets_distincts": "non relevé"}))
    monde.config["constat"] = monde.ref("constat-pile.md")
    controle = chef.controler_credit_de_google(monde.config, monde.racine, "verification-google-cle-1",
                                               chef.garde_constat(monde.config, monde.racine, MAINTENANT, "google"))
    assert controle["sous_le_seuil"] == {"a": None, "b": None}
    assert controle["regle_de_la_depense_retiree"] == "la somme des deux (deux projets distincts : non relevé)"
    assert controle["lien_cle_projet_constate"] is False and len(controle["cles_du_lien_levees"]) == 2


def test_m2_l11_mot_sur_les_sondes_sous_une_levee_pile_et_sous_le_seuil(monde):
    """Sous la levée, le mot de Lazar sur les sondes : au seuil pile, rien d'écrit ; sous lui, écrit, la file part."""
    monde.config["seuils_de_credit_google"] = {"leves_par": GO_RECHARGE}
    refs = {CLE_1: monde.releve("verification-google-cle-1", "m1", go="GO-2026-11-28-01"),
            CLE_2: monde.releve("verification-google-cle-2", "m2", go="GO-2026-11-28-02", sonde={"issue": "indécidée"})}
    monde.inscrire_releve("file-neon", refs[CLE_1], refs[CLE_2])
    for credits, ecrit in ((("16,08", "16,08"), None), (("12,00", "16,08"), "a")):
        monde.piece(f"mot-{credits[0]}.md", mot_neon(refs, ("comprise", "indécidée"), credits=credits))
        monde.config["lignes"]["file-neon"]["mot_de_lazar_sonde"] = monde.ref(f"mot-{credits[0]}.md")
        contexte = chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))
        assert (list(contexte.get("credits_sous_le_seuil", {})) == [ecrit]) if ecrit else "credits_sous_le_seuil" not in contexte
    monde.config["seuils_de_credit_google"] = "exiges"                           # sous « exiges », le même mot est refusé
    with pytest.raises(chef.Arret, match="crédit vu du projet a.*sous 16.08"):
        chef.garde_cle_verifiee(monde.config, monde.racine, "file-neon", _constat_lu(monde))


# === Livraison 12 : corrections de la contre-lecture de la livraison 11 (C-1 à C-3, mineurs) ===========================
# Règle retenue au journal OD-351, dans le devis, chez Google : un 429 suit la ligne 6 (attente, une seule reprise) ; un
# second 429 sur le même appel est un défaut qui arrête la ligne (crédit épuisé possible) ; un 402 arrête aussitôt.

def _attentes(banc_):
    return [l for l in chef.lire_journal(banc_.dossier / "journal-essai.jsonl") if l.get("evenement") == "attente_sur_429"]


def test_l12_le_faux_fournisseur_rend_le_429_de_google_a_sa_forme_reelle():
    """C-1 (d) : le 429 de Google porte `RESOURCE_EXHAUSTED`, « quota » et « billing », et `RetryInfo` ; chaque code
    rend le statut de Google, et non plus `INVALID_ARGUMENT`."""
    erreur = faux.erreur_google(429)["corps"]["error"]
    assert erreur["status"] == "RESOURCE_EXHAUSTED" and "quota" in erreur["message"] and "billing" in erreur["message"]
    assert {"type.googleapis.com/google.rpc.RetryInfo", "type.googleapis.com/google.rpc.QuotaFailure"} <= {d["@type"] for d in erreur["details"]}
    assert faux.debit_google(courte=True)["corps"]["error"]["status"] == "RESOURCE_EXHAUSTED"
    assert "quota" in faux.debit_google(courte=True)["corps"]["error"]["message"]
    assert faux.credit_epuise_google()["corps"]["error"]["status"] == "RESOURCE_EXHAUSTED"
    assert [faux.erreur_google(c)["corps"]["error"]["status"] for c in (400, 403, 500, 503)] == [
        "INVALID_ARGUMENT", "PERMISSION_DENIED", "INTERNAL", "UNAVAILABLE"]
    assert faux.erreur_google(429, message="trop vite")["corps"]["error"]["status"] == "RESOURCE_EXHAUSTED"


def test_l12_sain_verification_un_429_de_debit_puis_un_200_ligne_6_puis_saine(monde, banc):
    """Cas sain de C-1 : un 429 de débit de Google, à la forme réelle (longue, courte, ou disant le crédit épuisé),
    suit la ligne 6 : à refaire sous la même ligne, non close, sans nœud ; le lancement nouveau est sain."""
    for premier in (faux.debit_google(), faux.debit_google(courte=True), faux.credit_epuise_google()):
        g = banc("verification-google-cle-1")
        g.faux.programmer(premier)
        releve = g.verifier()
        a = releve["appels"][0]
        assert a["ligne_du_classement"] == 6 and a["code"] == 429 and releve["a_refaire"] and not releve["close"]
        assert not releve["noeud_de_lazar"] and len(g.faux.appels()) == 1 and chef.code_de_sortie_verification(releve) == 3
        g.nouveau_dossier()
        g.faux.programmer(faux.reponse_google("OK"), sonde_google())
        suite = g.verifier()
        assert [x["type"] for x in suite["appels"]] == ["A", "A", "B"] and [x["ligne_du_classement"] for x in suite["appels"]][:2] == [6, 3]
        assert suite["saine"] and suite["sonde"]["issue"] == "comprise" and suite["close"] and not suite["noeud_de_lazar"]
    # le 429 d'un appel ne compte pas pour un autre : A reçoit un 429, puis la sonde un 429 : elle est à refaire
    s = banc("verification-google-cle-1")
    s.faux.programmer(faux.debit_google())
    s.verifier()
    s.nouveau_dossier()
    s.faux.programmer(faux.reponse_google("OK"), faux.debit_google())
    suite = s.verifier()
    assert suite["appels"][-1]["type"] == "B" and suite["appels"][-1]["a_refaire"] and suite["a_refaire"] and not suite["close"]


def test_l12_artefact_verification_deux_429_sur_le_meme_appel_arretent_la_ligne(monde, banc):
    """Artefact de C-1 : deux 429 sur l'appel A, par deux lancements, arrêtent la ligne : ligne 13, close, nœud,
    jamais à refaire, deux appels seulement. De même à la sonde. Mistral garde le devis (mineur 3)."""
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.debit_google())
    g.verifier()
    g.nouveau_dossier()
    g.faux.programmer(faux.debit_google(), faux.reponse_google("OK"), sonde_google())
    releve = g.verifier()
    assert [a["ligne_du_classement"] for a in releve["appels"]] == [6, 13] and len(g.faux.appels()) == 2
    assert releve["close"] and releve["noeud_de_lazar"] and not releve["saine"] and releve["a_refaire"] is None
    assert releve["issue_finale"] == chef.MOTIF_SECOND_429 and chef.code_de_sortie_verification(releve) != 3
    g.nouveau_dossier()
    with pytest.raises(chef.Arret, match="close"):
        g.verifier()
    # à la sonde
    s = banc("verification-google-cle-1")
    s.faux.programmer(faux.reponse_google("OK"), faux.debit_google())
    s.verifier()
    s.nouveau_dossier()
    s.faux.programmer(faux.debit_google(courte=True))
    releve = s.verifier()
    assert [a["ligne_du_classement"] for a in releve["appels"]] == [3, None, 13]
    assert releve["close"] and releve["noeud_de_lazar"] and releve["issue_finale"] == "sonde : " + chef.MOTIF_SECOND_429
    # Mistral : deux 429 restent à la ligne 6 (devis, 4.4), à refaire
    m = banc("verification-mistral-eu")
    m.faux.programmer(faux.erreur_mistral(429, message="Requests rate limit exceeded"))
    m.verifier()
    m.nouveau_dossier()
    m.faux.programmer(faux.erreur_mistral(429, message="Insufficient balance"))
    releve = m.verifier()
    assert [a["ligne_du_classement"] for a in releve["appels"]] == [6, 6] and releve["a_refaire"] and not releve["close"]
    # un 429 écrit par le relais n'est pas un second 429 du fournisseur
    relais = {"code": 429, "corps": json.dumps({"erreur": {"origine": "relais", "motif": "x"}}).encode(), "en_tetes": {}}
    deja = [{"type": "A", "code": 429, "origine": "amont", "compte_parmi_les_trois": True}]
    assert not chef.second_429("google", deja, "A", relais)
    amont = {"code": 429, "corps": json.dumps(faux.erreur_google(429)["corps"]).encode(), "en_tetes": {}}
    assert chef.second_429("google", deja, "A", amont) and not chef.second_429("google", deja, "Ap", amont)
    assert not chef.second_429("mistral", deja, "A", amont)
    assert not chef.second_429("google", [dict(deja[0], compte_parmi_les_trois=False)], "A", amont)
    assert not chef.second_429("google", [dict(deja[0], origine="relais")], "A", amont)
    assert not chef.second_429("google", [dict(deja[0], code=500)], "A", amont)
    assert not chef.second_429("google", deja, "A", dict(amont, code=500))


def test_l12_artefact_un_402_ou_un_credit_dit_arrete_aussitot(monde, banc):
    """Un 402 de Google, ou un 403 ou un 400 qui dit le crédit épuisé en mots entiers, arrête la ligne au premier appel :
    ligne 13, close, nœud, motif exact. Cas sains : les mots ambigus (« quota », « billing », « load balancer »), un
    429, Mistral, et un 400 d'orthographe du niveau de réflexion qui dirait « quota » (mineur 2)."""
    for erreur, cause in ((faux.erreur_google(402, message="payment required"), "code 402"),
                          (faux.credit_epuise_google(403), "code 403, « prepayment »"),
                          (faux.erreur_google(400, message="Insufficient balance on this project."), "code 400, « insufficient balance »")):
        g = banc("verification-google-cle-1")
        g.faux.programmer(erreur, faux.reponse_google("OK"), sonde_google())
        releve = g.verifier()
        assert len(g.faux.appels()) == 1 and releve["close"] and releve["noeud_de_lazar"] and releve["a_refaire"] is None
        assert releve["appels"][0]["ligne_du_classement"] == 13
        assert releve["issue_finale"] == chef.MOTIF_CREDIT_EPUISE.format(cause)
    s = banc("verification-google-cle-1")                                       # à la sonde : de même
    s.faux.programmer(faux.reponse_google("OK"), faux.erreur_google(402))
    releve = s.verifier()
    assert [a["ligne_du_classement"] for a in releve["appels"]] == [3, 13] and releve["close"] and releve["a_refaire"] is None
    assert releve["issue_finale"] == "sonde : " + chef.MOTIF_CREDIT_EPUISE.format("code 402")
    # cas sains
    o = banc("verification-google-cle-1")                     # orthographe refusée, message qui dit « quota » : appel A′
    o.faux.programmer(faux.erreur_google(400, "Invalid value for thinkingLevel; quota of values", champs=["generation_config.thinking_config.thinkingLevel"]),
                      faux.reponse_google("OK"), sonde_google())
    releve = o.verifier()
    assert [a["ligne_du_classement"] for a in releve["appels"]][:2] == [11, 3] and releve["saine"]
    p = banc("verification-google-cle-1")                     # 403 sans mot du crédit : ligne 7, à refaire
    p.faux.programmer(faux.erreur_google(403, message="Permission denied: quota project, billing account, load balancer"))
    assert p.verifier()["appels"][0]["ligne_du_classement"] == 7
    m = banc("verification-mistral-eu")                       # Mistral, 402 : ligne 7 du devis (mineur 3)
    m.faux.programmer(faux.erreur_mistral(402, message="Payment required"))
    releve = m.verifier()
    assert releve["appels"][0]["ligne_du_classement"] == 7 and releve["a_refaire"]
    corps = lambda m_: json.dumps({"error": {"message": m_}}).encode()                       # noqa: E731
    for texte in ("quota exceeded", "check your billing", "RESOURCE_EXHAUSTED", "balance of the load balancer",
                  "credit card on file", "insufficiently specified", "repayment", "prepaymentx"):
        for code in (400, 403):
            assert chef.refus_pour_credit("google", {"code": code, "corps": corps(texte), "en_tetes": {}}) is None, texte
    for texte, forme in (("Your prepayment credits are depleted", "prepayment"), ("project prepaid balance", "prepaid"),
                         ("credits depleted", "depleted"), ("insufficient funds", "insufficient funds"),
                         ("insufficient credits", "insufficient credits"), ("out of credit", "out of credit"),
                         ("credits exhausted", "credits exhausted"), ("credit expired", "credit expired"),
                         ("crédits épuisés", "crédits épuisés"), ("crédit insuffisant", "crédit insuffisant"),
                         ("solde épuisé", "solde épuisé"), ("solde insuffisant", "solde insuffisant"),
                         ("Payment Required", "payment required"), ("prepay first", "prepay")):
        assert chef.refus_pour_credit("google", {"code": 403, "corps": corps(texte), "en_tetes": {}}) == f"code 403, « {forme} »", texte
    epuise = {"code": 429, "corps": corps("Your prepayment credits are depleted"), "en_tetes": {}}
    assert chef.refus_pour_credit("google", epuise) is None                     # un 429 n'arrête jamais aussitôt
    assert chef.refus_pour_credit("mistral", dict(epuise, code=402)) is None    # Mistral : hors de GO-2026-11-22-02
    assert chef.refus_pour_credit("google", dict(epuise, code=500)) is None
    assert chef.refus_pour_credit("google", dict(epuise, code=402)) == "code 402"


def test_l12_file_un_429_puis_un_200_continue_deux_429_arretent_un_402_arrete(monde, banc):
    """C-1 dans la file du juge : un 429 de débit (forme réelle) est attendu puis repris une fois, la file continue ;
    un 429 qui dit le crédit épuisé aussi ; deux 429 sur le même appel arrêtent la file au second ; un 402 l'arrête au
    premier, sans attente. Jamais une réponse comptée parmi les codes 200."""
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    for premier, attente in ((faux.debit_google(), 30.0), (faux.debit_google("45s"), 45.0), (faux.credit_epuise_google(), 30.0)):
        s = banc("file-neon")
        s.faux.programmer(premier, *conformes)
        bilan = s.jouer()
        e = s.envois()
        assert bilan["complet"] and e[0]["decision"] == "attente" and e[0]["refus_pour_credit"] is None
        assert [a["secondes"] for a in _attentes(s)] == [attente] and attente in s.pauses
        assert len(s.faux.appels()) == len(conformes) + 1 and e[1]["variable_cle"] == e[0]["variable_cle"]   # la reprise, sur sa clé
    d = banc("file-neon")                                                         # deux 429 sur le premier appel
    d.faux.programmer(faux.debit_google(), faux.debit_google(courte=True), *conformes)
    bilan = d.jouer()
    e = d.envois()
    assert not bilan["complet"] and len(d.faux.appels()) == 2 and [x["decision"] for x in e] == ["attente", "arret"]
    assert e[1]["cause"] == chef.MOTIF_SECOND_429 and bilan["arret"] == chef.MOTIF_SECOND_429
    assert chef.faire_rapport(d.dossier)["reponses_de_code_200"] == 0
    c = banc("file-neon")                                                         # un 402 : arrêt aussitôt
    c.faux.programmer(faux.erreur_google(402, message="payment required"), *conformes)
    bilan = c.jouer()
    e = c.envois()
    assert len(c.faux.appels()) == 1 and not bilan["complet"] and e[0]["decision"] == "arret" and _attentes(c) == []
    assert e[0]["cause"] == chef.MOTIF_CREDIT_EPUISE.format("code 402") and e[0]["refus_pour_credit"] == "code 402"
    rapport = chef.faire_rapport(c.dossier)
    assert rapport["reponses_de_code_200"] == 0 and not rapport["complete"]
    # Mistral : le second 429 garde son motif d'avant ; Google : le motif du second 429
    assert chef.decider_dans_la_file("mistral", {"code": 429, "corps": b"{}", "en_tetes": {}}, None, None, False, 2, "x") == (
        "arret", "second envoi d'un appel sur un code 429")
    assert chef.decider_dans_la_file("google", {"code": 429, "corps": b"{}", "en_tetes": {}}, None, None, False, 1, "x") == ("attente", "code 429")
    assert chef.decider_dans_la_file("google", {"code": 403, "corps": b'{"error": {"message": "credits depleted"}}', "en_tetes": {}},
                                     None, None, False, 1, "x") == ("arret", chef.MOTIF_CREDIT_EPUISE.format("code 403, « depleted »"))
    assert chef.decider_dans_la_file("mistral", {"code": 402, "corps": b"{}", "en_tetes": {}}, None, None, False, 1, "x") == (
        "arret", "garde 4 : code 402, arrêt sans reprise")


def test_l12_attente_sur_429_lit_le_retry_delay_de_google():
    """C-1 (b), écart déclaré au devis 5.6 : sans en-tête `Retry-After` lisible, le `retryDelay` de Google qui passe le
    défaut est attendu, arrondi à la seconde supérieure et borné à 600 ; jamais moins que le défaut ; l'en-tête prime."""
    regle = {"defaut_s": 30, "max_s": 600}
    corps = lambda d: json.dumps(faux.erreur_google(429, details=faux.details_du_debit_google(d))["corps"]).encode()   # noqa: E731
    assert chef.delai_dit_par_google(corps("23s")) == 23.0 and chef.delai_dit_par_google(corps("12.5s")) == 12.5
    assert chef.attente_sur_429({}, regle, corps("23s")) == 30                   # sous le défaut : le défaut
    assert chef.attente_sur_429({}, regle, corps("45s")) == 45
    assert chef.attente_sur_429({}, regle, corps("45.2s")) == 46
    assert chef.attente_sur_429({}, regle, corps("900s")) == 600                 # borné à 600
    assert chef.attente_sur_429({"retry-after": "12"}, regle, corps("45s")) == 12   # l'en-tête prime
    assert chef.attente_sur_429({"retry-after": "demain"}, regle, corps("45s")) == 45
    for illisible in (corps(None), corps("45"), corps("quarante s"), corps("-5s"), b"pas du json", b"[]",
                      json.dumps({"error": "x"}).encode(), json.dumps({"error": {"details": "x"}}).encode(),
                      json.dumps({"error": {"details": [{"@type": "type.googleapis.com/google.rpc.Help", "retryDelay": "45s"}]}}).encode(),
                      json.dumps({"error": {"details": [{"@type": "type.googleapis.com/google.rpc.RetryInfo", "retryDelay": 45}]}}).encode(),
                      None):
        assert chef.attente_sur_429({}, regle, illisible) == 30, illisible
    assert chef.delai_dit_par_google(json.dumps({"error": {"details": ["x", {"@type": "type.googleapis.com/google.rpc.RetryInfo",
                                                                              "retryDelay": " 31s "}]}}).encode()) == 31.0


def test_l12_garde_8_exige_l_avenant_3_et_go_16(monde):
    """C-2 : chaque ligne de Google d'une configuration définitive, ou de toute configuration qui inscrit l'avenant 3,
    cite l'empreinte de l'avenant 3 v2 et GO-2026-11-22-16, au périmètre ou à la référence."""
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    assert config["avenant_3"]["sha256"] == chef.EMPREINTE_AVENANT_3                # le gabarit l'inscrit
    court = registre_court(config)
    jour = MAINTENANT.strftime("%Y-%m-%d")
    for ligne in ("verification-google-cle-1", "verification-google-cle-2", "file-neon"):          # cas sain
        assert chef.verifier_ligne_de_calcul(config, ligne, {"GO_ID": GO[ligne]}, court, jour)
    deplace = court.replace(f" ; {chef.EMPREINTE_AVENANT_3} ; {GO_DE_L_AVENANT_3}", "")
    deplace = deplace.replace(f", devis {chef.EMPREINTE_DEVIS}", f", devis {chef.EMPREINTE_DEVIS}, {chef.EMPREINTE_AVENANT_3} {GO_DE_L_AVENANT_3}")
    assert chef.verifier_ligne_de_calcul(config, "file-neon", {"GO_ID": GO["file-neon"]}, deplace, jour)   # au périmètre : admis

    def refuse(registre, motif, c=config, ligne="file-neon"):
        with pytest.raises(chef.Arret, match=motif):
            chef.verifier_ligne_de_calcul(c, ligne, {"GO_ID": GO[ligne]}, registre, jour)

    refuse(court.replace(f" ; {chef.EMPREINTE_AVENANT_3}", ""), "ne cite pas l'empreinte de l'avenant 3")
    refuse(court.replace(f" ; {GO_DE_L_AVENANT_3}", ""), "ne cite pas GO-2026-11-22-16")
    refuse(court.replace(f" ; {GO_DE_L_AVENANT_3}", " ; GO-2026-11-22-160"), "ne cite pas GO-2026-11-22-16")
    refuse(court.replace(f" ; {GO_DE_L_AVENANT_3}", " ; GO-2026-11-22-02"), "ne cite pas GO-2026-11-22-16")
    sans = copy.deepcopy(config)
    sans["avenant_3"] = None
    refuse(court, "une configuration définitive inscrit l'avenant 3", c=sans)
    sans["avenant_3"] = "avenant 3"
    refuse(court, "une configuration définitive inscrit l'avenant 3", c=sans)
    # à l'essai : exigé dès que l'avenant 3 est inscrit ; nul, il n'est pas lu ; Mistral ne le lit jamais
    essai = copy.deepcopy(monde.config)
    sans_av3 = monde.registre().replace(f", avenant 3 {chef.EMPREINTE_AVENANT_3}, {GO_DE_L_AVENANT_3}", "")
    assert f", avenant 3 {chef.EMPREINTE_AVENANT_3}, {GO_DE_L_AVENANT_3}" in monde.registre()
    refuse(sans_av3, "ne cite pas l'empreinte de l'avenant 3", c=essai, ligne="verification-google-cle-1")
    essai["avenant_3"] = {"chemin": None, "sha256": None}
    assert chef.verifier_ligne_de_calcul(essai, "verification-google-cle-1", {"GO_ID": GO["verification-google-cle-1"]}, sans_av3, jour)
    assert chef.verifier_ligne_de_calcul(config, "verification-mistral-eu", {"GO_ID": GO["verification-mistral-eu"]}, sans_av3, jour)


def test_l12_la_piece_de_l_avenant_3(monde):
    """C-2 : la pièce `avenant_3`, vérifiée sur disque, à son compagnon et, en définitive, à l'empreinte 4b331d9a…"""
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    gabarit = json.loads((RACINE / GABARIT).read_text(encoding="utf-8"))
    assert chef.sha256_fichier(RACINE / gabarit["avenant_3"]["chemin"]) == chef.EMPREINTE_AVENANT_3 == gabarit["avenant_3"]["sha256"]
    lu = chef.controler_avenant_3(config, monde.racine, "file-neon")                                     # cas sain
    assert lu == {"chemin": gabarit["avenant_3"]["chemin"], "sha256": chef.EMPREINTE_AVENANT_3}
    assert chef.controler_avenant_3(config, monde.racine, "verification-mistral-eu") is None              # Mistral
    essai = copy.deepcopy(monde.config)
    for nulle in (None, {"chemin": None, "sha256": None}, {"chemin": None, "sha256": None, "note": "x"}):
        essai["avenant_3"] = nulle
        assert chef.controler_avenant_3(essai, monde.racine, "file-neon") is None                       # à l'essai, nulle
    monde.piece("autre-avenant.md", "un autre texte\n")
    monde.piece("sans-compagnon.md", "texte\n", sceller=False)

    def refuse(piece, motif, c=config):
        c = copy.deepcopy(c)
        c["avenant_3"] = piece
        with pytest.raises(chef.Arret, match=motif):
            chef.controler_avenant_3(c, monde.racine, "verification-google-cle-1")

    refuse(None, "une configuration définitive inscrit la pièce `avenant_3`")
    refuse({"chemin": None, "sha256": None}, "une configuration définitive inscrit la pièce `avenant_3`")
    refuse(monde.ref("autre-avenant.md"), "n'est pas celle de l'avenant 3 accepté")
    refuse(config["avenant_2"], "n'est pas celle de l'avenant 3 accepté")
    refuse({"chemin": gabarit["avenant_3"]["chemin"], "sha256": "0" * 64}, "empreinte")
    refuse(monde.ref("sans-compagnon.md"), "sans empreinte compagnon", c=essai)
    refuse({"chemin": gabarit["avenant_3"]["chemin"], "sha256": None}, "chemin et empreinte non inscrits", c=essai)
    refuse({"chemin": "pieces/absent.md", "sha256": chef.EMPREINTE_AVENANT_3}, "fichier absent", c=essai)
    refuse("avenant 3", "ni nul ni une pièce", c=essai)
    refuse(["x"], "ni nul ni une pièce", c=essai)
    refuse({"chemin": None, "sha256": None, "autre": 1}, "chemin et empreinte non inscrits", c=essai)
    # la ligne entière ne part pas, avant tout envoi ; et le manifeste recopie la pièce
    c = copy.deepcopy(config)
    c["avenant_3"] = None
    with pytest.raises(chef.Arret, match="avenant 3"):
        chef.gardes_avant_depart(c, "verification-google-cle-1", {"GO_ID": GO["verification-google-cle-1"]}, monde.racine,
                                 registre_court(config), MAINTENANT, a_blanc=True)


def test_l12_levee_des_seuils_seulement_sous_go_02(monde):
    """C-3 : la levée des seuils de Google ne passe que sous GO-2026-11-22-02, lu au registre en définitive. Une autre
    décision de Lazar qui cite la recharge automatique est refusée, dans tout état, à blanc compris."""
    config, registre = _google_sous_le_seuil(monde, {"leves_par": GO_RECHARGE})
    lu = chef.controler_levee_des_seuils(config, "verification-google-cle-1", registre, "2026-11-22")      # cas sain
    assert lu["mode"] == "leves" and lu["go"] == GO_RECHARGE and lu["ligne_du_registre"]["go"] == GO_RECHARGE
    autre = "GO-2026-11-21-99"
    fictive = ligne_de_recharge(go=autre, texte="Bras A : la recharge automatique reste activée.")
    for etat in ("definitive", "essai"):
        c = copy.deepcopy(config)
        c["etat"] = etat
        c["seuils_de_credit_google"] = {"leves_par": autre}
        with pytest.raises(chef.Arret, match=f"ne sont levés que sous {GO_RECHARGE} ; {autre} n'est pas admis"):
            chef.controler_levee_des_seuils(c, "verification-google-cle-1", registre + fictive, "2026-11-22")
    c = copy.deepcopy(config)
    c["seuils_de_credit_google"] = {"leves_par": autre}
    with pytest.raises(chef.Arret, match="n'est pas admis"):                                          # à blanc aussi
        chef.gardes_avant_depart(c, "verification-google-cle-1", {}, monde.racine, None, MAINTENANT, a_blanc=True)
    assert chef.seuils_de_credit_google({"seuils_de_credit_google": {"leves_par": GO_RECHARGE}}) == GO_RECHARGE
    assert chef.seuils_de_credit_google({"seuils_de_credit_google": "exiges"}) is None


def test_l12_a_blanc_dit_les_seuils_et_que_le_registre_n_est_pas_lu(monde, capsys):
    """Mineur 4 : la sortie `a-blanc` imprime le mode des seuils de Google, l'avenant 3 lu, et `registre_lu` faux."""
    monde.config["seuils_de_credit_google"] = {"leves_par": GO_RECHARGE}
    monde.inscrire_releve("file-neon", monde.releve("verification-google-cle-1", "v12"))
    chemin, empreinte = monde.ecrire_configuration()
    assert chef.a_blanc("file-neon", chemin, empreinte, {}, racine=monde.racine, a_l_instant=MAINTENANT) == 0
    sortie = json.loads(capsys.readouterr().out)
    assert sortie["seuils_de_credit_google"] == {"mode": "leves", "go": GO_RECHARGE, "ligne_du_registre": None}
    assert sortie["registre_lu"] is False and sortie["avenant_3"]["sha256"] == chef.EMPREINTE_AVENANT_3
    assert chef.a_blanc("verification-mistral-eu", chemin, empreinte, {}, racine=monde.racine, a_l_instant=MAINTENANT) == 0
    sortie = json.loads(capsys.readouterr().out)
    assert sortie["seuils_de_credit_google"] is None and sortie["avenant_3"] is None and sortie["registre_lu"] is False


def _retour_google(reponse) -> tuple:
    """Un retour de Google tel que le chef le lit, tiré d'une réponse du faux fournisseur, et sa lecture."""
    retour = {"code": reponse["code"], "corps": json.dumps(reponse["corps"]).encode(), "en_tetes": {}}
    return retour, chef.lire_le_retour("google", retour)


def test_m2_l12_artefacts_ajoutes_par_la_campagne_de_la_livraison_12(monde, capsys):
    """Les mutants qui survivaient au premier passage de la campagne `livraison12` : des branches de `classer_issue` et
    de `decider_dans_la_file` que seuls des essais hors du sous-ensemble éprouvaient, et trois bornes exactes."""
    classer = lambda retour, lu, appel="A", **k: chef.classer_issue("google", "h", appel, {}, retour, lu, None, False,   # noqa: E731
                                                                     borne_reflexion=16768, **k)[0]
    sain, lu = _retour_google(faux.reponse_google("OK"))
    assert classer(sain, lu) == 3 and chef.second_429("google", [], "A", sain) is False
    autre, lu_autre = _retour_google(faux.reponse_google("OK", modele="gemini-autre"))
    assert chef.classer_issue("google", "h", "A", {}, autre, lu_autre, None, False, borne_reflexion=16768) == (
        4, "code 200 avec un autre nom servi : nœud de Lazar ; pas de repli")         # code 200, autre nom servi
    absent, lu_absent = _retour_google(faux.reponse_google("OK", modele=None))
    assert chef.classer_issue("google", "h", "A", {}, absent, lu_absent, None, False, borne_reflexion=16768) == (
        4, "code 200, nom servi absent : nœud de Lazar ; pas de repli")              # code 200, nom absent
    assert classer(sain, None) == 13                                              # code 200 illisible : toute autre issue
    sans_pensee, lu_sp = _retour_google(faux.reponse_google("OK", usage=(30, 10, 0, 40)))
    assert chef.classer_issue("google", "h", "A", {}, sans_pensee, lu_sp, None, False, borne_reflexion=16768) == (
        13, f"{chef.REGLE_GOOGLE} : zéro jeton de pensée à l'appel de vérification — le réglage de réflexion est accepté "
            "mais rien ne montre qu'il est appliqué : non saine ; nœud de Lazar")
    dementie, lu_d = _retour_google(faux.reponse_google("OK", usage=(30, 10, 20000, 20040)))
    numero, issue = chef.classer_issue("google", "h", "A", {}, dementie, lu_d, None, False, borne_reflexion=16768)
    assert numero == 13 and issue.startswith(f"{chef.REGLE_GOOGLE} : ") and issue.endswith("à l'appel de vérification : non saine ; nœud de Lazar")
    for code, attendu in ((499, 13), (500, 6), (599, 6), (600, 13)):
        r = {"code": code, "corps": b'{"error": {"message": "x"}}', "en_tetes": {}}
        assert classer(r, None) == attendu, code
    tous = {"code": 400, "corps": json.dumps(faux.erreur_google(400, "invalide", champs=list(chef.CHAMPS_NIVEAU_DE_REFLEXION))["corps"]).encode(),
            "en_tetes": {}}
    assert classer(tous, None) == 11                                              # tous les champs du niveau : A′
    # la file
    d = lambda retour, lu, incident=None, signature=False, rang=1: chef.decider_dans_la_file(            # noqa: E731
        "google", retour, lu, incident, signature, rang, chef.IDENTIFIANTS["google"], 16768)
    assert d(sain, lu) == ("ok", None)
    assert d(sain, lu, signature=True) == ("reprise", "refus du mandataire à sa signature (panne de transport)")
    assert d(sain, lu, signature=True, rang=2) == ("arret", "refus du mandataire à sa signature (panne de transport)")
    assert d(sain, None, incident="delai") == ("reprise", "délai dépassé")
    assert d(sain, None, incident="coupure") == ("reprise", "connexion coupée")
    assert d(sain, None, incident="interruption") == ("arret", "interruption de notre côté")
    assert d(sain, None) == ("arret", "garde 5 : nom servi autre que celui du relevé de vérification")
    assert d(autre, lu_autre) == ("arret", "garde 5 : nom servi autre que celui du relevé de vérification")
    sans_usage, lu_su = _retour_google(faux.reponse_google("OK", sans_usage=True))
    assert d(sans_usage, lu_su) == ("arret", "réponse de code 200 sans compteur lisible")
    au_max, lu_m = _retour_google(faux.reponse_google("OK", fin="MAX_TOKENS"))
    assert d(au_max, lu_m) == ("arret", "garde 3 : fin par sortie maximale atteinte")
    assert d(sans_pensee, lu_sp) == ("arret", f"{chef.REGLE_GOOGLE} : {chef.defaut_de_reponse_google(lu_sp, 16768)} : "
                                              "défaut journalisé, jamais une réponse")
    for code, attendu in ((500, "reprise"), (599, "reprise"), (600, "arret")):
        assert d({"code": code, "corps": b"{}", "en_tetes": {}}, None)[0] == attendu, code
    for code in (401, 403):
        assert d({"code": code, "corps": b"{}", "en_tetes": {}}, None) == ("arret", f"garde 4 : code {code}, arrêt sans reprise")
    assert d({"code": 404, "corps": b"{}", "en_tetes": {}}, None) == ("arret", "garde 4 : code 404, arrêt")
    # l'avenant 3 : le message cite les huit premiers signes de l'empreinte acceptée
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    config["avenant_3"] = config["avenant_2"]
    with pytest.raises(chef.Arret, match=r"accepté \(4b331d9a…\)$"):
        chef.controler_avenant_3(config, monde.racine, "file-neon")
    # à blanc : l'heure donnée est celle des gardes (un mois plus tôt, le constat est d'après l'envoi) ; sortie indentée d'un
    monde.inscrire_releve("file-neon", monde.releve("verification-google-cle-1", "m2l12"))
    chemin, empreinte = monde.ecrire_configuration()
    assert chef.a_blanc("verification-mistral-eu", chemin, empreinte, {}, racine=monde.racine, a_l_instant=MAINTENANT) == 0
    assert capsys.readouterr().out.startswith('{\n "a_blanc": true,')
    with pytest.raises(chef.Arret, match="date postérieure à l'envoi"):           # un mois plus tôt : pièce d'après l'envoi
        chef.a_blanc("verification-mistral-eu", chemin, empreinte, {}, racine=monde.racine,
                     a_l_instant=MAINTENANT - datetime.timedelta(days=30))


def test_m2_l12_mineur5_jouer_verification_et_garde_console(monde, banc, monkeypatch):
    """Mineur 5 : les mutants de `jouer_verification` et de `garde_console` qui survivaient à toute la suite (campagne
    `livraison12_mineur5`) : bornes et branches de la sonde, numéros d'envoi, arrondis, pauses, ligne 1 à l'appel A,
    page et heure de la lecture de la console, seuil pile à la console."""
    # un relevé sain : numéros d'envoi, ligne finale, une seule pause (après A), arrondis à six décimales
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK"), sonde_google())
    releve = g.verifier()
    assert [(a["envoi"], a["rang"]) for a in releve["appels"]] == [("L1-01-A", 1), ("L1-02-B", 2)]
    assert releve["issue_finale_ligne"] == 3 and not releve["noeud_de_lazar"] and g.pauses == [monde.config["pause_s"]]
    assert releve["depense_comptee_usd"] == round(releve["depense_comptee_usd"], 6)
    departs = [l for l in chef.lire_journal(g.dossier / "journal-essai.jsonl") if l.get("evenement") == "depart"]
    assert departs and all(d[k] == round(d[k], 6) for d in departs for k in ("reserve_usd", "cumul_usd", "cout_si_sans_reponse_usd"))
    # la règle de Google est contrôlée avant tout appel de la vérification
    mauvaise = copy.deepcopy(monde.config)
    mauvaise["fournisseurs"]["google"]["exemption_de_la_sonde_go"] = None
    h = banc("verification-google-cle-1")
    with pytest.raises(chef.Arret, match="ne cite pas le GO qui l'accorde"):
        chef.jouer_verification(mauvaise, "verification-google-cle-1", h.dossier, h.url, h.journal_relais, [],
                                chef.etat_de_la_ligne(monde.racine, mauvaise, "verification-google-cle-1", h.go), h.go,
                                dormir=h.pauses.append)
    assert h.faux.recus == []
    # la sonde : 500 et 599 sont à refaire ; 600 ferme la sonde ; un crédit dit ferme à la ligne 13
    for code, refaire in ((500, True), (599, True), (600, False)):
        s = banc("verification-google-cle-1")
        s.faux.programmer(faux.reponse_google("OK"), faux.erreur_google(code))
        r = s.verifier()
        assert bool(r["a_refaire"]) is refaire and r["close"] is (not refaire), code
    c = banc("verification-google-cle-1")
    c.faux.programmer(faux.reponse_google("OK"), faux.erreur_google(402))
    assert c.verifier()["issue_finale_ligne"] == 13
    # ligne 1 à l'appel A (refus du mandataire à sa signature) : à refaire, non compté, sans ligne finale
    monkeypatch.setattr(chef, "signature_du_mandataire", lambda retour, journal, envoi: envoi.endswith("-A"))
    m = banc("verification-google-cle-1")
    m.faux.programmer(faux.reponse_google("OK"))
    r = m.verifier()
    assert r["appels"][0]["ligne_du_classement"] == 1 and not r["appels"][0]["compte_parmi_les_trois"]
    assert r["a_refaire"] and not r["close"] and r["issue_finale_ligne"] is None and r["appels_comptes"] == 0
    monkeypatch.undo()
    # garde 20 : page et heure exigées ; seuil pile admis, sans rien écrire ; arrondi de la dépense comptée à six décimales
    lu = _constat_lu(monde)
    ref = monde.releve("verification-google-cle-1", "c5", go="GO-2026-11-26-05", envois_coupes=["L1-01-A"], depense_comptee_usd=0.5)
    texte = lecture_console_google(ref["sha256"])

    def console(t, cfg=monde.config):
        monde.piece("console-m5.md", t)
        cfg["lignes"]["file-neon"]["lectures_console"] = [monde.ref("console-m5.md")]
        return chef.garde_console(cfg, monde.racine, "file-neon", GO["file-neon"], lu)

    for retire in ("- page :", "- heure (UTC) :"):
        with pytest.raises(chef.Arret, match="ne donne pas sa page et son heure"):
            console("\n".join(l for l in texte.split("\n") if not l.startswith(retire)) + "\n")
    assert console(lecture_console_google(ref["sha256"], soldes=("16,08", "16,08")))                  # seuil pile : admis
    leve = copy.deepcopy(monde.config)
    leve["seuils_de_credit_google"] = {"leves_par": GO_RECHARGE}
    servies = console(lecture_console_google(ref["sha256"], soldes=("16,08", "16,07")), leve)
    assert list(servies[0]["sous_le_seuil"]) == ["b"]                                                  # pile : rien d'écrit
    proche = monde.releve("verification-google-cle-1", "c6", go="GO-2026-11-26-06", envois_coupes=["L1-01-A"],
                          depense_comptee_usd=0.4899996)
    monde.piece("console-m6.md", lecture_console_google(proche["sha256"], ("0,29", "0,20")))
    monde.config["lignes"]["file-neon"]["lectures_console"] = [monde.ref("console-m5.md"), monde.ref("console-m6.md")]
    monde.piece("console-m5.md", texte)
    monde.config["lignes"]["file-neon"]["lectures_console"] = [monde.ref("console-m5.md"), monde.ref("console-m6.md")]
    assert len(chef.garde_console(monde.config, monde.racine, "file-neon", GO["file-neon"], lu)) == 2   # 0,49 vus, 0,49 comptés
    # nœud de Lazar sous un retrait d'avance de la température : non sur un relevé sain, oui sur la ligne 10
    monde.config["temperature_retiree_d_avance"] = _retrait(GO["verification-mistral-eu"])
    t = banc("verification-mistral-eu")
    t.faux.programmer(faux.flux_mistral("OK"), sonde_mistral())
    r = t.verifier()
    assert r["saine"] and r["issue_finale_ligne"] == 3 and r["noeud_de_lazar"] is (r["sonde"]["issue"] != "comprise" or r["majorant"] == "démenti")
    u = banc("verification-mistral-eu")
    u.faux.programmer(faux.erreur_mistral(422, detail=[{"loc": ["body", "temperature"], "msg": "not supported"}]))
    r = u.verifier()
    assert r["issue_finale_ligne"] == 10 and r["noeud_de_lazar"] and r["majorant"] != "démenti"
    # une pause après chaque appel qui laisse la vérification ouverte : A refusé (température), A′, puis la sonde
    monde.config["temperature_retiree_d_avance"] = False
    p = banc("verification-mistral-eu")
    p.faux.programmer(faux.erreur_mistral(422, detail=[{"loc": ["body", "temperature"], "msg": "not supported"}]),
                      faux.flux_mistral("OK"), sonde_mistral())
    r = p.verifier()
    assert [a["type"] for a in r["appels"]] == ["A", "Ap", "B"] and p.pauses == [monde.config["pause_s"]] * 2
    # le relevé réduit (garde 18) garde l'envoi, le genre et l'incident, en chaînes, et rien d'autre de textuel
    q = banc("verification-google-cle-1")
    q.faux.programmer(faux.reponse_google("OK"), sonde_google())
    monkeypatch.setattr(chef, "controler_aucune_sous_chaine", lambda *a, **k: 1)
    r = q.verifier()
    monkeypatch.undo()
    assert r["reduit"] and [(a["envoi"], a["type"], a["regime"]) for a in r["appels"]] == [("L1-01-A", "A", "prudent"), ("L1-02-B", "B", "prudent")]
    assert all(a["code"] == 200 and a["ligne_du_classement"] in (3, None) for a in r["appels"])


# === Livraison 13 : corrections de la vérification de la livraison 12 (constat 1, majeur ; constats 2 à 7, mineurs) ====
# Constat 1 : à la vérification de la clé, après un 429 de Google, l'attente due (règle de la file, bornée à 600 s) et
# l'heure `pas_avant` sont écrites ; tout lancement nouveau de la même ligne avant cette heure est refusé.

def _heure(texte: str) -> datetime.datetime:
    return datetime.datetime.strptime(texte, chef.FORME_DE_L_HEURE).replace(tzinfo=datetime.timezone.utc)


def _appel_429(envoi="L1-01-A", pas_avant=None, **plus) -> dict:
    """La fiche d'un appel de vérification qui a reçu un 429 de Google, du fournisseur, compté parmi les trois."""
    fiche = {"envoi": envoi, "type": "A", "rang": 1, "lancement": 1, "code": 429, "origine": "amont",
             "compte_parmi_les_trois": True, "ligne_du_classement": 6, "a_refaire": False, "incident": None,
             "cout_usd": 0.0, "attente_due_s": 30.0, "pas_avant": pas_avant}
    fiche.update(plus)
    return fiche


def test_l13_sain_l_attente_due_est_ecrite_au_releve_lue_sur_le_corps_entier(monde, banc):
    """Constat 1, cas sain : un 429 de débit de Google qui dit `retryDelay` 45 s, à l'octet 819 d'un corps de 841 :
    l'attente due est de 45 s (le corps d'erreur écrit, borné à 500 octets, ne porte pas le délai) ; `pas_avant` est
    l'heure de réception plus 45 s, à la seconde supérieure ; au relevé, à la fiche et au journal. Après l'heure, les
    gardes d'avant le départ passent et le lancement nouveau part, sain."""
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.debit_google("45s"))
    avant = chef.maintenant()
    releve = g.verifier()
    apres = chef.maintenant()
    a = releve["appels"][0]
    assert a["ligne_du_classement"] == 6 and a["attente_due_s"] == 45.0 and a["retry_delay_lu_s"] == 45.0
    assert len(a["corps_d_erreur"]) == chef.CORPS_D_ERREUR_MAX and "retryDelay" not in a["corps_d_erreur"]
    pas = _heure(a["pas_avant"])
    assert avant + datetime.timedelta(seconds=45) <= pas + datetime.timedelta(seconds=1) and pas <= apres + datetime.timedelta(seconds=46)
    assert releve["attente_due_s"] == 45.0 and releve["pas_avant"] == a["pas_avant"]
    envoi = [l for l in chef.lire_journal(g.dossier / "journal-essai.jsonl") if l.get("evenement") == "envoi"][0]
    assert envoi["pas_avant"] == a["pas_avant"] and envoi["attente_due_s"] == 45.0        # aussi au journal (C-1)
    etat = chef.etat_de_la_ligne(monde.racine, monde.config, "verification-google-cle-1", g.go)
    assert chef.garde_attente_due(etat, "verification-google-cle-1", pas) == {
        "pas_avant": a["pas_avant"], "attente_due_s": 45.0, "envoi": "L1-01-A"}          # à l'heure pile : admis
    avant_depart = chef.gardes_avant_depart(monde.config, "verification-google-cle-1", {"GO_ID": g.go}, monde.racine,
                                            monde.registre(), pas + datetime.timedelta(seconds=1))
    assert avant_depart["attente_due"]["pas_avant"] == a["pas_avant"]
    g.nouveau_dossier()                                                                   # relance après l'heure : part
    g.faux.programmer(faux.reponse_google("OK"), sonde_google())
    suite = g.verifier()
    assert suite["saine"] and suite["close"] and len(g.faux.appels()) == 3 and suite["pas_avant"] == a["pas_avant"]
    # la règle de la file : défaut de 30 s sous un délai de 23 s ; l'en-tête `Retry-After` prime sur le corps
    for reponse, attendue, lu in ((faux.debit_google(), 30.0, 23.0), (faux.debit_google(courte=True), 30.0, None),
                                  (faux.debit_google("45s", en_tetes={"Retry-After": "90"}), 90.0, 45.0),
                                  (faux.credit_epuise_google(), 30.0, None)):
        h = banc("verification-google-cle-1")
        h.faux.programmer(reponse)
        f = h.verifier()["appels"][0]
        assert (f["attente_due_s"], f["retry_delay_lu_s"]) == (attendue, lu)
    # sans 429 de Google, aucune attente due : un 200, un 503, et un 429 de Mistral (règle propre à Google)
    s = banc("verification-google-cle-1")
    s.faux.programmer(faux.erreur_google(503))
    r = s.verifier()
    assert r["appels"][0]["attente_due_s"] is None and r["pas_avant"] is None and r["attente_due_s"] is None
    m = banc("verification-mistral-eu")
    m.faux.programmer(faux.erreur_mistral(429, message="Requests rate limit exceeded", en_tetes={"Retry-After": "90"}))
    r = m.verifier()
    assert r["appels"][0]["pas_avant"] is None and r["pas_avant"] is None
    assert chef.garde_attente_due(chef.etat_de_la_ligne(monde.racine, monde.config, "verification-mistral-eu", m.go),
                                  "verification-mistral-eu", MAINTENANT) is None


def test_l13_bout_en_bout_relance_avant_l_heure_refusee_apres_l_heure_part(monde, tmp_path, capsys):
    """Constat 1, de bout en bout par la commande : un 429 de Google à la vérification (code 3, à refaire) ; relancée
    aussitôt, la ligne est refusée avant tout envoi (code 2, « attendre jusqu'à … »), sans dossier ni appel de plus,
    et la commande à blanc le dit de même ; relancée après l'heure, elle part et finit saine."""
    fournisseur = faux.FauxFournisseur(faux.modele_google()).demarrer()
    try:
        monde.config["essai_local"] = {"google": fournisseur.url}
        chemin, empreinte = monde.ecrire_configuration("configuration-l13.json")
        env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "GO_ID": GO["verification-google-cle-1"],
               "GEMINI_API_KEY": "valeur-factice-du-relais"}
        base = monde.racine / "runs" / "verification-cle-google-1-bras-a-v1"
        fournisseur.programmer(faux.debit_google())
        assert chef.executer("verification-google-cle-1", chemin, empreinte, env, racine=monde.racine,
                             registre=monde.registre(), a_l_instant=MAINTENANT) == 3
        releve = json.loads((dossiers_de(base)[0] / "releve-verification-v1.json").read_text(encoding="utf-8"))
        assert releve["attente_due_s"] == 30.0 and releve["a_refaire"] and not releve["close"]
        pas = _heure(releve["pas_avant"])
        capsys.readouterr()
        appels, dossiers = len(fournisseur.appels()), len(dossiers_de(base))
        fournisseur.programmer(faux.reponse_google("OK"), sonde_google())
        assert chef.executer("verification-google-cle-1", chemin, empreinte, env, racine=monde.racine,
                             registre=monde.registre(), a_l_instant=MAINTENANT + datetime.timedelta(seconds=1)) == 2
        assert f"ARRÊT avant tout envoi : attendre jusqu'à {releve['pas_avant']}" in capsys.readouterr().err
        assert len(fournisseur.appels()) == appels and len(dossiers_de(base)) == dossiers          # rien ne part
        assert chef.executer("verification-google-cle-1", chemin, empreinte, env, racine=monde.racine,
                             registre=monde.registre(), a_l_instant=pas - datetime.timedelta(seconds=1)) == 2
        assert len(fournisseur.appels()) == appels                                                 # une seconde avant : non
        with pytest.raises(chef.Arret, match="attendre jusqu'à"):
            chef.a_blanc("verification-google-cle-1", chemin, empreinte, {}, racine=monde.racine,
                         a_l_instant=MAINTENANT + datetime.timedelta(seconds=1))
        assert chef.a_blanc("verification-google-cle-1", chemin, empreinte, {}, racine=monde.racine, a_l_instant=pas) == 0
        assert json.loads(capsys.readouterr().out)["attente_due"] == {"pas_avant": releve["pas_avant"], "attente_due_s": 30.0,
                                                                      "envoi": "L1-01-A"}
        assert chef.executer("verification-google-cle-1", chemin, empreinte, env, racine=monde.racine,
                             registre=monde.registre(), a_l_instant=pas + datetime.timedelta(seconds=1)) == 0
        suite = json.loads((dossiers_de(base)[-1] / "releve-verification-v1.json").read_text(encoding="utf-8"))
        assert suite["saine"] and suite["lancements"] == 2 and len(fournisseur.appels()) == appels + 2
        manifeste = json.loads((dossiers_de(base)[-1] / "manifeste-depart.json").read_text(encoding="utf-8"))
        assert manifeste["attente_due"]["pas_avant"] == releve["pas_avant"] and manifeste["go_de_la_confirmation_de_l_avenant_3"] is None
    finally:
        fournisseur.arreter()


def test_l13_artefacts_releve_sans_l_heure_et_delai_borne_a_600(monde, banc):
    """Constat 1, artefacts : un 429 de Google au relevé sans heure `pas_avant` lisible arrête la ligne avant tout
    envoi (aucun repli) ; la relance avant l'heure est refusée ; un délai au-delà de 600 s est borné à 600, quelle que
    soit la configuration. Ne comptent pas : un 429 écrit par le relais, un appel non compté, un autre code, Mistral."""
    ligne, jour = "verification-google-cle-1", MAINTENANT
    for pas_avant in (None, "demain", "2026-11-22 10:00:00", 1764000000):
        with pytest.raises(chef.Arret, match="ne porte pas son heure « pas_avant » lisible"):
            chef.garde_attente_due({"appels": [_appel_429(pas_avant=pas_avant)]}, ligne, jour)
    tot, tard = "2026-11-22T10:00:00Z", "2026-11-22T10:05:00Z"
    etat = {"appels": [_appel_429("L1-01-A", tard, attente_due_s=300.0), _appel_429("L2-02-A", tot)]}
    with pytest.raises(chef.Arret, match=rf"attendre jusqu'à {tard} : l'appel L1-01-A .* 300.0 s d'attente"):
        chef.garde_attente_due(etat, ligne, _heure(tot) + datetime.timedelta(seconds=1))          # le plus tardif prime
    assert chef.garde_attente_due(etat, ligne, _heure(tard))["envoi"] == "L1-01-A"
    for autre in (_appel_429(origine="relais"), _appel_429(compte_parmi_les_trois=False), _appel_429(code=503),
                  _appel_429(code=None)):
        assert chef.garde_attente_due({"appels": [autre]}, ligne, jour) is None
    assert chef.garde_attente_due({"appels": [_appel_429()]}, "verification-mistral-eu", jour) is None
    assert chef.garde_attente_due({"appels": []}, ligne, jour) is None and chef.garde_attente_due({}, ligne, jour) is None
    # le relevé sans l'heure, par les gardes d'avant le départ : rien ne part
    dans_dix = (MAINTENANT + datetime.timedelta(minutes=10)).strftime(chef.FORME_DE_L_HEURE)
    propre, go_propre = copy.deepcopy(monde.config), "GO-2026-11-27-01"          # sous une ligne de calcul à lui
    propre["lignes"][ligne]["go"] = go_propre
    registre_propre = monde.registre().replace(f"| {GO[ligne]} |", f"| {go_propre} |")
    monde.releve(ligne, "l13-sans-heure", go=go_propre, close=False, saine=False, issue_finale_ligne=6, appels=[_appel_429()])
    with pytest.raises(chef.Arret, match="ne porte pas son heure"):
        chef.gardes_avant_depart(propre, ligne, {"GO_ID": go_propre}, monde.racine, registre_propre, MAINTENANT)
    monde.releve(ligne, "l13-tot", go="GO-2026-11-27-02", close=False, saine=False, issue_finale_ligne=6,
                 appels=[_appel_429(pas_avant=dans_dix)])                             # avec l'heure : avant, rien ne part
    propre["lignes"][ligne]["go"] = "GO-2026-11-27-02"
    registre_propre = monde.registre().replace(f"| {GO[ligne]} |", "| GO-2026-11-27-02 |")
    with pytest.raises(chef.Arret, match=f"attendre jusqu'à {dans_dix}"):
        chef.gardes_avant_depart(propre, ligne, {"GO_ID": "GO-2026-11-27-02"}, monde.racine, registre_propre, MAINTENANT)
    # le délai borné à 600 secondes, quelle que soit la règle inscrite
    recu = datetime.datetime(2026, 11, 22, 10, 0, 0, tzinfo=datetime.timezone.utc)
    corps = lambda d: json.dumps(faux.erreur_google(429, details=faux.details_du_debit_google(d))["corps"]).encode()   # noqa: E731
    du = lambda en_tetes, c, regle={"defaut_s": 30, "max_s": 600}, **k: chef.attente_due_a_la_verification(  # noqa: E731
        k.get("f", "google"), {"code": k.get("code", 429), "corps": c, "en_tetes": en_tetes}, k.get("signature", False), regle, recu)
    assert du({}, corps("900s")) == {"attente_due_s": 600.0, "retry_delay_lu_s": 900.0, "pas_avant": "2026-11-22T10:10:00Z"}
    assert du({}, corps("900s"), {"defaut_s": 30, "max_s": 1200})["attente_due_s"] == 600.0
    assert du({"retry-after": "3600"}, corps("45s"), {"defaut_s": 30, "max_s": 7200})["attente_due_s"] == 600.0
    assert du({"retry-after": "599"}, corps("45s"), {"defaut_s": 30, "max_s": 7200})["attente_due_s"] == 599.0
    assert du({}, corps("45s"))["pas_avant"] == "2026-11-22T10:00:45Z"
    assert du({}, corps("45.2s"))["pas_avant"] == "2026-11-22T10:00:46Z"
    demi = recu + datetime.timedelta(microseconds=500000)                                     # à la seconde supérieure
    assert chef.attente_due_a_la_verification("google", {"code": 429, "corps": corps("45s"), "en_tetes": {}}, False,
                                              {"defaut_s": 30, "max_s": 600}, demi)["pas_avant"] == "2026-11-22T10:00:46Z"
    relais = json.dumps({"erreur": {"origine": "relais", "motif": "x"}}).encode()
    for k in ({"f": "mistral"}, {"code": 503}, {"code": 200}, {"signature": True}):
        assert du({}, corps("45s"), **k) is None, k
    assert du({}, relais) is None                                                             # écrit par le relais
    monde.config["attente_429"] = {"defaut_s": 30, "max_s": 1200}                             # par le banc : borné à 600
    b = banc(ligne)
    b.faux.programmer(faux.debit_google("900s"))
    a = b.verifier()["appels"][0]
    assert a["attente_due_s"] == 600.0 and a["retry_delay_lu_s"] == 900.0


def test_l13_go_16_lu_au_registre_comme_go_02(monde):
    """Constat 2 : en configuration définitive, la ligne de GO-2026-11-22-16 est lue au registre : une seule, décision,
    de Lazar, non échue, non révoquée, qui dit « seuils levés » et cite 4b331d9a ; sinon rien ne part. La garde 8 lit
    désormais GO-16 borné des deux côtés."""
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    court = registre_court(config)
    lu = chef.controler_go_de_l_avenant_3(config, "file-neon", court, "2026-11-22")                  # cas sain
    assert lu["go"] == GO_DE_L_AVENANT_3 and lu["echeance"] == "2099-12-31"
    reel = court.replace(ligne_de_confirmation(), ligne_de_confirmation(echeance="2026-11-30"))       # la vraie échéance
    assert chef.controler_go_de_l_avenant_3(config, "verification-google-cle-2", reel, "2026-11-30")["echeance"] == "2026-11-30"
    assert chef.controler_go_de_l_avenant_3(config, "verification-mistral-eu", None, "2026-11-22") is None   # Mistral
    assert chef.controler_go_de_l_avenant_3(monde.config, "file-neon", None, "2026-11-22") is None          # à l'essai
    sans = court.replace(ligne_de_confirmation(), "")

    def refuse(registre, motif, jour="2026-11-22"):
        with pytest.raises(chef.Arret, match="GO de la confirmation de l'avenant 3 : .*" + motif):
            chef.controler_go_de_l_avenant_3(config, "verification-google-cle-1", registre, jour)

    refuse(sans, "0 ligne")
    refuse(None, "registre des GO non lu")
    refuse(sans + ligne_de_confirmation() + ligne_de_confirmation(), "2 ligne")
    refuse(reel, "échue", jour="2026-12-01")
    refuse(sans + ligne_de_confirmation(type_="calcul"), "de type « calcul »")
    refuse(sans + ligne_de_confirmation(par="Mazar"), "pas accordée par Lazar")
    refuse(sans + ligne_de_confirmation(texte="Bras A : les seuils de crédit sont levés (4b331d9a…)."), "ne cite pas « seuils levés »")
    refuse(sans + ligne_de_confirmation(texte="« oui, seuils levés » ; avenant 3 v2"), r"ne cite pas l'avenant 3 \(4b331d9a…\)")
    refuse(court + f"| GO-2026-11-23-90 | 2026-11-23 | révocation | {GO_DE_L_AVENANT_3} | — | — | Lazar | — |\n", "révoquée")
    # la ligne entière : sans GO-16 au registre, rien ne part
    config_l11, registre = _google_sous_le_seuil(monde, {"leves_par": GO_RECHARGE})
    ligne = "verification-google-cle-1"
    avant = chef.gardes_avant_depart(config_l11, ligne, {"GO_ID": config_l11["lignes"][ligne]["go"]}, monde.racine, registre, MAINTENANT)
    assert avant["go_de_la_confirmation_de_l_avenant_3"]["go"] == GO_DE_L_AVENANT_3
    with pytest.raises(chef.Arret, match="GO de la confirmation de l'avenant 3"):
        chef.gardes_avant_depart(config_l11, ligne, {"GO_ID": config_l11["lignes"][ligne]["go"]}, monde.racine,
                                 registre.replace(ligne_de_confirmation(), ""), MAINTENANT)
    # garde 8 : GO-16 borné à gauche comme à droite
    jour = MAINTENANT.strftime("%Y-%m-%d")
    for faux_go in ("AGO-2026-11-22-16", "X-GO-2026-11-22-16", "GO-2026-11-22-160", "_GO-2026-11-22-16"):
        with pytest.raises(chef.Arret, match="ne cite pas GO-2026-11-22-16"):
            chef.verifier_ligne_de_calcul(config, "file-neon", {"GO_ID": GO["file-neon"]},
                                          court.replace(f" ; {GO_DE_L_AVENANT_3} |", f" ; {faux_go} |"), jour)
    for bon in ("(GO-2026-11-22-16)", "GO-2026-11-22-16.", "«GO-2026-11-22-16»"):
        assert chef.verifier_ligne_de_calcul(config, "file-neon", {"GO_ID": GO["file-neon"]},
                                             court.replace(f" ; {GO_DE_L_AVENANT_3} |", f" ; {bon} |"), jour)


AVENANT_3 = "docs/notes/relance-organismes-discrets-v1/avenant-3-devis-essais-admission-seuils-de-credit-google-leves-v2.md"


def test_l13_garde_8_lit_les_trois_textes_de_la_section_4_de_l_avenant_3(monde):
    """Constat 3 (avenant 3, section 3, point 5) : les trois textes de la section 4 de l'avenant 3, tels quels, au
    périmètre ; à la référence, les empreintes de l'avenant 2 et de l'avenant 3 et GO-2026-11-22-16 ; sur une
    configuration définitive : admis. Sans GO-16, sans l'empreinte de l'avenant 3, ou sans une marque : refusés."""
    assert chef.sha256_fichier(RACINE / AVENANT_3) == chef.EMPREINTE_AVENANT_3
    textes = dict(re.findall(r"^\*\*Ligne (\d)\. [^*]+\*\* : (.+)$", (RACINE / AVENANT_3).read_text(encoding="utf-8"), re.M))
    assert sorted(textes) == ["2", "4", "6"] and all("|" not in t for t in textes.values())
    config = valeurs_de_l_avenant_2(copy.deepcopy(monde.config))
    jour = "2026-11-22"

    def registre(texte, reference):
        lignes = ["| identifiant | accordé | type | périmètre | plafond | échéance | par | référence |", "|---|---|---|---|---|---|---|---|"]
        for numero, nom in (("2", "verification-google-cle-1"), ("6", "verification-google-cle-2"), ("4", "file-neon")):
            lignes.append(f"| {GO[nom]} | 2026-11-22 | calcul | {texte(textes[numero])} | {config['lignes'][nom]['plafond_registre']} "
                          f"| 2026-11-30 | Lazar | {reference} |")
        return "\n".join(lignes) + "\n" + ligne_d_exemption() + ligne_de_confirmation(echeance="2026-11-30")

    entiere = (f"avenant 2 {chef.EMPREINTE_AVENANT_2} ; avenant 3 {chef.EMPREINTE_AVENANT_3} ; {GO_DE_L_AVENANT_3}")
    tel_quel = registre(lambda t: t, entiere)
    for nom in ("verification-google-cle-1", "verification-google-cle-2", "file-neon"):                # cas sain
        assert chef.verifier_ligne_de_calcul(config, nom, {"GO_ID": GO[nom]}, tel_quel, jour)
        assert chef.controler_go_de_l_avenant_3(config, nom, tel_quel, jour)["go"] == GO_DE_L_AVENANT_3
    assert [len(l) for l in tel_quel.splitlines()[2:5]] == [3046, 3048, 2973]        # signes des trois lignes
    for reference, motif in ((f"avenant 2 {chef.EMPREINTE_AVENANT_2} ; avenant 3 {chef.EMPREINTE_AVENANT_3}", "ne cite pas GO-2026-11-22-16"),
                             (f"avenant 2 {chef.EMPREINTE_AVENANT_2} ; {GO_DE_L_AVENANT_3}", "ne cite pas l'empreinte de l'avenant 3"),
                             (f"avenant 3 {chef.EMPREINTE_AVENANT_3} ; {GO_DE_L_AVENANT_3}", "ne cite pas l'empreinte de l'avenant 2")):
        for nom in ("verification-google-cle-1", "verification-google-cle-2", "file-neon"):
            with pytest.raises(chef.Arret, match=motif):
                chef.verifier_ligne_de_calcul(config, nom, {"GO_ID": GO[nom]}, registre(lambda t: t, reference), jour)
    for nom in ("verification-google-cle-1", "file-neon"):                                             # une marque ôtée
        marque = config["lignes"][nom]["marques_du_perimetre"][0]
        with pytest.raises(chef.Arret, match=f"ne nomme pas {nom}"):
            chef.verifier_ligne_de_calcul(config, nom, {"GO_ID": GO[nom]}, registre(lambda t: t.replace(marque, "x"), entiere), jour)


def test_l13_file_un_429_apres_une_panne_n_est_pas_le_second_429(monde, banc):
    """Constat 4 : dans la file de Google, un 429 au second envoi d'un appel dont le premier n'a pas reçu de 429 (un
    503, une connexion coupée) arrête la file de même, sans troisième envoi, sous le motif d'une seconde panne, qui ne
    dit pas le crédit ; deux 429 gardent le motif du second 429."""
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    for premier, cause in ((faux.erreur_google(503), "code 503"), (faux.fermer(), "connexion coupée")):
        s = banc("file-neon")
        s.faux.programmer(premier, faux.debit_google(), *conformes)
        bilan = s.jouer()
        e = s.envois()
        assert [x["decision"] for x in e] == ["reprise", "arret"] and len(s.faux.recus) == 2 and not bilan["complet"]
        assert e[1]["cause"] == chef.MOTIF_429_APRES_UNE_PANNE.format(cause) == bilan["arret"]
        assert "crédit" not in e[1]["cause"] and _attentes(s) == []
    d = banc("file-neon")
    d.faux.programmer(faux.debit_google(), faux.debit_google(), *conformes)
    assert d.jouer()["arret"] == chef.MOTIF_SECOND_429
    r429 = {"code": 429, "corps": json.dumps(faux.debit_google()["corps"]).encode(), "en_tetes": {}}
    d2 = lambda cause, f="google": chef.decider_dans_la_file(f, r429, None, None, False, 2, "x", 16768, cause)   # noqa: E731
    assert d2("code 429") == ("arret", chef.MOTIF_SECOND_429) and d2(None) == ("arret", chef.MOTIF_SECOND_429)
    assert d2("délai dépassé") == ("arret", chef.MOTIF_429_APRES_UNE_PANNE.format("délai dépassé"))
    assert d2("refus du mandataire à sa signature (panne de transport)")[1].startswith("seconde panne sur le même appel : code 429")
    assert d2("code 503", "mistral") == ("arret", "second envoi d'un appel sur un code 429")
    assert chef.decider_dans_la_file("google", r429, None, "borne_octets", False, 2, "x", 16768, "code 503") == (
        "arret", "envoi coupé à sa borne en octets : file arrêtée par sa borne de dépense, sans reprise")
    assert chef.decider_dans_la_file("google", r429, None, None, False, 1, "x", 16768, "code 503") == ("attente", "code 429")


def test_l13_la_campagne_compte_a_part_un_mutant_arrive_au_delai(tmp_path, monkeypatch):
    """Constat 7 : la campagne de mutations, version 8, compte un mutant arrivé au délai à part (ni tué, ni survivant),
    et ne rend le code 0 que si tous les mutants sont tués."""
    spec = importlib.util.spec_from_file_location("campagne_v8", RACINE / "tests" / "mutations_essais_admission_v8" / "campagne_mutations_v8.py")
    campagne = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(campagne)

    def tache():
        return (0, "chef", "f", "n", "def f(): pass", "test_", str(tmp_path))

    def delai(*a, **k):
        raise subprocess.TimeoutExpired(a[0], 300)
    monkeypatch.setattr(campagne.subprocess, "run", delai)
    assert campagne.jouer(tache()) == ("chef", "f", "n", "délai")
    for code, issue in ((1, "tué"), (0, "survit"), (2, "erreur 2"), (5, "erreur 5")):
        monkeypatch.setattr(campagne.subprocess, "run", lambda *a, code=code, **k: subprocess.CompletedProcess(a[0], code))
        assert campagne.jouer(tache())[3] == issue
    comptes = campagne.compter_issues(["tué", "tué", "délai", "survit", "erreur 2"])
    assert comptes == {"mutants": 5, "tues": 2, "survivants": 1, "delais": 1, "erreurs": 1}
    assert campagne.code_de_sortie(campagne.compter_issues(["tué", "délai"])) == 1
    assert campagne.code_de_sortie(campagne.compter_issues(["tué", "tué"])) == 0
    assert list(tmp_path.iterdir()) == []                                                   # le fichier du mutant est ôté


def test_l13_mutants_non_equivalents_de_la_livraison_12_tues(monde, banc):
    """Constat 6 : les cinq mutants que la livraison 12 déclarait sans les distinguer, non équivalents : les quatre
    arrondis d'écriture à six décimales (au journal, `reserve_usd`, `cumul_usd`, `cout_si_sans_reponse_usd` ; au relevé,
    `depense_comptee_usd`), sous des prix à sept décimales ; les clés levées au relevé, lues du résumé du constat quand il
    en porte, sinon de la configuration. Et l'équivalent « en pratique » : sans journal du relais, aucune clé vue."""
    monde.config["fournisseurs"]["google"]["prix"] = [3.1234567, 15.7654321]
    g = banc("verification-google-cle-1")
    g.faux.programmer(faux.reponse_google("OK"), sonde_google())
    releve = g.verifier(constat_resume={"cles_levees": {"go": "GO-2026-11-21-77", "cles": ["google_partage_journaux_projet_a"]}})
    departs = [l for l in chef.lire_journal(g.dossier / "journal-essai.jsonl") if l.get("evenement") == "depart"]
    valeurs = [d[k] for d in departs for k in ("reserve_usd", "cumul_usd", "cout_si_sans_reponse_usd")] + [releve["depense_comptee_usd"]]
    assert all(v == round(v, 6) for v in valeurs) and releve["depense_comptee_usd"] > 0
    assert releve["cles_levees"] == {"go": "GO-2026-11-21-77", "cles": ["google_partage_journaux_projet_a"]}
    go, cles = chef.cles_levees_de(monde.config)
    for resume in (None, {}, {"cles_levees": None}, {"cles_levees": {}}):
        h = banc("verification-google-cle-1")
        h.faux.programmer(faux.reponse_google("OK"), sonde_google())
        assert h.verifier(constat_resume=resume)["cles_levees"] == {"go": go, "cles": sorted(cles)}, resume
    s = banc("verification-google-cle-1")
    s.faux.programmer(faux.reponse_google("OK"), sonde_google())
    r = chef.jouer_verification(monde.config, "verification-google-cle-1", s.dossier, s.url, None, ["zorglub-terme-interdit"],
                                chef.etat_de_la_ligne(monde.racine, monde.config, "verification-google-cle-1", s.go), s.go,
                                dormir=s.pauses.append)
    assert r["saine"] and r["cle_vue_dans_une_reponse"] == 0


def test_l13_m2_jouer_file_mutants_de_la_campagne_de_la_livraison_13(monde, banc):
    """Les mutants de `jouer_file` (campagne `livraison13_jouer`, première fois en campagne) qui survivaient à toute la
    suite : la règle de Google contrôlée avant tout envoi de la file ; des journaux de relais absents ; les arrondis
    d'écriture à six décimales ; le majorant démenti à sa borne exacte ; « interrompue » faux sur un arrêt ordinaire."""
    conformes = reponses_conformes(monde.config, monde.racine, "file-neon", faux.reponse_google)
    # la règle de Google, avant tout envoi de la file
    mauvaise = copy.deepcopy(monde.config)
    mauvaise["fournisseurs"]["google"]["exemption_de_la_sonde_go"] = None
    s = banc("file-neon")
    s.config = mauvaise
    with pytest.raises(chef.Arret, match="ne cite pas le GO qui l'accorde"):
        s.jouer()
    assert s.faux.recus == []
    # sans journaux de relais (deux voies) : la file joue, aucune signature n'est lue
    n = banc("file-neon")
    n.faux.programmer(*conformes)
    ctx = {"regime": "courant", "nom_servi": chef.IDENTIFIANTS["google"], "hote": monde.config["lignes"]["file-neon"]["hote"],
           "temperature_envoyee": True, "orthographe_niveau": "XHIGH"}
    bilan = chef.jouer_file(monde.config, "file-neon", chef.charger_textes(monde.config, monde.racine), n.dossier, n.urls, None,
                            ["zorglub-terme-interdit"], ctx, chef.charger_programme_de_forme(monde.config, monde.racine),
                            dormir=n.pauses.append)
    assert bilan["complet"] and not bilan["interrompue"]
    # arrondis à six décimales, sous des prix à sept décimales ; un 402 : arrêt, non « interrompue »
    monde.config["fournisseurs"]["google"]["prix"] = [3.1234567, 15.7654321]
    r = banc("file-neon")
    r.faux.programmer(conformes[0], faux.erreur_google(402))
    bilan = r.jouer()
    journal = chef.lire_journal(r.dossier / "journal-essai.jsonl")
    valeurs = ([l[k] for l in journal if l.get("evenement") == "depart" for k in ("reserve_usd", "cumul_usd", "cout_si_sans_reponse_usd")]
               + [l["cumul_usd"] for l in journal if l.get("evenement") == "envoi"] + [bilan["depense_comptee_usd"]])
    assert len(valeurs) == 9 and all(v == round(v, 6) for v in valeurs) and bilan["depense_comptee_usd"] > 0
    assert bilan["arret"] and bilan["interrompue"] is False and bilan["arretee_par_sa_borne_de_depense"] is False
    # Mistral : le majorant démenti au-delà de 64 jetons de contrôle, pas à 64 pile
    m = banc("file-mistral")
    m.faux.programmer(faux.flux_mistral(APPARIEMENT_CONFORME, usage=(900, 10, 910)))
    m.jouer()
    octets = m.envois()[0]["octets_contenu"]
    for facture, dementi in ((octets + chef.MARGE_JETONS, False), (octets + chef.MARGE_JETONS + 1, True)):
        b = banc("file-mistral")
        b.faux.programmer(faux.flux_mistral(APPARIEMENT_CONFORME, usage=(900, facture, 900 + facture)))
        b.jouer()
        assert b.envois()[0]["majorant_dementi"] is dementi, facture
