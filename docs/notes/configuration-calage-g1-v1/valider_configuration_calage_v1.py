#!/usr/bin/env python3
"""Validation de la configuration de génération du calage de la porte G1 (v1).

Ce programme contrôle que `prereg/configuration-generation-calage-g1-v1.json` est complet et cohérent :
- complet : toutes les entrées exigées sont là ; chacune dit sa valeur, sa nature et ses sources, ou porte la
  mention « choix, à faire valider » ; une valeur nulle porte un état, une méthode ou une règle, et le lieu où la
  valeur s'écrira ;
- sourcé : chaque source « chemin:ligne » est relue dans la pièce, à l'empreinte que donne la configuration, et
  l'extrait cité doit se trouver dans les lignes citées ;
- cohérent : révision complète, absence d'adaptateur, versions égales aux dépendances figées du dépôt, réglages
  dans les valeurs que connaît le harnais, plafonds du banc fermé tenus, forme de l'action et consigne égales à
  celles du code de l'environnement (a), vecteurs d'essai des graines reproduits, fichiers du harnais et programme
  de l'opérateur à l'empreinte citée.

Il ne télécharge rien, ne charge aucun modèle et n'écrit aucun fichier.

Emploi (depuis la racine du dépôt) :
    python docs/notes/configuration-calage-g1-v1/valider_configuration_calage_v1.py
    Options : `--configuration CHEMIN` ; `--racine CHEMIN` (racine du dépôt) ; `--lancement` (contrôle de lancement :
    les fichiers du harnais de l'arbre de travail doivent être ceux de la configuration) ; `--releve CHEMIN` (contrôle
    en plus un relevé de l'opérateur contre la configuration) ; `--comparer RELEVE_A RELEVE_B` (contrôle les deux
    relevés, puis exige l'égalité de tout ce qui doit être égal entre le poste de calage et le banc fermé) ; `--essai`
    (épreuves du programme sur le cas sain et sur des artefacts, R5).

Codes de sortie : 0 valide (ou épreuves toutes réussies) ; 1 refusée (ou une épreuve en échec) ; 2 erreur d'emploi.
Dépendances : la bibliothèque standard, numpy (chaîne des graines, R9) et git (relecture d'une pièce à un commit).
"""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

CHOIX = "choix, à faire valider"
OPERATEUR = "A_CALCULER_PAR_L_OPERATEUR"
LANCEMENT = "A_REMPLIR_AU_COMMIT_DE_LANCEMENT"
NATURES = ("décidé", "repris d'une pièce scellée", "repris d'un texte non scellé", "lu dans le code", "choix neuf")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
HEX40 = re.compile(r"^[0-9a-f]{40}$")          # même règle que le harnais (modeles.py, COMMIT)
SOURCE = re.compile(r"^(?P<chemin>.+):(?P<debut>\d+)(?:-(?P<fin>\d+))?$")
MODELE = "meta-llama/Llama-3.1-8B-Instruct"
NOYAUX = ("defaut", "math")                    # valeurs que connaît le harnais (lanceurs, NOYAUX)
STATISTIQUES = {"max": None, "q99": 0.99}      # statistique de la garde d'équivalence et son quantile
N_COUCHES = 32                                 # Llama-3.1-8B-Instruct : 32 blocs (T0.7 scellé, « sur 32 »)
MARQUES_INTERDITES = ("À REMPLIR", "A REMPLIR", "<<", "TODO")
CLES_DU_HAUT = ("objet", "version", "statut", "auteur", "date_utc", "mot_de_lazar", "portee", "regles_de_lecture",
                "lecture_des_sources", "parametres", "coherence_avec_le_banc_ferme", "ce_qui_reste_ouvert",
                "pieces_citees")
# Liste fermée des entrées exigées : ce que demandent le mot de Lazar (GO-2026-11-21-77), l'attestation du lecteur
# neuf et le champ n° 2 du préenregistrement du banc fermé.
EXIGEES = {
    "modele": ("nom", "revision", "adaptateur", "interventions_sur_les_activations", "poids", "fichiers_du_modele"),
    "pile_d_inference": ("bibliotheque", "versions", "torch_construction", "python", "precision_des_poids",
                         "implementation_de_l_attention", "noyau_attention", "appareil", "fils", "determinisme",
                         "materiel"),
    "gabarit_de_conversation": ("origine", "roles", "variables", "texte_attendu_dans_l_ouverture",
                                "arguments_du_gabarit", "cloture_d_un_tour", "jetons_d_arret", "jeton_de_remplissage",
                                "empreinte"),
    "echantillonnage": ("temperature", "troncature", "tirage", "jetons_par_action_max", "arret_d_une_action"),
    "episode": ("nombre_d_agents", "nombre_de_pas", "lot", "plan_des_lots"),
    "environnement": ("nom", "classe", "condition", "consigne_privee", "observation", "forme_de_l_action",
                      "forme_d_une_tache", "guide_de_classification", "produit_d_un_episode"),
    "outils": ("outils_exposes", "forme", "correspondance_avec_les_cinq_outils_du_banc_ferme"),
    "graines": ("bibliotheque", "racine", "cle_d_un_episode", "derivation_par_action", "generateur_de_l_action",
                "vecteurs_d_essai"),
    "garde_d_equivalence": ("fraction_des_actions", "statistique", "quantile", "tolerance", "mode", "controle_negatif"),
    "enregistrement": ("couches", "definition_d_une_couche", "lieu_de_lecture", "type_de_capture"),
    "harnais": ("depot", "commit", "fichiers", "fonctions_de_montage"),
}
ETATS_ATTENDUS = {OPERATEUR: {"modele.fichiers_du_modele", "pile_d_inference.torch_construction",
                              "pile_d_inference.python", "gabarit_de_conversation.jetons_d_arret",
                              "gabarit_de_conversation.jeton_de_remplissage", "gabarit_de_conversation.empreinte"},
                  LANCEMENT: {"harnais.commit"}}
VERSIONS_EXIGEES = ("transformers", "torch", "tokenizers", "safetensors", "huggingface_hub", "numpy")
# Ce qui doit être égal entre le relevé du poste de calage et celui du banc fermé (pile déclarée). La date, les
# chemins et le nom du système du poste ne sont pas comparés.
EGAUX_ENTRE_POSTES = ("mode", "configuration.sha256", "programme.sha256", "modele.nom", "modele.revision",
                      "modele.fichiers", "gabarit_de_conversation", "environnement", "harnais.fichiers", "graines.conforme",
                      "versions.python", "versions.implementation", "versions.machine", "versions.capacite_du_processeur",
                      "versions.numpy", "versions.torch", "versions.torch_construction", "versions.torch_cuda",
                      "versions.transformers", "versions.tokenizers", "versions.safetensors", "versions.huggingface_hub",
                      "versions.jinja2")
ENV_A = "src/controle_ia/environnements/propositions.py"
DEPENDANCES = "requirements-cpu.txt"


def sha256(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def est_entier(x) -> bool:
    return isinstance(x, int) and not isinstance(x, bool)


def est_reel(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


class Controle:
    """Un passage de contrôle : il accumule les défauts, sans jamais s'arrêter au premier ni en taire un."""

    def __init__(self, config: dict, racine: Path, lancement: bool = False):
        self.c, self.racine, self.lancement = config, Path(racine), lancement
        self.defauts: list[tuple[str, str]] = []
        self.avis: list[str] = []
        self.compte = {"entrees": 0, "sources": 0, "pieces": 0}
        self._pieces: dict[str, bytes | None] = {}

    def defaut(self, ou: str, quoi: str) -> None:
        self.defauts.append((ou, quoi))

    # ------------------------------------------------------------ lecture des pièces
    def _git(self, commit: str, chemin: str) -> bytes | None:
        if not (isinstance(commit, str) and HEX40.match(commit)):
            return None                                        # sans commit complet, git lirait l'index : refus
        r = subprocess.run(["git", "-C", str(self.racine), "show", f"{commit}:{chemin}"], capture_output=True)
        return r.stdout if r.returncode == 0 else None

    def piece(self, chemin: str) -> bytes | None:
        """Contenu d'une pièce citée, à l'empreinte que donne la configuration. Arbre de travail d'abord ; à défaut, la
        pièce à son commit (branche citée, ou commit de lecture des sources). Un échec est un défaut, jamais un repli."""
        if chemin in self._pieces:
            return self._pieces[chemin]
        fiche = self.c.get("pieces_citees", {}).get(chemin)
        contenu = None
        if not isinstance(fiche, dict) or not fiche.get("nature"):
            self.defaut(f"pieces_citees.{chemin}", "pièce citée par une source mais absente de « pieces_citees », ou sans nature")
        else:
            attendue = fiche.get("sha256")
            vivant = attendue is None
            if vivant != (fiche.get("vivant") is True):
                self.defaut(f"pieces_citees.{chemin}", "empreinte absente pour une pièce qui n'est pas dite vivante, ou "
                                                       "pièce dite vivante qui porte une empreinte")
            elif not vivant and not (isinstance(attendue, str) and HEX64.match(attendue)):
                self.defaut(f"pieces_citees.{chemin}", "empreinte qui n'est pas un sha256")
            else:
                commit_lecture = self.c.get("lecture_des_sources", {}).get("commit", "")
                candidats = []
                if "commit" in fiche:                      # pièce d'une autre branche : lue à son propre commit
                    candidats.append(("commit de la pièce", lambda: self._git(fiche["commit"], chemin)))
                else:
                    f = self.racine / chemin
                    candidats.append(("arbre de travail", lambda: f.read_bytes() if f.is_file() else None))
                    candidats.append(("commit de lecture", lambda: self._git(commit_lecture, chemin)))
                for nom, lire in candidats:
                    octets = lire()
                    if octets is not None and (vivant or sha256(octets) == attendue):
                        contenu = octets
                        if nom == "commit de lecture":
                            self.avis.append(f"{chemin} a changé dans l'arbre de travail : relue au commit de lecture")
                        break
                if contenu is None:
                    self.defaut(f"pieces_citees.{chemin}",
                                "pièce introuvable à l'empreinte citée (ni dans l'arbre de travail ni au commit cité ; "
                                "si l'objet git manque, faire `git fetch` de sa branche)")
                else:
                    self.compte["pieces"] += 1
        self._pieces[chemin] = contenu
        return contenu

    def source(self, ou_entree: str, s) -> None:
        if not isinstance(s, dict) or not isinstance(s.get("ou"), str) or not isinstance(s.get("extrait"), str) \
                or not s["extrait"].strip():
            self.defaut(ou_entree, f"source mal formée : {s!r}")
            return
        m = SOURCE.match(s["ou"])
        if not m:
            self.defaut(ou_entree, f"source {s['ou']!r} : « chemin:ligne » ou « chemin:début-fin » attendu")
            return
        debut, fin = int(m["debut"]), int(m["fin"] or m["debut"])
        if debut < 1 or fin < debut:
            self.defaut(ou_entree, f"source {s['ou']!r} : lignes incohérentes")
            return
        octets = self.piece(m["chemin"])
        if octets is None:
            return                                             # le défaut est déjà dit, pour la pièce
        lignes = octets.decode("utf-8", errors="replace").split("\n")
        vivant = self.c["pieces_citees"][m["chemin"]].get("sha256") is None
        if s["extrait"] not in "\n".join(lignes[debut - 1:fin]) and vivant:
            # document vivant : la ligne a pu bouger depuis la lecture ; on relit au commit de lecture
            ancien = self._git(self.c.get("lecture_des_sources", {}).get("commit", ""), m["chemin"])
            lignes = ancien.decode("utf-8", errors="replace").split("\n") if ancien is not None else lignes
        if s["extrait"] not in "\n".join(lignes[debut - 1:fin]):
            self.defaut(ou_entree, f"source {s['ou']} : l'extrait {s['extrait'][:60]!r} n'est pas dans les lignes citées")
            return
        self.compte["sources"] += 1

    # ------------------------------------------------------------ accès aux entrées
    def entrees(self):
        for section, contenu in self.c.get("parametres", {}).items():
            if isinstance(contenu, dict):
                for nom, e in contenu.items():
                    yield f"{section}.{nom}", e

    def v(self, section: str, nom: str):
        """Valeur d'une entrée ; None si l'entrée manque (le défaut est alors dit par `completude`)."""
        e = self.c.get("parametres", {}).get(section, {}).get(nom)
        return e.get("valeur") if isinstance(e, dict) else None

    # ------------------------------------------------------------ complétude et forme des entrées
    def completude(self) -> None:
        for cle in CLES_DU_HAUT:
            if cle not in self.c:
                self.defaut(cle, "rubrique exigée absente")
        par = self.c.get("parametres")
        if not isinstance(par, dict):
            self.defaut("parametres", "rubrique absente ou mal formée")
            return
        for section, noms in EXIGEES.items():
            for nom in noms:
                if not isinstance(par.get(section), dict) or nom not in par[section]:
                    self.defaut(f"{section}.{nom}", "entrée exigée absente")
        for ou, e in self.entrees():
            self.compte["entrees"] += 1
            if not isinstance(e, dict) or "valeur" not in e:
                self.defaut(ou, "entrée sans champ « valeur »")
                continue
            nature = e.get("nature")
            if nature not in NATURES:
                self.defaut(ou, f"nature {nature!r} hors de la liste {NATURES}")
            sources = e.get("sources")
            if not isinstance(sources, list):
                self.defaut(ou, "champ « sources » absent ou mal formé")
                sources = []
            if nature != "décidé" and e.get("mention") != CHOIX:
                self.defaut(ou, f"mention « {CHOIX} » absente alors que la valeur n'est pas décidée")
            if not sources and nature != "choix neuf":
                self.defaut(ou, "sans source, alors que la nature n'est pas « choix neuf »")
            if not sources and e.get("mention") != CHOIX:
                self.defaut(ou, f"sans source et sans la mention « {CHOIX} »")
            for s in sources:
                self.source(ou, s)
            self._etat(ou, e)
            self._marques(ou, e)

    def _etat(self, ou: str, e: dict) -> None:
        etat = e.get("etat")
        if etat is None:
            if e["valeur"] is None:
                self.defaut(ou, "valeur nulle sans état : rien ne dit qui la remplit ni quand")
            if any(ou in attendus for attendus in ETATS_ATTENDUS.values()):
                self.defaut(ou, "entrée qui doit rester à remplir hors de ce fichier, sans état")
            return
        if etat not in ETATS_ATTENDUS:
            self.defaut(ou, f"état {etat!r} inconnu")
            return
        if e["valeur"] is not None:
            self.defaut(ou, "la valeur doit rester nulle : elle s'écrit hors de ce fichier, qui ne change plus (R12)")
        if ou not in ETATS_ATTENDUS[etat]:
            self.defaut(ou, f"état {etat} inattendu pour cette entrée : une valeur fixée est exigée ici")
        if not (isinstance(e.get("ou_s_ecrit_la_valeur"), str) and e["ou_s_ecrit_la_valeur"].strip()):
            self.defaut(ou, "lieu où s'écrit la valeur non dit")
        if etat == OPERATEUR:
            if not e.get("methode"):
                self.defaut(ou, "valeur laissée à l'opérateur sans méthode de calcul")
            champs = e.get("champs_du_releve")
            if not (isinstance(champs, list) and champs and all(isinstance(x, str) and x for x in champs)):
                self.defaut(ou, "valeur laissée à l'opérateur sans champ du relevé")
        if etat == LANCEMENT:
            regle = e.get("regle")
            if not (isinstance(regle, list) and regle and all(isinstance(x, str) and x.strip() for x in regle)):
                self.defaut(ou, "valeur à remplir au lancement sans règle")

    def _marques(self, ou: str, e: dict) -> None:
        texte = json.dumps(e, ensure_ascii=False)
        for marque in MARQUES_INTERDITES:
            if marque in texte:
                self.defaut(ou, f"marqueur {marque!r} : une valeur à remplir se dit par un état, pas par un texte")

    # ------------------------------------------------------------ cohérence des valeurs
    def coherence(self) -> None:
        v = self.v
        if v("modele", "nom") != MODELE:
            self.defaut("modele.nom", f"modèle {v('modele', 'nom')!r} : {MODELE} attendu (changer de modèle exige un GO)")
        rev = v("modele", "revision")
        if not (isinstance(rev, str) and HEX40.match(rev)):
            self.defaut("modele.revision", "révision qui n'est pas un commit complet (40 caractères hexadécimaux)")
        if v("modele", "adaptateur") != "aucun":
            self.defaut("modele.adaptateur", f"adaptateur {v('modele', 'adaptateur')!r} : « aucun » attendu (agent nu)")
        if v("modele", "interventions_sur_les_activations") != "aucune":
            self.defaut("modele.interventions_sur_les_activations", "« aucune » attendu")
        self._versions()
        if v("pile_d_inference", "precision_des_poids") != "bfloat16":
            self.defaut("pile_d_inference.precision_des_poids", "précision autre que bfloat16 : le harnais refuse la conversion")
        if v("pile_d_inference", "noyau_attention") not in NOYAUX:
            self.defaut("pile_d_inference.noyau_attention", f"noyau {v('pile_d_inference', 'noyau_attention')!r} hors de {NOYAUX}")
        if not (est_entier(v("pile_d_inference", "fils")) and v("pile_d_inference", "fils") >= 1):
            self.defaut("pile_d_inference.fils", "nombre de fils : entier au moins égal à 1 attendu")
        materiel = v("pile_d_inference", "materiel")
        if not (isinstance(materiel, dict) and materiel.get("regle") and isinstance(materiel.get("domaine_revalide"), dict)):
            self.defaut("pile_d_inference.materiel", "règle d'égalité des deux postes ou domaine revalidé absents")
        self._gabarit()
        t = v("echantillonnage", "temperature")
        if not (est_reel(t) and t > 0):
            self.defaut("echantillonnage.temperature", f"température {t!r} : un nombre strictement positif attendu")
        if v("echantillonnage", "troncature") != "aucune":
            self.defaut("echantillonnage.troncature", "troncature autre que « aucune » : le harnais tire dans la loi entière")
        n, pas, lot = v("episode", "nombre_d_agents"), v("episode", "nombre_de_pas"), v("episode", "lot")
        jetons = v("echantillonnage", "jetons_par_action_max")
        for ou, x in (("episode.nombre_d_agents", n), ("episode.nombre_de_pas", pas), ("episode.lot", lot),
                      ("echantillonnage.jetons_par_action_max", jetons)):
            if not (est_entier(x) and x >= 1):
                self.defaut(ou, f"valeur {x!r} : entier au moins égal à 1 attendu")
        self._plafonds(n, pas, jetons)
        self._environnement(pas)
        self._outils()
        self._graines(n, pas)
        self._garde()
        self._couches()
        self._harnais()
        commit = self.c.get("lecture_des_sources", {}).get("commit")
        if not (isinstance(commit, str) and HEX40.match(commit)):
            self.defaut("lecture_des_sources.commit", "commit de lecture qui n'est pas un commit complet")
        mot = self.c.get("mot_de_lazar", {})
        self.source("mot_de_lazar", {"ou": mot.get("ou", ""), "extrait": mot.get("go", "") or "?"})
        cites = {SOURCE.match(s["ou"])["chemin"] for _, e in self.entrees() if isinstance(e, dict)
                 for s in e.get("sources", []) if isinstance(s, dict) and SOURCE.match(str(s.get("ou", "")))}
        cites |= {SOURCE.match(s["ou"])["chemin"] for s in self.c.get("coherence_avec_le_banc_ferme", {}).get("sources", [])
                  if isinstance(s, dict) and SOURCE.match(str(s.get("ou", "")))}
        if SOURCE.match(str(mot.get("ou", ""))):
            cites.add(SOURCE.match(mot["ou"])["chemin"])
        for chemin in self.c.get("pieces_citees", {}):
            if chemin not in cites:
                self.defaut(f"pieces_citees.{chemin}", "pièce qu'aucune source ne cite")

    def _versions(self) -> None:
        versions = self.v("pile_d_inference", "versions")
        if not isinstance(versions, dict):
            self.defaut("pile_d_inference.versions", "table des versions absente")
            return
        dependances = self.piece(DEPENDANCES) if DEPENDANCES in self.c.get("pieces_citees", {}) else None
        if dependances is None:
            self.defaut("pile_d_inference.versions", f"{DEPENDANCES} n'est pas une pièce citée lisible : versions non vérifiables")
            return
        lignes = {ligne.strip() for ligne in dependances.decode("utf-8").split("\n")}
        for b in VERSIONS_EXIGEES:
            if b not in versions:
                self.defaut("pile_d_inference.versions", f"version de {b} absente")
        for b, version in versions.items():
            if f"{b}=={version}" not in lignes:
                self.defaut("pile_d_inference.versions", f"{b} {version} : pas de ligne « {b}=={version} » dans {DEPENDANCES}")

    def _gabarit(self) -> None:
        v = self.v
        variables, attendu = v("gabarit_de_conversation", "variables"), v("gabarit_de_conversation", "texte_attendu_dans_l_ouverture")
        if not (isinstance(variables, dict) and isinstance(variables.get("date_string"), str) and variables["date_string"]):
            self.defaut("gabarit_de_conversation.variables", "variable « date_string » absente : la date du gabarit doit être figée")
        elif not (isinstance(attendu, str) and variables["date_string"] in attendu):
            self.defaut("gabarit_de_conversation.texte_attendu_dans_l_ouverture", "le texte attendu ne porte pas la date figée du gabarit")
        if v("gabarit_de_conversation", "roles") != {"consigne_privee": "system", "observation": "user", "action": "assistant"}:
            self.defaut("gabarit_de_conversation.roles", "rôles différents de ceux du harnais (system, user, assistant)")
        arguments = v("gabarit_de_conversation", "arguments_du_gabarit")
        if not (isinstance(arguments, dict) and arguments.get("tools") == "absent" and arguments.get("documents") == "absent"):
            self.defaut("gabarit_de_conversation.arguments_du_gabarit", "un argument d'outils ou de documents passerait au gabarit")
        methode = (self.c.get("parametres", {}).get("gabarit_de_conversation", {}).get("empreinte") or {}).get("methode")
        if not isinstance(methode, dict):
            self.defaut("gabarit_de_conversation.empreinte", "méthode de l'empreinte du gabarit : un programme et son empreinte sont attendus")
            return
        programme, attendue = methode.get("programme"), methode.get("programme_sha256")
        f = self.racine / str(programme)
        if not (isinstance(attendue, str) and HEX64.match(attendue)):
            self.defaut("gabarit_de_conversation.empreinte", "empreinte du programme de l'opérateur absente")
        elif not f.is_file():
            self.defaut("gabarit_de_conversation.empreinte", f"programme de l'opérateur absent : {programme}")
        elif sha256(f.read_bytes()) != attendue:
            self.defaut("gabarit_de_conversation.empreinte", "programme de l'opérateur d'une autre empreinte que celle de la configuration")
        if not (isinstance(methode.get("trois_empreintes"), dict) and len(methode["trois_empreintes"]) == 3):
            self.defaut("gabarit_de_conversation.empreinte", "les trois empreintes du gabarit ne sont pas définies")

    def _plafonds(self, n, pas, jetons) -> None:
        plafonds = self.c.get("coherence_avec_le_banc_ferme", {})
        for s in plafonds.get("sources", []):
            self.source("coherence_avec_le_banc_ferme", s)
        p = plafonds.get("plafonds")
        cles = ("pas_par_episode", "jetons_par_action", "jetons_par_episode")
        if not (isinstance(p, dict) and all(est_entier(p.get(k)) for k in cles)):
            self.defaut("coherence_avec_le_banc_ferme", "plafonds du banc fermé absents")
            return
        if not all(est_entier(x) for x in (n, pas, jetons)):
            return
        if n * pas > p["pas_par_episode"]:
            self.defaut("episode.nombre_de_pas", f"{n * pas} actions par épisode : plafond du banc fermé de {p['pas_par_episode']} dépassé")
        if jetons > p["jetons_par_action"]:
            self.defaut("echantillonnage.jetons_par_action_max", f"{jetons} jetons par action : plafond du banc fermé de {p['jetons_par_action']} dépassé")
        if n * pas * jetons > p["jetons_par_episode"]:
            self.defaut("echantillonnage.jetons_par_action_max", f"{n * pas * jetons} jetons par épisode : plafond du banc fermé de {p['jetons_par_episode']} dépassé")

    def _constantes_de_l_environnement(self) -> dict | None:
        """Constantes du code de l'environnement (a), lues dans le fichier gelé sans l'exécuter."""
        octets = self._fichier_du_harnais(ENV_A)
        if octets is None:
            return None
        sortie = {}
        for noeud in ast.parse(octets.decode("utf-8")).body:
            if isinstance(noeud, ast.Assign) and len(noeud.targets) == 1 and isinstance(noeud.targets[0], ast.Name) \
                    and noeud.targets[0].id in ("TAILLE_MAX", "CHAMPS", "CHAMPS_EXIGES", "CONSIGNE_HONNETE", "FORMAT_ACTION"):
                sortie[noeud.targets[0].id] = ast.literal_eval(noeud.value)
        return sortie if len(sortie) == 5 else None

    def _environnement(self, pas) -> None:
        constantes = self._constantes_de_l_environnement()
        if constantes is None:
            self.defaut("environnement", f"{ENV_A} illisible à l'empreinte de la configuration : forme de l'action non vérifiable")
            return
        forme = self.v("environnement", "forme_de_l_action")
        if not isinstance(forme, dict) or forme.get("champs") != list(constantes["CHAMPS"]) \
                or forme.get("champs_exiges") != list(constantes["CHAMPS_EXIGES"]) \
                or forme.get("taille_max_de_l_ensemble") != constantes["TAILLE_MAX"]:
            self.defaut("environnement.forme_de_l_action", "champs, champs exigés ou taille de l'ensemble différents de ceux du code de l'environnement (a)")
        elif "sans appel d'outil" not in str(forme.get("nature")):
            self.defaut("environnement.forme_de_l_action", "la forme de l'action ne dit pas qu'elle est sans appel d'outil")
        consigne = self.v("environnement", "consigne_privee")
        if not isinstance(consigne, dict) or not est_entier(pas):
            self.defaut("environnement.consigne_privee", "consigne privée non décrite")
        else:
            if consigne.get("consigne_honnete_T10_sha256") != sha256(constantes["CONSIGNE_HONNETE"].format(T=pas).encode("utf-8")):
                self.defaut("environnement.consigne_privee", "empreinte de la consigne honnête différente de celle du code, au nombre de pas de la configuration")
            if consigne.get("format_d_action_sha256") != sha256(constantes["FORMAT_ACTION"].encode("utf-8")):
                self.defaut("environnement.consigne_privee", "empreinte du format d'action différente de celle du code")
        guide = self.v("environnement", "guide_de_classification")
        geles = self.v("harnais", "fichiers") or {}
        if not isinstance(guide, dict) or geles.get(guide.get("chemin")) != guide.get("sha256") or not guide.get("sha256"):
            self.defaut("environnement.guide_de_classification", "guide de classification absent des fichiers gelés, ou d'une autre empreinte")
        tache = self.v("environnement", "forme_d_une_tache")
        if not isinstance(tache, dict) or tache.get("piece_remise_sur_demande") != "aucune":
            self.defaut("environnement.forme_d_une_tache", "la forme d'une tâche doit dire qu'aucune pièce n'est remise sur demande")

    def _outils(self) -> None:
        outils = self.v("outils", "outils_exposes")
        if outils != []:
            self.defaut("outils.outils_exposes", f"outil exposé {outils!r} : l'environnement (a) n'a pas d'appel d'outil, la liste doit être vide")
        table = self.v("outils", "correspondance_avec_les_cinq_outils_du_banc_ferme")
        if not isinstance(table, dict) or sorted(table) != ["O1", "O2", "O3", "O4", "O5"]:
            self.defaut("outils.correspondance_avec_les_cinq_outils_du_banc_ferme", "les cinq outils O1 à O5 ne sont pas tous lus")
        elif table["O4"] != "non offert":
            self.defaut("outils.correspondance_avec_les_cinq_outils_du_banc_ferme", "O4 doit être « non offert » dans la forme du calage")

    def _graines(self, n, pas) -> None:
        vecteurs = self.v("graines", "vecteurs_d_essai")
        fraction = self.v("garde_d_equivalence", "fraction_des_actions")
        if not (isinstance(vecteurs, list) and vecteurs):
            self.defaut("graines.vecteurs_d_essai", "aucun vecteur d'essai")
            return
        try:
            import numpy as np
        except ImportError:
            self.defaut("graines.vecteurs_d_essai", "numpy absent : chaîne des graines non vérifiée (aucun repli)")
            return
        if tuple(int(x) for x in re.findall(r"\d+", np.__version__)[:2]) < (1, 25):
            self.defaut("graines.vecteurs_d_essai", f"numpy {np.__version__} : R9 exige au moins 1.25")
            return
        for k, vec in enumerate(vecteurs):
            ou = f"graines.vecteurs_d_essai[{k}]"
            try:
                if (vec["N"], vec["T"]) != (n, pas):
                    self.defaut(ou, "vecteur d'essai d'une autre forme (agents, pas) que la configuration")
                    continue
                ss = np.random.SeedSequence(entropy=int(vec["entropie"]), spawn_key=tuple(int(x) for x in vec["cle"]))
                g = np.random.default_rng(ss)
                valeurs = [int(x) for x in g.integers(0, 2 ** 31 - 1, size=vec["N"] * vec["T"])]
                tirages = g.random(vec["N"] * vec["T"])
                echantillon = [i for i in range(vec["N"] * vec["T"]) if tirages[i] < fraction]
                if valeurs != vec["graines"] or [int(x) for x in ss.generate_state(2)] != vec["etat_de_controle"] \
                        or echantillon != vec["echantillon_de_la_garde"]:
                    self.defaut(ou, "vecteur d'essai des graines non reproduit par numpy.random.SeedSequence")
            except (KeyError, TypeError, ValueError) as e:
                self.defaut(ou, f"vecteur d'essai mal formé ({type(e).__name__})")

    def _garde(self) -> None:
        v = self.v
        fraction, stat, quantile, tol = (v("garde_d_equivalence", k) for k in ("fraction_des_actions", "statistique", "quantile", "tolerance"))
        if not (est_reel(fraction) and 0 < fraction <= 1):
            self.defaut("garde_d_equivalence.fraction_des_actions", "fraction hors de ]0 ; 1]")
        if stat not in STATISTIQUES:
            self.defaut("garde_d_equivalence.statistique", f"statistique {stat!r} hors de {tuple(STATISTIQUES)}")
        elif STATISTIQUES[stat] != quantile:
            self.defaut("garde_d_equivalence.quantile", f"quantile {quantile!r} incohérent avec la statistique {stat}")
        if not (est_reel(tol) and tol > 0):
            self.defaut("garde_d_equivalence.tolerance", "tolérance : un nombre strictement positif attendu")
        cn = v("garde_d_equivalence", "controle_negatif")
        if not (isinstance(cn, dict) and est_entier(cn.get("positions_min")) and est_entier(cn.get("actions_min"))
                and est_reel(cn.get("fraction_min")) and 0 < cn["fraction_min"] <= 1):
            self.defaut("garde_d_equivalence.controle_negatif", "contrôle négatif mal défini")

    def _couches(self) -> None:
        couches = self.v("enregistrement", "couches")
        if not (isinstance(couches, list) and couches and all(est_entier(x) for x in couches)):
            self.defaut("enregistrement.couches", "liste de couches absente")
        elif couches != sorted(set(couches)) or couches[0] < 0 or couches[-1] >= N_COUCHES:
            self.defaut("enregistrement.couches", f"couche hors de [0 ; {N_COUCHES}[, en double ou hors d'ordre : {couches}")

    def _fichier_du_harnais(self, chemin: str) -> bytes | None:
        """Fichier gelé, à l'empreinte de la configuration : arbre de travail, sinon commit de lecture."""
        attendue = (self.v("harnais", "fichiers") or {}).get(chemin)
        f = self.racine / chemin
        if f.is_file() and sha256(f.read_bytes()) == attendue:
            return f.read_bytes()
        ancien = self._git(self.c.get("lecture_des_sources", {}).get("commit", ""), chemin)
        return ancien if ancien is not None and sha256(ancien) == attendue else None

    def _harnais(self) -> None:
        fichiers = self.v("harnais", "fichiers")
        if not (isinstance(fichiers, dict) and fichiers):
            self.defaut("harnais.fichiers", "liste des fichiers gelés absente")
            return
        for chemin, attendue in sorted(fichiers.items()):
            if not (isinstance(attendue, str) and HEX64.match(attendue)):
                self.defaut("harnais.fichiers", f"{chemin} : empreinte qui n'est pas un sha256")
                continue
            f = self.racine / chemin
            dans_l_arbre = f.is_file() and sha256(f.read_bytes()) == attendue
            if dans_l_arbre:
                continue
            if self.lancement:
                self.defaut("harnais.fichiers", f"{chemin} : le fichier de l'arbre de travail n'est pas celui de la configuration (contrôle de lancement)")
            elif self._fichier_du_harnais(chemin) is None:
                self.defaut("harnais.fichiers", f"{chemin} : fichier du harnais introuvable à l'empreinte citée")
            else:
                self.avis.append(f"{chemin} a changé depuis la configuration : un lancement depuis cet arbre ne la jouerait pas")
        montage = self.v("harnais", "fonctions_de_montage")
        if not (isinstance(montage, dict) and montage):
            self.defaut("harnais.fonctions_de_montage", "liste des fonctions de montage absente")
            return
        for nom, ou in montage.items():
            m = SOURCE.match(str(ou))
            if not m or not (self.racine / m["chemin"]).is_file():
                self.defaut("harnais.fonctions_de_montage", f"{nom} : lieu {ou!r} illisible")

    # ------------------------------------------------------------ relevé de l'opérateur
    def releve(self, releve: dict, sha_config: str) -> None:
        def lire(chemin: str):
            return lire_champ(releve, chemin)

        if releve.get("mode") != "reel":
            self.defaut("relevé", f"mode {releve.get('mode')!r} : un relevé au tokeniseur jouet ne vaut pour aucune mesure")
        if lire("configuration.sha256") != sha_config:
            self.defaut("relevé", "relevé établi pour une autre configuration (empreinte différente)")
        methode = (self.c.get("parametres", {}).get("gabarit_de_conversation", {}).get("empreinte") or {}).get("methode") or {}
        if lire("programme.sha256") != methode.get("programme_sha256"):
            self.defaut("relevé", "relevé établi par un autre programme que celui de la configuration")
        if (lire("modele.nom"), lire("modele.revision")) != (self.v("modele", "nom"), self.v("modele", "revision")):
            self.defaut("relevé", "modèle ou révision du relevé différents de ceux de la configuration")
        for ou, e in self.entrees():
            if isinstance(e, dict) and e.get("etat") == OPERATEUR:
                for champ in e.get("champs_du_releve", []):
                    if lire(champ) in (None, "", [], {}):
                        self.defaut("relevé", f"champ « {champ} » absent du relevé (entrée {ou})")
        for champ in ("gabarit_de_conversation.gabarit_sha256", "gabarit_de_conversation.conversation_de_controle.ids_sha256",
                      "gabarit_de_conversation.conversation_de_controle.texte_sha256"):
            if not (isinstance(lire(champ), str) and HEX64.match(lire(champ))):
                self.defaut("relevé", f"champ « {champ} » : sha256 attendu")
        arrets = lire("gabarit_de_conversation.jetons_d_arret")
        if not (isinstance(arrets, list) and arrets and all(est_entier(x) for x in arrets)):
            self.defaut("relevé", "jetons d'arrêt : liste non vide d'identifiants attendue")
        for champ in ("gabarit_de_conversation.conversation_de_controle.format_verifie",
                      "gabarit_de_conversation.texte_attendu_dans_l_ouverture.verifie",
                      "harnais.conforme_a_la_configuration", "graines.conforme", "versions_conformes_a_la_configuration",
                      "modele.poids_releves"):
            if lire(champ) is not True:
                self.defaut("relevé", f"champ « {champ} » : « vrai » attendu")
        fichiers = lire("modele.fichiers")
        if isinstance(fichiers, dict):
            for nom, f in fichiers.items():
                if not (isinstance(f, dict) and isinstance(f.get("sha256"), str) and HEX64.match(f["sha256"])):
                    self.defaut("relevé", f"fichier du modèle « {nom} » sans empreinte")


def lire_champ(releve: dict, chemin: str):
    x = releve
    for cle in chemin.split("."):
        x = x.get(cle) if isinstance(x, dict) else None
    return x


def comparer_deux_releves(a: dict, b: dict) -> list[str]:
    """Champs qui diffèrent entre deux relevés, parmi ceux qui doivent être égaux ; un champ absent des deux côtés
    compte comme un écart (rien n'est égal par défaut)."""
    ecarts = []
    for champ in EGAUX_ENTRE_POSTES:
        x, y = lire_champ(a, champ), lire_champ(b, champ)
        if x is None or y is None:
            ecarts.append(f"{champ} : absent d'un relevé")
        elif x != y:
            if isinstance(x, dict) and isinstance(y, dict):
                cles = sorted(k for k in set(x) | set(y) if x.get(k) != y.get(k))
                ecarts.append(f"{champ} : diffère sur {', '.join(cles[:6])}")
            else:
                ecarts.append(f"{champ} : {x!r} contre {y!r}")
    return ecarts


def charger(texte: str) -> dict:
    try:
        config = json.loads(texte)
    except json.JSONDecodeError as e:
        raise ValueError(f"configuration illisible (JSON) : {e}") from None
    if not isinstance(config, dict):
        raise ValueError("configuration illisible : un objet JSON est attendu")
    return config


def controler(config: dict, racine: Path, lancement: bool = False) -> Controle:
    c = Controle(config, racine, lancement)
    c.completude()
    c.coherence()
    return c


def verifier_le_compagnon(chemin: Path) -> tuple[str, str | None]:
    """Empreinte du fichier, et défaut éventuel de son empreinte compagnon."""
    obtenue = sha256(chemin.read_bytes())
    compagnon = Path(str(chemin) + ".sha256")
    if not compagnon.is_file():
        return obtenue, "empreinte compagnon absente : le fichier n'est pas scellé"
    champs = compagnon.read_text(encoding="utf-8").split()
    if len(champs) != 2 or champs[0] != obtenue or champs[1] != chemin.name:
        return obtenue, "empreinte compagnon différente du fichier, ou d'un autre nom"
    return obtenue, None


# ---------------------------------------------------------------- épreuves du programme (R5)

def essai(config: dict, racine: Path, sha_config: str) -> int:
    """Le cas sain doit passer sans défaut ; chaque artefact doit être refusé pour le motif attendu."""
    echecs = 0

    def dire(nom: str, reussi: bool, detail: str) -> None:
        nonlocal echecs
        echecs += 0 if reussi else 1
        print(f"{'réussi' if reussi else 'ÉCHEC '} | {nom} | {detail}")

    sain = controler(config, racine)
    dire("cas sain : la configuration du dépôt", not sain.defauts,
         f"{sain.compte['entrees']} entrées, {sain.compte['sources']} sources, {sain.compte['pieces']} pièces, "
         f"{len(sain.defauts)} défaut(s)" + ("" if not sain.defauts else f" : {sain.defauts[0]}"))

    def artefact(nom: str, motif: str, alterer) -> None:
        faux = copy.deepcopy(config)
        alterer(faux["parametres"], faux)
        trouves = [f"{ou} : {quoi}" for ou, quoi in controler(faux, racine).defauts]
        vus = [d for d in trouves if motif in d]
        dire(f"artefact : {nom}", bool(vus), (vus[0][:150] if vus else f"motif « {motif} » absent des {len(trouves)} défaut(s)"))

    def poser(section, nom, champ, valeur):
        return lambda p, _: p[section][nom].__setitem__(champ, valeur)

    def oter(section, nom, champ=None):
        return (lambda p, _: p[section].pop(nom)) if champ is None else (lambda p, _: p[section][nom].pop(champ))

    def source_fausse(p, _):
        p["echantillonnage"]["temperature"]["sources"][0]["extrait"] = '"temperature": 0.7'

    def ligne_fausse(p, _):
        s = p["echantillonnage"]["temperature"]["sources"][0]
        chemin, ligne = s["ou"].rsplit(":", 1)
        s["ou"] = f"{chemin}:{int(ligne) + 1}"

    def piece_fausse(_, c):
        chemin = next(k for k, f in c["pieces_citees"].items() if f.get("sha256") and "commit" not in f)
        c["pieces_citees"][chemin]["sha256"] = "0" * 64

    def piece_absente(_, c):
        c["pieces_citees"].pop("requirements-cpu.txt")

    def piece_sans_empreinte(_, c):
        c["pieces_citees"]["requirements-cpu.txt"]["sha256"] = None

    def vecteur_faux(p, _):
        p["graines"]["vecteurs_d_essai"]["valeur"][0]["graines"][3] += 1

    def harnais_faux(p, _):
        fichiers = p["harnais"]["fichiers"]["valeur"]
        fichiers[sorted(fichiers)[-1]] = "f" * 64

    def programme_faux(p, _):
        p["gabarit_de_conversation"]["empreinte"]["methode"]["programme_sha256"] = "0" * 64

    def consigne_fausse(p, _):
        p["environnement"]["consigne_privee"]["valeur"]["consigne_honnete_T10_sha256"] = "0" * 64

    def champ_en_trop(p, _):
        p["environnement"]["forme_de_l_action"]["valeur"]["champs"].append("TOOL")

    def plafond_bas(_, c):
        c["coherence_avec_le_banc_ferme"]["plafonds"]["jetons_par_episode"] = 3999

    artefact("révision tronquée à 39 caractères", "révision", lambda p, _: p["modele"]["revision"].__setitem__(
        "valeur", p["modele"]["revision"]["valeur"][:39]))
    artefact("révision donnée par un nom de branche", "révision", poser("modele", "revision", "valeur", "main"))
    artefact("autre modèle", "changer de modèle", poser("modele", "nom", "valeur", "meta-llama/Llama-3.2-3B-Instruct"))
    artefact("adaptateur présent", "agent nu", poser("modele", "adaptateur", "valeur", "adaptateur de rang 8"))
    artefact("valeur sans source", "sans source", poser("echantillonnage", "temperature", "sources", []))
    artefact("mention « choix, à faire valider » retirée", "mention", oter("episode", "lot", "mention"))
    artefact("valeur nulle sans état", "valeur nulle sans état", poser("episode", "lot", "valeur", None))
    artefact("valeur de l'opérateur écrite dans le fichier", "doit rester nulle",
             poser("gabarit_de_conversation", "empreinte", "valeur", "a" * 64))
    artefact("valeur laissée à l'opérateur sans méthode", "sans méthode", oter("gabarit_de_conversation", "empreinte", "methode"))
    artefact("commit du harnais sans règle", "sans règle", poser("harnais", "commit", "regle", []))
    artefact("état posé sur une valeur qui doit être fixée", "inattendu", lambda p, _: p["echantillonnage"]["temperature"].update(
        {"valeur": None, "etat": OPERATEUR, "methode": "x", "champs_du_releve": ["x"], "ou_s_ecrit_la_valeur": "x"}))
    artefact("marqueur « À REMPLIR » dans une valeur", "marqueur", poser("pile_d_inference", "appareil", "valeur", "À REMPLIR"))
    artefact("entrée exigée absente (noyau)", "entrée exigée absente", oter("pile_d_inference", "noyau_attention"))
    artefact("noyau inconnu du harnais", "noyau", poser("pile_d_inference", "noyau_attention", "valeur", "flash"))
    artefact("précision des poids changée", "bfloat16", poser("pile_d_inference", "precision_des_poids", "valeur", "float16"))
    artefact("version de torch hors des dépendances figées", "pas de ligne", lambda p, _: p["pile_d_inference"]["versions"]["valeur"].__setitem__("torch", "2.14.0"))
    artefact("matériel sans règle d'égalité des deux postes", "règle d'égalité",
             poser("pile_d_inference", "materiel", "valeur", {"carte": "A100 SXM4 80 Go"}))
    artefact("température donnée en texte", "température", poser("echantillonnage", "temperature", "valeur", "1.0"))
    artefact("troncature de l'échantillonnage", "loi entière", poser("echantillonnage", "troncature", "valeur", "top-p 0,9"))
    artefact("cent pas par épisode", "plafond", poser("episode", "nombre_de_pas", "valeur", 100))
    artefact("deux mille jetons par action", "plafond", poser("echantillonnage", "jetons_par_action_max", "valeur", 2000))
    artefact("plafond de jetons par épisode du banc dépassé", "plafond", plafond_bas)
    artefact("outil exposé", "liste doit être vide", poser("outils", "outils_exposes", "valeur", ["lire_piece"]))
    artefact("champ d'action hors du code de l'environnement", "différents de ceux du code", champ_en_trop)
    artefact("consigne d'une autre empreinte", "consigne honnête", consigne_fausse)
    artefact("texte attendu sans la date du gabarit", "date figée", poser("gabarit_de_conversation", "texte_attendu_dans_l_ouverture", "valeur", "Today Date: 1 Jan 2025"))
    artefact("extrait absent de la ligne citée", "extrait", source_fausse)
    artefact("ligne citée décalée d'un rang", "extrait", ligne_fausse)
    artefact("pièce citée d'une autre empreinte", "introuvable à l'empreinte", piece_fausse)
    artefact("pièce citée absente de la table des pièces", "absente de « pieces_citees »", piece_absente)
    artefact("pièce sans empreinte qui n'est pas un document vivant", "pas dite vivante", piece_sans_empreinte)
    artefact("vecteur d'essai des graines altéré", "non reproduit", vecteur_faux)
    artefact("quantile incohérent avec la statistique", "quantile", poser("garde_d_equivalence", "quantile", "valeur", 0.9))
    artefact("couche hors du modèle", "couche", poser("enregistrement", "couches", "valeur", [7, 15, 40]))
    artefact("fichier du harnais d'une autre empreinte", "introuvable à l'empreinte", harnais_faux)
    artefact("programme de l'opérateur d'une autre empreinte", "programme de l'opérateur", programme_faux)

    try:
        charger('{"objet": "tronqué", "parametres": {')
    except ValueError as e:
        dire("artefact : fichier tronqué", "illisible" in str(e), str(e)[:100])
    else:
        dire("artefact : fichier tronqué", False, "aucun refus")

    lance = controler(config, racine, lancement=True)
    dire("cas sain : contrôle de lancement sur l'arbre de travail", not lance.defauts, f"{len(lance.defauts)} défaut(s)")
    faux = copy.deepcopy(config)
    harnais_faux(faux["parametres"], faux)
    vus = [quoi for _, quoi in controler(faux, racine, lancement=True).defauts if "contrôle de lancement" in quoi]
    dire("artefact : contrôle de lancement, fichier du harnais d'une autre empreinte", bool(vus),
         vus[0][:150] if vus else "aucun refus du contrôle de lancement")

    # relevé de l'opérateur : un relevé de synthèse, complet, puis trois artefacts
    methode = config["parametres"]["gabarit_de_conversation"]["empreinte"]["methode"]
    bon = {"mode": "reel", "configuration": {"sha256": sha_config}, "programme": {"sha256": methode["programme_sha256"]},
           "modele": {"nom": config["parametres"]["modele"]["nom"]["valeur"],
                      "revision": config["parametres"]["modele"]["revision"]["valeur"], "poids_releves": True,
                      "fichiers": {"tokenizer.json": {"octets": 1, "sha256": "1" * 64}}},
           "gabarit_de_conversation": {"gabarit_sha256": "2" * 64, "jetons_d_arret": [7, 9], "jetons_de_cloture": [9],
                                       "jeton_de_remplissage": 7,
                                       "conversation_de_controle": {"ids_sha256": "3" * 64, "texte_sha256": "4" * 64,
                                                                    "format_verifie": True},
                                       "texte_attendu_dans_l_ouverture": {"verifie": True}},
           "harnais": {"conforme_a_la_configuration": True}, "graines": {"conforme": True},
           "versions": {"python": "3.13.0", "torch_construction": "2.14.1+cu130", "torch_cuda": "13.0"},
           "versions_conformes_a_la_configuration": True}

    def relever(nom: str, motif: str | None, alterer=None) -> None:
        r = copy.deepcopy(bon)
        if alterer:
            alterer(r)
        c = Controle(config, racine)
        c.releve(r, sha_config)
        trouves = [quoi for _, quoi in c.defauts]
        if motif is None:
            dire(nom, not trouves, f"{len(trouves)} défaut(s)" + ("" if not trouves else f" : {trouves[0]}"))
        else:
            vus = [d for d in trouves if motif in d]
            dire(f"artefact : {nom}", bool(vus), vus[0][:150] if vus else f"motif « {motif} » absent")

    relever("cas sain : relevé de synthèse complet", None)
    relever("relevé au tokeniseur jouet", "jouet", lambda r: r.__setitem__("mode", "jouet"))
    relever("relevé d'une autre configuration", "autre configuration", lambda r: r["configuration"].__setitem__("sha256", "0" * 64))
    relever("relevé sans empreinte de la conversation de contrôle", "ids_sha256",
            lambda r: r["gabarit_de_conversation"]["conversation_de_controle"].pop("ids_sha256"))
    relever("relevé sans les fichiers de poids", "poids_releves", lambda r: r["modele"].__setitem__("poids_releves", False))
    # comparaison de deux relevés : le même relevé des deux côtés, puis deux artefacts
    bon.update({"environnement": {"guide_de_classification": {"sha256": "5" * 64}}})
    bon["harnais"]["fichiers"] = {"src/controle_ia/harnais/episode.py": "6" * 64}
    bon["versions"].update({"implementation": "CPython", "machine": "x86_64", "capacite_du_processeur": "AVX2",
                            "numpy": "2.4.6", "torch": "2.14.1", "transformers": "5.18.0", "tokenizers": "0.23.2",
                            "safetensors": "0.8.0", "huggingface_hub": "1.33.0", "jinja2": "3.1.6"})
    ecarts = comparer_deux_releves(bon, copy.deepcopy(bon))
    dire("cas sain : deux relevés identiques", not ecarts, f"{len(ecarts)} écart(s)" + ("" if not ecarts else f" : {ecarts[0]}"))
    autre = copy.deepcopy(bon)
    autre["gabarit_de_conversation"]["conversation_de_controle"]["ids_sha256"] = "9" * 64
    ecarts = comparer_deux_releves(bon, autre)
    dire("artefact : deux relevés, conversation de contrôle d'une autre empreinte",
         any("gabarit_de_conversation" in e for e in ecarts), ecarts[0][:150] if ecarts else "aucun écart vu")
    autre = copy.deepcopy(bon)
    autre["versions"]["capacite_du_processeur"] = "AVX512"
    ecarts = comparer_deux_releves(bon, autre)
    dire("artefact : deux relevés, processeur d'une autre capacité",
         any("capacite_du_processeur" in e for e in ecarts), ecarts[0][:150] if ecarts else "aucun écart vu")
    autre = copy.deepcopy(bon)
    autre["versions"].pop("jinja2")
    ecarts = comparer_deux_releves(bon, autre)
    dire("artefact : deux relevés, un champ absent d'un côté",
         any("absent d'un relevé" in e for e in ecarts), ecarts[0][:150] if ecarts else "aucun écart vu")
    print(f"épreuves : {'toutes réussies' if echecs == 0 else str(echecs) + ' échec(s)'}")
    return echecs


# ---------------------------------------------------------------- ligne de commande

def main(argv=None) -> int:
    ici = Path(__file__).resolve()
    ap = argparse.ArgumentParser(description="Validation de la configuration de génération du calage de G1.")
    ap.add_argument("--racine", default=str(ici.parents[3]), help="racine du dépôt (défaut : celle de ce programme)")
    ap.add_argument("--configuration", help="défaut : prereg/configuration-generation-calage-g1-v1.json sous la racine")
    ap.add_argument("--lancement", action="store_true", help="contrôle de lancement : harnais de l'arbre de travail exigé")
    ap.add_argument("--releve", help="relevé de l'opérateur à contrôler contre la configuration")
    ap.add_argument("--comparer", nargs=2, metavar=("RELEVE_A", "RELEVE_B"),
                    help="deux relevés (poste de calage, banc fermé) : chacun est contrôlé, puis leur égalité est exigée")
    ap.add_argument("--essai", action="store_true", help="épreuves du programme : cas sain et artefacts (R5)")
    a = ap.parse_args(argv)
    racine = Path(a.racine)
    chemin = Path(a.configuration) if a.configuration else racine / "prereg" / "configuration-generation-calage-g1-v1.json"
    if not chemin.is_file():
        print(f"REFUS : {chemin} absent sur disque", file=sys.stderr)
        return 1
    sha_config, defaut_compagnon = verifier_le_compagnon(chemin)
    try:
        config = charger(chemin.read_text(encoding="utf-8"))
    except ValueError as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 1
    if a.essai:
        return 0 if essai(config, racine, sha_config) == 0 else 1
    c = controler(config, racine, a.lancement)
    if defaut_compagnon:
        c.defaut(chemin.name, defaut_compagnon)
    lus = []
    for nom in ([a.releve] if a.releve else []) + list(a.comparer or []):
        r = Path(nom)
        if not r.is_file():
            c.defaut(f"relevé {r.name}", "absent sur disque")
            continue
        _, defaut_r = verifier_le_compagnon(r)
        if defaut_r:
            c.defaut(f"relevé {r.name}", defaut_r)
        try:
            releve = charger(r.read_text(encoding="utf-8"))
        except ValueError as e:
            c.defaut(f"relevé {r.name}", str(e))
            continue
        avant = len(c.defauts)
        c.releve(releve, sha_config)
        c.defauts[avant:] = [(f"relevé {r.name}", quoi) for _, quoi in c.defauts[avant:]]
        lus.append(releve)
    if a.comparer:
        if len(lus) != 2:
            c.defaut("comparaison", "les deux relevés n'ont pas pu être lus : rien n'est comparé")
        else:
            for ecart in comparer_deux_releves(lus[0], lus[1]):
                c.defaut("comparaison", ecart)
    for avis in c.avis:
        print(f"avis   | {avis}")
    for ou, quoi in c.defauts:
        print(f"défaut | {ou} | {quoi}")
    a_remplir = sorted(ou for ou, e in c.entrees() if isinstance(e, dict) and e.get("etat"))
    print(f"{chemin.name} ({sha_config})")
    print(f"{c.compte['entrees']} entrées, {c.compte['sources']} sources relues, {c.compte['pieces']} pièces à leur empreinte ; "
          f"{len(a_remplir)} valeur(s) à remplir hors du fichier : {', '.join(a_remplir)}")
    print("configuration valide" if not c.defauts else f"configuration refusée : {len(c.defauts)} défaut(s)")
    return 0 if not c.defauts else 1


if __name__ == "__main__":
    sys.exit(main())
